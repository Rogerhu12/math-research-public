// Complete exact text transformations; no scientific evaluation.
// Every parent and every output is independently whole-byte pinned.
export const specifications = {
 "base": {
  "parent": {
   "path": "scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py",
   "sha256": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
   "bytes": 40771
  },
  "output": {
   "name": "so3_radial_refined_public_reference_meridian_operator.py",
   "bytes": 45749,
   "sha256": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0"
  },
  "patches": [
   [
    974,
    1061,
    "SCHEMA = 'complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1'\n",
    "SCHEMA = 'complete-R711-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1'\nRADIAL_LAYOUT_SOURCE_SHA256 = 'cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744'\nEXACT_AFFINE_REFERENCE_SOURCE_SHA256 = '2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117'\nRADIAL_OBSERVATION_SOURCE_SHA256 = '2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74'\n"
   ],
   [
    5824,
    5894,
    "                 seed_parameters=None, seed_mean_kernel_module=None):\n",
    "                 seed_parameters=None, seed_mean_kernel_module=None,\n                 radial_layout_module=None, affine_reference_module=None,\n                 radial_observation_module=None):\n"
   ],
   [
    7518,
    7741,
    "        self.M, self.K, self.J = int(parent_problem.M), int(parent_problem.K), int(parent_problem.J)\n        if self.K != 3:\n            raise ValueError('Retain exactly the originally fixed first three core coefficients')\n",
    "        self.M, self.K, self.reference_J = int(parent_problem.M), int(parent_problem.K), int(parent_problem.J)\n        self.J = self.current_J = 1845\n        if (self.M != 160 or self.K != 3 or self.reference_J != 923\n                or int(parent_problem.full_N) != 2048):\n            raise ValueError('Retain the actual full M160/N2048/J923 reference and select current J1845')\n        for module,expected,method in (\n                (radial_layout_module,RADIAL_LAYOUT_SOURCE_SHA256,'construct_current_carriers'),\n                (affine_reference_module,EXACT_AFFINE_REFERENCE_SOURCE_SHA256,'definition'),\n                (radial_observation_module,RADIAL_OBSERVATION_SOURCE_SHA256,'definition')):\n            if (module is None or sha(module.__file__) != expected\n                    or sha(getattr(module,method).__code__.co_filename) != expected):\n                raise ValueError('Bind every complete exact-query, layout and full-observation source')\n        self.radial_layout_module = radial_layout_module\n        self.radial_carriers = radial_layout_module.construct_current_carriers(self.context)\n        self.radial_layout_definition = self.radial_carriers['definition']\n        self.radial_layout_identity = canonical(self.radial_layout_definition)\n        self.exact_nodes = self.radial_carriers['exact_nodes']\n        self.reference_mesh = np.array(parent_problem.mesh,copy=True)\n"
   ],
   [
    7769,
    7993,
    "        self.mesh = np.array(parent_problem.mesh, copy=True)\n        if self.mesh[0] != 0 or np.any(np.diff(self.mesh) <= 0):\n            raise ValueError('Use the complete original increasing mesh from core zero to cap S')\n",
    "        self.mesh = np.array(self.radial_carriers['mesh'],copy=True)\n        if (self.mesh.shape != (self.J,) or self.mesh[0] != 0\n                or np.any(np.diff(self.mesh) <= 0)\n                or self.mesh[::2].tobytes() != self.reference_mesh.tobytes()):\n            raise ValueError('Keep every original node word at the actual current even index')\n"
   ],
   [
    8064,
    8134,
    "        self.P, self.N = int(parent_problem.P), int(parent_problem.N)\n",
    "        self.exact_affine_reference = affine_reference_module.ExactAffineSupportedReference(\n            self.parent_jet,expected_seed_identity_sha256=self.parent_jet.model_identity,\n            expected_reference_identity_sha256=self.context.identity)\n        self.radial_observations = radial_observation_module.CompleteDyadicObservationPlan(\n            self.context,self.radial_carriers,radial_layout_module)\n        self.plan = self.radial_observations\n        self.reference_plan = self.context.plan\n        self.P, self.N = len(self.plan.cells), int(parent_problem.N)\n"
   ],
   [
    8183,
    8601,
    "        self.legacy_P = int(parent_problem.legacy_P)\n        self.phi = np.array(parent_problem.phi, copy=True)\n        self.times = np.array(parent_problem.times, copy=True)\n        self.observation_cells = np.array(parent_problem.observation_cells, copy=True)\n        self.observation_u = np.array(parent_problem.observation_u, copy=True)\n        self.multiplicity = np.array(parent_problem.multiplicity, copy=True)\n",
    "        self.legacy_P = int(self.plan.legacy_count)\n        self.phi = np.array(parent_problem.phi,copy=True)\n        self.times = np.array(self.plan.times,copy=True)\n        self.observation_cells = np.array(self.plan.cells,copy=True)\n        self.observation_u = np.array(self.plan.local_u,copy=True)\n        self.multiplicity = np.array(parent_problem.multiplicity,copy=True)\n"
   ],
   [
    8661,
    8716,
    "        self.a = np.array(parent_problem.a, copy=True)\n",
    "        self.a = np.array(self.plan.a,copy=True)\n        self.stage_legacy_simpson_weights = np.array(self.plan.legacy_simpson_weights,copy=True)\n        self.stage_quadrature_weights = np.array(self.plan.quadrature_weights,copy=True)\n        self.common_parent_stage_map = np.array(self.plan.parent_stage_map,copy=True)\n"
   ],
   [
    8775,
    9032,
    "        if (self.N != self.full_N//4+1 or self.full_N%4 or self.a.shape != (self.P,)\n                or np.any(self.a <= 0) or self.multiplicity.sum() != self.full_N):\n            raise ValueError('Retain every actual original positive target/angle orbit')\n",
    "        if (self.N != 513 or self.full_N != 2048 or self.legacy_P != 3689\n                or self.a.shape != (self.P,) or np.any(self.a <= 0)\n                or self.multiplicity.sum() != self.full_N\n                or self.phi.tobytes() != np.asarray(parent_problem.phi).tobytes()):\n            raise ValueError('Keep the complete fine+old radial union and all original literal angles')\n"
   ],
   [
    10957,
    10957,
    "",
    "        self.radial_observation_files = self.radial_observations.save(self.cache_directory/'complete-radial-input')\n"
   ],
   [
    12705,
    12771,
    "            M=self.M, J=self.J, mesh_sha256=array_sha(self.mesh),\n",
    "            M=self.M, J=self.J, reference_J=self.reference_J, current_J=self.current_J,\n            mesh_sha256=array_sha(self.mesh),reference_mesh_sha256=array_sha(self.reference_mesh),\n            radial_layout_source_sha256=RADIAL_LAYOUT_SOURCE_SHA256,\n            radial_layout_definition=self.radial_layout_definition,\n            radial_layout_identity_sha256=self.radial_layout_identity,\n            exact_affine_reference_source_sha256=EXACT_AFFINE_REFERENCE_SOURCE_SHA256,\n            exact_affine_reference_definition=self.exact_affine_reference.definition,\n            exact_affine_reference_identity_sha256=self.exact_affine_reference.identity,\n            radial_observation_source_sha256=RADIAL_OBSERVATION_SOURCE_SHA256,\n            radial_observation_definition=self.radial_observations.definition,\n            radial_observation_identity_sha256=self.radial_observations.identity,\n"
   ],
   [
    12874,
    13002,
    "            physical_S='same exact original S and affine symbolic nodes as the bound reference; mesh is its numerical carrier',\n",
    "            physical_S='same exact original S; current symbolic nodes exactly bisect every frozen original affine cell; mesh contains copied old and new numerical carriers',\n"
   ],
   [
    13654,
    13732,
    "            all_original_outer_free_variables_and_norm_layout_unchanged=True,\n",
    "            all_original_outer_free_variables_retained_and_new_radial_jets_added=True,\n            current_norm_layout_changed=True, reference_seed_and_material_chart_unchanged=True,\n            frozen_reference_radial_mesh_unchanged=True,\n            current_row_rule_changed_and_common_parent_functional_required=True,\n"
   ],
   [
    15824,
    15928,
    "            raise ValueError('Use actual exact-binary addresses on the unchanged exact reference mesh')\n",
    "            raise ValueError('Use actual exact-binary addresses on the complete current dyadic symbolic mesh')\n"
   ],
   [
    17207,
    17289,
    "        result = self.parent_jet.evaluate(query['cells'], query['local'], angles)\n",
    "        result = self.exact_affine_reference.evaluate_cells(self.exact_nodes,\n            query['cells'].tolist(),query['local'].tolist(),angles,\n            original_cells=(query['cells']//2).tolist())\n"
   ],
   [
    30217,
    30274,
    "        return self.parent.mixed_stage_weights(fraction)\n",
    "        return self.radial_observations.mixed_stage_weights(fraction)\n"
   ],
   [
    30275,
    30275,
    "",
    "    def common_parent_weights(self, fraction):\n        return self.radial_observations.common_parent_weights(fraction)\n\n    def common_parent_unweight(self, native):\n        value = self.unweight(native)\n        if value.shape != (self.P,self.N,3):\n            raise ValueError('Read every actual fine residual row before common-parent attribution')\n        return value[self.common_parent_stage_map].copy()\n\n"
   ],
   [
    32483,
    32483,
    "",
    "            exact_affine_reference=self.exact_affine_reference.metadata(),\n            complete_current_radial_observations=self.radial_observations.metadata(),\n            current_radial_input_files=self.radial_observation_files,\n            complete_radial_carrier_record=self.radial_carriers['record'],\n            reference_J=self.reference_J,current_J=self.J,\n            whole_current_node_and_width_carrier_errors_recorded=True,\n            midpoint_coefficient_restriction_rounding_errors_enclosed=False,\n            complete_common_parent_row_count=len(self.common_parent_stage_map),\n"
   ]
  ]
 },
 "binder": {
  "parent": {
   "path": "scripts/resume_20261126/frequency_refined_smooth_triangle_literal_zero_moment_input.py",
   "sha256": "bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971",
   "bytes": 31068
  },
  "output": {
   "name": "radial_refined_public_reference_literal_zero_moment_input.py",
   "bytes": 35736,
   "sha256": "59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652"
  },
  "patches": [
   [
    915,
    1122,
    "SCHEMA = 'frequency-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'\nDEFINITION_SCHEMA = 'frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'\n",
    "SCHEMA = 'radial-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'\nDEFINITION_SCHEMA = 'radial-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'\n"
   ],
   [
    1770,
    1951,
    "BASE_SCHEMA = 'complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1'\nBASE_SOURCE_SHA = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'\n",
    "BASE_SCHEMA = 'complete-R711-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1'\nBASE_SOURCE_SHA = '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'\n"
   ],
   [
    11950,
    11950,
    "",
    "def _radial_source_module(name,expected,method):\n    import importlib.util\n    import sys\n    path=Path(__file__).resolve().with_name(name)\n    if sha(path)!=expected:\n        raise ValueError('The complete radial model consumer source changed: '+name)\n    key='_radial_literal_Q_'+expected\n    module=sys.modules.get(key)\n    if module is None:\n        spec=importlib.util.spec_from_file_location(key,path)\n        module=importlib.util.module_from_spec(spec)\n        sys.modules[key]=module\n        spec.loader.exec_module(module)\n    function=getattr(module,method)\n    if sha(function.__code__.co_filename)!=expected:\n        raise ValueError('The complete radial consumer method changed: '+method)\n    return module\n\n\ndef _radial_binding(base,reference):\n    layout_source='cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744'\n    affine_source='2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117'\n    observations_source='2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74'\n    layout=_radial_source_module('radial_bisection_layout.py',layout_source,'validate_definition')\n    affine=_radial_source_module('exact_affine_supported_reference.py',affine_source,'validate_definition')\n    observer=_radial_source_module('complete_dyadic_radial_observations.py',observations_source,'definition')\n    rad=base.get('radial_layout_definition')\n    if (base.get('radial_layout_source_sha256')!=layout_source\n            or not isinstance(rad,dict)\n            or layout.validate_definition(rad)!=base.get('radial_layout_identity_sha256')\n            or rad.get('complete_original_reference_model')!=reference\n            or rad.get('current_mesh_sha256')!=base.get('mesh_sha256')\n            or rad.get('reference_mesh_sha256')!=reference.get('mesh_sha256')\n            or base.get('reference_mesh_sha256')!=reference.get('mesh_sha256')\n            or base.get('M')!=160 or base.get('J')!=1845\n            or base.get('reference_J')!=923 or base.get('current_J')!=1845\n            or base.get('all_original_outer_free_variables_retained_and_new_radial_jets_added') is not True\n            or base.get('current_norm_layout_changed') is not True\n            or base.get('reference_seed_and_material_chart_unchanged') is not True\n            or base.get('frozen_reference_radial_mesh_unchanged') is not True\n            or base.get('current_row_rule_changed_and_common_parent_functional_required') is not True):\n        raise ValueError('Keep the full accurate current/reference radial split and all newly free jets')\n    query=base.get('exact_affine_reference_definition')\n    if (base.get('exact_affine_reference_source_sha256')!=affine_source\n            or not isinstance(query,dict)\n            or affine.validate_definition(query)!=base.get('exact_affine_reference_identity_sha256')\n            or query.get('complete_original_seed_model')!=base.get('fixed_supported_unit_seed_model')\n            or query.get('original_reference_identity_sha256')!=canonical(reference)):\n        raise ValueError('Bind the entire exact-affine query path to the same unchanged reference')\n    observations=base.get('radial_observation_definition')\n    if (base.get('radial_observation_source_sha256')!=observations_source\n            or not isinstance(observations,dict)\n            or canonical(observations)!=base.get('radial_observation_identity_sha256')):\n        raise ValueError('Bind the whole complete native-plus-parent observation rule')\n    expected=observer.definition(reference,rad,\n        observation_arrays=observations.get('complete_observation_arrays'))\n    if observations!=expected:\n        raise ValueError('Do not omit old observations, alter their scalar target or replace the positive rule')\n    arrays=observations['complete_observation_arrays']\n    P=arrays['cells']['shape']\n    if (not isinstance(P,list) or len(P)!=1 or type(P[0]) is not int\n            or not 14753<=P[0]<=22130):\n        raise ValueError('Keep all native rows and every original row in the complete union')\n    P=P[0]\n    for name,record in arrays.items():\n        require_digest(record.get('sha256'),'complete radial array '+name)\n        shape=[7377] if name.startswith('parent_') else [P]\n        dtype='int64' if name in ('cells','parent_stage_map') else 'float64'\n        if record.get('shape')!=shape or record.get('dtype')!=dtype:\n            raise ValueError('The full radial observation array has the wrong shape or dtype: '+name)\n    return dict(layout_identity_sha256=canonical(rad),\n        exact_affine_reference_identity_sha256=canonical(query),\n        radial_observation_identity_sha256=canonical(observations))\n\n"
   ],
   [
    14386,
    14445,
    "    for key in ('fixed_chart_core_sha256', 'mesh_sha256'):\n",
    "    for key in ('fixed_chart_core_sha256',):\n"
   ],
   [
    14624,
    14755,
    "    if (base.get('M') != 320 or base.get('current_M') != 320\n            or base.get('reference_M') != 160 or base.get('J') != 923\n",
    "    _radial_binding(base,reference)\n    if (base.get('M') != 160 or base.get('reference_J') != 923\n            or base.get('current_J') != 1845 or base.get('J') != 1845\n"
   ]
  ]
 },
 "calibration": {
  "parent": {
   "path": "scripts/resume_20261126/frequency_refined_public_reference_calibration.py",
   "sha256": "b72572b13f94bf5482ced96c06aa940b5097ace270c159ec1837495519d9387a",
   "bytes": 12345
  },
  "output": {
   "name": "radial_refined_public_reference_calibration.py",
   "bytes": 12760,
   "sha256": "c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178"
  },
  "patches": [
   [
    657,
    933,
    "ENDPOINT_SCHEMA = 'complete-frequency-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nBASE_SOURCE = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'\nBASE_SCHEMA = 'complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1'\n",
    "ENDPOINT_SCHEMA = 'complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nBASE_SOURCE = '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'\nBASE_SCHEMA = 'complete-R711-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1'\n"
   ],
   [
    4329,
    4540,
    "        if (base.reference_M != 160 or base.M != 320 or core.shape != (320,)\n                or core[:160].tobytes() != base.parent_core.tobytes()\n                or np.any(core[160:] != 0) or np.any(jets != 0)\n",
    "        if (base.M != 160 or base.reference_J != 923 or base.J != 1845\n                or core.shape != (160,) or core.tobytes() != base.parent_core.tobytes()\n                or jets.shape != (1845,3,482) or np.any(jets != 0)\n                or base.model['radial_layout_identity_sha256'] != canonical(base.radial_layout_definition)\n"
   ],
   [
    5160,
    5329,
    "            reference_point_coordinate_layout='new M320 zero embedding of the frozen M160 core/H with all omega zero',\n            frozen_reference_M=160,current_M=320,\n",
    "            reference_point_coordinate_layout='new J1845 all-zero outer omega with the frozen original J923/M160 core and H',\n            frozen_reference_M=160,current_M=160,frozen_reference_J=923,current_J=1845,\n            complete_radial_layout_identity_sha256=base.radial_layout_identity,\n            exact_affine_reference_identity_sha256=base.exact_affine_reference.identity,\n            current_observation_identity_sha256=base.radial_observations.identity,\n"
   ]
  ]
 },
 "stage_jacobian": {
  "parent": {
   "path": "scripts/resume_20261126/frequency_refined_public_reference_stage_jacobian.py",
   "sha256": "2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2",
   "bytes": 24227
  },
  "output": {
   "name": "radial_refined_public_reference_stage_jacobian.py",
   "bytes": 24224,
   "sha256": "0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9"
  },
  "patches": [
   [
    674,
    861,
    "ENDPOINT_SCHEMA = 'complete-frequency-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nBASE_SOURCE_SHA256 = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'\n",
    "ENDPOINT_SCHEMA = 'complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nBASE_SOURCE_SHA256 = '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'\n"
   ]
  ]
 },
 "normal_frame": {
  "parent": {
   "path": "scripts/resume_20261126/frequency_refined_public_reference_normal_frame.py",
   "sha256": "787825f17de647598099fe7b4cbfc3d82b6ad90eac9943de6b67f653f092520a",
   "bytes": 33671
  },
  "output": {
   "name": "radial_refined_public_reference_normal_frame.py",
   "bytes": 33668,
   "sha256": "8fb0f326356d8e94337d51bfba85068c5872453df8f08e6619f241dfe7f715ce"
  },
  "patches": [
   [
    725,
    912,
    "ENDPOINT_SCHEMA = 'complete-frequency-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nBASE_SOURCE_SHA256 = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'\n",
    "ENDPOINT_SCHEMA = 'complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nBASE_SOURCE_SHA256 = '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'\n"
   ]
  ]
 },
 "frame_c1": {
  "parent": {
   "path": "scripts/resume_20261126/frequency_refined_public_reference_frame_c1.py",
   "sha256": "f272aaa95e63867d18015d9e92fa321f36785459377433a4433382794ae9c15a",
   "bytes": 35894
  },
  "output": {
   "name": "radial_refined_public_reference_frame_c1.py",
   "bytes": 35894,
   "sha256": "bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e"
  },
  "patches": [
   [
    1188,
    1286,
    "ANALYTIC_STAGE_SOURCE_SHA256 = '2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2'\n",
    "ANALYTIC_STAGE_SOURCE_SHA256 = '0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9'\n"
   ],
   [
    1310,
    1391,
    "BASE_SOURCE = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'\n",
    "BASE_SOURCE = '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'\n"
   ]
  ]
 },
 "stage_matrices": {
  "parent": {
   "path": "scripts/resume_20261126/frequency_refined_public_reference_stage_matrices.py",
   "sha256": "d7a6ebc317637667a18b8fb58ac8717aba8cbada981a349027bcaa60b448e4b7",
   "bytes": 47775
  },
  "output": {
   "name": "radial_refined_public_reference_stage_matrices.py",
   "bytes": 47775,
   "sha256": "fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387"
  },
  "patches": [
   [
    1408,
    1506,
    "ANALYTIC_STAGE_SOURCE_SHA256 = '2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2'\n",
    "ANALYTIC_STAGE_SOURCE_SHA256 = '0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9'\n"
   ],
   [
    1530,
    1622,
    "FRAME_C1_SOURCE_SHA256 = 'f272aaa95e63867d18015d9e92fa321f36785459377433a4433382794ae9c15a'\n",
    "FRAME_C1_SOURCE_SHA256 = 'bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e'\n"
   ],
   [
    1726,
    1814,
    "BASE_SOURCE_SHA256 = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'\n",
    "BASE_SOURCE_SHA256 = '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'\n"
   ]
  ]
 },
 "adjacent_matrices": {
  "parent": {
   "path": "scripts/resume_20261126/frequency_refined_public_reference_adjacent_matrices.py",
   "sha256": "610805744bdb5f4826d0c3a63bb769c9744639734db232ec31b3dbeaa0f89569",
   "bytes": 36761
  },
  "output": {
   "name": "radial_refined_public_reference_adjacent_matrices.py",
   "bytes": 36761,
   "sha256": "3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4"
  },
  "patches": [
   [
    746,
    844,
    "ANALYTIC_STAGE_SOURCE_SHA256 = '2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2'\n",
    "ANALYTIC_STAGE_SOURCE_SHA256 = '0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9'\n"
   ],
   [
    868,
    1056,
    "FRAME_C1_SOURCE_SHA256 = 'f272aaa95e63867d18015d9e92fa321f36785459377433a4433382794ae9c15a'\nSTAGE_MATRIX_SOURCE_SHA256 = 'd7a6ebc317637667a18b8fb58ac8717aba8cbada981a349027bcaa60b448e4b7'\n",
    "FRAME_C1_SOURCE_SHA256 = 'bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e'\nSTAGE_MATRIX_SOURCE_SHA256 = 'fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387'\n"
   ],
   [
    1155,
    1243,
    "BASE_SOURCE_SHA256 = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'\n",
    "BASE_SOURCE_SHA256 = '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'\n"
   ]
  ]
 },
 "normal": {
  "parent": {
   "path": "scripts/resume_20261126/so3_frequency_refined_public_reference_normal_lift.py",
   "sha256": "014fd521d315db223590d45b9b4d4da4e09975036044e533f601dcab636731d9",
   "bytes": 96556
  },
  "output": {
   "name": "so3_radial_refined_public_reference_normal_lift.py",
   "bytes": 96539,
   "sha256": "8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5"
  },
  "patches": [
   [
    718,
    1004,
    "SCHEMA = 'complete-frequency-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nANALYTIC_STAGE_SOURCE_SHA256 = '2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2'\nANALYTIC_FRAME_SOURCE_SHA256 = '787825f17de647598099fe7b4cbfc3d82b6ad90eac9943de6b67f653f092520a'\n",
    "SCHEMA = 'complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1'\nANALYTIC_STAGE_SOURCE_SHA256 = '0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9'\nANALYTIC_FRAME_SOURCE_SHA256 = '8fb0f326356d8e94337d51bfba85068c5872453df8f08e6619f241dfe7f715ce'\n"
   ],
   [
    1907,
    2435,
    "REFERENCE_CENTERING_SOURCE_SHA256 = 'b72572b13f94bf5482ced96c06aa940b5097ace270c159ec1837495519d9387a'\nNEW_REFERENCE_INPUT_SCHEMA = 'frequency-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'\nNEW_REFERENCE_INPUT_BINDER_SHA256 = 'bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971'\nSUPPORTED_BASE_SCHEMA = 'complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1'\nSUPPORTED_BASE_SOURCE_SHA256 = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'\n",
    "REFERENCE_CENTERING_SOURCE_SHA256 = 'c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178'\nNEW_REFERENCE_INPUT_SCHEMA = 'radial-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'\nNEW_REFERENCE_INPUT_BINDER_SHA256 = '59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652'\nSUPPORTED_BASE_SCHEMA = 'complete-R711-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1'\nSUPPORTED_BASE_SOURCE_SHA256 = '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'\n"
   ],
   [
    2743,
    3029,
    "FRAME_C1_SOURCE_SHA256 = 'f272aaa95e63867d18015d9e92fa321f36785459377433a4433382794ae9c15a'\nSTAGE_MATRIX_SOURCE_SHA256 = 'd7a6ebc317637667a18b8fb58ac8717aba8cbada981a349027bcaa60b448e4b7'\nADJACENT_FRAME_SOURCE_SHA256 = '610805744bdb5f4826d0c3a63bb769c9744639734db232ec31b3dbeaa0f89569'\n",
    "FRAME_C1_SOURCE_SHA256 = 'bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e'\nSTAGE_MATRIX_SOURCE_SHA256 = 'fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387'\nADJACENT_FRAME_SOURCE_SHA256 = '3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4'\n"
   ],
   [
    32991,
    33064,
    "        nu, core = tensor(self.reference_freq), tensor(self.parent_core)\n",
    "        nu, core = tensor(self.freq), tensor(self.parent_core)\n"
   ]
  ]
 },
 "packets": {
  "parent": {
   "path": "scripts/resume_20261126/immutable_frequency_refined_public_reference_root_packets.py",
   "sha256": "4b352626ed6f306bcdb1dc0126131c8f9fb4ab3d081376ae70739ec7c9d752f9",
   "bytes": 69734
  },
  "output": {
   "name": "immutable_radial_refined_public_reference_root_packets.py",
   "bytes": 69728,
   "sha256": "8d2b93dd055cc600aac14183d060d101421a924590c1fe8300625931bc8c0403"
  },
  "patches": [
   [
    635,
    722,
    "SCHEMA = 'immutable-frequency-refined-public-reference-analytic-frame-root-packets-v1'\n",
    "SCHEMA = 'immutable-radial-refined-public-reference-analytic-frame-root-packets-v1'\n"
   ],
   [
    916,
    1487,
    "    '014fd521d315db223590d45b9b4d4da4e09975036044e533f601dcab636731d9': {'schema': 'complete-frequency-refined-public-reference-analytic-frame-normal-plane-SO3-v1', 'base': '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2', 'adjacent': '610805744bdb5f4826d0c3a63bb769c9744639734db232ec31b3dbeaa0f89569', 'calibration': 'b72572b13f94bf5482ced96c06aa940b5097ace270c159ec1837495519d9387a', 'analytic': '2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2', 'analytic_frame': '787825f17de647598099fe7b4cbfc3d82b6ad90eac9943de6b67f653f092520a'},\n",
    "    '8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5': {'schema': 'complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1', 'base': '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0', 'adjacent': '3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4', 'calibration': 'c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178', 'analytic': '0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9', 'analytic_frame': '8fb0f326356d8e94337d51bfba85068c5872453df8f08e6619f241dfe7f715ce'},\n"
   ],
   [
    3286,
    3367,
    "        base='41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2',\n",
    "        base='130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0',\n"
   ]
  ]
 }
};
