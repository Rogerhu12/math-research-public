# actual68 / actual70：同父阻尼试验的完整有限数组对照

类型：原 Actions 数值产物的字节证据；不是新的科学计算或接受条件。

作者：`exact_refinement`。日期：2026-11-15 UTC。

## 1. 结论及范围

actual68 与 actual70 确实使用同一 actual66 父 warm/status、同一冻结的 21-query 算子、同一 43008 行约束说明和同一连续局部坐标。两轮共有的 60 个来源文件 SHA 逐一相同，导出的 `base-and-local-layout.npz` 整文件也相同。

但是，实际重新形成的有限数组 **并非全部逐字相同**。全部 21 处的 `Gamma` 和完整 `rows` 块，以及保存的 `b/g` 不同；原完整 A 的五个输入块所报告的 raw SHA 也不同。全部基线 β、全部 `Pi`、约束右端 `c`、尺度 `S` 和行权重 `Wr` 相同。因此可以称它为同父、同源码约定、同查询下把 λ 从 270 改为 27 的算法试验；不能进一步称它为固定全部 binary64 的 A/B/b/g、只改变 λ 的严格有限模型对照。

本记录没有计算不同元素的绝对误差、相对误差或 ULP，也没有据哈希判断差异只在末位或足以解释试步变化。下面两个 merit 的确只在已保存十进制输出的末段不同；这个事实不能替代对其余数组差异大小的计算。

原70 warm、FD 和 artifact 均已完成；该 run 的最后 publisher 失败不能改写成科学失败。原70试步、实际候选和 FD 叙述由对应 actual70 note 保留。本附记只限定其与68的模型对照范围，不重复全部试步或增加跨 run 通过门。

## 2. 原输入与读回身份

| 项目 | actual68 | actual70 |
|---|---|---|
| 科学 run | `43653811809` | `43656059206` |
| 原 artifact | `14137921466` | `14139045881` |
| 原 ZIP 字节 | 590574983 | 606816318 |
| 原 ZIP SHA256 | `0fe545ea42c48bb2d5551afddb86190af3c7ff1a14509b9f1ed5a6e5d0e53784` | `e45f32846bf48cb474c738c58675b30dada435229846ed3b27e319d8dcb63bd9` |
| 完整字节读回 run | `43655562831` | `43657876708` |
| 完整 audit JSON 字节 | 723383 | 784652 |
| 完整 audit JSON SHA256 | `2e5b678efa113789649c15b893e07d93fdd94fef4ab44086e308a1d11e0e8abb` | `e1f8d6ba9778f822ef67b78e16a172d1a7867050b26fb4918c58756dc93978a1` |
| 原 λ | 270 | 27 |

共用父 warm SHA 为 `80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6`，原父 status SHA 为 `04ace7953961b3905d2b72639976025dc9c4efd0bef7b932585cf21f8249bcd4`。完整父 producer 子树和真实新 warm 的身份均由各自原读者绑定。

共用算子 `geometry_20261114_twenty_one_query_domain_operator.py` SHA 为 `0007a3dd345cb60172c75ef6490fa3f0bbcfdc178be90e532120302fc6c15a65`。68生产者 SHA 为 `b7956525ce484c4ed17724c2d84c04b6080688e2d0afc8367c5ba46cbf8626f2`；70独立 λ27 生产者 SHA 为 `a8dd293b4b10ab45a2e69dd1e3e37a2032e4af3eb4d5f21eefa556277cb0d64c`。

两份完成的 public Actions reader 已各自读取完整原 artifact、数组及来源，并保存有界原报告副本。此次本地只用标准库重新核这些小包和完整 audit receipt 的文件 SHA，再逐项比较其中已核的完整数组身份。没有再次下载两份约 0.6 GB 原包，没有重新运行 NumPy、SciPy、原科学模块或算子。

比较源为 `exact_20261115_compare_actual68_70_readback_bytes.py`，15025 B，SHA `4d02c9cc698c7f4f74cc3fe0d311de092ab82c89620f37d995c266079dad82d6`。

## 3. 完整 B 导出与基点：哪些相同、哪些不同

每轮均有 190 个 domain NPZ 文件和 1226 个内部数组身份。本次比较覆盖两轮的完整文件集合，没有只检查最近失效点。

| 对象 | 实际字节对照 |
|---|---|
| `base-and-local-layout.npz` | 整压缩文件相同：3810064 B，SHA `f92a70aa5756135a281f8dfdb88772e0e8525c57646cfd5ece405e6143cc718d`；所有内部数组相同 |
| 全 43008 个 typed-query 基线 β | 完整数组相同 |
| 21 个 query 的全部 `Pi` | 每处完整数组相同 |
| 21 个 query 的全部 `Gamma` | 每处完整数组 SHA 不同 |
| 21 个 query 的全部 `rows` | 每处完整数组 SHA 不同 |
| 各 query 的列/行索引、其余几何基点与导出成员 | 读者列出的其余数组身份相同 |

不同的内部数组恰为 168 个 `Gamma` chunk 和 168 个 `rows` chunk，即每处完整 2048 角按原八块保存的两类数组，共 336 个。其余 890 个数组相同。168 个 NPZ 文件含上述差异；其余 22 个文件的内部数组均相同。

这已经是实际 payload 的不同，不能把它仅解释为新 producer 导致的 model metadata SHA 变化。与此同时，model metadata SHA 本身确实也不同：68为 `7e5512fa872b45e87fd88e5a2a0c4857ab8881fef8a2e47b3d78b77075486bcc`，70为 `23df7023ac5215339c8df134782f00b3381c2ccae5cdf8e158d349201031000d`。元数据 SHA 和科学数组 SHA 在本报告中分别比较。

相同的 typed query 说明、基点、β、Pi 与列映射排除了“换了父场、遗漏原查询或改变局部布局”这一类标签混淆；它们不证明 Γ/rows 的浮点形成完全可重复，也没有给出实际差异量级或根因。

## 4. b、g、约束 c 与完整 A 输入身份

这里 `original_c` 是约束 `Bz+c>=0` 中的完整 43008 维余量，**不是** C 投影的列预条件对角。

| 完整保存数组 | actual68 raw SHA256 | actual70 raw SHA256 | 比较 |
|---|---|---|---|
| `original_b`，236036 项 | `f5a4482bc87b9cdab4792bcc7ad8b1df3c28cd4e928b1dce454a63151d41b360` | `87c74c1546708fd71b881811f076a7f99da2dd2ccff6fb3541ce71bc62198018` | 不同 |
| `original_g`，236036 项 | `fd8b185b8497cd8b2503eec258bd747a9c7fef15ea5418182030ec3c4c537da3` | `091e1b9a48c935fce210e498c89c4a3e2f1e63fd655d2d88fa7df63fbcba8ea2` | 不同 |
| `original_c`，43008 项 | `7a6f3da063cd225464b8a6c2eb6f0f8e71b32061795c17fab03bb9d42c2973c5` | 同左 | 相同 |

对完整 A 链输入，原库在每轮形成与恢复时记录了九项形状、字节数和 raw SHA，且同一轮两处记录相同。这九项原大 payload 没有完整导出，因此以下是 **原 Actions 报告的输入哈希对照**，不能冒充本地独立重新读取全 A：

| 输入 | 两轮原 raw SHA 记录 |
|---|---|
| `L`、`R`、`P`、`BY`、`BC` | 不同 |
| `BP`、`inlet`、`S`、`Wr` | 相同 |

具体完整 SHA、形状、dtype、order 和字节数均存于小 JSON 的 `reported_full_A_inputs`。local condensation 的14份导出 raw 中，`local-indices` 相同；其余13份 raw 不同，包括原 `g`、affine、local root/gradient/center、实际 full recovery 和其残差。λ改变本就需要重建阻尼因子及局部 root；本次另有实际 A/b/g/B 差异，所以不能把所有 root 差异单独归因于 λ。

来源文件对照的60个共同文件没有任何 SHA 不同。68另有原21-query observer/FD；70另有独立 λ27 warm/observer/FD。这一结果支持“原共享源码未被静默替换”，但不能据此认定跨 worker 的浮点数组必逐位一致。本次没有对机器/BLAS、执行顺序或其他原因作未经原证据支持的归因。

## 5. 原标量和后续解释边界

下面只复制两个原 `model-000.json` 的存值，不重新计算差值、比率或范数：

| 原字段 | actual68 | actual70 |
|---|---:|---:|
| `fixed_weight_merit_before` | 43.75526502490638 | 43.755265024906336 |
| `actual_coefficient_direction_max` | 0.00014514922579697757 | 0.006661320259912167 |
| `selected_angle_row_count` | 43008 | 43008 |
| `accepted` | true | true |

不同 λ 下实际有限预算 QP、恢复和真实回溯的结果仍是有效的各自运行事实。它们不能升级成固定同一有限 A/B/b/g 的严格单参数因果结论，也不能把更大方向、较小接受 α 或不同 domain 失败只归因于 λ。完整非线性接受仍由各轮原门决定；本次字节差异既不撤销这些原接受，也不新增一个等待比对通过的条件。

若后续确实需要固定有限模型的阻尼因果对照，可在同一次公开 Actions 中形成一次 A/B/b/g/weights 后复用该实例，仅改变 λ 与其 C/QR/root，然后各自读原结果。本次没有执行这项额外实验，它也不是继续现有主线的前置要求。

## 6. 可复核产物

本批 JSON 已按原相对文件名保存在 `notes/actual68-70-byte-comparison/`，保持 descriptor 路径和 SHA：

- [summary.json](actual68-70-byte-comparison/summary.json)：比较器实际完成摘要；
- [science-array-comparison-summary.json](actual68-70-byte-comparison/science-array-comparison-summary.json)：28264 B，SHA `a8bf3433b93cb181b4a86ff8c993f00d358fa4b2d5a6baf00e42af1b2b85696b`，含完整小表、来源交叉、基点成员和复制的原数值；
- [complete-byte-comparison.json.gz](actual68-70-byte-comparison/complete-byte-comparison.json.gz)：179038 B，SHA `7517eb91b43fa04462254bc46954b589372de94c3e53874194af73437bbaeece`，完整逐文件、逐数组和逐 query-group 身份，不包含科学 raw payload。

本地只进行了文件/JSON/哈希/元数据计数与相等比较。没有新的科学数组、范数、作用、比率、优化或有理账。
