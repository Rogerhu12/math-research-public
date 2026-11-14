# Full 213-cell canonical modal input for the existing R74 auxiliary family

2026-11-13, geometry_audit, GPT-6 Astra Pro, AI-assisted.

## Actual result

The fresh `inner_aux_all213_canonical_modal_input.py` has completed with
formal exit 0. All 20,352 exact identity, column, normalization, domain,
positive-far, and complete-map gates passed. The compressed input is
1,508,330 bytes, SHA256
`325bc24ddfed3a06702ea23a98511f7c87fb93c446c5978d47e28d203d61016e`.
The formal run took 19.955399751663208 seconds, peak RSS 90508 KiB.

This packet concerns the existing **old-g R74 auxiliary low46 family** on all
20 original independent parameter axes. It therefore also covers the R100
six-axis auxiliary restriction. It is not a packet for the accepted q098,
q106, or a future q122 metric. It proves no new existence theorem and does
not give a full-frequency head or cut by itself. It prepares actual data for
finite substitution into the already proved auxiliary fixed-point identity.

All 213 cells, all 46 low modes, every source-target pair, the complete mean
and inverse source domain, and positive true-far budgets remain. No ODE,
new Green kernel, source integral, or Node worker was evaluated.

## Exact normalization and usable matrix

For cell \(n=12,\ldots,224\), retain the original reference width

\[
 \tau_n=\max\{2,1+(n-12)\log(2)/4\}.
\]

Let \(x_n\) be the exact positive dyadic in `reference_x_upper`. It is an
outward 160-bit enlargement of that cell's original 192-bit reference upper
endpoint. Both the original interval and the chosen exact value are saved.
All subsequent factors, columns, common caps, matrix entries, and domain
checks use this same chosen \(x_n\). The field and the metric are unchanged.

The canonical norm of a positive mode is the complete reflected Fourier pair
with weight

\[
 e^{m\tau_n}\bigl((1+m)^3|Q_m|+(1+m)|\Xi_m|\bigr).
\]

The modal and common state caps in this packet are divided by \(x_n\).
The source norm is the original \(L^1_rW_{\tau_n}\) norm of the scalar
canonical \(\Xi\)-source.

The original `closure_plateau2_green.py` computes, for each mode, the actual
ordered \(\phi/\psi\) kernel, multiplies its output components by
\((1+m)^3\) and \((1+m)\), and includes
\(e^{m(\tau_k-\tau_n)}\). It then takes the maximum over all 46 modes.
Consequently the saved upper \(2^{\gamma_{kn}}\) bounds the operator on
each individual retained mode as well as the original common modal mass.
Using that same maximum for every modal equation is conservative; it does
not authorize summing 46 copies of a common source budget.

The true material coefficient \(B_n\) is enclosed from the original source
packet by

\[
 \widehat B_n\ge
 \frac{\operatorname{upper}(\mathrm{complete\_R23\_source\_L1}_n)}
      {\operatorname{lower}(\mathrm{reference\_X}_n)^2}.
\]

The lower reference endpoint in the denominator is essential. The chosen
\(\widehat B_n\) is itself an exact outward dyadic. The complete positive
matrix supplied to the consumer is

\[
 A_{kn}\ge
 2^{\gamma_{kn}}\widehat B_n\frac{x_n^2}{x_k}.
\]

Every one of the 45,369 entries is retained and positive. No additional
Fourier width, Wronskian, frame, or radial factor should multiply this
matrix. The underlying Green source, reference, original low46 columns,
ordered refinements, R74 family, original auxiliary box, true-far lift, and
R121 cell12 packet are all checked against their immutable SHA256 values.

## Actual linear modal caps

For each of the six original column groups and all 213 cells, the extractor
reads the complete \(Q,\Xi\) column suprema and divides by the proven
nonzero lower modulus of the actual shallow \(Q\)-gain. On cells with an
existing ordered refinement it takes the minimum with that independently
valid column bound. It then multiplies by the original shallow height bound
\(|q_m^*|+a_m\) on all 20 R74 axes; the other 26 shallow linear heights
are exactly zero. Thus no original nonzero center is deleted.

For the plateau, \(e^{m\tau_n}=e^{2m}\). For \(n\ge18\), use

\[
 e^{m\tau_n}=e^m2^{m(n-12)/4}.
\]

The rational bound \(e<87/32\) and a rational upper square root of 2
give positive outward endpoints, including the half-integer binary powers.
The independent original common linear cap \(\alpha=513/512\) remains
available. Every individual cap may be intersected with it, and the common
cap is the minimum of \(\alpha\) and the sum of all modal caps.

The source difference-frequency correlation is supplied for every positive
minimum mode \(m\):

\[
 e^{-2m\tau_n}\le
 \begin{cases}
 (3/8)^{4m},&12\le n\le17,\\
 (3/8)^{2m}2^{-m(n-12)/2},&n\ge18.
 \end{cases}
\]

These are rational bounds because \(e>8/3\) and all modes are even.
The matrix already transports the source width to the target width; the
correlation factor belongs only to opposite-sign input interactions inside
the source convolution.

## Simultaneous common, modal, and far budgets

For the original R74 correction radius \(\rho_n\), all modes initially
have the valid cap \(\rho_n\), and the independent common cap is also
\(\rho_n\). On cell12 only, the proved R121 complete modal and common
caps are intersected after explicitly multiplying by its saved reference
upper divided by the newly chosen \(x_{12}\). Thus the data use the same
field and correct normalization even if two outward stored endpoints differ.

The unchanged complete field cap is
\(S U_n\), where \(S=257/256\). The R23 domain is rechecked after the
small outward reference enlargement, and the packet supplies

\[
 R_n\le\frac{\widehat B_n x_n}{32}X_n,
 \qquad
 \|\text{source}\|\le
 \widehat B_nx_n^2
 \left[\frac{23}{288}\operatorname{conv}_n
       +\frac{13}{16}R_nX_n^2\right].
\]

The constants are the complete R121/R23/R106 inequalities, including the
mean root and full inverse remainder. A consumer must retain a separate
common source budget and charge the shared complete remainder once there.

For each target, the saved positive far budget is

\[
 f_k\ge B_{{\rm far},k}\,2^{1967}(2^{-2224})^2/x_k.
\]

It is one common low46 mass, retained strictly positive at every target.
It is a valid individual modal cap, but a common row adds it once. The
extractor also verifies for every target that the original complete coarse
source image, including all 213 sources and this far mass, remains below its
original R74 correction radius after the chosen reference enlargement.

## Consumer schema and finite-induction scope

The schema is `inner-r74-all213-canonical-modal-bootstrap-input-v1`.
Every numerical cap is `[mantissa_string,binary_exponent]`, an exact dyadic
upper. `A_upper[target][source]` uses the matrix above. Each `rows[n]` includes
the original and chosen reference, material coefficients, 46 linear caps,
independent common linear cap, 46 initial correction caps, common correction
cap, source physical conversion, opposite-sign correlations, full domain,
and shared true-far cap.

Finite updates of the form

\[
 E_{km}^{\rm new}=\min\left\{E_{km}^{\rm old},\rho_k^{\rm new},
 \sum_nA_{kn}\left[\frac{23}{288}\operatorname{conv}_{nm}
  +\frac{13}{16}R_nX_n^2\right]+f_k\right\}
\]

are legitimate enclosures of the existing same auxiliary field when all
common rows are paid simultaneously. This preparation does not execute or
claim such later updates.

An initial r1 extraction passed its arithmetic checks but was not released
to a consumer: its reference serialization required an explicit choice of
one saved normalization, and an unused gain-ledger label needed the original
interval instead of an upward-compressed value called a lower bound. The
r2 source chooses the exact saved reference before every calculation,
rechecks all whole-cell domains and maps, and stores each original gain
interval. The r1 source/resource and output hash remain as a reproducible
audit record; only r2 is the scientific consumer input.
