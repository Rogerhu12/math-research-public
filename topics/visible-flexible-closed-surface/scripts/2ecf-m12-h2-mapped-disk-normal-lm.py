#!/usr/bin/env python3
"""Disk-streamed original physical normal and one-band complete M12 Gram direct LM with an explicit H2 step penalty.

The nonlinear objective is the original complete fixed-g Gram energy. H2 is
only the norm of the proposed increment, never a penalty on the target field.
Every direction solves (J^T J + lambda*S2)d = -J^T r. All Fourier cross terms
are retained by the existing complete-Gram assembly. C2 step control, actual
normal residuals, true nonlinear observations and source identities are saved.
"""
from __future__ import annotations
import argparse,gc,hashlib,importlib.util,json,math,resource,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.linalg import cholesky_banded,cho_solve_banded

HERE=Path(__file__).resolve().parent

def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def save(p,x):Path(p).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')

def h2_bands(linear):
 """Fixed-chart integral of |dss|^2+2|dsθ|^2+|dθθ|^2+|ds|^2+|dθ|^2+.01|d|^2.

 Actual material ds and uniform angular dθ/(2π) are used. Planar complex
 columns have norm one; nonconstant vertical cosines have norm 1/2.
 No original-g residual row is removed or modified by this increment norm.
 """
 B=linear.B0,linear.B1,linear.B2;w=linear.weights;nb=linear.basis.nb
 bands=[]
 for mat in B:
  gram=(mat.T@mat.multiply(w[:,None])).tocsr()
  if gram.nnz and np.max(abs(gram.tocoo().row-gram.tocoo().col))>5:raise ArithmeticError('Unexpected H2 bandwidth')
  bands.append(np.array([np.pad(gram.diagonal(-j),(0,j)) for j in range(6)]))
 result=[]
 for a,k in enumerate(linear.basis.modes):
  k=float(k);norm=1. if a<len(linear.basis.pm) or k==0 else .5
  result.append(norm*(bands[2]+(2*k*k+1)*bands[1]+(k**4+k*k+.01)*bands[0]))
 return np.asarray(result)

def apply_h2(bands,coeff):
 x=np.asarray(coeff);out=np.zeros_like(x);nb,nc=x.shape
 for a in range(nc):
  for d in range(min(5,nb-1)+1):
   v=bands[a,d,:nb-d]
   out[d:,a]+=v*x[:nb-d,a]
   if d:out[:nb-d,a]+=v*x[d:,a]
 return out

def add_h2(packed,bands,lam):
 nb=packed.shape[1]//len(bands);nc=len(bands)
 for d in range(min(5,nb-1)+1):
  ids=(np.arange(nb-d)[:,None]*nc+np.arange(nc)[None,:]).ravel()
  packed[d*nc,ids]+=lam*bands[:,d,:nb-d].T.ravel()

def raw_ops(normal,linear):
 obj=SimpleNamespace(linear=linear,basis=linear.basis)
 return (lambda c:normal.CompleteGramRightPreconditioned.raw_matvec(obj,c),
         lambda v:normal.CompleteGramRightPreconditioned.raw_transpose(obj,v))

def derivative_control_bounds(basis,coeff,total):
 """Conservative binary64 screening only; exact R226 is run separately."""
 c=np.pad(np.asarray(coeff),((3,3),(0,0)));knots=basis.knots.copy();degree=5
 modes=np.asarray(abs(basis.modes),float);raw={}
 for d in range(3):
  for j in range(3-d):raw[d,j]=float(np.max(np.sum(abs(c)*modes[None,:]**j,axis=1)))
  if d<2:
   den=knots[degree+1:-1]-knots[1:-degree-1]
   c=degree*np.diff(c,axis=0)/den[:,None];knots=knots[1:-1];degree-=1
 H=.684;Hq=60.;cuff=.15
 ws=raw[1,0]/(total*H);wt=raw[0,1]
 wss=raw[2,0]/(total**2*H**2)+Hq*raw[1,0]/(total*H**3)
 wst=raw[1,1]/(total*H);wtt=raw[0,2]
 return {'native_six_jet_screen':{str(k):v for k,v in raw.items()},'position':raw[0,0],
         'fixed_chart_first_screen':ws+wt/cuff,'fixed_chart_second_screen':wss+2*wst/cuff+wtt/cuff**2,
         'screen_only_not_an_outward_rounded_certificate':True}

def factor_solve(H,S,lam,gradient):
 began=time.monotonic()
 if not H.flags.f_contiguous or H.dtype!=np.float64:raise ValueError('One owned Fortran binary64 Gram band is required')
 p=H;add_h2(p,S,lam)
 diag=p[0].copy()
 if np.any(diag<=0) or not np.all(np.isfinite(diag)):raise ArithmeticError('Nonpositive regularized normal diagonal')
 scale=1/np.sqrt(diag);n=len(scale)
 for left in range(0,n,2048):
  right=min(n,left+2048)
  for d in range(p.shape[0]):
   stop=min(right,n-d)
   if stop>left:p[d,left:stop]*=scale[left+d:stop+d]*scale[left:stop]
  p.flush();p._mmap.madvise(__import__('mmap').MADV_DONTNEED)
 factor=cholesky_banded(p,lower=True,overwrite_ab=True,check_finite=False)
 if factor.ctypes.data!=p.ctypes.data:raise ArithmeticError('The actual H2 Cholesky allocated a second band')
 rhs=-scale*gradient.ravel();direction=scale*cho_solve_banded((factor,True),rhs,check_finite=False)
 return direction.reshape(gradient.shape),factor,scale,{'lambda_step':float(lam),'factorization_seconds':time.monotonic()-began,
      'factor_bytes':factor.nbytes,'physical_Gram_band_consumed_inplace':True,'factor_shares_original_band_storage':True,'minimum_diagonal':float(diag.min()),'maximum_diagonal':float(diag.max())}

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for name in ('scripts','data','grid','query-report','query-cache','initial-field','initial-result','out'):
  ap.add_argument('--'+name,type=Path,required=True)
 ap.add_argument('--lambda-step',type=float,default=1e-12)
 ap.add_argument('--lambda-retries',type=int,default=4)
 ap.add_argument('--steps',type=int,default=1)
 ap.add_argument('--block',type=int,default=24)
 ap.add_argument('--normal-assembly-block',type=int,default=8)
 ap.add_argument('--hessian-step-cap',type=float,default=.05)
 ap.add_argument('--gradient-tolerance',type=float,default=1e-8)
 ap.add_argument('--observe-angular-factor',type=int,default=2)
 args=ap.parse_args();began=time.monotonic()
 if args.out.exists() or Path(str(args.out)+'.field.npz').exists():raise FileExistsError('Fresh complete LM output required')
 if not math.isfinite(args.lambda_step) or args.lambda_step<=0:raise ValueError('Positive step regularization required')
 core=load('m12_original_warm_core',args.scripts/'6a65-m12-entire-half-cartesian-warm-refinement.py')
 joint=core.load('m12_h2_original_joint',args.scripts/'6a65-m12-global-common-cut-position-recovered.py')
 bg=core.load('m12_h2_original_background',args.scripts/'6a65-m12-original-tail-background.py')
 normal=load('m12_h2_complete_normal',args.scripts/'6a65-m12-complete-gram-normal-preconditioner.py')
 __import__('os').environ['M12_BAND_DIR']=str(args.out.parent)
 assembly_module=load('m12_complete_Gram_assembly_only',HERE/'2ecf-m12-complete-gram-mapped-assembly-only.py')
 physical=load('m12_disk_physical_linearization',HERE/'2ecf-m12-disk-physical-linearization.py');physical_storage=[]
 grid=read(args.grid);args.background_tolerance=grid['background_tolerance']
 notes,meta_path,bridge_path,meta,native,chart=core.definition(args,joint,bg)
 for k,p in [('data_sha256',args.data),('common_meta_sha256',meta_path),('bridge_sha256',bridge_path),('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(bg.__file__))]:
  if grid[k]!=sha(p):raise ValueError('Changed source '+k)
 tail=core.TailQueries(args.query_report,args.query_cache)
 if tail.record['query_file_sha256']!=grid['query_file_sha256']:raise ValueError('Query recipe changed')
 src=joint.CommonCutSource(args.data,meta_path,bridge_path,args.query_report,args.query_cache)
 unused,central_c=joint.ad.exact_section(args.data,core.Q(0));central=joint.ad.NativeCurve(central_c,512,32)
 position=core.WholePosition(src,central,chart,tail,joint)
 mesh=np.asarray(grid['unit_mesh']);order,N,gauss=grid['order'],grid['angular'],grid['gauss']
 basis=core.basis_for(joint,mesh,order,chart);z,w=core.quadrature(mesh,gauss,chart)
 old=read(args.initial_result)
 if old['field_sha256']!=sha(args.initial_field) or old['grid_sha256']!=sha(args.grid):raise ValueError('Actual initial field identity changed')
 with np.load(args.initial_field,allow_pickle=False) as f:
  coeff=f['coefficients'].copy()
  for key,value in [('unit_knots',basis.knots),('planar_modes',basis.pm),('vertical_modes',basis.zm)]:
   if not np.array_equal(f[key],value):raise ValueError('Actual initial basis changed: '+key)
 if coeff.shape!=(basis.nb,basis.na) or coeff.dtype!=np.float64:raise ValueError('Whole actual initial field required')
 initial=coeff.copy();rows=[];stream=joint.stream;initial_training=None
 for step in range(args.steps):
  print(json.dumps({'stage':'actual-full-H2-LM-step','step':step,'initial_field_sha256':sha(args.initial_field),'unknowns':coeff.size}),flush=True)
  linear=physical.build_linearized(stream,basis,z,w,position,coeff,N,args.block,directory=args.out.parent)
  if initial_training is None:initial_training=linear.statistics
  gradient=physical.initial_gradient(linear);gnorm=float(np.linalg.norm(gradient))
  print(json.dumps({'stage':'actual-linearization-complete','resident':assembly_module.resident(),'original_physical_gradient_norm':gnorm}),flush=True)
  assemble=assembly_module.CompleteGramNormalAssemblyOnly(linear,1e-6,args.scripts/'6a65-cartesian-complete-radial-normal.py',args.normal_assembly_block)
  H=assemble.normal_band;assembly=assemble.receipt;reassemblies=[];gc.collect()
  S=h2_bands(linear);attempts=[];accepted=None
  for trial in range(args.lambda_retries):
   lam=args.lambda_step*10**trial
   if trial:
    H=None;assemble=None;gc.collect()
    assemble=assembly_module.CompleteGramNormalAssemblyOnly(linear,1e-6,args.scripts/'6a65-cartesian-complete-radial-normal.py',args.normal_assembly_block)
    H=assemble.normal_band;reassemblies.append(assemble.receipt)
   print(json.dumps({'stage':'actual-inplace-H2-factor','lambda_step':lam,'resident':assembly_module.resident()}),flush=True)
   try:change,factor,scale,fact=factor_solve(H,S,lam,gradient)
   except np.linalg.LinAlgError as err:
    attempts.append({'lambda_step':lam,'factorization_failed':str(err)});continue
   # Actual original physical operator supplies the residual, not the assembled H.
   refinements=[]
   for it in range(4):
    streamed=physical.normal_direction(linear,change);physical_normal=streamed['physical_normal'];regnormal=physical_normal+lam*apply_h2(S,change)
    regnorm=float(np.linalg.norm(regnormal));relative=regnorm/max(np.finfo(float).tiny,gnorm)
    refinements.append({'iteration':it,'relative_regularized_normal':relative,'regularized_normal_norm':regnorm})
    if relative<=args.gradient_tolerance or it==3:break
    delta=scale*cho_solve_banded((factor,True),-scale*regnormal.ravel(),check_finite=False);change+=delta.reshape(change.shape)
   screen=derivative_control_bounds(basis,change,float(chart.total))
   alpha0=min(1.,args.hessian_step_cap/max(np.finfo(float).tiny,screen['fixed_chart_second_screen']))
   slope=streamed['unregularized_slope'];prediction=-2*slope-streamed['Jd_norm_squared']
   diagnostics={**fact,'actual_initial_physical_gradient_norm':gnorm,'actual_physical_normal_norm':float(np.linalg.norm(physical_normal)),
      'actual_relative_physical_normal_norm':float(np.linalg.norm(physical_normal))/max(np.finfo(float).tiny,gnorm),
      'actual_regularized_normal_refinement':refinements,'direction_H2_norm_squared':float(np.sum(change*apply_h2(S,change))),
      'actual_unregularized_direction_slope':slope,'actual_Jd_norm_squared':streamed['Jd_norm_squared'],'scalar_reduction_is_sum_of_block_dots':True,'predicted_unregularized_energy_decrease':prediction,'direction_screen':screen,'alpha_from_second_jet_screen':alpha0,
      'regularization_applies_only_to_increment':True,'nonlinear_original_g_unchanged':True,'complete_Gram_rows_and_all_cross_channels_retained':True}
   del factor;H=None;assemble=None;gc.collect()
   current={'lambda_step':lam,'linear_solve':diagnostics,'nonlinear_trials':[]};attempts.append(current)
   for back in range(6):
    alpha=alpha0*2**(-back);stat=stream.observe(basis,z,w,position,coeff+alpha*change,N,args.block)
    current['nonlinear_trials'].append({'alpha':alpha,**stat})
    if stat['weighted_energy']<linear.statistics['weighted_energy'] and stat['metric_peak']<=linear.statistics['metric_peak']*1.001:
     accepted={'alpha':alpha,'lambda_step':lam,'statistics':stat};coeff+=alpha*change;break
   if accepted is not None:break
  rows.append({'step':step,'before':linear.statistics,'complete_normal_assembly':assembly,'actual_reassemblies_for_lambda_retries':reassemblies,'attempts':attempts,'accepted':accepted})
  print(json.dumps({'step':step,'before':linear.statistics,'accepted':accepted,'last_direction_diagnostics':attempts[-1].get('linear_solve')}),flush=True)
  physical.cleanup(linear);physical_storage.append(linear.disk_receipt)
  streamed=None;gradient=None;physical_normal=None;regnormal=None;change=None;scale=None
  del linear,assemble,H,S;gc.collect()
  if accepted is None:break
 oz,ow=core.quadrature(mesh,gauss+2,chart);ON=N*args.observe_angular_factor
 print(json.dumps({'stage':'actual-independent-before','resident':assembly_module.resident(),'radial_nodes':len(oz),'angular_nodes':ON}),flush=True)
 before_obs=stream.observe(basis,oz,ow,position,initial,ON,args.block)
 print(json.dumps({'stage':'actual-independent-after','resident':assembly_module.resident(),'radial_nodes':len(oz),'angular_nodes':ON}),flush=True)
 after_obs=stream.observe(basis,oz,ow,position,coeff,ON,args.block)
 field=Path(str(args.out)+'.field.npz');np.savez_compressed(field,coefficients=coeff,unit_knots=basis.knots,planar_modes=basis.pm,vertical_modes=basis.zm)
 out={k:v for k,v in old.items() if k not in ('rows','seconds','actual_linear_preconditioner','actual_full_normal_assemblies','exact_initial_transfer')}
 out.update(schema='2ecf-original-M12-entire-half-sparse-Cartesian-disk-normal-inplace-H2-increment-direct-LM-v1',script_sha256=sha(__file__),field_sha256=sha(field),grid_sha256=sha(args.grid),
   source=src.source_identity,background=chart.background.receipt(),data_sha256=sha(args.data),query_report_sha256=sha(args.query_report),query_cache_sha256=sha(args.query_cache),
   complete_Gram_source_sha256=sha(args.scripts/'6a65-m12-complete-gram-normal-preconditioner.py'),assembly_only_source_sha256=sha(HERE/'2ecf-m12-complete-gram-mapped-assembly-only.py'),single_inplace_normal_band=True,unused_H1_normal_factor_removed=True,original_core_source_sha256=sha(args.scripts/'6a65-m12-entire-half-cartesian-warm-refinement.py'),
   actual_initial_field_sha256=sha(args.initial_field),actual_initial_result_sha256=sha(args.initial_result),order=order,angular=N,gauss=gauss,elements=len(mesh)-1,unknowns=int(coeff.size),
   initial_training_entire_half=initial_training,rows=rows,independent_observer_before=before_obs,independent_observer_after=after_obs,
   independent_peak_material_q=float(oz[after_obs['peak_radial_index']]*chart.total),accepted_steps_this_refinement=sum(r['accepted'] is not None for r in rows),
   central_and_true_cuff_correction_jets_max=[float(np.max(abs(B@coeff))) for B in basis.matrices([0.,1.])],
   original_exact_metric_unchanged=True,all_internal_interfaces_free=True,true_flat_cuff_included=True,full_half_including_finite_tail_and_deep_collar=True,
   nonlinear_target_regularization=0.,regularization_applies_only_to_increment=True,continuous_metric_certificate=False,exact_isometry_proved=False,whole_family_reach_certified=False,
   physical_storage=physical_storage,physical_stream_source_sha256=sha(HERE/'2ecf-m12-disk-physical-linearization.py'),no_global_Jd_or_Jd_plus_residual_arrays=True,
   resident_high_water_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,seconds=time.monotonic()-began)
 save(args.out,out)
 print(json.dumps({'result':str(args.out),'field_sha256':sha(field),'accepted':out['accepted_steps_this_refinement'],'observer_before':before_obs,'observer_after':after_obs,'seconds':out['seconds']}),flush=True)

if __name__=='__main__':main()
