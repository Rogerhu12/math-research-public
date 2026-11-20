# R960: the original r=2 Igusa formal height and an explicit Jacobi coefficient

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved geometric and coefficient criteria.** The original complete $r=2$ Cartier matrices are the matrices of an explicit Kummer curve. Its inverse Igusa-character factor has a one-dimensional formal group. The actual odd Cartier-chain length $L$ of R955 is exactly one less than that formal group's height. A specific coefficient of a finite power of the original Jacobi polynomial detects height two. The coefficient is proved integral after the displayed division by $p$, and independent modulo $p$ of the permitted polynomial lift used to calculate it. Its nonvanishing is not proved here.

This is an actual Igusa factor, rather than an identification of the different original height-two CM target with an Igusa quotient. No source scalar from R932 is discarded. No new mathematical computation is executed.

## 1. The actual coarse Igusa Kummer curve

Keep the original $r=2$ conditions and notation of R939/R958:
$$
p\ge41,\quad p\equiv11\pmod{12},\quad
p=6N+5,\quad D(u)=1-4u^3,\quad
\mathcal A(u)=uD(u)^{N+1}H(u^3).
\tag{960.1}
$$
Here $N$ is odd, $H\in\mathbf F_p[t]$ has degree $N$, is squarefree, and $H(0)H(1/4)\ne0$. The original application also retains $p\equiv2,5\pmod9$. Set
$$
d=(p-1)/2=3N+2,\qquad m=2N+1=(p-2)/3.
\tag{960.2}
$$
The symbol $d$ in this result is a Kummer degree; it is neither the original $p+1$ character modulus nor R932's fine-cover degree $d_1$.

On the original generic $H_6$ curve use the corrected R939 frame
$$
E_u:y_E^2=x_E^3+3uD x_E+D(1/2-4u^3),\qquad
\rho=dx_E/(2y_E),\qquad \operatorname{KS}(\rho^2)=du/D.
\tag{960.3}
$$
Write the canonical Igusa Hasse root as $\mathfrak a=\alpha\rho$. It satisfies $\alpha^{p-1}=\mathcal A(u)$. The central sign sends $\alpha$ to $-\alpha$; hence the scalar $y=\alpha^2$ is the coordinate after the actual $\{\pm1\}$ quotient in R918. Its function field is
$$
\boxed{\quad
\mathscr I_p:\qquad y^d=uD(u)^{N+1}H(u^3).
\quad}
\tag{960.4}
$$
By $\mathscr I_p$ we mean the smooth projective normalization. The simple zero at $u=0$ proves that this Kummer extension has degree $d$ and is geometrically connected. Thus (960.4) is the generic function field of the same tame $H_6$ Igusa quotient; it does not add another Igusa component. The normalization extends that generic identification over the complete smooth curves.

Here is the full branch accounting. There are $3N$ simple roots of $H(u^3)$, the simple root $u=0$, and three roots of $D$. The last three have exponent $N+1$. All are distinct, and
$$
\gcd(d,N+1)=1.
$$
Every one of these $3N+4$ finite points is therefore totally ramified of degree $d$. The degree of the right side of (960.4) is $6N+4=2d$, so infinity is unramified, with $d$ geometric points above it. Riemann--Hurwitz gives
$$
g(\mathscr I_p)=\frac{(d-1)(3N+2)}2=\frac{d(d-1)}2.
\tag{960.5}
$$
The three elliptic $D=0$ points have not been deleted. Their tame normalization orders are used in the differential calculation below.

The Kummer action is $\epsilon:(u,y)\mapsto(u,\epsilon y)$ for $\epsilon\in\mu_d\subset\mathbf F_p^\times$. In the once-transported original marking of R958 the actual cubic deck action is
$$
\delta:(u,y)\longmapsto(\zeta^2u,\zeta y).
\tag{960.6}
$$
Indeed $d\equiv2\pmod3$, so both sides of (960.4) are multiplied by $\zeta^2$. This is compatible with the original $u=E_4/(4sV_4^\dagger)$ and $\delta V_4^\dagger=\zeta V_4^\dagger$. It does not combine that transported coordinate with the opposite pre-transport direction of $u$.

## 2. Both entire inverse character spaces, including their dimensions

Let $\Omega_+$ be the $\mu_d$ character $\epsilon$ part of $H^0(\mathscr I_p,\Omega^1)$, and $\Omega_-$ the character $\epsilon^{-1}$ part. These are distinct because $d>2$. Direct normalization gives
$$
\boxed{\quad
\Omega_+=\left\{\omega_q=
\frac{D^Nq(u)}{6y^{d-1}}\,du:\ \deg q\le3N\right\},
\qquad
\Omega_-=k\,\frac{du}{y}.
\quad}
\tag{960.7}
$$
These are complete character spaces, over any perfect field containing the original constants; they are not selected Hecke eigenlines.

For completeness, an eigen-differential of character $\epsilon$ has the form $f(u)du/y^{d-1}$. At a totally ramified point of exponent $e$, its order is
$$
d\,\operatorname{ord}(f)+(d-1)-(d-1)e.
$$
At the $e=1$ points this requires $f$ to have no pole. At each $D=0$ point, $e=N+1$, it requires precisely $\operatorname{ord}(f)\ge N$. Thus $f=D^Nq$ with $q$ a polynomial. At infinity $y$ has pole order two and $du$ pole order two; regularity requires $\deg q\le3N$. Conversely these conditions make the differential regular everywhere. For the inverse character use $f(u)du/y$: all finite points require $f$ to have no pole, and infinity requires $\deg f\le0$. This proves (960.7).

The original Igusa maps are exactly these forms. For a high form $H_q$ with scalar evaluation $D^{N+1}q(u)$,
$$
\Phi_{p-1}(H_q)=\frac16\operatorname{KS}
\left(H_q/\mathfrak a^{p-3}\right)=\omega_q.
\tag{960.8}
$$
For the original low form $v=V_4^\dagger$, whose evaluation is $12sD$,
$$
\boxed{\Phi_4(v)=2s\,du/y.}
\tag{960.9}
$$
In particular the low differential is the named original one, with its factor $2s$ retained. The full norm extension and original determinant transport are those already proved in R918; no alternative extension is introduced.

The $\delta$ eigenspaces are as follows:

| Space | $\delta=\zeta$ | $\delta=\zeta^2$ | $\delta=1$ |
|---|---:|---:|---:|
| $\Omega_+$ | $q=P(u^3)$, dimension $N+1$ | $q=u^2K(u^3)$, dimension $N$ | $q=uK(u^3)$, dimension $N$ |
| $\Omega_-$ | $k\,du/y$, dimension $1$ | $0$ | $0$ |

The character calculation uses (960.6) on both $du$ and $y^{d-1}$; for $q=1$ the quotient has character $\zeta$. This is the same pair of high character spaces as R958, together with its previously excluded invariant summand.

## 3. The complete Hasse--Witt realization

The polynomial formulas of R958 are therefore actual Cartier matrices on $\Omega_+$. They can also be recovered directly from (960.4). Put
$$
Z(u)=uH(u^3).
$$
Since $p=2d+1$, the rule $\operatorname{Car}(f^p\eta)=f\operatorname{Car}(\eta)$ gives, after removing the factors $D^{pN}$ and $Z^p$,
$$
\boxed{\quad
\operatorname{Car}(\omega_q)=\omega_{q'},\qquad
q'\,du=Z(u)\operatorname{Car}_{\mathbf P^1}
\left(\frac{D(u)^{4N+2}q(u)}{Z(u)^3}\,du\right).
\quad}
\tag{960.10}
$$
To check every exponent, start with
$$
\frac{D^Nq}{y^{d-1}}\,du
=\left(\frac1{y^{d-1}}\right)^p
D^Nq\,\mathcal A^{p-3}\,du.
$$
The exponent of $D$ is
$N+(N+1)(p-3)=pN+4N+2$, and
$u^{p-3}H^{p-3}=Z^p/Z^3$.
The coefficient $1/6$ is fixed by inverse Frobenius. This proves (960.10), including its normalization and coefficient roots.

The rational input in (960.10) has poles of order at most three at the simple roots of $Z$. Its polynomial part at infinity has degree at most $p-2$, because
$$
3(4N+2)+3N-3(3N+1)=6N+3=p-2.
$$
Cartier kills that polynomial part. At a finite pole of order less than $p$, only the residue term survives. Thus a second exact form of (960.10) is
$$
q'=Z(u)\sum_{Z(\xi)=0}
\frac{\left(\operatorname{res}_{u=\xi}
D^{4N+2}q\,du/Z^3\right)^{1/p}}{u-\xi}.
\tag{960.11}
$$
The formula is over a splitting field and descends. Each $d\log(u-\xi)$ is Cartier-fixed; the root in (960.11) acts on the residue, not on the variable in its denominator. This is a geometric Hasse--Witt realization of the interpolation matrices, rather than an assumption that their roots lie in $\mathbf F_{p^2}$.

The invariant $\delta=1$ block is bijective. Here is a direct check, so that no extra nilpotent part is hidden outside R958's two blocks. For $H_K(E_u,\rho)=uD^{N+1}K(t)$, $t=u^3$, $\deg K<N$, the same Serre rule as R958 gives
$$
\mathscr D_2H_K=u^2D^{N+2}\mathcal L_H K,
\quad
\mathcal L_H=9tD\frac{d^2}{dt^2}
+12(1-8t)\frac d{dt}-25.
\tag{960.12}
$$
Indeed the first derivative has bracket
$(1-8t)K+3tDK'$, and the second derivative plus $E_4/144$ has bracket three times its derivative minus $K$. On monomials the diagonal of $\mathcal L_H$ is $-(6j+5)^2$. These are all units for $0\le j<N$. In R958's algebra $k[t]/H$, the actual output is
$$
K_{\rm out}=\operatorname{Fr}_p^{-1}
\left((t^{2N+1}a)^{-1}\mathcal L_HK\bmod H\right),
\quad a=2D^{2N+1}\beta^2.
\tag{960.13}
$$
Every multiplier is a unit. The points $u=0$ and $D=0$ satisfy the forced zero conditions, exactly as in R958. Hence this block is bijective.

It follows that the entire $\Omega_+$ has the one-dimensional Cartier kernel $k\Phi_{p-1}(F)$ of R958, and its whole nilpotent part is the same single odd chain $\mathcal N$ of R955. It has dimension
$$
L=2b+1\qquad(0\le b\le N).
\tag{960.14}
$$
There is no extra nilpotent block from another $\delta$ or from another $\mu_d$ character in this assertion.

## 4. The actual one-dimensional formal factor and its height

Let $J_p=\operatorname{Jac}(\mathscr I_p)$. Since $d$ is prime to $p$ and $\mu_d\subset\mathbf F_p$, the character idempotents of $\mathbf Z_p[\mu_d]$ split $J_p[p^\infty]$. Use the idempotent whose cotangent space is $\Omega_-$, and call that factor $G_-$. This specifies the convention without exchanging a character with its contravariant dual. It has dimension one by (960.7).

The canonical principal polarization is invariant under the curve automorphisms. Consequently its Rosati involution sends $\epsilon$ to $\epsilon^{-1}$, and identifies $G_-^\vee$ with the factor $G_+$ whose cotangent space is $\Omega_+$. In particular
$$
\operatorname{ht}(G_-)=\operatorname{ht}(G_+)
=\dim G_-+\dim G_+=1+(3N+1)=d.
\tag{960.15}
$$
This height uses one character factor and its dual; the two are not counted twice.

Let $\mathcal F_p$ be the connected formal group of $G_-$, and let its height be $h_p$. The connected--étale sequence shows that the étale quotient of $G_-$ has height $d-h_p$. Its Cartier dual is the maximal multiplicative part of $G_+$ and contributes precisely $d-h_p$ dimensions to the Cartier-bijective part of $\Omega_+$. Therefore the dimension of its nilpotent part is
$$
(d-1)-(d-h_p)=h_p-1.
$$
Comparing with (960.14) proves
$$
\boxed{\quad h_p=L+1=2b+2.\quad}
\tag{960.16}
$$

The Cartier statement used here can be checked on the contravariant Dieudonné module: the cotangent module is $M/FM$, Cartier is induced by $V$, and the $V$-invertible part is precisely the multiplicative part, dual to the étale part of the opposite group. Thus the argument uses the actual connected--étale and duality operations, not the mere presence of one low eigenline. The nilpotent dimension is $h_p-1$ whether or not the full character factor has an étale part.

There is an independent check of the parity and the range. The $\delta$-invariant part of $G_-$ has zero cotangent dimension and height $N$, so it is étale. On the remaining factor, the two conjugate $\delta$ pieces of de Rham cohomology each have dimension $N+1$: the Hodge dimensions in the table and the inverse-character Serre dual dimensions give this explicitly. Frobenius interchanges them. The action of $\delta$ on the one-dimensional cotangent line is $\zeta$, giving an action of the unramified quadratic ring $\mathbf Z_p[\zeta]$. Its connected height is even and at most $2N+2$. Also Cartier on $du/y$ is zero, since it must have the absent inverse-Frobenius character $\zeta^2$ in $\Omega_-$. Thus $h_p\ge2$, in agreement with (960.16).

In particular R955 and R958 now give the exact equivalences
$$
\boxed{\quad
S\ne0\ \Longleftrightarrow\ L=1
\ \Longleftrightarrow\ h_p=2
\ \Longleftrightarrow\ \ell_N(R_F)\ne0.
\quad}
\tag{960.17}
$$
Here $S$, $F$, and $R_F$ are the unchanged original quantities. This is not an assertion that $G_-$ is the original positive-CM target. In particular (960.15) does not replace its actual height by two.

## 5. A smooth lift and an integral formal logarithm

Choose a polynomial $\widetilde H\in\mathbf Z_p[t]$ of degree $N$ lifting $H$, and keep the factorization
$$
\widetilde y^{\,d}
=u(1-4u^3)^{N+1}\widetilde H(u^3).
\tag{960.18}
$$
The reduction of $\widetilde H$ is squarefree and is disjoint from $0$ and $1/4$. After an unramified extension its roots lift to disjoint sections. Normalizing this tame cyclic cover therefore gives a smooth proper lift of (960.4). The exponent $N+1$ at each of the three $D$ roots is retained: replacing this geometrically by an arbitrary perturbation of the whole degree-$m$ polynomial would not give the same smooth lift.

The $\mu_d$ action and $\delta$ lift. The character idempotent on the formal Jacobian gives a one-dimensional smooth formal group over the coefficient DVR. Its reduction is $\mathcal F_p$. The idempotent has unit denominator $d$; the $\mathbf Z_p$ scalars act on the formal $p$-divisible group, so this is an integral direct factor, not only a characteristic-zero linear projection.

Put
$$
\widetilde H^{\rm rev}(x)=x^N\widetilde H(1/x),
\qquad
a(x)=(1-x/4)^{N+1}
\frac{\widetilde H^{\rm rev}(x)}{\widetilde H_N}.
\tag{960.19}
$$
Then $a(0)=1$ and $\deg a=m$. At one of the unramified points above infinity take $z=1/u$. Choose the unit $w_0$ with
$$
w_0^d=(-4)^{N+1}\widetilde H_N.
$$
It exists after a finite unramified extension. The local equation becomes
$$
\widetilde y=z^{-2}w_0a(z^3)^{1/d},
\qquad
-w_0\frac{du}{\widetilde y}=a(z^3)^{-1/d}\,dz.
\tag{960.20}
$$
The projected Abel map at that point has an invertible tangent map to the one-dimensional formal factor, because $du/\widetilde y$ is nonzero there. It therefore identifies this formal disc with the formal group, integrally. In the resulting coordinate $z$, the normalized invariant differential and logarithm are
$$
\boxed{\quad
\omega_{\mathcal F}=a(z^3)^{-1/d}\,dz,
\qquad
\log_{\mathcal F}(z)=\int_0^z a(T^3)^{-1/d}\,dT.
\quad}
\tag{960.21}
$$
The scaling $-w_0$ only normalizes the logarithm to have derivative one. Equation (960.9), rather than a reassignment of the original modular vector, fixes its relation to the original Igusa differential.

The point above infinity is fixed by $\delta$, and $\delta z=\zeta z$. Thus the displayed coordinate realizes that automorphism exactly. The first nonzero term of multiplication by $p$ in characteristic $p$ has degree $p^{h_p}$; commutation with $z\mapsto\zeta z$ forces $h_p$ even. This also directly proves that every coefficient of $[p]_{\mathcal F}(z)$ in degrees below $p^2$ is divisible by $p$.

## 6. The first possible height coefficient

Write
$$
j=\frac{p^2-1}{3}=pm+(2m+1),
\qquad b(x)=a(x)^{-1/d}\in\mathbf Z_p[[x]].
\tag{960.22}
$$
The exponent $-1/d\in\mathbf Z_p$ and $a(0)=1$ make all coefficients of $b$ integral. Let $b_j=[x^j]b$. The coefficient of $z^{p^2}$ in the logarithm (960.21) is $b_j/p^2$.

If $[p]_{\mathcal F}(z)=P(z)$, compare coefficients in
$\log_{\mathcal F}(P(z))=p\log_{\mathcal F}(z)$. Every coefficient of $P$ below degree $p^2$ is divisible by $p$. For a logarithm term of degree $q\ge2$, its coefficient has valuation at least $-v_p(q)$; its contribution at degree $p^2$ in $P(z)^q$ has valuation at least $q-v_p(q)>0$. Thus modulo $p$ only the linear logarithm term contributes on the left. It follows both that $b_j\in p\mathbf Z_p$ and that
$$
\boxed{\quad
\kappa_p:=\frac{b_j}{p}\bmod p
=[z^{p^2}]\,[p]_{\mathcal F}(z)\bmod p.
\quad}
\tag{960.23}
$$
Consequently
$$
\boxed{\quad
\kappa_p\ne0\ \Longleftrightarrow\ h_p=2
\ \Longleftrightarrow\ S\ne0.
\quad}
\tag{960.24}
$$
If $\kappa_p=0$, then $h_p\ge4$ and the original chain has length at least three. These are actual geometric alternatives, not an abstract nonreduced-algebra example.

## 7. A finite polynomial coefficient and lift independence

Set
$$
A(x)=a(x)^2,\qquad \deg A=2m<p.
$$
The height coefficient admits the finite expression
$$
\boxed{\quad
\kappa_p=
\frac1p[x^j]A(x)^{p+1}\pmod p.
\quad}
\tag{960.25}
$$
The indicated integer or $p$-adic coefficient is divisible by $p$. There is no additional factor $A(x^p)$ in (960.25).

Here is a proof that also separates its arithmetic from the geometric lift. Since $p-1=2d$, the identity $b^{p-1}=a^{-2}$ gives
$$
b=A b^p.
$$
For an integral series $f$ define the integral Frobenius quotient
$$
Q_p(f)=\frac{f(x)^p-f(x^p)}p.
$$
Then
$$
b=A b(x^p)+pA Q_p(b).
\tag{960.26}
$$
Because $j\bmod p=2m+1>\deg A$, the coefficient of $x^j$ in $A b(x^p)$ is zero. Reduction modulo $p$ and iteration also give
$$
b\equiv B:=A(x)A(x^p)\pmod{(p,x^{p^2})}.
$$
Writing $b=B+pc$ to this precision shows
$Q_p(b)\equiv Q_p(B)-c(x^p)\pmod p$. The same degree gap kills the coefficient of $A c(x^p)$ at $j$. The product identity is
$$
Q_p(B)=A(x)^pQ_p(A)(x^p)
+A(x^{p^2})Q_p(A)(x).
$$
Its first term, after multiplication by $A$, again has zero target coefficient modulo $p$. Since $j<p^2$, the second term can replace $A(x^{p^2})$ by one. Therefore
$$
\frac{b_j}{p}\equiv[x^j]A Q_p(A)
=\frac1p[x^j]\bigl(A^{p+1}-A A(x^p)\bigr)
=\frac1p[x^j]A^{p+1}\pmod p.
$$
This proves (960.25). Its divisibility also follows immediately from
$A^{p+1}\equiv A(x)A(x^p)\pmod p$ and the same degree gap.

For pure coefficient calculation, one may now replace $a$ by **any** degree-at-most-$m$ integral lift $a'$ of the same residual polynomial with constant term one. This does not assert that the arbitrary polynomial defines a smooth lift of (960.4). If $a'=a+pc$, then
$$
(a')^{-1/d}-a^{-1/d}
\equiv 2p\,b\,c/a\pmod{p^2}.
$$
To degree $j<p^2$ the right side divided by $p$ is congruent to
$2a(x)c(x)A(x^p)$. Its degree in the first factor is at most $2m$, strictly smaller than $j\bmod p$. Its target coefficient is zero. Thus $\kappa_p$ in (960.23) and (960.25) is independent of this arithmetic lift. In particular it is an invariant in $\mathbf F_p$ of the original polynomial $H$, not of an unchosen absolute CM period.

## 8. An equivalent original Fourier coefficient

In this section the two modular forms are exactly
$$
v=V_4^\dagger,\qquad
F=V_{p-1}^\dagger
=F_{p-1}(Q)-2^{p-1}\zeta^2F_{p-1}(Q^4).
$$
Thus $F(E_u,\rho)=-D^{N+1}C(u^3)$ as in R958. It is not the Hasse polynomial $H$, nor the scalar $D^{N+1}H$; the polynomial $H$ appears only in the Kummer cover and its lift.

There is a useful expression in the original width-six cusp. Choose the geometric lift in §5 using the actual normalized level-one Eisenstein series $E_{p-1}$. Its evaluation in (960.3) has the form
$$
E_{p-1}(E_u,\rho)=uD^{N+1}\widetilde H(u^3)
$$
with an integral degree-$N$ polynomial reducing to $H$. For example this shape follows termwise from the level-one weight relation $4a+6b=p-1$: necessarily $a=1+3i$, $b=N-2i$, and the evaluations of $E_4,E_6$ give precisely the displayed factors. Integrality follows from the integral modular section and the same tame divisor argument used in R958. Its Fourier expansion is congruent to one modulo $p$.

The original Tate branch also fixes the unit used in §5. The evaluations at infinity are $E_4(E_u,\rho)\sim24^2u^4$ and $E_6(E_u,\rho)\sim24^3u^6$. Since the normalized $E_{p-1}$ has cusp constant one, its leading coefficient is $24^d$; hence $(-4)^{N+1}\widetilde H_N=24^d$, and the original Tate branch takes $w_0=24$. The normalized differential in (960.21) is consequently $-24\,du/y=4s\,\Phi_4(v)$, using $s^2=-3$. This determines the branch and scale rather than leaving a new period unit unspecified.

Put
$$
E(Q)=E_{p-1}(Q^6),\qquad e(Q)=\frac{E(Q)-1}{p}.
$$
At the corresponding Igusa cusp the normalized formal logarithm in coordinate $Q$ has invariant differential
$$
v(Q) E(Q)^{-2/(p-1)}\,\frac{dQ}{Q}.
\tag{960.27}
$$
This follows from (960.9) and the Hasse root $E(Q)^{1/(p-1)}$, with leading coefficient one in the original Tate frame. It is a lift of the same one-dimensional formal factor. Moreover $z=1/u=4sQ+O(Q^2)$. A change of parameter with linear coefficient $c$ changes the first possible $p^2$ coefficient by $c^{1-p^2}$. Here $c=4s\in\mathbf F_{p^2}^\times$, so that factor is one. Consequently the coefficient is exactly the same $\kappa_p$ as (960.23).

The original CM relation gives $[Q^{p^2}]v=-p^3$: the prime $p$ is inert for the normalized weight-four CM form, and the $Q^4$ oldform does not contribute at an odd index. Expanding the other factor in (960.27) modulo $p^2$ therefore yields
$$
\boxed{\quad
\kappa_p=2[Q^{p^2}]\,v(Q)e(Q)\pmod p.
\quad}
\tag{960.28}
$$
For a direct residual formula, von Staudt--Clausen gives
$pB_{p-1}\equiv-1\pmod p$; hence
$$
e(Q)\equiv-2\sum_{n\ge1}\sigma_{p-2}(n)Q^{6n}\pmod p,
\quad
\Theta_Qe=\frac{E_2(Q^6)-E_2(Q^6)^p}{2}.
\tag{960.29}
$$
The second identity includes the $p$-divisible indices: for $p\nmid n$, $n\sigma_{p-2}(n)=\sigma_1(n)$ modulo $p$, and the remaining terms are exactly removed by $E_2^p$.

Finally the original companion identity is $\Theta_Q^2F=v$ modulo $p$. At coefficient $Q^{p^2}$, integration by parts twice changes $[Q^{p^2}](\Theta_Q^2F)e$ into $[Q^{p^2}]F\Theta_Q^2e$; no division by the zero index $p^2\bmod p$ is made. Ramanujan's identity, with the original factor six, gives
$\Theta_Q^2e=(E_2(Q^6)^2-E_4(Q^6))/4$. Thus
$$
\boxed{\quad
\kappa_p=\frac12[Q^{p^2}]
F(Q)\bigl(E_2(Q^6)^2-E_4(Q^6)\bigr).
\quad}
\tag{960.30}
$$
Equivalently this is half that Fourier coefficient of the actual homogeneous modular form
$$
F\bigl(144\mathcal B^2-\mathcal A^2E_4\bigr)
\in S_{3p+1}(H_6),
\tag{960.31}
$$
because $\mathcal A(Q)=1$ and $12\mathcal B(Q)=E_2(Q^6)$. The form $F$ here is the unchanged original high CM vector, including the sign and phase of R939/R958. Equations (960.28--31) identify a concrete coefficient; none proves it nonzero.

## 9. The remaining assertion

The outstanding $r=2$ full-trace question is now the particular Jacobi-coefficient assertion
$$
\frac1p[x^{(p^2-1)/3}]
\left((1-x/4)^{N+1}
\frac{\widetilde H^{\rm rev}(x)}{\widetilde H_N}\right)^{2p+2}
\not\equiv0\pmod p.
\tag{960.32}
$$
All operations and the lift independence in this formula have been proved. The value may equivalently be tested by the original Fourier coefficient (960.30). There is no positivity argument in a finite field, and a one-dimensional formal group with the displayed unramified quadratic action can have height greater than two. Thus its dimension or its cubic automorphism does not settle (960.32).

R945 also continues to prohibit using even a proof of this full-trace nonvanishing as a unit-source identification with the central original normal derivative. The present result addresses the actual Cartier chain and full trace, and does not reopen or remove that separate obstruction.

## Sources and exact dependencies

- [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md), §§2--4: original $H_6$ quotient, single $\operatorname{Ig}(p)/\{\pm1\}$ component, complete low character space, and the original full norm extension.
- [R936](R936-explicit-polynomial-trace-of-the-whole-supersingular-pairing.md) and [R939](R939-original-Jacobi-Hasse-and-denominator-free-supersingular-trace.md): exact original scalar family, Hasse polynomial, simple-root and elliptic-point accounting, corrected frame and cusp phase.
- [R958](R958-original-r2-Cartier-matrices-and-one-moment-trace-criterion.md): actual complete two-deck high spaces, both Cartier matrices, and exact single-moment comparison with $S$.
- [R955](R955-original-Cartier-nilpotent-packet-is-a-single-odd-chain.md): original nilpotent chain, its actual CM primary support, and $S\ne0\iff L=1$.
- [R952](R952-exact-Cartier-formula-for-the-last-Hasse-obstruction.md): global Cartier root and the exact pointwise formula used for the invariant block in §3.
- [R956](R956-original-trace-as-a-fixed-low-weight-Cartier-edge-pairing.md): separate exact low-weight edge formulation. The low vector there is not replaced by $v$ in this proof.
- J. Tate, *$p$-Divisible Groups*, in *Proceedings of a Conference on Local Fields* (1967), pp. 158--183: §1.4, p. 160, connected--étale sequences; §2.2, Proposition 1, pp. 162--164, connected formal groups; §2.3, Proposition 3 and Example (b), p. 166, the dual height/dimension relation and the abelian formal completion. [Primary scan](https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf).
- B. Cais, *On the $U_p$ operator in characteristic $p$* (2013), Proposition 3.1 and §3: complete Igusa differential character spaces and the inverse-Frobenius Cartier normalization. [Author paper](https://arxiv.org/pdf/1305.4188).

The specific Kummer equations, full character and branch calculations, height comparison, logarithm, finite coefficient formula, lift-independence argument, and original Fourier identities are proved above. No numerical nonvanishing, new constant-height assertion, or replacement of an original source factor is used.
