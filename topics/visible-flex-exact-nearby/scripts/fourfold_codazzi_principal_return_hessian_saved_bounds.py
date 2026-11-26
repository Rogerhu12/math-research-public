#!/usr/bin/env python3
"""New rational combinations for the complete RP return; no scientific target."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

PINS = {
 "results/R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md":
 "b1751a475c30ec9ca823681598b60326befc85909d462a5ff7b18acaad237c23",
 "results/R144-supplement-complete-low-norm-tame-Hessian-and-mean-preserving-smoothing.md":
 "141f98f90c236a6588223469e61f97ff9c133533ae06e7d496e7c2420a79db87",
 "results/R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md":
 "29aef0d490809cdf1a88d36d4a475c392b68e188637bcf960bb850b336e2d207",
 "results/R133-supplement-complete-phase-row-approximate-inverse-and-quadratic-defect.md":
 "58bdf1739e1b3c98c50e096657502d30b14033f9ee2b81bbfda89652ddf14278",
 "results/R133-supplement-actual-complete-strict-radial-first-symbol-defect.md":
 "3176f8aeead06c039a6b6eb4fd65916cd79ef17092d4a02f1c5b2f6c8a55509a",
 "results/R144-supplement-actual-negative-and-root-propagation-in-a-full-tail-neighbourhood.md":
 "2b53fc6216cd6a70c230129ce1c6ed45bf1da9e83fb3517f90e6726e2a7fedd5",
 "results/R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md":
 "d4aaa732fe987213857f2b7af4f383e521f15142648ba14be5d51df91c9ad856",
}


def main():
    topic = Path(__file__).resolve().parents[1]
    for relative, expected in PINS.items():
        assert hashlib.sha256((topic / relative).read_bytes()).hexdigest() == expected, relative
    checks = []

    def less(name, value, upper):
        assert value < upper, (name, value, upper)
        checks.append({"name": name, "exact_rational": str(value), "strict_upper": str(upper)})

    rho, e0, e1, d = F("1e-6"), F("2e-6"), F("3e-6"), F("1e-10")
    length, support, b, q0 = F(".239"), F(".13"), F(6), F(7)
    less("compact value inclusion", F("4.739e-7")+F("3.861e-18")+rho, e0)
    less("compact first angular inclusion", F("1.255e-6")+F("1.970e-17")+rho, e1)
    less("common whole state margin", F("6.408")+e0, q0)
    less("common old first angular margin", F("5.439")+e1, q0)
    old_l = F(".036374621")
    inc1 = 2*b*(2*q0*e0+e0*e0)*length+2*4*d*q0*q0*support
    inc2 = 2*b*(q0*e1+q0*e0+e0*e1)*length+2*4*d*q0*q0*support
    less("one-leg nearby Lipschitz integral", old_l+inc1, F(".037"))
    less("two-leg full second angular integral", 2*(256*old_l+inc2), F(19))
    j, cj = F(27,25), F(26,25)
    less("complete Jacobian exponential", 1/(1-2*F(".037")), j)
    less("whole L2 composition squared", j, cj*cj)
    dr = F("1.03")*e0+7*F("1.048e-7")/(2*F(".5338"))
    less("complete weighted state difference", dr, F("3e-6"))
    less("whole point receiver increment", 2*2*F(1,2)*dr+F("4e-10"), F("1e-5"))
    less("complete nearby L2 receiver", F("1.03")*(F(".591950779")+F(".49e-5")), F(".610"))
    less("metric speed first derivative", (1+F("1.061"))*24/(2*F(".5338")), F(47))
    less("strict positive metric speed lower", F(1,2), F(".5338"))
    less("metric field first derivative", 4*F(1,2)*49+7*47, F(430))
    less("mixed state metric field", 2*4*F(1,2)*7+47, F(76))
    less("pure second metric field", 14*F(1,2)*49+7*(2*47**2), F(32000))
    less("metric field angular derivative", F(4*49), F(200))
    less("folded state L1 factor squared", 4*length, F(1))
    less("first full state source", 2*F(".610"), F(2))
    less("first full metric source", 2*support*430, F(2*100))
    less("metric first angular source", 2*support*200, F(84*100))
    less("support square root", support, F(".361")**2)
    less("mixed second source", 2*F(".361")*76, F(55))
    less("mixed weighted module coefficient", F(55), F(24*100))
    less("pure metric weighted module coefficient", 2*support*32000, F(24*100**2))
    hessian = j*(19*(j*2)**2+2*cj*(j*2)*84+24)
    mixed = j*j*(19*(j*2)+cj*84)
    spatial = j**3*19
    less("whole return Hessian", hessian, F(530))
    less("whole return mixed spatial derivative", mixed, F(150))
    less("whole return spatial second derivative", spatial, F(24))
    less("phase state Hessian coefficient", F(3,2)*530/2, F(400))
    less("phase mixed Hessian coefficient", F(3,2)*150*F(11,10), F(400))
    less("phase pure lift Hessian coefficient", F(24)*F(11,10)/2, F(400))
    less("fixed-parameter full phase remainder", F(3,4)*530*length, F(96))
    print(json.dumps({"complete": True, "comparisons": len(checks),
                      "scientific_producers_called": 0, "bounds": checks},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
