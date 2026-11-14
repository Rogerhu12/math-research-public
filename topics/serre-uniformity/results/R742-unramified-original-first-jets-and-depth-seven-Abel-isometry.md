# R742 — Unramified original first jets and a depth-seven Abel isometry

Date: 2026-11-14. Status: **proved**.

The first flat jet of every actual primitive positive coefficient
embedding is unramified at the inert prime $p$. Consequently its
valuation is an integer. This supplies the missing rounding step in
R737 and gives an isometric original Abel component on the complete
closed disc $v_p(a-1)\ge7$ for every sufficiently large allowed prime.

The descent below uses the full arithmetic $\mathrm{GL}_2$ action,
including its determinant action on Fourier coefficients. It is not
an inference from complex torus invariance alone.

## 1. Statements with the original normalization

Let $p\ge41$, $p\equiv5\pmod6$, and put $n=p+1$. Fix an actual
primitive positive label

$$
1\le h<n,\qquad (h,n)=1,\qquad h\equiv1\pmod6.
\tag{742.1}
$$

Use the original R575/R588 positive cubic marking, the original
Teichmueller character $\theta_h(y)=[y]^{-h(p-1)}$, and the original
Cartan average $u_h=A_{\mathsf T_\zeta}e_0$. Let $F_h$ be the
corresponding raw cusp-normalized weight-two form, including its
actual tame vector $(1,-4\zeta^2)$ in the basis $(H_0,H_2)$.
Here $\zeta^2+\zeta+1=0$ is the fixed positive complex embedding.

Throughout this result, $F_h$ means exactly the form already fixed
by the absolute normalization of R588. We do not apply a further
tame slash operation to that form while keeping the name $M_{2,h}$.
This convention does not identify the base level coset $I$ with
the original $c_1$ point. R738 makes the other full theta
enumeration explicit: $c_1$ has two-level coset $C$, represented by
$g_*\zeta$, where one may take

$$
g_*=\begin{pmatrix}1+9p^2&3p\\3p&1\end{pmatrix}.
$$

Its determinant is one; its $p$ and $3$ components are identity
and its $2$ component is $C$.
At $p=41$ it is exactly
$\left(\begin{smallmatrix}15130&123\\123&1\end{smallmatrix}\right)$.
Passing between this enumeration and the R588 representative
transports the original form, tame basis, level marking, and
differential frame together. In an untransported raw tame table
one has $F_1^\circ|_2g_*=\zeta^2F_1^\circ$; Section 3 records
this phase explicitly. It is not multiplied a second time into
the fixed R588 jet. The equality below uses precisely that fixed
jet and its original period.

Retain the original good CM curve and period:

$$
E_0:y^2=x^3-1,\qquad \omega=dx/(2y),\qquad
\Lambda=\Omega\mathbf Z[\zeta],\qquad\Omega>0.
\tag{742.2}
$$

The absolute flat normalization of R588/R592 is

$$
M_{2,h}=
 \left(\frac{2\pi i}{\Omega}\right)^6
 \delta_4\delta_2F_h(\zeta),
\qquad
\delta_k=\frac1{2\pi i}\frac d{d\tau}
             -\frac{k}{4\pi\operatorname{Im}\tau}.
\tag{742.3}
$$

**Theorem 742.1.** In the fixed $p$-adic embedding, $M_{2,h}$ lies
in a finite unramified extension of $\mathbf Q_p$. In particular,

$$
\boxed{
M_{2,h}=0\quad\hbox{or}\quad v_p(M_{2,h})\in\mathbf Z.
}
\tag{742.4}
$$

This assertion is unconditional for every label (742.1);
it does not assume a nonzero Cartier residue or a nonzero central
$L$-value.

For the remaining statements impose the actual prime classes
$p\equiv2,5\pmod9$, and put

$$
\mathcal H^*=\{h\bmod n:(h,n)=1,\ h\equiv1\pmod6\},
\qquad g=|\mathcal H^*|=\varphi(n)/2.
$$

**Theorem 742.2.** If $M_{2,1}\ne0$ and $p\ge2^{160}$, then some
actual primitive label $h\in\mathcal H^*$ satisfies

$$
\boxed{M_{2,h}\ne0,\qquad v_p(M_{2,h})\le1.}
\tag{742.5}
$$

For any actual label satisfying (742.5), let $s=a-1$ be the
original rational coarse parameter, and retain the whole scalar
Abel increment

$$
\mathcal I_h(s)=
 \sum_{j\ge1}\frac{M_{3j-1,h}}{(3j)!}\,
                  z_{\mathrm f}(s)^{3j}.
\tag{742.6}
$$

Then

$$
\boxed{
\frac{16\,\mathcal I_h(p^7u)}{p^7M_{2,h}}
  =u+pH_h(u),\qquad
H_h\in u^2\mathbf Z_p\langle u\rangle.
}
\tag{742.7}
$$

It is an isometric automorphism of the closed unit disc, with an
inverse in the same integral Tate algebra. Over every complete
valued extension, and for $s_1,s_2\in p^7\mathcal O$,

$$
\boxed{
v_p\bigl(\mathcal I_h(s_1)-\mathcal I_h(s_2)\bigr)
 =v_p(M_{2,h})+v_p(s_1-s_2).
}
\tag{742.8}
$$

The genuine original quotient component is
$J_h(s)=\gamma_h\mathcal I_h(s)$, where $\gamma_h\ne0$ is exactly
the fixed Kodaira–Spencer comparison of R705/R730.
Its difference valuation adds $v_p(\gamma_h)$.
No unit normalization of $\gamma_h$ is assumed.

R729 makes $M_{2,1}\ne0$ unconditional for every sufficiently
large allowed prime. Thus (742.7) holds for some original
primitive component at each such prime. The chosen label may
depend on $p$.

## 2. A genuine weight-zero function for the same first jet

Write

$$
D=\frac1{2\pi i}\frac d{d\tau}=q\frac d{dq},\qquad
\partial_k=D-\frac{k}{12}E_2,\qquad
X=E_2^*=E_2-\frac3{\pi\operatorname{Im}\tau}.
\tag{742.9}
$$

Here $E_2,E_4,E_6$ have their usual rational Fourier expansions
with constant term one. The Serre derivative $\partial_k$ takes
weight $k$ forms to weight $k+2$ forms of the same full level.
Its covariance follows directly by differentiating the weight-$k$
slash action and using the transformation formula for $E_2$.
Also

$$
\delta_k=\partial_k+\frac{k}{12}X,\qquad
\delta_2X=\frac{X^2-E_4}{12}.
\tag{742.10}
$$

The latter identity follows from
$DE_2=(E_2^2-E_4)/12$ and differentiation of
$1/\operatorname{Im}\tau$.
The weight-graded Leibniz rule therefore gives the exact identity

$$
\delta_4\delta_2F
 =\partial_4\partial_2F
    +\frac X2\,\partial_2F
    +\left(\frac{X^2}{24}-\frac{E_4}{72}\right)F.
\tag{742.11}
$$

At $\tau=\zeta$ the order-three elliptic stabilizer forces
$E_2^*(\zeta)=E_4(\zeta)=0$: their weights are two and four,
and the corresponding automorphy factors are different from one.
Hence

$$
\delta_4\delta_2F_h(\zeta)
  =\partial_4\partial_2F_h(\zeta).
\tag{742.12}
$$

Define the meromorphic weight-zero modular function

$$
\mathfrak J_h(\tau)=
       \frac{\partial_4\partial_2F_h(\tau)}{E_6(\tau)}.
\tag{742.13}
$$

It is finite at $\zeta$. Indeed, the Weierstrass equation in
(742.2) gives $g_3(\Lambda)=4$, and the usual lattice expression
for $g_3$ is

$$
g_3(\Omega(\mathbf Z+\mathbf Z\zeta))
 =\frac{8\pi^6}{27\Omega^6}E_6(\zeta).
$$

In particular $E_6(\zeta)\ne0$, and, with the actual period
normalization,

$$
\left(\frac{2\pi i}{\Omega}\right)^6E_6(\zeta)
 =-216g_3(\Lambda)=-864.
\tag{742.14}
$$

Combining (742.3), (742.12), and (742.14) proves the exact identity

$$
\boxed{M_{2,h}=-864\,\mathfrak J_h(\zeta).}
\tag{742.15}
$$

There is no factorial omitted here: $M_2$ is the flat derivative,
and (742.3) is precisely R588 (588R.32) for $m=2$.
The scalar $-864$ is a $p$-adic unit. No replacement of $\Omega$,
of the tame vector, or of the cusp-normalized Cartan average has
occurred.

## 3. The actual determinant action on the finite type

This section fixes the distinction between the original left
finite representation and the right arithmetic action on modular
functions.

For the full-level and coefficient checks, the raw degeneracy
functions before a change of tame enumeration are

$$
H_0^\circ(\tau)=f_{\theta_h}(\tau/(6p)),\qquad
H_2^\circ(\tau)=f_{\theta_h}(2\tau/(3p)).
\tag{742.16}
$$

Both are weight-two forms on $\Gamma(6p)$. For example,
conjugating a matrix of $\Gamma(6p)$ by
$\operatorname{diag}(1/(6p),1)$ gives a matrix of
$\Gamma_0(9p^2)$; its lower-left entry is a multiple of
$36p^2$. For the second degeneracy the lower-left entry is a
multiple of $9p^2$. This is the original level of the
untwisted newform. The finite Cartan projection preserves the
full level.

When using the R738 enumeration, the same marking transport is
applied to both functions, their coefficient vector, and the frame.
Its $p$ component is identity, so it commutes with all the
$p$-component actions used below. The raw phase can also be checked
directly. In the basis $(H_0^\circ,4H_2^\circ)$ the pure two-level
matrices are

$$
S_2=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
T_2=\begin{pmatrix}-1&0\\-1&1\end{pmatrix}.
$$

The coefficient matrix for the right slash by $C=S_2T_2$ is
$T_2S_2$. For the original positive vector,

$$
(T_2S_2)\binom{1}{-\zeta^2}
 =\zeta^2\binom{1}{-\zeta^2}.
$$

Thus the raw representative and its $g_*$ translate differ by the
explicit factor $\zeta^2$, which is fixed by $p$-inertia.
If a basis is already transported, this factor is not applied again.
Our $F_h$ and $M_{2,h}$ remain the fixed R588 objects throughout.
Either enumeration therefore has the same level, coefficient-field,
and arithmetic $p$-Cartan descent statements, without suppressing
the phase in the comparison of representatives.

The newform coefficients lie in $\mathbf Q(\zeta_n)$:
its ideal-sum coefficients are sums of
$a\epsilon_3(a)\theta_h(a)$, with
$a\in K=\mathbf Q(\zeta)\subset\mathbf Q(\zeta_n)$.
The original finite-type matrices also have coefficients in
$\mathbf Q(\zeta_n)$, by their explicit Weyl sums, and the tame
matrices use only $\zeta$. Thus the original finite and tame
coefficient scalars are unramified at $p$.

The R592 cusp realization of the finite left basis is

$$
e_r\longmapsto f_r
 =\sum_{\nu\ge1}a_\nu\zeta_p^{-\nu r}Q^\nu.
\tag{742.17}
$$

The tame tensor factor is unchanged throughout this formula.
The index here is the local $p$-cusp index of R592.
If one instead uses the global parameter $q^{1/(6p)}$ and
CRT translates $k_r\equiv0\pmod6$, $k_r\equiv r\pmod p$,
the phase is $\zeta_p^{-\nu r/6}$.
This is a fixed tame-unit reindexing, and it still sends
$r$ to $dr$ under the same determinant automorphism.
The finite left action corresponds to the inverse of the
classical right slash action. This is the original intertwining
convention, not a new twist of the representation.

To check the determinant part, take $d\in\mathbf F_p^\times$.
Choose an arithmetic determinant element whose component at $p$
is

$$
\Delta_d=\operatorname{diag}(1,d),
$$

and whose components at all primes dividing $6n$ are identity.
Equivalently, the scalar determinant has residue $d$ modulo $p$
and residue one modulo $6n$. The associated Fourier-coefficient
automorphism fixes $\mathbf Q(\zeta_{6n})$ and sends
$\zeta_p$ to $\zeta_p^d$. Therefore, term by term in (742.17),

$$
f_r^{\,\Delta_d}=f_{dr}.
\tag{742.18}
$$

On the original affine left model,

$$
\rho_h(\Delta_d^{-1})e_r=e_{dr}.
\tag{742.19}
$$

Thus the semilinear determinant action is exactly the inverse
finite left action, with no extra character of the determinant.
The coefficients of $\rho_h$ and of $u_h$ are fixed by the
chosen coefficient automorphism, so this check also applies to
their linear combinations.

The determinant-one part is the already fixed slash
intertwining of R592/R727. Since every element of
$\mathrm{GL}_2(\mathbf F_p)$ is a product of a determinant
element and a determinant-one element, (742.18)–(742.19)
prove the complete arithmetic identity

$$
(F_v)^g=F_{\rho_h(g^{-1})v}
\tag{742.20}
$$

for $p$-component actions $g$, with identity components on the
tame level and on the prime-to-$p$ coefficient level.
Here $F_v$ includes the fixed tame vector.
The original finite representation factors through
$\mathrm{PGL}_2(\mathbf F_p)$, so scalar matrices introduce no
additional factor.

In particular the actual Cartan-averaged form satisfies

$$
F_h^{\,g}=F_h
\quad\text{for every }g\text{ whose }p\text{ component is in }
\mathsf T_\zeta
\text{ projectively, and whose other components are identity}.
\tag{742.21}
$$

A period-basis change conjugates this group and transports
$v$, $e_0$, and the full level marking together. Equation
(742.20) is equivariant under precisely that simultaneous
transport. In particular it does not replace the translated
split vector $e_{1/2}$ of R588 by $e_0$ in the trace-zero basis.

The same arithmetic invariance holds after either Serre
derivative. For determinant-one matrices this is its slash
covariance. For $\Delta_d$, differentiation of $q^{\nu/N}$
multiplies its coefficient by the rational number $\nu/N$,
so $D$ commutes with coefficient Galois action; multiplication
by the rational $q$-series $E_2$ also commutes. The level-one
rational form $E_6$ is fixed. Hence (742.21) applies to
$\mathfrak J_h$.

## 4. Remove the p-part of the CM conductor, without moving the tame data

Set

$$
N^*=6pn,\qquad N_0=6n.
\tag{742.22}
$$

The Fourier coefficients just described, and those of
$\mathfrak J_h$, lie in $\mathbf Q(\zeta_{N^*})$.
The analytic full level $6p$ divides $N^*$.
Thus $\mathfrak J_h$ belongs to the arithmetic modular-function
field $\mathcal F_{N^*}$: weight zero, level $\Gamma(N^*)$,
and coefficients in $\mathbf Q(\zeta_{N^*})$.
The enlargement records the coefficient field; it does not
change the actual vector or its CM value.

Use Shimura reciprocity in its arithmetic right-action convention:

$$
\mathfrak J_h(\zeta)^{\operatorname{Art}_K(x)}
 =\mathfrak J_h^{\,g_\zeta(x^{-1})}(\zeta),
\qquad
g_\zeta(x)\binom{\zeta}{1}
 =x\binom{\zeta}{1}.
\tag{742.23}
$$

This formula, including the determinant coefficient action and
the inverse on $x$, is stated for $K=\mathbf Q(\sqrt{-3})$ in
E. Rosu, *Central values of L-functions of cubic twists*,
[§5, Theorem 35](https://link.springer.com/article/10.1007/s00208-020-02018-0).
It applies here to a finite value of a weight-zero modular
function. No reciprocity formula for a nonholomorphic derivative
is being assumed.

Let $x$ be an idele which is an arbitrary unit
$x_p\in\mathcal O_{K_p}^{\times}$ at the inert prime $p$ and
equals one at every other finite place.
Write $x_p=A+B\zeta$. Then the matrix in (742.23) is exactly

$$
g_\zeta(x_p)
 =\begin{pmatrix}A-B&-B\\ B&A\end{pmatrix}.
\tag{742.24}
$$

Its determinant is $A^2-AB+B^2=\operatorname N(x_p)$,
a $p$-adic unit. Modulo $p$, it belongs to the original torus:
in R727's notation take $a=A-B$, $b=B$ in

$$
\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}.
$$

Its inverse belongs to the same torus. At every place dividing
$N_0$, the component of $g_\zeta(x^{-1})$ is identity.
In particular it does not alter the conductor-six character,
the positive $\mu_3$ marking, or the $\mu_n$ coefficient field.
Its determinant action is exactly the one checked in
(742.18), together with its determinant-one factor.

Equation (742.21), now applied to $\mathfrak J_h$, makes the
right side of (742.23) equal to $\mathfrak J_h(\zeta)$.
Local units at $p$ map onto the inertia subgroup in this
abelian CM extension. Thus the CM value is fixed by the
entire inertia subgroup at $p$.

Equivalently, although the a priori ray modulus is $N^*$,
the value belongs to its subfield with no conductor factor
at $p$; the remaining modulus divides $N_0$.
The use of an idele supported at $p$ is essential here.
We have not replaced it by a principal representative with
uncontrolled residues at $2$, $3$, or primes dividing $n$.
The units $\mu_6$ of $K$ cause no difficulty in the reciprocity
quotient, and no nontrivial unit action is imposed on the
tame marking.

It follows that $\mathfrak J_h(\zeta)$ belongs locally to a
finite unramified extension of $K_p$.
Since $p\equiv2\pmod3$, the field $K_p/\mathbf Q_p$ is itself
unramified quadratic. Equation (742.15) proves Theorem 742.1.

This proves unramifiedness of the actual $M_2$, not only of
its square or of a separately rescaled eigenvector.

The same descent also applies to every label $h\equiv1\pmod6$
in the full family of R733, even if $(h,n)>1$.
Indeed $\theta_h(\zeta)=\zeta^{-1}$, so $\theta_h$ is nontrivial
and nonquadratic; the same cuspidal model, trivial central action,
coefficient field, and actual tame formula apply.
Primitivity was not used in Sections 2–4.
This extends the unramifiedness statement only: nonprimitive
labels are not relabelled as coefficient embeddings of the
original primitive quotient. All the selection, rational-jet,
and Abel-map assertions below retain (742.1).

### 4.1. The same field contains every allowed flat jet

There is also an all-order version, including when $M_{2,h}=0$.
Construct modular forms $A_{m,r}$ by
$A_{0,0}=F_h$, with all other initial terms zero, so that

$$
\delta_2^mF_h=\sum_{r=0}^{m}A_{m,r}X^r,
\qquad
\operatorname{wt}(A_{m,r})=2+2m-2r.
\tag{742.24a}
$$

Here $\delta_2^m$ denotes the composition with its increasing
weights. This expression is obtained by an explicit recurrence,
not by assuming that an arbitrary constant coefficient is modular.
If $k=2+2m$, set terms outside $0\le r\le m$ equal to zero and put

$$
A_{m+1,r}=
\partial_{k-2r}A_{m,r}
 +\frac{k-r+1}{12}A_{m,r-1}
 -\frac{r+1}{12}E_4A_{m,r+1}.
\tag{742.24b}
$$

Every term has weight $k+2-2r$ and is a genuine modular form.
The recurrence follows by applying the graded Leibniz rule
and $\delta_2X=(X^2-E_4)/12$ to each summand of (742.24a).
It proves (742.24a) inductively. All the coefficients have the
same arithmetic coefficient field, and all retain the same
full $p$-Cartan invariance, since the Serre operators and
multiplication by $E_4$ commute with the arithmetic actions
already checked in Section 3.

For an allowed order $m=3j-1$, the coefficient $A_{m,0}$ has
weight $6j$. Since $X(\zeta)=0$ and $E_6(\zeta)\ne0$, the function

$$
\mathfrak J_{m,h}=A_{m,0}/E_6^j
\tag{742.24c}
$$

is a weight-zero function finite at $\zeta$ with the same
Cartan invariance and level/coefficient bounds.
The flat/raising identity of R588 is valid at every derivative
order, by its Gauss–Manin chain-rule induction. Thus

$$
\boxed{
M_{3j-1,h}=(-864)^j\mathfrak J_{3j-1,h}(\zeta)
\qquad(j\ge1).
}
\tag{742.24d}
$$

The same supported-idele argument places all these values in
one finite CM field with ray modulus dividing $N_0$, unramified
at $p$. Therefore every nonzero allowed original jet has integer
valuation, without a nonvanishing premise on $M_2$.
For $m=2$, $A_{2,0}=\partial_4\partial_2F_h-E_4F_h/72$;
its CM value agrees exactly with the first-jet formula (742.15).
This all-order extension also applies to the full positive
family just described, with the same scope restriction.

## 5. Consequences for individual valuations and the original product

When $M_{2,h}\ne0$, R730's unchanged rational-line argument gives

$$
\frac{M_{3j-1,h}}{M_{2,h}}\in\mathbf Q_p
\qquad(j\ge1).
\tag{742.25}
$$

These ratios are rational $p$-adic numbers, in addition to the
unramified field statement of Section 4.1.
The comparison uses one fixed line and does not rescale
different derivative orders. Its rationality will keep the
normalized Tate series over $\mathbf Z_p$ itself.

The full one-$p$ Hodge bound of R730 is

$$
v_p(M_{m,h}/m!)\ge-1-m\frac p{p+1}
\qquad(m\ge0).
\tag{742.26}
$$

At $m=2$, the bound is strictly greater than $-3$.
Combining it with (742.4) gives the useful lower bound

$$
\boxed{v_p(M_{2,h})\ge-2\quad\text{when }M_{2,h}\ne0.}
\tag{742.27}
$$

There is also an exact parity consequence for R717's original
period product. R740 proves
$v_p(N_h)\in2\mathbf Z_{\ge0}$.
The original norm, including its tame phase, is

$$
\frac{M_{2,h}^2}{\zeta^2}
 =-\frac{8N_hC_0^2}{(p+1)^2}P_h,\qquad
P_h=\frac{S_{2,h}S_{3,h}}{C_0^2}.
\tag{742.28}
$$

All the fixed displayed factors are $p$-units. Therefore,
when $P_h\ne0$,

$$
\boxed{
v_p(P_h)=2v_p(M_{2,h})-v_p(N_h)\in2\mathbf Z.
}
\tag{742.29}
$$

This parity comes from the full descent and R740.
It was not assumed by the exact continuation in R739,
whose retained examples are consistent with it.

## 6. Apply the original second moment and select an actual component

Assume $M_{2,1}\ne0$. R730 proves that every primitive
$M_{2,h}$ is nonzero. Write $\eta_h=v_p(M_{2,h})$.
R737, with all its original conductor-six factors and periods,
gives

$$
\frac1g\sum_{h\in\mathcal H^*}2\eta_h<3+\delta_p,
$$
$$
\delta_p=
\frac{134\log2+\log(1+\log p)+2\log(2+\log_2p)}
     {\log p}.
\tag{742.30}
$$

For $p\ge2^{160}$, R737 proves $\delta_p<1$.
Theorem 742.1 makes every $2\eta_h$ an even integer.
If every $\eta_h$ were at least two, their doubled average
would be at least four, contrary to (742.30).
This proves (742.5).

The same argument gives many eligible labels if desired.
Let

$$
b_p=\#\{h\in\mathcal H^*:\eta_h\le1\}.
$$

All other labels have $\eta_h\ge2$, while (742.27) gives
$\eta_h\ge-2$ for every label. Thus

$$
\sum_h2\eta_h\ge-4b_p+4(g-b_p)=4g-8b_p.
$$

Consequently

$$
\boxed{\frac{b_p}{g}>\frac{1-\delta_p}{8}.}
\tag{742.31}
$$

For $p\ge2^{512}$, the proven inequality $\delta_p<1/2$
gives $b_p>g/16$. These are labelled actual coefficient
embeddings, with the same convention as R737. They need
not coincide with the unit-norm labels counted in R741.

## 7. The entire Tate tail at the improved scale

Fix a label with $M_{2,h}\ne0$ and $\eta_h\le1$.
Use the original flat variable and full coarse change:

$$
V=\frac{z_{\mathrm f}^3}{p^3},\qquad
V=\Psi(s/p^3),\qquad
\Psi(v)=\frac38v+\sum_{j\ge2}\psi_jv^j,
$$
$$
\Psi\in\mathbf Z_p\langle v\rangle,\qquad
\psi_j\in p\mathbf Z_p.
\tag{742.32}
$$

These are the complete R710/R711 changes; no finite Taylor
truncation substitutes for them.

Put

$$
E_{j,h}=\frac{p^{3j}M_{3j-1,h}}{(3j)!},\qquad
\mathscr I_h(V)=\sum_{j\ge1}E_{j,h}V^j.
\tag{742.33}
$$

Thus $\mathcal I_h(s)=\mathscr I_h(\Psi(s/p^3))$.
The bound (742.26), with the extra factor $3j$ in the
denominator retained, gives

$$
v_p(E_{j,h})
 \ge\frac{3j-1}{p+1}-v_p(3j)>0
 \qquad(j\ge1),
\tag{742.34}
$$

and the lower bound tends to $+\infty$.
For completeness, if $p\nmid3j$ the strict positivity is
immediate. If $a=v_p(3j)\ge1$, then $j\ge p^a$ and the
right side is at least
$(3p^a-1)/(p+1)-a>1$ for $p\ge41$.
This proves the estimate for every degree, including those
whose factorial is divisible by $p$.

Normalize by the actual first coefficient:

$$
E_{1,h}=\frac{p^3M_{2,h}}6,\qquad
G_h(V)=\frac{\mathscr I_h(V)}{E_{1,h}}
       =V+\sum_{j\ge2}\beta_{j,h}V^j.
\tag{742.35}
$$

Every $\beta_{j,h}$ belongs to $\mathbf Q_p$ by (742.25).
Its valuation satisfies

$$
v_p(\beta_{j,h})>-\eta_h-3\ge-4.
$$

The valuation of a nonzero rational $p$-adic number is an
integer, so the correct improved bound is

$$
\boxed{
\beta_{j,h}\in p^{-3}\mathbf Z_p,\qquad
v_p(\beta_{j,h})\longrightarrow+\infty.
}
\tag{742.36}
$$

It follows on the entire restricted series, not just its
first two coefficients, that

$$
\frac{G_h(p^4u)}{p^4}
 =u+\sum_{j\ge2}p^{4(j-1)}\beta_{j,h}u^j
 \in u+p\,u^2\mathbf Z_p\langle u\rangle.
\tag{742.37}
$$

Indeed $4(j-1)-3\ge1$ for every $j\ge2$.
This is the change from the depth-eight argument:
its $p^{-4}$ tail is replaced by (742.36), and the flat
scaling is now $p^4$.

At $s=p^7u$, formula (742.32) gives

$$
\frac{\Psi(p^4u)}{p^4}
 =\frac38u+p\,u^2\mathbf Z_p\langle u\rangle.
\tag{742.38}
$$

Compose (742.37) with this restricted series. Using the exact
first coefficient in (742.35), the resulting normalization is

$$
\begin{aligned}
\frac{16\,\mathcal I_h(p^7u)}{p^7M_{2,h}}
 &=\frac83\,\frac{G_h(\Psi(p^4u))}{p^4}\\
 &=u+pH_h(u),\qquad
H_h\in u^2\mathbf Z_p\langle u\rangle.
\end{aligned}
\tag{742.39}
$$

This proves (742.7), including both the factor sixteen and
the original coarse scale $p^7$.

## 8. Isometry, inverse, and the precise remaining boundary

A restricted series $T(u)=u+pH(u)$ with
$H\in u^2\mathbf Z_p\langle u\rangle$ has a restricted inverse:
for target variable $v$, the iteration

$$
u_{r+1}=v-pH(u_r),\qquad u_0=v,
$$

is a contraction in the complete unit ball of
$\mathbf Z_p\langle v\rangle$.
It produces an inverse with integral coefficients.
For two points in the closed unit disc over any complete
valued extension, the restricted series

$$
\frac{H(u_1)-H(u_2)}{u_1-u_2}
$$

is integral, by termwise difference factorization and
convergence. Thus
$T(u_1)-T(u_2)=(u_1-u_2)(1+pQ)$ with $v_p(Q)\ge0$.
The second factor is a unit. Applying this to (742.39) gives
(742.8) exactly.

The scalar increment has only its simple central zero on
$v_p(s)\ge7$. The actual Abel vector is injective there,
because the chosen actual component already is.
Multiplication by the original nonzero $\gamma_h$ preserves
injectivity and adds its valuation to (742.8).

For sufficiently large allowed $p$, R729 supplies the
nonvanishing premise and R737 supplies the selected label.
The theorem is therefore uniform in $p$ at this fixed depth,
without claiming one fixed primitive label works for all primes.

The full candidate region starts at depth four.
Depths four through six have not been removed here.
Moreover, the positive-rank rational-point condition is still
the original height condition with its fixed constants.
An injective Abel component does not require a rational
candidate to have its central Abel value.
This result neither supplies the missing original height jets
nor concludes Serre uniformity.

## Dependencies and primary reciprocity source

- R588 (588R.32), R592: the unchanged absolute flat jet,
  tame vector, finite-type cusp realization, and original full-level
  algebraic normalization.
- R727 and R730: the actual primitive embeddings, full arithmetic
  finite model, one-$p$ Hodge bound, and rational jet ratios.
- R710/R711: the complete rational flat/coarse change.
- R729/R737: sufficiently-large original nonvanishing and the
  complete central second-moment bound.
- R740 is used only for the additional period-product parity
  in (742.29), not for the proof of Theorem 742.1.
- E. Rosu, *Central values of L-functions of cubic twists*,
  Mathematische Annalen 378 (2020), 1327–1370,
  [§5, arithmetic action and Theorem 35](https://link.springer.com/article/10.1007/s00208-020-02018-0).
  The $p$-supported idele and its original matrix are made
  explicit in (742.23)–(742.24).

