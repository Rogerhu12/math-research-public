"""Apply only a material identity to the frozen physical driver's fine cache.

For a subsequent actual continuation, call run() instead of mutating the
shared ancestor module. The source SHA pins every original scientific line.
The cache comparison, two records after actual fine scans, and an explicit
skip of an already completed source initializer are the only syntax changes.
No numerical operation or acceptance threshold is injected.
"""
import ast
import hashlib
from pathlib import Path
import re

SOURCE = 'r582_physical_epigraph_continuation_20261127.py'
SOURCE_SHA = 'c0c5c1c82808ea7b54ad68cc5bfee0a921726dc2bf8dfa2ac725600859133e02'
MATERIAL = 'fine_qualification_material_knots_and_jets_sha256'


def material_bound_main(source):
    if hashlib.sha256(source).hexdigest() != SOURCE_SHA:
        raise ValueError('the original physical driver changed')
    main, = (n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name=='main')
    assigns = [n for n in ast.walk(main) if isinstance(n,ast.Assign) and len(n.targets)==1
               and isinstance(n.targets[0],ast.Name)]
    gate, = (n for n in assigns if n.targets[0].id=='reused_initial')
    if not isinstance(gate.value,ast.BoolOp) or not isinstance(gate.value.op,ast.And):
        raise ValueError('the original complete baseline cache predicate differs')
    extra = ast.parse('retained['+repr(MATERIAL)+'] == field.material_mesh_sha256',mode='eval').body
    gate.value.values.append(ast.increment_lineno(extra,gate.lineno-1))
    warm, = (n for n in assigns if n.targets[0].id=='use_warm')
    if not isinstance(warm.value,ast.BoolOp) or not isinstance(warm.value.op,ast.And):
        raise ValueError('the original source warm initializer predicate differs')
    skip = ast.parse("not source.get('skip_completed_source_warm_trial', False)",mode='eval').body
    warm.value.values.append(ast.increment_lineno(skip,warm.lineno-1))
    writes = [n for n in assigns if n.targets[0].id=='retained' and isinstance(n.value,ast.Dict)]
    if len(writes)!=2:
        raise ValueError('expected the complete baseline and full-fine accepted state writers')
    for n in writes:
        n.value.keys.append(ast.copy_location(ast.Constant(MATERIAL),n.value))
        field = ast.parse('field.material_mesh_sha256',mode='eval').body
        n.value.values.append(ast.increment_lineno(field,n.lineno-1))
    return ast.fix_missing_locations(ast.Module(body=[main],type_ignores=[]))


def run(driver, loader, emitter, schema, *, qualified_source_material_sha256, pending=None):
    """The explicit source SHA belongs to the *qualifying scan*, even when
    a later interrupted run merely carried that historical record. Optional
    pending records p, q_identity, fine_radial_identity, fine_theta_nodes and
    material_sha256; only a real completed matching fine can close that debt.
    """
    path = Path(driver.__file__).resolve()
    if path.name!=SOURCE or re.fullmatch('[0-9a-f]{64}',qualified_source_material_sha256) is None:
        raise ValueError('the actual source and qualifying scan material identity are required')
    active, closed = None, False
    def bound_loader(raw,digest):
        source, paid, fine = loader(raw,digest)
        state = source['resume97_state']
        rec = state['actual_retained_state']
        if rec.get(MATERIAL,qualified_source_material_sha256)!=qualified_source_material_sha256:
            raise ValueError('the previously paid fine record carries a different material identity')
        # Preserve the complete historical record, including during a clock
        # in field construction or during mandatory new-material qualification.
        state['actual_retained_state'] = dict(rec,**{MATERIAL:qualified_source_material_sha256})
        return source,paid,fine
    def bound_emit(tag,value):
        nonlocal active, closed
        if tag=='FINITE_LOCAL_TAIL_FIELD':
            active = value['field']['material_mesh_binary64_sha256']
        if pending and tag=='FINITE_LOCAL_TAIL_PROGRESS':
            t = value['last_completed_full_scan_trial']
            s = t['scan']
            if (active==pending['material_sha256'] and t['q_identity']==pending['q_identity']
                    and t['p']==pending['p'] and s['complete_fine_scan'] is True
                    and s['radial_grid_identity']==pending['fine_radial_identity']
                    and s['theta_nodes']==pending['fine_theta_nodes']):
                closed = True
        if tag in ('FINITE_LOCAL_TAIL_DEFINITION','FINITE_LOCAL_TAIL_FIELD','FINITE_LOCAL_TAIL_FINAL'):
            value = dict(value,source_fine_qualifying_material_sha256=qualified_source_material_sha256,
                current_generated_material_sha256=active,complete_physical_fine_cache_checks_material=True)
            if pending:
                value.update(source_pending_trial=pending,source_pending_fine_closed_on_original_material_and_grid=closed)
        emitter(tag,value)
    namespace = dict(vars(driver),load_input=bound_loader,emit=bound_emit,SCHEMA=schema)
    exec(compile(material_bound_main(path.read_bytes()),str(path),'exec'),namespace)
    namespace['main']()
