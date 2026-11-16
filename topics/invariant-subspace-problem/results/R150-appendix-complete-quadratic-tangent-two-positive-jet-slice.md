# R150 supplement: the complete quadratic tangent-degree-two slice

Astra-ISP-789f / literature_audit; AI-assisted with GPT-6 Astra Pro.  
2026-11-16.

The [previous 135-coordinate lemma](R150-appendix-complete-135-coordinate-quadratic-high-slice.md) fixes the original coefficient conventions. This supplement enlarges only that declared correction support. It does not assume that all full corrections have normal degree at most two.

## 1. Exhaustive high equations on the declared support

Over a critical field $K=\mathbb Q(\alpha)$, retain the original expansion

$$
F_i=q_i d^2+(L_i+cC_i+dD_i)n+Q_i(n,n),
$$

where $q\ne0$, $\operatorname{rank}L=8$, and $\ker L=Kv$.

A two-normal functional of tangent degree at most two has six symmetric matrices

$$
T_0,\ T_c,\ T_d,\ T_{cc},\ T_{cd},\ T_{dd}.
$$

The $45$ original two-normal sources, for any equation with $q_i\ne0$, force $T_{dd}=0$. No division by a vanishing parameter is involved. The one-normal sources, with tangent degree at most two, then give exactly

$$
\begin{aligned}
LT_{cc}&=0,&LT_{cd}&=0,\\
LT_c+CT_{cc}+DT_{cd}&=0,&LT_d+CT_{cd}&=0,\\
LT_0+CT_c+DT_d&=0. &&
\end{aligned} \tag{1.1}
$$

Thus symmetry forces

$$
T_{cc}=a vv^T,\qquad T_{cd}=b vv^T.
$$

The same symmetric-matrix argument as in the 135-coordinate lemma gives uniquely

$$
T_c=vw_c^T+w_cv^T,\qquad
T_d=vw_d^T+w_dv^T,
$$

where

$$
Lw_c+aCv+bDv=0,\qquad Lw_d+bCv=0. \tag{1.2}
$$

The combined system (1.2) has shape $34\times20$ and rank at least $16$, so its kernel has dimension at most four. It has at least the two independent choices $(w_c,w_d)=(v,0),(0,v)$ with $a=b=0$.

For each actual basis vector of this kernel, the only remaining condition is

$$
LT_0=-(CT_c+DT_d),\qquad T_0=T_0^T. \tag{1.3}
$$

The symmetric matrix $T_0$ has $45$ ordinary-monomial values. Equation (1.3) has $153=17\cdot9$ scalar rows and at most $45+4$ columns. Its homogeneous kernel with the top parameters zero is exactly $Kvv^T$. The complete legal slice therefore has dimension at most five.

The consumer solves both complete systems and checks every original source. Ordinary diagonal conventions are retained: $(vw^T+wv^T)_{jj}=2v_jw_j$, while $(avv^T)_{jj}=av_j^2$.

## 2. All source rows and the low return

A pure source can read these two-normal values only through its quadratic-normal term. It therefore returns only on pure multipliers of tangent degree at most two, precisely $17\cdot6=102$ source rows.

One-normal sources are exhausted by (1.1). Two-normal sources are exhausted by $qT_{dd}=0$; their tangent-degree-one multiples cannot reach the declared support. Three-normal sources have larger normal degree. Thus all other $6188-102=6086$ original rows vanish.

Conversely these equations were obtained from actual original source rows, so the construction exhausts the stated $270$-coordinate slice. Its $d^2$ block is forced to zero, leaving the five displayed symmetric blocks. No assertion is made about tangent degree three or normal degree three through five.

## 3. Enlarging the low block without repeating canonical lifting

Use the $102\times59$ original low block with target columns

$$
\{c^ad^b:1\le a+b\le4\}
\quad\cup\quad
\{c^ad^b n_j:a+b\le2,\ b\le1,\ 2\le j\le10\}.
$$

There are $14+45=59$ columns. Every original source outside the low $102$ rows kills this block identically in the parameter:

* a pure multiplier of degree three cannot reach the declared target degrees;
* a one-normal source would have to use the pure term $qd^2$, but the allowed one-normal targets have $d$-degree at most one;
* larger source normal degrees cannot occur.

The old $36$ low columns are retained. The new columns are five pure degree-four monomials and eighteen $c^2n_j,cdn_j$ columns. Two new pure columns, $c^4,c^3d$, are exact. Consequently the already completed eleven canonical chains, together with these two exact columns, give thirteen low heads. The two remaining exact pure degree-five columns, $c^5,c^4d$, are added at the end.

The full constant rank $4352$ and the complete fifteen original constant heads imply that this enlarged low block has constant rank $59-13=46$. The new consumer checks this value explicitly. It does not assume the new equation's head rank.

The original $25\times25$ unit and its actual LU factors are read from the completed parent. All old Taylor coefficients are compared with the parent identity after exact row transport. The enlarged constant and final equations use that same unit, followed by the full remaining-row Schur complement. No new canonical series is solved, and no parent checkpoint is modified.

## 4. Positive jet transfer and its boundary

Let $Z$ be the actual complete high slice, of dimension $q\le5$, and $G$ its low return. Let $X(t)$ be the inherited thirteen-chain family, including the two new exact pure heads. At the original exit order $e=3$ for either cubic field or $e=2$ for E8, compute its complete original residual $R_e$.

The last correction equation is

$$
S_0x+Ga+R_ec=0, \tag{4.1}
$$

of shape $102\times(72+q)$. Eliminating the paid unit leaves all $77$ other rows and at most $52$ columns. The complete kernel is projected to the thirteen $c$ coordinates. If this image has actual rank $r$, adding the two exact pure degree-five heads gives $r+2$ full original heads.

Every resulting cochain is substituted into all $6188$ original rows at every order $0,\ldots,e$. The constant head rank is checked independently. Since the generic left free rank is thirteen, the valid positive conclusion is

$$
\boxed{\delta_{\mathrm{full},\alpha}\ge2e+(r-11).} \tag{4.2}
$$

The code checks $11\le r\le13$ and the paid full upper bound. A zero gain exhausts the declared high slice only in combination with the declared low block and inherited lower chains. It remains no negative statement about the full higher connection.

## 5. Frozen continuation

The [new driver](../notes/2026-11-16-r150-critical-quadratic-tangent-two-positive-jets-789f.py) has SHA256

$$
\texttt{ae0b291dbcd88509044c2d4933782aa73d9717de73e476f9bb62b864f4aceaac}.
$$

The [interface](../notes/2026-11-16-r150-critical-quadratic-tangent-two-interface-789f.json) pins each completed parent outer receipt, its raw receipt identity, its manifest, and all five source dependencies. Parent bindings differ by field and are not relabeled.

The three new computations are not reported as completed here. Immutable child checkpoints retain full mathematical arrays temporarily; a budget stop exits with code $75$. Only actual complete original products and independent heads authorize a new positive length bound.

## 6. Actual exhaustive result: the enlarged high slice equals the previous slice

All three tasks have now completed in run **43756208221** with exit code zero. They used exactly driver SHA256 `ae0b291dbcd88509044c2d4933782aa73d9717de73e476f9bb62b864f4aceaac`, the frozen helper pins, and each field's actual immutable parent.

| Field | Mathematical seconds | Top pencil rank / nullity | Symmetric compatibility shape / rank | Complete high dimension | Combined rank | Full leading rank | New length |
|---|---:|---|---|---:|---:|---:|---:|
| $F_+$ | 19.256911595999554 | 18 / 2 | $153\times47$ / 45 | 2 | 50 | 13 | 0 |
| $F_-$ | 23.841089172001375 | 18 / 2 | $153\times47$ / 45 | 2 | 50 | 13 | 0 |
| $E_8$ | 132.4904519189986 | 18 / 2 | $153\times47$ / 45 | 2 | 50 | 13 | 0 |

The old 135-coordinate high slice has dimension two. The new program checks its inclusion in the complete tangent-degree-two high slice and checks that the latter also has dimension two. Therefore the two high correction spaces are **equal**, not merely equal in a projected rank. This equality concerns the stated high slices; the larger low block is retained separately.

The expanded low constant block has shape $102\times59$ and actual rank 46. Its same-parent 25-unit Schur block has shape $77\times34$ and rank 21. The complete final equation has shape $102\times74$ and rank 50; its Schur block has shape $77\times49$ and rank 25. Its kernel has dimension 24, but its projection to the thirteen leading-chain coefficients has rank only 11. Adding the two exact pure degree-five heads gives the complete verified leading rank 13.

Every original cochain product is checked: 321776 coordinates for each cubic and 241332 for $E_8$, plus 12376 original products for the two high columns in each field. Every old Taylor coefficient and all inherited earlier-chain equations match the immutable parent. There is no new canonical lifting hidden in this comparison.

Thus the complete tangent-degree-two slice, paired with the specified larger low block and inherited lower jets, still proves only the paid full local lower lengths $6,6,4$. The upper bounds remain $8,8,5$. This result does not exclude a correction with normal degree three through five, tangent degree three, or different complete lower jets. It does not change the current global degree or characteristic-zero target membership bounds.

### Actual receipt and temporary certificate identities

- **plus:** [actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-plus-quadratic-tangent-two-positive-jets.json); execution `d911b71c93dd43ea63c6faa66d29e43df2205c0d`; raw 6265 bytes / `7bd8cf63125751bcdbf95e07f7663af34874ccfa793328df283da523a262e352`; binding `60f622f497289f0c64d0133c769012de6816b100c336813f2492b1bc00960f24`. Complete temporary cochains: 123661 bytes / `4202e2a389d59041f61299ae5e08e5cef79928429001185d6f7dd09cc67a9661`, payload `2a6dbb8213ad69a8a5b05b63afe035ab35ec88be27ed562b4c8fa57d7ee243ea`.
- **minus:** [actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-minus-quadratic-tangent-two-positive-jets.json); execution `9ddddb3d6d1ddd2d97bbd435993493f3dad4bffb`; raw 6269 bytes / `e695f0593b8d8376af7485bc55ded5a794a73adbcec4fce32ea83c2623463111`; binding `6b040e74a47d880e49b95cc3694a470938c9818b3a1d8ba8037ecc59b98b2cc7`. Complete temporary cochains: 183011 bytes / `1cba73e2dfb8162e272a39979a173c7165fbebe504f9adc1042c0c6525b11cae`, payload `f5d840dc7719638d6d277d5ae9d648b9f505197a8e9676eb09386e572f5fb694`.
- **e8:** [actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-e8-quadratic-tangent-two-positive-jets.json); execution `058b83f9b5a7451a5fe99165299c6ae8e3b686ed`; raw 6108 bytes / `be2cf4f70842db5b74272718b5c74ed868b06af3def2e810722f730636aed58b`; binding `c1a4842b0a7da51fb7a11d831a3594598c67bab365a01f3a4de9ccc4ce7f8edd`. Complete temporary cochains: 538197 bytes / `e6863bce8997b0c645632f00071961f7fc13ba310f8856e443d649fdd8ea8167`, payload `6bc50deda52b2d92ebca8f45854fa6db8a273c77f66dc700b546e66a1577bcd3`.

All large arrays remain temporary. The next declared candidate adds an actual normal-degree-three constant tensor; the present equality is not used to omit its original high-source constraints.
