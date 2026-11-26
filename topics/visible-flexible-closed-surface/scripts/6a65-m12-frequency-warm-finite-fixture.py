#!/usr/bin/env python3
"""Independent finite checks for the new M12 frequency-only warm interface.

Synthetic nonzero coefficients exercise every old planar/height channel.
No original M12 field, source solve, nonlinear acceptance, or geometric
certificate is asserted by this fixture. All generated arrays are temporary.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os,subprocess,sys,tempfile,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solve_triangular

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p);module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module);return module
def eval_direct(knots,coeff,pm,zm,z,theta,dr,da):
    full=np.vstack((np.zeros((3,coeff.shape[1])),coeff,np.zeros((3,coeff.shape[1]))))
    amplitude=BSpline(knots,full,5,axis=0)(z,nu=dr)
    P=len(pm);c=np.exp(1j*np.outer(theta,pm))*(1j*pm)[None,:]**da
    planar=amplitude[:,:P]@c.T
    height=(amplitude[:,P:]@((np.exp(1j*np.outer(theta,zm))*(1j*zm)[None,:]**da).real).T)
    return np.stack((planar.real,planar.imag,height),axis=-1)
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('Fresh finite warm-interface receipt required')
    files={key:args.scripts/name for key,name in {
      'grid':'6a65-m12-frequency-only-grid-prepare.py',
      'transfer':'6a65-m12-frequency-only-warm-transfer.py',
      'warm':'6a65-m12-entire-half-cartesian-warm-refinement.py'}.items()}
    transfer=load('synthetic_frequency_transfer',files['transfer'])
    warm=load('synthetic_frequency_warm',files['warm'])
    rng=np.random.default_rng(202611261421);mesh=[0.,.03,.13,.31,.44,.71,.9,1.]
    knots=np.r_[[0.]*6,mesh[1:-1],[1.]*6];old_order,new_order=3,5
    old_pm=3*np.arange(-old_order,old_order+1)+1;old_zm=3*np.arange(old_order+1)
    new_pm=3*np.arange(-new_order,new_order+1)+1;new_zm=3*np.arange(new_order+1)
    coeff=rng.normal(size=(len(knots)-12,len(old_pm)+len(old_zm)))*2e-5
    lifted,indices,extra=transfer.transfer(coeff,old_pm,old_zm,new_pm,new_zm)
    points=np.unique(np.r_[0.,1.,mesh,np.linspace(.003,.997,33)])
    theta=(np.arange(37)+.317)*2*np.pi/37
    jet_errors={}
    for dr,da in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)):
        a=eval_direct(knots,coeff,old_pm,old_zm,points,theta,dr,da)
        b=eval_direct(knots,lifted,new_pm,new_zm,points,theta,dr,da)
        jet_errors[str((dr,da))]=float(np.max(np.abs(a-b)))
    end_errors=[float(np.max(np.abs(eval_direct(knots,lifted,new_pm,new_zm,[0.,1.],theta,dr,0)))) for dr in range(3)]
    # Independently generate dense triangular factors. This checks recovery
    # of physical gradients, not a duplicate of the production indexing loop.
    nb,na=9,5;modes=np.array([-2,1,3,0,2]);factors={}
    physical=rng.normal(size=(nb,na));coordinate=np.empty_like(physical)
    for k in np.unique(abs(modes)):
        dense=np.diag(1.5+rng.random(nb))
        for d in range(1,6):dense+=np.diag(.1*rng.normal(size=nb-d),-d)
        lower=np.zeros((6,nb))
        for d in range(6):lower[d,:nb-d]=np.diag(dense,-d)
        factors[int(k)]=(lower,None)
        for col in np.flatnonzero(abs(modes)==k):
            coordinate[:,col]=solve_triangular(dense,physical[:,col],lower=True)
    op=SimpleNamespace(basis=SimpleNamespace(nb=nb,na=na,modes=modes),bandwidth=5,factors=factors)
    recovered=warm.physical_gradient_from_old_coordinates(op,coordinate.T.ravel())
    gradient_error=float(np.linalg.norm(recovered-physical)/np.linalg.norm(physical))
    stage_receipts=[]
    with tempfile.TemporaryDirectory(prefix='m12-frequency-fixture-') as temporary:
        root=Path(temporary);old_grid=root/'old-grid.json';new_grid=root/'new-grid.json'
        old_field=root/'old-field.npz';old_result=root/'old-result.json';out=root/'transfer.json'
        queries=Path(str(old_grid)+'.queries.json')
        queries.write_text(json.dumps({'schema':'synthetic-query-fixture','radii':['1/5','3/5']})+'\n')
        definition={key:'synthetic-'+key for key in transfer.DEFINITION_KEYS}
        definition.update(schema='synthetic-fixed-definition-only',unit_mesh=mesh,order=old_order,angular=48,gauss=6,
          query_file_sha256=sha(queries),comparison_observer={'angular_nodes':96,'missing_old_unit_nodes':[.123],
          'missing_old_radial_indices':[11],'missing_old_observer_origins':[[{'origin_grid_sha256':'synthetic','origin_radial_index':11}]],
          'old_gauss':8,'all_old_nodes_contained_in_union':True,
          'all_unchanged_element_nodes_retained_exactly':True,'all_ancestor_observers_contained_in_union':True,
          'ancestor_grid_sha256s':['synthetic']})
        old_grid.write_text(json.dumps(definition,indent=2)+'\n')
        np.savez_compressed(old_field,coefficients=coeff,unit_knots=knots,planar_modes=old_pm,vertical_modes=old_zm)
        old_result.write_text(json.dumps({'field_sha256':sha(old_field),'grid_sha256':sha(old_grid),
          'original_exact_metric_unchanged':True,'all_internal_interfaces_free':True,
          'true_flat_cuff_included':True,'full_half_including_finite_tail_and_deep_collar':True,
          'this_is_a_synthetic_interface_fixture_not_an_original_M12_field':True})+'\n')
        commands=[
          [sys.executable,str(files['grid']),'--old-grid',str(old_grid),'--out',str(new_grid),'--order',str(new_order),'--angular','96'],
          [sys.executable,str(files['transfer']),'--old-grid',str(old_grid),'--new-grid',str(new_grid),
           '--old-field',str(old_field),'--old-result',str(old_result),'--out',str(out)]]
        env={k:v for k,v in os.environ.items() if k not in ('GITHUB_TOKEN','GH_TOKEN','M12_RECOVERY_TOKEN')}
        for command in commands:
            p=subprocess.run(command,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            stage_receipts.append({'source':Path(command[1]).name,'exit_code':p.returncode})
            if p.returncode:raise RuntimeError('Actual fixture child failed: '+p.stderr[-2000:])
        saved=json.loads(out.read_text());prepared=json.loads(new_grid.read_text())
        reader_args=SimpleNamespace(warm_field=Path(str(out)+'.field.npz'),warm_receipt=out,
             scripts=args.scripts,grid=new_grid)
        reader_basis=SimpleNamespace(knots=knots,pm=new_pm,zm=new_zm,nb=coeff.shape[0],na=len(new_pm)+len(new_zm))
        consumed,receipt=warm.actual_warm_field(reader_args,reader_basis)
        consumed_exact=np.array_equal(consumed,lifted)
        unchanged_query=Path(str(new_grid)+'.queries.json').read_bytes()==queries.read_bytes()
        ancestor_preserved=prepared['comparison_observer']['missing_old_unit_nodes']==[.123]
        old_angle_count_preserved=96 in prepared['comparison_observer']['ancestor_angular_nodes']
    verified=bool(max(jet_errors.values())<1e-11 and max(end_errors)==0. and gradient_error<2e-14
                  and consumed_exact and unchanged_query and ancestor_preserved and old_angle_count_preserved
                  and np.count_nonzero(coeff)==coeff.size and len(extra)>0)
    report={'schema':'6a65-frequency-only-warm-interface-independent-finite-fixture-v1',
      'fixture_sha256':sha(__file__),'sources':{k:sha(p) for k,p in files.items()},
      'synthetic_only':True,'original_M12_field_consumed':False,'new_nonlinear_solve_executed':False,
      'seed':202611261421,'nonzero_old_coefficients':int(np.count_nonzero(coeff)),
      'old_order':old_order,'new_order':new_order,'old_shape':list(coeff.shape),'new_shape':list(lifted.shape),
      'old_coefficients_bitwise_copied':lifted[:,indices].tobytes()==coeff.tobytes(),
      'all_new_channels_exactly_zero':bool(np.count_nonzero(lifted[:,extra])==0),
      'direct_independent_six_jet_maximum_differences':jet_errors,
      'exact_clamped_endpoint_jet_errors':end_errors,
      'physical_gradient_recovery_relative_error':gradient_error,
      'actual_CLI_stages':stage_receipts,'actual_warm_reader_consumed_complete_field':consumed_exact,
      'exact_query_recipe_bytes_retained':unchanged_query,
      'ancestor_radial_and_angular_observers_retained':ancestor_preserved and old_angle_count_preserved,
      'verified':verified,'seconds':time.monotonic()-started}
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2,allow_nan=False))
    if not verified:raise AssertionError('Warm interface finite check failed')
if __name__=='__main__':main()
