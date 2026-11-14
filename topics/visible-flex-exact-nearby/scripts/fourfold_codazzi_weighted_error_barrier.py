#!/usr/bin/env python3
"""Execute the two full R134 linear energy barriers and the actual C0 gate."""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_piecewise_barrier import read_json,up,down
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_two_jet_newton_source import record,save,sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--tube',type=Fraction,default=Fraction(1,16))
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();ctx.prec=a.bits
    if a.out.exists():raise FileExistsError('new output path required')
    d=read_json(a.input)
    if (d.get('kind')!='actual_complete_Codazzi_cleared_polynomial_residual_for_R134'
        or not d.get('complete') or d.get('failure') is not None
        or d['covered_interval']!=d['exact_requested_interval']
        or not d.get('whole_affine_parameter_interval') or not d.get('whole_real_angular_circle')
        or not d.get('exact_denominator_clearing') or not d.get('full_target_quadratic_remainder')):
        raise ValueError('complete actual R134 coefficient/residual input required')
    producer=Path(__file__).with_name('fourfold_codazzi_cleared_polynomial_residual.py')
    if sha(producer)!=d['source_sha256']:raise ValueError('complete residual producer changed')
    for path,digest in d['inputs'].items():
        if sha(Path(path))!=digest:raise ValueError('actual residual input changed: '+path)
    for name,digest in d['dependencies'].items():
        if sha(Path(__file__).with_name(name))!=digest:raise ValueError('residual dependency changed: '+name)
    if a.tube<=0:raise ValueError('positive fixed tube required')
    T=exact_arb(a.tube);tiny=arb(2)**-180;inflation=1+arb(2)**-40
    b0=d['rows'][0]['bounds'];M0=up(b0['Mhat'])+T;g0=down(b0['candidate_gap'])-2*T
    eps0,eps1=(up(d['actual_initial_error'][k]) for k in ('epsilon0','epsilon1'))
    if not g0>0 or not eps0<T:raise ValueError('initial actual tube/gap not strict')
    E0=((2/g0).sqrt()*eps0*inflation+tiny).upper()
    EW=((2/g0).sqrt()*(2*M0*eps1+2*up(b0['D1'])*eps0)*inflation+tiny).upper()
    initial=dict(E0=record(E0),EW=record(EW),eps0=record(eps0),eps1=record(eps1))
    rows=[];failure=None;cursor=Fraction(0);maximum=arb(0);mingap=None
    for i,row in enumerate(d['rows']):
        left,right=map(Fraction,row['interval'])
        if left!=cursor or not left<right:raise ValueError('noncontiguous actual radial interval')
        gl,gr=map(Fraction,row['actual_scalar_germ'])
        if not gl<=left<right<=gr:raise ValueError('actual scalar germ changed')
        b=row['bounds'];h=exact_arb(right-left)
        M=(up(b['Mhat'])+T).upper();g=(down(b['candidate_gap'])-2*T).lower()
        if not g>0:
            failure=dict(row=i,reason='candidate_gap_minus_two_tubes_not_positive',interval=row['interval']);break
        gamma,beta,kappa=(up(b[k]) for k in ('gamma','beta','kappa'))
        L0=(gamma*up(b['S1'])+beta*(3+5*M*M)+2*kappa).upper()
        LW=(beta*(3+7*M*M)+6*kappa).upper()
        C=(gamma*up(b['What1'])+8*beta*M*up(b['What0'])).upper()
        factor=(2/g).sqrt().upper()
        r0,rW=factor*up(b['rho0']),factor*up(b['rhoW'])
        den0,denW=(1-h*L0/2).lower(),(1-h*LW/2).lower()
        if not den0>0 or not denW>0:
            failure=dict(row=i,reason='linear_barrier_denominator_not_positive',interval=row['interval']);break
        next0=(((E0+h*r0)/den0)*inflation+tiny).upper()
        nextW=(((EW+h*(C*next0+rW))/denW)*inflation+tiny).upper()
        margin0=(next0-E0-h*(L0*next0/2+r0)).lower()
        marginW=(nextW-EW-h*(LW*nextW/2+C*next0+rW)).lower()
        recovered=(2*M*(next0*next0+arb.pi()/g*next0*(nextW+2*up(b['D1'])*next0))).sqrt().upper()
        gates=dict(strict_first_energy_barrier=bool(margin0>0),
            strict_weighted_gradient_barrier=bool(marginW>0),
            strict_Sobolev_C0_tube=bool(recovered<T),positive_actual_gap=bool(g>0))
        saved=dict(interval=row['interval'],actual_scalar_germ=row['actual_scalar_germ'],
            initial_E0=record(E0),initial_EW=record(EW),final_E0=record(next0),final_EW=record(nextW),
            actual_M_upper=record(M),actual_gap_lower=record(g),Lambda0=record(L0),LambdaW=record(LW),
            coupling=record(C),first_residual_load=record(r0),weighted_gradient_residual_load=record(rW),
            first_strict_margin=record(margin0),second_strict_margin=record(marginW),
            actual_C0_error_upper=record(recovered),gates=gates)
        rows.append(saved)
        if not all(gates.values()):
            failure=dict(row=i,reason='a_full_linear_or_Sobolev_gate_failed',interval=row['interval'],
                         attempted_C0_error=record(recovered));break
        E0,EW,cursor=next0,nextW,right
        maximum=max(maximum,recovered).upper();mingap=g if mingap is None else min(mingap,g).lower()
    success=failure is None and ['0',str(cursor)]==d['exact_requested_interval']
    out=dict(kind='R134_actual_two_linear_weighted_energy_C0_barrier',complete=True,
        continuation_certified=success,closed_surface_complete=False,failure=failure,
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,
        exact_requested_interval=d['exact_requested_interval'],certified_positive_interval=['0',str(cursor)],
        object_sha256=d['object_sha256'],candidate_sha256=d['candidate_sha256'],
        exact_center_parameter=d['exact_center_parameter'],parameter_half_width=d['parameter_half_width'],
        tube=str(a.tube),source_sha256=sha(__file__),inputs={str(a.input):sha(a.input),str(producer):sha(producer)},
        theorem_inputs={str(p):sha(p) for p in (
            Path('results/R134-weighted-error-energy-and-Sobolev-continuation.md'),
            Path('results/R131-linear-degenerate-weighted-gradient-and-C0-continuation.md'))},
        bits=a.bits,initial=initial,rows=rows,
        certified_maximum_C0_error=record(maximum),
        certified_actual_gap_lower=record(mingap) if mingap is not None else None,
        scope='Only passed full boxes are certified. R131 supplies actual derivative finiteness from the genuine C0 tube and gap. A failed requested endpoint is never promoted to successful continuation.')
    save(a.out,out)
    print(dict(continuation_certified=success,rows=len(rows),failure=failure,
        certified_positive_interval=out['certified_positive_interval'],
        maximum_C0=out['certified_maximum_C0_error'],out=str(a.out)),flush=True)


if __name__=='__main__':main()
