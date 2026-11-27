# Run10：用不可写字节所有者绑定完整当前点，保留完整原方程与历史

## 1. 本次实际修改与执行边界

本交付是完整独立运行源码及完整参数方案。没有执行新的场、根、积分、J、J*、QP、科学数组例子或局部 fixture；没有运行本地 Python AST/compile。已在 JavaScript 中对 15 个完整来源进行全文正向与反向字面重放，并核验全部输出 SHA256。这些重放仅处理来源文本。

改动针对已刊完整 `same_chain_detached_closure_values.py`（e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e）中 `CompleteClosureValueScope.key` 的一个具体操作：每次可缓存请求都把完整当前自由点转成一个新的 bytes，再与入口保存的完整字节比较。原点维数为 1,333,370，所以该调用产生的完整点字节长度为 10,666,960；这只是源码和维数给出的单次长度，不是测得的内存带宽或用时。

新的完整 normal 仅把 `_select_point` 保存当前点的方式改成不可写 bytes 所有者。新 helper 在每个可缓存 key 中检查同一个 ndarray、同一个 bytes 所有者、同一完整布局及当前点身份。完整点词仍在可缓存作用域的入口与出口读取。所有数据 tensor/version、全部 controls 各角 jet 的完整词检查保留。

不从原运行时间或计数宣称速度。既有 `binding_and_key_seconds`、`original_closure_seconds` 和完整计数会在新的真实 Actions 返回中如实记录；这次还把已有计时标量加入可配置的活进度摘录。活进度仍不是 immutable 科学输入，也不代表接受、驻点、最终场或连续认证。

## 2. 完整真实来源与固定输入

原完整父链为：

- driver `fullclosed_run10_detached_closure_so3_qp.py`：`c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1`；
- pure reader `read_run10_detached_closure_so3_report.py`：`2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e`；
- normal `so3_reference_centred_closure_values_normal_lift_operator.py`：`6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4`；
- closure helper `same_chain_detached_closure_values.py`：`e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e`；
- unchanged meridian base：`6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865`；
- unchanged actual run10 memory：`f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba`。

已真实冻结的 run10 输入身份不变：

| 项目 | 完整身份 |
| --- | --- |
| actual run | 45972294636/1 |
| complete target identity | `e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049` |
| actual reference model | `081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5` |
| whole immutable binding | `4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf`，430908 bytes |
| fixed chart | `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` |
| actual current scalar table | 2218 leaves；完整原 metadata 与六真实文件仍由原 binding 核验 |
| historical restored carrier | 旧 run05 的完整 dc5 carrier；2397 是该历史再生的责任，不冒当前 scalar table |

没有从缓存检查方式推定另一 runner 的输入相同。这里仍严格采用原 run10 已绑定的完整 reference、scalar、chart、节点、carrier、两组支持、18 个 literal Q 词和冻结 seed。历史 `same_mathematical_g_claimed=False` 字段仍描述其原来源关系；本次同 run10 父子关系另外通过完整模型剥除明确工作来源字段后的逐对象相等核验，不能用一个历史 false 标志替代实际关系判定。

## 3. 当前点的原读写路径已逐体定位

在原 6d2 normal 的完整文件中，`_current_x` 只有两个赋值位置：构造时置 None，及 `_select_point` 实际选择新点时 `value.copy()`。原 base 没有 `_current_x` 字段读写。实际下游消费者包括：

1. detached closure scope：读取对象、当前点摘要及完整点词；
2. detached stage-matrix scope：读取点对象、完整词与 array SHA；没有写回；
3. adjacent-frame provenance：读取完整点 array SHA；没有写回；
4. immutable root-packet recorder：读取/复制完整点并核验摘要、写 runner NPZ；没有写回。

新完整 normal 保留原选择逻辑、finite/shape 检查、`np.array_equal` 判定、`array_sha(value)`、root/residual/failure/batch 清理及 calibration 点切换，唯一替换为：

```python
self._current_x = np.frombuffer(value.tobytes(order='C'), dtype=np.float64)
```

没有把只调用 `setflags(write=False)` 的拥有可写分配的 ndarray 当成不可变数据。这里真正的存储所有者是 exact built-in `bytes`；数组是对该只读缓冲区的直接 view，不能在 NumPy 的合法写接口中把该底层 owner 改成可写分配。

原 `np.array_equal` 对已选点的判定（包括原来对符号零的数值相等处理）没有改；没有借此新增重选点或清空旧历史的规则。只有原代码本来会保存新点时，才生成新的完整 bytes。各式实际求值继续接收原 `x` 或原 active tensor，点身份快照不是一个新的 active 参数对象。

## 4. 不可写 owner 的完整局部合同

新 `_immutable_point_owner` 不扫描或复制点词。它要求：

- `type(value) is np.ndarray`；
- `type(value.base) is bytes`；
- native float64，shape 恰 `(q.free_size,)`，ndim 为 1；
- stride 恰为一个 float64 的长度，C contiguous；
- `writeable=False` 且 `owndata=False`；
- 完整 owner 长度与数组 nbytes 均为 `8*q.free_size`；
- 作用域开始后，每次都是同一个 exact bytes 对象。

完整连续数组长度已占满整个 owner。非零正 offset 将要求超过这个 owner 的字节，负 stride 已被 stride 检查拒绝；因此不是把 owner 的另一子段冒同一完整点。任意新的 view、改 shape/dtype/stride、换 owner、替换当前数组、改变当前点摘要，都不能通过同一作用域 key 的要求。只读 memoryview、ndarray subclass、可写 ndarray owner 或可撤销的 flags 方案均不满足该合同。

`CompleteClosureValueScope._point_binding` 另要求：

```python
q._current_x is self.point_object
q._current_point_sha256 == self.point_identity
```

入口保留该 bytes 所有者的强引用。每 key 无需对完整点重新做 hash，也不把一次 metadata 检查记作整词读回。

### 4.1 完整词责任没有转移给 metadata

原可缓存 scope 入口仍通过原 `_float_array_words` 读取完整点词，并要求该完整结果等于完整 owner bytes。出口仍读取完整点，比较入口完整词与 owner 完整词；原完整 data 的 version/token、数据词摘要及 physical carrier 复读一并保留。原 optional cache 不可用路径仍走原完整公式，失败/异常照实记录。

新 key 的其它部分保持原体：同一个 data、同作用域、合法请求 order、完整 data token、完整 carrier、全部 six-control angular slots 的 shape/stride/storage offset 与全部 binary64 词。并非只绑定 `u0`；传入的 `u0/u1/u2` 槽存在几个就完整消费几个，order 另在 key 中。完整 named data 的递归 tensor/version 责任未删除。

### 4.2 在完整原数值公式上的等价范围

固定一个原来可缓存的 scope。令 $P$ 为入口已保存的完整点词，$O$ 为同一 immutable bytes owner，$D$ 为原 bound data token，$U$ 为全部实际 control 词。入口实际验证 $P=O$。合法 Python/NumPy 读写语义及所核完整来源保证 $O$ 在其生命周期不变。每个 eligible key 再核同数组、同 owner、同完整布局和点摘要，故该时刻数组仍表示 $P$。原 data/version 与全部 $U$ key 同时核验。

因此新 metadata/owner 检查所允许复用的点状态，仍是原完整点词检查所要求的那个状态。复用的仍仅是先前原完整 closure formula 已返回的全部 $C$ angular jets，返回时仍 clone；没有从一个 scalar 或省略分量重造完整 closure。

这说明本次没有修改闭合方程、控制、自由量、积分范围或选择分支政策。它不宣称一次未执行的新多线程浮点评价必然逐位相同，也不把来源推导当速度、root error、全角唯一性或几何证书。

## 5. active / transformed 路径与强制原式重读

原 `_environment_reason` 和 `_plain_tensor` 整体保留。进入 no_grad 之前捕获 caller tracking；reverse grad、inference、forward dual、functorch、functional tensor、compile/JIT、dispatch/function mode、autocast 或探针未知，都继续旁路缓存。只看到 `torch.no_grad()` 从不构成允许复用的充分条件。

完整 active J/J*、上游 normal frame、初零目标、core/H、所有自由 omega 仍由原路径求值。没有 detach 原 active 图，也没有用缓存点替换其自变量。

原每个正常段完成后的 `original_stage_residual_reread` 及最终 `original_final_endpoint_reread` 都继续显式调用原完整积分公式。`_request` 的 forced 分支没有查缓存。完整 32 段、所有 tau、Newton/Armijo、domain、容差、角 jet solve、stage matrix、完整 trace、原最终 endpoint read 保留。

文本复核结果：normal 中 53 个缩进函数段的顺序和数量全保；除 `_select_point` 外其余 52 段逐字相等。整个 `_run_chain`、`_get_roots`、`_implicit_jet_value`、`fields_torch`、J/J*、save/load 的正文均未改。旧 protected/typed/history 与选择行逻辑不会通过这项存储修改被重新定义。

## 6. 计数和时长必须按真实工作解释

新 helper 保留原全部 34 个计数键，并新增 6 个键：

| 计数 | 本新来源的实际含义 |
| --- | --- |
| point_word_checks | scope 入口/出口实际完整点词读取的尝试数；不再把 metadata key 检查算进这里 |
| point_entry_word_checks | 完整入口点词读取尝试数 |
| point_exit_word_checks | 完整出口点词读取尝试数 |
| immutable_point_binding_checks | 实际 immutable owner/布局/点身份检查总数 |
| immutable_point_entry_checks | 入口 immutable binding 检查数 |
| immutable_point_key_checks | 每个 eligible key 的 immutable binding 检查数 |
| immutable_point_exit_checks | 出口 immutable binding 检查数 |

纯 reader 要求：

$$
\mathrm{point\_word\_checks}
 =\mathrm{point\_entry\_word\_checks}
 +\mathrm{point\_exit\_word\_checks},
$$

并要求 immutable 总数等于其 entry/key/exit 三数之和；各计数必须非负整数，入口/出口不能超过真实 scope 数，key 检查不能超过真实 key 请求数。原 started/returned/failed、实际 in-flight、original/cache/forced costs 闭包继续保留。

不能将新 `immutable_point_key_checks` 和旧 e1af 的 `point_word_checks` 直接拼成“同一种整词检查”。完整 definition 和 pure 返回明确标注两个作用域。原 source 的统计不回写、不改标签。

原时间 `binding_and_key_seconds` 包括 key 生成及其原计时范围内的检查；新过程仍按同围栏计时。它不是整个 solver 的性能结论。活进度发布只新增原式时长和 key 时长两个已有标量。完整原始 progress 文件也保留已关闭 scope 时长；公开 selector 不选择它，scope 在运行中时不把尚未结算的 scope 时间补成已完成。所有 mutable progress 的成功推断标志仍为 False。

## 7. 完整 source 家族与最少必要依赖变化

本次 15 个新运行体如下。其余通用完整来源直接复用原已刊文件；不会把它们改名以假称新算法。

| 完整文件 | bytes | SHA256 |
| --- | ---: | --- |
| immutable_point_detached_closure_values.py | 59041 | `2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb` |
| analytic_local_stage_jacobian_immutable_point.py | 25732 | `21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024` |
| analytic_normal_frame_jets_immutable_point.py | 47279 | `4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa` |
| normal_frame_c1_immutable_point.py | 37361 | `53b5bc456cb3f62c6a25d329de54920253d9193168ef3fb761198ff61fa0822d` |
| detached_stage_matrices_immutable_point.py | 47791 | `a41872f7563683b28d34cb9da35d7fc3bd0879fb5a8d1d183230a518f6b8f052` |
| adjacent_normal_matrices_immutable_point.py | 36766 | `ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59` |
| reference_centred_immutable_point_calibration.py | 11905 | `794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238` |
| so3_reference_centred_immutable_point_normal_lift_operator.py | 98473 | `9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6` |
| immutable_point_normal_root_packets.py | 71680 | `b4c41b2dc8754607441c30cdb3a34199d7e40f8b52fc5e4a8f5d653ea524eac8` |
| run10_immutable_point_source_binding.py | 34790 | `85f3007a6927968eb253eab168e9379f9a1f732caf5aa43b9f24776f39606d97` |
| so3_run10_immutable_point_geometry.py | 70708 | `dbbd4601f4bbc0798759f3c63cd3caae3cfc19f1a62ec9dbd02cc6fbceb896ce` |
| transfer_run10_immutable_point_memory.py | 66265 | `0007abf0b2814b09a3ecc30f621cbd8814a3d94528c753762aa7be5175d08486` |
| fullclosed_run10_immutable_point_so3_qp.py | 87787 | `a7031dfa247dd98053692b356999104d3bebe7624c635e219a55ee8133ea8a65` |
| launch_run10_immutable_point_actions.py | 21785 | `668bf9170657ad6c8d3bb12fe90b688becbc2ab8c010134d430f84dd2ed072aa` |
| read_run10_immutable_point_so3_report.py | 97696 | `41a6e7c3149f493dcabea908574a8ca0ff031cf275e9aa471e4dcff7786c67f3` |

lower 9 体中，closure helper 和 normal 的明确 point-storage 段是实质修改；J3、六控制 frame、C1、detached/adjacent matrix、calibration 仅更新完整依赖 pin/schema。根包保留全部旧 registry，并加入真实新 normal/policy 来源；已有数组、requested/completed order、各段 provenance、QP/report hook 与 0 科学调用责任保持。

上层保留 unchanged f1c memory 和所有原 scan/row 数学。新的 geometry、binding、transfer、driver、launcher、reader 使用完整新来源。driver 的 `save_report` 起至 EOF 共 20121 bytes，全文 SHA256 为 `eb1d8813bd161358c451b06b47b570cdfdb9173b12f2661ee7ec37344dbf5254`，与原 c3dc 对应后缀逐字相等。没有改候选循环、完整 C、Phase I、真实 Phi、回溯或接受出口。

原完整 75 个来源 tuple 全部保留。新 driver 有 90 个 role：当前替换的 12 个来源以额外明确 parent role 保留旧完整文件，再保留旧 driver、reader、launcher。每个来源仍全文件 hash 核验，完整原 parent reader 可以读取自己的完整 75-role 家族，而不是借用新 source 身份。

## 8. 真正完整 c3dc 父的继承及一个具体纯接口修正

新的 `PARENT_FAMILIES` 明确增加原 c3dc driver、2efa reader、6d2 normal 和原 f1c memory。旧 run07/08/09 家族仍各自保留，不能冒充 current run10 target。

新 binding 对真正 6d2 父：

1. 核完整 c3dc 文件、唯一完整 literal SOURCE_PINS、全部 75 个文件与其 hash；
2. 核完整 dc3b 文件与原 `validate_current_model` 实函数来源，调用它核原完整旧模型/每个旧政策；
3. 新模型仍由完整新 `validate_current_model` 核验；
4. 两边仅剥除明确六工作政策、schema/source 及 calibration 两个来源字段；
5. 其余完整模型对象必须相等，包括 reference、base、scalar/chart、seed/Q、全部变量、支持与共同 normal partition。

父报告必须由其完整原 pure reader 先读；terminal 定义保持，进行中的 mutable/partial 报告不会变成一个已完成父。完整 final 还必须核所有 13 个 NPZ 成员、实际来源/model/policy、mesh、fixed core、全部 omega/core/H 字，重建原完整自由布局并核父最后真实点摘要。它不导入旧根、J、函数值、Phi、接受或几何证书。新场和 norm 都在新来源下重新真实读取。

完整历史仍走原 walker、全部显式保护角色、uncapped typed union 和每一旧 ordinal/first-discovery provenance。继承父的 unknown peer origin 整对象保留；后继同来源 restart 保留原已转移 initial typed prefix。旧未知角色没有被补成空或伪造等价。

静态核此此前未实际走通的父桥时，发现原 eca pure validator 要求键 `only_explicit_source_schema_and_matrix_working_policy_fields_changed`，而 dc3b 的完整模型比对实际返回键是 `only_explicit_source_schema_and_frame_matrix_working_policy_fields_changed`。新 transfer 仅将该取键对准实际完整比对结果。没有删除模型比对，也没有把此静态不符称为任何已发生运行的失败原因。

## 9. 两个完整参数方案；没有伪造未来父

以下两件是互斥的完整方案，不表示都应执行，也不表示已经准入：

- **独立方案**：`run10-immutable-point-independent-complete-ready.json`，91753 bytes，`9948e5db970cea85d7b176a14ec1dd8397c80a3b2bc90069f76ac14f1e938f0c`。保留原 149 个 argv token 的顺序，唯一原 token 路径变化为 fresh outdir；另加 4 个 token，明确 current run10 c3dc 仍是待真实合并的同 target peer。原 run07/08/09 全部 pending source 仍保。若执行，是从原冻结 reference 点开始的新工作算法分支，不是从当前未知点续算。
- **完整父方案**：`run10-immutable-point-complete-parent-complete-ready.json`，92231 bytes，`8cb06ff176d7bd06818bb4d0892bbf10769a9c7f2deacac5f9d2cbfec695b4e1`。只移除与 strict parent 互斥的 independent/pending 命令行入口，再加入 complete parent report、完整 final seed report/checkpoint 三对参数，合计 142 argv token。每一个数值、方程、空间、QP、线筛参数仍原样；原 unknown peer 义务来自实际父 report 的完整 provenance，而非被丢弃。

两个方案都明确 future report SHA、checkpoint SHA、full point SHA 为 null。路径仅表示实际消费位置。没有把现有活进度的 point digest 当 checkpoint，也没有制造“父已完成”标志。13-member final 没有真实返回时，完整父方案就没有合法输入；这不是新 fixture 或行政前门。

原 budget 为 1 个 metric direction、maxiter 16；4 个 restoration direction、各 maxiter 64；原 15 ray trials、192 原行前缀、full M160/J923/N2048、全部 mean/core/H、32 normal stages、所有几何门均保留。新输入模式不会暗增或缩减该 budget。原 explicit damping .01 仍是该预算参数，不冒继承尚未知的父末 damping。

两份都保留原 373 个 science 摘要、357 个 pure 摘要和 43 个 progress 摘要的每个原 key/value。增加 6 个实际计数后为 379/366（pure 再加 3 个口径标量），进度遵 controller 上限只增加 immutable entry/key/exit 三个计数与原 key/original 两个已有时长，合计 48；其余完整诊断仍保在自然返回报告。所有新增都是标量或口径短文，没有数组字符串公刊。cleanup patterns 只指向各自 fresh outdir，不能误清原 c3dc 父的行缓存。

## 10. 再生、核验及交付结论

完整两再生器：

- `derive_complete_immutable_point_normal_sources.py`：51478 bytes，`06f13531946f74d32686b2ba20f5d5f156951040116375153b824f5ebda1eb5e`；9 个完整 lower；
- `derive_run10_complete_immutable_point_entry.py`：50163 bytes，`7bdf92c3fb4e7e886320962f743acf9009283d6ff10b88cfc1a512a2c9420b7f`；6 个完整 upper。

每个再生器保留 parent 完整路径/SHA、全部字面替换 before/after/count、整个输出 SHA/bytes，并逆向复原完整原文件；不是省略函数体的补丁说明。仅读来源文本，没有科学 import，写已有不同内容会拒绝覆盖。它们是复现工具，不需要在真实科学入口前另跑一个数值 gate。

本次实际做完的是 JS 全文正/逆重放、完整来源依赖与调用边界静态核、全部原 selector/argv 差异核。没有声称本地 AST、科学正确性实验、实际缓存命中或速度测试已发生。真正的完整场与性能判断继续依据公开 Actions 的完整原预算返回。
