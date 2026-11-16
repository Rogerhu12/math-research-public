# R133 supplement: complete paired Neumann reconstruction and physical root96 normalization

2026-11-16, newton_source. Pure operator theorem and a conditional implementation contract; no numerical function is evaluated.

**Proved: a conditional operator theorem. The actual finite gate remains to be evaluated.**

The WIC inherited refinement-160 theorem already supplies the actual tail inverse. The current WPS consumer is designed to evaluate the complete finite gate. This note explains precisely what a successful gate would permit next. It gives an iteration on the entire actual finite-plus-tail system, a complete a posteriori residual estimate, and the genuine prescribed-root96 realization. It requires no prior implementation of the unknown actual Schur inverse or actual tail inverse.

A failed WPS sufficient gate does not activate this conclusion and does not prove singularity. The theorem does not replace any independent negative-head, metric, $\nu$, $\Theta$, physical-mean, external-function or later matching equation.

## WPN1. The same four blocks and two right sides

Use exactly the selected member, ordinary radial measure, inherited refinement160, cell maps, projection, and Hilbert coordinates of WIC and WPS. Let

$$
 \mathcal A=
 \begin{pmatrix}A&B\\C&R\end{pmatrix}:
 X_f\oplus X_t\longrightarrow Y_f\oplus Y_t .
 \tag{WPN.1}
$$

Here the finite input has the normalized cell coefficients, the 97-dimensional root complement, and the actual 96-dimensional outer chart. The prescribed root-even96 data are in the original right side. The finite dimension is $193N+193$, with $N=24480$. The physical even mean has weight1; the nonzero real sine and cosine modes have their original square-root-of-two normalization. The outer coordinates retain the actual $H^{-5/6}$ Riesz factors.

The full right side is written

$$
 \mathcal A\binom{x}{z_{\rm raw}}=\binom{f_f}{g_t}.
 \tag{WPN.2}
$$

The term $g_t$ is the genuine radial-meanzero tail row. It is not set to zero for an arbitrary source, independent function or interface input. In particular the two finite radial moments of WPS2 do not describe the whole unprojected Volterra source.

Let $R_D$ be the true principal tail operator, in the same transformed Hilbert coordinates. Let $Q_f$ be the actual inverse of the finite rational-normalizer reference square $A_\rho$. Both are bounded two-sided isomorphisms, by the WPT and WIC principal theorems. They are reference operators, not approximations asserted to equal $R$ or the actual finite Schur matrix.

Use the principal trials

$$
 Z=R_D^{-1}C_D,\qquad
 Y=R_D^{-*}B_D^*Q_f^* .
 \tag{WPN.3}
$$

All adjoints are in the actual Hilbert coordinates. The complete principal mean, endpoint rows, centered ramp, cell lengths and outer weights are already included in these definitions. There is no unweighted transpose standing in for an adjoint.

The actual defects are those of WDS and WPS:

$$
 T=C-RZ,\qquad
 D^*=Q_fB-Y^*R,
$$
$$
 E_0=Id-Q_fA+Q_fBZ+Y^*T .
 \tag{WPN.4}
$$

The symbols $D^*$ and $T$ describe full tail-input and finite-input operators. They are not lists of tested columns or merely formal interior differential residuals.

## WPN2. An exact complete left-right reduction

Define the triangular coordinate and row maps

$$
 \mathcal W=
 \begin{pmatrix}Id&0\\-Z&Id\end{pmatrix},
 \qquad
 \mathcal L=
 \begin{pmatrix}Q_f&-Y^*\\0&R_D^{-1}\end{pmatrix}.
 \tag{WPN.5}
$$

Their source and target spaces are the corresponding full direct sums in (1). Since $Q_f$ and $R_D$ are bounded two-sided isomorphisms and $Y,Z$ are bounded, both triangular maps are bounded isomorphisms. This fact is needed to preserve equivalence with the original system.

Multiplication in the displayed order gives

$$
 \mathcal L\mathcal A\mathcal W
 =
 \begin{pmatrix}
 Id-E_0&D^*\\
 R_D^{-1}T&R_D^{-1}R
 \end{pmatrix}
 =Id-\mathcal N,
$$
$$
 \boxed{\quad
 \mathcal N=
 \begin{pmatrix}
 E_0&-D^*\\
 -R_D^{-1}T&K
 \end{pmatrix},\qquad
 K=Id-R_D^{-1}R .
 \quad}
 \tag{WPN.6}
$$

For example, the upper-left entry before subtraction is

$$
 Q_f(A-BZ)-Y^*(C-RZ)=Id-E_0.
$$

The lower-left entry is $R_D^{-1}(C-RZ)$, with no change of order. The lower-right entry is the genuine $R_D^{-1}R$. No coefficient, Volterra map, projection, primitive or exterior observation has been commuted.

Put

$$
 \binom{b_f}{b_t}
 =\mathcal L\binom{f_f}{g_t}
 =\binom{Q_ff_f-Y^*g_t}{R_D^{-1}g_t}.
 \tag{WPN.7}
$$

Then the complete original problem is equivalent to

$$
 (Id-\mathcal N)\binom{x}{v}=\binom{b_f}{b_t},
 \qquad z_{\rm raw}=v-Zx.
 \tag{WPN.8}
$$

This is an exact use of both original right-side rows. It does not require applying an unknown $R^{-1}$ or an unknown actual finite Schur inverse.

## WPN3. The already declared WPS gate controls the whole system

The inherited WPT/WIC estimate is a bound on the same left-principal-preconditioned tail error:

$$
 \|K\|\le\gamma,\qquad \gamma=2/3,
 \qquad \|R_D^{-1}\|\le1 .
 \tag{WPN.9}
$$

The published analytic proof actually gives a strict smaller rational bound; the non-strict value in (9) is a safe constant. This is not a claim that $\|Id-R\|\le2/3$ without the principal inverse. The WPS record $t$ continues to bound the complete $T$ itself: its use in the lower-left entry pays the already proved factor $\|R_D^{-1}\|\le1$. No unproved norm-one identification is made.

Suppose a complete WPS result gives

$$
 \|E_0\|\le e,\qquad \|D\|\le d,\qquad \|T\|\le t,
 \qquad e+3dt<1.
 \tag{WPN.10}
$$

Here $e,d,t$ are complete nonnegative scalar bounds for the same actual operators and same trial. No entry is selected from another incomplete candidate.

For every pair of vectors, (6) implies the component estimate

$$
 \binom{\|(\mathcal Nu)_f\|}{\|(\mathcal Nu)_t\|}
 \le M\binom{\|u_f\|}{\|u_t\|},
 \qquad
 M=\begin{pmatrix}e&d\\t&2/3\end{pmatrix}.
 \tag{WPN.11}
$$

Write

$$
 \Delta=(1-e)/3-dt>0,\qquad
 \omega_f=1/3+d,\qquad \omega_t=1-e+t .
 \tag{WPN.12}
$$

Both weights are strictly positive. Direct multiplication gives

$$
 (Id-M)\binom{\omega_f}{\omega_t}
       =\Delta\binom11 .
 \tag{WPN.13}
$$

Therefore, for the equivalent norm

$$
 \|(u_f,u_t)\|_\omega
  =\max\{\|u_f\|/\omega_f,\|u_t\|/\omega_t\},
$$

the complete operator satisfies

$$
 \|\mathcal N\|_\omega
 \le 1-\frac{\Delta}{\max(\omega_f,\omega_t)}<1.
 \tag{WPN.14}
$$

This proves a bounded two-sided inverse of $Id-\mathcal N$ on the full finite-plus-infinite space. In particular

$$
 \boxed{\quad
 \mathcal A^{-1}
 =\mathcal W\sum_{n=0}^{\infty}\mathcal N^n\mathcal L .
 \quad}
 \tag{WPN.15}
$$

The series converges in operator norm. It is a constructive full-system version of the same WDS sufficient gate; it is not an additional gate or an additional assumption about the head Fredholm index.

Only the fixed reference inverses $Q_f$ and $R_D^{-1}$ occur in a single application of $\mathcal N$. The other factor is the actual operator $\mathcal A$. Implementing its actual high action remains a real computational obligation; it cannot be replaced by the high trial without its complete correction certificate.

## WPN4. Explicit two-component solution and error bounds

For a complete right-side family, let $a_f$ and $a_t$ bound the two norms in (7). The nonnegative inverse of $Id-M$ is

$$
 (Id-M)^{-1}
  =\frac1\Delta
       \begin{pmatrix}1/3&d\\t&1-e\end{pmatrix}.
 \tag{WPN.16}
$$

Thus the solution of (8) obeys

$$
 \|x\|\le\frac{a_f/3+d a_t}{\Delta},\qquad
 \|v\|\le\frac{t a_f+(1-e)a_t}{\Delta}.
 \tag{WPN.17}
$$

The estimate applies equally to a bounded family of inputs by using the corresponding operator norms. Its two inputs are independent. There is no assertion that their output images are orthogonal.

More usefully, let $(\widehat x,\widehat v)$ be any admissible approximation, and enclose the complete preconditioned residual

$$
 r=\binom{b_f}{b_t}
       -(Id-\mathcal N)\binom{\widehat x}{\widehat v},
 \qquad
 \|r_f\|\le\varepsilon_f,\quad
 \|r_t\|\le\varepsilon_t .
 \tag{WPN.18}
$$

Then (17) holds for the error with $a_f,a_t$ replaced by $\varepsilon_f,\varepsilon_t$. If a complete saved finite-gap record gives

$$
 0<g\le1-e-3dt,
$$

the following convenient bounds use that old gap without reevaluating an old whole target:

$$
 \|\widehat x-x\|
 \le\frac{\varepsilon_f+3d\varepsilon_t}{g},
$$
$$
 \|\widehat v-v\|
 \le\frac{3t\varepsilon_f+3\varepsilon_t}{g}.
 \tag{WPN.19}
$$

The second inequality uses $1-e\le1$ only after the complete bound (16). It is conservative but does not change the operator.

Let $z_0$ bound the already defined complete $Z$. Reconstruction gives

$$
 \|\widehat z_{\rm raw}-z_{\rm raw}\|
 \le \|\widehat v-v\|+z_0\|\widehat x-x\|.
 \tag{WPN.20}
$$

The cell part of $x$ and $z_{\rm raw}$ lie in orthogonal radial projection spaces. Its raw head is recovered in the original order by $S^{-1}$. Any reported raw or Sobolev state estimate must pay that complete coordinate map and the original given-head high columns. Neither a trace nor an endpoint is evaluated on an arbitrary intermediate $L^2$ head.

If evaluation of the actual operator is approximate, retain its complete error vector $\eta_f,\eta_t$. Add it to the corresponding two residual bounds in (18). A sample residual, a residual of a truncated angular operator, or only the interior high equation is not such a certificate.

## WPN5. The 96 prescribed-root columns are genuine and normalized

The root decomposition is fixed, not chosen by the reference solver:

$$
 a(r_*)=E_dd+E_cc,
$$

where $E_d$ contains the 96 normalized odd modes and physical mean, and $E_c$ contains the 96 normalized even nonmean modes. The actual outer low chart has its independent 96 coordinates. These are the same embeddings as WIC.7.

For the pure prescribed-root input, with every other independent input zero, the zero-IVP right-side pair before radial projection is exactly

$$
 \mathcal F_c c
   =\binom{S C_*E_c c}{-E_c c},
 \qquad
 (C_*v)(r)=v .
 \tag{WPN.21}
$$

The identity $C_*v(r)=v$ is exactly WOB.24 and WOB.30--31, not a new root-chart choice. $S$ is constant on each inherited cell. Hence $Q_NS C_*E_c=0$. This particular right side has $g_t=0$. This conclusion does not apply to a general ordinary source or a jump inside a cell.

Under the complete gate (10), let $U_c$ be the solution family obtained by applying (15) to (21), then reconstructing the same actual high state and original chart data. The low equation implies its actual $H^1$ regularity, or the original piecewise $H^1$ regularity with the prescribed jumps. Only at that point is the true root trace read. It gives

$$
 \boxed{\quad
 \Pi_{\rm root,even,1:96}\,U_c=Id_{\mathbb R^{96}} .
 \quad}
 \tag{WPN.22}
$$

Consequently these are 96 linearly independent actual positive solutions, not reference vectors and not columns of an unsigned norm bound. If the requested signed normalization is exactly this prescribed root-even trace, its matrix is the identity by the original boundary condition. A second numerical determinant test for that same identity is unnecessary.

A different requested readout is not identified with (22). Its true conversion, signed values, and any independent compatibility remain to be proved. The theorem also does not state that the standalone supplied-head Fredholm operator has zero kernel. It proves invertibility of the entire prescribed-root positive problem containing the complete head feedback and outer matching.

Independent $\nu$, $\Theta$, negative-side matching, metric rows, physical-density means, WFR/WCF auxiliary factors and original functional inputs remain in their genuine equations. No such row is removed by (22).

## WPN6. Every source, trace and jump remains in the residual oracle

The complete actual action used in (6), (18) is defined by the original seven-port realization. A new numerical application must retain:

1. Both ordinary collar and body source portions, in their original Sobolev source windows and ordinary $dr$ measure.
2. The original stable datum and all exterior chart, height and physical-mean data, with the actual endpoint Riesz maps.
3. All three original interface-source classes, both sides of every actual jump and the corresponding homogeneous raw transmission.
4. Every independent affine, low-head, mean and external functional column.
5. The full raw endpoint row, including the high trace, regular Robin remainder, mean reconstruction and its actual signs.
6. The full principal-tail and centered-ramp corrections in the chosen left and right trials.

The complete primal Green identity or complete dual weak Green identity of WDS may certify a high application. In either case the body and every boundary/interface defect must be received through the already admitted whole column for that exact port. Zero trial traces only remove the trial's own boundary term; they do not remove a nonzero observation in the requested functional.

Signed centre coefficients can be used with a declared true-to-centre error as in WDS7 and WPS7. The degree32 centre support does not clip the complete degree96 error. Each difference is a signed interval difference or a proved whole two-factor estimate. Subtracting positive norm uppers is never a residual calculation.

The full independent right side is transformed by (7). An ordinary source $g$ contributes both $S V_0g$ and minus its complete integral in the endpoint row before the split. Its $Q_N$ component stays in $b_t$. An affine jump contributes its actual step term and endpoint correction, even if that step is not constant on a chosen refined cell. It is not replaced by a finite moment without an exact identity.

## WPN7. Minimal next contract after a successful WPS result

This section specifies preparation; it does not report a numerical run or assign a prospective successful input.

The next consumer first binds the complete actual WPS file, its execution and manifest, all source identities and the complete retained input scope. It requires all 22 structural gates, every completed graph, and a true complete finite gate. It copies the saved $e,d,t,q$, $Z$/profile and finite-gap/inverse records from their exact named paths. Existing WIC/WPS reference, old receiver, source, mean, jump, endpoint and completed target records are read verbatim.

There are then two distinct deliverables.

**Existence and root normalization.** Equations (15), (21), (22) already prove the actual family and its specified normalization. They require no repeated WPS computation, no dense 4724833-square matrix, no independent determinant of the root-even identity and no numerical construction of every state column.

**Numerical approximation or a different physical readout.** Freeze an actual trial family, its complete signed coefficient definition and finite resource cap. Enclose both components of (18), including the complete Green-oracle error. Save those two complete residual targets before any error receiver uses them. New bounds such as (19), (20), or a different complete physical readout are distinct targets. The old finite gap and every original receiver are read, not recomputed.

For a 96-column family, a valid finite-input option is to process columns one at a time, preserve a complete ordered prefix and use the Euclidean sum of squared complete column residuals to obtain each whole operator residual. This is a declared full-column bound, not output orthogonality. A sharper complete simultaneous Schur certificate is also possible. Either method must include all 96 actual inputs and both residual components. It does not allocate the entire finite matrix.

A reference application costs the proved modewise circuit work. This fact alone is not a runtime bound for an actual high action. Before execution, separately cap all coefficient enclosures, primal/dual source evaluations, actual angular support, interface checks and both output rows. No adaptive increase in modes, mesh or iterations is permitted after a failure unless it is a separately defined remaining task.

Any computed trial, signed pivot, complete residual, received error or whole readout must be saved before downstream use. Temporary vectors or coefficient arrays stay in Actions. A failure preserves every completed target and prefix; it does not authorize a new trial under the same consumed marker.

## WPN8. Status and immutable primary evidence

This theorem is conditional on the actual complete WPS gate. It is independent of the success of any particular unpublished execution. At writing, no actual finite success is inferred from the manifest, static models, reference circuit or analytic tail alone.

The exact source and coordinate identities used here are:

| Complete primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WDS full four blocks, both right sides and weak Green oracle | 5e93ca37c37d82787ea870aad977712f41b2d4ea | 32943 | 4c7c9d6e582a486f0fe233ac2e617b0f3136ac8a1ed168001f7134050b2230f9 |
| WIC actual inherited tail, reference inverse and root coordinate table | 019b1136ebe81e44e98399dff5fb895aafb4362e | 29026 | 527fc35e48f8bb8807e2dc7e7a4b8726e381d35183f31bf8977b252dbb66e59f |
| Published WPS complete paired residual and both source rows | e830f7df4643fe77b941478dbde06ebf9378ebef | 43851 | ffd000ff15f705ffaaf3c33dddcd0c09c997c0c92d5110bab5be5ea9c114fa72 |
| WOB complete zero-IVP root embedding and physical outer rows | 8a55c94d8decc25f33876665119b327eb1d1fd29 | 41683 | f13024a72e09d9b388fc51eac39d675b656d4d75ee72cdafe449a1c325e92979 |

All four complete texts were read to check the displayed order and domain. No original scientific calculation, new norm, finite inverse or operator application was executed to write this note.
