# R133 supplement: a true radial Airy partition and complete central power-series bounds

2026-11-14, phase_inverse.

**Proved refinement of an existing full-frequency operator estimate.**
This note keeps the actual Airy columns, all output modes, the old mean,
the true circle maps, and their previously paid composition costs.
It changes only the scalar bounds on the Airy profiles in
[A.12--A.18](R133-supplement-analytic-Airy-columns-and-complete-exponential-Fourier-bound.md).
No trial, radial cutoff, coefficient table, or amplitude solve changes.

The statement applies to real radial points and every real member of
the already declared explicit parameter interval. It does not assert
positivity of a radial reference for complex parameter values.
Numerical consequences require a new public consumer.

## 1. Retain the actual radial reference

Use the closed characteristic formula in
[the piecewise root construction](R133-supplement-piecewise-real-root-fold-and-closed-forced-Airy-transport.md).
For each real $\rho$ and allowed real parameter, let

$$
 a(\rho)=\eta(\rho)\sqrt{k(\rho)},\qquad
 \overline A(\rho)=\frac32\int_0^1s^{1/2}a(s\rho)\,ds .
 \tag{R.1}
$$

Here $a$ is a positive radial scalar. On the entire radial window
suppose $0<a_-\le a\le a_+$, and on the same old-angle strip used
for the complete leading columns suppose the true characteristic
Jacobian obeys $|X_\phi-1|\le j<1$.
The exact characteristic expression for $A$ then gives

$$
 a_-\le\overline A(\rho)\le a_+,\qquad
 |A(\rho,\phi)-\overline A(\rho)|\le a_+j .
 \tag{R.2}
$$

The second bound holds on the full declared complex angle strip.
It uses the actual characteristic at every integration point:
subtract 1 from its Jacobian, retain $a(s\rho)$, and use
$\frac32\int_0^1s^{1/2}\,ds=1$.
It does not replace the radial function $a$ by a constant.

Set

$$
 \epsilon=\frac{a_+j}{a_-}<1,\qquad g=1-\epsilon .
 \tag{R.3}
$$

At each real radial point, (R.2) implies

$$
 |A-\overline A|\le\epsilon\,\overline A,\qquad
 \operatorname{Re}A\ge g\,\overline A,\qquad
 |A|\le(1+\epsilon)\overline A.
 \tag{R.4}
$$

These are relative angular bounds at one and the same radial point.
A broad interval enclosing the radial variation of $a$ does not enter
the ratio in the last two inequalities.

The actual previously proved bounds
$\operatorname{Re}A\ge A_->0$ and $|A|\le A_+$ remain available.
They are still used for the powers of the actual $A$ in the high
profiles below. In particular, the partition parameter $a_-$ is
not substituted without its factor $g$ for a lower bound on $|A|$.

## 2. Partition by that same real scalar

Fix $x=|\rho|>0$, an input cutoff $J$, and $n=4|j_{\rm in}|\ge4J$.
Write

$$
 \overline t=\frac23 n x^{3/2}\overline A(\rho),\qquad
 t=\frac23 n x^{3/2}A(\rho,\phi),\qquad
 z=n^{2/3}x A^{2/3}.
 \tag{R.5}
$$

Use the branch fixed by the positive real value. Declare the high
input indices by $\overline t\ge1$ and the central indices by
$\overline t<1$.

This selector depends on $\rho$ and the real parameter, but not on
$\phi$. Both sets are orthogonal input projections in every Fourier
Sobolev space. The decomposition is used only at the radial point
to estimate the already fixed, entire Airy trial. Neither its
derivative nor a radial indicator is inserted into the equation.
It introduces no artificial seam, source, or parameter change.

For high columns, $\operatorname{Re}t\ge g$ by (R.4).
The horizontal Volterra bounds in A.7--A.11 therefore give

$$
 c_-=\frac{\exp(5/(36g))}{2\sqrt\pi},\qquad
 c_+=\frac{\exp(5/(72g))}{2\sqrt\pi},\qquad
 d_\pm=\left(1+\frac{11}{36g}\right)c_\pm .
 \tag{R.6}
$$

The coefficient $11/36$ is $1/6+5/36$: it includes both the
derivative of the Airy power prefactor and the normalized
Volterra derivative. Each negative ray branch consequently has

$$
 n^{1/6}|\operatorname{Ai}\text{ branch}|
 \le c_-x^{-1/4}A_-^{-1/6},\qquad
 n^{-1/6}|\operatorname{Ai}'\text{ branch}|
 \le d_-x^{1/4}A_+^{1/6}.
 \tag{R.7}
$$

For the positive decaying Airy column use $c_+,d_+$.
Its factor $e^{-t}$ remains inside the analytic symbol and has
modulus at most 1. The only positive-side real composition is $X$.

For a central column, (R.4)--(R.5) instead give

$$
 |z|\le Z_\epsilon
   :=\left(\frac32(1+\epsilon)\right)^{2/3},\qquad
 n^{1/6}\le x^{-1/4}\left(\frac{3}{2a_-}\right)^{1/6}.
 \tag{R.8}
$$

This is the improvement over using a ratio of the global radial
upper and lower envelopes in the central disk.

## 3. Complete entire bounds without an exponential overestimate

Let $F_0,F_1$ be the entire solutions of $F''(z)=zF(z)$ with
initial data $(1,0)$ and $(0,1)$ respectively. Explicitly,

$$
 F_r(z)=\sum_{k=0}^{\infty} c_{3k+r}^{(r)}z^{3k+r},
 \quad r=0,1,\qquad c_r^{(r)}=1,\qquad
 c_{m+3}^{(r)}=\frac{c_m^{(r)}}{(m+3)(m+2)} .
 \tag{R.9}
$$

All omitted powers have zero coefficient and all displayed
coefficients are positive. The recurrence follows by direct
substitution in the differential equation. It also proves
absolute convergence on every bounded complex disk.

The already paid joint initial bound
$|\operatorname{Ai}(0)|+|\operatorname{Ai}'(0)|<1$ gives, for $|z|\le Z$,

$$
 |\operatorname{Ai}(\pm z)|\le C_A(Z):=\max(F_0(Z),F_1(Z)),
 \qquad
 |\operatorname{Ai}'(\pm z)|\le C_D(Z):=
                         \max(F_0'(Z),F_1'(Z)).
 \tag{R.10}
$$

Indeed
$\operatorname{Ai}(z)=\operatorname{Ai}(0)F_0(z)
+\operatorname{Ai}'(0)F_1(z)$ by the entire initial-value
uniqueness theorem. Positivity of the series coefficients
bounds each function and derivative by its value at $Z$.
The same argument applies at $-z$, including the absolute
value of the derivative. The use of the joint initial bound
justifies the maximum instead of a sum.

For clarity, every infinite series in (R.10) has a direct finite
consumer. Choose an integer $K\ge1$, put $m=3K+r$, and let

$$
 u_K=c_m^{(r)}Z^m,\qquad v_K=m c_m^{(r)}Z^{m-1},\qquad
 q_F=\frac{Z^3}{(m+3)(m+2)},\qquad
 q_D=\frac{Z^3}{m(m+2)}.
 \tag{R.11}
$$

If $q_F,q_D<1$, monotonicity of the denominators gives

$$
 \begin{split}
 F_r(Z)&\le \sum_{k=0}^{K-1}c_{3k+r}^{(r)}Z^{3k+r}
                         +\frac{u_K}{1-q_F},\\
 F_r'(Z)&\le \sum_{k=0}^{K-1}(3k+r)c_{3k+r}^{(r)}Z^{3k+r-1}
                         +\frac{v_K}{1-q_D}.
 \end{split} \tag{R.12}
$$

The derivative summand at $k=r=0$ is exactly zero and is
handled as such, without evaluating a negative power.
The value ratio follows immediately from (R.9).
For derivative terms the factor $(m+3)/m$ cancels the first
denominator factor, leaving $q_D$.
All later ratios decrease. Thus (R.12) retains the entire tail;
there is no sampling of an Airy function and no truncated
series asserted to be exact.

Any finite directed upper bounds obtained from (R.12) may
replace $C_A,C_D$ below. The looser already proved bound
$\exp(Z+Z^2/2)$ is also valid, but is not required.

## 4. New scalar profiles, unchanged complete operators

For the same componentwise bounds $(W_a,W_b)$ on the same
complex strip, set $N=4J$, $0<x\le R$, and define

$$
 \begin{split}
 B_c={}&C_A(Z_\epsilon)
            \left(\frac{3}{2a_-}\right)^{1/6}W_a
       +C_D(Z_\epsilon)R^{1/4}N^{-1/6}W_b,\\
 B_-={}&c_-A_-^{-1/6}W_a+
                         d_-R^{1/2}A_+^{1/6}W_b,\\
 B_+={}&c_+A_-^{-1/6}W_a+
                         d_+R^{1/2}A_+^{1/6}W_b .
 \end{split} \tag{R.13}
$$

The complete Fourier factor $\mathcal D_{J,\tau}$, the actual
real composition constants, and
$\tau=(1-j)\sigma$ are exactly those already paid in A.1--A.6.
The full old-angle Airy column operators satisfy

$$
 \|\mathsf S_\rho(W)\|_{H^{-4/3}\to H^{-5/3}}
 \le x^{-1/4} C_\Phi\mathcal D_{J,\tau}
                    \sqrt{B_c^2+4B_-^2}
 \quad\text{on the negative side},
 \tag{R.14}
$$

$$
 \|\mathsf S_\rho(W)\|_{H^{-4/3}\to H^{-5/3}}
 \le x^{-1/4} C_X\mathcal D_{J,\tau}
                    \max(B_c,B_+)
 \quad\text{on the positive side}.
 \tag{R.15}
$$

The proof is the same full-input argument as A.17--A.18:
orthogonal central/high inputs on the negative side and
the sum of the two genuine branches; on the positive side
all columns have the single real phase $X$, so a uniform
symbol bound is the maximum. No Fourier output, including
the old mean, is removed.

The symbols in each group remain analytic on the same
whole old-angle strip, because their selector is independent
of the angle. Both input signs are retained. The pointwise
bound is uniform over the real parameter interval; it does
not require choosing one common threshold for all parameters.

## 5. Exact reuse and limits of the conclusion

The direct angular matrix jets in
[the existing matrix theorem](R133-supplement-direct-angular-matrix-jets-for-analytic-Airy-sources.md)
and all ordered old inverse products remain unchanged.
In particular, the complete tensors for $H^{-1}$, $H_D$,
$w_0$, $\partial_\rho w_0$, the composition factors and
the entire Fourier-tail bounds may be reused verbatim.
Only the three two-component scalar profiles in (R.13)
are newly evaluated.

The exact derivative and old-mean identities still use those
same tensors and the same projected operators in the same
order. The current successful 1328 coefficient/moment rows
and 1328 directed rows need no recomputation. A new consumer
can copy the six completed amplitude tensor cases, replace
only their profile field, and integrate the resulting source
norms on the same exact common radial cover.

The two sides of the true root interval remain distinct.
Each one-sided root-band integral of $|\rho|^{-1/2}$ keeps
its separately proved bound. Positive collar/body subdivision,
independent even mean, and all supplied source and interface
columns are retained.

This refinement is not yet a numerical smallness assertion.
A public directed consumer must check $\epsilon<1$, both
series tail ratios, the exact old tensor/native identities,
and every complete integral. It does not pay the local
$L_0w_1$ residual, the full positive low/mean inverse, a
complete numerical strong-return norm, a cutoff-97 inverse,
or the true PDE branch.
