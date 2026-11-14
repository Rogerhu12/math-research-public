#!/usr/bin/env python3
"""Directed physical-angle cap coefficients and complete radial remainders.

The background is the explicit exact continuous value repair of ac1.  The
physical coefficients Q_B=2u and Q_C=-u^2-K(2s dv+dv^2) are composed with
the genuine inverse angle.  A directed FFT is used only after that inverse
has been enclosed at every quadrature node.  Complete analytic alias and
Fourier-tail bounds, in the joint coefficient-supremum Wiener algebra,
are then added.  A third radial jet pays every point of the closed cell.
No physical Fourier truncation is treated as the actual coefficient.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from dataclasses import dataclass
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from flint import arb, ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_final_continuous_value_repair import iter_repair
from fourfold_codazzi_full_body_graft_target_jets import ReciprocalFullTargetJets
from fourfold_codazzi_reciprocal_continuous_residual_v3 import (
    add, mul, scale, polynomial_at_affine, centre_real, target_model)
from fourfold_phase_beta_bulk_box import (
    Box, CBox, zeros, DirectedFFT, arb_box, reduce_box, complex_sincos)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

CURRENT='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
KIND='actual_continuous_repaired_physical_cap_full_coefficient_jets_v1'


def ffrac(value):return Fraction.from_float(float(value))


def bsum(value):
    return arb(float(reduce_box(Box(value.abs_upper())).hi)).upper()


def csum(value):
    return arb(float(reduce_box(Box(value.magnitude_upper())).hi)).upper()


def point_series(cube,knot,left,right):
    """Taylor coefficients at a variable real point of the whole cell."""
    rr=arb_box(exact_arb(left-knot).union(exact_arb(right-knot)))
    out=[]
    for n in range(4):
        value=Box(np.zeros(cube.shape[-1]))
        for j in range(4-n):
            degree=3-j
            value=value*rr+Box(cube[j])*math.comb(degree,n)
        out.append(value)
    return out


def series_inverse(values):
    out=[values[0].reciprocal()]
    for n in range(1,len(values)):
        out.append(-out[0]*sum((values[j]*out[n-j] for j in range(1,n+1)),Box(0.)))
    return out


def positive_product(a,b,n=4):
    return [sum((a[j]*b[k-j] for j in range(max(0,k-len(b)+1),min(k,len(a)-1)+1)),arb(0)).upper()
            for k in range(min(n,len(a)+len(b)-1))]


def weighted_amplitude_norm(values,frequencies,width,order=0):
    weights=arb_box(exact_arb(width))*Box(frequencies)
    # Arb exponentiation is scalar and exact-input directed; no libm exp.
    ww=Box(np.asarray([float((exact_arb(width)*int(k)).exp().lower()) for k in frequencies]),
           np.asarray([float((exact_arb(width)*int(k)).exp().upper()) for k in frequencies]))
    # The conversion to double is widened by the canonical Arb bridge.
    ww=Box(np.asarray([arb_box((exact_arb(width)*int(k)).exp()).lo for k in frequencies]),
           np.asarray([arb_box((exact_arb(width)*int(k)).exp()).hi for k in frequencies]))
    return bsum(values*ww*Box(np.asarray(frequencies,dtype=float)**order))


@dataclass
class FourierBudget:
    coefficients:list
    norm:arb
    error:arb
    analytic_taylor_norms:list
    detailed_error:dict


class PhysicalCapCoefficientJets:
    def __init__(self,candidate,object_path,repair_report,*,half_width=Fraction(1,10**9),
                 width=Fraction(1,16),angles=512,cutoff=128,nodes=512):
        self.candidate=Path(candidate);self.object_path=Path(object_path)
        self.repair_report=Path(repair_report);self.width=Fraction(width)
        self.N=int(angles);self.cutoff=int(cutoff);self.half_width=Fraction(half_width)
        if sha(self.candidate)!=CURRENT:raise ValueError('the complete original final centre is required')
        if self.N&(self.N-1) or self.N<=2*self.cutoff or self.cutoff<32:
            raise ValueError('a complete directed angular grid and explicit cutoff are required')
        self.saved=load_candidate(self.candidate);meta=json.loads(str(self.saved['metadata']))
        self.alpha=Fraction(meta['exact_float_amplitude']);self.nu=Fraction(meta['exact_float_nu'])
        if int(meta['modes'])!=32 or self.saved['piece_coefficients'].shape!=(4,6144,65):
            raise ValueError('all original 6144 cubics and 65 states are required')
        self.mc=32;self.knots=list(map(ffrac,self.saved['radial_nodes']))
        report=json.loads(gzip.decompress(self.repair_report.read_bytes()))
        if not report.get('complete') or report.get('derived_definition_sha256')!=REPAIR:
            raise ValueError('the exact complete continuous repair is required')
        encoded=(json.dumps(report['definition'],sort_keys=True,separators=(',',':'))+'\n').encode()
        if hashlib.sha256(encoded).hexdigest()!=REPAIR:raise ValueError('derived definition changed')
        digest=hashlib.sha256();lower=[];upper=[]
        for piece,offset,jump in iter_repair(self.saved,self.alpha):
            digest.update((json.dumps(dict(piece=piece,physical_offset=list(map(str,offset))),
                                      sort_keys=True,separators=(',',':'))+'\n').encode())
            row=[arb_box(exact_arb(v)) for v in offset]
            lower.append([float(v.lo) for v in row]);upper.append([float(v.hi) for v in row])
        if digest.hexdigest()!=report['definition']['offset_sequence_sha256']:
            raise ValueError('all exact physical offsets must match')
        self.offsets=Box(np.array(lower),np.array(upper))
        self.target=ReciprocalFullTargetJets(object_path,self.half_width,nodes)
        self.fft=DirectedFFT();seed=zeros((self.N,self.mc))
        for j in range(self.mc):seed[j+1,j]=1.
        self.roots=self.fft.fft(seed,inverse=True)*self.N
        self.freq=4*np.arange(1,self.mc+1)
        self.cosfreq=np.r_[0,self.freq]
        self.dependency_names=(
            'fourfold_codazzi_final_continuous_value_repair.py',
            'fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_full_body_graft_target_jets.py',
            'fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_root_interval.py',
            'fourfold_codazzi_reciprocal_continuous_residual_v3.py')

    def local_jets(self,piece,left,right,target):
        row=point_series(self.saved['piece_coefficients'][:,piece],self.knots[piece],left,right)
        al=arb_box(exact_arb(self.alpha));u=[];dv=[];s=[];K=[]
        for n in range(4):
            a=row[n]*al
            if n==0:a=a+self.offsets[piece]
            u.append(a[:self.mc]);dv.append(a[self.mc:])
            s.append(arb_box(target['s'+(str(n) if n else '')]/math.factorial(n)))
            K.append(arb_box(target['K'+(str(n) if n else '')]/math.factorial(n)))
        mean=[s[n]+dv[n][0] for n in range(4)]
        if not float(mean[0].hi)<0:raise ValueError('the actual moving mean must stay negative')
        inv=series_inverse(mean)
        psi=[sum((dv[j][1:]*inv[n-j]/Box(self.freq) for j in range(n+1)),Box(np.zeros(self.mc)))
             for n in range(4)]
        return dict(u=u,dv=dv,s=s,K=K,mean=mean,psi=psi)

    def analytic_bounds(self,jets):
        """Joint sum_m sup_(r,eta), not sup_(r,eta) sum_m."""
        double=2*self.width
        def norms(series,freq):
            return [[weighted_amplitude_norm(series[n],freq,double,j)
                     for j in range(4-n)] for n in range(4)]
        P=norms(jets['psi'],self.freq);U=norms(jets['u'],self.freq)
        V=norms(jets['dv'],self.cosfreq)
        if not P[0][0]<exact_arb(self.width):raise ValueError('full analytic inverse displacement is unresolved')
        if not P[0][1]<1:raise ValueError('full analytic inverse contraction is unresolved')
        inv=1/(1-P[0][1]);x1=(P[1][0]*inv).upper()
        x2=((P[2][0]+P[1][1]*x1+P[0][2]*x1*x1/2)*inv).upper()
        x3=((P[3][0]+P[2][1]*x1+P[1][1]*x2+P[1][2]*x1*x1/2
             +P[0][2]*x1*x2+P[0][3]*x1**3/6)*inv).upper()
        def compose(T):
            return [T[0][0],
                (T[1][0]+T[0][1]*x1).upper(),
                (T[2][0]+T[1][1]*x1+T[0][1]*x2+T[0][2]*x1*x1/2).upper(),
                (T[3][0]+T[2][1]*x1+T[1][1]*x2+T[1][2]*x1*x1/2
                 +T[0][1]*x3+T[0][2]*x1*x2+T[0][3]*x1**3/6).upper()]
        uu,vv=compose(U),compose(V)
        ss=[arb(float(x.abs_upper())).upper() for x in jets['s']]
        kk=[arb(float(x.abs_upper())).upper() for x in jets['K']]
        vv2=positive_product(vv,vv);sv=positive_product(ss,vv)
        qt=positive_product(kk,[(2*x+y).upper() for x,y in zip(sv,vv2)])
        u2=positive_product(uu,uu)
        qb=[(2*x).upper() for x in uu]
        qc=[(x+y).upper() for x,y in zip(u2,qt)]
        return dict(QB=qb,QC=qc,psi=P[0][0],psi_phi=P[0][1],
                    inverse_radial_Taylor=[x1,x2,x3],mean_gap=arb(float(-jets['mean'][0].hi)).lower())

    def trig(self,x):
        ss,cc=complex_sincos(CBox(x.reshape(self.N,1)*Box(self.freq).reshape(1,self.mc)))
        ee=self.roots*CBox(cc.real,ss.real)
        return ee.imag,ee.real

    def sine(self,coeff,trig,order=0):
        sn,cs=trig
        base=(sn,cs,-sn,-cs)[order%4]
        return reduce_box(base*coeff.reshape(1,self.mc)*Box(self.freq**order).reshape(1,self.mc),1)

    def cosine(self,coeff,trig,order=0):
        sn,cs=trig
        base=(cs,-sn,-cs,sn)[order%4]
        value=reduce_box(base*coeff[1:].reshape(1,self.mc)*Box(self.freq**order).reshape(1,self.mc),1)
        return value+coeff[0] if order==0 else value

    def inverse_samples(self,jets,analytic):
        # A floating root is just a centre for an explicit directed bracket.
        coeff=(jets['psi'][0].lo+jets['psi'][0].hi)/2
        theta=np.arange(self.N)*np.pi/(2*self.N);x=np.zeros(self.N)
        for _ in range(12):
            phase=(theta+x)[:,None]*self.freq
            value=x+np.sin(phase)@coeff
            deriv=1+np.cos(phase)@(coeff*self.freq)
            x-=value/deriv
        radius=2.**-34;accepted=False
        for _ in range(10):
            left=np.nextafter(x-radius,-np.inf);right=np.nextafter(x+radius,np.inf)
            low=Box(left)+self.sine(jets['psi'][0],self.trig(Box(left)))
            high=Box(right)+self.sine(jets['psi'][0],self.trig(Box(right)))
            if np.all(low.hi<0) and np.all(high.lo>0):accepted=True;break
            radius*=8
        if not accepted:raise ValueError('directed inverse-angle endpoint signs failed')
        X=Box(left,right)
        for _ in range(4):
            mid=np.minimum(np.maximum(X.lo/2+X.hi/2,X.lo),X.hi)
            F=Box(mid)+self.sine(jets['psi'][0],self.trig(Box(mid)))
            J=1+self.sine(jets['psi'][0],self.trig(X),1)
            if not np.all(J.lo>0):raise ValueError('real inverse-angle derivative lost positivity')
            Z=Box(mid)-F/J
            X=Box(np.maximum(X.lo,Z.lo),np.minimum(X.hi,Z.hi))
        trig=self.trig(X);J=1+self.sine(jets['psi'][0],trig,1)
        phi1=-self.sine(jets['psi'][1],trig)/J
        phi2=-(self.sine(jets['psi'][2],trig)
               +phi1*self.sine(jets['psi'][1],trig,1)
               +phi1*phi1*self.sine(jets['psi'][0],trig,2)/2)/J
        def composed(series,evaluate):
            f0=evaluate(series[0],trig)
            f1=evaluate(series[1],trig)+phi1*evaluate(series[0],trig,1)
            f2=evaluate(series[2],trig)+phi1*evaluate(series[1],trig,1)
            f2=f2+phi2*evaluate(series[0],trig,1)+phi1*phi1*evaluate(series[0],trig,2)/2
            return [f0,f1,f2]
        u=composed(jets['u'],self.sine);v=composed(jets['dv'],self.cosine)
        uv2=mul(u,u);vv2=mul(v,v);sv=mul(jets['s'][:3],v)
        qc=mul(jets['K'][:3],add(scale(sv,2),vv2))
        QB=scale(u,2);QC=[-uv2[j]-qc[j] for j in range(3)]
        block=zeros((self.N,6))
        for j in range(3):block[:,2*j]=CBox(QB[j]);block[:,2*j+1]=CBox(QC[j])
        dft=self.fft.fft(block)/self.N
        return dft,dict(inverse_bracket_radius=radius,
            maximum_final_inverse_width=float(np.max((X.hi-X.lo))),
            minimum_node_J_lower=float(np.min(J.lo)))

    def fourier_model(self,dft,norms,half,component):
        selected=[];rounding=arb(0);alias=arb(0);tail=arb(0);h=exact_arb(half)
        for j in range(3):
            raw=dft[:,2*j+component];centre=zeros((self.N,));fee=arb(0)
            if component==1:
                value=raw.real[0];point,error=centre_real(value)
                centre[0]=CBox(point);fee+=arb(float(error.abs_upper())).upper()
            for k in range(1,self.cutoff+1):
                if component==0:
                    pos,neg=raw.imag[k],-raw.imag[-k]
                else:pos,neg=raw.real[k],raw.real[-k]
                value=Box(max(float(pos.lo),float(neg.lo)),min(float(pos.hi),float(neg.hi)))
                point,error=centre_real(value);fee+=2*arb(float(error.abs_upper())).upper()
                if component==0:
                    centre[k]=CBox(0.,point);centre[-k]=CBox(0.,-point)
                else:centre[k]=CBox(point);centre[-k]=CBox(point)
            scaled=centre*arb_box(h**j)
            cr,er=centre_real(scaled.real);ci,ei=centre_real(scaled.imag)
            chosen=CBox(cr,ci);fee_scale=bsum(er)+bsum(ei)
            selected.append(chosen)
            rounding+=(h**j*fee+fee_scale).upper()
            # One aggregate alias sum: no spurious factor 2K+1 is needed.
            alias+=(h**j*norms[j]*(-4*exact_arb(self.width)*(self.N-self.cutoff)).exp()).upper()
            tail+=(h**j*norms[j]*(-4*exact_arb(self.width)*(self.cutoff+1)).exp()).upper()
        radial=(h**3*norms[3]).upper()
        finite=sum((csum(c) for c in selected),arb(0)).upper()
        error=(rounding+alias+tail+radial).upper()
        return FourierBudget(selected,finite,error,norms,
            dict(directed_interval_and_model_rounding=rounding,full_quadrature_alias=alias,
                 full_unretained_physical_Fourier_tail=tail,complete_third_radial_Taylor_remainder=radial))

    def coefficients(self,left,right):
        left,right=Fraction(left),Fraction(right)
        if not Fraction(9,10)<=left<right<=Fraction(25,8):raise ValueError('outside the proved actual physical cap')
        piece=bisect_right(self.knots,left)-1
        if not self.knots[piece]<=left<right<=self.knots[piece+1]:
            raise ValueError('a coefficient cell crosses an original candidate cubic')
        whole,germ=self.target.coefficients(left,right,self.nu)
        mid=(left+right)/2;half=(right-left)/2
        centre,midgerm=self.target.coefficients(mid,mid,self.nu)
        if germ!=midgerm:raise ValueError('the same actual scalar germ is required')
        wholejets=self.local_jets(piece,left,right,whole)
        centjets=self.local_jets(piece,mid,mid,centre)
        analytic=self.analytic_bounds(wholejets)
        dft,sample=self.inverse_samples(centjets,analytic)
        models={name:self.fourier_model(dft,analytic[name],half,j)
                for j,name in enumerate(('QB','QC'))}
        scalar={name:target_model(centre,whole,name,half) for name in ('gamma','beta','K','s')}
        return dict(models=models,scalar=scalar,whole=whole,centre=centre,analytic=analytic,
                    sample=sample,piece=piece,germ=germ,left=left,right=right,half=half)

    def row(self,result):
        return dict(interval=list(map(str,(result['left'],result['right']))),
            candidate_piece=result['piece'],actual_scalar_germ=list(map(str,result['germ'])),
            physical_coefficient_models={name:dict(finite_A0=record(value.norm),
                complete_joint_A0_error=record(value.error),
                physical_radial_Taylor_analytic_norms=[record(v) for v in value.analytic_taylor_norms],
                complete_error_terms={k:record(v) for k,v in value.detailed_error.items()})
                for name,value in result['models'].items()},
            analytic_inverse={k:record(result['analytic'][k]) for k in ('psi','psi_phi','mean_gap')},
            actual_directed_node_inversion=result['sample'],
            all_original_target_coefficients={k:record(v) for k,v in result['whole'].items()})


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--repair-report',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--left',type=Fraction,default=Fraction(9,10));ap.add_argument('--width',type=Fraction,default=Fraction(1,100000))
    ap.add_argument('--strip',type=Fraction,default=Fraction(1,16));ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    ap.add_argument('--angles',type=int,default=512);ap.add_argument('--cutoff',type=int,default=128)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve each actual coefficient attempt')
    doc=dict(kind=KIND,complete=False,source_sha256=sha(__file__),failure=None,rows=[],
        base_candidate_sha256=CURRENT,continuous_centre_definition_sha256=REPAIR,
        parameter_half_width=str(args.half_width),physical_analytic_width=str(args.strip),
        angular_quadrature_nodes=args.angles,physical_coefficient_cutoff=args.cutoff,
        joint_norm='sum over all physical Fourier modes of sup over the whole closed r,eta cell',
        full_inverse_angle_and_alias_and_infinite_tail_retained=True,
        whole_cap_graph_or_body_inverse_claimed=False)
    try:
        provider=PhysicalCapCoefficientJets(args.candidate,args.object,args.repair_report,
                    half_width=args.half_width,width=args.strip,angles=args.angles,cutoff=args.cutoff)
        p=bisect_right(provider.knots,args.left)-1
        end=min(args.left+args.width,provider.knots[p+1],
                next(x for x in provider.target.cuts if x>args.left))
        result=provider.coefficients(args.left,end);doc['rows'].append(provider.row(result))
        doc.update(complete=True,inputs={str(p):sha(p) for p in (args.candidate,args.object,args.repair_report)},
            dependency_sha256={n:sha(Path(__file__).with_name(n)) for n in provider.dependency_names})
    except Exception as error:doc['failure']=dict(type=type(error).__name__,message=str(error))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(json.dumps(dict(complete=doc['complete'],failure=doc['failure'],wall_seconds=doc['wall_seconds'])),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
