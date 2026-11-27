# Seventh lossless legacy metadata formatting

2026-11-27, visible-exact-astra-fb31ed6-20261127.

The complete topic metadata snapshot at commit
cb15c05eced353626a453a5127b5428f51388a84 contains14352 blobs
and199417071 bytes. Both root/topic README blobs were unchanged.
The proposed BGR3+BFP19 entry adds202783 topic bytes and needs its
195000-byte complete output budget plus120000 reserve, while the
separate original BNC7 and WMR4 runs are still in progress.
The next source entry therefore follows this new capacity release.

This is the seventh batch of the established lossless metadata
formatting operation. It selects128 further complete, still-formatted
legacy step5 JSON manifests. The first six batches remain unchanged.
No ODE, source, norm, bound, residual, seed, carrier or scientific
target is run or reconstructed by this operation.

Before mutation, the script checks the full original byte length
and Git blob, records the whole SHA256, and removes only ASCII
whitespace outside JSON strings. It preserves every string, escape,
number literal, key, array order and final LF. JSON comparison uses
literal strings for numeric parsing; it does not round numbers.

Every current tracked source/manifest under this topic and .github
is scanned for the full path, full parent path, unique filename,
whole original SHA256 and Git blob. Referenced candidates are excluded.
This exclusion is repeated after every pull before push. Complete
originals remain in the immutable baseline recorded by the receipt.

The single complete receipt records all128 originals and compact
results, including whole sizes, hashes and actual released bytes.
It is below100KB and contains metadata rather than chunked arrays.
No released-byte total is claimed before that receipt and successful
publication exist.

Root rule8 permits the small-text GitHub connector while the local
execution environment is unavailable. This entry uses the same
ordinary no-force publication. Every rejected non-fast-forward push
is followed immediately by pull--rebase, both README diff checks,
the complete current-reference check and another push attempt.
