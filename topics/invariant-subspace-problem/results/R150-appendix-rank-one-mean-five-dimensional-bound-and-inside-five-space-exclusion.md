# R150 appendix — physical means have common support at most five, and an inside physical mean excludes dimension five

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved**.

## 1. Statement

Use the original six-mode Hankel tensors and
$$
T_3=y^3-6yH+4V,\qquad M=H-yy^{\mathsf T}/4.
$$
Suppose the mean has catalecticant rank one, so
$$
y=a v(s),\qquad a\ne0,
$$
and suppose the essential support $W$ of $T_3$ has dimension three.

Then:

1. The minimal common supporting space $E$ of $y,H,V$ has dimension
   at most five.
2. If $y\in W$, then in fact $\dim E\le4$.

These are consequences of the original Hankel and essential-support
structure; neither assertion requires the low critical equations.
The second assertion does not assume $\operatorname{ess}(V)=5$.
Every finite or infinite physical point and every vanishing lower
local coefficient is included.

The outside-mean common dimension-five case, and the remaining
common dimensions at most four, are not classified by this theorem.

For the zero mean there is a separate immediate fact: $T_3=4V$.
The already proved invertibility of the
[original highest Hankel coefficient map $J_3$](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)
makes the highest identity imply $V=0$.
Thus a complete critical point with $y=0$ cannot have essential
third-moment dimension three. The work below concerns nonzero
physical means.

## 2. The conormal defect is the entire physical tangent space

Let
$$
T=\operatorname{span}\{v(s),v'(s)\},
$$
where the derivative is a genuine local jet at infinity when needed.
The exact conormal annihilator is
$$
\{z:yz^{\mathsf T}+zy^{\mathsf T}\text{ is Hankel}\}=T.
\tag{2.1}
$$
To verify it, use covariance of the rational normal curve and of
Hankel tensors to move $s$ to zero for this linear-algebra calculation.
Then $y$ is a nonzero multiple of $e_0$. The anti-diagonal equalities
in $yz^{\mathsf T}+zy^{\mathsf T}$ force $z_2=\cdots=z_5=0$;
$z_0,z_1$ are free. Transporting back gives (2.1).
No change of the original $K$ is made in any physical argument.

For every curve quadric $q(r)=r^{\mathsf T}Qr$, the exact identity
$(1/6)q(\partial)T_3=-4MQy$ and (2.1) give
$$
M(\operatorname{ann}T)\subset W.
\tag{2.2}
$$
This is the same tensor identity used in the rank-two conormal
appendix, now with its correct two-dimensional defect.

The minimal common space is exactly
$$
E=W+\mathbb Cy+\operatorname{Ran}M.
\tag{2.3}
$$
Indeed $H=M+yy^{\mathsf T}/4$ and
$$
V=T_3/4+y^3/8+(3/2)yM
$$
give one inclusion; the defining expression for $T_3$ and for $M$
gives the other.

## 3. A common dimension bound with the whole defect retained

Let $C=W\cap T$ have dimension $d$, and choose
$$
W=C\oplus W_0,\qquad T=C\oplus T_0.
$$
The condition (2.2), together with symmetry of $M$, gives
$$
M=M_W+B_{T_0}+\sum_{i=1}^d
(c_i z_i^{\mathsf T}+z_i c_i^{\mathsf T}),
\tag{3.1}
$$
where $M_W$ is supported on $W$, $B_{T_0}$ on $T_0$, and the $c_i$
form a basis of $C$. The vectors $z_i$ need not belong to $W+T$.

For clarity, choose a complementary block $Z$ so that the ambient
space is $C\oplus W_0\oplus T_0\oplus Z$.
Covectors in $\operatorname{ann}T$ have only $W_0,Z$ coordinates.
Their images outside $W$ must vanish. Therefore the
$T_0$–$W_0$, $Z$–$W_0$, $T_0$–$Z$, and $Z$–$Z$ matrix blocks
vanish, as do their transposes. The only remaining exterior blocks
are $T_0$–$T_0$ and blocks with one index in $C$, exactly (3.1).

Since $y\in T$ and $\dim T_0=2-d$, (2.3) gives
$$
E\subset W+T_0+\operatorname{span}(z_1,\ldots,z_d),
\qquad \dim E\le3+(2-d)+d=5.
\tag{3.2}
$$
In particular the argument does not discard a second exterior
direction when the entire tangent space is already in $W$.

## 4. Any common five-space is an exact physical hyperplane

Assume for contradiction that $y\in W$ and $\dim E=5$.
Every hyperplane in the six-dimensional coefficient space is
annihilated by one nonzero homogeneous binary quintic $g$.
The physical jets on its zero divisor, of length five, are independent
and span that hyperplane. Thus
$$
E=E_g,\qquad \deg g=5.
\tag{4.1}
$$

The same $g$ genuinely supports $H,V$, even when either tensor
has smaller essential rank. Every Hankel column lies in $E_g$,
so its pairing with the coefficient vector of $g$ vanishes.
For $H$ these are all degree-ten relations $gS_5$; for $V$ all
degree-fifteen relations $gS_{10}$. Division by $g$ and the local
decomposition give their unique jet representations on $g$.
Some top local coefficients may be zero.

Let $D_H,D_V$ be their exact minimal sub-divisors, obtained by
deleting those zero tails. Minimality of the common space means
$$
D_H\vee D_V\vee[s]=g.
\tag{4.2}
$$
Otherwise all of $y,H,V$ would be supported on at most four
independent physical jets.

## 5. Two independent annihilating directions identify the top blocks

The space $L=\operatorname{ann}_E W$ has dimension two.
Every $\lambda\in L$ has $\lambda(y)=0$.
Contraction of $T_3$ gives
$$
V\lambda=y(H\lambda).
\tag{5.1}
$$
Both $V\lambda$ and $H$ are original Hankel tensors.
By (2.1), $H\lambda\in T$.

The map
$$
L\longrightarrow T,\qquad \lambda\longmapsto H\lambda
\tag{5.2}
$$
is injective. If $H\lambda=0$, then (5.1) gives $V\lambda=0$;
together with $\lambda(y)=0$, this says that $\lambda$ annihilates
the entire minimal common space $E$, so $\lambda=0$.
Both spaces in (5.2) have dimension two, hence it is an isomorphism.
In particular $T\subset E$, and
$$
\{V\lambda:\lambda\in L\}
=yT=\operatorname{span}\{y^2,yv'(s)\}.
\tag{5.3}
$$
The latter is the complete two-dimensional Hankel quadratic space
on the physical double point $2s$.

At any support point other than $s$, the contractions in (5.1)
and (5.2) vanish. Local nondegeneracy at the exact top coefficient
there implies that every $\lambda\in L$ vanishes on the entire
local support of $H$ and of $V$ at that point.
Thus every physical jet of $g$ away from $s$ belongs to $W$.

Let $m$ be the exact local length of $H$ at $s$, and $n$ that of $V$.
Both are at least two by (5.2)–(5.3).
Use Taylor jets of one local nonzero physical representative,
and let $j$ be the smallest vanishing order at $s$ attained by a
nonzero restriction of a member of $L$.

A tensor with exact top local coefficient in length $m$ has the
Frobenius multiplication pairing on $\mathbb C[\epsilon]/(\epsilon^m)$.
Contraction by a function of order $j$ has exact remaining length
$m-j$. Since (5.2) is the full first-two-jet space,
$$
j=m-2.
$$
The same calculation for (5.3) gives $j=n-2$. The minimum order is
the same actual local function in both calculations, so
$$
m=n.
\tag{5.4}
$$
Every $\lambda$ vanishes on $y=a v(s)$, hence $j\ge1$ and $n\ge3$.

More precisely, restrictions of $L$ form exactly the ideal
$(\epsilon^{n-2})$ of dimension two in the length-$n$ local algebra.
Both contraction maps are injective, and their images are the full
length-two spaces, so no coefficient in that ideal is missing.
Therefore
$$
W=E_{(n-2)s}\oplus E_{g-ns},
\qquad n\in\{3,4,5\}.
\tag{5.5}
$$
The second summand includes every block away from $s$, proved above.
Its dimension is $5-n$, making the right side exactly three-dimensional.

## 6. The two top monomials cannot both cancel

Write the Taylor jets at $s$ as $u_0,\ldots,u_{n-1}$, with
$y=a u_0$, $a\ne0$. Let the nonzero top coefficients of $H,V$
at $s$ be $h,v$, respectively.
Their highest local parts are
$$
H_{\rm top}=h\sum_{i+j=n-1}u_i u_j,\qquad
V_{\rm top}=v\sum_{i+j+k=n-1}u_i u_j u_k.
\tag{6.1}
$$
These are ordered sums in the homogeneous tensor polynomials.

By (5.5), $u_{n-2},u_{n-1}$ lie outside $W$.
The coefficient of $u_0^2u_{n-1}$ in the full $T_3$ is
$$
12(v-ah).
$$
It must vanish.

For $n=3$, the coefficient of $u_0u_1^2$ is
$$
6(2v-ah).
$$
For $n=4,5$, the coefficient of the distinct-variable monomial
$u_0u_1u_{n-2}$ is
$$
12(2v-ah).
$$
Each of these monomials also involves a direction outside $W$,
so its coefficient must vanish.
Lower local coefficients have lower total jet index and cannot
contribute; different physical blocks are independent and cannot
cancel them.

Thus $v=ah$ and $2v=ah$, forcing $v=h=0$.
This contradicts the exact local lengths in (5.4).
The common five-dimensional case with $y\in W$ is impossible,
which proves the second assertion.

## 7. Scope for the continuing rank-one-mean classification

The rank-one conormal defect is two-dimensional, so it would be
incorrect to assume the earlier rank-two one-companion formula.
The theorem retains the entire defect, proves the common bound,
and excludes the inside five-space even when neither $H$ nor $V$
has essential dimension five.

The outside-mean five-space still needs its own argument.
The common dimensions three and four also require their actual
original critical equations. Nothing here asserts that a rank-one
mean automatically has the already classified $W_\pm$ support or
that a scalar classification supplies natural Jacobian powers.
