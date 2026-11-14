#!/usr/bin/env python3
"""Public-runner entry: exact centre replay, then the new physical cap graph.

Large regenerable arrays stay under --work, outside the repository. Only
small actual reports and the endpoint proposal are exported. No finite
success is represented as a continuous graph or a whole-body inverse.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic',type=Path,default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--candidate',type=Path)
    parser.add_argument('--work',type=Path,required=True)
    parser.add_argument('--out-dir',type=Path,required=True)
    parser.add_argument('--address-space-mib',type=int,default=6144)
    args=parser.parse_args();started=time.monotonic()
    topic,work,out=args.topic.resolve(),args.work.resolve(),args.out_dir.resolve()
    if topic==work or topic in work.parents:
        raise ValueError('large cap arrays must stay in runner temporary storage')
    work.mkdir(parents=True,exist_ok=True);out.mkdir(parents=True,exist_ok=True)
    summary_path=out/'runner-status.json'
    if summary_path.exists():raise FileExistsError('preserve the actual previous runner outcome')
    summary=dict(kind='actual_public_runner_full_physical_cap_DN_proposal',complete=False,
                 source_sha256=sha(__file__),children=[],failure=None,
                 mathematical_certificate=False,continuous_graph_error_not_yet_certified=True)
    def save():
        summary['wall_seconds']=time.monotonic()-started
        temporary=summary_path.with_suffix('.partial')
        temporary.write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n');temporary.replace(summary_path)
    def limit():
        bound=args.address_space_mib*1024**2
        resource.setrlimit(resource.RLIMIT_AS,(bound,bound))
    def execute(command,limited=False):
        start=time.monotonic();print(json.dumps(dict(actual_command=command)),flush=True)
        child=subprocess.run(command,cwd=topic,preexec_fn=limit if limited else None)
        summary['children'].append(dict(command=command,actual_returncode=child.returncode,
                                         wall_seconds=time.monotonic()-start))
        save()
        if child.returncode:raise RuntimeError('actual child returned '+str(child.returncode))
    save()
    try:
        if args.candidate is None:
            pointer=work/'final-candidate-path.txt'
            execute([sys.executable,str(topic/'scripts/fourfold_codazzi_final_replay_chain_runner.py'),
                '--topic',str(topic),'--work',str(work/'replay'),'--out-dir',str(out/'replay'),
                '--candidate-path-file',str(pointer),'--address-space-mib',str(args.address_space_mib)])
            candidate=Path(pointer.read_text().strip())
        else:candidate=args.candidate.resolve()
        if sha(candidate)!='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413':
            raise ValueError('the exact original final centre must actually be restored')
        summary['candidate_sha256']=sha(candidate)
        native=out/'physical-cap-DN-proposal.json'
        execute([sys.executable,str(topic/'scripts/fourfold_codazzi_physical_cap_DN_proposal.py'),
            '--candidate',str(candidate),'--left','9/10','--max-new-blocks','10000000',
            '--work',str(work/'physical-cap'),'--out',str(native)],limited=True)
        result=json.loads(native.read_text())
        if not result.get('complete') or result.get('failure'):
            raise RuntimeError('the actual cap graph proposal did not complete')
        endpoint=Path(result['physical_endpoint_graph']['path'])
        if sha(endpoint)!=result['physical_endpoint_graph']['sha256']:
            raise ValueError('the actual complete endpoint matrix changed')
        if endpoint.stat().st_size>5_000_000:
            raise ValueError('only a small endpoint proposal may be exported')
        destination=out/'physical-cap-endpoint-graph.npz'
        if destination.exists():raise FileExistsError('preserve the earlier endpoint graph')
        shutil.copyfile(endpoint,destination)
        summary.update(complete=True,native_sha256=sha(native),
                       endpoint_graph_sha256=sha(destination),
                       complete_matrix_Hermite_arrays_location=str(work/'physical-cap'),
                       arrays_are_reconstructible_not_published=True,
                       original_all_193_state_and_97_regular_rows_retained=True,
                       continuous_residual_and_all_Fourier_tail_still_required=True)
    except Exception as error:
        summary['failure']=dict(type=type(error).__name__,message=str(error))
        raise
    finally:save()
    print(json.dumps(dict(complete=True,out_dir=str(out))),flush=True)


if __name__=='__main__':main()
