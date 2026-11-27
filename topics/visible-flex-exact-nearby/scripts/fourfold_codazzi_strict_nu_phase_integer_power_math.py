"""PHI's identical full square-root jets with an explicit integral cube.

The first new q-jet attempted arb ** 3 on a ball centred at zero.
Use the literal product for that one integer power.  All four complete
old derivative balls, both exponent signs, and the whole Taylor error
remain.  No scientific target is evaluated by importing these definitions.
"""
from pathlib import Path as _Path
import ast as _ast
import hashlib as _hashlib

_original = _Path(__file__).with_name('input_pre_integer_power_math.py')
if not _original.exists():
    _original = _Path(__file__).with_name('fourfold_codazzi_strict_nu_phase_math.py')
_raw = _original.read_bytes()
if _hashlib.sha256(_raw).hexdigest() != '1374965ab4d6c786ca1f3738e3f477a3bcd846064547b3a9f356eba4ae13c5c2':
    raise ValueError('whole unchanged first PHI formula source')
_tree = _ast.parse(_raw.decode(),filename=str(_original))
exec(compile(_tree,str(_original),'exec'),globals())


def curvature_power_jets(jets,exponent,read_ball):
    k = [-read_ball(jets['K'+str(j) if j else 'K'])/factorial(j) for j in range(4)]
    require(k[0].lower() > 0 and exponent in (F(1,2),F(-1,2)), 'whole negative curvature denominator')
    base = k[0].sqrt() if exponent > 0 else 1/k[0].sqrt()
    s = base*0+exponent.numerator; s /= exponent.denominator
    r1,r2,r3 = (value/k[0] for value in k[1:])
    return [base,base*s*r1,base*(s*r2+s*(s-1)*r1*r1/2),
            base*(s*r3+s*(s-1)*r1*r2+s*(s-1)*(s-2)*(r1*r1*r1)/6)]
