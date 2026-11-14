#!/usr/bin/env python3
"""Closed assembly of the explicitly selected target-metric rr finite tail.

The original source background, complete raw states, prefix, phase, fixed
width-.01 cut patch and inner zero-two-jet collar remain. Plan/render source
identity is this adapter, so an old default plan is not silently reused.
"""
import math
from pathlib import Path
import exact_20261114_resolved_closed_assembly as resolved
from exact_20261114_source_knot_rr_probe import TargetMetricTail


def main():
    here=Path(__file__).resolve().parent
    hashes={str(p):resolved.sha(p)for p in [Path(__file__),Path(resolved.__file__),here/'exact_20261114_source_knot_rr_probe.py']}
    original_loader=resolved.load_module;last_tail=None
    def load_module(name,path):
        nonlocal last_tail
        module=original_loader(name,path)
        if name=='exact_resolved_closed_base':
            module.RefinedTail=TargetMetricTail
            load0,write0=module.load,module.write
            def load(args):
                nonlocal last_tail
                saved,tail,config=load0(args);last_tail=tail;return saved,tail,config
            def write(path,obj):
                if isinstance(obj,dict):
                    diagnostics=None if last_tail is None else {k:v if math.isfinite(v)else None for k,v in last_tail.diag.items()}
                    obj['target_metric_rr']=dict(source_sha256_at_start=hashes,
                        rule='Gauss-Weingarten node completion with original g and actual cardinal Ftheta.',
                        diagnostics=diagnostics,selected_for_this_finite_output=True,
                        previous_default_closed_outputs_unchanged=True,
                        scope='Explicit finite interpolation choice; no exact nonlinear or infinite-tail assertion.')
                write0(path,obj)
            module.load=load;module.write=write
        return module
    resolved.load_module=load_module
    # The inner entry already uses its __file__ as the plan/render identity.
    # Give this genuinely different field its own identity as well.
    original_file=resolved.__file__;resolved.__file__=__file__
    try:resolved.main()
    finally:resolved.load_module=original_loader;resolved.__file__=original_file


if __name__=='__main__':main()
