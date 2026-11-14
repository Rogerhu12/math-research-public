# R133 supplement: actual final all-mode physical cap Green operator

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved.** On the true interval $[9/10,25/8]$, the physical Codazzi
Jacobi operator at the final `ac1d5b98…` centre has a complete continuous
two-ended inverse, including the derivative of the actual nonlinear
regular exterior. Its full feedback is less than $.820523$ and its
resolvent factor is less than $5.571744$. These statements hold for all
physical Fourier modes, both curvature means, the original whole affine
parameter interval, and the complete primitive tail.

This is an actual stable positive-cap graph. It does not use a radial
collocation inverse. It is not yet the inverse of the complete moving
body: the residual-sensitive moving-to-physical operator bridge and the
negative/turning matching remain separate. In particular, a small
candidate residual is not silently replaced by zero in that bridge.

## 1. Object, variables, and the exact small multiplication columns

The candidate is the complete 32-mode moving polynomial with index SHA256

```
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413
```

and exact parameters

$$
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 \nu=-\frac{2572625729470897}{72057594037927936}.
 \tag{C.1}
$$

The compact metric modification is supported in $(.05,.18)$. Thus all
intrinsic coefficients on this cap are those of the actual unchanged
rotational target. The complete interval is $I=[L,R]$ with
$L=9/10$, $R=25/8$; no old nonradial centre is used.

Write the moving centre as

$$
 u=\alpha U,\quad v=s+\alpha V,\quad s=C_{\rm ref}^{-1},\quad
 m=\langle v\rangle_\phi,\qquad
 \theta=\phi+\psi(\phi),\quad \psi=\frac1m I(v-m).
 \tag{C.2}
$$

Here $I=\partial_\phi^{-1}P_{\ne0}$ has the original zero-mean convention.
The physical centre is
$\widehat B=(u/v)\circ\phi(\theta)$,
$\widehat C=(1/v)\circ\phi(\theta)$.
Put $\ell=K/C_{\rm ref}^2$ and $c=\widehat C-C_{\rm ref}$.
For the exact physical nonlinear algebra

$$
 Q(B,c)=\frac{B^2+\ell c^2}{C_{\rm ref}+c},\qquad
 A=A_{\rm ref}-\ell c+Q(B,c),
 \tag{C.3}
$$

its derivative at this centre is multiplication by two particularly
simple functions:

$$
 \boxed{Q_B=2u,\qquad Q_c=\ell-u^2-Kv^2
       =-u^2-K(2s\alpha V+\alpha^2V^2),}
 \tag{C.4}
$$

followed by the genuine inverse angle in (C.2). Formula (C.4) is an exact
identity. In particular, there is no reciprocal of the nonradial $v$ in
these multiplication columns. Neither Codazzi equation is assumed to
hold at the finite centre in deriving (C.4).

## 2. The physical angle and the order of radial and Fourier norms

For a scalar coefficient define

$$
 \|a\|_{\mathfrak A_\sigma}
   =\sum_{k\in4\mathbb Z}e^{\sigma|k|}\sup_{r\in I}|a_k(r)|.
 \tag{C.5}
$$

The supremum is taken separately for every coefficient before summation.
At the finite candidate interfaces one can use the direct sum of the
closed radial pieces; both one-sided values are retained. This is a
Banach algebra, with the usual complete convolution product.

Set $\sigma=1/64$. The actual complete cubic intersections give

$$
 \|\psi\|_{\mathfrak A_{2\sigma}}<.003774146<\sigma,
 \qquad
 \|\psi_\phi\|_{\mathfrak A_{2\sigma}}<.015211829<1.
 \tag{C.6}
$$

For $h\in\mathfrak A_\sigma$ with $\|h\|\le\sigma$, the complete
Fourier exponential series gives

$$
 \|\psi({\rm id}+h)\|_{\mathfrak A_\sigma}
 \le\|\psi\|_{\mathfrak A_{2\sigma}},\quad
 \|D_h\psi({\rm id}+h)\|
 \le\|\psi_\phi\|_{\mathfrak A_{2\sigma}}.
 \tag{C.7}
$$

Consequently $h=-\psi({\rm id}+h)$ has a unique solution in that ball.
It is the real inverse lift $\phi(\theta)=\theta+h(\theta)$; uniqueness
also preserves the exact reflection. Independently the full real
Jacobian is bounded by

$$
 .9865997340<\theta_\phi<1.0134002660.
 \tag{C.8}
$$

For any complete finite centre coefficient $a$, composition gives
$\|a\circ\phi\|_{\mathfrak A_\sigma}
\le\|a\|_{\mathfrak A_{2\sigma}}$.
The actual directed computation of (C.4), before this composition,
therefore proves

$$
 \|Q_B\|_{\mathfrak A_\sigma}<.039196064,
 \qquad
 \|Q_c\|_{\mathfrak A_\sigma}<.051432066.
 \tag{C.9}
$$

In particular these are physical-angle $\mathfrak A_0$ bounds, not
unjustified identifications of moving and physical Fourier coefficients.

The unknown direction uses the Hilbert module

$$
 \|x\|_{\mathfrak M}
   =\left(\sum_{k\in4\mathbb Z}\sup_{r\in I}|x_k(r)|^2\right)^{1/2},
 \qquad
 \|(x_1,x_2)\|_{\mathfrak M^2}
   =\|x_1\|_{\mathfrak M}+\|x_2\|_{\mathfrak M}.
 \tag{C.10}
$$

Young's inequality for complete sequences proves
$\|ax\|_{\mathfrak M}\le\|a\|_{\mathfrak A_0}\|x\|_{\mathfrak M}$.
Thus the true full multiplication map

$$
 \mathcal Q(b,c)=Q_Bb+Q_cc
 \quad\hbox{satisfies}\quad
 \|\mathcal Q\|<.051432066.
 \tag{C.11}
$$

All zero and nonzero modes are included. The norm in (C.10) is stronger
than $L_r^\infty L_\theta^2$; they are not interchanged in the proof.
The ordinary volume-source norm below is genuinely $L_r^2L_\theta^2$.

## 3. The complete rotational reference and the continuous two-ended kernels

For each nonzero physical mode $k$, put $M=|k|$ and
$b_k=i\operatorname{sgn}(k)\,\delta B_k$, $c_k=\delta C_k$.
The full rotational reference is

$$
 b_k'=-2\beta b_k+M\gamma\ell c_k+F_{b,k},\qquad
 c_k'=M\gamma b_k-\beta(\ell+1)c_k+F_{c,k}.
 \tag{C.12}
$$

The actual radial coefficients include their entire original primitive
tail. Let $q_M$ be the complete positive reference line propagated from
the genuine rotational outer multiplier. Its equation is

$$
 q_M'=M\gamma(q_M^2-\ell)+\beta(\ell-1)q_M.
 \tag{C.13}
$$

The producer computes a suffix invariant interval on every true native
box. If
$d=-\beta(\ell-1)/(4\gamma)$, it uses the positive roots of
$\ell_-+\min(0,d_-)x-x^2=0$ and
$\ell_++\max(0,d_+)y-y^2=0$, along with the actual complete outer
interval. It then checks both inward faces strictly on every box.
This proves all $M\in4\mathbb N$ at once.

For the actual linearized nonlinear term $Q=\mathcal Q(\delta B,\delta C)$,
and with $d_k=b_k+q_Mc_k$, the exact equations are

$$
 \begin{split}
 d_k'&=(M\gamma q_M-2\beta)d_k
       +(-M\gamma+q_M\beta)Q_k+F_{b,k}+q_MF_{c,k},\\
 c_k'&=-[M\gamma q_M+\beta(\ell+1)]c_k
       +M\gamma d_k+\beta Q_k+F_{c,k}.
 \end{split}
 \tag{C.14}
$$

Prescribe $d_k(R)$ and $c_k(L)$. Integrate the first equation from $R$
backward and the second from $L$ forward. The true exponential kernels
are used in these opposite directions; there is no outward unstable
shooting inverse. The native comparisons prove

$$
 M\gamma q_M-2\beta\ge M s_D,
 \qquad M\gamma q_M+\beta(\ell+1)\ge M s_C,
 \quad s_D>2.9252958741,\quad s_C>.8601652212.
 \tag{C.15}
$$

Writing $T,K_D,K_C$ for the complete triangular, $Q$-to-$d$, and
direct $Q$-to-$c$ kernel bounds, the actual values are

$$
 q_M<1.389936764,\quad T<3.625263015,\quad
 K_D<1.430261636,\quad K_C<.891297547.
 \tag{C.16}
$$

For example each row pays

$$
 T_j=\frac{\gamma_{j,+}}{(s_C)_j},\quad
 (K_D)_j=\frac{\gamma_{j,+}+q_{j,+}|\beta_j|/4}{(s_D)_j},\quad
 (K_C)_j=\frac{|\beta_j|}{4(s_C)_j}.
 \tag{C.17}
$$

These are valid for variable coefficients: each numerator is bounded
pointwise by its stated constant times the actual positive damping
rate, whose exponential kernel has total mass at most one. A single
global maximum is taken only after these correlated ratios are paid.

Since $b=d-q_Mc$, put

$$
 C_Q=TK_D+K_C,\quad B_Q=K_D+q_+C_Q,\quad
 H_D=1+(1+q_+)T,\quad H_C=1+q_+.
 \tag{C.18}
$$

For the mean equations, separately and without a limiting $M=0$ argument,

$$
 B_0'=-2\beta B_0+F_{B,0},\qquad
 c_0'=-\beta(\ell+1)c_0+\beta Q_0+F_{C,0}.
 \tag{C.19}
$$

Both are solved backward from their independent outer values. As
$\beta<0$ throughout this cap, their homogeneous backward kernels have
norm at most one, and the $Q_0$ kernel is bounded by
$K_0=1/(1+\ell_-)<.523455817$.
The full module $Q$-to-pair constant is therefore

$$
 K_G=B_Q+\max(C_Q,K_0)<15.952406835.
 \tag{C.20}
$$

This establishes the extension from the original coefficientwise Green
kernel to (C.10). It is not an inference from an abstract $\ell^1$
operator norm. The explicit maximum in (C.20) pays the full mean in the
Hilbert-module pair norm.

## 4. Ordinary and divergence sources, jumps, and all endpoint columns

Let $b_- =\inf(-\beta)>0$ and $\ell_-=\inf\ell>0$ on this actual cap.
For an ordinary nonzero-mode source, the squared backward/forward
exponential kernels have integrals at most
$1/(2Ms_D)$ and $1/(2Ms_C)$. With $M\ge4$, define

$$
 A_D=(8s_D)^{-1/2},\quad A_C=(8s_C)^{-1/2},\quad
 A_{B0}=(4b_-)^{-1/2},\quad
 A_{C0}=[2b_-(1+\ell_-)]^{-1/2}.
 \tag{C.21}
$$

Cauchy--Schwarz is applied to each full radial integral before the
Fourier square sum. The actual pair source bounds used by the producer
are the conservative complete values

$$
 \begin{split}
 G_B&=(1+q_+T)A_D+T A_D+A_{B0}<2.283958510,\\
 G_C&=(1+q_+T)q_+A_D+(1+q_+)A_C+Tq_+A_D+A_{C0}
       <3.980645850.
 \end{split}
 \tag{C.22}
$$

Thus these multiply the independent norms
$\|F_B\|_{L_r^2L_\theta^2}$ and $\|F_C\|_{L_r^2L_\theta^2}$.
Their means were paid separately in (C.19), not removed.

If the physical equations also contain $\partial_\theta G_B$ and
$\partial_\theta G_C$, take $G_B,G_C\in\mathfrak M$. The factor $M$
cancels the modewise kernel mass. The corresponding complete constants
are

$$
 G_{\partial B}=H_D/s_D<3.303648510,\qquad
 G_{\partial C}=H_Dq_+/s_D+H_C/s_C<7.370324962.
 \tag{C.23}
$$

The divergence source has zero physical mean; an additional ordinary
mean source still uses (C.19). No estimate of an arbitrary derivative
source in ordinary $L^2$ is claimed.

At any radial interface, prescribe the complete physical jump
$(j_B,j_C)$ in the same physical angle. In the reference coordinates it
is $(Jj_B+q_Mj_C,j_C)$. The two-ended Green yields pair gain at most

$$
 H_D\|j_B\|_2+(H_Dq_++H_C)\|j_C\|_2,
 \tag{C.24}
$$

including the separately bounded means. The sums of all such norms are
retained. The reference $q_M$ and intrinsic coefficients are continuous
at their genuine joins; no candidate PPoly interface is removed.

The unclosed complete endpoint gain is

$$
 H_C\|c_{\ne0}(L)\|_2+H_D\|d_{\ne0}(R)\|_2
       +|B_0(R)|+|c_0(R)|.
 \tag{C.25}
$$

In particular the even mean at $L$ is an output. No unspecified fifth
condition is added to this two-ended system.

## 5. Close the actual complete exterior without dropping its mean

The actual nonlinear exterior derivative, evaluated at the true final
centre input, is the already proved physical $L^2$ graph

$$
 J\delta B+Q_{\rm true}\delta C_{\ne0}
     =D d\,\delta C_{\ne0}+e_D,
 \qquad
 \delta C_0=D c_0\,\delta C_{\ne0}+e_0.
 \tag{C.26}
$$

All its independent outer-height, Robin residual and mean-charge
columns remain in $e_D,e_0$. Its actual bounds on the $10^{-12}$ input
ball are $\|Dd\|<5.898255\,10^{-6}$ and
$\|Dc_0\|<7.372818\,10^{-7}$.
The true long exterior includes the original mean holonomy small root.
This is a derivative graph at the centre's input; it does not assert
that the centre already satisfies its nonlinear boundary equation.

The rotational reference multiplier need not be identified with a
changed exterior profile. Both multipliers are compared with the same
$q_*=(1+w_R^2)^{-1/2}$. The original rotational fee retained by the
native is strictly positive and less than $10^{-85170599}$; the current
complete long comparison is less than $2^{-512}$. The producer adds
their sum explicitly, verifies it is less than $2^{-500}$, and uses

$$
 L_D=5.898255\,10^{-6}+\epsilon_{\rm old}+2^{-512},
 \qquad L_0=7.372818\,10^{-7}.
 \tag{C.27}
$$

Hence the total complete contraction is

$$
 \chi=K_G\max(\|Q_B\|_{\mathfrak A_0},\|Q_c\|_{\mathfrak A_0})
        +H_D L_D+L_0
       <.820523<1.
 \tag{C.28}
$$

This is a bounded operator on the full space (C.10), so its Neumann
series supplies genuine existence and uniqueness of the continuous
linear cap BVP. Evaluation at either end is bounded in $L^2$. There is
no finite-frequency proviso and no hidden requirement that a large
radial mesh resolve $M\gamma$.

The full resolvent multiplier is less than $5.571744$. Conservative
closed pair gains are as follows:

| Independent input | Gain to $\mathfrak M^2$, hence to either $L^2$ trace |
| --- | ---: |
| $c_{\ne0}(L)$ | $13.316116$ |
| outer $e_D$ | $53.846164$ |
| outer $B_0$ | $5.571744$ |
| outer $e_0$ | $5.571744$ |
| ordinary $F_B$, in $L_r^2L_\theta^2$ | $12.725633$ |
| ordinary $F_C$, in $L_r^2L_\theta^2$ | $22.179140$ |
| divergence $G_B$, in $\mathfrak M$ | $18.407084$ |
| divergence $G_C$, in $\mathfrak M$ | $41.065564$ |
| sum of all physical $B$ jumps | $53.846164$ |
| sum of all physical $C$ jumps | $88.158880$ |

The reflection class imposes $B_0(R)=0$ only when that physical boundary
condition is actually requested. The general source/port theorem keeps
it independent. The external mean height and rigid-position data are
still the separate reconstruction outputs of the true exterior; a
curvature graph does not replace those rows.

## 6. Actual continuous computation and exact reproduction

The source is
`scripts/fourfold_codazzi_final_physical_cap_linear_module.py`.
It verifies the complete candidate index and every original shard,
the original target identity, the complete positive-cap native and its
producer/dependencies, and the exact moving-coordinate declaration.
It consumes the original 1,334-box intrinsic theorem and intersects the
selected suffix with every exact dyadic candidate PPoly interface.
The result has 1,346 complete closed intersections. Every Fourier
coefficient, including the actual even mean and the complete quadratic
band, is evaluated by directed 320-bit Arb Horner and convolution.

The report records all coefficientwise radial suprema, the complete
closed cover, every all-mode Riccati face and rate, all independent
source/port constants, and the true exterior multiplier comparison.
The canonical completed report is

```
notes/2026-11-14-R133-final-physical-cap-linear-module-r09-v2-native.json.gz
```

The earlier `r09-native` report computed the same cap kernels before
the independent old/current exterior-$q$ comparison was made explicit.
It is retained as a provisional calculation. Only the `v2` report is
used for the full exterior-closed statement here.

From the topic directory:

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python3 scripts/fourfold_codazzi_final_physical_cap_linear_module.py \
  --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --left 9/10 \
  --out /a-new-path/current-physical-cap-linear-module.json.gz
```

The source refuses to overwrite a previous attempt. The final large
candidate is reproduced by the already published exact six-step chain;
it is not duplicated in this bundle.

## 7. The remaining complete-body interface

This theorem supplies the exact physical stable graph at $r=.9$ and a
continuous all-mode source operator behind it. It can therefore be used
in a finite-head Schur construction without propagating unstable
positive modes from the waist to the far end.

The actual global trial is in moving unknowns. Its conversion to the
physical pair contains the already derived full nonlocal mean term.
At a nonsolution centre the two linearized PDEs differ by the exact
residual-sensitive operator. That difference must be represented by
the ordinary/divergence source columns above and bounded using the
actual complete residual and its angular derivative. Similarly the
moving PPoly interface must be converted into its exact same-physical-
angle jump before (C.24) is used. None of these fees is declared zero
or included by a formal change of names.

The negative return, its true high-frequency arithmetic, the remaining
head/high feedback, the scalar $\nu$ amplitude Schur and a compatible
nonlinear iteration are still separate obligations. The cap theorem
does not assert the README completion standard.
