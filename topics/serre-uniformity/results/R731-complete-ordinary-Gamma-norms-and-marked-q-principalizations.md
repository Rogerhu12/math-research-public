# R731: the complete ordinary Gamma-norm image in every original p layer

Date: 2026-11-14. **Status: proved.** Keep the actual $p=43$,
the original $776$-bit $q$, all CM and Weil markings, the
positive arithmetic Artin convention, and the unaveraged
projector $P_+=44e_{\chi^-}$.

For the original compatible fields and Robert units of R686, put

$$
B_n=K(A_0[p^{n+1}])^{\mu_{42}},\qquad
M_n=LB_n,\qquad
P_n=S_n\times T_n,\qquad n\ge1,
$$
$$
F_{t,n}=B_n^{S_n},\qquad
N_n=M_n^{S_n},\qquad
u_n\in E_{B_n},\qquad u_{t,n}=N_{S_n}u_n.
$$

The groups $S_n=\langle s\rangle$ and $T_n=\langle t\rangle$
have order $r=p^n$. Write $N_{T_n}=\sum_{j=0}^{r-1}t^j$,
and retain $\Gamma=\operatorname{Gal}(L/F)=C_p$ and
$\pi=\gamma-1$. Then the exact ordinary unit norm is

$$
\boxed{
N_\Gamma E_{M_n}
=(p,s-1,N_{T_n})\mathcal O[S_n,T_n]u_n
=(p,s-1,N_{T_n})E_{B_n}.
}
\tag{731.1}
$$

In particular,

$$
\boxed{
E_{B_n}/N_\Gamma E_{M_n}
\simeq k[T_n]/(N_{T_n}).
}
\tag{731.2}
$$

This is an equality of complete ordinary lattices. The proof
first eliminates the actual difference between field norms of
units and norms of ordinary units. It then computes their
common image by the original local residue map. Neither step
uses a numerical value for $b$, $C$, or $J_\ell$.

A further consequence is a genuinely global, exactly normalized
$q$-principalization in $M_n$:

$$
\boxed{
\operatorname{div}Z_n=N_{T_n}P_+Q_n,\qquad
N_\Gamma Z_n=A_\alpha,
\quad A_\alpha=P_+[\alpha_F],\quad
\alpha_F=1+89460y_F.
}
\tag{731.3}
$$

Here $Q_n$ is the original compatible $q$ prime of $M_n$.
The equalities are in completed ordinary multiplicative and
full-divisor modules. Its coordinates are not evaluated.

## 1. Ordinary modules and the previously proved exact inputs

Set

$$
\mathcal O=\mathbf Z_{43}[i],\qquad k=\mathcal O/p,\qquad
R_\Gamma=\mathcal O[\Gamma]/(N_\Gamma)
=\mathcal O[\zeta_p].
$$

For each field $V$, use

$$
\mathscr K_V=(V^\times\otimes\mathcal O)_{\chi^-},\qquad
E_V=(\mathcal O_V^\times\otimes\mathcal O)_{\chi^-},
$$
$$
D_V=(\operatorname{Div}_{\mathrm{fin}}V\otimes\mathcal O)_{\chi^-},
\qquad
\mathscr P_V=\operatorname{div}(\mathscr K_V),\qquad
A_V=(\operatorname{Cl}(V)\otimes\mathcal O)_{\chi^-}.
$$

All multiplicative groups are written additively after completion.
Thus $\mathscr P_V$ means full principal divisors, not divisors
with primes outside a selected set removed. Flat completion
and the integral prime-to-$p$ character idempotent preserve the
ordinary exact sequences.

R686 proves at every level, with actual compatible Robert
ancestors,

$$
E_{B_n}=\mathcal O[S_n,T_n]u_n,\qquad A_{B_n}=0,
$$
$$
E_{F_{t,n}}=\mathcal O[T_n]u_{t,n},\qquad A_{F_{t,n}}=0.
\tag{731.4}
$$

The fixed marked prime $q$ splits in every $F_{t,n}/F$,
and its residue degree in $B_n/F$ is $r=p^n$. The precise
reason is the equality of endomorphisms
$\operatorname{Fr}_q^2=[-q]$, not just a congruence at the
first level. In the compatible scalar subgroup,

$$
\operatorname{Fr}_{K_q}=s_\infty^{a_q^{\mathrm{sc}}},
\qquad
a_q^{\mathrm{sc}}\in\mathbf Z_p^\times,\qquad
a_q^{\mathrm{sc}}\equiv32\pmod p.
\tag{731.5}
$$

Its anti-scalar component is zero at every level. The extension
$M_n/B_n$ is totally ramified of degree $p$ at all $q$ primes,
split above $p$ and $2$, and unramified elsewhere.

R718 supplies the endpoint and the exact scalar norm valuation:

$$
A_{M_n}=R_\Gamma/\pi^{42n+1},\qquad
N_{S_n}A_{M_n}=\pi^{42n}A_{M_n}\ne0.
\tag{731.6}
$$

In particular $A_{M_n}^\Gamma$ is the one-dimensional
$k$-line $\pi^{42n}A_{M_n}$.

## 2. The actual q class generates the whole ambiguous line

Let

$$
e_n=[P_+Q_n]\in A_{M_n}.
$$

The prime $Q_n$ is fixed by $\Gamma$, since $\Gamma$ is
the full inertia group at this $q$ prime. We prove that
$e_n$ is nonzero. Mere nonvanishing of the abstract socle
in (731.6) would not establish this.

Use the actual positive Frobenius lift from R686,
(686.26)-(686.27), in the ordinary Hilbert class extension
and its $\chi^-$ quotient. In its semidirect-product
coordinates it is

$$
f=(c,s^{a_q^{\mathrm{sc}}}),
\qquad \varphi_n(c)=32,
\tag{731.7}
$$

where $\varphi_n:A_{M_n}\twoheadrightarrow k$ is the
original strict-$p$ genus quotient. It factors through
$A_{M_n}/\pi A_{M_n}$. Thus $c$ has nonzero image
modulo $\pi$, and generates the cyclic
$R_\Gamma$-module $A_{M_n}$.

The residue field at $Q_n$ is $\mathbf F_{q^{2r}}$.
Consequently the positive Frobenius in the unramified
Hilbert extension over $M_n$ is $f^r$. Since
$a_q^{\mathrm{sc}}$ is a unit modulo $r$, its class
coordinate is exactly

$$
\sum_{j=0}^{r-1}s^{j a_q^{\mathrm{sc}}}c
=N_{S_n}c.
\tag{731.8}
$$

Multiplying a chosen Frobenius lift by tame inertia does
not alter this class: the inertia has order $p$, commutes
with the lifted Frobenius here, and $p$ divides $r$.
Applying the unchanged projector gives

$$
e_n=44\,N_{S_n}c.
\tag{731.9}
$$

The factor $44$ is a unit in $\mathcal O$. By (731.6)
and the primitivity of $c$, this is a nonzero generator
of $\pi^{42n}A_{M_n}$. Therefore

$$
\boxed{
A_{M_n}^{\mathrm{st}}=A_{M_n}^{\Gamma}
=k e_n.
}
\tag{731.10}
$$

Here $A^{\mathrm{st}}$ denotes the classes represented
by $\Gamma$-invariant full divisors. The first inclusion
holds because $P_+Q_n$ itself is such a divisor; its
nonzero class already fills the whole ambiguous line.
This is the step that rules out an extra ordinary
norm obstruction.

## 3. The exact ambiguous-class and principal-divisor sequences

Write $M=M_n$ and $B=B_n$ for this section. The full
ordinary sequence is

$$
0\longrightarrow\mathscr P_M\longrightarrow D_M
\longrightarrow A_M\longrightarrow0.
\tag{731.11}
$$

The group $D_M$ is a direct sum of permutation lattices.
For each stabilizer $H\le\Gamma$,
$H^1(H,\mathcal O)=\operatorname{Hom}(H,\mathcal O)=0$.
Shapiro's lemma, direct sums, and the character projection
therefore give $H^1(\Gamma,D_M)=0$. Taking invariants
in (731.11) yields the exact sequence

$$
0\longrightarrow A_M^{\mathrm{st}}
\longrightarrow A_M^\Gamma
\longrightarrow H^1(\Gamma,\mathscr P_M)
\longrightarrow0.
\tag{731.12}
$$

Thus (731.10) proves

$$
H^1(\Gamma,\mathscr P_M)=0.
\tag{731.13}
$$

For completeness the full ramified-divisor sequence is

$$
0\longrightarrow H^1(\Gamma,E_M)
\longrightarrow D_M^\Gamma/jD_B
\longrightarrow A_M^{\mathrm{st}}
\longrightarrow0.
\tag{731.14}
$$

Indeed Hilbert 90 applied to
$0\to E_M\to\mathscr K_M\to\mathscr P_M\to0$
identifies
$\mathscr P_M^\Gamma/j\mathscr P_B$ with
$H^1(\Gamma,E_M)$. Since $A_B=0$, the induced map to
$D_M^\Gamma/jD_B$ is injective and has the displayed
cokernel. The quotient $D_M^\Gamma/jD_B$ is precisely

$$
k[T_n].
\tag{731.15}
$$

Only the $q$ primes contribute: they have ramification
index $p$, and their distinct primes after the
$\Delta$ projection are indexed by $T_n$.
All other finite divisors descend with ramification
index one. Under (731.15), the class map is
$f(T)\mapsto f(1)e_n$, because $T_n$ acts trivially
on the socle in (731.10). Hence one also obtains the
actual module identification

$$
H^1(\Gamma,E_M)\simeq (T-1)k[T_n].
\tag{731.16}
$$

No quotient by outside-support classes occurs in any
of (731.11)-(731.16).

## 4. Why every normic ordinary unit is an ordinary unit norm

The multiplicative sequence and Hilbert 90 give an
injection

$$
H^1(\Gamma,\mathscr P_M)
\hookrightarrow H^2(\Gamma,E_M)
\longrightarrow H^2(\Gamma,\mathscr K_M).
$$

The invariant lattices are $E_M^\Gamma=E_B$ and
$\mathscr K_M^\Gamma=\mathscr K_B$.
Cyclic cohomology therefore identifies the kernel of
the last map as

$$
H^1(\Gamma,\mathscr P_M)
=
\frac{E_B\cap N_\Gamma\mathscr K_M}
     {N_\Gamma E_M}.
\tag{731.17}
$$

This equality follows from the ordinary exact
sequence. It is not a replacement of ordinary units
by unrestricted global elements.

Combining (731.13) and (731.17) proves the exact
integral equality

$$
\boxed{
N_\Gamma E_M=E_B\cap N_\Gamma\mathscr K_M.
}
\tag{731.18}
$$

The Hilbert 90 and cohomology calculations remain
valid after the completion used here. Finite-group
cohomology is computed by complexes of finite sums,
flat tensoring preserves their kernels and images,
and the $\Delta$ idempotent commutes with the maps.
Thus no finite denominator or torsion quotient is
lost at this step.

## 5. The full q-local norm map and its integral kernel

At the original marked prime of $F_{t,n}$, retain
R686's exact inverse-power convention

$$
A_n(T)=
\sum_{j=0}^{r-1}\ell(t^j u_{t,n})T^{-j}
\in k[T_n],\qquad
\ell(v)=\log_\zeta
 \bigl(\bar v^{(q^2-1)/p}\bigr).
\tag{731.19}
$$

R686 proves from actual norm compatibility with the
R198 unit, at every $n$,

$$
A_n(1)=0,\qquad A_n'(1)=-13i,\qquad
A_n(T)=(T-1)v_n(T),\quad v_n\in k[T_n]^\times.
\tag{731.20}
$$

Now the residue field at the corresponding prime of
$B_n$ is $\mathbf F_{q^{2r}}$. Define its order-$p$
norm obstruction logarithm by

$$
\ell_{B_n}(z)=
\log_\zeta\bigl(\bar z^{(q^{2r}-1)/p}\bigr).
$$

For the unramified scalar extension at $q$, the
residue-field norm proves the exact identity

$$
\ell_{B_n}(z)=
\ell\bigl(N_{S_n}z\bigr).
\tag{731.21}
$$

There is no extra factor $r$ in this identity.
For an element already in the lower field, the
norm on the right does of course raise it to
the $r$th power; this distinction must be retained.

The tame totally ramified $\Gamma$ extension has
degree $p$. A local unit is a norm if and only if
its residue is a $p$th power. The norm on principal
units is onto, since their residue characteristic
is $q\ne p$. Thus the complete character-valued
local obstruction module is $k[T_n]$.

The action of $S_n$ on this order-$p$ obstruction
is trivial. By (731.4), (731.19), and (731.21),
the exact map on all ordinary base units is

$$
\rho_n:
\mathcal O[S_n,T_n]u_n\longrightarrow k[T_n],
\qquad
h(s,t)u_n\longmapsto\bar h(1,T)A_n(T).
\tag{731.22}
$$

Put $z=T-1$. Since $r=p^n$,

$$
k[T_n]=k[z]/(z^r),\qquad
N_{T_n}=z^{r-1}\quad\hbox{in }k[T_n].
$$

Equation (731.20) gives

$$
\operatorname{Ann}_{k[T_n]}(A_n)
=(z^{r-1})=(N_{T_n}).
\tag{731.23}
$$

The kernel of reduction and scalar augmentation
$\mathcal O[S_n,T_n]\to k[T_n]$ is $(p,s-1)$.
Taking the full inverse image of (731.23) therefore
gives the exact integral kernel

$$
\ker\rho_n=(p,s-1,N_{T_n})E_{B_n}.
\tag{731.24}
$$

At $p$ and $2$, $\Gamma$ is split. At every other
finite place except $q$ it is unramified, so all local
units are norms. There are no real places.
The cyclic Hasse Norm theorem, tensored with the
flat ring $\mathcal O$ and projected to the same
character, consequently gives

$
E_{B_n}\cap N_\Gamma\mathscr K_{M_n}=\ker\rho_n.
\tag{731.25}
$$

Combining (731.18), (731.24), and (731.25) proves
(731.1). Dividing the complete free base lattice
by this ideal gives (731.2). Equivalently, the
actual residue map identifies that quotient with
the ideal $(T-1)k[T_n]$ by multiplication by
the unchanged $A_n(T)$.

In particular both ordinary cyclic cohomology
groups have $k$-dimension $p^n-1$:

$$
H^1(\Gamma,E_{M_n})\simeq (T-1)k[T_n],\qquad
H^2(\Gamma,E_{M_n})\simeq k[T_n]/(N_{T_n}).
\tag{731.26}
$$

## 6. An exactly normalized global q-principalization after scalar base change

The element $e_n$ in (731.9) is killed by $p$ and is
fixed by $T_n$. Hence

$$
[N_{T_n}P_+Q_n]=p^n e_n=0
\quad\hbox{in }A_{M_n}.
$$

The full completed divisor sequence supplies a
global $q$-unit $Z_n^0$ with

$$
\operatorname{div}Z_n^0=N_{T_n}P_+Q_n.
\tag{731.27}
$$

Its norm divisor to $B_n$ is exactly the extension
of $\operatorname{div}A_\alpha=P_+P_F$.
The reason is that $\Gamma$ is totally ramified
with residue degree one, while the $T_n$ translates
are exactly the distinct primes of $B_n$ above
the marked $q$ prime of $F$. Therefore

$$
N_\Gamma Z_n^0=A_\alpha+v_n^0,\qquad
v_n^0\in E_{B_n}.
\tag{731.28}
$$

We now pay the norm correction in ordinary units.
First $A_\alpha$ is an unrestricted global
$\Gamma$ norm after this scalar base change.
At a $q$ completion of $B_n$, its local
reciprocity value in $\Gamma$ is obtained by
taking the norm down to the $q$ completion of
$F$. The element $A_\alpha$ comes from $F$,
and that unramified degree is $r=p^n$.
The resulting character value is $r$ times
the base value, which is zero in the order-$p$
group $\Gamma$. This applies also to the
valuation term; it is not merely a unit-residue
test. At $p,2$ the extension is split, and at
all remaining places $A_\alpha$ is a unit in
an unramified extension. The cyclic Hasse Norm
theorem gives

$$
A_\alpha\in N_\Gamma\mathscr K_{M_n}.
\tag{731.29}
$$

Both terms on the left of
$v_n^0=N_\Gamma Z_n^0-A_\alpha$ are field norms.
Thus $v_n^0$ lies in the intersection in
(731.18). By that equality there is an
**ordinary unit** $e_n^0\in E_{M_n}$ with
$N_\Gamma e_n^0=v_n^0$.
Set $Z_n=Z_n^0-e_n^0$.
This retains the entire divisor (731.27)
and makes its norm exactly $A_\alpha$,
proving (731.3).

All solutions of (731.3) form the precise
ordinary torsor

$$
Z_n+\ker(N_\Gamma:E_{M_n}\to E_{B_n}).
\tag{731.30}
$$

Indeed equal full divisors force the difference
to be an ordinary unit, and the equal norms
force it into this kernel; the reverse
inclusion is immediate. This is a global
existence and exact normalization result,
not a choice of arbitrary local roots.

It also gives the true ordinary identities

$$
pZ_n-A_\alpha\in\ker N_\Gamma E_{M_n},
$$
$$
N_{S_n}Z_n-p^{n-1}A_\alpha
\in\ker N_\Gamma E_{N_n}.
\tag{731.31}
$$

For the first, the extension of the base
$q$ divisor to $M_n$ has ramification index
$p$, hence $\operatorname{div}A_\alpha
=pN_{T_n}P_+Q_n$.
For the second, the scalar extension is
unramified of residue degree $p^n$ at $q$,
whereas $A_\alpha$ in $N_n$ has divisor
$pN_{T_n}P_+Q_{N_n}$. Norm compatibility
then proves both zero $\Gamma$-norms.

## 7. Level one and the remaining marked numerical problem

At $n=1$ the statement reads

$$
N_\Gamma E_M=(p,s-1,N_T)E_B,
\qquad E_B=\mathcal O[S,T]u_B.
$$

The generators $pu_B$, $(s-1)u_B$, and
$N_Tu_B=u_s$, together with their
$\mathcal O[S,T]$ translates, therefore
have actual ordinary $\Gamma$-norm
preimages in $M$. This assertion is in
the full field $M$; it does not assert
that a preimage of $u_s$ lies in the
smaller $T$-fixed field.

The first generator has the evident
preimage $u_B$. For the second, the
original ancestor itself provides one:
R613 has
$N_\Gamma c_B=(1-s^{11})u_B$.
The element $1+s+\cdots+s^{10}$ is a
unit of the local group ring
$\mathcal O[S]$, because its augmentation
is $11$. Thus
$-(1+s+\cdots+s^{10})^{-1}c_B$
is an ordinary completed preimage of
$(s-1)u_B$. The theorem proves existence
for the third generator without assigning
a numerical coordinate to it.

Equation (731.3) at this level retains
the original $A_\alpha$, the original
prime label and the full ordinary
divisor. It supplies another concrete
global norm torsor for the ongoing
comparison with the marked $X_t$ in
$F_t$. It does not evaluate either
principalization, the original moment
$J_\ell$, or the mixed ordinary chain
coefficient $b$.

In particular the already proved
$C=9ib$ and
$\Omega_2=\varepsilon(22+17b)$
still require the actual $b$.
No one-dimensional module comparison,
pure-$p$ reference value, or local norm
choice is substituted for it.

## Dependencies

- [R686](R686-all-p-power-layers-and-exact-ordinary-class-growth-law.md):
  the actual higher fields, Frobenius, ordinary Robert
  lattices, exact norm compatibility, and unchanged
  residue derivative.
- [R718](R718-all-ordinary-class-lengths-and-exact-universal-unit-norms.md):
  the full endpoint $42n+1$ and the actual
  $S_n$-norm valuation $42n$.
- [R619](R619-ordinary-anti-p-class-group-and-actual-artin-nine.md):
  the original ordinary divisor and principal-norm
  conventions and the fixed value $-13i$.
- [R613](R613-mixed-p-capitulation-and-the-exact-34-boundary.md):
  the same original mixed ancestor and
  $N_\Gamma c_B=(1-s^{11})u_B$.
- [R720](R720-original-C-and-b-by-the-complete-Robert-chain-comparison.md):
  the original $C/b$ bridge whose numerical input
  is not supplied here.
- J. S. Milne, *Class Field Theory*, Chapters II--III for
  cyclic cohomology and local reciprocity; the section
  "The local-global principle for norms and quadratic forms",
  Theorem 3.1 (printed p. 234), for the cyclic Hasse Norm theorem,
  <https://www.jmilne.org/math/CourseNotes/CFT.pdf>.
