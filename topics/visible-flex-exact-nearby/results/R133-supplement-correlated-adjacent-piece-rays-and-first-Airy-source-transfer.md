# R133 supplement: correlated transport from the root piece into its two genuine neighbors

2026-11-15, visible-exact / phase_inverse.

**Proved exact identities and conditional enclosure contract.**
This note compares the actual first Airy correction on a neighboring
physical piece with an auxiliary analytic continuation of the original
root-piece coefficients. Both objects have the same entry trace at their
genuine common physical seam. Their difference is transported on the
actual two rays. The complete local numerator and old-circle source
bounds can then retain the previously computed signed root Taylor
correlations.

The auxiliary continuation is not the physical background beyond its
original piece. Its principal-ray difference is paid explicitly.
No numerical smallness, domain enlargement, seam cancellation, strong
return or high-frequency inverse is asserted before the new public
consumer passes the stated gates.

## 1. Objects, traces and domains

The actual background is the same repaired 65-mode centre plus its
complete repaired 193-mode parameter direction, at fixed intrinsic
$\eta_0$ and real $|\delta|\le10^{-8}$.
The intrinsic functions $K,\beta,\gamma,s$ and the true root $r_*$ are
unchanged. Write $\rho=r_*-r$ and $b=\beta$.

The reference, marked by a bar, uses the original piece-2549 cubic
coefficients and its exact repairs, analytically evaluated beyond that
piece only where their already paid auxiliary germ applies.
Its intrinsic functions are the same functions of $r$, not a new metric.
The reference fold, leading amplitudes and first correction are the
analytic functions whose complete root Taylor coefficients and
holomorphic remainder bounds have already been certified.

For either neighboring physical piece $I$, let $r_e$ be its genuine
interface with piece 2549 and put $\rho_e=r_*-r_e$.
The present contract requires, and a consumer must verify:

1. The complete closed physical interval $I$ lies in the same original
   intrinsic germ. The reference old-product inverse image lies in its
   paid holomorphic domain, including $|\rho|<1/6000$ and the declared
   angular strip.
2. Every allowed true root gives $0<h\le|\rho|\le H$ throughout $I$.
   The exact physical endpoints and the entire root interval are used.
3. The actual and reference backgrounds have their exact repaired common
   value at $r_e$. All Fourier components and the repaired direction mean
   are included. Containing zero in a computed interval alone is not a
   proof of this exact identity.
4. Both folds and both $M_0$ matrices retain their original nonzero gaps,
   and every reference evaluation and complex-angle trajectory remains
   inside a common declared domain.

The exact entry identities are
$$
 (X,A,G,w_1)(\rho_e,\phi)
   =(\bar X,\bar A,\bar G,\bar w_1)(\rho_e,\phi).
 \tag{N.1}
$$
They follow because the physical and auxiliary constructions agree from
the root through the whole original root piece. The first-order
transport selects their common value at the interface.
These common values are generally nonzero. They are copied as complete
known traces; the actual transport is never restarted with zero data.
Only their difference is zero under this exact identity.
If a consumer has only a nonzero certified difference enclosure, that
entire initial difference must instead be retained in the two comparison
integrals below.

The same statement does not identify their second or third radial jets
on the two sides. The background derivative jumps and all resulting
forcing and reconstructed physical jumps remain.

This compares two known constructions. It does not tilt an unknown
ordinary source onto a graph.

## 2. Complete finite background differences

Put $\Delta f=f-\bar f$. On the new physical piece, compute
$\Delta u,\Delta v$ as differences of the original signed cubic
coefficients before taking absolute values.
They remain cubic in the physical radial coordinate and affine in the
same parameter $\delta$. The exact common repaired value gives zero
constant term when they are expanded at $r_e$.
No derivative at the seam is set to zero.

The complete scalar differences are
$$
 \Delta m=\langle\Delta v\rangle,\qquad
 \Delta\eta=-\gamma\Delta m,\qquad \eta=-\gamma m,
$$
$$
 \Delta S
 =2\bar u\,\Delta u+(\Delta u)^2
   +K\{2\bar v\,\Delta v+(\Delta v)^2\},
 \qquad
 \Delta d=-bI(\Delta S).
 \tag{N.2}
$$
Here $I$ is exactly the original old-circle primitive with its mean
projection. The mean $\langle\Delta S\rangle$ is separately retained.
The Fourier support of each full quadratic expression is at most 192;
all of it is included, including the ordinary physical mean.

All radial derivatives through order two follow by differentiating
(N.2), using the common intrinsic jets and the actual cubic derivative
differences. There is no source from a mismatch of intrinsic parameters.

The same signed polynomial algebra supplies complete differences of
$\ell,e,B_{\rm coef},T_0,V_0,\vartheta$ and their required first radial
derivatives from their original definitions.
A bound on $\Delta(uv)$, for example, comes from its signed difference or
from the exact identity
$\Delta(uv)=(\Delta u)v+\bar u\,\Delta v$.
Subtracting two upper bounds is never used.

## 3. A sharper divided-curvature jet from already completed data

There is no need to use
$(|K_{rrr}|+3|k_{\rho\rho}|)/h$ if the existing root Taylor coefficients
and the common complex germ give a sharper bound.

Let $\mathscr K(\rho)=K(r_*-\rho)=-\rho k(\rho)$.
The true root identity is $\mathscr K(0)=0$.
Suppose its already completed coefficients through degree 15 and the
bound
$$
 |\mathscr K_{\rho\rho\rho}(\rho)|\le M_3
 \quad (|\rho|\le R_c)
$$
refer to this same true-root centre and intrinsic germ.
If the original native is a fixed physical complex rectangle, first
verify that the full root-centred disk, including root uncertainty, is
contained in that rectangle.

Write
$$
 \mathscr K(\rho)=\sum_{j=1}^{15}K_j\rho^j+\text{tail},
 \qquad
 k_{\rm fin}(\rho)=-\sum_{j=1}^{15}K_j\rho^{j-1}.
$$
The root coefficients are ordinary Taylor coefficients, so any stored
true derivatives are divided by their factorials and acquire
$(-1)^j$ when converted from $r$ to $\rho$.
For $|\rho|\le H<R_c$, $x=H/R_c$, Cauchy applied to
$\mathscr K_{\rho\rho\rho}$ gives
$$
 |K_{n+1}|
 \le {M_3R_c^{2-n}\over(n+1)n(n-1)},\qquad n\ge15.
 \tag{N.3}
$$
Consequently the complete tails for $k$ and its first three derivatives
satisfy
$$
 \begin{split}
 |k-k_{\rm fin}|&\le {M_3R_c^2x^{15}\over14\cdot15\cdot16(1-x)},\\
 |k_\rho-(k_{\rm fin})_\rho|&\le
                       {M_3R_cx^{14}\over14\cdot16(1-x)},\\
 |k_{\rho\rho}-(k_{\rm fin})_{\rho\rho}|&\le
                       {M_3x^{13}\over16(1-x)},\\
 |k_{\rho\rho\rho}-(k_{\rm fin})_{\rho\rho\rho}|&\le
                       {M_3x^{12}\over R_c(1-x)}.
 \end{split}
 \tag{N.4}
$$
For the last line the exact coefficient factor is
$(n-2)/(n+1)\le1$. The other reciprocal coefficient factors decrease monotonically and
are bounded by their first omitted value. These are full infinite
tails, not zeros assigned to unsaved coefficients.

The same argument applies to the common intrinsic $\beta,\gamma,s$
when useful, with their own completed Taylor orders and certified
complex derivative bounds. This is new scalar consumption of old
coefficients, not a new intrinsic target or FFT.

## 4. The actual two rays, including their principal difference

Use the original fold notation
$$
 x=X_\phi,\quad y=T_\phi,\quad T=-\rho A^{2/3},\quad
 Q=\eta\sqrt{k}\,A^{-1/3},\quad
 DT=Qx,\quad DX=-QTy,
$$
where $D=-\partial_\rho-d\partial_\phi$.
Choose compatible strict-side branches $\tau^2=T$ and
$\bar\tau^2=\bar T$.
Then $Q\tau=\eta\sqrt K$ and
$\bar Q\bar\tau=\bar\eta\sqrt K$ on the same chosen branch.

For $\epsilon=\pm1$ and $\sigma=\pm1$, set
$$
 \Theta_\sigma=X+\frac23\sigma i\epsilon T\tau,\qquad
 v_\sigma=-d-\sigma i\epsilon Q\tau.
$$
The exact equations are
$$
 (\Theta_\sigma)_\rho=v_\sigma(\Theta_\sigma)_\phi,
 \qquad
 \Delta v_\sigma=-\Delta d-\sigma i\epsilon\sqrt K\,\Delta\eta.
 \tag{N.5}
$$
The barred equations have their own barred velocities.
Thus the principal drift and principal radial-speed differences are
both retained.

Let $e_\sigma=\Theta_\sigma-\bar\Theta_\sigma$. From (N.1),
$$
 (e_\sigma)_\rho-v_\sigma(e_\sigma)_\phi
   =\Delta v_\sigma(\bar\Theta_\sigma)_\phi,
 \qquad e_\sigma(\rho_e,\phi)=0.
 \tag{N.6}
$$
A comparison that simply evaluates the old auxiliary trial in the new
physical background without (N.6) would leave a first-order principal
error. That shortcut is not used here.

In (N.7)--(N.20), $\|f\|_\sigma$ denotes the holomorphic
strip supremum $\sup_{|\operatorname{Im}\phi|\le\sigma}|f(\phi)|$,
uniform in the declared real parameter and radial arguments.
It is not the old-circle Wiener norm.
The characteristic composition estimates below directly control this
supremum.

For real $\delta$ on the negative side, the radial part of $v_\sigma$
is real on the real circle. Complex-angle width growth is controlled
by $|d_\phi|$.
On the positive side the additional imaginary radial speed has modulus
$|\eta\sqrt K|$.
For example, a sufficient trajectory gate for a starting width $\sigma_1$
inside a wider paid width $\sigma_0$ is
$$
 \sigma_1 e^{\int_I D_1\,|d\rho|}
   +\int_I c_{\rm im}(t)
             e^{\int_{[t,\rho]}D_1\,|d\rho|}\,|dt|
       <\sigma_0,
 \tag{N.7}
$$
where $D_1$ bounds the actual $d_\phi$ on that wider strip and
$c_{\rm im}=0$ on the negative side,
$c_{\rm im}=|\eta\sqrt K|_{\rm up}$ on the positive side.
The oriented solution is integrated away from the true entry seam;
absolute length is used in this sufficient bound.
Uniform complex-parameter coefficient bounds may supply the
majorants, but (N.7) is a real-parameter operator statement.

Along these actual characteristics, (N.6) gives
$$
 \|e_\sigma(\rho)\|_{\sigma_1}
 \le \int_{\rho_e}^{\rho}
    \|\Delta v_\sigma(t)\|_{\sigma_0}
    \|(\bar\Theta_\sigma)_\phi(t)\|_{\sigma_0}\,|dt|.
 \tag{N.8}
$$
There is no matrix reaction exponential in this scalar formula.
If a certified nonzero entry error is retained, its complete transported
supremum is added to the right side.

## 5. Complete mixed phase and leading jets

For angular derivatives use a positive declared Cauchy loss:
$\|\partial_\phi^qe_\sigma\|_{\sigma}
 \le q!(\sigma_1-\sigma)^{-q}\|e_\sigma\|_{\sigma_1}$.
The radial jets are obtained by the exact recursion
$$
 \partial_\rho^{p+1}\partial_\phi^q e_\sigma
 =
 \partial_\phi^q\sum_{a=0}^p {p\choose a}
 \left[
 (\partial_\rho^a v_\sigma)
       \partial_\rho^{p-a}\partial_\phi e_\sigma
 +(\partial_\rho^a\Delta v_\sigma)
       \partial_\rho^{p-a}\partial_\phi\bar\Theta_\sigma
 \right],\quad 0\le p\le2 .
 \tag{N.9}
$$
It requires velocities only through their second radial derivatives.
The original exact intrinsic jets and the cubic difference provide
these; the complete reference jets are evaluated from the saved
Taylor coefficients and their full tails.

Because the same $\rho$ is used for both folds,
$$
 \Delta X=\tfrac12(e_++e_-),\qquad
 \Delta A=
 {3(e_+-e_-)\over4i\epsilon(-\rho)^{3/2}}.
 \tag{N.10}
$$
The second identity uses the compatible branch in (N.5).
It is a strict-side identity, not a root division.
Differentiating its exact radial scalar factor supplies every required
mixed jet; the true lower distance $h$ pays all denominators.

For the leading scalar $G$,
$$
 {G\over\bar G}
 =\left({A\over\bar A}\right)^{1/6}
     \exp\!\left[
       2\int_{\rho_e}^{\rho}b(t)\langle\Delta S(t)\rangle\,dt
     \right].
 \tag{N.11}
$$
The common intrinsic $k$ and the common root normalization cancel in
this ratio. The complete ordinary mean in its exponent does not.

All power differences must use the same analytic branches and paid
gaps. A sufficient homotopy gate is
$\|\Delta A\|<\inf|\bar A|$ on the claimed domain.
Then the segment $\bar A+t\Delta A$, $0\le t\le1$, stays away from zero,
and the exact formula
$$
 \Delta(A^p)=p\,\Delta A\int_0^1
                  (\bar A+t\Delta A)^{p-1}\,dt
 \tag{N.12}
$$
is legitimate.
This also supplies derivative bounds after ordinary product
differentiation. The endpoint gap of each function alone is not used
as an unproved gap for the entire connecting segment.

Equations (N.9)--(N.12), $T=-\rho A^{2/3}$, and
$Q=\eta\sqrt{k}A^{-1/3}$ determine complete differences of the
leading amplitudes
$$
 a_0=G(x^2-Ty^2),\qquad b_0=-2i\epsilon Gxy
$$
through radial order three and all needed angular orders.
The principal factor is always
$\mu=Q^2(x^2+Ty^2)$.
The different signs in the leading amplitude and principal factor are
not identified.

## 6. Correlated leading forcing and its first radial derivative

Use the exact unnormalized differential expression of
[E.19--E.22](R133-supplement-ordered-old-radial-transport-and-strict-exterior-first-correction-derivatives.md):
$$
 \mathcal Lw=w_{\rho\rho}+2d\,w_{\rho\phi}
   +c_2w_{\phi\phi}+c_1w_\phi+T_0w_\rho+V_0w
           +i\epsilon(\vartheta Q)K_Tw,
$$
$$
 c_2=d^2+\eta^2K,\quad
 c_1=d_\rho+dd_\phi+T_0d,\quad
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix}.
 \tag{N.13}
$$
Let $\mathcal N_0=\mathcal Lw_0$ and
$\bar{\mathcal N}_0=\bar{\mathcal L}\bar w_0$.
The exact difference is
$$
 \Delta\mathcal N_0
   =\mathcal L(\Delta w_0)
       +(\mathcal L-\bar{\mathcal L})\bar w_0.
 \tag{N.14}
$$
Every coefficient difference in the second term is retained, including
the complete difference of $(\vartheta Q)K_T$.
Differentiating (N.14) once gives $\Delta(\mathcal N_0)_\rho$.
It uses precisely the third leading jets from (N.9)--(N.12) and the
same first derivatives of local coefficients as E.21.

Put $F=-\mu^{-1}\mathcal N_0$ and
$\bar F=-\bar\mu^{-1}\bar{\mathcal N}_0$. Then
$$
 \Delta F=-\mu^{-1}
       \{\Delta\mathcal N_0+\Delta\mu\,\bar F\},
$$
$$
 \Delta F_\rho
 =-\mu^{-1}\{
       (\Delta\mathcal N_0)_\rho
       +(\Delta\mu)_\rho\bar F+\Delta\mu\,\bar F_\rho\}
       -{\mu_\rho\over\mu}\Delta F .
 \tag{N.15}
$$
This preserves the correlations that are lost by separately bounding
the full actual and reference numerators.

Let
$$
 M_0=\begin{pmatrix}a_0&Tb_0\\b_0&a_0\end{pmatrix},
 \qquad P_s=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad f=P_sM_0^{-1}F=(f_a,f_b)^t.
$$
The complete normalized forcing difference is
$$
 \Delta f=P_s\left[
 M_0^{-1}\Delta F
 -M_0^{-1}(\Delta M_0)\bar M_0^{-1}\bar F
 \right].
 \tag{N.16}
$$
Its first radial derivative is the ordinary derivative of the displayed
ordered products, using
$(M_0^{-1})_\rho=-M_0^{-1}(M_0)_\rho M_0^{-1}$
and the analogous barred identity. No matrix factors are exchanged.

## 7. Root-value subtraction and a second scalar comparison

Keep the same complete root function $b_*(X)$ from the original
[exact root-value subtraction](R133-supplement-exact-root-value-subtraction-and-real-radial-first-Airy-amplitude-bounds.md).
Write $Z=M_0^{-1}w_1=(\mathcal A,\mathcal B)^t$,
$\widetilde{\mathcal B}=\mathcal B-b_*(X)$, and
$$
 g_a=f_a+2i\epsilon T b_*'(X),\qquad
 L_b={f_b-b_*(X)\over T}.
$$
The barred definitions use $\bar X,\bar T,\bar f$ and the same
root function $b_*$.
On the strict neighbor these are exact expressions. In particular
$$
 \Delta g_a=\Delta f_a+
  2i\epsilon\{\Delta T\,b_*'(X)
       +\bar T[b_*'(X)-b_*'(\bar X)]\},
$$
$$
 \Delta L_b=
 {\,\Delta f_b-[b_*(X)-b_*(\bar X)]-\Delta T\,\bar L_b\over T}.
 \tag{N.17}
$$
These retain the nonzero root value and its full nonmean part.
Composition differences use the actual $X$ and $\bar X$ images inside
the paid root-function strip, with their connecting segments or an
equivalent certified analytic path.

Set
$$
 V_\sigma=\mathcal A+\sigma\tau\widetilde{\mathcal B},
 \qquad C_\sigma=Q(x-\sigma i\epsilon\tau y),
 \qquad H_\sigma=-\tfrac12 C_\sigma(g_a+\sigma\tau L_b).
$$
The exact scalar equation is
$$
 (V_\sigma)_\rho=v_\sigma(V_\sigma)_\phi+H_\sigma.
 \tag{N.18}
$$
It follows directly from E.3 after subtraction of $b_*(X)$.
The term $f_b-b_*(X)=TL_b$ removes the displayed
$T^{-1/2}$ forcing singularity without deleting the root function.
Its actual integration constant at the entry is the full, generally
nonzero value
$$
 V_\sigma(\rho_e)
 =\mathcal A(\rho_e)+\sigma\tau(\rho_e)
       \{\mathcal B(\rho_e)-b_*(X(\rho_e))\}.
$$
That value is common to the reference only by (N.1), not because it
vanishes.

Let $E_\sigma=V_\sigma-\bar V_\sigma$.
The entry difference is zero under (N.1), and
$$
 (E_\sigma)_\rho-v_\sigma(E_\sigma)_\phi
  =\Delta v_\sigma(\bar V_\sigma)_\phi+\Delta H_\sigma,
$$
$$
 \Delta H_\sigma=-\tfrac12\left[
 \Delta C_\sigma(\bar g_a+\sigma\bar\tau\bar L_b)
 +C_\sigma\{\Delta g_a+\sigma\Delta\tau\,\bar L_b
                              +\sigma\tau\,\Delta L_b\}
 \right].
 \tag{N.19}
$$
Thus a second actual-ray integration gives
$$
 \|E_\sigma(\rho)\|_{\sigma_1}
 \le\|E_\sigma(\rho_e)\|_{\sigma_0}
 +\int_{\rho_e}^{\rho}
   \left(
    \|\Delta v_\sigma\|\,\|(\bar V_\sigma)_\phi\|
                  +\|\Delta H_\sigma\|
   \right)|dt|
 \tag{N.20}
$$
on a domain satisfying the same trajectory gate.
The explicit initial term is zero only when its exact common-trace
identity has been verified.
There is no additional $1/T$ reaction exponential in this equation.

The normalized amplitude differences are reconstructed exactly by
$$
 \Delta\mathcal A=\tfrac12(E_++E_-),
$$
$$
 \Delta\widetilde{\mathcal B}
  ={E_+-E_-\over2\tau}
     -{\Delta\tau\over\tau}\,\bar{\widetilde{\mathcal B}},
 \qquad
 \Delta\mathcal B=
   \Delta\widetilde{\mathcal B}
       +b_*(X)-b_*(\bar X).
 \tag{N.21}
$$
The denominator is paid by the strict $|T|$ gap.
Both signed branches are retained.

## 8. Ordered radial jets and the complete first-correction source

Use the exact matrices $C,M,N$ of E.5, with no change of sign or
ordering. Put $\Delta Z=Z-\bar Z$.
Their difference equation is
$$
 \begin{split}
 (\Delta Z)_\rho={}&
 C(\Delta Z)_\phi+M\Delta Z-N\Delta f\\
 &+\Delta C\,\bar Z_\phi+\Delta M\,\bar Z-\Delta N\,\bar f .
 \end{split}
 \tag{N.22}
$$
Angular differentiation gives the complete mixed derivative.
Radial differentiation gives
$$
 \begin{split}
 (\Delta Z)_{\rho\rho}={}&
 C_\rho(\Delta Z)_\phi+C(\Delta Z)_{\rho\phi}
 +M_\rho\Delta Z+M(\Delta Z)_\rho
 -N_\rho\Delta f-N(\Delta f)_\rho\\
 &+(\Delta C)_\rho\bar Z_\phi+\Delta C\,\bar Z_{\rho\phi}
 +(\Delta M)_\rho\bar Z+\Delta M\,\bar Z_\rho
 -(\Delta N)_\rho\bar f-\Delta N\,\bar f_\rho .
 \end{split}
 \tag{N.23}
$$
Only the first forcing derivative is needed.
The matrix products keep their exact input/output order.

Reconstruction and its ordinary derivatives use
$$
 \Delta w_1=M_0\Delta Z+(\Delta M_0)\bar Z .
 \tag{N.24}
$$
For any required $(p,q)$, the complete mixed derivative is the
two-variable Leibniz sum with coefficients
$\binom{p}{a}\binom{q}{b}$.
This gives the needed $p\le2$ and angular derivatives, with any further
angular derivatives paid by an explicit positive Cauchy loss.

The local unnormalized first-correction numerator obeys the exact
identity
$$
 \boxed{\quad
 \mathcal N_1=\mathcal Lw_1
   =\bar{\mathcal N}_1+
        \mathcal L(\Delta w_1)
        +(\mathcal L-\bar{\mathcal L})\bar w_1 .
 \quad}
 \tag{N.25}
$$
The reference $\bar{\mathcal N}_1$ is the same complete signed
degree-ten numerator with its full Taylor and Fourier tails.
It may be evaluated at a new radius inside its certified auxiliary
domain, but no unsaved higher coefficient is assigned zero.
The two difference terms use the actual physical coefficients and
(N.22)--(N.24). Formula (N.25) does not subtract two norm upper bounds.

For the old-circle nonlocal terms and independent mean, first form
complete bounds for the actual $w_1,w_{1,\rho}$ from
$\bar w_1+\Delta w_1$ on the same actual old-angle strip.
Then apply the already paid actual coefficient words, projections,
$J$, and mean functionals for the physical neighboring row.
All nine nonlocal words and all five independent-mean terms remain.
A previously paid bound can be minimized only against another bound
for that same complete operator on that same domain and norm.

Before a strip-supremum estimate is inserted into any Wiener
coefficient word, a positive additional loss must be paid.
For the original fourfold modes $e^{4ij\phi}$ and
$\sigma'<\sigma$,
$
 \|f\|_{\mathcal A_{\sigma'}}
 \le {1+e^{-4(\sigma-\sigma')}\over
                1-e^{-4(\sigma-\sigma')}}\,\|f\|_\sigma .
$
For an angular derivative of order $q$, one can instead use the
complete factor
$\sum_{j\in\mathbb Z}(4|j|)^q
 e^{-4|j|(\sigma-\sigma')}$, with the mean interpreted as one for
$q=0$ and zero for $q>0$.
Both signed tails and the mean are included.
A direct previously paid Wiener estimate may be used on its own
declared domain, but no same-strip supremum/Wiener identification is
permitted.

The Airy output factors use the actual physical fold in this step.
The auxiliary phase is never substituted for the actual phase in an
all-frequency output bound.

## 9. What an actual consumer must preserve

The new calculation is limited to the two declared neighboring pieces.
It reuses the original signed Taylor coefficients, the complete
correlated-numerator coefficients, the original physical cubic shards,
intrinsic jets, actual fold-domain records, matrix-word rows and all
unmodified exterior source rows.

New operations are separately counted: finite background differences,
reference coefficient norms not already saved, full Taylor-tail
evaluations at the new radii, the two scalar difference-transport
integrals, ordered derivative-difference budgets, and the resulting
complete source integrals.
Every completed new natural stage is saved before the next one.
A failed trajectory, homotopy, denominator or remainder gate retains
its exact input and successful prefix.

The actual physical seams remain the same interfaces. Although the two
known amplitudes in the comparison agree in value at the entry, their
one-sided derivatives need not agree. The existing reconstructed
physical jump contracts are retained, including both ordinary source
rows and the independent mean.
This argument does not turn those old recorded jumps into a complete
corrected-trial seam operator for free.

Outside the two refined neighboring pieces, the original complete
source payloads are copied byte-for-byte.
Reassembling a radial integral uses interval covers and existing
positive-cut conventions; it does not subtract an old integral upper
bound from another upper bound.

The new consumer must report any improvement or lack of improvement
from actual public numerical gates. It does not infer a small
strong-return constant merely from zero entry differences, finite
background degree, or a small physical mesh width.
