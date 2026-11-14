# R615 — Full six-torsion Kronecker traces and integral \(C_p\)

**Status: proved in the precise scope below.** This result gives a complete
finite algebra recurrence for the fixed six-torsion Kronecker traces, with
their factorial and period normalization, and proves that the resulting
\(C_p\) is \(p\)-integral at every inert prime \(p\geq5\). The complete
inverse-sigma factor is essential. The calculations at \(k=5,11,41\)
below were actually executed in exact rational arithmetic.

This result does **not** assume the lost R572 comparison between these
fixed-family numbers and the coefficients of \(R_-\). In particular, the
observed equality \(r_2=cC_{41}\) at \(41\) is not asserted for all primes.
R605 already proves the actual \(c_1\) criterion in terms of \(r_2r_3\);
that criterion is not replaced by an unproved \(C_p\) criterion here.

## 1. Conventions and the exact theorem

Use

\[
E_0:y^2=x^3-1,\qquad \omega=\frac{dx}{2y}=dz,\qquad
D=\frac d{dz},\qquad \alpha^3=4,\quad \beta^2=3.
\tag{615.1}
\]

For the complex normalization take \(\alpha,\beta>0\),
\(\Lambda=\Omega\mathcal O_K\), \(K=\mathbf Q(\zeta)\), and \(\Omega>0\)
the real primitive period. Write

\[
\mathcal A=\frac{\operatorname{covol}(\Lambda)}{\pi},\qquad
e_Q=\zeta_\Lambda(Q)-\overline Q/\mathcal A.
\]

The eighteen labeled points and their character are those of R586 and
the restored R564:

\[
Q_{\delta ij}=(\alpha\zeta^i,\delta\beta)+(\zeta^j,0),
\qquad
\chi_6(Q_{\delta ij})=\delta\zeta^{j-i}.
\tag{615.2}
\]

Thus \(Q_{\delta ij}=\Omega a/6\), where
\(a\bmod3=\delta\zeta^i\), \(a\bmod2=\zeta^j\). The character is
\(\chi_6=\varepsilon_3\kappa_4^{-1}\). The sum in this result uses
**\(\chi_6\)**, whereas the original \(R_-\) kernel uses
\(\chi_6^{-1}\).

Let \(\sigma\) be the Weierstrass sigma function with
\(\sigma(w)=w+O(w^7)\), and define

\[
s_Q(z)=\frac{\sigma(Q+z)}{\sigma(Q)}
       \exp(-\overline Qz/\mathcal A),\qquad
\Theta_Q(z,w)=\frac{s_Q(z+w)}{s_Q(z)\sigma(w)}.
\tag{615.3}
\]

Here \(z\) is the holomorphic variable; the constant \(\overline Q\) is
held fixed. In particular,
\(D\log s_Q(z)=\zeta(Q+z)-\overline Q/\mathcal A\).

For \(k\equiv5\pmod6\), \(k\geq5\), put \(m=k-1\),

\[
\mathcal H_m=
\sum_{\delta,i,j}\chi_6(Q_{\delta ij})
[z^mw^m]\Theta_{Q_{\delta ij}}(z,w),\qquad
C_+=\frac{144\beta}{\alpha^2},
\]

and **define**

\[
\boxed{\ C_k=(-3)^m m!\,\frac{\mathcal H_m}{C_+}\ }.
\tag{615.4}
\]

Then:

1. Formulae (615.8)–(615.13) below compute \(C_k\) entirely in
   \(\mathbf Q[r]/(r^3-4)\), using finitely many rational additions and
   multiplications. In particular \(C_k\in\mathbf Q\).
2. For the actual fixed-conductor Hecke character
   \[
   \xi_k((\nu))=\chi_6(\nu)^{-1}\nu^{2k-1},
   \qquad(\nu,6)=1,
   \]
   its exact central-value normalization is
   \[
   \boxed{\ L(\xi_k,k)=
       \frac{\alpha\beta\,\Omega\,\mathcal A^{k-1}}
            {(-3)^{k-1}}C_k\ }.
   \tag{615.5}
   \]
3. For every prime \(p\equiv5\pmod6\), \(p\geq5\),
   \[
   \boxed{\ C_p\in\mathbf Z_{(p)}\ }.
   \tag{615.6}
   \]
   Formula (615.20) is an exact finite-torsion expression for its
   reduction. It proves integrality, not nonvanishing.

The definition in (615.4), rather than an unrecovered historical file,
fixes every scalar in this statement.

## 2. Three-dimensional initial data

Set \(r=\alpha\zeta^{i-j}\), so \(r^3=4\). The group law gives

\[
x(Q_{\delta ij})=\zeta^j\frac{r+2}{r-1},
\qquad
y(Q_{\delta ij})=-\frac{3\delta\beta}{(r-1)^2}.
\]

For \(\delta=1,j=0\), reduction modulo \(r^3-4\) gives

\[
X=r^2+r+2,\qquad
Y=y/\beta=-r^2-2r-3,\qquad
e=e_Q/\beta=\frac{r^2+2r+2}{6}.
\tag{615.7}
\]

The last formula has no period ambiguity. Indeed,
\(e(T_2)=0\), the tripling identity gives
\(e(Q_3)=-r^2/(2\beta)\), and the addition correction is
\(\beta/(r-1)\). Since
\((r-1)^{-1}=(r^2+r+1)/3\), their sum is precisely (615.7).
It also agrees with the restored R574 division-polynomial expression
for the same completed zeta value.

Put \(\xi=\beta z\). In this coordinate the exact initial-value system
is

\[
\frac{dx}{d\xi}=2Y,\qquad
\frac{dY}{d\xi}=x^2,\qquad
\frac{de}{d\xi}=-\frac{x}{3},\qquad
\frac{ds}{d\xi}=es,\quad s(0)=1,
\tag{615.8}
\]

with initial data (615.7). The first two equations preserve
\(3Y^2=x^3-1\). Thus all coefficients of \(s\) lie in
\(\mathbf Q[r]/(r^3-4)\), without a numerical period evaluation.

If \(x_n,Y_n,e_n,s_n\) are the coefficients of \(\xi^n\), the recurrence
actually used is

\[
\begin{aligned}
x_{n+1}&=\frac{2Y_n}{n+1},&
Y_{n+1}&=\frac1{n+1}\sum_{i=0}^n x_i x_{n-i},\\
e_{n+1}&=-\frac{x_n}{3(n+1)},&
s_{n+1}&=\frac1{n+1}\sum_{i=0}^n e_i s_{n-i}.
\end{aligned}
\tag{615.9}
\]

## 3. The complete inverse-sigma factor

Define \(\widetilde\sigma(\xi)=\beta\sigma(\xi/\beta)\). Its
Weierstrass function has invariants \(g_2=0,g_3=4/27\), so

\[
\widetilde x(\xi)=\xi^{-2}+
\sum_{n\geq1}a_n\xi^{6n-2},\qquad a_1=\frac1{189}.
\]

Substitution into \(\widetilde x''=6\widetilde x^2\), including the
two terms involving \(\xi^{-2}\), yields

\[
a_n=\frac{\sum_{i=1}^{n-1}a_i a_{n-i}}
           {(n-1)(6n+1)}\qquad(n\geq2).
\]

Twice integrating \(-\widetilde x\) with the prescribed sigma leading
term gives

\[
\frac{\xi}{\widetilde\sigma(\xi)}
=\exp\left(\sum_{n\geq1}
      \frac{a_n}{6n(6n-1)}\xi^{6n}\right)
=\sum_{h\geq0}u_h\xi^{6h},\qquad u_0=1.
\tag{615.10}
\]

This determines \(u_h\) by the ordinary exponential-series recurrence.
There is no omitted quadratic exponential: the hexagonal lattice has
the reduced \(G_2^*=0\) normalization used in (615.3).

Let \(b_j=[\xi^j]s(\xi)^{-1}\), obtained from

\[
b_0=1,\qquad b_n=-\sum_{j=1}^n s_jb_{n-j}.
\]

Then the exact diagonal coefficient in the scaled variables is

\[
\boxed{\quad
c_m=\sum_{j=0}^m b_j
 \sum_{\substack{h\geq0\\2m+1-j-6h\geq m-j}}
 u_h\,s_{2m+1-j-6h}
 \binom{2m+1-j-6h}{m-j}.
\quad}
\tag{615.11}
\]

This is simply coefficient extraction from
\[
\frac{s(\xi+\eta)}{s(\xi)\widetilde\sigma(\eta)}.
\]
Only \(s_0,\ldots,s_{2m+1}\), \(b_0,\ldots,b_m\) and
\(u_0,\ldots,u_{\lfloor(m+1)/6\rfloor}\) are used.
Consequently the recurrence is finite for every specified \(k\).

The physical coefficient in \(z,w\) is
\(\beta^{2m+1}c_m=\beta3^mc_m\). Negating a torsion point changes
this coefficient by \(-1\), and also changes \(\chi_6\) by \(-1\).
Rotating a point by \(\zeta^j\) changes the coefficient by
\(\zeta^{-j(2m+1)}=1\), since \(k\equiv5\pmod6\). Thus the eighteen
terms reduce, with all weights retained, to

\[
\frac{\mathcal H_m}{C_+}
 =\frac{3^m}{6}
   \operatorname{Tr}_{\mathbf Q[r]/\mathbf Q}(c_m/r).
\tag{615.12}
\]

If \(c_m=c_0+c_1r+c_2r^2\), then
\(\operatorname{Tr}(c_m/r)=3c_1\), because \(r^{-1}=r^2/4\).
Combining (615.4) and (615.12) proves the directly executable formula

\[
\boxed{\ C_k=\frac{(-1)^m3^{2m}m!}{2}\,[r]c_m.\ }
\tag{615.13}
\]

This proves the first assertion of the theorem. In particular,
“rational” follows from the finite algebra, not from recognizing a
floating-point approximation.

## 4. Exact Hecke and period normalization

For a unit \(u\in\mu_6\), \(\chi_6(u)=u^3\). Since
\(2k-1\equiv3\pmod6\), the defining expression for \(\xi_k\) is
independent of the generator of the principal ideal. The class number
of \(\mathcal O_K\) is one, so, initially in an absolute-convergence
half-plane, its ideal sum is \(1/6\) times the sum over nonzero
generators prime to \(6\).

At the central point, changing the generator \(\nu\) to
\(\overline\nu\) gives

\[
L(\xi_k,k)
=\frac16\sum_{(\nu,6)=1}
 \chi_6(\nu)\frac{\overline\nu^{k-1}}{\nu^k}.
\tag{615.14}
\]

This formula is interpreted by continuation: insert an additional
\(|\nu|^{-2t}\) for sufficiently large \(\Re(t)\), perform the
following grouping there, and continue to \(t=0\).

Split the generators into their eighteen unit classes modulo \(6\).
The substitution \(\nu=6(Q_a+\lambda)/\Omega\) gives

\[
L(\xi_k,k)=\frac{\Omega}{36}
  \sum_{a\in(\mathcal O_K/6)^\times}
   \chi_6(a)e^*_{m,m+1}(Q_a,0).
\tag{615.15}
\]

The Kronecker generating formula, with the residue-one normalization
(615.3), is

\[
[z^mw^m]\Theta_{Q_a}(z,w)
  =\frac{e^*_{m,m+1}(Q_a,0)}{m!\mathcal A^m}.
\tag{615.16}
\]

There is no sign here: the general sign is
\((-1)^{a+b-1}\), which is \(+1\) for \(a=m,b=m+1\).
This is Bannai–Kobayashi, *Algebraic theta functions and the p-adic
interpolation of Eisenstein–Kronecker numbers*, Theorem 1.17
([primary text](https://arxiv.org/pdf/math/0610163)).
Only its complex generating identity is being used; no ordinary
\(p\)-adic interpolation assertion is invoked.

Equations (615.15)–(615.16) give
\[
L(\xi_k,k)=\frac{\Omega m!\mathcal A^m}{36}\mathcal H_m.
\]
Finally \(C_+/36=4\beta/\alpha^2=\alpha\beta\), proving
(615.5) with its full factorial, cubic root and period factors.

## 5. Integrality at the diagonal weight \(k=p\)

Fix \(p\geq5\), \(p\equiv5\pmod6\). All eighteen points and their
completed zeta values have integral coordinates over a finite
unramified extension at \(p\): (615.7), its rotations, and
\(\alpha^3=4,\beta^2=3\) display their denominators explicitly.

Work first in the integral polynomial algebra

\[
\mathscr R=\mathbf Z_{(p)}[x,y,e]/(y^2-x^3+1),\qquad
Dx=2y,\quad Dy=3x^2,\quad De=-x.
\]

Let
\[
S_0=1,\qquad S_{n+1}=DS_n+eS_n.
\tag{615.17}
\]
These are ordinary derivatives of the shifted sigma function, before
division by a factorial. Write the physical inverse sigma as
\[
\sigma(w)^{-1}=\sum_{h\geq0}b_{6h}w^{6h-1},\qquad b_0=1.
\]
The factors \(3^{3h}\) relating these \(b_{6h}\) to (615.10) are
\(p\)-units. To compute the coefficient of \(w^{p-1}\) only
\(6h\leq p\) occurs, hence \(6h\leq p-5\). Every denominator in
(615.10) and its exponential recurrence to this bound is prime to
\(p\): in particular \(6h+1\leq p-4\) and \(6h-1<p\).
Thus these \(b_{6h}\) are \(p\)-integral.

At any of the eighteen points,

\[
[w^{p-1}]\Theta_Q(z,w)
=\sum_{0\leq6h\leq p}
 b_{6h}\frac{S_{p-6h}(Q+z)}{(p-6h)!}.
\tag{615.18}
\]

For \(h\geq1\) the denominator factorial is a \(p\)-unit.
The only possible denominator after extracting \(z^{p-1}\) is
therefore the factor \(p\) in \(p!\) for \(h=0\).

The restored R574 proves, in \(\mathscr R/p\),

\[
S_p=e^p+yT,\qquad D(yT)=B,\qquad DS_p=B,
\]

where
\((x^3-1)^{(p-1)/2}=U+x^pT\) and
\(B=[x^{p-2}]U\ne0\).
Since \(p-1\geq2\), it follows that
\[
D^{p-1}S_p=0\quad\hbox{in }\mathscr R/p.
\]
Equivalently,
\[
U_p:=\frac{D^{p-1}S_p}{p}\in\mathscr R.
\tag{615.19}
\]
This is coefficientwise divisibility after reducing \(y^2=x^3-1\);
it is not division of a residue-field numerical zero by \(p\).

Consequently every \(D^{p-1}[w^{p-1}]\Theta_Q\) is \(p\)-integral.
In (615.4), the factor \((p-1)!\) cancels the one used to extract
the \(z\)-coefficient, and \(C_+\) is a unit. Thus \(C_p\) is
integral over \(\mathbf Z_{(p)}\). As it is rational by (615.13),
this proves \(C_p\in\mathbf Z_{(p)}\).

The same proof gives the explicit reduction

\[
\boxed{\displaystyle
C_p\equiv\frac1{C_+}\sum_Q\chi_6(Q)
\left(
-U_p(Q)+
\sum_{1\leq6h\leq p}
 b_{6h}\,
 \frac{D^{p-1}S_{p-6h}(Q)}{(p-6h)!}
\right)\pmod p.}
\tag{615.20}
\]

Here \((-3)^{p-1}=1\) and \((p-1)!=-1\) modulo \(p\).
The first term requires the actual integral lift (615.19), or
equivalently one extra \(p\)-adic digit before division. The
identity \(S_{p+1}(Q)=B\) alone does not evaluate it. This is why
(615.6) must not be upgraded to a unit assertion.

## 6. Executed exact values and the first actual-channel comparison

The script R615_full_six_torsion_kronecker.py implements
(615.9)–(615.13) with fractions.Fraction and triples in
\(\mathbf Q[r]/(r^3-4)\). One specified weight is processed per
invocation; no prime scan was run.

| \(k\) | \(c_{k-1}\) | \(\mathcal H_{k-1}/C_+\) | \(C_k\) |
|---:|---|---|---|
| 5 | \(r/17496\) | \(1/432\) | \(9/2\) |
| 11 | \(r/45560649506400\) | \(1/1543147200\) | \(972/7\) |
| 41 | see the exact JSON | see the exact JSON | \(\dfrac{574168637166800435427012363416613708}{12258649578393708893528125}\) |

The measured runtimes were \(0.009\), \(0.090\), and \(1.553\)
seconds. At \(k=11\), the inverse-sigma coefficient \(u_1=1/5670\)
contributes a second block. Its constant and \(r^2\) terms cancel
the corresponding nonzero terms in the \(h=0\) block. The saved
two blocks therefore exhibit explicitly why omitting
\(\widetilde\sigma^{-1}\) is false beyond the low-degree range.

The last rational number is a \(41\)-adic unit with
\(C_{41}\equiv28\pmod{41}\). The already published R605 actual
coefficient is \(r_2=24\), and the R564 Cartier scalar at \(41\)
is \(c=36\). Hence the single actual comparison
\[
cC_{41}\equiv36\cdot28\equiv24=r_2\pmod{41}
\tag{615.21}
\]
holds. This is a new fixed three-dimensional algebra calculation;
the old \(41\)-torsion orbit was not repeated.

The three JSON files retain the working field name
normalization_candidate_Ck and the flag that identification
with the lost R572 is not assumed. Formulae (615.4) and
(615.13) now give an independent proved definition and
normalization of those exact values. The flag remains accurate
about the unrecovered historical comparison.

## 7. Remaining actual comparison

For clarity, R605 concerns
\[
R_-=\frac{x^2(x^6+34x^3-8)}
 {x^9-228x^6+48x^3-64},\qquad
r_2=[z^{p^2-p}]R_-,\quad
r_3=[z^{(p-1)(p-3)}]R_-.
\]
It already proves the actual \(c_1\) lowest-valuation criterion
\[
v_p(M_2)=-1\quad\Longleftrightarrow\quad r_2r_3\ne0.
\]

To replace \(r_2\) by \(cC_p\) for every \(p\), a further
Cartier comparison is required. For \(0\leq a\leq p-1\), the
finite-residue part has a natural candidate: with
\(q=-B^{-1}D^{p-2}x\), compare
\(\mathcal C(q^aR_-\omega)\) with the rational coefficient of
\(\exp(-E(z)w)\sum_Q\chi_6(Q)\Theta_Q(z,w)\), multiplied by
the exact factor \(cB^{-a}a!/C_+\).
Their finite residues agree. The difference can still have a
pole at \(O\) of order at most \(a-2\); equality of finite
residues does not kill that space. This term is not discarded
in the present theorem.

Thus the proved output is the full finite algebra, its exact
fixed-family \(L\)-normalization, and its \(p\)-integrality.
It contains no general nonvanishing claim, no replacement of
an actual Cartan jet by a fixed-curve value, and no new global
candidate exclusion.

## 8. Reproduction

The three actual commands were

    python scripts/R615_full_six_torsion_kronecker.py --k 5 --output C5.json
    python scripts/R615_full_six_torsion_kronecker.py --k 11 --output C11.json
    python scripts/R615_full_six_torsion_kronecker.py --k 41 --output C41.json

Their exact outputs and source SHA are recorded in the corresponding
JSON certificates and `notes/R615-agent-handoff-manifest.json`; the published bytes are bound by `notes/R615-handoff-manifest.json`. Larger computations,
if subsequently needed, are subject to the repository's public-runner
rule; none is launched or claimed by this result.
