# R133 supplement: five whole maxima for the complete value-tail and inherited radial refinements

2026-11-16, root.

The outer cell primitive can be retained inside the actual adjoint estimate. This yields a complete tail gate from five whole maxima, without the separate product of the largest cell length and the largest unweighted low-to-high dual coefficient. Uniformly refining a fixed partition then reuses the same complete coefficient and composite enclosures.

This is a proof and an executable-target reduction. No new numerical maximum, reference, mesh count, sufficient comparison, or inverse has been evaluated. The failed WHV sufficient test, every successful old record and the actual finite/head/mean obligations remain unchanged.

## WPTVR1. The unchanged operator and the unprojected source primitive

Use exactly WPT and WPTV's ordinary radial space
\[
 \mathscr H=L^2(I_+;E_L),\qquad \dim E_L=193,\qquad
 \widetilde K=S B_{LH}G_H B_{HL}S^{-1}.
 \tag{WPTVR.1}
\]
The physical even constant is part of \(E_L\). The actual high given-head inverse is
\[
 G_H:L^2_rH^{-2/3}_{\phi,H}\longrightarrow L^2_rH^{-1}_{\phi,H}.
 \tag{WPTVR.2}
\]
All its original boundary, transmission, physical mean and source conventions are retained. It is not the coupled physical inverse.

Fix parent cells \(I_i\) of true lengths \(h_i\), with the original collar/body cut and every genuine value/transmission discontinuity at a cell endpoint. Let \(\Pi_i\) be cell averaging and \(Q_i=Id-\Pi_i\). On the full source space define
\[
 V_i f(r)=\int_{\inf I_i}^r f(t)\,dt,\qquad
 T_i=Q_i V_i,\qquad \tau_i=h_i/\pi .
 \tag{WPTVR.3}
\]
The complete Poincare inequality gives
\[
                   \|T_i\|=\|T_i^*\|\le\tau_i .
 \tag{WPTVR.4}
\]
There is no right \(Q_i\) in \(T_i\). Its source can have a nonzero cell mean. Replacing it by the periodic mean-zero primitive would delete the centered-ramp column.

The mean-preserving \(S_i\), symmetric transformed principal \(S_iD_iS_i^{-1}\), and finite reference \(B_i^0\) are constant on a parent cell. Define
\[
 C_i=S_i^{-*}B_i^{0*},\qquad
 E_i=S_i^{-*}(B_{HL}^*-B_i^{0*}).
 \tag{WPTVR.5}
\]
Use complete, same-cell bounds
\[
 \begin{split}
 e_i&\ge\|S_i(A_L-D_i)S_i^{-1}\|,\\
 E_{B,i}&\ge\|E_i\|_{H^{2/3}\to E_L},\\
 C_{A,i}&\ge\|C_iA_{HH}^*\|_{H^{2/3}\to E_L},\\
 C_{B,i}&\ge\|C_iB_{LH}^*S_i^*\|_{E_L\to E_L},\\
 L_i&\ge\|B_{LH}^*S_i^*\|_{E_L\to H^1}.
 \end{split}
 \tag{WPTVR.6}
\]
These retain the complete drift, reaction, ordered primitive, actual principal and all relevant physical mean terms as specified in WPTV. They are not obtained by subtracting unrelated norm upper bounds. Every exact source of \(S_i\) or \(S_i^{-1}\) is present in (WPTVR.6).

A chosen positive rational lower floor for a body reference \(q_i\) is allowed: \(q_i\) is a reference, not a claimed curvature lower bound. All differences \(\eta K-\eta_iq_i^2\) and \(\eta-\eta_i\) must still enter \(e_i\). The root choice \(S_0=Id,D_0=0,B_0^0=0\) requires no positive curvature gap.

## WPTVR2. Keep the true outer adjoint before taking norms

Past-cell Volterra integrals are constant on a receiving cell and are annihilated by its \(Q_i\). Thus the complete feedback part of the tail is
\[
 \mathcal E=QSV_0KS^{-1}Q=T\widetilde KQ,\qquad
 T=\bigoplus_iT_i,\quad Q=\bigoplus_iQ_i .
 \tag{WPTVR.7}
\]
Take any \(\psi\in\mathscr H\), and set
\[
 \theta=T^*\psi,\qquad
 v=B_{LH}^*S^*\theta,\qquad w=G_H^*v .
 \tag{WPTVR.8}
\]
The first estimate is local:
\[
 \|\theta\|_{I_i}\le\tau_i\|\psi\|_{I_i},\qquad
 \|v\|_{L^2H^1}\le L\|\psi\|,\qquad
                  L:=\max_i\tau_iL_i .
 \tag{WPTVR.9}
\]
No multiplier is commuted with \(T^*\); \(v\) is still the actual product in (WPTVR.8).

The same weak adjoint source equation as WPTV gives, within each parent cell,
\[
 -w'=A_{HH}^*w+B_{LH}^*S_i^*\theta,\qquad
 (\widetilde K^*\theta)|_{I_i}=C_iw+E_iw .
 \tag{WPTVR.10}
\]
Although the whole \(w\) need not gain an angular derivative, the finite quantity \(C_iw\) has the required ordinary weak radial derivative. Poincare and (WPTVR.6) therefore give
\[
 \begin{split}
 \|Q_i\widetilde K^*\theta\|_{I_i}
 &\le (E_{B,i}+\tau_iC_{A,i})\|w\|_{I_i,H^{2/3}}
           +\tau_i C_{B,i}\|\theta\|_{I_i}\\
 &\le (E_{B,i}+\tau_iC_{A,i})\|w\|_{I_i,H^{2/3}}
           +\tau_i^2 C_{B,i}\|\psi\|_{I_i}.
 \end{split}
 \tag{WPTVR.11}
\]
The second factor of \(\tau_i\) in the last term comes from the complete \(T_i^*\), not an inserted projection. No derivative of an ordinary input, of \(B_{HL}\), or of a saved upper record is used.

Let \(I_c,I_b\) be the same original collar and body source regions. The original full source columns imply
\[
 \|\mathbf1_{I_j}w\|_{L^2H^{2/3}}\le C_j\|v\|_{L^2H^1},
 \qquad j=c,b .
 \tag{WPTVR.12}
\]
These are source restrictions of the actual adjoint. They do not assume that the two forward output columns are orthogonal.

For a general parent partition define
\[
 E_j=\max_{I_i\subset I_j}E_{B,i},\qquad
 U_j=\max_{I_i\subset I_j}\tau_i C_{A,i},\qquad
 B=\max_i\tau_i^2 C_{B,i}.
 \tag{WPTVR.13}
\]
Minkowski in the direct sum of cells, followed by (WPTVR.9) and (WPTVR.12), proves
\[
 \boxed{\quad
 \|\mathcal E\|\le
 L\sqrt{[C_c(E_c+U_c)]^2+[C_b(E_b+U_b)]^2}+B .
 \quad}
 \tag{WPTVR.14}
\]
Separately taking the maxima in (WPTVR.13) is a complete upper estimate for the same operator. It does not select entries from different references or candidates.

## WPTVR3. The five-maxima root/collar choice

Use \(S=Id,D=0,B^0=0\) throughout the original collar. Then
\[
 e_i=G_c,\qquad E_{B,i}=A_c,\qquad C_{A,i}=C_{B,i}=0
 \quad (I_i\subset I_c)
 \tag{WPTVR.15}
\]
are valid choices using WHV's original complete records \(G_c,A_c\). The same old collar bound for \(L_i\) may be used with its original full shell and units. This does not extend any collar record into the body.

Consequently \(E_c=A_c\) and \(U_c=0\) are read rather than newly computed. Only the following five whole maxima are needed:
\[
 \boxed{\quad
 A=\max_i\tau_i e_i,\qquad E_b,\qquad U_b,\qquad
 L=\max_i\tau_iL_i,\qquad B=\max_i\tau_i^2C_{B,i}.
 \quad}
 \tag{WPTVR.16}
\]
The principal operator \(R_D\) on the radial mean-zero complement still satisfies \(\|R_D^{-1}\|\le1\). Including the full \(A_L-D\) difference, a sufficient gate for the actual tail is
\[
 \delta_1=
 A+L\sqrt{(C_c A_c)^2+[C_b(E_b+U_b)]^2}+B<1.
 \tag{WPTVR.17}
\]
Only a saved outward strict comparison can grant the bound
\(\|R_Q^{-1}\|\le(1-\delta_1)^{-1}\). A false comparison remains a complete outcome and does not prove singularity.

## WPTVR4. Uniform inherited refinements need no new coefficient contraction

Fix a positive integer \(m\) before the scientific invocation. Split every parent cell, including the collar cells, into \(m\) equal cells. Inherit the parent \(S_i,D_i,B_i^0,e_i,E_{B,i},C_{A,i},C_{B,i},L_i\) on each child. Every parent enclosure remains a bound on a child because its whole original domain was covered.

The actual multiplication operator \(S\) and therefore the full transformed operator \(\widetilde F_0\) are unchanged. The projection \(Q_m\), the cell primitive \(T_m\), and the finite mean-coordinate space do change. Child lengths are exactly \(h_i/m\), so the complete estimates become
\[
 A_m\le A/m,\qquad L_m\le L/m,\qquad
 U_{b,m}\le U_b/m,\qquad B_m\le B/m^2,\qquad E_{b,m}\le E_b.
 \tag{WPTVR.18}
\]
Apply the proof of (WPTVR.14) to the child cells. For the collar choice in (WPTVR.15),
\[
 \boxed{\quad
 \delta_m=
 \frac A m+\frac L m
 \sqrt{(C_c A_c)^2+
       \left[C_b\left(E_b+\frac{U_b}{m}\right)\right]^2}
       +\frac B{m^2}
 \quad}
 \tag{WPTVR.19}
\]
is a complete sufficient upper bound for
\(\|R_{D,m}-Q_m\widetilde F_0Q_m\|\). The five saved parent maxima and the unchanged old source columns determine this whole candidate.

All physical endpoints remain the same. If a collar starts at the true root \(r_*\), its refined endpoints are defined by the actual affine subdivision of that interval. Numerical length bounds must use the original complete root enclosure. This does not replace the true root by an enclosure endpoint, and any future signed finite pairing still must enclose the actual endpoint.

Refinement neither removes genuine discontinuities nor converts old coefficient subdivisions into impulses. Changes of \(S\) and every true transmission jump remain projection endpoints. Every actual affine jump, initial coordinate and independent source stays in the original right side.

Different \(m\)'s define different complete tail and finite Schur decompositions. A later choice must select one whole candidate, keep its own full signed finite core, and retain all four WPT.31 blocks and both right sides. A finite-dimensional allocation is not authorized merely because a tail gate is true. If the original prescribed-root problem has \(193N+193\) scalar coordinates on \(N\) cells, the uniformly refined realization has \(193mN+193\); this is only a dimension formula.

## WPTVR5. Small-output execution and remaining obligations

A subsequent manifest must fix the exact parent partition recipe, reference rule, complete set of \(m\)'s, parent/refined cell caps, memory and runtime caps, and all input identities before evaluation. An observed false comparison cannot enlarge that set or allocate a larger finite matrix.

Complete temporary coefficient and finite-composite enclosures can be reduced to the five whole maxima in (WPTVR.16). Their original qualifications, complete coverage counts and full maximizing witnesses must be saved. The mathematical output is the whole maxima and each complete scalar gate, not a public cell-array or matrix certificate. After each fully processed parent cell, preserve the complete running maxima, witness data and exact processed-prefix identity atomically, so a later continuation can identify precisely what remains.

No old maximum, Green propagation, repair sequence, response trial, successful Fourier envelope or already completed scientific target is recomputed. Restoring the original data is a byte-identity operation in the public repository's own Actions. All new scientific arithmetic also belongs there.

This result pays no genuine signed finite inverse, physical 96-column normalization, cokernel compatibility, negative radial head, parameter/mean Schur system, high graph constraint, background exactness or nonlinear matching. The physical even mean is retained both as a head input and in the complete \(A_L-D\) remainder. The complete outer mean row and all independent ports remain exactly as in WPT and WPTV.

## Immutable primary text

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WPT, cellwise principal inverses and complete dual tail | b37c59bc05a2131b27014f37c1a6555d6f7e2c58 | 22954 | 22fb6fac312540818390bea1bb3a3ed2c750f515ad91bbbb1b0790fcdfe1fd6e |
| WPTV, complete value-only cross-block certificate | ddccd14e855ba95048fe92cbd21edfb82ebd8e6f | 21178 | dda500b8f5e2d02a39fbef4efcc5c2ad10dac93eef194f6e8d5b9b5a816cd0e9 |
| WPTV complete input inventory | 18ec6014b06315aaf24cf9068e6fa31e05e6025a | 38086 | f7dd2ed019b30c076aa70ad1536601813095ef59bb504049d976eb0cd93b1547 |
| Actual frozen WHV scalar conclusion | ebe7ae42c2482ce9b20e7af1d41e02f89b920010 | 12011 | ff5d6e5231e6be66107217d670133b18727dd5b24b81e7566fa884973b29df72 |

The first three complete texts were read by root. The exact adjoint identity and both original source-column types are WPT.13--18 and WPTV.10--16. WPTV.17--20 retains the unprojected outer primitive. The new conclusion here keeps that primitive's adjoint in place and makes the inherited-refinement reduction explicit. No new numerical result is asserted.
