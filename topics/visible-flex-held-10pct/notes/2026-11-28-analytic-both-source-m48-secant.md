# 两个真实接受源分别完整升至 M48 后的全状态割线初猜

为下一次原 δ/support 设计求解提供 λ = .128、M48、angular 1536 的明确未接受初猜。两个输入是本会话实际通过全部原门槛的 λ = .032/M32 与 λ = .064/M40，而不是两次没有完整返回的 −9 进程状态。这里只准备原未知量；不造新的 accepted run，不宣称固定 g 收敛、完整尾闭合或连续曲面族。

独立实现 [`both_source_lifted_secant.py`](../scripts/resume_20261128/analytic/both_source_lifted_secant.py)，SHA `dd5b0d88eb6609fb57324486dcc231b65ad386afcd48f36bcb31ef7e27b90eb4`。实际 session 73805 正常退出 0。为避免原 geometry loader 全局类安装互相覆盖，左右源在两个顺序执行的独立子进程中重建；分别保留各自 λ、加性 δ、物理核心、原 literal chart、实际 support 控制及原 mean 规则。

对每个源 i，将参数按其原物理尺度输送到相同 M48 空间，并在共同计算坐标 t 上直接评价原保存 cubic。随后使用已有完整升模公式

\[
Y_i^{48}(t)=\operatorname{embed}_{M_i}^{48}Y_i(t)
 +a_i(s_i(t))\chi_i(s_i(t))
   \bigl(I_i^{48}-\operatorname{embed}_{M_i}^{48}I_i^{M_i}\bigr).
\]

完整 exact-lift 系数为 1；λ 不被误用成该系数。两份源各自的 inlet projection 差都实际非零，分别为 1.6317198308255797e−8 与 3.949994903976483e−9，因此不能只零填充状态。两次参数输送后所有共有原 support 系数均逐位不变，新加系数恰为 0。

共同网格优先保留右源全部 952 个节点；左源的 947 个节点均与已保留点相距不超过 2e−12，因而不再重复插入。最终仍为 952 点，没有均匀重采样。两个完整升模值都直接在该网格评价，不为升模源另拟合 cubic，不输出伪造的物理 interpolant。

最后对全部 145 个状态和全部 48 个原参数使用

\[
\beta=\frac{.128-.064}{.064-.032}=2,\qquad
Y_{\rm init}=Y_R^{48}+\beta(Y_R^{48}-Y_L^{48}),\qquad
p_{\rm init}=p_R^{48}+\beta(p_R^{48}-p_L^{48}).
\]

预测物理 δ 为 .06412892684644424。这里的割线是在原计算 t 和 support 参数坐标中形成的初猜；两个源的物理径向图及 mean 规则本来可以不同，不因此声称两个曲面相同。

## 实际输入和参考检查

| 输入 | λ / M | 真源 run SHA |
|---|---|---|
| 左 | .032 / 32 | `652c3a343c3f64950db5f9486d1c98f387e92fc8fa2efd02e08f97dcbdeee2b4` |
| 右 | .064 / 40 | `05e9ad770c7f55f3738fad0f7ed5e3525cb98e1edbb40363a3a6f78b4f4d3711` |

原导出 port48 SHA 为 `5a6e62c8fdff09ff7199c5b5cb65001ac40893694bf731be8d6943026f8e72bd`，逐项确认它仅增大线性端口分辨率，未改物理 profile、tail parameters 或 cut。

沿用既有升模入口的参考两阶 jet 检查：各 102 个 s 点、4640 个角点，原阈值 1e−7。左源六种参考 jet 差的最大值为 9.108769501816945e−15，右源为 3.849929460653035e−14；两份 rho 差都是 0。这些参考检查保留原完整 core-lift，报告的 raw reference jets 按既有合同不包含共同 mean-height 项；它们不是完整 Cartesian 误差界、连续区间证书或新 BVP 验收。

原源 mean 分别为 1552 和 1936；本次没有重算或替换它们。真正 λ = .128/M48 的目标解必须按原 M48 规则重新构造完整 mean 2320 并支付原 metric audit。

左右子进程分别用时 35.3386161010003 和 37.669767173001674 秒，峰 RSS 分别为 771520 和 779576 KiB；顺序执行结束即释放。总计 75.26872005500081 秒，没有组装 J 或执行 BVP。

## 输出与后继门槛

实际输出目录 `held10-design-work/lambda128-m48-both-source-secant-20261128`；`initial.npz` SHA 为 `36ffb0fa969f3be5442a70e372fcfd2cd3555a51fa6fd321ee0585fa7bdc35e5`。完整 source/hash、每源 lift 记录及初猜数据绑定保存在[实际记录](2026-11-28-analytic-both-source-m48-secant-observed.json)，SHA `0a74c7a857350363db4116b3eb19826637a2a11400593c6f22eb35db99531133`。

状态为 `unaccepted_two_source_lifted_secant_initializer_ready`。后继须使用目标 λ、M48 全未知量及原物理参数执行原 initial-domain、完整 BVP/RMS、physical BC 与 full metric audit；本初猜不会替代这些门槛。原固定 g M32 的独立恢复仍以自己的全节点检查点为输入，两条任务的物理问题不相互替换。
