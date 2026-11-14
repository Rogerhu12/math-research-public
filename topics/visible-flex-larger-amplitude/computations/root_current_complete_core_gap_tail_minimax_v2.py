#!/usr/bin/env python3
"""Allow the current full-gap model to request zero loss of complete core gap.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The separately frozen complete current-field LP is unchanged except that its
gap lower-target may equal zero. Size factors and trust remain positive.
This permits a genuine current-direction search for more curvature/size
margin without reducing the full core gap. No numerical field is created.
"""
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
BASE='root_current_complete_core_gap_tail_minimax.py'
BASE_SHA='ba36c553dc141a559676429b4222b193489c90a531874428b5b577a94e0301c3'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    if sha(HERE/BASE)!=BASE_SHA:raise ValueError('The frozen current full-core-gap design source changed')
    import root_current_complete_core_gap_tail_minimax as base
    original_transform=base.transformed_module
    extra=[
        ("    if any(not np.isfinite(v) or v<=0 for v in args.q1_factors+args.size_factors+[args.trust_factor]):",
         "    if (any(not np.isfinite(v) or v<0 for v in args.q1_factors) or any(not np.isfinite(v) or v<=0 for v in args.size_factors+[args.trust_factor])):"),
        ("        raise ValueError('Finite positive trust, growth, and size factors required')",
         "        raise ValueError('Finite nonnegative full-gap requests and positive trust/size factors required')")]
    def transform(name,edits):
        if name=='root_geometry_minimax_initial_laws_controls.py':edits=[*edits,*extra]
        return original_transform(name,edits)
    original_argv=list(sys.argv)
    base.transformed_module=transform
    try:base.main()
    finally:base.transformed_module=original_transform
    flag='--prepare-source-only' if '--prepare-source-only' in original_argv else '--out'
    if original_argv.count(flag)!=1:raise ValueError('One explicit final output path is required')
    out=Path(original_argv[original_argv.index(flag)+1])
    result=json.loads(out.read_text())
    result['nondecreasing_complete_gap_request_adapter']=dict(
        source_sha256=sha(__file__),original_complete_gap_entry_sha256=BASE_SHA,
        exact_parser_edits=[dict(before=b,after=a) for b,a in extra],
        zero_complete_gap_lower_increment_allowed=True,
        negative_requested_gap_increment_allowed=False,
        original_positive_size_and_trust_requirements_preserved=True,
        geometric_rows_and_full32_gap_tail_formulas_changed=False,
        exact_reverse_included_in_original_driver_preparation=True,
        no_new_physical_gate_or_problem_completion_standard=True)
    temp=out.with_name(out.name+'.nondecreasing-gap.tmp')
    temp.write_text(json.dumps(result,indent=2)+'\n');temp.replace(out)
    print(json.dumps(dict(event='current_nondecreasing_full_gap_interface_finished',out=str(out),sha256=sha(out),source_prepare_only=(flag=='--prepare-source-only'))),flush=True)


if __name__=='__main__':main()
