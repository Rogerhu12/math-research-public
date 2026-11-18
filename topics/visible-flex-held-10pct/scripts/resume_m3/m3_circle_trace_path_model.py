"""Build distinct fixed-lambda M8 models, preserving the original .06 gauge.

The final old frozen physical profile and chart are copied unchanged. Each
model has its own Flow/BVP classes and immutable core factory; no lift/core
cache is shared across lambda. q(lambda) is the defining support amplitude,
while the numerical gauge, seven pscales, and warp reference remain .06.
This module does not seed, reproject, solve or integrate a mean height.
"""
import copy
import numpy as np
from m3_raw_diagnostic_model import RawDiagnosticEnvironment
from circle_trace_homotopy_core import make_core_factory
from synchronous_core_lift import install_synchronous_lift


class CircleTracePathEnvironment:
    def __init__(self, bound, native_reference, base_settings):
        self.bound=bound
        self.native=native_reference
        self.original_cosine=type(native_reference.core)
        self.settings=copy.deepcopy(base_settings)
        self.chart=copy.deepcopy(bound.record['chart'])
        # This installs the existing source/profile/Fourier-Jac modules. Its
        # generic raw classes are not instantiated or used as a path model.
        self.environment=RawDiagnosticEnvironment(bound.source_topic,bound.short_bridge,
                                                  self.chart,self.settings)
        self.coupler=self.environment.coupler

    def make(self, homotopy, primary_q):
        from plateau_core import PlateauSupportCore
        cp=self.bound.record
        settings={**self.settings,'homotopy':float(homotopy)}
        factory,description=make_core_factory(PlateauSupportCore,self.original_cosine,settings)
        __import__('fixed_metric_mode3_core').PlanarSupportCore=factory
        __import__('fixed_metric_mode3_bvp').PlanarSupportCore=factory
        # The original from-import inside build_classes captures this fixed
        # factory. Later model constructions cannot change an existing model.
        Flow,Base=self.coupler.adaptive.build_classes(copy.deepcopy(self.chart))
        Lift=install_synchronous_lift(Flow,Base,float(homotopy),window=(.5,.9))
        class BVP(self.coupler.TailMixin,Lift):
            def initial(self,p):
                result=super().initial(p)
                # Preserve the path's 1e-5 floor also on its literal legacy
                # branch, without changing the legacy core constructor itself.
                if not self._core.rho_lower>1e-5:
                    raise FloatingPointError('The path keeps its original rho>1e-5 floor')
                return result
        port=copy.deepcopy(self.native.flow.port_data)
        port['_sha256']=cp['physical_port_sha256']
        obj=BVP(copy.deepcopy(cp['frozen_profile']),port,.06,8,cp['config']['angular'],False,.06)
        oldscales=np.asarray(cp['central_correction_scales'],float)
        if obj.pscale.tobytes()!=oldscales.tobytes():
            raise ValueError('The original seven .06-gauge pscales changed')
        if obj._core_key is not None or obj._core is not None:
            raise ValueError('Set the independent support seed before the first core evaluation')
        obj.seed_support_amplitude=float(primary_q)
        obj.bcweights=np.full(8,cp['config']['physical_bc_tol']/cp['config']['bc_tol'])
        obj.path_definition=dict(**description,settings=settings,numerical_gauge=.06,
            defining_support_amplitude=float(primary_q),warp_reference=.06,
            fixed_metric=False,p0_scope='Only delta; frozen_profile already contains the old historical p0.',
            parameter_scales=obj.pscale.tolist(),
            mean_height_scope='Use the original height_integral on this actual model/solution. No old mean trajectory is copied to a positive-lambda model.')
        return obj
