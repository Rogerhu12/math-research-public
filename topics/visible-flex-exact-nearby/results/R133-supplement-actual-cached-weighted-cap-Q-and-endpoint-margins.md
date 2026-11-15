# R133: actual cached weighted cap coefficient gate and scalar endpoint margins

## Actual result and exact scope

Public run [43695160055/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43695160055), at workflow commit `1c78995f9996ee2eac0909fed54b213af9c0eeff`, completed the mathematical child with return code **0** and **21/21 gates**. The scientific consumer took **1.277747273000017 seconds**. The decisive missing coefficient bound is now paid:

$$
 \max\{\|wQ_B\|_{\mathcal A_\sigma}^{\rm joint},
          \|wQ_C\|_{\mathcal A_\sigma}^{\rm joint}\}
 <3.561348304031\,10^{-6}<10^{-5},
 \qquad \sigma=1/8192.
$$

Here the background is the same fixed-$\eta_0$, continuously repaired M32 centre, with $\delta=0$, on the entire true cap $[9/10,25/8]$. The sum is over both Fourier signs and includes the complete even mean. The radial supremum is taken separately for every Fourier coefficient before the angular sum. The radial damping weight is the one defined from the original complete reference in [the frozen consumer contract](../notes/2026-11-15-R133-cached-weighted-cap-Q-contract.md).

This run supplies the numerical coefficient gate and scalar compatibility bounds required by [the weighted endpoint invariance theorem](R133-supplement-weighted-Q-endpoint-invariance-and-small-analytic-cap-ball.md), whose SHA256 is `0e6c0f6acfa4a40378176cf56e03ee941d1932885149a64cd145a7b4e9b91cfe`. Application of that complete theorem is a separate proof step. The consumer retains its explicit false flags for a complete nonlinear cap solution, complete endpoint invariance, and the whole infinite BVP inverse; its success must not be relabelled as a global PDE, high-frequency return, or $\nu$ response closure.

## Original evidence and execution identity

Both records below are complete original small texts from the actual run:

| Record | Bytes | SHA256 |
| --- | ---: | --- |
| [process.json](../notes/cached_weighted_cap_Q_ci/run-43695160055-1-cached-weighted-cap-Q/process.json) | 18414 | `3034426e40730fb3e6b880df66e551b4b0b158ecd178b833e532dfe07bfe18fb` |
| [actual-weighted-cap-Q-summary.json](../notes/cached_weighted_cap_Q_ci/run-43695160055-1-cached-weighted-cap-Q/actual-weighted-cap-Q-summary.json) | 32926 | `c0b2ba3c7c51f64c602f94951144dae92057dbedc7ef0ea3b83ed1a88a50fdb4` |

The process records one actual mathematical child, lasting 2.000678244999989 seconds including launch and polling. Its temporary log was 29504 bytes, SHA256 `3423712ab8e4839cb8b38ce043caece52b0e8e57b33a510ce018ef5e1b22d057`.

The final exact identities are:

- Science: `scripts/fourfold_codazzi_cached_weighted_cap_Q.py`, SHA256 `1be4b1115380c722a09c504e2fea99f6e32d3e0b12c8e92f44b1aa50ee27de16`.
- Worker: `scripts/fourfold_codazzi_cached_weighted_cap_Q_CI.py`, SHA256 `0e240776c168743dc39df806633ee718eab150beab610792decd18eaa7bfc20e`.
- Input manifest: `notes/2026-11-15-R133-cached-weighted-cap-Q-CI-inputs.json`, SHA256 `61def9069aaca22071de918d766e5d983f755d20e87fd924caa7c31e436edfeb`.
- Contract SHA256: `d709a83211053e2dee5a27e4ce6026403a4b510058627d7586d133ab45b764a6`.
- Workflow SHA256: `6bd876639c6dc1f7bc90568b314796464a3baeae71015f56b10b46a0a641e974`.

The 28 pinned inputs were all verified before the child ran. Seventeen original files were restored exactly from public history at `7c130fb94528de8f003a43e7049fb42768a64eec` into the temporary immutable scientific tree. Python 3.12.14, python-flint 0.9.0, numpy 2.3.5, and 320-bit interval arithmetic were recorded.

The actual temporary full output was **8193386 bytes**, SHA256 `58189255b268ef363fc2f495a26c4334c5da0e4c063fa110915babe7299cc06b`. It was not persisted. No new recomputable array, native output, Actions artifact, or Release attachment was published.

## New work and exact reuse

The original 4650 positive rows were restored from their existing four original parts and validated. Their original complete native SHA256 remains `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`. The consumer selected the 1346 cap rows and used the original 949 reference rows and 1346 closed intersections.

The only newly enclosed candidate component was the raw mean cubic, component 32, on **1346 exact Bernstein domains**, all inside the original candidate part004. The candidate index is the original ac1 identity `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`; part004 has SHA256 `314a6846ef2b5a257ddf20068332d105a7707b5aef27026f30477a47984eec4c`.

The finite coefficient envelopes, intrinsic row bounds, complete continuous repair, inverse-angle bounds, and prior L1 and endpoint source integrals were consumed in their original units. No old target, full coefficient convolution, L1 integral, endpoint Fourier moment, or reference Riccati solve was repeated.

For each Fourier label, the new row bound was intersected with its original complete global coefficient envelope. The exact common partition then supplied the weighted radial maximum for that label. Only after this operation were the full signed labels summed with the inverse-angle and $\sigma$ weights. This order preserves the joint norm; it does not replace the sum of radial suprema by a maximum of rowwise sums.

The actual inverse displacement upper bound was less than $0.003774145639$, so the needed moving width, $h_*+\sigma$, was less than $0.003896215951<1/64$. The old raw width-$1/32$ repair was added separately. The complete mean contribution to $Q_C$ remained present.

## Actual coefficient and reference bounds

All decimal bounds in this note are rounded upward from the original interval records.

| Quantity | Strict upper bound |
| --- | ---: |
| Repaired physical weighted $Q_B$ joint $\mathcal A_\sigma$ norm | $2.740389221095\,10^{-6}$ |
| Repaired physical weighted $Q_C$ joint $\mathcal A_\sigma$ norm | $3.561348304031\,10^{-6}$ |
| Complete reference $Q$ endpoint gain $K_e$ | $4.898174641284<5$ |
| $Q_B$ repair contribution | $9.662731242492\,10^{-18}$ |
| $Q_C$ repair contribution | $9.654488248239\,10^{-18}$ |
| Original raw joint $U$ bound | $0.019598031930<1/50$ |
| Original raw joint $V$ bound | $5.953141387043<6$ |
| Original cap $K$ upper bound | $0.164543193845$ |

The endpoint gain used the same completed scalar quantities
$T_{dc}<0.823763627240$,
$T<3.625263014269$,
$q_+<1.389936763369$, and
$K_C<0.891297546109$ in

$$
 K_e=T_{dc}T+(1+q_+T_{dc})K_C.
$$

These are consumed bounds, not a new reference solution. The largest weighted Fourier contributions occur at labels $\pm1$. The actual $Q_C$ mean contribution is nonzero, less than $7.275818711579\,10^{-8}$, and is included in the total.

## Full Fourier tails, true right data, and scalar margins

The old width-$1/8$ endpoint estimates were consumed using the complete infinite tail formula in F.12 of [the actual moving-centre endpoint proof](R133-supplement-final-moving-centre-actual-regular-boundary.md). At $\sigma=1/8192$, the full $B$ and $C$ tails are respectively below $1.493025965456\,10^{-37}$ and $7.023752409727\,10^{-37}$. Thus the tail allowance below $10^{-30}$ covers the entire infinite tail, not merely the old 128 retained modes.

The original finite source and endpoint moments were multiplied by their exact small-strip factors. The repaired right endpoint, true regular graph, and independent mean were then retained:

| Quantity | Strict upper bound |
| --- | ---: |
| Repaired nonmean endpoint $Z_0$ at $\sigma$ | $2.696354530653\,10^{-13}$ |
| Complete true right $d$ load at $\sigma$ | $1.341495597213\,10^{-15}$ |
| Complete true independent right $C$ mean load | $2.048793672765\,10^{-19}$ |
| Complete known body and affine load at $\sigma$ | $3.208341026859\,10^{-7}$ |
| Complete known nonmean endpoint load at $\sigma$ | $2.604258251649\,10^{-14}$ |

The scalar consumer used the complete original body-and-outer coefficient, less than $0.878289249280$, and retained the true outer $D_Zd$ bound, less than $0.005906950159$. For the exact declared radii

$$
 \rho=3\,10^{-6},\qquad
 \zeta=9.9\,10^{-10},\qquad
 r_Z=10^{-9},
$$

the recorded scalar inequalities give:

- Body image upper bound $<2.961873\,10^{-6}<0.99\rho$.
- Body Lipschitz upper bound $<0.880249<0.881$.
- Endpoint image using the fixed threshold $q_w<10^{-5}$: $<8.899801\,10^{-10}<0.9\zeta$.
- Endpoint image using the actual computed coefficient bound: $<6.827271113222\,10^{-10}<\zeta$.

The associated input ranges are the original nonmean inner $C$ port of norm at most $10^{-9}$ and normalized outer height of norm at most $2^{-60}$. Both complete means, the full true outer graph, the quadratic physical term, and the independently retained affine loads belong to the declared theorem. These scalar checks supply its required parameters; they do not construct or identify an unrelated global solution.

## Prior identity failure remains part of the record

The first public run [43694827122/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43694827122) returned child code **1** at its first scientific identity gate, before any new Bernstein domain or weighted row was computed. Its actual process and summary remain unchanged:

- Process SHA256 `f1fa9464130f6ad3ee502c63573920a7cec2419b70e1db737aafcd16d7859dc4`, 20886 bytes.
- Summary SHA256 `e4b62e7a64b15d0ec023012d605f9d8106ad0cc3b27c9cf37ead3fc94252c244`, 3648 bytes.

The failed constant had omitted one `b7` pair from the original producer SHA256. The corrected original producer identity is `1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c`. The correction changed only that identity and its dependent pins. No mathematical formula or numerical gate was relaxed. The two original failure receipts are explicit inputs to the successful run.

## Actual pull, README, and storage checks

The worker recorded four genuine pulls, each with an empty diff for both the root and topic READMEs. The first was at **2026-11-15 08:34:58.685207 UTC**, ending at `1e5ac783ec374d5188fdb47ef7f6338ade11f99f`. The final was at **08:35:10.052104 UTC**, at `8cf47d782bc952616f0e888dc56b2cbf565b8304`. A non-fast-forward publication rejection was retained and retried after a real pull.

The metadata-only topic audit, before the new final small records, found **199792517 bytes in 13973 files**, at commit `1e5ac783ec374d5188fdb47ef7f6338ade11f99f`, leaving 207483 bytes under the 200000000-byte limit. It did not read scientific data blobs. This is the recorded initial audit, not a claim about the current repository total after subsequent commits.

The run followed reviewed-rules SHA256 `f2661bd5cf5cb006c1f78c64126b3ac065e6bc26a50790545ac443efb5e372bd`. The published evidence consists only of the frozen scripts, parameters, run identity, output hashes, and small actual summaries. The full new numerical output remained temporary.
