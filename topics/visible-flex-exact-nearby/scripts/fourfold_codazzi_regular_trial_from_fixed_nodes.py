#!/usr/bin/env python3
"""Restore the original Hermite trial from its fixed complete nodal answer.

The recorded finite QR solve is historical. This process neither reruns
nor relabels it: it reconstructs all original one-sided Hermite pieces
with the unchanged producer and requires every original array and shard
SHA256. Its actual process result is a separate record. No inverse or
continuous residual claim follows from reconstructing a floating trial.
"""
from __future__ import annotations
import argparse, gzip, hashlib, json, sys, time
from pathlib import Path
import numpy as np
from flint import ctx
from fourfold_codazzi_final_regular_head_model import FinalHead
from fourfold_codazzi_final_regular_head_trial import HeadCollocation, Budget, incremental_spline
from fourfold_codazzi_candidate_shards import save_candidate
from fourfold_codazzi_phase_high7_CI_worker import save, now


def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):h.update(block)
    return h.hexdigest()


def restore_answer(manifest_path,role,destination):
    manifest=json.loads(manifest_path.read_text());entry=manifest['roles'][role]
    if destination.exists():raise FileExistsError('preserve every restored original answer')
    offset=0
    with destination.open('wb') as stream:
        for i,part in enumerate(entry['parts']):
            if part['index']!=i or part['offset']!=offset or Path(part['file']).name!=part['file']:
                raise ValueError('the original nodal container has a gap or invalid filename')
            path=manifest_path.parent/part['file'];raw=path.read_bytes()
            if len(raw)!=part['compressed_bytes'] or hashlib.sha256(raw).hexdigest()!=part['compressed_sha256']:
                raise ValueError('a compressed original nodal piece changed')
            decoded=gzip.decompress(raw)
            if len(decoded)!=part['bytes'] or hashlib.sha256(decoded).hexdigest()!=part['sha256']:
                raise ValueError('an original nodal byte range changed')
            stream.write(decoded);offset+=len(decoded)
    if offset!=entry['original_bytes'] or digest(destination)!=entry['original_sha256']:
        raise ValueError('the full original nodal answer was not restored exactly')
    return manifest,entry


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--nodal-manifest',type=Path,required=True)
    ap.add_argument('--role',choices=('response','adjoint'),required=True)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--q-vector',type=Path,default=Path('notes/2026-11-13-R133-regular-r25over8-q256-floating.json'))
    ap.add_argument('--waist-row',type=Path,default=Path('notes/2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json'))
    ap.add_argument('--work',type=Path,required=True)
    ap.add_argument('--trial-directory',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every actual reconstruction outcome')
    args.work.mkdir(parents=True,exist_ok=True);args.trial_directory.mkdir(parents=True,exist_ok=True)
    doc=dict(kind='actual_same_regular_trial_from_original_nodal_answer_v1',complete=False,
        role=args.role,source_sha256=digest(__file__),started_utc=now(),failure=None,
        finite_QR_solve_reexecuted=False,historical_case_refers_to_original_nodal_solution=True,
        actual_new_reconstruction_separate_from_historical_solve=True,
        continuous_BVP_inverse_proved=False)
    try:
        manifest,entry=restore_answer(args.nodal_manifest,args.role,args.work/'answer-0.npy')
        if digest(args.candidate)!=manifest['candidate_sha256']:
            raise ValueError('the complete original ac1 candidate changed')
        producer=Path(__file__).with_name('fourfold_codazzi_final_regular_head_trial.py')
        if digest(producer)!=manifest['original_trial_source_sha256']:
            raise ValueError('the original complete one-sided Hermite algorithm changed')
        historical={}
        for name,item in entry['historical_complete_trial_source'].items():
            path=args.nodal_manifest.parent/item['file']
            if path.stat().st_size!=item['bytes'] or digest(path)!=item['sha256']:
                raise ValueError('a historical trial descriptor changed')
            historical[name]=json.loads(path.read_text())
        prior=historical['finite-native.json']
        if not prior['complete'] or prior['failure'] is not None or prior['case']!=entry['case']:
            raise ValueError('the original finite nodal solve is not its recorded complete case')
        if (prior['identity']['role']!=args.role or prior['identity']['radial_subdivisions']!=1
            or prior['identity']['span']!=8 or prior['source_sha256']!=digest(producer)):
            raise ValueError('the original full trial parameters changed')
        model=FinalHead(args.candidate,args.object,args.q_vector,args.waist_row,
            modes=96,angles=1024,boundary_angles=8192)
        if model.identity!=prior['identity']['model']:
            raise ValueError('the actual scientific head model differs from the original')
        problem=HeadCollocation(model,model.nodes,args.role)
        answer=np.load(args.work/'answer-0.npy',mmap_mode='r',allow_pickle=False)
        if answer.shape!=(problem.n*problem.nodes+1,) or not np.all(np.isfinite(answer)):
            raise ValueError('the full original nodal answer has an invalid shape')
        cubic=incremental_spline(problem,args.work,answer,Budget(100000000))
        cubic_sha=digest(args.work/'trial-cubic.npy')
        doc['actual_reconstructed_cubic_sha256']=cubic_sha
        doc['expected_original_cubic_sha256']=entry['original_cubic']['sha256']
        if cubic_sha!=entry['original_cubic']['sha256']:
            raise ValueError('the reconstructed Hermite cubic differs from the original bytes')
        outputs={}
        for projected,label in ((False,'full'),(True,'nonmean')):
            old=historical[label+'.json'];path=args.trial_directory/(args.role+'-'+label+'.json')
            coefficients=np.asarray(cubic).copy() if projected else cubic
            if projected:coefficients[:,:,model.m]=0.
            save_candidate(path,radial_nodes=problem.x,piece_coefficients=coefficients,
                initial_state=coefficients[-1,0,:].copy(),metadata=np.array(json.dumps(old['metadata'])))
            expected=entry['historical_complete_trial_source'][label+'.json']['sha256']
            actual=digest(path)
            outputs[label]=dict(path=str(path),sha256=actual,expected_sha256=expected)
            doc['outputs']=outputs
            if actual!=expected:raise ValueError('a reconstructed original trial index or shard differs: '+label)
            new=json.loads(path.read_text())
            if new!=old:raise ValueError('the original complete trial descriptor differs')
            for part in old['parts']:
                file=path.parent/part['file']
                if file.stat().st_size!=part['bytes'] or digest(file)!=part['sha256']:
                    raise ValueError('an original complete Hermite shard changed')
        doc.update(complete=True,original_case=entry['case'],original_answer_sha256=entry['original_sha256'],
            original_trial_source_sha256=digest(producer),whole_candidate_sha256=digest(args.candidate),
            all_original_one_sided_derivatives_reconstructed=True,all_original_shards_match=True,
            all_finite_mean_and_nonmean_columns_retained=True,trial_piece_count=problem.nodes-1)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        doc.update(wall_seconds=time.monotonic()-started,finished_utc=now());save(args.out,doc)
    print(json.dumps(dict(complete=doc['complete'],role=args.role,original_case=entry['case'],
        cubic_sha256=cubic_sha)),flush=True)


if __name__=='__main__':main()
