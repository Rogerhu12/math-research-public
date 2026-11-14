"""Original resumable protocol with explicit frozen binary calibration, bounded storage and GC.

The original client remains untouched and reproducible. These exact recorded
substitutions select a new storage-only worker and expose Node's garbage
collector; they do not edit equations, warm conversion or acceptance.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
template = HERE/'tail_resumable_client.py'
source = template.read_text()
replacements = [
    ("worker = HERE / 'tail_resumable_worker.mjs'",
     "worker = HERE / 'tail_frozen_worker.mjs'"),
    ("['node', str(worker), str(self.config)]",
     "['node', '--expose-gc', str(worker), str(self.config)]"),
]
for before, after in replacements:
    if source.count(before) != 1:
        raise RuntimeError('Compact client template mismatch')
    source = source.replace(before, after)
namespace = dict(__file__=str(template), __name__=__name__+'_original_protocol')
exec(compile(source, str(template), 'exec'), namespace)
Base = namespace['WeightedTailPort']


class WeightedTailPort(Base):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
        except Exception as error:
            proc = getattr(self, 'proc', None)
            before = proc.poll() if proc is not None else None
            if proc is not None:
                self.close()
            after = proc.poll() if proc is not None else None
            prefix = getattr(self, 'record_prefix', None)
            if prefix is not None:
                prefix.with_name(prefix.name+'_initialization.json').write_text(
                    json.dumps(dict(status='failed', error=repr(error),
                        worker_returncode_before_close=before,
                        worker_returncode_after_close=after,
                        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),
                        indent=2)+'\n')
            raise
        frozen = self.ready['storedMetricAdapter'].get('frozenCalibrationAdapter', {})
        checks = frozen.get('profileVerification', [])
        if (frozen.get('name') != 'frozen-binary-calibration-lookup-v1'
                or frozen.get('reusedCalibrationCount') != 160
                or {item.get('kind') for item in checks} != {'rational-head','stored-head'}
                or not all(item.get('exactFingerprintMatch') for item in checks)):
            self.close()
            raise RuntimeError('Frozen binary calibration and full-head fingerprints were not verified')
        compact = self.ready['storedMetricAdapter'].get('compactStorageAdapter', {})
        if (compact.get('name') != 'original-g-smaller-point-cache-and-explicit-gc-v1'
                or compact.get('fingerprintBefore') != compact.get('fingerprintAfter')
                or compact.get('explicitGcAvailable') is not True):
            self.close()
            raise RuntimeError('Compact storage invariants were not verified')
        for name in ('tail_frozen_client.py','tail_frozen_worker.mjs','tail_frozen_geometry.mjs','strong_frozen_calibration_factory.mjs'):
            self.sources[name] = hashlib.sha256((HERE/name).read_bytes()).hexdigest()
