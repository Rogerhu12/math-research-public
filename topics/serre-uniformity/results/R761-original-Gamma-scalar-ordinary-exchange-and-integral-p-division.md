# R761: the original Gamma-scalar ordinary exchange is integrally p-divisible

Date: 2026-11-14. **Status: proved.** For the actual original
three-norm construction of R736/R756, the unit
$\mathcal W_{\Gamma S}$ is in $43E_M$. Consequently the
$\Gamma$ and scalar boundaries have a single ordinary
unit primitive, with all three norms zero. The proof uses
the actual ordinary lattice and every marked q phase.
It does not assert the same divisibility for the other
two pairs of directions and does not evaluate $J_\ell$
or $b$.

## 1. The same fields, divisors, and norm construction

Keep $p=43$, $\mathcal O=\mathbf Z_{43}[i]$, $k=\mathcal O/p$,
the original fields $F_t=B^S$, $N=LF_t$, and $M=LB$, and
the commuting marked groups $\Gamma=\langle\gamma\rangle$,
$S=\langle s\rangle$, $T=\langle t\rangle$. Put
$\pi=\gamma-1$. All modules are completed ordinary unit,
principal-divisor, or full divisor modules in the original
character selected by $P_+=44e_{\chi^-}$. The projector
is unaveraged, and multiplicative groups are written additively.

Use exactly the $X_t,Y$ of R736. If $\mathfrak q=P_+Q_M$,
their identities in $M$ are

$$
\begin{aligned}
\operatorname{div}X_t&=p\mathfrak q,&N_TX_t&=A_\alpha,\\
\operatorname{div}Y&=D_T\mathfrak q,&
N_\Gamma Y=N_SY&=D_TX_t,
\end{aligned}
\tag{761.1}
$$

where $D_T=\sum_{j=0}^{42}jt^j$. These retain the actual
q prime and the original norm target $A_\alpha$.
The first divisor is its extension from $F_t$: $q$ is
totally ramified of degree $p$ in $M/B$ and unramified
of degree $p$ in the scalar direction. The $T$ direction
is split at q. In particular both $\Gamma$ and $S$ fix
every q prime in (761.1).

Put

$$
Z=X_t-(t-1)Y,\qquad k_0=(p-1)/2=21.
$$

Then R756 has

$$
\operatorname{div}Z=N_T\mathfrak q,\qquad
N_\Gamma Z=N_SZ=N_TZ=A_\alpha.
\tag{761.2}
$$

For $i=\Gamma,S$ let

$$
D_i=\sum_{j=0}^{p-1}jg_i^j,\qquad
B_i=D_i-k_0N_i,
\qquad g_\Gamma=\gamma,\quad g_S=s.
\tag{761.3}
$$

These $B_i$ are the explicitly displayed balanced
operators. They are not substituted for R561's separately
marked balanced Robert operator. We only use the exact
identities

$$
(g_i-1)D_i=p-N_i,\qquad
\operatorname{aug}D_i=pk_0,\qquad
\operatorname{aug}B_i=0.
\tag{761.4}
$$

## 2. An actual ordinary two-direction cocycle

Define

$$
R_\Gamma=B_\Gamma Y
=D_\Gamma Y-k_0D_TX_t,
\qquad
R_S=B_SY=D_SY-k_0D_TX_t,
\tag{761.5}
$$

and

$$
R_{\Gamma S}
=D_\Gamma D_SY-pk_0^2D_TX_t.
\tag{761.6}
$$

All three are ordinary units. For (761.5), the two
divisors are both $pk_0D_T\mathfrak q$. For (761.6),
the two divisors are both $p^2k_0^2D_T\mathfrak q$.
There are no outside-support terms to discard.

Using (761.1) and (761.4),

$$
\begin{aligned}
\pi R_\Gamma&=(s-1)R_S=pY-D_TX_t,\\
N_\Gamma R_S&=N_SR_\Gamma=0,\\
\pi R_{\Gamma S}&=pR_S,\qquad
(s-1)R_{\Gamma S}=pR_\Gamma,\\
N_\Gamma R_{\Gamma S}&=N_SR_{\Gamma S}=0.
\end{aligned}
\tag{761.7}
$$

For example
$\pi R_{\Gamma S}=pD_SY-D_SN_\Gamma Y
=pD_SY-pk_0D_TX_t=pR_S$.
For its $\Gamma$ norm, both terms in (761.6) become
$p^2k_0^2D_TX_t$; the scalar norm has the same calculation.

Thus the assignment

$$
f(\gamma)=R_S,\qquad f(s)=R_\Gamma
\tag{761.8}
$$

is a genuine $\Gamma\times S$ cocycle with values in
$E_M$. The order-$p$ conditions are the two zero norms
in (761.7), and the commuting-generator condition is
$\pi R_\Gamma=(s-1)R_S$.

The ordinary unit of the R756 cube is

$$
\mathcal W_{\Gamma S}
=D_\Gamma D_SZ-pk_0^2A_\alpha.
$$

There is the exact factorization

$$
\boxed{\mathcal W_{\Gamma S}=-(t-1)R_{\Gamma S}.}
\tag{761.9}
$$

Indeed $(t-1)D_TX_t=pX_t-A_\alpha$, while
$D_\Gamma D_SX_t=p^2k_0^2X_t$ because $X_t$ is
fixed by both $\Gamma$ and $S$. Substituting these
identities into (761.6) proves (761.9), including its sign.

## 3. Both balanced derivatives have zero full q phase

We need the entire p-primary phase, including the poles
of $Y$, and not only the phase at the one translate
where its valuation is zero.

At an original q completion, $M$ has residue field
$\mathbf F_{q^{2p}}$. Since $v_p(q+1)=1$ and
$p\nmid q-1$, the elementary lifting-the-exponent formula
gives $v_p(q^{2p}-1)=2$. Its full p-primary residue roots
are consequently $\mu_{p^2}$.
The actual scalar generator acts on these roots as
$s=1+2p\pmod{p^2}$; this is the original
$\operatorname{Fr}_{q^2}=s^{32}$ marking of R561.
The $\Gamma$ direction is inertia and fixes the residue field.

Use R207/R736's actual real q-ray uniformizer $\theta$.
It is $S$-fixed and satisfies
$\gamma\theta/\theta\equiv\zeta$ at the marked prime,
where $\zeta$ is the positive original Weil root.
At any T translate write locally

$$
t^jY=n_j\theta+V_j,
\tag{761.10}
$$

with $V_j$ a unit and $n_j$ the actual valuation.
In the original labeling $n_j$ is the representative
of $-j$ in $\{0,\ldots,42\}$. No replacement by a
constant valuation vector is made. At a Delta translate
the same calculation is multiplied by the actual
character coefficient; the zero conclusions below are
therefore valid at every prime in the character divisor.

The two sums required in the calculation are exactly

$$
\sum_{a=0}^{p-1}(a-k_0)=0,
\qquad
\sum_{a=0}^{p-1}a(a-k_0)
=\frac{p(p^2-1)}{12}\in p\mathbf Z.
\tag{761.11}
$$

For $B_S$, the pole in (761.10) is killed by the first
sum, because $S$ fixes $\theta$. If the p-primary
unit residue is $\xi^e$ with $\xi^p=\zeta$, its exponent
after applying $B_S$ is

$$
e\sum_{a=0}^{p-1}(a-k_0)(1+2p)^a
\equiv
e\left(\sum_a(a-k_0)+2p\sum_a a(a-k_0)\right)
\equiv0\pmod{p^2}.
\tag{761.12}
$$

For $B_\Gamma$, its action on the unit residue $V_j$
is killed by its zero augmentation. Its action on the
pole is the $\mu_p$ phase with exponent

$$
n_j\sum_{a=0}^{p-1}a(a-k_0),
$$

which is zero modulo $p$ by the second sum in (761.11).
The uniformizer power itself is killed by the first sum.
This accounts for the full pole term of $B_\Gamma Y$.

We have therefore proved

$$
\boxed{
r_{\mu_{p^2}}(t^jR_S)
=r_{\mu_{p^2}}(t^jR_\Gamma)=0
\quad(0\le j\le42),
}
\tag{761.13}
$$

and the same vanishing at all their Delta translates.
Here coefficients are extended to $\mathcal O/p^2$;
the computation is linear and so applies to the
completed character components without choosing
integer representatives for the Teichmuller projector.

## 4. The ordinary Gamma phase injection in this actual field

We spell out the part of R731 that is needed to pass
from (761.13) to an ordinary global primitive.

The base $B$ is the actual pure-$p^2$ field, with
$A_B=0$ in the indicated character and
$E_B=\mathcal O[S,T]u_B$. The extension $M/B$ is
cyclic of degree $p$, ramifies only at q, is totally
ramified there, and is split above p. Let $a\in E_M$
satisfy $N_\Gamma a=0$. Hilbert 90 in the completed
character component supplies an element $z$ of
$M^\times\otimes\mathcal O$ such that

$$
(\gamma-1)z=a.
$$

The full divisor of $z$ is $\Gamma$-invariant. At every
unramified prime an invariant integral divisor is the
extension of a divisor of $B$. At a q prime write
$z=d\theta+z_0$ locally, with $z_0$ a unit. Inertia
acts trivially on its unit residue, and the fixed positive
uniformizer convention gives

$$
r_{\mu_p}(a)=d\pmod p.
\tag{761.14}
$$

This is a statement in the corresponding
$\mathcal O/p$ character coefficient. In particular,
zero phase is equivalent to the q valuation being
divisible by $p$, exactly the condition for that
invariant divisor to be the extension of an integral
divisor from $B$.

If $a$ has zero phase at every q prime, its entire
divisor is therefore $j_{M/B}D$ for a full character
divisor $D$ of $B$. Since $A_B=0$, that divisor is
principal in the completed character module. Subtract
a corresponding element of $B^\times\otimes\mathcal O$
from $z$. The result is an ordinary unit with the
same $\Gamma$ boundary $a$.

This proves the exact implication

$$
\boxed{
a\in\ker N_\Gamma E_M,\quad
r_{\mu_p}(a)=0\text{ at all q primes}
\quad\Longrightarrow\quad
a\in(\gamma-1)E_M.
}
\tag{761.15}
$$

It is the required injection of ordinary
$H^1(\Gamma,E_M)$ into the q ramification-phase module.
All divisors, including any outside-support terms of
the Hilbert 90 solution, have been retained. The argument
does not assert that a field-norm preimage is automatically
an ordinary unit, and does not use an unmarked q root.

## 5. A single ordinary primitive in both directions

Apply (761.15) to $a=R_S$, using (761.7) and (761.13).
There is an ordinary $F_0\in E_M$ with

$$
\pi F_0=R_S.
$$

The error

$$
h=(s-1)F_0-R_\Gamma
$$

is $\Gamma$-invariant by the cocycle identity in (761.7),
so it belongs to the exact ordinary invariant lattice
$E_M^\Gamma=E_B$. Its scalar norm is zero. Since
$E_B=\mathcal O[S,T]u_B$ is free over $\mathcal O[S]$,
its scalar cohomology vanishes integrally:
$\ker N_S E_B=(s-1)E_B$. Choose an ordinary
$e_B\in E_B$ with $(s-1)e_B=h$ and set
$F=F_0-e_B$. We obtain the genuine simultaneous
ordinary primitive

$$
\boxed{\pi F=R_S,\qquad (s-1)F=R_\Gamma.}
\tag{761.16}
$$

Every choice made here has been inside an actual
ordinary unit lattice. Two such $F$'s differ by
$E_M^{\Gamma\times S}=E_{F_t}$.

Equation (761.7) now shows that

$$
e=pF-R_{\Gamma S}\in E_{F_t}.
\tag{761.17}
$$

Applying either norm to (761.17), and using the zero
norms of $R_{\Gamma S}$, gives

$$
\boxed{N_\Gamma F=N_SF=e.}
\tag{761.18}
$$

Cancellation of $p$ is legitimate: these unit lattices
are torsion-free over $\mathcal O$. There is no global
$\mu_p$ in $M$, whose degree $88p^3$ is not divisible
by $p-1=42$, and prime-to-$p$ torsion disappears in
the completion.

## 6. Every q translate of the lower ordinary norm has zero phase

For each $j$, the ordinary unit $t^jF$ satisfies

$$
(s-1)t^jF=t^jR_\Gamma.
$$

The right hand side has zero full p-primary phase by
(761.13). If the phase exponent of $t^jF$ in
$\mu_{p^2}$ is $e_j$, the actual action
$s=1+2p$ implies

$$
2p e_j=0\pmod{p^2},\qquad e_j=0\pmod p.
$$

Thus the phase of $t^jF$ lies in $\mu_p$.
Its $\Gamma$ norm raises the residue to the $p$th
power, since the extension is totally ramified and
$t^jF$ is an ordinary unit. By (761.18) that norm is
$t^je$, and consequently

$$
\boxed{\ell(t^je)=0\quad(0\le j\le42).}
\tag{761.19}
$$

The logarithm is the original Weil-normalized one
in $F_t$. Restriction to the larger residue field
does not change this zero statement. There is no
uniformizer correction, because $F$ is ordinary.

Use the actual full lattice $E_{F_t}=\mathcal O[T]u_t$
and write $e=g(t)u_t$. R619/R756 prove

$$
A_u(T)=\sum_{j=0}^{42}\ell(t^ju_t)T^{-j}
       =(T-1)v(T),\qquad v(1)=-13i\ne0,
$$

and hence $\operatorname{Ann}_{k[T]}A_u=kN_T$.
The complete vector (761.19) says exactly
$\bar g A_u=0$, in the original inverse-power
convention. Therefore

$$
\bar g\in kN_T,
\qquad
e\in pE_{F_t}+\mathcal O u,
\qquad
(t-1)e\in pE_{F_t}.
\tag{761.20}
$$

This uses all $43$ phases. Vanishing at one q prime
alone would not prove (761.20).

## 7. The exact p-division and its ordinary common primitive

Combine (761.9), (761.17), and (761.20):

$$
\mathcal W_{\Gamma S}
=-p(t-1)F+(t-1)e\in pE_M.
$$

We have proved

$$
\boxed{\mathcal W_{\Gamma S}\in43E_M.}
\tag{761.21}
$$

For an explicit description of its integral quotient,
write $e=ph_t+\rho u$ with $h_t\in E_{F_t}$ and
$\rho\in\mathcal O$, as allowed by (761.20), and put
$H=F-h_t$. Then

$$
\begin{aligned}
R_{\Gamma S}&=pH-\rho u,\\
\pi H&=R_S,&(s-1)H&=R_\Gamma,\\
N_\Gamma H&=\rho u,&N_SH&=\rho u.
\end{aligned}
\tag{761.22}
$$

It follows that the unique ordinary unit

$$
\boxed{
\mathcal L_{\Gamma S}
=-\frac{\mathcal W_{\Gamma S}}p
=(t-1)H\in E_M
}
\tag{761.23}
$$

satisfies

$$
\boxed{
\pi\mathcal L_{\Gamma S}=\mathcal V_S,\qquad
(s-1)\mathcal L_{\Gamma S}=\mathcal V_\Gamma,\qquad
N_\Gamma\mathcal L_{\Gamma S}
=N_S\mathcal L_{\Gamma S}
=N_T\mathcal L_{\Gamma S}=0.
}
\tag{761.24}
$$

Here the $\mathcal V_i$ are exactly those of R756,
with $\mathcal V_i=(t-1)R_i$ for $i=\Gamma,S$.
The two first equalities follow from (761.22), and
the first two norms vanish because $t$ fixes $u$.
The third norm vanishes because (761.23) is a genuine
ordinary $T$ coboundary.

There is no division ambiguity: $p$ is injective on
$E_M$, so (761.23) is independent of $F,h_t$, and
the lift of $\rho$. In (761.22), the residue
$\bar\rho$ is fixed by $R_{\Gamma S}$, since
$u\notin pE_M$. To check the last assertion, a
hypothetical $u=pv$ in $E_M$ would, by torsion
freeness, make $v$ fixed by all of $\Gamma,S,T$.
Then $v\in E_F=\mathcal O u$, contradicting the
primitivity of $u$ in that base lattice.

Thus the same proof also gives the exact local reduction

$$
R_{\Gamma S}\equiv-\bar\rho u\pmod{pE_M},
\qquad
\operatorname{loc}_p(R_{\Gamma S})
\equiv-\bar\rho\operatorname{loc}_p(u)\pmod{pU_M}.
\tag{761.25}
$$

For a supplied actual p-local coordinate vector of
$R_{\Gamma S}$, its coefficient can therefore be
read by any explicitly normalized base local
functional taking $u$ to $1$; the vector already
lies on that primitive line. Equation (761.25)
does not supply the unknown global coordinate vector
of $Y$, nor assert that $\bar\rho$ is independent
of changing $Y$ within its original ordinary torsor.

## 8. Scope of the new exchange

The proof applies to every genuine ordinary global
$Y$ satisfying (761.1) with the original markings.
It uses additional global information absent from
a bare local solution of the three norm equations:
the ordinary divisor-phase injection (761.15),
the primitive global lattice $E_B$, and the
complete ordinary residue kernel in $E_{F_t}$.

There is no contradiction with R756's semilocal
counterexample to automatic division from the norm
equations alone. That example does not provide a
global ordinary $Y$ with (761.1). In the present
proof it is the actual global ordinary primitive
$F$ that makes the argument with all T translates
of $e$ possible.

Only the $\Gamma/S$ pair has been handled here.
No assertion is made that $\mathcal W_{\Gamma T}$,
$\mathcal W_{ST}$, or the top cube element is
ordinarily p-divisible. Those further compatibilities,
and the descent of the primitive to the original
supported rational dual cochain of R755, must be
proved separately. The remaining finite-flat section
and the actual $J_\ell,b,\sigma_2,I_\alpha$ are
not evaluated by (761.21)--(761.25).

## Dependencies

- [R207](R207-gaussian-trace-model-of-the-actual-ray-extension.md):
  the original real q-ray uniformizer.
- [R561](R561-restored-scalar-norm-cocycle-and-ordinary-artin-class.md):
  the actual scalar Frobenius and $\mu_{p^2}$ action.
- [R619](R619-ordinary-anti-p-class-group-and-actual-artin-nine.md):
  the saturated lattice $E_{F_t}$ and original derivative $-13i$.
- [R686](R686-all-p-power-layers-and-exact-ordinary-class-growth-law.md):
  the pure-p ordinary lattice $E_B=\mathcal O[S,T]u_B$ and $A_B=0$.
- [R731](R731-complete-ordinary-Gamma-norms-and-marked-q-principalizations.md):
  the full ordinary q-divisor and Gamma-cohomology framework.
- [R736](R736-original-three-norm-exchange-and-minus-four-moment-phase.md):
  the original $X_t,Y,Z$ and their exact norms and q markings.
- [R756](R756-original-three-norm-ordinary-lattice-and-exact-scalar-cohomology.md):
  the original ordinary derivative cube.
