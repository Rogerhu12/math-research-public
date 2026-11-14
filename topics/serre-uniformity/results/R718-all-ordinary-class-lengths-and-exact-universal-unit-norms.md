# R718: every ordinary class length and the exact universal unit norms

Date: 2026-11-14. **Status: proved.** This is the higher-layer
continuation of R715. It uses R686's actual compatible pure-$p$
fields and R700's integral reciprocity sequence at every level.
It does not extrapolate a level-one Robert calculation.

Keep the original $p=43,q,\Gamma,\pi,\mathcal O,k$, all prime
labels, and the same unaveraged character projector. Let

$$
B_n=K(A_0[p^{n+1}])^{\mu_{42}},\quad
M_n=LB_n,\quad
P_n=S_n\times T_n\simeq C_{p^n}^2,\quad n\ge1,
$$
$$
F_{t,n}=B_n^{S_n},\qquad N_n=LF_{t,n}=M_n^{S_n}.
$$

Then

$$
\boxed{A_{M_n}\simeq R_\Gamma/\pi^{42n+1}
\quad\text{for every }n\ge1.}
\tag{718.1}
$$

Thus the single parameter $d$ of R686 is now determined:

$$
\boxed{d=\infty,\qquad
\varprojlim_{\,N} A_{M_n}\simeq R_\Gamma.}
\tag{718.2}
$$

Moreover, for the full ordinary unit lattices,

$$
\boxed{N_{S_n}E_{M_n}=E_{N_n},\qquad
N_{P_n}E_{M_n}=(p,\pi)E_L\quad(n\ge1).}
\tag{718.3}
$$

Consequently the intersection of the ordinary norms to the
original $L$ is exactly

$$
\boxed{\bigcap_{n\ge1}N_{M_n/L}E_{M_n}=(p,\pi)E_L.}
\tag{718.4}
$$

All equalities are in the same completed ordinary character
lattices. They assert existence and exact norm images; they
do not give numerical coordinates of a norm preimage of
the original $y$, and do not evaluate $C,J,b,\mathcal L$.

## 1. Integral inputs at each level

R686 proves separately at every $n$ that

$$
A_n:=A_{M_n}=R_\Gamma/\pi^{m_n},\qquad
1\le m_n\le42n+1.
\tag{718.5}
$$

The class norms are onto and identify

$$
m_n=\min(m_{n+1},42n+1),\qquad
m_n=\min(d,42n+1).
\tag{718.6}
$$

For $m_n\ge2$, the original compatible scalar generator
$s_\infty=1+p$ acts by

$$
s=1+i\pi+O(\pi^2)
\quad\text{on }A_n.
\tag{718.7}
$$

The anti-scalar generator is the actual
$t_\infty=\exp(21pi)$ of R686. Its first coefficient,
when defined, lies in $\mathbf F_p$. For the argument
below only $t\equiv1\bmod\pi$ is needed. When $m_n=1$,
both generators act trivially; no first coefficient is
assigned.

R700 supplies, for this actual $n$, the full exact sequence

$$
0\longrightarrow E_n\longrightarrow U_n
\longrightarrow X_n^{(p)}
\longrightarrow A_n\longrightarrow0,
$$
$$
U_n\simeq\mathcal O[P_n]^{86},\qquad
X_n^{(p)}\simeq\mathcal O[P_n]^{43}.
\tag{718.8}
$$

Its freeness was proved at all levels using the actual
primitive $q$ Frobenius, global cohomology, and local
unit norms. No conjectural ordinary norm surjectivity
is an input to (718.8).

The full invariant ordinary lattice is
$E_n^{P_n}=E_L=R_0y$. The proof is the same integral
invariants argument as R715: invariant ordinary units
are ordinary units of the fixed field before completion,
flat completion preserves the kernel, and no $p$-power
root of unity occurs in a field of absolute degree
$88p^{2n+1}$. All actions commute with $\Gamma$.

## 2. Natural dimension shift and the product-group resolution

Applying the two natural connecting maps of (718.8)
gives, for every subgroup $H\le P_n$,

$$
\widehat H^j(H,E_n)\simeq
\widehat H^{j-2}(H,A_n)
\tag{718.9}
$$

as $R_0$-modules. As in R715, no
$\Gamma$-compatible free basis is required.
In particular,

$$
E_L/N_{P_n}E_n\simeq H_1(P_n,A_n).
\tag{718.10}
$$

The standard integral resolution obtained by tensoring
the two cyclic resolutions has the degree-one maps

$$
d_1(x,z)=(s-1)x+(t-1)z,
$$
$$
d_2(c,d,e)=
\bigl(N_{S_n}c-(t-1)d,\ (s-1)d+N_{T_n}e\bigr).
\tag{718.11}
$$

The maps have the same form for order $p^n$ as for
order $p$; the actual norm operators now have $p^n$
terms. In particular neither of these operators is
silently replaced by the order-$p$ norm.

## 3. Uniform valuations of the actual p-power norm operators

For any integral $w\equiv1\bmod\pi$, put

$$
\mathcal N_p(w)=1+w+\cdots+w^{p-1}.
$$

Writing $w=1+\pi c$, the exact polynomial expansion is

$$
\mathcal N_p(w)=
\sum_{j=1}^p\binom pj(\pi c)^{j-1}.
$$

Every term has $\pi$-valuation at least $42$, since
$v_\pi(p)=42$. This also holds for $w=1$, for which
the norm is exactly $p$. The factorization

$$
\mathcal N_{p^n}(w)=
\prod_{r=0}^{n-1}\mathcal N_p(w^{p^r})
$$

therefore proves

$$
v_\pi\bigl(\mathcal N_{p^n}(w)\bigr)\ge42n.
\tag{718.12}
$$

For a lift $v=1+i\pi+O(\pi^2)$ of the actual scalar
action, R686 proves

$$
v_\pi(v^{p^n}-1)=42n+1,\qquad v_\pi(v-1)=1.
$$

Since
$(v-1)\mathcal N_{p^n}(v)=v^{p^n}-1$
in the DVR $R_\Gamma$, the scalar norm has the sharper
exact value

$$
\boxed{v_\pi(N_{S_n})=42n,\qquad
v_\pi(N_{T_n})\ge42n.}
\tag{718.13}
$$

These statements concern scalar lifts in the DVR;
their reduction to $A_n$ is the actual group action.
Different lifts agree on $A_n$, so the use of a lift
does not create an additional hypothesis.

## 4. The cyclicity contradiction rules out every shorter length

Suppose $m_n\le42n$. Then (718.12) makes both norms
zero on $A_n$. If $m_n=1$, all maps in (718.11)
vanish and $H_1(P_n,A_n)=k^2$.

If $m_n\ge2$, write

$$
s-1=\pi\alpha,\quad \alpha\in A_n^\times,\qquad
t-1=\pi\beta,\quad
\eta=\alpha^{-1}\beta.
$$

The change of variables
$(x,z)\mapsto(z,x+\eta z)$
identifies $\ker d_1$ with
$A_n\oplus\operatorname{Ann}_{A_n}(\pi)$.
The mixed boundary identifies its first coordinate
modulo $\pi A_n$, and the two norm boundaries are
zero. Thus, exactly as $R_0$-modules,

$$
H_1(P_n,A_n)\simeq
(A_n/\pi A_n)\oplus\operatorname{Ann}_{A_n}(\pi)
\simeq k^2.
\tag{718.14}
$$

This calculation does not require $pA_n=0$.
For $n>1$ and longer $m_n$, multiplication by $p$
on $A_n$ can be nonzero; only the two actual
$p^n$-norms were set to zero. The two resulting
summands in (718.14) are nevertheless killed by $\pi$.

The left side of (718.10) is a quotient of the
cyclic $R_0$-module $R_0y$. It cannot be
the $\Gamma$-trivial module $k^2$.
This contradiction proves $m_n>42n$.
The upper bound (718.5) now gives
$m_n=42n+1$ for this arbitrary $n$, proving (718.1).

## 5. The exact full norms at the endpoint

At $m_n=42n+1$, (718.13) gives

$$
N_{S_n}A_n=\pi^{42n}A_n
=\operatorname{Ann}_{A_n}(\pi).
\tag{718.15}
$$

In the coordinates used for (718.14), the mixed
boundary kills $\pi A_n\oplus0$, and the scalar
norm boundary kills the entire second summand.
The anti-scalar norm boundary has first coordinate
in $\pi^{42n}A_n\subset\pi A_n$, so it cannot
kill the remaining first-coordinate quotient.
Therefore

$$
H_1(P_n,A_n)\simeq A_n/\pi A_n\simeq k.
\tag{718.16}
$$

Combining (718.10), the cyclic generator $y$,
and the unique maximal ideal $(p,\pi)$ of
$R_0$ proves
$N_{P_n}E_n=(p,\pi)E_L$.
Since the same subgroup occurs for every $n$,
its intersection is (718.4).

This intersection is also the image of the genuine
norm-compatible inverse limit $\varprojlim_N E_n$ in $E_L$.
Indeed, for a fixed $u\in(p,\pi)E_L$, each norm fiber
$\mathcal F_n=\{x\in E_n:N_{M_n/L}x=u\}$ is a nonempty
compact subset of the finite-rank $\mathcal O$ lattice $E_n$.
In the compact product $\prod_n\mathcal F_n$, the norm
compatibility conditions are closed, and any finite
collection can be satisfied by choosing a point at the
highest involved level and taking its successive norms.
The finite intersection property gives a compatible
sequence over all $n$; conversely every such sequence
maps to the displayed intersection.

## 6. Scalar ordinary norms are onto at every level

For the cyclic subgroup $S_n$, the scalar action
has $(s-1)A_n=\pi A_n$, its invariant group is
$\pi^{42n}A_n$, and (718.15) is the full norm
onto that invariant group. Also

$$
\ker(N_{S_n}:A_n\to A_n)=\pi A_n=(s-1)A_n.
$$

Both cyclic Tate groups of $A_n$ vanish. Cyclic
periodicity and (718.9) imply that the corresponding
Tate groups of the full ordinary lattice $E_n$
vanish as well. In degree zero this is precisely

$$
E_{N_n}/N_{S_n}E_n=0.
\tag{718.17}
$$

Thus the first equality of (718.3) is an ordinary
unit statement, not a Hasse field-norm substitute.
It recovers R715 when $n=1$. In particular the
original $y$, viewed in each $E_{N_n}$, has
an ordinary scalar norm preimage at each $n$.
No compatibility of chosen preimages is asserted
without an additional inverse-limit argument.

## 7. The infinite class parameter and the remaining numerical problem

Equation (718.1) is unbounded in $n$, so R686's
$d=\sup_n m_n$ is infinite. R686 already proves
that the cyclic presentations can be chosen
compatible with the actual ordinary class norms.
Taking the inverse limit of the quotients
$R_\Gamma/\pi^{42n+1}$ therefore gives the
complete DVR $R_\Gamma$, proving (718.2).

There is no remaining finite-length stabilization
alternative. This conclusion uses the natural
ordinary comparison at each layer, not a new
numerical window or a guessed class-field action.

The coefficient $b$ is defined at every nontrivial
layer and is compatible with the norm maps, but its
value is not fixed by these length calculations.
Neither the original $C$, the original first
moment $J$, nor the marked ordinary norm units
have been evaluated here.

Dependencies:
[R686](R686-all-p-power-layers-and-exact-ordinary-class-growth-law.md),
[R700](R700-p-ramified-free-lattices-and-the-retained-ordinary-quotient.md),
and
[R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md).
All additional homology calculations, norm valuations,
and endpoint deductions have been proved above.
