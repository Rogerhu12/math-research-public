"""Original frozen true-tail client with strict same-grid raw warm storage.

All original protocol, source, physical identity, Newton and audit gates remain.
The new worker changes only warm restoration and unreachable-storage collection.
"""
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
TEMPLATE=HERE/'tail_frozen_client.py'
ORIGINAL=TEMPLATE.read_text()
EXPECTED='fe14e590f56fc43b1d87eb976377cbd1ec6db1c85ce680c264f18afada687e69'
if hashlib.sha256(ORIGINAL.encode()).hexdigest()!=EXPECTED:
    raise ValueError('Frozen client source changed before exact-raw adaptation')
BEFORE="worker = HERE / 'tail_frozen_worker.mjs'"
AFTER="worker = HERE / 'strong_exact_raw_tail_worker.mjs'"
if ORIGINAL.count(BEFORE)!=1:
    raise ValueError('Exact-raw client worker-selection anchor is not unique')
SOURCE=ORIGINAL.replace(BEFORE,AFTER)
NAMESPACE=dict(__file__=str(TEMPLATE),__name__=__name__+'_original_frozen_protocol')
exec(compile(SOURCE,str(TEMPLATE)+':exact-raw-adapter','exec'),NAMESPACE)
Base=NAMESPACE['WeightedTailPort']

class WeightedTailPort(Base):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        warm=self.ready.get('exactRawWarmAdapter',{})
        expected_worker=hashlib.sha256((HERE/'strong_exact_raw_tail_worker.mjs').read_bytes()).hexdigest()
        expected_helper=hashlib.sha256((HERE/'strong_exact_raw_tail_warm.mjs').read_bytes()).hexdigest()
        if (warm.get('name')!='same-discretization-exact-raw-shooting-warm-v1'
                or warm.get('workerAdapterSHA256')!=expected_worker
                or warm.get('warmHelperSHA256')!=expected_helper
                or self.ready.get('warmEmbedding',{}).get('method')!=warm['name']):
            self.close()
            raise ValueError('The exact-raw worker/source/full-state identity did not verify')
        for name in ('strong_exact_raw_tail_client.py','strong_exact_raw_tail_worker.mjs','strong_exact_raw_tail_warm.mjs'):
            self.sources[name]=hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        provenance=dict(scope=__doc__,template=str(TEMPLATE),template_sha256=EXPECTED,
            transformed_client_sha256=hashlib.sha256(SOURCE.encode()).hexdigest(),
            source_transform=dict(before=BEFORE,after=AFTER,count=1),
            ready_exact_raw_adapter=warm,full_state_warm_diagnostics=self.ready['warmEmbedding'],
            all_original_frozen_storage_and_profile_guards_preserved=True,
            full_original_solve_jacobian_and_audit_required=True)
        self.record_prefix.with_name(self.record_prefix.name+'_exact-raw-adapter.json').write_text(
            json.dumps(provenance,indent=2)+'\n')
