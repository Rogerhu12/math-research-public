# R150: equality of the full infinity orders makes the affine divisor monic at 31

Date: 2026-11-15 (UTC)

Author: AI (ChatGPT / literature_audit)

Status: a consequence of the actual full rational and finite-field
infinity order $66$, the original projective Gauss lemma, and the
already computed affine divisor over $\mathbb F_{31}$. No new matrix
computation is used.

## 1. Same original homogeneous minors

Let $D=\mathbb Z_{(31)}$. Use the original integer natural
homogenization of the full $4367\times6188$ matrix, of generic rank
$r=4354$. Its source and output weights, and their compatibility with
the infinity chart $(s,t)=(1,u)$, are those in the
[original projective divisor proof](R150-appendix-full-projective-divisor-degree381-and-residual-multiplier170.md).

Let $M_\alpha(s,t)$ range over all nonzero original $r$-minors.
Their homogeneous degrees need not coincide. Let
$\mathscr D(s,t)\in\mathbb Z[s,t]$ be a primitive representative of
their gcd over $\mathbb Q[s,t]$.

The newly completed [full rational infinity calculation](R150-appendix-infinity-complete-tenth-connection-one-and-full-characteristic-zero-spectrum66.md)
and the already completed [full finite-field calculation](R150-appendix-full-original-infinity-mod31-length66-and-output-projection-gap28.md)
give, on this same natural chart,

$$
\min_\alpha \operatorname{ord}_u M_\alpha(1,u)
=
\min_\alpha \operatorname{ord}_u \overline{M_\alpha}(1,u)
=66.
\tag{1.1}
$$

The second minimum is taken over the nonzero reduced minors. In
particular there is an original minor $M_{\alpha_*}$ for which the
coefficient of $u^{66}$ is a $31$-unit.

This uses the full original matrix. No identification of that minor
with the previously selected order-$243$ square is made.

## 2. A unit leading coefficient for the complete affine gcd

The characteristic-zero equality in (1.1) says exactly that the
$t$-valuation of $\mathscr D$ is $66$. Write

$$
\mathscr D(s,t)=t^{66}G(s,t),\qquad t\nmid G.
\tag{2.1}
$$

Since $\mathscr D$ is primitive and $t^{66}$ is a monomial, $G$ is an
integer homogeneous polynomial with the same content.

The multivariate Gauss lemma gives, for every original minor,

$$
M_\alpha(s,t)=t^{66}G(s,t)H_\alpha(s,t),
\qquad H_\alpha\in\mathbb Z[s,t].
\tag{2.2}
$$

To see the integrality assertion, a primitive integer polynomial
which divides an integer polynomial over $\mathbb Q[s,t]$ also divides
it over $\mathbb Z[s,t]$; no denominator is introduced in the
quotient. This remains true for minors of different total degrees.

Taking the coefficient of $u^{66}$ in (2.2) for $\alpha_*$ gives

$$
[u^{66}]M_{\alpha_*}(1,u)=G(1,0)H_{\alpha_*}(1,0).
\tag{2.3}
$$

The left side is a $31$-unit, and both factors on the right belong to
$D$. Therefore

$$
\boxed{G(1,0)\in D^\times.}
\tag{2.4}
$$

Put $a=G(1,0)$ and define the monic affine gcd by

$$
\Delta(s)=a^{-1}G(s,1).
\tag{2.5}
$$

If $d=\deg G$, then $a$ is exactly the coefficient of $s^d$ in
$G(s,1)$. Thus

$$
\boxed{\Delta\in D[s]\text{ is monic},\qquad
       \deg\overline\Delta=\deg\Delta.}
\tag{2.6}
$$

Dehomogenization gives the complete affine gcd: an affine common
factor homogenizes to a common homogeneous factor, and the only
homogeneous factor lost upon setting $t=1$ is the infinity factor.
Hence (2.5) is not merely a known subfactor of the complete gcd.

Reducing (2.2) gives

$$
\boxed{\overline\Delta\mid \Delta_{31,\mathrm{aff}}.}
\tag{2.7}
$$

The [complete affine finite-field divisor](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)
has degree $315$. Therefore (2.6)--(2.7) give the affine bound
$\deg\Delta\le315$ directly, without a possible loss of degree to
infinity under reduction.

For example, the primitive factor $1-31s$ cannot occur in this
complete characteristic-zero gcd: its homogenization would add an
extra infinity factor after reduction, contradicting (1.1).

## 3. A monic integral residual and its exact reduced envelope

The already proved common factor is

$$
K_{158}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4,
\tag{3.1}
$$

where

$$
\begin{aligned}
F_+&=5s^3-25s^2+32s-8,\\
F_-&=5s^3+135s^2+864s+864,\\
E_8&=5s^8+50s^7+153s^6-936s^5-2888s^4\\
&\qquad+15936s^3-3392s^2-25472s+9600.
\end{aligned}
$$

Its leading coefficient is $5^{16}$, a unit of $D$. Set

$$
\widehat K=5^{-16}K_{158},\qquad
\widehat R=\Delta/\widehat K.
\tag{3.2}
$$

Both $\Delta$ and $\widehat K$ are monic members of $D[s]$.
Polynomial division by the monic $\widehat K$ takes place in $D[s]$;
the remainder is zero over $\mathbb Q$, hence is zero in $D[s]$.
Consequently

$$
\boxed{\widehat R\in D[s]\text{ is monic},\qquad
       \deg\widehat R\le157.}
\tag{3.3}
$$

Use the exact old finite-field notation

$$
\begin{aligned}
P_+&=s^3+26s^2+25s+17,\\
P_-&=s^3+27s^2+24s+24,\\
E_6&=s^6+13s^5+18s^4+2s^3+15s+30,
\end{aligned}
$$

and let $Q=Q_2Q_6Q_7Q_{16}Q_{29}$ be the five explicitly recorded
monic irreducible factors of total degree $60$ in the complete
finite-field divisor proof. The exact reduction is

$$
\overline E_8=5(s-2)(s-1)E_6.
$$

Thus the old complete degree-$315$ formula and (2.7) imply

$$
\boxed{
\overline{\widehat R}\mid
(s-2)^{16}(s-1)^3P_+^2P_-^2E_6Q^2.
}
\tag{3.4}
$$

The right side has degree

$$
16+3+6+6+6+120=157.
$$

Unlike the earlier projective residual envelope, (3.4) has no
remaining infinity factor. It is an envelope after reduction, not
a characteristic-zero factorization. In particular two distinct
rational irreducible factors may still acquire common factors
modulo $31$.

Every factor on the right of (3.4) is nonzero at $s=0$ and
$s=-6$. This follows directly from the displayed factors and the
five exact $Q_d$ coefficient lists in the cited complete finite-field
proof. Hence
$$
\widehat R(0),\ \widehat R(-6)\in D^\times.
\tag{3.5}
$$
Every monic rational factor or quotient of $\widehat R$ is in
$D[s]$ by the argument below. Its values at these two points are
therefore also units, since their products are the units in (3.5).
This does not assert that $\widehat R(2)$ is a $31$ unit; the
already proved nonvanishing at $2$ is over $\mathbb Q$.


## 4. Outside factors and the nine-target multiplier

Let $\Sigma_0=s(s-2)(s+6)F_+F_-E_8$. Choose all rational factors
monic. Every monic rational factor of a monic member of $D[s]$
belongs to $D[s]$: its roots are integral over $D$, so its rational
coefficients are integral over $D$, and $D$ is integrally closed
in $\mathbb Q$.

It follows that the outside part $R_{\mathrm{out}}$ of $\widehat R$
is monic and belongs to $D[s]$. The established exact original
cokernel sequence implies that the outside projection divisor
$\Omega$ divides $R_{\mathrm{out}}$. Therefore, once that divisor
is determined, its monic normalization and

$$
M=R_{\mathrm{out}}/\Omega
$$

also belong to $D[s]$.

The [original PID target comparison](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md)
then provides, with the same original source module,

$$
M h_* t_j\in\operatorname{im}A\subset\mathbb Q[s]^{4367},
\qquad 2\le j\le10,
$$

where

$$
h_*=s^3F_+^2F_-^2E_8,\qquad
t_j=\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2.
$$

For $d=\deg\Omega$, the current bounds are

$$
\deg M\le157-d,\qquad
\deg(Mh_*)\le180-d.
\tag{4.1}
$$

The same original three-branch source estimate is

$$
8526-d,\qquad 8531-d,\qquad 328-d,
$$

and hence the overall bound remains $8531-d$. This paragraph does
not supply the coefficients of $M$ or a value of $d$.

The joint monic target annihilator supported outside $\Sigma_0$,
which divides $M$, is likewise a member of $D[s]$. Coprimality with
$\Sigma_0$ over $\mathbb Q$ is not asserted to survive reduction
modulo $31$.

## 5. Scope

There is also an existence statement for an original maximal minor:
the minor $M_{\alpha_*}$ from (1.1), after dehomogenization, has
a $31$-unit leading coefficient. Its original homogeneous degree
determines its actual affine degree by subtracting $66$.

This does not identify its original row and column sets, does not
give that property to the previously fixed square of finite-field
infinity order $243$, and does not replace the source-cost argument
based on that fixed square. An explicit newly selected original
minor requires the separate original-coordinate unit projection
argument.

No equality $\deg\Delta=315$ has been proved. The residual multiplier
may be nonconstant. Integrality of a parameter multiplier does not
make its original source coefficients $31$-integral and does not
supply a uniform power of $31$ clearing those coefficients.
For a simple illustration of this distinction, the matrix $[31,s]$
over $D[s]$ has monic full gcd $1$ and a unit direction in its natural
infinity chart $[31u,1]$. Yet a source for the target $1$ over
$\mathbb Q[s]$ must have a $31$ denominator, as evaluation at $s=0$
shows. Thus a good infinity lattice does not alone remove a finite
parameter obstruction to integral sources.
The original $h_0$ global-membership problem therefore remains open.

All arguments in this note use already completed original-matrix
results. No additional rank computation, factorization, or
large-array reconstruction was performed.
