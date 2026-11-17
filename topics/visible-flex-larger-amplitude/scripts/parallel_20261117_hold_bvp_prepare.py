#!/usr/bin/env python3
"""Prepare, but do not solve, the full M160 HoldProfile BVP to 1.04.

The true old prefix and successful type-interface IVP define a common-jet
R637 bridge, then a linear Fourier projection supplies a new finite warm
field. Only beyond the type interface is the explicit quadratic endpoint
jet used. Frozen terminal moving-frame Schur rows retain their nonzero
Taylor reference target; no Fourier mode or ODE row is removed.
Only tail cells with invalid actual collocation midpoints are bisected,
recursively within the original 1800-node budget. The quadratic reference
and terminal target do not change. This is initial-mesh preparation only.
"""
import argparse,gzip,hashlib,importlib.util,json,tempfile,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigvals,solve,svdvals
import parallel_20261117_frenet_symbol as fs
from parallel_20261117_profile import Profile

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def project(v,old,M):
 v=np.asarray(v);m=min(old,M);z=np.zeros((*v.shape[:-1],3*M+2));z[...,:m+1]=v[...,:m+1]
 z[...,M+1:M+m+1]=v[...,old+1:old+m+1];z[...,2*M+1:2*M+m+2]=v[...,2*old+1:2*old+m+2];return z
def coefficients(y,v,acc,h):
 c0=y[0];c1=h*v[0];c2=h*h*acc[0]/2;a=y[1]-c0-c1-c2;b=h*v[1]-c1-2*c2;c=h*h*acc[1]-2*c2
 return np.array([c0,c1,c2,10*a-4*b+c/2,-15*a+7*b-c,6*a-3*b+c/2])
def evaluate(co,u,h):
 return (np.polynomial.polynomial.polyval(u,co),np.polynomial.polynomial.polyval(u,np.arange(1,6)[:,None]*co[1:])/h,
  np.polynomial.polynomial.polyval(u,(np.arange(2,6)*np.arange(1,5))[:,None]*co[2:])/(h*h))

def main(a):
 started=time.perf_counter();p=json.loads(gzip.decompress(a.parent.read_bytes()));d=json.loads(gzip.decompress(a.interface.read_bytes()))
 if not p.get('success') or not d.get('ivp_reached_end') or d.get('old_prefix_C2_join_completed') or d['reference_sha256']!=sha(a.parent):raise ValueError('Require the actual old parent and its successful unmodified interface')
 if d['hold_profile_sha256']!=sha(a.hold_source):raise ValueError('Scalar source changed')
 scalar=load(a.hold_source,'prep_hold_scalar');profile=scalar.HoldProfile(p['fixed_scalar_profile']['geometry'],p['analytic_extension_origin'])
 if profile.spec()!=d['hold_scalar_profile']:raise ValueError('Different HoldProfile')
 M,N,free,left=160,2048,157,325;q=fs.Frenet(M,N);audit=fs.Frenet(M,8192);old=fs.Frenet(p['M'],p['N']);base=Profile(p['fixed_scalar_profile']['geometry'],p['analytic_extension_origin'])
 px=np.array(p['mesh']);py=np.array(p['states']);pv=np.array(p['rhs']);pa=[]
 for s,y,v in zip(px,py,pv):
  r,ap,app=base(s);k=ap/r;pa.append(old.jvp(y,k,v,dk=app/r-k*k))
 PY,PV,PA=[project(z,p['M'],M)for z in (py,pv,pa)];x=np.array(d['mesh']);Y,V,A=[project(d[key],d['M'],M)for key in ('states','rhs','d2')]
 if x[0]!=px[-1] or not np.array_equal(Y[0],PY[-1]):raise ValueError('Different true cut')
 dv=V[0]-PV[-1];da=A[0]-PA[-1];w=x[32]-x[0];p1=np.array([0,1,0,-6,8,-3.]);p2=np.array([0,0,.5,-1.5,1.5,-.5]);ev=np.polynomial.polynomial.polyval
 for j in range(1,32):
  u=(x[j]-x[0])/w;Y[j]-=w*ev(u,p1)*dv+w*w*ev(u,p2)*da
  V[j]-=ev(u,np.arange(1,6)*p1[1:])*dv+w*ev(u,np.arange(1,6)*p2[1:])*da
  A[j]-=ev(u,np.arange(2,6)*np.arange(1,5)*p1[2:])*dv/w+ev(u,np.arange(2,6)*np.arange(1,5)*p2[2:])*da
 Y[0]=PY[-1];V[0]=PV[-1];A[0]=PA[-1]
 cutjet=[float(np.max(abs(z[-1]-b[0])))for z,b in zip((PY,PV,PA),(Y,V,A))]
 X=np.r_[px,x[1:]];Y,V,A=[np.r_[z,b[1:]]for z,b in zip((PY,PV,PA),(Y,V,A))];end=1.04;interface=float(X[-1]);ye,ve,ae=Y[-1].copy(),V[-1].copy(),A[-1].copy()
 def reference(s):
  if s>interface:
   t=s-interface;return ye+t*ve+.5*t*t*ae,ve+t*ae,ae
  j=int(np.searchsorted(X,s))
  if j<len(X) and X[j]==s:return Y[j],V[j],A[j]
  j=max(0,min(len(X)-2,j-1));h=X[j+1]-X[j];return evaluate(coefficients(Y[j:j+2],V[j:j+2],A[j:j+2],h),(s-X[j])/h,h)
 # All 499 old nodes are retained; the local reference is explicitly resampled.
 mesh=np.unique(np.r_[px,np.linspace(x[0],interface,81)[1:],np.linspace(interface,end,21)[1:],x[32],.997,1.017,1.037])
 layers=[];stop_reason=None
 def values(y,s):
  r,ap,_=profile(float(s));_,dt,dd=audit.jet(y);Q=np.sum(dt*dt,axis=1);W=np.sum(np.cross(dt,dd)**2,axis=1);H=W-(ap/r)**2*Q**3
  return [float(v.min())for v in (Q,W,H)]
 while True:
  samples=[reference(float(s))for s in mesh];yy=np.array([v[0]for v in samples]);vv=np.array([v[1]for v in samples]);ff=[];node_min=np.full(3,np.inf);bad_node=[]
  for j,(s,y)in enumerate(zip(mesh,yy)):
   nodal=values(y,s);node_min=np.minimum(node_min,nodal);r,ap,_=profile(float(s))
   if min(nodal)<=0:bad_node.append(j)
   try:ff.append(q.rhs(y,ap/r))
   except FloatingPointError:ff.append(np.full(q.n,np.nan));bad_node.append(j)
  ff=np.array(ff);difference=vv-ff;relative=difference/(1+abs(ff));bad_cell=[];mid_min=np.full(3,np.inf)
  if not bad_node:
   for i,h in enumerate(np.diff(mesh)):
    s=float((mesh[i]+mesh[i+1])/2);ym=(yy[i]+yy[i+1])/2-h*(ff[i+1]-ff[i])/8;val=values(ym,s);mid_min=np.minimum(mid_min,val)
    if min(val)<=0:bad_cell.append(i)
  row=dict(layer=len(layers),nodes=len(mesh),invalid_node_indices=sorted(set(bad_node)),invalid_collocation_cells=bad_cell,
   node_QWH_lower=node_min.tolist(),collocation_midpoint_QWH_lower=mid_min.tolist(),
   node_full_ODE_coefficient_defect=float(np.max(abs(difference))),node_full_ODE_relative_defect=float(np.max(abs(relative))),
   node_full_ODE_relative_vector_rms=float(np.sqrt(np.mean(relative*relative,axis=1)).max()))
  layers.append(row);print(json.dumps(dict(event='tail_mesh_preparation',**row)),flush=True)
  if bad_node:stop_reason='An unchanged reference node is outside the actual angular domain';break
  if not bad_cell:stop_reason='All actual collocation midpoints are admissible on the audit grid';break
  if any(mesh[j]<interface for j in bad_cell):stop_reason='A bad collocation cell is outside the authorized quadratic tail';break
  if len(mesh)+len(bad_cell)>1800:stop_reason='The next complete bad-cell bisection exceeds the original 1800-node budget';break
  mesh=np.unique(np.r_[mesh,[(mesh[j]+mesh[j+1])/2 for j in bad_cell]])
 jets=[reference(float(s))for s in mesh];WY,WV,WA=[np.array([z[k]for z in jets])for k in range(3)];nodes=len(mesh)
 minima={k:dict(value=np.inf)for k in ('Q','W','H')};bad=[];defect=dict(coefficient_max=0.,relative_component_max=0.,relative_vector_rms_max=0.)
 def domain(qq,y,s,kind):
  r,ap,_=profile(float(s));_,dt,dd=qq.jet(y);Q=np.sum(dt*dt,axis=1);W=np.sum(np.cross(dt,dd)**2,axis=1);H=W-(ap/r)**2*Q**3
  for key,value in zip(('Q','W','H'),(Q,W,H)):
   j=int(np.argmin(value));v=float(value[j])
   if v<minima[key]['value']:minima[key]=dict(value=v,s=float(s),angle=float(qq.angle[j]),N=qq.N,kind=kind)
  good=min(Q.min(),W.min(),H.min())>0
  if not good:bad.append(dict(s=float(s),N=qq.N,kind=kind,Q=float(Q.min()),W=float(W.min()),H=float(H.min())))
  return bool(good)
 for i,h in enumerate(np.diff(mesh)):
  co=coefficients(WY[i:i+2],WV[i:i+2],WA[i:i+2],h)
  for j in range(5):
   if i and j==0:continue
   u=j/4;s=float(mesh[i]+u*h)
   yy,dy,_=(WY[i],WV[i],WA[i])if j==0 else ((WY[i+1],WV[i+1],WA[i+1])if j==4 else evaluate(co,u,h))
   if domain(audit,yy,s,'declared_warm_quintic'):
    r,ap,_=profile(s)
    try:f=q.rhs(yy,ap/r)
    except FloatingPointError:domain(q,yy,s,'RHS_grid_failure');continue
    rr=dy-f;relative=rr/(1+abs(f))
    for key,value in (('coefficient_max',max(abs(rr))),('relative_component_max',max(abs(relative))),('relative_vector_rms_max',np.sqrt(np.mean(relative*relative)))):
     if value>defect[key]:defect[key]=float(value);defect[key+'_s']=s
  if (i+1)%100==0:print(json.dumps(dict(event='warm_cells',count=i+1,total=nodes-1,Hmin=minima['H']['value'])),flush=True)
 F=[]
 for s,y in zip(mesh,WY):
  r,ap,_=profile(float(s))
  try:F.append(q.rhs(y,ap/r))
  except FloatingPointError:F.append(np.full(q.n,np.nan))
 F=np.array(F);collocation=dict(max_coefficient=np.inf,max_per_length=np.inf,max_relative_per_length=np.inf,finite=False)
 midpoints=[]
 if np.isfinite(F).all():
  maxima=np.zeros(3)
  for i,h in enumerate(np.diff(mesh)):
   s=float((mesh[i]+mesh[i+1])/2);yy=(WY[i]+WY[i+1])/2-h*(F[i+1]-F[i])/8;midpoints.append(yy)
   if not domain(audit,yy,s,'complete_collocation_midpoint'):continue
   r,ap,_=profile(s);fm=q.rhs(yy,ap/r);res=WY[i+1]-WY[i]-h*(F[i]+F[i+1]+4*fm)/6
   maxima=np.maximum(maxima,[max(abs(res)),max(abs(res/h)),max(abs(res/h)/(1+abs(fm)))])
  collocation=dict(max_coefficient=float(maxima[0]),max_per_length=float(maxima[1]),max_relative_per_length=float(maxima[2]),finite=not bad)
 BA=np.zeros((q.n,q.n));BB=np.zeros_like(BA);target=np.zeros(q.n);BA[0,0]=1;target[0]=1
 for j in range(3):BA[1+j,1+j]=1;target[1+j]=p['core']['coefficients'][j]
 for j in range(M):BA[4+j,1+j]=q.freq[j+1];BA[4+j,M+1+j]=1
 BA[4+M:left,2*M+1:]=np.eye(M+1)
 schur_record={};benchmark={};prepared=False;L=np.zeros((free,q.n));ref=reference(end)[0];array_values={}
 helper_path=a.topic/'notes/2026-11-17-parallel-geometry-frenet-schur.py';qr_path=a.topic/'computations/geometry_20261114_separated_qr_bvp.py'
 if min(values(ref,end))>0:
  helper=load(helper_path,'prep_complete_moving_schur');begin=time.perf_counter();z=helper.physical(q,ref,profile,end);terminal_physical_seconds=time.perf_counter()-begin
  T,Ts=helper.moving_frame_map(q,z);B=solve(T.T,(T@z['J']+Ts).T).T;re=np.sort(eigvals(B).real);lo,hi=float(re[-free-1]),float(re[-free]);threshold=(lo+hi)/2
  schur_record=dict(reference_time=end,reference='Explicit degree-two continuation of the saved true interface 0/1/2 jets, then projection to M160',lower=lo,upper=hi,gap=hi-lo,threshold=threshold,T_condition_2=float(np.linalg.cond(T)))
  if hi-lo>1e-8:
   info,LB=helper.selected_left(B,lambda v:v>threshold,M,None);schur_record['selected']={k:v for k,v in info.items()if k!='modal_energy'}
   if info['dimension']==free:
    L=LB@T;BB[left:]=L;target[left:]=L@ref;schur_record.update(rows_condition_2=float(np.linalg.cond(L)),right_reference_target_max=float(max(abs(target[left:]))),right_reference_target_norm=float(np.linalg.norm(target[left:])))
    prepared=True;array_values=dict(terminal_frame=T,terminal_frame_s=Ts,terminal_moving_B=B,terminal_J=z['J'])
  # A single representative cell measures cost only. No complete QR or Newton solve.
  if prepared:
   qr=load(qr_path,'prep_single_qr_cost');j=max(0,int(np.searchsorted(mesh,.5))-1);h=mesh[j+1]-mesh[j];smid=float((mesh[j]+mesh[j+1])/2);jm=[];jt=[]
   for s,y in ((mesh[j],WY[j]),(smid,midpoints[j]),(mesh[j+1],WY[j+1])):
    r,ap,_=profile(float(s));begin=time.perf_counter();jm.append(q.jacobian(y,ap/r));jt.append(time.perf_counter()-begin)
   begin=time.perf_counter();bl,br=qr.local_blocks(h,*jm);block_seconds=time.perf_counter()-begin
   with tempfile.TemporaryDirectory(prefix='parallel-hold-qr-cost-',dir=a.out.parent)as work:
    begin=time.perf_counter();factor=qr.DiskQRFactor(q.n,2,BA,BB,left,work);initial_qr_seconds=time.perf_counter()-begin
    begin=time.perf_counter();factor.append(0,bl,br);append_seconds=time.perf_counter()-begin;disk_bytes=(factor.directory/'00000.npz').stat().st_size;factor.close()
   jac_time=float(np.median(jt));persistent=8*(nodes*q.n*free+(nodes-1)*free*free+nodes*q.n+(nodes-1)*free)
   benchmark=dict(representative_cell=j,representative_interval=[float(mesh[j]),float(mesh[j+1])],terminal_physical_seconds=terminal_physical_seconds,jacobian_three_seconds=jt,jacobian_median_seconds=jac_time,local_block_seconds=block_seconds,one_disk_append_seconds=append_seconds,
    initial_left_QR_seconds=initial_qr_seconds,one_interval_disk_bytes=disk_bytes,estimated_complete_factor_seconds=(2*nodes-1)*jac_time+(nodes-1)*(block_seconds+append_seconds)+initial_qr_seconds,
    estimated_factor_disk_bytes=(nodes-1)*disk_bytes,persistent_QR_arrays_bytes=persistent,chunk32_jacobian_arrays_bytes=8*q.n*q.n*65,
    complete_QR_performed=False,Newton_performed=False)
 boundary_residual=BA@WY[0]+BB@WY[-1]-target
 warm=dict(schema='hold-M160-full-BVP-preparation-v1',scope=__doc__,success=False,bvp_solved=False,preparation_only=True,prepared=prepared and not bad,
  source_sha256=sha(__file__),parent_sha256=sha(a.parent),interface_sha256=sha(a.interface),hold_profile_sha256=sha(a.hold_source),fixed_scalar_profile=p['fixed_scalar_profile'],analytic_extension_origin=p['analytic_extension_origin'],hold_scalar_profile=profile.spec(),
  M=M,N=N,mesh=mesh.tolist(),states=WY.tolist(),warm_quintic_first=WV.tolist(),warm_quintic_second=WA.tolist(),full_ode_rhs_at_nodes=F.tolist(),
  left_count=left,right_count=free,fixed_core_first_three=p['core']['coefficients'][:3],terminal_rows=L.tolist(),terminal_target=target[left:].tolist(),terminal_reference=ref.tolist(),
  tail_mesh_preparation=layers,tail_mesh_stop_reason=stop_reason,
  warm_definition='Retain all original prefix nodes; local uniform81 plus32-node bridge endpoint and scalar breaks; quadratic reference only after the type interface; bisect only bad actual collocation tail cells up to1800 nodes; all sampled jets define the new common quintic. Not refinement or an accepted parent.')
 a.warm.write_bytes(gzip.compress((json.dumps(warm)+'\n').encode(),mtime=0));np.savez_compressed(a.arrays,BA=BA,BB=BB,target=target,terminal_reference=ref,**array_values)
 report=dict(scope=__doc__,source_sha256=sha(__file__),parent_sha256=sha(a.parent),interface_sha256=sha(a.interface),hold_profile_sha256=sha(a.hold_source),frenet_sha256=sha(fs.__file__),
  schur_helper_sha256=sha(helper_path),QR_helper_sha256=sha(qr_path),warm_sha256=sha(a.warm),arrays_sha256=sha(a.arrays),M=M,N=N,dimension=q.n,left_count=left,right_count=free,
  nodes=nodes,start=float(mesh[0]),end=float(mesh[-1]),true_interface=interface,extrapolated_duration=end-interface,common_cut_jet_differences=cutjet,tail_mesh_preparation=layers,tail_mesh_stop_reason=stop_reason,
  domain_sample_grid=8192,radial_subdivisions=4,domain_minima=minima,invalid_samples=bad,full_warm_ODE_defect=defect,full_collocation_defect=collocation,
  left_matrix_rank=int(np.linalg.matrix_rank(BA[:left])),boundary_residual_max=float(max(abs(boundary_residual))),pure_separated_rows=bool(not np.any(BA[left:])and not np.any(BB[:left])),
  terminal_schur=schur_record,QR_cost_estimate=benchmark,preparation_gates_passed=prepared and not bad,BVP_solved=False,seconds=time.perf_counter()-started,
  limitations='The down-projected/resampled/extrapolated warm field is not a refinement or an accepted parent. Domain extrema are sampled, not interval-certified. Instantaneous frozen Schur rows with nonzero reference target are a new finite boundary, not a nonlinear DN map. No global Jacobian condition or Newton success is asserted.')
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True);print(json.dumps(dict(output_sha256=sha(a.out))),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','parent','interface','hold-source','warm','arrays','out'):p.add_argument('--'+key,type=Path,required=True)
 main(p.parse_args())
