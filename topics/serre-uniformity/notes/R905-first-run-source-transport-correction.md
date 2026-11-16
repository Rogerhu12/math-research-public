# R905 first-run source transport correction

The actual run 43892405424 / job 133387056768 at commit 29e088e272785f0e11357e6039c08302d9443117 stopped before importing the mathematical core. The wrapper failed in Handle.__init__ when the frozen R824 Archive reader checked the supplied artifact name. No mathematical stage or complete input carrier was created.

Only prepared_transports.R827[0].archive.artifact_name changes:

- Requested: serre-required-original-source-intake-43854607823-1
- Actual API value: serre-R880-six-Dstar-source-intake-43854607823-1

The immutable transport identity is unchanged: run 43854607823, source ed3ed6bf901aa66b3b8668d24b2173e608d82b72, artifact 14221081225, 12926425 bytes, platform ZIP SHA256 a333e11c9c99617d6c8f66c0e61cd47ae36009f57afacb14fdada74c67043b99. The API reports expiry 2026-11-17T11:06:13Z. The bound inner R827 package remains 12876078 bytes / f89b94019e6a8e567444e5b6326d449c9d21ea1c2878e3f1efa5a18b2d3e9766.

Core d0810c29, linear algebra helper ced5b652, wrapper ff7ff5f1, method a2600cfb, workflow 7d3087a5 are byte-identical. Resume remains null because no mathematical output exists. This fixes the transport identity without relaxing the source-name check. No local mathematics ran.

The failed output artifact is 14237372355, 1553 bytes, ZIP SHA256 7e979ba277ec89245693d58de69585f19f55c8d282978ca04b1a2852741d81dd; full manifest 301 bytes / 274f0931a7e1ca018d8eea0ef31e1ec6c6779784a80de528a2920fec7cc943c5.
