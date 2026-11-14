# R133 supplement: exact first-forcing seams and the two-row first-correction jump

2026-11-14, phase_inverse.

**Proved ordered jump identities.** At an original polynomial seam,
the jump of the first Airy forcing depends only on the first radial
derivative jumps of the continuously repaired background. The much
larger second and third coefficient derivative jumps do not enter this
particular identity. They remain necessary inputs at subsequent
transport orders and are not removed from the saved seam ledger.

The first corrected curvature state generally has a nonzero first-row
jump. Its exact value and a complete bound are given below. This is
an affine source to be paid with the genuine propagators, not an
ordinary volume residual.

## 1. Fixed conventions at an actual seam

Use the exact old-angle amplitudes, ordered operator and matrices in
[the explicit first-forcing theorem](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md).
Here $n=4|j|$, $\epsilon=\operatorname{sgn}j$,
$\rho=r_*-r$, $a=\eta\sqrt{k}$,
$D=\partial_r-d\partial_\phi$ and $U_n$ is the genuine Airy
two-profile map. Write
$$
 w_0=(a_0,b_0^{\rm Airy}),\qquad
 \mathcal T_\epsilon w_1=(F_b,F_a)=-\mathcal L_0w_0 .
 \tag{J.1}
$$
The local original coefficient $b_0=b(1-u^2-3Kv^2)$ is always
distinguished from $b_0^{\rm Airy}$.

A bracket denotes the right $r$ trace minus the left $r$ trace
at one original seam $r_s\ne r_*$. No change to the old angle
or to its projection $P=1-\Pi$ is made when taking that bracket.
The entire window lies outside the intrinsic compact support.
Thus $b,K,\gamma,s$ and all of their intrinsic derivatives are
smooth there; adjoining cached enclosures refer to those same
functions. The exact repairs make $u,v$ and every angular
derivative continuous. Their radial derivatives may jump.

The closed leading construction proves that $X,A,G,T,w_0$ and
their first radial derivatives are continuous on each strict
seam, as are all of their angular derivatives. The old inverse
$J=A_{\rm op}^{-1}$ and the coefficient operator $B$ are continuous
as bounded operators on their declared spaces. This uses the
operator $A_{\rm op}=\eta\partial_\phi+L$, distinct from the
scalar fold amplitude $A$.

## 2. All local coefficient jumps are first-derivative data

Put $\Delta u=[u_r]$, $\Delta v=[v_r]$, and retain the actual
independent mean $\Delta m=[m_r]=\Pi\Delta v$. Then
$$
\begin{split}
 \Delta\eta_r&=-\gamma\Delta m,&
 \Delta a_r&=-\gamma\sqrt{k}\,\Delta m,\\
 \Delta S_r&=2u\Delta u+2Kv\Delta v,&
 \Delta d_r&=-bI\Delta S_r,\\
 \Delta d_{r\phi}&=-bP\Delta S_r,&
 \Delta\ell_r&=-2b(v\Delta u+u\Delta v),\\
 \Delta(b_0)_r&=-2b(u\Delta u+3Kv\Delta v).
\end{split}
 \tag{J.2}
$$
All multipliers in these formulas take their common repaired
value at $r_s$. In particular no derivative of an interval
enclosure is requested. The actual full65 and full193 component
jumps, including $\Delta m$, were saved by the completed
piecewise native.

For example, if $J_s$ bounds the sum of the two complete angular
Wiener norms of $(\Delta u,\Delta v)$, then
$$
\begin{split}
 \|\Delta S_r\|&\le2(U_0+|K|V_0)J_s,\\
 \|\Delta d_r\|&\le |b|\|\Delta S_r\|/4,\qquad
 \|\Delta d_{r\phi}\|\le |b|\|\Delta S_r\|,\\
 \|\Delta\ell_r\|&\le2|b|(U_0+V_0)J_s,\\
 \|\Delta(b_0)_r\|&\le2|b|(U_0+3|K|V_0)J_s .
\end{split}
 \tag{J.3}
$$
The separate exact mean jump may give a sharper $\Delta\eta_r$
than $J_s$; it is not discarded.

## 3. Exact second-derivative jumps of the genuine fold

The two exact leading equations, in the $r$ direction, are
$$
 X_r=dX_\phi-\tfrac23a\rho^2A_\phi,\qquad
 A_r=dA_\phi+\tfrac{3}{2\rho}(A-aX_\phi).
 \tag{J.4}
$$
The apparent denominator in the second equation is harmless
at this strict seam, and the root itself is treated by its
original analytic germ. Differentiate once in $r$ and take
the jump. Every value and first-derivative term common to both
sides cancels, giving
$$
 \boxed{
 [A_{rr}]=\Delta d_r\,A_\phi
                -{3\Delta a_r\over2\rho}X_\phi,}
 \tag{J.5}
$$
$$
 [A_{\phi rr}]
 =\Delta d_{r\phi}A_\phi+\Delta d_rA_{\phi\phi}
               -{3\Delta a_r\over2\rho}X_{\phi\phi},
 \tag{J.6}
$$
$$
 [X_{\phi rr}]
 =\Delta d_{r\phi}X_\phi+\Delta d_rX_{\phi\phi}
             -\tfrac23\Delta a_r\rho^2A_{\phi\phi}.
 \tag{J.7}
$$
The signs use $d\rho/dr=-1$. The smooth radial function $a$
itself has no value jump; its derivative jump is the explicit
quantity in (J.2).

Since $T=-\rho A^{2/3}$,
$$
 [T_{rr}]=-\tfrac23\rho A^{-1/3}[A_{rr}],
 \tag{J.8}
$$
$$
 [T_{\phi rr}]
 =-\tfrac23\rho\left\{
 A^{-1/3}[A_{\phi rr}]
       -\tfrac13 A^{-4/3}A_\phi[A_{rr}]\right\}.
 \tag{J.9}
$$
The leading radial exponential obeys
$(\log E_G)_r=-2b\langle S\rangle$. Thus
$$
 [G_{rr}]
   =G\left\{{[A_{rr}]\over6A}
                    -2b\langle\Delta S_r\rangle\right\}.
 \tag{J.10}
$$
No second or third cubic derivative jump appears in
(J.5)--(J.10). This cancellation follows from the exact
first-order fold equations; it is not an estimate by an
independently fitted approximate fold.

Let $x=X_\phi$ and $y=T_\phi$. The second derivatives of the
two leading amplitudes consequently have the exact jumps
$$
 [a_{0,rr}]
 =[G_{rr}](x^2-Ty^2)
   +G\{2x[X_{\phi rr}]-[T_{rr}]y^2
                              -2Ty[T_{\phi rr}]\},
 \tag{J.11}
$$
$$
 [b_{0,rr}^{\rm Airy}]
 =-2i\epsilon\{[G_{rr}]xy
                +G([X_{\phi rr}]y+x[T_{\phi rr}])\}.
 \tag{J.12}
$$
All cross products of first derivatives have zero jump because
those derivatives are continuous.

## 4. The full first-forcing jump, with the one-gain term retained

The values of $\mu,H,H_D,T_0-\eta_r/\eta$ are continuous at
the seam. From (L.4),
$$
 [T_0]={\Delta\eta_r\over\eta},\qquad
 [V_0]={\Delta\eta_r\over\eta}\,b_0-\Delta(b_0)_r,\qquad
 [\vartheta]={\Delta\ell_r\over\eta}
                         -{\ell\Delta\eta_r\over\eta^2}.
 \tag{J.13}
$$
Also
$[D^2w_0]=[w_{0,rr}]-\Delta d_r\,\partial_\phi w_0$.
Therefore the exact complete degree-zero jump is
$$
\boxed{\begin{split}
 [\mathcal L_0w_0]=\mu^{-1}\bigg\{&
 [w_{0,rr}]-\Delta d_r\,\partial_\phi w_0
              -{\Delta\eta_r\over\eta}Dw_0\\
 &+\left({\Delta\eta_r\over\eta}b_0-\Delta(b_0)_r\right)w_0\\
 &-\left({\Delta\ell_r\over\eta}
          -{\ell\Delta\eta_r\over\eta^2}\right)
                        H^{-1}H_Dw_0\bigg\}.
\end{split}}
 \tag{J.14}
$$
The last row is the contribution of the true one-gain radial
operator. Its order and sign are not optional. The two components
of $-[\mathcal L_0w_0]$ are $([F_b],[F_a])$.

Equations (J.2)--(J.14), the actual fold gaps and the complete
leading derivative bounds give a direct directed norm recipe.
Every factor $1/\rho$ uses the genuine positive lower bound for
the absolute seam-to-root distance. No displayed decimal root
is substituted for the actual root interval.

The old projections and finite primitive/inverse remainders are
outside the degree-zero expression and retain their own exact
jump terms. This formula does not declare their complete operator
jump to be zero.

## 5. The first corrected curvature state has a real affine jump

The actual characteristic integral gives continuous $w_1$ at
each strict seam. Its first radial derivative need not be
continuous. In the exact convention of (M.16),
$$
 [a_{1,r}]
 ={aA^{-1/3}\over2}
        \{X_\phi[F_a]+i\epsilon T_\phi[F_b]\},
 \tag{J.15}
$$
$$
 [b_{1,r}]
 ={aA^{-1/3}\over2}
        \{i\epsilon T_\phi[F_a]+X_\phi[F_b]/T\}.
 \tag{J.16}
$$
The factor $T^{-1}$ is kept and paid at the actual strict seam.
For example, if $F_{J,s}$ bounds
$\|[F_a]\|+\|[F_b]\|$, then
$$
 \|[a_{1,r}]\|+\|[b_{1,r}]\|
 \le{a_+A_-^{-1/3}\over2}
 \left\{|X_\phi|+2|T_\phi|+
                      {|X_\phi|\over|T|}\right\}F_{J,s}.
 \tag{J.17}
$$
This is a complete, possibly conservative, sup bound on the
declared old angular strip. It is not a same-width Wiener
claim.

Construct the actual finite trial by
$$
 F^{[1]}_n=U_n(w_0+n^{-1}w_1),\qquad
 h_2=PF^{[1]}_n,\qquad h_1=J(D_0-B)PF^{[1]}_n .
 \tag{J.18}
$$
The second row is continuous and the exact first-row jump is
$$
 \boxed{
 j_2=0,\qquad
 j_1=n^{-1}JP\,U_n([a_{1,r}],[b_{1,r}]).}
 \tag{J.19}
$$
The leading trial alone contributes no state jump. All terms
in (J.18) other than the actual radial derivative have the same
two one-sided values. If the trial is projected to the actual
high block, its jump is $P_Hj$; $P_H$ is not commuted through
$J$. The finite complementary jump remains its own head row.

The correction solves the genuine moving system with the
opposite signed jump $-j$, in addition to every true ordinary
residual, mean equation and external port. Negative propagation
may consume the actual mixed
$H^{-2/3}\times H^{-1}$ jump norm, or the stronger
$H^{1/3}\times L^2$ norm when that is what has been proved.
Positive propagation uses its own declared weighted affine
jump input. Formula (J.19) alone does not grant a conversion
between those norms.

## 6. Quantitative consequence and remaining work

The saved original first derivative jump sums are small, and
(J.14) identifies exactly where that fact can be used. A
subsequent public consumer can evaluate (J.2)--(J.17) using the
completed radius-$1/50$ native and the new actual first-forcing
bounds, without re-evaluating any original target or polynomial
solve. It must still estimate the actual Airy map and full $J$
in (J.19), with the same frequency and source conventions.

The original second and third coefficient derivative jumps
remain untouched and may enter $\partial_r\mathcal L_0$,
$\mathcal L_1$, later amplitude derivatives and later
reconstructed state jumps. This theorem isolates one genuinely
smaller part of that work. It neither evaluates the final
strong return norm nor closes the coupled high and low inverse.
