#!/usr/bin/env python3
"""Pure AST and isolated refresh-block protocol checks; zero Newton/BVP calls.

The only executed excerpt of either Newton definition is its refresh block,
inside a synthetic harness with string inputs and fake jac/splu/solve objects.
No SciPy routine, original install(), selector mutation, real LU, geometry,
tail, mesh or solve_newton function is called.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path
import sys
from types import ModuleType, SimpleNamespace
import weakref

HERE = Path(__file__).resolve().parent
ORIGINAL = HERE.parent / 'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py'
DERIVED = HERE / 'db6f-prefix-domain-newton-release-lu.py'
SELECTOR = HERE / 'db6f-prefix-select-domain-newton-release-lu.py'


def identity(path):
    p = Path(path).resolve(); data = p.read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def node(path, name):
    text = Path(path).read_text()
    matches = [n for n in ast.parse(text).body if isinstance(n, ast.FunctionDef) and n.name == name]
    require(len(matches) == 1, 'Ambiguous definition')
    return text, matches[0]


def refresh_node(function):
    loop = next(n for n in function.body if isinstance(n, ast.For))
    return next(n for n in loop.body if isinstance(n, ast.If)
                and isinstance(n.test, ast.Name) and n.test.id == 'refresh')


class Step:
    def __init__(self, tag, square):
        self.tag, self.square = tag, square

    def __matmul__(self, other):
        require(other is self, 'Changed merit expression')
        return self.square


def make_harness(refresh):
    template = ast.parse('''
def isolated_refresh(refresh, factors, have_old, make_old, jac, splu, Step):
    y,p,ym,ff,fm,br,residual='Y','P','YM','FF','FM','BR','R'
    step=Step('previous',9.)
    cost=9.
    if have_old:
        factor=make_old()
    for protocol_once in (0,):
        pass
    return {'kind':'normal-exit','factors':factors,'step':step.tag,'cost':cost,
            'factor':factor.tag if 'factor' in locals() else None}
''')
    function = template.body[0]
    loop = next(n for n in function.body if isinstance(n, ast.For))
    loop.body = [copy.deepcopy(refresh)]
    ast.fix_missing_locations(template)
    namespace = {}
    exec(compile(template, '<isolated-lifetime-refresh-protocol>', 'exec'), namespace)
    return namespace['isolated_refresh']


def exercise(function, spec):
    events = []; old_ref = [None]
    def old_alive():
        return old_ref[0] is not None and old_ref[0]() is not None
    def event(name, **rest):
        events.append({'event':name,'old_reference_alive':old_alive(),**rest})
    class FakeFactor:
        def __init__(self, tag):
            self.tag = tag
        def solve(self, residual):
            event('factor.solve', factor=self.tag, residual=residual)
            if spec.get('failure') == 'solve-runtime':
                raise RuntimeError('synthetic solve failure')
            if spec.get('failure') == 'solve-floating':
                raise FloatingPointError('synthetic solve failure')
            return Step('replacement-step', 4.)
    def make_old():
        value = FakeFactor('old')
        old_ref[0] = weakref.ref(value)
        return value
    def jac(*args):
        require(args == ('Y','P','YM','FF','FM','BR'), 'Changed Jacobian input order')
        event('jac')
        if spec.get('failure') == 'jac-runtime':
            raise RuntimeError('synthetic jac failure')
        if spec.get('failure') == 'jac-memory':
            raise MemoryError('synthetic jac failure')
        return 'synthetic-J'
    def splu(value):
        require(value == 'synthetic-J', 'Changed LU input')
        event('splu')
        if spec.get('failure') == 'splu-runtime':
            raise RuntimeError('synthetic LU failure')
        if spec.get('failure') == 'splu-memory':
            raise MemoryError('synthetic LU failure')
        return FakeFactor('new')
    try:
        result = function(spec['refresh'],spec['factors'],spec['have_old'],make_old,jac,splu,Step)
        result = {'return':result}
    except Exception as error:
        result = {'exception_type':type(error).__name__,'exception_message':str(error)}
    return {'outcome':result,'events':events}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    require(not args.out.exists(), 'Refusing an existing output')
    selector=ModuleType('pure_lu_selector_definitions')
    selector.__file__=str(SELECTOR)
    exec(compile(SELECTOR.read_bytes(),str(SELECTOR),'exec'),selector.__dict__)
    sources=selector.definitions(ORIGINAL)
    old_text,old=node(ORIGINAL,'solve_newton')
    new_text,new=node(DERIVED,'solve_newton')
    old_source=ast.get_source_segment(old_text,old)
    new_source=ast.get_source_segment(new_text,new)
    addition='            factor=None\n'
    require(new_source.count(addition)==1 and new_source.replace(addition,'',1)==old_source,
            'The function is not a byte-exact one-statement derivative')
    old_refresh,new_refresh=refresh_node(old),refresh_node(new)
    require(len(new_refresh.body)==len(old_refresh.body)+1,
            'Unexpected refresh block extent')
    require(isinstance(new_refresh.body[0],ast.If)
            and isinstance(new_refresh.body[0].body[0],ast.Break),
            'Release moved before the factorization budget guard')
    assignment=new_refresh.body[1]
    require(ast.dump(assignment,include_attributes=False)==
            ast.dump(ast.parse('factor=None').body[0],include_attributes=False),
            'Wrong release statement')
    old_harness,new_harness=map(make_harness,(old_refresh,new_refresh))
    cases=[
        {'name':'first-refresh','refresh':True,'factors':0,'have_old':False},
        {'name':'replacement-refresh','refresh':True,'factors':1,'have_old':True},
        {'name':'reuse-full-step','refresh':False,'factors':1,'have_old':True},
        {'name':'budget-exhausted','refresh':True,'factors':8,'have_old':True},
    ]
    for failure in ('jac-runtime','splu-runtime','jac-memory','splu-memory','solve-runtime','solve-floating'):
        cases.append({'name':failure,'refresh':True,'factors':1,'have_old':True,'failure':failure})
    results=[]
    for spec in cases:
        before,after=exercise(old_harness,spec),exercise(new_harness,spec)
        require(before['outcome']==after['outcome'], 'Changed control outcome: '+spec['name'])
        def mathematical_trace(value):
            return [{k:v for k,v in row.items() if k!='old_reference_alive'} for row in value['events']]
        require(mathematical_trace(before)==mathematical_trace(after),
                'Changed callback order or inputs: '+spec['name'])
        if spec['refresh'] and spec['factors']<8:
            require(after['events'] and after['events'][0]['event']=='jac'
                    and all(not e['old_reference_alive'] for e in after['events']),
                    'Old strong reference survived the intended release')
            if spec['have_old']:
                require(before['events'][0]['old_reference_alive'],
                        'Original assignment did not retain the old reference during its RHS')
        else:
            require(before['events']==after['events']==[], 'Unexpected factorization outside refresh')
            require(after['outcome']['return']['factor']=='old', 'Required retained factor was lost')
        if spec.get('failure') in ('jac-runtime','splu-runtime'):
            require(after['outcome']=={'return':('Y','P',True)}, 'Original RuntimeError return changed')
        results.append({'case':spec,'original':before,'derived':after,'passed':True})
    # Execute only the alias statement itself with dummy metadata containers.
    original=SimpleNamespace(STATS={'calls':7}); imported_dictionary=original.STATS
    derived=SimpleNamespace(STATS={'calls':0})
    select_source=node(SELECTOR,'select_newton')[1]
    aliases=[n for n in select_source.body if isinstance(n,ast.Assign)
             and ast.dump(n,include_attributes=False)==ast.dump(
                 ast.parse('derived.STATS = original.STATS').body[0],include_attributes=False)]
    require(len(aliases)==1, 'No unique original-STATS alias')
    exec(compile(ast.fix_missing_locations(ast.Module(body=[copy.deepcopy(aliases[0])],type_ignores=[])),
                 '<isolated-STATS-alias>', 'exec'),{'original':original,'derived':derived})
    derived.STATS['calls']+=1
    require(imported_dictionary is derived.STATS and imported_dictionary['calls']==8,
            'Imported original counters would become stale')
    negative=[]
    try:
        selector.definitions(DERIVED)
    except ValueError as error:
        negative.append({'case':'derived-cannot-impersonate-original-source','error':str(error)})
    require(len(negative)==1, 'Wrong-source negative gate did not reject')
    report={'status':'PURE_LIFETIME_PROTOCOL_PASS','scope':__doc__,
            'sources':[identity(p) for p in (ORIGINAL,DERIVED,SELECTOR,Path(__file__))],
            'byte_exact_function_after_removing_one_assignment':True,
            'single_statement_AST_check':sources,
            'cases':results,'negative_gates':negative,'STATS_alias_preserved':True,
            'actual_newton_calls':0,'actual_scipy_LU_calls':0,'actual_BVP_calls':0,
            'actual_DN_or_RK_calls':0,'runtime_selector_install_calls':0,
            'limitation':'Weak-reference checks establish Python-reference lifetime in the isolated protocol, not SuperLU bytes, allocator release, RSS reduction or successful candidate computation.'}
    payload=(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode()
    require(len(payload)<100000,'Pure metadata output too large')
    with args.out.open('xb') as f:f.write(payload)
    print(json.dumps({'status':report['status'],'cases':len(results),'output':identity(args.out),
                      'actual_solver_calls':0,'actual_install_calls':0},sort_keys=True))
    return 0


if __name__=='__main__':
    sys.exit(main())
