# R133 supplement: actual fixed-eta physical-cap coefficient pilot

2026-11-14. Public run [43619535345](https://github.com/Rogerhu12/math-research-public/actions/runs/43619535345).

**Proved.** At affine parameter offset zero, hence the fixed physical $\eta_0$, 336 new coefficient domains yield a complete same-$w_0$ physical-cap error upper bound below $1.508953388222\,10^{-6}$. The full 1,977-parent cover consists of 16 refined parents and 1,961 unchanged complete parents. Every parent uses one consistent eight-channel coefficient representation, and all six original boundary/jump errors remain.

## 1. Actual computation and reuse

The original 257-output, 97-input Hermite arrays and all four original direct one-column ranges were received by their exact native/process identities. Their mathematical cells were not rerun. The new domains use parameter half-width zero and, on each of the 16 selected parents, radial subdivisions $1,4,16$. These are 336 new smaller parameter/radial domains.

The actual public child returned zero, passed six scientific gates, and completed in 443.609966474 mathematical seconds, with recorded child wall time 450.010949063 seconds. All 336 complete coefficient rows and their Hermite contractions remain in the native.

The selected original parent indices are
$861,862,873,875,884,895,896,906,908,920,929,931,941,942,952,1021$.
The exact continuous centre and direction remain, respectively,
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`
and
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`.
The physical even input includes its independent mean; the same fixed direction hash is
`f77f64367593908c9dd3ba8ac318090275a3b59aa43542620858aadce7b0cbd0`.

## 2. Complete bounds

The independently reconstructed old direct, coupled eight-channel baseline gives
$$
 \varepsilon_{\rm direct}<2.418183101946\,10^{-6}.
$$
Choosing one entire valid coefficient representation on each parent, then summing all 1,977 parents and all fourteen physical contributions, gives
$$
 \varepsilon_{\rm new}<1.508953388222\,10^{-6}.
$$
Different finite-polynomial/remainder decompositions are never mixed component by component. The old published mixed bound is recorded only for comparison.

The new principal fee components are:

| Already Green-weighted contribution | Outward upper bound |
|---|---:|
| Divergence $B$ remainder | $1.382810857749\,10^{-6}$ |
| Ordinary $C$ remainder | $7.483366438\,10^{-8}$ |
| Divergence $C$ remainder | $2.407911732\,10^{-8}$ |
| Finite nonmean $B$ residual | $1.225422324\,10^{-8}$ |
| Finite nonmean $C$ residual | $1.411411480\,10^{-8}$ |
| Finite even mean residual | $3.570628365\,10^{-10}$ |

Every remaining contribution, including the genuine inlet, outer regular row, both means and both jump columns, is retained in the full small summary. No physical-to-moving Hessian fee is included in this physical-only result.

## 3. What the actual diagnostic resolves

For representative parent 861, the divergence-$B$ square accumulator is bounded by the following values. These are source square accumulators, not whole-cap error bounds.

| Domain choice | Divergence-$B$ square accumulator |
|---|---:|
| Original whole parameter cell | $9.820673422\,10^{-16}$ |
| Fixed $\eta_0$, unsplit parent | $9.818867272\,10^{-16}$ |
| Four radial subcells, summed | $4.497939160\,10^{-20}$ |
| Sixteen radial subcells, summed | $3.211635756\,10^{-24}$ |

The parameter restriction alone has little effect here. Actual radial refinement pays the broad third-order target/coefficient remainder much more tightly. Parents 895 and 1021 show the same mechanism. The finite residual component remains present and can then become the limiting component.

This justifies extending the four-subcell calculation to the other parents. That extension must reuse the already completed $16\times4$ quarter-cell results byte for byte; it is not yet part of this pilot conclusion.

## 4. Evidence and scope

Evidence directory:
`notes/fixed_eta_physical_cap_pilot_ci/run-43619535345-1-fixed-eta0-physical-cap-pilot/`.

| Evidence | SHA256 |
|---|---|
| Complete native, 2,213,670 bytes | b5a157d4005eb4aad1c536512c4ea5dcb431e90d09c4b05f324db5cf09203138 |
| Read repository process, 16,236 bytes | 02fa971c029489d360db9f5fb78ac8d1da8594cb0d8ad6d68f3b0a7bef2ccd2a |
| Small summary, 34,252 bytes | 3bb0abaf36152e39bd5d6f113b2f6c7001c66660f1af7bcb68b11ba26b2e6dbe |
| Scientific source | 3cbadc70a5fc2f1fb9567d9e982995c6e194952913914d234e728a3aee18b75a |
| Worker | 953940428d8c2ac6a1bf9a1874d9e806d8920f2787f00ba9042ce449db208267 |
| Immutable 156-file manifest | 0e0c95425c53d9fa0d3287f656b9ac478483ff03b159a5412048b39e04f5ffad |

The complete native is `native/fixed-eta0-refined-physical-cap-coefficient-pilot.json.gz`. The summary is `evidence/fixed-eta0-physical-cap-pilot-summary.json`; each selected parent also has its own small diagnostic. Binary data stayed in the public Actions channel.

The process records real pull/README checks with no rule differences. The last read commit is `90e615fd55d98fcad7e96ea7a0657ede109dd09b`; the explicit rule-review commit remains `ee26c0a65a2e63c15f2ccfba6714181584416542`.

The result concerns one complete known direction at the fixed centre. It neither improves the unknown-input cap error operator nor closes the finite response, infinite high feedback, full parameter Schur complement, or nonlinear problem.
