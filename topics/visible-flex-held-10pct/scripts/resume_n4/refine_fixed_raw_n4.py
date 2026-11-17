#!/usr/bin/env python3
"""Freeze a raw n4 checkpoint's complete metric and refine its nested core/map.

Eta remains fixed. Unknowns are log(q/q_gauge), free c8/q_gauge, c12/q_gauge,
... . The frozen J low start and every raw compact column are independent
of M. Releasing c8 is explicit; it is not described as the design c8=0 rule.
"""
import hashlib
from pathlib import Path
import types
from tight_moment_interval_bounds import install,PROVENANCE as INTERVAL_PROVENANCE
install()
from raw_fixed_core import make_core_class,provenance

SOURCE=Path(__file__).with_name('refine_fixed_large_radius.py')
text=SOURCE.read_text()
begin="    J=rec.get('core_projection_order',M0)if lam>0 else None"
end="    par=np.r_[np.log(qnew/q0),c/q0]"
first=text.index(begin);last=text.index(end,first)+len(end)
replacement='''    if 'raw_control_anchor_modes' not in rec:
        raise ValueError('A declared raw n4 checkpoint is required')
    J=int(rec['raw_control_anchor_modes'])
    if M0<J or M<J:raise ValueError('The frozen raw anchor cannot be discarded')
    Core=RAW_CORE(ReferenceCore,J)
    oldcore=Core(oldq,oldc,4,arc_nodes=1024,**settings)
    c=np.zeros(M-1);c[:len(oldc)]=oldc;qnew=oldq
    embedding=dict(method='Exact zero-padding of all raw controls with frozen original J and an explicitly free c8 column',
                   raw_control_anchor_modes=J,old_c8=float(oldc[0]),initial_new_c8=float(c[0]))
    par=np.r_[np.log(qnew/q0),c/q0]'''
text=text[:first]+replacement+text[last:]
transforms=[
    ("core_transform=dict(source_sha256=SOURCE_SHA256,replacements=TRANSFORMS),",
     'core_transform=RAW_PROVENANCE(J),coefficient_certificate=INTERVAL_PROVENANCE,'),
    ("core_kind='n4_fixed_local_circle'","core_kind='n4_fixed_raw_mean_circle'"),
    ('fixed_metric=True,\n                solver_success=',
     'fixed_metric=True,raw_control_anchor_modes=J,raw_control_provenance=RAW_PROVENANCE(J),\n                solver_success='),
    ('install();started=time.monotonic()',
     "install();from trace_domain_newton import install as observe_newton\n        observe_newton(a.out.with_name(a.out.name+'-newton.jsonl'));started=time.monotonic()")]
for before,after in transforms:
    if text.count(before)!=1:raise RuntimeError('Raw fixed driver transformation mismatch: '+before)
    text=text.replace(before,after)
module=types.ModuleType('refine_fixed_raw_n4_literal');module.__file__=str(SOURCE)
module.__dict__.update(RAW_CORE=make_core_class,RAW_PROVENANCE=provenance,
                       INTERVAL_PROVENANCE=INTERVAL_PROVENANCE)
exec(compile(text,str(SOURCE),'exec'),module.__dict__)
build_seed=module.build_seed

if __name__=='__main__':
    module.main()
