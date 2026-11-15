# R133: complete directional matrix Green bounds with true boundary and interface defects

This contract concerns the fixed complete finite193 BVP on $[0,L]$, $L=9/10$, at the same fixed physical $\eta_0$, original $\nu$ and repaired M32 centre as the immutable reference profile. The state consists of all 96 reflected odd modes and all 97 reflected even modes, including the independent even mean. It does not supply the negative high BVP inverse, an infinite head/high Schur inverse, a changed-background transfer, or the true parameter response.

The inputs are the complete 5970 same-forward-polynomial matrix cover, its four original successful cells, the true weighted 96/97 endpoint certificate, the complete ordinary $L^2$ Green kernel, and all 5970 actual individual interface gains. The producer binds their complete source, native and process identities. All new arithmetic runs in the public repository's Actions. No old target, original projector, forward polynomial, source/output Gram, or positive Green port is recalculated.

## G.1. One local fundamental matrix and two complete source channels

In each original cell $I_i=[r_i,r_{i+1}]$ use the already certified exact matrix polynomial $\widehat F_i(t)$ and complete exact frame $S_i$. Their full 193 rows, same-$\widehat F_i$ inverse enclosure, true generator discrepancy, and signed source/output Grams are retained. Put $\Psi_i(t)=\widehat F_i(t)S_i$. The physical state is $h=R^{-1}y$, where $R=\operatorname{diag}(I_{96},\rho I_{97})$ is the original continuous positive radial weight.

The first source channel is the complete saved 193-by-128 reference for $R A_{LH}$. The second is the artificial edge source $E_i P_{\rm edge}$, with the recorded complete uniform discrepancy $E_i$ and the 128 edge coordinates corresponding to low modes 33 through 96 in both reflected components. The exact low body cross block reads high modes 97 through 160; all higher input modes vanish under this fixed M32 cross projection.

For the second channel, the existing unit-edge source Gram is multiplied by $E_i^2$. Indeed a true omitted source matrix $D_i(r)$ with $\|D_i(r)\|\le E_i$ and that edge output support satisfies

$$
D_i(r)D_i(r)^*\preceq E_i^2P_{\rm edge}.
\tag{G.1}
$$

The two channel responses are combined only by an operator triangle inequality at the end. They are not independent copies of the original high input. This construction includes the complete model, Fourier, scalar and rounding error already recorded in $E_i$, including the original four cells' chosen reference error.

## G.2. Exact coordinate changes at shared nodes

The selected upper triangular map in one cell is

$$
T_i=\begin{pmatrix}A_i&B_i\\0&D_i\end{pmatrix},
\qquad
\widehat F_i(1)S_i=S_i^+T_i .
\tag{G.2}
$$

At an internal node the next cell may have a different complete complement. Its original first 96 columns $Q$ must be exactly the same bytes, and its physical $R$ weight must be exactly the same rational value. The complete frames have true verified inverses. Therefore

$$
C_i=S_{i+1}^{-1}S_i^+
 =\begin{pmatrix}I&B_i^c\\0&D_i^c\end{pmatrix}.
\tag{G.3}
$$

The new consumer verifies these original byte and weight equalities and the inverse identity. The first block column in (G.3) is an exact algebraic identity, not a claim that independent QR complements reproduce the same bytes.

Combine this coordinate event with the preceding cell:

$$
T_i^{\rm eff}=C_iT_i
 =\begin{pmatrix}
 A_i&B_i+B_i^cD_i\\
 0&D_i^cD_i
 \end{pmatrix}.
\tag{G.4}
$$

Write $B_i^{\rm eff}$ and $D_i^{\rm eff}$ for its upper-right and lower-right blocks. Every complete $D_i^{\rm eff}$ inverse is verified. The local source integral and its full Gram are unchanged, since (G.3) changes only the coordinates at the right endpoint. At the true cut $C_i=I$. A shared-$Q,R$ coordinate change creates no physical jump.

## G.3. Past and future source coordinates

For one source channel let

$$
\eta_i=\int_{I_i}S_i^{-1}\widehat F_i(r)^{-1}B_i^{\rm source}(r)f(r)\,dr
       =(\eta_{p,i},\eta_{q,i}).
\tag{G.5}
$$

The saved signed 193-by-193 matrix $H_i$ is a Loewner upper bound for its complete source covariance. With terminal proposal $q_N=0$, define a chosen graph $V_i$ by $p_i=V_iq_i+w_i$. Here $w_i$ depends only on forcing strictly to the left, and $q_i$ depends only on forcing at and to the right. The exact local relations are

$$
\begin{aligned}
q_i&=(D_i^{\rm eff})^{-1}q_{i+1}-\eta_{q,i},\\
w_{i+1}&=A_iw_i+A_i[I,-V_i]\eta_i,\\
V_{i+1}^{\rm ex}&=(A_iV_i+B_i^{\rm eff})(D_i^{\rm eff})^{-1}.
\end{aligned}
\tag{G.6}
$$

The cancellation of the $B_i^{\rm eff}\eta_{q,i}$ term in the second relation is exact. It does not permit dropping the signed $p/q$ source covariance.

Let $Q_i$ denote the future covariance upper bound, and $W_i$ the past covariance upper bound. Disjoint radial input supports give the two sweeps

$$
\begin{aligned}
Q_i&\succeq(D_i^{\rm eff})^{-1}Q_{i+1}(D_i^{\rm eff})^{-*}+H_{qq,i},
&Q_N&=0,\\
H_{w,i}&=[I,-V_i]H_i[I,-V_i]^*,\\
W_{i+1}&\succeq A_i(W_i+H_{w,i})A_i^*,
&W_0&=0 .
\end{aligned}
\tag{G.7}
$$

Every off-diagonal entry is kept signed before the complete matrix or quadratic form is enclosed. No entrywise absolute-value covariance replaces (G.7).

The numerical covariance storage is an exact symmetric sum of two dyadic matrices plus a verified nonnegative dyadic scalar times the identity. The scalar dominates the entire signed matrix enclosure error in operator norm. Thus every stored matrix is a valid Loewner upper bound. Its mean coordinate is retained.

## G.4. The chosen graph and its real jumps

Each $V_i$ is defined as the exact sum of two saved binary64 matrices. The addition is performed in exact/Arb arithmetic, never as a binary64 sum. No fixed number of accurate bits is assumed; the actual full matrix discrepancy is enclosed.

If $V_{i+1}$ differs from $V_{i+1}^{\rm ex}$, the resulting physical weighted-state jump is

$$
j_i=Q_{i+1}^{\rm anchor}
       (V_{i+1}-V_{i+1}^{\rm ex})q_{i+1}.
\tag{G.8}
$$

This is a real model defect, not a free coordinate change. Its complete Hilbert--Schmidt bound uses the full future covariance $Q_{i+1}$ and the actual Gram of the saved anchor, with no orthonormality assumption on its floating-point columns.

At $L$, the proposal has exact $q_N=0$. Consequently its terminal graph selection creates no jump, and no new fictitious interface is inserted at $L$.

At the waist the chosen $V_0$ approximates $-(UQ_0)^{-1}UN_0$, where $U$ is the actual restriction to all 96 odd rows. Its true defect $UQ_0V_0+UN_0$ is evaluated against the entire 97-coordinate initial future covariance. It is paid separately with the original left-boundary response column.

## G.5. Complete output covariance inside each cell

Put $E_p=(I,0)^T$ and $\mathcal L_i=(V_i,I)^T$. At an interior point, direct substitution of (G.6) gives

$$
y(r)=\Psi_i(r)\left[
 E_pw_i+\mathcal L_i(D_i^{\rm eff})^{-1}q_{i+1}
 +P_{p,i}\eta_i(r_i,r)-P_{q,i}\eta_i(r,r_{i+1})\right],
\tag{G.9}
$$

where

$$
P_{p,i}=E_p[I,-V_i],
\qquad
P_{q,i}=\mathcal L_i[0,I].
\tag{G.10}
$$

The four source supports in (G.9) are genuinely disjoint: strict past, strict future, the current left subinterval and the current right subinterval. Each partial current-cell covariance is separately dominated by the existing full $H_i$. Therefore a constant complete covariance majorant is

$$
\mathcal C_i=
 E_p(W_i+H_{w,i})E_p^*+\mathcal L_iQ_i\mathcal L_i^* .
\tag{G.11}
$$

Using $H_i$ twice in this upper bound does not declare two full-cell copies of the same source independent. Independence was used only for the two actual disjoint partial intervals, before replacing each by its valid full-cell upper bound.

For any saved complete output Gram $J_i$, (G.11) gives

$$
\operatorname{tr}(J_i\mathcal C_i)
 =
 \operatorname{tr}(J_{pp,i}(W_i+H_{w,i}))
 +\operatorname{tr}(\mathcal L_i^*J_i\mathcal L_i\,Q_i).
\tag{G.12}
$$

The consumer retains both terms and all signs. The saved Grams already pay true radial measure exactly once. They separately cover the whole physical inner interval, the complete fixed safe negative phase interval, and the weighted state. The one cell meeting the fixed negative endpoint uses its saved partial output Gram.

## G.6. Whole-body operator defects in the ordinary source norm

Let $\delta_i$ be the recorded complete weighted-generator discrepancy between the true finite193 operator and $\widehat F_i'\widehat F_i^{-1}$. On $I_i$ the ordinary physical residual of the proposal is bounded by

$$
\|R^{-1}(A_{\rm true}-A_{\widehat F})y\|
 \le \max(1,\rho_{i,\min}^{-1})\delta_i\|y\|.
\tag{G.13}
$$

Thus its ordinary $L^2$ Hilbert--Schmidt square is bounded by the sum of the saved weighted output traces from (G.12), multiplied by
$\max(1,\rho_{i,\min}^{-1})^2\delta_i^2$.
This sum always runs over the entire inner BVP. Restricting the requested output to the negative interval does not remove positive-side operator defects.

All 5970 exact cells, all matrix source columns, and the independent even mean are retained. The original complete model fee and the endpoint patch fee are paid exactly as certified; no new coefficient midpoint is substituted.

## G.7. The true 97-row regular boundary

The nominal complete weighted boundary is

$$
\widehat B_R=
\begin{pmatrix}I_{96}&J/\rho_L\\0&M/\rho_L\end{pmatrix},
\tag{G.14}
$$

where $J$ is the exact saved 96-by-97 dyadic matrix and $M$ is the complete independent mean row. The original full boundary theorem bounds the true error only on the even97 input columns:

$$
\|(B_R-\widehat B_R)y\|\le E_R\|y_{\rm even}\|.
\tag{G.15}
$$

At the proposal cut, $y_L=Q_{\rm cut}^{\rm anchor}w_N$. With full cut covariance $W_N$, the true boundary defect is bounded by the sum

$$
\begin{aligned}
&\sqrt{\operatorname{tr}\!\left[
 (\widehat B_RQ_{\rm cut})^*(\widehat B_RQ_{\rm cut})W_N\right]}\\
&\quad+
 E_R\sqrt{\operatorname{tr}\!\left[
 Q_{{\rm cut},{\rm even}}^*Q_{{\rm cut},{\rm even}}W_N\right]} .
\end{aligned}
\tag{G.16}
$$

This retains direction and correlation. It does not apply a finite97 input estimate to an arbitrary external high input. The full infinite cap high-trace column remains a separate input in the coupled problem.

## G.8. Posterior correction by the already proved true inverse

Let $K$ be one of the two piecewise matrix proposal kernels. For the complete original finite BVP operator $\mathcal D$, its exact posterior identity is

$$
G_LB=K-G_L\bigl((\partial_r-A_{\rm true})K-B,\,
                         B_0K,\,B_RK,\,\{[K]_i\}\bigr).
\tag{G.17}
$$

No new Neumann argument is needed for this identity. The body term uses the original actual ordinary $L^2$-source Green norm. Left and right defects use their distinct actual boundary response columns. Every interface uses its own actual weighted-state impulse gain.

For multiple graph-rounding jumps acting on the same source, the consumer uses
$\sum_i g_i\|j_i\|_{\rm HS}$.
It does not add their squares as if different interface responses were orthogonal.

The reference-channel and source-error-channel posterior norms are finally added. Hilbert--Schmidt bounds dominate the corresponding operators on arbitrary radial $L^2$ input functions; the calculation is not limited to 128 fixed radial forcing profiles.

## G.9. A separate true cut trace

The proposal cut covariance retains all 96 incoming directions. Its ordinary trace uses the full physical metric, including all 97 even states.

For the posterior correction, the ordinary source-to-cut gain is taken from the original L2 kernel's actual final-node two-row Gram and the exact cut metric. The two boundary-to-cut gains use the actual last forward $p$ values and

$$
q_L\le D_Lp_L+L_R\|g_R\|.
\tag{G.18}
$$

For one interface jump with zero external right source, its already paid
$p_{\rm after}$ includes the interface's own $b$ factor. Propagation through all events strictly outside that interface gives

$$
g_i^{\rm cut}\le
 \max(1,\rho_L^{-1})\sqrt{1+D_L^2}\,
 p_{{\rm after},i}\prod_{\text{events strictly outside }i}b .
\tag{G.19}
$$

This is a new scalar product of the original signed positive port bounds; no exponential or old port is reevaluated. It is not obtained by treating an entire-body $L^2$ bound as a trace. The zero-right-source premise in (G.19) applies to this individual jump response, not to a general boundary load.

## G.10. Provenance, recovery and limits

The covariance sweeps preserve the exact original interval order, original shared $Q$ bytes and rational $R$ values. Every chosen graph and covariance matrix is saved with its actual public run, attempt, artifact, shape and byte SHA. Complete row proofs are written in bounded native chunks; a resumed successful prefix reuses those rows and arrays by their original identities. A mathematical success followed by a publication failure remains reusable only through its exact successful native and process chain.

A successful new consumer proves direction-preserving bounds for the same complete finite193 BVP's body cross response and its cut trace. It does not close the full infinite BVP: the negative high inverse, full head/high feedback including the independent cap high trace, the nonzero-$\delta$ transfer, and the nonlinear background and parameter obligations remain separate.
