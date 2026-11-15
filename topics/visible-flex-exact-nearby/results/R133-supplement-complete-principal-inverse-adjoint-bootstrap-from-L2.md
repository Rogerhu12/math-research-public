# R133 supplement: complete principal inverse by adjoint bootstrap from L2

2026-11-15, visible-exact / phase_inverse.

**Proved analytic estimate; no new scientific execution.** An already established complete real principal inverse on $L^2$ gives a bound for the same inverse on $H^{-4/3}$ using only the first weighted Fourier norm of its nonmean coefficient. The proof retains the auxiliary scalar mean and the two separate physical mean coordinates. It first constructs the adjoint solution using the existing $L^2$ inverse, then proves its additional regularity. It does not infer inverse existence from a formal differential equation.

For the same selected input of PG, this supplies a new logarithmic candidate and a minimum with the original complete PG negative-window candidate. The successful PG computation, when available, is read unchanged. A separate optional sign condition gives an elementary $L^2$ estimate, but no presently available unsigned coefficient bound is asserted to satisfy that condition.

## 1. Original objects and scope

Use the normalized circle of length $\pi/2$, physical frequencies $n=4j$, and
$$
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 I=\partial_\phi^{-1}(1-\Pi),\qquad C_I=\frac{\sqrt{17}}4 .
 \tag{PIB.1}
$$
Let
$$
 c=\nu+b,\qquad \nu=\langle c\rangle\in\mathbb R,\qquad
 \langle b\rangle=0,\qquad T_c=1+M_c I .
 \tag{PIB.2}
$$
All products have their displayed order. In particular $I M_b$ and $M_b I$ are different operators.

The elementary assumptions used below are
$$
 V\ge\|b\|_\infty,\qquad
 B\ge W_{1/3}(b):=
       \sum_{j\in\mathbb Z}(1+|4j|)^{1/3}|\widehat b_j| ,
 \tag{PIB.3}
$$
and an established complete two-sided inverse
$$
 T_c^{-1}:L^2\longrightarrow L^2,\qquad
                        \|T_c^{-1}\|\le K_0 .
 \tag{PIB.4}
$$
Here $b$ is real, and both Fourier signs are included. The complete inverse in MI supplies the existence in (PIB.4); an optional failed Neumann test does not remove that existence.

The elementary weight inequality gives
$$
 \|M_b:H^t\to H^t\|\le B,\qquad |t|\le1/3.
 \tag{PIB.5}
$$
No $W_{4/3}(b)$ estimate is required in this proof. Smoothness of the actual coefficient is not used to insert an uncharged higher derivative.

The exact primary records are:

| Primary statement | Immutable Git blob | SHA256 |
|---|---|---|
| PG, complete first-derivative principal budgets | 58cae91cb563b4f11102ca671cda2929b8dc7ecd | 0a5e4ad71d0d980a097e6c0f4afa8476780a46b4b3e82e5a583633f8bb66ad1a |
| MI, the complete inverse with nonzero scalar mean | 3f02025c20a5c1f2adee59c541f9e2d5434d7af4 | f1fb4dca205a776968f80ab24b79740fdf6e79e875b186e778dace24af871404 |
| IC, individual branch identities and root normalization | bd4ed3ab5d72a10021df281542d080ef2f67fb0e | 4164e4a7a10db651654cf63b7ecf7772fc1ba2cb966da4f9347711156301ddee |

The IC row identifies the proof object. The proof below only uses its exact identities $c_i=-\mu/2+v_i$ and $c_o=\mu/2+v_o$, with the same selected true density input and complete root normalization. It does not use an upper bound for a ratio coefficient as a substitute for either individual coefficient.

## 2. The exact adjoint equation with its scalar mean

For real $\nu$, define
$$
 T_\nu=1+\nu I,\qquad T_\nu^*=1-\nu I,\qquad
 I_{-\nu}=(\partial_\phi-\nu)^{-1}(1-\Pi).
 \tag{PIB.6}
$$
The shifted primitive is defined by its complete Fourier multipliers:
$$
 \widehat{I_{-\nu}f}_j=
 \begin{cases}
   (i4j-\nu)^{-1}\widehat f_j,&j\ne0,\\
   0,&j=0 .
 \end{cases}
 \tag{PIB.7}
$$
It is defined at $\nu=0$ as well. There is no division by the scalar mean. The inverse of $T_\nu^*$ has mean multiplier one and nonmean multiplier $i4j/(i4j-\nu)$. Therefore
$$
 \|(T_\nu^*)^{-1}:H^s\to H^s\|\le1,\qquad
 \|I_{-\nu}:H^s\to H^{s+1}\|\le C_I
 \quad(s\in\mathbb R),
 \tag{PIB.8}
$$
and the exact ordered identity is
$$
                  (T_\nu^*)^{-1}I=I_{-\nu}.
 \tag{PIB.9}
$$

For $f\in H^{4/3}$, first use (PIB.4) to define
$$
                     u=(T_c^*)^{-1}f\in L^2.
 \tag{PIB.10}
$$
Its existing $L^2$ norm is bounded by $K_0\|f\|_2$. Since $I^*=-I$ and $c$ is real,
$$
 T_c^*=1-I M_c=T_\nu^*-I M_b.
$$
Consequently
$$
       u=(T_\nu^*)^{-1}f+I_{-\nu}(bu).
 \tag{PIB.11}
$$
The right shifted primitive only removes the mean in the original occurrence of $I$. The scalar mean equation is still
$\Pi u=\Pi f$, because both $I M_c$ and $I_{-\nu}$ have zero output mean. This is not a replacement of either independent physical mean equation.

## 3. Two successive regularity gains

The first step uses only $bu\in L^2$. Equations (PIB.8)--(PIB.11) imply $u\in H^1$, and hence $u\in H^{1/3}$, with
$$
 \begin{split}
 \|u\|_{H^{1/3}}
 &\le\|f\|_{H^{1/3}}+C_I\|bu\|_2\\
 &\le(1+C_I V K_0)\|f\|_{H^{4/3}} .
 \end{split}
 \tag{PIB.12}
$$
The embeddings $H^1\hookrightarrow H^{1/3}$ and $H^{4/3}\hookrightarrow L^2$ each have norm one in (PIB.1).

The second step now uses the already obtained $H^{1/3}$ regularity, the multiplication bound (PIB.5), and one further shifted primitive:
$$
 \begin{split}
 \|u\|_{H^{4/3}}
 &\le\|f\|_{H^{4/3}}+C_I\|bu\|_{H^{1/3}}\\
 &\le
 \left(1+C_I B+C_I^2 B V K_0\right)\|f\|_{H^{4/3}} .
 \end{split}
 \tag{PIB.13}
$$
The two uses of the primitive occur in two successive estimates for the same $u$. No new inverse and no second independent solution is introduced.

For completeness, $T_c^*$ is a bounded map on $H^{4/3}$ under the stated assumptions: embed into $H^{1/3}$, multiply by the constant $\nu$ and by $b$, and apply $I:H^{1/3}\to H^{4/3}$. Its $L^2$ inverse just shown to preserve $H^{4/3}$ is therefore a two-sided inverse on that space. The original $L^2$ uniqueness proves both compositions there.

Taking the Hilbert-space dual gives the same distributional inverse on the negative window:
$$
 \boxed{\quad
 \|T_c^{-1}:H^{-4/3}\to H^{-4/3}\|
       \le K_-^{\rm boot}:=1+C_I B+C_I^2 B V K_0 .
 \quad}
 \tag{PIB.14}
$$
The boundedness of $T_c$ on this window also follows directly from
$I:H^{-4/3}\to H^{-1/3}$, (PIB.5), and
$H^{-1/3}\hookrightarrow H^{-4/3}$. On the dense subspace $L^2$ the dual inverse equals the original inverse in (PIB.4). Thus the two windows refer to one operator, including the full scalar mean, and not to unrelated extensions.

## 4. A new logarithmic candidate without evaluating an exponential

Suppose the complete saved PG certificate is
$$
                    K_0\le e^{L_0},\qquad L_0\ge0.
 \tag{PIB.15}
$$
The exponential here states the meaning of the saved logarithm; it need not be evaluated. Since $e^{L_0}\ge1$, (PIB.14) gives
$$
 K_-^{\rm boot}
 \le e^{L_0}\left(1+C_I B+C_I^2 B V\right).
$$
The new complete logarithmic candidate is therefore
$$
 \boxed{\quad
 L_-^{\rm boot}
   =L_0+\log\left(1+C_I B+C_I^2 B V\right).
 \quad}
 \tag{PIB.16}
$$
If $L_-^{\rm PG}$ is the original whole PG negative-window certificate, then
$$
 \|T_c^{-1}:H^{-4/3}\to H^{-4/3}\|
 \le
 \exp\left(\min\{L_-^{\rm PG},L_-^{\rm boot}\}\right).
 \tag{PIB.17}
$$
Each entry of this minimum is a complete bound for the same inverse, on the same negative window and in the same selected input chart. This is not an entrywise minimum across different operators or an inference from subtracting upper bounds.

A new current-only consumer may read, verbatim, the following complete fields from a successful PG receipt:

| Existing field | Role here |
|---|---|
| complete_new_nonmean_primitive_conclusion.complete_V0_upper | $V$ |
| complete_new_nonmean_primitive_conclusion.complete_B_one_third_upper | $B$ |
| complete_new_nonmean_primitive_conclusion.complete_I_derivative_gain_constant | $C_I$ |
| complete_new_log_inverse_conclusion.complete_log_L2_inverse_upper | $L_0$ |
| complete_new_log_inverse_conclusion.complete_log_Hminus4_3_inverse_upper | $L_-^{\rm PG}$ |

Only the new positive scalar products, one logarithm and the same-window whole minimum are evaluated. Every read upper endpoint is used in a monotone increasing expression. The product inside the logarithm is at least one. The consumer preserves the old $L_0$ and $L_-^{\rm PG}$ records unchanged, and records the new candidate and selected complete minimum separately. It never evaluates either exponential or reruns a PG, CG, TF, WX or SN producer.

This same uniform construction applies to both $T_{c_i}$ and $T_{c_o}$ when PG provides the common complete $V,B,L_0$ bounds. It makes no claim for a different selected angle or an unproved family of conjugacies.

## 5. Optional strictly signed coefficient

There is also an elementary additional $L^2$ estimate. Suppose one has independently proved, for one actual complete coefficient,
$$
             \sigma c(\phi)\ge\kappa>0
 \quad\hbox{on the full real circle},\qquad \sigma\in\{-1,1\}.
 \tag{PIB.18}
$$
For $h=T_c^{-1}f$ let $v=Ih$ and $m=\Pi h$. Then
$$
                 f=v'+m+cv,\qquad \Pi v=0.
$$
For complex-valued inputs use the real part of the Hermitian pairing. Periodicity and the exact zero mean of $v$ give
$$
 \operatorname{Re}\langle f,v\rangle
       =\int c|v|^2,\qquad
                \|v\|_2\le\kappa^{-1}\|f\|_2 .
 \tag{PIB.19}
$$
The missing mean is not discarded: its pairing with this particular $v$ is exactly zero. The complete solution still has the mean determined by MI.

Use the ordered identity from MI,
$$
                       h=T_\nu^{-1}(f-bv).
$$
The constant-mean inverse is contractive, so
$$
 \boxed{\quad
       \|T_c^{-1}:L^2\to L^2\|\le1+\frac{V}{\kappa}.
 \quad}
 \tag{PIB.20}
$$
The weaker estimate $1+\|c\|_\infty/\kappa$ also follows by estimating $h=f-cv$ directly. Formula (PIB.20) retains the useful exact constant-mean contraction.

For the individual IC coefficients, a sufficient additional test would be a signed mean interval and
$$
                 \frac{|\mu|_{\rm lower}}2>V_\sigma ,
 \tag{PIB.21}
$$
which supplies $\kappa=|\mu|_{\rm lower}/2-V_\sigma$. Alternatively, because the true density map has positive derivative, a complete signed lower bound for
$C_{\sigma,c}+g_\sigma-F_*$ before that density change supplies a signed lower bound afterwards using its independently established derivative lower bound.

The existing unsigned CG and PG coefficients alone do not supply either signed hypothesis. The exact means $-\mu/2,+\mu/2$ do not imply pointwise signs. No actual sign gate is claimed here, and no signed test is required for (PIB.14)--(PIB.17).

## 6. Physical interfaces retained

The theorem concerns the complete scalar principal factors in the same selected true common input of IC and PG. If two independent physical means are adjoined, extend the principal inverse by their identity blocks and retain every finite rank difference between full density and identity-on-mean realizations.

The actual incoming and outgoing errors, original finite/high and high/finite maps, sign and Maslov selectors, stable normalization, root rows, and physical matching means are unchanged. The inverse in this note is not an inverse of the complete incoming operator. No finite Schur inverse, full return remainder, nonlinear background or final surface is asserted.

In particular a previously proved high-block estimate that uses the complete $L^2$ principal inverse continues to use its $L^2$ constant in that position. The new negative-window source constant cannot be moved to that output position merely because both constants belong to the same inverse.
