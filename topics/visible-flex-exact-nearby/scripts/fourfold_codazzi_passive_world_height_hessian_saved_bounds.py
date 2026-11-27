#!/usr/bin/env python3
"""New WH rational combinations of complete saved bounds; no science producer."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

PINS = {
 "results/R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md":
 "b1751a475c30ec9ca823681598b60326befc85909d462a5ff7b18acaad237c23",
 "results/R144-supplement-complete-low-norm-tame-Hessian-and-mean-preserving-smoothing.md":
 "141f98f90c236a6588223469e61f97ff9c133533ae06e7d496e7c2420a79db87",
 "results/R133-supplement-actual-complete-strict-radial-first-symbol-defect.md":
 "3176f8aeead06c039a6b6eb4fd65916cd79ef17092d4a02f1c5b2f6c8a55509a",
 "results/R133-supplement-actual-full-frequency-moving-root-budget.md":
 "2a146e4ba1dcb268a185d709423f6275192c0a13340c47716cd04cec4f8beeaf",
 "results/R133-supplement-current-moving-positive-root-Riccati-and-full-head.md":
 "38d7ec697d8a0565b2563324aca689776749aa81fc8bf8b0dab4d0f28fcfd8fb",
 "results/R133-supplement-actual-whole-positive-N97-inverse.md":
 "39db339c6702a4cd363126d892cb6f04f629997a2acb544d6309486ca2faae2e",
 "scripts/fourfold_codazzi_current_positive_complete_coefficients.py":
 "1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c",
 "results/R133-supplement-actual-selected-parameter-core-scalar-fees-and-collar-jets.md":
 "f9758b3dbd81e5234a598c5a53ecbe309fe8915c005dab21de7c750d83cb8c44",
 "results/R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md":
 "825113583ae91127e6b99fc839a7b5fd32bdaa660befcce5c7d5728c253f0538",
 "results/R133-supplement-moving-frame-with-complete-residual-and-mean.md":
 "4628cb73db40b15652415106a48c134e334eea7d78031fedc2f65b6f8b064fbe",
 "results/R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md":
 "d4aaa732fe987213857f2b7af4f383e521f15142648ba14be5d51df91c9ad856",
}


def main():
    topic = Path(__file__).resolve().parents[1]
    for name, expected in PINS.items():
        assert hashlib.sha256((topic/name).read_bytes()).hexdigest() == expected, name
    checks = []

    def less(name, value, bound):
        value, bound = F(value), F(bound)
        assert value < bound, (name, value, bound)
        checks.append(dict(name=name, exact=str(value), strict_upper=str(bound)))

    A, R = F(2**20), F(25,8)
    less("whole nearby pair", F('6.407')+F('1e-6'), 7)
    less("complete mean remains separated", 1,
         F('1.068')-F('4.739e-7')-F('1e-6'))
    less("complete log radius interval", 6*(R-F(9,10)), F(27,2))
    less("factorial-series bound for e", F(65,24)+F(1,100), F(11,4))
    less("half-exponent comparison squared", F(11,4), F(5,3)**2)
    less("whole original physical radius", F(5,3)**27, A)
    less("root beta gamma ratio", F(9,5)/F('1.119607700127'), 2)
    less("compact waist inclusion", F('4.739e-7')+F('1e-6'), F('2e-6'))
    less("true waist point gap", F(1,13), F('.0833357128')-F('1e-6'))
    less("whole physical waist Jacobian", F(1,100), F(1,91))
    less("complete drift value", F(6*49,4), 74)
    less("weighted metric first drift", 49, 21*100)
    less("all drift second groups", F(33,20)+F(7,100)+F(49,10000), 4)
    less("whole three factor second groups", 28+518+F('23.1')+147+74, 800)
    less("whole reciprocal drift second groups", 4+74+21, 100)
    less("p first L2", 2*739+F(518,100)+6, 1490)
    less("p first Linfinity", 2*F('893.4')+F(518,100)+6*F(11,10), 1800)
    less("p complete second", 2*800+F(739,100)+F(518,40000), 1610)
    less("k first L2", 14+7*F(24,100)+739, 755)
    less("k first Linfinity", 14*F(11,10)+7*F(24,100)+F('893.4'), 911)
    less("k complete second", 800+F(24,100)+7*F(24,20000), 801)
    less("M first Linfinity sum", 1800+911+116, 2900)
    less("M complete second sum", 1610+801+100, 2600)
    less("c first L2 sum", F(7,100)+739+14+7*F(7,100), 754)
    less("c complete second sum", 800+F(7,100)+8*F(7,40000), 801)
    less("full radial square root", R, F(9,5)**2)
    less("entire first frame L2", 1+2340*A*F(9,5), 4213*A)
    less("entire first frame Linfinity", 2+2900*A*F(9,5), 5222*A)
    less("entire second frame", 5222*A*2340*A*F(9,5)+2600*A, 22000000*A*A)
    f1 = 1+R*630*A*4213*A+754*A*F(9,5)
    f2 = R*630*A*22000000*A*A+5222*A*754*A*F(9,5)+801*A
    less("entire first position", f1, 9000000*A*A)
    less("entire second position", f2, 44000000000*A**3)
    less("whole first physical weight", 2*(7*F(9,4)+8), 48)
    less("all four physical second weight groups",
         7*F(9,4)**2+7*F(9,2)+2*F(9,4)*8+16, 120)
    height = 14*44000000000*A**3+48*9000000*A*A+120*A*(1+630*R)
    less("whole physical Hminus3 Hessian", height, 2**100)
    print(json.dumps(dict(complete=True, comparisons=len(checks),
                         old_scientific_targets_evaluated=0,
                         new_frame_integrations=0, bounds=checks), indent=2))


if __name__ == '__main__':
    main()
