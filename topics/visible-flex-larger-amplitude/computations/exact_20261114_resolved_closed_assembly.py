#!/usr/bin/env python3
"""Closed finite map using a newly solved same-H tail and the original prefix.

The old prefix is not asserted to satisfy the refined DN boundary operator.
Its original complete cut jet remains the target of the same width-.01
Cartesian patch. Source geometry, phase, mean, markers, cap and collar rules
are unchanged. The display-grid correction is inherited without editing it.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out;spec.loader.exec_module(out)
    return out


def main():
    own_hash=sha(__file__)
    original=HERE/'exact_20261114_refined_closed_assembly.py'
    display_path=HERE/'exact_20261114_closed_display_adapter.py'
    hashes={str(p):sha(p) for p in (original,display_path)}
    base=load_module('exact_resolved_closed_base',original)
    display=load_module('exact_resolved_closed_display',display_path)
    original_load,original_write=base.load,base.write
    binding=None
    def load(args):
        nonlocal binding
        saved,tail,config=original_load(args)
        binding=tail.meta.get('refinement_binding')
        if binding is None:
            raise ValueError('This entry requires the newly solved same-H readout')
        for flag in ('all_physical_parameters_equal','all_complete_H_equal','actual_newton_converged','DN_jacobian_present'):
            if binding.get(flag) is not True:
                raise ValueError('Incomplete same-H refinement binding '+flag)
        actual=args.checkpoint.parent/Path(saved.rec['actual_tail']['final_response']).name
        if binding['baseline_response_sha256']!=sha(actual) or binding['config_sha256']!=sha(args.config):
            raise ValueError('New tail does not refine this actual prefix/H/config')
        if binding['original_endpoint_nonmean_jets_reused'] or not binding['residual']<binding['original_tolerance']:
            raise ValueError('The finite refined shooting solve is incomplete')
        return saved,tail,config
    def write(path,obj):
        if isinstance(obj,dict):
            obj['fixed_H_tail_refinement']=dict(source_sha256_at_start=own_hash,
                original_sources_sha256_at_start=hashes,binding=binding,
                accepted_prefix_resolved=False,original_prefix_complete_cut_jet_retained=True,
                definition='Finite tail re-solved at exactly the same complete H and physical parameters. The unchanged saved prefix is attached through the original fixed-width full Cartesian jet patch; no new prefix BVP acceptance is implied.')
            obj['display_query_adapter']=dict(source_sha256_at_start=hashes[str(display_path)],
                original_assembly_sha256_at_start=hashes[str(original)],
                merged_near_equal_display_requests=display.merges,physical_function_unchanged=True,
                definition='Unchanged display-only near-equal radius correction; no source node, coefficient, field or physical parameter is moved.')
        original_write(path,obj)
    base.load=load;base.write=write;base.anchors=display.display_anchors
    base.__file__=__file__
    base.main()


if __name__=='__main__':
    main()
