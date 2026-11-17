# m3 首谷 β₀=4.625：q=0.040 真联立接受

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
可信度：数值证据；2026-11-17 20:23 UTC 完整有限联立终态。

从 β₀=4.125/q=0.040 完整状态出发，只把首谷控制 β₀ 提高到
4.625，其余控制参数不变。全局重标定重新计算整个 r(x)，因此
这不是同一物理度量或保持后部物理函数不变的操作。初始化明确
使用 old nonlinear + new linear − old linear，随后重新求解
prefix 的 δ/全部校正和 actual tail。没有把线性修正计为解。

M8、spacing3、depth8、parts8、RK16、N128 与全部原门保留。
四次 actual tail 调用均接受；最后一次含完整 audit。第三调用
曾到 5.5072e-9、4.8188e-9，继续原 Newton 后在 iteration5
降到 1.3768e-9，并非提前宣布这些中间值是终端失败或精度极限。

| 量 | 完整结果 |
|---|---:|
| δ | 0.061051601505166045 |
| 节点 | 936 |
| prefix metric l1 | 6.90988913332426e-9 |
| prefix Darboux l1 | 2.341483956047609e-4 |
| prefix sampled κ | 8.719248179262602 |
| 物理 BC max | 9.050473003574717e-10 |
| final actual tail residual | 1.376797359405243e-9 |
| flow min A | 0.7423215122220379 |
| audit actualMetric | 5.987454976264015e-10 |
| audit fullD | 4.118297095834561e-6 |
| audit formalCurvature | 8.238446813262973 |
| mean 一阶 seam mismatch | 1.3739009929736312e-13 |
| mean 二阶 seam mismatch | −1.1070988570338613e-10 |
| nonmean 二阶 seam mismatch | 2.1711344528642373e-8 |

相对 β₀=4.125 的独立 q=0.040 联立，min A 从约 .61755
提高到 .74232，tail fullD 从约 1.0098e-5 降到约 4.1183e-6。
两次的完整 H 和 δ 都重新求解，不能将比较解释为固定 H 的容量
认证。全域闭合/同 g 加密/精确圆弧/持握仍未由本笔支付。

复现入口 `continue_valley_design.py` 使用已提交的显式 design
与 linear-difference initializer 源，`--beta0 4.625 --amplitude .04`，
输入 β4.125/q040 prefix、final tail 以及 β4.125 的实际 port。
完整命令、参数、源 hash 与标量见
`scripts/resume_m3/beta4625_q040_coupled_record.json`。

prefix SHA-256：
`c55a2ebfcce39fe72810703e8fb239f60ce291b48cf7650a27d6b5ef52180bc9`。
final tail SHA-256：
`96c7b441e8a220acea983d2ddf726854e98828726d71279e764acc51bd5d23b5`。
实际场在 `m3_work/beta4625-q040-linear-difference`，不入仓库。

已立即从本态启动同 β₀ 的 q=0.060 真联立；同一时间准备将
已定义的大半径圆弧通过精确 core lift 及全部 c6 等补弧自由度
接入原实际 TailMixin。新的 R3 三重窗口以 q=.085/a=.21 为目标，
不会用当前 cos3 核冒充精确圆弧。
