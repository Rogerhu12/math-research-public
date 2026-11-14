# Exact native cap-energy continuation on disjoint CI ranges

The local native session became unavailable: querying session 84232 returned
"Unknown process id". No child exit code was observed. The last saved FE2
partial had 14 paid intervals, recorded CPU 45.590719252 seconds, and file
mtime 2026-11-12 18:22:15.306814 UTC. It is preserved byte for byte as
data/cap_physical4_energy/native_element002_interrupted_182215.json.gz,
SHA256 fc28b9a378356abadde23304454996214cd3a8a82cc4e57a85c03eda288b2673.
This observation is not labeled an OOM, exit 137, or successful completion.

FE0 and FE1 are complete and frozen in the R95 package. The original
incomplete local manifest is copied without editing to
data/cap_physical4_energy/native_local_manifest_at_interruption.json.
It still correctly declares the old whole requested range incomplete;
the final collector uses only its two explicitly complete element entries.

## 1. Small exact input set

notes/2026-11-12-cap-native-ci-inputs.json lists the complete static local
Python dependency closure and every actual data input used by the native
entry: 34 source files and eight data files, 2,562,144 bytes in total.
Its SHA256 is
abb5b478edb98ff6068319bb597421677a002a9bb4066e0d85bd62d377366565.
The floating moment cache NPZ and the large return-map/reference caches
are not required.

The small wrapper fourfold_phase_cap_native_ci.py verifies these hashes
and the requested exact FE range, then executes the unchanged frozen
fourfold_phase_cap_native_cover_v2.py. It adds no quadrature, no new
mathematical acceptance criterion, and no replacement for a missing
interval. Its observed runtime and child return code are recorded
separately in worker_provenance.json.

The local check-only invocation verified all 42 files and imported the
original kernel successfully. It did not redo numerical energy integrals.
The observed local package versions were NumPy 2.3.5, SciPy 1.17.0 and
python-flint 0.9.0. The CI workflow uses its separately pinned runtime.

## 2. Nine disjoint actual jobs

The right endpoint of each FE index range is exclusive:

| First | Last | Topic-relative output directory |
|---:|---:|---|
| 2 | 4 | data/cap_physical4_energy/native_ci_002_004 |
| 4 | 6 | data/cap_physical4_energy/native_ci_004_006 |
| 6 | 8 | data/cap_physical4_energy/native_ci_006_008 |
| 8 | 10 | data/cap_physical4_energy/native_ci_008_010 |
| 10 | 12 | data/cap_physical4_energy/native_ci_010_012 |
| 12 | 14 | data/cap_physical4_energy/native_ci_012_014 |
| 14 | 16 | data/cap_physical4_energy/native_ci_014_016 |
| 16 | 18 | data/cap_physical4_energy/native_ci_016_018 |
| 18 | 20 | data/cap_physical4_energy/native_ci_018_020 |

For example, from the topic directory:

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_native_ci.py \
  --manifest-sha256 abb5b478edb98ff6068319bb597421677a002a9bb4066e0d85bd62d377366565 \
  --first-element 2 --last-element 4 \
  --out-dir data/cap_physical4_energy/native_ci_002_004
~~~

Change only the two indices and the independent output directory for the
other eight jobs. The wrapper supplies all frozen native settings
explicitly: 160 bits, primitive size 256, 1024 angles, normalized strip
1/32, minimum radial analytic radius 1/4096, Gauss order at most 32,
radial depth at most 10, and error density 1/10000.

The original seed and old paid-prefix argument are retained exactly to
preserve the kernel identity. For these jobs the old prefix lies in FE0,
outside the requested range, so it contributes no reused FE2 rows.
FE2 is recomputed as a whole. This avoids treating its interrupted
partial as a completed finite element.

Every accepted interval is checkpointed by the original kernel. A CI
rerun reuses complete original element reports only after the original
identity check. Before an incomplete report could be overwritten, the
wrapper preserves an exact SHA-named copy in the output recovery folder.
The CI artifact upload must run even on failure and include the entire
independent output folder. An unfinished job remains unfinished.

## 3. Artifact restoration and final collector

Restore each artifact under the identical topic-relative directory shown
above. Its manifest paths then remain portable. Do not replace the local
FE0/1 manifest with a remote two-element manifest.

Use the frozen collector without changing its source:

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_energy_collect.py \
  --body-manifest data/cap_physical4_energy/native_local_manifest_at_interruption.json \
  --body-manifest data/cap_physical4_energy/native_ci_002_004/manifest.json \
  --body-manifest data/cap_physical4_energy/native_ci_004_006/manifest.json \
  --body-manifest data/cap_physical4_energy/native_ci_006_008/manifest.json \
  --body-manifest data/cap_physical4_energy/native_ci_008_010/manifest.json \
  --body-manifest data/cap_physical4_energy/native_ci_010_012/manifest.json \
  --body-manifest data/cap_physical4_energy/native_ci_012_014/manifest.json \
  --body-manifest data/cap_physical4_energy/native_ci_014_016/manifest.json \
  --body-manifest data/cap_physical4_energy/native_ci_016_018/manifest.json \
  --body-manifest data/cap_physical4_energy/native_ci_018_020/manifest.json \
  --body-manifest data/cap_physical4_energy/body_wiener_0800_3000/manifest.json \
  --body-manifest data/cap_physical4_energy/body_wiener_0900_3000_vector/manifest.json \
  --out notes/2026-11-12-actual-cap-compression-energy.json
~~~

The collector also requires the already complete natural-graft/true-tail
report at its frozen default path. It verifies complete exact intervals,
all numerical identities and hashes, and rejects overlaps. Until all
body elements 0 through 63 exist, it writes only an explicit
complete:false/missing-elements result. A shell exit code of zero alone
does not change that status. No absent endpoint, element, or matrix is
replaced by zero.

After completion, the same output gives both the finite DN compression
enclosure and the entire primal/dual energy gap required by R95. Their
error quantities and boundary norms remain distinct.
