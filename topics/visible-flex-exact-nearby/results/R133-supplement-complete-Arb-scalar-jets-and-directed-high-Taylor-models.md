# R133 supplement: complete Arb scalar jets and directed high Taylor models

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved algorithm, with an actual complete first-germ computation.**
The actual intrinsic target, with its full infinite angular primitive,
admits directed scalar jets of every declared order $3\le p\le12$
through a finite Laurent calculation and an explicit infinite Fourier
remainder. The same jets give exact dyadic degree-$p$ models of
$\beta,K,s,\gamma,q=\sqrt{-K}$ on closed negative cells. They use the
true scalar and compact-control germs; no angular grid or primitive
frequency cutoff is treated as exact.

For the actual fixed final $\nu$, original affine offset $\eta=0$, and
the first complete intrinsic germ

$$
 I_0=\left[0,\frac{2609037194989121}{1152921504606846976}\right],
                                                               \tag{J.1}
$$

two actual degree-seven models suffice, with

$$
 \int_{I_0}\sum_{f\in\{\beta,K,s,\gamma,q\}}
                   |f(r)-\widetilde f(r)|\,dr
 <9.117418\,10^{-17}.                                    \tag{J.2}
$$

This is a complete scalar coefficient result. It does not assert that
all 169 negative germs have already been computed, or that a true
characteristic flow, conjugacy, arithmetic condition, or complete
operator inverse has been certified.

## 1. Exact finite scalar germs before any interval evaluation

The underlying object is
`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json`,
SHA256
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`.
The original exact affine centre is loaded by the existing target
loader. The additional original affine offset is applied once, after
the origin and direction spline germs have been differentiated.

On each common actual knot cell, the two seed angular phases $b,g$,
radius $a$, and height $z$ are finite radial polynomials. The seed and
raw spline degrees are five, so $b$ has degree at most twenty and $g$
at most fifteen; the radius splines have degree five and the height
integrals degree six. The affine direction has the same degree limits.
The producer checks the resulting maximum degree twenty explicitly.

At the exact rational midpoint of a true common cell, the existing
de Boor polynomial germ is evaluated with Arb series precision 21.
Every one of its 21 normalized coefficients is retained. These
coefficient balls are cached before evaluating a radial interval; the
subsequent evaluation is exact polynomial Horner arithmetic on an Arb
series $r+\epsilon$. In particular a double-box field cache is not used
to supply the high-precision scalar coefficients.

For scalar jet order $p$ the calculation retains $p+3$ normalized
coefficients of $a,z,b,g$. The common cell is also cut at $1/20$ and
$9/50$, the genuine endpoints of the compact control. A request that
crosses any such cell is rejected. The procedure never extends a
polynomial expression across a different true spline germ.

## 2. Entire angular exponentials, including every omitted frequency

Write $\zeta=e^{i4\theta}$. Since the seed phases are real odd sine
polynomials, $i b$ and $i g$ have real antisymmetric Laurent
coefficients. For each of $b+g,b-g,g$, let

$$
 A(\epsilon,\zeta)=\sum_{d=0}^{p+2} A_d(\zeta)\epsilon^d
       +O(\epsilon^{p+3})
$$

be its imaginary phase. Each $A_d$ is a complete finite Laurent
polynomial; all 24 seed angular indices are retained.

Split $A_0=P(\zeta)+Q(\zeta^{-1})$ into its positive and negative
parts, with zero constant coefficient. Formal Arb series give every
coefficient through degree $n$ of $\exp P$ and $\exp Q$. For a chosen
positive weight $\sigma$ define
$M_{P,\sigma}=\sum_j|P_j|e^{j\sigma}$, and similarly for $Q$.
The retained product $E_0^{[n]}$ has full Wiener remainder

$$
 \|e^{A_0}-E_0^{[n]}\|_{A_0}
 \le e^{-\sigma(n+1)}
 \left[e^{M_{P,\sigma}+M_{Q,0}}
       +e^{M_{Q,\sigma}+M_{P,0}}\right]
 =:\epsilon_0.                                           \tag{J.3}
$$

Indeed the one-sided omitted coefficient sum is bounded by its weighted
norm times $e^{-\sigma(n+1)}$. Multiplication by the other full factor
uses its complete $A_0$ norm; the finite retained factor has no larger
$A_0$ norm. The producer chooses a certified integer cutoff with
$\epsilon_0<2^{-160}$, preserving the whole finite product rather
than sampling it on a periodic grid.

All normalized radial derivatives follow from finite Bell polynomials:

$$
 B_0=1,\qquad
 B_d=\frac1d\sum_{k=1}^d kA_kB_{d-k},\qquad
 [e^{A}]_d=e^{A_0}B_d.                                    \tag{J.4}
$$

Therefore the complete radial coefficient remainder is
$\epsilon_d\le\epsilon_0\|B_d\|_{A_0}$. The code forms these finite
Laurent products for every required $d$ before collapsing to norms.
This is a full angular exponential estimate for every radial derivative,
not a finite DFT alias estimate.

## 3. Actual unit primitive and complete radial energy

In the rotating radial/tangential frame the original tangent correction
is

$$
 T_x=-\cos g\sin b,\qquad
 T_y=\cos g\cos b-1,\qquad T_z=\sin g.                    \tag{J.5}
$$

The identities involving $b+g,b-g,g$ reconstruct these three components
from the exponentials in (J.3). Write $T_x=i t_x$, $T_y=t_y$,
$T_z=i t_z$, where the displayed lower-case symbols have real Laurent
coefficients. For physical frequency $n=4j$, the normalized primitive is

$$
 P_x[n]=\frac{-n t_x[n]+t_y[n]}{1-n^2},\qquad
 P_y[n]=i\frac{-t_x[n]+n t_y[n]}{1-n^2},\qquad
 P_z[n]=\frac{t_z[n]}n\quad(n\ne0).                       \tag{J.6}
$$

The $P_y,P_z$ means are exactly zero. Formula (J.6) follows by solving
the two rotating-frame derivative equations
$i nP_x-P_y=T_x$, $P_x+i nP_y=T_y$ and the vertical derivative.
At the mean, $P_x[0]=T_y[0]$ is retained.

If $e_x,e_y,e_z$ bound the full $A_0$ tails in (J.5), then the complete
primitive tails are bounded componentwise by

$$
 e_{P_x}\le\frac4{15}e_x+e_y,\qquad
 e_{P_y}\le\frac1{15}e_x+\frac4{15}e_y,\qquad
 e_{P_z}\le\frac14e_z.                                   \tag{J.7}
$$

The $e_y$ factor one pays the nonzero primitive mean. For nonzero
physical frequencies $|n|\ge4$, the remaining factors follow directly
from $1/(n^2-1)\le1/15$ and $|n|/(n^2-1)\le4/15$.

The complete reference position is
$F=(a+aP_x,\ aP_y,\ z+aP_z)$ in the rotating frame. For each normalized
radial coefficient, all products with $a$ and every primitive remainder
in (J.7) are included. Write the finite coefficient as $F_d^\mathrm{fin}$
and its componentwise error as $\varepsilon_{d,c}$. The actual radial
metric is

$$
 E=\langle F_r\cdot F_r\rangle,\qquad
 E_d=\sum_{i=0}^d(i+1)(d-i+1)
       \langle F_{i+1}\cdot F_{d-i+1}\rangle.              \tag{J.8}
$$

The finite zero Fourier coefficient is computed by complete Laurent
convolution. The tangential component carries its exact $i^2=-1$
factor. If $N_{d,c}=\|F_{d,c}^{\rm fin}\|_{A_0}$, each product error is
bounded by

$$
 N_{i+1,c}\varepsilon_{d-i+1,c}
 +N_{d-i+1,c}\varepsilon_{i+1,c}
 +\varepsilon_{i+1,c}\varepsilon_{d-i+1,c}.                 \tag{J.9}
$$

These are summed over all three components and every $i$ with the
weights in (J.8). The calculation retains $E_0,\ldots,E_{p+1}$, which
together with $a_0,\ldots,a_{p+2}$ suffice for all scalar jets below.

## 4. Same compact metric and complete scalar jets

The actual compact function is

$$
 w(r)=4096t^6(1-t)^6,\quad
 t=\frac{r-1/20}{9/50-1/20},\quad 1/20\le r\le9/50,
 \qquad w=0\text{ outside}.                              \tag{J.10}
$$

It is a $C^5$ compactly supported polynomial, not an exponential bump.
The metric uses $E_\nu=E e^{\nu w}$. With
$\beta=a'/a$ and $K_0=-a''/(aE)+a'E'/(2aE^2)$,

$$
 K= e^{-\nu w}\left(K_0+\frac{\nu\beta w'}{2E}\right),
 \quad\gamma=\frac{\sqrt{E_\nu}}a,
 \quad s=-a\sqrt{\frac{E_\nu}{E_\nu-(a')^2}}.              \tag{J.11}
$$

These are formal-series operations on the complete coefficients in
(J.8). The producer requires $a,E_\nu,E_\nu-(a')^2>0$ on the whole
requested real interval before using the positive square roots. It
requires sufficient output series precision before reading any declared
derivative. To add $q=\sqrt{-K}$ on a negative cell, the cache additionally
requires $K<0$ throughout that cell and sets the global series cap to
at least $p+1$ before the square root; it checks that the returned series
retains every one of these coefficients. Thus no high derivative is
silently read from a truncated formal series.

The first actual cache uses

$$
 \nu=-\frac{2572625729470897}{72057594037927936},
 \qquad \eta=0.                                          \tag{J.12}
$$

The general scalar producer can retain a whole original affine offset
interval, but (J.2) and the current cache are expressly for (J.12).
A later phase choice of $\nu$ requires its own parameter or recomputation
fee; the current fixed metric is not silently varied inside a flex family.

## 5. Exact dyadic polynomial models and their uniform remainder

Let $[c-h,c+h]$ be a closed true cell and let $f$ be any of
$\beta,K,s,\gamma,q$. The point jets at $c$ enclose all normalized
derivatives through order $p-1$; the whole cell encloses $f^{(p)}$.
Choose exact dyadic numbers $a_0,\ldots,a_p$ by taking the Arb
midpoints of these normalized point jets and of the whole
$f^{(p)}/p!$ interval. Put

$$
 \widetilde f(r)=\sum_{j=0}^p a_j(r-c)^j.
$$

Taylor's integral remainder, with the constant $p!a_p$ subtracted
inside that integral, gives the uniform bound

$$
 \boxed{\quad
 \|f-\widetilde f\|_{L^\infty[c-h,c+h]}
 \le\sum_{j=0}^{p-1}
       \left|\frac{f^{(j)}(c)}{j!}-a_j\right|h^j
    +\frac{h^p}{p!}\sup_{[c-h,c+h]}|f^{(p)}-p!a_p|.
 \quad}                                                     \tag{J.13}
$$

Every term on the right is evaluated outwards using the full scalar
jets. The same estimate applies to either side of $c$. The final
derivative's interval width, rather than its absolute magnitude, is
paid after choosing $a_p$. This is an exact reorganization of the
remainder and does not assume an uncomputed $(p+1)$st derivative.

All model coefficients are saved as exact rational strings. Their
denominators are powers of two, since they are Arb midpoints taken
*after* normalization by the factorial. Complete uniform remainders
and complete point/whole exponential error data are saved with every
accepted cell.

## 6. Exact adaptive allocation and actual first-germ result

The intended full interval ends at

$$
 r_b=\frac{1191984371497}{5000000000000}-2^{-32},             \tag{J.14}
$$

strictly before the already proved common root lower bound. Splitting
at every true target/control germ produces 169 intervals. This is a
declared domain and a resumable work list, not a claim that the work
list is complete.

For a cell $[a,b]$, let $e(a,b)$ be its length times the sum of the five
actual uniform errors in (J.13). A convenient positive allocation
weight is

$$
 W(a,b)=2\big(\sqrt{r_{*,\rm lower}-a}
                  -\sqrt{r_{*,\rm lower}-b}\big).          \tag{J.15}
$$

The code accepts a cell only if the computed upper bound for $e(a,b)$
is below the computed lower bound for
$2^{-42}W(a,b)/W(0,r_b)$. The weights telescope exactly. Thus a complete
accepted cover would prove an integrated scalar remainder below
$2^{-42}$. The allocation is only an adaptive device: every saved
certificate records its actual error, and no weighted allocation is
substituted for a mathematical remainder.

On $I_0$ the whole-cell attempt did not meet this allocation and was
retained in `rejected_cells`. Its two exact half cells did. Their
computed combined error is less than $9.117418\,10^{-17}$, below
the first-germ allocation $1.081778\,10^{-15}$. All six complete
germ gates passed: the saved germ loop took 24.19 seconds, and the
complete invocation including initialization took 26.49 seconds.
This improves the valid third-order
pilot, which required 64 cells and 140.63 seconds on the same germ,
without relaxing the requested integrated scalar budget.

An earlier high-order prototype used the global series cap six while
forming $q$ through order seven. Its whole attempt is explicitly
invalidated and excluded; the corrected producer both raises the cap
and checks the returned precision. The successful native in this
theorem was generated afresh by that corrected source. The original
third-order pilot and the separate complete scalar provider were not
affected by this cache-level error.

The cache writes a partial checkpoint after every actual accept or
subdivide decision. It resumes only when source, provider, object,
precision, parameter, and all numerical settings agree. Completed
germs are never silently recomputed under changed bytes. Failures and
rejected interval attempts are retained.

## 7. Files, commands, and the next actual consumer

- Full scalar provider:
  `scripts/fourfold_codazzi_phase_complete_Arb_high_scalar_jets.py`.
- Resumable model producer:
  `scripts/fourfold_codazzi_phase_Arb_high_Taylor_cache.py`.
- Actual complete first-germ native:
  `notes/2026-11-14-R133-complete-Arb-high-scalar-Taylor-first-germ-native.json.gz`.
- Attempt and scope record:
  `notes/2026-11-14-R133-complete-Arb-scalar-model-attempts.md`.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 \
  scripts/fourfold_codazzi_phase_Arb_high_Taylor_cache.py \
  --germ-start 0 --germ-stop 1 \
  --out-dir /workspace/scratch/ac0d699811ad/phase-scalar-cache-20261114/high7-pilot02
```

For a new worker, disjoint ranges of `--germ-start`/`--germ-stop`
partition the same complete target without changing the models or
normalization. `--resume` accepts only exact matching checkpoints.
The final manifest must prove all 169 germs are present before a full
negative coefficient cover is asserted.

The next ray consumer must combine these scalar models with every exact
candidate Fourier coefficient and repair, pay the nonlinear products
in the actual characteristic field, and separately pay the final root
sliver. A finite transported phase must have its full radial/angular
PDE residual and every interface defect bounded. None of those steps
is replaced by the scalar error (J.2), and no floating conjugacy fit is
identified with a true one here.
