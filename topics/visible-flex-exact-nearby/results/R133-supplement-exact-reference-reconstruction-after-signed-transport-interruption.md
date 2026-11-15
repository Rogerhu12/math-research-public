# R133 supplement: exact reference reconstruction after the fifth signed-transport interruption

2026-11-15. This is a recovery contract for the one interrupted new SN target. It does not repeat any previously completed residual, parameter or energy budget. It changes no signed transport equation, derivative order, parameter ball or physical angular convention.

## RR1. Actual interrupted execution and preserved evidence

The fifth public execution was **43746794222/1**, job **132911762122**, on workflow commit **31e2a9bf985007ac16a37778a040b944f9bcdd6a**. Its immutable scientific source and arithmetic helper were:

- source SHA256 **540a0f8edea546a478907579e68be764c8985a317d80062d03175da58a132e99**;
- helper SHA256 **217a91e25ec7bb6cad5c115ddc4749f4d714c5ca47601e8ad8dd540e69ed1718**;
- input manifest SHA256 **bbe747a6bcb0c5384472a0996a1e2b7a7236555c1d583ec1607899f461c8be36**.

The complete published execution is
[execution.json](../notes/signed_nonmean_density_H3_ci/run-43746794222-1/execution.json),
blob **cdd801b262702cbbcc25ded730f34c6e2d53a0fd**, **30,735 bytes**, SHA256
**d2855e79fbf3332a993b927ff74d3371e72b74748145d87f191666803a360d56**.

The actual supervision exception was a read-only Git-tree metadata request returning HTTP 502. The worker then terminated the active mathematical child, which returned **-15**. The scientific failure field is null. All 17 scientific gates reached before transport completion had passed. This is not a successful completed H3 target, nor evidence that the mathematical domain failed.

The exact original scientific JSON is recovered from the complete embedded receipt by its original sorted-key canonical encoding. Its size is **17,323 bytes**, and its SHA256 is
**97f2e921dd6f846f9e46b28e4fbfb9fd7ccc8cb8e2862716ea6e137e62ba526e**.
This byte identity is checked independently; a differently ordered JSON representation is not substituted for it.

The saved complete transport endpoint has:

- **314** completed original intervals;
- **1,256** completed new subcells, each counted once after both branches;
- the exact common radial cursor
$$
 r_*=\frac{34092249179194657}{144115188075855872};
 \tag{RR.1}
$$
- both complete four-column outgoing H3 derivative-error bounds;
- the next original interval, index **2831**, with its exact endpoints, original candidate piece **2473**, exact two linear-mean coefficients, complete mean-reference validation, speed bound and optical work upper;
- the already completed angle and root-entry conclusions inherited from the earlier immutable preparatory execution.

The last subcell diagnostic belongs to completed original interval 2832, branch +1, subcell 3. Its residual, parameter, drift, jump and energy scalar columns are saved and finite. The next original interval 2831 had reached its saved mean-and-speed stage. Work after that checkpoint is not specified by the saved receipt and may have been in progress when the worker terminated it.

## RR2. Precisely what was lost

The temporary file **complete-new-signed-source-and-reference.jsonl.gz** had **365,535,907 bytes** and SHA256
**7a83abf8eeaa687e6ff6ae59d2374eacabb8dda8ecc14a58260e384d08db3a98**.
It was never uploaded to Git, a Release or an artifact.

Each uncompressed record contains an original interval and piece identity, an exact subcell interval, and two branch records. A branch record contains the complete finite Taylor force and speed, the proposed finite reference coefficients, the complete residual polynomial, the derivative-error columns, source-error columns, mean error and energy matrix. The small scientific receipt does not contain the finite reference coefficients themselves.

In particular the original receipt does not retain the accumulated reference hash or either final reference polynomial, and it does not retain the complete prefix maxima of source, parameter or mean diagnostics. The whole temporary gzip hash cannot be checked by regenerating only reference values: its bytes also contain the already completed directed residual and energy budgets. Those budgets must not be recomputed merely to reproduce that container hash.

The recovery below therefore records a **new reconstruction hash**. It expressly does not claim equality to an originally saved prefix-reference hash, because no such hash was saved. The original temporary-file identity remains an honest lost-data receipt.

## RR3. The saved counts determine every prefix subdivision

In the original source every original interval uses
$$
 p_i=4\max\{1,\lceil\operatorname{upper}(\mathrm{work}_i)\rceil\}.
 \tag{RR.2}
$$
Thus each completed interval contributes an integer multiple of four subcells and at least four. The saved endpoint has
$$
 \sum_{i=1}^{314}p_i=1256=4\cdot314.
 \tag{RR.3}
$$
Consequently **every one of those 314 intervals used exactly four subcells**. This conclusion follows from the completed counters and the frozen original algorithm; it does not require evaluating an old speed bound again.

The exact ordered original intervals are indices 3145 down through 2832. Their four equal rational subdivisions are recovered directly from their original exact endpoints. Both branches use the same subdivision, as in the original source. The resulting last endpoint must equal (RR.1).

## RR4. The reference depends only on finite point data

The original reference is a numerical proposal whose residual is validated separately. It starts from the exact zero polynomial at the original strict cut. The angular support is quarter-mode 128, the physical frequency is 4j, the radial degree is six, and every proposal coefficient and endpoint is recentered to the same exact dyadic real Fourier polynomial with zero mean.

On an original interval with inward coordinate t = right - r, its linear radial mean reference is
$$
 \widehat m(t)=m_0+m_1t,\qquad
 m_0=\operatorname{mid}_{\rm dyadic}(m_{\rm old,right}),\quad
 m_1=\operatorname{mid}_{\rm dyadic}
       \left(\frac{m_{\rm old,left}-m_{\rm old,right}}
                    {\mathrm{right}-\mathrm{left}}\right).
 \tag{RR.4}
$$
The endpoint enclosures are read from the old completed scalar integral. Equation (RR.4) is only the definition of the lost reference proposal. It does not reevaluate the old scalar integral, the new mean curvature bound or its interpolation error.

For each of the known four subcells, the original complete Taylor routine had combined point coefficients of orders zero through five with a final whole-subcell coefficient of order six. The degree-six reference recurrence uses only the first six coefficients:
$$
 v_0=\operatorname{mid}_{128,0}(v_{\rm in}),\qquad
 v_{k+1}=\operatorname{mid}_{128,0}
 \left[
 \frac{F_k-\partial_\phi
      \sum_{i=0}^{k}a_i v_{k-i}}{k+1}
 \right],\quad 0\le k\le5 .
 \tag{RR.5}
$$
Its endpoint is the same midpoint projection of
$\sum_{k=0}^6v_kh^k$. The two midpoint operations retain the full positive and negative Fourier signs and set the reference mean to zero exactly.

The reconstruction therefore calls only the same nominal point source at the original right endpoint, with the original Taylor order seven and the original exact linear reference (RR.4), followed by the unchanged reference_step arithmetic. It does not call complete_taylor's whole-cell branch, complete_reference_residual, parameter_error or gram_error_step on any of the completed 1,256 subcells.

All original scientific input hashes, source definitions, helper hash, 320-bit precision, Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5 and the original arithmetic context remain fixed. The nominal point field and finite proposal routines are unchanged. Induction through (RR.5), in the same serial operation order and on the exact subdivisions from RR3, reconstructs the original lost finite reference endpoint.

This is a deterministic reconstruction under frozen arithmetic identities. It is not an independent comparison to an unavailable old polynomial. The new hash records the reconstructed value and is labelled accordingly.

## RR5. Resume with the saved complete error certificate

For each branch the fifth execution already certified, at the common endpoint (RR.1),
$$
 \|\partial_\phi^q(V_{\sigma,\delta}
                  -\widehat V_{\sigma,*})\|_2
 \le E_{\sigma,q}^{\rm saved},\qquad 0\le q\le3,
 \quad |\delta|\le10^{-10}.
 \tag{RR.6}
$$
All old source terms, parameter variation, true means, reference jumps and directed energy steps are included in these saved columns. The recovery reads their upper endpoints; it does not verify the completed residuals or energy steps a second time.

Once RR4 reconstructs the same $\widehat V_{\sigma,*}$, (RR.6) is the initial error certificate for the remaining suffix. The next original interval is index 2831, whose complete mean and speed data are also read from the fifth receipt. Every later suffix interval is a genuinely unfinished part of the same new target and uses the unchanged SN validation.

The final endpoint reference and error columns therefore cover the entire path, with the prefix supplied by its already completed certificate and the suffix supplied by the new continuation. Every original value interface, both branches, the physical 4j convention, the complete mean and the real parameter fee remain unchanged.

Prefix source/parameter/curvature maxima are not reconstructed from bounds for other quantities. Final diagnostic maxima newly computed on the suffix are explicitly labelled as suffix maxima. They are not used as whole-path maxima. The complete first-symbol H3 conclusion uses the endpoint reference and the complete transported errors, not these auxiliary maxima.

## RR6. Checkpoints, publication and scope

The new execution must verify the complete fifth receipt, its exact scientific byte hash, all original input hashes, the 314/1256 counters, the exact common cursor, both four-column errors and the next saved interval before reconstructing any reference. The four preparatory stages from the third execution remain read-only.

New checkpoints record the exact common cursor, completed-prefix and newly verified-suffix counts separately, both error columns, the current reference endpoint hash and the scope of any running maxima. A reference hash alone is not claimed to contain its coefficients. All finite reference arrays remain temporary in the public runner.

A read-only metadata transport failure may postpone capacity auditing and publication; it must not kill a healthy immutable scientific child. Actual README changes, failed frozen-input identities, a proved topic-capacity violation or mathematical failure remain fatal. No Git publication may use stale capacity after a failed audit. True pulls and README checks remain periodic.

No job is started by this contract. Deployment requires the explicit recorded lost-result scope and a separately reviewed source, worker, manifest and workflow. Successful old scientific consumers and the 1,256 completed prefix residual/parameter/energy budgets are never rerun. This recovery supplies no new numerical H3 constant, high inverse, incoming inverse, strong-return remainder or nonlinear solution.
