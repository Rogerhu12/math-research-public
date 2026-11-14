# P1: complete DQ window coefficients at the translated inner width

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Scope and actual input

This is a source-coefficient result conditional on the already established modal centre bounds. It constructs no ODE or Green kernel, no nonlinear fixed point, no old/new solution identification and no cut or surface theorem. Every output belongs to the original inner physical field and the actual P1 parameter domain; none is transferred to a new strong-amplitude metric.

The actual input is `inner-P1-shift040-modal-r1.json.gz`, SHA `c23f7f76037247d877a62833f00eb9a96798d4720b8188c5243bc8f128a3c773`, with its own completed resource SHA `0b042b5eabf6a78702b07dc33e03608110d2033ba469698bb99f40c03e4dc426`. It supplies every cell 12 through 224, the full 46 even centre modes 2 through 92, the complete saved common centre mass and all exact parameter caps. The domain is `R156_actual_full_cut_posterior`, with S product radius 3/8, T common radius 1/64 and its 46 saved individual T caps, without replacing them by a larger independent box.

The actual source width is

\[
\tau'_n(r)=\tau_n(r)+2/5.
\]

For every cell, the consumer checks its original outer-width lower bound against the pinned original density and checks that the new bound is exactly that old rational plus 2/5. The original physical B and its floor remain unchanged. The physical normalization remains

\[
V'=(257/256)V_s.
\]

The input centre caps are already the actual caps in the new translated width. No full error field, infinite tail or previous fixed-point radius is reweighted by this producer. A later finite consumer must supply its own valid error bounds in this width.

## Paired Fourier convention and two materials

Let \(c_k\) be the saved nonnegative strong mass for the signed Fourier pair of centre mode \(k\), in physical \((Bp,\kappa_\perp)/V'\) normalization. Let \(z_n\) denote the corresponding strong pair mass of an input direction. The pair convention includes both Fourier signs; no further factor 2 is added.

For the original derivative \(DQ(C)[e]\), the previously proved two-material positive coefficients are

\[
\beta_s(k,n)=\frac{5kn}{4(1+k)(1+n)},
\]

\[
\beta_\ell(k,n)=
\frac{\max\{1,5k/(4B_0),5n/(4B_0),(5kn+1)/(4B_0^2)\}}
 {(1+k)(1+n)}.
\]

Here \(B_0=\lfloor B\rfloor\) is checked separately in every cell and is at least 120. The numerator has already paid angular derivatives. These are DQ coefficients, not the half-sized coefficients of an ordered-pair representation of Q itself.

The output is a weak Fourier source mass. No output \(1+m\) factor is built into these coefficients. In the relative equation for N the radial materials are \(s(V'/w)^2\) and \(|\ell|(V'/w)^2\). In the physical \(\kappa\) source \(wN\), the corresponding two materials are exactly

\[
d_1=\frac{V'^2}{rw},\qquad
d_\lambda=\frac{|w_r/w|V'^2}{w}.
\]

The later Green or endpoint consumer must use its matching material kernel once; this source table does not include any radial integration, Wronskian, frame jump, mean/inverse remainder or endpoint conversion fee.

## Sum and difference support

For output window \(W\) and a fixed input mode n, the complete positive coefficient is

\[
F_{W}(n)=\sum_{k=2,4,\ldots,92}
c_k\beta(k,n)\left[
\mathbf1_{k+n\in W}
 +e^{-2\min(k,n)\tau'_{n,\mathrm{out}}}
  \mathbf1_{|k-n|\in W}\right].
\]

All output windows start at 94. Consequently a nonzero difference contribution has n > k, so the minimum in its exponent is k. The decay factors are newly evaluated at the actual translated width; no old-width decay table is reused. Each window coefficient is an upper bound for \(\sup_{n\in I}F_W(n)\), where I is one complete input window. Thus

\[
\|\Pi_W DQ(C)[e]\|_{\mathrm{weak,material}}
\le\sum_I K_{W,I}\sum_{n\in I}z_n.
\]

This consumes each input window's common strong mass once. It does not replace that common mass by a cap independently available to every n, and it does not multiply by the number of modes in the window.

The 13 output windows are [94,94], [96,96], [98,104], [106,112], [114,128], [130,184], [186,192], [194,256], [258,512], [514,1024], [1026,2048], [2050,4096] and [4098,8190]. The 15 input windows are [2,92], those same 13 windows, and [8192,infinity]. For a fixed output window all n above its maximum plus 92 have exactly zero DQ support. The infinite input window is therefore treated by its entire finite relevant segment, including the possible 8192 through 8282 differences into the final output window. Its contribution is not discarded.

## Finite maximization and singleton inputs

The saved 1,806 even-frequency membership intervals contain all changes of the sum/difference support. Within each such interval the centre sums and their difference weights are independent of n. The s coefficient is a nonnegative constant times n/(1+n), hence its maximum occurs at an endpoint.

Because k <= 92 and B0 >= 120, the ell numerator reduces exactly to max(1,5n/(4B0)). Indeed 5k/(4B0) <= 1 and 1 <= 5n(B0-k) imply that the remaining mixed numerator is bounded by 5n/(4B0). With t=1/(1+n), the ell coefficient is a nonnegative constant times max(t,5(1-t)/(4B0)), a convex function. Its maximum on each membership interval also occurs at an endpoint. The original endpoint algorithm therefore covers every possible even n, including the relevant part of the unbounded input window.

The same inequalities give coefficientwise beta_ell <= beta_s. The producer checks all 41,535 resulting window/material comparisons and keeps the 213 complete per-cell aggregate gate records. It retains both material matrices for consumers that can benefit from the smaller ell coefficient.

The companion singleton table keeps each of the 46 low input modes separately. For k,n <= 92, the difference frequency is at most 90 and cannot enter any output window. Only the original sum support is present. For every cell and output window, all 46 individual low columns are retained. Their distinct caps can be summed, or a common-mass support functional can be applied to those same columns; a common low mass must not be repeated 46 times.

All arithmetic uses 256-bit Arb enclosures. Every saved coefficient is rounded upward to a positive dyadic with 160 significant bits, with the outward inequality checked by the original packing routine. Exact rational input widths, original B floors, the full parameter domain and all support partitions are retained in the mathematical payload.

## Actual outcome and memory limitation of the first attempt

The completed second producer formally exited 0 in 17.672854740 seconds with an owned peak of 91,892 KiB, below 96 MiB. It retains 213 rows, all 213 x 2 x 13 x 15 window coefficients, all 213 x 2 x 13 x 46 low-singleton coefficients, 47,107 saved positive gates and 41,535 actually executed material-domination comparisons. No ODE, Node worker or new Green integration ran.

The first producer also completed its mathematical checks and returned exit 0, but the final report allocation raised its measured peak to 98,536 KiB, 232 KiB above the requested 96 MiB limit. Its internal pre-report guard did not catch that final increase. It is retained as an attempt that failed the actual memory budget, with its original exit code unchanged. The successor removes only the 41,535 duplicated dictionary keys for domination checks: every comparison still executes, and one aggregate record per completed cell is saved. It does not weaken or change a coefficient formula, strip, parameter domain or positivity test.

## Reproduction and compact storage

The complete second primary is 4,433,403 bytes, SHA `5ea3bb43d88beac1b1cbe784097397d9756e6e96b6c9ecdeda72fa047409be3d`. It stays in scratch as a cheap regenerable intermediate under repository rule 11 and is directly available to the current finite consumer. The committed material is the complete source, input identities and domain, this proof, both measured resource records and a mathematical reproduction digest.

The owned resource preserves the exact producer argv. Re-run it with the identical pinned modal input, original density and same arithmetic versions, using a fresh output path. The complete primary's volatile timing and command fields may differ on regeneration. The companion `inner_DQ_source_math_digest.py` hashes the complete nonvolatile mathematical payload, including every coefficient, centre cap, width, parameter cap, window, support partition, normalization and contract. The canonical mathematical SHA is `4421fdbce8153c6bf7006fd1c51e6cbb52a413f2c1d1dbd6036b09a1ed4456b2`; this is the identity to compare after regeneration. The original complete byte hash remains an immutable identity of the actual run and is not silently changed.

Full quadratic unknown-error terms, the complete mean/inverse remainder, far input and any old/new solution comparison remain separate obligations of the downstream consumer. This result establishes only the stated uniformly valid DQ source coefficients on the actual translated P1 domain.
