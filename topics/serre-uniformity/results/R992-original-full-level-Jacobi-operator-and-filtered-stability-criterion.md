# R992 — An actual full-level Jacobi operator and a filtered stability criterion

Date: 2026-11-20. Author: serre-public-astra-20261120-de0a3e3b / legendre_shift. Independently reviewed in full by root and literature_frontier; the reused public output and actual pivot semantics were separately inspected by both reviewers.

**Status: proved operator, simple spectrum, exact Hasse kernel, and a conditional same-label nonvanishing criterion.** The operator below acts on the entire actual weight-\(p-5\) space of R968, after its apparent denominators cancel. Its normalized eigenforms all have marked value one. A nonzero subspace preserved by this operator therefore has a nonzero marked value, even when its dimension is much smaller than that of the whole space.

The actual primitive/Legendre filtered span has not been proved nonzero and invariant for every prime. Those are explicit hypotheses in the application, not consequences of the ambient operator. The stronger claim that every individual source column is an eigenform is false: the already certified \(p=227\) central column gives a counterexample. No new mathematical computation is executed; that finite fact is read from R969's existing output and frozen algorithm.

## 1. The unchanged full-level space and marked coordinate

Let \(p\ge41\) be prime, \(p=6N+5\), and set
\[
k=\lfloor p/12\rfloor,\qquad w=p-5=6N.
\]
The two possibilities are
\[
\begin{array}{c|c|c}
p&N&\dim M_w\\ \hline
12k+5&2k&k+1\\
12k+11&2k+1&k+1.
\end{array}
\tag{992.1}
\]
For the original application retain also \(p\equiv2,5\pmod9\). The construction of the operator itself does not require this additional restriction.

Write \(X=E_4\), \(Y=E_6\), and work in the integral full-level modular ring reduced at \(p\). R968's actual weight space has the equivalent basis
\[
X^{3d}Y^{N-2d},\qquad 0\le d\le k.
\]
Indeed this is the usual \(X,Y\) basis, and its change from R968's
\(Y^{N-2d}\Delta^d\) basis uses only powers of the unit \(1728\).
On \(Y\ne0\), put
\[
z=\frac{X^3}{Y^2}
=1+1728\,\frac{\Delta}{Y^2}.
\tag{992.2}
\]
Thus every \(F\in M_w(\mathbf F_p)\) has the unique expression
\[
F=Y^N P(z),\qquad P\in\mathbf F_p[z],\quad \deg P\le k.
\tag{992.3}
\]
The displayed expression extends as a polynomial in \(X,Y\), since \(N-2d\ge0\). It does not introduce a pole at \(Y=0\).

At the original R968 CM mark \(X=0\), \(Y\) is a unit, so the unchanged normalized marked functional is
\[
\operatorname{ev}_0(F)
=\left[\frac{F}{Y^N}\right]_{\rm mark}
=P(0).
\tag{992.4}
\]
In particular \(z\), rather than a freely chosen affine coordinate, is the original fine cubic parameter \(E_4^3/E_6^2\). R968's complete same-label failure is divisibility of each visible \(F\) by \(E_4^3\), equivalently \(z\mid P\).

Use the actual Serre derivation on the modular ring:
\[
D=-\frac{Y}{3}\partial_X-\frac{X^2}{2}\partial_Y.
\tag{992.5}
\]
On a homogeneous modular form of weight \(v\), this is
\(\Theta_\tau-vE_2/12\). Every occurrence of \(D\) below uses this derivation; \(D^2\) means its second iterate on the full homogeneous expression.

## 2. A rational-looking expression that is regular on the whole space

Define initially on \(XY(X^3-Y^2)\ne0\)
\[
\boxed{\qquad
\mathcal G(F)
=\frac{D^2(XF)+X^2F/144}{X^2(1-z)}.
\qquad}
\tag{992.6}
\]
The claim is that (992.6) extends to an endomorphism of the entire actual \(M_w(\mathbf F_p)\). The cancellation is an identity on the space, not an assumption about the particular CM source.

First, direct differentiation gives
\[
D z=\frac{X^2}{Y}(z-1),
\qquad
DF=X^2Y^{N-1}
\left((z-1)P'-\frac N2P\right).
\tag{992.7}
\]
Put \(Q=(z-1)P'-NP/2\). A further differentiation of \(XF\) gives
\[
\begin{aligned}
\frac{D^2(XF)}{X^2Y^N}
={}&z(1-z)^2P''\\
&+(1-z)\left(\frac43+\left(N-\frac32\right)z\right)P'\\
&+\left(\frac{4N+1}{6}
       +\frac{N(N-1)}4z\right)P.
\end{aligned}
\tag{992.8}
\]
This identity is obtained in the polynomial function field before reduction. In the present residue field \(N=(p-5)/6\equiv-5/6\), so addition of \(P/144\) to the right side of (992.8) factors it as
\[
(1-z)\left\{
z(1-z)P''+\left(\frac43-\frac73z\right)P'
-\frac{55}{144}P
\right\}.
\]
Consequently
\[
\boxed{\quad
\mathcal G(Y^NP)=Y^N\mathscr L P,\qquad
\mathscr L
=z(1-z)\partial_z^2
 +\left(\frac43-\frac73z\right)\partial_z
 -\frac{55}{144}.
\quad}
\tag{992.9}
\]
The operator \(\mathscr L\) preserves polynomials of degree at most \(k\). Equation (992.3) therefore proves all of the promised cancellations in (992.6), including at \(X=0\), at the cusp \(z=1\), and at \(Y=0\). The result is a genuine modular form in the same weight.

An equivalent expression, useful for applying the operator to the complete R968 source, is
\[
\boxed{\quad
\mathcal G(F)
=\frac{D^2F/X-2Y\,DF/(3X^2)+25F/144}{1-z}.
\quad}
\tag{992.10}
\]
It follows from \(DX=-Y/3\) and \(D^2X=X^2/6\). The constant \(25/144\) includes both \(D^2X\) and the extra term in (992.6).

If the zero-order term is omitted from the Jacobi operator, the correct formula is instead
\[
Y^N\left\{z(1-z)P''+
\left(\frac43-\frac73z\right)P'\right\}
=\frac{D^2F/X-2Y\,DF/(3X^2)
 +(5/9-55z/144)F}{1-z}.
\tag{992.11}
\]
The constant \(5/9\) cannot be dropped. Equations (992.10) and (992.11) distinguish the two operator conventions.

## 3. Complete simple spectrum, with every denominator controlled

For \(0\le d\le k\), define the terminating polynomial
\[
B_d(z)={}_2F_1\left(-d,d+\frac43;\frac43;z\right)
=\sum_{j=0}^{d}
\frac{(-d)_j(d+4/3)_j}{(4/3)_j\,j!}z^j.
\tag{992.12}
\]
This is a finite algebraic definition over \(\mathbf F_p\). All its denominators are units: \(j\le k<p\), and the numerators of the factors in \((4/3)_j\) are \(4,7,\ldots,3j+1<p\). Its leading coefficient is a unit as well. The factors from \((-d)_d\) are \(p\)-units, and the remaining positive numerators are at most \(6k+1<p\). Thus \(B_d\) has exactly degree \(d\), and \(B_d(0)=1\).

Its finite coefficient recurrence proves the Gauss equation
\[
z(1-z)B_d''+
\left(\frac43-\frac73z\right)B_d'
+d\left(d+\frac43\right)B_d=0.
\]
Hence
\[
\boxed{\quad
\mathscr L B_d=\lambda_d B_d,\qquad
\lambda_d=-\left(d+\frac5{12}\right)
              \left(d+\frac{11}{12}\right).
\quad}
\tag{992.13}
\]
For different \(d,e\in\{0,\ldots,k\}\),
\[
\lambda_d-\lambda_e
=-(d-e)\left(d+e+\frac43\right).
\tag{992.14}
\]
The first factor is nonzero. For the second,
\[
0<3(d+e)+4\le6k+4<p,
\]
so it too is nonzero. The spectrum is therefore simple over \(\mathbf F_p\), not merely over an unspecified extension.

The \(k+1\) actual modular eigenforms
\[
\mathcal E_d=Y^N B_d(z),\qquad0\le d\le k,
\tag{992.15}
\]
form a basis. Their unchanged normalized marked values are
\[
\boxed{\operatorname{ev}_0(\mathcal E_d)=1
\quad(0\le d\le k).}
\tag{992.16}
\]
This does not say that every linear combination has nonzero marked value.

For \(p=12k+5\), \(k+5/12=0\) in the field; for \(p=12k+11\), \(k+11/12=0\). Thus \(\lambda_k=0\). Simplicity of the spectrum shows that no other \(\lambda_d\) is zero, and
\[
\ker\mathcal G=\mathbf F_p\,\mathcal E_k.
\tag{992.17}
\]

## 4. The kernel is the actual Tate-normalized Hasse quotient

Let \(A_H=E_{p-1}\bmod p\) be the Tate-normalized Hasse invariant and let \(B_H=E_{p+1}\bmod p\). Their standard modular differential identities are
\[
DA_H=\frac{B_H}{12},\qquad
DB_H=-\frac{X A_H}{12}.
\tag{992.18}
\]
For completeness, these follow directly from their actual Fourier series. One has \(A_H(q)=1\) and \(B_H(q)=E_2(q)\) modulo \(p\). Therefore \(DA_H\) has the same weight-\(p+1\) Fourier series as \(B_H/12\). Likewise the Ramanujan identity \(\Theta E_2=(E_2^2-X)/12\) gives the same weight-\(p+3\) Fourier series for \(DB_H\) and \(-XA_H/12\). The modular expansion principle gives (992.18).

The factor \(X=E_4\) divides \(A_H\) in both classes of (992.1). This also follows directly from the weights: the \(X\) exponent of every weight-\(p-1\) monomial is one modulo three. R969's actual holomorphic target is consequently
\[
F_H=A_H/X\in M_w(\mathbf F_p).
\]
By (992.18),
\[
D^2(XF_H)+X^2F_H/144
=D^2A_H+XA_H/144=0.
\]
Thus \(F_H\) is in the kernel (992.17), and is not zero, since its Tate Fourier series is \(1/E_4\).

The cusp in the coordinate (992.2) is \(z=1\), \(Y=1\). The terminating Vandermonde identity gives
\[
B_k(1)=\frac{(-1)^k k!}{(4/3)_k}\in\mathbf F_p^\times.
\tag{992.19}
\]
Comparing constant Fourier coefficients fixes the full scalar:
\[
\boxed{\quad
\frac{A_H}{E_4 E_6^N}
=\frac{B_k(E_4^3/E_6^2)}{B_k(1)}.
\quad}
\tag{992.20}
\]
This is a global normalized identity, with the original Tate Hasse invariant and the original modular coordinates. In particular
\[
\operatorname{ev}_0(F_H)=B_k(1)^{-1}\ne0.
\tag{992.21}
\]
It is the actual target of R969, not an arbitrary polynomial with the same marked value.

The same \(B_k\) is the Jacobi polynomial in R990. In the actual algebraic frame \(X=12u\), \(Y=864\), its variable is \(z=u^3/432\), because (992.2) gives that equality exactly. The source scalar also follows directly: differentiating (992.20) at \(X=0\) and using (992.18) gives
\[
\beta=(DA_H)(0,864)
=-\frac{864^{N+1}}{3B_k(1)}
=-\frac{288\,864^N}{B_k(1)},
\qquad \beta=E_{p+1}(E_+,\omega)/12.
\]
Consequently \((A_H/E_4)(12u,864)=-\beta B_k(u^3/432)/288\), with the actual original frame. No equality between this variable and a ring-class uniformizer is used.

## 5. A cyclic marked functional and the conditional filtered bridge

The action on the monomial basis is particularly explicit:
\[
\boxed{\quad
\mathscr L z^d
=d\left(d+\frac13\right)z^{d-1}+\lambda_dz^d.
\quad}
\tag{992.22}
\]
If a nonzero \(P\) has exact order \(s\ge1\) at \(z=0\), then \(\mathscr LP\) has exact order \(s-1\), because
\(s(s+1/3)\) is a unit for \(s\le k\). More precisely,
\[
(\mathscr L^sP)(0)
=s!(4/3)_s\,[z^s]P\ne0.
\tag{992.23}
\]
Equivalently the \(k+1\) functionals
\[
P\longmapsto(\mathscr L^jP)(0),\qquad0\le j\le k,
\]
form a basis of the dual of \(\mathbf F_p[z]_{\le k}\): in the monomial basis their matrix is triangular with diagonal \(j!(4/3)_j\), all units.

It follows that
\[
\boxed{\quad
0\ne V\subset M_w,\quad\mathcal G(V)\subset V
\quad\Longrightarrow\quad
\operatorname{ev}_0|_V\ne0.
\quad}
\tag{992.24}
\]
One proof is to take a nonzero member of \(V\) of least vanishing order at the mark and apply (992.22). Alternatively, the simple spectral projectors show that a nonzero invariant subspace contains one of the eigenlines (992.15), whose marked value is one.

Now form exactly the original R968 filtered space
\[
V_p=\operatorname{span}_{\mathbf F_p}
\left\{
w_i Z_{6i+4,\,6(N-1-i)+1}:0\le i<N
\right\},
\]
\[
w_i=\mathbf1_{\gcd(6i+7,p+1)=1}\,
P_{6i+6}(1/s),\qquad s^2=-3.
\tag{992.25}
\]
The \(P_d(1/s)\) in (992.25) are the original Legendre polynomials; they are unrelated to the coordinate polynomial \(P(z)\) in (992.3). Each \(w_i\) lies in \(\mathbf F_p\), because its Legendre index is even and \((1/s)^2=-1/3\). R968's exact marked scalar is retained:
\[
\operatorname{ev}_0
\left(w_iZ_{6i+4,\,6(N-1-i)+1}\right)
=-72(-864)^{-N}\,
w_i f_i g_{N-1-i}.
\tag{992.26}
\]
The scalar is a unit. Therefore (992.24) gives the following genuinely same-label conditional result:
\[
\boxed{\begin{gathered}
V_p\ne0,\qquad\mathcal G(V_p)\subset V_p\\
\Longrightarrow\
\exists\,0\le i<N:
\gcd(6i+7,p+1)=1,\quad
P_{6i+6}(1/s)\,f_i g_{N-1-i}\ne0.
\end{gathered}}
\tag{992.27}
\]
All factors refer to that one original \(h=6i+7\). The conclusion follows because a nonzero linear functional on the span cannot vanish on every original generator. It is not a claim that a newly chosen linear combination is itself a new admissible label.

This criterion does not require full spanning. For example, the ambient invariant line \(\mathbf F_pY^N=\mathbf F_p\mathcal E_0\) has marked value one and does not contain \(A_H/E_4\), whose coordinate polynomial has positive degree \(k\). This is an illustration of the distinction between the two conclusions, not an assertion that this line is contained in the actual \(V_p\).

There is also an exact stronger sufficient criterion for the particular target. The spectral projector
\[
\Pi_k=\prod_{d=0}^{k-1}
\frac{\mathcal G-\lambda_d}{-\lambda_d}
\tag{992.28}
\]
is well-defined, and for \(F=Y^NP\),
\[
\Pi_kF=
\frac{[z^k]P}{[z^k]B_k}\,\mathcal E_k.
\tag{992.29}
\]
Hence an invariant \(V_p\) containing a member of exact degree \(k\) contains the actual Hasse target. The weaker (992.27) does not need this additional top-degree hypothesis.

## 6. The old central zero rules out individual-column eigenform claims

Reuse only R969's already certified public run
[44736934491](https://github.com/Rogerhu12/math-research-public/actions/runs/44736934491),
job \(136290572303\), source
48359d18d5ea7aa116e6be60cac425759a829cf0.
Its deterministic report is bound by SHA256
7c3e1e2569996a2d3389be06b02e66c7aa55503f97facdff581c024a42dcfc64.

At \(p=227\), \(N=37\), \(k=18\), the original central index is
\((i,j,h)=(18,18,115)\). The existing mask record has
\[
\gcd(h,p+1)=1,\qquad P_{114}(1/s)=107\ne0,
\]
and the existing marked comparison gives \(\operatorname{ev}_0(Z_i)=0\), consuming R945's original \(f_{18}g_{18}=0\).

The same already produced report includes
{"coefficient":13,"h":115,"i":18}
in the successful target combination. This alone would not prove the source column nonzero for an arbitrary solver. Here the frozen actual consumer
[full_level_critical_hasse_span_three_prime_consumer.py](../scripts/full_level_critical_hasse_span_three_prime_consumer.py),
SHA256
5bb625faec68b4276677213e948456df188af75c94f1fab9121946088790445a,
initializes its solution to zero and assigns entries only at the RREF pivot columns in the function named solve_or_annihilator. A nonzero reported solution entry therefore proves that this original column was a pivot, and in particular nonzero. Since its mask factor \(107\) is a unit, the unweighted \(Z_i\) is nonzero too.

Thus this is a specified nonzero actual source form with zero marked value. Every nonzero eigenvector of \(\mathcal G\) is a multiple of one \(\mathcal E_d\), by the simple spectrum, and has nonzero marked value by (992.16). Consequently
\[
\boxed{\text{The actual }p=227,\ i=18\text{ column is not an eigenvector of }\mathcal G.}
\tag{992.30}
\]
No sigma array, Fourier column, rank, or new prime is recomputed here. The inference uses only the old certified output and its actual solver semantics.

This does not refute invariance of the entire filtered span. At that prime R969 already proves \(V_p=M_w\), so invariance is automatic. The same is true at R969's other two full-rank primes; a new stability computation at those three primes would add no information.

## 7. Exact third-Serre-derivative detection at the original mark

The operator has another source-specific interface that uses the original Serre derivation without any division by \(X\) at the mark. Write

\[
F=Y^N\left(P(0)+P'(0)\frac{X^3}{Y^2}+O(X^6)\right).
\]

In computing the first three Serre derivatives at \(X=0\), only the two displayed terms can contribute. The first derivative is

\[
DF=-\left(\frac N2P(0)+P'(0)\right)X^2Y^{N-1}+O(X^5).
\]

Using \(DX=-Y/3\) and \(DY=-X^2/2\) twice more therefore gives

\[
DF(0,Y)=D^2F(0,Y)=0,
\qquad
D^3F(0,Y)
=-\frac{Y^{N+1}}9\left(NP(0)+2P'(0)\right).
\tag{992.31}
\]

On the other hand, (992.9) gives

\[
\mathcal G(F)(0,Y)
=Y^N\left(\frac43P'(0)-\frac{55}{144}P(0)\right).
\]

Eliminating \(P'(0)\) and using \(N\equiv-5/6\pmod p\) proves the exact raw evaluation identity

\[
\boxed{\quad
\mathcal G(F)(0,Y)
=\frac{25}{144}F(0,Y)-\frac6Y D^3F(0,Y).
\quad}
\tag{992.32}
\]

Equivalently, after normalizing each term to the weight of \(F\),

\[
\operatorname{ev}_0(\mathcal G F)
=\frac{25}{144}\operatorname{ev}_0(F)
-6\left[\frac{D^3F}{Y^{N+1}}\right]_{X=0}.
\tag{992.33}
\]

In the original \(E_+\) algebraic frame \(Y=864\), (992.32) becomes

\[
\boxed{\quad
\mathcal G(F)(0,864)
=\frac{25F(0,864)-D^3F(0,864)}{144}.
\quad}
\tag{992.34}
\]

Thus vanishing of the original marked value does not imply vanishing after applying \(\mathcal G\): the latter tests an actual third Serre derivative. These are identities of the full modular source. They do not assert that the third derivative is a combination of the retained critical columns. Applying R968's exact heat recurrence to it must keep the separate mixed Taylor indices, the Gaussian terms, and the canonical-zeta terms. A total Taylor degree passing \(p\) alone does not create a \(p\)-denominator in that mixed expansion.

## 8. The source-specific gap is still explicit

The ambient endomorphism and its spectrum are now completely fixed. Equations (992.6), (992.9), and (992.10) apply to the actual complete source columns, including every Gaussian and canonical-zeta term of R968/R971.

What is not proved is a source identity expressing each
\(\mathcal G(w_iZ_i)\) as a combination of the same retained columns for all original primes. Although a differential operator in the modular variable formally commutes with the numerical mask in the label variable, that commutation does not imply invariance of the finite column span. The individual-column shortcut is explicitly excluded by (992.30).

The nonzero-space hypothesis \(V_p\ne0\) also remains part of (992.27). The globally nonzero graph-level source in R959 is not silently identified with R968's full-level source away from the mark. A nonzero single term in the norm-one/Gaussian expression of R971 is not a proof that the corresponding complete column is nonzero. The three old full-rank primes satisfy both hypotheses, but do not prove them uniformly.

R971's infinite-prime column-count obstruction remains valid. A proper invariant subspace can satisfy (992.24), so that obstruction does not rule out the present conditional route. The work still needed is the actual filtered source action or an equally precise propagation of vanishing. Neither the complete high trace nor an unfiltered Hasse endpoint is substituted for the same-label conclusion.

## Dependencies and provenance

- [R968](R968-full-level-mixed-CM-jet-and-critical-factor.md): the actual full-level source, its integral weight space, both original filters, and the exact marked scalar.
- [R971](R971-complete-Wilson-Fourier-source-and-filtered-span-obstruction.md): the complete Fourier source and the infinite-prime obstruction to full spanning after the actual primitive mask.
- [R969](R969-certified-filtered-full-level-span-at-three-primes.md) and its frozen consumer: the reused \(p=227\) column, mask, marked value, and pivot semantics.
- [R945](R945-original-central-sigma-zeros-and-same-label-alternatives.md): the already proved central sigma zero used by R969.
- [R990](R990-original-hypergeometric-fixed-r-coefficient.md): the same precisely normalized terminating Jacobi polynomial and the actual frame \(z=u^3/432\). The operator and its full-space cancellation are proved independently above.
- Frederico Bianchini, *On the Ramanujan Vector Field modulo \(p\)*,
  [arXiv:2602.20109](https://arxiv.org/pdf/2602.20109), §2.1.3, Proposition 2.1 (its derivation is \(12D\)):
  the standard Hasse/Eisenstein differential relations. Their exact two Fourier-series proofs needed here are also supplied in (992.18).

The new conclusions are the genuine modular endomorphism, its simple marked spectrum, the exact Hasse kernel, the conditional filtered criterion, the old-data exclusion of individual eigencolumns, and the exact third-Serre-derivative marked interface. The actual all-prime filtered stability and the main Serre-uniformity goal remain open.

