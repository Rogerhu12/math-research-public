#!/usr/bin/env python3
"""Derive only the complete pure reader's ac03 background-policy correction.

No scientific module, field, J, root, array or report is executed here.
"""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path

PARENT_SHA='0d659ab94bff7fe12337cc8f1eb18263ae1623f8fb8bcbb40108e7e03ad3856f'
FRAME_SHA='ac03c43dba4c24016a79012e322d66a53b0ed155a1e5e00065e476846cc8ec33'
DRIVER_SHA='a0e27f36692d565d333b1ef5a207afa425ec0fc9a120164a0df3a3057f3dc743'
OUTPUT_SHA='cfd248e7159bb2ff19d6947c4ab4e2f5bc9673e49eac94324cc676c759dad0bf'
OUTPUT_NAME='read_so3_cached_current_pcg_soc_report_v2.py'
HEADER="# Independent pure-reader v2.  The full ac03/76b/a0e scientific sources and\n# report schema are unchanged.  Only the ac03 fixed-background policy shape\n# and the resulting pure readout schema are corrected from complete 0d659.\n"
PATCHES=(
    ("    if enabled:\n        frame = prep['frame']",
        "    if enabled:\n        # ac03 stores beta together with its explicit fixed-scale policy.\n        # The original 0d65 reader incorrectly treated this complete dict as\n        # a scalar. Validate its real shape and retain the whole object.\n        background = prep.get('fixed_background_inverse')\n        common = {'policy', 'explicit_algorithm_choice', 'value', 'value_hex',\n            'optimal_scale_claimed', 'unchanged_until_QP_returns'}\n        if (not isinstance(background, dict)\n                or not _finite(background.get('value')) or background['value'] <= 0\n                or background.get('value_hex') != float(background['value']).hex()\n                or background.get('explicit_algorithm_choice') is not True\n                or background.get('optimal_scale_claimed') is not False\n                or background.get('unchanged_until_QP_returns') is not True):\n            raise ValueError('Keep the actual positive beta and its entire fixed-for-one-QP policy')\n        if background['policy'] == 'reciprocal-current-coarse-average-Rayleigh':\n            if (set(background) != common | {'numerator', 'denominator', 'formula'}\n                    or background.get('formula') != 'trace(WT W)/trace(current compressed H)'\n                    or any(not _finite(background.get(key)) or background[key] <= 0\n                        for key in ('numerator', 'denominator'))\n                    or float(background['numerator']/background['denominator']).hex()\n                        != background['value_hex']):\n                raise ValueError('The complete current coarse-Rayleigh scale record changed')\n        elif background['policy'] == 'explicit-positive-literal-background':\n            if set(background) != common:\n                raise ValueError('Keep the complete explicitly supplied fixed scale policy')\n        else:\n            raise ValueError('The actual ac03 producer has only its two declared scale policies')\n        frame = prep['frame']"),
    ("                or prep['positive_small_factor_diagonal_min'] <= 0\n                or not _finite(prep.get('fixed_background_inverse'))\n                or prep['fixed_background_inverse'] <= 0):",
        "                or prep['positive_small_factor_diagonal_min'] <= 0):"),
    ("            fixed_background_inverse=prep['fixed_background_inverse'],\n            data_Gram_diagonal_json=",
        "            fixed_background_inverse=background,\n            fixed_background_inverse_value=background['value'],\n            fixed_background_inverse_value_hex=background['value_hex'],\n            fixed_background_inverse_policy=background['policy'],\n            complete_background_scale_policy_retained=True,\n            data_Gram_diagonal_json="),
    ("schema='actual-complete-normalized-parent-current-eight-column-PCG-SOC-readout-v1'",
        "schema='actual-complete-normalized-parent-current-eight-column-PCG-SOC-readout-v2'"),
)

def digest(value):
    return hashlib.sha256(value).hexdigest()

def derive(parent,frame,driver):
    if (digest(parent.encode())!=PARENT_SHA or digest(frame.encode())!=FRAME_SHA
            or digest(driver.encode())!=DRIVER_SHA):
        raise ValueError('Require all three complete actual original source bodies')
    text=parent
    for before,after in PATCHES:
        if text.count(before)!=1:raise ValueError('The exact pure fragment changed')
        text=text.replace(before,after)
    first='#!/usr/bin/env python3\n'
    if not text.startswith(first):raise ValueError('Keep the actual complete source header')
    text=first+HEADER+text[len(first):]
    if digest(text.encode())!=OUTPUT_SHA:
        raise ValueError('The complete independent pure output changed')
    old=ast.parse(parent);new=ast.parse(text)
    compile(text,OUTPUT_NAME,'exec')
    functions=lambda tree:{n.name:ast.dump(n,include_attributes=False)
        for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
    a,b=functions(old),functions(new)
    if set(a)!=set(b):raise ValueError('Do not add or omit original pure functions')
    changed={name for name in a if a[name]!=b[name]}
    if changed!={'current_metric_preconditioner','read_report'}:
        raise ValueError('Only the actual policy reader and output schema may change')
    declarations=lambda tree:[ast.dump(n,include_attributes=False) for n in tree.body
        if not isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))]
    if declarations(old)!=declarations(new):
        raise ValueError('All old complete source/schema bindings and imports must remain')
    for n in ast.walk(new):
        if isinstance(n,ast.Dict):
            keys=[k.value for k in n.keys if isinstance(k,ast.Constant) and isinstance(k.value,str)]
            if len(keys)!=len(set(keys)):raise ValueError('Duplicate literal key')
        if isinstance(n,ast.Call):
            keys=[k.arg for k in n.keywords if k.arg is not None]
            if len(keys)!=len(set(keys)):raise ValueError('Duplicate keyword')
    return text,dict(parent_pure_reader_sha256=PARENT_SHA,
        actual_scientific_driver_sha256=DRIVER_SHA,actual_frame_producer_sha256=FRAME_SHA,
        full_output_sha256=OUTPUT_SHA,full_output_bytes=len(text.encode()),
        changed_original_pure_functions=sorted(changed),
        unchanged_original_pure_functions=len(a)-len(changed),
        scientific_source_bodies_changed=False,scientific_execution=False)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--verify-existing',action='store_true')
    a=p.parse_args();topic=a.repo.resolve()/'topics/visible-flex-larger-amplitude'
    directory=topic/'scripts/resume_20261126'
    parent=(directory/'read_so3_cached_current_pcg_soc_report.py').read_text()
    frame=(directory/'so3_current_eight_column_preconditioner.py').read_text()
    driver=(directory/'fullclosed_so3_cached_current_pcg_soc.py').read_text()
    result,record=derive(parent,frame,driver)
    output=a.outdir/OUTPUT_NAME
    if a.verify_existing:
        if output.read_text()!=result:raise ValueError('The complete saved reader differs')
    else:
        a.outdir.mkdir(parents=True,exist_ok=True)
        output.write_text(result)
        (a.outdir/'current-pcg-pure-v2.diff').write_text(''.join(difflib.unified_diff(
            parent.splitlines(True),result.splitlines(True),fromfile='complete-original-0d65.py',
            tofile=OUTPUT_NAME)))
        (a.outdir/'current-pcg-pure-v2-source.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True))

if __name__=='__main__':
    main()
