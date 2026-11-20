# R141 补篇：同一实际高逆的径向加权 head 源响应

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**已证明：** 对同一个已成实际 given-head 高逆，下面的加权标量积分给出完整 head 源的另一组上界。它使用全部原 closed gap/frame 行，保原外边界反馈和两端口拼接；不要求重算任何已成 Riccati、旧 ordinary-source sweep、GH5 五个源率或 GH4 四个响应目标。**尚未计算：** 本篇五个新的加权标量。没有据此声称低高或物理外边界逆已通过。

本篇消费 [full-real-delta 正区高图](R133-supplement-full-real-delta-positive-high-root-to-regular-graph.md) 的 (P.4)、(P.11)–(P.15)，以及 [完整源窗合同](R141-supplement-actual-GH-source-window-and-return-contract.md) 的 (H.2)–(H.5)。原低角 $193$ 维、独立 moving mean、物理频率 $4j$、归一化角测度、普通 $dr$、真正 root 和 $R=25/8$ 全不改变。

## W1. 新目标与旧目标的区别

原 GH5 用全 collar/body 的点态 sup，GH4 将其乘已成高图的 ordinary-source 列。那些完整结果继续只读保留。新目标保留源系数在径向上的分布，将它和**原已成**阻尼核组合后才取 whole-domain 最大值。

令

$$
\mathscr X=L^2(I;E_L),\qquad
B(r)=[B_{HL,c}(r)+\Delta B_{HL}(r)]S(r)^{-1},\qquad
S=\operatorname{diag}(I,q,qI).
\tag{W.1}
$$

这里 $B$ 已含一次且仅一次输入 $S^{-1}$。它是角向算子、径向点态；角 primitive 项没有造成径向非局部输入。$B_{HL,c}$ 的高输出至160，实际 family 差的高输出至288；这只限定源的支集，不截断高未知量。

在每个原 body comparison panel $J_k$ 上，取完整新局部比较

$$
b_k\ge\|\langle4D\rangle^{1/3}B_{HL,c}S^{-1}\|_{J_k}
 +(1+16\cdot288^2)^{1/6}
       \|\Delta B_{HL}\|_{J_k}\max(1,q_k^{-1}).
\tag{W.2}
$$

第一项按原 signed $128\times193$ real matrix 算完所有系数和后，再左乘逐模 $(1+16j^2)^{1/6}$、右乘原 even/mean $q^{-1}$，最后取全矩阵 Schur 上界。第二项用同一 context 的完整 `HL` family fee。中心 mean 列确为零；**实际 family mean 列保留**。所有真实 principal/drift/primitive/mean 差沿用同原源定义，不另加或删掉一项。

这些局部 $b_k$ 仅是本篇新加权积分的运行期中间量。本次不求或保存原 GH5 的任何全 collar/body sup，不调用其五目标入口。collar 的完整源界直接读取 GH5 已存两条 whole balls之和 $b_c$，不再构造 collar 源率。

## W2. 只读的完整高比较行

同一原 body native
`1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c`
的 base-order 全4650行，每行保存了正阻尼下界 $k_i>0$ 和 source frame 上界 $C_i>0$。原文件还保存完整反馈 $\chi$、原外高反射、两阶、3594 interfaces和真实参考身份；whole-object admission先验证全部这些事实。

对同155 comparison panels（其中154个 body panels）与4650原 closed rows取**精确有理共同细分**。最多4803格，每格 $I_\alpha=[a_\alpha,b_\alpha]$ 有长度 $h_\alpha=b_\alpha-a_\alpha>0$，携带其原 row 的 $k_i,C_i$ 及原 source panel 的 $b_k$。完整覆盖

$$
I_b=[1192029371497/5000000000000,25/8]
\tag{W.3}
$$

且不遗漏任何原 row 或 source panel。细分没有缩窄 source balls，没有新接缝跳项，也没有把原区间包围当作点值；每个原包围在所属所有子格继续完整使用。原真正 root collar另由已成 collar合同保留。

在 $I_\alpha$ 上设 $f_\alpha=C_i^2b_k^2$，解两个**新的**标量比较方程

$$
 y_+'=f_\alpha-2k_i y_+,
 \quad y_+(r_b)=0;
 \qquad
 -y_-'=f_\alpha-2k_i y_-,
 \quad y_-(R)=0.
\tag{W.4}
$$

对任一固定非负初值 $v$，整格末值为

$$
v_{\rm end}=e^{-2k_ih_\alpha}v
 +(1-e^{-2k_ih_\alpha})\frac{f_\alpha}{2k_i}.
\tag{W.5}
$$

该常系数解朝 $f_\alpha/(2k_i)$ 单调，因此整格最大值不超过两个端值的最大值。这是 closed-cell 估计，不能用未付导数的采样插值替代。实现从原 gap whole ball取 lower，从 frame whole ball取 upper；所有新非负上界先取 directed endpoint再作正乘积，整格长度按真有理差包围。每格末端上界传给下一格，两个方向均扫完整共同细分。

## W3. 为什么取两支最大值即可

在原真实 diagonal high frame 中，固定输出半径 $r$，stable 和 unstable 两支的输入区间分别是 $[r_b,r]$ 与 $[r,R]$。它们在普通 $L^2_r$ 中正交；两支输出在原 $Z=(Z_s,Z_u)$ 的 Hilbert 直和中也正交。

令 $K_B$ 是实际 body diagonal source算子与 (W.1) 的复合。原 pointwise frame/阻尼比较和 Cauchy–Schwarz给

$$
\|(K_Bx)_s(r)\|^2
 \le y_+(r)\|x\|_{L^2([r_b,r])}^2,
\qquad
\|(K_Bx)_u(r)\|^2
 \le y_-(r)\|x\|_{L^2([r,R])}^2.
\tag{W.6}
$$

两式相加得

$$
\|K_Bx\|_{L^\infty_rZ}
 \le G_B\|x\|_{L^2(I_b)},\qquad
G_B^2=\sup_{r\in I_b}\max\{y_+(r),y_-(r)\}.
\tag{W.7}
$$

半区的共同端点是零测集，不改变输入范数。此处的最大值来自真实径向输入支集，而不是把同一个输入产生的两个输出误当作独立输入。旧无权源列用两支平方积分之和是合法较粗估计；本篇无需重算它，也不把改用最大值说成旧结论错误。

角向有限源矩阵、原 high frame以及 angular primitive都在同一个 $r$ 上作用，故不会破坏 (W.6) 的径向支集。高反馈算子本身可能混合两支，但它继续由原已成完整 resolvent统一控制，不能对该反馈免费重复使用本支集改善。

## W4. 保原实际高反馈和两端口拼接

只读原 base0 whole summary 的

$$
q_c,r_c,B_c,q_b,r_b^{\rm op},\sigma,
\tag{W.8}
$$

分别对应 `collar_resolvent`、`collar_reflection_upper`、`collar_ordinary_source_gain`、`body_resolvent`、`body_cut_reflection_upper`、`interface_resolvent`。$q_b$ 已包含全部实际高 family 和 canonical exterior high reflection。原 native 的 $C_b$ 为 `raw_reconstruction_L2_multiplier`；也只读整条保存球，不重新积分。

写 $\xi_c=\|P_cx\|$、$\xi_b=\|P_bx\|$。它们来自真正点态低到高源的两径向输入区，所以
$\xi_c^2+\xi_b^2=\|x\|^2$。
在原 (P.11)–(P.14) 中以 (W.7) 替换唯一的 body普通源项，得到以下正行向量（列顺序为 $\xi_c,\xi_b$）：

$$
\begin{aligned}
X&=(\sigma q_cB_cb_c,\ \sigma r_cq_bG_B),\\
Y&=r_b^{\rm op}X+(0,q_bG_B),\\
S_b&=q_b[X+(0,G_B)],\\
S_c&=q_c[Y+(B_cb_c,0)],\qquad U=S_c.
\end{aligned}
\tag{W.9}
$$

$U$ 是真实 root outgoing state 行；在这个 homogeneous head-response 函数中，原 stable-root、外部mean/head、affine和两个cut独立端口都设为零。那些端口在完整原高图中仍各自存在，不能把 (W.9)当作它们的响应矩阵。

这一步既不重算原 $\chi$，也不重新判断已成接口门。只读值即使因显示球而略宽，(W.9)都是正表达式，上界方向仍保持。

## W5. 完整体、root及外迹新上界

令 $h_c=9/10^6$ 是原真正 collar长度上界。原重构给

$$
\|G_HBx\|_{L^2(I_c)}\le3\sqrt{h_c}\,S_c\xi,
\qquad
\|G_HBx\|_{L^2(I_b)}\le C_b S_b\xi .
\tag{W.10}
$$

两个输出区间正交。因此新的完整 raw-$L^2$ 响应可以用明确的正2×2矩阵

$$
H_B^{\rm rad}
=\left\|\begin{pmatrix}3\sqrt{h_c}S_c\\ C_bS_b\end{pmatrix}\right\|_2.
\tag{W.11}
$$

它不用先把两列各自取 norm再套 triangle；也没有假定全高解的两次响应彼此正交。矩阵每个 entry是完整已付的非负上界，取其2范数是对全部 $\xi\ge0,\|\xi\|_2=1$ 的合法最坏情况。

若 $A^TA$ 的上界元素为 $\bar a,\bar b,\bar d\ge0$，则

$$
\|A\|_2^2\le
\frac{\bar a+\bar d+
\sqrt{(\bar a-\bar d)^2+4\bar b^2}}2.
\tag{W.12}
$$

这里是先构成非负上界矩阵，再用其 Perron最大特征值；$(\bar a-\bar d)^2$ 不是原两个不确定对角差平方的区间替代。

另外保存

$$
H_Z^{\rm rad}=\|S_b\|_2,\qquad
H_{\rm root}^{\rm rad}=\|U\|_2,\qquad
t_X^{\rm rad}=\frac5{388}H_Z^{\rm rad}.
\tag{W.13}
$$

末式仍是原真正高 frame 的有界外迹恢复，不从任意体 $L^2$取端点。普通外端 $H^{-5/6}$、原 root $Z$ 单位均不改。GH4的完整旧四球继续保留；本篇新组合即使未比它紧，也不能据上界大小推断奇异性。

## W6. 五目标保存与后续消费

纯模块 `fourfold_codazzi_actual_GH_radially_weighted_math.py` 只在原七模块 context与whole admitted body上定义这些新目标。保存顺序为：

| 字段 | 资格 |
|---|---|
| `actual_GH_body_weighted_unperturbed_source_upper` | (W.7) 的完整 $G_B$ |
| `actual_GH_weighted_raw_L2_from_complete_head_upper` | (W.11) 的完整 $H_B^{\rm rad}$ |
| `actual_GH_weighted_body_Z_sup_from_complete_head_upper` | (W.13) 的 body $Z$ sup |
| `actual_GH_weighted_root_outgoing_Z_from_complete_head_upper` | (W.13) 的原 root outgoing $Z$ |
| `actual_GH_weighted_outer_even_Hminus5over6_from_complete_head_upper` | 真正高外 even trace |

每量whole ball写入后完整读回并检查包含原有向upper，后继只消费读回upper。(W.9)使用第一条保存后的 $G_B$；末条使用第三条保存后的 $H_Z^{\rm rad}$。数值失败只保已完成小前缀，禁止把未完成扫格或未保存球写成成功。

实际工作量是152个原 body source-parent矩阵（同父格的两个cutoff拆分仅复用同一 packet/q/fee）、不超过4803格的两个scalar sweeps；约9606次新标量指数，无新矩阵指数或193传播，无旧源扫格调用。运行期只存小规模共同细分与局部系数，不发表这些可重算数组。公共 owner还须保旧GH5/GH4、L、centre排除以及两完整高图的只读引用；公共Actions之外不执行数值。

本篇可把未来 actual internal body门中的 $H_B$ 和 physical外块中的 $t_X$ 换成新的合格完整上界，其余 low receiver、family return和193atoms公式不变。它**不能**授旧WJK $F$ 同样结果，不能省略 $C(F-G_H)B$、原finite-$\rho$桥、原七外端口、两条WPN RHS、负区连接或非线性完成标准。
