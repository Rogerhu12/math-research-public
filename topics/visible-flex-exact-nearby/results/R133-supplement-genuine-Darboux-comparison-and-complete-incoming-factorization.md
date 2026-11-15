# R133 supplement: genuine Darboux comparison and complete incoming factorization

2026-11-15, visible-exact / phase_inverse.

**Proved exact comparison and typed positive-budget recipe.** The common radial potential can be removed from the first transport coefficient by an exact finite Darboux calculation. Its remaining root matrix has the full input-diagonal order $-4/3$, including the nonzero $\beta_n$. Its inhomogeneous remainder has two input orders of gain. This supplies a concrete route from the current genuine trial to the same first symbol as the original free-Airy construction.

The numerical input [PC actual](R133-supplement-actual-genuine-positive-Airy-cutoff-and-complete-strong-correction.md), public run 43740173506/1, is only the completed base-window correction
$H^{-4/3}\to L^2$ in the old-circle waist primitive-density pair, with both means. The new strict-cut comparison constants, additional strict propagation, trial first-neglected coefficients, incoming-coordinate cutoff, and finite cross maps below have not been numerically evaluated by that run.

## 1. Exact objects and normalization

Use the same real family $Q_\delta$, $|\delta|\le10^{-8}$, fixed physical $\eta_0$, and the same original root piece. Put
$$
n=4|j|\ge388,\quad \epsilon=\operatorname{sgn}j,\quad
\lambda=n^{2/3},\quad
K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix},\quad
E_{22}=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\tag{IN.1}
$$
The subscript in $K_T$ names the matrix and is not a derivative. The angular primitive remains
$I=\partial_\phi^{-1}(1-\Pi)$ with the full old mean $\Pi$.

Let $F_n$ be the exact free two-state Airy matrix A.10 and $\Psi_n$ the genuine two-state matrix A.19 of
[the common radial columns](R133-supplement-genuine-common-radial-reference-columns-and-two-source-ports.md).
Thus
$$
F_n'=\begin{pmatrix}0&1\\n^2T&0\end{pmatrix}F_n,\quad
\Psi_n'=\begin{pmatrix}0&1\\n^2T-V_n&0\end{pmatrix}\Psi_n,\quad
\Psi_n(0)=F_n(0)C_n,\quad
C_n=\begin{pmatrix}1&0\\\beta_n&1\end{pmatrix}.
\tag{IN.2}
$$
The first genuine column is the normalized terminal-Ai column. Neither it nor $C_n$ is replaced by a root-normalized free Ai column.

Write $\mathcal B=\mathcal B_n(T)$ for the exact regular solution
$$
\mathcal B+2T\mathcal B'=V_n,\qquad
\mathcal B(0)=V_n(0),\qquad
\mathcal B^{(p)}(T)=\frac12\int_0^1s^{p-1/2}V_n^{(p)}(sT)\,ds .
\tag{IN.3}
$$
The complete interval, complex product, parameter and frequency qualifications are those of the accepted common potential and RV conclusions. Every segment $sT$, $0\le s\le1$, must lie in that same paid disk. Primes here are canonical $T$ derivatives, never physical $r$ derivatives.

The leading amplitude is the original $w_0$. The first corrections satisfy the already proved whole-function identity
$$
w_1^V=w_1+\mathcal B K_Tw_0,\qquad
w^V=w_0+n^{-1}w_1^V .
\tag{IN.4}
$$
The original free $w_1$ is the P.8 first transport. It is used as an exact analytic identity, not reconstructed by rerunning its producer.

## 2. A finite Darboux matrix and its complete residual

For any free solution $Y$ define
$$
Y_d=Y-\frac{\mathcal B}{n^2}Y',\qquad
\mathcal D_n(T)=
\begin{pmatrix}
1&-\mathcal B/n^2\\
-T\mathcal B&1-\mathcal B'/n^2
\end{pmatrix}.
\tag{IN.5}
$$
The exact two-state value is
$(Y_d,Y_d')^t=\mathcal D_n(Y,Y')^t$. Direct differentiation gives
$$
(\partial_T^2-n^2T+V_n)Y_d
=-\frac{H_n(T)}{n^2}Y',
\qquad H_n=\mathcal B''+V_n\mathcal B.
\tag{IN.6}
$$
The coefficient of $Y$ is
$V_n-\mathcal B-2T\mathcal B'=0$. Equation (IN.6) retains the entire remaining derivative term. There is no inversion of an asymptotic series.

At the profile-row level,
$$
(Y_d,Y_d'/n)
=(Y,Y'/n)
\left[1-\frac{\mathcal B K_T}{n}
          -\frac{\mathcal B'E_{22}}{n^2}\right].
\tag{IN.7}
$$
Since $K_T^2=T\,1$, multiplication by (IN.4), in this order, gives
$$
\begin{split}
\left[1-\frac{\mathcal B K_T}{n}
          -\frac{\mathcal B'E_{22}}{n^2}\right]w^V
={}&w_0+n^{-1}w_1-n^{-2}R_2-n^{-3}R_3,\\
R_2={}&\mathcal B K_Tw_1^V+\mathcal B'E_{22}w_0,\qquad
R_3=\mathcal B'E_{22}w_1^V .
\end{split}\tag{IN.8}
$$
In particular every order-$n^{-1}$ common-potential contribution cancels exactly. The right side needs only the already completed genuine amplitudes and $\mathcal B$ to bound its two remainder amplitudes. It does not require a new computation of free $w_1$, its finite Taylor coefficients, or its original transport.

## 3. The actual root matrix is retained as an input multiplier

Set
$$
N_n=F_n(0)^{-1}\mathcal D_n(0)F_n(0),\qquad
D_n^{\rm root}=C_n^{-1}(C_n-N_n).
\tag{IN.9}
$$
No inverse of $N_n$ is used. In particular no new determinant gate for the Darboux matrix is needed.

A.5 gives each of the four free root values absolute value below one. Therefore the two root rows have Euclidean norms below $\sqrt2$, and the exact Wronskian gives
$$
\|N_n-1\|\le
2\pi\{|\mathcal B(0)|n^{-4/3}
            +|\mathcal B'(0)|n^{-2}\}.
\tag{IN.10}
$$
The accepted potential values copied by PC actual, `complete_positive_domain_conclusion.V` and `.VT`, are respectively below $276$ and $27000$ on the common product used here. Hence (IN.3) gives
$|\mathcal B(0)|<276$ and $|\mathcal B'(0)|<9000$.
Using $n^{2/3}>52$, $\pi<4$, A.20, and $\|C_n^{-1}\|<20/19$ proves the conservative rational bounds
$$
\|C_n-N_n\|<4096n^{-4/3},\qquad
\|D_n^{\rm root}\|<8192n^{-4/3}.
\tag{IN.11}
$$
For example the right side of (IN.10) is below
$8(276+174)n^{-4/3}$; the full shear adds less than
$138n^{-4/3}$ before multiplication by $C_n^{-1}$.

This is a matrix on the **input reference-column label** at each physical $n$. It is independent of $T,\phi$ and has both columns and both signs. With $\Lambda_j=(1+16j^2)^{1/2}$,
$$
\|D^{\rm root}:H^{-4/3}(\mathbb C^2)\to L^2(\mathbb C^2)\|
<16384.
\tag{IN.12}
$$
Indeed $\Lambda_j/n\le\sqrt{17}/4$ on the full nonzero fourfold spectrum. The constant includes the nonzero $\beta_n$.

A columnwise Hilbert–Schmidt argument would be invalid for this term: at exactly order $-4/3$ the weighted column squares need not sum. The diagonal-input multiplier estimate (IN.12) is the required argument. It neither deletes the physical output mean nor turns the analytic parameter $j^{-2}=0$ into the physical Fourier mean.

## 4. Exact inhomogeneous comparison, with both state rows

Define the full two-state error
$$
\mathcal E_n(T)=\Psi_n(T)-\mathcal D_n(T)F_n(T).
$$
Variation of constants using (IN.6) gives
$$
\begin{split}
\mathcal E_n(T)
={}&\Psi_n(T)D_n^{\rm root}\\
&+\int_0^T\Psi_n(T)\Psi_n(s)^{-1}e_2\,
       \frac{H_n(s)}{n^2}\,[F_n(s)]_{2,:}\,ds .
\end{split}\tag{IN.13}
$$
The integral has its actual orientation when $T<0$. Its inverse column is exactly
$$
\Psi_n(s)^{-1}e_2
=\frac{\pi}{\lambda}(-g_n(s),\widehat f_n(s))^t .
\tag{IN.14}
$$
Thus both genuine columns, the derivative row of the free matrix, the Wronskian and the whole source $H_n$ are present.

For a complete scalar estimate one may use the accepted positive-width product to bound $H_n$. For example
$H_0=\mathcal B_2+V_0\mathcal B_0$ on that product is valid, and the first two old-angle derivatives on a narrower strip cost
$H_0/\sigma$ and $2H_0/\sigma^2$. This is a new complete bound for the new product $H_n$, not an assertion that an old real-angle jet is holomorphic. The strict remaining strip and $T$-image margins are separate gates.

## 5. An all-output zero-order row bound from the original positive budget

At a fixed genuine negative circle let
$$
\mathcal S^V(w)c=\sum_j n^{1/6}\mathcal U_j^V(w_j)c_j .
$$
Use the same real fold, same frequency partition and same positive profile triples as V.11–18 of
[the genuine negative-column operator theorem](R133-supplement-genuine-negative-reference-column-operators-and-complete-source-ledger.md).

For one of its three phases $\Phi$, let $D_0,D_1,D_2$ be exactly the nonnegative Leibniz budgets V.17 and put
$$
B_2^\Phi=D_2/m_\Phi^2+D_1F_{2,\Phi}/m_\Phi^3.
$$
After the actual inverse-angle change, each Fourier coefficient row is bounded by
$\min(D_0,B_2^\Phi/(16\ell^2))$. Full row and column Schur sums therefore give
$$
\mathcal Z_\rho(w)=\rho^{-1/4}
\sum_\Phi m_\Phi^{-1/2}
   \left(D_0+\frac{\pi^2}{48}B_2^\Phi\right)
\ \ge\ \|\mathcal S^V(w):L^2\to L^2\|.
\tag{IN.15}
$$
The input is the complete two-column, two-sign direct sum; the output includes every Fourier coefficient and its mean. The phase-dependent input partition is the original circle-independent one. No angular derivative of a frequency selector is taken.

Let $a_J=2^{5/3}\Lambda_J^{-1/3}$. V.18's **underlying positive algorithm** has, for each phase, the expression
$$
\rho^{-1/4}C_\Phi
\left[
a_J\left(D_0+\frac{\pi^2}{48}B_2^\Phi\right)
+8B_2^\Phi(J^{-4/3}+3J^{-1/3})^{1/2}
\right].
\tag{IN.16}
$$
Every displayed coefficient and the tail term are nonnegative. Also V.16 implies
$C_{2,\Phi}\ge m_\Phi^{-1/2}=C_{0,\Phi}$, since
$C_{2,\Phi}^2\ge M_\Phi/m_\Phi^2\ge1/m_\Phi$.
Consequently $C_\Phi\ge C_{0,\Phi}$, and term by term
$$
\mathcal Z_\rho(w)
\le a_J^{-1}\mathcal A^{\rm alg}_\rho(w).
\tag{IN.17}
$$
This is positive-budget domination. It is **not** an inference that an arbitrary
$H^{-4/3}\to H^{-5/3}$ operator norm controls an $L^2\to L^2$ norm.

A saved upper may be used on the right only when its producer identity proves that it dominates this very expression on the same profile/fold/partition. The already read eighteen positive calibration coefficients are suitable with their original complete positive sum. A subsequently chosen minimum of other legal operator bounds is not automatically suitable: each candidate needs the same domination proof. No old profile, calibration, convolution or integral is reevaluated by (IN.17). The same envelope also bounds the free columns, which satisfy the stronger free estimates used in the proof of V.8–15.


There is also a direct readout of the original complete profile triples from those eighteen saved coefficients. Let
$\kappa_{\Phi,a,0},\kappa_{\Phi,a,1},\kappa_{\Phi,a,2}$ and
$\kappa_{\Phi,b,0},\kappa_{\Phi,b,1},\kappa_{\Phi,b,2}$ be the accepted upper endpoints for one phase, **with the common $\rho^{-1/4}$ removed**, in exactly the order recorded by C's
`complete_positive_linear_operator_conclusion`.
They bound the six coefficients of the underlying nonnegative algorithm, not the six values of an arbitrary norm-minimization output.

For the original $J_0=97$, put
$c_{\rm der}=a_{J_0}\pi^2/48+8(J_0^{-4/3}+3J_0^{-1/3})^{1/2}$.
The elementary inequalities $\Lambda_{97}<512$ and $97<125$ give
$$
a_{97}>1/4,\qquad c_{\rm der}>4,\qquad
0<m_\Phi\le1,\quad C_\Phi\ge1.
\tag{IN.17a}
$$
Here $m_\Phi\le1$ follows from the degree-one real circle lift and from its certified lower-endpoint meaning. Expanding V.17 in the six independent nonnegative amplitude inputs therefore proves, before any numerical evaluation,
$$
\begin{split}
\widehat{\mathbf p}_\Phi
={}&\left(
 \min\{4\kappa_{\Phi,a,0},\kappa_{\Phi,a,2}/4\},
 \kappa_{\Phi,a,1}/8,\kappa_{\Phi,a,0}/4\right),\\
\widehat{\mathbf q}_\Phi
={}&\left(
 \min\{4\kappa_{\Phi,b,0},\kappa_{\Phi,b,2}/4\},
 \kappa_{\Phi,b,1}/8,\kappa_{\Phi,b,0}/4\right).
\end{split}\tag{IN.17b}
$$
These are complete upper triples for the original $p_0,p_1,p_2$ and
$q_0,q_1,q_2$. For example
$\kappa_{\Phi,a,0}\ge a_{97}p_0$ and
$\kappa_{\Phi,a,0}\ge c_{\rm der}p_2$;
$\kappa_{\Phi,a,1}\ge2c_{\rm der}p_1$; and
$\kappa_{\Phi,a,2}\ge c_{\rm der}p_0$.
The same four inequalities hold for $q$. Each uses
$C_\Phi/m_\Phi^2\ge1$ and only retained nonnegative terms. The positive original tail is included in $c_{\rm der}$, not discarded or subtracted.

C's completed calibration takes a minimum of several independently proved upper bounds for each same positive algorithm coefficient. Every candidate bounds that same coefficient, so its final minimum retains all inequalities just used. This is different from taking the minimum of unrelated operator norms in (IN.17).
The new arithmetic in (IN.17b) is only a readout of already accepted bound numbers. No original profile, frequency partition, calibration or convolution is run again.

## 6. The new integral profiles and their actual phases

For the integral part of (IN.13), put $s=\tau T$, $0\le\tau\le1$, before differentiating any angular amplitude. The source contributes the exact factor
$$
\frac{\pi T}{\lambda n^2}H_n(\tau T).
\tag{IN.18}
$$
Its remaining three factors are a genuine output row at $T$, a genuine height column at $\tau T$, and a free derivative row at $\tau T$. The two internal frequency powers cancel exactly:
$$
\lambda^{-1}\,
(n^{-1/6}|\tau T|^{-1/4})
(n^{5/6}|\tau T|^{1/4})=1 .
\tag{IN.19}
$$
At central arguments, use the full central height bound and the derivative divided by $\lambda$ instead. Their product is uniformly bounded at $\tau=0$. There is no division by $\tau$ in the complete central estimate.

Decompose each of the three factors by its circle-independent central/two-branch partition. There are at most 27 product pieces. Their phases have the form
$$
\Phi_{\boldsymbol\sigma,\tau}
=X+c_{\boldsymbol\sigma}(\tau)\omega,\qquad
|c_{\boldsymbol\sigma}(\tau)|\le3,\qquad
\omega=\frac23(-T)^{3/2}.
\tag{IN.20}
$$
The sign convention absorbs $\epsilon$ into the branch label, so both physical input signs are retained. A valid new common phase gate is
$$
\inf X_\phi-3\sup|\omega_\phi|>0.
\tag{IN.21}
$$
Phase second and third derivative budgets use the corresponding full sums
$|X^{(k)}|+3|\omega^{(k)}|$. It would be incorrect to reuse only the old $X\pm\omega$ phase gap without checking (IN.21).

For each product piece, the full binomial rule applied to its three profile rows, $T$, $H_n(\tau T)$ and the supplied amplitude gives its two old-angle derivative budgets. V.6–15 supply the genuine/free profile derivative bounds at both arguments; their weighted derivatives remain uniform as $\tau\downarrow0$ because the central branch is retained. Apply the zero-order Schur formula (IN.15) to each complete product piece and integrate its nonnegative bound in $\tau$.

Denote the resulting positive functional by $\mathcal Z_{\rm int}(w)$, with the explicit $n^{-2}$ of (IN.18) removed. It bounds the full integral profile map on $L^2$, including both reference columns. The selector is used only in the norm estimate of the already differentiated exact expression; it creates no new radial interface or jump.


A closed all-$\tau$ implementation of this recipe is available. Set
$$
\widehat{\mathbf p}=\sum_\Phi\widehat{\mathbf p}_\Phi,\qquad
\widehat{\mathbf q}=\sum_\Phi\widehat{\mathbf q}_\Phi,\qquad
(\mathbf a\star\mathbf b)_k
=\sum_{\ell=0}^k{k\choose\ell}a_\ell b_{k-\ell},\quad 0\le k\le2.
\tag{IN.21a}
$$
Use the exact original profile qualification: the same $A_\pm$, bounds for
$\partial_\phi\log(-T)$ and $\partial_\phi^2\log(-T)$, the original full radial upper endpoint $R$, and the same potential and $N=388$.
For $0<\tau\le1$, the argument
$\tau T=-(\tau\rho)A(\rho,\phi)^{2/3}$ satisfies these same bounds with effective radial variable $\tau\rho\le R$.
The angular derivatives of $A(\rho,\phi)$ are taken at the same outer $\rho$, not at $\tau\rho$. Thus this applies the existing profile inequalities to a new radial argument satisfying their actual hypotheses; it does not identify two different physical fold values.

Consequently the two inner factors can both be bounded with their complete original common factors $(\tau\rho)^{-1/4}$:
$$
\|\partial_\phi^k(\text{inner height profile})\|
 \le n^{-1/6}(\tau\rho)^{-1/4}\widehat p_k,\qquad
\|\partial_\phi^k(\text{inner derivative profile})\|
 \le n^{5/6}(\tau\rho)^{-1/4}\widehat q_k .
\tag{IN.21b}
$$
These inequalities are for the central and demodulated high profiles, separately before the displayed sums; derivatives of the high exponential belong to (IN.20). The same complete envelope bounds the free inner derivative row. In particular the central pieces have not been removed. This deliberately uses a coarser integrable radial weight than the exact high-high cancellation (IN.19).

Let $\mathbf a,\mathbf b$ be the supplied complete angular triples of $w$, let
$\mathbf t$ bound $(T,T_\phi,T_{\phi\phi})$ in modulus, and let $\mathbf H$ bound the first two angular derivatives of $H_n(\tau T)$ uniformly over the whole segment. For example already paid canonical bounds give
$$
\begin{split}
H_0&=\mathcal B_2+V_0\mathcal B_0,\\
H_1&=(\mathcal B_3+V_1\mathcal B_0+V_0\mathcal B_1)y_0,\\
H_2&=(\mathcal B_4+V_2\mathcal B_0
       +2V_1\mathcal B_1+V_0\mathcal B_2)y_0^2\\
&\hspace{1.7em}
 +(\mathcal B_3+V_1\mathcal B_0+V_0\mathcal B_1)y_1 ,
\end{split}\tag{IN.21c}
$$
where $V_k$ and $\mathcal B_k$ are uniform canonical derivative bounds and
$y_0,y_1$ bound $T_\phi,T_{\phi\phi}$.
Factors $\tau,\tau^2$ have only been bounded by one. Their original complete potential disks and all-$sT$ qualifications must be checked; no real-angle bound is promoted to one of these canonical bounds.

On a fixed strict circle with $\rho\ge\rho_->0$, define the three nonnegative numbers
$$
\mathbf E=
2\pi\rho_-^{-3/4}\,
 \mathbf t\star\mathbf H\star
 (\widehat{\mathbf p}\star\mathbf a+
                    \widehat{\mathbf q}\star\mathbf b)
 \star\widehat{\mathbf p}\star\widehat{\mathbf q}.
\tag{IN.21d}
$$
The two inner factors in (IN.21b) contribute $(\tau\rho)^{-1/2}$, the outer normalized row contributes $\rho^{-1/4}$, and the Wronskian cancels the inner frequency factor as
$\lambda^{-1}n^{-1/6}n^{5/6}=1$.
The exact measure is $ds=T\,d\tau$, already included by $\mathbf t$.
The remaining scalar integral is exactly
$\int_0^1\tau^{-1/2}\,d\tau=2$.
This positive improper majorant is integrable even though it is unbounded at its single endpoint; the exact central integrand is regular there.

Let $m_3>0$ be the new lower gap (IN.21) and
$F_{2,3}=|X_{\phi\phi}|+3|\omega_{\phi\phi}|$.
Then the completely explicit choice
$$
\mathcal Z_{\rm int}(w)=m_3^{-1/2}
 \left[
 E_0+\frac{\pi^2}{48}
       \left(\frac{E_2}{m_3^2}
                 +\frac{E_1F_{2,3}}{m_3^3}\right)
 \right]
\tag{IN.21e}
$$
bounds the whole integral. Expansion of the sums in (IN.21a) gives every one of the at most27 product pieces with its full Leibniz coefficient. Each piece has the common phase gap and second-derivative bound just used, so triangle inequality and Schur give (IN.21e). There is no claim that different phases commute or are orthogonal.
Equations (IN.17b) and (IN.21a)--(IN.21e) require only new scalar products of immutable successful numbers, with no old profile evaluation and no quadrature or truncation in $\tau$.

Thus, for any supplied amplitude $w$ on the common domain,
$$
\|\mathcal S^{\mathcal E}(w):H^{-4/3}\to L^2\|
\le \mathcal Z_E(w):=
16384\,\mathcal Z_\rho(w)
+2(4J)^{-2/3}\mathcal Z_{\rm int}(w).
\tag{IN.22}
$$
The first term is (IN.12); the second is the input multiplier $n^{-2}$ with
$\Lambda_j^{4/3}/n^2<2(4J)^{-2/3}$.
The integral term is a new operator product, not the old single-profile calculation.
Its explicit all-$\tau$ envelope (IN.21a)--(IN.21e), phase gate and complete coefficient budgets are new scalar obligations.

## 7. Reconstruction of both physical rows: inhomogeneous terms are not lost

For a fixed reference-column label $\alpha\in\{1,2\}$, let
$e_\alpha=(\mathcal E_n)_{1,\alpha}$ and let
$\mathcal U^{\mathcal E,\alpha}(w)$ use its profile row
$(e_\alpha,(e_\alpha)_T/n)$. This row satisfies the genuine first-order profile equation with the additional profile row
$$
\mathfrak r_{n,\alpha}
=\left(0,\frac{H_n(T)}{n^3}[F_n(T)]_{2,\alpha}\right).
\tag{IN.23}
$$
In the identities below suppress $\alpha$; both labels are summed in the complete operator. The index is a reference-column input, not a physical mean.

Use the same full matrices $H_j^V$, $B_j=(H_j^V)^{-1}$ and $H_{D,j}^V$ as G.5, with
$y=T_\phi$ and $D=\partial_r-d\partial_\phi$. For
$$
h=\eta^{-1}B_jH_{D,j}^Vw,\qquad
g=Dw-\eta h_\phi
$$
one obtains the exact identities
$$
\begin{split}
D\mathcal U^{\mathcal E}(w)
-\eta\partial_\phi\mathcal U^{\mathcal E}(h)
={}&\mathcal U^{\mathcal E}(g)\\
&+e^{i\epsilon nX}\mathfrak r_n
       [(DT)w-\eta y h],\\
n\mathcal U^{\mathcal E}(w)
={}&\partial_\phi\mathcal U^{\mathcal E}(B_jw)
-\mathcal U^{\mathcal E}(\partial_\phi(B_jw))
-e^{i\epsilon nX}y\mathfrak r_nB_jw .
\end{split}\tag{IN.24}
$$
They follow by differentiating the two-state equation before applying any norm or frequency partition. They contain the full $B_j$, its derivatives, and the two extra inhomogeneous rows. The formulas do not treat $\mathcal E$ as a homogeneous reference column.

The physical reconstruction remains the same linear map
$$
\mathscr R f=(J(D_0-B_{\rm op})P_\perp f,\ P_\perp f).
\tag{IN.25}
$$
Applying (IN.24) gives the genuine G.11/G.20 reconstruction with its displayed extra source. There is no change of $J$, no deletion of its rank/mean terms, and no differentiation of an interval error.

The two density orders must be treated separately:

- Density zero is $n^{7/6}\mathcal U^{\mathcal E}(w_0)$. Its primitive and mean are bounded by (IN.24) and
$\mathcal Z_E(Bw_0)+\mathcal Z_E(\partial_\phi(Bw_0))$, with the extra $n^{-2}$ free-profile term in the second line retained. The identical rule is applied to $h_0$ and $g_0$ using their complete saved normalized columns.
- Density one is $n^{1/6}\mathcal U^{\mathcal E}(w_1^V)$. It uses $\mathcal Z_E(w_1^V)$ directly, and similarly $h_1=p_1/\eta$ and $g_1$. There is no need to invent $p_1'''$. The saved complete orders $0,1,2$ are sufficient for this row.

For density zero the first extra source in (IN.24), after multiplication by $n^{7/6}$, is exactly a free derivative-profile term with input factor $n^{-1}$. For density one it has factor $n^{-2}$. The free derivative profile is $n^{-5/6}Y_T$. Its remaining amplitude is
$H_n[(DT)w-\eta yh]_2$.
Apply the original complete $\mathcal A$ budget to this amplitude in
$H^{-5/3}$, then the original $J:H^{-5/3}\to H^{-2/3}$ and the outer full primitive–mean readout. The extra source is not part of $g$ and is not set to zero.

The other remainder sources use $L,B_{\rm op}$ in that same exact window. An $H^{-1}$ bound embeds contractively into $H^{-5/3}$ before these operations. Finally
$$
(I,\Pi):H^{-1}\longrightarrow L^2\oplus\mathbb C,\qquad
\|(I,\Pi)\|\le\sqrt{17}/4
\tag{IN.26}
$$
retains the mean column. At the strict cut, multiply by the true radial
$n_g=a_{\rm phys}^2/m^2$ and $T(q)$, $q=\sqrt{-K}$, with their paid lower and upper bounds. The resulting map is
$$
H^{-4/3}\longrightarrow
\bigl(L^2(\mathbb C^2)\oplus\mathbb C^2\bigr)_{\rm old\ circle\ density}.
\tag{IN.27}
$$
No raw $H^{-1}$ state is renamed a raw $L^2$ state.

The two explicit free amplitude terms $R_2,R_3$ of (IN.8) use the same reconstruction with the free $H^0$ and its full inverse, with no inhomogeneous row (IN.23). Their input factors are $n^{-2},n^{-3}$ before convolution. Their complete mixed derivative inputs may be read from M and the original leading/potential products. Neither the accepted M mixed jets nor an accepted amplitude derivative is recomputed.

Equations (IN.15)–(IN.27) define a finite positive recipe for a complete strict-cut comparison constant $C_{\rm Dar}$. All physical mean coordinates, root matrix columns, finite output modes and exact reconstruction terms belong to that constant.

## 8. Same first coefficient, with the full root and physical frame

At the strict cut P.22, or another explicitly paid strict cut in the same original root piece, subject to the common-profile qualifications and the strict phase gap (IN.21), (IN.8), (IN.11) and (IN.13) show that the genuine and original free first-transport trials differ in the complete class (IN.27). Their first order $n^{-1}$ terms agree. This includes both reconstructed curvature rows and the exact old primitive.

The strict first normalizer, the order-minus-two normalizer and any true density circle change must be applied in their original order, with their complete mean blocks. At a fixed strict cut their boundedness preserves the $4/3$ class. Its genuine wrong-branch order-minus-one cancellation is the one proved in P.23a and PF; it is not inferred by dropping a cross amplitude.

Thus the current genuine trial has the same first coefficient as the actual free P.8 construction. The root finite function and the selected scalar coefficient are the ones identified in the published full-family and PF proofs. No new old-ray, scalar finite-part or KAM arithmetic is needed for this identity. The complete common finite function is not replaced by its mean.

The current PC correction has exactly the same base strong input/output type at the waist. A bounded, correctly typed subsequent coordinate map preserves that strong class. Its norm, and the ordinary-source contribution required for a strict first-order transport comparison, still have to be charged. The numerical PC constant alone is not the total $C_E$ of P.24.

## 9. Exact stable-port cancellation and the finite complement

Let $\mathcal P_+$ be the stable-input column of the already selected full positive seven-port map. Retain its original head, mean, ordinary-source and exterior columns independently. Let $S_{\rm tr}^{Y}$ be the actual stable root trace, in the original $Y=N^{-1}Z$ frame, of the density-normalized genuine trial and its corrected columns. The PC correction has zero stable trace, so this trace is unchanged by correction.

For precisely the homogeneous high problem of PC.35, with its specified zero supplied head and other positive inputs, the corrected high columns satisfy
$$
\mathcal C_H=\mathcal P_+ S_{\rm tr}^{Y}.
\tag{IN.28}
$$
The finite equations and both independent means remain separate equations. If other positive inputs $p$ are supplied, their full additional term $\mathcal P_{\rm rest}p$ remains; it is not part of the factor canceled below.

The trace is nonzero. The actual input density normalization is $N_{\rm in}^{7/6}$, whereas the $Y$ trace itself has principal order $N^{1/6}$, exactly as in PC.35. The order-zero stable map used in P.20 is the ordered map
$S_{\rm nat}=N_{\rm out}S_{\rm tr}^{Y}N_{\rm in}^{-7/6}$.
Here $N_{\rm out}$ is on the declared high stable root coordinates; no mean is divided by zero.

Writing $S_{\rm tr}$ for this same actual right coordinate factor, the common factor cancels only on common natural domains:
$$
(\mathcal B_o S_{\rm tr}^{-1})
(\mathcal B_i S_{\rm tr}^{-1})^{-1}
=\mathcal B_o\mathcal B_i^{-1}.
\tag{IN.29}
$$
One does not commute $S_{\rm tr}$ through a Fourier projection, a density map, or $N^{7/6}$. In particular the output factor in $S_{\rm nat}$ is on its stated side. The bounded order-zero inverse and the corresponding weighted natural-domain inverse are different descriptions of this same ordered map, not an unweighted $L^2$ bound for $S_{\rm tr}^{Y}$.

The original P.19–21 and the full-family B theorem (immutable blob `e561b822673bbce15c1391ee851fb93d4143d43e`) give the leading stable diagonal of $S_{\rm nat}$
$$
c_n=
\frac{\operatorname{Ai}(0)-(\lambda_*/\eta_*)\operatorname{Ai}'(0)}
     {\sqrt{1+\widetilde p_n}}>1/25,\qquad \widetilde p_n<66.
\tag{IN.30}
$$
The genuine root change (IN.11) and the unchanged first-transport root normalization preserve this leading diagonal. The original finite analytic root construction then gives an invertible compression of $S_{\rm nat}$ after a sufficiently large finite cutoff, and hence the corresponding stable-coordinate isomorphism on its ordered natural domains. A quantitative chosen cutoff must include its actual stable-error constant in the required Sobolev windows; (IN.30) alone does not prove invertibility at 97.

Every exposed finite stable coordinate is retained as an actual positive Poisson port. This subtraction requires no inverse for the finite Schur block. All finite/high cross maps and both means remain. Equation (IN.29) supplies a cancellation of a common coordinate factor in the complete relation, not an excuse to discard its finite cross blocks.

## 10. A complete two-space incoming gate

Work in one fixed common branch chart after the leading invertible density multipliers and circle maps have been explicitly separated. Let the normalized true maps be
$$
B_i=1+K_i+E_i,\qquad B_o=1+K_o+E_o,\qquad
K_\alpha=M_{c_\alpha}I,\qquad
E_\alpha:H^{-4/3}\to L^2 .
\tag{IN.31}
$$
All complete normalizer, mean and coordinate remainders must be inside $E_\alpha$ or retained as finite rows before using this display. This notation does not grant their norms.

Let $P=P_{\{|j|\ge J\}}$ in this chart, and
$$
D=P+P(K_i+E_i)P .
$$
If $m_{i,t}$ bounds multiplication by $c_i$ on $H^t$, define
$$
\chi_t(J)=\frac{m_{i,t}}{4J}+C_{E_i}\Lambda_J^{-4/3},
\qquad t=0,-4/3 .
\tag{IN.32}
$$
Then $\chi_0<1$ and $\chi_{-4/3}<1$ imply
$$
\|D^{-1}\|_{H^t\to H^t}\le(1-\chi_t)^{-1}.
\tag{IN.33}
$$
For $t=0$, the small factor for $E_iP$ is on its input. For $t=-4/3$, it is on the high output $PE_i$. These are distinct embeddings; both are required. The two inverses agree on their common dense domain.

Put $\Delta K=P(K_o-K_i)P$ and $A=P(K_i+E_i)P$. The exact compressed identity is
$$
P B_o P D^{-1}-(P+\Delta K)
=\{P(E_o-E_i)P-\Delta K A\}D^{-1}.
\tag{IN.34}
$$
A principal rotation or scalar Maslov factor may be put on the left only in a chart where it actually commutes with $P$. No low physical projection is silently identified with that chart projection.

Let $m_{\Delta,t}$ be the complete multiplication norms of $c_o-c_i$ and $\gamma_J=\Lambda_J/(4J)$. Then
$$
\|\Delta K\,P K_iP\|_{H^{-4/3}\to L^2}
\le
\gamma_J^2m_{\Delta,\,2/3}m_{i,\,-1/3}\Lambda_J^{-2/3},
\tag{IN.35}
$$
because the two primitives give two gains, and the final high embedding pays $2/3$. Also
$$
\|\Delta K\,P E_iP\|_{H^{-4/3}\to L^2}
\le \frac{m_{\Delta,0}}{4J}\,C_{E_i}.
\tag{IN.36}
$$
Thus a complete strong bound for (IN.34) is
$$
\frac{C_{E_o}+C_{E_i}
+\gamma_J^2m_{\Delta,2/3}m_{i,-1/3}\Lambda_J^{-2/3}
+(4J)^{-1}m_{\Delta,0}C_{E_i}}
 {1-\chi_{-4/3}(J)} .
\tag{IN.37}
$$
If the exact signed difference $E_o-E_i$ has its own complete bound it may replace the first two summands. Subtracting their numerical upper bounds is not allowed.

The genuine leading multipliers and circle maps multiply this estimate on the appropriate output $L^2$ and input $H^{-4/3}$ sides. Their norms are not one by declaration. The same applies to the final exact CN/EN normalizer and its full mean commutators.

## 11. The finite equations are part of the same relation

Let $F=1-P$ on the full already-declared coordinate space, including the original finite head and mean. Write the true incoming and outgoing maps in these two blocks. Solving only the high incoming row gives, with finite input $\xi_F$,
$$
\xi_H=D^{-1}(b_H-B_{i,HF}\xi_F).
$$
The remaining three equations are exactly
$$
\begin{split}
b_F={}&(B_{i,FF}-B_{i,FH}D^{-1}B_{i,HF})\xi_F
                 +B_{i,FH}D^{-1}b_H,\\
o_H={}&B_{o,HH}D^{-1}b_H
 +(B_{o,HF}-B_{o,HH}D^{-1}B_{i,HF})\xi_F,\\
o_F={}&B_{o,FH}D^{-1}b_H
 +(B_{o,FF}-B_{o,FH}D^{-1}B_{i,HF})\xi_F .
\end{split}\tag{IN.38}
$$
No finite equation has been solved or set to zero. In particular the first coefficient in the second line is a high block of this bordered relation; it is not, by itself, a full high BVP with all finite incoming coordinates fixed to zero.

A finite rank map $\sum_\alpha u_\alpha\ell_\alpha$ is charged by
$$
\sum_\alpha\|u_\alpha\|_{L^2}
              \|\ell_\alpha\|_{(H^{-4/3})^*}.
\tag{IN.39}
$$
The dual row window is $H^{4/3}$. A mere $L^2$ row bound is insufficient.
The physical degree-96 projector and the projector in a true ray/KAM angle need not commute. Their complete cross maps are retained by (IN.38)–(IN.39), including both means.

## 12. The next scalar computations, without repeating completed work

The first new scalar package should evaluate the strict-cut Darboux comparison, not rerun PC. Its inputs are the accepted common potential and $\mathcal B$ bounds, original leading/inverse products, the complete saved genuine amplitudes and M mixed jets, the eighteen original positive coefficients, and the true local geometric/frame coefficients. Its new work is precisely:

1. The new all-$\tau$ product profile and the phase family (IN.20), including the strict gap (IN.21), with full source $H_n$.
2. The complete positive reconstruction of (IN.24), both density orders and all inhomogeneous additions, plus the two explicit amplitudes $R_2,R_3$.
3. The complete strict-cut density/frame and finite-row constants needed by (IN.27) and (IN.39).
4. The free trial's first-neglected Airy/reconstruction coefficient at that cut, using the existing exact finite amplitudes and a complete analytic remainder formula; it must include the full family's already proved root and first-symbol identities. No previously completed amplitude or free-transport producer is called.

There is a separate radial interface: the P.22 near-root strict cut is not the SP actual cut $r_+-1/200$. A permitted minimal continuation evaluates only the previously unused tail interval between these two cuts by the complete SP primitive–mean equations, then composes in the original orientation with the already completed SP prefix. Its inputs are exact old whole rows on that tail, with all one-sided physical seams and compact-metric qualifications. It neither reruns the old SP prefix nor reinterprets the old four-state $H^1$ flow as an $L^2$ flow.

Finally the strict first-order parametrix remainder, true incoming coefficient norms, stable spanning gate, leading coordinate factors and complete finite rows enter (IN.31)–(IN.39). Their actual constants must be reported before a numerical full-return bound or a selected high inverse is claimed. The already completed PC correction is copied at its own exact base-window type, with its nonzero trial stable trace intact. The theorem makes no assertion for all $s$, no inverse at cutoff 97, no finite Schur closure, and no full nonlinear branch.
