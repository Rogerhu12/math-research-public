#!/usr/bin/env node
// Complete source-only text reproduction. This is not a scientific admission gate.
// It reads and writes complete UTF-8 sources; it does not import their Python modules.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const SPEC = {
  "schema": "complete-source-text-missing-angle-geometry-reproduction-v1",
  "parent": {
    "name": "so3_fixed_fejer_stage_point_geometry.py",
    "bytes": 70709,
    "sha256": "2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471",
    "git_blob_sha": "2677d379e87b359088177b244428894311348996"
  },
  "output": {
    "name": "so3_fixed_fejer_batched_missing_angle_geometry.py",
    "bytes": 88163,
    "sha256": "51b7a056baa6f81cac5d5acd5278d4258365f45bf5c98dd868cc520ecef7b898"
  },
  "patches": [
    {
      "label": "actual complete batching parent",
      "before": "\nSCHEMA = \"complete-fixed-fejer-immutable-point-envelope-world-geometry-v1\"",
      "after": "\nMISSING_ANGLE_BATCH_PARENT_GEOMETRY_SHA256 = '2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471'\nSCHEMA = \"complete-fixed-fejer-immutable-point-envelope-world-geometry-v1\"",
      "count": 1
    },
    {
      "label": "new geometry algorithm schema",
      "before": "SCHEMA = \"complete-fixed-fejer-immutable-point-envelope-world-geometry-v1\"",
      "after": "SCHEMA = \"complete-fixed-fejer-batched-missing-angle-envelope-world-geometry-v1\"",
      "count": 1
    },
    {
      "label": "whole-source analytic_J3",
      "before": "ANALYTIC_STAGE_SOURCE_SHA256 = '7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72'",
      "after": "ANALYTIC_STAGE_SOURCE_SHA256 = '223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811'",
      "count": 1
    },
    {
      "label": "whole-source endpoint",
      "before": "ENDPOINT_SOURCE_SHA256 = '42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10'",
      "after": "ENDPOINT_SOURCE_SHA256 = '388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4'",
      "count": 1
    },
    {
      "label": "whole-source stage_matrices",
      "before": "STAGE_MATRIX_SOURCE_SHA256 = 'e4d42910f9550a20d0afc16aab8f54b5ea1ceb18ace375128f3a79bfef0e76ce'",
      "after": "STAGE_MATRIX_SOURCE_SHA256 = 'f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791'",
      "count": 1
    },
    {
      "label": "whole-source adjacent_matrices",
      "before": "ADJACENT_FRAME_SOURCE_SHA256 = 'd04cf80d40a16410a2338f3b4b0c3bbdd0084cfc2ad5270bee21d33ded9449b5'",
      "after": "ADJACENT_FRAME_SOURCE_SHA256 = 'bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564'",
      "count": 1
    },
    {
      "label": "whole-source reference_calibration",
      "before": "REFERENCE_CENTERING_SOURCE_SHA256 = 'fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c'",
      "after": "REFERENCE_CENTERING_SOURCE_SHA256 = 'aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3'",
      "count": 1
    },
    {
      "label": "whole-source closure_values",
      "before": "CLOSURE_VALUE_SOURCE_SHA256 = '01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595'",
      "after": "CLOSURE_VALUE_SOURCE_SHA256 = '2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0'",
      "count": 1
    },
    {
      "label": "complete new endpoint schema",
      "before": "OPERATOR_SCHEMA = \"complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1\"",
      "after": "OPERATOR_SCHEMA = \"complete-fixed-fejer-detached-meridian-values-normal-layer-v1\"",
      "count": 1
    },
    {
      "label": "actual C1 helper source",
      "before": "'1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca'",
      "after": "'c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246'",
      "count": 1
    },
    {
      "label": "actual complete query-independent meridian producer",
      "before": "KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')",
      "after": "DETACHED_MERIDIAN_VALUES_SOURCE_SHA256 = '7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd'\nKEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')",
      "count": 1
    },
    {
      "label": "complete pure batching policy and result validator",
      "before": "\nclass GeometryScreen:\n",
      "after": "\nMISSING_ANGLE_BATCH_SCHEMA = 'complete-literal-missing-angle-normal-root-batching-v1'\n\n\ndef missing_angle_batch_policy():\n    return dict(schema=MISSING_ANGLE_BATCH_SCHEMA, source_sha256=sha(__file__),\n        operator_source_sha256=ENDPOINT_SOURCE_SHA256,\n        parent_geometry_source_sha256=MISSING_ANGLE_BATCH_PARENT_GEOMETRY_SHA256,\n        selection='actual explicit union insertion order; first occurrence of a missing literal phi only',\n        candidate_locations='only positions whose complete sixjets are absent from the current-point field cache',\n        batch_size='the unchanged actual operator angle_block',\n        requested_angular_order=2,\n        existing_cached_angles_never_recomputed_by_this_preparation=True,\n        existing_first_order_angles_keep_original_pointwise_upgrade=True,\n        original_get_roots_and_all_normal_stages_used=True,\n        every_original_explicit_point_read_and_aggregation_order_retained=True,\n        no_geometric_constraint_or_point_removed=True,\n        original_active_J_and_Jtranspose_paths_unchanged=True,\n        original_stage_and_final_endpoint_rereads_retained=True,\n        working_words_equal_to_original_singleton_evaluation_claimed=False,\n        continuous_branch_or_field_certificate_claimed=False)\n\n\ndef validate_missing_angle_batches(value, *, model_identity, point_sha256,\n                                   geometry_complete):\n    \"\"\"Pure metadata validation; this never evaluates a field or supplies a missing result.\"\"\"\n    if not isinstance(value, dict) or value.get('schema') != MISSING_ANGLE_BATCH_SCHEMA:\n        raise ValueError('Keep the complete actual missing-angle batching record')\n    policy = missing_angle_batch_policy()\n    if (value.get('policy') != policy\n            or value.get('policy_identity_sha256') != canonical(policy)\n            or value.get('actual_model_identity_sha256') != model_identity\n            or value.get('current_full_point_sha256') != point_sha256\n            or value.get('original_point_order_changed') is not False\n            or value.get('geometric_points_skipped') != 0\n            or value.get('same_working_words_as_original_singleton_roots_claimed') is not False):\n        raise ValueError('Bind actual batching policy, source, model and complete point')\n    count = value.get('original_union_location_count')\n    read = value.get('original_point_reads_completed')\n    counter_names = ('original_point_reads_completed', 'geometric_points_skipped',\n        'field_cache_already_complete_locations', 'existing_cached_root_angle_count',\n        'existing_first_order_angles_left_to_original_upgrade')\n    for name in counter_names:\n        if type(value.get(name)) is not int or value[name] < 0:\n            raise ValueError('Keep actual nonnegative point/root counters: '+name)\n    if count is None:\n        if any(value[name] for name in counter_names):\n            raise ValueError('No completed explicit reads are invented before the union exists')\n    elif (type(count) is not int or count < 0\n            or any(value[name] > count for name in counter_names)):\n        raise ValueError('The whole original union bounds every actual completed read')\n    if (value['existing_first_order_angles_left_to_original_upgrade']\n            > value['existing_cached_root_angle_count']\n            or type(value.get('original_point_loop_complete')) is not bool\n            or type(value.get('normal_stage_count')) is not int\n            or value['normal_stage_count'] < 1):\n        raise ValueError('Keep the actual full normal partition and original upgrade counts')\n    if geometry_complete and (count is None or read != count\n            or value.get('original_point_loop_complete') is not True):\n        raise ValueError('A complete geometry result retains every original explicit point')\n    records = value.get('batches')\n    if not isinstance(records, list):\n        raise ValueError('Keep every attempted original missing-angle batch')\n    maximum = value.get('original_angle_block')\n    if type(maximum) is not int or maximum < 1:\n        raise ValueError('Keep the unchanged actual angle block')\n    plan = value.get('planned_missing_angles')\n    if not isinstance(plan, list):\n        raise ValueError('Keep the complete ordered literal-angle plan')\n    keys, positions = [], []\n    for item in plan:\n        if (not isinstance(item, dict) or type(item.get('first_union_position')) is not int\n                or count is None or not 0 <= item['first_union_position'] < count\n                or not isinstance(item.get('literal_phi_hex'), str)):\n            raise ValueError('Every planned angle keeps its actual first union address')\n        angle = float.fromhex(item['literal_phi_hex'])\n        if not math.isfinite(angle) or angle.hex() != item['literal_phi_hex']:\n            raise ValueError('Keep exact finite binary64 angle words')\n        keys.append(item['literal_phi_hex'])\n        positions.append(item['first_union_position'])\n    if (len(keys) != len(set(keys)) or len(positions) != len(set(positions))\n            or positions != sorted(positions)):\n        raise ValueError('Missing angles follow their unique first appearances, without sorting phi')\n    consumed = 0\n    for index, item in enumerate(records):\n        if (not isinstance(item, dict) or item.get('batch_index') != index\n                or item.get('requested_angular_order') != 2\n                or item.get('normal_stage_count') != value.get('normal_stage_count')\n                or item.get('current_full_point_sha256') != point_sha256\n                or type(item.get('returned')) is not bool):\n            raise ValueError('Bind every actual attempted batch and full normal partition')\n        actual = item.get('literal_angle_hex')\n        expected = keys[consumed:consumed+maximum]\n        if (not expected or actual != expected\n                or item.get('first_union_positions') != positions[consumed:consumed+maximum]):\n            raise ValueError('Batching may neither skip nor reorder the complete angle plan')\n        consumed += len(actual)\n        for prefix in ('normal', 'endpoint'):\n            before, after = item.get(prefix+'_counts_before'), item.get(prefix+'_counts_after')\n            delta = item.get(prefix+'_count_delta')\n            if (not all(isinstance(record, dict) for record in (before, after, delta))\n                    or set(before) != set(after) or set(before) != set(delta)\n                    or any(type(before[key]) is not int or before[key] < 0\n                        or type(after[key]) is not int or after[key] < before[key]\n                        or type(delta[key]) is not int or delta[key] != after[key]-before[key]\n                        for key in before)):\n                raise ValueError('Keep all actual original root counters and their complete deltas')\n        if item['returned']:\n            if (item.get('returned_angle_count') != len(actual)\n                    or item.get('all_original_stage_and_final_checks_returned') is not True\n                    or item.get('all_requested_roots_present_at_same_point') is not True):\n                raise ValueError('Do not upgrade a partial batch to a complete root return')\n            roots = item.get('returned_root_records')\n            if (not isinstance(roots, list) or len(roots) != len(actual)\n                    or any(not isinstance(root, dict)\n                        or root.get('all_normal_stages_returned') is not True\n                        or root.get('normal_stage_count') != value.get('normal_stage_count')\n                        or root.get('final_original_physical_endpoint_equation_checked') is not True\n                        for root in roots)):\n                raise ValueError('Keep every actual original root return record')\n        elif index != len(records)-1:\n            raise ValueError('No later batch follows an actual failed preparation')\n    status = value.get('root_preparation_status')\n    if status not in ('not-started', 'running', 'returned', 'failed'):\n        raise ValueError('Keep the actual preparation state')\n    if status == 'returned' and (consumed != len(keys)\n            or any(not item['returned'] for item in records)):\n        raise ValueError('A returned preparation covers its whole actual plan')\n    if value.get('root_preparation_complete') is not (status == 'returned'):\n        raise ValueError('Do not manufacture root preparation completion')\n    if geometry_complete and status != 'returned':\n        raise ValueError('A complete scan must finish its declared root preparation')\n    return dict(schema=MISSING_ANGLE_BATCH_SCHEMA, policy_identity_sha256=canonical(policy),\n        actual_model_identity_sha256=model_identity, current_full_point_sha256=point_sha256,\n        original_union_location_count=count, original_point_reads_completed=read,\n        original_angle_block=maximum, normal_stage_count=value['normal_stage_count'],\n        field_cache_already_complete_locations=value['field_cache_already_complete_locations'],\n        existing_cached_root_angle_count=value['existing_cached_root_angle_count'],\n        existing_first_order_angles_left_to_original_upgrade=value['existing_first_order_angles_left_to_original_upgrade'],\n        actual_missing_angle_count=len(keys), actual_batch_count=len(records),\n        actual_returned_batch_count=sum(item['returned'] for item in records),\n        root_preparation_status=status, original_point_loop_complete=value.get('original_point_loop_complete') is True,\n        no_geometric_point_removed=True, original_active_derivative_chain_unchanged=True,\n        working_singleton_words_inherited=False, scientific_evaluation_by_validator=False)\n\nclass GeometryScreen:\n",
      "count": 1
    },
    {
      "label": "bind the actual integration-data entry",
      "before": "        local_matrix = problem.analytic_stage_jacobian\n",
      "after": "        root_data_method = problem.detached_meridian_values.integration_data\n        if sha(root_data_method.__func__.__code__.co_filename) != DETACHED_MERIDIAN_VALUES_SOURCE_SHA256:\n            raise ValueError('Use the complete actual query-independent meridian data producer')\n        local_matrix = problem.analytic_stage_jacobian\n",
      "count": 1
    },
    {
      "label": "whole original root and point entry guards",
      "before": "('grid_fields', 'point_fields', 'point_vjp', 'prepare', 'domain', 'fields_torch'):",
      "after": "('grid_fields', 'point_fields', 'point_vjp', 'prepare', 'domain', 'fields_torch',\n                     '_select_point', '_get_roots'):",
      "count": 1
    },
    {
      "label": "initial honest batching state",
      "before": "        self._last_scan = None\n        self._radial_index = {}\n",
      "after": "        self._last_scan = None\n        self._missing_angle_batches = self._new_missing_angle_record(None)\n        self._radial_index = {}\n",
      "count": 1
    },
    {
      "label": "complete geometric source-binding policy",
      "before": "        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),\n",
      "after": "        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),\n            missing_angle_root_batch_policy=missing_angle_batch_policy(),\n            detached_meridian_value_source_sha256=DETACHED_MERIDIAN_VALUES_SOURCE_SHA256,\n",
      "count": 1
    },
    {
      "label": "complete new preparation methods",
      "before": "    def scan(self,x,witnesses=(),radius_witnesses=()):\n",
      "after": "\n    def _new_missing_angle_record(self, point_sha256):\n        policy = missing_angle_batch_policy()\n        return dict(schema=MISSING_ANGLE_BATCH_SCHEMA, policy=policy,\n            policy_identity_sha256=canonical(policy),\n            actual_model_identity_sha256=self.q.identity,\n            current_full_point_sha256=point_sha256,\n            original_angle_block=int(self.q.angle_block),\n            normal_stage_count=int(self.q.normal_stage_count),\n            original_union_location_count=None, original_union_address_order_identity_sha256=None,\n            original_point_reads_completed=0, original_point_loop_complete=False,\n            original_point_order_changed=False, geometric_points_skipped=0,\n            field_cache_already_complete_locations=0,\n            existing_cached_root_angle_count=0,\n            existing_first_order_angles_left_to_original_upgrade=0,\n            planned_missing_angles=[], batches=[],\n            root_preparation_status='not-started', root_preparation_complete=False,\n            same_working_words_as_original_singleton_roots_claimed=False)\n\n    def _prepare_missing_angle_batches(self, union):\n        \"\"\"Prefetch only roots that the unchanged explicit point loop would actually need.\"\"\"\n        q = self.q\n        value = self._missing_angle_batches\n        value['original_union_location_count'] = len(union)\n        ordered = [self._location(item) for item in union.values()]\n        if any(not self.envelope.contains(item) for item in ordered):\n            raise ValueError('A physical location escaped its complete declared envelope')\n        value['original_union_address_order_identity_sha256'] = canonical(\n            [list(_key(item)) for item in ordered])\n        if not ordered:\n            value.update(root_preparation_status='returned', root_preparation_complete=True)\n            return\n        # All subsequent field and point reads remain the original operations.\n        # The helper supplies the original query-independent integration data;\n        # this preparation does not construct a dummy physical query.\n        x = torch.as_tensor(self._x, dtype=torch.float64, device='cpu')\n        q._select_point(x)\n        if q._current_point_sha256 != self._token:\n            raise ValueError('Batch roots belong to the same complete actual scan point')\n        missing, seen, seen_existing = [], set(), set()\n        for ordinal, item in enumerate(ordered):\n            if _key(item) in self._field_cache:\n                value['field_cache_already_complete_locations'] += 1\n                continue\n            key = float(item['phi']).hex()\n            if key in q._root_cache:\n                if key not in seen_existing:\n                    seen_existing.add(key)\n                    value['existing_cached_root_angle_count'] += 1\n                    if q._root_cache[key]['order'] == 1:\n                        value['existing_first_order_angles_left_to_original_upgrade'] += 1\n                continue\n            if key not in seen:\n                seen.add(key)\n                missing.append(dict(literal_phi_hex=key, first_union_position=ordinal))\n        value['planned_missing_angles'] = missing\n        value['root_preparation_status'] = 'running'\n        for begin in range(0, len(missing), int(q.angle_block)):\n            planned = missing[begin:begin+int(q.angle_block)]\n            keys = [item['literal_phi_hex'] for item in planned]\n            if any(key in q._root_cache for key in keys):\n                raise ValueError('The declared missing-root batch changed before its actual execution')\n            record = dict(batch_index=len(value['batches']),\n                current_full_point_sha256=self._token,\n                literal_angle_hex=keys,\n                first_union_positions=[item['first_union_position'] for item in planned],\n                requested_angular_order=2, normal_stage_count=int(q.normal_stage_count),\n                returned=False, returned_angle_count=0,\n                all_original_stage_and_final_checks_returned=False,\n                all_requested_roots_present_at_same_point=False,\n                endpoint_counts_before=dict(q.endpoint_counts),\n                normal_counts_before=dict(q.normal_counts))\n            value['batches'].append(record)\n            try:\n                phi = np.asarray([float.fromhex(key) for key in keys], dtype=np.float64)\n                with torch.no_grad():\n                    data = q.detached_meridian_values.integration_data(x, phi, curvature=True)\n                    items = q._get_roots(data, phi, 2, need_linearization=False)\n                if (q._current_point_sha256 != self._token or len(items) != len(keys)\n                        or any(key not in q._root_cache for key in keys)\n                        or any(item['order'] != 2 or len(item['stages']) != q.normal_stage_count\n                            or item['record'].get('all_normal_stages_returned') is not True\n                            or item['record'].get('final_original_physical_endpoint_equation_checked') is not True\n                            for item in items)):\n                    raise ValueError('Keep every actual returned full normal chain at this complete point')\n                record.update(returned=True, returned_angle_count=len(items),\n                    all_original_stage_and_final_checks_returned=True,\n                    all_requested_roots_present_at_same_point=True,\n                    returned_root_records=json.loads(json.dumps([item['record'] for item in items],\n                                                               allow_nan=False)))\n            except BaseException as error:\n                record.update(error_type=type(error).__name__, error=str(error)[:1000])\n                value.update(root_preparation_status='failed', root_preparation_complete=False)\n                raise\n            finally:\n                record['endpoint_counts_after'] = dict(q.endpoint_counts)\n                record['normal_counts_after'] = dict(q.normal_counts)\n                record['endpoint_count_delta'] = {key:q.endpoint_counts[key]-count\n                    for key,count in record['endpoint_counts_before'].items()}\n                record['normal_count_delta'] = {key:q.normal_counts[key]-count\n                    for key,count in record['normal_counts_before'].items()}\n        value.update(root_preparation_status='returned', root_preparation_complete=True)\n\n    def scan(self,x,witnesses=(),radius_witnesses=()):\n",
      "count": 1
    },
    {
      "label": "new scan owns its actual point and partial record",
      "before": "            and np.isfinite(attempted).all() else None)\n        try:\n",
      "after": "            and np.isfinite(attempted).all() else None)\n        self._missing_angle_batches = self._new_missing_angle_record(attempted_token)\n        try:\n",
      "count": 1
    },
    {
      "label": "prefetch only the complete existing explicit union",
      "before": "            union.update(self._radius_memory)\n            point_records=[]\n",
      "after": "            union.update(self._radius_memory)\n            self._prepare_missing_angle_batches(union)\n            point_records=[]\n",
      "count": 1
    },
    {
      "label": "count a point only after its original complete geometric read",
      "before": "                    radius=point_radius,area=area,amplitude={key:float(v) for key,v in av.items()}))\n",
      "after": "                    radius=point_radius,area=area,amplitude={key:float(v) for key,v in av.items()}))\n                self._missing_angle_batches['original_point_reads_completed'] += 1\n",
      "count": 1
    },
    {
      "label": "complete original point loop remains explicit",
      "before": "            explicit_complete=True\n",
      "after": "            explicit_complete=True\n            self._missing_angle_batches['original_point_loop_complete'] = True\n",
      "count": 1
    },
    {
      "label": "freeze complete or partial batch provenance in every returned scan",
      "before": "            result['material_envelope']=self.envelope.observe_scan(result,\n",
      "after": "            result['missing_angle_root_batches'] = json.loads(json.dumps(\n                self._missing_angle_batches, allow_nan=False))\n            result['material_envelope']=self.envelope.observe_scan(result,\n",
      "count": 2
    }
  ]
};
const fail = message => { throw new Error(message); };
const digest = value => crypto.createHash('sha256').update(value,'utf8').digest('hex');
const bytes = value => Buffer.byteLength(value,'utf8');
const occurrences = (value, needle) => value.split(needle).length-1;
const args = process.argv.slice(2);
const allowed = new Set(['--source-directory','--generated-directory','--verify-existing']);
let sourceDirectory=null, generatedDirectory=null, verify=false;
for(let index=0; index<args.length; index++) {
  const key=args[index];
  if(!allowed.has(key)) fail('Unknown argument: '+key);
  if(key==='--verify-existing') { if(verify) fail('Repeated --verify-existing'); verify=true; continue; }
  const value=args[++index];
  if(value===undefined || value.startsWith('--')) fail('Missing argument value: '+key);
  if(key==='--source-directory') { if(sourceDirectory!==null) fail('Repeated source directory'); sourceDirectory=value; }
  else { if(generatedDirectory!==null) fail('Repeated generated directory'); generatedDirectory=value; }
}
if(sourceDirectory===null || generatedDirectory===null) fail('Provide complete source and generated directories');
const inputPath=path.resolve(sourceDirectory,SPEC.parent.name);
const outputPath=path.resolve(generatedDirectory,SPEC.output.name);
if(inputPath===outputPath) fail('The complete historical parent may not be overwritten');
const original=fs.readFileSync(inputPath,'utf8');
if(bytes(original)!==SPEC.parent.bytes || digest(original)!==SPEC.parent.sha256) fail('Complete parent source identity mismatch');
let result=original;
for(const patch of SPEC.patches) {
  if(occurrences(result,patch.before)!==patch.count) fail('Forward patch count differs: '+patch.label);
  result=result.split(patch.before).join(patch.after);
}
if(bytes(result)!==SPEC.output.bytes || digest(result)!==SPEC.output.sha256) fail('Complete generated source identity mismatch');
let restored=result;
for(const patch of [...SPEC.patches].reverse()) {
  if(occurrences(restored,patch.after)!==patch.count) fail('Inverse patch count differs: '+patch.label);
  restored=restored.split(patch.after).join(patch.before);
}
if(restored!==original || digest(restored)!==SPEC.parent.sha256) fail('Whole original parent was not restored');
if(verify) {
  const existing=fs.readFileSync(outputPath,'utf8');
  if(existing!==result) fail('Existing complete generated file differs');
} else {
  fs.mkdirSync(path.dirname(outputPath),{recursive:true});
  if(fs.existsSync(outputPath)) {
    if(fs.readFileSync(outputPath,'utf8')!==result) fail('Refuse to replace a different existing complete generated source');
  } else fs.writeFileSync(outputPath,result,{encoding:'utf8',flag:'wx'});
}
process.stdout.write(JSON.stringify({
  schema:SPEC.schema,parent:SPEC.parent,output:SPEC.output,
  patch_count:SPEC.patches.length,whole_inverse_restored:true,
  source_only:true,python_modules_imported:false,scientific_evaluations:0,
  independent_execution_gate_created:false,verify_existing:verify
},null,2)+'\n');
