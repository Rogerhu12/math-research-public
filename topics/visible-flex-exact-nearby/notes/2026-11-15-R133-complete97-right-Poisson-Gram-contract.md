# R133: complete 97-input right Poisson Grams from the same finite193 matrix BVP

This is a consumer contract for the same fixed repaired M32 centre, physical $\eta_0$, original $\nu$, and complete finite193 BVP on $[0,L]$, $L=9/10$. It supplies a direction-preserving interface for the full 97-component right boundary load, including the independent even mean. It is not an infinite high inverse, a nonzero-$\delta$ transfer, or a claim that the numerical gates have already passed.

The inputs are the complete 5970 same-$F$ local matrix cover, the actual complete direction-preserving covariance sweep and its saved dyadic graphs, the full true weighted 96/97 boundary certificate, and the original true finite193 Green/kernel/interface certificates. Their full identities and actual successful processes must be checked before numerical use. No target, local $F$ or $C$ polynomial, source/output Gram, or old scalar Green port is recalculated.

## P.1. Boundary input units and exact local coordinates

The complete weighted state is $y=Rh$, where
$R=\operatorname{diag}(I_{96},\rho I_{97})$ is the original positive continuous radial weight. The true boundary problem is

$$
\mathcal D h=(f,g_0,g_R),\qquad
g_0\in\mathbb R^{96},\quad g_R\in\mathbb R^{97}.
\tag{P.1}
$$

The norm of $g_R$ is exactly the original complete boundary-row Euclidean norm. It is not multiplied by $\rho$ a second time. The last coordinate is the independent mean row.

In an original cell let $\Psi_i(r)=\widehat F_i(r)S_i$ and retain the exact already certified effective triangular map

$$
T_i^{\rm eff}=
\begin{pmatrix}A_i&B_i^{\rm eff}\\0&D_i^{\rm eff}\end{pmatrix}.
\tag{P.2}
$$

The effective map includes the exact shared-node coordinate change between complete complements. The common 96-column anchor $Q$ and the physical weight $R$ are identical at that node. Consequently this coordinate change itself is not a physical jump.

Use the actual saved graph $V_i$ at the left endpoint of every cell and write
$\mathcal L_i=(V_i,I_{97})^T$. The graph consists of the exact sum of the two saved dyadic matrices. Its independent rounding is not discarded.

There is no ordinary body source in the proposed Poisson family. Hence the strict-past coordinate is zero, and

$$
q_i=(D_i^{\rm eff})^{-1}q_{i+1},\qquad
y(r)=\Psi_i(r)\mathcal L_iq_i .
\tag{P.3}
$$

All 193 state coordinates and all 97 future coordinates remain present.

## P.2. The true terminal trace uses the unrounded endpoint graph

The previous body-cross proposal used $q_N=0$. That fact made its independently selected final $V_N$ harmless at the cut. It cannot be reused for nonzero boundary data without a fee.

For the new Poisson family use instead the exact endpoint expression of the last cell,

$$
V_{\rm cut}^{\rm ex}
 =(A_{\rm last}V_{\rm last}+B_{\rm last}^{\rm eff})
   (D_{\rm last}^{\rm eff})^{-1},\qquad
\Lambda_{\rm cut}=
\begin{pmatrix}V_{\rm cut}^{\rm ex}\\I_{97}\end{pmatrix}.
\tag{P.4}
$$

Here “exact” refers to the canonical expression in the already saved exact matrices and true inverse. Arb arithmetic encloses this expression. No independent endpoint selection is inserted into the physical trace.

Let $S_{\rm cut}$ be the saved complete frame and let $\widehat B_R$ be the exact nominal weighted boundary matrix

$$
\widehat B_R=
\begin{pmatrix}I_{96}&J/\rho_L\\0&M/\rho_L\end{pmatrix}.
\tag{P.5}
$$

The 96-by-97 matrix $J$ and complete 97-component row $M$ are the original saved dyadics. Define
$P=\widehat B_RS_{\rm cut}\Lambda_{\rm cut}$.
A true inverse enclosure of this full 97-by-97 matrix is required. Choose a new exact dyadic matrix
$C=\operatorname{exact}(C_{\rm hi})+\operatorname{exact}(C_{\rm lo})$
from that enclosure. Its actual residual $PC-I_{97}$ is retained. Neither a chosen midpoint nor a small residual is declared to be the exact true boundary inverse.

For a boundary input $g$, set

$$
q_N=Cg,\qquad
E_N=C,\qquad E_i=(D_i^{\rm eff})^{-1}E_{i+1}.
\tag{P.6}
$$

The exact proposed physical Poisson map in a cell is

$$
K_R(r)g=R(r)^{-1}\Psi_i(r)\mathcal L_iE_i g.
\tag{P.7}
$$

At the cut its trace is
$R_L^{-1}S_{\rm cut}\Lambda_{\rm cut}Cg$.
The nominal inverse in (P.5) is only a construction device. The posterior proof below does not require a new Neumann closure for the whole BVP.

## P.3. Enclosing the products does not introduce new state jumps

The exact matrices $E_i$ in (P.6) are canonical products. A numerical checkpoint may enclose them by an exact dyadic matrix $\widehat E_i$ and a nonnegative scalar $e_i$ such that

$$
\|E_i-\widehat E_i\|\le e_i .
\tag{P.8}
$$

This is an enclosure of the same exact product, not a new choice of the state. It therefore causes no additional physical jump.

If $\widehat E_{i+1}$ and $e_{i+1}$ are known, a new dyadic enclosure obeys

$$
e_i\le
 \|(D_i^{\rm eff})^{-1}\|e_{i+1}
 +\|(D_i^{\rm eff})^{-1}\widehat E_{i+1}-\widehat E_i\|.
\tag{P.9}
$$

The second term includes the full directed arithmetic and storage difference. Both dyadic matrices are added in exact arithmetic, not in binary64.

For any fixed positive semidefinite matrix $J$, (P.8) gives the useful full-matrix estimate

$$
E_i^*JE_i\preceq
 \widehat E_i^*J\widehat E_i+
 \|J\|\bigl(2\|\widehat E_i\|e_i+e_i^2\bigr)I_{97}.
\tag{P.10}
$$

The signed product is evaluated before adding this scalar slack. A further full signed-matrix arithmetic enclosure is stored as two exact symmetric dyadics plus a verified nonnegative diagonal slack, exactly as in the complete directional Green consumer.

An actual empty interval, failed inverse, nonfinite product, or failed enclosure must remain a failed prefix. It is not repaired by changing the exact input, expected hash, or mathematical definition.

## P.4. Full input Grams for the proposed solution

Let $J_{i,Y}$ denote the original complete output Gram for an output region $Y$: the whole inner body, the exact fixed negative phase window, or the full weighted output used for residual fees. Its true radial measure and the original physical $R^{-1}$ factors are already included exactly once.

Define

$$
H_{K,Y}\succeq
 \sum_i E_i^*\mathcal L_i^*J_{i,Y}\mathcal L_iE_i .
\tag{P.11}
$$

All off-diagonal entries remain signed. The sum is a 97-by-97 positive Gram on the single boundary input $g$; it is not a sum of independent boundary copies. Thus

$$
\|K_Rg\|_Y^2\le g^*H_{K,Y}g .
\tag{P.12}
$$

For the cut output, replace (P.11) by the exact terminal matrix Gram

$$
H_{K,{\rm cut}}\succeq
 C^*\Lambda_{\rm cut}^*S_{\rm cut}^*
 R_L^{-*}R_L^{-1}
 S_{\rm cut}\Lambda_{\rm cut}C .
\tag{P.13}
$$

This is a true trace estimate. A whole-body $L^2$ norm is never substituted for it.

## P.5. The complete ordinary body defect

Let $\delta A_i$ be the actual complete uniform difference between the true weighted generator and the same patched-$F$ generator, as certified in the original matrix row. Put
$m_i=\max(1,\rho_{i,\min}^{-1})$.
The ordinary body residual of (P.7) has the complete 97-input Gram majorant

$$
H_{\rm body}\succeq
 \sum_i(\delta A_i m_i)^2
 E_i^*\mathcal L_i^*J_{i,{\rm weighted}}\mathcal L_iE_i .
\tag{P.14}
$$

This sum is over all 5970 cells in $[0,L]$, even when the requested output is restricted to the negative phase window. Positive-side coefficient and endpoint-patch errors are not omitted.

The complete generator discrepancy includes the old exact-reference error and the actual endpoint patch fee. No new coefficient midpoint is substituted, and no physical scalar-source or divergence fee is silently replaced by a finite matrix approximation.

## P.6. Waist, regular boundary and true graph jumps

Let $U$ be the restriction to the 96 physical odd coordinates at the waist. Its true defect is the full matrix

$$
D_0=US_0\mathcal L_0E_0,\qquad
H_0\succeq D_0^*D_0 .
\tag{P.15}
$$

The independent even mean is in $E_0$ and $\mathcal L_0$ throughout. The original true left-boundary response column pays this defect.

The original full weighted boundary certificate gives

$$
\|(B_R-\widehat B_R)y\|\le \varepsilon_R\|y_{\rm even}\|.
\tag{P.16}
$$

Set

$$
N=PC-I_{97},\qquad
V_{\rm even}=\Pi_{\rm even}S_{\rm cut}\Lambda_{\rm cut}C .
\tag{P.17}
$$

For any positive constants $a,b$, the full true 97-row right defect has the positive Gram majorant

$$
H_R^{\rm def}\succeq
 (a+b)\left(\frac{N^*N}{a}
        +\frac{\varepsilon_R^2V_{\rm even}^*V_{\rm even}}{b}\right).
\tag{P.18}
$$

A term proved exactly zero can be omitted instead of dividing by a zero weight. The true mean row is included in (P.16)–(P.18), and only the complete even97 columns receive the boundary-error fee.

At an internal node use the exact graph difference

$$
\Delta V_i=
 V_{i+1}-(A_iV_i+B_i^{\rm eff})(D_i^{\rm eff})^{-1}.
\tag{P.19}
$$

Its real weighted-state jump is

$$
J_i g=Q_{i+1}^{\rm anchor}\Delta V_iE_{i+1}g,\qquad
H_i^{\rm jump}\succeq J_i^*J_i .
\tag{P.20}
$$

The actual anchor Gram is retained; its floating-point columns are not assumed exactly orthonormal. Product enclosures such as (P.8) are charged to the matrix bound in (P.20), not mislabelled as extra state jumps.

There is no new cut jump, because (P.4) uses the actual last-cell expression. The waist boundary defect (P.15) is separate. The original Green proof's virtual waist projector event is not inserted a second time into this physical proposal.

## P.7. Matrix-valued posterior correction

Let $G_R$ denote the true right Poisson operator of the already proved complete finite193 BVP. The exact identity is

$$
G_R=K_R-
 G_L\bigl((\partial_r-A_{\rm true})K_R,\,
              B_0K_R,\,
              B_RK_R-I_{97},\,
              \{[K_R]_i\}\bigr).
\tag{P.21}
$$

For each output $Y$, use the original actual constants
$g_{{\rm body},Y}$, $g_{0,Y}$, $g_{R,Y}$ and $g_{i,Y}$ for ordinary body source, left boundary, right boundary and the individual weighted-state jump. For the cut output these are the separately proved actual point-kernel and trace columns, not an $L^2$-to-trace inference.

The positive matrices

$$
\begin{aligned}
M_{K,Y}&=H_{K,Y},\\
M_{{\rm body},Y}&=g_{{\rm body},Y}^2H_{\rm body},\\
M_{0,Y}&=g_{0,Y}^2H_0,\qquad
M_{R,Y}=g_{R,Y}^2H_R^{\rm def},\\
M_{i,Y}&=g_{i,Y}^2H_i^{\rm jump}
\end{aligned}
\tag{P.22}
$$

bound the squared norm of each corresponding output contribution on every fixed input $g$. Therefore, for arbitrary strictly positive weights $\alpha_\ell$ on the nonzero terms,

$$
G_R^*G_R\preceq
 H_Y^{\rm true}:=
 \left(\sum_\ell\alpha_\ell\right)
 \sum_\ell\frac{M_{\ell,Y}}{\alpha_\ell}.
\tag{P.23}
$$

The adjoint in (P.23) is between the exact boundary Euclidean space and the indicated output Hilbert space. It is not an assertion that the cap Dirichlet-to-Neumann map is self-adjoint.

Equation (P.23) is weighted Cauchy–Schwarz applied to the triangle inequality for the actual output vectors. In particular, all graph jumps act on the same $g$ and are not declared orthogonal. Their covariance matrices remain signed before positive accumulation.

Weights may be selected from verified bounds on $\sqrt{\|M_{\ell,Y}\|}$. Each selected weight is a recorded exact positive number. A computed upper bound is never used as a negative coefficient or as an unknown lower bound. Matrix accumulation and the positive total weight are rounded outward.

A separate posterior-error Gram may omit the proposal term. Retaining both this Gram and $H_{K,Y}$ permits later consumers to combine known directions more tightly while keeping the same true error.

## P.8. The all-frequency cap interface remains separate

Suppose an independently proved cap operator $C_H$ sends a genuine full high trace to the complete 97-component low boundary load in exactly the units of (P.1). Then (P.23) gives

$$
\|G_R C_Hu_H\|_Y^2
 \le \langle C_H^*H_Y^{\rm true}C_Hu_H,u_H\rangle .
\tag{P.24}
$$

This is the intended interface. The matrix certificate keeps all 97 input directions, so a future cap consumer can exploit its actual frequency structure or weighted trace bounds.

The present contract does not construct $C_H$, set it to zero, infer it from a finite97-input cap matrix, or replace the high trace by a whole-body $L^2$ high norm. The full cap's independent mean and high-output obligations remain separate. A finite193 Poisson Gram does not supply the missing negative high inverse or complete low/high Schur closure.

## P.9. Provenance and failure recovery

The producer must verify the complete matrix cover and directional-sweep identities before reusing a saved graph. Every actual old graph, source/output Gram, endpoint frame, true boundary certificate, original ordinary kernel and individual impulse gain remains unchanged.

All new products, matrix residuals, positive weights and positive Gram bounds are stored with exact public run/attempt identities and directed error receipts. A completed prefix is reused by its full original identities, including success that preceded a later publication failure. New arithmetic is confined to public Actions; native matrix arrays are never transmitted through a text-only connector.

This contract establishes the algebra of a possible consumer. Numerical invertibility, finite enclosures, complete coverage, positive weights, actual output bounds and their scope require the corresponding real public run.
