# R971 — The complete Wilson–Fourier source and the filtered full-span obstruction

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved complete finite-source identities, short CM ray separation,
and an infinite-prime obstruction to full spanning after the original
mask.** Every Gaussian and canonical-zeta term of R968 is retained. The
rank obstruction does not rule out inclusion of the particular target
$A/E_4$, or the weaker original marked nonvanishing. All arguments are
paper proofs; no mathematical computation is executed.

## 1. One complete primary source

Let $p=6N+5\ge41$, $q=Q^6$ and $e(q)=\eta^4/Q$. Work modulo $p$ and
$q^{L+1}$ with $6L+1<p$. For every ideal coprime to $2s$ use its unique
generator $\alpha\equiv1\pmod{2s}$, and put
$$
n_\alpha=\alpha\bar\alpha,\qquad
t_\alpha=\alpha/\bar\alpha\in\mu_{p+1},\qquad
\nu_\alpha=t_\alpha^6\in\mu_{N+1}.
\tag{971.1}
$$
The norm bound makes all displayed inverses legitimate. Since $p$ is
inert in $\mathbf Z[\zeta]$, $\alpha^p=\bar\alpha$ in $\mathbf F_{p^2}$.
The finite character has been absorbed by the primary generator; no
new choice of phase is made.

For Taylor indices with $a-b=1\pmod6$, the unit-orbit factor six cancels
the factor six in R968(968.2). Thus, writing $c=E_2/2$,
$$
T_{a,b}=e^{-1}
\sum_{r=0}^{\min(a,b)}\frac{(-c)^r}{r!(a-r)!(b-r)!}
\sum_{\substack{\alpha\equiv1\ (2s)\\n_\alpha\le6L+1}}
 \alpha^{a-r}\bar\alpha^{b-r}q^{(n_\alpha-1)/6}.
\tag{971.2}
$$
For the other unit classes $T_{a,b}=0$. Formula (971.2) is the complete
Gaussian expansion of the actual source. It does not replace it by a
pure harmonic theta coefficient.

## 2. Wilson's identity including every Gaussian term

Put $a=6i+4$, $0\le i<N$, and $b=p-6-a$. A term of R968(968.9) has
the form $T_{a,b+2-2M}$. It vanishes unless $M=0\pmod3$.

Define the explicit polynomial
$$
P_{M,r}(A)=\prod_{j=1-r}^{2M+r+3}(A+j).
\tag{971.3}
$$
When both factorial indices are nonnegative, Wilson's theorem gives
$$
\frac1{(a-r)!(p-4-a-2M-r)!}
=(-1)^rP_{M,r}(a).
\tag{971.4}
$$
Indeed the complementary factorial has index $a+2M+r+3$, whose parity
is $r+1$ because $a$ is even. The sign in (971.4) cancels the Gaussian
sign in (971.2), so the contribution is $c^rP_{M,r}(a)/r!$.

For $r>a$ the consecutive product (971.3) contains zero. If the other
factorial index is negative, it contains a factor $p$. Therefore the
formula extends with zero to those invalid ranges. A product of at
least $p$ consecutive factors is zero at every $a\in\mathbf F_p$, so
one may restrict to $M+r\le(p-5)/2$ without discarding any term.

The original CM monomial becomes, using Frobenius only in the finite
coefficient field,
$$
\begin{aligned}
\alpha^{a-r}\bar\alpha^{p-4-a-2M-r}
&=\frac{\alpha}{\bar\alpha^4}
 t_\alpha^a\bar\alpha^{-2M}n_\alpha^{-r}\\
&=\frac{\alpha}{\bar\alpha^4}
 t_\alpha^{4+M}\nu_\alpha^i n_\alpha^{-M-r}.
\end{aligned}
\tag{971.5}
$$
Consequently the **complete**, not just leading, Taylor coefficient is
$$
\boxed{
T_{a,b+2-2M}
=e^{-1}\sum_{r\ge0}\frac{c^r}{r!}P_{M,r}(a)
\sum_{\alpha\equiv1\ (2s)}
 \frac{\alpha}{\bar\alpha^4}
 t_\alpha^{4+M}\nu_\alpha^i n_\alpha^{-M-r}
 q^{(n_\alpha-1)/6}
}
\tag{971.6}
$$
for $M=0\pmod3$, with the same norm cutoff and the finite restrictions
above. No Taylor factorial at or beyond $p$ has been inverted.

## 3. All canonical-zeta corrections

Write $\beta_m=B_{2m}E_{2m}/(2m)!$ exactly as in R968. Define
$$
d_0(a)=(a+10)(a+11),\qquad d_1(a)=0,
$$
$$
d_M(a)=6(2M+21+2a)\beta_M
+36\sum_{\substack{u,v\ge2\\u+v=M}}\beta_u\beta_v
\quad(M\ge2).
\tag{971.7}
$$
Then the actual critical form is exactly
$$
\boxed{
Z_{6i+4,\,6(N-1-i)+1}
=\sum_{\substack{M\ge0\\M=0\ (3)}}
d_M(a)T_{a,b+2-2M},
}
\tag{971.8}
$$
where terms outside $2M\le b+2$ are zero, and each $T$ is given by
(971.6). The first coefficient is $(b-4)(b-5)=(a+10)(a+11)$ modulo $p$;
the single-zeta coefficient is
$6(2M+9-2b)=6(2M+21+2a)$ modulo $p$. The double sum is ordered, exactly
as in R968(968.9).

All norms, powers, Gaussian factors, eta denominator and canonical-zeta
coefficients have thus been retained in one finite Fourier source.
The original mask still multiplies the resulting column by
$$
w_i=\mathbf1_{(6i+7,p+1)=1}P_{6i+6}(1/s).
\tag{971.9}
$$
Neither that mask nor its Legendre factor is changed by (971.6)–(971.8).

In particular the $r=M=0$ factorial factor alone is
$(a+1)(a+2)(a+3)$, and its first-operator contribution is the product
of this cubic and $(a+10)(a+11)$. Those five factors are units for all
the present $a$. This statement concerns only one summand of the full
source and does not make the full source matrix invertible.

## 4. Distinct short CM rays give distinct Fourier nodes

Let $B=\lfloor(p-5)/12\rfloor$. The source norms needed for the true
Sturm rows satisfy
$$
n_\alpha\le6B+1<p/2.
\tag{971.10}
$$
Suppose two such primary points satisfy
$\nu_\alpha=\nu_\gamma$. Then
$t_\alpha/t_\gamma\in\mu_6$.

If this ratio lies in $\mu_3$, choose a unit $u$ with
$u/\bar u=t_\alpha/t_\gamma$, and put $\delta=u\gamma$.
Then $\alpha\bar\delta-\bar\alpha\delta$ is zero modulo $p$.
Writing $\alpha=A+B\zeta$, $\delta=C+D\zeta$, this difference is
$s(BC-AD)$ up to the immaterial fixed sign. The real absolute bound
$$
|BC-AD|\le\frac2{\sqrt3}\sqrt{n_\alpha n_\delta}<p
$$
forces this integer to be exactly zero. Thus
$\alpha/\delta\in\mathbf Q$.

If the ratio lies in $-\mu_3$, choose the unit so that
$t_\alpha/t_\delta=-1$. Now the integer trace
$\alpha\bar\delta+\bar\alpha\delta$ is divisible by $p$ and has
absolute value at most $2\sqrt{n_\alpha n_\delta}<p$. It is exactly
zero, so $\alpha/\delta\in s\mathbf Q$. This would make
$n_\alpha/n_\delta=3r^2$ for some nonzero $r\in\mathbf Q$, impossible
because both norms are units at $3$ and the right side has odd
$3$-adic valuation.

Therefore
$$
\boxed{
\nu_\alpha=\nu_\gamma
\iff \alpha=u r\gamma
\text{ for a unit }u\in\mu_6\text{ and }r\in\mathbf Q^\times,
}
\tag{971.11}
$$
within the strict norm range (971.10). The converse is immediate.
The two rows beyond the Sturm bound in R969 do not enter this lemma;
their norm cutoff need not satisfy the strict $p/2$ inequality.

## 5. The original mask prevents full spanning at infinitely many allowed primes

The successful finite full-rank cases of R969 cannot extend to a
full-spanning theorem at every sufficiently large allowed prime. This
already follows from the exact original primitive mask, before the
Legendre factor removes any additional columns.

Put
$$
M_0=5\cdot7\cdot11\cdot13\cdot17\cdot19\cdot23=37182145,
$$
$$
\varphi(M_0)=4\cdot6\cdot10\cdot12\cdot16\cdot18\cdot22
=18247680.
$$
These explicit products give
$$
2\varphi(M_0)=36495360<M_0,
\qquad M_0-2\varphi(M_0)=686785>0.
\tag{971.12}
$$
Consider the arithmetic progression
$$
p\equiv12M_0-1\pmod{36M_0}.
\tag{971.13}
$$
Its residue is coprime to $M_0$ and to $6$, so it is coprime to $36M_0$.
Dirichlet's theorem on primes in reduced arithmetic progressions
therefore gives infinitely many primes in (971.13). Write each of
them as
$$
p=6M_0t-1,\qquad t\equiv2\pmod6.
\tag{971.14}
$$
Since $M_0\equiv1\pmod6$, they satisfy
$p\equiv11\pmod{36}$. In particular they lie in the original
$p\equiv11\pmod{12}$, $p\equiv2\pmod9$ source class. Their associated
index is $N=M_0t-1$, which is odd because $t$ is even.

The original labels are exactly
$$
h=6i+7=6k+1,\qquad 0\le i<N,\quad 1\le k\le M_0t-1.
\tag{971.15}
$$
On the complete range $0\le k\le M_0t-1$, the map $k\mapsto6k+1$
contains every residue modulo $M_0$ exactly $t$ times. Exactly
$t\varphi(M_0)$ of these labels are coprime to $M_0$. Removing the first
one, $k=0$ and $h=1$, leaves exactly
$$
\#\{1\le k\le M_0t-1:(6k+1,M_0)=1\}=t\varphi(M_0)-1.
\tag{971.16}
$$
Every label primitive for the actual modulus $p+1=6M_0t$ must be among
these; factors of $t$ may remove more. The Legendre condition can
only decrease the number further. Consequently the number of
nonzero weighted source columns is at most $t\varphi(M_0)-1$.

On the other hand, the full-level target space has the exact dimension
$$
\dim M_{p-5}(\mathbf F_p)
=\left\lfloor\frac N2\right\rfloor+1
=\frac{M_0t}{2}.
\tag{971.17}
$$
Combining (971.12), (971.16) and (971.17) proves
$$
\boxed{
\operatorname{rank}_{\mathbf F_p}\{w_iZ_i:0\le i<N\}
\le t\varphi(M_0)-1
<\dim M_{p-5}(\mathbf F_p)
}
\tag{971.18}
$$
at infinitely many primes in the actual $r=2$ residue class. The
dimension deficit is at least $686785\,t/2+1$. No prime search,
primality assertion about the first term, or finite-rank computation
is needed for this result.

This is an obstruction only to the stronger claim that the complete
masked source spans *every* form of weight $p-5$. A proper subspace
can contain $A/E_4$, and can have nonzero evaluation at the original
mark. Thus (971.18) does not disprove either of those weaker targets,
and does not give a prime with all original same-label products zero.

## 6. The genuine remaining matrix problem

The finite Fourier nodes are distinct after the precise rational-ray
identification (971.11). However, (971.6) contains many different polynomial
operators in $a$, inverse norm powers and $t_\alpha^M$ weights. Because
$E_2$ has constant term one, the Gaussian terms with $r>0$ already
contribute to $q^0$. They cannot be discarded as a strictly lower
Fourier-row perturbation of the $r=0$ term. The eta and zeta products
also have their actual convolution coefficients.

Section 5 proves that the number of retained primitive labels is
strictly smaller than $\dim M_{p-5}$ at infinitely many original
allowed primes. Any argument from ordinary Vandermonde invertibility
must therefore establish a relation for the particular target or the
marked evaluation of this complete operator-valued source, with its
actual deleted columns. Distinctness of its short CM directions alone
proves no such relation.

The useful unresolved target remains
$A/E_4\in\operatorname{span}_{\mathbf F_p}\{w_iZ_i\}$, or another
genuine linear functional forcing at least one selected marked value
to be nonzero. This note supplies a full source formula for that
question and does not answer it.

## Sources and exact dependencies

- [R954](R954-original-odd-sigma-and-conductor-two-s-CM-evaluations.md)
  and [R964](R964-inverse-conductor-two-s-CM-family-and-original-sigma-heat-channel.md):
  the two actual finite-character CM families and their original phase.
- [R966](R966-single-conductor-two-s-CM-kernel-and-original-critical-jet.md):
  the complete common theta source and the unchanged same-label masks.
- [R968](R968-full-level-mixed-CM-jet-and-critical-factor.md), especially
  (968.2), (968.7), (968.9), (968.10) and (968.15): the Gaussian,
  canonical zeta, first-$p$ integrality, original marked value and
  integral full-level basis.
- [R969](R969-certified-filtered-full-level-span-at-three-primes.md)'s
  exact three-prime source contract: the finite Fourier cutoff
  motivating (971.10). Its finite successes do not enter the proof of
  (971.18).
- P. G. Lejeune Dirichlet, *Beweis des Satzes, dass jede unbegrenzte
  arithmetische Progression, deren erstes Glied und Differenz ganze
  Zahlen ohne gemeinschaftlichen Factor sind, unendlich viele
  Primzahlen enthält*, 1837, *Abhandlungen der Königlich Preussischen
  Akademie der Wissenschaften*, pp. 45–81. The original theorem is
  stated in the opening paragraph; see the
  [ETH-Bibliothek scan of the original paper in the collected works](https://www.e-rara.ch/download/pdf/5688045.pdf),
  printed p. 315, or the
  [translation of the original paper by R. Stephan](https://arxiv.org/abs/0808.1408).
  Only the standard infinitude theorem for a coprime residue and
  modulus is used, with that coprimality checked explicitly above.

No new mathematical computation was run. The universal full-span
route is ruled out, while the original marked nonvanishing and the
particular $A/E_4$ inclusion remain unresolved.
