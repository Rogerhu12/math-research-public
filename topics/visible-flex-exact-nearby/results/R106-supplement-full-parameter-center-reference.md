# R106 supplement: an accurate full-parameter seven-field reference

The
[moving-root parameter theorem](R106-supplement-moving-root-parameter-fields.md)
has now been applied to an actually completed center Fourier/Taylor reference.
The represented family remains the full original
\(|p-p_5|\le10^{-9}\), with its actual moving root.
The tiny auxiliary interval used to calculate a center reference does not
replace or shrink that family.

## 1. Executed center coefficients and actual full-family transfer

The center coefficient run uses degree \(80\), radial precision \(92\),
\(2048\) angular evaluation nodes, and every retained Fourier mode
\(-650,\ldots,650\). Its auxiliary half-width is \(10^{-24}\), so in
particular it contains the exact center \(p_5\).
All center interval errors, finite DFT errors, aliases, unretained Fourier
modes and radial tails are paid on

\[
 |\rho|\le7/25000,\qquad |\Im\theta|\le1/400.
\]

The finite coefficients are exact dyadics and remain unchanged by the
transfer. For each field the new complete error is exactly the proved
mean-value estimate

\[
 e_f=e_{f,\rm center}+10^{-9}
      \sup_{p,\rho,\theta}|\partial_p f|_{\rho,\theta}.
\]

The derivative is the actual one at fixed moving-root \(\rho\) and physical
angle, on the entire bidisk and original parameter interval.
The consumer checks the center coefficient shards and outer geometry,
the full \(1024\)-cell parameter derivative cover, every required source
hash, both object identities, and inclusion of the error domain.

The complete full-family errors are:

| Field | Outward full-parameter sup error |
| --- | ---: |
| \(G\) | \(3.574\,10^{-13}\) |
| \(q\) | \(4.275\,10^{-10}\) |
| \(k_*\) | \(1.161\,10^{-8}\) |
| \(S_{\rm reg}\) | \(8.365\,10^{-12}\) |
| \(L_\theta\) | \(1.091\,10^{-11}\) |
| \(U_0\) | \(2.329\,10^{-12}\) |
| \(U_1\) | \(8.858\,10^{-10}\) |

These errors bound the complete true functions relative to the complete
finite center polynomials. They are not individual mode errors and do not
omit the infinite complements.

The center report is

    data/R106/root_seven_center_degree80/report.json

SHA256:

    7307c9581b631353680f01eb733b6f8662b566b2074d7e8918223b6080fbc997

The full-parameter transfer report is

    notes/2026-11-13-R106-seven-field-full-parameter-transfer.json

SHA256:

    7c411f5807fc6a97a466fe6800f75c71cdac5c1d5b24e3d54fa289e5ddd37497

The source
[parameter transfer](../scripts/fourfold_subprincipal_root_parameter_transfer.py)
also supplies a loader that rechecks the full input chain and recomputes
the transfer error when consuming the report.

## 2. Complete regularized source and boundary errors

Use the unchanged original physical cut
\(r_c=268136140016943/1125899906842624\),
the full-family root interval from the actual derivative certificate, and
\(c(p)=\sqrt{t(p)-r_c}\).
No center root radius is substituted for the true cut radius.
The full-family errors above are supplied to the proved R106 regularized
source formula, on the original source strip \(1/800\), with the two equal
angular Cauchy losses from the larger strip \(1/400\).

The complete finite input norms are computed from all center coefficients.
Actual full-family input moduli are bounded both by the true derivative-domain
geometry and by finite norm plus complete error; the smaller valid bound is
used. The source-error theorem then gives:

| True field minus exact finite center expression | Outward sup error |
| --- | ---: |
| regularized source \(H_\sigma\) | \(0.000694547\) |
| transport boundary \(B_{-3}/c^3+B_{-1}/c\) | \(7.646\,10^{-7}\) |
| root endpoint \(Z_\sigma\) | \(2.726\,10^{-12}\) |

For example, writing \(e_{B_1}\) for the paid transport coefficient error,
the complete transport boundary error is

\[
 E_B=\frac{e_G}{3c_{\min}^3}+\frac{e_{B_1}}{c_{\min}}.
\]

The source error is the complete analytic source error of the
transport-counterterm theorem plus
\(e_{S_{\rm reg}}/(1/400-1/800)\).
The complete full cut-field error separately adds the \(U_0,U_1,L_\theta\)
fees. All these directed values are retained in the report.

On the same actual ray and with the same actual endpoints, the field-only
error in one reduced root contribution, before multiplying by the complete
global \(J\), is

\[
 E_B+c_{\max}E_H+E_Z
 <1.161683\,10^{-5}.                                        \tag{1}
\]

This is the actual full-family field approximation error. A later exact
finite coefficient expression can be formed from the center coefficients
with every product frequency retained. If a later producer chooses new
rounded output coefficients, that new choice fee must also be paid.
Likewise (1) does not pay a true-minus-reference characteristic error,
reference Jacobian error, endpoint-position error or continuous quadrature.
Those remain separate obligations of the phase integration.

The source and report are
[transferred source error](../scripts/fourfold_subprincipal_transferred_source_error.py)
and

    notes/2026-11-13-R106-full-parameter-regularized-source-errors.json

SHA256:

    8a02c538abda9c22767289035b367d9fe4b8e83671149f1a9aac3ac437e42f95

## 3. Exact reproduction

Run from the topic directory:

~~~bash
python3 scripts/fourfold_subprincipal_root_fourier_v2.py \
  --domain-report notes/2026-11-13-R106-seven-field-boundary-v2-native-2048.json.gz \
  --include-root-aux --half-width 1/1000000000000000000000000 \
  --degree 80 --precision 92 --angles 2048 --keep 650 \
  --working-radius 7/25000 --working-strip 1/400 \
  --out-dir data/R106/root_seven_center_degree80

python3 scripts/fourfold_subprincipal_root_parameter_transfer.py \
  data/R106/root_seven_center_degree80/report.json \
  notes/2026-11-13-R106-seven-field-moving-parameter-bidisk.json.gz \
  --out notes/2026-11-13-R106-seven-field-full-parameter-transfer.json

python3 scripts/fourfold_subprincipal_transferred_source_error.py \
  notes/2026-11-13-R106-seven-field-full-parameter-transfer.json \
  --out notes/2026-11-13-R106-full-parameter-regularized-source-errors.json
~~~

The completed center report records every shard hash. Downstream loaders use
the compressed center coefficient shards; the larger node intermediates can
be reproduced from the exact first command and are not needed by these
consumers. The new outputs preserve all preceding whole-parameter reports.
