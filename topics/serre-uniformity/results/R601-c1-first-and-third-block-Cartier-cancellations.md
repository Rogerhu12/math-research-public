# R601 — Universal Cartier cancellation of the first and third actual c1 blocks

## 1. Statement and fixed normalization

Let \(p\ge41\) be prime with \(p\equiv5\pmod6\). All reductions below use the specified embedding in which \(\alpha^3=4\) reduces to the unique cube root in \(\mathbf F_p\). Work on
\[
E:y^2=x^3-1,\qquad \omega=\frac{dx}{2y},\qquad D=\frac d{dz}.
\]
Put
\[
\begin{aligned}
\Delta(x)&=x^9-228x^6+48x^3-64,\\
N_-(x)&=x^2(x^6+34x^3-8),&
N_+(x)&=x^2(x^6-20x^3-8),\\
R_-&=N_-/\Delta,&R_+&=N_+/\Delta.
\end{aligned}
\tag{601.1}
\]
This is R580/R595's actual \(c_1\) tame pair. Neither function is R589's \(c_0\) function \(R_0\).

In R595's notation the following identities hold for every such prime:
\[
\boxed{[z^{2p-2}]R_+=0,\qquad K_0=K_2=0,\qquad K_p=K_1.}
\tag{601.2}
\]
Consequently R595's actual primitive criterion is exactly
\[
v_p(M_2)=-1
\quad\Longleftrightarrow\quad
K_1\,r_3\ne0\pmod p,\qquad
r_3=[z^{(p-1)(p-3)}]R_-.
\tag{601.3}
\]
No universal nonvanishing of the right side is asserted.

We use the following already proved inputs in their original normalization. R574 gives a nonzero \(B\in\mathbf F_p\) such that
\[
D^{p-1}x=-B,\qquad
D^{p-2}x(Q)=e_Q^p
\tag{601.4}
\]
at prime-to-\(p\) torsion points, with \(e_Q=E_1^*(Q)\) the completed zeta value. In particular there is no additional period or sign in the second equality; it is the same (574.12)/(574.13) used in R586. R564 gives the full Cartier exchanges
\[
\mathcal C(R_-\omega)=cR_+\omega,\qquad
\mathcal C(R_+\omega)=\gamma R_-\omega,
\tag{601.5}
\]
where \(c=(3/p)\alpha^2/2\) and \(\gamma\ne0\). The explicit value of \(\gamma\) cancels in the new proof.

## 2. The exact eighteen-point identity

Let \(\mathcal Q\) be the eighteen points \(Q=(x_Q,y_Q)\) for which \(\Delta(x_Q)=0\), and set
\[
a_Q=\operatorname{Res}_{-Q}(R_-\omega)
=-\frac{N_-(x_Q)}{2y_Q\Delta'(x_Q)}.
\tag{601.6}
\]
These are genuine prime-to-\(p\) six-torsion points in R580's selected tame orbit. They remain distinct and avoid the two-torsion for \(p\ge5\). One direct verification uses
\[
\psi_6=6xy(x^3-4)(x^3+8)\Delta(x).
\tag{601.7}
\]
Since \(E[6]\) is etale away from \(2,3\), the displayed factors are disjoint there. For example \(\Delta(0)=-64\), \(\Delta|_{x^3=1}=-243\), \(\Delta|_{x^3=4}=-3456\), and \(\Delta|_{x^3=-8}=-15552\).

The completed zeta values have the exact rational formula
\[
e_Q
=\frac{y_Qx_Q^2(-19x_Q^6+4328x_Q^3-16)}{5184}.
\tag{601.8}
\]
This is the formula used in the actual R580 finite kernel. It also follows independently from (601.7) and
\[
e_Q=-\frac{D^2\psi_6(Q)}{72D\psi_6(Q)}.
\tag{601.9}
\]
For completeness, (601.9) is obtained by taking the constant term at \(Q\) in
\(D\log\psi_6=6E_1^*(6z)-36E_1^*(z)\).
The completed function is periodic, so the constant on the first term at \(6Q=0\) is zero. Formula (601.8) was checked by exact integer cross multiplication modulo \(\Delta\), not by pointwise floating point evaluation.

For a polynomial \(P\), the sum
\[
\sum_{\Delta(\xi)=0}\frac{P(\xi)}{\Delta'(\xi)}
=[x^8]\operatorname{rem}_{\Delta}P
\tag{601.10}
\]
is the usual Lagrange trace. Pairing \(Q\) with \(-Q\) and using (601.8) gives
\[
\sum_Q a_Q=0,\qquad
\sum_Q a_Qe_Q=0,\qquad
\sum_Q a_Qy_Q=-1.
\tag{601.11}
\]
For the middle identity, the relevant remainder is that of
\(N_-(x)x^2(-19x^6+4328x^3-16)\); its exponents are \(1\pmod3\), so its \(x^8\) coefficient is zero. The last identity follows because \(N_-\) is monic of degree eight.

The remaining identity is especially short. With \(s=x^3\),
\[
\begin{aligned}
&(s^2+34s-8)(-19s^3+4328s^2-16s+5184)\\
&\quad=-s(19s+650)(s^3-228s^2+48s-64)+134784s-41472.
\end{aligned}
\tag{601.12}
\]
The remainder contains no \(s^2\). Equations (601.6), (601.8), and (601.10) therefore prove
\[
\boxed{\sum_Qa_Q(e_Qx_Q+y_Q)=0,\qquad
\sum_Qa_Qe_Qx_Q=1.}
\tag{601.13}
\]
All these identities hold in characteristic zero and reduce at every \(p\ge5\). The accompanying exact integer certificate checks (601.7), (601.8), (601.12), and all three weighted traces.

## 3. A rational primitive and its precise expansion at O

Put
\[
q=-B^{-1}D^{p-2}x.
\tag{601.14}
\]
Equation (601.4) gives \(Dq=1\). Its only possible pole is \(O\), of order at most \(p\). The leading term of \(D^{p-2}x\) is
\[
(-1)^{p-2}(p-1)!\,z^{-p}=z^{-p}\pmod p
\]
by Wilson's theorem; hence the pole has order exactly \(p\), with coefficient \(-B^{-1}\).

Here is a direct construction of the local coordinate needed in the Cartier argument, which does not use any unproved high logarithm coefficient. Set \(u=x^{-1/2}\) at \(O\) with
\[
y=-u^{-3}\sqrt{1-u^6},\qquad
\omega=(1-u^6)^{-1/2}du.
\]
Since \(dq=\omega\) is regular, the negative Laurent part of \(q\) in \(u\) has only the term \(-B^{-1}u^{-p}\). Thus
\[
z_0=q+B^{-1}u^{-p}
\]
is a regular formal parameter satisfying \(dz_0=\omega\) and with linear coefficient one. The \(\mu_6\) weights of \(u\), \(q\), and \(z_0\) are all one: the weight of \(D^{p-2}x\) is \(-p\equiv1\pmod6\).

The characteristic-zero flat parameter is
\[
z=uZ(u^6),\qquad
Z(w)=\sum_{k\ge0}\frac{\binom{2k}{k}}{4^k(6k+1)}w^k.
\tag{601.15}
\]
Its coefficients are \(p\)-integral in degrees \(<5p\), since the first positive multiple of \(p\) congruent to one modulo six is \(5p\). Two primitives of \(\omega\) in characteristic \(p\) differ by a series in \(u^p\). The weight-one condition makes their first possible positive discrepancy have degree \(5p\). Consequently \(z_0\) agrees with the reduction of (601.15) in all degrees used below, and we may call it \(z\).

Finally \(u=z+O(z^7)\), so in characteristic \(p\)
\[
u^{-p}=z^{-p}+O(z^{5p}).
\]
This proves the exact truncated identity
\[
\boxed{q=z-B^{-1}z^{-p}+O(z^{5p}).}
\tag{601.16}
\]
Every coefficient extracted in the next section has index at most \(3p-1<5p\).

## 4. Cartier reconstruction proves the low coefficient is zero

Write \(r_+=[z^{2p-2}]R_+\). Cartier in a formal parameter is
\[
\mathcal C\!\left(\sum_na_nz^n\,dz\right)
=\sum_j a_{pj+p-1}^{1/p}z^j\,dz.
\tag{601.17}
\]
The \(z^2\) coefficient of the second identity in (601.5), using
\(R_-=z^2+O(z^8)\), gives
\[
\bigl([z^{3p-1}]R_+\bigr)^{1/p}=\gamma.
\tag{601.18}
\]
By (601.16), the \(z^{2p-1}\) coefficient of \(qR_+\) is
\(r_+-B^{-1}[z^{3p-1}]R_+\). Hence
\[
[z^1]\frac{\mathcal C(qR_+\omega)}{\omega}
=r_+^{1/p}-B^{-1/p}\gamma.
\tag{601.19}
\]

We compute the same coefficient globally from the actual finite poles. Define the rational function
\[
W(P)=\sum_{Q\in\mathcal Q}a_Qe_Q
\left(e_Q+\frac{y(P)-y_Q}{x(P)-x_Q}\right).
\tag{601.20}
\]
The zeta addition law identifies the parentheses with
\(E_1^*(P+Q)-E_1^*(P)\). The term involving \(E_1^*(P)\) cancels by (601.11), so (601.20) is an algebraic expression, not an unchosen primitive. It has residue \(a_Qe_Q\) at \(-Q\); the apparent pole at \(Q\) is removable. It is regular at \(O\), again because \(\sum a_Qe_Q=0\). Its linear coefficient is
\[
W'(O)=-\sum_Qa_Qe_Qx_Q=-1.
\tag{601.21}
\]

From (601.4), oddness of \(e_Q\), and (601.14),
\[
q(-Q)=B^{-1}e_Q^p.
\]
The residue of \(\mathcal C(qR_+\omega)\) at \(-Q\) is therefore
\[
q(-Q)^{1/p}
\bigl(\operatorname{Res}_{-Q}R_+\omega\bigr)^{1/p}
=\gamma B^{-1/p}a_Qe_Q.
\tag{601.22}
\]
There are no other finite poles. At \(O\), the original differential \(qR_+\omega\) has pole order \(p-2<p\) and residue zero. The residue vanishes also directly by its \(\mu_6\) weight four. In the negative exponent range Cartier could retain only the residue term; thus its Cartier image is regular at \(O\).

It follows that
\[
\mathcal C(qR_+\omega)-\gamma B^{-1/p}W\omega
\]
is holomorphic. Since the curve has genus one, it is a constant multiple of \(\omega=dz\), which contributes no coefficient of \(z\,dz\). Equations (601.19) and (601.21) now give
\[
r_+^{1/p}-B^{-1/p}\gamma=-B^{-1/p}\gamma.
\]
This proves \([z^{2p-2}]R_+=0\) for every prime in the stated range.

For comparison, its explicit finite coefficient expression is
\[
[z^{2p-2}]R_+
=[w^{(p-2)/3}]
\frac{1-20w-8w^2}{1-228w+48w^2-64w^3}
Z(w)(1-w)^{-1/2}\pmod p.
\tag{601.23}
\]
Indeed Lagrange first yields
\(n^{-1}[w^m](2A_++6wA_+')Z^2\) for \(n=2p-2\), \(m=(p-2)/3<p\);
Frobenius gives \(Z^{-n}=Z^2\) in this truncation. The identity
\(Z+6wZ'=(1-w)^{-1/2}\) and \(n+2=2p\) then give (601.23).
Its vanishing is proved by the global Cartier argument, not by sampling primes.

## 5. The first R595 block vanishes by a derivation identity

In \(\overline{\mathbf F}_p[E,x,y]/(y^2-x^3+1)\), put
\[
DE=-x,\quad Dx=2y,\quad Dy=3x^2,
\]
and define the actual Kronecker polynomials
\[
T_1=-(Ex+y),\qquad
T_2=-\frac{E^2y+2Ex^2+xy}{2}.
\tag{601.24}
\]
Direct differentiation gives
\[
\partial_E T_2=\frac12DT_1.
\tag{601.25}
\]
The \(p\)-th power of a derivation in characteristic \(p\) is again a derivation. Equation (601.4) gives its action on all three generators, so
\[
D^p=B\partial_E.
\tag{601.26}
\]
Let \(F=D^{p-1}T_2-(B/2)T_1\). Equations (601.25)–(601.26) imply
\(\partial_EF=0\) and \(DF=0\). Its degree in \(E\) is at most two, smaller than \(p\); hence \(F\) belongs to the elliptic function field alone. The kernel of \(D\) on that field is the subfield of \(p\)-th powers, so \(F\) is a \(p\)-th power.

The only possible pole of \(F\) is \(O\), of order at most \(p+4<2p\). Its \(p\)-th root therefore has at most a simple pole at \(O\). A genus-one curve has no nonconstant function with a single simple pole, so \(F\) is constant. Under
\((E,x,y)\mapsto(-E,x,-y)\), both terms in \(F\) are odd, since \(p-1\) is even. The constant is zero:
\[
\boxed{D^{p-1}T_2=\frac B2T_1.}
\tag{601.27}
\]

The actual finite tame sums satisfy
\(H_j(P)=\sum_Q\chi_6(Q)^{-1}T_j(P+Q)\) and
\(H_0=C_0R_-\), \(C_0=72\sqrt3/\alpha\).
Their residues give \(\chi_6(Q)^{-1}=C_0a_Q\). Thus (601.13) says
\(H_1(O)=0\) exactly. Since \(p-1<p\), Taylor extraction and Wilson give
\[
[z^{p-1}]H_2=-\frac B2H_1(O)=0\pmod p.
\tag{601.28}
\]
The actual CM coordinate \(Y\) in R595 agrees with flat \(z\) to this degree. Consequently \(K_0=0\).

## 6. The third block, including its coordinate and index bounds

Let \(e=p^2-1\),
\[
n_2=p-1+2e,\qquad n^*=n_2-2p+2=2p^2-p-1.
\]
R595 proves in its actual integral CM coordinate
\[
\omega=(1+O(pY^e)+O(Y^{2e}))\,dY.
\tag{601.29}
\]
It also proves \(pE\equiv-BY^p\pmod p\) in the coefficient range needed here: no allowable \(p^2\)-denominator exponent of the primitive occurs before \(5p^2\). The exact coefficient of \(E^2\) in \(H_2\) is \(D^2H_0/4\). All other terms disappear after multiplication by \(p^2\) and reduction in this range. Therefore
\[
K_2=\frac{B^2}{4}[Y^{n^*-2}]D^2R_-
=\frac{B^2}{2}[Y^{n^*}]R_-\pmod p.
\tag{601.30}
\]
For the second equality, \(n^*<2e\) and
\(n^*(n^*-1)\equiv2\pmod p\), so (601.29) makes \(D^2\) ordinary differentiation at precisely these degrees.

Since \(n^*=p(2p-1)-1\), the first exchange in (601.5) gives
\[
\bigl([Y^{n^*}]R_-\bigr)^{1/p}
=c[z^{2p-2}]R_+.
\tag{601.31}
\]
The low-degree \(Y\) and \(z\) coordinates agree. In the specified \(\mathbf F_p\) embedding this is exactly
\[
K_2=\frac{B^2c}{2}[z^{2p-2}]R_+.
\tag{601.32}
\]
Even without the field identification, the vanishing follows from (601.31). Section 4 proves \(K_2=0\). This finishes (601.2) and reduces the already established R595 criterion to (601.3).

## 7. Verification and exact scope

The accompanying JavaScript checker uses BigInt integer polynomial arithmetic only. It checks the division-polynomial factorization, the completed-zeta formula by faithful cross multiplication, the short polynomial identity (601.12), and the weighted residue sums. It does not claim to replace the symbolic Cartier and genus-one arguments. The checker was actually executed in the available JavaScript environment; all remainders were zero. No executor computation, new prime grid, or old torsion orbit was run.

The result includes the actual remaining congruence classes \(p\equiv2,5\pmod9\). It supplies an exact structural simplification and a necessary-and-sufficient first-term criterion, not a proof that \(K_1r_3\) never vanishes. The \(c_0\) and \(c_1\) tame points, their candidate transport, and the existence of an actual rank-zero quotient remain separate inputs. In particular R594's prime \(269\equiv8\pmod9\) concerns a broader local theorem and is not a remaining-prime counterexample. No primitive CM coefficient is here identified with a global quadratic-Chabauty leading coefficient.
