#!/usr/bin/env python3
"""Exact angular Rayleigh lower at an ACTUAL stored mirror-prefix inlet.

The map is read from its defining saved nodal constants. No BVP, DN, ODE,
producer, target constructor, bridge solver or new candidate is run.
The lower persists under every positive radial rescaling and every common-cut
extension that retains this inlet and the declared exact flat target there.
No completed common-cut graph or closed surface is asserted by this check.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import time

import numpy as np


HERE = Path(__file__).resolve().parent
BUDGET = Q(1, 500_000_000)
SOURCES = {
    '950f-root-fullxyz-hermite.py': '4f60dbd1735268e2f4953748d12c4a87099d49ddf69dcb34d40b9f26986d0bd9',
    'db6f-root-mirror-hermite.py': 'ddb785a7e5199f1488fa50937668fc5236a1dee7b24679f75b39a4f15cb7f4b6',
    'db6f-audit-metric-supplier.py': 'de2cafcb235a843b2f930decb54cf065c6cbc441884b050f09edb900ac196bd0',
    'db6f-root-common-cut-v2.py': '317e519fda8d78fb70b53f8a8c80d51599dec1ac46e92741cd9b2576a3f4fa7d',
    '78718-prefix-fullxyz-hermite-storage-v1.py': '2ab813fba7d3a33ef273799a4f6d27628b9cc2f98285fb3d3371fdacb49b009d',
    '78718-prefix-mirror-hermite-storage-v1.py': 'f975ab40ca05f5237954398533934eda2365ceda38cb0ba4dfe8d9e3287f6957',
    '78718-prefix-metric-supplier-storage-v1.py': 'f2d8e79504a2a3895ec8705457eabe46321e80b68b8e7c7de11f13015d160ff3',
    '78718-prefix-common-cut-storage-v1.py': '34b0b92c6f4d92bd497f3d84d28cbd73cb29271e36b240d3a19795987f057d43',
    '78718-prefix-storage-v1.py': '83cf59cfe5ab373421e53d0c0d8d2274edfc6a6b266fc2ab6161274b474a4329',
    '78718-prefix-byte-shards-v1.py': 'e23153ae6b364854a24acc464be97921b134f7e25024e82c8c91995ca2f96f39',
    'db6f-prefix-flat-geometry-source.py': '23299890cebc07c938910995058d8e2ee09fbf289d323a3cac65bc3afc117c6f',
    'db6f-prefix-flat-profile.py': '5066cd6d8f94d3b22c0450cc2016df6f90d04efb85d7a13bc833c11868eaaa4b',
    'db6f-root-exact-bridge.py': 'f5d10784f58fa5008220354665de710ab4991b795f1b902e26a70ca44f382fd1',
}
FAMILIES = {
    'original': ('950f-root-fullxyz-hermite.py', 'db6f-root-mirror-hermite.py',
                 'db6f-audit-metric-supplier.py', 'db6f-root-common-cut-v2.py'),
    'storage': ('78718-prefix-fullxyz-hermite-storage-v1.py',
                '78718-prefix-mirror-hermite-storage-v1.py',
                '78718-prefix-metric-supplier-storage-v1.py',
                '78718-prefix-common-cut-storage-v1.py'),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(path):
    p = Path(path).resolve()
    require(p.is_file() and p.stat().st_size < 5_000_000,
            'Missing or oversized physical file: '+str(p))
    raw = p.read_bytes()
    return {'path': str(p), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def display(value):
    """Exact Fraction plus certified binary and decimal enclosures."""
    mid = float(value)
    require(math.isfinite(mid), 'Unbounded reported scalar')
    qmid = Q.from_float(mid)
    low = math.nextafter(mid, -math.inf) if qmid > value else mid
    high = math.nextafter(mid, math.inf) if qmid < value else mid
    require(Q.from_float(low) <= value <= Q.from_float(high), 'Bad binary enclosure')
    grid = 10**24
    scaled = value*grid
    a = scaled.numerator//scaled.denominator
    b = -((-scaled.numerator)//scaled.denominator)
    def decimal(integer):
        sign = '-' if integer < 0 else ''
        integer = abs(integer)
        whole, part = divmod(integer, grid)
        return sign+str(whole)+'.'+str(part).zfill(24)
    require(Q(decimal(a)) <= value <= Q(decimal(b)), 'Bad decimal enclosure')
    return {'exact': str(value), 'binary64_lower': low, 'binary64_upper': high,
            'decimal_lower_exact': decimal(a), 'decimal_upper_exact': decimal(b)}


def inlet_axis(row, modes, warp, alternating):
    sign = -1 if alternating else 1
    tangent = Q.from_float(float(row[0]))
    for j in range(1, modes+1):
        tangent += sign**j*(Q.from_float(float(row[j]))+
                             3*j*Q.from_float(float(row[modes+j])))
    rho = 1-sign*warp
    require(rho > 0, 'Inlet target chart is not regular at this axis')
    relative = tangent*tangent/(rho*rho)-1
    return {'axis_exact': 'pi/3' if alternating else '0',
            'angular_tangent_coefficient': display(tangent),
            'target_rho': display(rho), 'target_metric_psipsi': display(rho*rho),
            'map_metric_psipsi': display(tangent*tangent),
            'relative_signed_error': display(relative),
            'relative_operator_lower': display(abs(relative))}, abs(relative)


def run(args):
    start = time.monotonic()
    require(not args.out.exists(), 'Refuse to replace a prior exact report')
    source_records = []
    for name, expected in SOURCES.items():
        record = identity(HERE/name)
        require(record['sha256'] == expected, 'Frozen source changed: '+name)
        source_records.append(record)
    geometry_id, target_id = identity(args.geometry), identity(args.target)
    meta = json.loads(args.geometry.read_text())
    target = json.loads(args.target.read_text())
    family = 'storage' if 'data_storage' in meta else 'original'
    producer, mirror, supplier, common = FAMILIES[family]
    require(meta.get('representation') is None and meta.get('mirror_inlet_C2_exact') is True
            and meta.get('ell') == 0., 'Input is not the actual uncorrected mirror prefix')
    require(meta.get('script_sha256') == SOURCES[producer]
            and meta.get('wrapper_sha256') == SOURCES[mirror]
            and meta.get('profile_loader_sha256') == SOURCES['db6f-prefix-flat-geometry-source.py']
            and meta.get('profile_implementation_sha256') == SOURCES['db6f-prefix-flat-profile.py'],
            'Actual prefix source identity differs')
    require(target.get('geometry_sha256') == geometry_id['sha256']
            and target.get('script_sha256') == SOURCES[supplier]
            and target.get('frozen_profile') == meta.get('frozen_profile'),
            'Exact target is not bound to this prefix and source family')
    require(meta['frozen_profile'].get('ramp_law') == 'flat', 'Different target core profile')
    chart = meta['chart']
    require(chart['knots'][0] == 0. and chart['values'][0] == 1.,
            'Target does not have the proved exact inlet spline value')
    qref = meta['warp_reference_q']
    require(type(qref) in (int, float) and math.isfinite(qref) and 0 < qref < .125,
            'Invalid inlet warp reference')
    warp = 8*Q.from_float(float(qref))
    inputs = [geometry_id, target_id]
    for name, key in [('checkpoint', 'checkpoint_sha256'), ('linear_port', 'port_sha256')]:
        record = identity(meta[name])
        require(record['sha256'] == meta[key], 'Original source file changed: '+name)
        inputs.append(record)
    if family == 'storage':
        spec = importlib.util.spec_from_file_location('inlet_lower_explicit_storage',
                HERE/'78718-prefix-storage-v1.py')
        storage = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(storage)
        saved_meta, payload, bindings = storage.read_payload(args.geometry, verify_arrays=True)
        require(saved_meta == meta, 'Prefix metadata changed during storage read')
        for record in bindings:
            actual = identity(record['file'])
            require(actual['bytes'] == record['bytes'] and actual['sha256'] == record['sha256'],
                    'Logical storage binding changed')
            inputs.append(actual)
    else:
        require('data_storage' not in meta and type(meta['data_file']) is str
                and Path(meta['data_file']).name == meta['data_file'], 'Invalid original single container')
        data_path = args.geometry.parent/meta['data_file']
        record = identity(data_path)
        require(record['sha256'] == meta['data_sha256'], 'Original prefix bytes changed')
        inputs.append(record)
        payload = data_path.read_bytes()
    M, N = meta['modes'], meta['nodes']
    require(type(M) is int and M > 0 and type(N) is int and N >= 3, 'Bad defining dimensions')
    with np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False) as saved:
        require(len(saved.files) == 3 and set(saved.files) == {'mesh','jets','mean_increments'},
                'Unexpected defining arrays')
        mesh, jets, increments = saved['mesh'], saved['jets'], saved['mean_increments']
    for array, shape in [(mesh,(N,)), (jets,(3,N,3*M+2)), (increments,(N-1,))]:
        require(array.dtype.str == '<f8' and array.shape == shape and np.isfinite(array).all(),
                'Nonfinite or differently typed defining array')
    require(mesh[0] == 0. and np.all(np.diff(mesh) > 0), 'Invalid prefix mesh')
    require(np.all(jets[0,0,2*M+1:] == 0.) and np.all(jets[1,0,:-1] == 0.)
            and jets[1,0,-1] == 1. and np.all(jets[2,0,2*M+1:] == 0.),
            'Stored inlet does not have the defining mirror parity')
    correction_start = int(np.searchsorted(mesh, mesh[-1]-.15))
    require(0 < correction_start < N-1, 'Declared common-cut support reaches the inlet')
    computed = [inlet_axis(jets[0,0], M, warp, alternating) for alternating in (False,True)]
    witness, lower = max(computed, key=lambda item:item[1])
    report = {'schema':'78718-stored-prefix-inlet-angular-lower-v1',
        'status':'EXACT_STORED_INLET_ANGULAR_RAYLEIGH_LOWER_COMPUTED',
        'script':identity(__file__), 'source_bindings':source_records,
        'input_bindings':sorted({row['path']:row for row in inputs}.values(), key=lambda row:row['path']),
        'storage_family':family, 'modes':M, 'nodes':N,
        'native_node_index':0, 's_exact':'0', 'target_radius_at_inlet_exact':'1',
        'warp_at_inlet':display(warp), 'axes':[row for row,_ in computed],
        'witness_axis_exact':witness['axis_exact'], 'relative_operator_lower':display(lower),
        'original_budget_exact':str(BUDGET), 'exceeds_original_budget':lower > BUDGET,
        'common_extension_conditions':{
            'implementation':str(HERE/common), 'implementation_sha256':SOURCES[common],
            'requested_width_float_hex':(.15).hex(), 'correction_start_index':correction_start,
            'start_coordinate':display(Q.from_float(float(mesh[correction_start]))),
            'correction_identically_zero_near_inlet':True,
            'radial_change':'sigma=lambda*s for any constant lambda>0; no angular change at s=0',
            'exact_final_target':'a_*(0)=1 and the same frozen angular chart at the inlet',
            'lower_persists_for_every_extension_satisfying_these_conditions':True},
        'scope':{'exact_saved_finite_map':True, 'exact_point_lower':True,
            'complete_common_cut_generated_or_claimed':False, 'exact_bridge_root_recomputed':False,
            'complete_closed_surface_claimed':False, 'new_M15_success_claimed':False,
            'infinite_exact_isometry_rejected':False, 'new_acceptance_requirement':False},
        'solver_calls':0, 'DN_calls':0, 'ODE_calls':0, 'producer_calls':0,
        'seconds':time.monotonic()-start}
    for record in [report['script'], *source_records, *report['input_bindings']]:
        require(identity(record['path']) == record, 'Input or source changed during exact read')
    encoded = (json.dumps(report,indent=2,sort_keys=True)+'\n').encode()
    require(len(encoded) < 1_000_000, 'Report unexpectedly large')
    with args.out.open('xb') as stream:
        stream.write(encoded)
    print(json.dumps({'status':report['status'], 'output':identity(args.out),
        'witness_axis':witness['axis_exact'], 'strict_safe_decimal_lower':
        report['relative_operator_lower']['decimal_lower_exact'],
        'exceeds_original_budget':lower > BUDGET, 'solver_calls':0},sort_keys=True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geometry',type=Path,required=True)
    parser.add_argument('--target',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    run(parser.parse_args())


if __name__ == '__main__':
    main()
