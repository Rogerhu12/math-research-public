# R205：权零、权 −2 两个完整 pure 函数块与一个右 step 查询的同时真实支付

日期：2026-11-15。**完整纸面证明，本稿没有新研究计算。** 使用 R201 与 R204 已付的两个完整 pure 像，同时保留真实控制词的全部基准第四成本。它不是从线性 span 直接宣布几何可达。

来源：[R102](R102-finite-query-fourth-cost-control-and-cone-quotient.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R180](R180-fixed-circle-invisible-third-hook-and-signed-fourth-period-gauge.md)、[R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R199](R199-faithful-monotone-step-for-the-complete-universal-pure-space.md)、[R200](R200-right-step-nonzero-bridge-response-and-closed-hook-obstructions.md)、[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md)、[R204](R204-complete-weight-minus2-pure-image-equals-nine-dimensional-response.md)。

## 1. 结论与真实对象

记 U 为 R105 的完整 canonical 第四成本空间，R 为真实第四响应空间，$\pi V=V_{-4}$ 为 universal pure 四次算子。令

$$
P=\pi U,\qquad P_0=\pi U_0=\pi R_0,\qquad
P_{-2}=\pi U_{-2}=\pi R_{-2}.
$$

R201 与 R204 已分别证明

$$
\boxed{\dim P_0=3,\qquad\dim P_{-2}=9.}                      \tag{1}
$$

这里保留全部 profile 函数与真实右锚；这些下标是正仿射作用的真权，不是相位 Fourier 模式。R204 的新 run 为 43684612905，source `df8522fc261de1dbb09975a594f0fda93f0867b0`；它只消费已存九个响应纯基与十二个新增真实基，十二列全部准确成员，未重做旧联合 rank 或原式归约。本稿使用其完整数学结论，不重复该实际。

**定理。** 可以固定一个共同物理区间、一个非退化重叠的光滑三矩 R183 圆 $(f,g)$、其最右 g 下降带中的一点 $x_0$，以及一个非零常数 $\kappa$，使下列结论成立。

对任意给定 $F_0\in P_0$、$F_{-2}\in P_{-2}$ 和实数 z，存在一条实际有限、光滑、空间闭合的 hook 几何 $X$，其 scalar/frame 全部周期相接，并有

$$
M_X=0,\qquad T_X=\kappa\mathfrak H,
$$

$$
\boxed{
\operatorname{pr}_0\pi V_X=F_0,\qquad
\operatorname{pr}_{-2}\pi V_X=F_{-2},\qquad
(\pi V_X)(g)(x_0)=z.
}                                                           \tag{2}
$$

前两个等式都是 universal 函数算子身份，$\operatorname{pr}_0,\operatorname{pr}_{-2}$ 是真权投影。此几何上的同一圆满足 R183 的完整二阶、三阶 range。$\mathfrak H$ 是 R180 的非零、对该圆不可见的第三 hook；$\kappa$ 与目标 $F_0,F_{-2},z$ 无关。

特别取三个目标都为零，准确支付的是**权零和权 −2 两个完整 pure 函数分量，共十二个函数坐标**，再加一个额外末 step period 查询。未声称 $\pi V_X$ 在其他权为零，也未支付完整 mixed 周期或逐 s 第四 ruling。

本结论选择新的参考几何，因而其度量也随设计改变。对每个最终选定 X，之后才固定它自己的目标 $g_\varepsilon$；没有把设计参数当作已经构造的同一 g 等距运动。

## 2. 十二个完整函数坐标与一个真实低权响应

先在 $P_0\oplus P_{-2}$ 中选一个真实基 $F_1,\ldots,F_{12}$。两权不同，故直和准确。R201 的三基和 R151/R204 的九基提供这一选择；本稿只使用 (1) 的真实结论。

对任意 $V\in U$，令

$$
(\operatorname{pr}_0+\operatorname{pr}_{-2})\pi V
=\sum_{i=1}^{12} Q_{{\rm low},i}(V)F_i,
\qquad Q_{\rm low}=(Q_{{\rm low},1},\ldots,Q_{{\rm low},12}). \tag{3}
$$

这些是完整 U 上的固定实线性泛函。

真实响应空间由

$$
K=\mathcal B_P(\tau),\qquad P\in E_8,\quad\tau\in W
$$

张成，其中每个 P 有 R70 的实际小二阶族、每个 $\tau$ 有同端口实际零矩第三环。不能把真权投影自动当作一个这样的原方向。因此，先将给 (1) 的有限个响应向量写为有限个原生成方向的实线性组合；收集这些原方向后，其 $Q_{\rm low}$ 像仍张满 $\mathbb R^{12}$。从中选十二个真实生成器

$$
K_j=\mathcal B_{P_j}(\tau_j),\qquad 1\le j\le12,
$$

使 $\mathsf A=(Q_{\rm low}(K_1)\ \cdots\ Q_{\rm low}(K_{12}))$ 可逆。这个选择只用有限维真实 span，不授任何免费第四成本；每个实际第三环的成本稍后全部保留。

第十三个方向取 R200 的

$$
K_{13}=\mathcal B_A([P,R]),
$$

其中未乘长度的正常态 second 算子 A 与 $\tau_0=[P,R]_{\rm diag}$ 正是 R200 (1)、(3)。其 pure 响应是

$$
\mathcal H(q)=\frac{D\tau_0(q)[A(q,q)]-2A(q,\tau_0(q))}{8}.  \tag{4}
$$

按 R71/R83 的规范，$\pi K_{13}=\mathcal H$。这也可直接从 R83 的三项完整 $\mathcal B$ 式取 $-4$ 模式得到：系数依次为 $1/8,1/4,-1/4$，恰合为 (4)。本文固定这个方向。

R200 的 A 在 E8 中只有权 $-1,1,-3$ 的三个分量，$\tau_0$ 的权为 $-5$。其中权 $-3$ 分量是 P 的倍数，而

$$
D\tau_0(q)[P(q,q)]-2P(q,\tau_0(q))=0.                       \tag{5}
$$

确实，置 $p=q''$，有 $(P(q,q))''=-2pp'$、$\tau_0''=p^2p'$，式 (5) 的两项都等于 $2J(p^3p')=-p^4/2$；右 collar 给端值零。因此

$$
\boxed{\pi K_{13}\in P_{-6}+P_{-4},\qquad Q_{\rm low}(K_{13})=0.} \tag{6}
$$

这里 (5) 是原式函数身份，不是纯幂尾消项的外推。

## 3. 共同物理区间、同一个 faithful step 与非零第十三行

先固定十三个生成器的实际小二阶族和实际第三环，并用有限的真实连接将它们放到同一个 scalar 常值 germ、frame $I\to I$。同时固定 R180 的 hook prototype 及两个零矩、零第三 frame 桥。以上只是有限多个路径和小参数紧族，因此有一个共同紧 scalar 包络。

在这个包络之后，先固定最终使用的共同 $\xi$ 坐标及合法物理区间 I，使 $h>0$ 与 $\xi+\omega>0$ 有正间隙，并预留足够的 profile 带、左三矩补偿带及末 step 带。若布局需要共同仿射变换，在这一步已经完成；下文不再对已选 step 或查询施加一个未经核对的最终变换。不要求任意预给窄 I 都容许这些控制。

具体在这些**最终坐标**中选末 step 的右端 $c>1$，并使全部有限 packet 布局留在上述正间隙内。直接使用 R200 在这个最终 c 处的原式首项：若 $q(c-t)=a_0t^8+O(t^9)$，则 $\mathcal H(q)$ 的 $t^{25}$ 系数为 $a_0^4 8^4 7^4 c(7c^2-5)/(192\cdot25)$，严格非零。因此先在最终坐标中得到单下降 step q 及带内点 $x_0$，满足

$$
\mathcal H(q)(x_0)\ne0.                                    \tag{7}
$$

先在这个最终坐标的充分小邻域中，按 R200 的完整积分式所需有限阶拓扑平滑该 step，使它真为光滑平端下降 step，并保 (7)；此处只需该式的 $q,q',q''$ 连续性，不要求把有限正则 step 在任意高阶拓扑逼近。再用 R199 的小幅 compact 扰动，可在**任意充分小的同一最终坐标邻域内**使这个已经光滑的末 step 对整个 P faithful；四次行列式非零只排除有限个扰动幅度，单调性和 (7) 都是可保持的开放条件。这里没有使用“任意共同仿射变换只把 $\mathcal H(q)$ 的这个查询乘非零常数”的未经证明说法。

重新执行 R183 的左三复矩补偿、八个完整 packet 和统一归一，得到固定的 $(f,g)$。这些操作不改最右查询看到的右尾；末 packet 的非零幅度与统一归一只将 (7) 乘一个非零四次因子。故仍有

$$
(\pi K_{13})(g)(x_0)\ne0.                                 \tag{8}
$$

同时存在这个**同一末 step** 内的有限个点 $x_1,\ldots,x_m$，使

$$
\mathcal E_g:P\longrightarrow\mathbb R^m,\qquad
F\longmapsto(F(g)(x_1),\ldots,F(g)(x_m))
$$

为单射。取有限维左逆后，(3) 的十二个坐标就是这些真实查询的固定实线性组合。没有只用两个已付权的表来忽略其他权在同一 profile 上的相消。

在末 step 及其右方 f=0，原相位 pure 输入是 $q=f+ig=ig$，而四次齐次性给 $F(ig)=F(g)$。因此这些读数就是该圆实际 $-4$ 模式的查询。它们没有要求输入 primitive 独立取值。

定义

$$
Q(V)=\big(Q_{\rm low}(V),(\pi V)(g)(x_0)\big)\in\mathbb R^{13}.
$$

由 (6)、(8)，其真实响应矩阵是

$$
\boxed{
\mathsf K=\big(Q(K_1)\ \cdots\ Q(K_{12})\ Q(K_{13})\big)
=\begin{pmatrix}\mathsf A&0\\ *&\mathcal H(g)(x_0)\end{pmatrix},
\qquad\det\mathsf K\ne0.
}                                                           \tag{9}
$$

## 4. 把全部真实基准成本纳入同一个求解

对十三个实际第三环 $L_j$，写

$$
M_{L_j}=0,\quad T_{L_j}=\tau_j,\quad V_{L_j}=v_j.
$$

每个 $v_j$ 是真实第四成本，既不置零，也不假设只有所选十三个分量。R101/R102 的复制词给

$$
M_{Z_j(t_j,n)}=T_{Z_j(t_j,n)}=0,\qquad
V_{Z_j(t_j,n)}=E_j(t_j)+n(2v_j+t_jK_j),                      \tag{10}
$$

其中 $E_j$ 连续，是真实偶成本且与复制数 n 无关。所有值属于有限 U；对未知的其他函数分量也没有清零操作。

把十三个词拼接，得实际控制块 Z。由完整零矩传递，

$$
Q(V_Z)=E(t)+n(2v_\Sigma+\mathsf Kt),                         \tag{11}
$$

其中 $v_\Sigma=\sum_jQ(v_j)$，$E(t)=\sum_jQ(E_j(t_j))$。令

$$
t^0=-2\mathsf K^{-1}v_\Sigma,\qquad
\mathcal C=t^0+[-1,1]^{13}.
$$

若 $\mathcal C$ 超出某个原小族参数区间，先以固定有限次数复制小族来覆盖它，保持同一个 scalar 包络；不能把大 t 擅自放进一个局部族。至此 E 是固定紧立方体上的连续函数。

对任意目标 $y\in\mathbb R^{13}$，取有限整数 n 足够大，使

$$
t\longmapsto t^0+n^{-1}\mathsf K^{-1}(y-E(t))
$$

把 $\mathcal C$ 映入自身。Brouwer 不动点给真实有限 t，使 (11) 准确等于 y。这就是 R102 的保基准证明，并非只取导数作线性响应。

所有顺序均已支付：先实际小族和共同包络，再 I、圆、Q 与 (9)，再 $t^0$ 和固定小族复制次数，最后 n。目标不同只改变有限控制参数与复制数，不要求重新选择圆。

## 5. 空间闭合、八边词和准确四倍成本

取第 3 节固定的 R180 prototype $L_t$，有 $M=0,T=t\mathfrak H$，并取同 scalar 的 $M=T=0$ frame 桥 $C_1,C_2$。设

$$
P_1=L_tC_1,\qquad P_2=C_2.
$$

把实际控制 Z 插入第一类 prototype，改成 $P_1'=L_t ZC_1$。它的 scalar/frame 端点准确保持，M、T 也保持；其真实空间位移一般改变，本稿不将它归零。

按照 R180 的 Klein 八边词 $1,2,1,2,2,1,2,1$ 组装。每类 prototype 在 Klein 四群的四个 ambient 左旋位置各出现一次，其位移和因四群矩阵之和为零而相消。于是得到真正光滑、空间闭合的周期浸入带 X，并有

$$
M_X=0,\qquad T_X=4t\mathfrak H=\kappa\mathfrak H.
$$

M=0 各段之间的完整第四传递可加；ambient 左旋不改 scalar 成本。若 $V_{\rm base}$ 是未插 Z 的整个八边几何成本，则

$$
\boxed{V_X=V_{\rm base}+4V_Z.}                            \tag{12}
$$

这里是四倍，不是把 R200 另含 $BB^{\rm rev}$ 加倍的八倍搬来。$V_{\rm base}\in U$：即使它的第三算子非零，R105 的真实倒行倍增已将任意 M0 同端口/frameI 成本收入 U。

在 (11) 取

$$
y=\frac14\left(\big([F_0+F_{-2}]_{F_1,\ldots,F_{12}},z\big)-Q(V_{\rm base})\right),
$$

便得到 (2)。原基准、frame 连接、控制词自身、非零第三 hook 以及实际位移全部留在证明中。

R183 的三个矩和八包三次幅度恒等式对这些真实变量几何仍成立；T 的整算子只取同一 $\kappa\mathfrak H$，并在这个圆的所需槽上不可见。因此同一个圆的完整二、三阶 range 保持，不需要逐设计重新拟合 profiles。

## 6. 已支付与仍未支付

这是十三个独立真实目标的同时支付，其中前十二个等价于权零、权 −2 两个完整 pure 函数为指定值。其他仿射权可由 (10) 的所有基准同时改变；(2) 不声称这些改变为零。

没有把 R201/R204 的两个 pure 像等号外推到整个 P，也没有把一条末 step 查询归零当作 R198 的整段函数归零。独立二阶 gauge 的 joint period/ruling、所有第四逐 s 条件、高阶、收敛、嵌入、reach 和宏观幅度仍未付。

本稿也不把准确零值经任意几何近似搬到无开常段路径：非零门是开放条件，等于零通常不是。要同时消去常段并保 (2)，需要在新几何族中另保足够正则的约束参数；这里没有自动获得它。
