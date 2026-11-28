#!/usr/bin/env python3
"""Compare both full angular contractions on actual M12 warm-state blocks."""
import argparse,hashlib,importlib.util,json,resource,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def original_contraction(spectrum,frequency,coefficient,N,helper):
 nr=spectrum.shape[0];nc=frequency.shape[1];Q=np.zeros((nr,nc,nc,2,2),complex)
 for d in range(2):
  for e in range(2):
   sector=spectrum[:,:,d,:,e,:]
   for left in range(2):
    fa=frequency[left];za=coefficient[left]*(1j*fa[:,None])**(1-d)
    for right in range(2):
     fb=frequency[right];zb=coefficient[right]*(1j*fb[:,None])**(1-e)
     F=helper.positive_exponential_moment(sector,fa[:,None]+fb[None,:],N)
     Q[:,:,:,d,e]+=np.einsum('ic,sijcd,jd->sij',za,F,zb,optimize=True)
 return Q

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ('scripts','data','grid','field','transfer-receipt','parent-result','query-report','query-cache','out'):ap.add_argument('--'+k,type=Path,required=True)
 a=ap.parse_args();began=time.monotonic()
 if a.out.exists():raise FileExistsError('Fresh actual M12 block audit required')
 grid=json.loads(a.grid.read_text());tr=json.loads(a.transfer_receipt.read_text())
 for key,p in [('new_grid_sha256',a.grid),('transferred_field_sha256',a.field),('old_result_sha256',a.parent_result)]:
  if tr[key]!=sha(p):raise ValueError('Actual warm field identity changed '+key)
 core=load('audit_original_whole',a.scripts/'6a65-m12-entire-half-cartesian-warm-refinement.py');joint=load('audit_original_joint',a.scripts/'6a65-m12-global-common-cut-position-recovered.py');bg=load('audit_original_background',a.scripts/'6a65-m12-original-tail-background.py')
 cache=load('audit_exact_value_cache',HERE/'2ecf-m12-h2-cached-direct-lm-v2.py');receipts=[];cache.cache_tail_apply(core.TailQueries,receipts)
 a.background_tolerance=grid['background_tolerance'];_,mp,bp,_,_,chart=core.definition(a,joint,bg)
 tail=core.TailQueries(a.query_report,a.query_cache);src=joint.CommonCutSource(a.data,mp,bp,a.query_report,a.query_cache)
 _,c=joint.ad.exact_section(a.data,core.Q(0));central=joint.ad.NativeCurve(c,512,32);position=core.WholePosition(src,central,chart,tail,joint)
 adapter=load('audit_C2_basis',HERE/'2ecf-m12-h2-c2-direct-lm.py');basis=adapter.checked_basis(core.basis_for,joint,np.asarray(grid['unit_mesh']),grid['order'],chart,grid['unit_knots'])
 with np.load(a.field,allow_pickle=False) as f:
  coeff=f['coefficients'].copy()
  if not np.array_equal(f['unit_knots'],basis.knots) or not np.array_equal(f['planar_modes'],basis.pm) or not np.array_equal(f['vertical_modes'],basis.zm):raise ValueError('Actual full C2 warm basis changed')
 z,w=core.quadrature(np.asarray(grid['unit_mesh']),grid['gauss'],chart);N=grid['angular']
 original=load('audit_original_complete_Gram',HERE/'2ecf-m12-complete-gram-assembly-only.py');generic=load('audit_original_fft_moment',a.scripts/'6a65-cartesian-complete-radial-normal.py');sparse=load('audit_sparse_M12_angular',HERE/'2ecf-m12-complete-sparse-cartesian-angular.py')
 frequency,coefficient=original.coupled_terms(basis);rows=[]
 for left in [8,376,2000,2256,4496,5800]:
  sl=slice(left,left+8);p,bb=position(z[sl],N);p+=joint.stream.packet(basis,basis.matrices(z[sl]),coeff,N)
  weight=np.sqrt(w[sl,None]*bb/N);cov=original.point_covariance(p[:,1],p[:,2],bb,weight);spectrum=np.fft.rfft(cov,axis=1);del cov
  start=time.monotonic();reference=original_contraction(spectrum,frequency,coefficient,N,generic);original_seconds=time.monotonic()-start
  start=time.monotonic();actual,receipt=sparse.contract(spectrum,frequency,coefficient,N);sparse_seconds=time.monotonic()-start
  difference=actual-reference;relative=float(np.linalg.norm(difference)/max(np.finfo(float).tiny,np.linalg.norm(reference)));maximum=float(np.max(abs(difference)))
  if relative>5e-14:raise ArithmeticError('Actual complete angular contraction changed beyond rounding')
  rows.append({'first_actual_training_radial_index':left,'radial_points':8,'angular_nodes':N,'angular_channels':basis.na,'relative_full_complex_Q_difference':relative,'maximum_absolute_full_complex_Q_difference':maximum,'original_seconds':original_seconds,'sparse_seconds':sparse_seconds,'complete_point_rows':8*N*3,'all_signed_Cartesian_cross_terms_retained':True,'kernel_receipt':receipt})
  print(json.dumps(rows[-1]),flush=True)
 report={'schema':'2ecf-M12-actual-warm-field-sparse-angular-block-audit-v1','script_sha256':sha(__file__),'grid_sha256':sha(a.grid),'field_sha256':sha(a.field),'transfer_receipt_sha256':sha(a.transfer_receipt),'parent_result_sha256':sha(a.parent_result),'actual_source_identity':src.source_identity,'original_assembly_source_sha256':sha(original.__file__),'sparse_angular_source_sha256':sha(sparse.__file__),'rows':rows,'all_checks_passed':True,'actual_exit':0,'whole_normal_or_new_nonlinear_solve_not_claimed':True,'peak_RSS_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'seconds':time.monotonic()-began}
 a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('rows','actual_source_identity')}),flush=True)
if __name__=='__main__':main()
