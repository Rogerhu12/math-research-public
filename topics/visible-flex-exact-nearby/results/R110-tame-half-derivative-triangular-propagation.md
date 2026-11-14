# R110 supplement. Tame half-derivative propagation with a base-energy forcing layer

Date: 2026-11-13.

## A. Exact scope and the reason for this supplement

This result strengthens the complete coefficient-input theorem [R110](R110-constraint-preserving-strict-core-energy-and-strong-sources.md). It concerns the same explicit symmetrized affine family, the entire real parameter interval $|p-p_5|\le10^{-9}$, the physical angle $\theta$ of period $\pi/2$, and the actual scalar operator
$$
\mathcal P u=\partial_r(a u_r+b u_\theta)
 +\partial_\theta(bu_r+cu_\theta)+d u,\qquad d=\tau+\partial_\theta\sigma.
$$
Its strict-negative coefficients are
$$
\alpha=a^{-1}>0,\qquad v=b/a,\qquad
\gamma=(b^2-ac)/a>0.
$$
The weight $\lambda$ is either a fixed positive exact constant or the actual radial function $\kappa=-K_0>0$. It is never silently replaced by $d$: the actual potential $d$ has already been observed to change sign near the waist.

Every interval in this theorem must have complete positive lower bounds for $\alpha,\gamma,\lambda,\kappa$, throughout all real angles, the complete radial interval, and the stated whole parameter family. The quarter-core $[-1/4,1/4]$ also contains positive collars. This theorem does not cross its turning roots or pay the Airy or positive-cap maps.

The earlier R110 program puts every commutator contribution into a single $H^{1/2}$ exponential. That is a valid but potentially expensive bound. Here the highest-order part of the commutator is retained with its sign in the actual energy matrix. Its entire remaining Fourier contribution is driven by the separately controlled base energy. No term, selected-coefficient error, or infinite Fourier tail is discarded.

The first native replay of the old R110 consumer on one complete strict leaf gave an old commutator bound $4508.912398724946$. That is only an observed old bound on that leaf. No numerical improvement by the source in this supplement is asserted before its own actual replay.

## B. The exact physical multiplier and two cutoff-free estimates

Put
$$
\omega_k=4k,\qquad L_k=\max(1,|\omega_k|),\qquad
J_k=\sqrt{L_k},\qquad J e^{4ik\theta}=J_k e^{4ik\theta}.
$$
Thus $J$ is exactly the R110 half-derivative multiplier, including weight one at the angular mean. For a coefficient $a$ define the complete Fourier sums
$$
\begin{aligned}
A(a)&=\sum_m(\sqrt{1+|\omega_m|}-1)|a_m|,\\
W_1(a)&=\sum_m|\omega_m||a_m|,\\
D A(a)&=\sum_m|\omega_m|(\sqrt{1+|\omega_m|}-1)|a_m|,\\
W_{3/2}(a)&=\sum_m|\omega_m|^{3/2}|a_m|.
\end{aligned}                                                   \tag{A.1}
$$
These sums are over all integers, not just saved modes.

First,
$$
|J_k-J_l|\le\sqrt{1+|\omega_{k-l}|}-1.                           \tag{A.2}
$$
Indeed $L_k,L_l\ge1$, $|L_k-L_l|\le|\omega_{k-l}|$, and
$\sqrt{x+t}-\sqrt{x}$ decreases with $x\ge1$. Therefore
$$
\|[J,a]z\|_2\le A(a)\|z\|_2.                                  \tag{A.3}
$$
This is a base-norm bound, stronger than estimating the same expression by $A(a)\|Jz\|_2$.

A useful unsigned version of the differentiated estimate is
$$
|\omega_k|\,|J_k-J_l|
 \le \frac{|\omega_{k-l}|}{2}J_l
   +|\omega_{k-l}|\big(\sqrt{1+|\omega_{k-l}|}-1\big).           \tag{A.4}
$$
To prove it, put $r=L_k$, $p=L_l$, $s=\sqrt r$, $q=\sqrt p$, and
$t=|\omega_{k-l}|$. One has
$$
\frac{r}{s+q}\le \frac q2+(s-q)_+.
$$
For $s\le q$ this follows from $s^2/(s+q)\le q/2$. For $s\ge q$ it follows after multiplying by $s+q$, since
$(s-q)(s+q/2)\ge0$. Multiply by $|r-p|\le t$, use $|\omega_k|\le r$, and apply (A.2). Convolution then gives
$$
\|D[J,a]z\|_2
 \le \frac12 W_1(a)\|Jz\|_2+D A(a)\|z\|_2.                    \tag{A.5}
$$
Every nonzero physical frequency is at least four. Hence the already paid R110 sums also imply
$$
W_1(a)\le
 \min\!\left(\frac{B_{1/2}(a)}{\sqrt5},
             \frac{D A(a)}{\sqrt5-1}\right).                  \tag{A.6}
$$
These are full-frequency statements and require no cutoff.

## C. Retaining the signed principal commutator

The preferred decomposition is
$$
D[J,a]z=\frac12(Da)Jz+\mathcal R_a z,\qquad
\|\mathcal R_a z\|_2\le W_{3/2}(a)\|z\|_2.                    \tag{A.7}
$$
Here $D=\partial_\theta$ and no factor of four is absorbed into $a$.

For a coefficient frequency $m=k-l$, the residual Fourier multiplier, with its harmless factor $i$ removed, is
$$
\omega_k(J_k-J_l)-\tfrac12\omega_m J_l.
$$
When $l\ne0$, let $F(x)=x\sqrt{|x|}$. Since $\omega_l\ne0$ lies in $4\mathbb Z$,
$$
F'(\omega_l)=\tfrac32J_l,\qquad
\omega_k(J_k-J_l)-\tfrac12\omega_mJ_l
 =F(\omega_l+\omega_m)-F(\omega_l)-F'(\omega_l)\omega_m.
$$
The derivative $F'(x)=\tfrac32\sqrt{|x|}$ satisfies
$$
|F'(x+h)-F'(x)|\le\tfrac32\sqrt{|h|}.
$$
The integral remainder is therefore at most $|\omega_m|^{3/2}$.
For $l=0$ and $m\ne0$ the exact residual is
$\omega_m(\sqrt{|\omega_m|}-3/2)$, whose absolute value is at most
$|\omega_m|^{3/2}$ because $|\omega_m|\ge4$. The case $m=0$ is zero.
This proves (A.7) including the mean. Young's convolution inequality proves its operator bound.

If the old complete sums alone are used, then
$$
W_{3/2}(a)\le
 \min\!\left(B_{1/2}(a),
       \frac{\sqrt5+1}{2}D A(a)\right).                       \tag{A.8}
$$
For the second bound, the ratio
$\sqrt t/(\sqrt{1+t}-1)=\sqrt{1+1/t}+1/\sqrt t$ decreases for $t\ge4$ and has value $(\sqrt5+1)/2$ at $t=4$.

A saved complete coefficient rectangle gives a sharper alternative. Let its finite coefficient approximation be $\widehat a_m$ and let $E_1,E_2$ bound the complete first and second absolute Fourier moments of its error. Then
$$
W_{3/2}(a)
 \le\sum_{\text{saved }m}|\omega_m|^{3/2}|\widehat a_m|
      +\sqrt{E_1E_2}.                                      \tag{A.9}
$$
The last term follows from Cauchy-Schwarz with respect to the complete nonnegative coefficient-error masses. It includes retained midpoint errors, both aliases, and the complete unretained time and angle complements. A small finite spectral tail alone cannot be substituted for it.

## D. Constraint-preserving state and exact signed energy matrix

For the full divergence load
$$
\mathcal P u=f_0+\partial_r f_r+D f_\theta
$$
use the same shifted physical momentum as R107 and R110:
$$
q=Du,\qquad p=a u_r+bq-f_r.
$$
The exact state equations are
$$
\begin{aligned}
u_r&=\alpha p-vq+\alpha f_r,\\
q_r&=D(\alpha p-vq)+D(\alpha f_r),\\
p_r&=-D(vp-\gamma q)-d u+f_0+D(f_\theta-vf_r).              \tag{A.10}
\end{aligned}
$$
For the saved finite weak residual,
$(f_0,f_r,f_\theta)=(-R_0,R_r,R_\theta)$ and $p=p_N$ exactly.
The momentum convention, all radial seams, the angular mean, and the separate regular cap input are unchanged.

Define
$$
E_0=\int\lambda|u|^2+\gamma|q|^2+\alpha|p|^2,\qquad
E_h=\int\lambda|Ju|^2+\gamma|Jq|^2+\alpha|Jp|^2.             \tag{A.11}
$$
The normalized base matrix from R110 is
$$
H_0=
\begin{pmatrix}
r_u&0&c_*\\
0&r_q&0\\
c_*&0&r_p
\end{pmatrix},
$$
where, for the implemented radial $\lambda$,
$$
\begin{aligned}
r_u&=\lambda_r/\lambda+v_\theta,\\
r_q&=(\gamma_r+v\gamma_\theta)/\gamma-v_\theta,\\
r_p&=(\alpha_r+v\alpha_\theta)/\alpha-v_\theta,\\
c_*&=(\lambda-d)\sqrt{\alpha/\lambda}.                     \tag{A.12}
\end{aligned}
$$
The identity $Jq=DJu$ remains exact after commutation. It is this constraint that cancels the apparent $u$-transport growth.

In the commuted equations, (A.7) gives the principal additions
$$
h_q^{\rm pr}=\tfrac12\alpha_\theta Jp-\tfrac12v_\theta Jq,
\qquad
h_p^{\rm pr}=-\tfrac12v_\theta Jp+\tfrac12\gamma_\theta Jq.
$$
The entire $h_u=[J,\alpha]p-[J,v]q$ is retained as base-energy forcing.
Consequently the actual signed principal energy matrix is exactly
$$
H_h=
\begin{pmatrix}
r_u&0&c_*\\
0&r_q-v_\theta&b_*\\
c_*&b_*&r_p-v_\theta
\end{pmatrix},
\qquad
b_*=\frac{\sqrt{\alpha\gamma}}2
          \left(\frac{\alpha_\theta}{\alpha}
                     +\frac{\gamma_\theta}{\gamma}\right). \tag{A.13}
$$
In particular the half-order transport contribution is kept with its actual sign. It is not estimated by a Fourier norm times $E_h$.

Equation (A.13) is obtained by differentiating the actual constrained commuted state. It does not claim that a separately truncated principal subsystem preserves $Jq=DJu$; no such auxiliary evolution is needed.

Let
$$
g_{0,+}\ge\sup\lambda_{\max}(H_0),\quad
g_{h,+}\ge\sup\lambda_{\max}(H_h),
$$
and similarly $g_{0,-},g_{h,-}$ using $-H_0,-H_h$. All suprema include the whole radial interval, real angular circle, and real parameter box. Set $b_0=g_{0,\pm}/2$, $b_h=g_{h,\pm}/2$ for the chosen direction.

The executable signed path evaluates (A.13) on the same complete closed angular cells and whole radial interval used by the original energy report. It bounds the largest eigenvalue by directed Gershgorin:
$$
g_{h,+}\le\max\{r_u+|c_*|,\ r_q-v_\theta+|b_*|,\
                r_p-v_\theta+|c_*|+|b_*|\},                \tag{A.14}
$$
with the diagonal signs reversed for $g_{h,-}$. These are sufficient bounds, not exact eigenvalue assertions. A more precise certified eigenvalue calculation can later replace them without changing the theorem.

## E. The complete base-driven remainder and source wiring

Write $\lambda_\pm,\gamma_\pm,\alpha_\pm$ for complete positive ranges on the same interval. For the signed method let
$R(a)=W_{3/2}(a)$, bounded by the minimum of the independent complete bounds (A.8)--(A.9). Let
$$
A_d=A(d)\le A(\tau)+D A(\sigma).
$$
The norm of the entire commutator remainder in half-energy variables is at most
$T\sqrt{E_0}$, where $T$ is any outward upper bound for the operator norm of the nonnegative matrix
$$
\mathcal T=
\begin{pmatrix}
0&
 \sqrt{\lambda_+/\gamma_-}A(v)&
 \sqrt{\lambda_+/\alpha_-}A(\alpha)\\
0&
 \sqrt{\gamma_+/\gamma_-}R(v)&
 \sqrt{\gamma_+/\alpha_-}R(\alpha)\\
 \sqrt{\alpha_+/\lambda_-}A_d&
 \sqrt{\alpha_+/\gamma_-}R(\gamma)&
 \sqrt{\alpha_+/\alpha_-}R(v)
\end{pmatrix}.                                             \tag{A.15}
$$
Signs may be discarded in this base-forcing bound because no term is being charged to the half-energy exponential here.

The source product space remains
$$
\mathcal S=H^{1/2}f_0\oplus H^{3/2}f_r\oplus H^{3/2}f_\theta,
$$
with exact physical weights $\max(1,|4k|)^s$. Let $S_h$ be the actual complete R110 source gain. One may always take $S_0=S_h$. A sharper complete base gain is the minimum of $S_h$ and the norm of
$$
\begin{pmatrix}
0&\sqrt{\lambda_+}\| \alpha\|_{\mathcal A_0}&0\\
0&\sqrt{\gamma_+}(\|\alpha\|_{\mathcal A_0}+W_1(\alpha))&0\\
\sqrt{\alpha_+}&
 \sqrt{\alpha_+}(\|v\|_{\mathcal A_0}+W_1(v))&
 \sqrt{\alpha_+}
\end{pmatrix}.                                             \tag{A.16}
$$
The sum $\|\alpha\|_{\mathcal A_0}+W_1(\alpha)$ is the full coefficient multiplier for $H^1$; the source is already in the stronger stipulated $H^{3/2}$ space.

For
$X_0=\sqrt{E_0}$, $X_h=\sqrt{E_h}$ and
$F(r)=\|(f_0,f_r,f_\theta)(r)\|_{\mathcal S}$, the complete comparison inequalities are
$$
\begin{pmatrix}X_0\\X_h\end{pmatrix}'
 \le
 \begin{pmatrix}b_0&0\\T&b_h\end{pmatrix}
 \begin{pmatrix}X_0\\X_h\end{pmatrix}
 +\begin{pmatrix}S_0\\S_h\end{pmatrix}F.                    \tag{A.17}
$$
At a zero energy value, the statement follows by replacing $\sqrt E$ with $\sqrt{E+\varepsilon}$ and passing to the limit. Both $b_0,b_h$ may be negative. The off-diagonal comparison coefficient $T$ is nonnegative.

The program also offers the unsigned method (A.5). In that case $R(a)=D A(a)$ and the half-energy rate is $b_h=b_0+C_1$, where $C_1$ is the largest eigenvalue of the symmetric part of
$$
\frac12
\begin{pmatrix}
\sqrt{\gamma_+/\gamma_-}W_1(v)&
\sqrt{\gamma_+/\alpha_-}W_1(\alpha)\\
\sqrt{\alpha_+/\gamma_-}W_1(\gamma)&
\sqrt{\alpha_+/\alpha_-}W_1(v)
\end{pmatrix}.                                             \tag{A.18}
$$
This gives a second valid full comparison pair. Rates and remainders from different decompositions must not be minimized independently: the selected pair must come from one complete proof.

## F. Ordered two-level Duhamel constants

For an interval of length $\ell$, the exact constant comparison matrix in (A.17) is
$$
P(\ell)=
\begin{pmatrix}
e^{b_0\ell}&0\\
T\ell e^{b_0\ell}\operatorname{exprel}((b_h-b_0)\ell)&
e^{b_h\ell}
\end{pmatrix},\qquad
\operatorname{exprel}(x)=
\begin{cases}(e^x-1)/x,&x\ne0,\\1,&x=0.\end{cases}             \tag{A.19}
$$
No commutativity of different radial intervals is assumed.

Put
$$
J(b,\ell)=\int_0^\ell e^{2bt}\,dt,\quad
b_*=\max(b_0,b_h),\quad
d_*=
\begin{cases}
\min(\ell,1/|b_h-b_0|),&b_h\ne b_0,\\
\ell,&b_h=b_0.
\end{cases}
$$
A complete componentwise $L^2$ source kernel vector is
$$
K_0=S_0\sqrt{J(b_0,\ell)},\qquad
K_h=(S_h+T S_0d_*)\sqrt{J(b_*,\ell)}.                       \tag{A.20}
$$
Indeed
$$
\frac{e^{b_ht}-e^{b_0t}}{b_h-b_0}
=e^{\max(b_0,b_h)t}\frac{1-e^{-|b_h-b_0|t}}{|b_h-b_0|}
\le e^{b_*t}\min(t,1/|b_h-b_0|).
$$
If an interval ball for $b_h-b_0$ includes zero, the executable uses $\ell$ rather than dividing by it. Its exprel fallback is
$\operatorname{exprel}(x)\le e^{\max(0,x)}$ for real $x$.
The analogous $J$ fallback is the already proved R110 one. These rules retain directed rounding for either sign of the rates.

Suppose a closed strict interval is covered in radial order by complete adjacent pieces. The true $\lambda,\gamma,\alpha$ agree continuously at their shared endpoints. If the energy-weight definition is identical, the energy matches exactly; no new norm-equivalence factor is paid at every leaf.

Let $P_j$ and $K_j$ be the full local matrix and source vector. Then
$$
X_{\rm end}\le P_n\cdots P_1X_{\rm start}
       +\sum_j P_n\cdots P_{j+1}K_j\,\|F\|_{L^2(I_j)}.      \tag{A.21}
$$
Define $k_j=P_n\cdots P_{j+1}K_j$. Since the radial supports are disjoint,
$$
X_{{\rm end},i}
 \le (P_n\cdots P_1X_{\rm start})_i
       +\left(\sum_j(k_j)_i^2\right)^{1/2}
                       \|F\|_{L^2(\cup I_j)}.             \tag{A.22}
$$
Backward propagation reverses the piece order and uses the actual negative energy matrices. It is not obtained by commuting the forward matrices.

If a full five-input strong-source Gram $G$ satisfies
$$
\int_{\cup I_j}\|F(r;z)\|_{\mathcal S}^2\,dr\le z^*Gz,
$$
the zero-initial forced endpoint satisfies
$$
E_i(z)\le
 \left(\sum_j(k_j)_i^2\right)z^*Gz.                         \tag{A.23}
$$
This retains all source columns. A sharper piecewise Gram version follows by weighted Cauchy-Schwarz exactly as in R110. The direct regular-cap column is zero in the core Gram but remains present in the full retained system.

If only an initial half-energy bound is supplied, a permitted one-time conversion is
$$
\sqrt{E_0}\le
 \sqrt{\frac{\max(\lambda_+,\gamma_+,\alpha_+)}
              {\min(\lambda_-,\gamma_-,\alpha_-)}}
 \sqrt{E_h}.                                               \tag{A.24}
$$
This follows from $J_k\ge1$ in unweighted $L^2$. It is not inserted at every seam.

Finally, the unchanged R110 coercivity gives
$$
E_h\ge\min(\lambda_-,\gamma_-)\|u\|_{H^{3/2}}^2
                       +\alpha_-\|p\|_{H^{1/2}}^2.
$$
Converting this physical state to canonical/root/label coordinates still requires its actual separate frame map. Strong root and cap feedback, the full high inverse and its scalar compatibilities are not consequences of (A.23) alone.

## G. Executable input contract and status

The new consumer is
[scripts/fourfold_phase_strict_core_tame_energy.py](../scripts/fourfold_phase_strict_core_tame_energy.py).
It takes completed original R110 continuous energy reports. Every input source and dependency hash is checked. For the signed method it also verifies and reloads the original complete nine-field rectangle and exact dyadic arrays. It samples no new geometric primitive.

The underlying evaluator covers the entire declared real radial interval and all closed angular gaps, adding the original complete value, radial and angular error budgets. Its output provides (A.13), (A.9), and optionally complete actual first moments. A single radial or angular point does not meet this contract.

For several input reports, the consumer rejects gaps, overlaps, different actual affine families, different whole real parameter intervals, or a change of energy-weight definition. Its successful output is a strict-interval comparison certificate, not a whole-quarter-core inverse.

Example from the topic directory, after the lost complete nine-field and original energy outputs have actually been restored or rerun:
~~~sh
python scripts/fourfold_phase_strict_core_tame_energy.py \
  --energy-reports notes/strict_core_energy_gate.json \
  --method signed --bits 256 \
  --out notes/strict_core_tame_signed.json
~~~
The optional unsigned path is:
~~~sh
python scripts/fourfold_phase_strict_core_tame_energy.py \
  --energy-reports notes/strict_core_energy_gate.json \
  --method tame --refine-first-moments --bits 256 \
  --out notes/strict_core_tame_unsigned.json
~~~

This supplement and its source were written while the native executor was unavailable. The new consumer has not yet been run. The observed original leaf certificate and its lost full JSON/NPZ must be replayed; its small execution receipt is not an interchangeable proof input. No improved numerical rate, global strict-core propagation, complete high inverse, or nonlinear repair is asserted here.
