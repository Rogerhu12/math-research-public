"""Persist the original full shooting tangent without changing the tail solve.

The retained exact-raw protocol selects a fresh storage worker. All original
geometry, complete H, residual, Jacobian and audit checks remain. Converged
flow Jacobians are saved as exact binary sidecars and are restored only as
input to the unchanged original full-state tangent warm predictor.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE/'strong_exact_raw_tail_client.py'
ORIGINAL = TEMPLATE.read_text()
EXPECTED = 'ff5f521f4a40522b134710ff0db7eff9a6342637b58b5aaf1080ca370d0bafef'
if hashlib.sha256(ORIGINAL.encode()).hexdigest() != EXPECTED:
    raise ValueError('Retained exact-raw protocol differs')
EDITS = [
    ('AFTER="worker = HERE / \'strong_exact_raw_tail_worker.mjs\'"',
     'AFTER="worker = HERE / \'strong_full_tangent_tail_worker.mjs\'"'),
    ("expected_worker=hashlib.sha256((HERE/'strong_exact_raw_tail_worker.mjs').read_bytes()).hexdigest()",
     "expected_worker=hashlib.sha256((HERE/'strong_full_tangent_tail_worker.mjs').read_bytes()).hexdigest()"),
]
SOURCE = ORIGINAL
for before, after in EDITS:
    if SOURCE.count(before) != 1:
        raise ValueError('Full tangent client anchor is not unique')
    SOURCE = SOURCE.replace(before, after, 1)
NAMESPACE = dict(__file__=str(TEMPLATE), __name__=__name__+'_retained_exact_raw_protocol')
exec(compile(SOURCE, str(TEMPLATE)+':full-tangent-storage-client', 'exec'), NAMESPACE)
Base = NAMESPACE['WeightedTailPort']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def checkpoint_snapshot(config):
    """Resolve an explicitly recorded snapshot, checking its immutable hash."""
    cfg = read(config)
    checkpoint = cfg.get('initialCheckpoint')
    if not checkpoint:
        return None
    packet = Path(checkpoint)
    record = read(packet)
    saved = record.get('response', {}).get('fullFlowTangentSnapshot')
    if saved is None:
        explicit = os.environ.get('VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST')
        if not explicit:
            return None
        source = Path(explicit)
        if not source.is_file():
            raise ValueError('The explicitly requested initial tangent snapshot is missing')
        return dict(path=str(source.resolve()), sha256=sha(source),
                    checkpoint=str(packet), checkpoint_sha256=sha(packet),
                    origin='explicit-manifest-still-bound-to-complete-checkpoint-in-worker')
    source = Path(saved['manifestPath'])
    expected = saved['manifestSha256']
    if not source.is_file():
        source = packet.parent/source.name
    if not source.is_file() or sha(source) != expected:
        raise ValueError('The recorded full-flow tangent manifest is missing or changed')
    return dict(path=str(source.resolve()), sha256=expected,
                checkpoint=str(packet), checkpoint_sha256=sha(packet),
                origin='original-response-snapshot-reference')


class WeightedTailPort(Base):
    def __init__(self, config, source_root, record_prefix, node_heap=384):
        snapshot = checkpoint_snapshot(config)
        updates = {
            'VISIBLE_FLEX_FULL_TANGENT_OUTPUT_PREFIX': str(Path(record_prefix).resolve())+'-full-tangent',
            'VISIBLE_FLEX_FULL_TANGENT_INPUT': snapshot['path'] if snapshot else None,
            'VISIBLE_FLEX_FULL_TANGENT_INPUT_SHA256': snapshot['sha256'] if snapshot else None,
        }
        previous = {key: os.environ.get(key) for key in updates}
        try:
            for key, value in updates.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value
            super().__init__(config, source_root, record_prefix, node_heap=node_heap)
        finally:
            for key, value in previous.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value
        names = (
            'strong_exact_stage_tail_client.py', 'strong_exact_stage_tail_worker.mjs',
            'strong_exact_stage_engine.mjs', 'strong_exact_stage_flow_store.mjs',
            'strong_exact_stage_seed.mjs', 'strong_exact_stage_evaluation_check.mjs',
            'strong_full_tangent_tail_client.py', 'strong_full_tangent_tail_worker.mjs',
            'strong_full_flow_tangent_storage.mjs',
        )
        hashes = {name: sha(HERE/name) for name in names}
        stage = self.ready.get('exactStageCacheAdapter', {})
        expected = {
            'workerSHA256': hashes['strong_full_tangent_tail_worker.mjs'],
            'stageEngineSHA256': hashes['strong_exact_stage_engine.mjs'],
            'seedHelperSHA256': hashes['strong_exact_stage_seed.mjs'],
            'evaluationCheckSHA256': hashes['strong_exact_stage_evaluation_check.mjs'],
        }
        tangent = self.ready.get('fullFlowTangentAdapter', {})
        restored = self.ready.get('fullFlowTangentRestored')
        if (stage.get('name') != 'exact-input-persistent-actual-stage-worker-v1'
                or stage.get('actualVariationalBackend') != 'fourier-root-and-product-moments-v1'
                or any(stage.get(key) != value for key, value in expected.items())
                or len(self.ready.get('exactStageStorage', {}).get('identitySHA', '')) != 64
                or self.ready.get('tailJacobian') != 'fourier-root-and-product-moments-v1'
                or tangent.get('name') != 'original-full-shooting-tangent-storage-worker-v1'
                or tangent.get('workerSHA256') != hashes['strong_full_tangent_tail_worker.mjs']
                or tangent.get('stageTemplateSHA256') != hashes['strong_exact_stage_tail_worker.mjs']
                or tangent.get('storageHelperSHA256') != hashes['strong_full_flow_tangent_storage.mjs']
                or tangent.get('originalPredictorSHA256') != self.sources['78718-tail-tangent-predictor.mjs']
                or bool(snapshot) != bool(restored)
                or (snapshot and not restored.get('originalFactoryCalled'))):
            self.close()
            raise ValueError('Original full-flow tangent/source identity did not verify')
        self.sources.update(hashes)
        provenance = dict(
            scope=__doc__, original_client_sha256=EXPECTED,
            transformed_client_sha256=hashlib.sha256(SOURCE.encode()).hexdigest(),
            source_transform=[dict(before=a, after=b, count=1) for a, b in EDITS],
            source_sha256_at_start=hashes, ready_stage_manifest=stage,
            ready_tangent_manifest=tangent, restored_tangent=restored,
            checkpoint_snapshot=snapshot,
            original_full_H_solve_Jacobian_positivity_and_audit_required=True,
            original_predictor_factory_unchanged=True,
            same_H_exact_raw_branch_still_has_priority=True,
        )
        self.record_prefix.with_name(self.record_prefix.name+'_full-tangent-adapter.json').write_text(
            json.dumps(provenance, indent=2)+'\n')
