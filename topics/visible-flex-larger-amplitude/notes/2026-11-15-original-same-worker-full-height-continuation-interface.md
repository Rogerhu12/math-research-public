# 原同一 worker 的完整物理 H 向量续接接口草稿

作者：ChatGPT `/root/amplitude`，AI-assisted，2026-11-15。

本文仅给出原源码可实现的责任接口，尚未运行，没有新的 request、run、尾解或接受锚。它不修改已冻结的120入口或113实验。是否实际采用，取决于120真实失败所在阶段；单纯耗时尚不能判定为冷初猜失败。

## 1. 用途与不变问题

120首先以实际119第3批的六参数及显式 $\lambda=0.001$ 构造完整453态初猜，再由原 `true_height` 得到全部112项物理材料高度 $H_*$. 小的前三core比例不直接给出 $H_*$ 的大小或尾求解难度；原圆上传输及材料边界变换仍须实际执行。

若原冷启动在非零 $H_*$ 处失败，而真实记录支持改变初猜，拟在同一原尾worker内取

$$H(s)=sH_*,\qquad 0\leq s\leq1.$$

这里缩放全部112项，不删高模，不把近零项阈值化成零。最后一次目标直接复制原 $H_*$ 的有限数组，不从中间点或摘要重建。中间尾解只为最终同一Dirichlet问题提供初猜；它们不是120完整前缀场的解，也不是已经通过最终几何审计的尾锚。

原T112几何、metric、cut、far Robin、均值、576实际stage/原cusp网格、完整224状态和全部原残差行保持。实际维度和stage数仍从原配置/worker读，不用乘法猜测。原32次Newton上限、每次10个回溯、$2\times10^{-9}$残差阈值、原域和最终audit不变。

## 2. 已核源码入口

| 文件 | SHA256 |
|---|---|
| `geometry_20261115_six_control_full112.py` | `807f6a35e0d66aee7a2f324e4573bd2b9e9be8feab1972e4b073aa8ee91ed7a2` |
| `exact_20261114_true_tail_client.py` | `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09` |
| `tail_frozen_worker.mjs` | `3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054` |
| `tail_resumable_engine.mjs` | `1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8` |
| `tail_frozen_geometry.mjs` | `db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3` |
| `closure_linear_stage_graphs.mjs` | `be119b692fa20ea4cc646ff6c0e109fe473076974689558b4551c46e00359fdd` |
| `numerical-tail-slope-jacobian.mjs` | `206d82d3b41e6b9ce24b26447a2026c19c1c7126765107c23d58e55da25639e2` |
| 原 `78718-tail-tangent-core.mjs` | `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3` |

当前120的完整99来源闭包及78原公开源恢复仍是全部来源责任；表中只是本文直接涉及的入口，并非缩小依赖集合。原T112配置2161B、SHA `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` 没有 `initialCheckpoint`。两个ready仍按120/113的历史原字节恢复到既有env槽。未把91/95/103失败状态装成成功输入。

原Python接口已接受 `solve(height, jacobian=False, audit=False)`。原worker对每次请求调用同一 `dn.solve`；只有 `sol.converged` 才更新 `last` 及其tangent predictor。原core在进入一次求解时逐行 `Float64Array.from` 复制初猜，失败trial不会原地改写先前保存的收敛状态。

但 `jacobian=False` **不省Newton本身的完整withJ评价**：原core每个Newton迭代仍先 `evaluate(states,target,true,scales)`。该标志只省请求末端的 `heightJetJacobian` 生成。不能把本方案描述成便宜的无J尾求解。

## 3. 可实现的薄接口

拟独立接口为 `continue_complete_height(client, H_star, recipe, journal)`，借用已经创建的同一真实 `TailClient`，不另建配置或worker，不关闭调用方拥有的client。返回值只在 $s=1$ 的原目标完整响应及原J验证成功后有效。

recipe必须显式给出首个正目标比例、最大目标请求次数、增长/缩小策略和独立墙钟预算；未取得120实际记录前，本文不伪选一次已验证的步长。参数属于候选初猜策略，不是新的数学接受门。

执行次序如下。

1. 绑定当次未接受完整前缀初猜、六参数、$\lambda$、原四输入、配置、完整来源及精确的112项 $H_*$. 保存有限数组字节SHA和字面值摘要。只读120的摘要不足以重造初猜或完整尾状态；独立run须按同公开recipe真实重算，或在同job内消费尚存的真实状态。
2. 在同一worker真实求解 $H(0)$。这一步也必须经原非线性残差/域判据返回 `converged:true`。旧6815B零H响应及其J只可作为已有来源或线性初猜资料，不能替代这次完整worker返回。
3. 从最后一个实际收敛的 $s_a$ 提出 $s_t>s_a$，形成全部112项 $H(s_t)$，请求 `jacobian=False,audit=False`。原worker自身用真实tangent predictor或原amplitude warm构造初猜，原完整Newton与10档回溯决定是否收敛。
4. 只有原响应真实收敛、残差严格小于配置阈值、全部jets/均值/请求高度通过原client验证，才把 $s_t$ 记为本路径新的收敛点。中间点没有最终audit，标记为 `tail_nonlinear_converged`，不冒完整fullDN接受。
5. 可识别的原数学拒绝不推进 $s_a$。策略可减小目标增量后重新从原worker上一个收敛 `last` 试探；所有失败请求及原拒绝原因保留紧凑读数。不得把最新iteration恢复文件当成已收敛点。
6. $s=1$ 收敛后，在同一live client上请求原 $H_*$ 的 `jacobian=True,audit=False`。原Python缓存只有在已拥有完整J时才可复用；没有J的前一响应会真实再次进入worker。这个末端请求自身仍可能失败，不能以此前noJ收敛覆盖它。
7. 完整338×112响应、实际相同H、原三类边界FD及完整合同通过后，才把同一owner交回原fullDN调用链。后续每个新H仍由真实client求解；最终当前H的fresh native J、audit、BC、RMS、seam等原门照常执行。

核心调用只是复用既有协议，不能给 `client.cache_value`、worker的 `last`、`tangentPredictor` 或原 `converged` 字段人为赋值。若后续需要把这项策略装到full112入口，须独立source/schema明确记录它，不能修改807f旧源后仍沿用旧身份。

## 4. 零点到首正点并不自动得到好初猜

原worker的amplitude warm使用 $H_{new,1}/H_{prev,1}$，只在该比值有限且位于 $(0.25,4)$ 时生效。从零H到首正目标，该比值通常无定义。若零点处tangent predictor未能建立，原代码会回到原 `tail.initial`；因此“零H成功”不保证首个非零s更易求解。

必须记录 `tangent_predictor_ready/unavailable`、`tangent_warm_predictor/fallback`、`geometric_amplitude_warm` 的真实trace。第一个正s失败，与已有正s收敛后的后续拒绝，属于不同证据。原normalized residual按高度相关scale归一化；把s缩小也可能放大绝对舍入误差的相对作用，不能预称单调改善。

原worker的Dirichlet修正保全部高模，并经自己的 `r^4` 物理端口转换。薄接口只交物理H，不直接把H当raw Q、不手动重做端口缩放。

## 5. 数学拒绝与工程失败分开

原client先读取完整worker响应并写临时record，再验证 `converged`、残差、jets及J。只有明确拿到本次原响应，且它记录 `failed` 或 `converged:false` 的数学路径，才可按上述增量策略继续。不能把任意Python异常归为数学拒绝。

worker退出、JSON/IPC损坏、超时、文件限额/磁盘写入失败、缺失J或无来源字段，都应停止编排并如实标记partial/engineering failure。尤其响应记录写入失败时，worker可能已在内部推进了 `last`，调用方却没有完整受核响应；此时不得猜测状态并继续缩步。

原 `accepted-trial-recovery-only` 文件只说明某一次Newton回溯接受，不表示整尾达到 $2\times10^{-9}$；它不能满足本接口的收敛点责任。原失败checkpoint亦然。最终J失败应与中间非线性失败分开报告，不偷换为一个成功的noJ锚。

## 6. 预算与临时生命周期

每一个目标H请求仍独立保原32×10及原最终评价，不削减它们来伪造“便宜续接”。若最多付 $K$ 次目标请求，总费用为这些真实完整请求之和，再加末端全J/原FD及后续fullDN。原solver在循环后可能还有其既有最终withJ重评，故不能把墙钟简单写成 $K\times32$ 次RHS。

外层墙钟、最大目标请求次数及尚未访问的区间必须显式记录。预算耗尽时只报已到的 $s_a$ 和未完成的 $s=1$，不声称无解、路径已贯通或120成功。零H或首个正H就失败时，立即保原失败阶段，不盲目重复同冷初猜。

所有完整状态、tangent graph、响应和临时记录在同一Actions工作目录中保留到实际消费者用完；输出只紧凑原读数、源/输入/输出SHA与公开recipe/run。不得上传可重算raw到repo、Release或新artifact。删临时数据前必须完成相应紧凑读回；不靠摘要重建某个历史“已接受”状态。

原client存在单份临时压缩record的既有限额；若它触发，应作为具体工程阻断报告，不能删字段或忽略I/O失败后继续假装协议完成。新策略不修改这个原实现。

## 7. 对当前数学目标的有限作用

本方案只可能改善原当前H的初猜，并没有改善primal算术精度。若120重复103那种完整仿射预测改善而十档原noJ全部不降的事实，优先依据113完整128原始评价与R283匹配有限trace变分推进，不继续把问题归结为H步长。

即便尾边界路径到达 $s=1$，仍须完整非零前缀/fullDN接受。之后才可能把core目标 $\lambda A$ 逐步推进到原大目标、冻结最终六参数与同一g精化，并实际完成闭合、全t强C²、整像held幅度、含反射刚性差异、全域metric与reach。尾路径参数s不是曲面族t，也不是core幅度参数 $\lambda$；三者不能混用。

当前结论只是：同worker顺序请求及真实收敛初猜复用有原源码接口支持；首非零点可达、末端J成功、全场接受和上述最终几何目标均未得到新数值证据。本文未改源、未执行科学、未派发。
