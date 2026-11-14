# Actual58: the saved final direction at the largest collocation row

- Classification: original-byte readback and source-level algebra; no new numerical solve.
- Author: amplitude agent.
- Date: 2026-11-14 UTC.

## Original data located

The [actual58 conclusion](2026-11-14-actual-request58-quarter-step-existing-domain-limit.md) identifies interval 461, radial mode 1, physical component 1, original zero-based residual row 155819 as the complete unweighted collocation maximum at the base and accepted warm. The source order is interval-major physical rows followed by the right boundary rows.

The original artifact is `14130714261` from run `43638348140`, source `ba8bc4f4acd547fd5219826da4f6e35f859bca56`. Its complete ZIP has 465122089 bytes and SHA `288f67d35684d7d4cb73ff869dd90bd29aa9b559b0a1ecf295524eac0b374570`. No new download or scientific execution was needed for this readback.

Within `seventeen-condensed-warm/`, the original `condensed-QP-result.json.gz` has SHA `cc316175c891dfb78bcab2d4b9814d54c27754362f92cd481841e9e35ef35adc`. It preserves both the original weighted residual and the final selected complete-H direction's already computed original action:

| Result field | Original NPZ under `condensed-arrays/` | Stored row 155819 value | Original little-endian bytes |
|---|---|---:|---|
| `original_b` | `array-0001-part-0000.npz` | `-1.4154122374775011` | `522f654d87a5f6bf` |
| `final_selected_evidence.action` | `array-0033-part-0000.npz` | `0.00026246452261009833` | `060d7d8a6c33313f` |

Each NPZ contains `actual.npy`, C-order `<f8`, shape `[236036]`. The original NPZ SHA values are respectively `719fcf5fcf8338881bc4267896342bc1fc3097768e9557ea3544d81585ef79ea` and `6a7129cd472f197d78d3c0321dd403c12a5db206c00c238ff05f0e01b1e24385`. Their complete saved array identities are `31ea0218a53a759b1b052aeb1eb84b3fa5abe9e47d0bf81b72a87779f9fa9e1b` and `fd7bb6ff4ebfa75a82ecaa966564df008722f621a3058afd278e2dd3ed148b03`.

The [single-row byte receipt](2026-11-14-actual58-stored-row155819-b-and-Az.json) is 1730 bytes, SHA `8daefd256b22e79de0e61cf8e773353facd76e0df10bff9f93166c1239e2a89a`. It records original descriptors, NPZ/member identities and the two decoded binary64 entries. No product, division, norm, new maximum or matrix action was computed locally.

## Exact source meaning of the saved action

The frozen seventeen-query entry's `evidence()` computes `action = np.asarray(A @ z)` after selecting the final complete-H candidate and saves it as `final_selected_evidence.action`. It is not the raw LSMR vector or the unrepaired local candidate. The comparison report binds the same final action identity.

The original `CompleteLinearization.operator()` defines $A=WJS^{-1}$, where $W$ is the original residual weight vector, $J$ the complete constrained residual Jacobian and $S$ the chart scale. The original warm engine sets $b=WR(q)$ and evaluates actual trials at $q+\alpha S^{-1}z$. Write $a=Az$ and let $r=155819$. The corresponding linear predictions are therefore

$$
 b_r+\alpha a_r,
 \qquad
 R_r(q)+\alpha\frac{a_r}{W_r}.
$$

The contribution of this row to the original unregularized model's predicted merit reduction is

$$
 -\alpha b_r a_r-\frac{\alpha^2}{2}a_r^2.
$$

These are algebraic formulas, not newly evaluated scalar diagnostics. The global damping penalty acts on the scaled direction and is not assigned to this residual row by an invented per-row decomposition.

## Observed weight and interpretation limits

The original read-only observer records $W_r=199.07511842631416$ from the one actual base `weights()` call, whose full array identity is `9203028f7011aec415017449ec721b274c2006268693132202f5bf5f992c08bf`. It is frozen across all actual58 trials. At the base the signed unweighted row is `-0.007109940451957601`; after the accepted alpha 1/4 step it is `-0.00710961172228531`. These values come from the original observer, not a local reconstruction.

The final original model itself supplies a small positive change to this negative row. Thus the observed slow improvement is not explained by an absent row or zero weight. The row lies outside the domain operator's local node support, but remains in the complete objective and R270 exterior response. This evidence does not isolate damping as the unique cause, establish a new scientific acceptance gate, or justify changing the equations, weights or lambda. No additional scientific run is needed merely to locate these two saved scalars.
