# R717: independent chirp phases and reuse of the fixed public bins

This note describes a numerical enclosure repair. It changes no L-value,
period, Gauss factor, character label, denominator, analytic tail bound,
integer trace formula, or p-adic embedding in R717.

## 1. Exact phase identity

For $n=p+1$, the Bluestein convolution in R717 uses
$$
c_j=\exp(\pi i j^2/n),\qquad 0\le j<n.
$$
The original recurrence $c_{j+1}=c_j\omega^{2j+1}$, with
$\omega=\exp(\pi i/n)$, is an exact identity. It is nevertheless
ill-conditioned as a propagation rule for rectangular complex balls:
every multiplication encloses the rotated rectangle by a new rectangle,
and the loss is compounded over the full chain.

The repaired routine evaluates each phase independently:
$$
c_j=\exp\!\left(\pi i\,\frac{j^2\bmod 2n}{n}\right).
$$
The numerator and the reduction modulo $2n$ are exact integers.
The two displayed phases differ by the exponential of an integer
multiple of $2\pi i$, so this changes no Fourier transform. Division
and `exp_pi_i()` are certified ball operations. No chirp ball depends on
an earlier chirp ball, and the negative transform still uses complex
conjugation of the same independently enclosed phases.

For a transform sign $\epsilon=\pm1$, the unchanged convolution identity
$$
c_k^\epsilon
 \sum_{j=0}^{n-1}a_jc_j^\epsilon c_{k-j}^{-\epsilon}
 =\sum_{j=0}^{n-1}a_j
   \exp(2\pi i\epsilon kj/n)
$$
follows from $k^2+j^2-(k-j)^2=2kj$. Here $c_j$ is defined for
all integer indices; $c_{-j}=c_j$, so the stored convolution coefficients
also give the negative indices. The unchanged polynomial product
therefore encloses the same exact DFT as before.

The repaired source does not presume a numerical error bound or an
integer answer from proximity of midpoints. Every final trace must
still contain a unique integer, have an imaginary interval containing
zero, and have real radius strictly below $1/4$. The exact cyclotomic
remainder and the original Teichmueller p-adic evaluation are reached
only after all these tests pass.

## 2. Public retained-ball diagnostic

Public Actions run `43602040433` performed zero DFTs and zero lattice
enumerations. It inspected the original failed run `43597802237`,
verified the exact hashes of its four bins, embedding balls, trace balls
and archived producer, and separately compared the original chirp routine
with direct phase evaluations. Its complete summary is

`computations/R717-trace-diagnostics-p137147/43602040433-1/R717-diagnostic-summary.json`

with SHA-256
`7177f7a2a698d20fb4bb7789f9cb95f73c7aba3af272848cfa0b118a2d51ecbb`.

All $137148$ retained trace balls lacked a unique integer and had real
radius at least $1/4$; all their imaginary intervals contained zero.
The largest real trace radius was exactly
$$
532573319\cdot2^{278783}.
$$
The original chirp recurrence first reached component radius $1/4$
at index $3509$, and radius $1$ at index $3519$. Its largest
component radius was
$$
120899187\cdot2^{46409}.
$$
The thirteen representative comparisons, including index $137147$,
gave narrow directly evaluated phases, and both real and imaginary
differences from the original enclosures contained zero.

The four original bins remained narrow: the largest component radius
over all four shards was exactly
$$
794971585\cdot2^{-398}<2^{-368}.
$$
Thus the observed failure is a loss of useful numerical enclosure during
the recursive complex-phase propagation, already visible before a DFT.
It supplies no evidence that an exact trace is nonintegral, and no value
or valuation of the original $M_2$.

## 3. Explicit scope of the retained-bin compatibility

The optional compatibility interface authorizes only the four completed
files for $p=137147$ from public run `43597802237`, source
`ffc69b45d58ea9aaafd1e0686fc55377701a00be`. Each compressed bin has a
hard-coded SHA-256, as do the old source and its archived gzip file.
The old parameter hash and all source identifiers are also fixed.

The interface compares the entire old and new source prefix before
`def chirps(n):` byte for byte. That prefix includes the imports,
configuration and all finite-field, tame-character, interval-kernel and
lattice-bin producer code. The current mathematical source is itself
pinned in the request and in its new configuration. After the source
hash and parameter hash are replaced, every other configuration field
must be exactly equal. Each bin must still have the original
configuration, its exact assigned row count, its exact terminal row,
its matching shard index, and the completed flag.

This is not a general exemption from source or parameter equality. Runs
without this explicit manifest retain the original strict source
equality. The compatibility option is rejected in any phase other than
`recover`. The manifest and the old compressed source become hashed
artifacts of the final certificate.

The recovery wrapper copies only the four completed bins, the archived
original producer and this manifest. It does not copy the failed
embedding balls or failed trace balls. Three DFTs are recomputed from the
fixed bins using the independent phases; no lattice row or term is
enumerated again. A pre-existing compatible complete certificate is
reused, and a conflicting complete certificate causes a stop.

The wrapper records minimal input and failure receipts before source
archiving, archives all reviewed sources, checks both README files
against current public `main` before recovery and at least hourly
during a long recovery, and retains failure artifacts. A changed README
stops the immutable calculation for review. Only the public repository's
Actions executes the target calculation.

## 4. Interpretation

A diagnostic failure or a repaired numerical run is not a zero or a unit
statement about the original $M_2$. An actual value or valuation is
registered only after the full original trace certificate succeeds.
Even such a valuation is an Abel input; it is not, by itself, a height
identity or a Serre-uniformity exclusion.
