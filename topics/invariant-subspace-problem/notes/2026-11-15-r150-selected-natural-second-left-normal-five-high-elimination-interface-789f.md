# 同一自然第二页的 normal5 高方程压缩接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

**状态。** normal≤4 的完整计算已经结束：仍为 22 个真二阶头，原 130 个新增修正余类与旧 14 维 forcing 余空间交为零。本入口只推进 normal5 的完整高方程，尚不计算新的二阶头、原目标成员性或行列式首系数单位性。源码同字节本地 AST 和下面的独立小矩阵验证已通过；没有本地重算研究矩阵。

## 1. 已付结果与需要保留的耦合

实际 run43702348535 的 `selected-natural-second-left-normal-four-complete130` 已完成。执行源为 `df9062e41dee04d287e9e157b502a8a405d58fa5`，数学用时355.1528731239996秒。实际完整166列原残差秩为144，交维为0，22个独立头的全部95788个原来源产品为零。完整 normal≤4 支撑因此没有新增头。

保持此前两个嵌入 $E_{\rm old}$、$E_{\rm new}$、同一原自然参数和同一 $I,J$。令
$$
M_0=B_0^{\mathsf T}E_{\rm new},\qquad
M_4=B_0^{\mathsf T}E_4,\qquad
M_5=B_0^{\mathsf T}E_5.
$$
$E_4$ 含1485个原 normal4 输出坐标；$E_5$ 含1287个原 normal5 坐标。整个修正补空间的维数为
$$
1546+1485+1287=4318.
$$
旧的1736个高行对 $M_0,H_F,T$ 全部为零。加入normal5后，这些行上的**实际方程**是
$$
H_5\eta_5+H_4\eta_4=0,\qquad H_i=M_i[\mathrm{high},:].
$$
不能因先前normal≤4无新增，就把 $\eta_4$ 在新方程中设为零。

本入口完整保留 $H_4$ 的全部1485列，只消 $H_5$ 的1287列。已成的130个高核方向、其原单位解及166列残差保持原文件，供后继利用；本入口不读取重算它们的大有理解。

## 2. 原 H5 的列满性与实际检查

原常数17式都在纯切向平面 $m_0=\cdots=m_8=0$ 上为零，而且 moment 次数不超过2。来源乘子次数不超过3。因此 normal5 输出只可能由 normal3 来源乘子及二normal的二次式项产生。

源码从同一17×77原整数常系数重建 $M_5$ 的全部4354行，并实际核：

1. 所有非零行都属于原1736个高行，且其来源乘子normal次数为3；
2. 高行之外的原2618个行位并不作为新商删去：直接逐行保真零；
3. 原 $M_4$ 按已付SHA读取，全1485坐标保持原顺序。

完整已付常左核只支持normal次数≤2。故 $H_5z=0$ 推出 $B_0^{\mathsf T}E_5z=0$，再由支持不交推出 $z=0$。因此 $H_5$ 在 $\mathbb Q$ 上列满。

源码仍独立计算本次原 $1736\times1287$ 矩阵的模31秩、转置选行和实际1287阶单位子式，必须实际取得秩1287及非零行列式才继续。这同时给出同一原矩阵的有理列满证据；没有把有限域核当有理核。

## 3. 精确压缩，而非数百个新 M0 右端

原高矩阵按列排列为
$$
[H_5\mid H_4],
$$
前1287列是允许消去的normal5变量，后1485列全部受保护。

每次只选前1287列中的一个实际非零有理主元。若主元行的该系数是 $a\ne0$，另一行的系数为 $b$，先令 $g=\gcd(|a|,|b|)$，再作
$$
r_{\rm new}=(a/g)r-(b/g)r_{\rm pivot}.
$$
随后除**整条附带H4行**的整数content。这只乘非零有理标量，故严格保持 $\mathbb Q$ 核。它不被解释为各中间数组的模31单位变换。

一次pivot的所有受影响行、fill数及整数高度先在pending数组中算完。只有所有门槛及时间检查都通过，才一起提交真实行、incidence、变量集合和逆代DAG。中断或越界时，整个尚未提交pivot丢弃，原已提交系统不变。

每条逆代记录保：

- 原来源行位与原编号；
- 被消的normal5变量编号；
- 实际主元整数；
- 其余所有尚存normal5变量及全部normal4项；
- 本次确定性候选分数和预计工作量。

若1287列全部消完，留下**449行、1485列**的完整有理等价 $H_4$ Schur 系统，可能含零行。原normal5修正由逆代唯一决定。最终组合仍须对原 $H_5\eta_5+H_4\eta_4$，以及完整4354行的二阶恒等式实际乘回，才能形成新二阶结论。

本次并不展开该Schur核的约千维自由族，也不盲求其所有M0右端。下一算法依据实际Schur的规模、稀疏度及整数高度选择，只对有关forcing和真实来源继续。

## 4. 精确 CLI、预算和限额

~~~text
python -B {scripts}/2026-11-15-r150-selected-natural-second-left-normal-five-high-elimination-789f.py
 --regauged-out {work}/selected-natural-second-left-regauged
 --rebuild-root {work}/selected-natural-u-rebuilt
 --normal-four-out {work}/selected-natural-second-left-normal-four-complete130
 --out {work}/selected-natural-second-left-normal-five-high-elimination
 --seconds 60
 --memory-mib 2048
~~~

建议外层墙钟120秒，保留最终无损checkpoint写出的时间。回执区分停下数学事务时的用时、最终checkpoint用时及总用时，不把封存时间隐藏为数学成功。

固定默认门槛：

| 项目 | 值 |
|---|---:|
| 候选行 | 当前最稀疏64行，逐行所有H5候选 |
| 完整pending非零项 | ≤500000 |
| 完整pending整数高度 | ≤8192 bit |
| 单pivot预计更新工作量 | ≤150000 |
| 周期checkpoint | 每50个完整pivot或至少经过5秒 |
| 数学共享时钟 | 60秒 |
| 进程地址上限 | 2048MiB |

在候选行中只尝试按确定性评分排列的前128个候选；这不被称为全局Markowitz最优。门槛、候选数进入语义binding；时间、内存和绝对路径不进入binding。同一代码和门槛可从真实checkpoint继续。若需要改变门槛，须明确迁移旧绑定，不能偷偷接受新含义。

主回执：
`normal-five-high-elimination-receipt.json`。

源码：
`notes/2026-11-15-r150-selected-natural-second-left-normal-five-high-elimination-789f.py`，
blob `2c21a5a9ad98eb982a75dfa70d3d9b891309a578`，
20716B，
SHA256 `8c671b279161dad3dce4e0caeed3ed49f9911ac6844dba705bf040e2ebcf1a3d`。

使用现有Python-flint0.9.0，只有新H5字段选元用nmod；后面的行变换使用Python精确整数。无native编译、无安装、无NumPy。

## 5. 五个实际输入

| 键 | 相对输入路径 | 字节数 | SHA256 |
|---|---|---:|---|
| old_unit | regauged-out/prepared/second-left-m0-unit-input.json.gz | 9008513 | `c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe` |
| coefficients | rebuild-root/rebuilt-first/same-original-natural-constant-and-first-coefficients.json.gz | 20580 | `7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1` |
| profile | rebuild-root/rebuilt-inputs/same-selected-original-output-indices.json | 21066 | `044b28d717749d23a2959a02c0f8ed7570bfa19bcdff04207056f2a66d2e413d` |
| paid_m4 | normal-four-out/paid-high/complete-original-normal-four-block.json.gz | 911218 | `a359450582e0081fbabd6ff79e6e0e7083d7cd5bfdcef1d801438d00a3d5c814` |
| paid_full | normal-four-out/full-products/normal-four-full-products-receipt.json | 27679 | `4158cc3b978edeafd9c993e7f1c054d9acc419eb9a5d3f34cf8e9f2cff965c22` |

这里 `paid_m4` 是新完成130入口重新绑定后的文件，绑定为
`672a21c0de59ec537f5d19333524f92ceb71ad3621eec643b9c11cf3f3fce2d3`，
不是此前911018B或910759B的同内容包装文件。

## 6. 检查点与精确分支

临时 `prepared/` 保存完整原M5、全部 $[H_5,H_4]$ 原高行，以及实际H5字段单位profile。完整准备回执存在时，重入逐SHA复用，不重构原M5或再选元。

数学状态采用两个临时槽和一个小原子指针：

- `normal-five-high-state-slot0.json.gz`；
- `normal-five-high-state-slot1.json.gz`；
- `normal-five-high-active-checkpoint.json`。

每槽保存全部剩余行、所有附带H4项、剩余H5变量、完整逆代DAG和初始行content。先完整写非active槽并取SHA，再原子更新小指针。硬杀写入中的新槽不会使旧active槽失效。

每个已提交状态满足
$$
\#\mathrm{remaining\ H5}+\#\mathrm{pivots}=1287,\qquad
\#\mathrm{remaining\ rows}+\#\mathrm{pivots}=1736.
$$

完成压缩：

- `status=completed`；
- `outcome=complete-normal-five-high-schur`；
- `completeExactH5Elimination=true`；
- 输出 `complete-high-normal-four-schur.json.gz`；
- 保449行和1485个原normal4坐标，以及1287条真逆代记录。

资源门槛停在完整前缀：

- `status=completed-prefix`；
- `outcome=bounded-high-elimination-prefix`；
- exit75；
- 报实际已完成pivot、剩余列/行、非零项、整数高度及最后完整状态SHA。

时间或信号停为 `checkpointed-time-budget`、exit75。任何算术/输入失配为 `failed-or-incomplete`，不登记新的数学结论。

所有分支均保：
`newM0RightHandSidesSolved=0`，
`normalFiveSecondEnvelopeComputed=false`，
`allFinalOriginalSecondProductsVerified=false`，
`leadingUnitProved=false`。

## 7. 已实际通过的小验证

没有另写一份消元算法。验证器从冻结源码AST提取同一个 `while active` 事务块，对原整矩阵
$$
\begin{pmatrix}
2&1&3&1\\
1&3&0&2\\
1&1&1&1
\end{pmatrix}
$$
只消前两列，并保留后两列的非平凡耦合。真实Schur为 $(-1,1)$；从其核 $(1,1)$ 按真实DAG逆代得到 $(-2,0,1,1)$，三个原产品全零。原前三列子式为 $-1$，独立证明全部核恰一维。

第二次执行在第2个pivot的pending更新中间触发预算异常。已提交第1个pivot后的rows、active、DAG、nnz规范状态逐字节不变，未提交事务被舍弃。此为本地独占/tmp小验证，不是Actions，也未读取研究数组。

- 生成器 `notes/2026-11-15-r150-selected-natural-normal-five-high-small-validation-789f.py`：blob `e06bd546cc7b21aaf6027ed8be85007b0e4d6515`，5500B，SHA `e8b8b373f85946736ad3eb994816534955ed93bfbaf61a8065566fb6cdb65ae7`。
- 实际回执 `notes/2026-11-15-r150-selected-natural-normal-five-high-small-validation-receipt-789f.json`：blob `7e7f2f53ed60d31636911db06ac3d621b9c9c06d`，1335B，SHA `73ce0694c327bfba1d87d4f488e59dde087df20e9e06c71c1643dd0f30bc31e9`。
- 实际小验证时长为0.05462024500593543秒。

只发布以上小文本、参数、实际run和SHA。所有可重算矩阵、DAG和checkpoint仅留同job临时目录，不进入Git、Release或数据工件。

## 8. 本次真实高块运行

run43702348535，step selected-natural-second-left-normal-five-high-elimination，实际执行源4b95ba8d3a2542b01b55d2879e724042a2117c20。原H5在Q/F31秩均1287，实际原单位子式模31为18；全部4354行构造且高行外真零。

本次在单pivot工作量150000门槛处保完整前缀，exit75：已消786列，余501个H5变量、950行，361878个非零整数，最大3996bit。封存前27.760002284秒、最终checkpoint2.930131236秒、数学总30.715285713秒、外层30.840243188秒。未计算完整449行Schur或新二阶头。

完整binding为eff732ce44d956078f54b08550801cecf96aed1f1ce9d517cd3bfd0c45698b2b；generation17的active slot1为72645943B，SHA256179b3645a70b7d9be552f1910252cc4ed3ab5db4611a376f2a3642c10f465cb7。所有旧130解保持原样。原小回执SHA256为04efeded2528b471dba9898c0dfde67567889518b55f69a90e4c1dcb8a0110d0，详见[实际回执](r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-normal-five-high-elimination.json)。

前缀可恢复但不擅自换binding或重786步。后继先核原29个来源零向量与当前端点、同J坐标的等价关系；若成立，直接小forcing配对可先给完整第二的更强下界。未以该候选接口预填秩。
