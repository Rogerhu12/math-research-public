# R133 补充：已知完整响应的真实腰部与正帽切口源

**状态：已证明（完整已知边界源；未知高频反馈与全逆继续保留）。**

公开 Actions [43599771405](https://github.com/Rogerhu12/math-research-public/actions/runs/43599771405)
实际完成全部10项检查，子过程退出码0，墙钟5.000472532秒，数学原件自记1.2798199119999936秒。
本次完整消费原193态立方、实际mean流、真cap低97/mean/high证书和weighted两端；
没有重建trial、重算mean或重算cap矩阵格。

## 1. 同一已知响应与实际单侧迹

原响应索引为
`ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6`。
原完整body/mean的全部7721格与6143跳均保留。
已知准解为$q_*=q_{\rm raw}+e_z e_2$，
其中even mean独立保留，非mean物理振幅除以$\sqrt2$进入正交槽。

实际腰取$0+$的原piece 0、mean row 0。
切口准确为$L=9/10$，取内段左迹，原response piece 5484、完整mean row 6375。
它没有用binary64的0.9代替有理切口，也没有把邻接右侧trial迹混入内段源。
全部193个槽、96腰源槽和97名义切口源槽均在完整native中保存。

参数源的真实紧支撑为$[1/20,9/50]$。
因此在$[9/10,25/8]$上真实参数响应满足homogeneous cap方程；
只控制内段响应误差时，可以在$9/10$截断已知trial。
完整真cap及未知高输入仍保留，不必把旧外帽trial残差再传播回来。

## 2. 实际完整边界源

以下均是对原生有向上界向外放宽的十进制界。
角测度归一化，even块含完整mean。

| 实际量 | 严格上界 |
|---|---:|
| 全部96腰行源$\|g_0\|$ | $8.922944\cdot10^{-16}$ |
| 切口完整97维even输入$\|v\|$ | $0.411797354580$ |
| 名义96个odd行残差 | $2.533914\cdot10^{-10}$ |
| 名义独立mean行残差 | $6.540809\cdot10^{-9}$ |
| 名义完整97行残差 | $6.545716\cdot10^{-9}$ |
| 真96个odd行源 | $0.000194841582807$ |
| 真独立mean行源 | $0.0000603566806700$ |
| 真完整97行源$\|g_R\|$ | $0.000203975908607$ |
| 原完整高输出规范下的独立已知源 | $0.000195001650779$ |

[完整边界源合同](../notes/2026-11-14-R133-known-response-boundary-source-contract.md)
给出准确公式。写$v$为even97槽、$o$为odd96槽，
$$
g_0=-q_{*,\rm odd}(0+),\qquad
g_{R,\rm nom}=-\binom{o+Jv}{Mv}.
$$
消费者同时计算
$$
\|(o+Jv,Mv)\|+\varepsilon_{97}\|v\|
$$
和
$$
\sqrt{(\|o+Jv\|+\varepsilon_{\rm odd}\|v\|)^2+
       (|Mv|+\varepsilon_{\rm mean}\|v\|)^2},
$$
并取两种已证上界中的较小者。当前较小者是保独立mean的第二种。

径向权为$R=\operatorname{diag}(I_{96},\rho I_{97})$。
因为$B_R=B_{\rm true}R^{-1}$，
$$
B_R(Rq_*)=B_{\rm true}q_*,
$$
表中源直接配已证$L_R,D_L$，没有另乘$\rho$或$\rho^{-1}$。
腰源同理直接配$L_0$。
原虚腰接口$0+\to0-$仍必须先进入完整Green跳链。

独立高源是原完整cap合同
$\|(I-\Pi_{96})S(HB_{\rm even}-K_{\rm actual}HC)v\|$
的完整已知输入上界；它不是未知高输入的反馈常数。
其范数规范不能无代价换成另一个未经证明的物理高迹规范。

## 3. 不可替换的原生证据

| 对象 | SHA256 |
|---|---|
| 123项manifest（原117项逐字不变） | baebd3764b9a1f013f1b6cf89df5864e2fbe850ceb99510a8efe0460b0aa6f85 |
| 数学producer | 79796ab53f20088da1ef11261be81e2ce548c16772c991eb9d5e8148b2b23204 |
| 原cap-cut native | 36f498e3b0addbb46290c12fae6b63af7673db20ba230e22dd83809d18427104 |
| 原weighted两端native | 56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25 |
| 新完整native | b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263 |
| 实际过程 | 6ff7f39ab70150f99eebb8a880fb0f52867574b25e122b59d95c1a0105e2609e |
| 完整UTF-8摘要 | 4990ad13c3ae68c2a9653fc04318e52d894b9e3a04df10a5516b107c10e48950 |

[原执行过程](../notes/known_response_boundary_ci/run-43599771405-1-known-waist-and-true-cap-sources/process.json)
与[原完整摘要](../notes/known_response_boundary_ci/run-43599771405-1-known-waist-and-true-cap-sources/evidence/known-waist-and-true-cap-sources-summary.json)
保全部10门、原输入身份、单侧迹、源界、实际退出与README检查。
完整压缩native在同目录的native子目录保存，未改原字节。

## 4. 下一组成项的准确范围

本结果与[实际repair差源](R133-supplement-actual-complete-response-repair-source.md)
合在同一固定物理$\eta_0$、原$\nu$、精确连续repair中心上。
内段还须保全部原非mean trial跳、已知repair残差、完整Green，
以及真实low/high互相反馈。完成这些之前，不把任何表中源范数改称
$\|q_\nu-q_*\|$，也不授真参数Schur或非线性闭族。
