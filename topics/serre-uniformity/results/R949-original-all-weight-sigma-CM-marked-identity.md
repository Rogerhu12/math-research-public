# R949 — The original all-weight sigma–CM marked identity

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift. **Status: proved for every integer $i\ge0$ in characteristic zero, with the original positive CM embedding and full-six marking.** The proof uses a complete Jacobi generating function, its heat equation, and the specified degree-two isogeny. No finite coefficient interpolation or new numerical computation is used. The result does not assert that these values are units at every sufficiently large prime, and does not identify a supersingular trace with the original normal coefficient.

## 1. Statement and the unchanged original sources

Put
$$
\zeta=e^{2\pi i/3},\qquad s=1+2\zeta=i\sqrt3,
\qquad \rho=1+\zeta=-\zeta^2=e^{\pi i/3}.
\tag{949.1}
$$
Keep R697's original real period and sigma function:
$$
E_0:y_0^2=x_0^3-1,\qquad dz=\frac{dx_0}{2y_0},
\qquad \Lambda_0=\Omega\mathbf Z[\zeta],\quad \Omega>0,
$$
$$
F_0(z)=x_0(z)\sigma_0(z)^6
       =z^4\sum_{i\ge0}f_i z^{6i},\qquad f_0=1.
\tag{949.2}
$$
For $k=6i+4$ let $F_k$ be exactly R913's normalized positive CM form of level nine:
$$
F_k(q)=\sum_{\mathfrak a\text{ prime to }(s)}
       \Xi_k(\mathfrak a)q^{N\mathfrak a},\qquad
\Xi_k((\alpha))=\epsilon_3(\alpha)\alpha^{k-1},\qquad a_1=1.
\tag{949.3}
$$
If $\alpha=(n_1+sn_2)/2$ with $n_1\equiv n_2\pmod2$, then
$\epsilon_3(\alpha)=(\frac{2n_1}{3})$; it is extended by zero when $s\mid\alpha$. The power is $\alpha^{k-1}$ in the positive embedding, not $\overline\alpha^{k-1}$.

Use the original full-six variable and oldform direction:
$$
Q=e^{2\pi i\tau'/6},\qquad
V_k^\dagger(\tau')=F_k(Q)-2^k\zeta^2F_k(Q^4).
\tag{949.4}
$$
The marked point is R918–R920's branch
$\vartheta_2(\tau')^4=\zeta\vartheta_4(\tau')^4$ above $j=0$. Its analytic representative is $\tau'=\rho$. In particular this is the branch on which
$$
\left.\frac{E_6}{\eta^{12}}\right|_{\rm mark}=-24s,
\tag{949.5}
$$
as already fixed in R920; no conjugation of this marking is made. The factor $E_6$ throughout this result is $E_6(\tau')$, with Tate constant term one.

Every $V_k^\dagger$ vanishes at this point. Its quotient by $V_4^\dagger$ is regular there, since $V_4^\dagger$ has a simple zero. Define
$$
\mathcal C_k^{\rm mark}
=\left[\frac{V_k^\dagger}{V_4^\dagger E_6^i}\right]_{\rm mark},
\qquad k=6i+4.
\tag{949.6}
$$
Here $\mathcal C_k^{\rm mark}$ is a new notation for this quotient value, not the full six-torsion Kronecker number $C_k$ of R615/R697. The theorem is
$$
\boxed{
\mathcal C_{6i+4}^{\rm mark}
=\frac{(6i+4)!}{24}(-864)^{-i}f_i,
\qquad
A_{6i+5}=6(-108)^i\mathcal C_{6i+4}^{\rm mark}
\quad(i\ge0).
}
\tag{949.7}
$$
The signed $A_{6i+5}$ is precisely R697(697.2), so its sign has not been selected after squaring. In particular $\mathcal C_{6i+4}^{\rm mark}\in\mathbf Z[1/6]$, by R697's integrality theorem.

## 2. A complete positive-CM Jacobi generating function

Set $t=\tau'/2$ and $q_t=e^{2\pi it}$, so $Q=q_t^{1/3}$. Fix the odd theta convention
$$
\theta(z;t)=q_t^{1/8}(e^{\pi iz}-e^{-\pi iz})
\prod_{n\ge1}(1-q_t^n)(1-e^{2\pi iz}q_t^n)
                         (1-e^{-2\pi iz}q_t^n).
\tag{949.8}
$$
Then
$$
\theta_z(0;t)=2\pi i\eta(t)^3,
\qquad 4\pi i\theta_t=\theta_{zz}.
\tag{949.9}
$$
Define the entire function in $z$
$$
J(z,t)=\frac{\theta(z;t)\theta(\zeta z;t)
                         \theta(\zeta^2z;t)}{\eta(t)}.
\tag{949.10}
$$
The $A_2$ Macdonald identity, in the precise convention of Wagner, Proposition 4.9, is
$$
\begin{aligned}
&\sum_{n_1\equiv n_2\ (2)}
\left(\frac{2n_1}{3}\right)
e^{2\pi i(n_1z_1+3n_2z_2)/6}
q_t^{(n_1^2+3n_2^2)/12}\\
&\hspace{12mm}=
\frac{\theta((z_1+3z_2)/6;t)
      \theta((z_1-3z_2)/6;t)\theta(z_1/3;t)}{\eta(t)}.
\end{aligned}
\tag{949.11}
$$
Take $z_1=3z$, $z_2=sz$. The three theta arguments are
$\rho z,-\zeta z,z$. Since $\rho=-\zeta^2$ and theta is odd, the two minus signs cancel. Consequently
$$
J(z,t)=\sum_{\alpha\in\mathbf Z[\zeta]}
          \epsilon_3(\alpha)e^{2\pi i\alpha z}Q^{N\alpha}.
\tag{949.12}
$$
This substitution fixes the positive embedding in (949.3) explicitly. Each ideal prime to $(s)$ has six generators, and for $d\equiv3\pmod6$ the quantity $\epsilon_3(\alpha)\alpha^d$ is independent of its generator. Moreover $J(\zeta z,t)=J(z,t)$ and $J(-z,t)=-J(z,t)$. Taylor expansion of the complete sum therefore gives
$$
J(z,t)=6\sum_{i\ge0}F_{6i+4}(Q)
                     \frac{(2\pi iz)^{6i+3}}{(6i+3)!}.
\tag{949.13}
$$
There are no other powers of $z$. In particular the complete generating function for the actual oldforms, with their original phase, is
$$
\boxed{
\mathcal V(z,t):=J(z,t)-2\zeta^2J(2z,4t)
=6\sum_{i\ge0}V_{6i+4}^\dagger(2t)
                     \frac{(2\pi iz)^{6i+3}}{(6i+3)!}.
}
\tag{949.14}
$$
The coefficient of the second oldform is exactly $2\cdot2^{6i+3}=2^{6i+4}$. It has not been inferred from a few weights.

## 3. Differentiating the original oldform at its actual mark

Let $g=T^2S$ act by $g(u)=2-1/u$. The theta transformation law gives
$$
J(z/u,-1/u)=uJ(z,u),\qquad
J(z,u+2)=\zeta^2J(z,u).
\tag{949.15}
$$
For the first identity the three Gaussian exponents cancel because
$1+\zeta^2+\zeta^4=0$. The remaining multiplier can also be read from the leading term
$J(z,u)=(2\pi i)^3\eta(u)^8z^3+O(z^9)$ and
$\eta(-1/u)^8=u^4\eta(u)^8$. For the second identity,
$\theta(z,u+2)=i\theta(z,u)$ and
$\eta(u+2)=e^{\pi i/6}\eta(u)$ give precisely $\zeta^2$.

Thus
$$
J(z/u,g(u))=\zeta^2uJ(z,u).
\tag{949.16}
$$
Put
$$
t_0=\rho/2,\qquad u(t)=\frac1{2-4t}.
$$
Then $g(u(t))=4t$, $u(t_0)=t_0$, $u'(t_0)=\zeta$, and
$$
\mathcal V(z,t)=J(z,t)-2\zeta u(t)J(2u(t)z,u(t)).
\tag{949.17}
$$
For every $t$, the product definition gives $J(\rho z,t)=-J(z,t)$. Equation (949.17) now shows
$\mathcal V(z,t_0)=0$ identically in $z$. Differentiating this exact identity in the $t$ direction, before specializing, gives
$$
\boxed{
\mathcal V_t(z,t_0)
=(1-\zeta)J_t(z,t_0)
  +2\zeta^2\bigl(J(z,t_0)+zJ_z(z,t_0)\bigr).
}
\tag{949.18}
$$
For example the coefficient of $J_t$ is
$1+2\zeta t_0\zeta=1-\zeta$, and both coefficients of $J$ and $zJ_z$ are $2\zeta^2$. These factors use the original oldform phase from (949.14).

## 4. The specified degree-two lattice quotient

For the rest of the analytic calculation write
$$
\Lambda=\mathbf Z+\rho\mathbf Z=\mathbf Z[\zeta],
\qquad \Lambda_1=\mathbf Z+t_0\mathbf Z
                 =\Lambda+\mathbf Z Q_2,
\qquad Q_2=\rho/2.
\tag{949.19}
$$
Thus the direction is the degree-two quotient
$\mathbf C/\Lambda\longrightarrow\mathbf C/\Lambda_1$, preserving $dz$.
On the first lattice put
$$
x=\wp_\Lambda(z),\quad y=\wp_\Lambda'(z)/2,
\quad Z=\zeta_\Lambda(z),\quad \sigma=\sigma_\Lambda(z),
\quad e=x(Q_2).
$$
Since $Q_2$ is nonzero two-torsion and $g_2(\Lambda)=0$,
$$
e\ne0,\qquad y^2=x^3-e^3,\qquad x'=2y,\quad y'=3x^2.
\tag{949.20}
$$
Write $x_1,Z_1$ for the Weierstrass functions of $\Lambda_1$.
The lattice addition formulas and their Laurent normalizations give
$$
\boxed{
x_1(z)=x(z)+\frac{3e^2}{x(z)-e},\qquad
Z_1(z)=2Z(z)+\frac{y(z)}{x(z)-e}+ez.
}
\tag{949.21}
$$
Indeed $x_1=x+x(z+Q_2)-e$ and
$x(z+Q_2)=e+3e^2/(x-e)$. Integration gives the second formula; its $ez$ term is forced by the absence of a linear term in the normalized zeta Laurent expansion.

The CM relation and Legendre relation give the quasiperiod
$\eta_\Lambda(1)=2\pi/\sqrt3$. From (949.21), for $\lambda\in\Lambda$,
$$
\eta_{\Lambda_1}(\lambda)=2\eta_\Lambda(\lambda)+e\lambda.
$$
In particular, writing $a=\eta_{\Lambda_1}(1)$,
$$
a=\frac{4\pi}{\sqrt3}+e.
\tag{949.22}
$$
The algebraic value $e$ itself is not assigned a new real or cubic-root phase; it is the value at the specified $Q_2$ and will cancel from the final coefficient ratio.

## 5. The Jacobi product is the original degree-six sigma section

The theta–sigma relation in convention (949.8) is
$$
\theta(v;t_0)=\theta_z(0;t_0)
                   e^{-av^2/2}\sigma_{\Lambda_1}(v).
\tag{949.23}
$$
The Gaussian factors cancel in the threefold product. Furthermore
$$
\prod_{j=0}^2\sigma_{\Lambda_1}(\zeta^jz)
=-y(z)\sigma_\Lambda(z)^6.
\tag{949.24}
$$
For a direct proof retaining its sign, differentiate the logarithm of the left side. Apply (949.21),
$Z(\zeta^jz)=\zeta^{-j}Z(z)$, $x(\zeta^jz)=\zeta^jx(z)$,
$y(\zeta^jz)=y(z)$, and
$$
\sum_{j=0}^2\frac{\zeta^j}{\zeta^jx-e}
=\frac{3x^2}{x^3-e^3}.
\tag{949.25}
$$
The resulting logarithmic derivative is $6Z+3x^2/y$, the logarithmic derivative of $y\sigma^6$. The leading term of the product is $z^3$, whereas $y\sigma^6=-z^3+O(z^9)$. This proves (949.24) locally and hence identically by analytic continuation.

Consequently
$$
\boxed{
J(z,t_0)=K\,y(z)\sigma(z)^6,
\qquad K=-\frac{\theta_z(0;t_0)^3}{\eta(t_0)}
        =-(2\pi i)^3\eta(t_0)^8\ne0.
}
\tag{949.26}
$$
In particular, with $\mathcal L=J_z(z,t_0)/J(z,t_0)$,
$$
\mathcal L=6Z+3x^2/y.
\tag{949.27}
$$
Equations (949.21), (949.23), and (949.24) use the sigma function with its original zero quadratic exponential parameter. No independent $e^{cz^2}$ factor has been introduced.

## 6. The heat equation and its exact cancellation

The logarithmic theta derivative from (949.23) is
$\theta_z/\theta=Z_1(v)-av$. Also
$4\pi i\eta_t(t_0)/\eta(t_0)=-a$, since
$\eta_t/\eta=\pi iE_2/12$ and $a=\pi^2E_2(t_0)/3$.
Using the heat equation (949.9) in (949.10) therefore gives
$$
4\pi i\frac{J_t}{J}(z,t_0)
=\sum_{j=0}^2Z_1(\zeta^jz)^2
 -\sum_{j=0}^2x_1(\zeta^jz)
 -2a(1+z\mathcal L).
\tag{949.28}
$$
The constant $-2a$ includes the eta derivative; dropping it would change the answer. Since
$\zeta^2/(1-\zeta)=1/s$ and $8\pi i/s=8\pi/\sqrt3$,
equations (949.18), (949.22), and (949.28) yield
$$
\mathcal V_t(z,t_0)=\frac{1-\zeta}{4\pi i}J(z,t_0)
\left\{\sum_jZ_1(\zeta^jz)^2-\sum_jx_1(\zeta^jz)
                         -2e(1+z\mathcal L)\right\}.
\tag{949.29}
$$
The nonalgebraic quasiperiod term $4\pi/\sqrt3$ has canceled exactly against the derivative of the original oldform transport.

Here is the remaining rational-function calculation in full. Put
$q_j=y/(\zeta^jx-e)$. Differentiating or dividing
$\prod_j(\zeta^jx-e)=x^3-e^3=y^2$ gives
$$
\sum_j\zeta^jq_j=\frac{3x^2}{y},\qquad
\sum_j\zeta^{-j}q_j=\frac{3ex}{y},\qquad
\sum_jq_j^2=\frac{3e(2x^3+e^3)}{y^2},
$$
$$
\sum_jx_1(\zeta^jz)=\frac{9e^4}{y^2}.
\tag{949.30}
$$
By (949.21),
$$
Z_1(\zeta^jz)=2\zeta^{-j}Z+q_j+e\zeta^jz.
$$
Thus the expression in braces in (949.29) is
$$
\begin{aligned}
&\frac{3e(2x^3+e^3)-9e^4}{y^2}
 +\frac{12exZ}{y}+12eZz+\frac{6ex^2z}{y}
 -2e(1+z\mathcal L)\\
&\hspace{20mm}=4e+\frac{12exZ}{y},
\end{aligned}
\tag{949.31}
$$
where (949.20) and (949.27) give the last equality.
Finally set $F_\Lambda=x\sigma^6$. Its derivative is
$F_\Lambda'=2(y+3xZ)\sigma^6$. Substituting (949.26) into (949.29) proves the complete generating identity
$$
\boxed{
\mathcal V_t(z,t_0)
=\frac{(1-\zeta)eK}{2\pi i}\,F_\Lambda'(z).
}
\tag{949.32}
$$
Its scalar is nonzero. In particular the coefficient of $z^3$ proves directly that $\partial_tV_4^\dagger(2t)|_{t=t_0}\ne0$. Together with (949.14) and (949.17), this proves all the vanishing and regular-quotient assertions used in (949.6), without assuming any $f_i$ is nonzero.

## 7. Coefficient comparison and the period normalization

Scaling the original lattice $\Lambda_0=\Omega\Lambda$ gives
$$
F_\Lambda(z)=\Omega^{-4}F_0(\Omega z)
           =z^4\sum_{i\ge0}f_i\Omega^{6i}z^{6i}.
\tag{949.33}
$$
For $k=6i+4$, compare the coefficient of $z^{k-1}$ in (949.14) and (949.32), then divide by the coefficient for $k=4$. The common nonzero scalar, including the specified $e$, cancels. Since $V_4^\dagger$ has a simple zero, the quotient value is its derivative quotient, and the result is
$$
\left[\frac{V_k^\dagger}{V_4^\dagger}\right]_{\rm mark}
=\frac{\partial_t V_k^\dagger(2t_0)}
       {\partial_t V_4^\dagger(2t_0)}
=\frac{k!}{24}f_i\left(\frac{\Omega}{2\pi i}\right)^{6i}.
\tag{949.34}
$$
The derivative notation here means differentiating $t\mapsto V_k^\dagger(2t)$ and then evaluating at $t_0$; the factor two is the same in numerator and denominator.

For the lattice $\mathbf Z+\rho\mathbf Z$, the standard invariant with the equation $y^2=x^3-g_3/4$ is
$$
g_3(\Lambda)=140\sum_{0\ne\lambda\in\Lambda}\lambda^{-6}
           =280\zeta_{\mathrm R}(6)E_6(\rho)
           =\frac{8\pi^6}{27}E_6(\rho).
\tag{949.35}
$$
On $E_0$ the invariant is $g_3(\Lambda_0)=4$. Hence
$$
g_3(\Lambda)=4\Omega^6,\qquad
\Omega^6=\frac{2\pi^6}{27}E_6(\rho),\qquad
\frac{(\Omega/(2\pi i))^6}{E_6(\rho)}=-\frac1{864}.
\tag{949.36}
$$
This is the source of the sign and the factor $864$; $i^6=-1$ is retained. Division of (949.34) by $E_6(\rho)^i$ proves the first identity of (949.7).

By R697(697.2), for this same original sigma function,
$$
A_{6i+5}=2^{-(6i+4)/2}(6i+4)!f_i.
\tag{949.37}
$$
Combining (949.37) with the first identity of (949.7) gives
$A_{6i+5}=6(-108)^i\mathcal C_{6i+4}^{\rm mark}$, including the sign. This completes the proof for every $i\ge0$.

The previously registered $\mathcal C_4^{\rm mark}=1$ and
$\mathcal C_{10}^{\rm mark}=-20$ from R918/R920 are consistent with R697's $A_5=6$ and $A_{11}=12960$. These old calibrations are not inputs to the all-weight argument and have not been recomputed.

## 8. Reduction and the precise remaining boundary

For every fixed $i\ge0$, R697 and (949.7) prove
$$
A_{6i+5},\ \mathcal C_{6i+4}^{\rm mark}\in\mathbf Z[1/6].
$$
Thus at any $p>3$ their reductions vanish simultaneously, because $6(-108)^i$ is a unit. The marked quotient in (949.6) also has the usual integral geometric interpretation: on the fine level-six model the stabilizer character forces every weight $6i+4$ cusp form in this original direction to vanish along the marked $j=0$ section; $V_4^\dagger/E_4$ and $E_6$ are units there, as in R918(918.22). This gives its regular integral value rather than a quotient of two zero residues.

When
$$
6i+4<p,
\tag{949.38}
$$
the factorial in (949.37) is also a unit. Consequently
$$
\boxed{
f_i=0\pmod p
\quad\Longleftrightarrow\quad
\mathcal C_{6i+4}^{\rm mark}=0\pmod p
\qquad(6i+4<p).
}
\tag{949.39}
$$
The first-$p$ coefficient range and integral reduction of $f_i$ are exactly the range used in R891. For $6i+4\ge p$, (949.7) remains an exact rational identity, but this unit-equivalence with the unnormalized $f_i$ is not asserted.

This identifies one complete original sigma subsequence with actual marked CM quotients in increasing weights. It does not prove those quotients are units, identify each increasing-weight space with the actual primitive cotangent image, or supply a value for the original integer $a_h$. It also does not identify the complementary sequence $g_j$ with this same CM family. The second sequence and every same-label source comparison retain their own indices, phase, and factorial boundaries.

## Sources and proof provenance

- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md), (697.1–4), (697.11–15): original $c=0$ sigma sections, signed arithmetic square roots, and integrality away from six.
- [R913](R913-original-Igusa-Cartier-functional-and-two-CM-companions.md), §§5–6: the normalized positive CM series and the full original $2^k\zeta^2$ oldform direction.
- [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md), (918.22), and [R920](R920-original-upper-primitive-Igusa-layer-and-inert-Hecke-row.md): the actual marked branch, the simple zero of $V_4^\dagger$, and the already registered weight-ten calibration.
- Ian Wagner, *Jacobi forms with CM and applications*, [arXiv:2208.01807](https://arxiv.org/abs/2208.01807), §4.1 theta convention and Proposition 4.9, printed p. 14; published in *Journal of Number Theory* **246** (2023), 15–48, [doi:10.1016/j.jnt.2022.11.014](https://doi.org/10.1016/j.jnt.2022.11.014). Only the established $A_2$ product identity is used; its positive-embedding specialization, the original oldform derivative, the two-isogeny calculation, and all period constants are derived above.

No script was executed to obtain the identities in this result. The theorem is a characteristic-zero generating-function identity, followed by the explicitly delimited integral reduction in §8. The main Serre-uniformity problem remains open.
