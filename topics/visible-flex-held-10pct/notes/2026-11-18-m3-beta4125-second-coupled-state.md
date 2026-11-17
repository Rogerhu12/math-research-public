# m3 首谷 β₀=4.125：q=0.025 的第二个真正联立态

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
计算终态为 2026-11-17 20:06 UTC。目录日期沿用本会话前面笔记。

## 结论与适用范围

在 β₀=4.125 的同一物理尾设计下，现有 q=0.020 之外的
q=0.025 真正 prefix/actual-tail 联立态已完整返回。这里的“同一”
指尾的物理控制参数不变；prefix 的 δ 和所有允许的校正系数仍然
重新求解。这不是旧线性 DN 前缀的替名，也不是固定 g 的幅值族
认证。有限阶、有限深度、有限采样的接受与闭曲面最终完成标准
仍是两件事。

所有原门槛保留：M8、spacing=3、depth=8、shootingParts=8、
RK steps=16、完整角向 N=128，最后 shooting 必须小于 2e-9。
本次最终残差 1.9768747165665916e-9 靠近门槛，按原值记录，
不以中断运行中更小的尾残差替换。

| 量 | 完整终态 |
|---|---:|
| q | 0.025 |
| δ | 0.06105528088752851 |
| prefix 径向节点 | 1367 |
| 最大 RMS collocation residual | 9.938240727336711e-7 |
| prefix sampled metric l1 | 1.1439575261744346e-8 |
| prefix sampled Cartesian Darboux l1 | 4.758490909330009e-4 |
| prefix sampled κ | 8.215612924101766 |
| cut 物理 BC max | 6.271741953418251e-10 |
| final actual tail residual | 1.9768747165665916e-9 |
| flow min A | 0.7539365572518805 |
| tail audit min A | 0.7539454284479784 |
| tail audit actualMetric | 1.900057888826127e-11 |
| tail audit fullD | 1.364840904585902e-7 |
| tail audit formalCurvature | 8.093175603593664 |
| mean 一阶 seam mismatch | 1.9821089214389076e-12 |
| mean 二阶 seam mismatch | −2.9886160213266066e-10 |
| nonmean 二阶 seam mismatch | 1.3658547182998134e-8 |

本次 sampled prefix Darboux defect 比 q=0.020 的 5.6473e-5
大，不能由 tail audit 的小数值推断整个拼接像的 C² 误差也小。
本笔只建立第二个实际有限联立状态；径向/角向/尾深度收敛和完整
Cartesian 闭合须继续按各自原条件处理。

## 先前运行中断及本次重启

原 `m3_work/beta4125-q025` 在 19:48 UTC 之后执行句柄消失；
没有终端 summary，也没有保存的 prefix 场或最终 audit 第四响应。
第三个 actual-tail 响应本身确实接受，残差约 6.6374e-10，
但它不能单独把未保存的联合态补成完整成功。原因未知，不作
OOM、方程失效或分支不存在的推断。

`m3_work/beta4125-q025-resume` 从已接受 β₀=4.125/q=0.020
prefix 出发，只把上述第三响应作为新的 tail 初值。新目标仍为
q=0.025；完整 prefix 及 actual tail 再次求解，产生本笔的终态。
其初始化使用明确的 `designInitialCheckpoint` 入口，物理控制
参数比较与原接受门均保留。四个实际 tail 调用都接受；最后一次
重新做完整 audit。

机器记录 `scripts/resume_m3/beta4125_q025_coupled_record.json`
包含完整命令、物理参数、四次响应标量、源 hash 和工程中断证据。
复现入口是 `continue_valley_design.py`：source-topic 指向安装了
显式 design initializer 的独立 source 副本，`--prefix-restart`
指向 β₀=4.125/q=0.020，`--tail-restart` 指向原中断的第三响应，
`--restart-port` 指向上述 q=0.020 的实际 port，`--beta0 4.125
--amplitude .025`；其余路径及参数由记录完整给出。

最终 prefix SHA-256：
`6c08d6ec2c37c52d45bdfec83b96886478eed83e2be84eeb08ff1808d328b92a`。
最终 tail `seed_tail_0004.json.gz` SHA-256：
`5924267f0d90e0a35bbdbab350da4cf173e73590e378cf39324f9357857e9df8`。
真实场与 checkpoint 只在 scratch，未提交进仓库。

下一实际运行已用同 β₀ 下 q=0.020、q=0.025 两个完整 prefix
作 secant，并用本次 final tail 作初值，目标 q=0.030。它不改变
尾物理控制参数，也不把尚未返回的增幅计为成功。
