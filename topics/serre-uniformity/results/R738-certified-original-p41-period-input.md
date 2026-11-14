# R738 — Certified integral period input for the original p41 curve

Date: 2026-11-14. Status: **proved and computed in the public repository Actions**.

This result constructs the original marked modular curve's integral closed
cycles and their alternating pairing. The computation was completed in
[run 43612108090](https://github.com/Rogerhu12/math-research-public/actions/runs/43612108090),
attempt 1, from source commit
`651aa3f7eaac6f97bfd7f87ec25b210eb7d6f4ca`.
The actual CM Hodge periods, quotient functions, and point difference have
not yet been evaluated. They are distinct remaining inputs to R732.

## 1. The actual curve and the output

Use the same positive cubic direction and rational curve as R575 and R616:

$$
X_1=\operatorname{Norm}
\bigl(X_{\mathrm{ns}}^+(41)\times_j\mathbf P^1_a\bigr),
\qquad j=6912a^3(1-a^3).
\tag{738.1}
$$

The relation to the canonical six-level parameter is
$a=\sqrt[3]4\,u$, with the positive real cube root. The period basis is
$(\zeta,1)$, where $\zeta^2+\zeta+1=0$ and
$\operatorname{Im}\zeta>0$.

For this curve, the complete finite calculation gives

$$
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
\text{level}&246\\
[\mathrm{PSL}_2(\mathbf Z):\overline\Gamma]&4920\\
\text{order-two elliptic fixed cosets}&0\\
\text{order-three elliptic fixed cosets}&3\\
\text{cusps}&20\\
\text{width of every cusp}&246\\
g(X_1)&400\\
\operatorname{rank}H_1(X_1,\mathrm{cusps};\mathbf Z)&819\\
\operatorname{rank}H_1(X_1;\mathbf Z)&800.
\end{array}
\tag{738.2}
$$

Every Manin edge has an explicit $\mathrm{SL}_2(\mathbf Z)$ matrix and
therefore exact rational endpoints. The output contains an integral basis
$\gamma_1,\ldots,\gamma_{800}$ of compact homology, represented by finite
integer sums of those edges, and the alternating matrix

$$
\Omega_{ij}=\gamma_i\cdot\gamma_j\in\mathbf Z,
\qquad \det\Omega=1.
\tag{738.3}
$$

The matrix uses the same order of the actual closed chains. It is not a
separately chosen rational symplectic form.

The original CM points have the following exact labels in the retained
zero-based breadth-first enumeration:

| Original point | Finite tame label | Retained coset indices | Meaning |
|---|---|---|---|
| $c_1$, $a=1$ | $C$ | $4424$ | Unique real order-three fixed coset |
| $\delta_\zeta c_1$, $a=\zeta$ | $I$ | $0$ | First deck translate |
| $\delta_\zeta^2c_1$, $a=\zeta^2$ | $C^2$ | $1258$ | Second deck translate |
| $c_0$, $a=0$ | The orbit of $S_2$ | $2876,2822,2823$ | One coarse point, represented by one length-three orbit |

All four rows use the same nonsplit pair
$\{\zeta,\zeta^2\}$ at $41$. In particular, the breadth-first reference
coset $0$ is **not** the original real $c_1$.

## 2. The full level-six graph and original nonsplit pair

Put

$$
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad R=ST,
\qquad C=\begin{pmatrix}0&1\\1&1\end{pmatrix}\in\mathrm{GL}_2(\mathbf F_2).
\tag{738.4}
$$

We use right multiplication on left cosets. The Brau–Jones graph is

$$
H_6=\{(\vartheta(g),g):g\in\mathrm{GL}_2(\mathbf F_3)\},
\tag{738.5}
$$

with the following complete quotient convention:

$$
\vartheta(S_3)=I,\quad \vartheta(T_3)=C,\quad
\vartheta\bigl(\operatorname{diag}(1,-1)\bigr)=T_2.
\tag{738.6}
$$

It can be defined without any unrecorded conjugation. Act on the three
unordered two-two partitions of $\mathbf P^1(\mathbf F_3)$,

$$
\{\infty,0\}\mid\{1,2\},\qquad
\{\infty,1\}\mid\{0,2\},\qquad
\{\infty,2\}\mid\{0,1\},
\tag{738.7}
$$

and identify these with $\infty,0,1$ in that order over $\mathbf F_2$.
The program generates all 48 values, checks the homomorphism on every
pair of elements, and verifies that the kernel has order eight. Thus the
actual $Q_8$ graph is retained, including its determinant-minus-one part.

On the complex determinant-one component, the tame left-coset label is

$$
k=\vartheta(g_3)^{-1}g_2\in\mathrm{GL}_2(\mathbf F_2).
\tag{738.8}
$$

Its right actions are

$$
k\buildrel S\over\longmapsto kS_2,
\quad k\buildrel T\over\longmapsto C^{-1}kT_2,
\quad k\buildrel R\over\longmapsto C^{-1}kC.
\tag{738.9}
$$

The $41$-factor is marked by the torus

$$
\mathsf T_\zeta=
\left\{\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}\right\},
\tag{738.10}
$$

which stabilizes the same pair $\{\zeta,\zeta^2\}$ used in the local CM
calculation. The left coset $N_{\mathrm{ns}}g$ is labeled by
$g^{-1}\{\zeta,\zeta^2\}$. There are $41(41-1)/2=820$ nonreal
conjugate pairs. In the basis $1,\zeta$, conjugation is

$$
\overline{a+b\zeta}=(a-b)-b\zeta.
\tag{738.11}
$$

Consequently the right $S,T$ actions on a pair representative are
$z\mapsto-1/z$ and $z\mapsto z-1$. The inverse on the coset label is
essential to the latter sign.

The program enumerates all $6\cdot820=4920$ product labels. It records a
matrix modulo 246 for each, then recomputes both labels from that matrix.
Every residue matrix is lifted to an integral determinant-one matrix;
the determinant and full congruence modulo 246 are checked separately
for every lift. This supplies actual rational endpoints for every
subsequent Manin edge.

## 3. Exact real marking of c1 and its three deck translates

The arithmetic real structure must be computed in the same level basis.
Set

$$
M=\begin{pmatrix}-1&-1\\0&1\end{pmatrix},\qquad M\bar\zeta=\zeta.
\tag{738.12}
$$

Complex conjugation has column matrix $M^{\mathsf t}$ on the period
basis $(\zeta,1)$. A coset $Hg$ has the corresponding level basis
$g^{\mathsf t}$, so its conjugate basis is
$M^{\mathsf t}g^{\mathsf t}=(gM)^{\mathsf t}$. Thus the operation on
the CM cosets is right multiplication by $M$.

Since $M=-\operatorname{diag}(1,-1)T$, the tame operation is

$$
k\longmapsto(T_2C)^{-1}kT_2.
\tag{738.13}
$$

The $R$-fixed tame labels are $C^a$, $a\in\mathbf Z/3$. On their
exponents, (738.13) is $a\mapsto-1-a$, whose unique fixed point is
$a=1$. At $41$, $M$ exchanges $\zeta$ and $\zeta^2$, so it preserves
the original pair. The unique real fixed CM label is therefore
$(C,\{\zeta,\zeta^2\})$.

Among the three unramified $j=0$ points of (738.1), only $a=1$ is real.
This proves that this label is exactly the original $c_1$ and is
compatible with $u=1/\sqrt[3]4$ in the chosen positive real embedding.
An explicit integral matrix representative is

$$
g_*=
\begin{pmatrix}15130&123\\123&1\end{pmatrix},\qquad
\det g_*=1,\quad g_*\equiv I\pmod{123},\quad g_*\equiv C\pmod2.
\tag{738.14}
$$

Its analytic representative on the quotient is $g_*\zeta$.
The finite program verifies this same matrix against the full label.

The translation $T^{82}$ is the identity at 41 and acts on the tame
label by $k\mapsto C^{-1}k$. With the original cusp phase of R575 it
is the deck transformation $\delta_\zeta:a\mapsto\zeta a$.
Hence the exact orbit is

$$
C\ (a=1)\ \longmapsto I\ (a=\zeta)
\ \longmapsto C^2\ (a=\zeta^2).
\tag{738.15}
$$

The program checks that this deck permutation has order three, commutes
with the $S,T$ monodromy, and is inverted by the real structure. It
checks that the real structure is an involution and sends $R$ to
$R^{-1}$. The label $(S_2,\{\zeta,\zeta^2\})$ has a length-three
$R$ orbit, invariant under both deck and conjugation; this is the one
coarse $c_0$ with $a=0$. Thus the output preserves both original points
needed for the same difference $q[c_1-c_0]$.

## 4. Integral relative and compact cycles

The $S$ permutation has no fixed point. The tame $R$ action has exactly
three fixed points. At 41, an $R$-fixed nonreal conjugate pair must be
$\{\zeta,\zeta^2\}$: the equation $Rz=z$ is
$z^2+z+1=0$, whereas $Rz=\bar z$ would give
$-1-z=\operatorname N(z)\in\mathbf F_{41}$, which is impossible.
The full $R$ action therefore has three fixed points. The tame $T$ is
a six-cycle and each nonreal-pair translation orbit at 41 has length
41, so all full cusp widths equal 246. The ordinary genus formula gives

$$
g=1+\frac{4920}{12}-\frac{3}{3}-\frac{20}{2}=400.
\tag{738.16}
$$

These values were also obtained from all actual permutation cycles,
rather than being accepted solely as predicted dimensions.

Choose the smaller coset in each $S$ pair as the positive Manin edge
$\{g0,g\infty\}$. There are 2460 edges. The corresponding Farey
dual graph has 1642 vertices, namely the $R$ orbits. The saturated
Manin three-term relations are its integral vertex coboundaries.
At a fixed $R$ vertex the unsaturated relation is $3e=0$; ordinary
surface homology is torsion-free, so the saturated relation is $e=0$,
which is the corresponding leaf-vertex coboundary.

A spanning tree of 1641 edges gives integral elimination with pivots
$\pm1$. The 819 remaining actual edges consequently form an integer
basis of relative homology. This is a unimodular graph elimination;
there is no passage from rational rank to an unproved saturation.

The relative boundary is the exact map

$$
\partial\{g0,g\infty\}=[g\infty]-[g0].
\tag{738.17}
$$

In finite labels it is the $T$ orbit of $g$ minus the $T$ orbit of
$gS$. The 819 columns are therefore the incidence matrix of a connected
graph on the 20 cusps. Choose a second spanning tree, of 19 edges.
For each of the remaining 800 edges, add the reverse tree path between
its cusp endpoints. Every resulting chain has zero boundary, as is
checked directly. Its coefficient on its own remaining edge is one,
and its coefficients on the other 799 remaining edges are zero.
Thus the 800 chains form an integral basis of the entire compact
kernel. This proves the asserted integer basis in (738.3).

## 5. The alternating pairing in that same basis

Contract the first tree and join the cusp faces along the second tree.
The retained surface has one vertex, one face, and 800 edges. Its
oriented face boundary has length 1600, and each edge appears once
with each sign. The direction is the positive cusp loop $T$, since
$\tau\mapsto\tau+w$ is positive around
$q=\exp(2\pi i\tau/w)=0$.

The Poincaré duals of the compact chains in Section 4 have the standard
coordinate values on the remaining dual edges. If $a_i(\ell)$ is the
value of the $i$th cochain on the $\ell$th oriented polygon side and
$A_i(\ell)$ is the sum over preceding sides, polygon triangulation gives

$$
2\Omega_{ij}=\sum_\ell
\bigl(A_i(\ell)a_j(\ell)-A_j(\ell)a_i(\ell)\bigr).
\tag{738.18}
$$

Indeed, on each small triangle the factor twice the wedge integral of
the two linear primitives is their determinant. Summing cancels the
interior edges and gives (738.18). This fixes the intersection sign
using the original surface orientation.

The exact computation verifies that every right side is even, that
$\Omega$ is alternating, and that its integer determinant is exactly
one. The polygon, chains, matrix, and their common edge order are all
stored together. They provide the integer period lattice and pairing
needed for the degree computation in R732 once the actual Hodge period
matrix is evaluated.

## 6. Public certificate and preservation of the full input

The public computation finished at `2026-11-14T15:48:22.165252+00:00`.
The exact core took 9.776806469999997 seconds. Its small final certificate
is
[p41-original-period-input-certificate.json](../computations/R738-p41-original-period-input/43612108090-1/p41-original-period-input-certificate.json).
The source, request, method, receipts, and final certificate are tied by
the retained manifests.

| Object | SHA-256 |
|---|---|
| Exact core | `b2dc9305b6d891f0a0fd4df3be6827d89cb065e0527f566eecb6b20c0b6f62eb` |
| Public driver | `e9dddc574bc386896afca475df3d61c30c5b8f69e9d18727786bef9d3d756fbb` |
| Method | `2bbebd7525203e4dd628d34762b5cc44f8061e2a2a0c6740a13a50ebadd5e7c9` |
| Request | `dd85d6ec5a17caeb31109e253fa180048147555ab2cbd8273bc3cc03e8b64c16` |
| Final certificate | `a853f36bf5d6f7d238e805a5c2134b2f7b3db17528195d56d980e66c9c769009` |
| Core receipt | `521443a37ab9e8f46f35ade971c737921b1a952ca9791bcbbf505724d513af4c` |
| Run receipt | `1d9db77b970ec0595894ffea7d544526fb8a34f132dd4f8fb6db0d57f5d83578` |
| Full-output manifest | `43e8726199560ac5b4cb109d6c583222a3fa4c0926ba3f12bd6c22f5859f39af` |

The complete reconstructible tables are retained in the artifact
`serre-global-R738-p41-original-period-input-43612108090-1`, with the
following exact files:

| File | Bytes | SHA-256 |
|---|---:|---|
| `original-cosets-and-markings.json.gz` | 135387 | `6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161` |
| `integral-compact-Manin-cycles.json.gz` | 170516 | `d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf` |

These include every finite label, integral lift, cusp, generating
permutation, real and deck action, both trees, closed chain, and matrix
entry. The repository contains the small certificate and manifest,
not a duplicated large intermediate table.

## 7. Scope and the next actual algebraic input

R735 has already constructed the original target elliptic model.
The present result supplies the marked source's integral topology for
R732. The same original positive CM factor still requires its Hodge
basis and complete finite adelic translate coefficients on this source,
including the determinant components and transport by $g_*$.
Evaluating their periods by R732 then supplies the integer lattice
conditions for an actual map.

In particular, neither a standard newform at level $9p^2$ nor a basis
on a different $\Gamma_1$ curve may be substituted for this missing
marked Hodge input. No quotient rational function, coordinate of
$\beta=q[c_1-c_0]$, actual height coefficient, or height zero exclusion
is asserted by (738.2)–(738.3).

## Sources and dependencies

- The [pre-run method](../notes/R738-p41-original-period-input-method.md)
  and [exact core](../scripts/R738_p41_original_period_input.py) specify
  the finite construction and all verification steps.
- Brau–Jones, *Elliptic curves with 2-torsion contained in the 3-torsion
  field*, [author manuscript](https://homepages.math.uic.edu/~ncjones/2tin3t.pdf):
  the original full $Q_8$ graph and level-six model.
- William Stein, *Modular Forms: A Computational Approach*,
  [General Modular Symbols](https://wstein.org/books/modform/modform/modular_symbols.html):
  the Manin presentation for arbitrary finite-index subgroups. The
  integral saturation, both tree eliminations, and pairing calculation
  used here are specified directly above.
- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md),
  [R616](R616-original-CM-point-difference-and-explicit-height-basis.md):
  the original cubic direction, deck convention, and actual CM point
  difference.
- [R732](R732-original-CM-period-kernel-and-bounded-rational-function-recovery.md),
  [R735](R735-exact-original-p41-CM-model-and-Neron-input.md):
  the exact period-to-function interface and computed original target.
