#!/usr/bin/env python3
"""R131 v2: preserve failed gates without nonfinite JSON placeholders.

The C0 residual and candidate theta derivative are consumed on every closed
box. No candidate second theta derivative, residual theta derivative, C1
error barrier or Riccati discriminant is read. Actual initial weighted
derivatives are independently enclosed from the true finite phase formula.
"""
from __future__ import annotations
import argparse,gzip,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
import sympy as sp
from flint import arb,ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_phase_two_jet_newton_source import (
    arb_box,square_box,box_abs_upper,record,range_record,sha,save,
)
from fourfold_phase_beta_bulk_interval import exact_arb


def read_json(path):
    raw=Path(path).read_bytes()
    if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
    return json.loads(raw)


def upper(record):return arb(record['upper']).upper()
def lower(record):return arb(record['lower']).lower()


def symbolic_checks():
    p,q,pt,qt,beta,kappa,gamma,rp,rq,rpt,rqt=sp.symbols('p q pt qt beta kappa gamma rp rq rpt rqt')
    d=p-q;f=-beta*q*(1+p*p)+kappa*d;g=-beta*p*(1+q*q)-kappa*d
    a=beta*(1-3*p*q)+3*kappa;b=-beta*(1+p*p)-kappa;c=-beta*(1+q*q)-kappa
    dpd=f-g-gamma*d*qt;dqd=f-g-gamma*d*pt
    dppt=gamma*qt*pt+sp.diff(f,p)*pt+sp.diff(f,q)*qt
    dqqt=gamma*pt*qt+sp.diff(g,p)*pt+sp.diff(g,q)*qt
    expressions=dict(
        source_difference=f-g-d*(beta*(1-p*q)+2*kappa),
        weighted_p=dpd*pt+d*dppt-a*d*pt-b*d*qt,
        weighted_q=dqd*qt+d*dqqt-c*d*pt-a*d*qt,
        forced_weighted_p=(dpd+rp-rq)*pt+d*(dppt+rpt)-a*d*pt-b*d*qt-(rp-rq)*pt-d*rpt,
        forced_weighted_q=(dqd+rp-rq)*qt+d*(dqqt+rqt)-c*d*pt-a*d*qt-(rp-rq)*qt-d*rqt)
    results={name:bool(sp.Poly(sp.expand(value),p,q,pt,qt,beta,kappa,gamma,rp,rq,rpt,rqt).is_zero)
        for name,value in expressions.items()}
    if not all(results.values()):raise ValueError('an independent exact polynomial identity check failed')
    return dict(engine='SymPy exact polynomial arithmetic',version=sp.__version__,checks=results)


def initial_weighted_derivative(object_path,half_width,nodes,angles):
    target=CodazziCoefficientTarget(object_path,half_width,nodes,angles)
    coefficient=target.coefficients(Fraction(0),Fraction(0))
    if not coefficient['K']<0:raise ValueError('initial true K is not strictly negative')
    actual=target.exact_initial_C_polynomials(1)
    C,Ct=[p.angular_cells(angles) for p in actual]
    if not np.all(C.hi<0):raise ValueError('initial actual C chart is unresolved')
    k2=arb_box(-coefficient['K'])
    U0=-2*k2*Ct/(square_box(C)*C)
    bound=box_abs_upper(U0).upper()
    if not bound.is_finite():raise ValueError('nonfinite initial weighted derivative')
    return bound,dict(initial_B='0',initial_C='-(1+sum_j 4j beta_j(0) cos(4j theta))/a(0)',
        initial_p='k/C',initial_q='-k/C',initial_weighted_p='-2 k^2 C_theta/C^3',
        initial_weighted_q='2 k^2 C_theta/C^3',
        initial_C_range=range_record(C),initial_C_theta_range=range_record(Ct),
        target_initial_K=record(coefficient['K']),weighted_gradient_upper=record(bound),
        whole_parameter_interval=True,whole_real_angular_circle=True,primitive_nodes=nodes,closed_angle_cells=angles,
        actual_initial_provider_sha256=sha(Path(__file__).with_name('fourfold_phase_codazzi_coefficients.py')))


def propagate(native,initial_weighted,tube):
    inflation=arb(1)+arb(2)**-40;tiny=arb(2)**-180
    start=(2*upper(native['initial_error']['epsilon0'])+tiny).upper()
    initial_c0=start;weighted=(initial_weighted+tiny).upper();accumulated=arb(0)
    endpoint=Fraction(0);rows=[];minimum_gap=None;minimum_k=None;maximum_gradient=arb(0)
    for number,item in enumerate(native['rows']):
        left,right=map(Fraction,item['interval']);gl,gr=map(Fraction,item['actual_scalar_germ'])
        if left!=endpoint or not gl<=left<right<=gr:raise ValueError('noncontiguous actual scalar cover')
        raw=item['bounds']
        u={name:upper(raw[name]) for name in ('Mhat','D1','rho0','gamma','beta','kappa')}
        if not all(v.is_finite() and v>=0 for v in u.values()):raise ValueError('invalid complete C0 comparison bound')
        candidate_gap=lower(raw['candidate_gap']);k=lower(raw['k_lower']);h=exact_arb(right-left)
        M=(u['Mhat']+tube).upper();J=(u['beta']*(1+3*M*M)+2*u['kappa']).upper()
        A0=(u['gamma']*u['D1']+J).upper();den=(1-h*A0).lower()
        if not den>0:raise ValueError(f'row {number}: C0 affine denominator failed')
        end=((start+h*u['rho0'])/den*inflation+tiny).upper()
        margin=(end-start-h*(A0*end+u['rho0'])).lower()
        actual_gap=(candidate_gap-2*end).lower()
        actual_M=(u['Mhat']+end).upper()
        L=(u['beta']*(2+4*actual_M*actual_M)+4*u['kappa']).upper()
        weighted_end=(weighted*(h*L).exp()).upper();accumulated=(accumulated+h*L).upper()
        gates=dict(positive_k=bool(k>0),C0_inside_tube=bool(end<tube),
            C0_barrier_strictly_increases=bool(end>start),strict_C0_affine_margin=bool(margin>0),
            strict_actual_gap=bool(actual_gap>0),finite_weighted_growth=bool(weighted_end.is_finite()))
        if all(gates.values()):gradient=(weighted_end/actual_gap).upper()
        else:gradient=None
        row=dict(native_row=number,interval=[str(left),str(right)],
            C0_initial=record(start),C0_final=record(end),C0_margin=record(margin),
            C0_coefficient=record(A0),bootstrap_M=record(M),actual_M=record(actual_M),
            actual_gap_lower=record(actual_gap),weighted_transport_coefficient=record(L),
            weighted_gradient_initial=record(weighted),weighted_gradient_final=record(weighted_end),
            actual_first_angular_derivative_upper=record(gradient) if gradient is not None else None,
            actual_first_angular_derivative_certified=bool(all(gates.values())),gates=gates)
        rows.append(row)
        if not all(gates.values()):
            return dict(passed=False,failed_row=number,rows=rows,covered_interval=['0',str(endpoint)])
        endpoint=right;minimum_gap=actual_gap if minimum_gap is None else min(minimum_gap,actual_gap).lower()
        minimum_k=k if minimum_k is None else min(minimum_k,k).lower()
        maximum_gradient=max(maximum_gradient,gradient).upper();start=end;weighted=weighted_end
    if not rows or ['0',str(endpoint)]!=native['exact_requested_interval']:raise ValueError('incomplete actual radial coverage')
    return dict(passed=True,covered_interval=['0',str(endpoint)],rows=rows,
        initial_C0_barrier=record(initial_c0),final_C0_barrier=record(start),
        initial_weighted_derivative_upper=record(initial_weighted),final_weighted_derivative_upper=record(weighted),
        integrated_weighted_transport_coefficient=record(accumulated),
        actual_first_angular_derivative_upper=record(maximum_gradient),actual_gap_lower=record(minimum_gap),
        target_k_lower=record(minimum_k))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--native',type=Path,default=Path('notes/2026-11-13-Codazzi-continuation-r005-v4-native.json.gz'))
    p.add_argument('--producer',type=Path,default=Path('scripts/fourfold_phase_codazzi_continuation_validate.py'))
    p.add_argument('--provider',type=Path,default=Path('scripts/fourfold_phase_codazzi_coefficients.py'))
    p.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-codazzi-dense-r0005-n1024-candidate.npz.gz'))
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--tube',type=Fraction,default=Fraction(1,16));p.add_argument('--angles',type=int,default=16384)
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--bits',type=int,default=256)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx.prec=args.bits;ctx.cap=4;started=time.monotonic()
    if args.out.exists():raise FileExistsError('refusing to overwrite a completed R131 report')
    data=read_json(args.native)
    if (data.get('kind')!='actual_R126_continuous_Codazzi_Cauchy_validation' or not data.get('complete')
        or data.get('failure') is not None or not data.get('whole_real_angular_circle')
        or not data.get('whole_affine_parameter_interval') or data['covered_interval']!=data['exact_requested_interval']):
        raise ValueError('not a complete true continuous coefficient/residual report')
    for path,key in ((args.object,'object_sha256'),(args.candidate,'candidate_sha256'),
                     (args.producer,'source_sha256'),(args.provider,'coefficient_provider_sha256')):
        if sha(path)!=data[key]:raise ValueError('native input/source identity mismatch: '+str(path))
    if args.tube<=0:raise ValueError('nonpositive C0 bootstrap tube')
    checks=symbolic_checks()
    weighted,initial=initial_weighted_derivative(args.object,Fraction(data['parameter_half_width']),args.nodes,args.angles)
    result=propagate(data,weighted,exact_arb(args.tube))
    doc=dict(kind='R131_true_C0_only_continuation_with_weighted_gradient_transport',source_sha256=sha(__file__),
        complete=True,continuation_certified=result['passed'],closed_surface_complete=False,consumer_revision=2,
        failed_box_policy='Retain every failed gate and its finite input/barrier records; the uncertified derivative bound is null, never infinity.',
        native_path=str(args.native),native_sha256=sha(args.native),native_producer_sha256=data['source_sha256'],
        native_provider_sha256=data['coefficient_provider_sha256'],candidate_sha256=data['candidate_sha256'],
        object_sha256=data['object_sha256'],exact_center_parameter=data['exact_center_parameter'],
        parameter_half_width=data['parameter_half_width'],whole_affine_parameter_interval=True,whole_real_angular_circle=True,
        exact_requested_interval=data['exact_requested_interval'],bits=args.bits,tube=str(args.tube),
        native_old_global_C0_C1_barrier_passed=data.get('continuation_certified'),
        symbolic_polynomial_checks=checks,initial_actual_weighted_derivative=initial,barrier=result,
        reads_candidate_second_theta_derivative=False,reads_residual_theta_derivative=False,
        uses_C1_error_Riccati_gate=False,wall_seconds=time.monotonic()-started,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ('fourfold_phase_codazzi_coefficients.py','fourfold_phase_newton_source_centered.py',
             'fourfold_phase_two_jet_newton_source.py','fourfold_phase_beta_bulk_interval.py')},
        scope='Actual full PDE continuation on the stated strictly negative interval under the R131 theorem; no cap, closed surface, common-metric flex or positive-K continuation.')
    save(args.out,doc)
    print(dict(continuation_certified=result['passed'],initial_weighted=str(weighted),
        final_C0=result.get('final_C0_barrier'),actual_C1=result.get('actual_first_angular_derivative_upper'),
        wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
