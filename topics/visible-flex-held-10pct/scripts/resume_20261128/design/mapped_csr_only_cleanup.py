"""Remove only an explicitly owned store after the actual child has returned.

This is called by the original controller immediately after its invoke/wait
returns, never by a timer or a PID guess. Small owner and cleanup records
remain. Mathematical fields, checkpoints, source, matrix-check evidence and
any other caller directory are outside this function's deletion scope.
"""
import hashlib
import json
from pathlib import Path
import shutil


def cleanup_joined_child(outdir, returncode, *, child_return_observed, entry_sha256):
    if child_return_observed is not True or not isinstance(returncode, int):
        raise ValueError('An actual joined child terminal is required for scratch cleanup')
    outdir = Path(outdir).resolve()
    directory = outdir/'mapped-factor-storage'
    if not directory.exists():
        return dict(child_returncode=returncode, store_created=False, removed=[])
    if directory.is_symlink() or directory.resolve().parent != outdir:
        raise ValueError('The complete-CSR-and-factor store is not the owned child directory')
    owner_path = directory/'owner.json'
    if owner_path.is_symlink() or not owner_path.is_file():
        raise ValueError('The actual child ownership record must be an ordinary local file')
    owner = json.loads(owner_path.read_text())
    if (owner.get('kind') != 'owned_complete_CSR_only_before_QR_scratch_storage'
            or Path(owner['actual_child_outdir']).resolve() != outdir
            or owner['entry_sha256'] != entry_sha256):
        raise ValueError('The exact actual child store ownership is not established')
    removed = []
    for path in sorted(directory.iterdir()):
        if path.name == 'owner.json':
            continue
        if path.is_symlink() or not path.is_dir() or not path.name.startswith('complete-qr-'):
            raise ValueError('Unexpected content in the uniquely owned factor store')
        files = list(path.iterdir())
        if any(file.is_symlink() or not file.is_file() or file.name not in ('all-arrays.bin','layout.json')
               for file in files):
            raise ValueError('Unexpected file in the temporary complete-CSR-and-factor backing directory')
        record = dict(directory=str(path), files=[dict(path=str(file), bytes=file.stat().st_size,
            allocated_disk_bytes=file.stat().st_blocks*512) for file in files])
        if (path/'layout.json').exists():
            record['layout_sha256'] = hashlib.sha256((path/'layout.json').read_bytes()).hexdigest()
        # No original field or accepted result lives in this unique directory.
        shutil.rmtree(path)
        record['removed_after_actual_child_terminal'] = True
        removed.append(record)
    result = dict(scope=__doc__, child_returncode=returncode,
        actual_child_terminal_observed=True, owner=str(owner_path),
        owner_sha256=hashlib.sha256(owner_path.read_bytes()).hexdigest(),
        store_created=True, removed=removed,
        original_fields_checkpoints_or_verification_evidence_removed=False)
    (outdir/'joined-child-mapped-storage-cleanup.json').write_text(
        json.dumps(result, indent=2, allow_nan=False)+'\n')
    return result
