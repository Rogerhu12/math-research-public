"""Add the existing C2 interpolation allowance to the same raw m3 core guard.

The exact rho/curve definition, all jets, the original 1e-5 positivity floor,
the original grid ceiling, and both original sufficient lower bounds remain.
Only a third lower bound is added.  Its second-derivative budget is analytic
on the whole angular domain; it is not a sampled rho'' maximum.  This remains
a numerical source guard, not a rigorous libm or complete-surface certificate.
"""
import hashlib
from pathlib import Path
import sys
import types

LIBRARY = Path(__file__).with_name('round_raw_lib')
if str(LIBRARY) not in sys.path:
    sys.path.insert(0, str(LIBRARY))
from fixed_large_radius_core import TRANSFORMS as RELEASE_FIRST_CONTROL

SOURCE = LIBRARY/'large_radius_local_core.py'
SECOND = '''            # The C4 cutoff obeys |chi'|<=630/(256*eps) and
            # |chi''|<=2520/(64*eps**2) on its whole transition.
            # rho''=q*((1-lambda*chi)*s''-2*lambda*chi'*s'
            #           -lambda*chi''*(s+beta-C)) + full control rho''.
            # Here 0<=lambda*chi<=1, and every control bound comes from
            # the original exact-coefficient/analytic cutoff budgets.
            n=self.base_mode;eta=self.bimodal_eta;factor=self.factor
            smooth_first=factor*n*(1+3*eta)
            smooth_second=factor*n*n*(1+5*eta)
            delta_upper=factor*(1+2*eta)+abs(self.local_flatten_beta)+abs(self._circle_constant)
            base_second=self.q*(smooth_second+self.lam*(2*(630/256)/self.transition*smooth_first+(2520/64)/self.transition**2*delta_upper))
            self.rho_second_derivative_bound=math.nextafter((base_second+float(np.sum(abs(self.c)*ddb)))*(1+128*np.finfo(float).eps),math.inf)
'''
ADDITIONS = [
    ('rb=db=np.zeros(0);control_error=0.',
     'rb=db=ddb=np.zeros(0);control_error=0.'),
    ('rb,db,_=self.basis.homotopy_rho_bounds(self.lam)',
     'rb,db,ddb=self.basis.homotopy_rho_bounds(self.lam)'),
    ('            # Coefficient uncertainty is certified by rational moment intervals.',
     SECOND+'            # Coefficient uncertainty is certified by rational moment intervals.'),
    ('                self.rho_lower=max(self.rho_triangle_lower,float(rr.min()-slack))\n'
     '                self.rho_upper=min(self.rho_triangle_upper,float(rr.max()+slack))',
     '                second_slack=math.nextafter((self.T/count)**2*self.rho_second_derivative_bound/8*(1+128*np.finfo(float).eps)+self.rho_value_roundoff_allowance,math.inf)\n'
     '                self.rho_lower=max(self.rho_triangle_lower,float(rr.min()-slack),float(rr.min()-second_slack))\n'
     '                self.rho_upper=min(self.rho_triangle_upper,float(rr.max()+slack),float(rr.max()+second_slack))'),
    ('                       rho_value_roundoff_allowance=self.rho_value_roundoff_allowance,',
     "                       rho_value_roundoff_allowance=self.rho_value_roundoff_allowance,\n"
     "                       rho_second_derivative_bound=self.rho_second_derivative_bound,\n"
     "                       numerical_positivity_guard='Maximum of original triangle, original first derivative grid, and C2 interpolation lower bounds',")]

text = SOURCE.read_text()
for before, after in [*RELEASE_FIRST_CONTROL, *ADDITIONS]:
    if text.count(before) != 1:
        raise RuntimeError('The original raw core guard transform does not match: '+before)
    text = text.replace(before, after)
module = types.ModuleType('m3_raw_second_order_core_literal')
module.__file__ = str(SOURCE)
exec(compile(text, str(SOURCE)+'::C2_guard', 'exec'), module.__dict__)
make_core_class = module.make_core_class
PROVENANCE = dict(
    source=str(SOURCE),source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    released_first_control_sha256=hashlib.sha256((LIBRARY/'fixed_large_radius_core.py').read_bytes()).hexdigest(),
    complete_derived_source_sha256=hashlib.sha256(text.encode()).hexdigest(),
    scope=__doc__,unchanged_positivity_floor=1e-5,unchanged_grid_ceiling=32768,
    second_derivative_scope='Whole-domain analytic primary and full-control bounds; '
        'the unchanged numerical coefficient/evaluation allowance is retained.',
    additions=ADDITIONS)
