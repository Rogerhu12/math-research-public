# R993 method — two new original rows and a verified first-zero contract

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.
Authoring agent: handoff_audit. **Status: proved algorithm and execution contract; not executed.**

This is one explicitly bounded falsification attempt for the open all-prime unit assertion. It consumes the proved R989/R990 formulas. The new algorithmic ingredient is a fast independent original sigma ODE, checked against its entire defining differential equation. No old window is repeated.

## 1. Exact difference sets and unchanged source

The requested sets are
\[
\begin{aligned}
\mathcal P_8&=\{p:20000<p\le200000,\ p\text{ prime},\
 p\equiv5\pmod{12},\ p\bmod9\in\{2,5\}\},\\
\mathcal P_2&=\{p:100000<p\le200000,\ p\text{ prime},\
 p\equiv11\pmod{12},\ p\bmod9\in\{2,5\}\}.
\end{aligned}
\tag{993M.1}
\]
R991 completed the entire original r=8 window through 20000, and R963 completed the entire original r=2 window through 100000. Earlier R936/R939 and R973/R983 data are below these new lower endpoints. The two new rows are themselves disjoint modulo 12.

An exact sieve in the public runner supplies both lists and their **increasing merged order**. The lists and hashes are printed before evaluation. The upper endpoint is fixed at 200000; no adaptive extension is included. The first two primes in each row, if reached, receive all three source checks. Every first zero also receives all three before a successful zero claim. A point fulfilling both requirements is checked once.

The target is precisely
\[
E_+:y^2=x^3+1,\quad\omega=dx/(2y),\quad
c_n^+=[z^n w^{n-1}]\frac{\sigma_+(z+w)}
 {\sigma_+(z)\sigma_+(w)},\qquad n=p-r,
\tag{993M.2}
\]
with derivative-one canonical sigma and no extra Gaussian. Both rows have \(n\equiv3\pmod6\). The original minus-model phase is \(c_n^+=-c_n^-\). R988 proves
\[
c_{p-r}^+=0\quad\Longleftrightarrow\quad S_{\rm orig}=0.
\tag{993M.3}
\]
Thus a verified zero changes the proposed nonvanishing of the original complete supersingular trace. It does not disprove Serre uniformity or assert failure of every same-label \(Q'_h\).

## 2. Both fixed-r denominator boundaries

R990 gives
\[
k=\lfloor p/12\rfloor,\quad m=(p-r)/3,\quad
\ell=(p+1)/3,\quad b=(r+1)/3,\quad m=\ell-b<\ell.
\]
Explicitly,
\[
\begin{array}{c|c|c|c}
p&r&m&\ell\\ \hline
12k+5&8&4k-1&4k+2\\
12k+11&2&4k+3&4k+4
\end{array}.
\tag{993M.4}
\]
The actual polynomial and series are
\[
B_0=1,\quad
B_i=B_{i-1}\frac{(i-1-k)(3k+3i+1)}{i(3i+1)}
\quad(1\le i\le k),
\]
\[
H=((1-z)B^2)^{-1},\quad f_i=H_i/(1-3i)\ (0\le i\le m),
\]
\[
Q=4+12zB'/B-z/(1-z),\qquad J_{p,r}=[z^m]Qf^{-r}.
\tag{993M.5}
\]
All inversions have constant term one. The denominator \(1-3i\) first vanishes at \(i=\ell\), which is never used. The rational series \(H\), involving no such division, is computed through \(\ell\) and checked against \(H_\ell=B(1)^{-2}\). That resonance unit is not substituted for \(J_{p,r}\).

The exact extraction is
\[
\boxed{\quad c_{p-r}^+
 =\frac{(-32)^m(r-1)!}{4}J_{p,r}\pmod p.\quad}
\tag{993M.6}
\]
The scale is \((-32)^m/4\) in row 2 and \(1260(-32)^m\) in row 8. Its proof is the actual Ramanujan parametrization and Lagrange extraction in R990, not the prior observed row-8 agreement. Row 2 has the proved integrality endpoint \(3m+1=p-1<p\), including the last needed coefficient of \(A'\).

## 3. Independent original Chazy channel with explicit r

R975/R989 start from
\[
e'=(e^2-x)/12,\quad x'=(ex-y)/3,\quad y'=(ey-x^2)/2,
\quad(e,x,y)(0)=(0,0,864).
\]
Writing \(e(T)=T^2a(T^3)\), they prove
\[
a_0=12,\qquad
a_{j+1}=
\frac{(9j^2-9j-8)[u^j]a^2-45[u^j](u a')^2}
 {6(j+1)(3j+4)(3j+5)}.
\tag{993M.7}
\]
Set \(M=(p-r-3)/3=m-1\). Only \(a_0,\ldots,a_M\) are required, and the largest denominator index is \(3M+2=p-r-1<p\). The second convolution uses the global weighted sequence \(v_i=ia_i\).

The R989 CDQ proof applies directly. At a node \([l,r_0)\), midpoint \(h\), the square increment for a sequence \(v\) is
\[
u^l\left(\sum_{i=l}^{h-1}v_i u^{i-l}\right)
 \left(\sum_{j=0}^{h-1}v_j u^j+\sum_{j=0}^{l-1}v_j u^j\right).
\tag{993M.8}
\]
Only targets in the right child receive its coefficient of degree target minus one. Each ordered pair is assigned once at the unique node separating its maximum input index from the larger target. Prefixes are truncated to length \(r_0-l-1\), preserving their global exponents. The same update is used for \(a\).

R989's source formula \(c_n^+=a_M/(12n!)\) and Wilson give the distinct original terminal scales
\[
\boxed{\quad
c_{p-2}^+=a_{(p-5)/3}/12,\qquad
c_{p-8}^+=420a_{(p-11)/3}.
\quad}
\tag{993M.9}
\]
The new functions take \(r\) explicitly and verify its residue class and new lower endpoint. They never change the old consumer's global row constant or relax its contract.

## 4. Fast independent original sigma prefix

This channel starts on the original negative model:
\[
E_-:y^2=x^3-1,\quad\omega=dx/(2y),\quad
x(z)=z^{-2}+\sum_{j\ge1}X_jz^{6j-2},\qquad X_1=1/7.
\]
The original R973 ODE gives
\[
X_j=\frac{\sum_{a=1}^{j-1}X_aX_{j-a}}{(6j+1)(j-1)}
\quad(j\ge2).
\tag{993M.10}
\]
For \(p=6N+5\), only \(X_1,\ldots,X_N\) are needed. Every denominator factor is a unit.

Shift \(y_j=X_{j+1}\), so \(\sum_{a\ge1}X_au^a=u y(u)\). Then the exact equivalent recurrence is
\[
\boxed{\quad y_0=1/7,\qquad
 y_{j+1}=\frac{[u^j]y(u)^2}{(j+1)(6j+13)}.\quad}
\tag{993M.11}
\]
To determine \(y_i\), use the single square update (993M.8), then divide by \(i(6i+7)\). The last index is \(i=N-1\), with \(6i+7=p-4\), so no zero is inverted. The sequence \(y_0,\ldots,y_{N-1}\) gives exactly the original \(X_1,\ldots,X_N\).

Although polynomial multiplication is shared, the mathematical source is independent of the hypergeometric and Chazy channels. After completing this prefix, form \(W(u)=1+\sum_{j=1}^NX_ju^j\). The original differential equation \(x''=6x^2\), with \(u=z^6\), becomes
\[
\boxed{\quad W+uW'+6u^2W''-W^2=0\pmod{u^{N+1}}.\quad}
\tag{993M.12}
\]
The consumer verifies this **entire polynomial residual** using independent derivatives and multiplication. With \(W_0=1\) and \(X_1=1/7\), its coefficient at each \(j\ge2\) is (993M.10), with a unit leading factor. Hence it characterizes the unique original prefix. A shared CDQ error cannot be accepted just because two final targets agree.

Next use the unchanged original identities
\[
\ell_j=-X_j/(6j(6j-1)),\qquad
S=\exp\left(\sum_{j=1}^N\ell_j u^j\right)\pmod{u^{N+1}},
\qquad S^{-1}\pmod{u^{N+1}}.
\tag{993M.13}
\]
The frozen R989 Newton exponential is reused unchanged: \(S\gets S(1+\ell-\log S)\) at doubled precision. All integration indices are below \(p\). The complete truncated checks \(S'=\ell'S\), \(SS^{-1}=1\), and the original phase \(s_1=-1/210\) are retained.

This independent prefix costs \(O(\mathsf M(N)\log N)\), followed by quasilinear exponential and inverse operations. It uses neither a quadratic point loop nor a high-pole rational prefix.

## 5. Single-carry contraction in both rows

Let \(t=(n-3)/6\). Then \(t=N\) in row 2 and \(t=N-1\) in row 8. Retain the original constant
\[
B_{\rm old}=(-1)^{(p-1)/2-(p-2)/3}
 \binom{(p-1)/2}{(p-2)/3}\ne0.
\tag{993M.14}
\]
R973 proves \(p s_{N+1+j}=-B_{\rm old}s_j\pmod p\), for \(0\le j\le N\). Put \(s_i=S_i\), \(b_i=(S^{-1})_i\) and
\[
U_i=b_i/(n+1-6i)!,\quad V_i=b_i/(n-6i)!\quad(0\le i\le t),
\qquad C=UV,
\]
\[
w_{k_0}=
\begin{cases}
s_{k_0}(6k_0+1)!,&k_0\le N,\\
B_{\rm old}s_{k_0-N-1}(6k_0+1-p)!,&k_0>N.
\end{cases}
\]
Then the exact original value is
\[
\boxed{\quad c_n^-=\sum_{k_0=0}^{2t+1}C_{2t+1-k_0}w_{k_0},
\qquad c_n^+=-c_n^-.\quad}
\tag{993M.15}
\]
This is the proved single-product contraction of the complete R973 double sum, with out-of-range coefficients of \(C\) equal to zero.

The bounds also cover the new row 2. The smallest factorial arguments in \(U,V\) are 4 and 3; the maxima are \(n+1\le p-1\) and \(n\le p-2\). The highest sigma index is \(2N+1\) in row 2, inside the exact first-pole range, and \(2N-1\) in row 8. A high binomial top is \(p+h\), with \(0<h\le p-3\) in row 2 and \(0<h\le p-15\) in row 8. Its two lower factorial indices are positive and below \(p\), so
\[
\binom{p+h}{A}/p=-h!/(A!(p+h-A)!)\pmod p.
\]
This minus sign cancels the original pole minus sign, giving the positive high term in (993M.15). Only inverse-sigma coefficients through \(t\le N\) are used.

## 6. Isolation, pins, timing and terminal semantics

The new consumer is 'scripts/original_balanced_combined_disjoint_window.py'. The old R989 script is unchanged. After verifying its exact SHA256, the new worker imports only the row-independent helpers 'inverses', 'coefficients', and 'exp_series_from_log'. It never calls the old main, worker, or row-8 coefficient functions, and never overwrites any old constant.

The new method and script, the frozen R989 script and method, R990, R975, R988, the R973 source contract, and the R963/R991 coverage receipts are pinned in the request. The old dependencies additionally have exact expected hashes inside the new consumer. Runtime is python-flint 0.9.0. Before any mathematical work, including the sieve, require 'GITHUB_ACTIONS=true' and repository 'Rogerhu12/math-research-public'. Local review is only paper proofs, I/O, AST parsing and hashes.

Every main-channel prime uses \(O(\mathsf M(p))\) field operations and \(O(p)\) memory. The first two reached primes per row and a possible first zero additionally use the two quasilinear independent channels above. There are no \(p^2\)-length arrays or quadratic prefix recurrences. R991 measured 1.999 seconds for its 349 smaller new primes; this is a runtime reference, not a time theorem for the larger request. The fixed 620-second guard governs the actual experiment.

The 620-second wall-clock interval starts before source hashing and the sieve. The parent reserves the final 15 seconds for draining/terminating the worker, constructing the exact tail, emitting the summary and writing the scratch payload. It stops collecting new work at the earlier computation deadline, bounds process joins by the remaining total budget, and marks a total-budget overrun as failure. This reserve is part of 620 seconds, not an additional allowance. With a deliberately shorter command-line budget, the reserve is the smaller of 15 seconds and one quarter of that budget. Acceptance additionally requires the final separate budget receipt to say 'within_total_budget=true' and process exit zero. An overrun during even the final I/O receives nonzero exit and cannot be accepted solely from an earlier successful mathematical summary.

The worker emits a provisional zero before independent checks. Only after both checks agree does it emit the certified row and successful first-zero terminal. Budget exhaustion terminates the worker and reports an unfinished zero as unverified. A nonzero completion requires equality of the requested and completed merged lists and all four scheduled calibration points.

The only successful terminal states are:

- 'complete_nonzero_difference_sets': every requested target and scheduled check completed, with no zero;
- 'first_zero_verified': exactly one verified terminal zero, all earlier targets nonzero, and the entire unattempted tail explicitly listed.

Every other termination is a failure or partial result with its actual prefix and full tail. No truncated prefix receives a fabricated FINAL or complete-window label. Zero is a mathematical result, not filtered out as a runtime failure.

Stdout contains deterministic contract, rows, source-prefix hashes and summary. Requested, completed and uncompleted primes are compact integer lists for each row; their increasing merged order is obtained by sorting the disjoint union. No repeated per-prime objects are needed for these lists. The canonical payload is {contract,rows,summary}, encoded with sorted keys and compact separators plus one newline. Timing is separate.

Every JSON event of at most 12000 ASCII bytes is printed directly. A larger event is split into consecutive 4000-character fragments. Each physical JSON log line has kind 'combined_event_chunk', the original event kind, full event byte length and SHA256, zero-based chunk index, total chunk count and 'json_fragment'. The exact assembly protocol is: require all indices once, concatenate fragments in index order, check the ASCII byte length and SHA256, and JSON-decode that string. Fragments are complete data, not omissions; the canonical payload and all hashes always refer to the unfragmented original objects. This prevents long contract/summary lines from losing an uncompleted tail through log-line truncation.

Arrays remain memory/runner scratch; none are committed or uploaded to artifacts or Releases. The root must read the actual public receipt before registering the finite outcome.

## Dependencies and limits

- [R989 method](R989-original-r8-sparse-heat-and-Kronecker-window-method.md): sparse heat, CDQ ownership, original sigma contraction and Newton exponential.
- [R990](../results/R990-original-hypergeometric-fixed-r-coefficient.md): actual source proof for both fixed-r rows.
- [R975](../results/R975-original-balanced-Kronecker-integral-heat-recurrence.md), [R988](../results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md), and [R973 contract](R973-original-balanced-Kronecker-four-prime-execution-method.md): unchanged definitions and exact interpretation.
- [R963](../results/R963-original-r2-moment-window-through-100000.md) and [R991](../results/R991-certified-original-r8-balanced-window-through-20000.md): completed coverage, consumed without recomputation.

Even a complete nonzero result proves only the specified finite cases. The all-prime coefficient, original same-label marked condition, and final Serre-uniformity problem remain separate goals.

