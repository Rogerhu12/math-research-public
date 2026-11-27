# Run 05 全部已执行来源的材料地址闭包与 Run 07 的准确字绑定

本文是完整源码的地址集合归纳与实际输入身份说明，不是新的场计算、连续几何证书或旧报告重建。它扩充已刊 `2026-11-26-seed19-permanent-location-source-closure-and-envelope-policy.md`：后者证明旧 Run 05 的第 19 步 `e482` 所能新增的地址属于既有地址与完整固定网格的并集；本文补齐该步之前第 1–18 步的全部来源、两类角色与保护标签边界，并接实际成功的旧载体复原。

完整历史属于 `45870334713 / attempt 1`；必要输入复原属于 `45909290354 / attempt 1`。本次只做源码、JSON 小记录、字节身份和 AST 的静态读取，未在本地执行 NumPy、场、根、Jacobian 或数值包围。文中科学返回值来自已公开的实际 Actions 小记录。所有文件路径均相对本课题目录，除特别说明外源码位于 `scripts/resume_20261126/`。

## 1. 要证明的集合和不作的推断

材料地址以完整三元组

$$
\operatorname{key}(c,u,\phi)
=\bigl(c,\operatorname{float.hex}(u),\operatorname{float.hex}(\phi)\bigr)
$$

记录。这里 $c$ 是真实原胞号，$u$ 是该胞的实际 binary64 局部坐标，$\phi$ 是固定初始材料角图的实际 binary64 角字。本文的集合身份不作十进制舍入或近邻合并。

这不把原 4d9 walker 改说成 hex-key 字典：它原本按 numeric tuple 去重并合并角色，e54 的实际指纹明确记录该语义及幸存的 signed-zero 字。本文的 $P_0$ 是原 walker 实际产生的集合，三套指纹必须按其幸存字重现；hex 表达用于准确记录这些字。后继包络可以更严格地区分两个 signed-zero 字，却不能因此丢掉任何原已保留字，也不能重新解释原保护合并规则。

令 $P_0$ 为实际 4e 准备器消费完整十一份历史参数后得到的全部明确地址的并集。各自的 curvature、radius、protected-curvature 集合仍分别保留；$P_0$ 作为集合符号只表示它们的地址并集。令

$$
G_{05}=\{(\mathrm{cells}_{05}[p],\mathrm{u}_{05}[p],\phi_j):
0\le p<7377,\ 0\le j\le512\}.
$$

本文证明：下述实际源码和已给输入的任意执行前缀中，凡能被原 `Locations.walk` 识别并进入永久物理地址责任的新增位置，均属于

$$
E_{05}=P_0\cup G_{05}.
$$

这包括成功、拒绝、异常之前已经完成的真读取和 SOC 分离。归纳不需要猜测未知第 19 步最终接受了几步，也不从最终位置计数相同推断中间没有新角色、保护标签或读场。失败报告没有 `initial` 或 `final` 也不能单独证明其包围的初始化代码从未进入部分几何读取；本文的集合结论覆盖这种保守情形。

“位置属于 $E_{05}$”不等于恢复了历史曲率数值、半径数值、参数梯度、有效证书、受保护行的先后次序，或某次原工作集。尤其原仅作为半径位置的 $P_0\setminus G_{05}$ 点，也可能在后续完整扫描或 SOC 中成为曲率极点并获得保护。因此未知历史角色和保护次序的范围是整个 $E_{05}$，不能只写成未知网格点。

## 2. 十一份原输入的完整来源

实际初始包为 `scripts/resume_20261120/a04_historical_location_seeds.json`，63,070 bytes，SHA256：

`8fef7ae761e8c2f9982a452eb841f1db440539fe2ce13cf09bf8b4db9397afa8`。

schema 为 `a04-historical-location-parameters-v1`，完整有序名称为：

1. `legacy_memory`；
2. `restore_grid`；
3. `restore_local`；
4. `witness_positive`；
5. `witness_lowphi`；
6. `full13_curvature`；
7. `full13_radius`；
8. `r17_grid`；
9. `r17_local`；
10. `r17_fixed`；
11. `continue_union`。

4e 的 `add_supplied_locations` 首先核完整原节点、固定 scalar 定义、923 节点、160 模式、1845 legacy stages、7377 observed stages 及全圈 2048 角。它对每个完整 payload 保留内容与顺序、原来源 SHA、原 capacities/counters 等出处，明确不把历史容量当新的存储上限。它额外展开四种早期 indexed 数组 `curvature_locations`、`radius_locations`、`grid_curvature_locations`、`grid_radius_locations`，并完整调用 4d9 walker；`full13_radius` 的角色、两个 witness 和 `full13_curvature` 的曲率角色均显式保留。legacy-memory stage 必须在原 1845 前缀内。

带整数角索引的点在绑定的真实 carrier 上用完整 `resolve_grid` 转成字面位置。旧 normal-angle 数值被明确作为新固定材料图的 $\phi_0$ 地址读取；4e 没有声称这是跨表示同一个空间点，更没有迁移旧值或证书。原更早 carrier SHA 是参数出处，不能替换旧 Run 05 的实际 dc5 carrier。

当准备器生成 `supplied-location-provenance.json` 时，它保存的是完整 `original_payload`、完整 `ordered_records` 和准确节点/scalar 绑定；不是只保存十一份文件名或计数。新消费者从该完整来源重新按原规则读十一份，并在真实旧 dc5 上解析 indexed 点，最后核三套准确字集合的既有实际指纹：

| 集合 | 实际条数 | 完整有序化字集合 SHA256 |
|---|---:|---|
| curvature | 1250 | `0d18c105c0899f463979a1a99b28c7c74cc26dd3f3132ad58bae8803374ba9a8` |
| radius | 208 | `1758d6f5c7376dacf573d8495f576e62d06277f0b3be158e7b7b444def79d471` |
| protected curvature | 18 | `4959a1e7725524fee90517420406f6d3c1e1d12c1ca2255967d5b6056b43872a` |

这些条数只用于完整来源读取后的身份核验，不能代替十一份 payload 或集合证明。角色并集也不删除原三套独立责任。

## 3. Run 05 第 1–18 步的完整来源链

实际记录在 `notes/2026-11-26-public-actions-45870334713-1-part-001.md` 至 `part-005.md`；各条保留实际 launcher/source、CLI、输入与输出身份。下表的序号是本 run 的真实执行顺序，不是历史编号 3/17/21/26/30。

| Run 05 步 | 实际作用与科学主体 | 物理地址来源 |
|---:|---|---|
| 1 | 067b warm 再生；实际未传完整求解 `--implementation` | 产生 warm、节点、scalar 输入；不运行本轮 SO3 几何选点或永久点更新 |
| 2 | 4e 独立轴对称参考准备 | 完整十一份参数，按 §2 真实绑定成 $P_0$ |
| 3 | 606 独立 direct 首方向 | `locations.json`，完整实际 $G_{05}$ |
| 4 | 359 direct-SOC，02875 完整分离 helper | `locations.json`、真实第 3 步 restart report；同 $G_{05}$ |
| 5 | 7b7 / d2 R696 角向表示首方向 | `locations.json`、真实第 3 步 report；同 $G_{05}$ |
| 6 | 606 原 integral 范数首方向 | `locations.json` 与第 3、4、5 步完整报告；同 $G_{05}$ |
| 7 | e54 纯来源/初点/地址指纹读取 | 只消费既有第 2–6 步输入和报告，不生成场或新地址 |
| 8 | 606 integral 真实 restart | `locations.json` 与第 3、4、5、6 步完整报告，第 6 步真实父；同 $G_{05}$ |
| 9 | 6d54 纯读取第 8 步 | 只转录和核已有报告字段 |
| 10 | e54 全历史指纹读取至第 8 步 | 完整既有报告与真实 carrier，不生成新场地址 |
| 11 | 6253 所有实际 trial 家族读取 | 只从第 8 步实际记录复制已有地址，不作连续位置搜索 |
| 12 | 8f37 / b712 gamma-KKT 显式 H 初读，实际失败 | `locations.json` 与第 3、4、5、6、8 步报告；根状态不是额外物理地址 |
| 13 | c3fd 纯读取第 12 步 | 来源、原点、根与已有几何字段归因 |
| 14 | b3d 实际保存 KKT 矩阵归因 | 读取已保存矩阵/状态，计算诊断；不读新场或生成物理位置 |
| 15 | 68a6 / 42ea fixed-normal 初读，实际失败 | 上述完整输入再加第 12 步；同 $G_{05}$ |
| 16 | 8381 纯读取第 15 步 | 只核完整来源及已记录 normal 状态 |
| 17 | e8e0 / 42ea 显式 H fixed-normal 初读，实际失败 | 上述输入再加第 15 步完整报告；同 $G_{05}$ |
| 18 | f826 纯读取第 17 步 | 只核完整来源及已记录状态 |

第 1 步 `reproduce_and_solve.py` 的真实无 `--implementation` 分支顺序调用 `rebuild_fullclosed.py`、`rebuild_closed_warm.py`，然后返回 warm 输入；它不会进入该脚本可选的完整非线性求解分支。warm 再生含节点积分和既有桥接，不能称为无科学计算，但这不是新的 SO3 几何选点过程。其报告、节点和 scalar 输入也不是下列完整 driver 的新增位置 manifest。新增位置的初始来源严格由第 2 步的十一份包决定。

第 7、10 步的指纹不以计数推闭包；它们仅提供与完整来源配套的准确字指纹。第 11 步的 `address` 仅校验并复制已经命名的 `cell/u/phi` 或原 stage/angle；`small_location` 还会省去某些 stage/angle 标记，因此不能仅凭其公开十六进制数“看起来像 Gauss”反推来源。本文没有使用这种逆推。

## 4. 共同完整扫描器的准确静态相等

以 2240 `so3_axisymmetric_meridian_geometry.py` 为基，完整解析以下四个实际变体：

- 8fa `so3_angular_unit_geometry.py`；
- 0c48 `so3_zero_gamma_kkt_geometry.py`；
- 2557 `so3_zero_normal_lift_geometry.py`；
- d84b `so3_supported_unit_normal_lift_geometry.py`。

stdlib AST 逐函数比较表明，每个变体只有 `GeometryScreen.__init__` 改变；下列全部 24 个方法的完整 AST 相等，没有增删方法：

`_set_x`、`_location`、`_remember`、`_grid_location`、`_validate_fields`、`_point`、`_point_geometry`、`_amplitude_values`、`_scalar_values`、`_offer`、`_block_candidates`、`_ensure_grid`、`_new_locations`、`scan`、`scan_geometry`、`single_fields`、`curvature_cotangent`、`_check_prepared`、`fields_at`、`pullback`、`pullback_at`、`_pullback`、`_amplitude_row`、`build_rows`。

构造器的来源/model/layout 守卫仍逐实际表示核对，不能因方法相等省略来源绑定。相同方法给出的地址结论是：

1. `_grid_location` 只从当前 q 的 `observation_cells[p]`、`observation_u[p]`、`phi[a]` 取实际字，因此其输出属于 $G_{05}$。
2. `_ensure_grid`、`_block_candidates` 及 top-pool 保留的候选来自这些完整网格读数；没有对 $u$ 或 $\phi$ 再做连续极值搜索。
3. `scan` 在完整网格后遍历两类永久地址的并集。每个所读永久位置都沿用原 literal 三元组，不投影到网格，也不重新采样。
4. `_new_locations`、曲率 worst、farthest、body 和 paired-distance pools 只择取本轮实际已经读取的位置。它们可以改变角色或保护状态，但不会创造新的坐标字。
5. `build_rows` 对旧 e783 selector 的适配只重新读已指定 grid/arbitrary 地址或已有常量 core/cap 标量行，未增加连续地址优化器。

几何完整扫描在每个所读点计算两主曲率、半径和两个握持见证符号，因此“原 radius 角色”不意味着该点永远不会被记为 curvature。这个角色提升正是 §1 的必要限定。

## 5. Driver 与 SOC 的归纳步骤

606、359、7b7 中 `add_location`、`remember`、`scan`、`all_locations` 的完整 AST 相同。8f37、68a6、e8e0 的前三个方法也完全相同；其 `all_locations` 只把实际来源 report 的选择显式化为 `source_report_path`，完整 walker、同 N/carrier 核验、角色和 protected 合并逻辑保留。

`add_location` 只复制合法 literal 点，或者按 q 的真实 arrays 解析已有 stage/angle。`remember` 把几何返回的两套 new-location 数组并入 append-only 内存；保护位取并集，不清零。`scan` 每次调用完整 screen 后马上执行 `remember`。初读、每轮当前父重读、每条到达真实几何的 ray、SOC corrected trial 和最终真读取都沿此路径。被拒绝的场所得位置也保留。

假设进入一次扫描前的内存属于 $E_{05}$。§4 表明完整扫描只访问 $G_{05}$ 与已有内存，所以全部新结果仍在 $E_{05}$。`remember` 只并入这些字，归纳成立。selector 形成行不改变其位置来源。

02875 的额外 SOC 支路必须单独核，因为它也能给新位置 protected 标记：

- `prior_rejection_requests` 从真实、来源相同的 complete rejected geometry 中提取已有 worst、body/distance pools，不从数值值反求新的位置。
- `_actual_diameter_partner` 只在当前已读 farthest 点、常量 core 直径、cap-height 直径之间选择真实分支。点分支的地址已在 $E_{05}$；另两分支是已有标量约束，没有新的 material 地址。
- `seed_before_qp` 对历史真拒绝地点在当前真实父重读两曲率分支、当前 diameter partner 和所需幅度分支；不继承旧曲率/梯度。`_parent_row` 不改变描述中的地址。
- `extend_from_rejected_geometry` 同样只取当前实际 corrected 拒绝记录中已经读取的位置。两主曲率与距离两符号不会因一个旧活跃符号而删除。
- `_append_descriptors` 可把这些点加入 protected curvature 或 radius memory；所有 descriptor、partner 和错误元数据仍只含已有地址。负当前父界会诚实拒绝可行零假设，不制造替代点。
- 359 的完整 driver 在 `seed_before_qp` 后、每轮 `extend_from_rejected_geometry` 后，均把 helper 的两套新增位置交给原 `add_location`；即使分离失败，已存在的错误 descriptor 被完整保存也不会越出 $E_{05}$。

因此原 ray、拒绝 ray、多轮 corrected SOC、prior rejection 分离和中途异常都保地址归纳。是否进行了更多 CG、是否接受了步长，以及 norm 从 jet-sum 换 integral，都不在这些地址生成函数内。

## 6. 角向表示与零闭合内部节点不是新的物理 memory

7f 和 d2 从已验证 parent problem 原样复制 `observation_cells`、`observation_u` 与 `phi`。R696 的内部角积分节点用于求同一被请求地址的物理场；它的 `grid_fields` 仍返回请求的全部 observation × quarter-phi 数组，只按原块重分。内部 primitive/积分节点不交给永久位置回调。42ea 和 b712 的原胞积分、normal/KKT 中间控制与 root 角节点也用于评价当前查询的场，不是新的 $u$ 搜索器。

完整 `Locations.walk` 真正识别的地址入口为：

- dict 中同时出现 `cell/u/phi`；
- dict 中 `stage` 配 `phi` 或 `angle`；
- `grid`、`grid_radius`、`arbitrary`、`arbitrary_radius` tagged 项；
- `protected_current_representatives` 的既有 current/seed location；
- 命名的 `curvature_points`、`radius_points`、`protected_curvature_points` 三元表。

它还由 curvature/radius/worst/diameter 等路径语义和显式 protected 位传递角色。`fixed_core`、`cap_height` tagged 标量是已有标量约束，不成为任意新空间点。

对完整 b712 和 42ea 的根失败、批次、metadata 构造及所调用的 base/reference metadata 逐段检查：新根记录使用 `angle_index`、`local_angle_index`、`batch_stage`、`normal_stage_index`、`material_angles_binary64_hex`、控制向量和乘子等字段。它们没有 walker 所需的 radial `cell/u`，也不组合成 `stage` 配 `phi/angle` 的物理入口。9 维 KKT state、6 维 controls、3 维 normal increments 不能仅因列表长度为 3 就当物理三元组；原 walker 只有上述命名入口才如此解释。H-only 输入记录含完整自由点摘要、非 H 前缀摘要与 H 字，也不引入物理地址。

报告中可递归出现的真实几何元数据和输入历史仍由 §2–5 处理；不是因为字段深而漏掉。动态传入的原来源定义、input records、原 seed payload 也不能被称为“无输入”，它们的地址责任已经由完整 $P_0$ 和上述归纳覆盖。

第 12、15、17 步的实际根失败不被扩张为不可达性结论。本文也不依赖“初读失败所以只剩 $P_0$”这个更强断言；即使初始化异常之前已经读了一部分几何，已读地址仍属于 $E_{05}$。

## 7. 纯读取步骤的闭包

e54 只绑定完整实际报告、已有 carrier 和来源，再用同 4d9 walker 计算字集合身份；它不生成场、Jacobian 或新的优化点。6d54、c3fd、8381、f826 的 pure report reader 只核来源、当前点、norm/根/几何字段并转录已存在信息。它们不会调用 `point_fields`、continuous-position search 或新的场评价。

6253 的 `address` 校验并复制实际已命名的字段，`family_geometry` 遍历完整实际 trial 中的 reach、五幅度、worst/farthest 和候选池；只改输出表达与添加已有值的 hex，不生成新角字。它明确不把 pooled distance 候选说成各符号独立 argmax。

b3d 对来源已绑定的真实 saved 9×9 KKT 矩阵、同矩阵点 state 和 residual 做 Actions 中的有限矩阵诊断。它不重新执行 F/J/root，也不生成 radial material 地址；其角索引和内部 state 不满足 §6 的 walker 入口。矩阵实际点与返回失败点的区别仍保留。这一步的数值诊断不能被称为新几何读取或连续 rank/SOSC 证书。

所以 pure 步骤即使被以后完整 walker 再读，任何留下的真实 physical location 都来自其完整原报告，不能越出已证的 $E_{05}$。读数摘要不会补回未公开的历史保护次序。

## 8. Run 07 必要输入复原的实际返回

Run 07 首参考实际载体与旧 Run 05 全文件不同，不能由同 CLI 推出地址字相同：

| 角色 | SHA256 | bytes |
|---|---|---:|
| 旧 Run 05 carrier | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` | 227202 |
| 当前 Run 07 carrier | `7c8b3cbffd66a360b01341db8e1179f211da3c264de85812020a5e48ad5637c3` | 227211 |
| 完整原 warm，两 run 相同 | `3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c` | 由实际 input record 保留 |

必要消费者 `restore_actual_run05_observation_carrier.py` 的完整 SHA 为 `ef67425800ae9de626a7f8f48fd89deb125fbf0e4d6af72cf79741d1e254664e`。它按已公开真实 2397 live leaves 恢复原准确积分的同一优先级/序号/拆分顺序；完整原 scalar 参数、node recipe、旧准确区间及原保存顺序都实际重核。只有重建文件全 SHA 和字节数都与旧 dc5 相同才写绑定。这是必要输入再生，不是从摘要假造数组。

该消费者已在 `45909290354 / attempt 1` 实际成功返回，source commit：

`40f73dbacdd18bab36cda4cd6b421a1d1b917694`。

公开小记录 `notes/2026-11-26-public-actions-45909290354-1-part-001.md` 在该返回时为 31,775 bytes，SHA `8630c9e440a6eaf648e3fcec35eb86e67b03a7d4ddab4db07ca2ba1ef2888749`。输出：

- 完整 report：19,691 bytes，`926db461a4efce0fa40ab539b9df28143f8664cca25ec96e95ebe1d7aa83dcdf`；
- 重建 NPZ：227,202 bytes，完整旧 `dc5ffc55…`；
- `material-envelope-carrier-binding.json`：1,537 bytes，`aaa65a5ecac807e97cf771a08dd57d2ac26b48adf6acc9592025c0c706581c8e`。

报告实际返回 full-original-carrier match、cells equal、u equal、Gauss equal 全部 true；内部输入再生 389.465780085 秒，F/J/root 均为零。它没有重跑旧非线性方向、旧 seed19 或旧几何。

实际旧/新共同的三个数组摘要为：

| 数组 | 实际摘要 |
|---|---|
| observation cells | `3ecef008e7512aa30ef85790e6a0e9bf0414adfed8698249be4fd5df7b19f31b` |
| observation u | `ab35773d7256855fcca1355c933ebb2affd8f2e6a1544ea3c6cabf5950152c69` |
| six Gauss unit nodes | `0d6887a8bbd6ba21f90a86b350730858552df0d2ff00d087a40de05f705e95e6` |

此处引用既有实际返回，未本地重算这些数组。下游仍实际 rehash 两个完整 NPZ 并读全部地址成员，不能把一个自报 `equal=true` 代替消费。若用于另一个未来 carrier，必须重新按真实文件构造旧/新并集，不能把本次等号自动移植。

## 9. 全部角字的精确闭包

4e `AxisymmetricReferenceContext.create_pair` 实际使用

`q.N, q.phi = L+1, np.pi*np.arange(L+1)/(2*L)`，其中本次完整全圈 N=2048，L=512。

7f、d2 及其零层只复制这套实际角数组；没有用 current core 的逆图角替换材料地址。4d9 对整数 tag 的式子是 `math.pi*j/(N//2)`。本次两式均为同一 binary64 π 常量乘精确整数 $j\in\{0,\ldots,512\}$，再除 1024，运算顺序为先乘后除。整数在 binary64 中准确表示，除数是准确的二次幂。这里没有 sin/cos、特征值、求和归约、leggauss 或自适应路径；采用原实现声明的 binary64 逐次舍入，两式的每一字相同。

新消费者仍把当前 q.phi 的全部 513 个 hex 与该完整公式逐字核对，并记录实际数组摘要；不能只核两个端点或角数。结合 §8 真返的 old/current cells/u 完整字等号，得到本次 $G_{05}=G_{07}$ 的材料地址字等号。原精确 mesh 与固定 chart 的字身份也独立保留：

- mesh：`eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262`；
- initial fixed core/chart：`90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e`；
- original scalar-parameter projection：`e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`。

这些地址与 chart 身份不把旧 scalar 文件 SHA、当前准确 profile 身份或当前场点改标成旧身份，也不提供跨场的物理值等号。

## 10. 包络能承担的完整责任与新工作行政策

结合第 1–18 步的上述归纳与已刊 seed19 源码闭包，旧 Run 05 已执行但未返回的任意 seed19 前缀所可能留下的全部材料位置均被 $E_{05}$ 包含。旧任务终态、原 raw 报告是否存在仍按真实记录陈述；本结论不补造一个 final report。

后继可以完整消费 $P_0$、真正恢复的旧 carrier 和真实当前 carrier，并把旧/新整个网格并集作为隐式永久 nonlinear memory。所有明确原历史地址仍保留 original roles/protection。每个当前完整场、rejected trial 和最终读取必须在该整个集合上读完整六 jet、两主曲率、半径及两个 witness 符号；core/cap/H 标量行另保原定义。

未知历史角色、protected 标记和原选行次序没有恢复。root 已明确选择独立的新 working-row policy：保留已知明确历史的原 e783 prefix，整个 $E$ 进入永久真筛，按当前完整读数增加 near-active typed 行及 append-only 分离行。这不是同旧未知工作集的逐字续算；source/schema/policy 身份必须独立记录，不能只把 envelope 作为省略历史的别名。新代码也不能宣称每一个潜在 protected 点已进入原 192 行 selector。

所有 unknown role/priority 的声明必须覆盖 $P_0\cup G$，而不只是 $G$。某个旧仅 radius 的 P0 点可能已被旧 SOC 升格为 protected curvature；新的统一 full-envelope policy 必须承担该位置的全部 nonlinear family，而不是猜一个旧 flag。

若以后某个真实新的 continuous-position search 或外部 manifest 引入 $E$ 外地址，应显式扩充永久地址与来源；本文没有证明任何未来算法的地址都在这个固定包络内。当前已审来源没有这种新搜索器。

## 11. 完整源码身份表

下表是本次地址闭包直接核读的完整小源；不以简称代替实际来源身份。

| 源码 | SHA256 |
|---|---|
| `scripts/resume_20261120/reproduce_and_solve.py` | `067b3f2e14145a6f88b2d171c555f1174f0505b45a5aaf670c3ec2610f7c286d` |
| `scripts/resume_20261120/rebuild_closed_warm.py` | `63950b72e75e8b6497ad2119ca16076c2c8749f9615166beb6d52adcab86708e` |
| `so3_axisymmetric_reference.py` | `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3` |
| `scripts/resume_20261120/launch_refinement_from_full_report.py` | `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60` |
| `fullclosed_axisymmetric_so3_qp.py` | `606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9` |
| `fullclosed_axisymmetric_so3_separation_soc.py` | `359ffc94df1b33485c2cda4de0f5662ef7bc802c588f583a023fcd5723a7872d` |
| `complete_axisymmetric_so3_rows_soc.py` | `02875e4a150644f8addb6073b346e2de3b0f3cf50498e9cf6efe8fe0333d7c97` |
| `fullclosed_angular_unit_qp.py` | `7b7cc0c9b27a0339debab0319c6854323dfc6c21f3e92c64946cbffc70824c7d` |
| `fullclosed_zero_gamma_kkt_height_so3_qp.py` | `8f37529deaa8e07d4561e00371b39b82cb641a4e52e0790d41555b2ae9e320a9` |
| `fullclosed_zero_normal_lift_so3_qp.py` | `68a6e483a4916d72411d08647622a1e539b26f9eca3c1449b4e7399bec17dd38` |
| `fullclosed_zero_normal_lift_height_so3_qp.py` | `e8e096f9a2a2acd5b08e907aa2b9df1fc9a402d033f67e1420f072dc579c6fe7` |
| `so3_axisymmetric_meridian_geometry.py` | `2240a1f68021991a85c502ed3cf67c82f6bac6e1e4e10b3b3286eab120d4f229` |
| `so3_angular_unit_geometry.py` | `8fa941feb48f9c7a8a180a14d7f3ead9df00decb63e287531bf773b27285a6a5` |
| `so3_zero_gamma_kkt_geometry.py` | `0c4886237d642382a1ae329d36517d5752ba717f0fa1471993bb98769e828f17` |
| `so3_zero_normal_lift_geometry.py` | `255760e188d13f22ffef86c029f35f5d1629384411d2e32f03f75df60f4ab71c` |
| `so3_supported_unit_normal_lift_geometry.py` | `d84b540d21622d4d609efa5ea85fef432a2dcebb51bea0f3c7c24376294918f4` |
| `so3_axisymmetric_meridian_operator.py` | `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf` |
| `so3_angular_unit_operator.py` | `d2f8a93c3356fc172e5c6ac365b0bff65660fea2bb3bf8350ab124537a0f4a14` |
| `so3_zero_gamma_kkt_operator.py` | `b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a` |
| `so3_zero_normal_lift_operator.py` | `42ea8ec5920e3815b99c83c41448efb38ee37860f4d9362ddea6bce2418d39fe` |
| `scripts/resume_20261120/fullclosed_point_inequalities_v2.py` | `e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8` |
| `scripts/resume_20261120_curvature_qp.py` | `a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854` |
| `read_complete_so3_location_and_initial_fingerprints.py` | `e54cad5e7e78f3576412fef82701a3b276fb9af8795ca16d3e016cb9bc0382e7` |
| `read_axisymmetric_so3_report.py` | `6d54cbba7ff998bc98b0f39c6a26ae33c16957fb0b9dc0fffced1037212455eb` |
| `read_axisymmetric_so3_trial_families.py` | `625317b44fd3610903b395d6e8fd5374a4764d6930ef08fb92c33f45e15c7cd3` |
| `read_zero_gamma_kkt_height_so3_report.py` | `c3fdd83c29dabeb00974899bb183360da01c57fcf364704759efcc1ac643b9ec` |
| `read_actual_gamma_height_kkt_matrices.py` | `b3d424b30563ad883b3dcbed8aa82537138243a1b7a12a93baf9045b2316347d` |
| `read_zero_normal_lift_so3_report.py` | `8381cd9e034fda5917cae5f221f0c3f5420953cab6ca8dd809c82f3de0f7e1e8` |
| `read_zero_normal_lift_height_so3_report.py` | `f8261f971d7993534d7e020efaef5ca480c51ba2d2da7861d18e6a18d2af799b` |

完整 scan/row 方法与 driver 的静态相等只用于缩减重复的源码论证，不会把不同 constructor 的 model、不同 source SHA 或不同真实场归并。所有结论均保留当前完整自由变量、原完整 nonlinear 阈值与新政策的独立身份；没有新增精度门或完成标准。
