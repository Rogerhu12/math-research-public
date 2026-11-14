#!/usr/bin/env python3
"""Consume the original complete body rows and both actual scalar errors.

This infrastructure adapter never recomputes a completed residual row. It
checks the original 40-part partition, preserves all original process
records, restores only the original canonical trial aliases, and invokes
the unchanged complete scalar mean-error consumer. A complete outcome is
a residual certificate, not a continuous inverse or a true Schur bound.
"""
from __future__ import annotations
import argparse, gzip, os, shutil, signal, sys
from fractions import Fraction
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest, read, link_exact
from fourfold_codazzi_phase_high7_CI_worker import TOPIC, REPO, save

REPOSITORY='Rogerhu12/math-research-public'


class CompleteMeanWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-complete-mean-from-{args.original_run}'
        self.dest=TOPIC/'notes/correlated_body_ci'/self.name
        self.state.update(kind='actual_public_complete_correlated_body_mean_consumer_process',
            original_body_run=args.original_run,original_body_attempt=args.original_attempt,
            finalizer_source_sha256=digest(__file__),requested_rows=[0,7721],
            continuous_BVP_inverse_proved=False,true_nu_Schur_nonzero_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if digest(__file__)!=self.args.finish_source_sha:
            raise ValueError('the explicit complete-mean adapter changed')
        if self.manifest['total_common_cells']!=7721:
            raise ValueError('this original complete body domain changed')

    def restore_original_bundle(self):
        prepared=self.args.prepared.resolve();bundle=read(prepared/'prepared-manifest.json')
        if (bundle.get('kind')!='exact_same_all_regular_body_CI_bundle_v1'
            or not bundle.get('complete')
            or bundle.get('input_manifest_sha256')!=self.args.manifest_sha
            or not bundle.get('all_original_cubic_and_trial_shard_SHA256_verified')):
            raise ValueError('the successful original complete body preparation is required')
        for relative,entry in bundle['files'].items():
            path=prepared/relative
            if path.stat().st_size!=entry['bytes'] or digest(path)!=entry['sha256']:
                raise ValueError('an original body trial byte changed')
        for canonical,relative in bundle['canonical_aliases'].items():
            link_exact(canonical,prepared/relative)
        for original,expected in self.manifest['row_identity']['original_inputs'].items():
            path=Path(original) if Path(original).is_absolute() else self.science_topic/original
            if digest(path)!=expected:
                raise ValueError('an original canonical scientific input changed')
        save(self.evidence/'original-preparation-identity.json',dict(
            original_body_run=self.args.original_run,original_body_attempt=self.args.original_attempt,
            original_prepared_manifest_sha256=digest(prepared/'prepared-manifest.json'),
            all_original_scientific_bytes_verified=True,
            original_expected_SHA256_values_unchanged=True))

    def original_complete_parts(self):
        paths=[];expected=set()
        for item in self.manifest['already_complete_original_parts']:
            path=self.science/item['path']
            if digest(path)!=item['sha256']:
                raise ValueError('an already completed original part changed')
            paths.append(path);expected.add(tuple(item['indices']))
        requested={tuple(x) for x in self.manifest['consumer_ranges']}
        observed=set()
        for folder in sorted(self.args.previous_artifacts.iterdir()):
            if not folder.is_dir():continue
            process=folder/'process.json'
            if not process.exists():raise ValueError('an original row artifact has no actual process record')
            actual=read(process)
            if (actual.get('repository')!=REPOSITORY
                or str(actual.get('run_id'))!=str(self.args.original_run)
                or str(actual.get('run_attempt'))!=str(self.args.original_attempt)
                or actual.get('input_manifest_sha256')!=self.args.manifest_sha
                or not actual.get('complete') or actual.get('failure')):
                raise ValueError('an original body worker has not actually completed this scientific input')
            pair=tuple(actual['requested_rows'])
            if pair not in requested or pair in observed:
                raise ValueError('a body worker artifact is missing, duplicated or outside its original assignment')
            observed.add(pair)
            children=actual.get('children',[])
            if any(c.get('actual_returncode')!=0 for c in children):
                raise ValueError('retain the original unsuccessful mathematical child outcome')
            target=self.evidence/'original-processes'/folder.name
            target.mkdir(parents=True,exist_ok=True);shutil.copyfile(process,target/'process.json')
            if (folder/'producer.stdout.log').exists():
                (target/'producer.stdout.log.gz').write_bytes(gzip.compress(
                    (folder/'producer.stdout.log').read_bytes(),mtime=0))
            assigned=self.manifest['atomic_ranges'][f'{pair[0]}-{pair[1]}']
            actual_files={}
            for path in sorted((folder/'native').glob('*.json.gz')):
                document=read(path)
                if document.get('kind')!=self.manifest['residual_kind']:
                    raise ValueError('an original native artifact contains another scientific object')
                selected=tuple(document['selected_indices'])
                if list(selected) not in assigned or selected in actual_files:
                    raise ValueError('an original atomic body part is duplicated or outside the assigned range')
                actual_files[selected]=path
            if set(actual_files)!={tuple(x) for x in assigned}:
                raise ValueError('an original worker artifact has an incomplete atomic cover')
            paths.extend(actual_files.values());expected.update(actual_files)
        if observed!=requested:raise ValueError('all eight original complete body artifacts are required')
        ordered=[]
        for path in paths:
            doc=read(path)
            if (doc.get('kind')!=self.manifest['residual_kind']
                or doc.get('identity')!=self.manifest['row_identity']
                or not doc.get('selected_cells_complete') or doc.get('failure') is not None):
                raise ValueError('every original body part must retain its complete successful identity')
            first,end=doc['selected_indices'];rows=doc['rows']
            if [r['common_row'] for r in rows]!=list(range(first,end)):
                raise ValueError('an original body part has a missing or repeated exact row')
            for a,b in zip(rows,rows[1:]):
                if Fraction(a['interval'][1])!=Fraction(b['interval'][0]):
                    raise ValueError('an original body part has a radial gap')
            ordered.append(dict(path=path,indices=[first,end],sha256=digest(path),
                rows=len(rows),interval=[rows[0]['interval'][0],rows[-1]['interval'][1]]))
        ordered.sort(key=lambda x:x['indices'][0]);next_index=0;next_radius=Fraction(0)
        for item in ordered:
            if item['indices'][0]!=next_index or Fraction(item['interval'][0])!=next_radius:
                raise ValueError('the complete original body assembly contains a gap or duplicate')
            next_index=item['indices'][1];next_radius=Fraction(item['interval'][1])
        if next_index!=7721 or next_radius!=Fraction(25,8) or len(ordered)!=40:
            raise ValueError('the exact original full 7721-row, 40-part body cover is required')
        cover=dict(kind='actual_complete_original_body_row_cover_before_mean_error_flow',
            complete=True,original_body_run=self.args.original_run,
            original_body_attempt=self.args.original_attempt,original_row_identity=self.manifest['row_identity'],
            complete_common_rows=7721,exact_interval=['0','25/8'],each_original_row_once=True,
            all_exact_radial_joins_checked=True,original_rows_recomputed=0,
            original_parts=[dict(item,path=str(item['path'])) for item in ordered],
            complete_mean_error_flow_claimed=False,continuous_BVP_inverse_claimed=False)
        save(self.evidence/'complete-original-row-cover.json',cover)
        self.state.update(complete_original_row_cover_verified=True,complete_original_rows=7721,
            original_rows_recomputed=0,original_part_count=40)
        return [item['path'] for item in ordered]

    def consume(self):
        self.restore_original_bundle();parts=self.original_complete_parts();self.publish()
        native=self.cache/'complete-correlated-body-and-mean-errors.json.gz'
        command=[sys.executable,'-u',str(self.science_topic/'scripts/fourfold_codazzi_correlated_mean_error_consumer.py')]
        for name,path in self.manifest['original_cli_inputs'].items():command+=['--'+name,path]
        command+=['--parts',*[str(p) for p in parts],'--out',str(native)]
        self.execute('complete_original_7721_rows_both_scalar_errors_and_all_trial_jumps',command)
        document=read(native)
        if (document.get('kind')!='actual_complete_correlated_mean_errors_and_full_body_residuals_v1'
            or not document.get('complete') or document.get('failure')
            or document.get('row_identity')!=self.manifest['row_identity']
            or document.get('complete_original_common_cells')!=7721
            or not document.get('exact_continuous_completed_means')
            or not document.get('complete_mean_residuals_exactly_zero')):
            raise ValueError('the actual complete original mean-error consumer did not succeed')
        omit={'full_trial_mean_jumps','adjoint_error_flow','response_error_reverse',
            'residual_rows','response_nonmean_jumps','adjoint_nonmean_jumps'}
        summary={k:v for k,v in document.items() if k not in omit}
        summary['native_array_lengths']={k:len(document[k]) for k in omit if k in document}
        summary['complete_native_sha256']=digest(native)
        save(self.evidence/'complete-body-mean-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            complete_original_mean_errors_and_body_residuals=True,
            continuous_BVP_inverse_proved=False,true_nu_Schur_nonzero_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',type=Path,required=True);p.add_argument('--manifest-sha',required=True)
    p.add_argument('--rules',type=Path,required=True);p.add_argument('--rules-sha',required=True)
    p.add_argument('--driver-sha',required=True);p.add_argument('--finish-source-sha',required=True)
    p.add_argument('--original-run',type=int,required=True);p.add_argument('--original-attempt',type=int,default=1)
    p.add_argument('--prepared',type=Path,required=True);p.add_argument('--previous-artifacts',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True);p.add_argument('--artifact-dir',type=Path,required=True)
    p.add_argument('--compute-minutes',type=int,default=310);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if digest(__file__)!=a.finish_source_sha:raise ValueError('the requested complete-mean adapter changed')
    a.kind='body';a.mode='finish-body';a.first=0;a.end=7721;a.recovery_manifest=None;a.recovery_sha=None
    worker=CompleteMeanWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
