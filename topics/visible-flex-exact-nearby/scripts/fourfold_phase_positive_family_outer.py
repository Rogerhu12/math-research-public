#!/usr/bin/env python3
"""True affine-family positive body with the radial curvature cancellation removed.

The infinite unit-tangent chart is unchanged.  We subtract its exact circular
tangent before the directed FFT and retain both the finite part and its true
analytic Fourier tail.  This gives E=a_r^2+Z_r^2+e without subtracting two large
interval expressions when the physical radius becomes small.  This program
certifies a finite regular-to-regular positive component, not an exterior cap.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import gzip
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_bulk_box import (
    CBox, Box, zeros, cstack, cdot, trig_jets, jet_product,
    arb_box, reduce_box)
from fourfold_phase_beta_interval import primitive_fourier_budget, ball_record
from fourfold_phase_beta_parameter_germ import ParameterGermFastBulkTarget, provenance, sha
from fourfold_phase_actual_positive_cap import PositiveCapTarget, real_range, stored_upper
from fourfold_phase_uniform_tail import up


class StablePositiveFamily(ParameterGermFastBulkTarget):
    geometry = PositiveCapTarget.geometry

    def finite_data(self, radial):
        delta = CBox.from_acb(radial-acb(self.anchor))
        jet = zeros((4, 2*self.modes+2))
        for n in range(20, -1, -1):
            jet = jet*delta+cstack([self.scalar_poly[n], jet[0], 2*jet[1], 3*jet[2]])
        beta, gamma = jet[:, :self.modes], jet[:, self.modes:2*self.modes]
        radius, height = jet[:, -2], jet[:, -1]
        self.last_scalar = beta, gamma, radius, height
        b = (beta.reshape(4,self.modes,1)*self.fast_sines.reshape(1,self.modes,self.nodes)).sum(1)
        g = (gamma.reshape(4,self.modes,1)*self.fast_sines.reshape(1,self.modes,self.nodes)).sum(1)
        sb, _ = trig_jets(b)
        sg, _ = trig_jets(g)
        shb, _ = trig_jets(b/2)
        shg, _ = trig_jets(g/2)
        cmb, cmg = -2*jet_product(shb,shb), -2*jet_product(shg,shg)
        one = zeros((4,self.nodes)); one[0] = 1
        # cos(gamma)cos(beta)-1 is evaluated through exact half-angle squares.
        tangent_difference = cstack([
            -jet_product(one+cmg,sb), cmg+cmb+jet_product(cmg,cmb), sg],-1)
        coefficient = self.fast_fourier.fft(tangent_difference,1)/self.nodes
        primitive = zeros((4,self.nodes,3))
        n = np.asarray(self.frequency)
        ii = CBox(0.,Box(n.reshape(1,-1)))
        denominator = Box((1-n*n).reshape(1,-1))
        primitive[:,:,0] = (ii*coefficient[:,:,0]+coefficient[:,:,1])/denominator
        primitive[:,:,1] = (-coefficient[:,:,0]+ii*coefficient[:,:,1])/denominator
        nz = np.flatnonzero(n)
        primitive[:,nz,2] = coefficient[:,nz,2]/CBox(0.,Box(n[nz].reshape(1,-1)))
        primitive[:,self.nodes//2,:] = 0
        primitive[:,0,1],primitive[:,0,2] = 0,0
        pos = np.arange(1,self.nodes//2)
        for j,parity in enumerate((1,-1,1)):
            value = (primitive[:,pos,j]+parity*primitive[:,-pos,j])/2
            primitive[:,pos,j],primitive[:,-pos,j] = value,parity*value
        primitive = jet_product(primitive,radius.reshape(4,1,1))
        self.last_difference_primitive = primitive
        full = primitive+zeros(primitive.real.lo.shape)
        full[:,0,0] = full[:,0,0]+radius
        full[:,0,2] = full[:,0,2]+height
        return full,radius

    def tail_errors(self, radial, inner_sigma=arb(0)):
        rho = arb_box(abs(radial-acb(self.anchor)).upper()+self.tail_radius).hi
        bounds = np.zeros(2*self.modes+2)
        for n in range(20,-1,-1):
            bounds = up(up(bounds*rho)+self.scalar_abs[n])
        phase = sum(((arb(float(bounds[j]))+arb(float(bounds[self.modes+j])))
                    *(self.tail_sigma*(j+1)).cosh() for j in range(self.modes)),arb(0)).upper()
        key=inner_sigma.str(35)
        if key not in self.tail_factor_cache:
            self.tail_factor_cache[key] = primitive_fourier_budget(
                self.nodes,self.tail_sigma,inner_sigma,self.tail_radius,arb(1),arb(0),arb(1))[0]
        # T(beta,gamma)-T(0,0)=int_0^1 d_s T(s beta,s gamma) ds.
        # Each rotating component is bounded by phase*exp(phase), uniformly
        # on the true scalar germ disk and the larger normalized angle strip.
        factor = arb(float(bounds[-2]))*phase*phase.exp()
        return [(x*factor).upper() for x in self.tail_factor_cache[key]]

    def complete_fast_data(self, radial):
        coefficient,radius = self.finite_data(radial)
        difference = self.last_difference_primitive
        errors = self.tail_errors(radial)
        reverse=(-np.arange(self.nodes))%self.nodes
        dx,dy,dz=difference[1],difference[2],difference[3]
        ar,arr,arrr=radius[1],radius[2],radius[3]
        _,_,_,height=self.last_scalar
        zr,zrr,zrrr=height[1],height[2],height[3]
        e0=2*ar*dx[0,0]+cdot(dx,dx[reverse]).sum()
        e1=2*arr*dx[0,0]+2*ar*dy[0,0]+2*cdot(dx,dy[reverse]).sum()
        e2=(2*arrr*dx[0,0]+4*arr*dy[0,0]+2*ar*dz[0,0]
            +2*(cdot(dy,dy[reverse])+cdot(dx,dz[reverse])).sum())
        eps=[arb_box(math.factorial(j)*errors[0]/self.tail_radius**j) for j in range(4)]
        B=[Box(np.max(reduce_box(Box(difference[j].magnitude_upper())).hi)) for j in range(4)]
        arabs,arrabs,arrrabs=[Box(float(np.max(v.magnitude_upper()))) for v in (ar,arr,arrr)]
        fees=[2*arabs*eps[1]+3*(2*B[1]*eps[1]+eps[1]*eps[1]),
              2*arrabs*eps[1]+2*arabs*eps[2]+6*(B[1]*eps[2]+B[2]*eps[1]+eps[1]*eps[2]),
              2*arrrabs*eps[1]+4*arrabs*eps[2]+2*arabs*eps[3]
              +6*(2*B[2]*eps[2]+eps[2]*eps[2]+B[1]*eps[3]+B[3]*eps[1]+eps[1]*eps[3])]
        real=radial.imag==0
        e0,e1,e2=[v.pad(f,real) for v,f in zip((e0,e1,e2),fees)]
        E0=ar*ar+zr*zr+e0
        E1=2*ar*arr+2*zr*zrr+e1
        N=2*zr*(ar*zrr-arr*zr)+ar*e1-2*arr*e0
        Np=(2*zrr*(ar*zrr-arr*zr)+2*zr*(ar*zrrr-arrr*zr)
            +ar*e2-arr*e1-2*arrr*e0)
        K=N/(2*radius[0]*E0*E0)
        Kp=Np/(2*radius[0]*E0*E0)-K*(ar/radius[0]+2*E1/E0)
        if real:
            K,Kp=CBox(K.real),CBox(Kp.real)
        self.last_stable_diagnostics=dict(E=real_range(E0) if real else None,
            e=real_range(e0) if real else None,
            e_radial=real_range(e1) if real else None,
            E_correction_errors=[float(f.hi) for f in fees])
        return coefficient,K,Kp,errors,real

    def evaluate_positive(self,left,right,sigma):
        radial=acb(real_interval(left,right))
        coefficient,K,Kp,errors,real=self.complete_fast_data(radial)
        krange=real_range(K)
        if not krange[0]>0:
            raise ValueError('true target curvature has no positive lower bound')
        real_geometry=self.geometry(radial,coefficient,errors,arb(0))
        complex_geometry=self.geometry(radial,coefficient,errors,sigma)
        return dict(radial_interval=[str(left),str(right)],K=krange,Kprime=real_range(Kp),
                    stable_target=self.last_stable_diagnostics,
                    real_geometry=real_geometry,complex_geometry=complex_geometry,
                    primitive_errors=[ball_record(x) for x in errors])


def aggregate(rows,left,right,sigma):
    # Integrate each local Lipschitz bound; a remote small radius does not
    # multiply a worst core constant by the full body length.
    lr,lc=arb(0),arb(0)
    amin,amax,bmin,bmax,ac,bc=[],[],[],[],[],[]
    for row in rows:
        a,b=map(Fraction,row['radial_interval']);length=exact_arb(b-a)
        real,comp=row['real_geometry'],row['complex_geometry']
        lr+=length*max(arb(abs(x)) for x in real['drift_theta'])
        lc+=length*stored_upper(comp['drift_theta_modulus'])
        amin.append(arb(real['alpha'][0]));amax.append(arb(real['alpha'][1]))
        bmin.append(arb(real['eta'][0])*arb(row['K'][0]))
        bmax.append(arb(real['eta'][1])*arb(row['K'][1]))
        ac.append(stored_upper(comp['alpha_modulus']))
        bc.append(stored_upper(comp['eta_modulus'])*arb(row['K'][1]))
    jr,jc=lr.exp(),lc.exp()
    m=min(min(amin),min(bmin))/jr
    M=max(max(amax),max(bmax))*jr
    width=sigma/(8*jc)
    Ccomplex=max(max(ac),max(bc))*jc
    values=dict(length=exact_arb(right-left),integrated_real_drift_theta=lr,
        integrated_complex_drift_theta=lc,J_upper=jr,J_inverse_upper=jr,
        uniform_regular_matrix_lower=m,uniform_regular_matrix_upper=M,
        physical_coefficient_strip=sigma/4,flow_coefficient_strip=width,
        complex_matrix_modulus=Ccomplex,
        target_curvature_lower=min(arb(row['K'][0]) for row in rows),
        target_curvature_upper=max(arb(row['K'][1]) for row in rows),
        Yz_lower=min(arb(row['real_geometry']['Yz'][0]) for row in rows),
        Yz_upper=max(arb(row['real_geometry']['Yz'][1]) for row in rows))
    if not m>0 or not width>0 or any(not x.is_finite() for x in values.values()):
        raise ValueError('regular positive aggregate is not finite and coercive')
    return {k:ball_record(v) for k,v in values.items()}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--center-object',type=Path,required=True)
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,2000000))
    ap.add_argument('--left',type=Fraction,default=Fraction(1,4))
    ap.add_argument('--right',type=Fraction,default=Fraction(3))
    ap.add_argument('--normalized-strip',type=Fraction,default=Fraction(1,128))
    ap.add_argument('--max-cell-width',type=Fraction,default=Fraction(1,256))
    ap.add_argument('--quarter-nodes',type=int,default=256)
    ap.add_argument('--angles',type=int,default=512)
    ap.add_argument('--bits',type=int,default=160)
    ap.add_argument('--max-depth',type=int,default=14)
    ap.add_argument('--max-attempts',type=int,default=20000)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=4
    started=time.monotonic()
    target=StablePositiveFamily(args.center_object,args.half_width,args.quarter_nodes,args.angles,
                               arb('.003'),arb('.0025'),arb('.32'))
    left,right=args.left,args.right;sigma=exact_arb(args.normalized_strip)
    if not 0<left<right<=3 or not args.max_cell_width>0 or not sigma>0:
        raise ValueError('invalid finite body interval/width')
    knots={left,right}
    for key,values in target.frozen.items():
        if key.endswith('_knots'):
            knots.update(q for q in (abs(Fraction.from_float(float(x))) for x in values) if left<q<right)
    points=sorted(knots);initial=list(zip(points,points[1:]))
    queue=deque()
    for a,b in initial:
        count=max(1,-(-(b-a)//args.max_cell_width))
        queue.extend((a+(b-a)*j/count,a+(b-a)*(j+1)/count,0) for j in range(count))
    rows=[];failures=[];attempts=0
    identity=provenance(target,args.center_object);identity.pop('dependency_sha256')
    report=dict(kind='uniform_exact_affine_positive_regular_body',complete=False,**identity,
        radial_domain=[str(left),str(right)],normalized_angle_strip=str(args.normalized_strip),
        max_initial_cell_width=str(args.max_cell_width),initial_original_spans=len(initial),
        quarter_nodes=args.quarter_nodes,angular_boxes=args.angles,bits=args.bits,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ['fourfold_phase_beta_parameter_germ.py','fourfold_phase_beta_parameter_root.py',
             'fourfold_phase_actual_positive_cap.py','fourfold_phase_beta_affine.py',
             'fourfold_phase_beta_interval.py','fourfold_phase_beta_bulk_interval.py',
             'fourfold_phase_beta_bulk_box.py','fourfold_phase_root_interval.py',
             'fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']},
        cells=rows,failed_cells=failures,
        scope=['Exact shared affine parameter before nonlinear trigonometry and all infinite primitives.',
               'Continuous real r/theta/parameter boxes and a paid complex theta strip.',
               'True target curvature via exact cancellation; no finite Fourier target substitution.',
               'Finite regular-to-regular positive body only; no exterior closure or held open H.'])
    report['source_sha256']=sha(__file__)
    def save():
        report['attempts']=attempts;report['pending']=[[str(a),str(b),d] for a,b,d in queue]
        report['elapsed_seconds']=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        temporary=args.out.with_suffix(args.out.suffix+'.tmp')
        raw=(json.dumps(report,indent=2)+'\n').encode()
        temporary.write_bytes(gzip.compress(raw,mtime=0) if args.out.suffix=='.gz' else raw)
        temporary.replace(args.out)
    while queue and attempts<args.max_attempts:
        a,b,depth=queue.popleft();attempts+=1;target.set_cell(a,b)
        try:
            row=target.evaluate_positive(a,b,sigma);rows.append(row)
            print(json.dumps(dict(attempt=attempts,accepted=len(rows),pending=len(queue),
                 interval=[float(a),float(b)],K=row['K'],elapsed_seconds=time.monotonic()-started)),flush=True)
        except (ValueError,ZeroDivisionError) as exc:
            if depth<args.max_depth:
                mid=(a+b)/2
                queue.appendleft((mid,b,depth+1));queue.appendleft((a,mid,depth+1))
            else:failures.append(dict(interval=[str(a),str(b)],reason=str(exc)))
            print(json.dumps(dict(attempt=attempts,refinement=depth,reason=str(exc))),flush=True)
        save()
    rows.sort(key=lambda row:Fraction(row['radial_interval'][0]))
    cursor=left
    for row in rows:
        a,b=map(Fraction,row['radial_interval'])
        if a!=cursor:break
        cursor=b
    report['exact_radial_cover']=bool(cursor==right and not queue and not failures)
    if report['exact_radial_cover']:
        report['operator_constants']=aggregate(rows,left,right,sigma);report['complete']=True
    save()
    print(json.dumps(dict(complete=report['complete'],accepted=len(rows),failed=len(failures),
                         elapsed_seconds=report['elapsed_seconds']),indent=2),flush=True)
    if not report['complete']:raise SystemExit('the finite positive body is not yet certified')


if __name__=='__main__':main()
