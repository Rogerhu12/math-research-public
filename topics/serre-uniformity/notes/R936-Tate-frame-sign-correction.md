# R936: correcting the Tate-frame signs while retaining the exact trace

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: correction of an actual normalization error in the published R936 proof.** The assertions $E_6(E_u,\omega)=c_6(E_u,\omega)$, $\eta^{12}(E_u,\omega)=6sD$, and $\operatorname{KS}(\omega^2)=-du/D$ in the original version of R936 are incorrect for its stated Tate-normalized $E_6$ and differential $\omega=dx/(2y)$. They must be replaced by the signs proved below. This is not an arbitrary choice of phase or Hodge frame.

The finite polynomials $b$ and $C$, the script, its input parameters, and the six complete trace values can nevertheless be kept exactly as published. They are auxiliary polynomials with the corrected relation to the actual modular sections. The even exponents in the proved weight-zero function remove both signs exactly. This note proves that claim; it does not assume it because the numerical outputs were nonzero.

## 1. The standard Tate sign

For a short Weierstrass equation
$$
y^2=x^3+Ax+B,\qquad\omega=dx/(2y),
$$
the invariants are
$$
c_4=-48A,\qquad c_6=-864B.
\tag{SC1}
$$
In the Tate convention in which
$$
E_4(q)=1+240q+\cdots,\qquad E_6(q)=1-504q+\cdots,
$$
the modular sections evaluate as
$$
E_4=c_4,\qquad E_6=-c_6.
\tag{SC2}
$$
The sign is already forced at the Tate cusp. Its equation at $q=0$ is $y^2+xy=x^3$ with invariant differential $dx/(2y+x)$. Completing the square and replacing $x$ by $x-1/12$ gives
$$
y^2=x^3-x/48+1/864,
$$
with the same invariant differential. Thus $c_4=1$ and $c_6=-1$, whereas the stated normalized $E_6$ has constant term $1$. The complete Tate identities give (SC2), not the opposite sign. Equivalently, Baker's normalization on $y^2=4x^3-ax-b$ is $E_4=12a$, $E_6=-216b$; substituting $a=-4A$, $b=-4B$ gives the same result.

## 2. The original family and the unchanged marked cusp

Keep R936's exact family and its original parameter:
$$
E_u:\quad y^2=x^3+3uD x+D(1/2-4u^3),
\qquad D=1-4u^3,\qquad t=u^3.
\tag{SC3}
$$
The invariant calculations in R936 (ET16) were correct:
$$
c_4=-144uD,\qquad c_6=-432D(1-8t),\qquad
\Delta=-108D^2.
\tag{SC4}
$$
Consequently the correct modular evaluations are
$$
E_4(E_u,\omega)=-144uD,
\qquad E_6(E_u,\omega)=+432D(1-8t).
\tag{SC5}
$$
Use exactly the original $s^2=-3$, $\zeta=(-1+s)/2$, and $\zeta^2$ oldform phase. The original Fourier identities
$$
V_4^\dagger=Q+8sQ^4+O(Q^7),\qquad
E_4=1+O(Q^6),\qquad j=Q^{-6}+744+O(Q^6)
$$
still give the same branch
$$
u=(4s)^{-1}E_4/V_4^\dagger,
\qquad u\sim(4s)^{-1}Q^{-1}.
\tag{SC6}
$$
Only $E_4$, $j$, and $V_4^\dagger$ enter this comparison, so the error concerning $E_6$ does not affect it. Hence
$$
V_4^\dagger(E_u,\omega)=12sD
\tag{SC7}
$$
remains unchanged.

The sign of $\eta^{12}$ must be corrected along with that of $E_6$. From (SC5–6), the weight-six frame factor is
$$
\frac{E_6(E_u,\omega)}{E_6(Q^6)}
\sim-\frac18Q^{-6}.
$$
Since the original $\eta^{12}(Q^6)$ begins with $Q^3$, its evaluation begins with $-Q^{-3}/8$. In contrast, $6sD$ begins with $+Q^{-3}/8$. The identity $(\eta^{12})^2=\Delta$ therefore fixes
$$
\boxed{\quad
\eta^{12}(E_u,\omega)=-6sD,
\qquad
(E_6/\eta^{12})(E_u,\omega)=24s(1-8t).
\quad}
\tag{SC8}
$$
The ratio in (SC8) is precisely the original R936 ratio: both its numerator and denominator have changed sign. Its value at the transported order-three point $t=1/4$ is still $-24s$, as required by R920. No conjugate oldform, different square root, or different cusp parameter was inserted.

## 3. Kodaira–Spencer and the Hasse derivative

The identity in the stated Tate normalization is
$$
d j/j=-(E_6/E_4)\operatorname{KS}(\omega^2).
$$
For (SC3–5),
$$
d j/j=\frac{3(1-8t)}{uD}\,du,
\qquad E_6/E_4=-\frac{3(1-8t)}u.
$$
Thus
$$
\boxed{\operatorname{KS}(\omega^2)=+du/D.}
\tag{SC9}
$$
The equality extends across the removable $j=0,1728$ expressions on $D\ne0$.

R936's direct Cartier-coefficient calculation of the Tate-normalized Hasse invariant did not use the mistaken $E_6$ or KS identification. It remains
$$
\mathcal A(E_u,\omega)=uD^{N+1}H_N(t).
\tag{SC10}
$$
At its zero locus the connection term in $\partial_{p-1}\mathcal A$ vanishes, so (SC9) gives the corrected derivative relation
$$
\mathcal B(E_u,\omega)
\equiv +D\frac{d\mathcal A(E_u,\omega)}{du}
\pmod{\mathcal A}.
\tag{SC11}
$$
Retain the published auxiliary definition
$$
b(t)=-D(t)(H_N(t)+3tH_N'(t)).
\tag{SC12}
$$
Then the correct statement on the complete $D\ne0$ supersingular algebra is
$$
\boxed{\mathcal B(E_u,\omega)=-D^{N+1}b(t).}
\tag{SC13}
$$
The proof that $b$ is a unit is unchanged. The degree and squarefreeness of $H_N$, the point $u=0$, and the zero contributions of $D=0$ do not depend on these erroneous signs.

## 4. The original companion and the retained polynomial $C$

The proved Fourier-basis identity
$$
F=V_4^\dagger\eta^{12J}P_J(E_6/\eta^{12})
$$
uses the original series and is unchanged. Retain the published auxiliary polynomial
$$
C(t)=12s(6s)^JP_J(24s(1-8t)).
\tag{SC14}
$$
Substituting the correct evaluations (SC7–8) gives
$$
\boxed{F(E_u,\omega)=(-1)^JD^{J+1}C(t).}
\tag{SC15}
$$
For the two original rows, $J$ is odd: if $p\equiv11\pmod{12}$ then $N$ and $J=N$ are odd; if $p\equiv5\pmod{12}$ then $N$ is even and $J=N-1$ is odd. Thus the actual companion evaluation is the negative of the auxiliary expression previously asserted to equal it.

## 5. Exact preservation of the full sum and the published computation

R932's frame-independent weight-zero function is
$$
\mathfrak R=F^{p+1}/\mathcal B^w,
\qquad w=k_-=6J+4.
$$
Using (SC13) and (SC15), with the original unchanged $F$ and $\mathcal B$,
$$
\begin{aligned}
\mathfrak R
&=\frac{((-1)^JD^{J+1}C)^{p+1}}
{(-D^{N+1}b)^w}\\
&=(-1)^{J(p+1)-w}
D^{(J+1)(p+1)-(N+1)w}C^{p+1}b^{-w}\\
&=D^{2N+2}C^{p+1}b^{-w}=R(t).
\end{aligned}
\tag{SC16}
$$
The sign is exactly one because $p+1$ and $w$ are even. The last exponent equality is R936 (ET29), which was unaffected. Therefore the same full finite-algebra trace, with the same point multiplicities, computes the original $S^p$ without an additional scalar.

One can also check the principal-part values directly. R932 gives
$g_P=c_r b_P^{r-1}F_P$, with $c_r=-6^{r-1}(r-1)!$ and $r$ even. Relative to the erroneous intermediate evaluations, (SC13) and (SC15) multiply $g_P$ by $(-1)^{r-1+J}=1$ in both original rows. The denominator $b_P^r$ is unchanged. Thus the entire original $S$, not only an unspecified rescaling of it, is retained. Equivalently, (SC16) preserves $S^p$ and injectivity of Frobenius preserves $S$.

The published script constructs exactly the auxiliary polynomials (SC12) and (SC14), then computes the unchanged right side of (SC16). It does not use the false assertions that these auxiliary values are already the actual modular-section values. Hence its complete trace outputs retain their original identity, after this proof correction. No rerun or changed output hash is necessary to justify the retained values.

The six reported $(p,\operatorname{Tr},S^p)$ triples remain
$$
(41,3,39),\ (47,9,34),\ (59,35,16),\
(71,59,70),\ (83,35,14),\ (107,6,24).
$$
The actual source factor $m_{\rm I}(c_h^{\rm F})^{1/p}/[d_1 6^r(r-1)!]$ from R932 is unchanged and is not set to one. Primes 71 and 107 remain auxiliary.

## 6. Required edits to the published proof

- Keep the Weierstrass invariants (ET16) and every polynomial definition in (ET5–9).
- Replace $E_6=c_6$ by $E_6=-c_6$.
- In (ET17), replace $\eta^{12}=6sD$ by $\eta^{12}=-6sD$; keep $V_4^\dagger=12sD$ and the ratio $E_6/\eta^{12}=24s(1-8t)$.
- Replace the cusp-frame sign used to justify $\eta^{12}$ by the sign in §2 above.
- Replace (ET18) by $\operatorname{KS}(\omega^2)=+du/D$.
- Replace (ET26) by $\mathcal B\equiv+D\,d\mathcal A/du$.
- In (ET27), write $\mathcal B/D^{N+1}\equiv-b$ on the SS algebra.
- Replace (ET28) by $F=(-1)^JD^{J+1}C$.
- Insert (SC16) before concluding the unchanged trace formula, and explicitly identify $b,C$ as auxiliary finite polynomials with these corrected evaluation relations.

## Sources and verification boundary

- R913 and R918: the original Fourier phase and marked cusp.
- R920: the original ratio value $-24s$; it is retained, not rederived using a changed marking.
- R932: actual Serre derivative, principal-part formula, frame-independent residue sum, and retained source factor.
- R936: the actual family, complete finite algebra, point counts, script, and run receipts.
- Andrew Baker, *A supersingular congruence for modular forms*, Acta Arithmetica 86 (1998), 91–100, §1: https://www.maths.gla.ac.uk/~ajb/dvi-ps/modforms.pdf . Its displayed evaluations independently fix the same Tate sign.
- The standard Tate Weierstrass equation, reduced directly at $q=0$ in §1, fixes the normalization error independently of the trace values.

All calculations in this correction are symbolic paper algebra. No new local mathematical computation was performed.
