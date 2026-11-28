# 真严格段的两行物理腰读数及所有原负侧接口

取实际选定成员，$c=r_+-1/200$。在原 $0\le r\le c$ 任意位置、任意完整 $H^{-1}\oplus H^{-1}$ 物理输入到归一 WPL 腰行的费用小于 $3.828$。对 $L^2\oplus L^2$ 输入，真实 $P_{97}$ 高腰行的费用小于 $0.01957$。两个真实均值都由同一原传播演化。初态与接口作为原子进入，普通源按 $dr$ 积分。

**证明。** 原 SP.34/PRN.18 的直接严格源注入把一个物理原子送到该截面完整 $(Y,Z)$，费用小于 $1.060693$，第二坐标含两密度均值。ASQ29.1 在任意部分严格区间给径向费用 $3.24$，非径向逆序传播的第一行费用 $1.488$。腰端物理密度转换 $1.041$ 及 WPL 半读 $0.719$ 接在其后。故完整物理行费用小于 $0.719(1.041)(3.24)(1.488)(1.060693)<3.828$。独立的真普通 $L^2$ 严格传播 $8.22$ 接真实高行 $0.00238$ 得第二式。[严格两态原注入 PRN.18](R149-supplement-complete-phase-receiver-in-original-negative-source-windows.md)；[真实截面 ASQ29.1](R149-supplement-true-strict-cut-and-two-physical-output-windows.md)；[原态严格传播 NRO.1](R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md)

严格段 $A=\eta\partial+L_0$ 的同一真角逆还满足
$$
 \|J:H^{-1}_{\mathrm{even},0}\longrightarrow L^2_{\mathrm{odd}}\|<5.77.
$$
事实上对 $P_0=\eta^{-1}I$ 有 $J=(1-JL_0)P_0$。使用 GJO 原 $\|L_0\|_{L^2\to L^2}<1855913/500000$、JCR 原 $\|J\|_{L^2\to L^2}<7/5$、$\eta>1.10865$ 和 $\|I\|_{H^{-1}\to L^2}=\sqrt{17}/4$。把前式乘 $0.00238(8.22)$，则严格段真正第一行在 $J$ 前的标量 $H^{-1}$ 输入到高腰的费用小于 $0.113$。若使用原局部 $J:H^{-2}\to H^{-1}$，则相应整腰费用为其实际局部常数乘 $3.828$。这些摄入范数可各自用于原物理频率投影分部，最后输出同在真实腰上。[严格完整角逆](R149-supplement-uniform-negative-circle-inverse-through-the-true-root.md)；[原 GJO 严格 $L_0$ 及双角逆估计](../scripts/fourfold_codazzi_genuine_outer_seam_operator.py)

[原 GJR 46145341825/1](R149-supplement-actual-all-576-genuine-root-window-interface-operators.md) 的 576 个原接口之和 $m=2.0673760869834316\,10^{-8}$ 是实际 mixed 输入的有向上界。对其中 $r\ge c$ 的接口用 $40.72$，其余完整 $H^{-1}$ 输入由原 mixed 输入支配，亦可共用系数 $40.72$。[原 GJOR 46150669215/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46150669215) 的其余全部 1973 个真严格接口有 $s=2.945707169633746\,10^{-12}$ 的完整两行 $H^{-1}$ 源有向上界，故自然腰费用小于 $1.128\,10^{-11}$。两张原表物理接口不交；原 521 个附加同 cubic 分点的跃迁准确为零。由此，所有 2549 个原负侧接口在双参考列、双符号、全部 $n\ge388$ 上给
$$
 C_{\rm nat}<40.72m+3.828s<8.42\,10^{-7},\qquad
 C_{\rm common}<1.045\,10^{-5},\qquad C_{\rm ASQ16}<8.60\,10^{-7}.
$$
后两项分别应用 GSW 原 $62/5$ 和有序 $10.611(1.061)\sqrt{.097^2+.022^2}/1.1$。接口费用不乘体源长度。原两收据完整 SHA256 分别为 `47348f89fa2dd8b19c2a5dab4d3719c4ef2adf6f883d36e5d4c43035df6f8f0e`、`7db431ce7fea60a5e46da17641fcefbc8842753430f12a588ee345160c419380`。上述比较只读取原完整有向端点并作有理数运算。[原有序右端](R149-supplement-first-genuine-source-through-the-physical-waist-and-common-input.md)；[读取器](../scripts/fourfold_codazzi_true_strict_waist_all_interfaces.py)
