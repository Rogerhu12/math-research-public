# R966 — A single CM rank-two kernel for the original critical sigma jet

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved complete two-variable source and exact filtered-jet identities.**
The conductor-$(2s)$ source of R954, with both CM variables retained, has an
exact rank-two expression at the original mark. A specified second-order
meromorphic differential operator and the original unit projection recover
the actual tensor $F_0\otimes G_0$. Its primitive and Legendre filtered critical
jet is therefore a jet of this single CM source. The marked polynomial of
R959 is its derivative with an explicit unit factor. Its nonvanishing is not
proved here.

The six-rank sigma addition kernel of R784, the first-$p$ cross corrections of
R788, and the unitary cross-heat source are retained. The new statement is the
specific conductor-$(2s)$ two-variable CM kernel below; it is not another proof
of those already registered addition identities. No mathematical computation,
coefficient window, or interpolation is executed.

## 1. The complete original CM source

Keep the positive embedding and original mark
$$
\mathcal O=\mathbf Z[\zeta],\qquad
s=1+2\zeta=i\sqrt3,\qquad \rho=1+\zeta,
\qquad Q=e^{2\pi i\tau/6},\qquad \tau_{\rm mark}=\rho.
$$
The finite character $\epsilon=\epsilon_{2s}$ is the one in R954: for
$(\alpha,2s)=1$, $\epsilon(\alpha)$ is the unique $u\in\mu_6$ such that
$u\alpha\equiv1\pmod{2s}$, and it is zero off the units. In particular
$\epsilon(u)=u^{-1}$ and
$\epsilon(\overline\alpha)=\epsilon(\alpha)^{-1}$.

Define the complete, normally convergent two-variable series
$$
\mathcal J_o(z,w;\tau)
=\sum_{\alpha\in\mathcal O}
\epsilon(\alpha)
 e^{2\pi i(\alpha z+\overline\alpha w)}Q^{N\alpha}.
\tag{966.1}
$$
At $w=0$ this is exactly R954's $J_o$. In the same theta conventions,
Wagner's full source, specialized before either variable is set to zero, is
$$
\mathcal J_o(z,w;\tau)
=\frac12\left\{
 \sum_{a=2}^4\theta_a^*(z+w;\tau)\theta_a(s(z-w);\tau)
 -s\theta^*(z+w;\tau)\theta(s(z-w);\tau)\right\}.
\tag{966.2}
$$
Here the starred theta functions are precisely
$\theta_a^*=\eta\theta(2z)/\theta_a(z)$ and
$\theta^*=\eta\theta(2z)/\theta(z)$ from R954. The sign of the last term
is the original minus sign. Conjugating the ideal generator gives
$$
\mathcal J^{\rm inv}(z,w;\tau)=\mathcal J_o(w,z;\tau),
\qquad
\mathcal J_o(uz,\overline u w;\tau)=u\mathcal J_o(z,w;\tau)
\quad(u\in\mu_6).
\tag{966.3}
$$
Thus the inverse-character source of R964 is the transpose of this source,
not a new unchosen theta phase.

## 2. Both actual multipliers and the five-dimensional allowed space

At $\tau=\rho$ write
$$
\Lambda=\mathbf Z+\rho\mathbf Z,\qquad
x=\wp_\Lambda,\quad y=\wp'_\Lambda/2,\quad
Z=\zeta_\Lambda,\quad \sigma=\sigma_\Lambda,\quad S=\sigma^6,
$$
$$
y^2=x^3-\Omega^6,\qquad x'=2y,\qquad y'=3x^2,
\qquad \Omega>0.
\tag{966.4}
$$
The period $\Omega$ is exactly R949's original one. Its quasiperiod is
$\eta_\Lambda(\lambda)=(2\pi/\sqrt3)\overline\lambda$. Put
$$
\gamma=6\eta_\Lambda(1)=4\pi\sqrt3,
\qquad
\widehat{\mathcal J}_o(z,w)
=e^{\gamma zw}\mathcal J_o(z,w;\rho).
\tag{966.5}
$$
This fixed mixed Gaussian is specified by the source multipliers. It does
not change the original zero quadratic parameter of $\sigma$.

For clarity, both translations can be checked directly. If
$\lambda=m+n\rho$, then
$$
s\lambda=-(m+2n)+(2m+n)\rho.
$$
The starred factor in (966.2) has theta index $3/2$ and the second factor
has index $1/2$. Their signs cancel as in R954. The part of their common
multiplier involving the other variable is
$$
\exp\bigl(-2\pi i(3n-(2m+n)s)w\bigr)
=e^{-\gamma\lambda w}
$$
for translation in $z$. The same calculation in the other variable gives
$e^{-\gamma\lambda z}$. The complete formulas are
$$
\begin{aligned}
\mathcal J_o(z+\lambda,w;\rho)
 &=e^{6\eta_\Lambda(\lambda)(z+\lambda/2)}
   e^{-\gamma\lambda w}\mathcal J_o(z,w;\rho),\\
\mathcal J_o(z,w+\lambda;\rho)
 &=e^{6\eta_\Lambda(\lambda)(w+\lambda/2)}
   e^{-\gamma\lambda z}\mathcal J_o(z,w;\rho).
\end{aligned}
\tag{966.6}
$$
Consequently the mixed Gaussian in (966.5) cancels exactly the extra
factor in each variable. The result is an entire section of the genuine
external product $L_6\boxtimes L_6$, where $L_6=O(6[O])$ is R697's line.

Use its actual basis
$$
S,\quad xS,\quad yS,\quad x^2S,\quad -xyS,\quad x^3S.
$$
The respective unit classes are $0,4,3,2,1,0$. Since the mixed Gaussian
is unchanged by $(z,w)\mapsto(uz,\overline u w)$, (966.3) permits only
class pairs $a-b=1\pmod6$. Thus the entire allowed tensor space is the
span of the following five tensors:
$$
G\otimes S,\quad G\otimes x^3S,\quad
x^2S\otimes G,\quad Y\otimes x^2S,\quad F\otimes Y,
\tag{966.7}
$$
where $G=-xyS$, $F=xS$, and $Y=yS$. This is a complete space calculation,
including both class-zero basis vectors; no unlisted theta component is
discarded.

## 3. Exact determination of all five coefficients

Set $K=12\pi i\eta(\rho)^4$ and
$H=(x^3+2\Omega^6)S$. R964 gives
$$
\mathcal J_o(0,w;\rho)=0,\qquad
\left.\partial_z\mathcal J_o(z,w;\rho)\right|_{z=0}=K H(w).
$$
Differentiating the Gaussian produces a term multiplying the first,
identically zero expression. Since $G(z)=z+O(z^7)$ and the other first
factors in (966.7) have orders at least two, the first two coefficients
are therefore exactly the single tensor $K G\otimes H$.

The remaining three coefficients are forced by the base family
$W_2=\eta^4$. Write $L=(2\pi i)^2$, let
$D_b=\Theta_Q^b\eta^4/\eta^4$, and keep
$\Theta_Q=6\Theta_\tau$. The complete lattice source gives
$$
\frac{[z^{b+1}w^b]\widehat{\mathcal J}_o}{K}
=\sum_{q=0}^b\frac{\gamma^q}{q!}
 \frac{L^{b-q}D_{b-q}}{(b-q+1)!(b-q)!}.
\tag{966.8}
$$
This formula follows by taking the corresponding mixed derivative of
(966.1): $\alpha^{b+1}\overline\alpha^b=\alpha N(\alpha)^b$, so the
lattice sum is the $b$th $\Theta_Q$ derivative of the actual weight-two
series. There is no guessed relation between different CM weights.

Ramanujan's identities give, exactly,
$$
D_0=1,\quad D_1=E_2,\quad
D_2=\frac{3E_2^2-E_4}{2},\quad
D_3=3E_2^3-3E_2E_4+E_6.
\tag{966.9}
$$
All Eisenstein values in this section are at the same $\rho$.
The quasiperiod normalization of R949 gives
$$
E_2(\rho)=\frac{2\sqrt3}{\pi},\qquad
\gamma=-\frac{L E_2(\rho)}2,\qquad
E_4(\rho)=0,\qquad L^3 E_6(\rho)=-864\Omega^6.
\tag{966.10}
$$
Substitution in the finite formula (966.8) gives respectively
$$
\begin{array}{c|c}
b&[z^{b+1}w^b]\widehat{\mathcal J}_o/K\\ \hline
1&0\\
2&-L^2E_4/24=0\\
3&L^3E_6/144=-6\Omega^6.
\end{array}
\tag{966.11}
$$
For example the cubic expression before specialization has its $E_2^3$
coefficient $1/48-3/48+3/48-1/48=0$ and its $E_2E_4$ coefficient
$-1/48+1/48=0$, leaving exactly $E_6/144$.

The leading terms $x^2S=z^2+\cdots$, $Y=-z^3+\cdots$, and
$F=z^4+\cdots$ now identify each of the remaining three entries of
(966.7). The two middle tensors have zero coefficient, and the last
has coefficient $6K\Omega^6$. Therefore
$$
\boxed{
e^{4\pi\sqrt3 zw}\mathcal J_o(z,w;\rho)
=12\pi i\eta(\rho)^4
\left\{G(z)H(w)+6\Omega^6 F(z)Y(w)\right\}.
}
\tag{966.12}
$$
The two first factors are independent, as are the two second factors;
their unit classes differ. Hence the tensor rank is exactly two.
The proof fixes every coefficient in the complete five-dimensional
allowed space by exact source identities, not by fitting a coefficient
window to an unproved global expression.

## 4. The original sigma tensor is a specified derivative of this source

Return to the original curve and coordinate
$$
E_0:y_0^2=x_0^3-1,\qquad du=dx_0/(2y_0),\qquad
F_0=x_0\sigma_0^6,\quad G_0=-x_0y_0\sigma_0^6,
$$
$$
Y_0=y_0\sigma_0^6,\qquad H_0=(x_0^3+2)\sigma_0^6.
$$
The same lattice scaling as R949/R964 yields the normalized source
$$
\begin{aligned}
\mathscr K_0(u,v)
&=\frac{\Omega}{12\pi i\eta(\rho)^4}
 e^{(4\pi\sqrt3/\Omega^2)uv}
 \mathcal J_o(u/\Omega,v/\Omega;\rho)\\
&=G_0(u)H_0(v)+6F_0(u)Y_0(v).
\end{aligned}
\tag{966.13}
$$
The right side gives the algebraic source over $\mathbf Q$, with the
unchanged $c=0$ sigma identification. In particular its definition is
not an arbitrary choice of an absolute CM period modulo $p$.

Let $Z_0=\zeta_{\Lambda_0}$ denote the original Weierstrass zeta function,
and define the specified meromorphic derivative in the second variable
by
$$
\nabla_v=\partial_v-6Z_0(v).
$$
It means exactly $\nabla_v(f\sigma_0^6)=f'\sigma_0^6$ in the rational
frame $\sigma_0^6$. Put
$$
\Pi_4^u T(u,v)=\frac16\sum_{\epsilon\in\mu_6}
 \epsilon^{-4}T(\epsilon u,v).
$$
Since $y_0''=12x_0y_0$, one has
$$
\nabla_v^2Y_0=12x_0y_0\sigma_0^6=-12G_0.
$$
The projection kills the class-one first tensor in (966.13). Therefore
$$
\boxed{
\Pi_4^u\nabla_v^2\mathscr K_0(u,v)
=-72F_0(u)G_0(v).
}
\tag{966.14}
$$
The derivative is taken with the first variable fixed. Although its
unprojected first tensor can have a pole at $v=0$, that entire tensor
is removed by $\Pi_4^u$; the displayed result is holomorphic there.
This is a complete identity of the named sources, not a value inferred
from a high Bol identity at the supersingular mark.

## 5. The exact critical jet and both unchanged filters

Let $p=6N+5\ge41$ be prime, put $\ell=N-1$, and retain the original
labels $h=6i+7$, $0\le i\le\ell$, $j=\ell-i$. The application still
requires $p\equiv2,5\pmod9$ and $(h,p+1)=1$.

First perform the differential operator in (966.14), and only then set
$u=Ct$, $v=t$. The actual unfiltered critical polynomial is
$$
\begin{aligned}
\mathcal U_p^{\rm raw}(C)
&=-\frac1{72}[t^{p-6}]
 \left(\Pi_4^u\nabla_v^2\mathscr K_0\right)(Ct,t)\\
&=\sum_{i+j=\ell}f_i g_j C^{6i+4}.
\end{aligned}
\tag{966.15}
$$
All required coefficients are in the first-$p$ integral range of
R697/R702. No full, nonintegral infinite sigma series is reduced modulo
$p$. Equivalently one uses the algebraic section (966.13) and its proved
local comparison in this range.

For explicitness put
$r=\prod_{q\mid(p+1),\ q>3}q$, a product of distinct primes, and define
$$
\begin{aligned}
\mathcal P_3 U(C)
 &=\sum_{e\mid r}\frac{\mu(e)}e
       \sum_{\lambda\in\mu_e}\lambda^3 U(\lambda C),\\
\mathcal L_2 U(C)
 &=\frac1{p+1}\sum_{q\in\mu_{p+1}}R_q^2 U(R_q C),
\qquad R_q=\frac{1+q+q^{-1}}s.
\end{aligned}
\tag{966.16}
$$
These are the original R770/R957 filters with the exponent shift
appropriate to (966.15). Indeed, for $a=6i+4$, the primitive exponent is
$a+3=h$, while the Legendre moment exponent is $a+2=h-1$.
Every latter exponent is less than $p+1$, as required by the exact
finite Legendre average. The factors are consequently $\lambda^3$ and
$R_q^2$, rather than the $\lambda^4$ and $R_q^3$ used for R957's
degree-$6i+3$ source. Nothing about the actual labels is changed.

The operators commute, and their exact output is
$$
\boxed{
\mathcal U_p(C):=\mathcal P_3\mathcal L_2\mathcal U_p^{\rm raw}(C)
=\sum_{i=0}^{\ell}
 \mathbf1_{(6i+7,p+1)=1}P_{6i+6}(1/s)
 f_i g_{\ell-i} C^{6i+4}.
}
\tag{966.17}
$$
These coefficients are in $\mathbf F_p$. Thus $\mathcal U_p$ is nonzero
if and only if some original permitted label has all three original
factors nonzero. This statement retains the primitive and Legendre
conditions; no neighboring label is substituted.

Finally let $\mathscr B_p(C,X)$ be exactly R959(CM16), and set
$X_0=-1/24$. R957(957.27), with the original $\zeta^2$ oldform phase
already fixed by R949, gives
$$
\boxed{
\mathscr B_p(C,X_0)
=\frac32(p-7)!(-864)^{-(N-1)}
              \frac d{dC}\mathcal U_p(C).
}
\tag{966.18}
$$
Indeed the derivative multiplies each term by $6i+4$ and lowers its
$C$ exponent by one, precisely the two changes in R957(957.27).
The scalar and every $6i+4$ are units modulo $p$. Hence this derivative
is injective on the specified support, and
$$
\mathcal U_p=0
\quad\Longleftrightarrow\quad
\mathscr B_p(C,X_0)=0
\quad\Longleftrightarrow\quad
(1+24X)\mid\mathscr B_p(C,X).
\tag{966.19}
$$

## 6. What this source identity does and does not force

Equations (966.12)–(966.14) are a coupling of the actual original
sections, including $F_0\otimes G_0$. They retain more than the isolated
$H_0$ channel of the inverse family. The single CM source, its fixed
mixed Gaussian, the second-order derivative, both finite filters, and
the exact marked-polynomial comparison have all been specified.

The global rank-two source and the global tensor in (966.14) are
nonzero. That alone does not imply that their degree-$p-6$ filtered jet
is nonzero: a nonzero section can have a zero selected homogeneous jet,
and the primitive and Legendre operators can remove coefficient
directions. Nor does a zero value at $C=1$ mean that the entire
polynomial (966.17) is zero. No such implication is used here.

The remaining assertion is exactly $\mathcal U_p\ne0$ for the required
primes, or another genuine restriction excluding the common factor in
(966.19). The original rational-point exclusion and the main
Serre-uniformity problem remain open.

## Sources and exact dependencies

- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md): the original zero-parameter sigma, the full degree-six section space and its unit classes.
- [R949](R949-original-all-weight-sigma-CM-marked-identity.md): positive period, quasiperiod and $E_6$ scales, the named $F_0$, and the unchanged original $\zeta^2$ oldform direction.
- [R954](R954-original-odd-sigma-and-conductor-two-s-CM-evaluations.md): exact conductor-$(2s)$ character, Wagner source and theta conventions, and $J_o(z,\rho)=12\pi i\eta(\rho)^4G(z)$.
- [R964](R964-inverse-conductor-two-s-CM-family-and-original-sigma-heat-channel.md), (964.8) and (964.10): the identically zero transposed one-variable source and its exactly normalized first mixed derivative.
- [R957](R957-original-Legendre-filter-as-a-fixed-pole-CM-convolution.md), (957.27), and [R959](R959-exact-coarse-CM-factor-criterion-for-the-original-antidiagonal.md), (CM16)–(CM17): the original marked polynomial, all scalar factors, and its exact common-factor criterion.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md): the actual antidiagonal, primitivity and finite Legendre moments. These filters are reused here.
- Ian Wagner, *Jacobi forms with CM and applications*, [arXiv:2208.01807](https://arxiv.org/abs/2208.01807), Propositions 4.1–4.2 and 4.5; published in *Journal of Number Theory* **246** (2023), 15–48, [doi:10.1016/j.jnt.2022.11.014](https://doi.org/10.1016/j.jnt.2022.11.014). Only the already normalized complete source of R954 is used; the two multipliers, rank-two decomposition and critical-jet comparison are proved above.
