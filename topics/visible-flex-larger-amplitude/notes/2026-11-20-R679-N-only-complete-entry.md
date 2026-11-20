# R679 的 N-only 完整入口：原载体、旧角位置和共同角归因

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / geometry_path。

状态：完整新源及源码接口准备；**没有执行 N-only 科学计算、数值 fixture、候选读出或新 Actions 任务**。这里直接消费 [R679](../results/R679-dyadic-angular-refinement-and-common-grid-attribution.md)，不重证其角规则结论，也不以已有径向方向的小收益断言存在频率瓶颈。

## 1. 新源与固定范围

完整新源 `scripts/resume_20261120/launch_angle_only_fullclosed.py`，49,985 字节，SHA256：

`e738e4ed8c0d367a629f6edd89a5bfdc6345e55ab4a984c817940f08d277e38c`。

实际输入由一个自然完成的 full-QP 报告及其 final bundle 绑定。新入口只允许该报告的 full $N$ 严格倍增到 $2N$，并要求原 $N>4M$、$4\mid N$。保持 $M$、全部自由变量、原径向 observation plan、全部 literal $a$、正径向权、准确 $g$、mesh、node report、帽接口及全部既有位置。它不补零、不径向插值、不调用 R676 的 factor=1，不生成新 seed 或新 node report。

原 bundle、node report 和 observation NPZ 的路径及文件 SHA 原样保留。free dimension、integrated dimension 和 coarse dimension 不变；full 残差行数倍增。输入文件在执行返回时再次核 SHA，没有将新默认 N 写回原 carrier。

新有限目标确实改变。保留 p8、$\varepsilon=.001$、$c=.05$、原半混合径向正权、$\nu_c=24$、$.992/.025$ 数值几何政策及原母范数。继承自然父实际末 $\mu$，不因行数翻倍把 $\mu$ 乘二或除二。后续 driver 仍使用其原真实回溯更新；可选方向数/迭代预算明确记录，源码准备本身没有执行它们。

## 2. 已有源复用与父身份

主要复用项：

| 角色 | 已有完整源及 SHA256 |
|---|---|
| M-only 中已有的 stdlib 目标/路径及实际 affine 检查函数 | `launch_frequency_only_fullclosed.py` — `eea174b983d20543a154df6fdb308bb5742c7f3bde04936c960fd572de267677` |
| 自然父、末阻尼、全部真实位置 | `launch_refinement_from_full_report.py` — `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60` |
| exact-location 完整 AST 变换 | `launch_fixed_g_refinement_qp.py` — `100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622` |
| 同场 canonical 模型核对 | `refine_fixed_g_fullclosed.py` — `2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a` |
| 纯 SOC 完整父绑定 | `derive_full_phi_parent_row_soc.py` — `805823e49970246bf532b65a0caefd88244b414ee52f8f555ff28b745d2fd30a` |
| SOC 的真实末阻尼/已接受修正记录检查 | `launch_full_phi_parent_row_soc.py` — `9b7d50fd7d1a0332fc493f848688b792dff39fd2a1af4914349d048abe080d0a` |
| PCG+SOC 完整父绑定 | `derive_full_phi_coarse_pcg_soc.py` — `40e8c42b8c66424d06ff08af8dff8d1505eff2b4f48ba905c9ae405000d2357e` |

这不是调用 M-only 执行路线：新源没有调用它的 `prepare` 或 `materialize`，只复用已经存在的小函数。原完整 original/R671 launcher 的 `--print-command` 用于取得冻结依赖路径和完整参数骨架；此路径只做 stdlib 源准备，不加载候选数组。

父来源按三种实际情况严格分流：

1. 冻结 original/R671 或 R676 manifest-only 派生父：由 4d helper 核整个实际 body，下一方向使用冻结的 exact-location 派生 body。
2. 纯 SOC 父：由 805 完整重建并核 body；下一方向直接复用这个已经绑定的实际 source 文件、原 tau、原 helper 和原求解器。
3. PCG+SOC 父：由 40e8 重建 frozen → exact locations → SOC → PCG 的完整 body，并核四个数值组件；下一方向直接复用该实际 source，保持启用状态、组件源、beta 规则及原 SOC。

后两种不降回无 SOC 或无 PCG 的旧 body。没有只看注释头的兼容分支，没有接受未知任意父源。完整目标、场、母范数和 QP 的 source SHA 与父报告逐角色核对；新的角数由明确 `--angles` 参数表达，不伪装成相同 finite Phi。

## 3. 命令接口与两阶段准备

默认只生成 `angle-plan.json`、必要派生源及完整后续 argv；不读 NPZ 数组，不执行算子、oracle 或 QP。例如：

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/launch_angle_only_fullclosed.py" \
  --repo "$REPO" --work "$RUNWORK" \
  --parent-report "$PARENT_REPORT" --parent-source "$ACTUAL_PARENT_DRIVER" \
  --bundle "$PARENT_FINAL_BUNDLE" --carrier "$SAME_OBSERVATION_NPZ" \
  --node-report "$SAME_NODE_REPORT" --scalar-input "$SAME_SCALAR_INPUT" \
  --manifest "$COMPLETE_PHYSICAL_POSITION_MANIFEST" \
  --directions 1 --maxiter 256 --stage-block 64 \
  --outdir "$RUNWORK/angle-only-01"
```

变量分别应指向本次实际父链的完整文件，不能用历史文件名替代实际 SHA。`--new-angles` 可省略，默认准确取实际父 N 的两倍；若给出，则必须等于两倍。`--maxiter` 省略时继承实际父报告的 `max_qp_hessian_advances`。方向数缺省为 1，只是未来显式执行的参数，不表示本说明已经安排了一次方向。

在公开 Actions 中，对同一个尚未执行的准备加 `--execute` 才会读取真实数组、导出位置并执行。相同输入/参数/源的纯准备目录可以接执行；一旦有实际 attempt、位置 materialization 或求解目录，不能自动重跑同一目录。新实际尝试须使用新目录并保留前一记录。raw 输出必须位于 Git checkout 之外。

**仅读当前固定场的新偶/奇角**可在上述命令加：

```text
--readout-only --execute
```

这不启动 QP。它只支付父在新 $2N$ 网格上的同一份有限 first-jet buffer，以及由其直接取得的三份角分区统计。

若已有自然返回的同父 $2N$ 求解，可用新的只读输出目录，加：

```text
--readout-only --execute
--final-report ACTUAL_NEW_N_REPORT
--final-bundle ACTUAL_NEW_N_FINAL
--final-source ACTUAL_NEW_N_DRIVER
```

final 仍须来自本 exact parent bundle，N 为两倍、原模型/全部依赖/范数/初始末阻尼均匹配；不是一个任意外来候选。未知派生 final 不能因为数值看似接近就通过。原冻结 final 可以省略其 `--final-source`，由已知实际 SHA 定位；派生 final 须给实际 body。

同范数还逐项比较 `coarse_low_modes`、`requested_coarse_centers` 和 `actual_coarse_center_nodes`，不能只看粗变量数量。外部 final 也须保持父的 QP 容差、行秩阈值、活动行数量/选择/分块参数、回溯次数、target 及额外曲率 cap，并保持同一 original/SOC/PCG 策略分支。原有检查继续支付 p8/权/角 H² 参数、reach 政策、全部源、精确场载体和初始末阻尼。方向数及迭代预算是本入口允许明确选择的工作量，不伪称由这些策略比较固定。

## 4. 旧 grid 地址先解码，N 从不猜

`Locations` 每次以**该输入自己的旧 full N**实例化。父完整报告使用其实际 `N`；外部 raw 报告/清单可使用其明确 `N`、`optimization_full_angles` 或 `full_angles`。纯 `cell/u/phi` 位置没有角索引迁移，原 binary 三元组直接保留。

若一个外部 grid 清单缺失 N，可显式提供：

```text
--grid-manifest 2048 ACTUAL_OLD_GRID_MANIFEST
```

该数字是那份位置来源的真实 old N，不是新求解 N。矛盾的 N 声明直接报错；包含另一个 N 的嵌套完整 grid 报告应单独提供，不能用外层 N 解释。没有 nearest-angle、round13 或把旧索引直接当新索引的步骤。数学索引关系 $k\mapsto2k$ 仅作为准确关系记录；实际永久点保持原 literal $\phi$，并不投影到新 grid。

实际 radial carrier 仍在 Actions 内用于将 stage 解成原 `cell/u`。所有旧来源先各自正确解码，再按准确 binary tuple 合并，protected 位保留。原始历史中已完全丢失的信息不伪造恢复。

输入合并生成 `complete-permanent-locations.json`。自然 final 返回后，其 grid 位置由**新 N**解码，再与已保存的旧数值三元组并成 `complete-permanent-locations-final.json`。这一阶段只解析已经返回的位置，不新增科学读出、不复制旧几何数值，也不把 metric 残差当作已支付的曲率约束值。

## 5. 一份新网格 buffer 的三组真实统计

小 reader 使用一个实际 $2N$ observed operator，随后依次 pack parent 和 final。每个 stage block 只取一次完整原 first jets，使用其 raw Gram 同时计算：

| 分区 | 新 quarter 列 | orbit 总和 | 自己的归一分母 |
|---|---|---:|---:|
| `even` | `0,2,...,2L` | $N$ | $WN$ |
| `odd` | `1,3,...,2L-1` | $N$ | $WN$ |
| `all` | 全部列 | $2N$ | $2WN$ |

这里 $N=4L$、$W=\sum_s w_s$。两端各 2、中间各 4 的原 quarter multiplicity 只用一次。每组有独立的 mean Phi、Frobenius SSE/mean、最大 Gram、最坏 stage/cell/u、new index、适用时 old index、literal `phi`/hex、理想 `phi/pi` 分数、minimum E/determinant 和实际最小归一权。

同一次 buffer 给出的 `Phi_all_minus_half_even_minus_half_odd` 与 `max_all_minus_max_parts` 如实保存普通浮点求和差；没有为把差调到任意阈值而重跑，也没有把它称作向外证书。

实际 `op.phi[::2]` 与冻结旧公式产生的 literal angle 数组逐字核对。如果这个相同角载体条件不成立，本实现不冒称已经取得共同旧角，须另用明确的旧角 reader；不能用相近位置替代。该检查没有比较两个不同 FFT 长度的场值是否 bitwise 相同。旧 driver 的 Phi 与新 reader 的 even Phi 会单列，因为场合成和求和路径可能出现普通浮点差异。

若 parent 与 final 的 q/H 及完整相同模型逐字相同，只读取一次场，明确写 `actual_readout_reused_from`；文件名不同不会被当作两个新计算对象。

不重读同一终态报告已有的全曲率场。真正新网格和完整永久点的几何过滤仍由完整求解 driver 真实执行并记录。`--readout-only` 不宣称支付了这些几何值。

## 6. 原场及 R671 的完整身份

原场直接构造同观察 carrier 的 frozen observed operator。canonical $\lambda=0$ 和非零 R671 则先由 R676 的完整 `model_definition` 检查 actual bundle、mesh/M、node/scalar/carrier、$\lambda/\eta$ 和全部源，再用冻结 factory 构造当前 $2N$ context。构造完成后，`context.definition()` 必须与输入模型逐对象相同；其中本来没有 N 字段。

本入口没有新 profile 缓存 API，也不把新 $a/I$ 当作插值多项式。冻结 factory 会在同径向点重取/缓存它实际需要的整数 oracle 数据，成本在真实 reader 秒数中计入。parent/final 共用同一个 reader context，不为第二个候选再构造一套径向 profile。

原 profile 文件不改写、旧 profile SHA 不冒充新输出。完整 solver 若按其原行为另存一个 profile，其实际文件身份仍由它自身报告给出。模型相同、profile 在数学上与 N 无关，不等于原文件 SHA 可以随意继承，也不支付新 finite grid 的几何标志。

## 7. 输出、归因与未返回范围

主要输出均留 runner：

| 文件 | 内容 |
|---|---|
| `angle-plan.json` | 完整实际来源/参数/argv、父 binding、末阻尼、位置来源各自 N、执行阶段和返回状态 |
| `complete-permanent-locations.json` | 准确解码后的完整旧位置输入 |
| `solve/report.json`、`solve/final.npz` | 原完整 driver 在新 N 的真实返回；只读模式不存在 |
| `complete-permanent-locations-final.json` | 自然 final 的新 N 位置和全部旧 literal 位置并集 |
| `common-even-odd-readout.json` | parent/final 在同一新 operator 上的三份有限角统计及同函数差 |

适合公开紧凑摘要的 dot-path 包括：

```text
parent.partitions.even.mean_Phi
parent.partitions.odd.mean_Phi
parent.partitions.all.mean_Phi
parent.partitions.all.maximum_relative_Gram
final.partitions.even.mean_Phi
final.partitions.odd.mean_Phi
final.partitions.all.mean_Phi
final.partitions.all.maximum_relative_Gram
same_functional_changes.even.final_minus_parent_Phi
same_functional_changes.odd.final_minus_parent_Phi
same_functional_changes.all.final_minus_parent_Phi
complete_pair
```

最后四项只有相应真实读出完整返回才成立。程序分别记录：父旧报告到 parent-even 的普通求值路径差；同父 all−even 的角规则改变；以及 final−parent 的 even、odd、all 三个**各自同函数**变化。不把 final-$\Phi_{2N}$ 减 parent-$\Phi_N$ 当作单独求解收益。

每个 reader block 完整形成三份结果后才计入 returned rows。算术失败时报告实际已返回范围、失败位置及 returned-only 非归一和；完整 mean Phi/max 保持 `null`，未返回行不补零。真实 solver 非零退出不会被说成自然成功；若其父只读部分能够返回，就单独记录该已付范围。运行被外部截断而没有返回时，也没有虚构预算完成或结果。

所有结论仍是有限普通浮点读出。它没有支付连续角间峰、连续径向度量、reach 或 README 的 $10^{-6}$ 完成条件，也不扩大 $M$ 所定义的场空间。后续是否值得真正进行 N-only 方向，应由实际新父和主线安排决定；本次只有源码准备，没有改动现队列。

## 8. 已做的源码核对

新源已作 AST 解析与编译；11 个动态覆盖参数和 17 个共有依赖参数与两个冻结完整 driver 的 parser 逐项静态对上，R671 的 node/scalar/lambda/keep-q 参数也与实际入口相符。检查没有加载 candidate、构造数组、执行科学模块或新增数值 fixture。已有科学依赖的冻结源均未修改。

此前未执行草稿 `a82eb4200f976190a4dbfdbba7333ea2d5e55b0bdbce733c0161f2e6f442d6fa` 对可选 external final 只比较粗变量维数，可能容纳不同中心的同维粗基。当前 e738 仅补足上述粗基与实际延续策略字段比较，并把同策略分支检查扩到 original 父；own scientific argv 原本已正确继承这些参数。静态确认新增的 15 个报告字段在两个冻结原 driver 中均存在。没有运行或重跑科学结果，旧 a82 不作为实际执行证据。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
