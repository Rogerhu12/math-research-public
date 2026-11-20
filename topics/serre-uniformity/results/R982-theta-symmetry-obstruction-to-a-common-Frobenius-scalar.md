# R982 — Theta symmetry obstructs a common Frobenius scalar

Date: 2026-11-20. Author: `serre-public-astra-20261120-de0a3e3b / legendre_shift`.

**Status: proved obstruction to one precisely specified comparison model.**
This note rules out a coefficientwise replacement of the antiholomorphic
lattice variable by its residue Frobenius using only one common period
factor and one common exponent-shift factor. It does not rule out a
comparison at a single near-\(p\) index, or a comparison with explicit
index-dependent factorial, Gamma, regularizer, or carry corrections.
All calculations below are symbolic; no new arithmetic has been executed.

## 1. The original differential and the exact factorials

Let \(p\ge41\), \(p\equiv5\pmod6\), and use the actual pair
\[
E_+:y^2=x^3+1,\qquad \omega=\frac{dx}{2y},\qquad
(g_2,g_3)=(0,-4).
\tag{982.1}
\]
Let \(\Lambda\) be its complex period lattice and put
\(\mathcal A=\operatorname{area}(\mathbb C/\Lambda)/\pi\).
The symbol \(\mathcal A\) denotes this area factor, not a Hasse invariant.
Write
\[
K(z,w)=\frac{\sigma(z+w)}{\sigma(z)\sigma(w)},\qquad
c_j^+=[z^jw^{j-1}]K(z,w),
\]
\[
H_{u,v}=\frac{e^*_{u,v}(0,0;\Lambda)}{\mathcal A^u}.
\tag{982.2}
\]
Here \(\sigma'(0)=1\) and \(-\partial_z^2\log\sigma=\wp\).
On the equianharmonic lattice the reduced-theta quadratic exponential
vanishes by its weight-two transformation under \(\mu_6\). Thus the
Bannai–Kobayashi Laurent expansion used in R974 gives, for \(u\ge0,v\ge1\),
away from the two polar terms,
\[
[z^{v-1}w^u]K(z,w)
=\frac{(-1)^{u+v-1}}{u!}\,H_{u,v}.
\tag{982.3}
\]
In particular symmetry \(K(z,w)=K(w,z)\) gives the exact identities
\[
H_{j-1,j+1}=-(j-1)!c_j^+,\qquad
H_{j,j}=-j!c_j^+,
\]
\[
\boxed{\quad H_{j,j}=jH_{j-1,j+1}.\quad}
\tag{982.4}
\]
The factor \(j\) in the second line is not an optional normalization.

Only two already proved low coefficients will be needed. R975,
(975.13), evaluated at \(g_2=0,g_3=-4\), gives
\[
U_3=2,\qquad U_6=-96,
\]
and hence
\[
c_3^+=\frac{2}{3!2!}=\frac16,\qquad
c_6^+=\frac{-96}{6!5!}=-\frac1{900}.
\tag{982.5}
\]
Thus both sides of (982.4) are \(p\)-adic units for \(j=3,6\) in the
stated range. These are exact low-weight identities reused from R975,
not newly computed prime samples.

## 2. The two pure indices and Robert's actual reflection

Use exactly the pure Hurwitz coefficients of R978/R980:
\[
\log\frac{\sigma(z)}z
=-\sum_{k\ge4}\frac{\mathcal G_k}{k}z^k.
\tag{982.6}
\]
Robert's \(S_k(E_+,\omega)\) is precisely \(\mathcal G_k\), with no
factorial left over: his Laurent formula for the Weierstrass function
is \(z^{-2}+\sum(k-1)S_kz^{k-2}\), as checked in R980, (980.7)–(980.8).
Set
\[
q=p^2,\qquad B_p=E_{p+1}(E_+,\omega),\qquad \beta=B_p/12.
\tag{982.7}
\]
R980 establishes \(\beta\in\mathbb Z_p^\times\) in this original frame.

For \(j=3\) or \(6\), put
\[
t_j=p+1-j,\qquad
L_j=t_j(p-1)=q-1-j(p-1),
\]
\[
K_j=L_j+p+1=q-1+(j+1)-p(j-1).
\tag{982.8}
\]
Here \(1<t_j<p\). Both indices lie between \(4\) and \(q+1\), are
divisible by six, and avoid Robert's modified weights
\(p+1,q-1,q+1\). In particular the unmodified coefficients at these
indices are \(p\)-integral. Their reflection relation is
\[
K_j+pL_j\equiv p+1\pmod{q-1}.
\]
Robert's explicit constant in §5.4(i), printed p. 150, is
\(b_{L_j}=1/t_j\). His theorem, applied exactly as in R980, therefore gives
\[
\boxed{\quad
\overline{\mathcal G_{K_j}}
=\frac{\overline\beta}{\overline{t_j}}
\overline{\mathcal G_{L_j}}.
\quad}
\tag{982.9}
\]
Bars mean reduction in \(\overline{\mathbb F}_p\). Nothing here asserts
that either pure coefficient is nonzero without a further hypothesis.

## 3. The restricted replacement model and its contradiction

The formal substitution \(\bar\lambda\rightsquigarrow\lambda^p\) in
the mixed exponents sends \((j,j)\) to \(-j(p-1)\) and
\((j-1,j+1)\) to \((j+1)-p(j-1)\). Adding the same \(q-1\) to both
gives exactly \(L_j,K_j\) in (982.8).

The hypothesis to be excluded is the following precise model: there
exist fixed \(\alpha,\xi\in\overline{\mathbb F}_p^\times\), independent
of \(j\), such that **for both \(j=3\) and \(j=6\)**,
\[
\overline{H_{j-1,j+1}}
=\xi\alpha^{j-1}\overline{\mathcal G_{K_j}},\qquad
\overline{H_{j,j}}
=\xi\alpha^j\overline{\mathcal G_{L_j}}.
\tag{982.10}
\]
Thus \(\alpha\) allows an arbitrary common Frobenius period multiplier,
and \(\xi\) allows an arbitrary common multiplier for the common
\(q-1\) index shift. Their values are not prescribed. The model does
not include additional index-dependent factors.

By (982.5), the left sides in (982.10) are nonzero. Therefore its two
pure right-hand coefficients are nonzero, so division in the following
argument is legitimate. Combining (982.4), (982.9), and (982.10) gives
\[
j=\frac{\overline{H_{j,j}}}{\overline{H_{j-1,j+1}}}
=\alpha\frac{\overline{\mathcal G_{L_j}}}
 {\overline{\mathcal G_{K_j}}}
=\frac{\alpha\overline{t_j}}{\overline\beta}.
\]
Consequently
\[
\frac{\alpha}{\overline\beta}
=\frac{j}{p+1-j}.
\tag{982.11}
\]
For the two specified values this requires simultaneously
\[
\frac{\alpha}{\overline\beta}=-\frac32,
\qquad
\frac{\alpha}{\overline\beta}=-\frac65.
\tag{982.12}
\]
Their difference is \(-3/10\), nonzero for every \(p\ge41\). This
contradiction proves that the model (982.10) cannot hold.

## 4. What a corrected comparison would have to retain

For example, if the same two equalities are instead proposed with
extra nonzero factors \(C_{j-1,j+1}\) and \(C_{j,j}\), the identical
argument only imposes the necessary condition
\[
\boxed{\quad
\frac{C_{j,j}}{C_{j-1,j+1}}
=\frac{j\overline\beta}{\alpha\overline{t_j}}.
\quad}
\tag{982.13}
\]
Such index dependence removes the contradiction; this note neither
constructs nor excludes a genuine comparison with these corrections.
It also does not prove that satisfying (982.13) is sufficient.

For the original near-\(p\) index \(n=p-r\), \(r=2\) or \(8\), put
\(a=r+1\). The corresponding formal index is
\[
q-1+(n+1)-p(n-1)=(a+1)p-a+1=k_{\rm lo}^{*},
\]
and the modular weights satisfy
\[
k_{\rm lo}^{*}-2n=r(p+1).
\tag{982.14}
\]
R980 proves that \(\mathcal G_{k_{\rm lo}^{*}}\) is a unit. Neither
(982.14) nor the failure of (982.10) proves or disproves an identity
between this unit and \(c_n^+B_p^r\) with the correct index factors.
In particular, a single near-\(p\) comparison does not imply the two
low-index equalities assumed in (982.10).

The new conclusion is confined to the incompatibility of a common
\(\alpha,\xi\) replacement rule with exact theta symmetry and Robert's
explicit reflection constants. The actual two-variable integral
comparison, the unit status required in R974/R975, the same-label
primitive/Legendre condition, and the main uniformity problem remain
unsettled here.

## Sources and dependencies

1. [R974](R974-original-balanced-coefficient-and-one-sided-CM-period-bridge.md),
   §6 and (974.28): the reduced-theta convention and exact mixed
   Eisenstein–Kronecker factorial. Its curve \(g_3=+4\) is changed to
   the explicitly fixed \(g_3=-4\) pair in (982.1), retaining the
   canonical sigma normalization; see also R979, §3.
2. [R975](R975-original-balanced-Kronecker-integral-heat-recurrence.md),
   (975.2), (975.13): the universal integral balanced polynomials and
   the two low values used in (982.5).
3. [R978](R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md),
   (978.3), (978.10): the actual differential and pure coefficients.
4. [R980](R980-original-level-one-Hurwitz-reflection-and-distinct-mirror-pairs.md),
   §§2–4: the exact Robert normalization, supersingular unit, and
   explicit reflection constant.
5. Kenichi Bannai and Shinichi Kobayashi, *Algebraic theta functions
   and the p-adic interpolation of Eisenstein–Kronecker numbers*,
   author version math/0610163v4, Theorem 1.17 and Definition 1.5,
   <https://arxiv.org/pdf/math/0610163>.
6. Gilles Robert, *Congruences entre séries d'Eisenstein, dans le cas
   supersingulier*, Inventiones Mathematicae **61** (1980), 103–158,
   §1.4(2), printed p. 114; §5.4(i), printed p. 150; Theorem 8,
   printed p. 152. [Primary scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0061/LOG_0012.pdf).
   The coefficient normalization and case (i) were independently read
   from the primary page images for this note.
