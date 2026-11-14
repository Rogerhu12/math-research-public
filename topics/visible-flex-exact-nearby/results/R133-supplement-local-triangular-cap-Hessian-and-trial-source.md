# R133 supplement: local triangular cap Hessian and complete trial sources

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved.** At the exactly continuous repair of the final `ac1d5b98` centre,
the complete residual-sensitive conjugation on $[9/10,25/8]$ has an
upper triangular zero-order source bound in the physical $(B,C)$ variables.
The companion computation consumes all 1,341 genuine residual cells and
records its complete local coefficients. It does not recompute the target,
replace a complete Fourier output by a truncation, or assume that a cap
trial is an exact solution.

The actual residual input has affine parameter **$\eta=\eta_0$**, with
offset $\delta\eta=0$. The earlier physical background transfer holds for
the whole original parameter interval; that larger permission is not
asserted for this residual-sensitive bridge.

## 1. Same object and already paid complete Green operator

Use the exact repaired definition
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`
and the notation of
[the continuous physical-cap conjugation](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md).
Write $x=D\Psi h=(x_B,x_C)$, $Q=(u,v)$, $m=\langle v\rangle_\phi$,
$W=(B,C)$ and $R=Q_r-F(Q)$. Every quantity below is at this same centre.

The complete physical module is

$$
 \|x\|_{\mathfrak M}
 =\left(\sum_k\sup_r|x_{B,k}(r)|^2\right)^{1/2}
 +\left(\sum_k\sup_r|x_{C,k}(r)|^2\right)^{1/2}.
 \tag{L.1}
$$

The physical Green operator $G$ already includes the full coefficient
feedback and the genuine exterior derivative. Its ordinary-source gains
are $G_{o,B},G_{o,C}$, and its angular-divergence module gains are
$G_{d,B},G_{d,C}$. They are read, without a second background feedback,
from the complete bridge input. The original additional Hessian feedback
satisfies

$$
 \chi_H<0.003840162,
 \qquad (1-\chi_H)^{-1}<1.003855.
 \tag{L.2}
$$

All physical mean rows and true inner/outer ports remain part of $G$.

## 2. The physical even reconstruction is independent of $x_B$

Let $U,V,C_*,B_*,C_1,B_1$ be the already proved bounds for
$|u|,|v|,|C|,|B|,|C_\theta|,|B_\theta|$ and let $J_*$ be the
complete physical-to-moving measure bound. Put

$$
 I_*=(1+J_*)/4,
 \qquad p_C=I_\theta(x_C-mC\langle x_C\rangle_\theta).
 \tag{L.3}
$$

The full inverse differential, including the physical even mean, is

$$
 h=\begin{pmatrix}v&-uv\\0&-v^2\end{pmatrix}
       \{x-vW_\theta p_C\}.
 \tag{L.4}
$$

Thus, in the physical $L^2$ measure,

$$
 \|h_1\|_2\le V\|x_B\|_2+H_C\|x_C\|_2,
 \qquad \|h_2\|_2\le H_2\|x_C\|_2,
 \tag{L.5}
$$

where

$$
 H_C=UV+V^2(B_1+UC_1)I_*,
 \qquad H_2=V^2(1+VC_1I_*).
 \tag{L.6}
$$

The value of $H_2$ is the same proved bound used in the original bridge.
In particular the second component in (L.4) is exactly independent of
$x_B$; this assertion includes its mean and is not a projection argument.

## 3. Local complete source coefficients

On a true residual cell $I_i$, let $r_{U,0},r_{V,0}$ bound the complete
physical-normalized moving residuals in $A^0$, and let
$r_{U,1},r_{V,1}$ be their complete inhomogeneous $A^1$ bounds.
The new consumer uses the original per-cell fields
`complete_residual_A0` and `complete_residual_A1`, multiplies by the exact
$\alpha=6890507429876859/9007199254740992$, and adds the already proved
continuous-repair residual difference of the corresponding order.
No residual component, mean, or primitive error is omitted.

With the complete inverse-angle displacement bound $h_*$, set

$$
 \begin{aligned}
 R_{V,A}&=r_{V,0}+\sum_{j=1}^{96}
       \min\{r_{V,0},r_{V,1}/(1+4j)\}e^{4jh_*},\\
 E_A&=C_*R_{V,A}/4,&
 E_\infty&=\pi C_*r_{V,0}/8,&E_1&=2C_*r_{V,0},\\
 t_B&=C_*r_{U,0}+B_*C_*r_{V,0},&t_C&=C_*^2r_{V,0},\\
 t_{B,1}&=C_1r_{U,0}+C_*J_*r_{U,1}
       +(B_1C_*+B_*C_1)r_{V,0}+B_*C_*J_*r_{V,1},\\
 t_{C,1}&=2C_*C_1r_{V,0}+C_*^2J_*r_{V,1},\\
 b_*&=C_*^2r_{V,0}/4+2C_*E_\infty.
 \end{aligned}
 \tag{L.7}
$$

The number 96 is the exact coefficient support of the centre residual.
It is not a bound on an unknown variation or a trial output.
Equation (C.20) of the original theorem reads

$$
 D^2\Psi[R,h]=-e x_\theta+Zx,
 \qquad e=I_\theta(CR_2).
 \tag{L.8}
$$

Its zero-order part satisfies the complete componentwise estimate

$$
 \begin{pmatrix}\|(Zx)_B\|_2\\\|(Zx)_C\|_2\end{pmatrix}
 \le
 \begin{pmatrix}Z_{BB}&Z_{BC}\\0&Z_{CC}\end{pmatrix}
 \begin{pmatrix}\|x_B\|_2\\\|x_C\|_2\end{pmatrix},
 \tag{L.9}
$$

where

$$
 \begin{aligned}
 Z_{BB}&=t_CV,\\
 Z_{BC}&=t_CH_C+
   (C_*t_B+B_*t_C+t_{B,1}C_*/4+B_1b_*)H_2,\\
 Z_{CC}&=(2C_*t_C+t_{C,1}C_*/4+C_1b_*)H_2.
 \end{aligned}
 \tag{L.10}
$$

Indeed $DP[t]h$ contributes $(t_Ch_1-(C_*t_B+B_*t_C)h_2,
-2C_*t_Ch_2)$ in modulus. The term $-t_\theta e_h$ uses
$\|e_h\|_2\le C_*\|h_2\|_2/4$. The entire remaining bracket,
including both mean pairings, is bounded by $b_*\|h_2\|_2$.
Substitution of (L.5) gives (L.10). No $C_{\theta\theta}$, derivative
of the centre residual beyond first angular order, or inverse frequency
on the mean is introduced.

Writing $-ex_\theta=\partial_\theta(-ex)+e_\theta x$, the ordinary
source therefore has local matrix

$$
 O_i=\begin{pmatrix}E_1+Z_{BB}&Z_{BC}\\0&E_1+Z_{CC}\end{pmatrix}.
 \tag{L.11}
$$

## 4. Consuming an actual complete cap trial

Consider any finite collection of physical trial columns $T_a$, with
an explicitly orthonormal input basis. Every formula is also valid for
a single trial. Suppose genuine local coefficient envelopes give

$$
 b_i^2=\sum_{k,a}\sup_{r\in I_i}|T_{B,k,a}(r)|^2,
 \qquad c_i^2=\sum_{k,a}\sup_{r\in I_i}|T_{C,k,a}(r)|^2.
 \tag{L.12}
$$

Any unretained Fourier output must be included in these envelopes or
paid separately by the complete Green gains. Define

$$
 \begin{aligned}
 D_B^2&=\sum_i(E_{A,i}b_i)^2,&D_C^2&=\sum_i(E_{A,i}c_i)^2,\\
 O_B^2&=\sum_i |I_i|\big[(E_{1,i}+Z_{BB,i})b_i+Z_{BC,i}c_i\big]^2,\\
 O_C^2&=\sum_i |I_i|\big[(E_{1,i}+Z_{CC,i})c_i\big]^2.
 \end{aligned}
 \tag{L.13}
$$

Then the full physical Green response to the actual Hessian defect is
bounded in $\mathfrak M$ by

$$
 \mathcal E_H(T)
 \le G_{d,B}D_B+G_{d,C}D_C+G_{o,B}O_B+G_{o,C}O_C.
 \tag{L.14}
$$

For the divergence terms, the coefficientwise supremum over the whole
cap is at most the square sum of the suprema on its cells. Young's
complete Fourier convolution inequality on each cell proves the first
line of (L.13). There is **no cell-length factor** in these module
terms. A sharper implementation can form actual product coefficients
and take their maximum over cells before summing modes. Replacing that
coefficientwise operation by a maximum of local $L^2$ norms is not
authorized. For the ordinary terms, genuine radial $L^2$ integration
gives the cell-length factors in the remaining lines.

Let $x_{\rm phys}$ be the exact physical cap solution for the same full
ports and let an independently certified trial defect give
$\|x_{\rm phys}-T\|_{\mathfrak M}\le\varepsilon_T$. The true moving
solution in physical variables obeys $x_{\rm mov}=x_{\rm phys}+Ax_{\rm mov}$,
where $A=G D^2\Psi[R,D\Psi^{-1}(\cdot)]$ and $\|A\|<\chi_H$.
Consequently

$$
 \boxed{\quad
 \|x_{\rm mov}-T\|_{\mathfrak M}
 \le\frac{\varepsilon_T+\mathcal E_H(T)}{1-\chi_H}.
 \quad}
 \tag{L.15}
$$

This pays the actual decay of each trial column without charging its
largest value over the entire cap. It does not equate a physical trial
with a moving solution. All inner data errors, outer regular errors,
mean errors and true jumps belong in $\varepsilon_T$ with their original
gains. A subsequent physical-to-moving boundary transformation retains
its own already paid norm and full high-output remainder.

## 5. Actual computation and exact scope

The new consumer
`scripts/fourfold_codazzi_local_cap_Hessian_source.py` completed eight
gates in 3.254 seconds and read the original complete 7,296-row residual
certificate. All 1,341 cap cells were consumed. Its outward bounds give

| Local coefficient | Maximum on the complete cap |
|---|---:|
| $E_A$ | $<4.006101\,10^{-6}$ |
| $E_\infty$ | $<2.887603\,10^{-8}$ |
| $E_1$ | $<1.470644\,10^{-7}$ |
| $Z_{BB}$ | $<1.392831\,10^{-7}$ |
| $Z_{BC}$ | $<2.835041\,10^{-5}$ |
| $Z_{CC}$ | $<2.652684\,10^{-5}$ |

The complete native is
`notes/2026-11-14-R133-complete-local-cap-Hessian-source-native.json.gz`.
Each row records its exact interval, normalized and repaired residual
permissions, and the six coefficients in the table. The native also
preserves the original complete Green gains and bridge resolvent.

The exact invocation, from the topic directory, is

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps OPENBLAS_NUM_THREADS=1 \
python scripts/fourfold_codazzi_local_cap_Hessian_source.py \
  --residual /workspace/scratch/ac0d699811ad/continuous-final-20261114/complete-merged.json.gz \
  --out notes/2026-11-14-R133-complete-local-cap-Hessian-source-native.json.gz
```

No trial is consumed by this computation. Thus (L.15) is a complete
source contract, while a numerical graph-error conclusion still requires
the actual trial envelopes and its full physical residual. The whole
mixed-body inverse, the negative return, the parameter Schur complement
and a nonlinear iteration are not concluded here.
