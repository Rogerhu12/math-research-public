#!/usr/bin/env node
// Complete source-text reproduction only. No Python import, AST, F/J/root or fixture.
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const SPEC = [
  {
    "role": "geometry",
    "parent": {
      "role": "geometry",
      "name": "so3_fixed_fejer_halfwave_geometry.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_halfwave_geometry.py",
      "bytes": 88164,
      "sha256": "494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b",
      "git_blob_sha": "602ef5d9e322a3301ede97a811fa9b10044bc61b"
    },
    "output": {
      "role": "geometry",
      "name": "so3_fixed_fejer_halfwave_dk_cache_geometry.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_halfwave_dk_cache_geometry.py",
      "bytes": 88487,
      "sha256": "da9b1be0146e48aad117124b7fc84c1754ecb0a78d5adeaa683710c5f7a8b316",
      "git_blob_sha": "624871ceac5955b78fe2ba0728ff50ddee99d64d"
    },
    "patches": [
      {
        "old": "SCHEMA = \"complete-fixed-fejer-paired-halfwave-envelope-world-geometry-v1\"",
        "new": "SCHEMA = \"complete-fixed-fejer-paired-halfwave-dk-cache-world-geometry-v1\""
      },
      {
        "old": "SELECTOR_SHA256 = 'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'",
        "new": "SELECTOR_SHA256 = 'f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112'"
      },
      {
        "old": "scripts/'resume_20261120/fullclosed_point_inequalities_v2.py'",
        "new": "scripts/'resume_20261120/fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py'"
      },
      {
        "old": "            unchanged_original_selector_sha256=SELECTOR_SHA256,",
        "new": "            unchanged_original_selector_sha256='e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8',\n            current_selector_source_sha256=SELECTOR_SHA256,\n            current_selector_is_unchanged_original_source=False,\n            complete_curvature_pullback_cache_policy=self.selector.complete_curvature_pullback_cache_definition(),"
      }
    ]
  },
  {
    "role": "batched_geometry_binding",
    "parent": {
      "role": "batched_geometry_binding",
      "name": "fixed_fejer_halfwave_geometry_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_halfwave_geometry_binding.py",
      "bytes": 12118,
      "sha256": "45aedd26f59920938f6a6245dca48a06293f6cf1593124762a77063e4d0e5102",
      "git_blob_sha": "9c8d986ea6a601e552fa1c50782928dc5f391783"
    },
    "output": {
      "role": "batched_geometry_binding",
      "name": "fixed_fejer_halfwave_dk_cache_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_halfwave_dk_cache_binding.py",
      "bytes": 20546,
      "sha256": "ca2a7884039df93f7b5b243d476c60d2e8e810bf1071545a84bbc283a460aaad",
      "git_blob_sha": "319ed19012c7b588e85108a98ace0efcca830c75"
    },
    "patches": [
      {
        "old": "This module loads only two explicitly selected standard-library functions\nfrom the exact complete geometry source.",
        "new": "This module loads explicitly selected standard-library-only functions\nfrom the exact complete geometry and numerical-selector sources."
      },
      {
        "old": "SCHEMA = 'actual-fixed-fejer-halfwave-geometry-report-binding-v1'",
        "new": "SCHEMA = 'actual-fixed-fejer-halfwave-dk-cache-report-binding-v1'"
      },
      {
        "old": "GEOMETRY_NAME = 'so3_fixed_fejer_halfwave_geometry.py'",
        "new": "GEOMETRY_NAME = 'so3_fixed_fejer_halfwave_dk_cache_geometry.py'"
      },
      {
        "old": "GEOMETRY_SHA256 = '494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b'",
        "new": "GEOMETRY_SHA256 = 'da9b1be0146e48aad117124b7fc84c1754ecb0a78d5adeaa683710c5f7a8b316'"
      },
      {
        "old": "GEOMETRY_BYTES = 88164",
        "new": "GEOMETRY_BYTES = 88487"
      },
      {
        "old": "GEOMETRY_SCHEMA = 'complete-fixed-fejer-paired-halfwave-envelope-world-geometry-v1'",
        "new": "GEOMETRY_SCHEMA = 'complete-fixed-fejer-paired-halfwave-dk-cache-world-geometry-v1'"
      },
      {
        "old": "\ndef bind_report(report, *, source_by_role, geometry_source):",
        "new": "\nCURVATURE_SELECTOR_NAME = 'fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py'\nCURVATURE_SELECTOR_SHA256 = 'f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112'\nCURVATURE_SELECTOR_BYTES = 35982\nCURVATURE_CONSTANT_NAMES = ('_CURVATURE_CACHE_SCHEMA','_CURVATURE_CACHE_LIMIT',\n    '_CURVATURE_CACHE_NORMAL_SHA256','_CURVATURE_CACHE_MERIDIAN_SHA256')\nCURVATURE_FUNCTION_NAMES = ('_curvature_cache_sha',\n    'complete_curvature_pullback_cache_definition',\n    'validate_complete_curvature_pullback_cache')\n\n\ndef _selected_curvature_selector(path):\n    \"\"\"Read the complete selector; compile only its three original pure functions.\"\"\"\n    path = Path(path).resolve()\n    raw = path.read_bytes()\n    if (path.name != CURVATURE_SELECTOR_NAME or len(raw) != CURVATURE_SELECTOR_BYTES\n            or hashlib.sha256(raw).hexdigest() != CURVATURE_SELECTOR_SHA256):\n        raise ValueError('Keep the whole exact halfwave numerical-pullback selector')\n    tree = ast.parse(raw.decode('utf-8'), filename=str(path))\n    constants, functions = {}, {}\n    for node in tree.body:\n        if isinstance(node, ast.Assign):\n            names = [item.id for item in node.targets if isinstance(item, ast.Name)]\n            selected = [name for name in names if name in CURVATURE_CONSTANT_NAMES]\n            if selected:\n                if (len(node.targets) != 1 or len(names) != 1 or len(selected) != 1\n                        or selected[0] in constants):\n                    raise ValueError('Keep each complete pure selector constant exactly once')\n                constants[selected[0]] = node\n        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in CURVATURE_FUNCTION_NAMES:\n            if (not isinstance(node, ast.FunctionDef) or node.decorator_list\n                    or node.name in functions):\n                raise ValueError('Keep each original undecorated pure selector function')\n            functions[node.name] = node\n    if set(constants) != set(CURVATURE_CONSTANT_NAMES) or set(functions) != set(CURVATURE_FUNCTION_NAMES):\n        raise ValueError('Do not drop any complete pure numerical-cache definition or validator')\n    # The only nonliteral selected constant is the original 64*1024*1024.\n    # Its entire source is already hard bound above; no scientific body is selected.\n    nodes = [constants[name] for name in CURVATURE_CONSTANT_NAMES]\n    nodes += [functions[name] for name in CURVATURE_FUNCTION_NAMES]\n    namespace = dict(__file__=str(path), Path=Path, hashlib=hashlib)\n    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), 'exec'), namespace)\n    if (namespace['_CURVATURE_CACHE_SCHEMA'] != 'complete-same-point-returned-curvature-pullback-cache-v1'\n            or namespace['_CURVATURE_CACHE_LIMIT'] != 64*1024*1024\n            or not _sha_word(namespace['_CURVATURE_CACHE_NORMAL_SHA256'])\n            or not _sha_word(namespace['_CURVATURE_CACHE_MERIDIAN_SHA256'])):\n        raise ValueError('The original whole numerical-cache source policy differs')\n    for name in CURVATURE_FUNCTION_NAMES:\n        if (Path(namespace[name].__code__.co_filename).resolve() != path\n                or sha(namespace[name].__code__.co_filename) != CURVATURE_SELECTOR_SHA256):\n            raise ValueError('The actual pure selector function lost its complete-source identity')\n    if path.read_bytes() != raw:\n        raise ValueError('The entire numerical selector changed during pure binding')\n    return path, namespace\n\n\ndef _complete_curvature_cache_scopes(report, roles, geometry_path, identity):\n    path, pure = _selected_curvature_selector(\n        geometry_path.parent.parent/'resume_20261120'/CURVATURE_SELECTOR_NAME)\n    policy = pure['complete_curvature_pullback_cache_definition']()\n    if (roles.get('geometry_selector') != CURVATURE_SELECTOR_SHA256\n            or policy.get('source_sha256') != CURVATURE_SELECTOR_SHA256\n            or policy.get('old_source_normal_sha256') != roles.get('endpoint')\n            or policy.get('old_source_meridian_helper_sha256') != roles.get('detached_meridian_values')):\n        raise ValueError('Use the declared complete current normal, helper and selector source family')\n    scopes = []\n    for field, phase in (('metric_directions','metric'),('restoration_directions','restoration')):\n        directions = report.get(field, [])\n        if not isinstance(directions, list):\n            raise ValueError('Retain the original complete direction list')\n        for ordinal, direction in enumerate(directions):\n            if not isinstance(direction, dict) or direction.get('phase') != phase:\n                raise ValueError('Each returned cache scope belongs to its actual scientific direction')\n            rows = direction.get('complete_selected_inequalities')\n            start = direction.get('starting_geometry')\n            if not isinstance(rows, dict) or not isinstance(start, dict):\n                raise ValueError('Every recorded direction retains its original rows and starting geometry')\n            point = rows.get('current_full_point_sha256')\n            prefix = rows.get('original_selection_metadata')\n            if (not _sha_word(point) or start.get('current_full_point_sha256') != point\n                    or start.get('actual_model_identity_sha256') != identity\n                    or not isinstance(prefix, dict)\n                    or rows.get('original_selector_source_sha256') != CURVATURE_SELECTOR_SHA256):\n                raise ValueError('A returned numerical cache may not use the report latest point in place of its own point')\n            count = rows.get('original_prefix_rows')\n            if (type(count) is not int or not 0 <= count <= 192\n                    or prefix.get('selected_rows') != count\n                    or not isinstance(prefix.get('rows'), list) or len(prefix['rows']) != count\n                    or not isinstance(rows.get('rows'), list) or len(rows['rows']) < count):\n                raise ValueError('The cache must retain every original selected prefix row in its actual order')\n            source = rows.get('source_binding')\n            if (not isinstance(source, dict)\n                    or source.get('source_sha256') != GEOMETRY_SHA256\n                    or source.get('actual_model_identity_sha256') != identity\n                    or source.get('current_selector_source_sha256') != CURVATURE_SELECTOR_SHA256\n                    or source.get('complete_curvature_pullback_cache_policy') != policy):\n                raise ValueError('The full row builder must bind this actual complete selector policy')\n            checked = pure['validate_complete_curvature_pullback_cache'](\n                prefix.get('complete_curvature_pullback_cache'), selected_rows=count,\n                current_full_point_sha256=point, model_identity_sha256=identity)\n            scopes.append(dict(direction_list=field, ordinal=ordinal,\n                direction_index=direction.get('index'), direction_serial=direction.get('serial'),\n                current_full_point_sha256=point, original_prefix_rows=count,\n                complete_original_prefix_row_metadata_sha256=canonical(prefix['rows']),\n                actual_complete_cache_record=checked))\n    return dict(schema='actual-complete-halfwave-curvature-pullback-cache-binding-v1',\n        selector_source=dict(path=str(path), bytes=CURVATURE_SELECTOR_BYTES,\n            sha256=CURVATURE_SELECTOR_SHA256),\n        actual_model_identity_sha256=identity, policy=policy,\n        policy_identity_sha256=canonical(policy), scopes=scopes,\n        complete_actual_direction_scopes=len(scopes),\n        every_recorded_direction_own_point_used=True,\n        logical_requests_not_counted_as_actual_point_vjp_executions=True,\n        original_complete_direction_and_row_validators_still_required=True,\n        missing_future_direction_or_final_values_created=False,\n        field_root_derivative_or_quadrature_evaluations=0,\n        scientific_module_imported=False,\n        independent_scientific_admission_gate_created=False)\n\n\ndef bind_report(report, *, source_by_role, geometry_source):"
      },
      {
        "old": "    policy_identity = canonical(policy)\n    binding = dict(",
        "new": "    policy_identity = canonical(policy)\n    curvature_cache = _complete_curvature_cache_scopes(report, roles, path, identity)\n    binding = dict("
      },
      {
        "old": "        angle_block=angle_block, policy=policy, policy_identity_sha256=policy_identity,",
        "new": "        angle_block=angle_block, policy=policy, policy_identity_sha256=policy_identity,\n        complete_curvature_pullback_cache=curvature_cache,"
      },
      {
        "old": "                    or source.get('missing_angle_root_batch_policy') != policy\n",
        "new": "                    or source.get('missing_angle_root_batch_policy') != policy\n                    or source.get('current_selector_source_sha256') != CURVATURE_SELECTOR_SHA256\n                    or source.get('complete_curvature_pullback_cache_policy') != curvature_cache['policy']\n"
      }
    ]
  },
  {
    "role": "driver",
    "parent": {
      "role": "driver",
      "name": "fullclosed_fixed_fejer_halfwave_so3_qp.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_halfwave_so3_qp.py",
      "bytes": 99375,
      "sha256": "095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec",
      "git_blob_sha": "ef97023191b76706692db7aaff20216cbf79efd7"
    },
    "output": {
      "role": "driver",
      "name": "fullclosed_fixed_fejer_halfwave_dk_cache_qp.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_halfwave_dk_cache_qp.py",
      "bytes": 99410,
      "sha256": "7883d9fac2422509e5577fada1ed58f7a0d83f76031d00f3abf9aa41d5159910",
      "git_blob_sha": "c0e24fb110b3f893bbd1fa1d52eb2457d78c6872"
    },
    "patches": [
      {
        "old": "SCHEMA = \"complete-fixed-fejer-paired-halfwave-material-envelope-SO3-QP-v1\"",
        "new": "SCHEMA = \"complete-fixed-fejer-paired-halfwave-dk-cache-SO3-QP-v1\""
      },
      {
        "old": "\"geometry_selector\":(\"scripts/resume_20261120/fullclosed_point_inequalities_v2.py\",\"e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8\")",
        "new": "\"geometry_selector\":(\"scripts/resume_20261120/fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py\",\"f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112\")"
      },
      {
        "old": "\"geometry\":(\"scripts/resume_20261126/so3_fixed_fejer_halfwave_geometry.py\",\"494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b\")",
        "new": "\"geometry\":(\"scripts/resume_20261126/so3_fixed_fejer_halfwave_dk_cache_geometry.py\",\"da9b1be0146e48aad117124b7fc84c1754ecb0a78d5adeaa683710c5f7a8b316\")"
      },
      {
        "old": "\"batched_geometry_binding\":(\"scripts/resume_20261126/fixed_fejer_halfwave_geometry_binding.py\",\"45aedd26f59920938f6a6245dca48a06293f6cf1593124762a77063e4d0e5102\")",
        "new": "\"batched_geometry_binding\":(\"scripts/resume_20261126/fixed_fejer_halfwave_dk_cache_binding.py\",\"ca2a7884039df93f7b5b243d476c60d2e8e810bf1071545a84bbc283a460aaad\")"
      },
      {
        "old": "\"scalar_progress\":(\"scripts/resume_20261126/fixed_fejer_complete_geometry_trial_progress.py\",\"321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5\")",
        "new": "\"scalar_progress\":(\"scripts/resume_20261126/fixed_fejer_complete_geometry_location_progress.py\",\"4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94\")"
      }
    ]
  },
  {
    "role": "launcher",
    "parent": {
      "role": "launcher",
      "name": "launch_fixed_fejer_halfwave_actions.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_halfwave_actions.py",
      "bytes": 22120,
      "sha256": "6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c",
      "git_blob_sha": "7711e406787df02c8e0ab45965050c010c3b6f3b"
    },
    "output": {
      "role": "launcher",
      "name": "launch_fixed_fejer_halfwave_dk_cache_actions.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_halfwave_dk_cache_actions.py",
      "bytes": 22125,
      "sha256": "804bb61c3d26f4116dc486feb735afd73eb733a85399a7908525e40187ca2ffe",
      "git_blob_sha": "38498ca8650584030c38386d4efab9d17cdb404d"
    },
    "patches": [
      {
        "old": "095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec",
        "new": "7883d9fac2422509e5577fada1ed58f7a0d83f76031d00f3abf9aa41d5159910"
      },
      {
        "old": "fullclosed_fixed_fejer_halfwave_so3_qp.py",
        "new": "fullclosed_fixed_fejer_halfwave_dk_cache_qp.py"
      }
    ]
  },
  {
    "role": "reader",
    "parent": {
      "role": "reader",
      "name": "read_fixed_fejer_halfwave_so3_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_halfwave_so3_report.py",
      "bytes": 99816,
      "sha256": "be9bb58fa612fc25ab01458a2d6e21e0fa10c7573dad37e65effb845c6e29e92",
      "git_blob_sha": "04cf36b7372841fc714ebe827b7530ec9fed9945"
    },
    "output": {
      "role": "reader",
      "name": "read_fixed_fejer_halfwave_dk_cache_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_halfwave_dk_cache_report.py",
      "bytes": 99812,
      "sha256": "82a5c50f3006090398a054a1db12a607169bb1b074c25a00fae15ce447b704da",
      "git_blob_sha": "141407cc50df2d2043313fb168f779b0c018fc31"
    },
    "patches": [
      {
        "old": "095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec",
        "new": "7883d9fac2422509e5577fada1ed58f7a0d83f76031d00f3abf9aa41d5159910"
      },
      {
        "old": "fullclosed_fixed_fejer_halfwave_so3_qp.py",
        "new": "fullclosed_fixed_fejer_halfwave_dk_cache_qp.py"
      },
      {
        "old": "REPORT_SCHEMA = \"complete-fixed-fejer-paired-halfwave-material-envelope-SO3-QP-v1\"",
        "new": "REPORT_SCHEMA = \"complete-fixed-fejer-paired-halfwave-dk-cache-SO3-QP-v1\""
      },
      {
        "old": "schema='actual-fixed-fejer-halfwave-observed-envelope-SO3-readout-v1'",
        "new": "schema='actual-fixed-fejer-halfwave-dk-cache-observed-SO3-readout-v1'"
      }
    ]
  }
];
const SUPPORT = {
  "selector": {
    "name": "fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py",
    "bytes": 35982,
    "sha256": "f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112",
    "git_blob_sha": "a8c04e0044ae95d1debd4d96dcd753430f0fd797"
  },
  "observer": {
    "role": "scalar_progress",
    "name": "fixed_fejer_complete_geometry_location_progress.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_location_progress.py",
    "bytes": 42637,
    "sha256": "4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94",
    "git_blob_sha": "bad0be021443e7fa7a8fbfe4ee473f3e05ccadad"
  },
  "parent_binding": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json",
    "bytes": 67013,
    "sha256": "6dd246a030ffaf9e58e750c135e26424b12668b182f0e6a59726c2af006c1638",
    "git_blob_sha": "4f20af6e3663bdf69aca7193bc29624dc706411c",
    "fixed_publication_commit": "7d34ebe278826c68a9e84c32179251220bf2fc3b"
  },
  "current_binding": {
    "role": "complete_runtime_binding",
    "name": "fixed-fejer-paired-halfwave-curvature-cache-current-runtime-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-curvature-cache-current-runtime-binding.json",
    "bytes": 51709,
    "sha256": "d449d0a54b69b23c598234a28fede12917473ce7058e9d8815ba8b524c6f869f",
    "git_blob_sha": "38f781117d79710e72947cb8f8f0ecb258f0dabb"
  }
};

function sha(raw) { return crypto.createHash('sha256').update(raw).digest('hex'); }
function require(condition, message) { if (!condition) throw Error(message); }
function argumentsOf(argv) {
  const known = new Set(['--source-root','--output-directory']);
  const values = {};
  for (let i=0;i<argv.length;i+=2) {
    require(known.has(argv[i]) && i+1<argv.length && !(argv[i] in values),
      'Use exactly --source-root and --output-directory');
    values[argv[i]] = path.resolve(argv[i+1]);
  }
  require(Object.keys(values).length===2,'Both complete source and generated directories are required');
  return values;
}
async function readComplete(root, record) {
  const filename = path.join(root,record.path);
  const stat = await fs.stat(filename);
  require(stat.isFile() && stat.size===record.bytes && stat.size<100000,
    'Whole source size differs: '+record.path);
  const raw = await fs.readFile(filename);
  require(raw.length===record.bytes && sha(raw)===record.sha256,
    'Whole source hash differs: '+record.path);
  const text = raw.toString('utf8');
  require(Buffer.from(text,'utf8').equals(raw),'Keep exact UTF-8 source bytes');
  return {filename,raw,text};
}
function replaceExactlyOnce(text, before, after) {
  require(typeof before==='string' && before.length>0 && typeof after==='string',
    'Each source change is a complete nonempty literal replacement');
  const pieces=text.split(before);
  require(pieces.length===2,'Original whole source literal occurrence count differs');
  return pieces[0]+after+pieces[1];
}
function build(parent, item) {
  let result=parent;
  for(const patch of item.patches) result=replaceExactlyOnce(result,patch.old,patch.new);
  const raw=Buffer.from(result,'utf8');
  require(raw.length===item.output.bytes && raw.length<100000 && sha(raw)===item.output.sha256,
    'Complete derived source identity differs: '+item.role);
  let inverse=result;
  for(const patch of [...item.patches].reverse()) inverse=replaceExactlyOnce(inverse,patch.new,patch.old);
  require(inverse===parent && sha(Buffer.from(inverse,'utf8'))===item.parent.sha256,
    'All changes must reverse to the entire original source');
  return raw;
}
const args=argumentsOf(process.argv.slice(2));
const sourceRoot=args['--source-root'], outputRoot=args['--output-directory'];
require(sourceRoot!==outputRoot,'Generate a separate complete source tree');
const dependencies={};
for(const [role,record] of Object.entries(SUPPORT))
  dependencies[role]=await readComplete(sourceRoot,record);
const oldBinding=JSON.parse(dependencies.parent_binding.text);
const newBinding=JSON.parse(dependencies.current_binding.text);
const oldRoles=oldBinding.complete_source_role_registry;
const newRoles=newBinding.complete_source_role_registry;
require(Object.keys(oldRoles).length===137 && Object.keys(newRoles).length===137,
  'Keep all complete 137 scientific role pairs');
const changed=Object.keys(oldRoles).filter(role=>JSON.stringify(oldRoles[role])!==JSON.stringify(newRoles[role]));
require(JSON.stringify(changed.slice().sort())===JSON.stringify(
  ['geometry_selector','geometry','batched_geometry_binding','scalar_progress'].sort()),
  'Only the four declared actual current source-role pairs may change');
require(newRoles.geometry_selector[1]===SUPPORT.selector.sha256
  && newRoles.scalar_progress[1]===SUPPORT.observer.sha256,
  'Keep the entire actual halfwave selector and zero-new-field observer');
const generated=[];
for(const item of SPEC) {
  const parent=await readComplete(sourceRoot,item.parent);
  const output=build(parent.text,item);
  const filename=path.join(outputRoot,item.output.path);
  await fs.mkdir(path.dirname(filename),{recursive:true});
  await fs.writeFile(filename,output);
  generated.push({role:item.role,...item.output,exact_parent_inverse:true});
}
// Reused complete selector/observer and exact registry are copied byte-for-byte.
// Their independent complete source constructors remain named in the delivery.
for(const role of ['selector','observer','current_binding']) {
  const record=SUPPORT[role], value=dependencies[role];
  const filename=path.join(outputRoot,record.path);
  await fs.mkdir(path.dirname(filename),{recursive:true});
  await fs.writeFile(filename,value.raw);
  generated.push({role, ...record, unchanged_complete_input_copy:true});
}
process.stdout.write(JSON.stringify({
  schema:'complete-paired-halfwave-curvature-cache-source-text-reproduction-v1',
  generated, scientific_source_role_count:137, unchanged_role_count:133,
  changed_roles:changed, scientific_modules_imported:false,
  AST_fixture_benchmark_or_scientific_evaluation:false,
  new_public_scientific_admission_step:false
},null,2)+'\n');
