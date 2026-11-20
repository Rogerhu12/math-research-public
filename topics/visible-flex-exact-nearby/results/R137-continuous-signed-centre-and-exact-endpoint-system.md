# R137：连续有符号 WJK 中心与精确609维端点系统

2026-11-20, `visible-exact-astra-ac637-20261120 / positive_inverse`.

**Proved below:** the continuous version of the fixed-WVC complete signed centre has an exact realization with 1217 scalar states and 608 left / 609 right boundary conditions. Invertibility of `Id-Hc_cont` on its complete body-plus-193-atoms space is equivalent to a single 609 by 609 endpoint matrix being nonsingular. The published finite receiver is the radial projection of this continuous map; it is not silently identified with it. This removes the small-centre-norm requirement for a prospective continuous preconditioner. It neither proves that the endpoint matrix is nonsingular nor changes the actual positive operator.

No numerical target has been evaluated. The actual family remainder, both original right-side rows, all seven high ports, actual outer graph, physical mean, negative head, metric/nu rows and nonlinear matching remain. This note is a concrete alternative after, or alongside, the current W2C norm evaluation. It does not change that already declared candidate or recompute its successful predecessors.

## 1. Fixed same-object inputs

All paths below are relative to `topics/visible-flex-exact-nearby`.

- `results/R133-supplement-joint-centre-Green-kernel-and-complete-collar-cross-terms.md`, especially JK.3--8 and JK.15--21.
- `results/R133-supplement-complete-collar-Volterra-dual-feedback-candidate.md`, especially W2C.5, W2C.10--21, W2C.25--32.
- `results/R133-supplement-paired-source-circuits-and-complete-finite-residual-candidate.md`, WPS.1 and WPS.12--15, for the complete source/endpoint pair.
- `scripts/fourfold_codazzi_collar_dual_feedback_math.py::prepare_complete_kernel_context` supplies the genuine signed collar, same 153 parents and 155-or-fewer comparison panels, original WVC reference and normalized real coefficient fields.

Use the true interval $[a,R]$, true collar $[a,c]$, the same $\chi,\psi$ and ordinary $dr$. Set $p_c={\bf1}_{[a,c]}$, $p_b=1-p_c$. On the collar $\chi=0$, $\psi=1$; the continuation and transition of $J$ are exactly the old ones.

Work in the original normalized real coordinates. Let

$$
 E_L=\operatorname{span}(o_1,\ldots,o_{96},m,e_1,\ldots,e_{96}),
 \qquad \dim E_L=193,
$$
$$
 K_0=\operatorname{span}(o_j,e_j:97\le j\le160),\quad \dim K_0=128,
$$
$$
 K_1=\operatorname{span}(o_j,e_j:97\le j\le224),\quad \dim K_1=256.
 \tag{S.1}
$$

Here $o_j=(\sqrt2\sin4j\phi,0)$, $e_j=(0,\sqrt2\cos4j\phi)$ and $m=(0,1)$. Denote the isometric inclusion $K_0\to K_1$ by $E$ and its transpose by $P$.

Use the **raw** centre blocks

$$
 A_L=A_{LL,c},\quad B=B_{HL,c}:E_L\to K_0,
 \quad C=B_{LH,c}:K_0\to E_L,
$$
$$
 A_{11}=\Pi_1A_c\Pi_1,\qquad A_{10}=A_{11}E,
 \qquad A_{01}=P A_{11}.
 \tag{S.2}
$$

The right $S^{-1}$ is applied to an input before these raw blocks, and the original $S$ and atom Riesz factors are applied to outputs. They are not omitted. The full physical mean is in $A_L$.

The old high reference $G=G_{0,160}$ is the two-boundary inverse of $\partial_r-D$ on $K_0$, with root even value zero and outer odd+$p_0$ even value zero, $p_0=13/80$. Its generator on mode $j$ is

$$
 D_j=4j\widehat\eta\begin{pmatrix}0&q^2\\1&0\end{pmatrix}.
 \tag{S.3}
$$

The piecewise $\widehat\eta,q$ are the same original WVC reference data. The low reference $D_f$ additionally has the same tracefree diagonal $\operatorname{diag}(a_j,-a_j)$ and zero reference mean. No actual low mean coefficient is thereby zeroed.

## 2. Exact projection needed by the returned centre, not by the actual high inverse

The centre source $Bf$ lies in $K_0$. The centre operator has angular bandwidth64. Consequently

$$
 p=\{\chi G\chi+\psi(J+JA_cJ)\}Bf
 \quad\hbox{takes values in }K_1.
 \tag{S.4}
$$

Its full centre residual $r=(\partial_r-A_c)p-Bf$ can reach288, exactly as W2C states. However the *returned signed centre* only reads

$$
 C\{p-Q^*r\},\qquad
 Q^*=\chi G\chi+(-J^*+J^*A_cJ^*)\psi.
 \tag{S.5}
$$

The first term of $Q^*$ reads $\Pi_0r$. The direct $J^*$ term is followed by $C=C\Pi_0$. In the last term $\Pi_0 A_c$ reads only $K_1$, because $j>224$ cannot reach $j\le160$ in one bandwidth64 action. The radial primitives do not change angular support. Therefore every occurrence of $r$ in (S.5) can be replaced **exactly** by $r_1=\Pi_1r$.

This is a two-sided support statement for one known finite trial composite. It does not say that the complete residual stops at224, does not clip its norm, and does not project $G_Hr$. The actual centre residual288 and family residual416 used in W2C remain unchanged.

## 3. The six auxiliary states

For a raw low field $x(r)$ set $f=Bx\in K_0$. Introduce

$$
 \begin{array}{c|c|c}
 \text{state}&\text{definition}&\text{dimension}\\ \hline
 y&G(\chi f)&128\\
 z_0&Jf&128\\
 z_1&JA_cJf&256\\
 y_r&G(\chi P r_1)&128\\
 t_0(r)&\displaystyle\int_r^R\psi(s)r_1(s)\,ds&256\\
 t_1(r)&\displaystyle\int_r^R p_c(s)A_{01}(s)t_0(s)\,ds&128
 \end{array}
 \tag{S.6}
$$

All six functions are continuous ordinary $H^1$ fields for an ordinary $L^2$ input. In particular $z_0,z_1$ are constant beyond $c$. The state $t_0$ is defined on the **whole interval** and has terminal value zero at $R$. This is what retains the true upper limit $R$ in $J^*$. Replacing its terminal point by $c$ would delete the original transition contribution.

The differential equations are

$$
 y'=Dy+\chi f,\quad z_0'=p_cf,\quad z_1'=p_cA_{10}z_0,
$$
$$
 y_r'=Dy_r+\chi P r_1,\quad
 t_0'=-\psi r_1,\quad t_1'=-p_cA_{01}t_0.
 \tag{S.7}
$$

The two $G$ states each have both original homogeneous reference boundary conditions. The $z$ states are zero at $a$; the $t$ states are zero at $R$. No adjoint generator is used in the second $G$: (S.5) contains $Q^*$, which uses the original $G$, not $G^*$. The transpose of the dual trial has already been taken in JK.4.

Put $p_1=\chi Ey+\psi(Ez_0+z_1)$. Differentiating the complete fields, using only (S.7), gives the exact signed residual

$$
\begin{split}
 r_1={}&(\chi^2+\psi p_c-1)Ef
 +(\chi'E+\chi ED-\chi A_{10})y\\
 &+(\psi'E-\psi p_bA_{10})z_0
 +(\psi'I_{K_1}-\psi A_{11})z_1.
\end{split}
 \tag{S.8}
$$

No derivative of $x$, $B$, $A_c$ or a coefficient enclosure is taken. Both cutoff derivatives are present. On the collar (S.8) reduces to $-A_{11}z_1$, the projected version of the exact second-order collar residual. On the body it contains the full transition and old body defect.

Since $J^*h=p_c(r)\int_r^R h(s)ds$, substitution in (S.5) yields

$$
 \boxed{\quad P Ff
 =\chi y+\psi(z_0+Pz_1)-\chi y_r
                    +p_c(Pt_0-t_1).\quad}
 \tag{S.9}
$$

Here $F=P_{
m trial}+Q^*-Q^*L_cP_{
m trial}$ is exactly JK.7; $P$ in (S.9) denotes only the coordinate projection. The notation is deliberately separated from the old trial letter. Formula (S.9) contains all five JK.8 collar terms automatically. No separate positive upper has been subtracted.

## 4. Closing the centre: 1217 states, 608 left rows, 609 right rows

The continuous low centre equation, with ordinary source $g$, is

$$
 x'=A_Lx+C\,PFBx+g .
 \tag{S.10}
$$

Together with (S.7)--(S.9) this is a finite first-order linear ODE on

$$
 X=(x,y,z_0,z_1,y_r,t_0,t_1),\qquad
 \dim X=193+128+128+256+128+256+128=1217 .
 \tag{S.11}
$$

The homogeneous low reference boundary conditions are the96 root-even values, the96 outer odd+$p_0$ even relations, and the outer physical mean. With the six auxiliary conditions, the left boundary map $L$ consists of

$$
 x^e_{1:96}(a),\quad y^e_{97:160}(a),\quad
 z_0(a),\quad z_1(a),\quad y_r^e{}_{97:160}(a).
 \tag{S.12}
$$

Its row count is $96+64+128+256+64=608$. The right boundary map $B_R$ consists of

$$
 x^o+p_0x^e,\quad x^m,\quad
 y^o+p_0y^e,\quad y_r^o+p_0y_r^e,\quad t_0,\quad t_1
 \quad\text{at }R.
 \tag{S.13}
$$

Its row count is $96+1+64+64+256+128=609$. The independent outer low coordinates are the even endpoint values with their original $H^{-5/6}$ weights. The root odd96 plus physical mean are the97 root-complement observations. They have not been turned into extra free conditions.

All coefficients are bounded on the true interval by the admitted full collar and body packets. In particular (S.7)--(S.10) divide by neither $K$ nor $\sqrt K$. Finite-dimensional ODE theory therefore gives an absolutely continuous fundamental matrix $\Phi(r,a)$. All states cross each original raw identity interface continuously; a jump of the coordinate weight $S$ is not inserted into these raw equations.

Let $N:\mathbb R^{609}\to\ker L$ be the coordinate isometry whose columns are

$$
 (x^o_{1:96},x^m),\quad y^o_{97:160},\quad
 y_r^o{}_{97:160},\quad t_0,\quad t_1
 \quad\text{at }a.
 \tag{S.14}
$$

For zero left data every solution is $X=\Phi N c+X_p$, with $X_p$ the zero-initial particular for the complete ordinary source. Hence the entire boundary problem is equivalent to

$$
 \boxed{\quad M_{609}c=b_R-B_RX_p(R),\qquad
 M_{609}=B_R\Phi(R,a)N.\quad}
 \tag{S.15}
$$

This proves both directions: $M_{609}$ nonsingular gives a unique solution for every ordinary source and right datum; if it is singular, a nonzero $\Phi Nc$ is a homogeneous solution. Nonzero left data are handled by their exact initial lift and do not change the matrix. The count609 is not a claimed193-dimensional reduction.

There is no auxiliary-only homogeneous kernel hidden in this statement. If a homogeneous state has $x=0$, then $f=Bx=0$. The same two-boundary reference inverse gives $y=0$; the zero left data and the two successive equations give $z_0=z_1=0$. Formula (S.8) then gives $r_1=0$, so the second identical reference problem gives $y_r=0$. Finally the zero terminal data give $t_0=t_1=0$. To verify the reference uniqueness directly, in one mode start (S.3) from $(y^o,y^e)(a)=(\alpha,0)$. Since $\widehat\eta\ge0$ and $q^2>0$, its value at $R$ is $\alpha(v_1,v_2)$ with $v_1\ge1$ and $v_2\ge0$. The condition $y^o(R)+p_0y^e(R)=0$, with $p_0>0$, forces $\alpha=0$. Thus a nonzero vector in $\ker M_{609}$ necessarily has a nonzero low field $x$.

## 5. The exact square space and the original finite projection

Let

$$
 \mathscr Z=L^2(I;E_L)_{\widetilde a=Sa}
       \oplus\mathbb R^{97}_d\oplus\mathbb R^{96}_{\widehat b},
 \qquad\widehat b_j=(1+16j^2)^{-5/12}b_j.
 \tag{S.16a}
$$

The body uses ordinary $L^2$ in the transformed variable, and both finite summands use Euclidean norm in the displayed inherited coordinates. Let $\operatorname{pr}_{\rm body}$ read only its first summand. Let $G_D$ be the full raw low reference ordinary-source inverse and let $\mathcal O_D$ give $S$ times its body plus its97 root-complement and96 weighted outer observations. Define the explicitly **continuous** lifted centre by

$$
 H_c^{\rm cont} z=\mathcal O_D G_D
 \{(A_L-D_f)S^{-1}z_{\rm body}+C F B S^{-1}z_{\rm body}\}.
 \tag{S.16}
$$

Independent atom inputs are mapped to zero by $H_c^{\rm cont}$. Thus $I-H_c^{\rm cont}$ is a genuine square operator on (S.16a), with the identity retained on the input atoms. It is the unprojected continuous kernel used to bound the W2C centre.

More precisely, let $P_f:\mathscr Z\to X_f$ be the actual normalized cell projection on the body and the identity on the193 atoms. WPS defines the published $G_f=P_f\mathcal O_DG_D$. If $\iota_{\rm body}$ includes a transformed head input with zero atoms, then the published nonsquare WJK map is

$$
 H_c^{\rm published}=P_f H_c^{\rm cont}\iota_{\rm body}.
 \tag{S.16b}
$$

A bound only on the right side after $P_f$ does not bound the unprojected map. Conversely the complete continuous-body/atomic kernel bounds imply the corresponding projected bound because $\|P_f\|=1$. No inverse is transferred by this inequality.

To solve $(I-H_c^{\rm cont})z=h$, put $h_0=S^{-1}h_{\rm body}$ and write the raw head as $h_0+x$. The correction $x$ satisfies the same homogeneous boundary conditions as (S.12)--(S.13) in its low rows, and

$$
 x'=A_Lx+(A_L-D_f)h_0+C F B(x+h_0).
 \tag{S.17}
$$

Use the same auxiliary equations with $f=B(x+h_0)$. This is exactly the1217-dimensional boundary problem, with a known bounded $L^2$ forcing depending on $h_0$. The given atom inputs are added unchanged at the output. **No radial derivative or endpoint value of the arbitrary $L^2$ input $h_0$ is taken.** The only endpoint values read are those of the reconstructed $H^1$ correction $x$.

Conversely any solution of (S.17) gives $z$ satisfying (S.16). For a fixed member, all finite coefficient maps and ODE inverses on this finite interval are bounded. If $M_{609}$ is nonsingular, variation of constants and its finite inverse give a bounded map from the entire $L^2$ forcing to the $H^1$ correction; the arbitrary input atom coordinates are added unchanged. If $M_{609}$ is singular, the preceding exclusion of auxiliary-only states gives a nonzero homogeneous low field $x$, and $z=\mathcal O_Dx$ is a nonzero kernel vector of $I-H_c^{\rm cont}$. Conversely a kernel vector reconstructs that same nonzero state system. These arguments prove both directions without differentiating the input.

There is also a compact-operator check: for fixed coefficients the source in (S.16) is bounded from $\mathscr Z$ to $L^2(I;E_L)$, and $G_D$ maps it boundedly into $H^1(I;E_L)$. The finite-component embedding $H^1\hookrightarrow L^2$ on this finite interval is compact. Multiplication by the bounded, boundedly invertible fixed weight $S$, including its inherited panel jumps, preserves compactness, and the193 atomic outputs are finite dimensional. Hence $H_c^{\rm cont}$ is compact on $\mathscr Z$, and $I-H_c^{\rm cont}$ is Fredholm of index zero. In particular absence of its kernel suffices for a bounded two-sided inverse. Therefore

$$
 \boxed{M_{609}\text{ nonsingular}
 \iff I-H_c^{\rm cont}:\mathscr Z\longrightarrow\mathscr Z
                 \text{ is a bounded two-sided isomorphism}.}
 \tag{S.18}
$$

This statement permits $\|H_c^{\rm cont}\|>1$, including a large nonnormal or skew contribution. It does not imply that the present matrix is nonsingular, or that a finite matrix built by independently projecting the centre is invertible. It is an equivalence for each fixed coefficient member; a family-uniform inverse bound still needs uniform endpoint transversality and quantitative propagation or Green-kernel bounds.

### The radial lift and normalizer remain explicit

Let $W_D:X_f\to\mathscr Z$ be the exact principal right lift from WIC: its body is $E_Nu-Zx_f$, and its atom entries are the original $d,b$. Then $P_fW_D=I$. Put

$$
 F_c=P_f H_c^{\rm cont}W_D,\quad
 J_\rho=Q_f\Delta_\rho,\quad
 E_c=J_\rho+(I-J_\rho)F_c.
 \tag{S.18a}
$$

These are the complete **finite** paired-centre factors occurring in WPS.11 and WPS.15. In particular

$$
 I-E_c=(I-J_\rho)(I-F_c).
 \tag{S.18b}
$$

Neither the principal radial-tail lift nor the rational-normalizer error has disappeared. Even knowing $T=(I-H_c^{\rm cont})^{-1}$ does not automatically invert $I-F_c$. The natural finite trial $T_f=P_fTW_D$ has the exact defect identity

$$
 T_f(I-F_c)=I+P_fT(I-W_DP_f)H_c^{\rm cont}W_D.
 \tag{S.18c}
$$

To prove it, expand $W_D(I-P_fH_c^{\rm cont}W_D)$ as $(I-H_c^{\rm cont})W_D+(I-W_DP_f)H_c^{\rm cont}W_D$ and use $P_fW_D=I$. A certified norm smaller than one for the last term would give a finite inverse by finite dimensionality; that norm is a separate unpaid target. The complete $I-J_\rho$ factor in (S.18b), both source rows and all endpoint/mean terms would still be needed before returning to the original finite test. Formula (S.18c) is a bridge with its error displayed, not a free conversion.

## 6. What an actual certification must still compute

The companion no-entry module `scripts/fourfold_codazzi_signed_centre_bvp_math.py` implements:

1. The exact coordinates and all21 nonzero state blocks of (S.7)--(S.10), as a block list rather than a dense1217-square allocation.
2. The complete coefficient adapter from the existing W2C context, with $A_{10},A_{01}$ taken as exact submatrices of $A_{11}$.
3. The whole608 left and609 right rows, including the physical mean, and the explicit isometric609-column initial injection.
4. The forcing in (S.17) for arbitrary ordinary $L^2$ input, preserving the direct input and the complete root/outer atoms.

These definitions are reusable exact code. They do not integrate an ODE or verify a determinant when imported.

A practical *diagnostic* may propagate the609-dimensional left solution subspace through the1217-dimensional sparse system, reorthogonalizing between panels. If $\Phi(R,a)N=QR$ with $R$ nonsingular, then (S.15) is nonsingular exactly when $B_RQ$ is nonsingular. Thus one need not multiply huge unstable scalar transfer factors merely to inspect transversality. Numerical QR and a floating-point singular value remain diagnostics until their full integration and rounding errors are certified. Whole-parent centre hulls define enclosures; their midpoints are not exact coefficient values.

A rigorous implementation must supply both a certified endpoint transversality and a whole inverse/source norm. For example two complete left/right frames give an exact Green representation, and verified frame residuals plus a global defect estimate can certify it. A large unweighted forward fundamental matrix norm is not an informative estimate of the mixed-boundary inverse. There is presently no supplied runtime claim or proof that the existing153 whole-parent hulls are narrow enough.

After a full bound for $T=(I-H_c^{\rm cont})^{-1}$, a **new continuous** preconditioning of the actual positive system could use

$$
 I-H_c^{\rm cont}-\mathcal R=(I-H_c^{\rm cont})(I-T\mathcal R).
 \tag{S.19}
$$

Here the left side must first be derived from the original complete zero-IVP operator by its true continuous principal inverse. The remainder $\mathcal R$ must contain the whole actual-family difference of W2C.26, the actual independent outer column, the complete outer Robin/mean/high-trace observation and every original source/port term in its original row. Only a complete bound $\|T\mathcal R\|<1$ proves that actual system invertible. Direct composition bounds are preferable to paying a large global $\|T\|$ unnecessarily. This is not a claim that the existing finite $e+3dt$ gate has become true.

The old finite $Q_fE_{\rm end}$ record is not automatically the continuous $G_D$ endpoint inverse. Any conversion must include the principal radial-tail and $\rho_2-\rho_*$ factors or evaluate the complete continuous endpoint map. Both original right-side rows remain through (S.19). Even success here would leave the original negative head, nu/metric Schur, exact nonlinear branch and geometry/matching obligations.

## 7. Why positivity alone does not already settle this same problem

The repository already contains the relevant geometric energy reductions; they should not be proved again:

- `results/R32-exact-darboux-and-full-scattering-interface.md` §§3,7 gives the self-adjoint Darboux equation for a genuine star-shaped immersion and the positive-cap ground-state transform. Its §11 explicitly retains the actual Robin/DN domain as an input.
- `results/R89-actual-physical-high-volume-coercivity.md` supplies a positive weak form and explicit high-frequency coercivity for its actual physical object, with the mean slots retained.
- `results/R133-supplement-passive-physical-positive-Dirac-and-complete-Schur.md` gives the exact passive physical half-density symmetrizer and a high-cone theorem; its margin involves $N\eta\sqrt K$ and does not give a low-frequency margin at $K=0$.

The current WVC operator is the moving linearization at the not-yet-solved Codazzi centre, with nonlocal primitive, physical mean and prescribed low/root plus high-stable boundary conditions. No previously supplied identity identifies that complete realization with a scalar positive Dirichlet problem. Establishing a residual-sensitive coordinate and boundary equivalence could open a shorter geometric route, but simply applying the scalar maximum principle would omit that substantive step. The finite-state result (S.18) stays within the already fixed WVC realization and does not require this missing bridge.

## 8. The first low-centre diagnostic is a separate, smaller computation

The additional no-entry source `scripts/fourfold_codazzi_low_centre_endpoint_diagnostic.py` uses only the full193-state raw low block $A_L$, with97 left-free directions and96 right-free directions. It defines a piecewise-constant comparison generator by the entrywise floating midpoint of each whole-panel coefficient enclosure and the floating midpoint of its true-length interval. It does not identify this generator with the actual centre. Forward and backward exponential propagation with thin QR yields a97-square terminal matrix and193-square matching frames at every panel boundary. These floating singular values are diagnostic quantities only; high feedback $CFB$, coefficient enclosure errors, between-panel transversality, full inverse norms and every original endpoint/port obligation remain unpaid. The first numerical execution has not yet occurred.
