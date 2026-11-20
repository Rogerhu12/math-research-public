# R967: certified original kappa and weak-unit scale at two primes

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

**Status: completed finite public computation.** At exactly \(p=1019,1031\), a direct polynomial power modulo \(p^2\) gives the original secondary height coefficient \(\kappa_p\). An independent eta-product computation gives the original weak coefficient \(g_p\). Both R965 identities \(g_p=48B_*\) and \(\kappa_p=-g_pT\) hold with the unchanged original normalization. The old values of \(T\) are consumed from R963 and are not recomputed.

This result certifies two new computations of the comparison scale. It neither extends R963's nonvanishing window nor proves a uniform nonvanishing theorem or the same-label normal coefficient.

## 1. Public execution and frozen source

- Run: [44735075802](https://github.com/Rogerhu12/math-research-public/actions/runs/44735075802), conclusion **success**.
- Job: [136284299120](https://github.com/Rogerhu12/math-research-public/actions/runs/44735075802/job/136284299120), all steps successful.
- Source commit: `615047a18e76d0632fba87a074f2f30603bbd96c`.
- Consumer: [r2_original_kappa_scale_two_prime_consumer.py](../scripts/r2_original_kappa_scale_two_prime_consumer.py), SHA256 `950616f303be3241dafaf3f7ef308c65eda26a08c1f0506e862db6d2e490d2e8`.
- Contract: [R967 execution method](../notes/R967-original-kappa-scale-two-prime-execution-method.md), SHA256 `1704aea1c0e88d9489218b63e445cc86aa63a3808cf43b7fecaab799ccf863a5`.
- Runtime: `python-flint==0.9.0`; internal budget 620 seconds, outer subprocess limit 650 seconds.

The start record binds the actual source commit, run, runtime, script hash and the R963 source rows. The execution completed both requested primes in **2.732445 seconds**. There was no exception, incomplete prime, budget stop or uncompleted tail.

## 2. The new independent arithmetic

For the unchanged Hasse polynomial, put
\[
p=6N+5,\quad m=2N+1,\quad
a(x)=(1-x/4)^{N+1}H^{\rm rev}(x)/H_N,\quad
j=(p^2-1)/3.
\]
The actual lift uses the canonical integer representatives \(0,\ldots,p-1\) of the coefficients of \(a\), retaining degree at most \(m\). R960 proves that this arithmetic lift is permitted for the coefficient and that the resulting division by \(p\) is lift-independent. No smooth-lift assertion for arbitrary coefficient choices is used.

The consumer directly computes
\[
c=[x^j]\widetilde a(x)^{2p+2}\pmod{p^2},\qquad
\kappa_p=c/p\pmod p,
\]
checks \(p\mid c\), and separately computes
\[
B_*=[x^{m+1}]a(x)^2.
\]
The power modulo \(p^2\) is evaluated independently of the previously computed \(T\).

The other independent calculation starts from the exact CM form
\[
F_4(\tau)=\eta(3\tau)^8,\qquad
v(Q)=F_4(Q)-16\zeta^2F_4(Q^4).
\]
For \(P(X)=\prod_{n\ge1}(1-X^n)^8\) and \(q=Q^6\), write
\[
A(q)=\sum_{j\ge0}P_{2j}q^j,\qquad B(q)=8P(q^2).
\]
The checked identity \(P(X)_{\rm odd}=-8XP(X^4)\), together with
\(-16\zeta^2=8(1+s)\), gives the original phase
\[
v(Q)=Q\bigl(A(q)+sQ^3B(q)\bigr),\qquad s^2=-3.
\]
Consequently the actual weak Fourier coefficient is
\[
g_p=[Q^p]\frac{E_4(Q^6)^2}{v(Q)}
=[q^{N+1}]
\frac{E_4(q)^2A(q)}{A(q)^2+3qB(q)^2}.
\]
The denominator has constant term one. This calculation does not define \(g_p\) using \(B_*\) or the target identity.

## 3. Complete finite results

All values below are the recorded original-field scalars, with residues represented by integers between zero and \(p-1\). The coefficient \(c\) is represented between zero and \(p^2-1\).

| \(p\) | \(N\) | \(m\) | \(j\) | consumed \(H_0\) | consumed \(T\) | \(B_*\) | independent \(g_p\) | \(c\bmod p^2\) | direct \(\kappa_p\) | checked \(-g_pT\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1019 | 169 | 339 | 346120 | 531 | 502 | 859 | 472 | 492177 | 483 | 483 |
| 1031 | 171 | 343 | 354320 | 318 | 394 | 651 | 318 | 505190 | 490 | 490 |

The completed row times are 1.650131 and 0.983443 seconds respectively. Each row records successful checks of the original eta oldform phase, \(g_p=48B_*\), divisibility of the direct coefficient by \(p\), and \(\kappa_p=-g_pT\). Both independent weak coefficients and both direct height coefficients are nonzero.

The consumed data are exactly R963 run44731335315/job136271559447/source `efdeebbe23cf971f0d66d39e53964e99a9ccc67c`, whose arithmetic-row SHA256 is `26009267ff3ae699f724fe79d98c0ccabdaf0a81b0dfe41abeb72636cb16cdd5`. The consumer contains the two required rows explicitly and calls no old moment or trace routine.

## 4. Evidence integrity and scope

The root session read the actual job logs and independently verified the three hashes by pure JSON/text IO. This audit executed no mathematical consumer.

| Record | Verified SHA256 |
|---|---|
| Canonical arithmetic rows, without timing/event fields | `053d6dd2718cd4eff677b42b9e2b540ff5d617edc775853b0cb820cf52279069` |
| Canonical stdout records before the summary | `68912a0d629c0d9ae3419af5a31f784fc459516641d645761cdaafb89420fee8` |
| Summary payload before its own hash field | `1fbf36c9ac4fde09dfef03628373500daee8888ec8b042b7cea2d22901d519bc` |

The stdout contains six records: start, eta stage and completed row for each prime, then summary. The public job installed the pinned runtime, checked the README and script hashes, and ran the frozen request successfully. No raw log, array, generated certificate or artifact is stored in Git or Releases.

The two values agree with R965's independently proved exact identity and with R960's original-coordinate coefficient. They do not replace those proofs. They also do not make the actual Igusa factor the original CM target, eliminate R945's complete-trace-to-normal obstruction, or close the absolute Serre-uniformity goal.
