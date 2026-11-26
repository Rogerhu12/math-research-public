#!/usr/bin/env python3
"""Bind genuine complete fixed-deep parents without relabelling a SOC report.

Only source/report bytes are read. No field, derivative, scalar integral or
geometry fixture is evaluated. A SOC parent is reconstructed from its entire
published base and deriver before its existing target invariants are checked.
Accepting that parent does not add SOC to the subsequent fine solver.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys

BASE_SCHEMA = 'complete-fixed-deep-scalar-with-held-amplitude-budgets-v1'
BASE_SOURCE = ('fullclosed_deep_scalar_amplitude_qp.py',
    'd3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95')
OLD_FINE_SCHEMA = 'complete-refined-fixed-deep-scalar-with-held-amplitude-budgets-v1'
OLD_FINE_SOURCE = ('fullclosed_refined_deep_scalar_amplitude_qp.py',
    '1745cfae02b7ad0335577a340cfee52f179e1f27508c8d20ef1487abec00f154')
SOC_SCHEMA = 'complete-fixed-deep-scalar-amplitude-separated-SOC-v1'
SOC_SOURCE = ('fullclosed_deep_amplitude_separation_soc.py',
    '329ebd1828e12d18fcf89137ee0370b7ebafbb61644bbf7bc97cb0b26b284f90')
DERIVER_SOURCE = ('derive_deep_amplitude_separation_soc.py',
    'd80f9af278b89796d64cebf708080499cd44e3a8cde089be1009b7c26e2105ec')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_bound(name, path, expected):
    path = Path(path)
    if sha(path) != expected:
        raise ValueError('Changed complete parent source: '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def bind_parent(report, repo, *, current_fine_schema, current_fine_source,
        current_fine_sha256):
    """Bind one actual completed parent to a closed, exact source list.

    The caller binds its own complete fine source before passing that identity;
    the actual source is read again here. No arbitrary schema/path from report
    metadata is executed. Every remaining same-target/measure/carrier check is
    still performed by the original fine driver, launcher or coordinator.
    """
    source = Path(repo)/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    current_fine_source = Path(current_fine_source)
    if current_fine_schema in (BASE_SCHEMA, OLD_FINE_SCHEMA, SOC_SCHEMA):
        raise ValueError('The independent fine continuation needs its own schema')
    allowed = {
        BASE_SCHEMA: (source/BASE_SOURCE[0], BASE_SOURCE[1]),
        OLD_FINE_SCHEMA: (source/OLD_FINE_SOURCE[0], OLD_FINE_SOURCE[1]),
        SOC_SCHEMA: (source/SOC_SOURCE[0], SOC_SOURCE[1]),
        current_fine_schema: (current_fine_source, current_fine_sha256),
    }
    if report.get('complete') is not True or report.get('schema') not in allowed:
        raise ValueError('Use a complete actual fixed-deep scalar parent')
    path, expected = allowed[report['schema']]
    if report.get('source_sha256') != expected or sha(path) != expected:
        raise ValueError('The parent schema, report and full source bytes disagree')
    whole_soc_binding = None
    if report['schema'] == SOC_SCHEMA:
        module = load_bound('_whole_deep_SOC_parent_body_binding',
            source/DERIVER_SOURCE[0], DERIVER_SOURCE[1])
        whole_soc_binding = module.bind_report(report, path, repo,
            base_source=source/BASE_SOURCE[0])
    return dict(schema='actual-fixed-deep-refinement-parent-source-binding-v1',
        binding_source_sha256=sha(__file__), actual_parent_schema=report['schema'],
        actual_parent_source_repository_relative_path=
            'topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+path.name,
        actual_parent_source_sha256=expected,
        actual_parent_complete_SOC_binding=whole_soc_binding,
        source_only_no_parent_field_or_J_calls=True,
        fine_globalization_unchanged=True,
        parent_SOC_algorithm_inherited_by_fine_solver=False,
        same_SOC_globalization_refinement_claimed=False)
