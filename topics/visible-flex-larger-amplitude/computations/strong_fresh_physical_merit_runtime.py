"""Fixed positive-coordinate merit for a fresh original actual continuation.

The exact cost and Newton-installation methods are inherited from the reviewed
fixed-S implementation. This runtime does not restore or replace any affine
anchor: the original outer method obtains the new warm H, K and full J from
the explicitly audited packet and checks every subsequently changed H.
"""
from __future__ import annotations
import atexit
import gzip
import hashlib
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
EXPECTED_PRIOR = 'e330336daab09ef9d0bcb93cb36e04581636e33e645ed5e319987c3cc0f2810f'
if hashlib.sha256((HERE/'strong_physical_merit_and_affine_resume.py').read_bytes()).hexdigest() != EXPECTED_PRIOR:
    raise ValueError('The reviewed fixed-coordinate cost implementation changed')
from strong_physical_merit_and_affine_resume import Runtime as PriorRuntime


class Runtime(PriorRuntime):
    def __init__(self, configuration, out):
        import numpy as np
        self.np, self.configuration, self.out = np, dict(configuration), Path(out)
        self.started, self.closed, self.disk = time.monotonic(), False, None
        self.M, self.q = int(configuration['modes']), float(configuration['gauge'])
        self.weights = np.asarray(configuration['fixed_parameter_weights'], dtype=float)
        if (self.weights.shape != (self.M+3,) or not np.isfinite(self.weights).all()
                or not (self.weights > 0).all()):
            raise ValueError('Require the fixed complete strictly positive parameter weights')
        self.weights.setflags(write=False)
        names = ('strong_fresh_physical_merit_runtime.py', 'strong_fresh_physical_merit_actual_bvp.py',
            'strong_domain_rejection_observer.py', 'strong_physical_merit_and_affine_resume.py',
            'root_domain_newton.py', 'root_actual_neck_bvp.py')
        self.hashes = {str(HERE/name):hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names}
        self.stats = dict(merit_evaluations=0)
        self.transform_records = {}
        self._newton_installed = False
        atexit.register(self.finish)

    def install_affine_on_class(self, cls):
        raise ValueError('Fresh continuation must keep the original complete outer method')

    def restore_anchor(self, *args, **kwargs):
        raise ValueError('This runtime does not restore a pending affine anchor')

    def write_record(self):
        record = dict(scope=__doc__, configuration=self.configuration,
            source_sha256_at_start=self.hashes, stats=dict(self.stats),
            runtime_source_transforms=self.transform_records,
            reused_cost_implementation_sha256=EXPECTED_PRIOR,
            original_Newton_merit_changed=True, original_linear_system_unchanged=True,
            original_outer_coupling_method_unmodified=True,
            no_pending_affine_anchor_restoration=True,
            original_RMS_BC_full_H_Jacobian_and_final_audit_gates_unchanged=True,
            seconds=time.monotonic()-self.started, no_new_solution_implied=True)
        path=self.out.with_name(self.out.name+'-fresh-physical-merit-adapter.json')
        temporary=path.with_name(path.name+'.tmp')
        temporary.write_text(json.dumps(record,indent=2)+'\n');temporary.replace(path)
        return record

    def finish(self):
        if self.closed:
            return
        record=self.write_record()
        for path in (self.out.with_suffix('.json.gz'),self.out.with_name(self.out.name+'-summary.json')):
            if not path.is_file():
                continue
            value=path.read_bytes()
            data=json.loads(gzip.decompress(value) if path.suffix=='.gz' else value)
            data['fresh_fixed_physical_merit']=record
            value=(json.dumps(data,indent=2)+'\n').encode()
            if path.suffix=='.gz': value=gzip.compress(value,mtime=0)
            if len(value)>=5_000_000:
                raise ValueError('Final explicit merit metadata exceeds the file-size rule')
            temporary=path.with_name(path.name+'.fresh-merit.tmp')
            temporary.write_bytes(value);temporary.replace(path)
        self.closed=True
