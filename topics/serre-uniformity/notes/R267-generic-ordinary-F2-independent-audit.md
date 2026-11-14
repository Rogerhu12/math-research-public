# Generic ordinary F2 executor audit, with the actual ORD_j07 input chain

This audit accompanies R267 and occupies no separate result number. It compares
the two generic executors directly with the frozen R259 and R262 sources. It
also executes independent standard-library hash, tangent and scalar checks on
the actual ORD_j07 outputs. It does not repeat the group chain, Riemann–Roch
construction, actual Hecke trace or local Taylor computation.

## Frozen source comparison

| Source | SHA-256 |
|---|---|
| R259 center source | 4ef5e267a5d730e9bb0c102eba708ff8dca5221a8b339258cf89464170fa9917 |
| Generic center source | c55a5722d08c759caa6dfaeda3cfeca467e01dfbe973507b44d4b34aef62a298 |
| R262 local source | 229bcedac9b0ded228bce0ccf69eda671cbca408a443736479a7385068e40988 |
| Generic local source | 204d53270cf4fd82e1affd45f6dd40cf4d0e48641f45f6879bc1881c93400c0e |

The center diff introduces explicit disk/result/input arguments, selects the
ordinary physical model by its recorded residue label, and removes j05-specific
expected scalar values. It adds disk and dependency hash assertions. The five
finite-pole constructions, their residue and calibration equations, actual
three-branch T2 trace with its factor $1/2$, fixed family1 integrations, canonical
relation, tangent normalization and final height formula are unchanged.

The local diff changes the same disk and input selectors and removes
j05-specific expected coefficients and its no-root assertion. The moving
two-pole RR equations, actual T2 trace in faithful $V_4$, self-regular value,
classical-invariant $j$ expansion, derivative, precision bound and independent
global assembly are unchanged. It returns the actual residual roots and sets the
whole-disk exclusion flag exactly when this list is empty.

The applicability conditions remain effective assertions. Every finite pole in
the center construction satisfies $f_c=1$; the local executor requires its
recorded frame to equal the actual $f_c$, verifies all recorded jets and compares
its center to the actual first pole of $\eta_C$. Division by $j'$ and the fixed
rational functions is only used in the ordinary noncollision range. The center
checks $\Phi_2(j,j)$, $\Phi_2(0,j)$, and the residues of
$j$, $j-1728$, $j-54000$, $j+3375$, $j-8000$ are units. This is a generic executor
on that verified range, not a claim that elliptic, fixed-support or Hecke
collision disks satisfy those hypotheses.

## Actual input identity and tangent checks

The independent verifier checked 19 named dependency edges through

- polynomial to center, Abel and multiplication;
- center to second-kind, principal expression, T2 support and full Norm;
- full Norm to T2 Norm, principal expression, second-kind, multiplication and
  based points;
- T2 Norm to principal expression and actual T2 support;
- principal expression to second-kind;
- second-kind to Abel, multiplication and based points;
- Abel to multiplication.

It additionally checked the completed 304-bit status, the exact final-point
hash, the multiplication's based-point hash, all 54 second-kind constants modulo
$47^3$, and the actual 54 family1 physical parameters. The independent freezer
verified all 457 retained function hashes and all 459 archive members byte for
byte. Thus matching disk labels are not being used as a substitute for input
identity.

The fixed/collision Norm output independently records the two genuine
$j$-tangent values
$(a_b,a_P)=(3413944,2364106)$. These exactly match the newly computed center
values. Pure integer arithmetic gives
$\sigma=(a_b/a_P)^4=1280378$ and $\log\sigma=80699$ modulo $47^4$.
The tiny integral is $532463$ and the complete first-variable Norm log is
$4107988$. With the actual positive multiplier $m$, the checked expression
$\log\sigma+m^{-1}(532463+4107988)$ equals $2629321$ modulo $47^4$.
This equals the local polynomial's constant coefficient, so the two generic
executors use the same canonical section and initial scale.

## Independent residual arithmetic

The actual local coefficients in $y=z/47$ are
$[2629321,709136,1848933,2595575]$.
The independently assembled global coefficients are
$[2845474,2908501,822500,163466,2076460]$.
Subtracting $800$ times the local height gives

$$
[2531185,1642697,219443,2447572,2076460]\pmod{47^4}.
$$

After division by $47$, its reduction is $40+30y+16y^2$ over $\mathbf F_{47}$.
All 47 values were checked independently. The roots are $7$ and $44$, with
derivatives $19$ and $28$; the discriminant is $32$. Consequently this one F2
equation does not exclude ORD_j07. Lifting the known polynomial through the
available precision gives

| Residual root | Base-47 digits of $y$ | $y\bmod47^3$ | $z\bmod47^4$ |
|---|---|---:|---:|
| 7 | $(7,13,16)$ | 35962 | 1690214 |
| 44 | $(44,5,0)$ | 279 | 13113 |

These are candidates for this single F2 equation. They are not asserted to be
common roots of the 53 QC equations or rational points. The unchanged R262
tail estimate justifies computing the displayed precision from these stored
coefficients.

## Bound artifacts

- Actual center: ORD_j07_actual_canonical_F2_height47.json.gz,
  SHA cfd54f630d943d1fec6239b6f6f2d6638ef015965cdb3028703f011d90f2c136.
- Actual disk polynomial: ORD_j07_actual_canonical_F2_polynomial47.json.gz,
  SHA c5804c476458091a29eea1f0e640a960f957b36d8b9cad28586abe9f6135fa87.
- Independent verifier: verify_generic_ordinary_F2_inputs47.py,
  SHA 2ad9d16939b6f150ba8118afca5182671be03ba1a42f90deae40937dcb308a26.
- Independent audit: ORD_j07-generic-F2-independent-audit.json,
  SHA bf01a5e4523328ce46c4ddea2c9eb436bd3e1084ef97aaa3794df8d0f4fbbeb9.
- Complete input freeze manifest: ORD_j07-complete-input-freeze-manifest.json,
  SHA d88ce39c6f02dfdb47ae6c9dc892e4cdb833a285aa1cde9c03a0ea9649be25ba.

The scalar verifier was actually executed. The source comparison is a review of
the two complete diffs. No additional expensive numerical execution is implied.

