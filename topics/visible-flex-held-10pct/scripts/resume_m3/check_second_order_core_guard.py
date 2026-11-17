#!/usr/bin/env python3
"""Check the C2 guard addition on existing m3 endpoint inputs and trial controls.

No BVP, Newton or tail is solved.  Geometry and parameter jets are compared
bitwise where both old and new guards construct the core.  The already
recorded 21 trial controls are evaluated only under the new core guard; no
Frenet, merit or accepted-solution conclusion is drawn for those trials.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_comparison(a,b):
    a,b=np.asarray(a),np.asarray(b)
    return dict(shape=list(a.shape),dtype=str(a.dtype),
        same_dtype_and_shape=a.shape==b.shape and a.dtype==b.dtype,
        byte_identical=a.shape==b.shape and a.dtype==b.dtype and
            np.ascontiguousarray(a).tobytes()==np.ascontiguousarray(b).tobytes(),
        max_absolute_difference=float(abs(a-b).max()),
        original_bytes_sha256=hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest(),
        new_bytes_sha256=hashlib.sha256(np.ascontiguousarray(b).tobytes()).hexdigest())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--diagnostic',type=Path,required=True)
    p.add_argument('--initial-record',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angular',type=int,default=2048)
    a=p.parse_args();start=time.monotonic()
    d=json.loads(a.diagnostic.read_text());initial=json.loads(a.initial_record.read_text())
    lib=Path(__file__).with_name('round_raw_lib');sys.path.insert(0,str(lib))
    from plateau_core import PlateauSupportCore
    from tight_moment_interval_bounds import install
    install()
    from fixed_large_radius_core import make_core_class as old_factory
    from raw_second_order_core import make_core_class as new_factory, PROVENANCE
    from exact_lift_parameter_jac import parameter_jets
    Old,New=old_factory(PlateauSupportCore),new_factory(PlateauSupportCore)
    settings=d['settings'];q=d['q_gauge']
    if settings['positivity_grid_max']!=32768 or settings['homotopy']!=1.:
        raise ValueError('The declared original endpoint/grid setting changed')
    par=np.asarray(d['parameters']);step=np.asarray(d['parameter_step'])
    scales=np.asarray(d['original_control_scales'])
    if len(d['trials'])!=21 or any(z.get('core_domain_passed') for z in d['trials']):
        raise ValueError('Expected the recorded all-core-rejected 21-trial sequence')
    psi=2*np.pi*np.arange(a.angular)/a.angular
    material=psi-.32*np.sin(3*psi)/3
    vectors={'original_endpoint_entry':np.asarray(initial['initial_physical_controls']),
             'saved_failed_endpoint':par[1:]*scales}
    comparisons={}
    for name,c in vectors.items():
        old=Old(q,c,3,arc_nodes=1024,**settings)
        new=New(q,c,3,arc_nodes=1024,**settings)
        og,ng=old.evaluate(material),new.evaluate(material)
        oldjets,newjets=old.rho_material_jets(material),new.rho_material_jets(material)
        values={key:array_comparison(og[key],ng[key]) for key in ('F','Ft','Ftt','kappa','phi')}
        values.update({key:array_comparison(oldjets[key],newjets[key]) for key in
            ('rho','rho_u','rho_uu','rho_phi','rho_phiphi','normal')})
        for j,(u,v) in enumerate(zip(parameter_jets(old,material),parameter_jets(new,material))):
            values['full_parameter_jet_'+str(j)]=array_comparison(u,v)
        if not all(z['byte_identical'] for z in values.values()):
            raise ArithmeticError('A geometry or parameter jet changed at '+name)
        row=dict(all_checked_jets_byte_identical=True,comparisons=values,
            old_guard_lower=old.rho_lower,new_guard_lower=new.rho_lower,
            old_guard_grid=old.positivity_grid_per_sector,new_guard_grid=new.positivity_grid_per_sector,
            original_sample_min=old.rho_min_sample,new_sample_min=new.rho_min_sample,
            analytic_second_derivative_bound=new.rho_second_derivative_bound,
            unchanged_value_roundoff_allowance=old.rho_value_roundoff_allowance==new.rho_value_roundoff_allowance)
        if not row['unchanged_value_roundoff_allowance']:
            raise ArithmeticError('The point-value allowance changed')
        comparisons[name]=row
        print(json.dumps(dict(event='same_geometry',state=name,
            old_lower=old.rho_lower,new_lower=new.rho_lower,
            old_grid=old.positivity_grid_per_sector,new_grid=new.positivity_grid_per_sector,
            bitwise=True)),flush=True)
    trials=[]
    for original in d['trials']:
        alpha=original['alpha'];tp=par-alpha*step;c=tp[1:]*scales
        row=dict(alpha=alpha,original_error=original['error'])
        try:
            core=New(q,c,3,arc_nodes=1024,**settings)
            row.update(new_core_guard_passed=True,rho_lower=core.rho_lower,
                rho_sample_min=core.rho_min_sample,grid=core.positivity_grid_per_sector,
                analytic_second_derivative_bound=core.rho_second_derivative_bound,
                point_value_allowance=core.rho_value_roundoff_allowance)
            if not core.rho_lower>1e-5 or core.positivity_grid_per_sector>32768:
                raise ArithmeticError('The original floor or ceiling was not retained')
        except FloatingPointError as error:
            row.update(new_core_guard_passed=False,error=str(error))
        trials.append(row);print(json.dumps(dict(event='guard_trial',**row)),flush=True)
    sources=[Path(__file__),Path(__file__).with_name('raw_second_order_core.py'),*sorted(lib.glob('*.py'))]
    result=dict(scope=__doc__,command=sys.argv,
        input_diagnostic=dict(path=str(a.diagnostic.resolve()),sha256=sha(a.diagnostic)),
        input_initial_record=dict(path=str(a.initial_record.resolve()),sha256=sha(a.initial_record)),
        settings=settings,q=q,angular_samples=a.angular,
        material_chart='u=psi-.32*sin(3*psi)/3, the original warp_reference=.04 inlet chart',
        provenance=PROVENANCE,source_sha256={str(f.resolve()):sha(f) for f in sources},
        comparisons=comparisons,trials=trials,
        new_guard_pass_count=sum(row['new_core_guard_passed'] for row in trials),
        new_guard_fail_count=sum(not row['new_core_guard_passed'] for row in trials),
        seconds=time.monotonic()-start,
        interpretation='A finite bitwise geometry/parameter-jet comparison and a '
            'same-input numerical guard check. The additional second derivative '
            'budget is whole-domain analytic, but the floating guard is not a '
            'rigorous libm/complete-surface certificate. Newly passing core trials '
            'must still face the unchanged original Frenet/BC/merit and full BVP '
            'and actual-tail gates in a separate owned run.')
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='finished',passes=result['new_guard_pass_count'],
        fails=result['new_guard_fail_count'],seconds=result['seconds'])),flush=True)


if __name__=='__main__':
    main()
