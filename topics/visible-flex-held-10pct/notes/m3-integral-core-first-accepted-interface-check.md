# 第一个 solver-accepted 积分 core 的生产读取验证

维护：Astra-held10-7322d0de-20261118 / closed_geometry。

使用 `beta4625-q040-lam00002-parts16-v2/seed.json.gz`，执行已经登记的
`resume_closed/audit_integral_prefix.py`。这是 `lambda=.0002` 的 canonical
圆化状态；它通过原有限 nonlinear solver 接受门，但完整 metric 远未达到
课题要求。`lambda` 也不是 `1`，所以不能领取 R32 的精确圆弧结论。

本次用生产入口读取真实 checkpoint，保留 `accepted_anchor`、
`core_round_sources`、完整物理输入与七个实际控制的核对，并通过原
`curve_stable_prefix_bvp.load_checkpoint` 解码 coefficient chunks。
没有修改 checkpoint，没有运行 BVP 或尾 shooting，没有接入尾部或铺新的闭图盒。

实际运行 `N=256`，径向审计点共 2070 个，结束码 `0`。
源 `Flow.geo` 已加 reference 项与导出器独立展开的同一项之间，七种 jet 的
最大差不超过 `4.952613e-15`；中心 `X=Gamma,Fs=e_z,Fss=0` 的数值恒等式
误差不超过 `1.777224e-15`。这说明新生产读取路径和单次 `H` 导出接口已在
真实分块 checkpoint 上贯通，补上先前非解探针没有覆盖的输入路径。

完整新有限前缀的 metric 采样指标为

`3.969242378188142e-4`。

它诚实复现 source 中约 `3.97e-4` 的全角缺口，明显超过 `1e-6`。
没有把两个不同采样口径下的末位差异称作改善或收敛，也没有取得连续界。

为区分真实解缺口与表示误差，本次另记录：

| 数值诊断 | 最大位置差 | 最大径向一阶差 | 最大径向二阶差 |
|---|---:|---:|---:|
| raw finite 相对原 source | `9.809152e-16` | `1.061313e-10` | `2.679812e-8` |
| 加中心补缝后的 finite 相对原 source | `3.026198e-8` | `2.968185e-6` | `1.094709e-3` |

中心实际二阶补缝 `Delta_ss` 的数值范数约 `.0010947091`，其角一阶/二阶导数
约 `.04879869/2.61900413`。因此这个状态中的主要中心二阶缺口不是 Cartesian
五次式导出误差；将 source 的积分中心位置精确保留，并不自动使投影方程的
全部二阶角函数精确闭合。

这条记录只确认生产输入、source reference 单次计数及中心接缝的实现。
它不声称完整闭曲面、真积分 `g` 的连续 metric、reach、固定 `g` 收敛或
10% 已通过。数组保留为可再生 scratch 数据，命令与输入/输出 hash 在
`scripts/resume_closed/accepted_integral_prefix_interface_execution.json`。
