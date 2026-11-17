"""Replace only the original restart's final inlet repair window.

The source method before its final repair is retained verbatim, including its
material-angle pullback, gauge conversion and physical parameter initial guess.
No residual, Jacobian, Newton implementation, core or acceptance gate changes.
"""
import hashlib
import inspect
import json
from pathlib import Path
import textwrap
import numpy as np


OLD = "correction=self.initial(p)-y[:,0];cutoff=(f.Tu if f.direction=='outward'else f.Td)/2;y+=correction[:,None]*np.maximum(0,1-s/cutoff)[None,:]**3"
NEW = """correction=self.initial(p)-y[:,0]
    u=np.clip((s-.5*f.prefix_end)/(.4*f.prefix_end),0.,1.)
    weight=f.profile(s)[0]*(1-u**3*(10-15*u+6*u*u))
    y+=correction[:,None]*weight[None,:]"""


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def install(BVP, record_path):
    original = BVP.restart
    original_text = textwrap.dedent(inspect.getsource(original))
    if original_text.count(OLD) != 1:
        raise RuntimeError('The unique original restart repair source does not match')
    modified_text = original_text.replace(OLD, NEW)
    namespace = dict(original.__globals__)
    namespace.update(inspect.getclosurevars(original).nonlocals)
    compiled = {}
    exec(compile(modified_text, str(Path(__file__).resolve())+'::restart', 'exec'),
         namespace, compiled)
    changed = compiled['restart']
    metadata = dict(
        kind='same-original-material-restart-shared-C2-inlet-window-v1',
        original_restart_source_sha256=digest(original_text),
        changed_restart_source_sha256=digest(modified_text),
        original_final_repair=OLD, changed_final_repair=NEW,
        scope='Only the final additive initial-guess repair window changes. '
            'The entire preceding original restart source is identical. '
            'The window is a(s)*chi(s), with chi=1 through .5*prefix_end '
            'and zero from .9*prefix_end. Its first two inlet derivatives '
            'vanish; this does not itself prove second-jet matching.')
    record_path = Path(record_path)
    def restart(self, path):
        t, y, p = changed(self, path)
        self.initial(p)
        flow = self.flow(p[0])
        report = dict(metadata)
        report.update(source_checkpoint=str(Path(path).resolve()),
            initial_nodes=len(t), initial_parameters=p.tolist(),
            original_control_scales=self.pscale.tolist(),
            initial_physical_controls=(np.asarray(p[1:])*self.pscale).tolist(),
            q_gauge=self.q, actual_q=self.support_amplitude,
            initial_profile=dict(flow.cfg) if hasattr(flow, 'cfg') else
                {**self.cfg, 'delta':self.cfg['delta']+float(p[0])},
            initial_tail_height=(self.bridge.sigma*self.q*y[self.iz:,-1]).tolist(),
            scope='Initial-guess provenance only; no solution or audit acceptance.')
        record_path.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(dict(event='shared_C2_restart_ready',
            nodes=len(t), parameters=p.tolist(), q_gauge=self.q,
            actual_q=self.support_amplitude, record=str(record_path))), flush=True)
        return t, y, p
    BVP.restart = restart
    return metadata
