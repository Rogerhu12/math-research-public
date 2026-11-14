# 真 M14 谱权联解实现：全文独立审查

审查者：`/root/tail_review_continued`，2026-11-09，接续原 tail 审查角色。**结论：PASS，限于本次冻结 selector / preparer / 只读关闭审计的实现和实际已闭历史输入兼容性。没有执行新的候选初始化、BVP、DN 或真实联解；本结论不宣称新的数值解、G5 或 README 完成。**

## 1. 冻结审查对象与范围

本审逐字阅读三个新脚本和实现说明全文，并重读其实际调用的原 coupled、flat loader、shared client、谱权 v2、affine metadata helper。此前已审静态接口继续保留，未覆盖其稿件或结论。作者闭清单为 `prefix-spectral-true-m14-publication.json`，SHA256 `e4c5857bed8624c30b4f4730d688ec1fc4ec42c4d14e9296c8673ffd875cc15b`，八件共133097字节。

| 对象 | 本次审查的 SHA256 |
|---|---|
| `db6f-prefix-spectral-true-m14.py` | `d0eba3d875f5691c939825ee4824e0bf009b840e5c60f21ffa2138b3f228df99` |
| `db6f-prefix-prepare-spectral-true-m14.py` | `de3ce21bdc49880a7057a7e3fdd1737a18cc23f5b5a5ffce44b4b881fab5d7ff` |
| `db6f-prefix-audit-spectral-true-m14.py` | `1aa5e53985b5574dee68a032aa84ac47aa43e9aa8bd185b4af8650b618dcf0fa` |
| 实现说明 | `0bb461fe3e07bb6cd42e663135dfb4c8ccfadedb77d3fb72020b3a6b900bf75c` |
| 新 launch | `710fbd942be28cc67bddcc511d3e01a1bcc9de77adc5e7fea91f69adb5562666` |

新运行 stem 为 `2026-11-09-db6f-prefix-spectral-true-m14q512-01`。对它的首真包、前缀 CP、最终 summary 和 reproduction 的将来成功，本审均不作预设。作者的纯准备实际回执 `ff0ed2/exit0` 只证明准备程序闭合；缺 root 观察的实际负门 `ce2fb4/exit2` 也不等于执行过候选。

## 2. 共同物理问题、初值与来源闭包

纯准备继承已审 affine launch 的97来源，但取用的是其中的**原真 M14/N512 CP 与自己的真末包**：CP SHA256 `3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0`，自身 `_tail_0002` SHA256 `009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762`。它不依赖新的 affine 诊断是否成功，更没有将其 scope flag 翻为真联解。

新 launch 共106项绑定，所有旧97项按 path/bytes/SHA 完整包含；三份新代码、实现说明、接口及审查文档和新配置也在闭包内。独立脚本另重建21项 callback 的 AST 身份，包含完整文件、qualified name、首行与去末尾空白源码哈希，逐项匹配 launch。原 main 与新 selector main 纳入 Python 导入扫描；未使用的其它 CLI main 可以排除函数体扫描，但所在文件仍冻结。原实际 coupled main 没有沿用 affine 诊断的“不执行”例外。

固定 profile、chart、port、gauge、原六个 restart 字段、meridian length 以及物理尾参数通过实际输入链绑定。新 tail config 从原真配置复制，只更换实际 I/O：本次只有 `initialCheckpoint/traceFile/iterationCheckpointFile` 三键改变；原缺席的 `trialDiagnosticFile`、`trialStatePrefix`、`projectionFloor`、`correctInitialBoundary` 仍缺席。非 I/O 字段采用 canonical JSON 相等，故不会把布尔量和数值1混同。

原 spacing3、M14、N512、depth12、parts8、steps32、auditSteps32、36轮、tail tol2e−9、默认floor .05与默认初值边界修正保留；prefix 原 tol2e−9、bc1e−8、physical_bc2e−11、angular512、audit1024也保留。`max_nodes=6500` 是明确资源预算，不是换物理度量或放宽残差。argv 中 `--warmup-scales` 后没有数值，随后即 `--lagged-tail`，因此原 main 的 warmup 循环为空。

原 restart 会真正重建保存的多项式并作入口处理；准备器没有执行它，也没有预造首次物理高度。旧真实末包作为 warm 不意味着新首次请求无需实际求解。

## 3. 选择器只替换原全局 BVP callable

新 selector 加载原 flat wrapper 的 `.m`。独立 AST 检查其属性赋值只有 `runner.solve_bvp` 和两次保存/恢复 `sys.argv`；未修改 tail client、BC、原 `solve_with_actual_tail`、原 main 或几何回调。原 outer 函数中的两处 BVP 调用均解析到该 module-global 名字；因此这个插入点确实覆盖本次 lagged 路径。

令 $u=Wy$，本次43状态的 $W$ 是原谱权 v2 实际返回的正二幂对角，三块14模相同，最大2048，首槽1，并满足第 $j$ 模 $1+9j^2\le W_j<2(1+9j^2)$。原已审共轭直接复用：

$$
u'=Wf(x,W^{-1}u,p),\qquad b(W^{-1}u_a,W^{-1}u_b,p)=0.
$$

RHS Jacobian 是 $Wf_yW^{-1}$ 与 $Wf_p$；BC 两端状态列乘 $W^{-1}$，参数列和 BC 值不再缩放。参数 $p$ 保持原14个自由未知量。物理高度仍由 $H=\sigma q_gY_Z$ 给出，tail Jacobian 的物理尺度和原 $1/\sqrt E$ 因子没有额外谱权。

谱权 callable 对原状态、导数及 cubic PPoly 除权返回；原 chart 转换和 quintic `c2_interpolant` 随后照常执行。加权的有限精度轨迹可以变化，本审不将其称为只有模数改变的对照。weighted RMS、physical RMS、quintic 的采样 metric 以及保存 XYZ 的连续 metric 仍是不同证据。

## 4. 每次运行身份与真实 DN 外层

原 main 执行原 `domain_newton.install()` 后才进入 `solve_with_actual_tail`。每次新的 BVP callable 在前后都检查 `_bvp.solve_newton is f6curve_domain_newton.solve_newton`，并核实际文件、qualname、源码和11参数签名。准备器与审计器均不会自行安装 Newton。仅 SciPy 磁盘哈希不能替代这个运行期对象身份；实现确实保留了两种证据。

调用开始时检查原 M14 fixed 对象、512角数以及 `fun/bc/fun_jac/bc_jac` 的共同 owner。14项可直接取得的运行 callback 均核来源；访问的是原对象已构造的 `fixed_flow` 方法，没有额外调用 `flow()`、重新初始化候选或改变 RHS。静态绑定则另外覆盖实际 outer/main/shared solve/close/restart 等调用路径。

原 outer 顺序未改：先发真实 DN/J；内层期间临时使用由该真实响应线性化的 affine slope port；`finally` 恢复实际 tail；内层成功后，在新物理 cut 上再求真 DN/J，并用原 `o.bc` 判真实外边界；最多8轮，最后另作真实 audit seam。

因此谱权 callable 内重算的 physical BC 仍处于临时 affine port 下。它只支付内层物理坐标 BC，真实非线性 BC 则由恢复后的新 DN 和原 outer 检查支付。实现说明与最终 auditor 均明确分开，未把其中任何一个冒充另一个。

## 5. 首真请求绑定与异常关闭

空 warmup 保证原首请求编号是 `_tail_0001`。其响应返回后，第一次 inner BVP 开始前，selector 从原函数实参的物理 `y` 计算 $H=\sigma q_gy_Z$，核首包请求、完整配置、原八源、收敛、Jacobian 与状态 schema，然后以 exclusive 模式写首请求绑定。这是运行时证据，准备器未制造该包或该高度。

原 main 可能捕获数学异常后正常返回，因此新 selector 不凭函数返回值宣称成功；它在返回后调用 `check_outputs`。缺完整最终 CP/summary/seam、原 `solver_success=false` 或任何错误都使新程序记录 failure 并请求 exit2。输出 stem 已有 CP、coefficients、tail、summary、reproduction 或首请求绑定时拒绝覆盖；运行期小型 reproduction 用同目录临时文件替换。

在正常异常路径中，callback 与谱权异常都保留记录；在强中断、I/O失败或资源不足时，程序仍可能无法完整写出关闭记录。这时不能以陈旧 RUNNING、guard child 值或请求退出码代替工具实际退出。该限制已在实现与审计入口保留，本审没有把异常可记录性当作必然。

## 6. 新 M14 包 schema 的完整性

新 auditor 只允许原普通 shared envelope `request/response/config/source_sha256`。响应必须为原正常七字段 schema、`converged is True`、有限残差严格小于2e−9，且没有 `failed` 键。请求必须精确对应14维物理高度、`jacobian=True` 和正确 audit flag；八源必须等于旧真 M14 的实际普通 shared 来源，不能换成 M15 trial 八源或 linear-DN 九源。

| 对象 | 本次实际要求 |
|---|---:|
| 高度 Jacobian |616有限数|
| jets |14标量及3个长度14向量|
| audit |8有限标量；非audit请求则为null|
| staged states |865×28|
| raw states |13×28，与原 rawNode 指定行逐项一致|
| prefix状态 / 参数 / 中央高模尺度 |43 / 14 / 13|

checkpoint 的 resolved parameters 除 I/O 外与历史真参数 typed 相等；I/O键存在性和数值与新 config 一致。history 每行保留原有限量，未强制最后基点 norm 必须等于最终 residual，亦未错误要求已在收敛 break 前缺席的 chartCondition 必然存在。

本次独立检查不仅读 schema，还将**历史真实已闭末包**实际交给新只读 `check_packet`，正常通过。随后只在内存中分别损坏该历史包的 convergence、Jacobian长度、raw mirror、typed config、audit request 或失败标志，六例均在输出任何正报告前被拒绝。它们不是未来成功包，没有写回历史数据。

## 7. 最终 CP、物理 PPoly 与真实 seam

关闭审计同时要求原 summary 和 CP 的成功、无 error，扣除各自存储字段/时间后数据相等；新 config 精确为真 M14/N512 原容差与 fixed metric。固定物理字段对原 seed 逐项核验。保存 mesh 必须严格递增、从0到原物理 meridian length，节点不超过6500；所有已核文件大小与SHA的 finite float64 quintic 分片必须连续覆盖43槽。

审计器仅用已保存系数建立 PPoly 求末端高度，不调用原 flow 或 ODE。独立检查把历史真 M14的实际分片交给此方法，所得 $H=-q_gY_Z$ 与其自己的真末包请求逐位相同，确认了 axis、符号、槽位和端点约定的实际兼容性。这一重放不产生新候选，也不把旧 metric 移给新图。

原 outer row 必须顺序编号、inner成功、真tail有限且残差<2e−9，最后实际原 scaled BC≤1e−8。按该 row 的真正 `tail_calls` 定位自身真响应。内层节点值与随后 quintic 的端点求值不被错误要求逐位一致。

最终 seam 必须发生在最后 outer call 之后，按原 CP `tail_record` 定位新的 audit=True/Jac=True 包；其请求高度则必须和实际保存 PPoly 的末端高度精确相等。896角样本、全部mean/nonmean一二jet诊断、真实jets/残差、完整 source audit都检查。只要求原有限诊断如实存在，没有新加几何误差阈值，也没有把 source `actualMetric`当作实际保存XYZ的连续界。

每一谱权 call 都必须有原 weighted success、physical success、round-trip、原物理 RMS/BC门、14参数/43状态与原tol记录；数量对应成功outer数量，实际 runtime callback/前后Newton身份重新核验。最后physical RMS和节点数必须就是最终原CP保存的值。原代码上的成功标志与这些关闭记录一起使用，不能靠文件名或单项采样通过。

## 8. 实际退出观察是另外的必要证据

最终 CLI 要求 `observer=/root` 的实际完成观察，包含正 session_id、非空工具完成回执、真实 `actual_exit_code=0`、本次 stem 和关闭文件清单。程序的 `requested_process_exit_code=0` 不是实际退出的替代品。root观察须绑定 launch、reproduction、CP、summary、首请求绑定/首包、末次outer真包、最终seam真包和全部系数分片；重新读取全部文件后才给有限关闭 PASS。

这份 JSON 的真实性最终由持有实际工具会话的 root 负责，字符串字段本身不能创造一个工具事件。当前没有这样的新成功事件。本审独立运行正常final入口而不给观察，真实回执 **`7f2be3`、exit2**，正确返回 `NOT_READY: root actual tool-exit observation is required`，零输出文件、零求解。

首包模式不同：它只支付已经关闭的首个真 DN，并不要求主进程结束；仍不能被当成完整前缀或G5。本审没有运行未来首包的正入口。

## 9. 独立实际检查记录

独立检查脚本为 `scripts/db6f-tail-review-spectral-true-m14-implementation.py`。实际执行起始回执 `091313`，session81949，最终真实回执 **`e3dd99/exit0`**。报告 `notes/2026-11-09-db6f-tail-review-spectral-true-m14-implementation-check.json`，33529字节，SHA256 `c071919195a98d4f61e58d16b0d9d95b06e66feb8f8c0a6cda7a88bec3d5a937`。

本轮重哈希107个不同输入，前后同值；重建21项callback；复核106/97来源包含关系、全部八源、typed配置、空warmup、两处原全局BVP插入点与原finally恢复。只导入新审计和纯metadata定义，没有导入或构造候选模块；历史保存多项式端点只读求值一次。新候选初始化、restart、flow、RHS、Newton install、weighted solver factory、BVP、DN调用数全部为0。

作者实际准备/负门观察与本次独立观察分开保存；本审没有声称亲自观察作者的旧工具事件。最终审稿、独立脚本、检查报告、完整sources与观察文件由单独闭清单一起冻结。

## 10. 资源说明及尚未支付的门

实现说明关于 Linux `RLIMIT_DATA` 的窄描述已重新核对官方 [Linux man-pages, getrlimit(2)](https://man7.org/linux/man-pages/man2/getrlimit.2.html) 的 `RLIMIT_DATA` 与 `NOTES`（2026-11-09访问）：限制是每进程的数据/heap范围，Linux4.7起也影响相关mmap；fork继承且exec保留。这不是总cgroup内存或6500节点稀疏分解可容纳性的保证。该实现本身不设限额，root另作资源安排；先前affine的资源失败不改变这里的数学门。

本审不保证1.5GiB或任何未实际验证预算足够；也不把单进程affine预算直接移给带Node的真联解。后续真实运行必须保留资源失败与数学失败的区别、实际退出和完整来源。

即便将来新有限M14联解通过这里的全部关闭门，仍需自己新的共同cut、完整尾/XYZ表示、全域连续metric/曲率/位置、全时reach、握持与非全等、同g真实加密账本、新网格和未参与者独立全流程复跑。旧M14非单调历史以及无限尾严格存在缺口仍在。**本实现可交root实际运行；本审不支付这些尚未发生的后续门。**
