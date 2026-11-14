#!/usr/bin/env python3
"""Local frozen-p Codazzi range: mixed/ruling chart and split quadrature.

Only the two endpoint correction arrays of a selected coast cell are free.
The ruling chart is used locally, with its real one-sided spatial jets; this
script does not construct a global atlas or a new BVP solution. Splitting
quadrature leaves the original two P1 nodes and all physical parameters
unchanged. Every local state is merely a finite linear diagnostic.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,copy,datetime,json,resource,time,traceback
from pathlib import Path
import numpy as np
from scipy import sparse,linalg
from scipy.optimize import lsq_linear
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_raw_bump_coast_reference import CoastReferenceRawBumpDAE,coast_window
from fd2d_k0_ruling_chart import FrozenRulingChart
from fd2d_gc_native_inverse_recovery import install_observed_recovery
from fd2d_gc_gauss_cell_codazzi_d2 import gauss_cell_codazzi_d2
from fd2d_gc_gauss_cell_codazzi_endpoint_d2 import gauss_cell_codazzi_endpoint_d2
from fd2d_gc_gauss_cell_codazzi import _view


class LocalRulingCoordinates:
    def __init__(self,original,inlet):
        self.original=original;self.frozen=FrozenRulingChart(inlet);self.theta=original.theta
    def coordinates(self,s,coordinate=None):
        x=np.atleast_1d(np.asarray(s,float));xi=self.theta if coordinate is None else np.atleast_1d(np.asarray(coordinate,np.longdouble))
        rows=[]
        for q in x:
            f=self.frozen
            sigma=0. if q==f.entry_s else f.length if q==f.entry_s+f.length else float(q-f.entry_s)
            rows.append(f.jet(sigma,xi))
        names=dict(u='U',u_s='U_s',u_xi='U_xi',u_ss='U_ss',u_sxi='U_sxi',u_xixi='U_xixi')
        out={k:np.stack([np.asarray(r[v],float) for r in rows],axis=1) for k,v in names.items()}
        if np.any(out['u_xi']<=0):raise ValueError('Local ruling chart lost positive angular derivative')
        out['advection']=out['u_s']/out['u_xi']
        # Old beta metadata has no meaning in this local chart and is omitted.
        return out


def view_on(problem,endpoints,chart):
    q=copy.copy(problem);q.chart=chart;q.x=np.asarray(endpoints,float);q.N=len(q.x);q.h=np.diff(q.x)
    q.size=q.N*q.q+q.parameter_count;q.residual_size=q.N*q.q+2*q.K+2
    q.coords={k:np.asarray(v,float) for k,v in chart.coordinates(q.x).items()}
    # Unused beta metadata is absent instead of being a nonfinite field.
    for key in ('beta','beta_s','beta_ss'):
        if key in q.coords and not np.all(np.isfinite(q.coords[key])):q.coords.pop(key)
    q._operator_cache={};q._cell_gauss_view_cache=None;q._chunked_gauss_codazzi_views=None
    return q


def make_local_scheme(problem,left,right,chart,kind):
    ref=problem.coast_reference;rim=problem.reference_rim_fraction*ref.length
    cuts=[left,right]
    order=2
    if kind=='rim_split_Gauss3':
        cuts += [z for z in (ref.entry_s,ref.entry_s+rim,ref.exit_s-rim,ref.exit_s) if left<z<right]
        order=3
    cuts=sorted(set(cuts));length=right-left;pieces=[];I=np.eye(problem.q)
    for a,b in zip(cuts[:-1],cuts[1:]):
        ta,tb=(a-left)/length,(b-left)/length
        transform=np.block([[(1-ta)*I,ta*I],[(1-tb)*I,tb*I]])
        pieces.append((view_on(problem,[a,b],chart),(b-a)/length,transform))
    return dict(pieces=pieces,order=order,cuts=cuts,length=length,original_endpoints=[left,right],kind=kind)


def local_evaluate(scheme,coefficient_vector,parameters,*,jacobian=False):
    r=None;J=None;full=None;point_G=0.;kappa=0.;nmin=float('inf');nmax=-float('inf');weight_integral=0.
    for view,w,transform in scheme['pieces']:
        yy=transform@coefficient_vector;vector=np.r_[yy,parameters]
        consumer=gauss_cell_codazzi_endpoint_d2 if scheme['kind']=='endpoint_lifting_Gauss2' else gauss_cell_codazzi_d2
        result=consumer(view,vector,order=scheme['order'],jacobian=jacobian)
        rr=np.r_[result['retained_residual'],result['high_residual']]
        r=w*rr if r is None else r+w*rr
        ff=result['full_codazzi_cells'];full=w*ff if full is None else full+w*ff
        if jacobian:
            mat=sparse.vstack((result['retained_jacobian'],result['high_jacobian']),format='csc')[:,:2*view.q].toarray()@transform
            J=w*mat if J is None else J+w*mat
        point_G=max(point_G,result['info']['sampled_interior_Gauss_maximum'])
        rule=_view(view,scheme['order']);qv,tau,weights=rule['view'],rule['tau'],rule['weights']
        yz=yy.reshape(2,view.q);yq=(1-tau)[:,None]*yz[0]+tau[:,None]*yz[1]
        lift=qv.lifting(parameters[qv.profile_parameter_slice],parameters[qv.tail_parameter_slice])
        fields=np.stack((qv.E@yq[:,:qv.e].T,qv.O@yq[:,qv.e:qv.d].T,qv.E@yq[:,qv.d:].T),axis=-1)+lift['values']
        n,m,l=(fields[:,:,j] for j in range(3));disc=np.hypot(l-n,2*m)
        kappa=max(kappa,float(np.max(np.maximum(abs(l+n+disc),abs(l+n-disc)))/2));nmin=min(nmin,float(n.min()));nmax=max(nmax,float(n.max()))
        _,wp=coast_window(rule['points'],view.coast_reference.entry_s,view.coast_reference.length,view.reference_rim_fraction)
        weight_integral+=w*scheme['length']*float(weights@np.asarray(wp).ravel())
    low_count=scheme['pieces'][0][0].d
    return dict(residual=r,jacobian=J,full_mean_maximum=float(np.max(abs(full))),
        retained_l2=float(np.linalg.norm(r[:low_count])),high_l2=float(np.linalg.norm(r[low_count:])),
        point_Gauss_maximum=point_G,formal_kappa=kappa,n_minimum=nmin,n_maximum=nmax,
        actual_weight_derivative_integral=weight_integral)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for flag in ('candidate','field','radius-packet','reference-inlet','reference-cache','out-prefix'):
        ap.add_argument('--'+flag,type=Path,required=True)
    ap.add_argument('--cell',type=int,default=71)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Unique output prefix required')
    stem.parent.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    report=dict(schema='fd2d-local-coast-chart-endpoint-lifting-range-v3',source=identity(__file__),
        inputs={k:identity(getattr(args,k)) for k in ('candidate','field','radius_packet','reference_inlet','reference_cache')},
        dependencies={n:identity(Path(__file__).parent/n) for n in ('fd2d_gc_native_inverse_recovery.py','fd2d_gc_raw_bump_coast_reference.py','fd2d_gc_frozen_coast_reference.py','fd2d_k0_ruling_chart.py','fd2d_gc_gauss_cell_codazzi_d2.py','fd2d_gc_gauss_cell_codazzi_endpoint_d2.py')},
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),completed=False,exception=None,
        physical_parameters_changed=False,global_atlas_constructed=False,nonlinear_BVP_performed=False,
        original_field_preserved=False,origin='Zero local correction, same fixed physical p; affine range is independent of this origin',
        no_certified_lower_bound_or_geometry_claim=True,comparisons=[])
    def save():
        report['seconds']=time.monotonic()-start;report['peak_RSS_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        d=load_npz(args.field);proof=json.loads(args.radius_packet.read_text());candidate=identity(args.candidate)
        if not proof['passed'] or proof['candidate_sha256']!=candidate['sha256']:raise ValueError('Wrong radius proof')
        definition=json.loads(str(d['coast_reference_definition']))
        problem=CoastReferenceRawBumpDAE(args.candidate,modes=int(d['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            reference_rim_fraction=float(definition['rim_fraction']),base_lower_bound='4/5',
            base_lower_provenance=dict(**identity(args.radius_packet),candidate_sha256=candidate['sha256']),radius_floor=.1)
        if definition!=problem.coast_reference_definition or not np.array_equal(d['mesh'],problem.x):raise ValueError('Saved actual identity differs')
        report['inverse_recovery_observations']=[]
        def observe_inverse(event):
            report['inverse_recovery_observations'].append(event);save()
        install_observed_recovery(problem.coast_reference,observer=observe_inverse)
        report['reference_evaluation_scope']='Loaded old26 cache unchanged; new local points use same native formula and 2e-13 tolerance, with explicit retained-bracket bisection after old60 iterations. No enlarged cache published as the original cache.'
        if not 0<=args.cell<problem.N-1:raise ValueError('Bad cell index')
        left,right=problem.x[args.cell:args.cell+2]
        if left<problem.coast_reference.entry_s or right>problem.coast_reference.exit_s:raise ValueError('This local chart comparison is restricted to the actual coast')
        p=np.asarray(d['parameters'],float);origin=np.zeros(2*problem.q);arrays={'parameters_fixed':p,'original_cell':np.array([left,right])}
        charts={'original_mixed':problem.chart,'natural_ruling':LocalRulingCoordinates(problem.chart,args.reference_inlet)}
        for chart_name,chart in charts.items():
            boundary=view_on(problem,[left,right],chart)
            lift=boundary.lifting(p[boundary.profile_parameter_slice],p[boundary.tail_parameter_slice])['values']
            projected=np.concatenate((boundary.PE@lift[:,:,0],boundary.PO@lift[:,:,1],boundary.PE@lift[:,:,2]),axis=0).T
            cap=1/.136;bound=cap*np.r_[np.sum(abs(boundary.PE),axis=1),np.sum(abs(boundary.PO),axis=1),np.sum(abs(boundary.PE),axis=1)]
            lo=(-bound[None,:]-projected).ravel();hi=(bound[None,:]-projected).ravel()
            for scheme_name in ('endpoint_lifting_Gauss2',):
                scheme=make_local_scheme(problem,left,right,chart,scheme_name)
                original=local_evaluate(scheme,origin,p,jacobian=True);r,J=original['residual'],original['jacobian']
                norms=np.linalg.norm(J,axis=0);used=norms>0;A=J[:,used]/norms[used]
                row=dict(chart=chart_name,quadrature=scheme_name,cell=args.cell,endpoints=[float(left),float(right)],
                    known_lifting_derivative_integration='Exact full endpoint difference; displayed sampled w-prime integral is an unused comparison only',
                    split_points=scheme['cuts'],order_per_subspan=scheme['order'],matrix_shape=list(J.shape),
                    U_xi_node_minimum=float(np.min(boundary.coords['u_xi'])),
                    actual_weight_derivative_integral=original['actual_weight_derivative_integral'],
                    exact_weight_derivative_integral=float(coast_window(np.array([right]),problem.coast_reference.entry_s,problem.coast_reference.length,problem.reference_rim_fraction)[0][0]-coast_window(np.array([left]),problem.coast_reference.entry_s,problem.coast_reference.length,problem.reference_rim_fraction)[0][0]),
                    original_zero_origin_l2=float(np.linalg.norm(r)),cases=[])
                for cutoff in (1e-10,1e-12):
                    coef,_,rank,sv=linalg.lstsq(A,-r,cond=cutoff,lapack_driver='gelsd')
                    yy=np.zeros_like(origin);yy[used]=coef/norms[used]
                    actual=local_evaluate(scheme,yy,p)
                    row['cases'].append(dict(kind='unbounded_SVD',relative_cutoff=cutoff,rank=int(rank),
                        minimum_scaled_singular_value=float(sv[-1]),maximum_coefficient=float(np.max(abs(yy))),
                        actual_l2=float(np.linalg.norm(actual['residual'])),predicted_l2=float(np.linalg.norm(r+J@yy)),
                        backsubstitution_maximum=float(np.max(abs(actual['residual']-r-J@yy))),
                        full_mean_maximum=actual['full_mean_maximum'],high_l2=actual['high_l2'],
                        formal_kappa=actual['formal_kappa'],point_Gauss_maximum=actual['point_Gauss_maximum']))
                fit=lsq_linear(A,-r,bounds=(lo[used]*norms[used],hi[used]*norms[used]),method='bvls',tol=1e-11,max_iter=240)
                yy=np.clip(origin,lo,hi);yy[used]=fit.x/norms[used]
                actual=local_evaluate(scheme,yy,p)
                row['necessary_component_coefficient_box']=dict(cap=cap,status=int(fit.status),optimality=float(fit.optimality),iterations=int(fit.nit),
                    actual_l2=float(np.linalg.norm(actual['residual'])),predicted_l2=float(np.linalg.norm(r+J@yy)),
                    full_mean_maximum=actual['full_mean_maximum'],high_l2=actual['high_l2'],
                    formal_kappa=actual['formal_kappa'],point_Gauss_maximum=actual['point_Gauss_maximum'],
                    maximum_coefficient=float(np.max(abs(yy))),box_is_not_sufficient_for_curvature_cap=True)
                key=chart_name+'_'+scheme_name;arrays[key+'_box_corrections']=yy.reshape(2,problem.q);arrays[key+'_box_residual']=actual['residual']
                report['comparisons'].append(row);save();print(json.dumps(row,allow_nan=False),flush=True)
        report['local_states']=save_npz(stem.with_name(stem.name+'-local-states.npz'),**arrays)
        report['reference_cache_final_statistics']=problem.coast_reference.cache_statistics()
        report['completed']=True;save();return 0
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise


if __name__=='__main__':raise SystemExit(main())
