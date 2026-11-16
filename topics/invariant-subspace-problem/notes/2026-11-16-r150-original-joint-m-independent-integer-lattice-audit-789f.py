#!/usr/bin/env python3
"""Independent integer-lattice audit of the original root-two M coordinates.
Author: ChatGPT (AI), Astra-ISP-789f, 2026-11-16.
Uses integer HNF indices, without the producer's modular Smith transformations.
All input and mathematical output files remain temporary.
"""
import argparse, hashlib, json, time
from pathlib import Path
from math import comb
from flint import fmpz_mat

P = 31
MOD = P**6

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode()

def checked(path, length, digest):
    raw = path.read_bytes()
    assert len(raw) == length and sha(raw) == digest
    return json.loads(raw)

def product(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def multiply(a, b):
    assert len(a[0]) == len(b)
    return [[sum(x*y for x, y in zip(row, col)) % MOD
             for col in zip(*b)] for row in a]

def polynomial(coefficients, x):
    n = len(x)
    out = [[0]*n for _ in range(n)]
    for c in reversed(coefficients):
        out = multiply(out, x)
        for i in range(n):
            out[i][i] = (out[i][i]+c) % MOD
    return out

def join(*matrices):
    return [sum((a[i] for a in matrices), []) for i in range(len(matrices[0]))]

def scaled(a, c):
    return [[c*x for x in row] for row in a]

def valuation(n):
    assert n > 0
    v = 0
    while n % P == 0:
        n //= P
        v += 1
    assert n == 1, 'lattice index must be a pure power of 31'
    return v

def image_length(a, exponents):
    n = len(exponents)
    generators = [list(col) for col in zip(*a)]
    generators += [[P**e if i == j else 0 for i in range(n)]
                   for j, e in enumerate(exponents)]
    h = fmpz_mat(generators).hnf()
    basis = [[int(h[i, j]) for j in range(n)] for i in range(h.nrows())
             if any(h[i, j] for j in range(n))]
    assert len(basis) == n
    index = abs(int(fmpz_mat(basis).det()))
    return sum(exponents)-valuation(index)

def group(a, exponents):
    lengths = [image_length(scaled(a, P**k), exponents)
               for k in range(max(exponents)+1)]
    assert lengths[-1] == 0
    at_least = [lengths[k-1]-lengths[k] for k in range(1, len(lengths))]
    assert all(x >= y >= 0 for x, y in zip(at_least, at_least[1:]))
    exact = [at_least[i]-(at_least[i+1] if i+1 < len(at_least) else 0)
             for i in range(len(at_least))]
    orders = [i+1 for i, count in enumerate(exact) for _ in range(count)]
    assert sum(orders) == lengths[0]
    return {'exponents': orders, 'length': lengths[0],
            'successivePImageLengths': lengths,
            'method': 'integer-HNF-lattice-index'}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=Path, required=True)
    parser.add_argument('--completion-dir', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    receipt = checked(args.input_dir/'original-joint-m-root-two-complete-p12-receipt.json',
                      37792, 'e6867a8f20e37f90aeaa08b8df44ead2fdac73475a6725a5114285609142afc2')
    z = checked(args.input_dir/'root-two-complete-six-digit-coordinates.json',
                9046, 'c31f78775508475bc62e8c772309b006356593a0547307f8cb9bc83fc66bc8ca')
    assert receipt['status'] == 'failed'
    assert z['binding'] == receipt['binding'] == '38139cd17a0a87190fc7302d7f9a271cd6370e379090de91ed9706eb3fa673e9'
    assert len(receipt['parameters']['stages']) == 42
    output_count = 0
    for name, stage in receipt['parameters']['stages'].items():
        assert stage['status'] == 'completed' and stage['exitCode'] == 0
        cache = json.loads((args.input_dir/'stage-cache'/(name+'.json')).read_bytes())
        assert cache['inputBinding'] == stage['inputBinding']
        for relative, expected in cache['outputs'].items():
            output = (args.input_dir/relative).resolve()
            assert output.is_relative_to(args.input_dir.resolve())
            raw = output.read_bytes()
            assert {'bytes': len(raw), 'sha256': sha(raw)} == expected
            output_count += 1
    completion = checked(args.completion_dir/'original-joint-m-root-two-p12-readonly-completion-receipt.json',
                         10067, '18085ddfc8be6d691c87588ed6ee03a5470f1996588cea0fc0d08f4ca97ce0bf')
    presentation = checked(args.completion_dir/'root-two-complete-presentation-and-action.json',
                           16797, '46cb736d61e85daf6af0a4476ffa857c98b06f84d8c6e149b6180ce054d14a5c')
    assert completion['status'] == 'completed'
    assert sha(canonical(completion['parameters']['inputIdentity'])) == completion['binding']
    assert presentation['binding'] == completion['binding']
    e, a = z['ambientExponents'], z['coordinateRows']
    assert e == [1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
    assert len(a) == 14 and all(len(row) == 26 for row in a)
    beta = z['betaModuloP6']
    free = z['freeCoefficientsModuloP6']
    c = [1]+free[:8]
    assert free[8:17] == [beta*v % MOD for v in c]
    assert free[17:26] == [beta*beta*v % MOD for v in c]
    assert all(a[i][j] == sum(P**k*z['torsionDigits'][k][i][j]
                              for k in range(6)) % P**e[i]
               for i in range(14) for j in range(26))
    assert free == [sum(P**k*z['freeDigits'][k][j] for k in range(6)) % MOD
                    for j in range(26)]
    x = [[0]*26 for _ in range(26)]
    u = [[int(i == 8)] for i in range(26)]
    for j in range(1, 9):
        x[8+j][j-1] += 1
        x[8][j-1] -= c[j]
    for j in range(9):
        x[17+j][8+j] += 1
        x[8][8+j] -= beta*c[j]
        x[17+j][17+j] += beta
        x[8][17+j] -= beta*beta*c[j]
    ax = multiply(a, x)
    au = multiply(a, u)
    assert presentation['coordinateRows'] == a
    assert presentation['xActionOnOriginal26Generators'] == [[v % MOD for v in row] for row in x]
    relations = presentation['completeDRelationMatrix']
    assert all(v % P**e[i] == 0 for i, row in enumerate(multiply(a, relations)) for v in row)
    assert all(v % P**e[i] == 0 for i, row in enumerate(multiply(ax, relations)) for v in row)
    h = product([0, 0, 0, 1], product(
        product([-8, 32, -25, 5], [-8, 32, -25, 5]),
        product(product([864, 864, 135, 5], [864, 864, 135, 5]),
                [9600, -25472, -3392, 15936, -2888, -936, 153, 50, 5])))
    assert len(h) == 24 and h[-1] == 3125
    ht = [sum(h[d]*comb(d, k)*2**(d-k) for d in range(k, len(h))) % MOD
          for k in range(len(h))]
    assert sum(v*pow(beta, k, MOD) for k, v in enumerate(ht)) % MOD == 0
    q = [0]*(len(ht)-1)
    for i in range(len(q)-1, -1, -1):
        q[i] = (ht[i+1]+(beta*q[i+1] if i+1 < len(q) else 0)) % MOD
    assert (ht[0]+beta*q[0]) % MOD == 0
    hx, qu = polynomial(ht, x), multiply(polynomial(q, x), u)
    bg = [[(c[j]*qu[i][0]+(hx[i][j-1] if j else 0)) % MOD
           for j in range(9)] for i in range(26)]
    b, xb = multiply(a, bg), multiply(ax, bg)
    sgroup = group(a, e)
    bgroup = group(join(b, xb), e)
    bxgroup = group(xb, e)
    bpxgroup = group(scaled(xb, P), e)
    singles = [group([[row[j] for row in (b[i], xb[i])] for i in range(14)], e)
               for j in range(9)]
    assert bgroup['exponents'] == [1]*6+[2, 3, 4, 4, 5]
    assert bxgroup['exponents'] == [1, 1, 1, 2] and bpxgroup['exponents'] == [1]
    assert all(g['exponents'] == [2, 5] for g in singles)
    relation_index = abs(int(fmpz_mat(relations).det()))
    assert valuation(relation_index) == sgroup['length']
    snakayama = sgroup['length']-image_length(join(scaled(a, P), ax), e)
    mnakayama = 1+sgroup['length']-image_length(join(scaled(a, P), ax, au), e)
    assert 8 <= mnakayama <= 9
    result = {'format': 'r150-original-m-root2-independent-integer-hnf-audit-v1',
              'author': 'ChatGPT (AI), Astra-ISP-789f', 'status': 'completed',
              'sourceSHA256': sha(Path(__file__).read_bytes()),
              'originalFailedRunBinding': z['binding'],
              'originalSixDigitCoordinateSHA256': 'c31f78775508475bc62e8c772309b006356593a0547307f8cb9bc83fc66bc8ca',
              'S2': sgroup, 'xS2': group(ax, e), 'pxS2': group(scaled(ax, P), e),
              'completeB': bgroup, 'xB': bxgroup, 'pxB': bpxgroup,
              'allNineOriginalSingleBTypesVerified': True,
              'minimumRootTwoPolynomialGeneratorsS2': snakayama,
              'minimumRootTwoPolynomialGeneratorsM': mnakayama,
              'generatorCountsFromIndependentLatticeIndices': True,
              'producerSmithMatricesUsed': False,
              'original42StageOutputsRehashed': output_count,
              'completeActualRelationLatticeProductsAndIndexVerified': True,
              'completionBinding': completion['binding'],
              'elapsedSeconds': time.monotonic()-start}
    args.out.write_bytes(canonical(result))
    print(json.dumps(result, sort_keys=True))

if __name__ == '__main__':
    main()
