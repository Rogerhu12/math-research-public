# Run22: complete paired-halfwave bhalf parameters and exact parent recovery

Prepared at 2026-11-28 00:38:31 UTC. This is a complete, unexecuted parameter package for the independently named `fixed-fejer-paired-halfwave-bhalf-first` branch. It does not report an actual run22 input, field, accepted iterate, complete solver result, checkpoint, or certificate.

## 1. Concrete scientific choice

The complete numerical parameter parent is run19's bhalf family. Boundary fraction is exactly `1/2`, profile parameter is `1/32`, metric damping is `.01`, and restoration damping is `.01`. The current source family implements the paired-halfwave seed in R724. The change is not obtained by replacing a historical source label, moving a prior accepted field, widening the seed to `5/8`, or changing either damping.

On the two equal central material intervals, the prescribed profiles are respectively
\[
+\lambda h_\delta(t/2),\qquad -\lambda h_\delta(t/2),\qquad 0\le t\le1.
\]
All their original scalar-mean parameters and the auxiliary twelve-piece mean kernel remain the mathematical objects specified in the complete new source binding. R724 supplies the exact paired integral and endpoint identities. Those identities do not assert equality of the new whole physical field to the old full-wave field or equality of its finite geometry, Gram observations, working roots, or accepted iterates.

The planned relative support is the original pair \([1/32,15/32]\), \([17/32,31/32]\). At boundary fraction \(1/2\), each end layer has length \(S/8\). The central intervals are \([5/32,11/32]\), \([21/32,27/32]\) in \(s/S\), each of length \(3S/16\), total \(3S/8\). These are exact planned definitions. No future binary64 length carrier or mean-root word is supplied.

R724 is the complete published source: `results/R724-paired-halfwave-central-seed-and-complete-source-identity.md`, 25,314 bytes, SHA256 `fea22bde71c3780bead8b7448c5fc057e64f8e6429f97c1b3155e1d13e32f878`, blob `e2dbf61239c0092025ef8a5c0f6cac80b4e87d83`, publication `21bb485ad77530cf7623f9ef5c01b77294bc4ca3`.

The physical profile has six pieces per central interval. The auxiliary mean kernel's twelve pieces are a separate source fact. The original outer whole-cell eight-point Gauss rules and partial-cell integration rules are preserved. This package does not say that the new physical cuts have automatically subdivided those outer rules, nor that any quadrature or continuous error fee has been paid.

## 2. Complete current sources, not inherited historical claims

The current complete runtime binding was read as a whole, with its recorded byte count and SHA256. Its scientific registry has 137 roles. Comparing those complete pairs to the immediate run19 family gives exactly 120 unchanged pairs and 17 changed pairs. This count is not the older claim that a particular historical set of “original120” pairs is wholly unchanged: that inherited current claim is explicitly false in these new files.

There are 18 current runtime responsibilities in the binding, and 20 complete new source files. Driver, launcher, and reader are among the complete new files; the scientific registry and runtime inventory count different things. The complete source package was published by root at `7d34ebe278826c68a9e84c32179251220bf2fc3b`; the 67,013-byte binding itself is unchanged from the protected parent read here.

Current main source identities are:

| Role | Complete source | Bytes | SHA256 |
| --- | --- | ---: | --- |
| Driver | `fullclosed_fixed_fejer_halfwave_so3_qp.py` | 99375 | `095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec` |
| Launcher | `launch_fixed_fejer_halfwave_actions.py` | 22120 | `6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c` |
| Pure reader | `read_fixed_fejer_halfwave_so3_report.py` | 99816 | `be9bb58fa612fc25ab01458a2d6e21e0fa10c7573dad37e65effb845c6e29e92` |

The complete 17-role comparison is retained here as an exact mapping. Every corresponding full file record, not just these hashes, remains in the bound source package.

| Changed role | Complete immediate parent SHA256 | Complete new SHA256 |
| --- | --- | --- |
| root_packets | `c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4` | `8bf66692d39950c1e7c3a2b48812b686ed27a51068316ca7a786dbeaa08aee4a` |
| analytic_J3 | `223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811` | `617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247` |
| analytic_J3_binding | `3ee65e2c45d6e9cb81fac1ad0a4c439a291aa2cc3fc73d68f896107c24e2ee68` | `1a510efc3e5285bd3359229d739cecbcfc853d48dfe58b7f9c848343d6827384` |
| seed_reference | `ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a` | `cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0` |
| meridian | `552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3` | `b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6` |
| geometry | `5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135` | `494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b` |
| endpoint | `76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d` | `c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac` |
| new_moment_input | `ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3` | `53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333` |
| reference_calibration | `aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3` | `c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106` |
| frame_C1 | `c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246` | `edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b` |
| stage_matrices | `f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791` | `6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2` |
| envelope_transfer | `b8af97a4772e5d641c5daea3f2232c65fe52055154d94e45b4c88f661e9778dc` | `64a7c4380bb7150cf6738dc3102c7a33bf87dd32ed093f606a1d9b0d369a6bef` |
| adjacent_matrices | `bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564` | `ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657` |
| analytic_frame | `d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd` | `5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e` |
| closure_values | `2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0` | `3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73` |
| detached_meridian_values | `eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de` | `f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e` |
| batched_geometry_binding | `9104c29d03a589939f46ccdb08a55a3564f702acd147840cc91488b72eee2d06` | `45aedd26f59920938f6a6245dca48a06293f6cf1593124762a77063e4d0e5102` |

The original whole source files and their original paths remain historical provenance. The ready files leave their original source-constructor records intact and expressly label them as historical. They do not claim those old constructors generate the new halfwave family. The complete new 137-role registry is shared by the exact whole source binding and its `/complete_source_role_registry` pointer.

## 3. Entire steps, selectors, and numerical budgets

The science ready retains a complete 157-word argument vector. Its only changed argument word relative to run19 is the value after `--outdir`. Its script is the actual new launcher, not the old launcher relabeled with a new hash. The pure ready retains all seven argument words; only the current report and readout paths change. Its script is the actual new pure reader.

Both complete step objects retain all original keys, outputs, scopes recoverable from their exact parent, cleanup patterns, parent bundle, summary maps and fixed-reference-cache retention policy. Reversing only the declared current namespace, script, and explanatory step scope restores each original whole step value exactly. This is a text/JSON comparison of two complete parameter objects, not a numerical execution or a new solver gate.

| Item | Complete retained value |
| --- | --- |
| Current angular grid / radial layout / core layout | \(N=2048,\ J=923,\ M=160\) |
| Normal stages / block / angular block | 32 / 64 / 8 |
| Integration rule order | 8 |
| Norm | jet-sum; radial length .05; angular transition 24 |
| Torch threads | 4 |
| Metric outer directions / QP iterations | 1 / 16 |
| Restoration directions / QP iterations | 4 / 64 |
| Metric / restoration damping | .01 / .01 |
| Line trials / active rows / near-active rows | 15 / 192 / 32 |
| QP absolute / relative tolerance | 0 / 1e-6 |
| Reach ratio / reach safety factor | .03 / .992 |
| Active band | .025 |
| Marked diameter / witness lower / height floor | 4.2 / .9 / 1.01 |
| Spectral \(p\), epsilon, scale, legacy fraction | 4 / .001 / .05 / .5 |
| Metric target | 1e-9 |
| Reference panels | 128 |
| Endpoint root tolerance / iterations / backtracks / Armijo | 2e-12 / 24 / 18 / 1e-4 |
| Seed radial / profile quadrature order | 8 / 16 |
| Seed mean tolerance / iterations / backtracks / Armijo | 2e-12 / 128 / 24 / 1e-4 |
| Seed scalar iterations | 64 |
| Endpoint control radius | 2 |
| Science formal selectors | 458 |
| Pure formal selectors | 445 |
| Live fields | 48: six normal and 42 mathematical |

The entire flags, moment definition, fixed-Q input hash, two endpoint support triplets, three gamma positions, full permanent-material responsibility, original five peer CLI pairs, and all other argument words are present in the ready, not replaced by this table. The table is explanatory and not an alternate command.

The display is the complete prior display plus explicit current-source and recovery attribution. Only the two current progress-file keys change namespace. Every original live field name, selector string and ordering is preserved. Older 48-field and 18+30-field mappings remain in their original history. No additional live field, F, J, root solve, quadrature, acceptance decision or diagnostic execution is introduced.

## 4. Fresh independent mode and peer responsibilities

The complete current transfer and main source were read through the independent branch and parser interfaces. The original five `--pending-parallel-envelope-run` / `--pending-parallel-envelope-source` pairs are supported family entries and are retained word for word. That mode rejects mixing an actual old parent report, restart, previous final checkpoint, or transferred seed into the fresh independent start.

The original six external peer obligations are retained. Three additional external records identify the actually started run19, run20 and run21, with their known whole parameter records and actual start/head provenance:

- run19: `46076669320/1`, complete old bhalf numerical parent;
- run20: `46079535427/1`, the independently started `.001` restoration-damping branch;
- run21: `46084442413/1`, the independently started `5/8` boundary-width branch.

All three retain the genuine old driver SHA256 `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f`. They are not inserted into the current transfer's supported family registry, not passed as invented new CLI families, and not relabeled as new driver `095bf318...`. Their dated status observations are retained as provenance; they are not a fresh poll of their current state.

The resulting external list has nine obligations, distinct from the five supported CLI pairs. None supplies an unknown complete typed sequence, final checkpoint, accepted point, transfer priority, physical evaluation, or certificate to run22. Unknown complete history remains an obligation rather than an empty collection. Literal old material addresses and fixed current reference interpretation follow the complete independent transfer source; this parameter package does not assert a same-physical-point transfer across different seed fields.

The fresh branch can start after its own two complete necessary input stages. It does not need another independent runner's natural return. Its future run/attempt, reference, preparation, model, point, report, final checkpoint and acceptance identities are null here. The maker/reference path contract remains the original `fixed-fejer-r690-inputs` and `fixed-fejer-reference`; this package changes neither the maker nor reference numerical recipe and does not copy prior runner raw outputs.

## 5. Lossless sharing of historical metadata

The three parameter artifacts use compact UTF-8 JSON followed by one newline. Their complete value sets are retained. Compact serialization changes their bytes and whole identity, which are explicitly new.

Exactly two historical objects in each science/pure parent are represented by exact whole-parent JSON references:

1. `/complete_original_parameter_metadata`;
2. `/pre_repair_current_runtime_source_records`.

Each reference contains the complete parent path, byte count, SHA256, Git blob and fixed publication, plus the exact pointer and an explicit `truncated_or_replaced_by_summary=false` assertion. The entire parent is already published and remains unchanged. These references share history; they do not discard scientific flags, selectors, fields, or metadata. Restoring their full values requires parsing that exact whole parent and resolving the given pointer. No similar-name object or current output may substitute for it.

Every changed current top-level metadata value has a corresponding pointer in `complete_immediate_parent_metadata_recovery`. Every other original field stays inline. Thus the parent and the current views are distinct, and every original field can be recovered exactly. Old source/pin-only descriptions remain only in their explicit historical location; the current scope states the physical mechanism change and the 17 changed source roles.

No raw scientific array, checkpoint, mesh, mean batch or root packet has been extracted into this metadata. New raw inputs and all eventual reports remain runner scratch under the established contract.

## 6. Complete parameter text constructor

The new MJS reads the exact whole current runtime binding and the three exact whole run19 parents. It reconstructs the full display, science and pure objects, performs only text/JSON preservation checks, and writes complete artifacts at their repository-relative paths under the chosen output directory. All expected output byte counts and SHA256 identities are embedded. It can reproduce the exact current three files without scientific modules, AST, fixtures, numerical calls, network access, ref updates or queue changes.

Its optional source-reproduction command is:

```sh
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_paired_halfwave_bhalf_parameters.mjs --repo <complete-repository> --output-directory <generated-tree>
```

This command is archival construction capability, not an extra step before the actual solver. It is not added to the public scientific queue. The present delivery used complete JSON/text construction and exact whole-step comparisons; it does not claim an independent local execution of this MJS, any Python AST check or any scientific result.

The four exact complete input files are:

- `topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json`: 67013 bytes; SHA256 `6dd246a030ffaf9e58e750c135e26424b12668b182f0e6a59726c2af006c1638`; complete Git blob `4f20af6e3663bdf69aca7193bc29624dc706411c`.
- `topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json`: 90652 bytes; SHA256 `242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67`; complete Git blob `9c4c28ef3c5b189e094c65f51038fafeef48bc48`; fixed publication `543cfdf281c9bcd0f9b13197721b003a275c5967`.
- `topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json`: 80254 bytes; SHA256 `8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7`; complete Git blob `202b6ca81c72c009c34c04094ef234db2e337328`; fixed publication `543cfdf281c9bcd0f9b13197721b003a275c5967`.
- `topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json`: 25057 bytes; SHA256 `cc564e5c273367242aae226913a0dd82ae5b88b3e166fbcbb8da68d6c04edb2d`; complete Git blob `fac08bdbafbefd0e599687e2b7f0a5c6e71382e7`; fixed publication `543cfdf281c9bcd0f9b13197721b003a275c5967`.

## 7. Final protected deliverables and boundaries

- `topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-science-complete-ready.json`: 94317 bytes; SHA256 `f60ce7bc9c0a6392a84fe73f5a9fcdf347ad294add8066c57233003389a0818d`; complete Git blob `a8348cd238af32a441ebd5c63bc913cb6157891b`.
- `topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-pure-complete-ready.json`: 84075 bytes; SHA256 `1a7649f702c005eadd7b0c9d8b4a064f0ed70be37dabc449bbc1e9afcf3b8cc9`; complete Git blob `76e73edb425a30cda39c94275ee193914a319fb4`.
- `topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-complete-display-correspondence.json`: 30196 bytes; SHA256 `472e385c78f39a2b3bb582a162b642e2e349696708aa8b3d130e0a1fa2c8403c`; complete Git blob `4d15d836b40ba5547542e7468dfe0aff52d07934`.
- `topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_paired_halfwave_bhalf_parameters.mjs`: 28509 bytes; SHA256 `55eb55688a990ab66c5b4d2d661b140bf36f8ec2921229c43a618e05e6427232`; complete Git blob `94864fd0705d5debbd2bfb7aba06266f9c59acae`.

The delivery manifest adds this complete note and the full six-file inventory, exact source/parameter links, current/null execution scope, and declared changes. Root alone publishes and schedules them. Neither this source work nor its prepared selector maps establish that a run22 field has been produced.

The decisive next scientific action is the original full-budget independent solve with the paired-halfwave family. Its complete natural report and fixed checkpoint, if returned, determine what can be read or continued. The halfwave mechanism may reduce a particular central derivative while changing integrated displacement, diameter and Gram quantities. No prediction of acceptance, total runtime, curvature feasibility, whole-surface reach, continuous isometry, R716 moments or nontrivial amplitude is made by these parameters.
