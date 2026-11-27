// Complete exact text transformations; no scientific evaluation.
// Every parent and every output is independently whole-byte pinned.
export const specifications = {
 "transfer": {
  "parent": {
   "path": "scripts/resume_20261126/frequency_refined_public_reference_history_transfer.py",
   "sha256": "fdc29a36ca562cec8327a2ca250ecdd3a505827415617255993b6fcab5389279",
   "bytes": 82084
  },
  "output": {
   "name": "radial_refined_public_reference_history_transfer.py",
   "bytes": 86470,
   "sha256": "2720bd9033391fc3f0a48afe33f50ea5843b2bf225a6596ee5a5b7077819e55c"
  },
  "patches": [
   [
    1502,
    1680,
    "SCHEMA = 'strict-public09-M160-to-M320-complete-material-history-transfer-v1'\nANALYTIC_BINDING_SOURCE_SHA256 = 'a62e122d32b5a8faa7e1dee82e8f8855c40c1f2d8a1bceeb14a298a6512ba931'\n",
    "SCHEMA = 'strict-public09-J923-to-J1845-complete-material-history-transfer-v1'\nANALYTIC_BINDING_SOURCE_SHA256 = '5b50b02aea139b81e7e1ed3cbf37c4ad8870d182c63d48bf648fb197e1cf3734'\n"
   ],
   [
    1770,
    1868,
    "CURRENT_MEMORY_SOURCE_SHA256 = '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'\n",
    "CURRENT_MEMORY_SOURCE_SHA256 = '6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a'\nORIGINAL_CURRENT_MEMORY_SOURCE_SHA256 = '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'\nRADIAL_ADDRESS_SOURCE_SHA256 = '6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716'\n"
   ],
   [
    1981,
    2071,
    "LAYOUT_SOURCE_SHA256 = 'ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27'\n",
    "LAYOUT_SOURCE_SHA256 = 'cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744'\n"
   ],
   [
    8170,
    8451,
    "        frequency_layout_source_sha256=LAYOUT_SOURCE_SHA256,reference_M=160,current_M=320,J=923,full_N=2048,\n        complete_fixed_target_reference_seed_mesh_observer_Q_gamma_partition_retained=True,\n        three_unequal_rotation_blocks_copied_with_explicit_new_zero_modes=True,\n",
    "        radial_layout_source_sha256=LAYOUT_SOURCE_SHA256,reference_J=923,current_J=1845,M=160,full_N=2048,\n        radial_address_source_sha256=RADIAL_ADDRESS_SOURCE_SHA256,\n        complete_fixed_target_reference_seed_Q_gamma_partition_and_frequency_space_retained=True,\n        current_observation_and_norm_definition_explicitly_refined=True,\n        all_three_rotation_blocks_and_all_original_radial_node_words_retained=True,\n        new_midpoint_shared_quintic_jets_explicit_and_free=True,\n        exact_affine_material_addresses_verified_in_original_and_current_coordinates=True,\n        working_midpoint_coefficient_error_enclosed=False,\n"
   ],
   [
    9576,
    9644,
    "        original_memory_math_history_scans_and_rows_unchanged=True,\n",
    "        original_physical_screen_and_typed_families_retained_with_exact_radial_address_transfer=True,\n"
   ],
   [
    10039,
    10335,
    "        all_original_reference_base_chart_carrier_and_envelope_policy_must_match=True,\n        changed_model_fields='complete declared M160-to-M320 free layout, exact dependent frozen-point identities, source/schema and fully bound unchanged matrix policies; fixed target and observer retained',\n",
    "        whole_original_reference_chart_carriers_and_independent_target_must_match=True,\n        changed_model_fields='complete J923-to-J1845 free-jet inclusion, exact-affine reference queries, complete refined observation/norm/calibration and current sources; the full original target/seed/M/N/Q/gamma/partition stay fixed',\n"
   ],
   [
    11300,
    11301,
    "\n",
    ""
   ],
   [
    12359,
    12403,
    "            or not 0 <= int(value[0]) < 922\n",
    "            or not 0 <= int(value[0]) < 1844\n"
   ],
   [
    15832,
    15922,
    "    path=Path(__file__).with_name('frequency_refined_public_reference_source_binding.py')\n",
    "    path=Path(__file__).with_name('radial_refined_public_reference_source_binding.py')\n"
   ],
   [
    17719,
    17930,
    "    if (q.M!=320 or q.n!=962 or q.J!=923 or q.full_N!=2048 or q.N!=513\n            or q.base.reference_M!=160):\n        raise ValueError('Use the exact M320 current layout with the frozen M160/N2048 reference')\n",
    "    if (q.M!=160 or q.n!=482 or q.J!=1845 or q.full_N!=2048 or q.N!=513\n            or q.base.reference_J!=923):\n        raise ValueError('Use the exact J1845 current layout with the frozen J923/M160/N2048 reference')\n"
   ],
   [
    19692,
    19692,
    "",
    "    radial_bridge=_radial_addresses()\n    radial_layout=q.base.radial_layout_definition\n    original_memory=_original_memory()\n"
   ],
   [
    21878,
    22056,
    "    expected_memory=(CURRENT_MEMORY_SOURCE_SHA256 if independent else\n        restart.get('material_envelope',{}).get('source_sha256') if restart is not None else parent_memory)\n",
    "    expected_memory=CURRENT_MEMORY_SOURCE_SHA256\n"
   ],
   [
    22099,
    22181,
    "            or (parent_memory is not None and parent_memory!=actual_memory_sha)):\n",
    "            or (parent_memory is not None and parent_memory!=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256)\n            or (restart is not None and restart.get('material_envelope',{}).get('source_sha256')!=actual_memory_sha)):\n"
   ],
   [
    22464,
    22519,
    "        if family['memory_sha256']!=actual_memory_sha:\n",
    "        if family['memory_sha256']!=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256:\n"
   ],
   [
    22981,
    23056,
    "                or payload.get('N') != q.full_N or payload.get('J') != q.J\n",
    "                or payload.get('N') != q.full_N or payload.get('J') != 923\n"
   ],
   [
    23097,
    23210,
    "                or payload.get('original_variables') != q.base.frequency_layout_definition['original_free_size']\n",
    "                or payload.get('original_variables') != q.base.radial_layout_definition['original_free_size']\n"
   ],
   [
    23878,
    23974,
    "        memory.validate_report_metadata(actual,model_identity=payload['model_identity_sha256'],\n",
    "        original_memory.validate_report_metadata(actual,model_identity=payload['model_identity_sha256'],\n"
   ],
   [
    27219,
    27275,
    "        locations = history.Locations(q.J,q.P,q.full_N)\n",
    "        locations = history.Locations(923,7377,2048)\n"
   ],
   [
    27703,
    27703,
    "",
    "        mapped_arrays=radial_bridge.map_arrays(old_arrays,radial_layout,source_J=923)\n"
   ],
   [
    27738,
    27822,
    "            if not {_point(row) for row in old_arrays[role]} <= current_sets[role]:\n",
    "            if not {_point(row) for row in mapped_arrays[role]} <= current_sets[role]:\n"
   ],
   [
    27988,
    27988,
    "",
    "        mapped_rows=[radial_bridge.transfer_typed_row(row,radial_layout,source_J=923) for row in rows]\n"
   ],
   [
    28672,
    28672,
    "",
    "            complete_mapped_role_arrays=copy.deepcopy(mapped_arrays),\n            actual_mapped_role_fingerprints=_address_fingerprints(mapped_arrays),\n            complete_mapped_typed_rows=copy.deepcopy(mapped_rows),\n"
   ],
   [
    29365,
    29409,
    "        for ordinal,row in enumerate(rows):\n",
    "        for ordinal,old_row in enumerate(rows):\n            row=mapped_rows[ordinal]\n"
   ],
   [
    29896,
    29960,
    "                complete_original_typed_row=copy.deepcopy(row))\n",
    "                complete_original_typed_row=copy.deepcopy(old_row),\n                original_typed_core_sha256=_typed_key(old_row),\n                radial_layout_identity_sha256=canonical(radial_layout),\n                original_and_current_material_coordinates_exactly_equal=True)\n"
   ],
   [
    33440,
    33479,
    "        reference_M=160,current_M=320,\n",
    "        reference_J=923,current_J=1845,\n"
   ],
   [
    34115,
    34216,
    "            'strict-current-target-terminal-transfer' if parent_memory==CURRENT_MEMORY_SOURCE_SHA256\n",
    "            'strict-current-target-terminal-transfer' if parent_memory==ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256\n"
   ],
   [
    36182,
    36183,
    "\n",
    ""
   ],
   [
    41638,
    41733,
    "    if (not same(arrays['mesh'],q.mesh) or not same(arrays['fixed_parent_core'],q.parent_core)\n",
    "    if (not same(arrays['mesh'],q.base.reference_mesh) or not same(arrays['fixed_parent_core'],q.parent_core)\n"
   ],
   [
    41899,
    41989,
    "    flat=arrays['omega_jets'].reshape(3*q.J,482)\n    zero_slots=[0,3*(q.J-1),3*(q.J-1)+1]\n",
    "    flat=arrays['omega_jets'].reshape(3*923,482)\n    zero_slots=[0,3*922,3*922+1]\n"
   ],
   [
    42128,
    42293,
    "    old=np.r_[arrays['core'][q.K:],flat[q.radial_free].ravel(),float(arrays['Hcap'])]\n    if old.shape!=(q.base.frequency_layout_definition['original_free_size'],):\n",
    "    old=np.r_[arrays['core'][q.K:],flat[np.asarray(q.base.radial_layout_definition['original_free_radial_slots'],dtype=int)].ravel(),float(arrays['Hcap'])]\n    if old.shape!=(q.base.radial_layout_definition['original_free_size'],):\n"
   ],
   [
    42704,
    42790,
    "    result,inclusion=module.embed_outer_words(old,q.base.frequency_layout_definition)\n",
    "    result,inclusion=module.embed_outer_shared_quintic_words(old,q.base.radial_layout_definition,\n        q.base.radial_carriers['original_width_carriers'])\n"
   ],
   [
    42829,
    43126,
    "    if (not same(core[:160],arrays['core']) or np.any(core[160:]!=0)\n            or not same(omega[:,:,:161],arrays['omega_jets'][:,:,:161])\n            or not same(omega[:,:,321:482],arrays['omega_jets'][:,:,161:322])\n            or not same(omega[:,:,642:802],arrays['omega_jets'][:,:,322:482])\n",
    "    if (not same(core,arrays['core']) or omega.shape!=(1845,3,482)\n            or not same(omega[::2],arrays['omega_jets'])\n"
   ],
   [
    43185,
    43547,
    "        raise ValueError('Reconstruct all three correctly offset odd-sine/odd-cosine/even-sine blocks and the complete core/H')\n    used=np.zeros(962,dtype=bool);used[:161]=True;used[321:482]=True;used[642:802]=True\n    if np.any(omega[:,:,~used]!=0):\n        raise ValueError('Every added rotation mode must be explicitly zero, never a copied old block alias')\n",
    "        raise ValueError('Keep every original SO3 node/three-jet/channel/core/H word in its exact current slot')\n"
   ],
   [
    43880,
    44041,
    "    record=dict(schema='actual-complete-M160-final-to-M320-zero-inclusion-v1',\n        mode='actual-complete-parent-zero-inclusion',source_sha256=sha(__file__),\n",
    "    record=dict(schema='actual-complete-J923-final-to-J1845-quintic-inclusion-v1',\n        mode='actual-complete-parent-quintic-inclusion',source_sha256=sha(__file__),\n"
   ],
   [
    44708,
    44747,
    "        reference_M=160,current_M=320,\n",
    "        reference_J=923,current_J=1845,\n"
   ],
   [
    45362,
    45432,
    "        all_original_variable_words_retained_and_new_modes_zero=True,\n",
    "        all_original_variable_words_retained_and_new_midpoint_jets_explicit=True,\n        working_quintic_restriction_rounding_enclosed=False,\n"
   ],
   [
    45827,
    45828,
    "\n",
    ""
   ],
   [
    46471,
    46636,
    "            or value.get('schema')!='actual-complete-M160-final-to-M320-zero-inclusion-v1'\n            or value.get('mode')!='actual-complete-parent-zero-inclusion'\n",
    "            or value.get('schema')!='actual-complete-J923-final-to-J1845-quintic-inclusion-v1'\n            or value.get('mode')!='actual-complete-parent-quintic-inclusion'\n"
   ],
   [
    47079,
    47155,
    "            or value.get('reference_M')!=160 or value.get('current_M')!=320\n",
    "            or value.get('reference_J')!=923 or value.get('current_J')!=1845\n"
   ],
   [
    47252,
    47373,
    "        raise ValueError('The actual coarse final inclusion must belong to this complete independently read M320 point')\n",
    "        raise ValueError('The actual coarse final inclusion must belong to this complete independently read J1845 point')\n"
   ],
   [
    47624,
    47728,
    "    for key in ('source_complete_field_read','all_original_variable_words_retained_and_new_modes_zero',\n",
    "    for key in ('source_complete_field_read','all_original_variable_words_retained_and_new_midpoint_jets_explicit',\n"
   ],
   [
    49314,
    49503,
    "    if (inclusion.get('layout_source_sha256')!=LAYOUT_SOURCE_SHA256\n            or inclusion.get('layout_identity_sha256')!=model['base_complete_model']['frequency_layout_identity_sha256']\n",
    "    if (inclusion.get('source_sha256')!=LAYOUT_SOURCE_SHA256\n            or inclusion.get('layout_identity_sha256')!=model['base_complete_model']['radial_layout_identity_sha256']\n"
   ],
   [
    49713,
    49932,
    "    layout_module=_module(Path(__file__).with_name('so3_frequency_refinement_layout.py'),LAYOUT_SOURCE_SHA256)\n    layout_module.validate_inclusion(inclusion,model['base_complete_model']['frequency_layout_definition'])\n",
    "    _radial_binding().validate_radial_inclusion(inclusion,\n        model['base_complete_model']['radial_layout_definition'],source_directory=Path(__file__).parent)\n    if value.get('working_quintic_restriction_rounding_enclosed') is not False:\n        raise ValueError('Actual midpoint-word injection is not an accurate coefficient certificate')\n"
   ],
   [
    50372,
    50470,
    "            or layout['J']!=923 or layout['n']!=962 or layout['K']!=3 or layout['core_size']!=317\n",
    "            or layout['J']!=1845 or layout['n']!=482 or layout['K']!=3 or layout['core_size']!=157\n"
   ],
   [
    50619,
    50719,
    "        raise ValueError('Keep the complete current M320 layout without treating M160 as its size')\n",
    "        raise ValueError('Keep the complete current J1845 layout without treating J923 as its size')\n"
   ],
   [
    51450,
    51451,
    "\n",
    ""
   ],
   [
    58443,
    58509,
    "                !=CURRENT_MEMORY_SOURCE_SHA256 for p in parents):\n",
    "                !=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256 for p in parents):\n"
   ],
   [
    59118,
    59180,
    "                or family['memory_sha256']!=actual_memory_sha\n",
    "                or family['memory_sha256']!=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256\n"
   ],
   [
    60525,
    60775,
    "                or binding.get('full_fixed_reference_chart_profile_seed_mesh_Q_gamma_partition_and_observer_equal') is not True\n                or binding.get('only_declared_current_frequency_layout_and_complete_source_policies_changed') is not True\n",
    "                or binding.get('full_fixed_reference_chart_profile_seed_Q_gamma_partition_and_frequency_space_equal') is not True\n                or binding.get('current_radial_quadrature_and_calibration_recomputed') is not True\n"
   ],
   [
    64507,
    64614,
    "            if origin.get('complete_original_typed_row')!=old_row or _typed_key(old_row)!=_typed_key(row):\n",
    "            mapped_old=_radial_addresses().transfer_typed_row(old_row,\n                model['base_complete_model']['radial_layout_definition'],source_J=923)\n            if (origin.get('complete_original_typed_row')!=old_row or _typed_key(mapped_old)!=_typed_key(row)\n                    or origin.get('original_typed_core_sha256')!=_typed_key(old_row)\n                    or origin.get('radial_layout_identity_sha256')!=model['base_complete_model']['radial_layout_identity_sha256']\n                    or origin.get('original_and_current_material_coordinates_exactly_equal') is not True):\n"
   ],
   [
    67005,
    67165,
    "        reference_M=160,current_M=320,full_N=2048,J=923,\n        fixed_target_observer_and_original_free_variables_retained=True,continuous_certificate=False)\n\n",
    "        reference_J=923,current_J=1845,full_N=2048,M=160,\n        fixed_target_and_all_original_free_variables_retained=True,\n        current_observation_and_norm_explicitly_refined=True,continuous_certificate=False)\n"
   ],
   [
    67198,
    67440,
    "    source=_original_memory()\n    cap=new.get('additional_current_near_active_rows')\n    if old!=new or new!=source.definition(cap):\n        raise ValueError('M-only inclusion preserves the entire actual envelope policy and near-active cap')\n",
    "    original=_original_memory()\n    if old!=original.definition(new.get('additional_current_near_active_rows')):\n        raise ValueError('Preserve the entire actual original policy and its original near-active cap')\n    current=_module(Path(__file__).with_name('radial_refined_public_reference_memory.py'),\n        CURRENT_MEMORY_SOURCE_SHA256)\n    if new!=current.definition(new.get('additional_current_near_active_rows')):\n        raise ValueError('Bind the whole explicitly new radial envelope policy')\n    for key in ('complete_original_free_variables_and_all_new_radial_jets_retained',\n            'fixed_target_and_full_objective_formula_unchanged',\n            'current_discrete_norm_and_positive_row_rule_explicitly_refined',\n            'original_J923_indices_resolved_before_exact_dyadic_transfer',\n            'current_native_grid_and_all_old_grids_preserved',\n            'discovered_typed_separation_rows_have_no_eviction_or_count_cap'):\n        if new.get(key) is not True:raise ValueError('A complete refinement responsibility is missing: '+key)\n"
   ],
   [
    67471,
    67759,
    "    source=_original_memory()\n    source._validate_grid(old['implicit_grid']);source._validate_grid(new['implicit_grid'])\n    if old['implicit_grid']!=new['implicit_grid']:\n        raise ValueError('M-only inclusion must retain every original/current radial and literal angular address')\n",
    "    original=_original_memory();original._validate_grid(old['implicit_grid'])\n    bridge=_radial_addresses()\n    ob,nb=old['historical_address_binding'],new['historical_address_binding']\n"
   ],
   [
    67812,
    68512,
    "        before,after=copy.deepcopy(old['historical_address_binding'][key]),copy.deepcopy(new['historical_address_binding'][key])\n        before['record'].pop('path');after['record'].pop('path')\n        if before!=after:raise ValueError('Retain the complete identical radial carriers')\n    old_target=old['historical_address_binding']['actual_path_binding']['fixed_target_definition']\n    new_target=new['historical_address_binding']['actual_path_binding']['fixed_target_definition']\n    if old_target!=new_target:\n        raise ValueError('A frequency inclusion cannot relabel another exact target')\n    return dict(full_N=2048,quarter_angles=513,J=923,\n        complete_old_current_grid_equal=True,\n",
    "        if ob[key]!=nb[key]:\n            raise ValueError('Keep both actual complete J923 carrier records and every member word')\n    old_target=ob['actual_path_binding']['fixed_target_definition']\n    if old_target!=nb['actual_path_binding']['fixed_target_definition']:\n        raise ValueError('Radial refinement retains the entire actually returned fixed target')\n    r=nb['radial_address_transfer'];layout=r['complete_radial_layout_definition']\n    old_current=original.read_carrier(ob['current_carrier']['record']['path'])\n    old_origin=original.read_carrier(ob['origin_carrier']['record']['path'])\n    fine=bridge.read_refined_plan(r['complete_observation_files'],r['complete_observation_definition'],\n        original_current=old_current)\n    old_words=set(old_current['radial_words'])|set(old_origin['radial_words'])\n    mapped=set(bridge.mapped_radial_words(old_words,layout))\n    union=set(fine['radial_words'])|mapped\n    og,ng=old['implicit_grid'],new['implicit_grid']\n    if (og.get('actual_phi_sha256')!=ng.get('actual_phi_sha256')\n            or og.get('angular_count')!=513 or ng.get('angular_count')!=513\n            or og.get('full_angular_count')!=2048 or ng.get('full_angular_count')!=2048\n            or canonical(sorted(old_words))!=og.get('union_radial_words_sha256')\n            or len(old_words)!=og.get('union_unique_radial_count')\n            or canonical(sorted(union))!=ng.get('union_radial_words_sha256')\n            or len(union)!=ng.get('union_unique_radial_count')\n            or canonical(layout)!=ng.get('current_radial_layout_identity_sha256')\n            or canonical(fine['definition'])!=ng.get('current_observation_identity_sha256')):\n        raise ValueError('Every actual old material point and angle must remain in the full fine union')\n    return dict(reference_J=923,current_J=1845,full_N=2048,M=160,\n        all_original_material_points_exactly_mapped=True,\n        old_radial_union_count=len(old_words),mapped_old_radial_union_count=len(mapped),\n        old_radial_union_sha256=canonical(sorted(old_words)),\n        mapped_old_radial_union_sha256=canonical(sorted(mapped)),\n        current_union_sha256=canonical(sorted(union)),\n"
   ],
   [
    68587,
    68737,
    "        complete_old_grid_identity_sha256=canonical(old['implicit_grid']),\n        complete_new_grid_identity_sha256=canonical(new['implicit_grid']))\n",
    "        complete_old_grid_identity_sha256=canonical(og),\n        complete_new_grid_identity_sha256=canonical(ng),\n        physical_value_or_quintic_rounding_identity_claimed=False)\n"
   ],
   [
    68738,
    68808,
    "def frequency_initial_record(args,q,x,*,transfer_record,seed_record):\n",
    "def radial_initial_record(args,q,x,*,transfer_record,seed_record):\n"
   ],
   [
    68895,
    69313,
    "    current=array_sha(x)\n    relation=transfer_record['frozen_original_point_relation']\n    if (array_sha(q.base.initial())!=relation['current_full_point_sha256']\n            or q.reference_point_sha256!=relation['current_full_point_sha256']):\n        raise ValueError('The reference seed cannot move when choosing the current M320 input point')\n    mode=transfer_record['current_invocation_memory_mode']\n    extra={}\n",
    "    current=array_sha(x);relation=transfer_record['frozen_original_point_relation']\n    if array_sha(q.base.initial())!=relation['current_full_point_sha256'] or q.reference_point_sha256!=relation['current_full_point_sha256']:\n        raise ValueError('The fixed reference cannot move when selecting a current fine point')\n    mode=transfer_record['current_invocation_memory_mode'];extra={}\n"
   ],
   [
    69345,
    69563,
    "        if current!=seed_record['current_full_point_sha256']:\n            raise ValueError('The complete included old final is not the actual first fine point')\n        selected='actual-complete-parent-zero-inclusion'\n",
    "        if current!=seed_record['current_full_point_sha256']:raise ValueError('Use the entire included actual final point')\n        selected='actual-complete-parent-quintic-inclusion'\n"
   ],
   [
    69772,
    69883,
    "        if mode!='same-source-restart':raise ValueError('Restart input and restored memory must be identical')\n",
    "        if mode!='same-source-restart':raise ValueError('The same-source point and history must match')\n"
   ],
   [
    70044,
    70616,
    "        if current!=relation['current_full_point_sha256']:\n            raise ValueError('Without a complete final or restart, use the full zero-included original reference point')\n        if mode=='explicit-independent-branch':selected='fresh-original-reference-zero-inclusion'\n        elif mode=='strict-current-target-terminal-transfer':selected='terminal-history-original-reference-zero-inclusion'\n        else:raise ValueError('Declare the actual fresh or terminal-history input mode')\n    return dict(schema='actual-public09-M320-input-point-and-fixed-reference-v1',\n",
    "        if current!=relation['current_full_point_sha256']:raise ValueError('Use the original zero-omega reference point')\n        if mode=='explicit-independent-branch':selected='fresh-original-reference-quintic-inclusion'\n        elif mode=='strict-current-target-terminal-transfer':selected='terminal-history-original-reference-quintic-inclusion'\n        else:raise ValueError('Declare the complete fresh or real-terminal-history mode')\n    return dict(schema='actual-public09-J1845-input-point-and-fixed-reference-v1',\n"
   ],
   [
    70701,
    70792,
    "        frequency_layout_identity_sha256=q.base.model['frequency_layout_identity_sha256'],\n",
    "        radial_layout_identity_sha256=q.base.radial_layout_identity,\n"
   ],
   [
    70856,
    71063,
    "        all_original_free_variables_retained=True,all_new_mode_initialization_explicit=True,\n        fixed_reference_seed_unchanged=True,\n        new_initial_field_roots_geometry_and_norm_require_read=True,\n",
    "        all_original_free_variables_retained=True,all_new_radial_jet_initialization_explicit=True,\n        fixed_reference_seed_unchanged=True,new_initial_field_roots_geometry_and_norm_require_read=True,\n"
   ],
   [
    71285,
    71328,
    "    name='_complete_M320_transfer_'+digest\n",
    "    name='_complete_J1845_transfer_'+digest\n"
   ],
   [
    71741,
    71779,
    "        CURRENT_MEMORY_SOURCE_SHA256)\n",
    "        ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256)\n"
   ],
   [
    73475,
    73861,
    "    \"\"\"Pure complete-source/file validation of every actual migrated lineage.\"\"\"\n    source=value.get('actual_current_driver_source',{})\n    _same_bytes(source)\n    if source.get('sha256')!=caller_source_sha256:\n        raise ValueError('Bind the actual caller source path before pure cross-M validation')\n    source_path=Path(source['path']).resolve()\n    topic=source_path.parents[2]\n",
    "    source=value.get('actual_current_driver_source',{});_same_bytes(source)\n    if source.get('sha256')!=caller_source_sha256:raise ValueError('Read the actual complete caller source')\n    source_path=Path(source['path']).resolve();topic=source_path.parents[2]\n"
   ],
   [
    74102,
    74635,
    "        raise ValueError('The complete caller role table does not bind this actual M history bridge')\n    binding=_module(Path(__file__).with_name('frequency_refined_public_reference_source_binding.py'),ANALYTIC_BINDING_SOURCE_SHA256)\n    binding.validate_frozen_point_relation(value.get('frozen_original_point_relation'),model,source_directory=source_path.parent)\n    if value.get('reference_M')!=160 or value.get('current_M')!=320:\n        raise ValueError('Retain the explicitly separate frozen and current frequency dimensions')\n",
    "        raise ValueError('The complete caller must bind this actual radial history bridge')\n    binding=_radial_binding()\n    binding.validate_frozen_point_relation(value.get('frozen_original_point_relation'),model,\n        source_directory=source_path.parent)\n    if value.get('reference_J')!=923 or value.get('current_J')!=1845:\n        raise ValueError('Keep the frozen and current radial dimensions distinct')\n    bridge=_radial_addresses();layout=model['base_complete_model']['radial_layout_definition']\n"
   ],
   [
    75011,
    75193,
    "        if family['memory_sha256']!=CURRENT_MEMORY_SOURCE_SHA256:\n            raise ValueError('An actual M-parent must belong to the same complete independent fixed target family')\n",
    "        if family['memory_sha256']!=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256:\n            raise ValueError('An actual radial parent must belong to this same complete fixed public09 target')\n"
   ],
   [
    75427,
    75530,
    "                or payload.get('N')!=2048 or payload.get('observation_carrier_sha256')!=carrier_sha256\n",
    "                or payload.get('N')!=2048 or payload.get('J')!=923 or payload.get('M')!=160\n                or payload.get('observation_carrier_sha256')!=carrier_sha256\n"
   ],
   [
    75624,
    75785,
    "                or _compatible_models(payload['representation'],model,pins,frozen_point_relation=value['frozen_original_point_relation'])!=item['model_binding']\n",
    "                or _compatible_models(payload['representation'],model,pins,\n                    frozen_point_relation=value['frozen_original_point_relation'])!=item['model_binding']\n"
   ],
   [
    76021,
    76145,
    "            raise ValueError('The complete original report, target, typed rows or unresolved ancestor obligations changed')\n",
    "            raise ValueError('The complete actual original source, target, parent or unresolved obligations changed')\n"
   ],
   [
    76375,
    76461,
    "            raise ValueError('Keep the entire actual original input-history closure')\n",
    "            raise ValueError('Keep every original actual history input')\n"
   ],
   [
    76522,
    76720,
    "        if _address_fingerprints(old_arrays)!=item.get('actual_complete_walker_role_fingerprints'):\n            raise ValueError('Keep every complete known original role and protected-address set')\n",
    "        mapped=bridge.map_arrays(old_arrays,layout,source_J=923)\n        if (_address_fingerprints(old_arrays)!=item.get('actual_complete_walker_role_fingerprints')\n                or mapped!=item.get('complete_mapped_role_arrays')\n                or _address_fingerprints(mapped)!=item.get('actual_mapped_role_fingerprints')):\n            raise ValueError('Retain full original role words and their exact current coordinate images')\n"
   ],
   [
    76755,
    76956,
    "            if not {_point(v) for v in old_arrays[role]}<=current_sets[role]:\n                raise ValueError('The full old explicit/protected history is not contained in the current initial memory')\n",
    "            if not {_point(v) for v in mapped[role]}<=current_sets[role]:\n                raise ValueError('An old explicit or protected material point was omitted')\n        old_rows=payload['material_envelope']['actual_separation_memory']['rows']\n        mapped_rows=[bridge.transfer_typed_row(row,layout,source_J=923) for row in old_rows]\n        if mapped_rows!=item.get('complete_mapped_typed_rows'):\n            raise ValueError('All typed families, locations and diameter partners must be accurately mapped')\n"
   ],
   [
    77153,
    77244,
    "            raise ValueError('The entire complete unchanged observation identity changed')\n",
    "            raise ValueError('The complete original/fine union differs')\n"
   ],
   [
    77318,
    78079,
    "    module=getattr(q.base,'frequency_layout_module',None)\n    if module is None:\n        # The current base stores the source-bound module in its constructor globals.\n        path=Path(q.base.__class__.__init__.__code__.co_filename).parent/'so3_frequency_refinement_layout.py'\n        if sha(path)!=LAYOUT_SOURCE_SHA256:\n            raise ValueError('Bind the complete independent frequency-layout module')\n        name='_actual_frequency_layout_'+LAYOUT_SOURCE_SHA256\n        spec=importlib.util.spec_from_file_location(name,path)\n        module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)\n    for function in (module.definition,module.validate_base_model,module.embed_outer_words,module.validate_inclusion):\n",
    "    path=Path(q.base.__class__.__init__.__code__.co_filename).parent/'radial_bisection_layout.py'\n    module=_module(path,LAYOUT_SOURCE_SHA256)\n    for function in (module.definition,module.validate_definition,module.embed_outer_shared_quintic_words):\n"
   ],
   [
    78148,
    78495,
    "            raise ValueError('Keep each complete current layout and byte inclusion body')\n    if pins.get('frequency_layout',(None,None))[1]!=LAYOUT_SOURCE_SHA256:\n        raise ValueError('The actual full caller must pin the independent layout source')\n    module.validate_base_model(q.base.model,expected_base_source_sha256=pins['meridian'][1])\n",
    "            raise ValueError('Keep the entire exact radial layout and all-channel inclusion source')\n    if pins.get('radial_layout',(None,None))[1]!=LAYOUT_SOURCE_SHA256:\n        raise ValueError('The full caller must pin the exact dyadic layout source')\n    module.validate_definition(q.base.radial_layout_definition)\n"
   ],
   [
    78573,
    78600,
    "    module=_layout(q,pins)\n",
    "    module=_layout(q,pins);layout=q.base.radial_layout_definition\n"
   ],
   [
    78730,
    78930,
    "        raise ValueError('Bind the current complete point identity source')\n    old=np.r_[q.parent_core[q.K:],np.zeros(len(q.radial_free)*482),float.fromhex(q.parent_jet.model['initial_height_hex'])]\n",
    "        raise ValueError('Bind the complete actual full-point identity source')\n    old=np.r_[q.parent_core[q.K:],np.zeros(len(layout['original_free_radial_slots'])*482),\n        float.fromhex(q.parent_jet.model['initial_height_hex'])]\n"
   ],
   [
    78959,
    79044,
    "    included,record=module.embed_outer_words(old,q.base.frequency_layout_definition)\n",
    "    included,record=module.embed_outer_shared_quintic_words(old,layout,\n        q.base.radial_carriers['original_width_carriers'])\n"
   ],
   [
    79115,
    79498,
    "            or included.tobytes()!=current.tobytes()\n            or array_sha(current)!=q.reference_point_sha256):\n        raise ValueError('The new frozen reference point must be the exact zero inclusion of the old core/H/zero-omega point')\n    return dict(original_full_point_sha256=array_sha(old),\n        current_full_point_sha256=array_sha(current),coordinate_inclusion=record)\n",
    "            or included.tobytes()!=current.tobytes() or array_sha(current)!=q.reference_point_sha256):\n        raise ValueError('The fine frozen seed must retain the original whole core/H and all zero omega jets')\n    return dict(original_full_point_sha256=array_sha(old),current_full_point_sha256=array_sha(current),\n        coordinate_inclusion=record)\n"
   ],
   [
    80112,
    80172,
    "    if (payload.get('N')!=q.full_N or payload.get('J')!=q.J\n",
    "    if (payload.get('N')!=q.full_N or payload.get('J')!=923\n"
   ],
   [
    80799,
    80916,
    "        raise ValueError('Keep the same full observation measure, spectral loss and strict geometric safety policy')\n",
    "        raise ValueError('Keep the same original observation parameters, spectral loss and strict geometric safety policy')\n"
   ],
   [
    82084,
    82084,
    "",
    "\ndef _radial_binding():\n    return _module(Path(__file__).with_name('radial_refined_public_reference_source_binding.py'),\n        ANALYTIC_BINDING_SOURCE_SHA256)\n\n\n\ndef _radial_addresses():\n    return _module(Path(__file__).with_name('radial_material_address_transfer.py'),\n        RADIAL_ADDRESS_SOURCE_SHA256)\n\n\n"
   ]
  ]
 },
 "geometry": {
  "parent": {
   "path": "scripts/resume_20261126/so3_frequency_refined_public_reference_envelope_geometry.py",
   "sha256": "be23caab6ba3b62bf02129f5da5043dffe6fe4d51b394590f16400a61dbf1de6",
   "bytes": 68931
  },
  "output": {
   "name": "so3_radial_refined_public_reference_envelope_geometry.py",
   "bytes": 69975,
   "sha256": "2fe41a0ecc48d1404973b55dcde4cb4591bc4029fb4158740bbf5369aa869877"
  },
  "patches": [
   [
    751,
    860,
    "CURRENT_MATERIAL_ENVELOPE_MEMORY_SHA256 = '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'\n",
    "CURRENT_MATERIAL_ENVELOPE_MEMORY_SHA256 = '6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a'\n"
   ],
   [
    961,
    1247,
    "SCHEMA = 'complete-public09-frequency-refined-analytic-frame-envelope-world-geometry-v1'\nANALYTIC_STAGE_SOURCE_SHA256 = '2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2'\nOPERATOR_SCHEMA = 'complete-frequency-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\n",
    "SCHEMA = 'complete-public09-radial-refined-analytic-frame-envelope-world-geometry-v1'\nANALYTIC_STAGE_SOURCE_SHA256 = '0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9'\nOPERATOR_SCHEMA = 'complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\n"
   ],
   [
    1422,
    1901,
    "ENDPOINT_SOURCE_SHA256 = '014fd521d315db223590d45b9b4d4da4e09975036044e533f601dcab636731d9'\nSTAGE_MATRIX_SOURCE_SHA256 = 'd7a6ebc317637667a18b8fb58ac8717aba8cbada981a349027bcaa60b448e4b7'\nADJACENT_FRAME_SOURCE_SHA256 = '610805744bdb5f4826d0c3a63bb769c9744639734db232ec31b3dbeaa0f89569'\nBASE_OPERATOR_SCHEMA = 'complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1'\nBASE_SOURCE_SHA256 = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'\n",
    "ENDPOINT_SOURCE_SHA256 = '8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5'\nSTAGE_MATRIX_SOURCE_SHA256 = 'fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387'\nADJACENT_FRAME_SOURCE_SHA256 = '3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4'\nBASE_OPERATOR_SCHEMA = 'complete-R711-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1'\nBASE_SOURCE_SHA256 = '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'\n"
   ],
   [
    2077,
    2176,
    "SUPPORTED_INPUT_BINDER_SHA256 = 'bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971'\n",
    "SUPPORTED_INPUT_BINDER_SHA256 = '59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652'\n"
   ],
   [
    2283,
    2386,
    "REFERENCE_CENTERING_SOURCE_SHA256 = 'b72572b13f94bf5482ced96c06aa940b5097ace270c159ec1837495519d9387a'\n",
    "REFERENCE_CENTERING_SOURCE_SHA256 = 'c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178'\n"
   ],
   [
    14657,
    14789,
    "                or frozen.get('schema') != 'frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'\n",
    "                or frozen.get('schema') != 'radial-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'\n"
   ],
   [
    15191,
    15191,
    "",
    "        if (problem.M!=160 or problem.J!=1845 or problem.base.reference_J!=923\n                or problem.full_N!=2048 or problem.N!=513\n                or base.get('radial_layout_definition')!=problem.base.radial_layout_definition\n                or canonical(base['radial_layout_definition'])!=base.get('radial_layout_identity_sha256')\n                or base.get('radial_observation_definition')!=problem.base.radial_observations.definition\n                or canonical(base['radial_observation_definition'])!=base.get('radial_observation_identity_sha256')\n                or self.envelope._fixed['implicit_grid']['current_radial_layout_identity_sha256']\n                    !=base['radial_layout_identity_sha256']\n                or self.envelope._fixed['implicit_grid']['current_observation_identity_sha256']\n                    !=base['radial_observation_identity_sha256']):\n            raise ValueError('Bind the complete fine J1845 observer and exact mapped original J923 material envelope')\n"
   ],
   [
    15817,
    15954,
    "        new_literal_input = frozen['schema'] == 'frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'\n",
    "        new_literal_input = frozen['schema'] == 'radial-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'\n"
   ],
   [
    16135,
    16264,
    "            if (literal_input_schema != 'frequency-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'\n",
    "            if (literal_input_schema != 'radial-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'\n"
   ],
   [
    21012,
    21129,
    "                or policy.get('source_sha256') != 'f272aaa95e63867d18015d9e92fa321f36785459377433a4433382794ae9c15a'\n",
    "                or policy.get('source_sha256') != 'bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e'\n"
   ],
   [
    30281,
    30413,
    "            coordinate_semantics='cell/u on the unchanged symbolic radial mesh; phi is the NEW fixed-parent chart coordinate phi0',\n",
    "            coordinate_semantics='cell/u on complete accurate dyadic J1845 nodes; all original J923 addresses are exactly mapped before evaluation; phi0 uses the unchanged frozen M160 chart',\n"
   ]
  ]
 },
 "driver": {
  "parent": {
   "path": "scripts/resume_20261126/fullclosed_frequency_refined_public_reference_so3_qp.py",
   "sha256": "0dc3bbb46df6168f3f3130bb9009ee4cd94845f455926ba036ba987a79c8cc41",
   "bytes": 86793
  },
  "output": {
   "name": "fullclosed_radial_refined_public_reference_so3_qp.py",
   "bytes": 90333,
   "sha256": "1709eb319dcecfc1310c9c763cfb812aad56599736965b39de3790dec719aa0f"
  },
  "patches": [
   [
    829,
    906,
    "SCHEMA = 'complete-public09-M320-analytic-frame-material-envelope-SO3-QP-v1'\n",
    "SCHEMA = 'complete-public09-J1845-analytic-frame-material-envelope-SO3-QP-v1'\n"
   ],
   [
    1123,
    1890,
    " 'adjacent_matrices': ('scripts/resume_20261126/frequency_refined_public_reference_adjacent_matrices.py',\n                       '610805744bdb5f4826d0c3a63bb769c9744639734db232ec31b3dbeaa0f89569'),\n 'analytic_J3': ('scripts/resume_20261126/frequency_refined_public_reference_stage_jacobian.py',\n                 '2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2'),\n 'analytic_J3_binding': ('scripts/resume_20261126/frequency_refined_public_reference_source_binding.py',\n                         'a62e122d32b5a8faa7e1dee82e8f8855c40c1f2d8a1bceeb14a298a6512ba931'),\n 'analytic_frame': ('scripts/resume_20261126/frequency_refined_public_reference_normal_frame.py',\n                    '787825f17de647598099fe7b4cbfc3d82b6ad90eac9943de6b67f653f092520a'),\n",
    " 'adjacent_matrices': ('scripts/resume_20261126/radial_refined_public_reference_adjacent_matrices.py',\n                       '3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4'),\n 'analytic_J3': ('scripts/resume_20261126/radial_refined_public_reference_stage_jacobian.py',\n                 '0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9'),\n 'analytic_J3_binding': ('scripts/resume_20261126/radial_refined_public_reference_source_binding.py',\n                         '5b50b02aea139b81e7e1ed3cbf37c4ad8870d182c63d48bf648fb197e1cf3734'),\n 'analytic_frame': ('scripts/resume_20261126/radial_refined_public_reference_normal_frame.py',\n                    '8fb0f326356d8e94337d51bfba85068c5872453df8f08e6619f241dfe7f715ce'),\n"
   ],
   [
    3439,
    3617,
    " 'endpoint': ('scripts/resume_20261126/so3_frequency_refined_public_reference_normal_lift.py',\n              '014fd521d315db223590d45b9b4d4da4e09975036044e533f601dcab636731d9'),\n",
    " 'endpoint': ('scripts/resume_20261126/so3_radial_refined_public_reference_normal_lift.py',\n              '8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5'),\n"
   ],
   [
    5029,
    5397,
    " 'envelope_transfer': ('scripts/resume_20261126/frequency_refined_public_reference_history_transfer.py',\n                       'fdc29a36ca562cec8327a2ca250ecdd3a505827415617255993b6fcab5389279'),\n 'frame_C1': ('scripts/resume_20261126/frequency_refined_public_reference_frame_c1.py',\n              'f272aaa95e63867d18015d9e92fa321f36785459377433a4433382794ae9c15a'),\n",
    " 'envelope_transfer': ('scripts/resume_20261126/radial_refined_public_reference_history_transfer.py',\n                       '2720bd9033391fc3f0a48afe33f50ea5843b2bf225a6596ee5a5b7077819e55c'),\n 'frame_C1': ('scripts/resume_20261126/radial_refined_public_reference_frame_c1.py',\n              'bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e'),\n"
   ],
   [
    7039,
    10486,
    " 'frequency_layout': ('scripts/resume_20261126/so3_frequency_refinement_layout.py',\n                      'ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27'),\n 'frequency_parent_adjacent_matrices': ('scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py',\n                                        '3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695'),\n 'frequency_parent_analytic_J3': ('scripts/resume_20261126/analytic_frame_local_stage_jacobian.py',\n                                  '894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866'),\n 'frequency_parent_analytic_J3_binding': ('scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py',\n                                          '15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592'),\n 'frequency_parent_analytic_frame': ('scripts/resume_20261126/analytic_normal_frame_jets.py',\n                                     '4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8'),\n 'frequency_parent_driver': ('scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py',\n                             'ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'),\n 'frequency_parent_endpoint': ('scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py',\n                               '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc'),\n 'frequency_parent_envelope_transfer': ('scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py',\n                                        '6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707'),\n 'frequency_parent_frame_C1': ('scripts/resume_20261126/analytic_frame_c1_reuse.py',\n                               'f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb'),\n 'frequency_parent_geometry': ('scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py',\n                               'e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13'),\n 'frequency_parent_meridian': ('scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py',\n                               '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'),\n 'frequency_parent_new_moment_input': ('scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py',\n                                       '307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7'),\n 'frequency_parent_reader': ('scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py',\n                             'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32'),\n 'frequency_parent_reference_calibration': ('scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py',\n                                            'fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0'),\n 'frequency_parent_root_packets': ('scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py',\n                                   '094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0'),\n 'frequency_parent_stage_matrices': ('scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py',\n                                     'fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255'),\n",
    ""
   ],
   [
    10660,
    10844,
    " 'geometry': ('scripts/resume_20261126/so3_frequency_refined_public_reference_envelope_geometry.py',\n              'be23caab6ba3b62bf02129f5da5043dffe6fe4d51b394590f16400a61dbf1de6'),\n",
    " 'geometry': ('scripts/resume_20261126/so3_radial_refined_public_reference_envelope_geometry.py',\n              '2fe41a0ecc48d1404973b55dcde4cb4591bc4029fb4158740bbf5369aa869877'),\n"
   ],
   [
    11485,
    11701,
    " 'independent_envelope_memory': ('scripts/resume_20261126/complete_material_envelope_memory_public_reference.py',\n                                 '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'),\n",
    " 'independent_envelope_memory': ('scripts/resume_20261126/radial_refined_public_reference_memory.py',\n                                 '6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a'),\n"
   ],
   [
    12095,
    12278,
    " 'meridian': ('scripts/resume_20261126/so3_frequency_refined_smooth_triangle_meridian_operator.py',\n              '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'),\n",
    " 'meridian': ('scripts/resume_20261126/so3_radial_refined_public_reference_meridian_operator.py',\n              '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'),\n"
   ],
   [
    13026,
    13229,
    " 'new_moment_input': ('scripts/resume_20261126/frequency_refined_smooth_triangle_literal_zero_moment_input.py',\n                      'bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971'),\n",
    " 'new_moment_input': ('scripts/resume_20261126/radial_refined_public_reference_literal_zero_moment_input.py',\n                      '59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652'),\n"
   ],
   [
    13680,
    13680,
    "",
    " 'radial_address_transfer': ('scripts/resume_20261126/radial_material_address_transfer.py',\n                             '6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716'),\n 'radial_affine_reference': ('scripts/resume_20261126/exact_affine_supported_reference.py',\n                             '2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117'),\n 'radial_layout': ('scripts/resume_20261126/radial_bisection_layout.py',\n                   'cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744'),\n 'radial_observations': ('scripts/resume_20261126/complete_dyadic_radial_observations.py',\n                         '2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74'),\n 'radial_parent_adjacent_matrices': ('scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py',\n                                     '3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695'),\n 'radial_parent_analytic_J3': ('scripts/resume_20261126/analytic_frame_local_stage_jacobian.py',\n                               '894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866'),\n 'radial_parent_analytic_J3_binding': ('scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py',\n                                       '15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592'),\n 'radial_parent_analytic_frame': ('scripts/resume_20261126/analytic_normal_frame_jets.py',\n                                  '4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8'),\n 'radial_parent_driver': ('scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py',\n                          'ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'),\n 'radial_parent_endpoint': ('scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py',\n                            '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc'),\n 'radial_parent_envelope_transfer': ('scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py',\n                                     '6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707'),\n 'radial_parent_frame_C1': ('scripts/resume_20261126/analytic_frame_c1_reuse.py',\n                            'f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb'),\n 'radial_parent_geometry': ('scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py',\n                            'e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13'),\n 'radial_parent_memory': ('scripts/resume_20261126/complete_material_envelope_memory_public_reference.py',\n                          '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'),\n 'radial_parent_meridian': ('scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py',\n                            '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'),\n 'radial_parent_new_moment_input': ('scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py',\n                                    '307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7'),\n 'radial_parent_reader': ('scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py',\n                          'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32'),\n 'radial_parent_reference_calibration': ('scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py',\n                                         'fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0'),\n 'radial_parent_root_packets': ('scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py',\n                                '094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0'),\n 'radial_parent_stage_matrices': ('scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py',\n                                  'fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255'),\n"
   ],
   [
    13836,
    14229,
    " 'reference_calibration': ('scripts/resume_20261126/frequency_refined_public_reference_calibration.py',\n                           'b72572b13f94bf5482ced96c06aa940b5097ace270c159ec1837495519d9387a'),\n 'root_packets': ('scripts/resume_20261126/immutable_frequency_refined_public_reference_root_packets.py',\n                  '4b352626ed6f306bcdb1dc0126131c8f9fb4ab3d081376ae70739ec7c9d752f9'),\n",
    " 'reference_calibration': ('scripts/resume_20261126/radial_refined_public_reference_calibration.py',\n                           'c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178'),\n 'root_packets': ('scripts/resume_20261126/immutable_radial_refined_public_reference_root_packets.py',\n                  '8d2b93dd055cc600aac14183d060d101421a924590c1fe8300625931bc8c0403'),\n"
   ],
   [
    14889,
    15078,
    " 'stage_matrices': ('scripts/resume_20261126/frequency_refined_public_reference_stage_matrices.py',\n                    'd7a6ebc317637667a18b8fb58ac8717aba8cbada981a349027bcaa60b448e4b7'),\n",
    " 'stage_matrices': ('scripts/resume_20261126/radial_refined_public_reference_stage_matrices.py',\n                    'fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387'),\n"
   ],
   [
    15245,
    15339,
    "ROOT_SNAPSHOT_SCHEMA = 'actual-frequency-refined-public-reference-analytic-frame-snapshot-v1'\n",
    "ROOT_SNAPSHOT_SCHEMA = 'actual-radial-refined-public-reference-analytic-frame-snapshot-v1'\n"
   ],
   [
    28088,
    28149,
    "    p.add_argument('--current-modes', type=int, default=320)\n",
    "    p.add_argument('--current-radial-factor', type=int, default=2)\n"
   ],
   [
    40710,
    40893,
    "            or a.current_modes!=320 or a.angles!=2048):\n        raise ValueError('M-only inclusion retains the full actual target, all 32 stages, N2048 and eight radial Gauss nodes')\n",
    "            or a.current_radial_factor!=2 or a.angles!=2048):\n        raise ValueError('Radial-only inclusion retains the full actual target, M160/N2048, all 32 stages and eight radial Gauss nodes')\n"
   ],
   [
    44716,
    44807,
    "    frequency_layout = load('_complete_actual_frequency_layout',paths['frequency_layout'])\n",
    "    radial_layout = load('_complete_exact_dyadic_layout',paths['radial_layout'])\n    radial_affine = load('_complete_exact_affine_reference',paths['radial_affine_reference'])\n    radial_observations = load('_complete_dyadic_observation_input',paths['radial_observations'])\n"
   ],
   [
    46538,
    46621,
    "        current_modes=args.current_modes,frequency_layout_module=frequency_layout)\n",
    "        radial_layout_module=radial_layout,affine_reference_module=radial_affine,\n        radial_observation_module=radial_observations)\n"
   ],
   [
    50096,
    50208,
    "        expected_base_schema='complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1',\n",
    "        expected_base_schema='complete-R711-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1',\n"
   ],
   [
    53722,
    53796,
    "    frequency_record=envelope_transfer.frequency_initial_record(args,q,x,\n",
    "    radial_record=envelope_transfer.radial_initial_record(args,q,x,\n"
   ],
   [
    54168,
    54168,
    "",
    "    parent_stage_weights=base.common_parent_weights(args.legacy_fraction)\n    if (parent_stage_weights.shape!=(7377,) or not np.isfinite(parent_stage_weights).all()\n            or np.any(parent_stage_weights<=0)):\n        raise ValueError('The complete original 7377-row positive functional must be retained separately')\n    parent_normalizer=float(parent_stage_weights.sum()*q.full_N)\n"
   ],
   [
    57256,
    57666,
    "        frequency_refinement=frequency_record,reference_M=160,current_M=320,\n        frequency_layout_definition=base.frequency_layout_definition,\n        frequency_layout_identity_sha256=base.model['frequency_layout_identity_sha256'],\n        frequency_layout_source=file_record(paths['frequency_layout']),\n        radial_observation_refinement_performed=False,angular_observation_refinement_performed=False,\n",
    "        radial_refinement=radial_record,reference_J=923,current_J=1845,\n        radial_layout_definition=base.radial_layout_definition,\n        radial_layout_identity_sha256=base.model['radial_layout_identity_sha256'],\n        radial_layout_source=file_record(paths['radial_layout']),\n        exact_affine_reference_definition=base.exact_affine_reference.definition,\n        exact_affine_reference_source=file_record(paths['radial_affine_reference']),\n        complete_radial_observation_definition=base.radial_observations.definition,\n        complete_radial_input_files=base.radial_observation_files,\n        complete_radial_input_metadata=base.radial_observations.metadata(),\n        radial_observation_source=file_record(paths['radial_observations']),\n        radial_address_source=file_record(paths['radial_address_transfer']),\n        radial_observation_refinement_performed=True,angular_observation_refinement_performed=False,\n        frequency_refinement_performed=False,\n        current_coordinate_norm_and_positive_observation_rule_changed=True,\n        current_midpoint_coefficient_rounding_enclosed=False,\n        common_parent_radial_functional=dict(reference_J=923,full_N=2048,complete_original_rows=7377,\n            legacy_fraction=args.legacy_fraction,normalizer=parent_normalizer,\n            positive_stage_weights_sha256=meridian.array_sha(parent_stage_weights),\n            full_current_to_parent_stage_map_sha256=meridian.array_sha(base.common_parent_stage_map),\n            complete_original_scalar_target_words_verified=True,\n            all_three_metric_components_and_full_mean_cross_terms_retained=True,\n            values_from_current_fine_physical_field_not_from_saved_parent=True,\n            old_and_current_Phi_not_directly_compared_as_one_measure=True),\n"
   ],
   [
    68302,
    68302,
    "",
    "        common=base.common_parent_unweight(native)\n        if common.shape!=(7377,q.N,3):\n            raise ValueError('Keep all original material rows and all three current physical Gram components')\n        common_spectrum=spectral.statistics(common,parent_stage_weights,q.multiplicity,parameters)\n        common_spectrum=centered.augment_statistics(common,parent_stage_weights,q.multiplicity,parameters,\n            common_spectrum,stage_block=args.stage_block)\n"
   ],
   [
    68574,
    68574,
    "",
    "            common_parent_functional=dict(spectral=common_spectrum,max_relative_gram=maximum(common),\n                complete_original_rows=7377,full_N=2048,\n                current_full_point_sha256=meridian.array_sha(point),\n                actual_current_model_identity_sha256=q.identity,\n                measure=report['common_parent_radial_functional'],\n                same_current_physical_field_used=True,saved_parent_values_reused=False),\n"
   ]
  ]
 },
 "launcher": {
  "parent": {
   "path": "scripts/resume_20261126/launch_frequency_refined_public_reference_so3_actions.py",
   "sha256": "55fbc4900dd0b049b11e4ecfa1aba642daf39a85241f0b1cb4283cf657506e03",
   "bytes": 21902
  },
  "output": {
   "name": "launch_radial_refined_public_reference_so3_actions.py",
   "bytes": 22323,
   "sha256": "2658b074a61afa32305703def009e71c8aa99836036a6b756508e6305a7770ec"
  },
  "patches": [
   [
    483,
    563,
    "DRIVER_SHA = '0dc3bbb46df6168f3f3130bb9009ee4cd94845f455926ba036ba987a79c8cc41'\n",
    "DRIVER_SHA = '1709eb319dcecfc1310c9c763cfb812aad56599736965b39de3790dec719aa0f'\n"
   ],
   [
    2016,
    2077,
    "    p.add_argument('--current-modes', type=int, default=320)\n",
    "    p.add_argument('--current-radial-factor', type=int, default=2)\n"
   ],
   [
    14756,
    14939,
    "            or a.current_modes!=320 or a.angles!=2048):\n        raise ValueError('M-only inclusion retains the full actual target, all 32 stages, N2048 and eight radial Gauss nodes')\n",
    "            or a.current_radial_factor!=2 or a.angles!=2048):\n        raise ValueError('Radial-only inclusion retains the full actual target, M160/N2048, all 32 stages and eight radial Gauss nodes')\n"
   ],
   [
    15133,
    15211,
    "    driver = source/'fullclosed_frequency_refined_public_reference_so3_qp.py'\n",
    "    driver = source/'fullclosed_radial_refined_public_reference_so3_qp.py'\n"
   ],
   [
    18304,
    18407,
    "    record = dict(schema='public-actions-complete-R711-stage-matrix-envelope-transfer-SO3-command-v1',\n",
    "    record = dict(schema='public-actions-complete-public09-J1845-SO3-command-v1',\n"
   ],
   [
    19056,
    19308,
    "        fixed_supported_unit_seed=True,reference_M=160,current_M=args.current_modes,\n        every_original_free_word_retained_with_correct_three_block_zero_inclusion=True,\n        original_reference_M160_chart_and_N2048_radial_observer_retained=True,\n",
    "        fixed_supported_unit_seed=True,M=160,full_N=2048,reference_J=923,current_J=1845,\n        current_radial_factor=args.current_radial_factor,\n        all_original_radial_node_words_and_all_old_free_jet_words_retained=True,\n        every_new_shared_radial_midpoint_jet_initialized_from_complete_original_quintic=True,\n        frozen_original_reference_M160_chart_N2048_and_J923_retained=True,\n        current_radial_observer_and_norm_explicitly_refined=True,\n        full_common_parent_functional_reread_on_current_field=True,\n        new_midpoint_coefficient_rounding_errors_enclosed=False,\n        exact_field_inclusion_requires_compatible_selected_normal_branch=True,\n"
   ]
  ]
 },
 "reader": {
  "parent": {
   "path": "scripts/resume_20261126/read_frequency_refined_public_reference_so3_report.py",
   "sha256": "f56c4f81037fa9d54edcdc566552c8eefb79cb372920419ed7e81fcf1b5aaf2e",
   "bytes": 97436
  },
  "output": {
   "name": "read_radial_refined_public_reference_so3_report.py",
   "bytes": 97634,
   "sha256": "c344478b6dbb0df0dfa80e924b6ef6a739d79460ab3094a16f23b8b33bdb2695"
  },
  "patches": [
   [
    610,
    774,
    "DRIVER_SHA = '0dc3bbb46df6168f3f3130bb9009ee4cd94845f455926ba036ba987a79c8cc41'\nREPORT_SCHEMA = 'complete-public09-M320-analytic-frame-material-envelope-SO3-QP-v1'\n",
    "DRIVER_SHA = '1709eb319dcecfc1310c9c763cfb812aad56599736965b39de3790dec719aa0f'\nREPORT_SCHEMA = 'complete-public09-J1845-analytic-frame-material-envelope-SO3-QP-v1'\n"
   ],
   [
    776,
    969,
    "OPERATOR_SCHEMA = 'complete-frequency-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nROOT_SNAPSHOT_SCHEMA = 'actual-frequency-refined-public-reference-analytic-frame-snapshot-v1'\n",
    "OPERATOR_SCHEMA = 'complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nROOT_SNAPSHOT_SCHEMA = 'actual-radial-refined-public-reference-analytic-frame-snapshot-v1'\n"
   ],
   [
    43956,
    44083,
    "            or value.get('schema') != 'frequency-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'\n",
    "            or value.get('schema') != 'radial-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'\n"
   ],
   [
    44140,
    44248,
    "                != 'frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'\n",
    "                != 'radial-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'\n"
   ],
   [
    44902,
    45008,
    "    path = topic/'scripts/resume_20261126/frequency_refined_smooth_triangle_literal_zero_moment_input.py'\n",
    "    path = topic/'scripts/resume_20261126/radial_refined_public_reference_literal_zero_moment_input.py'\n"
   ],
   [
    46516,
    46628,
    "    if (base.get('schema') != 'complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1'\n",
    "    if (base.get('schema') != 'complete-R711-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1'\n"
   ],
   [
    48885,
    49060,
    "                    'all_original_outer_free_variables_retained_and_new_modes_added',\n                    'frozen_reference_layout_unchanged','current_norm_layout_changed')),\n",
    "                    'all_original_outer_free_variables_retained_and_new_radial_jets_added',\n                    'frozen_reference_radial_mesh_unchanged','current_norm_layout_changed',\n                    'reference_seed_and_material_chart_unchanged')),\n"
   ],
   [
    67299,
    67299,
    "",
    "        common_parent_functional=value['common_parent_functional'],\n"
   ],
   [
    76747,
    76848,
    "    driver = topic/'scripts/resume_20261126/fullclosed_frequency_refined_public_reference_so3_qp.py'\n",
    "    driver = topic/'scripts/resume_20261126/fullclosed_radial_refined_public_reference_so3_qp.py'\n"
   ],
   [
    88479,
    88581,
    "    return dict(schema='actual-run09-public-reference-analytic-frame-packet-envelope-SO3-readout-v1',\n",
    "    return dict(schema='actual-public09-J1845-analytic-frame-packet-envelope-SO3-readout-v1',\n"
   ],
   [
    89364,
    89364,
    "",
    "        radial_refinement=extra['analytic_J3_binding']['radial_refinement'],\n"
   ]
  ]
 }
};
