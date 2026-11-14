# Completed nineteen-field arrays: exact read-only relocation

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

Root explicitly authorized moving these private, completed derived arrays
to a separate `/dev/shm` directory to recover disk space for the sole actual
Jacobian. This changes scratch storage only. It does not remove any array
content, change scientific values, modify Git paths, or reconstruct a field.

The operation consumed original plan
`56715b1a962a10412d2913b4187ddcf33baac85ed0f2bd33f189b3fd95855c66`,
the previously completed nineteen-field reader, and all nineteen individual
owned exit-zero resources. Every original field retains 3,767 radial points,
768 angular points, three saved components, and eighteen complete chunks.
The unchanged source/input identities and each exact reconstruction command
are included in the inventory.

All **342 chunks / 498,653,953 bytes** are now stored at

```
/dev/shm/visible-flex-geometry-readonly-relocation/current-A19-20261113/
```

The original paths inside `geometry-work/m32-q126-r1` remain valid as
symlinks to those exact bytes. Each destination was completely copied,
flushed, and checked against the original recorded SHA and byte count
before replacement of the original private path. Each old source was
checked again before its atomic symlink replacement. The complete SHA was
then read once more through the original reader path. All original field,
screen, and owned-resource metadata hashes are unchanged.

The full inventory was durably saved before replacing any path. The receipt
records every completed replacement. Destinations are read-only regular
files, and the scientific source/raw/accepted packets and the active BVP
were untouched. No mathematical computation was repeated.

The owned relocation completed with exit zero in **18.112 seconds**, at
**14,492 KiB** peak RSS. At its final observation the workspace had
1,437,081,600 bytes available. Concurrent writers make that free-space
observation a timestamped diagnostic, not a promised future reservation.

The files remain reproducible scratch data. If the RAM filesystem is lost,
use the retained exact per-case command, inputs, source hashes, grid, and
original output SHA to regenerate only the actually missing field. An
attempt without the original gates and a new owned exit-zero observation
must not be relabeled completed. The relocation inventory is part of the
compact archive; the 498 MB of derived arrays is not copied into Git.
