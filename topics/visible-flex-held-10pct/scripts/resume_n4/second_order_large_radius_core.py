"""Add a C2 interpolation certificate to the same complete core rho guard.

On each angular grid interval of length h, a C2 function differs from its
linear interpolant by at most h*h*sup(abs(f''))/8. Keep both original lower
bounds and add this third sufficient bound. All core values, rho floor,
maximum grid size, coefficient intervals and point-value allowance remain.
"""
import hashlib,types
from pathlib import Path
SOURCE=Path(__file__).with_name('large_radius_local_core.py')
SOURCE_SHA256=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
SECOND='''            # |chi'| <= (630/256)/eps and |chi''| <= (2520/64)/eps**2.
            # For delta=s+beta-C, |delta| <= f*(1+2*eta)+|beta|+|C|.
            # rho''=q*((1-lambda*chi)*s''-2*lambda*chi'*s'-lambda*chi''*delta)
            #        + the full complementary rho''; 0 <= lambda*chi <= 1.
            n=self.base_mode;eta=self.bimodal_eta;factor=self.factor
            smooth_first=factor*n*(1+3*eta)
            smooth_second=factor*n*n*(1+5*eta)
            delta_upper=factor*(1+2*eta)+abs(self.local_flatten_beta)+abs(self._circle_constant)
            base_second=self.q*(smooth_second+self.lam*(2*(630/256)/self.transition*smooth_first+(2520/64)/self.transition**2*delta_upper))
            self.rho_second_derivative_bound=math.nextafter((base_second+float(np.sum(abs(self.c)*ddb)))*(1+128*np.finfo(float).eps),math.inf)
'''
TRANSFORMS=[
 ('rb=db=np.zeros(0);control_error=0.','rb=db=ddb=np.zeros(0);control_error=0.'),
 ('rb,db,_=self.basis.homotopy_rho_bounds(self.lam)','rb,db,ddb=self.basis.homotopy_rho_bounds(self.lam)'),
 ('            # Coefficient uncertainty is certified by rational moment intervals.',SECOND+'            # Coefficient uncertainty is certified by rational moment intervals.'),
 ('                self.rho_lower=max(self.rho_triangle_lower,float(rr.min()-slack))\n                self.rho_upper=min(self.rho_triangle_upper,float(rr.max()+slack))',
  '                second_slack=math.nextafter((self.T/count)**2*self.rho_second_derivative_bound/8*(1+128*np.finfo(float).eps)+self.rho_value_roundoff_allowance,math.inf)\n                self.rho_lower=max(self.rho_triangle_lower,float(rr.min()-slack),float(rr.min()-second_slack))\n                self.rho_upper=min(self.rho_triangle_upper,float(rr.max()+slack),float(rr.max()+second_slack))'),
 ('                       rho_value_roundoff_allowance=self.rho_value_roundoff_allowance,',
  "                       rho_value_roundoff_allowance=self.rho_value_roundoff_allowance,\n                       rho_second_derivative_bound=self.rho_second_derivative_bound,\n                       positivity_certificate='Maximum of original triangle, original first-derivative grid, and C2 interpolation bound',")]
text=SOURCE.read_text()
for before,after in TRANSFORMS:
    if text.count(before)!=1:raise RuntimeError('Second-order core guard literal transform mismatch: '+before)
    text=text.replace(before,after)
mod=types.ModuleType('second_order_large_radius_core_literal');mod.__file__=str(SOURCE)
exec(compile(text,str(SOURCE),'exec'),mod.__dict__)
make_core_class=mod.make_core_class
PROVENANCE=dict(source_sha256=SOURCE_SHA256,replacements=TRANSFORMS,scope=__doc__)
