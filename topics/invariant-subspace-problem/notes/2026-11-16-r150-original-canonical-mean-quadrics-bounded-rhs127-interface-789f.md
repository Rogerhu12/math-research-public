# 四个字面规范均值二次式的原权八右端接口

作者：OpenAI ChatGPT（literature_audit）；日期：2026-11-16。

## 1. 本次输入与范围

这是独立源码、独立 format、独立 binding 和独立输出目录。它读取已经完整结束的原 $17674\times1386$ 权八矩阵及其秩 $1312$ 单位行状态，只新增四个右端。父权七状态只用于完整源标签与三十个 $N_iY_j$ 来源的身份核验；本次不对权七矩阵再作右端降约。

全部输入身份见
[输入清单](2026-11-16-r150-original-canonical-mean-quadrics-bounded-rhs127-inputs-789f.json)。
所有矩阵、字典、状态和来源数组均留 TMP；发布仅含源、参数、run、SHA 与正式结论。

系数域严格是合法原剩余点 $\mathbf F_{127}$、$d=100$。本次正证也只给该域的原来源；不把它当作 $E$ 或 $\mathbf Q$ 的来源。七个已完成的 $\delta$ 余式不决定这四个新右端的结果。

## 2. 四个 q 的字面身份

[原规范 pencil](../results/R150-appendix-original-rank-three-mean-incidence-and-complete-sextic-pencil.md) §2 与
[十九图覆盖](../results/R150-appendix-original-mean-quadrics-dual-normalization-and-complete-bell-cover.md) 使用
$$
T'_j=\sum_{i=0}^3T_iV_{ij},\quad
U_{aj}=(T_j)_{0a}\ (0\le a,j\le3),\quad V=U^{-1},
\qquad q_j(y)=y^TT'_jy.
$$
原模型保存的是 $T_i$；它们不是未经变换即可称作十九图规范基的 $T'_i$。

新程序逐项执行以下门：

1. 原六个 mean 列与全部 $24$ 个 quad 轴的字面系数相等，四个原矩阵全部 $144$ 项对称且为规范域元素。
2. 在 $21$ 个上三角原坐标中按原精确 pencil 的同一规则选首个独立四行，并硬核它们确为 $(0,0),(0,1),(0,2),(0,3)$。
3. 原 $4\times4$ 常数 $U$ 可逆；全部 $UV=VU=I$ 的 $32$ 个坐标通过。
4. 对全部 $21\times4$ 原坐标核 $A'=AV$ 和 $A'U=A$，共 $168$ 个正反坐标；规范四行严格为 $I_4$。
5. 原四个 $y^TT_iy$ 与四个规范 $q_j$ 的八个多项式正反恒等式全部通过。采用 ordinary monomial：对角系数不额外乘二，非对角的两个矩阵项都保留；没有二分之一约定。
6. 原精确 pencil 小源码按完整 SHA 绑定；匹配同一系数三次式和合法 $(127,100)$ 嵌入。这里不执行旧精确 pencil 的大计算。

$U,V,T_i,T'_i,q_i$ 的完整新归一化阶段保存到 TMP，并有物理与逻辑双 SHA。它不包含新的参数求逆；$U$ 只由已付固定常数构成。

## 3. 四个完整右端

令 $b=\sum_i y_iw_i$。实际四个右端严格是
$$
q_jb^2e_0\in F_8,\qquad j=0,1,2,3.
$$
每个都展开到原 $17674$ 输出字典，保全部十二个参数和 ordinary monomial。程序沿用冻结的只读 native：
[完成状态原来源读取器](2026-11-16-r150-original-completed-row-rhs127-789f.cpp)。

该 native 的所有数学字节不改。它读取已完成的 $1312$ 个单位行和全部 $1386$ 原来源，输出四列完整原来源系数及四个完整余式。必须核：

- 原状态、字典、输入、完成结果的全部 SHA、binding、EOF、canonical 域系数、padding；
- 父状态确已处理全部 $1386$ 行，实际秩 $1312$；
- 所有已选主元位置余式为零；
- 对全部 $4\cdot17674=70696$ 个原坐标用字面原输入乘回 $T=Xc+R$；
- 运行后四个父原文件 SHA 不变。

没有新 Gaussian 消元，也没有采用部分完成的行状态。原权七父的全部身份检查仍保留，因为权八来源中有三十个原 first-frontier 列；它不增加右端计算。

## 4. 零余式的完整原正门

只有某列余式完全为零，才按全部 $1386$ 原标签恢复来源：

1. 对每个实际使用的原列，重新核完整十坐标向量与其原十八列来源；
2. 对组合核全部十坐标等于 $q_jb^2e_0$；
3. 核原十八生成元乘回，Bell 系数严格为零；
4. 用原 Jacobian 运输到物理十七梯度，并再核原十七乘回；
5. 核这些原十八、原十七来源的总权均至多 $8$；
6. 最后只改变 Bell 来源系数，使用
$$
q_j=q_jb^2-(b+1)q_j(b-1).
$$
再核完整原十八及原十七加 Bell 的多项式乘积，并核粘合后来源权至多 $8$。

该步骤给出相应规范 $q_j$ 图的真实域来源；它不需要四列同时成功。任何中途预算暂停都不能提前标记该列已通过完整正门。

## 5. 有界 Bell 来源判准

令 $\mathcal G=B\langle Y,C,V,W\rangle$ 为已付首轮齐次梯度子模，其最小权为 $5$，本次原矩阵给出完整 $\mathcal G_8$。来源权至多 $8$ 指每个梯度项的总权至多 $8$，而 Bell 系数 $H$ 满足 $\operatorname{wt}(H)+3\le8$。

对任一权 $2$ 的 $q e_0$，
$$
q e_0\text{ 有这种 Bell 来源权至多 }8
\quad\Longleftrightarrow\quad q b^2e_0\in\mathcal G_8.
$$
证明：若 $qe_0=G+(b-1)H$，最低权比较给
$H_0=H_1=0$、$H_2=-qe_0$、$H_3=H_4=0$。权 $5$ 给
$H_5=G_5-bqe_0$；权 $8$ 给
$$
b^2qe_0=G_8+bG_5\in\mathcal G_8.
$$
反向正是 §4 的字面 Bell 恒等式。

所以非零余式可排除这个准确有限来源空间内权至多 $8$ 的表示；不能据此否定更高权来源或完整原理想。该判准也说明四个 q 检查有独立价值，并非把旧 $\delta$ 负结果换名重复。

## 6. 完成状态、精度和预算

默认实际预算 $180$ 秒、$2048$ MiB，外层 $240$ 秒。新的 AST 已核；native 完全沿用已实际编译和执行的冻结源。此接口冻结时未预填四个结果。

运行产物均在新的独立目录：

- canonical-mean-quadrics-bounded-rhs-receipt.json；
- canonical-mean-quadrics-bounded-rhs-manifest.json；
- complete-original-canonical-mean-quadrics.json.gz；
- weight8-rhs/ 下的完整 RHS input/result/native receipt；
- 完整原正证阶段（仅当实际零余式且全部原门完成）。

程序只有实际完成整段的阶段才写 manifest。预算暂停为 $75$；可复用同 binding 下已完成的新 native/result 或完整正来源阶段。不允许空续尚无完整新结果的 native，也不跨 binding 将旧 $\delta$ 余式冒作新 q 结果。失配、类型/EOF/SHA 门失败或数学乘回失败均为 $1$，不当作预算。

父数组只读，复跑也必须逐 SHA 核完整父。无需等待新的第二轮 $104$ 列来源；本次完整权八空间已冻结。

## 7. 最小 CLI 与依赖变化

输入清单的 suggestedCLI 给出完整可重现参数。相对于已实际完成的七个 $\delta$ 右端程序：

- 主源码另名，全部输出另名，format/binding 独立；
- 去掉旧 chart-source，换为 exact-pencil 小源码，用来钉同一规范化常数规则；
- 原矩阵、原输入顺序、两个父状态校验与只读 native 均不变；
- 只降约四个规范 q 的权八右端，保全部 $70696$ 原乘积；
- 只在完整正门后使用各自的 Bell 粘合。

当前原数学数组不进入 Git、Release 或新 artifacts；失败身份、真实 run 与输出 SHA 单独保存。

