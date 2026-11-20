# Complete coarse three-jet physical space

Date: 2026-11-20 UTC. Status: algebraic construction and a recovered, **not yet executed** v2 implementation. The 63-dimensional predecessor was actually run; its numerical result is recorded separately in `2026-11-20-physical-fit-six-step-result.md`. No numerical value from that run is attributed to v2.

## Why all three coarse jets are needed

The five position hats of v1 have zero first and second derivatives at their coarse centers. Consequently their 55 angular copies cannot change the meridional velocity at those centers. The accepted v1 output still has sampled Gram error about 0.5864, with its worst point near the coarse center 1.3580749679. This is a limitation of the chosen correction space, not a proof that the full closed problem is infeasible.

The v2 space supplies independent position, velocity, and acceleration corrections at every one of the same five coarse nodes. All original high angular modes, all original radial nodes, the analytic lift, the fixed scalar metric, and every original residual row are retained. The complete free problem still has 1,332,245 coordinates; the 173-dimensional space is a warm-improvement subspace or an additional right-preconditioner block.

## Exact radial cardinal functions

Let successive coarse breakpoints be \(\sigma_0=0,\ldots,\sigma_6=S\), with five interior breakpoints taken from the existing fine mesh. Let \(u=(s-\sigma_i)/h\) on a coarse interval of width \(h\). The polynomial three-jets below are evaluated at the fine nodes and interpreted by the original shared quintic interpolation, so they define the same physical polynomial on every nested fine interval.

For an interior coarse node, the position cardinal is the existing smoothstep hat: its left branch is \(S_5(u)=10u^3-15u^4+6u^5\), and its right branch is \(1-S_5(u)\). It has the coarse jet \((1,0,0)\).

The velocity cardinal uses
\[
h(-4u^3+7u^4-3u^5)
\]
on its left interval and
\[
h(u-6u^3+8u^4-3u^5)
\]
on its right interval. Both yield jet \((0,1,0)\) at the middle node and zero three-jet at the two support endpoints.

The acceleration cardinal uses
\[
\tfrac12h^2(u^3-2u^4+u^5)
\]
on its left interval and
\[
\tfrac12h^2(u^2-3u^3+3u^4-u^5)
\]
on its right interval. Both yield jet \((0,0,1)\) at the middle node and zero three-jet at the support endpoints.

Physical first and second derivatives include division by \(h\) and \(h^2\), respectively. Thus all 15 radial functions are \(C^2\), are supported on two adjacent coarse intervals, and preserve the core and terminal three-jets. At a shared coarse node their three jets have exactly the required cardinal values.

## Angular channels, core freedom, and cap height

Use the same eleven rotating-frame angular fields as v1:
\[
R_0,\quad Z_0,\quad R_m,T_m,Z_m\quad(m=1,2,3),
\]
where the physical frequencies are \(2m\). Fifteen radial functions times eleven channels give 165 directions.

Retain the seven horizontal core-acceleration directions from v1, with radial function
\[
c(s)=(s/S)^2(1-s/S)^3.
\]
They use \(R_0,R_m,T_m\), \(m=1,2,3\), and vary only the allowed horizontal part of the core acceleration; the core curve and initial velocity stay fixed. The vertical core acceleration is constrained and is not included.

Retain the one smooth cap-height direction
\[
\delta H=1,\qquad \delta q_Z=B(s)-\chi(s),\qquad B(s)=S_5(s/S).
\]
The actual stored nodal three-jets and original lift are evaluated, including the original midpoint interpolation. The algorithm does not replace the stored field by an unrecorded smooth surrogate. This gives \(165+7+1=173\) directions.

All fixed support coefficients, including the first three, remain unchanged in this subspace, so \(\rho(\phi)\) and \(\Theta(\phi)\) are fixed during a subspace solve. Later full-space iterations may still vary every allowed core coefficient.

## Separated exact normal matrix

Let \(V=F_s\), \(d=F_\phi\), and \(a=a(s)\). The three physical residuals are
\[
r_0=V\cdot V-1,\quad
r_1=\frac{V\cdot d}{a\rho},\quad
r_2=\frac{d\cdot d}{(a\rho)^2}-1.
\]
The objective is the original full angular sum of \(r_0^2+2r_1^2+r_2^2\). Quarter-orbit weights are 2 at the two endpoint angles and 4 at interior angles, exactly as in R653; they reproduce the original full-circle objective.

Write the physical correction as
\[
\delta F=\sum_{b,c}z_{bc}Y_b(s)h_c(\phi),\quad
\delta V=\sum_{b,c}z_{bc}U_b(s)h_c(\phi),\quad
\delta d=\sum_{b,c}z_{bc}Y_b(s)\partial_\phi h_c(\phi).
\]
Here \(\partial_\phi h_c\) includes differentiation of the rotating frame. The height direction is included using its actual physical stage values.

With \(w\) the square root of the angular orbit weight, define the angular derivative arrays
\[
A_0=2w(V\cdot h),\quad A_1=\frac{w(d\cdot h)}{a\rho},\quad
B_1=\frac{w(V\cdot\partial_\phi h)}{a\rho},\quad
B_2=\frac{2w(d\cdot\partial_\phi h)}{(a\rho)^2}.
\]
The derivative column for a radial-angular pair \((b,c)\), with the middle residual given its Frobenius factor \(\sqrt2\), is
\[
\big(U_b A_{0,c},\ \sqrt2(U_bA_{1,c}+Y_bB_{1,c}),\
Y_bB_{2,c}\big).
\]
Therefore the eleven-by-eleven angular kernels are
\[
K_{uu}=A_0^\top A_0+2A_1^\top A_1,\quad
K_{uy}=2A_1^\top B_1,\quad
K_{yy}=2B_1^\top B_1+B_2^\top B_2.
\]
For two selected pairs \((b,c),(e,f)\), their normal-matrix entry at a stage is exactly
\[
U_bU_e(K_{uu})_{cf}
+U_bY_e(K_{uy})_{cf}
+Y_bU_e(K_{uy}^{\top})_{cf}
+Y_bY_e(K_{yy})_{cf}.
\]
The gradient uses
\[
g_u=A_0^\top(wr_0)+2A_1^\top(wr_1),\qquad
g_y=2B_1^\top(wr_1)+B_2^\top(wr_2).
\]
The entry is \(U_b(g_u)_c+Y_b(g_y)_c\). Summing over all 1,845 original stages gives precisely the same Gauss--Newton system as forming 173 full weighted Jacobian columns. This factorization saves work and memory without deleting equations or approximating their weights.

## Full-space right-preconditioner interface

`make_space(base_source, operator, low_modes=3)` constructs the space. The methods `free_direction(z)` and `transpose_free(v)` implement a linear map \(B\) and its Euclidean transpose \(B^\top\) in the original packed coordinate ordering:
\[
(c_{K:},\ A_{0,XY},\ \text{all interior three-jets},\ H).
\]
The core-support entries of \(Bz\) are zero. The core horizontal acceleration entries and all interior jets are copied from the literal physical basis, and the final packed coordinate is the height coefficient. The transpose takes exactly these contractions and adds the height cotangent.

A complete solve can use the augmented right map \([D,B]\), for an existing full-space scaling \(D\). This retains all original free directions. Such a preconditioner still requires a correctly transposed action and the original nonlinear objective to accept a trial. This note records the interface, not a convergence result.

## Recovered code and first-run command

Publication path:
`scripts/resume_20261120_physical_subspace_v2.py`.

The initial v2 draft was written locally, but its process never started because the execution environment disconnected. The recovered complete source adapts its dependency argument to `--base-source`, retaining `--basis-source` as an alias; the default is the sibling `resume_20261120_physical_subspace.py`. Its first actual run must be recorded as a new execution.

From a checkout, with work outside the tracked tree:

```sh
python "$topic/scripts/resume_20261120_physical_subspace_v2.py" \
  --bundle "$work/physical-fit-six-step.npz" \
  --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
  --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
  --batch-source "$batch_source" \
  --out "$work/physical-threejet-six-step.json"
```

The defaults are six steps, at most eight trial step lengths per iteration, initial scaled damping \(10^{-3}\), 2,048 full-circle angles, three low angular correction modes, and a 600-second compute budget. The output bundle is `physical-threejet-six-step.npz` beside the report. These raw local outputs are for immediate continuation only; the repository stores source, formulas, a short result summary after a real run, and their provenance.

The selected parent is the actual 63-dimensional output with recorded SHA256 `af89a4414fb0cee35d75dba5530e9b45b62abd248ddf7509cca92c2a9696a505` and native sampled SSE 6430.555483124957. The unavailable parent bundle must be regenerated from its complete recipe before the new run; its old digest alone is not a restorable artifact. A regenerated bundle may have a different archive digest and must record its own exact bytes and numerical state.

## Limits

This is a construction of useful physical search directions. It gives no continuous metric certificate, no all-phase embedding or reach certificate, and no lower bound for held amplitude. The whole closed candidate still fails the \(10^{-6}\) metric requirement. Any new candidate must first be evaluated using the actual complete operator, then receive the separate continuous and geometric checks required by the topic README. No infeasibility conclusion follows from failure of this finite subspace.
