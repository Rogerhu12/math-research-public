# R144 DH: the full physical outer curvature residual Hessian

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved on the actual QN exterior domain; all16 saved-rational comparisons pass.** The complete physical
curvature residual at \(R=25/8\), including its two mean equations,
has a uniform mixed second derivative with only one angular derivative
on one direction. The independent nonmean exterior height input is
included in its original \(\dot H^2\) units. The quantitative bound is

\[
 \|D^2\mathcal R_\partial(Q,g)[x,y]\|_{\mathcal O}
 \le10000\{\mathcal H(x)\mathcal E(y)+
                    \mathcal H(y)\mathcal E(x)\}.              \tag{DH.1}
\]

The norms and actual input class are specified below. This pays the
curvature DN part left open by
[UH](R144-supplement-uniform-real-physical-boundary-Hessian-near-compact-centres.md).
It does not assert an unrestricted rough-background nonlinear graph,
or discharge the separate world-height, phase, finite inverse and
iteration equations.

## DH1. One actual graph, physical angle and independent inputs

Keep precisely the selected metric, intrinsic entrance, frozen tail
parameters and admissible reflection class used by
[QN.4--QN.31](R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md).
At the actual outer endpoint impose the independent full-tail condition

\[
 Q=Q_*+q,\qquad \|q\|_{A^3,\oplus_1}\le10^{-9}.                \tag{DH.2}
\]

It is the smaller exterior condition, not merely the \(10^{-6}\) body
condition. The unknown \(q\) uses the ordinary real Wiener norm and
need not extend to any positive spatial strip. Let

\[
 (B_Q,C_Q)=\Psi(Q),\quad
 Z_Q=P_{\ne0,\theta}(C_Q-C_{\rm ref}),\quad
 g=|D_\theta|^2 f_B,\quad
 \|g\|_{A^0_\sigma}\le2^{-60},\quad \sigma\ge1/16.             \tag{DH.3}
\]

The physical angle is the original normalized angle
\(\Theta=\mathrm{id}+I(v/\langle v\rangle-1)\).
The mean in its defining primitive is not replaced by a point value.
The variable \(g\) is nonmean and is measured in the original normalized
height units. If an external convention uses an unnormalized physical
height, its original scale \(s_B\) must be applied before (DH.3).
It is not an additional factor that can be omitted.

In the fixed physical \(\theta\) coordinates define the same actual
long-graph map as QN,

\[
 \Gamma(Z,g)=\bigl(d(Z,|D_\theta|^{-2}g),
                          c_0(Z,|D_\theta|^{-2}g)\bigr).
                                                               \tag{DH.4}
\]

Its output norm is \(L^2_{\ne0,\theta}\oplus_1\mathbb R\).
The true equations from
[L.9](R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md)
give the complete curvature residual

\[
 \mathcal R_\partial(Q,g)=
 \begin{pmatrix}
 J_\theta B_Q+Q_\theta Z_Q-d(Z_Q,|D_\theta|^{-2}g)\\
 \langle C_Q\rangle_\theta-C_{\rm ref}
                         -c_0(Z_Q,|D_\theta|^{-2}g)\\
 \langle B_Q\rangle_\theta
 \end{pmatrix},\quad
 \mathcal O=L^2_{\ne0,\theta}\oplus_1\mathbb R\oplus_1\mathbb R .
                                                               \tag{DH.5}
\]

All three rows are retained. In a parity class the last row can vanish
by the exact symmetry, but it has not been dropped from the operator.
Independent prescribed affine right sides do not change this Hessian.
The actual \(J_\theta\) has symbol \(i\operatorname{sgn}(m)\), and the
true \(Q_\theta\) has the original symbol \(q_m(R)\).
[P.1](R133-supplement-actual-regular-R25over8-vector-and-long-ports.md)
proves \(0<q_m(R)<1\) for every nonzero mode. Neither a leading
multiplier nor a truncated finite vector replaces it.

No varying moving-angle normalizer multiplies a nonzero residual in
(DH.5). The distinct affine Robin/height ports retain their original
units; the independent constant height, holonomy and global phase
equations are not inferred from the curvature rows.

For a direction \(x=(h,p)\), where
\(p=|D_\theta|^2\dot f_B\) and the moving pair \(h\) is held fixed in
\(\phi\), set

\[
 \begin{split}
 E(h)&=\|h_1\|_{L^2_\phi}+\|h_2\|_{L^2_\phi},\\
 H(h)&=\|h_1\|_{H^1_\phi}+\|h_2\|_{H^1_\phi},\\
 \mathcal E(h,p)&=E(h)+4\|p\|_{L^2_\theta},\\
 \mathcal H(h,p)&=H(h)+200\|p\|_{H^1_\theta}.
 \end{split}                                                   \tag{DH.6}
\]

Thus \(\mathcal E\le\mathcal H\). In particular the high height
direction is the actual \(\dot H^3\) height norm, and its low norm
is the actual \(\dot H^2\) norm. The directional estimate is first
proved on smooth directions in the stated class and then extended
with these norms. It does not claim that arbitrary large directions
may be used as nonlinear backgrounds.

## DH2. Function-parameter Cauchy bounds in the genuine L2 module

QN5 proved the zero-width value graph and its complete square-zero
\(L^2\) module, retaining the real holonomy small root, both means,
the finite long length and the two endpoint lifts. Consequently
the \(L^2\)-operator-valued derivatives of \(\Gamma\) are holomorphic
in the background function parameters on

\[
 \|Z\|_{A^0}<\bar z=10^{-10},\qquad
                 \|g\|_{A^0}<\bar b=10^{-11}.                 \tag{DH.7}
\]

This is the already proved function-parameter holomorphy; there is no
complex spatial evaluation of the unknown \(q\).
For completeness take the original positive expressions QN.29 at
these wide radii:

\[
 \begin{gathered}
 \epsilon=2^{-512},\quad
 F=10(\bar z+\bar b)+\bar b,\quad
 \kappa=36(4096)F,\\
 J_f=9/(1-\kappa),\qquad J_B=(\epsilon+\kappa)/(1-\kappa),\\
 T=\epsilon+4(16384)FJ_f,\quad C=(T-\epsilon)/8,\\
 U=\epsilon+4(16384)F(1+J_B),\quad V=(U-\epsilon)/8 .
 \end{gathered}                                                 \tag{DH.8}
\]

New exact rational combinations of these completed formulas give

\[
 \|D_Z\Gamma\|_{L^2\to L^2\oplus_1\mathbb R}
             \le T+C<10^{-3}=:M_Z,\qquad
 \|D_g\Gamma\|_{L^2\to L^2\oplus_1\mathbb R}
             \le U+V<10^{-4}=:M_B .                           \tag{DH.9}
\]

The strictly positive finite-length fee \(\epsilon\) remains in both
expressions. At every actual background QN.25 gives
\(\|Z_Q\|_{A^0}<4\,10^{-11}\). Legitimate remaining radii are

\[
 r_Z=5\,10^{-11},\qquad r_B=9\,10^{-12}.                       \tag{DH.10}
\]

Indeed \(4\,10^{-11}+r_Z<\bar z\) and \(2^{-60}+r_B<\bar b\).
For a background direction \(X=(\zeta,p)\), write

\[
 L(X)=\|\zeta\|_{A^0}/r_Z+\|p\|_{A^0}/r_B .
                                                               \tag{DH.11}
\]

If \(L(X)>0\), the complex one-variable disc of radius
\(1/L(X)\) in the direction \(X\) stays inside (DH.7).
Cauchy's estimate for each operator in (DH.9), followed by the triangle
inequality, yields for \(Y=(\eta,t)\)

\[
 \|D^2\Gamma[X,Y]\|
 \le L(X)\{M_Z\|\eta\|_2+M_B\|t\|_2\}.                        \tag{DH.12}
\]

The case \(L(X)=0\) follows by linearity. There is no additional
factor from a two-variable polydisc. Smooth directions are in both
the parameter algebra and the Hilbert module, so symmetry of the
actual second derivative allows the average of (DH.12) and the same
whole bound with \(X,Y\) interchanged. Density gives the stated
mixed extension. This argument bounds a second derivative at the
admitted background; it does not extend the nonlinear value graph
to an unrestricted \(L^2\) input ball.

## DH3. The real physical chart pays both direction types

QN.23 gives the exact mean-aware variation

\[
 (DC_Q[h])\circ\Theta
 =-\frac{h_2}{v^2}
      +\frac{v_\phi}{v^3}I(h_2-j\langle h_2\rangle).
                                                               \tag{DH.13}
\]

The real composition and inverse in QN.22 have norm below
\(c=1.000001\) on \(H^2\). On \(L^2\), direct change of variables
gives their bounds \(\sqrt{j_u}\) or \(1/\sqrt{j_l}\), which are
also below \(c\) on that domain. Thus the same \(A^2\) multiplier
and primitive expression proves at both orders \(s=0,2\)

\[
 \|DC_Q[h]\|_{H^s_\theta}
 \le c\left\{5.84^{-2}
       +\frac{V_1\,5.84^{-3}}4(2+W_a/m_l)\right\}
                 \|h_2\|_{H^s_\phi}
 <.03\|h_2\|_{H^s_\phi},                                    \tag{DH.14}
\]

where, exactly as in QN.19,
\(V_1=3336(9.603792\,10^{-9})+10^{-9}\),
\(W_a=145(9.603792\,10^{-9})+10^{-9}\), and
\(m_l=5.84461145233-10^{-9}\).
This supplies the \(L^2\) endpoint directly, not by inferring it
from an \(H^2\)-operator bound. Interpolation gives the same
constant at \(s=1\).

On the normalized fourfold circle,

\[
 \|f\|_{A^0}\le\frac{11}{10}\|f\|_{H^1}.                     \tag{DH.15}
\]

For example the squared Cauchy--Schwarz sum is bounded by
\[
 \sum_{j\in\mathbb Z}(1+16j^2)^{-1}
 <1+\frac18\left(\sum_{j=1}^{5}j^{-2}+\frac15\right)
 <(11/10)^2 .
\]
The tail uses the decreasing-function integral after \(5\).
All means are included in this inequality. The nonmean projection
is contractive in all three spaces used here.

Therefore \(Z'_Q[h]=P_{\ne0}DC_Q[h]\) satisfies

\[
 \|Z'_Q[h]\|_2<.03E(h),\qquad
               \|Z'_Q[h]\|_{A^0}<.033H(h).                  \tag{DH.16}
\]

For \(X=(Z'_Q[h],p)\), \(Y=(Z'_Q[k],t)\), (DH.11) gives

\[
 L(X)\le660000000\,\mathcal H(h,p),\qquad
 M_Z\|Z'_Q[k]\|_2+M_B\|t\|_2
                     \le\frac3{100000}\mathcal E(k,t).
                                                               \tag{DH.17}
\]

Here \( (11/10)/r_B <660000000(200)\);
the two height weights in (DH.6) explicitly pay the different
source units. Applying the symmetric average of (DH.12) proves

\[
 \|D^2\Gamma[X,Y]\|
 \le9900\{\mathcal H(x)\mathcal E(y)+
                         \mathcal H(y)\mathcal E(x)\}.        \tag{DH.18}
\]

## DH4. Complete chain rule and both curvature means

The chain rule also contains
\(D_Z\Gamma\,D^2Z_Q[h,k]\). It cannot be omitted.
UH.1, valid on the larger \(A^3\) ball, gives

\[
 \|D^2Z_Q[h,k]\|_2
 \le2\{H(h)E(k)+H(k)E(h)\}.                                 \tag{DH.19}
\]

At the actual smaller background, the two complete QN.31 first
derivatives have sum at most
\(.0012+.00015=.00135\). Hence this chain-rule term costs
at most \(.0027\{H(h)E(k)+H(k)E(h)\}\).
Its scalar mean output is included.

The linear map of the physical pair in (DH.5) has norm at most
two from \(L^2_\theta\oplus_1L^2_\theta\) to \(\mathcal O\):
both \(J_\theta\) and \(Q_\theta\) have norm at most one, and
the nonmean and constant observations of each scalar cost at
most twice its full \(L^2\) norm. Applied to UH.1, this part
costs at most \(4\{H(h)E(k)+H(k)E(h)\}\).
In particular the actual mean identities
\(\langle C_Q\rangle_\theta=1/\langle v\rangle_\phi\) and
\(\langle B_Q\rangle_\theta=\langle u\rangle_\phi/
\langle v\rangle_\phi\) have both been differentiated.
The means are not frozen to their centre values.

Combining (DH.18)--(DH.19), and using
\(9900+4+.0027<10000\), proves (DH.1). The estimate is for
the actual nonlinear DN residual evaluated at the compact
background. It does not assume that the background already
satisfies its curvature or mean equations.

## DH5. Actual quadratic and difference estimates

Let the entire real segment from \((Q,g)\) to \((Q,g)+x\)
stay in the admitted domain (DH.2)--(DH.3), and put

\[
 \mathcal N(x)=\mathcal R_\partial((Q,g)+x)
               -\mathcal R_\partial(Q,g)-D\mathcal R_\partial(Q,g)x .
\]
The integral Taylor identity and (DH.1) give

\[
 \|\mathcal N(x)\|_{\mathcal O}
                         \le10000\,\mathcal H(x)\mathcal E(x).
                                                               \tag{DH.20}
\]

If the two increments \(x,y\) and the needed connecting segments
stay in that same domain, and
\(\mathcal H(x),\mathcal H(y)\le\rho_1\), then

\[
 \|\mathcal N(x)-\mathcal N(y)\|_{\mathcal O}
                       \le20000\rho_1\,\mathcal H(x-y).       \tag{DH.21}
\]

Indeed \(D\mathcal N(w)=D\mathcal R_\partial(Q+w)-
D\mathcal R_\partial(Q)\), whose integral Hessian bound is
at most \(20000\rho_1\) in the \(\mathcal H\)-operator norm.
These estimates are not extended to paths leaving the independent
small height domain.

For the particularly useful fixed-height path based at \(Q_*(R)\),
an arbitrary full-tail correction with component-sum
\(\|h\|_{A^3}\le10^{-9}\) has \(H(h),E(h)\le10^{-9}\).
Consequently its full physical curvature remainder, including
the two means, is at most \(10^{-14}\).
The linear part and original nonzero residual still have to be solved.

The companion saved-bound reader uses only exact rational combinations
of QN/UH and their displayed original sources. It calls no scientific
producer, does not restore any trial, and does not repeat old
integrals or first-derivative certifications.
Higher Sobolev DN estimates, the separate phase and world-height
Hessians, the finite/parameter Schur inverse and a convergent
augmented iteration remain separate obligations.
