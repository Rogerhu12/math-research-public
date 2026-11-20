# R967 execution contract: original kappa scale at two new coordinates

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

This is a new finite verification of the exact identities proved in [R965](../results/R965-exact-original-trace-calibration-of-the-Igusa-height-coefficient.md). It is not a repeat of R963's trace or moment calculation, and is not an all-prime nonvanishing claim. Actual mathematical execution is restricted to this public repository's Actions.

## Frozen inputs and new work

The consumer is `scripts/r2_original_kappa_scale_two_prime_consumer.py`, SHA256 `950616f303be3241dafaf3f7ef308c65eda26a08c1f0506e862db6d2e490d2e8`. It hard-locks the primes 1019 and 1031. It consumes R963's original `(H_0,T)` pairs `(531,502)` and `(318,394)`, bound to run44731335315/job136271559447/source efdeebbe23cf971f0d66d39e53964e99a9ccc67c and the published row hash. The old trace/moment routine is not called.

For each prime, build the unchanged normalized Hasse polynomial by its existing recurrence and put
\[
 a(x)=(1-x/4)^{N+1}H^{\mathrm{rev}}(x)/H_N,
 \quad m=(p-2)/3,\quad j=(p^2-1)/3.
\]
Use its canonical degree-at-most-\(m\) coefficient lift in \(\mathbf Z/p^2\mathbf Z[x]\). A direct truncated polynomial power computes
\[
 c=[x^j]\widetilde a^{2p+2}\pmod{p^2},\qquad
 \kappa_p=(c/p)\pmod p.
\]
The program requires \(c\) to be divisible by \(p\). Its validity and lift independence are exactly R960, not a presumed smooth lift for an arbitrary coefficient choice.

Independently compute the original \(g_p=[Q^p](E_4^2/v)\) from the finite eta Euler product for \(\eta(3\tau)^8\), retaining the original \(-16\zeta^2\) oldform coefficient. The odd-product identity and the denominator's constant unit are checked. Also compute \(B_*=[x^{m+1}]a^2\) in \(\mathbf F_p\). Require
\[
 g_p\ne0,\qquad g_p=48B_*,\qquad \kappa_p=-g_pT.
\]
The two finite rows establish only the named checks at these two primes. In particular they do not extend R963's nonvanishing window or identify an original CM target with the Igusa factor.

## Execution and evidence contract

Use `python-flint==0.9.0` in the existing public exact-research workflow. Internal budget is 620 seconds, with a 650-second outer subprocess limit. The script emits a start record, a small eta-stage record before each large power, a completed row for each prime, and a summary with row/prefix/summary SHA256 values. A budget stop or exception must report only the actually completed prefix. Local work is limited to source review, AST parsing, text IO, and hashes; this consumer has not been run locally.

No arrays, raw logs, generated certificates, or artifacts are committed or uploaded. Computation uses memory and stdout; the final receipt will bind the actual public run, job, source commit, finite outputs and hashes after they exist. The current request replaces the already completed R963 request without rerunning it.
