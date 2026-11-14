#!/usr/bin/env python3
"""Actual R33 nonmean metric defect, with complete angular tails.

This measures the geometry defect, not a Galerkin linear-solver residual.
A point report certifies all theta and the whole requested affine parameter
interval, but only its explicitly stated radial points. A nonzero interval
is a continuous radial certificate on one exact common scalar germ.
The target is diag(mean(|F_r|^2), a^2); reflection makes mean(F_r.F_theta)=0.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_cap_parameter_comparison import ParameterDiskBody
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_bulk_box import CBox, Box, zeros, cstack, cdot, reduce_box
from fourfold_phase_beta_interval import ball_record

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, doc):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(doc, indent=2, allow_nan=False)+"\n").encode()
    if path.suffix == ".gz":
        data = gzip.compress(data, mtime=0)
    temporary = path.with_suffix(path.suffix+".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)

def upper(value):
    return arb(float(np.max(value.magnitude_upper()))).upper()

def positive_real(value, name):
    z = value.to_acb()
    if not z.imag.contains(0) or not z.real > 0:
        raise ValueError("unresolved positive real "+name)
    return z.real

def record(value):
    return ball_record(arb(value))

class MetricDefectTarget(ParameterDiskBody):
    def __init__(self, object_path, half_width, nodes):
        super().__init__(object_path, Fraction(1,10000), False, nodes, 2*nodes)
        self.offset = acb(arb(0, exact_arb(Fraction(half_width))))
        self.real_parameter = True
        self.metric_half_width = Fraction(half_width)
        self.metric_tail_strip = arb(1)/32

    def scalar_jets_and_fourier(self, radial):
        P, a = self.unit_finite_data(radial)
        _, _, a, z = self.last_scalar
        F = []
        for j in range(4):
            v = zeros((self.nodes,3))
            for h in range(j+1):
                v = v+math.comb(j,h)*a[j-h]*P[h]
            v[0,0] = v[0,0]+a[j]
            v[0,2] = v[0,2]+z[j]
            F.append(v)
        frequency = np.asarray(self.frequency)
        Y = []
        for j in range(3):
            v = F[j]*CBox(0.,Box(frequency[:,None]))
            v[:,0] = v[:,0]-F[j][:,1]
            v[:,1] = v[:,1]+F[j][:,0]
            Y.append(v)
        E = self.unit_tail_errors(radial,self.metric_tail_strip)[0]
        errorsF = []
        for j in range(4):
            row = []
            for q in range(4):
                tail = arb(0)
                for h in range(j+1):
                    primitive = (math.factorial(h)/self.tail_radius**h
                        *math.factorial(q)*(4/self.metric_tail_strip)**q*E)
                    tail += math.comb(j,h)*upper(a[j-h])*primitive
                row.append(tail.upper())
            errorsF.append(row)
        errorsY = [[(errorsF[j][q]+errorsF[j][q+1]).upper()
                    for q in range(3)] for j in range(3)]
        return F,Y,a,errorsF,errorsY,E

    def finite_norm(self, value, order):
        n = value.real.lo.shape[0]
        frequency = 4*np.asarray([k if k<n//2 else k-n for k in range(n)])
        weights = np.abs(frequency).astype(float)**order
        values = Box(value.magnitude_upper())
        if values.lo.ndim > 1:
            weights = weights[:,None]
        reduced = reduce_box(values*Box(weights))
        return arb(float(np.max(reduced.hi))).upper()

    def prepare_product(self,value):
        n = 2*self.nodes
        full = zeros((n,3))
        indices = (np.asarray(self.frequency)//4)%n
        full[indices] = value
        constant = value[0]
        full[0] = 0
        samples = self.fast_fourier.fft(full,inverse=True)*n
        return full,samples,constant

    def product(self,left,right):
        a,sa,ca = left
        b,sb,cb = right
        n = a.real.lo.shape[0]
        result = self.fast_fourier.fft(cdot(sa,sb))/n
        result = result+cdot(a,cb)+cdot(b,ca)
        result[0] = result[0]+cdot(ca,cb)
        return result

    @staticmethod
    def product_error(Ma,Ea,Mb,Eb,q):
        total = arb(0)
        for h in range(q+1):
            total += 3*math.comb(q,h)*(Ma[h]*Eb[q-h]
                +Mb[q-h]*Ea[h]+Ea[h]*Eb[q-h])
        return total.upper()

    def metric_budget(self,left,right):
        radial=acb(real_interval(left,right))
        F,Y,a,EF,EY,primitive_tail=self.scalar_jets_and_fourier(radial)
        MF=[[self.finite_norm(v,q) for q in range(3)] for v in F]
        MY=[[self.finite_norm(v,q) for q in range(3)] for v in Y]
        PF=[self.prepare_product(v) for v in F]
        PY=[self.prepare_product(v) for v in Y]
        cache={}
        def pp(family,i,j):
            key=family,i,j
            if key not in cache:
                cache[key]=self.product(PF[i],PF[j] if family=="FF" else PY[j])
            return cache[key]
        fe,fb,ee,eb=[],[],[],[]
        for i in range(3):
            e=zeros((2*self.nodes,)); b=zeros((2*self.nodes,))
            for h in range(i+1):
                e=e+math.comb(i,h)*pp("FF",h+1,i-h+1)
                b=b+math.comb(i,h)*pp("FY",h+1,i-h)
            fe.append(e);fb.append(b)
            efee=[];bfee=[]
            for q in range(3-i):
                xe=arb(0);xb=arb(0)
                for h in range(i+1):
                    xe += math.comb(i,h)*self.product_error(
                        MF[h+1],EF[h+1],MF[i-h+1],EF[i-h+1],q)
                    xb += math.comb(i,h)*self.product_error(
                        MF[h+1],EF[h+1],MY[i-h],EY[i-h],q)
                efee.append(xe.upper());bfee.append(xb.upper())
            ee.append(efee);eb.append(bfee)
        mean=[]
        for i in range(3):
            z=fe[i][0].to_acb()
            if not z.imag.contains(0):
                raise ValueError("the real mean metric derivative lost reality")
            mean.append(z.real+arb(0,ee[i][0]))
            fe[i][0]=0
            # The true mixed mean is exactly zero by angular reflection.
            # The finite product has the same symmetry. Keep a check.
            if not (fb[i][0].to_acb()+acb(arb(0,eb[i][0]),arb(0,eb[i][0]))).contains(0):
                raise ValueError("the exact mixed angular mean lost zero")
            fb[i][0]=0
        if not mean[0] > 0:
            raise ValueError("true mean radial metric positivity unresolved")
        aa=[a[j].to_acb().real for j in range(3)]
        if not aa[0] > 0:
            raise ValueError("true physical radius positivity unresolved")
        rawE={};rawB={}
        for i in range(3):
            for q in range(3-i):
                key=f"{i},{q}"
                rawE[key]=(self.finite_norm(fe[i],q)+ee[i][q]).upper()
                rawB[key]=(self.finite_norm(fb[i],q)+eb[i][q]).upper()
        E,E1,E2=mean
        A=[1/E,-E1/(E*E),2*E1*E1/(E**3)-E2/(E*E)]
        t=1/(aa[0]*E.sqrt())
        l=-aa[1]/aa[0]-E1/(2*E)
        lp=-aa[2]/aa[0]+(aa[1]/aa[0])*(aa[1]/aa[0])-E2/(2*E)+(E1/E)*(E1/E)/2
        B=[t,t*l,t*(l*l+lp)]
        normalized={}
        for i in range(3):
            for q in range(3-i):
                x=sum((math.comb(i,h)*abs(A[i-h])*rawE[f"{h},{q}"]
                       for h in range(i+1)),arb(0))
                y=sum((math.comb(i,h)*abs(B[i-h])*rawB[f"{h},{q}"]
                       for h in range(i+1)),arb(0))
                normalized[f"{i},{q}"]=(x*x+2*y*y).sqrt().upper()
        N=lambda i,q:normalized[f"{i},{q}"]
        ka=abs(aa[1]/(aa[0]*E.sqrt())).upper()
        ks=abs(aa[2]/(aa[0]*E)-aa[1]*aa[1]/(aa[0]*aa[0]*E)
               -aa[1]*E1/(2*aa[0]*E*E)).upper()
        nabla1=(N(1,0)/E.sqrt()).upper()
        nabla2=(N(0,1)/aa[0]+2*ka*N(0,0)).upper()
        H11=(N(2,0)/E+abs(E1)/(2*E*E)*N(1,0)).upper()
        H12=(N(1,1)/(aa[0]*E.sqrt())+ka*N(0,1)/aa[0]
              +2*ks*N(0,0)+2*ka*N(1,0)/E.sqrt()).upper()
        H21=(N(1,1)/(aa[0]*E.sqrt())+ka*N(0,1)/aa[0]
              +2*ka*N(1,0)/E.sqrt()+2*ka*ka*N(0,0)).upper()
        H22=(N(0,2)/(aa[0]*aa[0])+4*ka*N(0,1)/aa[0]
              +4*ka*ka*N(0,0)+ka*N(1,0)/E.sqrt()).upper()
        C1=(nabla1*nabla1+nabla2*nabla2).sqrt().upper()
        C2=(H11*H11+H12*H12+H21*H21+H22*H22).sqrt().upper()
        return dict(exact_radial_interval=list(map(str,(left,right))),
            exact_scalar_germ=list(map(str,self.cell)),
            whole_angular_circle=True,
            metric_target="diag(mean_theta(|F_r|^2),a^2); exact mixed mean zero",
            mean_radial_metric_jets_0_2=list(map(record,mean)),
            radius_jets_0_2=list(map(record,aa)),
            complete_physical_coordinate_derivative_A0=dict(
                nonmean_rr={k:record(v) for k,v in rawE.items()},
                mixed_rtheta={k:record(v) for k,v in rawB.items()},
                thetatheta_exactly_zero=True),
            frame_component_derivative_bounds={k:record(v) for k,v in normalized.items()},
            intrinsic_target_metric_C012=list(map(record,(N(0,0),C1,C2))),
            intrinsic_definition="Hilbert-Schmidt point norms of h=g_F-g0 and its first two g0-covariant derivatives, using g0-orthonormal frames; this is not a finite angular sample norm.",
            complete_primitive_A_sigma_error=record(primitive_tail),
            full_metric_product_remainders=dict(
                rr=[[record(v) for v in row] for row in ee],
                rtheta=[[record(v) for v in row] for row in eb]),
            limitations=["Only the stated radial interval; no unlisted radial coverage.",
                         "A finite bound is not a smallness or Newton convergence certificate."])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--points",type=Fraction,nargs="+")
    p.add_argument("--left",type=Fraction)
    p.add_argument("--right",type=Fraction)
    p.add_argument("--bits",type=int,default=192)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec,ctx.cap=args.bits,4
    started=time.monotonic()
    obj,_,_,delta=load_definition(args.object)
    target=MetricDefectTarget(args.object,args.half_width,args.nodes)
    common=common_cells(target)
    requested=([(v,v) for v in args.points] if args.points else [(args.left,args.right)])
    if any(a is None or b is None or a>b for a,b in requested):
        raise ValueError("supply points or a valid continuous interval")
    doc=dict(kind="actual_R33_geometry_metric_defect",complete=False,
        whole_closed_surface_defect_complete=False,
        source_sha256=sha(__file__),object_sha256=sha(args.object),
        origin_sha256=obj["origin_inputs"]["sha256"],direction_sha256=obj["direction"]["sha256"],
        exact_center=str(delta),exact_half_width=str(args.half_width),
        exact_parameter_interval=[str(delta-args.half_width),str(delta+args.half_width)],
        primitive_nodes=args.nodes,bits=args.bits,rows=[],
        mathematical_scope="Complete theta and entire affine parameter interval on exactly the listed radial domains.")
    save(args.out,doc)
    for left,right in requested:
        index=min(len(common)-2,bisect_right(common,(left+right)/2)-1)
        span=common[index:index+2]
        if not span[0]<=left<=right<=span[1]:
            raise ValueError("a requested interval crosses an exact scalar knot")
        target.set_cell(*span)
        row=target.metric_budget(left,right)
        doc["rows"].append(row)
        doc["wall_seconds"]=time.monotonic()-started
        save(args.out,doc)
        print(json.dumps(dict(r=list(map(str,(left,right))),
            C012=[v["mid_float"] for v in row["intrinsic_target_metric_C012"]],
            seconds=doc["wall_seconds"])),flush=True)
    doc.update(complete=True,wall_seconds=time.monotonic()-started,
        dependency_sha256={n:sha(Path(__file__).with_name(n)) for n in (
            "fourfold_phase_cap_parameter_comparison.py","fourfold_phase_cap_scaled_body.py",
            "fourfold_phase_beta_affine.py","fourfold_phase_beta_parameter_germ.py",
            "fourfold_phase_beta_bulk_interval.py","fourfold_phase_beta_bulk_box.py",
            "fourfold_phase_beta_interval.py","fourfold_phase_root_interval.py",
            "fourfold_phase_uniform_tail.py")})
    save(args.out,doc)

if __name__=="__main__":
    main()
