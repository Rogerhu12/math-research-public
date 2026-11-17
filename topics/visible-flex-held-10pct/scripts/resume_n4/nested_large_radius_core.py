"""One fixed positive-homotopy projection on nested local-circle spaces."""
from functools import lru_cache
import types
from nested_projection_core import NestedProjectionBasis,embed_compact_coefficients
import fixed_large_radius_core as fixed

def make_core_class(ReferencePlateauCore,projection_order):
    mod=types.ModuleType('nested_large_radius_literal');mod.__file__=str(fixed.SOURCE)
    exec(compile(fixed.text,str(fixed.SOURCE),'exec'),mod.__dict__)
    mod.ComplementaryMomentBasis=lru_cache(maxsize=32)(lambda **kwargs:NestedProjectionBasis(projection_order=projection_order,**kwargs))
    Base=mod.make_core_class(ReferencePlateauCore)
    class NestedCore(Base):
        def __init__(self,*args,**kwargs):
            if not 0<kwargs.get('homotopy',1.)<=1:raise ValueError('Positive lambda required by frozen projection family')
            super().__init__(*args,**kwargs)
        def summary(self):
            out=super().summary();out.update(control_projection_order=projection_order,control_family='Nested local circle controls under one frozen projection')
            return out
    return NestedCore
