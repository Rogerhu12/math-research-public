# R957 — The original Legendre filter as a fixed-pole CM convolution

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift. **Status: proved source and kernel identities.** This gives a new closed kernel for the actual Legendre-weighted antidiagonal of R949/R954, retaining the original primitive labels. Its pole order is seven, independent of the prime. It does not prove that the resulting marked CM value or polynomial is nonzero. No mathematical computation or finite interpolation is used.

The unfiltered sigma convolution, the finite Legendre average, and the primitive projection are already in R770. The six-section addition kernel and its limitations are already in R782/R788; the complete horizontal primitive/Legendre source is already in the unitary cross-heat note. The new assertions here are the common positive-CM lattice source, its exact marked normalization, and the fixed six-degree kernel obtained from a genus-zero Cartier calculation.

## 1. The actual antidiagonal and the two unchanged evaluation families

Keep the original constants and marking of R949/R954:
$$
\zeta=e^{2\pi i/3},\quad s=1+2\zeta=i\sqrt3,\quad
\rho=1+\zeta=-\zeta^2,\quad
Q=e^{2\pi i\tau'/6},\quad \tau'_{\rm mark}=\rho.
\tag{957.1}
$$
The original sigma function has zero quadratic exponential parameter,
$$
E_0:y^2=x^3-1,\quad dz=\frac{dx}{2y},\qquad
F_0=x\sigma^6=z^4\sum_{i\ge0}f_i z^{6i},\quad
G_0=-xy\sigma^6=z\sum_{j\ge0}g_j z^{6j}.
\tag{957.2}
$$
Let $p=6N+5\ge41$ be prime, and put
$$
\ell=N-1,\qquad d=6\ell+4=p-7.
\tag{957.3}
$$
For $0\le i\le\ell$ the actual paired index and original label are
$$
j=\ell-i,\qquad h=6i+7,\qquad
m_1=h-3=6i+4,\quad m_2=p-h-3=6j+1.
\tag{957.4}
$$
Thus $m_1+m_2=p-6$, and the Jacobi degrees below are
$m_1-1$ and $m_2$, whose sum is $d$. Every displayed factorial index is strictly below $p$.

Write $V_k^\dagger$ for the original positive-CM oldform of R949 and $W_k$ for the conductor-$(2s)$ evaluation family of R954. Their exact marked identities are
$$
\left[\frac{V_{6i+4}^\dagger}{V_4^\dagger E_6^i}\right]_{\rm mark}
=\frac{(6i+4)!}{24}(-864)^{-i}f_i,
$$
$$
\left[\frac{W_{6j+2}}{\eta^4E_6^j}\right]_{\rm mark}
=(6j+1)!(-864)^{-j}g_j.
\tag{957.5}
$$
In particular the two modular weights in the same-label product are
$h-3$ and $p-h-2$. They have sum $p-5$. They are not identified with the two Igusa weights of R913, and the second evaluation family is not identified with the original Jacobian companion.

## 2. A common positive-CM lattice source, including the original oldform phase

Let $\mathcal O=\mathbf Z[\zeta]$. Retain the two finite characters from R949/R954:
$$
\epsilon_3(\alpha)=0\quad(s\mid\alpha),\qquad
\epsilon_{2s}(\beta)=0\quad((\beta,2s)\ne1).
$$
For a unit modulo $(2s)$, $\epsilon_{2s}(\beta)$ is the unique $u\in\mu_6$ with $u\beta\equiv1\pmod{2s}$. The character $\epsilon_3$ is the original quadratic character modulo $(s)$, so $\epsilon_3(2)=-1$.

Define
$$
a(\alpha)=\epsilon_3(\alpha)
       \bigl(1+2\zeta^2\mathbf1_{2\mid\alpha}\bigr),
\qquad b(\beta)=\epsilon_{2s}(\beta).
\tag{957.6}
$$
The parenthesis equals $1$ off $2\mathcal O$ and $-s$ on $2\mathcal O$. It is not a freely chosen oldform direction.

In the notation of R949, put
$$
\mathcal V_e(z,\tau')=\mathcal V(z,\tau'/2)
=J(z,\tau'/2)-2\zeta^2J(2z,2\tau').
$$
Reindexing the second lattice sum by $\alpha=2\gamma$, and using
$\epsilon_3(2)=-1$, gives the complete identity
$$
\boxed{
\mathcal V_e(z,\tau')
=\sum_{\alpha\in\mathcal O}a(\alpha)
                      e^{2\pi i\alpha z}Q^{N\alpha}.
}
\tag{957.7}
$$
The odd generator of R954 uses exactly the same norm exponent:
$$
J_o(z,\tau')=\sum_{\beta\in\mathcal O}b(\beta)
                      e^{2\pi i\beta z}Q^{N\beta}.
\tag{957.8}
$$
For an indeterminate $C$, define the homogeneous moment
$$
\mathcal M_d(C;Q)
=\sum_{\alpha,\beta\in\mathcal O}
 a(\alpha)b(\beta)(C\alpha+\beta)^d Q^{N\alpha+N\beta}.
\tag{957.9}
$$
Every Fourier coefficient is a finite sum, so this is also an integral formal definition. Analytically it is $(2\pi i)^{-d}$ times the $d$th derivative at $z=0$ of
$\mathcal V_e(Cz,\tau')J_o(z,\tau')$.

The two complete Jacobi expansions give
$$
\boxed{
\mathcal M_d(C;Q)
=36\sum_{i+j=\ell}
  \binom d{6i+3}C^{6i+3}
  V_{6i+4}^\dagger W_{6j+2}.
}
\tag{957.10}
$$
Each product has weight $d+2=p-5$ on the common full-six fine cover. There are no omitted Jacobi powers: the even source has degrees $3\pmod6$, and the odd source has degrees $1\pmod6$.

All terms in (957.10) are divisible locally at the actual mark by $V_4^\dagger$. R918's theta formula proves that $V_4^\dagger/E_4$ is a unit there in every characteristic under consideration; $\eta$ and $E_6$ are units there as well. Consequently the following marked quotient is regular, and (957.5) gives
$$
\boxed{
\left[\frac{\mathcal M_d(C;Q)}
 {V_4^\dagger\eta^4E_6^\ell}\right]_{\rm mark}
=\frac32d!(-864)^{-\ell}
   \sum_{i+j=\ell}(6i+4)f_i g_j C^{6i+3}.
}
\tag{957.11}
$$
Indeed $36\binom d{6i+3}(6i+4)!(6j+1)!/24
=(3/2)d!(6i+4)$. This also fixes the factor $36$, the remaining factor $3/2$, and the shift $6i+4$ without a finite coefficient comparison.

## 3. The closed Legendre moment kernel

Reduce at the original inert prime and use a perfect field containing $\mathbf F_{p^2}$. The chosen $s$ satisfies
$s^2=-3$ and $s^p=-s$. For $q\in\mu_{p+1}$ set
$$
R_q=\frac{1+q+q^{-1}}s.
\tag{957.12}
$$
Define two fixed binary forms
$$
\Delta(u,v)=v^2+2uv-3u^2,
$$
$$
\begin{aligned}
K_6(u,v)={}&7v^6-42uv^5+63u^2v^4-196u^3v^3\\
&-189u^4v^2-378u^5v-189u^6.
\end{aligned}
\tag{957.13}
$$
Then, as a polynomial identity in arbitrary $\alpha,\beta$ over the residue field,
$$
\boxed{
\frac1{p+1}\sum_{q\in\mu_{p+1}}
 R_q^3(\alpha R_q+\beta)^{p-7}
=s^{-3}\Delta(\alpha/s,\beta)^{(p-13)/2}
                    K_6(\alpha/s,\beta).
}
\tag{957.14}
$$
All exponents on the right are nonnegative. Thus (957.14) includes
$\alpha=0$, $\beta=0$, and the two degeneracies $\Delta=0$; no denominator involving $\alpha$, $\beta$, or $\Delta$ remains. In the original frequencies the quadratic factor is
$$
\Delta(\alpha/s,\beta)
=\alpha^2+\frac{2\alpha\beta}s+\beta^2
=(\beta-s\alpha)(\beta+s\alpha/3).
\tag{957.15}
$$
In particular the unprojected kernel has a fixed-degree exceptional set of slopes. This is a statement about one lattice summand, not about cancellation in the complete theta sum or at its marked value.

## 4. Proof by a conic with two poles of order seven

Set
$$
D(t)=(t-3)(t+1)=t^2-2t-3,\qquad m=(p-1)/2,
\qquad u=\alpha/s,\quad v=\beta.
$$
For $t\in\mathbf F_p$, the number of $q\in\mu_{p+1}$ with
$t=1+q+q^{-1}$ is $1-\chi(D(t))$. To verify this, use
$q^2-(t-1)q+1=0$. A nonsquare discriminant gives a pair exchanged by Frobenius and hence of norm one; a nonzero square gives no norm-one root, and a zero discriminant gives the single root $q=\pm1$.

Since $p+1=1$ in the residue field, the left side of (957.14) is
$$
s^{-3}\sum_{t\in\mathbf F_p}t^3(ut+v)^{p-7}
                      (1-D(t)^m).
$$
The first summand has degree at most $p-4$ and sums to zero. In the second summand the degree is at most $2p-5<2(p-1)$, so the finite-field power-sum rule leaves just the coefficient of $t^{p-1}$. The signs from the preceding minus sign and $\sum t^{p-1}=-1$ cancel. Thus it suffices to prove
$$
c(u,v):=[t^{p-1}]t^3D(t)^m(ut+v)^{p-7}
=\Delta(u,v)^{m-6}K_6(u,v).
\tag{957.16}
$$

Work first on the open set $u\ne0$, $D(t_0)\ne0$, where $t_0=-v/u$. On the smooth projective conic
$$
Y^2=D(t)
$$
consider the rational differential
$$
\omega=\frac{t^3\,dt}{Y(ut+v)^7}.
\tag{957.17}
$$
It is regular at the branch points and both points at infinity; its only poles are the two points over $t_0$, each of order at most seven. The conic has genus zero.

The equality $Y^p=YD(t)^m$ gives
$$
t^3D(t)^m(ut+v)^{p-7}dt
  =(Y(ut+v))^p\omega.
$$
The polynomial on the left has degree at most $2p-5$. Cartier commutes with the separable pullback from the $t$ line; its coefficient rule and $p^{-1}$-linearity therefore yield
$$
\mathcal C\omega
=c(u,v)^{1/p}\frac{dt}{Y(ut+v)}.
\tag{957.18}
$$
Choose $y_0$ with $y_0^2=D(t_0)$ and let $P_+=(t_0,y_0)$. Its residue is
$$
r=\operatorname{Res}_{P_+}\omega
 =u^{-7}\frac1{6!}
       \left.\left(\frac d{dt}\right)^6\frac{t^3}{Y}
        \right|_{P_+}.
\tag{957.19}
$$
The other residue is $-r$. Because $p>7$, Cartier leaves at most simple poles at these points, with residues $r^{1/p}$ and $-r^{1/p}$. There is no holomorphic differential on the conic to add. Equivalently, comparing the residue in (957.18) gives
$$
c(u,v)=(uy_0)^p r.
\tag{957.20}
$$
This uses the exact differential and its two complete polar parts; it does not infer a specified marked value from global nonvanishing.

For a fully explicit evaluation of (957.19), define the rational polynomials
$$
R_n(t)=\frac{D(t)^{n+1/2}}{n!}
                  \left(\frac d{dt}\right)^n\frac{t^3}{\sqrt{D(t)}}.
$$
Ordinary differentiation gives the finite recurrence
$$
R_0=t^3,\qquad
R_{n+1}=\frac{D R_n'-(2n+1)(t-1)R_n}{n+1}.
\tag{957.21}
$$
For clarity, the steps needed for $n=6$ are
$$
\begin{aligned}
R_1={}&2t^4-5t^3-9t^2,\\
R_2={}&t^5-5t^4+27t^2+27t,\\
R_3={}&-7t^3-27t^2-27t-27,\\
R_4={}&7t^4+32t^3+36t^2+54t-27,\\
R_5={}&-7t^5-37t^4-48t^3-108t^2+81t-81,\\
R_6={}&7t^6+42t^5+63t^4+196t^3-189t^2+378t-189.
\end{aligned}
\tag{957.22}
$$
These are paper polynomial identities under (957.21); no numerical interpolation is involved. All denominators in the recurrence and in $6!$ are units for the primes under consideration.

Since $y_0^p=y_0D(t_0)^m$, equations (957.19)–(957.22) give
$$
c(u,v)=u^{p-7}D(t_0)^{m-6}R_6(t_0).
$$
Now $D(t_0)=\Delta(u,v)/u^2$ and
$u^6R_6(-v/u)=K_6(u,v)$. The powers of $u$ cancel exactly, since
$(p-7)-2(m-6)-6=0$. This proves (957.16) on the stated open set. Both sides are polynomials in $u,v$, so the identity extends over the entire affine plane, including the degenerate cases. This proves (957.14).

## 5. The actual primitive filter and the resulting CM source

Let
$$
r_p=\prod_{\substack{q\mid p+1\\q\text{ prime},\ q>3}}q.
$$
For a polynomial $H(C)$ define operators in characteristic $p$ by
$$
(\mathscr L H)(C)=\frac1{p+1}
       \sum_{q\in\mu_{p+1}}R_q^3 H(R_qC),
$$
$$
(\mathscr P H)(C)=
\sum_{e\mid r_p}\frac{\mu(e)}e
              \sum_{\lambda\in\mu_e}\lambda^4H(\lambda C).
\tag{957.23}
$$
The letter $q$ in the first sum denotes a root of unity, not a prime. The two operators commute.

On the actual powers $C^{6i+3}$ they act by
$$
\mathscr L:C^{6i+3}\longmapsto
       P_{6i+6}(1/s)C^{6i+3},
$$
$$
\mathscr P:C^{6i+3}\longmapsto
       \mathbf1_{(6i+7,p+1)=1}C^{6i+3}.
\tag{957.24}
$$
The first statement is the exact finite constant-term formula of R770: the exponent $6i+6=h-1$ is below $p+1$, so averaging over $\mu_{p+1}$ extracts only the Laurent constant term of $(1+q+q^{-1})^{h-1}$. For the second, $e^{-1}\sum\lambda^{6i+7}$ is the indicator of $e\mid6i+7$, and $6i+7$ is automatically prime to six. These are the unchanged original primitive and Legendre conditions, now expressed in the Jacobi variable $C$.

Define the finite frequency kernel
$$
\boxed{
\mathcal K_p(\alpha,\beta)=s^{-3}
 \sum_{e\mid r_p}\frac{\mu(e)}e
 \sum_{\lambda\in\mu_e}\lambda^4
 \Delta(\lambda\alpha/s,\beta)^{(p-13)/2}
 K_6(\lambda\alpha/s,\beta).
}
\tag{957.25}
$$
Every $e$ is prime to $p$, and every $\lambda$ lies in $\mu_{p+1}\subset\mathbf F_{p^2}$. No order-$p$ denominator is introduced. Equation (957.14), applied before any theta summation, proves the complete Fourier identity
$$
\boxed{
\begin{aligned}
\mathcal T_p(C;Q)
&:=(\mathscr P\mathscr L\mathcal M_d)(C;Q)\\
&=\sum_{\alpha,\beta\in\mathcal O}
     a(\alpha)b(\beta)\,
     \mathcal K_p(C\alpha,\beta)Q^{N\alpha+N\beta}
      \pmod p.
\end{aligned}
}
\tag{957.26}
$$
Here frequencies and finite characters are reduced at the chosen original prime. The identity is coefficientwise: every Fourier coefficient contains only finitely many pairs. The finite characters, the $-s$ coefficient on $2\mathcal O$, and the positive CM powers are all retained.

Applying these operators to (957.11) gives the exact marked polynomial
$$
\boxed{
\left[\frac{\mathcal T_p(C;Q)}
 {V_4^\dagger\eta^4E_6^\ell}\right]_{\rm mark}
=\frac32d!(-864)^{-\ell}
 \sum_{i=0}^{\ell}
 \mathbf1_{(6i+7,p+1)=1}(6i+4)
 P_{6i+6}(1/s)f_i g_{\ell-i}C^{6i+3}.
}
\tag{957.27}
$$
The quotient means division by the actual common simple zero before evaluation; it is not the zero value of $\mathcal T_p$ itself at the mark. Its denominator has the same total weight $p-5$ as its numerator. Reduction is legitimate by (957.5) and the marked units stated after (957.10).

The scalar in front of the sum and all $6i+4$ are units. Therefore the polynomial in (957.27) is nonzero if and only if some actual nonendpoint primitive label has
$$
P_{h-1}(1/s)f_{(h-7)/6}g_{(p-h-4)/6}\ne0.
\tag{957.28}
$$
This is exactly the same-label three-factor condition in R770. Evaluating (957.27) at $C=1$ gives a single sufficient weighted sum; its vanishing alone does not imply that the polynomial is zero.

## 6. Scope of the new constraint

The Legendre part of (957.26) is now a fixed seventh-order pole calculation with an explicit degree-six numerator. The prime still occurs in the quadratic power, in the primitive root-of-unity averages, and in the degree of the marked polynomial. The formula does not make the complete primitive source a fixed-dimensional space.

There is no positivity in the residue field. A nonzero lattice kernel, a nonzero Fourier series, and a nonzero global geometric class do not by themselves give a nonzero value of the quotient at the original mark. In particular no step above claims that the right side of (957.27) is nonzero. Its nonvanishing, or another constraint forcing one of its original coefficients to be nonzero, remains a concrete missing step. The original rational-point exclusion and the topic completion criterion remain open.

## Dependencies and provenance

- [R949](R949-original-all-weight-sigma-CM-marked-identity.md), especially (949.7), (949.12–14): the original positive CM family, oldform phase, and full sigma normalization.
- [R954](R954-original-odd-sigma-and-conductor-two-s-CM-evaluations.md), especially (954.2), (954.6), (954.8–10): the conductor-$(2s)$ evaluation family and complete odd generator.
- [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md), (918.22): the actual simple zero and unit $V_4^\dagger/E_4$ in good characteristic.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md): the original antidiagonal, finite Legendre average, and primitive mask, which are reused rather than re-registered as new nonvanishing results.
- The new common-lattice formula, the genus-zero Cartier calculation, and the polynomial identities are proved above. No local or public numerical arithmetic is used.
