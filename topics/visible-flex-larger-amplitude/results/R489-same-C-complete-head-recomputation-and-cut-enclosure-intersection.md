# R489 — 同一准确 C 的完整头部重积分与 cut 三叶包围相交

作者：geometry agent（AI）。日期：2026-11-16。

**可信度：已证明（限下述条件命题）；已写独立来源实现，尚未科学执行。** 不存在本项实际输入、运行、accepted 场、新包围数值或严格收紧结果。本文不修改当前 209、212、214，也不增添 BVP、native 或闭面验收门。

本结果补的是 R426 明示的来源缺口：R426 的 live query 继续使用原1440片累计径向端点，不能靠更深逆像分裂重新计算这些既定端点。这里复用原 f12f 完整生产器，真正重新求原全头六 primitive 和相同查询，再调用原完整 cut 叶读取器。没有另写积分核、根选择器、任意精化 oracle 或新的 field 定义。

## 489.1 固定模型及既有结论

原模型仍是 `R286-original-stored-continuous-model-convention-C-v1`。其实际输入包含完整160条 shallow 表、准确解释为 dyadic 的原 alpha/R、原 global lambda、全部 cap/flat/weight 参数、物理 cut/cuff 及原定义源码。依 R286，深尾保所有许可原精确根序列；不借旧有限选择器、R26 数值证书或任意盒中点选一个根。

以下三份原生产/生命周期源保持原字节：

| 作用 | 真实源码 | SHA256 |
|---|---|---|
| 全1440片与六 primitive、原查询 | `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| 原点 query 全部叶的 E/E_r/E_rr hull | `geometry_20261115_stored_C_v3_cut_twojet_readout.py` | `1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed` |
| 自有子进程组与真实 quiet | `geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py` | `5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95` |

原 f12f 自己继续核9aa0/0040祖先、原公式源码、R286证明、三原输入及 query recipe。本文不把三个直接文件说成全部递归依赖。

R306 的完整 cap 端点 primitive、原 Acb fallback、全闭分支和六分量 full-width 工作目标全部沿用。[R352 §352.9] 已区分共享依赖宽度与固定输入叶盒；[R383 命题383.1] 已区分同数学定义与运行/provenance；本文只接原完整生产路径及包围交，不重复这些定理。

## 489.2 同输入命题及实际核对边界

设 $\Omega$ 为同一原 C 许可根序列族。对 $\omega\in\Omega$，用 $r_\omega$、$w_\omega$、$E_\omega=1+w_\omega^2$ 记原准确定义。改变工作精度、积分目标、细分深度、计数或时间预算，不改变这些函数。

**命题489.1。** 若两次生产均使用同一原 f12f 源，五个原输入角色（config、ledger-ready、stored-ready、query recipe、R286 proof）的实际字节相同，全部非工作 input-binding 字段相同，且 `deep_definition` 均为 `original-exact-root-family`，则两次生产的每个原六 primitive、自然外端、原闭查询及 cut 三 jet，具有相同的准确语义和同一许可根量词。

**证明。** 完整 shallow 表、global lambda、所有几何/权重/截断常量及定义源码相同，所以每个 n159..0/j0..8 分片中的准确实表达相同。原生产器按相同顺序连接这些1440片，三原输入所定义的内端及全部深尾族也相同。六 primitive 是这些同一实表达的同一积分；自然外端由同一径向积分与内端决定。query recipe 相同，使每个准确闭径向集合、原 binary cut、端点闭合属性及顺序相同。对任何固定 $\omega$，两次生产所包围的准确函数、积分和导数因而相同。工作参数只改变向外求值与停止位置，不进入这个数学定义。证毕。

实现的 `semantic_bindings` 不只比较一个历史 fingerprint。它要求两份 input-binding 的完整 key 集相同；仅剔除 `runtime` 和 `work_parameters` 两段后，用保持 JSON 有符号零的 canonical 字节逐字比较所有余下字段。work 中 `deep_definition` 单独固定，实际变化只允许原十一工作字段。runtime 的真实两份记录照存，不把运行库记录假充数学输入相等的证明。新增未知非工作字段不会被一个旧白名单静默忽略。

这项来源相等是使用两个包围指向同一对象的必要合同，不是新增求解成功阈值。源、输入或语义不同就不得把包围相交后标签成同 C；该情况不推出原数学问题无解。

## 489.3 为什么重新积分确实更新累计端点

原 f12f `build_head` 从相同内端起，逐原 source piece 调 `SixPrimitiveIntegrator.integrate`，保所有已接受 primitive panel。一个完整 panel 上的径向增量为

$$\Delta r\in I_A+\lambda I_B,$$

并与同一整片的正径向速度范围积分求交。随后由真实上一个累计包围形成下一个端点。最终完整头还用全六积分的 A/B 总和重新形成自然外端的另一包围并求交。

R489 的子进程使用新输出目录和全部原参数名调用原 `main`；它没有把 R426 的已存累计端点作为这次头部的初值。因而本次1440分片、所有 accepted panels、全头总和、自然外端及新查询各有真实新 ledger。较高精度或较紧积分工作目标可以重新支付这些求值责任；本文不保证结果比旧界窄。

部分 piece 不能越过未付区间继续构造假外端。该规则仍由原 `build_head` 执行：保当前已付前缀、全部六前缀积分、实际 pending panels 和未访原片后缀。外部停止若发生在原生产器最终 result 写成之前，本组件不从残存几行 ledger 推导已付完整头，只保实际原件身份、完整新责任未付和旧界仍在。

## 489.4 原查询与完整 cut 三叶

原 `QueryCover` 对每个可能逆像分片只在严格向外半径排除时删除。闭二分保父片的整个并集；资源停保剩余完整粗父；深尾保持统一全根族解析包围。因此，原查询 `complete_closed_domain_bound` 与其 `work_resolution_complete` 必须分责：前者可以在后者为 false 时成立。

R489 不增加“达到 value-width 才读取”的门。它对实际返回的原新 result 调用1c39，1c39重新核原 config 的 binary cut、自然域包含、完整 point leaf span、完整原叶流身份与全部 E/E_r/E_rr 行，然后作原完整 hull。

这里保两个准确限制：

- 原 f12f 查询的工作宽目标只针对 E，**没有新增 E_r/E_rr 宽度目标**。即使完整 cut 三叶存在，也不能由 E 工作完成推出两个导数已达到某精度。
- 自然 $R_{\rm out}$ 不被改成 nominal binary cut；同一原 cut 的自然域包含必须仍由实际新 result/reader支付。

新头没有完整结果、新查询未返回或三叶条件未付时，新 cut 包围保持 null/未付；不取原数值点代填。旧完整包围不因此撤销。

## 489.5 同语义包围相交

**命题489.2。** 固定命题489.1的同一 $\Omega$。设原、新两个完整结果分别给准确量 $X(\omega)$ 的包围 $I_0,I_1$，即对每个 $\omega\in\Omega$ 都有 $X(\omega)\in I_0\cap I_1$。则

$$I_\cap=[\max(\underline I_0,\underline I_1),\min(\overline I_0,\overline I_1)]$$

仍包围每一个相同允许根选择的准确量，且宽度不大于任一原界。

**证明。** 对任意固定 $\omega$，两个原下端均不大于 $X(\omega)$，两个上端均不小于它。因此上述最大下端与最小上端仍夹住同一个 $X(\omega)$。端点排序给宽度结论。证毕。

实现只用实际原 dyadic 端点的准确有理比较，不用显示小数或盒中点。它分别作用于：

1. 两份完整 cut 读取已付时的 E0、E1、E2；
2. 两份完整自然外端；
3. 两份完整 finite-head 六积分及 full-deep-plus-head 六积分，全部六槽原名保留。

若旧 cut 未完整而新 cut 完整，只返回新完整三叶，不虚构旧界参加相交。空交被记录为来源/计算不一致，不能解释为目标反证后任意选择其中一边。

对三个叶分别相交仍是一个外包盒：同一个 $\omega$ 的三量均在其中。这不声称盒中每个独立组合都来自某一共同准确 C 实例，也不选择一个共同 midpoint realization。原真实联合依赖可能比盒更小，当前相交不会凭空支付这种依赖表示。

## 489.6 更紧包围不改变目标，也不自动接好旧消费者

真实准确 C、core/DAG、十参数和首材料/完整 construction 不变时，得到一个更窄有效外包不改变真实函数。这一点与 R383 相同。可是当前 R400 `AccurateTenTarget` 从其实际 definition 的 `actual_enclosure_leaves` 读叶，R416 的准确 patch也以该对象形成系数；来源 JSON 的新字节不能覆盖成原 definition 的 SHA。

因此本实现只产生独立 `same-C-refined-enclosures.json`，包括完整旧新来源、准确三叶交以及原自然端/六积分交。它**不改**原 CP、factory result、definition、已接受参数、shadow、native rows、H/J 或原 field，也不声称下游已消费新叶。未来薄 consumer应保原 CP/definition，在命题489.1的完整绑定下重新包围同一 DAG/同一准确 patch，单列实际新叶 provider。当前源码明确 `downstream_R400_R416_refined_leaf_consumer_registered=false`。

即使两份输入相同，更多积分位数也不保证任意小的全族宽度：深族的真变化、解析 majorant松弛、原固定字词、天然区间相关性及实际场误差分别保留。这里尤其不把 cut 盒变窄解释为 solver residual 降低，或把 native $2\times10^{-9}$ 改称全闭域 metric floor。[R352 §352.9；R426 §426.10；R459 §459.8]

## 489.7 原钟、所有权与 partial

此最薄实现显式注册实际 `actual202205` 的56cb driver、227e launcher和 `request205-owned-job-science-deadline-v1`。214/212等运行虽有不同外层实验号，只要其原真实内部 launch仍属于该未改来源，读取的是本次实际 run/source 的 launch及其实际 deadline receipt，不读一个未生成的未来父，也不凭 namespace 文件模板替代已绑定 deadline。

总 scientific end仍为原 namespace start加18900秒，原 readback end仍加2700秒。新的完整 phase预算是子额度，取较早的绝对终点；绑定、子进程和末包围形成均消耗该额度。开始 head之前预留声明的 cut-readout 与 shutdown资源。原 f12f内部预算仍按其原起点；真实外层 child wall额度另外包括其启动/输入绑定，因此不伪称两者起点相同。

两子进程用 `start_new_session=True`，直接复用冻结5bb2的 `OwnedChild`。TERM/INT记原信号，不在 Popen与 owner赋值间抛异步异常；实际已观测PID/start_ticks成员按原TERM→KILL/reap处理。共享 runner PGID从不当作独占科学组。任何未静止/身份冲突都保留，不能写完整清理marker。

readback只核真实已返回文件/完整ledger字节与行数、原查询对象、错误和owner状态；不重算科学。结果仍区分新head完成、新cut完成、同语义相交已形成、完整必要读回、owner静止和下游场/metric未付。只有必要正文完整且真实quiet时写readback marker；单正文超90000B诚实70、不分包，所有原件留同job临时。当前源码本身没有任何cleanup。

## 489.8 可执行结论及未执行边界

在命题的完整来源条件下，本结果给出真正更新全1440片累计径向包围的原生产入口、完整点叶读取、原六积分/自然外端/cut三jet的合法交与其真实同job生命周期。它补R426未重积分的一层，仍保原全部深根族与闭域责任。

尚未选择未来工作参数或运行；未得到更窄区间、accepted450、metric序列、reach、held、精确解存在性或README最终完成。新的来源组件可以独立接入后续明确请求，不能把其未执行当作另一条BVP必须等待的门。
