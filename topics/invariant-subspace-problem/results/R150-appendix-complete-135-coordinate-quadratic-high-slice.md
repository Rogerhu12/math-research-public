# R150 supplement: completeness of the 135-coordinate quadratic high slice

Astra-ISP-789f / literature_audit; AI-assisted with GPT-6 Astra Pro.  
2026-11-16.

This supplements the [weak quadratic positive-jet construction](R150-appendix-critical-weak-quadratic-columns-and-positive-jet-transfer.md). It changes no executable source, binding, or checkpoint. All statements are over one of its characteristic-zero critical fields $K=\mathbb Q(\alpha)$.

## 1. Precisely the slice being exhausted

Retain the original expansion

$$
F_i=q_i d^2+\sum_{l=2}^{10}(L_{il}+cC_{il}+dD_{il})n_l
       +\sum_{2\le l\le m\le10}Q_{i,lm}n_ln_m,
$$

with $\operatorname{rank}L=8$ and $\ker L=Kv$ for a fixed $v\ne0$.

Consider functionals supported exactly in the allowed set

$$
\{n_jn_l,\ cn_jn_l,\ dn_jn_l:2\le j\le l\le10\}.
$$

It has $3\cdot45=135$ coordinates. Write their values as symmetric $9\times9$ matrices $T_0,T_c,T_d$. All other target values are zero. Require vanishing on every original source except the $51$ rows $F_i,cF_i,dF_i$.

## 2. Complete source equations on this slice

For $n_jF_i$, $cn_jF_i$, and $dn_jF_i$, the conditions are exactly

$$
LT_0+CT_c+DT_d=0,\qquad LT_c=0,\qquad LT_d=0. \tag{2.1}
$$

These matrix equations use column $j$ for the source $n_j$. There is no additional factor on a diagonal coordinate: the coefficient of $n_j^2$ in $n_jL_{ij}n_j$ is $L_{ij}$.

Every remaining source is accounted for as follows.

* A one-normal source of tangent degree two cannot reach tangent degree at most one in this slice.
* A source with at least two normal factors can only reach normal degree two through $q_i d^2$, giving tangent degree at least two, outside the slice.
* The linear and quadratic terms of such a source have normal degree at least three.
* A pure source multiplier of tangent degree two or three can only reach this slice through the quadratic-normal term, and its tangent degree is too large.

Thus (2.1) is both necessary and sufficient for all $6137$ source rows outside the prescribed low $51$ rows to vanish. No original row is omitted.

## 3. Exhaustive parametrization by the small pencil

Since $\ker L=Kv$, each column of $T_c$ and $T_d$ is a multiple of $v$. Symmetry therefore gives unique scalars

$$
T_c=a\,vv^T,\qquad T_d=b\,vv^T. \tag{3.1}
$$

Put $u=aCv+bDv$. The first equation in (2.1) becomes

$$
LT_0=-u v^T. \tag{3.2}
$$

Choose $j$ with $v_j\ne0$ and put $w_0=T_0[:,j]/v_j$. Then $Lw_0=-u$. Every column of $T_0-w_0v^T$ lies in $\ker L$, so

$$
T_0=w_0v^T+vz^T
$$

for some $z$. Symmetry implies

$$
(w_0-z)v^T=v(w_0-z)^T,
$$

hence $w_0-z\in Kv$. Taking $w=(w_0+z)/2$ gives

$$
T_0=wv^T+vw^T,\qquad Lw+aCv+bDv=0. \tag{3.3}
$$

Conversely (3.1) and (3.3) satisfy all of (2.1). This proves an exact linear isomorphism

$$
\boxed{
\ker[L,\ Cv,\ Dv]\ \cong\
\{\hbox{all legal high columns in the stated 135-coordinate slice}\}.
} \tag{3.4}
$$

Injectivity follows directly: $T_c=T_d=0$ implies $a=b=0$; choosing $j$ with $v_j\ne0$, the diagonal equation $T_0(j,j)=2v_jw_j=0$ first gives $w_j=0$, and the mixed entries then give every $w_l=0$. Characteristic zero is used to divide by two.

In ordinary-monomial coordinates the diagonal values are consequently

$$
Z(n_j^2)=2v_jw_j,\qquad
Z(cn_j^2)=a v_j^2,\qquad
Z(dn_j^2)=b v_j^2.
$$

The factor two in the first expression belongs to the parametrization, not to an extra normalization of the source coefficient.

## 4. Exact low return and the remaining boundary

The only surviving source values are

$$
\begin{aligned}
Z(F_i)&=\sum_{j\le l}Q_{i,jl}(v_jw_l+w_jv_l),\\
Z(cF_i)&=a\sum_{j\le l}Q_{i,jl}v_jv_l,\\
Z(dF_i)&=b\sum_{j\le l}Q_{i,jl}v_jv_l .
\end{aligned}
$$

Here $Q_{i,jl}$ denotes the actual ordinary coefficient of $n_jn_l$ in the original equation. The physical coefficient reconstruction and the complete original multiply-back in the frozen consumer verify these formulas independently.

Consequently the consumer's small pencil exhausts this high slice; it is not merely a selection of sample high columns. Its positive length conclusion remains the one in the main construction. If a computation gives zero gain, it excludes improvement using this entire high slice together with that consumer's specified low correction block and fixed lower jets.

It still says nothing negative about higher tangent degree, normal degree three through five, or any larger complete correction system. In particular, the small rank is not a lower bound for a full original higher connection.

## 5. Actual complete computations for all three fields

The frozen consumer has now completed all three independent tasks in run **43756208221**, using exactly source SHA256 `f211696b5cb789f054e259648a54be7a60f2d8c7c7772d410143bc0025025b1b` and the four pinned original helpers. Every task exited zero. The full source/target counts are 6188 and 4367.

| Field | Mathematical seconds | Pencil dimension | Combined shape / rank | Leading rank before / after four exact pure columns | Additional length proved |
|---|---:|---:|---|---|---:|
| $F_+$ | 8.92243722999774 | 2 | $51\times49$ / 29 | 9 / 13 | 0 |
| $F_-$ | 9.712567801998375 | 2 | $51\times49$ / 29 | 9 / 13 | 0 |
| $E_8$ | 31.30352311599927 | 2 | $51\times49$ / 29 | 9 / 13 | 0 |

The original low constant rank is 25, its head count is 11, and its actual exit rank is two at order three for the cubics and order two for $E_8$. Each combined system has kernel dimension 20. The verified original jet products comprise 321776 coordinates for each cubic and 241332 for $E_8$; every one vanishes. All 12376 products for the two high columns are also checked independently against the complete original sources.

Consequently this entire 135-coordinate high slice, when paired with the consumer's stated low correction block and fixed earlier jets, gives **no improvement** over the already paid full local lower lengths $6,6,4$. This is not a proof that the actual full local lengths equal those lower bounds. Their upper bounds remain $8,8,5$. The global affine degree interval remains $278\le\deg\Delta_A\le299$, and the outside remaining multiplier still has degree at most 21. Neither characteristic-zero target membership nor $\mu=1$ follows.

All nine ordinary-square readouts vanish in the 13 selected cochains at every computed order. These are readouts of this particular surviving family, not a test against the full original dual connection; they do not prove target membership.

### Actual receipts and temporary checkpoint identities

- **plus:** [actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-plus-weak-quadratic-positive-jets.json), execution commit `d767319594bb49f7d2b8b299b77ba8b45a68f4d4`; raw 14425 bytes / `c7b70b2ec6155d0d9e3e4dc706ba5c39b3cd6433383458551f695c162600557e`; binding `fc1dd340764a2c3f419f2f8fa2cb13581585be8af1a680871ddac1d7fa157593`. Complete temporary cochains: 123732 bytes / `de8faa13fd960f68f218bf757b849417b5aa40d1a15418714f0ed687b3c859ab`, payload `4baf8f819640e6efe2b0f5befef6adb43edb7153a4820d98d3253d0206591b3a`.
- **minus:** [actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-minus-weak-quadratic-positive-jets.json), execution commit `2e5cee2f23ddd2675fe5cd4fd5481a9bdf9d0e39`; raw 14429 bytes / `79ef5a020dcdbf1a113eed0940208f5bad7449a6b4467f6c886429c708776885`; binding `108c040d0df21708a57e1bdc8ba64d796ad894d066476efa56871abd2ffa976d`. Complete temporary cochains: 183475 bytes / `b392dcf660315a55f795daaecbd044f2ce4650eadec44a705ff0d72e086c6c99`, payload `838cd8b285fa7d53a025ba70f8c52c18e0208656a16f16dc1400dbf828dfa0e3`.
- **e8:** [actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-e8-weak-quadratic-positive-jets.json), execution commit `296056a6426ca4a064891eb1d4eeff55caecb478`; raw 14267 bytes / `dc8f194bbc11634cf60b3b40968ff3123d2cd60f61a87a752e7925e8744c90f7`; binding `6b2bd281d07a3796c302c5ca8a09d00f22433fb9501c62ff0df682733d8ce7f5`. Complete temporary cochains: 540181 bytes / `a52ca48046b6babb2e14af82b7f9c486b61946f8bbbe38f273e0da2d8f8d1ad8`, payload `5ef1f6dd42337f2138e290e6049c9828d92c2b08a7708c6cfd4c5fdc5c6e8c2c`.

No large coefficient arrays were committed or uploaded. The existing temporary low series and exact field checkpoints remain available for the next genuine higher-tangent or higher-normal correction. Repeating the same pencil cannot close the missing connection; the next attempt must enlarge a stated original correction space.
