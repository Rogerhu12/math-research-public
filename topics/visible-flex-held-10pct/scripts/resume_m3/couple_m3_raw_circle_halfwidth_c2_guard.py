#!/usr/bin/env python3
"""A new exact-circle halfwidth design with the same C2 seed and rho allowance.

This derives the original actual raw coupler without changing its equations,
analytic parameter jets, exact reference lift, tail gate, or acceptance tests.
This owned entry explicitly permits a changed protected halfwidth and transition
widths from an accepted raw checkpoint; symmetry and original equations stay fixed.
The complete new core is a physical design, not a fixed-metric refinement.
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
    parser.add_argument('--round-halfwidth',type=float,default=.01)
    parser.add_argument('--round-transition',type=float,default=.08)
    parser.add_argument('--control-transition',type=float,default=.16)
    parser.add_argument('--reference-check-only',action='store_true')
    a,rest=parser.parse_known_args()
    if '--fixed' in rest or '--preserve-restart-mesh' in rest:
        raise ValueError('This runner changes the physical core; fixed-g refinement is a separate task')
    if a.homotopy != 1.:raise ValueError('This explicit endpoint entry requires lambda=1')
    if not 0<a.round_halfwidth<=.21:raise ValueError('This design continuation uses 0<a<=.21')
    source=a.source_topic.resolve();lib=Path(__file__).with_name('round_raw_lib')
    sys.path.insert(0,str(lib))
    from plateau_core import PlateauSupportCore
    from raw_second_order_core import make_core_class, PROVENANCE as rho_guard_provenance
    from tight_moment_interval_bounds import install as install_moments
    install_moments();GeneralCore=make_core_class(PlateauSupportCore)
    class Core(GeneralCore):
        def summary(self):
            value=super().summary()
            value['control_family']='C4 complementary controls, all support harmonics free'
            value['first_free_support_frequency']=2*self.base_mode
            value['primary_support_moment_locked']=True
            value['control_path']='raw-mean-primary-compact-v1'
            return value
    settings=dict(halfwidth=a.round_halfwidth,transition=a.round_transition,
                  control_transition=a.control_transition,homotopy=a.homotopy,
                  center=math.pi/3,bimodal_eta=0.,lock_fundamental=True,
                  coefficient_precision=80,positivity_grid_max=32768)
    restart=Path(rest[rest.index('--restart')+1])
    rec=json.load(gzip.open(restart,'rt'));accepted_anchor(rec,restart)
    if rec['config']['base_mode']!=3:raise ValueError('Expected actual m3 prefix')
    if not rec.get('core_round_settings') or rec.get('core_control_path')!='raw-mean-primary-compact-v1':
        raise ValueError('This endpoint requires an accepted actual raw-path state')
    for k in ('center','bimodal_eta','lock_fundamental'):
        if rec['core_round_settings'].get(k)!=settings[k]:
            raise ValueError('The endpoint changes a protected core setting: '+k)
    design_changes={k:dict(before=rec['core_round_settings'].get(k),after=settings[k])
                    for k in ('homotopy','halfwidth','transition','control_transition')
                    if rec['core_round_settings'].get(k)!=settings[k]}
    out=Path(rest[rest.index('--out-prefix')+1]);out.parent.mkdir(parents=True,exist_ok=True)
    record=dict(scope=__doc__,settings=settings,command=sys.argv,
                explicit_endpoint_design=True,physical_design_changes=design_changes,
                halfwidth_design_scope='A changed exact-circle halfwidth is a new physical core design; only the final a=.21 can use the existing target geometry window.',
                parent_entry_sha256=sha(Path(__file__).with_name('couple_m3_raw_circle_endpoint_c2_guard.py')),
                numerical_rho_guard=rho_guard_provenance,
                base_raw_runner_sha256=sha(Path(__file__).with_name('couple_m3_round_core_raw.py')),
                control_path='raw-mean-primary-compact-v1',
                low_moment_scope='Control support mean and primary moments remain zero; other control moments may change with the endpoint widths and lambda.',
                input=str(restart.resolve()),input_sha256=sha(restart),
                source_hashes={str(p.resolve()):sha(p) for p in [Path(__file__),a.short_bridge,
                  source/'scripts/db6f-prefix-coupled.py',source/'scripts/950f-prefix-adaptive-chart-bvp-v2.py',
                  source/'scripts/db6f-prefix-flat-profile.py',source/'scripts/78718-prefix-fourier-jacobian.py',
                  Path(__file__).with_name('install_endpoint_c2_restart.py'),
                  Path(__file__).with_name('couple_m3_raw_circle_endpoint.py'),
                  Path(__file__).with_name('couple_m3_raw_circle_endpoint_c2_seed.py'),
                  Path(__file__).with_name('raw_second_order_core.py'),
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
            obj['core_control_path']='raw-mean-primary-compact-v1'
            obj['core_numerical_positivity_guard']='triangle-first-plus-C2-grid-v1'
            obj['core_round_sources']=record['source_hashes']
            obj['config']['core_kind']='exact_m3_raw_local_circle_integral_lift'
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
        from install_endpoint_c2_restart import install as install_c2_restart
        record['restart_initializer']=install_c2_restart(BVP, out.with_name(out.name+'-c2-restart-record.json'))
        save()
        return Flow,BVP
    c.adaptive.build_classes=build
    sys.argv=[sys.argv[0],'--source-root',str(source/'repro/source-root')]+rest
    began=time.monotonic()
    try:
        c.main();record['wrapper_returned']=True
    finally:
        record['seconds']=time.monotonic()-began;save()


if __name__=='__main__':main()
