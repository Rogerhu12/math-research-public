#!/usr/bin/env python3
"""Plan extra physical restart nodes from an accepted raw RMS ledger.

This uses only the standard library and never loads a Flow, evaluates the
surface RHS, or starts a solver.  Raw numerical interval indices are first
matched to the saved physical quintic knots.  Each selected physical interval
is bisected once.  A later fixed-metric restart must map these physical nodes
through its own inverse_chart and evaluate the original saved PPoly/pullback.
The old normalized t values are not valid new-chart nodes in general.

The plan changes only a warm initial mesh.  It does not certify the saved
physical metric, predict the new RMS residual, or change a solver tolerance.
"""
from __future__ import annotations
import argparse
import array
import ast
import bisect
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import sys


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def vector_from_manifest(manifest, name, hashes):
    """Read a verified 1D float64 .npy.gz vector without importing NumPy."""
    record = document(manifest)
    item = record['arrays'][name]
    if len(item['shape']) != 1 or item['dtype'] != 'float64':
        raise ValueError('Expected a one-dimensional raw float64 vector')
    values = []
    for chunk in item['chunks']:
        if chunk['first'] != len(values) or Path(chunk['file']).name != chunk['file']:
            raise ValueError('Raw chunk layout changed')
        path = Path(manifest).parent / chunk['file']
        if digest(path) != chunk['sha256']:
            raise ValueError('Raw vector SHA256 mismatch')
        hashes[str(path)] = chunk['sha256']
        data = gzip.decompress(path.read_bytes())
        if data[:6] != b'\x93NUMPY':
            raise ValueError('Raw chunk is not an NPY array')
        version = tuple(data[6:8])
        if version == (1, 0):
            size = struct.unpack('<H', data[8:10])[0]
            start = 10
        elif version in ((2, 0), (3, 0)):
            size = struct.unpack('<I', data[8:12])[0]
            start = 12
        else:
            raise ValueError('Unsupported NPY version')
        header = ast.literal_eval(data[start:start+size].decode('utf-8'))
        if (header['descr'] not in ('<f8', '>f8', '=f8')
                or tuple(header['shape']) != (chunk['count'],)):
            raise ValueError('Unexpected raw NPY dtype or dimensions')
        payload = data[start+size:]
        if len(payload) != 8*chunk['count']:
            raise ValueError('Unexpected raw NPY byte count')
        part = array.array('d')
        if part.itemsize != 8:
            raise ValueError('This platform does not have binary64 doubles')
        part.frombytes(payload)
        order = header['descr'][0]
        if (order == '<' and sys.byteorder != 'little'
                or order == '>' and sys.byteorder != 'big'):
            part.byteswap()
        values.extend(part)
    if len(values) != item['shape'][0]:
        raise ValueError('Incomplete raw vector')
    if not all(math.isfinite(x) for x in values):
        raise ValueError('Non-finite raw vector')
    return values


def recorded_chart_values(reference_t, physical_s, points):
    """The recorded C2 neck-chart formula, for checking index alignment only.

    Standard-library summation can round differently from NumPy's sum.
    This comparison is therefore reported numerically, never bitwise.
    """
    h = [b-a for a, b in zip(reference_t, reference_t[1:])]
    r = [(b-a)/dt for a, b, dt in zip(physical_s, physical_s[1:], h)]
    if min(h) <= 0 or min(r) <= 0:
        raise ValueError('Invalid recorded meridian chart')
    v = [r[0]] + [2/(1/a+1/b) for a, b in zip(r, r[1:])] + [r[-1]]
    ratios = [2*(a+b)/(5*c) for a, b, c in zip(v, v[1:], r)]
    scale = (1+sum((ratio/.95)**64 for ratio in ratios))**(-1/64)
    v = [x*scale for x in v]
    answer = []
    for t in points:
        j = min(max(bisect.bisect_right(reference_t, t)-1, 0), len(h)-1)
        u = (t-reference_t[j])/h[j]
        a, b = v[j:j+2]
        c3, c4, c5 = 10*r[j]-6*a-4*b, -15*r[j]+8*a+7*b, 6*r[j]-3*a-3*b
        answer.append(physical_s[j]+h[j]*(a*u+c3*u**3+c4*u**4+c5*u**5))
    return answer


def make_plan(checkpoint, raw_manifest, target_tolerance, fraction, max_nodes):
    checkpoint, raw_manifest = Path(checkpoint), Path(raw_manifest)
    hashes = {str(checkpoint): digest(checkpoint), str(raw_manifest): digest(raw_manifest)}
    saved, raw = document(checkpoint), document(raw_manifest)
    if (not saved.get('solver_success') or saved.get('audit_pending', True)
            or not raw.get('solver_success') or raw.get('physical_surface') is not False
            or raw.get('raw_collocation_only') is not True):
        raise ValueError('An audited converged design and accepted raw state are required')
    if saved['raw_collocation_checkpoint']['sha256'] != hashes[str(raw_manifest)]:
        raise ValueError('The raw state does not belong to this physical checkpoint')
    if not math.isfinite(target_tolerance) or target_tolerance <= 0 or not 0 < fraction <= 1:
        raise ValueError('A positive tolerance and fraction in (0,1] are required')
    numerical = vector_from_manifest(raw_manifest, 'x', hashes)
    rms = vector_from_manifest(raw_manifest, 'rms', hashes)
    physical = saved['mesh']
    if len(numerical) != len(physical) or len(rms) != len(physical)-1:
        raise ValueError('Raw intervals and saved physical knots do not match')
    if any(b <= a for a, b in zip(physical, physical[1:])):
        raise ValueError('Saved physical mesh is not increasing')
    if any(b <= a for a, b in zip(numerical, numerical[1:])) or min(rms) < 0:
        raise ValueError('Raw mesh/RMS is invalid')
    chart = saved['numerical_meridian_chart']
    if (chart['kind'] != 'C2-all-physical-knots-v1'
            or chart['reference_t'] != raw['identity']['numerical_reference_knots']):
        raise ValueError('Raw and physical chart records differ')
    mapped = recorded_chart_values(chart['reference_t'], chart['physical_s'], numerical)
    alignment = max(abs(a-b) for a, b in zip(mapped, physical))
    if alignment > 2e-12*max(1., saved['meridian_length']):
        raise ValueError('Raw interval indices do not map to saved physical intervals')
    threshold = fraction*target_tolerance
    indices = [j for j, value in enumerate(rms) if value > threshold]
    extra = [(physical[j]+physical[j+1])/2 for j in indices]
    if not all(physical[j] < value < physical[j+1] for j, value in zip(indices, extra)):
        raise ValueError('A physical midpoint collapsed onto an old endpoint')
    merged = sorted(physical+extra)
    if len(merged) > max_nodes:
        raise ValueError('Requested buffered initial mesh exceeds the unchanged node cap')
    old_indices = [bisect.bisect_left(merged, value) for value in physical]
    preserved = all(struct.pack('<d', merged[j]) == struct.pack('<d', value)
                    for j, value in zip(old_indices, physical))
    if not preserved:
        raise ValueError('An old physical knot changed')
    return dict(scope=__doc__,plan_only=True,new_solution=False,
        source_sha256=hashes,physical_checkpoint=str(checkpoint),raw_manifest=str(raw_manifest),
        source_rms_tolerance=raw['identity']['tol'],target_solver_tolerance=target_tolerance,
        buffer_fraction=fraction,selection_threshold=threshold,
        comparison='old accepted interval RMS > fraction * planned target tolerance',
        source_chart_kind=chart['kind'],source_chart_reference_t=chart['reference_t'],
        interval_alignment_check=dict(max_abs_physical_error=alignment,
            summation='standard-library replay of recorded NeckChart formula; not a bitwise comparison'),
        original_physical_nodes=len(physical),selected_intervals=indices,
        selected_old_rms=[rms[j] for j in indices],extra_physical_s=extra,
        extra_nodes=len(extra),total_planned_physical_nodes=len(merged),max_nodes=max_nodes,
        all_old_physical_nodes_preserved_bitwise=preserved,
        old_node_indices_in_merged_mesh=old_indices,
        merged_physical_mesh_sha256=hashlib.sha256(struct.pack('<'+'d'*len(merged),*merged)).hexdigest(),
        old_physical_mesh_sha256=hashlib.sha256(struct.pack('<'+'d'*len(physical),*physical)).hexdigest(),
        metric_design_changed=False,solver_tolerance_changed=False,
        later_integration='Add obj.inverse_chart(extra_physical_s,0.) to the ordinary fixed-restart grid before merge_profile_mesh; retain original pullback.convert(saved,...) for the complete field.',
        limitations=['Saved RMS labels guide a warm mesh and do not predict the new spectral/coordinate residual.',
            'The old normalized t grid and raw cubic are not reused as new-chart data.',
            'A downstream merge may snap points to exact physical breakpoints; report its resulting node count.',
            'The source design can fail the physical metric threshold despite finite solver convergence.'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--raw-manifest',type=Path,required=True)
    parser.add_argument('--target-tol',type=float,required=True)
    parser.add_argument('--fraction',type=float,default=.5)
    parser.add_argument('--max-nodes',type=int,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    own_hash = digest(__file__)
    report = make_plan(args.checkpoint,args.raw_manifest,args.target_tol,args.fraction,args.max_nodes)
    report['source_sha256'][str(Path(__file__))] = own_hash
    report['command'] = sys.argv
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:report[key] for key in ('original_physical_nodes','extra_nodes',
        'total_planned_physical_nodes','selection_threshold','all_old_physical_nodes_preserved_bitwise',
        'interval_alignment_check')}),flush=True)


if __name__ == '__main__':
    main()
