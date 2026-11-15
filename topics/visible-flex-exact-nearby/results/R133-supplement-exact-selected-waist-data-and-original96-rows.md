# R133 supplement: exact selected waist data in the original 96 rows

2026-11-15. This is a new scalar consumer of the saved background and the already proved continuous response direction. It does not recompute a response, a Green operator, a repair sequence, or a PDE residual.

## WA1. The actual left source and its units

Use the same continuous physical family as NF.21 and SR.20:
$$
Q_\delta=\bar Q+\delta Z,\qquad
b_{0,\delta}=-UQ_\delta(0),\qquad U=(I_{96},0).
\tag{WA.1}
$$
The circle has period $\pi/2$ and normalized measure. Its real orthonormal odd basis is $\sqrt2\sin(4j\phi)$, $1\le j\le96$. Consequently a physical sine amplitude is divided by $\sqrt2$ in the original 96 Euclidean waist rows. There is no additional radial weight.

The original background index has SHA256
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413.
Its normalized state order is 32 odd sine amplitudes followed by the even mean and 32 cosine amplitudes. Let its first 32 initial values be $a_j$, extended by exact zeros to $j=96$. Only this background is multiplied by
$$
\alpha=\frac{6890507429876859}{9007199254740992}.
\tag{WA.2}
$$

The full response index has SHA256
ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6.
Its first 96 initial values are the physical, unnormalized sine amplitudes $z_j$. They are not multiplied by $\alpha$. The remaining 97 entries, including the genuine even mean, remain part of the complete input identity. The waist operator reads the prescribed odd block; it does not impose a zero even mean.

## WA2. Exact initial traces and the two continuous repairs

The base shard writer stores an initial vector separately from its cubic coefficients. Its file format alone does not prove these two objects agree. The new runner therefore restores only the original background index and first shard and checks, in all 65 entries,
$$
\operatorname{bits}(\mathrm{initial\_state})
 =\operatorname{bits}(\mathrm{piece\_coefficients}[3,0,:]).
\tag{WA.3}
$$
The first radial node must be exactly zero, the local powers descending, and the complete first-shard shape, byte count and SHA must match the immutable index. No other background shard is needed for this endpoint statement.

For $Z$, the already successful producer
scripts/fourfold_codazzi_phase_explicit_response_direction.py
(SHA256 9c08e253d2b4cdd951392a31aafc190b2341793a162c46aaadd914780894bf5c)
checked the full 193-state initial trace against the first cubic coefficient and all complete value-interface repairs. Its published proof is
[the explicit continuous direction](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md), particularly Q.1--3. Its original seven gates are reused as proved facts; the producer is not called again.

Both exact continuous repairs start with zero offset. Thus they leave the two first traces unchanged. The direction definition is
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04;
the background definition is
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47.

The response index is read from the complete reconstructible document in
notes/2026-11-14-R133-all-regular-head-complete-reconstruction.json.
Re-serializing that document with the original shard writer's exact JSON convention must reproduce its full original index SHA. This is identity checking only; no response shard, repair, QR, inverse or finite solve is reconstructed or rerun.

## WA3. Exact signed polynomial and a uniform interval bound

Treat every original binary64 coefficient as its exact rational value. Then
$$
(b_{0,\delta})_j=-\frac{\alpha a_j+\delta z_j}{\sqrt2},
\qquad 1\le j\le96.
\tag{WA.4}
$$
Define the three exact rationals
$$
A=\frac{\alpha^2}{2}\sum_{j=1}^{96}a_j^2,\qquad
B=\alpha\sum_{j=1}^{96}a_jz_j,\qquad
D=\frac12\sum_{j=1}^{96}z_j^2 .
\tag{WA.5}
$$
The complete signed relation is
$$
\|b_{0,\delta}\|_{\ell^2_{96}}^2=A+B\delta+D\delta^2.
\tag{WA.6}
$$
All 96 terms are retained. The cross coefficient $B$ is signed, and its exact rational value is saved. There is no sampled parameter or cancellation based on rounded upper bounds.

Since $D\ge0$, the quadratic is convex. Hence, for every exact $d\ge0$,
$$
\max_{|\delta|\le d}\|b_{0,\delta}\|^2
 =\max\{A+Bd+Dd^2,A-Bd+Dd^2\}
 =A+d|B|+d^2D.
\tag{WA.7}
$$
This is an equality for the uniform maximum, including $d=0$ and the degenerate cases $B=0$ or $D=0$. The new consumer reports exact $A,B,D$, both exact endpoint squared norms, the exact uniform maximum, and an outward Arb square-root bound for
$$
d\in\{0,10^{-10},10^{-8},10^{-5}\}.
\tag{WA.8}
$$
The exact check $B^2\le4AD$ is a consistency gate, not a substitute for the input identities. The output does not assume that any original floating coefficient is exactly zero.

## WA4. Scope of the new conclusion

WA.6 is an algebraic identity for the explicitly given finite family at the waist. WA.7 at a larger $d$ does not enlarge any previously proved metric, phase, cap or PDE domain. Within the appropriate domain it supplies the independent $\|b_{0,\delta}\|$ input in NF.26 or SR.20--21.

The new calculation does not evaluate NF.23's $\ell_0$, SR.9's fifth column, an unknown cut trace, a high-frequency inverse, or a nonlinear existence statement. The genuine even mean, high waist conditions, right affine data, full matching and the fixed selected parameter remain independent. A nonzero bound cannot be replaced by an exact zero condition.

Only the new small scalar conclusion, exact input identities and execution metadata are published. The two old input files are restored temporarily at their unchanged historical paths; no coefficient arrays or new native data are persisted to Git, Releases or artifacts.
