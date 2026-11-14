# R736: the original three-norm exchange chain and the exact minus-four moment phase

Date: 2026-11-14. **Status: proved.** This result keeps the
original $p=43$, $q$, $S,T,\Gamma$, $P_0$, $P_+$, $\zeta$,
and positive Frobenius conventions. It connects the marked
$q$-principalization $X_t$ in the pure anti-$p$ field with
a global principalization in the mixed field by exact
ordinary corrections. It does not evaluate $J_\ell$ or $b$.

Use the original level-one fields

$$
B=K(A_0[p^2])^{\mu_{42}},\quad
M=LB,\quad F_t=B^S,\quad N=LF_t=M^S,
$$
$$
S=\langle s=1+p\rangle,\quad
T=\langle t=1+21pi\rangle,\quad
\Gamma=\langle\gamma\rangle,\quad
\pi=\gamma-1.
$$

Let $Q$ be the marked prime of $M$ above the original
$P_0$ of $F_t$, and abbreviate
$\mathfrak q=P_+Q$. Let the original completed witness satisfy

$$
\operatorname{div}_{F_t}X_t=P_+P_0,\qquad
N_TX_t=A_\alpha=P_+[\alpha_F],
\qquad \alpha_F=1+89460y_F.
\tag{736.1}
$$

Set $D_T=\sum_{j=0}^{42}jt^j$. There exists a genuine
completed global $q$-unit $Y\in\mathscr K_M$ with

$$
\boxed{
\operatorname{div}_M Y=D_T\mathfrak q,\qquad
N_\Gamma Y=N_SY=D_TX_t.
}
\tag{736.2}
$$

Define, with no further choice,

$$
\boxed{Z=X_t-(t-1)Y.}
\tag{736.3}
$$

Then its full divisor and all three marked norms are exactly

$$
\boxed{
\operatorname{div}_M Z=N_T\mathfrak q,\qquad
N_\Gamma Z=N_SZ=N_TZ=A_\alpha.
}
\tag{736.4}
$$

At the original $q$ place, $Y$ is a local unit. The actual
ordinary unit $(s-1)Y$ has residue in $\mu_p$, and its
direct residue exponent is

$$
\boxed{r_\mu((s-1)Y)=-4J_\ell.}
\tag{736.5}
$$

The finite-flat target and witness of the restored first-moment
note give the identical chain with

$$
\boxed{r_\mu((s-1)Y_{\mathrm{fl}})
=-4(J_\ell-18).}
\tag{736.6}
$$

The coefficient $-4$ is proved below from the actual
unramified scalar action on $\mu_{p^2}$. It is not an
identification of $r_\mu$ with the power-residue
logarithm $\ell$.

## 1. Full ordinary kernel lattices

Use $\mathcal O=\mathbf Z_{43}[i]$ and $k=\mathcal O/p$.
All groups and divisors are tensored with $\mathcal O$
and projected to the same $\chi^-$ summand as R633.
In particular $P_+=44e_{\chi^-}$ is not averaged.
Write

$$
K_M=\ker(N_\Gamma:E_M\to E_B),\qquad
K_N=\ker(N_\Gamma:E_N\to E_{F_t}).
$$

The proved inputs are

$$
E_B=\mathcal O[S,T]u_B,\qquad
K_N=R_\Gamma[T]c_t,\qquad
R_\Gamma=\mathcal O[\Gamma]/(N_\Gamma),
\tag{736.7}
$$
$$
N_Su_B=u_t,\quad
N_Sc_B=c_t,\quad
N_\Gamma c_B=(1-s^{11})u_B,
\tag{736.8}
$$
$$
N_\Gamma E_M=\mathcal J
:=(p,s-1,N_T)E_B.
\tag{736.9}
$$

Here (736.7) is the entire saturated ordinary lattice of
R633/R657, not merely the Robert subgroup.
Equation (736.9) is R731. R715/R718 also prove that
the two cyclic Tate cohomology groups of $E_M$ for
$S$ vanish:

$$
\widehat H^{-1}(S,E_M)=
\widehat H^0(S,E_M)=0.
\tag{736.10}
$$

Apply the natural Tate sequence to

$$
0\longrightarrow K_M\longrightarrow E_M
\xrightarrow{N_\Gamma}\mathcal J\longrightarrow0.
$$

The two vanishing groups in (736.10) identify

$$
K_N/N_SK_M
=\widehat H^0(S,K_M)
\simeq \widehat H^{-1}(S,\mathcal J).
\tag{736.11}
$$

This is compatible with the actual $\Gamma,T$ actions.
The action of $\Gamma$ on $\mathcal J\subset E_B$
is trivial.

Put $R=\mathcal O[S,T]$ and
$I=(p,s-1,N_T)\subset R$, using the fixed generator
$u_B$ to identify $\mathcal J=Iu_B$.
The regular cyclic $S$ module gives
$\ker(N_S:R\to R)=(s-1)R$.
Since $(s-1)R\subset I$,

$$
\widehat H^{-1}(S,I)
=\frac{(s-1)R}{(s-1)I}.
$$

Multiplication by $s-1$ identifies this quotient with
$R/(I+N_SR)$. But $N_SR\subset I$, since
$N_S\equiv p\bmod(s-1)$. Therefore

$$
\widehat H^{-1}(S,\mathcal J)
\simeq R/I\simeq k[T]/(N_T).
\tag{736.12}
$$

The image of the actual generator $c_t$ is primitive.
To see this directly in the connecting map, put
$H(s)=1+s+\cdots+s^{10}$. It is a unit in
$\mathcal O[S]$, because its augmentation is $11$.
The unit $v=-H(s)^{-1}c_B$ has

$$
N_\Gamma v=(s-1)u_B,\qquad
N_Sv=-\frac1{11}c_t.
$$

Thus the generator in (736.12) connects, up to the
common connecting-map sign, to the unit multiple
$-c_t/11$. This also fixes the integral generator
rather than just the isomorphism type of the quotient.

Combining (736.7), (736.11), and (736.12) proves

$$
\boxed{
N_SK_M=(\pi,N_T)K_N
=(\pi,N_T)R_\Gamma[T]c_t.
}
\tag{736.13}
$$

In particular the image is a precise ordinary
kernel-norm lattice.

## 2. The original scalar action on the local p-primary roots

Put $Q_0=q^2$ for the residue cardinality at $P_0$.
The original congruences are

$$
q\equiv-1+11p\pmod{p^2},\qquad
-q\equiv1+32p\pmod{p^2},
$$
$$
\frac{Q_0-1}{p}\equiv-22\equiv21\pmod p.
\tag{736.14}
$$

At the $q$ place of $B$, the scalar extension is
unramified of degree $p$, and its residue field is
$\mathbf F_{Q_0^p}$. Since $v_p(Q_0-1)=1$,

$$
v_p(Q_0^p-1)=2.
\tag{736.15}
$$

Its entire $p$-primary residue subgroup is consequently
$\mu_{p^2}$. The positive Frobenius over the completion
of $F_t$ is the original $s^{32}$. Frobenius acts on
that residue field by the $Q_0$th power, so the actual
$s$ acts on $\mu_{p^2}$ by

$$
\boxed{s:z\longmapsto z^{\,1+2p}\pmod{p^2}.}
\tag{736.16}
$$

Indeed $Q_0\equiv1+21p\bmod p^2$, and
$32\cdot2\equiv21\bmod43$. This checks the specified
generator, not just an unspecified generator of $S$.

Consequently the residue action of its norm is

$$
\sum_{j=0}^{p-1}(1+2p)^j\equiv p\pmod{p^2}.
\tag{736.17}
$$

The $\Gamma$ extension is totally ramified at $q$.
It acts trivially on the residue field, so its norm
also raises the residue of a unit to the $p$th power.

Choose temporarily a residue root $\xi$ of exact order
$p^2$ with $\xi^p=\zeta$. All formulas ultimately use
only $\zeta$ and exponents modulo $p$, so a different
choice of $\xi$ gives the same conclusions. Tensoring
the cyclic residue modules with $\mathcal O$ treats
the character coefficients linearly; it does not
assert that an arbitrary $\mathcal O$ exponent is an
ordinary integer exponent.

## 3. The actual phase of c_t and the complete phase kernel

For an ordinary unit in $K_N$, the residue is in
$\mu_p$, since its $\Gamma$ norm is zero and
$\Gamma$ acts trivially on residue. Define
$r_\mu$ to be the exponent of that residue in the
original $\zeta$.

Write the $p$-primary residue components of the
actual $u_B$ and $c_B$ at the specified $q$ place
as $\xi^m$ and $\xi^n$. From (736.8) and (736.16),

$$
pn\equiv\bigl(1-(1+2p)^{11}\bigr)m
\equiv-22pm\pmod{p^2}.
$$

Hence $n\equiv-22m\bmod p$.
Equation (736.17) shows that
$c_t=N_Sc_B$ has residue $\zeta^n$, whereas
$u_t=N_Su_B$ has $p$-primary residue $\zeta^m$.
Using the original power-residue definition at $P_0$,
not a direct root exponent, gives

$$
\ell(u_t)=\frac{Q_0-1}{p}m
\equiv21m\equiv-22m\pmod p.
$$

Therefore, with the exact original normalizations,

$$
\boxed{r_\mu(c_t)=\ell(u_t).}
\tag{736.18}
$$

The argument applies to every actual $T$ and $\Delta$
translate, since their actions commute with the
norms and preserve the chosen residue marking.
No averaging factor or changed Robert ancestor is
introduced.

Retain the inverse-power convention

$$
A_u(T)=\sum_{j=0}^{42}\ell(t^ju_t)T^{-j}
=(T-1)v(T),\qquad v(T)\in k[T]^\times,
\quad A_u'(1)=-13i.
$$

Equation (736.18) proves that the whole phase map on
the complete lattice $K_N$ is

$$
\rho_N:R_\Gamma[T]c_t\longrightarrow k[T],
\qquad h(\gamma,t)c_t
\longmapsto \bar h(1,T)A_u(T).
\tag{736.19}
$$

Here $\rho_N$ records all marked $q$ places, with
coefficients $r_\mu(t^j e)$ and inverse powers $T^{-j}$.
The action of $\Gamma$ on residue is trivial.
Since $\operatorname{Ann}_{k[T]}(A_u)=(N_T)$,
(736.19) has exact integral kernel

$$
\ker\rho_N=(\pi,N_T)K_N.
$$

Together with (736.13), this gives the useful
ordinary equality

$$
\boxed{N_SK_M=\ker\rho_N.}
\tag{736.20}
$$

This is a statement about the full vector of actual
$q$ phases and about ordinary unit norms. It does
not replace either by a dimension count.

## 4. Comparing the two local norms, including the pole

The next local fact allows the second norm to be
corrected without changing the first.

Use the same real $q$-ray uniformizer $\theta$ of
R207/R561/R619. It belongs to the $S$-fixed ray field.
Both

$$
\frac{N_\Gamma\theta}{q},
\qquad \frac{\theta^p}{q}
$$

have residues in $\mathbf F_q^\times$. Their
$p$-primary phases are zero, since $p$ does not
divide $q-1$. For the first ratio the norm belongs
to the real rational local base field; for the
second ratio reality and the residue field of the
real totally ramified degree-$p$ subfield give the
same assertion.

Let $V$ be any local multiplicative element at a
$q$ place of $M$, and remove its valuation by
writing $V=d\theta+v$ additively, with $v$ a local
unit. The element $(N_S-N_\Gamma)V$ has valuation
zero. The uniformizer contribution has zero
$p$-primary residue phase by the preceding
paragraph. The contribution of $v$ also has
zero phase, because (736.17) and the last
paragraph of Section 2 make both norm exponents
equal to $p$ on $\mu_{p^2}$.

Consequently

$$
\boxed{
(N_S-N_\Gamma)V
\text{ is a local unit with zero }p
\text{-primary residue phase.}
}
\tag{736.21}
$$

This includes a nonzero valuation of $V$.
It is not obtained by applying a unit formula to
an element with a pole. The calculation extends
$\mathcal O$-linearly to completed character
elements and applies at every marked $T$ translate.

## 5. A global simultaneous Gamma/S norm lemma

Let $x$ be a completed global $q$-unit of $F_t$ with

$$
\operatorname{div}_{F_t}x=d(t)P_+P_0,
\qquad d(t)\in\mathcal O[T],\qquad d(1)\in p\mathcal O.
\tag{736.22}
$$

There exists a completed global $q$-unit $V$ in $M$
with

$$
\boxed{
\operatorname{div}_M V=d(t)\mathfrak q,\qquad
N_\Gamma V=N_SV=x.
}
\tag{736.23}
$$

Here is the full global proof.

R731 proves that the actual class
$e=[\mathfrak q]\in A_M$ is the nonzero
$\Gamma$-socle, is fixed by $T$, and is killed by
$p$. Thus the class of $d(t)\mathfrak q$ is
$d(1)e=0$. The full completed divisor sequence
gives a global $q$-unit $V_0$ with precisely that
divisor.

Its $\Gamma$ norm has the same full divisor in
$B$ as $x$, so
$N_\Gamma V_0=x+v_0$ with $v_0\in E_B$.
The element $x$ is a field norm from $M/B$:
at $q$, restriction to the unramified scalar
degree-$p$ extension multiplies its base
$\Gamma$ norm obstruction by $p$; at $p,2$
the extension is split; at all other places
$x$ is a unit in an unramified extension.
The cyclic Hasse Norm theorem applies.
R731 then identifies
$E_B\cap N_\Gamma\mathscr K_M=N_\Gamma E_M$.
It supplies an ordinary unit correction,
giving $V_1$ with the same divisor and
$N_\Gamma V_1=x$.

Now

$$
v_1=N_SV_1-x\in K_N.
$$

Its divisor is zero: $S$ is unramified of
residue degree $p$ at $q$, and extension from
$F_t$ to $N$ has ramification index $p$ there.
Its $\Gamma$ norm is zero by commuting norms
and the fact that both $S,\Gamma$ fix $x$.
At every marked $q$ place,
$v_1=(N_S-N_\Gamma)V_1$, so (736.21) proves
$\rho_N(v_1)=0$.

The exact ordinary identity (736.20) supplies
$e_1\in K_M$ with $N_Se_1=v_1$.
Set $V=V_1-e_1$.
This is an ordinary unit correction, so the
entire divisor remains unchanged; it preserves
$N_\Gamma V=x$ and makes $N_SV=x$.
This proves (736.23).

For a fixed $x$ and full divisor, all such
solutions form the exact torsor under

$$
K_M\cap\ker N_S.
\tag{736.24}
$$

The proof uses global principalization followed
by ordinary corrections. Local existence alone
does not produce these elements.

## 6. The original exact exchange and its three norms

Apply the lemma with $x=D_TX_t$ and
$d(t)=D_T$. Its augmentation is

$$
D_T(1)=\frac{p(p-1)}2\in p\mathcal O.
$$

This gives exactly the element $Y$ of (736.2),
with no new prime, phase, or norm target.

The integral group-ring identity is

$$
(t-1)D_T=p-N_T.
\tag{736.25}
$$

In $M$, the extension of the original divisor
of $X_t$ is $p\mathfrak q$:
$\Gamma$ is totally ramified of degree $p$,
whereas the scalar step is unramified.
Thus the definition $Z=X_t-(t-1)Y$ gives

$$
\operatorname{div}_M Z
=p\mathfrak q-(t-1)D_T\mathfrak q
=N_T\mathfrak q.
$$

Both $\Gamma$ and $S$ fix $X_t$. Using (736.2)
and (736.25) gives, separately for either of
these two norms,

$$
N_\Gamma Z
=pX_t-(t-1)D_TX_t=N_TX_t=A_\alpha,
$$
$$
N_SZ
=pX_t-(t-1)D_TX_t=A_\alpha.
$$

Finally $N_T(t-1)=0$ gives

$$
N_TZ=N_TX_t=A_\alpha.
$$

This proves the three exact identities in
(736.4). They concern one and the same
global $Z$ constructed from one and the
same $Y$. There is no uncorrected ordinary
exchange term.

## 7. The original q value is exactly minus four times the first moment

The coefficient of the original $Q$ in
$D_T\mathfrak q$ is zero. Therefore $Y$
is a local unit at that prime. Also
$(s-1)Y$ is an ordinary global unit:
$S$ fixes each $q$ prime in its full divisor.
Its $\Gamma$ norm is
$(s-1)D_TX_t=0$, since $S$ fixes $F_t$.
Its residue is therefore in $\mu_p$.

Write the $p$-primary residue of $Y$ as
$\xi^m$. Since $\Gamma$ acts trivially
on residue, the exact norm in (736.2)
gives the $p$-primary residue
$\zeta^m$ for $D_TX_t$.
At the original $P_0$ this is a unit, and
the restored first-moment definition is

$$
J_\ell=\ell(D_TX_t).
$$

Using (736.14) gives

$$
J_\ell\equiv21m\pmod {43}.
\tag{736.26}
$$

On the other hand (736.16) gives

$$
\operatorname{res}((s-1)Y)=\xi^{2pm}=\zeta^{2m}.
$$

Since $21^{-1}=-2\bmod43$, its direct exponent is

$$
r_\mu((s-1)Y)=2m
=2\cdot21^{-1}J_\ell
=-4J_\ell.
$$

This proves (736.5). All three ingredients are
needed: the actual scalar generator, the
local $\mu_{p^2}$ before the norm, and the
original definition of $\ell$ over
$\mathbf F_{q^2}$. Replacing this calculation
by $\ell((s-1)Y)$ would insert another
factor $21$ and change the asserted value.

The phase is independent of the choice in
(736.24). If $Y'$ is another solution, then
$Y'-Y\in K_M$, whose residue lies in
$\mu_p$. The scalar generator fixes
$\mu_p$ by (736.16), so
$r_\mu((s-1)(Y'-Y))=0$.
Thus (736.5) is the value of the actual
marked global exchange class, not an
arbitrary selection among local roots.

## 8. The same exchange for the finite-flat target

The restored first-moment note proves, with
the same original R185 units and without
averaging the projector,

$$
X_{\mathrm{fl}}
=X_t-\frac{8i}{1848}u_t,\qquad
A_{\alpha,\mathrm{fl}}
=A_\alpha-\frac{8i}{1848}u,
$$
$$
N_TX_{\mathrm{fl}}=A_{\alpha,\mathrm{fl}},
\qquad
J_{\mathrm{fl}}=J_\ell-18.
\tag{736.27}
$$

The full divisor is unchanged. Apply the
same lemma to $D_TX_{\mathrm{fl}}$, and
define

$$
Z_{\mathrm{fl}}
=X_{\mathrm{fl}}-(t-1)Y_{\mathrm{fl}}.
$$

The proof of Section 6 gives, integrally,

$$
N_\Gamma Z_{\mathrm{fl}}
=N_SZ_{\mathrm{fl}}
=N_TZ_{\mathrm{fl}}
=A_{\alpha,\mathrm{fl}},
$$

with the same divisor $N_T\mathfrak q$.
The proof of Section 7 is unchanged and yields

$$
r_\mu((s-1)Y_{\mathrm{fl}})
=-4J_{\mathrm{fl}}=-4(J_\ell-18).
$$

The unit correction is retained in the exact
norm targets; its phase is not absorbed
into a relabelled root.

## 9. Remaining comparison and computation

This result puts the reconstructed first
moment into a specific ordinary global
exchange unit and gives an exact
three-norm chain. The witnesses have not
been numerically evaluated. The identity
does not yet identify this exchange
class with R720's original tangent
coefficient $b$.

R720 proves
$C=9ib$ and
$\Omega_2=\varepsilon(22+17b)$.
The comparison of the remaining
$T/\Gamma$ chain with that original
class, or an actual evaluation of the
marked witnesses, is still required.
No value of $J_\ell$ or $b$ is assigned
by (736.5) or (736.6).

## Dependencies

- [R613](R613-mixed-p-capitulation-and-the-exact-34-boundary.md):
  the identical $u_B,c_B$, and the actual
  exponent $11$ in their distribution.
- [R633](R633-complete-ordinary-unit-lattice-in-the-anti-pq-layer.md):
  the complete ordinary lattice
  $\ker N_\Gamma E_N=R_\Gamma[T]c_t$.
- [R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md)
  and [R718](R718-all-ordinary-class-lengths-and-exact-universal-unit-norms.md):
  both vanishing cyclic $S$ Tate groups
  of the actual full ordinary unit lattice.
- [R731](R731-complete-ordinary-Gamma-norms-and-marked-q-principalizations.md):
  the complete ordinary $\Gamma$-norm
  image and the actual nonzero $q$ socle class.
- [R207](R207-gaussian-trace-model-of-the-actual-ray-extension.md),
  as used with the original real uniformizer
  in [R561](R561-restored-scalar-norm-cocycle-and-ordinary-artin-class.md)
  and [R619](R619-ordinary-anti-p-class-group-and-actual-artin-nine.md).
- [The restored first-moment note](../notes/2026-11-14-r599-first-moment-normalization-reconstruction.md):
  the exact ordinary $X_t$ torsor, the
  same $J_\ell$, and the original
  finite-flat correction $18$.
