# TC 终态以后严格补集上的完整 cell 续接与全域 source 聚合

本页处理原 TC 的执行瓶颈，所认证的 trial、真根、物理 193 状态、96 列、
原 source 窗口和方程均不改变。它没有计算一套新 trial，也没有完成真 PDE
列、正侧逆或有限物理方阵。原 `46117170011/1` 活跃期间，本入口没有权利
领取任何 cell；新生成器只返回 `ready=false`。

相关完整源码：

- [元数据、单格 memo 与完整并集算术](../scripts/fourfold_codazzi_true_root_missing_cell_fleet.py)；
- [missing-cell 与聚合科学 owner](../scripts/fourfold_codazzi_true_root_missing_cell_fleet_owner.py)；
- [互斥 cell 作业公开 worker](../scripts/fourfold_codazzi_true_root_missing_cell_fleet_public_worker.py)；
- [完整终态并集公开 worker](../scripts/fourfold_codazzi_true_root_missing_cell_fleet_merge_public_worker.py)；
- [元数据生成器及实际工作流模板](../scripts/make_true_root_missing_cell_fleet_manifest.py)；
- [执行入口与状态](../notes/2026-11-28-TCF-terminal-missing-cell-fleet-entry.md)。

## TCF.1 原对象与已完成目标

唯一初始父输入是完整 manifest
[`2026-11-28-true-root-trial-complete2677-inputs.json`](../notes/2026-11-28-true-root-trial-complete2677-inputs.json)，
whole SHA256 为
`6b82d09170ed4ec780eccd0910cb69df98615390ef2f73237ed324d1e3f2c692`。
它有 184 个完整 current 文件、32 个完整 historical 输入，包含原 40 个
native part 的恢复与完整方向重建 recipe。这些边仍由原 manifest 的全部
whole-file 身份决定；新 manifest 以整文件 DAG 引用它，不截短它的输入集合。

原 trial 的 7671 个节点、7724 个 certification cell、真正的 root 节点和
四个 `[7671,193,96]` 端点数组保持不变。定义及 plan 的 whole SHA 分别为

```
bd98e1f64448a1531304ed5f7a07ebcc991ad642bf550d436312d8232816fe12
5617310e579bf61b9e4f0a67d6d0dadda8524562cc65a5f39ff254db93809fe4
```

四个数组各 1,137,026,304 B；依次是值和一、二、三阶径向导数，whole SHA 为

```
52147b57bc94ad5f8bd458cc8bc4588b8a2e3b119ea48d1622aad19bc80f19de
347b4d3b09d450431e1fd9c000e903711facf14d3df66d5a1b0a512240fc2ae9
da4a4a3f8665ee589be57c79e27e6413cb7a19bc6e23bffe856a5eac8f831857
0110dde53231a7ba5c91517ebb6fc705af5af038f405270c6cdb37f8e3fd59b1
```

必要恢复仍调用原 `choose_all_columns`，但只把这些已定义数组重建为作业私有
输入。四个全文件必须逐一匹配以上身份；此调用不授新数学结论。它不进入旧
signed matrix、waist norm 或任何已完成 source norm 的计算。原 signed matrix
和父终态已经完成的 negative source 结果均逐字复制。

完整 source 名称及列数仍为

| 原窗口 | 每个结论的列数 | 原投影 |
| --- | ---: | --- |
| `negative_root` | 96 | 全部原 mode |
| `negative_strict` | 96 | 全部原 mode |
| `positive_low` | 96 | 原 low 投影 |
| `positive_high_collar` | 96 | 原 high 投影 |
| `positive_high_body` | 96 | 原 high 投影 |

每个 cell 都先形成其所有活动窗口、每个窗口的全部 96 个贡献，随后才能
推进一次完整 cell 游标。未在该 cell 活动的窗口保持完整零向量；这仅表示
该窗口的积分区域不含此 cell，不表示删去物理源、mean 或方程分量。

## TCF.2 初始终态准入

`inspect_parent` 读取父 run 的完整 state、完整 parallel ledger、完整
contiguous prefix、矩阵、可能已经完成的 source 文件及 execution。各文件
均有全长度、全 SHA 和 Git blob 身份，execution 必须逐项绑定整个科学文件。
原 TCXV owner 的 whole SHA 固定为
`2408b84e7aa820ec6942dcd6255b77583cd776072c09fb6f521866930fcb7200`。
调用的原 parallel validator 校验所有 seed 和三个完整区间的身份、游标、
五组 96 上界，以及 contiguous prefix 与整个 accepted union 的一致性。

父记录必须包含科学 child 和公开 job 的终态时间、真实整数 return code，
以及全部原 arithmetic child 的终态。执行前 worker 另外读取真实 GitHub
Actions run API，要求 `46117170011/1` 的 `status=completed`。workflow
conclusion 可为 failure：接受的对象是严格验证过的完整 cell 上界，不把
workflow success 当成数学证明。任何活跃父 run 都不能通过此准入。

若父 accepted union 为 (A_0\subset\{0,\ldots,7723\})，新作业只拥有

\[
 M_0=\{0,\ldots,7723\}\setminus A_0.
\]

初始 (A_0) 由旧完整 seed 及原三个已接受区间前缀组成。比较的是**整个并集**，
不是仅取 contiguous 前缀。原第一子进程之后仍有洞时，第二、第三子进程
已经完成的 cell 同样不可重算。

## TCF.3 互斥分配与再次续接

元数据生成器把 (M_0) 的每个连通整数区间按至多 256 个原 cell 划分；该
调度整数可在 `[1,512]` 内显式指定。它不依据 trial 数值选择列或积分片段。
每份 assignment 都记录完整起止编号、96 列和五个原窗口。验证器要求所有
assignment 按序展开后恰好等于整个 (M_0)，且无重复编号。

每个公开 runner 只有一个 arithmetic child。默认最多六个独立公开 jobs
并行，`fail-fast=false`。这是改变计算资源分配；它没有把 96 列或一个 cell
的多个窗口拆成不同成功目标。所有局部记录都继续标明
`original_TC_global_targets_complete=false`。

在 native 输入恢复之前，各 job 必须成功推送两种小标记：

1. 同一终态父并集的共同标记，绑定 fleet manifest SHA 和全部 assignment；
2. 本 assignment 的唯一 consumed 标记，绑定真实 run、attempt 和输出目录。

共同标记已存在时必须逐字相同；因此另一个 manifest 不能把同一父并集的
missing cells 重新划分后并行领取。相同 assignment 的已消费标记禁止科学
重试。任何非快进推送均由原完整 public transport 立即 pull/rebase 后继续推。

每个完整 cell 的五组 96 累加器和新游标在同一原子文件内保存。发生失败时，
该文件保留最后一个完整 cell；失败 cell 的部分窗口不进入累加器。公开 worker
定期推送整个记录，并在真实终态再次保存最新整个文件。没有分块上传私有数组。

所有 assignment jobs 真正终态后，聚合 job 即使看到部分 job failure 也读取
其已保存的完整前缀。它检查真实 job API 的全部固定 job 名称、run/attempt 和
终态，再把每个 accepted 前缀及父 (A_0) 合成一个完整并集 (A_1)。
新的 `actual-accepted-union.json` 含全部五组 96 上界、全部接受区间、全部
余缺区间和每个源 actual/execution 的 whole 身份。

若 (A_1) 仍有洞，下次生成器必须同时给出此前整个 fleet manifest 和聚合
actual/execution。它沿完整小元数据 DAG 验证此前每个 job、整数域及祖先，
直接复制已认证的整个 (A_1) 上界。新的 worker 要求前一 fleet 的**整个
Actions run** 已 completed，才能领取 (A_1^c)。新的父身份包含该完整终态
并集，故同一代仍互斥，下一代只恢复此前未接受的严格尾段。

## TCF.4 唯一局部算术优化

执行的 cell body 是原 owner
[`fourfold_codazzi_true_root_trial_owner.py`](../scripts/fourfold_codazzi_true_root_trial_owner.py)
中从 `budget()` 到完整贡献形成结束的逐字表达式；整 owner 的 SHA 为
`193a317166204eef3870f12e5aee08be5a3de46e18b65de4b471b2a478f253dc`。
提取的完整 cell text SHA 为
`5aee786a11a3fddce44a114e46c5055fb28a15c9c280631fb60e9f1f207623ca`。
完整 scalar 输入函数同样按原 AST 原样取出。真 (h)、七阶 Hermite、完整
reflection、多项式径向导数、cutoff、完整 selected background、完整 residual
以及所有窗口 norm 的计算顺序均不改变。

原 `pair_cell_norm_squared` 在每个窗口内，对两个完整 residual Fourier
张量分别调用 `legendre_coefficients(p.Fourier())`。正侧同一 cell 有 low 与
high 窗口时，原程序重复变换相同的两个缓存 Fourier 对象。新 memo 只省去
这个已经完成的、输入完全相同的变换。

严格契约如下：

- memo 在进入一个完整原 cell 时建立，退出该 cell 即清空，并恢复原方法；
- 键是完整输入 `CBox` 的对象身份；缓存保存强引用，防止 Python 回收后重用 id；
- 首次调用前，把输入 real/imag 的 lo/hi 四个数组设为只读；原变换产出也
  把全部对应数组设为只读；
- 首次调用仍执行原完整 `legendre_coefficients`；以后相同对象的调用返回
  第一次完整输出，绝不选中点、降阶、截尾或重建一个更窄 Box；
- 原 `Fourier()` 已经按原代码缓存完整结果；随后 norm 只读该缓存和 Legendre
  输出。原 cell body 在此阶段没有任何修改它们底层别名的操作；
- 每个窗口的投影、Sobolev 权、平方、逐阶积分、完整有限支撑误差三角不等式
  和向量累加仍各自执行。memo 不缓存或复用一个窗口的 norm 来代替另一个窗口。

设第一次变换返回 (L=T(Z))。原上下文、320 bit 常数、原有向数组基本运算
及其顺序固定，第二次作用于同一个未变 (Z) 的完整表达式也是 (T(Z))。
复用整个第一次 (L) 因而没有新增误差项，也没有改变任何窗口的数学量。
只读要求若触发实际写入错误，作业必须失败并保留此前完整 prefix，不能移除
只读保护后继续冒称相同条件。memo 的生命周期最多一个 cell；统计中保留
请求数及相同对象命中数，以实际运行说明是否节省了重复工作。

这里没有声明速度倍数。当前只作静态审计；每个真实 cell wall time 与 memo
命中会留在 actual 中。独立 runner 减少原三个 arithmetic children 在同一
runner 上争用内存带宽的可能性，但其实际收益同样以新 run 为准。

## TCF.5 完整上界的聚合证明

令 (w) 是上述一个原窗口，(j\in\{1,\ldots,96\})，(I_i) 是原完整
certificate cell。原 cell 方法已经证明非负有向上界

\[
 \int_{I_i\cap W_w}\|P_w R_j(r)\|_{Y_w}^2\,dr
 \le e_{i,w,j}.
 \tag{TCF.1}
\]

它包括原 finite polynomial 的完整 Parseval/Legendre 部分，以及原完整
有限支撑 error triangle。此处不改变 (R_j,P_w,Y_w)、ordinary (dr) 或
normalized circle。对任意已接受的互斥 cell 集合 (B)，其整个 saved vector

\[
 U_{B,w,j}\ge\sum_{i\in B}e_{i,w,j}
 \tag{TCF.2}
\]

由原向量上取整累加器保证。新 cell job 继续使用原
`_whole96_add_upper`，保留先前修正的完整 96 元零向量维数，不退回标量广播。

设父完整并集及所有新 accepted prefix 的集合为互斥的

\[
 B_0,B_1,\ldots,B_m,
 \qquad A=\mathop{\dot\bigcup}_{\alpha=0}^m B_\alpha.
\]

每个 saved binary64 上界均由规范 `float.hex()` 全字串读回。聚合科学 child
把它转成**精确 dyadic Fraction**，对所有源完整相加，再只上取整一次：

\[
 V_{A,w,j}=\operatorname{up}_{64}
       \left(\sum_{\alpha=0}^m U_{B_\alpha,w,j}\right).
 \tag{TCF.3}
\]

精确和为非负。程序比较所得 binary64 的精确 Fraction；若其低于精确和，
才向 (+\infty) 作一次 `nextafter`。程序要求最终值有限且不小于精确和。
因此 (TCF.1)—(TCF.3) 给出整个 (A) 的每个原 source 上界。这里的聚合是
此前尚未完成的更大 domain 的新上界；没有重新计算旧 cell 或旧 source norm。
在后继 fleet 中，已完成的 (V_A) 直接作为一个整体 (U_{B_0}) 复制使用。

仅当完整整数覆盖检查得到

\[
 A=\{0,1,\ldots,7723\}
 \tag{TCF.4}
\]

时才可形成尚未完成的原负侧/正侧完整 source 结论：

\[
 \|P_wR_j\|_{L^2(dr;Y_w)}\le\sqrt{V_{A,w,j}}.
 \tag{TCF.5}
\]

平方根在实际公开科学 child 中以原 320 bit Arb 做有向包围。其上端序列化
后重新读取，必须包含原有向上端。负侧两个窗口或正侧三个窗口的全部 96
记录作为一个自然完整文件保存，仍使用原 `validate_complete_result` 的
全部字段、两 independent waist means 和原 14 ports 资格。

已经完成的负侧目标若在父终态存在，只逐字复制，不再计算 (TCF.5)。全部
signed matrix/waist 原结果也逐字复制。新聚合结果的 input manifest SHA
指向新真实聚合输入；不会伪装成旧 manifest 下已经发生的计算。

一旦一个新 union 或完整 source 文件保存，科学 child 等待该整个结论的
真实 push acknowledgment，才进入下一条新结论。公开 worker 保留整文件
SHA、run/attempt、实际 return code、源 job API 和最终 execution。整个
accepted union 的保存成功与完整 source 域成功是两个独立字段；部分并集
绝不标成全部原 source 结论。

## TCF.6 资源、记录与适用范围

每个 cell runner 只保存必要原输入与四个完整 trial 数组，声明的完整私有
数组限额为 12 GiB；数组不进入 Git、artifact 或 Release。公开容量按每个
assignment 的完整 actual/execution、共同标记和最后整个聚合预算一起预留。
设 $N$ 为全部互斥 assignment 数。每个完整科学 actual 小于 65,000 B，保留
全部五组 96 维上界；每个 public execution 小于 20,000 B。非空 accepted
prefix 的 actual 必须含原四 whole-array 恢复回执。空 prefix 允许尚未恢复。
整个 transport state 在作业私有目录完整写入并逐字节读回；公开记录绑定其
长度与 whole SHA，并保留科学文件身份、run/attempt、实际退出、已接受游标、
输入身份以及 README 检查链。容量以 $85000N+390000$ B 加 120,000 B
reserve 核算。390,000 B 中聚合占至多 360,000 B；生成器以全部真实分配、
20 位 run id 长度上界和与 worker 相同的序列化函数核算其余标记至多
30,000 B。并发上限只控制同时运行个数。生成器落盘前核对应真实 run API
已终止，worker 在领格前复核。

每个公开文件必须小于 100,000 B，topic 仍按实际完整 Git tree 的 200 MB
规则核算。没有把大型数组转成文本、切片或逐 cell 文件来绕过容量规则。

原 public transport 的 pull/rebase、真实树容量和两 README 检查保持原实现。
每次 pull 都核两 README；长计算最长 1800 秒再次 pull。规则有差异时保存
已有完整 prefix 后按实际差异处理，不能继续使用未读新规则。

本方法只解决同一原 TC trial 的完整 source 认证的缺格计算。它可提供原
7724 cell 全覆盖后的完整 residual96；实际 PDE correction、positive/negative
receiver、SC 真 root96、完整 Θ、mean/phase/height 行及最终物理方阵还须各自
满足已有接口。特别是 finite trial、全域 residual norm、已修正 PDE 列和
可逆 square 是不同对象，本页没有把其中任一个替代另一个。

**初始交付状态：**全部新源码/完整旧前缀只作 AST 与元数据检查；原 run 仍在
运行，故尚无新 fleet manifest、实际 job、任何新 cell 数值或完整 source 结果。
终态后可用生成器直接得到整份实际工作流；任何后续数字只以其真实 public
actual/execution 为准。
