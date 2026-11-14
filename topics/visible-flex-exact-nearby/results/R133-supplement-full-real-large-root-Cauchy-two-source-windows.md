# R133 supplement: full real root Cauchy energies on the certified piecewise radius

2026-11-14, visible-exact-astra-0df9 / root.

**Analytic conclusion with explicit new numerical gates.** The regular
Fourier energy used on the original root germ extends to the full real
radius $R=1/50$ when the saved root ratio $k=-K/\rho$ is at least one,
the actual full-family angular speed is at most $13/10$, and the
explicit nonmonotone weight fee below is finite. The original attempted
gate $K_r>1$ on the whole window failed in public run43621351216;
that failure is retained. This theorem pays the actual negative
weight derivative instead of discarding it. The companion consumer
integrates the complete two-row growth on the original common
refinement. No numerical pass is asserted by this proof.

The result concerns the same explicit repaired family, all angular
frequencies, the independent physical even mean, ordinary sources and
actual affine jumps. It is a Cauchy estimate, not a full boundary
inverse, a numerical strong-return bound or a nonlinear PDE branch.

## 1. The complete equation and the actual real domain

Use the unprojected equation (N.3) in
[complete moving scalarization](R133-supplement-complete-moving-root-scalarization.md).
The original circle has physical Fourier frequencies $4j$, normalized
measure, $\partial=\partial_\phi$, $\Pi f=\langle f\rangle$ and
$I=\partial^{-1}(1-\Pi)$. The state is $h=(h_1,h_2)$; its even second
row retains its independent mean.

The real family is $Q_\delta=Q_0+\delta Z$,
$\nu_\delta=\nu_0+\delta$, at physical $\eta_0$,
$|\delta|\le10^{-8}$. The notation $\eta=-\gamma\langle v\rangle$
below means the angular speed. The entire root radius-$1/50$ window
lies to the right of $9/50$, where the intrinsic compact bump is
exactly zero. Thus the saved original intrinsic jets apply to this
same family. This fact does not remove the intrinsic parameter
variation elsewhere.

Let $r_*\in[r_-,r_+]$ be the true simple root certified in the original
native. Set $\rho=r_*-r$ and $q^2=-K$. The numerical hypotheses on
the actual real cover $[r_--R,r_+]$ are
$$
 K(r_*)=0,\qquad q^2=\rho k,\quad k\ge1,\qquad
 |\eta|\le a_*:=13/10.
 \tag{E.1}
$$
Then for $0\le\rho\le R$, $q^2(0)=0$,
$(q^2)_\rho=K_r$ and $q^2\ge\rho$. The derivative $K_r$
is allowed to have either sign away from the root.
Both root endpoints are retained; a fixed cut at $r_--h$ is not
identified with $\rho=h$. The use of the larger fixed interval only
enlarges nonnegative integrals by a certified amount.

The background still has full degree96, and its quadratic
coefficients have degree192, hence physical lags at most768.
The unknown state and every source have no Fourier cutoff.

## 2. The same regular Fourier weight on the larger real interval

For every $j\in\mathbb Z$, including zero, define
$$
 \Lambda_j=\sqrt{1+16j^2},\quad x=\rho\Lambda_j^{2/3},\quad
 w_j^2=q^2+\Lambda_j^{-2/3}e^{-x},\quad
 \theta_j=e^{-a_*(1-e^{-x})},\qquad
 M=\operatorname{diag}(\theta/w,\theta).
 \tag{E.2}
$$
For $s=0,-1$, write $Z_s=\Lambda^sMh$.
The multipliers are positive and commute with radial scalar
coefficients, $\partial$, $I$ and $\Pi$. The two-row principal matrix
is conjugated explicitly in (E.5); it is not commuted through $M$.

Since $x+e^{-x}\ge1$ and (E.1) holds,
$$
 w\ge\Lambda^{-1/3},\quad w\ge q,\quad
 w\le W:=\sqrt{1+q_{\max}^2},\quad \theta^{-1}<4,\quad
 (w^2)_\rho=K_r-e^{-x}.
 \tag{E.3}
$$
On a common row $I_i=[l_i,u_i]$, let $k_i$ be its proved
root-ratio lower bound and $\kappa_i$ its original whole $K_r$
lower bound. Use the following nonnegative constant:
$$
 S_i=\begin{cases}
 0,&\kappa_i\ge1,\\
 \dfrac{1-\kappa_i}{2k_i(r_--u_i)},&
       \kappa_i<1\ \hbox{and}\ u_i<r_-.
 \end{cases}                                      \tag{E.3a}
$$
If neither case applies, this consumer must fail; it may not remove
that row. On the actual negative part of the row,
$\rho\ge r_--u_i$ in the second case, and
$$
 \max\{-w_\rho/w,0\}
 =\max\{(e^{-x}-K_r)/(2w^2),0\}\le S_i.
$$
Near the root the first case uses the actual positive $K_r$ gate;
the root ball is not replaced by a single decimal.
Here $e^{13/10}<4$. Also $2a_*/(3e)<1/3$.
The two logarithmic multiplier derivatives still satisfy
$$
 |\partial_{\log\Lambda}\log M_\nu|\le1/3,\qquad
 \partial_{\log\Lambda}\log(\Lambda^{-1}M_\nu)
                           \in[-4/3,-2/3].
 \tag{E.4}
$$
Indeed the negative derivative of $\log\theta$ is at most
$2a_*xe^{-x}/3$, whereas $-\partial_{\log\Lambda}\log w$
lies in $[0,1/3]$. These terms have opposite signs in $M_1$.
For the latter bound use
$(1+x)e^{-x}\le q^2\Lambda^{2/3}+e^{-x}$, a consequence of
$q^2\Lambda^{2/3}\ge x$. The former local requirement59 is therefore
unnecessary for this extension; the actual gate in (E.1) is sufficient.

The $\rho$ principal matrix becomes exactly
$$
 -\eta w\begin{pmatrix}0&1\\1&0\end{pmatrix}\partial
 +\begin{pmatrix}
 0&\eta\Lambda^{-2/3}e^{-x}w^{-1}\partial\\0&0
 \end{pmatrix}.
 \tag{E.5}
$$
The first term is skew-adjoint for real parameters.
The second has norm at most $a_*\Lambda^{2/3}e^{-x}$;
the equal negative scalar $\theta_\rho/\theta$ appears on both
diagonals. Their total real energy contribution is nonpositive.
The remaining first-row term $-w_\rho/w$ contributes at most $S_i$.
This bound applies to $Z_0$ and $Z_{-1}$ because all radial scalar
multipliers commute with $\Lambda^s$. No divergent frequency
supremum is integrated near the root.

The data and output maps are
$$
 \|Z_s(0)\|^2
 =\|h_1(0)\|_{H^{s+1/3}}^2+\|h_2(0)\|_{H^s}^2,\qquad
 \|h(\rho)\|_{H^s\times H^s}\le4W\|Z_s(\rho)\|.
 \tag{E.6}
$$
An ordinary source $g$ costs at most
$\|(g_1,g_2)\|_{H^{s+1/3}\times H^s}$, and hence at most the
isotropic $H^{s+1/3}\times H^{s+1/3}$ norm. This is not a
positive-side lower-source estimate.

## 3. Explicit local growth for both source windows

On a true common row let $Q\ge q^2$, $q_+=\sqrt Q$,
$W_+=\sqrt{1+Q}$, $b_+\ge|b|$, $\gamma_+\ge|\gamma|$.
Let $U_i,V_i$ bound the full ordinary angular Wiener derivatives
of $u,v$; the saved positive-width bounds also suffice.
Let $D_1,D_2$ be the saved full angular bounds for $d_\phi,d_{\phi\phi}$.
Define
$$
\begin{split}
 A_0&=b_+(1+3U_0^2+QV_0^2),&
 A_1&=b_+(6U_0U_1+2QV_0V_1),\\
 B_0&=b_+(1+U_0^2+3QV_0^2),&
 B_1&=b_+(2U_0U_1+6QV_0V_1),\\
 L_0&=2b_+U_0V_0,&
 L_1&=2b_+(U_1V_0+U_0V_1).
\end{split} \tag{E.7}
$$
These are complete coefficient norms, not signs of diagonal entries.
The primitive constants are
$$
 C_I=\sqrt{17}/4,\qquad
 \|I\|_{L^2\to H^{1/3}}=17^{1/6}/4<41/100.
 \tag{E.8}
$$

For $s=0$ a sufficient total growth is
$$
\begin{split}
 G_0={}&S_i+\tfrac{21}{2}D_1+10(A_0+B_0)
            +4(q_++W_+)L_0\\
 &+8b_+(W_+U_0+QV_0)
           \{(41/100)(U_1+U_2)+V_1/4\}\\
 &+4\gamma_+\{Q(V_1+V_2)+U_1\}.
\end{split} \tag{E.9}
$$
For $s=-1$ a sufficient total growth is
$$
\begin{split}
 G_{-1}={}&S_i+\tfrac12D_1+\tfrac{40}{3}(D_1+D_2)
       +10(A_0+A_1+B_0+B_1)\\
 &+4(q_++W_+)(L_0+L_1)\\
 &+8b_+C_I(U_1+V_1)
       \{W_+(U_0+U_1)+Q(V_0+V_1)\}\\
 &+4\gamma_+(QV_1+U_1).
\end{split} \tag{E.10}
$$

For completeness, (E.4) and physical lag at most768 give
$\|M_\nu aM_\nu^{-1}\|\le10\|a\|_{\mathcal A_0}$ and
$\|[M_\nu,d]M_\nu^{-1}\partial\|\le10D_1$.
For $s=-1$ the corresponding bounds are
$10(\|a\|_{\mathcal A_0}+\|a_\phi\|_{\mathcal A_0})$ and
$(40/3)(D_1+D_2)$, by the convex $4/3$ multiplier estimate
proved in [the negative-one theorem](R133-supplement-full-family-negative-one-root-Cauchy-and-seam-sources.md).
The ordinary transport energy adds $D_1/2$.

For the two off-diagonal local terms use $q^2/w\le q_+$,
$w\le W_+$ and $\theta^{-1}<4$ in the original order; for
$s=-1$ an angular multiplier costs its value plus first derivative.
The exact primitive term remains
$-2b(u_\phi,v_\phi)^T I(uh_1+Kvh_2)$.
Its complete two terms give the second line of (E.9), or the
third line of (E.10), with the exact interior $H^{-1}$ norm
before applying $I$ in the latter case.
Finally $\gamma\Pi h_2(Kv_\phi,-u_\phi)$ gives the final line.
The bound $|\Pi h_2|\le4\|Z_{s,2}\|$ holds for both values of $s$
because $\Lambda_0=1$. No mean or response to it has been set to zero.

These are the old complete growth arguments with local
$Q,W_+,b_+,\gamma_+$ and the additional nonnegative fee $S_i$.
They include no derivative of a radial interval bound. The values
$\kappa_i$ are original genuine whole derivatives; $k_i$ is a
root-ratio bound and is never mistaken for $K_r$.

## 4. Ordered propagation, ordinary sources and actual seam impulses

Let the true common rows be $I_i$, and set
$$
 {\cal I}_s=\sum_i |I_i|G_{s,i},\qquad
 {\cal C}_s=4\sqrt{1+\max_i Q_i}\,e^{{\cal I}_s}.
 \tag{E.11}
$$
All rows are intersected with the fixed enclosing negative interval
$[r_--R,r_+]$. The integral over any true root-to-point segment
is no larger. Let $j_a$ be any prescribed actual jumps at original
interfaces. Then
$$
 \boxed{\displaystyle
 \sup_{0\le\rho\le R}\|h(\rho)\|_{H^s\times H^s}
 \le {\cal C}_s\left[
  \|(h_1(0),h_2(0))\|_{H^{s+1/3}\times H^s}
  +\sqrt R\,\|g\|_{L^2_\rho(H^{s+1/3}\times H^{s+1/3})}
  +\sum_a\|j_a\|_{H^{s+1/3}\times H^s}\right],
 \quad s=0,-1 .} \tag{E.12}
$$
A zero-data case uses the non-strict form. The same ordered
subinterval argument handles impulses at every genuine seam.
The extra root-ball width only enters the growth integral in
(E.11), not an assertion that the root is a displayed decimal.

For $s=-1$, applying the original primitive afterwards costs exactly
$C_I$. Thus the complete bracket in (E.12) has the ordinary $L^2$
output bound $C_I{\cal C}_{-1}$ after $I$.
A finite trial corrected by opposite jumps uses these same sources.
Coefficient derivative jumps do not themselves imply state jumps
for this first-order equation; a reconstructed amplitude's actual
jump must still be computed and paid.

Fourier Galerkin projection commutes with the radial weights,
$\partial,I,\Pi$. The above full multiplier estimates are uniform
in truncation. Weak compactness on fixed Fourier coordinates,
lower semicontinuity and density therefore yield the full-frequency
energy solution; the zero-source estimate proves uniqueness.
This step does not require that a propagated input column retain
its initial frequency support.

## 5. Minimal actual numerical consumer and preserved scope

The consumer receives the original successful radius-$1/50$ native
$dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212$
and its actual child0 process. It also receives exactly the six
original parts listed in
[the shared intrinsic-jet manifest](../notes/2026-11-14-R133-original-root-window-intrinsic-third-jet-parts.json),
all from public run43583838026. SHA, original row identity, actual
closed intervals and full successful cover are checked before use.

The saved root-ratio lower bounds check $k_i\ge1$, the original
whole $K_r$ derivatives and exact row-to-root distances pay (E.3a),
and the saved full-family $\eta$ bounds check $13/10$.
The complete $U_0,U_1,U_2$,
$V_0,V_1,V_2,D_1,D_2$ come from the existing $1/64$ strip rows.
Only the common refinement, scalar arithmetic in (E.7)--(E.11)
and the six prescribed-radius totals are new. The same native
retains every common-row identity and each local growth budget.
An original candidate-piece index is never substituted for an
intrinsic common-row number. Successful new prefixes are reusable
only with identical source and input bytes.

All new numerical work runs in this public repository's Actions.
The root/candidate/response/scalar target, old angular coefficients
and old169-germ/4650-positive data are not recalculated.

A successful consumer authorizes (E.12) only on its explicitly
passed real radii. It does not grant the positive Green map a new
Sobolev source window, extend to complex parameter Hilbert energies,
remove the independent mean, evaluate the first Airy forcing,
pay numerical $C_E,C_s$ for the return, or establish a coupled
infinite BVP inverse.
