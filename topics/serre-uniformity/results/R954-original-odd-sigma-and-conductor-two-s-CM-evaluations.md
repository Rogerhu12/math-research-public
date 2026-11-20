# R954 — The original odd sigma sequence as a conductor-(2s) CM evaluation family

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift. **Status: proved for every integer $j\ge0$ in characteristic zero, with the full original sigma and period normalization.** This supplies the second sequence complementary to R949. The new modular forms have conductor $(2s)$; they are explicitly an evaluation family, not a claimed identification with the original Jacobian's Hecke companion. No finite interpolation or mathematical computation is used.

## 1. The original odd sequence and the exact new CM family

Retain R949's positive constants and original curve:
$$
\zeta=e^{2\pi i/3},\quad s=1+2\zeta=i\sqrt3,
\quad \rho=1+\zeta=-\zeta^2,
\quad E_0:y_0^2=x_0^3-1,
$$
$$
dz=\frac{dx_0}{2y_0},\qquad
\Lambda_0=\Omega\mathbf Z[\zeta],\quad\Omega>0,
\qquad
G_0(z)=-x_0(z)y_0(z)\sigma_0(z)^6
      =z\sum_{j\ge0}g_jz^{6j},\quad g_0=1.
\tag{954.1}
$$
The sigma function has its original zero quadratic exponential parameter. The word “odd” refers to this odd function of $z$; the modular weights below are the even integers $6j+2$.

Let $\epsilon_{2s}$ be the following finite character of
$(\mathbf Z[\zeta]/(2s))^\times$. For $\alpha$ prime to $(2s)$, choose the unique $u\in\mu_6$ such that
$$
u\alpha\equiv1\pmod{2s},\qquad
\epsilon_{2s}(\alpha)=u.
\tag{954.2}
$$
Existence and uniqueness follow because reduction identifies $\mu_6$ with this unit group: its two CRT factors have orders three and two. Extend the character by zero off the units. In particular
$\epsilon_{2s}(u)=u^{-1}$ for $u\in\mu_6$.

For $k=6j+2$ define the positive CM theta form
$$
H_k(q)=\sum_{\mathfrak a\text{ prime to }(2s)}
             \Psi_k(\mathfrak a)q^{N\mathfrak a},
\qquad
\Psi_k((\alpha))=\epsilon_{2s}(\alpha)\alpha^{k-1},
\qquad a_1=1.
\tag{954.3}
$$
The displayed value is independent of the generator, since
$k-1\equiv1\pmod6$. Its finite character is primitive modulo $(2s)$: it is nontrivial on both CRT factors. Thus these are the usual CM cusp forms of level
$|D_{\mathbf Q(s)}|N(2s)=36$. Their nebentypus is trivial because on rational integers prime to six the finite character is the quadratic character of $\mathbf Q(s)$. The finite character remains the same for every $j$; it does not become the conductor-$(s)$ character in R913.

Use the same full-six parameter as before,
$$
Q=e^{2\pi i\tau'/6},\qquad
W_k(\tau')=H_k(Q),
\tag{954.4}
$$
and the same analytic marked point $\tau'=\rho$. Put
$$
\mathcal D_{6j+2}^{\rm mark}
=\left[\frac{W_{6j+2}}{\eta(\tau')^4E_6(\tau')^j}
  \right]_{\tau'=\rho}.
\tag{954.5}
$$
Both denominator factors are nonzero at this point. The theorem is
$$
\boxed{
\mathcal D_{6j+2}^{\rm mark}
=(6j+1)!(-864)^{-j}g_j,
\qquad
A_{6j+2}=(-108)^j\mathcal D_{6j+2}^{\rm mark}
\quad(j\ge0).
}
\tag{954.6}
$$
Here $A_{6j+2}$ is the original signed square root of R697(697.2). There is no factor six in its second equality. This differs from the even sigma sequence in R949 precisely because the original base ordinary derivative is $G_0'(0)=1$, whereas $F_0^{(4)}(0)=24$.

## 2. A complete Jacobi source with the specified finite character

Use R949(949.8)'s odd theta convention, so
$\theta_z(0;t)=2\pi i\eta(t)^3$. Let $\theta_2,\theta_3,\theta_4$ be the corresponding standard even theta functions. Define
$$
\theta^*(z;t)=\eta(t)\frac{\theta(2z;t)}{\theta(z;t)},
\qquad
\theta_a^*(z;t)=\eta(t)\frac{\theta(2z;t)}{\theta_a(z;t)}
\quad(a=2,3,4).
\tag{954.7}
$$
The quotients are entire, because the zeros of each denominator are contained among the zeros of $\theta(2z;t)$. These expressions agree, including their signs, with Wagner's shifted $\theta_a^*$ in Propositions 4.1–4.2: substituting the half-period shifts into $\theta^*$ gives exactly (954.7).

Wagner's Proposition 4.5, specialized by $z_1=6z$, $z_2=2sz$, gives the following complete identity:
$$
\begin{aligned}
J_o(z,t)
&:=\sum_{\alpha\in\mathbf Z[\zeta]}
       \epsilon_{2s}(\alpha)e^{2\pi i\alpha z}
                            e^{2\pi itN\alpha/6}\\
&=\frac12\left\{
\theta_3^*(z;t)\theta_3(sz;t)
+\theta_4^*(z;t)\theta_4(sz;t)
+\theta_2^*(z;t)\theta_2(sz;t)
-s\theta^*(z;t)\theta(sz;t)\right\}.
\end{aligned}
\tag{954.8}
$$
For clarity about the embedding, if
$\alpha=(n_1+sn_2)/2$, the source exponent before specialization is
$(n_1z_1+3n_2z_2)/12$. After the displayed substitution it is exactly $\alpha z$. The coefficient is the character determined by (954.2), as in the conductor-$(2s)$ construction preceding that proposition. No replacement by the conjugate power has occurred.

For any $u\in\mu_6$, reindexing the sum gives
$$
J_o(uz,t)=uJ_o(z,t).
\tag{954.9}
$$
As every ideal has six generators, Taylor expansion of the entire source gives
$$
\boxed{
J_o(z,t)=6\sum_{j\ge0}H_{6j+2}(e^{2\pi it/6})
                 \frac{(2\pi iz)^{6j+1}}{(6j+1)!}.
}
\tag{954.10}
$$
Every power of $z$ outside $1\pmod6$ vanishes. Thus (954.10) identifies the whole family, rather than a finite set of Fourier or Taylor coefficients.

## 3. Exact degree-six multipliers at the same marked lattice

Set $t=\rho$ and $\Lambda=\mathbf Z+\rho\mathbf Z$. As in R949, let
$x=\wp_\Lambda$, $y=\wp_\Lambda'/2$, and $\sigma=\sigma_\Lambda$. The quasiperiod map is
$$
\eta_\Lambda(\lambda)=\frac{2\pi}{\sqrt3}\overline\lambda.
\tag{954.11}
$$
It is necessary to check the actual multiplier, since merely having weight one under the CM unit action would not identify a section of the original degree-six line bundle.

Write $\theta_0=\theta$ and, for $a=0,2,3,4$, put
$$
R_a(z)=\eta(\rho)\theta(2z;\rho)
                    \frac{\theta_a(sz;\rho)}{\theta_a(z;\rho)}.
\tag{954.12}
$$
Each is entire by (954.7). If $\lambda=m+n\rho$, then
$$
s\lambda=(-m-2n)+(2m+n)\rho.
\tag{954.13}
$$
For every theta characteristic in (954.12), the translation sign depends only on the two coordinates modulo two. The sign for $s\lambda$ is therefore the sign for $\lambda$, so these signs cancel in the ratio. The sign for the shift $2\lambda$ in $\theta(2z)$ is one. The standard theta translation formula consequently gives
$$
\frac{R_a(z+\lambda)}{R_a(z)}
=\exp\left(-\pi i\bigl(3n^2+(2m+n)^2\bigr)\rho
            -2\pi i\bigl(3n+(2m+n)s\bigr)z\right).
\tag{954.14}
$$
The coefficient of $z$ in this exponent is exactly
$6\eta_\Lambda(\lambda)$. For the constant coefficient put
$N=m^2+mn+n^2=\lambda\overline\lambda\in\mathbf Z$. Then
$$
-\pi i\bigl(3n^2+(2m+n)^2\bigr)\rho
=-4\pi iN\rho
=3\eta_\Lambda(\lambda)\lambda-2\pi iN.
$$
The last summand has exponential one. Thus, for all four summands, the full multiplier is exactly
$$
\boxed{
R_a(z+\lambda)
=e^{6\eta_\Lambda(\lambda)(z+\lambda/2)}R_a(z).
}
\tag{954.15}
$$
These are the multipliers of $\sigma(z)^6$ with its original zero quadratic exponential parameter. There is no remaining flat character or Gaussian modification.

Equation (954.8) is
$J_o(z,\rho)=(R_3+R_4+R_2-sR_0)/2$. Hence it is an entire section of this same degree-six line bundle. Its quotient by $\sigma^6$ is an elliptic function with no pole off $O$ and a pole of order at most six there.

Now use the already proved R697(697.10–11) decomposition of this exact space. Its CM degree class one is a single line, generated by
$$
G_\Lambda(z)=-x(z)y(z)\sigma(z)^6=z+O(z^7).
$$
Equation (954.9), together with the complete multiplier check above, therefore proves
$$
J_o(z,\rho)=K_oG_\Lambda(z)
\tag{954.16}
$$
for one scalar $K_o$. The next section determines that scalar and proves it is nonzero.

## 4. Base derivative and the exact eta factor

For $a=2,3,4$, the theta functions are even and nonzero at zero, so
$\theta_a(sz;t)/\theta_a(z;t)=1+O(z^2)$. For $a=0$, the ratio is
$s+O(z^2)$. Also $\theta(2z;t)=2\theta_z(0;t)z+O(z^3)$.
It follows directly from (954.8) that, for every $t$ in the upper half-plane,
$$
\partial_zJ_o(0,t)
=\eta(t)\theta_z(0;t)(3-s^2)
=6\eta(t)\theta_z(0;t)
=12\pi i\eta(t)^4.
\tag{954.17}
$$
Comparing with the first term of (954.10) proves the complete identity
$$
H_2(e^{2\pi it/6})=\eta(t)^4.
\tag{954.18}
$$
This fixes the normalized base form, rather than introducing an unspecified proportionality constant. At the actual mark it also gives
$$
\boxed{
K_o=12\pi i\eta(\rho)^4\ne0,
\qquad
J_o(z,\rho)=12\pi i\eta(\rho)^4G_\Lambda(z).
}
\tag{954.19}
$$
All signs in this formula use the $-s$ term in (954.8). In particular the contribution of that term to the base derivative is $-s^2=3$, not $-3$.

## 5. All coefficients and the original period

Scaling $\Lambda_0=\Omega\Lambda$ gives
$$
G_\Lambda(z)=\Omega^{-1}G_0(\Omega z)
            =z\sum_{j\ge0}g_j\Omega^{6j}z^{6j}.
\tag{954.20}
$$
Compare (954.10) at $t=\rho$ with (954.19). With $m=6j+1$ this gives
$$
\frac{W_{6j+2}(\rho)}{\eta(\rho)^4}
=m!g_j\left(\frac{\Omega}{2\pi i}\right)^{6j}.
\tag{954.21}
$$
R949(949.35–36), using $g_3(\Lambda_0)=4$, proved the unchanged period relation
$$
\frac{(\Omega/(2\pi i))^6}{E_6(\rho)}=-\frac1{864}.
\tag{954.22}
$$
Division of (954.21) by $E_6(\rho)^j$ proves the first equality in (954.6). Finally R697's actual odd-sequence normalization is
$$
A_{6j+2}=2^{-3j}(6j+1)!g_j.
\tag{954.23}
$$
Together with (954.22), it gives
$A_{6j+2}=(-108)^j\mathcal D_{6j+2}^{\rm mark}$, proving the second equality. Neither an absolute value nor a square has been taken at any stage.

## 6. Integral reduction and the two factors at one original label

For every fixed $j$, R697's arithmetic integrality and (954.6) prove
$$
\mathcal D_{6j+2}^{\rm mark}\in\mathbf Z[1/6].
$$
Thus its reduction vanishes if and only if $A_{6j+2}$ vanishes at every $p>3$. When
$$
6j+1<p,
\tag{954.24}
$$
the factorial in (954.23) is also a unit, and the original sigma coefficient is integral. Hence
$$
\boxed{
g_j=0\pmod p
\quad\Longleftrightarrow\quad
\mathcal D_{6j+2}^{\rm mark}=0\pmod p
\qquad(6j+1<p).
}
\tag{954.25}
$$
No assertion removing this factorial boundary is made. The geometric marked evaluation is well-defined on the same fine full-six model: the pulled-back level-36 forms in (954.4) are modular for $\Gamma(6)$, and $\eta^4$ and $E_6$ are units at this noncuspidal $j=0$ point. The comparison is therefore with the displayed regular quotient, not with an arbitrarily rescaled vector.

The exact consequence for R770's same-label pair can now be stated without changing either index. Let
$$
p=6N+5\ge41,\qquad 0\le i\le N-1,\qquad
j=N-1-i,\qquad h=6i+7.
\tag{954.26}
$$
Any requirement that $h$ be primitive remains the original condition
$(h,p+1)=1$; the formulas do not imply it. Put
$m_1=6i+4=h-3$ and $m_2=6j+1=p-h-3$. Equations (949.7) and (954.6) give the exact characteristic-zero identity
$$
\boxed{
f_i g_j
=\frac{24(-864)^{N-1}}{m_1!m_2!}
\mathcal C_{h-3}^{\rm mark}
\mathcal D_{p-h-2}^{\rm mark}.
}
\tag{954.27}
$$
Both factorials are units modulo $p$, because $m_1,m_2<p$. Consequently the two actual sigma factors vanish jointly or separately exactly as the two displayed actual CM evaluations. In particular
$$
f_i g_j\ne0\pmod p
\quad\Longleftrightarrow\quad
\mathcal C_{h-3}^{\rm mark}
\mathcal D_{p-h-2}^{\rm mark}\ne0\pmod p.
\tag{954.28}
$$
The Legendre factor of this same $h$ is still a separate original factor; it has not been replaced by a neighboring or unshifted value.

These two evaluation weights are $h-3$ and $p-h-2$. They generally differ from R913's original Igusa companion weights
$k_+=2h-p+1$ and $k_-=2p+2-2h$. Moreover their finite characters are those explicitly fixed in R949 and (954.2), respectively. Equations (954.27–28) are therefore exact evaluation identities, not a silent identification of their modular forms with the original primitive cotangent image. They prove neither all-prime nonvanishing nor a supersingular-trace/unit-source comparison to $Q'_h(0)$.

## Sources and proof provenance

- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md), (697.2), (697.4), and (697.10–11): original signed odd sigma sequence, integrality, and the one-dimensional degree-class-one subspace of the actual degree-six line bundle.
- [R949](R949-original-all-weight-sigma-CM-marked-identity.md), §§1 and 7: unchanged original marking, real period, even sequence, and the exact factor $-1/864$.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md): the unchanged same-label indices and separate primitive/Legendre conditions.
- Ian Wagner, *Jacobi forms with CM and applications*, [arXiv:2208.01807](https://arxiv.org/abs/2208.01807), §4.1.2 and Proposition 4.5, printed pp. 11–12, together with Propositions 4.1–4.2 for the theta conventions; published in *Journal of Number Theory* **246** (2023), 15–48, [doi:10.1016/j.jnt.2022.11.014](https://doi.org/10.1016/j.jnt.2022.11.014). The character, positive-embedding specialization, complete multipliers, base scalar, and period normalization required here are all specified above.

No numerical coefficient comparison, extra prime window, or new arithmetic execution is used. The main Serre-uniformity problem and same-label uniform nonvanishing remain open.
