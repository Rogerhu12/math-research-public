#!/usr/bin/env python3
"""Audit and preserve the v7 checkpoint-only inherited nu-description error.

The runtime parameter has always been metadata['nu']; the final v7 candidate
and report recompute its exact binary rational.  Only accepted checkpoints
inherited the warm-start exact_float_nu string.  v8 refreshes this description
and the checkpoint mean-boundary description without changing the execution.
"""
from __future__ import annotations
import argparse,ast,gzip,hashlib,io,json
from fractions import Fraction
from pathlib import Path
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint',type=Path,nargs='+',default=[
        Path('notes/2026-11-13-R133-m128-accepted-v7-b8-000.npz.gz'),
        Path('notes/2026-11-13-R133-m128-accepted-bounded-v7-b4-000.npz.gz'),
        Path('notes/2026-11-13-R133-m128-accepted-bounded-v7-b4-001.npz.gz')])
    ap.add_argument('--final-index',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-candidate.json'))
    ap.add_argument('--final-report',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-floating.json'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('preserve prior checkpoint audits')
    old=Path(__file__).with_name('fourfold_codazzi_compact_metric_branch_refine_v7_probe.py')
    new=old.with_name('fourfold_codazzi_compact_metric_branch_refine_v8_probe.py')
    old_ast=ast.parse(old.read_text());new_ast=ast.parse(new.read_text())
    changes=[]
    class UndoMetadataFix(ast.NodeTransformer):
        def visit_FunctionDef(self,node):
            if node.name=='checkpoint':
                for statement in node.body:
                    if (isinstance(statement,ast.Assign) and isinstance(statement.value,ast.Call)
                        and any(isinstance(t,ast.Name) and t.id=='metadata' for t in statement.targets)):
                        before=statement.value.keywords
                        changed=[x.arg for x in before if x.arg in ('exact_float_nu','exact_float_amplitude','mean_boundary')]
                        if set(changed)!={'exact_float_nu','exact_float_amplitude','mean_boundary'}:
                            raise ValueError('the checkpoint fix no longer has its specified scope')
                        changes.extend(changed)
                        statement.value.keywords=[x for x in before if x.arg not in changed]
            return self.generic_visit(node)
        def visit_Constant(self,node):
            a='floating_refined_compact_metric_normalized_Codazzi_branch_v8_full_FFT_matrix_free_preconditioned_Newton'
            if node.value==a:
                changes.append('final_diagnostic_kind')
                return ast.Constant(value=a.replace('_v8_','_v7_'))
            return node
    restored=UndoMetadataFix().visit(new_ast)
    same=ast.dump(restored,include_attributes=False)==ast.dump(old_ast,include_attributes=False)
    if not same:raise ValueError('v8 contains changes beyond the four declared metadata fields')
    rows=[]
    for path in args.checkpoint:
        raw=path.read_bytes();payload=gzip.decompress(raw) if path.suffix=='.gz' else raw
        data=np.load(io.BytesIO(payload),allow_pickle=False);meta=json.loads(str(data['metadata']))
        if meta['kind']!='complete_accepted_Newton_nodal_checkpoint':raise ValueError('not an accepted complete checkpoint')
        r,y,yr=(data[k] for k in ('radial_nodes','state','radial_derivative'))
        if len(r)!=y.shape[1] or y.shape!=yr.shape or y.shape[0]!=2*int(meta['modes'])+1:
            raise ValueError('complete state or derivative dimensions changed')
        if not np.all(np.isfinite(y)) or not np.all(np.isfinite(yr)) or not np.all(np.diff(r)>0):
            raise ValueError('invalid complete accepted state')
        correct=str(Fraction.from_float(float(meta['nu'])))
        rows.append(dict(path=str(path),sha256=sha(path),payload_sha256=hashlib.sha256(payload).hexdigest(),
            amplitude=meta['amplitude'],runtime_nu=meta['nu'],correct_exact_float_nu=correct,
            inherited_exact_float_nu=meta.get('exact_float_nu'),inherited_description_matches_runtime=(meta.get('exact_float_nu')==correct),
            nodes=len(r),state_shape=list(y.shape),complete_state_and_radial_derivative_retained=True,
            checkpoint_bytes_unchanged=True))
    index=json.loads(args.final_index.read_text());report=json.loads(args.final_report.read_text())
    identity=[]
    for label,doc in (('final_candidate_index',index['metadata']),('final_report',report)):
        correct=str(Fraction.from_float(float(doc['nu'])))
        if correct!=doc['exact_float_nu']:raise ValueError('a final identity is inconsistent')
        identity.append(dict(kind=label,nu=doc['nu'],exact_float_nu=correct,identity_matches=True))
    out=dict(kind='v7_inherited_checkpoint_parameter_description_audit_v1',source_sha256=sha(__file__),
        v7_source_sha256=sha(old),v8_source_sha256=sha(new),v8_executable_AST_equal_after_only_declared_metadata_reversal=same,
        changed_description_fields=changes,checkpoint_rows=rows,final_identity_rows=identity,
        final_inputs={str(p):sha(p) for p in (args.final_index,args.final_report)},
        stored_checkpoint_arrays_or_previous_artifacts_modified=False,
        execution_parameter_field='nu',resume_exact_fraction_field_used_by_v7=False,
        mathematical_conclusions_changed=False,
        conclusion='Accepted v7 checkpoints retain correct runtime doubles and complete arrays; exact_float_nu can be inherited and stale. Final v7 candidate/report identities are correctly recomputed. v8 only refreshes checkpoint descriptions and its diagnostic kind.')
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(dict(checkpoints=len(rows),stale=sum(not x['inherited_description_matches_runtime'] for x in rows),
        final_identities_correct=True,only_metadata_changed=same,output_sha256=sha(args.out)),flush=True)


if __name__=='__main__':main()
