#!/usr/bin/env python3
"""Native scalar-time DFT evaluation of the exact symbolic retarget reference.

Every Fourier mode of U, Q and the static initial correction is retained.
Products are formed at the actual points, not projected to the grid's degree.
Negative Fourier coefficients conjugate the *time-polynomial coefficients*,
never the evaluated positive coefficient at a nonreal time.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
from flint import arb, acb, acb_poly, ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_retarget_reference_jets import (
    RetargetReference, segment_arrays, scalar_time_coefficients, time_value,
)


class RealTimeFourier:
    """Finite function real on real time and real normalized label x."""
    def __init__(self, positive_time_coefficients):
        self.coefficients = [[acb(v) for v in row] for row in positive_time_coefficients]
        self.terms = len(self.coefficients)
        if self.terms < 1 or not self.coefficients[0]:
            raise ValueError('nonempty finite time/Fourier coefficients required')
        self.K = len(self.coefficients[0])-1
        if any(len(row)!=self.K+1 or not row[0].imag==0 for row in self.coefficients):
            raise ValueError('inconsistent finite Fourier degree or nonreal mean')
        self.polynomials=[]
        for k in range(-self.K,self.K+1):
            values=[row[abs(k)].conjugate() if k<0 else row[k] for row in self.coefficients]
            self.polynomials.append(acb_poly(values))
        self.derivatives=[p.derivative() for p in self.polynomials]
        self._weights={}

    def norms(self,width):
        """Complete per-time-coefficient A_width and first derivative bounds."""
        s=exact_arb(width)
        weights=[arb(1)]+[2*(k*s).exp() for k in range(1,self.K+1)]
        zero=[];first=[]
        for row in self.coefficients:
            zero.append(sum((abs(v)*w for v,w in zip(row,weights)),arb(0)).upper())
            first.append(sum((k*abs(v)*weights[k] for k,v in enumerate(row)),arb(0)).upper())
        imaginary_zero=(2*sum((abs(self.coefficients[0][k])*(k*s).sinh()
                              for k in range(1,self.K+1)),arb(0))).upper()
        return zero,first,imaginary_zero

    def grid(self,u,count,width=Fraction(0)):
        if count<1:raise ValueError('positive number of finite evaluation points required')
        width=Fraction(width)
        key=(width,ctx.prec)
        if key not in self._weights:
            s=exact_arb(width)
            self._weights[key]=[(-k*s).exp() for k in range(-self.K,self.K+1)]
        weights=self._weights[key]
        rows=[[acb(0) for _ in range(count)] for _ in range(3)]
        for k,p,dp,w in zip(range(-self.K,self.K+1),self.polynomials,self.derivatives,weights):
            value=p(u)*w;position=k%count
            rows[0][position]+=value
            rows[1][position]+=dp(u)*w
            rows[2][position]+=acb(0,k)*value
        return [[count*v for v in acb.dft(row,inverse=True)] for row in rows]


class NativeRetargetSegment:
    def __init__(self,reference,leg,segment,left=Fraction(0),right=Fraction(1)):
        if not isinstance(reference,RetargetReference):
            raise ValueError('validated symbolic retarget reference required')
        if leg not in ('forward','backward') or not 0<=left<right<=1:
            raise ValueError('invalid oriented reference subsegment')
        self.reference,self.leg,self.segment=reference,leg,segment
        self.left,self.right=left,right
        bp,base=reference.base[leg];qp,q=reference.Q[leg]
        real,imag,brow=segment_arrays(bp,base,segment,['U','L'])
        qr,qi,qrow=segment_arrays(qp,q,segment,['Qtilde'])
        self.U=RealTimeFourier(scalar_time_coefficients(real[:,0,:],imag[:,0,:],left,right))
        self.Q=RealTimeFourier(scalar_time_coefficients(qr,qi,left,right))
        self.a=RealTimeFourier(reference.a)
        self.end=RealTimeFourier(reference.forward_end) if leg=='backward' else None
        endpoints=base['exact_time_endpoints'][segment:segment+2]
        a,b=map(time_value,endpoints)
        ta=a+(b-a)*exact_arb(left);tb=a+(b-a)*exact_arb(right)
        self.center,self.h=(ta+tb)/2,(tb-ta)/2
        if not base['time_orientation']*self.h>0:
            raise ValueError('reference local coordinate has wrong time orientation')
        self.identity=dict(retarget_descriptor_sha256=sha(reference.path),leg=leg,segment=segment,
            normalized_subspan=[str(left),str(right)],exact_segment_time_rows=endpoints,
            branch_sign=base['trace_identity']['sign'],base_shard=brow,Q_shard=qrow,
            old_exact_delta_fraction=reference.doc['old_exact_delta_fraction'],
            target_exact_delta_fraction=reference.doc['target_exact_delta_fraction'],
            target_object_sha256=reference.doc['target_object']['sha256'],
            target_root_sha256=reference.doc['target_root']['sha256'])
        self._static={}

    def static_grid(self,count,width):
        key=(count,Fraction(width),ctx.prec)
        if key not in self._static:
            a,_,ax=self.a.grid(acb(0),count,width)
            if self.end is not None:
                e,_,ex=self.end.grid(acb(0),count,width)
                a,ax=[v*w for v,w in zip(e,a)],[v*w+x*y for v,w,x,y in zip(ex,a,e,ax)]
            self._static[key]=a,ax
        return self._static[key]

    def grid(self,u,count,width=Fraction(0)):
        U,Uu,Ux=self.U.grid(u,count,width)
        Q,Qu,Qx=self.Q.grid(u,count,width)
        a,ax=self.static_grid(count,width)
        s=exact_arb(width);pi=arb.pi()
        labels=[acb(2*pi*j/count,s) for j in range(count)]
        Y=[z/4+v+w*b for z,v,w,b in zip(labels,U,Q,a)]
        Yu=[v+w*b for v,w,b in zip(Uu,Qu,a)]
        Yx=[arb(1)/4+v+w*b+c*d for v,w,b,c,d in zip(Ux,Qx,a,Q,ax)]
        return Y,Yu,Yx

    def bounds(self,time_radius,label_width):
        """Full finite bounds; no true field or nonzero q inference."""
        R=exact_arb(time_radius);s=exact_arb(label_width)
        if not R>=1 or not s>=0:raise ValueError('outer time disk and nonnegative strip required')
        U,Ux,IU=self.U.norms(label_width)
        Q,Qx,IQ=self.Q.norms(label_width)
        a,ax,Ia=self.a.norms(label_width);B,Bx,IB=a[0],ax[0],Ia
        if self.end is not None:
            e,ex,Ie=self.end.norms(label_width)
            B,Bx,IB=e[0]*B,ex[0]*B+e[0]*Bx,Ie*B+e[0]*IB
        C=[v+w*B for v,w in zip(U,Q)]
        Cx=[v+w*B+z*Bx for v,w,z in zip(Ux,Qx,Q)]
        mean_time_image=IU+IQ*B+Q[0]*IB
        image=(s/4+mean_time_image+sum((R**i*C[i] for i in range(1,len(C))),arb(0))).upper()
        q_change=sum((R**i*Cx[i] for i in range(1,len(Cx))),arb(0)).upper()
        return dict(
            normalized_time_radius=str(time_radius),normalized_initial_label_strip=str(label_width),
            physical_theta_image_strip=image,
            q_difference_from_real_time_center=q_change,
            full_q_modulus=(arb(1)/4+sum((R**i*v for i,v in enumerate(Cx)),arb(0))).upper(),
            full_Yu_modulus=sum((i*R**(i-1)*C[i] for i in range(1,len(C))),arb(0)).upper(),
            periodic_Y_modulus=sum((R**i*v for i,v in enumerate(C)),arb(0)).upper(),
            static_correction_modulus=B.upper(),static_correction_derivative_modulus=Bx.upper())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path,default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--leg',choices=('forward','backward'),default='forward')
    p.add_argument('--segment',type=int,default=419)
    p.add_argument('--nodes',type=int,default=8192)
    p.add_argument('--label-width',default='1/512')
    p.add_argument('--outer-label-width',default='1/64')
    p.add_argument('--time-real',default='1/2');p.add_argument('--time-imag',default='1/8')
    p.add_argument('--time-radius',default='6');p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    reference=RetargetReference(args.descriptor)
    model=NativeRetargetSegment(reference,args.leg,args.segment)
    u=acb(exact_arb(Fraction(args.time_real)),exact_arb(Fraction(args.time_imag)))
    tick,cpu=time.monotonic(),time.process_time()
    Y,Yu,Yx=model.grid(u,args.nodes,Fraction(args.label_width))
    timing=dict(seconds=time.monotonic()-tick,cpu_seconds=time.process_time()-cpu)
    checks=[];hx=arb(1)/65536
    for j in sorted({0,args.nodes//7,args.nodes//3,args.nodes-1}):
        label=acb(2*arb.pi()*j/args.nodes,exact_arb(Fraction(args.label_width)))
        (direct,_),_,_,_,_=reference.jets(args.leg,args.segment,Fraction(0),Fraction(1),
            label,hx,8,2,exact_arb(Fraction(args.time_radius)),arb(1))
        expected=[acb_poly([direct.coefficient(i,0) for i in range(8)])(u),
                  acb_poly([i*direct.coefficient(i,0) for i in range(1,8)])(u),
                  acb_poly([direct.coefficient(i,1)/hx for i in range(8)])(u)]
        actual=[Y[j],Yu[j],Yx[j]]
        if not all(a.real.overlaps(b.real) and a.imag.overlaps(b.imag) for a,b in zip(actual,expected)):
            raise ValueError('native finite reference grid disagrees with direct symbolic jets')
        checks.append(dict(node=j,all_Y_Yu_Yx_direct_jet_checks_passed=True))
    bounds=model.bounds(Fraction(args.time_radius),Fraction(args.outer_label_width))
    report=dict(kind='exact_symbolic_retarget_reference_native_scalar_grid',complete=True,
        source_sha256=sha(__file__),identity=model.identity,bits=args.bits,nodes=args.nodes,
        input_time=dict(real=args.time_real,imaginary=args.time_imag),label_width=args.label_width,
        timing=timing,full_finite_outer_bounds={k:ball_record(v) if isinstance(v,arb) else v for k,v in bounds.items()},
        independent_direct_symbolic_checks=checks,
        limitations=['Finite reference evaluation only, not a true flow or residual certificate.',
                     'No q lower bound or field-image inclusion is inferred automatically.'])
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(complete=True,timing=timing,bounds=report['full_finite_outer_bounds'])),flush=True)


if __name__=='__main__':main()
