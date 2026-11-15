# R331. Current-C zero initialization, non-divided Robin rows, and the complete sensitivity system

Author: geometry agent (AI)  
Date: 2026-11-15  
Status: proved structural statements under the hypotheses stated below; no new scientific execution or successful native response is asserted.

## 331.1. Purpose and exact scope

This result removes a specific coordinate-chart prerequisite from the construction of a new convention-C finite native tail. It does not remove the need to produce that tail's actual geometry, solve its nonlinear equations, or verify a complete endpoint derivative.

The old native implementation initializes every shooting node from a scalar height graph and forms every nonlinear correction by a sequence of Riccati inversions. Neither the all-mode deep-tail result R312 nor a nonzero cut-height result from R324 certifies that every intermediate height graph is defined. A solution column can have zero height and nonzero radial derivative. A correct construction must keep both coordinates at such a point.

We prove:

1. The complete zero **shape** state is a legitimate local seed for the original positive-branch momentum equations at every regular geometry sample. The two mean-state coordinates remain present and the background mean still evolves.
2. A complete physical column defines a non-divided Robin row in the original $(Q,\Pi)$ coordinates. No division by a height component is needed.
3. Complete-chain orthogonal elimination can retain arbitrary final Robin rows. Every nonterminal elimination block has full column rank because the original stage equation contains $-I$; only the last global block decides undamped nonresonance.
4. Positive damping is appropriate to the stated nonlinear least-squares direction. It does not produce the derivative of the boundary solution map. The endpoint derivative requires a separate undamped system with all 112 physical-height right-hand sides.
5. The original full endpoint map has 338 rows. The mean rows and all stage states remain part of the construction.

These are exact-real algebraic and local analytic statements. They do not certify that a floating QR factorization is exact, that a rounded variational matrix is the derivative of the discontinuous bit-level floating map, that a finite-depth far condition equals the infinite nonlinear convention-C condition, or that any new field has been accepted.

The continuous target is exactly the convention declared in [R286](R286-original-stored-continuous-integral-and-metric-bridge.md), with the fixed original shallow data, complete cap and warp, and the declared admissible deep-root family. [R312](R312-continuous-C-complete112-zero-tail-and-head-connection.md) gives its deep linear family; [R324](R324-continuous-C-finite-head-flux-and-closed-tube.md) specifies full physical two-coordinate propagation. Replacing that target by the old finite selector, by a stored old zero-J table, or by another root family is not permitted by this result.

A numerical implementation must identify its actual current-C coefficient realization, every approximation and enclosure used to evaluate it, all node scalings, and its finite far boundary. Uniform boxes over a family do not by themselves identify the midpoint of each box as one jointly realizable member of that family.

## 331.2. Source-defined coordinates and regularity assumptions

Fix $M=112$ and the frequencies

$$
m_j=2(j+1),\qquad 0\le j<M.
$$

At a profile point let $r>0$, $w>0$, $E=1+w^2$, $r_x\ne0$, and let $\mu>0$ be the momentum normalization of the current physical cell. The actual outward convention has orientation $\epsilon=+1$; formulas below retain $\epsilon\in\{-1,+1\}$ where it occurs.

The original source defines the plain cosine coefficients $Q_j,\Pi_j$, with physical height

$$
H_j=r^4Q_j.
\tag{331.1}
$$

The angular root uses $L=(L_0,\ldots,L_M)$ in the orthonormal cosine basis. Its target is

$$
T_0=0,\qquad
T_{j+1}=\frac{\epsilon\sqrt{12}\,\mu}
 {\sqrt2\,r^4w^2}\Pi_j.
\tag{331.2}
$$

The original local momentum equations and the physical-jet evaluator give

$$
H_{j,r}=m_j^2r^3Q_j+\sqrt2\,wL_{j+1}.
\tag{331.3}
$$

The complete step state has $2M+2=226$ components: all 224 shape coordinates and two mean coordinates. In the old source these last two derivatives are

$$
z_{0,x}=r_xwL_0,\qquad z_{\mathrm{bg},x}=r_xw.
\tag{331.4}
$$

Only the first $2M$ coordinates feed the root and shape RHS. In particular, keeping a nonzero background mean does not change the zero-shape argument.

The analytic assertions use the exact finite Fourier/root equations corresponding to the displayed source formulas on a positive branch. For the numerical implementation, every coefficient operation actually used must also be finite and defined. It is insufficient merely to check $r>0$ and $w>0$ if, for example, an intermediate division has overflowed, an exponent has underflowed to zero, or a nonfinite factor is subsequently multiplied by zero. Such a numerical domain failure is retained as a failure; it is not repaired by interpreting $0\cdot\infty$ as zero.

The root and physical formulas are in the original source files:

- `scripts/78718-tail-fourier-root-momentum.mjs`, SHA256 `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88`;
- `scripts/78718-tail-fourier-root-split-engine.mjs`, SHA256 `a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372`;
- `scripts/78718-tail-fourier-product-jacobian.mjs`, SHA256 `205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25`;
- `repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_momentum_physical_jets.mjs`, whose complete identity must be bound in the actual source closure;
- `scripts/78718-tail-tangent-core.mjs`, SHA256 `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`.

The original mode-capacity adapter changes only constructor ceilings. It does not prove a high-mode bound or replace any root, quadrature, or projection-floor condition.

## 331.3. The zero-shape seed

**Proposition 331.1.** At every regular sample satisfying §331.2, the state $Q=\Pi=0$ has angular root $L=0$. Every positive-branch test is exactly one:

$$
D=S=A=1.
\tag{331.5}
$$

All shape derivatives vanish. The mean correction derivative vanishes and the background mean derivative is $r_xw$. For the ideal finite root equations the root derivative with respect to $L$ at that state is $I_{M+1}$.

**Proof.** The source's sine coefficient $P$, cosine derivative $P_\theta$, and coefficient $U$ are linear expressions in $Q,L$. They are zero at $Q=L=0$. The source writes $K=L-P_\theta$, so $K=0$. Consequently the nonlinear quantity

$$
\mathcal T=2K+K^2+E P^2
$$

is zero, and the definitions

$$
D=1-w^2\mathcal T,\quad S=1-w^2P^2,\quad
A=1+L+w^2P_\theta
$$

give (331.5). Every term of the quadratic root correction vanishes. Equation (331.2) has target zero; hence the root residual at $L=0$ is zero.

Every nonlinear Gram correction contains a factor that is zero at this state. The identity term remains, giving the asserted root derivative. The implicit function theorem therefore supplies a local analytic positive-branch root near zero for this fixed regular sample. It gives no uniform neighborhood over an unbounded geometric family unless a separate bound establishes one.

The split shape RHS consists of its homogeneous linear action on $(Q,\Pi)$ and higher-order terms evaluated at this root. It is zero. Equation (331.4) proves the mean statements. ∎

**Corollary 331.2.** A complete chain may be initialized with all 577 shape nodes zero, independently of any stage height graph, gain, or cut-height division. Every interior residual and every homogeneous far Robin residual is then zero in exact arithmetic. For a nonzero requested cut target $t$, the cut residual is $-t$.

This is an initialization statement. It does not claim convergence of Newton, damped least squares, or the original ten-trial line search. It does not impose the cut target at the initial point. A soft cut residual must not be silently set to zero or projected away.

The original RK4 state expressions preserve zero shape whenever all actual intermediate coefficient operations are finite. Both mean entries are advanced with the same original RK4 schedule. Signed-zero words may depend on ordinary floating operations; a claim of identical bit patterns must be supported by the actual saved words, not inferred from this exact-real proposition.

For 576 native stages the constructor can therefore keep the original 32-iteration budget, ten steps $2^{-k}$ for $k=0,\ldots,9$, positive-branch guards, and strict decrease rule without requesting a per-node chart as an initialization prerequisite.

## 331.4. Non-divided physical and momentum boundary rows

At the zero root, (331.2) and (331.3) give the exact linear conversion

$$
\begin{pmatrix}H_j\\H_{j,r}\end{pmatrix}
 =
T_j
\begin{pmatrix}Q_j\\\Pi_j\end{pmatrix},
\qquad
T_j=
\begin{pmatrix}
r^4&0\\
m_j^2r^3&\epsilon\sqrt{12}\mu/(r^4w)
\end{pmatrix}.
\tag{331.6}
$$

Its determinant is $\epsilon\sqrt{12}\mu/w\ne0$. Thus it is an invertible two-coordinate change even if a particular column has zero height.

Let $v_j=(U_j,K_j)\ne(0,0)$ be a physical column at the finite far boundary. Its line is specified by

$$
-K_j H_j+U_j H_{j,r}=0.
\tag{331.7}
$$

Substitution of (331.6) gives the row

$$
c_{Q,j}Q_j+c_{\Pi,j}\Pi_j=0,
\quad
c_{Q,j}=-K_jr^4+U_jm_j^2r^3,
\quad
c_{\Pi,j}=U_j\frac{\epsilon\sqrt{12}\mu}{r^4w}.
\tag{331.8}
$$

No quotient by $U_j$ occurs. If $U_j=0$, then $K_j\ne0$ and this is the nonzero height row $-K_jr^4Q_j=0$. If $K_j=0$, the row still expresses the intended derivative condition. Since $T_j$ is invertible, the entire row cannot vanish for a nonzero physical column.

For an interval column, an assertion that the exact line is nonzero requires an actual nonvanishing argument about that column; a box containing the origin is not made nonzero by choosing a convenient midpoint. An actual scalar midpoint row is a disclosed numerical boundary approximation. Its uncertainty, joint parameter realization, and relation to the infinite-tail boundary remain separate responsibilities.

Multiplying one exact boundary row by a nonzero constant preserves its zero set. It changes a weighted least-squares residual unless the corresponding row weight is transformed consistently. A new implementation may declare a fixed positive power-of-two normalization and retain it as part of its explicit new norm. It may not call the resulting norm identical to the old $[-G,I]$ norm without proving that identity.

At a cell interface the momentum coordinate uses the cell's declared $\mu$. For the same physical angular connection,

$$
\Pi^{\mathrm{out}}
 =\frac{\mu_{\mathrm{in}}}{\mu_{\mathrm{out}}}
   \Pi^{\mathrm{in}}.
\tag{331.9}
$$

This is the original port operation. It acts on every momentum row of the nonlinear flow and its tangent. The cut conversion must use the actual outer port of the first stage. It is not permissible to reuse a stored old port or old node radius merely because the number of stages is unchanged.

## 331.5. The complete current chain and its weights

Let $N=576$, $K=224$, and $x_n\in\mathbb R^K$ for $0\le n\le N$. Let $F_n$ be the actual current finite stage map, including its momentum port. At a fixed current state write

$$
r_n=F_n(x_{n+1})-x_n,\qquad
J_n=DF_n(x_{n+1}).
\tag{331.10}
$$

Let $C=[I_M,0]$ be the complete cut selector and let $B\in\mathbb R^{M\times K}$ contain all finite far rows, including any mode coupling if a future actual construction supplies it. The full nonlinear residual is

$$
\mathcal R(x,H)=
\begin{pmatrix}
Cx_0-t(H)\\
F_0(x_1)-x_0\\
\vdots\\
F_{N-1}(x_N)-x_{N-1}\\
Bx_N
\end{pmatrix},
\qquad t(H)=H/r_c^4.
\tag{331.11}
$$

There are $M+NK+M=(N+1)K$ rows and the same number of unknowns. Its state derivative is the full block-bidiagonal system with boundary rows:

$$
A\delta=
\begin{pmatrix}
C\delta_0\\
-\delta_0+J_0\delta_1\\
\vdots\\
-\delta_{N-1}+J_{N-1}\delta_N\\
B\delta_N
\end{pmatrix}.
\tag{331.12}
$$

No coordinate is removed from this system.

Choose explicitly declared numbers $\sigma_n>0$. Define
$T=\operatorname{diag}(\sigma_nI_K)$ and the row weights
$W=\operatorname{diag}(\sigma_0^{-1}I_M,\sigma_0^{-1}I_K,
\ldots,\sigma_{N-1}^{-1}I_K,\sigma_N^{-1}I_M)$.
Then with $\delta=Tz$ the stage row is

$$
-z_n+V_nz_{n+1}+\rho_n,\qquad
V_n=\frac{\sigma_{n+1}}{\sigma_n}J_n,\quad
\rho_n=\frac{r_n}{\sigma_n}.
\tag{331.13}
$$

The cut and far matrices remain $C$ and $B$. Scalar positive weights do not require any height component to be nonzero.

For example, a caller may explicitly declare
$\sigma_n=s_*=\max(s_{\min},\|t\|_\infty)$ for every node, where $s_{\min}>0$ is a specified finite constant. This is a well-defined new reference norm with no old gains. It is not asserted to have the old graph-based conditioning or the old numerical acceptance scaling. Alternative complete positive scales must likewise be part of the current request and its saved identity.

The new target $g$, actual numerical geometry, scale vector, and boundary rows jointly determine the finite problem whose norm is tested. Keeping the literal number $2\cdot10^{-9}$ is not permission to conceal a change in any of these objects.

## 331.6. Complete damped QR without interior height charts

For an explicit $\eta>0$, consider

$$
\min_z\frac12\|W(ATz+\mathcal R)\|_2^2+
              \frac{\eta^2}{2}\|z\|_2^2.
\tag{331.14}
$$

It has a unique minimizer because its Hessian is
$(WAT)^\mathsf T(WAT)+\eta^2I\succeq\eta^2I$.
This exact-real coercivity does not certify the outcome of a rounded numerical factorization.

The complete-chain QR method is the orthogonal-compression construction of R273 with the final $[-G,I]$ replaced by the actual $B$. Each node contributes its complete penalty $\eta I_K$. Every residual column and every pure constant left after compression is retained.

**Proposition 331.3.** At every nonterminal stage, the columns being eliminated have full rank, independently of the ranks of all $J_n$ and independently of every intermediate height projection.

**Proof.** Before eliminating $z_n$, the coefficient block for it contains the complete stage block $-I_K$. If $L_n$ is the entire left block of that front, then

$$
L_n^\mathsf TL_n
 =I_K+P_n^\mathsf TP_n+\eta^2I_K
 \succeq I_K,
\tag{331.15}
$$

where $P_n$ denotes the carried constraints, with all preceding orthogonal transformations absorbed into them. Thus the $K$ columns are independent.

An orthogonal transformation makes them upper triangular and moves the remaining next-node rows below. Those rows may be compressed by another orthogonal transformation into at most $K$ carried coefficient rows plus pure affine rows. No inverse of that next-node coefficient block is taken, so its rank deficiency is harmless at this compression step. The pure affine rows must be retained because their squared norms are part of (331.14). The next original stage again supplies $-I_K$. Induction proves the assertion. ∎

For $\eta>0$, the last penalty also makes the terminal columns independent. Thus no exact-real local or terminal rank obstruction is introduced by a vertical height chart. Numerically, nonfinite formation, zero/underflowed pivots, finite resource exhaustion, or a failed triangular solve are still actual failures. They are not repaired by truncating modes, modifying the original data, or silently adding a different ridge.

The direction from (331.14) need not decrease the original weighted infinity norm. The same ten actual no-J trials and strict comparison decide its usefulness. Neither the least-squares objective nor an exact linear residual is a new nonlinear acceptance gate.

## 331.7. Undamped nonresonance is global

For the derivative of a solution map set $\eta=0$. Proposition 331.3 still applies: the $-I_K$ block supplies (331.15) without a penalty. All nonterminal variables can be eliminated without assuming that a stage height graph exists.

After these eliminations the coefficient matrix is orthogonally equivalent, up to an invertible ordering, to block upper triangular form with nonsingular nonterminal diagonal blocks $R_0,\ldots,R_{N-1}$ and one terminal block $R_N$. Accordingly,

$$
\operatorname{rank}A=(N K)+\operatorname{rank}R_N,
\qquad
A\text{ is invertible}\ \Longleftrightarrow\ R_N\text{ is invertible}.
\tag{331.16}
$$

This is a statement about the exact complete matrix, not about a chosen set of local Riccati denominators. It does not assert that $R_N$ is invertible for an uncomputed current state.

Strict nonresonance may be established by any valid exact or interval argument for this complete system. A floating nonzero triangular diagonal alone does not establish it. Conversely, failure of an old intermediate height graph alone does not establish global resonance. The numerical implementation must distinguish these cases in its result.

The same distinction applies to [R324](R324-continuous-C-finite-head-flux-and-closed-tube.md): a certified nonzero cut component of a particular zero-state mode column is useful information, but it does not prove nonzero height components at every intermediate node, and it is not a nonlinear full-current-state nonresonance certificate.

## 331.8. All 112 physical-height sensitivities

Suppose the ideal finite branch is differentiable near a solution of (331.11), and suppose its full current $A$ is invertible. The implicit function theorem gives the derivative $X_n=D_Hx_n\in\mathbb R^{K\times M}$ as the unique solution of

$$
CX_0=r_c^{-4}I_M,\qquad
-X_n+J_nX_{n+1}=0,\qquad
BX_N=0.
\tag{331.17}
$$

All 112 right-hand sides must be included. They can be carried simultaneously through the same complete undamped QR. No stage height graph is required. All pure affine rows of the multiple-right-hand-side compression remain part of the readback.

A damped solve of (331.17) instead satisfies a regularized least-squares problem. Except in a special coincident case, it is not $D_Hx$. Hence the $\eta=1$ nonlinear correction and the $\eta=0$ endpoint sensitivity have separate identities and separate outputs.

In a floating implementation, the native target uses one actual binary64 denominator $d_c=\operatorname{fl}(r_c^4)$ and the actual division by that fixed word. The child must receive that original denominator word; independently recomputing $r_c^4$ in extended precision is not the same finite coefficient formation. The exact-real statement (331.17), the explicitly formed floating system, and the readback against its original saved operands must be kept distinct.

The top half of the mathematical $X_0$ is exactly $r_c^{-4}I_M$. A numerical solve should retain its actual top half and residual; it must not overwrite the saved sensitivity to force that identity. Where the old endpoint finite-difference convention explicitly uses a known unit $Q$ perturbation and the returned momentum tangent, its use and the residual of the solved top rows must both be reported.

## 331.9. Endpoint two-jets and all 338 response rows

Let $Y$ be the cell-engine cut state obtained from the shooting state by the actual cut momentum port. The original physical-jet evaluator supplies

$$
\begin{aligned}
H_{j,r}&=m_j^2r_c^3Y_{Q,j}+\sqrt2\,wL_{j+1},\\
H_{j,rr}
&=\frac{m_j^2r_c^3(F_{Q,j}+3(r_x/r_c)Y_{Q,j})
 +\sqrt2\,w(L_{j+1,x}+(\log w)_xL_{j+1})}{r_x},\\
b_r^{\mathrm{corr}}&=wL_0,\\
b_{rr}^{\mathrm{corr}}&=\frac{w((\log w)_xL_0+L_{0,x})}{r_x}.
\end{aligned}
\tag{331.18}
$$

The full background additions are $w$ and $w(\log w)_x/r_x$. They are not discarded or relabelled as zero.

The response vector has the order

$$
\bigl((H_{j,r})_{j=0}^{M-1},
(H_{j,rr})_{j=0}^{M-1},
b_r^{\mathrm{corr}},b_{rr}^{\mathrm{corr}},
(H_j)_{j=0}^{M-1}\bigr),
\tag{331.19}
$$

so it has $3M+2=338$ rows. The complete height derivative therefore has shape $338\times112$.

The analytic first-slope chain rule can be written without a local Dirichlet graph. Let $P_c$ multiply the cut momentum rows by the actual port ratio, and put $\widehat X_0=P_cX_0$. If $F_Q'$ denotes the first $M$ rows of the actual local RHS derivative, then

$$
D_H(H_r)=\frac{r_c^4}{r_x}F_Q'\widehat X_0+
                        4r_c^3(X_0)_Q,
\tag{331.20}
$$

and for the first mean-state derivative row $F_{\mathrm{mean}}'$,

$$
D_H b_r^{\mathrm{corr}}=\frac1{r_x}
 F_{\mathrm{mean}}'\widehat X_0.
\tag{331.21}
$$

These follow by differentiating
$H_r=r_c^4Q_x/r_x+4r_c^3Q$ and
$b_r^{\mathrm{corr}}=z_{0,x}/r_x$, with fixed geometry. The complete nonlinear boundary response changes $H$ and the state, not the declared target metric.

The original second-jet numerical adapter uses a symmetric difference along the current cut tangent with its stated step. A new owner may preserve that method and its full 338 layout, but must retain its finite-difference scope and actual current sensitivity source. It may not substitute the old graph, omit the mean rows, or call this numerical difference an exact derivative certificate.

The original full finite audit still evaluates the actual current root, RHS, physical two-jets, all native stages and angle nodes. Its sampled metric/Darboux/holonomy diagnostics do not become a continuous infinite-tail or complete closed-surface certificate.

## 331.10. Correct source and geometry responsibilities for the new provider

A runnable current-C owner needs more than the algebra above:

- The same actual C source/config/ready identities and the same declared continuous model.
- Actual coefficient values at every RK/root and final-audit point, including the complete cap/flat/valley geometry, all ports, means, and the true cut containment. If interval evaluation is used, the numerical selection, its error, and any unresolved joint-realization premise must remain explicit.
- A complete actual finite far row for each of the 112 modes, transported from the declared deep data to the actual finite nonlinear boundary. A cut-only slope table does not supply these rows at another radius.
- All 576 current stage maps and full current variational matrices, with every original no-J trial evaluated from its actual rounded state.
- An explicit positive current scale vector and the intended weighted norm; no hidden inheritance from old graphs or gains.
- The complete current nonlinear result, the distinct undamped 112-column sensitivity, the full 338 response, and the original finite final audit.

A zero seed pays none of the missing geometric data. A schema string does not prove that a coefficient producer called the correct continuous expression. A complete boundary matrix does not prove its nonresonance. A successful finite numerical native solve does not prove the infinite nonlinear tail, the full 699/453 boundary-value problem, same-$g$ refinement, or any closed-surface conclusion.

The independent sources for request153 can reuse the frozen root/product/physical-jet formulas and the unchanged complete Householder front routine while giving the new geometry, scale, general boundary, current state, and all-RHS result their own identities. The old sources and all old actual results remain unchanged.

## 331.11. What is added, and what remains unpaid

The new result is the graph-independent structural route from a regular current-C geometry to a full finite nonlinear shooting and sensitivity computation. It strengthens neither the deep-root existence theorem nor the continuous metric certificate. It introduces no numerical fixture, new nonlinear threshold, rank-truncation rule, or additional acceptance test.

The obligations that require real computation remain explicit: complete current geometry and far-row production; positive-branch existence along actual trials; actual native convergence; a current complete sensitivity result and any strict nonresonance certificate claimed for it; the full finite audit; and the subsequent full physical BVP/continuous/closed-field responsibilities.

In particular, none of those obligations has been marked paid merely by proving that the zero seed and the non-divided chain algebra are well defined.
