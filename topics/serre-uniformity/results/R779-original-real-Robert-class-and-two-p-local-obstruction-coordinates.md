# R779: an explicit real Robert class and the original obstruction in two p-local coordinates

Date: 2026-11-14. **Status: proved.** There is an explicitly
specified real Robert derivative class
$\mathfrak d_R\in H^1(G_{\mathbf Q,\Sigma},W(1))$,
defined below from the original $c_s$ and u alone.
Write its localization in the original R185 basis as

$$
(\mathfrak d_R)_p=B_1b_1+B_{45}b_{45},
\qquad B_1,B_{45}\in\mathbf F_{43}.
$$

For every value of the original b, including zero, one has

$$
\boxed{
b=-3B_1-5B_{45},\qquad
\Omega_2=\varepsilon(22-8B_1+B_{45}).
}
\tag{779.1}
$$

The class is specified by an actual ordinary unit expression,
not by choosing an origin in an abstract invariant quotient.
Both its global descent and its local descent have zero
inflation--restriction obstruction; the relevant $H^2$ term
is explicitly zero. The two numerical coordinates have not
yet been evaluated.

When $b\ne0$, the same class realizes the remaining coordinate
of R776 and gives the additional exact formulas

$$
\boxed{
I_0/\varepsilon=32+25B_1,\qquad
I_\alpha/\varepsilon=32+3B_1-8B_{45}.
}
\tag{779.2}
$$

The missing arithmetic is the actual p-local value of the
fixed mixed Robert expression. The already computed Gamma
embedding matrix supplies its labels and sufficient precision,
but does not supply that unit value.

## 1. The original units and a specified integral expression

Keep $p=43$, $\mathcal O=\mathbf Z_{43}[i]$, $k=\mathcal O/p$,
the original $F$, $L=FL_q$, $V=LF_s=M^T$, and

$$
\Gamma=\langle\gamma\rangle,\qquad S=\langle s\rangle,
\qquad x=\gamma-1,\quad z=s-1,\quad a=15i/7.
$$

All units are in the same unaveraged $P_+=44e_{\chi^-}$
component. In particular $c=c_s=N_Tc_B$ is R613's actual
mixed Robert unit, including its $s^{11}$ shift; u is the
same primitive pure-p Robert unit as R185 and R561.

Define the actual ordinary unit expression

$$
n=x^{40}z^{42}c+i x^{41}z^{41}c-x^{42}z^{40}c,
$$
$$
\boxed{
n_R=-in+\frac{11}{2}u.
}
\tag{779.3}
$$

Here division by 2 is in the integral coefficient ring
$\mathcal O$. The expression contains no unknown ordinary
norm unit and no q-principalization.

We first prove the invariance and reality of its mod-p class
without assuming $b\ne0$. The unconditional norm relations
are

$$
\begin{gathered}
N_Su_s=u,\quad N_\Gamma y=u,\quad N_Sc=c_q,\\
N_\Gamma c=(1-s^{11})u_s,\quad
xy=a\gamma^{22}c_q,\quad
py=u+aD_\Gamma^{\rm bal}c_q.
\end{gathered}
\tag{779.4}
$$

Modulo p, set

$$
e_0=x^{42}z^{41}c,\qquad e_1=x^{41}z^{42}c.
$$

Since $N_\Gamma=x^{42}$ and $N_S=z^{42}$ in characteristic p,
the first mixed norm relation gives

$$
x^{42}z^{42}c=0,\qquad e_0=-11u.
\tag{779.5}
$$

Applying $x^{41}$ to the fifth relation of (779.4) gives
$x^{42}y=ae_1$, since the top corner in (779.5) is zero.
As $x^{42}y=u$, this proves

$$
ae_1=u=-\frac1{11}e_0,\qquad
\boxed{e_1=-ie_0.}
\tag{779.6}
$$

The last equality uses $a=-4i$ and $1/11=4$ in k.
These are direct consequences of (779.4); they do not use
the conditional full-lattice generation in R773.

Now multiply (779.3)'s expression for n by x and z.
The $x^{43}$ and $z^{43}$ terms vanish modulo p, and
the remaining terms are $e_1+ie_0$ and $ie_1-e_0$.
Both vanish by (779.6). Since u is fixed integrally,

$$
\boxed{x[n_R]=z[n_R]=0\quad\text{in }E_V/pE_V.}
\tag{779.7}
$$

## 2. The exact real normalization

R613 uses real original points R and $Q_q$. Its original
$P_2$ transformation and character projection give

$$
\tau c_B=-c_B,\qquad \tau u_B=-u_B.
$$

The same result records $\tau S\tau=S$ and
$\tau T\tau=T^{-1}$. Taking the original T norm therefore
gives, without changing either point marking,

$$
\tau c=-c,\qquad \tau u=-u.
\tag{779.8}
$$

The involution is semilinear on coefficients:
$\tau i=-i$, and

$$
\tau x\tau=\gamma^{-1}-1=-\gamma^{-1}x,\qquad
\tau z\tau=z.
$$

Apply these formulas to the three terms of n. Modulo p,
using $x^{43}=z^{43}=0$ and the top-corner relation,

$$
\begin{split}
\tau n
&=-(1+x)^3x^{40}z^{42}c
  -i(1+x)^2x^{41}z^{41}c
  +(1+x)x^{42}z^{40}c\\
&=-n-3e_1-2ie_0\\
&=-n+ie_0
 =-n-11iu.
\end{split}
\tag{779.9}
$$

It follows that

$$
\tau\left(-in+\frac{11}{2}u\right)
=-in+\frac{11}{2}u
\quad\text{in }E_V/pE_V.
\tag{779.10}
$$

Thus the class in (779.3) has the original rational real
normalization. The coefficient $11/2$ is forced by the
actual involution; it is not a freely adjustable ordinary
unit correction.

For comparison, when $b\ne0$, R773 writes the real original
target as $U_V=(4/C)n+\eta u$, with $C=9ib$.
Applying (779.9), noting that $4/C$ is purely imaginary,
gives

$$
\eta+\bar\eta=\frac{44i}{C}=\frac1{9b}.
$$

This independently recovers
$\operatorname{Re}\eta=1/(18b)$ from R776's cochain computation.

## 3. Global descent, including the H2 obstruction

Use the original support $\Sigma=\{2,p,q,\infty\}$.
The ordinary unit class $[n_R]$ is unramified outside
the primes above $\Sigma$ in V: away from residue
characteristic p, Kummer classes of local units are
unramified, and the field extension itself is unramified
outside this support.

On $G_V$, the coefficient module is the original k-valued
Tate twist. The field V does not contain $\mu_p$.
Indeed $[V:K]=44p^2$, while $[K(\mu_p):K]=42$ does not
divide that degree. Consequently

$$
W(1)^{G_{V,\Sigma}}=0.
\tag{779.11}
$$

Let $Q=\operatorname{Gal}(V/\mathbf Q)$, with its original
action on the coefficients. The full initial
inflation--restriction sequence is

$$
\begin{split}
0\longrightarrow&
H^1\bigl(Q,W(1)^{G_{V,\Sigma}}\bigr)
\longrightarrow H^1(G_{\mathbf Q,\Sigma},W(1))\\
\longrightarrow&
H^1(G_{V,\Sigma},W(1))^Q
\longrightarrow
H^2\bigl(Q,W(1)^{G_{V,\Sigma}}\bigr).
\end{split}
\tag{779.12}
$$

Both outer groups in (779.12) are zero by (779.11).
In particular the obstruction to an invariant restriction
class is zero, as well as the kernel of restriction.

The character component in (779.3) is the same Kummer
component as in R768: the original $\Delta$ character
projection supplies precisely the required coefficient
equivariance. Equations (779.7) supply Gamma/S invariance,
and (779.10) supplies the remaining rational involution.
Thus its Kummer class belongs to the invariant group
on the second line of (779.12).

There is therefore a unique class

$$
\boxed{
\mathfrak d_R\in H^1(G_{\mathbf Q,\Sigma},W(1)),
\qquad
\operatorname{res}_V\mathfrak d_R=[n_R].
}
\tag{779.13}
$$

This is actual cohomological descent. No invariant class
has been lifted past an unexamined $H^2$ obstruction,
and no locally chosen p-th root specifies the descended
global class.

## 4. The original scalar Bockstein fixes its q coefficient

R743 proves the complete supported dual space

$$
H^1(G_{\mathbf Q,\Sigma},W(1))
=\mathbf F_p d_q\oplus\mathbf F_p d_0.
$$

Write, uniquely,

$$
\mathfrak d_R=A_Rd_q+B_Rd_0,
\qquad A_R,B_R\in\mathbf F_{43}.
\tag{779.14}
$$

We determine $A_R$ from the actual ordinary divisor
cocycle, keeping the case $b=0$.

Put

$$
D_S=\sum_{j=0}^{42}js^j,\qquad
D_\Gamma=\sum_{j=0}^{42}j\gamma^j,
$$
$$
v_s=u_s-y+aD_\Gamma^{\rm bal}c,\qquad
U_{\rm can}=D_Sv_s-11aD_\Gamma y.
\tag{779.15}
$$

The original norm identity gives $N_Sv_s=0$ exactly.
Since S fixes y,

$$
(s-1)U_{\rm can}=pv_s.
$$

For the usual ordinary multiplication-by-p connecting map,

$$
\beta_S:(E_V/pE_V)^S\longrightarrow H^1(S,E_V),
$$

this says

$$
\beta_S[U_{\rm can}]=[v_s].
\tag{779.16}
$$

We need its exact relation to the specified n, not merely
its position in an abstract invariant subspace. All of the
following is modulo p. One has
$D_\Gamma^{\rm bal}=D_\Gamma=-x^{41}-x^{42}$ and
$D_S=-z^{41}-z^{42}$.
Expanding $H_{11}(1+z)$ at z equal to zero gives coefficients
11 and 55 in degrees zero and one. From (779.4)--(779.6),

$$
z^{41}u_s=-\frac1{11}x^{42}z^{40}c-5u,
$$
$$
x^{41}y=a x^{40}z^{42}c+22a e_1.
\tag{779.17}
$$

Substitute these into (779.15). Its three degree-82 terms
are

$$
11a^2x^{40}z^{42}c
+a x^{41}z^{41}c
+\frac1{11}x^{42}z^{40}c=-4n.
$$

The remaining corner terms are
$ae_0+(a+242a^2)e_1+(4+11a)u$.
Using $a=-4i$, $e_1=-ie_0$, and $e_0=-11u$ gives

$$
\boxed{
U_{\rm can}=-4n+(5+21i)u
\quad\text{in }E_V/pE_V.
}
\tag{779.18}
$$

No nonzero-b hypothesis entered this computation.
As u is S fixed integrally, (779.16) implies

$$
\beta_S(n)=-\frac14[v_s],\qquad
\boxed{\beta_S(n_R)=\frac i4[v_s].}
\tag{779.19}
$$

The original ordinary divisor convention sends
$[v_s]$ to $C e_L$, where
$e_L=[P_+Q_L]\ne0$ is the specified generator of $A_L=k$
and $C=9ib$ by R720. Thus (779.19) has divisor class

$$
\frac i4 C e_L=-\frac{9b}{4}e_L.
\tag{779.20}
$$

We compare this with (779.14) using full divisors.
Choose $\mathcal O$ lifts of $A_R,B_R$, and an ordinary
representative w of $[n_R]$. Equality of the Kummer
classes in V gives an actual element $Z_R\in\mathscr K_V$
such that

$$
w=A_RA_\alpha+B_R\frac{i}{1848}u-pZ_R.
\tag{779.21}
$$

The original divisor of $A_\alpha$ in L is $pP_+Q_L$.
The S extension is unramified at q, so in V it is
$p\,j_{V/L}(P_+Q_L)$. All other displayed terms except
$Z_R$ are ordinary units. Hence the full divisor equality is

$$
\operatorname{div}Z_R
=A_Rj_{V/L}(P_+Q_L).
\tag{779.22}
$$

Applying the ordinary connecting map to (779.21) gives
the cocycle $-(s-1)Z_R$, whose descended divisor class
is $-A_Re_L$.

This conclusion is valid without first assuming that
$e_L$ capitulates. If $A_R\ne0$, equation (779.22)
itself proves the required capitulation. If $A_R=0$,
its descended class is zero. The full ordinary divisor
map used here has no omitted ramification correction:
q is unramified in $V/L$, the p and 2 prime-divisor
modules have zero original character component, and
all remaining primes are unramified. This is the
same exact Hilbert-90 divisor convention as R561.

Comparing with (779.20), and using $e_L\ne0$, proves

$$
\boxed{A_R=\frac{9b}{4}=13b\quad\text{in }\mathbf F_{43}.}
\tag{779.23}
$$

In particular $b=0$ forces the actually constructed
$\mathfrak d_R$ to belong to the minimal-support line
$\mathbf F_{43}d_0$. Nothing in this argument assumes
the ordinary descent of $d_q$ in that case.

## 5. The original p coordinates recover b and the obstruction

Use precisely R185's Artin--Hasse coordinates:

$$
(d_0)_p=24b_1+20b_{45},\qquad
(d_q)_p=20b_1+29b_{45}.
\tag{779.24}
$$

The determinant is $38\ne0$. Equations (779.14) and
(779.23) therefore give

$$
B_1=2b+24B_R,\qquad
B_{45}=33b+20B_R.
\tag{779.25}
$$

The indicated linear combination removes the entire
remaining global coefficient:

$$
\begin{split}
-3B_1-5B_{45}
&=-3(2b+24B_R)-5(33b+20B_R)\\
&=-171b-172B_R=b
\quad\pmod{43}.
\end{split}
$$

This proves the first formula of (779.1).
Substituting into the original
$\Omega_2=\varepsilon(22+17b)$ proves its second formula.

At q, the same normalization gives

$$
(\mathfrak d_R)_q
=13b(16,1)=(36b,13b).
\tag{779.26}
$$

This records its precise finite and singular coordinates.
It is not a new evaluation of either of them.

When $b\ne0$, R773/R776 give
$U_V=(4/C)n+\eta u$ with
$\eta=1/(18b)+i\eta_I$.
Substituting into (779.3) and using
$d_0|_V=(i/1848)u=-iu$ proves, by the injectivity
in (779.12),

$$
\boxed{
\mathfrak d_R=\frac{9b}{4}(d_q+\eta_I d_0).
}
\tag{779.27}
$$

Consequently the exact p coordinates are

$$
\boxed{
B_1=11b(\eta_I+8),\qquad
B_{45}=b(33+2\eta_I).
}
\tag{779.28}
$$

Thus $\eta_I+8$ is the actual finite-flat defect of the
specified real Robert derivative: the R185 finite-flat
dual line is $\mathbf F_{43}b_{45}$, so
$\mathfrak d_R$ belongs to that line at p exactly when
$\eta_I+8=0$, for $b\ne0$.

The R776 expression
$I_0/\varepsilon=32+17b(\eta_I+8)$ now gives
$I_0/\varepsilon=32+25B_1$, since $17/11=25$.
Subtracting $7b$ and applying (779.1) gives the other
formula in (779.2). These two secondary-invariant
formulas are asserted only when $b\ne0$; (779.1) holds
without that restriction.

## 6. Actual local descent requires no freely chosen root

Fix the original p branch of $L_q$ supplied by R704.
Since $L_q$ is split at p, the chosen completion of V
is the actual scalar completion $F_{s,p}$. Over $K_p$,
its degree is $44p=1892$, with residue degree one;
over $\mathbf Q_p$ the CM coefficient field is the
original unramified quadratic field.

The completion does not contain $\mu_p$:
$[K_p(\mu_p):K_p]=42$ does not divide 1892.
This local assertion is separate from the global
absence of $\mu_p$ in §3.

For $H=G_{F_{s,p}}$ inside $G_{F_p}$, the local
inflation--restriction sequence again has both terms

$$
H^1(S,W(1)^H)=0,\qquad H^2(S,W(1)^H)=0.
$$

Therefore restriction is an isomorphism onto the
invariant subspace. The localization of (779.3)
has a unique descended local class over $F_p$.
Its original tame character and rational involution
then identify it with the same
$B_1b_1+B_{45}b_{45}$ of §5.

Equivalently, use the complete local unit lattice
of R701,

$$
U_{F_s}\simeq\mathcal O[S]^2.
$$

Its mod-p invariant subspace has dimension two over k.
The two embedded original basis classes $b_1,b_{45}$
are independent there by the local restriction
injectivity just proved. Thus, in a certified basis
of $U_{F_s}/pU_{F_s}$, the computation is an
$86$-row, two-column linear equation for the actual
local vector (779.3). There is no quotient by an
unknown global ordinary-unit lattice and no choice
of a local p-th root in this equation.

The output coefficients are required to be in
$\mathbf F_{43}$ by the rational descent already
proved. Their two coordinates in the exact vector
equation, not a relabelled eigenvector, are the
$B_1,B_{45}$ in (779.1).

## 7. Finite precision and the remaining original unit input

The scalar completion has ramification index
$e=44\cdot43=1892$. If $\varpi_s$ is an actual
uniformizer, logarithm and exponential are inverse
on $U^{46}$, because $46>1892/(43-1)$.
Multiplication by p on the logarithm raises the
valuation by 1892. Hence

$$
U^{1938}=(U^{46})^{43}.
\tag{779.29}
$$

In particular the actual unit residues modulo
$\varpi_s^{1938}$ determine their full Kummer
classes. Lower unit filtrations must still be
represented in a genuine local Kummer basis;
a logarithm used below its inverse-exponential
range does not by itself supply that basis.

The fixed input expression is only

$$
-i x^{40}z^{42}c_s+x^{41}z^{41}c_s
+i x^{42}z^{40}c_s+\frac{11}{2}u.
\tag{779.30}
$$

The u contribution is already normalized by
$[u]_p=i(d_0)_p$. The unknown numerical input is
the actual p-local value of the displayed
Gamma/S derivatives of $c_s$.
It can be supplied by the original
Gamma-labelled local values of $c_s$ to
(779.29), or by a proved faster identity evaluating
the same expression. The original $c_q$ is its
S norm and need not be supplied as an independent
unit input for (779.30).

R704 has already evaluated the original 43
Gamma-labelled embeddings of $L_q$ modulo $43^2$.
For integral field coordinates this gives
$\varpi_s$ precision at least $3784>1938$.
Its original real root and positive Gamma
ordering must be retained when those embeddings
are applied to a unit representation.
As R704 states, its matrix evaluates field
coordinates; it does not itself produce the
coordinates of the mixed Robert unit.

No numerical value for (779.30) is asserted here.
The existing pure-p Robert evaluations at q
are not these p-local mixed-unit values, and the
raw partial q-torsion product is not proposed as
a feasible enumeration. This theorem identifies
the exact remaining finite local input and its
unconditional output formula; it does not count
an unevaluated coordinate interface as the
original b computation.

## Dependencies

- [R185](R185-p-local-robert-and-principal-unit-coordinates.md):
  the original p basis, exact $d_0,d_q$ coordinates, and finite-flat line.
- [R561](R561-restored-scalar-norm-cocycle-and-ordinary-artin-class.md)
  and [R613](R613-mixed-p-capitulation-and-the-exact-34-boundary.md):
  the original units and real torsion choices, full ordinary
  divisor convention, and exact norm and involution formulas.
- [R701](R701-original-C-as-a-marked-43-dimensional-p-local-scalar.md):
  the entire local unit lattice and the finite local precision.
- [R704](R704-actual-original-Gamma-p-split-embedding-matrix.md):
  the completed, correctly labelled p-split embedding matrix
  and its precise remaining unit-input boundary.
- [R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md)
  and [R720](R720-original-C-and-b-by-the-complete-Robert-chain-comparison.md):
  the genuine ordinary endpoint and the exact $C=9ib$ comparison.
- [R743](R743-original-first-moment-and-the-exact-flat-primal-secondary-slope.md):
  completeness of the supported dual cohomology space.
- [R768](R768-original-supported-dual-Kummer-class-and-ordinary-companion.md):
  the original full-divisor Kummer identification and character conventions.
- [R773](R773-complete-ordinary-scalar-lattice-and-original-mixed-Robert-phase.md)
  and [R776](R776-original-cochain-p-division-and-the-remaining-scalar-unit-coordinate.md):
  the specified unit vectors, conditional ordinary coordinate eta,
  and its exact original cochain pairing.
