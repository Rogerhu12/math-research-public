#!/usr/bin/env python3
"""Exact QQ divisibility lower bounds for the ORIGINAL 73x73 C/X Sylvester matrix.

No resultant is computed.  Each polynomial division is multiplied back.  A
minimum-weight perfect matching and its complete integer dual prove the
determinant lower bound.  Candidate polynomials are tested as explicit QQ[w]
polynomials; no modular reconstruction is presumed correct.
"""
import argparse
import hashlib
import json
import resource
import signal
import time
from pathlib import Path

from flint import fmpq, fmpq_mpoly_ctx, fmpq_poly


def digest(value):
    return hashlib.sha256(value).hexdigest()


def minimum_assignment(cost):
    """Hungarian minimization, returning a matching and feasible integral dual."""
    n = len(cost)
    assert n and all(len(row) == n for row in cost)
    inf = 10**15
    u, v, matching, way = ([0] * (n + 1) for _ in range(4))
    for row in range(1, n + 1):
        matching[0] = row
        col = 0
        reduced_min = [inf] * (n + 1)
        used = [False] * (n + 1)
        while True:
            used[col] = True
            active_row = matching[col]
            delta, next_col = inf, 0
            for j in range(1, n + 1):
                if not used[j]:
                    reduced = cost[active_row - 1][j - 1] - u[active_row] - v[j]
                    if reduced < reduced_min[j]:
                        reduced_min[j], way[j] = reduced, col
                    if reduced_min[j] < delta:
                        delta, next_col = reduced_min[j], j
            assert next_col and delta < inf
            for j in range(n + 1):
                if used[j]:
                    u[matching[j]] += delta
                    v[j] -= delta
                else:
                    reduced_min[j] -= delta
            col = next_col
            if matching[col] == 0:
                break
        while True:
            next_col = way[col]
            matching[col] = matching[next_col]
            col = next_col
            if col == 0:
                break
    permutation = [None] * n
    for j in range(1, n + 1):
        permutation[matching[j] - 1] = j - 1
    assert sorted(permutation) == list(range(n))
    assert all(cost[i][j] >= u[i + 1] + v[j + 1]
               for i in range(n) for j in range(n))
    objective = sum(cost[i][j] for i, j in enumerate(permutation))
    assert objective == sum(u[1:]) + sum(v[1:])
    assert all(cost[i][j] == u[i + 1] + v[j + 1]
               for i, j in enumerate(permutation))
    return objective, permutation, u[1:], v[1:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=Path, default=Path(__file__).parent)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_suffix('.receipt.json'))
    args = parser.parse_args()
    start = time.perf_counter()
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))

    def timeout(signum, frame):
        print(json.dumps({'stage': 'timeout_unknown', 'elapsedSeconds': time.perf_counter()-start}), flush=True)
        raise SystemExit(124)

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(115)
    ctx = fmpq_mpoly_ctx.get(('rho', 'lam', 'w'), 'lex')
    input_specs = [
        ('C', 'L0_original_eight_by_eight_curve.json', 'curve', 39, 53,
         '6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c'),
        ('X', 'L0_XY_P1_N1.json', None, 34, 52,
         '519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68'),
    ]
    coefficient_rows, input_receipts = [], []
    for label, filename, key, lam_degree, w_degree, expected_hash in input_specs:
        raw = (args.input_dir / filename).read_bytes()
        data = json.loads(raw)
        if key:
            data = data[key]
        polynomial = ctx.from_dict({tuple(exponent): fmpq(value) for exponent, value in data})
        assert digest(str(polynomial).encode()) == expected_hash
        assert tuple(map(int, polynomial.degrees())) == (0, lam_degree, w_degree)
        coeffs = [fmpq_poly([]) for _ in range(lam_degree + 1)]
        grouped = [dict() for _ in coeffs]
        for exponent, value in polynomial.to_dict().items():
            assert exponent[0] == 0
            grouped[int(exponent[1])][int(exponent[2])] = value
        for j, group in enumerate(grouped):
            coeffs[j] = fmpq_poly([group.get(k, fmpq(0))
                                  for k in range(max(group, default=-1) + 1)])
        reconstructed = ctx.from_dict({(0, j, k): value
            for j, coeff in enumerate(coeffs)
            for k, value in enumerate(coeff.coeffs()) if value})
        assert reconstructed == polynomial
        coefficient_rows.append(coeffs[::-1])
        input_receipts.append({'label': label, 'file': filename,
            'inputFileSha256': digest(raw), 'polynomialSha256': expected_hash,
            'lambdaDegree': lam_degree, 'wDegree': w_degree,
            'coefficientReconstructionVerified': True})
    candidates_raw = (args.input_dir / 'L0_new_support_group_candidates.json').read_bytes()
    candidates = json.loads(candidates_raw)['candidates']
    tests = [('w', [0, 1], 757), ('w-1', [-1, 1], 202),
             ('w+1', [1, 1], 63), ('2w+1', [1, 2], 33)]
    for multiplicity in [92, 36, 2, 8, 3]:
        tests.append((f'candidate_multiplicity_{multiplicity}',
                      candidates[str(multiplicity)], multiplicity))
    n, c_repeats, x_repeats = 73, 34, 39
    zero_cost = 10**9
    results = []
    print(json.dumps({'stage': 'begin', 'matrixSize': n,
        'originalPolynomialHashesVerified': True,
        'sourceSha256': digest(Path(__file__).read_bytes())}), flush=True)
    for name, phi_coeffs, target in tests:
        phi = fmpq_poly([fmpq(x) for x in phi_coeffs])
        assert phi.degree() > 0
        division_checks = 0
        trace = hashlib.sha256()
        valuations, residual_hashes = [], []
        for row_number, coeffs in enumerate(coefficient_rows):
            values, residuals = [], []
            for column_number, original in enumerate(coeffs):
                if not original:
                    values.append(None)
                    residuals.append(None)
                    continue
                current, exponent = original, 0
                while True:
                    quotient, remainder = divmod(current, phi)
                    assert quotient * phi + remainder == current
                    assert not remainder or remainder.degree() < phi.degree()
                    division_checks += 1
                    trace.update(json.dumps([row_number, column_number, exponent,
                        str(current), str(quotient), str(remainder)],
                        separators=(',', ':')).encode())
                    if remainder:
                        break
                    current = quotient
                    exponent += 1
                assert original == phi**exponent * current
                assert divmod(current, phi)[1]
                values.append(exponent)
                residuals.append(digest(str(current).encode()))
            valuations.append(values)
            residual_hashes.append(residuals)
        cv, xv = [[zero_cost if value is None else value for value in row]
                  for row in valuations]
        cost = ([[zero_cost] * j + cv + [zero_cost] * (c_repeats - 1 - j)
                 for j in range(c_repeats)] +
                [[zero_cost] * j + xv + [zero_cost] * (x_repeats - 1 - j)
                 for j in range(x_repeats)])
        assert len(cost) == n and all(len(row) == n for row in cost)
        objective, permutation, dual_rows, dual_columns = minimum_assignment(cost)
        assert all(cost[i][j] != zero_cost for i, j in enumerate(permutation))
        finite_entries = sum(value != zero_cost for row in cost for value in row)
        record = {'factorName': name, 'factorCoefficientsAscending': list(map(str, phi.coeffs())),
            'factorDegree': phi.degree(), 'modularSuggestedMultiplicity': target,
            'provedQQDivisibilityExponentLowerBound': objective,
            'reachesSuggestedMultiplicity': objective >= target,
            'C_LambdaCoefficientsDescendingPhiOrders': valuations[0],
            'X_LambdaCoefficientsDescendingPhiOrders': valuations[1],
            'nonzeroMatrixEntries': finite_entries, 'matrixSize': n,
            'everyPolynomialDivisionMultipliedBack': True, 'divisionIdentityCount': division_checks,
            'divisionTraceSha256': trace.hexdigest(), 'residualPolynomialHashes': residual_hashes,
            'minimumMatchingColumnsZeroBased': permutation,
            'dualRowPotentials': dual_rows, 'dualColumnPotentials': dual_columns,
            'completeDualConstraintCount': n*n,
            'completeDualAndPrimalEqualityVerified': True}
        results.append(record)
        print(json.dumps({'stage': 'factor_complete', 'factor': name,
            'factorDegree': int(phi.degree()), 'exactQQDeterminantDivisibilityLowerBound': objective,
            'suggestedMultiplicity': target, 'divisionChecks': division_checks,
            'elapsedSeconds': round(time.perf_counter()-start, 6)}), flush=True)
    receipt = {'sourceSha256': digest(Path(__file__).read_bytes()),
        'inputReceipts': input_receipts,
        'candidateFileSha256': digest(candidates_raw),
        'matrixDefinition': '34 shifted rows of C39_53 and 39 shifted rows of X34_52, lambda coefficients descending',
        'determinant': 'Res_lambda(C39_53,X34_52)',
        'boundArgument': 'Each nonzero determinant term is divisible by phi raised to its assignment cost; the complete integer dual bounds every cost below by the stated objective.',
        'candidateStatus': 'Explicit rational test polynomials; no reconstruction or irreducibility claim is assumed.',
        'computedAnyResultant': False, 'results': results,
        'elapsedSeconds': round(time.perf_counter()-start, 6),
        'peakRssKiB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'wholeL0Excluded': False, 'ordinaryISPClaim': False}
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    signal.alarm(0)
    print(json.dumps({'stage': 'complete',
        'receiptSha256': digest(args.output.read_bytes()),
        'receiptBytes': args.output.stat().st_size,
        'sourceSha256': receipt['sourceSha256'],
        'elapsedSeconds': receipt['elapsedSeconds'],
        'peakRssKiB': receipt['peakRssKiB'], 'wholeL0Excluded': False}), flush=True)


if __name__ == '__main__':
    main()
