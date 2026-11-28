# Near-cut transfer by an inverse radius chart and a background-only difference

This is an independent conditional proof for the complete finite tail map. It does not certify an unspecified tail, rerun R58, or change any saved field. Its inputs are a genuine complete old shared-radius tail certificate and rigorous bounds for the same true R58 background on the interval stated below. All perturbation height means and all declared Fourier modes remain unchanged. No third derivative of the perturbation is needed.

## 1. Domains and the exact inverse chart

Let \(R_c>0\) be the physical cut radius, \(d>0\) the literal transition-width input, and \(c\) the saved finite tail's outer radius. Assume

\[
0<R_-:=R_c-d<c\le R_c,\qquad e=|c-R_c|,\qquad
a=\frac{15e}{8d}<1.
\tag{1}
\]

The old true-background stage kernel explicitly rejects a literal outer radius greater than \(R_c\). Thus the hypothesis \(c\le R_c\) is already necessary for using its accepted cut-stage certificate; it is not supplied by extrapolating that certificate. If a new source has \(c>R_c\), this theorem must not be applied without a separate extension contract and corresponding old certificate.

On the physical interval \([R_-,R_c]\) define

\[
r(R)=R+(c-R_c)P((R-R_-)/d),\qquad
P(u)=10u^3-15u^4+6u^5.
\tag{2}
\]

Before \(R_-\), let \(r(R)=R\). The identities \(P(0)=P'(0)=P''(0)=0\), \(P(1)=1\), and \(P'(1)=P''(1)=0\) make this a \(C^2\) chart with

\[
r(R_-)=R_-,\quad r(R_c)=c,\quad r'(R_c)=1,\quad r''(R_c)=0.
\tag{3}
\]

Since \(0\le P'\le15/8\), equation (1) proves strict monotonicity. Its inverse \(\phi\) maps the **actual old interval**

\[
J=[R_-,c]\quad\hbox{onto}\quad K=[R_-,R_c].
\tag{4}
\]

Both \(r\) and \(\phi(r)\), and the interval between them, lie in the same true-background domain \(K\). The old finite perturbation is evaluated only at \(r\in J\), never at a nonexistent outer value \(V(R)\) for \(R>c\).

Define

\[
b=\frac{6e}{d^2},\qquad
A=\frac{a}{1-a},\qquad B=\frac{b}{(1-a)^3}.
\tag{5}
\]

The exact maximum of \(|P''|\) is \(10/\sqrt3<6\). The inverse-function formulas therefore give

\[
|\phi-r|\le e,\quad
\frac1{1+a}\le\phi'\le\frac1{1-a},\quad
|\phi'-1|\le A,\quad |\phi''|\le B.
\tag{6}
\]

These bounds are mathematical inequalities for the real chart; a numerical inverse need not be chosen to define it.

## 2. The complete old and new maps in one coordinate

Write the old map as

\[
X_0(r,\theta)=B_0(r,\theta)+V(r,\theta),\qquad
B_0(r,\theta)=r e_r(\theta)+(C+H(r))e_z,
\tag{7}
\]

where \(H'(r)=-w(r)\), \(C\) is the same fixed placement constant, and \(V\) includes the complete saved perturbation with its cumulative height zero mode. A fixed reflection may be absorbed into \(V\) and \(B_0\); it changes none of the norms below. The exact background metric is

\[
g_0=E(r)\,dr^2+r^2d\theta^2,\qquad E(r)=1+w(r)^2.
\tag{8}
\]

The intended new map in physical radius is \(B_0(R,\theta)+V(r(R),\theta)\). In the inverse coordinate it is exactly

\[
X_1(r,\theta)=X_0(r,\theta)+D(r,\theta),\qquad
D=B_0(\phi(r),\theta)-B_0(r,\theta).
\tag{9}
\]

The whole function \(V(r,\theta)\), including every mean and high mode, cancels from the difference. This is a change of coordinate of the new map, not an extension, truncation, or replacement of \(V\).

Suppose the old complete certificate supplies

\[
\|g_0^{-1/2}(dX_0^TdX_0-g_0)g_0^{-1/2}\|\le\epsilon_0,\quad
\|dV\|_{g_0}\le\eta_0,\quad
\|\nabla^2_{g_0}V\|\le\beta_0.
\tag{10}
\]

The Frobenius bounds used by the existing kernel imply the operator bounds in (10). Use the original certified span bounds, or their maximum over a genuine complete covering of \(J\). A span intersecting \(R_-\) may be restricted to that intersection without changing its bound. No tail region or angular frequency may be omitted.

## 3. Background-only first and second derivative bounds

Obtain rigorous real-background bounds on all of \(K\):

\[
|w|\le W,\qquad |w_R|\le W_1,\qquad |w_{RR}|\le W_2.
\tag{11}
\]

Here \(w\) is continuously differentiable on \(K\); \(w_R\) is continuous and absolutely continuous on each member of a finite partition of \(K\). The last bound in (11) may hold almost everywhere, or be obtained from both one-sided values on the partition pieces. Continuity at their joins then makes \(w_R\) globally Lipschitz with constant \(W_2\). This covers the absolute-value cusps in the R58 radius construction and does not assume that the background has a globally continuous third derivative.

Let \(\delta=\phi-r\). Direct differentiation gives

\[
\begin{aligned}
D_r&=\delta'(e_r-w(\phi)e_z)
       -(w(\phi)-w(r))e_z,\\
D_{rr}&=\delta''(e_r-w(\phi)e_z)\\
 &\quad-\{w_R(\phi)((\phi')^2-1)
                 +w_R(\phi)-w_R(r)\}e_z,\\
D_\theta&=\delta e_\theta,\quad
D_{r\theta}=\delta'e_\theta,\quad
D_{\theta\theta}=-\delta e_r .
\end{aligned}
\tag{12}
\]

The mean-value estimate for \(w\), and the integral/Lipschitz estimate \(|w_R(u)-w_R(v)|\le W_2|u-v|\), are applied only inside the true-background interval \(K\). For the latter estimate, split the segment at every partition join and add the almost-everywhere derivative bounds; a globally defined classical \(w_{RR}\) is unnecessary. Equations (6), (11), and (12) imply

\[
\begin{aligned}
Q_0&=e\sqrt{1+W^2},\\
Q_1&=A\sqrt{1+W^2}+W_1e,\\
Q_2&=B\sqrt{1+W^2}+W_2e
             +W_1((1-a)^{-2}-1),
\end{aligned}
\tag{13}
\]

with \(|D|\le Q_0\), \(|D_r|\le Q_1\), \(|D_{rr}|\le Q_2\), and
\(|D_\theta|\le e\), \(|D_{r\theta}|\le A\), \(|D_{\theta\theta}|\le e\).
The displayed bound for \(|(\phi')^2-1|\) covers both sides of the interval in (6).

Using \(E\ge1\) and \(r\ge R_-\), a compatible normalized first-jet bound is

\[
\eta_D=\sqrt{Q_1^2+(e/R_-)^2}.
\tag{14}
\]

The sharper operator bound \(\max(Q_1,e/R_-)\) also follows because \(D_r\) lies in the radial/vertical plane and \(D_\theta\) is orthogonal to that plane. Formula (14) directly matches the old kernel's Frobenius convention.

For the second derivative, the normalized covariant components are

\[
\frac{D_{rr}}E-\frac{ww_R}{E^2}D_r,\qquad
\frac{D_{r\theta}-D_\theta/r}{r\sqrt E},\qquad
\frac{D_{\theta\theta}}{r^2}+\frac{D_r}{rE}.
\tag{15}
\]

The true R58 bounds \(|w|\le41/100\) and meridional curvature
\(|w_R|/E^{3/2}\le8\) imply

\[
\frac{|ww_R|}{E^2}\le\frac{8|w|}{\sqrt E}\le\frac{82}{25}.
\tag{16}
\]

This is a bound for the **normalized** coefficient in (15), not a claim that the unnormalized Christoffel symbol is at most \(82/25\).

Consequently set

\[
\begin{aligned}
h_{11}&=Q_2+\tfrac{82}{25}Q_1,\\
h_{12}&=(A+e/R_-)/R_-,\\
h_{22}&=e/R_-^2+Q_1/R_-,\\
\beta_D&=\sqrt{h_{11}^2+2h_{12}^2+h_{22}^2}.
\end{aligned}
\tag{17}
\]

Then \(\|\nabla^2_{g_0}D\|\le\beta_D\). There is no derivative of \(V\) in (12)--(17), and no perturbation third-jet estimate is required.

## 4. Metric transfer and the physical target

By (10), \(\|dX_0\|_{g_0}\le\sqrt{1+\epsilon_0}\). Expanding the Gram matrix of \(X_0+D\) gives, relative to \(g_0\),

\[
\widetilde\epsilon=
\epsilon_0+2\sqrt{1+\epsilon_0}\eta_D+\eta_D^2.
\tag{18}
\]

The desired target in the inverse coordinate is the physical metric at \(R=\phi(r)\):

\[
g_1=(\phi')^2E(\phi)\,dr^2+\phi^2d\theta^2.
\tag{19}
\]

It is not \(g_0\). Its two diagonal ratios relative to \(g_0\) are

\[
q_r=(\phi')^2E(\phi)/E(r),\qquad q_\theta=(\phi/r)^2.
\tag{20}
\]

One explicit enclosure uses any certified \(E_{\min}\le E(r)\), with \(E_{\min}\ge1\). Let

\[
\zeta=2WW_1e/E_{\min},\qquad \chi=e/R_-,
\tag{21}
\]

and verify \(\zeta<1,\chi<1\). The bound on \(E(\phi)-E(r)\) comes from
\(|E'|\le2WW_1\). Then

\[
\frac{1-\zeta}{(1+a)^2}\le q_r\le
\frac{1+\zeta}{(1-a)^2},\qquad
(1-\chi)^2\le q_\theta\le(1+\chi)^2 .
\tag{22}
\]

Let \(q_-\) be the smaller lower endpoint and \(q_+\) the larger upper endpoint in (22), and put
\(\delta_g=\max(1-q_-,q_+-1)\). If \(\delta_g<1\), matrix congruence and the triangle inequality give the required bound

\[
\boxed{\quad
\epsilon_{\rm new}\le
\frac{\widetilde\epsilon+\delta_g}{1-\delta_g}.
\quad}
\tag{23}
\]

The final acceptance check must apply (23), with outward arithmetic, against the original metric tolerance. Smallness of \(e\) alone does not waive that check.

## 5. Curvature and optional placement bounds

Assume \(\eta_0+\eta_D<1\). Relative to \(g_0\), the new differential has least singular value at least \(1-\eta_0-\eta_D\). Since \(B_0\) is an isometric background with curvature bound \(8\) and its covariant Hessian is normal, projection onto the new normal yields

\[
\boxed{\quad
K_{\rm new}\le
\frac{8+\beta_0+\beta_D}{(1-\eta_0-\eta_D)^2}.
\quad}
\tag{24}
\]

This is a bound for the actual map's principal curvatures, computed with reference \(g_0\). Curvature is unchanged by the inverse coordinate. No additional target-ratio factor from (19) is needed in (24).

If an old complete placement certificate also gives \(|X_0|\le R_0\) and
\(X_0\cdot n_0\ge\sigma_0\), then \(|X_1|\le R_0+Q_0\). For a conservative support transfer, put

\[
t=2\sqrt{1+\epsilon_0}\eta_D+\eta_D^2.
\]

The normalized old area is at least \(1-\epsilon_0\). If
\(\epsilon_0<1\) and \(t<1-\epsilon_0\), the orientation remains consistent and
\(\lvert n_1-n_0\rvert\le2t/(1-\epsilon_0)\). Hence

\[
X_1\cdot n_1\ge
\sigma_0-Q_0-\frac{2R_0t}{1-\epsilon_0}.
\tag{25}
\]

These are bounds on this same transformed map, not substitutions of independently favorable fields.

The placement and support bounds require the old certificate to use the same height constant \(C\) as (7). If its height placement differs by a known constant translation \(\Delta C\,e_z\), add \(|\Delta C|\) to the position difference \(Q_0\) in these two placement bounds. This does not change \(\eta_D,\beta_D\), the metric transfer, or the curvature transfer. In particular, the final prefix height and the tail's cumulative height mean cannot be silently replaced by a convenient older placement.

## 6. Data obligations and scope

Bind the old complete tail certificate to the actual full coefficient files, all shared spans, its unreset mean chain, its full planar/height spectrum, and the same true-background normalization. Check (1), exact coverage of \(J\), and the original kernel's \(c\le R_c\) domain gate. Bind the literal \(R_c,c,d\) and the actual background bounds (11) on the complete interval \(K\).

The exact identities (9) and (19) preserve the full perturbation and the physical target. They resolve the apparent missing \(V(R)\) outside \(c\) without inventing an extension. Existing old certificates are used only on their stated domain. If the needed complete old certificate or the true-background derivative bounds are absent, this theorem remains conditional; neither a sampled background cache nor a partial tail certificate supplies them.

All inequalities are uniform in angle. The recorded phase rotations and lower reflection preserve their Euclidean norms and the axisymmetric background, so the same bounds apply to those pieces once the actual old all-angle certificate is bound. Closed-surface assembly, held-set identities and noncongruence are separate obligations.

## Source contracts

The original complete shared-radius kernel is [`certify_q060_shared_r_tail_batch.py`](../scripts/resume_n4/certify_q060_shared_r_tail_batch.py). Its normalized first derivative and covariant second derivative conventions, its real-background oracle, and its literal outer-radius domain gate supply the contracts used above. The real background and its curvature bound are established in [R58](../results/R58-q060-valley-background-height-and-curvature.md). The intended physical near-cut map is defined in [`actual_closed_map_v2.py`](../scripts/resume_20261128/tail/actual_closed_map_v2.py); the transfer applies to its complete perturbation with its saved mean and every declared Fourier mode, with the literal radius and width inputs bound to the selected actual map. This note proves the transfer conditional on those inputs; its adjacent provenance record does not declare any new finite tail accepted.
