# 独立23-query入口：从实际72只增加原collocation midpoint484

分类：独立数值实现与输入/输出契约；本文冻结时尚未执行的新计算。  
作者：ChatGPT（amplitude，AI辅助）。  
日期：2026-11-15 UTC；代码继续沿用本轮`20261114`源名。

## 1. 实际依据与新增范围

实际72从真实68父场构造22-query模型，在原全部检查下接受
$\alpha=1/16$。该次固定权重下merit由`43.7023098469222`降为
`43.6768430926219`，实际下降`0.025466754300296657`，预测比率
`0.9947316625002146`。最近拒绝档$\alpha=1/8$的全部原节点有效、
22个已建模完整角网格均为正，只有原collocation中点484失效：原
$\beta^2$最小值`-0.004507469409975373`，角index983，物理角
`3.0158062289831706`，共4个负角。该档尚未执行完整RMS检查，原记录
没有实际merit值；其`0.050652437084443655`是预测下降，不能充作实降。
完整原试步和身份见
[实际72正式结论](2026-11-14-actual-request72-twenty-two-query-nearest-midpoint484.md)。

本独立入口只把该原中点484的2048个物理角行加入优化模型，并保留
原15个left-RMS和7个中点查询。实际72的$\alpha=1/4$也只观察到中点
484失败；更远$\alpha=1/2$同时失败于中点484、485、486及已建模
left466、left484、mid485。因此不能把全部回溯限制归因于同一个缺失
查询，也不保证新增这一组后单位步长可接受。

实际72最终完整方向的线性slack均可行，保存的完整stationarity范数为
`7.380438637607479e-6`，局部和后续完整径向比例均接近1。这些是
该轮已保存的浮点模型读数，不是新QP精确解证书，也不改变原非线性
接受条件。当前方案保留阻尼270、512条工作行、200次dual预算及原17档
真实回溯，不增加迭代预算，不增加其他未观察到的查询。

## 2. 四份独立源码及冻结身份

| 新独立文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_three_query_domain_operator.py` | 32291 | `755d9bf2a01c5c417b28bfd265ee76712bba54a9fdeddf34ea56c4668abefe98` |
| `geometry_20261114_twenty_three_query_condensed_warm.py` | 42436 | `1fe5b698e452112583ee82a81ab7890095c7f3f31de05cdfb60c79e35039721c` |
| `geometry_20261114_twenty_three_query_condensed_response.py` | 2625 | `1eb07544b30abdce43599d3297c5f7732c3d19f4c74bf5aedd15ae008fa87e8a` |
| `geometry_20261114_twenty_three_query_collocation_observer_warm.py` | 16736 | `06ed3a98c48cbb2feffbc319f08c6509012f5ab9f7a460a5af3d6f74e73fc697` |

四源位于`/tmp/visible-larger-twenty-three-source/`，每个文件旁的
`.py.diff`保留相对冻结22源的完整差异。冻结22四源没有修改。
新domain钉住原22domain
`083abbf5e7f6dfede4f717d059192011e2ca4f895ff2f57e2d3760f49d06feb0`；
新warm钉住原22warm
`2b01d4384f312a435b4e00feb9296c93a15aebe063a29fe9c588ac230aaf867a`，
并递归保留原`SOURCE_NAMES/FROZEN`来源。

原R270凝聚库保持
`84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`；
局部QP保持
`ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173`；
完整QR保持
`596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722`。
原完整A/J、边界、标量profile、原338维物理场、112维core/tail、3个
全局control以及C投影和warm引擎的计算公式不改。

源检查回执`twenty-three-source-static-check.json`为4517B，SHA
`b48240702e03fa22a124487096364ef84da104f91bdab893b71cd6cd34eee1c1`。
它逐项核实7个核心计算函数及12个只读observer函数的AST与22一致，
原中点导数赋值AST一致，FD全文仅名称和身份替换可逆。源AST、编译语法、
字节SHA及整数索引检查通过；没有导入科学模块或执行数值模型。

## 3. Typed行序、完整支持及不变的局部布局

固定顺序为15个left-RMS，然后8个原collocation midpoint。每组都有
原物理角index0至2047：

```text
LEFT = (466,467,468,469,470,471,472,473,475,477,479,480,481,482,484)
MID  = (473,475,477,480,481,482,484,485)
```

left分数仍为`0.17267316464601146`；原中点分数为0.5。查询身份保留
`kind/query_index/fraction`，同一个interval的left和mid不合并。
新增mid484位于mid485之前：当前query_index21是新增mid484，其行段为
43008至45055；当前query_index22是mid485，其行段为45056至47103。
原22模型中这两个行段的语义不能直接套用。当前`row_order`说明字符串、
`QUERY_SPECS`、实际行块、导出和试步读数均包含mid484。

| 对象 | 新23-query身份 |
|---|---|
| 完整未知量 | 原236036个缩放坐标 |
| 完整B行数 | `23×2048 = 47104` |
| 唯一捕获cell | 16个，与22相同 |
| 实际查询端点 | nodes466至486，共21节点，与22相同 |
| 实际B列并集 | 21个338维物理节点及3个control，共7101列 |
| R270声明连续局部布局 | 同nodes466至486及3个control，共7101列 |
| 当前零布局列 | 无；显式空int64数组 |
| 原C可修正支持 | nodes471至482及3个control，共4059列 |

实际22已经通过left484将node484纳入真实B列与原J/P捕获。新增mid484
使用已存在的端点484、485，因此本次没有新增捕获节点，没有扩大实际
或声明B支持，也没有扩大R270局部维数。旧22的15个left查询全部保留。
当前模型不恢复历史21的zero484说法；父producer中旧历史原样保留。

新模型重新映射每个block的local列索引，完整正向和转置仍使用同一套
冻结行块及原全局scatter。当前身份同时记录实际和声明布局、空零布局、
`complete_capture_support_unchanged_from_parent=True`及
`complete_B_capture_expanded=False`。这些说明的是源契约和支持集合，
不预言不同运行中的有限浮点B数组逐位相同。

## 4. 新中点484的原始基点与完整导数链

新中点的基点直接读取原一次完整残差返回的`state.middle[484]`与
`problem.mid[484]`；不用left-RMS替代，也不重新构造另一个近似基点。
原collocation中点为

$$
Y_m=\tfrac12(Y_L+Y_R)-\tfrac h8(f_R-f_L).
$$

固定原mesh下，完整一阶链为

$$
\delta Y_m=\tfrac12(\delta Y_L+\delta Y_R)
           -\tfrac h8(\delta f_R-\delta f_L),\qquad
\delta f_i=J_i\delta Y_i+P_i\delta p.
$$

若$\Gamma$是该实际查询处对物理状态的域行导数，$\Pi$是查询处
标量参数的直接项，则编译块仍为

$$
B_L=\tfrac12\Gamma+\tfrac h8\Gamma J_L,\qquad
B_R=\tfrac12\Gamma-\tfrac h8\Gamma J_R,
$$

$$
B_p=\tfrac h8(\Gamma P_L-\Gamma P_R)+\Pi.
$$

上述各块再依原exact chart映射和原列尺度$S$处理，只除一次$S$。
共享control、共享端点和入口core注入按原实现保留；新增中点也保留
完整原$a$及返回$a'$的直接control链。端点J/P只从当前唯一完整A/J
构造捕获，不增加另一次完整Jacobian，不因query重复额外重算。

15个left查询保持原CubicHermiteSpline全链，其他7个中点保持原直接
`state.middle/problem.mid`基点。完整B伴随、full/local一致性与实际
complex方向检查按当前23个typed查询运行。它们检验实现，不替代
原全部域检查，也不成为连续全角、全站点或精确等距证书。

## 5. 固定C支持、outside项与完整R270响应

C候选的局部修正支持仍是$S_C=$nodes471至482及3个control，共4059列。
完整B作用于全部236036维，C子问题的offset仍为

$$
c+B_{\overline{S_C}}z_{0,\overline{S_C}}.
$$

outside节点包括466、467、468、469、470、483、484、485、486。
node484及新增mid484对应的outside贡献均实际存在，不能因更早历史
模型曾有零列而省略。固定C支持投影可能不可行，原径向修复、完整ray
及同一模型目标的备份/线段选择仍保留，不额外设科学门。

R270完整H路径保留7101维局部QP、原$g=A^Tb$、所有pure-global/core
项及外部仿射条件最优响应。它没有把C的固定支持施加到完整H方向。
恢复和候选选择之后，仍用完整原A/AT/B/BT读回实际gdot、全部47104行
slack和R267浮点后验。后验读数不替代原实际域或BVP验收，也不把
有限预算QP称作精确最优。末尾全向量径向缩放仍会改变outside raw部分，
不能声称最终outside保持原值。

完整权重定义、阻尼270、候选预算、dual预算及原merit均保留。
更换父场会重新冻结该轮权重，跨轮merit不能直接相减；同一轮C/H
候选比较和预测比率始终使用同一固定模型。

## 6. 首次真实父pair与own-schema续接

首次父场严格为实际72新warm/status：

| 字段 | 原身份 |
|---|---|
| science run/source | `43656584956` / `eff90c141df410e83e273d568e4b707903bf8df2` |
| parent schema | `exact-constraint-twenty-two-query-condensed-complete-H-warm-v1` |
| 原压缩warm | 4837630B，`f59e8c64399a9fed392a8f8c3976209aaa3fa662c5c6ea65d864342cca697213` |
| 原JSON status | 2213797B，`73a0c0148f6166608ce47ecd4831b6e09a013e50907bfe7aae7468b687ce857f` |
| 公开status gzip | 265087B，`ca0d071817362575517592e703b15e37f7394e2a40876d5ccbe273bea946ede7` |

公开目录为
`notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/`。
工作流透明解压status并核原JSON字节SHA，不重新序列化；warm直接保留
原压缩字节。若原JSON和gzip同时存在，解码字节必须一致。大原status
通过正常终端/Actions读取，不能经小文本connector整取或分块搬运。

原完整父`optimization_warm`子树、源账、标量、mesh及常数core/control
按原validator保留。父场及当前新warm仍明确`success=False`、
`new_coupled_finite_acceptance=False`；优化下降不是完整DN或闭面验收。

新schema为
`exact-constraint-twenty-three-query-condensed-complete-H-warm-v1`。
首次22-schema父必须匹配上述实际72双SHA；未来真实完成的23-schema
warm/status可用明确的新双SHA进行一次模型调用，仍核完整原producer。
不把prepared、pending或未完成试步当作完成父场。observer的独立
执行源身份进入当前账，数学producer是新23warm；历史22子树不改名。

## 7. 精确CLI及原预算

公开Actions恢复原accepted96、699-node prepared112、T112配置和真
零H响应后，调用：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_three_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT72/warm-001.json.gz" \
  --expected-resume-sha f59e8c64399a9fed392a8f8c3976209aaa3fa662c5c6ea65d864342cca697213 \
  --parent-status "$VISIBLE_PARENT72/driver-status.json" \
  --expected-parent-status-sha 73a0c0148f6166608ce47ecd4831b6e09a013e50907bfe7aae7468b687ce857f \
  --out "$VISIBLE_OUT/twenty-three-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
```

`T112_TRUE_ZERO_ANCHOR`仍是原`e788a28d…`完整真响应，路径
`public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz`。
实际下降warm保存后，执行新的原FD入口：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_three_query_condensed_response.py" \
  --accepted "$VISIBLE_ACCEPTED" --prepared "$VISIBLE_CONDENSED_WARM" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
```

FD在真实新warm处重新运行原完整方向、两阶Richardson及`5e-5`门。
使用的是原真零H全J明确构成的affine图，不把当前非零H称作已有真
native响应。此次优化入口没有新增native求解、完整DN联解或最终
闭面审计。原全部节点/中点、两套完整RMS、rho、实际merit和17档
回溯保留；23组模型网格不替代这些实际门。

## 8. 输出与唯一调度草稿

输出保留完整原model/trials、typed角读数、原中点及collocation只读
observer、B/Gamma/Pi/原端点捕获、R270局部root/affine/recovery、QP
数组、C/H同模型比较、完整原残差后验、新warm与实际FD身份。observer
只读取原evaluate返回值和原一次权重，不新增科学调用；观察异常只记
报告，不改原finite、merit、返回值或决定。

geometry负责的唯一工作流草稿已独立交付root，本接口不创建第二个
dispatch。草稿目录`/tmp/visible-larger-request74/`：

- `visible-larger-public-condensed-qp.yml`，23792B，SHA
  `40ca08e5ab84b13dcb4670830301127af0720b5f39548aa62960b21cd4662f43`。
- `public-condensed-qp-request.json`，13319B，SHA
  `d3bc7e4adbf0b1036864a2f8c5344b413b5eca1043b7d2b1ef9bbfd7fc977920`。
- `workflow-relative-to-actual72.diff`与`request-relative-to-actual72.diff`
  保存相对真实72工作流/请求的完整差异。
- `static-check.json`，9279B，SHA
  `9d1bce391fe11de0cb3545ca5dae88fd15ceffb3ae94d4417de18b35e4613f7d`。

47个源pin逐字核对，包括原43项和新四源；publisher钉住
`5a0216d00c8ca732b03886904ca232bc9453bc12d47a697d9384e4871c594de9`。
11段bash语法和6段内联Python AST通过；原trigger、selector、并发、
环境、预算及阈值保持。父22与当前23的schema分别验证，没有递归修改
历史父字段。以上仅为源码和字节检查，不是74实际计算回执。

root负责普通Git、真实pull/README检查、推送及唯一调度。运行后先读
全部原试步、最近拒绝的真实阶段与新父pair；完成字节读取可另记范围，
不把追加审计变成停止主线的门。
