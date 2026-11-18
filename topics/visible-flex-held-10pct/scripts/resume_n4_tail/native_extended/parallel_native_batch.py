#!/usr/bin/env python3
"""Run unchanged independent native stages concurrently and restore wire order.

No floating-point payload is decoded/re-encoded or numerically evaluated here.
Each original stage body and every numeric configuration byte are copied to
one unchanged original CLI. Only the number of stages and opaque identity
change in the child headers. The parent identity/order are restored on merge.
For valid batches, the first domain failure in original stage order is kept.
Malformed wire/child process failures remain engineering errors, never DN
acceptance. Timing is per actual invocation, not promised byte-identical.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import time


def digest(data):
    return hashlib.sha256(data).hexdigest()


def reference(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=digest(path.read_bytes()), bytes=path.stat().st_size)


def split_wire(data):
    if len(data) < 140 or data[:8] != b'VFN4LD01':
        raise ValueError('Malformed original batch header')
    abi, modes, angular, spacing, nq, root_iterations, halves, count, jac = struct.unpack_from('<9i', data, 8)
    if not (abi == 1 and 1 <= modes <= 64 and 0 < nq <= 1048576 and halves == 20 and
            0 < count <= 1048576 and jac in (0, 1)):
        raise ValueError('Invalid original batch dimensions')
    end = 140 + 8*(halves + nq*(2*modes+1))
    if end > len(data):
        raise ValueError('Truncated original common coefficients')
    header = data[:end]
    spans = []
    for stage in range(count):
        start = end
        if end+8 > len(data):
            raise ValueError('Truncated original stage header')
        steps, points = struct.unpack_from('<2i', data, end)
        if not (0 < steps <= 1048576 and 0 < points <= 1048576):
            raise ValueError('Invalid original stage dimensions')
        end += 8 + 8*(2*modes+2 + points*(modes+12)) + 36*steps
        if end > len(data):
            raise ValueError('Truncated original stage body')
        spans.append((start, end))
    if end != len(data):
        raise ValueError('Unexpected original trailing bytes')
    return dict(abi=abi, modes=modes, count=count, jac=jac,
                header=header, token=data[44:108], spans=spans)


def output_records(data, shape, child_count, token, returncode):
    expected = b'VFN4OUT1' + struct.pack('<4i', shape['abi'], shape['modes'], child_count, shape['jac']) + token
    if data[:88] != expected:
        raise ValueError('Child output header/identity changed')
    width = 8*(2*shape['modes']+2)*(1+shape['jac']*2*shape['modes']) + 64
    records, pos, failed = [], 88, None
    for local in range(child_count):
        start = pos
        if pos+8 > len(data):
            raise ValueError('Truncated child stage status')
        index, status = struct.unpack_from('<2i', data, pos)
        pos += 8
        if index != local:
            raise ValueError('Child local stage order changed')
        if status:
            if pos+4 > len(data):
                raise ValueError('Truncated child domain error length')
            length, = struct.unpack_from('<I', data, pos)
            pos += 4+length
            if pos > len(data):
                raise ValueError('Truncated child domain error')
            failed = local
        else:
            pos += width
            if pos > len(data):
                raise ValueError('Truncated child state/Jacobian/diagnostics')
        records.append((start, pos, status))
        if status:
            break
    if pos != len(data) or returncode != (3 if failed is not None else 0):
        raise ValueError('Child exit/status/payload extent mismatch')
    return records, failed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--plan', type=Path,
                        default=os.environ.get('VISIBLE_FLEX_PARALLEL_NATIVE_PLAN'))
    args = parser.parse_args()
    if args.plan is None:
        parser.error('Supply --plan or VISIBLE_FLEX_PARALLEL_NATIVE_PLAN')
    plan = json.loads(args.plan.read_text())
    native = Path(plan['native_cli']['path']).resolve()
    if digest(native.read_bytes()) != plan['native_cli']['sha256']:
        raise ValueError('The original native CLI identity changed')
    workers = plan['workers']
    if type(workers) is not int or not 1 <= workers <= 32:
        raise ValueError('Invalid declared worker count')
    src, dst = args.input.resolve(), args.output.resolve()
    directory = Path(str(dst)+'.parallel-work')
    metadata = Path(str(dst)+'.parallel.json')
    if dst.exists() or directory.exists() or metadata.exists():
        raise FileExistsError('Use a fresh original output path')
    wire = src.read_bytes()
    shape = split_wire(wire)
    workers = min(workers, shape['count'])
    directory.mkdir(parents=True)
    begun = time.monotonic()
    result = dict(scope=__doc__, started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source=reference(__file__), plan=reference(args.plan), native_cli=reference(native),
        original_input=reference(src), stages=shape['count'], modes=shape['modes'],
        with_jacobian=bool(shape['jac']), workers=workers,
        layout='global_stage = local_stage * workers + child_index',
        child_token='SHA256(child header with64 zero ASCII identity bytes + literal stage bodies)',
        numeric_stage_bytes_copied_exactly=True, records=[], success=False)
    children = []
    try:
        for child in range(workers):
            indices = range(child, shape['count'], workers)
            header = bytearray(shape['header'])
            struct.pack_into('<i', header, 36, len(indices))
            header[44:108] = b'0'*64
            body = b''.join(wire[a:b] for a, b in (shape['spans'][j] for j in indices))
            token = digest(header+body).encode('ascii')
            header[44:108] = token
            inp, out = directory/f'child-{child:02d}-input.bin', directory/f'child-{child:02d}-output.bin'
            inp.write_bytes(header+body)
            stdout, stderr = directory/f'child-{child:02d}-stdout.txt', directory/f'child-{child:02d}-stderr.txt'
            with stdout.open('xb') as so, stderr.open('xb') as se:
                proc = subprocess.Popen([str(native), str(inp), str(out)], stdout=so, stderr=se)
            children.append(dict(child=child, count=len(indices), token=token,
                inp=inp, out=out, stdout=stdout, stderr=stderr, process=proc))
        print(json.dumps(dict(event='original_native_parallel_started', workers=workers,
                              stages=shape['count'], input_sha256=digest(wire))), flush=True)
        failures, outputs = [], []
        for item in children:
            rc = item['process'].wait()
            item['returncode'] = rc
            row = dict(child=item['child'], stages=item['count'], command=item['process'].args,
                       returncode=rc, input=reference(item['inp']),
                       stdout=reference(item['stdout']), stderr=reference(item['stderr']))
            if item['out'].exists():
                row['output'] = reference(item['out'])
            result['records'].append(row)
            if rc not in (0, 3):
                raise RuntimeError('Unchanged child CLI engineering exit: '+str(rc))
            data = item['out'].read_bytes()
            blocks, failed = output_records(data, shape, item['count'], item['token'], rc)
            outputs.append((data, blocks))
            if failed is not None:
                failures.append(failed*workers+item['child'])
        first = min(failures) if failures else None
        stop = shape['count'] if first is None else first+1
        parent_header = b'VFN4OUT1'+struct.pack('<4i', shape['abi'],shape['modes'],shape['count'],shape['jac'])+shape['token']
        with dst.open('xb') as stream:
            stream.write(parent_header)
            for global_stage in range(stop):
                child, local = global_stage % workers, global_stage // workers
                data, blocks = outputs[child]
                start, end, status = blocks[local]
                stream.write(struct.pack('<i',global_stage))
                stream.write(data[start+4:end])
                if status:
                    length, = struct.unpack_from('<I',data,start+8)
                    message = data[start+12:start+12+length].decode('utf8',errors='replace')
                    print('stage '+str(global_stage)+': '+message,file=sys.stderr,flush=True)
        result.update(success=first is None, parent_returncode=0 if first is None else 3,
            earliest_original_stage_failure=first, complete_output=reference(dst))
    except BaseException as error:
        result.update(engineering_error=repr(error), parent_returncode=2)
        print(repr(error), file=sys.stderr, flush=True)
    finally:
        for item in children:
            process = item['process']
            if process.poll() is None:
                process.terminate()
                process.wait()
        result['elapsed_seconds'] = time.monotonic()-begun
        result['ended_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        metadata.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(event='original_native_parallel_terminal',
                              metadata=str(metadata),success=result['success'],
                              returncode=result['parent_returncode'],elapsed_seconds=result['elapsed_seconds'])),flush=True)
        if result['success'] and not plan.get('retain_shards',False):
            shutil.rmtree(directory)
    return result['parent_returncode']


if __name__ == '__main__':
    sys.exit(main())
