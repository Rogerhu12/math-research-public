# R144 supplement: complete residual and operator fees at the selected-metric compact centres

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved, uniformly for every real $|\delta|\le10^{-10}$.**
The exact-mean compact centre of
[SM](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md)
has a complete nonmean moving residual
$R_\delta=(F_u+\partial_\phi Q_u,F_v+\partial_\phi Q_v)$ with

$$
 \begin{array}{c|cccc}
  &\|F_u\|_2&\|Q_u\|_2&\|F_v\|_2&\|Q_v\|_2\\ \hline
 \hbox{strict upper}
  &1.107\,10^{-7}&1.705\,10^{-6}
  &7.469\,10^{-8}&1.594\,10^{-6}.
 \end{array}
 \tag{SC.1}
$$

These are whole-$[0,25/8]$ bounds with normalized angular measure
and actual radial measure $dr$. The second residual has exactly
zero moving mean. All original nonmean interfaces, the cutoff
derivative, the original raw residual and the intrinsic metric
change are retained. In particular no ordinary metric source is
discarded by moving its mean to a different equation.

At the same intrinsic metric, the complete physical differential
differs from the original selected-family differential by a
first-order operator whose finite193 body fee is less than
$0.002634$ on $[0,9/10]$. Its complete high-to-low shell fee is
less than $0.007711$. These are actual operator differences in
ordinary physical moving $L^2$ units, not an inverse theorem or
a change of boundary conditions.

No new native rows, Fourier products, quadratures, old residuals
or scientific targets are computed. The proof transforms the
already completed LC and selected-parameter scalar conclusions.

## 1. Exact state and the old complete scalar inputs

Write the original raw state as $(u,v)$, with

$$
 m=\langle v\rangle,\quad w=v-m,\quad z=w/m,\quad j=1+z,
 \quad U=\langle u^2\rangle,\quad Z=\|z\|_2.
 \tag{SC.2}
$$

The $Z$ in this formula is a scalar norm and is distinct from the
old degree-96 selected-family response, denoted $Z^{\rm sel}$ below.
Keep the exact original $\alpha,\eta_0,\nu_0$ and raw candidate of
[LC](R144-supplement-localized-full-state-C0-and-compact-source-receivers.md).
Let $\mathcal I=\partial_\phi^{-1}P_{\ne0}$ on the fourfold circle.
Use $K=K_{\nu_0}$, $\gamma=\gamma_{\nu_0}$ and
$d_0=-\beta\mathcal I(u^2+Km^2j^2)$.

For the unique root $\xi=\xi(\delta)$ of SM put

$$
 \begin{gathered}
 e=\xi\chi,\qquad\lambda=1+e,\qquad j_\xi=1+\lambda z,
 \qquad M=m_\delta,\qquad \widetilde Q_\delta=(u,Mj_\xi),\\
 K_\delta=e^{-\delta\chi}(K+\delta T\chi'),\qquad
 \gamma_\delta=\gamma e^{\delta\chi/2},\qquad
 T=\frac{\beta}{2E_{\nu_0}},\\
 |M-m|\le b_n:=2.464\,10^{-7},\qquad
 |\xi|<r_n:=1.75\,10^{-11}.
 \end{gathered}
 \tag{SC.3}
$$

The functions $a,\beta$ and the physical raw $u,m,w$ remain fixed.
The true scalar equation is

$$
 M'=\beta M\{1-U-K_\delta M^2\langle j_\xi^2\rangle\},
 \qquad [M]_i=0.
 \tag{SC.4}
$$

Both endpoint mean values are the original prescribed values.
This equation, including its continuous mean and the actual
$K_\delta$, is needed in the residual calculation.

The full LC output from public run $45797426031/1$ has SHA256
60ac20418b405281a3150216e45f7bffd0e73b7625ccc8c383cf4204968b5748.
Its complete upper endpoints give

$$
 \begin{gathered}
 \|u\|_{A^0}<0.628,\quad \|w\|_{A^0}<0.986,\quad
 1.068<|m|<6,\quad \|w\|_2^2<0.474,\\
 E_u<3.214\,10^{-8},\qquad E_v<6.269\,10^{-8},\\
 \|f_u^{\,o}\|_2<8.105\,10^{-8},\quad
 \|q_u^{\,o}\|_2<1.815\,10^{-6},\quad C_v^{\,o}<1.190,\\
 \|f_\chi^{\,o}\|_2<9.757\,10^{-5},\qquad
 \|q_v^{\,o}\|_2<1.695\,10^{-6}.
 \end{gathered}
 \tag{SC.5}
$$

Here the superscript $o$ refers to the old LC positive receiver
functions, with the exact saved radii $b_o,r_o$. They are neither
new residuals nor lower bounds for residual values.
The two raw residual bounds are $E_u=\|R_u\|_2$ and
$E_v=\|R_v\|_2$ at $\nu_0$.

The other input is the complete scalar conclusion of
[D-actual](R133-supplement-actual-selected-parameter-core-scalar-fees-and-collar-jets.md),
public run $43713242980/1$. Its embedded small scientific result
has SHA256
55076dbd11edf8aaae03d27d53e5cbf5bc8bffc8911568fecedce33d1d7bd80b;
the containing execution receipt has SHA256
6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071.
The original positive functions $M_0^o,M_1^o$ are exactly (D.6)
with $Q_0^\#=7,Q_1^\#=6,E_0^o=19d,E_1^o=83d,E_m^o=19d$,
$d=10^{-10}$. The producer uses these global constants in
its function selected_parameter_fees. It did not replace them
by a smaller signed response value.

On the compact metric window $C=[1/20,9/50]$, the same saved
conclusion already gives

$$
 \|M_0^o\|_{L^2(C)}<1.614208\,10^{-8},\qquad
 \|M_1^o\|_{L^2(C)}<3.683076\,10^{-9}.
 \tag{SC.6}
$$

These are the saved complete compact integrals. No full integral
is subtracted from another upper bound to obtain them.

## 2. Exact residual identities with the metric change included

Define radial coefficient differences

$$
 \begin{aligned}
 \Delta S&=K_\delta M^2j_\xi^2-Km^2j^2,\\
 A&=K_\delta M^2\lambda-Km^2,\qquad
 B=K_\delta M^2\lambda^2-Km^2,\\
 C_\gamma&=\gamma_\delta K_\delta M^2\lambda-\gamma Km^2.
 \end{aligned}
 \tag{SC.7}
$$

Thus

$$
 \Delta S=(K_\delta M^2-Km^2)+2Az+Bz^2,\qquad
 \mathcal I\Delta S=2A\mathcal Iz+B\mathcal I(z^2).
 \tag{SC.8}
$$

Use the residual sign of CS: $R=Q_r-F(Q,\nu)$, so the
residual is added to the right side of the moving equation.
Then the complete changed residual is exactly

$$
 \boxed{
 \begin{aligned}
 F_u&=R_u+\beta\langle\Delta S\rangle u,\\
 Q_u&=\beta u\mathcal I\Delta S-C_\gamma z,\\
 F_v&=\frac{M\lambda}{m}(R_v-jR_0)+M\xi\chi' z,
              \qquad R_0=\langle R_v\rangle,\\
 Q_v&=M\{e(d_0-\gamma u)+
                 \beta\mathcal I\Delta S\,j_\xi+
                    (\gamma_\delta-\gamma)u\}.
 \end{aligned}}
 \tag{SC.9}
$$

For the first row, subtraction of the two physical moving
equations gives
$R_u+\beta\mathcal I\Delta S\,u_\phi
+\beta u\Delta S-\partial_\phi(C_\gamma z)$.
Use
$(\mathcal I\Delta S)_\phi=\Delta S-\langle\Delta S\rangle$
to obtain the first two identities.

For the second row the raw density obeys the exact equation

$$
 j_r=\partial_\phi(d_0j-\gamma u)+(R_v-jR_0)/m.
 \tag{SC.10}
$$

The new mean equation (SC.4) implies that the new second
residual is $M$ times
$\partial_rj_\xi-\partial_\phi(d_\delta j_\xi-\gamma_\delta u)$,
where $d_\delta=d_0-\beta\mathcal I\Delta S$.
Now

$$
 \begin{aligned}
 \partial_rj_\xi&=\lambda j_r+\xi\chi'z,\\
 \lambda d_0j-d_\delta j_\xi&=
                    e d_0+\beta\mathcal I\Delta S\,j_\xi,\\
 \gamma_\delta-\lambda\gamma&=
                    (\gamma_\delta-\gamma)-e\gamma .
 \end{aligned}
 \tag{SC.11}
$$

These identities prove the last two lines of (SC.9).
In particular the true metric forcing in the mean equation
has been used before multiplying by the new density.
It is not legitimate to keep the old mean equation and omit
that forcing. Equivalently, in a calculation at fixed $\nu_0$
the additional scalar mean residual
$-\beta(K_\delta-K)M^3\langle j_\xi^2\rangle$ cancels precisely
the second-row ordinary mean part of the metric change.

Every ordinary function in (SC.9) has zero angular mean:
the first row is odd, and
$\langle R_v-jR_0\rangle=\langle z\rangle=0$.
Thus the second residual has zero mean exactly on every piece,
as well as no mean jump. No division of an unknown response
by the density or change of angular coordinate is made.

## 3. Transforming the already completed five LC receivers

First split (SC.9) into its fixed-$K,\gamma$ CS expression with
the new $M,\xi$, plus its explicit metric difference.
For this algebraic split it is not necessary that $M$ solve the
old fixed-metric mean equation; (SC.9) was already established
using the correct equation (SC.4).

The exact saved radii satisfy

$$
 b_n<0.938\,b_o,\qquad r_n<8.2\,10^{-7}r_o.
 \tag{SC.12}
$$

The LC majorants are positive polynomials in $b,r$.
In detail, $|K|b(2|m|+b)$ scales by at most $0.938$;
$|K|(|m|+b)^2r\chi$ and
$|K|(|m|+b)^2(2r\chi+r^2\chi^2)$ do also.
The factors $|m|+b$, $1+r\chi$ and $c_v$ decrease.
Consequently the fixed-metric pieces satisfy

$$
 \begin{gathered}
 \|f_u^{\,n}\|_2\le0.938\|f_u^{\,o}\|_2,\quad
 \|q_u^{\,n}\|_2\le0.938\|q_u^{\,o}\|_2,\quad
 \|q_v^{\,n}\|_2\le0.938\|q_v^{\,o}\|_2,\\
 C_v^{\,n}\le C_v^{\,o},\qquad
 \|f_\chi^{\,n}\|_2\le8.2\,10^{-7}\|f_\chi^{\,o}\|_2
                                      <8.001\,10^{-11}.
 \end{gathered}
 \tag{SC.13}
$$

This includes every old row and the exact old $\chi'$ square
mass. In particular the small control value is used only for
the actual centre, not for an unjustified derivative estimate.

## 4. Paying the intrinsic metric difference from old positive budgets

Put $\widetilde v=Mj_\xi$, $v_c=\widetilde v-M$,
$\Delta K=K_\delta-K$, $\Delta\gamma=\gamma_\delta-\gamma$.
The additional ordinary and flux functions in (SC.9) are

$$
 \begin{aligned}
 f_u^\nu&=\beta\Delta K\langle\widetilde v^2\rangle u,\\
 q_u^\nu&=\beta\Delta K\,u\mathcal I(\widetilde v^2)
       -(\gamma_\delta K_\delta-\gamma K)M v_c,\\
 q_v^\nu&=\beta\Delta K\,\widetilde v\mathcal I(\widetilde v^2)
       +M\Delta\gamma\,u .
 \end{aligned}
 \tag{SC.14}
$$

There is no additional second ordinary function. All three
functions in (SC.14) vanish identically off $C$.
For every $r$ and all allowed $\delta$, (SC.3)--(SC.5) imply

$$
 \begin{gathered}
 |M|<6.000001,\qquad
 \|v_c\|_{A^0}<0.987,\qquad \|v_c\|_2<0.690,\qquad
 \|\widetilde v\|_{A^0}<7,\\
 \|\mathcal I(\widetilde v^2)\|_2
 \le\frac{(2|M|+\|v_c\|_{A^0})\|v_c\|_2}{4}<2.25.
 \end{gathered}
 \tag{SC.15}
$$

The primitive estimate retains both $2Mv_c$ and
$v_c^2-\langle v_c^2\rangle$.

Use the original positive coefficient bounds $k_\Delta,J_\Delta$
of D.5 on the same complete intrinsic rows. They bound
$|\Delta K|$ and the full Euclidean matrix norm of
$\gamma_\delta J(K_\delta)-\gamma J(K)$, respectively.
In particular both $|\Delta\gamma|$ and
$|\gamma_\delta K_\delta-\gamma K|$ are bounded by $J_\Delta$.
The original functions satisfy pointwise

$$
 M_0^o\ge147|\beta|k_\Delta,\qquad
 M_1^o\ge7J_\Delta .
 \tag{SC.16}
$$

These terms are already present in (D.6); keeping the other
positive terms only increases its valid upper bound.
Combining (SC.14)--(SC.16) gives

$$
 \begin{aligned}
 \|f_u^\nu(r)\|_2&<0.157M_0^o(r),\\
 \|q_u^\nu(r)\|_2&<0.010M_0^o(r)+0.60M_1^o(r),\\
 \|q_v^\nu(r)\|_2&<0.108M_0^o(r)+0.54M_1^o(r).
 \end{aligned}
 \tag{SC.17}
$$

For example the first ratio is bounded by
$0.628(6.000001^2+0.690^2)/147<0.157$.
The two first-flux ratios are
$0.628(2.25)/147<0.010$ and
$6.000001(0.690)/7<0.60$.
For the second flux use
$7(2.25)/147<0.108$ and
$6.000001(0.628)/7<0.54$.
Using the saved compact integrals (SC.6) therefore proves

$$
 \|f_u^\nu\|_2<2.535\,10^{-9},\quad
 \|q_u^\nu\|_2<2.372\,10^{-9},\quad
 \|q_v^\nu\|_2<3.733\,10^{-9}.
 \tag{SC.18}
$$

The completed small coefficient fees, rather than new intrinsic
suprema or quadratures, pay the entire intrinsic change.

## 5. Whole nonmean residual, all joins and finite carrier

The exact projection bound
$\|g-j\langle g\rangle\|_2\le\sqrt{1+Z^2}\|g\|_2$
is already part of CS and LC. Hence (SC.5), (SC.13) and
(SC.18) imply

$$
 \begin{aligned}
 \|F_u\|_2
 &<3.214\,10^{-8}+0.938(8.105\,10^{-8})
                                  +2.535\,10^{-9},\\
 \|Q_u\|_2&<0.938(1.815\,10^{-6})+2.372\,10^{-9},\\
 \|F_v\|_2&<1.190(6.269\,10^{-8})+8.001\,10^{-11},\\
 \|Q_v\|_2&<0.938(1.695\,10^{-6})+3.733\,10^{-9}.
 \end{aligned}
 \tag{SC.19}
$$

These inequalities give (SC.1), with each comparison made
against the full saved interval endpoint.

The exact centre still has moving degree 32. Each ordinary
and flux source in (SC.9) has moving degree at most 96 and
has no constant mode. Therefore the physical frequencies
are $4,\ldots,384$. For every $0\le s\le1$,
$\|F+\partial_\phi Q\|_{H^{-s}}\le4^{-s}\|F\|_2+
384^{1-s}\|Q\|_2$. In particular

$$
 \begin{array}{c|c}
 \hbox{complete source norm}&\hbox{strict upper}\\ \hline
 L^2_rH^{-2/3}_\phi\text{ first row}&1.244\,10^{-5}\\
 L^2_rH^{-2/3}_\phi\text{ second row}&1.162\,10^{-5}\\
 L^2_rH^{-1}_\phi\text{ second row}&1.613\,10^{-6}\\
 (H^{-2/3},H^{-2/3})\text{ Euclidean pair}&1.703\,10^{-5}\\
 (H^{-2/3},H^{-1})\text{ Euclidean pair}&1.255\,10^{-5}.
 \end{array}
 \tag{SC.20}
$$

These are norms in the same moving angle. A physical-angle
composition requires its own density and composition estimate.
The ordinary full residual can also be consumed, without
forgetting the angular derivative: its first and second
$L^2_{r,\phi}$ rows are respectively below
$6.549\,10^{-4}$ and $6.122\,10^{-4}$, and its Euclidean pair
is below $8.965\,10^{-4}$. These deliberately coarser values
use the valid factor 384, not a unit divergence multiplier.

At every one of the original 6143 interfaces,

$$
 [\widetilde u]_i=[u]_i,\qquad
 [\widetilde v]_i=M\lambda[z]_i,\qquad
 \langle[\widetilde v]_i\rangle=0.
 \tag{SC.21}
$$

The LC jump majorant is monotone in $b,r$, so the complete sums
still satisfy

$$
 \sum_i\|[\widetilde u]_i\|_{A^0}<3.370\,10^{-13},\qquad
 \sum_i\|[\widetilde v]_i\|_{A^0}<2.691\,10^{-12}.
 \tag{SC.22}
$$

Their exact individual traces remain the affine jump sources;
the sums do not replace them by zero. The compact support of
the metric corrections in (SC.14) does not localize the whole
residual or the original mean change. Degree 96 of this
particular forcing does not truncate the unknown correction
or its response after any inverse or return map.

## 6. Actual same-metric full differential fees

Let $Q_\delta^{\rm sel}=Q_0+\delta Z^{\rm sel}$ be the original
repaired degree-96 family, at the same $\nu_\delta$.
SM gives

$$
 \begin{gathered}
 \|\widetilde Q_\delta-Q_\delta^{\rm sel}\|_{A^0,\rm pair}
       <E_0:=4.760\,10^{-7},\\
 \|\partial_\phi\widetilde Q_\delta-
             \partial_\phi Q_\delta^{\rm sel}\|_{A^0,\rm pair}
       <E_1:=1.264\,10^{-6},\\
 |\langle\widetilde v_\delta-v_\delta^{\rm sel}\rangle|
       <E_m:=2.484\,10^{-7}.
 \end{gathered}
 \tag{SC.23}
$$

For the last line use $b_n+19d+3.861\,10^{-18}<E_m$.
The actual complete response-repair summary
[43597921732/1](../notes/response_repair_source_ci/run-43597921732-1-complete-known-response-centre-repair/evidence/complete-known-response-centre-repair-source-summary.json),
also quoted immediately before D.5, supplies the stricter
raw bounds $6.406213$ and $5.437241$, with complete repair
fees $3.861\,10^{-18}$ and $1.970\,10^{-17}$.
Consequently the original response bounds give explicitly

$$
 \begin{aligned}
 \|Q_\delta^{\rm sel}\|_{A^0,\rm pair}
  &<6.406213+3.861\,10^{-18}+19d<7,\\
 \|\partial_\phi Q_\delta^{\rm sel}\|_{A^0,\rm pair}
  &<5.437241+1.970\,10^{-17}+83d<6.
 \end{aligned}
 \tag{SC.23a}
$$

The strict spare margins in these original complete bounds
are used here; a bound $7$ for $Q_0$ alone would not prove
a bound $7$ after adding $\delta Z^{\rm sel}$.
Thus the state-change part of the full D.4 differential is
bounded by

$$
 \begin{aligned}
 \widehat M_1
 &=|\beta|K_+(14E_0+E_0^2)/4+G_+K_+E_m,\\
 \widehat M_0
 &=3|\beta|K_+(14E_0+E_0^2)
   +\frac{|\beta|K_+}{2}\{6E_0+(7+E_0)E_1\}
   +G_+K_+E_1 .
 \end{aligned}
 \tag{SC.24}
$$

Here $G_+,K_+$ are the same old positive bounds valid for
every $\nu_\delta$. There is no new intrinsic difference
between the two states in this comparison.
For every angular $H^1$ input, with its genuine even mean,

$$
 \|[DF(\widetilde Q_\delta,\nu_\delta)
       -DF(Q_\delta^{\rm sel},\nu_\delta)]h\|_2
 \le\widehat M_1\|h_\phi\|_2+\widehat M_0\|h\|_2 .
 \tag{SC.25}
$$

This is the complete physical differential, including
$-2\beta Q_\phi\mathcal I(uh_1+Kvh_2)$,
the principal $m$ term, and the rank-one term
$\gamma\langle h_2\rangle J(K)Q_\phi$.
The latter is paid by $G_+K_+E_1$; it is not removed by
the zero mean of the centre residual.
The scalar mean graph does not make the response's independent
moving mean vanish.

Put $e_0=19d,e_1=83d$ and $\Lambda=251$.
Exact rational inequalities give

$$
 \begin{gathered}
 14E_0+E_0^2<\Lambda(14e_0+e_0^2),\qquad
 6E_0+(7+E_0)E_1<\Lambda\{6e_0+(7+e_0)e_1\},\\
 E_m<\Lambda e_0,\qquad E_1<\Lambda e_1.
 \end{gathered}
 \tag{SC.26}
$$

Every omitted term of $M_j^o$ is nonnegative. Consequently

$$
 \widehat M_0\le251M_0^o,\qquad
 \widehat M_1\le251M_1^o
 \tag{SC.27}
$$

pointwise on the complete core. This transfers the saved
true radial suprema and their integrals, without rereading
or reevaluating the original native rows.

For the original $P=P_{\le96}$, including its even mean,
the quadratic coefficients of the difference have degree at
most 192. The primitive and mean operations do not enlarge
that band. Thus the actual ordinary source fees are

$$
 \begin{aligned}
 \|P\Delta APh\|_2
     &\le(\widehat M_0+384\widehat M_1)\|Ph\|_2,\\
 \|P\Delta A(1-P)h\|_2
     &\le(\widehat M_0+1152\widehat M_1)
                   \|P_{97\le|j|\le288}h\|_2,\\
 \|(1-P)\Delta APh\|_2
     &\le(\widehat M_0+384\widehat M_1)\|Ph\|_2.
 \end{aligned}
 \tag{SC.28}
$$

The last output has degree at most 288. From the saved
pointwise maxima, (SC.27) yields the following strict
$L^2_rL^2_\phi$ body operator bounds:

| Complete interval | $\|\widehat M_0\|_\infty$ | $\|\widehat M_1\|_\infty$ | low-to-low / low-to-high fee | high-to-low fee |
|---|---:|---:|---:|---:|
| $[0,2383968743003/10^{13}]$ | $1.519\,10^{-5}$ | $3.247\,10^{-6}$ | $0.001262$ | $0.003755$ |
| $[0,9/10]$ | $9.474\,10^{-5}$ | $6.611\,10^{-6}$ | $0.002634$ | $0.007711$ |

The low/high fees use the saved supremum of the combined
positive function, rather than adding separately maximized
terms from different cells. All full parameter endpoints,
compact seams and original one-sided rows are included.

These are raw physical moving operator bounds. Applying them
in a weighted low193 Green space must retain that space's
actual conjugation and source normalizations. In particular
the existing WVC hybrid operator is not silently identified
with either differential in (SC.25). The old hybrid-to-actual
difference, original 193 jump atoms, full boundary rows,
height/phase functionals and any true trace receivers remain
their separate exact interfaces. This result supplies their
new centre-dependent body difference and complete residual;
it does not assert that a previously unknown inverse or
full nonlinear correction has become known.

## 7. Reproducible scalar arithmetic

The accompanying
[saved-bound comparison script](../scripts/fourfold_codazzi_selected_metric_compact_residual_saved_bounds.py)
reads only the two complete small outputs cited in section 1.
It uses exact rational arithmetic on every displayed saved
ball endpoint, the old radii and the rational constants above.
It compares the complete source values, all reported norms
and the operator scaling factors. It invokes no scientific
producer, native row scan, numerical quadrature or Fourier
calculation. The analytic identities and positive domination
arguments above, rather than a finite test of an unknown
operator, establish the result.
