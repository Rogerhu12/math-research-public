"""Original resumable protocol with explicit compact storage and GC.

The original client remains untouched and reproducible. These exact recorded
substitutions select a new storage-only worker and expose Node's garbage
collector; they do not edit equations, warm conversion or acceptance.
"""
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
template = HERE/'tail_resumable_client.py'
source = template.read_text()
replacements = [
    ("worker = HERE / 'tail_resumable_worker.mjs'",
     "worker = HERE / 'tail_compact_worker.mjs'"),
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
        super().__init__(*args, **kwargs)
        compact = self.ready['storedMetricAdapter'].get('compactStorageAdapter', {})
        if (compact.get('name') != 'original-g-smaller-point-cache-and-explicit-gc-v1'
                or compact.get('fingerprintBefore') != compact.get('fingerprintAfter')
                or compact.get('explicitGcAvailable') is not True):
            self.close()
            raise RuntimeError('Compact storage invariants were not verified')
        for name in ('tail_compact_client.py','tail_compact_worker.mjs','tail_compact_geometry.mjs'):
            self.sources[name] = hashlib.sha256((HERE/name).read_bytes()).hexdigest()
