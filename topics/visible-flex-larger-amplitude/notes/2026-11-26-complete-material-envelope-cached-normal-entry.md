# 完整材料地址包络的独立 cached normal 入口

**状态：完整源码、来源、参数和纯读数器已锁定；本文交付时尚未准入或执行科学。** 本稿对应 `material-envelope-entry/generated/` 的完整 driver、launcher、reader 和两步 ready。三依赖均为实际完整文件 SHA，完整源码再生及 `--verify-existing` 已真实执行；没有导入科学模块或运行数值 fixture。

## 1. 这次改变的责任与不变的物理问题

本入口采用一个明确的新有限工作集政策：完整永久非线性责任为 $E=P_0\cup G$。$P_0$ 是当前可完整读取、准确解析及绑定的显式历史地址，$G$ 是按独立来源闭包证明承担的完整历史网格包络。所有地址均在当前候选的固定材料角图中重读；不继承旧场的函数值、曲率、可行性或连续证书。

新政策不声称恢复了缺失报告中每个地址的旧 `protected` 标记或旧 required 行优先次序。已有显式 $P_0$ 的原 e783 selector 前缀和原幅度行保持；$G$ 的全部点承担真实非线性筛选，另由明确的新近活动和实际分离政策进入线性工作集。`unknown_historical_protected_labels_reconstructed=False` 和 `old_protected_required_priority_equivalence_claimed=False` 是完整报告合同的一部分。

物理 operator 仍是已锁 a62c cached reference-centred normal 全体，校准仍为 3e47，frame helper 仍为 ba3d。其完整模型、固定标量 $g$、固定 seed、原 core/omega/H 自由量、全部 32 个共同 normal 阶段、全部隐式矩阵与外参数 J/J* 均不在本次改动中重定义。每个新场必须先完整读自身初值，再据同一正测度比较自己的 Phi；不借另一个表示的旧 Phi。

## 2. 跨运行地址绑定必须来自实际完整输入

来源相同、数组形状相同、角数相同、名义积分阶数相同，都不能单独证明两个 carrier 中的地址字相同。`--material-envelope-binding` 由独立 consumer 严格核实际载体证据；仅当完整当前 carrier 确实与指定原载体逐字同 SHA 时，才可使用其明确的同载体分支。

若旧、新径向 Gauss 字不同，责任集合是旧与新准确 literal 径向地址的并集，均配完整角格。此差异不能通过把旧角/径向 index 按新数组重解释来消掉。当前已存在的 reference `locations.json` 继续作为显式 manifest；consumer 还严格从实际 preparation 的 `new_locations` 记录读取完整当前 P0。不存在的旧运行报告不会在参数中伪造为存在，也不会用空报告替代。

旧 normal-angle 的 literal 数值被当作新冻结材料图的 phi0 地址，这一既有解释明确保留，不声称两种图的地址代表同一物理点。任何真正跨节点转移须经过独立的准确节点和位置绑定，不能只依据浮点 times 的相等或点数相同。

## 3. 完整入口和依赖 API

| 层 | 完整文件 | 实际职责 |
|---|---|---|
| 永久记忆 | `complete_material_envelope_memory.py` | 严格来源闭包、实际历史地址绑定、显式点和隐式包络、append-only typed 分离状态 |
| 行选择 | `complete_material_envelope_rows.py` | 保原完整前缀，追加新包络政策选择的完整物理行 |
| 真筛 | `so3_reference_centred_c1_material_envelope_geometry.py` | 当前全网格、必要的旧径向额外网格、全部显式点及两个主曲率/两支距离真读 |
| 科学入口 | `fullclosed_reference_centred_c1_material_envelope_so3_qp.py` | 原完整 metric/Phase I/回溯循环，只接新记忆和筛选 API |
| Actions launcher | `launch_reference_centred_c1_material_envelope_so3_actions.py` | 完整来源绑定，明确透传全部参数，保公开 Actions 执行限制 |
| 纯读数器 | `read_reference_centred_c1_material_envelope_so3_report.py` | 完整 source/model/预算/每次扫描/三类行及实际归因，不计算 F/J/根/积分 |

consumer 的真实入口为：

```python
load_memory(args, preparation, q, history,
            restart=None, source_report_path=None)
    -> witnesses, radius_witnesses, history_record, envelope
```

`envelope.definition` 是完整政策定义，`envelope.metadata()` 每次返回新的独立 snapshot。原报告和已完成 trial 的字典不能被以后加入的新点反向改写。geometry 使用原 API，只在构造时明确增加 `envelope=envelope`；scan 的原字段仍保留，另加当前这一次的 `material_envelope` scope。

新增数值参数只有 `--envelope-near-active-rows`，默认 32，必须是正整数。它限制当前网格近活动候选的新增池；本算法实际拒绝并发现的 typed 分离地址永久保留，不受这个上限截断。原 `--active-band` 仍是明确的实际行选择参数。`--material-envelope-binding` 是来源证据路径，不是数值可行性容差。

## 4. 全部真实非线性筛选

每次 starting、trial、accepted 和 final 的完整 geometry 都有其自身点身份和包络 scope。完整 scope 必须实际记录当前网格完整、历史额外网格完整、所有显式地址读完、每个隐式地址全 sixjets、两个主曲率分支、两支 witness 距离以及历史地址绑定完整。纯读数器调用 consumer 的完整 `validate_scan_metadata`，不另复制一个宽松的规则集。

若 scan 返回不完整字典，scope 必须保留真实 false/null 与已完成范围。缺失读数不能被解释为零违约。没有进行 geometry 的 trial 仍保留 `full_geometry=None`；原 core/domain/root 失败也保持原真实失败归因。首个场计算失败时，初始场、方向数和最终 bundle 不会被补成成功。

原 driver 只有在行准备、QP 和整段回溯结束后，才把方向 record 加入方向列表。因此已写首场失败报告保持空方向列表；读数器不为不存在的方向捏造 rows、QP 或可接受 trial。

## 5. 线性行、缓存和 Phase I

完整行数恒等式改为：

$$
n_C=n_{\rm original}+n_{\rm amplitude}+n_{\rm envelope}.
$$

原 `original_prefix_rows` 与 `appended_amplitude_rows` 的含义不变，新增 `appended_envelope_rows`。报告同时记录 `known_geometry_and_amplitude_prefix_rows`、`known_prefix_bytes`、`envelope_rows_start_index` 和 `known_prefix_rewritten=False`。新增行从旧完整前缀末尾开始；mmap 原位扩容，仅写新后缀，不重写原行、不另外建立一份完整大前缀。

每行仍携带真实 physical_g、正归一化比例、归一化 bound、当前完整点身份和来源。完整 Phase I 的 `original_rows` 等于三类行总数。共同 slack 只用于线性恢复子问题，不代替真实 geometry；接受依据仍是原完整非线性读数与原真实正违约下降。原 metric 方向仍需真实同 Phi 下降和完整真实几何通过。

## 6. 报告持久状态和自续

初始 report 字典在第一次 F 之前写入 `material_envelope=envelope.metadata()`。这是必要的实际初始化：原入口在首次 F 前直接 `write_json`，尚未走后续 `save_report`。这份初始 snapshot 可以诚实描述尚无完成 scan 的状态。

原 `save_report` 只新增以下一行：

```python
report['material_envelope'] = envelope.metadata()
```

这使新实际 typed 分离状态随每次报告保存。新 reader 校验完整 consumer/source/政策与当前模型、carrier，再读取该状态。自续只能从同一个完整新 driver/source/model 及其真实已完成 report/checkpoint 进入；它必须恢复原完整 append-only 状态，而不是只恢复当前极值。

本稿不声称整个原 `save_report` 到 EOF 字节未改。实际静态准则是：只剔除上述唯一新行后，整个剩余后缀逐字 SHA 为原来的 `9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee`。这样分别说明真正必要的持久状态改动与未改的科学循环。

## 7. 纯读数器的完整来源闭合

本派生明确从 revision2 的 3803 reader 开始，保留其 `model.get('schema') != OPERATOR_SCHEMA` 修复。不会沿用旧 8b5 中已发现的 plain-centered schema 常量。

reader 新增一个完整 `material_envelope_binding`：完整核 driver pin、实际文件 SHA、真实 pure validator 函数的 codefile、政策定义、cap、三来源角色、当前模型和 carrier。随后将该 validator 作为显式 `envelope_check` 参数传入 `geometric` 与 `direction`，覆盖 starting/trial/accepted/final，避免模块全局状态或跨报告回填。

完整 scan 的外层点 SHA 必须等于其 `material_envelope.current_full_point_sha256`。每个已完成方向的行记录还独立核原前缀实际前后 SHA 相等、完整 free-coordinate 列数、真实 prefix/total cache 字节、追加后缀 metadata 的完整 SHA、同一个 starting point 与政策、真实 active-band/cap，以及 consumer 验证过的同期 uncapped typed memory。新政策不会改变原 normal 34 项 snapshot、完整 reference-centering、fixed seed、同图 C1 和独立 no-grad 数值缓存的读数范围。frame 缓存命中数只作实际成本记录，不用于减少物理责任，也不宣称未测加速。

## 8. 静态验证与实际执行范围

目前已实际完成纯源码再生、AST/compile、无重复 literal dict key、完整 driver/launcher 82 个参数的相同解析；读取的是原声明参数字符串，没有导入科学模块。三体均小于 100KB。完整函数 AST 对照中：driver 仅 all_locations/parse_args/main 改变；launcher 仅 parse_args/main 改变；reader 仅 geometric/direction/read_report 改变并新增独立 binding，18 个原函数保持相同。

最终三依赖已逐文件核 SHA 后填入并完整再生。30 个 runtime source role 均对实际完整文件核同，全部 82 个参数由实际 driver/launcher 的 parse_args 解析为同一映射；完整 ready 已写入真实 address-binding 路径。所有源码实际通过 AST、compile、py_compile、重复 literal key/keyword 与尾空白检查。没有另外的科学 fixture 或数值准入条件。

科学步骤只在公开 Actions 运行。此次没有执行科学 F/J、根、积分或新的候选，没有已接受方向或连续证书。有限全包络通过也仅说明这次完整有限责任的结果；统一连续 metric、reach、全局 embedding 与最终研究目标仍需各自真实同场证明。


## 9. 真实 run07 输入证据与完整两步参数

run07 的必要输入再生已由独立公开步骤完成，记录见[整个旧载体恢复与径向地址逐字核同](2026-11-26-run07-actual-restored-old-carrier-and-radial-word-identity.md)。执行源为 `ef67425800ae9de626a7f8f48fd89deb125fbf0e4d6af72cf79741d1e254664e`；该步骤仅再生输入，不执行 surface F/J/root，也不是本新入口的科学返回。

| 实际输入证据 | 字节 | SHA256 |
|---|---:|---|
| `run05-actual-observation-carrier-restored/report.json` | 19691 | `926db461a4efce0fa40ab539b9df28143f8664cca25ec96e95ebe1d7aa83dcdf` |
| `run05-observations-restored.npz` | 227202 | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` |
| `material-envelope-carrier-binding.json` | 1537 | `aaa65a5ecac807e97cf771a08dd57d2ac26b48adf6acc9592025c0c706581c8e` |

本次实际新旧 cells、u 和六 Gauss 字逐字相同。整个当前 carrier 的 SHA 与旧 carrier 不同，所以 ready 显式提供 binding 文件，consumer 仍要重新 hash 并完整读取两个实际 NPZ；不会因上表或 producer 的 `true` 而跳过读取。旧字的真实恢复也没有恢复或伪造 seed19 的旧 protected 升级顺序。

完整 ready 使用 `{work}/run05-actual-observation-carrier-restored/material-envelope-carrier-binding.json`。初始参考、carrier、preparation 与 node/scalar 路径均使用当前 run07 的实际文件，source/model/target 在运行时按它们重新严格绑定；不把旧 reference SHA 填成当前。

科学步仍为完整新场 1 个 metric 方向、每方向最多 16 个 QP advances，另保 4 个 restoration 方向、每个最多 64 advances；15 次原线搜索、原 mu=.01、jet-sum 范数 .05/24、N2048、M160、共同 normal32、原 endpoint 和 implicit 预算都不改。seed 径向积分阶数明确为 8，中央每片 16，完整 12 片及 lambda 的原 `(0,pi)` 数值定义保留。近活动新 cap 为 32，不限制永久 typed 分离数。完整参数逐个载于 ready，本文数字不是参数的替代品。

独立 fresh 输出目录为 `reference-centred-c1-material-envelope-normal-lift-first`。纯读数器的 parent bundle 用当前已存在 reference，而非可能因真实失败未生成的 final。纯读会逐项输出 actual false/null/错误；只有实际 complete 报告才启用 final bundle 核验。所有 summary 均为具体标量 dot-path；不把整个 directions、metadata 或原数组列入公开摘要。

## 10. 新发现的 sixjet 诊断接口遗漏

本次完整 grid 接线静态审发现：真实 a62c `fields_torch` 返回六个物理 jet，以及 `rho0`、`closure_delta` 和 `centered_closure_residual`。其旧 geometry 验证器只列前两个诊断，因而尚未运行的旧 cached/plain 入口在遇到这个额外 key 时会拒绝。

独立新包络 geometry 明确添加第三个诊断的接受范围，并逐项核它是实际角块 `(A,3)`、全有限；三个诊断均不计作 sixjet，也不放开任意未知 extra。`point_fields` 仍只返回原六物理键，完整 point VJP 不变。这个改动是新 geometry 的实际源码差异；没有改已锁 a62c/3531 历史，没有虚报一个尚未发生的科学失败。

## 11. 完整锁定来源及复现

| 完整文件 | 字节 | SHA256 |
|---|---:|---|
| `complete_material_envelope_memory.py` | 40091 | `c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152` |
| `complete_material_envelope_rows.py` | 13744 | `729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7` |
| `so3_reference_centred_c1_material_envelope_geometry.py` | 65678 | `bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f` |
| `fullclosed_reference_centred_c1_material_envelope_so3_qp.py` | 68070 | `cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5` |
| `launch_reference_centred_c1_material_envelope_so3_actions.py` | 17931 | `b93af9809adaf42a3eee9328c6ca857156c38609f40db975a92c3bea5f5af991` |
| `read_reference_centred_c1_material_envelope_so3_report.py` | 86230 | `104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7` |
| `derive_reference_centred_material_envelope_entry.py` | 38063 | `56d5b7d9b58902cfb413ba1d2c306d7f54a52e401ac27bdf1f0e3547fe120263` |
| `reference-centred-c1-material-envelope-normal-run07-ready.json` | 47633 | `a948584e5cf21be77c4a1334a4af29dddc436cbad3b9249dd8abf0af88ac111f` |

新科学 entry 的完整 source role 表和 ready 的完整 source map 还保所有其余实际依赖，包含原 192 selector、旧 point/cotangent、完整谱损失和 Hessian、原全部 H² 范数、QP v3、真实 history walker、完整 fixed seed/base/normal/calibration/C1 来源。完整派生器直接重建三份正文并核上表的预期 SHA，不靠小补丁冒完整体。

从已刊 checkout 纯源码复现到一个外部 scratch 目录的命令为：

```bash
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/derive_reference_centred_material_envelope_entry.py \
  --repo /absolute/current/checkout \
  --dependencies-directory /absolute/current/checkout/topics/visible-flex-larger-amplitude/scripts/resume_20261126 \
  --outdir /absolute/scratch/material-envelope-regenerated
```

再次加入 `--verify-existing` 即逐字核完整三体与 ready，不执行任何科学模块。默认 parent 来源是公开 f075 driver、509d launcher 和修正后的 3803 reader，完整原参数是 02a6 ready；缺失或任何完整 SHA 不符都会停止。solver 的独立完整三依赖派生器另保其自身全部原源和所有新正文，不由本入口忽略其科学内容。

后续若运行实际 direct/new field 发现新的地址，仍须由真实完整报告或独立经核的地址闭包加入下一入口，不能把本包络政策当任意未来地址已付。detached stage-matrix cache 目前没有接入本 entry；这里仅保已刊 ba3d frame C1/value 两层，不能把未实现的后继省工计入成本或成果。


### 交付前的独立 pure revision2

独立审查确认实际 scan 与 rows 字段闭包后，再将每个 scan 的完整政策 definition/hash 以及每个行状态的政策 identity 显式要求等于本 report 的已绑定政策。这两处仅收紧纯读数来源归因，拒绝把同一 consumer 下另一 cap 的合法记录混入本报告。driver、launcher、三依赖及全部科学参数逐字不变。原未运行的 df97 reader、7e18 deriver、ff358 ready 和 26cf 说明留在初稿 scratch 身份下；本表给出最终 revision2。没有科学失败或科学重跑。

## 12. root 完整复核及本次实际队列准入

root 从完整 56d5 派生器独立纯文本再生三份正文和 ready，四个完整 SHA 与第11节逐字相同；34 个来源（30 个 runtime role 加三入口与派生器）均核实际完整文件。与 02a6 完整原参数逐项相比，只改 fresh 输出路径、明确采用当前真实 manifest、实际 binding 路径和新 near-active=32；其余全部原数值参数相同。没有执行本地科学或 fixture。

本提交将 ready 的两个完整步骤追加至仍 finish_when_done=false 的公开 run07 动态队列：`complete-material-envelope-cached-normal-first-20261126-07` 和 `actual-material-envelope-cached-normal-first-20261126-07`。这代表已准入；实际启动、完成、候选、缓存命中与残差须由 run45909290354/1 后续真实返回另记，本文不预填。此前 ready 中 executed/admitted=false 是冻结交付时状态，不覆盖本次准入事实。必要旧载体恢复已实际完成，此新消费者仍独立重核完整字节和来源。

旧4d9的地址去重按 numeric tuple，signed-zero字由原walker的幸存记录决定；本文新hex身份只在该实际消费集合之后建立，不倒称旧walker曾逐hex去重。修订的全05来源证明与完整原e54三集合指纹一起保存。连续metric、reach及真实加密仍未付。
