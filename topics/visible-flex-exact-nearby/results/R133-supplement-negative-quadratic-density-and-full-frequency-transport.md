# R133 supplement: negative quadratic density and complete signed-frequency transport

2026-11-14, phase_inverse. **Proved, with 22 exact rational/polynomial
gates actually executed.** This concerns the same final moving M32
centre, manifest

    ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413

and exact parameters

\[
 \alpha=6890507429876859/9007199254740992,\qquad
 \nu=-2572625729470897/72057594037927936.                 \tag{Q.1}
\]

There are two conclusions. First, an exact change of the **complete**
moving Jacobi equation removes its common quadratic reaction in
favour of the actual mean residual. It preserves both wave branches,
the primitive, the mean column, ordinary sources and every PPoly
interface. Second, the remaining principal quadratic-density
transport, in a specified negative Sobolev norm, has an exact
all-sign Fourier Hermitian cancellation. For the complete high block
\(|j|\ge97\) on the current negative root germ its logarithmic norm
integral is less than \(1/4000\).

The second statement is a principal-block estimate. The cross-wave
operator, the actual mean residual, the nonlocal operator, all
head paths and the root traces are displayed below and are **not**
included in that small number. This is not yet a whole-return
inverse or a physical \(L^2\) reconstruction bound.

## 1. Complete moving equation at an unsolved centre

The circle has length \(\pi/2\); all averages and \(L^2\) norms use
normalized measure. Put \(I=\partial_\phi^{-1}P_{\ne0}\), with zero
constant multiplier, and

\[
 m=\langle v\rangle,\quad S=u^2+Kv^2,\quad
 d=-\beta I S,\quad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.             \tag{Q.2}
\]

The actual nonlinear moving right side is

\[
 F(Q)=
 \binom{d u_\phi+\gamma mK v_\phi-\beta u(1+S)}
       {d v_\phi-\gamma m u_\phi+\beta v(1-S)} .
\tag{Q.3}
\]

We differentiate this expression at the complete saved centre, without
assuming its residual vanishes. For an ordinary unnormalized moving
source \(f\), the exact variational equation is

\[
\begin{split}
 h_r={}&(d\,{\rm Id}+\gamma mJ)h_\phi+Lh\\
 &-2\beta Q_\phi I(u h_1+Kv h_2)
          +\gamma\langle h_2\rangle JQ_\phi+f,\\
 L={}&
 \begin{pmatrix}
 -\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
 -2\beta uv&\beta(1-u^2-3Kv^2)
 \end{pmatrix}.
\end{split}                                                       \tag{Q.4}
\]

In the reflection class \(h_1\) is odd and \(h_2\) is even. Its second
mean remains an unknown. A supplied parameter source is part of \(f\);
no fixed-\(Q\) parameter column is replaced by a normalized candidate
column. In particular the current compact metric has
\(\gamma_\nu=+\tfrac12w\gamma\). The separate residual-sensitive bridge
is still required if (Q.4) is to be identified with the original
physical-angle Jacobi operator at an approximate centre.

Let \(a_{\rm phys}\) be the actual intrinsic radius, so
\(a_{\rm phys}'/a_{\rm phys}=\beta\). Define the **actual** centre mean
residual by

\[
 R_0=m'-\beta m(1-\langle S\rangle).                    \tag{Q.5}
\]

Indeed, integration by parts using \(d_\phi=-\beta(S-\langle S\rangle)\)
gives \(\langle F_2(Q)\rangle=\beta m(1-\langle S\rangle)\).
Thus (Q.5) is exactly the second mean of \(Q_r-F(Q)\), including its
sign; it is not assumed small merely because the centre was obtained
numerically.

## 2. Two complete characteristic states

On any closed strict negative subinterval, set

\[
 q=\sqrt{-K}>0,\quad \eta=-\gamma m>0,\quad
 r_\sigma=u+\sigma qv,\quad
 T_\sigma h=\frac{h_1+\sigma qh_2}{\sqrt{2q}},
 \qquad \sigma\in\{+1,-1\}.                            \tag{Q.6}
\]

Write \(z_\sigma=T_\sigma h\) and \(c_\sigma=d+\sigma\eta q\).
Direct multiplication in (Q.4), including \(T_rT^{-1}\), gives

\[
 (z_\sigma)_r=c_\sigma(z_\sigma)_\phi
          -2\beta S z_\sigma+B_\sigma z_{-\sigma}
          +(\mathcal N z)_\sigma+T_\sigma f,           \tag{Q.7}
\]
where

\[
 B_\sigma=-\frac{q'}{2q}-\beta(1+r_\sigma^2),            \tag{Q.8}
\]
\[
 (\mathcal N z)_\sigma=
 -\beta(r_\sigma)_\phi I(r_-z_++r_+z_-)
 -\frac{\sigma\gamma}{2}(r_\sigma)_\phi
                      \langle z_+-z_-\rangle .        \tag{Q.9}
\]

Here and below the subscript \(r_\sigma\) denotes a wave coefficient,
not a radial derivative. Formula (Q.9) includes the original rank-one
mean column and the zero-mode convention of \(I\).

One way to check all factors is to use
\(E=\left(\begin{smallmatrix}1&q\\1&-q\end{smallmatrix}\right)\).
Then \(T=(2q)^{-1/2}E\) and
\(2qE^{-1}=\left(\begin{smallmatrix}q&q\\1&-1\end{smallmatrix}\right)\).
The four entries of \(EL(2qE^{-1})\) are respectively
\(-4q\beta S,-2q\beta(1+r_+^2),
 -2q\beta(1+r_-^2),-4q\beta S\).
The additional differentiated frame has zero diagonal and both
off-diagonal entries \(-q'/(2q)\). These polynomial identities are
among the executed exact gates.

Now put

\[
 n=\frac{a_{\rm phys}^2}{m^2}>0,\qquad w_\sigma=n z_\sigma .
\tag{Q.10}
\]
Since \(n'/n=2\beta\langle S\rangle-2R_0/m\), (Q.7) becomes

\[
 \boxed{
 (w_\sigma)_r=c_\sigma(w_\sigma)_\phi
       +2d_\phi w_\sigma-\frac{2R_0}{m}w_\sigma
       +B_\sigma w_{-\sigma}
       +(\mathcal Nw)_\sigma+nT_\sigma f .}
\tag{Q.11}
\]

Thus the common \(-2\beta S\) reaction is a quadratic-density
transport term plus the **true residual** \(-2R_0/m\). No
\(\exp\int2|\beta S|\) is intrinsically required for this diagonal.
The term \(q'/q\) is still present in (Q.8). Formula (Q.11) does not
authorize taking the singular \(q=0\) endpoint in this wave frame.

The inverse and its physical moving mean are

\[
 h_1=\frac{\sqrt{q/2}}n(w_++w_-),\qquad
 h_2=\frac{w_+-w_-}{n\sqrt{2q}},\qquad
 \langle h_2\rangle=
  \frac{\langle w_+\rangle-\langle w_-\rangle}{n\sqrt{2q}} .
\tag{Q.12}
\]

Every source has the exact transformed value \(f_w=nTf\).
In particular no angular differentiation or projection is silently
applied to the original ordinary source.

## 3. True labels, sources, means and interfaces

For either sign let \(H_\sigma\) be the true circle lift defined by

\[
 (H_\sigma)_r=-c_\sigma\circ H_\sigma,\qquad
 H_\sigma(r_0,\xi)=\xi,\qquad
 J_\sigma=\partial_\xi H_\sigma>0.                     \tag{Q.13}
\]

On a strict compact subinterval these real smooth flows exist and are
invertible by the scalar ODE and its Jacobian equation
\((J_\sigma)_r=-(d_\phi\circ H_\sigma)J_\sigma\).
Define

\[
 X_\sigma=J_\sigma^2\,w_\sigma\circ H_\sigma .           \tag{Q.14}
\]

The entire \(c_\sigma\partial_\phi+2d_\phi\) part cancels exactly
in the derivative of (Q.14). For \(S_\sigma=H_\sigma^{-1}\), set
\(F_\sigma=S_{-\sigma}\circ H_\sigma\). Its two exact derivatives are

\[
 (F_\sigma)_\xi=
 \frac{J_\sigma}{J_{-\sigma}\circ F_\sigma},\qquad
 (F_\sigma)_r=
 -\frac{2\sigma\eta q}{J_{-\sigma}\circ F_\sigma}.       \tag{Q.15}
\]

Consequently the cross term in the label equation is exactly

\[
 (B_\sigma\circ H_\sigma)(F_{\sigma,\xi})^2
                  X_{-\sigma}\circ F_\sigma,           \tag{Q.16}
\]
and the source is
\(J_\sigma^2(nT_\sigma f)\circ H_\sigma\).
The whole nonlocal expression (Q.9) is transformed by the same
quadratic-density rule; it has not disappeared.

For example the actual mean row becomes

\[
 \langle h_2\rangle=
 \frac{\langle J_+^{-1}X_+\rangle-
       \langle J_-^{-1}X_-\rangle}{n\sqrt{2q}} .         \tag{Q.17}
\]

In general the label mean cannot replace either weighted mean here.
Reflection gives \(X_+(-\xi)=-X_-(\xi)\), consistent with (Q.17);
it does not set the even physical mean to zero.
The exact \(L^2\) density norm formula is

\[
 \|J_\sigma^2 g\circ H_\sigma\|_2^2
 =\int J_\sigma(S_\sigma(\phi))^3|g(\phi)|^2\,d\phi .
\tag{Q.18}
\]

Thus a use of this label transform in a quantitative unweighted
\(L^2\) argument must pay the actual \(J^{3/2}\) and inverse factors.
None is declared to be one.

At a candidate PPoly interface let \(h^+=h^-+g\), including any
prescribed jump source. Intrinsic \(K,a_{\rm phys}\) are continuous.
The exact transmission is

\[
 w^+=\left(\frac{m^-}{m^+}\right)^2w^-
                     +n^+T(q)g .                     \tag{Q.19}
\]

The piecewise flow and \(J\) are continued continuously. Its label
version is obtained by multiplying (Q.19) by the same \(J^2\).
The scalar transmission factor is part of the full mean/residual
ledger; omitting it would falsely convert a piecewise polynomial
centre into a globally continuous one.

## 4. An ordered cross-wave integration identity

This section records an exact available normal-form step, without
granting its inverse. In (Q.16) let
\(a_\sigma=(B_\sigma\circ H_\sigma)F_{\sigma,\xi}^2\).
For fixed external test functions define

\[
 \mathcal L_\sigma=
 M_{a_\sigma/F_{\sigma,r}}\,C_{F_\sigma}I,\qquad
 \mathcal Z_\sigma=
 M_{\partial_r(a_\sigma/F_{\sigma,r})}\,C_{F_\sigma}I .
\tag{Q.20}
\]

The denominator is nonzero on every strict compact interval.
Using \(\partial_\xi I=P_{\ne0}\) gives the full identity

\[
 \mathcal K_\sigma
 =\partial_r\mathcal L_\sigma-\mathcal Z_\sigma
                              +M_{a_\sigma}P_0,\qquad
 \mathcal K_\sigma=M_{a_\sigma}C_{F_\sigma}.             \tag{Q.21}
\]

The last term is the exact label-mean column; it must remain.
For a full solution \(X'=\mathcal A X+F\), and a comparison
propagator \(\mathcal U_D(t,s)\) generated by \(\mathcal A_D\),
integration by parts on each smooth piece yields

\[
\begin{split}
 \int_a^t\mathcal U_D(t,s)\mathcal K(s)X(s)\,ds
={}&[\mathcal U_D(t,s)\mathcal L(s)X(s)]_a^t\\
 &+\int_a^t\mathcal U_D(t,s)
     [\mathcal A_D\mathcal L-\mathcal Z-\mathcal L\mathcal A]X\,ds\\
 &-\int_a^t\mathcal U_D(t,s)\mathcal L F\,ds
   +\int_a^t\mathcal U_D(t,s)M_aP_0X\,ds .
\end{split}                                                       \tag{Q.22}
\]

All products are ordered. In particular \(\mathcal L X'\), both
endpoints, the ordinary source and the mean column have been paid
algebraically, rather than dropped after differentiating a fixed
test function. At a join retain both one-sided endpoint terms and
(Q.19). Actual smallness of these complete operators, root finite
parts and a final return gap are further obligations.

There is no commuting of a physical Fourier projection through
\(C_F\) anywhere in (Q.20)--(Q.22).

## 5. The Fourier norm in which the principal growth cancels

Let \(D=-i\partial_\phi\) and \(\Lambda=(1+D^2)^{1/2}\), with
\(\Lambda_0=1\). On the full moving circle define

\[
                  Y_\sigma=\Lambda^{-3/2}w_\sigma .    \tag{Q.23}
\]

This is a precise change of Sobolev index:
\(\|Y\|_{H^s}=\|w\|_{H^{s-3/2}}\).
Its inverse is \(\Lambda^{3/2}\); it is not bounded from \(L^2\) to
ordinary curvature \(L^2\). The complete equation becomes

\[
\begin{split}
 Y_{\sigma,r}={}&
 \Lambda^{-3/2}(c_\sigma\partial_\phi+2d_\phi)
                         \Lambda^{3/2}Y_\sigma
 -\frac{2R_0}{m}Y_\sigma\\
 &+\Lambda^{-3/2}M_{B_\sigma}\Lambda^{3/2}Y_{-\sigma}
 +\Lambda^{-3/2}\mathcal N\Lambda^{3/2}Y
 +\Lambda^{-3/2}nTf .
\end{split}                                                       \tag{Q.24}
\]

All modes, including mean, occur here. If a head-preserving version
is preferred, use multiplier 1 for \(|k|<M_0\) and
\((\langle k\rangle/\langle M_0\rangle)^{-3/2}\) for
\(|k|\ge M_0\). Its high-to-high matrix ratios are identical to
(Q.23); its complete low-to-high and high-to-low matrices must be
kept. We do not identify (Q.23) with the previous positive
Riccati/Airy state \(M^{1/6}T_M^{-1}S_\sigma Rh_M\).

For real \(d\), the complete Fourier matrix of the nonradial principal
part in (Q.24), for physical frequencies \(k,n\in4\mathbb Z\), is

\[
 A_{kn}=i(2k-n)
       \left(\frac{\langle n\rangle}{\langle k\rangle}\right)^{3/2}
       \widehat d(k-n).                                  \tag{Q.25}
\]

The radial \(\sigma\eta q\partial_\phi\) is exactly skew-adjoint.
The Hermitian part of (Q.25) has entries

\[
 H_{kn}=\frac i2\widehat d(k-n)
 \left[(2k-n)R_{kn}-(2n-k)R_{kn}^{-1}\right],\qquad
 R_{kn}=\left(\frac{\langle n\rangle}{\langle k\rangle}\right)^{3/2}.
\tag{Q.26}
\]

This formula includes both Fourier signs. Reality of the coefficient
is used only to form the adjoint, not to erase a negative cone.

## 6. Complete all-sign bound, including arbitrary coefficient tails

Suppose \(|k|,|n|\ge M_0\ge1\). First take \(k=m\ge n>0\),
\(l=m-n\), and put \(f(x)=(1+x^2)^{3/2}=x^3+g(x)\).
For \(x\ge1\),

\[
 \frac32x\le g(x)\le2x,\qquad
 0\le g'(x)=\frac{3x}{\sqrt{x^2+1}+x}\le\frac32.          \tag{Q.27}
\]

The upper bound for \(g\) follows by integrating
\(g'\le3/2\) from 1 and \(g(1)<2\); the lower bound follows
from convexity of \((1+t)^{3/2}\).
The numerator in (Q.26), after multiplication by
\(\sqrt{f(m)f(n)}\), has the exact cubic identity

\[
 (2m-n)n^3-(2n-m)m^3=(m-n)^3(m+n).                     \tag{Q.28}
\]

If \(l\le n\), its additional \(g\) part is

\[
 G=3l\,g(n)-(n-l)(g(m)-g(n)),\qquad 0\le G\le6nl .
\]
Since \(\sqrt{f(m)f(n)}\ge m^{3/2}n^{3/2}\), the absolute
bracket in (Q.26) is at most

\[
                  \frac{2l^3+6l}{n^2}.                \tag{Q.29}
\]

For \(m/n=R\ge2\), the two terms in that bracket have the same
sign. Since \(R_{mn}\le1\) and \(R_{mn}^{-1}\le R^{3/2}\),

\[
 |{\rm bracket}|
 \le n[(2R-1)+(R-2)R^{3/2}]
 \le3n(R-1)^3=\frac{3l^3}{n^2}.                         \tag{Q.30}
\]

For clarity, \(2R-1\le3(R-1)\), and
\(R^{3/2}\le R^2\le3R(R-1)\). The resulting two
majorants add to exactly \(3(R-1)^3\).
Changing both signs or exchanging the frequencies preserves the
absolute bound.

For opposite signs, take \(|k|=m\ge|n|=n_0\), \(R=m/n_0\ge1\).
Now \(|k-n|=m+n_0\), and

\[
 |{\rm bracket}|
 \le n_0[(2R+1)+(R+2)R^{3/2}]
 \le\frac32n_0(R+1)^3
 =\frac{3|k-n|^3}{2n_0^2}.                             \tag{Q.31}
\]

Indeed \(R^{3/2}\le R^2\),
\((R+2)R^2\le(R+1)^3\), and
\(2R+1\le(R+1)^3/2\) for \(R\ge1\).
This proves the whole negative-cone and cross-cone bound, not only
a positive-frequency asymptotic.

Combining (Q.29)--(Q.31), and then using the complete convolution
Schur estimate on \(\ell^2\), gives

\[
 \left\|\operatorname{Herm}
 P_H\Lambda^{-3/2}(d\partial_\phi+2d_\phi)
                     \Lambda^{3/2}P_H\right\|
 \le\frac{\frac32\|d'''\|_{A^0}+3\|d'\|_{A^0}}{M_0^2}
 \le\frac{3\|d\|_{A^3}}{2M_0^2}.                       \tag{Q.32}
\]

The second inequality is the pointwise polynomial inequality
\(\tfrac32l^3+3l\le\tfrac32(1+l)^3\).
Thus (Q.32) also permits complete unknown coefficient tails in
\(A^3\). No exact finite bandwidth is assumed there.

If instead the whole coefficient satisfies
\(\widehat d(l)=0\) for \(|l|\ge M_0\), every high-to-high pair
with a nonzero matrix entry has the same sign and ratio less than 2.
Only (Q.29) is then needed, and the stronger bound is

\[
 \left\|\operatorname{Herm}P_H A P_H\right\|
 \le\frac{\|d'''\|_{A^0}+3\|d'\|_{A^0}}{M_0^2}.         \tag{Q.33}
\]

These are logarithmic norm estimates: the derivative of the
squared norm has twice the displayed constant. Consequently the
norm of a principal propagator is bounded by the exponential of
its integral, in either radial direction.

For smooth coefficients this follows first for finite Galerkin
solutions. The full generator differs by a bounded operator from
the skew-adjoint half-density transport
\(P_H(d\partial_\phi+d_\phi/2)P_H\). The matrix difference is bounded
by a complete convolution of
\(C|l|(1+|l|/M_0)^{3/2}|\widehat d(l)|\), which is summable
under \(A^3\). A real \(C^1\) circle flow supplies the underlying
half-density group; its finite-dimensional head compression only
adds bounded off-diagonal blocks. Bounded perturbation, or the
same Galerkin limit and its adjoint uniqueness, gives the actual
two-way principal evolution. This passage does not truncate the
high Fourier output.

## 7. Actual current root-germ budget

We consume the already proved complete complex germ, whose joint
rectangle contains

\[
 \operatorname{Re}r\in[r_*^--10^{-5},r_*^++10^{-5}],
 \quad |\operatorname{Im}r|\le10^{-5},
 \quad |\operatorname{Im}\phi|\le1/1024 .               \tag{Q.34}
\]

It is entirely within actual PPoly piece 2549 and the intrinsic
scalar germ. The numerical inputs are whole-parameter bounds
for (Q.1), not old amplitude-\(3/4\) coefficients. On its real
circle the published bounds imply

\[
 |\beta|<9/5,\quad |u|_\infty<8/5,\quad
 \|v\|_{A^0}<9/5,\quad |K'|<60.465470<61 .
\tag{Q.35}
\]

The first three follow from the full joint-domain gaps and
physical-to-moving angle bounds in the published germ and
positive-root proof; they do not depend on the sign of \(K\).
Only its positive-only assertion \(S\ge0\) is not reused.

Take
\(r_a=0.2383878742994\) and any closed strict subinterval of
\([r_a,r_*)\). Its total length is less than \(10^{-5}\) for every
\(r_*\in[0.2383968742994,0.2383968743003]\).
On this negative interval,

\[
 -61/100000<K\le0,\qquad
 -\frac{61}{100000}\frac{81}{25}\le S\le\frac{64}{25}.
\tag{Q.36}
\]

Its range length is exactly bounded above by
\(6404941/2500000<13/5\).
Since \(u,v\) have all their moving modes in \(|j|\le32\),
\(d_\phi=-\beta(S-S_0)\) has at most 128 nonzero complex coefficients
and physical support \(|l|\le256\). Parseval gives

\[
 \|d_\phi\|_{A^0}
 \le\sqrt{128}\,\frac95\,\frac{13}{5}<54,\qquad
 \|d'''\|_{A^0}\le256^2\cdot54 .                       \tag{Q.37}
\]

This argument pays the signed negative \(S\) range and every centre
mode; no angular sampling or unproved Fourier cutoff appears.

For \(P_H=P_{\{|j|\ge97\}}\), \(M_0=388>256\).
Using (Q.33),

\[
 E_{\rm tr}
 \le \frac{54(256^2+3)}{388^2}
 =\frac{1769553}{75272}
 <23.508781485811457115527687 .                         \tag{Q.38}
\]
Hence

\[
 \int E_{\rm tr}\,dr
 <\frac{1769553}{7527200000}<\frac1{4000},\qquad
 \|\mathcal U_{\rm principal,H}(r,t)\|
 <\frac{4000}{3999}.                                   \tag{Q.39}
\]

The elementary inequality \(e^x\le(1-x)^{-1}\), \(0\le x<1\),
was used in the last bound. It is uniform over all inner points
of the strict interval and both radial directions. It includes
both Fourier cones. It applies to the principal part of (Q.24)
in its explicitly stated norm, not to the full right side.

## 8. Exact remaining block and port obligations

In the current finite centre the coefficients of the complete
nonlocal and reaction operators have their proved finite support,
but their head-to-high effects cannot be discarded. Split
\(Y=Y_L+Y_H\) only after the complete equation (Q.24) is formed.
The equations retain all four blocks \(A_{LL},A_{LH},A_{HL},A_{HH}\),
the full source, and the two branches. A label pullback from
Section 3 does not commute with these projections.

The following are not part of (Q.39):

* the exact cross-wave \(B_\sigma\), including \(q'/q\);
* the whole primitive/mean operator (Q.9);
* \(-2R_0/m\) and the actual scalar interface factors (Q.19);
* all low/high feedback and the actual exterior mean functional;
* the conversion of (Q.23) to either physical ordinary traces or
  the positive two-row Airy/Riccati norm;
* the root finite part, the complete negative return phase,
  the actual regular graph and the original \(\nu\) scalar Schur.

The exact cancellation nevertheless changes the legitimate
budget: one should not reinsert the removed \(2|\beta S|\)
common diagonal into a subsequent estimate of this same state.
For a final ordinary Sobolev theorem, the smoothing gauge must
be inverted in the required stronger output space and all the
listed terms must be consumed there. Neither a negative-order
norm change nor a small principal Hermitian part proves a
same-\(L^2\) inverse by itself.

## 9. Executed arithmetic and reproduction

Source:

    scripts/fourfold_codazzi_negative_quadratic_density_transport.mjs

Actual rational report:

    notes/2026-11-14-R133-negative-quadratic-density-transport-rational.json

The report has 22 passed exact BigInt and multivariate polynomial
gates. The current environment executed the same pure arithmetic
core in V8. It did not rerun the previously completed native
joint-germ calculation and did not fabricate a new field table.
The report records the SHA256 and Git blob of each consumed
published input proof, the complete candidate identity, and the
scope exclusions above. The standalone Node source verifies those
same input hashes before reproducing the arithmetic and refuses
to overwrite an existing report.

From the topic directory:

    node scripts/fourfold_codazzi_negative_quadratic_density_transport.mjs \
      --out notes/a-new-negative-quadratic-density-report.json

The complete signed-frequency inequalities (Q.27)--(Q.33) and
the mean/source/interface identities are proved in this document;
the gates check their polynomial identities and the actual
outward rational budget. A finite arithmetic check is not used
as a substitute for their infinite-frequency proof.
