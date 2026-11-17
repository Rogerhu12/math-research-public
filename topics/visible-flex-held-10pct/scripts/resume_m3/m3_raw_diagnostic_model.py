"""Read-only reconstruction of the original m3 raw integral source objects.

No production acceptance gate is bypassed: callers must label diagnostic failed
states as failed.  The factory is local to a fresh Python process; no source
file or active solver is edited.  Core settings may be changed between object
constructions, while already built immutable cores remain attached to their
original flows.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


class RawDiagnosticEnvironment:
    def __init__(self, source_topic, short_bridge, chart, settings):
        self.source = Path(source_topic).resolve()
        self.short_bridge = Path(short_bridge).resolve()
        self.library = Path(__file__).with_name('round_raw_lib')
        sys.path.insert(0, str(self.library))
        from plateau_core import PlateauSupportCore
        from fixed_large_radius_core import make_core_class
        from tight_moment_interval_bounds import install as install_moments
        install_moments()
        Core = make_core_class(PlateauSupportCore)
        self.settings = dict(settings)
        scripts = self.source / 'scripts'
        self.coupler = module('diagnostic_m3_actual_coupler', scripts/'db6f-prefix-coupled.py')
        c = self.coupler
        module('diagnostic_m3_flat', scripts/'db6f-prefix-flat-profile.py').install(c.adaptive)
        c.adaptive.old.install_source(self.source/'repro/source-root')
        module('diagnostic_m3_short', self.short_bridge).install()
        factory = lambda q, corrections=(), base_mode=3: Core(
            q, corrections, base_mode, arc_nodes=1024, **self.settings)
        core_module = __import__('fixed_metric_mode3_core')
        core_module.PlanarSupportCore = factory
        if 'fixed_metric_mode3_bvp' in sys.modules:
            sys.modules['fixed_metric_mode3_bvp'].PlanarSupportCore = factory
        module('diagnostic_m3_fourier_jac', scripts/'78718-prefix-fourier-jacobian.py').install(c.adaptive)
        Flow, Base = c.adaptive.build_classes(chart)
        from exact_core_lift import install_core_lift
        from analytic_adaptive_core_jac import install as install_parameter_jac
        Lift = install_core_lift(Flow, Base, window=(.5, .9))
        install_parameter_jac(Lift)
        class BVP(c.TailMixin, Lift):
            pass
        self.Flow, self.BVP = Flow, BVP
        self.sources = {str(path): sha(path) for path in [
            Path(__file__).resolve(), self.short_bridge,
            scripts/'db6f-prefix-coupled.py',
            scripts/'950f-prefix-adaptive-chart-bvp-v2.py',
            scripts/'db6f-prefix-flat-profile.py',
            scripts/'78718-prefix-fourier-jacobian.py',
            *sorted(self.library.glob('*.py'))]}

    def activate(self, settings):
        self.settings.clear()
        self.settings.update(settings)

    def make(self, settings, profile, port, q_gauge, modes, angular,
             fixed, warp_reference):
        self.activate(settings)
        return self.BVP(profile, port, q_gauge, modes, angular, fixed, warp_reference)

