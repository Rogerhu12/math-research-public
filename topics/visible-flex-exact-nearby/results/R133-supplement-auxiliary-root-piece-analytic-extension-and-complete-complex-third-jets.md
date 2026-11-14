# R133 supplement: auxiliary analytic continuation of one root piece and its complete complex third jets

2026-11-14, phase_inverse.

**An exact continuation and directed evaluation contract.** A larger
auxiliary complex domain may be used to bound derivatives of the
actual root germ. The auxiliary functions keep the original scalar
germ polynomials, original root-piece cubics, exact physical scaling,
continuous value repairs and complete $193$-component parameter
direction. They agree with the actual piecewise family on the
original root piece. They are not asserted to equal that piecewise
family outside the piece.

New intrinsic and polynomial evaluations on the larger domains are
new mathematical work. They must run in the public repository's
Actions and preserve every domain and derivative prefix. The original
small-domain certificates remain unchanged.

## 1. The auxiliary object and its precise identification domain

Let $[g_-,g_+]$ be the exact original common scalar germ containing
the actual root, and let $[c_-,c_+]$ be original candidate/response
piece $2549$. Their exact endpoints are retained from the original
complex-germ native. The actual root lies in $[r_-,r_+]$.

On this scalar germ, use exactly the scalar polynomials selected
by the original `BulkTarget.set_cell` and
`ParameterDiskBody.set_cell` construction. Their anchor, complete
affine parameter coefficients and degree at most $20$ remain fixed.
The degree bound follows from the original degree-five spline
factors: the largest product is the phase factor times the cube
of the degree-five base factor. The remaining scalar products
have no higher degree.

Continue these same polynomials holomorphically. Reconstruct the
original unit tangent and its complete angular primitive by the
same trigonometric formulas, full Fourier remainder and bilinear
energy. This defines an auxiliary intrinsic germ wherever its
actual denominators and chosen square-root branches are separated.
The compact $\nu$ bump is identically zero on the original germ;
its auxiliary continuation here is the identically zero function.

For the moving background and direction, continue the **same**
$65$- and $193$-component dyadic cubics from piece $2549$.
The background is multiplied by its original exact physical
amplitude. The response is already physical. Add the same original
constant value repairs on this piece. In radial orders $p\ge1$,
those constant repairs have derivative zero.

The auxiliary explicit family has the same complex parameter
disk $|\delta|\le10^{-8}$ and fixed $\eta_0$. For intrinsic
enclosures the original whole affine-parameter box may still
be retained as a larger set. In particular it must not be
silently replaced by sampled parameter values.

On the open intersection
$$
 (g_-,g_+)\cap(c_-,c_+)
 \tag{E.1}
$$
all these auxiliary functions equal the actual functions of the
given family. This follows from their identical exact local
formulas. There is no assertion that the auxiliary extension
equals a neighboring physical polynomial piece.

## 2. The original complete primitive remains complete on the new domain

For a proposed rational radius $R>10^{-5}$ evaluate the auxiliary
functions on the whole rectangle
$$
 \operatorname{Re}r\in[r_- -R,r_+ +R],\qquad
 |\operatorname{Im}r|\le R .
 \tag{E.2}
$$
No containment of this rectangle in (E.1) is required for the
auxiliary evaluation. Its original scalar germ and its original
candidate piece nevertheless remain explicitly recorded.

The original finite tangent primitive is obtained from the same
$512$-point directed Fourier construction. It is accompanied by
the full infinite primitive remainder. In the original
`unit_tail_errors` formula, the scalar-polynomial radius is
$$
 |r-\text{anchor}|+R_{\rm tail},
 \tag{E.3}
$$
including the complex radial box and the original positive radial
Cauchy margin $R_{\rm tail}$. Evaluate that expression anew on
(E.2). The auxiliary polynomials and trigonometric functions are
entire before taking the subsequent metric quotients, so the
same complete primitive estimate applies on this declared
extension. The numerical calculation must retain the full
remainder and not reuse its old small-domain value.

The angular energy is the analytic bilinear expression
$\langle F_r\cdot F_r\rangle$. No complex conjugation and no
extraction of a real part is permitted on (E.2).

## 3. Six original primitive jets pay complete intrinsic third jets

Use the original `CubicCodazziTarget.scalar_jets_and_fourier`
construction, which gives $F^{(j)}$ for $0\le j\le5$ and a
complete primitive-error bound for each derivative. For its
finite Fourier polynomials $P_j$ and full errors $\varepsilon_j$,
a complete directed product-mean error is
$$
 \left|\langle F^{(i)}\cdot F^{(j)}\rangle
        -\langle P_i\cdot P_j\rangle\right|
 \le3\{N_i\varepsilon_j+N_j\varepsilon_i+
                         \varepsilon_i\varepsilon_j\},
 \tag{E.4}
$$
where $N_j$ bounds the complete finite component Wiener sums.
A complex disk error may be enclosed by the corresponding
rectangle in both real and imaginary components.

Consequently the ordinary derivatives
$$
 E^{(m)}
 =\sum_{j=0}^m{m\choose j}
   \langle F^{(j+1)}\cdot F^{(m-j+1)}\rangle,
 \qquad 0\le m\le4,
 \tag{E.5}
$$
are paid before any quotient is differentiated. The same original
finite scalar polynomial gives the physical radius derivatives
$a^{(0)},\ldots,a^{(5)}$.

Here $a$ denotes the original physical radius in the intrinsic
metric formulas, not the root characteristic coefficient
$\eta\sqrt{k}$. To form derivatives, put
$$
 A(t)=\sum_{j=0}^5\frac{a^{(j)}}{j!}t^j,\qquad
 \mathcal E(t)=\sum_{j=0}^4\frac{E^{(j)}}{j!}t^j .
$$
Complete truncated power-series arithmetic then gives
$$
 \begin{aligned}
 K(t)&=-A''(t)A(t)^{-1}\mathcal E(t)^{-1}\\
 &\quad+\tfrac12A'(t)\mathcal E'(t)
                    A(t)^{-1}\mathcal E(t)^{-2},\\
 \beta(t)&=A'(t)A(t)^{-1},\\
 \gamma(t)&=\mathcal E(t)^{1/2}A(t)^{-1},\\
 s(t)&=-A(t)
  \left\{\frac{\mathcal E(t)}
                 {\mathcal E(t)-A'(t)^2}\right\}^{1/2}.
 \end{aligned}
 \tag{E.6}
$$
For each displayed coefficient only terms through degree three
are used. The stored ordinary derivative of order $j$ is
$j!$ times its series coefficient. The complex inverse and
square-root recurrences are
$$
 b_0=a_0^{-1},\quad
 b_n=-a_0^{-1}\sum_{j=1}^na_jb_{n-j},
$$
$$
 q_0=a_0^{1/2},\quad
 q_n=\frac{a_n-\sum_{j=1}^{n-1}q_jq_{n-j}}{2q_0}.
 \tag{E.7}
$$
Thus no derivative is inferred from a lower-order value-only
error. The actual finite energy, every infinite product fee,
and the factorial convention remain inspectable in the native.

Before (E.6), the entire new rectangle must satisfy strict
right-half-plane gaps for $a$, $E$ and $E-(a')^2$.
The selected rotational branch must have $\operatorname{Re}s<0$.
A useful root continuation additionally checks
$\operatorname{Re}K_r>0$ on the full rectangle.
A failed gap is recorded as a failed domain; it cannot be
replaced by an absolute-value denominator.

## 4. Complete polynomial and parameter derivatives

For each original physical component
$$
 p(r)=c_0(r-c_-)^3+c_1(r-c_-)^2+c_2(r-c_-)+c_3
$$
evaluate its value and its first three derivatives by bounded
Horner multiplication on (E.2):
$$
 \begin{aligned}
 p'(r)&=(3c_0(r-c_-)+2c_1)(r-c_-)+c_2,\\
 p''(r)&=6c_0(r-c_-)+2c_1,\qquad
 p'''(r)=6c_0 .
 \end{aligned}
 \tag{E.8}
$$
All original $65$ and $193$ components are retained. In particular
the background even mean includes the full new $s^{(p)}$, and
the direction mean is its original component $96$.

For a safely bounded constant direction repair, the already
completed root-scalarization native saves
$B_{\rm raw}$ and an upward-rounded $B_{\rm raw}+e$ with $e\ge0$
for every component. Therefore
$$
 e\le (B_{\rm repaired})_{\rm upper}
                    -(B_{\rm raw})_{\rm lower}.
 \tag{E.9}
$$
This pays a valid constant repair enclosure on the auxiliary
continuation. It does not redefine the direction, assume its
repair to be zero, or differentiate that value enclosure.
The exact background repair offsets remain their original
$65$ rational values.

The full parameter radius is applied only after retaining these
complete derivative arrays. With $m$ the true even mean,
$$
 \eta^{(p)}
 =-\sum_{j=0}^p{p\choose j}\gamma^{(j)}m^{(p-j)}
 \tag{E.10}
$$
holds for $0\le p\le3$. The same common parameter acts in all
components; independently enclosing its contributions only
enlarges the bound.

## 5. Identification of subsequent analytic fold and amplitude bounds

The root in the original germ is a root of the auxiliary
intrinsic $K$ by (E.1). The analytic divided curvature
$$
 k(\rho)=\int_0^1K_r(r_*-t\rho)\,dt
 \tag{E.11}
$$
therefore equals $-K(r_*-\rho)/\rho$ away from zero and has
the same analytic root value at zero. A positive real-part
bound for the new $K_r$ box pays the corresponding complex
gap for $k$; its next two derivatives obey
$$
 |k_\rho|\le\tfrac12\sup|K_{rr}|,\qquad
 |k_{\rho\rho}|\le\tfrac13\sup|K_{rrr}|.
 \tag{E.12}
$$
Both derivative bounds are now complex-domain bounds from
(E.6), not an extension of the old real-only third jets.

Once a consumer separately pays its complete flow, fold and
nonzero gaps, the closed $G,A,X,T$ formulas define the auxiliary
leading amplitude. The finite derivative proof (L.12)--(L.24)
applies on this genuinely analytic single-piece extension:
its integrals run on straight radial segments and its estimates
use the same complex moduli and positive domain margins.
There are no auxiliary polynomial seams, so the auxiliary
version of its seam sum is zero. This statement does not
delete any seam of the original global piecewise problem.

On a smaller neighborhood lying in (E.1), analytic ODE
uniqueness and the same exact root normalization identify the
auxiliary fold and leading amplitude with the original ones.
The same holds for the zero-common-trace forced amplitude
when its full first forcing and characteristics have been paid.
This is an identification of local analytic germs. One may then
use larger auxiliary complex domains to bound derivatives of
that germ on the smaller original neighborhood.

No piecewise trial is replaced on a neighboring real piece,
no new cutoff is introduced, and no artificial interface source
is created. The original real seams, old primitive/inverse
remainders, independent mean and all exterior source ports
retain their original equations and fees.

## 6. Execution and scope

The proposed first consumer evaluates only the new auxiliary
intrinsic and complete finite-polynomial jets on four rational
radii:
$$
 R\in\{1/10000,\ 1/2000,\ 1/1000,\ 1/500\}.
$$
It records the exact original scalar and polynomial germs,
the whole affine-parameter identity, all original source and
NPZ hashes, each attempted domain, every actual denominator
gap, and every completed derivative prefix. Later resumes
must reuse identical accepted native records; a scientific
source change requires an explicit separately reviewed migration.

These domain and third-jet results are inputs to the subsequent
fold/leading/forcing consumer. They alone are not the enlarged
fold, a next-amplitude estimate, a physical continuation across
a seam, or a numerical strong-return norm. A failed larger
domain must remain visible alongside any smaller successful
domains, and no success on one radius certifies another radius.
