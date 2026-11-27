#!/usr/bin/env python3
"""Recreate every complete analytic-J3 upper entry from immutable full sources.

This is standard-library source processing only. It neither imports generated
scientific modules nor evaluates any numerical field, root, integral or example.
The lower six bodies have their own complete locked source deriver. The packet
body is the independently source-bound complete v2 recorder, copied unchanged.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PLAN = json.loads(r'''{
  "schema": "complete-analytic-J3-packet-entry-exact-source-derivation-v1",
  "parent_public_commit": "35e4d40fd459bef32055684a1048323f96de4a33",
  "plans": [
    {
      "parent_role": "geometry",
      "parent_filename": "so3_reference_centred_independent_chart_material_envelope_geometry.py",
      "parent_sha256": "1bccece84925523a5a4a54b4ba021b119a10d4c90a693fe89565200f440fbbd3",
      "parent_bytes": 68275,
      "filename": "so3_reference_centred_analytic_j3_material_envelope_geometry.py",
      "sha256": "781778dc41303e5c8555df46e774e74e6c96fe2fa4ab3cb2bc3d4d0dccaae50a",
      "bytes": 68945,
      "edits": [
        {
          "old": "SCHEMA = 'complete-R715-adjacent-frame-material-envelope-world-geometry-and-preserved-prefix-rows-v1'",
          "new": "SCHEMA = 'complete-R715-analytic-J3-material-envelope-world-geometry-and-preserved-prefix-rows-v1'\nANALYTIC_STAGE_SOURCE_SHA256 = '64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d'",
          "count": 1
        },
        {
          "old": "OPERATOR_SCHEMA = 'complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'",
          "new": "OPERATOR_SCHEMA = 'complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'",
          "count": 1
        },
        {
          "old": "d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb",
          "new": "04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e",
          "count": 1
        },
        {
          "old": "375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59",
          "new": "5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1",
          "count": 1
        },
        {
          "old": "955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3",
          "new": "8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787",
          "count": 1
        },
        {
          "old": "ccb3340e500a032943aaed084376136fd67ad81b222e1afbcc5e79d468f21ef8",
          "new": "4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d",
          "count": 1
        },
        {
          "old": "        calibration = problem.reference_calibration",
          "new": "        local_matrix = problem.analytic_stage_jacobian\n        if (local_matrix.q is not problem\n                or local_matrix.definition != model.get('analytic_stage_jacobian')\n                or local_matrix.definition.get('source_sha256') != ANALYTIC_STAGE_SOURCE_SHA256\n                or sha(type(local_matrix).__init__.__code__.co_filename) != ANALYTIC_STAGE_SOURCE_SHA256\n                or local_matrix.model_identity != problem.identity):\n            raise ValueError('Bind the entire selected local J3 producer without changing the physical sixjets')\n        calibration = problem.reference_calibration",
          "count": 1
        }
      ]
    },
    {
      "parent_role": "transfer",
      "parent_filename": "transfer_material_envelope_memory_to_independent_chart.py",
      "parent_sha256": "182a4a5401c959c983ebd8c544bdae58c02d5df942c4491b14c89f83880f8590",
      "parent_bytes": 58387,
      "filename": "transfer_material_envelope_memory_to_analytic_j3.py",
      "sha256": "0d2a5e9c9f5651e149d53da859ac42ced1c3b44709f9a5a3416a82c8d8702608",
      "bytes": 62891,
      "edits": [
        {
          "old": "SCHEMA = 'strict-prior-envelope-transfer-or-explicit-independent-fixed-chart-branch-v1'",
          "new": "SCHEMA = 'strict-prior-envelope-transfer-or-explicit-independent-fixed-chart-analytic-J3-branch-v1'\nANALYTIC_BINDING_SOURCE_SHA256 = 'a1971fd5328032af735553a7e99fcfcd78f44e7b37ee78f666564d7e0b294680'",
          "count": 1
        },
        {
          "old": "        changed_model_fields='strict terminal transfer only: schema/source, full detached_stage_matrix_reuse, adjacent_normal_frame_matrices, and calibration source/endpoint source',",
          "new": "        changed_model_fields='strict terminal transfer only: complete source/schema, full explicitly bound C1/detached/adjacent/analytic-J3 policies, and calibration source/endpoint source',\n        complete_analytic_source_and_report_binding_sha256=ANALYTIC_BINDING_SOURCE_SHA256,",
          "count": 1
        },
        {
          "old": "def _compatible_models(old,new,current_pins):\n    if (old.get('schema') != ORIGINAL_OPERATOR_SCHEMA\n            or old.get('source_sha256') != ORIGINAL_OPERATOR_SHA256\n            or new.get('source_sha256') != current_pins['endpoint'][1]\n            or new.get('reference_centering_definition',{}).get('source_sha256')\n                != current_pins['reference_calibration'][1]\n            or new.get('reference_centering_definition',{}).get('endpoint_source_sha256')\n                != current_pins['endpoint'][1]\n            or old.get('reference_centering_definition',{}).get('source_sha256')\n                != ORIGINAL_CALIBRATION_SHA256\n            or old.get('reference_centering_definition',{}).get('endpoint_source_sha256')\n                != ORIGINAL_OPERATOR_SHA256):\n        raise ValueError('Only the explicitly declared complete old/new endpoint and calibration sources may differ')\n    before,after = copy.deepcopy(old),copy.deepcopy(new)\n    matrix = after.pop('detached_stage_matrix_reuse',None)\n    if (not isinstance(matrix,dict) or matrix.get('source_sha256') != current_pins['stage_matrices'][1]\n            or matrix.get('original_complete_C1_operator_source_sha256') != ORIGINAL_OPERATOR_SHA256\n            or matrix.get('original_stage_equations_domain_solves_and_trace_retained') is not True\n            or matrix.get('original_active_residual_and_full_upstream_parameter_chain_retained') is not True):\n        raise ValueError('A new model may add only its fully bound detached-matrix working policy')\n    adjacent=after.pop('adjacent_normal_frame_matrices',None)\n    if (not isinstance(adjacent,dict) or adjacent.get('source_sha256')!=current_pins['adjacent_matrices'][1]\n            or adjacent.get('complete_detached_matrix_source_sha256')!=current_pins['stage_matrices'][1]\n            or adjacent.get('complete_frame_C1_source_sha256')!=current_pins['frame_C1'][1]\n            or adjacent.get('complete_base_source_sha256')!=current_pins['meridian'][1]\n            or adjacent.get('all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained') is not True\n            or adjacent.get('original_active_residual_and_all_upstream_parameter_edges_retained') is not True\n            or adjacent.get('block_products_have_independent_working_rounding_definition') is not True):\n        raise ValueError('Only the explicitly bound complete adjacent-frame working producer may be added')\n    for value in (before,after):\n        for key in ('schema','source_sha256'):\n            value.pop(key)\n        calibration = value['reference_centering_definition']\n        for key in ('source_sha256','endpoint_source_sha256'):\n            calibration.pop(key)\n    if before != after:\n        raise ValueError('The full actual base/reference/profile/chart/free space/partition or other field definition changed')\n    return dict(complete_unchanged_definition_sha256=canonical(before),\n        exact_old_complete_model_identity_sha256=canonical(old),\n        exact_new_complete_model_identity_sha256=canonical(new),\n        full_base_reference_chart_profile_and_partition_equal=True,\n        only_explicit_source_schema_and_matrix_working_policy_fields_changed=True,\n        computed_float_field_equality_claimed=False)\n\n",
          "new": "def _compatible_models(old,new,current_pins):\n    path=Path(__file__).with_name('analytic_j3_source_and_report_binding.py')\n    if (sha(path)!=ANALYTIC_BINDING_SOURCE_SHA256\n            or current_pins.get('analytic_J3_binding',(None,None))[1]!=ANALYTIC_BINDING_SOURCE_SHA256):\n        raise ValueError('Bind the complete explicit new local-matrix model relation')\n    name='_complete_analytic_J3_model_relation_'+ANALYTIC_BINDING_SOURCE_SHA256\n    if name not in sys.modules:\n        spec=importlib.util.spec_from_file_location(name,path)\n        module=importlib.util.module_from_spec(spec)\n        sys.modules[name]=module\n        spec.loader.exec_module(module)\n    module=sys.modules[name]\n    if sha(module.compatible_legacy_model.__code__.co_filename)!=ANALYTIC_BINDING_SOURCE_SHA256:\n        raise ValueError('The complete model-relation function changed')\n    return module.compatible_legacy_model(old,new,current_pins,source_directory=path.parent)\n\n",
          "count": 1
        },
        {
          "old": "ANALYTIC_BINDING_SOURCE_SHA256 = 'a1971fd5328032af735553a7e99fcfcd78f44e7b37ee78f666564d7e0b294680'",
          "new": "ANALYTIC_BINDING_SOURCE_SHA256 = 'f34fcafc06b50594b7a651a90e38553ea8ae3da5b6ac8b6ca4ea691d2ab9f14f'",
          "count": 1
        },
        {
          "old": "TYPE_KEYS = ('family','location','partner','branch','sign')",
          "new": "TYPE_KEYS = ('family','location','partner','branch','sign')\nPARENT_FAMILIES = {\n    ORIGINAL_DRIVER_SHA256: dict(report_schema=ORIGINAL_REPORT_SCHEMA,\n        reader_sha256=ORIGINAL_READER_SHA256,reader_relative=ORIGINAL_READER_RELATIVE,\n        operator_sha256=ORIGINAL_OPERATOR_SHA256,operator_schema=ORIGINAL_OPERATOR_SCHEMA,\n        memory_sha256=MEMORY_SOURCE_SHA256),\n    '95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9': dict(\n        report_schema='complete-R711-reference-centred-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1',\n        reader_sha256='f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470',\n        reader_relative='scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py',\n        operator_sha256='d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb',\n        operator_schema='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',\n        memory_sha256=CURRENT_MEMORY_SOURCE_SHA256)}\n\n\ndef _parent_family(source, payload=None):\n    if source not in PARENT_FAMILIES:\n        raise ValueError('Use one complete explicitly supported original parent source')\n    family=PARENT_FAMILIES[source]\n    if payload is not None and (payload.get('source_sha256')!=source\n            or payload.get('schema')!=family['report_schema']\n            or payload.get('representation',{}).get('source_sha256')!=family['operator_sha256']\n            or payload.get('representation',{}).get('schema')!=family['operator_schema']\n            or payload.get('material_envelope',{}).get('source_sha256')!=family['memory_sha256']):\n        raise ValueError('The parent report must bind its own complete source, field and memory')\n    return family\n\n\ndef requested_parent_memory(args):\n    \"\"\"Select a complete loader only; load_memory still performs every full read.\"\"\"\n    selected=None\n    for filename in getattr(args,'material_envelope_parent_report',[]):\n        record,raw=_record_bytes(filename)\n        value=json.loads(raw)\n        memory=_parent_family(value.get('source_sha256'),value)['memory_sha256']\n        if selected is not None and selected!=memory:\n            raise ValueError('Do not mix different full material-envelope policies in one transfer')\n        selected=memory\n        _same_bytes(record)\n    return selected\n",
          "count": 1
        },
        {
          "old": "        supported_prior_calibration_sha256=ORIGINAL_CALIBRATION_SHA256,",
          "new": "        supported_prior_calibration_sha256=ORIGINAL_CALIBRATION_SHA256,\n        complete_explicit_parent_families=copy.deepcopy(PARENT_FAMILIES),\n        same_frozen_current_target_95559_final_transfer_supported=True,\n        prior_pending_parallel_obligations_preserved_as_complete_source_bound_origins=True,",
          "count": 1
        },
        {
          "old": "def _old_reader(topic):\n    path = topic/ORIGINAL_READER_RELATIVE\n    if sha(path) != ORIGINAL_READER_SHA256:\n        raise ValueError('Use the complete original corrected 104e reader')\n    name = '_complete_original_envelope_transfer_reader_'+ORIGINAL_READER_SHA256\n    spec = importlib.util.spec_from_file_location(name,path)\n    module = importlib.util.module_from_spec(spec)\n    sys.modules[name] = module\n    spec.loader.exec_module(module)\n    if sha(module.read_report.__code__.co_filename) != ORIGINAL_READER_SHA256:\n        raise ValueError('The complete original report reader body changed')\n    return module\n\n",
          "new": "def _old_reader(topic, family):\n    path=topic/family['reader_relative']\n    expected=family['reader_sha256']\n    if sha(path)!=expected:\n        raise ValueError('Use the complete actual original parent reader')\n    name='_complete_original_envelope_transfer_reader_'+expected\n    spec=importlib.util.spec_from_file_location(name,path)\n    module=importlib.util.module_from_spec(spec)\n    sys.modules[name]=module\n    spec.loader.exec_module(module)\n    if sha(module.read_report.__code__.co_filename)!=expected:\n        raise ValueError('The complete original report reader body changed')\n    return module\n\n",
          "count": 1
        },
        {
          "old": "    expected_memory=(CURRENT_MEMORY_SOURCE_SHA256 if independent else\n        restart.get('material_envelope',{}).get('source_sha256') if restart is not None else MEMORY_SOURCE_SHA256)\n    if expected_memory!=actual_memory_sha or (paths and actual_memory_sha!=MEMORY_SOURCE_SHA256):\n        raise ValueError('Keep original strict c79 transfer separate from the complete new-restorer independent input')\n\n    old_reader = _old_reader(topic) if paths else None",
          "new": "    parent_memory=requested_parent_memory(args)\n    expected_memory=(CURRENT_MEMORY_SOURCE_SHA256 if independent else\n        restart.get('material_envelope',{}).get('source_sha256') if restart is not None else parent_memory)\n    if (expected_memory!=actual_memory_sha\n            or (parent_memory is not None and parent_memory!=actual_memory_sha)):\n        raise ValueError('Select the exact complete memory of the explicitly bound parent family')\n",
          "count": 1
        },
        {
          "old": "        payload = json.loads(raw)\n        pure = old_reader.read_report(args.repo,path,verify_final_bundle=False)",
          "new": "        payload = json.loads(raw)\n        family=_parent_family(payload.get('source_sha256'),payload)\n        pure = _old_reader(topic,family).read_report(args.repo,path,verify_final_bundle=False)",
          "count": 1
        },
        {
          "old": "        if (payload.get('schema') != ORIGINAL_REPORT_SCHEMA\n                or payload.get('source_sha256') != ORIGINAL_DRIVER_SHA256\n                or payload.get('observation_carrier_sha256') != current_carrier_sha",
          "new": "        if (payload.get('observation_carrier_sha256') != current_carrier_sha",
          "count": 1
        },
        {
          "old": "            model_binding=model_binding,original_complete_reader_sha256=ORIGINAL_READER_SHA256))",
          "new": "            model_binding=model_binding,family=family,\n            original_complete_reader_sha256=family['reader_sha256']))",
          "count": 1
        },
        {
          "old": "            original_complete_reader_sha256=ORIGINAL_READER_SHA256,\n            actual_terminal_report_kind=parent['terminal'],",
          "new": "            original_complete_reader_sha256=parent['family']['reader_sha256'],\n            inherited_prior_independent_branch_origin=copy.deepcopy(\n                payload.get('material_envelope_transfer',{}).get('independent_branch_origin')),\n            actual_terminal_report_kind=parent['terminal'],",
          "count": 1
        },
        {
          "old": "'same-source-restart' if restart is not None else 'strict-terminal-transfer'),",
          "new": "'same-source-restart' if restart is not None else\n            'strict-current-target-terminal-transfer' if parent_memory==CURRENT_MEMORY_SOURCE_SHA256\n            else 'strict-terminal-transfer'),",
          "count": 1
        },
        {
          "old": "        family=_parent_family(payload.get('source_sha256'),payload)\n        pure =",
          "new": "        family=_parent_family(payload.get('source_sha256'),payload)\n        if family['memory_sha256']!=actual_memory_sha:\n            raise ValueError('The captured complete parent changed the selected memory family')\n        pure =",
          "count": 1
        },
        {
          "old": "    pure = _old_reader(topic).read_report(args.repo,report_path,verify_final_bundle=True)",
          "new": "    family=_parent_family(payload.get('source_sha256'),payload)\n    pure = _old_reader(topic,family).read_report(args.repo,report_path,verify_final_bundle=True)",
          "count": 1
        },
        {
          "old": "            or payload.get('schema') != ORIGINAL_REPORT_SCHEMA\n            or payload.get('source_sha256') != ORIGINAL_DRIVER_SHA256\n",
          "new": "",
          "count": 1
        },
        {
          "old": "        if (str(saved['schema'].item()) != ORIGINAL_OPERATOR_SCHEMA",
          "new": "        if (str(saved['schema'].item()) != family['operator_schema']",
          "count": 1
        },
        {
          "old": "        source_checkpoint=bundle_record,original_complete_reader_sha256=ORIGINAL_READER_SHA256,\n        source_driver_sha256=ORIGINAL_DRIVER_SHA256,",
          "new": "        source_checkpoint=bundle_record,original_complete_reader_sha256=family['reader_sha256'],\n        source_driver_sha256=payload['source_sha256'],",
          "count": 1
        },
        {
          "old": "    if (not requested or not isinstance(value,dict)\n",
          "new": "    family=_parent_family(value.get('source_driver_sha256')) if isinstance(value,dict) else None\n    if (not requested or not isinstance(value,dict)\n",
          "count": 1
        },
        {
          "old": "            or value.get('source_driver_sha256') != ORIGINAL_DRIVER_SHA256\n            or value.get('original_complete_reader_sha256') != ORIGINAL_READER_SHA256",
          "new": "            or value.get('original_complete_reader_sha256') != family['reader_sha256']",
          "count": 1
        },
        {
          "old": "    if mode not in ('explicit-independent-branch','same-source-restart','strict-terminal-transfer'):",
          "new": "    if mode not in ('explicit-independent-branch','same-source-restart','strict-terminal-transfer',\n            'strict-current-target-terminal-transfer'):",
          "count": 1
        },
        {
          "old": "    if branch is None and actual_memory_sha!=MEMORY_SOURCE_SHA256:\n        raise ValueError('The strict previous-terminal path retains its original complete memory source')",
          "new": "    if branch is None and actual_memory_sha==CURRENT_MEMORY_SOURCE_SHA256:\n        if not parents or any(_parent_family(p.get('actual_driver_sha256'))['memory_sha256']\n                !=CURRENT_MEMORY_SOURCE_SHA256 for p in parents):\n            raise ValueError('The current-target strict path requires its complete same-target parent lineage')",
          "count": 1
        },
        {
          "old": "        digest = _digest(report.get('sha256'))\n        if (",
          "new": "        digest = _digest(report.get('sha256'))\n        family=_parent_family(parent.get('actual_driver_sha256'))\n        if (",
          "count": 1
        },
        {
          "old": "                or parent.get('actual_driver_sha256') != ORIGINAL_DRIVER_SHA256\n                or parent.get('original_complete_reader_sha256') != ORIGINAL_READER_SHA256",
          "new": "                or parent.get('original_complete_reader_sha256') != family['reader_sha256']\n                or family['memory_sha256']!=actual_memory_sha",
          "count": 1
        },
        {
          "old": "        _digest(parent.get('actual_model_identity_sha256'))",
          "new": "        origin=parent.get('inherited_prior_independent_branch_origin')\n        if origin is not None:\n            if not isinstance(origin,dict):\n                raise ValueError('Preserve the entire prior independent origin, not a flag')\n            if family['memory_sha256']==CURRENT_MEMORY_SOURCE_SHA256:\n                if (origin.get('schema')!='explicit-independent-fixed-chart-complete-material-envelope-origin-v1'\n                        or origin.get('actual_origin_driver_sha256')!=parent['actual_driver_sha256']\n                        or origin.get('actual_origin_model_identity_sha256')!=parent['actual_model_identity_sha256']\n                        or origin.get('actual_origin_carrier_sha256')!=carrier_sha256\n                        or origin.get('later_actual_addresses_and_typed_memory_require_bound_merge') is not True\n                        or origin.get('pending_parallel_terminal_reports_read') is not False\n                        or origin.get('pending_parallel_final_or_typed_discovery_words_inherited') is not False\n                        or origin.get('unknown_typed_priority_equivalence_claimed') is not False):\n                    raise ValueError('Retain the actual parent origin and every unresolved peer obligation')\n                pending=origin.get('pending_parallel_runs')\n                if (not isinstance(pending,list) or len(pending)!=len(set(pending))\n                        or any(not isinstance(v,str) or len(v.split('/'))!=2\n                            or any(not w.isdigit() or int(w)<1 or str(int(w))!=w\n                                for w in v.split('/')) for v in pending)):\n                    raise ValueError('Do not fabricate or discard canonical unread peer identities')\n        elif family['memory_sha256']==CURRENT_MEMORY_SOURCE_SHA256:\n            raise ValueError('A 95559 parent must retain its own actual independent origin')\n        _digest(parent.get('actual_model_identity_sha256'))",
          "count": 1
        },
        {
          "old": "        elif mode!='strict-terminal-transfer' or count==0 or branch is not None:\n            raise ValueError('The original strict fresh branch retains its nonempty terminal-input requirement')",
          "new": "        elif (mode!=('strict-current-target-terminal-transfer' if actual_memory_sha==CURRENT_MEMORY_SOURCE_SHA256\n                else 'strict-terminal-transfer') or count==0 or branch is not None):\n            raise ValueError('Each strict fresh branch retains its nonempty complete terminal-input requirement')",
          "count": 1
        },
        {
          "old": "            if (source is None or origin.get('source_driver_sha256') != ORIGINAL_DRIVER_SHA256",
          "new": "            if (source is None or origin.get('source_driver_sha256') != source['actual_driver_sha256']",
          "count": 1
        },
        {
          "old": "Fresh use requires an\nactual terminal predecessor report; a future filename is not evidence.",
          "new": "A strict prior-field transfer requires an\nactual terminal predecessor report. An explicitly independent fresh entry uses\nthe complete frozen reference and declares all unknown peer obligations.",
          "count": 1
        },
        {
          "old": "        prior_pending_parallel_obligations_preserved_as_complete_source_bound_origins=True,",
          "new": "        prior_pending_parallel_obligations_preserved_as_complete_source_bound_origins=True,\n        each_current_pending_run_has_an_explicit_whole_parent_driver_source=True,",
          "count": 1
        },
        {
          "old": "    pending=list(getattr(args,'pending_parallel_envelope_run',[]))",
          "new": "    pending=list(getattr(args,'pending_parallel_envelope_run',[]))\n    pending_sources={}\n    for item in getattr(args,'pending_parallel_envelope_source',[]):\n        fields=item.split('=')\n        if (len(fields)!=2 or fields[0] in pending_sources\n                or fields[1] not in PARENT_FAMILIES):\n            raise ValueError('Each pending run must explicitly name one supported complete parent driver')\n        pending_sources[fields[0]]=fields[1]\n    if set(pending_sources)!=set(pending):\n        raise ValueError('Bind every declared unknown peer run one-to-one to its actual source family')",
          "count": 1
        },
        {
          "old": "            pending_parallel_runs=pending,pending_parallel_driver_sha256=ORIGINAL_DRIVER_SHA256,",
          "new": "            pending_parallel_runs=pending,pending_parallel_driver_sources=pending_sources,\n            pending_parallel_driver_sha256=(next(iter(set(pending_sources.values())))\n                if len(set(pending_sources.values()))==1 else None),",
          "count": 1
        },
        {
          "old": "                or branch.get('pending_parallel_driver_sha256')!=ORIGINAL_DRIVER_SHA256):",
          "new": "):",
          "count": 1
        },
        {
          "old": "        pending=branch.get('pending_parallel_runs')",
          "new": "        pending=branch.get('pending_parallel_runs')\n        pending_sources=branch.get('pending_parallel_driver_sources')\n        if (not isinstance(pending_sources,dict) or not isinstance(pending,list)\n                or set(pending_sources)!=set(pending)\n                or any(source not in PARENT_FAMILIES for source in pending_sources.values())\n                or branch.get('pending_parallel_driver_sha256')!=(next(iter(set(pending_sources.values())))\n                    if len(set(pending_sources.values()))==1 else None)):\n            raise ValueError('The complete unknown-peer source map must retain every actual declared run')",
          "count": 1
        },
        {
          "old": "                or actual_memory_sha!=CURRENT_MEMORY_SOURCE_SHA256\n):",
          "new": "                or actual_memory_sha!=CURRENT_MEMORY_SOURCE_SHA256):",
          "count": 1
        }
      ]
    },
    {
      "parent_role": "driver",
      "parent_filename": "fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py",
      "parent_sha256": "95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9",
      "parent_bytes": 75152,
      "filename": "fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py",
      "sha256": "0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51",
      "bytes": 78907,
      "edits": [
        {
          "old": "SCHEMA = 'complete-R711-reference-centred-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1'",
          "new": "SCHEMA = 'complete-R711-reference-centred-analytic-J3-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1'",
          "count": 1
        },
        {
          "old": "so3_reference_centred_independent_chart_material_envelope_geometry.py",
          "new": "so3_reference_centred_analytic_j3_material_envelope_geometry.py",
          "count": 1
        },
        {
          "old": "transfer_material_envelope_memory_to_independent_chart.py",
          "new": "transfer_material_envelope_memory_to_analytic_j3.py",
          "count": 1
        },
        {
          "old": "so3_reference_centred_adjacent_frame_smooth_triangle_normal_lift_operator.py",
          "new": "so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py",
          "count": 1
        },
        {
          "old": "reference_centred_adjacent_frame_smooth_triangle_calibration.py",
          "new": "reference_centred_analytic_j3_smooth_triangle_calibration.py",
          "count": 1
        },
        {
          "old": "normal_frame_c1_reuse.py",
          "new": "analytic_j3_normal_frame_c1_reuse.py",
          "count": 1
        },
        {
          "old": "detached_normal_stage_matrix_reuse.py",
          "new": "analytic_j3_detached_normal_stage_matrix_reuse.py",
          "count": 1
        },
        {
          "old": "adjacent_normal_frame_matrices.py",
          "new": "analytic_j3_adjacent_normal_frame_matrices.py",
          "count": 1
        },
        {
          "old": "1bccece84925523a5a4a54b4ba021b119a10d4c90a693fe89565200f440fbbd3",
          "new": "781778dc41303e5c8555df46e774e74e6c96fe2fa4ab3cb2bc3d4d0dccaae50a",
          "count": 1
        },
        {
          "old": "182a4a5401c959c983ebd8c544bdae58c02d5df942c4491b14c89f83880f8590",
          "new": "d11fd0ed7fecd47d1f9710380f6dfbd431ac9f658f6e32d9256f990f264bdc6b",
          "count": 1
        },
        {
          "old": "d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb",
          "new": "04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e",
          "count": 1
        },
        {
          "old": "ccb3340e500a032943aaed084376136fd67ad81b222e1afbcc5e79d468f21ef8",
          "new": "4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d",
          "count": 1
        },
        {
          "old": "ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9",
          "new": "8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8",
          "count": 1
        },
        {
          "old": "375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59",
          "new": "5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1",
          "count": 1
        },
        {
          "old": "955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3",
          "new": "8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787",
          "count": 1
        },
        {
          "old": "SOURCE_PINS = {",
          "new": "SOURCE_PINS = {'analytic_J3': ('scripts/resume_20261126/analytic_normal_stage_jacobian.py', '64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d'),\n 'analytic_J3_binding': ('scripts/resume_20261126/analytic_j3_source_and_report_binding.py', 'a1971fd5328032af735553a7e99fcfcd78f44e7b37ee78f666564d7e0b294680'),\n 'analytic_parent_frame_C1': ('scripts/resume_20261126/normal_frame_c1_reuse.py', 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'),\n ",
          "count": 1
        },
        {
          "old": "ROOT_SNAPSHOT_SCHEMA = 'actual-reference-centred-C1-normal-current-point-snapshot-v1'",
          "new": "ROOT_SNAPSHOT_SCHEMA = 'actual-reference-centred-analytic-J3-normal-current-point-snapshot-v1'",
          "count": 1
        },
        {
          "old": " 'current_reference_calibration')",
          "new": " 'current_reference_calibration',\n 'analytic_stage_jacobian')",
          "count": 1
        },
        {
          "old": "    stage_matrices = load('_actual_complete_detached_stage_matrices',paths['stage_matrices'])",
          "new": "    analytic_stage = load('_actual_complete_analytic_local_J3',paths['analytic_J3'])\n    stage_matrices = load('_actual_complete_detached_stage_matrices',paths['stage_matrices'])",
          "count": 1
        },
        {
          "old": "        adjacent_matrix_module=adjacent_matrices)",
          "new": "        adjacent_matrix_module=adjacent_matrices,analytic_stage_module=analytic_stage)",
          "count": 1
        },
        {
          "old": "        adjacent_normal_frame_matrix_source=file_record(paths['adjacent_matrices']),",
          "new": "        adjacent_normal_frame_matrix_source=file_record(paths['adjacent_matrices']),\n        analytic_stage_jacobian_definition=q.analytic_stage_jacobian.definition,\n        analytic_stage_jacobian_source=file_record(paths['analytic_J3']),\n        analytic_stage_J3_full_original_residual_and_chain_retained=True,\n        analytic_stage_J3_speedup_or_rounding_certified=False,",
          "count": 1
        },
        {
          "old": "a1971fd5328032af735553a7e99fcfcd78f44e7b37ee78f666564d7e0b294680",
          "new": "f34fcafc06b50594b7a651a90e38553ea8ae3da5b6ac8b6ca4ea691d2ab9f14f",
          "count": 1
        },
        {
          "old": "d11fd0ed7fecd47d1f9710380f6dfbd431ac9f658f6e32d9256f990f264bdc6b",
          "new": "aed482145c835b28fd74611dc9b7deffa1e433ab43a90a020daf357ace23c3b7",
          "count": 1
        },
        {
          "old": "SOURCE_PINS = {",
          "new": "SOURCE_PINS = {\n 'root_packets': ('scripts/resume_20261126/immutable_analytic_normal_root_packets_v2.py',\n    '1e0656b19de4eb78937a9f8305569d7c1cce59f48614fb7a279738942bcd622e'),\n 'analytic_parent_stage_matrices': ('scripts/resume_20261126/detached_normal_stage_matrix_reuse.py',\n    '375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59'),\n 'analytic_parent_adjacent_matrices': ('scripts/resume_20261126/adjacent_normal_frame_matrices.py',\n    '955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3'),\n 'analytic_parent_driver': ('scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py',\n    '95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9'),\n 'analytic_parent_reader': ('scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py',\n    'f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470'),\n",
          "count": 1
        },
        {
          "old": "    qp = load('_so3_complete_QPv3', paths['qp'])",
          "new": "    qp = load('_so3_complete_QPv3', paths['qp'])\n    root_packets = load('_actual_immutable_normal_root_packets', paths['root_packets'])",
          "count": 1
        },
        {
          "old": "    if (args.independent_envelope_branch or (restart is not None\n            and restart.get('material_envelope',{}).get('source_sha256')==SOURCE_PINS['independent_envelope_memory'][1])):",
          "new": "    if (args.independent_envelope_branch or (restart is not None\n            and restart.get('material_envelope',{}).get('source_sha256')==SOURCE_PINS['independent_envelope_memory'][1])\n            or envelope_transfer.requested_parent_memory(args)==SOURCE_PINS['independent_envelope_memory'][1]):",
          "count": 1
        },
        {
          "old": "    initial_envelope_metadata=envelope.metadata()",
          "new": "    packet_recorder = root_packets.NormalRootPacketRecorder(q,repo=args.repo,\n        outdir=args.outdir/'immutable-normal-root-packets',caller_source=__file__,source_paths=paths)\n    initial_envelope_metadata=envelope.metadata()",
          "count": 1
        },
        {
          "old": "        complete=False, independent_preparation_report=file_record(args.preparation_report),",
          "new": "        complete=False, independent_preparation_report=file_record(args.preparation_report),\n        normal_root_packet_source=file_record(paths['root_packets']),\n        normal_root_packet_definition=root_packets.definition(),normal_root_packet_record_only=True,\n        normal_root_packets=packet_recorder.metadata(),normal_root_packet_latest_entry_capture=None,",
          "count": 1
        },
        {
          "old": "    def save_report():\n        report['latest_operator_metadata'] = q.metadata()",
          "new": "    def save_report():\n        report['latest_operator_metadata'] = q.metadata()\n        report['normal_root_packet_latest_entry_capture'] = packet_recorder.capture_entry(\n            report['latest_operator_metadata'],outer_full_point_sha256=meridian.array_sha(x),\n            witnesses=witnesses,radius_witnesses=radius_witnesses,label='actual-report-save')\n        report['normal_root_packets'] = packet_recorder.metadata()",
          "count": 1
        },
        {
          "old": "        record['actual_QP_operator_counts'] = {key: q.counts[key]-qp_counts_before[key] for key in q.counts}",
          "new": "        record['actual_QP_operator_counts'] = {key: q.counts[key]-qp_counts_before[key] for key in q.counts}\n        record['normal_root_packet_at_QP_return'] = packet_recorder.capture_entry(q.metadata(),\n            outer_full_point_sha256=meridian.array_sha(x),witnesses=witnesses,\n            radius_witnesses=radius_witnesses,label=phase+'-QP-return-'+str(record['serial']))",
          "count": 1
        },
        {
          "old": "aed482145c835b28fd74611dc9b7deffa1e433ab43a90a020daf357ace23c3b7",
          "new": "0d2a5e9c9f5651e149d53da859ac42ced1c3b44709f9a5a3416a82c8d8702608",
          "count": 1
        },
        {
          "old": "    p.add_argument('--pending-parallel-envelope-run', action='append', default=[])",
          "new": "    p.add_argument('--pending-parallel-envelope-run', action='append', default=[])\n    p.add_argument('--pending-parallel-envelope-source', action='append', default=[])",
          "count": 1
        },
        {
          "old": "    a.manifest = [path.resolve() for path in a.manifest]",
          "new": "    pending_sources={}\n    for value in a.pending_parallel_envelope_source:\n        parts=value.split('=')\n        if (len(parts)!=2 or parts[0] in pending_sources or len(parts[1])!=64\n                or any(c not in '0123456789abcdef' for c in parts[1])):\n            raise ValueError('Use one complete explicit driver digest per pending run')\n        pending_sources[parts[0]]=parts[1]\n    if set(pending_sources)!=set(a.pending_parallel_envelope_run):\n        raise ValueError('Every pending peer requires its exact run-to-source declaration')\n    a.manifest = [path.resolve() for path in a.manifest]",
          "count": 1
        }
      ]
    },
    {
      "parent_role": "launcher",
      "parent_filename": "launch_reference_centred_independent_chart_material_envelope_so3_actions.py",
      "parent_sha256": "10422033f229649aa2e8237c25880670219d618d24690d429025347fd73f039b",
      "parent_bytes": 20746,
      "filename": "launch_reference_centred_analytic_j3_material_envelope_so3_actions.py",
      "sha256": "6228512d27d54027edf6985b640d74edac9a79c8ddb5e386b0b064e362bdb797",
      "bytes": 21366,
      "edits": [
        {
          "old": "95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9",
          "new": "dcac1f6856d83d94c082603b08de7d58f99309cd3fbf6cb194d664838b68e359",
          "count": 1
        },
        {
          "old": "fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py",
          "new": "fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py",
          "count": 1
        },
        {
          "old": "dcac1f6856d83d94c082603b08de7d58f99309cd3fbf6cb194d664838b68e359",
          "new": "6834ca8314c831b7611ce6f501accf881b81a35c69851ca6f85851108da7242a",
          "count": 1
        },
        {
          "old": "original_Newton_matrices_and_all_stage_equations_retained=True",
          "new": "selected_local_J3_and_all_stage_equations_retained=True",
          "count": 1
        },
        {
          "old": "6834ca8314c831b7611ce6f501accf881b81a35c69851ca6f85851108da7242a",
          "new": "0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51",
          "count": 1
        },
        {
          "old": "    p.add_argument('--pending-parallel-envelope-run', action='append', default=[])",
          "new": "    p.add_argument('--pending-parallel-envelope-run', action='append', default=[])\n    p.add_argument('--pending-parallel-envelope-source', action='append', default=[])",
          "count": 1
        },
        {
          "old": "    a.manifest = [path.resolve() for path in a.manifest]",
          "new": "    pending_sources={}\n    for value in a.pending_parallel_envelope_source:\n        parts=value.split('=')\n        if (len(parts)!=2 or parts[0] in pending_sources or len(parts[1])!=64\n                or any(c not in '0123456789abcdef' for c in parts[1])):\n            raise ValueError('Use one complete explicit driver digest per pending run')\n        pending_sources[parts[0]]=parts[1]\n    if set(pending_sources)!=set(a.pending_parallel_envelope_run):\n        raise ValueError('Every pending peer requires its exact run-to-source declaration')\n    a.manifest = [path.resolve() for path in a.manifest]",
          "count": 1
        }
      ]
    },
    {
      "parent_role": "reader",
      "parent_filename": "read_reference_centred_independent_chart_material_envelope_so3_report.py",
      "parent_sha256": "f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470",
      "parent_bytes": 98389,
      "filename": "read_reference_centred_analytic_j3_material_envelope_so3_report.py",
      "sha256": "c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e",
      "bytes": 99527,
      "edits": [
        {
          "old": "DRIVER_SHA = '95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9'",
          "new": "DRIVER_SHA = 'dcac1f6856d83d94c082603b08de7d58f99309cd3fbf6cb194d664838b68e359'",
          "count": 1
        },
        {
          "old": "complete-R711-reference-centred-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1",
          "new": "complete-R711-reference-centred-analytic-J3-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1",
          "count": 1
        },
        {
          "old": "complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1",
          "new": "complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1",
          "count": 1
        },
        {
          "old": "actual-reference-centred-C1-normal-current-point-snapshot-v1",
          "new": "actual-reference-centred-analytic-J3-normal-current-point-snapshot-v1",
          "count": 1
        },
        {
          "old": " 'current_reference_calibration')",
          "new": " 'current_reference_calibration','analytic_stage_jacobian')",
          "count": 1
        },
        {
          "old": "names = {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST'}",
          "new": "names = {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST','ANALYTIC_STAGE_SOURCE_SHA256'}",
          "count": 1
        },
        {
          "old": "'BASE_SOURCE_SHA256','PHASES','NORMAL_COUNTER_KEYS'}",
          "new": "'BASE_SOURCE_SHA256','PHASES','NORMAL_COUNTER_KEYS','ANALYTIC_STAGE_SOURCE_SHA256'}",
          "count": 1
        },
        {
          "old": "'PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256','COUNTER_KEYS'}",
          "new": "'PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256','COUNTER_KEYS','ANALYTIC_STAGE_SOURCE_SHA256'}",
          "count": 1
        },
        {
          "old": "original_Newton_matrices_unchanged=True",
          "new": "selected_local_matrices_unchanged_by_cache=True",
          "count": 1
        },
        {
          "old": "original_root_Newton_J3_and_active_chain_retained=True",
          "new": "selected_local_J3_and_original_root_active_chain_retained=True",
          "count": 1
        },
        {
          "old": "fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py",
          "new": "fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py",
          "count": 1
        },
        {
          "old": "def read_report(repo, report_path, *, verify_final_bundle=False):",
          "new": "def extra_bindings(report,topic,driver):\n    answer={}\n    for role,function in (('analytic_J3_binding','read_actual'),('root_packets','validate_entry_report')):\n        relative,expected=load_pins(driver)[role];path=topic/relative\n        if sha(path)!=expected:raise ValueError('Changed complete entry helper: '+role)\n        spec=importlib.util.spec_from_file_location('_entry_pure_'+expected,path)\n        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)\n        fn=getattr(module,function)\n        if sha(fn.__code__.co_filename)!=expected:raise ValueError('Changed actual pure entry function')\n        answer[role]=(fn(report,roles=report['source_sha256_by_role'],source_directory=path.parent)\n            if role=='analytic_J3_binding' else fn(report,reread_packets=True,reread_arrays=True))\n    return answer\n\n\ndef read_report(repo, report_path, *, verify_final_bundle=False):",
          "count": 1
        },
        {
          "old": "    independent_target=independent_chart_binding(report,envelope_binding)",
          "new": "    independent_target=independent_chart_binding(report,envelope_binding)\n    extra=extra_bindings(report,topic,driver)",
          "count": 1
        },
        {
          "old": "actual-complete-R711-reference-centred-independent-chart-material-envelope-normal-plane-SO3-scalar-readout-v1",
          "new": "actual-complete-R711-reference-centred-analytic-J3-packet-envelope-SO3-scalar-readout-v1",
          "count": 1
        },
        {
          "old": "        reference_centering=centered_binding,",
          "new": "        reference_centering=centered_binding,analytic_stage_jacobian=extra['analytic_J3_binding'],\n        normal_root_packets=extra['root_packets'],",
          "count": 1
        },
        {
          "old": "dcac1f6856d83d94c082603b08de7d58f99309cd3fbf6cb194d664838b68e359",
          "new": "0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51",
          "count": 1
        }
      ]
    }
  ],
  "lower_sources": [
    {
      "filename": "analytic_normal_stage_jacobian.py",
      "bytes": 24240,
      "sha256": "64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d"
    },
    {
      "filename": "analytic_j3_normal_frame_c1_reuse.py",
      "bytes": 35625,
      "sha256": "8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8"
    },
    {
      "filename": "analytic_j3_detached_normal_stage_matrix_reuse.py",
      "bytes": 47673,
      "sha256": "5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1"
    },
    {
      "filename": "analytic_j3_adjacent_normal_frame_matrices.py",
      "bytes": 36734,
      "sha256": "8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787"
    },
    {
      "filename": "reference_centred_analytic_j3_smooth_triangle_calibration.py",
      "bytes": 11911,
      "sha256": "4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d"
    },
    {
      "filename": "so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py",
      "bytes": 96906,
      "sha256": "04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e"
    }
  ],
  "pure_binding": {
    "filename": "analytic_j3_source_and_report_binding.py",
    "source": "#!/usr/bin/env python3\n\"\"\"Pure complete source/model/report binding for the analytic local-J3 family.\n\nOnly immutable source text and already returned JSON metadata are consumed.\nThere is no NumPy/Torch import, numeric matrix construction, F/J/root call,\nquadrature, or inference of root/geometry success.\n\"\"\"\nimport ast\nimport copy\nimport hashlib\nimport json\nimport math\nfrom pathlib import Path\n\nSCHEMA = 'complete-analytic-J3-source-model-and-report-binding-v1'\nOPERATOR_SCHEMA = 'complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'\nROOT_SNAPSHOT_SCHEMA = 'actual-reference-centred-analytic-J3-normal-current-point-snapshot-v1'\nLEGACY_OPERATOR_SCHEMA = 'complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1'\nLEGACY_OPERATOR_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'\nLEGACY_CALIBRATION_SHA256 = '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'\nLEGACY_C1_SHA256 = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'\nBASE_SOURCE_SHA256 = '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'\nSOURCE_BINDINGS = {\n    \"analytic_J3\": (\"analytic_normal_stage_jacobian.py\", \"64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d\"),\n    \"frame_C1\": (\"analytic_j3_normal_frame_c1_reuse.py\", \"8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8\"),\n    \"stage_matrices\": (\"analytic_j3_detached_normal_stage_matrix_reuse.py\", \"5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1\"),\n    \"adjacent_matrices\": (\"analytic_j3_adjacent_normal_frame_matrices.py\", \"8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787\"),\n    \"reference_calibration\": (\"reference_centred_analytic_j3_smooth_triangle_calibration.py\", \"4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d\"),\n    \"endpoint\": (\"so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py\", \"04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e\"),\n}\nPOLICY_KEYS = {\n    'analytic_J3':'analytic_stage_jacobian',\n    'frame_C1':'normal_frame_C1_reuse',\n    'stage_matrices':'detached_stage_matrix_reuse',\n    'adjacent_matrices':'adjacent_normal_frame_matrices'}\nPOLICY_CONSTANTS = {\n    'analytic_J3':{'SCHEMA','ENDPOINT_SCHEMA','BASE_SOURCE_SHA256',\n        'PARENT_NORMAL_SOURCE_SHA256','METHOD_AST','COUNTER_KEYS','OBSERVED_COUNTER_KEYS'},\n    'frame_C1':{'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST','ANALYTIC_STAGE_SOURCE_SHA256'},\n    'stage_matrices':{'SCHEMA','FRAME_C1_SOURCE_SHA256','ORIGINAL_C1_OPERATOR_SOURCE_SHA256',\n        'BASE_SOURCE_SHA256','PHASES','ANALYTIC_STAGE_SOURCE_SHA256'},\n    'adjacent_matrices':{'SCHEMA','FRAME_C1_SOURCE_SHA256','STAGE_MATRIX_SOURCE_SHA256',\n        'PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256','ANALYTIC_STAGE_SOURCE_SHA256'}}\n\n\ndef sha(path):\n    return hashlib.sha256(Path(path).read_bytes()).hexdigest()\n\n\ndef canonical(value):\n    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),\n        allow_nan=False).encode()).hexdigest()\n\n\ndef _pure(path,expected,constants,functions):\n    path=Path(path).resolve()\n    raw=path.read_bytes()\n    if len(raw)>=100000 or hashlib.sha256(raw).hexdigest()!=expected:\n        raise ValueError('Bind the whole independently declared small source: '+path.name)\n    tree=ast.parse(raw)\n    body=[];seen_names=set();seen_functions=set()\n    for node in tree.body:\n        if (isinstance(node,ast.Assign) and len(node.targets)==1\n                and isinstance(node.targets[0],ast.Name) and node.targets[0].id in constants):\n            ast.literal_eval(node.value)\n            body.append(node);seen_names.add(node.targets[0].id)\n        if isinstance(node,ast.FunctionDef) and node.name in functions:\n            body.append(node);seen_functions.add(node.name)\n    if seen_names!=set(constants) or seen_functions!=set(functions):\n        raise ValueError('The full source-bound pure interface changed: '+path.name)\n    namespace=dict(Path=Path,hashlib=hashlib,json=json,math=math,__file__=str(path))\n    exec(compile(ast.Module(body=body,type_ignores=[]),'<complete bound pure analytic J3>','exec'),namespace)\n    if sha(path)!=expected:\n        raise ValueError('Source bytes changed during pure extraction')\n    return namespace\n\n\ndef _policies(directory):\n    directory=Path(directory).resolve()\n    result={}\n    for role,key in POLICY_KEYS.items():\n        name,digest=SOURCE_BINDINGS[role]\n        functions={'sha','definition'}\n        if role=='analytic_J3':\n            functions|={'canonical','_copy','_digest','_counts','validate_metadata'}\n        namespace=_pure(directory/name,digest,POLICY_CONSTANTS[role],functions)\n        result[key]=namespace['definition']()\n        if role=='analytic_J3':\n            result['actual_validator']=namespace['validate_metadata']\n    return result\n\n\ndef validate_current_model(model, *, roles, source_directory):\n    directory=Path(source_directory).resolve()\n    for role,(name,expected) in SOURCE_BINDINGS.items():\n        if roles.get(role)!=expected or sha(directory/name)!=expected:\n            raise ValueError('The actual full analytic-J3 source role differs: '+role)\n    if (not isinstance(model,dict) or model.get('schema')!=OPERATOR_SCHEMA\n            or model.get('source_sha256')!=roles['endpoint']\n            or model.get('base_source_sha256')!=BASE_SOURCE_SHA256\n            or model.get('base_complete_model',{}).get('source_sha256')!=BASE_SOURCE_SHA256\n            or canonical(model['base_complete_model'])!=model.get('base_model_identity_sha256')):\n        raise ValueError('Keep the complete actual current normal and fixed base')\n    policies=_policies(directory)\n    for role,key in POLICY_KEYS.items():\n        if model.get(key)!=policies[key]:\n            raise ValueError('The complete actual current working policy changed: '+key)\n    centering=model.get('reference_centering_definition',{})\n    if (centering.get('source_sha256')!=roles['reference_calibration']\n            or centering.get('endpoint_source_sha256')!=roles['endpoint']\n            or model.get('common_partition_for_all_angles_and_free_points') is not True\n            or model.get('per_angle_adaptive_normal_partition') is not False\n            or model.get('normal_stage_count',0)<1\n            or model.get('implicit_control_dimension')!=6\n            or model.get('normal_increment_dimension')!=3\n            or model.get('complete_first_angular_implicit_dimension')!=6*model['normal_stage_count']\n            or model.get('complete_second_angular_implicit_dimension')!=9*model['normal_stage_count']):\n        raise ValueError('The current calibration, complete six controls or finite chain changed')\n    return policies\n\n\ndef compatible_legacy_model(old,new,current_pins,*,source_directory):\n    \"\"\"Strict cc0a/104e or 95559/f382 relation, after the whole original reader.\"\"\"\n    roles={role:record[1] for role,record in current_pins.items()}\n    validate_current_model(new,roles=roles,source_directory=source_directory)\n    adjacent_source='d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb'\n    adjacent_schema='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'\n    adjacent_calibration='ccb3340e500a032943aaed084376136fd67ad81b222e1afbcc5e79d468f21ef8'\n    stage_source='375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59'\n    adjacent_helper='955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3'\n    original=old.get('source_sha256')\n    if original==LEGACY_OPERATOR_SHA256:\n        old_schema,old_calibration=LEGACY_OPERATOR_SCHEMA,LEGACY_CALIBRATION_SHA256\n        old_keys=['normal_frame_C1_reuse']\n    elif original==adjacent_source:\n        old_schema,old_calibration=adjacent_schema,adjacent_calibration\n        old_keys=['normal_frame_C1_reuse','detached_stage_matrix_reuse','adjacent_normal_frame_matrices']\n    else:\n        raise ValueError('This explicit transfer supports only its two whole declared parent families')\n    if (old.get('schema')!=old_schema\n            or old.get('reference_centering_definition',{}).get('source_sha256')!=old_calibration\n            or old.get('reference_centering_definition',{}).get('endpoint_source_sha256')!=original\n            or roles.get('analytic_parent_frame_C1')!=LEGACY_C1_SHA256):\n        raise ValueError('Bind the complete actual parent normal, calibration and original frame source')\n    original_policies={\n        'normal_frame_C1_reuse':('normal_frame_c1_reuse.py',LEGACY_C1_SHA256,\n            {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST'},'analytic_parent_frame_C1')}\n    if original==adjacent_source:\n        original_policies.update({\n            'detached_stage_matrix_reuse':('detached_normal_stage_matrix_reuse.py',stage_source,\n                {'SCHEMA','FRAME_C1_SOURCE_SHA256','ORIGINAL_C1_OPERATOR_SOURCE_SHA256',\n                 'BASE_SOURCE_SHA256','PHASES'},'analytic_parent_stage_matrices'),\n            'adjacent_normal_frame_matrices':('adjacent_normal_frame_matrices.py',adjacent_helper,\n                {'SCHEMA','FRAME_C1_SOURCE_SHA256','STAGE_MATRIX_SOURCE_SHA256',\n                 'PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256'},'analytic_parent_adjacent_matrices')})\n    for key,(name,digest,constants,role) in original_policies.items():\n        if roles.get(role)!=digest:\n            raise ValueError('The whole original parent working policy is absent: '+role)\n        namespace=_pure(Path(source_directory)/name,digest,constants,{'sha','definition'})\n        if old.get(key)!=namespace['definition']():\n            raise ValueError('Do not relabel the actual complete parent working policy: '+key)\n    before,after=copy.deepcopy(old),copy.deepcopy(new)\n    for key in old_keys:\n        before.pop(key)\n    for key in POLICY_KEYS.values():\n        after.pop(key)\n    for value in (before,after):\n        for key in ('schema','source_sha256'):\n            value.pop(key)\n        for key in ('source_sha256','endpoint_source_sha256'):\n            value['reference_centering_definition'].pop(key)\n    if before!=after:\n        raise ValueError('The complete actual base/target/chart/seed/free space/partition or other field definition changed')\n    return dict(complete_unchanged_definition_sha256=canonical(before),\n        exact_old_complete_model_identity_sha256=canonical(old),\n        exact_new_complete_model_identity_sha256=canonical(new),\n        full_base_reference_chart_profile_and_partition_equal=True,\n        only_explicit_source_schema_and_matrix_working_policy_fields_changed=True,\n        computed_float_field_equality_claimed=False)\n\ndef read_actual(report,*,roles,source_directory):\n    \"\"\"Validate every actual new snapshot and full metadata at its OWN point.\"\"\"\n    model=report['representation']\n    policies=validate_current_model(model,roles=roles,source_directory=source_directory)\n    expected=policies['analytic_stage_jacobian']\n    if (report.get('analytic_stage_jacobian_definition')!=expected\n            or report.get('analytic_stage_jacobian_source',{}).get('sha256')!=roles['analytic_J3']\n            or report.get('analytic_stage_J3_full_original_residual_and_chain_retained') is not True\n            or report.get('analytic_stage_J3_speedup_or_rounding_certified') is not False):\n        raise ValueError('Bind the complete declared analytic partial without inherited success or speed')\n    validator=policies['actual_validator']\n    count=0\n    metadata_count=0\n    def visit(value):\n        nonlocal count,metadata_count\n        if isinstance(value,dict):\n            if value.get('schema')==ROOT_SNAPSHOT_SCHEMA:\n                if (value.get('operator_schema')!=OPERATOR_SCHEMA\n                        or value.get('operator_source_sha256')!=roles['endpoint']\n                        or value.get('model_identity_sha256')!=canonical(model)):\n                    raise ValueError('An analytic matrix snapshot belongs to another actual field')\n                validator(value.get('analytic_stage_jacobian'),model=model,source_by_role=roles,\n                    current_full_point_sha256=value.get('current_full_point_sha256'))\n                count+=1\n            elif value.get('schema')==OPERATOR_SCHEMA and 'model' in value:\n                if value['model']!=model or value.get('model_identity_sha256')!=canonical(model):\n                    raise ValueError('A full matrix metadata record belongs to another actual field')\n                validator(value.get('analytic_stage_jacobian'),model=model,source_by_role=roles,\n                    current_full_point_sha256=value.get('current_full_point_sha256'))\n                metadata_count+=1\n            for child in value.values():\n                visit(child)\n        elif isinstance(value,list):\n            for child in value:\n                visit(child)\n    visit(report)\n    latest=report.get('latest_operator_metadata')\n    actual=None\n    if latest:\n        if latest.get('schema')!=OPERATOR_SCHEMA or latest.get('model')!=model:\n            raise ValueError('Do not substitute another latest operator record')\n        actual=validator(latest.get('analytic_stage_jacobian'),model=model,source_by_role=roles,\n            current_full_point_sha256=latest.get('current_full_point_sha256'))\n    elif report.get('complete') is True:\n        raise ValueError('A complete budget must retain its own actual local-matrix counters')\n    return dict(schema=SCHEMA,source_sha256=sha(__file__),\n        actual_analytic_source_sha256=roles['analytic_J3'],\n        actual_operator_source_sha256=roles['endpoint'],\n        actual_model_identity_sha256=canonical(model),\n        definition=expected,definition_identity_sha256=canonical(expected),\n        actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,\n        latest_actual_diagnostics=actual,\n        snapshot_values_backfilled_from_latest=False,\n        original_full_stage_residual_domain_Armijo_and_all_upstream_J_retained=True,\n        local_J3_is_not_an_endpoint_root_or_geometry_certificate=True,\n        every_matrix_request_is_a_complete_three_by_three_batch=True,\n        source_or_binding_failures_silently_fallback=False,\n        current_scientific_values_recomputed=False)\n",
    "sha256": "f34fcafc06b50594b7a651a90e38553ea8ae3da5b6ac8b6ca4ea691d2ab9f14f",
    "bytes": 14308
  },
  "packet": {
    "filename": "immutable_analytic_normal_root_packets_v2.py",
    "sha256": "1e0656b19de4eb78937a9f8305569d7c1cce59f48614fb7a279738942bcd622e",
    "bytes": 67095,
    "blob": "4eef12117ecef023ffef257607ea1ef2fec75a6a"
  }
}''')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def checked_text(path, expected):
    raw=Path(path).read_bytes()
    if len(raw)!=expected['bytes'] or digest(raw)!=expected['sha256']:
        raise ValueError('Whole source differs: '+str(path))
    if len(raw)>=100000:
        raise ValueError('Every full source remains individually below 100000 bytes')
    return raw.decode('utf-8')


def check_source(text, name):
    if not text.endswith('\n') or any(line.rstrip()!=line for line in text.splitlines()):
        raise ValueError('Keep the full source without trailing whitespace: '+name)
    tree=ast.parse(text,filename=name)
    compile(tree,name,'exec')
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            seen=set()
            for key in node.keys:
                if key is None:
                    continue
                try:
                    value=ast.literal_eval(key)
                    hash(value)
                except (ValueError,TypeError,SyntaxError):
                    continue
                if value in seen:
                    raise ValueError('A duplicate literal dictionary key occurs: '+name)
                seen.add(value)
    return tree


def literal(tree, key):
    values=[ast.literal_eval(node.value) for node in tree.body
        if isinstance(node,ast.Assign) and len(node.targets)==1
        and isinstance(node.targets[0],ast.Name) and node.targets[0].id==key]
    if len(values)!=1:
        raise ValueError('Bind one complete literal '+key)
    return values[0]


def functions(tree):
    return {node.name:ast.dump(node,include_attributes=False)
        for node in tree.body if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef))}


def class_methods(tree):
    return {(node.name,method.name):ast.dump(method,include_attributes=False)
        for node in tree.body if isinstance(node,ast.ClassDef)
        for method in node.body if isinstance(method,(ast.FunctionDef,ast.AsyncFunctionDef))}


def parse_without_launcher_flags(tree):
    function=next(node for node in tree.body
        if isinstance(node,ast.FunctionDef) and node.name=='parse_args')
    body=[]
    for statement in function.body:
        if (isinstance(statement,ast.Expr) and isinstance(statement.value,ast.Call)
                and statement.value.args and isinstance(statement.value.args[0],ast.Constant)
                and statement.value.args[0].value in ('--install-torch','--print-command')):
            continue
        body.append(statement)
    function.body=body
    return ast.dump(function,include_attributes=False)


def write_exact(path, raw):
    path=Path(path)
    if path.exists():
        if path.read_bytes()!=raw:
            raise FileExistsError('Never overwrite a different complete source: '+str(path))
        return
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as stream:
        stream.write(raw)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-directory',type=Path,required=True)
    parser.add_argument('--lower-directory',type=Path,required=True)
    parser.add_argument('--packet-source',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    source=args.source_directory.resolve();lower=args.lower_directory.resolve()
    out=args.out.resolve()
    input_paths=[source/item['parent_filename'] for item in PLAN['plans']]
    input_paths += [lower/item['filename'] for item in PLAN['lower_sources']]
    input_paths.append(args.packet_source.resolve())
    if any(out==path or out in path.parents for path in input_paths):
        raise ValueError('The output namespace must not contain any complete input source')
    produced={};parents={};trees={};original_trees={}
    changes={}
    for item in PLAN['plans']:
        old=checked_text(source/item['parent_filename'],
            dict(bytes=item['parent_bytes'],sha256=item['parent_sha256']))
        parents[item['parent_role']]=old
        original_trees[item['parent_role']]=check_source(old,item['parent_filename'])
        value=old
        for change in item['edits']:
            if value.count(change['old'])!=change['count']:
                raise ValueError('An exact complete-source patch differs: '+item['filename'])
            value=value.replace(change['old'],change['new'])
        raw=value.encode('utf-8')
        if len(raw)!=item['bytes'] or digest(raw)!=item['sha256']:
            raise ValueError('The regenerated full source identity differs: '+item['filename'])
        trees[item['parent_role']]=check_source(value,item['filename'])
        produced[item['filename']]=raw
        before=functions(original_trees[item['parent_role']])
        after=functions(trees[item['parent_role']])
        changes[item['parent_role']]=dict(
            changed_functions=[name for name in sorted(before.keys()&after.keys()) if before[name]!=after[name]],
            added_functions=sorted(after.keys()-before.keys()),
            removed_functions=sorted(before.keys()-after.keys()),
            unchanged_functions=sum(before[name]==after[name] for name in before.keys()&after.keys()))
    item=PLAN['pure_binding'];value=item['source'];raw=value.encode('utf-8')
    if len(raw)!=item['bytes'] or digest(raw)!=item['sha256']:
        raise ValueError('The full pure binding literal differs')
    check_source(value,item['filename']);produced[item['filename']]=raw
    packet=checked_text(args.packet_source,PLAN['packet'])
    check_source(packet,PLAN['packet']['filename'])
    produced[PLAN['packet']['filename']]=packet.encode('utf-8')
    lower_records=[]
    for item in PLAN['lower_sources']:
        value=checked_text(lower/item['filename'],item)
        check_source(value,item['filename'])
        lower_records.append(dict(filename=item['filename'],bytes=item['bytes'],sha256=item['sha256']))
    # The complete mathematical geometry methods remain the original methods.
    before=class_methods(original_trees['geometry']);after=class_methods(trees['geometry'])
    changed=[key for key in before if before[key]!=after[key]]
    if before.keys()!=after.keys() or changed!=[('GeometryScreen','__init__')]:
        raise ValueError('Only the exact new geometry source/instance binding may change')
    # The two added packet hooks only copy already existing actual data.
    driver_name=next(item['filename'] for item in PLAN['plans'] if item['parent_role']=='driver')
    driver=produced[driver_name].decode()
    suffix=driver[driver.index('    def save_report():'):]
    for change in next(item for item in PLAN['plans'] if item['parent_role']=='driver')['edits']:
        if (change['old'].startswith("    def save_report():\n")
                or change['old'].startswith("        record['actual_QP_operator_counts']")):
            if suffix.count(change['new'])!=1:
                raise ValueError('The exact complete immutable-copy hook changed')
            suffix=suffix.replace(change['new'],change['old'])
    original_suffix=parents['driver'][parents['driver'].index('    def save_report():'):]
    if suffix!=original_suffix:
        raise ValueError('The original QP, global implicit chain, Phase I and true screening body changed')
    if parse_without_launcher_flags(trees['driver'])!=parse_without_launcher_flags(trees['launcher']):
        raise ValueError('Launcher and full driver arguments must remain exactly the same')
    pins=literal(original_trees['driver'],'SOURCE_PINS')
    current=literal(ast.parse(driver),'SOURCE_PINS')
    required_added={'analytic_J3','analytic_J3_binding','analytic_parent_frame_C1',
        'analytic_parent_stage_matrices','analytic_parent_adjacent_matrices',
        'analytic_parent_driver','analytic_parent_reader','root_packets'}
    if set(current)-set(pins)!=required_added or set(pins)-set(current):
        raise ValueError('Retain every original source role and each declared new complete role')
    modified={'endpoint','reference_calibration','frame_C1','stage_matrices',
        'adjacent_matrices','geometry','envelope_transfer'}
    for role in pins:
        if role not in modified and current[role]!=pins[role]:
            raise ValueError('An unrelated original source role changed: '+role)
    identities={name:digest(raw) for name,raw in produced.items()}
    identities.update({item['filename']:item['sha256'] for item in PLAN['lower_sources']})
    for role,(relative,expected) in current.items():
        name=Path(relative).name
        if name in identities and identities[name]!=expected:
            raise ValueError('The actual full generated role has a different source identity: '+role)
    lock=dict(schema=PLAN['schema'],complete_source_only_replay=True,
        scientific_modules_imported=False,scientific_computations_executed=False,
        parent_public_commit=PLAN['parent_public_commit'],
        complete_lower_sources=lower_records,
        outputs=[dict(filename=name,bytes=len(raw),sha256=digest(raw))
            for name,raw in produced.items()],
        full_source_role_count=len(current),source_sha256_by_role={key:value[1] for key,value in current.items()},
        all_original_roles_retained=True,
        complete_original_scientific_suffix_after_removing_only_two_record_hooks_sha256=
            digest(original_suffix.encode()),
        geometry_changed_methods=[list(key) for key in changed],
        top_level_function_changes=changes,
        full_source_whole_byte_identical_replay=True,
        actual_numerical_success_or_speedup_claimed=False)
    for name,raw in produced.items():
        write_exact(out/name,raw)
    write_exact(out/'analytic-J3-complete-entry-source-lock.json',
        (json.dumps(lock,indent=2,sort_keys=True)+'\n').encode())
    print(json.dumps(dict(complete=True,output_directory=str(out),
        source_only=True,output_count=len(produced),source_role_count=len(current),
        scientific_computations_executed=False),sort_keys=True))


if __name__=='__main__':
    main()
