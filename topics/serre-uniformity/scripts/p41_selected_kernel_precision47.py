#!/usr/bin/env python3
"""Lift only the constant kernels needed at actual near-CM4 norm points.

The already certified four-digit kernel is used as a finite etale coordinate
algebra.  One division-polynomial Newton step lifts its torsion generator to
up to eight digits, and its characteristic polynomial gives the lifted kernel.
No individual torsion splitting field or B multiplication chain is rebuilt.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
import types


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    if str(path).endswith('.gz'):
        raw = gzip.compress(raw, mtime=0)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+'.tmp')
    tmp.write_bytes(raw)
    tmp.replace(path)


def precision_engine(script_dir, precision):
    """Reuse the exact R209 algebra with a documented precision substitution."""
    assert 4 <= precision <= 8
    path = Path(script_dir)/'p41_coprime_kernel_dag47.py'
    source = path.read_text()
    assert source.count('\nQ = 47**4\n') == 1
    assert source.count('for _ in range(2):') == 2
    source = source.replace('\nQ = 47**4\n', '\nQ = 47**'+str(precision)+'\n')
    source = source.replace('for _ in range(2):',
                            'for _ in range('+str((precision-1).bit_length())+'):')
    module = types.ModuleType('p41_precision_engine_'+str(precision))
    module.__file__ = str(path)
    exec(compile(source, str(path)+'[precision='+str(precision)+']', 'exec'), module.__dict__)
    return module, hashlib.sha256(source.encode()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--constant-dag', type=Path, required=True)
    ap.add_argument('--selection', type=Path, required=True)
    ap.add_argument('--precision', type=int, default=6)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    import p41_coprime_kernel_dag47 as E4
    from p41_etale_torsion_lift47 import QuadraticRing
    E, runtime_sha = precision_engine(args.script_dir.resolve(), args.precision)
    R, Q = E.R, E.Q
    data, selection = read(args.constant_dag), read(args.selection)
    assert data['curve'] == 'CM4' and data['modulus'] == 47**4
    selected = selection['near_CM4_node_inventory']
    if isinstance(selected, dict):
        wanted = sorted(selected)
    else:
        wanted = sorted(v.get('node', v.get('node_key')) for v in selected)
    assert len(wanted) == len(set(wanted)) == 200
    A0, B0 = R.integer(-1), R.zero
    _, _, primes4, inputs = E4.load_primes(args.script_dir, 'CM4')
    lifted_primes, nodes = {}, {'1': dict(data['nodes']['1'], A=A0, B=B0)}
    bindings = {'constant_dag_sha256':sha(args.constant_dag),
                'selection_sha256':sha(args.selection), 'source_sha256':sha(__file__),
                'kernel_engine_sha256':sha(args.script_dir/'p41_coprime_kernel_dag47.py'),
                'precision_specialized_engine_sha256':runtime_sha}
    if args.output.exists():
        old = read(args.output)
        assert old['bindings'] == bindings and old['precision'] == args.precision
        lifted_primes = old['lifted_source_kernels']
        nodes = old['nodes']

    def output(complete=False, logarithms=None):
        return {'scope':'Selected actual near-CM4 constant targets at sufficient logarithmic precision',
                'curve':'CM4','precision':args.precision,'modulus':Q,'bindings':bindings,
                'input_sha256':inputs,'requested_nodes':wanted,
                'lifted_source_kernels':lifted_primes,'nodes':nodes,
                'complete':complete,'near_CM4_logarithms':logarithms or {}}

    def lift_kernel(h4, ell, A, B):
        S = E.EtaleKernel(h4)
        D = E.Dual(S)
        x = S.generator
        val, der = E.division_polynomial(ell,(x,S.one),
                         (S.constant(A),S.zero),(S.constant(B),S.zero),D)
        assert all(v % (47**4) == 0 for c in val for v in c)
        x = S.sub(x, S.mul(val, S.inverse(der)))
        assert E.division_polynomial(ell,x,S.constant(A),S.constant(B),S) == S.zero
        h = S.charpoly(x)
        assert [[v % (47**4) for v in c] for c in h] == [list(c) for c in h4]
        return h

    def source_kernel(ell, line):
        key = str(ell)+':'+str(line)
        if key not in lifted_primes:
            h4 = primes4[ell][line]['kernel_polynomial_ascending']
            lifted_primes[key] = lift_kernel(h4,ell,A0,B0)
            # Save each expensive lifted prime immediately, even before its target.
            save(args.output,output())
            print('source kernel precision',key,'digits',args.precision,flush=True)
        return [tuple(c) for c in lifted_primes[key]]

    def get(key):
        if key in nodes:
            return nodes[key]
        old = data['nodes'][key]
        parent = get(old['parent'])
        if old.get('nondual_cyclic_order_four'):
            h = lift_kernel(old['kernel'],2,tuple(parent['A']),tuple(parent['B']))
        else:
            h = source_kernel(old['ell'],old['line'])
            for edgekey in parent['path']:
                h = E.transport_kernel(h,get(edgekey))
        assert [[v % (47**4) for v in c] for c in h] == old['kernel']
        A,B = E.velu_model(old['ell'],h,tuple(parent['A']),tuple(parent['B']))
        assert tuple(v % (47**4) for v in A) == tuple(old['A'])
        assert tuple(v % (47**4) for v in B) == tuple(old['B'])
        nodes[key] = dict(old,kernel=h,A=A,B=B,source_A=parent['A'],source_B=parent['B'])
        return nodes[key]

    start = time.monotonic()
    for n,key in enumerate(wanted,1):
        get(key)
        if n % 10 == 0:
            save(args.output,output())
            print('selected target',n,'/200','total nodes',len(nodes),flush=True)
    R4 = QuadraticRing(47**4)
    def logarithm(unit):
        z = R4.sub(R4.power(unit,47**2-1),R4.one)
        assert all(v % 47 == 0 for v in z)
        ans = R4.add(R4.sub(z,R4.scale(R4.power(z,2),pow(2,-1,47**4))),
                     R4.scale(R4.power(z,3),pow(3,-1,47**4)))
        return R4.scale(ans,pow(47**2-1,-1,47**4))
    logarithms = {}
    for key in wanted:
        v = nodes[key]
        A,B = tuple(v['A']),tuple(v['B'])
        assert R.is_unit(A) and all(c % 47 == 0 for c in B)
        assert any(c % (47**2) for c in B)
        # v47(B)=1 and v47(u)=2: six input digits leave four unit digits.
        assert args.precision >= 6
        u = R.mul(R.power(B,2),R.inverse(R.power(A,3)))
        assert all(c % (47**2) == 0 for c in u)
        uu = tuple(c//(47**2) % (47**4) for c in u)
        denominator = R.add(R.integer(4),R.scale(u,27))
        jminus = R.mul(R.scale(u,-46656),R.inverse(denominator))
        assert all(c % (47**2) == 0 for c in jminus)
        jj = tuple(c//(47**2) % (47**4) for c in jminus)
        logu,logj = logarithm(uu),logarithm(jj)
        conversion = tuple(c % (47**4) for c in R.mul(R.integer(-46656),R.inverse(denominator)))
        assert logj == R4.add(logu,logarithm(conversion))
        logarithms[key] = {'valuation_B':1,'valuation_u':2,
                           'u_mod47_sixth':u,'u_unit_mod47_fourth':uu,'log_u_mod47_fourth':logu,
                           'j_minus1728_unit_mod47_fourth':jj,
                           'log_j_minus1728_mod47_fourth':logj,
                           'j_to_u_unit_conversion_checked':True}
    save(args.output,output(True,logarithms))
    print('COMPLETE selected200',sha(args.output),'seconds',round(time.monotonic()-start,3),flush=True)


if __name__ == '__main__':
    main()
