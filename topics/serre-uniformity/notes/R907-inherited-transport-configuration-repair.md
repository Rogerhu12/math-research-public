# R907: repair of inherited transport metadata after the actual pre-core failure

Date: 2026-11-20. Status: IO/schema correction; no new mathematics.

The original run [43924786163](https://github.com/Rogerhu12/math-research-public/actions/runs/43924786163), job133543328511, stopped in `Registry.carry` before importing the mathematical core. It passed a verified carrier source identity together with an older transport descriptor to the strict `same_source` check. That descriptor did not contain `configuration_sha256`. The old R899 request indeed has unsealed R845 and R872 routes; the existing R903 request contains the same R872 source with its actual configuration identity.

The local correction does not change the frozen common IO module or any mathematical source identity. After the existing parent inventory, parent tag, manifest and carried byte checks, `seal_inherited_transport` first requires equality of all five immutable fields (result/run/source commit/core SHA/manifest SHA). It then copies the already verified inventory's exact configuration SHA only when the transport descriptor lacks it. An existing unequal configuration is rejected. The original strict check is applied to the resulting descriptor. Direct source checks remain unchanged.

The actual old R872 descriptor from the R899 request and the matching sealed descriptor from the R903 request exercise the original missing-field case. In an isolated AST extraction containing only the two standard-library schema functions, that case succeeds; changes to either source commit or configuration SHA are rejected. No arithmetic core is imported or executed.

The wrapper's new SHA is bound in the original request. Its `producer_inputs_pending` is now true for a separate observed reason: the four pinned direct artifact IDs 14254777999, 14251161202, 14234003349 and 14218009053 all return HTTP404 on 2026-11-20. Their original recorded expiry dates were 2026-11-17. Changing a schema does not recover their bytes, and metadata cannot replace the complete original arrays. The workflow therefore leaves the core inactive until genuine source transport is restored, while the all-prime proof work continues.

The core, helper, method, proof hashes, requested j1 direction, original target algebra, old completed mathematics and source mathematical identities are unchanged. No successful pencil, norm, endpoint, or height is claimed by this repair.
