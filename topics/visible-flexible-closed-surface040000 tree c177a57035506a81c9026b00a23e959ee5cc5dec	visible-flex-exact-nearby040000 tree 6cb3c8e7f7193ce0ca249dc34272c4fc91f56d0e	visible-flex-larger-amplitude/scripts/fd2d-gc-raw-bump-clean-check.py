"""Actual mesh/central-lifting conversion and one full analytic-JVP check."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse, json, time
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_raw_bump_dae import RawBumpDAE
from fd2d_gc_raw_bump_clean import CleanRawBumpDAE, seed_weight
from fd2d_gc_codazzi_complement import codazzi_complement
from fd2d_gc_bump_residual_locations import residual_locations


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();stem=args.out_prefix
    a=load_npz(args.input);K=int(a['modes'])
    old=RawBumpDAE(args.candidate,modes=K,supports=a['profile_supports'])
    if not np.array_equal(a['mesh'],old.x):
        raise ValueError('The observed old field does not use the recorded old mesh')
    old_vector=np.r_[a['corrections'].ravel(),a['parameters']]
    old_f,old_d=old.evaluate(old_vector)
    old_c=codazzi_complement(old,old_vector,data=old_d,jacobian=False)
    new=CleanRawBumpDAE(args.candidate,modes=K,supports=a['profile_supports'])
    vector,conversion=new.warm_from_bump(a['mesh'],a['corrections'],a['parameters'],
        old_seed_definition=new.legacy_seed_weight_definition)
    f,j,d=new.evaluate(vector,jacobian=True)
    c=codazzi_complement(new,vector,data=d,jacobian=True)
    high=old.seed-old.E@(old.PE@old.seed)
    ss=np.linspace(0,old.profile.central_end,4097)
    w,ws=seed_weight(ss,new.legacy_seed_weight_definition)
    wn,wsn=seed_weight(ss,new.seed_weight_definition)
    seed_screen=dict(angular_points=old.work,radial_points=len(ss),
        omitted_seed_maximum=float(np.max(abs(high))),
        omitted_seed_rms=float(np.sqrt(np.mean(high**2))),
        old_cylinder_end_weight=float(w[-1]),
        old_central_high_forcing_maximum=float(np.max(abs(ws))*np.max(abs(high))),
        new_central_seed_derivative_maximum=float(np.max(abs(wsn))),
        new_cylinder_weight_error=float(np.max(abs(wn-1))),
        scope='Sampled angular Fourier complement; central quintic extrema include s=.275 exactly')
    # Compare the full fixed physical target functions, not only labels.
    delta=a['parameters'][new.profile_parameter_slice]
    old.profile.set_parameters(delta);new.profile.set_parameters(delta)
    so=np.linspace(0,new.profile.end,517)
    jo,jn=old.profile.jet(so),new.profile.jet(so)
    target_errors={k:float(np.max(abs(jo[k]-jn[k]))) for k in ('a','a_s','a_ss','c','K')}
    co,cn=old.chart.coordinates(so),new.chart.coordinates(so)
    chart_errors={k:float(np.max(abs(np.asarray(co[k])-np.asarray(cn[k])))) for k in co}
    # One mixed nonzero state/central/tail/profile direction; no new BVP.
    rng=np.random.default_rng(128137)
    direction=rng.normal(size=new.size)
    direction[:new.N*new.q]*=.03
    direction[new.N*new.q:]*=.003
    direction=new.impose_linear_boundary_values(vector+direction)-vector
    actual=np.r_[f,c['residual']]
    analytic=np.r_[j@direction,c['jacobian']@direction]
    checks=[]
    for eps in (2e-6,1e-6):
        plus=vector+eps*direction;minus=vector-eps*direction
        fp,dp=new.evaluate(plus);fm,dm=new.evaluate(minus)
        cp=codazzi_complement(new,plus,data=dp,jacobian=False)
        cm=codazzi_complement(new,minus,data=dm,jacobian=False)
        fd=(np.r_[fp,cp['residual']]-np.r_[fm,cm['residual']])/(2*eps)
        checks.append(dict(epsilon=eps,absolute_l2=float(np.linalg.norm(fd-analytic)),
            relative_l2=float(np.linalg.norm(fd-analytic)/max(1.,np.linalg.norm(analytic))),
            maximum=float(np.max(abs(fd-analytic)))))
    f,d=new.evaluate(vector);c=codazzi_complement(new,vector,data=d,jacobian=False)
    y,p=new.unpack(vector)
    warm=save_npz(stem.with_name(stem.name+'-warm.npz'),mesh=new.x,corrections=y,parameters=p,
        modes=np.array(K),profile_supports=new.profile.supports,profile_count=np.array(new.J),
        fixed_base_T=np.array(new.fixed_base_T),profile_kind=np.array(new.profile_kind),
        tail_kind=np.array(new.tail_kind),base_kind=np.array(new.base_kind),
        candidate_sha256=a['candidate_sha256'],blend=np.array(new.blend),
        seed_weight_definition=np.array(json.dumps(new.seed_weight_definition,sort_keys=True)),
        representation_kind=np.array(new.representation_kind))
    report=dict(schema='fd2d-raw-bump-clean-actual-check-v1',source=identity(__file__),
        providers={k:identity(Path(__file__).parent/k) for k in ('fd2d_gc_raw_bump_clean.py',
            'fd2d_gc_raw_bump_dae.py','fd2d_gc_codazzi_complement.py','fd2d_gc_bump_residual_locations.py')},
        candidate=identity(args.candidate),old_actual_state=identity(args.input),
        mesh_coalescence=new.mesh_coalescence,seed_screen=seed_screen,warm_conversion=conversion,
        target_function_errors=target_errors,angular_chart_errors=chart_errors,
        old_diagnostics=old.diagnostics(old_vector,old_d),
        old_locations=residual_locations(old,old_vector,old_d,old_c),
        new_diagnostics=new.diagnostics(vector,d),
        new_locations=residual_locations(new,vector,d,c),
        new_omitted_codazzi=c['info'],analytic_jvp=checks,warm=warm,
        seconds=time.monotonic()-start,nonlinear_solve_performed=False,continuous_certificate=False)
    stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(seconds=report['seconds'],old_nodes=old.N,new_nodes=new.N,
        new_min_cell=float(new.h.min()),seed_screen=seed_screen,jvp=checks,
        old_raw=float(np.max(abs(old_f))),new_raw=float(np.max(abs(f))),warm=warm),allow_nan=False),flush=True)


if __name__=='__main__':main()
