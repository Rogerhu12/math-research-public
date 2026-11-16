# R150 appendix — original five-moment Jacobian is a complete intersection and the full parameter quotient is free of rank 32

Authors: Astra-ISP-789f / normal_annihilator and root.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16 UTC.

Status: **proved.** The fixed original five-moment calculation is
complete, and the filtered source argument below holds over the entire
parameter ring. The quotient by only five original transported
gradients is free of rank $32$; the remaining twelve gradients are
not discarded and their normalized critical locus is not declared empty.

## 1. Original model and the exact theorem

Use the unchanged matched cubic field
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$
and the [global polynomial coordinates](R150-appendix-global-matched-bell-hyperbolic-coordinates-and-normalized-critical-ideal.md)
$$
(y,H)\longleftrightarrow(y,w,u),\qquad
B_r=y^{\mathsf T}w,\qquad
R'=R_3\circ\Psi.
$$
All $17$ original gradients are transported by a complete
invertible polynomial Jacobian over $E$. The weights are
one for the six $y$ variables and two for the six $w$ and
five $u$ variables.

Let
$$
C(u)=R'(0,0,u)=-8\operatorname{tr}((KH(u))^3),\qquad
q_i=\partial_{u_i}C\quad(1\le i\le5).
$$
Here $H(u)$ is the original physical Hankel matrix obtained
from the actual inverse coordinate map with $y=w=0$.

The complete actual calculation proves
$$
\boxed{E[u]_6=\sum_{i=1}^5q_iE[u]_4.}
\tag{1.1}
$$
It follows that the five quadratic forms $q_i$ are a regular
sequence and
$$
\operatorname{Hilb}\big(E[u]/(q_1,\ldots,q_5);t\big)
=(1+t)^5.
\tag{1.2}
$$
In particular this quotient has $E$-dimension $32$.

Now put
$$
A=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad
F_i=\partial_{u_i}R',
$$
and retain the full parameter-dependent polynomials $F_i$.
Then
$$
\boxed{\mathcal A=A[u_1,\ldots,u_5]/(F_1,\ldots,F_5)
       \text{ is a free }A\text{-module of rank }32.}
\tag{1.3}
$$
The same $32$ fixed monomials in $u$ give a basis after every
$E$-algebra base change on the parameters. In particular
$$
\mathcal A\otimes_A A/(y^{\mathsf T}w-1)
$$
is still free of rank $32$ over $A/(y^{\mathsf T}w-1)$.
There is no parameter discriminant or parameter denominator
in this statement.

## 2. Complete original finite matrix

The preceding actual coordinate computation retained the
entire $C$: all $35$ cubic monomials in five variables and
their three matched-field components. It verified the trace
formula against the complete original $H$-only restriction
of $R_3$.

The present consumer locks the parent source, the entire
compressed model, its canonical logical hash and its semantic
binding. It differentiates that exact cubic. The resulting
$5\times15$ coefficient matrix is compared entry by entry with
the parent's stored polar matrix: all $225$ rational field
coordinates agree.

The map used in (1.1) is
$$
\mathcal M:\bigoplus_{i=1}^5 E[u]_4\longrightarrow E[u]_6,
\qquad(a_i)\longmapsto\sum_i a_iq_i.
\tag{2.1}
$$
Every original column and row is kept:
$$
5\binom84=5\cdot70=350\text{ source columns},\qquad
\binom{10}{4}=210\text{ output rows}.
$$
No source relation or output coordinate is removed beforehand.

Use the exact $E/\mathbb Q$ basis $(1,d,d^2)$ to write (2.1)
as a rational linear map with $630$ rows and $1050$ columns.
For each original source $(i,u^\alpha,d^j)$, the source
multiplies every coefficient of $q_i u^\alpha$ by $d^j$
and reduces by the exact monic matched cubic.

Each resulting rational column is multiplied by its own
nonzero rational constant to become a primitive integer
column. All $47250$ nonzero coefficient products in these
scalings are checked. These are invertible source changes
over $\mathbb Q$ and hence preserve rational rank.
They are **not** claimed to be units over
$\mathbb Z_{(127)}$.

Reducing the resulting entire integer matrix modulo the
fixed prime $127$, the actual rank is
$$
\boxed{\operatorname{rank}_{\mathbb F_{127}}\overline{\mathcal M}_{\mathbb Q}
       =630.}
\tag{2.2}
$$
Thus a $630$-row minor is nonzero modulo $127$ and therefore
is a nonzero rational minor of the scaled matrix.
The full rational rank is $630$, and the $E$-linear rank of
(2.1) is $210$. This proves (1.1).

This inference needs no assertion about unramified coordinates,
flat reduction of the matched field, or integral saturation
of the original cubic coefficients. The computation is a
rational regular representation followed by a nonzero-minor
lower bound and the exact row-count upper bound.

## 3. The fixed homogeneous complete intersection

Let $\mathfrak m=(u_1,\ldots,u_5)$.
Since the entire degree-six component is in $(q_1,\ldots,q_5)$,
multiplying those identities by monomials gives
$$
\mathfrak m^6\subset(q_1,\ldots,q_5).
\tag{3.1}
$$
The five $q_i$ therefore form a system of parameters at the
homogeneous maximal ideal of $E[u]$.

The polynomial ring over a field is Cohen–Macaulay, and in
a Cohen–Macaulay local ring a system of parameters is a
regular sequence. These standard algebraic facts are stated,
respectively, in
[Stacks, Lemma 10.104.7](https://stacks.math.columbia.edu/tag/00N7)
and [Stacks, Lemma 10.104.2](https://stacks.math.columbia.edu/tag/02JN).
Applying them at $\mathfrak m$ and using homogeneity gives
the regular sequence in $E[u]$.

The exact homogeneous Koszul complex then gives the Hilbert
series
$$
\frac{(1-t^2)^5}{(1-t)^5}=(1+t)^5.
$$
Consequently the graded dimensions are
$$
\boxed{(1,5,10,10,5,1)\quad\text{in degrees }0,\ldots,5,}
\tag{3.2}
$$
and zero thereafter.

In geometric language the projective hypersurface $C=0$
has no projective critical point. Euler's identity
$3C=\sum_i u_iq_i$ shows that its singular scheme is governed
by these same five quadratic partials. This conclusion
concerns this fixed original five-variable cubic, not the
full parameter-dependent critical locus.

## 4. Why the full parameter deformation has the same initial ideal

The original weighted-six structure gives
$$
F_i=q_i+\ell_i(y,w;u)+c_i(y,w),
\tag{4.1}
$$
where $\ell_i$ has $u$-degree at most one and $c_i$ has
$u$-degree zero. The highest $u$-degree parts are the same
fixed quadratic forms $q_i$ at every parameter value.

Filter $A[u]$ by total $u$-degree. We claim that
$$
\operatorname{in}_u(F_1,\ldots,F_5)
=(q_1,\ldots,q_5)A[u].
\tag{4.2}
$$
The inclusion from right to left follows directly from (4.1).
For the other inclusion, consider an identity
$$
g=\sum_i a_iF_i.
$$
If the highest terms of the right side do not cancel, its
initial form belongs to $(q_i)$. If they do cancel, the
highest homogeneous coefficient vector $(a_i^{\rm top})$
is a syzygy of $(q_i)$.

Exactness of the Koszul complex expresses that vector as
$$
a_i^{\rm top}=\sum_j b_{ij}q_j,\qquad b_{ij}=-b_{ji}.
$$
The same Koszul exactness is valid over $A$: the exact
complex over the field $E$ remains exact after tensoring
with the $E$-algebra $A$.
Replace the coefficients by
$$
a_i\longmapsto a_i-\sum_j b_{ij}F_j.
$$
The total combination $\sum_i a_iF_i$ is unchanged, because
the antisymmetric double sum $\sum_{ij}b_{ij}F_iF_j$ is
zero. Its coefficient tuple has strictly smaller highest
$u$-degree. Repeating this finite descent proves (4.2).

Thus there is an exact associated-graded identification
$$
\operatorname{gr}_u\mathcal A
 \simeq A\otimes_E E[u]/(q_1,\ldots,q_5).
\tag{4.3}
$$
This is a source-preserving argument: every reduction is
an explicit combination of the original $F_i$ with
polynomial coefficients over $A$.

## 5. A fixed monomial basis and parameter-free reduction

For each degree $d$, choose an $E$-linear complement
$$
E[u]_d=(q_1,\ldots,q_5)_d\oplus W_d
$$
spanned by monomials. By (3.2), these complements have
dimensions $1,5,10,10,5,1$ for $d=0,\ldots,5$ and are
zero for $d\ge6$.
Let $\mathcal W$ be their combined $32$ monomials.

The same $\mathcal W$ generates $\mathcal A$ over $A$:
subtract original $F_i$ combinations to remove the highest
$u$-degree part, then continue to lower degrees.
It is independent by (4.2): the highest nonzero homogeneous
part of a relation among $\mathcal W$ would lie both in
$A\otimes_E W_d$ and in $(q_i)A[u]_d$.

This proves the free-module assertion (1.3). Every scalar
inverse required by the construction belongs to the fixed
field $E$, from the finite homogeneous linear systems for
$(q_i)$. No inverse of a polynomial in $y,w$ is needed.

More explicitly, for a polynomial $P$ of $u$-degree $D$,
one obtains
$$
P=\operatorname{NF}(P)+\sum_i a_iF_i,\qquad
\operatorname{NF}(P)\in A\mathcal W,
$$
with
$$
\deg_u a_i\le\max(D-2,0).
\tag{5.1}
$$
For $D<2$ no reduction is needed, so all $a_i$ may be zero.
The statement does not claim an optimal parameter-degree
bound.

Nothing in this proof requires a particular parameter
specialization or that the parameter ring be a domain.
After every base change from $A$ to an $E$-algebra, the
same reduction and independence hold. In particular the
Bell normalization $y^{\mathsf T}w=1$ preserves all $32$
basis elements without a new rank computation.

The present calculation proves existence and gives the
exact finite original linear systems defining these
reductions. It has not yet materialized a chosen
$32$-element basis, its full parameter multiplication
matrices, or all remaining gradient normal forms.

## 6. The precise remaining original problem

In the finite algebra $\mathcal A$, retain the twelve
classes
$$
[\partial_{y_i}R'],\quad[\partial_{w_i}R']
\qquad(0\le i\le5).
$$
The complete original gradient quotient is exactly
$$
\mathcal A/
\big([\partial_{y_i}R'],[\partial_{w_i}R']\big).
\tag{6.1}
$$
For the Bell-nonzero question, base-change (6.1) to
$y^{\mathsf T}w=1$.
All original sources are retained by the polynomial
Jacobian transport and by the reductions in §5.

Thus the continuation can use a rank-$32$ finite algebra
over the twelve-parameter ring, or over its normalized
Bell hypersurface. It need not restart an unconstrained
seventeen-variable elimination.

Neither (1.3) nor (6.1) says the full critical quotient
has rank $32$, is zero, or is parameter-flat. The remaining
twelve relations can change it. They must actually be
consumed to decide Bell radical membership. In the finite
algebra, weighted Euler gives
$$
6[R']=\sum_i y_i[\partial_{y_i}R']
       +2\sum_i w_i[\partial_{w_i}R'],
$$
so the original potential also remains under exact
source control.

## 7. Actual identity, source and limits

The [complete gate source](../notes/2026-11-16-r150-original-five-moment-cubic-complete-jacobian-gate-789f.py)
is the $9133$-byte blob
~~~
a923dce5f28f17eb2d12d26306ead7ff410b3615
~~~
with SHA-256
~~~
ed98a483008a74a081d4b2a75101b5a47fb56d861de23e063fe2686a71e68ae5
~~~
The [frozen input contract](../notes/2026-11-16-r150-original-five-moment-cubic-complete-jacobian-inputs-789f.json)
pins the entire parent model, the complete original source
dictionary, prime $127$, Python $3.12.14$ and python-flint
$0.9.0$. The bounded execution used $60$ seconds and $1024$
MiB.

Actual local execution completed at $2026$-$11$-$16$
$04{:}52{:}43.008253$ UTC, exit code zero, after
$14.829539719998138$ seconds. The
[execution identity](../notes/r150-nonrankone-execution-789f/20261116-local-five-moment-cubic-complete-jacobian-gate.json)
records the tool session and every output SHA. This is a
local execution; no Actions run is attributed to it.

The semantic binding is
~~~
35d8d699301fd0916097cf796078efad734787a8220b37e393a98b665ccc070a
~~~
The $1747$-byte receipt has SHA-256
~~~
1af39e72547ed9962cc01abaeb36053deaacbf75a194e0bffae2c08e5ed7c191
~~~
The complete temporary reduction-input model has $4435758$
logical bytes and logical SHA-256
~~~
cef307471088203fcbb763223e132b90ecc3867158241366a364e934e16971d7
~~~
Its $962420$-byte gzip SHA-256 is
~~~
05301272897e83766ee604aa0873c0b5af977aa2fe5263fa37e51a0cd73dc6ca
~~~

The full original source and output dictionary hashes are
~~~
531816a894ab804bb0bb9ed5be1f17830d97aed7ca89353c5ee29f2c59062d8d
93fd9ffefbaf38cbe756a1e7a2e26352ce55634b03d637b66cfe43690ae31e14
~~~
The primitive integer matrix reduced modulo $127$, in
column-major order, has SHA-256
~~~
e8b732d9a54cc932e21ce7286fd945c096671dbd00c3f1d556a5db3266ab6d39
~~~

The largest primitive integer coefficient has $8584$ bits.
The actual checks include every one of the $225$ original
polar coordinates and all $47250$ nonzero primitive-scaling
products before the full $630$-row rank computation.
There is no random prime selection, no dropped output row,
and no inference of characteristic-zero nonregularity from
a deficient finite-field rank.

Only sources, parameters, execution identity, hashes and
this proof are stored in the repository. The full models
and matrix arrays remain temporary.
