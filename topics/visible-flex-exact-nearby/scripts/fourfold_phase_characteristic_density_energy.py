#!/usr/bin/env python3
"""Actual R110 characteristic-density coupling and full strong-source budgets.

Consumes completed nine-field and old strict-energy certificates. It samples
no geometric primitive. Both characteristic channels and the exact scalar
mean remain. Actual all-time diagonal L2 gains are paid by the R106-derived
small exact report. The higher channel is the three-halves-density transport
of J*y, with every lower-to-higher commutator retained.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import math
from pathlib import Path
import time
import traceback
from flint import arb, acb, acb_mat, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_low_feedback_paid_inputs import norm
from fourfold_phase_strict_core_energy import (
    CompleteEnergyFields, sha, read, save, finite, interval)
from fourfold_phase_strict_core_kernel_tame_energy import (
    closed_second_derivative, up, matrix_record)

OBJECT_SHA='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
ORIGIN_SHA='0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b'
DIRECTION_SHA='8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab'
DENSITY_SHA='65a7c9088ba491e018e3e038f22ef014e71e6cf9d60ed7c303ed38bb8f4e361f'
CENTER=Fraction(-7789843107295549,4611686018427387904)
ETA=Fraction(1,10**9)
FAMILY_KEYS=('object_sha256','origin_inputs_sha256','direction_sha256',
             'exact_parameter_interval','exact_parameter_half_width')


def sup_abs(values):
    answer=max(abs(z).upper() for z in values).upper()
    return finite(answer)


def kernel_commutator(values,derivatives):
    lo=min(z.lower() for z in values);hi=max(z.upper() for z in values)
    constant=arb(float((lo+hi)/2))
    oscillation=sup_abs([z-constant for z in values])
    derivative=sup_abs(derivatives)
    bound=(oscillation+4/arb.pi().sqrt()*(oscillation*derivative).sqrt()).upper()
    return bound,dict(chosen_exact_constant=ball_record(constant),
                      oscillation=ball_record(oscillation),
                      first_derivative=ball_record(derivative),
                      complete_commutator_upper=ball_record(bound))


def kernel_remainder(first,second):
    L1=sup_abs(first);L2=sup_abs(second)
    bound=(6/(2*arb.pi()).sqrt()*(L1*L2).sqrt()+3*L1/2).upper()
    return bound,dict(first_derivative=ball_record(L1),
                      second_derivative=ball_record(L2),
                      complete_signed_remainder_upper=ball_record(bound))


def mixed_radial_theta(fields,name,left,right,nodes):
    """Complete r-theta derivative on closed theta cells.

    Finite theta2 of the radial polynomial pays only its finite angular gap.
    The complete saved r-theta error is added uniformly afterwards.
    """
    u=interval((left-fields.center)/fields.h,(right-fields.center)/fields.h)
    h=exact_arb(fields.h);coeff=[]
    for k in range(fields.K+1):
        value,derivative=arb(0),arb(0)
        for number in fields.raw[name][:,k][::-1]:
            derivative=derivative*u+value
            value=value*u+arb(float(number))
        coeff.append(derivative/h)
    data=[acb(0) for _ in range(nodes)];finite_second=arb(0)
    for k in range(1,fields.K+1):
        w=arb(4*k)
        p=acb(0,coeff[k]) if name in ('v','sigma') else acb(coeff[k])
        n=-p if name in ('v','sigma') else p
        data[(-k)%nodes]=p*acb(0,w)
        data[k%nodes]=n*acb(0,-w)
        finite_second+=2*w*w*abs(coeff[k]).upper()
    error=(fields.errors[name][1][1]+arb.pi()/(4*nodes)*finite_second).upper()
    answer=[]
    for z in acb.dft(data):
        if not z.imag.contains(0):raise ValueError('mixed derivative lost real symmetry')
        answer.append(z.real+arb(0,error))
    return answer


def check_density_budget(path):
    if sha(path)!=DENSITY_SHA:raise ValueError('actual all-time density certificate changed')
    doc=read(path)
    if (not doc.get('complete') or doc.get('kind')!=
            'R110_actual_characteristic_density_L2_transport'):
        raise ValueError('completed actual characteristic-density certificate required')
    if len(doc['gates'])!=16 or not all(x['passed'] is True for x in doc['gates']):
        raise ValueError('the exact density arithmetic gates are incomplete')
    region=doc['proved_region'];prov=doc['provenance']
    if (Fraction(region['parameter_center'])!=CENTER or
            Fraction(region['parameter_half_width'])!=ETA or
            prov['actual_object_sha256']!=OBJECT_SHA):
        raise ValueError('different actual ray family')
    script=Path(__file__).with_name('fourfold_characteristic_density_budget_exact.mjs')
    if sha(script)!=prov['source_sha256']:
        raise ValueError('density arithmetic source differs')
    K0=exact_arb(Fraction(doc['bounds']['density_transport_L2_norm_upper']['exact']))
    Kh=exact_arb(Fraction(doc['bounds']['three_halves_density_transport_L2_norm_upper']['exact']))
    if K0!=exact_arb(Fraction(3101,500)) or Kh!=exact_arb(Fraction(38459,1000)):
        raise ValueError('unexpected true transport constants')
    D=acb_mat(6,6)
    for i,z in enumerate((arb(1),K0,K0,arb(1),Kh,Kh)):D[i,i]=z
    return doc,D


def positive_matrix_exp(B,length,terms):
    """Entrywise rigorous e^(length*B) for a nonnegative upper matrix.

    A complete infinity-norm Taylor remainder is added to every entry.
    This trades a little sharpness for a replayable finite formula; no
    unverified native matrix exponential or eigenvalue is needed.
    """
    if terms<2:raise ValueError('at least two matrix Taylor terms required')
    n=B.nrows()
    if n!=B.ncols():raise ValueError('square comparison matrix required')
    for i in range(n):
        for j in range(n):
            if not B[i,j].imag.contains(0) or not B[i,j].real>=0:
                raise ValueError('comparison matrix is not entrywise nonnegative')
    hB=B*length
    q=max(sum((B[i,j].real.upper() for j in range(n)),arb(0))
          for i in range(n))*length
    q=q.upper()
    eye=acb_mat(n,n)
    for i in range(n):eye[i,i]=1
    total=eye;term=eye
    for k in range(1,terms):
        term=(term*hB)/k
        total=total+term
    qpower=arb(1)
    for _ in range(terms):qpower=qpower*q
    tail=(q.exp()*qpower/math.factorial(terms)).upper()
    finite(tail)
    result=acb_mat(n,n)
    for i in range(n):
        for j in range(n):
            result[i,j]=abs(total[i,j]).upper()+tail
    return result,dict(terms=terms,infinity_radius=ball_record(q),
                       full_entrywise_remainder=ball_record(tail))


def piece(path,D,terms):
    report=read(path)
    if (not report.get('complete') or report.get('kind')!=
            'actual_strict_negative_half_derivative_energy_inputs'):
        raise ValueError('a complete original continuous energy certificate is required')
    if sha(Path(__file__).with_name('fourfold_phase_strict_core_energy.py'))!=report['source_sha256']:
        raise ValueError('original energy source changed')
    for name,digest in report['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('original energy dependency changed: '+name)
    if not (report.get('strict_negative_target_curvature_proved') and
            report.get('full_real_radial_interval_paid') and
            report.get('full_real_theta_circle_paid')):
        raise ValueError('this is not a full strict-negative real radial/angular certificate')
    identity=report['identity']
    if not identity.get('uniform_in_the_entire_real_parameter_interval'):
        raise ValueError('whole real parameter interval is missing')
    if (identity['object_sha256']!=OBJECT_SHA or
            identity['origin_inputs_sha256']!=ORIGIN_SHA or
            identity['direction_sha256']!=DIRECTION_SHA or
            Fraction(identity['exact_parameter_half_width'])!=ETA or
            list(map(Fraction,identity['exact_parameter_interval']))!=[CENTER-ETA,CENTER+ETA]):
        raise ValueError('coefficient rectangle and true ray family differ')
    left,right=map(Fraction,report['exact_physical_interval'])
    if not left<right:raise ValueError('empty actual strict interval')
    field_path=Path(report['input_field_report']['path'])
    if sha(field_path)!=report['input_field_report']['sha256']:
        raise ValueError('actual nine-field report changed')
    fields=CompleteEnergyFields(field_path)
    if fields.doc['identity']!=identity:
        raise ValueError('different true coefficient rectangle')
    nodes=report['angular_closed_cells']
    values,coefficients,moments=fields.evaluate(left,right,nodes)
    tt={name:closed_second_derivative(fields,name,coefficients,nodes)
        for name in ('alpha','v','gamma','sigma')}
    rt={name:mixed_radial_theta(fields,name,left,right,nodes)
        for name in ('alpha','gamma')}
    names=('A','Ainv','t','Bp','Bm','hp','hm','sp','sm')
    rows={name:dict(value=[],theta=[],theta2=[]) for name in names}
    minima={'alpha':None,'gamma':None,'kappa':None}
    for j in range(nodes):
        a=values['alpha']['value'][j];at=values['alpha']['theta'][j]
        ar=values['alpha']['radial'][j];att=tt['alpha'][j]
        g=values['gamma']['value'][j];gt=values['gamma']['theta'][j]
        gr=values['gamma']['radial'][j];gtt=tt['gamma'][j]
        v=values['v']['value'][j];vt=values['v']['theta'][j];vtt=tt['v'][j]
        k=values['kappa']['value'][j]
        if not a>0 or not g>0 or not k>0:
            raise ValueError('a complete closed cell is not strictly negative')
        for name,z in (('alpha',a),('gamma',g),('kappa',k)):
            minima[name]=z.lower() if minima[name] is None else min(minima[name],z.lower())
        A=(g/a).sqrt().sqrt();Ai=1/A;c=(a*g).sqrt()
        ax=at/a;gx=gt/g
        lt=(gx-ax)/4
        lr=(gr/g-ar/a)/4
        ltt=(gtt/g-gx*gx-att/a+ax*ax)/4
        lrt=(rt['gamma'][j]/g-(gr/g)*gx-
             rt['alpha'][j]/a+(ar/a)*ax)/4
        ct=c*(ax+gx)/2
        ctt=c*((att/a-ax*ax+gtt/g-gx*gx)/2+
               (ax+gx)*(ax+gx)/4)
        At=A*lt;Ait=-Ai*lt
        d=values['tau']['value'][j]+values['sigma']['theta'][j]
        dt=values['tau']['theta'][j]+tt['sigma'][j]
        t=d*Ai;t_t=dt*Ai+d*Ait
        bp=lr+(v+c)*lt;bm=lr+(v-c)*lt
        bpt=lrt+(vt+ct)*lt+(v+c)*ltt
        bmt=lrt+(vt-ct)*lt+(v-c)*ltt
        hp=(a*A-v*Ai)/2;hm=(-a*A-v*Ai)/2
        for name,val,der in (('A',A,At),('Ainv',Ai,Ait),('t',t,t_t),
                              ('Bp',bp,bpt),('Bm',bm,bmt)):
            rows[name]['value'].append(val);rows[name]['theta'].append(der)
        rows['hp']['value'].append(hp);rows['hm']['value'].append(hm)
        for name,sign in (('sp',-1),('sm',1)):
            rows[name]['value'].append(v+sign*c)
            rows[name]['theta'].append(vt+sign*ct)
            rows[name]['theta2'].append(vtt+sign*ctt)
    zero={name:sup_abs(row['value']) for name,row in rows.items()}
    comm={};crecord={}
    for name in ('A','Ainv','t','Bp','Bm'):
        comm[name],crecord[name]=kernel_commutator(rows[name]['value'],rows[name]['theta'])
    rem={};rrecord={}
    for name in ('sp','sm'):
        rem[name],rrecord[name]=kernel_remainder(rows[name]['theta'],rows[name]['theta2'])
    P=(zero['t']*zero['Ainv']/8).upper()
    Ep=(comm['t']*zero['Ainv']+zero['t']*comm['Ainv'])/8
    Ep=Ep.upper()
    C=acb_mat([[0,zero['hp'],zero['hm']],
        [zero['t'],P,zero['Bp']+P],
        [zero['t'],zero['Bm']+P,P]])
    R=acb_mat([[0,0,0],
        [comm['t'],rem['sp']+Ep,comm['Bp']+Ep],
        [comm['t'],comm['Bm']+Ep,rem['sm']+Ep]])
    alpha0=sup_abs(values['alpha']['value'])
    M1={name:(moments[name][0][0]+moments[name][0][1]).upper()
        for name in ('alpha','v')}
    Mh={name:up(report['actual_multiplier_and_commutator_inputs'][name]['Mthreehalf'])
        for name in ('alpha','v')}
    HA=(zero['A']+comm['A']).upper();Hi=(zero['Ainv']+comm['Ainv']).upper()
    source0=(zero['A']*M1['alpha']+zero['Ainv']*M1['v']).upper()
    sourceh=(HA*Mh['alpha']+Hi*Mh['v']).upper()
    S0=acb_mat([[0,alpha0,0],[zero['Ainv'],source0,zero['Ainv']],
               [zero['Ainv'],source0,zero['Ainv']]])
    Sh=acb_mat([[0,alpha0,0],[Hi,sourceh,Hi],[Hi,sourceh,Hi]])
    Cstar=acb_mat(6,6);Sstar=acb_mat(6,3)
    for i in range(3):
        for j in range(3):
            Cstar[i,j]=C[i,j];Cstar[i+3,j+3]=C[i,j];Cstar[i+3,j]=R[i,j]
            Sstar[i,j]=S0[i,j];Sstar[i+3,j]=Sh[i,j]
    B=D*Cstar;S=D*Sstar;length=exact_arb(right-left)
    transition,tail=positive_matrix_exp(B,length,terms)
    W=transition*S
    K=[]
    for i in range(6):
        squares=arb(0)
        for j in range(3):
            value=abs(W[i,j]).upper();squares+=value*value
        K.append((length*squares).sqrt().upper())
    # These are positive componentwise maps; the repeated mean is the same
    # actual mean, not an additional free port.
    incoming=acb_mat([[1,0],
        [zero['A'],zero['Ainv']],[zero['A'],zero['Ainv']],
        [1,0],[HA,Hi],[HA,Hi]])
    outgoing=acb_mat([[0,comm['Ainv']/2,comm['Ainv']/2,1,
                      zero['Ainv']/2,zero['Ainv']/2],
                     [0,comm['A']/2,comm['A']/2,0,
                      zero['A']/2,zero['A']/2]])
    doc=dict(complete=True,identity={key:identity[key] for key in FAMILY_KEYS},
        exact_physical_interval=[str(left),str(right)],
        original_energy_report=dict(path=str(path),sha256=sha(path)),
        coefficient_report=dict(path=str(field_path),sha256=sha(field_path)),
        angular_closed_cells=nodes,
        true_positive_lower={name:ball_record(z) for name,z in minima.items()},
        complete_field_suprema={name:ball_record(z) for name,z in zero.items()},
        complete_zero_order_commutators=crecord,
        complete_signed_transport_remainders=rrecord,
        complete_potential_coupling=ball_record(P),
        complete_potential_low_to_high=ball_record(Ep),
        C=matrix_record(C),R=matrix_record(R),
        S_base=matrix_record(S0),S_half=matrix_record(Sh),
        actual_diagonal_gain=matrix_record(D),
        coupling_generator=matrix_record(B),
        source_matrix=matrix_record(S),
        local_comparison_transition=matrix_record(transition),
        transition_complete_tail=tail,
        local_L2_source_kernel=list(map(ball_record,K)),
        incoming_physical_Hthreehalf_Hhalf=matrix_record(incoming),
        outgoing_physical_Hthreehalf_Hhalf=matrix_record(outgoing),
        source_norm='L2(dr; Hhalf f0 direct_sum Hthreehalf fr direct_sum Hthreehalf ftheta), physical frequencies 4k and mean weight one',
        scope='complete actual real radial interval and whole real parameter family; no root/positive collar is crossed')
    return doc,dict(P=transition,K=K,incoming=incoming,outgoing=outgoing)


def collect(pieces,D,direction):
    order=list(range(len(pieces)))
    if direction=='backward':order.reverse()
    full=acb_mat(6,6)
    for i in range(6):full[i,i]=1
    for j in order:full=pieces[j][1]['P']*full
    # Only one D at the original endpoint. The local transitions contain
    # D*C, not a new raw diagonal-flow factor at each spline knot.
    initial=full*D
    suffix=acb_mat(6,6)
    for i in range(6):suffix[i,i]=1
    squares=[arb(0) for _ in range(6)]
    for j in reversed(order):
        local=pieces[j][1]
        k=suffix*acb_mat([[x] for x in local['K']])
        for i in range(6):
            z=abs(k[i,0]).upper();squares[i]+=z*z
        suffix=suffix*local['P']
    kernels=[z.sqrt().upper() for z in squares]
    incoming=pieces[order[0]][1]['incoming']
    outgoing=pieces[order[-1]][1]['outgoing']
    physical=outgoing*initial*incoming
    physical_source=outgoing*acb_mat([[x] for x in kernels])
    source_norm2=arb(0)
    for i in range(2):
        z=abs(physical_source[i,0]).upper();source_norm2+=z*z
    return dict(exact_order=[pieces[j][0]['exact_physical_interval'] for j in order],
        initial_diagonal_gain_insertions=1,
        ordered_coupling_transition=matrix_record(full),
        full_initial_state_comparison=matrix_record(initial),
        global_L2_source_kernel=list(map(ball_record,kernels)),
        physical_Hthreehalf_Hhalf_comparison=matrix_record(physical),
        physical_homogeneous_operator_upper=ball_record(norm(physical).upper()),
        physical_source_components=matrix_record(physical_source),
        physical_source_operator_upper=ball_record(source_norm2.sqrt().upper()),
        complete_source_Gram_rule='For the full five-input G in the common strong source space, the zero-initial physical endpoint (u,pbar) Gram is bounded by physical_source_operator_upper squared times G. No omitted input column or uncharged frame is included.')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--energy-reports',type=Path,nargs='+',required=True)
    ap.add_argument('--density-budget',type=Path,
        default=Path('notes/2026-11-13-R110-characteristic-density-transport.json'))
    ap.add_argument('--matrix-terms',type=int,default=32)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    wall,cpu=time.monotonic(),time.process_time()
    report=dict(kind='actual_characteristic_density_strict_core_two_level_budget',
        complete=False,source_sha256=sha(__file__),bits=args.bits,
        actual_full_core_inverse_proved=False,nonlinear_family_complete=False)
    save(args.out,report)
    try:
        density,D=check_density_budget(args.density_budget)
        paid=[piece(path,D,args.matrix_terms) for path in args.energy_reports]
        paid.sort(key=lambda x:Fraction(x[0]['exact_physical_interval'][0]))
        identity=paid[0][0]['identity']
        cursor=Fraction(paid[0][0]['exact_physical_interval'][0])
        for doc,_ in paid:
            left,right=map(Fraction,doc['exact_physical_interval'])
            if left!=cursor:raise ValueError('gap or overlap in complete strict cover')
            if doc['identity']!=identity:raise ValueError('different whole parameter family')
            cursor=right
        report.update(complete=True,identity=identity,pieces=[p[0] for p in paid],
            exact_physical_interval=[paid[0][0]['exact_physical_interval'][0],str(cursor)],
            actual_density_certificate=dict(path=str(args.density_budget),sha256=sha(args.density_budget)),
            forward=collect(paid,D,'forward'),backward=collect(paid,D,'backward'),
            source_convention='f0=-R0, fr=Rr, ftheta=Rtheta, shifted physical momentum=p_N',
            retained_mean=True,
            regular_cap_column='The sixth regular low input has zero direct core forcing and is retained in the separate full cap/Schur map.',
            limits=['closed truly negative pieces only',
                    'all local fields and parameter errors are retained',
                    'ordinary core, real roots and positive collars are separate',
                    'actual canonical/root/label source frame not paid here',
                    'no full high inverse or nonlinear correction is asserted'])
    except Exception as exc:
        report.update(failure=repr(exc),traceback=traceback.format_exc())
    report.update(CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_strict_core_energy.py',
            'fourfold_phase_strict_core_kernel_tame_energy.py',
            'fourfold_phase_core_energy_fields.py',
            'fourfold_characteristic_density_budget_exact.mjs',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_interval.py',
            'fourfold_phase_low_feedback_paid_inputs.py')})
    save(args.out,report)
    print({key:report.get(key) for key in ('complete','failure','exact_physical_interval','CPU_seconds')},
          flush=True)
    if not report['complete']:raise SystemExit(1)


if __name__=='__main__':
    main()
