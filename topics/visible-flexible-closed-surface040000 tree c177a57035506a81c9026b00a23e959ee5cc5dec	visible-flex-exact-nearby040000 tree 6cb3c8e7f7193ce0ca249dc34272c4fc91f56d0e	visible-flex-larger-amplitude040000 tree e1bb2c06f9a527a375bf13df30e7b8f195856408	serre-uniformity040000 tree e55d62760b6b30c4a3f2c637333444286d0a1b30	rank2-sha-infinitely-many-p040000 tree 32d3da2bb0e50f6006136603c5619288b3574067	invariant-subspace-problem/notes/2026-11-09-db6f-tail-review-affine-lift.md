# 自由 cut affine-prefix 初猜的独立审查

审查者：/root/tail_theory，2026-11-09；未参与新预测器或其公式的构造。本文仅审查辅助 warm 问题，不把它视为真实 DN 或完整联解。

**结论：PASS，可用于所记录同一 g 的 M14 到 M15 辅助初猜。** 冻结源码 scripts/db6f-prefix-affine-lift.py，SHA256
7d0267b0097e7da5e7fe1696715283f4806ddef4494269a084295eadf9171a2a。
方法稿 notes/2026-11-09-db6f-prefix-affine-lift-method.md，SHA256
4880cd103868a32b0b92f82de79196488f78f94abda376ebb402b405cb55dd6f。
实际输入和矩阵检查在 notes/2026-11-09-db6f-tail-review-affine-lift.json，SHA256
75845ec267df38b607e71670f49cfcc2e75e43ab41110880a2c1f5e6f64f0a55。

## 1. 实际锚点与物理单位

输入为完整 M14/N512 的 prefix CP
db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14.json.gz
及其 tail_0002。已直接读取并核对 prefix solver_success、actual_nonlinear_tail 和该 tail response 的 converged 均为真；tail 的 N=512、projectionFloor=.05。该读入不是将旧 M14/N256 首响应冒作 N512。

冻结线性 port 为 db6f 对应的 weighted-k6-port96-cusp1024，输入 SHA 与 prefix 保存的 physical_port_sha256 一致。保存的 physical_tail_parameters 与 cut 数据也逐值相同。

尾源的 heightJetJacobian 构造顺序明确先列 slope 各分量，再列 second、mean corrections 和 height。对第 k 列，源代码扰动的是 $Q_k$，最终除以 $2h r_c^4$；因为物理高度 $H_k=r_c^4Q_k$，矩阵前 M 行的单位已经是

$$
\frac{\partial S_j}{\partial H_k}.
$$

该矩阵是锚点保存的数值 Jacobian，本审查未将它声称为严格区间导数；对于定义一个 affine 初猜，采用这个固定矩阵是明确的辅助选择。

linearSlope 的生成是同一个微小线性端口扰动所得 jets.slope[j]/jets.height[j]，所以新增第15模的 d15 也是物理斜率/物理高度之比。其物理频率是 45；本次值为 194.8136275707011。不应再乘 45、$r_c^4$、$w$ 或 momentum 的归一因子。新实现没有多乘这些因子。

## 2. 新增块只是 surrogate 的定义

脚本把 $H_0=(H_{14},0)$、$S_0=(S_{14},0)$，并定义

$$
\widehat J=\operatorname{diag}(J_{14},d_{15}),\qquad
\widehat S(H)=S_0+\widehat J(H-H_0).
$$

独立实际矩阵检查确认：

- 原14乘14斜率块与保存 Jacobian 前14行逐项完全相同；
- 两个交叉块恰为零，新增对角项恰为 linearSlope[14]；
- 在 $H=H_0$ 输出恰为 $S_0$；
- 仅改变新增坐标时，原14模输出不变、新模输出恰为 $d_{15}H_{15}$；
- audit=True 请求被显式拒绝。

交叉块置零和新增锚点斜率取零都只是辅助初猜的定义。它们**没有**断言真正 M15 非线性 DN 的交叉导数或 $S_{15}(H_{14},0)$ 为零。此选择不保证新初猜更接近真实 joint 解；效果必须由后续实际计算判断。

3M+2 行返回格式中的其他行是未用占位。原 TailMixin 的 terminal 和 bc_jac 只读取 slope 与矩阵前 M 行；真实 seam_audit 会要求 audit=True，已被 surrogate 拒绝。因此占位没有被误当作完整 mean/second jets。

## 3. 边界链式法则

原 TailMixin 保持

$$
H=\sigma qY_z,\qquad
{\cal B}=q\,\partial_sY_z-\frac{\widehat S(H)}{\sqrt{E_{\rm cut}}}.
$$

其 Jacobian 的高度列修正为

$$
-\frac{\sigma q}{\sqrt{E_{\rm cut}}}\widehat J.
$$

这是对上述复合函数的直接链式法则。整体 boundary scaling 最后统一除以 bcweights；没有重复缩放新增模。源码直接复用现有 TailMixin，未另写一套可能遗漏 $\sigma$ 或 $q$ 的边界规则。

## 4. 同一 g、容差和输出范围

实例以 fixed=True 构造，并通过原保存网格 restart 检查 chart、frozen profile、physical tail 参数、cut 与 warp_reference_q。旧模系数按原有符号索引 padding，新自由高模只是未知嵌入的初猜；物理度量、有限校准表、无限尾定义和相位区间没有被改写。

实际原配置的 tol=2e-9、bc_tol=1e-8、physical_bc_tol=2e-11 均直接保留；计划 angular=512、max_nodes=4500 是辅助求解的数值设置。projectionFloor=.05 在 manifest 中记录，这个辅助 BVP 本身没有执行尾 root 或降低其门槛。

输出 CP 明确 actual_nonlinear_tail=False、frozen_affine_dn=True、status=UNSOLVED。solver_success 仅指辅助 affine BVP。后续 prefix audit 是原有限采样几何诊断，不调用真实 tail seam；报告又覆盖其 scope 为初猜的 prefix。即使辅助 solver 成功或 prefix metric 改善，仍须以预测切口返回原 M15 真实 DN、原方程边界和最终 seam 审计。

本审查未启动 BVP 或改动活 worker；只做全文/依赖审查和约一秒的实际输入矩阵核验。没有发现阻止该辅助 warm 方案运行的符号、单位或范围错误。
