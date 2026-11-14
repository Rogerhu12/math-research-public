# M14/N512 谱权 affine runner：完整实现独审

审查者：`tail_theory`。状态：**冻结 runner、纯准备器、输入身份和运行门设计全文 PASS**。本审查只执行一个独立标准库 metadata/AST 检查器；没有导入 runner，没有创建 prefix、bridge 或 flow，没有运行 restart、Newton install、谱权 solver factory、BVP 或 DN。

本次结论是实现与入口审查，不是对将来实际运行结果的预先通过。所有未来输出始终是 `actual_nonlinear_tail=false`、`frozen_affine_dn=true` 的诊断。root 仍须实际持有运行进程，并分别记录程序返回、工具退出和该 affine 配点问题的状态。

## 1. 精确审查身份

| 文件 | SHA-256 |
|---|---|
| `scripts/db6f-prefix-spectral-affine-replay.py` | `ad219dbab80278670665ac3cb5401cb55daf33834cea8495dd16bf1c1396e4bd` |
| `scripts/db6f-prefix-prepare-spectral-affine-m14.py` | `915c3701e8b2de3857e10e7462e09630a5d5f4f955fc77882723788f1344fc99` |
| `notes/2026-11-09-db6f-prefix-spectral-affine-m14q512-01-launch.json` | `e45c553ea6832525c6a2719a197dbcc49a7ee5dd77badfb4b363e19a4b974a83` |
| `notes/2026-11-09-db6f-prefix-spectral-affine-m14-method.md` | `07ef29867fe40fe46f5b2048c3e220711e9f7d725afea47cb36cfed306422500` |
| `notes/2026-11-09-db6f-prefix-spectral-affine-m14-publication.json` | `7f94ae12cb5dde41c3dc4adabeae8fbd5d6ee11e775d465b639445c66f7a3ebe` |

全文读过上述两源、方法稿、作者定义层检查源及结果；逐段与原 `db6f-prefix-affine-replay.py` 对照。又重读实际原 TailMixin、AffineTailForInnerBVP、saved-mesh restart、SupportBVP chart/BC、adaptive Flow 及其 quintic 插值、原 save_checkpoint 和实际 f6 Newton 补丁。

已审谱权共轭 v2 模块仍是 `47e1128c8cabb7c77797ebea6534cf77d63964add54f78a2cab827d1f0101854`。其输入修复、共轭公式和 cubic 物理 RMS 返回门见先前 `2026-11-09-db6f-tail-review-spectral-conjugacy.md`；本次不把此前解析 toy 当作真实 prefix 全链验证。

## 2. 冻结问题确为 M14 自己的真 DN 基点

独立检查实际重新读取闭 M14/N512 CP、该 CP 的 `tail_seam.tail_record` 指向的 `_tail_0002` 包，以及原 physical port。它们的 hash 分别是 `3df8eefb…`、`009bf547…`、`500e0a0c…`，与 launch 严格对应。

原 prefix 是 `solver_success=true` 的固定 metric 解；原尾请求的 Jac/audit 均为 true，原 residual 在 $2\times10^{-9}$ 内，Jacobain 长度为 $616=(3\cdot14+2)14$，jets 为 14 scalar 加 3 个长度14的向量，audit 为原8键。原 CP 的 seam 成功字段及 residual 与这个包一致。没有借用 M12 或另一条 M14 的 tangent。

六项原 restart 身份、gauge、profile/chart/config 原文件、linear-port 的 physical 参数与 cut、原尾八个源码 hash、全部系数块字节和 SHA 均通过。本次检查只读系数块的 bytes/hash，没有加载数组或运行插值。实际 runner 未来仍会在 `load_checkpoint` 后核系数形状 $(6,n_{\rm spans},43)$ 和有限性，并执行原 restart 的实际初始化检查；这些运行门没有被静态审查预付。

原已闭真成功 packet 是仿射模型的输入证据，**新求解不成为真 DN 求解**。其端口始终是

$$
S_{\rm aff}(H)=S_0+J_0(H-H_0),
$$

其中 $J_0$ 取该原 physical Jacobian 的首14行。源码没有 `WeightedTailPort` 构造，没有调用 `solve_with_actual_tail` 或 `seam_audit`。原 client 模块的定义可被导入，但没有实例化 worker。

## 3. 原方程、自由参数和边界标度

对象构造、`fixed=True`、saved-mesh restart、`obj.initial` 和 flow 的来源与原 affine 基线相同。固定物理 profile 与 gauge 不变；自由参数 $p_0$ 仍只通过原 central support 初值等接口起作用，未被改成额外固定边界值。

原边界仍以

$$
H=\sigma q y_Z(L),\qquad
\frac{q f_Z(L,y,p)-S_{\rm aff}(H)/\sqrt{E_{\rm cut}}}
 {\mathrm{bcweights}}
$$

计算。`bcweights=physical_bc_tol/bc_tol`，所以原 scaled 容差对应原物理 terminal 容差。`TailMixin.bc_jac` 保留原 RHS Jacobian 及 $\sigma qJ_0/\sqrt E$ 的链式因子；原 inlet 参数 Jacobian 从父类保留。新增 `boundary_diagnostics` 复算同一式的分子和原 inlet/整体 BC，没有引入新的几何、二阶或 reach 阈值。

本次设置为 M14、prefix N512、tol $2\times10^{-9}$、bc_tol $10^{-8}$、physical_bc_tol $2\times10^{-11}$，均与该原 CP 的对应字段带类型一致。6500 是明确记录的配点资源上限，不是新物理参数。没有新 tail 调用，因此没有改变任何 tail RK、角求积或 projection floor。

## 4. 谱权与物理返回链

43 个未知量是一 mean 槽加 R/T/Z 三组各14模。独立用整数 bit-length 重建全部权重：mean 为1，三组第 $j$ 模同用不小于 $1+9j^2$ 的最小二幂。这与 launch 完全同值，未漏一组或错用 Fourier 索引。14个参数 $p$ 不加权。

使用已审正对角共轭后，原连续有限维方程和边界的解集保持对应；浮点运行轨迹、Newton merit 与自适应网格并不声称逐位不变。原 scalar/domain 检查是通过已还原物理状态的 callbacks 执行，不能因为换坐标就把越界 trial 静默裁剪。

谱权模块返回的 `sol.y/yp/sol` 已恢复物理 state 分量，但其自变量仍是原数值 chart 坐标 $t$。新 runner 随后显式执行

$$
s=\operatorname{chart}(t,p_0),\qquad
\text{physical.y}=\text{sol.y},
$$

再调用原 `Flow.adapt_c2_interpolant`。该函数在真实 $s$ 节点用原 RHS 和原 `velocity_s` 求共享两 jet，以原 longdouble 公式构造6系数 quintic，最后按原协议保存 float64。没有把 cubic 的 $t$ 导数直接误当物理 $s$ 导数。

谱权模块的原物理 RMS 是返回 cubic collocation 多项式的指标。quintic 使用原节点和重新计算的原导数，因而是另一个明确表示；RMS 不能自动当作它的全域 metric 证书。runner 另调用原 `adaptive.audit` 对新 quintic 作有限采样诊断，方法稿把这两者分开正确。后续实际闭图/连续认证仍需新证书。

## 5. 实际 f6 Newton 身份与原域拒绝

原 `f6curve_domain_newton.py` 的实际文件 hash 为 `6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654`。全文核过其实现：它只经 `col_fun`、`bc`、`jac` 评估状态；没有绕过 callbacks 直接把某些 weighted 数值槽当成 physical geometry。$S$ 奇异项不在支持范围内，谱权模块已明确拒绝。

其域内回溯仍捕获原 `FloatingPointError`，没有新增容差放宽、截断平方根或修改 physical 数据。权重改变 merit 中各未知量的数值尺度，这是此诊断希望检验的数值效果，不是一个新方程或成功保证。

runner 在对象构造后核15个 actual callback 的文件、qualname、首行和完整源码摘要。随后显式调用原 `domain_newton.install()`，要求 `_bvp.solve_newton is domain_newton.solve_newton`，再核实际函数源码和原11参数签名；求解后再次核对象 identity。这个逻辑正确处理了先前审查指出的风险：已审 `_bvp.py` 磁盘 hash 只能确认其布局/残差估计器，不能单凭它断言运行时仍使用 SciPy 默认 Newton。

独立检查器只核了15项 AST 身份和原签名。作者另运行的定义层检查实际未创建对象，报告来源吻合且 Newton 对象未改变；本审查已全文核该脚本及其范围，但没有将作者执行冒认独立运行。**安装后的真实身份门必须由未来 main 当场执行。**

## 6. 纯准备、依赖与新输出隔离

准备器只读取闭 JSON、hash 和 AST，加载的 runner 是 definitions-only；没有创建 prefix/bridge/flow、执行 restart、安装 Newton 或调用 solver factory。原 matched 121项闭包只作为已冻 source provenance 锚，输入候选仍是明确的 M14/N512；没有读取活动 M15 状态。

源码递归采用实际 source-root、notes、scripts 顺序，并保留实际新 runner main 的 imports。被排除的是未调用依赖的 CLI `main()`，不是实际类和 callback。首次过宽扫描把两个旧 CLI 依赖纳入，作者真实退出1并保留快照；修订后纯准备才退出0。作者没有用虚构模块填补缺依赖，也没有因此删掉实际回调链。

已独立重哈希新 launch 的全部97项，并核全部15 callback AST 文件均在其中。新 stem 的 stdout、reproduction、summary、CP 和系数输出都位于独立名字下，不是任何绑定输入。main 在写 STARTING 前拒绝已有诊断结果；未来外层 guard 观察应另外命名，不能覆写这个 runner 自己的 reproduction。

原 `save_checkpoint` 仍按约4.4MB原始系数块 gzip 分片，并拒绝超过5MB的压缩单件。新 runner 没有改变系数内容或包装定义；所有 metadata 写入还独立限制为小于1MB。

## 7. 输出可信度、异常和退出

首次 CP 和最终 CP 的顶层与 config 都显式写 `actual_nonlinear_tail=false`、`frozen_affine_dn=true`；summary 同样写这两个标志。原 `tail_seam`、`actual_outer_checks`、真实 tail_calls 等成功结论未从输入 CP 复制。旧 tail_config 和 `frozen_actual_tail` 仅作冻结来源保留。

`solver_success` 指已审谱权模块的 affine 配点状态，包括其返回后的原物理 RMS/BC 检查。它不表示真实 nonlinear DN 或闭图成功。原 affine 类在 `audit=True` 时会拒绝，而新 runner 没有调用 seam audit。

若 raw 配点失败，程序保存明确失败的诊断并请求 exit2；若初始化、C²重建、采样 audit 或写出过程抛异常，则 reproduction/summary 记录异常，不能由此前可能已经写出的中间 CP 反推全流程成功。正常完整结束才请求 exit0，仍保持 affine 范围。工具实际退出由 root 另行观察，不由 `requested_process_exit_code` 反推。

## 8. 独立实际检查与采用范围

独立脚本为 `scripts/db6f-tail-review-spectral-affine-inputs.py`。它仅使用标准库，不导入 NumPy、SciPy 或 runner。工具 `99db4a` 实际 exit0，耗时约0.349秒：97项文件绑定、15项 callback AST、43状态权重、14参数、616 Jacobian、17 jets、8 audit、原8尾源及六物理 restart 字段全部通过。

输出 `2026-11-09-db6f-tail-review-spectral-affine-inputs.json`，3338字节，SHA-256 `36121327bd55a4f64de6834c10c8f0da838469046bb7606c8ac334453f104884`。当前没有执行未来 main，没有真实 M14 重求，也没有产生加权 positive candidate。一次只读工具 transport 拒绝和一次附带 rg 的不存在路径结果仅是读取记录，不是数学或运行门失败；随后实际闭输入检查全部完成。

完整静态实现及闭输入审查未发现仍需修订的阻断项。root 可在既定授权和资源安排下执行这个明确的 affine 诊断；实际运行若有 callback/source/初始化门失败，应原样记录。即使加权配点或采样 metric 改善，也只能成为后续真实 DN 校正的依据，不能直接替代真联解、连续全图证书或 README G5。
