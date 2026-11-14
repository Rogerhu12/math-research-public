# R133 supplement: the current moving body's complete actual Airy collar

2026-11-13, visible-exact / phase_inverse. **Proved and computed: all
27 gates pass.** This is the complete new amplitude-$0.765$ M32 full
moving centre with manifest SHA
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.
The input is its newly proved
[true physical complex germ](R133-supplement-current-moving-body-physical-complex-germ.md),
including the complete implicit physical-angle inverse. The numerical
fold, full potential, source, and graph bounds below are all recomputed
from that new input. No old nonradial numerical constant is transferred.

The actual root collar has canonical half-width

$$\delta=2^{-36}.                                                     \tag{N.1}$$

Its full padded Airy operator has Neumann perturbation norm less than
$0.028684969$. Both ordinary source columns, every Fourier mode and
both independent means are retained. The actual physical fixed circle
$r=r_*(\eta)-2^{-37}$ is also attached as its genuine nonconstant
negative canonical graph, with explicit two-direction input spaces.

The only universal numerical kernel reused here is the
[full two-port Airy kernel](R133-supplement-uniform-two-port-Airy-kernel-with-full-source.md)
of norm at most 32, including its correctly reflected negative-side
derivative. Its equation and normalized spaces are independent of the
candidate. All coefficient-dependent quantities are computed anew.

## 1. The true new physical labels and fold

Use the original physical two-state Jacobi equation at the actual
approximate centre, not the nonlocal moving variation equation. After
$R=\operatorname{diag}(-1,1)$ it is

$$y_r=(dI+aJ(K))y_\theta+Ly+Rf,\qquad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\quad L_{12}=K L_{21}.
                                                                    \tag{N.2}$$

The coefficient germ is holomorphic jointly in the true physical angle
of width $\sigma=1/8192$ and the radial disk of radius $10^{-5}$ about
every actual root. It is wholly inside the new candidate piece 2549
and its original scalar germ. Its full affine parameter box remains.

Let $z^2=r_*-r$, $k=K/(r-r_*)$, $p=a\sqrt{k}$, and $Z=1/512$.
The actual characteristic flows solve

$$ (H_\pm)_z=2zd(r_*-z^2,H_\pm)\mp2z^2p(r_*-z^2,H_\pm),
 \qquad H_\pm(0,x)=x.                                   \tag{N.3}$$

The complete Picard displacement and angular Lipschitz integral are
bounded by

$$
 \varepsilon=Z^2d^*+(2/3)Z^3p^*<2.768308\cdot10^{-6}<\sigma/32,
 \quad\lambda=Z^2d_\theta^*+(2/3)Z^3p_\theta^*
                                      <2.816115\cdot10^{-5}.          \tag{N.4}
$$

Thus both exact flows and their inverse labels $S_\pm$ exist on the
required complete complex products. The original physical coefficients
are analytic functions of $z^2$, so uniqueness gives
$S_+(-z)=S_-(z)$. The two flows have the same $2zd$ term and their
first difference is cubic. Consequently

$$
 X=(S_++S_-)/2,\qquad (S_+-S_-)/2=z^3G,
 \qquad G(0,\theta)=2p(0,\theta)/3,
 \qquad T=(r-r_*)(3G/2)^{2/3}.                           \tag{N.5}
$$

The analytic division in (N.5) and the selected fractional power use
the actual lower real part of $G$. On the full preliminary radial
radius $\rho=2^{-26}$ it is greater than $2.5136845048$. The equations
for the labels give the true canonical characteristic slopes
$\pm\sqrt{-T}$; merely removing the common drift would not establish
this conclusion.

Here are the complete new holomorphic gates:

$$
 \operatorname{Re}T_r>1.1848935643,\quad
 |J_f|\ge1.1804352935,\quad J_f=T_rX_\theta-X_rT_\theta,
 \quad\operatorname{Lip}(\hbox{joint inverse Picard map})<0.033367722.
                                                                    \tag{N.6}
$$

The joint inverse is therefore defined on the entire product

$$|T|\le2^{-34},\qquad |\operatorname{Im}X|\le1/32768.                \tag{N.7}$$

The proof is the direct two-variable contraction
$r-r_*=T/C(r,\theta)$, $\theta=X-(r-r_*)H(r,\theta)$,
where $C=(3G/2)^{2/3}$ and $X=\theta+(r-r_*)H$.
The new displacement, positive branch, derivative and contraction
values in (N.4)–(N.6) pay every hypothesis of that construction. Both
real injectivity and the complex inverse follow. No unconstructed
new coordinate is assumed.

## 2. Both local rows, frame and ordinary source

Set $D=\partial_r-d\partial_\theta$, $A=DT$ and
$A_T=A I-aT_\theta J(K)$. The complete algebra of the actual fold gives

$$
 b^2=T/K,\qquad F=\operatorname{diag}(b^{-1/2},b^{1/2}),\qquad
 Rh=FU,\qquad
 U_T=J(T)U_X+\mathcal VU+g,
 \quad g=F^{-1}A_T^{-1}Rf.                              \tag{N.8}
$$

The polynomial identity separating $A_T$, the positive branch of $b$,
and the actual Jacobian is checked before any corresponding division.
The full lower-order matrix is

$$
 \mathcal V=F^{-1}A_T^{-1}LF+J(T)F^{-1}F_X-F^{-1}F_T
          =\begin{pmatrix}d_1&T e_{12}\\e_{21}&d_2\end{pmatrix}.       \tag{N.9}
$$

In particular $e_{12}$ is a bounded actual analytic removable quotient,
not a formal pointwise division near zero. It follows from the exact
$L_{12}=K L_{21}$ identity. Both rows and all diagonal terms remain.
The new full holomorphic bounds are

$$
 \|\mathcal V\|<583745.928,\qquad
 |d_i|<357214.280,\qquad |e_{12}|,|e_{21}|<226185.676.       \tag{N.10}
$$

The physical collar $\Omega_\delta$ is the exact inverse image of
$[-\delta,\delta]\times\mathbb S^1$ under the actual chart. It is not
substituted by a rectangle in the original coordinates.

## 3. Full-frequency padded Airy inversion

Let $P=\langle D_X\rangle$. For all physical frequencies
$m\in4\mathbb Z\setminus\{0\}$ define

$$
 \omega_m=(|T|+|m|^{-2/3})^{1/2},\quad W_m=\omega_m^{-1/2},
 \quad\mathcal D=P^{1/6}\operatorname{diag}(W,W^{-1}),\quad
 \|U\|_{\mathcal E(T)}=\|\mathcal D(T)U\|_2.              \tag{N.11}
$$

At both means $W_0=1$. For every frequency,
$\|U\|_2\le\|U\|_{\mathcal E}$ and
$\|\mathcal Dg\|_2\le\|g\|_{H_X^{1/3}}$.

For completeness, the same-space multiplication bound used here is
the capped norm $A_t=P(1+t^3P^2)^{-1/2}$, $t=|T|$.
Its exact variational norm is

$$
 \|A_tf\|_2^2=
 \inf_{f=f_1+f_0}(\|Pf_1\|_2^2+t^{-3}\|f_0\|_2^2).
                                                                    \tag{N.12}
$$

If $a_j\ge\|\partial_X^ja\|_\infty$, full multiplication in the
$W^{\pm1}$ conjugates has bound
$M_0=2a_0^{5/6}(a_0+a_1)^{1/6}$. Its full angular commutator has
$M_1=2a_1^{5/6}(a_1+a_2)^{1/6}$. Interpolation after that commutator
gives the padded bound $M_0^{5/6}(M_0+M_1)^{1/6}$.
This includes all finite modes and all mean crossings.
For the off-diagonal terms, the lower-left cost is
$E_0^{5/6}(E_0+E_1)^{1/6}$; the upper-right term has the additional
$\sqrt{|T|}$ factor supplied by the exact $T$ in (N.9).

The new canonical strip in (N.7), rather than the old centre's strip,
is used for all derivatives: $Q_X=8/\sigma=65536$,
$D_1=Q_XD_0$, $D_2=2Q_X^2D_0$, $E_1=Q_XE_0$.
The complete new directed calculation gives

$$\|\mathcal D\mathcal V\mathcal D^{-1}\|
           <30800250.139=:M_{\mathcal E}.                \tag{N.13}$$

The universal two-port Airy Green has kernel at most 32 in these
weights, and commutes with the padding $P^{1/6}$. It keeps one
negative incoming port and one positive unstable port. For $m=0$
these are the first state at the negative endpoint and the independent
second state at the positive endpoint. Therefore the full reference
$L^2$ Green norm is at most $B=64\delta=2^{-30}$ and its two-column
Poisson norm is at most $64\sqrt\delta=2^{-12}$. In particular

$$BM_{\mathcal E}<0.028684969<1/8.                       \tag{N.14}$$

The full Neumann series converges on the single Hilbert space
$L^2_T\mathcal E(T)$; it introduces no repeated angular loss.
Finite-frequency approximation and the uniform bound give the full
untruncated solution, including both means. The actual estimates are

$$
\begin{aligned}
 \|U\|_{L^2_T\mathcal E}
 &<9.588265\cdot10^{-10}\|g\|_{L^2_TH_X^{1/3}}
       +0.000251351\|\mathfrak g\|_{H^{1/6}\oplus H^{1/6}},\\
 \|\operatorname{Tr}_\pm U\|_{\mathcal E\oplus\mathcal E}
 &<0.000251351\|g\|_{L^2_TH_X^{1/3}}
       +65.890055\|\mathfrak g\|_{H^{1/6}\oplus H^{1/6}}.
\end{aligned}                                                       \tag{N.15}
$$

Both full endpoint states, including the complementary means, are
among the outputs in the second line. This is a complete two-port
local BVP, not two zero Cauchy traces on the negative side together
with an additional positive condition.

## 4. Actual physical source and reconstruction, with radial derivatives

The real inverse image is much smaller than its preliminary complex
Picard box. The consumer retains $G(0,\theta)=2p(0,\theta)/3$ and
uses the actual new physical first and second angular derivative
bounds before bounding only the remaining radial Taylor tail.
This gives the complete real source contracts

$$
\begin{aligned}
 \|g\|_{L^2_{T,X}}&<2.276612\|f\|_{L^2_{r,\theta}},\\
 \|g\|_{L^2_TH_X^1}&<40.532977\|f\|_{H^1_{r,\theta}},\\
 \|g\|_{L^2_TH_X^{1/3}}&<5.944685\|f\|_{H^1_{r,\theta}},\\
 \|h\|_{L^2_{r,\theta}}&<1.424596\|U\|_{L^2_{T,X}}.
\end{aligned}                                                       \tag{N.16}
$$

For the derivative row, explicitly
$g_X=(M_f)_X f+M_f(r_Xf_r+\theta_Xf_\theta)$, with the actual
Jacobian used in the volume norm. Thus the physical $H^1$ norm in
(N.16) includes $f_r$. The output reconstruction uses
$dT\,dX=J_fdr\,d\theta$. The half-power Airy padding in (N.11)
already controls $U$ in ordinary $L^2$, so no factor $\delta^{-1/4}$
is inserted.

Combining the exact unrounded records of (N.15)–(N.16) gives

$$
 \|h\|_{L^2(\Omega_\delta)}
 <8.120083\cdot10^{-9}\|f\|_{H^1(\Omega_\delta)}
  +0.000358073\|\mathfrak g\|_{H^{1/6}\oplus H^{1/6}}.    \tag{N.17}
$$

The real fixed-$T$ angular Jacobian differs from one by less than
$1.143147\cdot10^{-6}$, and $\|F^{\pm1}\|<2.229184$.
Thus the full two-boundary physical trace reconstruction costs less
than $2.229186$. In ordinary physical endpoint $L^2$ norms,

$$
 \|\operatorname{Tr}_{\rm physical,\pm}h\|_{L^2\oplus L^2}
 <0.003330849\|f\|_{H^1(\Omega_\delta)}
  +146.881125\|\mathfrak g\|_{H^{1/6}\oplus H^{1/6}}.     \tag{N.18}
$$

The exact physical measure on each of these true curves is used.

## 5. True negative fixed-r graph, both directions

On the actual physical circle $r=r_*-2^{-37}$, the new graph
$T=t_g(X)$ satisfies

$$
\begin{gathered}
 1.7816158955\cdot10^{-11}<-t_g(X)<4.5497551793\cdot10^{-11},\\
 |t_g'|<2.092246\cdot10^{-10},\qquad
 |t_g''|<1.317546\cdot10^{-6}.                            \tag{N.19}
\end{gathered}
$$

It lies strictly between $T=-\delta$ and the negative outer canonical
section $T=-15\delta/4$. The complete two-sided same-weight Airy
propagator between any canonical sections in that negative annulus
has bound less than $69.253020$.

A graph trace is not inferred from that fixed-section bound. Instead,
for each direction use the actual foliation
$t(\tau,X)=(1-\tau)t_{\rm in}(X)+\tau t_{\rm out}(X)$ between
$t_g(X)$ and $-\delta$. With $p=t_X$, $\ell=t_\tau$, $Q=-t$,
the complete equation is

$$
 U_\tau=(d_fI+a_fJ(t))U_X+a_f(I+pJ)\mathcal VU
             +a_f(I+pJ)M_ff,
 \quad a_f=\frac{\ell}{1-p^2Q},\quad d_f=a_fpQ.           \tag{N.20}
$$

The new actual graph slopes in (N.19) prove spacelikeness. The true
domain measure is $d\tau dX=J_f|\ell|^{-1}drd\theta$.
Differentiating (N.20) includes both $\mathcal V_X+p\mathcal V_T$
and $(M_f)_X+p(M_f)_T$. All these terms are evaluated anew from the
new complex product and its new real derivative bounds.

The complete energies
$E_0=\|\operatorname{diag}(1,\sqrt Q)U\|_2$,
$E_1=\|\operatorname{diag}(1,\sqrt Q)U_X\|_2$
have two-direction gains less than $1.768215$; the full forcing from
$C_XU$ has coefficient less than $0.724652038$.
The second row is then treated as its real scalar transport equation,
so $\|U_2\|_2$ is obtained directly from the initial $U_2$, $E_0$,
$E_1$ and its ordinary source. It is not bounded by $E_0/\sqrt Q$.

At the flat endpoint, with $q_-=\sqrt\delta$,

$$
 \|U\|_{\mathcal E}^2
 \le H_*^2+q_-^{2/3}Y_*^{5/3}H_*^{1/3}+c_*Y_*^2,
 \quad H_*=(\sup E_0^2+\sup E_1^2)^{1/2},\quad
 Y_*=\sup\|U_2\|_2,\quad c_*=(\sqrt{17}/4)^{1/3}.        \tag{N.21}
$$

This is the complete Fourier inequality, including the two identity
mean weights. Its positive power of $q_-$ results from the ordered
second-row reconstruction and interpolation. It explains why a
quarter-power cost is absent from the actual graph contract.

The full new result is

$$
\begin{aligned}
 \|h\|_{L^2_\theta\text{ at }r_*-2^{-37}}
 &<4.528367\|U(-\delta)\|_{H_X^1}
             +0.000176579\|f\|_{H^1(\Omega_g)},\\
 \|U(-\delta)\|_{\mathcal E}
 &<32.817996\|h\|_{H^1_\theta\text{ at }r_*-2^{-37}}
             +0.001715000\|f\|_{H^1(\Omega_g)}.
\end{aligned}                                                       \tag{N.22}
$$

The two different input spaces in (N.22) are part of the result; they
are not a same-space inverse claim. The proof is exactly the genuine
foliation energy, scalar second row and complete source construction
of the fixed radial port theorem, with every numerical input evaluated
for this new centre. No external rectangle or unbounded graph-trace
evaluation is assumed.

## 6. Means, ports and obligations outside the collar

At a fixed-$T$ physical curve the original physical mean uses the
density $T_r/J_f$. At the true fixed-$r$ circle it uses $1/X_\theta$:

$$
 \langle h\rangle_\theta
 =\frac1{\pi/2}\int RFU\,\frac{T_r}{J_f}\,dX
 \quad\hbox{or}\quad
 \frac1{\pi/2}\int RFU\,\frac1{X_\theta}\,dX,
                                                                    \tag{N.23}
$$

respectively. Both independent mean states and their full source are
kept in every equation above. Neither expression is replaced by
canonical zero mean. The mixed-coordinate source also retains all
fully supplied original parameter columns.

The local two-port BVP, both full output states, and the genuine
negative fixed-$r$ interfaces are now proved for the current centre.
The whole common-piece strict connection, its actual exterior PPoly
interfaces, the positive regular graph, and the body feedback inverse
are distinct remaining interfaces. A moving variation input requires
the full residual-sensitive bridge to the physical operator; the
centre's small residual has not been set to zero. These permissions
are explicitly recorded as separate flags.

## 7. Reusable one-entry consumer and native record

Source:
`scripts/fourfold_codazzi_current_moving_fold_Airy.py`.
Complete native:
`notes/2026-11-13-R133-current-moving0765-complete-fold-Airy-ports-native.json.gz`.
The consumer takes the actual new physical germ and the universal
Airy certificate, checks their source identities and scope, then
recomputes the whole fold, balanced inverse and real graph contract.
It has 9 fold gates, 7 complete balanced gates and 11 graph/source
gates, all passed. No large new cache or candidate copy is required.

The root scale parameters are command-line options; their defaults
give this actual certificate. Any other candidate or scale requires
its own complete gate result, including every inverse-image and
source-domain condition.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/fourfold_codazzi_current_moving_fold_Airy.py --out notes/2026-11-13-R133-current-moving0765-complete-fold-Airy-ports-native.json.gz
```

The source refuses to overwrite existing reports. Every complete
coefficient, exact scale, input SHA and directed bound is preserved
in the compressed native record.
