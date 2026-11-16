# R150 supplement: complete pure cubic-normal extension of the critical high slice

Astra-ISP-789f / literature_audit; AI-assisted with GPT-6 Astra Pro.  
2026-11-16.

## 1. Original equations and the precise slice

Work over a critical field $K=\mathbb Q(\alpha)$ for $F_+$, $F_-$ or $E_8$, in the original local parameter $t=s-\alpha$. Use the original moment coordinates $c,d,n_2,\ldots,n_{10}$ and all seventeen equations with every multiplier of degree at most three.

At $t=0$ the actual equations are

$$
F_i=q_i d^2+\sum_{j=2}^{10}(L_{ij}+cC_{ij}+dD_{ij})n_j
       +\sum_{2\le j\le l\le10}Q_{i,jl}n_jn_l. \tag{1.1}
$$

The coefficient $Q_{i,jl}$ is the ordinary monomial coefficient, including the actual coefficient when $j\ne l$. The original physical normalization, including $q_i$ and its nonzero $g(\alpha)$ factor, is retained. The paid original matrix $L$ has rank eight and $\ker L=Kv$, with $v\ne0$.

Enlarge the [complete 135-coordinate slice](R150-appendix-complete-135-coordinate-quadratic-high-slice.md) by the $165$ pure cubic-normal coordinates. Thus a high functional $Z$ may be nonzero only on

$$
n_jn_l,\quad cn_jn_l,\quad dn_jn_l,\quad n_jn_ln_k,
\qquad 2\le j\le l\le k\le10, \tag{1.2}
$$

where the first three families have their usual $j\le l$ range. There are $135+165=300$ allowed values. Require $Z$ to vanish on every source except $F_i,cF_i,dF_i$, a set of $51$ rows.

No claim about the full higher-normal correction space is included in this definition.

## 2. Source equations force a single cubic tensor

Write the quadratic values as symmetric matrices $T_0,T_c,T_d$, and write the cubic values as a symmetric three-tensor $U$. For a multiplier $n_jn_l$, the only term reaching (1.2) is the constant linear-normal part of $F_i$. Therefore

$$
\sum_kL_{ik}U_{jlk}=0
\quad\text{for all }i,j,l. \tag{2.1}
$$

Since $\ker L=Kv$, the last index of $U$ lies in $Kv$. Symmetry forces all three indices into the same line, so

$$
U_{jlk}=\lambda v_jv_lv_k \tag{2.2}
$$

for one scalar $\lambda$.

The multipliers $cn_j$ and $dn_j$ give

$$
LT_c=0,\qquad LT_d=0. \tag{2.3}
$$

Symmetry then gives unique $a,b\in K$ with

$$
T_c=a vv^T,\qquad T_d=b vv^T. \tag{2.4}
$$

Define the actual quadratic evaluation column

$$
q(v,v)_i=\sum_{j\le l}Q_{i,jl}v_jv_l. \tag{2.5}
$$

The multiplier $n_j$ reads the quadratic values of the linear part and the cubic values of the quadratic part. Its complete equation is

$$
LT_0+CT_c+DT_d+\lambda q(v,v)v^T=0. \tag{2.6}
$$

Exactly as in the 135-coordinate lemma, every symmetric solution of this equation has a unique parametrization

$$
T_0=vw^T+wv^T,\qquad
Lw+aCv+bDv+\lambda q(v,v)=0. \tag{2.7}
$$

For completeness, put $u=aCv+bDv+\lambda q(v,v)$. Choose an index $j$ with $v_j\ne0$ and set $w_0=T_0[:,j]/v_j$. Then $Lw_0=-u$, and $T_0-w_0v^T$ has all columns in $Kv$. Symmetry permits replacing the resulting pair of vectors by their average, yielding (2.7). Injectivity follows from the diagonal value $2v_jw_j$ and then the mixed values. Characteristic zero permits division by two.

Consequently there is an exact linear isomorphism

$$
\boxed{
\ker[L,\ Cv,\ Dv,\ q(v,v)]
\ \cong\
\{\text{all legal high columns supported on (1.2)}\}.
} \tag{2.8}
$$

The matrix on the left has shape $17\times12$. Its rank is at least eight, so the dimension is at most four. The previously completed two-dimensional quadratic slice embeds by setting $\lambda=0$; the consumer independently checks inclusion of its two actual original columns.

## 3. Ordinary monomial convention and complete source coverage

The values supplied to the original matrix are

$$
\begin{aligned}
Z(n_jn_l)&=v_jw_l+w_jv_l,\\
Z(cn_jn_l)&=a v_jv_l,\\
Z(dn_jn_l)&=b v_jv_l,\\
Z(n_jn_ln_k)&=\lambda v_jv_lv_k.
\end{aligned} \tag{3.1}
$$

In particular, $Z(n_j^2)=2v_jw_j$, whereas $Z(n_j^3)=\lambda v_j^3$. No further factorial or multiplicity factor is inserted. For repeated indices, the source product already has its ordinary polynomial coefficient. Equation (2.5) uses those same coefficients.

The following verifies necessity and sufficiency on every source outside the low $51$ rows.

* Pure multipliers of degree two or three can reach neither the quadratic tangent degree at most one nor the pure cubic support.
* One-normal multipliers of tangent degree zero give (2.6). Tangent degree one gives (2.3). Tangent degree two is outside all the allowed values.
* Two-normal multipliers of tangent degree zero give (2.1). Tangent degree one is outside the cubic support. The pure term $q_i d^2$ always has tangent degree at least two and is outside the quadratic support.
* Three-normal multipliers give at least two tangent powers through the pure term, or normal degree at least four through the other terms. Neither reaches (1.2).

Thus all $6137$ source rows outside $F_i,cF_i,dF_i$ vanish. The new cubic tensor has no direct low return because each $F_i$ has normal degree at most two. The low return is still

$$
\begin{aligned}
Z(F_i)&=\sum_{j\le l}Q_{i,jl}(v_jw_l+w_jv_l),\\
Z(cF_i)&=a\,q(v,v)_i,\\
Z(dF_i)&=b\,q(v,v)_i.
\end{aligned} \tag{3.2}
$$

The cubic parameter can change which $(w,a,b)$ satisfy the high equations; that is its possible effect on (3.2). It is not discarded because it has no direct low value.

## 4. Reuse of the actual canonical low jets

Retain the completed original low $51\times36$ block $S(t)$, its true constant unit of size $25$, and all eleven canonical cochains $X(t)$. At each of the two cubic fields put $e=3$; at the E8 field put $e=2$. Their actual identities are

$$
[t^k]S(t)X(t)=0\quad(k<e),\qquad
R_e=[t^e]S(t)X(t). \tag{4.1}
$$

The original parent manifests, complete outer receipts and source hashes are fixed. The new consumer reads them without mutation, rebuilds and compares every original low Taylor coefficient, verifies all inherited products, and checks all $625$ entries of the original unit factorization. It does not solve a new canonical low series.

Let $q$ be the actual dimension in (2.8), let $Z$ be its full original-column basis, and let $G$ be the $51\times q$ low return. The sole new last-order equation is

$$
S_0x+Ga+R_ec=0. \tag{4.2}
$$

All three terms use the same original nonzero rational row contents. Its shape is $51\times(47+q)$, at most $51\times51$. The saved $25$-unit reduces it to a complete Schur system of shape at most $26\times26$; no row is dropped from the final multiply-back.

If the projection of the full kernel of (4.2) to $c\in K^{11}$ has actual rank $r$, choose independent image representatives and form

$$
\lambda_k=\operatorname{embed}(X_kc)\quad(k<e),\qquad
\lambda_e=\operatorname{embed}(X_ec+x)+Za. \tag{4.3}
$$

Add the four all-parameter exact functionals at $c^4,c^5,c^3d,c^4d$. The consumer checks the resulting $r+4$ original heads are independent and checks all $6188$ original source products at every order $0,\ldots,e$. Both complete high sectors, of sizes $450$ and $990$, are retained in the temporary cochain pack; sectors four and five are explicitly zero.

Only the actual quadratic-normal coefficient at $t=0$ is needed, since the new high functional occurs only at order $e$. An attempted use of an uncomputed higher quadratic Taylor coefficient is an error, not a zero substitution.

## 5. Exact conclusion and its scope

The full original local module has thirteen free left heads and two positive Smith indices. The inherited low construction gives both positive indices at least $e$. The new full heads through order $e$ give

$$
h=r-9,\qquad
\delta_{\mathrm{full},\alpha}\ge 2e+h. \tag{5.1}
$$

The consumer measures $r$ and verifies $9\le r\le11$. It checks the resulting bound against the paid full upper bound, respectively $8,8,5$, without assuming that either bound is attained.

The high pencil is complete for the 300-coordinate slice (1.2). A zero value of $h$ would nevertheless be a restricted result: it would concern that slice, the declared low36 correction block, and these inherited lower jets. It would not identify a positive rank of a full higher connection, nor rule out more general normal or tangent supports.

## 6. Frozen executable and status

The [new driver](../notes/2026-11-16-r150-critical-weak-cubic-positive-jets-789f.py) is $23975$ bytes with SHA256

$$
\texttt{634b258dec87cdba34d01a2be8f1ab61fce7f944b910b5c9438343b3b423a314}.
$$

Its [interface](../notes/2026-11-16-r150-critical-weak-cubic-positive-jets-interface-789f.json) fixes the three actual parent receipts, their immutable manifests, the original physical generator, all action and field helpers, and three independent commands. Each default task has $300$ seconds and $2$ GiB. A saved budget prefix exits $75$; completed status requires every stated original product and rank gate.

The three new cubic-slice computations had not run when this proof was frozen. No new numerical critical gain is claimed here.

## 7. Actual result over all three critical fields

All three tasks completed in run **43756208221** using the frozen source SHA256 in §6, with exit code zero and the same immutable first-round parents.

| Field | Mathematical seconds | Complete pencil rank / nullity | Final equation rank | Low leading rank | Full leading rank | Additional length |
|---|---:|---|---:|---:|---:|---:|
| $F_+$ | 1.6565226160018938 | 10 / 2 | 29 | 9 | 13 | 0 |
| $F_-$ | 1.8808102780021727 | 10 / 2 | 29 | 9 | 13 | 0 |
| $E_8$ | 3.4594687310018344 | 10 / 2 | 29 | 9 | 13 | 0 |

The previous quadratic high slice has dimension two and is explicitly included. The complete new 300-coordinate slice also has dimension two, so these two high spaces are equal. In particular the cubic parameter $\lambda$ is zero throughout the actual new kernel. The quadratic-column and low-return hashes equal their corresponding first-round hashes in every field, independently confirming the same original high columns.

The complete final system has shape $51\times49$ and rank 29, with kernel dimension 20. Reusing the actual 25-unit gives a $26\times24$ Schur block of rank four. Its leading coefficient image has rank nine; the four exact pure heads give full rank thirteen. All original 6188 products vanish at every computed order: 321776 coordinates for either cubic and 241332 for $E_8$. The two high columns contribute another 12376 original products in each field.

Thus adding the entire declared pure cubic-normal layer does not improve the local lower lengths $6,6,4$. This does not determine the complete local lengths or the full next connection. The next step must address the complete high kernel or a genuinely larger coupled correction space, with all original source constraints preserved.

### Receipt and temporary certificate identities

- **plus:** [actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-plus-weak-cubic-positive-jets.json); execution `45f9057305f468af7cabb89e288a9d15f3823966`; raw 5606 bytes / `4b4e6d3fb058f5ec5c4425acde31857bc98c9460f8069739afe6cbf7ce471b4c`; binding `e5f589a5fb26b58587ea2c662a1d91927beef3db93c16159e9ff3745fb9f0ef6`. Complete cochains: 140186 bytes / `605950fac2277a896e426ec3ac0d65564df46f08853da0dd1f7d940b7a10bce0`, payload `97c7c590805ef95733790b5077b41600d579b2e819464a43cb38b8fc3cb01b07`, temporary only.
- **minus:** [actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-minus-weak-cubic-positive-jets.json); execution `ffebf163f8d467d08fb319f7e1f5828868094ef9`; raw 5609 bytes / `6153030aefdab3bb35c2081464f6a607ed341490dbcc011e3380794d943ee712`; binding `8d9102a2c86599c0c0305bcb964dfc160932930029745f97c380d89748f9a459`. Complete cochains: 184459 bytes / `30dd160f13c835d63ee93ddbe796873eda6bc8c197bf435e2abe7d4df35058d2`, payload `475735e4b31384ad09a6436b5d1089f1e14de571b12af3c83d8cb32dd3c441f7`, temporary only.
- **e8:** [actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-e8-weak-cubic-positive-jets.json); execution `13e260d7e925b57cf14ef6a83cf2c14b096f1ba6`; raw 5447 bytes / `47f5f0d8f78afd02180d32105f33b59af481c2c5cf741a8ed411d8f29306f387`; binding `7a9ebc028a4634690aeb0c45fc9a949328706ac589a38339b31a55d86b4e9e95`. Complete cochains: 511264 bytes / `99e8f4c350924d1a3ec507feabe8ec5ff2bb6aa3ff2fc9200fd09c2d8707c411`, payload `b3049f8f31d0f09737f6eefc54c7a0d8e67c6f0cdd52adcdb48b9c1f6e13368d`, temporary only.

The independent coefficient-127 result has already lowered the global affine upper bound to 298 and the outside multiplier bound to 20. The zero gains here do not lower either bound further, and do not establish characteristic-zero target membership.
