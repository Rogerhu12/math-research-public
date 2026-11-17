#!/usr/bin/env python3
"""Complete weighted tail with an explicit material seed and separated QR storage.

The supplied physical-angle trace is truncated explicitly to M modes; rho remains the complete fixed core metric.  Its
height-normal derivative is read out for matching, never imposed in addition
to the M Dirichlet rows.  The same new fixed background is used throughout a
homotopy and spectral refinement.  The finite deep graph is a design boundary.  A material seed is only an
unaccepted initial guess: the physical trace, fixed metric, rho, and declared
deep rows remain the target, and the complete weighted BVP is solved anew.
"""
import argparse,gzip,hashlib,json,time,importlib.util
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from parallel_20261117_dynamic_tail import Background
from parallel_20261117_weighted_tail import WeightedMean,weak_deep_boundary
from parallel_20261117_continue import feasible_newton


def main(a):
    started=time.perf_counter();source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    trace_raw=a.trace.read_bytes();trace=json.loads(trace_raw);bg=Background(a.background,a.coordinate)
    if bg.data.get('shallow_at')!='left':raise ValueError('This prefix-cuff design expects the shallow cut at the left')
    if a.fast_jacobian:
        from parallel_20261117_weighted_tail_fast import FastWeightedMean
        q=FastWeightedMean(a.modes,a.angles,trace['rho_cos_coefficients'])
    else:q=WeightedMean(a.modes,a.angles,trace['rho_cos_coefficients'])
    q.require_positive_height_slope=not a.allow_height_turn
    target=a.scale*np.array(trace['Ptilde_sin_coefficients'][:q.M])
    columns=None;deep_sha=None
    if a.deep_columns:
        raw=a.deep_columns.read_bytes();columns=json.loads(raw);deep_sha=hashlib.sha256(raw).hexdigest()
    bp,bk,deep_boundary=weak_deep_boundary(q,bg,columns)
    source_names=['parallel_20261117_weighted_tail.py','parallel_20261117_dynamic_tail.py','parallel_20261117_continue.py']
    if a.fast_jacobian:source_names.append('parallel_20261117_weighted_tail_fast.py')
    dependencies={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in source_names}
    qr_path=Path(__file__).resolve().parents[1]/'computations/geometry_20261114_separated_qr_bvp.py'
    dependencies['geometry_20261114_separated_qr_bvp.py']=hashlib.sha256(qr_path.read_bytes()).hexdigest()
    initial_seed=None
    if a.material_input and a.input:raise ValueError('Choose either a physical accepted input or an explicit material initializer')
    if a.material_input:
        seedraw=a.material_input.read_bytes();old=json.loads(gzip.decompress(seedraw))
        if not old['success'] or old['background_sha256']!=bg.sha256 or old['coordinate']!=a.coordinate:raise ValueError('Material seed must be an accepted same-background same-coordinate field')
        if old.get('angular_chart')=='fixed physical phi' or 'rho_cos_coefficients' in old:raise ValueError('The material initializer must actually use the material angle')
        x=np.array(old['mesh']);source=np.array(old['states']).T;M0=old['M']
        rho=np.array(trace['rho_cos_coefficients']);rf=2*np.arange(1,len(rho)+1)
        theta=q.angle+np.sin(q.angle[:,None]*rf[None,:])@(rho/rf)
        mf=2*np.arange(1,M0+1);SM=np.sin(theta[:,None]*mf);CM=np.cos(theta[:,None]*mf)
        Pmap=(2/q.N)*(q.S.T@(q.R*SM));Kmap=(2/q.N)*(q.C.T@CM);cmap=np.mean(CM,axis=0)
        ratio=a.scale/old['scale'];y=np.zeros((q.n,len(x)))
        y[:q.M]=ratio*(Pmap@source[:M0]);y[q.M:2*q.M]=ratio*(Kmap@source[M0:2*M0])
        y[-1]=ratio*(source[-1]+cmap@source[M0:2*M0])
        sample=np.array([0,len(x)//2,len(x)-1]);pr=ratio*(q.R*(SM@source[:M0,sample]));kr=ratio*(CM@source[M0:2*M0,sample]+source[-1,sample])
        initial_seed=dict(kind='unaccepted material-to-physical projected initializer',input_sha256=hashlib.sha256(seedraw).hexdigest(),input_M=M0,input_scale=old['scale'],target_scale=a.scale,angular_samples=q.N,
                          Ptilde_three_point_projection_max=float(np.max(abs(q.S@y[:q.M,sample]-pr))),K_three_point_projection_max=float(np.max(abs(q.C@y[q.M:2*q.M,sample]+y[-1,sample]-kr))))
    elif a.input:
        old=json.loads(gzip.decompress(a.input.read_bytes()))
        if not old['success'] or old['background_sha256']!=bg.sha256 or old['coordinate']!=a.coordinate:raise ValueError('Need accepted same-background same-coordinate input')
        x=np.array(old['mesh']);yy=np.array(old['states']).T;y=np.zeros((q.n,len(x)))
        k=min(q.M,old['M']);y[:k]=yy[:k];y[q.M:q.M+k]=yy[old['M']:old['M']+k];y[-1]=yy[-1]
        y*=a.scale/old['scale']
    else:
        selected=sorted(set([0,len(bg.r)-1]+[i for i,r in enumerate(bg.rows) if i%a.mesh_stride==0 or r['x'] in (0,1)]))
        x=bg.x[selected];y=np.zeros((q.n,len(x)));y[:q.M]=target[:,None]
        y[q.M:2*q.M]=a.scale*np.array(trace['K_cos_coefficients'][:q.M])[:,None]
        y[-1]=a.scale*a.scale*trace['K_mean']
    left,right=bg.x[[0,-1]];counts=dict(fun=0,jac=0)
    def fun(x,y):
        counts['fun']+=1;out=np.empty_like(y)
        for i in range(0,len(x),a.batch):
            sl=slice(i,i+a.batch)
            try:out[:,sl]=q.evaluate(y[:,sl],*bg(x[sl]))
            except FloatingPointError:out[:,sl]=np.nan
        return out
    def fjac(x,y):
        counts['jac']+=1;out=np.empty((q.n,q.n,len(x)))
        for i in range(0,len(x),a.batch):
            sl=slice(i,i+a.batch);out[:,:,sl]=q.jacobian(y[:,sl],*bg(x[sl]))
        return out
    def bc(ya,yb):
        _,d=q.evaluate(ya[:,None],*bg(np.array([left])),True)
        return np.r_[ya[:q.M]-target,d['mean'][0],bp@yb[:q.M]+bk@yb[q.M:2*q.M]]
    def bj(ya,yb):
        A=np.zeros((q.n,q.n));B=np.zeros_like(A);ii=np.arange(q.M)
        A[ii,ii]=1;B[q.M+1:,:q.M]=bp;B[q.M+1:,q.M:2*q.M]=bk;h=1e-25
        for j in range(q.n):
            v=ya.astype(complex);v[j]+=1j*h;A[q.M,j]=bc(v,yb)[q.M].imag/h
        return A,B
    import scipy.integrate._bvp as backend
    spec=importlib.util.spec_from_file_location('parallel_tail_existing_qr',qr_path)
    qr=importlib.util.module_from_spec(spec);spec.loader.exec_module(qr)
    qr.enable(a.out.with_suffix('.qr-work'),q.M+1,chunk_size=a.batch,checkpoint=str(a.out)+'.checkpoint.gz',M=q.M,N=q.N)
    backend.splu=qr.factor
    backend.solve_newton=feasible_newton
    print(json.dumps(dict(event='start',M=q.M,N=q.N,scale=a.scale,nodes=len(x),r_shallow=float(bg.r[0]),r_deep=float(bg.r[-1]))),flush=True)
    sol=solve_bvp(fun,bc,x,y,fun_jac=fjac,bc_jac=bj,tol=a.tol,bc_tol=1e-11,max_nodes=a.max_nodes,verbose=2)
    audit={k:0. for k in ('max_mean','max_P','max_K','max_eta_radial','max_full_P_radial_residual','max_full_K_radial_residual','max_relative_radial_coefficient_residual')}
    for key in ('D','S','L','y','N'):audit['min_'+key]=float('inf')
    for i in range(0,len(sol.x)-1,32):
        le=sol.x[i:min(i+32,len(sol.x)-1)];ri=sol.x[i+1:min(i+32,len(sol.x)-1)+1]
        xx=np.ravel(le[:,None]+(ri-le)[:,None]*np.linspace(0,1,5));yy=sol.sol(xx);yp=sol.sol(xx,1)
        rhs,d=q.evaluate(yy,*bg(xx),True);_,rx=bg.radial(xx)
        rawp=q.S@rhs[:q.M]-d['pde_p_residual']
        vals={'max_mean':np.max(abs(d['mean'])),'max_P':np.max(abs(d['P'])),'max_K':np.max(abs(d['K'])),
              'max_eta_radial':np.max(abs(d['eta']/rx)),
              'max_full_P_radial_residual':np.max(abs((q.S@yp[:q.M]-rawp)/(rx*q.R))),
              'max_full_K_radial_residual':np.max(abs((q.C@yp[q.M:2*q.M]+yp[-1]-d['raw_k'])/rx)),
              'max_relative_radial_coefficient_residual':np.max(abs((yp-rhs)/rx)/(1+abs(rhs/rx)))}
        for key,val in vals.items():audit[key]=max(audit[key],float(val))
        for key in ('D','S','L','y','N'):audit['min_'+key]=min(audit['min_'+key],float(np.min(d[key])))
    cut=sol.y[:,0];reference=np.r_[a.scale*np.array(trace['K_cos_coefficients'][:q.M]),a.scale*a.scale*trace['K_mean']]
    mismatch=cut[q.M:]-reference
    report=dict(scope=__doc__,success=bool(sol.success),status=int(sol.status),message=sol.message,M=q.M,N=q.N,scale=a.scale,
                background_sha256=bg.sha256,trace_sha256=hashlib.sha256(trace_raw).hexdigest(),source_sha256=source_sha,
                operator_source_sha256=dependencies['parallel_20261117_weighted_tail.py'],dependency_sha256_at_start=dependencies,
                initial_seed=initial_seed,linear_solver='existing separated QR',left_boundary_rows=q.M+1,deep_columns_sha256=deep_sha,fast_jacobian=a.fast_jacobian,allow_height_turn=a.allow_height_turn,height_mean_anchor=trace['height_mean'],
                coordinate=a.coordinate,angular_chart='fixed physical phi',deep_boundary=deep_boundary,rho_cos_coefficients=trace['rho_cos_coefficients'],seconds=time.perf_counter()-started,counts=counts,nodes=len(sol.x),
                collocation_rms_max=float(np.max(sol.rms_residuals)),boundary_residual_max=float(np.max(abs(bc(sol.y[:,0],sol.y[:,-1])))),
                cut_P_coefficients=cut[:q.M].tolist(),cut_K_coefficients=cut[q.M:2*q.M].tolist(),cut_K_mean=float(cut[-1]),
                cut_K_coefficient_mismatch=float(np.max(abs(mismatch))),cut_K_sampled_mismatch=float(np.max(abs(q.C@mismatch[:-1]+mismatch[-1]))),
                mesh=sol.x.tolist(),radial_mesh=bg.radial(sol.x)[0].tolist(),states=sol.y.T.tolist(),rhs=fun(sol.x,sol.y).T.tolist(),audit=audit)
    a.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
    print(json.dumps({k:v for k,v in report.items() if k not in ('scope','mesh','radial_mesh','states','rhs','cut_P_coefficients','cut_K_coefficients','rho_cos_coefficients','deep_boundary')}),flush=True)
    print(json.dumps(dict(output_sha256=hashlib.sha256(a.out.read_bytes()).hexdigest())),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--background',type=Path,required=True);p.add_argument('--trace',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--input',type=Path);p.add_argument('--material-input',type=Path);p.add_argument('--modes',type=int,default=8)
    p.add_argument('--angles',type=int,default=512);p.add_argument('--scale',type=float,default=.01);p.add_argument('--tol',type=float,default=1e-6)
    p.add_argument('--max-nodes',type=int,default=12000);p.add_argument('--mesh-stride',type=int,default=1);p.add_argument('--batch',type=int,default=64)
    p.add_argument('--deep-columns',type=Path);p.add_argument('--allow-height-turn',action='store_true');p.add_argument('--fast-jacobian',action='store_true')
    p.add_argument('--coordinate',choices=['source-index','physical-r'],default='source-index');main(p.parse_args())
