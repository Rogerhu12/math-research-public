#!/usr/bin/env python3
"""True complete physical core/cap interface multipliers at r=1/4.

The native infinite primitive supplies F and Fr. Ftheta=aT is exact in the
phase representation, and the moving-frame D/M/H identities supply the true
radial principal coefficients. A new complex denominator gate is paid at
this cut; the separate |r|<=.24 chart is not reused outside its domain.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_affine import AffineFastBulkTarget,provenance
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import (CBox,Box,cstack,cdot,complex_sincos,
    scalar_arb,arb_box)
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_actual_positive_cap import complex_separation
from fourfold_phase_core_low_coefficients import extend_half
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_cap_energy_interval import sha


NAMES=('height_Y','inverse_height','conormal_pY','energy_shear_YpY','conormal_ratio_pY_over_Y')


def real_sqrt(value):
    if not np.min(value.real.lo)>0:raise ValueError('the real position norm square is not positive')
    entries=[arb_box(scalar_arb(value.real[j]).sqrt()) for j in range(len(value.real.lo))]
    return cstack([CBox(x) for x in entries])


class InterfaceTarget(AffineFastBulkTarget):
    def parts(self,radial,coefficient,errors,sigma=None):
        fields=self.fast_fields(radial,coefficient,errors,True,sigma)
        F,X=fields[0,0],fields[1,0]
        if sigma is None or sigma==0:
            for value in (F,X):
                if np.any(value.imag.lo>0) or np.any(value.imag.hi<0):
                    raise ValueError('a genuine real interface field lost the real axis')
            F,X=CBox(F.real),CBox(X.real)
        beta,gamma,radius,_=self.last_scalar
        ss,cc=((self.angle_sines,self.angle_cosines) if sigma is None
               else self.angle_shift_cache[sigma.str(35)])
        frequency=CBox((4*np.arange(1,self.modes+1)).reshape(-1,1))
        phase=lambda v,j:(v[j].reshape(-1,1)*ss).sum()
        angle=lambda v:(v[0].reshape(-1,1)*frequency*cc).sum()
        b,g,br,gr,bt,gt=phase(beta,0),phase(gamma,0),phase(beta,1),phase(gamma,1),angle(beta),angle(gamma)
        sb,cb=complex_sincos(b);sg,cg=complex_sincos(g)
        aa=radius[0]
        tangent=cstack((-cg*sb,cg*cb,sg),-1)
        Ftheta=aa*tangent
        h=-sb*X[:,0]+cb*X[:,1]
        v=-cb*X[:,0]-sb*X[:,1]
        Q=cg*X[:,2]-sg*h
        D=(1+bt)*cg*Q-gt*v
        M=br*cg*Q-gr*v
        fh=-sb*F[:,0]+cb*F[:,1]
        fv=-cb*F[:,0]-sb*F[:,1]
        H=(cg*F[:,2]-sg*fh)*v-fv*Q
        return dict(Fz=F[:,2],Xz=X[:,2],Ftheta_z=Ftheta[:,2],
            R2=cdot(F,F),FX=cdot(F,X),Ftheta_dot_F=cdot(F,Ftheta),
            D=D,M=M,H=H,radius=aa)

    def values(self,radial,coefficient,errors):
        p=self.parts(radial,coefficient,errors)
        R2,Fz,H=p['R2'],p['Fz'],p['H']
        root=real_sqrt(R2)
        Y=Fz/root;inverse=root/Fz
        shear=Fz/(H*H)*(p['D']*(p['Xz']-Fz*p['FX']/R2)
            -p['M']*(p['Ftheta_z']-Fz*p['Ftheta_dot_F']/R2))
        values=(Y,inverse,shear*inverse,shear,shear*R2/(Fz*Fz))
        if any(not np.all(np.isfinite(x.magnitude_upper())) for x in values):
            raise ValueError('a real core/cap multiplier is nonfinite')
        return {name:CBox(value.real) for name,value in zip(NAMES,values)}

    def moduli(self,radial,coefficient,errors,strip):
        p=self.parts(radial,coefficient,errors,strip)
        upper=lambda value:arb(float(np.max(value.magnitude_upper())))
        Rlo=arb(float(np.min(p['R2'].real.lo)))
        if not Rlo>0:raise ValueError('the actual cut lacks a right-half-plane position norm square')
        Zlo=complex_separation(p['Fz'],'actual cut Fz')
        Hlo=complex_separation(p['H'],'actual cut support divided by a')
        Rup,Zup=upper(p['R2']),upper(p['Fz'])
        y=Zup/Rlo.sqrt();inverse=Rup.sqrt()/Zlo
        shear=Zup/Hlo**2*(upper(p['D'])*(upper(p['Xz'])+Zup*upper(p['FX'])/Rlo)
            +upper(p['M'])*(upper(p['Ftheta_z'])+Zup*upper(p['Ftheta_dot_F'])/Rlo))
        values=(y,inverse,shear*inverse,shear,shear*Rup/Zlo**2)
        real=self.parts(radial,coefficient,errors,arb(0))
        real_z=arb(float(np.min(real['Fz'].real.lo)))
        real_Rup=arb(float(np.max(real['R2'].real.hi)))
        if not real_z>0:raise ValueError('the full real cut height is not positive')
        return dict(zip(NAMES,[v.upper() for v in values])),dict(
            normalized_angular_strip=ball_record(strip),
            physical_angular_strip=ball_record(strip/4),
            true_complex_Re_F_dot_F_lower=ball_record(Rlo),
            true_complex_Fz_modulus_lower=ball_record(Zlo),
            true_complex_support_over_radius_modulus_lower=ball_record(Hlo),
            complete_real_height_lower=ball_record((real_z/real_Rup.sqrt()).lower()))


def geometric_tail(K,strip,order,modulus):
    q=(-strip).exp();a=arb(K+1);den=1-q;power=q**(K+1)
    if order==0:total=power/den
    elif order==1:total=power*(a/den+q/den**2)
    elif order==2:total=power*(a*a/den+2*a*q/den**2+q*(1+q)/den**3)
    else:raise ValueError('only the complete 0/1/2 physical derivative tails are requested')
    return (2*modulus*arb(4)**order*total).upper()


def positive_sum(row,order):
    result=arb(float(row[0])) if order==0 else arb(0)
    for k in range(1,len(row)):
        result+=2*arb(float(row[k]))*(4*k)**order
    return result.upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--primitive-nodes',type=int,default=512)
    ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--keep',type=int,default=512)
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--normalized-strip',type=Fraction,default=Fraction(1,16))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec,ctx.cap=args.bits,4
    if not 0<args.keep<args.angles//2:raise ValueError('the retained Fourier modes must exclude Nyquist')
    wall,cpu=time.monotonic(),time.process_time()
    target=InterfaceTarget(args.object,args.primitive_nodes,args.angles,arb('.003'),arb('.0025'),arb('.32'))
    cuts=common_cells(target);r=Fraction(1,4);k=bisect_right(cuts,r)-1
    target.set_cell(cuts[k],cuts[k+1]);radial=acb(exact_arb(r))
    coefficient,_,_,errors,real=target.complete_fast_data(radial)
    if not real:raise ValueError('the interface radius must be mathematically real')
    values=target.values(radial,coefficient,errors)
    strip=exact_arb(args.normalized_strip)
    if not strip>0:raise ValueError('a positive true angular strip is required')
    moduli,domain=target.moduli(radial,coefficient,errors,strip)
    centers=np.empty((len(NAMES),args.keep+1),float)
    fees=np.empty_like(centers);records={}
    for index,name in enumerate(NAMES):
        full=extend_half(values[name],1)
        transformed=target.fast_fourier.fft(full)/args.angles
        if np.any(transformed.imag.lo>0) or np.any(transformed.imag.hi<0):
            raise ValueError('a real even interface function lost its real Fourier coefficients')
        for lag in range(args.keep+1):
            alias=moduli[name]*((-(args.angles-lag)*strip).exp()
                +(-(args.angles+lag)*strip).exp())/(1-(-args.angles*strip).exp())
            true=transformed[lag].to_acb().real+arb(0,alias.upper())
            chosen=float(true.mid())
            radius=abs(true-arb(chosen)).upper()
            saved_fee=float(np.nextafter(float(radius),np.inf)) if radius else 0.
            if not np.isfinite(saved_fee):raise ValueError('nonfinite saved Fourier coefficient error')
            centers[index,lag],fees[index,lag]=chosen,saved_fee
        tails=[geometric_tail(args.keep,strip,j,moduli[name]) for j in range(3)]
        selected=[positive_sum(fees[index],j) for j in range(3)]
        error=[(a+b).upper() for a,b in zip(selected,tails)]
        finite=[positive_sum(np.abs(centers[index]),j) for j in range(3)]
        half_finite=arb(abs(float(centers[index,0])))
        for lag in range(1,args.keep+1):
            half_finite+=2*abs(arb(float(centers[index,lag])))*arb(1+4*lag).sqrt()
        half_error=(error[0]+(error[0]*error[1]).sqrt()).upper()
        discarded=[]
        for cutoff in (8,16,32,64,128,256):
            if cutoff>args.keep:continue
            norms=[]
            for j in (0,1):
                value=tails[j]
                for lag in range(cutoff+1,args.keep+1):
                    value+=2*(abs(arb(float(centers[index,lag])))+arb(float(fees[index,lag])))*(4*lag)**j
                norms.append(value.upper())
            discarded.append(dict(physical_index_cutoff=cutoff,
                complete_true_discarded_A0=ball_record(norms[0]),
                complete_true_discarded_A1=ball_record(norms[1]),
                complete_true_discarded_Hhalf_multiplier_bound=ball_record((norms[0]+(norms[0]*norms[1]).sqrt()).upper())))
        records[name]=dict(whole_true_complex_strip_modulus=ball_record(moduli[name]),
            selected_coefficient_error_A012=list(map(ball_record,selected)),
            complete_unretained_tail_A012=list(map(ball_record,tails)),
            complete_polynomial_error_A012=list(map(ball_record,error)),
            finite_selected_polynomial_A012=list(map(ball_record,finite)),
            Hhalf_multiplier_error=ball_record(half_error),
            true_Hhalf_multiplier_norm_upper=ball_record((half_finite+half_error).upper()),
            discarded_true_multiplier=discarded)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    arrays=args.out.with_suffix('.npz')
    np.savez_compressed(arrays,positive_fourier_coefficients=centers,
        positive_coefficient_error_radii=fees,physical_indices=np.arange(args.keep+1))
    identity=provenance(target,args.object)
    identity.pop('source_sha256');identity.pop('dependency_sha256')
    result=dict(kind='true_complete_physical_quarter_cut_interface_multipliers',complete=True,
        **identity,source_sha256=sha(__file__),
        exact_physical_radius='1/4',selected_common_scalar_span=list(map(str,target.cell)),
        exact_function_names=list(NAMES),quarter_primitive_nodes=args.primitive_nodes,
        angular_nodes=args.angles,retained_positive_indices=args.keep,bits=args.bits,
        normalized_angular_strip=str(args.normalized_strip),domain=domain,
        true_infinite_primitive_error_budgets=list(map(ball_record,errors)),
        functions=records,
        exact_finite_definition='c0+2*sum_{k=1..K} c_k*cos(4*k*theta), with saved binary64 c_k interpreted exactly',
        coefficient_contract='The true positive Fourier coefficient is real and lies in c_k+[-r_k,r_k] with saved binary64 r_k exact; negative coefficients are equal by exact real-even angular symmetry.',
        arrays=dict(path=str(arrays),sha256=sha(arrays),bytes=arrays.stat().st_size),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_affine.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_core_low_coefficients.py','fourfold_phase_actual_positive_cap.py',
            'fourfold_phase_cap_scaled_body.py')},
        CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        scope=['Actual r=1/4 physical Fourier interface only. A new complex domain is proved at this point.',
               'All selected coefficient arithmetic, infinite primitive errors, complete DFT aliases and unretained Fourier tails are paid.',
               'These multipliers do not certify the radial two-channel propagation, omitted-mode Schur feedback, or a nonlinear solution.'])
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(complete=True,domain=domain,errors={
        name:records[name]['complete_polynomial_error_A012'][0]['ball'] for name in NAMES},
        CPU_seconds=result['CPU_seconds'],wall_seconds=result['wall_seconds']),indent=2),flush=True)


if __name__=='__main__':main()
