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
