# R106 native recovery and first completed seven-field bidisk

2026-11-13, phase_inverse. Status: the three lost jobs and the new common
seven-field domain have actually executed. Whole returned phase and strong
PDE inverse remain open.

## Recovered original jobs

Run from this topic with Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5,
`PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps`, and one BLAS thread:

```
python3 scripts/fourfold_subprincipal_recover_native_0102.py \
  --out-dir data/R106/recovered_20261113_phase_inverse
```

All three original kernels completed. The extracted bulk gzip has exactly the
previous SHA256 `5f8ead1a783632d5a942403405cb42bf7d957a3d7a7847c85d138f63b240053e`.
The point and 64-cell whole-parameter root strip reports also have
`complete=true, proved=true`; their timing-dependent hashes are recorded in
`data/R106/recovered_20261113_phase_inverse/replay_manifest.json`.
This is a fresh computation from full retained inputs, not reconstruction from
an execution receipt. The real-angle-only scope of the transferred bulk remains
unchanged.

## Executed boundary-domain repair

The original `fourfold_subprincipal_root_bidisk_boundary.py` failed after its
initial checkpoint with `series must have one common declared precision`.
The failure report remains at
`notes/2026-11-13-R106-seven-field-boundary-native-2048.json.gz`.
Radial differentiation lowers an acb_series declaration from m to m-ar,
whereas the unused Fourier modes had been initialized with ctx.cap=m.
This is a finite-array representation error, not a failed geometry gate.

The new `scripts/fourfold_subprincipal_root_bidisk_boundary_v2.py` initializes
those exactly zero Fourier modes at the common differentiated precision.
No nonzero coefficient, true remainder, or geometric formula changes. The
original source is preserved. It was then run as

```
python3 scripts/fourfold_subprincipal_root_bidisk_boundary_v2.py \
  --half-width 1/1000000000 --physical-strip 1/64 \
  --radial-radius 1/2500 --precision 40 --angles 2048 --nodes 512 \
  --out notes/2026-11-13-R106-seven-field-boundary-v2-native-2048.json.gz
```

All 2048 closed angular cells pass. The complete report is 867991
bytes, SHA256 `92c9da078e1dfa4d18843dcc2a31e0fea70b83f16ec1acf6a9c73cab896bb712`. Elapsed wall time: 39.248 s.
It binds all input, source and dependency hashes. The source also records every
six-jet cell fee and all denominator lower bounds.

The new `fourfold_subprincipal_root_fourier_v2.py` differs from the stored,
unexecuted Fourier entry only by admitting the new boundary producer with its
actual source SHA; there is no relaxed numerical or domain check. Subsequent
`*_regularized_fft_v2.py` and `*_reference_v2.py` pin that new producer chain
without changing old source identities.

See `results/R106-supplement-actual-seven-field-native-bidisk.md` for the proved
common domain and constants. The finite Fourier-Taylor and actual-ray tasks
continue separately; this domain does not supply them automatically.

## Completed degree-64 seven-field representation

The next native command also completed; the output directory is immutable:

```
python3 scripts/fourfold_subprincipal_root_fourier_v2.py \
  --domain-report notes/2026-11-13-R106-seven-field-boundary-v2-native-2048.json.gz \
  --include-root-aux --degree 64 --precision 76 --angles 1024 --keep 450 \
  --working-radius 7/25000 --working-strip 1/400 \
  --out-dir data/R106/root_seven_native_degree64
```

The report SHA256 is
`abf77633bb8340eaf11fe45d6f3fb943a80d265c9a5c0d2ce234c64d9ee36bab`.
It preserves every signed mode -450..450 and all radial rows 0..64; the
complete sup errors include node balls, finite arithmetic, all aliases,
unretained angles, and the radial tail. The node shards are reproducible
intermediates; only required coefficient shards and the report need retention.
The report already records every omitted intermediate's input/size/hash.
The later source consumer reads only the report and coefficient shards.

Complete errors on rho radius 7/25000 and physical strip 1/400 are
G < 0.000004317, q < 0.00038451, kstar < 0.010876,
Sreg < 0.000002547, Ltheta < 0.00043997, U0 < 0.000031793,
U1 < 0.0047968. These are complete sup errors, not same-width Wiener
errors. Most of the G error is the whole-parameter node enclosure
transported through the weighted DFT; simply increasing radial degree
does not remove that contribution.

The positive-branch regularized source also completed with command

```
python3 scripts/fourfold_subprincipal_root_regularized_fft_v2.py \
  data/R106/root_seven_native_degree64/report.json \
  --sigma 1 --working-strip 1/800 \
  --out-dir data/R106/root_regularized_native_degree64_plus
```

The actual complete source sup error is below 1402.853, the cut error
below 4.50834, and the root-field error below 0.000109992. The true
continuous ray correction and complete returned phase remain separate.

The original descriptor-based reference sampler was attempted at segment
549 and failed because the original Q_forward/segments_00528.npz.gz
is not in this checkout. Its manifest is present; the complete small
549 package is present and permits a faithful package-based continuation.
No reference sample or integral is inferred from that failed command.
