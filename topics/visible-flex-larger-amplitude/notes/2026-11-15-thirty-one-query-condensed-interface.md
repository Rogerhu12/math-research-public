# 独立31查询入口：从真实94继续，加入 LEFT464、LEFT486、MID486

分类：独立有限算法接线、原件身份与公开 Actions 调用契约。  
作者：ChatGPT（geometry，AI辅助）。日期：2026-11-15 UTC。  
状态：四源、完整相对差异和静态检查已冻结；本稿没有新的科学运行或未来结果 SHA。

## 1. 三个新增查询各自有原实际失败证据

实际94从真实89父场形成一个完整新模型。第四个原试探 `alpha=1/8`
接受，同一模型固定 W 下的 merit 从 `43.45995557126006` 到
`43.42759299648642`；原报告下降 `0.032362574773642905`、比率
`0.9894236434528396`。这里只引用原保存字段，不重新计算它们。
完整事实、四试探、原28查询、B/C/H与FD范围见
[实际94正式结论](2026-11-15-actual-request94-twenty-eight-query-eighth-step.md)。

| 原实际试探 | 已经过的原检查 | 真正失效位置 | 保存原值 |
|---|---|---|---|
| `alpha=1/4`，最近拒绝档 | 原节点、全部28个选定网格有效 | 唯一坏原中点 MID486 | beta平方 `-0.033482995304567886`，角968，phi `2.9697868053466014`，4个负角 |
| `alpha=1/2` | 原节点、全部原中点、28网格有效；真实merit已下降 | 完整原左RMS的 LEFT464 | beta平方 `-0.8341048662546815`，原左分数 `0.17267316464601146` |
| 同一 `alpha=1/2` | 同上 | 完整原左RMS的 LEFT486 | beta平方 `-0.01000663458228912`，同一原左分数 |

四分之一步没有进入实际merit及完整RMS。半步真实merit为
`43.344792966854236`，原下降 `0.11516260440582471`、比率
`0.9280139626199154`；随后左RMS恰有464、486两处失败，右RMS全部有效。
半步原中点486有效、四分之一步却无效，所以没有非线性域随alpha单调
的事实。正线性reserve、全部选定网格有效，均没有替代完整原检查。

原28中既没有LEFT464、LEFT486，也没有MID486。保留的LEFT487和MID487
在半步、四分之一步及接受的八分之一步均为正。此次只按以上三处已观察
失败，同时加入三个查询；不经过29或30查询中间运行，也不预言更大接受步。
新父场、全A、B、C offset、H与方向都将实际重形成，不能把未来变化归因于
新增某一查询的唯一效果。

## 2. 独立四源与冻结身份

交付目录 `/tmp/visible-larger-thirty-one-source/`。每件同名 `.py.diff`
是相对真实94 dispatch `b75f41fa32b8ead9bb5121b725a0afe1a2f5ae5c`
所用冻结28同类源的完整差异。原28四源及其历史父源均未改写。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_thirty_one_query_domain_operator.py` | 34319 | `44c82d410f1e52f45e6b87f9e9eb86b3aeccb0e937510f04561855360347128f` |
| `geometry_20261114_thirty_one_query_condensed_warm.py` | 47119 | `1cf2d88dfeeba1ea542dabad261759151f1c6e30e29caece8fc2056fbe5f107e` |
| `geometry_20261114_thirty_one_query_condensed_response.py` | 2619 | `1bc1f6e02e2d450b24df73aab6e660c4453fdbf088e9aa2b3054b5ae5a2d84d5` |
| `geometry_20261114_thirty_one_query_collocation_observer_warm.py` | 16728 | `1e2f1ff075daf761c496271b5d93d29178d7af098d2bc03ba0eb6b38328107a1` |

domain锁实现来源为原28domain
`25767045b9a26764bfdb89881832ec7da01de1ac86ebc491402c7b9801175cd0`；
warm锁直接父28warm
`990029102808ede1134bd9e6a163b6da84ae0d9189857f49af216ba64bfa188c`。
新warm继承父 `FROZEN` 和完整 `SOURCE_NAMES`，增加本次domain/warm，
数学producer集合从实际父64项变为66项。FD与observer继续各自记来源，
不把只读wrapper塞进历史数学producer集合或改写 `resume_producer`。
这两个新增数学文件和额外response/observer身份都明确是新来源。

新optimizer schema：
`exact-constraint-thirty-one-query-condensed-complete-H-warm-v1`。
新B schema：
`captured-thirty-one-query-original-RMS-and-collocation-midpoint-domain-v1`。

基础完整角域源 `af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7`、
R270 condensation `84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`、
local-QP `ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173`
以及原C公式均不变。

## 3. 完整查询次序、捕获cell与新节点464

```text
LEFT = (464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487)
MID  = (473,475,477,479,480,481,482,484,485,486,487)
```

先20个LEFT、后11个MID，每个保原2048个物理角。删除三个新增项后，
余下整个28项typed序列与父序列逐项相同，包含kind、interval、fraction；
仅原组号会因插入而变化。每个kind的定义不因共享interval而合并。

| 对象 | 实际94的28查询 | 本次31的源级整数配置 |
|---|---:|---:|
| LEFT / MID数 | 18 / 10 | 20 / 11 |
| B行数 | 57344 | 63488 |
| 唯一捕获cell | 18 | 20；新增464、486 |
| endpoint union | 465至488，24节点 | 464至488，25节点 |
| 唯一新增endpoint | — | 464 |
| 完整B/H局部维度 | 8115 | `25×338+3=8453` |
| 原C局部维度 | 4059 | `12×338+3=4059` |
| 显式zero-layout | 空 | 空 |
| 原完整未知量 | 236036 | 236036 |

新增LEFT486/MID486使用的486、487两端已在父endpoint union中，
但新cell486仍须进入capture records，不能只因两个端点已出现就跳过
这个cell的原完整J/P绑定。LEFT464需要真正新增节点464，同时使用旧节点465。

`CAPTURE_INTERVALS`仅对捕获去重；`QUERY_ENDPOINT_NODES`由所有cell的
左右端点联合集推得；`LOCAL_LAYOUT_NODES`直接引用该联合集。运行时仍从
全部实际B block的global columns形成并集，与布局逐项比较。8453是
源级整数配置，不是已生成新B或新H的数值结论，不预填矩阵SHA。

原完整chart中节点j使用 `[(j-1)*338,j*338)`。新增464的原完整列是
`[156494,156832)`，恰338列；global p仍 `[236033,236036)`。
原全局列编号没有重新编号。因在B局部物理块前插入464，旧B局部物理列及
p列的位置整体后移338；所有block的局部位置继续由 `searchsorted`
原全局indices重新形成，不能搬用父B局部indices或C局部映射。

下表均为0起始，行区间半开：

| 新查询 | 新query index | 新B行区间 |
|---|---:|---|
| LEFT464 | 0 | `[0,2048)` |
| LEFT486 | 18 | `[36864,38912)` |
| MID486 | 29 | `[59392,61440)` |

原LEFT465至485各自组号后移1；原LEFT487从17变为19。
原MID473至485从18至26变为20至28；原MID487从27变为30。
完整31条与原28映射保存在 `thirty-one-source-static-check.json`，
同时保存每条原typed定义、节点对与全部行区间。历史28结果保持历史行序。

## 4. 保留原LEFT与MID的全部状态链

LEFT464/486沿用原左分数 `0.17267316464601146`，原station浮点表达式
与原 `CubicHermiteSpline` 取值不变。它们不是collocation midpoint。
其完整Hermite链仍包含左右节点全部338物理分量、两端原J/P与查询处
3个global控制的直接标量项。没有手写新多项式替换原spline计算。

MID486直接读取原evaluate返回的 `state.middle[486]` 和 `problem.mid[486]`。
原定义及变分为

$$
Y_m=\tfrac12(Y_L+Y_R)-\tfrac h8(f_R-f_L),\qquad
\delta f_i=J_i\delta Y_i+P_i\delta p.
$$

若原角域函数对查询状态的完整行梯度为 $\Gamma$，直接控制项为 $\Pi$，
保存的原组装式仍为

$$
B_L=\tfrac12\Gamma+\tfrac h8\Gamma J_L,\qquad
B_R=\tfrac12\Gamma-\tfrac h8\Gamma J_R,
$$

$$
B_p=\tfrac h8(\Gamma P_L-\Gamma P_R)+\Pi.
$$

原坐标尺度只除一次。完整正向与转置继续用同一份rows/global-columns。
所有原18 LEFT和10 MID也按同样定义保留；每个完整grid及Gamma/Pi均沿
原256角chunk导出。新增捕获使用同一次完整A/J已有的端点因子，不另构造
第二个完整Jacobian，不冻结某些控制或删去outside列。

`__init__`的完整数值AST、原完整验证和export AST，除描述范围的字符串
外与原28相同。`query_value`、`selected_actual_angles`逐AST完全相同。
本次只改变选择集合及必要身份，不以该静态检查宣称新父场上所有角均有效。

## 5. C4059与完整H8453分别重新形成

原 `geometry_20261114_fixed_support_halfspaces.py` 的固定支持仍是节点
471至482的全部物理列，加三个global p，原109 free-core不在C局部未知量中。
该源SHA为
`0c5573ea26d2c69c1a22595e00de9e41b38981793b88f4f52086d7713d111f68`。
其 `fixed_support_indices` 仍使用原完整chart列，重新核包含于本次B列集合；
因此C4059不用也不能通过旧B局部位置硬编码来保留。

对完整当前原LSMR方向 $z_0$，原C子问题的全部行offset仍为

$$c+B_{\mathrm{out}}z_{0,\mathrm{out}}.$$

当前outside节点为464至470、483至488，共13节点；新增464的贡献必须
真正参与这一次完整B action。所有63488行都保留。原C列对角来自本次
完整原模型；原局部zero-row/infeasibility报告、fallback、全向量radial
和segment处理均不变。没有要求offset必须正，也不把某个C局部子问题
不适定或未收敛转成原BVP的拒绝门。实际94的C报告不能冒成新31报告。

完整H支路仍调用
`CondensedModel(factor,g,np.asarray(domain.local_indices))`；因此其局部
未知量实际接8453完整B列，不受C4059限制。原完整H仍是同一全A、原W、
原chart与lambda270形成的完整阻尼模型；完整g仍由原A转置作用得到。
自由core109、全部纯global行与外部物理变量仍按原完整链条件消元和恢复。
新支持的first/last为464/488，原索引公式的左右外部物理节点数为463/210。
这些为布局推论；实际因子、局部root/affine/g及完整恢复方向在Actions重新生成。

`main.project`逐AST同原28，原C调用只执行一次并返回同一tuple，
`actual_current_B_C_layout`仅读取本次原返回的维度、indices与SHA。
`main.choose`、完整A/AT/B/BT读回、同一个f_C与H候选比较、R267原浮点
后验、完整恢复及原选择器也逐AST不变。R267仍为rawfloat诊断，不冒严格证书，
不添加QP最优性或线性reserve阈值作为新的科学门。

## 6. 真实父94与own-schema续接范围

父公开目录：
`notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm`。

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| `warm-001.json.gz` | 4913995 | `292732a80175af1fc6328e68954a04587cedc871246d2db75b6dd1d7d46df9c0` |
| `driver-status.json`原始解压字节 | 3165856 | `8b65e2f913e882fffc2a9d92998ea908f89981cd448afc0b81a367a5581ff237` |
| `driver-status.json.gz`公开压缩原件 | 361821 | `50e9075ade6d3876f229d91431fbde237e73983ab0e424004e9a0f639cafd982` |

首个31入口同时硬锁真实94 pair。其父schema为原28，而本次schema为31，
不把原父producer改标签。以后同31源的own-schema恢复沿原完整身份分支；
本稿不预造未来31 warm或成功条件。

源码阅读也确认：**冻结28入口本来就能以自身schema继续真实94**。
原28 `main` 与 `_run_engine` 两处均只在初始26父schema时硬锁实际89，
own28分支转入原完整 `baseline.bind_parent`。后者核真实warm/status、
完整producer源集合及各SHA、原prepared/accepted/zeroanchor/config、
完整profile/mesh/field representation和末端常数p身份。原observer把额外
身份放独立字段，不破坏这个own-schema分支。选择31是针对本次三处实际
失败的明确算法试验，不是因为28入口无法恢复。

本次两层31验证沿同结构，只把初始父切成实际94原28，并保own31分支。
父64个数学源、status.identity嵌入与warm/status SHA已在本地只读原字节核对。
新进程不会复用父A/J/C/H/direction或把父merit作为fresh值，原engine会真正
重新evaluate、固定新W并形成一次完整新模型。

原四个物理输入继续为已完成accepted96、prepared112、真实zero-H T112
affine-J anchor、T112-config；当前非零H的完整native没有因本任务而新增。
warm中的所有112高度及完整p等字段原样传递，不阈值化或用zero代替。

## 7. 唯一原共享工作流与完整CLI

草稿目录 `/tmp/visible-larger-request98/`，基线为冻结request94。
最终由root接入同一个
`.github/workflows/visible-larger-public-condensed-qp.yml`，唯一push触发仍是
`topics/visible-flex-larger-amplitude/computations/public-condensed-qp-request.json`。
原lane `condensedqp`、concurrency和不取消前次运行的策略保持，无另支并发。

请求保全部63个旧显式pins，加四新源为67。publisher仍是
`22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`。
Python3.12.14、numpy2.3.5、scipy1.17.0、原固定setup actions、public78
恢复、原四输入和最终always artifact/publisher均不变。该67是工作流显式
来源表，不与数学producer66或FD/observer集合计数混为一谈。

父status允许公开plain/gzip别名；如果gzip存在，先核压缩原件，再解压并核
原始3165856字节。若两别名都存在，原字节须完全相同。warm直接复制压缩原件，
status用 `write_bytes(raw_status)`，不经JSON重新序列化。记录parent94的
run/source及两种传输身份；不下载746 MB完整历史artifact。

原科学调用：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_thirty_one_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT94/warm-001.json.gz" \
  --expected-resume-sha 292732a80175af1fc6328e68954a04587cedc871246d2db75b6dd1d7d46df9c0 \
  --parent-status "$VISIBLE_PARENT94/driver-status.json" \
  --expected-parent-status-sha 8b65e2f913e882fffc2a9d92998ea908f89981cd448afc0b81a367a5581ff237 \
  --out "$VISIBLE_OUT/thirty-one-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
```

原warm进程35分钟、FD25分钟、job80分钟保持。工作流已有的accepted-warm
身份读取只决定后续FD取哪个真实文件，不替换原科学接受。没有调高模型、
LSMR、QP、projection、回溯或时间预算，也没有新增额外数值检查进程。

随后原FD用本次真实warmSHA和完整producer，入口仅改为
`geometry_20261114_thirty_one_query_condensed_response.py`，其余参数
逐字保原：`--accepted`、`--prepared "$VISIBLE_CONDENSED_WARM"`、
原zeroanchor/config、`--out "$VISIBLE_OUT/physical-response" --angles 4096`。
原完整方向、步长、两级Richardson及 `5e-5` 门保持。它仍是实际新warm处的
zero-H true-J affine映射校验，不冒当前H非线性native响应。

## 8. 输出、来源与静态证据范围

将输出原完整warm/status/model、完整31-query B/Gamma/Pi与actual node capture、
原C报告、完整H因子/恢复、QP及全原trial理由、只读collocation/midpoint资料，
并在warm实际进步后运行完整FD。原artifact路由仍
`visible-followup-condensedqp-${run}-${attempt}`。任何失败仍由always上传保全；
没有未来success、下降值、矩阵身份或native完成flag预填。

关键当前静态原件：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `thirty-one-source-static-check.json` | 19078 | `6e5f58cad128889add14b48f7409bd14b15e508c07f48b24bb657af70b13099f` |
| `visible-larger-public-condensed-qp.yml` | 27554 | `7b8091cdedcf601bdd678c6b0a8c25b5d65b56ea86bed67db2fa7816a845aa92` |
| `public-condensed-qp-request.json` | 27611 | `de47834ecc9f81437ae5bb5efb18a3368cf1b5006f2f6627d821e06c32a1df2d` |
| `request98-static-check.json` | 28343 | `b8f9708411bb9d06165c5df5115b3cda6f5a7c35d49b0b22109137ec8ea0183a` |

已完成的本地验证仅有：四新源AST/compile-only和完整diff；17个核心函数
逐AST相同；完整domain构造/verify/export排除范围描述字符串后相同；
FD全文逆向换名相同；observer全文逆向换名和entrypin后相同；真实父64源
及pair字节/JSON关系；全部整数typed顺序/endpoint/global与local映射；
67工作流sourcepins逐文件SHA；11个shell块 `bash -n`、6个内嵌Python AST；
原setup、78恢复、四物理输入、预算及数值CLI逐项相同。父恢复body在明确
真实run/source/schema/hash/字节数换回后与94全文相同。

没有导入科学模型、构造算子、生成新矩阵、计算范数、求解、域扫描、FD、
native或本地数学运行。检查结果是可复核的来源/接线证据，不是新的科学门。
原README的完整BVP、当前H真实native、same-g精化、闭场与全像证书责任仍保留。
