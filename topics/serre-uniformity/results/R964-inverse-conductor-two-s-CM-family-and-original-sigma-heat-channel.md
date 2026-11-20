# R964 — The inverse conductor-(2s) CM family and the original sigma heat channel

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved all-weight source and heat identities, with the exact inert Frobenius companion.** The odd CM evaluation family of R954 has an inverse finite-character family. Its first nonzero marked heat variation is precisely the original section $(x_0^3+2)\sigma_0^6$. This gives an exact factorial-normalized identity in every weight and the actual same-label index $h_{i+2}$ in the first-$p$ range. The result does not identify this family with R913's original Jacobian companion, or identify pointwise values through a higher differential equation. No mathematical computation is executed.

## 1. The companion character and its complete generator

Retain $\mathcal O=\mathbf Z[\zeta]$, the positive embedding $s=1+2\zeta=i\sqrt3$, $\rho=1+\zeta$, $Q=e^{2\pi i\tau/6}$, and $\epsilon=\epsilon_{2s}$ of R954. For $(\alpha,2s)=1$, $\epsilon(\alpha)$ is the unique unit $u\in\mu_6$ such that $u\alpha\equiv1\pmod{2s}$; it is zero otherwise. Define
$$
H_{6a}^{\rm inv}(Q)
=\sum_{\mathfrak a\text{ prime to }2s}
       \epsilon(\alpha)^{-1}\alpha^{6a-1}Q^{N\mathfrak a},
\qquad a\ge1,
\tag{964.1}
$$
where $(\alpha)=\mathfrak a$. This is independent of the generator because
$\epsilon(u)^{-1}=u$ for $u\in\mu_6$. Its first $Q$ coefficient is one.

Use the complete two-variable source
$$
\mathcal J^{\rm inv}(z,w;\tau)
=\sum_{\alpha\in\mathcal O}
 \epsilon(\alpha)^{-1}
 e^{2\pi i(\alpha z+\overline\alpha w)}Q^{N\alpha}.
\tag{964.2}
$$
The inverse character is extended by zero off the units. Conjugation of the finite character is its inverse. Reindexing the complete Wagner source by $\alpha\mapsto\overline\alpha$ therefore gives, at $w=0$,
$$
\mathcal J^{\rm inv}(z,0;\tau)
=\tfrac12\{R_2(z,\tau)+R_3(z,\tau)+R_4(z,\tau)+sR_0(z,\tau)\},
\tag{964.3}
$$
Here the original theta convention of R954 is retained, and explicitly
$$
R_a=\theta_a^*(z;\tau)\theta_a(sz;\tau),\quad
\theta_a^*(z;\tau)=\frac{\eta(\tau)\theta(2z;\tau)}{\theta_a(z;\tau)}
\quad(a=2,3,4),
$$
while $R_0=\theta^*(z;\tau)\theta(sz;\tau)$ with
$\theta^*=\eta\theta(2z)/\theta(z)$. These are exactly the terms of R959 §1. Relative to R954 only the displayed sign has changed. More generally the first arguments of the starred theta functions are $z+w$, and the second arguments are $s(z-w)$; the same plus sign in front of the odd term applies. This follows by substituting $z_1=6(z+w)$, $z_2=-2s(z-w)$ in the original two-variable identity, before restricting either variable.

The unit action is
$$
\mathcal J^{\rm inv}(uz,\overline u w;\tau)
=u^{-1}\mathcal J^{\rm inv}(z,w;\tau).
\tag{964.4}
$$
Thus the one-variable source has precisely the degrees $5\pmod6$, and
$$
\mathcal J^{\rm inv}(z,0;\tau)
=6\sum_{a\ge1}H_{6a}^{\rm inv}(Q)
                 \frac{(2\pi iz)^{6a-1}}{(6a-1)!}.
\tag{964.5}
$$
The S and T calculation of R959 applies term by term to the plus-sign combination as well: its $T$ multiplier is $\rho$, and under $(z,\tau)\mapsto(z/\tau,-1/\tau)$ the common factor is $-\tau$ because $3+s^2=0$. The nonzero ideal norms are $1\pmod6$, so the quotient by $\eta^4$ is holomorphic at the full-level cusp with constant term one. Consequently
$$
H_{6a}^{\rm inv}/\eta^4\in M_{6a-2}(\mathrm{SL}_2(\mathbf Z)).
\tag{964.6}
$$
These full-level forms have an $E_4$ factor: a monomial of weight $6a-2$ in $E_4,E_6$ has its $E_4$ exponent congruent to one modulo three. The Fourier coefficients are integers, since conjugate ideals give conjugate algebraic integers, and $\eta^4/Q$ has an integral power-series inverse. The basis
$$
E_4 E_6^{a-1-2b}\Delta^b,\qquad 0\le b\le\lfloor(a-1)/2\rfloor,
$$
has respective initial terms $q^b$ with coefficient one. Integral triangular elimination therefore gives
$$
\boxed{
\frac{H_{6a}^{\rm inv}}
 {\eta^4E_4E_6^{a-1}}
=\widetilde R_{a-1}\!\left(\frac{\eta^{24}}{E_6^2}\right),
\quad \widetilde R_{a-1}\in\mathbf Z[U],\quad
\deg\widetilde R_{a-1}\le\lfloor(a-1)/2\rfloor,
\quad\widetilde R_{a-1}(0)=1.
}
\tag{964.7}
$$
In particular $H_6^{\rm inv}=\eta^4E_4$ is forced by the full weight-four space, without a numerical coefficient computation.

## 2. The actual marked two-variable heat calculation

At $\tau=\rho$ put
$$
\Lambda=\mathbf Z+\rho\mathbf Z,\quad
x=\wp_\Lambda,\quad y=\wp_\Lambda'/2,\quad
\sigma=\sigma_\Lambda,\quad g_3(\Lambda)=4\Omega^6.
$$
The positive real $\Omega$ is the unchanged period of R949. Thus
$y^2=x^3-\Omega^6$ and the original curve has lattice $\Omega\Lambda$.

Exactly as in R954, each term of (964.3) is an entire section with the multipliers of $\sigma^6$. Its class under $z\mapsto uz$ is five. The original six-dimensional space of R697 has basis
$$
\sigma^6,\quad x\sigma^6,\quad y\sigma^6,\quad x^2\sigma^6,\quad xy\sigma^6,\quad x^3\sigma^6;
$$
its classes are respectively $0,4,3,2,1,0$. Class five is absent, so
$$
\mathcal J^{\rm inv}(z,0;\rho)=0
\quad\text{for all }z.
\tag{964.8}
$$

Define
$$
K(z)=\partial_w\mathcal J^{\rm inv}(z,w;\rho)|_{w=0}.
$$
This is genuinely a section of the same degree-six line. To check the point, let $\lambda=m+n\rho\in\Lambda$. The arguments $z+w$ and $s(z-w)$ shift respectively by $\lambda$ and $s\lambda$. The parity signs cancel just as in R954, and their common multiplier is
$$
\exp(6\eta_\Lambda(\lambda)(z+\lambda/2))
\exp(-2\pi i(3n-(2m+n)s)w).
$$
The extra term produced upon differentiating the second exponential multiplies (964.8), hence is zero. Therefore $K$ has precisely the $\sigma^6$ multiplier. Differentiating (964.4) shows $K(uz)=K(z)$. The actual weight-zero section space of R697 is two-dimensional, so
$$
K(z)=(a+b x(z)^3)\sigma(z)^6.
\tag{964.9}
$$

Its value at zero follows from the complete lattice sum. Reindexing by conjugation gives
$$
K(0)=2\pi i\sum_\alpha\epsilon(\alpha)^{-1}\overline\alpha Q^{N\alpha}
=12\pi i H_2(Q)=12\pi i\eta^4.
$$
Thus $b=12\pi i\eta^4$.

The $z^6$ coefficient is fixed by the already identified $H_6^{\rm inv}$:
$$
[z^6]K
=\frac{6(2\pi i)^7}{6!}\Theta_Q H_6^{\rm inv}
=\frac{36(2\pi i)^7}{6!}\Theta_\tau(\eta^4E_4),
$$
where $\Theta_\tau=(2\pi i)^{-1}d/d\tau$ and $\Theta_Q=6\Theta_\tau$. At the mark $E_4=0$,
$\Theta_\tau E_4=-E_6/3$, and R949 gives
$(2\pi i)^6E_6=-864\Omega^6$.
It follows that
$$
[z^6]K/b=\frac{12}{5}\Omega^6.
$$
The original Laurent normalization gives
$$
x^3\sigma^6=1+\frac25\Omega^6z^6+O(z^{12}),\qquad
\sigma^6=z^6+O(z^{12}).
$$
Substitution in (964.9) therefore yields the exact source
$$
\boxed{
K(z)=12\pi i\eta(\rho)^4
                 (x(z)^3+2\Omega^6)\sigma(z)^6.
}
\tag{964.10}
$$
This uses a two-dimensional geometric section space and two forced normalizations, not a fit of an unproved formula to a coefficient window.

Termwise differentiation of (964.2) gives its complete heat equation
$$
\partial_\tau\mathcal J^{\rm inv}
=\frac1{12\pi i}\partial_z\partial_w\mathcal J^{\rm inv}.
\tag{964.11}
$$
The factor uses the norm exponent $Q^{N\alpha}$ with $Q=e^{2\pi i\tau/6}$. Combining (964.10) and (964.11),
$$
\boxed{
\partial_\tau\mathcal J^{\rm inv}(z,0;\rho)
=\eta(\rho)^4\frac d{dz}
              \bigl((x(z)^3+2\Omega^6)\sigma(z)^6\bigr).
}
\tag{964.12}
$$

## 3. The all-weight marked identity on the original curve

On the original normalized curve define
$$
H_0(z)=(x_0(z)^3+2)\sigma_0(z)^6
       =\sum_{a\ge0}h_a z^{6a},\qquad h_0=1.
\tag{964.13}
$$
This is an original theta section, namely the displayed fixed combination of the two weight-zero sections. It is not the $H_k^{\rm inv}$ modular form. Lattice scaling gives
$$
(x(z)^3+2\Omega^6)\sigma(z)^6=H_0(\Omega z).
$$
At the mark all $H_{6a}^{\rm inv}$ have the $E_4$ factor. Differentiating it once gives
$$
\partial_\tau H_{6a}^{\rm inv}|_{\rho}
=-\frac{2\pi i}{3}\eta(\rho)^4E_6(\rho)^a
        \widetilde R_{a-1}(-1/1728).
$$
Compare the coefficient of $z^{6a-1}$ in (964.5) and (964.12). Using the unchanged scale
$\left(\Omega/(2\pi i)\right)^6/E_6(\rho)=-1/864$ yields
$$
\boxed{
\widetilde R_{a-1}(-1/1728)
=-\frac{(6a)!}{2}(-864)^{-a}h_a
\qquad(a\ge1).
}
\tag{964.14}
$$
For every prime $p>3$ with $6a<p$, the scalar multiplying $h_a$ is a $p$-adic unit. The quotient on the left belongs to $\mathbf Z[1/6]$, so the formula also proves $p$-integrality of $h_a$ in this range and gives
$$
h_a\equiv0\pmod p\quad\Longleftrightarrow\quad
\left[\frac{H_{6a}^{\rm inv}}{\eta^4E_4E_6^{a-1}}\right]_{\rm mark}\equiv0\pmod p.
$$
The quotient is the regular marked quotient after its forced $E_4$ zero; $\eta^4$ and $E_6$ are units at the mark. For $6a\ge p$ the characteristic-zero identity remains valid, but its factorial must not be removed after reduction. No nonvanishing is inferred in either range.

## 4. The actual Frobenius companion of an odd evaluation form

Let $p\equiv5\pmod6$, $k=6j+2<p+1$, and $r=p+1-k>0$. At the chosen inert reduction, $\alpha^p=\overline\alpha$. On coefficients prime to $p$,
$$
N(\alpha)^r\epsilon(\alpha)\alpha^{k-1}
=\epsilon(\alpha)\overline\alpha^{r+1}.
$$
Reindex by conjugation; the finite character becomes $\epsilon^{-1}$. Coefficients from ideals divisible by $(p)$ vanish on both sides modulo $p$. Therefore
$$
\boxed{
\Theta_Q^r W_k=H_{r+2}^{\rm inv}\pmod p
\quad\text{as complete }Q\text{ series}.
}
\tag{964.15}
$$
When $\Theta_Q$ is interpreted as the Katz modular operator, weight matching restores the exact Hasse factor:
$$
\boxed{
\Theta_Q^r W_k=\mathcal A^{r+1}H_{r+2}^{\rm inv},
\qquad k+r(p+1)=(r+1)(p-1)+(r+2).
}
\tag{964.16}
$$
The Tate-normalized Hasse invariant $\mathcal A$ has $Q$ series one. Thus (964.16) follows from (964.15) and the modular $q$ expansion principle; no ordinary-prime interpolation is used.

For the unchanged original critical pair, write
$$
p=6N+5\ge41,\qquad 0\le i\le N-1,\qquad j=N-1-i,\qquad h=6i+7.
$$
The application retains $p\equiv2,5\pmod9$ and the separate actual primitivity condition $(h,p+1)=1$. Here $k=6j+2=p-h-2$, and the companion equation means
$$
r=6i+10,\qquad r+2=6(i+2).
\tag{964.17}
$$
The new companion's marked quotient is therefore controlled by $h_{i+2}$ in (964.14), not by the even sequence $f_i$ and not by the original Igusa companion assigned to label $h$. If $j\ge1$, then $i+2\le N$, so $6(i+2)<p$ and the factorial in that comparison is a unit. The boundary $j=0$ has $g_0=1$ already, but $i+2=N+1$ and $6(i+2)=p+1$; the unit comparison is not available there.

Equation (964.16) is a higher differential identity. It does not identify the value $W_k(\rho)$ with the first derivative of $H_{r+2}^{\rm inv}$, or imply that their zeros agree. A further argument would be needed to turn this genuine companion/source coupling into an exclusion of the common factor in R959(CM17). In particular neither the original Legendre value $P_{h-1}(1/s)$ nor the primitive mask is changed, and the two evaluation weights from R954 remain $h-3$ and $p-h-2$. They are not replaced by R913's $2h-p+1$ and $2p+2-2h$. No such pointwise or source identification is asserted here.


## Sources and exact dependencies

- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md): the original $c=0$ sigma, signed odd section, six-dimensional theta line, and its unit classes. The present $H_0$ is the displayed fixed linear combination of its two class-zero sections.
- [R949](R949-original-all-weight-sigma-CM-marked-identity.md), §§1 and 7: the unchanged positive period $\Omega$, lattice scaling, original marking, and exact scale $\left(\Omega/(2\pi i)\right)^6/E_6(\rho)=-1/864$.
- [R954](R954-original-odd-sigma-and-conductor-two-s-CM-evaluations.md), §§2–4 and 6: the exact conductor-$(2s)$ finite character, complete Wagner theta source, original $W_{6j+2}$ family, and unchanged same-label indices.
- [R959](R959-exact-coarse-CM-factor-criterion-for-the-original-antidiagonal.md), §1: the full S and T transformations, cancellation of the Gaussian, and integral triangular modular-basis argument. Its exact common-factor criterion is retained as the unresolved target.
- [R913](R913-original-Igusa-Cartier-functional-and-two-CM-companions.md): the distinct original Igusa companions and the complete modular normalization, used here to state precisely which source identifications are not made.
- Ian Wagner, *Jacobi forms with CM and applications*, [arXiv:2208.01807](https://arxiv.org/abs/2208.01807), §4.1.2, Propositions 4.1–4.2 and 4.5; published in *Journal of Number Theory* **246** (2023), 15–48, [doi:10.1016/j.jnt.2022.11.014](https://doi.org/10.1016/j.jnt.2022.11.014). The theta conventions and original specialization are the ones already fixed in R954; the inverse-character sign, mixed heat derivative, complete source scalar and all-weight evaluation are derived above.

The first-$p$ reduction and the $j=0$ endpoint are stated explicitly. No finite coefficient window, numerical interpolation, or uniform nonvanishing claim is used. The original same-label three-factor question and the main Serre-uniformity problem remain open.
