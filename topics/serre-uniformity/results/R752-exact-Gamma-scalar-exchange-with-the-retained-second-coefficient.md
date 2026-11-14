# R752: exact Gamma/scalar exchange with the retained second coefficient

Date: 2026-11-14. **Status: proved.** This result compares the actual
ordinary Hilbert first jet with the actual finite-flat pure-$p$
primitive. It retains, and precisely identifies, the second scalar
coefficient and the remaining global Gamma/scalar invariant. It does
not evaluate $J_\ell$, $b$, or those two additional quantities, and
does not assert the unproved R723 comparison between $J_\ell-18$
and $b-24$.

Use the original $p=43$, $q$, CM and Weil markings, positive arithmetic
Artin convention, and all original units of R561/R720. Put

$$
\Sigma=\{2,p,q,\infty\},\qquad
d_{\rm fl}=d_q-8d_0,\qquad J_{\rm fl}=J_\ell-18.
$$

The scalar group is still denoted $S=\langle s\rangle$; it is
different from the support set $\Sigma$.

The original ordinary class module and marked first actions are

$$
A=A_M=R_\Gamma/\pi^{43},\qquad
\pi=\gamma-1,\qquad
s_{\rm act}=1+i\pi\pmod{\pi^2},\qquad
t_{\rm act}=1+b\pi\pmod{\pi^2}.
$$

There is an intrinsic $\sigma_2\in\mathbf F_{43}$ defined by

$$
s_{\rm act}
=1+i\pi+\left(\sigma_2-\frac{1+i}{2}\right)\pi^2
\pmod{\pi^3}.
\tag{752.1}
$$

Let $D_0$ be any $\Sigma$-supported primitive

$$
\delta D_0=(-\ell_{\rm cyc}-2i\kappa_q)\cup w.
\tag{752.2}
$$

Sections 2--3 define an affine local functional
$\mathscr L_q(D_0)$ using the exact local quadratic primitive.
It agrees with $2(a-16c)$ on differences which are local
cocycles of finite/singular coordinates $(a,c)$. Define

$$
I_0=
\mathscr L_q(D_0)
-\frac{20}{23}
 \langle[D_{0,p}],d_{{\rm fl},p}\rangle_p.
\tag{752.3}
$$

This is independent of every choice of the supported primitive,
of its cochain representative, and of the local normalization
used in its definition. The exact exchange formula is

$$
\boxed{I_0=\varepsilon\bigl(21\sigma_2+2bJ_{\rm fl}\bigr).}
\tag{752.4}
$$

All factors in this identity use the original rational local
coordinates. In particular the factor $32$ below already uses
the positive Frobenius of $\mathbf Q_{q^2}$.

## 1. The genuine second scalar coefficient

Since $p$ has $\pi$-valuation $42$, the quotient $A/\pi^3A$
is $k[\pi]/\pi^3$, where $k=\mathbf F_{43^2}$.
The action of $s$ commutes with $\Gamma$, so is multiplication
by an intrinsic element of this commutative ring. Write

$$
s_{\rm act}=1+i\pi+a_2\pi^2.
$$

Changing the cyclic class generator does not change this scalar
action. Complex conjugation conjugates $k$, sends
$\gamma$ to $\gamma^{-1}$, and fixes the scalar group generator
$s$. Thus

$$
\tau(\pi)=-\pi+\pi^2\pmod{\pi^3}.
$$

Applying $\tau$ to $s_{\rm act}$ gives

$$
1+i\pi+(\bar a_2-i)\pi^2.
$$

It follows that

$$
a_2-\bar a_2=-i.
\tag{752.5}
$$

Consequently

$$
\sigma_2=a_2+\frac{1+i}{2}\in\mathbf F_{43},
$$

which proves (752.1). Equivalently, in the degree-two truncated
formal logarithm, put

$$
\lambda=\pi-\frac{\pi^2}{2}.
$$

Then

$$
\log(s_{\rm act})=i\lambda+\sigma_2\lambda^2
\pmod{\pi^3}.
\tag{752.6}
$$

The logarithms in (752.6) are polynomials in the characteristic-$p$
quotient, with denominators at most $2$. They are not the
$p$-adic logarithm of the torsion element $\gamma$ in
$R_\Gamma$. No equality $s=\gamma^i$ in the complete class
module is asserted. In particular (752.5) fixes the imaginary
part of $a_2$, and does not set $\sigma_2$ to zero.

## 2. A rational local quadratic primitive

At $q$, identify the original primal coefficient module with
$k$, with $F_0=1$, $K_0=i$, and rational Frobenius acting by
conjugation on $k$. Let

$$
v_q=\kappa_S+i\kappa_q,
\qquad \ell_{\rm cyc}=2\kappa_S.
$$

Here $\kappa_S(s)=1$, $\kappa_q(\gamma)=1$, and the original
real q-ray normalization has no unramified $\Gamma$ component.
For the positive quadratic Frobenius $f$ and positive marked
tame inertia $x$,

$$
v_q(f)=32,\qquad v_q(x)=i.
\tag{752.7}
$$

The original local class $w_q=(-16\varepsilon,-\varepsilon)$
is represented by

$$
w_q^0=-\varepsilon v_q.
$$

The identity is compatible with rational descent: $\kappa_S$
is invariant, $\kappa_q$ has the anti character, and multiplying
the latter by $i$ gives exactly the conjugation action on the
$K_0$-line.

Write

$$
\mathcal B_0=-\ell_{\rm cyc}-2i\kappa_q=-2v_q.
$$

It acts on the local coefficient algebra by multiplication.
Multiplication $k\otimes k\to k$ is equivariant for conjugation.
Therefore the rational local $1$-cochain

$$
\mathfrak q(g)=-\varepsilon\,v_q(g)^2
\tag{752.8}
$$

satisfies

$$
\delta\mathfrak q
=2\varepsilon\,v_q\cup v_q
=\mathcal B_0\cup w_q^0.
\tag{752.9}
$$

This follows by expanding
$(v_q(g)+g v_q(h))^2$ in the inhomogeneous coboundary.
It includes the Galois action on the second factor.

It is not necessary that the globally selected cocycle $w$,
already normalized to vanish at $p$, have precisely this
representative at $q$. Choose a local $0$-cochain $h$ with

$$
w_q=w_q^0+\delta h.
$$

If a global cochain $D$ satisfies
$\delta D=\mathcal B_0\cup w$ locally at $q$, put

$$
D_q^0=D_q+\mathcal B_0\cup h.
$$

The Leibniz sign for a degree-one cochain gives
$\delta(\mathcal B_0\cup h)=-\mathcal B_0\cup\delta h$.
Hence $D_q^0-\mathfrak q$ is a rational local cocycle.

For a rational local class $r$ of coordinates $(a,c)$, set

$$
\Lambda_q(r)=2(a-16c).
\tag{752.10}
$$

Define the promised affine functional by

$$
\mathscr L_q(D)=
\Lambda_q([D_q^0-\mathfrak q]).
\tag{752.11}
$$

Changing $h$ by an invariant local $0$-cochain changes
$D_q^0-\mathfrak q$ by a multiple of $w_q^0$. Its
$\Lambda_q$ value is zero. Thus (752.11) is independent of
the local gauge.

There is also a useful direct evaluation which avoids choosing
$h$. On the quadratic local group the residual module is
trivial. If $r$ is a rational cocycle, restriction gives

$$
r(f)=2a,\qquad r(x)=ic,
$$

so

$$
\Lambda_q(r)=r(f)+32i\,r(x).
\tag{752.12}
$$

For any $h\in k$, not only an invariant one, the correction
$\mathcal B_0h$ has values $-64h$ and $-2ih$ at $f$ and $x$.
Their contribution to (752.12) is

$$
-64h+32i(-2ih)=0.
$$

Thus (752.11) can be computed directly on the quadratic
restriction of $D-\mathfrak q$. Its value is in $\mathbf F_{43}$
because the gauge-corrected cocycle is rational.
This proves rational descent without suppressing a local
coboundary or making a second division by $2$.

## 3. The invariant $I_0$ is a full global quotient

R743 gives the complete supported primal space

$$
H^1(G_{\mathbf Q,\Sigma},W)
=\mathbf F_{43}c_p^{\rm Rob}\oplus\mathbf F_{43}w.
\tag{752.13}
$$

The actual values needed here are

$$
\begin{array}{c|cc}
&\Lambda_q&\langle\,\cdot\,,d_{{\rm fl},p}\rangle_p\\ \hline
c_p^{\rm Rob}&20&23\\
w&0&0 .
\end{array}
\tag{752.14}
$$

Indeed $(c_p^{\rm Rob})_q=(10,0)$, whereas
$w_q=(-16\varepsilon,-\varepsilon)$.
At $p$ the original functional of $c_p^{\rm Rob}$ is
$(6,10)$ and $d_{{\rm fl},p}=(0,41)$, giving
$10\cdot41=23$ modulo $43$. The strict-$p$ class $w$
has zero localization.

Two choices of $D_0$ in (752.2) differ, up to a coboundary,
by a unique linear combination of these two classes.
The two changes in (752.3) cancel for $c_p^{\rm Rob}$
by (752.14), and both are zero for $w$. Coboundaries
have zero local class. Together with §2, this proves
all the choice independence asserted for $I_0$.

Explicitly, put

$$
D_0^{\rm fl}
=D_0-\frac{\langle[D_{0,p}],d_{{\rm fl},p}\rangle_p}{23}
             c_p^{\rm Rob}.
\tag{752.15}
$$

It has the same support and differential as $D_0$, its
$p$ localization lies in the actual line $L_{\rm fl}$, and

$$
I_0=\mathscr L_q(D_0^{\rm fl}).
\tag{752.16}
$$

Any two such flat-normalized primitives differ by a multiple
of $w$, modulo coboundaries. Thus $I_0$ is a specific
global Gamma/scalar secondary invariant, rather than a
coordinate chosen arbitrarily in a one-dimensional local
space.

## 4. The full ordinary q decomposition reads $\sigma_2$

Use the actual ordinary Hilbert extension and the tame-fixed
splitting of R657, with the full conjugate pair of characters
before taking the indicated component. Its class-field
cocycle modulo $\pi^2$ is

$$
g=g_0+\pi g_1,\qquad
g_0=-\bar w/\varepsilon.
$$

R746 identifies the original strict-$p$ primitive as

$$
D_b=-2\varepsilon i\,\bar g_1.
\tag{752.17}
$$

The original q decomposition has marked inertia
$x=(a,\gamma)$ and positive Frobenius
$f=(c,s^{32})$, with genus values

$$
g_0(x)=-i,\qquad g_0(f)=32.
\tag{752.18}
$$

The ordinary Hilbert extension is unramified over $M$,
so $x$ has order $p$. The local tame relation therefore
gives $fxf^{-1}=x^{q^2}=x$.

R731 proves that the relative Frobenius class of the
original q prime is in $\pi^{42}A$, and is nonzero there.
In particular it vanishes modulo $\pi^3$. This is exactly
what is needed here; it does not determine a first-jet
cochain by itself.

Put $z=f^{39}$. Its quotient is $s$, since
$32\cdot39=1+29p$, and $z^{32}=f$ modulo
$\pi^3 A$ because $f^p$ lies in the q socle.
Write, in the class-field coordinates,

$$
g(x)=-i+\pi A_1+O(\pi^2),\qquad
g(z)=1+\pi B_1+O(\pi^2).
$$

The exact commutation of $x$ and $z$, computed one order
higher in the full class module, gives

$$
\pi g(z)=(s_{\rm act}-1)g(x).
$$

Its coefficient of $\pi^2$ is

$$
\boxed{B_1=iA_1-ia_2.}
\tag{752.19}
$$

No term $a_2$ can be discarded from this identity.

On the quadratic local group,

$$
g_0=\kappa_S-i\kappa_q,\qquad
\kappa_q+i\kappa_S=ig_0.
$$

The differential of $g_1$ is consequently
$-ig_0\cup g_0$. Set

$$
r=g_1-\frac{i}{2}g_0^2.
$$

The positive characteristic-$p$ quadratic identity shows
that $r$ is an additive local cocycle. At the two marked
elements,

$$
r(x)=A_1+\frac i2,\qquad
r(z)=B_1-\frac i2.
$$

Using (752.19) gives the exact cancellation

$$
r(x)+i\,r(z)
=a_2+\frac{1+i}{2}
=\sigma_2.
\tag{752.20}
$$

This equality does not require choosing $A_1$ to be real
or setting either local linear term to zero. If one makes
an additional conjugation-compatible choice, one may write
$A_1=h-i/2$ with $h\in\mathbf F_{43}$; then
$r(x)=h$, $r(z)=i(h-\sigma_2)$.
The calculation (752.20) shows directly why $h$ cancels.

The primal quadratic cochain (752.8) satisfies

$$
\mathfrak q
=-2\varepsilon i\,
 \overline{\left(\frac{i}{2}g_0^2\right)}
$$

on the quadratic group. Thus the cocycle part of
$D_b-\mathfrak q$ is $-2\varepsilon i\,\bar r$.
Since $r(f)=32r(z)$, formula (752.12) yields

$$
\begin{split}
\mathscr L_q(D_b)
&=-64\varepsilon i\,\overline{r(z)}
  +64\varepsilon\,\overline{r(x)}\\
&=64\varepsilon\,
  \overline{r(x)+i r(z)}\\
&=\boxed{21\varepsilon\sigma_2}.
\end{split}
\tag{752.21}
$$

Section 2 proves that any needed rational local
$0$-cochain correction contributes zero to this expression.
Changes of the normalized global class generator or the
strict-$p$ primitive likewise add only a multiple of $w$
at this stage, by R746 and (752.13).
Equation (752.21) is therefore an intrinsic statement with
the original markings.

## 5. The exact global exchange

Let $B_p^{\rm fl}$ be the original pure-$p$ primitive
constructed and flat-normalized in R743. It has

$$
\delta B_p^{\rm fl}=(-i\kappa_p)\cup w,\qquad
[B_{p,p}^{\rm fl}]\in L_{\rm fl},
$$

and the two proved values

$$
\Lambda_q(B_p^{\rm fl})=-\varepsilon J_{\rm fl},
\qquad
\langle[B_{p,p}^{\rm fl}],d_{0,p}\rangle_p
=-13\varepsilon.
\tag{752.22}
$$

The first uses the original cochain identity
$\kappa_p|_{G_q}=0$, so $B_p^{\rm fl}$ is a local cocycle
at $q$. The second is the original supported secondary
reciprocity calculation using R198's value $28K_0$.

R746 gives

$$
\langle[D_{0,p}],d_{0,p}\rangle_p=26\varepsilon b.
$$

Subtracting the $c_p^{\rm Rob}$ term in (752.15) does not
change this value: the original pairing of
$c_p^{\rm Rob}$ with $d_0$ is
$6\cdot24+10\cdot20=0$ modulo $43$.
Therefore

$$
E_b=D_0^{\rm fl}+2bB_p^{\rm fl}
\tag{752.23}
$$

has the same differential as the ordinary $D_b$ of R746,
and its $p$ localization annihilates both $d_{0,p}$
and $d_{{\rm fl},p}$. The first pairing is
$26\varepsilon b+2b(-13\varepsilon)=0$.
The second is zero because both summands in (752.23)
are flat-normalized.

The actual dual vectors

$$
d_{0,p}=(24,20),\qquad d_{{\rm fl},p}=(0,41)
$$

have determinant $38\ne0$. By the perfect local Tate
pairing, the $p$ class of $E_b$ is therefore zero.
This is a statement about two specified local functionals,
not an identification of two unspecified scalar spaces.

It follows that $E_b-D_b$ is a supported global cocycle
with zero $p$ localization. By (752.13) it is a multiple
of $w$, modulo a coboundary. Apply $\mathscr L_q$:

$$
\begin{split}
\mathscr L_q(D_b)
&=\mathscr L_q(E_b)\\
&=I_0+2b\Lambda_q(B_p^{\rm fl})\\
&=I_0-2b\varepsilon J_{\rm fl}.
\end{split}
$$

Combining this with (752.21) proves (752.4).
Every cochain adjustment used here preserves $\Sigma$.
No field norm is substituted for an ordinary unit norm,
and no auxiliary genus normalization is substituted for
the original $w$.

## 6. Exact scope and boundary cases

The identity holds also when $b=0$: then it says
$I_0=21\varepsilon\sigma_2$ and gives no information
about $J_{\rm fl}$. No division by $b$ was made.

At the obstruction's comparison value $b=24$, it reads

$$
I_0/\varepsilon=21\sigma_2+5J_{\rm fl}.
$$

Thus $b=24$ does not, from the results proved here,
imply $J_{\rm fl}=0$. One would still need a genuine
global evaluation or identity for $I_0$ and $\sigma_2$.
Conversely a vanishing $J_{\rm fl}$ only gives
$I_0=21\varepsilon\sigma_2$ from this exchange formula.

The q socle and the complete ordinary class lengths do
not supply the missing value of $\sigma_2$. At every
level they constrain the leading scalar action; the
scalar generators in the growing tower have increasing
orders. The inverse-limit scalar generator is not an
order-$p$ automorphism of $R_\Gamma$. Therefore one
cannot replace its action by a $p$-torsion scalar in
$R_\Gamma$ and infer $\sigma_2=0$.

R749 evaluates a different, already fixed quantity,
$\langle z_0,d_{0,p}\rangle_p=9\varepsilon$.
That exact reference value does not identify the
Gamma/scalar flat invariant (752.3), and it has not
been used to remove either term in (752.4).

## Dependencies

- [R657](R657-full-ordinary-class-module-and-exact-scalar-norm-criterion.md),
  §5: the actual tame-fixed Hilbert splitting, original q
  inertia/Frobenius, and marked scalar coefficient $i$.
- [R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md)
  and [R718](R718-all-ordinary-class-lengths-and-exact-universal-unit-norms.md):
  the complete ordinary class module and its tower.
- [R731](R731-complete-ordinary-Gamma-norms-and-marked-q-principalizations.md),
  §2: the genuine original q Frobenius class in the socle.
- [R743](R743-original-first-moment-and-the-exact-flat-primal-secondary-slope.md):
  complete supported spaces, the actual flat primitive, and
  its first-moment quotient.
- [R746](R746-original-ordinary-coefficient-as-a-strict-p-bockstein-condition.md):
  the strict-$p$ ordinary first jet, cochain normalization,
  and its original $d_0$ functional.
- [R749](R749-original-scalar-primitive-and-the-exact-reference-pairing.md):
  the separately evaluated scalar reference pairing and
  the retained difference from the ordinary/flat comparison.

