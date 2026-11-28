#!/usr/bin/env python3
"""Reproduce three complete R723-compatible mesh sources from exact whole parents.

Only stdlib source text is read and written. This program never imports the
generated runtime, parses Python AST, compiles code or performs scientific work.
It is a reproducibility artifact, not a required solver or certificate gate.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

SPEC = json.loads(r'''{
  "schema": "fixed-fejer-R723-compatible-mesh-source-construction-v1",
  "scientific_execution": false,
  "parsing_or_compilation_performed": false,
  "complete_parents_and_outputs": [
    {
      "role": "input",
      "parent": {
        "kind": "complete_runtime_source",
        "name": "fixed_fejer_meridian_batched_producer_bound_same_field_mesh_input.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_bound_same_field_mesh_input.py",
        "bytes": 73500,
        "sha256": "2ef316b9075f14af66e1deda235c4df9319a0c29cfeddb10a40130712a12d76c",
        "git_blob_sha": "62e4551908e43beb9684db85998a49ff81337d5e"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_mesh_input.py",
        "name": "fixed_fejer_R723_compatible_same_field_mesh_input.py",
        "bytes": 95330,
        "sha256": "6c678893db4cff3366a0836ee900e67aabd23b5267768369d6bfa41479197aa8",
        "git_blob_sha": "fe0c0798c6a5ff50c140a0ad00e5e1b5b88e2530"
      },
      "exact_ordered_text_patches": [
        {
          "before": "SCHEMA = \"actual-fixed-fejer-meridian-batched-producer-bound-same-field-complete-mesh-input-v1\"",
          "after": "SCHEMA = \"actual-fixed-fejer-R723-compatible-meridian-batched-producer-bound-same-field-complete-mesh-input-v1\""
        },
        {
          "before": "CURRENT_SCALAR_LEAVES = 2218\n",
          "after": "CURRENT_SCALAR_LEAVES = 2218\n\nR723_CLOSED_SOURCE_NAME = \"fixed_fejer_R723_directional_closed_phase_grip_evidence.py\"\nR723_CLOSED_SOURCE_SHA = \"1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc\"\nR723_CLOSED_SCHEMA = \"actual-fixed-fejer-R723-directional-closed-phase-grip-evidence-v1\"\nR723_EVIDENCE_SCHEMA = \"actual-fixed-fejer-R723-compatible-same-point-optional-closed-evidence-v1\"\nR723_THEOREM = (TOPIC+\"/results/R723-directional-normal-flow-support-reach.md\",\n    \"0edbd1039706186d07412a53c8e5c10411c5966dc36e38a7a504cf923d43e7eb\")\nR723_NORMAL_FEE_SOURCE_SHA = \"c6f6c9726b23ceb25533d5a6a6ac41fd31e8a3c14226895d5fc32e74787c0108\"\n"
        },
        {
          "before": "def bind_closed_phase_evidence(path, expected_sha, *, binding, repo, used):",
          "after": "def bind_legacy_closed_phase_evidence(path, expected_sha, *, binding, repo, used):"
        },
        {
          "before": "\ndef parse_original_command(driver, record, command_path, repo, used):",
          "after": "\ndef load_R723_closed_source(repo,used):\n    root=Path(repo).resolve()/TOPIC/SCRIPT\n    path=root/R723_CLOSED_SOURCE_NAME\n    record=used.add(path)\n    if record[\"sha256\"]!=R723_CLOSED_SOURCE_SHA:\n        raise ValueError(\"Use the exact complete independent R723 evidence producer\")\n    module=load(\"_mesh_complete_independent_R723_closed\",path,R723_CLOSED_SOURCE_SHA)\n    if (module.SCHEMA!=R723_CLOSED_SCHEMA\n            or module.PARENT!=(CLOSED_SOURCE_NAME,CLOSED_SOURCE_SHA)\n            or module.GEOMETRY[1]!=GEOMETRY_SHA\n            or module.R723!=R723_THEOREM):\n        raise ValueError(\"The complete R723 source family or theorem changed\")\n    for name in (\"validate_complete_report\",\"load_environment\",\"bind_geometry\",\n            \"preview_directional\",\"second_pass_directional\",\"unmarked_body_interpretation\",\n            \"build_field_cover\",\"directional_instantiation\"):\n        if sha(getattr(module,name).__code__.co_filename)!=R723_CLOSED_SOURCE_SHA:\n            raise ValueError(\"A complete R723 evidence function was replaced\")\n    used.verify(record)\n    return module,record\n\n\ndef bind_R723_closed_phase_evidence(path,expected_sha,*,binding,repo,used):\n    \"\"\"Read a distinct complete R723 proof for the actual selected mesh point.\n\n    All accurate field claims remain separate from numerical mesh word error.\n    The complete original 002eb branch is not weakened or relabelled here.\n    \"\"\"\n    path=Path(path).resolve()\n    main_record=used.add(path)\n    if expected_sha is not None and main_record[\"sha256\"]!=expected_sha:\n        raise ValueError(\"The explicitly expected complete R723 main report differs\")\n    main=used.read_json(main_record)\n    if (main.get(\"schema\")!=R723_CLOSED_SCHEMA\n            or main.get(\"source_sha256\")!=R723_CLOSED_SOURCE_SHA\n            or main.get(\"complete\") is not True\n            or main.get(\"status\")!=\"complete-same-field-consumption\"\n            or main.get(\"all_bound_input_and_generated_evidence_bytes_rechecked\") is not True):\n        raise ValueError(\"An optional R723 sidecar needs its final complete rechecked main report\")\n    snapshot_record=binding.get(\"actual_snapshot_file\")\n    if snapshot_record is None or binding.get(\"actual_snapshot_identity_sha256\") is None:\n        raise ValueError(\"An R723 proof cannot borrow an unrecorded mesh-point snapshot\")\n    snapshot=used.read_json(snapshot_record)\n    snapshot_definition=snapshot[\"definition\"]\n    if (snapshot.get(\"snapshot_identity_sha256\")!=binding[\"actual_snapshot_identity_sha256\"]\n            or snapshot_definition.get(\"current_full_point_sha256\")!=binding[\"point_sha256\"]\n            or snapshot_definition.get(\"all_required_angle_roots_recorded\") is not True):\n        raise ValueError(\"Use the genuine complete required-angle snapshot of this mesh point\")\n    point_arrays=snapshot_definition[\"current_point_file\"][\"arrays_file\"]\n    used.verify(point_arrays)\n    identities=dict(actual_current_full_point_sha256=binding[\"point_sha256\"],\n        complete_original_model_identity_sha256=binding[\"model_identity_sha256\"],\n        exact_fixed_target_identity_sha256=binding[\"fixed_target_definition_identity_sha256\"],\n        actual_snapshot_identity_sha256=binding[\"actual_snapshot_identity_sha256\"])\n    for key,value in identities.items():\n        if main.get(key)!=value:\n            raise ValueError(\"The complete R723 report belongs to a different selected field: \"+key)\n    inventories={}\n    for name in (\"actual_complete_input_records\",\"generated_evidence_records\"):\n        records=main.get(name)\n        if not isinstance(records,list) or not records:\n            raise ValueError(\"Every original complete R723 input and generated output is required\")\n        found={}\n        for record in records:\n            original=used.verify(record)\n            if str(original) in found:\n                raise ValueError(\"An original complete R723 path is declared more than once\")\n            found[str(original)]=record\n        inventories[name]=found\n    def declared(record,kind):\n        actual=used.verify(record)\n        if inventories[kind].get(str(actual))!=record:\n            raise ValueError(\"The exact whole R723 record is absent from its final inventory\")\n        return record\n    closed,current_closed=load_R723_closed_source(repo,used)\n    checked=closed.validate_complete_report(repo,path,\n        expected_report_sha256=main_record[\"sha256\"])\n    if (checked.get(\"final_main_report\")!=main_record\n            or checked.get(\"complete_main_and_exact_sidecars_reread\") is not True\n            or checked.get(\"original_full_streams_and_normal32_and_domain_reread\") is not True\n            or checked.get(\"source_copies_checked_by_entire_SHA_and_bytes_with_original_paths_retained\") is not True\n            or checked.get(\"original_eight_role_beta_claims_not_fabricated\") is not True\n            or checked.get(\"all_bound_input_and_generated_output_bytes_rechecked\") is not True\n            or type(checked.get(\"new_F_J_root_or_integrand_calls\")) is not int\n            or checked[\"new_F_J_root_or_integrand_calls\"]!=0):\n        raise ValueError(\"The original complete R723 proof was not fully re-consumed\")\n    checked_identities=dict(\n        actual_current_full_point_sha256=binding[\"point_sha256\"],\n        actual_model_identity_sha256=binding[\"model_identity_sha256\"],\n        actual_snapshot_identity_sha256=binding[\"actual_snapshot_identity_sha256\"],\n        exact_fixed_target_identity_sha256=binding[\"fixed_target_definition_identity_sha256\"],\n        original_geometry_binding_identity_sha256=main[\"original_geometry_binding_identity_sha256\"])\n    for key,value in checked_identities.items():\n        if checked.get(key)!=value:\n            raise ValueError(\"The full R723 validator is not bound to this actual mesh field\")\n    source_files=main.get(\"source_files\")\n    proofs=main.get(\"proof_sources\")\n    if (source_files!=checked.get(\"complete_source_records\")\n            or proofs!=checked.get(\"complete_proof_records\")\n            or not isinstance(source_files,dict) or not source_files\n            or not isinstance(proofs,dict) or not proofs):\n        raise ValueError(\"Retain the complete original R723 source and proof maps\")\n    for record in list(source_files.values())+list(proofs.values()):\n        declared(record,\"actual_complete_input_records\")\n    root=Path(repo).resolve()/TOPIC/SCRIPT\n    producer_copy=same_source_copy(source_files[\"closed_phase_producer\"],\n        current_closed,used,R723_CLOSED_SOURCE_SHA)\n    runtime_copies={}\n    for role,current in binding[\"source_roles\"].items():\n        runtime_copies[role]=same_source_copy(source_files[\"runtime_\"+role],\n            current,used,current[\"sha256\"])\n    other_source_copies={}\n    for role,original in source_files.items():\n        if role.startswith(\"runtime_\"):\n            continue\n        current=used.add(root/Path(original[\"path\"]).name)\n        other_source_copies[role]=same_source_copy(original,current,used,original[\"sha256\"])\n    parent=load(\"_mesh_complete_R723_closed_algorithm_parent\",\n        root/CLOSED_SOURCE_NAME,CLOSED_SOURCE_SHA)\n    used.add(parent.__file__)\n    proof_copies={}\n    expected_proofs=dict(parent.PROOFS)\n    expected_proofs[\"R723_directional_flow\"]=R723_THEOREM\n    if set(proofs)!=set(expected_proofs):\n        raise ValueError(\"Keep every original complete theorem and source-specific port proof\")\n    for role,(relative,digest) in expected_proofs.items():\n        proof_copies[role]=same_source_copy(proofs[role],\n            used.add(Path(repo).resolve()/relative),used,digest)\n    geometry_record=declared(main[\"geometry_report\"],\"actual_complete_input_records\")\n    geometry=used.read_json(geometry_record)\n    if (geometry.get(\"schema\")!=GEOMETRY_SCHEMA or geometry.get(\"source_sha256\")!=GEOMETRY_SHA\n            or any(geometry.get(key) is not True for key in\n                (\"complete\",\"all_input_and_output_bytes_rechecked\",\"full_upper_cover_processed\",\n                 \"continuous_curvature_bound_complete\",\"continuous_support_numerator_bounds_complete\"))):\n        raise ValueError(\"The R723 proof did not consume the complete same-field upper geometry\")\n    geometry_binding_record=declared(geometry[\"complete_binding\"],\"actual_complete_input_records\")\n    geometry_binding=used.read_json(geometry_binding_record)\n    if (canonical(geometry_binding)!=geometry[\"complete_binding_identity_sha256\"]\n            or canonical(geometry_binding)!=main[\"original_geometry_binding_identity_sha256\"]\n            or geometry_binding.get(\"complete_original_model\")!=binding[\"complete_model\"]\n            or geometry_binding.get(\"fixed_material_chart_identity_sha256\")!=binding[\"fixed_chart_core_sha256\"]\n            or geometry_binding.get(\"fixed_scalar_metric_identity_sha256\")!=\n                binding[\"fixed_scalar_metric\"][\"identity_sha256\"]\n            or geometry_binding.get(\"original_stage_count\")!=32\n            or geometry_binding.get(\"full_circle_without_symmetry_reduction\") is not True):\n        raise ValueError(\"The complete upper binding differs from the actual mesh field and target\")\n    for key,value in identities.items():\n        if geometry_binding.get(key)!=value:\n            raise ValueError(\"The actual upper and closed inputs select different full points\")\n    side_record=declared(main[\"R716_outward_tube_evidence\"],\"generated_evidence_records\")\n    if checked.get(\"R716_sidecar_record\")!=side_record:\n        raise ValueError(\"The exact final R723 sidecar record changed\")\n    side=used.read_json(side_record)\n    if (side!=checked.get(\"R716_independently_recomputed_sidecar\")\n            or side.get(\"schema\")!=R723_CLOSED_SCHEMA+\"-R716-unmarked-outward-tube\"\n            or side.get(\"source_sha256\")!=R723_CLOSED_SOURCE_SHA\n            or side.get(\"required_final_report_path\")!=str(path)\n            or side.get(\"final_complete_producer_report_required\") is not True\n            or side.get(\"intermediate_sidecar_without_final_complete_report_is_not_a_certificate\") is not True):\n        raise ValueError(\"An isolated or provisional R723 sidecar is not a complete same-field proof\")\n    normal_record=declared(side[\"original_complete_normal_report\"],\"actual_complete_input_records\")\n    if geometry.get(\"normal_report\")!=normal_record:\n        raise ValueError(\"The geometry and R723 sidecar use different complete original normal reports\")\n    normal=used.read_json(normal_record)\n    if (normal.get(\"source_sha256\")!=R723_NORMAL_FEE_SOURCE_SHA\n            or normal.get(\"complete\") is not True\n            or normal.get(\"all_planned_original_stages_and_sixjet_streams_complete\") is not True\n            or normal.get(\"all_bound_input_and_output_bytes_rechecked_at_final_report\") is not True):\n        raise ValueError(\"The complete original normal32 and physical-stream result is required\")\n    normal_binding_record=declared(normal[\"complete_binding\"],\"actual_complete_input_records\")\n    request_record=declared(normal[\"complete_input_and_request\"],\"actual_complete_input_records\")\n    normal_binding=used.read_json(normal_binding_record)\n    request=used.read_json(request_record)\n    actual=normal[\"actual_input\"][\"binding\"]\n    actual_identity=canonical(actual)\n    if (normal[\"actual_input\"][\"binding_identity_sha256\"]!=actual_identity\n            or normal_binding.get(\"actual_complete_input\")!=actual\n            or request.get(\"actual_complete_input\")!=actual\n            or canonical(normal_binding)!=normal[\"complete_binding_identity_sha256\"]\n            or canonical(normal_binding)!=checked[\"original_normal_binding_identity_sha256\"]\n            or canonical(request)!=normal[\"complete_input_and_request_identity_sha256\"]):\n        raise ValueError(\"The full original normal/request/actual-field bindings changed\")\n    comparisons={\n        \"current_full_point_sha256\":binding[\"point_sha256\"],\n        \"model_identity_sha256\":binding[\"model_identity_sha256\"],\n        \"actual_snapshot_identity_sha256\":binding[\"actual_snapshot_identity_sha256\"],\n        \"actual_snapshot_file\":snapshot_record,\n        \"current_point_arrays_file\":point_arrays,\n        \"complete_model\":binding[\"complete_model\"],\n        \"exact_fixed_target_identity_sha256\":binding[\"fixed_target_definition_identity_sha256\"],\n        \"mathematical_target_identity_sha256\":binding[\"mathematical_target_identity_sha256\"],\n        \"fixed_chart_core_sha256\":binding[\"fixed_chart_core_sha256\"],\n        \"fixed_scalar_metric_identity_sha256\":binding[\"fixed_scalar_metric\"][\"identity_sha256\"],\n        \"complete_actual_fixed_reference_input_binding\":binding[\"complete_actual_fixed_reference_input_binding\"],\n        \"complete_six_actual_inputs\":binding[\"complete_six_actual_inputs\"],\n        \"actual_driver_sha256\":DRIVER_SHA,\"complete_pure_reader_sha256\":READER_SHA}\n    for key,value in comparisons.items():\n        if actual.get(key)!=value:\n            raise ValueError(\"The accurate normal field and mesh point differ: \"+key)\n    outer_record=declared(actual[\"scientific_report\"],\"actual_complete_input_records\")\n    if normal.get(\"actual_report\")!=outer_record:\n        raise ValueError(\"The original accurate scientific report record changed\")\n    outer=used.read_json(outer_record)\n    if (outer.get(\"source_sha256\")!=DRIVER_SHA\n            or outer.get(\"source_commit\")!=binding[\"actual_source_commit\"]\n            or outer.get(\"github_run_id\")!=binding[\"actual_scientific_run_id\"]\n            or outer.get(\"workflow_trigger_commit\")!=binding[\"actual_workflow_trigger_commit\"]\n            or outer.get(\"representation\")!=binding[\"complete_model\"]\n            or outer.get(\"coordinate_norm\")!=binding[\"complete_original_coordinate_norm\"]\n            or outer.get(\"working_evaluation\")!=binding[\"complete_original_working_evaluation\"]\n            or outer.get(\"fixed_scalar_metric\")!=binding[\"fixed_scalar_metric\"]\n            or outer.get(\"actual_fixed_reference_input_binding\")!=binding[\"complete_actual_fixed_reference_input_binding\"]\n            or sum(item.get(\"snapshot_identity_sha256\")==binding[\"actual_snapshot_identity_sha256\"]\n                and item.get(\"snapshot_file\")==snapshot_record\n                and item.get(\"summary\",{}).get(\"all_required_angle_roots_recorded\") is True\n                for item in outer.get(\"normal_root_packets\",{}).get(\"snapshots\",[]))!=1):\n        raise ValueError(\"The normal and mesh reports lack the same complete actual scientific attribution\")\n    for key,value in {\n        \"current_full_point_sha256\":binding[\"point_sha256\"],\n        \"complete_model_identity_sha256\":binding[\"model_identity_sha256\"],\n        \"actual_current_full_point_sha256\":binding[\"point_sha256\"],\n        \"actual_model_identity_sha256\":binding[\"model_identity_sha256\"],\n        \"actual_snapshot_identity_sha256\":binding[\"actual_snapshot_identity_sha256\"],\n        \"exact_fixed_target_identity_sha256\":binding[\"fixed_target_definition_identity_sha256\"],\n        \"complete_actual_input_identity_sha256\":actual_identity,\n        \"complete_original_normal_binding_identity_sha256\":canonical(normal_binding),\n        \"actual_complete_model\":binding[\"complete_model\"],\n        \"actual_complete_point_arrays\":point_arrays,\"actual_complete_snapshot\":snapshot_record,\n        \"original_complete_normal_binding\":normal_binding_record,\n        \"original_complete_normal_input_and_request\":request_record,\n        \"complete_geometry_report\":geometry_record,\n        \"complete_binding_identity_sha256\":canonical(geometry_binding),\n        \"complete_geometry_binding_identity_sha256\":canonical(geometry_binding),\n        \"original_stage_count\":32,\"whole_circle_phi_over_pi\":[\"0\",\"2\"],\n    }.items():\n        if side.get(key)!=value:\n            raise ValueError(\"The full R723 main/normal/sidecar relationship changed: \"+key)\n    directional=checked.get(\"R723_evidence_available\") is True\n    if directional and (main.get(\"all_R723_directional_evidence_roles_paid\") is not True\n            or main.get(\"complete_closed_C2_immersion_certified\") is not True\n            or main.get(\"all_physical_phases_C2_continuous\") is not True\n            or main.get(\"all_physical_phases_embedded\") is not True\n            or main.get(\"outward_orientation_certified\") is not True\n            or F(checked[\"R723_reach_lower\"])<=0\n            or main.get(\"R723_directional_reach_lower\")!=str(checked[\"R723_reach_lower\"])):\n        raise ValueError(\"The distinct complete R723 all-phase conclusions changed\")\n    if (main.get(\"all_eight_original_beta_evidence_roles_paid\") is not False\n            or main.get(\"actual_outward_beta_package\") is not None):\n        raise ValueError(\"The independent R723 branch cannot fabricate old eight-role claims\")\n    claim_keys=(\"complete_closed_C2_immersion_certified\",\"all_physical_phases_C2_continuous\",\n        \"all_physical_phases_embedded\",\"outward_orientation_certified\",\n        \"complete_closed_geometry_certified\",\"all_phase_relative_Gram_standard_sufficient\",\n        \"reach_standard_sufficient\",\"grip_size_standard_sufficient\",\n        \"delta_hold_standard_sufficient\",\"delta_hold_stronger_target_sufficient\",\n        \"unmarked_all_phase_embedding_certified\",\n        \"R716_body_and_twelve_moment_additivity_interpretation_certified\")\n    for key in claim_keys:\n        if main.get(key) is not True and main.get(key) is not False and main.get(key) is not None:\n            raise ValueError(\"Preserve paid, insufficient and unavailable accurate claims distinctly\")\n    body_paid=(directional\n        and side[\"unmarked_all_phase_embedding_and_outwardness_certified\"] is True\n        and side[\"mark_height_strictly_below_unmarked_reach\"] is True\n        and side[\"R716_volume_and_all_twelve_raw_moment_additivity_interpretation_certified\"] is True)\n    used.verify(main_record)\n    used.verify(side_record)\n    used.recheck()\n    return dict(schema=R723_EVIDENCE_SCHEMA,provided=True,\n        route=\"independent-complete-R723-directional-proof\",\n        complete_same_point_evidence_bound=True,final_main_report=main_record,\n        exact_closed_source_copy=producer_copy,complete_runtime_source_copies=runtime_copies,\n        complete_other_source_copies=other_source_copies,complete_proof_source_copies=proof_copies,\n        original_geometry_report=geometry_record,complete_geometry_binding=geometry_binding_record,\n        original_geometry_binding_identity_sha256=canonical(geometry_binding),\n        original_complete_normal_report=normal_record,\n        original_complete_normal_binding=normal_binding_record,\n        original_complete_normal_binding_identity_sha256=canonical(normal_binding),\n        original_complete_normal_input_and_request=request_record,\n        original_accurate_scientific_report=outer_record,\n        mesh_scientific_report_capture=binding[\"scientific_report_capture\"],\n        original_scientific_report_paths_preserved=True,\n        different_report_versions_never_substitute_for_same_point_and_full_binding=True,\n        original_complete_normal_binding_checked=True,\n        original_full_streams_and_normal32_and_domain_reread=True,\n        complete_R723_directional_evidence_roles_paid=directional,\n        R723_directional_reach_lower=(str(checked[\"R723_reach_lower\"]) if directional else None),\n        R718_actual_marked_sigma=(str(checked[\"R718_actual_marked_sigma\"]) if directional else None),\n        independent_unmarked_tube_and_additivity_paid=body_paid,\n        original_eight_role_beta_claimed=False,original_R650_target_pass_required=False,\n        complete_R723_validation=closed.encoded(checked),outward_tube_sidecar=side_record,\n        complete_original_input_record_count=len(main[\"actual_complete_input_records\"]),\n        complete_generated_evidence_record_count=len(main[\"generated_evidence_records\"]),\n        same_field_identity=identities,accurate_field_claims={key:main.get(key) for key in claim_keys},\n        original_remaining_responsibilities=main.get(\"remaining\"),\n        all_original_records_rechecked=True,working_mesh_word_error_bound_supplied=False,\n        evidence_scope=\"accurate same-snapshot field; numerical meshes remain unproved working approximations\",\n        new_F_J_root_or_integrand_calls_for_evidence=0,\n        numerical_mesh_or_original_solver_admission_gate=False)\n\n\ndef bind_closed_phase_evidence(path,expected_sha,*,binding,repo,used):\n    \"\"\"Exact whole-source dispatch, preserving the full legacy and absent routes.\"\"\"\n    if path is None:\n        return bind_legacy_closed_phase_evidence(path,expected_sha,\n            binding=binding,repo=repo,used=used)\n    record=used.add(path)\n    if expected_sha is not None and record[\"sha256\"]!=expected_sha:\n        raise ValueError(\"The requested optional closed main report differs\")\n    main=used.read_json(record)\n    if (main.get(\"schema\")==R723_CLOSED_SCHEMA\n            and main.get(\"source_sha256\")==R723_CLOSED_SOURCE_SHA):\n        return bind_R723_closed_phase_evidence(path,expected_sha,\n            binding=binding,repo=repo,used=used)\n    return bind_legacy_closed_phase_evidence(path,expected_sha,\n        binding=binding,repo=repo,used=used)\n\n\ndef parse_original_command(driver, record, command_path, repo, used):"
        },
        {
          "before": "All numerical construction and field calls are public-Actions only.\n",
          "after": "All numerical construction and field calls are public-Actions only.\nThe independent optional R723 route re-consumes its complete accurate evidence;\nlegacy 002eb and no-evidence behavior are retained without altered claims.\n"
        }
      ]
    },
    {
      "role": "main",
      "parent": {
        "kind": "complete_runtime_source",
        "name": "fixed_fejer_meridian_batched_producer_bound_complete_same_field_phase_meshes.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_bound_complete_same_field_phase_meshes.py",
        "bytes": 53829,
        "sha256": "b3991da8585b553a6c3133da806fafa4903e2c01087634c18ee168e6718bc4d7",
        "git_blob_sha": "e691ac03f470b3d5477525b8f8c38007741a8747"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_phase_meshes.py",
        "name": "fixed_fejer_R723_compatible_same_field_phase_meshes.py",
        "bytes": 55097,
        "sha256": "f2a46875aaa230f24cfcb92011997aa6b3fa7a7caf985701e02461229e0057f2",
        "git_blob_sha": "be361ed47846be988c252aa049d1a57b68bfec47"
      },
      "exact_ordered_text_patches": [
        {
          "before": "SCHEMA = \"actual-fixed-fejer-meridian-batched-producer-bound-complete-same-field-closed-phase-mesh-refinement-v1\"",
          "after": "SCHEMA = \"actual-fixed-fejer-R723-compatible-meridian-batched-producer-bound-complete-same-field-closed-phase-mesh-refinement-v1\""
        },
        {
          "before": "    \"mesh_input\": [\n        \"scripts/resume_20261126/fixed_fejer_meridian_batched_producer_bound_same_field_mesh_input.py\",\n        \"2ef316b9075f14af66e1deda235c4df9319a0c29cfeddb10a40130712a12d76c\"\n    ]",
          "after": "    \"mesh_input\": [\n        \"scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_mesh_input.py\",\n        \"6c678893db4cff3366a0836ee900e67aabd23b5267768369d6bfa41479197aa8\"\n    ]"
        },
        {
          "before": "    \"optional_closed_phase_source\": [\n        \"scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py\",\n        \"002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f\"\n    ]\n}",
          "after": "    \"optional_closed_phase_source\": [\n        \"scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py\",\n        \"002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f\"\n    ],\n    \"optional_R723_closed_phase_source\": [\n        \"scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py\",\n        \"1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc\"\n    ],\n    \"optional_R723_directional_theorem\": [\n        \"results/R723-directional-normal-flow-support-reach.md\",\n        \"0edbd1039706186d07412a53c8e5c10411c5966dc36e38a7a504cf923d43e7eb\"\n    ]\n}"
        },
        {
          "before": "    return answer\n\n\ndef main():",
          "after": "    answer.update(\n        optional_closed_evidence_route=closed.get(\"route\",\n            \"original-complete-002eb-R722\" if closed.get(\"provided\") else None),\n        optional_R723_directional_evidence_paid=closed.get(\"complete_R723_directional_evidence_roles_paid\"),\n        optional_R723_normal_binding_checked=closed.get(\"original_complete_normal_binding_checked\",False),\n        optional_R723_full_original_domain_reread=closed.get(\"original_full_streams_and_normal32_and_domain_reread\",False),\n        optional_R723_reach_lower=closed.get(\"R723_directional_reach_lower\"),\n        optional_R723_marked_sigma=closed.get(\"R718_actual_marked_sigma\"),\n        optional_R723_independent_unmarked_tube_paid=closed.get(\"independent_unmarked_tube_and_additivity_paid\"),\n        optional_R723_old_eight_role_claimed=closed.get(\"original_eight_role_beta_claimed\"))\n    return answer\n\n\ndef main():"
        }
      ]
    },
    {
      "role": "reader",
      "parent": {
        "kind": "complete_runtime_source",
        "name": "read_fixed_fejer_meridian_batched_producer_bound_same_field_phase_mesh_report.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_meridian_batched_producer_bound_same_field_phase_mesh_report.py",
        "bytes": 22184,
        "sha256": "8197f77d1372710931ba6882c9fd88f035154a7082310bfdfa645865cde3e5c2",
        "git_blob_sha": "16fb78089178ebd50a925239d179c40588fa90bd"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py",
        "name": "read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py",
        "bytes": 22349,
        "sha256": "5d47382428fb551a5f6bbaa61fd56191922bc793963a0cbb6af45914c126d813",
        "git_blob_sha": "6fb32e6f51c30796a3e558eca38cf96fd4be7c8f"
      },
      "exact_ordered_text_patches": [
        {
          "before": "SCHEMA = \"actual-fixed-fejer-meridian-batched-producer-bound-complete-same-field-closed-phase-mesh-refinement-v1\"",
          "after": "SCHEMA = \"actual-fixed-fejer-R723-compatible-meridian-batched-producer-bound-complete-same-field-closed-phase-mesh-refinement-v1\""
        },
        {
          "before": "MAIN_NAME = \"fixed_fejer_meridian_batched_producer_bound_complete_same_field_phase_meshes.py\"",
          "after": "MAIN_NAME = \"fixed_fejer_R723_compatible_same_field_phase_meshes.py\""
        },
        {
          "before": "MAIN_SHA = \"b3991da8585b553a6c3133da806fafa4903e2c01087634c18ee168e6718bc4d7\"",
          "after": "MAIN_SHA = \"f2a46875aaa230f24cfcb92011997aa6b3fa7a7caf985701e02461229e0057f2\""
        },
        {
          "before": "if len(source_pins)!=144:",
          "after": "if len(source_pins)!=146:"
        },
        {
          "before": "Keep all 137 scientific roles and seven mesh/input/evidence source roles",
          "after": "Keep all 137 scientific roles and nine mesh/input/evidence source roles"
        },
        {
          "before": "This reader imports only stdlib-level mesh/input modules and the original\nsource-bound pure report reader. It never constructs q, calls F/J/root,\nresolves a chart, creates a mesh, or recomputes a numerical criterion.",
          "after": "The original numerical mesh checks and original source-bound report reader\nare retained. Optional R723 evidence invokes its full accurate-data validator,\nincluding complete NPZ word reads and rational full-domain evidence arithmetic.\nIt never constructs q, calls F/J/root, resolves a chart, creates a mesh, or\nrecomputes a numerical mesh criterion. No supplied proof pays working mesh error."
        }
      ]
    }
  ],
  "source_scope": "complete text only; no source or numerical gate is added to the solver"
}''')


def checked_read(repo,record):
    path=(repo/record["path"]).resolve()
    if repo not in path.parents:
        raise ValueError("Keep the exact complete parent below the selected repository")
    raw=path.read_bytes()
    if len(raw)!=record["bytes"] or hashlib.sha256(raw).hexdigest()!=record["sha256"]:
        raise ValueError("The whole immutable source parent differs: "+record["path"])
    return raw.decode("utf-8")


def exact_replace(text,before,after,label):
    if text.count(before)!=1:
        raise ValueError("A complete source patch must have one exact anchor: "+label)
    return text.replace(before,after,1)


def construct(parent,item):
    text=parent
    patches=item["exact_ordered_text_patches"]
    for i,patch in enumerate(patches):
        text=exact_replace(text,patch["before"],patch["after"],
            item["role"]+":"+str(i))
    result=text.encode("utf-8")
    output=item["output"]
    if len(result)!=output["bytes"] or hashlib.sha256(result).hexdigest()!=output["sha256"]:
        raise ValueError("The complete derived source differs: "+output["name"])
    reverse=text
    for i,patch in reversed(list(enumerate(patches))):
        reverse=exact_replace(reverse,patch["after"],patch["before"],
            item["role"]+":inverse:"+str(i))
    if reverse!=parent:
        raise ValueError("The source derivation is not byte-exactly reversible")
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--output-directory",type=Path,required=True)
    args=p.parse_args()
    repo=args.repo.resolve()
    out=args.output_directory.resolve()
    if out==repo or repo in out.parents:
        raise ValueError("Use a distinct source-construction directory outside the repository")
    results=[]
    for item in SPEC["complete_parents_and_outputs"]:
        parent=checked_read(repo,item["parent"])
        raw=construct(parent,item)
        target=out/item["output"]["name"]
        if target.parent!=out:
            raise ValueError("Keep the complete output basename")
        if target.exists() and target.read_bytes()!=raw:
            raise FileExistsError("Preserve an existing different source: "+str(target))
        results.append((target,raw,item["output"]))
    out.mkdir(parents=True,exist_ok=True)
    for target,raw,record in results:
        if not target.exists():
            target.write_bytes(raw)
    print(json.dumps(dict(
        schema=SPEC["schema"],
        complete_source_outputs=[record for _,_,record in results],
        exact_complete_parent_text_retained=True,
        mathematical_runtime_executed=False,
        AST_or_compilation_executed=False,
        admission_gate_added=False),indent=2))


if __name__=="__main__":
    main()
