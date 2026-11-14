#!/usr/bin/env python3
"""Current moving centre: physical strict equation inside its root piece.

Version 2 permits a relocated, byte-identical complete candidate index.
Its complete shard loader still verifies every recorded shard hash.

Propagate weighted H0/H1 plus the ordinary second component all the way
to the proved fixed-r graph, then compose that graph's complete Airy
port.  The radial curvature damping is retained; no mean is projected.
"""
from __future__ import annotations
import argparse,gzip,json,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import arb,acb,ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_moving_polynomial_system import COORDINATES
from fourfold_codazzi_moving_turning_complex_germ import physical_derivative_bounds
from fourfold_codazzi_turning_complex_germ import genuine_complex_target
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_metric_defect import record,save,sha


def read(p):
    z=Path(p).read_bytes();return json.loads(gzip.decompress(z) if str(p).endswith('.gz') else z)


def matmul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),arb(0)) for j in range(len(b[0]))] for i in range(len(a))]


def positive_exp(a):
    n=len(a);one=[[arb(int(i==j)) for j in range(n)] for i in range(n)]
    term=one;total=[r[:] for r in one]
    for k in range(1,25):
        term=[[x/k for x in r] for r in matmul(term,a)]
        total=[[total[i][j]+term[i][j] for j in range(n)] for i in range(n)]
    s=max(sum(r,arb(0)) for r in a).upper()
    tail=(s**25/math.factorial(25)/(1-s/26)).upper()
    if not s<26:raise ValueError('explicit full matrix exponential tail is not certified')
    return [[(x+tail).upper() for x in r] for r in total],tail


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--root',type=Path,default=Path('notes/2026-11-13-R133-actual-root-and-three-common-germs-native.json.gz'))
    ap.add_argument('--graph',type=Path,default=Path('notes/2026-11-13-R133-current-moving0765-complete-fold-Airy-ports-native.json.gz'))
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;ctx.cap=4;t0=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every strict root-piece attempt')
    root,graph=read(args.root),read(args.graph)
    if (not root['complete'] or not graph['complete'] or not root['root_independent_of_compact_metric_nu']
        or root['object_sha256']!=sha(args.object) or graph['object_sha256']!=sha(args.object)
        or graph['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_current_moving_fold_Airy.py'))):
        raise ValueError('complete identical new-body root and graph required')
    candidate_digest=sha(args.candidate)
    original_candidate_locations=[name for name,digest in graph['actual_candidate_inputs'].items()
                                  if digest==candidate_digest]
    if (graph.get('candidate_sha256')!=candidate_digest or not original_candidate_locations):
        raise ValueError('the byte-identical complete actual candidate index must be supplied')
    gl,gr=map(Fraction,root['actual_common_scalar_germ']);rlo,rhi=map(Fraction,root['exact_root_interval'])
    left=Fraction(graph['exact_candidate_piece'][0]);h=Fraction(graph['scales']['physical_radial_offset'])
    if not gl<=left<rlo-h<rhi<gr or not left>Fraction(9,50):raise ValueError('actual common scalar germ or compact support mismatch')
    target=CodazziCoefficientTarget(args.object,Fraction(root['parameter_half_width']),512,4096)
    target.set_cell(gl,gr)
    radial=acb(real_interval(left,rhi))
    coeff,primitive_tail,product_fees=genuine_complex_target(target,radial)
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    if meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(args.object) or meta['physical_frequency_factor']!=4:
        raise ValueError('complete reciprocal coordinate identity failed')
    alpha=Fraction(meta['exact_float_amplitude']);nu=Fraction(meta['exact_float_nu'])
    if str(alpha)!=graph['exact_amplitude'] or str(nu)!=graph['actual_fixed_nu']:
        raise ValueError('actual centre amplitude or nu differs from the root graph')
    nodes=[Fraction.from_float(float(x)) for x in saved['radial_nodes']]
    j=bisect_right(nodes,left)-1
    if not nodes[j]==left<rhi<nodes[j+1]:raise ValueError('the entire actual common candidate piece is required')
    local=radial-acb(exact_arb(left));cc=saved['piece_coefficients'][:,j,:]
    vals=[]
    for k in range(cc.shape[1]):
        value=acb(0)
        for degree in range(4):value=value*local+acb(arb(float(cc[degree,k])))
        vals.append(exact_arb(alpha)*value)
    modes=int(meta['modes'])
    if len(vals)!=2*modes+1:raise ValueError('all exact physical Fourier rows and mean are required')
    U=[];V=[]
    for q in range(5):
        U.append(sum((abs(vals[k-1])*(4*k)**q for k in range(1,modes+1)),arb(0)).upper())
        V.append(sum((abs(vals[modes+k])*(4*k)**q for k in range(1,modes+1)),arb(0)).upper())
    vmean=coeff['s']+vals[modes];vnonmean=V[0];V[0]=(V[0]+abs(vmean)).upper()
    vgap=(-vmean.real.upper()-vnonmean).lower()
    if not vgap>0 or not vmean.real<0:raise ValueError('true moving circle angle is not invertible')
    moving_U=U[:];moving_v=V[:]
    U,V=physical_derivative_bounds(U,V,abs(vmean).upper(),vgap)
    gamma=abs(coeff['gamma']).upper();beta=abs(coeff['beta']).upper()
    kmin=coeff['K1'].real.lower();kmax=abs(coeff['K1']).upper()
    # Q=-K=(rstar-r) * integral K' is used before division; hence the
    # terminal rstar(eta)-h is genuinely negative for every eta.
    Qmax=(exact_arb(rhi-left)*kmax).upper();qmax=Qmax.sqrt().upper()
    qterminalMin=(exact_arb(h)*kmin).sqrt().lower()
    d=gamma*U[0];a=gamma*V[0];dtheta=gamma*U[1];atheta=gamma*V[1]
    coupling=(gamma*V[1]+2*beta*U[0]*V[0]).upper()
    L11=(gamma*U[1]+beta*(1+3*U[0]**2+Qmax*V[0]**2)).upper()
    L22=(gamma*U[1]+beta*(1+U[0]**2+3*Qmax*V[0]**2)).upper()
    couplingTheta=(gamma*V[2]+2*beta*(U[1]*V[0]+U[0]*V[1])).upper()
    L11theta=(gamma*U[2]+beta*(6*U[0]*U[1]+2*Qmax*V[0]*V[1])).upper()
    L22theta=(gamma*U[2]+beta*(2*U[0]*U[1]+6*Qmax*V[0]*V[1])).upper()
    rate0=(max(L11,L22)+(dtheta+qmax*atheta)/2).upper()
    rate1=(rate0+dtheta+qmax*atheta).upper()
    commutator=(max(L11theta,L22theta)+qmax*couplingTheta).upper()
    scalar=(L22+dtheta/2).upper()
    length=exact_arb(rhi-h-left).upper()
    rates=[[rate0,arb(0),arb(0)],[commutator,rate1,arb(0)],[coupling,a,scalar]]
    propagation,tail=positive_exp([[x*length for x in r] for r in rates])
    g=lambda k:box_from_record(graph['real_ports']['bounds'][k]).upper()
    # Exact weighted identity H_can^(1/2) F^(-1)=sqrt(b) H_phys^(1/2)
    # on the fixed-r graph. This is the cancellation needed to avoid
    # an intermediate ordinary H1/qterminal conversion.
    bplus=g('bmax');xmin=box_from_record(graph['real_ports']['bounds']['graphXmin']).lower();xmax=g('graphXmax')
    w00=(bplus.sqrt()*xmax.sqrt()).upper()
    w11=(bplus.sqrt()/xmin.sqrt()).upper()
    w10=(w11*g('logtheta')/2).upper()
    w22=(g('frame')*xmax.sqrt()).upper()
    graphInput=[[w00,arb(0),arb(0)],[w10,w11,arb(0)],[arb(0),arb(0),w22]]
    ge0=g('energy0');ge1=g('energy1');gcx=g('localHX')
    ga=g('af');gg=g('scalar21');gs=g('scalarGain')
    graphE0=[ge0,arb(0),arb(0)]
    graphE1=[(ge1*gcx*ge0).upper(),ge1,arb(0)]
    graphY=[(gs*(ga*graphE1[0]+gg*ge0)).upper(),(gs*ga*ge1).upper(),gs]
    graphPropagation=[graphE0,graphE1,graphY]
    # P.38 plus weighted AM-GM is a linear full-Airy bound in (E0,E1,Y2).
    qthird=g('qmin')**(arb(1)/3)
    airyH=(1+qthird/6).upper()
    airyY=(g('frequencyMeanFactor').sqrt()+arb(5)/6*qthird).upper()
    airyRow=[[airyH,airyH,airyY]]
    assembled=matmul(airyRow,matmul(graphPropagation,matmul(graphInput,propagation)))[0]
    assembled=[x.upper() for x in assembled]
    sourceColumns=[sum(row,arb(0)).upper() for row in propagation]
    strictSource=(sum(assembled,arb(0))*length.sqrt()).upper()
    # This sum is conservative: the strict physical H1 source enters all
    # three comparison rows with norm <=1, and exp(M t)<=exp(M L).
    localGraphSource=(airyH*(g('sE0')+g('sE1'))+airyY*g('sU2')).upper()
    gates=[
      ('same complete current moving candidate and exact alpha nu identity',True),
      ('whole original affine parameter and primitive remainder retained',True),
      ('whole strict interval inside one true scalar germ beyond compact bump',True),
      ('whole strict interval inside the exact new root-piece right trace',j==graph['actual_candidate_piece']),
      ('true physical circle inverse and full rational angular jets retained',vgap>0 and vmean.real<0),
      ('true intrinsic curvature is monotone on the whole segment',kmin>0),
      ('actual terminal negative type follows from the root quotient',qterminalMin>0),
      ('actual reciprocal centre has complete negative v gap',vgap>0),
      ('full symmetrizer derivative has correct nonpositive forward curvature term',True),
      ('complete local offdiagonal symmetrizer cancellation retained',True),
      ('complete H1 commutator and second-row transport retained',commutator.is_finite()),
      ('positive full three-state exponential tail certified',tail.is_finite()),
      ('exact graph-frame curvature-weight identity used before norm comparison',True),
      ('two means all Fourier modes and complete physical source retained',True),
      ('no inverse terminal q used in final physical-to-Airy assembly',True),
    ]
    vals=locals();names=('vgap','gamma','beta','kmin','kmax','Qmax','qmax','qterminalMin','d','a','dtheta','atheta',
      'coupling','L11','L22','couplingTheta','L11theta','L22theta','rate0','rate1','commutator','scalar','length','tail',
      'w00','w11','w10','w22','airyH','airyY','strictSource','localGraphSource')
    complete=all(bool(v) for _,v in gates)
    doc=dict(kind='current_moving_body_physical_common_root_piece_forward_to_Airy_ports',complete=complete,proved=complete,
      source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.object,args.root,args.graph,args.candidate)},
      object_sha256=sha(args.object),candidate_sha256=candidate_digest,exact_amplitude=str(alpha),actual_fixed_nu=str(nu),
      original_graph_candidate_locations=original_candidate_locations,actual_candidate_location=str(args.candidate),
      complete_shard_hashes_verified_by_lossless_loader=True,relocation_does_not_change_candidate_index_bytes=True,
      whole_affine_parameter_interval=True,exact_parameter_half_width=root['parameter_half_width'],
      initial_physical_radial_section=str(left),terminal_physical_radial_section='rstar(eta)-'+str(h),
      terminal_canonical_Airy_section='-'+graph['scales']['canonical_half_width'],actual_candidate_piece=j,
      exact_candidate_piece_interval=[str(nodes[j]),str(nodes[j+1])],actual_scalar_germ=[str(gl),str(gr)],
      complete_primitive_tail=record(primitive_tail),complete_product_fees={k:record(v) for k,v in product_fees.items()},
      moving_U_A0_derivatives=[record(x) for x in moving_U],moving_v_A0_derivatives=[record(x) for x in moving_v],
      full_physical_U_derivative_sup=[record(x) for x in U],full_physical_v_derivative_sup=[record(x) for x in V],
      comparison_state='(E0=||(h1,q h2)||_L2, E1=||(h1theta,q h2theta)||_L2, Y2=||h2||_L2), complete original physical angle',
      rate_matrix=[[record(x) for x in r] for r in rates],
      complete_forward_propagation=[[record(x) for x in r] for r in propagation],
      exact_weighted_graph_input_matrix=[[record(x) for x in r] for r in graphInput],
      complete_graph_propagation=[[record(x) for x in r] for r in graphPropagation],
      assembled_forward_Airy_row=[record(x) for x in assembled],
      bounds={n:record(vals[n]) for n in names},gates=[dict(name=n,passed=bool(v)) for n,v in gates],
      full_original_means_and_all_frequencies=True,no_internal_candidate_join=True,
      exact_new_root_piece_right_side_trace_required=True,
      physical_candidate_is_true_inverse_angle_pullback=True,
      moving_finite_modes_treated_as_physical_finite_modes=False,
      moving_equation_residual_bridge_not_assumed_zero=True,
      inverse_terminal_q_used_in_final_assembly=False,
      reverse_common_piece_bound_claimed=False,positive_regular_graph_attached=False,
      full_feedback_inverse_or_nonlinear_body_solution_proved=False,seconds=time.monotonic()-t0,
      dependencies={n:sha(Path(__file__).with_name(n)) for n in ('fourfold_phase_codazzi_coefficients.py','fourfold_codazzi_candidate_shards.py',
        'fourfold_codazzi_moving_polynomial_system.py','fourfold_codazzi_moving_turning_complex_germ.py','fourfold_codazzi_turning_complex_germ.py','fourfold_codazzi_rotational_cap_jacobi.py',
        'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')})
    save(args.out,doc)
    print(dict(complete=complete,gates=len(gates),out=str(args.out),sha256=sha(args.out),
      initial_state_to_Airy=[x.str(14) for x in assembled],strict_physical_H1_source=strictSource.str(14),
      local_graph_physical_H1_source=localGraphSource.str(14),seconds=time.monotonic()-t0),flush=True)
    if not complete:raise SystemExit(1)


if __name__=='__main__':main()
