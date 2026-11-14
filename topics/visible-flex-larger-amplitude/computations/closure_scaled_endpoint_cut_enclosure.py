#!/usr/bin/env python3
"""Exact all-angle residual of an actual saved finite Fourier cut two-jet.

The Darboux numerator is a quadratic trigonometric polynomial. Full angular
holonomy is enclosed by rational Wiener-series tails, not sampled angles.
This is a statement about the supplied stored two-jet, not a radial solution
certificate or an assertion that an exact solution has no further modes.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from math import comb
from pathlib import Path
import resource
import time


def clean(a):
    return {m:c for m,c in a.items() if c}


def plus(*terms):
    out={}
    for a in terms:
        for m,c in a.items():out[m]=out.get(m,F(0))+c
    return clean(out)


def scale(a,s):
    return clean({m:s*c for m,c in a.items()})


def product(a,b):
    out={}
    for m,c in a.items():
        for n,d in b.items():out[m+n]=out.get(m+n,F(0))+c*d
    return clean(out)


def norm(a):
    return sum(map(abs,a.values()),F(0))


def weighted_norm(a,weight):
    return sum((abs(c)*weight**abs(m) for m,c in a.items()),F(0))


def real_interval(a):
    c=a.get(0,F(0));r=sum(abs(v) for m,v in a.items() if m)
    return c-r,c+r


def scalar(q):
    return dict(exact=str(q),decimal=float(q))


def cosine(mean,values,spacing):
    out={0:mean}
    for j,v in enumerate(values):
        m=spacing*(j+1);out[m]=out[-m]=F.from_float(v)/2
    return clean(out)


def enclose(jets,spacing,kind,order):
    r=F.from_float(jets['radius']);w=F.from_float(jets['backgroundSlope'])
    wr=F.from_float(jets['backgroundSecond'])
    if kind=='direct_stored_jet':
        E=F.from_float(jets['E']);Ep=F.from_float(jets['Ep'])
        k0=F.from_float(jets['meanSlope']);kr0=F.from_float(jets['meanSecond'])
    else:
        E=1+w*w;Ep=2*w*wr
        k0=w+F.from_float(jets['meanSlopeCorrection'])
        kr0=wr+F.from_float(jets['meanSecondCorrection'])
    one={0:F(1)}
    height=cosine(F(0),jets['height'],spacing)
    k=cosine(k0,jets['slope'],spacing)
    kr=cosine(kr0,jets['second'],spacing)
    # p=i*P and (k_theta-p)=i*R, with real odd Laurent coefficients.
    P={m:m*c/r for m,c in height.items()}
    pt={m:-m*c for m,c in P.items()}
    R=plus({m:m*c for m,c in k.items()},scale(P,-1))
    P2=product(P,P)
    leading=plus(k,scale(pt,E))
    numerator=plus(product(leading,kr),scale(product(R,R),E/r),
                   scale(plus(one,P2,product(k,pt)),-Ep/2))
    delta=plus({0:E},scale(product(k,k),-1),scale(P2,E))
    s0=plus(one,P2)
    Bmin,Bmax=real_interval(leading)
    Dmin,Dmax=real_interval(delta)
    Smin,Smax=real_interval(s0)
    if not (Bmin>0 and Dmin>F(1,2) and Smin>0):
        raise ValueError('This all-angle positive-branch enclosure did not close')
    Fn=norm(numerator)
    density_factor=F(101,100) if Dmin**3*F(101,100)**2>=1 else F(3)

    # Exact full holonomy: mean((1+k*p_theta/(1-p^2))/sqrt(Delta)).
    T=plus(delta,{0:F(-1)})
    t,u=norm(T),norm(P2)
    if t>=1 or u>=1:raise ValueError('Wiener series is outside its certified radius')
    invS={0:F(1)};sqrtInv={0:F(1)};powerS={0:F(1)};powerD={0:F(1)}
    for n in range(1,order+1):
        powerS=product(powerS,P2)
        powerD=product(powerD,T)
        invS=plus(invS,scale(powerS,(-1)**n))
        sqrtInv=plus(sqrtInv,scale(powerD,F((-1)**n*comb(2*n,n),4**n)))
    kpt=product(k,pt)
    Napprox=plus(one,product(kpt,invS))
    approx=product(Napprox,sqrtInv).get(0,F(0))-1
    error=(norm(kpt)*u**(order+1)/((1-u)*(1-t))
           +norm(Napprox)*t**(order+1)/(1-t))
    phi_bound=abs(approx)+error

    # A complete real mean root exists within this interval by monotonicity.
    # On the shift interval B>=Bmin/2, 1/2<=Delta<=2 imply dPhi/dk0>=Bmin/6.
    root_shift=8*phi_bound/Bmin
    delta_shift=2*root_shift*norm(k)+root_shift*root_shift
    root_gate=(root_shift<=Bmin/2 and Dmin-delta_shift>=F(1,2)
               and Dmax+delta_shift<=2)
    # Correct the entire radial-second trace after the exact scalar mean root.
    # The analytic Wiener algebra with weight 2^|m| embeds in |Im theta|<=log(2).
    analytic_weight=F(2)
    leading_radius=weighted_norm({m:c for m,c in leading.items() if m},analytic_weight)
    analytic_denominator=leading.get(0,F(0))-leading_radius-root_shift
    correction_gate=root_gate and analytic_denominator>0
    correction={
        'exists':correction_gate,
        'Fourier_weight':scalar(analytic_weight),
        'analytic_strip':'|Im(theta)| <= log(2)',
        'leading_denominator_lower':scalar(analytic_denominator),
        'formula':'kr_exact = kr - (F + s*(kr - Ep*p_theta/2))/(B+s), where Phi(k+s)=0',
        'height_and_nonmean_slope_unchanged':True,
        'fixed_E_and_Ep_unchanged':True,
    }
    if correction_gate:
        perturbation=plus(kr,scale(pt,-Ep/2))
        weighted_F=weighted_norm(numerator,analytic_weight)
        weighted_perturbation=weighted_norm(perturbation,analytic_weight)
        second_error=(weighted_F+root_shift*weighted_perturbation)/analytic_denominator
        second_error_real=(Fn+root_shift*norm(perturbation))/(Bmin-root_shift)
        next_mode=spacing*(len(jets['height'])+1)
        correction.update(
            weighted_Darboux_numerator=scalar(weighted_F),
            weighted_mean_shift_response=scalar(weighted_perturbation),
            radial_second_correction_weighted_l1=scalar(second_error),
            radial_second_correction_all_angle=scalar(second_error_real),
            first_unrepresented_frequency=next_mode,
            unrepresented_exact_radial_second_l1=scalar(second_error/analytic_weight**next_mode),
            scope='A complete analytic angular two-jet at this single cut; no radial trajectory or exact deep-tail matching claim.')
    return dict(
        interpretation=kind,
        input_metric=dict(r=scalar(r),E=scalar(E),Ep=scalar(Ep),
                          mean_slope=scalar(k0),mean_second=scalar(kr0)),
        all_angle=dict(
            leading_min_over_w=scalar(Bmin/w),
            Delta_min=scalar(Dmin),Delta_max=scalar(Dmax),one_minus_p2_min=scalar(Smin),
            Darboux_polynomial_l1=scalar(Fn),
            weighted_Darboux_numerator_abs_upper=scalar(density_factor*Fn),
            weighted_Darboux_numerator_formula='F / Delta^(3/2)',
            source_physical_Darboux_abs_upper=scalar(Fn/(E*E*r)),
            source_physical_Darboux_formula='F / (E^2*r)',
            defect_relative_to_background_wwr=scalar(Fn/abs(w*wr)),
            max_polynomial_frequency=max(map(abs,numerator),default=0)),
        holonomy=dict(
            formula='mean((1+k*p_theta/(1-p^2))/sqrt(Delta))-1',
            Taylor_order=order,Delta_minus_one_Wiener_norm=scalar(t),p_squared_Wiener_norm=scalar(u),
            rational_approximation=scalar(approx),remainder_abs_upper=scalar(error),
            lower=scalar(approx-error),upper=scalar(approx+error),abs_upper=scalar(phi_bound),
            complete_real_mean_root_exists=root_gate,
            mean_slope_root_correction_abs_upper=scalar(root_shift)),
        exact_full_angle_cut_correction=correction,
        scope='Exact rational enclosure for every real angle of this stored finite Fourier two-jet only.')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--order',type=int,default=4)
    args=p.parse_args()
    started=time.monotonic()
    raw=args.input.read_bytes()
    packet=json.loads(gzip.decompress(raw) if args.input.suffix=='.gz' else raw)
    jets=packet['response']['jets'];spacing=packet['response']['checkpoint']['parameters']['spacing']
    reports=[enclose(jets,spacing,kind,args.order)
             for kind in ['direct_stored_jet','split_background_jet']]
    a,b=[x['input_metric'] for x in reports]
    difference={k:scalar(F(a[k]['exact'])-F(b[k]['exact']))
                for k in ['E','Ep','mean_slope','mean_second']}
    out=dict(status='EXACT all-angle cut-jet enclosures; no radial or complete-surface claim',
             input=str(args.input),input_sha256=hashlib.sha256(raw).hexdigest(),
             entrypoint_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             spacing=spacing,modes=len(jets['height']),reports=reports,
             interpretation_differences=difference,
             elapsed_seconds=time.monotonic()-started,
             peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             limits=[
                 'The direct interpretation uses the saved E/Ep and total mean two-jet exactly as binary input data.',
                 'The split interpretation separately retains background and mean corrections, with E=1+w^2 and Ep=2*w*wr; it is not silently substituted for the direct stored metric.',
                 'Source-profile evaluation error, radial discretization and unrepresented exact solution modes are not enclosed.',
                 'The full angular residual of the supplied finite polynomial is enclosed without angular sampling.',
                 'The complete angular cut correction retains E/Ep, height and nonmean slope, but changes the mean slope and generally infinitely many radial-second coefficients.',
                 'This does not prove the nonlinear shallow trace matches R18.',
             ])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),elapsed=out['elapsed_seconds'],peak_RSS_KiB=out['peak_RSS_KiB'],
                          reports=[dict(kind=x['interpretation'],
                                        F=x['all_angle']['Darboux_polynomial_l1']['decimal'],
                                        phi=x['holonomy']['abs_upper']['decimal'],
                                        mean_root_shift=x['holonomy']['mean_slope_root_correction_abs_upper']['decimal'],
                                        radial_second_correction=x['exact_full_angle_cut_correction'].get('radial_second_correction_all_angle',{}).get('decimal'),
                                        root_exists=x['holonomy']['complete_real_mean_root_exists']) for x in reports])))


if __name__=='__main__':
    main()
