# R739 — Exact original valuations at p47/h7 and p41/h37

Date: 2026-11-14. Status: **proved by the retained exact finite certificates**.

This closes the two R739 precision questions, keeping the original split
vector, torus, Teichmüller generators, and positive tame direction.
No completed fiber enumeration, lattice sum, or DFT is repeated.

## 1. Conclusions

Use the original $N_h$, $M_{2,h}$, and
$P_h=S_{2,h}S_{3,h}/C_0^2$ of R588/R727. The exact continuation gives
$$
\boxed{p=47,\ h=7:\quad
v_{47}(N_7)=4,\quad N_7/47^4\equiv38\pmod{47},\quad
v_{47}(M_{2,7})=0.}
\tag{739.1}
$$
At the true primitive positive label $h=37$ for $p=41$, it gives
$$
\boxed{
v_{41}(P_{37})=-2,\quad41^2P_{37}\equiv23\pmod{41},\quad
N_{37}\equiv33\pmod{41},\quad v_{41}(M_{2,37})=-1.}
\tag{739.2}
$$
These are exact selected valuations, not lower bounds inferred from zero
residues. Neither R740 nor a parity assumption about $P_h$ is used.

## 2. Reuse the complete original p47 fiber counts

The first public run,
[43609325075](https://github.com/Rogerhu12/math-research-public/actions/runs/43609325075),
enumerated all original fibers for the 47 nonidentity torus elements and
retained all 48 character counts $c_j$. It used the actual matrices
$$
g_a=\begin{pmatrix}a&-1\\1&a+1\end{pmatrix}
$$
and the complete R727 Weyl fiber condition, including zero-coordinate
cases. The original positive character uses the inverse Weyl weight, so
the certified counts give
$$
Q_{47}(X)=46-\sum_{j=0}^{47}c_jX^{7j\bmod48},
\qquad N_7=Q_{47}(\eta),
\tag{739.3}
$$
with exactly the retained order-48 Teichmüller generator $\eta$.
That run established only $N_7\equiv0\pmod{47^4}$.

Reduce (739.3) in
$$
\mathbb Z[X]/(X^{16}-X^8+1)=\mathbb Z[\zeta_{48}].
$$
The multiplication matrix has integer entries. The continuation computes
its determinant by fraction-free Bareiss elimination, checking every
exact division, and checks that same determinant modulo two auxiliary
primes. The determinant is nonzero and its 47-adic valuation is eight.

For a nonzero algebraic integer, the rational norm valuation is the sum
of its nonnegative prime valuations weighted by residue degrees.
Consequently every selected local valuation is at most eight, and
precision $47^9$ suffices to determine it. This is a proved precision
bound, rather than a guessed stopping digit.

The original generator is lifted by repeated $47^2$ powers in the same
unramified quadratic ring. The run verifies compatibility with its old
value modulo $47^4$, its order, and the original torus and character
conventions. At precision nine the exact output is
$$
N_7\equiv490986333968611\pmod{1119130473102767},
\qquad1119130473102767=47^9.
\tag{739.4}
$$
The second coordinate in the original quadratic basis is zero.
The public integer division check gives valuation four and leading unit
38. This proves the finite-norm assertion in (739.1).

## 3. The same p47 label has an original unit second jet

The retained original ordinary-derivative certificate
[notes/R702-prime47.json](../notes/R702-prime47.json) gives
$$
A_5=6,\qquad A_{38}=34\quad\text{in }\mathbb F_{47}.
\tag{739.5}
$$
The exact R697 comparisons are
$$
\frac{4!C_5}{3}=A_5^2,\qquad -2\cdot37!C_{38}=A_{38}^2.
$$
Both factorials and the displayed fixed factors are 47-adic units.
Thus $C_5$ and $C_{38}$ are both units.

Here $h-2=5$ and $p-h-2=38$. The label $h=7$ is primitive modulo 48
and lies in the interior range of R727. The original low-block identities,
with their complete tail estimates, therefore imply
$$
v_{47}(P_7)=-4.
\tag{739.6}
$$
The exact original norm identity, with its unchanged tame phase, is
$$
\frac{M_{2,h}^2}{\zeta^2}
=-\frac{8N_hC_0^2}{(p+1)^2}P_h.
\tag{739.7}
$$
All displayed factors other than $N_h$ and $P_h$ are $p$-units.
Hence $2v_{47}(M_{2,7})=4-4=0$, completing (739.1).
In particular, $N_7\equiv0\pmod{47}$ does not imply that the full
original second jet vanishes.

## 4. Reuse the exact p41 polynomial at the original h37 embedding

The completed R717 run,
[43597163388](https://github.com/Rogerhu12/math-research-public/actions/runs/43597163388),
retained an exact integer polynomial
$$
T(X)=42D\,P,\qquad D=2^{37}3^{26}41^5,
\tag{739.8}
$$
in $\mathbb Z[X]/\Phi_{42}(X)$. Its source includes the original finite CM
sums and certified unique integer traces. The continuation verifies the
source configuration and fixed hashes before reusing this polynomial.

The original generator is in $\mathbb F_{41}[\zeta]$ and satisfies
$$
\gamma\bmod41=(7,30),\qquad\gamma^{14}=\zeta.
$$
Its original six-digit Teichmüller lift is extended compatibly.
Since $37\equiv1\pmod6$ and $(37,42)=1$, evaluation at $\gamma^{37}$
is the true primitive positive label with the same cubic tame direction.
No local parity statement for the old $h=1$ is assumed at this new label.

The exact multiplication determinant of $T$ in the degree-12 cyclotomic
ring is nonzero and has 41-adic valuation twenty. The same nonnegative
norm argument proves that precision $41^{21}$ suffices. The selected
evaluation returned is
$$
T(\gamma^{37})\equiv
1114799483959642221712312285402115
\pmod{7386879101213258109624223688656841},
\tag{739.9}
$$
where the modulus is $41^{21}$ and the second coordinate is zero.
The public run checks that the numerator valuation is three.
Removing (739.8), whose denominator valuation is five, gives
$v_{41}(P_{37})=-2$ and the exact leading residue
$41^2P_{37}\equiv23\pmod{41}$.

The original Legendre formula of R727 gives
$$
N_{37}\equiv-P_{36}(1/\sqrt{-3})^2
=-(19/9)^2=33\ne0\pmod{41}.
\tag{739.10}
$$
Using (739.7) yields $2v_{41}(M_{2,37})=-2$, proving (739.2).
One zero low Cartier coefficient at this label therefore does not make
the complete original $M_{2,37}$ vanish.

## 5. Exact public provenance

All arithmetic ran in this public repository's GitHub Actions.

| Item | Retained identifier |
|---|---|
| Source commit | fe7dff36dda93b42650062e733ada73a0385d7d6 |
| Run | [43610788824](https://github.com/Rogerhu12/math-research-public/actions/runs/43610788824) |
| Job | 132495159660 |
| Arithmetic runtime | 0.4737585160000002 seconds |
| New fiber enumerations / lattice terms / DFTs | 0 / 0 / 0 |
| Arithmetic source SHA256 | 654a3cddd121f56569a1f4c04ac924297eaab295901cfb70ef1308a898165b54 |
| Workflow SHA256 | 07f4a3be1f73ffb414ea62f7510ca9700ef6508704ed0165c6cd5c9e90afab78 |
| Exact result SHA256 | 6704f8813440fbd85e91206541fdb9c1c9296f8742cb5169ee6696932ee3cf7e |
| Exact integer audit gzip SHA256 | 8921a2a723a01c5bf9e81ee131228cd83ea30b78400dd86d2f7ed617bc20e1d8 |
| Run receipt SHA256 | b8aaa986da1b4e09283fa18c5b40a6c7f1b8a280b4d8665306dab41ee21f4028 |

Small outputs and the full manifest are under
[computations/R739-reused-cyclotomic-valuations/43610788824-1](../computations/R739-reused-cyclotomic-valuations/43610788824-1).
The source is
[scripts/R739_reused_cyclotomic_valuations.py](../scripts/R739_reused_cyclotomic_valuations.py).
The full artifact is serre-cartier-R739-reused-cyclotomic-valuations-43610788824-1,
ID 14119802838, 34870 bytes, zip SHA256
0f662c56f3e34a79d99913cf473ebc635fcca65b9c826c01a4e0b0a6416f9a50.

The five reused inputs were fixed before execution:

| Input | SHA256 |
|---|---|
| p47 original fiber checkpoint | eb805a0fe9fdd6404a5e75cba77fdef0084ff85b94874565cfdd471841c49e5f |
| p47 first-precision receipt | 33afb0aad5f900baea0cb881a888e44815e2caad504633daed576812506fab88 |
| p47 complete original fibers gzip | e01a1fda63168d8d32124199b06bf5627cb2ce68911eccaf8fb5ab3bdd0daa01 |
| p41 original integer polynomial gzip | 932899efb77482cb7712e8554376b6c6f65050620bf9a84485d610949ba0dbc7 |
| p41 original exact CM receipt | fb4d9ffadacda241575ab92a49f66819d8ac077ececa8f5151adf4aea3751fa6 |

Input paths, source snapshots, multiplication matrices, Bareiss division
checks, auxiliary determinant checks, precision bounds, compatible
generators, and final values are preserved with the manifest.

## 6. Scope and dependencies

The first-precision note remains accurate: it reported only
$v_{47}(N_7)\ge4$. The continuation upgrades that bound to equality.
R740 is a separate all-prime theorem about $N_h$ and is not an input here.

These selected embeddings do not prove even valuations for all $P_h$,
a uniform simultaneous Cartier-unit theorem, exclusion of original
height zeros on candidate discs, or the Serre completion criterion.

- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md):
  original torus, full fiber formula, exact norm phase, and complete
  low-block and tail comparison.
- [R702](R702-first-pole-block-and-uniform-shifted-units.md) and R697:
  original ordinary derivative convention and retained p47 values.
- [R739 continuation method](../notes/R739-cyclotomic-reuse-method.md):
  predeclared precision procedure and unchanged original embeddings.
- [R740](R740-even-valuations-of-original-finite-toric-norms.md):
  independent all-prime parity for the finite norms.
