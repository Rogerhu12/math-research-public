# R736. The original fixed Brandt model and all first-wild incidence rows

## Status and scope

This result gives a fixed, explicit finite model for the same universal quaternionic test vector used in R716 and R724. It then expresses every first-wild tame average, including its actual modulo-$p^2$ matching, in terms of that fixed vector.

The fixed model has 368 ideal classes. The original norm component, the original condition at $2$, and the original toric condition at $3$ reduce the vector to 47 integral signed coordinates. These coordinates do not vary with $p$. The maps from the norm-$p^2$ elements to the coordinates do vary with $p$; their anti-Fermat second digit is retained.

This is an exact model and an executable producer, not a proof that the first-wild averages are nonzero. The producer's default task computes only the fixed vector. No varying-prime sample is needed for the structural identities below. A computation of the fixed vector does not replace control of the complete incidence rows for arbitrarily large $p$.

## 1. The same quaternion algebra and the same order

Put

$$
K=\mathbb Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,
$$

and use

$$
B=K+Kj,\qquad j^2=-1,\qquad ja=\bar a j.
\tag{1}
$$

Thus

$$
\operatorname{nrd}(a+bj)=N_{K/\mathbb Q}(a)+N_{K/\mathbb Q}(b).
\tag{2}
$$

The algebra has discriminant $3$. This is the original algebra: the CM case of BHKO, Lemma 3.2, gives the product of the finite places with $\eta_{K_v}(-1)=-1$, which here is exactly $3$.

Let

$$
\mathcal O=\mathbb Z[\omega]+\mathbb Z[\omega]j.
\tag{3}
$$

The reduced-trace pairing in the basis $1,\omega,j,\omega j$ has determinant $-9$. Hence $\mathcal O$ has reduced discriminant $3$ and is maximal.

Every complex number has an Eisenstein integer at squared distance at most $1/3$. Consequently every element of $B\otimes\mathbb R$ has an element of $\mathcal O$ at reduced-norm distance at most $2/3$. Applying this to either quotient in the division algorithm proves that $\mathcal O$ is norm Euclidean on both sides. In particular every integral right $\mathcal O$-ideal is principal. Its units are

$$
\mathcal O^\times=\{\pm\omega^i,\ \pm\omega^i j:0\le i<3\},
\qquad |\mathcal O^\times|=12.
\tag{4}
$$

The order used here is

$$
\mathcal R=\mathbb Z[\omega]+34\delta\,\mathbb Z[\omega]j.
\tag{5}
$$

Its index in $\mathcal O$ is $N(34\delta)=3468$ and its reduced discriminant is

$$
3\cdot3468=36\cdot17^2=N_0.
\tag{6}
$$

It contains $\mathcal O_K$ optimally. Its local descriptions are

$$
\begin{aligned}
\mathcal R_2&=\mathcal O_{K,2}+2\mathcal O_2,\\
\mathcal R_{17}&=\mathcal O_{K,17}+17\mathcal O_{17},\\
\mathcal R_3&=\mathcal O_{K,3}+\delta\mathcal O_3,
\end{aligned}
\tag{7}
$$

and it is maximal elsewhere. Units multiplying the displayed conductors do not change the local orders.

These are the orders of discriminant $N_0$ with the original optimal toric embeddings in BHKO, Definition 3.6 and Lemma 3.7. The ramified description in BHKO, Lemma 3.11, is exactly the last line of (7). There is no replacement of the finite characters at $2,3,17$.

The primary reference is [BHKO, Hecke L-values, definite Shimura sets and mod ell non-vanishing](https://arxiv.org/html/2408.13932v3), §§2.3, 3.1--3.2 and Proposition 5.12. The absolute global normalization remains that of [R716](R716-original-wild-global-theta-period-and-exact-central-l-value.md).

## 2. All 368 classes as explicit finite cosets

Class number one gives

$$
X=\mathcal O^\times\backslash
\widehat{\mathcal O}^{\,\times}/\widehat{\mathcal R}^{\,\times}.
\tag{8}
$$

The nontrivial local right-coset sets are

$$
\begin{aligned}
Y_2&=\mathrm{GL}_2(\mathbb F_2)/\mathbb F_4^\times,
&|Y_2|&=2,\\
Y_{17}&=\mathrm{GL}_2(\mathbb F_{17})/\mathbb F_{289}^\times,
&|Y_{17}|&=272,\\
Y_3&=\mathbb F_9^\times/\mathbb F_3^\times,
&|Y_3|&=4.
\end{aligned}
\tag{9}
$$

For $q=2,17$, identify $Y_q$ with
$\mathbb P^1(\mathbb F_{q^2})\setminus\mathbb P^1(\mathbb F_q)$.
The reference point is $1+\omega$, fixed by the multiplication torus.

For $a=a_0+a_1\omega$, put

$$
M(a)=
\begin{pmatrix}a_0&-a_1\\ a_1&a_0-a_1\end{pmatrix},
\qquad
C=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}.
\tag{10}
$$

Use $t_2=1$ and $t_{17}=4$, both of norm $-1$ in the respective residue fields. Then

$$
M_q(a+bj)=M(a)+M(bt_q)C
\tag{11}
$$

is the split quaternion representation. At $3$, reduction modulo $\delta$ sends $\omega$ to $1$. Thus $a+bj$, for $a=a_0+a_1\omega$ and $b=b_0+b_1\omega$, maps to

$$
(a_0+a_1)+(b_0+b_1)j
\quad\text{in }\mathbb F_3[j],\quad j^2=-1.
\tag{12}
$$

The projective unit group
$\{1,\omega,\omega^2,j,\omega j,\omega^2j\}$
acts diagonally on $Y=Y_2\times Y_{17}\times Y_3$ using (11)--(12), and $X$ is exactly its orbit set.

There are $2176$ points in $Y$. Each of $\omega,\omega^2$ fixes $16$: two choices at $2$, two torus fixed points at $17$, and all four choices at $3$. None of $j,\omega j,\omega^2j$ fixes a point at $3$. Burnside's formula gives

$$
|X|=\frac{2176+16+16}{6}=368.
\tag{13}
$$

The original norm component $X^+$ consists of the norm-one classes at $3$ and has 184 points. For the standard stabilizer weight $1/w_x$,

$$
\sum_{x\in X^+}\frac1{w_x}=\frac{1088}{6}=\frac{544}{3}.
\tag{14}
$$

This is the same norm fibre established in §7.3 of the [original Brandt note](../notes/2026-11-15-first-wild-brandt-second-moment-and-synchronized-pairs.md).

## 3. The original vector lies in a fixed 47-dimensional signed lattice

Let $f$ be the universal toric vector for $E_{17}:y^2=x^3+17$. Proposition 5.12 of BHKO and the original root number $+1$ give

$$
f|_{X^-}=0.
\tag{15}
$$

The group $\mathcal R_2^\times$ is normal of index two in $\mathcal O_2^\times$, since $\mathbb F_4^\times$ is the index-two subgroup of
$\mathrm{GL}_2(\mathbb F_2)\simeq S_3$. Its invariant line in the original local representation is the same one-dimensional $K_2^\times$-invariant line. If the quotient involution acted by $+1$, this vector would be $\mathcal O_2^\times$-fixed, contradicting conductor exponent two at $2$. Therefore it acts by $-1$. In (9),

$$
f(\bar z_2,z_{17},k_3)=-f(z_2,z_{17},k_3).
\tag{16}
$$

The toric condition at $3$ also includes its uniformizer $\delta$. Right multiplication by $\delta$ at $3$, followed by global left multiplication by $\delta^{-1}$, acts by

$$
(z_2,z_{17},k_3)\longmapsto
\bigl(M_2(\delta)z_2,\ M_{17}(\delta)z_{17},\ \bar k_3\bigr).
\tag{17}
$$

Projectively $\delta^{-1}$ and $\delta$ agree. The last conjugation sends $j$ to $-j$ and is retained. The original vector is fixed by (17).

The relations (15)--(17) define a signed integral lattice of rank 47. After choosing one norm-one class at $3$ and using the global $j$ to remove its other choice, (16) leaves the 92 orbits of the order-three subgroup on $Y_{17}$. The involution (17) fixes exactly the two torus fixed-point orbits. Thus

$$
\frac{92+2}{2}=47.
\tag{18}
$$

Equivalently this is the space of functions on the 47 orbits of the order-six subgroup generated projectively by $\omega$ and $\delta$ on $Y_{17}$, with the prescribed sign at $2$. The reduction uses actual local invariance of the original vector.

## 4. Fixed Brandt operators and the original integral vector

For $\ell\nmid102$, let
$\mathcal Q_\ell=\{\beta\in\mathcal O:\operatorname{nrd}(\beta)=\ell\}$.
It has $12(\ell+1)$ elements, and the complete Brandt operator is

$$
(T_\ell F)(x)=\frac1{12}\sum_{\beta\in\mathcal Q_\ell}
F(\bar\beta\cdot x).
\tag{19}
$$

Indeed, each right ideal of norm $\ell$ is $\beta\mathcal O$ with $\beta$ determined up to right units. Its returned bad-place representative is $\beta^{-1}g$. Replacing $\beta$ by $\beta u$ changes this by a global left unit. Finally $\beta^{-1}=\bar\beta/\ell$, and the central denominator disappears from all local cosets. This proves both the side of the action and the factor $1/12$ in (19).

For

$$
a_\ell=\ell+1-\#E_{17}(\mathbb F_\ell),
$$

the original $f$ is the unique common eigenline in (15)--(17) satisfying

$$
T_\ell f=a_\ell f\qquad(\ell\nmid102).
\tag{20}
$$

Existence follows from the original Jacquet--Langlands representation and toric vector. Uniqueness follows from strong multiplicity one and the one-dimensional actual toric invariant line at every bad place. All equations are rational.

Fix the primitive integer vector $f_{\rm int}$ on this line, up to sign. A fixed nonzero scalar, independent of $p$, satisfies

$$
f=c_\psi f_{\rm int}.
\tag{21}
$$

It is not set to one in any use of the absolute R716 Waldspurger constant.

The producer imposes (19)--(20) at the fixed primes
$5,7,11,13,19,31,37,43$, retaining all 368 target rows, including $X^-$. It stops only when the exact rational kernel is one-dimensional. If the list does not suffice, it reports that more fixed equations are needed. The general proof does not assume that this particular finite list isolates the line.

The original class-number-one central value implies

$$
f_{\rm int}(1)=0.
\tag{22}
$$

The producer checks (22) after recovering the eigenline; it does not impose (22) to select it.

## 5. Every first-wild point from norm-$p^2$ elements

Let $p>19$ be inert, and write $R_p=\mathcal O_K/p^2\mathcal O_K$ in this section only. Choose an explicitly recorded $t_p\in R_p^\times$ with $N(t_p)=-1$ and use

$$
M_p(a+bj)=M(a)+M(bt_p)C
\quad\text{over }\mathbb Z/p^2\mathbb Z.
\tag{23}
$$

The producer chooses a norm-$-1$ residue modulo $p$ and lifts it by one explicit Hensel step.

Put

$$
\mathcal Q_{p^2}^{\rm prim}
=\{\beta\in\mathcal O:
\operatorname{nrd}(\beta)=p^2,\ \beta\notin p\mathcal O\}.
\tag{24}
$$

The image of $M_p(\beta)$ is a primitive cyclic rank-one direct summand modulo $p^2$, giving

$$
L_\beta\in\mathbb P^1(\mathbb Z/p^2\mathbb Z).
\tag{25}
$$

Every such line occurs exactly twelve times, once for each right unit. This is the principal-right-ideal argument of §4: cyclic index-$p^2$ sublattices give the primitive ideals, and the unique noncyclic ideal is $p\mathcal O$. Consequently

$$
|\mathcal Q_{p^2}^{\rm prim}|=12p(p+1).
\tag{26}
$$

For a primitive column $(a,b)^t$ of $M_p(\beta)$, let
$\alpha_\beta=a+b\omega\in R_p^\times$. The value at this CM point is

$$
F_p(L_\beta)=f_{\rm int}(\bar\beta\cdot1),
\tag{27}
$$

where the right side uses only the fixed bad-place maps (11)--(12) and the reference point $(1+\omega,1+\omega,1)$.

This is the conductor-$p^2$ orbit, not a new family. In the nonsplit BHKO formula (2.7), the image of the depth-two matrix modulo $p^2$ is the first coordinate line. In the basis $1,\omega-1$, multiplication by $2+\omega$ has the BHKO matrix (2.2). Thus the cyclic-line construction realizes the original orbit with the explicitly chosen compatible local identification.

Changing the norm-$-1$ splitting in (23) conjugates it by an actual unit of $R_p$, by Hilbert 90 for the unramified ring. This translates the complete ring-class orbit and adds a single fixed constant to its wild labels. It preserves the full second moment and the condition that all first-wild periods vanish. An individual labelled row must be transported by that actual translation.

## 6. The actual second digit and complete incidence rows

For $\alpha\in R_p^\times$, define

$$
q_p(\alpha)=\frac{\alpha^p/\bar\alpha-1}{p}\pmod p,
\qquad
\ell_p(\alpha)
=-34\,\frac{q_p(\alpha)-\overline{q_p(\alpha)}}{\delta}
\in\mathbb F_p.
\tag{28}
$$

This is the original wild parameter in R724. The division by $p$ is performed after actual exponentiation modulo $p^2$. It is not determined by the first residue digit.

The value is unchanged under rational-unit multiplication. Quotienting the line set by the global $\mu_3$ gives

$$
G_2=\Delta_p\times\Gamma_1,\qquad
|\Delta_p|=(p+1)/3,\quad|\Gamma_1|=p.
\tag{29}
$$

Every original tame average in the integral normalization is

$$
A_t^{\rm int}=\frac1{36}
\sum_{\substack{\beta\in\mathcal Q_{p^2}^{\rm prim}\\
\ell_p(\alpha_\beta)=t}}
f_{\rm int}(\bar\beta\cdot1).
\tag{30}
$$

The denominator is $12\cdot3$ from right units and global $\mu_3$. Every digit fibre in (24) has $12(p+1)$ elements.

For the fixed integral signed basis $e_1,\ldots,e_{47}$ of §3, write
$f_{\rm int}=\sum_i v_i e_i$. Then

$$
A_t^{\rm int}=\sum_{i=1}^{47}C_p(t,i)v_i,
\qquad
C_p(t,i)=\frac1{36}
\sum_{\substack{\beta\in\mathcal Q_{p^2}^{\rm prim}\\
\ell_p(\alpha_\beta)=t}}
e_i(\bar\beta\cdot1).
\tag{31}
$$

The coefficients are integers: right-unit invariance and the actual global $\mu_3$ action apply to every basis vector. Formula (31) is a finite exact expression for all synchronized rows. A fixed congruence class of $p$ does not determine these coefficients.

In the slope convention of the Brandt note, the same condition is

$$
x(a,t)=a+p\bigl(\kappa_p(a)+(1+3a^2)t\bigr)\pmod{p^2},
\tag{32}
$$

with the recorded unit change of additive wild coordinate when necessary. Formula (30) computes this matching; it does not delete $\kappa_p(a)$.

## 7. Diagonal energy and the remaining synchronous terms

The diagonal energy is

$$
D_p^{\rm int}=\frac1{36}
\sum_{\beta\in\mathcal Q_{p^2}^{\rm prim}}
 f_{\rm int}(\bar\beta\cdot1)^2.
\tag{33}
$$

The full synchronized second moment is exactly

$$
\mathcal M_p^{\rm int}
=\sum_{t\in\mathbb F_p}(A_t^{\rm int})^2
=v^{\mathsf t}C_p^{\mathsf t}C_pv.
\tag{34}
$$

The global ramified class of $\delta$ is a nontrivial order-two element of $\Delta_p$ and fixes the original vector. Every row in (30) is paired by this actual involution. Therefore

$$
A_t^{\rm int}\in2\mathbb Z.
\tag{35}
$$

The identity and this ramified class contribute exactly $2D_p^{\rm int}$ to (34). The remaining synchronous correlation is the integer

$$
E_p^{\rm rem}
=v^{\mathsf t}C_p^{\mathsf t}C_pv-2D_p^{\rm int}.
\tag{36}
$$

All branches and all collisions remain in (36). The unramified Hecke relation also gives

$$
\sum_t A_t^{\rm int}
=-\frac{p+1}{3}f_{\rm int}(1)=0.
\tag{37}
$$

Define

$$
c_{\rm int}
=\frac{\displaystyle\sum_{x\in X^+}
 f_{\rm int}(x)^2/w_x}{544/3}>0.
$$

The already proved original Brandt estimate is

$$
D_p^{\rm int}
=c_{\rm int}\frac{p(p+1)}3+O(p).
\tag{38}
$$

The implicit constant is fixed. In the R716 normalization the quadratic identities are multiplied by $c_\psi^2$.

The actual remaining assertion is

$$
C_pv\ne0
\tag{39}
$$

for the required infinite or density-one family of inert primes. If it fails, the exact consequence is

$$
E_p^{\rm rem}=-2D_p^{\rm int}.
\tag{40}
$$

Neither dimension 47 nor positivity of (38) alone excludes (40). Conversely, a structural or congruence proof of (39) for the explicit fixed vector would concern the original first-wild family, with all bad-place data and the full second digit retained.

The central-derivative-to-boundary question remains separate, as in R724 and the first-wild Rubin note.

## 8. Producer and reproducibility

The self-contained producer is [check-r736-original-brandt-vector-and-full-first-wild.py](../scripts/check-r736-original-brandt-vector-and-full-first-wild.py).

The default parameters are empty. It constructs the fixed 368-class model, the signed 47-coordinate lattice, and the original simultaneous Hecke eigenline. It reports the fixed 47 values, their exact value distribution, the norm-fibre mass and $c_{\rm int}$, and a SHA256 of the full reproducible table.

It reads no certificate or data file. The optional argument --prime p evaluates (23)--(38) on every primitive norm-$p^2$ element and retains the complete exponentiation in (28). It verifies line multiplicities, all digit fibres, the total sum and the ramified pairing. A finite optional evaluation does not prove (39) for varying primes.

All numerical execution uses the repository's public Actions workflow with python-flint 0.8.0. The run identifier and stdout SHA256 are recorded separately. Reproducible output is not committed to the repository or to a Release.


The completed public fixed-model run is [43705223442](https://github.com/Rogerhu12/math-research-public/actions/runs/43705223442), job 132784740866, at source e4f44a157794cfd37c9a4a58c969622df4d10600. The two exact Hecke steps at 5 and 7 reduce the signed rational kernel from 47 to 7 to 1. In the primitive integral normalization, the only values are 0, ±1 and ±2, the reference value is zero, and \(c_{\rm int}=81/68\). The complete table remains reproducible from the producer and is not stored as generated data. Its provenance and stdout digest are in the [run receipt](../ci/exact-check-20261115-r736-fixed-brandt.json).
