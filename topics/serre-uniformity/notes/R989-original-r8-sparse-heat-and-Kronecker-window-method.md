# R989 method — sparse original heat coefficients and a new r=8 window

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.
Authoring agent: handoff_audit. Mathematical execution: **not yet performed**.

This note proves two finite algorithms for the actual balanced coefficient,
including all indexing and model phases. The first is an online convolution
algorithm for the original Ramanujan flow. The second contracts the original
sigma quotient with its specified first pole, independently of that flow.
It also fixes a new, bounded, publicly executed falsification window.
A completed nonzero window is only a finite result. A verified zero would
disprove the proposed universal nonvanishing of the original complete trace,
not Serre uniformity itself.

## 1. The source and the new index range

Write
\[
E_+:y^2=x^3+1,\qquad \omega=dx/(2y),\qquad
c_n^+=[z^n w^{n-1}]
 \frac{\sigma_+(z+w)}{\sigma_+(z)\sigma_+(w)},
\quad \sigma_+'(0)=1.
\tag{989M.1}
\]
There is no Gaussian shift. The original minus model is
\(E_-:y^2=x^3-1\), with the same differential convention, and has
coefficient \(c_n^-\). For the actual indices \(n\equiv3\pmod6\),
R979/R988 give exactly \(c_n^+=-c_n^-\).

R975 identifies this source with the **full** universal Ramanujan derivation
\[
\mathcal R=\frac{E^2-X}{12}\partial_E
 +\frac{EX-Y}{3}\partial_X
 +\frac{EY-X^2}{2}\partial_Y.
\]
The corresponding integral formal flow, through each degree below \(p\), is
\[
e'=\frac{e^2-x}{12},\quad
x'=\frac{ex-y}{3},\quad
y'=\frac{ey-x^2}{2},\qquad
(e,x,y)(0)=(0,0,864).
\tag{989M.2}
\]
The independent variable in this flow is called \(T\); it is not silently
identified with a complex Cayley parameter or a ring-class uniformizer.
The factor \(+864\) belongs to \(E_+\), since
\(g_2=X/12\), \(g_3=-Y/216=-4\).

For \(1\le n<p\), R975's exact source comparison is
\[
\boxed{\qquad
c_n^+=\frac{[T^{n-1}]e(T)}{12n!}\pmod p.
\qquad}
\tag{989M.3}
\]
Indeed the ordinary Taylor coefficient of the flow is
\(\mathcal R^{n-1}E/(n-1)!\); the other factorial and the factor
\(12\) remain in (989M.3). All denominators used here are units.

The new window is precisely
\[
1000<p\le20000,\qquad p\text{ prime},\qquad
p\equiv5\pmod{12},\qquad p\bmod9\in\{2,5\}.
\tag{989M.4}
\]
Thus \(r=8\), \(n=p-8\), and \(n\equiv3\pmod6\). The requested
prime list will be generated exactly by a sieve in the public runner, and
the complete list and its hash will be printed before mathematical work.
No prime count or successful completion is assumed in advance.

The coverage audit uses the actual R939 receipt: its original complete
trace window is \(109\le p\le1000\), both rows, after excluding R936's
six old points. R973/R983 use only \(41,47,227,857\), also below this
window. R963 covers \(1000<p\le10^5\) **only in the r=2 row**
\(p\equiv11\pmod{12}\). Therefore these registered data have empty
intersection with (989M.4). The consumer will record those exclusions
explicitly and reject a lower bound below \(1000\); it will not rerun
the old r=2 window or the four old balanced coefficients. If additional
coverage is registered before execution, the frozen request must subtract
it rather than relabel it as new.

R988, with the original \(\eta\), arithmetic Artin character, and
\(\beta=E_{p+1}(E_+,\omega)/12\), gives
\[
\gamma_1=-\frac{24}{8!}\,
 \overline\eta^{-(m-b)}(\chi(\sigma)-1)\beta^7 c_{p-8}^+.
\tag{989M.5}
\]
Every displayed factor outside \(c_{p-8}^+\) is a proved unit. Hence
\(c_{p-8}^+=0\) if and only if the **original complete**
supersingular trace vanishes. This criterion does not identify that trace
with a specified same-label \(Q'_h(0)\); R945's actual counterexamples
to that further identification remain in force.

## 2. The exact mu_3 sparsity and a three-series recurrence

Give \(T,e,x,y\) respective characters \(1,2,1,0\) modulo \(3\).
The three equations (989M.2) respect these characters. Uniqueness of their
coefficient solution (division only by indices below \(p\)) therefore
gives
\[
e(T)=T^2 a(u),\qquad x(T)=T b(u),\qquad y(T)=c(u),
\qquad u=T^3.
\tag{989M.6}
\]
One can equivalently prove this by induction in the three original ODEs;
it does not require a primitive cube root in \(\mathbb F_p\).
Their constant coefficients are
\[
a_0=12,\qquad b_0=-288,\qquad c_0=864.
\]
For \(j\ge1\), the exact triangular recurrence is
\[
\begin{aligned}
c_j&=\frac{[u^{j-1}](ac-b^2)}{6j},\\
b_j&=\frac{[u^{j-1}]ab-c_j}{9j+3},\\
a_j&=\frac{[u^{j-1}]a^2-b_j}{36j+24}.
\end{aligned}
\tag{989M.7}
\]
For example the first equation follows from
\(3T^2c'(u)=T^2(ac-b^2)/2\); the other two follow by matching
\(x'=b+3ub'\) and \(e'=T(2a+3ua')\).
No coefficient on the right of a product has index \(j\), so the
ordering in (989M.7) determines the three new coefficients uniquely.

For any \(3\mid n<p\), put \(M=(n-3)/3\). Then
\[
c_n^+=\frac{a_M}{12n!}.
\tag{989M.8}
\]
All denominators in (989M.7) through index \(M\) are units:
\(j<p\), \(3j+1\le n-2<p\), and \(3j+2\le n-1<p\).
This supplies the exact admissible truncation rather than an infinite
characteristic-p solution across the first resonant degree.

## 3. One scalar recurrence with only two convolutions

Eliminate \(x,y\) from the actual three equations:
\[
x=e^2-12e',\qquad
y=e^3-18ee'+36e'',\qquad
e'''=e e''-\frac32(e')^2.
\tag{989M.9}
\]
To verify the last equation, differentiate the middle identity and use
\(y'=(ey-x^2)/2\). The terms \(3e^2e'\) cancel and leave
\(36e'''=36ee''-54(e')^2\). Thus this scalar equation retains
the source (989M.2); it is not a conjectured recurrence fitted to data.
Its initial conditions are \(e(0)=e'(0)=0\), \(e''(0)=24\).
Conversely (989M.9) reconstructs the three equations with their stated
initial values, through the same range of invertible Taylor indices.

Substitute \(e=T^2a(u)\). Direct differentiation gives
\[
27u^2a'''+108ua''+60a'
 =-4a^2+9u^2aa''-\frac{27}{2}u^2(a')^2.
\tag{989M.10}
\]
Set
\[
A_j=[u^j]a(u)^2,\qquad
V_j=[u^j](u a'(u))^2.
\]
Symmetry of the product gives
\[
[u^j]u^2aa''
=\frac{j(j-1)}2 A_j-V_j.
\]
The coefficient of \(a_{j+1}\) on the left of (989M.10) is
\(3(j+1)(3j+4)(3j+5)\). Therefore
\[
\boxed{\qquad
a_0=12,\qquad
a_{j+1}=
\frac{(9j^2-9j-8)A_j-45V_j}
 {6(j+1)(3j+4)(3j+5)}.
\qquad}
\tag{989M.11}
\]
The two products involve only the known coefficients through \(a_j\).
Their weighting is the **global** index: the second input sequence is
\(v_i=i a_i\), including \(v_0=0\).

Only \(0\le j<M\) is needed. The largest denominator factor of
the form \(3j+5\) is \(3M+2=n-1<p\). Hence every displayed
division is legitimate. As source calibrations over \(\mathbb Q\),
(989M.11) gives
\(a_1=-48/5\), \(a_2=96/35\), and thereby the already established
\(c_6^+=-1/900\), \(9!c_9^+=8/35\).
These paper identities are not extra finite-prime runs.

For the present r=8 row, Wilson's formula yields the especially short
final extraction
\[
\boxed{\qquad
c_{p-8}^+=420\,a_{(p-11)/3}\pmod p.
\qquad}
\tag{989M.12}
\]
Indeed \((p-8)!=1/7!\pmod p\), and \(7!/12=420\).
The multiplier is a unit for all primes in (989M.4).

## 4. CDQ evaluation: all pair ownership and all shifts

Here CDQ means a divide-and-conquer evaluation of a causal convolution
recurrence. The following proof fixes the algorithm completely.
The targets are the coefficient indices \(n=0,\ldots,M\).
For \(n>0\), the two sums needed to determine \(a_n\) are
\[
\sum_{i+j=n-1}a_i a_j,
\qquad
\sum_{i+j=n-1}(i a_i)(j a_j).
\tag{989M.13}
\]
Both inputs precede their target since \(i+j+1>\max(i,j)\).
Maintain two accumulators at each target index \(n\). To solve
an interval \([l,r)\), choose \(h=\lfloor(l+r)/2\rfloor\):

1. Solve the left interval \([l,h)\).
2. Add its newly determined contributions to targets \(n\in[h,r)\).
3. Solve the right interval \([h,r)\).

At a leaf \(n=0\), set \(a_0=12\). At any other leaf, apply
(989M.11), with \(j=n-1\), to its completed accumulators.

For either sequence \(w_i=a_i\) or \(w_i=i a_i\), the precise
polynomial added at step 2 is
\[
u^l
 \left(\sum_{i=l}^{h-1}w_i u^{i-l}\right)
 \left(\sum_{j=0}^{h-1}w_j u^j
       +\sum_{j=0}^{l-1}w_j u^j\right).
\tag{989M.14}
\]
Its coefficient of \(u^{n-1}\) is added to target \(n\), only
for \(h\le n<r\). The first product counts ordered pairs with
the first index in \([l,h)\) and the other below \(h\). The
second counts the reverse ordered pairs whose other index is below
\(l\). Thus a pair with both indices in the new interval is counted
once for each of its actual orderings, including exactly once on the
diagonal, while a new/old pair receives its two distinct orderings.

More formally, attach an ordered pair \((i,j)\) to the unique
lowest node of the recursion for which \(\max(i,j)\) lies in its
left child and \(i+j+1\) in its right child. Such a node exists
because the latter integer is strictly larger. At that node (989M.14)
counts the pair exactly once. At other nodes either its maximum is
not newly available or its target is not in the right child. This
proves that every accumulator is complete, with no duplicated pair,
when its target leaf is reached.

There is also a necessary truncation for the complexity assertion.
At a node \([l,r)\), only other indices
\[
j\le r-l-2
\]
can contribute, because the new index is at least \(l\) and the
target sum is at most \(r-2\). Thus both prefix sums in (989M.14)
are truncated to length \(r-l-1\); their exponents remain the
**original global indices**, not indices reset at \(l\). Compute
the product only through that length, then add its coefficient
\(n-1-l\). Each node therefore requires two products of length
\(O(r-l)\), not length \(O(r)\).

If \(\mathsf M(d)\) denotes polynomial multiplication cost, the
total is
\(O(\mathsf M(M+1)\log(M+1))\), assuming the usual superlinear
monotonicity of multiplication cost. Memory is \(O(M)\), apart
from recursion and transient products. This is a complexity bound,
not an unmeasured wall-clock promise. Exact finite-field products
are supplied by the documented python-flint `nmod_poly.mul_low`.
All inverses are of the units already bounded above.

## 5. Independent original Kronecker contraction in one product

The independent check starts from **E_-**, with \(g_3=4\), and
does not use (989M.2), (989M.9), any hypergeometric period formula,
or the value to be checked. Consume R973's already proved source:
\[
x(z)=z^{-2}+\sum_{j\ge1}X_j z^{6j-2},\qquad X_1=1/7,
\]
\[
X_j=\frac{\sum_{a=1}^{j-1}X_aX_{j-a}}
 {(6j+1)(j-1)},\qquad
\ell_j=-\frac{X_j}{6j(6j-1)},\qquad
S(z)=\sigma_-(z)/z=\exp\left(\sum_{j\ge1}\ell_jz^{6j}\right).
\tag{989M.15}
\]
Let \(p=6N+5\), \(n=p-8=6t+3\), so \(t=N-1\).
Only \(s_j=[z^{6j}]S\), for \(j\le N\), and
\(b_j=[z^{6j}]S^{-1}\), for \(j\le t\), are computed.
Every denominator in (989M.15) through \(N\) is a unit.
The low \(X_j\) are formed by the displayed original ODE
directly, using ordinary coefficient sums; the CDQ heat recurrence
is not reused to generate them.

For completeness, an exact efficient exponential uses Newton doubling.
If \(s\equiv\exp L\pmod{u^d}\), \(s(0)=1\), then
\[
s_{\rm new}=s(1+L-\log s)\pmod{u^{2d}},\qquad
\log s=\int_0^u s'/s.
\tag{989M.16}
\]
Indeed \(L-\log s\) has order at least \(d\), so its square
vanishes modulo \(u^{2d}\). Integrals have denominators strictly
below \(N+1<p\); the constant is fixed as zero. Polynomial
inversion has constant term one. The inverse prefix is computed
by polynomial inversion, and the exact truncated product
\(S\cdot S^{-1}=1\) is checked. No rational exponential is
evaluated at ramified torsion here.

The actual first-pole constant is the unchanged R574/R973 constant
\[
B=(-1)^{(p-1)/2-(p-2)/3}
   \binom{(p-1)/2}{(p-2)/3}\in\mathbb F_p^\times.
\tag{989M.17}
\]
R973 proves
\(p s_{N+1+j}=-B s_j\pmod p\) throughout the needed range,
and the exact original coefficient is its double sum (973M.7).
Define the finite polynomials
\[
U(u)=\sum_{i=0}^t\frac{b_i}{(n+1-6i)!}u^i,
\qquad
V(u)=\sum_{i=0}^t\frac{b_i}{(n-6i)!}u^i,
\quad C(u)=U(u)V(u).
\tag{989M.18}
\]
All factorial arguments are strictly between zero and \(p\):
their minima in this row are \(4\) and \(3\), respectively.
For \(0\le k\le2t+1\), put
\[
W_k=\begin{cases}
s_k(6k+1)!,&k\le N,\\
B s_{k-N-1}(6k+1-p)!,&k>N.
\end{cases}
\tag{989M.19}
\]
Then the independent exact reduction is
\[
\boxed{\qquad
c_n^-=\sum_{k=0}^{2t+1} C_{2t+1-k}W_k\pmod p.
\qquad}
\tag{989M.20}
\]
Undefined coefficients of \(C\) are zero, so the \(k=0\) endpoint
has no accidental contribution.

Here is the full single-carry verification of (989M.20).
For the term indexed by \((i,j)\) in R973, write
\(k=2t+1-i-j\), \(A=n+1-6i\), \(D=n-6j\).
Then \(A+D=6k+1\), and \(0<A,D<p\).
If \(k\le N\), the binomial is simply
\((6k+1)!/(A!D!)\) in \(\mathbb F_p\).
If \(k>N\), write \(6k+1=p+h\), with \(0<h<p\).
The integer binomial has exactly one factor of \(p\), and Wilson gives
\[
\frac1p\binom{p+h}{A}
\equiv-\frac{h!}{A!D!}\pmod p.
\]
Multiplying by the original pole residue \(-B s_{k-N-1}\)
cancels this minus sign. These are exactly the two cases (989M.19).
Grouping terms with the same \(i+j\) proves (989M.20), with
every source summand and each carry retained.

The whole calculation uses finite-field exact arithmetic. Its final
comparison is \(c_n^+=-c_n^-\), not equality without the model
phase. The direct \(X_j\) recurrence costs \(O(N^2)\) only
for the selected check points or the first zero, not for every prime
in the window. The exponential, inverse, and single contraction use
fast polynomial operations. Thus a large exact rational sigma prefix
and the original quadratic double sum are unnecessary.

## 6. Public execution contract and honest stopping states

The intended consumer is
`scripts/original_r8_balanced_new_window.py`.
All mathematical code must refuse execution unless
`GITHUB_ACTIONS=true` and
`GITHUB_REPOSITORY=Rogerhu12/math-research-public`.
The exact runtime is python-flint 0.9.0. Local review is limited to
paper proofs, file I/O, AST parsing, and hashes.

The separately proved and independently reviewed
[R990](../results/R990-original-hypergeometric-fixed-r-coefficient.md)
supplies the main window channel. For
\(k=\lfloor p/12\rfloor\), \(m=(p-8)/3\), its exact inputs are
\[
B_0=1,\quad
B_i=B_{i-1}\frac{(i-1-k)(3k+3i+1)}{i(3i+1)},\quad 1\le i\le k,
\]
\[
H=((1-z)B^2)^{-1},\qquad
f_i=H_i/(1-3i)\quad(0\le i\le m),\qquad
Q=4+12zB'/B-z/(1-z),
\]
\[
c_{p-8}^+=1260(-32)^m[z^m]Qf^{-8}\pmod p.
\tag{989M.21}
\]
The actual source proof is R990, not agreement of the finite window.
The consumer checks its frozen SHA256
`5c35e72804eee83dde2c74af68232dea3a57c5d97ba39026a07329a7db25a7a1`.
It computes the rational \(H\) through the first resonance
\(\ell=(p+1)/3\) and checks R990's exact
\(H_\ell=B(1)^{-2}\); it divides by \(1-3i\) only through
\(m=\ell-3\). The nonzero resonance coefficient is not substituted
for the different desired coefficient.
The CDQ algorithm (989M.11)–(989M.14) remains a separate source channel.
The original sigma contraction (989M.15)–(989M.20) is independent
of both and is mandatory at the following points:

- the first two eligible **new** primes in the window;
- the first prime with a main-channel zero, before any certified-zero
  claim or successful early termination.

At those same points the CDQ heat coefficient is also compared.
Each point is computed only once per channel and may satisfy more than
one of these conditions. Failure of equality is a source/implementation
failure, not a mathematical zero and not a successful window.

The public scan is in increasing prime order, stops at the first
**independently verified** zero, and otherwise must complete the entire
specified difference set. It has a strict maximum 620-second wall-clock
budget enforced by a parent process. No tail can be dropped to manufacture
a successful final record. The only successful terminal states are:

1. `complete_nonzero_window`: every requested new prime was computed,
   required independent checks passed, and all targets are nonzero;
2. `first_zero_verified`: a zero was verified in the original sigma
   quotient and the independent heat channel, all earlier requested
   primes were nonzero, and the unattempted tail is explicitly listed.

Budget exhaustion, an unfinished zero check, an arithmetic disagreement,
or a worker failure produces a non-success terminal state and lists the
completed prefix, any provisional zero, and the entire uncompleted tail.
The script must not print a fabricated `FINAL` or call a truncated prefix
the complete window. A zero remains a legitimate mathematical result;
it is not filtered from output or treated as a reason to continue scanning
for a preferred answer.

Stdout contains a deterministic contract record, the exact requested and
excluded sets, one compact row per completed prime, the independent-check
records, and a terminal summary. Hashes of full in-memory source prefixes
permit exact regeneration; raw arrays remain runner scratch and are not
committed, uploaded as artifacts, or copied to a Release. The deterministic
summary and its hash exclude elapsed time; timing is printed separately.
The root reads the actual public log before registering its outcome.

The formal algorithm is quasilinear per prime when the separately proved
fixed-r hypergeometric channel is used; only two or fewer successful
nonzero calibration points need the quadratic original ODE. This makes
the proposed range materially smaller than a naive repeated high-weight
polynomial expansion. Nevertheless the 620-second completion statement
requires the actual public receipt. If implementation review predicts
the bound cannot be met, the request must explicitly reduce the upper
endpoint **before** execution, retaining the same honest stopping rules.

## Sources and boundaries

- [R975](../results/R975-original-balanced-Kronecker-integral-heat-recurrence.md),
  (975.14)–(975.19): the original full Ramanujan source, exact factor
  12, factorials, and integrality.
- [R988](../results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md),
  (988.20)–(988.24): the model phase, exact original high coordinate,
  and the proved equivalence with the complete trace.
- [R973 source contract](R973-original-balanced-Kronecker-four-prime-execution-method.md),
  (973M.4)–(973M.13): the original sigma ODE, complete double sum,
  first-pole scale, and single carry. The new content here is its
  exact single-product contraction and its use at previously uncomputed
  r=8 primes, not a re-registration of those source identities.
- [R939 actual receipt](2026-11-20-R939-window-and-weight34-sigma-receipt.md),
  [R963](../results/R963-original-r2-moment-window-through-100000.md),
  [R973](../results/R973-certified-balanced-Kronecker-coefficients-at-four-primes.md),
  and [R983](../results/R983-certified-pure-Hurwitz-coordinates-and-factorial-model-counterexamples.md):
  the audited previous coverage.
- Official [python-flint nmod_poly 0.9.0 API](https://python-flint.readthedocs.io/en/latest/nmod_poly.html):
  exact `mul_low`, `inverse_series_trunc`, `pow_trunc`, and coefficient
  operations. Newton exponential (989M.16) is explicitly implemented;
  no nonexistent `nmod_poly.exp_series_trunc` method is assumed.

No statement here proves the all-prime balanced unit assertion, an
uncomputed first zero, any chosen same-label \(Q'_h\) unit, or the
topic's final completion criterion.
