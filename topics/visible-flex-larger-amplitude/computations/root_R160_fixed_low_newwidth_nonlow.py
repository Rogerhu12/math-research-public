#!/usr/bin/env python3
"""A fresh translated-width nonlow problem with the actual finite low field fixed.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only the known finite projection Pi_{2..92} F is reweighted. Every unknown
nonlow radius is newly solved, and identification uses a separate old-width
comparison box. All mean/inverse and infinite source terms remain positive.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from flint import arb, ctx

MODES = list(range(2, 93, 2))
TAU = F(18, 125)
M = 34816


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    raw = Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def ex(v):
    if isinstance(v, (F, int)):
        return F(v)
    if isinstance(v, dict):
        if 'upper' in v:
            return ex(v['upper'])
        if 'mantissa' in v:
            return F(int(v['mantissa'])) * F(2)**int(v['binary_exponent'])
        return F(int(v['numerator']), int(v['denominator']))
    return F(int(v[0])) * F(2)**v[1] if isinstance(v[1], int) else F(int(v[0]), int(v[1]))


def ab(v):
    v = ex(v)
    return arb(v.numerator) / arb(v.denominator)


def pack(v):
    z = v if isinstance(v, arb) else ab(v)
    if not z.is_finite() or z.upper() < 0:
        raise ArithmeticError('Finite nonnegative complete upper bound required')
    u = z.upper()
    if u == 0:
        return ['0', 0]
    m, e = map(int, u.man_exp())
    shift = max(0, m.bit_length()-160)
    if shift:
        m, e = (m+(1 << shift)-1) >> shift, e+shift
    if not arb(m)*arb(2)**e >= u:
        raise ArithmeticError('Outward serialization failed')
    return [str(m), e]


def up(v):
    return ex(pack(v))


def exp(v):
    return up(ab(v).exp())


def done(r):
    return r.get('exitcode', r.get('exit_code')) == 0 and r.get('termination_signal') is None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--shift', default='2/5')
    ap.add_argument('--finite-source-extra-width', default='1/2')
    a = ap.parse_args()
    if a.out.exists():
        raise FileExistsError('Preserve each actual new-width attempt')
    ctx.prec, ctx.threads = 512, 1
    start = time.monotonic()
    ids, data, gates = read(a.inputs), {}, {}
    shift, extra = F(a.shift), F(a.finite_source_extra_width)
    if not 0 < shift <= 1 or not 0 < extra <= 1:
        raise ValueError('Explicit positive finite width shifts required')

    def gate(name, ok):
        gates[name] = bool(ok)
        if not ok:
            raise ArithmeticError(name)

    for name, rec in ids.items():
        gate('identity_'+name, sha(rec['path']) == rec['sha256'])
        if not rec.get('source_only'):
            data[name] = read(rec['path'])
    sys.path.insert(0, str(Path(ids['nonlow_helper']['path']).parent))
    from nonlow_interface import NonlowInterface, inv
    spec = importlib.util.spec_from_file_location('known_finite_complete_source', ids['source_helper']['path'])
    src = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(src)
    outer, old, oldres = data['original_outer_inputs'], data['R156'], data['R156_resource']
    cs, head, wide, wideres = data['R155'], data['wide_head'], data['wide_primary'], data['wide_resource']
    p1, p1res = data['P1_modal'], data['P1_modal_resource']
    gate('actual_old_complete_field_and_real_parameter_scope', old['all_gates'] and all(old['gates'].values())
         and done(oldres) and old['same_existing_R127_field']
         and old['complete_mean_inverse_and_infinite_high_retained'])
    gate('same_finite_CL_and_original_source_formula', cs['all_gates'] and all(cs['gates'].values())
         and cs['same_CL_as_R101_R124_R127_and_R153'] and cs['no_centre_redefinition']
         and not cs['unknown_field_or_unknown_infinite_tail_widened']
         and old['inputs']['R155_centre_source']['sha256'] == ids['R155']['sha256'])
    gate('actual_new_complete_inner_field_identified', wide['all_gates'] and all(wide['gates'].values())
         and done(wideres) and wide['new_complete_fixedpoint_proved']
         and wide['same_original_full_field_identified'] and not wide['old_infinite_caps_reweighted']
         and wide['full_source_mean_inverse_far_retained'])
    gate('actual_P1_absolute_domain_for_the_same_real_point', p1['all_gates'] and all(p1['gates'].values())
         and done(p1res) and head['domain'] == wide['domain'] == p1['domain']
         and head['domain']['name'] == 'R156_actual_full_cut_posterior')
    gate('complete_actual_wide_head_export', head['all_gates'] and all(head['gates'].values())
         and done(data['wide_head_resource']) and head['primary']['sha256'] == ids['wide_primary']['sha256']
         and head['resource']['sha256'] == ids['wide_resource']['sha256']
         and head['complete_mean_inverse_far'] and head['complete_infinite_repaid']
         and ex(head['angular_weight_translation']) == shift
         and head['head_bands'] == [[94,184],[186,8190],[8192,None]]
         and head['same_original617_units']['sha256'] == '617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9')
    for name in ('nonlow', 'near', 'finite', 'high', 'balanced'):
        gate('original_complete_'+name, data[name]['all_gates'] and all(data[name]['gates'].values()))
    joint, finite, high, balanced = (data[k] for k in ('nonlow','finite','high','balanced'))
    gate('unchanged_nonlow_identity', outer['nonlow']['sha256'] == ids['nonlow']['sha256']
         and old['inputs']['original_finite']['sha256'] == ids['finite']['sha256']
         and old['inputs']['original_high']['sha256'] == ids['high']['sha256']
         and old['inputs']['original_balanced']['sha256'] == ids['balanced']['sha256'])
    gate('same_all25_causal_geometry_and_high_coordinates', joint['comparison_partition'] == finite['comparison_partition'] == high['comparison_partition']
         and joint['high_cutoff'] == M and joint['profile_high_block'] == 21
         and joint['physical_high_comparison_blocks'] == [5])
    ni = NonlowInterface(joint, data['near'])
    # All of the actual low projection is now fixed input. Zero is only the
    # expansion origin for the new H map, never a replacement for that field.
    ni.C = F(0)
    caps = [ex(row['same_CL_new_tau_pair_cap']) for row in cs['rows']]
    gate('same_original46_finite_modes', [r['mode'] for r in cs['rows']] == MODES
         and len(old['low_caps']) == 25 and all(len(r) == 46 for r in old['low_caps']))
    low_old, low_new, sources, source_records = [], [], [], []
    blocks = data['low_sources']['source_records']
    gate('all_original25_low_source_blocks', len(blocks) == 25
         and outer['low_sources']['sha256'] == ids['low_sources']['sha256'])
    for j, rec in enumerate(blocks):
        gate('actual_source_block_'+str(j), sha(rec['path']) == rec['sha256'])
        b = read(rec['path'])
        gate('same_block_strip_and_modes_'+str(j), b['index'] == j and b['modes'] == MODES)
        sigma = ex(b['sigma_max'])
        base = [up(c*exp(m*(sigma-TAU))+ex(u)) for m,c,u in zip(MODES,caps,old['low_caps'][j])]
        new = [up(c*exp(m*shift)) for m,c in zip(MODES,base)]
        plus = [up(c*exp(m*extra)) for m,c in zip(MODES,new)]
        low_old.append(base); low_new.append(new)
        positive = src.complete_source(plus, ni.V[j], 32)
        pairs = [(r['mode'], ex(r['bound'])) for r in positive['polynomial_pair_rows']]
        tail = ex(positive['shared_complete_inverse_tail'])
        # The entire positive tail is one mass for either output band.
        middle = up(sum((v*exp(-m*extra) for m,v in pairs if 94 <= m < M), F(0))+tail*exp(-94*extra))
        infinity = up(sum((v*exp(-m*extra) for m,v in pairs if m >= M), F(0))+tail*exp(-M*extra))
        gate('complete_known_finite_source_'+str(j), tail > 0 and middle > 0 and infinity > 0
             and positive['tail_is_one_mass_for_any_joint_frequency_partition'])
        sources.append((middle,infinity))
        source_records.append(dict(block=j,original_sigma_max=b['sigma_max'],shifted_sigma_max=pack(sigma+shift),
            exact_finite_source_extra_width=str(extra),old_actual_finite_pair_caps=list(map(pack,base)),
            new_actual_finite_pair_caps=list(map(pack,new)),source_mean_zero_cap=positive['mean_zero_cap'],
            source_inverse_leading_mass=positive['inverse_leading_mass'],complete_inverse_tail=positive['shared_complete_inverse_tail'],
            source_polynomial_support=positive['support_max_mode'],complete_middle_source=pack(middle),complete_infinite_high_source=pack(infinity)))
        print(json.dumps(dict(event='complete_fixed_actual_LF_source',block=j,low_mass=float(sum(new,F(0))),
            physical_low=float(ni.V[j]*sum(new,F(0))))),flush=True)
    hm = list(map(ex,head['translated_head_band_masses']))
    Bcut = ex(balanced['balanced_B_lower'])
    head_records=[]
    for i,(fr,hr) in enumerate(zip(finite['rows'],high['rows'])):
        gains=[ex(fr['given_band_gains'][band]['gain']) for band in ('near','rest','infinite')]
        if i == 21:
            cc=hr['initial_profile_balanced_column_sups']; hg=max(ex(cc[0])/Bcut,ex(cc[1]))
        elif i == 5:
            cc=hr['initial_balanced_column_sups']; hg=max(ex(cc[0])/Bcut,ex(cc[1]))
        else:
            cc=hr['initial_localV_separate_component_sups']; hg=max(sum(map(ex,cc[0]),F(0))/Bcut,sum(map(ex,cc[1]),F(0)))
        hf=up(sum((v*g for v,g in zip(hm,gains)),F(0)))
        hh=up(hm[2]*hg)
        sf=up(sum((ni.G[2][i][j]*sources[j][0] for j in range(i+1)),F(0)))
        sh=up(sum((ni.A[2][i][j]*sources[j][1] for j in range(i+1)),F(0)))
        ni.headf[i],ni.headh[i]=up(hf+sf),up(hh+sh)
        head_records.append(dict(block=i,actual_wide_finite_head=pack(hf),actual_wide_high_head=pack(hh),
            complete_fixed_low_middle_source=pack(sf),complete_fixed_low_high_source=pack(sh),
            new_constant_middle=pack(ni.headf[i]),new_constant_high=pack(ni.headh[i])))
    p=dict(U=[sum(r,F(0)) for r in low_new],caps=low_new,
           pure_f=[[F(0)]*(i+1) for i in range(25)],pure_h=[[F(0)]*(i+1) for i in range(25)],pure_q=[[F(0)]*(i+1) for i in range(25)])
    cold_domain=ni.domain(p,ni.headf,ni.headh)
    if any(v >= ni.Rstar for v in cold_domain):
        sol=dict(all_gates=False,failure={'reason':'complete_constant_upper_budget_exceeds_paid_physical_domain','blocks':[i for i,v in enumerate(cold_domain) if v>=ni.Rstar]},rows=[],r=[],h=[],weights=[])
    else:
        sol=ni.solve(p,padding=F(17,16),q=F(19,20),limit=128)
    comparison=[];same_field=False
    if sol['all_gates']:
        down_r=[up(r*exp(-94*shift)) for r in sol['r']]
        down_h=[up(h*exp(-M*shift)) for h in sol['h']]
        rr=[max(ex(old['finite_caps'][j]),down_r[j]) for j in range(25)]
        hh=[max(ex(old['high_caps'][j]),down_h[j]) for j in range(25)]
        uu=[sum(r,F(0)) for r in low_old];weights=[]
        domain=ni.domain(dict(U=uu),rr,hh)
        for i in range(25):
            nn=[ni.derivative_nn(i,j,uu[j],rr[j],hh[j]) for j in range(i+1)]
            rhs=(1+sum((nn[j][0]*weights[j][0]+nn[j][1]*weights[j][1] for j in range(i)),F(0)),
                 1+sum((nn[j][2]*weights[j][0]+nn[j][3]*weights[j][1] for j in range(i)),F(0)))
            w=inv(F(19,20),nn[i],rhs)
            if w is None:
                comparison.append(dict(block=i,all_gates=False,reason='comparison_positive_distance_inverse_failed'));break
            wf,wh=map(up,w);weights.append((wf,wh))
            df=sum((nn[j][0]*weights[j][0]+nn[j][1]*weights[j][1] for j in range(i+1)),F(0))/wf
            dh=sum((nn[j][2]*weights[j][0]+nn[j][3]*weights[j][1] for j in range(i+1)),F(0))/wh
            ok=domain[i]<ni.Rstar and df<F(19,20) and dh<F(19,20)
            comparison.append(dict(block=i,all_gates=ok,new_lowered_middle=pack(down_r[i]),new_lowered_high=pack(down_h[i]),
                comparison_middle=pack(rr[i]),comparison_high=pack(hh[i]),whole_physical_domain=pack(domain[i]),
                finite_distance_weight=pack(wf),high_distance_weight=pack(wh),finite_Jw_ratio=pack(df),high_Jw_ratio=pack(dh)))
            if not ok:break
        same_field=len(comparison)==25 and all(r['all_gates'] for r in comparison)
    complete=sol['all_gates'] and same_field
    result=dict(schema='same-actual-LF-new-uniform-width-complete50-nonlow-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.inputs),inputs=ids,all_gates=complete,
        gates={**gates,'new_complete_nonlow_selfmap_and_contraction':sol['all_gates'],'same_original_actual_field_identified':same_field},
        actual_parameter_scope='The same real R143 fixed point a*, with the existing actual finite low projection fixed. No new complex-parameter outer posterior is asserted.',
        parameter_domain=head['domain'],angular_weight_translation=str(shift),high_cutoff=M,
        original_geometry_unchanged=True,uniform_shift_cancels_in_every_same_frequency_Green_weight=True,
        low_projection_is_actual_existing_field_not_redefined_CL=True,only_known_finite_low_projection_reweighted=True,
        old_unknown_infinite_caps_reweighted=False,complete_mean_inverse_and_infinite_positive_sources=True,
        source_rows=source_records,head_and_source_rows=head_records,cold_upper_budget_domains=list(map(pack,cold_domain)),
        new_nonlow_solution=sol,old_width_comparison=comparison,new_fixedpoint_proved=sol['all_gates'],same_original_field_identified=same_field,
        nonlinear_equation='H=G_head(actual new-width nonlow head)+G_nonlow Pi_>92 N(LF+H), LF=Pi_<=92 of the already existing actual full solution.',
        identification='Lower the new H ball only. Compare new and old H in one old-width convex box at fixed identical LF; all50 complete derivative rows and physical mean/inverse domains are repaid.',
        failure_is_only_of_this_positive_budget_not_a_PDE_obstruction=not complete,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    def encode(v):
        if isinstance(v,F):return pack(v)
        raise TypeError(type(v).__name__)
    a.out.write_bytes(gzip.compress((json.dumps(result,default=encode,separators=(',',':'))+'\n').encode(),mtime=0))
    print(json.dumps(dict(all_gates=complete,new_fixedpoint=sol['all_gates'],same_field=same_field,failure=sol['failure'],
        primary_sha256=sha(a.out),bytes=a.out.stat().st_size,elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':
    main()
