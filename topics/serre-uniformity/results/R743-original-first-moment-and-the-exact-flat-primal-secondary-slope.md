# R743: the original first moment and the exact flat primal secondary slope

Date: 2026-11-14. **Status: proved.** Fix the original $p=43$,
$q$, CM and Weil markings, positive Artin convention, and
$S=\{2,p,q,\infty\}$ of R171/R185/R196/R200. This result identifies
the reconstructed first moment with a specified primal cup primitive
after imposing the actual finite-flat condition at $p$. It does not
identify that primitive with the ordinary class-action coefficient
$b$ of R720 and does not evaluate either scalar.

Write $d_0=d_p^{\rm Rob}$ and retain the original class $d_q$.
The actual finite-flat dual class is

$$
\widetilde d_q=d_q-8d_0,
\qquad J_{\rm fl}=J_\ell-18.
\tag{743.1}
$$

Let $w$ be R200's original strict-$p$ primal class. With the same
nonzero Tate sign $\varepsilon$, its $q$ coordinates are

$$
(a_q(w),b_q(w))=(27\varepsilon,-\varepsilon)
=(-16\varepsilon,-\varepsilon).
\tag{743.2}
$$

There exists an $S$-supported cochain $\mathfrak b_p(w)$ satisfying

$$
\delta\mathfrak b_p(w)=(-i\kappa_p)\cup w,
\qquad [\mathfrak b_p(w)|_{G_p}]\in L_{\rm fl}.
\tag{743.3}
$$

Here $w|_{G_p}=0$ and the original marked $\kappa_p|_{G_q}=0$
are taken as cochain identities, so the local classes appearing
in (743.3) and below are defined. The exact, choice-independent
formula is

$$
\boxed{
2\bigl(a_q(\mathfrak b_p(w))-16b_q(\mathfrak b_p(w))\bigr)
=-\varepsilon(J_\ell-18).
}
\tag{743.4}
$$

Thus $J_{\rm fl}=0$ is equivalent to the $q$ class of this
finite-flat-normalized pure-$p$ primitive belonging to the original
line $\mathbf F_{43}w_q$. The primitive concerns the original
ramified class $w$. R204's primitive for the different, purely
$\{2,p\}$-supported class $c_p^{\rm Rob}$ is not substituted for it.

## 1. The complete global spaces and supported existence

Set $W=\operatorname{ad}^0 A[p]/\mathbf F_pJ$, with the original
$J=[i]$, and use the trace pairing to identify its Tate dual with
$W(1)$. All cochains below are continuous cochains for
$G_{\mathbf Q,S}$ with these coefficient modules. Let
$S_0=\{2,p,\infty\}$.

The proved minimal-support statements of R161/R163 and R189 are

$$
H^1(G_{\mathbf Q,S_0},W(1))=\mathbf F_p d_0,
\qquad
H^1(G_{\mathbf Q,S_0},W)=\mathbf F_p c_p^{\rm Rob}.
\tag{743.5}
$$

For either coefficient module, the quotient of local $H^1$ at $q$
by its unramified subspace has dimension one. Its coordinate is
the singular coordinate fixed in R168. The kernel of the global
singular-coordinate map consists exactly of classes unramified
also at $q$, hence is the relevant space in (743.5).
The original $d_q$ has singular coordinate $1$. Consequently

$$
\boxed{
H^1(G_{\mathbf Q,S},W(1))
=\mathbf F_p d_0\oplus\mathbf F_p d_q.
}
\tag{743.6}
$$

This proves completeness of the dual space: it is not inferred
merely from the independence of two exhibited local classes.
Likewise $w$ has nonzero singular coordinate $-\varepsilon$, so

$$
\boxed{
H^1(G_{\mathbf Q,S},W)
=\mathbf F_p c_p^{\rm Rob}\oplus\mathbf F_p w.
}
\tag{743.7}
$$

R185 computes the two dual localizations in the same Artin--Hasse
basis $(b_1,b_{45})$:

$$
(d_0)_p=24b_1+20b_{45},\qquad
(d_q)_p=20b_1+29b_{45}.
\tag{743.8}
$$

Their determinant is $38\ne0$ if these two rows are put in this
order, or $5\ne0$ in the opposite order. Combining this with the
complete space (743.6) makes localization at $p$ injective on
$H^1(G_{\mathbf Q,S},W(1))$. In particular

$$
\Sha^1_S(W(1))=0.
$$

The Poitou--Tate perfect pairing between $\Sha^2_S(W)$ and
$\Sha^1_S(W(1))$ therefore gives

$$
\Sha^2_S(W)=0.
\tag{743.9}
$$

This is the direction of duality needed for the primal primitive;
it differs from the dual-primitive direction used in R200.

Use the original anti-cyclotomic character $\kappa_p$ and the
equivariant action

$$
j(\kappa,z)=-i\kappa z.
\tag{743.10}
$$

The class $j(\kappa_p\cup w)$ is locally zero at every place in
$S$. At $p$, $w_p=0$. At $q$, the pure-$p$ anti-cyclotomic
extension is split with the original real marking, so
$\kappa_{p,q}=0$. At $2$, the relevant $H^2$ vanishes by the
same nontrivial inertia and local-duality calculation as in
R189. At infinity, $p$ is odd. Outside $S$ the cochains are
unramified and the unramified local $H^2$ is zero.
Equation (743.9) proves

$$
j(\kappa_p\cup w)=0
\quad\hbox{in }H^2(G_{\mathbf Q,S},W).
$$

Hence a continuous $S$-supported primitive exists. No field-Norm
solution with unspecified outside support is used here.

The cochain conventions can be imposed without changing the
classes. Since $w_p$ is a coboundary and $H^0(\mathbf Q_p,W)=0$,
its killing $0$-cochain is unique. The $q$ normalization of
$\kappa_p$ is the actual real Frobenius splitting used in
R196/R204. Since $w_q\ne0$, an arbitrary different local
$\kappa_p$ gauge is not silently substituted.

## 2. The actual finite-flat correction and the remaining choices

The original R185 result is

$$
L_{\rm fl}^{\perp}=\mathbf F_p b_{45},\qquad
(\widetilde d_q)_p=41b_{45}.
\tag{743.11}
$$

R189 fixes the primal generator without an unknown scale and proves

$$
\bigl(\langle(c_p^{\rm Rob})_p,b_1\rangle_p,
\langle(c_p^{\rm Rob})_p,b_{45}\rangle_p\bigr)=(6,10),
\qquad
(c_p^{\rm Rob})_q=(10,0).
\tag{743.12}
$$

In particular, with the same pairing and the same $d_q-8d_0$,

$$
\langle(c_p^{\rm Rob})_p,(\widetilde d_q)_p\rangle_p
=41\cdot10=23\ne0\quad\bmod43.
\tag{743.13}
$$

For any supported primitive $B$ of (743.10), $B_p$ is a
$1$-cocycle because $w_p=0$. Set

$$
\lambda(B)
=\frac{\langle[B_p],(\widetilde d_q)_p\rangle_p}{23},
\qquad
B^{\rm fl}=B-\lambda(B)c_p^{\rm Rob}.
\tag{743.14}
$$

Then $[B^{\rm fl}_p]\in L_{\rm fl}$. Equivalently the coefficient
in (743.14) is $\langle[B_p],b_{45}\rangle_p/10$, exactly the
original R189 finite-flat correction. This correction changes the
$q$ finite coordinate by $-10\lambda(B)$ and leaves its singular
coordinate unchanged.

Any two supported primitives differ by a global $1$-cocycle. By
(743.7) its cohomology class is $a c_p^{\rm Rob}+b w$. If both
primitives satisfy the finite-flat condition, (743.11)--(743.13)
force $a=0$. Therefore the finite-flat primitives, modulo global
$1$-coboundaries, form an affine torsor under precisely
$\mathbf F_p w$.

Since $\kappa_{p,q}=0$, their restrictions at $q$ are cocycles.
Their images in

$$
H^1(\mathbf Q_q,W)/\mathbf F_p w_q
\tag{743.15}
$$

are identical. The functional

$$
\Lambda_q(a,b)=2(a-16b)
\tag{743.16}
$$

has kernel exactly $\mathbf F_p w_q$ by (743.2). It gives a fixed
coordinate on this actual quotient. Thus the left side of (743.4)
is defined independently of every remaining primitive choice.

## 3. The dual primitive keeps the original moment and the nonzero q class

The restored first-moment note, Section 8, proves using R191's
positive Norm cochain and the original inverse-power convention that
one can take an $S$-supported dual primitive $e$ with

$$
\delta e=j(\kappa_p\cup\widetilde d_q),\qquad
(c_q(e),d_q(e))=\left(\frac{J_\ell-18}{2},0\right).
\tag{743.17}
$$

The factor $-i$ in $j$ and the factor $2$ from quadratic
restriction have both already been included in (743.17).
This is the primitive of the exact same finite-flat target

$$
A_{\alpha,\rm fl}=A_\alpha-\frac{8i}{1848}u,
$$

not a new local root choice. The ordinary norm-zero corrections and
the original $q$ phase were treated in that note and in R736.

The class $\widetilde d_q$ is nonzero at $q$:

$$
(c_q(\widetilde d_q),d_q(\widetilde d_q))=(16,1).
\tag{743.18}
$$

The vanishing $(d_0)_q=0$ does not permit one to erase this
localization. It will supply the first of the two $q$ terms in
the next section.

Adding any global dual class to $e$ does not change its pairing
with $w_q$. Indeed (743.6) gives the two possibilities: $d_0$ has
zero $q$ localization and $d_q$ has coordinates $(16,1)$, which
pair to zero with (743.2). This also follows by full global
reciprocity since $w_p=0$.

## 4. The full secondary reciprocity identity and its sign

Here is the cochain proof, so that no comparison of one-dimensional
spaces is used to fix the scalar or sign. Use the nonhomogeneous
left-action differential. Put $d=\widetilde d_q$, $\kappa=\kappa_p$,
and let $B$ be any primitive satisfying $\delta B=j(\kappa\cup w)$.
Define

$$
A(g,h)=j(\kappa(g),g w(h)),\qquad
R(g,h)=j(g\kappa(h),w(g)),
$$
$$
h_0(g)=j(\kappa(g),w(g)),\qquad
T=j(\kappa\cup d).
$$

Direct expansion gives

$$
\delta h_0=-A-R.
\tag{743.19}
$$

Multiplication by $-i$ has the negative adjoint for the original
trace pairing, as in R200. Consequently

$$
\operatorname{tr}(R\cup d)
=-\operatorname{tr}(w\cup T).
\tag{743.20}
$$

Using $\delta B=A$, $\delta e=T$, and the Leibniz rule, the cochain

$$
\mathcal C
=\operatorname{tr}\bigl(B\cup d+w\cup e+h_0\cup d\bigr)
\tag{743.21}
$$

is a global $2$-cocycle with values in $\mu_p$. Its differential
is $-\operatorname{tr}(R\cup d)-\operatorname{tr}(w\cup T)=0$.

At $p$, the exact zero cochain $w_p=0$ also makes $h_{0,p}=0$,
so the invariant is
$\langle[B_p],d_p\rangle_p$. At $q$, the exact zero cochain
$\kappa|_{G_q}=0$ makes $h_{0,q}=0$ and both $B_q,e_q$ cocycles.
The invariant there is the sum

$$
\langle B_q,d_q\rangle_q+\langle w_q,e_q\rangle_q.
\tag{743.22}
$$

Both terms in (743.22) remain. In particular the first cannot be
removed using the zero localization of the different class $d_0$.

For completeness, at $2$ write $d=\delta t_0$, which is possible
because $H^1(\mathbf Q_2,W(1))=0$. Locally take
$e=-j(\kappa\cup t_0)$. Substitution in (743.21), with the same
Leibniz calculation as R200, gives

$$
\mathcal C_2
=-\delta\operatorname{tr}\bigl((B+h_0)\cup t_0\bigr).
$$

Any other local primitive differs by a cocycle whose $H^1$ at $2$
is zero, so this change does not alter the invariant. The invariant
at infinity vanishes since $p$ is odd. All remaining places have
zero invariant by $S$ support and unramified local cohomology.
Global reciprocity therefore proves the exact identity

$$
\langle[B_p],d_p\rangle_p
+\langle B_q,d_q\rangle_q
+\langle w_q,e_q\rangle_q=0.
\tag{743.23}
$$

This includes the local finite-flat correction, the nonzero
$q$ class $d_q$, all other places, and the negative adjoint sign.

## 5. Substitution in the original coordinates

Take $B=B^{\rm fl}$ of (743.14). Equation (743.11) makes the
first term of (743.23) zero. R168's exact local pairing is

$$
\langle(a,b),(c,d)\rangle_q=2(ad-bc).
\tag{743.24}
$$

Equations (743.18) and (743.24) give

$$
\langle B_q,\widetilde d_{q,q}\rangle_q
=2\bigl(a_q(B)-16b_q(B)\bigr).
$$

Equations (743.2), (743.17), and (743.24) give

$$
\langle w_q,e_q\rangle_q
=2\left(27\varepsilon\cdot0
-(-\varepsilon)\frac{J_\ell-18}{2}\right)
=\varepsilon(J_\ell-18).
$$

Substitution in (743.23) proves (743.4).
For an uncorrected primitive the equally exact formula is

$$
2\bigl(a_q(B)-16b_q(B)\bigr)
+\varepsilon(J_\ell-18)
=-\langle[B_p],(\widetilde d_q)_p\rangle_p.
\tag{743.25}
$$

The correction (743.14) is consistent with every sign in this
formula: its $p$ pairing is $23\lambda(B)$, while its change
of the $q$ functional is $-20\lambda(B)$, and
$23=-20\bmod43$.

## 6. The remaining ordinary comparison

Formula (743.4) is an equality for the original supported cochain
problem with its actual local finite-flat line. It fixes a concrete
coordinate in the quotient (743.15). No dimension count is used to
identify that quotient with an ordinary class-group quotient.

R720 identifies the distinct ordinary invariant by a full integral
chain comparison:

$$
\frac{\Theta[f_s]}{\Theta[f_t]}=ib,\qquad
C=9ib,\qquad
\Omega_2=\varepsilon(22+17b).
$$

The outstanding step is a natural, marked comparison of (743.15)
and its finite-flat primitive with those ordinary chains. This
paper does not supply that step and does not claim a proportionality
between $J_\ell-18$ and $b-24$. In particular R204 computes
$B_p(c_p^{\rm Rob})_q=24F_0$ for a different global class and a
specified Robert primitive. It supplies neither
$\mathfrak b_p(w)_q$ nor the ordinary coefficient $b$.

## Sources and proved inputs

- [R161](R161-strict-adjoint-selmer-line-and-tate-support-orthogonality.md)
  and [R163](R163-all-prime-primitive-adjoint-robert-generator.md):
  the complete minimal-support dual line and the strict
  primal condition.
- [R168](R168-tate-frobenius-sunit-slopes-and-weil-squareclasses.md):
  the original finite/singular coordinates and $2(ad-bc)$.
- [R185](R185-p-local-robert-and-principal-unit-coordinates.md):
  the complete local AH basis, both actual dual vectors,
  $\widetilde d_q=d_q-8d_0$, and $L_{\rm fl}^{\perp}$.
- [R189](R189-primal-robert-generator-and-exact-local-pairings.md):
  the entire minimal-support primal line, its actual generator,
  its $q$ value $10$, and the exact local functional $(6,10)$.
- [R191](R191-cyclotomic-principalization-and-eta-ray-field.md),
  [R196](R196-cm-reference-bockstein-and-the-actual-norm-field.md),
  and [R200](R200-second-obstruction-reference-cancellation-and-one-supported-norm-slope.md):
  the supported positive Norm primitive, original $-i$ convention,
  and the sign-sensitive secondary cochain identity.
- [The first-moment reconstruction, Section 8](../notes/2026-11-14-r599-first-moment-normalization-reconstruction.md):
  the actual dual value $((J_\ell-18)/2,0)$ with full support.
- J. S. Milne, *Arithmetic Duality Theorems*, second edition (2006),
  Chapter I, Theorem 4.10(a), printed pp. 56–57:
  <https://www.jmilne.org/math/Books/ADTnot.pdf>.

No new numerical evaluation is used in this proof. The displayed
residue constants are the original published R168/R171/R185/R189
and first-moment normalizations.
