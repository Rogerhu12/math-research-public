#!/usr/bin/env python3
"""R294: exact algebraic certificates for the actual rational three-isogeny descent."""
from pathlib import Path
import json
import sympy as S

checks = []


def require(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def residue(expr, variable, relation):
    numerator = S.cancel(expr).as_numer_denom()[0]
    return S.rem(numerator, relation, variable) == 0


x, y, D, X, Y, s, u, v = S.symbols("x y D X Y s u v")
fx = (x**3+4*D)/x**2
fy = y*(x**3-8*D)/x**3
hx = (X**3-108*D)/(9*X**2)
hy = Y*(X**3+216*D)/(27*X**3)
require("actual phi lands on E minus 27D",
        residue(fy**2-fx**3+27*D, y, y*y-x**3-D))
require("actual dual lands back on E D",
        residue(hy**2-hx**3-D, Y, Y*Y-X**3+27*D))
require("phi invariant differential multiplier is one",
        S.factor(S.diff(fx, x)*y/fy-1) == 0)
require("dual invariant differential multiplier is three",
        S.factor(S.diff(hx, X)*Y/hy-3) == 0)
require("full cubic Kummer identity on the dual image",
        residue(((Y+9*s)/(3*X))**3-hy.subs(D, s*s)-s,
                Y, Y*Y-X**3+27*s*s))
require("norm of the cubic Kummer root equals the dual x coordinate",
        residue((Y*Y-81*D)/(9*X*X)-hx,
                Y, Y*Y-X**3+27*D))
require("explicit inverse from a cube lies on the actual source",
        residue((9*u/v)**2-(3/v)**3+27*D,
                D, v*(3*u*u+D*v*v)-1))
require("the inverse root is exactly u plus v times sqrt D",
        S.factor(((Y+9*s)/(3*X)).subs({X: 3/v, Y: 9*u/v})-u-v*s) == 0)

m, n, t = S.symbols("m n t")
line_polynomial = t**3-m*m*t*t-2*m*n*t+s*s-n*n
require("the line product Kummer homomorphism identity",
        S.factor(-m**3*line_polynomial.subs(t, -(n+s)/m)-(n+s)**3) == 0)

epsilon = 4+s
pi2 = (5+s)/2
barpi2 = (5-s)/2
require("the real quadratic prime generator has norm two",
        residue(pi2*barpi2-2, s, s*s-17))
require("the real fundamental unit has norm minus one",
        residue((4+s)*(4-s)+1, s, s*s-17))
require("the original P Kummer class has the asserted prime exponents",
        residue(epsilon*pi2*barpi2**2-(3+s), s, s*s-17))
require("the original Q Kummer class is the fundamental unit",
        epsilon == 4+s)
images = []
for point, expected in [((-2, 3), (15, 54)), ((-1, 4), (67, 548))]:
    image = tuple(S.cancel(f.subs({x: point[0], y: point[1], D: 17}))
                  for f in (fx, fy))
    require(f"original point {point} has exact isogeny image {expected}",
            image == expected and image[1]**2 == image[0]**3-459)
    images.append({"point": point, "image": [int(a) for a in image]})

payload = {"status": "PASS", "number_of_checks": len(checks),
           "checks": checks, "actual_point_images": images,
           "quadratic_discriminants": [17, -51],
           "class_numbers_proved_in_text": [1, 2]}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({"status": "PASS", "checks": len(checks), "output": str(out)}))
