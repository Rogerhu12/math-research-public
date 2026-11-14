# Authorized cleanup of the completed old M28 geometry fields

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

The root agent explicitly authorized reclaiming the completed old q122 M28
seventeen-field geometry arrays after checking their hashes, reproduction
commands and original successful resources. This is storage maintenance and
does not change a mathematical conclusion or any accepted solution.

The completed run removed exactly 306 `.npy.gz` field chunks, totaling
451,721,535 logical bytes and 452,349,952 allocated bytes. Before deleting any
file it wrote and fsynced the complete inventory: all original paths, SHA-256
hashes, byte counts, radial ranges, original commands, successful owned
resources and field/report identities. Every chunk was hashed once to build
that complete inventory and again immediately before its deletion. The
per-file removal journal and the final result were saved separately.

All old field manifests, reports, commands and source files remain. Original
accepted/raw/collocation/fullflow and full/half response arrays remain. A/B
Cartesian point blocks remain. The true q126 M32 current baseline's eighteen
blocks and all of its metadata were hashed before the cleanup and rehashed
unchanged afterward. No removed array is a dependency in the actual current
baseline plan. The current nine-control response uses the accepted M32 raw
data, not these removed old M28 comparison fields.

The first validation attempt exited 1 before the inventory or any deletion:
the old thirteen-field resource schema has no `wait4_observed` field. Its
separately pinned `strong_resource_run.py` (SHA `bbf6c8ac...`) directly executes
`os.wait4(pid,0)`. The successful fresh consumer explicitly pins both that
original wait4 contract and the newer `strong_foreground_resource_run.py`
contract; it requires successful exit, no signal, and the exact original
command in either case. The first attempt and its source are preserved.

Successful cleanup exited 0 in 7.240456323 seconds, using 15,024 KiB. The
shared filesystem had 4,968,001,536 free bytes at completion. Other agents
were reclaiming storage concurrently, so this free-space change is not all
attributed to the present 452 MB removal.

## Regeneration

Each old field can be regenerated from its complete recorded scientific
arguments, original raw inputs, response arrays, source pins and grid. Use
a fresh output prefix, resource/log destinations and field manifest while
retaining the exact source/input arguments and cwd. The original chunk
producer deterministically gzip-encodes the finite Float64 arrays. Compare
each regenerated chunk's radial interval, size and SHA against the inventory;
no old mathematical or physical parameter is reconstructed from a summary.
The existing full-seventeen-field archive contains the original small
metadata and complete reader contract. No regeneration was performed during
this cleanup.
