# R763: ordinary torsor normalization preserves the original moment and real marking

Date: 2026-11-14. **Status: proved.** The residual coefficient
$\bar\rho$ in R761 is completely removable by changing the
allowed ordinary witness $Y$. The change preserves the original
$X_t$, its divisor, its exact norm target, the class
$\eta_\alpha$, and $J_\ell$. The same assertion holds with
the original semilinear real marking imposed. One can therefore
choose the witness so that $R_{\Gamma S}/43$ itself is an
ordinary unit of both $\Gamma$ and $S$ norm zero. This is a
normalization of a witness, not a computation of $J_\ell$ or $b$.

## 1. The actual ordinary torsor and its residual coefficient

Use the original $p=43$, fields $M=LB$ and $F_t=B^S$,
groups $\Gamma,S,T$, coefficient ring
$\mathcal O=\mathbf Z_{43}[i]$, residue field $k$, and
unaveraged projector $P_+$ of R736/R756/R761.
Put $\pi=\gamma-1$ and $k_0=21$, and retain

$$
D_i=\sum_{a=0}^{42}ag_i^a,\qquad
B_i=D_i-k_0N_i\qquad(i=\Gamma,S).
$$

Fix the same original witness $X_t$ with
$\operatorname{div}_{F_t}X_t=P_+P_0$ and
$N_TX_t=A_\alpha$. Let $\mathcal Y(X_t)$ be the set of
global q-units satisfying the original two norm conditions

$$
\operatorname{div}_M Y=D_T\mathfrak q,\qquad
N_\Gamma Y=N_SY=D_TX_t,
\qquad \mathfrak q=P_+Q_M.
\tag{763.1}
$$

R736 proves this set nonempty. Its exact difference module is

$$
K_{\Gamma S}
=\ker N_\Gamma E_M\cap\ker N_SE_M.
\tag{763.2}
$$

Indeed equal full divisors make a difference ordinary, and
the two equalities of norms put it in (763.2). Conversely
adding any element of (763.2) preserves all of (763.1).

For $Y\in\mathcal Y(X_t)$, the ordinary unit of R761 is

$$
R_{\Gamma S}(Y)
=D_\Gamma D_SY-pk_0^2D_TX_t
=B_\Gamma B_SY.
\tag{763.3}
$$

The last equality is exact. In expanding the two $B$'s,
each cross term is $pk_0^2D_TX_t$ because
$N_\Gamma Y=N_SY=D_TX_t$ and this target is fixed by
both groups. The last term adds back one copy of that same
quantity.

R761 proves that there are $H\in E_M$ and $\rho\in\mathcal O$
with

$$
R_{\Gamma S}(Y)=pH-\rho u,
\qquad u=N_\Gamma y\in E_F.
\tag{763.4}
$$

The residue $\bar\rho(Y)\in k$ is uniquely determined
for this fixed $Y$. This uses $u\notin pE_M$, proved
in R761 by ordinary integral invariants and the primitivity
of $u$ in $E_F$. It does not mean that $\bar\rho(Y)$ is
constant on the torsor (763.1).

## 2. The exact variation law in the ordinary lattice

For $V\in K_{\Gamma S}$, both norm operators kill $V$, so

$$
R_{\Gamma S}(Y+V)-R_{\Gamma S}(Y)
=B_\Gamma B_SV=D_\Gamma D_SV.
\tag{763.5}
$$

Applying (763.4) to the two valid witnesses shows that the
right side reduces modulo $pE_M$ to a unique scalar
multiple of $u$. Define the actual homomorphism

$$
\lambda:K_{\Gamma S}\longrightarrow k,
\qquad
B_\Gamma B_SV\equiv\lambda(V)u\pmod{pE_M}.
\tag{763.6}
$$

It is $\mathcal O$-linear, with target killed by $p$,
and the exact variation of the residual coefficient is

$$
\boxed{\bar\rho(Y+V)=\bar\rho(Y)-\lambda(V).}
\tag{763.7}
$$

We now prove that this homomorphism is onto by constructing
a genuine ordinary preimage of $1$. The actual endpoint
theorem R715 gives $N_SE_M=E_N$. In particular there is
an ordinary unit $Z_y\in E_M$ satisfying

$$
N_SZ_y=y,
\tag{763.8}
$$

where $y$ is R561's original unit with $N_\Gamma y=u$.
There is no replacement of this ordinary norm equation
by a field norm equation.

Set

$$
V_y=\pi(s-1)Z_y.
\tag{763.9}
$$

It is ordinary and has both norms zero, so it is an
allowed torsor difference. Using
$D_\Gamma\pi=p-N_\Gamma$ and
$D_S(s-1)=p-N_S$ gives the exact identity

$$
\begin{aligned}
B_\Gamma B_SV_y
&=(p-N_\Gamma)(p-N_S)Z_y\\
&=u+p\bigl(pZ_y-N_\Gamma Z_y-y\bigr).
\end{aligned}
\tag{763.10}
$$

The last equality uses the actual equalities (763.8) and
$N_\Gamma y=u$. Thus

$$
\boxed{\lambda(V_y)=1.}
\tag{763.11}
$$

For any lift $c\in\mathcal O$ of $\bar\rho(Y)$,
the new witness $Y+cV_y$ therefore satisfies

$$
\bar\rho(Y+cV_y)=0,
\qquad
R_{\Gamma S}(Y+cV_y)\in pE_M.
\tag{763.12}
$$

This proves surjectivity and, in particular, the exact
description $K_{\Gamma S}/\ker\lambda\simeq k$.
No splitting of this quotient by a $p$-torsion submodule
of the torsion-free ordinary lattice is asserted.

## 3. The original moment and cohomology class do not change

Every adjustment in §2 leaves $X_t$ and $A_\alpha$
literally unchanged. It consequently leaves the original
principalization first moment $J_\ell$ unchanged.

The statement is also exact at the cohomological level.
With $K_\Gamma=\ker N_\Gamma E_M$, R756 defines

$$
\eta_\alpha=[(s-1)Y]\in H^1(S,K_\Gamma).
$$

Under $Y\mapsto Y+V$, $V\in K_{\Gamma S}\subset K_\Gamma$,
its cocycle changes by the actual ordinary coboundary
$(s-1)V$. Hence

$$
\boxed{\eta_\alpha(Y+V)=\eta_\alpha(Y).}
\tag{763.13}
$$

The full phase vector $-4J_\ell-ij$ of R756 stays fixed
at the level of the actual representatives as well. Indeed,
at every T translate the ordinary unit $V$ has zero
$\Gamma$ norm. Its full $\mu_{p^2}$ residue is raised
to the $p$th power by that norm, so its exponent is
divisible by $p$ and its residue lies in $\mu_p$.
The actual action $s=1+2p$ then kills the full p-primary
phase of $(s-1)V$. There is no uniformizer term because
$V$ is ordinary. This conclusion uses the same marked
ordinary cohomology and the same inverse-power convention.
It is not a claim that an arbitrary local norm solution
has the same first moment.

The associated three-norm element changes by

$$
Z=X_t-(t-1)Y
\quad\longmapsto\quad Z-(t-1)V.
$$

Its difference is ordinary and has zero norms under
$\Gamma,S,T$. Thus its full divisor and all three exact
norms remain the original ones. The same argument applies
to the already fixed finite-flat target and witness,
without changing its counterterm $18$.

## 4. The exact semilinear real torsor

Write $\tau$ for the original semilinear involution on
the chosen character component. It conjugates coefficients
in $\mathcal O$ and satisfies

$$
\tau\gamma\tau^{-1}=\gamma^{-1},\qquad
\tau s\tau^{-1}=s,\qquad
\tau t\tau^{-1}=t^{-1},\qquad \tau(i)=-i.
\tag{763.14}
$$

The original $P_+$ is preserved by this semilinear
operation: conjugating its Teichmuller coefficients and
inverting the tame generator give the same unaveraged
sum. We retain the original fixed prime $P_0$ and
$\tau A_\alpha=A_\alpha$.

As in the reconstructed first-moment note, an original
principalization witness can be chosen with
$\tau X_t=X_t$ by averaging within its ordinary
principalization torsor. For the following real
normalization, fix that witness once and for all.
None of the subsequent changes alters this $X_t$.
The general result of §§1--3 applies to any fixed
witness, whether or not this initial real choice was made.

The unbalanced $T$ derivative has the exact identity

$$
\tau D_T=D_T(t^{-1})=p(N_T-1)-D_T.
\tag{763.15}
$$

Set $C_X=(N_T-1)X_t$. Then $\tau C_X=C_X$, and

$$
\iota(Y)=C_X-\tau Y
\tag{763.16}
$$

is an involution of the actual torsor $\mathcal Y(X_t)$.
For its divisor, use
$\operatorname{div}_M X_t=p\mathfrak q$ and
(763.15): subtracting the divisor of $\tau Y$ from
that of $C_X$ gives $D_T\mathfrak q$.
For either norm $N_i$, $i=\Gamma,S$, $C_X$ is
fixed by $g_i$, and the norm commutes with $\tau$.
Therefore

$$
N_i\iota(Y)
=p(N_T-1)X_t-D_T(t^{-1})X_t=D_TX_t.
$$

Finally $\iota^2(Y)=Y$ because $\tau C_X=C_X$.
Since $2$ is a unit in $\mathcal O$, replacing $Y$ by
$(Y+\iota(Y))/2$ is an allowed ordinary torsor change
and imposes the exact real condition

$$
\boxed{Y+\tau Y=(N_T-1)X_t.}
\tag{763.17}
$$

Both terms being averaged are elements of the same
torsor; their difference belongs to (763.2).
Thus (763.13) proves that this normalization preserves
the same $\eta_\alpha$ and $J_\ell$. A subsequent
torsor difference $V$ preserves (763.17) exactly
when $\tau V=-V$.

## 5. The allowed real coefficient is removed by an ordinary real change

The balanced operator in the $\Gamma$ direction satisfies

$$
B_\Gamma(\gamma^{-1})=-\gamma B_\Gamma(\gamma).
\tag{763.18}
$$

For example this follows from
$D_\Gamma(\gamma^{-1})=p(N_\Gamma-1)-D_\Gamma$
and $\gamma D_\Gamma=D_\Gamma+p-N_\Gamma$.
The scalar operator $B_S$ is fixed by $\tau$.
Also $B_\Gamma B_SC_X=0$, since $C_X$ is fixed by
both $\Gamma$ and $S$. Applying $\tau$ to (763.3)
under condition (763.17) therefore yields

$$
\boxed{\tau R_{\Gamma S}(Y)=\gamma R_{\Gamma S}(Y).}
\tag{763.19}
$$

The original Robert unit satisfies $\tau u=-u$.
Reducing (763.19) by (763.4) and using the primitivity
of $u$ gives

$$
\overline{\bar\rho}=-\bar\rho,
\qquad \bar\rho\in i\mathbf F_{43}.
\tag{763.20}
$$

The first bar on the left denotes coefficient conjugation;
the residue $\bar\rho$ remains the one from (763.4).
This condition restricts the coefficient to a line. It
does not itself make it zero.

For completeness the original $y$ also satisfies

$$
\tau y=-y.
\tag{763.21}
$$

One can see this directly from R561's definition:
$y=(a/k)P_+Y_{311}$, where $Y_{311}$ is real,
$a=15i/7$ is purely imaginary, and
$k=\Pi(\widehat\omega^{-1})$ is fixed by coefficient
conjugation because the rational coefficients of
$\Pi$ satisfy $n_j=n_{-j}$. It also follows from
the original relations
$\pi y=a\gamma^{22}c_q$, $N_\Gamma y=u$, and
$\tau c_q=-c_q$: they make $\tau y+y$ both
$\Gamma$-fixed and of zero $\Gamma$ norm, hence zero
in the torsion-free ordinary lattice.

Choose the ordinary scalar norm preimage in (763.8)
to be anti-invariant as well. Starting from any one,
replace it by

$$
Z_y^-=(Z_y-\tau Z_y)/2.
$$

Since $\tau$ commutes with $N_S$, (763.21) gives
$N_SZ_y^-=y$ and $\tau Z_y^-=-Z_y^-$.
Now define the actual ordinary torsor difference

$$
\boxed{V_\tau=i\gamma^{21}\pi(s-1)Z_y^-.}
\tag{763.22}
$$

It has both norms zero. All semilinear signs in its
conjugate are retained:

$$
\begin{aligned}
\tau V_\tau
&=(-i)\gamma^{-21}(-\gamma^{-1}\pi)
   (s-1)(-Z_y^-)\\
&=-i\gamma^{-22}\pi(s-1)Z_y^-=-V_\tau,
\end{aligned}
\tag{763.23}
$$

because $\gamma^{-22}=\gamma^{21}$ for the original
order-$43$ generator. Thus this difference preserves
(763.17) without changing any marking.

Multiplying (763.10) by $i\gamma^{21}$ and using
$\gamma u=u$ gives

$$
B_\Gamma B_SV_\tau\equiv i u\pmod{pE_M},
\qquad \lambda(V_\tau)=i.
\tag{763.24}
$$

If $\bar\rho=ir$ with $r\in\mathbf F_{43}$, choose
an integral lift $c\in\mathbf Z_{43}$ of $r$.
It is fixed by coefficient conjugation. Then
$Y+cV_\tau$ still satisfies (763.17), while

$$
\bar\rho(Y+cV_\tau)=ir-ci=0\quad\hbox{in }k.
\tag{763.25}
$$

Hence the whole allowed real line is realized by
genuine ordinary torsor changes. Choosing this
representative uses no statement that an arbitrary
local root is global.

## 6. The normalized ordinary common primitive and its remaining T direction

For the witness just normalized, write $Y^0$ and put

$$
\boxed{H^0=R_{\Gamma S}(Y^0)/p\in E_M.}
\tag{763.26}
$$

The division is legitimate by (763.12) or (763.25),
and is unique. R761's exact derivatives and zero norms
give

$$
\boxed{
\pi H^0=R_S(Y^0),\qquad
(s-1)H^0=R_\Gamma(Y^0),\qquad
N_\Gamma H^0=N_SH^0=0.
}
\tag{763.27}
$$

Thus the constant $\rho u$ has been removed from
both norm equations by an allowed change of witness.
For the real normalization, (763.19) further gives

$$
\tau H^0=\gamma H^0.
\tag{763.28}
$$

The original $Z^0=X_t-(t-1)Y^0$ obeys
$\tau Z^0=t^{-1}Z^0$, obtained by substituting
(763.17) and
$(t-1)(N_T-1)X_t=-(t-1)X_t$.
The unit

$$
\mathcal L_{\Gamma S}^0=(t-1)H^0
=-\mathcal W_{\Gamma S}(Y^0)/p
$$

has all three norms zero and the same original
two boundary identities as R761. Its exact real
law is

$$
\tau\mathcal L_{\Gamma S}^0
=-\gamma t^{-1}\mathcal L_{\Gamma S}^0.
\tag{763.29}
$$

This normalization does not assert $N_TH^0=0$.
Its actual remaining norm lies in
$E_{M^T}\cap\ker N_\Gamma\cap\ker N_S$ and must
be treated by the ordinary T-norm problem. Likewise
the two diagonal derivatives of
$\mathcal L_{\Gamma S}^0$ are not set to zero.
They remain in the exact descent problem for the
original dual primitive.

## 7. Arithmetic consequence and boundary

The coefficient $\bar\rho(Y)$ is not an arithmetic
invariant of the fixed original principalization or
of its finite-flat target. Equations (763.11) and
(763.24) explicitly change it through every permitted
value while leaving $\eta_\alpha$ and $J_\ell$ fixed.
It therefore cannot by itself be used to evaluate
the finite-flat section or the coefficient $b$.

The useful conclusion is constructive at the level
of the actual ordinary lattice: a valid representative
can be chosen with the stronger zero-norm primitive
(763.26)--(763.27), including the correct real law.
The actual remaining T descent, the diagonal terms,
and the comparison with R755's rational supported
dual primitive remain to be proved.

## Dependencies

- [R561](R561-restored-scalar-norm-cocycle-and-ordinary-artin-class.md):
  the original $u,y,c_q$ and their exact normalization.
- [R708](R708-exact-isogeny-compression-and-the-43-valued-local-norm-fiber.md):
  the original semilinear action on the Robert units.
- [R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md):
  the actual ordinary surjection $N_SE_M=E_N$.
- [R736](R736-original-three-norm-exchange-and-minus-four-moment-phase.md):
  the original two-norm torsor for the fixed $X_t$.
- [R756](R756-original-three-norm-ordinary-lattice-and-exact-scalar-cohomology.md):
  the marked class $\eta_\alpha$ and full moment phase.
- [R761](R761-original-Gamma-scalar-ordinary-exchange-and-integral-p-division.md):
  the exact residual coefficient and ordinary common primitive.
- [The reconstructed first-moment note](../notes/2026-11-14-r599-first-moment-normalization-reconstruction.md):
  the real witness convention and the unchanged finite-flat counterterm.
