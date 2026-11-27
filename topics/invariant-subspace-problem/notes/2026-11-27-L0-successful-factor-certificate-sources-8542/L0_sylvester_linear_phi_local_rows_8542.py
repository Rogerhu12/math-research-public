#!/usr/bin/env python3
"""Exact local extraction from the original QQ[w] C/X Sylvester matrix.

Only constant QQ elementary row operations and verified exact row division by
a LINEAR phi are used.  In particular no parameter-dependent pivot is inverted.
The full original matrix is reconstructed from the hash-checked C/X input.
"""
import argparse
import hashlib
import json
import resource
import signal
import time
from pathlib import Path

from flint import fmpq, fmpq_mpoly_ctx, fmpq_poly


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('root', help='rational zero of the linear factor w-root')
    parser.add_argument('--label', required=True)
    parser.add_argument('--suggested', type=int, required=True)
    parser.add_argument('--input-dir', type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    start = time.perf_counter()
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    alpha = fmpq(args.root)
    phi = fmpq_poly([-alpha, 1])
    n = 73
    trace = hashlib.sha256()
    state = {'factorRoot': str(alpha), 'factorCoefficientsAscending': list(map(str, phi.coeffs())),
             'matrixSize': n, 'sourceSha256': sha(Path(__file__).read_bytes()),
             'provedQQDivisibilityExponentLowerBound': 0,
             'modularSuggestedMultiplicity': args.suggested,
             'exactQQDivisibilityExponent': None,
             'fullRankModuloPhiProved': False,
             'constantElementaryRowOperations': 0, 'rowSwaps': 0,
             'rowOperationPolynomialMultiplyBackCount': 0,
             'exactDivisionPolynomialMultiplyBackCount': 0,
             'rounds': [], 'computedAnyResultant': False,
             'parameterPivotsInverted': False,
             'wholeL0Excluded': False, 'ordinaryISPClaim': False}
    output = args.input_dir / f'L0_local_phi_{args.label}_8542.receipt.json'

    def save(stage):
        state['stage'] = stage
        state['elapsedSeconds'] = round(time.perf_counter()-start, 6)
        state['peakRssKiB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        state['operationTraceSha256'] = trace.hexdigest()
        output.write_text(json.dumps(state, indent=2, sort_keys=True) + '\n')
        print(json.dumps({'stage': stage, 'factor': args.label,
            'lowerBound': state['provedQQDivisibilityExponentLowerBound'],
            'exact': state['exactQQDivisibilityExponent'],
            'completedRounds': len(state['rounds']),
            'rowOperations': state['constantElementaryRowOperations'],
            'elapsedSeconds': state['elapsedSeconds'],
            'peakRssKiB': state['peakRssKiB'],
            'receiptSha256': sha(output.read_bytes())}), flush=True)

    def timeout(signum, frame):
        save('timeout_partial_verified_lower_bound')
        raise SystemExit(124)

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(175)
    ctx = fmpq_mpoly_ctx.get(('rho', 'lam', 'w'), 'lex')
    inputs = [
        ('L0_original_eight_by_eight_curve.json', 'curve', 39, 53,
         '6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c'),
        ('L0_XY_P1_N1.json', None, 34, 52,
         '519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68')]
    coefficient_rows = []
    state['inputs'] = []
    for filename, key, lam_degree, w_degree, expected in inputs:
        raw = (args.input_dir / filename).read_bytes()
        data = json.loads(raw)
        if key:
            data = data[key]
        polynomial = ctx.from_dict({tuple(exponent): fmpq(value) for exponent, value in data})
        assert sha(str(polynomial).encode()) == expected
        assert tuple(map(int, polynomial.degrees())) == (0, lam_degree, w_degree)
        grouped = [dict() for _ in range(lam_degree + 1)]
        for exponent, value in polynomial.to_dict().items():
            assert exponent[0] == 0
            grouped[int(exponent[1])][int(exponent[2])] = value
        coeffs = [fmpq_poly([dd.get(k, fmpq(0)) for k in range(max(dd, default=-1)+1)])
                  for dd in grouped]
        assert ctx.from_dict({(0, j, k): value
            for j, coeff in enumerate(coeffs)
            for k, value in enumerate(coeff.coeffs()) if value}) == polynomial
        coefficient_rows.append(coeffs[::-1])
        state['inputs'].append({'filename': filename, 'fileSha256': sha(raw),
                                'polynomialSha256': expected})
    cp, xp = coefficient_rows
    zero = fmpq_poly([])
    matrix = ([[zero]*j + cp + [zero]*(33-j) for j in range(34)] +
              [[zero]*j + xp + [zero]*(38-j) for j in range(39)])
    assert len(matrix) == n and all(len(row) == n for row in matrix)
    save('begin_original_matrix_verified')

    def complexity(value):
        return abs(int(value.numerator)).bit_length() + int(value.denominator).bit_length()

    while True:
        constants = [[entry(alpha) for entry in row] for row in matrix]
        operations = []
        rank = 0
        pivots = []
        constant_identity_checks = 0
        for column in range(n):
            candidates = [i for i in range(rank, n) if constants[i][column]]
            if not candidates:
                continue
            pivot_row = min(candidates, key=lambda i: (complexity(constants[i][column]), i))
            if pivot_row != rank:
                constants[rank], constants[pivot_row] = constants[pivot_row], constants[rank]
                operations.append(('swap', rank, pivot_row, None))
            pivot = constants[rank][column]
            assert pivot
            pivots.append([column, str(pivot)])
            for i in range(rank + 1, n):
                entry = constants[i][column]
                if not entry:
                    continue
                factor = entry / pivot
                assert factor * pivot == entry
                before = constants[i]
                after = [a-factor*b for a,b in zip(before, constants[rank])]
                assert all(a == c+factor*b for a,b,c in zip(before, constants[rank], after))
                constant_identity_checks += n
                assert not after[column]
                constants[i] = after
                operations.append(('subtract', i, rank, factor))
            rank += 1
            if rank == n:
                break
        assert all(not any(row) for row in constants[rank:])
        const_hash = sha(json.dumps([[str(value) for value in row] for row in constants],
                                   separators=(',', ':')).encode())
        if rank == n:
            state['exactQQDivisibilityExponent'] = state['provedQQDivisibilityExponentLowerBound']
            state['fullRankModuloPhiProved'] = True
            state['terminalNonzeroPivots'] = pivots
            state['terminalGaussianRowOperationCount'] = len(operations)
            state['terminalConstantIdentityCount'] = constant_identity_checks
            state['terminalEchelonSha256'] = const_hash
            signal.alarm(0)
            save('complete_exact_phi_order')
            break
        for kind, i, j, factor in operations:
            if kind == 'swap':
                matrix[i], matrix[j] = matrix[j], matrix[i]
                state['rowSwaps'] += 1
                trace.update(json.dumps(['swap',i,j], separators=(',', ':')).encode())
                continue
            before = matrix[i]
            after = [a-factor*b for a,b in zip(before, matrix[j])]
            assert all(a == c+factor*b for a,b,c in zip(before, matrix[j], after))
            matrix[i] = after
            state['constantElementaryRowOperations'] += 1
            state['rowOperationPolynomialMultiplyBackCount'] += n
            trace.update(json.dumps(['subtract',i,j,str(factor)], separators=(',', ':')).encode())
        assert all(entry(alpha) == constants[i][j]
                   for i,row in enumerate(matrix) for j,entry in enumerate(row))
        for i in range(rank, n):
            assert any(matrix[i])
            quotients = []
            for entry in matrix[i]:
                quotient, remainder = divmod(entry, phi)
                assert not remainder and quotient * phi == entry
                quotients.append(quotient)
            matrix[i] = quotients
            state['exactDivisionPolynomialMultiplyBackCount'] += n
            state['provedQQDivisibilityExponentLowerBound'] += 1
            trace.update(json.dumps(['divide_row_by_phi',i], separators=(',', ':')).encode())
        state['rounds'].append({'rankModuloPhi': rank, 'extractedRows': n-rank,
             'totalExponent': state['provedQQDivisibilityExponentLowerBound'],
             'constantRowOperationsIncludingSwaps': len(operations),
             'constantIdentityCount': constant_identity_checks,
             'echelonSha256': const_hash,
             'nonzeroPivotsSha256': sha(json.dumps(pivots, separators=(',', ':')).encode())})
        save('exact_local_extraction_round')


if __name__ == '__main__':
    main()
