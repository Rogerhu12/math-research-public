# Request186：保原运算顺序的 R305 外提及完整当前128末态链

作者：ChatGPT /root/amplitude。日期：2026-11-15。本文件给出独立可运行请求、源码与生命周期合同；当前没有本请求的实际运行、速度或完整性结果。全部科学编译、原方程评价、变分、矩阵、QR及审计只能在本公开仓库 Actions 执行。实际结果编号预留 R397。

## 1. 实际动机及本次完整责任

已发表 R394 的实际160必要读回给出了具体瓶颈：当前持久128 owner 的一次 alpha=1 已使完整原 shooting norm 从约 $1.2209605\times10^{-4}$ 降到 $9.68582474751023\times10^{-11}$，独立全226 replay 的原词相同；但随后原 R305 stages 在8000秒内只完成20/576段。stage20–22各完成8/12原子步、stage23完成7/12，24–575未付。原阶段统计为61243 column-direction steps、272 RK batches、4线程。boundary缺完整stage而未启动，endpoint缺boundary而未启动；独立原audit完整完成576段/7488原子advance。这里仅引用已发表原事实，不再下载160日志，不重新计算其指标。

186不恢复已删160状态或stage矩阵，也不把旧容差记录当成功锚。它重新恢复同一实际91失败BASE字节，真实执行fresh64原J/R273、持久128 owner与fresh replay，再请求全部576×224原R305变分、完整112 boundary、338×112混合endpoint和独立原物理audit。新代码只减少R305中明确重复的值运算与模态子表达式；原科学预算和所有接受门保持。没有孤立benchmark、只付少数列或预先提速通过门。

20到576约需很大的实际吞吐改善。当前改动不保证达到所需倍数，不能把源码上减少重复计算当作实测性能结论。若预算仍耗尽，实际已付、partial、未付和依赖未启动将按原记录返回。

## 2. 冻结文件与完整来源

以下六运行源和request在本题 computations；workflow在仓库根 .github/workflows。本文在notes。每个文本小于100KB；只创建了对象供主控发布，没有更新任何ref、分支、commit或触发运行。

| 文件 | bytes | SHA-256 | Git blob |
|---|---:|---|---|
| geometry_20261115_native_hoisted_operator_trace128.hpp | 26768 | `ab246a536ba65399174aeafb56582d398c648700c51e5b0d3b11c29090c2ec4d` | `0b680aae26357b28c25013240d4b21ebe518bb12` |
| geometry_20261115_native_hoisted_operator_stage128.cpp | 11277 | `03ab73e1697f541bffdb776cb208733074f92b24c2661b38f9cef7f8128bcbe1` | `b37ddca4ab5d6f17dffd951a5dca9bd1b80dc5c6` |
| geometry_20261115_native_hoisted_operator_final128.py | 27511 | `97d4ed767009c2d5756d1d3641ec5cf94da30d2f993981d30327be88751d2092` | `73a743072eef328573d712f31fa0ea47d1d8c75b` |
| geometry_20261115_native_hoisted_operator_final128_same_job.py | 38264 | `d1e78734285f6fa5999897833c667237673528252d22fa41604bf53c44f691ab` | `cdf844911079c6e03b057bea191aefe69ea0a073` |
| geometry_20261115_native_hoisted_operator_final128_bridge.mjs | 15729 | `f85f36c396100340049b34681d03fc4431b575f2377a0a422ae8f4832a8d734d` | `15216f60bc42fee28c26cff689d4698537c3a4bc` |
| root_20261115_native_hoisted128_necessary.py | 36164 | `0b9ab4c884b70a9ef3d939da7d347f7964323bbcb211f36caa533e8b60465365` | `bb789a7fe5a9d938b06104ca537a83ef918b20de` |
| public-native-hoisted-final128-request.json | 43719 | `e44517c6c5eb009145c2d922150e64ab20e8a09a26cb7f7697b47974f2194afd` | `708130a8b19cccfb0cb81ca5aed863811eba9c77` |
| visible-larger-public-native-hoisted-final128.yml | 28399 | `8fda2260140391a575378b99f9fd5694df2e53167b0e141cac629627ed68247e` | `4ee000b2c6b3c81343582b36fd7904d6d54fa9ed` |

旧160的58个source_sha256键和值逐项保留，新增六运行源后为64。原182r3必要reader是纯源文本选取方法的基线，未作为运行时网络reader导入；新reader只依赖stdlib，未增加该旧77KB网络入口的运行责任。旧137/140/152/160同job、bridge及原stage/header均保留真实旧身份，不作为新执行别名。

原数学基线如下：

| 原件 | 原SHA-256 | 186责任 |
|---|---|---|
| geometry_20261115_native_operator_trace128.hpp | 950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0 | 原R305全部公式；新header正文基线及非空geometry参数fallback |
| geometry_20261115_native_operator_stage128.cpp | 86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926 | 完整576×224/226 stage调度与文件责任基线 |
| geometry_20261115_native_shared_trace128.hpp | bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b | 共享真实primal/root tape、原统计、完整RK |
| geometry_20261115_native_trace_variation128.cpp | 8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d | 原R283前缀，不运行其单独main |
| geometry_20261115_native_operator_final128.py | a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef | 新component launcher的完整正文基线 |
| geometry_20261115_native_final128_components.py | ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045 | 原当前状态/physical输入绑定、进程和boundary/endpoint/audit编译 |
| geometry_20261115_native128_qualified_json_components_v2.py | 5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf | 原JSON与统计名资格化；strict-field分支不执行 |
| geometry_20261115_native_persistent128.py | 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322 | 原32×10 owner数学；只独立source-view接末态消费者和必要读回 |
| geometry_20261115_native_persistent128.cpp | 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd | 原完整持久128状态与实际trial，不变 |
| geometry_20261115_native_persistent128_probe.py | 2683e8e13a8d73d6c08500e9d3716d5bac5dc2e66648a17c8e1d75d246c62107 | 原fresh64 worker/J/R273构造；不执行旧邻词proposal |
| root_20261115_read_actual160_native128_necessary.py | 1536a01102f2c6620adbb43c0b8e1708bd57e194961079f0aa3016a152629c28 | 成功182r3必要字段、原数词与相同元数据共享方法的源基线 |

所读160源文本固定ref为3e77437c8463eda5917614f427562fed04655ff8。旧同job/bridge/request/workflow的完整SHA分别为024a3c67…、f68e51d1…、cfa6fe34…、f2af3e84…；request保存其全值。相对这些原件的完整diff独立交主控，没有改旧文件。

## 3. 三项外提及逐词范围的条件说明

### 3.1 六个独立dual方向共享同一个值程序

原prepare_point对坐标 $(P,P_t,L,U,w_2,E)$ 分别重做六次相同value表达式。新D6只做一次value，携六个独立方向。对每个方向，原D的primitive公式保持：

$$
\begin{aligned}
\dot{(a+b)}&=\dot a+\dot b,\\
\dot{(ab)}&=\dot a\,b+a\,\dot b,\\
v&=a/b,\qquad \dot v=(\dot a-v\dot b)/b,\\
v&=\sqrt a,\qquad \dot v=\dot a/(2v).
\end{aligned}
$$

特别是除法没有换成另一种结合方式的商法则。D6的值、零/一方向初始化、加减乘除和sqrt均沿原式；原quad、rho、flux表达式未重新因式分解。原K/S/D/A/sqrtD/quad的same_value比较及六方向finite检查保留。local_partial_basis_evaluations仍计六个方向，新统计另外记录shared_six_axis_point_programs；不能把计数变化冒数值变化或速度实测。

**条件范围：** 对相同输入、相同逐primitive舍入行为、相同成功有限分支，六条原独立D程序的对应value相同；用一次该value给六条原方向primitive，保持每条数据依赖上的运算词。这里是源表达式与依赖次序的结论，不声称已经执行全576阶段的bitwise比较。异常浮点环境、资源截止位置、调度时刻及失败最先出现的位置不由此保证相同。新source显式记录whole_stage_bitwise_comparison_independently_run=false。

### 3.2 frequency×momentum子树缓存

原每个角度、每个模态重复计算 frequency[j]×momentum_direction[j]。新实现只在当前列已形成完整momentum方向后计算一次该同一乘积，再放回原角度n/模态j的Pt累加。P累加不变，Pt的j顺序和每个乘积与cos表相乘的括号不变。没有把列批次转成别的内积归约，也没有改变任何literal sin/cos值。

### 3.3 final flux模态子树缓存

原每角度重复的

$$
-m\,\dot L_{j+1}+(m^2-1)\,\dot{\mathrm{momentum}}_j
$$

按原括号计算一次后，再进入原dU的模态累加。角度n的flux投影、j归约、invN乘法位置和所有target/prefactor/geometry项保持。不得用理想三角积化和差或Toeplitz公式代换独立binary64-lift字面表。

### 3.4 通用geometry方向与统计

原geometry五词是独立literal坐标，mu也是独立输入；不假定w2来自w，也不把E换成连续恒等式。当rk4_batch_parameters收到非空StepDirections时，新header把完整h、各field的五geometry方向和mu方向逐项交给原qualified R305函数。原通用路径没有按“当前state-only”为由删除。

186完整stage调用仍走原state-only全224列，完整226态包含两个mean。四个真实RK现场、原root有限停止/回溯、nominal Cholesky tape、全Gram action、原C solve及其残差读数全部保留。新统计只是明确hoist次数与fallback次数。

R305原有限算术与R283逐Cholesky程序导数的区别仍存在：old_dL_graph_word_equality_claimed=false、nominal_factor_residual_derivatives_proved_zero=false、direction_error_bound_supplied=false、C_assumed_F_e=false。本次没有把R305提升为IEEE舍入映射导数、准确实导数证书或连续ODE证书。

## 4. 实际编译和include解析，避免复活旧工程错误

新stage和newheader均逐字复制进本次RUNNER_TEMP编译目录。原950e header由已发表v2 shim的copy_named_source生成qualified副本，其完整SHA固定为4610e1e851a1f3b51f829355f08ef4555d1dc212b61f193db2edce5bb2a13435。新header的quoted include在同一临时目录找到该副本，而不是回到HERE下未经资格化旧header。

这点是实际source责任：若只把新stage放HERE再加-I work，quoted include会先搜索源文件所在目录，可能再次包含旧未修版本。新launcher不采用那条路径。它验证原编译argv中的唯一新stage位置，只替换该translation-unit的文件路径；原g++ flags、输出可执行路径和include列表保持。

原boundary与physical-final仍由同一个v2 shim按原变换生成，原JSON全局限定及空格处理、原统计名资格化不变。新header/stage自身已显式限定::quoted和新BatchStats。没有另编single-field证书来代替完整stages。

原flags：

`g++ -std=gnu++17 -O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math … -lquadmath`

实际source-copy、fallback身份、R283前缀、actual command、compile进程及可执行/文件manifest身份均在本次临时原件。其必要identity随摘要给出，未在本地执行编译或性能测试。

## 5. 原输入、同一owner和四个完整消费者

输入仍为真实91的完整原artifact：run43672150224/source b78f0dd1471a118d2ed21467602509d188c2ab67，artifact14145200674，10267458B，SHA78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6。原state是失败BASE，只作字面初猜；没有accepted95或其他失败结果重标。

两个原constructor ready仍按历史8bd267107cc8710d371f3b62c02986655ac965b0的准确Git blob/bytes/SHA恢复到RUNNER_TEMP，并通过原已有environment槽消费。原78-source恢复及当前analytic-slope adapter的实际来源保持。没有改成DEFAULT_CONFIG、旧解包目录或由hash伪造几何输入。

fresh64原worker真实形成当前J和完整R273。持久128 owner保所有129248行及577×224状态；每轮只把当前128残差显式cast成固定fresh64 chord的QR右端。固定初始64 J不是当前128 DF。方向在128中用原sigma64与z64提升后相乘，接受状态不会降回64。原32方向、十个alpha、严格原sigma-scaled norm下降、2e-9和独立fresh replay保留。

source-view在原owner临时状态仍活着时调用四组件；每项都核当前packet/binding、同一run、owner source、precleanup summary和完整final-state.f128。缺真实状态则原样未启动。并未新增“必须先native_accepted=true”的前门。

| 组件 | 本次完整责任与依赖 |
|---|---|
| stages | 新hoisted R305；576段×224方向、全226 RK态、原node n+1→n、原shape port、两mean、实际原子步表 |
| boundary | 只有实际完整stage输入产生后，原R302全112 forcing与完整边界链；缺项即原样未启动 |
| endpoint | 只有实际完整boundary后，原338×112混合响应；first112+meanSlope用原有限trace/RHS，second/meanSecond/height沿原对称cut程序 |
| audit | 保留独立原预算，即使stages或boundary未完仍用本次真实state尝试完整原物理jet/metric程序 |

端点全338行均为解析Jacobian的声明仍false，physical C-based径向公式不冒有限root程序径向导数。全四组件即使完成也不自动构成native/fullDN接受、完整非零闭面或本题全部目标。

实际子步总数来自原packet/profile/cusp分配。不能把576×12当原总预算或漏掉13-step单元。完整stage程序和独立audit的原步表都不变。

## 6. 统一预算与原规则监控

| 范围 | 固定资源 |
|---|---:|
| 从fresh64源/J/R273之前开始的绝对deadline | 19200秒 |
| 全局必要读回/cleanup预留 | 120秒 |
| owner请求上限，含fresh replay | 6000秒 |
| owner内fresh replay预留 | 1200秒 |
| stages / boundary / endpoint / audit科学cap | 8000 / 600 / 600 / 1800秒 |
| 各component overhead allocation | 345 / 720 / 345 / 345秒 |
| 原单次compile cap | 300秒 |
| stage/audit线程 | 4 |
| science step / compute job | 330 / 350分钟 |
| necessary always step / report job | 2 / 5分钟 |
| 原规则同步周期 | 2700秒 |

原wall_clock_envelope对象与160逐项相同。各科学阶段继续共用Python monotonic_ns绝对deadline；Node预算元数据由同Python读取。fresh64/J/R273/packet、编译、owner/replay和原组件都计入同一期限，audit预留与原dependent约束不变。必要always步骤只做元数据和字节，不重置科学clock或调用任何数值程序。

science checkout固定实际触发commit。原rules runner通过独立镜像每2700秒真实pull/rebase；双README改变依原逻辑停止科学。reviewed root/topic blobs为21bd547f56590b7f2dd279d0297efb289a9b2783 / bff8aea253a9e6a7a4fac28d810ac454c5499fec。workflow保merge.stat=false；取件和规则token在启动科学child前移除，无个人PAT进源码或工具参数。

## 7. 原source-view的数学与工程边界

旧owner文件、旧probe文件不改。新same-job helper只在内存中形成明确独立view，并记录实际helper source；source-only反向替换可逐字恢复旧文件：

- owner view为39113B，SHA f01799d610f50f43f54b090d008837704b8edc4072d807ee43548ea2f9c86518。保原所有数值body；在原final seal前插四组件调用，把原末尾重复compact/无条件删除段换成必要reader前的最小owner→bridge收据，并把临时event-journal描述写准。
- probe view为17994B，SHA02ddd879306c0cffea7a0b9c22a1157876b6fa281aa0af293b5ac7924f3e350b。原四处改动为64端点责任标签、实际transport状态传播、保存原probe summary、延迟末尾raw cleanup。
- 两view的emit在新helper中明确绑定：完整原事件写本次临时journal，小型阶段/错误receipt公开；不再把完整科学树或stdout编码/分段。原真实数学评价与原子进程等候/终止函数不变。
- 原每trial/per-iteration QR已消费后立即删除的生命周期保持，全部原标量记录和数组身份先保留。仅末态/四组件所需raw的最后删除被延迟；它们不是新的持久锚。

组件launcher本身的局部compact是owner-to-parent索引，完整summary仍在同job。科学C++返回70与局部/最终协议70分别记录，不能把读回超限当原数学拒绝。旧component依赖只消费实际完整数学输入，不由hash恢复未付矩阵。

## 8. 一份必要摘要和所有范围边界

新necessary reader只读取本次临时原JSON/工程stderr和标准库进程元数据，不导入数学source、不读取科学二进制数组、不下载历史日志，不重新求norm/J/域/区间。它不是旧182网络扫描器的别名。

必要正文包括：

1. 原owner全部实际trial、完整原evaluation的norm/root统计/错误/partial字段；列并集与每行原key-set区分缺键和null。只有完整原evaluation字典相同时才共享。完整owner初末与真实未访字段保留。未识别原owner事件也显式保留，不把错误静默丢掉。
2. 原全部QR direction summary及formed-model读数，完整大输入/数组只身份。
3. 四个实际component原summary身份、源/输入绑定、主科学process与launcher/transport状态、budget、compile错误、原科学顶层指标。
4. 所有实际stage accounting的原地址、完整/partial、atomic/query进度及后缀、active位置和错误。只有非地址原字段完全相同时共享一份正文；每个原行索引与实际stage/input/output地址均显式列出，不根据count猜范围。成功逐stage的完整root统计/逐列大表仅完整身份与实际count。
5. actual original64受控停止、原native响应标量、原fresh/replay/state身份、所有终态责任flags。
6. 工程错误只从实际stderr/compiler stdout读取；保完整文件bytes/SHA、必要原错误行及真实选择/未返回范围。科学stdout不再当“错误日志”转运。
7. 本次child-reaped/quiet证据和实际临时清理责任。

相同的已选字典仅在整个字典canonical字段等同时，以一个同JSON内的明确pointer引用较早完整正文。这不是把大科学表编码、分块或隐藏成可重建传输。literal JSON数字词由专门类型保留，原文件SHA与排序canonical元数据SHA分列，不混称逐文件字节相等。

最终只有 `BEGIN_VISIBLE186_NECESSARY_SUMMARY` / `END_VISIBLE186_NECESSARY_SUMMARY` 之间的一份ASCII JSON，hard bound为90000B。计算job与report核同一payload的bytes/SHA；打印LF不属于GITHUB_OUTPUT payload，临时necessary-summary.json带LF。成功大矩阵/逐列对象不逐值返回给主控，不声称主控已读完整数据。

若必要字段仍超限、原件缺失或身份错误，返回明确summary_complete=false和协议70，保实际错误/attempted bytes/SHA及范围。不会提高上限、拆分、编码或删科学试步来宣称complete。尚未实测未来摘要大小，不能保证最大32×10全部复杂失败数据一定小于上限。

## 9. 清理只在必要读回成功且原owner静止后执行

新owner/bridge/probe保留最后临时原件，不能在reader超限时主动删除。fresh parent在原child实际wait/reap后写native186-child-close.json；always reader检查该原收据，并查同用户进程cmdline是否仍引用本请求owner/probe根。quiet观测范围明确，不冒已证明所有全机进程停止。

只有必要summary_complete、transport_complete、cleanup_allowed和原child_reaped均true，workflow才再次扫描本请求三个临时目录的进程引用，然后删除这些目录。actual91只对本请求同uid真目录添加owner权限，拒绝symlink/越界。读回失败或quiet不明即记录cleanup skipped；不上传raw，runner teardown最终回收临时空间。这个工程清理条件不改变任何数学接受门。

stage/audit失败或资源partial，只要原必要范围完整读回且子进程静止，可以清理已消费raw；不能因为科学未成功就伪称summary不完整。反之，运行返回success也不覆盖读回缺失。最终删除是否发生由独立原cleanup事件说明，摘要里的cleanup_allowed只表允许条件，不冒删除已经完成。

## 10. 本地已做与尚未付

已做的是原公开source全文阅读、完整source/JSON字节身份、原58/new6 pin对应、明确文本替换/全逆变换、完整差异与字段/生命周期核对。原19200预算对象保持，旧科学源保持。没有本地编译、模块导入、科学求值、数值fixture、benchmark或额外审批门；Actions沿既有AST/Node检查与真实编译路径执行。

主控唯一负责实际Git发布与触发。本合同未填未来run、完成stage数、speedup或accepted锚。186完成后按真实必要summary判断是否付清全576×224及后继责任；资源不足仍是具体未付，不能由正确源码或局部完成代替。
