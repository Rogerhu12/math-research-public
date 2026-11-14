#!/usr/bin/env python3
"""R110 supplement: tame triangular L2/H1/2 strict-core propagation.

Consumes complete actual continuous energy reports. All zero-order
commutators and the high-coefficient part of D[Lambda,a] drive base energy,
rather than appearing in the H1/2 exponential rate. The default signed
method retains the exact principal commutator in the real energy matrix.
No new geometry is sampled. Optional first-moment refinement reads the existing complete
nine-field rectangle. This cannot cross a turning root or positive collar.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
import time
import traceback
from flint import arb,acb,acb_mat,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_low_feedback_paid_inputs import norm
from fourfold_phase_strict_core_energy import (
    CompleteEnergyFields,sha,read,save,phi_integral,finite)


def up(record):
    result=arb(record['ball']).upper()
    if not result.is_finite():raise ValueError('nonfinite input constant')
    return result


def positive_range(report,name):
    lo,hi=report['coefficient_positive_ranges'][name]
    left=arb(lo['ball']).lower();right=arb(hi['ball']).upper()
    if not 0<left<=right:raise ValueError('unproved positive range '+name)
    return left,right


def matrix_record(value):
    for i in range(value.nrows()):
        for j in range(value.ncols()):finite(value[i,j].real)
    return [[ball_record(value[i,j].real) for j in range(value.ncols())]
            for i in range(value.nrows())]


def real_exprel(x):
    if x==0:return arb(1)
    if not x.contains(0):
        value=x.expm1()/x
    else:
        value=max(arb(0),x.upper()).exp()
    if not value>0:raise ValueError('invalid complete exponential divided difference')
    return value


def piece(path,refine_first_moments=False,method='signed'):
    report=read(path)
    if (not report.get('complete') or report.get('kind')!=
            'actual_strict_negative_half_derivative_energy_inputs'):
        raise ValueError('a complete actual continuous energy report is required')
    old=Path(__file__).with_name('fourfold_phase_strict_core_energy.py')
    if sha(old)!=report['source_sha256']:
        raise ValueError('the actual continuous energy source changed')
    for name,digest in report['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('continuous energy dependency changed: '+name)
    if not report.get('strict_negative_target_curvature_proved'):
        raise ValueError('a turning or positive interval cannot use this bound')
    if not report.get('full_real_radial_interval_paid') or not report.get('full_real_theta_circle_paid'):
        raise ValueError('a sample-only energy report is insufficient')
    if not report['identity'].get('uniform_in_the_entire_real_parameter_interval'):
        raise ValueError('the complete real parameter family is missing')
    left,right=map(Fraction,report['exact_physical_interval'])
    if not left<right:raise ValueError('empty strict interval')
    L=exact_arb(right-left)
    amin,amax=positive_range(report,'alpha')
    gmin,gmax=positive_range(report,'gamma')
    lmin,lmax=positive_range(report,'lambda_weight')
    positive_range(report,'kappa')
    inputs=report['actual_multiplier_and_commutator_inputs']
    norms={name:{key:up(value) for key,value in row.items()}
           for name,row in inputs.items()}
    for row in norms.values():
        if any(not value>=0 for value in row.values()):
            raise ValueError('negative Fourier majorant')
    root5=arb(5).sqrt()
    # Every nonzero physical frequency is at least four. These follow from
    # complete Bhalf/DAhalf sums, including their already paid infinite tails.
    W={name:min(norms[name]['Bhalf']/root5,
                 norms[name]['derivative_Ahalf']/(root5-1)).upper()
       for name in ('alpha','v','gamma')}
    first_moment_method='W1 <= min(Bhalf/sqrt(5), derivative_Ahalf/(sqrt(5)-1)); physical nonzero frequencies >=4'
    direct_moments=None
    if refine_first_moments or method=='signed':
        field_path=Path(report['input_field_report']['path'])
        if sha(field_path)!=report['input_field_report']['sha256']:
            raise ValueError('the underlying nine-field report changed')
        fields=CompleteEnergyFields(field_path)
        if fields.doc['identity']!=report['identity']:
            raise ValueError('the coefficient rectangle belongs to a different true family')
        values,coefficients,moments=fields.evaluate(left,right,report['angular_closed_cells'])
        direct_moments={name:[x.upper() for x in moments[name][0]]
                        for name in ('alpha','v','gamma')}
        W={name:min(W[name],direct_moments[name][1]).upper() for name in W}
        first_moment_method+='; minimum with complete actual rectangle A1 when provided'

    # Exact tame commutator:
    # |omega_k| |w(k)-w(l)|
    # <= |omega_(k-l)| w(l)/2
    #    + |omega_(k-l)| (sqrt(1+|omega_(k-l)|)-1).
    # Only the first term multiplies the H1/2 state.
    c11=(gmax/gmin).sqrt()*W['v']/2
    c12=(gmax/amin).sqrt()*W['alpha']/2
    c21=(amax/gmin).sqrt()*W['gamma']/2
    c22=(amax/amin).sqrt()*W['v']/2
    difference=abs(c11-c22).upper()
    off=(c12+c21).upper()
    # Use the numerical radius of the positive principal majorant, not
    # an unnecessarily larger norm of its unsymmetrized 2x2 matrix.
    C1=((c11+c22+(difference*difference+off*off).sqrt())/2).upper()
    Ad=up(report['actual_Ahalf_potential_upper'])
    remainder={name:norms[name]['derivative_Ahalf']
               for name in ('alpha','v','gamma')}
    signed_rates=None
    if method=='signed':
        # Exact D[Lambda,a] = (Da)Lambda/2 + R_a. On physical 4Z,
        # ||R_a|| <= sum |4k|^(3/2)|a_k|, including the zero-input mode.
        remainder={name:min(norms[name]['Bhalf'],
                    (root5+1)*norms[name]['derivative_Ahalf']/2).upper()
                   for name in remainder}
        for name in remainder:
            finite_part=sum((2*arb(4*k)*arb(4*k).sqrt()*abs(c).upper()
                             for k,c in enumerate(coefficients[name]) if k),arb(0))
            E0,E1,E2=fields.errors[name][0]
            remainder[name]=min(remainder[name],
                                finite_part+(E1*E2).sqrt()).upper()
        kind=report['energy_weight']['kind']
        if kind=='minus_actual_target_curvature':
            lambdas=values['kappa']['value'];lambda_r=values['kappa']['radial']
        elif kind=='positive_exact_constant':
            lam=exact_arb(Fraction(report['energy_weight']['value']))
            lambdas=[lam]*report['angular_closed_cells']
            lambda_r=[arb(0)]*report['angular_closed_cells']
        else:raise ValueError('unsupported actual energy-weight definition')
        forward=[];backward=[]
        for j in range(report['angular_closed_cells']):
            a=values['alpha']['value'][j];at=values['alpha']['theta'][j]
            ar=values['alpha']['radial'][j]
            g=values['gamma']['value'][j];gt=values['gamma']['theta'][j]
            gr=values['gamma']['radial'][j]
            v=values['v']['value'][j];vt=values['v']['theta'][j]
            d=values['tau']['value'][j]+values['sigma']['theta'][j]
            lam=lambdas[j]
            if not a>0 or not g>0 or not lam>0:
                raise ValueError('signed principal angular cell lost real positivity')
            ru=lambda_r[j]/lam+vt
            rq=(gr+v*gt)/g-2*vt
            rp=(ar+v*at)/a-2*vt
            cross=(lam-d)*(a/lam).sqrt()
            off=(a*g).sqrt()*(at/a+gt/g)/2
            # Directed Gershgorin for the true symmetric 3x3 energy matrix
            # [[ru,0,cross],[0,rq,off],[cross,off,rp]].
            c=abs(cross).upper();b=abs(off).upper()
            forward.append(max((ru+c).upper(),(rq+b).upper(),(rp+c+b).upper()))
            backward.append(max((-ru+c).upper(),(-rq+b).upper(),(-rp+c+b).upper()))
        signed_rates=dict(forward=max(forward).upper(),backward=max(backward).upper())
    elif method!='tame':
        raise ValueError('unknown whole commutator decomposition')
    R=acb_mat(3,3)
    R[0,1]=(lmax/gmin).sqrt()*norms['v']['Ahalf']
    R[0,2]=(lmax/amin).sqrt()*norms['alpha']['Ahalf']
    R[1,1]=(gmax/gmin).sqrt()*remainder['v']
    R[1,2]=(gmax/amin).sqrt()*remainder['alpha']
    R[2,0]=(amax/lmin).sqrt()*Ad
    R[2,1]=(amax/gmin).sqrt()*remainder['gamma']
    R[2,2]=(amax/amin).sqrt()*remainder['v']
    T=norm(R).upper()
    Ss=up(report['constants']['source_vector_energy_gain'])
    S0=Ss
    if direct_moments is not None:
        aa=direct_moments['alpha'];vv=direct_moments['v']
        W0=acb_mat([[0,lmax.sqrt()*aa[0],0],
            [0,gmax.sqrt()*(aa[0]+aa[1]),0],
            [amax.sqrt(),amax.sqrt()*(vv[0]+vv[1]),amax.sqrt()]])
        S0=min(Ss,norm(W0)).upper()
    initial_conversion=(max(lmax,gmax,amax)/min(lmin,gmin,amin)).sqrt().upper()
    result=dict(input_report=dict(path=str(path),sha256=sha(path)),
        exact_physical_interval=[str(left),str(right)],identity=report['identity'],
        energy_weight=report['energy_weight'],first_moment_method=first_moment_method,
        commutator_method=method,
        complete_physical_W1={name:ball_record(x) for name,x in W.items()},
        complete_L2_remainder_majorants={name:ball_record(x) for name,x in remainder.items()},
        principal_half_commutator_matrix=[[ball_record(x) for x in row]
                                         for row in ((c11,c12),(c21,c22))],
        unsigned_tame_principal_rate_addition=ball_record(C1),
        base_driven_commutator_matrix=matrix_record(R),
        base_driven_commutator_gain=ball_record(T),
        old_single_level_commutator_gain=report['constants']['half_derivative_commutator_gain'],
        source_gain_base=ball_record(S0),source_gain_half=ball_record(Ss),
        initial_bound_E0_sqrt_by_Ehalf_sqrt=ball_record(initial_conversion),
        source_space='L2(dr; H^(1/2) f0 direct_sum H^(3/2) fr direct_sum H^(3/2) ftheta), physical weights max(1,4|k|)^s',
        full_parameter_interval=True,complete=True)
    if direct_moments is not None:
        result['complete_rectangle_A012']={name:list(map(ball_record,row))
                                          for name,row in direct_moments.items()}
    if signed_rates is not None:
        result['complete_signed_principal_energy_rates']={k:ball_record(x) for k,x in signed_rates.items()}
    operators={}
    for direction in ('forward','backward'):
        b0=up(report['constants']['base_energy_rate_'+direction])/2
        bs=(signed_rates[direction]/2).upper() if signed_rates is not None else (b0+C1).upper()
        difference=bs-b0
        e0=(b0*L).exp()
        es=(bs*L).exp()
        coupling=(T*L*e0*real_exprel(difference*L)).upper()
        P=acb_mat([[e0,0],[coupling,es]])
        # For either sign of bs-b0,
        # theta(t) <= exp(max(bs,b0)*t)*min(t,1/abs(bs-b0)).
        # When the difference ball meets zero, the t bound remains valid.
        duration=L if difference.contains(0) else min(L,1/abs(difference)).upper()
        largest=max(b0,bs).upper()
        k0=(S0*phi_integral(b0,L).sqrt()).upper()
        ks=((Ss+T*S0*duration)*phi_integral(largest,L).sqrt()).upper()
        for x in (C1,T,S0,Ss,e0,es,coupling,k0,ks):finite(x)
        operators[direction]=(P,(k0,ks))
        result[direction]=dict(base_sqrt_rate=ball_record(b0),
            half_sqrt_rate=ball_record(bs),
            exact_constant_comparison_matrix=matrix_record(P),
            L2_source_kernel_vector=list(map(ball_record,(k0,ks))),
            identity='(sqrt(E0),sqrt(Ehalf)) obeys the ordered positive triangular comparison; the source vector is an L2 radial bound in the stated common strong-source space')
    return result,operators


def whole_direction(pieces,direction):
    indices=range(len(pieces)) if direction=='forward' else range(len(pieces)-1,-1,-1)
    order=list(indices)
    propagator=acb_mat([[1,0],[0,1]])
    for i in order:
        propagator=pieces[i][1][direction][0]*propagator
    # Propagate each complete local source kernel through every later true
    # energy interval. The sum of squared kernels uses disjoint radial L2
    # supports, not an invented commutativity of the local propagators.
    suffix=acb_mat([[1,0],[0,1]])
    costs=[arb(0),arb(0)]
    for i in reversed(order):
        P,K=pieces[i][1][direction]
        k=suffix*acb_mat([[K[0]],[K[1]]])
        for row in range(2):
            value=abs(k[row,0]).upper()
            costs[row]+=value*value
        suffix=suffix*P
    return dict(ordered_comparison_matrix=matrix_record(propagator),
        global_L2_source_kernel_vector=[ball_record(x.sqrt().upper()) for x in costs],
        exact_order=[pieces[i][0]['exact_physical_interval'] for i in order],
        kernel_rule='For a complete five-column source Gram G=integral F*F in the stated product space, the zero-initial endpoint energy E_j is at most kernel_j^2 times G as a quadratic form. Every radial piece, source seam and canonical/root conversion remains subject to its separate actual contract.')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--energy-reports',type=Path,nargs='+',required=True)
    ap.add_argument('--refine-first-moments',action='store_true')
    ap.add_argument('--method',choices=('tame','signed'),default='signed')
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    started,cpu=time.monotonic(),time.process_time()
    report=dict(kind='actual_tame_strict_core_two_level_energy_budget',
        complete=False,source_sha256=sha(__file__),bits=args.bits,method=args.method,
        actual_global_inverse_certified=False,nonlinear_family_complete=False)
    save(args.out,report)
    try:
        paid=[piece(path,args.refine_first_moments,args.method) for path in args.energy_reports]
        paid.sort(key=lambda p:Fraction(p[0]['exact_physical_interval'][0]))
        initial=paid[0][0]
        cursor=Fraction(initial['exact_physical_interval'][0])
        # Per-leaf identities legitimately carry their own original span.
        family_keys=('object_sha256','origin_inputs_sha256','direction_sha256',
                     'exact_parameter_interval','exact_parameter_half_width')
        for result,_ in paid:
            left,right=map(Fraction,result['exact_physical_interval'])
            if left!=cursor:raise ValueError('gap or overlap in the declared strict cover')
            cursor=right
            if result['energy_weight']!=initial['energy_weight']:
                raise ValueError('actual energy weights do not match at a radial seam')
            for key in family_keys:
                if result['identity'][key]!=initial['identity'][key]:
                    raise ValueError('different actual parameter or coefficient family')
        report.update(complete=True,pieces=[result for result,_ in paid],
            exact_physical_interval=[initial['exact_physical_interval'][0],str(cursor)],
            energy_weight=initial['energy_weight'],
            exact_parameter_interval=initial['identity']['exact_parameter_interval'],
            identity={k:initial['identity'][k] for k in family_keys},
            forward=whole_direction(paid,'forward'),
            backward=whole_direction(paid,'backward'),
            exact_source_convention='f0=-R0, fr=Rr, ftheta=Rtheta; shifted momentum pbar=p_N, unchanged from R107/R110',
            scope=[
                'Only the declared contiguous, genuinely strict-negative intervals and the entire actual real parameter interval.',
                'The complete zero-order and high-coefficient commutators are retained as base-energy forcing, not omitted.',
                'No maximum frequency cutoff enters the tame Fourier inequalities.',
                'The original full physical PDE, not the saved projected Galerkin ODE, is estimated.',
                'Root/Airy transfer, positive collars, cap feedback, frame conversion and nonlinear convergence are not supplied by this budget.'])
    except Exception as exc:
        report.update(failure=repr(exc),traceback=traceback.format_exc())
    report.update(CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-started,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_strict_core_energy.py','fourfold_phase_core_energy_fields.py',
            'fourfold_phase_low_feedback_paid_inputs.py','fourfold_phase_beta_interval.py',
            'fourfold_phase_beta_bulk_interval.py')})
    save(args.out,report)
    print(json.dumps({k:report.get(k) for k in ('complete','failure',
        'exact_physical_interval','forward','backward','CPU_seconds')},
        indent=2,allow_nan=False),flush=True)
    if not report['complete']:raise SystemExit(1)


if __name__=='__main__':
    main()
