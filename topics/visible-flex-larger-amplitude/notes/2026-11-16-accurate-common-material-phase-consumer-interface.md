# R447：准确共同材料相位消费者接口

作者：ChatGPT /root/amplitude（AI 协作）。日期：2026-11-16。

本次交付独立条件证明和 requestless source/API；没有实际请求、父场选择或运行。原 R437/R441/R416、全部原 BVP／geometry 消费者和正在执行的 Request204 完全不改。只有 root 负责 Git 发布与未来调度。

## 1. 冻结文件与科学范围

| 文件 | bytes | SHA256 |
|---|---:|---|
| `results/R447-accurate-common-material-phase-and-strong-C2-continuity.md` | 18846 | `e24b6c26d9bae2effa18c54f4ba7e683ad428694df50300648a609679b717ae2` |
| `computations/geometry_20261116_current_C_common_material_phase.py` | 31871 | `305eaf50958788caa2a7d0174f361cb08d3cf47e08fd3a7c3f9b9c44292a4ab8` |

对应证明：[R447](../results/R447-accurate-common-material-phase-and-strong-C2-continuity.md)。前提和相位来源：[R443](../results/R443-common-material-angle-pullback-and-fixed-closed-target.md)。源码的完整数学正文在本新文件，未用修改旧模块的视图或隐式 monkey patch。

本题实际需要的是 $t\mapsto F_t\in C^2$ 强连续。证明使用原完整 $C^2$ 空间场、原准确材料严格正性及全接缝；没有新增时间二次可微门。更强的时间二次可微到空间 $C^2$ 所需 12 类 jet、当前材料角四阶与原完整接缝责任另列；本源码没有形成或计算那 12 类 jet。

## 2. 明确注册的当前来源

当前 loader 已真实产生一个准确 bundle 后，helper 直接消费该实际对象，不再造 accepted checkpoint 或重复求 BVP。

| family | 实际 accurate bundle schema | cut / saved-prefix / shared 源 SHA256 |
|---|---|---|
| `R416-original-resolution` | `R416-current-C-ten450-accurate-cut-atlas-field-v1` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` / `1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520` / `6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3` |
| `R441-current-resolution` | `R441-current-C-resolution450-accurate-cut-atlas-field-v1` | `8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52` / `fb6e181cd0ddfb34cc70c874c119ceb149850ce8756d1f2f0dd775175e99cffb` / `1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935` |

两族分别有自己的来源，不能沿旧名替换新 pin。实际共享的完整六 jet 解释器为 `geometry_20261115_shared_active_interval_balls.py`，SHA256 `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b`。helper 从真实对象的 `type(instance).__module__` 取得实际模块，再核真实 `__file__` 和 SHA；不会遍历 `sys.modules` 取同路径的第一个模块，从而混入不同类对象。

当前接口只注册原完整 112 core 两族。R447 纸证对一般有限 $M_j$ 的陈述不使 R442 或未来 loader 自动得到兼容；新增来源须有独立明确的全数据／对象身份分支。

## 3. 首图输入：读正文，不由 hash 恢复

首图取 R437 已真实生成的 `first-material-transport.json`，其 source 必须是

`geometry_20261116_current_C_ten450_closed_parameter_policy.py`

SHA256 `d7d01460f5a22f4fa2ca75ad36475688d65a465ba488d9caff65cb5ef13fb871`。

该实际记录的 schema 是 `R437-current-ten450-explicit-closed-parameter-policy-v1-actual-material-transport-record-v1`；要求 `initial_capture` 与 `definition_capture_complete` 为真。完整原 `complete112_material_definition` 含全部 112 little-endian binary64 词、准确二进有理词、频率 2..224、准确 density/sine 系数；helper 逐项按同一原有理解释核这些定义资料。原负零字词保留在来源，准确实函数中的正零／负零都表示同一个零，二者责任分开。

另外实际读取首 `plan.json` 和 `assembly.json`，分别与该记录的 `actual_shared_expression_files.plan/assembly` 按 bytes/SHA 绑定。允许调用者提供其当前真实路径，但内容必须就是原文件。不能从旧 SHA 造正文。

首 assembly 的 `large_core_prefix` 必须属于原 `1c7a2e1c...` saved-prefix，其 `complete_accepted_checkpoint` 对应首记录，原 `global_rho_lower_exact` 和 `material_circle_diffeomorphism_source` 给已付完整 R237 材料正性来源。首完整 registration、inlet normalization、mean/gauge 及 phase 与原记录逐 canonical 资料一致。

helper 不重读首 raw checkpoint、全部 B 节点或所有原 FFT 数组；这些原文件的身份仍在首记录中，未读项清楚标为 identity。它没有把首 A/B、首归一化或旧有限数值场换入当前场。当前实际完整 field 数据仍由已经执行的 R416/R441 loader 负责。

## 4. 当前对象与同目标绑定

公开入口：

```python
common = Common.bind_loaded_common_material(
    current,
    first_material_transport=actual_first_material_path,
    first_material_sha256=actual_first_material_sha256,
    first_plan=actual_first_plan_path,
    first_assembly=actual_first_assembly_path,
    budget_check=existing_owner.check,
)
definition = common.describe()
```

`current` 是已真实绑定的 R416 或 R441 `AccurateCutBundle`，含原 `source_bundle/field/target/model/Active/Background/binding`。helper 保留该七元组与实际对象关系，核真实 current cut/saved/shared/675 源；没有重新载入另一个同名对象。

本分支严格支持同 job：首记录和当前 checkpoint 的 run/source 都是当前环境的实际值。它沿现有 R437/R441 的同一 `current_target_identity` 和全部十 binary64 词；允许当前 core 不同，却不允许借坐标变化偷换准确 C/标量目标。若未来两个不同来源的 C 包围需用 R383 语义等价跨身份连接，应写独立来源分支；当前不把不同 `target_identity` 默认为相同，也不把来源不兼容标成 BVP 数学拒绝。

构造绑定逐词保首 W/H、所有 marker、原 cuff，包括中心、半径、幅值、所在侧、顺序和负零。源保持原完整相位词及两反射／原转轴。两份 registration 和两份 core 的差异只记录；不要求相等，不改变原 native/FD/fullDN/450 接受。

`describe()` 输出独立 schema `R447-current-C-accurate-common-material-phase-v1-definition`，包含真实源／输入身份、准确逆定义、caps 恒等、原接缝前提、强连续性范围、原完整证书条件转述及可选六 jet 已完成调用计数。它不消费一份原完整 metric/reach/held 结果，也不因此生成这些 passed 标志。

## 5. 准确相位与固定帽

令 $\Theta_j(q)=\Phi_j(2\pi q)$，$I_j$ 为其唯一准确实提升逆。共同首图上的准确活动族为

$$
\widetilde F_{j,t}(x,q)
=R_{\pi t/2}K_j\bigl(x,I_j(\Theta_0(q)-\pi t/2)\bigr).
$$

`K_j` 是当前自己的准确 R416/R441 表达，不是旧 R409 数值 renderer。当前 prefix 输入 $s_{{\rm numeric},j}=L_{{\rm numeric},j}u$，其他活动片用原 r。原 B、全物理模式、两 mean、registration 和 inlet normalization 均随当前准确场保留。

首共同 q 中一般不是 `q-alpha`，也不自动是 `q-alpha/(2*pi)`。材料角逆虽可不求数值近似，仍是准确场定义不可省略的一部分。

两帽维持原 $F_{\rm side}(x,y)=(x,y,\mathrm{side}(H+b_{\rm side}(x,y)))$。准确 T 在帽 Cartesian 图中恒等。平 cuff 上物理角移和旋转在整个重叠环准确抵消，从而和固定帽拼接。全部非对称、重叠、负幅 marker 都保；没有全闭目标旋转对称假设，也不把非线性角换元延伸穿过帽中心。

R417／R441 原帽 API 继续消费原 bundle 和真实 R413 attachment；本 helper 不重写帽 source，也不把活动片六 jet 当帽数据。帽完整 cover、normal、曲率和全 mixed-pair 责任保持原接口。

## 6. 可选完整闭 cell 六 jet API

当调用者确实需要共同图上的包围、网格或场值时，可调用：

```python
cell = common.evaluate_active_cell(
    piece_index=actual_piece_index,
    radial=(actual_left, actual_right),
    angular=(actual_q_left, actual_q_right),
    time_interval=(actual_t_left, actual_t_right),
    lower=actual_reflected_side,
    interval_bits=explicit_work_precision,
    max_inverse_steps=explicit_finite_work_count,
)
temporary_json_value = common.encode_active_cell(cell)
```

输入全为真实源／原调用者已选资源，没有默认未知父或未来参数。`piece_index` 指向实际完整 `current.field.pieces`。prefix 的 `radial` 明确是公共 u，其余是原 r；helper 核映回后仍在原闭片，保所有端点。`angular` 是首 q 的完整闭区间，`time_interval` 是原 $t\in[0,1]$，不是 alpha。`lower` 必须显式 bool。

返回全 `value,u,q,uu,uq,qq` 的 3 向量 Arb 包围，并给完整所用闭区间、原 piece 地址、原径向尺度、alpha 包围、逆像包围、两项材料链导数和完整来源身份。它没有判 native、merit、曲率或几何接受。`encode_active_cell` 只把这些实际值写成内存 JSON 值，不 print、拆分、上传或创建文件。

### 可选逆像的算法与诚实有限范围

1. 用全部准确 sine 系数的绝对和构成全实提升初始包含区间 $(Y+[-B_0,B_0])/(2\pi)$。
2. 用原已付 $\rho\ge\beta>0$ 和全部 density 的绝对和给全导数区间。
3. 每次以准确有理 c 为中心，用均值定理形成 $c+(Y-\Theta_j(c))/D$，与旧区间相交；只收缩有效包围。
4. 到显式有限次数或当前精度不再收缩就返回仍有效的完整包围；没有“逆宽度通过”门。全实提升保留，不按近似取模漏掉周期端点。
5. 对当前导数的全角局部区间与原严格正全局界作相交；若形成新的 ball 因舍入不能显式隔正，就保原已隔正全局 ball。不能取导数中点作分母。
6. 原 field 的准确三角表达本身对全实 q 提升有定义。helper 调用该完整准确表达，保全部角模式，不用浮点 inverse、重新 FFT、裁剪模态或旧节点采样代替。

整个 cell 查询包含给定的全部空间和时间区间。Arb 外包只是对准确逆与准确场的包围，不是有限 Newton/IEEE 程序的“准确导数”。提高此查询精度不会重新形成原 C 叶包围或当前 cut 系数；原包围仍按实际字段保留，它们宽时不能假称已由材料逆收窄。

## 7. 原钟、精度、异常与现场

helper 没有 CLI、没有子进程、没有文件输出／删除、没有自己的墙钟。所有绑定和计算仅允许在本公开仓库 Actions。宿主传原有 `budget_check`，它在绑定、每次逆像包含更新、原完整 field 调用之前／之后及序列化前执行；不接受任何数学 residual 来改变原门。

调用方仍负责原绝对 deadline、外层中断、逐 cell 未访范围和必要 readback。原 field 大调用中途被宿主停机时，本 helper 不把该 cell 伪记完成；异常原样向外，宿主记录未付。它不以返回“宽但有效”的逆像包围冒整个 field cover 已完成。

可选查询临时设置已有 `Active.ctx.prec`，`finally` 恢复先前精度；需由宿主串行调用这个共享 Arb 上下文，不能在同一进程对共享 precision 并发改值。原载入的准确 C/节点资料不修改。

第一份 material、plan、assembly 与当前 field 所需临时数据要保到消费者结束。若已删除，必须由新的实际流程真实重建；旧 SHA 不恢复 payload。本 helper 不转存大场到 Git，不为传输大资料创建编码分片。

该源没有独立 necessary stdout 协议。未来宿主只输出原单份 ≤90KB 的必要结论／source／调用范围，实际六 jet 及完整 cell 原件留在本次 Actions 临时现场；不把这些可重算大表添加到源码／proof。当前未预留新请求或虚构计划数值。

## 8. 结构定理可以直接消费，数值逆不是第二次门

准确的 $T_j$ 由已付正材料图唯一确定。对同目标完整 $g_j$，$T_j^*g_j=g_0$ 是准确恒等式。若原当前准确场已有完整 Loewner 合同，它经合同变换保持原 eta；不需要为了这条恒等式再扫一遍数值逆或收紧 eta。

同理，真实全闭图册和原 $C^2$ 场结构已成立时，固定 j 的全时间强 $C^2$ 连续来自紧集上联合连续，不依赖每 cell 逆像宽度。实际六 jet 查询是可用消费者，不是给原 solver 或已证结构新设审核门。

相对地，本文不从 loader 成功或材料正性推出嵌入/reach/held，也不借相位零局部 cover 支付全 t mixed pairs。首/当前 A、B、登记、归一化可以不同；重参数化不会证明它们的场误差很小。跨精化层的统一逆导数、同 g 的真实误差下降、全 t C² 收敛和原 native／全闭消费者仍各自未付。

## 9. 更强时间性质的单独接口责任

源码 `STRONGER_JETS` 明列 12 对 `(a,b)`：$0\le a\le2,0\le b\le4-a$。这只是将来时间二次可微到空间 C² 所需原场 jet 索引，不是已有数值输出。

若实际扩展此更强 API，必须在当前准确表达上形成全部 12 个 3 向量 jet，保当前角至四阶、首角至二阶、全部 Faà di Bruno 项、每阶 prefix 长度因子、精确两反射和全原接缝。不能把 675 的六槽重命名为这些高阶量，不能把非线性逆后表达投影回旧有限频带。固定帽时间导数为零，无需因此要求它先空间 C⁴。

本次没有实现更强高 jet 查询，也没有任何实际高 jet 调用或数值包围。题 README 第 1 条仍只按已证强连续性范围解释。

## 10. 源码检查与交付

只做原源码全文／字段读取、条件纸证、独立文本编写及 bytes/SHA 记录。没有导入 helper／科学模块，没有 AST、编译、测试、fixture、区间或场计算。现有 helper 尚未在实际场上调用，接口完整不等于已执行。

本文§1列proof/source的完整冻结身份，三件原始publication manifest仅作暂存字节清单；root已全文阅读三件并单独发布。无新request/workflow或实际科学调用；未来实际调用的源码、参数、现场、原钟和原完整终门由其独立入口明确绑定。
