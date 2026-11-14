# 新78718 prefix 存储的生产调用链核对

日期：2026-11-10；numerical_recovery；纯源码/接口核对。
**没有执行新 producer、common-cut 构造、candidate 全门或连续证书；production_ready=false。**
本稿核对 root 已生成的新源与原生产调用链，不替代对全部134处替换的独立语义审查。
源码不作修改，单容器仍为当前优先分支；只有实际大小限制触发且新层独审后采用本支路。

root 的适配与 reader 实跑范围见
`2026-11-10-78718-storage-adapters-and-reader-check.md`。
本次另作 AST/source SHA 核对（实际工具 cb9449，自然 exit0，0数学调用），
报告 `2026-11-10-78718-numerical-storage-chain-source-pins.json`，10,407 B，
SHA 0ea6f4eea5442df8d2c4b75e94d95f80db79ce7e3e4f48e2e4a8ba7c26b29d1a。
新 terminal 的13项 PREFIX_SOURCES 全部逐字匹配，21项 SOURCES 字典完全等于原 terminal，
其全部34个来源文件实际 SHA 均匹配。两组作用域不同，不能拿旧源SHA代替新 prefix 源。

## 1. 旧 whole 程序不需要存储适配

全文读 `db6f-root-whole-metric-reach-v2.py` 的 main 与 separate_metric_certificate。
它从闭预算的7项 inputs 重哈希 JSON 证明文件，核 geometry 与 tail manifest 的连接，
从已给标量界以 Fraction 组成 metric/reach/H/held/非全等门；它不直接读取 prefix NPZ，
也没有把闭预算生产者 SHA 固定为旧 wrapper。
新 closed-budget 输出仍给全套同名字段及同样的7项 inputs，只新增 prefix_storage_bindings。
因此该**静态接口**可继续使用原 whole 程序，不需要为 prefix 格式另派生 whole。

新 terminal.candidate 明确要求 budget.script_sha256 对应
`78718-prefix-closed-budget-storage-v1.py`，同时继续要求
base_closed_budget_script_sha256 为旧 `db6f-root-closed-budget-v2.py` 的冻结SHA。
whole 自己的 script SHA 仍核原 `db6f-root-whole-metric-reach-v2.py`。
这使新 prefix wrapper 的来源身份与原精确标量/尾背景家族分开。
单独 whole 的正常 1e−6门仍不支付原2e−9终门。

## 2. 实际应替换的 CLI 与保留的 CLI

参数及数字采用原 `numerical-post-csc-chain.md` 已审条件生产清单；仅在选中本支路时，
以下 prefix 文件名整体替换，所有输出使用同一个新图的、未使用的路径。
原 run02 已失败，该旧清单的输入状态不可复用；未来成功 CP 必须先过其实际新 final gate，
并从该 CP 解析自己的真实末尾包。

| 阶段 | 本支路 CLI/依赖 | 接口核对 |
|---|---|---|
| 基础镜射 prefix | `78718-prefix-mirror-hermite-storage-v1.py` | 原 source-root/checkpoint/linear-port、M24/N768/Q8/subdivide1/ell0 参数不变；内部调用新 fullxyz producer |
| 同一解析目标 | `78718-prefix-metric-supplier-storage-v1.py` | 读取新 defining base；目标自身的 NPZ 保持原格式 |
| 基础 metric | `78718-prefix-metric-polynomial-storage-v1.py` | 新 ExactHermite 读取 prefix；原目标包读取保持 |
| 精确 bridge | **原** `db6f-root-exact-bridge.py` | 只读 geometry/target/tail/metric JSON；不读取 prefix 的物理容器 |
| common-cut make/geometry/metric/moment | `78718-prefix-common-cut-storage-v1.py` | 对应新 continuous/poly/moment 依赖；CLI任务与参数不变 |
| 必要局部过估计诊断 | `78718-prefix-metric-budget-storage-v1.py` | 新 angular-arithmetic / new ExactHermite；不能充完整证书 |
| 必要完整角界 | `78718-prefix-angular-metric-storage-v1.py` | 绑定新 common/target/poly/base/arithmetic；完整区间门保持 |
| 闭预算 | `78718-prefix-closed-budget-storage-v1.py` | 读取新 common 与 ExactHermite；原 transfer-v3/背景政策不变 |
| whole | **原** `db6f-root-whole-metric-reach-v2.py` | 如第1节；若不跑 metric-only，省对应可选参数 |
| 原2e−9终门 | `78718-prefix-terminal-error-storage-v1.py` | 新prefix家族；原BOUND、FACTOR、LOWER和M12/背景来源保持 |
| mesh plan/build | `78718-prefix-export-closed-mesh-storage-v1.py` | 新prefix依赖，原tail stream与实际同图whole；源账本附新helper/codec |
| mesh字节/小构件独审 | `78718-prefix-review-closed-mesh-storage-v1.py` | 冻结新exporter SHA及新supplier；仍须真实独立replay manifest |
| mesh离散拓扑审计 | **原** `db6f-audit-closed-mesh.py` | 只消费导出的PLY，不读prefix NPZ |

全部 tail exporter/collar/first-bounds、transfer-v3、full-tail、metric-only、
complete-metric-report 仍使用原文件，不能为了统一前缀而改用新 angular-arithmetic 的 tail CLI。
新 angular-arithmetic 只是 prefix 局部界所需的数学副本；其文件包含的 tail load_packet
仍读原 tail 背景 NPZ，它不是新的 tail 证明来源。

`db6f-tail-sample-background-height.mjs` 仍使用原文件：它消费 manifest/calibrations/
alpha/radii JSON，与 prefix NPZ 无直接接口。新 mesh plan 写出的 radii schema 未改变。

## 3. 残留直接 NPZ 入口逐类核对

本次 rg/AST 与上下文读取限定于上表实际可达路径，不声称扫描了整个仓库所有程序。

- fullxyz.SharedHermite 和 continuous.ExactHermite：直接 `np.load` 的参数已经是
  storage.read_payload 取得并核完整 SHA 的原逻辑 gzip/NPZ 字节。
- mirror：base.build 完成后经新 helper 读取原三数组，仅执行原 inlet parity 修改，
  以原 `np.savez`/gzip 顺序重序列化一次，然后存储。descriptor/parts 的文件名包含逻辑SHA，
  因而初步未镜射 payload 与最终镜射 payload 不会冲突覆盖；只由最终元数据所指闭包定义图。
  这项是源码核对，不是 producer 的实际新执行。
- common-cut 两处直接 NPZ 读取均先定位 defining base。M24 基础数组与扩充后的至少M64
  common元数据分别核查，不能用扩充mode数解释基础数组。
- angular-metric.validate_inputs 的 geometry NPZ 使用同一 defining base payload；
  另一个 `np.load(target_data)` 读取原解析目标包，属于不同格式。
- metric-polynomial、metric-budget 里的 target data_file，以及新 supplier 自己的
  target-data NPZ：均为解析目标(a/e/ep的系数区间)，并非遗漏的 prefix nodal NPZ。
  此分支没有改写该格式，也没有证明任意未来目标文件都不会触及大小上限；实际仍逐件检查。
- 新 angular-arithmetic.load_packet：对象是 tail 背景分区包；原 tail 输入格式保持。
- 新 mesh review 的 `np.load(mask_path)['fixed']`：对象是生成的固定顶点mask，
  不含prefix jets；原输出/审计格式保持。
- terminal 的 remaining data_file 引用分别是固定M12点包、背景转包、tail证书行数据和
  解析目标包。candidate 的 prefix 物理存储路径改由 prefix_storage 完整核 descriptor/parts，
  没有再把 base['data_sha256'] 当作某一个物理单文件SHA。

## 4. 报告来源与消费者闭包

新 common-cut 的四任务明确装载新 continuous/poly/moment；其读数组入口和所绑定的
base_geometry 保持一致。geometry、metric、moment、target、angular 与 closed-budget
各报告携带的 storage_bindings，均在新 terminal 的 prefix_storage_ledger 对实际闭包核对。
该检查允许报告旧绝对路径迁移，但要求实际 basename/bytes/SHA/multiplicity 匹配，
没有把找不到的旧路径当作自动通过。

新 mesh prepare 根据 common_cut_implementation_sha256 唯一选择新 common，
把新 continuous 类安装为该prefix对象；tail 则用原 StreamingExactIntegratedTail。
其 source_sha256 字典把新prefix读者/算术/helper/codec与原tail来源分别列出。
新 mesh review 的固定 EXPORTER_SHA 实际匹配当前新 exporter。
这些静态连接与 root 已实跑的 M2/M24 reader/terminal.storage fixture 相容。

**没有发现上述实际生产路径中仍将新prefix descriptor误当旧data_file的剩余入口。**
这只是当前源版本的接口结论；完整producer/common-cut/candidate、全域连续证书与网格
尚未在新真实候选上执行。完整独审及实际生产失败的可能性都仍保留，不能据本稿写ready=true。
