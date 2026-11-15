# 独立28-query入口：真实89父场，分别加入 LEFT487 与 MID487

分类：独立数值实现、原件身份与后续 Actions 调用契约。  
作者：ChatGPT（geometry，AI辅助）。日期：2026-11-15 UTC。  
状态：源码、完整差异及静态检查已冻结；本稿没有新的科学运行或预填结果。

## 1. 两个新增查询各自对应已保存的真实失败

实际89的全部六档原试探在同一个新模型、同一套固定 W 上比较。原
第六档 `alpha=1/32` 接受；实际 merit 从 `43.46872005143614` 变为
`43.46027880669424`，原保存下降 `0.00844124474189556`，原比率
`0.9946191991101806`。新 warm 和完整 affine Rphi FD 均已真实生成，
但 `success`、`new_coupled_finite_acceptance` 仍为 false。
详见[实际89完整结论](2026-11-15-actual-request89-twenty-six-query-step-and-cell487-limits.md)。

本次同时加入两个查询的根据如下，不把两种状态或两档失败混成一件事。

| 原实际试探 | 节点、中点及原26查询 | 真正阻点 | 保存原值 |
|---|---|---|---|
| `alpha=1/16`，最近拒绝档 | 原节点和26查询全部有效；仅原中点487失败 | MID487 | `beta_squared=-0.00668183443965642`，角 index982，phi `3.0127382674073995`，4个负角 |
| `alpha=1/4` | 原节点、全部原中点及26查询全部有效；真实 merit 已下降 | 完整原 RMS 扫描的 LEFT487 | 原分数 `0.17267316464601146`，s `1.2550366105017607`，`beta_squared=-0.007792206623105091` |

最近档原完整 RMS 和实际 merit 尚未执行。四分之一步的实际 merit
已经是 `43.41518161646212`，原保存下降 `0.05353843497401556`，
原比率 `0.8130548788761999`；随后原完整左 RMS 族在698点中只有
interval487失域，右 RMS 族698点全部有效。因此不能把四分之一步
写成“merit未下降”或“原中点失败”。

实际89的原9个 MID 明确为
`473,475,477,479,480,481,482,484,485`，没有487；原17个 LEFT 也没有487。
新增 MID479 在实际89的全部六档均有效。这只说明已观察的域分布，
不把不同父场/新模型的结果归因为某一个新增query的唯一效果。

本次直接从89的真实新 warm/status 继续，加 LEFT487 和 MID487，
不插入一个27-query中间试验。两个新增网格仍不能替代原全部非线性
节点/中点/RMS/边界检查，也不保证较大步长或完整BVP接受。

## 2. 四个独立源和冻结身份

交付目录：`/tmp/visible-larger-twenty-eight-source/`。每个 `.py.diff`
是相对原26同类源的完整差异；原四源没有改写。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_eight_query_domain_operator.py` | 33705 | `25767045b9a26764bfdb89881832ec7da01de1ac86ebc491402c7b9801175cd0` |
| `geometry_20261114_twenty_eight_query_condensed_warm.py` | 46021 | `990029102808ede1134bd9e6a163b6da84ae0d9189857f49af216ba64bfa188c` |
| `geometry_20261114_twenty_eight_query_condensed_response.py` | 2625 | `3a3d5f2888b4d826c69e2949ae9ec5ef896c54cb04f9b2283a71051221d7c5d9` |
| `geometry_20261114_twenty_eight_query_collocation_observer_warm.py` | 16736 | `fc5a3e4b35557a7056d96cd7ade6756b861f3667e44aea83d51e4f5cd59c7dfc` |

domain 的实现来源锁原26domain
`b5b72fde97ece27c034a5f1ae3c81f0c0288b4092050f63e96296f764e7068c8`；
warm 的直接父实现锁原26warm
`b9954eb5caffca7e3e001e66b07b0628a8275a22139ca3000cf527e258023197`。
新 warm 递归继承父 `FROZEN` 和 `SOURCE_NAMES`，而不是把原26模块的
query常量改写后称为同源。实际89 producer 的62个数学源已经逐字核；
新源码集合的构造在此基础上增加28domain和28warm，共64项。FD和
只读执行observer有自己的来源账，不覆盖历史 `resume_producer`。
64是源集合的静态计数，不是已发生的新运行回执。

原完整角域基础实现保持
`af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7`；
R270 condensation库保持
`84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`；
local-QP保持
`ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173`。

新 optimizer schema 为
`exact-constraint-twenty-eight-query-condensed-complete-H-warm-v1`；
新 B schema 为
`captured-twenty-eight-query-original-RMS-and-collocation-midpoint-domain-v1`。

## 3. 实际整数索引、端点捕获和完整列布局

```text
LEFT = (465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,487)
MID  = (473,475,477,479,480,481,482,484,485,487)
```

先18个 LEFT，后10个 MID；每组保原2048个物理角的全部行。
仅为捕获去重，typed query 行不去重：同一interval的LEFT和MID分别保留。
`CAPTURE_INTERVALS` 取全部query interval的集合；`QUERY_ENDPOINT_NODES`
取每个cell的左右端点并集；`LOCAL_LAYOUT_NODES` 直接等于这个集合。
这次不再复制旧的 `range(465,487)` 或7439维标签。

| 对象 | 原26 | 新28按完整索引公式 |
|---|---:|---:|
| LEFT / MID组数 | 17 / 9 | 18 / 10 |
| B行数 | 53248 | 57344 |
| 唯一捕获cell | 17 | 18，新增487 |
| 查询端点 | 465至486，共22 | 465至488，共24，新增487/488 |
| 完整B/H局部物理列+p | `22×338+3=7439` | `24×338+3=8115` |
| 显式zero-layout列 | 空 | 空 |
| 原完整未知量 | 236036 | 236036 |

原精确chart中，物理节点 j 的列为半开区间
`[(j-1)*338, j*338)`。新增节点的真实整数列如下：

| 节点 | 原完整chart半开列区间 | 列数 |
|---|---|---:|
| 487 | `[164268,164606)` | 338 |
| 488 | `[164606,164944)` | 338 |

新增676个物理列；global p仍是原完整列 `[236033,236036)`。
原109个free-core列及全部外部变量仍在完整236036维模型内，未因局部
B列布局变化而删掉。原完整状态仍699节点、每节点453状态分量。

新 LEFT487 是 query17、B行 `[34816,36864)`；原9个 MID 的组号
整体后移一位成为18至26，顺序不变；新 MID487 是query27、B行
`[55296,57344)`。这些是0起始整数索引。历史26输出按原行序解释，
不能把其query17直接当成新query17。

运行时仍从全部真实block拼出完整global列并集，与声明布局逐项比较。
description/export保实际列并集身份和实际维度。这里的8115等是明确
配置的整数推论，尚未生成的新B数值和SHA不预先声称已核。

全部新的端点487/488 J/P来自同一次原完整A/J构造的捕获器；不是
重新单独计算一个省略控制项的端点Jacobian。原节点factor缓存按实际
source身份导出。此次唯一完整模型和原调用次数保持。

## 4. LEFT487与MID487的状态及完整变分确实不同

令当前原cell左右站点为 $s_L,s_R$，$h=s_R-s_L$；原一次evaluate
返回完整 $Y_L,Y_R,f_L,f_R$。LEFT487使用原左Gauss分数
$\tau=0.17267316464601146$，站点仍由原浮点表达式
`float(x[j]+LEFT_FRACTION*h[j])` 形成。状态通过原
`CubicHermiteSpline(x[j:j+2], y[j:j+2], f[j:j+2], axis=0)(station)`
取值。既有标准Hermite形式是

$$
Y_\tau=H_{00}(\tau)Y_L+hH_{10}(\tau)f_L
       +H_{01}(\tau)Y_R+hH_{11}(\tau)f_R.
$$

本次源码没有用手写多项式替换这个原spline浮点实现。其完整导数仍由
冻结LEFT组件按同一原station、原spline和捕获的 J/P 组装，包含两端
全部物理分量及global-p链。原完整三控制标量的直接查询项也保留。

MID487则直接读取原evaluate的 `state.middle[487]` 和
`problem.mid[487]`，不通过LEFT站点或另建spline替代。原完整中点定义为

$$
Y_m=\frac12(Y_L+Y_R)-\frac h8(f_R-f_L),
\qquad
\delta f_i=J_i\delta Y_i+P_i\delta p.
$$

若当前有限角margin对查询状态的完整梯度为 $\Gamma$、查询处直接
标量控制贡献为 $\Pi$，原 MID 块保持

$$
B_L=\tfrac12\Gamma+\tfrac h8\Gamma J_L,
\qquad B_R=\tfrac12\Gamma-\tfrac h8\Gamma J_R,
$$

$$
B_p=\tfrac h8(\Gamma P_L-\Gamma P_R)+\Pi.
$$

原列尺度只除一次。全部338物理分量、3个global控制及通用入口/core
链按原源码保留。正向和转置用同一份完整rows/global-columns，
共享节点和global-p采用原scatter-add；新增query不删模态或链条。

复杂方向检查继续对 MID 直接形成原
`.5*(augmentedL+augmentedR)-h*(actual_rhsR-actual_rhsL)/8`，
LEFT仍走原spline；保原完整complex RHS、相同方向、相同实现阈值。
28个有限物理角网格没有被说成连续角域/全几何证明。

## 5. C按原支持公式新算，H按全部新局部列新算

这次扩大的是完整B及完整H局部未知量，不能把旧7439矩阵、旧C方向
或旧H条件恢复拷过来。入口仍在实际89新场生成一个原完整模型，
用原固定W、原A、$b$、原列尺度和原 $g=A^Tb$。

原C实现 `geometry_20261114_fixed_support_halfspaces.py` 的
`FIXED_PHYSICAL_NODES=range(471,483)`，`fixed_support_indices`按
原globalchart索引选择12个物理节点和p3。因此在**不改这个原公式**的
前提下，C允许修正的维度仍是 $12\cdot338+3=4059$；这不是强令新
完整B也保持4059，更不是复用原C数值。入口元数据用支持集合长度
重新给出维度，并从本次唯一原投影返回值记录真实
`full_compiled_B_local_dimension`、`local_dimension`、`constraint_rows`
及 `correction_support`，不把旧常数冒成本次输出。

原C目标与有效offset继续是

$$
\min\ \tfrac12\|C_{S_C}(z_{S_C}-z_{0,S_C})\|^2,
\qquad B_{S_C}z_{S_C}\ge -c-B_{\overline{S_C}}z_{0,\overline{S_C}}.
$$

新完整B在原C支持外的物理节点为
`465,466,467,468,469,470,483,484,485,486,487,488`。
`fixed_support_projection`每次对完整当前B实际计算原外列action；
新487/488的贡献进入offset，不能删掉、置零或仅检查局部行。
原raw fallback、全向量径向修复和same-model线段backup均保持。
这些全向量操作之后不声称外部方向仍等于raw LSMR。

完整H候选继续最小化原阻尼模型

$$
f(z)=\tfrac12\|b+Az\|_2^2+\tfrac12\lambda^2\|z\|_2^2,
\qquad \lambda=270,
$$

并对全部28组原margin线性约束使用同一 $Bz+c\ge0$。
R270仿射消元的局部索引参数仍传入本次 `domain.local_indices`，
现在覆盖8115列；全部其他节点、free-core和pure-global行按原完整
QR/仿射公式消去并在最后一次完整恢复中回到原坐标。原C的4059
支持绝不限制这一步。原父模型的A/B/H或factor没有复用为本模型。

H候选与C候选仍经过同一个原全模型选择器，比较同一 $f$。
实际所选完整向量继续读回原A/AT/B/BT、gdot、全部新行slack、
原后验报告和真正非线性试步。浮点R267后验不升级为严格证书或
新BVP门；阻尼项不计入实际非线性merit。

`main.project`唯一新增语句只在**原一次投影返回之后**复制已有报告
和列身份至 `condensed_QP_entry.actual_current_B_C_layout`；原调用
参数、顺序和返回tuple原样保留，没有新增projection、J、RHS或trial。

## 6. 实际89父件、历史producer和原四输入

第一父目录必须是
`notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/`。
实际原科学run/source/job为
`43671882961 / 032c513ab5db8aff98a6efca2070375418846098 / 132683564697`。

| 父件 | 字节数 | SHA256 |
|---|---:|---|
| `warm-001.json.gz` | 4902436 | `8985f7a5f146f0e98af04d5b1fc3d86648c7e6007403d9be54b1ed8ca4143fc9` |
| 原decoded `driver-status.json` | 3122352 | `c78528682d239d941ccc1391df004c8da3b51d60b6315c6d30334828d0204540` |
| 公开 `driver-status.json.gz` | 359700 | `c784987c5c45a35b43f9b805618c63b1ccbecb083dc676b0ae06e1233322499b` |

第一父schema是26。新源码硬锁真实warm和decoded status；原validator
继续核完整field/mesh/profile/constant core+p与producer。每一层历史
`resume_producer`保原字典，不把旧86/84场改标签为89。之后只有真正
生成的own28父件才能按既有own-schema契约继续，不预填未来SHA。

工作流同时支持原JSON或原gzip别名。gzip本身也核上表字节数/SHA；
若两别名同时存在，解码原JSON必须逐字相同。写入 `parent89/` 的是
原warm压缩字节和原decoded status字节，没有重新序列化。

| 原问题输入 | SHA256 |
|---|---|
| accepted96原场 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| 完整M112 prepared | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 真实zero-H T112完整J锚 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| T112配置 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

原参数化标量profile和g定义、p和core常量状态的完整原约束不变；
没有引入共享背景替代g，也不把本warm当成已完成native闭场。

## 7. Actions-only调用与原预算

以下是原工作流变量下的真实CLI模板，未在本地执行：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_eight_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT89/warm-001.json.gz" \
  --expected-resume-sha 8985f7a5f146f0e98af04d5b1fc3d86648c7e6007403d9be54b1ed8ca4143fc9 \
  --parent-status "$VISIBLE_PARENT89/driver-status.json" \
  --expected-parent-status-sha c78528682d239d941ccc1391df004c8da3b51d60b6315c6d30334828d0204540 \
  --out "$VISIBLE_OUT/twenty-eight-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
```

获得真正新warm后，原status/SHA确定 `$VISIBLE_CONDENSED_WARM`，再运行：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_eight_query_condensed_response.py" \
  --accepted "$VISIBLE_ACCEPTED" --prepared "$VISIBLE_CONDENSED_WARM" \
  --tail-anchor "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
```

原所有699节点、698中点、左右完整RMS族、uniform-phi rho、完整
边界、固定W merit、17档回溯和实现域条件继续原样。原FD全部方向、
步长、Richardson及 `5e-5` 门保持；它使用原真实zero-H J的affine图，
没有在新warm H处求真实native尾，也不能把旧FD pass复用为本次结果。

job仍80分钟，warm step35分钟，FD step25分钟。全部算法预算为原
1200秒、候选600秒、试探预留90秒、恢复预留30秒、512 working rows、
200 dual sweeps、200 LSMR和200 C projection sweeps。扩大支持会改变
实际计算成本；本稿不承诺相同耗时、内存或候选完成。原预算失败记录
及原C fallback范围保持，没有为多两query提高预算或降低验收要求。

## 8. 完整输出与观察范围

`twenty-eight-condensed-warm/`保存新status/warm、全model/trials、
全部B/Gamma/Pi、全部global/local索引、10个原mid输入、全部实际
endpoint J/P、condensation/QP完整数组与历史、原same-f比较和原
midpoint/collocation observers。每个query和实际试探readout都带
`kind`、interval与自己的fraction，不能只按interval把两个487合并。

新增metadata键为 `twenty_eight_query_projection_entry`，FD来源键为
`twenty_eight_query_condensed_QP_response_entry`。新
`actual_current_B_C_layout`记录原一次投影返回的实际支持；全H的
真实local indices和完整恢复身份仍由原condensation报告独立保存。

只读observer对原evaluate、weights各执行一次后读取既有数组。
observer异常只记诊断，不替换原有限标志、原向量或科学决策。
所有大数组保完整artifact；compact summary不能冒充完整数组认证。
新warm、FD或workflow success均不等于 fullDN/native/原README完成。

## 9. 唯一request94工作流草稿

交付 `/tmp/visible-larger-request94/`，沿用已存在
`.github/workflows/visible-larger-public-condensed-qp.yml`及唯一push触发
`topics/visible-flex-larger-amplitude/computations/public-condensed-qp-request.json`。
请求只含 `condensedqp`，原单lane、原concurrency、`cancel-in-progress:false`
都不变。没有第二个workflow/重复请求，root统一审读、写库和派发。

| 草稿 | 字节数 | SHA256 |
|---|---:|---|
| `visible-larger-public-condensed-qp.yml` | 26879 | `e25ab2027d1a9f9107778a0969cabc8c07ce5239af9e7429a3f1631005c4de4d` |
| `public-condensed-qp-request.json` | 25395 | `480f8d887402eb2c3b818c8fe672831019755f189d373f9ea09a6b3c4ab3af10` |
| `request94-static-check.json` | 15960 | `606dabceccbc3326b43c2d77f30fc29ea93fe52bc5317c5c33eca5b93727745e` |

全部59个既有request pins逐字保留，增加4个新源，共63。这个工作流
闭包计数与数学producer的64项是不同集合，不能混称。publisher仍是
`22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`。
原public78恢复、accepted/prepared/zero锚来源、固定SHA的checkout/
setup-python/upload-artifact、Python3.12.14、NumPy2.3.5、SciPy1.17.0、
单线程BLAS和两个科学step无token保持。always上传与出版失败保全
路径原样，不把transport结果当科学接受。

## 10. 已完成的本地静态核，不作为新科学门

`twenty-eight-source-static-check.json`：8476 B，
`ef25196760533cf545849857afebcbe7497e179ba37150c040fe9d148d3b8248`。

已完成四源AST/compile-only、完整相对26diff、实际89父件原SHA/JSON、
父62数学源逐文件SHA与有限整数索引核。原LEFT/MID状态函数、完整
query构造J/P链、evidence/choose/完整非线性observer的数学AST保持；
构造器只允许来源/范围标签差。原FD全文只替换新名字；observer全文
只替换新名字和新entry pin。C包装把新增只读metadata去除后，其唯一
原调用和返回tuple与原26的AST完全相同。

request静态核通过63源SHA/AST、11个shell块的 `bash -n`、6个inline
Python AST。原安装/source恢复/输入恢复/上传/出版步骤相等，原所有
数值CLI参数相等；父件恢复逻辑只替换显式原run/schema/bytes/SHA，
逆替换后正文相同。没有导入科研模块、构造数值对象、执行RHS/J/
ODE/求解或本地新范数。实际新结果和全部原门仍只由公开Actions决定。
