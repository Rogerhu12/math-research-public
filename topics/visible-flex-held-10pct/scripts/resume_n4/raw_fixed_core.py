"""Fixed-J raw circle core with the original full c8 parameter jets released."""
import hashlib
from pathlib import Path
import types
from fixed_large_radius_core import TRANSFORMS as FREE_TRANSFORMS
from second_order_large_radius_core import text as GUARDED_SOURCE,PROVENANCE as GUARD_PROVENANCE


def make_core_class(reference,anchor_modes):
    text=GUARDED_SOURCE
    transforms=[('from complementary_moment_basis import ComplementaryMomentBasis',
                 'from raw_n4_free_complementary import make_free_raw_basis\nComplementaryMomentBasis=make_free_raw_basis(RAW_ANCHOR_MODES)')]+FREE_TRANSFORMS
    for before,after in transforms:
        if text.count(before)!=1:raise RuntimeError('Raw fixed core transformation mismatch: '+before)
        text=text.replace(before,after)
    source=Path(__file__).with_name('large_radius_local_core.py')
    module=types.ModuleType('raw_fixed_core_literal');module.__file__=str(source)
    module.__dict__['RAW_ANCHOR_MODES']=int(anchor_modes)
    exec(compile(text,str(source),'exec'),module.__dict__)
    Core=module.make_core_class(reference);original=Core.summary
    def summary(self):
        out=original(self)
        out.update(control_family='Raw C4 mean-zero controls with independent free c8 at fixed metric',
                   control_homotopy='Frozen original canonical J start to raw compact endpoint; higher moments may vary',
                   control_projection_order=int(anchor_modes),raw_control_anchor_modes=int(anchor_modes),
                   raw_control_path='raw-mean-free-c8-with-frozen-canonical-low-start-v1')
        return out
    Core.summary=summary
    return Core


def provenance(anchor_modes):
    root=Path(__file__).parent
    return dict(scope=__doc__,anchor_modes=int(anchor_modes),guard=GUARD_PROVENANCE,
                free_parameter_transform=FREE_TRANSFORMS,
                source_sha256={name:hashlib.sha256((root/name).read_bytes()).hexdigest()for name in
                               ('raw_fixed_core.py','raw_n4_free_complementary.py','raw_n4_complementary.py',
                                'large_radius_local_core.py','second_order_large_radius_core.py')})
