# R150 appendix — the actual squarefree 32-basis and original constant reduction operators

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16 UTC.

Status: **proved by the actual complete finite calculation below.**
The $32$ basis monomials and all fixed original constant unit blocks
are now specified. Their exact inverses are defined by their adjugate
identities; their large number-field entries are not claimed to have
been numerically expanded.

## 1. The explicit basis

Keep the matched number field $E$, the global original coordinates
$B=y^{\mathsf T}w$, and the five derivatives
$$
F_i=\partial_{u_i}R'=q_i(u)+\text{terms of }u\text{-degree at most one}.
$$
The [complete original Jacobian calculation](R150-appendix-original-five-moment-jacobian-complete-intersection-and-parameter-free-rank32.md)
proved that $q_1,\ldots,q_5$ is a regular quadratic sequence,
with Hilbert series $(1+t)^5$, and that
$$
\mathcal A=E[y,w,u]/(F_1,\ldots,F_5)
$$
is free of rank $32$ over $E[y,w]$.

The present calculation proves that the following particular
preselected monomials, with no alteration after seeing the ranks,
form its basis:
$$
\boxed{\mathcal W=
 \{u_1^{\epsilon_1}\cdots u_5^{\epsilon_5}:
                  \epsilon_i\in\{0,1\}\}.}
\tag{1.1}
$$
Their counts in degrees $0,\ldots,5$ are $(1,5,10,10,5,1)$.
The same basis remains valid after arbitrary parameter base
change, including $y^{\mathsf T}w=1$.

## 2. Exact original blocks, not a finite-field basis substitution

For each $d=2,\ldots,6$, use the complete coefficient matrix
whose columns are, in order:

1. All squarefree monomials $\mathcal W_d$ of degree $d$.
2. All original products $q_i u^\alpha$ with $|\alpha|=d-2$.

All degree-$d$ output monomials in the five $u$ variables are
retained. The matrix is over the same characteristic-zero
field $E$ as the original model.

Every rational coefficient of these $q_i$ is actually integral
at $127$. The unchanged matched cubic has leading coefficient
a $127$-unit, and
$$
f(100)=0\quad\text{in }\mathbb F_{127}.
$$
Thus coefficient reduction followed by $d\mapsto100$ is a
valid ring homomorphism on all coefficients used here.
It is not assumed to be an embedding of the whole number field
into a finite field.

The actual field column profiles keep all prescribed
$\mathcal W_d$ columns, then select original source columns
until a square full-output block $U_d$ is reached. The actual
results are:

| Degree $d$ | All output rows | All original $q_i$ multiples | Squarefree columns | Selected original source columns | $\det U_d\bmod127$ |
|---:|---:|---:|---:|---:|---:|
| 2 | 15 | 5 | 10 | 5 | 44 |
| 3 | 35 | 25 | 10 | 25 | 58 |
| 4 | 70 | 75 | 5 | 65 | 5 |
| 5 | 126 | 175 | 1 | 125 | 60 |
| 6 | 210 | 350 | 0 | 210 | 1 |

The complete source dictionaries and selected original
indices are retained in the temporary model. Both matrix
inverse products over the actual finite field are checked,
in all $132652$ coordinates.

Each nonzero determinant is the specialization of the
determinant of that exact original $E$-matrix.
Therefore every $U_d$ is invertible over $E$.
No selected finite-field vector is lifted and asserted to
be a characteristic-zero source.

The already proved Hilbert dimensions show that the
selected $q_i$ columns have the full possible image dimension
at each degree. Consequently they span the entire homogeneous
original source image, including all nonselected source
columns. It follows that (1.1) is the exact complement in
$E[u]/(q_i)$, not merely a complement to a chosen subfamily.
The preceding filtered source theorem then gives the same
basis for $\mathcal A$.

## 3. Complete fixed constant reduction operators

For each displayed matrix define the exact operator
$$
\boxed{\mathcal R_d=U_d^{-1}
       =\frac{\operatorname{adj}U_d}{\det U_d}\in
          \operatorname{Mat}_{\binom{d+4}4}(E).}
\tag{3.1}
$$
Every entry of $U_d$ is specified by an original $q_i$,
an original multiplier and an original output monomial.
The nonzero denominator in (3.1) has just been certified
for that same matrix. Formula (3.1) therefore specifies
a complete exact reduction map, without needing to expand
its large constant coefficients.

If $v$ is the coefficient vector of a degree-$d$ polynomial,
the first $\dim\mathcal W_d$ coordinates of $\mathcal R_d v$
give its standard monomial part. The remaining coordinates
give its selected original $q_i u^\alpha$ source combination.
Thus
$$
P_d=\sum_{m\in\mathcal W_d}a_m m+\sum_i b_iq_i
$$
is an exact original polynomial identity over $E$.

For the parameter-dependent derivatives $F_i=q_i+\ell_i$,
replace $q_i$ by $F_i$ in that same source combination.
The error is $\sum_i b_i\ell_i$ of strictly smaller
$u$-degree. Continue by the fixed operators at lower
degrees. This is the complete source-preserving normal
form procedure over $E[y,w]$ and after every parameter
base change.

No $y$- or $w$-polynomial is inverted.
The present execution does not claim to have numerically
expanded the exact entries of (3.1), or to have constructed
all five $32\times32$ parameter multiplication matrices.
Those are subsequent possible evaluations of this
fully specified constant-operator presentation.

## 4. The first remaining normal forms only require the degree-two block

Weighted degree six gives an additional exact simplification.
The coefficient of every $u$-cubic term of $R'$ is a fixed
element of $E$. Differentiating with respect to any of the
six $y$ or six $w$ variables removes this top part.
Therefore all twelve remaining gradient generators have
$u$-degree at most two.

Let $S$ be the $5\times5$ matrix of coefficients of
$u_1^2,\ldots,u_5^2$ in $q_1,\ldots,q_5$, with the equation
orientation stated when it is used. Its invertibility
is exactly the degree-two block in §2 after the ten
squarefree columns are removed.
Thus all five squares can be replaced using only the
five full original equations $F_i$ and this fixed constant
matrix.

It follows that the twelve remaining gradient normal
forms lie in the $16$ basis monomials of degrees at most
two:
$$
1,\quad u_1,\ldots,u_5,\quad u_iu_j\ (i<j).
\tag{4.1}
$$
For the six $w$ derivatives, their quadratic $u$
coefficients are constants in $E$.
For the six $y$ derivatives, those coefficients are
linear in the original mean coordinates.
This follows directly from the weights.

Accordingly the next exact continuation may form the
full $12\times16$ polynomial-parameter matrix together
with its original five-source corrections. It need not
invert the degree-six block or form all $32$ multiplication
matrices simply to obtain these twelve generator normal
forms.

This does not say that the linear span of the twelve
rows decides their ideal inside the finite algebra:
multiplication by the remaining basis elements may still
be required. Neither that ideal nor its normalized
$B=1$ fiber has been computed in this appendix.

## 5. Actual source and execution

The [source](../notes/2026-11-16-r150-original-five-moment-squarefree32-fixed-reduction-789f.py)
is the $9917$-byte blob
~~~
12fc8f80f6b475d00b231449221cf720bc8edf65
~~~
with SHA-256
~~~
f7aa75ac0f78fad0cfb7882fb497a38c284e8527da2da7e89f61ceaf46f27327
~~~
It reads only the completed parent gate model, checking
the full bytes, logical payload and binding.
The [inputs](../notes/2026-11-16-r150-original-five-moment-squarefree32-inputs-789f.json)
and [actual local execution identity](../notes/r150-nonrankone-execution-789f/20261116-local-five-moment-squarefree32-fixed-reduction.json)
pin the complete reproducible scope.

Actual elapsed time was $0.3755828349967487$ seconds,
exit code zero. The fixed budget was $60$ seconds and
$1024$ MiB, using Python $3.12.14$ and python-flint $0.9.0$.
This was local execution, not an Actions run.

The semantic binding is
~~~
67f86e42cd7b1e01e30ca0184d136e2983842cfd6df31d28bd3d75fc8a0e8b33
~~~
The original $1534$-byte receipt SHA-256 is
~~~
6ada56d430ba73ae6479645d02f66d20a028c294f852a1cf170bc8007bd9af3c
~~~
The complete temporary model has $1185065$ logical bytes,
with logical SHA-256
~~~
b74faeb4ddf0a8ea38f6ece1585c437b01611f06cd11a1822ce9e145b902e62f
~~~
Its $578763$-byte gzip SHA-256 is
~~~
4be5d8a3a900799d41e5428671e1453a30082f0fdb8c3c2a130b416563031c42
~~~

Only sources, parameters, execution identity and hashes
are stored in the repository. The exact operator inputs
and all computed arrays remain temporary.
