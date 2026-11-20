# R963 execution method: new original r=2 moment window

2026-11-20. This is an execution contract, not a mathematical result.

The previously completed R936/R939 window through 1000 is reused and is excluded by the consumer. The new request covers only primes `1000 < p <= 100000` with `p = 11 mod 12` and `p = 2 or 5 mod 9`. The first zero stops the scan. A 620-second internal budget leaves time before the workflow's 650-second outer deadline; an incomplete interval is reported explicitly.

The frozen consumer is `scripts/r2_original_moment_new_window.py`, SHA256 `a3af15c40c8206dc62b266febe2710d941a877529df270ec1c663cce57d00aa5`. It uses the pinned binary wheel `python-flint==0.9.0`. Only AST parsing, text review and hashing are performed outside public Actions.

It consumes the original formulas in R939 and R958. With `p=6N+5`, it keeps the original Hasse normalization `H(0)=3(3N+2)!/((2N+1)!N!2^N)` and solves the negative-right-side equation for `C0=C/s`. Since `s^p=-s`, the true input is `R_F/s=+2 D^(2N+1) beta^2 C0^p mod tH`. Only the quotient modulus is made monic. The trace retains the `t=0` weight one, the H-root weight three and the original fine-cover factor.

For each prime the consumer verifies the Hasse ODE, the original C equation, `beta'=-H/3`, the full quotient's étaleness, Baker's denominator identity, the idempotent, and the exact independent trace comparison

`T=(3/2)(c_mom/s)(ell_N(R_F)/s)`, `S^p=432T=648(c_mom/s)(ell_N(R_F)/s)`.

At a zero it constructs the complete opposite-deck polynomial `Ktilde` and checks the literal polynomial equality `L_- Ktilde=R_F/s`. Then the original form `s u^2 D^(N+1) Ktilde(t)` is an actual Cartier preimage of F. Such a zero would refute the no-exception auxiliary moment claim, not Serre uniformity itself. A separate independent calculation must verify any newly found zero before its mathematical registration.

The JSONL stdout contains a start record, compact per-prime original values, a complete certificate only at the first zero, and a final summary. The summary hashes arithmetic rows, the certificate if present, the stdout prefix, and the uncompleted prime list. A persistent subprocess permits a truthful budget summary even if a polynomial operation is interrupted. No raw arrays or regenerated outputs are committed or released; this request uses no artifact upload.

Runtime API reference: [official python-flint 0.9.0 nmod_poly documentation](https://python-flint.readthedocs.io/en/latest/nmod_poly.html), including monic gcd, inverse series and `pow_mod` with a reversed-modulus inverse. The actual run ID, source SHA, outcome and finite coverage will be recorded from the public Actions receipt.
