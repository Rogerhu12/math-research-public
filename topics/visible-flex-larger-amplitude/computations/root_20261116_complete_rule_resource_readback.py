#!/usr/bin/env python3
"""R499: complete original rule/resource selection in explicit semantic tables.

Source-only metadata reader for the named public repository Actions.
No scientific module is executed and no scientific value is recomputed.
Original selection, errors, owner observation, one-body limit and marker remain.
Author: ChatGPT /root (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path

REPOSITORY="Rogerhu12/math-research-public"
SOURCE_NAME="root_20261116_complete_rule_resource_readback.py"
SCHEMA="R499-complete-original-rule-resource-tabular-readback-v1"
ORIGINAL_SCHEMA="request205-necessary-rule-resource-readback-v1"
ROOT_README="README.md"
TOPIC_README="topics/visible-flex-larger-amplitude/README.md"
README_SCHEMAS={
    "current576-rules-sync-attempt-v1",
    "current576-rules-sync-completed-v1",
}
IDENTITY_COLUMNS=["file","bytes","sha256"]
FILE_COLUMNS={
    "json":["file","identity","necessary_original_metadata"],
    "json_readme":["file","identity","README_blobs_set",
                   "necessary_original_metadata_without_README_blobs"],
    "text":["file","identity","lines","selected_error_text"],
    "literal":["original_row"],
}
RESOURCE_COLUMNS={
    "resource":["file","identity","necessary_original_values"],
    "literal":["original_row"],
}
JSON_KEYS={"file","identity","necessary_original_metadata",
           "full_member_tree_not_exported"}
TEXT_KEYS={"file","identity","lines","selected_error_text",
           "complete_original_text_not_exported"}
RESOURCE_KEYS={"file","identity","necessary_original_values",
               "complete_original_parameter_source_tree_not_exported"}


def canonical_utf8(value):
    # A lone surrogate, if any survives the original selector, is emitted as a
    # JSON Unicode escape. Ordinary scalar Unicode uses its actual UTF-8 bytes.
    # Number formatting/options and the single final LF remain the originals.
    text=json.dumps(value,ensure_ascii=False,sort_keys=True,
                    separators=(",",":"),allow_nan=False)+"\n"
    return text.encode("utf-8",errors="backslashreplace")


def _hex_word(value,n):
    return (type(value) is str and len(value)==n
            and all(c in "0123456789abcdef" for c in value))


def _identity_row(value):
    if (type(value) is dict and set(value)==set(IDENTITY_COLUMNS)
            and type(value["file"]) is str
            and type(value["bytes"]) is int and value["bytes"]>=0
            and _hex_word(value["sha256"],64)):
        return [value[k] for k in IDENTITY_COLUMNS]
    return None


def tabulate_rule_resource_summary(original,source_binding,original_identity):
    """Change only explicitly named outer containers and duplicate README sets.

    Ineligible/unfamiliar rows are kept as complete literal selected rows.
    No value is inferred from its path or hash. Lists preserve their order.
    The original selected object is not mutated.
    """
    if original.get("schema")!=ORIGINAL_SCHEMA:
        raise ValueError("Use the actual original rule/resource summary")
    out=dict(original)
    file_rows=[]
    resource_rows=[]
    readme_sets=[]
    readme_index={}
    used_json=used_text=used_resource=used_readme=0

    for row in original["files"]:
        ident=_identity_row(row.get("identity")) if type(row) is dict else None
        if (type(row) is dict and set(row)==JSON_KEYS and ident is not None
                and row["full_member_tree_not_exported"] is True):
            meta=row["necessary_original_metadata"]
            maps=meta.get("README_blobs") if type(meta) is dict else None
            eligible=(type(meta) is dict and type(meta.get("schema")) is str
                and meta.get("schema") in README_SCHEMAS
                and type(maps) is dict and set(maps)=={ROOT_README,TOPIC_README}
                and _hex_word(maps[ROOT_README],40)
                and _hex_word(maps[TOPIC_README],40))
            if eligible:
                key=(maps[ROOT_README],maps[TOPIC_README])
                if key not in readme_index:
                    readme_index[key]=len(readme_sets)
                    readme_sets.append(dict(maps))
                rest=dict(meta)
                del rest["README_blobs"]
                file_rows.append(["json_readme",row["file"],ident,
                                  readme_index[key],rest])
                used_readme+=1
            else:
                file_rows.append(["json",row["file"],ident,meta])
            used_json+=1
        elif (type(row) is dict and set(row)==TEXT_KEYS and ident is not None
                and row["complete_original_text_not_exported"] is True):
            file_rows.append(["text",row["file"],ident,row["lines"],
                              row["selected_error_text"]])
            used_text+=1
        else:
            file_rows.append(["literal",row])

    for row in original["resources"]:
        ident=_identity_row(row.get("identity")) if type(row) is dict else None
        if (type(row) is dict and set(row)==RESOURCE_KEYS and ident is not None
                and row["complete_original_parameter_source_tree_not_exported"] is True):
            resource_rows.append(["resource",row["file"],ident,
                                  row["necessary_original_values"]])
            used_resource+=1
        else:
            resource_rows.append(["literal",row])

    del out["files"]
    del out["resources"]
    out["schema"]=SCHEMA
    out["rule_files_table"]=file_rows
    out["resource_files_table"]=resource_rows
    out["representation"]=dict(
        kind="explicit-fixed-semantic-columns",
        original_schema=ORIGINAL_SCHEMA,
        identity_columns=list(IDENTITY_COLUMNS),
        file_columns=deepcopy(FILE_COLUMNS),
        resource_columns=deepcopy(RESOURCE_COLUMNS),
        omitted_true_field_by_row_kind={
            "json":"full_member_tree_not_exported",
            "json_readme":"full_member_tree_not_exported",
            "text":"complete_original_text_not_exported",
            "resource":"complete_original_parameter_source_tree_not_exported"},
        README_blobs_sets=readme_sets,
        original_selected_ascii_identity=dict(original_identity),
        actual_source_binding=deepcopy(source_binding),
        counts=dict(json_rows=used_json,text_rows=used_text,
                    resource_rows=used_resource,readme_context_uses=used_readme),
        original_row_order_values_null_negative_zero_and_errors_retained=True,
        original_owner_and_complete_necessary_scope_not_recomputed=True,
        no_new_member_omission_and_no_extra_scientific_gate=True,
        no_original_body_or_lost_prior_run_recovered=True)
    return out


def expand_rule_resource_summary(value):
    """Explicit inverse for the normal R499 representation; not a runtime gate.

    This helper is not called by the writer and does not read any raw file.
    It documents the complete meaning of every table field for later readers.
    """
    if value.get("schema")!=SCHEMA:
        raise ValueError("Use the explicit R499 necessary representation")
    rep=value["representation"]
    if (rep["identity_columns"]!=IDENTITY_COLUMNS
            or rep["file_columns"]!=FILE_COLUMNS
            or rep["resource_columns"]!=RESOURCE_COLUMNS):
        raise ValueError("Different semantic columns")
    result={k:deepcopy(v) for k,v in value.items()
            if k not in {"representation","rule_files_table","resource_files_table"}}
    result["schema"]=rep["original_schema"]
    files=[]
    for row in value["rule_files_table"]:
        kind=row[0]
        if kind=="literal":
            files.append(deepcopy(row[1]))
        elif kind in {"json","json_readme"}:
            if kind=="json_readme":
                meta=deepcopy(row[4])
                meta["README_blobs"]=deepcopy(rep["README_blobs_sets"][row[3]])
            else:
                meta=deepcopy(row[3])
            files.append(dict(file=row[1],identity=dict(zip(IDENTITY_COLUMNS,row[2])),
                necessary_original_metadata=meta,full_member_tree_not_exported=True))
        elif kind=="text":
            files.append(dict(file=row[1],identity=dict(zip(IDENTITY_COLUMNS,row[2])),
                lines=row[3],selected_error_text=deepcopy(row[4]),
                complete_original_text_not_exported=True))
        else:
            raise ValueError("Unknown rule file row kind")
    resources=[]
    for row in value["resource_files_table"]:
        if row[0]=="literal":
            resources.append(deepcopy(row[1]))
        elif row[0]=="resource":
            resources.append(dict(file=row[1],identity=dict(zip(IDENTITY_COLUMNS,row[2])),
                necessary_original_values=deepcopy(row[3]),
                complete_original_parameter_source_tree_not_exported=True))
        else:
            raise ValueError("Unknown resource row kind")
    result["files"]=files
    result["resources"]=resources
    return result


def main(argv=None):
    import hashlib,importlib.util,json,os,runpy,sys
    from pathlib import Path
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Read actual rule/resource metadata in this public repository Actions")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-sha256",required=True)
    args=parser.parse_args(argv)
    actual=Path(__file__).resolve()
    comp=Path(os.environ["VISIBLE_COMPUTATIONS"]).resolve()
    if actual.name!=SOURCE_NAME or actual.parent!=comp:
        raise ValueError("Use the explicit current computations source")
    source_bytes=actual.read_bytes()
    source_sha256=hashlib.sha256(source_bytes).hexdigest()
    if source_sha256!=args.source_sha256:
        raise ValueError("Actual complete R499 reader source differs from the caller pin")
    source_binding=dict(
        actual_source=dict(file=actual.name,bytes=len(source_bytes),sha256=source_sha256),
        ancestor_inline_rules_block=dict(bytes=6000,
            sha256="600b0723b03546f416daffa40a9d9e55b3cb9c7a54dc93ee5f70184d0174b6c5"),
        unchanged_actual_original_metadata_reader=dict(
            file="root_20261115_current_C_pruefer_positive_full453_necessary_readout.py",
            bytes=51108,sha256="34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9"),
        actual_repository=os.environ["GITHUB_REPOSITORY"],
        actual_run_id=os.environ["GITHUB_RUN_ID"],
        actual_source_commit=os.environ["GITHUB_SHA"])
    comp=Path(os.environ['VISIBLE_COMPUTATIONS']);base=Path(os.environ['VISIBLE_BASE'])
    name='root_20261115_current_C_pruefer_positive_full453_necessary_readout.py';raw=(comp/name).read_bytes()
    assert len(raw)==51108 and hashlib.sha256(raw).hexdigest()=='34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9'
    spec=importlib.util.spec_from_file_location('_request205_necessary_metadata_readback',comp/name)
    R=importlib.util.module_from_spec(spec);sys.modules[spec.name]=R;spec.loader.exec_module(R)
    owner=base/'request205_owned_process.py'
    assert hashlib.sha256(owner.read_bytes()).hexdigest()=='f779c6a296b8579469dffb27c46642d5d5aaffc08d53a027537d2ddb23ee9357'
    owned=runpy.run_path(str(owner),run_name='_request205_rule_readback_owner')
    observed=owned['observe']()
    launch=base/'BVP-launch'
    if launch.exists():
      try:
        if not launch.is_dir() or launch.is_symlink():raise ValueError('Owned BVP output is not its original directory')
        value=json.loads((launch/'result.json').read_bytes())
        if (value.get('run_id')!=os.environ['GITHUB_RUN_ID']
            or value.get('source_commit')!=os.environ['GITHUB_SHA']):
          raise ValueError('Owned BVP result does not bind this run and source')
        if value.get('owned_group_quiescent_before_readback') is not True:
          observed['unknown_owner_scopes'].append(dict(role='BVP-child',reason='Actual independent BVP group has no observed stopped receipt'))
      except Exception as error:
        observed['unknown_owner_scopes'].append(dict(role='BVP-child',
          reason='Owned BVP output exists without a complete launch-return identity',original_error=repr(error)))
    observed['quiescent']=not observed['live_original_owned_processes'] and not observed['unknown_owner_scopes']
    (base/'rule-readback-quiescence.json').write_bytes(R.canonical(observed))
    summary=dict(schema='request205-necessary-rule-resource-readback-v1',
      repository=os.environ['GITHUB_REPOSITORY'],run_id=os.environ['GITHUB_RUN_ID'],
      source_commit=os.environ['GITHUB_SHA'],owner_observation=observed,
      no_scientific_module_imported_or_scientific_value_recomputed=True,
      resource_and_rule_metadata_only_not_a_new_scientific_gate=True,
      new_postsolve_rule_scope_reported_by_distinct_closed_readback=True,
      large_original_scientific_logs_not_exported=True,files=[],resources=[])
    for name in ('job-science-deadline.json','pre-BVP-readback-quiescence.json',
        'rule-readback-quiescence.json','BVP-template-recipe.json','current-BVP-deadline.json',
        'construction/candidate-preparation/actual202-projected-accurate-ten-model-recipe.json',
        'candidate-binding-procedure-result.json','actual202-ten-BVP-input/adapter-result.json',
        'actual202-ten-BVP-input/actual202-accurate-ten-full453-frozen450-recipe.json',
        'actual202-ten-BVP-input/result.json','current-C-BVP-client-config.json','dispatch-request.json'):
      path=base/name
      if path.is_file():
        value,ident=R.document(path,'resource/'+name)
        chosen=R.small(value) if name in ('job-science-deadline.json','current-BVP-deadline.json') else R.select(value,
          ('schema','request_number','lambda_target','state_dimension','active_parameter_indices',
           'frozen_parameter_indices','initial_ten_parameters','second_state_dimension','quiescent'))
        summary['resources'].append(dict(file=name,identity=ident,necessary_original_values=chosen,
          complete_original_parameter_source_tree_not_exported=True))
    if observed['quiescent']:
      for path in sorted(base.glob('*rule-sync*')):
        if path.name=='postsolve-rule-sync':continue
        if not path.is_dir() or path.is_symlink():continue
        for item in sorted(path.rglob('*')):
          if item.is_symlink():
            R.fail('rule-file',ValueError('Owned symlink not followed'),path=str(item.relative_to(base)))
            continue
          if not item.is_file():continue
          name=str(item.relative_to(base))
          if item.name.endswith('.json'):
            value,ident=R.document(item,'rule/'+name)
            summary['files'].append(dict(file=name,identity=ident,
              necessary_original_metadata=R.small(value),full_member_tree_not_exported=True))
          else:
            logged=R.log_view(item,'rule/'+name)
            summary['files'].append(dict(file=name,identity=logged['original_file'],
              lines=logged['complete_lines'],
              selected_error_text=logged if logged['original_error_matched_lines'] else None,
              complete_original_text_not_exported=True))
    else:
      R.fail('rule-owner',RuntimeError('Original mutable rule/scientific scopes are live or unknown'))
    summary['original_read_errors']=R.ERRORS
    summary['omitted_metadata_member_count']=len(R.OMISSIONS)
    summary['omitted_metadata_member_index_sha256']=R.sha(R.canonical(R.OMISSIONS))
    summary['complete_necessary_scope']=bool(observed['quiescent'] and not R.ERRORS)
    original_selected=R.canonical(summary)
    summary=tabulate_rule_resource_summary(summary,source_binding,
        dict(bytes=len(original_selected),sha256=R.sha(original_selected)))
    packed=canonical_utf8(summary)
    if len(packed)>90000:
      print(json.dumps(dict(event='request205_necessary_rule_summary_over_budget',
        bytes=len(packed),sha256=R.sha(packed),no_part_transport=True,no_cleanup_marker=True,
        complete_scientific_result_not_inferred=True)),flush=True)
      raise SystemExit(70)
    print('BEGIN_REQUEST205_NECESSARY_RULE_RESOURCE_SUMMARY')
    print(packed.decode('utf-8'),end='')
    print('END_REQUEST205_NECESSARY_RULE_RESOURCE_SUMMARY')
    print(json.dumps(dict(event='request205_necessary_rule_identity',bytes=len(packed),sha256=R.sha(packed),
      hash_scope='canonical UTF8 JSON including LF')),flush=True)
    if not summary['complete_necessary_scope']:raise SystemExit(2)
    marker=dict(schema='request205-complete-rule-resource-readback-v1',
      repository=os.environ['GITHUB_REPOSITORY'],run_id=os.environ['GITHUB_RUN_ID'],
      source_commit=os.environ['GITHUB_SHA'],complete=True,quiescent=True,
      necessary_summary=dict(bytes=len(packed),sha256=R.sha(packed)),
      large_text_omission_scope_explicit=True)
    with (base/'rule-readback-complete.json').open('xb') as stream:
      stream.write(R.canonical(marker));stream.flush();os.fsync(stream.fileno())


if __name__=="__main__":
    main()
