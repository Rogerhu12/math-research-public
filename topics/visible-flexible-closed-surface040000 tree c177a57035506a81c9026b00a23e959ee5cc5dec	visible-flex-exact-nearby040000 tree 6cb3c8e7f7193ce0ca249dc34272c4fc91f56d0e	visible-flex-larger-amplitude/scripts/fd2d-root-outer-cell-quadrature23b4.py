"""Fixed-state no-J quadrature diagnosis of three actual non-coast P1 cells.

All terms of the complete physical RHS are integrated at identical points.
This compares finite rules, not a rigorous integral error or a solved BVP.
"""
from __future__ import annotations
import argparse, datetime, hashlib, json, resource, time
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import load_npz, identity
from fd2d_gc_midpoint_refined_positive_trace_v3 import create_midpoint_refined_problem
from fd2d_gc_hybrid_lifting_codazzi_d2 import fixed_lifting_breaks, point_view, quadrature_on_parts


def maximum(a):
    return float(np.max(np.abs(a), initial=0.))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args=ap.parse_args(); stem=args.out_prefix
    report_path=stem.with_name(stem.name+'-report.json')
    if report_path.exists(): raise FileExistsError(report_path)
    start=time.monotonic()
    field=Path('notes/2026-11-12-fd2d-raw-bump-reuse23-b0004-accepted-0001.npz')
    archived=Path('notes/2026-11-12-fd2d-raw-bump-reuse23-b0004-field.npz.gz')
    candidate=Path('notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    radius=Path('notes/2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json')
    inlet=Path('notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    cache=Path('notes/2026-11-12-fd2d-metric-frozen-coast-reference-01-cache.npz')
    saved=load_npz(field); old=load_npz(archived)
    for key in ('mesh','corrections','parameters'):
        if not np.array_equal(saved[key],old[key]): raise ValueError('Archived finite report binds another field')
    proof=json.loads(radius.read_text())
    if not proof['passed'] or proof['candidate_sha256']!=identity(candidate)['sha256']: raise ValueError('Wrong base radius witness')
    witness=dict(**identity(radius),candidate_sha256=proof['candidate_sha256'])
    problem=create_midpoint_refined_problem(candidate,saved_field=saved,split_cells=(),
        modes=31,max_step=.04,gap=.9,reference_inlet=inlet,reference_cache=cache,
        reference_rim_fraction=.12,minimum_active_n=.05,mesh_relative_tolerance=1e-12,
        base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=.1)
    if not np.array_equal(saved['mesh'],problem.x): raise ValueError('Original saved mesh changed')
    y,p=np.asarray(saved['corrections']),np.asarray(saved['parameters'])
    breaks,break_definition=fixed_lifting_breaks(problem)
    samples={}; rows=[]
    def evaluate(cell,points):
        values=[]; rhs=[]; gauss=[]
        left,right=problem.x[cell:cell+2]
        for first in range(0,len(points),2):
            xx=np.asarray(points[first:first+2],float)
            v=point_view(problem,xx)
            if np.any(v.window()!=0.) or np.any(v.trace_window()!=0.):
                raise ValueError('This affine-only diagnostic must remain wholly outside both nonlinear windows')
            t=(xx-left)/(right-left)
            yy=(1-t[:,None])*y[cell]+t[:,None]*y[cell+1]
            ops=v.operators(p[v.profile_parameter_slice]); jet=ops['jet']
            lift=v.lifting(p[v.profile_parameter_slice],p[v.tail_parameter_slice])
            f=np.stack((v.E@yy[:,:v.e].T,v.O@yy[:,v.e:v.d].T,v.E@yy[:,v.d:].T),axis=-1)+lift['values']
            fx=np.stack((v.Ex@yy[:,:v.e].T,v.Ox@yy[:,v.e:v.d].T,v.Ex@yy[:,v.d:].T),axis=-1)+lift['xi']
            inv,adv,c=ops['inv'],ops['adv'],jet['c'][None,:]
            ff=np.stack((inv*fx[:,:,1]+c*(f[:,:,2]-f[:,:,0])+adv*fx[:,:,0],
                         inv*fx[:,:,2]-2*c*f[:,:,1]+adv*fx[:,:,1]),axis=-1)
            gg=f[:,:,0]*f[:,:,2]-f[:,:,1]**2-jet['K'][None,:]
            values.append(f);rhs.append(ff);gauss.append(gg)
        return np.concatenate(values,axis=1),np.concatenate(rhs,axis=1),np.concatenate(gauss,axis=1)
    for cell in (81,82,101):
        left,right=map(float,problem.x[cell:cell+2]); width=right-left
        endpoints,_,_=evaluate(cell,np.array([left,right]))
        endpoint=(endpoints[:,1,:2]-endpoints[:,0,:2])/width
        g,w=np.polynomial.legendre.leggauss(2);g=(g+1)/2;w=w/2
        x2=left+width*g
        _,rhs2,G2=evaluate(cell,x2)
        C2=endpoint-np.einsum('wne,n->we',rhs2,w)
        cuts=np.r_[left,breaks[(breaks>left)&(breaks<right)],right]
        xf,wf,panels=quadrature_on_parts(left,right,cuts,8)
        _,rhsf,Gf=evaluate(cell,xf)
        Cf=endpoint-np.einsum('wne,n->we',rhsf,wf)
        xm=np.array([float((np.longdouble(left)+np.longdouble(right))/2)])
        _,_,Gm=evaluate(cell,xm)
        low=np.asarray(old['codazzi_cells'][cell]);high=np.asarray(old['omitted_codazzi_cells'][:,cell])
        Cold=np.stack((problem.E@low[:problem.e],problem.O@low[problem.e:]),axis=-1)+high
        diff=Cf-C2; lowdiff=np.r_[problem.PE@diff[:,0],problem.PO@diff[:,1]]
        row=dict(cell=cell,interval=[left,right],width=width,
            nonlinear_windows_identically_zero_at_all_evaluated_points=True,
            original_G2_reproduction_maximum_difference=maximum(C2-Cold),
            original_G2_full_Codazzi_maximum=[maximum(C2[:,j]) for j in range(2)],
            split_G8_full_Codazzi_maximum=[maximum(Cf[:,j]) for j in range(2)],
            split_G8_minus_G2_full_maximum=[maximum(diff[:,j]) for j in range(2)],
            split_G8_minus_G2_retained_maximum=maximum(lowdiff),
            actual_Gauss_maximum=dict(G2=maximum(G2),midpoint=maximum(Gm),split_G8=maximum(Gf)),
            fine_panels=panels,fine_weight_sum=float(wf.sum()))
        rows.append(row)
        samples.update({f'cell{cell}_C2':C2,f'cell{cell}_Cf':Cf,f'cell{cell}_G2':G2,
            f'cell{cell}_Gf':Gf,f'cell{cell}_Gmid':Gm,f'cell{cell}_xf':xf,f'cell{cell}_wf':wf})
        print(json.dumps(dict(event='closed_cell',**row)),flush=True)
    out=stem.with_name(stem.name+'-witnesses.npz')
    if out.exists(): raise FileExistsError(out)
    np.savez_compressed(out,**samples)
    sources=[Path(__file__),Path('scripts/fd2d_gc_midpoint_refined_positive_trace_v3.py'),
        Path('scripts/fd2d_gc_hybrid_lifting_codazzi_d2.py')]
    report=dict(schema='fd2d-fixed-23b4-noncoast-full-RHS-quadrature-diagnosis-v1',
        completed=True,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        sources=[identity(q) for q in sources],inputs=[identity(q) for q in (field,archived,candidate,radius,inlet,cache)],
        dimensions=dict(nodes=problem.N,modes=problem.K,parameters=problem.parameter_count,angles=problem.work),
        fixed_physical_g_and_all_parameters=True,unknown_mesh_unchanged=True,
        no_Jacobian_or_BVP_or_body_computed=True,continuous_error_certificate=False,
        exact_integral_claimed=False,rows=rows,witnesses=identity(out),
        fixed_break_definitions=break_definition,
        interpretation='All physical RHS terms use identical actual quadrature points. These are three fixed-state finite comparisons; no inferred impossibility or independent convergence certificate.',
        seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(event='completed',report=str(report_path),seconds=report['seconds'])),flush=True)


if __name__=='__main__': main()
