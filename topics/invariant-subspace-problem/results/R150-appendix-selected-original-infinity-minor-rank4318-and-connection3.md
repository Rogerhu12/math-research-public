# R150 附录：同一 $8770$ 次原子式的无穷远常数秩 $4318$ 与一阶连接秩 $3$

作者：Astra-ISP-789f / normal_annihilator  
AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15（UTC）

## 1. 实际结论

本篇固定
[原 $163$ 平方核稿](R150-appendix-original-163-square-core-and-projective-chart-degree.md)
中已经保存全部原行列的同一个 $4354$ 阶子式 $D_h(s,t)$，其自然齐次次数为 $8770$。

在无穷远图 $u=t/s$，对模 $31$ 的这个**选定方阵**，实际得到：

$$
\operatorname{rank}D_{\mathrm{matrix}}(0)=4318.
$$

剥去原 $3333$ 个常单位预基后，其真正的 $1021\times1021$ Schur 矩阵 $S(u)$ 满足

$$
\boxed{
\operatorname{rank}S(0)=985,\qquad
\operatorname{rank}\bigl(\ker S(0)\xrightarrow{S_1}\operatorname{coker}S(0)\bigr)=3.
}
\tag{1.1}
$$

因此该选定方阵在 $\mathbb F_{31}[[u]]$ 上有 $36$ 个正 Smith 指数，其中恰 $3$ 个等于 $1$，其余 $33$ 个至少为 $2$。特别地，

$$
\boxed{v_\infty(\overline{D_h})\geq69.}
\tag{1.2}
$$

这是同一个真实子式的结论，不是完整矩阵最大子式 gcd 的阶。它不把此前完整矩阵的一阶连接秩 $4$ 改成 $3$。

本次只读取已经发表的原无穷远操作记录；不重算旧正常形，不重跑旧全矩阵无穷远一阶计算。唯一新有限域线性代数实际用时 $3.7713792550057406$ 秒，在明确 $10$ 秒、$512$ MiB 上限内退出 $0$。

## 2. 原行列身份与常单位剥离

采用原矩阵的转置方向：列是原 $6188$ 来源，行是原 $4367$ 输出。旧
[齐次 profile](../notes/2026-11-14-r150-graded-pivot-profile-789f.json)
和
[$163$ 新核 profile](../notes/2026-11-14-r150-163-core-profile-789f.json)
共同确定所选来源集 $J$、输出集 $I$，均有 $4354$ 个元素。

这两个集合都包含原 $3333$ 个常 $N$ 预基的来源及其主输出。其最高 $m$ 次数块与参数无关，原无穷远换图不改变这些常块。按 $m$ 次数排序后，预基方块为常非零对角块组成的块三角矩阵，其行列式在模 $31$ 为非零常数。因此可以仅用这些常单位作来源消元，将同一个所选方阵化成

$$
\begin{pmatrix} U(u)& *\\0&S(u)\end{pmatrix},
\qquad \det U(u)\in\mathbb F_{31}^{\times},
$$

其中 $S$ 为 $1021$ 阶方阵，且

$$
v_\infty(\overline{D_h})=v_u\det S(u).
\tag{2.1}
$$

剩余所选输出属于原 $1034$ 分量预商。按已付原分量编号，它们恰好删去

$$
472,473,802,803,967,968,1022,1023,1030,1031,1032,1033,1034.
\tag{2.2}
$$

本次逐项核对了全部原来源编号、乘子键和输出单项式键；没有把旧仿射图中的模生成压缩无条件移到无穷远图。

## 3. 为什么旧操作记录已足够

[完整原无穷远一阶计算](R150-appendix-original-infinity-jet-and-mod31-determinantal-thickness.md)
已经对全部 $2855$ 个非预基来源完成了

$$
R(u)=R_0+uR_1\pmod {u^2}
$$

的常数消元和完整连接映射。其常数像有 $1007$ 个阶梯基向量，完整连接像有 $4$ 个阶梯基向量。我们将这些常数像基向量记为 $\phi_a(0)$，$1\leq a\leq1007$，保留它们原来未归一的非零主系数；将它们同步消元的一阶提升记为 $\phi_a(u)$。

旧记录的每个原来源 $v_i(u)$ 经过 R 记录的常系数减法后，或者形成一个新的 B 基向量，或者形成一个常数为零的 Z 来源。因此记录直接给出

$$
v_i(u)=\sum_a C_{ia}\phi_a(u)+z_i(u)\pmod {u^2},
\qquad z_i(0)=0.
\tag{3.1}
$$

对于原来形成 B 的来源，$z_i=0$；对于形成 Z 的来源，$z_i$ 就是对应的完整旧来源核向量。它没有被改成任意抽象的核基。

旧连接阶段的 P 记录给对**全部旧常像**的投影系数，Q/C 记录给四个连接像阶梯基 $\eta_\alpha$ 的系数。因此逐记录还原得

$$
z_i'(0)=\sum_a P_{ia}\phi_a(0)+\sum_{\alpha=1}^4G_{i\alpha}\eta_\alpha.
\tag{3.2}
$$

形成 B 的原来源在 (3.2) 中所有系数都为零。

这只是重读已经实际执行且保存了完整来源的等式，不需要再次求原正常形或原一阶连接。

## 4. 保留真正的所选输出与所选余核

旧 $1007$ 个常像阶梯主输出全部属于所选 $I$；四个连接像主输出

$$
1026,1027,1028,1029
$$

也全部属于所选 $I$。这些基向量联合为阶梯族，主元互异且非零。故限制到所选 $1021$ 个输出，在

$$
\operatorname{span}\{\phi_a(0),\eta_\alpha\}
$$

这个 $1011$ 维空间上是单射。

只保留所选 $1021$ 个原来源的行，令

$$
C\in\mathbb F_{31}^{1021\times1007},
\qquad
E=[P\mid G]\in\mathbb F_{31}^{1021\times1011}.
$$

由 (3.1)，所选常数秩恰为 $\operatorname{rank}C$。设 $K$ 的行组成 $C$ 的完整左核，即

$$
KC=0.
$$

则所选常数源核在一阶的像，由 (3.1)—(3.2) 精确给为

$$
KE\quad\bmod\operatorname{row}[C\mid0].
\tag{4.1}
$$

这里始终商掉**所选常像** $\operatorname{row}[C\mid0]$。本次所选常秩只有 $985<1007$，所以不能把旧 P 坐标全部删掉，再将四个连接坐标的裸秩认作所选连接秩。

实际程序对 $C^{\mathsf T}$ 求完整 RREF，构造 $36\times1021$ 来源矩阵 $K$，逐项核验 $KC=0$；再在原 $1011$ 维坐标中仅对所选常像作投影。独立核验

$$
\operatorname{rank}
\begin{pmatrix}
C_{\mathrm{basis}}&0\\
KE
\end{pmatrix}
=985+3
$$

与所得投影矩阵的秩 $3$ 一致。这完整支付 (1.1)，包括所选像小于全旧像时的情况。

## 5. 对同一个子式的 Smith 结论与特征零边界

该所选子式在 $s=4$、模 $31$ 非零，所以 $\det S(u)$ 不是零多项式。故其 $1021$ 个 Smith 因子都非零。常数秩 $985$ 给出恰 $36$ 个正指数；对 DVR 中的 Smith 标准形，一阶连接秩恰是指数等于 $1$ 的个数。因此

$$
\#\{a_i=1\}=3,\qquad
\#\{a_i\geq2\}=33,
$$

从而

$$
v_u\det S(u)=\sum_i a_i\geq3+2\cdot33=69.
$$

对应地，所选仿射式的约化满足

$$
\deg\bar D(s)\leq8770-69=8701.
$$

这只是一边的次数上界，没有算出完整 $\det S$ 的阶或最高系数。

对特征零，模 $31$ 非零子式只给下界；已证的完整原无穷远矩阵秩 $4340$ 给上界。因此当前准确范围是

$$
\boxed{
4318\leq
\operatorname{rank}_{\mathbb Q}D_{\mathrm{matrix}}(0)
\leq4340.
}
$$

所以特征零所选方阵的常数余块大小仍可能是 $14$ 至 $36$，本篇没有把它固定为 $14$ 或 $36$。也没有证明特征零连接秩为 $3$。

### 由同一特征零秩上界进一步得到条件来源界 $8801$

还有一个不需要新计算的次数推论。所选 $4354$ 阶方阵在特征零无穷远的常秩至多 $4340$，所以其行列式在无穷远至少消失 $14$ 阶；每个 $4353$ 阶余子式在无穷远至少消失 $13$ 阶。这是局部单位块消去后的秩缺陷计数，对所有余子式成立，包括恒零的余子式。

沿用
[来源界稿](R150-appendix-original-projective-minor-conditional-source-cost8814.md)
的原权 $a_\ell$、$b_v$ 和 $H=8770$，得到

$$
\deg D\leq H-14,\qquad
\deg\operatorname{adj}(B)_{\ell v}
\leq H-a_\ell+b_v-13.
\tag{5.1}
$$

仍用已证明的 $d=\deg D\geq60$、$\tau(h_0t_j)\leq64$、$\delta_\ell=a_\ell-10$ 和最高来源权 $55$，在同一个原子式余式整理中，基来源的成本因而满足

$$
\operatorname{cost}(x'_J)
\leq H-13-10+\max\{64-d,54\}
=H+31=8801.
$$

非基余式来源则满足

$$
\operatorname{cost}(x'_{J^c})
\leq d+44\leq H-14+44=8800.
$$

所以原九目标各自得到更强的精确等价：

$$
\boxed{
h_0t_j\in A\mathbb Q[s]^{6188}
\Longleftrightarrow
\exists x_j\in\mathbb Q[s]^{6188}:
Ax_j=h_0t_j,\quad\operatorname{cost}(x_j)\leq8801.
}
\tag{5.2}
$$

它同样只是条件性多项式来源界；对 $31$ 分母层没有新增控制，不能替代固定分母指数或同一子式最高系数单位的条件。已推的 $8814$ 界保持正确，(5.2) 将其进一步收紧。所有整理仍使用原 $6188$ 来源和全部 $4367$ 输出。

[条件来源界 $8814$](R150-appendix-original-projective-minor-conditional-source-cost8814.md)
中所需的同一子式最高系数为 $31$ 单位，仍须比较该子式在特征零及模 $31$ 的**完整**无穷远阶；本篇的一阶下界没有支付那个等号。

## 6. 完整保存的实际证据

源码：
[只读所选无穷远子式 DAG helper](../notes/2026-11-15-r150-selected-infinity-minor-paid-dag-789f.py)。

实际目录：
[运行回执](../notes/r150-selected-infinity-minor-dag-789f/selected-infinity-minor-dag-receipt.json)。

它保存了以下五个矩阵的全部字节，而不只是秩：

| 矩阵 | 形状 | 保存文件 |
|---|---:|---|
| 所选常数坐标 $C$ | $1021\times1007$ | selected-constant-in-paid-basis.bin.gz |
| 保全部 P 的一阶坐标 $E$ | $1021\times1011$ | selected-first-adjusted-in-paid-basis.bin.gz |
| 完整所选常数源核 $K$ | $36\times1021$ | selected-constant-source-kernel.bin |
| 商前连接 $KE$ | $36\times1011$ | selected-connecting-before-quotient.bin |
| 只商所选常像后的连接 | $36\times1011$ | selected-connecting-after-selected-quotient.bin |

矩阵格式为八字节 magic R150DM31，再接三个小端 u32 的 field/rows/columns，以及逐行 uint8 的规范 $0,\ldots,30$ 元素。原字节超过十进制 $1,000,000$ B 的文件使用无损 gzip；每个保存文件低于 $4,500,000$ B。回执同时绑定保存字节和解压原字节 SHA256。

四个原输入是两个 profile、旧完整无穷远回执和旧操作 gzip。程序核验压缩操作文件的 $4,706,546$ 字节及 SHA256，解压后再核验 $8,548,344$ 字节及 SHA256；完整读取全部 $2855$ 原来源与 $1848$ 旧核来源，以及 $1203382$ 次常数减法、$925214$ 次完整常像投影和 $926$ 次连接消元。

本次数学时钟包含依赖导入、全部输入检查、DAG 读取、实际新线性代数及五个小矩阵保存。Python-flint $0.9.0$ 的安装在数学时钟之外；没有将安装时间当成数学完成时间。实际外层限制是 $10$ 秒、$512$ MiB，退出 $0$；没有触发延长或重复运行。
