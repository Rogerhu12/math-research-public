# R248　有限 C² 闭图的相位族、固定帽与全参数归约

2026-11-14，geometry，AI 辅助研究。**状态：已证明的条件定理。** 本条适用于满足字面接缝条件的有限 $C^2$ 场，不要求它已经精确等距，也不要求 $F_0\in C^3$。它不把当前数值 BVP 的小反射残差当作准确 $C^2$ 接缝，不把带固定标记的整个族当作空间刚体运动。

## 1. 与已有结论的关系

以下工具已经证明，本条不重复认领：

| 已有条目 | 精确范围 |
|---|---|
| [R32 §9](R32-height-development-and-global-tail-graph.md) | 从其精确 Darboux 图假设得到 $C^2$ 连续参数族；(32.33) 给物理角的相移与逐点固定平盘 |
| [R8](R8-fixed-cap-curvature-markers.md) | 固定帽标记使用其自身固定诱导度量，保持共同度量与 $C^2$ 参数连续性 |
| [R11](R11-exact-all-phase-normal-chord-reduction.md) | 活动—固定点对的全相位法向弦条件准确化为四个标量余量 |
| [R37 §5](R37-double-normal-bottleneck-and-distance-cover.md) | 旋转不变平帽的未标记基面只需一次完整空间 reach 检查 |
| [R21](R21-flat-cap-markers-without-reach-loss.md)、[R24](R24-weak-markers-with-explicit-reach-margin.md) | 具有所列局部图、分离或定量余量时，固定弱标记保留全部相位的 reach |
| [R20](R20-cap-marker-amplitude-bounds-euclidean-gap.md) | 单侧帽标记高不超过 $A_b$ 时，这种机制的 $\delta_E\le A_b$ |
| [R238](R238-planar-germ-marker-rigidity.md) | 在其无平面开片、支撑边界与四个仿射独立标记中心假设下，排除包括反射的非平凡全等 |

这里补上任意有限 $C^2$ 载体的完整相位构造、相对算子误差的全相位恒等式、准确反射接口，以及哪些集合量能消去时间、哪些仍需整面空间输入。

## 2. 一个共同的材料面与固定帽

令 $M$ 是由活动闭环带 $M_A$ 与两个闭圆盘 $K_+,K_-$ 沿其边界圈粘合而成的紧连通闭光滑面。在环带上使用同一个真实材料角 $\theta\in\mathbb R/(2\pi\mathbb Z)$；不同径向片和中央反射缝使用兼容的径向图册。在帽的内部使用 Cartesian 坐标，极点的不同极角表示是同一个材料点。

设 $\psi_\alpha:M\to M$ 是下述共同圆周作用：环带上

$$\psi_\alpha(s,\theta)=(s,\theta+\alpha),$$

帽上是其 Cartesian 圆盘的平面旋转。边界的角图册一致，使这个作用在整个 $M$ 上光滑，且在帽极点也光滑。这里没有将一般非线性的 $\phi\leftrightarrow\theta$ 角变换沿半径硬延伸到极点；R240 指出的极点问题不在此被忽略。

令 $R_\alpha$ 为绕同一竖直轴的空间旋转。给定未标记的 $C^2$ 正则浸入

$$\bar F_0:M\longrightarrow\mathbb R^3$$

使其在两帽上恰为

$$\bar F_0(x)= (x,h_\pm),\qquad x\in \overline B_{r_\pm}(0). \tag{248.1}$$

因此两个帽圆心都在同一旋转轴上。实际前缀、尾、collar 的分段表达必须先有共同的完整 Cartesian 两阶 jet，使这里的 $\bar F_0$ 确为一个 $C^2$ 映射。

取固定的 $b_\pm\in C_c^2(B_{r_\pm})$，在帽的固定法向 $n_\pm=\pm e_z$ 方向加标记。把

$$B(x)=b_\pm(x)n_\pm\quad(x\in K_\pm),\qquad B=0\quad\text{在 }M_A$$

看作整个 $M$ 上的 $C^2$ 向量函数；紧支撑保证它在 cuff 附近连同两阶导数均为零。定义

$$
\bar F_\alpha=R_\alpha\bar F_0\circ\psi_{-\alpha},
\qquad F_\alpha=\bar F_\alpha+B. \tag{248.2}
$$

在活动环带上，这就是所要求的

$$F_\alpha(s,\theta)=R_\alpha F_0(s,\theta-\alpha). \tag{248.3}$$

在帽上，平面旋转和逆材料旋转抵消，所以 $\bar F_\alpha=\bar F_0$，继而 $F_\alpha=F_0$。固定的非轴标记并没有随 $R_\alpha$ 转走。

### 定理 248-A：有限场的相位正则性

在以上条件下，每个 $F_\alpha$ 都是整个闭面上的 $C^2$ 正则浸入，且

$$\alpha\longmapsto F_\alpha\in C^2(M;\mathbb R^3)\quad\text{连续}. \tag{248.4}$$

每个帽材料点逐点固定。因此帽中任一闭握持区 $H$ 的映射及直径与 $\alpha$ 无关。是否满足 $\operatorname{diam}F_0(H)\ge.2D$ 仍是单独的真实尺度条件。

**证明。** 旋转与光滑微分同胚的复合保持 $C^2$，故 $\bar F_\alpha\in C^2$；加上 $B\in C^2$ 保持此正则性。在活动区，它是正则浸入的微分同胚重参数化和空间等距变换；在帽上它是平面圆盘上的图，微分前两行组成单位矩阵，所以仍为正则浸入。cuff 附近 $B=0$，两侧来自同一个 $\bar F_\alpha$，没有新接缝。

证明 (248.4) 只需 $C^2$。取有限个较小闭坐标片覆盖紧面。对 $|\beta|\le2$，链式法则把 $\partial^\beta(\bar F_0\circ\psi_{-\alpha})$ 写为 $\bar F_0$ 的至多二阶导数在 $\psi_{-\alpha}(x)$ 的值与 $\psi_{-\alpha}$ 的至多二阶导数的有限乘积和。后者光滑依赖 $\alpha$，前者在对应紧集上一致连续。因此 $\alpha_j\to\alpha$ 时，这些表达在每个较小坐标片上一致收敛。有限覆盖给 $C^2$ 范数收敛；再乘连续的矩阵 $R_\alpha$、加固定 $B$ 即得结论。

此论证没有对 $F_0$ 作第三阶求导。它证明所需的 $C^2$ **强连续性**，不额外宣称 $\alpha\mapsto F_\alpha$ 可在 $C^2$ Banach 空间中求导。帽上的逐点固定性已由 (248.1)—(248.2) 直接得到。□

对任意连续相位函数 $\alpha(t)$，特别是 $\alpha(t)=\pi t/2$，复合后即得到 $t\mapsto F_t$ 的 $C^2$ 连续性。嵌入性仍须第 5 节的全空间条件；正则浸入不能替代它。

## 3. 有限片的准确接缝输入

### 3.1 cuff 与固定帽

在 cuff 附近使用同一个物理半径 $r$。准确的平帽两阶迹是

$$F(r_c,\theta)=(r_c\cos\theta,r_c\sin\theta,h),$$
$$F_r(r_c,\theta)=(\cos\theta,\sin\theta,0),\qquad F_{rr}(r_c,\theta)=0, \tag{248.5}$$

以及对上面已有迹作至多二阶所允许的角求导所给出的 $F_\theta,F_{r\theta},F_{\theta\theta}$。这些完整 Cartesian 迹在 $R_\alpha$ 与 $\theta-\alpha$ 的组合下不变。有限 collar 若使其非轴部分的 $0/1/2$ 径向 jet 在 cuff 为零，且背景有 $w=w_r=0$，就满足这项输入。

同属活动区的 prefix/tail、tail/collar 或径向 Hermite 接缝，在两侧用同一材料角施加 (248.3)，原来准确相等的两阶 jet 仍相等。只匹配高度两 jet、只在角样点匹配，或者在两侧使用不同角规范，都不足以给出这个结论。

### 3.2 中央反射缝

令 $U(s,\theta)$ 为上片，$s\ge0$，并用有符号坐标 $u$ 定义下片

$$F(u,\theta)=J\,U(-u,\theta)\quad(u\le0),\qquad
J=\operatorname{diag}(1,1,-1).$$

两侧成为 $C^2$ 映射的准确必要且充分迹条件为

$$
U_z(0,\theta)=0,\qquad
(U_s)_{xy}(0,\theta)=0,\qquad
(U_{ss})_z(0,\theta)=0
\quad\text{对全部 }\theta. \tag{248.6}
$$

**证明。** 零阶匹配为 $U=JU$，恰是第一式。一阶径向匹配为 $U_s=-JU_s$，恰是第二式。二阶径向匹配为 $U_{ss}=JU_{ss}$，恰是第三式。对第一式作角导数、对第二式作一次角导数，即得所有剩余至多二阶的角向和混合迹匹配。反过来，全两阶匹配当然包含这三式。分片 $C^2$ 函数在公共边界全两阶迹一致，便在共同坐标中成为 $C^2$ 函数。□

由于 $JR_\alpha=R_\alpha J$，而上、下片都使用同一 $\theta-\alpha$，(248.6) 对全部相位保持。非圆核心一般不允许上、下片各选独立相位；共同边界位置就可能不再相等。

若反射平面是 $z=h_c$，把第一式改为 $U_z=h_c$，反射写作 $(x,y,z)\mapsto(x,y,2h_c-z)$，其余两式不变。当前 large-core 消费者的配准是**只作用于 XY 的一次 proper SE(2)**，它不改变 $z=0$ 平面；新增绝对高度对齐只施加于尾，原完整 prefix 不另加均值。因此该消费者实际用的是 (248.6) 的 $h_c=0$ 版本。其报告中的 inlet $z$、XY $F_s$、$z$ $F_{ss}$ 小残差并不是这些函数准确为零的证明。

## 4. 同一个参考度量：全相位算子误差与曲率

在活动区给定同一个旋转不变的正定参考度量

$$g_A=E(s)\,ds^2+a(s)^2d\theta^2,$$

它在 cuff 图册中与平帽参考度量兼容。在固定帽上，给 $g$ 使用固定图 $F_0|_{K_\pm}$ 自身的诱导度量。这样得到一个共同参考度量 $g$；这项帽度量是在设计中明确固定的，不能把带标记图误称为对旧平帽度量等距。

令 $G_\alpha=F_\alpha^*\langle\cdot,\cdot\rangle$，定义点态相对误差

$$\varepsilon_\alpha(x)=
\left\|g_x^{-1/2}(G_\alpha(x)-g_x)g_x^{-1/2}\right\|_{\rm op}. \tag{248.7}$$

### 定理 248-B：无需时间网格的两项恒等式

在活动区有

$$G_\alpha=\psi_{-\alpha}^*G_0,\qquad
\varepsilon_\alpha(x)=\varepsilon_0(\psi_{-\alpha}x). \tag{248.8}$$

帽上的误差为零且与相位无关。因此

$$\sup_{x\in M}\varepsilon_\alpha(x)=\sup_{x\in M}\varepsilon_0(x)
\quad\text{对所有 }\alpha. \tag{248.9}$$

若 $\kappa_{\max,\alpha}(x)$ 是实际浸入的最大主曲率绝对值，则同样

$$\sup_{x\in M}\kappa_{\max,\alpha}(x)
=\sup_{x\in M}\kappa_{\max,0}(x). \tag{248.10}$$

**证明。** 活动区的 $B=0$，对 (248.3) 求空间导数，旋转保持 Euclidean 内积，故得到第一式。$\psi_{-\alpha}$ 是参考度量 $g_A$ 的等距自同构，所以相对 Gram 误差的两个自伴算子在对应点之间由一个线性等距映射共轭。其特征值与算子范数相同，得 (248.8)。活动区的圆周平移满射，帽图固定，接缝值由共同两阶迹连续延拓，遂得 (248.9)。

同样，活动区的第一、第二基本形式在重参数化下拉回；环境旋转把单位法向一同旋转，shape operator 在对应切空间中共轭。主曲率保持，或在改法向时同时变号，绝对值不变。帽固定，接缝的曲率从两阶 jet 连续延拓，故 (248.10) 成立。□

在 $E=1$ 图册，若归一化 Gram 误差矩阵是 $\begin{pmatrix}e&f\\f&d\end{pmatrix}$，这里的范数是

$$\frac{|e+d|+\sqrt{(e-d)^2+4f^2}}2,$$

不是 $\max(|e|,|f|,|d|)$。对角 $g_A$ 的一般 $E$ 情形使用 $e=G_{ss}/E-1$、$f=G_{s\theta}/(\sqrt E\,a)$、$d=G_{\theta\theta}/a^2-1$。分量范数也会在这一固定坐标规则下平移，但不能因此把两个范数混同。

**注意全局参考度量不必在 $\psi_\alpha$ 下不变。** 非轴固定标记可使帽上的 $g$ 不旋转不变；证明只在活动区使用 $\psi_\alpha^*g_A=g_A$，在帽上使用 $F_\alpha=F_0$。这正是固定标记与共同度量相容的方式。

若一个真正的同 $g$ 加密序列逐层使用同一相位公式和同一固定帽，则每层的全相位误差由 (248.9) 等于其完整 $\alpha=0$ 误差。后者下降到原求解容差，就同时控制全部相位；相位本身按准确公式计算，不引入时间插值误差。这不是把有限时间样本升级为全时间结论，而是先用恒等式消去该变量。若改用有限导出网格之间的线性插值作为实际族，该插值是另一个映射，不能援用本结论。

本条不增加“所有 C² jet 差须机器收敛”的标准。六 jet 与曲率须足够支持当前有限场的正则性和几何预算；同 $g$ 非线性加密仍按 README 第 5 条的等距误差判据处理。

## 5. 像集合与 reach：未标记和带标记必须分开

记

$$A=\bar F_0(M_A),\qquad C_0=\bar F_0(K_+\cup K_-),\qquad
C=F_0(K_+\cup K_-).$$

由材料角平移的满射性，准确有

$$\bar S_\alpha=\bar F_\alpha(M)=R_\alpha A\cup C_0
=R_\alpha\bar S_0, \tag{248.11}$$
$$S_\alpha=F_\alpha(M)=R_\alpha A\cup C. \tag{248.12}$$

式 (248.11) 使用了 $R_\alpha C_0=C_0$。一般没有 $R_\alpha C=C$，所以不能把第二式改写成 $S_\alpha=R_\alpha S_0$。

若未标记 $\bar F_0$ 已嵌入，则 $\bar F_\alpha=R_\alpha\bar F_0\psi_{-\alpha}$ 是嵌入，并且

$$\operatorname{reach}(\bar S_\alpha)=\operatorname{reach}(\bar S_0),
\qquad\operatorname{diam}\bar S_\alpha=\operatorname{diam}\bar S_0. \tag{248.13}$$

这是严格的全相位归约：空间等距保持距离及最近点的唯一性，因此保持 reach；也保持直径。一次完整基面空间证据即可覆盖所有 $\alpha$。基面证据可以由 R241 的浸入覆盖门先证明嵌入并支付 reach，不能仅靠主曲率上界或无交叉的显示网格。

### 5.1 固定标记的统一扰动路线

先假定未标记 $\bar F_0$ 已是 $C^2$ 嵌入（例如已由 R241 的完整覆盖门付清）。再假定基面的所有有向法向弦已经满足 R24 的 $\tau_0$ 不等式，且平帽内标记满足

$$\|b\|_\infty\le A_b,\quad \|\nabla b\|_\infty\le G_b,
\quad\|D^2b\|_{\rm op,\infty}\le K_b\le1/\tau,$$

对所有相位，其支撑到相应平帽补集的**完整空间距离**至少为 $d_0>2A_b$，并且

$$
\frac1{\tau_0}+\frac{2G_b}{d_0}+\frac{4A_b}{d_0^2}
\le\frac{(1-2A_b/d_0)^2}{\tau}. \tag{248.14}
$$

则逐相位使用 R24 得到全部 $F_\alpha$ 为 $C^2$ 嵌入，且 $\operatorname{reach}(S_\alpha)\ge\tau$。这里的 $d_0$ 可以由 R11 的径高投影公式支付：对活动点 $p$ 与固定支撑点 $q$，

$$\inf_\alpha|R_\alpha p-q|
=\sqrt{(|p_{xy}|-|q_{xy}|)^2+(p_z-q_z)^2}. \tag{248.15}$$

再对全部 $p,q$ 取下确界。另一个帽、全部尾、反射半片与接缝都须在相应补集中，不能只算同帽边界的径向距离。

### 5.2 直接的活动—固定空间点对路线

若已经支付全部相位嵌入，或者同时使用 R241 中能够排除零弦的覆盖门来证明它，则 R11 可直接处理 (248.12)：活动—活动点对的距离与法向弦表达随共同旋转保持，固定—固定点对不变，活动—固定点对使用 R11 (3)—(6) 的四个准确全相位余量；连续块版本可用 R16/R62。

这仍须覆盖完整连续空间点对与局部曲率。两个不相交时刻的样本不能替代它；法向弦式在零弦处为 $0\ge0$，也不能单靠该式跳过全局单射性。对带标记面，跨固定帽的材料短路径不能未经证明就随活动点标签一起旋转并保持长度，因为帽度量一般不具有该旋转对称性。

因此，marked 整面的 reach **没有无条件的相位恒等式**。真正可消去时间的是 (248.14) 的统一标记条件或 R11/R62 的混合点对公式。

## 6. 完整直径与握持 Hausdorff 距离

令 $D=\operatorname{diam}S_0$，恪守课题定义。若 $|b_\pm|\le A_b$，同一帽的竖直配对给

$$d_H(C,C_0)\le A_b,\qquad d_H(S_\alpha,\bar S_\alpha)\le A_b.$$

对任意紧集，Hausdorff 距离不超过 $a$ 会使直径变化不超过 $2a$：分别将一对点移到另一集的距离不超过 $a$ 的对应点并用三角不等式，再交换两集即可。因此

$$|\operatorname{diam}S_\alpha-\operatorname{diam}\bar S_0|\le2A_b. \tag{248.16}$$

所以基面的完整上界 $\bar D_+$ 给 $D\le\bar D_++2A_b$。带标记的 $\operatorname{diam}S_\alpha$ 不必严格恒定；本题归一化用的仍是 $\alpha=0$ 的完整 $D$。

定义 $h_C(\alpha)=d_H(R_\alpha A\cup C,A\cup C)$。由于 $C$ 包含在两幅像中，准确有

$$
h_C(\alpha)=\max\left\{
\sup_{p\in A}\operatorname{dist}(R_\alpha p,A\cup C),
\sup_{p\in A}\operatorname{dist}(p,R_\alpha A\cup C)
\right\}. \tag{248.17}
$$

**证明。** Hausdorff 距离的两个有向上确界分别在 $R_\alpha A\cup C$ 与 $A\cup C$ 上取。源点属于共同部分 $C$ 时到另一集的距离为零，故可从两个源集合中略去该部分。但距离的**目标集合**仍须保留完整活动面和固定帽。□

这说明一个真实活动见证点就可以给下界，不需要先找到所有相位的最大值。它绝不允许把目标只留下核心、只算同一材料点位移，或把开放前缀当作整面。

还有比一般两次 Hausdorff 扰动更紧的固定帽比较：若 $C'$ 也是所有相位共同的固定紧集，则

$$|h_C(\alpha)-h_{C'}(\alpha)|\le d_H(C,C'). \tag{248.18}$$

**证明。** 对任意点 $x$，$|\operatorname{dist}(x,E)-\operatorname{dist}(x,E')|\le d_H(E,E')$，这是对几乎最近点用三角不等式再交换两集得到的。又有 $d_H(A\cup C,A\cup C')\le d_H(C,C')$，旋转过的活动集也一样。将这两个估计代入 (248.17)，对同一活动源集合取上确界，再取两个数的最大值，仍只损失 $d_H(C,C')$。□

特别地，固定标记使每个相位的真实 Hausdorff 变化量、以及其时间最大值，至多改变 $A_b$，而不是必然要付 $2A_b$：

$$|\delta_{\rm hold}(S)-\delta_{\rm hold}(\bar S)|\le A_b. \tag{248.19}$$

这是条件传递式；未标记族的见证也必须针对**完整未标记闭面**证明。当前约 $.96$ 的核心支持差不能未经整面球排除就代入这里。

若 $R_A=\sup_{p\in A}|p_{xy}|$，取圆周上不超过 $\pi$ 的相位差 $\delta$，同一点 $p$ 的旋转配对还给

$$d_H(S_\alpha,S_\beta)\le2R_A\sin(\delta/2)\le R_A\delta. \tag{248.20}$$

因此 $h_C$ 连续，在紧相位区间取得最大值。任一已付的相位见证给 $\delta_{\rm hold}$ 下界；没有定理保证完整闭面的最大值一定在 $\alpha=\pi/2$。若需要上界，具有覆盖半径 $\eta\le\pi$ 的相位网和各网点真实整面 Hausdorff 值给

$$\max_jh_C(\alpha_j)\le\delta_{\rm hold}
\le\max_jh_C(\alpha_j)+2R_A\sin(\eta/2).$$

这里仍不把点云距离叫作整面 Hausdorff 距离。

## 7. 欧氏刚体商与非平凡性

未标记时，由 (248.11) 取逆旋转即可准确对齐两像，所以

$$\delta_E(\bar S)=0,$$

尽管固定帽材料点不动且 $\delta_{\rm hold}$ 可以为正。这正好区分像集合的对齐与材料点运动。

带标记时，逆旋转对齐活动像，但将固定帽变成 $R_{-\alpha}C$，一般不等于 $C$。若每帽的标记高度都在同一个单侧区间 $[0,A_b]$ 内，对两个图用同一平面坐标配对，其高度差至多 $A_b$，故 R20 的论证给

$$\delta_E(S)\le A_b.$$

若只知道 $|b|\le A_b$ 而允许正负混合，这个直接上界改为 $2A_b$。这些上界都不提供严格正性。

一个充分的正性条件是：在某个相位 $\alpha_*$，两像确实不同，并且每个把 $S_{\alpha_*}$ 送到 $S_0$ 的 Euclidean 等距都必须逐点固定同一组四个仿射独立的标记中心。后一假设可在满足全部字面输入时由 R238 或 R14 支付；它不是由“小 marker”自动给出的。

四个仿射独立点迫使该等距为恒等，所以两像不同排除所有精确全等。还须排除最优距离仅趋零的可能：若 $T_j(x)=Q_jx+v_j$ 且 $d_H(T_jS_{\alpha_*},S_0)\to0$，固定一个 $p\in S_{\alpha_*}$，其像距紧集 $S_0$ 有界，故 $v_j$ 有界。$O(3)$ 紧，取子列使 $Q_j,v_j$ 收敛；紧集上的一致收敛给极限等距 $T$ 满足 $TS_{\alpha_*}=S_0$，矛盾。因此该相位的刚体商距离严格正，继而 $\delta_E>0$。$O(3)$ 包括反射，故未漏掉反射对齐。

同样由 (248.20) 和 Hausdorff 三角不等式，$\inf_Td_H(TS_\alpha,S_0)$ 连续，紧相位区间上的最大值存在。

## 8. 当前有限消费者能够直接用到什么

当前构造把活动上下片同步旋转并使用共同材料角，固定帽与标记不动；单次 XY 配准与这个定义相容。只要有限基面的准确全两阶接缝和正则性已经按其定义付清，定理 248-A 就直接给连续时间的 $C^2$ 族，不需要对第三阶导数加门。

在这个前提下，(248.9)—(248.10) 使当前有限场的完整空间 metric/operator 与主曲率检查只需做一次。未标记空间覆盖加统一 R24 标记余量，或者直接的全相位混合点对公式，才进一步支付全部时间的嵌入和 reach。旧 A 的已完成 q8 数值覆盖不自动成为新 M112 场的输入。

现有 `geometry_20261114_large_core_saved_prefix.py` 用原 $Y,DY,DDY$ 定义物理 quintic；`geometry_20261114_large_core_closed_assembly.py` 只报告 inlet 的三个反射残差，并明确未认证 literal reflected $C^2$ seam。因此不能仅以原 BVP 的接受旗或这些小残差宣布 (248.6) 已准确成立。可另行构造只改首个 Hermite 区间的准确 parity 规范形，保留其他节点和原实际尾，再读出其相对**同一个** $g$ 的 metric 与曲率费用；那是明确标识的有限场处理，不是修改原 BVP 成功旗。本条尚未为将来的新处理宣布费用已过门。

完整闭面、相同 $g$ 的真正求解精化、整面 $D$、实际握持 Hausdorff 下界和 $\delta_E$ 输入仍按课题 README 分别交付；本条只消去已经由公式准确控制的相位变量。
