# Retention 41: thirteen historical condensed optimization-intent gzip outputs

## 1. Exact scope and status

This is the complete source and recovery record for removing thirteen generated `optimization-intent.json.gz` files from the current topic tree. Their combined compressed size is **2,596,023 bytes**. Every selected path, byte count and Git blob was independently read from directory metadata at fixed commit `44f0f866e48e97063605a71c8b38647c681dddfe`. No selected gzip body was fetched, decompressed, parsed or replaced.

This note and the two complete ledgers preserve the original scientific sources, every original request and parameter field, the actual parent warm/status pairs, the resulting warm/status pairs, source-specific publication behavior, and the actual scientific conclusions. They do not delete any of those inputs or results. Root performs the final ordinary repository commit; this source-only review has neither deleted a tracked file nor changed a ref.

The machine-readable record is split by complete run records, not by truncating any configuration:

- [Part A](../computations/legacy-condensed-gzip-intents-retention-41-part-a.json): the six complete request 64, 66, 67, 68, 70 and 72 records plus the shared complete source/input/recovery contract. 95076 bytes, SHA256 `85e1ae3cf0c13cfd49bf12486e13690092b2fc189a9f21fc76b398550f8507ee`, Git blob `ae8da201a5e41ae93ea22337edff72ea369e5146`.
- [Part B](../computations/legacy-condensed-gzip-intents-retention-41-part-b.json): the seven complete request 74, 76, 79, 84, 86, 89 and 94 records. 84536 bytes, SHA256 `b8656f0c40990afc8968349c89c44eacc29004f630a293b6fde2bebdff787710`, Git blob `101ddd791766be2be44d14d6a5b2e38b3aa01a21`. It pins Part A by its full path, size, SHA256 and Git blob.

Each ledger is below 100,000 bytes. Together their `delete_entries` contain precisely the thirteen paths in §2. A reader must retain both complete ledgers and the existing complete files they reference. The shared contract is not a replacement for a numerical manifest or for any original raw payload.

## 2. The only thirteen removal candidates

All paths are relative to `topics/visible-flex-larger-amplitude/` and have the exact form

`notes/public-actions-RUN-1-condensedqp/OUTPUT-DIRECTORY/optimization-intent.json.gz`.

The two `lambda27` directory names below are literal. No other file in any of these directories is included.

| Request | Actual run / attempt | Output directory | Compressed bytes | Exact Git blob |
| --- | --- | --- | --- | --- |
| 64 | 43648987661/1 | `nineteen-condensed-warm` | 144782 | `a51552c184051ec76178afb92cc40a2249ba759a` |
| 66 | 43651436427/1 | `twenty-condensed-warm` | 156164 | `890cfe27e291ad329e169d3c2afc3e1bcae7caf3` |
| 67 | 43652955632/1 | `twenty-lambda27-condensed-warm` | 157594 | `4d3fb8dfb9022f6c3e07b41803bacd289a5f6765` |
| 68 | 43653811809/1 | `twenty-one-condensed-warm` | 167568 | `163642881f425f6a5f6ba79b6ccefe224d799269` |
| 70 | 43656059206/1 | `twenty-one-lambda27-condensed-warm` | 169119 | `8c8d56fd03b3ce246956c93e7bf77987ec079eb0` |
| 72 | 43656584956/1 | `twenty-two-condensed-warm` | 179601 | `eb5233c835a2eb83569e318103a758bef58a7e3b` |
| 74 | 43659610548/1 | `twenty-three-condensed-warm` | 191691 | `d5a7156800d93e92a2daf8819a25101aa7b61097` |
| 76 | 43661532089/1 | `twenty-four-condensed-warm` | 204185 | `59d371236c4cb331cace44d5da422b58093d7619` |
| 79 | 43663293492/1 | `twenty-four-condensed-warm` | 216641 | `1eb89f23feb5b61e8a2334088e66489b41ecb646` |
| 84 | 43666177645/1 | `twenty-five-condensed-warm` | 229574 | `2225d8fe16f1c24556bb48c9cd742707a5ea781b` |
| 86 | 43668743515/1 | `twenty-five-condensed-warm` | 245056 | `e8c98964a080f12f57618e3bed852e3795f0b884` |
| 89 | 43671882961/1 | `twenty-six-condensed-warm` | 260060 | `15caf63607d90c33258270c5b3bbbd0e455047a6` |
| 94 | 43674854261/1 | `twenty-eight-condensed-warm` | 273988 | `6ad7e94d709f3f3011f18dd89d5d53e08c63e872` |

The whole SHA256 of each candidate gzip is **null** in the ledgers because no reliable small record supplying that particular whole hash was used. Its fixed historical Git blob and byte count are known. No hash has been fabricated, inferred from a different JSON serialization, or confused with the uncompressed identity. No new Actions run, scan or scientific replay is proposed to fill a missing hash.

The candidate recovery commit is `44f0f866e48e97063605a71c8b38647c681dddfe`. This is an immutable path-to-object recovery point for the thirteen candidates. It is not asserted to contain all of their historical scientific warm/status payloads; those have separate per-run recovery commits in §5 and the ledgers.

## 3. Why these are generated provenance outputs

The original complete engine is `computations/geometry_20261114_full_angle_projection_warm.py`, 36,439 bytes, SHA256 `7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152`, Git blob `d1fe5e5f595c319dfde4752295709fa7acc16fb2`. The previously completed source audit identified its actual write and read sites:

```python
write(args.out/"optimization-intent.json", identity)
resume_sha256=sha(args.resume), resume_producer=current["optimization_warm"]
optimization_warm=dict(identity, iteration=0, actual_fixed_weight_merit=merit1, ...)
```

The first line writes a newly constructed identity in the new output directory. The parent identity comes from the actual resumed warm object; the accepted output warm and the driver-status identity retain the live run's provenance. The standalone intent is consequently an audit output of that execution. This classification follows actual dataflow, not its filename or an assumption that it is small enough to ignore.

Retention 34/35/36 already closed the underlying engine, original source recovery, and warm/status reader scope. This review reuses those findings. To cover this particular later family, the nine ordinary 19/20/21/22/23/24/25/26/28-query complete small producer sources were fetched and checked at their identity annotation/write and parent warm/status read sites. Their `optimization-intent.json` uses occur in the two writer callbacks: the engine writer annotates the live intent; the outer writer annotates the outgoing intent, status identity or warm provenance before forwarding to the underlying writer. The original parent reads remain the complete `--resume` and `--parent-status` inputs with their full byte identities. No standalone old intent is opened by those reviewed parent-input paths.

The two lambda-27 adapters were also read as complete small pinned files:

- `geometry_20261114_twenty_query_lambda27_condensed_warm.py`: 14,779 bytes, SHA256 `7de5e7d01efa9464e9c0d671c94d3b70a6e093dc1b3fd844944456ebb46fbbb5`, Git blob `a0cb45d422bd20b7a67a05be361b1bd9592acc51`.
- `geometry_20261114_twenty_one_query_lambda27_condensed_warm.py`: 15,297 bytes, SHA256 `a8dd293b4b10ab45a2e69dd1e3e37a2032e4af3eb4d5f21eefa556277cb0d64c`, Git blob `918030085303e5ce45fb7aa32b5c16f1997fc973`.

They adapt the pinned complete functions and engine damping/current metadata, preserving the original write/read mechanism and their fixed actual parent pairs. This was a provenance-interface check. It is not described as a newly repeated mathematical audit of every full solver body.

The conclusion is bounded: the reviewed original warm continuation/response readers and the stated current warm recipe do not require these standalone intents as numerical inputs. It is not a claim that no historical diagnostic or arbitrary future program could request one. Such a reader can restore its complete original object as described in §9.

## 4. Complete original parameters and source identities remain

The original request wrappers are retained at

`notes/public-actions-RUN-1-condensedqp/followup-request-identity.json`.

Every field, source pin and nested original request remains in those whole files. The following table provides the whole wrapper hash and the retained complete parameter-context file. The ledgers additionally preserve each wrapper's bytes/Git blob, the original raw request SHA, its original source commit, and the complete original condensed-manifest recovery record. No reduced list of numeric options substitutes for the original parameter context.

| Request | Whole request-wrapper SHA256 | Complete retained parameter-context file | Parameter-context SHA256 |
| --- | --- | --- | --- |
| 64 | `061c30961af2cb90b6bd8c68c99eab30badd66e503273f1ae87aa02fe1e06d32` | `computations/legacy-condensed-source-parameters-run43648987661-retention30.json` | `c3fbeced265f400cd636e38cdbe86182d16da4558a7988bd54ec87b76336e18e` |
| 66 | `6b16ba14a06aa972129f5568c07b883525d2858315e1479a347fb66ef1cc338e` | `computations/legacy-condensed-source-parameters-run43651436427-retention30.json` | `ebebd65ced8fbcab256f80db4ff19964b32dd4a8870449e1adb9f4eb290d7a04` |
| 67 | `d1a3ece70ae231e6cea481daa8f912f05a86b5eff2f488c1a87041acd2e4be1e` | `computations/legacy-condensed-source-parameters-run43652955632-retention30.json` | `fbaa14e44417580634744766e8ebd19cf4c54c98ab7c9524f7b4fb70b50bc85b` |
| 68 | `d66e762d349a9f38097cfdb748bdc1b8adf2b274d533ab206ee819d681ed1bd2` | `computations/legacy-condensed-source-parameters-run43653811809-retention30.json` | `6b115f712f1b388b3b697aa9c96f110824dc0b76de6721f823626a6388368834` |
| 70 | `09342593c67b6104e771e9cd6e4c7b72bd24b15698b8d355a3088f3c36247727` | `computations/legacy-condensed-source-parameters-run43656059206-retention30.json` | `4d1ae572cb9eecdc9bde6f148bf6282a2fd23a6cfe1cce3f3a4995d99e84eb7c` |
| 72 | `9954937addf1a71cb144a9f4f249e64df26958ea067456f07b4580a395f1e066` | `computations/legacy-condensed-source-parameters-run43656584956-retention30.json` | `08c48a2805b76fff34b5d5efbe38ee2e4c400dfc0c2d737024bcf1ab1ba0bf69` |
| 74 | `68904da796b9faffda4e2ed91db8776d189def971d5a509ea4e0f89152ba5e7e` | `computations/legacy-condensed-source-parameters-run43659610548-retention30.json` | `08d227af0c3dc41a4300ed5d350a3706dc2634fcafb6bfd0bdc8e3ca94e29080` |
| 76 | `d51f3a4e321f33b777ee435b9de59d12ce09e4741a3ecff4edd1d037474d7a3f` | `computations/legacy-condensed-source-parameters-run43661532089-retention30.json` | `a5498939d8e97ae0b25b33734d281b477beb082b94d86aae7a4d322e77080ec1` |
| 79 | `816dabdcdfe43c8c4f36de9e68fa99c896bfff925444f2e4becead7788fa809f` | `computations/legacy-condensed-source-parameters-run43663293492-retention30.json` | `ac406a51e3dc4c5de668bd725a2201e0bcf93c479be68b6c8bca4c88cb6797bd` |
| 84 | `afba5a8235f844ff1a4742048041265b069016d732017667dff082d047ef4992` | `computations/legacy-condensed-source-parameters-run43666177645-retention30.json` | `54900c06bfb80bb105b418672590807ea646c658a0b16059cac77d90a07ea811` |
| 86 | `b279bdf3a20cf129b4d35b98e4d2b97d18cd436f7794841648151199bb218531` | `computations/legacy-condensed-source-parameters-run43668743515-retention30.json` | `59b70214959ae8afb5db627006a04d5dddea4d1090c3ac8f59e4699b9f80fef5` |
| 89 | `26e828589423cf91040e972c535aff7bba96fe7576ebbe9eb148a6ced2c874f5` | `computations/legacy-condensed-source-parameters-run43671882961-retention30.json` | `d71dc6364e39f6fa207b4d4c5d4d34f00ca58a3d8956a95e0fa9136c7837be39` |
| 94 | `81c457b58c777b6678badfd1043d0c1a542563cb92c472fdf019aaa0e98563c8` | `computations/legacy-condensed-source-parameters-run43674854261-retention30.json` | `b169ba3c36919a32e0176fef36e2ef136d6a87ad4e7be5a6241d054bd75c8ace` |

All 610 source-pin occurrences in these thirteen complete requests match the complete retention-30 source-version catalog. The per-run ledgers keep every occurrence, its actual source identity, the observer entry, the mathematical producer and the complete historical workflow record. The original science command and physical-response command are preserved verbatim for every run, including all original budgets, line-search limits, damping, angular sampling, workers, recovery reserves and stored-root options. The remaining setup, input restoration and publication commands are available in each whole original workflow at its actual source commit.

The raw request path is `computations/public-condensed-qp-request.json` at that run's original source commit. The field `request_sha256` hashes those original raw request bytes. It must not be replaced with the hash of the wrapper, a JSON object emitted by this ledger, or a new canonical serialization. The retention-30 canonical-request identity is separately recorded even where the two values happen to agree.

A real historical inconsistency is preserved: request 67 has a stale `declared_budgets.lambda` value of 270 while its explicit `algorithm_damping` and its actual workflow argument are 27. The complete old request is not silently corrected. The verbatim executed argument is `--damping 27`; the original declaration remains available as written. Request 70 also uses its actual explicit damping 27. Ordinary continuations retain their own full original settings.

Every original run's complete `T112-config.json` is the same 2,161-byte Git object `543d8364593985305438dda6a0c89b4b1a9c7ec5`, SHA256 `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`. Part A includes the complete parsed configuration, including the full valley-control array; the original file bytes remain at all original paths. No array tail, source pin or command option is elided.

The shared accepted input, prepared input, boundary-response record and tail anchor are separately retained in Part A with their original byte identities and restoration sources. None is a removal candidate. The original environment is recorded from the whole original workflows: `ubuntu-latest`, Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`. This retention work does not execute that environment.

## 5. Correct parent and output recovery, including the two branches

Each original parent warm/status pair was checked by directory metadata at the actual child workflow's source commit. Its complete 685-byte original restoration receipt supplies the original consumed warm SHA and original uncompressed status SHA/byte count. The ledgers retain the compressed warm object, compressed status object and original uncompressed status identity separately.

The parent relationships are not a single chronological chain. Request 66 and request 67 both start from actual request 64. Request 68 and request 70 both start from actual request 66. Request 72 continues request 68, not request 70. The later sequence is 72, 74, 76, 79, 84, 86, 89 and 94. All actual run identifiers and source commits are preserved below.

| Request | Actual scientific source commit | Actual parent request / run | Output recovery commit |
| --- | --- | --- | --- |
| 64 | `d625bb293e07541b4bf717524e14a45392be03aa` | 63 / 43646179305 | `cf3a8ff94fae3f7009f85047c69db3aeb8eb320a` |
| 66 | `cf3a8ff94fae3f7009f85047c69db3aeb8eb320a` | 64 / 43648987661 | `9ad4c5d56a85ba952d6e9a538c49fbd3aae4fa14` |
| 67 | `721edbfcacb28d6e7cfd4d139cc9bb6c939786b4` | 64 / 43648987661 | `f4277e28ea531f64e8eed8e8877a5a8ae208fcdf` |
| 68 | `9ad4c5d56a85ba952d6e9a538c49fbd3aae4fa14` | 66 / 43651436427 | `eff90c141df410e83e273d568e4b707903bf8df2` |
| 70 | `ab974f19df95e509346fa15d0cefc037780434fd` | 66 / 43651436427 | `71278605f92a76280f3f9405dbd07cfb331d5c80` |
| 72 | `eff90c141df410e83e273d568e4b707903bf8df2` | 68 / 43653811809 | `145d7a53ec05a64d39d0a36ac3e441e3475cb9bf` |
| 74 | `145d7a53ec05a64d39d0a36ac3e441e3475cb9bf` | 72 / 43656584956 | `1377826d89317b491f75036cafd63c3ea5bea5f1` |
| 76 | `1377826d89317b491f75036cafd63c3ea5bea5f1` | 74 / 43659610548 | `31d2ad909638aa3eb3211a9ea0feed632c0e9a2b` |
| 79 | `31d2ad909638aa3eb3211a9ea0feed632c0e9a2b` | 76 / 43661532089 | `39799fc1a52b91629b3deed3b4fb45e29ae7b6e7` |
| 84 | `39799fc1a52b91629b3deed3b4fb45e29ae7b6e7` | 79 / 43663293492 | `8d199eda5c1f1df162ded244e8dfd012e0c8d127` |
| 86 | `8d199eda5c1f1df162ded244e8dfd012e0c8d127` | 84 / 43666177645 | `032c513ab5db8aff98a6efca2070375418846098` |
| 89 | `032c513ab5db8aff98a6efca2070375418846098` | 86 / 43668743515 | `b75f41fa32b8ead9bb5121b725a0afe1a2f5ae5c` |
| 94 | `b75f41fa32b8ead9bb5121b725a0afe1a2f5ae5c` | 89 / 43671882961 | `55e800dc20289501a96146010247dc48d32e29b9` |

For normal continuation outputs, the following actual continuation's complete parent-restore receipt provides independent evidence of the previous warm/status bytes that were consumed. The two comparison branches and the last run have no such next-run link in this set, so their outputs use their actual publication commits:

| Actual request | Output publication commit | Warm bytes / Git blob | Status gzip bytes / Git blob |
| --- | --- | --- | --- |
| 67 | `f4277e28ea531f64e8eed8e8877a5a8ae208fcdf` | 4820060 / `62c67b70d578e8d69782ae9b643be4865032dc49` | 302506 / `7535a4bb3985c9a9293d5416bca56999f880431f` |
| 70 | `71278605f92a76280f3f9405dbd07cfb331d5c80` | 4830647 / `bde9b962528f221373d32f41a88724f78fe0ec6c` | 303558 / `1f6d48eb11b7709da70c255ab648249c6526ee6c` |
| 94 | `55e800dc20289501a96146010247dc48d32e29b9` | 4913995 / `afd54158ea5ea5d2140161cbfe6ab4b96871e4a7` | 361821 / `cc0644c1b3605361fa6bfc4efa3e78e038e7ec37` |

These commits were checked as historical path-to-object recovery points. They are not replaced by the fixed candidate commit or by `cf41802e7a538f1b3595397681d3371aebf4018d`, which is used only where the older retention record explicitly binds an original generated manifest. Some large warm objects had already left later active trees. The exact historical paths and blobs remain the correct recovery authority.

Request 67's output status gzip has a known blob and compressed byte count, but the original uncompressed JSON size/SHA were not supplied by the small evidence used here; both remain null. For request 70 the uncompressed original status is 2,736,077 bytes with SHA256 `3f8d217914b3c7fe737e9e06e4736d94ef7bd72f152a5623dd4ccc99221372b3`; its gzip whole SHA is unknown here and remains null. For request 94 the original status is 3,165,856 bytes with SHA256 `8b65e2f913e882fffc2a9d92998ea908f89981cd448afc0b81a367a5581ff237`; the known gzip SHA is `50e9075ade6d3876f229d91431fbde237e73983ab0e424004e9a0f639cafd982`. No missing value was generated by reading a large payload.

The original publisher versions are preserved in the full retention-30 source catalog. Their actual rule gzip-compresses JSON/JSONL/log bytes larger than 1,000,000 bytes using `mtime=0` and appends `.gz`, subject to the original publication size limit. Smaller permitted files follow the original copy branch. Restoring a published gzip blob reproduces that original compressed object; it does not imply that a new optimizer run would produce identical output. The original uncompressed intent byte counts and hashes are not inferred from this publication rule.

## 6. Scientific conclusions retained exactly within their original scope

Each of these thirteen actual runs accepted one warm step. The original affine-boundary physical-response checks passed. None thereby became an accepted full coupled BVP solution, a solved new-height nonlinear native tail, a proved closed surface, or a completed research goal. The retention ledgers explicitly retain those negative conclusions.

The recorded line-search outcomes are:

| Request | Accepted step | Nearest rejected step | Recorded limitation |
| --- | --- | --- | --- |
| 64 | 1/32 | 1/16 | Original midpoint485; all nineteen selected grids passed. Farther 1/8 had valid nodes/midpoints but increased merit. |
| 66 | 1/16 | 1/8 | Original left-RMS466 after an actual merit decrease; farther 1/4 failed midpoint484. |
| 67 | 0.001953125 | 0.00390625 | Original left-RMS466. Lambda27 improved the worst physical residual more than request66 but reduced its own fixed-weight merit less; finite QP budgets exhausted, no exact-minimizer comparison. |
| 68 | 1/8 | 1/4 | Original left-RMS484 after valid nodes/midpoints, all twenty-one modeled grids and decreased merit. |
| 70 | 1/128 | 1/64 | Original left-RMS465 after valid nodes/midpoints, all twenty-one modeled grids and decreased merit. Actual finite arrays differ from request68: no only-damping causal comparison. |
| 72 | 1/16 | 1/8 | Original midpoint484; complete RMS and merit were not reached at that nonfinite trial. |
| 74 | 1/64 | 1/32 | Original left-RMS485 after valid nodes/midpoints, all twenty-three modeled queries and decreased merit. |
| 76 | 1/4 | 1/2 | Original midpoint486 and separately saved negative existing left-RMS466. Full RMS and merit were not evaluated at that trial. |
| 79 | 1/32 | 1/16 | Original left-RMS465; same twenty-four-query schema relinearized at actual76. |
| 84 | 1/4 | 1/2 | Original midpoints479,486,487 and separately saved existing left-RMS465 failure; no sole-omitted-query attribution. |
| 86 | 1/16 | 1/8 | Only original midpoint479 at nearest rejection; all twenty-five selected nonlinear grids and original nodes valid. RMS and merit not reached. |
| 89 | 1/32 | 1/16 | Original midpoint487 at nearest rejection. Distinct farther 1/4 trial decreased merit before full RMS rejected left-RMS487. |
| 94 | 1/8 | 1/4 | Original midpoint486 while all twenty-eight selected grids valid. Farther 1/2 decreased merit before full RMS rejected left464 and left486. |

For clarity, the small actual notes also preserve these within-step merit values:

| Request | Its own fixed-weight merit before | Its own fixed-weight merit after |
| --- | --- | --- |
| 64 | 43.79040176025459 | 43.78409880606567 |
| 66 | 43.784169334438104 | 43.7556914034461 |
| 67 | 43.784169334438104 | 43.77799655333434 |
| 68 | 43.75526502490638 | 43.704499218930515 |
| 70 | 43.755265024906336 | 43.73282692338201 |
| 72 | 43.7023098469222 | 43.6768430926219 |
| 74 | 43.6764824644448 | 43.67047492812996 |
| 76 | 43.67031770334245 | 43.57938353308094 |
| 79 | 43.57627837509625 | 43.5661119869748 |
| 84 | 43.56581593085674 | 43.48929991208616 |
| 86 | 43.48685863012245 | 43.46927199458273 |
| 89 | 43.46872005143614 | 43.46027880669424 |
| 94 | 43.45995557126006 | 43.42759299648642 |

These values are copied as literal recorded strings, not recomputed. Each run constructs its own fixed-weight local model. The table is not a cross-round monotonicity assertion and does not authorize subtracting merit values from different local models.

Two execution/publication details matter. Request 67's first revision stopped at a fresh-output-directory guard before the first residual; its second revision is the actual science represented here. Request 70's science and finite-difference check succeeded, but the first publication met a HANDOFF rebase conflict. The existing artifact was subsequently published by run 43657876708 without rerunning the science. These facts are preserved separately from acceptance or nonacceptance.

The actual finite arrays in request 70 differ from request 68. The shared parent and intended formulas do not justify saying that only damping changed in a bit-identical finite experiment. Likewise, the nearest rejected step for requests 76 and 84 had multiple recorded limiting queries; this note does not reclassify them as a single omitted constraint.

The complete original result notes remain:

- Request 64: [`notes/2026-11-14-actual-request64-nineteen-query-nearest-midpoint485.md`](2026-11-14-actual-request64-nineteen-query-nearest-midpoint485.md), complete 13336 bytes, SHA256 `1c6a250dc04adf8ba29b42d007981d4f5d3762218efda4e42276947d3f7374f6`, Git blob `ccace0a2276825e197039d86ebeb0d876cb78bcd`.
- Request 66: [`notes/2026-11-14-actual-request66-twenty-query-nearest-left466.md`](2026-11-14-actual-request66-twenty-query-nearest-left466.md), complete 13921 bytes, SHA256 `9879aeb07c6d5f8699ab622c1f50eca82f05c02cd5d707a5bc8a27853179a95d`, Git blob `d512a0aded5d7103afb641473a67104b99d06186`.
- Request 67: [`notes/2026-11-14-actual67-lambda27-same-base-tradeoff-and-byte-comparison.md`](2026-11-14-actual67-lambda27-same-base-tradeoff-and-byte-comparison.md), complete 15224 bytes, SHA256 `fedfc381cb81066c9b88c2419c3702ccda1ddc0d177eba460a935ced132e2c64`, Git blob `8ba54010b1db22ec8693167890f91d8d28141bf0`.
- Request 68: [`notes/2026-11-14-actual-request68-twenty-one-query-nearest-left484.md`](2026-11-14-actual-request68-twenty-one-query-nearest-left484.md), complete 17383 bytes, SHA256 `ea24a4d487d66dd083f5f1789a71fb065f1683e100ff8cbd189fb946fe3601ca`, Git blob `c9b7ca18f833166da331f865711fe434b946270a`.
- Request 70: [`notes/2026-11-14-actual-request70-lambda27-nearest-left465.md`](2026-11-14-actual-request70-lambda27-nearest-left465.md), complete 16431 bytes, SHA256 `e781380b18409f138623ccd74850fec0f41636ac37e8bd920f7ac7436e7220b8`, Git blob `21b44279a101a1b0aeb0a7470a719cfaf02ccebb`.
- Request 72: [`notes/2026-11-14-actual-request72-twenty-two-query-nearest-midpoint484.md`](2026-11-14-actual-request72-twenty-two-query-nearest-midpoint484.md), complete 13212 bytes, SHA256 `54203b3279708bd6f617bd1002fff1b9b76634582cadd30b2d6d7fbc86594522`, Git blob `bf3705da566c804fe13fb0a5d289a587ae27767e`.
- Request 74: [`notes/2026-11-14-actual-request74-twenty-three-query-nearest-left485.md`](2026-11-14-actual-request74-twenty-three-query-nearest-left485.md), complete 15411 bytes, SHA256 `e39194cad3888a3addf65775e032db53bb10639fbe044417e0e3915b34ef521e`, Git blob `67f4d39867a48cadec06d8b7e4d5136752cc1d0e`.
- Request 76: [`notes/2026-11-15-actual-request76-twenty-four-query-quarter-step.md`](2026-11-15-actual-request76-twenty-four-query-quarter-step.md), complete 15289 bytes, SHA256 `dbc1027d35cc66d70e01c1723b675bada18dbae034f0d485d92fe0187402c8f2`, Git blob `480c010c8491f67d87602756382bf58c0692ae03`.
- Request 79: [`notes/2026-11-15-actual-request79-twenty-four-query-left465-limit.md`](2026-11-15-actual-request79-twenty-four-query-left465-limit.md), complete 18382 bytes, SHA256 `188b85c7412c0905e7c4ba007e902a21a0ca3a658b33824341b5b69d8978eb5c`, Git blob `2819815b994501a30d58324eae0d17bf80e6ae69`.
- Request 84: [`notes/2026-11-15-actual-request84-twenty-five-query-quarter-step.md`](2026-11-15-actual-request84-twenty-five-query-quarter-step.md), complete 21194 bytes, SHA256 `e35d8b8c90e287f4b5dcd7fc1958fe0dcf1639dede1278489ff63b3f282c1371`, Git blob `922695d364e5f87963f8c53fa051874fa404ec80`.
- Request 86: [`notes/2026-11-15-actual-request86-same-twenty-five-query-mid479-limit.md`](2026-11-15-actual-request86-same-twenty-five-query-mid479-limit.md), complete 19035 bytes, SHA256 `6d6884896e6699020259afc5e682abcfee027cbe79b7e19087af33192add04fe`, Git blob `3e56e9ee010e2970c1282b36efd76ba3828d9940`.
- Request 89: [`notes/2026-11-15-actual-request89-twenty-six-query-step-and-cell487-limits.md`](2026-11-15-actual-request89-twenty-six-query-step-and-cell487-limits.md), complete 26241 bytes, SHA256 `c0478968c63dac6a988c4b57e1bdd403eaa6289d0b84e16762680f38ca8c4b7f`, Git blob `93bbe5ace89d7643a86bfc69089b0caf19a99559`.
- Request 94: [`notes/2026-11-15-actual-request94-twenty-eight-query-eighth-step.md`](2026-11-15-actual-request94-twenty-eight-query-eighth-step.md), complete 29911 bytes, SHA256 `4aace482762f0bfc43841a43efb5792be5880af70dfd4668be6f7291cc4b3999`, Git blob `37f1b7a3806cb4990dbb668c6a3c80b0efa71bce`.

## 7. Existing source and parameter catalogs reused

This batch preserves and references these complete existing records:

| Complete retained record | Bytes | SHA256 | Git blob |
| --- | --- | --- | --- |
| `computations/legacy-condensed-manifests-retention-30-provenance.json` | 49041 | `17a1d795952ce8eeda11660f043132bbf5e1cc3b098f5c0f79f4716926eb47fe` | `b427218f9dc705e9d7da65cbc484b7207cbf08b2` |
| `computations/legacy-condensed-manifests-retention-30-sources.json` | 30464 | `b853135bb64ca987e701a0da3436e8d602459bfbc55f9da97b3be916bbcd4472` | `5ff70dbd644327c45a73ab128fcb7f05fce1dcd1` |
| `computations/legacy-condensed-intents-retention-34-provenance.json` | 93023 | `f19e26a0cfde7ca23c8a63962c6ac0fac4e286ea84a78019baa7079d106012b2` | `b962986e53a86a228660db0ecb6d6b7cf9860aaa` |
| `computations/legacy-condensed-intents-retention-35-provenance.json` | 91680 | `433e73a3064d11958cb73e707e33c6255075b19551709fb7ee54c1d642fc487a` | `94c17f4a064eca4c4c903cda07c21d2ae31203bf` |
| `computations/legacy-condensed-intents-retention-36-provenance.json` | 97043 | null (not added by this review) | `ac25369acbaaa87752780a92a3d63ead00b515fe` |

The retention-30 provenance record covers all 23 original condensed runs and their complete non-file parameter contexts. Its source catalog preserves all 77 source-version roles, including historical administrative publisher versions. Retention 34 provides the established generated-identity write/read and actual current warm recipe analysis. Retention 35/36 preserve the same family distinction and correct restoration contract. They are not replaced by this note or treated as a new numerical certificate.

The complete original source-recovery entry `exact_20261114_public_resume.py` and its complete 91-entry `source-dependencies.json` remain in Part A. The actual original workflow invokes `prepare_public_source`, restoring and checking the selected public numerical source files. The entry's unrelated standalone readout main is not substituted for the method the workflow actually called.

The scope reused here is specific: complete original source bodies and parameter records remain recoverable, and the actual reviewed standalone intents are generated outputs. It is unnecessary to rerun all original source audits or solve the original numerical problem before retaining their exact immutable objects.

## 8. Current warm recipe dependency

The previously completed direct dependency review applies to the same whole source identities:

| Actual entry/input writer | Bytes | Whole source SHA256 |
| --- | --- | --- |
| `scripts/resume_20261120/reproduce_and_solve.py` | 1984 | `067b3f2e14145a6f88b2d171c555f1174f0505b45a5aaf670c3ec2610f7c286d` |
| `scripts/resume_20261120/rebuild_fullclosed.py` | 4997 | `4e9ddeaeef2a0ab8b1b38b1412eb066b53578dd649d8f9b4d1a077c7256dee6b` |
| `scripts/resume_20261120/rebuild_closed_warm.py` | 9000 | `63950b72e75e8b6497ad2119ca16076c2c8749f9615166beb6d52adcab86708e` |
| `scripts/resume_20261126/rebuild_axisymmetric_so3_warm.py` | 22706 | `561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4` |
| `notes/2026-11-17-parallel-model-fullclosed-hold-warm.py` | 11230 | `bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3` |

The actual path is `rebuild_axisymmetric_so3_warm -> reproduce_and_solve` without an implementation override, followed by the original fullclosed and closed-warm reconstruction and the pulse/assembly/Hold/mode-warm path. Its full 21 declared source pins are preserved in Part A.

The only historical raw seed consumed by that reviewed path is the original accepted-099 input at commit `60321451c058c6a51da58c37ae5ec6f2d1145f74`, path `notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz`, SHA256 `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`. Its new prefix outputs are actual reconstructions, not relabelled copies of historical later fields. The mode-warm input path uses the actual pulse assembly, actual Hold warm bundle, actual Hold/node report and declared source closure.

None of the thirteen standalone condensed intents is opened by that reviewed direct current path. This is reused source evidence for those specific whole identities, not a claim about all possible historical diagnostics or future changes. If a different consumer needs an original intent, its exact full object remains available through §9.

## 9. Byte-preserving restoration procedure

Restoration is an ordinary file operation against the original immutable repository objects. It does not require a scientific rerun or a new Actions diagnostic.

For a removed candidate, read its complete `candidate` record and restore the exact full repository path from the recorded fixed commit into a fresh scratch file. An equivalent object operation uses its recorded Git blob directly. Check the recorded compressed size and object identity; preserve the complete compressed bytes.

If a historical program asks for `optimization-intent.json`, transparently decompress that original gzip to obtain the original JSON bytes. Do not parse and serialize it anew, substitute a filename stub, drop nested provenance, or use one of these ledgers as the input. This review has not performed such decompression.

For an original parent, use that entry's `actual_parent.restore_commit` and exact warm/status paths. Keep the original compressed warm input as consumed. Restore the exact status gzip and transparently obtain its original JSON bytes; compare the original uncompressed byte count and SHA where the original receipt provides them. Do not compare a recompressed gzip with an uncompressed JSON hash. A null recorded hash remains an explicit unknown rather than a claim of verification.

For an accepted output, use `actual_output.restore_commit` and its exact paths/Git blobs. This particularly matters for the independent lambda-27 branches and final request 94. The candidate recovery commit is not used as an assumed warm/status recovery point.

For a raw request, restore `computations/public-condensed-qp-request.json` from that run's actual scientific source commit and verify the original raw request SHA. The retained whole request wrapper and full retention-30 parameter context provide complete readable records, while the original workflow preserves the literal commands and source recovery sequence.

For scientific sources, follow the complete original source catalog, actual source commit and original `prepare_public_source` dependencies. These are unchanged. A separately authorized scientific replay would have to use the complete original numerical inputs, configuration and public-Actions execution policy. Such a replay is outside this retention operation and is not promised to reproduce output bytes.

## 10. Checks actually performed and checks not claimed

This review performed metadata and complete-small-text work only. It checked all thirteen candidate path/size/blob records at the fixed commit; whole request wrapper and parameter-context hashes; complete original workflow identities and literal science/response commands; all 610 source-pin occurrences against the retained complete catalog; all thirteen original parent warm/status directory records and their complete small restoration receipts; the independent/last output publication records; and the literal short conclusions in the complete retained result notes.

The later producer-family write/read checks are those described in §3. Earlier full mathematical and current warm dependency findings are explicitly reused with their original whole-source scope.

No candidate gzip body or large numerical payload was fetched. No gzip was decompressed here. No local scientific module, F/J/root, solver iteration, finite-difference example or numerical fixture was run. No new AST/compile claim is made. No ref, queue or tracked scientific source was changed by this review.

## 11. Publication boundary and accounting

Only the two ledgers' thirteen exact `delete_entries` are proposed for removal from the active tree. The original scientific sources, original requests/configurations, all original numerical inputs, correct warm/status results, other raw files, result notes, previous complete retention ledgers and exact Git history are outside that deletion set.

The gross removal is **2,596,023 bytes**. The two complete ledgers add **179,612 bytes**; this complete note adds its separately recorded actual byte count. Root can report the final net tree reduction from those exact three new file sizes when publishing. There is no need to trim a scientific source, shorten a parameter list or discard an original conclusion to obtain this space.

No independent rerun, scan, fixture or approval step is introduced. Root may publish the complete retention record and the precisely bounded deletion set by ordinary commit, preserving all immutable restoration identities above. This note records preparation and evidence; it does not assert that the deletion has already happened.
