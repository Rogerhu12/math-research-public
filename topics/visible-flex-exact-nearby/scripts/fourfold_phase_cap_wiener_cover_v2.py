#!/usr/bin/env python3
"""Bounded-memory, restartable real Wiener integration of actual cap body FEs.

Every actual scalar common span is kept. One completed finite-element report
is saved at a time; only the current element's matrices remain in memory.
Failure or a large error is retained explicitly and never silently skipped.
The complete flag refers exactly to the requested physical body interval.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time

from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_interval import FiniteTrial,gauss_rule,sha
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_cap_wiener_box import integrate_box
from fourfold_phase_cap_vector_germs import VectorWienerBodyForm as WienerBodyForm


def write_json(path,record):
    path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(record,indent=2)+'\n').encode()
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_bytes(gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw)
    temporary.replace(path)


def read_json(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial',type=Path,default=Path('notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    parser.add_argument('--start-element',type=int,default=20)
    parser.add_argument('--stop-element',type=int,default=64)
    parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--max-depth',type=int,default=4)
    parser.add_argument('--error-per-length',type=Fraction,default=Fraction(1,1000))
    parser.add_argument('--out-dir',type=Path,required=True)
    parser.add_argument('--stop-file',type=Path)
    args=parser.parse_args();ctx.prec,ctx.cap=args.bits,4
    wall,cpu=time.monotonic(),time.process_time()
    trial=FiniteTrial(args.trial)
    if not 0<=args.start_element<args.stop_element<=trial.cells:
        raise ValueError('invalid requested finite element interval')
    left=Fraction(float(trial.mesh[args.start_element]));right=Fraction(float(trial.mesh[args.stop_element]))
    if not Fraction(1,4)<=left<right<=3:
        raise ValueError('the Wiener body entry does not certify the distinct graft')
    target=WienerBodyForm(trial.object_path,128,128,arb('.003'),arb('.0025'),arb('.32'))
    common=common_cells(target);nodes,weights=gauss_rule(trial.degree+1)
    sources=[Path(__file__),*map(lambda name:Path(__file__).with_name(name),(
        'fourfold_phase_cap_wiener_box.py','fourfold_phase_cap_scaled_body.py',
        'fourfold_phase_cap_energy_interval.py','fourfold_phase_beta_affine.py',
        'fourfold_phase_beta_bulk_box.py','fourfold_phase_cap_moment_space.py',
        'fourfold_phase_cap_vector_germs.py'))]
    identity=dict(source_sha256=sha(__file__),dependency_sha256={p.name:sha(p) for p in sources[1:]},
        trial_report_path=str(args.trial),trial_report_sha256=sha(args.trial),
        exact_trial_arrays=trial.report['arrays'],object_sha256=trial.report['object_sha256'],
        exact_delta_fraction=trial.report['exact_delta_fraction'],bits=args.bits,
        error_density_target=str(args.error_per_length),max_depth=args.max_depth,
        boundary_physical_modes=trial.B,interior_physical_modes=trial.M,radial_degree=trial.degree)
    manifest=dict(kind='true_infinite_Wiener_body_energy_cover',complete=False,identity=identity,
        requested_exact_radial_interval=[str(left),str(right)],
        requested_element_range=[args.start_element,args.stop_element],elements=[],
        full_positive_cap_complete=False,
        scope='Only the requested body interval. All infinite angular perturbations and every scalar common span are included; no whole cap or final inverse claim.')
    def save():
        manifest['CPU_seconds_this_invocation']=time.process_time()-cpu
        manifest['wall_seconds_this_invocation']=time.monotonic()-wall
        write_json(args.out_dir/'manifest.json',manifest)
    for element in range(args.start_element,args.stop_element):
        if args.stop_file is not None and args.stop_file.exists():
            manifest['stopped_between_elements']=True
            save();break
        a,b=map(lambda x:Fraction(float(x)),trial.mesh[element:element+2])
        path=args.out_dir/f'element_{element:03d}.json.gz'
        if path.exists():
            saved=read_json(path)
            if saved.get('identity')!=identity or saved.get('exact_radial_interval')!=[str(a),str(b)]:
                raise ValueError('saved body element has a different actual function, source, or requested interval')
            if saved.get('complete'):
                manifest['elements'].append(dict(element=element,path=str(path),sha256=sha(path),
                    complete=True,errors=saved['integrated_operator_errors']))
                save();print(json.dumps(dict(resumed_element=element)),flush=True);continue
        points=sorted({a,b}|{x for x in common if a<x<b})
        rows=[];failed=[];rejected=[]
        record=dict(kind='true_infinite_Wiener_body_element_energy',complete=False,identity=identity,
            element=element,exact_radial_interval=[str(a),str(b)],
            original_common_span_count=len(points)-1,intervals=rows,failed=failed,rejected=rejected,
            gauss_nodes=list(map(ball_record,nodes)),gauss_weights=list(map(ball_record,weights)))
        local_wall,local_cpu=time.monotonic(),time.process_time()
        for start,end in zip(points,points[1:]):
            k=bisect_right(common,(start+end)/2)-1
            target.set_cell(common[k],common[k+1])
            pending=[(start,end,0)]
            while pending:
                l,r,depth=pending.pop()
                try:
                    values,diagnostics=target.whole_angle_values(l,r)
                    energies=integrate_box(values,trial,element,l,r,nodes,weights)
                    density=max(arb(x['full_operator_error']['ball']).upper() for x in energies)/exact_arb(r-l)
                    if not density<=exact_arb(args.error_per_length):
                        raise ValueError('full interval energy error density exceeds target: '+density.str(16))
                    rows.append(dict(exact_radial_interval=[str(l),str(r)],
                        actual_common_span=list(map(str,target.cell)),subdivision_depth=depth,
                        true_form_and_inverse_boxes=list(map(ball_record,values)),
                        infinite_Wiener_diagnostics=diagnostics,
                        primal_energy=energies[0],dual_energy=energies[1]))
                except (ValueError,ZeroDivisionError) as exc:
                    item=dict(exact_radial_interval=[str(l),str(r)],depth=depth,reason=str(exc))
                    if depth==args.max_depth:failed.append(item)
                    else:
                        rejected.append(item);mid=(l+r)/2
                        pending.extend([(mid,r,depth+1),(l,mid,depth+1)])
            # Save after each common cell.  The matrix working set is one FE,
            # not an accumulating raw primitive or all-body matrix cache.
            record['CPU_seconds']=time.process_time()-local_cpu
            record['wall_seconds']=time.monotonic()-local_wall
            write_json(path,record)
        rows.sort(key=lambda x:Fraction(x['exact_radial_interval'][0]))
        cursor=a
        for row in rows:
            l,r=map(Fraction,row['exact_radial_interval'])
            if l!=cursor:break
            cursor=r
        record['complete']=not failed and cursor==b
        record['integrated_operator_errors']={key:ball_record(sum((
            arb(row[key]['full_operator_error']['ball']).upper() for row in rows),arb(0)).upper())
            for key in ('primal_energy','dual_energy')}
        write_json(path,record)
        manifest['elements'].append(dict(element=element,path=str(path),sha256=sha(path),
            complete=record['complete'],errors=record['integrated_operator_errors']))
        save()
        print(json.dumps(dict(element=element,complete=record['complete'],accepted=len(rows),failed=len(failed),
            errors={k:v['ball'] for k,v in record['integrated_operator_errors'].items()},
            CPU_seconds=record['CPU_seconds'],wall_seconds=record['wall_seconds'])),flush=True)
        if not record['complete']:
            raise SystemExit('requested energy budget remains unpaid on this element; partial output preserved')
        del rows,record
    manifest['complete']=all(x['complete'] for x in manifest['elements']) and len(manifest['elements'])==args.stop_element-args.start_element
    manifest['integrated_operator_errors']={key:ball_record(sum((arb(x['errors'][key]['ball']).upper()
        for x in manifest['elements']),arb(0)).upper()) for key in ('primal_energy','dual_energy')}
    save();print(json.dumps(dict(complete=manifest['complete'],
        integrated_operator_errors=manifest['integrated_operator_errors'])),flush=True)


if __name__=='__main__':main()
