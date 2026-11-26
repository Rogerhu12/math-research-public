# R149 supplement: complete Theta row regularity and the same density inverse on the negative window

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved analytic conclusions.** The original same-sign density inverse has
a quantitative regularity bootstrap using only the first three derivatives
of its true inverse lift. This gives both a complete `Theta` row error after
the original one-derivative-loss reference inverse, and a same-operator
bound for `C^{-1}` on the original `H^{-4/3}` source window. Neither result
requires a smallness or finite-section invertibility assumption.

The constants below use the actual inverse lift and the same selected
member of [DC](R149-supplement-same-sign-density-compression-and-finite-Theta-rows.md).
The first public inverse-lift output will supply its new approximation
error and third derivative bound. This note proves the complete formulas;
it does not invent those numerical outputs or assert a finite Schur gate.

## DB1. The fixed maps, complete norms and true derivative inputs

Keep DC's complete nonmean carrier, normalized measure on the circle of
length `pi/2`, and physical frequencies `4j`. Write

\[
 N=|D_\phi|,\quad G=N^{-1},\quad
 \mathscr H=\dot H^{-1/2}_0,\qquad
 \|f\|_{\dot H^s}^2=\sum_{j\ne0}(4|j|)^{2s}|\widehat f_j|^2.
 \tag{DB.1}
\]

Use exactly

\[
 S=U_\psi,\quad p=\psi^{-1},\quad U_pf=p'(f\circ p),\qquad
 C=\tfrac12(S-ZSZ),\quad D=\tfrac12(S+ZSZ),
 \tag{DB.2}
\]

where `Z=i Pi_+ - i Pi_-`. The dagger denotes the `mathscr H` adjoint.
DC proves the genuine onto inverses and the exact identities

\[
 \|C^{-1}\|_{\mathscr H}\le1,\quad
 \|(C^\dagger)^{-1}\|_{\mathscr H}\le1,\qquad
 S^{-1}=C^\dagger-D^\dagger.
 \tag{DB.3}
\]

In particular `-D^dagger` is the **opposite-sign** block of `U_p`.
The input-mean column is not included in that statement: the original two
physical means and all auxiliary-mean ranks remain separate, as in WIT/DC.

Suppose complete real-axis bounds for this actual lift have been proved:

\[
 p'\ge m>0,\qquad |p''|\le b_2,\qquad |p'''|\le b_3,
 \qquad m_0=\min(m,1).
 \tag{DB.4}
\]

The already proved DC.21--22 allow `m=465/512` and `b_2=6`. To obtain
`b_3` from the new explicit entire compound `p_hat=K_48 circ A_-^0`, let
`h_3` bound its **whole** third derivative on the real axis and let
`E_p` bound `p-p_hat` on the whole physical strip of width `sigma=1/256`.
Cauchy's derivative formula on disks centered on the real axis gives

\[
 b_3=h_3+6E_p\sigma^{-3}.
 \tag{DB.5}
\]

One may use smaller radii and then take their increasing limit if the
strip is stated open. The difference is periodic even though the two
degree-one lifts are not; its full constant and the same fixed lifts are
retained. The `E_p` in (DB.5) is the complete DC.20 quantity, including
transport, root sliver, actual implicit parameter and true conjugacy fees.
It is not a sampled error or an old norm inferred from a subtotal.

## DB2. Two integrations by parts pay the entire opposite-sign operator

For positive integers `j,n`, let

\[
 c_{-j,n}=\frac1\ell\int_0^\ell
                 e^{i4(np(x)+jx)}\,dx,\qquad \ell=\pi/2.
\]

Periodicity of the exponential and the actual degree-one lift give the
exact density coefficient

\[
 (U_p)_{-j,n}=-\frac jn c_{-j,n}.
 \tag{DB.6}
\]

Indeed the integral of the derivative of the exponential is zero.
Set `t=4(np+jx)`. Its derivative is at least `4(nm+j)`. Two ordinary
integrations by parts, with no endpoint terms, give

\[
 c_{-j,n}=\frac1\ell\int_0^\ell e^{it(x)}
 \left(\frac{t'''(x)}{t'(x)^3}
                 -\frac{3t''(x)^2}{t'(x)^4}\right)dx .
 \tag{DB.7}
\]

Consequently

\[
 |(U_p)_{-j,n}|
 \le\frac j{16}\left(
      \frac{b_3}{(nm+j)^3}
       +\frac{3n b_2^2}{(nm+j)^4}\right)
 \le B\frac j{(n+j)^3},
 \qquad
 B=\frac1{16}\left(\frac{b_3}{m_0^3}
                          +\frac{3b_2^2}{m_0^4}\right).
 \tag{DB.8}
\]

The other sign block has the same bound by the reality of the lift.
This estimates every pair `n,j>=1`; there is no Fourier cutoff and no
unpaid alias or asymptotic remainder.

An orthonormal input vector for `mathscr H` is `sqrt(4n) e^{i4nx}`.
Thus the full weighted Hilbert--Schmidt sum gives

\[
 \begin{aligned}
 \|D^\dagger:\mathscr H\to L^2_0\|^2
 &\le8B^2\sum_{n,j\ge1}\frac{nj^2}{(n+j)^6}\\
 &=\frac23B^2\sum_{s\ge2}(s^{-2}-s^{-4})
 <\frac49B^2.
 \end{aligned}
 \tag{DB.9}
\]

Here `sum_{n=1}^{s-1} n(s-n)^2=s^2(s^2-1)/12`, and a completely
elementary rational comparison is

\[
 \sum_{s\ge2}s^{-2}
 <\frac14+\frac19+\frac1{16}+\frac1{25}+\int_5^\infty x^{-2}\,dx
 =\frac{2389}{3600}<\frac23.
\]

The same two integrations already suffice for the fractional positive
window needed by the original negative source scale:

\[
 \begin{aligned}
 \|D^\dagger:\mathscr H\to\dot H^{1/3}_0\|^2
 &\le8\,4^{2/3}B^2
           \sum_{n,j\ge1}\frac{n j^{8/3}}{(n+j)^6}\\
 &\le\frac23\,4^{2/3}B^2\sum_{s\ge2}s^{-4/3}
 <2\,4^{2/3}B^2<\frac{81}{16}B^2.
 \end{aligned}
 \tag{DB.10}
\]

The second line uses `j^{2/3}<=s^{2/3}` and the same exact finite sum.
The strict series bound is `sum_{s>=2}s^{-4/3}<integral_1^infinity
x^{-4/3} dx=3`. The last rational comparison follows from
`81^3>16*32^3`. These are operator bounds on the complete nonmean space.
Define the convenient whole constants

\[
 L_0=2B/3,\qquad L_{1/3}=9B/4.
 \tag{DB.11}
\]

The displayed strict series comparisons are understood for `B>0`.
If `B=0`, (DB.8) makes the whole opposite-sign operator zero, and all
subsequent non-strict norm bounds remain valid with `L_0=L_{1/3}=0`.

## DB3. Bootstrap the existing inverse rather than assuming regularity

The actual inverse density map `S=U_{p^{-1}}` obeys

\[
 S_0=m^{-1/2}\ge\|S:L^2_0\to L^2_0\|.
 \tag{DB.12}
\]

This follows directly by changing variables in its full squared norm.
For its first homogeneous derivative, put `psi=p^{-1}` and differentiate
the actual density expression:

\[
 (U_\psi f)'=\psi''(f\circ\psi)+\psi'^2(f'\circ\psi).
\]

Since `psi'=1/(p' circ psi)` and `psi''=-p'' circ psi/(p' circ psi)^3`,
the two complete `L^2` terms are bounded by
`b_2 m^{-5/2} ||f||_2` and `m^{-3/2} ||f'||_2`.
The input is nonmean, so the physical Poincare constant is `1/4`.
Therefore

\[
 S_1=m^{-3/2}+\frac{b_2}{4m^{5/2}}
      \ge\|S:\dot H^1_0\to\dot H^1_0\|,
 \qquad
 S_{1/3}=S_0^{2/3}S_1^{1/3}
      \ge\|S:\dot H^{1/3}_0\to\dot H^{1/3}_0\|.
 \tag{DB.13}
\]

The final inequality is constant-one interpolation on the same
nonmean Fourier Hilbert scale, for the same compatible density operator.

Let `T=(C^dagger)^{-1}` be the already constructed inverse on `mathscr H`.
For `h` in either `L^2_0` or `dot H^{1/3}_0`, solve `z=Th` first in
`mathscr H`. By (DB.3),

\[
 \|z\|_{\mathscr H}\le\|h\|_{\mathscr H},\qquad
 z=S(h-D^\dagger z).
 \tag{DB.14}
\]

The right-hand side lies in the stated stronger space by (DB.9)--(DB.13).
This proves regularity of the genuine solution and justifies the stronger
norm; it does not assume that a formal derivative is already square
integrable. On the two windows the resulting complete bounds are

\[
 \boxed{\begin{aligned}
 \|T:L^2_0\to L^2_0\|
 &\le K_{T,0}:=S_0(1+L_0/2),\\
 \|T:\dot H^{1/3}_0\to\dot H^{1/3}_0\|
 &\le K_{T,1/3}:=S_{1/3}(1+4^{-5/6}L_{1/3}).
 \end{aligned}}
 \tag{DB.15}
\]

The embeddings used here are respectively
`||h||_H<=||h||_2/2` and `||h||_H<=4^{-5/6}||h||_{dot H^{1/3}}`.
No condition such as `B<1`, a near-identity test, or a Galerkin determinant
appears in this argument.

## DB4. The same inverse on the original negative window

The Hilbert and ordinary adjoints have the exact relation

\[
 C^\dagger=N C^*N^{-1},\qquad
 C^{-1}=N T^*N^{-1}.
 \tag{DB.16}
\]

These identities hold on a common smooth distribution core. Duality and
the derivative shifts give the complete, **same-operator** bounds

\[
 \boxed{\quad
 \|C^{-1}:\dot H^{-1}_0\to\dot H^{-1}_0\|\le K_{T,0},\qquad
 \|C^{-1}:\dot H^{-4/3}_0\to\dot H^{-4/3}_0\|\le K_{T,1/3}.
 \quad}
 \tag{DB.17}
\]

They agree with DC/WIT's existing inverse on overlaps. The original
negative-window inverse is not replaced by an inverse of a different
operator or by an inverse available only on a more regular domain.
Since the smallest nonzero frequency is four, a valid bound in the
original inhomogeneous Bessel convention is

\[
 \boxed{\quad
 K_{C,-4/3}=(17/16)^{2/3}K_{T,1/3}
 \ge\|C^{-1}:H^{-4/3}_0\to H^{-4/3}_0\|.
 \quad}
 \tag{DB.18}
\]

Only one comparison factor is required: the output Bessel norm is no
larger than the homogeneous negative norm, and the reverse input
comparison costs `(17/16)^{2/3}`. This keeps the original `H^{-4/3}`
gain when a complete ordered high-frequency product uses it. For example
`S P_97 S^{-1} W^{-1} A = S P_97 C^{-1} A` exactly; this identity
does not commute `P_97` through `C^{-1}`, turn it into a transported
projection, delete a mean rank, or by itself certify the coupled high gate.

## DB5. Full H1 dual rows pay Theta's one derivative of loss

Keep DC.9--11 exactly:

\[
 A=Id-\mathcal T_\alpha I,\quad
 A^*=Id+I\mathcal T_\alpha,\quad
 b_j=ND_+e_j,\quad z_j=Tb_j,\quad r_j=A^*Gz_j,
 \qquad \Theta=V_Q\overline G.
 \tag{DB.19}
\]

Here `mathcal T_alpha=P alpha P` is the original real self-adjoint
Toeplitz compression, with its whole `A_0>=||alpha||_infinity` bound.
Set `K_A=1+A_0/4`. The original `D_+`, normalized real reflected basis,
and true physical frequency four are unchanged.

For finite explicit trial columns `z_hat_j`, define their **complete**
joint residual operator

\[
 R e_j=C^\dagger\widehat z_j-b_j,\qquad
 \|R:\ell^2_{96}\to L^2_0\|\le\varepsilon_0,\quad
 \|R:\ell^2_{96}\to\mathscr H\|\le\varepsilon_H.
 \tag{DB.20}
\]

Both estimates concern the same full residual, including both signs,
aliases, the entire infinite tail, and the true-map error. From (DB.14),
with `h=Rc`,

\[
 \|TR:\ell^2_{96}\to L^2_0\|
 \le S_0(\varepsilon_0+L_0\varepsilon_H)=:\varepsilon_z.
 \tag{DB.21}
\]

For any `e` in `L^2_0` the actual adjoint order now gives

\[
 N A^*Ge=e-Z\mathcal T_\alpha Ge,
 \qquad \|NA^*Ge\|_2\le K_A\|e\|_2.
 \tag{DB.22}
\]

There is **no angular derivative of alpha** in this formula. Moving `I`
to the other side of `mathcal T_alpha` would destroy this property and
would be a different operator. Since the output is nonmean,

\[
 \|A^*Ge\|_{H^1}\le(\sqrt{17}/4)K_A\|e\|_2.
 \tag{DB.23}
\]

Let `K_G` be a complete already qualified norm of the original
`Gbar:Y_a^0 -> H^{-1}_0`, including its actual low reference and its
high reflected spectral inverse. Define the trial row map by the true
pairings with `r_hat_j=A^*G z_hat_j`; its composition with `Gbar` is
well defined by `H^1`--`H^{-1}` duality. Then

\[
 \boxed{\quad
 \|\Theta-\widehat\Theta:Y_a^0\to\ell^2_{96}\|
 \le K_G\frac{\sqrt{17}}4 K_A S_0
               (\varepsilon_0+L_0\varepsilon_H).
 \quad}
 \tag{DB.24}
\]

This is a whole target-space operator estimate, not a statement restricted
to finite inputs. A Hilbert--Schmidt estimate from all96 complete columns
is valid for each residual norm; a joint Gram/operator estimate can also
be used. There is no additional `sqrt(96)` after either joint estimate.

If the actual trial substitutes a real `alpha_hat` for `alpha`, it must
also pay a full `e_alpha>=||alpha-alpha_hat||_infinity` and the whole
trial norm `Z_G>=||G z_hat:ell^2_96->L^2||`. In the **same** formula
the additional complete row error is at most

\[
 K_G(\sqrt{17}/4)e_\alpha Z_G.
 \tag{DB.25}
\]

Thus a scalar bound for `A` alone still does not determine signed rows.
The actual signed coefficient carrier or a fully paid trial is required.
The two physical means, all true parameter/phase rows and all remaining
finite/large-cutoff equations are not part of this nonmean coordinate
certificate.

For reference, the same proof yields the complete symbolic whole norm

\[
 \|\Theta\|
 \le K_G\frac{\sqrt{17}}4K_A S_0
               (384+L_0\sqrt{384}),
 \tag{DB.26}
\]

because the full joint maps `c -> sum b_j c_j` have `L^2` norm384
and `mathscr H` norm `sqrt(384)`. This is not an entrywise sum of96 rows.

## DB6. The complete L2 residual uses the same Fourier calculation

DC already gives the energy-norm alias, tail and true-model budgets.
The extra norm in (DB.20) can be paid from the **same** signed Fourier
head and analytic primitive, without rerunning a compound evaluation.
If the complete analytic periodic primitive `a` has supremum at most
`M` on strip `sigma`, set `q=exp(-8 sigma)`. For every integer `K>=0`,

\[
 \begin{aligned}
 \|\partial_\phi P_{|k|>K}a\|_2^2
 &\le32M^2\sum_{k>K}k^2q^k\\
 &=32M^2q^{K+1}\left[
 \frac{(K+1)^2}{1-q}
 +\frac{2(K+1)q}{(1-q)^2}
 +\frac{q(1+q)}{(1-q)^3}\right].
 \end{aligned}
 \tag{DB.27}
\]

The physical derivative multiplier and both Fourier signs produce32.
All terms in the last expression are positive, which permits direct
outward evaluation with an upper ratio. At `K=0` the same formula pays
the **whole** true-map model difference from DC.18, with
`M=E_p M_f`. Combine the squared norm of the full signed head, including
all aliases, with its disjoint evaluated tail, take a square root, then
add that complete model error. The exact density mean remains zero by
the primitive derivative identity.

The [pure formulas](../scripts/fourfold_codazzi_density_inverse_regularization_math.py)
implement these new scalar consequences without input/output or numerical
imports. An actual consumer must first admit all complete same-selected
inputs and persist each new result before downstream use. This analytic
proof runs no old ray, KAM, sign norm, inverse, source integral, Fourier
pairing or scientific target.
