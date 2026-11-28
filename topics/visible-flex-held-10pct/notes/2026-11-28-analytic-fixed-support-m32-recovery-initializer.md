# Explicit unaccepted recovery of the interrupted fixed-g M32 state

This follows the actual M32 exit137 record. That process returned no full nodal solution and no metric audit. Its saved 1272 interior midpoint columns remain only an unaccepted state; neither this note nor the new initializer promotes them to a returned solution.

The new independent helper reconstructs the actual fixed-support model with all 97 state components and all 32 original parameters. At each saved midpoint it evaluates the original complete RHS. These values and derivatives define a full-component cubic Hermite initial guess. The physical target, literal chart, lambda .002, delta .06413464112662924, gauge q .06, warp_reference_q .06 (actual warp_e .48), finite mean1168, support family and q branch [.055,.065] are unchanged.

The old nodal coordinates are not available. Recurrence from the literal rounded midpoint coordinates gives an approximate 1273-node grid, with an exact final endpoint discrepancy of 93507/73786976294838206464. The record explicitly sets historical_node_grid_recovered_exactly=false. All 1032 knots of the genuine accepted M24 source are then retained literally; inferred nodes within 2e-12 of those existing knots are omitted. This leaves 1273 initial nodes and retains every accepted source break. It does not discard a genuine returned M32 grid, because no such grid was saved.

The original inlet correction is applied to the initial guess only. Its largest component is 6.495448623411448e-11. The original parameter vector and scale vector are preserved bitwise. The actual initial support amplitude is .060000129165352675. Original node and collocation-midpoint domain checks return successfully. The complete initial collocation maximum is 4.612992233002975e-9, but the boundary maximum is 6.080240367105888e-6. The original boundary gate therefore has not passed. The nonlinear solver and its original off-midpoint RMS and metric gates remain necessary.

The helper completed in 83.151358916 seconds with maximum RSS391168 KiB. Its complete provenance, immutable initialization hash, exact source identity and unaccepted flags appear in the adjacent JSON. These are initialization facts only.

## Independent recovery runtime

The resource/recovery entry is a new file, fixed_support_literal_driver_v2.py. The old successful/interrupted driver has been restored byte-for-byte to SHA 6ca29978b422201e9312b30205de91d4abf3f9ac5c0ca78c627470c7df41a06e. The v2 file has its own SHA 756f55e7d4dc691cad0597c1ecee18a26d292d8676d46aca3342c4f765ff077e. Existing hash-bound run records are not silently rebound to the new source.

The new runtime accepts this explicitly unaccepted initializer through the old entry's declared unaccepted-raw mechanism, while checking the complete frozen physical problem and input hashes. It releases the obsolete factor before building a new full Jacobian and avoids a solve-closure reference cycle. It saves a separate atomic, complete nodal checkpoint immediately before full-J construction; subsequent midpoint calls cannot overwrite that file. Every such checkpoint remains marked unaccepted. Original complete equations, physical boundary tolerances, RMS checks and metric checks are retained.

The actual preparation through v2 preserved all 1273 input nodes and all fixed-profile/chart/gauge/mean semantics. Its initial nodal RHS agrees with the initializer's saved cubic derivative to 8.881784197001252e-16. The process then reached the explicit resource gate before invoking the BVP. This note records that preparation state; a later original solver return must be recorded separately.
