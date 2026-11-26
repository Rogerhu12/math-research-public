# 真实低逆输出后的58／224／32实际执行入口

2026-11-26，visible-exact-astra-198c63d15049。

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
