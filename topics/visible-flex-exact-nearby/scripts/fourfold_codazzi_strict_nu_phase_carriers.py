"""PHI necessary immutable phase inputs, without any old scientific target.

The original full two-leg degree12 polynomial is rematerialized in the
original 256-bit order and compared to its complete original digest.
No old residual, norm, source integral or parameter target is called.
"""
from __future__ import annotations
import ast, copy, gzip, hashlib, json, math, subprocess
from fractions import Fraction
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
COMMIT = '46f127c7153f5393dcd2a00f42d4c1d3662c294d'
PRODUCER = '3254a9225f4933ae11ffbfa1862a50ed1c7c585f03aa11e56606ad758ccc6961'
COVER = TOPIC+'/notes/phase_transport_complete_ci/run-43580721166-1/complete-169-cover.json.gz'
COVER_SHA = 'd2e9f2479dc677694c8e84945ac1787f6a5366446d4fd30eac5b3c3008ecc1ae'
LABEL = TOPIC+'/notes/2026-11-14-R133-complete169-label-L2-sharp-twist-native.json.gz'
LABEL_SHA = '8ad3c9e30a15e307f036456baf3334e00592208228af6df39a9c1cc020b8eeef'
OLD_INVENTORY = TOPIC+'/notes/2026-11-14-R133-phase-transport-resume127-inputs.json'
KIND = 'PHI_original_phase_prefix_131_packed_inventory_v1'


def require(ok, message):
    if not ok: raise ValueError(message)


def sha(raw): return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def phase_path(index):
    prefix = (TOPIC+'/data/phase_transport_resume127_20261114/transport/' if index < 127 else
              TOPIC+'/notes/phase_transport_complete_ci/run-43580721166-1/')
    return prefix+'transport-germ%04d.json.gz'%index


def scalar_path(index):
    if index == 0:
        return TOPIC+'/notes/2026-11-14-R133-complete-Arb-high-scalar-Taylor-first-germ-native.json.gz'
    lo = 1+42*((index-1)//42);hi = lo+42
    return (TOPIC+'/notes/phase_scalar_high7_ci/run-43573003976-1-germs%04d-%04d/'%(lo,hi)
            +'germ%04d.json.gz'%index)


def plan(root,tree_metadata=None):
    """Only immutable metadata and complete existing JSON definitions."""
    def git(*args):
        return subprocess.run(['git',*args],cwd=root,check=True,capture_output=True).stdout
    raw = git('show',COMMIT+':'+COVER)
    require(sha(raw) == COVER_SHA,'the original complete169 metadata')
    cover = parse(raw);inventory = json.loads((Path(root)/OLD_INVENTORY).read_bytes())
    require(cover['complete'] is True and cover['complete_transport_germs'] == 169
        and cover['original_producer_sha256'] == PRODUCER and len(cover['germs']) == 169,
        'the whole original completed phase, not a sampled prefix')
    wanted = {COVER,LABEL,*[phase_path(i) for i in range(131)],*[scalar_path(i) for i in range(131)]}
    sizes = None
    if tree_metadata is not None:
        tree = json.loads(Path(tree_metadata).read_bytes())
        require(tree['sha'] == '8d2cb322294efd4fecf41ac91995d3a1fecf0a73'
            and tree['truncated'] is False,'the whole immutable public topic-tree metadata')
        sizes = {TOPIC+'/'+x['path']:(x['sha'],x['size']) for x in tree['tree']
                 if x['type'] == 'blob' and TOPIC+'/'+x['path'] in wanted}
        require(set(sizes) == wanted,'every required original blob is in the complete metadata')
    # Without -l this reads Git tree objects, never all historical file bodies.
    # Actual whole bytes/hashes are still verified by the public input owner.
    raw_tree = git('ls-tree','-r',*(['-l'] if sizes is None else []),COMMIT,'--',*sorted(wanted))
    entries = {}
    for line in raw_tree.decode().splitlines():
        fields,path = line.split('\t',1)
        if path in wanted:
            if sizes is None:
                mode,kind,blob,size = fields.split();require(size.isdigit(),'complete blob size');size = int(size)
            else:
                mode,kind,blob = fields.split();reported,size = sizes[path]
                require(reported == blob,'the original Git blob and public-tree metadata agree')
            require(kind == 'blob' and type(size) is int and size > 0,'complete immutable blob metadata')
            entries[path] = {'path':path,'bytes':size,'git_blob_sha':blob,'commit':COMMIT}
    require(set(entries) == wanted,'every necessary original scalar and transport carrier exists publicly')
    packed = [];edge = Fraction(0)
    for i,germ in enumerate(cover['germs'][:131]):
        left,right = map(Fraction,germ['exact_interval']);pp,sp = phase_path(i),scalar_path(i)
        require(germ['germ_index'] == i and left == edge < right
            and inventory['files'][sp] == germ['scalar_native_sha256']
            and (i >= 127 or inventory['files'][pp] == germ['sha256']),
            'entire chronological original native identities')
        p,s = entries[pp],entries[sp]
        packed.append([i,p['bytes'],p['git_blob_sha'],germ['sha256'],
                         s['bytes'],s['git_blob_sha'],germ['scalar_native_sha256']])
        edge = right
    require(edge == Fraction(9,50) and sum(x['actual_steps'] for x in cover['germs'][:131]) == 1572,
        'the exact necessary prefix through9/50 with every original accepted step')
    extra = [dict(entries[COVER],role='phase_cover',sha256=COVER_SHA),
             dict(entries[LABEL],role='phase_label_bound',sha256=LABEL_SHA)]
    return {'kind':KIND,'immutable_commit':COMMIT,'whole_original_germs':169,
        'necessary_prefix_germs':131,'necessary_prefix_steps':1572,'exact_interval':['0','9/50'],
        'packed_columns':['index','phase_bytes','phase_git_blob_sha','phase_sha256',
                          'scalar_bytes','scalar_git_blob_sha','scalar_sha256'],
        'packed_germs':packed,'extra':extra}


def expand(plan):
    require(plan['kind'] == KIND and plan['immutable_commit'] == COMMIT
        and plan['whole_original_germs'] == 169 and plan['necessary_prefix_germs'] == 131
        and plan['necessary_prefix_steps'] == 1572 and plan['exact_interval'] == ['0','9/50']
        and plan['packed_columns'] == ['index','phase_bytes','phase_git_blob_sha','phase_sha256',
            'scalar_bytes','scalar_git_blob_sha','scalar_sha256']
        and len(plan['packed_germs']) == 131,'the full necessary immutable phase plan')
    out = []
    for i,row in enumerate(plan['packed_germs']):
        require(len(row) == 7 and row[0] == i,'all compact descriptors in the original order')
        for role,path,values in [('phase_germ_%04d'%i,phase_path(i),row[1:4]),
                                  ('phase_scalar_%04d'%i,scalar_path(i),row[4:7])]:
            size,blob,digest = values
            require(type(size) is int and size > 0 and len(blob) == 40 and len(digest) == 64,
                'complete immutable native descriptor')
            out.append({'role':role,'path':path,'bytes':size,'git_blob_sha':blob,
                        'sha256':digest,'commit':COMMIT})
    require(len(plan['extra']) == 2 and plan['extra'][0]['path'] == COVER
        and plan['extra'][0]['sha256'] == COVER_SHA and plan['extra'][1]['path'] == LABEL
        and plan['extra'][1]['sha256'] == LABEL_SHA
        and all(x['commit'] == COMMIT for x in plan['extra']), 'the original whole completed error inputs')
    return out+plan['extra']


def admit(plan,raws):
    specs = expand(plan);by = {x['role']:x for x in specs}
    cover = parse(raws[COVER]);label = parse(raws[LABEL]);cfg = cover['configuration']
    require(cover['complete'] is True and cover['whole_negative_domain'] is True
        and cover['kind'] == 'actual_chronological_full_frequency_phase_transport_cover'
        and cover['source_sha256'] == 'af496eeec4141abf534af691f775fe5542b958390de540646b7b32750c2231d8'
        and cover['original_producer_sha256'] == PRODUCER and len(cover['gates']) == 7
        and all(x['passed'] is True for x in cover['gates'])
        and cfg['modes'] == 64 and cfg['time_degree'] == 12 and cfg['bits'] == 256
        and cfg['exact_eta_offset'] == '0' and cfg['whole_original_eta'] is False
        and cfg['derived_definition_sha256'] == '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47',
        'same whole completed true transport and original exact finite definition')
    require(label['kind'] == 'actual_complete169_true_label_L2_energy_and_sharpened_twist'
        and label['complete'] is True
        and label['source_sha256'] == 'e8749d002cf2e9cce45ff818876f4e6bab62409320a368017243d79675d04472'
        and label['root_contract_sha256'] == cfg['root_contract_sha256']
        and label['consumed_germs'] == 169 and len(label['gates']) == 7
        and all(x['passed'] is True for x in label['gates'])
        and label['endpoint_error_Wiener_strip'] == '3/100'
        and label['all_full_angular_modes_and_complete_even_mean_retained'] is True,
        'the whole original paid transport error, not its unrelated explicit-family twist')
    edge = Fraction(0);steps = 0;phase_docs = [];scalar_docs = []
    for i in range(131):
        p,s = parse(raws[phase_path(i)]),parse(raws[scalar_path(i)])
        g = cover['germs'][i];left,right = map(Fraction,g['exact_interval'])
        require(g['germ_index'] == i and left == edge < right
            and g['sha256'] == by['phase_germ_%04d'%i]['sha256']
            and g['scalar_native_sha256'] == by['phase_scalar_%04d'%i]['sha256']
            and p['configuration'] == cfg and p['complete_requested_prefix'] is True
            and p['last_complete_germ'] == i and Fraction(p['last_exact_radial_point']) == right
            and s['complete'] is True and s['germ_index'] == i and s['configuration'] == cfg['scalar_configuration']
            and s['kind'] == 'actual_complete_phase_scalar_high_Taylor_germ_v2'
            and s['exact_interval'] == g['exact_interval'] and len(s['gates']) == 6
            and all(x['passed'] is True for x in s['gates']), 'one whole original scalar/phase germ')
        here = left
        for row in p['rows']:
            a,b = map(Fraction,row['interval'])
            require(row['germ_index'] == i and row['scalar_native_sha256'] == g['scalar_native_sha256']
                and a == here < b <= right and row['exact_initial_value_shared_with_previous_endpoint'] is True
                and len(row['polynomial_sha256']) == 64,'every original full accepted phase polynomial')
            here = b
        require(here == right and len(p['rows']) == g['actual_steps']
            and len(p['exact_phase_state']) == 2 and all(len(side) == 129 for side in p['exact_phase_state']),
            'whole original two-leg terminal state and complete step cover')
        here = left
        for row in s['rows']:
            a,b = map(Fraction,row['interval'])
            require(a == here < b <= right and set(row['models']) == {'beta','K','s','gamma','q'}
                and all(len(x['exact_centered_polynomial']) == 8 for x in row['models'].values()),
                'all full degree7 scalar input polynomials and complete remainders')
            here = b
        require(here == right,'the entire original scalar interval')
        steps += len(p['rows']);edge = right;phase_docs.append(p);scalar_docs.append(s)
    require(edge == Fraction(9,50) and steps == 1572,'the complete needed input prefix')
    return {'phase':phase_docs,'scalar':scalar_docs,'cover':cover,'label':label,
        'receipt':{'necessary_original_phase_germs':131,'necessary_original_phase_steps':steps,
            'whole_original_phase_and_scalar_inventory_sha256':sha(canonical(specs)),
            'old_scientific_targets_evaluated':0,'original_degree64_time12_bits256_retained':True}}


def recurrence_namespace(raw,flint):
    require(sha(raw) == PRODUCER,'the entire unchanged original phase recipe')
    original = ast.parse(raw.decode());names = {'frac','mid','cplx','shift_scale','scalar_mul',
        'radial_mul','scalar_times','radial_add','angular_derivative','exact_real_midpoint','encode','initial_state','Fields'}
    selected = [copy.deepcopy(x) for x in original.body if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name in names]
    require({x.name for x in selected} == names,'every original pure carrier helper')
    fields = next(x for x in selected if x.name == 'Fields')
    at = next(x for x in fields.body if isinstance(x,ast.FunctionDef) and x.name == 'at')
    stop = [i for i,x in enumerate(at.body) if isinstance(x,ast.Assign)
            and any(isinstance(y,ast.Name) and y.id == 'eps' for y in x.targets)]
    require(len(stop) == 1,'the original field-carrier/error boundary')
    at.body = at.body[:stop[0]]+[ast.Return(value=ast.Name(id='field',ctx=ast.Load()))]
    tree = ast.Module(body=selected,type_ignores=[]);ast.fix_missing_locations(tree)
    arb = flint.arb
    def exact_arb(value):
        q = Fraction(value);return arb(q.numerator)/q.denominator
    ns = {'Fraction':Fraction,'math':math,'hashlib':hashlib,'json':json,'MF':64,
          'arb':arb,'acb':flint.acb,'acb_poly':flint.acb_poly,'ctx':flint.ctx,'exact_arb':exact_arb}
    exec(compile(tree,'<unchanged original pure phase carrier helpers>','exec'),ns)
    return ns


def one_step(ns,fields,state):
    """Exactly the original sequential recurrence, stopping before old fees."""
    acb_poly = ns['acb_poly'];endpoints = [];polynomials = [];digest = hashlib.sha256()
    for F,start in zip(fields,state):
        N = (len(start)-1)//2;exact = [list(start)]
        W = [acb_poly(list(map(ns['cplx'],start)))];dW = [ns['angular_derivative'](W[0],N)]
        for n in range(12):
            rhs = F[n].left_shift(N) if n < len(F) else acb_poly([])
            for i in range(min(n,len(F)-1)+1):rhs += F[i]*dW[n-i]
            candidate = acb_poly([-rhs[64+j]/(n+1) for j in range(2*N+1)])
            coeff = ns['exact_real_midpoint'](candidate,N);exact.append(coeff)
            W.append(acb_poly(list(map(ns['cplx'],coeff))))
            dW.append(ns['angular_derivative'](W[-1],N))
        endpoint = [(sum((z[j][0] for z in exact),Fraction(0)),sum((z[j][1] for z in exact),Fraction(0)))
                    for j in range(2*N+1)]
        endpoints.append(endpoint);polynomials.append(exact)
        for p in exact:
            digest.update((json.dumps([[str(a),str(b)] for a,b in p],separators=(',',':'))+'\n').encode())
    return endpoints,polynomials,digest.hexdigest()


def consume(admitted,ns,flint,base,alpha,nodes,offsets,root,cell_consumer,germ_consumer):
    """Stream exact necessary polynomials once; emit only new integral calls."""
    cfg = admitted['cover']['configuration']
    require(root['exact_H_sine_coefficients'] == cfg['exact_initial_H_sine_coefficients']
        and root['exact_H_cosine_coefficients'] == cfg['exact_initial_H_cosine_coefficients'],
        'same complete original initial phase, including every cosine coefficient')
    prior_precision = flint.ctx.prec
    fields = ns['Fields'](base,alpha,nodes,offsets,None)
    state = ns['initial_state'](root,64);edge = Fraction(0);step_count = 0
    chain = None
    try:
        for index,(phase,scalar) in enumerate(zip(admitted['phase'],admitted['scalar'])):
            si = 0
            for row in phase['rows']:
                left,right = map(Fraction,row['interval']);piece = row['actual_candidate_piece']
                require(left == edge < right and nodes[piece] <= left < right <= nodes[piece+1],
                        'the exact original phase step and candidate piece')
                while Fraction(scalar['rows'][si]['interval'][1]) <= left:si += 1
                model = scalar['rows'][si];sl,sr = map(Fraction,model['interval'])
                require(sl <= left < right <= sr,'the original whole scalar polynomial for this step')
                flint.ctx.prec = 256
                true_fields = fields.at(model,piece,left,right)
                endpoint,polynomials,digest = one_step(ns,true_fields,state)
                require(digest == row['polynomial_sha256'],
                        'the entire original two-leg polynomial; no replacement trial is allowed')
                state = endpoint;edge = right;step_count += 1
                chain = sha(canonical({'previous':chain,'germ':index,'step':step_count,
                    'interval':row['interval'],'whole_original_polynomial_sha256':digest}))
                flint.ctx.prec = prior_precision
                cell_consumer(left,right,polynomials[0])
            require(ns['encode'](state) == phase['exact_phase_state'],
                    'the entire original two-leg129 terminal state')
            germ_consumer(index,edge,step_count,chain)
        require(edge == Fraction(9,50) and step_count == 1572,'every necessary original phase step consumed')
    finally:
        flint.ctx.prec = prior_precision
    return {'whole_original_polynomial_sha256_checks':step_count,
        'whole_original_two_leg_endpoint_checks':131,'polynomial_receipt_chain_sha256':chain,
        'original_phase_interval':['0','9/50'],'old_residual_or_norm_targets_evaluated':0,
        'new_original_phase_or_PDE_trial_selected':False}
