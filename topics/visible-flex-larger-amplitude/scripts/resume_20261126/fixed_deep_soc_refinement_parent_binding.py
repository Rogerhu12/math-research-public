#!/usr/bin/env python3
"""Exact parent source binding for the independent complete fine+SOC solver.

The complete coarse SOC and current fine SOC bodies are reconstructed by
their exact byte-bound derivers. Literal known ray parents remain explicit
separate source/schema entries. No report or canonical model is relabelled.
This stdlib-only helper evaluates no field, derivative, or scalar integral.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys


BASE_SCHEMA='complete-fixed-deep-scalar-with-held-amplitude-budgets-v1'
BASE_SOURCE=('fullclosed_deep_scalar_amplitude_qp.py',
    'd3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95')
OLD_FINE_SCHEMA='complete-refined-fixed-deep-scalar-with-held-amplitude-budgets-v1'
OLD_FINE_SOURCE=('fullclosed_refined_deep_scalar_amplitude_qp.py',
    '1745cfae02b7ad0335577a340cfee52f179e1f27508c8d20ef1487abec00f154')
RAY_FINE_SCHEMA='complete-refined-fixed-deep-scalar-with-held-amplitude-budgets-soc-parent-v1'
RAY_FINE_SOURCE=('fullclosed_refined_deep_scalar_amplitude_qp_soc_parent.py',
    'a616e88c1f1bd256d298f167f05f0030488a7842ca4af42d53ba3f41d70dff85')
COARSE_SOC_SCHEMA='complete-fixed-deep-scalar-amplitude-separated-SOC-v1'
COARSE_SOC_SOURCE=('fullclosed_deep_amplitude_separation_soc.py',
    '329ebd1828e12d18fcf89137ee0370b7ebafbb61644bbf7bc97cb0b26b284f90')
COARSE_DERIVER_SOURCE=('derive_deep_amplitude_separation_soc.py',
    'd80f9af278b89796d64cebf708080499cd44e3a8cde089be1009b7c26e2105ec')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_bound(name,path,expected):
    path=Path(path)
    if sha(path)!=expected:raise ValueError('Changed complete fixed-scalar parent source '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def bind_parent(report,repo,*,current_fine_schema,current_fine_source,current_fine_sha256,
                current_fine_deriver,current_fine_deriver_sha256):
    """The whole-bound caller supplies its own source, never a report code path.

    Passing the current deriver explicitly avoids a hash dependency cycle:
    that deriver itself binds THIS helper's fixed SHA. All runtime callers
    have already bound their complete current source/deriver bytes. A current
    fine parent still undergoes its full body reconstruction here.
    """
    source=Path(repo)/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    known={BASE_SCHEMA:BASE_SOURCE,OLD_FINE_SCHEMA:OLD_FINE_SOURCE,
        RAY_FINE_SCHEMA:RAY_FINE_SOURCE,COARSE_SOC_SCHEMA:COARSE_SOC_SOURCE}
    if current_fine_schema in known:
        raise ValueError('The complete fine+SOC continuation needs a distinct schema')
    allowed={key:(source/name,digest) for key,(name,digest) in known.items()}
    allowed[current_fine_schema]=(Path(current_fine_source),current_fine_sha256)
    if report.get('complete') is not True or report.get('schema') not in allowed:
        raise ValueError('Use one complete source-bound actual fixed-deep-scalar parent')
    path,expected=allowed[report['schema']]
    if report.get('source_sha256')!=expected or sha(path)!=expected:
        raise ValueError('The literal parent schema, full body and report bytes disagree')
    whole_binding=None
    if report['schema']==COARSE_SOC_SCHEMA:
        module=load_bound('_complete_coarse_deep_SOC_parent_binding',
            source/COARSE_DERIVER_SOURCE[0],COARSE_DERIVER_SOURCE[1])
        whole_binding=module.bind_report(report,path,repo,base_source=source/BASE_SOURCE[0])
    elif report['schema']==current_fine_schema:
        module=load_bound('_complete_current_fine_deep_SOC_parent_binding',
            current_fine_deriver,current_fine_deriver_sha256)
        if module.REPORT_SCHEMA!=current_fine_schema:
            raise ValueError('The current fine deriver binds another exact report type')
        whole_binding=module.bind_report(report,path,repo,base_source=source/RAY_FINE_SOURCE[0])
    return dict(schema='actual-complete-fine-deep-SOC-parent-source-binding-v1',
        binding_source_sha256=sha(__file__),actual_parent_schema=report['schema'],
        actual_parent_source_repository_relative_path=
            'topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+path.name,
        actual_parent_source_sha256=expected,actual_parent_complete_SOC_binding=whole_binding,
        actual_parent_implements_complete_SOC=whole_binding is not None,
        current_fine_solver_implements_complete_SOC=True,
        source_only_no_parent_field_or_J_calls=True,
        same_numerical_SOC_parameters_still_checked_by_caller=True,
        fixed_g_refinement_convergence_claimed=False)
