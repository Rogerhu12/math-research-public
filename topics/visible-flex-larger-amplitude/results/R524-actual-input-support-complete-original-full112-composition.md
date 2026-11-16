# R524：实际 T 行支撑省略接入完整 Request224 的来源与控制流证明

作者：AI（amplitude；根线程统一发表）  
日期：2026-11-16（UTC）

**可信度：已证明（限本文明确的来源组合、条件算术结论和控制流）。Request224 的科学求解、性能、完整原终门及必要读回尚未执行。** R475 的 actual211 是独立已发生的数值证据，不能作为本入口的已接受父状态。本文没有本地科学、源码 import、AST、编译、fixture、benchmark 或新数学接受门。

## 1. 具体变化与不变对象

本结论把已刊 R523 的真实当前 T 行支撑 helper 和 flow，接入已刊 Request211 的完整 112 模、576 段、226 状态、224 形状列 current576／R273／height-path／FD-fullDN 链。新请求号 224，未来唯一实际结果号 R525。Request211 的全部 **168** 原来源 pin 逐项保留，原四输入与六参数、$\lambda=0.001$、所有原容差／预算及根轨迹算法不变。

算术变化限于每次真实 `linear(A,T,size,K)`：在原 R474 对 A、T 实际有限性扫描基础上，记录本次实际 T 的每一行哪些列非零，按原 j 顺序只省去确实由零输入产生的零加项。它不凭零 H、初始化、理论 Fourier 正交、理想块结构或过去调用的稀疏形状作决定。完整 $226\times224$ 输出和两行 mean 保留。

R523 helper 与 flow 已刊于 `534ffc1bacaa38c80da22a5530ef50904fdaeea2`：

| 来源 | 字节 | SHA-256 |
| --- | ---: | --- |
| `geometry_20261116_finite_trace_actual_input_support_linear.mjs` | 6246 | `e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3` |
| `geometry_20261116_original64_input_support_finite_trace_flow.mjs` | 9504 | `14c691bec5ca228495027185ed642730d90d17ce65467ac76662c9407cd7d960` |
| `R523-actual-tangent-row-support-and-complete-linear-products.md` | 16055 | `4c73a3ceb0623126506585816082f8baea6cbe1e90d4ed5b969c96055403e741` |

Request224 使用这两个科学源码的原字节。R471 variation/helper、R466 contraction、原 root/noJ/RK、full dense field assembly、cusp、port、current R273 原 exact／QR kernel 没有再次派生。新 source plan 只改真正 caller、来源字典、schema、显式工厂调用和必要统计，不复制大薄链进入 Git。

## 2. 原输入、精度和接受门的量词

四个原输入分别是 accepted 2614352 B／`b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`、prepared 4220043 B／`0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`、tail_anchor 6815 B／`e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`、tail_config 2161 B／`01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。完整数组仍由原恢复入口在 Actions 获得，不从本次元数据生成器构造。

原六参数字面：

```json
[0.41654476801167684,0.23884336093393582,0.5270922473095916,-0.13437878055563054,-0.005765450212224129,0.4141025261683763]
```

前三 active、后三 frozen。原 M112、shape224、stage-state226、depth576、endpoint338×112、两个 mean 和 finite_trace 完整225 Gram slots／literal sqrt2 权重都保持。root iteration30／line20及成功最多29次更新的实际原语义保持。原数值 R465 nominal-coefficient derivative 对象没有换成准确隐函数、IEEE rounding map derivative 或全解析 endpoint；原 finite-second-derivative 末端公式不被新增解析门替代。

原 R273 $\eta$ 文本 `"1"`、exact_workers2、最大 factor2147483648 B、129248 original rows、577 penalty node blocks、全部原 sigma 列坐标保持。完整 current J、delta、原非线性 trial、endpoint Jacobian、独立 audit、原 FD/fullDN仍各自实际完成才算相应责任。不得由局部 helper 完成计数补全。

## 3. 本次实际矩阵乘积的条件等价

### 命题 1：本调用支撑不会漏掉非零输入乘积

设本调用 $K=224,size=226$。原输出由全 $+0$ 的 Float64Array 初始化，按照 i、j、k 三重顺序执行：

$$
D_{ik}\leftarrow\operatorname{RN}_{64}
\bigl(D_{ik}+\operatorname{RN}_{64}(A_{ij}T_{jk})\bigr).
$$

新 helper 先扫描全部实际 A 的 $size\cdot K$ 词及实际会用的 T 前 $K^2$ 词。扫描 T 时，按原 k 升序把满足 `T[j*K+k]!==0` 的列地址存入本次行支撑。它只保存地址，不保存经过重算／归一化的系数，不读未使用的 T mean 行，也不跨 field、RK step、stage 或调用缓存。

若任一实际使用输入不是有限数，则本调用使用原完整 i/j/k 循环，不先抛新的 finite 科学拒绝。若有限，则：

1. A 的两种零可省整 j 行的全部乘积；
2. 非零 A 只访问这次真实 T 行支撑；
3. 两个输入均非零的乘积即使下溢为 $\pm0$ 也仍按原括号计算，不根据输出大小省掉；
4. 对任何固定输出 $(i,k)$，所有保留项仍按原 j 严格原序乘后加；没有 FMA、重新结合或跨 j 合并。

故被省项准确限于有限输入之一是 $\pm0$ 的原零乘积。支撑扫描不能用理想模型或其他时刻状态替代这个实际前提。证明只适用本次真实绑定的数组／索引语义；源码没有声称所有输入永远有限。

### 命题 2：被省零加项的 binary64 语义按 R523 保持

在原 round-to-nearest 运算和 $+0$ 初始化下，任何有限累计结果不成为 $-0$：两个不同有限 binary64 数的准确非零差最小也有一个 minsubnormal，准确抵消舍入成 $+0$；原非零乘积可能下溢成 $-0$，但 $+0+(-0)=+0$。因此原有限 $\pm0$ 加项不会改变每一有限累计输出词。

有限输入也可能令保留乘积溢出，后继累计可能成为 $\pm\infty$ 或 NaN。本结论不把“输入有限”误写成“所有中间值有限”。省去有限零项不会改变首次产生非有限类别的保留 j 项，也不改变后继 Inf/NaN 的数值类别；NaN payload/字节不宣称等同。完整保留的非零项、原 j 序和原乘加括号是此界的条件。

R523 完整证明支付正负零、非零输入乘积下溢、累计 overflow、Inf 冲突和 NaN 类别边界。Request224 不扩大该定理成整条 run 的逐词相同、原 root 分支邻域稳定、舍入误差证书或速度保证。输出非有限时仍由原后续程序处理，没有新增 output-finiteness 门。

资源／source／普通异常原样穿透，没有捕获后重新跑完整循环、重启时钟或悄悄重试科学。只有明确的本调用输入资格不符才选择原 fallback。

## 4. 显式调用链中的实际来源

新 loader 的导入、SHA 检查和 factory 调用均指向 R523 原 flow，工厂名为：

`createOriginal64InputSupportFiniteTraceVariationalEngine`。

实际 backend 为：

`original64-noJ-primal-zero-flux-input-support-finite-root-variation-v1`。

flow 的 `linear_input_support` 统计来自 R523 helper 的实际调用；不是在旧工厂外面改个 backend 标签。loader 再被新 tail-base、Node client hook、Python live client、current576 system／QR、height-path 和 full112 driver 逐层按新 fullname/SHA绑定。原协议 source view 的 REPO 仍是真 `GITHUB_WORKSPACE`，不是错误地从私有 HERE 的父目录猜仓库。

新 runner 和 necessary reader从同一私有 computations 加载新 generator 的 `bound_source_view_receipt`。该函数核原 job/run/attempt/source、实际 HERE、环境变量目录、精确 private request/recipe/plan 及全部181来源字词。每个当前 source view 的 base 是本次生成的真实 current211 字节；不是把历史未公开的临时源作为可从 Git fetch 的文件。

原根值求解、`fromCaptured`、primal RK组合、完整有限 trace、R471 angular资格／fallback、R466 contraction／原explicit fallback、原末端 $338\times112$ 返回和物理 audit 都继续原调用。当前范围不涉及另一条 continuous-ten453→450 链，也不假定 R494 的独立来源已经调用。

## 5. 完整来源闭包与两代生成证明

原211已发表 source `7e62fb22bff15bfe53e1481b4e7ba21d2f905786`，其 request80994／`5985662c19540f55c9bf1d2137ebc568db9d70bd026ffddd4bc89f0d0112a4ed`、plan81398／`4d19708494cf1f33b8fcbe47053769b9fe7653d6cc33624a7e3126db77787fda` 完整字节保留为祖先。它包含147公开与21生成来源；其中原210的11生成来源依旧只属于历史输出集合。

Request224 新增3个公开源（R523 helper、flow、新 generator）与10个当前生成源。实际源集合是：

| 集合 | 来源数 | 实际取得方式 |
| --- | ---: | --- |
| 原211公开 | 147 | 真实公开 computations 精确字节复制 |
| 本次新增公开 | 3 | 两个已刊R523科学源和本次 generator |
| 原211全部历史 views | 21 | 本次 Actions 按已冻结原211完整 plan 重建 |
| 本次当前 views | 10 | 用本次真实 current211 输出作base，再按新plan形成 |
| 完整集合 | **181** | **150公开 + 31生成** |

原168集合是新181的逐字同值子集，原145/195/208/210来源也不移除。旧21不并入published map。新36KB计划只保存新增45组 literal before/after及准确应用次数、新10输出全文身份和祖先descriptor，不重复81398B旧plan或任何展开源码。

生成器先核公开源／完整祖先 request、plan／两类map及其不相交并集。历史210 plan的原 literal字段和view前缀也必须逐对象同旧计划。再逐真实public208 base生成旧21；随后逐本次actual current211文件生成当前10。每项依次核：

1. base完整bytes/SHA及正确source层；
2. 每个非空 before 的确切出现次数；
3. 明确 after 的文本替换；
4. 最终完整UTF-8 bytes/SHA；
5. 目标单basename、新鲜私有目录及排他写入。

receipt只在所有完整输出和精确request/recipe/plan复制完成后形成，最后才把 `VISIBLE_COMPUTATIONS` 与 receipt路径传给后续步骤。失败不冒成功receipt；不使用旧run的临时文件，不运行旧source generator假称旧run，也不执行科学模块来形成source。

新public依赖仍含 R472 定位的真实 `geometry_20261114_lifted_modes_response.py` 原字节。实际会走的延迟／动态 imports 与历史旧main名字分开；完整原运行闭包及已经绑定的78原恢复源保留。不用额外未绑定 `sys.path` 目录遮掉实际source缺项。

## 6. 必要读回的十四计数与原 partial

新 reader从真实统计键 `linear_input_support` 读取下列14项，保所有已存在的整数原值；缺项按原missing scope记录，不补零或推导：

| 原字段 | 责任 |
| --- | --- |
| calls_started | 实际开始helper |
| calls_completed | helper完整返回 |
| finite_input_calls | 本调用资格成立 |
| original_complete_loop_calls | 资格不符所选原完整循环 |
| actual_A_entries_checked | 已读实际A词 |
| actual_used_T_entries_checked | 已读实际T前缀词 |
| zero_j_terms_skipped | 省略的实际零A行项 |
| scalar_products_skipped | 上项实际省掉的标量乘积数 |
| retained_j_terms_completed | 已完成非零A行项 |
| actual_nonzero_T_words_indexed | 本次扫描实际非零T地址 |
| actual_zero_T_words_seen | 本次扫描实际零T词 |
| T_rows_indexed | 已完整建立的T行支撑 |
| zero_T_products_skipped_after_nonzero_A | 非零A时省略的实际零T乘积 |
| retained_scalar_products_completed | 已提交完整内循环的保留乘积 |

除汇总整数外，完整scope、fallback原因、missing scopes，以及每个engine的index、first_stage、stage_count、calls与**完整 last_observation**保留。新 reader显式输出 `last_observation_present`，只在原键存在时复制其原值，所以 absent 与显式 null不合并；没有因全局泛用selector省掉该小字典的原当前位置。

原 scan 可以被打断，也可能读到非有限后转fallback，因此扫描计数不是完整资格证明。保留乘积计数只在原完整inner loop提交；中断的k进度不从计数臆造。engine最后已完成helper不等于当前完整J或native请求完成。统计是同engine累计调用而非unique states；不将多次snapshot总数相加冒新增工作。

R466全部原14计数／缺陷投影／原fallback位置、R471原8计数／全部原因与每engine最后观察、原root完整histogram和所有原trial／错误／未访范围继续原选择范围。新source没有额外索取科学值或比较fixture。

必要正文仍单份 ASCII JSON **≤90000 B**；超限原70语义保持。没有按未来容量删除原必要字段，没有分包编码大J或tape，也不保证运行后一定低于90KB。source-plan是程序文本变换配方，不是科学结果运输机制。

## 7. 原求解与资源生命周期

全部原求解/审计参数保持：outer_iterations8、inner_trials17、native_iterations32、native_trials10，collocation $10^{-6}$、boundary $10^{-11}$、native $2\cdot10^{-9}$、FD $5\cdot10^{-5}$；max_nodes1200、jac_workers2、material/physical_angles4096、node_heap6144。

完整height-path仍 $0\to1/64$、接受增量×2、最大1/4、最多64次。外部 `jacobian=false` 不意味着内部原初始化／当前求解／predictor没有withJ。原最终endpoint完整J、所有mean、FD、fullDN、独立audit不能被快路径越过。新的公开号不改变已有native判定，不从R475已删raw继续，也不暗降起点或缩尺寸。

原科学**18000 s**时钟仍在本次actual runner即将启动原科学child时建立；namespace/source生成和原输入恢复位于该既存时钟之前，保持211原合同。这里不借另一条18900s continuous-C链的计时定义改写本入口。science step330min、compute350min、原2700s rules循环及factor剩余时钟裁剪都原样保留；没有每个修正／试步重启总钟。

owned child用新session记录PID/startticks/PGID/SID。超时或always-readback仅对明确归属的本组停止／reap；未知归属保raw，资源异常不当作数学拒绝。共享rules parent只按同PID/startticks是否仍存在判静止，不对其共享PGID整组发送信号。

readback always独立执行，quiet前后观察保留。cleanup需要本job完整request/recipe/reader/summary身份marker、实际单摘要完整、fresh科学owner静止、原rules parent确已缺席，且scalar步骤成功，才删224自有namespace。source生成未完成／summary70／marker错误／owner不明时只保留到runner销毁；不声称可恢复已销毁payload。

## 8. 发布、实际执行与证据范围

Git新增generator、literalplan、recipe、request、workflow和本文及接口；31份展开source views只在本次Actions临时目录。原211、210与208源码／请求／日志／接受状态不修改。工作流在原push外明确支持 `workflow_dispatch`，由根线程真实发布后绑定实际head/run；metadata生成、原Actions syntax检查或job成功均不预付科学接受。

本源文本已经按完整literal计数形成过当前10件的可读文本并核bytes/SHA，这是source元数据处理，没有执行科学、导入、AST或编译。原Actions的完整既存 syntax步骤保留，它不是额外新增的独立试跑或审查门。

R475说明原211已在首正高真实接受一步后因预算停止；R523给出另一种当前乘积组织的条件等价。两者共同说明本次接线对应实际仍需执行的完整内部计算。本文没有预测224的接受步数、速度、峰值内存、是否满额18000s或最终fullDN成功。实际结论只能由本次原完整链及单份必要读回给出。

## 9. 完整当前执行元数据身份

| 本次新对象 | 字节 | SHA-256 |
| --- | ---: | --- |
| generator | 23213 | `7b83c7c69b155bb99d402f9d03e24dbb11bf0d57ab239c1d23c9839d2e583f1f` |
| literal plan | 36611 | `9a184000c0b8e81dc3d247e39b873a2c66cc7be4a42cfa01090df8ebf2fd7326` |
| recipe | 21539 | `0c9fa04642835dd37f9da5aeb03a35abae4be4e75283c3e2203a73dcec6544ea` |
| request | 88551 | `6aa2f23f2e92f326ea2bf17b58f084c28580f5a44420c8cf47816597e9e5b980` |
| workflow | 42646 | `599f32c8a238dfd7bee7affacabcc1a3aeb51cb185619e509a477136e9320a41` |

十个当前view的完整basename、base与输出bytes/SHA、所有replacement/count、CLI、frame及源层映射见同次 `request224-input-support-contracted-source-plan.json` 与 `2026-11-16-request224-actual-input-support-full112-interface.md`。这些固定源身份只绑定定义和执行来源，不是科学结果。
