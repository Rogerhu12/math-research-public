# R133: complete cap coefficientwise bounds for the same full193 direction

2026-11-15, visible-exact-astra-0df9.

This consumer has one new task: bound the exact existing direction $Z$
on $I=[9/10,25/8]$ in the joint coefficientwise radial-supremum Wiener
norm. It reads the original physical cubic trial and already proved
continuous-repair bounds. It does not recompute a target, finite solve,
FFT, old cap residual, or repair.

## J.1. Exact original inputs

The original full193 index is
data/current_root_phase_response_20261114/response-full.json, SHA256
ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6.
Its physical state order is the sine amplitudes $j=1,\ldots,96$, the
true even mean, and cosine amplitudes $j=1,\ldots,96$, with angular
frequency $4j$. The cubics have the exact binary64 coefficients of the
original descending-power PPoly. They are already physical response
amplitudes: there is no new factor $\alpha$ or $\sqrt2$.

Only original shards 012 and 013 meet $I$. They are restored byte for
byte from the already successful public body-preparation artifact
visible-exact-body-prepared-43583838026-1, artifact ID 14109363064.
Their original SHA256s are respectively
777337c853329f26719b148e34db079c5ca0ed34991aa40220f25624e4af0b3c
and
4a863085ec89c7d7104b4fdf566f9ae380d22eb7b4e4f8b2146cd190c3b4b037.
The original index, both complete shard bytes, exact common node, and
every actual cap interval are checked. No new index or cubic is defined.

The exact continuous direction has definition SHA256
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
Its already complete certificate is
notes/2026-11-14-R133-explicit-continuous-response-direction-native.json.gz,
SHA256
87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88.
The field exact_complete_repair_coefficient_suprema contains all 193
exact rational upper bounds $e_k$ for the constant repair on every
original radial piece. This field is used directly. Its negative-only
norm tables are not used as positive-cap bounds.

## J.2. A complete exact Bernstein enclosure on each actual restriction

For an original scalar amplitude
$p(x)=c_3x^3+c_2x^2+c_1x+c_0$ and an actual intersection
$[a,b]\subset I$ of its original radial cell, put
$x_0=a-r_j$, $\ell=b-a>0$. With $t\in[0,1]$,
$$
 p(x_0+\ell t)=d_0+d_1t+d_2t^2+d_3t^3,
$$
$$
 d_0=p(x_0),\quad d_1=\ell p'(x_0),\quad
 d_2=\ell^2(3c_3x_0+c_2),\quad d_3=\ell^3c_3.
 \tag{J.1}
$$
Every coefficient and endpoint in this calculation is an exact
Fraction obtained from the original binary64 value or the specified
rational cap endpoint. The Bernstein coefficients are exactly
$$
 b_0=d_0,\quad b_1=d_0+d_1/3,\quad
 b_2=d_0+2d_1/3+d_2/3,\quad
 b_3=d_0+d_1+d_2+d_3.
 \tag{J.2}
$$
The cubic Bernstein basis is nonnegative and sums to one. Therefore
$$
 \sup_{r\in[a,b]}|p(r-r_j)|\le\max_{0\le l\le3}|b_l|.
 \tag{J.3}
$$
The first and last true intersections are handled by the same exact
formula; $9/10$ is not replaced by its neighboring floating-point node.

For each state coefficient separately take the maximum of (J.3) over
all actual intersecting pieces:
$$
 a_k=\max_{j:\,I_j\cap I\ne\varnothing}
       \max_l|b_{j,k,l}|,\qquad z_k=a_k+e_k.
 \tag{J.4}
$$
The stored 193 exact $a_k$, 193 original exact $e_k$, and 193 exact
$z_k$ retain the independent even mean. All intervals are checked as an
ordered gap-free cover of the entire $I$. Each completed row records the
SHA256 of its complete 193 exact Bernstein bounds and the exact original
shard/interval; the final coefficient maxima also retain their actual
maximizing pieces. No rowwise scalar bound is relabelled as a joint norm.

## J.3. Complete joint analytic norms and angular derivatives

Let $n_k=4j$ for either sine or cosine amplitude of index $j$, and let
$n_{96}=0$ for the true mean. A real sine or cosine amplitude contributes
its full modulus to the sum of its two signed complex Fourier
coefficients. Thus there is no missing factor two.

For each
$\sigma\in\{0,1/256,1/128,1/64\}$ and $q=0,1,2$,
$$
 \|\partial_\phi^q Z\|_{\mathscr A_\sigma,I,\mathrm{pair}}
 \le\sum_{k=0}^{192}z_k n_k^q e^{n_k\sigma}.
 \tag{J.5}
$$
For $q=0$ the multiplier at $n=0$ is one; for $q=1,2$ it is zero.
The two components, their complete pair, and the separate raw/repair
contributions are all reported. Every exponential and final sum is
enclosed by 320-bit Arb arithmetic on the public runner.

Here the joint norm means the sum of the separate complete radial
suprema. It is stronger than a supremum of the radial pointwise sum.
Equation (J.4), before (J.5), is precisely the required order. These are
homogeneous angular derivatives, not radial derivatives of the repair.

The norms concern the same fixed physical $\eta_0,\nu_0$ and the original
moving angle $\phi$. They can be multiplied by $|\delta|$ for the already
defined explicit affine family. A fixed physical-angle composition must
still use the separately proved complete angle bound; a change of the
unknown's angle is not declared close to identity. No changed outer
boundary, complete infinite inverse, nonlinear solution, or parameter
Schur is certified here.

## J.4. Execution and exact recovery

The original index, repair certificate and preparation receipt are
immutable pins. The public worker downloads the original preparation
archive, verifies its exact artifact identity and original byte digest,
and restores only the same index and two complete cap shard bytes.
It never invokes the historical reconstruction producer.

A scientific prefix contains the exact completed interval receipts,
all 193 running exact coefficient maxima and their maximizing pieces.
Only that exact successful prefix may be resumed with the same source
and inputs. A genuinely failed mathematical gate is not repeated without
a correction. An already complete child-0 native is reused if a later
publication failed. Actual process, source, native and summary identities
are preserved separately.

New native data are one natural compressed certificate; summaries are
genuine bounded summaries below 60000 UTF-8 bytes. Large original binary
inputs remain in public Actions artifacts. Real pull and README checks
run before publication and every ten minutes during a long child.
This first consumer pays only (J.5); it does not infer full-cap
$\beta,\gamma,K$ bounds from root data.
