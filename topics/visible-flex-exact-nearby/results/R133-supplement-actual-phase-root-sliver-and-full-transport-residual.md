# R133 supplement: actual phase root sliver and full transport residual

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved for the direct moving Jacobi principal rays of the same
continuous repaired final centre, with all original affine parameters.**
Let $r_b=r_{*,\rm lower}-2^{-32}$ be the endpoint of the new scalar
cache. For the exact finite proposed lift $H$ specified below, the entire
uncomputed two-ray root sliver contributes less than

$$
 \boxed{4.968975\,10^{-14}}                               \tag{T.1}
$$

to its conjugacy defect on the input strip $|\operatorname{Im}x|<1/64$.
The common angular drift cancels in a precise transport identity.
No frequency cutoff, deleted mean, or radial-root sampling is used.

More generally, every piecewise finite transported-phase proposal has
the complete a posteriori defect bound (T.12) below, including initial
errors, full PDE residuals, every radial interface jump, all Fourier
outputs, and the genuine variable-root endpoint. The PDE residuals and
terminal Fourier defect have not yet been evaluated by this result;
there is no claim here of a true conjugacy or Diophantine rotation.

## 1. Actual moving rays and the precise operator being considered

Use the same repaired centre
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`,
the exact original affine target, and the fixed final nu. In the negative
region put

$$
 q=\sqrt{-K},\qquad m=\langle v\rangle,\qquad
 d=\beta I(u^2+Kv^2),\qquad c=-\gamma m q.
                                                               \tag{T.2}
$$

The two principal vector fields of the direct moving Jacobi system are
$F_\pm=d\pm c$. Their actual flows from the waist are denoted
$X_\pm(r,x)$ and their inverse lifts by $S_\pm(r,\phi)$.
The true return is $P=X_-^{-1}(r_*)X_+(r_*)$.

This definition keeps the direct moving system's principal part. At an
approximate centre it is not an assertion that a passive pullback of
the physical Jacobi system has drift $d$ without its separately proved
residual correction. The complete residual-sensitive physical/moving
bridge remains necessary wherever those two operator realizations are
identified.

The actual whole-root interval is

$$
 r_*(\eta)\in
 \left[\frac{1191984371497}{5000000000000},
       \frac{2383968743003}{10000000000000}\right],
 \qquad
 r_b=\frac{1191984371497}{5000000000000}-2^{-32}.              \tag{T.3}
$$

The source verifies that the entire sliver from $r_b$ to the upper root
bound lies inside the same genuine intrinsic complex germ and the same
candidate cubic piece 2549. The exact cumulative repair on that piece,
including its even mean, is read from the repair native. The scalar
speed $c$ is real for real radial position and all allowed real eta.

## 2. The finite proposed lift is an exact analytic object

The earlier floating return fit supplied 24 real sine and 24 real cosine
coefficients. Here each recorded binary64 value is converted to its
exact dyadic rational and defines the finite function

$$
 H(x)=x+h(x),\qquad
 h(x)=\sum_{j=1}^{24}\big(a_j\sin4jx+b_j\cos4jx\big).
                                                               \tag{T.4}
$$

No fitted value is declared to be the true return or a true conjugacy.
Instead the complete finite polynomial (T.4) is bounded directly by Arb.
On $S_{1/32}$ the actual computation proves

$$
 \|h'\|<.018253651977,
 \qquad \frac1{32}-\|h\|>.0273781708029.                  \tag{T.5}
$$

Thus $H$ is an oriented real analytic circle lift with period $\pi/2$.
On the complex strip it is injective because the segment integral of
$H'$ has positive real part. For any $w$ with
$|\operatorname{Im}w|<1/32-\|h\|$, the map $z\mapsto w-h(z)$ maps
the closed radius-$\|h\|$ disk about $w$ into itself and has derivative
norm less than one. Its unique fixed point supplies the inverse. This
also gives $\|(H^{-1})'\|\le(1-\|h'\|)^{-1}$ there. These are
proved bounds for the exact proposed finite lift, independent of whether
its conjugacy defect will be small enough.

## 3. Exact transported phases and common-drift cancellation

Define the exact transported lifts

$$
 A_\pm(r,\phi)=H(S_\pm(r,\phi)),\qquad
 (A_\pm)_r+(d\pm c)(A_\pm)_\phi=0,
 \qquad A_\pm(0,\phi)=H(\phi).                            \tag{T.6}
$$

Their difference $D=A_--A_+$ is periodic. Subtracting the two equations
gives exactly

$$
 \boxed{D_r+dD_\phi=c\big((A_-)_\phi+(A_+)_\phi\big).}     \tag{T.7}
$$

In particular no term of size $d$ times an uncontrolled derivative of
a phase lift is charged across the tiny sliver. The common drift is
transported exactly, and only the true relative speed $2c$ remains as
a source. At the true root,

$$
 H(P(x))-H(x)=D(r_*,X_+(r_*,x)).                           \tag{T.8}
$$

This is an identity for the entire ordered two-ray composition; no
numerical inversion of a sampled ray is required to use it.

## 4. Actual complex paths and the complete root source

The previously completed full Fourier/3072-row analytic certificate,
on the outer field strip $S_{1/16}$, gives the one-leg angular
Lipschitz integral

$$ L<.049312859541.                                       \tag{T.9} $$

The scalar speed is real and creates no imaginary drift. All forward,
inverse, and intervening common-drift trajectories needed to evaluate
(T.6)--(T.8), starting with $x\in S_{1/64}$, therefore have imaginary
part at most

$$ e^{3L}/64<.018116276245<1/32.                           \tag{T.10} $$

The factor three conservatively pays a waist-to-root leg, an inverse
common-drift sliver, and an inverse principal leg. Each path remains
inside the already proved outer field strip, so this is a genuine
domain argument, not a real-axis derivative bound extended by assertion.
The same argument bounds the inverse-ray Jacobian by $e^L$ and hence
$|(A_\pm)_\phi|\le e^L(1+\|h'\|_{S_{1/32}})$ on these paths.

Let $\Delta=r_{*,\rm upper}-r_b$. The actual intrinsic root germ bounds
$|K'|\le K_1$, $|\gamma|\le\gamma_*$, and the complete repaired even
mean by $|m|\le m_*$. Since $K(r_*(\eta))=0$ and $K<0$ on the true
negative side,

$$
 q(r)\le\sqrt{K_1(r_*(\eta)-r)},\qquad
 \int_{r_b}^{r_*(\eta)}|c(r)|\,dr
 \le\frac23\gamma_*m_*\sqrt{K_1}\,\Delta^{3/2}
 <2.322547\,10^{-14}.                                    \tag{T.11}
$$

Only the real radial sliver is used. The positive part of the enclosing
root interval is not reclassified as negative for an individual eta.
The uniform upper endpoint in (T.11) merely bounds the length of each
actual negative sliver. Integration of (T.7), using (T.10), now proves
(T.1), namely twice (T.11) times $e^L(1+\|h'\|)$.

## 5. Complete finite-phase residual contract

Let $\widehat A_\pm=\phi+\widehat W_\pm$ be any periodic finite Fourier,
piecewise radial polynomial proposals on $[0,r_b]$, with one-sided
traces at every interface. Define their *complete true* residuals

$$
 R_\pm=(\widehat W_\pm)_r+
                    F_\pm\big(1+(\widehat W_\pm)_\phi\big).
$$

No projection is applied to this expression. If the field has degree
64 and the proposal has degree $N$, all output frequencies up to
$N+64$ occur in this finite product, and every model error in the
intrinsic scalar coefficients is an additional full residual term.
Let $J_{\pm,j}$ be right-minus-left jumps of $\widehat W_\pm$, and let
$E_{\pm,0}=H-(\phi+\widehat W_\pm(0))$.

The exact error $A_\pm-\widehat A_\pm$ obeys a transport equation with
source $-R_\pm$ and interface jumps $-J_{\pm,j}$. Integrating this
identity along actual characteristics uses no amplitude Gronwall
factor. Combining the two errors with (T.7)--(T.11) gives, for every
real constant $\Omega$,

$$
 \boxed{\begin{aligned}
 \|H\circ P-H-\Omega\|_{S_{1/64}}
 \le{}&\|\widehat W_-(r_b)-\widehat W_+(r_b)-\Omega\|_{S_{1/32}}\\
 &+\sum_{\sigma=\pm}\left[
    \|E_{\sigma,0}\|_{S_{1/32}}
    +\int_0^{r_b}\|R_\sigma(r)\|_{S_{1/32}}\,dr
    +\sum_j\|J_{\sigma,j}\|_{S_{1/32}}\right]\\
 &+4.968975\,10^{-14}.
 \end{aligned}}                                             \tag{T.12}
$$

The path margin (T.10) is what permits each displayed residual and
trace norm to be taken on the single fixed strip $S_{1/32}$.
The Fourier mean of $\widehat W_\sigma$ is retained in both the source
and the final difference. Any root phase, constant rotation, or lift
normalization must appear in the actual terminal constant $\Omega$;
it is not discarded as a nonzero-mode calculation.

For a finite scalar polynomial model $\widetilde F_\sigma$ one may
evaluate
$\widehat W_r+\widetilde F_\sigma(1+\widehat W_\phi)$ by exact
finite polynomial arithmetic, then add
$\|F_\sigma-\widetilde F_\sigma\|\,
 \|1+\widehat W_\phi\|$ on the same strip. This is the intended use
of the new complete scalar Taylor cache. A fitted orbit error, an
angular sample residual, or a radial collocation residual alone does
not supply any of the complete terms in (T.12).

## 6. Actual files and scope

All ten native gates passed in 1.40 seconds. The input identities,
whole parameter/root data, exact finite $H$ coefficients, every scalar
sliver bound, and all complex path margins are saved in
`notes/2026-11-14-R133-final-phase-root-sliver-and-transport-contract-native.json.gz`.
The source is
`scripts/fourfold_codazzi_final_phase_root_sliver_budget.py`.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 \
  scripts/fourfold_codazzi_final_phase_root_sliver_budget.py \
  --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --out notes/2026-11-14-R133-final-phase-root-sliver-and-transport-contract-native.json.gz
```

The prior floating fit is used only to specify one exact finite test
lift. Its sampled residual is not used in any bound above. The actual
terminal Fourier norm and full PDE residual integral are the next
computations. A phase parameter Schur additionally needs the true
continuous response and its error, and a complete high-frequency
inverse still needs its full first phase and strong remainder. These
separate obligations are unchanged by the small root-sliver constant.
