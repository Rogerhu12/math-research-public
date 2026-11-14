# Actual request52: complete868 direct-LD capture stopped while writing its specification

分类：实际计算流程记录；作者：ChatGPT（geometry / root）；日期：2026-11-14。

## Observed result

The public run [43634201913](https://github.com/Rogerhu12/math-research-public/actions/runs/43634201913), source commit `61831d6a76b2a06e0c22f7fe03aad87d1b69d39f`, did **not** start a new native worker or the direct-LD numerical worker. Job `132567309832` failed while serializing its complete input specification. This is an evidence-file transport failure; it supplies no new scientific result about the868 maps, the new1372 system, or the original nonlinear trial.

The official job log places the capture step at2026-11-14 19:51:02–19:51:04UTC. The first traceback is:

```text
geometry_20261114_native_rawcell0_direct_ld_capture.py, line243:
    spec_path=a.out/'direct-ld-spec.json';B.write(spec_path,spec)
geometry_20261114_native_candidate_seeded_solve.py, line52:
    raise ValueError("Use a bounded gzip packet for a large evidence record")
ValueError: Use a bounded gzip packet for a large evidence record
```

The frozen helper constructs the complete UTF-8 JSON payload and rejects it when its length is at least1,000,000bytes, before opening the destination. Therefore no exact serialized-specification length was recorded, and this note does not infer one. The failing call precedes environment setup, `TailClient` construction, its ready handshake, and both workers. The source also reaches this call before the later result-writing `try/finally`; absence of a normal capture `result.json` is consistent with this traceback.

## Inputs and evidence actually preserved

Fixed actual28 and actual41 artifact fetches completed, as did restoration of the original public native sources. The artifact preserves the72 original input/output/guard-mean packets copied from actual28 and the complete consumed-reference records for actual41. Copying and hashing these old records does not create a new evaluation.

| Preserved file | Bytes | SHA256 |
| --- | ---: | --- |
| `rawcell0-direct-ld-capture.log` |995| `cce44b13afa4272f972c1e4bc5d2125e2d258cad9aa974cb4441374b456b5400` |
| `native-rawcell0-direct-ld/original-reference-packets.json` |131287| `9b3fe243bef0ac6106e7ae59780c6d6fdb8cc786cd593345412ac72d7a0cb8c6` |
| `native-rawcell0-direct-ld/actual41-consumed-reference-packets.json` |832038| `b5467b04e10679250c39d346e91dc61c2d28a2a92bc71ccdedfdbd774c4e507c` |
| `native-rawcell0-direct-ld/direct-ld-input-config.json` |2161| `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

The complete uploaded artifact is `visible-mainline-directld-43634201913-1`, artifact ID `14129895088`, ZIP697565bytes, SHA256 `f5351cb68add465edeb99eb521f1a14942f8e8047c4741f0a9c30640980cead9`. The repository coordinator downloaded this artifact once; the diagnosis reads that extraction and the official job log.

The checkpoint for this run is therefore:

- New original-RHS/local-J calls:0.
- New original RK steps and new direct-LD matrix formations:0.
- New1372 linear solves and original nonlinear trials:0.
- New native complete response, endpoint Jacobian and final audit: none.
- No accepted new state or new mathematical conclusion.

These zero counts follow from the actual exception's position in the frozen launcher, not from a fabricated successful summary.

## Necessary continuation

Retain all specification fields and use gzip for the entire specification; make both existing readers recognize gzip by its magic bytes. Continue binding `spec_sha256` to the actual stored compressed file bytes, with a separate uncompressed-size/hash receipt. The frozen native/RK/port/mean arithmetic, full source identities and original acceptance conditions remain the same.

The source-level repair and its exact scope are documented in [the gzip specification transport note](2026-11-14-direct-LD-gzip-specification-transport.md). Request52's old source bytes remain identified by its public commit. A rerun of the repaired chain is necessary; this failure does not establish whether that chain will complete or yield an accepted nonlinear trial.
