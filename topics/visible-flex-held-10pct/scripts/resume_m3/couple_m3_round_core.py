#!/usr/bin/env python3
"""Install an exact local circular core into the original m3 actual coupler.

Only the primary rho/core controls and the exact reference lift change.
The original physical Frenet equations, nonlinear tail, boundary tests and
2e-9 tail gate are retained.  Homotopy lambda is a physical design change;
only lambda=1 has an exact circular arc.  The finite unknown is a correction
to the unprojected integral core lift, never a Fourier surrogate for that arc.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from couple_m3_smallcut_secant import accepted_anchor


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);sys.modules[name]=value
    spec.loader.exec_module(value);return value


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(add_help=False,allow_abbrev=False)
    parser.add_argument('--source-topic',type=Path,required=True)
    parser.add_argument('--short-bridge',type=Path,required=True)
    parser.add_argument('--homotopy',type=float,required=True)
    parser.add_argument('--round-halfwidth',type=float,default=.21)
    parser.add_argument('--round-transition',type=float,default=.08)
    parser.add_argument('--control-transition',type=float,default=.16)
    parser.add_argument('--reference-check-only',action='store_true')
    a,rest=parser.parse_known_args()
    if '--fixed' in rest or '--preserve-restart-mesh' in rest:
        raise ValueError('This runner changes the physical core; fixed-g refinement is a separate task')
    if not 0<=a.homotopy<=1:raise ValueError('lambda must lie in [0,1]')
    source=a.source_topic.resolve();lib=Path(__file__).with_name('round_core_lib')
    sys.path.insert(0,str(lib))
    from plateau_core import PlateauSupportCore
    from fixed_large_radius_core import make_core_class
    from tight_moment_interval_bounds import install as install_moments
    install_moments();GeneralCore=make_core_class(PlateauSupportCore)
    class Core(GeneralCore):
        def summary(self):
            value=super().summary()
            value['control_family']='C4 complementary controls, all support harmonics free'
            value['first_free_support_frequency']=2*self.base_mode
            value['primary_support_moment_locked']=True
            return value
    settings=dict(halfwidth=a.round_halfwidth,transition=a.round_transition,
                  control_transition=a.control_transition,homotopy=a.homotopy,
                  center=math.pi/3,bimodal_eta=0.,lock_fundamental=True,
                  coefficient_precision=80,positivity_grid_max=32768)
    restart=Path(rest[rest.index('--restart')+1])
    rec=json.load(gzip.open(restart,'rt'));accepted_anchor(rec,restart)
    if rec['config']['base_mode']!=3:raise ValueError('Expected actual m3 prefix')
    if rec.get('core_round_settings'):
        for k in ('halfwidth','transition','control_transition','center','bimodal_eta','lock_fundamental'):
            if rec['core_round_settings'].get(k)!=settings[k]:
                raise ValueError('Round continuation changes another core control: '+k)
    out=Path(rest[rest.index('--out-prefix')+1]);out.parent.mkdir(parents=True,exist_ok=True)
    record=dict(scope=__doc__,settings=settings,command=sys.argv,
                input=str(restart.resolve()),input_sha256=sha(restart),
                source_hashes={str(p.resolve()):sha(p) for p in [Path(__file__),a.short_bridge,
                  source/'scripts/db6f-prefix-coupled.py',source/'scripts/950f-prefix-adaptive-chart-bvp-v2.py',
                  source/'scripts/db6f-prefix-flat-profile.py',source/'scripts/78718-prefix-fourier-jacobian.py',
                  *sorted(lib.glob('*.py'))]},
                restart_scope='Original material-coordinate correction coefficients are initial guesses under the new exact lift; no identity of old and new full embeddings is asserted.')
    record_path=out.with_name(out.name+'-round-record.json')
    def save():record_path.write_text(json.dumps(record,indent=2)+'\n')
    save()
    c=module('m3_round_original_coupler',source/'scripts/db6f-prefix-coupled.py')
    flat=module('m3_round_original_flat',source/'scripts/db6f-prefix-flat-profile.py');flat.install(c.adaptive)
    short=module('m3_round_original_short',a.short_bridge)
    original_install=c.adaptive.old.install_source
    def install(root):
        original_install(root);short.install()
        coremod=__import__('fixed_metric_mode3_core')
        OriginalCore=coremod.PlanarSupportCore
        if a.reference_check_only:
            q=rec['actual_primary_amplitude']
            coeff=np.asarray(rec['parameters'][1:])*np.asarray(rec['central_correction_scales'])
            new=Core(q,coeff,3,arc_nodes=1024,**{**settings,'homotopy':0.})
            old=OriginalCore(q,coeff,3);u=np.linspace(.001,2*np.pi-.002,513)
            ng,og=new.evaluate(u),old.evaluate(u)
            checks={k:float(np.max(abs(ng[k]-og[k]))) for k in ('F','Ft','Ftt','kappa')}
            checks['parameter_F']=float(np.max(abs(new.parameter_derivatives(u)-old.parameter_derivatives(u))))
            checks['fundamental_leakage_linf']=float(np.max(abs(new.basis.fundamental_leakage)))
            checks['rho_lower']=new.rho_lower
            record['lambda_zero_reference_comparison']=checks;save()
            print(json.dumps(dict(event='lambda_zero_reference',**checks)),flush=True)
            return
        coremod.PlanarSupportCore=lambda q,corrections=(),base_mode=3:Core(q,corrections,base_mode,arc_nodes=1024,**settings)
        cpmod=__import__('curve_stable_prefix_bvp')
        original_save=cpmod.save_checkpoint
        def save_round(path,obj):
            obj['core_round_settings']=dict(settings)
            obj['core_round_sources']=record['source_hashes']
            obj['config']['core_kind']='exact_m3_local_circle_integral_lift'
            obj['config']['exact_core_lift']=True
            obj['config']['exact_circle_core']=settings['homotopy']==1.
            return original_save(path,obj)
        cpmod.save_checkpoint=save_round
    c.adaptive.old.install_source=install
    if a.reference_check_only:
        install(source/'repro/source-root');return
    backend=module('m3_round_fourier_jacobian',source/'scripts/78718-prefix-fourier-jacobian.py');backend.install(c.adaptive)
    base_build=c.adaptive.build_classes
    def build(chart):
        Flow,BVP=base_build(chart)
        from exact_core_lift import install_core_lift
        from analytic_adaptive_core_jac import install as install_parameter_jac
        BVP=install_core_lift(Flow,BVP)
        install_parameter_jac(BVP)
        return Flow,BVP
    c.adaptive.build_classes=build
    sys.argv=[sys.argv[0],'--source-root',str(source/'repro/source-root')]+rest
    began=time.monotonic()
    try:
        c.main();record['wrapper_returned']=True
    finally:
        record['seconds']=time.monotonic()-began;save()


if __name__=='__main__':main()
