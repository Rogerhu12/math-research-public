"""Independent exact-arithmetic checks for the scope audit.

These verify only ideal-spectrum comparisons and failure of one stated
R20 sufficient gate at n=160. They do not solve a nonlinear tail.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sys


def run():
    rows = []
    for j in range(1, 14):
        m = 3*j
        nu = F(m*m*(m*m-1), 12)
        lower2 = 4*nu*nu/F(2**m)
        upper2 = F(65, 64)**4*lower2
        if j <= 12:
            assert lower2 > 1
        else:
            assert upper2 < 1
            assert upper2 < F(537, 1000)**2
        rows.append({"j": j, "m": m, "nu": str(nu),
                     "large_eigenvalue_lower_squared": str(lower2),
                     "large_eigenvalue_upper_squared": str(upper2),
                     "ideal_type": "one unstable direction" if j <= 12 else "both stable"})
    # nu_{3(j+1)}/nu_{3j} is a product of four decreasing positive
    # factors (see the audit proof). At j=4 it equals 350/143.
    assert F(350, 143)**2 < 8
    # The positive square root 2^(3/2) thus exceeds this ratio.
    # All later normalized comparison terms decrease.

    # Current source delta_160=(3/500)*2^-160, with 3/500>2^-8.
    # Therefore delta_160^(-1/16)<2^10.5<1536.
    assert F(3, 500) > F(1, 256)
    assert F(1536)**2 > 2**21
    # R20 gamma=log(2)/64 and |log delta_160|>160 log(2).
    M_lower = 10016*64*160
    assert M_lower > 1536
    return {"status": "PASS; only ideal algebra and one failed sufficient depth gate",
            "r20_blob": "6c4a7c974386a864749b2c72b2e9cc7a922947d8",
            "source": {"delta0": "3/500", "n": 160},
            "M160_strict_lower": M_lower,
            "delta160_to_minus_one_sixteenth_strict_upper": 1536,
            "ideal_mode3_blocks": rows,
            "not_claimed": "An exact nonlinear threefold tail, a sufficient start N, or a finite-cut DN."}


if __name__ == "__main__":
    result = run()
    text = json.dumps(result, indent=2) + "\n"
    if len(sys.argv)>1:
        Path(sys.argv[1]).write_text(text)
    print(text)
