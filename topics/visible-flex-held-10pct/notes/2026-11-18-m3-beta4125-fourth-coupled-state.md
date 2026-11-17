# m3 β₀=4.125：完整真联合达到 q=0.040

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
可信度：数值证据，有限 M/深度/网格的完整联立接受。
计算于 2026-11-17 20:15 UTC 返回；日期前缀沿用本批记录。

## 结果

保持 β₀=4.125 及全部其余物理尾控制参数，采用同设计下已接受
q=0.025 与 q=0.030 的 material secant，尾从 q=0.030 final
checkpoint 初始化。原 canonical sparse source 的完整 prefix /
actual nonlinear tail 求解成功。δ 仍由新目标重新求解；本笔是
设计幅值增加，不是固定 g 收敛链。

M8、spacing3、depth8、shootingParts8、RK16、N128 不变，
没有启用可选局部 root 加严、L2 line search 或周期求积。
四个 actual-tail 调用全部接受，最后一次包含全 audit；原
shooting 2e-9 门与前缀边界门没有更改。

| 量 | q=0.040 完整终态 |
|---|---:|
| δ | 0.061051605540746214 |
| prefix 节点 | 936 |
| prefix sampled metric l1 | 6.90913189034608e-9 |
| prefix sampled Darboux l1 | 2.278633515018755e-4 |
| prefix sampled κ | 8.719247368454484 |
| cut 物理 BC max | 7.641885459816103e-11 |
| final actual tail residual | 8.024129215044245e-10 |
| flow min A | 0.6175486572505612 |
| tail audit actualMetric | 1.3337415616376848e-9 |
| tail audit fullD | 1.009764700629636e-5 |
| tail audit formalCurvature | 8.19058656765227 |
| mean 一阶 seam mismatch | −1.8228890619198523e-12 |
| mean 二阶 seam mismatch | 4.8375747851991946e-11 |
| nonmean 二阶 seam mismatch | 1.4846227442780679e-8 |

沿本 β 的 q=0.020、0.025、0.030、0.040 已有四个完整有限
联合态。最后一步 min A 仍明显为正，但 tail fullD 从 q=0.030
的约 7.20e-7 上升到约 1.01e-5。小的 metric defect 不能代替
高阶/闭合收敛；本笔没有宣称达到课题完成标准，也没有把原
cosine/support 核替成尚未联立求解的局域圆化核。

## 复现及实际下一运行

入口为 `scripts/resume_m3/continue_true_coupled.py`：
`--low-prefix beta4125-q025-resume/seed.json.gz`，
`--high-prefix beta4125-q030/seed.json.gz`，
`--high-tail beta4125-q030/seed_tail_0004.json.gz`，
`--linear-port beta4125-q025-resume/port.json`，`--amplitude .04`。
完整绝对路径、物理参数、源 hash 和所有调用标量保留在
`scripts/resume_m3/beta4125_q040_coupled_record.json`。

prefix SHA-256：
`e39386aab4b9fa816914afd26c2d80777ed9fa94d6a615d82036b9b76f72c33a`。
final tail SHA-256：
`10a6fa7463e7733a25f0da155b0409473c604a2a5bc4c56e569fcde1fc0ea077`。
真实场与 checkpoint 留在 `m3_work/beta4125-q040`，不入仓库。

已开始 β₀=4.625、同 q=0.040 的新物理设计联立。已登记的一阶
screen 提示首谷正性余量有望改善，现用 `continue_valley_design.py`
与明确的 old-nonlinear + new-linear − old-linear 初值入口，再次
完整求解 prefix/actual tail。其余控制参数不变；全局重标定仍会
改变整个 r(x) 分配，不能说后部物理函数不变。这个新目标在返回
前不算成功，线性 screen 也不构成非线性容量结论。
