# Request104: exact Git-object cleanup under Rule15

Date: 2026-11-15. Scope: repository bookkeeping, no mathematical computation.

This implements the author's Rule15 ordinary deletion instruction. It preserves
all published commits, performs no force push, creates no Release or artifact,
and makes no scientific acceptance decision. Only root's later publication of
the request may start the Actions cleanup.

## 1. Actual metadata that determines the whitelist

The personally read Git Tree API inventory is pinned to:

- Historical commit: 52704ecdfc84f1d67c8a3cf6233d910f46582844.
- Notes tree: 3832eb52ca0b5414ab761a47fd6774497695b431.
- Repository: Rogerhu12/math-research-public.
- Topic: topics/visible-flex-larger-amplitude.

The historical commit-to-notes-tree link was checked through Git commit/root/
topics/topic tree metadata. All 189 notes child directories were read with
nontruncated results. No scientific blob contents were transferred.

The complete pinned inventory has zero .pdf/.png/.jpg/.svg entries and zero
.jpeg/.gif/.webp entries. The selector no longer treats the former four suffixes
as deletable raw data. No paper or image is presumed regenerable from its name.

| Original metadata scope | Files | Stored bytes |
|---|---:|---:|
| Complete notes tree | 14551 | 2789284775 |
| Files directly in notes | 9277 | 1475463721 |
| 129 public-actions directories | 4834 | 1258921680 |
| Remaining 60 notes directories | 440 | 54899374 |

Deleting only public-actions would leave the large flat notes payloads.
The selector therefore runs over the entire pinned notes tree.

## 2. Conservative categories and exact counts

Order matters. Code/conclusions, named identity records and parameters are
recognized before compressed/raw outputs. Unknown JSON is retained.

| Decision/category | Files | Bytes |
|---|---:|---:|
| Keep Markdown/code/conclusions | 1181 | 10217498 |
| Keep named identity/manifest metadata | 1166 | 37106467 |
| Keep named parameters/config/intent/profile | 984 | 19430454 |
| Keep unknown entries | 3036 | 80601992 |
| Delete numeric/compressed regenerable payloads | 4519 | 2519384365 |
| Delete explicitly named computational JSON outputs | 1287 | 33268761 |
| Delete generated logs/JSONL/text outputs | 722 | 7575227 |
| Delete other public-actions JSON outputs | 1656 | 81700011 |
| **Total pinned deletion** | **8184** | **2641928364** |
| **Pinned notes remaining** | **6367** | **147356411** |

The already provided computation/results metadata is 18109660 and 2540068
bytes respectively. With the other root Markdown this first pass projects
roughly 168.5 MB for the topic. This is not substituted for the actual
post-push total: Actions reads all current topic sizes from GitHub tree metadata
and reports the actual final total.

Unknown JSON remains deliberately unclassified, including some files that may
also be regenerable. This pass does not claim to complete every Rule15 content
classification. It safely removes the identified payloads while preserving
code, parameters, compact textual conclusions and uncertain files.

## 3. Byte identity of the regenerable deletion plan

The full path list is not committed, split, uploaded, or sent through a
connector. It is regenerated in runner temporary storage from the pinned tree
and the committed selector.

- All-pinned metadata TSV: 1878273 bytes, SHA-256
  53e551c2075176798781a879bd0f5c45d0196f9aa166d9bf13ec831c96e9b488.
- Pinned deletion TSV: 1665949 bytes, SHA-256
  7b725628c3fb394d2d22f0fe7cbac28b7238bfac0d13a06227b1481804f450f0.
- Pinned NUL path list: 1032161 bytes, SHA-256
  289ac88afec320e42045f1928b4112a625e7dca70ff35bbf1c5fd7ede0371625.

The all-metadata TSV uses mode, Git blob SHA-1, decimal bytes and notes-relative
path, tab-separated with newline terminators. The deletion TSV adds category
and uses full repository paths. Sorting is UTF-8 path byte order; all pinned
paths are ASCII and have no tab, CR, LF or NUL.

The Git blob SHA-1 is explicitly an object identity, not a newly computed
payload SHA-256. Known original-input SHA-256 values are listed separately and
are not reverified by downloading their data in this cleanup.

## 4. Partial-clone and concurrency behavior

Sizes are taken only from GitHub Git Tree API metadata. The API reader first
uses a recursive tree response and falls back to complete direct/child tree
metadata if truncated. It refuses missing sizes, duplicate paths, unsupported
objects or mismatched pinned totals/hashes.

Current Git matching uses exactly ls-tree -r -z, without -l. The latter may
hydrate promisor blobs just to determine sizes and is therefore excluded.
There is no git show or cat-file data read. GIT_NO_LAZY_FETCH is set for Git
subprocesses; Git's own instruction-file diff is limited to the two small
README files if their policy changes.

Every Git subprocess also receives merge.renames=false and diff.renames=false
through process-only GIT_CONFIG entries; authentication is appended only in
that environment. The compact receipt records the actual git --version.
Keeping GIT_NO_LAZY_FETCH does not claim a separately executed compatibility test.

A pinned candidate is applicable only when the current HEAD has the identical
path, mode and blob OID. The API size must also be identical for that OID.
Already absent files need no action. Changed candidates are retained and their
complete metadata is placed only in a temporary receipt. Files introduced
after the pinned tree are not classified or deleted.

The apply path is explicit and Actions-only. It:

1. Starts from a clean sparse checkout and performs an ordinary pull/rebase.
2. Checks root README blob 74c08a36f6c997d0bc1e64a7956b42276f5fa5d7
   and topic README blob bff8aea253a9e6a7a4fac28d810ac454c5499fec.
3. Reproduces the pinned whitelist and matches current Git/API metadata.
4. Uses update-index --force-remove -z --stdin for exact matching paths.
5. Stages only those deletions and one uniquely named compact bookkeeping note.
6. Creates an ordinary commit, pulls/rebases and checks the README identities
   again immediately before an ordinary non-force push.
7. Retries non-fast-forward pushes with pull/rebase. On a modify/delete rebase
   conflict, it aborts the unpublished rebase, keeps that unpublished local
   branch, starts a new local branch from fetched origin/main, and rematches
   every candidate. It never resolves a changed remote file by blindly deleting
   it and never rewrites any published commit.
8. Reads the final public tree metadata and emits the actual topic size.

The source never edits HANDOFF.md, open.md or log.md. Root coordinates those
shared status files separately. The one note belongs only to this run/attempt;
its counts are explicitly tied to its planning HEAD, and final stdout records
the actual post-push total after any concurrent rebase.

## 5. Actual original-input continuity

The current pipeline's already declared fallback is historical commit
8bd267107cc8710d371f3b62c02986655ac965b0. Request101's actual workflow was
personally read: when an original input is absent from main, it fetches that
historical commit with blob:none, reads only the named original, and checks its
previous bytes/SHA-256. The later105/106 literal-recipe path does not need an
old parent-status payload in main. This cleanup does not add a new cache or
rename an old computed result as fresh.

| Original role | Notes-relative path | Disposition |
|---|---|---|
| Accepted96 | public-actions-43580643038-1-free3/stage-00/actual.json.gz | Historical byte-pinned bootstrap |
| Prepared112 | public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz | Historical byte-pinned bootstrap |
| Zero T112 anchor | public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz | Historical byte-pinned bootstrap |
| T112 parameters | public-actions-43588155190-1-prepare112/T112-config.json | Retained in main |
| Actual99 parent used by101 | public-actions-43677789194-1-smallcoreresonance/small-core-inexact-p3-restoration/inexact-p3-restoration-status.json | Historical byte-pinned bootstrap; later literal recipe does not need it |

The script carries all five exact sizes and previously verified SHA-256 values,
and checks their metadata OIDs/sizes against the pinned inventory. It does not
download those five payloads.

All computations and results remain outside this deletion selector, as does
the public78 source topic. The frozen public_resume source still obtains its
78 pinned sources from that source topic; none is removed here. Legacy
consumers of removed notes payloads must use their explicit history/source
identity rather than assuming that an old raw output still exists in main.

## 6. Files, CLI and hashes

- Script: computations/root_20261115_rule15_prune_notes_metadata.py.
- Request: computations/public-rule15-notes-cleanup-request.json.
- Workflow: .github/workflows/visible-larger-public-rule15-notes-cleanup.yml.
- This interface is documentation only; it is not an additional approval gate.

Script: 30997 bytes / SHA-256 7e0dfcb584ad1e03ce2df5a8b8c45508372edd2341fac22e1d9d46f5628d49bb.

Exact classify-function source: 1786 bytes / SHA-256
bb5108640323cbd61fefa933a463f05699709709bbfde2ab7407fd6ec491a669.

Request: 2387 bytes / SHA-256 9418f57b5b6d6a4d182b3a390d61cdb6962188fd3ac8326fc01d99e24b0c0192.

Workflow: 3329 bytes / SHA-256 bca95df881c42ecfe7667ed22ee752df6bf323eab3162c906d69d65e5a407f00.

~~~sh
python -u root_20261115_rule15_prune_notes_metadata.py \
  --repository "$GITHUB_WORKSPACE" \
  --recipe /temporary/request.json \
  --out /temporary/rule15-cleanup104-output \
  --apply
~~~

Omit --apply for a read-only metadata inventory. The output directory must be
new and outside the checkout. Full inventories exist only as temporary
operational files; no upload step exists.

The workflow has one request-path push trigger, independent cleanup
concurrency, contents:write for its authorized ordinary commit, Python3.12.14,
and no numerical runtime dependencies. Checkout uses blob:none and exact
sparse paths for two README files and the two small source/recipe files.
The source and recipe are copied to runner temporary storage before pulling,
so changes to main cannot silently change the executing program. The token is
provided only to the cleanup step; API requests are read-only GET requests,
and Git push authentication is held only in process environment, not a file.

## 7. Verification and honest limits

The actual complete API metadata, counts and ledger hashes were read/computed
without any scientific blob payload or scientific arithmetic. Source and
workflow were reviewed as text. The local terminal is unavailable, so no
Python AST run, shell execution, Git deletion, commit, push or cleanup Actions
run is claimed in this preparation. The workflow compiles the exact pinned
Python source before any apply step.

Only a detached small-text staging commit is authorized for delivery to root;
it does not move any branch or execute the cleanup. Root publishes the actual
request after reading it. There is no added BVP/native/jet/FD acceptance rule.
