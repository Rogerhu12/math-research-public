# 新 g 的 λ=.004/M24 实际返回与表示外频率

维护会话：Astra-held10-1b6d88ec-20261120。

本条继续已通过原有限门的 λ=.002/M24 设计。新的 λ=.004 原线性 DN 前缀实际收敛，但完整原 metric_l1=1.5330328152330117e−6，未通过 1e−6 门。原 λ=.002 的真实非线性尾和连续几何计算独立继续；本次没有替换其物理场。

## 1. 明确的设计变化和真实返回

只把核心设置中的 homotopy 从 .002 改成 .004，使用已过 λ=.002 的原 631 节点 raw 作新初猜，输出到独立目录。原 base profile 继续使用 multistage-linear-root-profile.json；没有把已吸收 p0 的 frozen_profile 再配旧 p0，以免重复加入 delta 位移。q=.06、warp=.06、τ=1、S=.5、b=.2、k=.2、M24、angular768、同一线性端口及全部原求解门保持。

这个变更是核心圆化的设计延拓。delta 和23个物理 c 随原 BVP 重解，不能叫固定全部参数的精化；旧 R60/R61 和前缀连续证书也不移给新场。

实际进程28660 exit0，258.119456秒，两个自适应网格，8个完整 Newton 接受步、0拒绝、最小alpha=1。

| 原指标 | 实际值 |
|---|---:|
| 节点数 | 635 |
| collocation RMS max | 9.954091430839747e−7 |
| 原24条linear DN physical BC max | 4.478384101851541e−15 |
| 原完整metric_l1 | **1.5330328152330117e−6，未门** |
| 全未投影flow defect | 2.2548194018793844e−5 |
| Darboux l1 | .009327845195324692 |
| delta | .06413456231556622 |
| 原实际审计角数／径向数 | 1168／1418 |

求解器的success和进程exit0只说明其各自成功，均不覆盖metric门。这里记录的是原有限FFT l1验收失败，尚未把该数误当连续全角算子范数下界或严格几何反例。

## 2. 一次原均值下的补空间诊断

对同一保存的完整physical quintic，固定原mean1168，只用1168角评价网格，运行既有audit_full_frenet_residual。该次session52296实际exit0，没有重新求BVP、改核心或改验收。原投影内径向缺陷最大1.584914604748215e−7，而补空间残差最大2.2548194018793844e−5，与全未投影残差峰相同。竖向零模最大2.922890240344483e−16；固定均值与本次评价均值差为0，没有用均值自由度吸收遗漏模式。

| 计算角ψ的Cartesian频壳 | 残差向量系数有限l1最大值 |
|---|---:|
| 0 | 6.927796555990688e−14 |
| 1—3 | 9.020963403486284e−8 |
| 4—73 | 2.900157032595649e−7 |
| 74—146 | **5.2196562624013655e−5** |
| 147—292 | 1.3054936165673075e−6 |
| 293—584 | 3.9219753735033546e−8 |

主要系数在ψ=±77、±79、±78、±75和±83，超出M24的Cartesian频率73。该证据支持下一步增加到M32；它是有限谱诊断，没有证明M32一定过门，也不能把ψ谱当材料θ谱或连续余项证书。

## 3. M32入口及复现

原共享分配的线性端口导出已实际exit0（97477）。新settings仅把modes24改成32；N512仍满足原严格N>4*M*3，depth8、steps16、linearSteps512、shootingParts16及全部物理参数不变，原Node heap2048保留。没有重新启动旧未共享OOM路径，也没有运行新的非线性尾。

升M使用既有完整参考补偿Ynew=embed(Yold)+a*chi*(Inew−embed(Iold))，系数1；新增8个控制只是初猜0，后续设计BVP仍按原模型求解。当前transfer入口58863已实际启动，最终返回与M32新求解另记；本条不预记通过。

[精简执行记录](2026-11-20-m3-newg-lambda0004-m24-execution.json)保存全部物理参数、原输入和来源哈希、两条实际argv及环境、原门和频壳小结果。核心设置另存scripts/resume_m3/multistage_wide_circle_lambda0p004.json，与这次scratch输入逐字相同。实际原完整命令如下。

~~~bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python /workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct/scripts/resume_m3/portable_prefix_continue.py --source-topic /workspace/scratch/1b6d88ecddf3/m3-work/multistage-source-v2 --short-bridge /workspace/scratch/1b6d88ecddf3/m3-work/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py --profile /workspace/scratch/1b6d88ecddf3/m3-work/multistage-linear-root-profile.json --chart /workspace/scratch/1b6d88ecddf3/m3-work/bootstrap/reference/chart.json --port /workspace/scratch/1b6d88ecddf3/m3-work/newg-wide-m24-port/linear-port.json --raw-restart /workspace/scratch/1b6d88ecddf3/m3-work/newg-wide-lambda0p002-m24-linear/inner-00.npz --core-module /workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct/scripts/resume_m3/material_support_factory.py --core-config /workspace/scratch/1b6d88ecddf3/m3-work/newg-wide-lambda0p004-m24-config.json --amplitude .06 --warp-reference .06 --modes 24 --angular 768 --audit-angular 512 --nodes 401 --max-nodes 6000 --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 --outdir /workspace/scratch/1b6d88ecddf3/m3-work/newg-wide-lambda0p004-m24-linear
~~~

残差诊断命令：

~~~bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python -u /workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct/scripts/resume_n4/audit_full_frenet_residual.py --model-adapter /workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct/scripts/resume_m3/actual_m3_metric_model.py --model-config /workspace/scratch/1b6d88ecddf3/m3-work/newg-wide-lambda0p004-m24-linear/run.json --physical /workspace/scratch/1b6d88ecddf3/m3-work/newg-wide-lambda0p004-m24-linear/physical.npz --metric-loader /workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct/scripts/resume_m3/audit_full_relative_metric.py --mean-nodes 1168 --angular 1168 --physical-cutoff 144 --batch 8 --out /workspace/scratch/1b6d88ecddf3/m3-work/newg-wide-lambda0p004-m24-full-residual.json
~~~

两命令均在清除LD_PRELOAD/LD_LIBRARY_PATH、OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1的环境执行。详细环境和后续端口导出argv见执行记录。

## 4. 保存边界

raw、physical quintic、完整运行输出与端口矩阵均只留运行目录。记录保留参数、方法、源码、命令和哈希，不提交可再生场或矩阵。当前仍无λ=1准确圆弧的完整前缀—真尾，更无满足全部10%要求的闭族；继续按实际新返回推进。
