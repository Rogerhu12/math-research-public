# n4：冻结胶囊 floor 0.1 与生产 DN floor 0.05 的入口区别

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 接口发现与明确选择

准备 native batch 接入时，只读源码和原 checkpoint 发现：**已有三段冻结胶囊的域 floor 是 0.1，而实际生产 DN 的域 floor 是 0.05**。原执行配置没有显式 `projectionFloor` 键；两个入口的默认值传播不同。

后续生产接口明确保留原 DN 的 **0.05**。不能把胶囊较强的 0.1 门默认为生产原门，也不能直接把只接受 0.1 的已执行 native 库接到生产后声称全部原规则相同。当前全部已执行源码、库、胶囊、MP 和 LD 输出保持冻结。

这项发现不改变既有三段输出相同或有限 MP90 算术误差的结论；它限定那些记录中的“原规则”为其**已冻结胶囊入口的规则**，不把该身份推广到整个生产入口。

## 默认值如何传播

精确文件、来源 SHA256、单一命中行和完整源字面量由 `scripts/resume_n4_tail/native_production_floor_binding.json` 保存。关键链如下：

| 路径 | 已存在的字面定义或调用 | 有效 floor |
|---|---|---:|
| `950f-tail-stage-core.mjs` 的 `createCompactTailShooting` | 解构默认 `projectionFloor=.05`，随后显式传给 `engineFactory` | 0.05 |
| `950f-tail-stage-split.mjs` | 从 `dn.tail.parameters` 取 `p.projectionFloor`，显式传给 split 引擎 | 0.05 |
| `general_root_tail_momentum.mjs` 直接引擎入口 | `floor=options.projectionFloor??.1` | 未传键时为 0.1 |
| `frozen_stage_arithmetic_bridge.mjs` | 从原 fixture 取 `cfg=frozen.config`，直接构造 `createSplitFluxMomentumTailEngine({...cfg,...})` | 0.1 |
| 同一 bridge 的胶囊记录 | `floor:cfg.projectionFloor??.1` | 记录为 0.1 |
| `native_extended/frozen_flow.cpp` | 配置检查硬锁 `c.floor!=.1` 时拒绝 | 只允许 0.1 |

原完整失败 CP 是 `n4_work/raw-primaryb016-lam002-actual-m20-parts32-v1/one-ulp-tail.json.gz`，SHA256 `b4356eabf97014127a364ef34b7951a930f4b184d8c6f4c4db83c161b2cbbb5e`。其 `config` 确实缺少 `projectionFloor`，而保存的 `response.checkpoint.parameters.projectionFloor` 为 **0.05**。原 `solveTolerance` 仍是 $2\times10^{-9}$；域 floor 和尾残差门是两件不同的事。

胶囊 summary 的 SHA256 为 `3785fff5412ec751d2275d3f774b6c7503bfecb7ad781a38068f811f06ab35f7`；其 `root_rules.floor` 明确为 **0.1**。已执行 native C++ SHA256 `916d0a948a15100f9bb68b255c2192460efe249c08a3559ea9fb800fbb59ac3f` 的配置检查与该胶囊一致。

## 已保存三个 stage 的实际范围

只读 collector 检查了胶囊现有的全部 `domain` 事件，包括原求根迭代及试步评估。全部保存的 D、S、A 判断均通过较强的 0.1；没有重算任何根或流。

| stage | 保存的 domain 事件数 | 最小 D | 最小 S | 最小 A |
|---:|---:|---:|---:|---:|
| 43 | 40960 | 0.999945619371 | 0.999999996500 | 0.999324437567 |
| 38 | 40960 | 0.999947926223 | 0.999999996111 | 0.998981843345 |
| 175 | 24576 | 0.999999639022 | 0.999999999999976 | 0.999975782689 |

此前原 DN 路径保存的三个完整 42 项输出，与胶囊参考输出仍逐位相同。本次 collector 再次只读核对这些原字节。所选三段已经观察到的更强域比较均通过，所以这里没有发现 floor 差异造成已保存路径的域拒绝变化；**这不是任意新状态、全 2304 段或未来 Newton 试步的等价证书**。

[native double 的 116608 事件基线](2026-11-18-n4-native-double-exact-baseline.md) 对照的是该胶囊的原保存事件，即其 floor 0.1。此前三段 [LD 状态与完整 Jacobian 同态](2026-11-18-n4-native-longdouble-pair-terminal.md)、既有 MP90，以及沿保存 MP90 state／L 的独立变分参照，也都应按这个具体冻结入口理解。它们没有付清生产 floor 0.05 的配置接入。

## 修复范围与尚未执行项

下一 owned native 版本只允许并显式绑定两个已声明 floor：生产的 0.05，以及用于既有接口身份对照的 0.1。原求根方程、Newton 矩阵、30 次上限、20 个减半因子、停止和 fallback 常数、RK、字面隐式 Jacobian 与所有边界转换保持原定义。已执行的 0.1 版本不修改。

新源码／计划需先明确验证位置，再单独编译和记录其身份；不能在这条只读发现中提前宣称新编译或新求解成功。后续可用原三段输入、两个 floor 的完整 42 项及 $42\times40$ batch 输出检查配置传播与新 ABI 身份，但这也不是重复扫描算法或绕过原 DN 门。

本条由 `record_native_production_floor_binding.py` 读取现有来源、配置和 trace 生成紧凑记录。没有 import 引擎、重建几何、调用数学内核、编译新库、改变生产 source，或得到新的 actual-tail 接受。
