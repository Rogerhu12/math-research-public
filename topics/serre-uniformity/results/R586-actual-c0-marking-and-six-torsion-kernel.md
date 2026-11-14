# R586 — Restored actual c0 marking and exact six-torsion kernel

> Recovery, 2026-11-14. This document restores the part of R586 required by R589 and the subsequent actual CM norm calculation. It is a new file with a new hash, not a claim that the lost original bytes survived. The full finite-torsion rational identities below were rebuilt and checked once in exact rational arithmetic. No old $41$-adic torsion orbit or prime scan was repeated. The old additional numerical experiments are not silently reconstructed from their reported answers.

## 1. The actual marking and its selection rule

Put $K=\mathbb Q(\zeta)$, $\zeta^2+\zeta+1=0$, and $p\ge41$, $p\equiv5\pmod6$. Retain the actual positive CM embedding and the cubic direction $\Psi_\theta\kappa_4$ established by R575. The local character is the specified primitive $\theta_{-1}$, so

$$
\theta(\zeta)=\zeta^{-1},\qquad \theta(\sqrt{-3})=-1.
\tag{586R.1}
$$

On the actual two-dimensional tame standard plane, use coefficient vectors in $(H_0,H_2)$, where

$$
H_0=f_\theta(\tau/(6p)),\qquad H_2=f_\theta(2\tau/(3p)).
\tag{586R.2}
$$

The right-slash matrices are

$$
S=\begin{pmatrix}0&1/4\\4&0\end{pmatrix},\qquad
T=\zeta\begin{pmatrix}-1&0\\-4&1\end{pmatrix}.
\tag{586R.3}
$$

The factors $4$ are the weight-two factors of the two actual degeneracy functions; the inert-$2$ identity $a_4=-2$, together with the Fourier support $n\equiv1\pmod3$, fixes the displayed translation. These are the same actual tame matrices used in the recovered R592 proof. All operations here commute with the $p$-Cartan projection.

Let $v=(1,-4\zeta^2)^T$ be the original $c_1$ vector. Direct multiplication gives

$$
(TS)v=v,\qquad Sv=(-\zeta^2,4)^T,\qquad
(TS)(Sv)=\zeta^2Sv.
\tag{586R.4}
$$

The $H_6$ geometric group is the diagonal $C_3$ in $S_3\times C_3$ (R348 §2, with its R575 correction). Its six-sheeted cover has, above $j=0$, three fixed branches $a^3=1$ and one orbit of length three $a=0$, since $j=6912a^3(1-a^3)$. The first vector is fixed by the actual CM three-cycle. Conjugation by the tame reflection is not fixed, by the last equality in (586R.4), so its coset is necessarily the length-three branch. Choosing its CRT lift to act trivially modulo $p$ preserves the actual nonsplit necklace. Consequently the translated actual vector at $c_0$ is

$$
F_0=-\zeta^2H_0+4H_2.
\tag{586R.5}
$$

At the fixed analytic CM point, the automorphy factor of $ST$ is $-\zeta^2$. A weight-$2+2n$ jet matches (586R.5) exactly for $n\equiv0\pmod3$. In the flat coordinate of R592,

$$
\mathcal F_0(z)=M_0+\frac{M_3}{3!}z^3+\frac{M_6}{6!}z^6+\cdots.
\tag{586R.6}
$$

This is an operation on the actual full-level marking. It is not an over-$j$ automorphism carrying an arbitrary coarse candidate from $a=1$ to $a=0$.

## 2. Eighteen individually labeled six-torsion points

Use the fixed good elliptic curve

$$
E_0:y^2=x^3-1,\qquad \omega=dx/(2y),\qquad
\alpha^3=4,\qquad \beta=\sqrt3.
\tag{586R.7}
$$

Choose the positive real primitive period $\Omega$ of $\omega$. The nonzero two- and specified three-torsion points are

$$
T_{2,j}=(\zeta^j,0),\qquad
T_{3,\delta i}=(\alpha\zeta^i,\delta\beta),
\quad \delta\in\{1,-1\},\quad i,j\in\{0,1,2\}.
\tag{586R.8}
$$

Here $T_{2,j}=\Omega\zeta^j/2$ and $T_{3,\delta i}=2\Omega\delta\zeta^i/3$ modulo the period lattice. Set

$$
Q_{\delta ij}=T_{3,\delta i}+T_{2,j}.
\tag{586R.9}
$$

They are precisely the points $\Omega a/6$ with $a$ invertible modulo $6$, with labels

$$
a\bmod3=\delta\zeta^i,\qquad a\bmod2=\zeta^j,
\tag{586R.10}
$$

because the CRT representative is $a=4a_3+3a_2$. This fixes the signs in the three-torsion choice, rather than choosing an unlabeled root of the division polynomial.

The original $c_1$ character and the translated $c_0$ character are

$$
\chi_6(Q_{\delta ij})=\delta\zeta^{j-i},\qquad
\boxed{\chi_0(Q_{\delta ij})=\delta\zeta^{-i-j}.}
\tag{586R.11}
$$

The tame reflection in (586R.3) inverts the nontrivial character on $(\mathcal O_K/2)^\times$ and retains the displayed $3$-component. Its Fourier normalization has no unknown scalar: for either nontrivial cubic character $\kappa$ of $\mathbb F_4^\times$, the Gauss sum for $(-1)^{\operatorname{Tr}}$ is $1-\zeta-\zeta^2=2$; division by the standard Fourier factor $2$ exchanges $\kappa$ with $\kappa^{-1}$ with coefficient $+1$. Thus (586R.11) is the actual translated tame label, not a guess based on the lowest exponent of a rational function.

Fix the completed zeta value

$$
e(P)=E_1^*(P)=\zeta_\Lambda(P)-\overline P/A(\Lambda),
\quad \Lambda=\Omega\mathcal O_K,
\quad A(\Lambda)=\frac{\sqrt3\,\Omega^2}{2\pi}.
\tag{586R.12}
$$

At the two-torsion $e(T_{2,j})=0$. From $\psi_3=3x(x^3-4)$ and the division-polynomial constant-term formula of restored R574,

$$
e(T_{3,\delta i})=-\frac{x^2}{2y}
=-\frac{\delta\alpha^2\zeta^{2i}}{2\beta}.
\tag{586R.13}
$$

The completed-zeta addition formula therefore gives the exact value

$$
e(Q_{\delta ij})
=\delta\left(\frac\beta{\alpha\zeta^i-\zeta^j}
-\frac{\alpha^2\zeta^{2i}}{2\beta}\right).
\tag{586R.14}
$$

There is no unrecorded quasi-period correction in this formula.

## 3. Two full rational tame traces

Set $C_0=72\beta/\alpha$, and define

$$
\mathcal H_0(P)=\sum_{\delta,i,j}\chi_0(Q_{\delta ij})^{-1}e(P+Q_{\delta ij}).
\tag{586R.15}
$$

The sum of the weights is zero, so the $e(P)$ term in the addition formula cancels. Pairing $\delta$ with $-\delta$ also cancels the $y(P)$ term. Hence the result is a rational function of $x(P)$, with the complete labeled divisor of poles retained.

Write $r=j-i$, $t_r=\zeta^r$, and put

$$
X_r=\frac3{(\alpha-t_r)^2}-\alpha-t_r,\qquad
V_r=\frac{t_r-X_r}{\alpha-t_r}.
\tag{586R.16}
$$

Then

$$
x(Q_{\delta ij})=\zeta^iX_r,\qquad
y(Q_{\delta ij})=\delta\beta V_r,
\quad X_r^3-3V_r^2=1.
\tag{586R.17}
$$

The exact identities are

$$
\prod_{r=0}^2(s-X_r^3)=s^3-228s^2+48s-64,
\tag{586R.18}
$$

$$
-\frac\alpha{12}\sum_{r=0}^2
\frac{t_rV_rX_r}{s-X_r^3}
=\frac{7s^2+4s+16}{s^3-228s^2+48s-64},
\tag{586R.19}
$$

and, for comparison with the other marking,

$$
-\frac\alpha{12}\sum_{r=0}^2
\frac{t_r^{-1}V_r}{s-X_r^3}
=\frac{s^2+34s-8}{s^3-228s^2+48s-64}.
\tag{586R.20}
$$

They may be verified by multiplying by the three displayed linear factors and reducing in
$\mathbb Q[\alpha,\zeta]/(\alpha^3-4,\zeta^2+\zeta+1)$. The reconstruction program performs precisely those complete polynomial equalities, with fractions and no approximate arithmetic. Summing the $i$ orbit in (586R.15) now proves

$$
\boxed{\mathcal H_0=C_0R_0,\qquad
R_0=\frac{x(7x^6+4x^3+16)}{x^9-228x^6+48x^3-64}.}
\tag{586R.21}
$$

With $u=x^{-1/2}$ this is

$$
R_0=u^4\frac{7+4u^6+16u^{12}}
 {1-228u^6+48u^{12}-64u^{18}}.
\tag{586R.22}
$$

Equation (586R.20) gives the independently labeled $c_1$ trace $C_0R_-$, with
$R_-=x^2(x^6+34x^3-8)/\Delta$. It starts at $u^2$ and cannot be substituted for (586R.22).

## 4. The weighted zeta value and the universal low coefficient

The direct formula (586R.14) gives

$$
\begin{aligned}
\sum_Q\chi_0(Q)e_Q
&=6\beta\sum_{r=0}^2\frac{\zeta^{-r}}{\alpha-\zeta^r}\\
&=6\beta\alpha=\frac{24\beta}{\alpha^2}.
\end{aligned}
\tag{586R.23}
$$

The terms involving $e(T_3)$ cancel on summing the $j$ index. The partial fraction sum in the second line is exact because $\alpha^3-1=3$.

Now work at a prime $p\ge41$, $p\equiv5\pmod6$, and choose the embedding of $\alpha$ whose reduction is the unique cube root of $4$ in $\mathbb F_p$. Put $\varepsilon=(3/p)$. The restored R574 theorem, in exactly the normalization (586R.12), gives

$$
e_Q^p=D^{p-2}x(Q).
\tag{586R.24}
$$

For the flat parameter $z$ with $dz=\omega$, differentiation of (586R.15) at the origin gives

$$
D^{p-1}\mathcal H_0(O)
=-\sum_Q\chi_0(Q)^{-1}D^{p-2}x(Q)
=-\sum_Q\chi_0(Q)^{-1}e_Q^p.
\tag{586R.25}
$$

Since $(p-1)!\equiv-1$, $\chi_0^p=\chi_0^{-1}$, $\alpha^p=\alpha$, and $\beta^p=\varepsilon\beta$, equations (586R.21), (586R.23), and (586R.25) imply

$$
\boxed{[z^{p-1}]R_0=\frac\varepsilon{3\alpha}\pmod p.}
\tag{586R.26}
$$

This is a unit for every stated prime. The degree is below $p$, so the flat expansion and any strict integral CM coordinate agree to the necessary order. No high-coefficient integrality assertion is needed here.

For the specified primitive finite sum

$$
S_0=-\sum_{P\in E[p]\setminus\{O\}}\theta(P)\,\mathcal H_0(P),
\tag{586R.27}
$$

write a nonzero torsion point in an integral $\mu_{p^2-1}$-equivariant CM parameter as $Y(P)=\varpi_0$. Its valuation is $1/(p^2-1)$, and all the other points are its $\mu_{p^2-1}$ orbit. The character projection retains exponents $p-1$ modulo $p^2-1$. Since the rational function (586R.21) is integral at $O$, higher retained terms have an extra factor of valuation at least one. Therefore

$$
S_0=-(p^2-1)C_0\frac\varepsilon{3\alpha}\,
\varpi_0^{p-1}\bigl(1+O(p)\bigr),
\qquad v_p(S_0)=\frac1{p+1}.
\tag{586R.28}
$$

The primitive channel and the choice of the $p$-adic embedding matter in this statement. It is not a claim about all rational factors or all Galois embeddings without their transported marking.

## 5. What is restored, and what remains a separate theorem

The new certificate proves the complete finite identities (586R.17)–(586R.23) in a six-dimensional rational algebra. The labels, actual $S_6$ action, and R574 then give the actual low coefficient and valuation (586R.26)–(586R.28). These are exactly the R586 inputs used in R589.

The second finite sum $S_1$ and its high coefficient are treated in the separately restored R589 proof. The norm identity identifying $S_0S_1$ with the actual modular value $M_0\overline{M_0}$ belongs to R588 and is not proved by (586R.21). In particular no equality $M_0=R_0(P)$ is asserted. Neither this finite-kernel theorem nor the local selection rule provides a rank-zero quotient, a zero image of a rational point, or a candidate transport between the two coarse CM points.

The preserved historical $p=41$ finite-product residue is $S_0S_1\equiv14\pmod{41}$, as recorded in R589. It is not presented as a new run of the lost higher-precision orbit. The supplied exact rational checker was genuinely executed during recovery and binds its source hash into its output certificate.
