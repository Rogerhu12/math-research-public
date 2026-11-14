# R658 — Cartier trace comparison and the actual \(C_p\) channel

**Status: proved.** The previously unresolved term supported at the origin
in the Cartier comparison is zero. The proof uses the genuine multiplication
trace, including the completed-zeta translation factors. It does not infer
global equality from finite residues alone.

The result identifies the already proved actual R605 coefficient \(r_2\)
with the complete, independently normalized R615 six-torsion coefficient
\(C_p\). It does not prove that this coefficient, or the other required
coefficient \(r_3\), is always a unit.

## 1. Statement and the two different character directions

Let \(p\ge41\) be prime, \(p\equiv5\pmod6\). Use precisely the R574/R564
normalization
\[
 E:y^2=x^3-1,\qquad
 \omega=\frac{dx}{2y}=dz,\qquad D=d/\omega,
\]
\[
 \Delta=x^9-228x^6+48x^3-64,\qquad
 R_-=\frac{x^2(x^6+34x^3-8)}{\Delta},\qquad
 R_+=\frac{x^2(x^6-20x^3-8)}{\Delta}.
 \tag{658.1}
\]
The chosen reduction of \(\alpha^3=4\) is the unique cube root in
\(\mathbf F_p\); put
\[
 \beta^2=3,\quad
 B=(-1)^{(p-1)/2-(p-2)/3}
       \binom{(p-1)/2}{(p-2)/3}\in\mathbf F_p^\times,\quad
 c=\frac{(3/p)\alpha^2}{2},\quad C_+=144\beta/\alpha^2.
 \tag{658.2}
\]
All finite-point calculations may be made over a perfect extension of
\(\mathbf F_p\). The final \(R_-\) coefficients and \(C_k\) are rational,
and reduce to \(\mathbf F_p\).

The eighteen points, with the same labels as R615, are
\[
 Q_{\delta ij}=(\alpha\zeta^i,\delta\beta)+(\zeta^j,0),\qquad
 \chi(Q_{\delta ij})=\delta\zeta^{j-i}.
 \tag{658.3}
\]
Thus \(\chi=\varepsilon_3\kappa_4^{-1}\). The kernel \(R_-\) is the
\(\chi^{-1}\) sum; the complete Kronecker sum defining \(C_k\) is the
\(\chi\) sum. Cartier, rather than a relabeling of a global quotient,
will exchange the two.

In characteristic zero let \(\mathcal E(z)=\zeta_\Lambda(z)\), with the
hexagonal reduced normalization, and let
\[
 \Theta_Q(z,w)=
 \frac{\sigma(z+Q+w)}{\sigma(z+Q)\sigma(w)}
                  \exp(-\overline Qw/\mathcal A),\qquad
 \mathcal A=\operatorname{covol}(\Lambda)/\pi.
 \tag{658.4}
\]
Write \(H^+(z,w)=\sum_Q\chi(Q)\Theta_Q(z,w)\).
For \(k\equiv5\pmod6\), \(m=k-1\), R615 defines, with the full
inverse-sigma factor retained,
\[
 C_k=(-3)^m m!\,[z^mw^m]H^+(z,w)/C_+.
 \tag{658.5}
\]
The exact fixed-family interpretation is
\[
 L(\xi_k,k)=
 \frac{\alpha\beta\Omega\mathcal A^{k-1}}{(-3)^{k-1}}C_k,\qquad
 \xi_k((\nu))=\chi(\nu)^{-1}\nu^{2k-1}.
 \tag{658.6}
\]
This interpretation and all its factors are already proved in R615.

For \(5\le k\le p\), \(k\equiv5\pmod6\), define
\[
 r_{p,k}=[z^{(p-1)k}]R_-(z).
 \tag{658.7}
\]
Then \(C_k\) and the displayed \(r_{p,k}\) are \(p\)-integral, and
\[
 \boxed{\quad
 r_{p,k}\equiv c\left(-\frac1{3B}\right)^{k-1}C_k\pmod p.
 \quad}
 \tag{658.8}
\]
In particular,
\[
 \boxed{r_2=[z^{p^2-p}]R_-\equiv cC_p\pmod p.}
 \tag{658.9}
\]
Here \(r_2\) is literally the actual R605 coefficient. The proof below
establishes the comparison afresh; no lost R572 statement is used.

## 2. Rational connection coefficients, including \(a=p-1\)

Define rational functions in characteristic zero by
\[
 \sum_{a\ge0}L_a(P)w^a
   =\frac{1}{C_+}\exp(-\mathcal E(z)w)H^+(z,w).
 \tag{658.10}
\]
The term \(w^{-1}\) cancels because \(\sum_Q\chi(Q)=0\).
To see rationality and the exact integral range, put
\[
 k_Q(P)=e_Q+\frac{y(P)-y(Q)}{x(P)-x(Q)},\qquad
 e_Q=\zeta_\Lambda(Q)-\overline Q/\mathcal A.
 \tag{658.11}
\]
The apparent singularity at \(P=Q\) is removable. The zeta addition
formula gives
\[
 k_Q(P)=\mathcal E(z+Q)-\mathcal E(z)-\overline Q/\mathcal A.
 \tag{658.12}
\]

Let \(S_0=1\), \(S_{n+1}=DS_n+eS_n\), where
\(Dx=2y,\ Dy=3x^2,\ De=-x\).
Write \(1/\sigma(w)=\sum_{h\ge0}b_{6h}w^{6h-1}\), \(b_0=1\).
Then
\[
 L_a(P)=\frac1{C_+}\sum_Q\chi(Q)
  \sum_{0\le6h\le a+1}
  b_{6h}\frac{
   S_{a+1-6h}(k_Q(P),x(P+Q),y(P+Q))}
   {(a+1-6h)!}.
 \tag{658.13}
\]
This is a rational expression on \(E\), not an unspecified
nonholomorphic primitive.

For \(a\le p-2\), all the factorials in (658.13) are \(p\)-units.
The needed \(b_{6h}\) are \(p\)-integral: \(6h\le p-5\), and the
unshifted-sigma recurrence of R615 has only unit denominators in this
range. All \(e_Q\), the six-torsion coordinates, and \(C_+^{-1}\)
are integral at \(p\).

There is one additional point at \(a=p-1\). R574 proves
\[
 g=D^{p-2}x=-yT,\quad Dg=-B,\qquad
 g(P+Q)=g(P)+g(Q)+
     \left(\frac{y(P)-y(Q)}{x(P)-x(Q)}\right)^p,
 \qquad e_Q^p=g(Q).
 \tag{658.14}
\]
Consequently
\[
 k_Q(P)^p=g(P+Q)-g(P).
 \tag{658.15}
\]
The ordinary Bell polynomial satisfies
\(S_p(e,x,y)=e^p-g(x,y)\pmod p\). Its value in (658.13) is therefore
\[
 S_p(k_Q(P),x(P+Q),y(P+Q))=-g(P)\pmod p,
 \tag{658.16}
\]
independently of \(Q\). Summing with \(\chi\) makes this zero exactly
modulo \(p\). After clearing the integral rational denominators, the
numerator is coefficientwise divisible by \(p\); this cancels the sole
factor \(p\) in \(p!\). Thus
\[
 L_a\text{ has a well-defined integral rational reduction for }
                   0\le a\le p-1.
 \tag{658.17}
\]
This is an actual cancellation before reduction. It does not replace
division by \(p\) by division of a residue-field zero.

The only finite poles of \(L_a\omega\) are simple poles at \(-Q\), and
\[
 \operatorname{Res}_{-Q}(L_a\omega)
       =\frac{\chi(Q)e_Q^a}{C_+a!}.
 \tag{658.18}
\]
Indeed the residue of \(\Theta_Q(z,w)\,dz\) at \(z=-Q\) is
\(\exp(-\overline Qw/\mathcal A)\); multiplying by
\(\exp(-\mathcal E(-Q)w)\) gives \(\exp(e_Qw)\).
Formula (658.18) remains valid at \(a=p-1\), whose factorial is a unit.
At \(O\), poles of \(L_a\) are allowed at this stage and are not deleted.

Finally, oddness of \(\sigma\), the relation \(\chi(-Q)=-\chi(Q)\),
and \(\mathcal E(-z)=-\mathcal E(z)\) give
\[
 L_a(-P)=(-1)^aL_a(P).
 \tag{658.19}
\]

## 3. The multiplication correction and trace of the tame kernels

Let \(N\) be any positive integer with \(N\equiv1\pmod6\) and \(p\nmid N\).
Use the rational function
\[
 \varphi_N(P)=\mathcal E(Nz)-N\mathcal E(z)
            =N^{-1}D\log\psi_N(P).
 \tag{658.20}
\]
The division-polynomial expression proves its rationality and its
integral reduction away from its actual pole divisor. Its definition
includes the quasi-periods; it is not \(\mathcal E(Nz)\) alone.

Iterating the two exact addition formulas, for \(\mathcal E\) in
characteristic zero and for \(g\) in (658.14), proves the identity of
reduced rational functions
\[
 g(NP)=Ng(P)+\varphi_N(P)^p.
 \tag{658.21}
\]
With
\[
 q=-B^{-1}g,\qquad Dq=1,
 \tag{658.22}
\]
this is
\[
 \boxed{q(NP)=Nq(P)-B^{-1}\varphi_N(P)^p.}
 \tag{658.23}
\]
For example, the induction step replaces \(P+Q\) by \((nP)+P\).
The characteristic-zero addition corrections sum to \(\varphi_N\);
Frobenius makes their sum's \(p\)-th power the sum of their \(p\)-th
powers. This proof takes place in the rational function field, so
occasional zeros of an addition denominator do not remove points from
the statement.

Our trace convention is the trace on differentials:
\[
 \operatorname{Tr}_{[N]}(f(z)\,dz)
  =\frac1N\sum_{T\in E[N]}f(z/N+T)\,dz
 \tag{658.24}
\]
in a target flat variable \(z\). In particular
\(\operatorname{Tr}_{[N]}(\omega)=N\omega\).

The usual completed Kronecker distribution formula is
\[
 \sum_{T\in E[N]}\Theta_{Q+T}(z,w)
       =N\Theta_{NQ}(Nz,w/N).
 \tag{658.25}
\]
It can be proved by comparing the simple poles and their residues as
sections of the same degree-zero line bundle in \(z\); for generic
\(w\) that bundle has no nonzero holomorphic section. Analytic
continuation gives the expansion at \(w=0\). It is also the
multiplication specialization of the Kronecker distribution relation
in Bannai–Kobayashi–Tsuji, Proposition 2.20, with its cited general
endomorphism formula (primary text:
https://smf.emath.fr/system/files/2017-08/ens_ann-sc_43_185-234.pdf).

Because \(NQ=Q\) on the six-torsion labels, the constant term of the
\(\chi^{-1}\) sum in (658.25) gives
\[
 \operatorname{Tr}_{[N]}(R_-\omega)=R_-\omega.
 \tag{658.26}
\]
There is a twisted trace formula for (658.10):
\[
 \boxed{\operatorname{Tr}_{[N]}
       \left(\exp(-\varphi_N w/N)
              \sum_{a\ge0}L_a w^a\omega\right)
       =\sum_{a\ge0}N^{-a}L_aw^a\omega.}
 \tag{658.27}
\]
Here and below the right-hand variable is the target variable of
\([N]\).

The completed translation factors in this formula are essential.
For a representative \(T\) of an \(N\)-torsion point,
\[
 \Theta_Q(z+T,w)
       =\exp(\overline T w/\mathcal A)\Theta_{Q+T}(z,w),
\]
whereas
\[
 \mathcal E(Nz+NT)
       =\mathcal E(Nz)+N\overline T/\mathcal A.
\]
Thus multiplication of
\(\exp(-\mathcal E(z+T)w)\Theta_Q(z+T,w)\) by
\(\exp(-\varphi_N(z+T)w/N)\) cancels both \(T\)-dependent factors.
What remains is
\(\exp(-\mathcal E(Nz)w/N)\Theta_{Q+T}(z,w)\).
Equation (658.25), followed by the factor \(1/N\) in (658.24), proves
(658.27).

By (658.17), reduction of (658.27) is valid coefficient by coefficient
through \(w^{p-1}\). Exponential factorials of those degrees are
\(p\)-units. We never assert an integral exponential in all degrees.

## 4. Twisted trace for Cartier and exact cancellation at \(O\)

Write \(\mathcal C\) for Cartier on rational differentials over a
perfect field of characteristic \(p\), and define
\[
 T_a=\frac{B^a}{a!}\mathcal C(q^aR_-\omega),
       \qquad 0\le a\le p-1.
 \tag{658.28}
\]
Cartier commutes with the trace of a finite etale morphism. This can
also be checked after an etale local splitting into branches, where
it is additivity and change-of-coordinate invariance of the usual
Laurent-series Cartier formula.

The \(w^a\) coefficient of
\(\exp(-\varphi_Nw/N)\sum T_jw^j\) is
\[
 \begin{aligned}
 \sum_{j+b=a}\frac{B^j(-\varphi_N/N)^b}{j!b!}
               \mathcal C(q^jR_-\omega)
 &=\frac1{a!}\mathcal C\left(
      (Bq-\varphi_N^p/N)^aR_-\omega\right)\\
 &=\frac{(B/N)^a}{a!}
      \mathcal C\left(q(NP)^aR_-\omega\right).
 \end{aligned}
 \tag{658.29}
\]
We used \(B,N,j!,b!\in\mathbf F_p\), together with
\(\mathcal C(f^p\eta)=f\mathcal C(\eta)\), so this computation keeps
all semilinearity factors. The projection formula, (658.26), and
Cartier/trace compatibility now imply
\[
 \operatorname{Tr}_{[N]}
       \left(\exp(-\varphi_Nw/N)\sum_{a=0}^{p-1}T_aw^a\right)
     =\sum_{a=0}^{p-1}N^{-a}T_aw^a\pmod{w^p}.
 \tag{658.30}
\]

Compare \(T_a\) with \(cL_a\omega\). At a finite pole \(-Q\),
R574 gives \(q(-Q)=B^{-1}e_Q^p\). The full R564 Cartier identity
\(\mathcal C(R_-\omega)=cR_+\omega\) fixes the residue normalization.
Thus
\[
 \operatorname{Res}_{-Q}T_a
    =\frac{B^a}{a!}(q(-Q)^a
          \operatorname{Res}_{-Q}R_-\omega)^{1/p}
    =\frac{c\chi(Q)e_Q^a}{C_+a!}.
 \tag{658.31}
\]
It follows that
\[
 T_a-cL_a\omega=h_a\omega
 \tag{658.32}
\]
for a rational function \(h_a\) with no possible pole except \(O\).
Its parity is
\[
 h_a(-P)=(-1)^ah_a(P).
 \tag{658.33}
\]
Indeed \(q\) is odd, \(R_-\) is even, Cartier commutes with
\([-1]\), and (658.19) gives the same parity on the other side.

We prove \(h_a=0\) by induction on \(a\). Assuming the lower
differences zero, the \(a\)-th coefficients of (658.27) and
(658.30) give the untwisted identity
\[
 \operatorname{Tr}_{[N]}(h_a\omega)=N^{-a}h_a\omega.
 \tag{658.34}
\]
The induction also applies at \(a=0\), where there are no lower
terms (or one may use R564 directly).

Choose the single integer
\[
 N=4p-1,\qquad N\equiv1\pmod6,\qquad N\equiv-1\pmod p.
 \tag{658.35}
\]
Suppose \(h_a\) has a pole of order \(d>0\) at \(O\). By parity,
\(d\equiv a\pmod2\). In the trace, the only branch contributing
this pole is the branch at \(O\); all other preimages of \(O\)
are regular for \(h_a\). Since \([N]\) has linear coefficient
\(N\), its leading pole coefficient is multiplied by
\[
 N^{d-1}=(-1)^{d-1}=(-1)^{a-1}.
 \tag{658.36}
\]
But (658.34) requires the factor \(N^{-a}=(-1)^a\), a contradiction
in odd characteristic. Thus there is no pole and \(h_a\) is constant.
If \(a\) is odd, parity kills this constant. If \(a\) is even,
the trace of a constant multiple of \(\omega\) multiplies it by
\(N=-1\), while the right side of (658.34) multiplies it by \(1\);
the constant is again zero.

This proves the full rational identity, including the previously
uncontrolled origin terms:
\[
 \boxed{\quad
 \mathcal C(q^aR_-\omega)
       =cB^{-a}a!L_a\omega,\qquad 0\le a\le p-1.
 \quad}
 \tag{658.37}
\]
No assertion about a vanishing single-pole space was needed for
large \(a\). Its possible nonconstant functions were killed by
the actual trace and parity, not by a dimension shortcut.

## 5. Exact local parameter range

Use the characteristic-zero coordinate of R594,
\[
 x=u^{-2},\quad y=-u^{-3}\sqrt{1-u^6},\quad
 z=uZ(u^6),\quad
 Z(w)=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(6j+1)}w^j.
 \tag{658.38}
\]
R594 proves that every coefficient needed below, of degree
strictly less than \(p^2\), is \(p\)-integral, with all canceled
\(p\)-denominators explicitly retained. Put \(E_{\rm low}(u)\)
equal to the Laurent truncation of \(\mathcal E\) containing
its polar term and the positive exponents less than \(p\).
It is \(p\)-integral.

The exact R594 comparison, in the Laurent expansion in \(u\), is
\[
 z\equiv q+B^{-1}E_{\rm low}(u)^p
                     \pmod{(p,u^{p^2})}.
 \tag{658.39}
\]
This uses R594 (594.4), (594.6), and (594.17), in particular the
proved constant \(K_p=-3/B\) and the identity \(L_p(1)=B^{-1}\).
It is the restored full logarithm decomposition, not merely an
equality of the leading polar terms.

For coefficient extraction one may define the exact
characteristic-\(p\) local parameter
\[
 z_*:=q+B^{-1}\overline E_{\rm low}(u)^p.
 \tag{658.40}
\]
The negative \(u^{-p}\) terms cancel. Also \(dz_*=dq=\omega\),
and its linear term is \(u\). Thus \(z_*\) is genuinely a
formal parameter. It agrees with the reduction of the flat
characteristic-zero parameter \(z\) through degree \(<p^2\).
This justifies the ordinary Cartier coefficient formula in
\(z_*\), without pretending that the entire characteristic-zero
formal logarithm is integral.

Since \(R_-=u^2+O(u^8)\), all coefficients
\([z^{(p-1)k}]R_-\) with \(k\le p\) lie in this integral range
and agree with the coefficients in \(z_*\).

## 6. Extracting the diagonal and keeping the complete sigma factor

Let \(m=k-1\), so \(0\le m\le p-1\). In the exact local parameter
\(z_*\), the coefficient rule for Cartier gives
\[
 r_{p,k}^{1/p}
   =[z_*^m]\frac{\mathcal C(z_*^mR_-\omega)}{\omega},
 \qquad
 (p-1)k+m=pk-1.
 \tag{658.41}
\]
Expanding (658.40), using semilinearity and (658.37), yields
\[
 \begin{aligned}
 \mathcal C(z_*^mR_-\omega)
 &=\sum_{a=0}^m
   \binom ma B^{-(m-a)}
       \overline E_{\rm low}^{\,m-a}
          \mathcal C(q^aR_-\omega)\\
 &=cB^{-m}m!
      \sum_{a=0}^m
       \frac{\overline E_{\rm low}^{\,m-a}}{(m-a)!}
                 L_a\omega.
 \end{aligned}
 \tag{658.42}
\]
All factorials in this expression are units. The \(L_a\) reductions
include the \(p!\) cancellation of Section 2 at the terminal index.

The last diagonal is exactly the original complete theta diagonal.
Indeed, before reduction,
\[
 \exp(E_{\rm low}w)\sum_{a\ge0}L_aw^a
   =\frac1{C_+}
      \exp((E_{\rm low}-\mathcal E)w)\,H^+(z,w).
 \tag{658.43}
\]
Here \(H^+\) is regular at \(z=0\): every \(Q\) is nonzero, and
the \(w^{-1}\) term has canceled. Moreover
\(E_{\rm low}-\mathcal E=O(u^p)=O(z^p)\).
For \(m<p\), every nonconstant exponential term on the right
of (658.43) has \(z\)-order at least \(p>m\). Consequently
\[
 [z^mw^m]\exp(E_{\rm low}w)\sum L_aw^a
       =[z^mw^m]H^+(z,w)/C_+.
 \tag{658.44}
\]
This equality is obtained after combining the functions that are
regular at \(O\). It would be invalid to discard the tail of
\(\mathcal E\) separately in each term with a polar \(L_a\).

The left side of (658.44) is integral by (658.17); hence the
right side is integral as well. Its local coefficient is
unchanged when the reduced flat parameter is replaced by
\(z_*\), since its degree is \(m<p\). Combining
(658.41)–(658.44) proves
\[
 r_{p,k}^{1/p}\equiv
 cB^{-m}m!\,[z^mw^m]H^+/C_+
   =c(-3B)^{-m}C_k\pmod p.
 \tag{658.45}
\]
Both \(r_{p,k}\) and \(C_k\) are rational, and \(B,c\in\mathbf F_p\);
therefore the \(p\)-th root on the left makes no change. This
is (658.8). For \(k=p\), Fermat gives
\((-3B)^{-(p-1)}=1\), proving (658.9).

## 7. The resulting actual \(c_1\) criterion

R605 already proves, for the actual R588/R595 \(c_1\) channel,
\[
 K_1=-B^2r_2/4,\qquad
 r_3=[z^{(p-1)(p-3)}]R_-,
\]
\[
 p^2S_2S_3\equiv648B^5\alpha^{-2}r_2r_3,\qquad
 (pM_2)^2\equiv5184\zeta^2B^5\alpha^{-2}r_2r_3.
 \tag{658.46}
\]
Substitution of the newly proved comparison gives
\[
 \boxed{
 K_1=-\frac{B^2c}{4}C_p,\qquad
 p^2S_2S_3\equiv324(3/p)B^5C_pr_3,\qquad
 (pM_2)^2\equiv2592(3/p)\zeta^2B^5C_pr_3
 }\pmod p.
 \tag{658.47}
\]
All displayed constants are units for \(p\ge41\). In particular,
\[
 \boxed{\quad v_p(M_2)=-1
            \ \Longleftrightarrow\ C_pr_3\ne0\pmod p.\quad}
 \tag{658.48}
\]
This is a necessary-and-sufficient lowest-valuation criterion,
not a proof that its right side is nonzero for every prime.
Nor does (658.48) assert a global rank-zero image, an equality
of the \(c_0\) and \(c_1\) disks, or an already completed
quadratic-Chabauty leading coefficient.

The role of the fixed-conductor Hecke family is now precisely
specified: (658.6) and (658.8) give an actual coefficient
congruence after the Cartier exchange. They do not identify
that high-weight family with a rational quotient of the
original modular Jacobian.

## 8. Executed targeted comparisons and reproduction

The proof is the trace argument above. The following small exact
computations were used only to check its normalization.

R615 already records at \(p=41\)
\[
 C_{41}\equiv28,\qquad c=36,\qquad r_2=24,
 \qquad 36\cdot28=24\pmod{41}.
 \tag{658.49}
\]
For the newly selected second prime \(47\), the unchanged
R615 exact rational recurrence actually returned
\[
 C_{47}=
 \frac{276294949782973985037265126347813459984}
      {2989802261797564455633015625},
 \qquad C_{47}\equiv35\pmod{47}.
 \tag{658.50}
\]
The unchanged R605 direct coefficient routine actually returned
\[
 B=10,\quad r_2=30,\quad K_1=2.
 \]
The selected cubic-root embedding has \(\alpha=18\) and
\((3/47)=1\), hence \(c=21\) and
\[
 21\cdot35\equiv30\pmod{47}.
 \tag{658.51}
\]
The exact-rational \(k=47\) computation took 1.717 seconds.
The coefficient computation was also a short direct finite-series
calculation. These were two targeted normalization computations,
not a prime grid or a repeated wild-torsion orbit.

The commands were

    python scripts/R615_full_six_torsion_kronecker.py --k 47 --output R658_full_kronecker_k47_probe.json
    python scripts/R605_r2_coefficient.py --prime 47 --output R658_r2_prime47_probe.json

The three saved JSON files retain the exact rational value, the
direct coefficient summands, and the elementary modular comparison.
Their working labels do not claim a new orbit computation.
The source programs are the already delivered R615 and published
R605 programs; neither was modified.

Separately, a 0.005-second check at \(p=41\) compared the constant
origin term for \(a=2\) and the sixth-order/constant terms for \(a=8\).
Both matched. This exploratory check is not a substitute for
Sections 3–4 and is not required as a new publication dependency.

The proof uses the now published R594 full formal-logarithm identity
(594.7). R594 precedes this result in the dependency record.
There is no new long computation in this result. The updated root
README rule 14 at af6f8d4d6ba739501182942bf907054e36748996 has been
read: the external public runner is disabled, no new ci-queue request
is to be created, and subsequent computations use the available local
execution environment.
