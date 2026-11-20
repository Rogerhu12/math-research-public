#!/usr/bin/env python3
"""Supplement only unpaid R665 cells with same-angle first-jet correlation.

Low angular modes use R656's rigorous finite-trig interval arcs. Every
remaining original Fourier coefficient and complete analytic-lift tail
is still paid. Already positive R665 cells are reused, not recalculated.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


PARENT_SHA='ec21d8575ad2d121d04beaa2b7ebc1902c0b7604c0dfaf8777610ad27f616200'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def make_reader(args):
    if sha(args.transfer_source)!=PARENT_SHA:
        raise ValueError('Use the complete published C1 transfer formulas')
    parent=load('C1_angle_transfer_parent',args.transfer_source)

    class AngularTransfer(parent.Transfer):
        def __init__(self):
            super().__init__(args.base,args.candidate,args.node_report,args.geometry_source,args.interval_source,
                args.difference_source,args.base_certificate,args.taylor_degree)
            self.prior=json.loads(args.prior_report.read_text())
            if (not self.prior['complete_scope'] or self.prior['source_sha256']!=PARENT_SHA
                    or self.prior['source_inputs']['candidate']['sha256']!=sha(args.candidate)
                    or self.prior['source_inputs']['base']['sha256']!=sha(args.base)
                    or self.prior['source_inputs']['base_certificate']['sha256']!=sha(args.base_certificate)
                    or [v['cell']for v in self.prior['records']]!=list(range(self.r.J-1))):
                raise ValueError('The prior paid cells must belong to this exact pair and old certificate')
            self.prior_records=self.prior['records'];self.reused=[];self.recomputed=[]
            self.paths.update(transfer_source=args.transfer_source,prior_report=args.prior_report)
            self.low_modes=args.low_modes;Q=args.angles
            if not 1<=self.low_modes<=self.r.M or Q<4 or Q&(Q-1) or Q<=4*self.low_modes:
                raise ValueError('Require a dyadic angular grid above the retained finite bandwidth')
            self.a=type(self.r).__new__(type(self.r))
            a,I=self.a,self.I
            a.I=I;a.M=self.low_modes;a.nu=2*np.arange(self.low_modes+1)
            a.Q=Q;a.transform=I.Transform(Q);a.angle_slice=slice(0,Q//4+1)
            a.step=I.div(I.exact(a.transform.pi_upper),I.exact(Q))
            a.halfstep2=I.scale(I.square(a.step),.5)
            a.discount=float(I.sub(I.exact(1.),I.scale(a.halfstep2,(2*self.low_modes)**2))[0])
            if a.discount<=0:raise ValueError('Need positive finite-mode oversampling discount')
            self.reuse_prior=args.cells=='unpaid'

        def field_boxes(self,definitions):
            I=self.I;L=self.low_modes
            groups={'cos':[],'sin':[]};positions={'cos':[],'sin':[]};remainders={'cos':[],'sin':[]}
            for name,(channels,parities,tail)in definitions.items():
                for k,(component,parity)in enumerate(zip(channels,parities)):
                    groups[parity].append(I.at(component,(slice(None),slice(0,L+1))))
                    coefficient_tail=I.sum_upper(I.absolute_upper(I.at(component,(slice(None),slice(L+1,None)))),axis=-1)
                    remainder=I.add(I.exact(coefficient_tail),I.exact(tail))[1]
                    remainders[parity].append(remainder);positions[parity].append((name,k))
            fields={name:[None,None,None]for name in definitions}
            for parity in ('cos','sin'):
                value=self.a.angle_boxes(I.stack(groups[parity]),parity)
                radius=np.asarray(remainders[parity])[...,None]
                value=I.down(value[0]-radius),I.up(value[1]+radius)
                for j,(name,k)in enumerate(positions[parity]):
                    fields[name][k]=value[0][j].min(axis=0),value[1][j].max(axis=0)
            return fields

        def cell(self,cell):
            if not 0<=cell<self.r.J-1:raise ValueError('Original cell out of range')
            if self.reuse_prior and self.prior_records[cell]['all_pieces_paid']:
                self.reused.append(cell)
                return dict(self.prior_records[cell],method='reused complete R665 global-angle bound')
            self.recomputed.append(cell)
            I,r=self.I,self.r;old=self.records[cell]
            h=r.width_box(r.nodes[cell],r.nodes[cell+1])
            base=r.hermite(I.at(self.basejets,cell),I.at(self.basejets,cell+1),h)
            delta=r.hermite(I.at(self.d.jets,cell),I.at(self.d.jets,cell+1),h)
            bd,dd=r.derivative(base,h),r.derivative(delta,h);pieces=[]
            for index,(left,right,u0,u1,active)in enumerate(r._cell_pieces(cell)):
                b,v,d,dv=[r.elevate(r.restrict(q,u0,u1))for q in (base,bd,delta,dd)]
                lift=r.lift_controls(left,right,active)
                fmax=float(I.absolute_upper(lift['f']).max());fpmax=float(I.absolute_upper(lift['fp']).max())
                deltaX=self.add_z0(self.channels(d,0),lift['chi'],self.d.height_difference)
                dx=self.tail_added(self.coefficient_norm(deltaX),fmax,self.delta_phase)
                bx=self.tail_added(self.coefficient_norm(deltaX,weighted=True),fmax,self.delta_phase)
                deltaV=self.add_z0(self.channels(dv,0),lift['cp'],self.d.height_difference)
                deltaT=self.channels(d,1)
                baseV=self.add_z0(self.channels(v,0),lift['cp'],self.H)
                baseV=self.add_horizontal(baseV,lift['fp'],self.er_cos,self.er_sin)
                baseT=self.add_horizontal(self.channels(b,1),lift['f'],I.neg(self.rhoer_sin),self.rhoer_cos)
                product=lambda x,y:float(I.mul(I.exact(x),I.exact(y))[1])
                phaseT=float(I.add(I.exact(self.delta_rho),I.mul(I.exact(self.rho_upper),I.exact(self.delta_phase)))[1])
                fields=self.field_boxes(dict(
                    V=(baseV,('cos','sin','cos'),product(fpmax,self.er_tail)),
                    T=(baseT,('sin','cos','sin'),product(fmax,self.rhoer_tail)),
                    dV=(deltaV,('cos','sin','cos'),product(fpmax,self.delta_phase)),
                    dT=(deltaT,('sin','cos','sin'),product(fmax,phaseT))))
                V,T,dV,dT=[fields[name]for name in ('V','T','dV','dT')]
                vmax,tmax,dvmax,dtmax=[I.sqrt(r.norm2(field))[1]for field in (V,T,dV,dT)]
                N=r.cross(T,V);N2a=r.norm2(N)
                N2b=I.sub(I.mul(r.norm2(V),r.norm2(T)),I.square(r.dot(V,T)))
                W2lo=np.maximum(old['minimum_normal_squared_lower'],np.maximum(N2a[0],N2b[0]))
                Wlo=I.sqrt(I.exact(W2lo))[0]
                eta=I.add(I.add(I.mul(I.exact(tmax),I.exact(dvmax)),
                    I.mul(I.exact(vmax),I.exact(dtmax))),I.mul(I.exact(dvmax),I.exact(dtmax)))[1]
                ratio=I.div(I.exact(eta),I.exact(Wlo))[1]
                newnormal=I.sub(I.exact(Wlo),I.exact(eta))[0]
                good=ratio<1
                support=np.full(ratio.shape,-np.inf)
                if np.any(good):
                    rt=I.exact(ratio[good]);s0=I.exact(old['support_lower'])
                    cosine=I.sqrt(I.sub(I.exact(1.),I.square(rt)))
                    tangent=I.sqrt(I.sub(I.exact(old['maximum_radius_squared_upper']),I.square(s0)))
                    support[good]=I.sub(I.sub(I.mul(s0,cosine),I.mul(tangent,rt)),I.exact(bx))[0]
                at=int(np.argmin(support));positive=bool(np.all(good)&np.all(support>0)&np.all(newnormal>0))
                pieces.append(dict(piece=index,active_lift=bool(active),position_difference_upper=dx,
                    weighted_position_difference_upper=bx,new_support_lower=float(support[at])if good[at]else None,
                    new_normal_lower=float(newnormal.min()),normal_ratio_upper=float(ratio.max()),
                    maximum_angle_local_velocity_difference=float(dvmax.max()),
                    maximum_angle_local_angular_difference=float(dtmax.max()),
                    worst_support_angle_grid_index=at,unpaid_angle_boxes=int(np.count_nonzero(~good|(support<=0))),
                    worst_angle_detail=dict(base_velocity_upper=float(vmax[at]),base_angular_upper=float(tmax[at]),
                        delta_velocity_upper=float(dvmax[at]),delta_angular_upper=float(dtmax[at]),
                        base_normal_lower=float(Wlo[at]),normal_difference_upper=float(eta[at]),normal_ratio_upper=float(ratio[at])),
                    support_paid=positive))
            return dict(cell=cell,pieces=pieces,method='same-angle finite-mode arcs with all tails paid',
                all_pieces_paid=all(p['support_paid']for p in pieces),
                support_lower=min((p['new_support_lower']for p in pieces if p['new_support_lower']is not None),default=None),
                normal_lower=min(p['new_normal_lower']for p in pieces),
                position_difference_upper=max(p['position_difference_upper']for p in pieces),
                maximum_normal_ratio_upper=max(p['normal_ratio_upper']for p in pieces))

    return AngularTransfer()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('base','candidate','node-report','geometry-source','interval-source','difference-source',
                'transfer-source','base-certificate','prior-report','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--cells',default='833');p.add_argument('--taylor-degree',type=int,default=8)
    p.add_argument('--angles',type=int,default=256);p.add_argument('--low-modes',type=int,default=24)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError('Keep prior signed results')
    np.seterr(over='raise',invalid='raise',divide='raise',under='ignore');started=time.monotonic()
    reader=make_reader(args)
    cells=list(range(reader.r.J-1))if args.cells=='unpaid'else[int(c)for c in args.cells.split(',')]
    report=reader.run(cells)
    report.update(schema='fullclosed-C1-same-angle-support-transfer-v2',source_sha256=sha(__file__),
        parent_source_sha256=sha(args.transfer_source),angles=args.angles,retained_finite_angle_modes=args.low_modes,
        angular_grid_created=True,original_all_modes_and_tails_paid=True,
        reused_prior_positive_cells=reader.reused,new_angle_correlated_cells=reader.recomputed,
        actual_same_candidate_new_first_jet_full_scan=False,
        all_unpaid_cells_supplemented=args.cells=='unpaid',seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in('records','covered_cells','reused_prior_positive_cells','new_angle_correlated_cells')}),flush=True)
    print(json.dumps(dict(event='C1_angle_transfer_returned',report_sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
