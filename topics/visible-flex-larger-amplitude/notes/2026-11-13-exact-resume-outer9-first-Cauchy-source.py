#!/usr/bin/env python3
"""Same original cell9: complete frame ledger and a full-frequency first-piece Cauchy extension.

No ODE or quadrature is performed. Original elementary coefficient enclosures
and the R142 complete node10 trace are consumed without altering the metric.
The first-piece theorem retains every even Fourier mode and the full mean root.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE/'outer-continuation-inputs'/'sources'))
from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball
from closure_split_joint_io import iter_array

WRAPPER = 'bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59'
READY = '563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6'
RADIUS = '28d491b998174029a80daf41e9365de6ab2c54757419de7b64f54445047b717f'
MATERIAL = '78dc58b9c8173e1ba5d4dafc8fc8225ab5c987411b100b99f15ea476929ae82e'
BRIDGE = 'b26c36452bc651f8d1ce55f9da23b6c904ad209878c268787a38cdce45612ae5'
GATES = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    data = Path(p).read_bytes()
    return json.loads(gzip.decompress(data) if str(p).endswith('.gz') else data)


def q(v):
    if isinstance(v, list):
        return F(int(v[0]))*F(2)**int(v[1])
    if isinstance(v, dict) and 'mantissa' in v:
        return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(v)


def gate(k, v):
    if k in GATES:
        raise ValueError('Repeated gate '+k)
    GATES[k] = bool(v)
    if not v:
        raise ArithmeticError('Unpaid gate '+k)


def finite(*values):
    return all(v.is_finite() for v in values)


def upper(x):
    if not x.is_finite():
        raise ArithmeticError('Nonfinite interval upper bound')
    return x.upper()


def poslog(x):
    if not x > 0:
        raise ArithmeticError('Nonpositive frame ratio')
    return max(arb(0), upper(x.log()))


def resource_ok(doc, name):
    gate(name+'_actual_exit0', doc['exitcode'] == 0 and doc['termination_signal'] is None)
    gate(name+'_actual_wait4', doc['resource_wrapper_sha256'] == WRAPPER)


def rec(x):
    if not x.is_finite():
        raise ArithmeticError('Nonfinite output')
    return ball_record(x)


def main():
    started = time.monotonic()
    ctx.prec = 256
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--material', required=True)
    p.add_argument('--material-resource', required=True)
    p.add_argument('--bridge', required=True)
    p.add_argument('--bridge-resource', required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    out = Path(args.out)
    if out.exists():
        raise FileExistsError('Fresh complete output required')
    m, bridge = read(args.material), read(args.bridge)
    gate('same_material_primary', sha(args.material) == MATERIAL)
    gate('same_R142_complete_trace', sha(args.bridge) == BRIDGE)
    resource_ok(read(args.material_resource), 'material')
    resource_ok(read(args.bridge_resource), 'R142')
    gate('all_original_material_gates', all(m['checks'].values()))
    gate('all_R142_gates', bridge['all_gates'] and all(bridge['gates'].values()))
    gate('same_original_ready_and_radius', set(m['original_metadata']['input_hashes'].values()) == {READY, RADIUS})
    gate('no_new_material_ODE_or_quadrature', m['original_metadata']['new_ODE_or_binary_quadrature'] == 0)
    gate('all_nine_segments', m['cell'] == 9 and [x['source_segment'] for x in m['groups']] == list(range(9)))
    port = next(z for z in bridge['true_cauchy_ports'] if z['node'] == 10)
    Rin = exact_q(q(port['complete_field']['nonmean_strong_radius']))
    sigma0, kappa, minimum = exact_q(F(1,64)), arb(1), exact_q(F(1,256))
    gates_by_segment, rows = [], []
    total_phase, total_dforward, total_dbackward, total_cbg = [arb(0) for _ in range(4)]
    prev, first, count, extension = None, None, 0, None
    inputs = {k:{'path':str(v),'sha256':sha(v)} for k,v in vars(args).items() if k!='out'}
    for g in m['groups']:
        segment = g['source_segment']
        gp = Path(g['path'])
        gate(f'segment{segment}_actual_sha', sha(gp) == g['sha256'])
        phase, forward, backward, cbgsum = [arb(0) for _ in range(4)]
        start, n, valid = F(0), 0, True
        first_b, end_b = None, None
        for row in iter_array(gp, 'panels'):
            left, right = F(row['x_left']), F(row['x_right'])
            if left != start or not left < right or row['segment'] != segment:
                raise ArithmeticError('Incomplete original panel coverage')
            start = right
            dx = exact_q(right-left)
            r, rx, ell, w = [ball(row[k]) for k in ('radius','radius_x','log_w_x','w')]
            if not finite(r,rx,ell,w) or not (r > 0 and rx > 0 and w > 0 and w.upper() <= arb(1)/2):
                raise ArithmeticError('Unpaid complete background branch')
            s = rx/r
            sl,su,el,eu = s.lower(),s.upper(),ell.lower(),ell.upper()
            square = max(minimum*minimum, upper(eu/su), upper(-(el+eu)/(sl+su)))
            b = upper(square.sqrt())
            gamma = upper(abs(s*b+ell/b)/2)
            cbar = upper(s+abs(ell))
            dplus = upper(max((-s-ell).upper(), (-2*ell).upper()))
            dminus = upper(max((s+ell).upper(), (2*ell).upper()))
            if not finite(s,b,gamma,cbar,dplus,dminus) or not (b>=minimum and cbar>0 and gamma>=0):
                raise ArithmeticError('Nonfinite or nonpositive comparison coefficient')
            fi,bi = upper(dplus*dx),upper(dminus*dx)
            if prev is not None:
                fi = upper(fi+poslog(prev/b))
                bi = upper(bi+poslog(b/prev))
            if first is None:
                first=b
            if first_b is None:
                first_b=b
            prev,end_b=b,b
            phase=upper(phase+gamma*dx)
            forward=upper(forward+fi)
            backward=upper(backward+bi)
            cbgsum=upper(cbgsum+cbar*dx)
            count,n=count+1,n+1
            if segment==0:
                gate('first_piece_single_complete_panel', g['panels']==1 and left==0 and right==1)
                # The same node10 is identified by the original radius ledger,
                # while interval overlap is explicitly checked as a sanity gate.
                a0,a1=q(row['radius_left']['lower']),q(row['radius_left']['upper'])
                b0,b1=q(port['background_radius']['lower']),q(port['background_radius']['upper'])
                gate('same_node10_radius_intersection', max(a0,b0)<=min(a1,b1))
                w0,w1=q(row['w']['lower']),q(row['w']['upper'])
                v0,v1=q(port['background_w']['lower']),q(port['background_w']['upper'])
                gate('same_node10_w_intersection', max(w0,v0)<=min(w1,v1))
                D=upper(max(arb(0),dplus)*dx)
                eD=upper(D.exp())
                Bin,Bout=max(arb(1),upper(1/b)),max(arb(1),b)
                H=upper(2*Bin*Bout*eD)
                G=upper(3*Bout*eD/(kappa*b))
                Rout=upper(2*H*Rin)
                sigma_end=sigma0-(gamma+kappa*cbar)*dx
                image=upper(H*Rin+arb(3)*G*Rout**2/2)
                lip=upper(4*G*Rout)
                gate('first_piece_finite_complete_budget',finite(D,eD,H,G,Rout,sigma_end,image,lip))
                gate('first_piece_terminal_width_above_1over128',sigma_end.lower()>exact_q(F(1,128)))
                gate('first_piece_whole_ball_inside_complete_mean_domain',Rout<exact_q(F(1,64)))
                gate('first_piece_strict_full_frequency_selfmap',image<Rout)
                gate('first_piece_complete_derivative_below_one_half',lip<arb(1)/2)
                extension=dict(source_segment=0,complete_panel_interval=['0','1'],
                    physical_radius_left=row['radius_left'],physical_radius_right=row['radius_right'],
                    fixed_frame=rec(b),s=rec(s),ell=rec(ell),cbg_majorant=rec(cbar),
                    Hermitian_mode_slope=rec(gamma),nonnegative_diagonal_integral=rec(D),
                    source_strip='1/64',target_strip='1/128',kappa='1',
                    terminal_moving_strip_lower=rec(sigma_end.lower()),
                    input_complete_physical_strong_radius=rec(Rin),
                    homogeneous_radial_first_physical_gain=rec(H),
                    complete_weak_source_to_radial_first_strong_gain=rec(G),
                    chosen_complete_physical_ball=rec(Rout),complete_selfmap_upper=rec(image),
                    complete_derivative_upper=rec(lip),
                    physical_width=row['width'],
                    even_frequencies='all signed nonzero even modes, no upper cutoff',
                    nonlinear_source='R98 full quotient and full mean root; source/cbg <= 3R^2/2, derivative <= 4R',
                    source_radial_order='fixed per-mode radial sup before angular convolution',
                    complete_mean_restored_by_R142_identity=True,
                    complete_height_and_embedded_annulus_extension=True)
            if count%128==0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>96*1024:
                raise MemoryError('Original 96 MiB resource guard')
        gate(f'segment{segment}_complete_coverage',start==1 and n==g['panels'])
        total_phase=upper(total_phase+phase)
        total_dforward=upper(total_dforward+forward)
        total_dbackward=upper(total_dbackward+backward)
        total_cbg=upper(total_cbg+cbgsum)
        rowout=dict(segment=segment,panels=n,phase_upper=rec(phase),cbg_integral_upper=rec(cbgsum),
            forward_with_initial_jump=rec(forward),backward_with_initial_jump=rec(backward),
            first_frame=rec(first_b),last_frame=rec(end_b),
            cumulative_phase_upper=rec(total_phase),
            cumulative_physical_forward_log_prefactor_upper=rec(upper(total_dforward+poslog(1/first)+poslog(prev))),
            cumulative_physical_backward_log_prefactor_upper=rec(upper(total_dbackward+poslog(1/prev)+poslog(first))))
        rows.append(rowout)
        print(json.dumps({'segment':segment,'panels':n,'phase_upper':str(phase),'cumulative_phase_upper':str(total_phase)}),flush=True)
    gate('all4985_original_panels_consumed',count==m['panels']==4985)
    gate('whole_cell_homogeneous_prefactors_and_jumps_paid',first is not None and prev is not None)
    gate('first_piece_actual_complete_extension',extension is not None)
    result=dict(schema='original-outer9-frame-and-first-piece-full-Cauchy-v1',source_sha256=sha(__file__),
        inputs=inputs,original_ready_sha256=READY,original_radius_sha256=RADIUS,
        original_cell9_panels=count,frame_ledger=rows,complete_cell9_phase_upper=rec(total_phase),
        complete_cell9_cbg_upper=rec(total_cbg),
        available_input_analytic_strip='1/64',
        sufficient_cell9_homogeneous_only_to_1over128=bool(total_phase<exact_q(F(1,128))),
        first_piece_full_Cauchy_extension=extension,
        whole_cell9_nonlinear_continuation_claimed=False,outer0to8_continuation_claimed=False,
        complete_mean_inverse_and_infinite_even_tail_retained=True,
        new_ODE_or_quadrature=0,gates=GATES,all_gates=all(GATES.values()),
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_text(json.dumps(result,indent=2)+'\n')
    if out.stat().st_size>=1000000 or result['peak_rss_kib']>96*1024:
        raise ArithmeticError('Declared output or observed RSS gate')
    print(json.dumps({'formal_mathematical_gates':len(GATES),'all_gates':True,
        'first_piece_R':str(Rout),'first_piece_Lip':str(lip),'whole_cell9_phase':str(total_phase)}),flush=True)


if __name__=='__main__':
    main()
