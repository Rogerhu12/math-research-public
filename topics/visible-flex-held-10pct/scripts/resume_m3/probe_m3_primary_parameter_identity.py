#!/usr/bin/env python3
"""Read-only actual-constructor and complete-primary-moment identity check.

No BVP, tail solve, restart predictor or new initializer is run. The recorded
old gauge and full parameter vector reconstruct the actual old core via its
original class family. A fixed split Gauss quadrature reads the complete
source h and rho moments, including all fifteen physical controls. Separately
mpmath directly integrates the defining primary rho function; that is a
numerical defining-integral readout, not an interval proof. The companion
Fraction calculation supplies the scalar enclosure and q rounding proof.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import inspect
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
import mpmath as mp
from m3_raw_diagnostic_model import RawDiagnosticEnvironment,sha

MAPPING_SOURCE_SHA='bdcca0c9f12db1fed025b53e905e6e274b7bd61ec39c4a697e1ec066b214e302'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mapping',type=Path,required=True)
    parser.add_argument('--reference-run',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();began=time.monotonic()
    mapping=json.loads(args.mapping.read_text())
    if sha(Path(__file__).with_name('match_m3_circle_primary_moment.py'))!=MAPPING_SOURCE_SHA:
        raise ValueError('The frozen primary-moment formula changed')
    for path,digest in mapping['source_sha256'].items():
        if sha(path)!=digest:raise ValueError('A defining-moment source changed: '+path)
    checkpoint=Path(mapping['checkpoint']['path'])
    if sha(checkpoint)!=mapping['checkpoint']['sha256']:raise ValueError('The old physical anchor changed')
    cp=json.loads(gzip.decompress(checkpoint.read_bytes()))
    launch_path=args.reference_run/'continuation-command.json'
    launch=json.loads(launch_path.read_text());command=launch['command']
    arg=lambda name:command[command.index('--'+name)+1]
    if Path(arg('restart')).resolve()!=checkpoint.resolve():raise ValueError('Another old anchor was declared')
    chart=json.loads(Path(arg('chart')).read_text());profile=json.loads(Path(arg('profile')).read_text())
    port_path=Path(arg('linear-port'));port=json.loads(port_path.read_text());port['_sha256']=sha(port_path)
    if chart!=cp['chart'] or profile!=cp['frozen_profile'] or port['_sha256']!=cp['physical_port_sha256']:
        raise ValueError('The old actual chart/profile/physical port changed')
    env=RawDiagnosticEnvironment(Path(arg('source-topic')),Path(arg('short-bridge')),chart,cp['core_round_settings'])
    old=env.make(cp['core_round_settings'],profile,port,cp['gauge_amplitude'],16,
        cp['config']['angular'],True,cp['warp_reference_q'])
    par=np.asarray(cp['parameters'],float);scales=np.asarray(cp['central_correction_scales'],float)
    if old.pscale.tobytes()!=scales.tobytes():raise ValueError('The recorded physical control scales changed')
    old.initial(par);core=old._core
    control=par[1:]*scales
    q_by_constructor=old.seed_support_amplitude*math.exp(float(par[0]))
    if (core.q.hex()!=float(cp['actual_primary_amplitude']).hex() or
        core.q.hex()!=q_by_constructor.hex() or old.support_amplitude.hex()!=core.q.hex() or
        core.c.tobytes()!=control.tobytes()):
        raise ValueError('The actual old core does not match its recorded parameter construction')
    qold=core.q
    if qold!=mapping['checkpoint']['actual_parameter_q']:
        raise ValueError('The mapping did not use the actual core base multiplier')
    # Independent full-source readout on the positive reflection half-sector.
    # It includes all controls and uses the actual integral-defined support h.
    order=128;gx,gw=np.polynomial.legendre.leggauss(order)
    settings=cp['core_round_settings'];L=math.pi/3;T=2*L
    cuts=sorted(set([0.,settings['halfwidth'],settings['halfwidth']+settings['transition'],
        settings['halfwidth']+settings['control_transition'],L]))
    hsum=rsum=csum=0.
    for lo,hi in zip(cuts[:-1],cuts[1:]):
        phi=math.pi/3+(lo+hi)/2+(hi-lo)/2*gx;weights=(hi-lo)/2*gw
        g=core.normal_geometry(phi);cosine=np.cos(3*phi)
        hsum+=float(weights@(g['h']*cosine));rsum+=float(weights@(g['rho']*cosine))
        support_controls=control@core.basis.support_jets(phi,0,core.lam)[0]
        csum+=float(weights@(support_controls*cosine))
    Qh=4/T*hsum;Qr=(4/T*rsum)/(-8);Qc=4/T*csum
    with mp.workdps(90):
        a=mp.mpf(str(settings['halfwidth']));b=mp.mpf(str(settings['transition']))
        lam=mp.mpf(float(settings['homotopy']));q=mp.mpf(qold);Lm=mp.pi/3
        def chi(x):
            if x<=a:return mp.mpf(1)
            if x>=a+b:return mp.mpf(0)
            z=(x-a)/b
            return 1-z**5*(126+z*(-420+z*(540+z*(-315+70*z))))
        def smooth(x):return 8*mp.cos(3*x)
        # Mean correction is itself integrated, rather than copied from P.
        mean_chi=mp.quad(chi,[0,a,a+b,Lm])/Lm
        beta=-mp.quad(lambda x:chi(x)*(8-smooth(x)),[0,a,a+b,Lm])/Lm/(1-mean_chi)
        def rho(x):return 1+q*(smooth(x)+lam*(chi(x)*(8-smooth(x))+beta*(1-chi(x))))
        direct=-mp.quad(lambda x:rho(x)*(-mp.cos(3*x)),[0,a,a+b,Lm])/(4*Lm)
        formula=q*mp.mpf(mapping['old_factor']['P'])
        direct_difference=direct-formula
        defining=dict(precision=90,base_primary_direct_quadrature=mp.nstr(direct,80),
            beta_direct_quadrature=mp.nstr(beta,80),Q_formula=mp.nstr(formula,80),
            direct_minus_formula=mp.nstr(direct_difference,40),
            complete_control_primary_exact=0,
            complete_control_scope='All fifteen locked raw control primary moments vanish in their defining integrals; the finite source quadrature below separately includes their actual floating evaluation.',
            scope='Direct high-precision integral readout only; the companion exact rational scalar intervals establish enclosure claims.')
    source_paths=[Path(__file__),Path(arg('source-topic'))/'scripts/950f-prefix-warped-bvp.py']
    source_hashes={**env.sources,**{str(p.resolve()):sha(p) for p in source_paths}}
    constructor_method=next(cls.__dict__['initial'] for cls in type(old).__mro__ if cls.__name__=='WarpedBVP')
    constructor_source=inspect.getsource(constructor_method)
    result=dict(scope=__doc__,command=sys.argv,source_sha256=source_hashes,
        mapping=dict(path=str(args.mapping.resolve()),sha256=sha(args.mapping)),
        reference_run_launch=dict(path=str(launch_path.resolve()),sha256=sha(launch_path)),
        old_constructor=dict(gauge_amplitude=old.q,seed_support_amplitude=old.seed_support_amplitude,
            fixed_metric=old.fixed,p0=float(par[0]),q_from_original_constructor=q_by_constructor,
            actual_core_q=core.q,actual_core_q_hex=core.q.hex(),
            recorded_actual_parameter_q=cp['actual_primary_amplitude'],
            actual_support_amplitude_field=old.support_amplitude,
            complete_control_binary64_equal=True,physical_controls=control.tolist(),
            constructor_rule='q=seed_support_amplitude*math.exp(p0) for fixed=True; PlanarSupportCore(q,p[1:]*pscale,3). The q argument multiplies unit_rho directly.',
            constructor_method_source_sha256=hashlib.sha256(constructor_source.encode()).hexdigest(),
            warning='The checkpoint field actual_primary_amplitude is this base multiplier q, not the complete signed Fourier support coefficient Q=q*P.'),
        direct_defining_moment=defining,
        finite_complete_source_readout=dict(gauss_order=order,half_sector_cuts=cuts,
            full_support_Q=Qh,full_rho_inferred_Q=Qr,complete_control_Q=Qc,
            formula_Q=float(formula),full_support_minus_formula=float(Qh-float(formula)),
            full_rho_minus_formula=float(Qr-float(formula)),
            scope='Fixed split Gauss readout of the actual old core, including all controls. Numerical comparison, not a certified quadrature remainder.'),
        BVP_solver_invoked=False,actual_tail_solver_invoked=False,initializer_constructed=False,
        seconds=time.monotonic()-began)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),q_constructor=q_by_constructor,
        Qh=Qh,Q_formula=float(formula),source_difference=Qh-float(formula),
        direct_defining_difference=defining['direct_minus_formula'],seconds=result['seconds'])),flush=True)


if __name__=='__main__':main()
