#!/usr/bin/env python3
"""Copy four original cardinal rows per tail node, with source-byte hashes.

This is a lossless byte extractor. It performs no Fourier transform, floating
jet reconstruction, root solve or ODE calculation. Exact geometric arithmetic
belongs to the separate public-Actions consumer. Every original node is read
and its compressed and raw hashes are verified before any byte is retained.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct
import time


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if data[:2] == b'\x1f\x8b' else data)


def exact_binary(value):
    numerator, denominator = float(value).as_integer_ratio()
    return f'{numerator}/{denominator}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--complete',type=Path,required=True)
    parser.add_argument('--plan',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--sigma',type=int,choices=(-1,1),default=-1)
    args = parser.parse_args()
    start = time.monotonic()
    complete_bytes, plan_bytes = args.complete.read_bytes(), args.plan.read_bytes()
    complete, plan = read(args.complete),read(args.plan)
    if not complete.get('finished') or complete.get('completedNodes') != len(complete['rows']):
        raise ValueError('Finished complete readout with every declared node required')
    if plan['inputs']['complete']['sha256'] != digest(complete_bytes):
        raise ValueError('The closed plan is not bound to this exact complete manifest')
    count, angular = len(complete['rows']),int(complete['angular'])
    if count < 2 or angular%4:
        raise ValueError('At least two radial nodes and four cardinal angular rows required')
    if args.out.exists():
        raise FileExistsError('Refusing to overwrite an extracted packet directory')
    packed = bytearray()
    rows = []
    # Preserve the source orientation: outer to inner. The consumer reverses
    # the node order once, before constructing exact shared-node jets.
    for index,row in enumerate(complete['rows']):
        if row['shape'] != [angular,12]:
            raise ValueError('Unexpected original node shape')
        source = args.complete.parent/row['file']
        encoded = source.read_bytes()
        raw = gzip.decompress(encoded)
        if digest(encoded)!=row['sha256'] or digest(raw)!=row['rawSha256']:
            raise ValueError('Original source-byte hash mismatch at node '+str(index))
        if len(raw)!=angular*12*8:
            raise ValueError('Unexpected original node byte count')
        retained = b''.join(raw[(angular*j//4)*96:(angular*j//4+1)*96] for j in range(4))
        packed.extend(retained)
        rows.append(dict(source_node=row['node'],source_file=row['file'],
            source_compressed_sha256=row['sha256'],source_raw_sha256=row['rawSha256'],
            four_cardinal_rows_sha256=digest(retained),
            radius=exact_binary(row['geometry']['r']),
            original_stage=row.get('originalStage'),raw_cell=row.get('rawCell'),
            raw_segment=row.get('rawSegment')))
        if (index+1)%2048==0:
            print(json.dumps(dict(event='cardinal_byte_extraction',copied=index+1,total=count)),flush=True)
    encoded = gzip.compress(packed,compresslevel=9,mtime=0)
    if len(encoded)>=5_000_000:
        raise ValueError('Compressed four-angle packet exceeds the per-file bound')
    args.out.mkdir(parents=True)
    data_path = args.out/'cardinal-node-rows.f64le.gz'
    data_path.write_bytes(encoded)
    index_raw = (json.dumps(rows,separators=(',',':'))+'\n').encode()
    index_encoded = gzip.compress(index_raw,compresslevel=9,mtime=0)
    index_path = args.out/'source-node-index.json.gz'
    index_path.write_bytes(index_encoded)
    result = dict(schema='original-tail-four-cardinal-byte-packet-v1',finished=True,
        extractor_sha256=digest(Path(__file__).read_bytes()),
        original_complete=dict(file=str(args.complete),bytes=len(complete_bytes),sha256=digest(complete_bytes)),
        original_plan=dict(file=str(args.plan),bytes=len(plan_bytes),sha256=digest(plan_bytes)),
        original_input_sha256=complete.get('input_sha256'),
        original_profile_fingerprint=complete.get('original_profile_fingerprint'),
        refinement_binding=complete.get('refinement_binding'),
        plan_inputs=plan['inputs'],
        definition=dict(cuff=exact_binary(plan['cuff']),inner=exact_binary(plan['tail_inner']),
            cut=exact_binary(plan['cut']),patch_width=exact_binary(plan['cut_correction_width']),
            sigma=args.sigma,source_orientation='outer-to-inner',
            source_angles=angular,retained_angles=['0','pi/2','pi','3*pi/2'],
            shape=[count,4,12],dtype='little-endian float64, original bytes unchanged',
            retained_columns='All twelve original columns retained; consumer uses perturbation position 0:3, radial first 3:6 and height radial second column 9.'),
        data=dict(file=data_path.name,bytes=len(encoded),sha256=digest(encoded),raw_bytes=len(packed),raw_sha256=digest(packed)),
        source_node_index=dict(file=index_path.name,bytes=len(index_encoded),sha256=digest(index_encoded),raw_sha256=digest(index_raw)),
        verified_original_nodes=count,
        extraction_only=True,new_numerical_solution=False,
        scope='Lossless four-angle rows from existing full readout. No numerical nonplanarity assertion is made by this extractor.',
        seconds=time.monotonic()-start)
    (args.out/'manifest.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),nodes=count,packet_bytes=len(encoded),index_bytes=len(index_encoded),seconds=result['seconds'])),flush=True)


if __name__=='__main__':
    main()
