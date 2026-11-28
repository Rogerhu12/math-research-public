# 原完整 Jacobian 直接 CSR，并与完整 QR 共享同一矩阵

独立新入口直接按原 collocation 行填 sorted CSR，每行完整保存2n+k项，包括原显式零。所有 A/B/P 公式、逐元素运算顺序、参数 midpoint 原位副作用、端点行和参数列均不变。相较已核 CSC 入口，BlockQR 原 tocsr 不再在构造期同时持有另一份全量 CSC；真正原矩阵继续常驻，真实残差及原非线性门全部保留。

真 M24/879 节点输入实际重建，64191×64191、10912470存储项。新 CSR 与原完整 CSC 转 CSR，以及历史保存矩阵的 CSR，data、indices、indptr 逐位相同；原 prepare_sys 实际安装及 dp_middle 副作用也逐位同。随后完整 QR 方向、所有 factor/solve stats 同样逐位相同，实际原矩阵绝对残差为2.346385251160285e−21；BlockQR.matrix 与输入 CSR 的存储共享已实核。详见 [完整小记录](2026-11-28-design-complete-csr-assembly-qr-bitwise.json)。

实际核验66.49秒，峰803424KiB，仍只是对照过程峰。新的逐 mesh 资源估计按当次真实 pre-J RSS，而不再把 M40 的整个基线按 n²外推；完整偏导、CSR、递归旧/新 edge 与累计QR factor、诊断块均显式计入，并另留64MiB内部和512MiB外部余量。预算是调度估计，不是峰值保证或数学验收门。

恢复入口明确消费[交接竞态保存的完整节点](2026-11-28-design-m48-nodal-interrupt-race.md)，在原 RHS 前逐字面恢复 x/y/p/pscale，随后原域、Newton、RMS、physical BC 和 metric audit照常。初猜身份不会被标作新接受场。当前实际首节点入口见 [运行记录](2026-11-28-design-csr-m48-actual-entry.json)，全部四数组以及NPZ SHA与真实中断nodal一致，原域检查通过，按当次4.549GiB可用内存真实放行原首J。

七个独立源为 direct_csr_collocation、check_direct_csr_assembly、prefix_csr_assembly_driver、complete_csr_memory_budget、prefix_csr_budget_driver、literal_design_nodal_restart、run_design_qr_dispatch_v4（均在 scripts/resume_20261128/design）。已绑定的 CSC/V5/旧QR 源字节不改。矩阵身份及入口返回都不代替最终 BVP／metric 验收。
