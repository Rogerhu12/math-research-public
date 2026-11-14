# R726 — Uniform primitive nonvanishing for the original CM point difference

Date: 2026-11-14. **Status: proved.** There is an absolute, effective
constant $p_0$ such that the original R616 point-difference and rank
conclusions hold for every prime $p>p_0$ with $p\equiv2,5\pmod9$.
There is no hypothesis on the factorization of $(p+1)/3$.
This removes the asymptotic primitive-nonvanishing premise for this
original factor. It does not prove Serre uniformity or exclude the
remaining zeros of the actual height equations.

## 1. The same original families and the statement

Use the objects and normalizations of R616 and R714. Thus

$$
K=\mathbf Q(\zeta),\quad \zeta^2+\zeta+1=0,\quad
M=(p+1)/3,\quad R=\operatorname{rad}(M),\quad
\mathcal D=\{o:o\mid R,\ o>2\},
$$
$$
L=\log p,\qquad c=\frac{\pi}{3\sqrt3},\qquad t=c/p,\qquad
S=\frac32(1+1/p)<2,\qquad J=|\mathcal D|=2^{\omega(M)}-2.
\tag{726.1}
$$

The set $\mathcal V$ consists of primary visible elements
$\beta=a+b\zeta\equiv1\pmod3$, with $\gcd(a,b)=1$ and
$(N\beta,6p)=1$. Set

$$
o(\beta)=\operatorname{ord}\bigl((\bar\beta/\beta)^3\bmod p\bigr),
\qquad
\mathcal B_p=
 \sum_{o\in\mathcal D}\frac1{\varphi(o)}
 \sum_{\substack{\beta\in\mathcal V\\o(\beta)=o}}
       \frac{e^{-c|\beta|^2/p}}{|\beta|}.
\tag{726.2}
$$

Reduction is in $\mathcal O_K/p=\mathbf F_{p^2}$, where conjugation
is the $p$-power map. The order in (726.2) is therefore exactly
R714's order of $\beta^{3(p-1)}$; it is not an order in the split
multiplicative group $\mathbf F_p^\times$.

**Theorem 726.1.** Uniformly over all the indicated primes,

$$
\boxed{\mathcal B_p\longrightarrow0\qquad(p\longrightarrow\infty).}
\tag{726.3}
$$

All estimates below are effective with absolute constants. In
particular the convergence does not use a density statement or an
unproved assertion about prime factors of $p+1$.

**Theorem 726.2.** For all sufficiently large such primes, the original
specified character $\theta_{-1}$ and the original positive cubic
quotient of $J_{X_1}$ satisfy

$$
\boxed{
 L'(g_{-1,+},1)L(g_{-1,-},1)\ne0,\qquad
 A_{-1,1}(\mathbf Q)\otimes\mathbf Q=F\beta_{-1},
}
\tag{726.4}
$$
$$
\beta_{-1}=q_1[c_1-c_0],\qquad
\operatorname{rank}A_{-1,1}(\mathbf Q)=\dim A_{-1,1},
\tag{726.5}
$$

and their original $p$-adic logarithm is the isomorphism specified in
R616. The opposite cubic twist remains only the second factor in
the original point-difference formula.

The proof of (726.3) occupies §§2–7. Section 8 checks the two different
analytic kernels and the exact original-family interface.

## 2. Uniform counts on individual projective lines

For $o\in\mathcal D$, write

$$
N_o(T)=\#\{\beta\in\mathcal V:o(\beta)=o,\ |\beta|\le T\}.
$$

There are $\varphi(o)$ elements of order $o$ in the quotient torus
of order $M$. Each has three lifts under $\alpha\mapsto\alpha^3$
in the norm-one torus of order $p+1$. Each lift of
$\alpha=\bar\beta/\beta$ specifies one projective line in
$\mathcal O_K/p$ over $\mathbf F_p$.

Its inverse image in $\mathcal O_K$ is an index-$p$ lattice. R614
(614.15), also used in R714 (714.15), gives the uniform visible-point
bound $4+6T^2/p$ on every such line. This bound includes lines with a
very short vector. Indeed, below the second successive minimum all
lattice points lie on a single rational direction, which has at most
two primitive integral points. Above that minimum the usual
$T/\lambda_1$ boundary term is bounded by a constant times
$T^2/\det\Lambda$. Thus no unbounded collection of nonprimitive
multiples of a short vector occurs in the count.

The global packing bound of R714 (714.12) and the line bound give

$$
\boxed{
 N_o(T)\le \min\{9T^2,\ \varphi(o)(12+18T^2/p)\}\quad(T\ge1).
}
\tag{726.6}
$$

All nonzero lattice elements have absolute value at least one.

Let $f(T)=e^{-cT^2/p}/T$. Partial summation and
$\int_Y^\infty T^2(-f'(T))\,dT\le2\sqrt{\pi p/c}$
give, for every $Y\ge1$,

$$
\frac1{\varphi(o)}
 \sum_{\substack{\beta\in\mathcal V,\ o(\beta)=o\\|\beta|>Y}}
 f(|\beta|)
 \le\frac{12}{Y}+\frac{C}{\sqrt p}.
\tag{726.7}
$$

The constant $C$ is absolute; one can take $36\sqrt{\pi/c}$.
The negative boundary term at $Y$ has only been discarded, and the
integral includes the entire infinite tail.

Put $Y=\sqrt{\varphi(o)}$. The contribution below $Y$ is at most
$18Y/\varphi(o)$ by global packing and partial summation, so

$$
\boxed{
 \frac1{\varphi(o)}
 \sum_{\substack{\beta\in\mathcal V\\o(\beta)=o}}f(|\beta|)
 \le \frac{30}{\sqrt{\varphi(o)}}+\frac{C}{\sqrt p}.
}
\tag{726.8}
$$

This estimate is uniform in both $o$ and the particular projective
lines. Using only its constant term and summing it over all orders
would be insufficient; the following sections retain the size of $o$.

## 3. Elementary prime-product bounds

We record the elementary estimates, with enough detail to make their
uniformity and effectiveness explicit. No prime number theorem is
needed.

Write $\vartheta(x)=\sum_{\ell\le x}\log\ell$ for the sum over primes.
The divisibility of $\prod_{n<\ell\le2n}\ell$ into
$\binom{2n}{n}$ gives
$\vartheta(2n)-\vartheta(n)\le2n\log2$.
Summing on dyadic integer endpoints and then enclosing a real $x$
between two such endpoints yields

$$
\vartheta(x)\le4(\log2)x<3x.
$$

Separating primes below and above $\sqrt x$ gives, for $x\ge2$,

$$
\pi(x)\le\sqrt x+\frac{2\vartheta(x)}{\log x}
       \le\frac{8x}{\log x}.
\tag{726.9}
$$

Here $\log x\le2\sqrt x$ suffices for the last inequality.

### 3.1 The reciprocal-totient product

Because $R<p$, splitting its prime divisors at $L$ gives

$$
\sum_{\substack{\ell\mid R\\\ell>L}}\frac1{\ell-1}
 \le \frac{2}{\log L}
$$

for sufficiently large $L$. Indeed their number is at most
$\log R/\log L<L/\log L$. For the small primes, partial summation
of (726.9) shows

$$
\sum_{\ell\le L}\frac1\ell\le8\log\log L+C.
$$

The total of $1/(\ell-1)-1/\ell$ is bounded by the convergent
sum over all integers $\ell\ge2$. Therefore

$$
\boxed{
 \sum_{o\mid R}\frac1{\varphi(o)}
 =\prod_{\ell\mid R}\left(1+\frac1{\ell-1}\right)
 =\frac R{\varphi(R)}
 \le C(\log L)^8 .
}
\tag{726.10}
$$

Only this weak elementary bound is required.

### 3.2 A Rankin bound for the large orders

Assume $L\ge e^4$ and put $\delta=1/\log L\le1/4$. For any $X>1$,

$$
\sum_{\substack{o\mid R\\o>X}}\frac1{\sqrt{\varphi(o)}}
 \le X^{-\delta}
 \prod_{\ell\mid R}\left(1+\frac{\ell^\delta}{\sqrt{\ell-1}}\right).
\tag{726.11}
$$

To bound this product uniformly, put $a=1/2-\delta$ and $b=1-a$.
Thus $1/4\le a<1/2$ and $1/2<b\le3/4$. Since
$\ell^\delta/\sqrt{\ell-1}\le2\ell^{-a}$, (726.9) gives

$$
\sum_{\ell\le L}\ell^{-a}
 \le\frac{8L^b}{\log L}
     +8a\int_2^L\frac{u^{-a}}{\log u}\,du
 \le\frac{48L^b}{\log L}.
\tag{726.12}
$$

For the second inequality, split the integral at $\sqrt L$.
Its lower part is at most $3L^{b/2}$ and its upper part at most
$4L^b/\log L$. The elementary maximum
$\sup_{x>1}\log x/x^{1/4}=4/e<2$ bounds the lower part by
$6L^b/\log L$. This proves the asserted uniform constant.

The number of divisors $\ell\mid R$ above $L$ is less than
$L/\log L$, and $\ell^{-a}\le L^{-a}$. Taking logarithms of the
product in (726.11), using $\log(1+u)\le u$, consequently gives

$$
\begin{aligned}
\log\prod_{\ell\mid R}
 \left(1+\frac{\ell^\delta}{\sqrt{\ell-1}}\right)
 &\le \frac{98L^{1/2+\delta}}{\log L}\\
 &< \frac{300\sqrt L}{\log L},
\end{aligned}
\tag{726.13}
$$

because $L^\delta=e<3$.

We will use the fixed choices

$$
X=\exp(302\sqrt L),\qquad Y=\exp(303\sqrt L),\qquad
Y_0=L^{1/4}.
\tag{726.14}
$$

Equations (726.11)–(726.13) then imply

$$
\boxed{
\sum_{\substack{o\mid R\\o>X}}\frac1{\sqrt{\varphi(o)}}
 \le \exp\left(-\frac{2\sqrt L}{\log L}\right).
}
\tag{726.15}
$$

Finally, if $r=\omega(R)$, then $R\ge(r+1)!$.
For $r\ge4$, $\log R\ge(r/2)\log(r/2)$.
It follows effectively that $r=O(L/\log L)$, whence

$$
J/\sqrt p\le
 \exp\bigl(O(L/\log L)-L/2\bigr)\longrightarrow0.
\tag{726.16}
$$

All constants here are absolute, even when $R$ has many small
prime factors.

## 4. A count for a fixed small-order subgroup at small height

The next lemma is proved directly in $K$. A result for subgroups of
$\mathbf F_p^\times$ is not silently applied to the nonsplit torus.

**Lemma 726.3.** Fix $A\ge1$. Suppose
$L\ge64A^2$, $H\ge2$, $\log H\le A\sqrt L$, and $o\mid M$ with
$o\le H^4$. Then

$$
\boxed{N_o(H)\le C_A H^{1/2},}
\tag{726.17}
$$

where $C_A$ is an effective constant depending only on $A$.

**Proof.** Let $\mathcal U$ be the elements counted by $N_o(H)$,
and for $\beta\in\mathcal U$ put $\alpha_\beta=\bar\beta/\beta$.
Let $d$ be the rank of the subgroup generated by these elements in
$K^\times/\mu_6$. Choose actual representatives
$\alpha_1,\ldots,\alpha_d$ from this set whose classes are
multiplicatively independent. The quotient by $\mu_6$ is used
only to define independence; no reduction map on that quotient
is assumed.

Put $h=\log H$ and

$$
k=\left\lfloor\frac{L-\log4}{2h}\right\rfloor.
$$

The hypotheses give $k\ge L/(8h)\ge1$. To see this, use
$L-\log4\ge L/2$ and
$L/(4h)\ge\sqrt L/(4A)\ge2$, before taking the floor.
Two monomials of total degree at most $k$ in the $\alpha_i$
can be written as $\bar B/B$ and $\bar C/C$, where
$B,C\in\mathcal O_K$, their norms are prime to $p$, and
$|B|,|C|\le H^k$.

If the reductions of the two monomials are equal, then

$$
\bar B C-B\bar C\in p\mathcal O_K,\qquad
|\bar B C-B\bar C|\le2H^{2k}\le p/2<p.
$$

A nonzero element of $p\mathcal O_K$ has absolute value at least $p$.
Hence the difference is exactly zero. Independence of the classes
of the $\alpha_i$ implies that the exponent vectors are equal.
Reduction is therefore injective on this set of monomials.

For every actual representative,
$\alpha_i^{3o}=1\bmod p$. Since $3o\mid p+1$, all monomial
reductions lie in the subgroup of order $3o$ of the norm-one torus.
Thus

$$
\binom{k+d}{d}\le3o\le3H^4.
\tag{726.18}
$$

This uses one fixed order $o$. It does not combine several
different small orders before invoking the subgroup bound.

As $\binom{k+d}{k}\ge(1+d/k)^k$, put $x=k/h$ to obtain

$$
x\log\left(1+\frac{d}{xh}\right)
 \le4+\frac{\log3}{h}<6,\qquad
x\ge c_A:=\frac1{8A^2}.
$$

The function $x(e^{6/x}-1)$ decreases for $x>0$. Consequently

$$
d\le D_A h,\qquad
D_A=c_A(e^{6/c_A}-1).
\tag{726.19}
$$

We now convert rank into a count without a hidden height-to-rank
assumption. The Eisenstein ring is a PID. A visible element with
norm prime to $6$ is divisible by no inert rational prime, and its
ideal is divisible by at most one of the two primes above each
split rational prime. Indeed an inert prime, or both primes above
a split prime, would divide both integral coordinates $a,b$.
The ramified prime over $3$ is excluded.

Choose one orientation at each split rational prime $\ell$.
If $v_\ell(\beta)$ is the exponent at that prime minus the exponent
at its conjugate, then

$$
N\beta=\prod_{\ell\ {\rm split}}\ell^{|v_\ell(\beta)|}.
\tag{726.20}
$$

The valuation vector of $\alpha_\beta$ is the corresponding signed
vector, with its two opposite coordinates. The rational vector
space spanned by these vectors has dimension $d$. Choose $d$
coordinate positions on which projection is injective. Denote
their distinct rational primes in increasing order by
$\ell_1,\ldots,\ell_d$, so $\ell_j\ge j+1$.

For elements of $\mathcal U$, equality of these $d$ coordinates
forces equality of all ideal valuations. The elements then differ
by a unit. The primary condition makes that unit equal to one:
the six elements of $\mu_6$ have distinct reductions modulo $3$.
Thus this projection is injective on $\mathcal U$ itself.

For any fixed $0<\sigma<1$, equation (726.20) bounds the number of
possible projected integer vectors by

$$
\begin{aligned}
N_o(H)
&\le H^{2\sigma}
 \prod_{j=1}^d\left(\sum_{v\in\mathbf Z}\ell_j^{-\sigma|v|}\right)\\
&=H^{2\sigma}
 \prod_{j=1}^d\left(1+\frac2{\ell_j^\sigma-1}\right)\\
&\le H^{2\sigma}\exp\bigl(C_\sigma d^{1-\sigma}\bigr),
\qquad
C_\sigma=\frac{2}{(1-\sigma)(1-2^{-\sigma})}.
\end{aligned}
\tag{726.21}
$$

For completeness, $\ell_j^\sigma-1\ge
(1-2^{-\sigma})\ell_j^\sigma$ and
$\sum_{j=1}^d(j+1)^{-\sigma}\le d^{1-\sigma}/(1-\sigma)$
prove the last inequality. If $d=0$, the empty product gives the
same bound.

Take $\sigma=1/8$ and use (726.19). With
$E_A=C_{1/8}D_A^{7/8}$, this gives

$$
N_o(H)\le H^{1/4}\exp(E_Ah^{7/8}).
$$

The function $E_Ah^{7/8}-h/4$ has a finite effective maximum on
$h\ge0$, namely
$(E_A/8)(7E_A/2)^7$.
Absorb its exponential into $C_A$ to obtain (726.17). This proves
the lemma. The displayed constants are deliberately very large;
their size has no bearing on uniform convergence. $\square$

## 5. The very small radii

The elementary inequality

$$
\varphi(n)\ge\sqrt{n/2}\qquad(n\ge1)
\tag{726.22}
$$

follows prime by prime from
$\varphi(\ell^a)^2/\ell^a=\ell^{a-2}(\ell-1)^2$:
every factor is at least one except the possible factor $1/2$
at $\ell=2,a=1$.

R614 Lemma 614.1, retained in R714 §3, gives
$|\beta|^{o(\beta)}\ge p/2$ whenever $o(\beta)>2$.
For $|\beta|\le Y_0=L^{1/4}$ it follows that

$$
o(\beta)\ge\frac{L-\log2}{\log Y_0},\qquad
\frac1{\varphi(o(\beta))}
 \le C\sqrt{\frac{\log L}{L}}.
$$

The global reciprocal-height count
$\sum_{0<|\beta|\le T}|\beta|^{-1}\le18T$
from R714 (714.13) therefore gives

$$
\sum_{\substack{\beta\in\mathcal V,\ o(\beta)\in\mathcal D\\
                  |\beta|\le Y_0}}
 \frac{f(|\beta|)}{\varphi(o(\beta))}
 \le C L^{-1/4}\sqrt{\log L}\longrightarrow0.
\tag{726.23}
$$

Here all orders are counted together. There is no factor $J$ in
this bound.

## 6. Intermediate radii, with all orders retained

Cover $(Y_0,Y]$ by the dyadic shells $(H/2,H]$ with
$H=2Y_0,4Y_0,\ldots$ until the last upper endpoint is at most
$2Y$. We may enlarge the last shell. For sufficiently large $L$,

$$
\log H\le304\sqrt L.
$$

Apply Lemma 726.3 with the single fixed absolute value $A=304$.
Its threshold $L\ge64\cdot304^2$ causes only a fixed initial
exceptional range.

In one shell first consider points with $o(\beta)>H^4$.
Equation (726.22) gives
$1/\varphi(o(\beta))\le\sqrt2/H^2$.
There are at most $9H^2$ points in total and $1/|\beta|<2/H$.
Their contribution to (726.2) is therefore at most $C/H$.

For the remaining orders $o\le H^4$, Lemma 726.3 and (726.10)
give

$$
\begin{aligned}
\sum_{\substack{\beta\in\mathcal V,\ o(\beta)\in\mathcal D\\
                H/2<|\beta|\le H,\ o(\beta)\le H^4}}
 \frac{f(|\beta|)}{\varphi(o(\beta))}
&\le \frac2H
   \sum_{\substack{o\mid R\\o\le H^4}}\frac{N_o(H)}{\varphi(o)}\\
&\le C_{304}H^{-1/2}(\log L)^8.
\end{aligned}
\tag{726.24}
$$

Both dyadic series are geometric. Summing over all the intermediate
shells gives

$$
\boxed{
\text{intermediate-radius contribution}
 \le C Y_0^{-1}
      +C_{304}Y_0^{-1/2}(\log L)^8
 =O(L^{-1/4})+O_{304}(L^{-1/8}(\log L)^8)
 \longrightarrow0.
}
\tag{726.25}
$$

The number of shells, which grows with $p$, is not multiplied into
the estimate; it is absorbed by the convergent geometric sums.
No restriction on $J$ occurs.

## 7. Large orders and the full remaining infinite tail

It is enough to combine the preceding bounds with the following
two contributions. Overlap between upper bounds only enlarges their
sum; one may alternatively assign each point to the first applicable
part of this partition.

For all orders $o>X$, irrespective of radius, (726.8), (726.15),
and (726.16) give

$$
\text{large-order contribution}
 \le30\exp\left(-\frac{2\sqrt L}{\log L}\right)
       +C J e^{-L/2}\longrightarrow0.
\tag{726.26}
$$

For the remaining orders $o\le X$ and radii $|\beta|>Y$,
there are at most $X$ orders. The complete tail (726.7) gives

$$
\text{small-order, large-radius contribution}
 \le12X/Y+CX/\sqrt p
 =12e^{-\sqrt L}+C e^{302\sqrt L-L/2}
 \longrightarrow0.
\tag{726.27}
$$

Every point in (726.2) is included: orders above $X$ use (726.26);
orders at most $X$ have radii in one of the ranges of §§5–6 or
in (726.27). The estimates in §§5–6 even bound all orders in
their respective radius ranges.

Collecting the bounds proves the effective inequality, for all
sufficiently large $L$,

$$
\begin{aligned}
\mathcal B_p\le {}&
 C L^{-1/4}\sqrt{\log L}
 +C L^{-1/4}
 +C_{304}L^{-1/8}(\log L)^8\\
&+30e^{-2\sqrt L/\log L}
 +C J e^{-L/2}
 +12e^{-\sqrt L}
 +C e^{302\sqrt L-L/2}.
\end{aligned}
\tag{726.28}
$$

Every term tends to zero, including the $J$ term by (726.16).
All estimates are elementary and effective. This proves Theorem
726.1 for every prime in the specified residue classes, with no
small-radical or bounded-divisor assumption.

## 8. Both signed-ray kernels and the original quotient

The original characters, with the notation of R714 §2, are

$$
\lambda_{p,\pm}((a))
 =a\,\kappa_4((a))^{\pm1}\kappa_p((a))^m,\qquad
m=\begin{cases}1,&p\equiv5\pmod9,\\2,&p\equiv2\pmod9.\end{cases}
\tag{726.29}
$$

The $p$-dependent cubic factor is retained. It has absolute value
one and is trivial on rational scalars, so the complete signed
sums over integer multiples of each visible ray remain exactly

$$
G_{2p}(u)=
 \sum_{\substack{n\ge1\\(n,2p)=1}}\frac{\chi_{-3}(n)}n E_1(un^2),
\qquad
F_{2p}(u)=
 \sum_{\substack{n\ge1\\(n,2p)=1}}\frac{\chi_{-3}(n)}n e^{-un^2}.
$$

R614 and R714 give $|G_{2p}(u)|\le S E_1(u)$ and
$|F_{2p}(u)|\le S e^{-u}$. Thus (714.7)–(714.9) imply

$$
|A_-^{\rm prim}-A_-^{\rm full}|\le2S\mathcal B_p.
\tag{726.30}
$$

For the derivative kernel we need a pointwise Gaussian bound,
not merely the constant bound $E_1(t|\beta|^2)\le E_1(t)$.
For $x>0$,

$$
e^xE_1(x)=\int_0^\infty\frac{e^{-u}}{x+u}\,du
 \le \log(1+1/x)+e^{-1}.
$$

The first integral over $[0,1]$ is bounded by
$\log(1+1/x)$, and over $[1,\infty)$ one can use
$1/(x+u)\le1$. Since $|\beta|\ge1$, $x=c|\beta|^2/p\ge c/p$.
For $p\ge41$, $c>3/5$ gives $1+p/c<2p$, and hence

$$
\boxed{
E_1(c|\beta|^2/p)
 \le(\log p+2)e^{-c|\beta|^2/p}.
}
\tag{726.31}
$$

The same complete signed-ray identity now gives

$$
|A_+^{\rm prim}-A_+^{\rm full}|
 \le2S(\log p+2)\mathcal B_p=o(\log p).
\tag{726.32}
$$

The original full-family lower bounds from R616 and R714 are

$$
A_-^{\rm full}>\frac{5393}{6150},\qquad
A_+^{\rm full}>\frac95(\log p-1)-\frac1{250}.
\tag{726.33}
$$

In view of (726.3), both primitive averages are strictly positive
for all sufficiently large $p$. For example it is enough to take
a sufficiently large effective threshold above which
$2S\mathcal B_p<1/4$; (726.30)–(726.33) then directly give positive
lower bounds for both averages.

The passage from these two averages to the specified factor is
the original primitive-orbit, Gross–Zagier, and rank argument of
R616 §§5–6, as also recorded in R714 §5. All primitive characters
in each fixed cubic direction belong to the one rational Galois
orbit of that factor. The original rank/Heegner interface transfers
nonvanishing between its embeddings, so the two positive averages
meet at $\theta_{-1}$ in (726.4). We have not asserted a direct
Galois action on transcendental derivative values. We have not
declared the opposite cubic family to be a quotient of $J_{X_1}$.
This proves Theorem 726.2.

## 9. Consequences and remaining work

The asymptotic R616 nonvanishing premise is now discharged for
all remaining prime classes $p\equiv2,5\pmod9$, without any
factorization restriction on $(p+1)/3$. At these sufficiently
large primes, the original CM point difference supplies the
fixed rank and logarithm basis required by R634/R682/R703/R724.
The finitely many primes below the effective threshold are not
classified here; the existing sharper R714 and R719 certificates
remain useful there.

The conclusion is positive rank, not vanishing of rational point
images. It supplies neither a $p$-unit assertion for that
logarithm nor the actual height matrices, canonical Taylor jets,
or a certificate excluding their common zeros. It does not bound
the remaining candidate discriminants or transport a result
between the different $X_1/c_1$ and $X_d/c_0$ quotients.
The final Serre-uniformity objective therefore remains open.

There is no new numerical computation in this proof. The very
large constants are explicit choices for an existence theorem;
no prime search or completed $L$-value computation is rerun.

## Sources and dependencies

- [R614](R614-actual-primitive-visible-ray-radical-bound.md):
  the complete signed-multiple kernels, short-direction order
  bound, and the uniform visible-point estimate on each line.
- [R714](R714-global-visible-count-and-sublogarithmic-divisor-primitive-region.md):
  the original-family ray identities, packing estimates, and
  full-average lower bounds.
- [R616](R616-original-CM-point-difference-and-explicit-height-basis.md):
  the original characters and positive quotient, primitive Galois
  orbit, same CM point difference, Gross–Zagier and rank interfaces.
- J. Bourgain, S. V. Konyagin, I. E. Shparlinski,
  *Distribution of Elements of Cosets of Small Subgroups and
  Applications*, International Mathematics Research Notices
  2012 (9), 1968–2009; [author preprint](https://arxiv.org/pdf/1103.0567).
  The small-height multiplicative-rank method motivates §4.
  Its rational-height results for $\mathbf F_p^\times$ are not
  used as a black-box theorem for the nonsplit torus: the needed
  number-field counting lemma, reduction injectivity, and valuation
  enumeration are proved in full above.
