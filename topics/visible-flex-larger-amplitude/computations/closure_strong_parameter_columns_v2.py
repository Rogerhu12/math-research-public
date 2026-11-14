# Previous parse-only failed source SHA256 e718f7f1480323e52ade9c017a9225d3db142d678c5ef6ae0fdd36a3135f94f4; v2 adds the missing parenthesis, with no numerical rule change.
#!/usr/bin/env python3
"""Certify all641x46 nonlinear parameter columns and response-based axes.

Floating solves only propose dyadic vectors. The original positive operator
is retained with every nonzero coefficient;192-bit Arb recomputes the full
forcing and checks every super-solution inequality. A rigorous W-remainder
repairs any floating residual. No interval inverse, ODE or new Green occurs.
The new parameter-dependent boxes are centred on the EXISTING R58 real
solution, not on an unverified numerical point.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted),2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import json
import math
from pathlib import Path
import resource
import time
import numpy as np
from flint import arb, arb_mat, ctx
from closure_real_head_source_enclosure import power2,ball_record
from closure_real_head_green_enclosure import ball
from closure_split_joint_io_v2 import digest,read,iter_array,metadata_without_array,label
from closure_two_material_joint_verify import compact
from closure_balance_parameter_axes_v2 import floorlog2


def point_pair(value):
    point=value.upper()
    if not point.is_exact():raise ArithmeticError('Expected an outward dyadic point')
    m,e=point.man_exp();return [int(m),int(e)]


def fraction_point(value):
    m,e=point_pair(value)
    return Fraction(m*(1<<e)) if e>=0 else Fraction(m,1<<(-e))


def rss_guard(cap):
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > cap*1024:
        raise MemoryError('The owned positive-column job exceeded its explicit RSS cap')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('matrix','domain','lifts','joint','density','out','summary'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--rss-limit-mib',type=int,default=120)
    p.add_argument('--refinements',type=int,default=4)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    if args.out.exists() or args.summary.exists() or args.out.suffix!='.gz':
        raise FileExistsError('Use a fresh compressed complete-column prefix')
    paths=[getattr(args,k) for k in ('matrix','domain','lifts','joint','density')]
    hashes={str(x):digest(x) for x in paths}
    meta=metadata_without_array(args.matrix,'rows')
    domain,lifts,joint,density=map(read,[args.domain,args.lifts,args.joint,args.density])
    if not meta['all_rows_contracting'] or not domain['all_gates'] or not joint['whole_head_closed'] or not all(joint['gates'].values()):
        raise ValueError('The exact actual head/domain/positive matrix certificates must be complete')
    for path in (args.domain,args.lifts,args.joint,args.density):
        if meta['input_hashes'].get(str(path))!=hashes[str(path)]:
            raise ValueError('The stored positive operator belongs to another exact problem')
    N,dim,inf,zi,M=213,641,639,640,46
    if meta['dimension']!=dim or lifts['cells']!=list(range(12,225)) or lifts['modes']!=list(range(2,93,2)):
        raise ValueError('All original physical cells and parameter modes are required')
    W=[ball(v) for v in meta['metric_weights']]
    if len(W)!=dim or not all(v.is_exact() and v>0 for v in W):
        raise ValueError('The exact original full641 positive metric is required')
    for i,row in enumerate(domain['rows']):
        if row['index']!=i or ball(row['metric_weight'])!=W[i]:raise ValueError('The full metric coordinates changed')
    lam=ball(meta['lambda_upper']);rho=ball(meta['physical_domain']);Z=ball(meta['independent_far_z'])
    if not 0<lam<1 or rho!=power2(-30) or Z!=power2(-2200):raise ValueError('The actual uniform domains changed')
    J=arb_mat(dim,dim);Jf=np.zeros((dim,dim),dtype=np.float64)
    seen=set();nonzeros=0;float_underflow=0;maxrow=arb(0)
    for row in iter_array(args.matrix,'rows'):
        i=row['index']
        if i in seen or not 0<=i<dim or any(row[k]!=v for k,v in label(i,N).items()):raise ValueError('A complete derivative row was omitted/reordered')
        seen.add(i);cols=set();total=arb(0)
        for j,m,e in row['coefficients']:
            if j in cols or not 0<=j<dim or type(m)is not int or type(e)is not int or m<=0:raise ValueError('A positive sparse coefficient is malformed')
            cols.add(j);v=compact([m,e]);J[i,j]=v;total+=v;nonzeros+=1
            fv=float(v)
            if fv==0:float_underflow+=1
            if not math.isfinite(fv) or fv<0:raise ValueError('The diagnostic scaling is nonfinite')
            Jf[i,j]=fv
        top=total.upper()
        if not top<=ball(row['row_sum_upper']).upper() or not top<lam:
            raise ArithmeticError('A complete compact derivative row escaped its strict margin')
        maxrow=max(maxrow,top)
    if seen!=set(range(dim)) or nonzeros!=meta['stored_nonzero_coefficients']:
        raise ValueError('Every original positive matrix entry must be consumed')
    rss_guard(args.rss_limit_mib)
    units=[ball(a['canonical_Q_axis']) for a in domain['axes']]
    if len(units)!=M or not all(v.is_exact() and v>0 for v in units):raise ValueError('All46 exact prior parameter units are required')
    A=[[compact(v) for v in row] for row in lifts['A_upper']]
    E=[compact(v) for v in lifts['far_E_upper']]
    lift=arb_mat(dim,M)
    for n in range(N):
        for j in range(M):lift[n,j]=(A[n][j]*units[j]/W[n]).upper()
    C=J*lift
    for j in range(M):C[zi,j]+=E[j]*units[j]/(Z*W[zi])
    for i in range(dim):
        for j in range(M):C[i,j]=C[i,j].upper()
    del lift
    rss_guard(args.rss_limit_mib)
    Cf=np.array([[float(C[i,j]) for j in range(M)] for i in range(dim)],dtype=np.float64)
    operator=np.eye(dim)-Jf
    proposed=np.linalg.solve(operator,Cf)
    if not np.isfinite(proposed).all():raise ArithmeticError('The untrusted floating proposal is nonfinite')
    P=arb_mat(dim,M)
    negative_proposals=int(np.count_nonzero(proposed<0))
    for i in range(dim):
        for j in range(M):P[i,j]=arb(float(max(0,proposed[i,j])))
    history=[];residual=None
    for step in range(args.refinements+1):
        residual=C+J*P-P
        eps=[max([arb(0)]+[residual[i,j].upper() for i in range(dim)]) for j in range(M)]
        worst=max(eps)
        history.append(dict(step=step,maximum_positive_residual=ball_record(worst),seconds=time.monotonic()-started))
        print(json.dumps(dict(event='parameter_column_refinement',step=step,positive_residual=str(worst),seconds=time.monotonic()-started,RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        rss_guard(args.rss_limit_mib)
        if worst<power2(-140) or step==args.refinements:break
        Rf=np.array([[float(residual[i,j].mid()) for j in range(M)] for i in range(dim)],dtype=np.float64)
        update=np.linalg.solve(operator,Rf)
        if not np.isfinite(update).all():raise ArithmeticError('The untrusted floating refinement is nonfinite')
        for i in range(dim):
            for j in range(M):P[i,j]=max(arb(0),(P[i,j]+arb(float(update[i,j]))).mid())
    repair=[(2*e/(1-lam)+power2(-140)).upper() for e in eps]
    for i in range(dim):
        for j in range(M):P[i,j]=(P[i,j]+repair[j]).upper()
    bound=C+J*P
    gaps=[[ (P[i,j]-bound[i,j]).lower() for j in range(M)] for i in range(dim)]
    all_super=all(v>0 for row in gaps for v in row)
    if not all_super:
        failed=[dict(row=i,mode=2*(j+1),gap=ball_record(gaps[i][j])) for i in range(dim) for j in range(M) if not gaps[i][j]>0]
        args.summary.write_text(json.dumps(dict(status='Complete parameter-column super-solution gate failed',failed=failed,history=history,input_hashes=hashes),indent=2)+'\n')
        raise ArithmeticError('An original641x46 positive super-solution inequality remains unpaid')
    D=arb_mat(dim,M)
    for i in range(dim):
        for j in range(M):D[i,j]=(W[i]*P[i,j]).upper()
    oldr=[ball(row['radius']) for row in joint['rows']]
    baseline=[(oldr[n]+oldr[N+n]+oldr[2*N+n]+oldr[inf]).upper() for n in range(N)]
    mean=[ball(row['V_over_w_upper']).upper() for row in density['rows']]
    zaux=ball(joint['auxiliary_far_z'])
    fields=arb_mat(N,M)
    for n in range(N):
        for j in range(M):fields[n,j]=(A[n][j]*units[j]+D[n,j]+D[N+n,j]+D[2*N+n,j]+D[inf,j]).upper()
    scales=[];axes=[]
    hf=domain['Q_to_physical_H_factor'];hl=domain['Q_to_physical_H_log2_factor']
    for j in range(M):
        limits=[]
        for n in range(N):
            limits.append((((rho-baseline[n])/(4*fields[n,j])).lower(),'physical',12+n))
            limits.append(((((arb(1)/64)/mean[n]-1-baseline[n])/(4*fields[n,j])).lower(),'mean',12+n))
        limits.append((((1-zaux/Z-oldr[zi])/(4*D[zi,j])).lower(),'far',225))
        lim,kind,where=min(limits,key=lambda x:x[0])
        if not lim>=1:raise ArithmeticError('The response-based domain must retain every paid R59 axis')
        sexp=floorlog2(fraction_point(lim));scale=power2(sexp);scales.append(scale)
        unit=(units[j]*scale).upper();exp=domain['axes'][j]['canonical_Q_axis_log2']+sexp
        axes.append(dict(j=j+1,physical_mode=2*(j+1),old_canonical_Q_axis_log2=domain['axes'][j]['canonical_Q_axis_log2'],
            enlargement_bits=sexp,canonical_Q_axis_log2=exp,canonical_Q_axis=ball_record(unit),
            limiting_domain=dict(kind=kind,cell=where),physical_H_axis=ball_record(ball(hf)*unit),
            guaranteed_physical_H_axis_log2=exp-18,physical_H_axis_log2=ball_record(ball(hl)+exp),
            original_unit_nonlinear_cut_low=ball_record(D[0,j]),
            original_unit_nonlinear_cut_near=ball_record(D[N,j]),
            original_unit_nonlinear_cut_rest=ball_record(D[2*N,j]),
            original_unit_nonlinear_cut_infinite=ball_record(D[inf,j]),
            enlarged_unit_nonlinear_cut_low=ball_record((scale*D[0,j]).upper()),
            enlarged_unit_nonlinear_cut_high=ball_record((scale*(D[N,j]+D[2*N,j]+D[inf,j])).upper()),
            enlarged_unit_complete_cut_field=ball_record((scale*fields[0,j]).upper())))
    combined=[(baseline[n]+max((scales[j]*fields[n,j]).upper() for j in range(M))).upper() for n in range(N)]
    far=(zaux/Z+oldr[zi]+max((scales[j]*D[zi,j]).upper() for j in range(M))).upper()
    gates=dict(all641_original_positive_rows_retained=seen==set(range(dim)),
        all275413_nonzero_coefficients_retained=nonzeros==meta['stored_nonzero_coefficients'],
        all641_uniform_row_sums_below_lambda=maxrow<lam<1,
        complete_actual_parameter_forcing_including_far=True,
        all641x46_positive_super_solutions=all_super,
        all46_previous_axes_contained=all(s>=1 for s in scales),
        all213_combined_physical_domains=all(v<rho for v in combined),
        all213_complete_mean_domains=all(mean[n]*(1+combined[n])<arb(1)/64 for n in range(N)),
        complete_true_R18_far_domain=far<1)
    if not all(gates.values()):raise ArithmeticError('A complete response-based parameter-domain gate failed')
    summary=dict(status='All641x46 nonlinear derivative super-solutions and enlarged actual46-parameter domain proved',
        all_gates=True,gates=gates,original_dimension=dim,parameter_modes=list(range(2,93,2)),
        supersolution_inequalities=dim*M,positive_matrix_nonzeros=nonzeros,
        metric_normalization='P_ij is the unknown correction derivative in units W_i per original R59 axis v_j. The direct linear lift is excluded from P and added separately in every field/domain bound.',
        direct_low_height_identity=True,nonlinear_low_height_correction_identically_zero=True,
        new_box_centre='The existing exact R58 full-frequency solution x0, not the floating finite-depth trajectory or auxiliary low centre.',
        new_box_formula='For fixed a, |x_i(a)-x0_i| <= sum_j W_i P_ij |a_j|/v_j_old. Its positive invariance follows columnwise from Jbar P+C<P; no max-of-columns box is substituted.',
        expanded_parameter_norm='sum_j |delta Q_(2j)(b)|/v_j_new <=1; all46 new axes are listed.',
        maximum_combined_total_radius=ball_record(max(combined)),
        complete_far_normalized_domain_upper=ball_record(far),
        maximum_compact_J_row=ball_record(maxrow),lambda_upper=ball_record(lam),
        refinements=history,uniform_positive_repairs=[ball_record(v) for v in repair],
        floating_negatives_clamped_in_proposal=negative_proposals,
        floating_underflow_entries_in_proposal_only=float_underflow,
        every_such_entry_retained_in_strict_Arb=True,
        exact_arithmetic_semantics='Every final P entry and source C endpoint is an outward exact dyadic. Every641x46 inequality is recomputed using the complete192-bit Arb matrix product. Floating solves and their refinements only propose values.',
        axes=axes,physical_domain=meta['physical_domain'],independent_far_z=meta['independent_far_z'],
        true_cut_radius=domain['true_cut_radius'],Q_to_physical_H_factor=hf,
        input_hashes=hashes,source_sha256=digest(Path(__file__)),
        helper_hashes={name:digest(Path(__file__).with_name(name)) for name in ('closure_split_joint_io_v2.py','closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py','closure_two_material_joint_verify.py')},
        no_new_kernel_or_radial_integration=True,no_interval_matrix_inverse=True,
        exact_outer_Schur_inverse_paid=False,outer0_to11_solution_paid=False,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload=dict(summary,
        original_axis_units=[ball_record(v) for v in units],metric_weights=meta['metric_weights'],
        rows=[dict(index=i,**label(i,N),scaled_derivative_upper=[point_pair(P[i,j]) for j in range(M)],
                   forcing_upper=[point_pair(C[i,j]) for j in range(M)],
                   minimum_strict_supersolution_gap=ball_record(min(gaps[i]))) for i in range(dim)],
        cells=[dict(cell=12+n,baseline_true_head_radius=ball_record(baseline[n]),
                    enlarged_parameter_total=ball_record(combined[n]),
                    original_unit_complete_field_upper=[point_pair(fields[n,j]) for j in range(M)]) for n in range(N)])
    raw=gzip.compress((json.dumps(payload,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(raw)>=5_000_000:raise ArithmeticError('The complete positive-column ledger exceeds the repository cap')
    args.out.write_bytes(raw);summary.update(output=str(args.out),output_sha256=digest(args.out),bytes=len(raw))
    args.summary.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',all_gates=True,gates=gates,first_Q_axis_log2=axes[0]['canonical_Q_axis_log2'],last_Q_axis_log2=axes[-1]['canonical_Q_axis_log2'],min_enlargement_bits=min(a['enlargement_bits'] for a in axes),max_enlargement_bits=max(a['enlargement_bits'] for a in axes),seconds=summary['elapsed_seconds'],RSS_KiB=summary['peak_RSS_KiB'],sha256=summary['output_sha256'],bytes=len(raw))),flush=True)


if __name__=='__main__':main()
