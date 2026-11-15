# R133 supplement: complete principal inverse from first-derivative budgets

2026-11-15, visible-exact / root.

**Proved analytic extension and exact consumer contract.** The real complete principal factors of WY can be bounded on both $L^2$ and $H^{-4/3}$ using the separate CG zeroth and first angular budgets, the completed TF root coefficient, and the already saved first two derivatives of the selected WX coordinate. A third derivative of that coordinate is not required. The inverse is the same mean-complete inverse as MI. The negative-window argument uses the one derivative gained by its shifted primitive before multiplication by the nonconstant coefficient.

This is a new low-regularity estimate for the current selected reference principal factors. It does not supply the complete physical incoming inverse, any retained border, a true-background perturbation bound, or the nonlinear solution. No new numerical mathematics is performed here. Every later scalar evaluation is restricted to the public repository's Actions.

## PG1. The same individual coefficients and selected coordinate

Use normalized measure on the physical period $P=\pi/2$, frequencies $4j$, and
$$
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 I=\partial_x^{-1}(1-\Pi),\qquad
 W_s(f)=\sum_{j\in\mathbb Z}(1+4|j|)^s|\widehat f_j|.
 \tag{PG.1}
$$
The exact identifications are [WY.49--50](R133-supplement-four-ordered-waist-receivers-and-complete-strong-error-assembly.md) and [CG.27--30](R133-supplement-separate-cut-and-propagated-first-coefficient-budgets.md):
$$
 \widetilde C_\sigma=C_\sigma-F_*,
 \quad C_\sigma=C_{\sigma,c}+g_\sigma,\qquad
 c_i=\mathcal S\widetilde C_+,\quad
 c_o=\mathcal S\widetilde C_-,
 \quad \mathcal S=U_\psi,\quad
 \psi=X_-\circ\mathcal H^{-1}.
 \tag{PG.2}
$$
Here $U_\psi f=\psi'(f\circ\psi)$ is the true density pullback. Both $c_i,c_o$ are real by the complete WY branch identification. The two input Fourier signs define these same real scalar functions; the Airy phase multiplier remains in its original separate operator position.

The WX map $\psi$ and all uses of $\mathcal H$ below refer only to the same accepted selected member. Bounds for this selected map do not assert a family of conjugacies throughout the larger real parameter interval. The independent physical means of the waist state are not identified with the scalar Fourier zero mode.

Suppose a completed CG receipt supplies the whole per-branch sup bounds
$$
 h_0\ge\|C_\sigma\|_\infty,\qquad
 h_1\ge\|\partial_\phi C_\sigma\|_\infty
 \quad(\sigma=\pm1).
 \tag{PG.3}
$$
These are the separate sums $h_j=c_j+g_j$ of CG.16. They are not inferred by subtracting any total upper bounds.

The completed TF coefficient has Fourier label support $|j|\le192$ and full $W_0$ bound $F_A$, including its mean. Therefore
$$
 \|F_*'\|_\infty\le 768F_A,\qquad
 t_0=h_0+F_A,\qquad t_1=h_1+768F_A .
 \tag{PG.4}
$$
The factor 768 is the physical angular frequency $4\cdot192$; it does not describe a finite support for either composed coefficient $C_\sigma$.

Read the complete WX bounds $M_\psi\ge\|\psi'\|_\infty$ and
$F_\psi\ge\|\psi''\|_\infty$. Direct differentiation of (PG.2) gives
$$
 c=\psi'(\widetilde C\circ\psi),\qquad
 c'=\psi''(\widetilde C\circ\psi)
       +(\psi')^2(\widetilde C'\circ\psi).
$$
Thus the two new scalar expressions
$$
 A_0=M_\psi t_0,\qquad
 A_1=F_\psi t_0+M_\psi^2t_1
 \tag{PG.5}
$$
satisfy
$$
 \|c_i\|_\infty,\|c_o\|_\infty\le A_0,\qquad
 \|c_i'\|_\infty,\|c_o'\|_\infty\le A_1.
 \tag{PG.6}
$$
These are sup estimates; no density Jacobian is omitted in converting an $L^2$ estimate. Normalized measure subsequently gives the corresponding $L^2$ bounds. Only $\psi'$ and $\psi''$ occur.

## PG2. Complete nonmean and primitive budgets

For either one of the two real coefficients set
$$
 \vartheta=\Pi c,\qquad b=c-\vartheta,\qquad p=Ib.
 \tag{PG.7}
$$
The symbol $\vartheta$ is the coefficient mean, not the geometric parameter $\nu_0$. In the WY/IC normalization the two exact means are $-\mu/2$ and $\mu/2$; no numerical value of $\mu$ is needed for the following bounds.

All zero-mean statements in (PG.7) follow from the exact definition. They do not discard an independent physical mean port. The following complete bounds use both Fourier signs and the entire nonzero spectrum:
$$
 \begin{split}
 V_0&=\min\{2A_0,A_1/2\}\ge\|b\|_\infty,\\
 P_0&=\min\{\pi V_0/8,A_1/8\}\ge\|p\|_\infty,\\
 B_{1/3}&=\frac{39}{32}A_1\ge W_{1/3}(b),\\
 P_{4/3}&=\frac{243}{160}A_1\ge W_{4/3}(p).
 \end{split}\tag{PG.8}
$$
Each minimum compares complete upper bounds for exactly the same norm.

For $V_0$, first use $|\Pi c|\le A_0$. Independently, the signed sum
$\sum_{j\ne0}|4j|^{-2}\le1/4$ and $b'=c'$ give
$W_0(b)\le\|c'\|_2/2$. The mean-zero primitive kernel on the period-$\pi/2$ circle has $L^1$ norm $\pi/8$, yielding the first candidate for $P_0$. Since $p=I^2c'$, the full signed Cauchy--Schwarz sum
$(\sum_{j\ne0}|4j|^{-4})^{1/2}<1/8$ yields the second.

For the last two estimates, use the full signed tail
$$
 \left(\sum_{j\ne0}|4j|^{-4/3}\right)^{1/2}<\frac98,
$$
and, for $n\ge4$,
$$
 (1+n)^{1/3}\le\frac{13}{12}n^{1/3},\qquad
 (1+n)^{4/3}\le\frac{27}{20}n^{4/3}.
$$
Cauchy--Schwarz against $b'=c'$ gives $39/32$, and against
$p''=c'$ gives $243/160$. These are the same two-sign estimates proved in [CG.17](R133-supplement-separate-cut-and-propagated-first-coefficient-budgets.md) and [LN.14--20](R133-supplement-lower-order-normalizer-budgets-from-complete-terminal-columns.md), applied here to exact zero-mean functions. No $H^3$ upper is divided by frequency to manufacture a lower derivative.

In particular $c\in H^1$ suffices, $b\in W_{1/3}$, and $p\in W_{4/3}$. This is less regularity than the sufficient $H^3$ assumption stated at the beginning of MI.

## PG3. The unchanged full-circle inverse

Write $a=e^p$. For real $\vartheta$, retain the full operators
$$
 (I_\vartheta f)_j=\frac{f_j}{i4j+\vartheta}\ (j\ne0),
 \quad (I_\vartheta f)_0=0,\qquad
 J_\vartheta=\Pi+\vartheta I_\vartheta.
 \tag{PG.9}
$$
They satisfy
$$
 \|J_\vartheta:H^s\to H^s\|\le1,\quad
 \|I_\vartheta:H^s\to H^s\|\le\frac14,\quad
 \|I_\vartheta:H^s\to H^{s+1}\|\le C_I:=\frac{\sqrt{17}}4 .
 \tag{PG.10}
$$
The mean multiplier of $J_\vartheta$ is one. At $\vartheta=0$, it is exactly $\Pi$. Its complete positive probability kernel and Jensen's inequality give the same denominator
$$
 d_\vartheta=\langle a^{-1}J_\vartheta a\rangle\ge1,\qquad
 \langle a^{-1}\rangle\ge1.
 \tag{PG.11}
$$
No estimate divides by $\vartheta$.

Use the exact same ordered formula as [MI.8--13](R133-supplement-complete-real-principal-inverse-with-nonzero-mean.md):
$$
 \begin{split}
 m(f)&=\frac{\langle a^{-1}J_\vartheta(af)\rangle}{d_\vartheta},\\
 u(f)&=I_\vartheta[a(f-m(f))],\\
 \kappa(f)&=-\frac{\langle a^{-1}u(f)\rangle}{\langle a^{-1}\rangle},\\
 v(f)&=a^{-1}(u(f)+\kappa(f)),\\
 T_c^{-1}f&=T_\vartheta^{-1}\{f-bv(f)\},\qquad
 T_c=1+M_cI,\quad T_\vartheta=1+\vartheta I .
 \end{split}\tag{PG.12}
$$
The constant Fourier multiplier of $T_\vartheta^{-1}$ is one; its other multipliers are $i4j/(i4j+\vartheta)$. It is a contraction on every $H^s$.

Both scalar mean equations are retained:
$$
 \langle v\rangle=0,\qquad
 v'+cv=f-m(f),\qquad I(T_c^{-1}f)=v.
 \tag{PG.13}
$$
The first line of (PG.12) supplies the missing constant equation for the shifted primitive. Omitting that line or $\kappa$ would change the inverse.

## PG4. The L2 bound and its logarithmic envelope

The probability-density argument of MI.14--17 uses only $P_0,V_0$. It therefore gives for the same inverse
$$
 K_0^{\rm ODE}=1+V_0Z(P_0),\qquad
 Z(P)=\frac14e^{2P}(1+e^P)^2,
 \qquad \|T_c^{-1}:L^2\to L^2\|\le K_0^{\rm ODE}.
 \tag{PG.14}
$$
If the directed test $V_0<4$ succeeds, the full factorization
$T_c=T_\vartheta(1+T_\vartheta^{-1}M_bI)$ also gives
$(1-V_0/4)^{-1}$. Its minimum with (PG.14) is a valid whole bound. Failure of that optional gate is not failure of the exact inverse.

To record a finite norm bound without constructing a very large exponential, use
$$
 L_0=\log(1+V_0)+4P_0,\qquad
 \|T_c^{-1}:L^2\to L^2\|\le e^{L_0}.
 \tag{PG.15}
$$
Indeed $Z(P)\le e^{4P}$ for $P\ge0$, and
$1+V_0e^{4P_0}\le(1+V_0)e^{4P_0}$.
A saved directed upper for $L_0$, together with this exact interpretation, is a complete logarithmic norm certificate. It is not itself the numerical norm $K_0$.

## PG5. Use the gained derivative in the negative window

Put $M=e^{P_{4/3}}$. Submultiplicativity of $W_{4/3}$ gives
$$
 W_{4/3}(a),W_{4/3}(a^{-1})\le M.
 \tag{PG.16}
$$
For $f\in H^{-4/3}$, the complete first row in (PG.12) costs at most $M^2$. Apply the derivative-gaining estimate in (PG.10) before multiplying by $b$:
$$
 \begin{split}
 |m(f)|&\le M^2\|f\|_{H^{-4/3}},\\
 \|u(f)\|_{H^{-1/3}}
      &\le C_I M(1+M^2)\|f\|_{H^{-4/3}},\\
 |\kappa(f)|&\le M\|u(f)\|_{H^{-1/3}},\\
 \|v(f)\|_{H^{-1/3}}
      &\le C_I M^2(1+M)(1+M^2)\|f\|_{H^{-4/3}}.
 \end{split}\tag{PG.17}
$$
The $\kappa$ estimate is a complete $H^{1/3}$ dual-row estimate; $W_{4/3}(a^{-1})$ bounds that row as well. It is not a pointwise estimate of a distribution.

Now use $M_b:H^{-1/3}\to H^{-1/3}$ with norm $B_{1/3}$, followed by the norm-one embedding $H^{-1/3}\hookrightarrow H^{-4/3}$, and finally the full $T_\vartheta^{-1}$ contraction in its original left position. This proves
$$
 \boxed{\quad
 \|T_c^{-1}:H^{-4/3}\to H^{-4/3}\|
 \le K_-^{\rm gain}
 :=1+C_I B_{1/3}M^2(1+M)(1+M^2).
 \quad}\tag{PG.18}
$$
The intermediate multiplier window is exactly $-1/3$. A bound for $W_{4/3}(b)$, and thus a second derivative of $c$ or third derivative of $\psi$, is not used.

The full negative-window perturbation $T_\vartheta^{-1}M_bI$ has the additional bound $C_IB_{1/3}$. Only if this directed bound is strictly below one may
$(1-C_IB_{1/3})^{-1}$ be included in the whole minimum.

A complete logarithmic envelope requiring only new small scalar arithmetic is
$$
 L_-=\log(1+4C_IB_{1/3})+5P_{4/3},\qquad
 \|T_c^{-1}:H^{-4/3}\to H^{-4/3}\|\le e^{L_-}.
 \tag{PG.19}
$$
Here $M^2(1+M)(1+M^2)\le4e^{5P_{4/3}}$.
If $b=0$, the exact choices $V_0=B_{1/3}=P_0=P_{4/3}=0$ recover the contraction bound one on both spaces. Positive upper budgets need not detect that special case.

## PG6. Justification under the stated low regularity

For smooth real $c$, the differential identities and uniqueness are exactly MI.9--13. For real $c\in H^1$, Fourier smoothing with the same mean gives
$b_n\to b$ in $W_{1/3}$ and $p_n\to p$ in $W_{4/3}$, by the same full signed estimates as PG2. The exponential maps converge in $W_{4/3}$; the strictly positive denominators stay at least one.

All operations in (PG.12) consequently converge as bounded maps on $L^2$ and on $H^{-4/3}$, with the latter primitive outputs in $H^{-1/3}$. Also $T_{c_n}\to T_c$ on those two spaces: on $L^2$ use uniform convergence of $c_n$, and on $H^{-4/3}$ use $I:H^{-4/3}\to H^{-1/3}$ followed by the $W_{1/3}$ multiplier estimate and embedding. Passing to the limit in both inverse identities proves a common two-sided inverse. The two mean equations survive as continuous dual pairings.

Thus (PG.18) is not a separate formal distributional solution. It bounds the same operator as (PG.14). Independent physical means are extended by their identity blocks, while every rank difference between that convention and a full-density convention remains explicitly in the existing physical assembly.

## PG7. Exact readout, no repetition of successful mathematics

A later current-only consumer reads the following completed fields or their whole literal copies:

| Input | Exact role | New use |
|---|---|---|
| Completed CG science | The full three-entry array $h_j=c_j+g_j$, including $h_0,h_1$ | (PG.4)--(PG.5); no cut, ray, or source integral is repeated |
| Completed TF science, run43766881076/1 | The full-root $F_A$, true degree192 and both physical means | The new first-derivative fee $768F_A$; no TF cutoff or inverse is recomputed |
| Completed WX execution, run43763424840/1 | Under actual_scientific_receipt.complete_selected_common_input_conclusion, common_input_derivative_upper and common_input_second_derivative_upper | The exact same selected $\psi'$, $\psi''$ in (PG.5) |
| WY and CG complete analytic identification | Same $c_i,c_o$, reality, root subtraction and density order | Qualifies (PG.2); no relation between upper bounds substitutes for function identity |
| MI full inverse | Complete shifted primitive, probability kernel, both scalar mean equations | Same inverse (PG.12); no old numerical normalizer is rerun |

The new small conclusion retains $t_0,t_1,A_0,A_1,V_0,P_0,B_{1/3},P_{4/3},L_0,L_-$ separately. If a direct exponential value is evaluated, it is separately labelled and saved; its absence does not negate the exact logarithmic bounds (PG.15), (PG.19). Optional Neumann tests must be strict directed tests, not point estimates. A failed optional test is recorded as such without calling the full inverse singular.

The original successful CG, TF and WX inputs are frozen. Only the displayed new scalar products, minima, and logarithmic envelopes are evaluated. Any saved direct inverse or logarithmic envelope is thereafter read without repetition. No new Fourier arrays, angle integration or radial data are needed.

These bounds are for $T_{c_i}^{-1}$ and $T_{c_o}^{-1}$. To use the physical incoming high-block theorem MI.24--28, the same fully qualified complete $E_i:H^{-4/3}\to L^2$ must first include every retained rank, physical mean and finite column. An error upper for only the paid high-input part does not meet that hypothesis. The preconditioned finite Schur block, full strong return, genuine nonlinear background and final geometric construction remain separate.

## PG8. Immutable primary identities

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| MI complete real principal inverse | 3f02025c20a5c1f2adee59c541f9e2d5434d7af4 | 12991 | f1fb4dca205a776968f80ab24b79740fdf6e79e875b186e778dace24af871404 |
| LN complete signed Fourier inequalities | e0ffc101b096d5216cdf690ee84a624310ded477 | 13407 | 53a3dd1dd637a61aec843262d51a2686ef9cf13f5478df4c62b93437db1c6da6 |
| WY same individual real coefficients | 847a7dd335158482811561c2ed5e1aa7175e8797 | 30764 | ebf8713508a11ef96decc5691056ea6eaa15d967d08b3a8af4b20c4284f6d1b3 |
| CG separate coefficient and ordered fees | e1af6de6c25643fd1e7669824ca4db2c52155eaa | 21714 | a66ad4c41c831a1d5efd343874c11945edd4cc2b04a39752ddd99d8b16aa72ff |
| TF completed full-root scalar science | 3766aea85aba59230be3813b4b7634d318316e49 | 18206 | a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720 |
| WX completed selected-coordinate execution | 5121a599896025d90e2861450756a256aaba659d | 43753 | e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12 |

The CG numerical readout is not asserted complete by this analytic text. Its exact successful identity must be pinned before the new PG consumer runs.
