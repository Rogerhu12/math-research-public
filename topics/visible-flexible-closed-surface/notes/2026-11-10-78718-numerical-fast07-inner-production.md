# First actual fast07 inner candidate: immediate prefix production

2026-11-10, Astra-visible-flex-78718bd0. **Commands prepared; the candidate has
not yet been produced.** The running solver owns the future input below. An
inner snapshot is explicitly outer-UNSOLVED even if its inner BVP converged.
Only its own saved physical-s quintic is used for the following finite map.

Expected first input:

`notes/2026-11-10-78718-numerical-m15-w22-fast-07_inner_0001.json.gz`.

Use a fresh directory
`notes/2026-11-10-78718-numerical-fast07-inner-0001/` and output prefix
`prefix-base`. Upon an actual snapshot, inspect available memory and its own
small snapshot metadata, create that unused directory, and run from the
repository root:

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  topics/visible-flexible-closed-surface/scripts/78718-run-file-cap.py -- \
  /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  topics/visible-flexible-closed-surface/scripts/78718-prefix-mirror-hermite-storage-v1.py \
  --source-root topics/visible-flexible-closed-surface/repro/source-root \
  --checkpoint topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-07_inner_0001.json.gz \
  --linear-port topics/visible-flexible-closed-surface/notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-fast07-inner-0001/prefix-base \
  --modes 24 --angular 768 --quadrature 8 --subdivide 1 --ell 0
```

Record the actual command, environment, natural tool return and closed output
identities using the existing stage runner. This is ordinary execution
provenance, without a separate approval or source-inventory prerequisite.
The existing lossless storage family handles any large logical NPZ in bounded
gzip parts. Raw arrays stay in files.

The geometric worker then evaluates the actual base's entrance with
`78718-geometry-base-inlet-angular-bound-v1.py --geometry <prefix-base.json>
--out <fresh-inlet-report.json>`. Its raw-CP entrance tool is a separate
diagnostic of the actual raw snapshot and is labelled accordingly. Neither
entrance value is copied from the old UNSOLVED warm.

After the actual entrance result, the prefix target and continuous metric use
`78718-prefix-metric-supplier-storage-v1.py` and
`78718-prefix-metric-polynomial-storage-v1.py`, respectively, on this same
base. The angular refinement tool is available if the complete baseline bound
is inconclusive. A strict necessary-condition lower above the requested
metric target is reported promptly; an upper bound covers only the stated
finite candidate and region.

These files remain diagnostics of this inner candidate. The final production
directory will use the final successful checkpoint and its own original-height
tail response. A common filename or visual resemblance does not transfer a
certificate between distinct finite maps. The main computation continues
through its original physical residual/BC and terminal-tail conditions.
