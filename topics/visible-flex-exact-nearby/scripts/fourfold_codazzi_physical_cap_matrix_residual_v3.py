#!/usr/bin/env python3
"""Complete error of the padded physical cap on the true moving96 inlet.\n\nAll 97 even moving input basis vectors (mean and normalized cosines), all\n257 physical states, and every full physical output are retained. The left\ninlet is the genuine directed H128x97 map with its complete physical tail.

Consumes the shared dyadic Hermite nodal values and one-sided derivatives
in the same working directory as the finite graph producer.  All physical
Fourier products, all 96 columns, the even mean, genuine outer DN error,
parameter interval, scalar tails and independent radial cells are kept.
The exact infinite coefficient remainder is a divergence source where
appropriate.  A finite QR success is not substituted for this certificate.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
from math import factorial
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_physical_cap_coefficient_jets import (
    PhysicalCapCoefficientJets,CURRENT,REPAIR,ffrac)
from fourfold_codazzi_reciprocal_continuous_residual_v3 import (
    add,mul,scale,evaluate,polynomial_at_affine,scalar_budget,BudgetPolynomial)
from fourfold_phase_beta_bulk_box import Box,CBox,zeros,arb_box,reduce_box
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha

KIND='complete_repaired_physical128_cap_moving96_inlet_residual_v3'
PROPOSALS={'actual_repaired_physical128_cap_precomposed_moving96_L2_proposal_v1'}
LEFT=Fraction(9,10);RIGHT=Fraction(25,8)


def read(path):
    p=Path(path);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)


def hs_bound(value):
    """Upper bound for the complete complex Fourier/column Euclidean norm."""
    upper=value.magnitude_upper() if isinstance(value,CBox) else Box.coerce(value).abs_upper()
    squared=Box(upper)*Box(upper)
    total=reduce_box(squared.reshape(-1))
    return arb(float(total.hi)).sqrt().upper()


def amplitude_hs(value,mean=False):
    return (hs_bound(Box.coerce(value))/(1 if mean else arb(2).sqrt())).upper()


def hermite_series(y0,y1,d0,d1,node0,node1,left,right):
    """Enclose exact rational Hermite coefficients, without new value jumps."""
    step=node1-node0;h=arb_box(exact_arb(step))
    a0=Box(y0);a1=Box(d0)*h
    a2=3*(Box(y1)-Box(y0))-h*(2*Box(d0)+Box(d1))
    a3=2*(Box(y0)-Box(y1))+h*(Box(d0)+Box(d1))
    offset=((left+right)/2-node0)/step;half=(right-left)/(2*step)
    value=polynomial_at_affine([a3,a2,a1,a0],offset,half)
    derivative=polynomial_at_affine([3*a3/h,2*a2/h,a1/h],offset,half)
    return value,derivative


def lift(values,m,N):
    columns=values.lo.shape[1];out=zeros((N,2,columns))
    b,c=values[:m],values[m:]
    out[1:m+1,0]=CBox(0.,-b/2);out[-m:,0]=CBox(0.,b[::-1]/2)
    out[0,1]=CBox(c[0]);out[1:m+1,1]=CBox(c[1:]/2)
    out[-m:,1]=CBox(c[1:][::-1]/2)
    return out


def synthesis(poly,m,N,fft):
    columns=poly[0].lo.shape[1];block=zeros((N,2*len(poly),columns));full=[]
    for j,c in enumerate(poly):
        row=lift(c,m,N);full.append(row);block[:,2*j:2*j+2]=row
    values=fft.fft(block,inverse=True)*N
    if not np.all((values.imag.lo<=0)&(values.imag.hi>=0)):
        raise ArithmeticError('complete real Hermite Fourier synthesis lost reality')
    fields=[[values.real[:,2*j+k] for j in range(len(poly))] for k in range(2)]
    norms=[]
    for component in range(2):
        bound=Box(np.zeros((N,columns)))
        for row in full:bound=bound+Box(row[:,component].magnitude_upper())
        norms.append(hs_bound(bound))
    return fields,norms


def coefficient_samples(model,N,fft):
    block=zeros((N,len(model.coefficients)))
    for j,c in enumerate(model.coefficients):block[:,j]=c
    values=fft.fft(block,inverse=True)*N
    if not np.all((values.imag.lo<=0)&(values.imag.hi>=0)):
        raise ArithmeticError('selected exact real coefficient model lost reality')
    return [values.real[:,j].reshape(N,1) for j in range(len(model.coefficients))]


def double_factorial(n):
    value=1
    while n>0:value*=n;n-=2
    return value


def radial_legendre(value):
    """Exact monomial-to-Legendre change; all coefficients are rational."""
    result=[]
    for k in range(len(value)):
        row=value[0]*0
        for n in range(k,len(value),2):
            coefficient=Fraction((2*k+1)*factorial(n),
                double_factorial(n-k)*double_factorial(n+k+1))
            row=row+value[n]*arb_box(exact_arb(coefficient))
        result.append(row)
    return result


def finite_component(volume,flux,component,N,support,columns,fft):
    length=max(len(volume),len(flux));block=zeros((N,2*length,columns))
    for j,c in enumerate(volume):block[:,2*j]=CBox(c)
    for j,c in enumerate(flux):block[:,2*j+1]=CBox(c)
    coefficients=fft.fft(block)/N
    modes=np.asarray([k if k<N//2 else k-N for k in range(N)])
    angular=CBox(0.,Box(4*modes).reshape(N,1))
    outside=abs(modes)>support;polynomial=[];orders=[]
    inverse_root=[]
    for mode in modes:
        value=arb(0) if mode==0 else (arb(1)/(4*abs(int(mode)))).sqrt()
        inverse_root.append(arb_box(value))
    weight=Box(np.array([v.lo for v in inverse_root]),
               np.array([v.hi for v in inverse_root])).reshape(N,1)
    for j in range(length):
        value=coefficients[:,2*j]+angular*coefficients[:,2*j+1]
        if not (np.all((value.real.lo[outside]<=0)&(value.real.hi[outside]>=0))
                and np.all((value.imag.lo[outside]<=0)&(value.imag.hi[outside]>=0))):
            raise ArithmeticError('a mathematically absent finite convolution mode lost zero')
        value[outside]=0.
        if component==0:
            if not np.all((value.real.lo<=0)&(value.real.hi>=0)):
                raise ArithmeticError('the exact odd B residual lost its real Fourier zero')
            value=CBox(0.,value.imag);value[0]=0.
        else:
            if not np.all((value.imag.lo<=0)&(value.imag.hi>=0)):
                raise ArithmeticError('the exact even C residual lost its imaginary Fourier zero')
            value=CBox(value.real)
        polynomial.append(value);orders.append(hs_bound(value))
    square=arb(0);mean_square=arb(0);ordinary_square=arb(0)
    for k,value in enumerate(radial_legendre(polynomial)):
        square+=hs_bound(value*weight)**2/(2*k+1)
        mean_square+=hs_bound(value[0])**2/(2*k+1)
        ordinary_square+=hs_bound(value)**2/(2*k+1)
    return dict(nonmean_inverse_sqrt_M_L2_average=square.sqrt().upper(),
        complete_mean_L2_average=mean_square.sqrt().upper(),
        complete_ordinary_L2_average=ordinary_square.sqrt().upper(),
        radial_order_HS=orders)


def truncate_scalar(value,degree=3):
    """Move every omitted scalar coefficient into its full uniform error."""
    fee=sum((arb(float(z.abs_upper())).upper() for z in value.coefficients[degree+1:]),arb(0))
    return BudgetPolynomial(value.coefficients[:degree+1],value.norm,value.error+fee)


def cell_residual(provider,coefficient,values,derivative,m=96):
    N=provider.N;columns=values[0].lo.shape[1]
    if N<=2*(m+provider.cutoff):raise ValueError('full physical convolution support is not resolved')
    (B,C),(Bn,Cn)=synthesis(values,m,N,provider.fft)
    (Br,Cr),_=synthesis(derivative,m,N,provider.fft)
    qb,qc=coefficient['models']['QB'],coefficient['models']['QC']
    Q=add(mul(coefficient_samples(qb,N,provider.fft),B),
          mul(coefficient_samples(qc,N,provider.fft),C))
    g,b,K,s=[scalar_budget(coefficient['scalar'][name]) for name in ('gamma','beta','K','s')]
    ell=K*s*s;a=truncate_scalar(g*ell);e=truncate_scalar(b*(ell+1))
    VB=add(Br,scale(mul(b.coefficients,B),2))
    FB=add(mul(a.coefficients,C),scale(mul(g.coefficients,Q),-1))
    VC=add(add(Cr,mul(e.coefficients,C)),scale(mul(b.coefficients,Q),-1))
    FC=scale(mul(g.coefficients,B),-1)
    finite=[]
    for component,volume,flux in ((0,VB,FB),(1,VC,FC)):
        finite.append(finite_component(volume,flux,component,N,m+provider.cutoff,columns,provider.fft))
    model_mix=(qb.norm*Bn+qc.norm*Cn).upper()
    error_mix=(qb.error*Bn+qc.error*Cn).upper()
    rB=(2*b.error*Bn).upper()
    rC=(e.error*Cn+b.error*model_mix+(b.norm+b.error)*error_mix).upper()
    dB=(a.error*Cn+g.error*model_mix+(g.norm+g.error)*error_mix).upper()
    dC=(g.error*Bn).upper()
    return dict(ordinary_remainder_HS=(rB,rC),divergence_module_HS=(dB,dC),
        finite_ordinary=finite,complete_Hermite_module_HS=(Bn,Cn),
        full_support=m+provider.cutoff,independent_columns=columns,
        scalar_remainder={name:record(z.error) for name,z in (('gamma',g),('beta',b),('gamma_ell',a),('beta_ell_plus_one',e))})


def boundary_error(state,left_derivative,right_derivative,nodes,q_vector,q_native,inlet_path):
    """True physical inlet, all outer rows, and the independent C mean."""
    m=128
    inlet=read(inlet_path)
    if (inlet.get('kind')!='actual_repaired_moving96_physical128_complete_C_port_matrix'
        or not inlet.get('complete') or inlet['candidate_sha256']!=CURRENT
        or inlet['derived_definition_sha256']!=REPAIR or inlet['exact_cut']!='9/10'
        or not inlet['whole_original_eta'] or inlet['parameter_half_width']!='1/1000000000'
        or inlet['physical_rows']!=128 or len(inlet['input_columns'])!=97
        or any(not gate['passed'] for gate in inlet['gates'])):
        raise ValueError('the actual complete directed moving-to-physical C inlet is required')
    poly,_=hermite_series(state[0],state[1],left_derivative[0],right_derivative[0],
                         nodes[0],nodes[1],LEFT,LEFT)
    value=evaluate(poly,Box(0.))
    den=int(inlet['exact_interval_denominator']);lo=np.empty((128,97));hi=np.empty_like(lo)
    for l,row in enumerate(inlet['rows'],1):
        if row['physical_index']!=l or row['physical_frequency']!=4*l:
            raise ValueError('every true physical inlet mode is required')
        for j,(a,b) in enumerate(row['exact_interval_numerators']):
            true=exact_arb(Fraction(int(a),den)).union(exact_arb(Fraction(int(b),den)))
            if j:true*=arb(2).sqrt()
            boxed=arb_box(true);lo[l-1,j]=boxed.lo;hi[l-1,j]=boxed.hi
    finite=amplitude_hs(value[m+1:]-Box(lo,hi))
    tail=box_from_record(inlet['complete_physical_tail_L2_gain']).upper()
    # Disjoint physical output modes are orthogonal. The finite part is
    # HS-bounded; the tail is the actual full L2 operator bound (not HS).
    eL=(finite*finite+tail*tail).sqrt().upper()
    q=read(q_vector);native=read(q_native)
    if not native.get('complete') or not native.get('whole_affine_parameter_interval'):
        raise ValueError('the original complete true qstar enclosure is required')
    if native['object_sha256']!=q['object_sha256']:raise ValueError('outer intrinsic object changed')
    qs=box_from_record(native['bounds']['actual_qstar'])
    vector=np.asarray(q['q_values'][:m],dtype=float)
    if vector.shape!=(m,):raise ValueError('every actual outer proposal row is required')
    right=Box(state[-1]);Cne=amplitude_hs(right[m+1:])
    model=amplitude_hs(right[:m]+Box(vector).reshape(m,1)*right[m+1:])
    qfee=max((abs(qs-arb(float(v))).upper() for v in vector)).upper()+arb(2)**-512
    eD=(model+(qfee+arb('0.000005898255'))*Cne).upper()
    e0=(hs_bound(right[m])+arb('0.0000007372818')*Cne).upper()
    meanlo,meanhi=inlet['physical_mean_row']['exact_interval_numerator']
    mr=exact_arb(Fraction(int(meanlo),den)).union(exact_arb(Fraction(int(meanhi),den)))
    true_mean=Box(np.zeros(97));true_mean[0]=arb_box(mr)
    mean_gap=true_mean-value[m]
    return dict(e_L=eL,e_D=eD,e_0=e0,e_B0=arb(0),j_B=arb(0),j_C=arb(0),
        exact_L2_input_basis_verified=True,
        actual_left_finite_inlet_HS=finite,actual_left_complete_input_tail=tail,
        actual_right_C_nonmean_HS=Cne,actual_model_Robin_HS=model,
        complete_true_q_to_floating_proposal_fee=qfee.upper(),
        outer_nonlinear_DN_L2=arb('0.000005898255'),outer_nonlinear_mean_L2=arb('0.0000007372818'),
        left_mean_matching_row_HS=hs_bound(mean_gap),
        left_mean_is_independent_matching_row_not_input=True)



GAIN_KEYS=dict(e_L='inner_C_port',e_D='outer_nonzero_d_port',e_0='outer_Cmean_port',
    e_B0='outer_Bmean_port',r_B='ordinary_L2rL2_B_source',r_C='ordinary_L2rL2_C_source',
    d_B='divergence_module_B_source',d_C='divergence_module_C_source',
    j_B='physical_B_jump_l1_source',j_C='physical_C_jump_l1_source')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True);ap.add_argument('--proposal',type=Path,required=True)
    ap.add_argument('--inlet',type=Path,default=Path('notes/2026-11-14-R133-repaired-moving96-physical128-C-matrix-native.json.gz'))
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--repair-report',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--cap-green',type=Path,default=Path('notes/2026-11-14-R133-continuous-repair-physical-cap-background-v2-native.json.gz'))
    ap.add_argument('--reference-cap',type=Path,default=Path('notes/2026-11-14-R133-final-physical-cap-linear-module-r09-v2-native.json.gz'))
    ap.add_argument('--q-vector',type=Path,default=Path('notes/2026-11-13-R133-regular-r25over8-q256-floating.json'))
    ap.add_argument('--q-native',type=Path,default=Path('notes/2026-11-13-R133-regular-r25over8-q256-long-ports-native.json.gz'))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9));ap.add_argument('--strip',type=Fraction,default=Fraction(1,16))
    ap.add_argument('--angles',type=int,default=512);ap.add_argument('--cutoff',type=int,default=127)
    ap.add_argument('--first',type=int,default=0);ap.add_argument('--count',type=int)
    ap.add_argument('--subdivide',type=int,default=1);ap.add_argument('--resume',type=Path)
    ap.add_argument('--parts',type=Path,nargs='*')
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every completed or partial matrix certificate')
    if args.subdivide<1:raise ValueError('invalid subdivision')
    proposal=read(args.proposal);green=read(args.cap_green)
    candidate_index=read(args.candidate);candidate_metadata=candidate_index['metadata']
    object_sha=sha(args.object)
    if (proposal.get('kind') not in PROPOSALS or not proposal.get('complete') or proposal.get('failure')
        or not proposal.get('parent_finite_gate_only',{}).get('passed')):
        raise ValueError('the complete actual physical128 cap precomposed with moving96 is required')
    if (not green.get('complete') or green.get('derived_definition_sha256')!=REPAIR
        or green.get('original_candidate_sha256')!=CURRENT):raise ValueError('actual repaired all-mode cap Green changed')
    if (sha(args.candidate)!=CURRENT
        or candidate_metadata['object_sha256']!=object_sha
        or green['object_sha256']!=object_sha
        or proposal['identity']['model']['object_sha256']!=object_sha
        or read(args.q_native)['object_sha256']!=object_sha
        or read(args.q_vector)['object_sha256']!=object_sha):
        raise ValueError('the full intrinsic object must be identical in every actual input')
    if (proposal['identity']['model']['exact_alpha']!=candidate_metadata['exact_float_amplitude']
        or proposal['identity']['model']['exact_nu']!=candidate_metadata['exact_float_nu']):
        raise ValueError('the actual amplitude or fixed metric parameter changed')
    if green['exact_interval']!=[str(LEFT),str(RIGHT)]:
        raise ValueError('the complete original physical cap interval is required')
    directory=Path(proposal['work_directory']);matrix=directory/'matrix-RHS'
    files=[matrix/'state.npy',matrix/'derivative-left.npy',matrix/'derivative-right.npy',
           directory/'physical-endpoint-graph.npz']
    if sha(files[0])!=proposal['full_matrix_state']['sha256']:raise ValueError('complete matrix values changed')
    if sha(files[3])!=proposal['physical_endpoint_graph']['sha256']:raise ValueError('complete endpoint graph changed')
    for p in files[:3]:
        if sha(p)!=proposal['full_matrix_inputs'][str(p)]:
            raise ValueError('a complete precomposed state or one-sided derivative changed')
    if sha(args.inlet)!=proposal['actual_physical_inlet_matrix']['sha256']:
        raise ValueError('the actual directed inlet matrix bytes changed')
    state,dl,dr=[np.load(p,mmap_mode='r',allow_pickle=False) for p in files[:3]]
    endpoint=np.load(files[3],allow_pickle=False);nodes=list(map(ffrac,endpoint['nodes']))
    if state.shape!=(len(nodes),257,97) or dl.shape!=(len(nodes)-1,257,97) or dr.shape!=dl.shape:
        raise ValueError('every original physical state, derivative and input column is required')
    if not np.array_equal(state[0],endpoint['left_state']) or not np.array_equal(state[-1],endpoint['right_state']):
        raise ValueError('the endpoint proposal is not from these full matrix states')
    provider=PhysicalCapCoefficientJets(args.candidate,args.object,args.repair_report,
        half_width=args.half_width,width=args.strip,angles=args.angles,cutoff=args.cutoff)
    expected=np.r_[float(LEFT),provider.saved['radial_nodes'][provider.saved['radial_nodes']>float(LEFT)]]
    from fourfold_codazzi_physical_cap_DN_refined_proposal import refined_nodes
    expected=refined_nodes(expected)
    if not np.array_equal(endpoint['nodes'],expected):raise ValueError('complete actual cap proposal partition changed')
    if proposal['identity']['model']['derived_centre_definition_sha256']!=REPAIR:
        raise ValueError('the matrix was built for another centre')
    if proposal['identity']['model']['q_vector_sha256']!=sha(args.q_vector):raise ValueError('floating outer rows changed')
    if args.half_width>Fraction(green['background_parameter_half_width']):raise ValueError('Green parameter scope is too small')
    reference=read(args.reference_cap)
    if (not reference.get('complete') or sha(args.reference_cap)!=green['cap_input_sha256']
        or reference['object_sha256']!=object_sha or reference['candidate_sha256']!=CURRENT
        or reference['exact_interval']!=[str(LEFT),str(RIGHT)]):
        raise ValueError('the original complete all-mode reference Green changed')
    rb=reference['bounds']
    qp=box_from_record(rb['q_upper']).upper();T=box_from_record(rb['triangular_coupling']).upper()
    sd=box_from_record(rb['D_rate_per_M']).lower();sc=box_from_record(rb['C_rate_per_M']).lower()
    if not sd>0 or not sc>0:raise ValueError('strict full-mode decay is required')
    HD=1+(1+qp)*T;HC=1+qp
    resolvent=box_from_record(green['bounds']['corrected_physical_cap_resolvent']).upper()
    weighted_gains=dict(f_B=(resolvent*HD/(2*sd).sqrt()).upper(),
        f_C=(resolvent*(HD*qp/(2*sd).sqrt()+HC/(2*sc).sqrt())).upper(),
        f_B0=(resolvent*box_from_record(rb['ordinary_L2rL2_B_source']).upper()).upper(),
        f_C0=(resolvent*box_from_record(rb['ordinary_L2rL2_C_source']).upper()).upper())
    cuts=sorted({LEFT,RIGHT}|{x for x in nodes+provider.knots+provider.target.cuts if LEFT<x<RIGHT})
    cells=[(a+(b-a)*j/args.subdivide,a+(b-a)*(j+1)/args.subdivide)
           for a,b in zip(cuts,cuts[1:]) for j in range(args.subdivide)]
    end=len(cells) if args.count is None else min(len(cells),args.first+args.count)
    if not 0<=args.first<end:raise ValueError('empty selected full-cell range')
    dependencies={n:sha(Path(__file__).with_name(n)) for n in (
        'fourfold_codazzi_physical_cap_coefficient_jets.py',
        'fourfold_codazzi_reciprocal_continuous_residual_v3.py',
        'fourfold_phase_beta_bulk_box.py','fourfold_phase_root_interval.py',
        'fourfold_codazzi_physical_cap_precompose_moving_head.py',
        'fourfold_codazzi_physical_cap_DN_refined_proposal.py')}
    identity=dict(base_candidate_sha256=CURRENT,derived_definition_sha256=REPAIR,
        proposal_sha256=sha(args.proposal),original_case=proposal['case'],
        exact_physical_inlet_matrix_sha256=sha(args.inlet),
        complete_input_basis='1,sqrt(2)*cos(4*j*phi), j=1,...,96; normalized circle L2',
        physical_modes=128,moving_even_input_columns=97,
        full_matrix_inputs={str(p):sha(p) for p in files},
        object_sha256=sha(args.object),cap_green_sha256=sha(args.cap_green),
        q_vector_sha256=sha(args.q_vector),q_native_sha256=sha(args.q_native),
        full_reference_cap_sha256=sha(args.reference_cap),
        parameter_half_width=str(args.half_width),analytic_width=str(args.strip),
        angles=args.angles,cutoff=args.cutoff,subdivide=args.subdivide,
        complete_original_cell_count=len(cells),source_sha256=sha(__file__),dependencies=dependencies)
    names=('weighted_finite_B_square_integral','weighted_finite_C_square_integral',
           'finite_Bmean_square_integral','finite_Cmean_square_integral',
           'ordinary_B_remainder_square_integral','ordinary_C_remainder_square_integral',
           'divergence_B_module_square','divergence_C_module_square')
    rows=[];sums=[arb(0) for _ in range(len(names))]
    if args.resume and args.parts:
        raise ValueError('choose an unchanged prefix or complete disjoint parts, not both')
    if args.parts:
        if args.first!=0 or end!=len(cells):
            raise ValueError('assembly must cover the complete original cap interval')
        for path in args.parts:
            part=read(path)
            if (part.get('kind')!=KIND or part['identity']!=identity or part.get('failure')
                or not part.get('selected_cells_complete') or part['first']!=len(rows)
                or part['end']-part['first']!=len(part['rows'])):
                raise ValueError('every assembled part must be a complete original contiguous block')
            for row in part['rows']:
                index=len(rows)
                if row['index']!=index or row['interval']!=list(map(str,cells[index])):
                    raise ValueError('the exact assembled common closed cover changed')
                rows.append(row)
                for k,name in enumerate(names):sums[k]+=box_from_record(row['accumulator_terms'][name])
        if len(rows)!=len(cells):raise ValueError('partial coverage is not a complete cap certificate')
    if args.resume:
        previous=read(args.resume)
        if previous['identity']!=identity or previous['first']!=args.first or previous.get('failure'):
            raise ValueError('only an unchanged actual completed prefix can be resumed')
        rows=previous['rows']
        for offset,row in enumerate(rows):
            index=args.first+offset
            if row['index']!=index or row['interval']!=list(map(str,cells[index])):
                raise ValueError('the saved complete prefix is not contiguous')
            for k,name in enumerate(names):
                sums[k]+=box_from_record(row['accumulator_terms'][name])
    doc=dict(kind=KIND,complete=False,failure=None,identity=identity,first=args.first,end=end,
        rows=rows,full_unknown_physical_Fourier_tail_retained=True,
        exact_continuous_Hermite_values_no_point_sources=True,
        independent_input_columns=97,physical_state_dimension=257,
        actual_moving_L2_basis_including_mean=True,physical_Cmean_matching_row_retained=True,
        ordinary_norm='finite nonmean: Hilbert-Schmidt ell2_97 to L2_r M^-1/2 L2_theta; complete mean and infinite coefficient error separate',
        finite_radial_L2_method='exact rational Legendre transformation and orthogonality; all output modes and input columns',
        complete_weighted_reference_gains={k:record(v) for k,v in weighted_gains.items()},
        divergence_norm='Hilbert-Schmidt ell2_97 to l2_k(sup_r), with sum of cell squares',
        whole_body_inverse_or_nonlinear_solution_claimed=False)
    if args.parts:doc['assembled_parts']={str(p):sha(p) for p in args.parts}
    try:
        for index in range(args.first+len(rows),end):
            left,right=cells[index];piece=max(0,bisect_right(nodes,left)-1)
            if not (nodes[piece]<=left or piece==0 and left==LEFT) or right>nodes[piece+1]:
                raise ValueError('a residual cell crosses an exact matrix Hermite join')
            values,derivative=hermite_series(state[piece],state[piece+1],dl[piece],dr[piece],
                                             nodes[piece],nodes[piece+1],left,right)
            co=provider.coefficients(left,right);rr=cell_residual(provider,co,values,derivative,m=128)
            length=exact_arb(right-left)
            finite=rr['finite_ordinary']
            component_values=[v['nonmean_inverse_sqrt_M_L2_average'] for v in finite]+[v['complete_mean_L2_average'] for v in finite]
            terms=[length*x*x for x in component_values+list(rr['ordinary_remainder_HS'])]+[x*x for x in rr['divergence_module_HS']]
            row=provider.row(co);row.update(index=index,matrix_piece=piece,
                finite_ordinary_L2={k:{kk:record(vv) for kk,vv in v.items() if kk!='radial_order_HS'} for k,v in zip(('B','C'),finite)},
                complete_ordinary_remainder_HS={k:record(v) for k,v in zip(('B','C'),rr['ordinary_remainder_HS'])},
                complete_divergence_module_HS={k:record(v) for k,v in zip(('B','C'),rr['divergence_module_HS'])},
                complete_trial_module_HS={k:record(v) for k,v in zip(('B','C'),rr['complete_Hermite_module_HS'])},
                finite_radial_order_HS={k:[record(x) for x in v['radial_order_HS']] for k,v in zip(('B','C'),finite)},
                scalar_remainder=rr['scalar_remainder'],full_resolved_support=rr['full_support'],
                accumulator_terms={k:record(v.upper()) for k,v in zip(names,terms)})
            rows.append(row);sums=[(a+b).upper() for a,b in zip(sums,terms)]
            doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
            print(json.dumps(dict(completed_rows=len(rows),requested=end-args.first,index=index,
                residual_prefix=[float(x.sqrt().upper()) for x in sums],wall_seconds=doc['wall_seconds'])),flush=True)
        doc['selected_cells_complete']=True
        if args.first==0 and end==len(cells):
            boundary=boundary_error(state,dl,dr,nodes,args.q_vector,args.q_native,args.inlet)
            errors={**boundary,**{k:v.sqrt().upper() for k,v in zip(('f_B','f_C','f_B0','f_C0','r_B','r_C','d_B','d_C'),sums)}}
            gains={k:box_from_record(green['corrected_all_mode_physical_Green_gains'][v]).upper()
                   for k,v in GAIN_KEYS.items()}
            gains.update(weighted_gains)
            fees={k:(gains[k]*errors[k]).upper() for k in gains}
            epsilon=sum(fees.values(),arb(0)).upper()
            doc.update(complete=True,complete_actual_cap_graph_error=record(epsilon),
                complete_error_data={k:(record(v) if isinstance(v,arb) else v) for k,v in errors.items()},
                complete_actual_input_matrix_tail_and_independent_mean_preserved=True,
                actual_Green_gains={k:record(v) for k,v in gains.items()},
                full_independent_error_contributions={k:record(v) for k,v in fees.items()},
                all_unretained_output_modes_included=True,
                all_ordinary_divergence_mean_true_Robin_and_endpoint_terms_consumed=True)
    except Exception as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error),completed_rows=len(rows))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(json.dumps(dict(complete=doc['complete'],failure=doc['failure'],rows=len(rows),wall_seconds=doc['wall_seconds'])),flush=True)
    if doc['failure']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
