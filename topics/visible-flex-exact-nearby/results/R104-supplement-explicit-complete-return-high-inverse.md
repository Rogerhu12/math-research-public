# R104 supplement: an explicit high inverse of the original complete return

**Proved for the original complete feedback at the actual R101 parameter
\(p_\infty\), with its original complete exterior tail.**
The full nonconstant phase and the complete strong remainder are those
of
[the actual two-cone normal form](R46-supplement-actual-two-cone-density-normal-form-and-base-Rstar.md).
The resulting explicit cutoff is

$$
\boxed{\quad N=2^{2108},\qquad
\kappa_N<0.014238672808<1/64,\qquad
\|A_H^{-1}:PH^{s+1}\to PH^s\|<15.941269,\quad
-4/3\le s\le0 .\quad}                                   \tag{C.1}
$$

This is the entire infinite high block, including both root-circle
copies. No high frequency is truncated. The integer \(N\) has 635
decimal digits and is stored in full in the native report.

The corresponding exact finite head has complex dimension
\(4N=2^{2110}\). Its full Schur matrix has **not** been assembled or
inverted. Thus (C.1) is an explicit, extremely large high cutoff and a
genuine high inverse; it is not a numerically tractable finite-head
certificate or a full feedback inverse.
The continued work on actual high density transport seeks to reduce
this cutoff and close that remaining head problem.

## 1. The same complete operator and the full high projection

The complete actual normalized feedback acts on two root-circle copies
and two independent regular slots. Its model is

$$
A_{\rm model}
=
\left[
  \bigl(I+U_\omega(I+iT_{b_+}D^{-1})\bigr)
  \oplus 2_{\rm first\ mean}
  \oplus\bigl(I+U_\omega(I+iT_{b_-}D^{-1})\bigr)
\right]
\oplus I_{\rm second\ root}\oplus2I_{\rm regular}.
                                                               \tag{C.2}
$$

Here the two nonzero first-root cones have already undergone their
correct positive rotation and negative **linear** reflection.
Both use positive integer frequency \(j\), the same \(+\omega\), and
the same mean \(\beta\), with

$$
b_+(x)=b_{\rm geom}(x),\qquad b_-(x)=b_{\rm geom}(-x).
$$

All true couplings among cones, both root means, the second root copy
and the independent regular slots remain in

$$
A=A_{\rm model}+R.
$$

The complete mean ledger
notes/2026-11-13-R46-two-cone-complete-mean-ledger.md
retains the original mean diagonal and all mean excursions in this
same \(R\). No additional replacement of its mean is made here.

The already paid full unweighted strong bound is

$$
\|R:H^s\to H^{s+4/3}\|
\le R_*<3.026346\,10^{208},
\qquad -4/3\le s\le0 .                                   \tag{C.3}
$$

This uses the full two-window theorem and interpolation. It is not
a finite matrix estimate or a columnwise asymptotic.
No positive \(s\) or fixed positive angular weight is inferred.

Let \(P\) retain \(|n|\ge N\) on **both** root-circle copies and be zero
on both regular slots. Put \(Q=I-P\), \(A_H=PAP\).
The high diagonal model has two first-root scalar factors and two
second-root identity cones. For the latter,

$$
\|I^{-1}D^{-1}\|_{PH^s\to PH^s}\le1/N\le110/7.
$$

Thus the same scalar small-divisor constant below pays the complete
augmented high model, including its second root copy.

## 2. Complete arithmetic and both actual phase functions

The actual complete phase satisfies

$$
|b_\pm(z)|\le M,\qquad
M<26409.294892,\qquad |\Im z|\le1/4096=:s_b.
                                                               \tag{C.4}
$$

The accurate actual \(\beta\) interval is retained as the two exact
fractions from R102/R104; the consumer does not replace it by a fitted
mean. The same exact quadratic rotation has all continued-fraction
partial quotients at most eight, including its complete golden tail.
Hence the cohomological bound is

$$
|1-e^{-il\omega}|>{2\over5|l|},\qquad l\ne0.               \tag{C.5}
$$

The R104 polynomial diagonal certificate, now also actually rerun by
its unchanged Node BigInt CLI, gives

$$
\left|1+e^{ij\omega}(1+i\beta/j)\right|>{7\over110j},
\qquad j\ge1.                                           \tag{C.6}
$$

The new replay is
notes/2026-11-13-R104-polynomial-diagonal-native-replay.json.
It verifies the same complete R102 arithmetic input and actual
\(\beta\) interval. The earlier report and its earlier execution
description remain unchanged.

For either actual \(b_\pm\), solve the complete cohomological equation

$$
a_l=-{b_l\over1-e^{-il\omega}}\quad(l\ne0),\quad a_0=0,
\qquad a-a(\cdot-\omega)=\beta-b.
$$

From (C.4)--(C.5),

$$
|b_l|\le M e^{-s_b|l|},\qquad
|a_l|\le {5\over2}|l|M e^{-s_b|l|}.
                                                               \tag{C.7}
$$

Both entire Fourier series and their entire infinite tails are retained.

## 3. Exact complete multiplier sums at the selected cutoff

For every required \(s\in[-4/3,0]\),

$$
(1+|l|/N)^{|s|}\le(1+|l|/N)^2 .
$$

Let \(z=e^{-s_b}\), and define the exact complete geometric moments

$$
S_0={z\over1-z},\qquad S_1={z\over(1-z)^2},\qquad
S_2={z(1+z)\over(1-z)^3},
$$

$$
S_3={z(1+4z+z^2)\over(1-z)^4},\qquad
S_4={z(1+11z+11z^2+z^3)\over(1-z)^5}.                    \tag{C.8}
$$

These are \(\sum_{l\ge1}l^k e^{-s_bl}\), not truncated estimates.
With \(B_\beta\) the actual interval bound for \(|\beta|\), use

$$
A_0(N)=5M(S_1+2S_2/N+S_3/N^2),\quad
A_1(N)=5M(S_2+2S_3/N+S_4/N^2),
$$

$$
B_0(N)=B_\beta+2M(S_0+2S_1/N+S_2/N^2),\quad
B_1(N)=2M(S_1+2S_2/N+S_3/N^2).                           \tag{C.9}
$$

These pay the complete high-to-high multiplier sums in the
[head-preserving gauge theorem](R104-supplement-head-preserving-cutoff-dependent-gauge.md),
simultaneously for the whole already paid negative-to-base window.

On each first-root scalar cone let

$$
C_N=PT_aPD^{-1}P,\qquad T_N=I+iC_N.
$$

On the second root copy and the regular slots \(T_N=I\).
The complete gauge is the identity on the entire finite head.
In particular its use does not remove or approximate a single low row.

Set

$$
q_0={A_0(N)\over N},\qquad
q_1={A_0(N)+A_1(N)/N\over N},
$$

$$
\mathcal E_N=
{A_0(N)[B_0(N)+B_1(N)/N]
 +B_\beta[A_0(N)+A_1(N)/N]\over N}.
$$

The complete strong error gives the explicit Neumann coefficient

$$
\kappa_N={1\over c(1-q_1)}
 \left\{\mathcal E_N+
 {R_*(1+q_0)\over(1+N^2)^{1/6}}\right\},
\qquad c={7\over110}.                                    \tag{C.10}
$$

The denominator \((1+N^2)^{1/6}\) is exactly
\(\langle N\rangle^{1/3}\).
The actual full strong remainder, including all its cone and
second-root couplings, appears in the second term.

Every quantity in (C.9)--(C.10) is evaluated with directed Arb
arithmetic. The producer brackets the first dyadic cutoff with
\(\kappa_N<1/64\) under these complete positive majorants.
They are decreasing with \(N\) whenever \(q_1<1\):
all their numerators are positive polynomials in \(N^{-1}\), while
the two positive denominators increase.
The actual adjacent results are

$$
\kappa_{2^{2107}}>0.0179396035929>1/64,\qquad
\kappa_{2^{2108}}<0.0142386728077<1/64.                    \tag{C.11}
$$

This claims the first passing dyadic for these particular majorants,
not the optimal true cutoff.

## 4. The actual complete high inverse

The exact full compressed identity is

$$
A_HT_H=T_H\mathcal D_H+E_H+R_HT_H .
$$

The identity block on the second root copy adds no gauge error.
Use the exact factorization

$$
\mathcal D_H^{-1}T_H^{-1}
=(\mathcal D_H^{-1}D^{-1})
 (DT_H^{-1}D^{-1})D .
$$

Equations (C.5)--(C.10), including the genuine full strong estimate
(C.3), therefore give

$$
\|\mathcal D_H^{-1}T_H^{-1}(E_H+R_HT_H)\|_{H^s\to H^s}
\le\kappa_N<1 .
$$

The complete Neumann series converges on the infinite high space.
For every \(g_H\in PH^{s+1}\) there is exactly one \(u_H\in PH^s\)
satisfying \(A_Hu_H=g_H\), and

$$
\|u_H\|_{H^s}
\le {1+q_0\over c(1-q_1)(1-\kappa_N)}
 \|g_H\|_{H^{s+1}}
<15.941269\,\|g_H\|_{H^{s+1}}.                            \tag{C.12}
$$

This is a one-derivative-loss statement. It does not assert a bounded
inverse from \(PH^s\) to itself.
For uniqueness among all \(PH^s\) solutions, the homogeneous equation
and the order-two/strong errors imply the factorized equation
\((I+K_H)T_H^{-1}u_H=0\), where \(\|K_H\|<1\).
Thus no further high kernel is left by the construction.

The true scope is the original \(p_\infty\), where the R101 rotation
is exactly the R102 quadratic target. The complete geometric constants
were paid on a larger parameter box, but the exact irrational rotation
is not silently transferred to all other parameters in that box.

## 5. The complete finite head, all source columns, and their remaining equation

The low space contains

- the first root mean and its \(2(N-1)\) nonzero low modes;
- the second root mean and its \(2(N-1)\) nonzero low modes;
- both independent regular slots.

Its exact complex dimension is therefore

$$
(2N-1)+(2N-1)+2=4N=2^{2110}.                              \tag{C.13}
$$

The head-preserving gauge theorem keeps all finite-input and
finite-output rows, even when they have infinitely many nonzero entries.
The complete low operator is still exactly

$$
S_L=A_{LL}-A_{LH}A_H^{-1}A_{HL}.                          \tag{C.14}
$$

At base order each finite low input has an analytic model column and a
full \(H^{4/3}\) remainder column. Thus its high component is in the
\(H^1\) input space required by (C.12). All terms of (C.14) are
well-defined; no finite truncation of a low column's high tail is used.

If and only if this complete finite matrix has the appropriate inverse,
the full reconstruction is

$$
u_L=S_L^{-1}(g_L-A_{LH}A_H^{-1}g_H),\qquad
u_H=A_H^{-1}(g_H-A_{HL}u_L).                              \tag{C.15}
$$

Neither the numerical size nor the invertibility of \(S_L\) is asserted
here. In particular the six-dimensional retained model R121 is not
substituted for this entire head.

The previously proved full physical source columns map their exact
original source spaces into the final normalized \(L^2\) data \(g\).
For the already paid index \(s=-1\), (C.12) consequently gives the
genuine high particular estimate

$$
\|A_H^{-1}Pg\|_{H^{-1}}
\le15.941269\,\|g\|_{L^2}.                                \tag{C.16}
$$

The new consumer multiplies every original ordinary, weak contact and
independent regular source column by its directed value of (C.12).
Those original source norms and labels are unchanged.
Equation (C.16) is the high particular for a prescribed zero head;
the full nonzero-head drive \(A_{HL}u_L\) and the low source equation
in (C.15) remain.
It is not an \(L^2\) amplitude bound or a \(C^2\) physical realization.
The additional \(H^1\) source window needed to use \(s=0\) remains a
separate obligation.

The proof does not transfer the old complete outer Robin/source
operator to the newer deep-tail candidate. That new object's
corresponding full-interface transfer is also separate.

## 6. Executed files

The unchanged original all-frequency arithmetic was actually replayed:

~~~bash
node scripts/fourfold_polynomial_diagonal_and_cutoff_exact.mjs \
  --out notes/2026-11-13-R104-polynomial-diagonal-native-replay.json
~~~

The new complete cutoff consumer is
scripts/fourfold_actual_return_explicit_high_cutoff.py:

~~~bash
python3 scripts/fourfold_actual_return_explicit_high_cutoff.py \
  --out notes/2026-11-13-R104-actual-return-explicit-high-cutoff.json
~~~

It checks the full normal-form source and inputs, the exact arithmetic
producer and all its input hashes, the same actual \(\beta\), and the
same complete quadratic target.
The native report contains the exact 635-digit integer, the adjacent
dyadic bracket, every complete Fourier moment, all gauge constants,
the full one-loss inverse bound and every \(L^2\)-source-to-high-\(H^{-1}\)
column.

No native geometry is recomputed and no finite-head inversion is claimed.

