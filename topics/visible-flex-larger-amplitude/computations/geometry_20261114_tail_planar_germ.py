#!/usr/bin/env python3
"""Exact nonplanarity checks for the finite background-preserving tail/collar.

For each radial polynomial piece, evaluate the determinant of four cardinal
angular positions using exact rational arithmetic. The angular mean (including
the external source background height) cancels. This certifies only the finite
polynomial field defined by the loaded coefficients; a tiny nonzero determinant
does not give a perturbation-stable nonplanarity certificate for an exact limit.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from exact_20261114_refined_tail_adapter import (
    hermite, module, prefix_cut_coefficients, sha)

HERE = Path(__file__).resolve().parent


def rational(x):
    if isinstance(x, F):
        return x
    if isinstance(x, (int, np.integer)):
        return F(int(x))
    n, d = x.as_integer_ratio()
    return F(int(n), int(d))


def cardinal(c):
    """Exact four-angle values of one complex Fourier coefficient array.

    All three zero-frequency coordinates are dropped: they translate each
    latitude and therefore cancel from the coplanarity determinant.
    """
    out = [[F(0) for _ in range(3)] for _ in range(4)]
    for frequency in range(1, len(c)):
        for component in range(3):
            value = c[frequency, component]
            re, im = rational(value.real), rational(value.imag)
            if not re and not im:
                continue
            for angle in range(4):
                power = (frequency*angle) % 4
                out[angle][component] += (re, -im, -re, im)[power]
    return out


def polynomial_cardinals(coefficients):
    return [cardinal(c) for c in coefficients]


def at(coefficients, t):
    result = [[F(0) for _ in range(3)] for _ in range(4)]
    for coefficient in reversed(coefficients):
        for j in range(4):
            for k in range(3):
                result[j][k] = result[j][k]*t+coefficient[j][k]
    return result


def add(a, b):
    return [[a[j][k]+b[j][k] for k in range(3)] for j in range(4)]


def det(points):
    a, b, c = [[points[j][k]-points[0][k] for k in range(3)]
               for j in range(1,4)]
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def determinant_record(value):
    # Every assertion has already been decided by exact Fraction operations.
    # Store compact hashes rather than megabytes of reproducible huge integers.
    numerator, denominator = str(value.numerator), str(value.denominator)
    return dict(sign=1 if value > 0 else -1 if value < 0 else 0,
                numerator_bits=abs(value.numerator).bit_length(),
                denominator_bits=value.denominator.bit_length(),
                numerator_sha256=hashlib.sha256(numerator.encode()).hexdigest(),
                denominator_sha256=hashlib.sha256(denominator.encode()).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('checkpoint', 'source-topic', 'port', 'config', 'complete', 'plan', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    if args.out.exists():
        raise FileExistsError('Refusing to replace existing evidence')
    base = module('geometry_tail_nonplanar_loader', HERE/'exact_20261114_refined_closed_assembly.py')
    saved, tail, config = base.load(args)
    plan = base.read(args.plan)
    for key, path in (('checkpoint', args.checkpoint), ('port', args.port),
                      ('config', args.config), ('complete', args.complete)):
        if plan['inputs'][key]['sha256'] != sha(path):
            raise ValueError('Plan binding differs for '+key)
    cuff, inner, cut, width = [float(plan[k]) for k in
                              ('cuff', 'tail_inner', 'cut', 'cut_correction_width')]
    if float(tail.r[0]) != inner or float(tail.r[-1]) != cut:
        raise ValueError('Tail bounds differ from plan')
    if not cuff < inner < cut or not 0 < width < cut-inner:
        raise ValueError('Invalid collar or fixed outer correction width')
    sigma = float(saved.flow.bridge.sigma)
    if sigma != -1:
        raise ValueError('Expected the reflected positive-r upper tail')

    # The cut target is evaluated with zero angular mean. Only k=0 differs
    # from the actual assembly; each determinant is translation-invariant.
    target, cut_geometry = prefix_cut_coefficients(saved, 0., 0., tail.N//2)
    outer = tail.node_coefficients(len(tail.r)-1)
    reflection = np.array([1., 1., sigma])
    aligned = [c.copy()*reflection for c in outer]
    for order, radius in enumerate((cut, 1., 0.)):
        aligned[order][1,:2] += np.array([radius, -1j*radius])
    differences = np.stack([(a-b)*reflection for a,b in zip(target, aligned)])
    differences[:,0,:] = 0  # Common translations only.
    zero = np.zeros_like(target[0])
    patch = hermite(zero, differences[0], zero, differences[1],
                    zero, differences[2], np.longdouble(width))
    inner_coeff = tail.node_coefficients(0)
    collar = hermite(zero, inner_coeff[0], zero, inner_coeff[1],
                     zero, inner_coeff[2], np.longdouble(inner-cuff))
    patch_values = polynomial_cardinals(patch)
    patch_start = rational(cut-width)  # Same binary64 scalar as the adapter.
    patch_width = rational(width)
    patch_end = patch_start+patch_width
    witness, failed = [], []

    def check_piece(label, lo, hi, origin, span_width, coefficients):
        polynomial = None
        constant = cardinal(coefficients[0])

        def value(radius):
            nonlocal polynomial
            t = (radius-origin)/span_width
            if t == 0:
                positions = [row[:] for row in constant]
            else:
                if polynomial is None:
                    polynomial = polynomial_cardinals(coefficients)
                positions = at(polynomial, t)
            if radius >= patch_start:
                pt = min(F(1), max(F(0), (radius-patch_start)/patch_width))
                positions = add(positions, at(patch_values, pt))
            for row in positions:
                row[2] *= -1
            # Add the exact rotational horizontal background r(cos,sin).
            for j, (co,si) in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
                positions[j][0] += co*radius
                positions[j][1] += si*radius
            return det(positions)

        # On this piece the determinant is a polynomial of degree <=15.
        # Sixteen distinct rational samples decide whether it is identically
        # zero. Endpoints are legitimate witnesses by polynomial continuity.
        fractions = [F(0), F(1), F(1,2)]
        fractions += [F(j,15) for j in range(1,15) if F(j,15) not in fractions]
        for fraction in fractions:
            radius = lo+(hi-lo)*fraction
            determinant = value(radius)
            if determinant:
                witness.append(dict(piece=label, lo=str(lo), hi=str(hi),
                    witness_radius=str(radius), witness_relative_position=str(fraction),
                    determinant=determinant_record(determinant)))
                return
        failed.append(dict(piece=label, lo=str(lo), hi=str(hi),
                           reason='The four-cardinal coplanarity polynomial is identically zero; this test does not prove a planar surface.'))

    check_piece('inner-collar', rational(cuff), rational(inner), rational(cuff),
                rational(inner-cuff), collar)
    for i in range(len(tail.r)-1):
        lo, hi = rational(tail.r[i]), rational(tail.r[i+1])
        span_width = rational(tail.r[i+1]-tail.r[i])
        cuts = [lo]+[x for x in (patch_start,patch_end) if lo < x < hi]+[hi]
        cuts = sorted(set(cuts))
        coefficients = tail.span(i)
        for part,(left,right) in enumerate(zip(cuts,cuts[1:])):
            check_piece(f'tail-{i}-part-{part}', left, right, lo, span_width, coefficients)
        if (i+1) % 128 == 0:
            print(json.dumps(dict(event='exact_tail_nonplanarity', completed_spans=i+1,
                                  uncovered=len(failed), seconds=time.monotonic()-started)), flush=True)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    witness_path = args.out.with_name(args.out.stem+'-witnesses.json.gz')
    if witness_path.exists():
        raise FileExistsError('Refusing to replace existing witness archive')
    raw = (json.dumps(witness,separators=(',',':'))+'\n').encode()
    encoded = gzip.compress(raw,compresslevel=9,mtime=0)
    if len(encoded) >= 5_000_000:
        raise ValueError('Witness archive would exceed repository size limit')
    witness_path.write_bytes(encoded)
    result = dict(schema='finite-background-tail-planar-germ-inputs-v1',
        source_sha256=sha(__file__),
        input_sha256={key:sha(getattr(args,key.replace('-','_'))) for key in
                      ('checkpoint','port','config','complete','plan')},
        adapter_sha256=sha(HERE/'exact_20261114_refined_tail_adapter.py'),
        tail_spans=len(tail.r)-1, polynomial_subpieces_checked=len(witness)+len(failed),
        all_finite_tail_and_collar_pieces_nonplanar=not failed,
        uncovered=failed, witness_file=witness_path.name,
        witness_sha256=sha(witness_path), witness_raw_sha256=hashlib.sha256(raw).hexdigest(),
        finite_field_definition='Exact rational interpretation of the binary floating Fourier/Hermite coefficients produced by the unchanged RefinedTail adapter, including its fixed outer Cartesian patch and finite inner collar. All source angular means cancel from the determinant.',
        patch_interval_exact=[str(patch_start),str(patch_end)],
        exact_limit_nonplanarity_certified=False, full_closed_embedding_certified=False,
        actual_delta_E_certified=False, task_completed=False,
        limitations=['A nonzero determinant may be arbitrarily small; no stability under refinement or exact correction is claimed.',
                     'The finite Fourier field after rFFT is the audited object; no unproved parity projection is made.',
                     'Embedding, C2 gluing of the represented pieces, topology, and genuine continuous image variation remain separate inputs to R238.',
                     'Zero-frequency translations, including the arbitrary source mean height, are eliminated exactly; no source mean is approximated by zero in the actual closed map.'],
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out), completed_spans=len(tail.r)-1,
                         uncovered=len(failed), actual_delta_E_certified=False,
                         seconds=result['seconds'])), flush=True)
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
