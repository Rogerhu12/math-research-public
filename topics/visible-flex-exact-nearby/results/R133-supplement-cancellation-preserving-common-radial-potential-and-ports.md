# R133 supplement: cancellation-preserving potential and ports for the common radial reference

2026-11-15, visible-exact / phase_inverse.

**Proved exact identities on the previously stated common domain.**
The common radial reference can be evaluated without separately enclosing
two occurrences of the same logarithmic derivative of $\eta$.
This is a formula for the same reference, potential and two physical source
ports. It does not give a new numerical potential bound, extend a radial
domain, replace the actual nonradial principal phase, or establish a
high-frequency inverse.

Use (C.1)--(C.18) of
[the common radial Langer reference](R133-supplement-common-radial-Langer-reference-and-complete-source-ports.md).
All derivatives in this note are ordinary physical $r$ derivatives.
The Fourier frequency is $n=4|j|$, $z=j^{-2}$, and $\epsilon=\operatorname{sgn}j$.
The complete finite Fourier degree is $M\le96$; both signs and the
complete physical even mean are retained.

## 1. One exact cancellation before taking intervals

Write
$$
 a=\eta+z\alpha,\qquad
 \zeta={z\alpha\over\eta},\qquad
 D=E-B,\qquad
 \ell={\kappa_r\over\kappa}.
 \tag{P.1}
$$
These are the exact quantities in (C.1), with the same bilinear complex
family coefficients. In particular the factors $1-\ell_0^2z$ in those
finite sums, for Fourier summation index $\ell_0$, have not been expanded
or dropped.

The common radial coordinate obeys
$$
 \kappa=\eta\sqrt{k}\,\bar A^{-1/3}.
$$
On any domain where the original reciprocal and branch gaps hold,
$$
 \ell={\eta_r\over\eta}+{k_r\over2k}
                       -{\bar A_r\over3\bar A},
 \qquad
 {a_r\over a}={\eta_r\over\eta}+{\zeta_r\over1+\zeta},
 \qquad
 q=D+{\eta_r\over\eta}+{\zeta_r\over1+\zeta}.
 \tag{P.2}
$$
Consequently the root-port coefficient $c=(\ell-q)/2$ is exactly
$$
 \boxed{\displaystyle
 c={k_r\over4k}-{\bar A_r\over6\bar A}
           -{D\over2}-{\zeta_r\over2(1+\zeta)}.}
 \tag{P.3}
$$
The repeated $\eta_r/\eta$ cancels algebraically before any modulus or
interval upper bound is taken. The complete dependence of $D$ and
$\zeta$ on $\eta$, the repaired mean and the other Fourier coefficients
is still present.

For example, at $z=0$ this becomes
$$
 c_\infty={k_r\over4k}-{\bar A_r\over6\bar A}
                  -{\langle e\rangle-\langle B_{\rm coef}\rangle\over2}.
 \tag{P.4}
$$
The finite $b=\beta$ contribution and the quadratic nonradial means in
the last term remain. They have not been declared a removable gauge
error.

## 2. The same complete potential

The common-coordinate potential of (C.11) satisfies
$$
 \boxed{\displaystyle
 \mathcal V(z,T(r))
 ={ -c_r+\tfrac12c(\ell+q)
       -16K\{2\eta\alpha+z\alpha^2\}\over\kappa^2}.}
 \tag{P.5}
$$
Indeed
$$
 {\kappa_{rr}\over\kappa}=\ell_r+\ell^2
$$
and hence
$$
 {q_r\over2}-{q^2\over4}
 +{3\kappa_r^2\over4\kappa^2}
 -{\kappa_{rr}\over2\kappa}
 ={q_r-\ell_r\over2}+{\ell^2-q^2\over4}
 =-c_r+\frac12c(\ell+q).
 \tag{P.6}
$$
Division by the same $\kappa^2$ and the exact removable-frequency
identity (C.3) give (P.5). No division by $K$, $\rho$ or $z$ is introduced.

The full physical derivative required in (P.5) is
$$
 \begin{split}
 c_r={}&{1\over4}\left({k_{rr}\over k}-{k_r^2\over k^2}\right)
 -{1\over6}\left({\bar A_{rr}\over\bar A}
                        -{\bar A_r^2\over\bar A^2}\right)
 -{D_r\over2}\\
 &-{1\over2}\left({\zeta_{rr}\over1+\zeta}
                       -{\zeta_r^2\over(1+\zeta)^2}\right).
 \end{split}
 \tag{P.7}
$$
For a fixed $z$,
$$
 \begin{split}
 \zeta_r&=z\left({\alpha_r\over\eta}
                          -{\alpha\eta_r\over\eta^2}\right),\\
 \zeta_{rr}&=z\left(
 {\alpha_{rr}\over\eta}
 -{2\alpha_r\eta_r+\alpha\eta_{rr}\over\eta^2}
 +{2\alpha\eta_r^2\over\eta^3}\right).
 \end{split}
 \tag{P.8}
$$
Thus the cancellation-preserving formula needs no radial order beyond
two for $\alpha,\eta,k,\bar A$ and one for $D$. It uses the same
already described finite rational-frequency sums, full physical
cubics, and intrinsic jets. A new consumer must actually bound every
displayed reciprocal on its declared common domain.

The identity is also valid for the complete complex parameter family.
Reality is needed only when invoking a positive real measure or a real
radial energy argument; it is not used to replace the bilinear sums by
conjugate products.

## 3. The gauge and both physical source rows

The same normalized gauge from (C.7) obeys
$$
 {G_r\over G}={E+B+a_r/a-\ell\over2}=B-c,
 \qquad G(z,r_*)=1.
 \tag{P.9}
$$
It can therefore be enclosed equivalently from
$$
 G(z,r)=\exp\left(\int_{r_*}^r[B(z,t)-c(z,t)]\,dt\right)
 \tag{P.10}
$$
on a common simply connected branch domain. Across an actual physical
seam this identity is applied piecewise with its true nonzero entry
value. It does not reset $G$ to one at each seam.

The original full two-state map remains
$$
 U={h_2\over G},\qquad
 P={A_jh_1+ch_2\over\kappa G},\qquad
 A_j=i\epsilon n a,
$$
and the ordinary sources remain exactly
$$
 U_T=P+{g_2\over\kappa G},\qquad
 P_T=(n^2T-\mathcal V)U+
                 {A_jg_1+cg_2\over\kappa^2G}.
 \tag{P.11}
$$
In particular the new expression for $c$ is not permission to remove
the $g_2$ column or its contribution to the second row. There is no
radial derivative of $g_2$. The frequency factor in $A_j$ is still
present and must be paid in the actual source/trace windows.

At the root the mixed physical trace is still transformed by
$$
 \begin{pmatrix}U\\n^{-2/3}P\end{pmatrix}_{r_*}
 =
 \begin{pmatrix}
 0&1\\
 i\epsilon a(z,r_*)/\kappa_*&
                n^{-2/3}c(z,r_*)/\kappa_*
 \end{pmatrix}
 \begin{pmatrix}n^{1/3}h_1\\h_2\end{pmatrix}_{r_*}.
 \tag{P.12}
$$
The independent ordinary even mean is the original $j=0$ equation.
It is not obtained by letting $j=0$ in this nonzero-mode elimination.

## 4. Consequences for a numerical consumer

A new potential consumer may use (P.3), (P.5), (P.7) and (P.8) to
avoid unnecessary interval loss from duplicated logarithmic
derivatives. The displayed identities do not identify different
occurrences of a varying function after separate norm upper bounds
have already been taken. The complete signed products must be formed
first, or a separately proved majorant must enclose their full
difference.

The numerical domain must supply nonzero gaps for $\eta,k,\bar A,a$
and $\kappa$, together with the finite rational-frequency denominators.
The bound $|z|\le97^{-2}$ concerns the declared finite-background
reference; it is not a bound for an unknown infinite-Fourier correction.
Any old complex rectangle, original cubic piece and true-root
uncertainty must be retained explicitly.

The same physical radial order is preserved in the full nonradial
coupling of (C.18). The first-order drift is not reduced to order zero
by (P.3). The old-circle primitive, projected inverse, both signed
branches, independent mean, true seam maps and all source ports remain
in that full equation.

A small displacement of the canonical chart does not supply a
same-order operator norm for its full composition map. Likewise a new
selected radial fundamental matrix cannot reuse the old free-Airy
source bounds without an explicit transfer. These identities prepare a
stable evaluation of the same radial reference; numerical potential,
propagation and strong-return gates remain to be paid.
