#!/usr/bin/env python3
"""Numerical angular spectra of actual full Gram errors at saved-field peaks.

Uses the original physical source queries and saved Cartesian field. This is
an adaptive-direction diagnostic, not a continuous certificate or an assertion
that residual Fourier modes equal independent correction degrees of freedom.
"""
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ('scripts','data','grid','field','result','query-report','query-cache','out'):ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--angular',type=int,default=1536);a=ap.parse_args();began=time.monotonic()
 if a.out.exists():raise FileExistsError('Fresh actual-field spectral report required')
 grid=json.loads(a.grid.read_text());result=json.loads(a.result.read_text())
 for k,p in [('field_sha256',a.field),('grid_sha256',a.grid),('query_report_sha256',a.query_report),('query_cache_sha256',a.query_cache)]:
  if result[k]!=sha(p):raise ValueError('Actual field/source identity changed '+k)
 core=load('spectrum_original_whole',a.scripts/'6a65-m12-entire-half-cartesian-bvp.py')
 joint=load('spectrum_original_joint',a.scripts/'6a65-m12-global-common-cut-position-recovered.py')
 bg=load('spectrum_original_background',a.scripts/'6a65-m12-original-tail-background.py')
 cache=load('spectrum_same_value_cache',HERE/'2ecf-m12-h2-cached-direct-lm-v2.py');cached=[];cache.cache_tail_apply(core.TailQueries,cached)
 a.background_tolerance=grid['background_tolerance'];_,mp,bp,_,_,chart=core.definition(a,joint,bg)
 for k,p in [('data_sha256',a.data),('common_meta_sha256',mp),('bridge_sha256',bp),('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(bg.__file__))]:
  if grid[k]!=sha(p):raise ValueError('Changed fixed input '+k)
 tail=core.TailQueries(a.query_report,a.query_cache);src=joint.CommonCutSource(a.data,mp,bp,a.query_report,a.query_cache)
 _,c=joint.ad.exact_section(a.data,core.Q(0));central=joint.ad.NativeCurve(c,512,32)
 position=core.WholePosition(src,central,chart,tail,joint);mesh=np.asarray(grid['unit_mesh']);basis=core.basis_for(joint,mesh,grid['order'],chart)
 if 'unit_knots' in grid:
  helper=load('spectrum_declared_C2',HERE/'2ecf-m12-h2-c2-direct-lm.py');basis=helper.checked_basis(core.basis_for,joint,mesh,grid['order'],chart,grid['unit_knots'])
 with np.load(a.field,allow_pickle=False) as f:
  coeff=f['coefficients'].copy()
  for k,v in [('unit_knots',basis.knots),('planar_modes',basis.pm),('vertical_modes',basis.zm)]:
   if not np.array_equal(f[k],v):raise ValueError('Saved basis mismatch '+k)
 zt,_=core.quadrature(mesh,grid['gauss'],chart);zo,_=core.quadrature(mesh,grid['gauss']+2,chart)
 t=result['rows'][-1];stat=t['accepted']['statistics'] if t['accepted'] is not None else t['before'];i=stat['peak_radial_index'];j=result['independent_observer_after']['peak_radial_index']
 points=[('training_peak',zt[i]),('independent_peak',zo[j])]
 for delta in (-1,1):
  if 0<=i+delta<len(zt):points.append(('training_neighbor_'+str(delta),zt[i+delta]))
 rows=[]
 for name,z in points:
  p,bb=position(np.array([z]),a.angular);p+=joint.stream.packet(basis,basis.matrices([z]),coeff,a.angular)
  x,y=p[0,1],p[0,2];b=bb[0];e=np.sum(x*x,axis=-1)-1;f=np.sum(x*y,axis=-1)/b;g=np.sum(y*y,axis=-1)/(b*b)-1
  modes=np.fft.rfft(np.stack((e,np.sqrt(2)*f,g)),axis=1)/a.angular
  power=np.sum(abs(modes)**2,axis=0);weights=np.full(len(power),2.);weights[0]=1.;weights[-1]=1.;power*=weights
  total=float(power.sum());top=np.argsort(power)[::-1][:16]
  rows.append({'point':name,'unit_coordinate':float(z),'material_q':float(z*chart.total),'radius':str(chart.radius(z)[0]) if z*chart.total>chart.S else None,
    'metric_operator_peak':float(np.max(abs((e+g)/2)+np.sqrt(((e-g)/2)**2+f*f))),
    'Gram_Frobenius_angular_mean_square':total,'Gram_Frobenius_mean':list(map(float,[e.mean(),f.mean(),g.mean()])),
    'tail_power_fraction_above_mode':{str(k):float(power[k+1:].sum()/total) for k in (48,96,144,192,256)},
    'strongest_Gram_error_modes':[{'mode':int(k),'power_fraction':float(power[k]/total),'amplitude_vector_e_sqrt2f_g':list(map(float,abs(modes[:,k])))} for k in top]})
 report={'schema':'2ecf-M12-actual-full-Gram-angular-spectrum-v1','script_sha256':sha(__file__),'field_sha256':sha(a.field),'grid_sha256':sha(a.grid),'solver_result_sha256':sha(a.result),'query_report_sha256':sha(a.query_report),'query_cache_sha256':sha(a.query_cache),'angular_nodes':a.angular,'same_saved_field_and_original_g':True,'finite_numerical_diagnostic_not_continuous_certificate':True,'residual_modes_not_identified_with_independent_correction_modes':True,'points':rows,'cached_source_angles':cached,'seconds':time.monotonic()-began}
 a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('points','cached_source_angles')}),flush=True)
 for row in rows:print(json.dumps({k:v for k,v in row.items() if k!='strongest_Gram_error_modes'}),flush=True)
if __name__=='__main__':main()
