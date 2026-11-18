#!/usr/bin/env python3
"""Read-only native long-double capability and existing finite-model survey.

No new flow, root, Jacobian, numerical DN or generated executable is run.
The compiler only preprocesses macros and checks a small declaration unit.
"""
import argparse
import datetime
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import shutil
import struct
import subprocess
import sys
import numpy as np
from record_fixed_actual import load, sha, scalar_tree


def ident(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def command(args, source=None):
    p = subprocess.run(args, input=source, text=True, capture_output=True, check=False)
    return dict(command=args, input=source, returncode=p.returncode, stdout=p.stdout, stderr=p.stderr)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scratch-root', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise ValueError('Do not overwrite completed capability evidence')
    work = a.scratch_root.resolve()/'n4_work'
    cs_path = work/'parts32-frozen-mp-baseline-v1/capsule-summary.json'
    cs = load(cs_path)
    if sha(cs['coefficients']['path']) != cs['coefficients']['sha256']:
        raise ValueError('Original frozen coefficient capsule changed')
    capsule = load(cs['coefficients']['path'])
    cpp = '''#include <cmath>
#include <cfloat>
#include <limits>
static_assert(LDBL_MANT_DIG == 64);
static_assert(sizeof(long double) == 16);
long double (*sq)(long double) = std::sqrt;
long double (*lp)(long double) = std::log1p;
long double (*em)(long double) = std::expm1;
'''
    flags = ['-std=c++17', '-O2', '-fno-fast-math', '-ffp-contract=off',
             '-fexcess-precision=standard', '-frounding-math']
    version = command(['g++', '--version'])
    macros = command(['gcc', '-dM', '-E', '-x', 'c', '-'], '#include <float.h>\n')
    relevant = ('LDBL_MANT_DIG', 'LDBL_MAX_EXP', 'SIZEOF_LONG_DOUBLE', 'FINITE_MATH_ONLY',
                'GNUC__', 'GNUC_MINOR__')
    macros['full_stdout_sha256'] = hashlib.sha256(macros['stdout'].encode()).hexdigest()
    macros['stdout'] = '\n'.join(line for line in macros['stdout'].splitlines()
                                 if any(key in line for key in relevant))
    syntax = command(['g++', '-x', 'c++']+flags+['-fsyntax-only', '-'], cpp)
    if any(r['returncode'] for r in (version, macros, syntax)):
        raise RuntimeError('Static capability check failed')
    frozen_gaps = []
    for fixture in capsule['fixtures']:
        gaps = [Fraction.from_float(point['coefficients']['E'])-
                (1+Fraction.from_float(point['coefficients']['w2'])) for point in fixture['points']]
        largest = max(gaps, key=abs)
        frozen_gaps.append(dict(stage=fixture['stage'], points=len(gaps),
            nonzero_E_minus_one_plus_w2_count=sum(bool(v) for v in gaps),
            maximum_absolute_E_identity_gap=float(abs(largest)),
            signed_largest_gap_exact_fraction=str(largest)))
    trig = {}
    for kind in ('cos', 'sin'):
        left = [float(v) for row in capsule['trig']['state_'+kind] for v in row]
        right = [float(v) for row in capsule['trig']['jacobian_'+kind] for v in row]
        if len(left) != len(right):
            raise ValueError('Original state/Jacobian trig dimensions differ')
        trig[kind] = dict(entries=len(left), different_binary64_entries=sum(
            struct.pack('<d', x) != struct.pack('<d', y) for x, y in zip(left, right, strict=True)),
            maximum_absolute_difference=max(abs(x-y) for x, y in zip(left, right, strict=True)))
    timing = {}
    for name, relative in (
        ('original_full_Jac_locator', 'raw-primaryb016-lam002-actual-m20-parts32-v1/one-ulp-locate-resource.json'),
        ('original_state_and_Jac_map_check', 'raw-primaryb016-lam002-actual-m20-parts32-v1/map-consistency-resource.json'),
        ('original_failed_DN_continuation', 'raw-primaryb016-lam002-actual-m20-parts32-v1/one-ulp-resource.json'),
        ('old_three_stage_MP90_state_only', 'parts32-frozen-mp90-v1/resource.json')):
        path = work/relative
        resource = load(path)
        if resource['status'] != 'observed_terminal':
            raise ValueError('An old timing lacks a real terminal')
        timing[name] = dict(identity=ident(path), observed=scalar_tree(resource))
    model_sources = {}
    directory = work/'shared-periodic-source/scripts'
    for relative in ('periodic-quadrature/general_root_tail_momentum.mjs',
                     'periodic-quadrature/f6tail_fast_momentum.mjs',
                     'periodic-quadrature/f6tail_momentum_split_flux.mjs',
                     'periodic-quadrature/f6tail_fast_split_flux_engine.mjs',
                     '950f-tail-stage-core.mjs'):
        model_sources[relative] = ident(directory/relative)
    headers = ['/usr/include/node/node_api.h', '/usr/include/nodejs/src/node_api.h',
               '/usr/include/nlohmann/json.hpp',
               str(Path(shutil.which('node')).resolve().parent.parent/'include/node/node_api.h')]
    result = dict(scope=__doc__, created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source=ident(__file__), helper=ident(Path(__file__).with_name('record_fixed_actual.py')),
        command=sys.argv, platform=platform.platform(), machine=platform.machine(),
        compiler=version, predefined_macros=macros, syntax_only_check=syntax,
        compiler_identity=ident(Path(shutil.which('g++')).resolve()), proposed_flags=flags,
        numpy_crosscheck=dict(nmant=np.finfo(np.longdouble).nmant,
            precision_significand_bits_including_leading_bit=np.finfo(np.longdouble).nmant+1,
            exponent_bits=np.finfo(np.longdouble).iexp, itemsize=np.dtype(np.longdouble).itemsize,
            epsilon=str(np.finfo(np.longdouble).eps)),
        precision_scope='This platform has64 significand bits in16 storage bytes, an80-bit extended format with padding. It is not binary128. No native mathematical evaluator is implemented or executed here.',
        optional_headers_observed={path:Path(path).exists() for path in headers},
        proposed_binding='No Node addon is assumed. One compiled scalar kernel can expose a C ABI for the three-stage harness and a binary whole-evaluate batch CLI for the existing synchronous Node caller.',
        original_capsule=ident(cs_path), original_coefficients=cs['coefficients'],
        original_model_sources=model_sources, frozen_E_identity_gaps={str(v['stage']):v for v in frozen_gaps},
        state_vs_original_fast_Jac_trig=trig,
        existing_timings=timing,
        exact_work_counts=dict(stages=2304, modes=20, physical_dimension=40, complete_state_dimension=42,
            RK_steps_per_stage=16, RK_fields_per_stage=64,
            dense_tangent_multiply_accumulate_terms_per_stage=42*40*40*64,
            dense_tangent_multiply_accumulate_terms_whole_2304=42*40*40*64*2304,
            full42_by40_tangents_binary64_bytes=2304*42*40*8,
            original_physical40_by40_tangents_binary64_bytes=2304*40*40*8,
            nominal48_point32_coefficient_binary64_bytes=2304*48*32*8),
        performance_scope='Operation/data counts are exact for the stated unoptimized shapes. Old wall times include initialization/export; none is a native benchmark or a rigorous whole-tail cost prediction.',
        future_Jacobian_scope='Differentiate the frozen literal moment/RHS formulas using their state trig and independent coefficients. The original point Newton B remains the iteration matrix; the literal implicit B_exact must be derived separately. Evaluate implicit derivatives at the returned approximate root; do not claim differentiation of stopping/branch/roundoff behavior.')
    encoded = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    if len(encoded.encode()) >= 100000:
        raise ValueError('Compact capability evidence exceeds100KB')
    a.out.write_text(encoded)
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out),
                         E_identity_gaps=result['frozen_E_identity_gaps'], trig=trig)))


if __name__ == '__main__':
    main()
