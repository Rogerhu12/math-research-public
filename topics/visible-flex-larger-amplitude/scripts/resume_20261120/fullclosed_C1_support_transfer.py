#!/usr/bin/env python3
"""Cheap continuous C1/support transfer from an already certified closed map.

No angular grid. Exact Hermite differences combine Delta Z0+chi Delta H
and their derivatives. Base V/T bounds combine a finite Taylor-Laurent
circle lift with the original modes, retaining all Fourier and Taylor tails.
Each old certified cell supplies support, normal and radius bounds. A sharp
normal-cone estimate transfers immersion and positive-flow support.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np


DIFFERENCE_SHA='f3b5acf135589c2ad6f10c80bebf7dfdf919350d4b06e9dbb764ba2a2ca0ade0'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


class Transfer:
    def __init__(self,base,candidate,node_report,geometry_source,interval_source,
                 difference_source,base_certificate,taylor_degree=8):
        if sha(difference_source)!=DIFFERENCE_SHA:
            raise ValueError('Use the published full C0 exact-field reader')
        module=load('C1_transfer_exact_difference',difference_source)
        self.d=module.Difference(base,candidate,node_report,geometry_source,interval_source)
        self.r,self.I=self.d.r,self.d.I
        r,I=self.r,self.I;r.nu=2*np.arange(r.M+1)
        self.certificate=json.loads(Path(base_certificate).read_text())
        C=self.certificate
        if (not C['complete_scope'] or not C['embedding_certified']
                or C['metadata']['bundle_sha256']!=sha(base)
                or C['metadata']['node_report_sha256']!=sha(node_report)
                or C['geometry_source_sha256']!=sha(geometry_source)
                or C['metadata']['interval_source_sha256']!=sha(interval_source)
                or C['unpaid_immersion_boxes']!=0
                or [v['cell']for v in C['records']]!=list(range(r.J-1))):
            raise ValueError('Require the same exact base and its complete first-jet certificate')
        self.records=C['records'];self.beta=F(C['metadata']['beta_exact'])
        if not F(0)<self.beta<=F(1):raise ValueError('The present normal cone bound uses 0<beta<=1')
        self.paths=dict(self.d.paths,difference_source=Path(difference_source),base_certificate=Path(base_certificate))
        q=self.d.base['qjets'];self.basejets=q.copy(),q.copy()
        core=I.at(self.basejets,(0,0,slice(1,r.M+1)))
        nu=2*np.arange(1,r.M+1)
        T=I.scale(core,-nu)
        self.basejets[0][0,0,r.M+1:2*r.M+1]=T[0]
        self.basejets[1][0,0,r.M+1:2*r.M+1]=T[1]
        self.H=r.fraction(F(float(self.d.base['Hcap'])))
        self.phase=I.div(I.scale(core,1-nu*nu),I.exact(nu))
        rho_coeff=I.scale(core,1-nu*nu)
        self.rho_upper=float(I.add(I.exact(1.),I.exact(I.sum_upper(I.absolute_upper(rho_coeff))))[1])
        self.base_phase_l1=float(I.sum_upper(I.absolute_upper(self.phase)))
        self.same_core=bool(np.array_equal(q[0,0,1:r.M+1],self.d.candidate['qjets'][0,0,1:r.M+1]))
        self.delta_phase=0. if self.same_core else self.d.phase_difference_upper
        self.delta_rho=0. if self.same_core else self.d.rho_difference_upper
        self.taylor_degree=int(taylor_degree)
        if self.taylor_degree<1:raise ValueError('Use at least one Taylor term')
        self._prepare_lift(rho_coeff)

    def convolution(self,a,b):
        I=self.I
        out=np.zeros(len(a[0])+len(b[0])-1),np.zeros(len(a[0])+len(b[0])-1)
        for j in range(len(b[0])):
            sl=slice(j,j+len(a[0]))
            value=I.add(I.at(out,sl),I.mul(a,I.at(b,j)))
            out[0][sl],out[1][sl]=value
        return out

    def _cos_sin(self,laurent):
        I=self.I;center=(len(laurent[0])-1)//2
        C=[I.at(laurent,center)];S=[I.exact(0.)]
        for j in range(1,center+1):
            p,m=I.at(laurent,center+j),I.at(laurent,center-j)
            C.append(I.add(p,m));S.append(I.sub(p,m))
        return I.stack(C),I.stack(S)

    def _split_coefficients(self,C,S):
        I,M=self.I,self.r.M
        Ctail=float(I.sum_upper(I.absolute_upper(I.at(C,slice(M+1,None)))))
        Stail=float(I.sum_upper(I.absolute_upper(I.at(S,slice(M+1,None)))))
        tail=float(I.sqrt(I.add(I.square(I.exact(Ctail)),I.square(I.exact(Stail))))[1])
        return I.at(C,slice(0,M+1)),I.at(S,slice(0,M+1)),tail

    def _prepare_lift(self,rho_coeff):
        I,r=self.I,self.r;M=r.M
        a=np.zeros(2*M+1),np.zeros(2*M+1)
        half=I.scale(self.phase,.5)
        for j in range(1,M+1):
            a[0][M+j],a[1][M+j]=I.at(half,j-1)
            a[0][M-j],a[1][M-j]=I.neg(I.at(half,j-1))
        term=I.exact(np.array([1.]));total=I.exact(np.array([1.]))
        for order in range(1,self.taylor_degree+1):
            term=I.div(self.convolution(term,a),I.exact(order))
            total=I.add((np.pad(total[0],(M,M)),np.pad(total[1],(M,M))),term)
        C,S=self._cos_sin(total)
        self.er_cos,self.er_sin,self.er_fourier_tail=self._split_coefficients(C,S)
        rho=np.zeros(2*M+1),np.zeros(2*M+1)
        rho[0][M]=rho[1][M]=1.
        half=I.scale(rho_coeff,.5)
        for j in range(1,M+1):
            rho[0][M+j],rho[1][M+j]=I.at(half,j-1)
            rho[0][M-j],rho[1][M-j]=I.at(half,j-1)
        C,S=self._cos_sin(self.convolution(total,rho))
        self.rhoer_cos,self.rhoer_sin,self.rhoer_fourier_tail=self._split_coefficients(C,S)
        remainder=I.exact(1.)
        for _ in range(self.taylor_degree+1):
            remainder=I.mul(remainder,I.exact(self.base_phase_l1))
        self.taylor_remainder=float(I.mul(remainder,r.fraction(F(1,math.factorial(self.taylor_degree+1))))[1])
        self.er_tail=float(I.add(I.exact(self.er_fourier_tail),I.exact(self.taylor_remainder))[1])
        self.rhoer_tail=float(I.add(I.exact(self.rhoer_fourier_tail),
            I.mul(I.exact(self.rho_upper),I.exact(self.taylor_remainder)))[1])

    def channels(self,controls,order):
        return [a for a,_ in self.r.channels(controls,order)]

    def add_z0(self,channels,scalar,height):
        I=self.I;Z=channels[2][0].copy(),channels[2][1].copy()
        v=I.add(I.at(Z,(slice(None),0)),I.mul(scalar,height))
        Z[0][:,0],Z[1][:,0]=v;return [channels[0],channels[1],Z]

    def coefficient_norm(self,channels,weighted=False):
        I=self.I
        sizes=[]
        for j,component in enumerate(channels):
            if weighted and j==2:component=I.mul(component,self.r.fraction(self.beta))
            sizes.append(I.exact(I.sum_upper(I.absolute_upper(component),axis=-1)))
        norm=I.sqrt(I.add(I.add(I.square(sizes[0]),I.square(sizes[1])),I.square(sizes[2])))
        return float(norm[1].max())

    def add_horizontal(self,channels,scalar,C,S):
        I=self.I;scalar=scalar[0][:,None],scalar[1][:,None]
        return [I.add(channels[0],I.mul(scalar,(C[0][None,:],C[1][None,:]))),
                I.add(channels[1],I.mul(scalar,(S[0][None,:],S[1][None,:]))),channels[2]]

    def tail_added(self,base,amplitude,tail):
        I=self.I
        return float(I.add(I.exact(base),I.mul(I.exact(amplitude),I.exact(tail)))[1])

    def cell(self,cell):
        if not 0<=cell<self.r.J-1:raise ValueError('Original cell index out of range')
        I,r=self.I,self.r;old=self.records[cell]
        h=r.width_box(r.nodes[cell],r.nodes[cell+1])
        base=r.hermite(I.at(self.basejets,cell),I.at(self.basejets,cell+1),h)
        delta=r.hermite(I.at(self.d.jets,cell),I.at(self.d.jets,cell+1),h)
        bd,dd=r.derivative(base,h),r.derivative(delta,h)
        pieces=[]
        for index,(left,right,u0,u1,active) in enumerate(r._cell_pieces(cell)):
            b,v,d,dv=[r.elevate(r.restrict(q,u0,u1))for q in (base,bd,delta,dd)]
            lift=r.lift_controls(left,right,active)
            fmax=float(I.absolute_upper(lift['f']).max());fpmax=float(I.absolute_upper(lift['fp']).max())
            deltaX=self.add_z0(self.channels(d,0),lift['chi'],self.d.height_difference)
            deltaV=self.add_z0(self.channels(dv,0),lift['cp'],self.d.height_difference)
            dx=self.tail_added(self.coefficient_norm(deltaX),fmax,self.delta_phase)
            bx=self.tail_added(self.coefficient_norm(deltaX,weighted=True),fmax,self.delta_phase)
            dV=self.tail_added(self.coefficient_norm(deltaV),fpmax,self.delta_phase)
            analytic_T=float(I.add(I.exact(self.delta_rho),I.mul(I.exact(self.rho_upper),I.exact(self.delta_phase)))[1])
            dT=self.tail_added(self.coefficient_norm(self.channels(d,1)),fmax,analytic_T)
            baseV=self.add_z0(self.channels(v,0),lift['cp'],self.H)
            baseV=self.add_horizontal(baseV,lift['fp'],self.er_cos,self.er_sin)
            Vmax=self.tail_added(self.coefficient_norm(baseV),fpmax,self.er_tail)
            baseT=self.add_horizontal(self.channels(b,1),lift['f'],I.neg(self.rhoer_sin),self.rhoer_cos)
            Tmax=self.tail_added(self.coefficient_norm(baseT),fmax,self.rhoer_tail)
            normal_delta=I.add(I.add(I.mul(I.exact(Tmax),I.exact(dV)),
                I.mul(I.exact(Vmax),I.exact(dT))),I.mul(I.exact(dV),I.exact(dT)))
            eta=float(normal_delta[1]);W=float(I.sqrt(I.exact(old['minimum_normal_squared_lower']))[0])
            t=float(I.div(I.exact(eta),I.exact(W))[1])
            normal_lower=float(I.sub(I.exact(W),I.exact(eta))[0])
            support=None
            if t<1:
                cosine=I.sqrt(I.sub(I.exact(1.),I.square(I.exact(t))))
                s0=I.exact(old['support_lower'])
                tangent=I.sqrt(I.sub(I.exact(old['maximum_radius_squared_upper']),I.square(s0)))
                support=float(I.sub(I.sub(I.mul(s0,cosine),I.mul(tangent,I.exact(t))),I.exact(bx))[0])
            minimum_speed=float(I.sub(I.sqrt(I.exact(old['minimum_E_lower'])),I.exact(dV))[0])
            pieces.append(dict(piece=index,active_lift=bool(active),position_difference_upper=dx,
                weighted_position_difference_upper=bx,velocity_difference_upper=dV,angular_difference_upper=dT,
                base_velocity_upper=Vmax,base_angular_upper=Tmax,normal_difference_upper=eta,
                base_normal_lower=W,normal_ratio_upper=t,new_normal_lower=normal_lower,
                new_support_lower=support,new_speed_lower=minimum_speed,
                support_paid=bool(support is not None and support>0 and normal_lower>0)))
        return dict(cell=cell,pieces=pieces,all_pieces_paid=all(p['support_paid']for p in pieces),
            support_lower=min((p['new_support_lower']for p in pieces if p['new_support_lower']is not None),default=None),
            normal_lower=min(p['new_normal_lower']for p in pieces),
            position_difference_upper=max(p['position_difference_upper']for p in pieces),
            maximum_normal_ratio_upper=max(p['normal_ratio_upper']for p in pieces))

    def run(self,cells):
        I,r=self.I,self.r;records=[self.cell(c)for c in cells]
        full=cells==list(range(r.J-1))
        H=r.fraction(F(float(self.d.candidate['Hcap'])))
        cap_support=float(I.mul(r.fraction(self.beta),H)[0])
        paid=all(v['all_pieces_paid']for v in records)
        support=min(cap_support,*(v['support_lower']for v in records)) if paid else None
        rho=float(I.sub(I.exact(self.certificate['metadata']['core_rho_continuous_lower']),I.exact(self.delta_rho))[0])
        epsilon=max(float(r.fraction(abs(self.d.height_difference_exact))[1]),*(v['position_difference_upper']for v in records))
        D=float(I.add(I.exact(self.certificate['diameter_upper']),I.scale(I.exact(epsilon),2))[1])if full else None
        return dict(schema='fullclosed-C1-normal-cone-support-transfer-v1',source_sha256=sha(__file__),
            source_inputs={name:dict(path=str(path.resolve()),sha256=sha(path))for name,path in self.paths.items()},
            base_core_same_as_candidate=self.same_core,beta_exact=str(self.beta),taylor_degree=self.taylor_degree,
            base_phase_l1_upper=self.base_phase_l1,base_rho_absolute_upper=self.rho_upper,
            circle_taylor_remainder_upper=self.taylor_remainder,er_fourier_tail_upper=self.er_fourier_tail,
            rhoer_fourier_tail_upper=self.rhoer_fourier_tail,delta_phase_upper=self.delta_phase,delta_rho_upper=self.delta_rho,
            covered_cells=cells,complete_scope=full,all_covered_cells_paid=paid,
            cap_support_lower=cap_support,covered_support_lower=support,new_core_rho_lower=rho,
            new_minimum_normal_lower=min(v['normal_lower']for v in records),complete_diameter_upper=D,
            all_body_C0_difference_upper=epsilon if full else None,
            embedding_certified=bool(full and paid and support>0 and rho>0),
            embedding_proof='R650 positive-flow projection, original exact closed C2 sphere; all caps and reflected side included',
            curvature_or_reach_certified=False,metric_certified=False,
            angular_grid_created=False,radial_subdivisions=0,full_analytic_lift_and_all_modes_retained=True,
            exact_base_control_cancellation_and_all_remainders_paid=True,
            arithmetic='f512 outward binary64; Fraction input; all finite Laurent tails retained through l1 plus real-phase Taylor remainder',
            records=records,worst_support_cells=sorted(records,key=lambda z:float('-inf')if z['support_lower']is None else z['support_lower'])[:8])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('base','candidate','node-report','geometry-source','interval-source','difference-source','base-certificate','out'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--cells',default='905');parser.add_argument('--taylor-degree',type=int,default=8)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError('Keep the original transfer report')
    np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
    start=time.monotonic()
    reader=Transfer(args.base,args.candidate,args.node_report,args.geometry_source,args.interval_source,
        args.difference_source,args.base_certificate,args.taylor_degree)
    cells=list(range(reader.r.J-1))if args.cells=='all'else[int(c)for c in args.cells.split(',')]
    report=reader.run(cells);report['seconds']=time.monotonic()-start
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in ('records','covered_cells')}),flush=True)
    print(json.dumps(dict(event='C1_support_transfer_returned',report_sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
