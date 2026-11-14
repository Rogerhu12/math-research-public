# R133 supplement: actual Fourier mean and fixed-eta subcell source diagnostic

2026-11-14. Public run
[43607383671](https://github.com/Rogerhu12/math-research-public/actions/runs/43607383671)
completed all seven gates. It evaluated the fourteen declared cached
rows and eighty new target calls, covering eight selected original
rows at one and four equal radial subcells. The mathematical child
took92.289771341 seconds; its actual wrapper child returned zero
after95.002834802 seconds.

The new radial subcells substantially tighten the large low193
source bounds. Restricting the parameter to fixed physical eta
without radial subdivision gives only a small change on those
rows. Direct Fourier mean correction also removes the severe
interval decorrelation of the former sample/FFT round trip.

## Exact actual records

| Object | SHA256 |
|---|---|
| Mathematical source | 51a7f917aeb3849aafb44de17be709664ff19e39b92ca4ee08fbb5df1bbfda7f |
| 131-input manifest | f0fae9a54a8a5655b81c0721bee613e45b4efbbc8549f284317e5ae680449bb8 |
| Complete new native | a73382575ca2b14afb810c2ed43ae0aec9d59aef563635a19f6785b414111993 |
| Actual small summary | 250ebccd140b3997615f7742bf0acb16359f1c93d0c0bf5038d3276e7f27d2e5 |
| Repository actual process | edc84a4a900fd932c7483a4fa64cc1a0317aece7ae9a6d122372e2b99620a841 |

The original compressed native has6,039,443 bytes, preserved in
four lossless original-byte parts under
[the actual run directory](../notes/low193_Fourier_mean_fixed_eta_ci/run-43607383671-1-low193-Fourier-mean-and-fixed-eta-pilot/).
The same directory contains separate readable diagnostics for every
selected row, including each newly certified target subcell.
All forty original scalar parts and all7721 original intervals
were audited; no original complete scalar or mean computation was
repeated. The original128 file hashes are unchanged.

The actual reviewed worker performed real pulls and README checks.
Its final recorded pull reached
9511825414473abecd12d99c50c8963a30ae7f75 at14:58 UTC, with no root
or topic README difference. These runner operations do not replace
or relabel the currently unavailable local terminal pull.

## Actual bounds on the selected large-source rows

All entries below are outward decimal upper bounds.
The first column bounds the old complete known output through160;
the other columns bound the complete low193 projection of the repaired
known residual, with independent mean and repair fees retained.
Thus these are valid comparisons of available upper bounds, not
lower bounds on the true residual or a claim that the high tail vanished.

| Original row | Old full160 | Cached Fourier low193 | Fresh fixed-eta whole row | Four fresh radial subcells |
|---:|---:|---:|---:|---:|
|1280|.014414608623|.014414585921|.014392436669|.000072488700|
|1283|.015039920606|.015039904686|.015016256309|.000074313090|
|1284|.015352590166|.015352577612|.015327962519|.000074990914|
|1289|.016316342714|.016316333230|.016289847645|.000078025613|
|1519|.038232449360|.038232141229|.038022220211|.000151392952|
|1524|.038362323073|.038362085259|.038133957059|.000149789959|

The actual radial \(L^2\) bound on row1524 is below
\(0.000002646609719\) with four subcells, while its cached Fourier
bound is below\(0.000678147323\).
The saved diagnostics separately record polynomial norms, complete
uniform remainders, each scalar target component and every source
component. They support refining the actual third-jet radial
enclosure, not an unsupported cancellation of its error.

The two other fresh rows also retain their actual outcomes:

| Original row | Former pilot low193 | New cached Fourier low193 | Four fresh radial subcells |
|---:|---:|---:|---:|
|3070|.000322672805|.000000402849|.000000382840|
|6375|.000058738144|.000000079398|.000000078835|

At row6375 the fresh whole-row bound is slightly better than the
four-subcell bound. All such outcomes remain saved. Subdivision is
not assumed to improve every independently valid enclosure.

## What changed mathematically

On each row the producer keeps the original Fourier coefficient
boxes and writes the old whole-row mean error as \(e_z=e_0+\epsilon\),
where \(e_0\) is a saved exact binary-rational constant. It forms
the polynomial \(R-e_0C\) directly, then pays its own remainder,
the original remainder of \(R\), the \(C\) remainder multiplied by
\(|e_0|\), and the complete \(\epsilon C\) fee.

It also retains the independently valid separate triangle bound.
A smaller norm estimate is never substituted as the uniform
remainder of a polynomial. The new fixed-eta model uses fresh
midpoint derivatives and a fresh complete third-jet enclosure on
each exact closed subcell. The old whole-parameter mean enclosure
and original repair fee remain valid on every restriction.

Complete support checks show that the known97..160 projection
comes from the full \(D\) source alone; \(F_\nu\) has degree96 and
the mean column has degree64. Their zero high support is checked
also for the complete remainder. This fact does not remove any
unknown high input or its feedback.

## The next complete consumer

This run is a selected diagnostic, not a complete new body cover
or the true response error. The continuation is to consume the
actual source-to-waist contributions, reuse every completed new
subcell and jet, refine the remaining necessary rows, and retain
old certified bounds on all others in a complete mixed cover.
The true cut source, independent mean equations and full unknown
high coupling must still enter the same Green/Schur calculation.
No parameter-Schur or nonlinear existence gate is inferred here.
