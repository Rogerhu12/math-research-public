# Actual first six steps of the all-mode polar/banded solver

Date: 2026-11-20 UTC. Status: numerical evidence for the original finite full-closed Gram objective. This is not a continuous or geometric acceptance.

The regenerated field bundle with SHA256 `c79e88cb48f94196d8ec8cfa18e7362fa849d4bd1aa4afee71a53e3445331792` was the actual input. It is the preceding 12-angular-mode, 11-coarse-node three-jet improvement. The full model remains $M=160$, $J=923$, with all $11,335,680$ original full-circle rows represented by $2,839,455$ exact multiplicity-weighted quarter rows.

## Reproducible source and invocation

Executed source:
`scripts/resume_20261120_polar_banded.py`, SHA256
`852f62b806f87e799e75f3c0a0665d217ffc0ab6e826b920c8658225599358a2`.

Original dense operator SHA256:
`e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d`.

Batched/quarter operator SHA256:
`02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a`.

The local process was actually launched, completed naturally with exit 0, and took 14.350971607000247 seconds. Session identifier: `87869`, in the resumed 24b2ab87 workspace. This is a local execution record, not an invented Actions run identifier.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_polar_banded.py" \
  --bundle "$work/root/physical-threejet-m12-r11-six-step.npz" \
  --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
  --batch-source "$batch_source" \
  --out "$work/geometry_path/polar-allm160-six-step.json" \
  --steps 6 --seconds 600
```

The defaults used are `--angles 2048 --stage-block 64 --regularization 1e-6 --backtracks 12`. The auxiliary regularizer is $\eta\sum_i h_i^{-1}\int|\delta F_s|^2ds$. The actual acceptance is the original Gram SSE, with a positive sampled determinant. The original-gradient fallback is enabled but was never used: every accepted step was the polar/global direction with step length 1.

All 157 free core support coefficients were held at their actual input values. Every one of the remaining 1,332,088 original free coordinates participates through the full mode space; no radial prefix, angular tail, interior jet, horizontal core acceleration, or cap height was frozen.

## Actual numerical results

| Accepted steps | Original Gram SSE | Sampled maximum Gram norm | Sampled minimum determinant |
|---:|---:|---:|---:|
| 0 | 36.118988424628064 | 0.05283234362354036 | 0.9504474815374816 |
| 1 | 22.18078637243211 | 0.03802444492310632 | 0.9537745714317262 |
| 2 | 21.49742236668846 | 0.036874819350560056 | 0.956491236944288 |
| 3 | 21.018626147134906 | 0.03703320417067629 | 0.9592790084124069 |
| 4 | 20.639060384424344 | 0.0371917387043573 | 0.9615142523297617 |
| 5 | 20.31651978472869 | 0.037310668193934846 | 0.9632730429633922 |
| 6 | 20.03110694953174 | 0.03740144312842687 | 0.9646834324289277 |

The SSE decreases in every step. The maximum Gram error reaches its smallest recorded value at step 2 and then rises slightly while the SSE continues to decrease. No uniform-error monotonicity is claimed.

$H$ changes from $1.8408123843527382$ to $1.8410781600648434$. The final sampled worst point is native stage 1679, angle index 332:
$$
s=1.2276382622098958,\qquad \phi=1.0185632431560658.
$$
Initial and final `pack(require_affine=True)` both return exact equality with zero per-jet projection differences.

The 322 radial factors have lower bandwidth 5. The vertical-mean/height Schur complement is $0.006116831576946424$. The first normalized linear-system residual is $1.0713228327942683\times10^{-13}$; subsequent residuals are about $2$–$3\times10^{-15}$. Local two-frame orthogonality errors are at most $2.220446049250313\times10^{-15}$.

The first packed correction has Euclidean coordinate norm $116901.08777967373$. This is a norm of differently scaled raw polynomial jets, not a curvature value or geometric certificate. Neither its size nor a decreasing sampled SSE determines the actual curvature between stages.

Output bundle SHA256:
`7a8275a953e6ff5399604adf4160f452072ea05ee6f215f92cfd8f1f260b794f`.

The report and raw output remain computational working files; no reproducible array or raw Actions artifact is retained in the repository.

## Necessary independent implementation check

Before the full run, `scripts/resume_20261120_check_polar_banded.py` actually ran on a small 208-coordinate model and exited 0. Its SHA256 is
`08f54ff2bca4712cb1a8a23d213901427b6de568797214387dfa2355890da52b`.

The check uses endpoint-Vandermonde interpolation and eight-point Gauss quadrature independently of the solver's five-point derivative rows. It checks the actual physical energy of a right-factor output, a transpose inner product, and the direct inverse against $BB^\top$:

- Independent physical energy relative error: $2.3708774624795016\times10^{-13}$.
- Right-factor transpose relative error: $9.56437849956085\times10^{-18}$.
- Direct inverse versus $BB^\top$ relative error: $3.969280434198401\times10^{-14}$.
- Small-model maximum scaled linear residual: $1.60035261725337\times10^{-11}$.

These are binary64 implementation checks, not interval certificates.

## Scope and next mathematical obligation

The sampled error is still over $0.037$, far above $10^{-6}$. The original node/midpoint Gram operator has an exact vertical-mean underintegration kernel, described in the formula note and the separate kernel analysis. The continuous derivative regularizer makes the auxiliary linear solve positive definite; it does not convert the original sampled residual into a continuous bound, and it does not bound second derivatives.

The actual output was then read by the root's complete native-stage six-jet curvature reader. It has sampled maximum absolute principal curvature **95055.26061254322**, at stage 996, $s=0.995$, $\phi=1.1873011298234863$. The reader evaluated all 946,485 quarter-orbit points (3,778,560 full-orbit points); the minimum sampled area was 0.09375628136909153. This is a severe geometric failure. The output is **not** selected as a feasible geometric parent.

The diagnostic report SHA256 is `10c291374f6ba258ed9ca8901fd215fd144de77f37721e87c300c4d8754db880`. The actually executed reader source SHA256 is `af0511e7d92eeffa44f99704c705ce8ee5961fb3e9b0757c9ce1f2872126d72a` and the six-jet helper SHA256 is `16cd8680d3d63e66a7ff335feadaa275a3efc96729028aaafa7fd9668a09181f`. That reader invocation preceded the later source extension adding the complete reflected-body diameter lower bound; its result is not retroactively attributed to the newer source.

In particular, the complete doubled surface and its caps determine $D$. No full-surface held ratio, all-phase reach, embedding, or reflection-sensitive noncongruence follows from the sampled Gram descent. The retained earlier 63-dimensional parent has much lower sampled curvature; subsequent work returns to that parent and uses actual curvature constraints or current-field second-derivative regularization, together with additional radial metric checks. The scalar and underlying field definition remain fixed.
