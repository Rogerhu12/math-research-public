# 单个 J6 的隐式 43 枢轴原式分离与唯一有界 Q 候选

## 1. 当前结论与唯一新增问题

本文是独立消费器 `literature_J6_implicit43_original_separation.py` 的设计说明，不是尚未执行的研究结论。全部真实 profile 原积分与原式归约只允许在公开仓库 `Rogerhu12/math-research-public` 的 Actions 中运行。新增源不修改已冻结的 forcing、响应、纯模式或 R161 消费器。

[R160](../results/R160-general-pure-J6-identity-and-balanced-mixed-entry.md) 已严格证明

$$
(J_6)_{-4}=(K_6)_{-4},\qquad
K_6=-\frac{C_0}{64}-\frac{C_{88}}{64}
-\frac{C_{41}}{128}-\frac{C_{73}}{32}
-\frac{5C_{81}}{128}+\frac{C_{193}}{256}.
$$

这里的下标是既有原响应的全局编号。R161 的公开实际回执 `43661460271` 对唯一新差 $\Xi(J_6-K_6)$ 作了 sound 归约，留下 176 项。因此 R161 仅未决，没有证明 $J_6=K_6$，也没有证明非成员。

本次唯一目标是判断

$$
J_6\stackrel{?}{\in}
E_D:=R_{8,-2}+\operatorname{span}_{\mathbb R}\{N^3G,J,D_0\}.
$$

[R131](../results/R131-third-G-translation-separation-and-111-query-control.md)、[R136](../results/R136-acceleration-coefficient-beyond-response-and-G-orbit.md) 与 [R153](../results/R153-D0-original-separation-beyond-response-G-and-J.md) 已证明 $\dim E_D=43$。其前 42 列记为 $U=(U_1,\ldots,U_{42})$，顺序严格消费原报告：40 个 $R_{8,-2}$ 真基、$N^3G$、$J$，最后新增列为 $D_0$。本次不重证其上界或独立性，不生成旧响应。

[R151](../results/R151-general-pure-J-identity-nine-dimensional-range-and-kernel.md)、[R157](../results/R157-general-pure-D0-identity-and-34-dimensional-zero-pure-kernel.md) 已给出 $\dim\pi_{-4}(E_D)=9$，故纯零核恰为 34 维。由 [R159](../results/R159-balanced-mixed-faithfulness-after-pure-cancellation.md)，本题也等价于唯一已校正目标 $\Xi(J_6-K_6)$ 是否属于该 34 维核的忠实像。此等价不要求本次物化或重新归约 31 个旧响应纯核关系。

## 2. 旧数据提供了什么，缺了什么

R136 保存了同一固定实 profile 对、同一右锚下的 42 阶原式评价矩阵 $A$。它有理可逆，其模 $p$ 行列式为 $602105349$，其中

$$p=2147483647.$$

R153 保存了 $D_0$ 在这 42 个枢轴查询处的原值、模坐标 $\bar c_D$，以及两个完整模多项式

$$
\bar R_D=\overline{D_0-\sum_{j=1}^{42}\widetilde c_{D,j}U_j}.
$$

$\widetilde c_{D,j}\in\{0,\ldots,p-1\}$ 是模坐标的整数代表，不是宣称的有理成员系数。已有第 43 个查询为

$$
e=(\text{mode }-2,\ \operatorname{Re},\ t=1/70,\ \xi=141/70),
$$

并且

$$
\bar R_D(e)=379682857\ne0,\qquad
\det\bar A_{43}=267072587\ne0.
$$

旧报告没有保存第 43 行的 42 个旧列单独值。本次明确保持这一缺失，不补评它们。保存的完整 $\bar R_D$ 已足以对任何新查询完成下一次 Schur 消元。

R153 的 $-4$ 模多项式为零；$-2$ 模多项式次数为 68。这只是已存数据，不是本次对 $D_0$ 或旧响应的重新评价。

## 3. 隐式 43 枢轴的准确有理意义

令 $e_{42}$ 为旧 42 个查询向量，$r_z(U)$ 为任意查询 $z$ 对旧列的行向量。对任意新目标 $X$，定义真实有理线性泛函

$$
L_z(X)=e_z(X)-r_z(U)A^{-1}e_{42}(X).
$$

已有 $L_e(D_0)\ne0$。因此

$$
\Lambda_z(X)
=L_z(X)-\frac{L_z(D_0)}{L_e(D_0)}L_e(X)
\tag{1}
$$

在真实 $\mathbb Q$ 上湮灭全部 43 个比较列。这是泛函的定义；不能把输出的模数当成其有理系数。

对唯一新目标 $X=J_6$，新增评价只做以下两件：

1. 评价 $X$ 的两个完整原式，得到旧 42 枢轴处的新值，并解 $\bar A\bar c_X=\bar e_{42}(X)$。
2. 把旧 42 原根按 $\bar c_X$ 的整数代表先合并成一个原式，再评价这一个整体和的两个模式。

记所得第一残差为 $\bar R_X$。检查它在旧 42 枢轴处全零后，计算

$$
\bar a=\frac{\bar R_X(e)}{379682857},\qquad
\bar E=\bar R_X-\bar a\bar R_D.
\tag{2}
$$

式 (2) 的第二项直接消费已存模多项式，不调用其原式评价器。新模 43 坐标是

$$
\bar c_{43}=(\bar c_X-\bar a\bar c_D,\bar a).
\tag{3}
$$

对所有旧枢轴，$\bar E$ 为零；它在新查询 $z$ 的值就是式 (1) 的模 $p$ 约化。所有参与约化的原式有理分母均由旧、新分母证书保证可逆，两个旧枢轴行列式也是模 $p$ 单位。

若存在查询 $z$ 使 $\bar E(z)\ne0$，则

$$
\det\bar A_{44}=267072587\,\bar E(z)\ne0.
\tag{4}
$$

这严格证明 $X\notin E_D$。结论也排除实系数成员：假如存在实系数关系，可逆的有理 43 枢轴已经迫使其唯一坐标为有理数；其分母在 $p$ 处可逆，约化后必须给出式 (3)，与新非零残差矛盾。

原 43 阶矩阵无需在本次被显式填满，式 (1)–(4) 已给出完整的有理含义和非零子式证书。

## 4. 同一个 profile、同一个右锚

全部新旧行继续使用 R136/R153 已冻结的同一实 profile 对。令 $t=\xi-2$，在 $0\le t\le1$ 上

$$
f=[t(1-t)]^8,\qquad
g=f(1+2t+3t^2+5t^3),
$$

区间外零延拓。其正则性为 $C^7$；新原根所需 jet 阶数必须不超过 7，否则消费器拒绝。本次不改 profile、不重配矩、不选择另一测试对。

原代数使用

$$I(F)(\xi)=\int_3^\xi F(\eta)\,d\eta,$$

保持真实符号及同一右锚。模评价在 $\mathbb F_p[i]$ 中执行；$p\equiv3\pmod4$，故这是域，最终查询取实部或虚部。

若某个模分量是次数 $d$ 的非零多项式，最多检查同一对 profile 上的 $d+1$ 个不同点 $t=j/(d+2)$，必有非零点。实际代码先检查 $-4$，再检查 $-2$，分别检查实部、虚部；保存实际额外行。增加一个查询点不是增加 profile，也不重评旧列。

此测试对不预先满足三矩。非零原式子式直接排除该对上的成员，也排除普适桥算子身份；不能因此排除所有合法三矩圆或一般可弯性。若需要合法圆存在结论，应另明确调用 R86 的平滑及左补偿引理，而不是把本次原对自动称为合法圆。

## 5. 模残差全零时，只试一个有界有理候选

若两个完整 $\bar E$ 多项式都为零，单靠模零不能宣称成员。为给同一个 J6 问题保留正向出口，本次在原 180 秒预算内增加一个有限分支。

固定

$$B=32767,\qquad 2B^2<p.$$

逐个模坐标尝试恢复约分后的 $a/b$，满足 $|a|\le B$、$1\le b\le B$ 及 $a\equiv\bar c\,b\pmod p$。两不同候选的交叉差绝对值小于 $p$ 且被 $p$ 整除，故在此盒中唯一。算法用扩展 Euclid，并显式复核界、互素和同余；任一坐标失败即保留未决，不寻找别的目标或扩大盒。

所有 43 个坐标成功时，只构造这一条新的 $\mathbb Q$ 原差

$$
F=J_6-\sum_{j=1}^{42}c_jU_j-c_{43}D_0.
\tag{5}
$$

$D_0$ 的原根由旧已保存残差加回其原整数和恢复，并核对原 SHA；没有重新评价或编译 $D_0$。有理组合使用 `Fraction`，独立于旧仅用于模代表的整数转换助手。

只验证两个新原根：$F_{-4}$ 和 $\Xi F$。两者均 sound 归零时，R159 严格推出完整 canonical 函数 $F=0$。证明保存同一组准确有理系数、原差 SHA、两个 fresh 归约和原始 DAG；不以代表坐标解或模零代替原式证明。

如果 $F_{-4}$ 恰好是 R160 已证明的同一原差，消费那份成功证明，不重做 pure。若 $\Xi F$ 恰好是 R161 已处理的同一原根，按 SHA、主报告及 publication 绑定消费其未决回执，不重跑 R161 NF。任何新的非零 sound 余项仍仅未决，归约器不声称完备。若候选分支耗尽剩余预算，保留已经完成的模原评价，标明候选验证预算未决。

阳性分支只首先证明 $J_6\in E_D$。只有原关系中 $J,D_0$ 两项都为零时，才可把 $J_6$ 放入已证明的 lineality；不能从任意 43 列成员关系自动推出正字符的 $c_0=\lambda J_6=0$ 或 PSD 的 $b_1=0$。若关系仅用 40 个响应列，则还可明确记录 $J_6\in R_{8,-2}$。

## 6. 来源绑定与已有工作的复用

输入必须同时核 source、run、lane、字节数、SHA、gzip 的原长度/SHA、原根 SHA 与列次序。主要公开输入如下。

| 用途 | 原 run / 源 commit | 关键文件 |
|---|---|---|
| 40 响应及 $N^3G$ 原根 | `43653293263` / `2f0add61f44365d713abf836beaa8b0be2806a3d` | `G-third-translation.json` 与原式导出 |
| 五族、J6 与 $J$ 原根，旧 42 枢轴 | `43654534244` / `1177f251dc3d9455adf88b585e4c0e4bd6f7e69b` | `acceleration-layer-mixed.json`、完整报告与原式导出 |
| $D_0$ 的模坐标、完整残差及 43 子式 | `43658922081` / `a63985719537feab6649745ecb9b8736bf094ff9` | `D0-pivot-residual.json`、完整报告与原残差导出 |
| J6 的完整 pure 成功证书 | `43660884663` / `b41c6f13ffbe56543d3593acb0b9023d8320e93c` | `general-pure-J6-membership.json` 与证书 |
| 仅当原根相同才复用 R161 未决状态 | `43661460271` / `ae7e5af322c13ba8bbff6130a284272b48446568` | `J6-balanced-original-difference.json` 与 receipt |

R153 的关键完整输入为：

- 主报告：21050 B，SHA `b91b06cdb452d1d938341231c1a85de4c45dfd46bec1ca44c498413c345ae89e`。
- receipt：36978 B，SHA `6876bfe2741a083533d1a5e62c37f28c6394c94ab425041054c1fe9eab84fd00`。
- 完整报告 gzip：32740 B，SHA `5c89ab45b79e32021d6466736be2d28a83841bad665f7789150c670e55a762ed`；原 83465 B，SHA `54a1ac32eb1895c512d533b6deb30853c60f92ee2d9e87c125fd5f2ae7f482dc`。
- 原残差 gzip：71856 B，SHA `eeac6ff33f19d75c5621fec7c615d400aa6a0119fe3383073d3768986795844b`；原 294020 B，SHA `29c18008975301e472c4ddbb9e2791ff42f8e7543f4001cdc8ba1a98f62ccb50`。
- 两模式完整模系数对象 SHA：`906c75134d3946af1f843db2e1b7fac57dc123b38dcefe97bfbb9618390de2fd`。

消费器不调用旧 study/main，不归约旧 40 列或 31 核关系，不重算旧子式，不评价任何旧单列或旧额外行。解码原始 DAG、线性合并原根和读取已存模多项式不是重新生成响应。

## 7. 预算、执行及输出

默认总墙钟预算 180 秒，内存软轮询 1024 MiB，原模多项式次数上限 256、操作检查 20000000。可选 Q 候选与其两个新原差使用同一总时间和内存预算，不另开研究任务。每个新 sound 归约最多 120000 次 primitive 调用、120000 项。

最小人工命令：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_J6_implicit43_original_separation.py \
  --toy-only --output /tmp/J6-implicit43-development.json
```

唯一实际命令：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_J6_implicit43_original_separation.py \
  --output /tmp/J6-implicit43-original-separation.json
```

实际入口必须同时满足 `GITHUB_ACTIONS=true` 与指定公开仓库名。默认输入目录均指向已发布目录，不要求重建任何旧研究。

输出最多三个文件：

- `J6-implicit43-original-separation.json`：小主报告，上限 90000 B。
- `J6-implicit43-original-separation-complete-report.json.gz`：全部新坐标、完整模多项式、精确候选及归约证据，上限 2000000 B。
- `J6-implicit43-original-separation-original-residual.json.gz`：10 个模残差原根；若生成唯一 Q 候选，再增加其两个完整模式差和 balanced 原根，上限 1500000 B。

总输出上限 3590000 B。附加导出达到上限时明确记录未导出，不因附加文件大小抹掉已经完成的数学状态。资源或接口异常保留 phase、错误、已完成 checkpoint 及来源；主报告不会因为完整数组太大而要求通过 API 读取大文件。

## 8. 新人工检查与待执行边界

仅人工执行覆盖：两次 Schur 的小矩阵直接对照、旧行列式乘新残差、整数 lifts 与有理坐标区别、零旧枢轴拒绝、完整模多项式恢复及 SHA 篡改拒绝、旧额外点消去、新点寻找、模零保持未决、有界有理恢复及非法盒拒绝、分数不被整数截断，以及一对小型纯/平衡原差的正向 sound 证明和非零余项未决。

这些检查不读取公开研究输入，不评价真实 profile，不编译研究目标。当前源只准备了此单 J6 的实际入口；任何新 44 子式、完整成员关系、维数变化或正性零化，都必须等待公开实际回执。
