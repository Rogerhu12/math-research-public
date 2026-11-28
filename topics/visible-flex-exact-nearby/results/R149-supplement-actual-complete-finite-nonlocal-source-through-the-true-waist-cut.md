# 原完整有限非局部源和独立物理均值在真截面的费用

在实际选定成员与原固定 $\eta_0$ 上，取 $97\le |j|\le 2^{20}$，物理频率 $n=4|j|$。从真根到原 $r_c=76285779072683/320000000000000$ 的完整 GNF 非局部源，对自然终端 Ai 的物理腰 $L^2$ 费用小于 $0.002848$，对同一冻结公共输入的费用小于 $0.03532$。以下各项包含独立物理均值和原根 Airy shear。两参考列一栏允许两个原参考输入同时存在。此处支付的源与有限 GLW 的局部加项分属同一原试探的两个线性加项。[GNF](R149-supplement-complete-root-collar-nonlocal-source-with-both-physical-circle-inverses.md)

| 原输入 | 完整 mixed 源的径向 $L^1$ | 归一物理腰 | 公共输入物理腰 | ASQ16 有序高行 |
|---|---:|---:|---:|---:|
| 原终端 Ai | $<0.0000699273$ | $<0.002848$ | $<0.03532$ | $<0.00291$ |
| 两参考列 | $<0.000138375$ | $<0.005635$ | $<0.06988$ | $<0.00575$ |

**证明。** [GNF 46150791569/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46150791569) 原终态科学与末步骤同一 2754 字节结论的 SHA256 为 `38ef9f41a3013fc54f6b781365597c96363a8d9674971fd00b82084211958dc7`，提交 `2ec32df32a1afe66000e4c38f26414e81f3ed32d`。全部 16 个原径向格及 1136 个频率组完成。对每一个径向格，原 owner 在全部输入组合完成后同时取 $H^{-2/3}$ 第一行的算子费用 $a_i$ 和真偶均值第二行的费用 $m_i$，累加
$$
 M=\sum_i |I_i|\sqrt{a_i^2+m_i^2}.
$$
整件 `physical_outputs_through_completed_slabs[mode].joint_L1[1]` 的两个有向端点为 $6.99272271138793\cdot10^{-5}$ 和 $1.383744086046234\cdot10^{-4}$。它们控制真正 $H^{-2/3}\oplus H^{-1}$ 的 Bochner 积分，因为角常数的 $H^{-1}$ 范数就是其绝对值。原 $g_1=J(K_w-R_QJe)$ 已含两个有序角逆的实际作用。[原 GNF 逐格累加](../scripts/fourfold_codazzi_collar_genuine_nonlocal_owner.py)

原整个支撑包含于 $[r_+-1/200,r_*]$。ASQ29.2 在该段每个真实插入位置从上述完整两行 mixed 原子到归一物理腰的界为 $40.72$。两个实际均值都在原传播中，WPL 左半读仅计一次。因此自然腰费用小于 $40.72M$。GSW 的 $\|N_i\|<62/5$ 给第三个费用列。对真正 ASQ16 高行，在原坐标次序利用 $N_i\mathcal S P_{97}=\Lambda_+^{-1}T_F^{-1}P_{97}$，自然费用另乘原 $10.611(1.061)\sqrt{0.097^2+0.022^2}/1.1$。在两参考列栏，此结论按相同右端正规作用于原允许的参考输入，包括将原终端嵌入第一列的限制。整件端点及各严格比较可用所附有理数读取器核对。其它径向原片、负侧局部源和正端响应保持各自真实输入。[真截面与完整腰行](R149-supplement-true-strict-cut-and-two-physical-output-windows.md)；[有序真右端](R149-supplement-first-genuine-source-through-the-physical-waist-and-common-input.md)；[有理数读取器](../scripts/fourfold_codazzi_complete_nonlocal_strict_cut_read.py)
