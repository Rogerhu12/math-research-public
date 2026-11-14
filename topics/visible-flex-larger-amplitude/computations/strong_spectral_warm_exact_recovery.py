#!/usr/bin/env python3
"""Recover derived M28-to-M32 raw warm chunks from accepted raw arrays.

This storage-only recipe does not run a provider, a tail, an ODE or a BVP.
The new modes are exact positive zero.  It never creates an accepted solution.
Original gzip headers and trailers are retained so reconstruction checks the
entire original compressed byte strings, as well as all float64 values.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import zlib
import numpy as np


def sha(data):
    return hashlib.sha256(data).hexdigest()


def document(path):
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def write_new(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise FileExistsError(str(path))
    else:
        with path.open('xb') as f:
            f.write(data)


def json_bytes(value):
    return (json.dumps(value, indent=2, allow_nan=False)+'\n').encode()


def load_arrays(path):
    record = document(path)
    arrays = {}
    for name, item in record['arrays'].items():
        flat = np.empty(int(np.prod(item['shape'])), dtype=np.float64)
        cursor = 0
        for part in item['chunks']:
            if Path(part['file']).name != part['file'] or part['first'] != cursor:
                raise ValueError('Invalid raw chunk order or path')
            data = (path.parent/part['file']).read_bytes()
            if sha(data) != part['sha256']:
                raise ValueError('Raw chunk SHA mismatch')
            block = np.load(io.BytesIO(gzip.decompress(data)), allow_pickle=False)
            if block.dtype != np.float64 or block.shape != (part['count'],):
                raise ValueError('Original raw float64 layout differs')
            flat[cursor:cursor+len(block)] = block
            cursor += len(block)
        if cursor != len(flat):
            raise ValueError('Incomplete original raw array')
        arrays[name] = flat.reshape(item['shape'])
    return record, arrays


def embedded(source, target, arrays):
    if (source['identity']['modes'] != 28 or target['identity']['modes'] != 32
            or not source['solver_success'] or target['solver_success']
            or source['physical_surface'] or target['physical_surface']
            or not target['provenance'].get('spectral_warm_only')):
        raise ValueError('Expected accepted M28 raw and explicitly unsolved M32 warm')
    if arrays['y'].shape[0] != 85 or arrays['p'].shape != (28,):
        raise ValueError('Only the complete fixed-view 28-mode raw layout is allowed')
    mapping = np.r_[0, 1+np.arange(28), 33+np.arange(28), 65+np.arange(28)]
    out = {name: value.copy() for name, value in arrays.items()}
    out['y'] = np.zeros((97, arrays['y'].shape[1]), dtype=np.float64)
    out['y'][mapping] = arrays['y']
    out['cubic'] = np.zeros((*arrays['cubic'].shape[:-1], 97), dtype=np.float64)
    out['cubic'][..., mapping] = arrays['cubic']
    out['p'] = np.zeros(32, dtype=np.float64)
    out['p'][:28] = arrays['p']
    if (out['y'][mapping].tobytes() != arrays['y'].tobytes()
            or out['cubic'][..., mapping].tobytes() != arrays['cubic'].tobytes()
            or out['p'][:28].tobytes() != arrays['p'].tobytes()):
        raise ValueError('A retained physical mode changed bits')
    for name, array in out.items():
        if list(array.shape) != target['arrays'][name]['shape']:
            raise ValueError('Target array shape differs')
    return out, mapping.tolist()


def split_gzip(data):
    if data[:3] != b'\x1f\x8b\x08' or data[3] & ~8:
        raise ValueError('Only the actual original filename-only gzip header is supported')
    end = 10
    if data[3] & 8:
        end = data.index(b'\0', end)+1
    return data[:end], data[end:-8], data[-8:]


def exact_chunk(array, item):
    stream = io.BytesIO()
    np.save(stream, array.ravel()[item['first']:item['first']+item['count']], allow_pickle=False)
    compressor = zlib.compressobj(level=6, wbits=-15)
    body = compressor.compress(stream.getvalue())+compressor.flush()
    result = bytes.fromhex(item['gzip_header_hex'])+body+bytes.fromhex(item['gzip_trailer_hex'])
    if sha(body) != item['deflate_sha256'] or sha(result) != item['sha256']:
        raise ValueError('Reconstructed original gzip bytes differ; no substitute accepted')
    recovered = np.load(io.BytesIO(gzip.decompress(result)), allow_pickle=False)
    original = array.ravel()[item['first']:item['first']+item['count']]
    if recovered.tobytes() != original.tobytes():
        raise ValueError('Exact gzip roundtrip changed float64 bits')
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='mode', required=True)
    create = sub.add_parser('create')
    create.add_argument('--source-raw', type=Path, required=True)
    create.add_argument('--target-raw', type=Path, required=True)
    create.add_argument('--out', type=Path, required=True)
    replay = sub.add_parser('recover')
    replay.add_argument('--recipe', type=Path, required=True)
    replay.add_argument('--source-directory', type=Path, required=True)
    replay.add_argument('--target-directory', type=Path, required=True)
    replay.add_argument('--out-directory', type=Path, required=True)
    replay.add_argument('--report', type=Path, required=True)
    args = p.parse_args()
    if args.mode == 'create':
        source, arrays = load_arrays(args.source_raw)
        target, target_arrays = load_arrays(args.target_raw)
        out, mapping = embedded(source, target, arrays)
        if any(out[name].tobytes() != target_arrays[name].tobytes() for name in out):
            raise ValueError('Actual preflight raw was not this exact spectral embedding')
        chunks = []
        for name, item in target['arrays'].items():
            for original in item['chunks']:
                data = (args.target_raw.parent/original['file']).read_bytes()
                header, body, trailer = split_gzip(data)
                chunk = dict(array=name, **original, bytes=len(data), gzip_header_hex=header.hex(),
                             gzip_trailer_hex=trailer.hex(), deflate_sha256=sha(body))
                if exact_chunk(out[name], chunk) != data:
                    raise ValueError('Compression replay differs from original')
                chunks.append(chunk)
        result = dict(scope=__doc__, source_raw=dict(file=args.source_raw.name, sha256=sha(args.source_raw.read_bytes())),
            target_raw=dict(file=args.target_raw.name, sha256=sha(args.target_raw.read_bytes())),
            source_modes=28, target_modes=32, row_mapping=mapping, new_modes_exact_positive_zero=True,
            target_solver_success=False, all_actual_array_bits_verified=True,
            all_original_compressed_chunk_bytes_verified=True, chunks=chunks,
            numpy_version=np.__version__, zlib_version=zlib.ZLIB_VERSION,
            source_sha256=sha(Path(__file__).read_bytes()))
        write_new(args.out, json_bytes(result))
        print(json.dumps(dict(event='spectral_warm_exact_recipe_created', chunks=len(chunks),
            original_compressed_bytes=sum(x['bytes'] for x in chunks), recipe=str(args.out))))
    else:
        recipe = document(args.recipe)
        if recipe['source_sha256'] != sha(Path(__file__).read_bytes()):
            raise ValueError('Recovery source SHA differs')
        source_path = args.source_directory/recipe['source_raw']['file']
        target_path = args.target_directory/recipe['target_raw']['file']
        if (sha(source_path.read_bytes()) != recipe['source_raw']['sha256']
                or sha(target_path.read_bytes()) != recipe['target_raw']['sha256']):
            raise ValueError('Original or derived manifest SHA differs')
        source, arrays = load_arrays(source_path)
        target = document(target_path)
        out, mapping = embedded(source, target, arrays)
        if mapping != recipe['row_mapping']:
            raise ValueError('Frozen embedding map differs')
        for chunk in recipe['chunks']:
            write_new(args.out_directory/chunk['file'], exact_chunk(out[chunk['array']], chunk))
        write_new(args.out_directory/target_path.name, target_path.read_bytes())
        _, restored = load_arrays(args.out_directory/target_path.name)
        if any(out[name].tobytes() != restored[name].tobytes() for name in out):
            raise ValueError('Full recovered raw readback differs')
        result = dict(scope=__doc__, recipe_sha256=sha(args.recipe.read_bytes()),
            recovered_chunks=len(recipe['chunks']), all_complete_array_bits_equal=True,
            all_original_compressed_chunk_bytes_equal=True, numerical_solution_accepted=False,
            no_provider_ODE_tail_or_BVP_called=True)
        write_new(args.report, json_bytes(result))
        print(json.dumps(result))


if __name__ == '__main__':
    main()
