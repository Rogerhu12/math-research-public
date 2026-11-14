"""Original exact-raw protocol with explicit complete-input stage persistence.

The worker records the actual Fourier-root engine choice in the complete cache
identity. The old full-H, final Jacobian and audit protocol is unchanged. Source
fingerprints explicitly include this adapter; a different client cannot silently
reuse its packets. The diagnostic request is separate from solve().
"""
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
TEMPLATE=HERE/'strong_exact_raw_tail_client.py'
ORIGINAL=TEMPLATE.read_text()
EXPECTED='ff5f521f4a40522b134710ff0db7eff9a6342637b58b5aaf1080ca370d0bafef'
if hashlib.sha256(ORIGINAL.encode()).hexdigest()!=EXPECTED:
    raise ValueError('Original exact-raw client source differs')
EDITS=[
    ('AFTER="worker = HERE / \'strong_exact_raw_tail_worker.mjs\'"',
     'AFTER="worker = HERE / \'strong_exact_stage_tail_worker.mjs\'"'),
    ("expected_worker=hashlib.sha256((HERE/'strong_exact_raw_tail_worker.mjs').read_bytes()).hexdigest()",
     "expected_worker=hashlib.sha256((HERE/'strong_exact_stage_tail_worker.mjs').read_bytes()).hexdigest()")]
SOURCE=ORIGINAL
for before,after in EDITS:
    if SOURCE.count(before)!=1:
        raise ValueError('Exact-stage client source anchor is not unique')
    SOURCE=SOURCE.replace(before,after,1)
NAMESPACE=dict(__file__=str(TEMPLATE),__name__=__name__+'_retained_exact_raw_protocol')
exec(compile(SOURCE,str(TEMPLATE)+':exact-stage-client','exec'),NAMESPACE)
Base=NAMESPACE['WeightedTailPort']


class WeightedTailPort(Base):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        names=('strong_exact_stage_tail_client.py','strong_exact_stage_tail_worker.mjs',
            'strong_exact_stage_engine.mjs','strong_exact_stage_flow_store.mjs',
            'strong_exact_stage_seed.mjs','strong_exact_stage_evaluation_check.mjs')
        hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names}
        manifest=self.ready.get('exactStageCacheAdapter',{})
        expected={'workerSHA256':hashes['strong_exact_stage_tail_worker.mjs'],
            'stageEngineSHA256':hashes['strong_exact_stage_engine.mjs'],
            'seedHelperSHA256':hashes['strong_exact_stage_seed.mjs'],
            'evaluationCheckSHA256':hashes['strong_exact_stage_evaluation_check.mjs']}
        storage=self.ready.get('exactStageStorage',{})
        if (manifest.get('name')!='exact-input-persistent-actual-stage-worker-v1'
                or manifest.get('actualVariationalBackend')!='fourier-root-and-product-moments-v1'
                or any(manifest.get(k)!=v for k,v in expected.items())
                or len(storage.get('identitySHA',''))!=64
                or self.ready.get('tailJacobian')!='fourier-root-and-product-moments-v1'):
            self.close()
            raise ValueError('Complete exact-stage worker/backend identity did not verify')
        self.sources.update(hashes)
        provenance=dict(scope=__doc__,original_client_sha256=EXPECTED,
            transformed_client_sha256=hashlib.sha256(SOURCE.encode()).hexdigest(),
            source_transform=[dict(before=a,after=b,count=1) for a,b in EDITS],
            source_sha256_at_start=hashes,ready_stage_manifest=manifest,
            initial_cache_identity_and_statistics=storage,
            every_changed_H_still_requires_original_true_solve_and_full_audit=True,
            cached_local_maps_are_identified_prior_computations=True)
        self.record_prefix.with_name(self.record_prefix.name+'_exact-stage-adapter.json').write_text(
            json.dumps(provenance,indent=2)+'\n')
