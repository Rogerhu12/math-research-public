#!/usr/bin/env python3
"""Actual complete original outer9..0 fixed-frame homogeneous budget.

The already certified cell9 rows are consumed, not regenerated. Cells8..1
are first-time material packets; cell0 reuses its original successful packet.
Every mode is covered. This ledger is not a nonlinear continuation claim.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'outer-continuation-inputs/sources'))
from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q,ball_record
from closure_real_head_green_enclosure import ball
from closure_split_joint_io import iter_array

GATES={}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def check(k,v):
    if k in GATES:raise ValueError('Repeated gate '+k)
    GATES[k]=bool(v)
    if not v:raise ArithmeticError('Unpaid gate '+k)
def up(v):
    if not v.is_finite():raise ArithmeticError('Nonfinite upper bound')
    return v.upper()
def plog(v):
    if not v>0:raise ArithmeticError('Nonpositive frame ratio')
    return max(arb(0),up(v.log()))
def rec(v):
    if not v.is_finite():raise ArithmeticError('Nonfinite output')
    return ball_record(v)
def main():
    started=time.monotonic();ctx.prec=256
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs',required=True)
    p.add_argument('--out-prefix',required=True)
    a=p.parse_args();ip=read(a.inputs);prefix=Path(a.out_prefix)
    target=prefix.with_suffix('.json')
    if target.exists():raise FileExistsError('Fresh ledger required')
    docs={}
    for k,v in ip['inputs'].items():
        check('pin_'+k,sha(v['path'])==v['sha256']);docs[k]=read(v['path'])
    prior=docs['cell9_ledger']
    check('same_actual_cell9',ip['inputs']['cell9_ledger']['sha256']=='0d00170ca522c8f900a46f5e826a1cc2d7a486127797a3b5ec48c0ef5621e977')
    check('all_prior_gates',prior['all_gates'] and all(prior['gates'].values()))
    minimum=exact_q(F(1,256));before=prior['frame_ledger']
    first=ball(before[0]['first_frame']);previous=ball(before[-1]['last_frame'])
    total_phase=ball(prior['complete_cell9_phase_upper'])
    total_f=up(sum((ball(z['forward_with_initial_jump']) for z in before),arb(0)))
    total_b=up(sum((ball(z['backward_with_initial_jump']) for z in before),arb(0)))
    total_c=ball(prior['complete_cell9_cbg_upper'])
    rows=[dict(cell=9,panels=prior['original_cell9_panels'],reused_prior_primary=True,
        cell_phase_upper=rec(total_phase),cumulative_phase_upper=rec(total_phase),
        cumulative_physical_forward_log_upper=rec(up(total_f+plog(1/first)+plog(previous))),
        cumulative_physical_backward_log_upper=rec(up(total_b+plog(1/previous)+plog(first))))]
    count=prior['original_cell9_panels'];files=[]
    for cell in range(8,-1,-1):
        m=docs[f'cell{cell}_material'];r=docs[f'cell{cell}_resource']
        check(f'cell{cell}_formal0',r['exitcode']==0 and r['termination_signal'] is None)
        check(f'cell{cell}_all_source_gates',all(m['checks'].values()) and m['cell']==cell)
        check(f'cell{cell}_same_background',set(m['original_metadata']['input_hashes'].values())=={
            '563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6',
            '28d491b998174029a80daf41e9365de6ab2c54757419de7b64f54445047b717f'})
        check(f'cell{cell}_all_nine_segments',[z['source_segment'] for z in m['groups']]==list(range(9)))
        cp,cf,cb,cc=arb(0),arb(0),arb(0),arb(0)
        segments=[];nc=0
        for g in m['groups']:
            seg=g['source_segment'];path=Path(g['path'])
            if not path.is_absolute():path=Path(ip['original_topic_root'])/path
            check(f'cell{cell}_seg{seg}_source_sha',sha(path)==g['sha256'])
            gp,gf,gb,gc=arb(0),arb(0),arb(0),arb(0)
            begin=F(0);n=0;bfirst=None
            for z in iter_array(path,'panels'):
                left,right=F(z['x_left']),F(z['x_right'])
                if left!=begin or right<=left or z['segment']!=seg:raise ArithmeticError('Original coverage')
                begin=right;dx=exact_q(right-left)
                rr,rx,ell,w=[ball(z[k]) for k in ['radius','radius_x','log_w_x','w']]
                if not all(x.is_finite() for x in [rr,rx,ell,w]) or not(rr>0 and rx>0 and w>0 and w.upper()<=arb(1)/2):
                    raise ArithmeticError('Whole original background gate')
                s=rx/rr;sl,su,el,eu=s.lower(),s.upper(),ell.lower(),ell.upper()
                sq=max(minimum*minimum,up(eu/su),up(-(el+eu)/(sl+su)))
                b=up(sq.sqrt())
                gamma=up(abs(s*b+ell/b)/2)
                dplus=up(max((-s-ell).upper(),(-2*ell).upper())*dx)
                dminus=up(max((s+ell).upper(),(2*ell).upper())*dx)
                cbg=up((s+abs(ell))*dx)
                if not b>=minimum or not gamma>=0 or not cbg>0:raise ArithmeticError('Fixed frame or complete source sign')
                dplus=up(dplus+plog(previous/b));dminus=up(dminus+plog(b/previous))
                previous=b
                if bfirst is None:bfirst=b
                gp=up(gp+gamma*dx);gf=up(gf+dplus);gb=up(gb+dminus);gc=up(gc+cbg)
                n+=1;nc+=1;count+=1
                if count%128==0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>96*1024:
                    raise MemoryError('96 MiB declared resource guard')
            check(f'cell{cell}_seg{seg}_whole_coverage',begin==1 and n==g['panels'])
            cp=up(cp+gp);cf=up(cf+gf);cb=up(cb+gb);cc=up(cc+gc)
            segments.append(dict(segment=seg,panels=n,phase_upper=rec(gp),cbg_integral_upper=rec(gc),
                first_frame=rec(bfirst),last_frame=rec(previous),forward_with_entry_jump=rec(gf),backward_with_entry_jump=rec(gb)))
        check(f'cell{cell}_complete_panel_count',nc==m['panels'])
        total_phase=up(total_phase+cp);total_f=up(total_f+cf);total_b=up(total_b+cb);total_c=up(total_c+cc)
        row=dict(cell=cell,panels=nc,reused_original_cell0=(cell==0),segments=segments,
            cell_phase_upper=rec(cp),cumulative_phase_upper=rec(total_phase),
            cumulative_cbg_integral_upper=rec(total_c),
            cumulative_physical_forward_log_upper=rec(up(total_f+plog(1/first)+plog(previous))),
            cumulative_physical_backward_log_upper=rec(up(total_b+plog(1/previous)+plog(first))))
        rows.append(row)
        checkpoint=prefix.with_name(prefix.name+f'-cell{cell:02d}.json')
        if checkpoint.exists():raise FileExistsError('Fresh cell checkpoint required')
        checkpoint.write_text(json.dumps(row,indent=2)+'\n')
        files.append(dict(path=str(checkpoint),sha256=sha(checkpoint),bytes=checkpoint.stat().st_size))
        print(json.dumps({'cell':cell,'panels':nc,'phase':str(cp),'cumulative_phase':str(total_phase),
            'forward_log':str(up(total_f+plog(1/first)+plog(previous)))}),flush=True)
    check('all_ten_original_cells',len(rows)==10 and [z['cell'] for z in rows]==list(range(9,-1,-1)))
    result=dict(schema='original-all-outer9to0-complete-fixed-frame-ledger-v1',source_sha256=sha(__file__),
        input_manifest_sha256=sha(a.inputs),inputs=ip,rows=rows,files=files,total_panels=count,
        complete_phase_upper=rec(total_phase),complete_forward_log_upper=rows[-1]['cumulative_physical_forward_log_upper'],
        complete_backward_log_upper=rows[-1]['cumulative_physical_backward_log_upper'],
        available_R142_trace_strip='1/64',target_example_strip='1/128',
        desired_input_strip_for_this_phase_bound=rec(up(total_phase+exact_q(F(1,128)))),
        homogeneous_only=True,nonlinear_Green_or_full_outer_continuation_proved=False,
        no_new_ODE_or_quadrature=True,all_source_order_and_frame_jumps_retained=True,
        gates=GATES,all_gates=all(GATES.values()),elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    target.write_text(json.dumps(result,indent=2)+'\n')
    if target.stat().st_size>=1000000:raise ArithmeticError('Compact output gate')
    print(json.dumps({'all_gates':True,'gate_count':len(GATES),'total_panels':count,
        'complete_phase':str(total_phase),'elapsed_seconds':result['elapsed_seconds']}),flush=True)


if __name__=='__main__':main()
