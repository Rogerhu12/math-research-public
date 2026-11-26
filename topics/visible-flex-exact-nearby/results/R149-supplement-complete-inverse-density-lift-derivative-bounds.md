# R149 补充 IL：原单腿完整逆 lift 及其三阶导数的首次实际入口

**状态：已证明（解析输入接线与公式）。** 本文不宣称尚未运行的
Actions 数值。会话 `visible-exact-astra-fb31ed6-20261127`，2026-11-27。

## IL.1 同一完整对象

采用 [DC](R149-supplement-same-sign-density-compression-and-finite-Theta-rows.md)
的全部原定义，特别是物理周期 $\pi/2$、频率 $4n$、
$\psi=X_-\circ H^{-1}$ 和 $p=\psi^{-1}=H\circ X_-^{-1}$。
这里 $H$ 是 W 的同一 selected affine family 的真共轭，不以已知数值
点代替 selected parameter。两 physical density means 仍是独立输出槽。

原公开 run `43580721166/1` 的完整 `complete-169-cover.json.gz` 与
run `43586895661/1` 的完整 `wiener.json.gz` 有完全相同的两条
`exact_terminal_phase_state`。每条按 $-64,\ldots,64$ 存储有理复系数；
不丢弃 central mean，也不把两腿的差当作任一腿。令第二条为

$$
 A_-(x)=x+a_0+\sum_{n=1}^{64}
 \{a_ne^{4inx}+\overline {a_n}e^{-4inx}\}.
 \tag{IL.1}
$$

原 `phase_full_transport_Taylor.py` 的两个符号按 $(+1,-1)$ 排列，
从 $H_{\rm fin}$ 开始解
$\partial_r A_\pm+(-d\pm\eta q)\partial_x A_\pm=0$。
因此第二条是真正 $H_{\rm fin}\circ X_{-,0}^{-1}$ 的有限 transport
trial。这是 DC.20 已核定的方向；不是 forward flow，也未交换两腿。
令原 post48 的完整 48 对系数定义

$$
 K(x)=x+\sum_{n=1}^{48}(s_n\sin4nx+c_n\cos4nx),\qquad
 \widehat p=K\circ A_- .                                      \tag{IL.2}
$$

$K$ 的常数平移为原精确零；$A_-$ 的真实有理 mean 完整保留。
独立 terminal rotation 不并入 $K$ 或重新拟合。新的计算不运行原
transport、KAM、Wiener widening、postcomposition fit 或旧范数目标。

## IL.2 完整 analytic 误差

在物理 strip $|\operatorname {Im}x|<\sigma=1/256$ 上，DC.20 给出

$$
 \|p-\widehat p\|_\sigma\le E_p
 :=E_H+G_1Y\,d_*+E_{\rm post,tr}+E_{\rm post,root},\qquad d_*\ge|\delta_*|.       \tag{IL.3}
$$

五项逐一来自完整旧 W/R31/post48 对象：

| 记号 | 原完整字段 |
|---|---|
| $E_H$ | W `selected.physical_true_conjugacy_minus_G_norm` |
| $G_1$ | W `exact_G_derivative_norm` |
| $Y$ | R31 `complete_return_first_parameter` |
| $d_*\ge|\delta_*|$ | W `selected.parameter_change` 的完整非负上界 |
| $E_{\rm post,tr}$ | post48 `multiplied_complete_true_transport_residual` |
| $E_{\rm post,root}$ | post48 `multiplied_genuine_Wiener_root_sliver` |

这里 $Y$ 可用于单腿，是因为原 R31 源码以完整非负项
$e^{2L_\delta}2(D_{1,\delta}+C_{1,\delta})$ 构造它；并非从一个
有符号 return derivative 反推单腿。原 $L_\delta<1/16$ 使复杂
单腿像宽至多 $16\sigma/15=1/240<1/128$。两项 post48 费用是
两腿分别绝对值费用的非负总和，故各自覆盖所需第二腿，不作除二。
旧真 root 的最后一段已由 root fee 支付。所有项取旧完整球的外向上界。

## IL.3 同一 finite compound 的三个完整实轴导数界

对 $r=1,2,3$ 定义

$$
 A_r={\bf1}_{r=1}+2\sum_{n=1}^{64}(4n)^r|a_n|,
 \qquad
 K_r={\bf1}_{r=1}+\sum_{n=1}^{48}(4n)^r\sqrt{s_n^2+c_n^2}.
 \tag{IL.4}
$$

每个和都遍历全部系数；中心 mean 的各正阶导数精确为零。有限
Fourier 级数逐项微分、三角不等式分别给出
$\|A_-^{(r)}\|_\infty\le A_r$ 和
$\|K^{(r)}\|_\infty\le K_r$。因为所有系数实对称，$A_-$ 将
实轴送入实轴，无需用复 strip 范数替代下列 composition 界：

$$
 \begin{aligned}
 P_1&=K_1A_1,\\
 P_2&=K_2A_1^2+K_1A_2,\\
 P_3&=K_3A_1^3+3K_2A_1A_2+K_1A_3 .
 \end{aligned}                                                 \tag{IL.5}
$$

链式法则逐项给出 $\|\widehat p^{(r)}\|_\infty\le P_r$。
这三个目标是原 finite **compound 单腿** 的新完整界；没有把旧
two-leg difference 的小量当成单腿导数。结合 (IL.3)，Cauchy 可
进一步给出 $\|p^{(r)}\|_\infty\le P_r+r!E_p/\sigma^r$；该后继
regularity 消费由独立证明处理，本入口只输出 $E_p,P_1,P_2,P_3$。

## IL.4 实际运行协议与范围

`fourfold_codazzi_inverse_density_lift_owner.py` 完整复用原 RW 的
W/R31/K48/H/normalizer 准入，并额外准入整个 169-cover 与 wiener、
原 cover process、原 source、九步 publication/manifest 的全链 SHA。
从固定 Git 历史恢复两份原 gzip；恢复不运行任何科学目标。
两 native 的全部 258 个 rational complex coefficient pairs 必须逐项
相同，负频共轭和两 central imaginary zero 均以精确有理数检验。

新科学只在本仓库公开 Actions，320-bit Arb。四个小目标有固定顺序，
每个完整结果球先保存再读回；最终 `complete=true` 只在四项均有
完整正式记录时成立。新的 JSON 不发布数组，保留原载体的完整
bytes/SHA/commit/source、同一 selected identity 和所有输入 receipt。
历史大载体只在 Actions 私有临时目录中使用，仓库不重添这些数据。

该结果是后继全频 compression residual 及 opposite-sign regularity 的
一个实际输入。它不授予有限 Galerkin inverse、全 $\Theta$ 的 one-loss
支付、真实 PDE signed matrix、两个 physical mean rows、$\nu$/phase
Schur、或本课题完成标准。
