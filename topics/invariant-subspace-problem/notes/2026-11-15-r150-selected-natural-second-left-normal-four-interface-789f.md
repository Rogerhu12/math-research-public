# 同一所选第二左 jet：normal 次数 4 的完整高核及原解续接

作者：Astra-ISP-789f / normal_annihilator。  
AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。

**状态：可执行算法与条件证明，尚未执行新数学。** 本地环境不可用，主源码仅已人工通读，不声称本地 AST 或新秩。实际运行由同一 Actions 会话进行。可重算矩阵仅作该 job 临时检查点，不上传 Git、Release 或永久附件。

## 1. 只复用已成 22 头后的真实对象

前一实际入口为 `run43702348535/selected-natural-second-left-regauged`，源码提交 `2cbfa8d0680e08ea57f202a4ab7091e767485666`。它已经给出：

- $M'_0=B_0^TE_{\rm new}$ 的模 31 满列秩 1546；实际原行单位块行列式为 $5$。
- 完整原第二右端 $R=[HF,T]$，以及全部 36 个实际有理单位解 $N_j/D_j$。
- 全部 4354 原行残差 $S_j=M'_0N_j+D_jR_j$，其有理秩为 14。
- normal 次数至多 3 的精确第二头维数为 22，95,788 个原产品全为零，完整第二秩目前仅为 $[9,11]$。

原 formal 稿为
`results/R150-appendix-selected-natural-second-left-twenty-two-heads-and-rank-interval.md`。
本轮不重这 36 个单位解、不重旧 $HF,T$，不以 24 头为前提。

## 2. 1736 个原高行的严格压缩

令 $E_4$ 是同一所选输出 $I$ 中全部 1485 个 normal 次数恰为 4 的坐标，置

$$
M_4=B_0^TE_4.
$$

所有列都从同一原 17 式整数常数项和原单项式字典生成。令 $H$ 是旧校正 $M'_0$ 恒零的 1736 个原来源行。实际旧右端在这些行上全部为零；新程序重新读取原缓存逐数字核

$$
(M'_0)_H=0,\qquad R_H=0.
$$

所以扩支持方程

$$
M'_0x+M_4\eta+Rz=0,\qquad z=(t,c)\in\mathbb Q^{36},
$$

必有

$$
H_4\eta=0,\qquad H_4=(M_4)_H\in\mathbb Z^{1736\times1485}.
$$

因此只需精确求完整有理核 $Z_4$，写 $\eta=Z_4a$；随后只引入

$$
W=M_4Z_4
$$

的实际 $k=\dim_{\mathbb Q}\ker H_4$ 个方向。这个归约使用全部 1736 行。它不引用完整端点矩阵的高核，也不预填 $k=2$。

## 3. 模 31 剖面只选择真实单位块

先对完整 $H_4$ 取模 31 原列、原行单位剖面，记录秩 $r$、原列集合 $C$、自由列集合 $F$、原行集合 $P$，实际核

$$
\det H_4[P,C]\not\equiv0\pmod{31}.
$$

它只给一个真有理单位块及下界 $r$。以 $H_C,H_F$ 表示其原列，准确解

$$
H_4[P,C]X=-H_4[P,F].
$$

每列先保存完整有理分子分母，再在全部 1736 原行形成 Schur 残量。若其列为 $N_j/D_j$，则保存的整数图列在自由坐标为 $D_j$、主坐标为 $N_j$，全原残量是

$$
S^{\rm high}_j=H_CN_j+D_jH_{F,j}.
$$

必须对这个完整小残量再取**有理核**。这样即使实际有理秩大于模 31 秩，也不会把有限域核冒充有理核。最终每个 $Z_4$ 整数列在全部 1736 原行乘回零，并核其自由坐标像独立。其维数与单位图、全 Schur 的核维数相等，故是完整有理核。

为明确本次预算，若初始有限域自由列数大于 64，则只保存完整原 $M_4$ 及实际单位剖面，返回 `completed-prefix/high-nullity-above-bounded-entry`，不运行超出此入口形状的求解，也不作任何负结论。若不超过 64，则本轮持续走完实际有理高核；时间不足按真实完成文件续接。

## 4. 只对真实高核追加新单位右端

若 $k>0$，新程序完整形成 $W=M_4Z_4$ 的全部 4354 行，并核 $W_H=0$。只对这 $k$ 个新右端使用**旧同一个** $1546$ 阶单位块：

$$
M'_{0,P_0}N'_j+D'_jW_{P_0,j}=0.
$$

旧原行系数公因子 $g_i$ 同时作用于矩阵和右端；原单位块、原选行和模 31 行列式都来自已付固定字节。本轮 generic worker 仅把 RHS 列数从固定 36 泛化为 $1\le k\le64$，其先保存完整解、后核全部 1546 原未缩放行的规则不变。

接着形成新的全原残差

$$
S'_j=M'_0N'_j+D'_jW_j.
$$

旧 36 个 $S_j$ 直接从原文件读取，逐一对照已付完整回执中的 SHA256，不重新乘回。对完整矩阵 $[S,S']$ 取有理核。若核向量为 $(\gamma,\xi)$，对应真实变量为

$$
x=N\gamma+N'\xi,\qquad
(t,c)=D\gamma,\qquad
a=D'\xi,\qquad
\eta=Z_4D'\xi.
$$

这里 $D,D'$ 表示各列正分母对角矩阵。不得把残差核坐标直接当作原来源变量。

每个新候选保存完整 $1546$ 个旧支持校正、$1485$ 个 normal4 校正、三个 $t$ 和 33 个 $c$。最后在**全部原 4354 个来源**核

$$
M'_0x+M_4\eta+HFt+Tc=0.
$$

原一阶来源仍由 $E_{\rm old}$ 嵌入；完整二阶来源族为

$$
\begin{aligned}
\lambda_0&=\Lambda Cc,\\
\lambda_1&=E_{\rm old}Xc+\Lambda Ft+\Lambda Cy,\\
\lambda_2&=E_{\rm new}x+E_4\eta+E_{\rm old}Xy+\Lambda e.
\end{aligned}
$$

其中 $y\in\mathbb Q^{33}$、$e\in\mathbb Q^{36}$ 全保留，不因新支持而更换旧 $X$ 的坐标含义。

## 5. 完整头维数与可宣布的结果

已付完整常数左核仅支持低坐标。新规范 $E_{\rm new}$ 对这些常核的规范评价可逆，而 $E_4$ 与之不交。因此 $[M'_0,M_4]$ 在当前规范的全部 3031 个坐标上有理单射。

若一个扩支持 reduced 解满足 $c=0$，先在完整 $\operatorname{coker}B_0^T$ 中用三个第一失败轴迫 $t=0$，再由上述单射迫 $x=\eta=0$。所以 reduced 核向 $c$ 的投影也是单射。程序仍实际对全部候选的 $33$ 行 $c$ 矩阵计算有理秩，不仅用这项结构证明。

设 $r_{\rm ext}=\operatorname{rank}_{\mathbb Q}[S,S']$，则当前支持内的精确头维数为

$$
d=36+k-r_{\rm ext},
$$

并实际有 $22\le d\le24$。新增头数为 $d-22$，也等于新 $W$ 残差像与旧 $S$ 像的交维数。只有全部原式及 $c$ 独立性完成之后才使用这个维数。

- 若 $d=24$，结合已付特征零第二秩下界 9，得到真第二连接秩恰为 9。
- 若 $d=22$ 或 $23$，只完成 normal 次数至多 4 的校正族；完整第二秩分别只被夹在 $[9,11]$ 或 $[9,10]$，normal 次数 5 仍开。
- 若真高核 $k=0$，当前扩支持不增加任何来源方向。直接继承旧 22 个已经完成的原产品，严格封 normal 次数至多 4 的头维数为 22，不为此重复旧乘回。
- 所有分支都不证明参数最高系数为 31 单位或整个特征零长度等于 243，也不证明原目标的特征零成员性。

## 6. 冻结源码和执行命令

主程序：

`notes/2026-11-15-r150-selected-natural-second-left-normal-four-789f.py`

- blob：`89bbe8c7b89aee24826f31118ebeec609f91d570`；
- 字节数：36,471；
- SHA256：`3fe9dfc2a3895f66871892079ed6042bedb6eba8ec04291c98c096df1612d9c0`。

新增单位 worker：

`notes/2026-11-15-r150-selected-left-additional-unit-solve-worker-789f.py`

- blob：`1f1aaa60dea2236c001c6439a09248244aae7fd8`；
- 字节数：16,409；
- SHA256：`28928f4298d0689f72ea8d39e530d474c4d15076af1c26aee612a2cb1413982e`。

准确 CLI：

```text
python -B {scripts}/2026-11-15-r150-selected-natural-second-left-normal-four-789f.py
  --regauged-out {work}/selected-natural-second-left-regauged
  --rebuild-root {work}/selected-natural-u-rebuilt
  --unit-worker {scripts}/2026-11-15-r150-selected-left-additional-unit-solve-worker-789f.py
  --out {work}/selected-natural-second-left-normal-four
  --seconds 300
  --memory-mib 2048
```

主回执为 `selected-natural-second-left-normal-four-receipt.json`。

只有 7 个固定主输入：旧单位输入、旧完整解、旧完整原产品回执、旧主回执、旧小残差 RREF、原常数系数、同一 $I$。其准确字节数与 SHA 在主源码的 `PINS` 中。旧 36 个残差文件的身份继承自已锁定的原完整产品回执，每次读用再逐项核哈希。

尤其旧主回执固定 20,323 B / `2343123363d6c38a871c66770afb67b37a1b3a6b882baa7aed040134914a345b`，旧完整解固定 18,124,389 B / `9c3b02d2674af645ffcfd5297cf5c9ac287fe314d0c40f49c8bb99be9396352d`。绑定保这 7 个实际输入、两个源码身份和维数/参数；临时绝对路径、运行预算不进入数学绑定。

## 7. 实际时钟、检查点和完成字段

五个连续阶段为：

1. `high-profile/`：原 $M_4$、全部 1736 高行与有限域真实单位剖面；
2. `high-kernel/`：完整返回的有理单位解、全高 Schur 和真 $Z_4$；
3. `new-images/`：全原 $M_4Z_4$ 以及实际 $k$ RHS 的单位输入；
4. `additional-unit/`：只对新 $k$ RHS 返回的完整有理解与逐原单位行产品；
5. `full-products/`：旧残差复用、新全残差、完整头及全原第二产品。

整个新数学共用 300 秒，每进程地址空间上限 2048 MiB，无编译、无新增安装、无 NumPy。各 native 返回的完整解先保存再做产品；时限到只记真实完成阶段，不声称未返回的解已成。恢复同一输出目录逐哈希复用完成阶段。

主要 outcome 及意义：

| outcome | 可宣布范围 |
|---|---|
| `same-selected-second-rank-nine-proved` | 24 真头及全原式已成，完整真第二秩为 9。 |
| `restricted-second-left-support-only` | 当前 normal≤4 完整支持已成，未封完整第二连接。 |
| `high-nullity-above-bounded-entry` | 仅有真实原高块和剖面，尚未算完整有理高核。 |
| `checkpointed-time-budget` | 真时间界，按实际检查点接续。 |
| `failed-or-incomplete` | 输入或计算未通过，不作为数学结果。 |

必须合读 `secondHeadImageDimension`、`all4354OriginalSecondLeftProductsZero`、`allHeadProjectionFreeCoordinatesIndependent`、`completeFixedSupportSecondEnvelopeComputed` 和 `selectedSecondConnectionRankExactly9`。零高核分支明确标记 `originalSecondProductsInheritedFromPaid22=true`，其已有产品不重算。

原旧步骤与其所有源码均保持冻结。新程序没有任何发布 Git/Release 或上传大数据的功能；实际主线只保小回执及源码、参数、run、哈希。

附：新增辅助单位输入明确设 `originalRightHandSideRowsUnchanged=false`，其 RHS 是新 $M_4Z_4$；旧 36 个 RHS 与完整解仍保留且不重算。辅助输入的来源说明也改为这组真实方程，避免沿用旧 36 列的审计标签。数学系数、求解和原式乘回算法不变。
