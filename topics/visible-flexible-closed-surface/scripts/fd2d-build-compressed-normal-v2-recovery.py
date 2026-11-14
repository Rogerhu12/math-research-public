#!/usr/bin/env python3
"""Recovery text generator for compact-metadata normal transport v2.

This is newly stored recovery source, not a claim about the still-pending
local exec. It reads the already published frozen v1 helper/reducer, writes
two NEW files, and AST-parses them. It performs no F/J, solve or array sum.
"""
from pathlib import Path
import argparse, hashlib, ast

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--scripts',type=Path,required=True)
    args=ap.parse_args();root=args.scripts
    oldpath=root/'fd2d_gc_compressed_normal_tile.py'
    old=oldpath.read_text()
    if hashlib.sha256(oldpath.read_bytes()).hexdigest()!='0a893bc33f50c13a4899ec4cff18a3c93b3c5035b2f291400a0b777c1fbdb105':
        raise ValueError('Frozen v1 helper differs')
    header=old[:old.index('def save_compressed_normal_tile')]
    header=header.replace("import io\n", "import io\nimport gzip\nimport hashlib\n")
    header=header.replace("SCHEMA='fd2d-compressed-original-local-normal-tile-v1'", "SCHEMA='fd2d-compressed-compact-metadata-local-normal-tile-v2'")
    custom=r'''def pack_existing_raw_checkpoint(raw_manifest,prefix,*,expected_binding):
    """Pack immutable raw checkpoint; change JSON whitespace only."""
    sources=_sources();raw_manifest=Path(raw_manifest).absolute()
    prefix=Path(prefix).absolute()
    if prefix.exists():raise FileExistsError(prefix)
    original_raw=raw_manifest.read_bytes();logical=json.loads(original_raw)
    if (logical.get('schema')!=transport.SCHEMA or logical.get('complete') is not True
            or logical.get('directory_name')!=RAW_BASENAME
            or raw_manifest.parent.name!=RAW_BASENAME):
        raise ValueError('Require complete unchanged original normal-tile checkpoint')
    binding=transport._binding(expected_binding)
    if (transport._binding(logical['binding'])!=binding
            or logical['binding_sha256']!=transport._sha(binding.encode())):
        raise ValueError('Actual normal binding differs')
    compact=(json.dumps(logical,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode()
    if not 0<len(compact)<LIMIT:raise ValueError('Compact metadata still exceeds bound')
    if json.loads(compact)!=logical:raise AssertionError('JSON object changed')
    prefix.parent.mkdir(parents=True,exist_ok=True)
    holder=Path(tempfile.mkdtemp(prefix='.'+prefix.name+'.compact-raw-',dir=prefix.parent))
    pending=Path(tempfile.mkdtemp(prefix='.'+prefix.name+'.compressed-v2-',dir=prefix.parent))
    private=holder/RAW_BASENAME;private.mkdir()
    try:
        for row in logical['pieces']:
            name=capsule_transport.basename(row['file'],'.npz')
            src=raw_manifest.parent/name;dst=private/name
            if not 0<row['bytes']<LIMIT:raise ValueError('Numerical piece too large')
            try:os.link(src,dst)
            except OSError:shutil.copyfile(src,dst)
        capsule_transport.write_bytes(private/'manifest.json',compact)
        raw_identity=capsule_transport.stream_identity(private/'manifest.json')
        inner=capsule_transport.create_normal_capsule(private/'manifest.json',pending/'payload',
            expected_manifest_sha256=raw_identity['sha256'])
        index=json.loads(inner.read_text())
        before=pending/'manifest-before-compaction.json.gz'
        with before.open('wb') as stream:
            with gzip.GzipFile(filename='',mode='wb',fileobj=stream,mtime=0) as out:out.write(original_raw)
        if before.stat().st_size>=LIMIT:raise ValueError('Compressed provenance too large')
        if gzip.decompress(before.read_bytes())!=original_raw:raise AssertionError('Provenance gzip changed')
        report=dict(schema=SCHEMA,complete=True,directory_name=prefix.name,sources=sources,
            payload_index=dict(file='payload/index.json',**capsule_transport.stream_identity(inner)),
            logical_manifest=dict(file='payload/original-manifest.json',**raw_identity),
            logical_normal_schema=transport.SCHEMA,
            logical_loader='fd2d_gc_normal_checkpoint.load_normal_checkpoint',
            logical_directory_name=RAW_BASENAME,
            binding_sha256=index['original_binding_sha256'],mapping_sha256=index['original_mapping_sha256'],
            metadata_sha256=index['original_metadata_sha256'],logical_piece_count=index['piece_count'],
            logical_numerical_bytes=index['original_numerical_bytes'],
            compressed_numerical_bytes=index['compressed_numerical_bytes'],
            largest_compressed_piece_bytes=index['largest_compressed_piece_bytes'],
            metadata_compaction=dict(operation='JSON whitespace/key serialization only; parsed object identical',
                before=dict(bytes=len(original_raw),sha256=hashlib.sha256(original_raw).hexdigest()),
                after=raw_identity,original_gzip=dict(file=before.name,**capsule_transport.stream_identity(before)),
                original_raw_directory_unmodified=True,component_piece_rows_and_hashes_unchanged=True,
                typed_metadata_mapping_binding_unchanged=True),
            original_manifest_and_pieces_lossless=True,
            original_manifest_recoverable_from_provenance_gzip=True,
            logical_manifest_is_compact_equivalent_JSON=True,
            raw_temporary_directory_removed_after_success=True,
            offline_piece_result='Verified original NPZ bytes, strictly below 1,000,000 bytes',
            numerical_operations_performed=False,mathematical_or_finite_objective_change=False)
        raw=(json.dumps(report,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
        if len(raw)>=LIMIT:raise ValueError('Outer manifest too large')
        capsule_transport.write_bytes(pending/'manifest.json',raw)
        transport._fsync_directory(pending)
        if prefix.exists():raise FileExistsError(prefix)
        os.rename(pending,prefix);transport._fsync_directory(prefix.parent)
    except BaseException as error:
        shutil.rmtree(pending,ignore_errors=True)
        raise RuntimeError('Original raw untouched; private compact data retained at '+str(holder)) from error
    shutil.rmtree(holder)
    return prefix/'manifest.json'


def save_compressed_normal_tile(normal,prefix,*,binding):
    """Original normal saver followed by explicit v2 format-only pack."""
    prefix=Path(prefix).absolute()
    if prefix.exists():raise FileExistsError(prefix)
    prefix.parent.mkdir(parents=True,exist_ok=True)
    holder=Path(tempfile.mkdtemp(prefix='.'+prefix.name+'.raw-v2-',dir=prefix.parent))
    try:
        manifest=transport.save_normal_checkpoint(normal,holder/RAW_BASENAME,binding=binding)
        result=pack_existing_raw_checkpoint(manifest,prefix,expected_binding=binding)
    except BaseException as error:
        raise RuntimeError('Helper-owned raw retained at '+str(holder)) from error
    shutil.rmtree(holder)
    return result


def _verify_metadata_compaction(path,outer,logical):
    row=outer['metadata_compaction'];packed=row['original_gzip']
    if packed.get('file')!='manifest-before-compaction.json.gz':raise ValueError('Wrong provenance path')
    original_path=path.parent/packed['file']
    if capsule_transport.stream_identity(original_path)!={k:packed[k] for k in ('bytes','sha256')}:
        raise ValueError('Provenance gzip changed')
    original=gzip.decompress(original_path.read_bytes())
    if dict(bytes=len(original),sha256=hashlib.sha256(original).hexdigest())!=row['before']:
        raise ValueError('Original metadata bytes changed')
    if json.loads(original)!=logical:raise ValueError('Parsed original and compact metadata differ')
    if row['after']!={k:outer['logical_manifest'][k] for k in ('bytes','sha256')}:
        raise ValueError('Compact metadata identity differs')


'''
    tail=old[old.index('def _read(capsule):'):]
    tail=tail.replace('    return path,outer,index,logical\n','    _verify_metadata_compaction(path,outer,logical)\n    return path,outer,index,logical\n')
    new=header+custom+tail
    p=root/'fd2d_gc_compressed_normal_tile_v2.py'
    if p.exists():raise FileExistsError(p)
    ast.parse(new);p.write_text(new)
    helper_sha=hashlib.sha256(p.read_bytes()).hexdigest()
    prior=root/'fd2d-gc-compressed-piecewise-normal-reduce.py'
    if hashlib.sha256(prior.read_bytes()).hexdigest()!='5416025f947fc02a7fafb84291b9a4272ba7839717618a20e491ea2c92579021':
        raise ValueError('Frozen v1 compressed reducer differs')
    reducer=prior.read_text()
    start=reducer.index('# The read-only capsule functions')
    end=reducer.index('def logical_manifest(path):',start)
    section=reducer[start:end]
    section=section.replace("import fd2d_gc_normal_capsule as capsule_transport", "import fd2d_gc_normal_capsule as capsule_transport\nimport gzip")
    section=section.replace("SCHEMA='fd2d-compressed-original-local-normal-tile-v1'", "SCHEMA='fd2d-compressed-compact-metadata-local-normal-tile-v2'")
    section=section.replace("FROZEN_COMPRESSED_HELPER_SHA256='0a893bc33f50c13a4899ec4cff18a3c93b3c5035b2f291400a0b777c1fbdb105'", f"FROZEN_COMPRESSED_HELPER_SHA256='{helper_sha}'")
    section=section.replace("'fd2d_gc_compressed_normal_tile.py'", "'fd2d_gc_compressed_normal_tile_v2.py'")
    va=new.index('def _verify_metadata_compaction');vb=new.index('def _read(capsule):',va)
    section=section.replace('def _read(capsule):',new[va:vb]+'def _read(capsule):')
    section=section.replace('    return path,outer,index,logical\n','    _verify_metadata_compaction(path,outer,logical)\n    return path,outer,index,logical\n')
    newer=reducer[:start]+section+reducer[end:]
    compat=r'''def _old_compressed_reader():
    import importlib.util
    path=Path(__file__).with_name('fd2d-gc-compressed-piecewise-normal-reduce.py')
    if source(path)['sha256']!='5416025f947fc02a7fafb84291b9a4272ba7839717618a20e491ea2c92579021':
        raise ValueError('Closed v1 reader changed')
    spec=importlib.util.spec_from_file_location('fd2d_closed_compressed_reduce_v1',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


'''
    newer=newer.replace('def logical_manifest(path):',compat+'def logical_manifest(path):')
    newer=newer.replace("    if header.get('schema')==SCHEMA:\n        return read_logical_manifest(path)", "    if header.get('schema')==SCHEMA:\n        return read_logical_manifest(path)\n    if header.get('schema')=='fd2d-compressed-original-local-normal-tile-v1':\n        return _old_compressed_reader().logical_manifest(path)")
    newer=newer.replace("    if header.get('schema')==SCHEMA:return read_logical_piece(path,row)", "    if header.get('schema')==SCHEMA:return read_logical_piece(path,row)\n    if header.get('schema')=='fd2d-compressed-original-local-normal-tile-v1':\n        return _old_compressed_reader().logical_piece(path,row)")
    rp=root/'fd2d-gc-compressed-piecewise-normal-reduce-v2.py'
    if rp.exists():raise FileExistsError(rp)
    ast.parse(newer);rp.write_text(newer)
    for f in (p,rp):print(f.name,f.stat().st_size,hashlib.sha256(f.read_bytes()).hexdigest())

if __name__=='__main__':main()
