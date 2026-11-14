# R717: p137147 certified budget and public artifact resume

Status: the analytic error and linear storage reductions below are proved.
The actual original norm at p137147 is not supplied by these reductions.
All target arithmetic is assigned to the public repository's GitHub Actions.

## Completed calibration and unchanged mathematical source

The public p41 calibration run 43597163388 used the complete original
norm algorithm, not a rerun of the old torsion orbit.  It covered 128 rows
and 3712 lattice terms and recovered p^2 S2 S3 = 1274 modulo 41^2 and
(p M2)^2/zeta^2 = 24 modulo 41.  Its core receipt SHA256 is
fb4d9ffadacda241575ab92a49f66819d8ac077ececa8f5151adf4aea3751fa6.
The p137147 request retains the identical mathematical core SHA256
75a81149a898e71ab33413ddd2cebc49a4b8abdbe6e8c0bc964a56092098d402.
The completed p41 calculation is not to be repeated.

## A strict smaller analytic budget

Use the notation of R717: c = pi/(3 sqrt(3) p),
kappa = alpha^2/(144 Omega^2 A^5), and D = 2^37 3^26 p^5.
The real-period integral gives Omega > 2.  Also A > 1 and alpha^2 < 3,
so kappa < 1/192.  The elementary inequalities pi > 3 and sqrt(3) < 2
give 1/c < 2p.

The same ideal-counting argument used for the full R717 tails gives,
for every truncated central-value sum as well as the full sum,

$$
|L_5^{\rm trunc}| \le 4\int_0^\infty K_2(cx)\,dx=12/c<24p,
\qquad
|L_7^{\rm trunc}| \le 16/c<32p.
$$

If each central value is enlarged by an analytic error radius
epsilon = 2^(-256), the analytic contribution to any integral trace
radius is bounded by

$$
nD\kappa p^2(56p\epsilon+\epsilon^2)
<
2^{37}3^{26}\left(\frac7{12}p^9\epsilon+
                    \frac1{96}p^8\epsilon^2\right)
<2^{-14}.
$$

Here n = p+1 < 2p, p = 137147 < 2^18, and
2^37 3^26 < 2^79.  In fact this deliberately loose last inequality
holds for every p < 2^18.  It does not estimate floating-point
rounding errors: those remain included in the exact Arb balls and
must pass the unchanged unique-integer test with radius < 1/4.

Set X = 360p.  Then x = cX > 216, since pi/(3 sqrt(3)) > 3/5.
For completeness, sqrt(3) < 26/15 and pi > 25/8 imply the latter
strict bound.  The lower bound for pi also follows directly from
Machin's identity and the alternating arctangent series:

$$
\pi=16\arctan(1/5)-4\arctan(1/239)
>16(1/5-1/375)-4/239>25/8.
$$

The polynomial Q_3(x) = 4+3x+x^2+x^3/6 satisfies
(d/dx)(exp(-x) Q_3(x)) < 0 for x >= 0.  Moreover
Q_3(216) = 1726924 < 2^21.  Since e > 8/3 and
(8/3)^5 > 2^7, one has e^216 > e^215 > 2^301.
Consequently the complete omitted-lattice bound is

$$
{\cal E}_3(X)
<8p\,e^{-216}Q_3(216)
<2^{3+18+21-301}=2^{-259}<2^{-256}.
$$

The r = 2 bound is smaller.  The core still independently certifies
both strict tail inequalities with Arb before accumulating any bins.

Thus the request uses precision 384 bits, tail target 256 bits, and
cutoff 360p.  Choosing a working precision is not a proof that its final
balls will be narrow enough: a run is complete only when all trace
intervals certify unique integers.  Failed precision is preserved as
a failure; it is not silently rounded or called a zero.

## Four disjoint shards and linear memory

Here n = 137148, X = 49372920, and a_max = 8113.  The four row sets are
a = i+1 modulo 4, for i = 0,1,2,3.  Their row counts are respectively
2029, 2028, 2028, 2028; the last rows are 8113, 8110, 8111, 8112.
They cover every original sector row exactly once.

Each bin job holds four arrays of n real balls and the finite-field
log tables; it never forms an n by n Fourier matrix.  The three
certified transforms use Bluestein multiplication of polynomial
lengths n and 2n-1.  Their product length is 3n-2 = 411442.
Thus the arrays and polynomial storage are linear in n, apart from
the bit lengths of ball endpoints and the multiplication library's
working storage.  This is an algorithmic storage bound, not an
unsupported numerical promise about Python's exact resident bytes.

The workflow has at most two concurrent bin jobs.  Each row prefix
is checkpointed every 100 assigned rows, with a final complete
checkpoint.  The explicit compute budget is 18000 seconds, inside
a 305-minute compute step and a 350-minute job.  Budgets are limits
for preservation and resumption, not estimates of the running time.
No target arithmetic was run locally.

## Large artifacts and restart without repeating completed work

Every job uploads the entire output directory, including gzip bins,
sources, receipts, logs, and failures.  The public publisher retains
bounded files in git and a SHA256 manifest for every omitted large
file.  Files above the repository's size limit stay in the original
Actions artifact; they are not divided or encoded into connector calls.

The single recover job downloads the four complete bin artifacts on
the runner through the GitHub CLI.  It checks each original complete
receipt, the bin SHA, the common source commit, the pinned arithmetic,
the exact configuration digest, every row endpoint, and complete
coverage before merging.  On a failed-job rerun it can select a
successful earlier attempt of the same workflow run for a shard.

If an interrupted prior run must be resumed, the request's
resume_artifacts list supplies its run ID, exact artifact name, result
identifier, and the SHA256 of the actual bin checkpoint (or complete
final receipt).  The restoration helper downloads on the runner and
checks those fixed hashes before the core sees any input.  Compatible
complete bins and complete final receipts are reused; incomplete bins
resume after their last recorded consecutive assigned row.

The wrapper checks the two README files at each elapsed hour during
a long core process.  It fetches the current main without changing the
running source checkout.  A rule diff or failed rule check is saved,
the process is terminated with its latest atomic checkpoint retained,
and root applies the actual new rules before resumption.  The public
publisher also performs its existing README checks after each pull.

The original request and output path are retained in a runner session,
so publication's checkout of the latest main cannot change the final
verification's calibration or input parameters.

## What a successful target certificate establishes

A completed target receipt determines the exact algebraic original
S2 S3 / C0^2 and its selected p-adic value, or certifies that it is exactly
zero through the exact cyclotomic remainder.  If the value is nonzero,
it reports the actual valuation of M2 and its normalized leading square.
The request does not require a unit result.  It does not replace the
original value by a high-precision lift of C_(p-3), and it asserts no
height exclusion or completion of the Serre problem.

The artifact transport follows the official GitHub CLI manuals:
[gh api pagination and slurp](https://cli.github.com/manual/gh_api) and
[gh run download with a fixed run and artifact name](https://cli.github.com/manual/gh_run_download).
