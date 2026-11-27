# Actual run09 constructor failure, exact selected-stage policy repair, and complete retry

## 1. Observed outcome and scope

The first run09 analytic-frame/J3/root-packet attempt did not reach its first complete physical-field readout. The actual scientific process failed while constructing GeometryScreen. Its subsequent pure reader failed because that scientific report did not exist. This revision corrects the single stale policy key identified by the actual inner traceback, retains the complete numerical solve, and uses a fresh output directory.

The original four entry files, original ready, original command record, actual failure records and actual logs remain historical evidence. This note does not classify the failure as a failure of the SO3 derivatives, a normal root, a geometric condition, or a solver direction.

The complete original entry was published at commit 53e8565c7688e1cd2b7c3d4055832ce3ebe86bb5. The actual trace evidence was subsequently published at d4d976d67b701fdf83cec8f7ad8be2eeb9af54d8. These are existing source/evidence commits, not predicted commits for this revision.

## 2. Actual failed steps and original-log evidence

Run: 45943410994/1.

The original scientific step was complete-run09-public-reference-analytic-frame-J3-packets-first-20261127. Its elapsed time was 10.754519880999396 seconds and its return code was 1. Its only returned declared output was the command record, 26,382 bytes, SHA256 17b6390dd32b9e5c0387f0ed94d5db809ec82fab3f927863913fd3ee82d75c81. No report.json was returned.

The original pure step was actual-run09-public-reference-analytic-frame-J3-packets-first-20261127. Its elapsed time was 5.7503399750003155 seconds and its return code was 1. It produced no readout. Its traceback is FileNotFoundError for the missing original scientific report.

The original scientific log has 6,387 bytes and SHA256 33671079a8ece2456621239ad80e51b7b8e3ff91aa3116b016391780319671de. The independent first/last-trace reader subsequently returned both trace steps successfully. The complete public volume containing these actual returns is:

- notes/2026-11-27-public-actions-45943410994-1-part-002.md
- 28,209 bytes; SHA256 a9c858d0cce4e376ba429a8dbd7a930a302164b6dabdbf082063a778c92f93f4
- Git blob a78e2b69963a175d182d61a3904f4d37c960bdbb.

The scientific trace readout is 10,917 bytes, SHA256 6ea4aa5ea8bdfc3c01f21f44898a0de65da8822c7bddde80d2c74c73e505011b. The pure trace readout is 6,290 bytes, SHA256 dd3027fbfe5d0aec9d10943d7c1719bb7ef61f12ca0aa381d6f980d92c205b77. These are existing trace outputs, not additional scientific evaluations.

The scientific inner call chain is the original driver's main, line 598, constructing GeometryScreen, followed by so3_run09_public_reference_analytic_frame_geometry.py, line 360. The actual exception is:

```text
ValueError: The adjacent-frame producer cannot replace roots, stages or the active field chain
```

The source flow places this constructor before the first q.residual call. No completed field report or source-bound seed-batch/root-packet readout was returned from this failed entry for use by later error consumers. This does not assert absence of every undeclared temporary runner file.

## 3. Exact cause and retained guard

The original geometry file, SHA256 ef121193668791c9c7bc10e8e72314c74ab3c32eff530a4a39dc2ec61d17d409, requested this literal definition key:

```text
all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained
```

The actual bound adjacent-frame producer, analytic_frame_adjacent_normal_matrices.py, SHA256 3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695, exposes this accurately named key with the literal value True:

```text
all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained
```

The selected complete stage equations, roots and angular solves are retained. The local Newton J3 producer already has its explicit analytic working-derivative identity. Adding a misleading old key to that producer would hide this distinction. Instead, the new geometry constructor reads the actual selected-stage key and still requires it to be exactly True.

The other adjacent-policy guard, requiring retention of the original active residual and every upstream parameter edge, remains unchanged. The complete method-codefile checks, source hashes, complete model equality, callback binding and remaining geometry constructor checks also remain unchanged. No permissive fallback or alternate schema is added.

## 4. Four complete independent source files

The following complete files have new basenames. The original files are not edited.

| Role and new basename | Bytes | SHA256 | Unreferenced Git blob |
|---|---:|---|---|
| geometry: so3_run09_public_reference_analytic_frame_geometry_v2.py | 68903 | e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13 | 6d3ddb2f52fc19b60566a567a3b5e2e747887b8a |
| driver: fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py | 80726 | ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5 | eab240470226ff883e618281c3d23be6ccc3b686 |
| launcher: launch_run09_public_reference_analytic_frame_actions_v2.py | 21359 | c1888457b67c85185aebe6c91d2bd4942ccc2d2074407e17f7f54a2825927d23 | 029e86780126fdbfb19daf42bc63f6191465e432 |
| reader: read_run09_public_reference_analytic_frame_so3_report_v2.py | 97351 | aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32 | ee2e71bddb759a659c683cdb4871d06cbb39aa4b |

All four files are below 100,000 bytes and are available as complete text.

The geometry body changes exactly one literal string. The driver changes exactly the geometry path and whole-source SHA in SOURCE_PINS. The launcher changes exactly the driver path and whole-source SHA. The pure reader changes exactly the driver path and whole-source SHA. The report schema remains the existing strict run09 schema; the source identities distinguish the old and repaired entries, and the pure reader still accepts only its exact new driver.

The complete selected-stage source repair does not change any mathematical operator. In particular, these actual bound sources remain unchanged:

| Role | SHA256 |
|---|---|
| Complete normal operator | 3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc |
| Analytic six-control frame | 4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8 |
| Analytic local J3 | 894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866 |
| C1 reuse | f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb |
| Detached stage matrices | fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255 |
| Adjacent angular matrices | 3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695 |
| Reference calibration | fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0 |
| Immutable existing root packets | 094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0 |
| Actual run09 memory | 2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb |
| Actual run09 input binding | 15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592 |
| Actual run09 memory transfer | 6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707 |

The new driver still has all 58 complete source roles. Only its geometry role changes. The complete role-to-path/SHA table is retained in the ready file.

## 5. Complete source-only closure

The independent reproducer is derive_run09_selected_stage_guard_entry.py, 10244 bytes, SHA256 7857547755be8637b64aaf9c4e37cd78c69791be51e158be6a6aa5850681c8f5, Git blob 99e3984d800e59dd54e8508f2775061f54760a9a. It consumes the four complete published parents by their exact whole SHA256, applies the exact literal replacements, and verifies all four expected complete output hashes. It does not import a scientific module.

The complete four-file reproduction actually returned exit code 0. Root separately replayed it with the same result. The independent solver review also reversed each specified replacement and recovered every complete original parent byte for byte.

The following were checked with source text and stdlib syntax/AST operations:

- All 15 driver functions have the same AST as the original driver.
- The full suffix beginning with the nested def save_report() and ending at EOF is 19,574 bytes, SHA256 d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376. It is byte-identical to the original, including both packet-recording hooks.
- The launcher and pure reader change only their source-bound driver identity/path. Their argument handling and readout logic are preserved.
- All 58 runtime source-role hashes close against complete source files; only geometry differs from the original entry's role table.
- Complete files parse and compile; no duplicate literal dictionary keys or trailing whitespace were introduced.
- Every literal policy .get key in this geometry constructor was matched against the actual producer definition. The audit covered 24 keys across C1 reuse, detached stage matrices, adjacent matrices, analytic local J3 and reference calibration. Only the diagnosed adjacent key was absent in the original. All repaired keys exist; required literal flags agree. Dynamic whole-source/model/point checks remain strict.

No local scientific import, field/Jacobian/root evaluation, numerical fixture, geometric scan or solver run was performed. These source checks establish the specified source repair, not numerical success or a continuous certificate.

## 6. Complete retry parameters and outputs

The complete ready file is run09-public-reference-analytic-frame-v2-complete-ready.json, 93108 bytes, SHA256 2ea114b413037b9c54508d4fbf21423abefee7dc73c69a54efc57259aecb1a9f, Git blob ea2d22f86cbc9be5152de5cc31c10b637e09ed38. Its compact JSON formatting removes indentation only. No parameter, selector, source role, evidence object or pending responsibility is removed.

It contains two complete steps:

1. complete-run09-public-reference-analytic-frame-v2-first-20261127, using launch_run09_public_reference_analytic_frame_actions_v2.py.
2. actual-run09-public-reference-analytic-frame-v2-first-20261127, using read_run09_public_reference_analytic_frame_so3_report_v2.py.

The scientific command contains the original 145 argument words and the pure command contains the original 7 argument words. The only argv changes are the fresh scientific output directory and matching pure report/readout paths. Every numeric argument remains unchanged.

The fresh scientific output directory is {work}/run09-public-reference-analytic-frame-v2-first. Its report is report.json in that directory, and the complete launcher command record uses the matching directory prefix. The pure output is {work}/postprocess/run09-public-reference-analytic-frame-v2-first-readout.json. The original failed output directory is retained.

All 333 scientific summary entries and 317 pure summary entries are preserved, with the corresponding output prefix changed. The scientific and pure steps both retain the actually existing reference.npz as parent_bundle. The pure step still requests --verify-final-bundle through its original complete reader; setup does not require an unreturned final bundle.

The full M160/J923/N2048 representation, full current core/rotation/height variables, all 32 normal stages, original residual tolerances, control domain, backtracking, norm, objective, metric direction, restoration directions, full geometric scans, permanent rows, typed witnesses, both distance signs and unknown peer obligations remain exactly those of the original complete ready. The fresh retry does not load an original failed checkpoint.

## 7. Actual input and history remain fixed

The input is still the genuinely returned run09 definition, with canonical target identity 7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a and complete reference model d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75. The actual full chart is 90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e.

The complete actual binding is still 430,906 bytes, SHA256 2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d. Its six actual files, complete fixed target, immutable original 22,456-byte public evidence snapshots, current preparation and whole old dc5 carrier reconstruction remain bound by the unchanged input/memory sources. The current reference is not relabelled from another run, and a future appended public volume is not substituted for the original immutable evidence snapshot.

The explicitly unreturned run07 cc0a report and run08 95559 report remain full source-bound future address and typed-role obligations. Run07's cancelled workflow does not prove its unreturned field/history empty. This revision does not delete either obligation or infer a final point.

The successful input reconstruction and source repair do not establish a mean/root error bound, exact quadrature, full angular continuity, global reach, amplitude success, a solver floor or task completion. Any later source-specific error producer must bind the actual new ff5444/aee22 entry and the actual returned reports/packets. The failed e3cb/47409 entry supplies the failure evidence above and supplies no completed numerical field for that purpose.

## 8. Publication and execution boundary

This package consists of complete source text, the complete source reproducer, this explanation and the full two-step ready. It is prepared for root's ordinary publication and Actions admission. This note records no outcome for the new two steps and invents no future report, checkpoint, packet, model digest or numerical margin.

Root remains the sole ref writer. The unchanged historical sources and failed actual records remain recoverable at their original identities. The repair is complete without an additional numerical preflight fixture.

## 9. Root publication and exact full-parameter check

Root independently replayed the complete four-source constructor with exit0, checked all58 actual repository source roles, and compared the full145/7 argv, complete333/317 selectors, outputs, parent paths and cleanup patterns against the original ready after only the declared fresh-prefix substitution. The full two objects are exactly those of the2ea114 ready. Actual6–7 complete original objects/records/header were verified against the42290-byte f37adad archive before replacing the active queue. The original input1–3 is not scheduled again.

The old four source bodies and both whole ready files remain unchanged at their own identities. The new queue is admission only; no future field or report value is filled. Root corrected two own log heading times to the actual Git commit UTC minutes: b0ebef06:29 and d4d97606:36.

An auxiliary attempt to retrieve old private-repository source files for a separate raw-retention review was rejected by automatic approval review as outside the explicit private QUEUE authorization. That retrieval is not used as a completed source check and was not retried. It does not block the authorized public source repair; subsequent retention work uses already available public sources.
