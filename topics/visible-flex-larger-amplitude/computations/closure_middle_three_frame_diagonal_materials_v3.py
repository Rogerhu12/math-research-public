#!/usr/bin/env python3
"""Prepared three-frame diagonal refinement of the actual R104 material kernels.

New v3: preserve both v2 candidates and add the exact constant candidate
b_phase=max(1,sqrt(L/S)). This minimizes only the same full-segment triangle
phase. For a pure second-component source, the balanced input 1/b combines
with the physical output 1+b into 1+1/b, so the older log(b) homogeneous
surrogate does not by itself optimize the forced kernel. Every candidate
is recomputed on all actual source leaves with the signed coefficient
boxes. No numerical gain or nonlinear solution is claimed before execution.

No new ODE or radius/source integration: consume the same 10793 source leaves
and positive R68 frames, recompute a rigorous physical Euclidean log norm on
each original leaf, and integrate its scalar comparison exactly. Output is
PHYSICAL strong norm (no target V divisor). This entry has not run yet.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import re
import resource
import sys
import time

def digest(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for z in iter(lambda:f.read(1<<20),b''):h.update(z)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('computations','blocks','blocks-resource','frame','out-prefix'):
        ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--frame-sha256',required=True)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--rss-kib',type=int,default=98304)
    args=ap.parse_args()
    if args.precision<256:raise ValueError('Keep original interval precision')
    for suf in ('.json','-failure.json'):
        if Path(str(args.out_prefix)+suf).exists():raise FileExistsError('Fresh output only')
    sys.path.insert(0,str(args.computations))
    from flint import arb,ctx
    from closure_outer_whole_field_profiles import derivative_density
    from closure_taylor_cut_slope_v2 import ball,record
    from closure_outer_physical_green_geometry_recovered_v2 import upper,point
    from closure_real_head_source_enclosure import exact_q,power2
    from closure_split_joint_io_v2 import iter_array
    ctx.prec=args.precision;ctx.threads=1
    began=time.monotonic()
    initial_source_sha256='7e5b9a38af269bee7803fb8e6c002a6ca9987267b0c01b3cbe7da2d2b82a2ba8'
    if digest(args.blocks)!='62156ade93e31729c7500e79dbc01c3f4267d1a89a2b7730af7fe1c6440df45a':
        raise ValueError('The completed original R104 physical material tensor changed')
    old=json.loads(args.blocks.read_text())
    resource_doc=json.loads(args.blocks_resource.read_text())
    if (resource_doc['exitcode']!=0 or resource_doc['termination_signal'] is not None
        or not old['all_enclosure_gates'] or not all(old['enclosure_gates'].values())
        or old['declared_modes']!=[94,96]
        or len(old['causal_block_rows'])!=18
        or old['config']['entrypoint_sha256']!='3bbbecae0b3df6927b157d56d0d11add096a6fe979e0d222339383a90d31f2b2'
        or not old['all_source_origins_signed_until_output']):
        raise ValueError('The complete actual source-origin object is required')
    for name,wanted in old['config']['source_hashes'].items():
        if digest(args.computations/name)!=wanted:raise ValueError('Frozen dependency changed: '+name)
    if digest(args.frame)!=args.frame_sha256:raise ValueError('Declared complete R68 frame packet changed')
    frames=json.loads(args.frame.read_text())
    if (frames['cells']!=[11,10] or frames['panels']!=10793
        or not all(frames['gates'].values())
        or frames['source_sha256'].get('root_outer_optimal_frame_budget.py')!='ef41df6103a8c8b9cabc4ac8f2be133a244d5e0361e7d861ff7266426498e63b'):
        raise ValueError('Require the complete frozen R68 positive-frame selection')
    ids={str(args.blocks):digest(args.blocks),str(args.blocks_resource):digest(args.blocks_resource),
         str(args.frame):args.frame_sha256}
    groups={}
    for path,wanted in old['config']['input_hashes'].items():
        if path.endswith('-summary.json') and 'outer-source-cell' in path:
            if digest(path)!=wanted:raise ValueError('Original source summary changed')
            d=json.loads(Path(path).read_text())
            if not d['all_gates'] or not all(d['gates'].values()):raise ValueError('True source is incomplete')
            ids[path]=wanted
            for g in d['groups']:groups[d['cell'],g['segment']]=g
    order=[(n,j) for n in (11,10) for j in range(9)]
    if set(groups)!=set(order):raise ValueError('All original 18 source segments required')
    frame_groups={}
    for f in frames['files']:
        match=re.search(r'-cell(\d{3})-seg([0-8])-panels\.jsonl\.gz$',f['path'])
        if match:frame_groups[int(match[1]),int(match[2])]=f
    if set(frame_groups)!=set(order):raise ValueError('All original 18 positive frame streams required')
    modes=[94,96];powers=[2,1,0];done=[];total=0;maximum_exponent=arb(0)
    strategies=['original_R68_leaf_frames','one_constant_segment_frame','one_constant_phase_frame']
    def guard():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>args.rss_kib:
            raise MemoryError('Owned observed RSS above the declared stop threshold')
    def up(x):
        if not x.is_finite() or x<0:raise ArithmeticError('Nonnegative finite bound required')
        return upper(x.upper(),96)
    def exact_point(x):
        if not x.is_finite():raise ArithmeticError('Finite exact point required')
        mantissa,exponent=x.man_exp()
        return [str(mantissa),int(exponent)]
    def exprel_up(z):
        fallback=(z if z>0 else arb(0)).exp().upper()
        if z==0:return arb(1)
        val=(z.exp()-1)/z
        if val.is_finite() and val>0:return min(fallback,val.upper())
        # Positive integral definition integral_0^1 exp(z t) dt.
        return fallback
    try:
        for gi,(n,j) in enumerate(order):
            g=groups[n,j];fg=frame_groups[n,j]
            if digest(g['path'])!=g['sha256'] or digest(fg['path'])!=fg['sha256']:
                raise ValueError('A complete actual leaf/frame stream changed')
            ids[g['path']]=g['sha256'];ids[fg['path']]=fg['sha256']
            # First pass defines one exact positive constant from the same
            # complete source segment. No derivative of this b is omitted.
            S=arb(0);L=arb(0);candidate_count=0
            for row in iter_array(Path(g['path']),'panels'):
                dx=exact_q(Fraction(row['x_right'])-Fraction(row['x_left']))
                rr=ball(row['radius']);rx0=ball(row['radius_x'])
                ell0=ball(row['log_w_x'])
                if not rr>0 or not rx0>0 or not dx>0:
                    raise ArithmeticError('The constant-frame source domain failed')
                S=(S+(rx0/rr).upper()*dx).upper()
                L=(L+abs(ell0).upper()*dx).upper()
                candidate_count+=1
                if candidate_count%64==0:guard()
            if candidate_count!=g['panels'] or not S>0:
                raise ValueError('Incomplete constant-frame source surrogate')
            constant_frames=[];phase_frames=[]
            for m in modes:
                # The surrogate derivative in t=log b is
                # 1+(m/2)(S exp(t)-L exp(-t)).
                # Stable positive formula for its b>=1 minimum.
                raw=(m*L/(1+(1+m*m*S*L).sqrt())).upper()
                constant_frames.append(max(arb(1),raw))
                # A second exact choice, not a claim about the optimal forced
                # integral. Its source and whole-leaf costs are paid below.
                phase_frames.append(max(arb(1),(L/S).sqrt().upper()))
            states=[[[arb(0) for p in powers] for m in modes] for z in strategies]
            ps=[[[arb(0) for p in powers] for m in modes] for z in strategies]
            ks=[[[arb(0) for p in powers] for m in modes] for z in strategies]
            previous_b=[[None for m in modes] for z in strategies]
            last_b=[[None for m in modes] for z in strategies]
            previous_right=Fraction(0);count=0
            with gzip.open(fg['path'],'rt') as ff:
                frame_it=(json.loads(line) for line in ff if line.strip())
                for row in iter_array(Path(g['path']),'panels'):
                    fr=next(frame_it)
                    if (row['panel']!=count or row['segment']!=j or fr['index']!=count
                        or Fraction(fr['x_left'])!=Fraction(row['x_left'])
                        or Fraction(fr['x_right'])!=Fraction(row['x_right'])):
                        raise ValueError('Source/frame panel correspondence failed')
                    left,right=Fraction(row['x_left']),Fraction(row['x_right'])
                    if left!=previous_right or not left<right<=1:raise ValueError('Complete source ordering failed')
                    previous_right=right
                    V,_,_,_=derivative_density(row,arb(17)/16,arb(1)/16,92)
                    if not V>0 or not V<=power2(-40):raise ArithmeticError('Same exact V domain failed')
                    r,rx,w,ell=(ball(row[k]) for k in ('radius','radius_x','w','log_w_x'))
                    if not r>0 or not rx>0 or not w>0 or not w.upper()<=arb(1)/2:
                        raise ArithmeticError('The true complete background domain failed')
                    s=rx/r
                    # Use one exact positive dyadic frame; recompute its actual
                    # coefficient norm instead of importing any old phase value.
                    original_b=ball(fr['chosen_frame']).upper()
                    if not original_b>0:raise ArithmeticError('A strictly positive fixed frame is required')
                    dx=exact_q(right-left)
                    c=(s.upper()+abs(ell).upper()).upper()
                    nonphase=max((-s-ell).upper(),(-2*ell).upper())
                    vp=[V*V,V,arb(1)]
                    for si,strategy in enumerate(strategies):
                        for mi,m in enumerate(modes):
                            b=(original_b if si==0 else
                               constant_frames[mi] if si==1 else phase_frames[mi])
                            pb=previous_b[si][mi]
                            jump=arb(1) if pb is None else max(arb(1),(pb/b).upper())
                            if si>0 and not jump==1:
                                raise ArithmeticError('A declared constant frame changed')
                            phase=(abs(s*b+ell/b)/2).upper()
                            z=((nonphase+m*phase)*dx).upper()
                            maximum_exponent=max(maximum_exponent,abs(z).upper())
                            growth=z.exp().upper();psi=exprel_up(z)
                            for pi,power in enumerate(powers):
                                q0=(states[si][mi][pi]*jump).upper()
                                d=(c*vp[pi]/b).upper()
                                qend=(growth*q0+d*dx*psi).upper()
                                # The scalar solution may increase or decrease;
                                # its whole-leaf maximum is at an endpoint.
                                qwhole=max(q0,qend)
                                ps[si][mi][pi]=max(ps[si][mi][pi],qwhole)
                                ks[si][mi][pi]=max(ks[si][mi][pi],(b*qwhole).upper())
                                states[si][mi][pi]=qend
                            previous_b[si][mi]=last_b[si][mi]=b
                    count+=1;total+=1
                    if count%64==0:guard()
                if next(frame_it,None) is not None:raise ValueError('Unused frame rows')
            if previous_right!=1 or count!=g['panels'] or count!=fg['panels']:
                raise ValueError('The complete diagonal source segment is unpaid')
            oldrow=old['causal_block_rows'][gi]
            if (oldrow['target_cell'],oldrow['target_segment'])!=(n,j):
                raise ValueError('Old target order differs')
            outm=[]
            for mi,m in enumerate(modes):
                om=oldrow['modes'][mi]
                if om['mode']!=m:raise ValueError('Old mode order differs')
                os=om['source_rows'][-1]
                if (os['source_cell'],os['source_segment'])!=(n,j):raise ValueError('Old diagonal source differs')
                vals=[]
                for pi,power in enumerate(powers):
                    od=os['density_rows'][pi]
                    if od['V_power']!=power:raise ValueError('Old density order differs')
                    candidates=[]
                    minP=point(od['P_sup']);minK=point(od['K_sup'])
                    for si,strategy in enumerate(strategies):
                        P=((1+m)*ps[si][mi][pi]).upper()
                        K=((1+m)*ks[si][mi][pi]).upper()
                        minP=min(minP,P);minK=min(minK,K)
                        candidates.append({'strategy':strategy,
                            'scalar_P_sup':up(P),'scalar_K_sup':up(K),
                            'scalar_physical_strong_row':up(P+K),
                            'endpoint_balanced_forcing_norm':up(states[si][mi][pi]),
                            'endpoint_P_bound':up(states[si][mi][pi]),
                            'endpoint_K_bound':up(last_b[si][mi]*states[si][mi][pi]),
                            'last_frame_exact':exact_point(last_b[si][mi])})
                    vals.append({'V_power':power,'candidates':candidates,
                        'old_R104_physical_strong_row':od['physical_strong_output_row'],
                        'combined_P_sup':up(minP),'combined_K_sup':up(minK),
                        'combined_min_component_row':up(minP+minK)})
                outm.append({'mode':m,'chosen_constant_frame_exact':exact_point(constant_frames[mi]),
                    'chosen_constant_phase_frame_exact':exact_point(phase_frames[mi]),'density_rows':vals})
            result={'cell':n,'segment':j,'panels':count,
                'positive_surrogate_S_upper':up(S),'nonnegative_surrogate_L_upper':up(L),
                'modes':outm}
            done.append(result)
            target=Path(str(args.out_prefix)+f'-completed-cell{n:03d}-segment{j}.json')
            if target.exists():raise FileExistsError('Do not overwrite a completed diagonal group')
            target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(result,separators=(',',':'))+'\n')
            print(json.dumps({'event':'complete_true_frame_diagonal','cell':n,'segment':j,
                'panels':count,'elapsed_seconds':time.monotonic()-began}),flush=True);guard()
        gates={'all18_actual_groups':len(done)==18,'all10793_original_source_leaves':total==10793,
            'same_original_V_and_true_background':True,'each_positive_frame_fixed_and_actual_coefficients_rebounded':True,
            'every_interface_frame_cost_paid':True,'whole_leaf_scalar_monotonicity_used':True,
            'two_components_separate_sup_and_one_plus_m_retained':True,
            'physical_output_no_target_V_divisor':True,'all_three_original_material_powers':True,
            'old_complete_true_initial_inputs_not_modified':True,
            'independent_constant_source_segment_frame_rebounded':True,
            'independent_constant_phase_frame_rebounded':True,
            'all_original_R104_offdiagonal_rows_retained':True}
        out={'schema':'visible-flex-R104-three-frame-diagonal-material-refinement-v3',
            'author':'exact_closure (GPT-6 Astra Pro; AI-assisted)',
            'status':'Actual diagonal linear kernels only; inspect later nonlinear consumption',
            'all_gates':all(gates.values()),'gates':gates,'rows':done,
            'input_hashes':ids,'entrypoint_sha256':digest(__file__),'precision':args.precision,
            'prepared_scalar_v1_retained_unchanged_sha256':initial_source_sha256,
            'prepared_scalar_v2_retained_unchanged_sha256':'3f7f4bb7bd26bbdb83b9df7a40e7fd9ca52cf0b6652f89e94978872cfb272ca7',
            'source_units':'source-x c_background V_I^p for p=2,1,0',
            'output_units':'physical strong Wiener norm with separate component radial sups',
            'maximum_abs_leaf_log_growth':up(maximum_exponent),
            'old_full_offdiagonal_and_both_initial_inputs_retained_in_R104':True,
            'whole_middle_or_joint_nonlinear_solution_claimed':False,
            'no_new_ODE_or_source_integral':True,
            'elapsed_seconds':time.monotonic()-began,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
        target=Path(str(args.out_prefix)+'.json');target.write_text(json.dumps(out,separators=(',',':'))+'\n');guard()
        print(json.dumps({'event':'all_true_frame_diagonals_complete','all_gates':out['all_gates'],
            'elapsed_seconds':out['elapsed_seconds'],'peak_rss_kib':out['peak_rss_kib']}),flush=True)
    except Exception as exc:
        target=Path(str(args.out_prefix)+'-failure.json')
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(json.dumps({'status':'Incomplete scalar consumption; no mathematical nonexistence claimed',
            'exception':repr(exc),'completed_groups':len(done),'original_panels':total,
            'source_sha256':digest(__file__)},indent=2)+'\n')
        raise
if __name__=='__main__':main()
