# m3 β₀=4.125：真联合幅值推进至 q=0.030

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
终态为 2026-11-17 20:10 UTC；日期前缀沿用本批记录。

## 本次新结论

β₀=4.125 的实际物理尾设计保持不变，用同设计下已接受的
q=0.020、0.025 两个 prefix 作 material secant，只作为 q=0.030
初值；尾用 q=0.025 的最终 accepted 状态初始化。随后仍重新求解
δ、全部 prefix 校正和 actual nonlinear DN。完整运行成功，
不是线性 DN、预热尾或内层 affine DN 的单独接受。

这次直接使用原 canonical sparse source，未启用局部 root 加严、
L2 line search、周期求积或其他可选数学/数值替换。M8、spacing3、
depth8、parts8、RK16、N128 和原 2e-9 最终门不变。实际尾共四次
调用，最终一次含 audit；第零次 outer actual BC 已通过原门。

| 量 | q=0.030 完整结果 |
|---|---:|
| δ | 0.06105428508814396 |
| prefix 节点 | 937 |
| prefix sampled metric l1 | 4.6406782316036645e-9 |
| prefix sampled Darboux l1 | 1.279675115227909e-4 |
| prefix sampled κ | 8.382153016476817 |
| cut 物理 BC max | 4.7316962645385535e-12 |
| actual tail residual | 1.647094021936774e-9 |
| flow min A | 0.7092065323708037 |
| tail audit min A | 0.709210078414982 |
| tail audit actualMetric | 9.858291960542065e-11 |
| tail audit fullD | 7.197641560455487e-7 |
| tail audit formalCurvature | 8.124368325111876 |
| mean 一阶 seam mismatch | −4.723582636145807e-13 |
| mean 二阶 seam mismatch | 1.1292522472672317e-11 |
| nonmean 二阶 seam mismatch | 1.0992274458576873e-10 |

q=0.025 的同设计前一态 min A 为 0.7539366；本次仍有明显
正性余量。这只能说明所记录有限系统的已接受状态，没有推出
非线性容量上界、连续族的统一证书或更大 q 的必然存在。
tail audit fullD 从前态约 1.36e-7 上升到约 7.20e-7，后续提高
模态/径向精度仍不可省略。不同幅值重新选取 δ，不能把本组
设计延拓当作固定 g 的收敛链。

当前核心仍是原 cosine/support 核；本次没有安装新局域圆化
λ=1 核，亦未从其他 n 的圆心或中心对称论证领取 10% 持握结论。
完整闭合、同一 g 的严格族和持握的全像下界仍由课题原标准判定。

## 复现与追踪

入口为 `scripts/resume_m3/continue_true_coupled.py`，取
`--low-prefix beta4125-q020-linear-difference/seed.json.gz`，
`--high-prefix beta4125-q025-resume/seed.json.gz`，
`--high-tail beta4125-q025-resume/seed_tail_0004.json.gz`，
`--linear-port beta4125-q025-resume/port.json`，`--amplitude .03`。
完整绝对路径、source/port/chart hash 与控制参数在
`scripts/resume_m3/beta4125_q030_coupled_record.json`。

最终 prefix SHA-256：
`e78b1db8ea9f17f13d9f5dba102919e540e8c87ce2372a8371acf36184363c7e`。
最终 tail SHA-256：
`9ddbb236732b4754bb95b1bc09e1238ae74ff668888f67239fdf0090b0793c09`。
真实场仅留 `m3_work/beta4125-q030`；本仓库仅存源、参数、标量
结果和 hash。

已立即继续 q=0.040：以 q=0.025、0.030 两个同设计完整 prefix
作 secant，使用本次 final tail 初始化。新目标返回前不计为成功。
