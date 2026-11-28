# 固定 g v6：最新真实节点与完整工作峰预算，仅准备未启动

日期：2026-11-28。独立 v6 源已编译，并对原固定 support 入口的 8 处声明替换逐项核唯一性、编译生成的实际 main。**尚未运行 v6 的模型准备或 BVP；当前明确不启动这一 RAM 存储路径。** 新设计链再次实际 signal9 后，团队转向独立 scratch-backed 完整 CSR/QR 存储；其真实核验完成后才接新的后继版本。

## 唯一初猜与原方程

输入为已实际返回的 `recover_fixed_support_nodal_v2.py` 初猜：最新 dedd 完整节点检查点的 1497 个 x、97 个状态分量、32 个参数与全部尺度逐位保留，新 initial SHA256 为 `8c4305b836eaa5acb34a50108bb971d117e7ce4014fb754dc3cc5a886bd8959b`。没有重复旧 4da 初猜，没有假 raw 返回。

同 λ=.002、同物理 δ=.06413464112662924、同完整 g、gauge q=.06、warp_reference_q=.06、实际 warp_e=.48、mean1168、M32、angular1024、tol2e-7、原 q branch、BC 归一化与物理 BC 门均保留。原末端仍为线性 Robin；此准备不能用于 fullDN 闭图接受。

v6 保 RHS64/Jac32 的原调用分组，在每块 finally 只清理不可达对象。原模型只持有同一个 live fixed Flow；不把设计 δ± Flow 路径或其资源原因搬到这里。此前已完成同一真实源的完整小块 RHS/dy/dp 同组逐位核对，因此不重复额外小 log(q) 差分探针；原完整求解仍使用全部原 Jacobian 列和全部原非线性门。

## 每个 mesh 的实际内存门

新增 `fixed_support_memory_budget.py` 继承已核共享 CSR/streamed-QR 账目。完整 J 的 prepare_sys 包装先保存当前**完整原节点状态**，再测当前 RSS、重新计算此 mesh 的预算；节点偏导及中点偏导均须在该门之后执行。此前完整因子在构造新 J 前释放，弱引用只用于观察存活，不形成保留因子的自环。

1497 节点的明确数组账目为：

| 占用项 | 字节 |
| --- | ---: |
| 包括全部显式零的完整 CSR | 394474560 |
| 最终全部内部 QR 因子数组 | 488990580 |
| 原设计实际整进程记录校准的非线性工作储备 | 1073741824 |
| 固定 RHS64/Jac32 的额外分组工作储备 | 536870912 |

还分别计算全部节点/中点偏导、CSR 装配临时量、递归 QR 同时存活的前后 edge、完整诊断块、16 个完整场向量与 64 MiB 杂项。预备的零 baseline 纯账目给出新分配峰加 512 MiB 外部余量共 **2954.538013458252 MiB**；这只是便于读者查看增量。真正执行时每次 pre-J 的 baseline 都必须从该进程真实测量，不能把零 baseline 称为实测 RSS。

共享的 1 GiB 非线性储备来自原 M48 设计整进程记录，其径向分组为 8；它不是固定 64/32 调用的已证明界。新增独立 512 MiB 分组储备明确支付这个不同设置，没有宣称两者工作峰相同。所有预算均标为保守调度估计，不是内存保证，也不证明任何 signal9 的具体原因。

完整因子仍存活时，原 RHS 非线性回评和完整线性求解均再读可用内存。该阶段可抵扣的保留量只来自实际 CSR data/indices/indptr 与实际记录的因子数组字节，另加真实 pre-J baseline；不把任意未知 RSS 当已预算内存。失败只动态等待原资源门，不改变 λ、容差、方程、网格规则、参数数目或接受标准。

## 冻结来源与当前状态

- 独立入口：`scripts/resume_20261128/analytic/fixed_support_literal_driver_v6.py`，SHA256 `8a226d98e1d4235a82aa2e7ef81a65af85ccdb49df560e26a1e4960626f4f5d3`。
- 真实新节点恢复源、原完整 CSR、原 streamed QR、共享预算 v1/v2、finally 包装及生成 main 的 SHA 全在配套 JSON。
- 预备命令保存在 `held10-analytic-work/fixed-lambda002-m32-v6-preparation/prepared-command.json`；**未执行**。
- M32 的数学状态没有晋级；下一存储后继必须使用独立新文件，并继续最新完整节点，不改任何旧 hash-bound 源。
