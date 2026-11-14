# R133 supplement: actual full-family negative-one root Cauchy and seam-source audit

2026-11-14, phase_inverse. **Actually executed in the public repository.
All thirteen mathematical gates passed.** This activates the complete
$H^{-1}$ root-to-negative Cauchy estimate, including its true
$H^{-2/3}$ source window and affine seam columns, for the real explicit
family $|\delta|\le10^{-8}$ on the original negative root interval.

The proof is
[the negative-one Cauchy and seam theorem](R133-supplement-full-family-negative-one-root-Cauchy-and-seam-sources.md).
The full original moving two-row system and its independent even mean
are retained. There is no finite-frequency restriction on the unknown
state or source.

## 1. Actual execution and immutable identity

The public execution is
[run 43613506152, attempt 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43613506152).
Its actual mathematical child returned zero in
$0.21443437599999982$ seconds, after checking eleven fixed input files.
Both complete older computations were reused without rerunning them.

| Item | Actual identity |
|---|---|
| Workflow event | 681d53f9212634d02b368d46ab542114b67b5381 |
| Scientific checkout | bd26144de9d95099725264586586f7b956644d0b |
| Mathematical source SHA256 | c8b1eef6c5aa3ecadac83ce9ca8351aa0d2e39aac59e25b7f10f84e8d2b645b2 |
| CI driver SHA256 | 0e9228a1609ea80ed652841907a68c9fbc63cfced8549c7088f60f5fd96f9d3c |
| Input manifest SHA256 | 7e955e222cbec6985a5c154213ec94f36786ae95e5036325cf35dbdb39fdc41c |
| Native SHA256 | 7c91e9745b997ccadd1b987b5765e5bd51006261872cd58ff52b8ccd416240b0 |
| Native bytes | 4428 |

The full actual process, all thirteen gates, every directed Arb ball,
both checkout identities and the actual command are preserved in
[the original process](../notes/current_negative_one_root_cauchy_ci/run-43613506152-1/consumers/process.json).
The unchanged original native is
[the complete negative-one certificate](../notes/current_negative_one_root_cauchy_ci/run-43613506152-1/consumers/current-negative-one-root-cauchy.json.gz).
The scientific input manifest is
[the eleven-file closure](../notes/2026-11-14-R133-current-negative-one-root-cauchy-CI-inputs.json).
The process SHA256 is 4e5fee926a13334224efd854d527de7390cf273d7840eafbe4f92735066d6486.

The two original native inputs remain the exact root germ
397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864
and the complete moving scalarization budget
10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f.
The proof file used by the execution has SHA256
ea57b008f6ee88ccdfa1cf3cbcaf2b167a21b62be444e4285d93a91534d4ba6d.

## 2. Actually paid growth and reconstruction fees

The following decimals are outward bounds on the original Arb output.
They are summaries of the full saved balls.

| Complete contribution | Strict upper bound |
|---|---:|
| Local diagonal terms and first angular derivatives | 35.357145975481 |
| Local cross terms and first angular derivatives | 13.060392227752 |
| Complete local contribution | 48.417538203232 |
| Drift, including the $4/3$ logarithmic lag fee | 10.424000882355 |
| Ordered original primitive term | 30.545434991456 |
| Independent even mean-rank term | 11.716463866152 |
| Total growth | 101.103437943193 |
| $4W\exp(112R)$ | 4.005123341343 |
| $(41/10)\|I\|_{H^{-1}\to L^2}$ | 4.226183266259 |

Thus all three proposed rational gates actually hold:
$$
 L_{\rm total}<112,\qquad
 4W e^{112R}<41/10,\qquad
 (41/10)\frac{\sqrt{17}}4<17/4,
 \qquad R=\frac9{10^6}.                                  \tag{A.1}
$$
The exact physical Fourier convention is frequency $4j$ and
$\Lambda_j=\sqrt{1+16j^2}$. The equality
$\|I\|_{H^{-1}\to L^2}=\sqrt{17}/4$ uses the first nonzero physical
frequency, while $I$ annihilates only its own zero mode.

The original hypotheses were also checked: the whole real family
stays in the same original root piece; $(q^2)_\rho>59$; the complete
characteristic coefficient is below $63/50$; and all full-family
angular coefficients through the required derivatives satisfy the
declared envelopes. Degree 96 of the explicit direction and degree
192 of the quadratic coefficients were paid. These degrees do not
truncate the propagated state.

## 3. Activated full-frequency map and genuine affine jumps

Let $h=(h_1,h_2)$ solve the exact moving system, with ordinary source
$g$, in the direction $\rho=r_*-r$ from the root towards the negative
side. Put
$$
 \mathcal B=
 \bigl(\|h_1(0)\|_{H^{-2/3}}^2+
       \|h_2(0)\|_{H^{-1}}^2\bigr)^{1/2}
 +\frac3{1000}\,
   \|g\|_{L^2_\rho(H^{-2/3}\times H^{-2/3})}
 +\sum_a
 \bigl(\|j_{1,a}\|_{H^{-2/3}}^2+
       \|j_{2,a}\|_{H^{-1}}^2\bigr)^{1/2}.               \tag{A.2}
$$
The last sum contains every prescribed affine jump on an actual
ordered interior interface. It is zero only when there are no such
jumps. The complete theorem now gives
$$
 \sup_{0\le\rho\le9/10^6}
       \|h(\rho)\|_{H^{-1}\times H^{-1}}
 \le\frac{41}{10}\mathcal B,                             \tag{A.3}
$$
$$
 \sup_{0\le\rho\le9/10^6}
       \|Ih(\rho)\|_{L^2\times L^2}
 \le\frac{17}{4}\mathcal B.                              \tag{A.4}
$$
All circle norms are normalized; the even mean is present in the
state and the source. The sharper anisotropic ordinary-source norm
$L^2_\rho(H^{-2/3}\times H^{-1})$ may replace the isotropic norm
in (A.2), by the same actual multiplier estimate.

For a seam at $\rho_a$, the first sum in (A.2) can be sharpened to
the actual regular-weight norm $\|W(\rho_a)j_a\|$, with
$W=\Lambda^{-1}\operatorname{diag}(\theta/w,\theta)$ from the proof.
A formal order assigned to a trial seam is not a bound for either
of these norms; its true reconstructed two-row jump must be inserted.

The estimate propagates actual full-frequency errors before applying
the original primitive. It does not presume that a propagated column
keeps its initial Fourier support. Every later wave gauge, multiplier,
composition or trace normalizer still needs its declared bounded map.

## 4. Scope that remains separate

This execution pays precisely the original real negative interval of
length $9\cdot10^{-6}$, the real parameter disk and the displayed
Sobolev windows. It does not extend that interval, prove a complex
energy inequality, or change the positive Green source contract.
Positive-side ordinary sources still use their previously paid
$H^{1/3}$ window.

The native explicitly records that a milliscale domain, a numerical
strong-return cutoff, an additional root reflection conclusion and
nonlinear existence are not outputs of this computation. The actual
larger piecewise domain, next Airy amplitudes and their volume and
seam residuals are separate consumers.
