#!/usr/bin/env python3
"""Actual C4 natural-weight graft from the finite R33 body to a radial cap.

The construction matches the exact affine graph at r=3.  On the graft the
physical beta and gamma retain a^3 and a^2, respectively.  All angle bounds
are Wiener-algebra bounds for the infinite tangent and primitive; no angular
sampling or finite Fourier target is substituted.  The radial continuation
after the graft is exact, but this file does not attach the infinite R72 tail.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import time

from flint import arb,acb,acb_series,ctx
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_parameter_germ import ParameterGermBulkTarget,provenance,sha
from fourfold_phase_exterior_entry_jet import entry_germs,serializable_entry


def poly(coefficients,x):
    value=acb_series([acb(coefficients[-1])])
    for c in coefficients[-2::-1]:value=value*x+c
    return value


def real_coefficient(value,j):
    z=value[j]
    if not z.imag.contains(0):raise ValueError('a real graft jet lost its real structure')
    return z.real


def modulus(value):return abs(value).upper()


def absolute_jet(value,order=5):
    return acb_series([acb(modulus(value[j])) for j in range(order+1)])


def sinh(value):return (value.exp()-(-value).exp())/2


def cosh_minus_one(value):return 2*sinh(value/2)**2


def nonnegative_coefficients(value,order):
    return [modulus(value[j]) for j in range(order+1)]


def symmetric(value,complex_angle=False):
    error=arb(0,arb(value).upper())
    return acb(error,error if complex_angle else arb(0))


def lower(record):return arb(record['lower']).lower()


def upper(record):return arb(record['upper']).upper()


def minimum_lower(values):return min(arb(v).lower() for v in values)


def maximum_upper(values):return max(arb(v).upper() for v in values)


def regular_positive_constants(rows,length,sigma):
    """Full two-regular-port form constants, after the true angular shear."""
    ell=exact_arb(length)
    real_drift=arb(0);complex_drift=arb(0)
    for row in rows:
        left,right=map(Fraction,row['offset_interval'])
        width=exact_arb(right-left)
        drift=row['real_geometry']['drift_theta']
        real_drift+=width*max(abs(lower(drift[0])),abs(upper(drift[1])))
        complex_drift+=width*upper(row['complex_geometry']['drift_theta_modulus'])
    jr=real_drift.exp();jc=complex_drift.exp()
    amin=min(lower(row['real_geometry']['alpha'][0]) for row in rows)
    amax=max(upper(row['real_geometry']['alpha'][1]) for row in rows)
    ekmin=minimum_lower(lower(row['real_geometry']['eta'][0])*lower(row['target_curvature']) for row in rows)
    ekmax=maximum_upper(upper(row['real_geometry']['eta'][1])*upper(row['target_curvature']) for row in rows)
    m=min(amin,ekmin)/jr;M=max(amax,ekmax)*jr
    rho=sigma/(2*jc)
    Mc=jc*max(max(upper(row['complex_geometry']['alpha_modulus']) for row in rows),
              maximum_upper(upper(row['complex_geometry']['eta_modulus'])*upper(row['target_curvature']) for row in rows))
    # For V=H^1 on an interval: disjoint endpoint tents, with support
    # d=min(length/2,1/<k>), give these squared trace/extension constants.
    Ct=2*max(arb(1),2/ell)
    CE=max(arb(1),2/ell)+arb(1)/3
    g=(1+ell**2/arb.pi()**2)/m
    poisson=CE.sqrt()*(1+M*g)
    dn=M*CE
    Nc=2*Mc*(-rho/2).exp()/(-(-rho/2).expm1())**2
    CL=CE*(1+2*g*(M+1))**2
    weight=minimum_lower((rho/2,1/Nc,1/(2*g*Nc),1/(2*CL*Nc)))
    source=jr.sqrt()*max(upper(row['real_geometry']['Yz'][1]) for row in rows)
    values=dict(radial_length=ell,integrated_real_drift=real_drift,
        integrated_complex_drift=complex_drift,real_J_and_inverse=jr,
        complex_J_and_inverse=jc,m=m,M=M,coefficient_strip=rho,
        complex_coefficient_modulus=Mc,trace_squared=Ct,extension_squared=CE,
        zero_trace_inverse=g,poisson_and_full_contact=poisson,
        full_DN=dn,coefficient_first_moment=Nc,DN_commutator=CL,
        admissible_signed_analytic_weight=weight,physical_L2_source_to_sheared_L2=source)
    if not all(v.is_finite() for v in values.values()) or not m>0 or not weight>0:
        raise ValueError('regular positive operator constants are not finite and positive')
    return {name:ball_record(value) for name,value in values.items()}


class NaturalGraft:
    def __init__(self,object_path,half_width,length):
        self.target=ParameterGermBulkTarget(object_path,half_width,256,512,
            arb('.003'),arb('.0025'),arb('.32'))
        self.entry=entry_germs(self.target)
        self.length=Fraction(length)
        if not self.length>0:raise ValueError('positive graft length required')
        self.ell=exact_arb(self.length)
        old,ctx.cap=ctx.cap,8
        beta,gamma,radius,_=self.target.scalars(acb(3),1)
        self.beta_normalized=[[real_coefficient(v/radius**3,j) for j in range(5)] for v in beta]
        self.gamma_normalized=[[real_coefficient(v/radius**2,j) for j in range(5)] for v in gamma]
        ctx.cap=old
        loga,c=self.entry['log_radius'],self.entry['slope_ratio']
        correction=sum((modulus(loga[j])*self.ell**j for j in range(2,5)),arb(0))
        cfee=sum((modulus(c[j])*self.ell**j for j in range(1,4)),arb(0))
        self.c_global=c[0]+arb(0,cfee.upper())
        if not self.c_global>0 or not loga[1]<0:
            raise ValueError('the actual entrance does not give positive height and decreasing radius')
        self.a_global=(loga[0]+loga[1]*real_interval(0,self.length)
                       +arb(0,correction.upper())).exp()
        self.Z_global=self.entry['height'][0]+arb(0,(self.ell*self.a_global**2*self.c_global).upper())
        # The true integral is nonnegative; the symmetric enclosure above is
        # deliberately retained so it is valid without correlated integration.
        if not self.Z_global>0:raise ValueError('the entire actual graft height is not positive')

    def jets(self,left,right):
        s=acb_series([acb(real_interval(left,right)),1])
        u=s/self.ell
        chi=(1-u)**5*(1+5*u+15*u**2+35*u**3+70*u**4)
        l=self.entry['log_radius'];c=self.entry['slope_ratio']
        loga=l[0]+l[1]*s+chi*sum((l[j]*s**j for j in range(2,5)),acb_series([0]))
        radius=loga.exp()
        slope_ratio=c[0]+chi*sum((c[j]*s**j for j in range(1,4)),acb_series([0]))
        beta=[radius**3*chi*poly(row,s) for row in self.beta_normalized]
        gamma=[radius**2*chi*poly(row,s) for row in self.gamma_normalized]
        return dict(beta=beta,gamma=gamma,radius=radius,log_radius=loga,
                    slope_ratio=slope_ratio,slope=radius**2*slope_ratio)

    def exact_radial_entrance(self):
        l,c=self.entry['log_radius'],self.entry['slope_ratio'][0]
        a=(l[0]+l[1]*self.ell).exp()
        increment=real_interval(0,1)*self.ell*self.a_global**2*self.c_global
        z=self.entry['height'][0]+increment
        omega=-l[1]/(4*c)
        if not omega>arb(5)/4 or not omega<2:
            raise ValueError('the true radial endpoint does not meet the connector entrance interval')
        return dict(physical_cut=str(Fraction(3)+self.length),
            radius=ball_record(a),height=ball_record(z),height_increment=ball_record(increment),
            log_radius_derivative=ball_record(l[1]),slope_ratio=ball_record(c),
            normalized_omega=ball_record(omega),normalized_q='0',
            stable_fourth_mode_R='-1/4',principal_curvature_bound=ball_record(c/(-l[1])),
            coordinate='u=4*c0*(r-(3+length)), with z_u=a^2/4 and h=1/a',
            phase_terminal_jets='beta=gamma=0 through radial derivative order four',
            height_definition='Z3+integral_0^length exp(2*log_radius(s))*slope_ratio(s) ds')

    def phase_bounds(self,jets,sigma):
        values={}
        for key in ('beta','gamma'):
            values[key]={}
            for r in range(6):
                for t in range(3):
                    values[key][r,t]=sum((modulus(v[r])*(4*(k+1))**t
                        *(sigma*4*(k+1)).exp() for k,v in enumerate(jets[key])),arb(0)).upper()
        return values

    def majorants(self,jets,sigma):
        bounds=self.phase_bounds(jets,sigma)
        B=acb_series([acb(bounds['beta'][j,0]) for j in range(6)])
        G=acb_series([acb(bounds['gamma'][j,0]) for j in range(6)])
        cmB,cmG=cosh_minus_one(B),cosh_minus_one(G)
        dx=(1+cmG)*sinh(B)
        dy=cmB+cmG+cmB*cmG
        dz=sinh(G)
        dh=dx+dy
        L=absolute_jet(jets['log_radius'].derivative())
        R=absolute_jet(jets['radius']*jets['slope_ratio'])
        H=L*dh+dh.derivative()
        V=(L*dz+dz.derivative())/4
        # The horizontal primitive has norm <=1 and the zero-mean vertical
        # primitive has norm <=1/4 on 4Z. Its radial zero mode is retained.
        mean_energy=2*L*(L*dy+dy.derivative())+H*H+V*V
        cross=L*dx+R*dz+H*(1+cmG)*B.exp()+V*dz
        radial=4*(L*H+R*V)+2*(H*H+V*V)
        A2=absolute_jet(jets['radius']**2)
        return dict(bounds=bounds,Dh=modulus(dh[0]),Dz=modulus(dz[0]),
                    Hh=modulus(H[0]),Hz=modulus(V[0]),
                    mean_energy=nonnegative_coefficients(mean_energy,2),
                    relative_cross=nonnegative_coefficients(cross,2),
                    relative_radial=nonnegative_coefficients(radial,2),
                    physical_cross=nonnegative_coefficients(A2*cross,2),
                    physical_radial=nonnegative_coefficients(A2*radial,2))

    def geometry(self,jets,maj,complex_angle):
        a=acb(real_coefficient(jets['radius'],0))
        ar=acb(real_coefficient(jets['radius'],1))
        zr=acb(real_coefficient(jets['slope'],0))
        # Analytic Wiener bounds enclose the true infinite primitive at every
        # angle; scalar background modes are retained exactly.
        dh=symmetric(modulus(a)*maj['Dh'],complex_angle)
        dz=symmetric(modulus(a)*maj['Dz']/4,complex_angle)
        xh=symmetric(modulus(a)*maj['Hh'],complex_angle)
        xz=symmetric(modulus(a)*maj['Hz'],complex_angle)
        F=[a+dh,dh,acb(self.Z_global)+dz]
        X=[ar+xh,xh,zr+xz]
        pb=maj['bounds']
        beta=symmetric(pb['beta'][0,0],complex_angle)
        gamma=symmetric(pb['gamma'][0,0],complex_angle)
        br,gr=[symmetric(pb[k][1,0],complex_angle) for k in ('beta','gamma')]
        bt,gt=[symmetric(pb[k][0,1],complex_angle) for k in ('beta','gamma')]
        btt,gtt=[symmetric(pb[k][0,2],complex_angle) for k in ('beta','gamma')]
        brt,grt=[symmetric(pb[k][1,1],complex_angle) for k in ('beta','gamma')]
        sb,cb=beta.sin(),beta.cos();sg,cg=gamma.sin(),gamma.cos()
        h=-sb*X[0]+cb*X[1];v=-cb*X[0]-sb*X[1]
        Q,R=cg*X[2]-sg*h,cg*h+sg*X[2]
        P=1+bt
        Q1=a*gr-P*sg*v-gt*R
        v1=a*cg*br-P*h
        D,M,W=P*cg*Q-gt*v,br*cg*Q-gr*v,Q*Q+v*v
        D1=btt*cg*Q-P*sg*gt*Q+P*cg*Q1-gtt*v-gt*v1
        M1=brt*cg*Q-br*sg*gt*Q+br*cg*Q1-grt*v-gr*v1
        fh=-sb*F[0]+cb*F[1];fv=-cb*F[0]-sb*F[1]
        fq=cg*F[2]-sg*fh
        support=fq*v-fv*Q
        if not D.real>0 or not support.real>0 or not F[2].real>0:
            raise ValueError('actual graft D/support/height separation failed')
        alpha=F[2]**2*D/support**2
        eta=F[2]**2*W**2/(D*support**2)
        btheta=-M1/D+M*D1/D**2
        if complex_angle:
            return dict(alpha_modulus=ball_record(modulus(alpha)),
                        eta_modulus=ball_record(modulus(eta)),
                        drift_theta_modulus=ball_record(modulus(btheta)),
                        D_real_lower=ball_record(D.real.lower()),
                        support_real_lower=ball_record(support.real.lower()))
        norm2=sum((x*x for x in F),acb(0))
        if not alpha.real>0 or not eta.real>0 or not norm2.real>0 or not W.real>0:
            raise ValueError('the actual real graft energy is not positive')
        def bounds(v):
            if not v.imag.contains(0):raise ValueError('real geometry lost real structure')
            return [ball_record(v.real.lower()),ball_record(v.real.upper())]
        Y=F[2]/norm2.sqrt()
        return dict(alpha=bounds(alpha),eta=bounds(eta),drift_theta=bounds(btheta),
                    Yz=bounds(Y),D=bounds(D),support_factor=bounds(support),
                    radius=bounds(a))

    def evaluate(self,left,right,sigma):
        jets=self.jets(left,right)
        real_maj=self.majorants(jets,arb(0))
        complex_maj=self.majorants(jets,sigma)
        a=real_coefficient(jets['radius'],0)
        c=real_coefficient(jets['slope_ratio'],0)
        cp=real_coefficient(jets['slope_ratio'],1)
        L=real_coefficient(jets['log_radius'],1)
        Lp=2*real_coefficient(jets['log_radius'],2)
        if not a>0 or not c>0 or not L<0:
            raise ValueError('monotone actual radius/height failed')
        eps0,eps1=real_maj['mean_energy'][:2]
        q0=L*L+a*a*c*c
        q=q0+arb(0,eps0)
        axis=c*(c*(L*L-Lp)+L*cp)
        fee=(modulus(L)*eps1+2*modulus(Lp)*eps0)/(2*a*a)
        numerator=axis+arb(0,fee.upper())
        if not q>0 or not numerator>0:raise ValueError('true synchronized graft curvature is not positive')
        K=numerator/(q*q)
        rg=self.geometry(jets,real_maj,False)
        cg=self.geometry(jets,complex_maj,True)
        physical=[];relative=[]
        for j in range(3):
            physical.append(max(math.factorial(r)*math.factorial(j-r)*sigma**(-(j-r))
                *max(complex_maj['physical_cross'][r],complex_maj['physical_radial'][r])
                for r in range(j+1)))
            relative.append(max(math.factorial(r)*math.factorial(j-r)*sigma**(-(j-r))
                *max(complex_maj['relative_cross'][r],complex_maj['relative_radial'][r])
                for r in range(j+1)))
        return dict(offset_interval=[str(left),str(right)],
                    physical_radial_interval=[str(3+left),str(3+right)],
                    target_curvature=ball_record(K),
                    log_radius_derivative=ball_record(L),slope_ratio=ball_record(c),
                    mean_energy_correction=[ball_record(v) for v in real_maj['mean_energy']],
                    physical_metric_error_C0_C1_C2=[ball_record(v.upper()) for v in physical],
                    relative_metric_error_C0_C1_C2=[ball_record(v.upper()) for v in relative],
                    real_geometry=rg,complex_geometry=cg)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--center-object',type=Path,required=True)
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,2000000))
    ap.add_argument('--length',type=Fraction,default=Fraction(1,8))
    ap.add_argument('--angle-strip',type=Fraction,default=Fraction(1,32))
    ap.add_argument('--cells',type=int,default=64)
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=6;started=time.monotonic()
    model=NaturalGraft(args.center_object,args.half_width,args.length)
    sigma=exact_arb(args.angle_strip)
    if not sigma>0 or args.cells<1:raise ValueError('positive strip and cell count required')
    identity=provenance(model.target,args.center_object);identity.pop('dependency_sha256')
    rows=[];failed=[]
    report=dict(kind='uniform_actual_natural_weight_C4_exterior_graft',complete=False,**identity,
        graft_length=str(args.length),physical_angle_strip=str(args.angle_strip),
        bits=args.bits,entry=serializable_entry(model.entry),
        normalized_phase_entry={k:[[ball_record(v) for v in row] for row in getattr(model,k)]
                                for k in ('beta_normalized','gamma_normalized')},
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in [
            'fourfold_phase_exterior_entry_jet.py','fourfold_phase_beta_parameter_germ.py',
            'fourfold_phase_beta_parameter_root.py','fourfold_phase_beta_affine.py',
            'fourfold_phase_beta_interval.py','fourfold_phase_beta_bulk_interval.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_combine.py']},
        rows=rows,failed=failed,
        scope=['Exact C4 matching to the actual full affine R33 graph at r=3.',
               'Exact radial exponential continuation after r=3+length.',
               'True infinite-angle Wiener bounds and whole parameter/radial coverage.',
               'The quantified metric defect is retained; exact isometry is not claimed.',
               'The R72 infinite flat tail and fixed open H remain separate unfinished work.'])
    # provenance already supplies a source field; replace it, do not relabel
    # the parameter-germ module as this actual construction.
    report['source_sha256']=sha(__file__)
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        temporary=args.out.with_suffix(args.out.suffix+'.tmp')
        temporary.write_text(json.dumps(report,indent=2)+'\n');temporary.replace(args.out)
    for j in range(args.cells):
        left,right=args.length*j/args.cells,args.length*(j+1)/args.cells
        try:
            row=model.evaluate(left,right,sigma);rows.append(row)
            print(json.dumps(dict(cell=j,complete_cells=len(rows),K=row['target_curvature']['ball'],
                                  physical_C2=row['physical_metric_error_C0_C1_C2'][2]['ball'])),flush=True)
        except (ValueError,ZeroDivisionError) as exc:
            failed.append(dict(cell=j,interval=[str(left),str(right)],reason=str(exc)))
            print(json.dumps(dict(cell=j,failed=str(exc))),flush=True)
        save()
    report['complete']=len(rows)==args.cells and not failed
    if report['complete']:
        report['regular_positive_operator_constants']=regular_positive_constants(rows,args.length,sigma)
        report['exact_radial_entrance']=model.exact_radial_entrance()
    save()
    print(json.dumps(dict(complete=report['complete'],cells=len(rows),failed=len(failed),
                         elapsed_seconds=report['elapsed_seconds']),indent=2),flush=True)
    if not report['complete']:raise SystemExit('actual natural graft gates remain unpaid')


if __name__=='__main__':main()
