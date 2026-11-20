# R988 — Original pure-to-balanced Cartier contraction and the actual high trace

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b. Authoring agent: legendre_shift; independently reviewed by root.

**Status: proved exact coefficient comparison and equivalent unit criteria.**
The original pure Hurwitz coefficient of R978 is an explicit unit times
the bare balanced Kronecker coefficient of R974/R975. This makes the
balanced unit criterion equivalent to nonvanishing of the original
complete trace. The comparison itself does not prove either quantity
nonzero for all primes. It retains the actual rational parameter, the
Frobenius in Cartier, the original root and character, and the two CM
model phases. All calculations below are symbolic.

The input identifying the complete rational functions is R987's exact
Cartier gluing identity. That proof controls every origin term. This
note supplies the subsequent coefficient contraction and its original
arithmetic scalars; it does not repeat that gluing argument.

## 1. Original sources and the general comparison

Let \(p\ge41\), \(p\equiv5\pmod6\), and put \(q=p^2\). Fix
\[
E_+:y^2=x^3+1,\qquad \omega=\frac{dx}{2y},\qquad
g_2=0,\quad g_3=-4,
\]
\[
\beta=\frac{\overline{E_{p+1}(E_+,\omega)}}{12}
\in\mathbb F_p^\times.
\tag{988.1}
\]
The differential and the supersingular unit are exactly those of
R978/R980. Write
\[
\log\frac{\sigma_+(z)}z
=-\sum_{N\ge4}\frac{\mathcal G_N}{N}z^N,
\qquad \sigma_+'(0)=1,
\]
\[
\Theta(z,W)=\frac{\sigma_+(z+W)}{\sigma_+(z)\sigma_+(W)},
\qquad c_j^+=[z^jW^{j-1}]\Theta(z,W).
\tag{988.2}
\]
These \(\mathcal G_N\) are the factorial-free pure coefficients of
R978, and the \(c_j^+\) are the bare canonical coefficients on this
same \(E_+\). In particular their values are rational. For \(j<p\),
the balanced coefficients are \(p\)-integral by R975.

The general result is
\[
\boxed{\quad
\overline{\mathcal G_{j(p-1)}}
=-j!\,\beta^{-j}\overline{c_j^+},
\qquad 1\le j\le p-2.
\quad}
\tag{988.3}
\]
Robert's actual reflection then gives
\[
\boxed{\quad
\overline{\mathcal G_{j(p-1)+p+1}}
=-(j-1)!\,\beta^{1-j}\overline{c_j^+},
\qquad 1\le j\le p-2.
\quad}
\tag{988.4}
\]
If \(3\nmid j\), both sides of each identity are zero by the
\(\mu_6\) character: \(\mathcal G_N\) vanishes unless \(6\mid N\),
and \(c_j^+\) vanishes unless \(3\mid j\). The substantive case
below is \(3\mid j\), which in this range has \(j\ge3\).

## 2. The actual rational Cartier source

Let \(k=\mathbb F_{p^2}\), and let \(C\) be Cartier on rational
differentials. Use the original functions of R986:
\[
D=\omega^{-1}d,\qquad Z=-\beta^{-1}D^{p-2}x,
\qquad dZ=\omega,
\]
\[
J=J_s,
\qquad dJ=(-x+\beta t^{p-1})\omega,
\qquad
\mathcal T=Z+\beta^{-1}J^p,
\qquad d\mathcal T=\omega.
\tag{988.5}
\]
Here \(t=-x/y\), and \(J_s\) is the explicitly constructed
square-root-parameter primitive of R986. Its displayed rational
formula in that result fixes the choice. Its local principal part is
\(t^{-1}\) with zero constant coefficient. The function
\(\mathcal T\) is regular at the origin, is a local uniformizer,
and satisfies
\[
\mathcal T(g_s(T))=T+O(T^q)
\tag{988.6}
\]
in the original strict Lubin–Tate parameter. Thus no formal coordinate
is selected merely for convenience in the following extraction.

The actual connection functions are
\[
e^{-\zeta(z)W}\Theta(z,W)
=\sum_{k\ge0}L_k(z)W^{k-1},\qquad L_0=1,\quad L_1=0.
\tag{988.7}
\]
We use the same notation for their reductions. R987 proves their
integral rational reduction for every \(0\le k\le p-1\), and the
complete identity
\[
\frac{C(xZ^k\omega)}{\omega}
=\beta^{1-k}k!L_k,
\qquad 0\le k\le p-1.
\tag{988.8}
\]
In particular the terminal index is part of the input. On this fixed
CM source its integrality uses \(\mathcal G_{p-1}=0\), so the
additional connection coefficient does not require division of a
residue-field zero by \(p\).

For \(0\le m\le p-1\), define the specified rational function
\[
\mathcal B_m=
\sum_{k=0}^m\frac{J^{m-k}}{(m-k)!}L_k.
\tag{988.9}
\]
It is the coefficient of \(W^{m-1}\) in the finite rational kernel
\(e^{JW}\Xi\), where \(\Xi=e^{-\zeta W}\Theta\). The combined
kernel has just the original simple origin pole, as proved in
R984/R986/R987. In particular \(\mathcal B_m\) is regular at the
origin for \(m\ge2\); \(\mathcal B_0=1\) and
\(\mathcal B_1=J\).

Expanding \(\mathcal T^m\) using (988.5) and applying Cartier
semilinearity gives an identity of full rational differentials:
\[
\begin{aligned}
C(x\mathcal T^m\omega)
&=\sum_{k=0}^m\binom mk
\beta^{-(m-k)}J^{m-k}C(xZ^k\omega)\\
&=\beta^{1-m}m!\mathcal B_m\omega.
\end{aligned}
\tag{988.10}
\]
Every factorial is a unit, and \(\beta\) and the binomial
coefficients lie in \(\mathbb F_p\). Formula (988.10) therefore
keeps, rather than suppresses, each Frobenius root in the rule
\(C(a^p\nu)=aC(\nu)\).

## 3. Exact low-index Cartier coordinates

Since \(D\mathcal T=1\), the rational function \(\mathcal T\) is
a \(p\)-basis of \(k(E_+)\). Write uniquely
\[
x=\sum_{i=0}^{p-1}b_i^p\mathcal T^i,
\qquad b_i\in k(E_+).
\tag{988.11}
\]
Multiplying by \(\mathcal T^{p-1-i}\omega\) and applying Cartier
extracts exactly the summand indexed by \(i\). The exponent ranges
from zero to \(2p-2\), whose only value congruent to \(-1\pmod p\)
is \(p-1\). Thus (988.10), with \(m=p-1-i\), proves
\[
\boxed{\quad
b_i=\beta^{1-m}m!\mathcal B_m,
\qquad m=p-1-i.
\quad}
\tag{988.12}
\]
In particular,
\[
\boxed{\begin{aligned}
b_0&=-\beta\mathcal B_{p-1},\\
b_6&=-\frac{\beta^7}{6!}\mathcal B_{p-7},\\
b_{p-2}&=J,\qquad b_{p-1}=\beta.
\end{aligned}}
\tag{988.13}
\]
The two first formulas are exactly the small Cartier indices
\(r-2=0,6\) in the original \(r=2,8\) rows. These are identities
of actual rational functions with the given \(\mathcal T\), rather
than choices of independent coordinates or common proportionality
constants.

The original high coefficient can already be read from (988.11).
Let \(n=p-r\), \(N=n(p-1)\). Its Laurent exponent satisfies
\[
N-2=(n-1)p+(r-2).
\]
Therefore
\[
\overline{\mathcal G_N}
=\frac1{r-1}
\left([T^{n-1}]b_{r-2}(g_s(T))\right)^p.
\tag{988.14}
\]
Here is the parameter bound behind this assertion. In the local
\(\mathcal T\)-coordinate, the two principal terms of \(x\) have
pole order two and no simple-pole coefficient. Hence the only
\(b_i\) that can have an origin pole is \(b_{p-2}=J\), which has
a simple pole. Equations (988.12)–(988.13) also establish this directly.
Substitution of \(\mathcal T=T+O(T^q)\) in that worst term first
changes degree \(q-3\). All other terms change later. The required
exponent \(N-2=q-(r+1)p+r-2\) is strictly below \(q-3\).
The original \(x(g_s(T))\) and \(\wp_+(T)\) likewise agree below
\(q-3\), by R986. Thus the coefficient on the left of the extraction
is exactly \((N-1)\mathcal G_N\), with
\(N-1\equiv r-1\pmod p\), proving (988.14).

## 4. The general balanced contraction, including theta symmetry

We give a direct coefficient proof of (988.3), which also explains
why the two Cartier rows in (988.13) produce the original balanced
coefficient. Take \(3\mid j\), \(3\le j\le p-2\), and set
\(N=j(p-1)\). All these indices satisfy \(N<q-1\) and
\(p\nmid N-1\). In the exact local parameter \(\mathcal T\),
Cartier's coefficient rule gives
\[
\left((N-1)\overline{\mathcal G_N}\right)^{1/p}
=[\mathcal T^{j-1}]
\frac{C(x\mathcal T^{j+1}\omega)}{\omega}.
\tag{988.15}
\]
Indeed the source exponent selected on the right is
\(p(j-1)+p-1=pj-1\); removing the factor
\(\mathcal T^{j+1}\) leaves \(N-2\). R986's exact jet and the
pole order two of \(x\) identify this with the original pure
coefficient, since \(N-2<q-3\).

Apply (988.10) with \(m=j+1\le p-1\). The right side of (988.15)
becomes
\[
\beta^{-j}(j+1)!
[\mathcal T^{j-1}]\mathcal B_{j+1}.
\tag{988.16}
\]
The last coefficient is exactly \(\overline{c_j^+}\). To check the
two exponents and all boundaries, \(\mathcal B_{j+1}\) is the
coefficient of \(W^j\) in \(e^{JW}\Xi\). R986's identification of
\(J_s\) with the genuine regularized zeta function shows that its
combined kernel differs from \(\Theta\) by factors starting in
\(T^pW\), after the original strict substitution. Since the theta
kernel has only a simple \(T\)-pole, those factors do not affect
\(T^{j-1}\), where \(j-1\le p-3\). The \(\mathcal T\)-to-\(T\)
change is still beyond the required range. It follows that
\[
[\mathcal T^{j-1}]\mathcal B_{j+1}
=[z^{j-1}W^j]\Theta(z,W)
=[z^jW^{j-1}]\Theta(z,W)=\overline{c_j^+}.
\tag{988.17}
\]
The middle equality is the genuine symmetry of the bare canonical
theta quotient. It is applied after forming the complete kernel;
individual summands of \(\mathcal B_{j+1}\) may have high poles.

All final coefficients in (988.15)–(988.17) are rational and reduce
to \(\mathbb F_p\), so the indicated \(p\)th root leaves them
unchanged. Since \(N-1\equiv-(j+1)\pmod p\), these equations give
\[
-(j+1)\overline{\mathcal G_N}
=\beta^{-j}(j+1)!\overline{c_j^+}.
\]
Division by the unit \(j+1\) proves (988.3).

For the same \(j\), Robert's reflection specialized as in R980 is
\(\mathcal G_{j(p-1)+p+1}=(\beta/j)\mathcal G_{j(p-1)}\).
Neither selected weight is an exceptional modified weight. This
proves (988.4). The zero-character cases complete both identities
for \(1\le j\le p-2\).

## 5. Original high indices, model phase, and the precise Artin–Hasse coordinate

Return to the original rows:
\[
\begin{array}{c|c|c|c}
p\bmod12&r&a=r+1&n=p-r\\ \hline
11&2&3&p-2\\
5&8&9&p-8
\end{array}
\qquad p\equiv2,5\pmod9.
\tag{988.18}
\]
Wilson's formula and \(\beta^{p-1}=1\) turn (988.3)–(988.4) into
\[
\boxed{\begin{aligned}
\overline{\mathcal G_{n(p-1)}}
&=-\frac{\beta^{r-1}}{(r-1)!}\overline{c_n^+},\\
\overline{\mathcal G_{np+a}}
&=\frac{\beta^r}{r!}\overline{c_n^+}.
\end{aligned}}
\tag{988.19}
\]
In the second line \(np+a=n(p-1)+p+1\) is the actual **high-star**
index of R980. The low-star index of R983's rejected common-scalar
probe was \((a+1)p-a+1\); that distinct comparison remains rejected.

For the original R974/R975 model
\(E_-:y^2=x^3-1\), let \(c_n^-\) denote its canonical balanced
coefficient. The exact phase of R979 gives, for the original
\(n\equiv3\pmod6\),
\[
c_n^+=-c_n^-.
\tag{988.20}
\]
Consequently (988.19) has respectively the scalars
\(+\beta^{r-1}/(r-1)!\) and \(-\beta^r/r!\) when written using
\(c_n^-\). The pure coefficients and \(\beta\) throughout remain
on \(E_+\).

Keep R978's exact original roots and arithmetic Artin convention:
\[
m=\frac{p+1}{3},\qquad b=\frac a3,\qquad
\varpi=\eta X,\quad \eta^m=-1,
\]
\[
\sigma=\operatorname{Frob}_{(2+s)}^{\rm arith}\bigm|_L,
\qquad \sigma\varpi=\zeta\varpi,
\qquad \chi(\sigma)=\zeta^{-b}.
\tag{988.21}
\]
Here \(\eta\) is the particular root of unity defined by the
original Robert point and root in R978, (978.24). It is not a freely
chosen comparison period.

Since \(n(p-1)\equiv r\pmod p\), substitution into R978's exact
high coordinate gives
\[
\boxed{\quad
\gamma_1
=-\frac{24}{r!}\,
\overline\eta^{-(m-b)}(\chi(\sigma)-1)
\beta^{r-1}\overline{c_n^+}
=\frac{24}{r!}\,
\overline\eta^{-(m-b)}(\chi(\sigma)-1)
\beta^{r-1}\overline{c_n^-}.
\quad}
\tag{988.22}
\]
This retains every original factor in (978.13). All factors outside
the balanced coefficient are units: \(p\ge41\), \(r=2\) or \(8\),
\(\eta\) is a root of unity, \(\beta\ne0\), and R976 proves
\(\chi(\sigma)-1\ne0\) on these original characters.

R978 therefore yields the equivalence
\[
\boxed{\quad
S_{\rm orig}\ne0
\quad\Longleftrightarrow\quad
\overline{c_{p-r}^+}\ne0
\quad\Longleftrightarrow\quad
\overline{c_{p-r}^-}\ne0.
\quad}
\tag{988.23}
\]
This is the new converse to the sufficient balanced unit criterion
of R974. Its proof uses the exact original Robert coordinate and
the actual Cartier contraction. It does not invert a merely integral
period quotient.

Using R975's exact universal formula, the same assertion is
\[
\boxed{\quad
S_{\rm orig}\ne0
\quad\Longleftrightarrow\quad
\mathcal F_{p-r}(0,-864)\ne0\pmod p,
\quad}
\tag{988.24}
\]
where \(\mathcal F_j(X,Y)=
(\mathcal R^{j-1}E)|_{E=0}\) is the specified Ramanujan polynomial
of R975. Its two factorials and the factor \(12\) are units in
the present range.

## 6. Explicit low-index calibrations

The low pure unit was already proved in R978. The new comparison
also supplies exact closed scalars for its two indices.
R975 gives \(3!c_3^+=1\). For the second fixed index, three direct
symbolic applications of its recurrence, beginning with its printed
\(U_6\), give
\[
\begin{aligned}
U_7&=-\frac{15}{4}g_2^2g_3,\\
U_8&=-\frac{13}{16}g_2^4-24g_2g_3^2,\\
U_9&=-18g_2^3g_3-144g_3^3.
\end{aligned}
\]
At \((g_2,g_3)=(0,-4)\), this is \(U_9=9216\), so
\[
9!c_9^+=\frac{U_9}{8!}=\frac8{35}.
\tag{988.25}
\]
These are paper deductions from the universal recurrence, with no
new numerical execution or prime window.

Equations (988.3)–(988.4) therefore give
\[
\boxed{\begin{array}{c|c|c}
a&\overline{\mathcal G_{a(p-1)}}
 &\overline{\mathcal G_{a(p-1)+p+1}}\\ \hline
3&-\beta^{-3}&-\dfrac1{3\beta^2}\\[2mm]
9&-\dfrac8{35}\beta^{-9}&-\dfrac8{315}\beta^{-8}.
\end{array}}
\tag{988.26}
\]
The denominators are units for all \(p\ge41\). Thus the established
low nonvanishing is compatible with fixed low balanced coefficients,
while (988.23) leaves the original varying high coefficient at
\(j=p-r\).

## 7. Scope and dependencies

The four-prime values in R983 are not used to infer (988.3).
The proof passes through the full rational Cartier identity, the
original finite Lubin–Tate jet, and the complete theta product.
All arithmetic phases in (988.22) remain the original ones.

The remaining high unit assertion is now the same assertion in the
pure, balanced, and actual trace descriptions. No one of these
equivalent assertions is proved for all original primes here. The
primitive label, same-label sigma factors, and Legendre factor needed
for an actual \(Q'_h\) unit are additional conditions. This result
does not complete Serre uniformity or turn the original complete
trace into any specified single-label unit.

- [R987](R987-original-Poincare-Cartier-identity-and-first-denominator.md),
  (987.14): the complete original Cartier connection identity and its
  finite integral endpoint. Its gluing proof is the source input for
  (988.8), not a consequence of this contraction.
- [R986](R986-explicit-rational-primitive-and-original-Lubin-Tate-jet.md),
  especially (986.29a), (986.28), and §§5–6: the exact functions
  \(Z,J_s,\mathcal T\), their pole bounds, and the original jet.
- [R984](R984-frobenius-regularized-finite-Kronecker-kernel-and-rational-Cartier-descent.md):
  the genuine finite kernel and the treatment of its regular
  \(p\)th-power remainder.
- [R985](R985-strict-coordinate-Frobenius-carry-and-original-pure-Hurwitz-coefficients.md):
  the coordinate carry that prevents an uncorrected direct comparison
  with an arbitrary regularized zeta primitive.
- [R978](R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md),
  (978.13) and (978.16): the exact actual high coordinate and trace
  criterion; [R980](R980-original-level-one-Hurwitz-reflection-and-distinct-mirror-pairs.md)
  for its two distinct reflection pairs.
- [R974](R974-original-balanced-coefficient-and-one-sided-CM-period-bridge.md),
  [R975](R975-original-balanced-Kronecker-integral-heat-recurrence.md),
  and [R979](R979-balanced-Kronecker-and-normalized-discriminant-Taylor-source.md):
  the original balanced normalization, its universal recurrence, and
  the exact \(E_+/E_-\) phase.
