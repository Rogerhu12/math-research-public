# Exact contract for the new Cartesian prefix cut correction

This is a read-only audit of actual_closed_map_v2.py, its inherited atlas, the complete v2 tail spectrum, and the R58 arclength cut identity. It does not invoke a BVP, export a new tail, or certify the corrected map. No hash-bound source was edited. It supplies the mathematical contract for a separate continuous verifier.

## 1. Defining data and derived real constants

Let \(R_c,w_c\) be the literal binary input parameters rCut and wCut, and let \(A_0,A_1,A_2\) be the complete saved tail Fourier coefficient vectors at its literal outer node \(c\). These vectors are the values and first two derivatives with respect to the tail's saved radius variable. Their complete declared planar and height frequency lists are part of the input.

Set, by real arithmetic,

\[
w_{R,c}=-7w_c/R_c,\qquad E_c=1+w_c^2,\qquad
\alpha=-E_c^{-1/2},\qquad \beta=-w_cw_{R,c}/E_c^2.
\]

Thus \(\alpha=R_s\) and \(\beta=R_{ss}\) for outward-increasing meridian arclength \(s\) passing into a tail of decreasing radius. In a rigorous implementation \(R_c,w_c,w_{R,c},E_c,\beta\) are rational expressions and \(\alpha\) is the fixed algebraic real expression. Rounded target.wr/ap/app caches are numerical evaluations of these expressions. Freezing those rounded derived values as independent exact constants would change the R58 seam contract.

Let \(Z\) be the final uncorrected Cartesian prefix's height zero-mode endpoint defining value. Concretely it is the height-frequency-zero entry of prefix.rep.jets[0,:,-1]. At this endpoint the complete radial core lift has zero value/first/second jets, and the center correction vanishes. The constructor uses the same shared endpoint mean datum, so the present intermediate mean_spline endpoint value equals this \(Z\); this endpoint identity must not be generalized to equality of the entire intermediate and final mean functions. Reading \(Z\) directly from the final defining jets makes the identity explicit.

Let \(\mu=A_{0,z,0}\) be the same saved tail height zero-mode coefficient, and write \(S=\operatorname{diag}(1,1,-1)\). If \(V_j(\psi)\) denotes the complete Fourier function with coefficients \(A_j\), then the common Cartesian arclength two-jet is

\[
\begin{aligned}
T_0&=R_c e_r+S V_0+(Z+\mu)e_z,\\
T_1&=\alpha(e_r+S V_1-w_c e_z),\\
T_2&=\alpha^2(S V_2-w_{R,c}e_z)
       +\beta(e_r+S V_1-w_c e_z).
\end{aligned}
\]

The signs agree with the upper tail height
\(Z+\mu+\int_R^{R_c}w(r)\,dr-V_z\).
The lower surface uses the recorded full vertical reflection; its signed-\(s\) first and mixed jets receive the additional orientation sign.

## 2. Exact coefficient construction and all angular orders

Use the union of the prefix and tail planar lists and the union of their height lists. The tail planar degree can exceed the prefix's original side-mode cutoff, even when their independent state count M is equal. Every declared tail planar coefficient remains part of the corrected map.

For a planar frequency \(m\), the target coefficients are

\[
\begin{aligned}
(T_0)_{xy,m}&=R_c\,1_{m=1}+A_{0,xy,m},\\
(T_1)_{xy,m}&=\alpha(1_{m=1}+A_{1,xy,m}),\\
(T_2)_{xy,m}&=\alpha^2A_{2,xy,m}
                    +\beta(1_{m=1}+A_{1,xy,m}).
\end{aligned}
\]

For nonzero height frequencies they are \(-A_{0,z,m}\),
\(-\alpha A_{1,z,m}\), and
\(-\alpha^2 A_{2,z,m}-\beta A_{1,z,m}\).
For the zero height mode they simplify to

\[
(T_0)_{z,0}=Z,\qquad
(T_1)_{z,0}=-\alpha(w_c+A_{1,z,0}),\qquad
(T_2)_{z,0}=-\alpha^2(w_{R,c}+A_{2,z,0})
                    -\beta(w_c+A_{1,z,0}).
\]

Only the value zero mode cancels. The complete tail mean's first and second derivative zero modes must remain. Explicitly using \(Z\) in the first formula avoids interval cancellation of two appearances of the same \(\mu\).

Angular derivatives multiply a planar exponential by \((im)^j\). A height cosine has derivatives
\(\cos(m\psi),-m\sin(m\psi),-m^2\cos(m\psi),m^3\sin(m\psi)\).
The existing ActualFiniteTailV2.fourier numerical method implements only orders zero through two: its final branch always chooses minus cosine. It must not be called with order three when making the new angular-three-jet tables. This is a restriction of that old numerical evaluator, not an error in its existing six-jet queries. A new interval implementation should use the full derivative cycle directly and retain signed planar frequencies.

## 3. Prefix correction in the same chart and target metric

Let \(C_j(\psi)\), \(j=0,1,2\), be the uncorrected endpoint jets of the same final Cartesian prefix, expressed in the union frequency lists. The complete core-lift endpoint jets must be checked to be literally zero before simplifying \(C_j\) to the finite rep coefficients. The shared phase chart has exact zero two-jet at the cut, so material angle and computational angle, including their relevant seam derivatives, agree there.

With \(D_j=T_j-C_j\), cut width \(L>0\), \(u=(s_e-s)/L\), and the usual left Hermite basis \(h_j\), define

\[
\widetilde X(s,\psi)=X(s,\psi)+
 \sum_{j=0}^2(-L)^j h_j(u)D_j(\psi)
\quad (s_e-L\le s\le s_e),
\]

and keep \(X\) unchanged before the strip. The three \(h_j\) have unit value/first/second left data respectively and zero two-jet at their right endpoint. Consequently the correction's endpoint two-jet is exactly \(D_j\), and its initial two-jet is zero.

For the radial/angle derivative pair \((r,k)\), add

\[
\sum_{j=0}^2(-1)^{j+r}L^{j-r}h_j^{(r)}(u)D_j^{(k)}(\psi).
\]

The radial D2 metric computation needs \(r\le3\), and its angular D2 computation needs \(k\le3\). These are exact fixed coefficient functions; interval coefficient bounds enclose them and never select interval midpoints. Split the radial partition at \(s_e-L\), all original common knots, all frozen target-profile joins, and the separate target-radius patch join \(s_e-1/1000\).

The target remains the same frozen \(ds^2+\widehat a(s)^2d\theta^2\) from R74. It already has the R58 endpoint radius two-jet \((R_c,\alpha,\beta)\). The correction does not create a new target by taking the induced metric of the corrected surface. R74 bounds can be reused on portions \(s\le s_e-L\) after exact defining-data identity and coverage are checked; the new strip requires its own complete metric and geometry bounds.

## 4. Physical radius and saved-radius reparametrization

The saved cut radius \(c\) may differ from \(R_c\). Set \(\varepsilon=c-R_c\) and let \(d\) be the literal input transition width .02. On the physical tail, define

\[
r(R)=R+\varepsilon\,P\!\left(\frac{R-(R_c-d)}d\right),
\qquad P(u)=10u^3-15u^4+6u^5,
\]

using zero before the transition and the endpoint value one at its outer boundary. This gives exactly

\[
r(R_c)=c,\qquad r'(R_c)=1,\qquad r''(R_c)=0.
\]

The sufficient monotonicity check is
\(\lvert\varepsilon\rvert\,15/(8d)<1\).
The exact real formula, rather than a numerical equality branch, establishes these identities.

Only the tail perturbation uses \(V(r(R),\theta)\). The background remains \(R e_r\), its height is the true \(\int_R^{R_c}w\), and its fixed metric is

\[
g_{\rm tail}=(1+w(R)^2)dR^2+R^2d\theta^2.
\]

Its derivatives include
\(V_R=r'V_r\) and \(V_{RR}=(r')^2V_{rr}+r''V_r\).
The R58 arclength seam follows from these exact endpoint identities. Because the background is not composed with \(r\), this is not merely a coordinate change of the entire already-certified saved-radius stage map. A certificate for that old stage map does not automatically certify the near-cut reparametrized tail. That region needs a direct complete evaluation or a rigorous transfer bound. A tail Taylor verifier also needs the corresponding third derivative terms.

## 5. Required identity checks before a new certificate

Bind the actual accepted prefix record and final defining arrays; the complete tail geometry bundle, accepted packet, shared-node index, cut stage and spectrum contract; the unscaled full-H identity and matching state count; and all physical background parameters. Confirm the cut-tail mean is the same coefficient used in the complete cut vector, the prefix/core/chart endpoint zero identities, and the two cut widths as exact input constants. Bind the resulting real-expression target definition and correction data separately from floating evaluator caches.

The prefix cut certificate requires no approximate Background.sample values: at the cut its background height is exactly zero and its first two radius derivatives are the explicit R58 values above. A later whole-tail or cap placement certificate additionally needs the true background primitive and its calibration, the exact deep collar definition, the real cap translation, and the marker's own fixed metric. The existing sampled cache of the background primitive cannot replace those definitions.
