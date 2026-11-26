# 真实低逆输出后的58／224／32实际执行入口

2026-11-26，visible-exact-astra-198c63d-20261126。

已有 B4–B21、P1–P16、L1–L25 的纯数学合同不改。本次补上实际运行代码：

- `scripts/fourfold_codazzi_moment_physical_consumer_math.py`：显式接受原R141七目标或R142六个新目标加旧Green前缀，保各自原kind与完整引用；原 B4–B21 公式不改。weighted高图通过独立已成whole对象绑定，未冒充旧GH4。
- `scripts/fourfold_codazzi_physical_chain_owner.py`：一个运行只支付gate、ports或wpn中的一个阶段，逐记录保存含原endpoint的whole ball、读回并核包含。旧阶段只读取，绝不重新调用旧组合函数。
- `scripts/fourfold_codazzi_physical_chain_public_worker.py`：复用既成小标量worker的完整文件准入、README差异、容量、失败prefix和非FF循环；无native或矩阵恢复。
- `scripts/make_physical_chain_manifest.py`：只对真实已完成前置结果生成相应manifest/workflow，输入缺失、失败prefix或完整false门均只输出readiness路由。

没有新科学结果或预填low成功文件。本次仅AST与实际旧失败路由检查：对44730452579/1输出
`low_whole_incomplete_or_failed_prefix_retained_no_source_consumption`，`ready=false`，没有创建manifest/workflow。

## 使用

在真实R142科学输出与execution已经发布后，运行生成器的`--stage gate`，指定
`--low-result-dir`为该实际输出目录，`--low-manifest`为它真实使用的manifest；指定新
`--manifest-out`与`--workflow-out`。只有完整低逆、四源、193atoms和whole-point结果
全部存在且成功，才生成科学入口。默认low manifest为
`notes/2026-11-26-low193-parent-moment-inputs.json`。

新gate实际通过后，以`--stage ports`并额外指定真实`--gate-result-dir`、
`--gate-manifest`生成224响应入口。完整224实际成功后，用`--stage wpn`并额外
指定真实`--ports-result-dir`、`--ports-manifest`生成32响应入口。
每阶段各有独立完整scientific/execution及由实际输入hash确定的consumed marker；
不得覆盖旧marker或重跑已成目标。

默认新manifest文件名为调用者明确给出的路径。后两阶段的默认前置manifest分别为
`notes/2026-11-26-physical-gate-inputs.json`和
`notes/2026-11-26-physical-ports-inputs.json`；若使用其他名字须明确传入。

## 保存与原字段

gate完整分支只允许16、51、53、54、58条；17条丢失正余量属于真实失败prefix。
只有58条严格通过才`proved=true`。ports固定224，wpn固定32。
完整结果按`actual-physical-stage.json`保存，使用原科学公式的准确record order。

owner显式保留每个新结果的逻辑资格；临时Arb对象不自动序列化。下一阶段从已保存
record重建旧私有receiver、kappa、boundary和inverse majorant，既不重新求值旧门，
也不把一个字段的upper冒充lower。完整原低输入、weighted及D的文件身份沿阶段核同。

WPN保持N=24480的原projection，使用已成WHVA的四个source界、D的完整mean子列界
及原exact_reference中q>=1/8的准确floor；原N4096 mesh false不被改写。所有原mean、
ordinary源、两个独立端点、rough高端口与原fixed-metric/负侧/非线性剩余义务不变。


## 已保存 strict-epsilon 与 R149 v2 来源的后继准入

新增 complete_R142_low193_neumann_source_point_continuation_v1 分支只接受实际 complete/proved true、child0 的 NS 完整低输出。NS 某次可以只支付其剩余1至5个目标，但交给 physical58 时四个 source、全部193 atoms、5696个真实闭盒及1424个完整 point cells 必须全部齐全。owner 和生成器全文核对 NS 自身源码、纯准入及证明，并沿实际 whole-file references 读取最初 PS scientific/execution/manifest；原 whole defect 六球、strict saved-epsilon 门、model/refinement/reference 必须一致。PS 完整六球后的真实后处理失败可以原样保留；NS 完整输出的成功条件不因此放松。

已有 R149 coercive source-point 分支同时接受已发布的 whole_R142_six_ball_false_branch_with_unchanged_execution_references_v2：完整旧六球可以来自原 R142 或 PS，但必须由同一固定 R149 纯来源准入逐字段验证，且与实际成功的 theta 原件保存的 provenance 相同。旧 complete/proved/failure/returncode 和 target 状态不会被改写。旧 R142 defect=null 仍明确不合格。原 strict 分支及原 R149 v1 分支保留。

上述窄适配不改58／224／32的任一数学公式、记录顺序或目标数。没有实际完整低输出时仍只给 readiness，不生成 future-path manifest 或虚构 actual。

## 每条标量的正式提交顺序

emit 先构造包含新球和新 cursor 的完整候选 scientific 文档，原子写临时文件，完整读回并核 bytes、整个解析对象及新 Arb 球包含关系；全部通过后才把同一批已验证 bytes 原子替换正式输出、更新内存 document。正式 completed 前缀不再先于包含核验推进。计算、保存或读回失败时，原已接受前缀保持原义。

生成器的 pip 安装行使用 YAML block scalar，避免命令中的 colon-space 被解析成非法 mapping；安装版本和实际数学资源不变。这些事务及 YAML 修正不构成新科学目标。
