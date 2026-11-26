#!/usr/bin/env python3
"""Exact rational combinations of completed small bounds; no scientific producers."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

PINS = {'results/R133-supplement-real-H1-physical-chart-remainder-and-complete-boundary-error.md': '1e443100d4c6749eb72c676b54571a5bed3944b22eba15bef3c333e2e5c57fc3', 'results/R144-supplement-complete-positive-hybrid-adapter-for-compact-centres.md': '85f542fa42cbf039a9038107dbd860163029c1f7db814d5922cb0a4cdd1e7115', 'results/R133-supplement-final-moving-centre-actual-regular-boundary.md': 'f4ae237c86542f29f2127f7e43d5ab97827756fcce86e71bcff8c0a610ec81af'}

def main():
    topic = Path(__file__).resolve().parents[1]
    for relative, expected in PINS.items():
        raw = (topic / relative).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == expected, relative
    checks = []
    def less(name, value, upper):
        assert value < upper, (name, value, upper)
        checks.append({"name": name, "complete_rational_bound": str(value),
                       "strict_upper": str(upper)})
    rho = F(1, 10**6)
    e0 = 2 * F("3.848e-7") + rho
    e1 = 2 * F("1.020e-6") + rho
    less("cut total value difference", e0, F("2e-6"))
    less("cut total first derivative difference", e1, F("4e-6"))
    less("cut total second derivative difference", 128*2*F("1.020e-6")+rho, F("0.001"))
    less("cut |u|", F(1,50)+e0, F(21,1000))
    less("cut negative mean gap", F(3), F(25,8)-e0)
    less("cut negative density gap", F(3), F(25,8)*F(63,64)-e0)
    less("cut density deviation", F(1,64)+(1+F(65,64))*e0/3, F(1,32))
    less("cut density first derivative", F(1,16)+(e1+e0/16)/3, F(1,15))
    less("cut joint first derivative", F(1,2)+e1, F(51,100))
    less("cut joint second derivative", 192+128*2*F("1.020e-6")+rho, F(193))
    outer_u, outer_w, outer_m = F("1.643190e-9"), F("9.603792e-9"), F("5.84461145233")
    less("outer |u|", outer_u+rho, F(21,1000))
    less("outer negative mean gap", F(3), outer_m-rho)
    less("outer negative density gap", F(3), outer_m-outer_w-rho)
    less("outer density deviation", (outer_w+rho)/(outer_m-rho), F(1,32))
    less("outer density first derivative", (128*outer_w+rho)/(outer_m-rho), F(1,15))
    less("outer joint first derivative", 128*(outer_u+outer_w)+rho, F(51,100))
    less("outer joint second derivative", 128**2*(outer_u+outer_w)+rho, F(193))
    less("inverse angle first variation", F(11,62), F(1,5))
    less("lift variation derivative", F(97,96), F(33,32))
    second_angle = F(32,31)*(F(33,160)+(F(1,375)+F(11,96))/2)
    less("inverse angle complete second variation", second_angle, F(1,3))
    u,p1,p2 = F(21,1000),F(51,100),F(193)
    less("second ratio product coefficient", 2*(u+1)/27, F(2,9))
    less("first ratio derivative h1 coefficient", F(1,3)+p1/9, F(2,5))
    less("first ratio derivative h2 coefficient", (u+1)/9+p1/9+2*(u+1)*p1/27, F(2,5))
    less("ratio first derivative v coefficient", (u+1)/9, F(1,3))
    less("ratio joint second derivative", p2/3+p1*p1/18+2*(u+1)*p1*p1/27, F(65))
    total = F(33,32)*(F(2,9)+F(2,25))+F(65,50)+F(17,300)
    less("complete full-mean physical Hessian", total, F(2))
    print(json.dumps({"complete": True, "checks": len(checks),
                      "scientific_producers_called": 0, "bounds": checks},
                     ensure_ascii=False, indent=2))
if __name__ == "__main__":
    main()
