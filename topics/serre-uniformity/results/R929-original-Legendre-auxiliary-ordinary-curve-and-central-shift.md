# R929 — The original Legendre auxiliary curve is ordinary in the split Gaussian class

Date: 2026-11-16. Status: **proved for every prime $p\ge41$ with $p\equiv5\pmod{12}$**. The unshifted Hasse value at the original Legendre argument is a unit. The shifted Legendre factor for the actual central primitive label is expressed exactly through its logarithmic derivative. This does not assert that the shifted factor or the original low normal coefficient is a unit.

## 1. Original argument and statement

Keep the original $s=\sqrt{-3}$ and Legendre normalization $P_d(1)=1$ of R727/R770. Put
$$
x_0=\frac1s,\qquad
\lambda_0=\frac{1-x_0}{2},\qquad
m=\frac{p-1}{2},\qquad
\mathcal A_p(X)=P_m(X)\pmod p.
\tag{929.1}
$$
The letter $X$ in $\mathcal A_p$ is a polynomial variable. Its derivative below is the ordinary polynomial derivative in $X$, not the Serre derivative or the original elliptic derivation $D$.

For $p\equiv5\pmod{12}$ one has $s^p=-s$, $x_0^p=-x_0$, and $m$ is even. Consequently
$$
\mathcal A_p(x_0),\quad x_0\mathcal A_p'(x_0)\in\mathbf F_p.
\tag{929.2}
$$
The new unit assertion is
$$
\boxed{\mathcal A_p(x_0)\in\mathbf F_p^\times.}
\tag{929.3}
$$
For the same actual primitive label used in R920/R924/R925,
$$
h=\frac{p+9}{2},\qquad
L_h=P_{h-1}(x_0),
\tag{929.4}
$$
the exact reduction is
$$
\boxed{
L_h=\frac{169\mathcal A_p(x_0)+896x_0\mathcal A_p'(x_0)}{105}.
}
\tag{929.5}
$$
All constants in this formula are reduced modulo $p$; its denominators and the coefficient $896x_0$ are units for $p\ge41$.

In particular the remaining Legendre zero condition is precisely
$$
\boxed{
L_h=0
\quad\Longleftrightarrow\quad
\frac{\mathcal A_p'(x_0)}{\mathcal A_p(x_0)}
=-\frac{169}{896x_0}.
}
\tag{929.6}
$$
The division on the left is justified by (929.3), not assumed. The proof gives no exclusion of the equality in (929.6).

## 2. The actual Legendre curve and a rational model

The original argument gives
$$
\lambda_0(1-\lambda_0)=\frac13,\qquad
1-\lambda_0+\lambda_0^2=\frac23.
\tag{929.7}
$$
Consider, over $\mathbf Q(s)$ or its reduction, the actual Legendre curve
$$
E_{\lambda_0}:Y^2=Z(Z-1)(Z-\lambda_0).
\tag{929.8}
$$
Its discriminant is $16/9$ and its invariant is
$$
j(E_{\lambda_0})
=256\frac{(1-\lambda_0+\lambda_0^2)^3}
          {\lambda_0^2(1-\lambda_0)^2}
=\frac{2048}{3}.
\tag{929.9}
$$
This is the auxiliary curve already located in the unitary note §8.1. It is distinct from the original sigma curve $E_0:y^2=x^3-1$.

The relation with the rational model used here is explicit. Substitute
$$
Z=u+\frac{1+\lambda_0}{3}.
$$
Equation (929.8) becomes
$$
Y^2=u^3-\frac29u-\frac{7}{81s}.
\tag{929.10}
$$
Set $d=3s$. With the quadratic-twist convention
$$
(y^2=u^3+au+b)^{(d)}:\quad
v^2=w^3+d^2aw+d^3b,
$$
the twist of (929.10) is exactly
$$
\boxed{E_*:\ v^2=w^3+6w+7.}
\tag{929.11}
$$
Indeed $d^2=-27$ and $d^3=-81s$. Over an extension containing $\sqrt d$, the pointed isomorphism is
$$
w=d\left(Z-\frac{1+\lambda_0}{3}\right),
\qquad v=d^{3/2}Y.
\tag{929.12}
$$
It pulls back $dw/(2v)$ to $d^{-1/2}dZ/(2Y)$. Thus the differential scale has not been dropped.

All translations, $d$, and this differential multiplier are units at every prime in question. In characteristic $p$ the construction can be performed over $\mathbf F_{p^2}(\sqrt d)$; no claim of an $\mathbf F_p$-isomorphism is made. Ordinarity and supersingularity are geometric properties, so this extension and twist preserve them.

For a check in the rational model itself,
$$
c_4(E_*)=-288,\qquad c_6(E_*)=-6048,\qquad
\Delta(E_*)=-2^4\,3^7,\qquad j(E_*)=\frac{2048}{3}.
\tag{929.13}
$$
In particular $E_*$ has good reduction at every $p\ge41$.

## 3. The four-torsion point and a nonzero Frobenius trace

Since $p\equiv1\pmod4$, choose $\iota\in\mathbf F_p$ with $\iota^2=-1$. The point
$$
P=(-4,9\iota)\in E_*(\mathbf F_p)
\tag{929.14}
$$
is defined because $(-4)^3+6(-4)+7=-81$. Its duplication slope is
$$
\frac{3(-4)^2+6}{2(9\iota)}
=\frac3\iota=-3\iota.
$$
The duplication formula consequently gives
$$
[2]P=(-1,0)\ne O.
\tag{929.15}
$$
The point on the right has order two, so $P$ has order exactly four. Therefore
$$
4\mid\#E_*(\mathbf F_p).
\tag{929.16}
$$

Write
$$
a_p(E_*)=p+1-\#E_*(\mathbf F_p)\in\mathbf Z.
$$
As $p+1\equiv2\pmod4$, (929.16) gives
$$
a_p(E_*)\equiv2\pmod4,\qquad a_p(E_*)\ne0.
\tag{929.17}
$$
Hasse's bound gives $|a_p(E_*)|\le2\sqrt p<p$ for $p>4$. Hence
$$
\boxed{a_p(E_*)\not\equiv0\pmod p.}
\tag{929.18}
$$
Only the torsion point and the bound are used; there is no point-count computation or finite-prime test.

## 4. Exact Hasse and twist factors

For a nonsingular cubic $f(Z)$ in characteristic $p$, put
$$
H(f)=[Z^{p-1}]\,f(Z)^m.
\tag{929.19}
$$
This is the usual scalar Hasse coefficient in the displayed Weierstrass differential. Its vanishing is equivalent to vanishing of Cartier on the invariant differential.

For a cubic defined over $\mathbf F_p$, the trace congruence
$$
a_p(y^2=f(Z))\equiv H(f)\pmod p
\tag{929.20}
$$
also follows directly from the character sum. The point count is
$p+1+\sum_{z\in\mathbf F_p}f(z)^m$ modulo $p$; the only positive exponent divisible by $p-1$ in the polynomial, whose degree is $3m<2(p-1)$, is $p-1$, and its power sum is $-1$.

For the Legendre cubic,
$$
\begin{aligned}
H\bigl(Z(Z-1)(Z-\lambda)\bigr)
&=(-1)^m\sum_{j=0}^{m}\binom mj^2\lambda^j\\
&=(-1)^mP_m(1-2\lambda)\quad\text{in }\mathbf F_p[\lambda].
\end{aligned}
\tag{929.21}
$$
For the last equality, expand the finite hypergeometric expression for $P_m$. In characteristic $p$ its coefficient
$(-1)^j\binom mj\binom{m+j}{j}$ equals $\binom mj^2$, because $2m=-1$.

Translation in the cubic leaves (929.19) unchanged. This can be read from the unchanged differential or checked coefficientwise: for $p\le k\le3m<2p-1$, the binomial coefficient $\binom{k}{p-1}$ is zero modulo $p$. Thus none of the higher terms produces a new $Z^{p-1}$ coefficient under translation.

The twist in (929.12) multiplies (929.19) by $d^m$. Indeed its cubic is $d^3 f(w/d)$, so the multiplier of the coefficient in question is $d^{3m-(p-1)}=d^m$. Combining this with (929.20–21), and using that $m$ is even, gives the exact phase
$$
a_p(E_*)\equiv d^m\mathcal A_p(x_0)\pmod p.
\tag{929.22}
$$
In the present prime class this multiplier is already rational over the residue field:
$$
\delta_p:=d^m=(-27)^{(p-1)/4}\in\mathbf F_p^\times,\qquad
\delta_p^2=-1.
\tag{929.23}
$$
For example, the latter equality follows from $d^p=-d$. The scalar is not set to one. Equations (929.18) and (929.22) prove (929.3), and also
$$
\mathcal A_p(x_0)=\delta_p^{-1}a_p(E_*)\pmod p.
\tag{929.24}
$$
Thus the actual auxiliary Legendre curve is ordinary throughout this prime class. A proposed argument conditional on its supersingularity would have an empty hypothesis here.

## 5. The exact four-step shift for the original label

The label in (929.4) is genuinely primitive in the original set. It is $1$ modulo six and odd, and
$$
2h-(p+1)=8.
$$
A common divisor of $h$ and $p+1$ would divide eight and be odd; hence it is one. Its indices are those of R925: if $p=12t+5$, then $h=6t+7$ and the original product is $f_tg_{t-1}$.

The finite Legendre formula gives, for $0\le n<p$,
$$
P_n(X)=P_{p-1-n}(X)\quad\text{in }\mathbf F_p[X].
\tag{929.25}
$$
To verify this, interchange the two hypergeometric parameters $-n,n+1$ modulo $p$. The terms beyond the smaller degree have a vanishing numerator and unit factorial denominator. For $n=h-1=m+4$, this gives
$$
L_h=P_{m-4}(x_0).
\tag{929.26}
$$
All indices are nonnegative in the stated range.

Put $A=P_m(X)$ and $C=P_{m-1}(X)$ temporarily. Starting with
$$
nP_n(X)=(2n-1)X P_{n-1}(X)-(n-1)P_{n-2}(X)
$$
and reducing $m=-1/2$ modulo $p$ yields
$$
\begin{aligned}
P_{m-2}(X)&=\frac{4XC-A}{3},\\
P_{m-3}(X)&=\frac{(32X^2-9)C-8XA}{15},\\
P_{m-4}(X)&=
 \frac{(384X^3-208X)C+(25-96X^2)A}{105}.
\end{aligned}
\tag{929.27}
$$
The last equality is obtained from
$7P_{m-4}=12XP_{m-3}-5P_{m-2}$, so no degree-dependent denominator has been silently inverted.

At $X=x_0$, where $X^2=-1/3$, the last row is
$$
P_{m-4}(x_0)=\frac{19A-112x_0C}{35}.
\tag{929.28}
$$
The original Legendre derivative formula is
$$
C=XA-2(1-X^2)A',
\tag{929.29}
$$
again using $m=-1/2$. Substituting $X^2=-1/3$ into (929.28–29) proves (929.5). Since (929.3) is now known, (929.6) follows.

The corresponding one-step formula for $p\equiv11\pmod{12}$ is already in the unitary note §8.1; it is not registered again as a new conclusion. The four-torsion argument here uses $p\equiv1\pmod4$ and proves no analogous unshifted unit assertion for that other prime class.

## 6. The remaining original coefficient

R925 proves, for exactly this same $h$, that the original critical jet is nonzero if and only if both
$$
L_h\ne0,\qquad Q_h'(0)\ne0.
\tag{929.30}
$$
Here $Q_h$ is its actual calibrated-map reduction, not a freely chosen polynomial. The new theorem makes the first condition the explicit inequality
$$
\frac{\mathcal A_p'(x_0)}{\mathcal A_p(x_0)}
\ne-\frac{169}{896x_0}.
\tag{929.31}
$$
It does not prove (929.31), the second condition in (929.30), or the all-prime same-label criterion. In particular an unshifted Hasse unit is not substituted for the shifted Legendre factor, and no value on this auxiliary curve is substituted for a value on the original $j=0$ sigma curve.

### Sources

- [R925](R925-original-low-normal-coefficients-and-same-label-critical-jet.md), §§1 and 6: the actual central label, original sigma product, and the exact low normal/critical-jet comparison.
- [Original unitary cross-heat note](../notes/2026-11-15-sigma-unitary-cross-heat-and-primitive-source.md), §8.1, (UH30–32): the already fixed Legendre argument, auxiliary $j=2048/3$, and the earlier one-step relation.
- J. S. Milne, [*Elliptic Curves*, second edition](https://www.jmilne.org/math/Books/EC2.pdf), Chapter IV, Theorem 9.4, printed p. 150: Hasse's bound. The model, twist, four-torsion point, trace congruence, phase and recurrence computations above are proved directly.
- B. H. Gross, [*A tameness criterion for Galois representations associated to modular forms (mod $p$)*](https://www.math.purdue.edu/~tongliu/seminar/Mlift/Gross.pdf), §1, printed p. 448: the Cartier definition of the Hasse invariant. The unit proof uses the explicit coefficient comparison (929.19–24).

No arithmetic was executed, and no new prime window was examined.
