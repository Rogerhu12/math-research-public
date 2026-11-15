# R197：单边活动包的非零 ruling 方向迁移到无开常段几何

日期：2026-11-15。完整纸面存在证明；没有新的几何积分、profile 评价或数值 rank 判定。

来源：[R70 任意矩阵桥](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R72 真实倒行的零二、三阶 frame 桥](R72-same-state-zero-second-third-arbitrary-frame-bridge.md)、[R180 闭 hook 几何](R180-fixed-circle-invisible-third-hook-and-signed-fourth-period-gauge.md)、[R189 无开常段正则桥](R189-nowhere-constant-state-matrix-bridges-and-closed-hook-geometry.md)及 [R195 单边活动包方向](R195-single-active-packet-period-kernel-and-nonzero-fourth-ruling-direction.md)。

R195 用一个标准常状态段证明单边活动包 gauge 的 ruling 商像确实非零。本稿保留一个有限四点增广子式，将该方向迁移到 R189 的真实无开常段几何。不能仅由“原商类非零”就援引开放性：三矩空间的秩必须先固定，本稿准确支付这一步。

## 1. 结论与目标度量的区别

存在有限光滑闭合 hook 几何 $\widetilde X$，满足

$$
M=0,\qquad T=\kappa\mathfrak H\ne0,
$$

且没有任何非空开区间使 $(k,h,\omega)$ 同时常值。可以选一个固定的 R183 光滑非退化三矩圆 f、g，以及一个固定 $w\in C_c^\infty(J)$，使：

- f 在 J 上为非零常值，$\mathbf m(g,w)=0$；
- 任意有限实倍的相位家族 $w_\theta=\sin^2\theta\,w$ 保完整第三 range、第四 period 和两个种子；
- 其第四 ruling 商响应不是零，给一条真实有符号方向。

几何扰动通常改变度量。本文不声称沿扰动保存原来的 $g_X$ 或原目标 $g_\varepsilon$。正确顺序是先选定一个最终的 $\widetilde X$，再固定其目标

$$
\mathsf g_\varepsilon
=g_{\widetilde X}+\varepsilon^2(dY_f^{\widetilde X})^2.
\tag{1}
$$

在这个新的固定几何、固定目标及同一 profile 圆上，才使用上述二阶 gauge。f、g、w 作为 $\xi$ 函数可在迁移中保持不变；相应实际向量场会随几何改变。

本文只得非零响应线，没有证明原第四 ruling 目标属于该线或完整 joint 像，也没有清掉原第四 period。

## 2. 先使三矩几何空间具有真实秩三

记 R47 的三列

$$
\mathbf w(s)=
\left(\frac{d(s)^2+1}{4h(s)},\frac{d(s)}2,\frac{h(s)}4\right),
\qquad d=h\omega-k.
$$

先构造一个有常态端 germs 的基准 hook 几何，并要求其中经过三个状态

$$
h=1,\qquad d=0,1,2.
\tag{2}
$$

可具体选择这三个状态为 $(k,h,\omega)=(0,1,j)$，$j=0,1,2$。R70 允许规定有限 frame/scalar 端口；连接每个相邻状态时保真实 $\omega_s=k_s/(2h)$，不是把 omega 独立指定成不合法函数。

把一条有限路线经过三态并回到标准 scalar 端口。其实际矩阵和 frame 增量可以非零。再用 R70 的任意矩阵、任意 frame 桥补成一条路径 B，使

$$
B:\quad M_B=0,\quad F_B:I\longrightarrow I,
$$

且 scalar 首末同为标准态 $(0,1,0)$。预先经过三态的路线可放进 R70 构造的固定连接部分；末端保留八个完整圆参数的可逆矩阵 Jacobian。故这仍是 R189 所需的正则有限路径，不是对一个没有正则性的任意路径直接使用其逼近结论。

采用真实倒行，而非形式负算子。令 $D=\operatorname{diag}(-1,1,-1)$。由于 B 的 frame 首末均为 I，

$$
F^{\rm rev}(s)=D F_B(L-s)D,\qquad
(k,h,\omega)^{\rm rev}(s)=(k,h,\omega)_B(L-s)
\tag{3}
$$

仍首末 frame I、同 scalar 端口。R72/R189 的原锚传递在 $M_B=0$ 时给

$$
M_{B^{\rm rev}}=0,\qquad T_{B^{\rm rev}}=-T_B.
$$

因此真实闭词 $B\,B^{\rm rev}$ 满足

$$
\boxed{M=0,\quad T=0,\quad F:I\longrightarrow I.}
\tag{4}
$$

位置位移未被规定，也通常不为零；(4) 没有把倒行误当第四成本的负元。

将 (4) 接入 R180 的一条 prototype。其 M、T、frame 端口不变，而整个闭体仍用实际新位移作 Klein 八边词组装。每种 prototype 在四个左旋位置出现，$I+g_1+g_2+g_1g_2=0$，故实际位置重新准确闭合。这样得到含 (2) 的基准闭 hook 几何 $X_0$，仍有同一个非零 $\kappa\mathfrak H$。

在三个采样状态上，三矩列的行矩阵为

$$
W_*=
\begin{pmatrix}
1/4&0&1/4\\
1/2&1/2&1/4\\
5/4&1&1/4
\end{pmatrix},
\qquad
\det W_*=-\frac1{16}\ne0.
\tag{5}
$$

所以基准几何的 $\mathcal W$ 真正三维。这个结论来自三个准确状态值，不是数值 Gram 小特征值。

## 3. 固定一个 R195 的非零 gauge 及四点子式

所有有限基准路径选定后，选择有正余量的共同物理区间 I。按 R183/R195 选择光滑圆，使一条 g 上升边位于 $c>1$，且 f 在该边为非零常值。由 R195 的四个测试函数构造，固定

$$
w\in C_c^\infty(J),\qquad
\mathbf m(g,w)=0,\qquad D_w\mathcal C(g)\ne0.
\tag{6}
$$

这里的圆和 w 已经固定；后续几何扰动不重新求解或调整它们。

在基准标准状态开段内选择两个不同位置 $s_a,s_b$，其局部参数差为 $\sigma_b-\sigma_a\ne0$。固定相位 $\theta=\pi/2$。R195 保完整入历史的公式给

$$
\mathcal B_{\pi/2}(w)(s_b)-\mathcal B_{\pi/2}(w)(s_a)
=2(\sigma_b-\sigma_a)D_w\mathcal C(g)\ne0.
\tag{7}
$$

入历史贡献在这两个状态点的差中准确相消，没有被人为设零。

再取 (2) 中 d=1、2 的两个采样点 $s_1,s_2$，按行 $s_a,s_1,s_2,s_b$ 形成增广矩阵

$$
\mathcal A(X_0)=
\begin{pmatrix}
\mathbf w(s_a)&\mathcal B_{\pi/2}(w)(s_a)\\
\mathbf w(s_1)&\mathcal B_{\pi/2}(w)(s_1)\\
\mathbf w(s_2)&\mathcal B_{\pi/2}(w)(s_2)\\
\mathbf w(s_b)&\mathcal B_{\pi/2}(w)(s_b)
\end{pmatrix}.
$$

末行减首行，由 (5)、(7)，

$$
\boxed{
\det\mathcal A(X_0)
=-\frac18(\sigma_b-\sigma_a)D_w\mathcal C(g)\ne0.
}
\tag{8}
$$

所以有一个明确有限的真实评价证书，同时证明三列秩三以及该 ruling 响应不属于其 span。改变合法共同齐次初值，只把最后一列加上前三列的常系数组合，不改变这个结论。

## 4. 几何与真实历史的连续性

把有限个基准构件分别拉到固定参数区间，保留每个构件的实际长度及速度因子；四个评价点随各自的固定归一化参数位置运输。长度均为严格正的固定有限数。

R195 式 (12)--(14) 写出该响应：

- 局部项只用 $h,d,h_s,d_s$ 的有限有理组合以及固定 profile 积分；
- 历史项只用 R73 的真实累计 $\mathsf m(s)=\int M_{\rm raw}\,ds$；
- $M_{\rm raw}$ 是有限阶真实几何 jets 的光滑表达式，实际 ds 及长度因子均保留。

在 $h$ 和 $\xi+\omega$ 有统一正下界的固定紧邻域中，这些有限积分、状态值及历史在足够高的有限 $C^m$ 拓扑下连续。R189 给的是这种含真实长度的逼近，不是把任意重参数化后导数仍当作原物理导数。

因此 $\mathcal A(X)$ 的全部 16 个数连续，且 (8) 在一个充分小的控制邻域内仍非零。这里确实使用了增广子式；若原 $\mathcal W$ 秩不足三，仅凭其旧商类非零不能作这一步推论。

共同 I 已留正余量，进一步缩小邻域即可使同一 I 继续满足 $h>0$、$\xi+\omega>0$。f、g、w 的支撑和全部三个矩因此保持原样。

## 5. 应用 R189，同时保准确 M、T 与闭合

现在对整份有限 prototype 配方应用 R189：

1. 所需矩阵桥保留其八个正则矩阵参数，并用第九个 omega 端值参数补偿。
2. 自由 h 扰动在两端全平，准确保持规定 frame/scalar 端值及目标矩阵，并可任意有限阶逼近原正则解。
3. 每条独立选择的桥都可选成内部无开常状态段；其余副本、倒行和左旋由这些新桥真实生成，不独立偷换。
4. hook 交换子词的矩阵和第三算子身份继续准确成立；$B\,B^{\rm rev}$ 仍用同一新 B 和它的真实倒行，所以 (4) 继续准确成立。
5. prototype 的实际位移可以改变，整个 Klein 八边词按新位移仍准确闭合。

原开常态 germ 被全平端 jets 代替。R189 已证明这足以使所有有限拼接、共同原函数及倒行为真正 C-infinity，并且有限拼接不会新造一个正长度常状态段。

选择逼近精度落入 §4 的子式非零邻域，得到一个最终的无开常段几何 $\widetilde X$，满足

$$
\det\mathcal A(\widetilde X)\ne0.
\tag{9}
$$

最终几何上原四个点一般已不是精确常态；不再从它们提取常段斜率。它们只作为连续运输的四个真实评价点使用，(9) 本身即证明

$$
[\mathcal B_{\pi/2}^{\widetilde X}(w)]\ne0
\quad\text{于 }C^\infty(S^1)/\mathcal W_{\widetilde X}.
$$

## 6. 最终同目标下的 gauge 作用与未付边界

在这个已选定的 $\widetilde X$ 上固定 (1)。R183 的低阶证明对真实变系数几何适用，仍给同一个 f、g 圆的完整二、三阶 range。由 (6)，w 自动满足六交叉矩，且 f 在其支撑上常值。hook 的 $L_f(w)=0$ 因而保持。

取 $w_\theta=\sin^2\theta\,w$，其任意有限实倍都有相位周期和种子零值，第四 period 准确不变。第四 ruling 商按该实倍线性变化，且在 $\pi/2$ 由 (9) 非零。gauge 平方及其他三矩分量由 R184 的同一个第三 profile 右逆真实支付。

这给无开常段几何上一条非零有符号 joint 响应方向，并没有把几何路径成本半群当作向量空间。正、负参数作用于最终固定几何上的二阶齐次 profile。

原第四 $V^0_\theta$ 可能仍不为零，原 $K^0_\theta$ 也未证明属于这些响应的可达商像。因此本文不授完整第四可解、收敛的有限等距族、嵌入、reach 或主课题的厚度结论。它支付的是一个此前欠缺的具体非零方向，且明确离开了依赖标准开常段的提取前提。
