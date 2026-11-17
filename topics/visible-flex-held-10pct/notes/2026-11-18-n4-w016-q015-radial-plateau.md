# wCut=.16、q=.015 的同 g 径向误差平台

维护：n4_round_core；2026-11-18（UTC+8）。可信度：实际有限 BVP 与完整保存图的采样数值证据。这里没有连续区间证书、精确等距族或不存在性结论。

## 固定的是哪一个 g

起点是新 wCut=.16 的 q=.015/M20 设计接受态，使用原真实24模线性端口。冻结其**全部** physical_profile 与物理 port，尤其 delta=.03016176956022264、vd=.25023170207554724、vu=.35、ramp=.45、ramp_eta=.05、cycles=1、ShortBridge K4/peak=.2；后续不再求解 delta/vd。

固定 g 的未知量改为 log(q/q_gauge)、c8 和其余核心控制。此处 M20、角向配置1280均保持，主要收紧径向 collocation 容差。lambda=0、eta=.1，尚未圆化，末端也仍是线性端口。不能与 wCut=.08 的旧 g 或主会话实际 nonlinear-tail g 混为同一精化链。

最终 build_seed 从原 solved parameters 定义整个核心，并从原核心重建 reference lift。该次 M20→M20 初猜的 F、Ft、Ftt 检查误差均为0，完整映射投影误差2.22045e-16；原867个物理节点全部保留，加入接口点后为870个，最大覆盖距离1.11022e-16。初猜 q=.015，入口修正仅1.91091e-15。

## 两笔已完成运行

| 项目 | 原 q=.015/M20 设计 | 同 g M20 径向精化 |
|---|---:|---:|
| collocation tol | 3e-7 | 1e-8 |
| 最终节点 | 867 | **2484** |
| 迭代轮数 | 4 | 3 |
| 最大 RMS | 2.99871488794e-7 | **9.99728602080e-9** |
| scaled BC | 1.80675445751e-15 | 7.52368036849e-15 |
| q坐标 | .015 | .014999995400232412 |
| metric FFT l1 | **1.20585716484e-5** | **1.20598361532e-5** |
| Cartesian Darboux tensor l1 | **.02321427308** | **.02320923352** |
| flow defect | .00012541054104 | .00012543752558 |
| 采样最大主曲率 | 6.96699834367 | 6.96699783867 |
| Frenet root margin最小值 | .00162295744 | .00162330933 |
| 审计径向样本数 | 1882 | 5116 |
| 审计角向样本数 | 1296 | 1296 |

设计运行有11次域拒绝、8次merit拒绝，28个接受步，最小alpha=1/128；记录求解段946.12秒。固定 g 精化的3个Newton接受步均alpha=1，没有域或merit拒绝，记录求解段426.89秒。观察钩子只计时和记录原STATS，不改原Newton运算、判据或返回值。

## 本次结果能排除什么

RMS约下降30倍、径向节点增加约2.86倍，核心实际 q 仅变动4.60e-9，但 metric l1 的精化/原值比为 **1.000104864**，Darboux tensor 比为 **.999782911**，均基本处于同一水平。因此**本次径向精化没有消除主要的完整图缺陷**，仍未通过所用 metric l1 的1e-6门。不能把 collocation 接受误写为完整几何通过，也不能据此断言任何 g 下都不可能完成。

角谱与其他尚未支付的误差分量需要实际后续验证；本条没有提前认定它们是唯一原因。主会话正准备同一个 g 下的 M24 精化，结果另记，不预先计为改善。圆化继续以此前 metric 门通过的新 cut q=.0125态为起点；q=.015只作明确未通过完整门的备用初值。

## 复现与来源

收集脚本为 `scripts/resume_transfer/record_fixed_prefix.py`，执行参数：`--work /workspace/scratch/7322d0dee069/transfer_work/n4-thicker-cut --out topics/visible-flex-held-10pct/scripts/resume_transfer/w016_q015_fixed_m20.json`。它核对两态整段物理 profile、port、M和角向配置相同，核对输入/输出 checkpoint及全部系数块 SHA，核对实际固定 driver与observer源码；只保存参数、标量和hash。没有重新求解已有终态。

完整运行命令和确切源码hash在 `scripts/resume_transfer/w016_q015_fixed_m20.json`。使用的 fixed driver SHA 为 f8431622a3973a0bb525a97c3155eb3cb7bbfe459193446eef91f5a69f943b39，observer SHA 为75647718cfcb83b70be3446d236693dbf66426ea3861c92d7ffc0a527ac952ee，外层 `run_observed_fixed.py` SHA 为d828228375fcf0f0b0955702735eea0f417d969ced5d1c1b9a1c59f35e8623f1。原 q015结果 SHA a59f4db5b51d64a04a6fc8d6e74a04841a8645182dc49ccf2395ba0d09ad6e65，固定 g 结果 SHA77d6442c4333c425314e2f570b8a0f9ed5091d6b10de88bd9ef43422b7640524。
