# R986 — An explicit rational primitive and the original Lubin–Tate jet

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b. Authoring agent: handoff_audit; independently reviewed by root, with the normalized primitive independently checked by literature_frontier.

**Status: proved identities on the original elliptic curve; no new arithmetic execution and no nonvanishing assertion.** This gives an explicit rational representative of the finite Kronecker source in the square-root parameter, retains the extra Frobenius term in a pure Hurwitz coefficient, and constructs one rational function whose jet through degree $p^2-1$ is the original strict Lubin–Tate coordinate. Both kinds of coefficient can therefore be written as specified residues of rational differentials on the same original curve. No common scalar between the two kinds of coefficient is asserted.

This is an increment to R978, R981, and R984. The original parameter $t$ used in R984 is not silently changed there. The function $J$ below belongs to the explicitly specified $s$-coordinate Frobenius regularization.

## 1. Field, source, and three different coordinates

Let $p=6h+5\ge41$, $q=p^2$, and
$$
k=\mathbb F_{p^2},\qquad A=W(k),\qquad
d=\frac{p-1}{2}=3h+2,\qquad
b_0=\frac{p+1}{6}=h+1,\qquad
j_0=\frac{p-2}{3}=2h+1.
\tag{986.1}
$$
All rational functions below are actually defined over $\mathbb F_p$, although the original formal-group coefficient field is retained as $k$.

Keep the R978 source and its differential:
$$
E_+:y^2=x^3+1,\qquad \omega=\frac{dx}{2y},\qquad
t=-x/y,\qquad (g_2,g_3)=(0,-4).
\tag{986.2}
$$
At the origin $O$, choose the formal square-root parameter $s=x^{-1/2}$ with $s=t+O(t^7)$. Then
$$
x=s^{-2},\qquad y=-s^{-3}\sqrt{1+s^6},\qquad
t=\frac{s}{\sqrt{1+s^6}},\qquad
\omega=\frac{ds}{\sqrt{1+s^6}}.
\tag{986.3}
$$
This is a strict integral change of formal parameter. The parameter $s$ is **not** a rational function on $E_+$; the rationality of each function used later is proved from its displayed expression in $x,y$.

Let $T$ be R978's fixed strict Lubin–Tate parameter, for which the formal group has $[-p](T)=-pT+T^q$. If $s=g_s(T)$ is the strict integral isomorphism to (986.3), then
$$
L(s):=\int_0^s\omega
=s\sum_{i\ge0}\frac{\binom{-1/2}{i}}{6i+1}s^{6i},
\qquad
L(g_s(T))=l_{\rm LT}(T)=T+O(T^q).
\tag{986.4}
$$
Every coefficient of $L$ below degree $q$ is integral by R978/R981. A congruence involving $L$ below will mean this integral finite jet, never reduction of its coefficient of degree $q$.

The pure numbers and the fixed supersingular unit are
$$
\log\frac{\sigma_+(z)}z=-\sum_{N\ge4}\frac{\mathcal G_N}{N}z^N,
\qquad
\beta=\frac{\overline{E_{p+1}(E_+,\omega)}}{12}\in\mathbb F_p^\times.
\tag{986.5}
$$
No factorial, period change, or Gaussian is included in $\mathcal G_N$.

## 2. The unit is a specified binomial coefficient

The source normalization gives
$$
\boxed{\quad
\beta=\binom d{b_0}=\binom d{j_0}\pmod p.
\quad}
\tag{986.6}
$$
Here $d-b_0=j_0$, and all factorials are units.

For a direct check that includes the scale, use the characteristic-zero residue identity of R981 at $N=p+1$ before dividing by $N-1$:
$$
p\mathcal G_{p+1}
=[X^{b_0}](1+X)^{-1/2}f(X)^{-p},
\qquad
f(X)=\sum_{i\ge0}\frac{\binom{-1/2}{i}}{6i+1}X^i.
$$
All needed $f$ coefficients are integral, and $b_0<p$. Thus $f(X)^{-p}\equiv1\pmod{p,X^{b_0+1}}$. The right side is $\binom{-1/2}{b_0}\equiv\binom d{b_0}$. Robert's original normalization, used in R980 and R984, is $p\mathcal G_{p+1}\equiv E_{p+1}/12$, proving (986.6). In particular this does not replace $E_{p+1}$ by an arbitrarily normalized nonzero value.

Equivalently, Cartier on the original curve gives
$$
C(x\omega)=\beta\,\omega.
\tag{986.7}
$$
Indeed $x\omega=x(1+x^3)^d\,dx/(2y^p)$. The only monomial in the numerator whose exponent is $p-1$ is indexed by $j_0$, with coefficient $\binom d{j_0}$. There is no second exponent congruent to $p-1$ in the range $1\le3j+1\le3d+1<2p-1$. Since the coefficient lies in $\mathbb F_p$, its Cartier $p$th root is itself.

## 3. An explicit primitive of the actual $s$-coordinate differential

Define the rational function
$$
\boxed{\quad
J=-\frac1{2y^p}
\sum_{\substack{0\le j\le d\\j\ne j_0}}
\frac{\binom dj}{3j+2}\,x^{3j+2}
\in\mathbb F_p(E_+).
\quad}
\tag{986.8}
$$
Every displayed denominator is a unit. In the range $2\le3j+2\le3d+2<2p$, the unique multiple of $p$ occurs at $j=j_0$ and has been omitted. Differentiation in characteristic $p$, with $d(y^{-p})=0$, yields
$$
\begin{aligned}
dJ
&=\frac{-x(1+x^3)^d+\beta x^{p-1}}{2y^p}\,dx\\
&=\bigl(-x+\beta t^{p-1}\bigr)\omega.
\end{aligned}
\tag{986.9}
$$

At $O$, the highest term $j=d$ has coefficient
$$
\frac1{2(3d+2)}t^{-1}=\frac1{3p+1}t^{-1}=t^{-1}
\quad\hbox{in }k((t)).
$$
The remaining terms have order at least five, and the parameter change $s=t+O(t^7)$ preserves the simple principal part. Therefore
$$
J=t^{-1}+O(t^5)=s^{-1}+O(s^5).
\tag{986.10}
$$
In particular the constant coefficient is zero. Away from $O$, the only possible poles of $J$ are the three points $y=0$, each of order at most $p$. Formula (986.8) is regular at every other point. These poles are permitted; $J$ is not claimed to be a regular function on the complete curve.

For comparison with R981's one-variable polynomials, set
$$
P_-(X)=\sum_{\substack{0\le b\le d\\b\ne b_0}}
\frac{\binom db}{1-6b}X^b.
$$
Replacing $j$ by $d-b$ in (986.8) gives the exact characteristic-$p$ local expression
$$
J(s)=s^{-1}P_-(s^6)(1+s^{6p})^{-1/2}.
\tag{986.11}
$$
This formula also verifies the principal part and the missing resonance. The expression in $x,y$ is what proves rationality on $E_+$.

### 3.1 Identification with the genuine Frobenius regularization

Apply the formal-group statement of Guerzhoy used in R984 to the strict integral parameter $s$. The CM weight-two term is zero and the same coefficient $\mu\in A$ satisfies $\overline\mu=-\beta$. Thus
$$
\mathcal R_s(s)=\zeta(L(s))-\frac\mu p L^\varphi(s^p)
\in s^{-1}+sA[[s]].
\tag{986.12}
$$
The superscript $\varphi$ acts on coefficients. In this model the logarithm coefficients are rational, but retaining the notation fixes the comparison with the original coefficient Frobenius.

Differentiating before reduction and using (986.3) gives
$$
d\overline{\mathcal R_s}
=-x\omega+\beta s^{p-1}(1+s^{6p})^{-1/2}\,ds
=\bigl(-x+\beta t^{p-1}\bigr)\omega.
\tag{986.13}
$$
The last equality uses $s(1+s^6)^{-1/2}=t$. Thus the right side is a rational differential on $E_+$ despite the use of the formal parameter $s$ in its construction.

Equations (986.9), (986.10), and (986.13), including the zero constant coefficients, imply
$$
\boxed{\quad
\overline{\mathcal R_s}(s)-J(s)=h_s(s)^p,
\qquad h_s(s)\in s\,k[[s]].
\quad}
\tag{986.14}
$$
This is an identity of local series. Its proof is simply that a series of derivative zero over a perfect field contains only powers divisible by $p$, with neither a negative term nor a constant here. It does not assert that $h_s$ is rational or zero.

## 4. The pure coefficient retains its Frobenius correction

Let $N$ satisfy
$$
6\mid N,\qquad 4\le N<q-1,\qquad p\nmid N-1.
\tag{986.15}
$$
This includes all four original R981 indices and its two extra diagnostic indices. For a rational function on $E_+$, its expression in $T$ means evaluation at the original formal point $s=g_s(T)$.

Since $L(g_s(T))=T+O(T^q)$, the expansions of $x$ and $\wp_+(T)$ agree below degree $q-3$. Also $\omega=dT+O(T^{q-1})\,dT$ in characteristic zero, and its reduced jet is $dT$ in the range needed here. Taking the coefficient of $T^{N-2}$ in (986.9) therefore gives
$$
\boxed{\quad
\overline{\mathcal G_N}
=-[T^{N-1}]J
+\frac\beta{N-1}[T^{N-2}]t^{p-1}.
\quad}
\tag{986.16}
$$
Every coefficient in this equation is a specified coefficient on the same source, and every scalar denominator is a unit.

The second term in (986.16) must be retained. Although strict integral coordinate changes preserve $\lambda,\mu$ in Guerzhoy's basis, they do not identify
$$
\frac1pL^\varphi(g_s(T)^p)
\quad\hbox{with}\quad
\frac1p l_{\rm LT}^\varphi(T^p).
$$
Their difference can have nonzero coefficients whose degrees are not multiples of $p$. Formula (986.16) follows directly from the actual rational differential and does not require this false substitution. The general coordinate-carry issue in the original $t$-coordinate is treated separately in R985.

For an optional explicit extraction of the correction using R981's series, put $M=N/6$. Residue change of variables gives
$$
[T^{N-2}]t^{p-1}
=[X^{M-b_0}](1+X^p)^{-1/2}\,\overline f(X)^{1-N}.
\tag{986.17}
$$
If $M-b_0<0$, the right side is zero. To prove this, insert $t=s(1+s^6)^{-1/2}$, $T=L(s)$, and $dT=(1+s^6)^{-1/2}ds$ in the coefficient residue. The required power of $s$ is $N-p-1=6(M-b_0)$, and the two powers of $1+s^6$ combine to exponent $-p/2$. All substitutions only use integral coefficients below degree $q$.

## 5. A compact rational function realizes the entire original jet below $q$

Define a second rational primitive
$$
R_0=\frac1{2y^p}
\sum_{j=0}^d\frac{\binom dj}{3j+1}x^{3j+1}.
\tag{986.18}
$$
No denominator here is divisible by $p$. In the range $1\le3j+1\le3d+1<2p$, a possible multiple could only be $p$; but $p\equiv2\pmod3$ cannot equal $3j+1$. Direct differentiation gives
$$
dR_0=\omega,\qquad R_0=t+O(t^7).
\tag{986.19}
$$
At $O$, its leading coefficient is $-1/(3p-1)=1$ in $k$. Its only possible poles are at $y=0$, of order at most $p$.

Let $A_0$ denote R981's first polynomial, with a subscript to distinguish it from the Witt coefficient ring:
$$
A_0(X)=\sum_{b=0}^d\frac{\binom db}{6b+1}X^b.
$$
The denominators $6b+1$ are units in this range. Changing $j$ to $d-b$ in (986.18) gives
$$
R_0(s)=sA_0(s^6)(1+s^{6p})^{-1/2}.
\tag{986.20}
$$

Now set
$$
H=\frac13\left(\frac{x^2}{y}+J\right)\in\mathbb F_p(E_+).
\tag{986.21}
$$
The simple poles at $O$ cancel: $x^2/y=-s^{-1}+O(s^5)$ and $J=s^{-1}+O(s^5)$. Therefore $H$ is regular at $O$ with zero constant coefficient. All of its other possible poles are again at $y=0$, of order at most $p$.

The elementary differential identity
$$
\frac13\left(d\left(\frac{x^2}{y}\right)-x\omega\right)
=\frac{x\,dx}{2y^3}
=s^4(1+s^6)^{-3/2}\,ds
\tag{986.22}
$$
and (986.9) imply
$$
dH=s^4(1+s^6)^{-3/2}\,ds
+\frac\beta3t^{p-1}\omega.
\tag{986.23}
$$
Write
$$
D(Y)=\sum_{i\ge0}\frac{(2i+1)\binom{-1/2}{i}}{6i+5}Y^i,
\qquad Z_{<p}(s)=\sum_{i=0}^{h-1}
\frac{(2i+1)\binom{-1/2}{i}}{6i+5}s^{6i+5}.
\tag{986.24}
$$
Only the displayed finite polynomial is reduced modulo $p$. The next term would have degree $p$ and denominator $p$; it is not reduced or discarded as zero. Differentiating the finite polynomial agrees with the first term of (986.23) below degree $p-1$, since
$$
\sum_{i\ge0}(2i+1)\binom{-1/2}{i}Y^i=(1+Y)^{-3/2}.
$$
The second term of (986.23) has order $p-1$. Both $H$ and $Z_{<p}$ have zero constant coefficient, and all positive integers below $p$ are invertible. Hence
$$
\boxed{\quad H(s)\equiv Z_{<p}(s)\pmod{s^p}.
\quad}
\tag{986.25}
$$
In particular $H(s)=s^5/5+O(s^{11})$, with nonzero leading coefficient.

Keep the exact nonzero Wilson-resonance constant of R981:
$$
e=\frac{5p-1}{6},\qquad
\mathfrak c_p=(-1)^{e+1}4^{-e}\frac{(2e-p)!}{(e!)^2}\in\mathbb F_p^\times.
\tag{986.26}
$$
Define
$$
\boxed{\quad
\mathcal T=R_0+\mathfrak c_p H^p\in\mathbb F_p(E_+).
\quad}
\tag{986.27}
$$
It is regular at $O$, has derivative $d\mathcal T=\omega$, and its only possible poles elsewhere are at $y=0$, of order at most $p^2$.

The complete source-sensitive jet assertion is
$$
\boxed{\quad
\mathcal T(s)\equiv\overline{L_{<q}(s)}\pmod{s^q},
\qquad
\mathcal T(g_s(T))=T+O(T^q)\quad\text{in }k[[T]].
\quad}
\tag{986.28}
$$
To prove it, multiply R981's two-digit formula by $s$ and use (986.20):
$$
\overline{L_{<q}(s)}
\equiv R_0(s)+\mathfrak c_p s^{5p}D(s^{6p})
\pmod{s^q}.
$$
Only $i<h$ occur in the second term, so it is exactly $\mathfrak c_p Z_{<p}(s)^p$ in this quotient. Equation (986.25) replaces it with $\mathfrak c_pH(s)^p$. Finally the original strict isomorphism identifies $L_{<q}(g_s(T))$ with $T$ below degree $q$, proving both assertions.

This proof keeps the unique resonant column of R981. In fact
$$
\mathcal T(s)-R_0(s)=\frac{\mathfrak c_p}{5}s^{5p}+O(s^{11p}),
\tag{986.29}
$$
so omitting that column already changes the first possible coefficient of degree $5p$. The rational function $\mathcal T$ is a representative of a finite jet in characteristic $p$; it is not asserted to be a group homomorphism, an integral global logarithm, or a replacement for the original characteristic-zero Lubin–Tate torsion point in R978.

### 5.1 A normalized two-function form

The expression for $\mathcal T$ has the following simpler exact form:
$$
\boxed{\quad
Z=-\beta^{-1}D^{p-2}x,\qquad D=\omega^{-1}d,
\qquad
\mathcal T=Z+\beta^{-1}J^p.
\quad}
\tag{986.29a}
$$
Both equalities are in $\mathbb F_p(E_+)$. In particular this is a relation between specified rational functions, not an equality only up to a $p$th power. The function $Z$ has its only pole at $O$, of order $p$, whereas $J$ is the function (986.8) with the stated finite poles. We give all normalizations in the proof.

First, the invariant derivation is
$$
Dx=2y,\qquad Dy=3x^2.
$$
Its $p$th iterate is again an invariant derivation, so it is a constant multiple of $D$. The source automorphism
$$
\alpha_\xi(x,y)=(\xi^{-2}x,\xi^{-3}y),\qquad \xi\in\mu_6,
\qquad \alpha_\xi^*\omega=\xi\omega
$$
acts on the two derivations with weights $-p$ and $-1$. Since $p\equiv-1\pmod6$, these weights are distinct, forcing $D^p=0$.

It follows that $D^{p-1}x\in k(E_+)^p$. Its only possible pole is at $O$, of order at most $p+1$. The order of a pole of a $p$th power is divisible by $p$, so its $p$th root has at most a simple pole at $O$. On a curve of genus one there is no nonconstant rational function with only one pole of order at most one. Thus $D^{p-1}x$ is constant.

Its value is fixed by the original differential. In the actual strict Lubin–Tate parameter, the coefficient of $T^{p-1}$ in $x$ is $p\mathcal G_{p+1}\equiv\beta$. The logarithm is $T+O(T^q)$, so replacing $D$ by $d/dT$ cannot affect the constant term after $p-1$ differentiations: a correction first occurs at a strictly positive degree. The derivative of the leading $T^{-2}$ term is zero after $p-1$ differentiations in characteristic $p$, and Wilson's formula yields
$$
D^{p-1}x=(p-1)!\,\beta=-\beta.
\tag{986.29b}
$$
Consequently $dZ=\omega$. Its leading term is $-\beta^{-1}t^{-p}$, because the leading term of $D^{p-2}x$ is $t^{-p}$. Its constant term is zero by its $\mu_6$ character, which is weight one. This also proves uniqueness: two primitives with only an $O$-pole of order at most $p$ differ by a $p$th power with a root having at most one simple pole, hence by a constant; the zero constant fixes it.

Next, $d(R_0-Z)=0$, so $R_0-Z=u^p$ for some $u\in k(E_+)$. The possible poles of $u$ have order at most one at the four points $E_+[2]$. On the genus-one curve the space of such functions has dimension four and the following explicit basis:
$$
L(E_+[2])=\operatorname{span}_k
\left\{1,\frac1y,\frac xy,\frac{x^2}y\right\}.
$$
The four functions are linearly independent and have the indicated pole bounds, proving the basis assertion. Their $\mu_6$ weights are $0,3,1,-1$, respectively. Both $R_0$ and $Z$ have weight one. As $p\equiv-1\pmod6$, their difference's unique $p$th root has weight $-1$. Thus $u$ is a multiple of $x^2/y$; no constant summand has this character. Comparing principal parts at $O$ gives the exact equality
$$
\boxed{\quad R_0=Z-\beta^{-1}(x^2/y)^p.\quad}
\tag{986.29c}
$$

Finally the constants in (986.6) and (986.26) satisfy
$$
\boxed{\quad \mathfrak c_p\beta=3.\quad}
\tag{986.29d}
$$
Here is a direct factorial proof. Put $k_0=(p+1)/6$, so $p=6k_0-1$, $e=5k_0-1$, and $\beta=\binom{-1/2}{k_0}$. Multiplying the two displayed formulas gives
$$
\mathfrak c_p\beta
=4^{-p}\frac{(4k_0-1)!(2k_0)!}{(5k_0-1)!^2k_0!^2}\pmod p;
$$
the sign is $(-1)^{6k_0}=1$. Wilson gives
$$
(4k_0-1)!(2k_0-1)!=1,
\qquad
(5k_0-1)!(k_0-1)!=(-1)^{k_0}.
$$
Since $4^{-p}=1/4$ in $\mathbb F_p$, the product becomes $1/(2k_0)=3$. All factorial arguments lie below $p$.

Substitute (986.29c), (986.29d), and $H=(x^2/y+J)/3$ into (986.27). In characteristic $p$, $3^p=3$ and taking $p$th powers is additive. This gives
$$
R_0+\mathfrak c_pH^p
=Z-\beta^{-1}(x^2/y)^p
+\beta^{-1}\bigl((x^2/y)^p+J^p\bigr)
=Z+\beta^{-1}J^p,
$$
proving (986.29a). Its two apparent poles of order $p$ at $O$ cancel with exactly the original scale. All the jet and residue conclusions retain the full $J^p$ term.

## 6. Pure and mixed coefficients as residues on this one curve

Because $\mathcal T$ is a local parameter at $O$ and $d\mathcal T=\omega$, every coefficient with respect to $\mathcal T$ is an ordinary rational residue. For (986.15), (986.28) and the pole order two of $x$ give
$$
\boxed{\quad
\overline{\mathcal G_N}
=\frac1{N-1}\operatorname{Res}_O
\bigl(x\,\mathcal T^{-(N-1)}\omega\bigr).
\quad}
\tag{986.30}
$$
Indeed $\mathcal T=T+O(T^q)$ changes the Laurent series of a function of pole order two only from degree $q-3$ onward; the required exponent is $N-2<q-3$. Formula (986.16) can equivalently be written entirely in this rational parameter:
$$
\overline{\mathcal G_N}
=-[\mathcal T^{N-1}]J
+\frac\beta{N-1}[\mathcal T^{N-2}]t^{p-1}.
\tag{986.31}
$$

For the mixed source, keep the connection functions of R984:
$$
e^{-\zeta(z)W}\frac{\sigma_+(z+W)}{\sigma_+(z)\sigma_+(W)}
=\sum_{j\ge0}L_j(z)W^{j-1}.
$$
For $0\le j\le p-2$, their reductions belong to $k[x,y]$. If $1\le n\le p-2$, define the specified rational function
$$
\mathcal B_n=
\sum_{j=0}^n\frac{J^{n-j}}{(n-j)!}\,\overline L_j
\in k(E_+).
\tag{986.32}
$$
All factorials are units. The same finite-kernel argument as R984, now using the explicitly identified remainder (986.14), gives
$$
c_n^+=[z^nW^{n-1}]
\frac{\sigma_+(z+W)}{\sigma_+(z)\sigma_+(W)},
\qquad
\overline{c_n^+}=[T^n]\mathcal B_n.
\tag{986.33}
$$
For clarity, the exponential Frobenius correction begins in $s^pW$; after multiplication by a theta function with only a simple $s$-pole, it cannot affect an $s$- or $T$-coefficient of degree at most $p-2$. The change from the integral remainder to $J$ contributes $\exp(-h_s^pW)$, which satisfies the same bound. Thus the entire $\mathcal B_n$ has at most a simple pole at $O$, although its individual summands may have higher poles. This argument retains every original coefficient and does not discard the regular part of $J$.

The same rational parameter therefore gives
$$
\boxed{\quad
\overline{c_n^+}
=\operatorname{Res}_O
\bigl(\mathcal B_n\mathcal T^{-n-1}\omega\bigr).
\quad}
\tag{986.34}
$$
Here the change $T\mapsto\mathcal T$ only begins affecting a function with a simple pole in degree $q-2$, well above $n$.

There is a further finite simplification for this mixed coefficient alone:
$$
\boxed{\quad
\overline{c_n^+}
=\operatorname{Res}_O
\bigl(\mathcal B_n R_0^{-n-1}\omega\bigr),
\qquad 1\le n\le p-2.
\quad}
\tag{986.35}
$$
Indeed (986.29) gives $\mathcal T-R_0=O(s^{5p})$. Both are local parameters with differential $\omega$, so the first possible coefficient change of a function of pole order one occurs in degree $5p-2>n$. No corresponding replacement is made for a general near-$p^2$ pure coefficient in (986.30).

Equations (986.30) and (986.34) now involve only the explicit rational functions $R_0,J,H,\mathcal T$, the finite integral connection functions, and residues on $E_+$. They do not need an unspecified strict formal isomorphism as input. The two numerators and the two exponents remain different.

## 7. Scope and remaining question

The exact improvement is the explicit rational formula (986.8) and the finite source jet (986.27)–(986.28), with the originally normalized Wilson-resonance constant. In particular, the first Frobenius correction is an identified function, not a guessed common scalar or a freely chosen period.

No sign, root, CM marking, or characteristic-zero torsion point in R972/R978 has been changed. The phase conversion from $c_n^+$ to the $g_3=+4$ coefficient is still the separate R979 conversion.

Nothing here proves either rational residue nonzero. The discarded common-scalar proposal tested in R983 is not restored by identifying their underlying curve or by giving both residues the same local parameter. A further argument must use the actual functions in (986.30) and (986.34), including the $\mathfrak c_pH^p$ term and the correction in (986.31).

## Sources

1. [R978](../results/R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md): original source, strict Lubin–Tate parameter, and integral jet below degree $p^2$.
2. [R980](../results/R980-original-level-one-Hurwitz-reflection-and-distinct-mirror-pairs.md): $\mathcal G_N=S_N(E_+,\omega)$ and the exact normalization of $E_{p+1}/12$. Robert's $pS_{p+1}$ normalization is also used in R984.
3. [R981](../results/R981-original-pure-Hurwitz-residue-compression.md): residue identity, all integral coefficients below degree $q$, two-digit formula, and the complete resonance constant $\mathfrak c_p$.
4. [R984](R984-frobenius-regularized-finite-Kronecker-kernel-and-rational-Cartier-descent.md): the actual finite integral kernel, rational connection functions, and $\overline\mu=-\beta$.
5. P. Guerzhoy, *On the $p$-adic values of the weight two Eisenstein series for supersingular primes*, Research in the Mathematical Sciences **12**, article 64 (2025), equation (4), Proposition 1, Corollary 1, equation (14), and Theorem 1. [Author manuscript](https://arxiv.org/pdf/2403.02592). Equation (4) explicitly allows any strictly integrally isomorphic formal-group law; it preserves $\lambda,\mu$, not equality of the integral remainders after arbitrary coordinate substitution.
6. K. Bannai, S. Kobayashi, T. Tsuji, *On the de Rham and $p$-adic realizations of the elliptic polylogarithm for CM elliptic curves*, Ann. Sci. Éc. Norm. Sup. **43** (2010), 185–234, Definitions 1.5–1.6, for the connection functions. Their small-index integral refinement is proved in R984.
