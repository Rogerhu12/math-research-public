# J1845 exact-affine notation correction

This source-only note corrects the notation in §3 of `2026-11-27-actual09-complete-exact-affine-radial-J1845-entry.md` (whole SHA256 `134aa876eced56f84b96c4b83e28a85b5b15442c498c3926cb53e39ff09c969f`, 26886 bytes, Git blob `f443f32b0ddd76c8cab3d8c0b48cb55822ba62ca`).

The affine pair is ordered as **coefficient of S, constant term**. The displayed formula must read

$$X_i=A_i S+B_i.$$

The original displayed `X_i=A_i+B_i S` reverses these two symbols. The actual complete implementations already use `alpha*S+beta`; the last endpoint has pair `(1,0)`. All midpoint identities, exact query mappings, original-node inclusion, and the complete three-channel quintic injection continue to use that same existing convention. No runtime source, numerical parameter, mathematical target, report, or computed result changes. This correction is a textual inspection, with no local mathematical or scientific execution.
