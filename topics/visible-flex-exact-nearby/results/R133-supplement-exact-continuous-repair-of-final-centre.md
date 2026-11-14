# R133 supplement: exact continuous repair of the final centre

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved by exact rational computation.** The complete final `ac1d5b98…`
polynomial centre has a distinct, explicitly defined continuous repair.
All 6,143 interfaces and all 65 real Fourier coefficients have been
processed exactly. The maximum full pair correction is less than
$3.861\,10^{-18}$ in $A^0$ and $5.635\,10^{-16}$ in $A^3$.
The genuine even mean is included. The entire waist state is unchanged.

The original centre, its scientific arrays, all successful computations
and all failed attempts remain unchanged. The derived centre is not
assigned the original candidate SHA. Its canonical definition SHA256 is

```
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
```

This result supplies the exact correction and the identities needed to
transfer subsequent bounds. It does not silently relabel any earlier
native as a computation on the repaired centre.

## 1. Complete exact definition

Let $0=r_0<\cdots<r_{6144}=25/8$ be the exact dyadic nodes of the
restored final candidate, and let $y_j(r)$ be its exact 65-component
radial cubic on $[r_j,r_{j+1}]$. Its first 32 components are the real
sine coefficients of $U$, and its last 33 are the real cosine
coefficients of $V$, including $V_0$.

The original physical moving state is

$$
 Q_j=(u_j,v_j)=(\alpha U_j,s_{\eta,\nu}+\alpha V_j),\qquad
 \alpha=\frac{6890507429876859}{9007199254740992}.
 \tag{V.1}
$$

The true radial $s=C_{\rm ref}^{-1}$ is continuous and has no candidate
PPoly value jump. Define all physical coefficient jumps and offsets by

$$
 J_j=\alpha\{y_j(r_j)-y_{j-1}(r_j)\},\qquad
 e_0=0,\qquad e_j=e_{j-1}-J_j\quad(1\le j\le6143).
 \tag{V.2}
$$

The new centre is

$$
 \boxed{\quad\bar Q_j(r,\phi)=Q_j(r,\phi)+e_j(\phi).\quad}
 \tag{V.3}
$$

Each $e_j$ is constant in $r$ on its original piece and has the same
complete 32-mode parity support, including its true even mean. All
operations in (V.2) are on exact binary rational numbers. No endpoint
is evaluated in floating arithmetic in this construction.

At every interface,

$$
 \alpha y_{j-1}(r_j)+e_{j-1}
       =\alpha y_j(r_j)+e_j.
 \tag{V.4}
$$

The source checks (V.4) component by component in exact arithmetic.
It follows that $\bar Q$ and all its angular derivatives are continuous
across every candidate interface. Its radial derivative can still jump;
that is neither removed nor asserted otherwise. On each open original
piece,

$$ \bar Q_r=Q_r. \tag{V.5} $$

The offsets do not depend on $\eta$ or $\nu$. The same construction
therefore applies to every original affine parameter and every compact
parameter for which the original true reference $s_{\eta,\nu}$ is
defined. The metric, $s$, the scalar target, and their parameter
derivatives have not been changed.

## 2. Exact all-mode and mean bounds

Use the physical inhomogeneous Wiener norms

$$
 \|f\|_{A^k}=\sum_{n\in4\mathbb Z}(1+|n|)^k|f_n|,
 \qquad \|(f,g)\|_{A^k}=\|f\|_{A^k}+\|g\|_{A^k}.
 \tag{V.6}
$$

For a real sine or nonmean cosine amplitude, the two complex Fourier
coefficients have half that amplitude. Thus summing the absolute real
amplitudes with the weights in (V.6) gives precisely the complete
complex-Fourier norm; the mean has weight one.

The full computation finds 399,295 nonzero exact component jumps and
proves the following outward decimal bounds:

| Maximum over all 6,144 pieces | Strict bound |
| --- | ---: |
| $\|e_j\|_{A^0}$ | $3.861\,10^{-18}$ |
| $\|e_j\|_{A^1}$ | $1.970\,10^{-17}$ |
| $\|e_j\|_{A^2}$ | $1.028\,10^{-16}$ |
| $\|e_j\|_{A^3}$ | $5.635\,10^{-16}$ |
| $\|e_j\|_{A^4}$ | $3.429\,10^{-15}$ |
| $\|e_j\|_{A^5}$ | $2.520\,10^{-14}$ |
| $\|e_j\|_{A^6}$ | $2.564\,10^{-13}$ |
| $|\langle e_{v,j}\rangle|$ | $5.842\,10^{-21}$ |

These are actual cumulative corrections, not merely the larger sum of
the absolute original jumps. The native also preserves every exact
maximum, its maximizing piece, and the complete sums of original jump
norms for $k=0,\ldots,6$.

For the stronger joint norm with coefficientwise radial suprema,

$$
 \sum_n e^{\sigma|n|}\sup_j |(e_j)_n|,
 \tag{V.7}
$$

the complete pair bounds are respectively

$$
 \begin{array}{c|cccc}
 \sigma&1/2048&1/1024&1/64&1/32\\ \hline
 \text{bound}&4.249\,10^{-18}&4.258\,10^{-18}
                  &4.526\,10^{-18}&4.832\,10^{-18}.
 \end{array}
 \tag{V.8}
$$

The sum in (V.7) is after the individual coefficient suprema. It has not
been interchanged with the supremum of an $A^0$ norm.

At $R=25/8$ the full pair change is less than $3.260\,10^{-18}$.
The actual mean change is the exact rational
`exact_right_mean_offset` in the native; numerically it is approximately
$-8.0438336551\,10^{-22}$. All 65 right offsets are retained as rational
strings, so no consumer needs to reconstruct a vector from these
displayed rounded numbers. The complete offset on the common root
piece 2549 is also explicitly recorded.

## 3. What continuity fixes, and what it does not assert

Where the true $v$ and $m$ remain separated from zero, form the curvature
angle and the physical curvature pair from the new centre itself:

$$
 \bar\theta=\phi+\frac1{\bar m}I(\bar v-\bar m),\qquad
 \bar B=(\bar u/\bar v)\circ\bar\phi,\qquad
 \bar C=(1/\bar v)\circ\bar\phi.
 \tag{V.9}
$$

The previously certified real denominator margins are many orders
larger than (V.6); their use still requires the stated explicit
subtraction of $\|e_v\|_{A^0}$ and $|\langle e_v\rangle|$.
Because the full state and every angular derivative agree exactly at
each interface, both the angle and its full linearized state map agree
there. A globally continuous moving direction therefore gives a
globally continuous physical direction in the same physical angle.
There is no residual bare angle-relabeling jump to call a small
$L^2$ operator.

This observation does not estimate a nontrivial composition minus the
identity. It removes that particular homogeneous interface mismatch by
the exact equality (V.4). Nonlinear residuals and ordinary source terms
remain. On the repaired centre they are genuine piecewise bounded
functions, without a value-jump Dirac measure.

## 4. Complete residual and Jacobi transfer identities

Write the complete moving equation as $Q_r=F_{\eta,\nu}(Q)$. Its radial
principal coefficient, drift, local polynomial and both mean/nonlocal
terms are those already defined in the complete moving theorem. On
each original open piece, the exact residual relation is

$$
 R(\bar Q)=R(Q)-[F(Q+e)-F(Q)].
 \tag{V.10}
$$

Thus a complete residual consumer uses the old complete ordinary
residual plus the full finite polynomial difference in (V.10), not the
old residual alone. The new distributional residual contains no
candidate value jumps; (V.4) accounts for their removal exactly.

For any full unknown variation $h$, the exact linearization difference
is

$$
 \bar D h-Dh=-[DF(Q+e)-DF(Q)]h.
 \tag{V.11}
$$

Although $e$ is finite, $h$ is unrestricted. In particular, the change
$\gamma\langle e_v\rangle J(K)\partial_\phi h$ remains a principal
term. It is not called a bounded $L^2$ perturbation, and no high return
arithmetic condition is inferred from the small decimal size of $e$.
The installed root neighbourhood theorem may consume the actual
$A^3$ correction in its own true radial reference; its principal mean
is to be reset exactly as required there.

Since the offsets are independent of $\nu$, the complete parameter
column satisfies

$$
 \partial_\nu F_{\eta,\nu}(Q+e)-\partial_\nu F_{\eta,\nu}(Q)
   =\int_0^1 D_Q\partial_\nu F_{\eta,\nu}(Q+t e)[e],dt.
 \tag{V.12}
$$

Every true mean column in this expression remains present. The source
sign is the already fixed convention $D h=+F_\nu\,\delta\nu+f$.
An old finite response or adjoint remains a perfectly usable proposal;
its residual and boundary consumer must use (V.11)--(V.12) or evaluate
the derived centre explicitly. It is not relabelled as an exact solution
of the new operator.

## 5. Waist, right endpoint and complete mean identities

The first-piece offset is exactly zero. Hence the whole waist state,
its physical angle, the physical fourth-amplitude row and all its
previously computed 96 columns are unchanged exactly. The intrinsic
waist target and its parameter dependence are also unchanged.

At any fixed endpoint write $E=e_v$ and $e_0=\langle E\rangle$. Before
inverting the physical angle, the exact angle change is

$$
 \bar\theta-\theta
 =I\left(\frac{mE-e_0v}{m(m+e_0)}\right).
 \tag{V.13}
$$

This keeps the entire mean correction and gives, for example,

$$
 \|\bar\theta-\theta\|_{A^0}
 \le\frac{\|E_{\ne0}\|_{A^0}
       +|e_0|\|v-m\|_{A^0}/|m|}{4(|m|-|e_0|)}.
 \tag{V.14}
$$

The exact complete physical mean identities are

$$
 \langle C\rangle_\theta=1/m,\qquad
 \langle\bar C-C\rangle_{\rm respective\ physical\ angles}
       =-\frac{e_0}{m(m+e_0)},\qquad
 \langle B\rangle_\theta=\langle\bar B\rangle_{\bar\theta}=0.
 \tag{V.15}
$$

The last equality is the actual sine/even reflection, not a deletion
of the even curvature mean or of the exterior height charges.
For pointwise reciprocal differences before angle composition,

$$
 \bar C-C=-\frac{E}{v(v+E)},\qquad
 \bar B-B=\frac{e_u}{v+E}-\frac{uE}{v(v+E)}.
 \tag{V.16}
$$

The fixed-physical-angle comparison also includes (V.13) through the
complete angular derivatives. The full nonlinear regular graph,
its mean, the independent outer-height data and its derivative are to
be evaluated at this changed right input or bounded uniformly on their
already proved ball. The finite array in the native makes these fees
explicitly computable; (V.16) alone is not substituted for the
fixed-angle comparison.

## 6. Actual computation, identities and reproduction

The exact source is
`scripts/fourfold_codazzi_final_continuous_value_repair.py`.
The complete report is
`notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz`.
Its public helper `iter_repair(saved, alpha)` yields the exact physical
offset and original jump on every piece, using `Fraction` throughout.

The run checked every original shard and all scientific array shapes,
processed all 6,143 interfaces, passed the six stated structural/size
gates, and exited normally after about 169 seconds. In addition to the
report's exact coefficient maxima, the complete ordered offset sequence
has its own SHA256. The canonical derived definition binds this
sequence digest, the original candidate index, exact amplitude, complete
radial and Fourier support, and the precise rule (V.2).

No large repaired cubic array needs to be committed or rounded. It is
reconstructed exactly from the original reproducible shards and (V.2).
The original index and the derived-definition SHA are distinct and
must both be recorded by any downstream consumer.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python3 scripts/fourfold_codazzi_final_continuous_value_repair.py \
  --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --out /a-new-path/exact-continuous-value-repair.json.gz
```

The root/strict/cap numerical-transfer consumers, full negative return,
continuous finite-head inverse, complete parameter Schur and nonlinear
closure remain separate. The correction is explicitly small; none of
these obligations is discharged solely by that adjective.
