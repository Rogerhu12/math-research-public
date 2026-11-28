# 原固定 support M32：独立资源入口 v3 的真实完整节点准备

这是原 fixed=True support 模型的独立资源／恢复入口，不是旧 warm/phase v3 模型。它接[真实完整节点恢复初猜](2026-11-28-analytic-fixed-support-m32-nodal-initializer.md)，保留 λ = .002、δ = .06413464112662924、gauge q = .06、warp_reference_q = .06（warp_e = .48）、mean 1168、原线性 Robin 端条件及全部原非线性验收门槛。

新源码 [`fixed_support_literal_driver_v3.py`](../scripts/resume_20261128/analytic/fixed_support_literal_driver_v3.py) SHA 为 `8ebbda010585c88c828d09bb53096a229c960672f25ea959964185c871370ff5`。旧实际接受 M24 绑定入口仍为 SHA `6ca29978b422201e9312b30205de91d4abf3f9ac5c0ca78c627470c7df41a06e`，旧中断 M32 v2 入口仍为 `756f55e7d4dc691cad0597c1ecee18a26d292d8676d46aca3342c4f765ff077e`，两者字节均未改动。

新入口只接明确的完整 nodal 恢复合同，要求同 M、同 angular、refine = 1 和相同参数尺度。原 1497 个 x、97×1497 的 y、32 个 p 和 31 个 pscale 直接复制；跳过旧入口即使同 M 也会执行的参数乘除尺度往返、网格合并和 PPoly 状态重评价。原 inlet projection 实际检查为完全相同，不添加补正。

实际 session 13270 以 `--prepare-only` 正常退出 0。运行到完整原节点 RHS 和 7 个真实节点的固定 support 参数语义检查后返回，没有执行 BVP，也没有组装完整 J。原 RHS 按 block 64 求值；它与恢复初猜 cubic 的节点导数最大差为 2.710505431213761e−20。q_actual = .060000491077815986；参数 p0 仍只改变 log(q_actual/q_seed)，其正负扰动没有改变固定 Flow 或完整 profile。

保存后又独立重新读取真实 donor checkpoint 和本次 `prepared-initial.npz`，x、y、p、pscale 的形状、dtype 和逐元素字节全部相等。初始网格仍为 1497 点。实际峰 RSS 451740 KiB，用时 88.00065581400122 秒，进程已退出并释放资源。

新入口还接入已由独立实际矩阵核验过的 `direct_csc_collocation.py`，保留每个原矩阵 entry/显式零；并保留重建 J 前释放旧 factor、无引用环 BlockQR wrapper、完整原 J residual 回检和独立完整 nodal checkpoint。完整核心 evaluate memo 使用已核原值／Jacobian 位同的实现。**本次 prepare-only 未到这些完整 J/分解操作，其实际求解正确性和终态不能由准备返回替代。**

实际目录 `held10-analytic-work/fixed-lambda002-m32-v3-prepare`；run SHA 为 `c7903c542044e96dc17dd2d084f677b52fe9f71752b30ed5d55d3ea4383353ff`，prepared 初猜 SHA 为 `4da6eaef2a2d7c9b0139df225b0cd1a63b69d95689ee6b9fc4fba5acef63e010`。本次修改后执行的原 main 文本 SHA 为 `52c7e61074da9b5dd37d74d4109599a9a7c43b810497590d7799afe8970c0927`，其未改原 main 为 `60169cde213fb0f8b7df8440b03f594898188c5abbd2f0f6926076a66f94c297`。

完整实际记录见[相邻 JSON](2026-11-28-analytic-fixed-support-m32-v3-prepared.json)，SHA `40c6087a72dcb399cf334259f3b1246244acbb20ec4e8291c81967c6f647798f`。M32 仍未接受；正式求解等待设计 .128/M48 后的明确前缀大 J 资源窗口，随后仍须全额执行原 RMS、physical BC 和完整 metric audit。
