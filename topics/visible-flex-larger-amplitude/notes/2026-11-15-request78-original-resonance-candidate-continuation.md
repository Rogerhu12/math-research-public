# Request78: continue the actual77 candidate with the original twenty-backtrack budget

**Classification:** source and provenance facts, with a proposed numerical diagnostic. The quoted numerical observations below were saved by actual77; no mathematical computation was performed locally. Request78 has not been executed by this preparation.

**Author:** amplitude branch of the visible-flex-larger-amplitude session, 2026-11-15 UTC.

## 1. The concrete change

Continue the frozen [R259 diagnostic](../computations/geometry_20261114_small_core_resonance.py) from the three parameters in actual77's original `final.parameters`:

```text
0.09307073916632971
-0.1321108634591744
-0.1241786723386648
```

Keep the eight-iteration candidate budget and change only its per-iteration backtrack budget from twelve to twenty. The original source already accepts `1 <= backtracks <= 20`. Consequently, this request needs no scientific source change and makes no attempt to pass an unsupported value such as 24 or 32.

The original trial sequence remains $\alpha=2^{-j}$. Actual77's failed second iteration stopped at $j=11$. Request78 permits $j=0,\ldots,19$, adding the eight previously untried levels $2^{-12},\ldots,2^{-19}$. It rebuilds the circular collocation reference from the same four mathematical inputs and the actual final parameters. The old circular reference is not used as an accepted nonzero-amplitude parent.

## 2. Why this is an evidence-based diagnostic

The [actual77 status](public-actions-43661078498-1-smallcoreresonance/resonance/resonance-status.json) is a 23,659-byte original JSON file with SHA-256:

```text
e003cc07e52789fa075289794f4bee76993b88cbdf1dc7b639a46872019fcc14
```

Its identity is run `43661078498`, source `1200c13713b0a4ce4d125a0534610583223ed4ef`, job `132650310904`. That diagnostic completed normally and saved `success: false`. Its first iteration accepted $\alpha=1/128$. The second iteration had twelve actual rejections; its last eight trials were finite and failed the existing merit test. The last saved trial, $\alpha=1/2048$, had merit `67097145297.87776`, against the iteration's original `65080884368.11076`; the saved directional slope was `-130161768736.19452`.

The final parameter derivative was also checked by the source's three existing real finite differences. The saved relative discrepancies were `5.683663624461545e-9`, `1.4303713790512272e-9`, and `8.478407449670264e-10`. The final original circular reference passed its saved node, midpoint, and two RMS query checks. The declared scalar-expression audit saved 494 leaves, 51 subdivisions, and zero unresolved leaves, for its stated radius/slope scope.

These records justify paying the remaining supported backtrack budget at the last actual candidate. They do not guarantee a new accepted step, a small resonance residual, or a nonzero nonlinear solution. No local value of a predicted smaller-step merit, Newton direction, norm, or threshold crossing has been computed.

## 3. What remains identical

The scientific file remains 25,799 bytes, SHA-256:

```text
3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5
```

All 68 source pins from request77 remain unchanged, including publisher `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`. The accepted96 provenance, original 699-node preparation, actual T112 zero response, and original tail configuration remain the same byte-identified four mathematical inputs. Actual75's historical diagnostic identity is retained separately from the new actual77 candidate identity.

The source still computes its actual three-equation direction and actual merit slope, checks every trial through its original circle/scalar evaluator, and applies its original rule

$$
\mathcal M(p+\alpha d)\leq \mathcal M(p)+0.2\alpha\,\mathcal M'(p)d.
$$

The candidate tolerance remains $10^{-8}$. The mesh remains 699 nodes; field and tail dimensions remain 112; the original physical angle grid is 2048 and material/boundary angle grid is 4096. The complete saved $112\times112$ true zero slope Jacobian is consumed. No off-diagonal entry is rounded away, and the source's guard against substituting a three-equation search for a genuinely coupled high-core Schur problem remains in place.

The source retains the final three parameter-difference checks, all 112 first-order right residuals, original complete-circle evaluation, and declared scalar-expression audit at 160 bits and depth 14. The latter is an enclosure for its explicit real scalar expression; it is not a certificate of the literal floating-point program, the whole Frenet field, or a nonzero surface.

The execution environment remains Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, python-flint 0.9.0, and one BLAS/RHS worker. The job and scientific-step timeouts remain 60 and 45 minutes. The original78 source restoration and original publisher are unchanged. No Node/native solve is started.

## 4. Exact provenance and workflow changes

The unique existing workflow trigger remains:

```text
topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json
```

The prepared files are `visible-larger-public-small-core-resonance.yml` and `public-small-core-resonance-request.json`. Their complete diffs against the actual77 drafts are included alongside them.

The workflow changes are limited to the request number and job/step labels, the two diagnostic argument values, and actual77 provenance. Sparse checkout adds the published original status. Before scientific invocation, the existing identity step checks its literal path, byte length, SHA-256, `final.parameters`, four input hashes, and consumed-source hashes. It copies the exact prior JSON bytes to `prior-candidate/actual77-resonance-status.json`. This is source/input binding, not a new mathematical acceptance test.

The workflow still makes one subprocess invocation of the unchanged scientific entry. Its essential existing arguments are:

```text
--parameters 0.09307073916632971 -0.1321108634591744 -0.1241786723386648
--newton-steps 8 --backtracks 20
--candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14
```

The four input paths and fresh `--out .../resonance` are supplied by the existing request-driven command builder. Original intermediate failures, every tried candidate, final status, circle-reference file, scalar audit, command, logs, and prior status are preserved under the same artifact naming scheme. The new binding receipt is `request78-input-and-source-identity.json`.

## 5. Completion scope and source-only checks

As in [R259](../results/R259-small-core-homotopy-and-resonance-conditions.md) and the [original diagnostic interface](2026-11-14-small-core-resonance-diagnostic-interface.md), a small low-mode candidate would still leave high-mode nonresonance, a justified nonzero-amplitude continuation, and the original full nonlinear/native/geometry acceptance work outstanding. The diagnostic does not prove transversality, perform high-free-core Schur elimination, exclude weighted homotopy paths, or satisfy the large-amplitude goal. A workflow success only means the requested diagnostic completed.

The preparation verified all 68 local source hashes, retained the four original input descriptors and runtime exactly, checked the prior original JSON and source/input ledgers, parsed every pinned Python source, parsed four inline Python blocks, and ran `bash -n` on seven existing shell steps. The original single trigger and concurrency policy are unchanged. The source's supported backtrack guard was inspected as syntax; no scientific module was imported. The detailed source-only receipt is `request78-static-check.json`.

If all twenty trials are rejected, the source preserves that actual evidence and stops the candidate search. No fallback alters the merit rule, parameter domain, tolerance, full right residual, or original BVP/native gates.
