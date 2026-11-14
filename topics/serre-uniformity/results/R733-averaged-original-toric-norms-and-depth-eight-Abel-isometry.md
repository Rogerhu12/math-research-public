# R733 — Averaging the actual toric norms and a fixed depth-eight Abel disc

Date: 2026-11-14. **Status: proved.** The original finite toric norms
have a much smaller average than their individual bound $p^2-1$.
Keeping the same split vector and CM torus gives an elementary
full-family bound $13p$ for that average. Together with R730 this
improves the uniformly available original Abel disc from depth nine
to depth eight.

No all-prime Cartier-unit assertion is made, and no canonical-height
condition is replaced by an Abel-zero equation.

## 1. Statements in the original family

Let $p\ge41$ and $p\equiv2,5\pmod9$. Put

$$
n=p+1,\qquad m=n/6,\qquad
\mathcal H=\{h\bmod n:h\equiv1\pmod6\},\qquad
\mathcal H^*=\{h\in\mathcal H:(h,n)=1\},
$$
$$
g=|\mathcal H^*|=\varphi(n)/2,\qquad
F_0=\mathbb Q(\zeta_n)^+.
\tag{733.1}
$$

For every $h\in\mathcal H$, use $\theta_h=\theta^h$ in the actual
finite cuspidal model and set

$$
N_h=G(e_0,\operatorname{Tr}_{\mathsf T_\zeta}e_0).
\tag{733.2}
$$

The form, split vector, and torus in this notation are exactly
those of R727/R730, in the representation attached to $\theta_h$.

**Theorem 733.1.** All $N_h$ for $h\in\mathcal H$ are nonnegative
real numbers, and

$$
\boxed{
\sum_{h\in\mathcal H}N_h<13mp.
}
\tag{733.3}
$$

The norms for $h\in\mathcal H^*$ are strictly positive. Consequently

$$
\boxed{
\left(\prod_{h\in\mathcal H^*}N_h\right)^{1/g}
 <5p(2+\log_2p).
}
\tag{733.4}
$$

This is a bound for the precise original scalars, not for a
conveniently conjugated torus with a different split vector.

**Theorem 733.2.** Suppose the specified original $M_{2,1}$ is
nonzero. Then

$$
\boxed{
\min_{h\in\mathcal H^*}2v_p(M_{2,h})
 <
 4+\frac{128\log2+\log(2+\log_2p)}{\log p}.
}
\tag{733.5}
$$

In particular, if $p\ge2^{136}$, one can choose an actual primitive
$h$ for which $M_{2,h}\ne0$ and $v_p(M_{2,h})\le2$.
For that embedding, the complete original coarse Abel increment
satisfies

$$
\boxed{
\frac{16\mathcal I_h(p^8u)}{p^8M_{2,h}}
 =u+pH_h(u),\qquad
 H_h\in u^2\mathbb Z_p\langle u\rangle.
}
\tag{733.6}
$$

It is an exact isometric automorphism of the closed unit disc.
The true component is still $J_h=c_h\mathcal I_h$ with its original
nonzero KS scalar.

By R729, the nonvanishing hypothesis holds for all sufficiently
large allowed primes. Thus the original Abel vector is injective
on its fixed closed depth-eight disc for every such prime.
The chosen component may vary with $p$.

## 2. The full positive family still consists of cuspidal representations

For $h\in\mathcal H$, primitivity of order $n$ is not required in
the proof of (733.3). The finite representation exists because

$$
\theta_h(\zeta)=\zeta^{-1}\ne1.
$$

Thus $\theta_h$ is nontrivial and is not quadratic. Its character
on the order-two projective element is still $-1$, since $h$ is odd.
The general finite cuspidal model of R727 therefore applies.

The Borel module of functions on $\mathbb F_p$ modulo constants
is irreducible. Its invariant positive Hermitian form is the same
normalized form

$$
G(e_r,e_s)=p\delta_{rs}-1
$$

for every such $\theta_h$. Finite-group averaging onto the
$\mathsf T_\zeta$-fixed space is an orthogonal projection. Hence

$$
N_h=(p+1)G(A_he_0,A_he_0)\ge0,\qquad
A_h=(p+1)^{-1}\operatorname{Tr}_{\mathsf T_\zeta}.
\tag{733.7}
$$

For primitive $h$, R727/R730 additionally give
$N_h=\sigma_h(N_1)\ne0$. We use nonnegativity for the full family
and strict positivity only for the primitive product.

## 3. Each torus element meets at most twelve relevant field elements

In the original basis $(\zeta,1)$ the actual torus has exactly
the identity and the following $p$ elements in
$\mathrm{PGL}_2(\mathbb F_p)$:

$$
g_x=
 \begin{pmatrix}x&-1\\1&x+1\end{pmatrix},
\quad x\in\mathbb F_p,\qquad
\Delta_x=x^2+x+1.
\tag{733.8}
$$

Since $p\equiv2\pmod3$, every $\Delta_x$ is nonzero.
Let $u(a)=\left(\begin{smallmatrix}1&a\\0&1\end{smallmatrix}\right)$,
and use the original
$w=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
The exact projective Bruhat decomposition is

$$
g_x=u(x)\operatorname{diag}(\Delta_x,1)\,w\,u(x+1).
\tag{733.9}
$$

The matrix on the right is $-g_x$, which is the same projective
element. Its action on the vector is computed by the original
Weyl formula. Pairing with $e_0$ gives, with no residual factor $p$,

$$
G(e_0,g_xe_0)
 =-\!\!\sum_{\substack{y\in\mathbb F_{p^2}^{\times}\\
        (x+1)N(y)+\operatorname{Tr}(y)=-x/\Delta_x}}
           \overline{\theta(y)}^{\,h}.
\tag{733.10}
$$

Indeed the affine left factor sends the Weyl output index $j$
to $x+\Delta_xj$, so the displayed fiber is exactly the condition
that it becomes zero. The constant part of $G$ contributes
$\sum_y\theta_h(y)=0$.

The characters in $\mathcal H$ are $h=1+6j$, $0\le j<m$.
For any character value $q=\theta(y)\in\mu_n$,

$$
\sum_{h\in\mathcal H}\overline q^{\,h}
 =\begin{cases}
   m\overline q,&q^6=1,\\
   0,&q^6\ne1.
  \end{cases}
\tag{733.11}
$$

The map
$\theta:\mathbb F_{p^2}^{\times}\to\mu_n$
is onto with kernel $\mathbb F_p^\times$. Its inverse image of
$\mu_6$ is therefore a disjoint union of six nonzero
$\mathbb F_p$-lines. Choose one nonzero representative $y_0$
of any of these lines and write $y=\lambda y_0$,
$\lambda\in\mathbb F_p^\times$.

The fiber in (733.10) becomes

$$
(x+1)N(y_0)\lambda^2+
        \operatorname{Tr}(y_0)\lambda+x/\Delta_x=0.
\tag{733.12}
$$

If $x\ne-1$, its quadratic coefficient is nonzero.
If $x=-1$, its constant coefficient is $-1$, since
$\Delta_{-1}=1$. Thus it is never the zero polynomial,
including the trace-zero line. It has at most two roots.
Each of the six lines contributes at most two field elements,
so at most twelve summands in (733.10) survive the full-family
sum (733.11).

Every surviving term of (733.11) has absolute value $m$.
It follows that

$$
\left|\sum_{h\in\mathcal H}G(e_0,g_xe_0)\right|
 \le12m\qquad(x\in\mathbb F_p).
\tag{733.13}
$$

This argument includes every exceptional fiber. It does not
assume the $h=1$ fiber sum stays constant for the other characters.

## 4. The full mean and the primitive geometric mean

The identity element contributes $G(e_0,e_0)=p-1$ for every $h$.
Summing the remaining $p$ torus elements and applying (733.13)
gives

$$
0\le\sum_{h\in\mathcal H}N_h
 \le m(p-1)+12mp<13mp,
$$

proving (733.3).
All the terms outside the primitive family are nonnegative by
(733.7), so

$$
\sum_{h\in\mathcal H^*}N_h<13mp.
$$

The arithmetic-geometric mean inequality yields

$$
\left(\prod_{h\in\mathcal H^*}N_h\right)^{1/g}
 <13p\,\frac mg
 =\frac{13p}{3}\frac n{\varphi(n)}.
\tag{733.14}
$$

Only an elementary totient estimate is needed.
Write the distinct prime divisors of $n$ in increasing order
$q_1<\cdots<q_k$. Then $q_j\ge j+1$ and

$$
\frac n{\varphi(n)}
 =\prod_{j=1}^k\frac{q_j}{q_j-1}
 \le\prod_{j=1}^k\frac{j+1}{j}=k+1
 \le1+\log_2n.
\tag{733.15}
$$

The last inequality follows from $2^k\le n$.
Since $n=p+1<2p$ and $13/3<5$, (733.14)–(733.15)
prove (733.4). No prime-distribution estimate, unproved
uniform character-sum bound, or restriction on the factorization
of $p+1$ is used.

## 5. Apply the same original global integral norm

Keep R717/R730's original quantities

$$
\mathcal P=S_2(\theta)S_3(\theta^{-1})/C_0^2\in F_0,
\quad N=N_1\in\mathcal O_{F_0},
\quad D=2^{37}3^{26}p^5,
\quad D\mathcal P\in\mathcal O_{F_0}.
$$

The nonvanishing of $M_{2,1}$ makes $DN\mathcal P$ a nonzero
algebraic integer. Its primitive conjugates use precisely the
same $N_h$ as above. The exact norm relation remains

$$
M_{2,h}^2
 =-\frac{8\zeta^2N_h}{(p+1)^2}C_0^2\sigma_h(\mathcal P).
\tag{733.16}
$$

R730 proves, from the full AFE and all lattice tails,

$$
|\sigma_h(\mathcal P)|<2^{36}p^3
\quad\text{for every }h\in\mathcal H^*.
\tag{733.17}
$$

Multiplying (733.17) over all primitive embeddings, then
using the geometric mean (733.4) and $2^{37}3^{26}<2^{89}$,
gives the improved field norm bound

$$
\begin{aligned}
0<
\left|N_{F_0/\mathbb Q}(DN\mathcal P)\right|^{1/g}
 &<2^{89}p^5\cdot2^{36}p^3\cdot5p(2+\log_2p)\\
 &<2^{128}p^9(2+\log_2p).
\end{aligned}
\tag{733.18}
$$

The prime $p$ splits completely in $F_0$. All the other
scalars in (733.16) are $p$-units. Thus the exact valuation
identity from R730 is

$$
v_p\left(N_{F_0/\mathbb Q}(DN\mathcal P)\right)
 =5g+2\sum_{h\in\mathcal H^*}v_p(M_{2,h}).
\tag{733.19}
$$

Each number $2v_p(M_{2,h})$ is an integer.
Comparing (733.18)–(733.19), dividing by $g$, and taking a
minimum proves (733.5).

For the stated explicit size condition, put $L=\log_2p$.
When $L\ge136$,

$$
128+\log_2(L+2)<L.
$$

At $L=136$ this follows from $138<256$; the function
$L-128-\log_2(L+2)$ is strictly increasing for $L\ge136$.
Hence the right side of (733.5) is less than five.
At least one of the integral numbers $2v_p(M_{2,h})$ is
therefore at most four. This proves the claimed
$v_p(M_{2,h})\le2$.

This conclusion selects an actual primitive component. It is not
a bound on a weighted sum of unrelated twists.

## 6. The complete depth-eight isometry

Fix such an $h$, and set $\eta=v_p(M_{2,h})\le2$.
R730 §§5–6 prove for every actual primitive embedding, without
a residue-unit hypothesis,

$$
M_{3j-1,h}/M_{2,h}\in\mathbb Q_p,\qquad
E_{j,h}=\frac{p^{3j}M_{3j-1,h}}{(3j)!},
$$
$$
v_p(E_{j,h})\ge
 \frac{3j-1}{p+1}-v_p(3j)>0,\qquad
v_p(E_{j,h})\longrightarrow\infty.
\tag{733.20}
$$

These are complete series estimates, not prefix bounds.
Normalize by $E_{1,h}=p^3M_{2,h}/6$ and write

$$
G_h(V)=V+\sum_{j\ge2}b_{j,h}V^j,\qquad
b_{j,h}=E_{j,h}/E_{1,h}\in\mathbb Q_p.
$$

Equation (733.20) gives

$$
v_p(b_{j,h})>-\eta-3\ge-5.
$$

The coefficients $b_{j,h}$ have integer valuations, regardless
of the valuation class of the separate jets. Therefore

$$
b_{j,h}\in p^{-4}\mathbb Z_p,\qquad
v_p(b_{j,h})\longrightarrow\infty.
$$

It follows that

$$
G_h(p^5u)/p^5\in u+p\,u^2\mathbb Z_p\langle u\rangle.
\tag{733.21}
$$

The complete original coarse change is

$$
V=\Psi(s/p^3),\qquad
\Psi(v)=\frac38v+p\,v^2\mathbb Z_p\langle v\rangle.
$$

At $s=p^8u$, compose (733.21) with
$\Psi(p^5u)/p^5=(3/8)u+p\,u^2\mathbb Z_p\langle u\rangle$.
Exactly as in R730, the normalization is

$$
\frac{16\mathcal I_h(p^8u)}{p^8M_{2,h}}
 =\frac83\,\frac{G_h(\Psi(p^5u))}{p^5}
 =u+pH_h(u).
$$

This proves (733.6) in the entire Tate algebra.
R730's explicit contraction and difference-factorization proof
then supplies the restricted inverse and the exact valuation

$$
v_p\bigl(\mathcal I_h(s_1)-\mathcal I_h(s_2)\bigr)
 =v_p(M_{2,h})+v_p(s_1-s_2)
\qquad(s_1,s_2\in p^8\mathcal O).
\tag{733.22}
$$

The original component $J_h$ adds $v_p(c_h)$. The scalar was
never silently normalized to a unit.

## 7. Scope

The finite-character average (733.3) is unconditional for each
allowed prime. The local depth-eight conclusion holds whenever
the original $M_{2,1}$ is nonzero and $p\ge2^{136}$; R729
therefore makes it unconditional for all sufficiently large
allowed primes.

The proof does not select one fixed finite list of labels.
Such a list of labels $h>1$ cannot remain primitive for all
allowed primes, as proved in
[the fixed-label note](../notes/fixed-finite-h-primitivity-obstruction.md).
The norm average supplies a label that is primitive for the
prime actually under consideration.

Depth eight remains deeper than the complete depth-four
candidate region. More importantly, the rational-point condition
at positive rank is still the original height condition, with
its fixed constants and line bundles. Neither (733.3) nor
(733.6) determines those height coefficients. The original
$q/\beta$ functions and common-root certificate remain open.

Dependencies:
[R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md),
[R729](R729-uniform-full-Abel-nonvanishing-and-valuation-bound.md),
[R730](R730-fixed-depth-original-Abel-isometry-by-all-embedding-norm.md).
All additional finite-field counts, norm averages, constants,
and all-tail changes of depth are proved above.
