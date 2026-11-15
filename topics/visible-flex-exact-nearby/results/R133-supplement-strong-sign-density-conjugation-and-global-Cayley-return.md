# R133 supplement: strong sign-density conjugation and the ordered global Cayley return

2026-11-15, tail_connector.

**Proved conditional analytic bridge; no new numerical evaluation.** The exact common-input outgoing map of MS is $U_{R_\Omega}\mathcal B_-Z^{\mathcal S}$. This note gives a complete $H^{-4/3}\to L^2$ bound for $Z^{\mathcal S}-Z$ from a true $C^4$ density chart, preserves its mean row, and identifies both sign corrections required to reach the scalar Cayley principal model. The original completed Cayley arithmetic is used only after those operator identities and their complete error hypotheses have been met.

The original terminal-Ai input, same selected angle, true waist, all original finite projections, and two independent physical means are unchanged. This theorem neither constructs the missing full incoming inverse nor assigns zero to a retained infinite block.

## ZD1. A true density chart and the full sign operator

Let $\psi:\mathbb R\to\mathbb R$ be a real orientation-preserving $C^4$ lift with
$$
 \psi(\phi+\pi/2)=\psi(\phi)+\pi/2,\qquad
 m_\psi:=\inf\psi'>0 .
 \tag{ZD.1}
$$
Use normalized measure on this circle, physical frequencies $4j$ and the Sobolev weights $\Lambda_j=(1+16j^2)^{1/2}$. Define
$$
 U_\psi f=\psi'(f\circ\psi),\qquad
 Z=\Pi_0+i\Pi_+-i\Pi_-,
 \qquad
 D_\psi=U_\psi ZU_\psi^{-1}-Z .
 \tag{ZD.2}
$$
The extension $Z1=1$ is the explicit auxiliary scalar convention of MS.9; it is not a replacement for either physical mean port.

Suppose numbers $M_2,M_3,M_4$ bound the indicated complete derivatives in ordinary supremum norm:
$$
 \|\psi^{(q)}\|_\infty\le M_q\quad(q=2,3,4),\qquad
 \underline m\le m_\psi,\quad \underline m>0,\qquad
 \underline\mu=\min(1,\underline m).
 \tag{ZD.3}
$$
Set
$$
 \boxed{\quad
 C_\psi^{(3)}
    =\frac{M_4}{\underline\mu^4}
       +\frac{10M_2M_3}{\underline\mu^5}
       +\frac{15M_2^3}{\underline\mu^6}.
 \quad}
 \tag{ZD.4}
$$
Let $K_{\psi^{-1},-}$ be a proved bound for the actual full inverse density map on $H^{-4/3}$. Then
$$
 \boxed{\quad
 \|D_\psi:H^{-4/3}\to L^2\|
   \le D_\psi^\#
      :=\frac{C_\psi^{(3)}}6K_{\psi^{-1},-}
                         +\frac{\sqrt2}{4}M_2 .
 \quad}
 \tag{ZD.5}
$$
No upper bound for $\psi'$ is required in (ZD.4). A positive lower bound and the actual three derivative bounds are required. A complex-strip estimate or an unknown chart is not substituted for the real chart in (ZD.1).

## ZD2. Three integrations by parts with the density amplitude

Write $a_{jk}=\langle U_\psi e_k,e_j\rangle$. For opposite nonzero signs, set
$$
 n=|k|,\quad p=|j|,\quad
 \theta=\frac{n}{n+p},\quad
 \kappa_\theta=1-\theta+\theta\psi',
 \quad N=4(n+p).
 \tag{ZD.6}
$$
The phase is $\epsilon N(\theta\psi+(1-\theta)\phi)$, where
$\epsilon=\operatorname{sgn}k$. Its normalized derivative is
$\kappa_\theta\ge\underline\mu$.

Starting from the actual density amplitude $F_0=\psi'$, define
$F_{q+1}=(F_q/\kappa_\theta)'$. Direct differentiation gives
$$
 \begin{split}
 F_1&=(1-\theta)\frac{\psi''}{\kappa_\theta^2},\\
 F_2&=(1-\theta)\left(
       \frac{\psi'''}{\kappa_\theta^3}
       -\frac{3\theta(\psi'')^2}{\kappa_\theta^4}\right),\\
 F_3&=(1-\theta)\left(
       \frac{\psi''''}{\kappa_\theta^4}
       -\frac{10\theta\psi''\psi'''}{\kappa_\theta^5}
       +\frac{15\theta^2(\psi'')^3}{\kappa_\theta^6}\right).
 \end{split}
 \tag{ZD.7}
$$
In particular $\|F_3\|_\infty\le(1-\theta)C_\psi^{(3)}$.
These are derivatives of the exact density amplitude. No truncated exponential is differentiated.

Each of the three boundary terms vanishes: the derivative coefficients are periodic and the full exponential has increment $2\pi\epsilon(n+p)$. Ordinary integration by parts therefore proves
$$
 \boxed{\quad
 |a_{jk}|
  \le\frac{C_\psi^{(3)}\,p}{64(n+p)^4},
       \qquad jk<0 .
 \quad}
 \tag{ZD.8}
$$
The factor $p/(n+p)$ comes from the actual density numerator in (ZD.7); it was not discarded before taking the Fourier sum.

For $j=0,k\ne0$, the exact density change of variable gives
$a_{0k}=0$. The column $k=0$ is $U_\psi1=\psi'$. Thus the output mean and the input mean require different treatments, handled explicitly below.

## ZD3. Complete weighted Fourier sum and the mean column

Put
$$
 K_\psi=[U_\psi,Z](1-\Pi_0).
 \tag{ZD.9}
$$
Its nonzero entries are the two opposite-sign blocks. Their multiplier difference has modulus two. Both blocks are included in the weighted Hilbert--Schmidt estimate:
$$
 \begin{split}
 \|K_\psi:H^{-4/3}\to L^2\|_{\rm HS}^2
 &\le
 8\left(\frac{C_\psi^{(3)}}{64}\right)^2
 \sum_{n,p\ge1}
      \frac{(1+16n^2)^{4/3}p^2}{(n+p)^8}\\
 &\le
 \frac{(C_\psi^{(3)})^2\,17^{4/3}}{2048}.
 \end{split}
 \tag{ZD.10}
$$
For the second line, use $(1+16n^2)^{4/3}\le17^{4/3}n^{8/3}$.
For $s=n+p$ the inner numerator sum is bounded by
$s^{8/3}\sum_{p=1}^{s-1}p^2<s^{17/3}/3$.
Finally
$\sum_{s=2}^\infty s^{-7/3}<\int_1^\infty x^{-7/3}dx=3/4$.
No numerical summation or sampled Fourier cutoff is used.

Since $17^{2/3}<7$ and $32\sqrt2>42$,
$$
 \|K_\psi:H^{-4/3}\to L^2\|
       \le\frac{C_\psi^{(3)}}6 .
 \tag{ZD.11}
$$
Both input signs have already been counted. A restriction to the conjugation-invariant real subspace inherits this bound without another $\sqrt2$.

The omitted input mean is the exact rank
$$
 [U_\psi,Z]\Pi_0=u_\psi\otimes\Pi_0,\qquad
 u_\psi=(1-Z)(\psi'-1),
 \qquad
 \|u_\psi\|_2=\sqrt2\|\psi'-1\|_2 .
 \tag{ZD.12}
$$
Here $\langle\psi'\rangle=1$, and physical-$4j$ Poincare gives
$\|\psi'-1\|_2\le\|\psi''\|_2/4\le M_2/4$.
In particular this row has not been discarded under a zero-mean input convention.

Use $\Pi_0U_\psi^{-1}=\Pi_0$ to obtain the complete identity
$$
 D_\psi=K_\psi U_\psi^{-1}
                   +u_\psi\otimes\Pi_0 .
 \tag{ZD.13}
$$
Taking norms proves (ZD.5). Only the first term is multiplied by
$K_{\psi^{-1},-}$. Equation (ZD.13) does not assert
$D_\psi1=u_\psi$: the first term can also act on the nonconstant function
$U_\psi^{-1}1$.

The complete output mean of $D_\psi$ is exactly zero because both density conjugation and $Z$ preserve the integral. Independent physical mean equations are still present in the original matching realization. If mean-identity density maps are used instead of full density maps, their actual $(\psi'-1)\Pi_0$ conversion terms must also be retained.

## ZD4. Exact source requirements for the actual common input

For MS the chart is
$$
 \psi=X_-\circ\mathcal H^{-1},\qquad
 U_\psi=\mathcal S .
 \tag{ZD.14}
$$
WX already supplies the same selected $K_{\mathcal S^{-1},-}$.
The complete AC result supplies
$$
 \frac{31}{32}\le\mathcal H'\le\frac{33}{32},\qquad
 \|\mathcal H''\|_\infty\le4,\quad
 \|\mathcal H'''\|_\infty\le1024,\quad
 \|\mathcal H''''\|_\infty\le393216 .
 \tag{ZD.15}
$$
These are the previously proved real derivatives of the same true selected angle, including its complete analytic tail. They are not a new KAM calculation.

For a transparent conditional input interface, let
$x_1^->0$ and $x_1,x_2,x_3,x_4$ bound
$\inf X_-'>0$ and the four ordinary derivative suprema of the same true waist map. Put $h_-=31/32$, $h_+=33/32$, $h_2=4$, $h_3=1024$, $h_4=393216$, and
$$
 \begin{split}
 y_1&=h_-^{-1},\\
 y_2&=h_2h_-^{-3},\\
 y_3&=3h_2^2h_-^{-5}+h_3h_-^{-4},\\
 y_4&=15h_2^3h_-^{-7}
                  +10h_2h_3h_-^{-6}+h_4h_-^{-5}.
 \end{split}
 \tag{ZD.16}
$$
These bound the derivatives of $\mathcal H^{-1}$. The actual composition gives the sufficient bounds
$$
 \begin{split}
 \underline m&=x_1^-/h_+,\\
 M_2&=x_2y_1^2+x_1y_2,\\
 M_3&=x_3y_1^3+3x_2y_1y_2+x_1y_3,\\
 M_4&=x_4y_1^4+6x_3y_1^2y_2
                     +x_2(3y_2^2+4y_1y_3)+x_1y_4 .
 \end{split}
 \tag{ZD.17}
$$
All denominators use the true positive lower bound. These are full ordinary derivatives of real maps, not derivatives inferred by dividing norm upper bounds.

In this interface the higher $X_-$ derivatives must be supplied from a complete same-object source certificate. The existing WX second-derivative record by itself does not supply $x_3$ or $x_4$. A valid original holomorphic/Cauchy source or a newly proved positive propagation bound may supply them without rerunning the old ray producer, but its radius, parameter domain and direction must first be verified. This note supplies no new directed numerical value for (ZD.17). The separate DX4 contract, `results/R133-supplement-complete-fourth-angle-derivatives-from-saved-cut-and-flow-bounds.md`, is the designated same-object source interface. If it reuses the already completed WX lower derivative and second-derivative bounds, those original rows are copied verbatim; (ZD.17) is not a request to reevaluate them. Only the genuinely new higher derivative combinations and (ZD.4)--(ZD.5) are new scalar targets.

## ZD5. From the exact outgoing order to a Fourier-sign principal factor

Retain the exact MS maps
$$
 B_i=T_i+E_i,\qquad
 \mathcal O_{\rm com}=U_{R_\Omega}(T_o+E_o)Z^{\mathcal S},
 \qquad
 T_i=1+M_{c_i}I,\quad T_o=1+M_{c_o}I .
 \tag{ZD.18}
$$
Here $E_i,E_o$ are complete errors, or exact decompositions into paid and retained terms. They are not automatically the WE paid subtotal. Write
$D=Z^{\mathcal S}-Z$ and let $D^\#$ bound its complete strong norm as above.
Since the straight Fourier $Z$ commutes with the rigid rotation, the exact identity is
$$
 \boxed{\quad
 \mathcal O_{\rm com}
    =Z U_{R_\Omega}(T_o+E_o^{\rm std}),\qquad
 E_o^{\rm std}
  =Z^{-1}\big([T_o,Z]+T_oD+E_oZ^{\mathcal S}\big).
 \quad}
 \tag{ZD.19}
$$
The first commutator is paid by MS.25:
$$
 \|[T_o,Z]\|_{H^{-4/3}\to L^2}
   \le \frac{17}{8}W_{1/3}(c_o-\langle c_o\rangle).
 \tag{ZD.20}
$$
The full $L^2$ bound for the left factor in $T_oD$ is
$1+\|c_o\|_\infty/4$; its constant mean has not been removed.

One may use either of the following complete negative-window bounds:
$$
 \|Z^{\mathcal S}\|_{H^{-4/3}\to H^{-4/3}}
 \le z_-^\#:=
 \min\left(
  \|\mathcal S\|_{-4/3}\|\mathcal S^{-1}\|_{-4/3},
                       \ 1+D^\#\right).
 \tag{ZD.21}
$$
The second follows from the complete strong bound for $D$ and the norm-one embedding $L^2\hookrightarrow H^{-4/3}$. The minimum is between two bounds for one whole operator.

If $\|E_o\|_{H^{-4/3}\to L^2}\le C_o$ has actually been proved, then
$$
 \boxed{\quad
 C_o^{\rm std}
  =\frac{17}{8}W_{1/3}(c_o-\langle c_o\rangle)
       +(1+\|c_o\|_\infty/4)D^\#+C_o z_-^\#
 \quad}
 \tag{ZD.22}
$$
bounds (ZD.19). When only $E_o^{\rm paid}$ is bounded, the same expression with
$C_o=C_{\rm paid}$ bounds just the two new known corrections and that paid submap; the additional exact retained term is
$Z^{-1}E_o^{\rm retained}Z^{\mathcal S}$. Nothing in (ZD.22) makes it zero, finite rank or norm-paid.

The nonmean Wiener term in (ZD.20) can also use the complete derivative bound
$W_{1/3}(c_o-\langle c_o\rangle)\le(39/32)\|c_o'\|_2$ of CG/PG, when those actual same-function inputs have been supplied. The raw root coefficient, its transported density and the selected $c_o$ cannot be interchanged by name.

Assume now the complete actual $B_i^{-1}$ exists on $H^{-4/3}$, with bound $L_{i,-}$, and retain the complete principal inverse $T_i^{-1}$ from MI/PG.
Let $\mathcal A=T_oT_i^{-1}$, with complete $L^2$ bound $K_{\mathcal A,0}$.
The ordered CY.19 identity becomes
$$
 \begin{split}
 (T_o+E_o^{\rm std})B_i^{-1}-\mathcal A
     &=(E_o^{\rm std}-\mathcal A E_i)B_i^{-1},\\
 \mathcal O_{\rm com}B_i^{-1}
     &=Z U_{R_\Omega}
           (\mathcal C_\mu+M_vI+E),\\
 \|E\|_{H^{-4/3}\to L^2}
     &\le C_E:=
 C_{\rm cor}
       +(C_o^{\rm std}+K_{\mathcal A,0}C_i)L_{i,-}.
 \end{split}
 \tag{ZD.23}
$$
Here $v=v_o-v_i$, $c_i=-\mu/2+v_i$, $c_o=\mu/2+v_o$, and
$\mathcal C_\mu=(1+\mu I/2)(1-\mu I/2)^{-1}$.
$C_{\rm cor}$ is the complete ordered two-primitive principal-ratio bound of CY.12--16, on the same functions and inverse. It is not recomputed or replaced by the old linear normal form.

The full incoming inverse and every retained row/column are hypotheses of (ZD.23). A high-block inverse alone does not provide them. If exact finite factors remain in the BF augmented system, this formula is used only with the corresponding complete typed block equations.

## ZD6. The second sign correction in the nonmean conjugation

Even after (ZD.23), a global sign operator cannot be moved through the cohomological normalizer for free. To avoid confusing it with the density chart $\mathcal S$, write
$$
 N=1+M_wI,\qquad
 N_-=1+M_{w_-}I=U_{R_\Omega}^{-1}NU_{R_\Omega},
 \quad w-w_-=-v,\quad \langle w\rangle=0 .
 \tag{ZD.24}
$$
All inverses here are the same full CN/LN inverse, with its two mean functionals retained. Suppose
$$
 K_{N,0}\ge\|N^{-1}\|_{L^2\to L^2},\qquad
 K_{N,-}\ge\|N^{-1}\|_{H^{-4/3}\to H^{-4/3}} .
 \tag{ZD.25}
$$
The corresponding bounds for $N_-^{-1}$ are identical because the rotation is an isometry.

For $A=\mathcal C_\mu+M_vI+E$ the exact global formula is
$$
 \boxed{\begin{split}
 N^{-1}(ZU_{R_\Omega}A)N
 &=ZU_{R_\Omega}\left[
  \mathcal C_\mu+N_-^{-1}(Q_{\rm Cay}+EN)+E_{\rm sign}\right],\\
 E_{\rm sign}
 &=-Z^{-1}N_-^{-1}[N_-,Z]N_-^{-1}AN,\\
 Q_{\rm Cay}
 &=M_vIM_wI+(\mathcal C_\mu-1)M_wI
                         -M_{w_-}I(\mathcal C_\mu-1).
 \end{split}}
 \tag{ZD.26}
$$
Indeed
$Z^{-1}N_-^{-1}Z
 =N_-^{-1}-Z^{-1}N_-^{-1}[N_-,Z]N_-^{-1}$,
and expansion of $AN-N_-\mathcal C_\mu$ gives the displayed
$Q_{\rm Cay}+EN$. The original first-order cancellation is exactly
$v+w-w_-=0$. The sign correction has the indicated minus sign.

Set
$$
 \begin{split}
 F_{N,-}&=1+W_{4/3}(w)/4,\\
 A_-^\#&=1+W_{4/3}(v)/4+C_E,\\
 C_{w,\rm sign}&=\frac{17}{8}W_{1/3}(w).
 \end{split}
 \tag{ZD.27}
$$
The first two lines bound the complete same-window operators $N$ and $A$.
They use the full mean and the complete strong $E$, not only an already paid part. Translation preserves the Wiener norms of $w$.
MS.25 gives $\|[N_-,Z]\|_{H^{-4/3}\to L^2}\le C_{w,\rm sign}$, including its mean output. Therefore
$$
 \boxed{\quad
 \|E_{\rm sign}\|_{H^{-4/3}\to L^2}
    \le K_{N,0}\,C_{w,\rm sign}\,
                          K_{N,-}\,A_-^\#\,F_{N,-}.
 \quad}
 \tag{ZD.28}
$$
The left inverse is used on $L^2$, the right inverse on $H^{-4/3}$.
There is no additional sign count and no independent quadratic-mean correction.

The complete bound for the other remainder in (ZD.26) is the original CY bound
$$
 C_{\rm Cay}
  =K_{N,0}\left[
    F_{N,-}C_E+
    \frac{17^{2/3}}{16}
       \left\{\|v\|_\infty W_{1/3}(w)
          +|\mu|\big(W_{1/3}(w)+\|w\|_\infty\big)\right\}
          \right].
 \tag{ZD.29}
$$
Thus $C_{\rm Cay}$ plus (ZD.28) is a permitted complete strong bound only after every stated input is actually supplied. The extra term in (ZD.28) is exactly what is absent when $\zeta$ is a single scalar in CY.23; a fixed-sector shorthand must not suppress it for the global two-sign map.

## ZD7. What the completed scalar Cayley gap then controls

The actual CYA computation proves, for the same selected $\mu_*=-4\beta_*$ and rotation,
$$
 \left|e^{2\pi ij\rho}
       \frac{1+i\beta_*/(2j)}{1-i\beta_*/(2j)}-\xi\right|
     \ge\frac1{1024|j|},
 \quad |j|\ge97,\quad \xi\in\{1,i,-1,-i\}.
 \tag{ZD.30}
$$
On $j\ne0$, $Z_j=i\,\operatorname{sgn}j$. Hence the principal equation
$1-ZU_{R_\Omega}\mathcal C_{\mu_*}$ uses the particular root
$\xi=Z_j^{-1}$ already included in (ZD.30). Its scalar inverse on the selected Fourier high space has the same proved one-derivative-loss bound256. This is a specialization of the completed four-root arithmetic, not another arithmetic run.

At $j=0$ the principal multiplier is one and this difference is zero. All principal low rows, the original transported $P_{97}$ complement, and the independent physical mean matching rows remain in their actual finite or coupled realization. The selected Fourier cutoff in (ZD.30) is not substituted for the original transported input cutoff.

Equations (ZD.19), (ZD.23) and (ZD.26) specify the complete operator corrections needed before (ZD.30) is a principal model for the actual common-input return. They do not certify that the strong remainder is small after a chosen smoothing step, that the finite Schur complement is invertible, or that any coupled nonlinear state exists.

## ZD8. Minimal inputs, provenance and scope

| Input | Exact role and present status |
|---|---|
| Same real $\psi=X_-\circ\mathcal H^{-1}$, positive derivative lower, derivatives through four | Required by (ZD.4)--(ZD.5). AC supplies the true $\mathcal H$ part. The complete matching $X_-$ third/fourth derivative source must be verified separately. |
| WX full $\|\mathcal S^{-1}\|_{-4/3}$ and $\|\mathcal S\|_{-4/3}$ | Already completed same selected coordinate bounds. They are ordinary operator norms, not entries of a finite matrix or unknown-state norms. |
| Complete selected $c_o$ supremum/nonmean derivative or $W_{1/3}$ bound | Supplies the first sign commutator and the full left $T_o$ factor. The CG/PG source identities specify this function. |
| WE paid $E_i,E_o$ submaps and every retained term | The paid numbers stay immutable. They may enter (ZD.22)--(ZD.23) only with an exact decomposition; a retained infinite term remains unbounded until actually paid. |
| Actual full incoming inverse and full principal ratio data | Required by (ZD.23), independently of the MI high inverse and of scalar CYA arithmetic. |
| Full $v,w$ Wiener bounds, the same two-window $N^{-1}$, all mean functionals | Required by (ZD.27)--(ZD.29). A first-coefficient scalar mean does not supply these nonmean bounds. |
| CYA selected coefficient and rotation | Supplies only the already completed scalar high principal gap (ZD.30), after the above ordered identifications. |

The complete true-angle source is
[AC](R133-supplement-actual-conjugacy-density-transfer-for-complete-first-coefficient.md),
blob `30591d2714e45dcad6ae2de1774a9b7e333466de`, 8974 bytes,
SHA256 `6527fa46ddc21ed3d3e8c6ce4bb1f39f2db816d9fff5684e6daf4f30951c46f4`.
The exact sign-order source is
[MS](R133-supplement-exact-Maslov-sign-operator-and-common-input-outgoing-order.md),
blob `10fdaddc0114e25ad349f1f411e80baf4f98fe26`, 19522 bytes,
SHA256 `44038eaed377863961aad7f0c74caa2bf498d6a689812f05933111777c191161`.
The CY primary is
[R133-supplement-exact-Cayley-principal-ratio-and-conditional-scalar-gap.md](R133-supplement-exact-Cayley-principal-ratio-and-conditional-scalar-gap.md),
blob `868ac231665c6ba7ac24a45def032609de767974`, 17846 bytes,
SHA256 `9a4e41c208f785e1dd3960c047a579a81493ea7cba17f870c9661caf550fd44e`.
The completed CYA primary is
[R133-supplement-actual-finite-Cayley-scalar-gap-and-selected-inverse.md](R133-supplement-actual-finite-Cayley-scalar-gap-and-selected-inverse.md),
blob `832f28f25698a82ea65a3cadd86fb2bd2fea0de8`, 16505 bytes,
SHA256 `2a5e9fb7b0d2476e0420dff30efdcb7168708dcc1b3fb6486a0d14dcafccd7f2`.

The displayed primitive, sign and mean identities are exact. All new scalar products remain unevaluated in this note. No old ray, enclosure, root, KAM, coefficient transport, successful scientific consumer, matrix sweep or gap computation is repeated.
