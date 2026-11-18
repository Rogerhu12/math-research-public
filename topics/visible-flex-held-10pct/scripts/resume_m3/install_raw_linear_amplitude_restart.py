"""A raw-control amplitude predictor, retaining the shared C2 inlet repair.

This installer is for a new physical-amplitude design.  It changes only the
initial guess: every physical raw support coefficient receives the same factor
q_target / q_old_actual.  Raw compact columns are independent physical controls;
there is no assumed q**j hierarchy.  Fixed-g restarts have ratio=1 and are not
the intended use.  No residual, Jacobian, core definition or solver gate changes.
"""
import hashlib
import inspect
import json
from pathlib import Path
import textwrap
import numpy as np

from install_endpoint_c2_restart import OLD as OLD_REPAIR, NEW as C2_REPAIR


OLD_CONTROL = "rec['parameters'][j]*rec['central_correction_scales'][j-1]*ratio**(j+1)/self.pscale[j-1]"
LINEAR_CONTROL = "rec['parameters'][j]*rec['central_correction_scales'][j-1]*ratio/self.pscale[j-1]"


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def install(BVP, record_path):
    """Install on an owned class before any other restart installer is applied."""
    original = BVP.restart
    original_text = textwrap.dedent(inspect.getsource(original))
    if original_text.count(OLD_CONTROL) != 1 or original_text.count(OLD_REPAIR) != 1:
        raise RuntimeError('The unique original adaptive restart source does not match')
    c2_text = original_text.replace(OLD_REPAIR, C2_REPAIR)
    modified_text = c2_text.replace(OLD_CONTROL, LINEAR_CONTROL)
    namespace = dict(original.__globals__)
    namespace.update(inspect.getclosurevars(original).nonlocals)
    compiled = {}
    exec(compile(modified_text, str(Path(__file__).resolve())+'::restart', 'exec'),
         namespace, compiled)
    changed = compiled['restart']
    metadata = dict(
        kind='raw-physical-controls-linear-amplitude-shared-C2-restart-v1',
        original_restart_source_sha256=digest(original_text),
        c2_restart_source_sha256=digest(c2_text),
        changed_restart_source_sha256=digest(modified_text),
        old_control_expression=OLD_CONTROL,
        new_control_expression=LINEAR_CONTROL,
        shared_C2_repair_expression=C2_REPAIR,
        scope='Compared with the existing shared-C2 restart, only the initial '
            'physical-control amplitude factor changes from ratio**(j+1) to ratio. '
            'Original material-angle pullback, gauge conversion, mesh, delta '
            'initialization, field predictor and C2 window remain. This is neither '
            'a solved state nor a fixed-metric refinement.')
    record_path = Path(record_path)

    def restart(self, path):
        t, y, p = changed(self, path)
        self.initial(p)
        flow = self.flow(p[0])
        from curve_stable_prefix_bvp import load_checkpoint
        previous = load_checkpoint(path)
        ratio = 1. if self.fixed else self.q/previous['actual_primary_amplitude']
        report = dict(metadata)
        report.update(
            source_checkpoint=str(Path(path).resolve()),
            source_checkpoint_sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest(),
            initial_nodes=len(t), initial_parameters=p.tolist(),
            original_control_scales=self.pscale.tolist(),
            initial_physical_controls=(np.asarray(p[1:])*self.pscale).tolist(),
            q_gauge=self.q, actual_q=self.support_amplitude,
            previous_actual_q=previous['actual_primary_amplitude'],
            physical_amplitude_ratio=ratio,
            initial_profile=dict(flow.cfg) if hasattr(flow, 'cfg') else
                {**self.cfg, 'delta':self.cfg['delta']+float(p[0])},
            initial_tail_height=(self.bridge.sigma*self.q*y[self.iz:,-1]).tolist(),
            scope='Initial-guess provenance only; all acceptance remains with the original solver.')
        record_path.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(dict(event='raw_linear_amplitude_restart_ready',
            nodes=len(t), q_gauge=self.q, actual_q=self.support_amplitude,
            physical_amplitude_ratio=ratio, record=str(record_path))), flush=True)
        return t, y, p

    BVP.restart = restart
    return metadata
