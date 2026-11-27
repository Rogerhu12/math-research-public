#!/usr/bin/env node
// Complete pure-text provenance reconstruction. No generated Python is imported
// or executed. This source utility is not a scientific admission prerequisite.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const JOBS = [
  {
    "role": "layout",
    "parent": {
      "name": "radial_bisection_layout.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/radial_bisection_layout.py",
      "bytes": 18923,
      "sha256": "cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744",
      "git_blob_sha": "50304523b343957632dc25de61de403b8ca3bad4"
    },
    "output": {
      "name": "fixed_fejer_radial_bisection_layout.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_radial_bisection_layout.py",
      "bytes": 18929,
      "sha256": "a31d80a953722cc3644f793e4a28a372d980f6d0af7c8d98402f5f4739e3b5cf",
      "git_blob_sha": "7374adfdd1cfef17d15aae80d7dd88295d518440"
    },
    "transactions": [
      {
        "before": "complete-fixed-reference-SO3-J923-to-J1845-dyadic-layout-v1",
        "after": "complete-fixed-fejer-reference-SO3-J923-to-J1845-dyadic-layout-v1",
        "count": 1
      },
      {
        "before": "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3",
        "after": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
        "count": 1
      },
      {
        "before": "R690-independent-axisymmetric-SO3-reference-input-v1",
        "after": "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1",
        "count": 1
      }
    ]
  },
  {
    "role": "affine",
    "parent": {
      "name": "exact_affine_supported_reference.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/exact_affine_supported_reference.py",
      "bytes": 23435,
      "sha256": "2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117",
      "git_blob_sha": "1c7f9ddde0b94692b792cca40cf466046e30ed5b"
    },
    "output": {
      "name": "fixed_fejer_exact_affine_supported_reference.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_exact_affine_supported_reference.py",
      "bytes": 23452,
      "sha256": "622e50feab2dcd65b0191a880375a6fb064be2382a8fd576f09e08a69ac6fd95",
      "git_blob_sha": "0ef1acf9c39f41ee932baebd76b8feb68db2e8a7"
    },
    "transactions": [
      {
        "before": "complete-supported-smooth-triangle-exact-affine-query-v1",
        "after": "complete-fixed-fejer-supported-meridian-exact-affine-query-v1",
        "count": 1
      },
      {
        "before": "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b",
        "after": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
        "count": 1
      },
      {
        "before": "complete-supported-smooth-triangle-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1",
        "count": 1
      },
      {
        "before": "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3",
        "after": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
        "count": 1
      },
      {
        "before": "R690-independent-axisymmetric-SO3-reference-input-v1",
        "after": "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1",
        "count": 1
      }
    ]
  },
  {
    "role": "observations",
    "parent": {
      "name": "complete_dyadic_radial_observations.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/complete_dyadic_radial_observations.py",
      "bytes": 28167,
      "sha256": "2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74",
      "git_blob_sha": "e7ab1d8f3a52720e484fc4531156d8e233d592ab"
    },
    "output": {
      "name": "fixed_fejer_complete_dyadic_radial_observations.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_dyadic_radial_observations.py",
      "bytes": 28203,
      "sha256": "a89cb4f660f56ccc49e6f59191730aacc414cb36714ec64c2061784d3215f07d",
      "git_blob_sha": "54a8322239c739dd9ea38bfa91827f765c7fd789"
    },
    "transactions": [
      {
        "before": "complete-fixed-target-dyadic-radial-observation-union-v1",
        "after": "complete-fixed-fejer-target-dyadic-radial-observation-union-v1",
        "count": 1
      },
      {
        "before": "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3",
        "after": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
        "count": 1
      },
      {
        "before": "cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744",
        "after": "a31d80a953722cc3644f793e4a28a372d980f6d0af7c8d98402f5f4739e3b5cf",
        "count": 1
      },
      {
        "before": "def counted_tail_class(deep_module):\n    \"\"\"New controller; inherited exact definition and all scalar kernels stay original.\"\"\"\n    class ReconstructedTail(deep_module.DeepValleyTail):\n        def __init__(self, full, *, original_input_identity, target_leaves,\n                     epsilon, integral_tolerance, historical_clock_seconds):\n            self.reconstruction_leaf_target = int(target_leaves)\n            if self.reconstruction_leaf_target < 1:\n                raise ValueError('A real positive recorded live-leaf count is required')\n            super().__init__(full, input_identity=original_input_identity,\n                epsilon=epsilon, integral_tolerance=integral_tolerance,\n                admission_seconds=historical_clock_seconds)\n\n        def _build_integral_table(self):\n            # The original e091 table body is preserved below except that its\n            # wall-clock admission comparison is replaced by the observed\n            # live-leaf count.  All per-leaf operations and tie order are exact.\n            tail = self._tail_integrals(self.epsilon)\n            points = sorted(set((self.epsilon,F(1,8),F(1,4))))\n            live,heap,sequence = {},[],0\n            total = list(tail)\n            def admit(leaf):\n                nonlocal sequence\n                sequence += 1\n                live[sequence] = leaf\n                width = sum(value[1]-value[0] for value in leaf['values'])\n                heapq.heappush(heap,(-width,sequence))\n                for j in range(2):\n                    total[j] = deep_module.add(total[j],leaf['values'][j])\n            for low,high in zip(points,points[1:]):\n                admit(self._leaf(low,high))\n            count = len(live)\n            while heap:\n                uncertainty = max(F(value[1]-value[0],deep_module.SCALE)*self.width\n                                  for value in total)\n                if uncertainty <= self.integration_tolerance:\n                    break\n                if len(live) >= self.reconstruction_leaf_target:\n                    break\n                _,key = heapq.heappop(heap)\n                leaf = live.pop(key)\n                for j in range(2):\n                    total[j] = (total[j][0]-leaf['values'][j][0],\n                                total[j][1]-leaf['values'][j][1])\n                middle = (leaf['low']+leaf['high'])/2\n                admit(self._leaf(leaf['low'],middle))\n                admit(self._leaf(middle,leaf['high']))\n                count += 2\n            self.leaves = sorted(live.values(),key=lambda leaf:leaf['low'])\n            self.total_integrals_dimensionless = tuple(total)\n            self.leaves_evaluated = count\n            self.integral_uncertainty = max(F(value[1]-value[0],deep_module.SCALE)*self.width\n                                            for value in total)\n            self.requested_integral_accuracy_reached = (\n                self.integral_uncertainty <= self.integration_tolerance)\n            if len(self.leaves) != self.reconstruction_leaf_target:\n                raise ArithmeticError('The original accuracy stop preceded the recorded leaf count')\n    return ReconstructedTail\n\n\n",
        "after": "def counted_tail_class(deep_module):\n    \"\"\"A declared fixed-work table; exact scalar kernels and integer tie order stay original.\"\"\"\n    class ReconstructedTail(deep_module.DeepValleyTail):\n        def __init__(self, full, *, original_input_identity, target_leaves,\n                     epsilon, integral_tolerance, historical_clock_seconds):\n            self.reconstruction_leaf_target = int(target_leaves)\n            if self.reconstruction_leaf_target < 1:\n                raise ValueError('A positive predeclared deterministic live-leaf count is required')\n            super().__init__(full, input_identity=original_input_identity,\n                epsilon=epsilon, integral_tolerance=integral_tolerance,\n                admission_seconds=historical_clock_seconds)\n\n        def _build_integral_table(self):\n            # The original e091 table body is preserved below except that its\n            # wall-clock admission comparison is replaced by the predeclared\n            # live-leaf count.  All per-leaf operations and tie order are exact.\n            tail = self._tail_integrals(self.epsilon)\n            points = sorted(set((self.epsilon,F(1,8),F(1,4))))\n            live,heap,sequence = {},[],0\n            total = list(tail)\n            def admit(leaf):\n                nonlocal sequence\n                sequence += 1\n                live[sequence] = leaf\n                width = sum(value[1]-value[0] for value in leaf['values'])\n                heapq.heappush(heap,(-width,sequence))\n                for j in range(2):\n                    total[j] = deep_module.add(total[j],leaf['values'][j])\n            for low,high in zip(points,points[1:]):\n                admit(self._leaf(low,high))\n            count = len(live)\n            while heap:\n                uncertainty = max(F(value[1]-value[0],deep_module.SCALE)*self.width\n                                  for value in total)\n                if uncertainty <= self.integration_tolerance:\n                    break\n                if len(live) >= self.reconstruction_leaf_target:\n                    break\n                _,key = heapq.heappop(heap)\n                leaf = live.pop(key)\n                for j in range(2):\n                    total[j] = (total[j][0]-leaf['values'][j][0],\n                                total[j][1]-leaf['values'][j][1])\n                middle = (leaf['low']+leaf['high'])/2\n                admit(self._leaf(leaf['low'],middle))\n                admit(self._leaf(middle,leaf['high']))\n                count += 2\n            self.leaves = sorted(live.values(),key=lambda leaf:leaf['low'])\n            self.total_integrals_dimensionless = tuple(total)\n            self.leaves_evaluated = count\n            self.integral_uncertainty = max(F(value[1]-value[0],deep_module.SCALE)*self.width\n                                            for value in total)\n            self.requested_integral_accuracy_reached = (\n                self.integral_uncertainty <= self.integration_tolerance)\n            if len(self.leaves) != self.reconstruction_leaf_target:\n                raise ArithmeticError('The exact accuracy stop preceded the declared fixed-work leaf count')\n    return ReconstructedTail\n\n\n\n",
        "count": 1
      }
    ]
  },
  {
    "role": "base",
    "parent": {
      "name": "so3_radial_refined_public_reference_meridian_operator.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_radial_refined_public_reference_meridian_operator.py",
      "bytes": 45749,
      "sha256": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0",
      "git_blob_sha": "9851a696fea6d07690d61dbe23452c185fc4485d"
    },
    "output": {
      "name": "fixed_fejer_radial_refined_meridian_operator.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_radial_refined_meridian_operator.py",
      "bytes": 45823,
      "sha256": "78ded2682f5a42bc44a1939e9d814eec17254d1385dfe08a545d6aee109892ef",
      "git_blob_sha": "f924383de380d1117c48633855687055c13b3fa6"
    },
    "transactions": [
      {
        "before": "complete-R711-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1",
        "count": 1
      },
      {
        "before": "cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744",
        "after": "a31d80a953722cc3644f793e4a28a372d980f6d0af7c8d98402f5f4739e3b5cf",
        "count": 1
      },
      {
        "before": "2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117",
        "after": "622e50feab2dcd65b0191a880375a6fb064be2382a8fd576f09e08a69ac6fd95",
        "count": 1
      },
      {
        "before": "2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74",
        "after": "a89cb4f660f56ccc49e6f59191730aacc414cb36714ec64c2061784d3215f07d",
        "count": 1
      },
      {
        "before": "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b",
        "after": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
        "count": 1
      },
      {
        "before": "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3",
        "after": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
        "count": 1
      },
      {
        "before": "complete-supported-smooth-triangle-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1",
        "count": 1
      },
      {
        "before": "frozen_material_chart='theta0(phi)=Theta_initial_warm_core(phi)'",
        "after": "frozen_material_chart='theta0(phi)=Theta_cbar(phi); predeclared RN-even64 Fejer B=1/4,n=7, not an optimized warm chart'",
        "count": 1
      }
    ]
  },
  {
    "role": "Q",
    "parent": {
      "name": "fixed_fejer_literal_zero_moment_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_literal_zero_moment_input.py",
      "bytes": 31409,
      "sha256": "ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3",
      "git_blob_sha": "172d2b82eca6496058d2c73560de86bada50f12d"
    },
    "output": {
      "name": "fixed_fejer_radial_literal_zero_moment_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_radial_literal_zero_moment_input.py",
      "bytes": 36238,
      "sha256": "2e0c056652b10b4158bc74ec1fd2cdae54e05fb439154a462d6f1e4eb717428c",
      "git_blob_sha": "def2762a906f138ae05a01d76a9a2124e5c0736a"
    },
    "transactions": [
      {
        "before": "fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1",
        "after": "fixed-fejer-radial-refined-supported-reference-literal-zero-endpoint-Q-input-v1",
        "count": 1
      },
      {
        "before": "fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1",
        "after": "fixed-fejer-radial-refined-supported-reference-literal-two-bubble-endpoint-Q-v1",
        "count": 1
      },
      {
        "before": "complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1",
        "count": 1
      },
      {
        "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
        "after": "78ded2682f5a42bc44a1939e9d814eec17254d1385dfe08a545d6aee109892ef",
        "count": 1
      },
      {
        "before": "def _current_binding",
        "after": "def _radial_source_module(name,expected,method):\n    import importlib.util\n    import sys\n    path=Path(__file__).resolve().with_name(name)\n    if sha(path)!=expected:\n        raise ValueError('The complete radial model consumer source changed: '+name)\n    key='_radial_literal_Q_'+expected\n    module=sys.modules.get(key)\n    if module is None:\n        spec=importlib.util.spec_from_file_location(key,path)\n        module=importlib.util.module_from_spec(spec)\n        sys.modules[key]=module\n        spec.loader.exec_module(module)\n    function=getattr(module,method)\n    if sha(function.__code__.co_filename)!=expected:\n        raise ValueError('The complete radial consumer method changed: '+method)\n    return module\n\n\ndef _radial_binding(base,reference):\n    layout_source='a31d80a953722cc3644f793e4a28a372d980f6d0af7c8d98402f5f4739e3b5cf'\n    affine_source='622e50feab2dcd65b0191a880375a6fb064be2382a8fd576f09e08a69ac6fd95'\n    observations_source='a89cb4f660f56ccc49e6f59191730aacc414cb36714ec64c2061784d3215f07d'\n    layout=_radial_source_module('fixed_fejer_radial_bisection_layout.py',layout_source,'validate_definition')\n    affine=_radial_source_module('fixed_fejer_exact_affine_supported_reference.py',affine_source,'validate_definition')\n    observer=_radial_source_module('fixed_fejer_complete_dyadic_radial_observations.py',observations_source,'definition')\n    rad=base.get('radial_layout_definition')\n    if (base.get('radial_layout_source_sha256')!=layout_source\n            or not isinstance(rad,dict)\n            or layout.validate_definition(rad)!=base.get('radial_layout_identity_sha256')\n            or rad.get('complete_original_reference_model')!=reference\n            or rad.get('current_mesh_sha256')!=base.get('mesh_sha256')\n            or rad.get('reference_mesh_sha256')!=reference.get('mesh_sha256')\n            or base.get('reference_mesh_sha256')!=reference.get('mesh_sha256')\n            or base.get('M')!=160 or base.get('J')!=1845\n            or base.get('reference_J')!=923 or base.get('current_J')!=1845\n            or base.get('all_original_outer_free_variables_retained_and_new_radial_jets_added') is not True\n            or base.get('current_norm_layout_changed') is not True\n            or base.get('reference_seed_and_material_chart_unchanged') is not True\n            or base.get('frozen_reference_radial_mesh_unchanged') is not True\n            or base.get('current_row_rule_changed_and_common_parent_functional_required') is not True):\n        raise ValueError('Keep the full accurate current/reference radial split and all newly free jets')\n    query=base.get('exact_affine_reference_definition')\n    if (base.get('exact_affine_reference_source_sha256')!=affine_source\n            or not isinstance(query,dict)\n            or affine.validate_definition(query)!=base.get('exact_affine_reference_identity_sha256')\n            or query.get('complete_original_seed_model')!=base.get('fixed_supported_unit_seed_model')\n            or query.get('original_reference_identity_sha256')!=canonical(reference)):\n        raise ValueError('Bind the entire exact-affine query path to the same unchanged reference')\n    observations=base.get('radial_observation_definition')\n    if (base.get('radial_observation_source_sha256')!=observations_source\n            or not isinstance(observations,dict)\n            or canonical(observations)!=base.get('radial_observation_identity_sha256')):\n        raise ValueError('Bind the whole complete native-plus-parent observation rule')\n    expected=observer.definition(reference,rad,\n        observation_arrays=observations.get('complete_observation_arrays'))\n    if observations!=expected:\n        raise ValueError('Do not omit old observations, alter their scalar target or replace the positive rule')\n    arrays=observations['complete_observation_arrays']\n    P=arrays['cells']['shape']\n    if (not isinstance(P,list) or len(P)!=1 or type(P[0]) is not int\n            or not 14753<=P[0]<=22130):\n        raise ValueError('Keep all native rows and every original row in the complete union')\n    P=P[0]\n    for name,record in arrays.items():\n        require_digest(record.get('sha256'),'complete radial array '+name)\n        shape=[7377] if name.startswith('parent_') else [P]\n        dtype='int64' if name in ('cells','parent_stage_map') else 'float64'\n        if record.get('shape')!=shape or record.get('dtype')!=dtype:\n            raise ValueError('The full radial observation array has the wrong shape or dtype: '+name)\n    return dict(layout_identity_sha256=canonical(rad),\n        exact_affine_reference_identity_sha256=canonical(query),\n        radial_observation_identity_sha256=canonical(observations))\n\ndef _current_binding",
        "count": 1
      },
      {
        "before": "for key in ('fixed_chart_core_sha256', 'mesh_sha256'):",
        "after": "for key in ('fixed_chart_core_sha256',):",
        "count": 1
      },
      {
        "before": "    if (base.get('M') != 160 or base.get('J') != 923\n",
        "after": "    _radial_binding(base,reference)\n    if (base.get('M') != 160 or base.get('reference_J') != 923\n            or base.get('current_J') != 1845 or base.get('J') != 1845\n",
        "count": 1
      },
      {
        "before": "base/4e/e091 target",
        "after": "base/e717/e091 target",
        "count": 1
      }
    ]
  }
];
const argv=process.argv.slice(2);
if(argv.length!==4 || argv[0]!=='--source-directory' || argv[2]!=='--output-directory')
  throw Error('Use --source-directory COMPLETE_PARENT_SCRIPTS --output-directory FRESH_DIRECTORY');
const source=path.resolve(argv[1]),out=path.resolve(argv[3]);
if(source===out || out.startsWith(source+path.sep) || fs.existsSync(out))
  throw Error('Use an absent independent output directory');
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
function bound(raw,record,label){
  if(raw.length!==record.bytes || digest(raw)!==record.sha256)throw Error('Whole source differs: '+label);
}
const ready=[];
for(const job of JOBS){
  const raw=fs.readFileSync(path.join(source,job.parent.name));bound(raw,job.parent,job.parent.name);
  const parent=raw.toString('utf8');if(!Buffer.from(parent,'utf8').equals(raw))throw Error('UTF-8 parent required');
  let body=parent;
  for(const op of job.transactions){
    if(op.before===op.after || body.split(op.before).length-1!==op.count)throw Error('Exact forward span: '+job.role);
    body=body.split(op.before).join(op.after);
  }
  const made=Buffer.from(body,'utf8');bound(made,job.output,job.output.name);
  let restored=body;
  for(const op of [...job.transactions].reverse()){
    if(restored.split(op.after).length-1!==op.count)throw Error('Exact reverse span: '+job.role);
    restored=restored.split(op.after).join(op.before);
  }
  if(restored!==parent)throw Error('Whole inverse source differs: '+job.role);
  ready.push({job,made});
}
fs.mkdirSync(out);
for(const {job,made}of ready)fs.writeFileSync(path.join(out,job.output.name),made,{flag:'wx'});
process.stdout.write(JSON.stringify({schema:'complete-fixed-fejer-J1845-base-text-reproduction-v1',outputs:JOBS.map(j=>j.output),whole_forward_and_inverse_equal:true,scientific_execution:false,source_reproduction_is_not_an_admission_gate:true},null,2)+'\n');
