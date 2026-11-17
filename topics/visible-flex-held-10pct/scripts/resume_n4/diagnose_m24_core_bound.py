from pathlib import Path
import gzip,json,time,hashlib
import numpy as np
from complementary_moment_basis import ComplementaryMomentBasis
from combined_control_bounds import bounds
begin=time.monotonic()
W=Path(__file__).parent
read=lambda name:json.loads(gzip.decompress((W/name).read_bytes()))
a=read('large-radius-eta010-vu035-q0125-m16-lam0.json.gz');b=read('large-radius-eta010-vu035-q015-m20-lam0.json.gz')
q=.0175;factor=(q-b['gauge_amplitude'])/(b['gauge_amplitude']-a['gauge_amplitude']);c=np.zeros(23)
for j in range(2,b['config']['modes']):
 vl=b['parameters'][j]*b['central_correction_scales'][j-1]/b['gauge_amplitude']
 vb=a['parameters'][j]*a['central_correction_scales'][j-1]/a['gauge_amplitude']if j<a['config']['modes']else 0.
 c[j-1]=q*((1+factor)*vl-factor*vb)
z=ComplementaryMomentBasis(base_mode=4,modes=24,halfwidth=.147,transition=.16,center=np.pi/4,precision=80)
rb,db,_=z.homotopy_rho_bounds(0.)
error=float(abs(c)@(15*z.fundamental_evaluation_error))
combined=bounds(z,c,0.)
result=dict(c=c.tolist(),rho_triangle=float(abs(c)@rb),rho_derivative=float(abs(c)@db),control_error=error,combined_rho=combined[0],combined_derivative=combined[1],fundamental_value=float(c@z.fundamental_leakage),fundamental_interval_error=float(abs(c)@z.fundamental_evaluation_error),neumann_residual=float(z.certificate['neumann_residual']),inverse_error=float(z.certificate['inverse_error']),seconds=time.monotonic()-begin)
(W/'diagnose_m24_core_bound.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
