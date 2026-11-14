# R133 supplement: actual piecewise root window of radius 1/50 and all original seams

2026-11-14, phase_inverse. **Actually executed:** the true real radial
root window now has radius $1/50$, with analytic old-angle
characteristics, a nondegenerate complete principal fold and the
full original-circle inverse. All 1300 closed rows and 1079 actual
candidate seams are retained. The complete complex explicit family
$|\delta|\le10^{-8}$ and all 193 direction components are included.

This activates
[the piecewise fold and forced transport theorem](R133-supplement-piecewise-real-root-fold-and-closed-forced-Airy-transport.md).
The numerical result concerns this explicit family. It does not yet
bound the next Airy forcing, the complete reconstructed seam errors
or a numerical strong-return remainder.

## 1. Actual execution, prefix recovery and provenance

[Public run 43616813816, attempt 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43616813816)
returned zero after $36.75047011999999$ seconds of actual mathematics.
It verified 204 fixed input files. The workflow event and the
scientific checkout were both
7250f9f45f1287f1f62891f62173a8309a9ecc55.

The original complete result is
dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212
(SHA256), 5923431 bytes. Its unchanged compressed native is retained
in the actual run artifact
visible-exact-piecewise-real-root-fold-resume-v2-43616813816-1,
as consumers/piecewise-real-root-fold-resumed-v2.json.gz.
It exceeds the repository's single-file publication threshold;
the original bytes were preserved without artificial splitting.

The committed
[actual process and selected full budget](../notes/piecewise_real_root_fold_resume_v2_ci/run-43616813816-1/consumers/process.json)
is 32670 bytes, SHA256 c30eb4c5e1efebd3663528418389ececf1ba8f4450f8e667496026915e2dfb64.
It preserves the actual command, child result, all global gates,
every radius outcome, selected directed balls and complete seam sums.

| Scientific input | SHA256 |
|---|---|
| New mathematical source | 840d7ae96c023f0f1055516cfefe62f22a8f46a3f8a0ea2974553b32760eb112 |
| CI driver | 0f688d095b2e6a62d8ba50e678d59bacb89dc25d721964bedd1b37184188a530 |
| 204-file manifest | 93346b9eb5d968cfdb160c665bd6f524b108d629e81487905b67708ab6c61166 |
| Original failed native reused | feab71e2ba588e79f97f2beb821b5db29425bf7c69dceb010719ec0df6dd49cd |

The first actual run 43615829270 stopped at the first positive
cache row: reading only the coarse displayed ball discarded the
positive information in its separately saved directed endpoints.
The resumed consumer uses the original provider's exact
lower-endpoint/upper-endpoint reconstruction. No original native,
coefficient, target, threshold or proof was changed.

The earlier native contains **766 actually completed rows**, rather
than the last periodic progress count 705. All 766 rows were reused
unchanged and matched by exact interval and original candidate piece;
only 534 new rows were evaluated. Its full failed
[native](../notes/piecewise_real_root_fold_ci/run-43615829270-1/consumers/piecewise-real-root-fold.json.gz)
and [process](../notes/piecewise_real_root_fold_ci/run-43615829270-1/consumers/process.json)
remain. No one of the 169 original scalar germs, their 626 accepted
cells, the 4650 positive rows, candidate solve or response solve was
rerun.

## 2. Every proposed radius actually passed

The fifteen global gates passed. For each of the six radii, all
seven characteristic, fold and full-inverse gates also passed.

| Exact radius | Complete closed rows | Actual original seams |
|---|---:|---:|
| $1/1000$ | 142 | 47 |
| $1/500$ | 270 | 146 |
| $1/200$ | 618 | 460 |
| $1/100$ | 884 | 693 |
| $3/200$ | 1085 | 876 |
| $1/50$ | 1300 | 1079 |

The largest selected exact fixed cover is
$$
 \left[
 \frac{1091984371497}{5000000000000},
 \frac{2583968743003}{10000000000000}
 \right].
$$
It contains the entire radius-$1/50$ interval about the true root
in its original certified root interval. The compact metric
perturbation is identically zero throughout this cover.

The old coefficient width is $1/16$. The genuine characteristics
are defined at old angular width $1/32$. The following outward
summaries are strict bounds on the saved directed quantities:
$$
 D_0<0.119438552683,\quad D_1<0.562079353471,\quad
 D_2<2.982935146146,
$$
$$
 O_-<0.020355402174,\quad O_+<0.010692080034,\quad
 M_R<0.022744173228<1/32.
$$
The entire true optical integrals, the drift and the uncertain root
margin were paid before granting the angle domain.

For the actual divided phase and principal fold,
$$
 A_->4.096024948378,\quad A_+<22.435013909711,\quad
 |S_{\pm,\phi}-1|<0.011305011150,
$$
$$
 |A_\phi|<0.830611382139,\quad |T_\phi|<0.006921747465,
 \quad |T|<0.159091712889,
$$
$$
 |X_\phi^2+TT_\phi^2|>0.977254552246,\quad
 |\operatorname{Jac}(T,X)|>1.506157398137,\quad
 |\mu|>2.321309328005 .
$$
The average angular displacement satisfies
$|X-\phi|<0.002413339676$.

For real data, the real fold image contains every real $X$ and
$$
                  |T|<0.05120020790294.                \tag{A.1}
$$
This is a real piecewise coordinate domain. There is no joint
holomorphic extension across the images of the original cubic
seams, and no fixed-$T$ reinterpretation of the old primitive.

## 3. Complete original-circle inverse and leading amplitudes

The full inverse $J$ retains all unknown Fourier modes, its
projection and primitive, and the independent even mean equation
remains separate. It is not a finite matrix inverse.

| Width | Neumann factor | $J:L^2\to L^2$ | $\partial_\phi J:L^2\to L^2$ |
|---|---:|---:|---:|
| $1/32$ | $<0.161685709592$ | $<0.238363996387$ | $<0.953455985547$ |
| $1/64$ | $<0.145668790714$ | $<0.233923770665$ | $<0.935695082660$ |

The corresponding complete analytic Hilbert and Wiener maps
use those same declared widths. The saved one-gain Sobolev bounds
include, at width $1/32$,
$$
 \|J\|_{H^{-2/3}\to H^{1/3}}<0.982799934447,\qquad
 \|J\|_{H^{-5/3}\to H^{-2/3}}<1.978736488763,
$$
and, at width $1/64$, bounds $0.964492414795$ and
$1.875976500971$, respectively. These windows use the paid
integer commutator recursion, its adjoint and interpolation.

The complete leading factors also have actual larger-window bounds:
$$
 |G|<2.297082816200,\quad |G|^{-1}<2.311350240315,
$$
$$
 |V_{\sigma,0}|<2.349313484609,\quad
 |V_{\sigma,0}|^{-1}<2.364509664471,\quad
 |b_0/T^2|<12.267642438345 .
$$
The saved forced Fa/Fb root-to-point factors bound the integral
for $V_\sigma/V_{\sigma,0}$ in (M.15). They still require the
leading factor and the actual two-branch reconstruction before
becoming amplitude bounds. They are not complete source or
parametrix error constants.

## 4. Nonzero seams remain quantitatively present

The exact continuous repair makes the background and direction
values continuous. Their open-piece radial derivative corrections
are exactly zero. The new consumer evaluated all original
one-sided polynomial derivatives through order three, retaining
all 65 background and 193 direction components and the true even
means. Each exact full component jump has its own recorded digest.

For illustration, the sums of the complete pair norms with no
additional angular derivative obey the following strict bounds:

| Radial derivative jump | Sum at width $1/32$ | Sum at width $1/64$ |
|---|---:|---:|
| First | $<1.510059658463\cdot10^{-13}$ | $<1.399674175368\cdot10^{-13}$ |
| Second | $<0.032014277056$ | $<0.029540193794$ |
| Third | $<400540.762440$ | $<370803.254387$ |

The complete sums with one and two additional angular derivatives
are also in the actual process. The second and third derivative
jumps have not been erased or inferred to vanish from the much
smaller first derivative jump.

These are coefficient seam budgets. The finite Airy trial has
its own genuine reconstructed state jumps given by (M.16)--(M.17).
Their norms must be evaluated from its actual forced amplitudes,
then inserted in the appropriate true propagation estimate. This
result does not extend the previously paid negative Cauchy radial
interval merely by constructing a larger coordinate domain.

The numerical next-amplitude forcing, full volume and affine seam
residuals, uniform strong-return norm and cutoff-97 inverse remain
separate gates. All original finite head, mean and regular exterior
columns are retained.
