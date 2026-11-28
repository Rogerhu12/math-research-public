# M48 完整 CSR 前置映射恢复入口

2026-11-28 UTC；入口与来源准备，尚未新增 BVP。

本次从最新实际 `design-secant-factor-mmap-m48-20261128/attempt-000/run.json`（ae21e9fa…）的 e889dd15… 完整 952×145 nodal 接续。独立 `nodal_recovery_provenance.recover` 实际重核四层 run / source / input / checkpoint / literal 恢复记录，最终绑定原 .032/.064 两个真实接受源和其完整双源 M48 升模割线；没有重放该初猜或已经付出的原 Newton 步。

v7 controller 保原 .128、.192、.256、.384、.512、.75、1 目标与 M48、64、80、96、128 原谱门升模规则；信号与 MemoryError 仍只作为工程中断，不做 λ 二分。新变化只有完整 CSR 在 QR 前映射、所有因子在 QR 后映射，以及相应当前 mesh 的资源预算/独占临时存储清理。原 V5 精确 δ 列、完整 state/support 列、所有原 BVP/域/metric 门均沿用。两种 backing 均在真实已保存 M16 全矩阵逐位检查中通过，旧源不动。

952×145 / 48 参数时，完整 direct-CSR 装配变量峰预算 1,012,464,116 B，完整 warm matrix+factor 诊断 1,270,976,052 B，保守复制重叠 1,279,512,108 B。以前次真实 pre-J RSS 246,059,008 B 为参考，再计 64 MiB 其他开销和 512 MiB 外余量，总新进程估计 2,030.898 MiB。实际 nodal 门会重新测 RSS，只以实测 RssAnon 作已经占用的信用；不能将 mapped 逻辑大小抵扣 MemAvailable。

完整 CSR + 所有因子 + 两份 manifest/对齐上界 + 512 MiB 外磁盘余量需要 1,825,948,803 B。每次 J 前和 CSR 预分配前都重新读实际磁盘；原完整 edges 抽取后的 CSR page-release 真实成功后，再作递归 QR 的实时 RAM 门。完整 warm solve 仍按所有矩阵/因子页面可能同时驻留计。原求解返回后，只有两套 store 的 DONTNEED 均真实成功才把方向交回原非线性阶段。预算是调度估计，不是内存保证，也不解释既往 −9。

源 SHA、完整 CLI 与四层来源记录见同名 JSON 及 scratch preparation/command.json。三个新入口实际 --help 和所有新源 compile 均 exit 0；未再跑其他数值探针。真实启动、原门与终态将另记，不能把本入口准备写成 λ=.128 接受。
