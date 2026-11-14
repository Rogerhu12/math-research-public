# R133 supplement: complete explicit-family circle KAM inputs and gates

2026-11-14, visible-exact-astra-0df / phase_inverse.

This supplies complete uniform $P,Q,T,B$ bounds for the **specified**
family

$$
 Q_\delta=\overline Q+\delta Z,\quad \nu_\delta=\nu_0+\delta,\quad
 F_\delta(x)=4G\big(P_\delta(G^{-1}(x/4))\big),\quad G=K48\circ H.
 \tag{C.1}
$$

The initial KAM lift is the identity. The exact target is
$\alpha=4\Omega_{15}=2\pi\rho_{15}$, and the complete circle
small-divisor constant is $K=17/4$.
All input estimates below concern the same actual family and actual
parameter interval. They do not identify $Z$ with a PDE response.

The numerical source is
`fourfold_codazzi_phase_explicit_family_R31.py`.
It has no local numerical gate execution: the public Actions DAG
executes the source with the pinned inputs and retains every actual
gate, including failures. The existence conclusion in Section6 is
activated only when that real execution reports all its gates true.
The uniform bound construction in Sections1--5 is proved here
independently of whether the final numerical smallness gate passes.

## 1. Fixed root and genuine parameter domain

The compact metric parameter has support
$[1/20,9/50]$, strictly below the true turning root. On this support
write $k=Tw'$; the exact identities are

$$
 K_\delta=(K+\delta k)e^{-\delta w},\qquad
 \gamma_\delta=\gamma e^{\delta w/2},\qquad
 c_\delta=-\gamma(m+\delta z)\sqrt{q^2-\delta k}.
 \tag{C.2}
$$

Here $m=\langle v\rangle$ and $z=\langle\zeta\rangle$ are the full
physical means. Off the support, $w=k=0$ exactly. In particular
$K_\delta=K$ on the entire root neighborhood, and the intrinsic
root $r_*$ is independent of$\delta$. There are no moving-root
parameter terms. The root part of $\partial_\delta^2c_\delta$ is
exactly zero, while the quadratic state term in
$\partial_\delta^2d_\delta$ is generally nonzero and is retained.

The complete all-parameter scalar native has already proved (C.2)
and the true square-root branch on the complex disc
$|\delta|\le10^{-6}$. We use the real interval

$$
 |\delta|<r_a=10^{-8}.
 \tag{C.3}
$$

For real$\delta$, $c_\delta$ is real, so it gives a real translation
in the angular Wiener algebra. Its large value causes no loss of
analytic width. Its first and second parameter derivatives remain
in every parameter-source bound. The complete mean margin also
persists on the larger certified disc.

## 2. Full second parameter field, including the root

All angular field norms in this section are on the physical
strip$s_*=1/16$. Let $U,V,X,Z$ be the proved complete uniform
norms of $u,v,\xi,\zeta$ of the exact continuous base and direction.
Let $M,z_*$ bound the full scalar means$|m|,|z|$.
Write $\rho=10^{-6}$ and $V_\rho=V+\rho Z$.

The drift is exactly

$$
 d_\delta=\beta I\big((u+\delta\xi)^2+
                         K_\delta(v+\delta\zeta)^2\big).
$$

Its complete second parameter derivative is

$$
 \partial_\delta^2d_\delta=
 \beta I\big(
    2\xi^2+K_\delta''(v+\delta\zeta)^2
    +4K_\delta'(v+\delta\zeta)\zeta+2K_\delta\zeta^2\big).
 \tag{C.4}
$$

Since $\|I\|_{A_s\to A_s}\le1/4$, the already computed scalar
coefficients

$$
 B_\beta=\int|\beta|/4,\quad
 B_K=\int|\beta K_\delta|/4,\quad
 B_{K'}=\int|\beta K_\delta'|/4,\quad
 B_{K''}=\int|\beta K_\delta''|/4
$$

give the strict-interval bound

$$
 D_{2,\rm strict}
 =2B_\beta X^2+B_{K''}V_\rho^2+
                 4B_{K'}V_\rho Z+2B_KZ^2.
 \tag{C.5}
$$

The integrals in (C.5) are the actual full626-cell bounds uniform
on the complex parameter disc; they are not point samples.
On the remaining root interval of length at most
$\Delta=r_*^{\rm upper}-r_b$, the true analytic germ and root
identity give $|K|\le K_1\Delta$ and $|\beta|\le\beta_*$. The
complete omitted quadratic drift is therefore bounded by

$$
 D_{2,\rm root}=
 \frac{\Delta\beta_*}{2}\big(X^2+K_1\Delta Z^2\big).
 \tag{C.6}
$$

Set $D_2=D_{2,\rm strict}+D_{2,\rm root}$.
Both components and all193 physical states of the direction are used.
The second parameter drift has angular degree at most192. Therefore
its first and second angular derivatives cost at most$768D_2$
and$768^2D_2$, respectively. These are support inequalities for the
complete finite field, not a projection of the resulting return.

The exact optical cancellation and the full all-parameter native
similarly give

$$
 C_2=M\,C_{2,m}+z_*\,C_{2,z}
 \ge\int_0^{r_*}
       \sup_{|\delta|\le\rho}|\partial_\delta^2c_\delta|\,dr.
 \tag{C.7}
$$

The integrand vanishes identically off compact support, so no
additional root optical term is missing.

## 3. Uniform true flow and parameter derivatives

The complete analytic-field native supplies

$$
 B_0=\int\|d_0\|,\quad
 L_0=\int\|\partial_\phi d_0\|,\quad
 D_{20}=\int\|\partial_\phi^2d_0\|.
$$

The full correlated first-parameter native supplies
$D_{10},D_{11},D_{12}$, the corresponding angular derivative orders
0,1,2 of $\partial_\delta d_0$, and
$C_{10}=\int|\partial_\delta c_0|$. All already include the true
root and all means. Taylor's integral formula in the **same**
parameter interval gives the complete one-leg bounds

$$
 \begin{aligned}
 B_\delta&=B_0+r_aD_{10}+\tfrac12r_a^2D_2,\\
 L_\delta&=L_0+r_aD_{11}+\tfrac12r_a^2(768D_2),\\
 D_{20,\delta}&=D_{20}+r_aD_{12}+\tfrac12r_a^2(768^2D_2),\\
 D_{1,\delta}&=D_{10}+r_aD_2,\\
 Q_{1,\delta}&=D_{11}+r_a(768D_2),\\
 C_{1,\delta}&=C_{10}+r_aC_2.
 \end{aligned}
 \tag{C.8}
$$

Represent $P_\delta$ as the true plus flow followed by the reversed
minus flow. The radial domain is fixed by Section1. Put

$$
 \ell=2L_\delta,\quad J=e^\ell,\quad
 V_1=2(D_{1,\delta}+C_{1,\delta}),\quad
 Q_1=2Q_{1,\delta},\quad
 V_2=2(D_2+C_2),\quad D_{20}^*=2D_{20,\delta}.
$$

On every actual allowed complex path, variational equations and
their full integration factors give

$$
 \begin{aligned}
 \|P_\phi\|&\le J,&
 \|P_\delta\|&\le Y:=JV_1,\\
 \|P_{\phi\delta}\|&\le JQ_1+J^2D_{20}^*V_1,&
 \|P_{\delta\delta}\|&\le
       JV_2+2JQ_1V_1+J^2D_{20}^*V_1^2,\\
 \|P_{\phi\phi}\|&\le J^2D_{20}^*.
 \end{aligned}
 \tag{C.9}
$$

For example, the mixed equation has source
$F_{\phi\phi}P_\phi P_\delta+F_{\phi\delta}P_\phi$.
Its propagation factor from a source point to the endpoint is
$\exp\int_{\rm remaining}\|F_\phi\|$. Combining this with the
initial-to-source factors gives at most$J^2$ for the first term
and$J$ for the second. The second parameter equation has sources
$F_{\phi\phi}P_\delta^2+2F_{\phi\delta}P_\delta+
F_{\delta\delta}$, giving the third line of (C.9).
Thus there is no dropped mixed derivative or second parameter source.

These are Wiener inequalities for the functions of the initial
complex angle. The real scalar translation is an isometry; the
periodic parts of the two actual flows have total norm at most
$2B_\delta$. All intermediate source compositions are covered by
the same full path budget.

## 4. One common wide angular domain for all P, Q and T

For any physical width$a$, compute exact finite norms
$h_j=\|h^{(j)}\|_a$ and
$k_j=\|k^{(j)}\|_{a+h_0}$, for$j=0,1,2$.
The whole compositions give

$$
 U_G(a)=h_0+k_0,\quad
 V_G(a)=h_1+(1+h_1)k_1,
$$

$$
 G_1(a)=(1+h_1)(1+k_1),\qquad
 G_2(a)=h_2(1+k_1)+(1+h_1)^2k_2.
 \tag{C.10}
$$

Use inverse outer width$a=1/24$ and normalized wide parameter
width$S_w=1/8$ (physical width$1/32$).
The actual gates are

$$
 V_G(1/24)<1,\qquad
 S_w/4+U_G(1/24)<1/24,
$$

$$
 S_w/4+U_G(1/24)+2B_\delta<1/16.
 \tag{C.11}
$$

The Banach-algebra contraction for the periodic part of $g=G^{-1}$
then gives, on physical width$S_w/4$,

$$
 \|g-{\rm id}\|\le U_G(1/24),\quad
 g_1=(1-V_G(1/24))^{-1},\quad
 g_2=G_2(1/24)g_1^3.
$$

The last gate in (C.11) places every return path in the already
proved field strip$1/16$ and every output argument of $G',G''$ in
that same strip. In (C.9), use the bounds after composition with$g$;
the path proof just given pays these compositions as well.

Write $G_1=G_1(1/16)$ and $G_2=G_2(1/16)$. With the normalization
$x=4\phi$, the actual uniform R31 quantities on$A_{S_w}$ are

$$
 \begin{aligned}
 P&=4G_1Y,\\
 Q&=g_1\big(G_2JY+G_1\|P_{\phi\delta}\|\big),\\
 T&=4\big(G_2Y^2+G_1\|P_{\delta\delta}\|\big).
 \end{aligned}
 \tag{C.12}
$$

The factors4,1,4 are respectively those of
$\partial_\delta F$, $\partial_x\partial_\delta F$ and
$\partial_\delta^2F$ for (C.1). The source also retains the direct
coarse second angular derivative

$$
 B_{\rm coarse}=\tfrac14\left[
 (G_2J^2+G_1\|P_{\phi\phi}\|)g_1^2+G_1Jg_2\right]
$$

as a separate check. The sharper bound used below is proved
independently; it does not silently substitute a fitted derivative.

## 5. A small genuine B from the whole initial error

The exact initial full defect is already bounded in physical
$A_{1/50}$. The postcomposition native also proves
$\|G-{\rm id}\|_{1/50}<.003672400504$ and a derivative contraction.
Consequently the actual inverse$g$ exists with the same periodic
norm bound on physical width$.016$, because

$$
 .016+\|G-{\rm id}\|_{1/50}<.02.
 \tag{C.13}
$$

Thus the normalized true initial circle error is bounded on
$A_{S_e}$ with$S_e=.064$, by exactly the same
$\varepsilon_0=4\|GPG^{-1}-{\rm id}-\Omega_{15}\|$ bound
obtained from the physical defect and the composition lemma.
The source uses the full paid target error, not its finite part.

Choose the R31 family width$S=.063$. The direct Fourier inequality

$$
 \|f''\|_{s-\eta}\le\frac4{e^2\eta^2}\|f\|_s
$$

gives the actual$F_0''$ bound from its true error on$S_e$.
For every real$|\delta|<r_a$, the fundamental theorem in$\delta$
and the uniform wider$P$ bound in (C.12) give

$$
 \boxed{
 B=\frac{4\varepsilon_0}{e^2(S_e-S)^2}
       +\frac{4r_aP}{e^2(S_w-S)^2}.}
 \tag{C.14}
$$

The second term pays the complete
$\partial_\delta\partial_x^2F$ by two angular losses on the wider
strip$S_w$. It is valid on the same explicit family, parameter
interval and genuine angular domain. The identity part and constant
target have zero second derivative, so no additional term is present.

## 6. Exact R31 choices and activation

Use the proved initial lift identity and the sharp actual parameter
row:

$$
 M_0=R_0=1,\quad \sigma_0=1/20,\quad
 K=17/4,\quad s_0=1/16,\quad
 \delta_0=3/200,\quad S=63/1000,\quad r_a=10^{-8}.
 \tag{C.15}
$$

With the same$p,q,t,b$ quantities in (C.12),(C.14), the source
forms precisely R31's

$$
 M=M_0+1,\quad R=2R_0,\quad L_a=2R/\sigma_0,\quad
 A_*=R(1+PL_a),\quad L_H=MKA_*,
$$

$$
 C=KA_*+\tfrac12BL_H^2+QL_HL_a+\tfrac12TL_a^2,\qquad
 Z=R_0QL_H+R_0TL_a+PR_0^2L_H.
$$

All bounds are rounded outward. It then checks all three smallness
inequalities together and both actual domain margins:

$$
 \varepsilon_0\le\delta_0^2\min\left(
 \frac1{32C},\frac1{4R_0L_H},\frac{\sigma_0}{8Z}\right),
$$

$$
 2L_a\varepsilon_0<r_a,\qquad
 s_0+\frac{2L_H\varepsilon_0}{\delta_0}<S.
 \tag{C.16}
$$

If the real public execution passes these gates, R31 proves the
existence of a **real**$\delta_\infty$ in (C.3) and an oriented
analytic circle lift$H_\infty$ satisfying

$$
 F_{\delta_\infty}\circ H_\infty
       =H_\infty\circ R_{2\pi\rho_{15}}.
 \tag{C.17}
$$

The parameter and conjugacy changes are the actual recorded
$2L_a\varepsilon_0$, $2L_H\varepsilon_0/\delta_0$ and
$2L_H\varepsilon_0/\delta_0^2$ bounds. No numerical value of
$\delta_\infty$ is asserted from an existence theorem.

For the choices (C.15), the proved final strip is
$s_\infty=s_0-4\delta_0=1/400=.0025$ in the normalized variable,
or$1/1600=.000625$ in physical angle. This positive width is part
of the conclusion. A subsequent normal form must actually pay its
analytic costs at an available width; the wider initial strip is
not automatically inherited by the exact conjugacy. Any later
smaller-loss R31 budget must be checked and recorded separately.

## 7. Public computation and scope

The public nine-step DAG is
`scripts/fourfold_codazzi_phase_small_consumers_CI.py`, with fixed
input manifest
`notes/2026-11-14-R133-phase-small-consumers-CI-inputs.json`.
It verifies the complete238 input paths, freezes the exact science,
and uses all169 existing transport natives without recomputation.
It produces fresh genuine Wiener, terminal K48, target15, sharp
parameter-row and R31 native files. The process record retains
the real public repository, run, attempt, commit, source hashes,
commands, exit codes and output hashes. A failed final gate is
preserved and does not activate (C.17).

Even a successful (C.17) concerns exactly the explicit family (C.1).
It supplies a real parameter conjugacy for its true principal
two-ray return. It does not make that family solve the full PDE,
replace its complete regular response by$Z$, establish the full
body inverse, or discard the physical first scalar phase and
strong return remainder. Those obligations remain in the joint
construction.
