# R969 execution contract — the actual filtered full-level span at three primes

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: frozen exact test contract, reviewed by the root session; actual execution pending.**
This document specifies the new consumer
`scripts/full_level_critical_hasse_span_three_prime_consumer.py`.
It does not assert that the tested inclusion is true. All arithmetic is
restricted to this public repository's GitHub Actions. Locally, the script
is only read, parsed as an AST and hashed.

Frozen consumer SHA256: `5bb625faec68b4276677213e948456df188af75c94f1fab9121946088790445a`. The current request uses only `--budget-seconds 240`, with stdout and no output file or artifact. R968 source proof SHA256: `186efc0cb109befcce458f931779802027d30193cfec687131f8fda5e10ccaaa`.

## 1. The precise new question

For each of the fixed primes
$$
p\in\{113,131,227\},\qquad p=6N+5,
$$
use the actual R968 forms
$$
Z_i=Z_{6i+4,\,6(N-1-i)+1}\in M_{p-5}(\mathbf F_p),
\qquad 0\le i<N,
$$
and the unchanged weights
$$
w_i=\mathbf1_{(6i+7,p+1)=1}P_{6i+6}(1/s),\qquad s^2=-3.
$$
The test is precisely
$$
\boxed{\quad A/E_4\ \stackrel{?}{\in}\
\operatorname{span}_{\mathbf F_p}\{w_i Z_i:0\le i<N\}.\quad}
\tag{C1}
$$
Here $A$ is the Hasse invariant, normalized by $A(q)=1$. Its full-level
weight is $p-1$, and its fine zero at $j=0$ is simple. Since $E_4$ has
the same simple fine zero there, $A/E_4$ is a holomorphic form of weight
$p-5$ and has nonzero value at the actual marked point. Equivalently,
the full-level ring in characteristic $p>3$ forces the weight-$p-1$
polynomial to contain $E_4$, because $p-1=4\pmod6$.

If (C1) holds, its exact combination, followed by R968(968.12), proves
that at least one of the original fully filtered same-label products
is nonzero at that particular prime. If (C1) fails, the normalized
annihilator in §4 is an exact counterexample to this proposed *span
criterion at that prime*. Failure does not imply that all original
products vanish.

The prime $113$ is included solely in the general same-label full-level
range $p=5\pmod6$, $p\bmod9\in\{2,5\}$. It is $5\pmod{12}$ and is
**not** represented as an $r=2$, $p=11\pmod{12}$ trace experiment. No
supersingular trace or sigma sequence is recomputed at any of the three
primes.

## 2. One complete CM source, with no fitted coefficients

Put $q=Q^6$, $\zeta^2+\zeta+1=0$ and $s=1+2\zeta$. The unique primary
generator of each ideal coprime to $2s$ is
$$
\beta=a+b\zeta\equiv1\pmod{2s},
$$
which in integer coordinates is exactly
$$
a\text{ odd},\quad b\text{ even},\quad a+b=1\pmod6.
\tag{C2}
$$
Indeed the first two conditions are reduction modulo $2$, and reduction
modulo $s$ gives $a+b=1\pmod3$. The six units map bijectively to the six
units modulo $2s$, so each eligible ideal appears exactly once. Its norm
$a^2-ab+b^2$ is $1\pmod6$.

For all needed differences $d=|a-b|$ of Taylor indices, the script forms
in one batched pass
$$
M_d(q)=\sum_{\beta\equiv1\ (2s)}
 \beta^d q^{(\mathrm N\beta-1)/6}.
\tag{C3}
$$
The lattice bound is the exact norm cutoff $6L+1$, where
$L=\lfloor(p-5)/12\rfloor+2$ is the final Fourier degree. The box
$|a|,|b|\le2\lfloor\sqrt{6L+1}\rfloor+2$ contains every point of this
norm: $a^2-ab+b^2\ge(a^2+b^2)/2$. The script asserts completeness under
conjugation $(a,b)\mapsto(a-b,-b)$ and normalization at norm one.
Conjugation gives rational integer sums in (C3), also checked before
discarding the second coordinate.

For $d=1\pmod6$, this is the original positive finite-character family
$W_{d+1}/Q$. For $d=5\pmod6$, it is the inverse finite-character family
$H_{d+1}^{\rm inv}/Q$. These are the actual R954/R964 families, because
the finite character is absorbed by choosing the primary generator.
The normalized boundary coefficients of R968 are therefore
$$
T_{d,0}=\frac{M_d}{d!\,(\eta^4/Q)}\quad(d=1\pmod6),
\qquad
T_{0,d}=\frac{M_d}{d!\,(\eta^4/Q)}\quad(d=5\pmod6).
\tag{C4}
$$
For the second formula the raw sum initially contains $\bar\beta^d$;
the complete conjugation permutation proves that its sum equals (C3).
The factor six from the unit orbit cancels exactly the factor six in
R968(968.2). Thus no unrecorded sign, factorial or factor six is supplied
by numerical normalization.

All mixed coefficients needed by all columns are filled once, with
memoization, by the proven recurrence
$$
T_{a,b}=
\frac{6q\partial_q T_{a-1,b-1}
 -(a+b-3)E_2T_{a-1,b-1}/2-E_4T_{a-2,b-2}/4}{ab}.
\tag{C5}
$$
Invalid negative indices or $a-b\ne1\pmod6$ give zero. Each individual
index and their required total degree are less than $p$, as in R968 §4.
Hence every division in (C4)–(C5) is by a unit.

The script then uses R968(968.9) verbatim to produce $Z_i$. Its canonical
zeta coefficients are computed directly as
$$
\beta_m=\frac1{(2m)!}
\left(B_{2m}-4m\sum_{n\ge1}\sigma_{2m-1}(n)q^n\right).
\tag{C6}
$$
This retains the weighted Eisenstein series as a whole: a Bernoulli
numerator is never inverted. The exact rational Bernoulli recurrence
is evaluated only in Actions. Every relevant $2m<p-1$; its Bernoulli
denominator and factorial are $p$-units. The source is therefore an
exact finite computation over $\mathbf F_p$, with no sigma interpolation,
high-derivative repetition or floating point arithmetic.

## 3. The complete mask and Fourier coordinates

The polynomial recurrence for $P_n(x)$ is used with $x^2=-1/3$. For
odd $n$ the script stores $P_n(x)/x$, and for even $n$ it stores $P_n(x)$.
All requested $n=h-1=6i+6$ are even and less than $p$. The exact
primitive gcd and the Legendre value are printed for every index. Only
indices with gcd one and nonzero Legendre value are selected. Their
actual columns are $w_iZ_i$, not an enlarged source with either filter
removed.

Set
$$
B=\lfloor(p-5)/12\rfloor=\lfloor N/2\rfloor,
\qquad D=B+1.
$$
The integral full-level basis is
$$
E_6^{N-2r}\Delta^r,\qquad 0\le r\le B.
\tag{C7}
$$
Its leading coefficients at $q^r$ are one. All rows $q^0,\ldots,q^B$
are retained; these are the complete Sturm coordinates, not a selected
submatrix. The consumer computes through $q^{B+2}$, triangularly reduces
every source form and the actual target $1/E_4$ against (C7), and asserts
that the residual vanishes at every coordinate, including the two rows
beyond the mathematical Sturm bound.

The target equality $A/E_4=1/E_4$ in Fourier expansions is an exact
modulo-$p$ identity, rather than a fitted choice of a form with the same
marked value. Its integral basis coordinates and all Sturm coordinates
are printed.

There is one cross-source check, which consumes two already proved
scalars and performs no new sigma calculation. R945 §1 and (945.10)
give, at $p=227$, the original products $f_{18}g_{18}=0$ and
$f_{24}g_{12}=16$. The consumer evaluates the two corresponding new
full-level basis polynomials at $U=-1/1728$ and checks exactly
$$
\left[Z_i/E_6^N\right]_{\rm mark}
=-72(-864)^{-N}f_i g_{N-1-i}.
\tag{C7a}
$$
The zero and nonzero comparisons together check the new Fourier source,
the original marked point and R968's negative period exponent against
the previously established source. The old run and output hash are
included in the report. These two sigma scalars are reused verbatim.

## 4. Exact solve or exact failure witness

Gaussian elimination on all Sturm rows records the row-operation matrix.
If (C1) holds, the consumer returns a sparse list of coefficients
$(i,h,c_i)$ for the actual weighted columns. It checks
$$
\sum_i c_iw_iZ_i=A/E_4
\tag{C8}
$$
at all coordinates through $q^{B+2}$. Sturm's theorem, together with
the proven modular source and target, makes this an exact identity of
modular forms modulo $p$.

If (C1) fails, it returns a row vector $\lambda\in\mathbf F_p^D$ and
checks every exact identity
$$
\lambda(w_iZ_i)=0\quad\text{for all selected }i,
\qquad \lambda(A/E_4)=1.
\tag{C9}
$$
This certifies failure of the proposed inclusion. The full mask, target
coordinates and this normalized separating functional make the output
concrete. The omitted arithmetic arrays are deterministically regenerable
from the source and are summarized by SHA-256. The rank and target
membership for the *unfiltered* source are reported only as separately
labelled diagnostics; they cannot replace the filtered result.

## 5. Execution and output

The only arithmetic command requested is

```text
python topics/serre-uniformity/scripts/full_level_critical_hasse_span_three_prime_consumer.py --budget-seconds 240
```

An optional `--output` may specify a temporary runner path. The workflow
must not commit, upload as an artifact, or preserve the regenerated JSON
or arithmetic arrays. Standard output contains one compact exact report
for each prime, then the deterministic full-report SHA-256 and byte count.
Elapsed time is printed separately and is excluded from all mathematical
report hashes. The report also contains the script's SHA-256. A timeout
or failed source assertion reports an incomplete result and exits with
failure; it never becomes an inclusion result.

The fixed three-prime choice is a test of a precise new structural route.
Either outcome is finite evidence only and does not establish uniform
nonvanishing, the original full trace, or Serre uniformity.

## Dependencies

- R954: the original conductor-$(2s)$ family and finite character.
- R964: the inverse-character companion and its genuine heat relation.
- R966: the complete two-variable source and original same-label filters.
- R968(968.2), (968.6), (968.9), (968.10), (968.12)–(968.16): the exact
  full-level coefficients, integrality, marked comparison and common-factor
  criterion.
- R945 §1 and (945.10): exactly two previously proved original sigma
  products used for the cross-source check (C7a). The existing run is
  `44720732478`; its output hash is retained by the consumer. No original
  sigma recurrence, supersingular trace or pole block is recomputed.
