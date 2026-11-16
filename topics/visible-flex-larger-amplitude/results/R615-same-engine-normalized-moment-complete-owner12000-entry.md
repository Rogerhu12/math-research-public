# R615：原 250 完整调用链实际使用同 engine 六 moment 归一化词，并保留完整必要读回

作者：OpenAI ChatGPT（AI），2026-11-16。

**可信度：已证明（限本文绑定来源、表达式及控制流条件命题）；request 253 的实际 source preparation、当前 H 的原 128 owner、完整 projected64 模型、FD、full-DN 与末次审计尚未执行。** 本文是独立执行源码与完整接口结论，实际 253 终态留给 R614；不得用本证明预填其返回、时间、数值、接受或必要读回是否在 90,000 B 内。

## 1. 要完成的具体调用及继承边界

[R611](R611-same-engine-six-moment-original-normalization-reuse.md) 已给出原 Fourier-product 局部 Jacobian 六组 moment 中，同一实际 engine 的三角表逐元素原除法词可复用的条件证明和独立源码。R611 本身没有改动正在运行的完整求解器。本结论将它接到 [R603 / request 250](R603-current-DN-input-support-complete-owner12000-entry.md) 的真实 worker → engine → current-call → R532 模型消费者，再把实际累计统计和完整来源选入原必要 reader。原 R602 / R523 的完整 $A T$ 算法继续使用同一实际输入；没有为取得新统计再次求 J。

唯一直接父合同是正式 250，发布头为 `25265e7eaca1b00a879311032a8520546516416c`。原 248 / R594 的 owner 上限 12,000 s 已经由 250 继承，原总科学钟为 19,200 s。本入口不沿旧 6,000 s 参数重新选预算，不沿另一个实验的来源断口组合。R611 的正式发布头为 `24d17b9332e535e9be33684b9dbe84bac1542b5e`；其执行源 9,963 B / `54a76c39befca05381f10b744c5986ac761dffb8db6d3ebe4fa0c48fa9f5d6d7` 原字消费。

R611 正式证明 19,582 B / `cd4b83229b9df410790430d540dd83b9daa1146d0c1035d375ac9c9b4dae9f81`，正式接口 13,621 B / `7e9c1ee5c130cf80bc7fe7389d84b049de8918c77d8924e3364019040f4b71ff`。该文明确八个 JavaScript Number 计数只能在 safe-integer 范围解释为准确次数；没有 BigInt 或源内计数溢出检测。本入口保留原数值，再加逐字段 `Number.isSafeInteger` 元数据，不能通过钳位、改类型或拒绝科学调用来消去此边界。

原 250 的实际数值返回截至本稿没有被本入口消费。父合同提供源码、固定输入与参数定义；250 的运行状态不能成为 253 的数值结果。本结论不更改 250 的 workflow、请求、已生成源或在途状态。

### 1.1 公开执行文件

下表给出全部新公开执行件。路径以仓库根为基准；workflow 位于根 `.github`。展开的十个 view 只在公开 Actions 的真实 computations 目录产生，不再次放入主树。

| 角色 | 仓库路径 | UTF-8 bytes | SHA-256 |
|---|---|---:|---|
| flow | `topics/visible-flex-larger-amplitude/computations/geometry_20261116_normalized_six_moment_fourier_product_flow.mjs` | 2814 | `b768c6bf377e1a7d3ebe03692948ac0f42ed3d6cdc50ff67a16662fa45043453` |
| factory | `topics/visible-flex-larger-amplitude/computations/geometry_20261116_normalized_six_moment_root_split_factory.mjs` | 2415 | `1f3f99b01b59565e6713cc894082e0579f92558e2f7cc71d65a8cb0ce08ba386` |
| generator | `topics/visible-flex-larger-amplitude/computations/root_20261116_live128_normalized_moment_source_views.py` | 29985 | `3329580248e7a19121d4e1fe05e65334ba667b46d48f0272aed17725845521b7` |
| plan | `topics/visible-flex-larger-amplitude/notes/r615-current-DN-normalized-moment-complete-source-plan.json` | 41859 | `ded97e0532dcceaab203ee5cac79353f1580586517e0877164978d419851206f` |
| outer | `topics/visible-flex-larger-amplitude/computations/public-live128-normalized-six-moment-composition-request.json` | 14540 | `111eec1320495ca0f4fe0030edf5b290183ca1f650bd5b74fedf3b4711df754e` |
| workflow | `.github/workflows/visible-larger-live128-normalized-six-moment-full112.yml` | 26196 | `83dff5ccc282f2fc9f454894939fd27b73f182d7e3b0d4ac9ccb78f979ed8281` |

R611 已刊源不是重复新增文件。源码计划中的每个 before、after、严格次数、完整基线身份及输出全文 SHA 均明确保存；本表没有用摘要替代该可执行计划。

### 1.2 十个当前 view

| 角色 | 实际 basename | 全文 bytes | 全文 SHA-256 | literal 数 |
|---|---|---:|---|---:|
| current_factory | `geometry_20261116_current_DN_normalized_moment_input_support_flow.mjs` | 6625 | `f1f21641f3f7c2f36616d7f2a841ef8cab94251eaac3758ca221b0bba0bbb011` | 8 |
| system | `exact_20261116_live128_normalized_moment_current576_system.py` | 29117 | `231b181fe9bb357f8dd40054085aa885985b7dc3f8bd4daf9e49f5cda58d4fa6` | 2 |
| qr | `exact_20261116_live128_normalized_moment_current576_chain_qr.py` | 21848 | `b0c4bf366945b578f75d133cb427f8f4b6944e0abdfdbef75f2b0c2b9c148be5` | 2 |
| pipeline | `geometry_20261116_live128_normalized_moment_call_pipeline.py` | 43266 | `b35179c75351edc50d4aba725f6b754ea165ca8090acccfe4987e760c9a61ad0` | 4 |
| call | `geometry_20261116_live128_normalized_moment_current_call.mjs` | 51193 | `337b769cff9260dc2c7d2ddb40dd2ff0e0225ecf54ebab5a6c8cc3ca95a1283f` | 13 |
| worker | `geometry_20261116_live128_normalized_moment_worker.mjs` | 9025 | `08c8bab4c91f0038c55b6fa75f3a03a34ec0c54a16b89a157a5e947a0f8853df` | 3 |
| client | `geometry_20261116_live128_normalized_moment_tail_client.py` | 42721 | `64cb7979dc1874bca5175b950e2772efc56f27eb303294dff0c6e16fd3ddd538` | 8 |
| fulldn | `geometry_20261116_live128_normalized_moment_original_full_dn.py` | 49006 | `49bd45f7cc55ce62474bf6f41d7f82f48d4b2f1af1460c8ca1d8112ed4d0ace7` | 4 |
| runner | `geometry_20261116_live128_normalized_moment_owned_run.py` | 39362 | `74c6fe1694ecc7d02605e4fe5131e3a0a8c3462b4925760d08d62a53dabb75a1` | 11 |
| reader | `root_20261116_live128_normalized_moment_necessary.py` | 68247 | `94078d508648b97f2c3cd9d71f2c4381224ba12029d8eb091e0e757a933ae4f2` | 16 |

所有 `output` 都是实际新身份。没有给新文本套用旧 basename/SHA；旧 250 全部 466 对源名/SHA 原值保留。新增公共集合为 R611、两个小 constructor 源和本 generator，共 4 件；新增生成集合为上表 10 件。因此本次明确集合为：

$$
466+4+10=480,\qquad
366+4=370\ {\rm public},\qquad
100+10=110\ {\rm generated}.
$$

这是本次显式完整执行闭包的集合计数，不声称已经证明任意未来动态 import 的全宇宙闭包。实际生成端遍历每个声明路径及完整 SHA，保留每个旧 pair，再核集合大小与新文件无冲突。历史 generated 项仍由冻结祖先计划在同一次 job 中生成，不当作公共 Git 文件读取。

## 2. 实际源码选择与唯一一套局部 J

### 2.1 需要改动的三个构造接点

原 `78718-tail-fourier-root-split-engine.mjs` 的完整身份为 2,045 B / `a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372`。它原来静态导入原 root engine 和原 product-flow。新小 factory 保其整个 root/split/RHS/rk4/optional cusp 构造数学，只作明确来源选择：

1. 原 root engine 从实际 `VISIBLE_FLEX_SOURCE_TOPIC/scripts/78718-tail-fourier-root-momentum.mjs` 导入；
2. 原 product-flow 改为新公开 `geometry_20261116_normalized_six_moment_fourier_product_flow.mjs`；
3. 其余 split-flux 与 cusp 来源仍来自原 `VISIBLE_FLEX_SOURCE_ROOT` 下的真实原路径。

原 flow 是 2,400 B / `717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f`。新小 flow 将局部 J import 指向真实 R611，保存一次 `localJacobian=createFourierProductJacobianEngine(options,base)` 返回，再把其 `rhsWithJacobian`、`normalizedMomentStatistics`、`normalizedMomentSourceBinding`、`momentEvaluation` 透传。原积分表、RK4、原完整状态和 tangent 表达式均保留。

最外层当前 flow view 由 R602 的实际 5,625 B / `f37bee075251957649c9ee5dc25582fac5c17fc3d3b804219cb537abf35f24f0` 派生。它先调用上述实际新 factory；再用原 R602 的 `flowStateWithJacobian`，对每次真正得到的局部 J 和当前 tangent 调 `completeInputSupportLinear`。返回 `{...base,flowStateWithJacobian,...}` 保留 base 中的 R611 observer 对象，不重新调用局部 J 构造器。

故这个路径只构造一套实际 R611 cosine/sine 表。没有先创建一套旧局部 J、再为记录数据另建新 J；原 root engine 自有表、split engine 自有数据仍按原构造需要存在，本结论没有把这些不同职责混称为已移除的重复工作。

### 2.2 为什么两个小源码直接公开而不伪装成已恢复的基线

本 workflow 的 source preparation 在原 78 源恢复前。若这时要求从尚未恢复的 `scripts` 目录读取两份原 constructor 作为 view baseline，会改变真实可用路径，或让计划声称已读一个尚不存在的文件。

本实现把上述两份确有 import/observer 变化的小源作为真实公开文件。source preparation 可直接核它们的实际 bytes/SHA；等原恢复步骤真正完成、科学 factory 实际加载时，再核原 a47df、717ac、205b、cusp 与 root 文件。原恢复顺序不后移、不省略，也不伪造源收据。十个生成 view 的所有基线都是冻结父准备已实际生成/恢复在 computations 的完整文件。

### 2.3 容量 loader 的路径必须仍然真实命中

实际 loader 为 `exact_20261114_tail_capacity_loader.mjs`，4,499 B / `07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395`。其 `registerHooks.load` 依确切原路径选择并核原全文，不能只凭一个相似文件名推定会接管新的 constructor。

新 factory 的 root import 刻意使用同一真实原路径。原 root 文件是 13,809 B / `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88`，所以原 loader 在该文件上仍按原完整 SHA 与实际 `VISIBLE_FLEX_TAIL_MODE_CAPACITY` 施行既定容量解释。新 flow/factory/R611 文件不冒充 loader 的三个原文件。原原始源字节与 loader 返回的执行文本身份范围分开：前者由源恢复和完整文件身份绑定，后者仍归原 loader 的实际解释。

因此对于本请求的 M=112，不能以旧 root 源中默认上限说明本次必拒绝，也不能声称新的 import 绕过上限；它仍经过相同原路径的既定容量 loader。这里仅证明真实调用接点与来源，未执行 loader、未验证未来运行成功。

## 3. 六 moment 原除法词复用的条件证明

设同一实际 engine 构造时原代码生成的 binary64 表元素为 $C_{nk},S_{nk}$，实际 quadrature 为 $N$。原六 moment 内循环先取

$$
c_{nk}=\operatorname{RN}_{64}(C_{nk}/N),\qquad
s_{nk}=\operatorname{RN}_{64}(S_{nk}/N),
$$

再按原顺序执行：

`FPm[k]+=FP*s; CKm[k]+=CK*s; FTm[k]+=FT*c; CUm[k]+=CU*c; CPm[k]+=CP*c; bmM[k]+=bm*c;`

R611 先完成原 cosine 全表和原 sine 全表构造。原 `Math.cos`、`Math.sin` 调用的参数表达式、次数、表序、`Math.sqrt(2)`/`Math.sqrt(12)` 及频率表达式没有变化。资格分支先核实际 $N$ 为有限正整数，并扫描两张实际完整表是否有限；在扫描结束前不改任一元素。任何不合格只把 `normalized=false`，保两张原表，后续执行原 `/N` 内循环。

合格时在同两张 `Float64Array` 表内逐元素执行原 `cos[n][k]/N` 与 `sin[n][k]/N`，没有先求倒数，没有改为 reciprocal multiplication，没有把除法移到 moment 和之后，也没有调用 trig 正交关系。此处保存的是该原表达式实际返回的 binary64 值。之后局部 J 只读取保存值；因表不再修改，且 $N$ 属该 engine 固定构造参数，每次读取等于该处原除法词。

**命题 615.1。** 在相同实际 source、engine 参数、原表元素与原状态/profile/$x$ 下，两条调用都完成时，合格分支六 moment 的每个乘数词与原执行一致；每一乘法、每一 `+=` 的 $n,k$ 遍历、括号和顺序相同。由逐项相同与每次相同 binary64 运算归纳，六组离散 moment 在有限结果及 signed-zero 情形返回词相同，非有限按原相同算术分类理解而不声明 NaN payload；原右端、FL、FQ、单次 Cholesky 及全列回代/装配保持原表达式，故完整该局部调用继续按原算法得到输出。资格 false 时直接走原表除法，亦不新增数值接受条件。

此命题只换 R611 所指的 `c=cos/N, s=sin/N`。原 root 的 Gram 表达式如 `(bm*cos)/N` 不是同一浮点括号，没有被约成 `bm*(cos/N)`；没有把 root primal 与方向算法换成 R466 finite-trace，也没有改成精确实数 trig 积分。

有限表元素且 $N\ge1$ 时这一次除法不增加幅值，可含 signed zero、subnormal 或舍入为零。其结果按原表达式产生并由同类型表保存，保留该处 ±0；没有用数学符号“零”覆盖原词。后续 FP/FT/CK/CU/CP/bm 与状态相关的中间量仍可能非有限；本结论不把有限三角表提升为整个局部 J 有限。原 NaN/Inf 算术和异常路径仍在原完整调用中承担其责任。本证明不声称 NaN payload、外部 fenv 标志、异常时间或整次有截止运行的逐事件轨迹相同。

原 `solveMany` 仍先建立同一 $J\times J$ 下三角因子，再对全部 $K=2M$ 右端逐列前后代；没有逐方向重求 root。原 `base.rhs(...,false,rt)` 消费同次已得到的 root。已有共享不是本次新增收益。M=112 时输出仍为完整 $226\times224$，包含两条 mean 行；第二 mean 行若原算法由初始化保零，其原责任仍是原完整输出中的一行，不能从表优化中删掉。

表正常复用减少的是原局部 J 反复形成同一除法词的源级操作。新增资格扫描、构造时除法、读取与 metadata 自有成本；不假设 JavaScript 引擎原先没有优化它，不推出实际 wall time 比例。科学时钟包括实际 engine 构造、当前模型与所有求解；归一化完成得早晚可能改变给定资源内走到的前沿。所有未完成范围必须按实际保存状态报告。

## 4. 当前模型、完整 A T 与原接受门

### 4.1 原当前模型的真实消费者

新的 Python system 选择新 client 与 worker，QR 选择新 system，pipeline 选择新 QR。new worker 真正 import 第 2 节的当前 factory，并把该 constructor 交给原当前模型恢复/计算，而不是只把新文件加进一个未使用的 source map。current-call 的实际 tuple 同时包含旧 owner 和新的 client/call/worker 完整身份；原 R532 loader 会消费这个真实 tuple。

以下数学消费者逐字不变：

| 角色 | basename | bytes | SHA-256 |
|---|---|---:|---|
| owner | `geometry_20261116_live128_synthesis_product_projected_same_call_owner.py` | 26666 | `2af373696034e49f61e6dcc49707e668ed60d600b5a4f9dbf0d71d85cd24ad17` |
| model_library | `geometry_20261116_live128_same_dn_projected_stages.mjs` | 32316 | `2279a605df5ee41c5400c658018722fd52e6add40ee35ff38dbca1a31b2bb76a` |
| final_components | `geometry_20261116_live128_projected_model_final_components.py` | 38561 | `c4b3a5eb05fc4d4ae6767c2c08f75ea38a5a5538366fcd3264ff59cec17bb04e` |
| response_assembly | `geometry_20261116_live128_projected_model_response_assembly.py` | 33269 | `863790de6c0c2020d79150ac99134b2a8ee74592cc42669127ca7df296a0f21a` |

同一次真正当前 H 的 128 owner 和完整 replay 仍是值来源；原 R532 从该真实当前状态取得 projected64 的完整线性模型。这个 binary64 投影点不升格为接受的 native 状态，也不声称其完整矩阵就是原 128 owner 迭代的解析导数。原模型交付全部 576 个 cell、全部方向及原 packet 责任依旧；没有引入“模型必须逐词等于旧模型”的新求解门。

原同 H 已有 warm/predictor、当前 Dirichlet 线性修正、root/Cholesky 共享继续存在。本次不会把它们说成之前未实现，不因为本地表常数可复用而跨 H 复用旧 J、旧误差、旧接受结果或旧 model。固定同 engine 的三角商词与状态无关；当前六个系数、当前 root 行、当前 RHS/J、当前 $A T$ 仍真实形成。

### 4.2 A T 的原有限资格与非有限后备

实际 helper 为 `geometry_20261116_finite_trace_actual_input_support_linear.mjs`，6,246 B / `e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3`。其名称含 finite-trace 不意味着 current worker 改用了那个局部 J；这里消费的是已在 R602 明确接入的纯矩阵乘法 API。当前 J 仍是原 205b Fourier-product 算法加 R611 的同词商表。

每次原 `field(s,t,p,x)` 先真求 `rhsWithJacobian`，更新原 minA/minD/rootRelative，再把其实际矩阵与实际 tangent 交给该 helper。helper 按原资格扫描 A 和被用的 T；不合格走原完整循环，合格只组织同次 T 的实际非零支撑，保每一输出的原 $j$ 顺序、乘后加、全零初始化和完整 226×224 输出。原 ±0/下溢/累加溢出/NaN 条件界沿 R523 / R602，不因本次商表正常就取消其扫描或假定输出有限。

积分 grid、cusp breakpoints、每个 RK stage 的状态/切向增量、最终 `h*(a+2*b+2*c+d)/6` 的原括号及更新顺序逐字保留。没有另换 integrationGrid，没有按稀疏性减少任何模式、方向、mean 或 cell。

### 4.3 原完整数值参数

所有数值对象来自本 job 实际形成的 current250 合同；generator 深复制后只改变本次来源、请求标识和明确统计合同，再逐字段比较原数值对象相等。下表是完整主参数，细项仍以冻结原请求完整对象为执行输入。

| 原责任 | 保持值 |
|---|---|
| field / tail modes、spacing | 112 / 112、2 |
| 原 tail depth / 径向 nodes | 576 / 577 |
| 每节点 shooting state | 224 |
| 带两 mean 的本地 RK state / 每 stage 方向 | 226 / 224 |
| 当前完整物理响应 J | 338×112，原混合导数合同 |
| 实际 jet 顺序 | slope112、second112、meanSlopeCorrection1、meanSecondCorrection1、height112 |
| 原 owner iteration / trials / tolerance | 32 / 10 / 2e−9 |
| FD 两方向组 | direct_boundary、separated_boundary，各 10 |
| 原 FD 步长层 / Richardson 层 / relative threshold | 3 / 2 / 5e−5 |
| prefix inner trials / RMS / boundary tol | 17 / 1e−6 / 1e−11 |
| outer iterations / max_nodes | 8 / 1200 |
| material / physical angles | 4096 / 4096 |
| extension_step / taper_fraction | 0.005 / 0.4 |
| native_eta | 原字字符串 `"1"` |
| node_heap / jac_workers / native_exact_workers | 6144 / 2 / 2 |
| native_max_factor_bytes | 2147483648 |
| 原末门 | 同一当前 H 的 fresh audit、原 physical RMS/domain、原全部 FD contractions、原 full-DN 接受条件 |

“全部 338 解析 J”不是原 gate，不能在这里添加。原 `noJ` 请求的外部旗标不意味着可以省原内部需要的完整 tangent、mean、predictor 或物理分量。本次也不以记录到完整组件的 completion flag 代替 native/fullDN 原接受字段。对象 `original_scientific_contract`、`arithmetic` 全部原字值保留。

本入口仍是原 finite-prefix 问题，不替换成新的连续 C 目标，也不声称由 finite native / FD / full-DN 门直接得到闭面、全 D、全 t 或严格几何证书。那些数学责任不被本次工程和局部表达式命题支付。

## 5. 原输入、初猜与源码恢复的完整来源

下表所有固定 Git 输入均从原 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复，保实际压缩件字节及解码责任。本次作者没有重新获取这些大原件，也没有把其内容当作本地 fixture；真实完整读取/解码发生在公开 Actions 的原 prepare 中。

| 角色 | 原 topic 相对路径 | stored bytes | stored SHA-256 | Git blob |
|---|---|---:|---|---|
| accepted | `notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz` | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` | `6a9dfda743c464af6ae1190208e7157fa66df30f` |
| warm | `notes/public-actions-43646179305-1-condensedqp/eighteen-condensed-warm/warm-001.json.gz` | 4799943 | `6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a` | `1b8fdc0305244cb6063b49e538665c0178fc330a` |
| warm_status | `notes/public-actions-43646179305-1-condensedqp/eighteen-condensed-warm/driver-status.json.gz` | 231286 | `6443fce5e818ff20fd36075f6038ee60630d0b77e8ed2304d41e4d072ea6a005` | `a146da49f3e972a891010cab5928ffead72fa14e` |
| tail_config | `notes/public-actions-43588155190-1-prepare112/T112-config.json` | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` | `543d8364593985305438dda6a0c89b4b1a9c7ec5` |
| frozen_ledger_ready | `notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json` | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` | `4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3` |
| frozen_stored_ready | `notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json` | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` | `b6c44fe237750f13c8b10366f15525b481a74e09` |

actual63 的原 producer 来源为 `db6d728f30ee2d0c9ea62c96c622d8d85d2354b2`；原完整 warm producer source ledger 继续真绑定。其 decoded status 是 1,810,333 B / `8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46`。原 port 从 `/complete_scalar_profile/complete_original_port` 实际读取完整对象，生成本 job 的 `actual63-original-port-object.json`；新的传输文件有自己的完整身份，不能冒旧 port 文件 SHA。actual63 只提供原 prefix 初猜，不继承 current native/fullDN 接受。

actual91 的原 artifact 是 run `43672150224`、artifact `14145200674`、名称 `visible-mainline-modelresponse-43672150224-1`、stored size 10,267,458 B、SHA `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`、producer `b78f0dd1471a118d2ed21467602509d188c2ab67`。原来源只提取 failed73 whole-state tail 初猜，不把它当 prefix、已完成响应、接受的 native 状态或新 H 的缓存。

原 78 源恢复与两个 ready 完整输入继续执行。新 source preparation 并不以源码计数代替原 producer closure、原 packet 或恢复回执。科学 namespace 的 `preparation.json`、原 source ledger、解码 status、port 对象以及真实初猜均由原运行步骤产生并由原 reader 选择；没有从旧文件 hash 重造已删科学内容。

## 6. 一次真实准备、实际 HERE 与派生请求

generator 的 `context` 限定真实 public repository、`GITHUB_ACTIONS=true`、当前完整外请求 SHA、当前 schema/request253/namespace，并要求：

`HERE == GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations`

及传入 computations 同一真实目录。所有新 view 生成到这个目录；不是在另一个目录写新源却让 cfg 或 loader 仍声称原 HERE。源目标必须是普通新 basename，不得已有、不得符号链接；使用排他写入，不能覆盖任一旧源码。

`prepare` 先核 checkout 实际 HEAD 等于本次 `GITHUB_SHA`，核新公开三源，再确认所有十个目标尚不存在。随后恰好一次调用冻结 R603 generator 的 `prepare`，其参数仍绑定原 250 outer SHA。父准备必须在同一 run 四键、同一真实目录返回 complete/0，才读取其实际 `current-request250.json`。该父准备继续原 R593 / R573 等祖先生成；没有拿以前 run 的源收据代替本次实际动作。

读取真实 parent current 后，先遍历全部 466 源实际文件和 SHA，再逐个完整 baseline + literal count 生成十个 view。每个生成后的全文 bytes/SHA 必须等于计划。中途有失败则保当前 phase、已生成文件完整身份、原 exception/traceback 以及未生成 role suffix，不把半套新 closure 表示成 complete。

派生 current253 保存新实际请求、计划与真实 parent current descriptor；原 `R593_resource_strategy` 和 `R603_current_DN_input_support` 作为历史祖先记录保留，其描述不能冒当前 factory 身份。当前 active 角色明确来自 `R615_current_DN_normalized_moments`。该新字段同时标明两旧字段只作 ancestry，真实 source map、execution/science/reader entry 都为当前新值。

以下完整对象逐结构与实际 parent current 比较相等，不靠作者在文稿中重抄代替：

`lanes`、`reviewed_README_blobs`、`original_inputs`、`actual63`、`actual91_artifact`、`runtime`、`resources`、`live_call_resources`、`original_scientific_contract`、`arithmetic`、`retention`。

成功后写实际 `source-views.json`、`complete-source-map.json`、`current-request253.json`，原子保存每步来源；最后向 `GITHUB_ENV` 写当前请求真实绝对路径与实际 SHA。当前临时 JSON 中含本 job 的路径/receipt，因此其 SHA 必须由这次真实字节计算，不能预填 250 outer 或本文固定外请求 hash。

所有上述操作是来源、文本与元数据绑定，不导入或执行科学模块，不新造科学 clock。workflow 继续保留原公开 Actions 中既有语法检查；本作者没有在本地执行它们，也没有另加 fixture、试算或独立审核前门。

## 7. 真时钟、caps、owned 生命周期

source-only 准备和原输入恢复在原科学钟前，这是冻结父的明确执行安排。之后原 runner 的 `run` 在任何规则同步和第一 native factory 之前只写一次 `job-deadline.json`；已有该文件则拒绝重启钟。其 schema 仍为 `R493-original-full112-live128-job-deadline-v1`，绑定当前 source/request/run，使用原 monotonic 绝对截止。

| 原资源职责 | 当前值与范围 |
|---|---|
| 总科学钟 | 19,200 s，一次启动，换 H 不重置 |
| 科学阶段最后读回/清理保留 | 120 s |
| current native owner | 12,000 s 上限，原 248 / 250 实际合同 |
| owner replay reserve | 1,200 s |
| owner threads | 4 |
| stage / boundary / endpoint / audit caps | 8,000 / 600 / 600 / 1,800 s |
| factor cap | 19,200 s，仍与原实际 remaining clip |
| start free-storage gate | 68,719,476,736 B |
| free-storage resource stop | 21,474,836,480 B |
| uncached protocol call 原最大数 | 18 |
| job / science-step timeout | 350 / 320 min |
| source prepare / 原输入恢复 | 10 / 30 min |
| source readback / science readback / cleanup / report | 5 / 20 / 5 / 5 min |

所有 cap 是局部上限，不可相加扩总钟，不是能完成所有调用的承诺。表初始化、资格扫描及所有真实统计动作在实际 worker/engine 生命周期发生，消耗原预算。没有把本次新表预先从另一 job 搬进来省钟，也没有从 owner12000 推已用或还可用12000。

原 process group、PID/startticks、rules child、原 same-PID exec、quiet/reap 和信号传播来自冻结 runner 主体。只有当前 namespace、source/schema/请求号与实际 fullDN 角色来源级联；不增加吞掉资源异常后重新科学运行的分支。原 math fail、resource stop、external signal、未启动和返回码继续分别报告。

不得把 generator 的 `complete=true` 解释成 native 编译完成、科学启动、所有 components 成功或原接受。它仅说明这一次 source metadata 动作完成。新的来源核对属于实际执行身份，不是添加数值阈值；R611 的数值资格失败仍走原公式而不拒收该科学点。

## 8. 完整统计、实际绑定和中断范围

### 8.1 R611 八个计数与原 R523 十四个计数同时返回

每个真正 engine 的 R611 对象包含以下全部八个 Number 计数，reader 不只选总数：

| 字段 | 实际更新范围 |
|---|---|
| `table_elements_scanned` | 真资格扫描已检查的 cosine/sine 元素数 |
| `normalization_divisions_completed` | 构造中实际已执行并保存的逐元素除法 |
| `rhs_calls_started` | 真进入该 engine 的局部 RHS/J 调用 |
| `rhs_calls_returned` | 真完成全局部 J 返回 |
| `cached_moment_rows_completed` | 合格路径完整完成原内层 k 循环的角行 |
| `fallback_moment_rows_completed` | 原除法后备完整完成的角行 |
| `cached_normalized_table_reads_in_complete_rows` | 已完成角行的两表读取次数 |
| `fallback_normalization_divisions_in_complete_rows` | 已完成后备角行的原除法次数 |

完整 `last_observation`、实际 N/M/spacing、qualification/reason、scope 及任何新增未知字段都原对象保存。原 resolved-base guard 仍在表构造之前，不能把资格 false 的后备描述成能够消除原 base 参数错误。原 original-row-coefficients、original-six-moment-inner-loop、right/FL/FQ/Cholesky、return 各 phase 记录实际到达位置。

这八项是同一个 engine 生命周期内的累计值；不是仅当前 H、不是某次 call 的自动差分。入口没有为了好看重置旧 engine 计数，也没有用两快照相减推断被中断的未保存工作。八项新计数在 safe-integer 范围才可解释为准确整数；源未改用 BigInt，未引入溢出检测或拒收。新增 metadata 原值保留，并为每个实际字段记录 `Number.isSafeInteger`，false 只限制其解释。

原 A T 对象的十四项一字保留：`calls_started`、`calls_completed`、`finite_input_calls`、`original_complete_loop_calls`、`actual_A_entries_checked`、`actual_used_T_entries_checked`、`zero_j_terms_skipped`、`scalar_products_skipped`、`retained_j_terms_completed`、`actual_nonzero_T_words_indexed`、`actual_zero_T_words_seen`、`T_rows_indexed`、`zero_T_products_skipped_after_nonzero_A`、`retained_scalar_products_completed`。原 `fallback_reason_counts`、完整 last 和所有 scope/未知字段仍为整个实际对象。

### 8.2 stage → engine → 完整来源

`bindInputSupportObservers` 对真实 DN 的 stage 引用做 engine 对象身份分组。所有 stage 地址仍在 `actual_stage_to_engine`；一个 engine 被多个 stage 共享时，保显式索引而不是抹掉这些 stage。新的 moment 来源池和原 A T 来源池分别保存完整实际对象，仅当完整有序编码严格相等时复用已有索引。恢复规则是逐 engine 的 `normalized_moment_source_binding_index` 指向 `actual_normalized_moment_source_bindings` 的整对象，原 source 索引同理。

实际核读的内容包含新 factory/flow/R611、原 205b/a47df/717ac/cusp/root 文件、当次 engine 的参数、归一化资格与当前源 receipt。current-call 还比较新 moment 当前源与外层绑定的 `actual_normalized_local_J` 完整对象相等，并逐一核新公开源属于真实 request source map。这个核对是来源一致性；没有要求数值资格必须 true。

不能只凭当前 output schema 相同就接受另一个 source。reader 另核实际 progress schema、当前 client SHA、当前 call hook SHA 和 call 目录编号；错误保入 metadata_read_errors，不把未知对象补成旧源码的统计。

### 8.3 保存与未完成地址

`saveInputSupport` 的原调用点保留：原 initial evaluate 前/后，原 projected-model clock 回调之后，模型返回之后，当前响应返回前，以及原失败 catch 能运行时。新增的是该次真实 observer 对象，不新增 RHS/J/模型求值。记录包含 native_call、当前 phase/sequence、实际 source、原 deadline、全部 stage 映射及两个完整统计对象。

每次保存使用 `input-support-progress.json.writing` 排他写，再原子替换 `input-support-progress.json`。reader 对已提交文件读取原值，对尚存在的 .writing 只保实际身份并明确不是 committed snapshot。硬中断落在同步科学工作内，最后保存快照之后的进展仍未知；不能把 last 描述为精确 kill 地址。R611 没有逐 k 保存，`inner_k_progress_recorded=false` 必须保持；已完成角行数不等于未返回 assembly 已完成。原 helper 对未完成的内部列范围也不因新增 moment 统计而被补齐。

整个 progress 对象保在 science necessary 的 `actual_calls[*].actual_current_DN_input_support.original_value`。缺失、null、真实空对象和明确 binding failure 按原 reader 分开；完整对象及未知字段不会为了未来90K压成某几个成功数。

## 9. 两份原必要 scope、来源超限和清理

### 9.1 来源必要读回

新 generator `readback` 独立运行一次冻结 R603 的原 readback，保存原真实 command、exit、stdout/stderr 身份。它读取同 job 原 transport，核 run 四键、原 schema、request/plan/source 完整身份。

若原 child 返回 70，原 transport 必须真声明完整 overflow descriptor；新层读取同 job 的 `request250-source-preparation/necessary-source-overflow.json` 全部字节，核文件完整身份、attempted_bytes 和 attempted_sha256，再解析其完整必要对象。原 child=70、原 fallback 的 false、原 transport 完整 body 及其身份全部保留。新层是否完整由实际被读到的父 full body 加当前 record 判断，不把旧70改成0，也不把一个 fallback descriptor 当作旧完整必要正文。

父 full body 整个保存在 `original_parent_complete_necessary.value`。原父表示中的具名关系不重排或删选；其既有完整 inverse 仍属该表示。新层可对 `current_source_record` 使用已刊 R588 helper 19,120 B / `6f7cb8049e8b77b26964deb675e5868d6b374ac2e07c49b6517c8e51d7db0dad` 的明确源关系，须绑定实际 complete-source-map 和原 record 身份。只有连全部新关系 header 计入后严格较短才采用。逆操作明确只作用当前字段，父必要对象字面保持；不能把此局部关系称为任意科学树编码。

新 source 的 stderr 文件逐实际文件保完整原字节文本与身份，stdout 保实际身份，scope 如源码明确。source-readback 返回的完整正文仍必须单份不超过90,000 B；超出写本地 `necessary-source-overflow.json`，外传真实 bytes/SHA/descriptor、`necessary_readback_complete=false`、cleanup false 并 exit70。没有截前缀、分片、靠未知数值编码跨限，也没有承诺累积祖先表示必然 fit。

### 9.2 原科学必要读回

新 scientific reader 首先以当前真实 request/source/run 绑定原 runner，调用原 quiet 流程。未证明 quiescent 就不读取科学文件来伪装终态。证明 quiet 后，原 selector 全保：

- 原 preparation、原初猜/port/源恢复和两ready责任；
- execution 返回码、science/rules return、resource stop、external signal、真实 elapsed/clock/disk；
- original orchestration、完整 actual-call 目录、同 client/worker handoff；
- 当前 H 请求/响应、owner/compile/replay、R532 current model、四 components、真实 partial/unreturned 地址；
- 原全部 RootStats、accepted evaluation reuse、normal average、exact product、synthesis 路径及未知字段，原 R588 具名完整关系；
- 原 direct/separated affine FD 各方向、所有原阶层与收缩，原 fullDN 历程/末门与 fresh audit；
- 原 rules 实际 completed/failed轮、实际错误和全部非空 stderr 原文本；
- 原全部实际文件 receipt、missing/null、未启动或未返回 scope。

新 reader 对原源码的变换只作当前角色/source/schema/namespace 和完整新 observer 注册；不是重写科学 selector。原 error 文本保原 UTF-8-surrogateescape 的 ASCII JSON 携带方式；不会把无文件当空 stderr。原 empty stderr 的具体选择范围沿原 selector，不新增声称每个空文件都被展开。

只有原 `full_BVP_accepted` 真返回时，才写 `fullDN_accepted=true`；程序返回0、components complete、source complete、统计很多或两个必要 body完整都不能替代。原 noJ、FD 与混合338×112合同仍按原消费者解释。

science necessary 也单份≤90,000 B；否则保整个选中对象在本地 `necessary-summary-overflow.json`，外传完整实际descriptor、false和exit70。该 fallback 不是完整数学结论，其内部未知不能由 ancestor run 填值。源正文超限与科学正文超限各独立判断。

### 9.3 always、report、quiet 与删除

source_readback 与 scientific necessary 是独立 `if: always()` 步骤。source child70不会因为 shell 默认中止而省掉另一份必要读回。workflow 各自校验正文的当前 schema、run/source/request SHA、完整长度；source还核当前plan，然后传同一原正文及 bytes/SHA 到 report。compute 和 report 中出现的同份正文是同一 scope 的传输，不是两次额外科学评估。

cleanup 只有两份 `necessary_readback_complete=true` 才进入原 runner cleanup；其内部还要按原 receipt 和 PID/startticks 验证实际 quiet、summary、namespace和原删除边界。否则明确 `removed=false`，原 raw 留在该 runner 临时目录至销毁；不把缺读回或失败视为许可删除。来源准备 metadata、输出正文和 report 的保留义务仍遵原流程，不上传 raw科学数组或展开源到 artifact/Git。

report 保留原 compute /必要步骤结果，不能因为打印了一个有效 JSON 而把失败升级为成功。实际253运行号、真实head、job、原日志和全部终态都尚待真实dispatch；本稿不写虚构回执。

## 10. 精确入口和输出接口

### 10.1 外层固定绑定

公开 workflow 为 `.github/workflows/visible-larger-live128-normalized-six-moment-full112.yml`，只开放原显式 `workflow_dispatch`，独立 concurrency group `visible-larger-live128-normalized-moment253`，`cancel-in-progress=false`。root 单独发布并派发，不能由本来源结论自造 run 或改正在跑的250。

当前外请求：

- file：`computations/public-live128-normalized-six-moment-composition-request.json`；
- schema：`public-live128-normalized-moment-composition-request-v1`；
- bytes：14,540；
- SHA：`111eec1320495ca0f4fe0030edf5b290183ca1f650bd5b74fedf3b4711df754e`。

计划 schema 为 `R615-live128-normalized-moment-complete-source-plan-v1`，计划全文为 41,859 B / `ded97e0532dcceaab203ee5cac79353f1580586517e0877164978d419851206f`。真实 generator 为 29,985 B / `3329580248e7a19121d4e1fe05e65334ba667b46d48f0272aed17725845521b7`。

workflow checkout 保原 pinned action、`filter: blob:none` 和明确 sparse 路径，原 requests/notes source plans 全部保留，新计划另加。它没有整体完整 clone，也没有凭 source map 把原历史 input 都提前打开。原 setup/runtime 安装与既定公开 Actions 语法核保原职责。

### 10.2 prepare CLI 与真实目录

在 Actions 已设置真实环境后，实际调用为：

~~~bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_normalized_moment_source_views.py" prepare \
  --request "$VISIBLE_COMPUTATIONS/public-live128-normalized-six-moment-composition-request.json" \
  --request-sha256 111eec1320495ca0f4fe0030edf5b290183ca1f650bd5b74fedf3b4711df754e \
  --computations "$VISIBLE_COMPUTATIONS" \
  --out "$RUNNER_TEMP/request253-source-preparation"
~~~

其中 `VISIBLE_COMPUTATIONS` 为真实 checkout 下 `topics/visible-flex-larger-amplitude/computations`。输出：

| 对象 | 真实路径 / schema |
|---|---|
| source receipt | `$RUNNER_TEMP/request253-source-preparation/source-views.json` |
| receipt schema | `R615-live128-normalized-moment-complete-source-preparation-v1` |
| 完整当前源映射 | `$RUNNER_TEMP/request253-source-preparation/complete-source-map.json` |
| 当前实际请求 | `$RUNNER_TEMP/request253-source-preparation/current-request253.json` |
| 当前请求 schema | `public-live128-normalized-moment-original-full112-FD-fullDN-request-v1` |
| 当前科学 namespace | `$RUNNER_TEMP/visible-live128-normalized-moment253` |
| 实际 science summary | `$RUNNER_TEMP/visible-live128-normalized-moment253-necessary.json` |
| 实际 source summary | `$RUNNER_TEMP/request253-source-preparation-necessary.json` |

prepare 成功后由实际源设置 `VISIBLE_CURRENT_REQUEST` 和 `VISIBLE_CURRENT_REQUEST_SHA256`。祖先同 job 的 `request250-source-preparation/current-request250.json` 继续保留独立原身份。本阶段没有新科学deadline。

workflow 的 preflight 按真实 nested contract 显式读 253 outer → 250 outer → 248 outer → 原246完整请求，分别核字节身份，再取其原 R534 core plan；没有把外层小组合 JSON 错当含所有原 source keys 的完整科学请求。480项核对以本次真实 current253 为准；历史250/R593字段是有标注的祖先。

### 10.3 原 prepare 与完整 run CLI

原输入/source恢复：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_normalized_moment_owned_run.py" prepare \
  --request "$VISIBLE_CURRENT_REQUEST" \
  --request-sha256 "$VISIBLE_CURRENT_REQUEST_SHA256" \
  --namespace "$VISIBLE_BASE"
~~~

其中 `VISIBLE_BASE=$RUNNER_TEMP/visible-live128-normalized-moment253`。随后在独立原科学步骤调用同源的 `run`，其余 argv 完全同上。`run` 才创建一次原科学deadline，before rules/first factory；全 owner/J/model/FD/fullDN/fresh audit 均在其原剩余钟内。

这里不是独立微型 benchmark，不先跑一个小 H 或缩列fixture。原 source-only动作、原 syntax checks 和必要 source读取没有变成新的科学验收条件。

### 10.4 readback、frame 与 cleanup CLI

来源必要使用第10.2节同一generator/argv，将模式换为 `readback`。其帧为：

`BEGIN_REQUEST253_NORMALIZED_MOMENT_SOURCE_NECESSARY`  
`END_REQUEST253_NORMALIZED_MOMENT_SOURCE_NECESSARY`

完整schema为 `R615-live128-normalized-moment-complete-source-preparation-v1-necessary-v1`。

科学必要：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/root_20261116_live128_normalized_moment_necessary.py" \
  --request "$VISIBLE_CURRENT_REQUEST" \
  --request-sha256 "$VISIBLE_CURRENT_REQUEST_SHA256" \
  --namespace "$VISIBLE_BASE" \
  --out "$VISIBLE_NECESSARY"
~~~

其中 `VISIBLE_NECESSARY=$RUNNER_TEMP/visible-live128-normalized-moment253-necessary.json`；science schema为 `R615-live128-normalized-moment-original-full112-necessary-v1`，帧为：

`BEGIN_REQUEST253_NORMALIZED_MOMENT_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY`  
`END_REQUEST253_NORMALIZED_MOMENT_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY`

cleanup 只在第9.3节条件成立时调用同runner的 `cleanup`，传同一 `--request` / `--request-sha256` / `--namespace`，另加 `--summary "$VISIBLE_NECESSARY"`。该参数用真current253 SHA，不使用fixedouter SHA代替；两者各自的文件、位置和责任必须保持区分。

## 11. 可复查的文本事实与未执行范围

本作者对完整source/JSON做了字面构成与身份计算：每个十view baseline完整bytes/SHA、每个明确literal出现次数、每个输出全文身份、完整generator/workflow相对基线文本的重构，以及480集合中全部旧466源对原值均得到一致元数据。此处是文本/字节核对，不是本地科学测试、模块导入、AST、编译、数值对拍或fixture。实际Actions仍必须执行自身原绑定和完整科学。

两个公开小constructor的完整数学体来自指定原源；原 source text 的出处与当前source hash分别保留。newfactory实际只选一个R611localJ，newflow只透传其observer，currentflow保原R602完整A T。十view除该真实source级联及明确必要metadata外，原owner、R532、四components、正向/FD/fullDN主算法与门保持冻结字节或逐literal未动主体。

本次新题内执行文件共91,613 B，根workflow26,196 B；完整作者证明另计其实际UTF-8字节。十展开view不入主树，不存科学raw或必要body为Git对象。交接manifest只是源与作者文稿的完整身份目录，不冒科学回执。

已经支付的是：R611同engine原除法词命题的真实完整caller、具体source/loader/HERE/clock接口、完整observer与原必要选择的实际接线。仍需实际253支付 source生成、全原inputs恢复、当前owner真实返回、全model/components/FD/fullDN/末audit、实际资源前沿、两份90K正文及quiet清理。哪一项未开始、失败、超限或中断均按实际证据保原范围，不能由本稿完整、某表qualification=true或统计量大推出接受，也不能由某个声明false直接补成数值失败。



## 12. 实际独立发布与单次派发回执

本节仅补正式发布/派发的实际行政事实，未填科学结果。完整七件source/proof按本稿身份以source commit3997774b988d7f6ed0a5fc3267c526ac4e083bc7进入唯一发布流程；行政run43922546475/job133493336177。实际17:51:12推送非快进后，立即真实pull/rebase，读main45b7e91f3d7dfdcf667999634dd23e669d71acf5；根/课题README仍分别为21bd547f56590b7f2dd279d0297efb289a9b2783和bff8aea253a9e6a7a4fac28d810ac454c5499fec。

17:51:16.0899952Z普通push成功，main为4d572940046abc277049507545cbfbaf5785bc60；该时题内总量199224738字节。随后同一次发布流程对workflow420425819只发一个官方POST，17:51:22.9807024Z回200，实际run43922725201。官方再核head仍为4d572940046abc277049507545cbfbaf5785bc60、event=workflow_dispatch、attempt=1，compute job133493981603。

17:51:45的官方metadata显示前1–5步完成、第6步安装原runtime；没有读取running log，没有实际source准备/科学返回预填。后续R614由同一指定读者在真实终态取原必要scope；本段不把发布成功或已启动当数学接受。
