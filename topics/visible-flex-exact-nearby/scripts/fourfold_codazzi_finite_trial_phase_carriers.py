"""P96: the entire original169 phase carrier, without old target calls.

The PHI recurrence and all original polynomial/endpoint checks are retained.
Only its necessary-prefix bounds and the consumer's scalar-model arguments
change. The last original phase endpoint is below the true root: the new
functional must pay that remaining sliver separately.
"""
from __future__ import annotations
import ast
import copy
import gzip
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
BASE = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_carriers.py'
BASE_SHA = 'b9fb05f92aa46b9d4064695a30f566fd9445323e301ba7d76d824ddcac3afee1'
COMMIT = '46f127c7153f5393dcd2a00f42d4c1d3662c294d'
TREE = '8d2cb322294efd4fecf41ac91995d3a1fecf0a73'
KIND = 'P96_complete_original169_phase_inventory_v1'
STOP = '1249886203106135147/5242880000000000000'
GERMS, STEPS = 169, 3095


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False, allow_nan=False)+'\n').encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def original(path):
    path = Path(path)
    raw = path.read_bytes()
    require(sha(raw) == BASE_SHA, 'the unchanged complete original PHI carrier helper')
    spec = importlib.util.spec_from_file_location('_P96_original_phase_recipe', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, raw


def plan(root, tree_metadata, complete_cover):
    """Read existing immutable metadata only; no recursive Git blob fetch."""
    old, unused = original(Path(root)/BASE)
    raw = Path(complete_cover).read_bytes()
    require(sha(raw) == old.COVER_SHA, 'the whole completed original169 cover')
    cover = parse(raw)
    tree = json.loads(Path(tree_metadata).read_bytes())
    require(tree['sha'] == TREE and tree['truncated'] is False,
            'the already saved whole immutable topic tree')
    require(cover['complete'] is True and cover['whole_negative_domain'] is True
            and cover['complete_transport_germs'] == GERMS
            and cover['actual_steps'] == STEPS
            and cover['exact_processed_interval'] == ['0', STOP],
            'all169 actual original germs and the explicit pre-root endpoint')
    wanted = {old.COVER, old.LABEL}
    wanted.update(old.phase_path(i) for i in range(GERMS))
    wanted.update(old.scalar_path(i) for i in range(GERMS))
    entries = {TOPIC+'/'+x['path']: x for x in tree['tree']
               if x['type'] == 'blob' and TOPIC+'/'+x['path'] in wanted}
    require(set(entries) == wanted, 'every whole original phase/scalar native is public')
    packed, edge = [], Fraction(0)
    for i, germ in enumerate(cover['germs']):
        left, right = map(Fraction, germ['exact_interval'])
        require(germ['germ_index'] == i and left == edge < right,
                'the complete chronological original169 cover')
        p, s = entries[old.phase_path(i)], entries[old.scalar_path(i)]
        packed.append([i, p['size'], p['sha'], germ['sha256'],
                       s['size'], s['sha'], germ['scalar_native_sha256']])
        edge = right
    require(edge == Fraction(STOP), 'the old phase carrier is not relabelled as reaching the root')
    extra = []
    for role, path, digest in [('phase_cover', old.COVER, old.COVER_SHA),
                               ('phase_label_bound', old.LABEL, old.LABEL_SHA)]:
        item = entries[path]
        extra.append({'role': role, 'path': path, 'bytes': item['size'],
                      'git_blob_sha': item['sha'], 'sha256': digest, 'commit': COMMIT})
    return {'kind': KIND, 'immutable_commit': COMMIT,
            'whole_original_germs': GERMS, 'necessary_prefix_germs': GERMS,
            'necessary_prefix_steps': STEPS, 'exact_interval': ['0', STOP],
            'packed_columns': ['index', 'phase_bytes', 'phase_git_blob_sha', 'phase_sha256',
                               'scalar_bytes', 'scalar_git_blob_sha', 'scalar_sha256'],
            'packed_germs': packed, 'extra': extra}


def expand(plan, old):
    require(plan['kind'] == KIND and plan['immutable_commit'] == COMMIT
            and plan['whole_original_germs'] == plan['necessary_prefix_germs'] == GERMS
            and plan['necessary_prefix_steps'] == STEPS
            and plan['exact_interval'] == ['0', STOP]
            and plan['packed_columns'] == ['index', 'phase_bytes', 'phase_git_blob_sha',
                'phase_sha256', 'scalar_bytes', 'scalar_git_blob_sha', 'scalar_sha256']
            and len(plan['packed_germs']) == GERMS,
            'the entire declared original169 input plan')
    out = []
    for i, row in enumerate(plan['packed_germs']):
        require(len(row) == 7 and row[0] == i, 'all original packed objects in order')
        for role, path, values in [
                ('phase_germ_%04d'%i, old.phase_path(i), row[1:4]),
                ('phase_scalar_%04d'%i, old.scalar_path(i), row[4:7])]:
            size, blob, digest = values
            require(type(size) is int and size > 0 and len(blob) == 40 and len(digest) == 64,
                    'one whole original native descriptor')
            out.append({'role': role, 'path': path, 'bytes': size, 'git_blob_sha': blob,
                        'sha256': digest, 'commit': COMMIT})
    require(len(plan['extra']) == 2
            and plan['extra'][0]['path'] == old.COVER
            and plan['extra'][0]['sha256'] == old.COVER_SHA
            and plan['extra'][1]['path'] == old.LABEL
            and plan['extra'][1]['sha256'] == old.LABEL_SHA
            and all(x['commit'] == COMMIT for x in plan['extra']),
            'both whole original error objects retained')
    return out+plan['extra']


def full_functions(old, raw):
    """Exact old functions with only declared prefix and callback changes."""
    require(sha(raw) == BASE_SHA, 'the complete unchanged old helper source')
    tree = ast.parse(raw.decode())
    selected = [copy.deepcopy(x) for x in tree.body
                if isinstance(x, ast.FunctionDef) and x.name in ('admit', 'consume')]
    require({x.name for x in selected} == {'admit', 'consume'}, 'both complete old functions')
    counts = {'131': 0, '1572': 0, 'stop_fraction': 0, 'stop_string': 0, 'callback': 0}

    class Extend(ast.NodeTransformer):
        def visit_Constant(self, node):
            if type(node.value) is int and node.value in (131, 1572):
                counts[str(node.value)] += 1
                return ast.copy_location(ast.Constant(GERMS if node.value == 131 else STEPS), node)
            if node.value == '9/50':
                counts['stop_string'] += 1
                return ast.copy_location(ast.Constant(STOP), node)
            return node

        def visit_Call(self, node):
            if (isinstance(node.func, ast.Name) and node.func.id == 'Fraction'
                    and ast.dump(node) == ast.dump(ast.parse('Fraction(9,50)', mode='eval').body)):
                counts['stop_fraction'] += 1
                return ast.copy_location(ast.Call(func=ast.Name(id='Fraction', ctx=ast.Load()),
                            args=[ast.Constant(STOP)], keywords=[]), node)
            if isinstance(node.func, ast.Name) and node.func.id == 'cell_consumer':
                require(len(node.args) == 3 and not node.keywords, 'the original complete-polynomial callback')
                counts['callback'] += 1
                node.args += [ast.Name(id='model', ctx=ast.Load()), ast.Name(id='piece', ctx=ast.Load())]
            return self.generic_visit(node)

    selected = [Extend().visit(x) for x in selected]
    require(counts == {'131': 3, '1572': 2, 'stop_fraction': 2, 'stop_string': 1, 'callback': 1},
            'only the exact necessary-prefix limits and scalar callback are extended')
    module = ast.Module(body=selected, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace = dict(vars(old))
    namespace['expand'] = lambda value: expand(value, old)
    exec(compile(module, '<same169-phase-admission-and-carrier-stream>', 'exec'), namespace)
    return namespace['admit'], namespace['consume'], {
        'complete_original_helper_sha256': BASE_SHA,
        'complete_extended_functions_AST_sha256': sha(ast.dump(module, include_attributes=False).encode()),
        'declared_prefix_changes': counts,
        'old_polynomial_recurrence_changed': False,
        'old_scientific_target_calls': 0,
        'true_root_sliver_still_separate': True,
    }
