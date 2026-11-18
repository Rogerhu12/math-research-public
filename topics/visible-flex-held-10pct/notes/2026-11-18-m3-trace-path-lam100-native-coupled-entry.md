# 从完整 λ=.64 状态直接继续 literal λ=1 的真实联立入口

**状态：一个已实际启动的原联立求解入口；本条不声明终态成功。**

上一份 [λ=.64 完整有限状态](2026-11-18-m3-trace-path-lam064-native-prefix-completed.md) 已完成原 inner、实际 BC、真实尾、mean/prefix audit 与实际 seam，但 metric 和接缝误差仍未满足最终标准。本条不重做这些工作，而按已确定的有限同伦继续到 $\lambda=1$。

定义保持原 $Q_*=$ binary64 `0.06` 的精确实数，故唯一指定的 support seed 为

$$
q_1=\operatorname{RN}\!\left(\frac{Q_*}{P(1)}\right)
=0.05210565550627671.
$$

数值 gauge、warp reference 和七个参数尺度仍为原 `.06` 配置；原全部八个参数与七个物理控制、原 base profile 完整继承。仍为 `fixed=False`，因此原 $p_0$ 只改变原 base profile 的 $\delta$，不能再次吸收旧 $p_0$。七列在端点为 $B_2,\ldots,B_6,T,U$，完整积分 lift 的强度为 1，窗口保持 $(.5,.9)$。这是新的物理同伦端点求解，不是固定完整问题的角模精化。

初值使用上一份完整物理 quintic 在原 raw mesh 对应物理位置的值，加入两份实际 reference 的有限投影差及原共享 C² 入口修补；没有把 raw.y 与 quintic 点值混称逐位同一对象，也没有复制旧 mean-height 轨迹。必要的数组仅构造一次，保存全部参数、状态和 H 哈希，没有另做初始 RMS 探针。初始完整 H 与上一真实物理 seam H 逐位相同，因而复用其真接受 `6074075c…`；不同 H 仍必须由实际新 provider 执行完整原 DN。

原完整 core 数值充分 guard 在这个初值给出下界约 $0.51025439$、样本最小值约 $0.51178359$。这只说明初值通过原数值域门，不能据此声明连续几何证书或后续 Newton 试步可行。

独立入口 [run_m3_trace_path_native_endpoint_v2.py](../scripts/resume_m3/run_m3_trace_path_native_endpoint_v2.py) 的 SHA 为 `018df4f4bdf6885647fe6bda748817ea6cd03eb6b6b6cd622573ae6aa4bcb852`。它保留已登记 endpoint 入口的表示转换、原八次 outer 预算、Newton/五点域检查、全部 raw 快照、真实 mean/metric/seam 和即时 audit 保存，只显式继承新 native provider 的来源、真实缓存与 worker。prefix 原源码/source-root 不随 worker 迁移。

原 [metric observer v2](../scripts/resume_m3/metric_audit_observer_v2.py)，SHA `47993e3856ebc7727b2a8e3bebfd0e9ee50f76a7261fbd3f687247c295bc8520`，在本来必需的首次 prefix audit 前安装。它只从既有 FFT/数组记录 E/F/G 最坏采样位置和主导频率，不再执行第二个 FFT、不新增模型计算或接受门。若求解未到 audit，这些读数就尚未产生。

实际 session **38274**，启动块 `31bbd3`；工作目录为 `m3_work/trace-path-lam100-native-coupled-v1`。207 个来源、原始/运行计划、完整数组和初始 H 绑定见 [紧凑入口记录](../scripts/resume_m3/trace_path_lam100_native_coupled_entry.json)。此入口不继承 R46 的高幅持握比例，也不把 literal 圆弧定义当成完整数值曲面已经过门；真实内层、尾和全部后处理终态将独立登记。
