# 完整材料包络参考节点：不可变工作字与全部准确输入费用

**状态：完整源接口/数学责任设计；未运行科学计算，未宣称已有场或费用完成。**

本入口继续已经公开的全部实际均值批次费用链，目标是支付同一固定 supported smooth-triangle 参考切向量在完整有限查询集上的 $T,T_\phi,T_{\phi\phi},T_s$ 费用。它不更换固定标量度量，不更换全部变量，不选择几个方便节点充当全域结果。当前外层来源严格是 `cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5`，完整纯读取器是 `104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7`；后续不同来源需要独立适配，不能借本输入的标签通过。

## 1. 已存在的真实输入与不能继承的工作字

`0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b` 的完整 provider 会在报告的 `latest_operator_metadata.base_complete_metadata.fixed_supported_unit_seed` 中保存完整 `mean_batch_records`，并保存 `radial_plan.runner_raw_arrays`、`radial_plan.runner_raw_description`。前者完整记录每个成功批次的实际角字、全部均值/两阶角导数/振幅/完整 profile 矩工作字；后者完整记录边界与补集的全部正权节点、标量工作载体、截断函数、精确分段、数值宽度和物理求积权。报告、全部数组和 description 都必须按其原始 SHA256/bytes 实读，读取前后再核，不能只信路径或 count。

原 base `6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865` 的 `_parent` 只有对 integration/grid 的内部缓存；旧报告没有为每个四 jet 输出建立完整不可变查询台账。因此：

- 新生产器可以恢复上述真实、只读、同 seed 的完整 `_plan` 与成功角 `_mean_cache`，再由**原 provider 的原 `evaluate` 完整体**实际重读四 jet。
- 这次输出明确是新生产器的实际工作字。没有原始输出记录时，不能称它已证明与旧外层每次 F/J 所用的字逐位相同，也不能以同 NumPy 或同公式代替该证明。
- 恢复缓存不伪造旧计数，不重新求均值根；缺少成功角时明确列出缺口，不偷偷计算新根，也不以缺失为零。
- 新四 jet 的准确费用对同一个固定数学参考成立。要把它转给旧完整外层浮点链，还需单独的实际工作字关联；当前 $F$、normal-root、参考校准、完整积分和几何责任不会由这一步自动支付。

这些边界不要求暂停主求解。完整新节点记录也可直接作为后续明确消费它们的外层求解/认证输入。

## 2. 来源闭包

节点生产器固定使用：

| 角色 | 完整 SHA256 |
|---|---|
| 全批费用协调器 | `3feff893d09257748d153f0423e75d64eafe75777933ba85ee67611ce61cad6d` |
| 准确均值生产器 | `ce686a593cd81167167adfda966b423e2d95f1c9ce708f5d7252089baed24f1d` |
| 完整均值/profile/节点公式消费者 | `2859943d522cd764b686112acd0acdb065dc6a893625f4a8e237641caf041d36` |
| 原准确 reference | `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3` |
| 全域标量闭包 | `a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6` |
| 实际四 jet provider | `0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b` |
| 实际均值核 | `f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917` |
| 完整材料包络/历史消费者 | `c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152` |
| 原完整地点 walker | `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60` |

完整 actual report 和五输入（reference bundle、carrier、node report、scalar input、preparation report）按已刊完整 binder 再核。seed model、原固定 core/H、固定 chart、完整 scalar definition、source 全文 SHA、全部径向节点均不能改变。原报告失败时仍保持实际失败字段；没有首个完整场不妨碍处理已有成功参考批次，但不得写成场已存在。

## 3. 完整查询责任

查询计划由实际材料包络输入生成，完整保存原顺序/字：

1. 原历史与当前 carrier 的全部径向地址并集乘以全部 513 个 quarter 材料角。两 carrier 独立实读全部数组并复核 SHA；不因已公开“相同”字段免读。每个角是原公式 `binary64 pi*j/1024` 的字，并与报告中实际角数组摘要相等。
2. 原 11 个 P0 payload 以原完整 walker/精确原 carrier 重建；实际 prepared locations、所有 history source、原 actual report 的真实新地点及 typed diameter partner 全部合并。初始集合摘要与原 `known_explicit_history` 真核；未知保护排序不伪造。
3. 对每个所需材料角，全部 922 个径向胞的完整正 Gauss 积分节点均列入。完整 actual reference bundle 的首批 `cached_scalar_cells/local` 记录实际 preparation 的 Q 节点；provider 的原 radial plan 也保存 base Gauss 字。两者必须实际比较。新记录将完整写明选用哪一组实际工作字；旧 base 内部重新 `leggauss` 的未记录字不被自动断言相同。
4. 计划还包括实际报告中所有成功均值批次的全部角字，防止只处理 quarter-grid 而漏掉任意地点首次触发的角。

每个查询只有同一真实 `(cell,u_binary64_hex,phi_binary64_hex)`。有限集合可以去重，但不减掉任何责任；去重规则、原计数、唯一计数和完整数组摘要同时记录。不存在的成功均值角单列 `missing_completed_mean_angles`，完整计划仍保留该责任。时间预算自然返回时只记已完成不可变节点块，不把一块或一个批次称为全部查询完成。

## 4. 精确材料坐标与工作载体分开

原节点的准确 affine 二元组是 $(\lambda,\eta)$，表示

$$s=\lambda S+\eta.$$

对字面 $u$，先用 `Fraction(float.fromhex(u_hex))` 取得该 binary64 字所代表的准确有理数，再精确组合相邻两条符号节点。完整准确坐标为

$$s(u)=(1-u)(\lambda_j S+\eta_j)+u(\lambda_{j+1}S+\eta_{j+1}).$$

原 mesh、浮点宽度、浮点 $s$、profile/cutoff 的数值局部坐标均只作为**工作载体**单独保存。它们不代替准确 $S$、准确胞宽或上述 affine 式。新费用通过准确输出盒与完整实际四 jet 字的直接差支付工作归一化、trig、profile、多项式运算与所有坐标载体误差，不从单个打印 residual 推断这些费用。

## 5. 四个原参考 jet 的完整准确输入

准确生产器 `ce686.ActualMeanBatch` 已按原完整源构造 `ScalarWholeInterval`。对真实 affine 点可调用 `scalar.enclose(point,point)`，得到完整 $(b,c,b_s,c_s)$ 盒；该接口包含 prefix、analytic、全部 Hold、replacement anchor 和无限 R690 尾的完整分支。不能调用要求正宽度的 `width_box(point,point)`。

同一个 literal 材料角的完整 Fourier/trig 区间由 `actual.chart(phi_hex)` 提供：$e,e_1,e_2$ 是固定原 chart 的水平径向向量及两角导数，其中

$$e_1=\rho_0 e_t,\qquad e_2=\rho_{0,\phi}e_t-\rho_0^2e.$$

于是原参考四 jet 的准确盒按完整恒等式组装：

$$T_0=be+c e_z,\quad (T_0)_\phi=be_1,\quad (T_0)_{\phi\phi}=be_2,\quad (T_0)_s=b_se+c_s e_z.$$

$b\in[-1,1]$、$c\in[0,1]$ 只由已绑定完整标量律的已证结构取交，不使用浮点归一化来“补证”准确单位性。所有交界由原完整标量包围处理。

## 6. 支持分支、cutoff 与完整 profile

设支持区为 $[a,b]S$，单端层相对宽为 $\delta$。左端层 $\xi=(s/S-a)/\delta$，右端层 $\xi=(b-s/S)/\delta$。准确分支上

$$\chi=S_5(\xi),\qquad \chi_s=\pm\frac{30\xi^2(1-\xi)^2}{\delta S}.$$

`S5` 用单调端点求值；导数多项式在 $[0,1/2]$ 增、$[1/2,1]$ 减，其闭盒极值取两端并在包含时取 $1/2$，再除准确正 $S$ 盒。不能直接对未证明处于端层的工作坐标裁到 $[0,1]$。

若当前准确 $S$ 盒尚不能判定点位于哪条支持/central 边界，使用准确 $s/S$ 盒分别与**全部可能的 outside、两端层、central 区间**取非空交；逐分支计算完整四 jet，最后 componentwise hull。原参考标量盒可保守使用该同一真实点的全盒。每个可能分支和交片清单保留。这样没有用工作 region 标签回避未定边界，也没有把同一点换成别的场。

central 分支调用原 `285994.bound_reference_node` 与完整 `central_profile_enclosures`，后者保留 R711 全十二段并支付真实 physical length。端层用准确原参考四 jet、准确 $\chi,\chi_s$ 和完整准确 $d,d_\phi,d_{\phi\phi}$；outside 使用准确原参考。四 jet 全量比较原 provider 本次实际字，均无省略或默认零费用。

## 7. 全批费用输入与不可变节点块

已有全批协调器报告只作为完整 mean/profile 费用的来源。选用的每份 successful consumer 输出必须实际读取其 SHA，并经原全批 validator 核 actual report、原 batch index、全部角字、原 raw batch、完整 fee-request SHA/source。不能任意取一个角的外部 JSON 冒作准确均值。

节点记录按明确顺序分为自然大小的块。每块包含：完整查询数组、四 jet 原始 binary64 数组、provider/source/seed/actual report/原 mean batch/radial plan 的所有输入记录、原 `evaluate` 调用计数、读取前后身份、完整准确分支责任和四 jet 范数误差。大数组及逐节点数据只留 runner；公开报告只给来源、完整计数、预算/耗时、最大误差标量和 SHA。

实际完整实现不会为几百万个节点反复保存庞大的 Fraction 区间 JSON。逐节点完整准确式先全部计算，然后对每个 jet 的准确范数上界 $q\ge0$ 产生 binary64 载体 $v$；以 `Fraction(v)` **实际核 $v\ge q$**，不足则 `nextafter` 向正无穷推进，并拒绝非有限载体。每节点四个向上误差载体和四个原始工作向量均完整保存，所以可直接得到同节点准确向量的分量包围 $[\widehat T_i-v,\widehat T_i+v]$。这里 $v$ 是欧氏误差上界，分量包围随即成立；没有把普通 float 转换假设成向上舍入。

完整有理四 jet 公式、每条准确材料地址、原均值/profile 费用输入、所有准确 scalar/chart/cutoff 来源均可从保存的完整源和输入重新计算。全部节点准确输入描述按带长度的原顺序更新 SHA；真正跨可能分支的节点还保留完整交片说明。块内各 jet 的准确 Fraction 最大误差及逐点上载体数组摘要均留 runner。这个紧凑表达保留全部节点，既不子采样，也不把原始误差数组拆分公刊。

文件先以 fresh 名写完整，再登记 SHA 到 append-only journal；同一块身份不得覆盖。恢复时逐块核 input/array/output SHA 和已完成前缀。尚未登记的 orphan 完整文件不被默默当完成或覆写。缺费用、缺均值角、自然预算结束、真实数值重读失败均分别记录，不算完整。

## 8. 完成语义与后续剩余责任

只有完整查询计划中每个节点均已有真实工作四 jet 和完整准确输入包围，且全部 mean/profile 来源已付，才可写 `complete_planned_reference_node_fees=True`。这只是同固定参考在已声明有限节点集上的费用。

以下责任始终独立：连续全角覆盖、准确径向积分离散误差、当前外层旋转及其参数/角导数、normal-chain 的全部隐式误差、原参考校准差、完整 $F$ 六 jet、metric/reach/嵌入与全部 $t$、旧外层未记账工作字与新节点字的关联。后继应实际消费这些不可变节点记录继续支付，不以本组件的完成替代课题 README。

## 9. 执行范围

所有 actual 原始读取、provider evaluate、区间计算和费用消费只在本公开仓库 Actions 执行。本地仅做完整来源阅读、文本派生、AST/compile/接口核查；没有新 fixture、没有请求降低变量/范数/历史责任。现阶段没有科学返回，也没有预填 `paid` 或 `complete`。

## 10. 已完成的完整小源与准入参数

两源均是独立完整入口，不修改已刊数学源、provider 或当前正在运行的 solver：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `material_envelope_reference_node_inputs.py` | 35219 | `80744e058f95e4d91192b74c9a01c2ed9018858a15b5c8fd83d3b960069e62eb` |
| `material_envelope_reference_node_fees.py` | 37276 | `81ce42aa036808cb4c429afe8c88f12c13c0afbce179bd3c8167139cd4941917` |
| `material-envelope-run07-complete-reference-node-fees-ready.json` | 5023 | `ef3a811a765473698167ece2bb9fe1fd635707a153f67739be4dccedf268ae8e` |

输入源负责完整实际绑定、所有历史地址及径向/角查询、原 `_plan`/`_mean_cache` 实际只读恢复、原 `evaluate` 新四 jet；费用源负责完整实际 mean/profile producer→request→consumer 来源、所有准确分支、四 jet 范数费和自然预算恢复。费用源完整硬钉输入源的实际 SHA，全部八个既有依赖的实际文件 SHA 已在本地**纯字节**核相等。

准入参数保留已刊全批费用入口的相同 actual report 和五输入，新增其真实费用报告路径。唯一新输出为 `{work}/material-envelope-first-complete-reference-node-fees`；预算 600 秒，panels128、precision160、Taylor48、profile-series48，工作块 64 径向行乘 8 角。这些块只是完整查询的流式执行单位，所有块均在完整计划中。原 report 或 mean-fee report 尚未存在时，不伪造结果或输入 SHA；ready 当前是准备状态，实际是否准入/执行须另读 Actions。

已做的检查仅为两个完整文件 AST/compile、重复字面字典键、尾空白、八依赖全文 SHA、完整 CLI flag 清单与原五输入逐值比较。geometry 对完整材料地址/P0/grid/积分角职责与准确 scalar/chart/跨分支/cutoff/向上转换作了指定范围的独立文字核；construction 对原 provider 的 12 个 mean 缓存键、七 plan 数组、原 evaluate 四 jet 和新根计数边界作了指定范围文字核。均未执行科学，没有以这些核查代替未来 actual 返回或另设新 fixture。

## 11. root 完整阅读与本次实际排入

root 已全文读两个完整源、全部参数和本说明，独立核八个既有依赖全文SHA；只作文本/AST/compile，没有执行科学模块或数值fixture。本普通提交把完整节点入口排在07已存在的全批mean/profile费用步骤之后；prepared ready本体保原准备状态，真正队列保全原五对象并加入这一完整步骤。实际是否开始、成功/失败、逐点费用及完整计划是否覆盖，仍只能由后续实际返回决定。

准确affine点、全部可能支持分支、原四参考jet、完整mean/profile输入、逐一向上binary64费用的责任如上；费用源每点先计算准确范数上界，再核其保存载体不小于准确值。若原报告尚未产出可绑定的radial_plan或成功均值context，入口会明确失败，不能称已有完整pending计划；只有实际完整查询责任可重建时，未有角/未有费用才保为pending。当前外层旧未记账节点字、normal/calibration/积分/完整F六jet和连续全域证明仍不由此支付。
