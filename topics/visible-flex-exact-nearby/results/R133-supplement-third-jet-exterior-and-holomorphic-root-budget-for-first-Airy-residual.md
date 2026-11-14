# R133 supplement: original third jets outside the root and an analytic inner budget for the first corrected Airy residual

2026-11-14, visible-exact / root.

**Proved identities and a complete derivative-budget contract.** This separates the actual first-amplitude residual into two overlapping regions. On strict real pieces the original intrinsic third jets suffice. On the one genuinely holomorphic root germ, explicit complex-domain margins pay the remaining derivatives. No fourth or fifth intrinsic target evaluation is required by this construction.

The estimates concern the same actual forced amplitude, with the same zero common root trace. They do not define two different trials or add a cutoff. No artificial interface source is created. The old polynomial seams and all of their actual sources remain.

All numerical domain choices and the resulting residual norm require a directed public consumer. This theorem does not claim that its finite constants are small.

## 1. The exact residual and the derivative issue

Use the original old-angle operator and first forcing from
[the complete first-forcing theorem](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md), (L.1)--(L.6):
$$
D=\partial_r-d\partial_\phi,\qquad
\mathcal L_0w=\mu^{-1}
 \{(D^2+\eta^2K\partial_\phi^2-T_0D)w+
       V_0w-\vartheta H^{-1}H_Dw\}.
\tag{D.1}
$$
Here the matrix order $H^{-1}H_D$, the complete degree-zero coefficients, and the old angle are unchanged. Write
$$
w_0=(a_0,b_0^{\rm Airy}),\qquad
(F_b,F_a)=-\mathcal L_0w_0,\qquad
\mathcal T_\epsilon w_1=(F_b,F_a),\quad a_1(0)=0.
\tag{D.2}
$$
The actual $w_1$ is the characteristic integral already constructed in
[the piecewise transport theorem](R133-supplement-piecewise-real-root-fold-and-closed-forced-Airy-transport.md), (M.13)--(M.17). The present task is to bound $\mathcal L_0w_1$, without replacing $w_1$ by fitted Fourier data.

At the root the Fuchsian equation does retain forcing derivatives. For the scalar part $2Tb_T+b=F_b$, its regular solution satisfies
$$
b^{(k)}(0)=F_b^{(k)}(0)/(2k+1).
\tag{D.3}
$$
The additional analytic coefficients and angular terms give lower-order jet terms in this recursion; they do not remove its leading forcing derivative. Thus a uniform second derivative at the root cannot be obtained merely by dividing the first-order equation by $T$ and retaining only $F_b,F_{b,T}$. The inner analytic argument below pays that missing information.

## 2. A third divided-curvature derivative from the original third jet

Put $\rho=r_*-r$ and
$$
k(\rho)=-K(r_*-\rho)/\rho
       =\int_0^1K_r(r_*-t\rho)\,dt .
\tag{D.4}
$$
The genuine root is fixed on the present explicit parameter family, since the compact intrinsic parameter bump vanishes on this window. All root uncertainty is still retained in numerical interval evaluations.

At every strict real point, exact differentiation gives
$$
\rho k_\rho+k=K_r,\qquad
\rho k_{\rho\rho}+2k_\rho=-K_{rr},\qquad
\rho k_{\rho\rho\rho}+3k_{\rho\rho}=K_{rrr},
\tag{D.5}
$$
where the right sides are evaluated at $r_*-\rho$. Moreover
$$
k_{\rho\rho}=\int_0^1t^2K_{rrr}(r_*-t\rho)\,dt.
$$
Therefore, on $|\rho|\ge h>0$,
$$
|k_{\rho\rho\rho}|
 \le\frac{|K_{rrr}|+3|k_{\rho\rho}|}{h}
 \le\frac{2}{h}\sup_{[r_*,r]}|K_{rrr}|.
\tag{D.6}
$$
This uses the original third intrinsic derivative, not an unproved fourth derivative. It also avoids the four separate large terms obtained by differentiating $-K/\rho$ three times.

A sharper cancellation is available without new target values:
$$
k_{\rho\rho\rho}
 =\frac{3}{\rho}\int_0^1t^2
 \{K_{rrr}(r)-K_{rrr}(r_*-t\rho)\}\,dt.
\tag{D.7}
$$
The complete saved closed intervals can bound this difference after subtracting any one common exact scalar anchor. The anchor cancels identically. Every interval of the root-to-point path must be included, and no derivative of a value-only error ball is taken. Formula (D.6) remains a valid fallback.

## 3. A third fold derivative without a third radial speed derivative

Use the paid radial coefficient $a=\eta\sqrt{k}$ and drift $e_d=-d$. The exact fold identities are
$$
X_\rho=e_dX_\phi+\tfrac23a\rho^2A_\phi,\qquad
2\rho A_\rho+3A=2\rho e_dA_\phi+3aX_\phi .
\tag{D.8}
$$
Differentiate the second identity twice, on one open original piece:
$$
\begin{split}
2\rho A_{\rho\rho\rho}+7A_{\rho\rho}
={}&4\{(e_d)_\rho A_\phi+e_dA_{\rho\phi}\}\\
&+2\rho\{(e_d)_{\rho\rho}A_\phi
       +2(e_d)_\rho A_{\rho\phi}
       +e_dA_{\rho\rho\phi}\}
 +3(aX_\phi)_{\rho\rho}.
\end{split}
\tag{D.9}
$$
The last product is
$$
(aX_\phi)_{\rho\rho}
 =a_{\rho\rho}X_\phi+2a_\rho X_{\rho\phi}
                      +aX_{\rho\rho\phi}.
$$
Every term on the right has at most two radial derivatives of $a$, and at most two radial derivatives of the previously bounded fold. Dividing by $2\rho$ is allowed only on the declared strict region. In particular a sufficient bound is the full triangle bound of the right side of (D.9), plus $7|A_{\rho\rho}|$, divided by $2h$.

The first equation of (D.8) gives
$$
\begin{split}
X_{\rho\rho\rho}={}&
 (e_d)_{\rho\rho}X_\phi+2(e_d)_\rho X_{\rho\phi}
                        +e_dX_{\rho\rho\phi}\\
&+\tfrac23\{
 a_{\rho\rho}\rho^2A_\phi
 +2a_\rho(2\rho A_\phi+\rho^2A_{\rho\phi})\\
&\hspace{35mm}+a(2A_\phi+4\rho A_{\rho\phi}
                         +\rho^2A_{\rho\rho\phi})\}.
\end{split}
\tag{D.10}
$$
Angular derivatives of (D.9)--(D.10) are paid either by the complete Fourier coefficient formulas or by a declared positive angular loss. For example $A_{\rho\rho\phi\phi}$ can be bounded from the already paid analytic $A_{\rho\rho\phi}$ norm on a larger strip. No new radial derivative is hidden in this angular step.

The actual lower radial derivatives used here are those of the same fold. In particular their previously paid seam contributions, including (L.21) of the first-forcing theorem, are not removed. Equations (D.9)--(D.10) hold separately on every original piece and on its one-sided traces.

## 4. The first forcing derivative requires no additional intrinsic jet

The leading formula is
$$
G=(k_*/\eta_*)^{1/6}A^{1/6}k^{-1/4}E_G,\qquad
a_0=G(X_\phi^2-TT_\phi^2),\quad
b_0^{\rm Airy}=-2i\epsilon GX_\phi T_\phi,\quad
T=-\rho A^{2/3}.
\tag{D.11}
$$
Here $(\log E_G)_\rho=2b\langle u^2+Kv^2\rangle$ is a genuine radial scalar. Its third derivative uses only two derivatives of the displayed integrand. Together with the true nonzero gaps for $A,k,\eta$, (D.5)--(D.10) give every third radial derivative of $w_0$, with additional angular derivatives supplied on a smaller strip.

For completeness, the coefficient derivative in $\partial_r\mathcal L_0w_0$ uses $\mu_r$, $d_{rr}$, $(T_0)_r$, $(V_0)_r$, $\vartheta_r$, and $(H^{-1}H_D)_r$. These follow by the exact product, quotient and inverse rules from the original fields through radial order two and the fold through order two. The mean in every product remains the original mean at fixed $r$. In particular
$$
(H^{-1})_r=-H^{-1}H_rH^{-1}
\tag{D.12}
$$
retains its full matrix order. The principal factor can be differentiated in its nonsingular form
$$
\mu=a^2A^{-2/3}(X_\phi^2+TT_\phi^2).
$$
The coefficient $\mu$ uses the same orientation convention as the original principal fold; this displayed identity and its nonzero gap are already part of that fold.

Consequently the exact $F_{a,r},F_{b,r}$ have finite complete bounds on each strict piece using only the original intrinsic jets through order three, the original finite physical cubics, all continuous repair fees at order zero, and the true lower-fold derivative arrays. No $K^{(4)}$, $K^{(5)}$ or $\gamma^{(4)}$ is needed in this strict construction.

This is a permission to consume the existing third jets with the displayed factors $h^{-1}$, not a claim that those factors are numerically inexpensive.

## 5. Strict-piece second derivatives of the actual forced amplitude

Use the exact physical-$r$ characteristic notation from (M.13)--(M.15):
$$
t=\sqrt{-T},\quad c_\sigma=d+\sigma\eta q,\quad
V_\sigma=a_1+\sigma i\epsilon t b_1,\quad
V_{\sigma,0}=G(X_\phi+\sigma tT_\phi)^2,
$$
$$
C_\sigma=aA^{-1/3}(X_\phi-\sigma tT_\phi),\quad
z_\sigma=V_\sigma/V_{\sigma,0},\quad
g_\sigma=\frac{C_\sigma}{2V_{\sigma,0}}
                 (F_a-\sigma i\epsilon F_b/t).
\tag{D.13}
$$
Both complex branches on the positive side are retained. Then
$$
(z_\sigma)_r=c_\sigma(z_\sigma)_\phi+g_\sigma,
$$
$$
(z_\sigma)_{rr}
 =c_\sigma^2(z_\sigma)_{\phi\phi}
   +\{(c_\sigma)_r+c_\sigma(c_\sigma)_\phi\}
                         (z_\sigma)_\phi
   +c_\sigma(g_\sigma)_\phi+(g_\sigma)_r .
\tag{D.14}
$$
In particular only one radial derivative of the forcing occurs.

The original complete first-amplitude bound and the complete leading branch inverse bound give
$$
|z_\sigma|\le
 |V_{\sigma,0}^{-1}|\,(|a_1|+|t|\,|b_1|).
$$
The first two angular derivatives of $z_\sigma$ follow by Cauchy with a strictly positive old-angle margin. The complete $g_\sigma,g_{\sigma,r}$ are evaluated from (D.13), (D.12), and Section 4; $g_{\sigma,\phi}$ likewise uses a declared angular margin. All these operations use the same original circle.

On $|\rho|\ge h$ the true bound
$$
|t|\ge h^{1/2}A_-^{1/3}
\tag{D.15}
$$
makes division in (D.13) and in the reconstruction legitimate. Use
$$
(V_\sigma)_{rr}
 =(V_{\sigma,0})_{rr}z_\sigma
 +2(V_{\sigma,0})_r(z_\sigma)_r
 +V_{\sigma,0}(z_\sigma)_{rr},
$$
then
$$
a_1=(V_++V_-)/2,\qquad
b_1=(V_+-V_-)/(2i\epsilon t).
\tag{D.16}
$$
The complete $t_r,t_{rr}$ follow from $t^2=-T$. This gives both amplitudes and all derivatives of total old $(r,\phi)$ order at most two on strict pieces. Every angular derivative required by a subsequent symbol bound is paid on a further smaller strip.

A separate scalar upper bound for each term in (D.14)--(D.16), followed by the full triangle sum, is valid. The two branches are not treated as equal and no independently rounded quotient is divided by a number approaching zero.

## 6. A nonsingular analytic inner bound using the paid leading branches

Only the actual root germ is used here. It is the germ with no original polynomial seam inside its certified old complex domain. The already executed
[closed-amplitude certificate](R133-supplement-actual-closed-leading-Airy-amplitude-bounds.md)
supplies leading bounds on the canonical rectangle
$|T|\le81/4000000,\ |\operatorname{Im}X|\le1/128$, together with the actual inverse-domain information from the fold.

Choose a smaller forcing rectangle
$$
|T|\le R_T,\qquad |\operatorname{Im}X|\le\Sigma_F
\tag{D.17}
$$
inside that paid rectangle. Its actual inverse image must have strictly positive radial and angular distances from the boundary of a paid old complex product. These are explicit gates, not assumed solely from $R_T>0$.

On that old product use the complete leading sup bound $W_g$ from the closed formula (D.11). This bound must hold on the entire old product used for Cauchy. A supremum known only on a canonical rectangle cannot be transferred to a larger old product unless its complete forward image has also been certified inside that rectangle; alternatively evaluate (D.11) directly with the original complex-germ enclosures. If the distances from the inverse image of (D.17) are $\Delta_r,\Delta_\phi>0$, Banach-valued Cauchy gives
$$
\|\partial_r^i\partial_\phi^j w_0\|
 \le i!j!W_g\Delta_r^{-i}\Delta_\phi^{-j}.
\tag{D.18}
$$
Apply the entire (D.1), including $V_0$ and $\vartheta H^{-1}H_D$, to obtain actual complex forcing bounds $F_a^g,F_b^g$. Original complex coefficient norms and their Cauchy margins also pay the first coefficient derivatives appearing in (D.1). This step does not promote the real-only larger-radius first-forcing bounds to complex radial bounds.

The containment can be checked using the actual inverse fold and, in particular,
$|\rho|\le R_TA_-^{-2/3}$ and
$|\operatorname{Im}\phi|\le\Sigma_F+\|X-\phi\|$,
together with the previously proved canonical inverse domain. Every inequality must be strict. The original uncertain root is retained.

There is a useful way to avoid a new large bound for the canonical transport reaction coefficients. Put $\tau=\sqrt T$ and
$$
v_\pm=a_1\pm\tau b_1,\qquad
v_{\pm,0}=a_0\pm\tau b_0^{\rm Airy}.
$$
The exact canonical transport equation (I.21) and its leading homogeneous solution imply
$$
(\partial_\tau\pm2i\epsilon\tau^2\partial_X)
       (v_\pm/v_{\pm,0})
 =(\tau F_a\pm F_b)/v_{\pm,0}.
\tag{D.19}
$$
The local scalar reaction cancels exactly; the first forcing still contains the entire matrix term in (D.1).

Let $B_0,B_0^{-}$ be complete bounds for both $v_{\pm,0}$ and their inverses on (D.17). They are the same leading branch factors already paid by the closed-amplitude theorem. For example $B_0$ may be bounded by $|a_0|+R_T^{5/2}|b_0^{\rm Airy}/T^2|$.

Along the straight complex $\tau$ path the angular displacement is at most $(2/3)R_T^{3/2}$. Thus for
$$
\Sigma_V+(2/3)R_T^{3/2}<\Sigma_F
$$
the exact zero-trace solution satisfies
$$
|v_\pm|\le
V:=B_0B_0^{-}\{(R_T/2)F_a^g+\sqrt{R_T}\,F_b^g\}.
\tag{D.20}
$$
Indeed this is the ordered integral of (D.19); no bound on $l,m$ is discarded, since their exact leading solution has already divided them out.

Uniqueness gives $v_+(-\tau,X)=v_-(\tau,X)$. Hence $a_1$ and $b_1$ are holomorphic in $T$. The odd holomorphic function $(v_+-v_-)/2$ vanishes at $\tau=0$. Applying the maximum modulus principle to its quotient by $\tau$, first on smaller circles and then taking their radii up to $\sqrt{R_T}$, gives
$$
|a_1|\le V,\qquad |b_1|\le V/\sqrt{R_T}
\quad (|T|<R_T,\ |\operatorname{Im}X|\le\Sigma_V).
\tag{D.21}
$$
There is no singular $1/\sqrt{|T|}$ output bound.

On any smaller rectangle $|T|\le R_i<R_T$, $|\operatorname{Im}X|\le\Sigma_i<\Sigma_V$, its complete mixed derivatives satisfy
$$
\|\partial_T^p\partial_X^q a_1\|
 \le p!q!V(R_T-R_i)^{-p}(\Sigma_V-\Sigma_i)^{-q},
\tag{D.22}
$$
and the same inequality with $V/\sqrt{R_T}$ for $b_1$. Composing with the actual old fold uses all first and second chain-rule terms. For instance
$$
w_{rr}=w_{TT}T_r^2+2w_{TX}T_rX_r+w_{XX}X_r^2
                         +w_T\,T_{rr}+w_X\,X_{rr},
\tag{D.23}
$$
where the last two products mean $w_T\,T_{rr}$ and $w_X\,X_{rr}$, not third derivatives of $w$. The paid fold jets, or Cauchy estimates on its genuine germ with positive margins, bound these factors. The other old mixed derivatives follow by the same finite chain rule.

## 7. One trial, full coverage, and the final local source budget

Choose a strict threshold $h>0$ so that the entire inner real set $|\rho|\le h$ at the selected old-angle strip maps inside the smaller rectangle of (D.22). A small overlap with the strict region is allowed and useful. The consumer must certify this inclusion, the inner complex margins, $|\rho|\ge h$ on every strictly estimated subinterval, and coverage of every original common interval.

The analytic germ and the piecewise transport describe the same solution of (D.2): they have the same common root trace and the same actual characteristic integral. On the overlap uniqueness identifies them and all of their true derivatives. The split is only a choice of estimate. No partition of unity, modified amplitude, or artificial delta source is introduced.

If $W^1_{ij}$ bounds the sum of the two actual $w_1$ amplitude norms after $i$ old radial and $j$ angular derivatives, the complete local residual is bounded by
$$
\begin{split}
\|\mathcal L_0w_1\|\le\mu_-^{-1}\big[
&W^1_{20}+2D_0W^1_{11}+(D_0^2+\eta_+^2|K|)W^1_{02}\\
&+(|d_r|+D_0D_1)W^1_{01}
 +|T_0|(W^1_{10}+D_0W^1_{01})\\
&+\{|V_0|+|\vartheta|\,\|H^{-1}\|\,\|H_D\|\}W^1_{00}\big].
\end{split}
\tag{D.24}
$$
Angular symbol derivatives of this complete residual require explicit further angular margins. The density factor of the first corrected local residual is $n^{7/6}n^{-1}=n^{1/6}$; subsequent old-$J$ reconstruction and source propagation must use their actually proved windows.

At an original strict seam, all derivatives in Sections 2--5 are one-sided. The already computed first-amplitude state jump remains exactly (M.17), with (M.16)'s two branch formulas. Its delta source is not put into a volume $L^2$ norm or counted twice. The original 1079-seam certificate remains valid because the amplitude has not changed.

The complete old-$I/J$ remainders on $w_1$, independent mean, true finite head, positive response and full return still have their own terms. This theorem pays a derivative route for the local first-corrected residual. Its public numerical execution must retain those distinctions, all original input identities and every failed prefix. Neither numerical smallness nor a cutoff-97 inverse follows before that execution and the remaining full operator composition.
