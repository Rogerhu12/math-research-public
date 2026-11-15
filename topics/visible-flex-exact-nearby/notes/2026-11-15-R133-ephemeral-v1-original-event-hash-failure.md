# Ephemeral v1: actual event-hash failure and exact v2 correction

## Actual public execution

Public run **43680721302**, attempt **1**, job **132710525437**, used commit
**2d648178615c3918f57c042f33fd5ec62a4cf1db**. Setup, exact Python 3.12.14,
package installation, source parsing and all original archive restoration
succeeded. Its mathematical child started at
**2026-11-15T05:25:36.416804+00:00**, returned **1**, and ran for
**9.229537212 seconds**.

The seven original input/coverage gates passed. The old future sweep was
restored from its actual final artifact: **1,886 completed rows**, originally
computed at 320 bits. No old row was recomputed. No new future, past,
product, canonical-port or local-group row completed in this run. The
failure was:

~~~text
ValueError: one true interface impulse belongs to a different event
~~~

This failure occurred in the input event identity comparison, before any
of the three new numerical streams started. It establishes neither a
192-bit arithmetic failure nor completion of the proposed full consumer.

## Exact cause and correction

The frozen original impulse producer uses
~~~python
hashlib.sha256(json.dumps(event, sort_keys=True,
    separators=(',', ':')).encode()).hexdigest()
~~~
through the canonical function of
fourfold_codazzi_finite193_L2_Green_kernel.py. The frozen matrix producer's
canonical function instead appends one newline before hashing. Both
conventions are legitimate identities for their respective producers.
The original matrix posterior helper erroneously used the latter
convention to check an impulse producer receipt.

The independent v2 source copies that posterior helper with its numerical
formula unchanged and checks this one event identity with
m.old.canonical(event), the actual original impulse convention. It keeps
the full equality test. Matrix rows, matrix states and the successful
1,886-row prefix keep their original newline-based identities. No native
input, numerical event, scalar port, matrix, target or input SHA is
relabelled.

All original v1 source, worker, manifest and failure receipts remain
unchanged. The v2 manifest preserves every original v1 pin and records the
new independent source/worker paths. Its worker also publishes genuine
compact archive and historical README-difference provenance; complete old
process bytes remain temporary inputs identified by their exact SHA.
There is no new persistent native, numerical archive or Release asset.

## Actual receipts

All paths below are relative to topics/visible-flex-exact-nearby/.

- Process:
  notes/ephemeral_parallel_matrix_Green_Poisson_ci/run-43680721302-1-ephemeral-parallel-matrix-Green-Poisson/process.json;
  45,479 bytes;
  SHA-256 25d268ffd4501dbdb90f6994450668d7d95feb1e7662b612ee5ef62191e7086b.
- Genuine conclusion summary in the same directory:
  actual-conclusion-summary.json; 5,710 bytes;
  SHA-256 4d22b6a1fc1df46f5bd411e5b10655b70f7a6875b6db846e1a023d6feead2cce.
- Temporary failed scientific output: 2,881 bytes;
  SHA-256 0e77ce7ab869707443edf79148b94f815116d5eeb731760d1a1b01aa07bc6495.
  Its bytes were not uploaded.
- Old successful future native:
  SHA-256 09df7651d1fbef04eb0d67ab5c762a29d4624ad2610015de1254496b70dce1e9;
  original run 43672023585, attempt 1, artifact 14146873569.
- That original artifact process:
  SHA-256 d2119ed8676cfe08cf6341611afa725133f041897ef1f3418d0afed6ca77c809.
- Last actual v1 pull:
  2026-11-15T05:25:52.706603+00:00,
  28b59a6f4ac64fdf1614773d9ca46aab8000ae9e to
  1b49a3634d4b5e0b451aca58f844d34ca063f570.
  Both README differences were empty.

The complete infinite BVP inverse, the unknown high feedback and the true
parameter Schur conclusion remain unproved by this failed execution.
