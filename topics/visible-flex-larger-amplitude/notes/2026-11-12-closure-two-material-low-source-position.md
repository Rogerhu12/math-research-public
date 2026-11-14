# 低输出两材料核：保留胞元 12 的真实源位置

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-12。

**状态。** 下列公式是 R42 有向 Green 表示的直接限制，给出独立的正上界；数值范围逐个输出文件明示。它们没有改变实际 strong M20 的 $g$、完整 20 个输入高度、46 个浅低频自由度、原 q 连续解析宽、完整均值或点态逆分母。尚不据此宣称 strong 全频联合盒通过。

## 1. 两种材料不得按总积分比例拆分

令 $n=12$，$k>12$，$m\in\{2,4,\ldots,92\}$。R42 记号下，$\phi_m$ 是深端线性边界条件与浅 Dirichlet 归一化的列，$\psi_m$ 满足真实浅端条件 $(Q,\Xi)=(0,1)$。其 Green 源列在目标 $k>n$ 是 $\phi_m(r)\psi_{m,Q}(s)\mu_n/\mu_{12}$。

strong 的物理包络与辅助中心剩余谱上界记为 $V_s$、$X_{s,n}$、$R_{s,n}$，并置

$$
\epsilon_{s,n}(r)=\frac{R_{s,n}}{X_{s,n}}
 \exp\{-2(\tau_{\rm ref,n}-\tau(r))\}.
$$

这里 $R_{s,n}$ 含辅助解校正与全部非主 $m=2$ 线性频率；它是固定的 canonical 逐频径向质量之和。R33 §16.7 因而允许源积分后再取输出模的最大值。不能将其变成随 $r$ 改变的频率质量分配。

独立径向材料为 $d_1=V_s^2/(rw)$。对每个真实材料面板 $I$，其 canonical 源积分有上界

$$
J_{1,I}=\sup_I\frac{r^4 V_s^2}{\sqrt{12}\,\mu_n}
 \int_I\frac{dr}{r}.
$$

故保留源位置的径向 corr 核满足

$$
\Gamma^{(1)}_{k n,m}\le
 \frac{\mu_n}{\mu_{12}}\Phi_{k,m}
 \sum_I\sup_I|\psi_{m,Q}|\,
 J_{1,I}\sup_I\epsilon_{s,n}\,
 e^{-m\inf_I\tau},
$$

其中 $\Phi_{k,m}$ 是两个物理输出分量分别取径向 supremum 后之和，且已含 $(1+m)e^{m\tau}$ 权和 strong 目标包络归一化。目标的 q 包通过同一 $\sigma_k$ 除法转成 strong 包，完整角权不另重复相乘。

旧合并正核 $\Gamma^{\rm tot}$ 本身也界定单独的 $d_1$ 或 $d_\lambda=|\lambda|V_s^2/w$ 限制。因此可取 $\min(\Gamma^{(1)},\Gamma^{\rm tot})$ 作为径向上界，同时用旧 $\Gamma^{\rm tot}$ 保守界定 $d_\lambda$。这不是把旧核乘某个总积分比例。

在 R55 两材料固定频率质量条件 $B\ge120,w\le1/2$ 下，中心剩余部分对 near 输入的低输出列可用

$$
\frac52\min(\Gamma^{(1)},\Gamma^{\rm tot})
 +\frac{2}{285}\Gamma^{\rm tot};
$$

对 low 输入改用 $2/9$。原显式 $m=2$ 主列保持其已付上界。上述系数仅用于中心二次导数；完整均值、点态逆分母和新变化的二次项仍分别保留原 $216\,\Gamma_{\rm rem}$、$3\rho\Gamma_{\rm base}$ 等项。

## 2. 真实浅列无需重做深端积分

在胞元 12 浅端，$\psi_Q=0,\psi_\Xi=1$ 是边界定义。对于 $u=m^2-4$，已用 gauge 的初值就是

$$
(q_g,\xi_g)=(0,(r_b/r_c)^u).
$$

原真实材料最后一个面板的 `radius_right` 已围住同一个 $r_b$，可直接初始化这一列。原 `closure_weighted_panel_flow_v4.py` 将各面板继续分为 Peano–Baker 子片，保留原 $AB\le2^{-20}$ 及严格正宽双端交集。反向推进使用同一个 determinant-one 精确流的区间逆与同一个 projective 公共幅度实现。每片的 $Q$ 绝对值还可与已付原 whole-cell $\psi_Q$ 上界取小；两者都包住同一个真列。

新的入口只调用 `SourceValues` 中与 `RealHead` 相同的显式源函数，不调用 `RealHead` 构造器的全背景半径积分。所有需要的真实半径来自已付材料包。它仍重新严格积分所需的流标量核，不能描述为“没有新积分”。输出分别记录流核积分次数及新背景半径积分数 0。

## 3. 已完成的首次粗界与最小真列探测

- `closure_two_material_low_edge.py` 的 session 39839 正式 exit 0，4.248 秒，峰值 72,356 KiB。它遍历 1873 个真实源面板与全部 46 模，却用 whole-cell $\psi_Q$ 上界代替上述逐面板值。最坏 $m=92$ 的径向上界 $\log_2\Gamma^{(1)}=3.6635889833\ldots$，旧合并核为 $-6.02299300329\ldots$；取小后的 near 列仅缩到旧列的约 $0.83567$。这是有效但过粗的上界，不是精确问题的障碍。
- `closure_two_material_low_pb_edge.py` 的 session 6291 正式 exit 0，14.877 秒，峰值 65,496 KiB。同一真实胞元的 5839 个 PB 子片、同一 192-bit 精度、同一解析宽，仅重算 $m=92$，得到 $\log_2\Gamma^{(1)}=-8.983036606255\ldots$；对应 near 修正列是旧 $3\Gamma^{\rm tot}$ 的 $0.109431134845\ldots$。此包明确 `full_low46_window_covered=false`。

## 4. 完整 46 模已付，但完整 strong 联合门仍未付

session 66660 使用同一已执行源码的 fresh prefix，正式 exit 0，93.923 秒，峰值 65,820 KiB。全部 46 模逐个重算完毕，最坏仍为 $m=92$，完整边的 $\log_2\Gamma^{(1)}=-8.983036606255\ldots$，near 修正列为旧 $3\Gamma^{\rm tot}$ 的 $0.109431134845\ldots$。完整输出 `closure-strong-two-material-low-pb-12to13-low46-r1.json` 明示 `full_low46_window_covered=true`，保留每模的 $\psi_Q$ 径向源积分，供其他更深目标按自己的真输出列复用。

随后 session 91559 正式 exit 0，14.357 秒，峰值 70,560 KiB。该**纯浮点诊断**将此完整低边和 R55 已付的五个 near 窗高边代回原完整 641 行，共改变 4 个中心二次导数条目，完整均值、点态逆分母、新变化二次项和真正远端反馈全保留。原大于 1 的两步循环消失，最大两步乘积的浮点 $\log_2$ 为 $-1.76689954547\ldots$；但整个正矩阵的浮点谱半径仍为 $61.0368852303\ldots$。因此这一步尚不支付 strong 全频联合收缩，也不能把单条循环改善当作完成。

下一份独立诊断将分解 LL、高块和远端反馈，并使用 R50 已证明的支撑零项：$DQ(C_{\rm low})$ 对 low 变化的输出至多 $|m|=184$，故 rest 和无限高频的该中心线性项为零；新变化二次项与完整 $216$ 余项不会随之删除。旧失败粗界、已执行源码和各自资源文件均冻结保留。
