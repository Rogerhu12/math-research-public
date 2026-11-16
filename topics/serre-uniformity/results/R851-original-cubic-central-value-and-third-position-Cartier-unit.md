# R851 — An original Cartier unit at a primitive third-position label

Date: 2026-11-16. Session: serre-public-astra-20261115 / sigma_uniform.

**Status: proved for every allowed prime $p\ge257$.** A rank-zero cubic-twist central value is a $p$ unit, and its exact original six-torsion Fourier sum forces one specified original $g_j$ to be a unit. The complementary $f_i$ and the Legendre factor at the same primitive label remain unproved. This is not completion of Serre uniformity.

## 1. Statement and unchanged original objects

Let
$$
p\ge257,\qquad p\equiv2,5\pmod9,\qquad
n=p+1,\qquad
e=\begin{cases}1,&p\equiv2\pmod9,\\2,&p\equiv5\pmod9.\end{cases}
\tag{851.1}
$$
Use the original $K=\mathbf Q(\zeta)$, $s=\sqrt{-3}$, curve and differential
$$
E_0:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad
\Lambda=\Omega\mathbf Z[\zeta],\quad\Omega>0.
$$
Let $\alpha^3=4$, $\beta^2=3$, with the original positive complex choices and the fixed $p$-adic embedding. In that embedding $\alpha\bmod p$ is the unique cube root of $4$ in $\mathbf F_p$. As in R697/R770, write
$$
F=x\sigma^6=z^4f(z^6),\qquad
G=-xy\sigma^6=zg(z^6),\qquad
f(v)=\sum f_iv^i,\quad g(v)=\sum g_jv^j.
\tag{851.2}
$$
Define
$$
k_p=\frac{(3-e)(p+1)}3,\qquad
j_p=\frac{k_p-2}{6},\qquad
h_p=p-k_p-2=\frac{e(p+1)}3-3,\qquad
i_p=\frac{h_p-7}{6}.
\tag{851.3}
$$
These are integers in the original admissible ranges, and $h_p$ is primitive. The theorem is
$$
\boxed{C_{k_p}\in\mathbf Z_p^\times,\qquad
       g_{j_p}\in\mathbf F_p^\times.}
\tag{851.4}
$$
Here $C_{k_p}$ is the actual R683 full six-torsion Cartier number, not a replacement central value. The two cases are

| Prime | $k_p$ | $j_p$ | $i_p$ | Original primitive $h_p$ |
|---|---:|---:|---:|---:|
| $p=18k+5$ | $6k+2$ | $k$ | $2k-1$ | $12k+1$ |
| $p=18k+11$ | $12k+8$ | $2k+1$ | $k-1$ | $6k+1$ |

This is a new assertion about an individual original coefficient. It is not inferred from an unfiltered sum or a dimension count.

## 2. The precise rank-zero cubic character and period

Retain the six-level character and Teichmüller direction of R717 and the [cubic-companion note](../notes/2026-11-16-sigma-third-labels-and-cubic-CM-companions.md):
$$
\chi_6(\delta\zeta^i\bmod3,\zeta^j\bmod2)
 =\delta\zeta^{j-i},\qquad
\theta(a)=\operatorname{Teich}(a/\bar a),\qquad
\chi=\theta^{n/3}.
$$
Put $D=4p^e$. The exact ideal character is
$$
\psi((a))=a\chi_6(a)\chi(a)^e
          =\psi_{C_D}((a)),\qquad
C_D:u^3+v^3=D.
\tag{851.5}
$$
The equality is the proved companion identification, with the conjugated cubic residue symbol and the same prime above $p$. Its conductor is exactly $(6p)$; the weight-two newform has conductor $108p^2$. No Euler factor at $p$ is inserted or deleted.

Write $\Omega_A$ for the real period of $Y^2=4X^3-1$ for $dX/Y$. Kezuka--Li (1.2) and the original coordinate scaling give
$$
\Omega_A=\frac{2\Omega}{\alpha},\qquad
\Omega_D=\frac{\Omega_A}{\beta D^{1/3}}
        =\frac{2\Omega}{\alpha\beta D^{1/3}}.
\tag{851.6}
$$
This is their actual Néron period. Their Theorem 1.1, together with the integrality statement immediately following (1.2), proves
$$
S_D:=\frac{L(C_D,1)}{\Omega_D}\in\mathbf Z\setminus\{0\}.
\tag{851.7}
$$
The rank-zero curve in (851.7) is $C_{4p}$ when $p\equiv2\pmod9$ and $C_{4p^2}$ when $p\equiv5\pmod9$. The opposite tame companion $C_{2p^e}$ has analytic rank one and is not substituted here.

## 3. The bad-prime BSD input and descent from $K$

The arithmetic input is Rubin, *The “main conjectures” of Iwasawa theory for imaginary quadratic fields*, Invent. Math. 103 (1991), **Theorem 11.1(i)**: for a rank-zero CM elliptic curve over its CM field, the BSD order formula is valid at primes not dividing the number of roots of unity. The theorem includes primes of bad reduction. For the precise source verification, Rubin's own CIME/AWS lecture notes, first page, expressly say that [Ru2] proves the stronger result without a good-reduction assumption. Kezuka--Li §2, p. 2119, likewise state for these $C_D$ that Rubin's argument excludes the $2$- and $3$-parts. The good-reduction hypothesis in the simplified proof of Theorem 12.19 of the lecture notes is not the scope of the cited 1991 theorem. Kezuka's [doctoral thesis](https://www.repository.cam.ac.uk/bitstream/1810/264939/1/PhDThesisYukakoKezuka.pdf), Introduction pp. 1–2, states the rational-curve formula (1.0.2) and expressly attributes its validity for every $p\nmid w$ to [17, Theorem 11.1].

Here $\mathcal O_K^\times=\mu_6$, so every $p$ in (851.1) is allowed, including the bad inert prime dividing $D$. The local valuation throughout this proof is normalized by $v_p(p)=1$. The prime $(p)$ of $K$ is unramified and has residue degree two. In particular $v_{(p)}$ on $K$ has this same normalization. An ideal norm multiplies its exponent by two; this factor will not be silently dropped.

For clarity, the passage from the theorem over $K$ to the rational central value is as follows. Put $E=C_D$. It has trivial rational torsion by the same Kezuka--Li introduction. The quadratic twist $E^{(-3)}$ is $\mathbf Q$-isogenous to $E$ by a $3$-isogeny: on a model $y^2=x^3+b$, the quotient by the rational subgroup scheme with $x=0$ has equation $y^2=x^3-27b$, which is precisely the $-3$ twist. Its kernel has order three, so the isogeny is invertible on all $p$-primary Galois modules in question.

Since $p$ is odd, restriction and corestriction split the $K/\mathbf Q$ cohomology into its two idempotents. The local conditions split as well. Therefore
$$
\Sha(E/K)[p^\infty]
 \simeq \Sha(E/\mathbf Q)[p^\infty]
       \oplus\Sha(E^{(-3)}/\mathbf Q)[p^\infty].
\tag{851.8}
$$
The two summands have the same order, by the $3$-isogeny. Also $E(K)[p^\infty]=0$. One can see the latter without any classification of torsion: $E$ has good reduction at the prime above $5$, whose residue field has $25$ elements; Hasse's bound gives at most $36<p$ points on that reduction. Reduction injects the $p$-primary torsion because $p\ne5$.

All finite Tamagawa factors are $p$ units. One can either read this from Rubin's CM formula up to $\mathcal O_K[1/6]^\times$, or check the local types: $j(E)=0$ is integral, so reduction is potentially good; component-group orders in the potentially good Kodaira types have prime factors only $2$ and $3$. At the particular prime $p\ge5$, the displayed cubic-twist model has types IV or IV* according as $e=1$ or $e=2$, again with $p$-unit component order. Minimality and a Néron differential are preserved by the unramified extension $K_{(p)}/\mathbf Q_p$. The complex Néron lattice is the actual $\Omega_D\mathcal O_K$ of Kezuka--Li. The real-versus-complex volume and discriminant conventions over $K$ introduce only factors supported at $2,3$; a different global differential generator likewise has algebraic comparison factor a $p$ unit. Thus the algebraic period-normalized quotient over $K$ has the same $p$ valuation as $S_D^2$. No factor $p^{e/3}$ is removed from (851.6), and no valuation is assigned to an unnormalized complex period.

The $-3$ isogeny also gives
$$
L(E/K,s)=L(E/\mathbf Q,s)^2.
$$
Rubin's formula and these unit observations consequently give an equality of **rational $p$ exponents**
$$
v_p\bigl(\#\Sha(E/K)\bigr)=2v_p(S_D).
\tag{851.9}
$$
Using (851.8) and cancelling the factor two yields
$$
v_p(S_D)=v_p\bigl(\#\Sha(E/\mathbf Q)\bigr).
\tag{851.10}
$$
The relevant Tate--Shafarevich groups are finite. The perfect alternating Cassels pairing on the finite odd-primary part over $\mathbf Q$ makes its order a square. Hence
$$
\boxed{v_p(S_D)\text{ is an even nonnegative integer}.}
\tag{851.11}
$$
Finiteness and the Cassels square-order implication for precisely these rank-zero curves are also recorded by Kezuka--Li immediately after (2.2), pp. 2119--2120. This argument does not invoke a conjectural BSD equality or a theorem restricted to good ordinary primes.

## 4. An explicit size bound: $0<|S_D|<p^2$ for $p\ge257$

The original additive convention is $\mathbf e_M(a+b\zeta)=e^{2\pi ib/M}$. The companion note proves
$$
\tau_p(\chi^e)=p,\qquad \tau_6(\chi_6)=-6,\qquad
\tau_{6p}(\chi_6\chi^e)=6p.
\tag{851.12}
$$
Thus the weight-two functional equation has root number $+1$. The same Mellin/Poisson argument as R717 §5, now with $\ell=1$ and the constant incomplete-gamma polynomial, gives
$$
L(C_D,1)
 =2\sum_{(\mathfrak a,6p)=1}
     \frac{\psi(\mathfrak a)}{\operatorname N\mathfrak a}
      \exp\!\left(-\frac{\pi\operatorname N\mathfrak a}
                         {3\sqrt3\,p}\right).
\tag{851.13}
$$
This is an exact absolutely convergent formula. Put $t=\pi/(3\sqrt3p)$. For an ideal of norm $m$, $|\psi(\mathfrak a)|=\sqrt m$, and the number of ideals of that norm is at most the ordinary divisor count $d(m)$, by the split, inert and ramified prime factorizations in a quadratic field. Hence
$$
|L(C_D,1)|\le2\sum_{m\ge1}d(m)m^{-1/2}e^{-tm}.
\tag{851.14}
$$
Here is a fully uniform elementary estimate. For $x\ge1$,
$$
\mathcal D(x)=\sum_{m\le x}d(m)
 \le x\sum_{a\le x}\frac1a\le x(1+\log x).
$$
Partial summation with $x^{-1/2}e^{-tx}$, followed by
$\log x=\log(1/t)+\log(tx)\le\log(1/t)+tx$, gives, for $0<t\le1$,
$$
\begin{aligned}
\sum_{m\ge1}d(m)m^{-1/2}e^{-tm}
&\le\int_0^\infty
 (1+\log(1/t)+tx)
 \left(\frac12x^{-1/2}+tx^{1/2}\right)e^{-tx}\,dx\\
&=\sqrt\pi\,t^{-1/2}\bigl(\log(1/t)+2\bigr).
\end{aligned}
\tag{851.15}
$$
The extension of the integral down to zero is an upper bound by a nonnegative integrand; the bound on $\mathcal D(x)$ itself is only used for $x\ge1$. The last equality uses $\Gamma(1/2)=\sqrt\pi$ and its two elementary successors.

Combining (851.6), (851.14) and (851.15) yields
$$
|S_D|\le
\frac{\alpha^2\beta\sqrt{3\beta}}{\Omega}
p^{e/3+1/2}
\left(\log\frac{3\beta p}{\pi}+2\right).
\tag{851.16}
$$
The original period satisfies
$$
\Omega=\int_1^\infty\frac{dx}{\sqrt{x^3-1}}>2.
$$
Using $\alpha<2$, $\beta<2$, $\pi>3$ and $4\sqrt6<10$, (851.16) gives the simple strict bound
$$
|S_D|<10p^{7/6}\bigl(\log(2p)+2\bigr).
\tag{851.17}
$$
For $x\ge256$, the function $x^{5/6}/(\log(2x)+2)$ is increasing. At $x=256$,
$$
256^{5/6}=64\,2^{2/3}>96,
\qquad
10(\log512+2)<83,
$$
where $2^{2/3}>3/2$ and $\log2<7/10$. These inequalities prove $10(\log(2p)+2)<p^{5/6}$ for every $p\ge257$. Consequently
$$
0<|S_D|<p^2.
\tag{851.18}
$$
If $p$ divided the nonzero integer $S_D$, (851.11) would make $p^2$ divide it, contradicting (851.18). We have proved the actual auxiliary unit
$$
\boxed{S_D\in\mathbf Z_p^\times\quad(p\ge257).}
\tag{851.19}
$$
No finite-prime calculation enters this bound.

## 5. Exact transport to the original integral Fourier coefficient

The original rational kernel and constant are
$$
R_-(P)=\frac{x^2(x^6+34x^3-8)}
                 {x^9-228x^6+48x^3-64},\qquad
C_0=\frac{72\beta}{\alpha},
$$
$$
H_0(P)=\sum_Q\chi_6(Q)^{-1}E_1^*(P+Q)=C_0R_-(P).
\tag{851.20}
$$
These are R595/R601's actual $c_1$ tame labels and R683's rational kernel. In particular this is not the distinct $c_0$ function $R_0$.

For $P_b=\Omega b/p$ in the original marking, define
$$
\mathcal S_0=-\sum_{b\in(\mathcal O_K/p)^\times}
                       \chi(b)^{-e}H_0(P_b).
\tag{851.21}
$$
Apply the exact residue-class identity R588(588R.14) with $r=0$ and finite character $\chi_6\chi^e$. In the CRT decomposition $c=6b+pa$, complex conjugation of the finite character gives $\chi_6(a)^{-1}\chi(b)^{-e}$ and $\chi_6(p)=-1$. Thus the sign in (851.21) is the original one, and
$$
L(\psi,1)=\frac{\Omega}{36p}\mathcal S_0.
\tag{851.22}
$$
The formula only requires the ideal character's unit condition; the $p$ character need not be primitive of order $p+1$. The threefold character in (851.21) is used to prove a coefficient at the primitive label (851.3), not to replace that label in the original criterion.

Now (851.6), (851.7) and (851.20) give the exact algebraic equality
$$
\boxed{\frac{\mathcal S_0}{C_0}
       =\frac{p}{3D^{1/3}}S_D.}
\tag{851.23}
$$
In particular the real-period comparison has been made before passing to the fixed $p$-adic embedding. The algebraic cube root $D^{1/3}$ and the nonunit factor $p$ remain. There is no valuation assigned to an unnormalized complex period. Equation (851.19) implies
$$
v_p(\mathcal S_0/C_0)=1-e/3=(3-e)/3.
\tag{851.24}
$$

Use the original integral $\mu_{p^2-1}$-equivariant CM parameter $Y$ from R589(589.6)--(589.10), also used in R710/R727. Put
$$
q_0=p^2-1,\quad \varpi=Y(P_1),\quad T_0=\varpi^{q_0}.
$$
Then
$$
v_p(\varpi)=1/q_0,\qquad T_0/p\equiv1\pmod p,
\qquad Y(P_b)=[b]\varpi.
\tag{851.25}
$$
The reduction is good at $p$, the mixed six-torsion poles are disjoint from $O$, and the denominator of $R_-$ at $O$ is a unit in a local parameter. Consequently
$$
R_-(Y)=\sum_{m\ge0}r_m^Y Y^m
\quad\text{has all }r_m^Y\text{ integral}.
\tag{851.26}
$$
There is no completed primitive with denominators in this zeroth kernel.

Since $\chi^{-e}=\theta^{k_p}$, orthogonality over all $[b]\in\mu_{q_0}$ selects exactly
$$
a_p=(p-1)k_p=(3-e)q_0/3\quad\pmod{q_0}.
$$
It follows that
$$
\frac{\mathcal S_0}{C_0}
 =-q_0\varpi^{a_p}
   \left(r_{a_p}^Y+\sum_{j\ge1}r_{a_p+jq_0}^Y T_0^j\right).
\tag{851.27}
$$
Every coefficient in the displayed tail is integral by (851.26), and its $j$th term belongs to $p^j\mathcal O$. Thus the entire infinite tail converges and is zero modulo $p$. This is a complete tail argument, not a first-block guess.

Equations (851.23) and (851.27) give, still retaining the phase,
$$
r_{a_p}^Y\equiv
-\frac{p}{3q_0D^{1/3}\varpi^{a_p}}S_D\pmod p.
\tag{851.28}
$$
The multiplier has valuation
$$
1-e/3-a_p/q_0=0.
$$
It is therefore a unit. No choice that this multiplier be $1$ has been made. Together with (851.19), this proves $r_{a_p}^Y\not\equiv0\pmod p$.

R589(589.10) proves that the formal logarithm $z$ agrees with $Y$ in every degree below $p^2$; equivalently, the first possible non-linear $\mu_{q_0}$-equivariant logarithm term has degree $p^2$. Since $0<a_p<q_0<p^2$, this comparison gives
$$
\mathfrak r_{k_p}:=[z^{(p-1)k_p}]R_-
             \equiv r_{a_p}^Y\ne0\pmod p.
\tag{851.29}
$$
The full logarithm and the full ordinary sigma series are not being reduced modulo $p$.

## 6. Original Cartier and sigma constants, primitive label and remaining factors

Here $2\le k_p<p$ and $k_p\equiv2\pmod6$. Thus R683(683.6), or R727(727.26), applies with exactly its original constants:
$$
\mathfrak r_{k_p}
 =c(-3B)^{-(k_p-1)}C_{k_p}\pmod p,
\quad c=(3/p)\alpha^2/2,\quad
B=(-1)^{(p-1)/2-(p-2)/3}
  \binom{(p-1)/2}{(p-2)/3}.
\tag{851.30}
$$
Both $c$ and $B$ are $p$ units. This proves the first assertion of (851.4). The even-branch square identity R697(697.2)--(697.3), equivalently R770(770.9), is
$$
C_{k_p}
 =-2^{-(k_p-1)}(k_p-1)!
       g_{(k_p-2)/6}^{\,2}.
\tag{851.31}
$$
Its multiplier is a unit because $k_p-1<p$. This proves the second assertion of (851.4), with the original sign and factorial.

For $p=6N+5$, the indices in (851.3) satisfy
$$
i_p+j_p=N-1,\qquad h_p=6i_p+7,
\qquad p-h_p-2=k_p.
$$
Also $h_p\equiv1\pmod3$ and
$$
3h_p=en-9.
$$
Any common prime divisor of $h_p$ and $n$ would divide $9$, whereas $3\nmid h_p$. Hence $(h_p,p+1)=1$ exactly; the assertion is not merely primitivity after removing $2$ and $3$.

At this particular original primitive label, R770's remaining sufficient condition is now
$$
\boxed{P_{h_p-1}(1/\sqrt{-3})\,f_{i_p}\ne0\pmod p,}
\tag{851.32}
$$
because its $g_{j_p}$ factor has been proved a unit. Neither factor in (851.32) has been proved uniformly here. The neighboring two-label Legendre theorem concerns its own labels and must not be used to reflect or move $f$ or $g$ between them. The full original target still permits all admissible primitive labels and is not replaced by this sufficient one-label window.

## Sources and verification scope

- [Rubin, *The “main conjectures” of Iwasawa theory for imaginary quadratic fields*](https://doi.org/10.1007/BF01239508), Invent. Math. 103 (1991), Theorem 11.1(i). The precise no-good-reduction scope was checked in [Rubin's own CIME/AWS lecture notes](https://swc-math.github.io/aws/1999/99RubinCM.pdf), first page, paragraph following the introductory theorem; it identifies this paper as [Ru2]. The current publisher link exposes the bibliographic page but not the subscription PDF, so this note does not claim a fresh full-page reading of the 1991 scan.
- [Kezuka--Li, Documenta Math. 25 (2020), 2115--2147](https://archive.ymsc.tsinghua.edu.cn/pacm_download/615/12104-liyx3.pdf): introduction after (1.2), Theorem 1.1, the Néron lattice preceding Theorem 2.1, and the discussion immediately after (2.2), pp. 2119--2120. These verify integrality, actual rank-zero nonvanishing, the period, the applicability of Rubin away from $2,3$, and finite Sha with Cassels square order for this family.
- R588(588R.14): original CRT identity, including conjugation and sign. R717 §5 and the cubic-companion note: original Gauss factor and the exact Mellin normalization.
- R589(589.6)--(589.10), R601 §5, R683(683.6), R697(697.2)--(697.3), R727 §6 and (727.26), R770(770.9): actual coordinate, rational kernel, complete Fourier extraction and the original even Cartier/sigma square.

This is a paper proof. No new arithmetic was executed locally or in Actions, and no new finite-prime window was opened.
