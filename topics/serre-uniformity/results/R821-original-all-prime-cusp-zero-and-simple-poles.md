# R821 — All original primitive cusp images are zero and the original quotient function has simple cusp poles

Date: 2026-11-15. Status: **proved** for the original arithmetic range of R725. This is an assertion on actual integral homomorphisms and their fixed $c_0$-normalized curve maps. No torsion point is discarded by tensoring its value with $\mathbf Q$.

## 1. The actual integral Hom lattice and the fixed normalization

Let
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
n=p+1=6m,\qquad K=\mathbf Q(\zeta_3),
\qquad c=(p-1)/2.
\tag{821.1}
$$
Then $m>1$ and $3\nmid m$. Keep the original fields $H,L$, target
$C/L:y^2=x^3+b$, and positive CM embedding of R725. The original source is
$$
X=X_p,\qquad j=6912a^3(1-a^3),\qquad
\delta(a)=\zeta_3 a,\qquad
\phi:X\longrightarrow Y=X/\langle\delta\rangle,\quad t=a^3.
\tag{821.2}
$$
The original $c_0$ is the $\mathbf Q$-rational CM point $a=0$ of R616(616.4–5), and the actual primitive quotient is $q:J_X\to A=A_{\theta,1}$.

Define the **full original integral lattice**
$$
\Lambda_{\rm orig}
=
\operatorname{Hom}_L(J_{X,L},C)
\ \cap\
\bigl(\operatorname{Hom}_L^0(A_L,C)\circ q\bigr)
\quad\text{inside }\operatorname{Hom}_L^0(J_{X,L},C).
\tag{821.3}
$$
Here $\operatorname{Hom}^0=\operatorname{Hom}\otimes_{\mathbf Z}\mathbf Q$.
This intersection includes all actual integral maps with the original primitive factor, even if their expression through a selected isogenous quotient uses a denominator.

For $u\in\Lambda_{\rm orig}$ the curve map is fixed, with no remaining translation:
$$
f_u(x)=u([x-c_0]),\qquad f_u(c_0)=O.
\tag{821.4}
$$
The Abel map $x\mapsto[x-c_0]$ is defined over $\mathbf Q$, so $f_u$ is $L$-defined and is additive in $u$. We do not start at a nonrational cusp. We do not first assume a cusp value is zero to obtain descent or additivity.

The positive action from R575 is $q\delta_J=[\zeta_3]q$ on the original factor. Its $K$ action on holomorphic differentials is the positive scalar action, also used on $C$. It follows for every $u$ in (821.3) that
$$
u\delta_J=[\zeta_3]u,\qquad
f_u\delta=[\zeta_3]f_u.
\tag{821.5}
$$
For a map expressed through a rational isogeny this is first an equality in the rational Hom space, hence an equality of actual homomorphisms: a Hom group of characteristic-zero abelian varieties is torsion-free. The curve identity then uses $\delta(c_0)=c_0$ and the fixed normalization (821.4), so no constant translation remains.

## 2. A cusp value is an actual three-torsion point

By R816, each cusp of $Y$ has a unique point above it in $X$, totally ramified of degree three under $a^3=t$. Consequently every geometric cusp $P$ of $X$ is fixed by $\delta$. Equation (821.5) therefore implies
$$
f_u(P)\in C[1-\zeta_3]
=\{O,(0,\sqrt b),(0,-\sqrt b)\}.
\tag{821.6}
$$
The group of points in (821.6) is cyclic of order three over a field containing $\sqrt b$. Over a smaller field it can consist only of $O$.

Fix an embedding of one cusp residue field over $K$. R816 identifies it exactly as
$$
K_c=K\mathbf Q(\xi_p)^+,\qquad [K_c:K]=c.
$$
Moreover
$$
[L:K]=m,\qquad \gcd(m,c)=1,\qquad L\cap K_c=K.
\tag{821.7}
$$
Both extensions of $K$ are Galois, so they are linearly disjoint. Put $M=LK_c$. The cusp $P$ is an $M$-point; in fact its chosen coordinates lie in $K_c$. Thus
$$
e_P:\Lambda_{\rm orig}\longrightarrow C[1-\zeta_3](M),
\qquad e_P(u)=f_u(P)
\tag{821.8}
$$
is an actual additive homomorphism of abelian groups, before any rationalization of its target.

## 3. Compatibility with the original integral operator

Use the same generator $g$ of $\operatorname{Gal}(H/K)$ as R819, and put
$$
\sigma=g|_L,\qquad \rho=g(r)/r\in L^\times,\qquad
\mathcal T u=D_{\rho^{-1}}\circ{}^\sigma u.
\tag{821.9}
$$
R728 and R819 prove that this is the actual primitive operator under Weil adjunction. It preserves (821.3): the Galois conjugate of an actual integral homomorphism is integral, $D_{\rho^{-1}}:C^\sigma\to C$ is an actual isomorphism, and the original primitive rational space is stable under this operator. Its inverse is of the same form.

On that rational primitive space,
$$
\Phi_n(\mathcal T)=0.
\tag{821.10}
$$
Because all coefficients of $\Phi_n$ are integers and $\mathcal T$ preserves the actual integral lattice, the left side of (821.10) is an actual integral homomorphism. An actual homomorphism which is zero after tensoring with $\mathbf Q$ is zero: if a nonzero integer multiple were zero, its connected image would lie in a finite torsion subgroup, which is impossible. Hence (821.10) is an exact equality on $\Lambda_{\rm orig}$, with no residual torsion-valued error.

By (821.7), $\sigma$ has a unique extension $\widetilde\sigma$ to $M$ which fixes $K_c$ pointwise. In particular it fixes the chosen cusp $P$ and $c_0$. Define
$$
S:C[1-\zeta_3](M)\longrightarrow C[1-\zeta_3](M),
\qquad
R\longmapsto D_{\rho^{-1}}\widetilde\sigma(R).
\tag{821.11}
$$
The first map sends $C$ to $C^\sigma$, and the second sends $C^\sigma$ back to $C$. Both are invertible and commute with the fixed $\zeta_3$ action. Thus $S$ is an automorphism of the group in (821.6), and the exact normalization (821.4) gives
$$
e_P(\mathcal T u)=S(e_P(u)).
\tag{821.12}
$$
If this group is nontrivial, its only automorphisms are multiplication by $\epsilon=1$ and $\epsilon=-1$. The choice of $\epsilon$ is fixed by (821.11) and is independent of $u$. If the group is trivial, the desired zero assertion already holds.

## 4. The cyclotomic polynomial kills no nonzero cusp value

We need the following exact integer evaluations:
$$
\boxed{\Phi_n(1)=\Phi_n(-1)=1.}
\tag{821.13}
$$
First, $n=6m$ has at least the two distinct prime divisors $2$ and $3$, so $\Phi_n(1)=1$. Here we use the elementary formula
$\Phi_N(1)=\ell$ if $N>1$ is a power of one prime $\ell$, and $\Phi_N(1)=1$ otherwise. It follows, for example, by taking the limit at $T=1$ in the Möbius product for $\Phi_N(T)$.

For the second evaluation there are two cases.

- If $v_2(n)\ge2$, then $\Phi_n(T)$ is an even polynomial. Hence $\Phi_n(-1)=\Phi_n(1)=1$.
- If $v_2(n)=1$, then $m$ is odd and $d=n/2=3m$ is odd. The identity $\Phi_{2d}(T)=\Phi_d(-T)$ gives $\Phi_n(-1)=\Phi_d(1)$. Since $m>1$ and $3\nmid m$, the integer $d=3m$ has at least two distinct prime divisors. Thus $\Phi_d(1)=1$.

Apply the additive map $e_P$ to (821.10). By (821.12), in the nontrivial-group case,
$$
0=e_P(\Phi_n(\mathcal T)u)
 =\Phi_n(S)e_P(u)
 =\Phi_n(\epsilon)e_P(u)
 =e_P(u).
\tag{821.14}
$$
The last equality uses the integer identity (821.13), not a reduction of the target point in a rational vector space.

We have proved:

**Theorem 821.1.** Every $u\in\Lambda_{\rm orig}$ satisfies
$$
\boxed{f_u(P)=O\quad\text{at every geometric cusp }P\text{ of }X.}
\tag{821.15}
$$
The proof can be repeated for any chosen cusp. Alternatively, the single $G_L$-orbit from R816 transports the zero value of the $L$-defined map to all of them.

For $p=41$ this agrees with the already computed complete-lattice result R764(764.1–3). No old cusp period or finite computation is repeated here. The new statement is the displayed general-prime integral argument.

## 5. Exact cusp poles of the original single function on $Y$

Assume now $u\ne0$ and write the actual nonconstant map as
$$
f_u=(x_u,y_u):X\longrightarrow C.
$$
Its degree is denoted by $d_u$. By (821.5),
$$
\delta^*x_u=\zeta_3x_u,\qquad \delta^*y_u=y_u,
$$
so the **same target coordinate** $y$ gives a function
$$
y_u\in L(Y),\qquad r_u=x_u/a\in L(Y),\qquad
y_u^2-b=t\,r_u^3.
\tag{821.16}
$$
This is the original coordinate on the original target, with the fixed $c_0$ normalization. No translated $y$ or replacement quotient variable is used.

R819 proves that every nonzero original primitive Hom direction is unramified at every cusp. This also applies to the full lattice (821.3): clear the denominator of its expression through $q$, apply R819 to the resulting map $[N]f_u$, and use that multiplication by $N\ne0$ on $C$ is étale in characteristic zero. At a cusp $P$ of $X$, (821.15) gives $f_u(P)=O$ and the local degree of $f_u$ is therefore one. The invariant Weierstrass coordinates on $C$ have orders
$$
\operatorname{ord}_O x=-2,\qquad \operatorname{ord}_O y=-3.
$$
Consequently
$$
\operatorname{ord}_P x_u=-2,\qquad
\operatorname{ord}_P y_u=-3.
\tag{821.17}
$$
If $Q=\phi(P)$, the map $\phi$ is totally ramified of degree three there. Since $y_u$ descends to $Y$, (821.17) gives
$$
\boxed{\operatorname{ord}_Q y_u=-1.}
\tag{821.18}
$$
Thus every original cusp of $Y$ is a simple pole of the original $y_u$.

Let $D_{\rm cusp}$ be the reduced cusp divisor on $Y_L$. R816 gives
$\deg D_{\rm cusp}=c$. Since $y:C\to\mathbf P^1$ has degree three and
$X\to Y$ has degree three,
$$
\deg(y_u:Y\to\mathbf P^1)=d_u.
$$
We therefore obtain the exact divisor decomposition
$$
\boxed{
(y_u)_\infty=D_{\rm cusp}+E_u,\qquad
E_u\ge0,\qquad
\operatorname{supp}(E_u)\cap\operatorname{supp}(D_{\rm cusp})=\varnothing,
\qquad \deg E_u=d_u-c.
}
\tag{821.19}
$$
Both divisors descend to $L$. In particular $d_u\ge c$. The noncusp divisor $E_u$ remains to be determined from the actual function; (821.19) does not supply its support.

The same local calculation also fixes two useful original orders. R816 gives $\operatorname{ord}_P a=-p$. Hence
$$
\operatorname{ord}_Q r_u=(p-2)/3.
\tag{821.20}
$$
If $h_u=f_u^*\omega_C$ and $\eta_u=h_u/a$, then $\eta_u$ is the descended meromorphic differential on $Y$, and unramifiedness gives
$$
\operatorname{ord}_P h_u=0,\qquad
\operatorname{ord}_Q\eta_u=(p-2)/3.
\tag{821.21}
$$
Indeed pullback of a differential through a characteristic-zero ramification point of index three has order $3\operatorname{ord}_Q(\eta_u)+2$, whereas $h_u/a$ has order $p$ at $P$. Equations (821.20–21) retain the original parameter $a$ and original differential scale.

## 6. Boundary and original sources

The result fixes all actual cusp values and their simple pole contribution for every original primitive integral map in the stated range. It does not compute the remaining poles, the value at $c_1$, a height, a Néron/Manin unit or the same-label critical Cartier/Legendre product modulo $p$.

The hypothesis $p\equiv2,5\pmod9$ is retained. We have used $3\nmid m$ and the actual R725/R728 field construction; the excluded prime class is not silently added.

- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md) and [R616](R616-original-CM-point-difference-and-explicit-height-basis.md), especially (616.4–5): original positive action, quotient and rational $c_0$-normalization.
- [R725](R725-original-CM-elliptic-model-and-splitting-field.md) and [R728](R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md): actual fields, coordinate scaling, finite-order operator and primitive idempotent.
- [R816](R816-original-all-prime-real-cusp-orbit-and-degree-coprimality.md): exact cusp residue fields, coprime compositum and threefold total ramification.
- [R819](R819-original-primitive-Hom-field-and-all-cusp-nonramification.md): actual primitive Hom action and all-cusp nonramification.
- [R762](R762-original-mu3-quotient-and-single-function-map-recovery.md) and [R764](R764-certified-original-cusp-images-and-base-translation.md): the original fixed-coordinate and base-point conventions, with the already completed $p=41$ cusp certificate preserved.

No mathematical computation was run for this proof.
