# Full-mean physical Sobolev multipliers from complete C2 bounds

2026-11-13, reproduce-newton.

**Proved bounds; unrun native consumers.** This supplement improves only
the coefficient multiplier inputs. It does not supply new geometric
values or an actual whole-core growth rate.

The helper
[scripts/fourfold_physical_sobolev_multipliers.py](../scripts/fourfold_physical_sobolev_multipliers.py)
retains the exact mean and the physical nonzero frequency gap four.
The new entry
[scripts/fourfold_phase_strict_core_kernel_tame_energy_v2.py](../scripts/fourfold_phase_strict_core_kernel_tame_energy_v2.py)
uses it on the same complete nine-field certificate and minimizes its
full source multiplier bounds against the old complete Fourier ones.
The original consumer and all old reports remain unchanged.

## 1. Exact norm convention and coefficient assumptions

Throughout the main calculation use
$$
 \|f\|_{s,*}^2=\sum_{k\in\mathbb Z}
       \max(1,|4k|)^{2s}|f_k|^2,\qquad
 J=\max(1,|D_\theta|)^{1/2}.
 \tag{M.1}
$$
This is the norm explicitly declared in the original
fourfold_phase_strict_core_energy.py and its source-product-space field.
The factors $(1+|4k|)^s$ in its **multiplier upper bounds** do not change
the underlying norm (M.1).

Let
$$
 a_\infty\ge\|a\|_\infty,\quad a_m\ge|\langle a\rangle|,\quad
 O\ge\|a-a_c\|_\infty,\quad
 L_1\ge\|D_\theta a\|_\infty,\quad
 L_2\ge\|D_\theta^2a\|_\infty .
 \tag{M.2}
$$
They must hold on the complete radial interval, entire angular circle
and whole real parameter family. The constant $a_c$ is one actual
constant; it need not equal the mean.
Orthogonal projection gives $\|a-\langle a\rangle\|_2\le O$.

Let $C$ be a full upper bound for $\|[J,a]\|_{2\to2}$.
The complete periodic-kernel theorem permits
$$
 C\le O+\frac4{\sqrt\pi}\sqrt{O L_1}.
$$
It can be minimized with another independently proved full bound.
Since $D_\theta a$ has exact mean zero, the same kernel theorem also gives
$$
 \|[J,D_\theta a]\|_{2\to2}
 \le C_D:=L_1+\frac4{\sqrt\pi}\sqrt{L_1L_2}.                  \tag{M.3}
$$

## 2. The complete mean/high matrices

Write $f=m+f_\perp$. At order $s$ identify its norm with the Euclidean
norm of $(|m|,\|f_\perp\|_{s,*})$.
For $s=1/2,1,3/2,2$ respectively, multiplication by $a$ is bounded by
the operator norm of these nonnegative matrices:
$$
 T_{1/2}=
 \begin{pmatrix}
 a_m&O/2\\
 \sqrt{O L_1}&a_\infty+C/2
 \end{pmatrix},\qquad
 T_1=
 \begin{pmatrix}
 a_m&O/4\\
 L_1&a_\infty+L_1/4
 \end{pmatrix},                                             \tag{M.4}
$$
$$
 T_{3/2}=
 \begin{pmatrix}
 a_m&O/8\\
 \sqrt{L_1L_2}&a_\infty+C/2+L_1/4+C_D/8
 \end{pmatrix},\qquad
 T_2=
 \begin{pmatrix}
 a_m&O/16\\
 L_2&a_\infty+L_1/2+L_2/16
 \end{pmatrix}.                                             \tag{M.5}
$$
Every column and row is retained. In particular the lower-left entry
measures the genuine nonconstant output from a constant input.

**Mean row.** The nonmean contribution to $\langle af\rangle$ is at most
$\|a_\perp\|_{-s,*}\|f_\perp\|_{s,*}\le4^{-s}O\|f_\perp\|_{s,*}$.
This gives all four displayed upper-right factors.

**Constant-input high column.** Parseval and Cauchy--Schwarz give
$$
 \|a_\perp\|_{1/2,*}\le
       \sqrt{\|a_\perp\|_2\|Da\|_2}\le\sqrt{O L_1},
$$
$$
 \|a_\perp\|_{3/2,*}\le
       \sqrt{\|Da\|_2\|D^2a\|_2}\le\sqrt{L_1L_2}.
$$
At orders one and two the corresponding bounds are $L_1,L_2$.

**Nonmean high column at order $1/2$.**
Use $J(af_\perp)=aJf_\perp+[J,a]f_\perp$ and
$\|f_\perp\|_2\le\|Jf_\perp\|_2/2$.
The projection onto nonzero output modes is a contraction.

**Nonmean high column at order $3/2$.**
Its exact norm is $\|JDf_\perp\|_2$, and
$$
 JD(af_\perp)
 =aJDf_\perp+[J,a]Df_\perp
       +(Da)Jf_\perp+[J,Da]f_\perp .
$$
The physical gap gives
$$
 \|Df_\perp\|_2\le\tfrac12\|JDf_\perp\|_2,\quad
 \|Jf_\perp\|_2\le\tfrac14\|JDf_\perp\|_2,\quad
 \|f_\perp\|_2\le\tfrac18\|JDf_\perp\|_2 .
$$
Substitution proves the lower-right entry of $T_{3/2}$.
For orders one and two, the usual product formulas and the gap four
give the remaining entries directly.

Let $N_s=\|T_s\|_{\mathbb R^2\to\mathbb R^2}$.
These are complete multiplication bounds in (M.1). They do not rely
on finite Fourier support.

## 3. Additional complete interpolation bounds

The weights in (M.1) form an exact positive Hilbert scale, including
the eigenvalue one on the mean. Complex interpolation of the same
multiplication operator therefore gives
$$
 M_{1/2}\le \min\{N_{1/2},\,a_\infty+C,\,
                           \sqrt{a_\infty N_1}\},
$$
$$
 M_{3/2}\le \min\{N_{3/2},\,\sqrt{N_1N_2},\,
                           (a_\infty N_2^3)^{1/4}\}.        \tag{M.6}
$$
The helper evaluates all these full bounds and selects their minimum.
Any previous complete Wiener bound may independently participate in
the same minimum. It is not legitimate to minimize bounds that refer
to different Sobolev norms without the conversion in the next section.

## 4. Bessel/Casimir convention: the factor is small, but not one

For the physical Bessel convention
$$
 \|f\|_{s,B}^2=\sum_k(1+(4k)^2)^s|f_k|^2,
$$
the exact comparison for $s\ge0$ is
$$
 \|f\|_{s,*}\le\|f\|_{s,B}
       \le\kappa_s\|f\|_{s,*},\qquad
 \kappa_s=(17/16)^{s/2}.                                    \tag{M.7}
$$
The ratio is one on the mean, and its largest nonzero value occurs at
$|4k|=4$. Consequently a multiplier bound $M_{s,*}$ from (M.1)
gives the **Bessel-safe** bound
$$
 M_{s,B}\le\kappa_s M_{s,*}.                                 \tag{M.8}
$$
There is only one conversion factor in this implication: the output
uses the upper inequality in (M.7), while the input uses the lower one.
No factor is silently replaced by one.

The helper outputs both conventions in separately named fields.
In particular,
$$
 \kappa_{1/2}<127/125=1.016,\qquad
 \kappa_{3/2}<1047/1000=1.047 .
$$
The corresponding exact integer comparisons were actually executed in V8:
~~~text
16*127^4 = 4162314256 > 17*125^4 = 4150390625
16^3*1047^4 = 4922057407205376 > 17^3*1000^4 = 4913000000000000
~~~
The factors themselves are evaluated with directed Arb arithmetic by the
unrun native helper. The two integer checks certify only the displayed
universal rational upper bounds.

## 5. Actual nine-field consumer and preserved scope

The v2 entry uses the same complete closed-angle $C^2$ kernel evaluations
as the preceding kernel consumer. For $\alpha$ it bounds the mean by
the full finite zero coefficient plus the complete saved error.
For $v$ it uses its exact angular oddness from R105, so its mean is
exactly zero. Both statements concern the same actual uniformly
symmetric parameter family, not an accidentally symmetric center array.

It first checks that the original source-product-space declaration
contains the physical max-weight convention (M.1).
It then takes the same-norm minima for
$M_{1/2}(\alpha)$, $M_{3/2}(\alpha)$ and $M_{3/2}(v)$.
The new complete source gain is obtained from the unchanged actual
energy-source wiring
$$
 \begin{pmatrix}
 0&\sqrt{\lambda_+}M_{1/2}(\alpha)&0\\
 0&\sqrt{\gamma_+}M_{3/2}(\alpha)&0\\
 \sqrt{\alpha_+}&\sqrt{\alpha_+}M_{3/2}(v)&\sqrt{\alpha_+}
 \end{pmatrix}.
$$
The resulting norm is minimized with the old complete source gain.
All actual Fourier tail, parameter, radial and angular-gap fees remain.

The companion output explicitly records the old bounds, the selected
same-norm bounds, and the separate Bessel-safe bounds.
No missing strong source Gram or physical/canonical frame is supplied
by this refinement. The source norm, signed principal energy,
two-way ordered comparison and strict-negative domain are unchanged.

Once the completed original field and energy outputs have actually been
restored or rerun:
~~~sh
python scripts/fourfold_phase_strict_core_kernel_tame_energy_v2.py \
  --energy-reports notes/strict_core_energy_gate.json \
  --method signed --bits 256 \
  --out notes/strict_core_kernel_multiplier_tame.json
~~~
The new helper and v2 consumer have not run. In particular, neither the
old source gain near $912$ nor the old commutator near $4509$ is replaced
here by a claimed new actual value.
