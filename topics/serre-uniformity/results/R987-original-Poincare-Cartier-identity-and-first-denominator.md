# R987 — Original Poincare Cartier identity and its first denominator

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b. Authoring agent: literature_frontier; independently reviewed by root, handoff_audit, and legendre_shift. No mathematical computation was run locally.

**Status: proved identities; no uniform nonvanishing assertion.** The main identity identifies the actual Cartier moments of the original invariant-differential primitive with the original rational Kronecker connection functions. The proof uses the concrete two-open-set transition and residues; it does not infer equality from a Hecke eigencharacter, a leading pole, or a common scalar model. The first nonintegral column and the actual theta connection's p-curvature are also calibrated. No uniform nonvanishing assertion is made.

## 1. Fixed original source and the two primitives

Keep the original primes and the original curve of R978/R980/R984/R986:
\[
p\ge41,\qquad p\equiv-1\pmod6,\qquad
E_+:y^2=x^3+1,\qquad \omega=\frac{dx}{2y},\qquad t=-x/y,
\tag{987.1}
\]
and put
\[
k=\mathbb F_{p^2},\quad q=p^2,\quad
\beta=E_{p+1}(E_+,\omega)/12\pmod p\in\mathbb F_p^\times,
\qquad D=\omega^{-1}d.
\tag{987.2}
\]
The invariant derivation is $D=2y\partial_x+3x^2\partial_y$. The reduction of the original connection functions will be denoted by $L_j$ without a bar in this note.

The inputs from R986 are genuine rational functions on this same curve:
\[
Z=-\beta^{-1}D^{p-2}x,\qquad
dZ=\omega,
\tag{987.3}
\]
\[
J=J_s,\qquad dJ=(-x+\beta t^{p-1})\omega,
\qquad
\mathcal T=Z+\beta^{-1}J^p,\qquad d\mathcal T=\omega.
\tag{987.4}
\]
Here $J_s$ is the square-root-parameter primitive of R986, not R984's different actual-$t$ primitive. Its poles are contained in $\{O\}\cup E[2]^{\ne0}$, the differential $J_s\omega$ has a simple pole of residue one at $O$, and its constant coefficient there is zero. The function $Z$ has its only pole at $O$, of order $p$. The function $\mathcal T$ is regular at $O$, is a uniformizer there, and agrees with the original strict Lubin--Tate coordinate through degrees below $q$.

For reference, the scale in (987.3) follows without an unproved period comparison. The invariant derivation satisfies $D^p=0$: its restricted $p$th power is another invariant derivation, and the $\mu_6$ action with $p\equiv-1\pmod6$ forces its scalar to vanish. Hence $D^{p-1}x$ is a rational $p$th power with only a possible pole of order at most $p+1$ at $O$. A $p$th root could have only a simple pole at $O$, which is impossible on a genus-one curve unless it is constant. In the strict Lubin--Tate coordinate, the coefficient of $T^{p-1}$ in $x$ is $p\mathcal G_{p+1}\equiv\beta$. Wilson's formula gives
\[
D^{p-1}x=-\beta.
\tag{987.5}
\]
The leading term of $D^{p-2}x$ is $t^{-p}$; thus $Z$ has leading term $-\beta^{-1}t^{-p}$. The $\mu_6$ character removes the constant ambiguity. This is the same $Z$ as in R986. The identities $D^p=0$ and $D^{p-1}x=-\beta$ are the already established R574 input, with the $E_+$ scale of R986; they are recalled here to fix the normalization, not registered as new results.

## 2. The finite connection functions extend through index p minus one

Use the original canonical sigma function, with $(g_2,g_3)=(0,-4)$, and write
\[
\Theta(z,W)=\frac{\sigma(z+W)}{\sigma(z)\sigma(W)},\qquad
\Xi(z,W)=e^{-\zeta(z)W}\Theta(z,W)
=\sum_{j\ge0}L_j(z)W^{j-1}.
\tag{987.6}
\]
Thus $L_0=1,L_1=0$. These are the functions of R984, not a shifted torsion-point theta kernel.

The proof of R984, Section 2, extends by one index on this fixed source:
\[
L_j\in\mathbb Z_p[x,y],\qquad 0\le j\le p-1.
\tag{987.7}
\]
Indeed
\[
W\Xi(z,W)=\exp\left(
-\sum_{m\ge2}\frac{D^{m-2}x}{m!}W^m
+\sum_{m\ge4}\frac{\mathcal G_m}{m}W^m\right).
\tag{987.8}
\]
All factorials required at indices below $p$ are units. The only extra potentially nonintegral pure term at index $p-1$ is exactly zero on $E_+$, since $6\nmid p-1$ and the $\mu_6$ symmetry forces $\mathcal G_{p-1}=0$ in characteristic zero. The remaining pure terms are integral by the argument already given in R984.

Put
\[
X(P,w)=\sum_{j=0}^{p-1}L_j(P)w^j
\quad\text{in }k(E)[w]/(w^p).
\tag{987.9}
\]
Every $L_j$ is regular away from $O$. The finite kernel associated with the actual $J_s$ is
\[
K_J(P,w)=w^{-1}e^{J(P)w}X(P,w)\pmod{w^{p-1}}.
\tag{987.10}
\]
All exponentials here and below are truncated at degree $p-1$ in the nilpotent variable; each factorial is a unit.

The square-root-parameter version of R984 gives
\[
K_J(P,w)-t^{-1}-w^{-1}\in k[[t,w]]\pmod{w^{p-1}}.
\tag{987.11}
\]
Only the residue, and not the regular difference between $s^{-1}$ and $t^{-1}$, is relevant in (987.11). To justify its use with $J_s$, take the actual integral regularized zeta function $R_s(s)$ supplied by Guerzhoy in this strict integral parameter. R986 gives
\[
\overline{R_s}=J_s+h_s^p,\qquad h_s\in s\,k[[s]].
\tag{987.12}
\]
The proof of R984 then applies verbatim, with $s$ in place of $t$: the true integral product has only a simple origin pole, and multiplication by $e^{-h_s^pw}$ cannot introduce any additional pole. Extending (987.7) to $j=p-1$ is precisely what permits (987.11) through $w^{p-2}$.

In particular $wK_J$ has at most a simple pole at $O$, with residue $w$ after multiplication by $\omega$.

## 3. Exact Cartier identity

Let $C$ be the Cartier operator on rational differentials of $E_+/k$, normalized by
\[
C\left(\sum_m a_m u^mdu\right)
=\sum_n a_{pn+p-1}^{1/p}u^n du.
\tag{987.13}
\]
We claim
\[
\boxed{\qquad
\frac{C(xZ^j\omega)}{\omega}
=\beta^{1-j}j!L_j,
\qquad 0\le j\le p-1.
\qquad}
\tag{987.14}
\]
This identifies the complete rational functions, including every possible lower pole and constant correction.

Set $B=k[W]/(W^p)$, and define coefficientwise Cartier generating functions
\[
H_U(P,W)=\sum_{j=0}^{p-1}
\frac{W^j}{j!}\frac{C(xZ^j\omega)}{\omega},
\qquad
H_V(P,W)=\sum_{j=0}^{p-1}
\frac{W^j}{j!}\frac{C(x\mathcal T^j\omega)}{\omega}.
\tag{987.15}
\]
The variable $W$ is an auxiliary parameter held fixed in this coefficientwise operation. We do not apply absolute Frobenius to it. Since the binomial coefficients, factorials, and $\beta$ lie in $\mathbb F_p$, the usual rule $C(a^pf\omega)=aC(f\omega)$ and (987.4) give the exact transition
\[
H_V=e^{WJ/\beta}H_U\quad\text{in }k(E)\otimes_k B.
\tag{987.16}
\]

Use the actual open cover
\[
U=E\setminus\{O\},\qquad
V=E\setminus E[2]^{\ne0}.
\tag{987.17}
\]
The function $H_U$ is regular on $U$, because $x$ and $Z$ have poles only at $O$ and Cartier creates no new poles. On $V$, the function $\mathcal T$ is regular. At $O$ it is a uniformizer with $d\mathcal T=\omega$. Consequently $x\mathcal T^j\omega$ has pole order at most $2-j$ at $O$. The case $j=0$ has zero residue; the case $j=1$ has residue one; the cases $j\ge2$ are regular. Applying (987.13) therefore shows that $H_V\omega$ has only a simple pole at $O$, of residue exactly $W$.

Compare these two functions with
\[
G_U=\beta X(P,W/\beta),\qquad
G_V=e^{WJ/\beta}G_U
=W K_J(P,W/\beta).
\tag{987.18}
\]
By (987.7), $G_U$ is regular on $U$. By (987.11), $G_V\omega$ has only a simple pole at $O$, also of residue $W$, and is otherwise regular on $V$.

Thus $D_U=H_U-G_U$ and $D_V=H_V-G_V$ satisfy
\[
D_U\in\mathcal O(U)\otimes B,
\qquad D_V\in\mathcal O(V)\otimes B,
\qquad D_V=e^{WJ/\beta}D_U.
\tag{987.19}
\]

Here is a direct residue-rigidity argument. Suppose the common lowest nonzero $W$-degree is $m$. Its two coefficients agree on $U\cap V$, so they define a regular function on the projective curve $E$. This coefficient is a nonzero constant $c\in k$. If $m\le p-2$, the next degree in (987.19) gives
\[
d_{V,m+1}-d_{U,m+1}=cJ/\beta.
\tag{987.20}
\]
Multiply by $\omega$ and take the residue at $O$. The left side has residue zero: the first term is regular there, while the second is a rational differential whose only possible pole is $O$, so its residue is zero by the global residue theorem. The right side has residue $c/\beta$, since $\operatorname{Res}_O(J\omega)=1$. This is a contradiction. Hence the only possible difference is
\[
D_U=D_V=cW^{p-1}.
\tag{987.21}
\]

Finally, the actual $\mu_6$ action kills this last constant. If an automorphism has multiplier $\alpha\in\mu_6$ on $\omega$, then $x$ has character $\alpha^{-2}$ and $Z$ has character $\alpha$. Cartier takes the scalar $\alpha^{j-1}$ to $\alpha^{(j-1)/p}=\alpha^{1-j}$; after division by $\omega$ the coefficient in $H_U$ has character $\alpha^{-j}$. The same is the character of $L_j$. At $j=p-1$, this is $\alpha^{-(p-1)}=\alpha^2$, which is nontrivial for a primitive sixth root. A constant cannot have that character, so $c=0$.

Equations (987.15), (987.18), and (987.21) prove (987.14). In particular the origin ambiguity left by a twisted trace argument is removed by the original local residues and their actual transition, not by imposing an unproved equality on that ambiguity.

## 4. The first actual denominator in the connection functions

The same fixed source identifies the first denominator, rather than merely bounding it. In (987.8), all contributions to $L_p$ except the single exponent term $-D^{p-2}x/p!$ are integral: a product of terms of indices below $p$ uses only unit factorials, and the pure term of odd index $p$ is zero. Therefore
\[
\boxed{\quad pL_p\pmod p=D^{p-2}x=-\beta Z.\quad}
\tag{987.22}
\]
The sign follows from $(p-1)!\equiv-1$.

For the actual square-root-parameter regularization write $l_s(s)=\int_0^s\omega$ and put
\[
K_s(s,W)=e^{R_s(s)W}\Xi(l_s(s),W),
\qquad M_p(s)=[W^{p-1}]K_s(s,W).
\tag{987.23}
\]
Then $pM_p$ is integral, and only the terms $L_p$ and $R_s^p/p!$ survive its reduction. Using (987.12) and (987.4) gives
\[
\boxed{\quad
pM_p\pmod p
=-\beta Z-\overline R_s^{\,p}
=-\beta\mathcal T-h_s^q.
\quad}
\tag{987.24}
\]
After the original strict integral substitution $s=g_s(T)$, R986 yields the precise finite boundary
\[
pM_p(g_s(T))\equiv-\beta T\pmod{p,T^q}.
\tag{987.25}
\]
Thus the coefficient of $T W^{p-1}$ in this one-sided regularized kernel has valuation exactly $-1$. In all other $T$-degrees below $q$, this first $W$-column has integral coefficients. There is no assertion that the full untruncated two-variable kernel is integral.

The genuine second-variable Frobenius correction cancels this displayed boundary in its finite range. More precisely, replace $W$ by $l_{\rm LT}(U)$, and multiply by
\[
\exp\left(-\frac\mu p l_{\rm LT}(T)
                    l_{\rm LT}^{\varphi}(U^p)\right).
\tag{987.26}
\]
At $U$-degree $p-1$ and $T$-degree below $q$, this changes the coefficient by $-\mu T/p$; since $\bar\mu=-\beta$, it cancels (987.25). Degrees below $p-1$ in $U$ are unaffected. This proves only the stated finite cancellation, not a supersingular analogue of an ordinary integral theta measure.

## 5. The actual finite theta connection and its p-curvature

On $k(E)[w]/(w^p)$, let $X$ be (987.9). It is a unit, and the connection obtained from the original theta kernel is
\[
\nabla_\Theta=D+xw-D\log X.
\tag{987.27}
\]
Indeed $D\log\Theta=-xw+D\log X$ before reduction. The rational gauge $X$ gives
\[
\nabla_\Theta(Xf)=X(D+xw)f.
\tag{987.28}
\]
For a derivation and a scalar multiplication operator, the characteristic-$p$ identity is
$(D+a)^p=D^p+a^p+D^{p-1}a$. Applying (987.5), $D^p=0$, and $w^p=0$ shows
\[
\boxed{\quad \psi_{\nabla_\Theta}(D)=-\beta w.\quad}
\tag{987.29}
\]

For the square-root-parameter source, the actual rational regularization is
\[
\nabla_J=\nabla_\Theta-\beta t^{p-1}w.
\tag{987.30}
\]
By (987.4), this is precisely the gauge of the trivial connection by $e^{Jw}X$; its $p$-curvature is zero. R984's actual-$t$ source has the different correction $\beta(tf)^{p-1}w$, where $\omega=f(t)dt$. These two corrections must not be interchanged.

The nonzero scalar in (987.29) and the exact cancellation in (987.30) concern the actual Poincare connection. They do not say that any specified interior coefficient of its horizontal section is nonzero. In particular they do not replace the still required unit statement for $c_{p-r}$.

## 6. Scope and dependencies

The principal new conclusion is (987.14), with its full rational-function normalization. It can be combined with R986's exact rational Lubin--Tate jet to compare the original pure high Hurwitz coefficient with the original balanced Kronecker coefficient. That contraction, with all factorials and the $E_+/E_-$ phase, is a separate subsequent comparison and is not assumed in this proof.

The proof uses only the established R984 finite kernel, the explicit R986 primitives, the Cartier formula, and the global residue theorem. It does not use an ordinary unit-root splitting, a two-variable $p$-adic measure, the disproved common-$\xi$ factorial model of R983, or a high-block continuation of the old sigma addition kernel. The identities do not by themselves prove that either remaining near-prime coefficient is a unit.

Sources and already established conventions:

- [R984](R984-frobenius-regularized-finite-Kronecker-kernel-and-rational-Cartier-descent.md), *A genuine Frobenius-regularized finite Kronecker kernel and rational Cartier descent*, for the original $L_j$, integral regularization, and simple-pole product.
- [R986](R986-explicit-rational-primitive-and-original-Lubin-Tate-jet.md), the actual square-root-parameter Cartier primitive and rational strict Lubin--Tate jet, for $J_s$, $Z$, $\mathcal T$, and the finite degree-$q$ precision.
- [R980](R980-original-level-one-Hurwitz-reflection-and-distinct-mirror-pairs.md), for the exact pure $\mathcal G_k$ normalization and $\beta=E_{p+1}(E_+,\omega)/12$.
- Bannai--Kobayashi--Tsuji, *On the de Rham and p-adic realizations of the elliptic polylogarithm for CM elliptic curves*, ASENS **43** (2010), Definitions 1.5--1.6, for the connection functions used throughout: <https://www.numdam.org/item/10.24033/asens.2119.pdf>.
- Guerzhoy, *On the p-adic values of the weight two Eisenstein series for supersingular primes*, Research in the Mathematical Sciences **12**, article 64 (2025), equation (4), Proposition 1, Corollary 1, and Theorem 1, as checked in R984: <https://arxiv.org/pdf/2403.02592>.

- [R574](R574-completed-zeta-Cartier-input.md), for the established invariant-derivation primitive; [R594](R594-formal-log-decomposition-and-wide-prime-c0-obstruction.md), equations (594.4)–(594.7), and [R658](R658-Cartier-trace-comparison-and-actual-Cp-channel.md), Section 5, for the already registered finite formal logarithm decomposition. The new assertion here is the complete bare connection-function identity (987.14), proved by its actual transition and residue obstruction.
