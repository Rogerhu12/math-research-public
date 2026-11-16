# R150 appendix: original weak quadratic columns and positive critical jets

Astra-ISP-789f / literature_audit; AI-assisted with GPT-6 Astra Pro.  
2026-11-16.

## 1. Scope and paid inputs

This is a small **positive-certificate construction** for the original seventeen equations. It does not identify the complete higher-normal correction space. A zero gain is not a negative result for the full local module.

Let $K=\mathbb Q(\alpha)$ for one of the already proved irreducible polynomials

$$
F_+=-8+32s-25s^2+5s^3,\qquad
F_-=864+864s+135s^2+5s^3,
$$

$$
E_8=9600-25472s-3392s^2+15936s^3-2888s^4-936s^5
       +153s^6+50s^7+5s^8.
$$

Use the genuine local parameter $t=s-\alpha$. The original binomial moment change is invertible over $K[[t]]$ and gives $c,d,n_2,\ldots,n_{10}$. All seventeen equations times all monomials of total degree at most three give the full $6188$ source coordinates. The nonconstant target monomials of degree at most five give $4367$ coordinates.

The paid full generic rank is $4354$, the full constant rank is $4352$, and the generic left free rank is $13$. The original low $51\times36$ block has constant rank $25$, generic rank $27$, and positive local Smith indices $(3,3)$ at $F_\pm$ and $(2,2)$ at $E_8$. The respective full local length upper bounds are $8,8,5$.

See the [noncontact original projection lemma](R150-appendix-rank-one-noncontact-centered-rank-controls-macaulay-projection.md), the [two cubic low Smith calculations](R150-appendix-both-cubic-fields-low-smith33-and-original-nine-target-local-membership.md), and the [original low projection and E8 result](R150-appendix-original-low-projection-double-linear-divisor-and-E8-local-target-membership.md). Local lengths below are over $K$; field degrees enter only the global rational divisor degree.

## 2. Original coefficient interface

At $t=0$ write the actual original equations as

$$
F_i=q_i d^2+\sum_{j=2}^{10}
       (L_{ij}+cC_{ij}+dD_{ij})n_j
       +\sum_{2\le j\le l\le10}Q_{i,jl}n_jn_l,
\qquad 0\le i<17. \tag{2.1}
$$

No parameter-dependent primitive row factor is removed. In particular $q_i$ retains the actual $g(\alpha)$ factor, and $g(\alpha)\ne0$.

The $17\times9$ original constant linear matrix $L$ has rank eight. Choose $0\ne v\in\ker L$, and solve

$$
Lw+aCv+bDv=0,\qquad (w,a,b)\in K^9\oplus K^2. \tag{2.2}
$$

Its full kernel has dimension $1\le q\le3$: its matrix has rank at least eight, and $(v,0,0)$ is a nonzero kernel vector. The value of $q$ and all subsequent gains are measured, not prescribed.

## 3. Legal two-normal coefficient functionals

For a solution of (2.2), define a target coefficient functional by

$$
\begin{aligned}
Z(n_jn_l)&=v_jw_l+w_jv_l,\\
Z(cn_jn_l)&=a v_jv_l,\\
Z(dn_jn_l)&=b v_jv_l,
\end{aligned}
\qquad 2\le j\le l\le10, \tag{3.1}
$$

and set all other values to zero. These are values on ordinary monomials: $Z(n_j^2)=2v_jw_j$, whereas the two tangent values on $n_j^2$ are $a v_j^2$ and $b v_j^2$. No divided-power factor is added.

The value on $n_jF_i$ is

$$
v_j(Lw+aCv+bDv)_i+w_j(Lv)_i=0. \tag{3.2}
$$

The values on $cn_jF_i$ and $dn_jF_i$ are respectively $a v_j(Lv)_i$ and $b v_j(Lv)_i$. One-normal sources of tangent degree two cannot reach the support. A source with at least two normal factors could only reach degree two through $q_i d^2$, whose tangent degree is at least two and is again outside the support. Larger normal degrees also vanish.

Thus every original source outside

$$
F_i,\ cF_i,\ dF_i,\qquad 0\le i<17 \tag{3.3}
$$

vanishes. This accounts for all $6137$ rows outside the low $51$ rows, and the consumer checks them explicitly.

The map $(w,a,b)\mapsto Z$ is injective. If $Z=0$, the $cvv$ and $dvv$ values give $a=b=0$. Choose $j$ with $v_j\ne0$. The diagonal value gives $w_j=0$; the mixed values then give every $w_l=0$. A genuine kernel basis of (2.2) therefore gives $q$ independent legal columns.

There is no claim that this family exhausts all legal higher-normal corrections.

## 4. Small exact jet extension

Let $S(t)$ be the original $51\times36$ block: its target columns are the nine pure monomials of degrees one through three and the twenty-seven $n_j,cn_j,dn_j$. Put $e=3$ at $F_\pm$, and $e=2$ at $E_8$.

A true $25\times25$ constant unit gives canonical cochains

$$
X(t)=\sum_{k=0}^e t^kX_k,\qquad X_k\in K^{36\times11},
$$

with constant free coordinates $I_{11}$ and all higher free coordinates zero. The consumer verifies every original row in

$$
[t^k]S(t)X(t)=0\ (k<e),\qquad
R_e=[t^e]S(t)X(t),\qquad \operatorname{rank}R_e=2. \tag{4.1}
$$

Let $G$ be the $51\times q$ return of (3.1). Any nonzero rational row contents removed from $S$ are also removed from $G$ and $R_e$. The new equation is only

$$
S_0x+Ga+R_ec=0, \tag{4.2}
$$

of shape $51\times(47+q)$, at most $51\times50$.

Compute the full kernel and its actual projection to the eleven $c$ coordinates. If this projection has rank $r$, select independent image representatives. The corresponding original cochains are

$$
\lambda_k=\operatorname{embed}(X_kc)\quad(k<e),\qquad
\lambda_e=\operatorname{embed}(X_ec+x)+Za. \tag{4.3}
$$

Add the four exact pure functionals at $c^4,c^5,c^3d,c^4d$. They are exact for all parameters: every pure original term contains $d^2$, and every other term contains a normal factor.

All $6188$ original products are verified at each order $0,\ldots,e$, and the constant head rank is checked in the actual target coordinates. The output is therefore $r+4$ independent full original left heads modulo $t^{e+1}$.

## 5. Exact local-length consequence

The full module has thirteen free left heads and two positive Smith directions. Fifteen independent heads through order $e-1$ imply that both positive indices are at least $e$.

The $r+4=13+(r-9)$ independent heads through order $e$ imply that at least $h=r-9$ of the two positive indices are at least $e+1$. Consequently

$$
\boxed{\delta_{\mathrm{full},\alpha}\ge2e+h,\qquad h=r-9.} \tag{5.1}
$$

The program checks $9\le r\le11$ and compatibility with the paid full upper bound. It never assigns $h$ in advance.

If the two cubic computations each give $h=2$ and the E8 computation gives $h=1$, the extra global rational divisor degree is

$$
3\cdot2+3\cdot2+8\cdot1=20. \tag{5.2}
$$

This is conditional on the new actual positive certificates. Smaller gains give their actual smaller lower bounds. Zero gain concerns only the stated candidate family.

## 6. Physical reconstruction and verification

The original pure and one-normal coefficient polynomials are rebuilt through their exact degree bound $25$ by the pinned original physical generator, without interpolation. Every required low Taylor coefficient is checked against the complete original sparse action.

Only the quadratic-normal coefficients at $\alpha$ are needed, because the new quadratic functional occurs at the last cochain coefficient. They are rebuilt directly from the original $6\times6$ kernel, $J_2,J_3$, and

$$
N=4MKM+6(L_yM)_p,
$$

$$
\Gamma=2\operatorname{tr}(KMKM)y+8MKMp-12(L_yM)_{KMK}.
$$

All original pure coefficients and all linear and tangent-normal cross coefficients are checked against the polynomial generator at $\alpha$. Polarization then gives the forty-five ordinary quadratic coefficients. No uncomputed higher quadratic Taylor coefficient is set to zero: any attempted use is an error.

Complete cochains, original selected units, and complete kernels stay in temporary immutable checkpoints. Normal sectors three through five are explicitly zero. Published metadata contains identities, hashes, actual ranks and verification counts, not the reproducible arrays.

## 7. Source and execution status

The [driver](../notes/2026-11-16-r150-critical-weak-quadratic-positive-jets-789f.py) has SHA256

$$
\texttt{f211696b5cb789f054e259648a54be7a60f2d8c7c7772d410143bc0025025b1b}.
$$

The [pinned interface](../notes/2026-11-16-r150-critical-weak-quadratic-positive-jets-interface-789f.json) gives all four helper identities and three independent commands. The default budget is $300$ seconds and $2$ GiB per field. A resumable budget checkpoint exits with code $75$, not completed status.

These new three field probes had not been executed when this construction was frozen. No new numerical gain is claimed in this appendix.
