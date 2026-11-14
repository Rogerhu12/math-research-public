# R137：真实第四闭成本锥的快速水平脉冲门与加速度 PSD

日期：2026-11-14。**纸面已证明。** 本稿把完整最高几何导数层的形式正性条件提升为真实成本闭锥正泛函的必要条件。矩阵、frame、第三算子和完整连接成本先支付，随后才使用时长极限和微幅脉冲。没有新的研究计算。

依据 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R112](R112-local-fourth-geometric-derivative-weights.md)、[R120](R120-G-lineality-of-the-closed-fourth-cost-cone.md)、[R127](R127-positive-affine-character-of-the-fourth-cost-cone.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md) 和 [R134](R134-acceleration-layer-from-complete-local-v4.md)。以下是 universal 原式空间上的结论；没有要求所有控制都留在任意预先指定的窄物理区间或有界总长中。

## 1. 成本锥与完整局部密度

按 R127 固定 scalar 常值 germ g、frame I→I，令

$$
\mathcal S_g=\{V_B:B\text{ 是实际有限同端口路径， }M_B=T_B=0\},
$$

$$
U=\operatorname{span}_{\mathbb R}\mathcal S_g,\qquad
C=\overline{\operatorname{cone}(\mathcal S_g)}\subset U.
\tag{1}
$$

R105/R120 保证 U、C 不依赖 g。取

$$
\lambda\in C^*.
$$

R120 给 $R=\mathcal R_8\subseteq C\cap(-C)$，因此

$$
\lambda(R)=0.
\tag{2}
$$

在包含 U 和所有完整局部系数的有限真实函数空间 E 内任取 λ 的线性延拓，仍记 λ。这个延拓只用于非零矩阵段的局部积分记账，不假设它在 E 的其他方向上非负。

R109/R112 的完整局部密度为

$$
L=L_0+L_2+L_4,\qquad m=m_0+m_2,
\tag{3}
$$

下标表示几何导数权。对任一平端路径 B 定义

$$
I_\lambda(B)=\int_B\lambda(L)\,ds.
\tag{4}
$$

局部积分 (4) 对真实拼接准确相加，无累计历史。若整条路径 $M_B=0$，由 R109 与 (2)，

$$
I_\lambda(B)=\lambda(V_B).
\tag{5}
$$

(5) 不要求 $T_B=0$；一般 $M_B\ne0$ 时，本稿不使用它。

状态与水平约束始终为

$$
S=(h,k,\omega),\quad h>0,\qquad
\omega_s=\frac{k_s}{2h}.
\tag{6}
$$

任一固定有限控制族先选定后，再取共同物理区间 I，使全部 $\xi+\omega$ 有统一正下界。无限重复同一有限族不会扩大其 scalar 包络。

## 2. 带线性局部成本上界的真实大矩阵补偿

**引理 1。** 固定 g、一个矩阵范数及一个紧 frame 小邻域。存在一套固定有限的真实单位矩路径及有界残差/末 frame 路径族，使任意 $M\in E_8$ 和该邻域内任意 frame A 都能由同 g 的平端路径 $Q(M,A)$ 实现，并且

$$
M_Q=M,\qquad F_Q=A,\qquad
|I_\lambda(Q)|\le c_\lambda(1+\|M\|).
\tag{7}
$$

全部路径的 scalar 值落在同一个紧集；(7) 没有约束总长、拼接数或累计第三算子。

**证明。** 取 E8 基 $E_1,\ldots,E_8$。R70 的真实桥定理给固定同 g、frame I、矩阵分别为 $\pm E_i$ 的十六条路径。另给同 g、frame I、矩阵目标在一个紧残差盒内的有界平滑路径族。后一族可用 R70 的大但固定辅助整圈数与统一参数 IFT 构造；有限覆盖后也只需有限族。每个族的正时长、scalar 正性、有限 jets 和局部积分均有统一界。

写 $M=\sum_i x_iE_i$。把每个 $x_i$ 分成带符号整数与绝对值小于 1 的余量。串接对应次数的 $\pm E_i$ 单位路径，再接残差路径，矩阵准确为 M，frame I。局部积分准确相加，所以其绝对值至多是单位成本界乘 $\sum_i|x_i|+8$，再加残差成本界。

最后接 R70/R72 给出的同 g、M=0、末 frame A 的有界局部族。它只增加固定成本界。每次接续仅按当前环境 frame 左旋转；m、L 均不因该固定环境旋转改变。由有限维范数等价得到 (7)。

每个单位路径闭合相同 scalar germ，重复只增加长度，不增加 scalar 值域。残差和 frame 族紧，故共同 I 可在这些族之后固定。证毕。

SO(3) 紧，R70 的局部平滑端点截面有有限子覆盖；每个子覆盖取紧的较小参数片后，jets 和局部成本上界的最大值有限。因此需要全部 frame 时也可取统一界，无须假设存在全局连续 Euler 角。下文实际上只有一个随快速缩放趋于固定值的 frame 小族，局部版本已经足够。

R70 的积分矩阵与 (3) 的点态矩阵对平端路径一致，因为 R73 的分部积分端项分别为零。这里没有替换矩阵约束的定义。

## 3. 先补 M/frame，再用真倒行去 T

对任一同 g、frame I、M=0 的实际路径 B，不论 $T_B$ 是否为零，R83 的真倒行满足

$$
M_{B^R}=0,\quad F_{B^R}=I,\quad
T_{B^R}=-T_B,\quad V_{B^R}=V_B.
$$

两块矩阵为零，实际第四传递的交叉项消失。因此

$$
BB^R\in\mathcal S_g,\qquad V_{BB^R}=2V_B.
$$

由 λ 非负和 (5)，

$$
\boxed{I_\lambda(B)\ge0
\quad\text{对同 g、frame I、M=0 的全部真实平端 B}.}
\tag{8}
$$

此处倒行没有给第四成本取负；它把已闭 frame、零矩阵路径的成本加倍，并准确消掉第三算子。

## 4. 快速缩放支付最高导数层的真实必要门

**定理 2。** 对任何满足 (6) 的光滑有限平端 scalar 路径 P，允许两端状态不同，

$$
\boxed{\int_P\lambda(L_4)\,ds\ge0.}
\tag{9}
$$

**证明。** 先固定 P。用固定平端桥从 g 接到 P 首状态，并从 P 末状态接回 g。桥按实际末 frame 左旋转，连接成本与矩阵不受这种旋转影响。

把 P 的时间参数压缩到原时长的 δ 倍，记为 $P_\delta$。scalar 状态路径与首末 germs 完全相同，真实水平约束 (6) 在重新参数化后仍成立；frame 则按实际新 k(s) 重新积分，不假设它保持不变。

导数权 (3) 给出准确等式

$$
M_{P_\delta}=\delta M_0(P)+\delta^{-1}M_2(P),
\tag{10}
$$

$$
I_\lambda(P_\delta)
=\delta I_0(P)+\delta^{-1}I_2(P)+\delta^{-3}I_4(P),
\tag{11}
$$

其中 $I_j(P)=\int_P\lambda(L_j)\,ds$。两条固定桥只给 (10)、(11) 增加 O(1)。

由于 P 的 k 值有界，快速段 frame 随 $\delta\to0$ 趋于 I。加上固定前后桥，完整路径末 frame 趋于一个固定旋转。其 scalar 首末为 g，矩阵范数为 $O(1+\delta^{-1})$。

按引理 1 接一个实际同 g 的补偿路径，使总矩阵为零、总末 frame 为 I。补偿矩阵是完整前序矩阵的负值，由真实正时长路径实现；不是负时间。其局部成本由 (7) 为 $O(1+\delta^{-1})$。首末 frame 的补偿由有界紧小族支付，不能用位置闭合或静默 frame 重置代替。

得到的总路径满足 (8)，因而

$$
0\le\delta^{-3}I_4(P)+O(1+\delta^{-1}).
$$

乘以正数 $\delta^3$ 并让 $\delta\downarrow0$，得到 (9)。补偿总长和重复数可以趋大，但每个 δ 对应真实有限路径；其 scalar 包络来自固定 P、固定桥与引理 1 的固定族，共同 I 不随重复数扩大。

最后接真倒行以去 T 已包含在 (8)，无需估计可能很大的第三累计历史。R109 的 (5) 在真实整条零矩路径上精确成立，所以没有遗漏其高阶历史的尺度贡献。证毕。

必须区分这里所界定的是 **局部** $I_\lambda(Q)$，并非补偿段完整 $V_Q$。后者的累计历史可以产生二次、三次重复数项，不能估成 O(重复数)。只有将实际完整零矩字形成之后，才按 R109 把它与 $\int L$ 的差识别为 R 中的响应；(2) 使这些真实历史项被 λ 准确杀掉。因此本证明没有用错误的“连接本身 O(1)，所以完整高阶历史也 O(1)”近似。

没有把 δ=0 当作实际路径，也没有证明一个固定总长或 reach 下可实施同样极限。

## 5. R129 正规式及加速度二次矩阵

R129 给

$$
L_4=D_sP_3+\mathcal N_4,
$$

$$
\mathcal N_4=
\bar A_{hh}a^2+\bar A_{hk}ab+\bar A_{kk}b^2
+(H_1u+H_2w)(ub-wa)+\widehat Q_4(S;u,w),
\tag{12}
$$

其中 $u=h_s,w=k_s,a=h_{ss},b=k_{ss}$。平端使 $P_3$ 两端分别为零。故 (9) 等价于对所有这样的真实 P，

$$
\int_P\lambda(\mathcal N_4)\,ds\ge0.
\tag{13}
$$

R130/R134 已证明 (12) 的正规状态系数属于实际 U，其 λ 值与第 1 节对 E 的任意延拓无关。

定义实对称矩阵

$$
A_\lambda(S)=
\begin{pmatrix}
\lambda(\bar A_{hh}(S))&\lambda(\bar A_{hk}(S))/2\\
\lambda(\bar A_{hk}(S))/2&\lambda(\bar A_{kk}(S))
\end{pmatrix}.
\tag{14}
$$

**推论 3。** 对每个 $S=(h,k,\omega)$，$h>0$，

$$
\boxed{A_\lambda(S)\succeq0.}
\tag{15}
$$

即两个对角元素非负，且

$$
4\lambda(\bar A_{hh})\lambda(\bar A_{kk})
-\lambda(\bar A_{hk})^2\ge0.
\tag{16}
$$

**证明。** 固定 $S_0$、向量 $(\alpha,\beta)$ 及非零 $f\in C_c^\infty(0,1)$。取

$$
h=h_0+\varepsilon\alpha f,\qquad
k=k_0+\varepsilon\beta f,
$$

由 (6) 准确积分 ω，起点为 $\omega_0$。小的正负 ε 均保持 h>0，路径平端，且 $S_\varepsilon=S_0+O(\varepsilon)$。速度、加速度分别为

$$
(u,w)=\varepsilon(\alpha,\beta)f',\qquad
(a,b)=\varepsilon(\alpha,\beta)f''.
$$

这时 $ub-wa=0$ 准确成立。将 (13) 除以 $\varepsilon^2$ 再取极限，得到

$$
(\alpha,\beta)A_\lambda(S_0)(\alpha,\beta)^T
\int_0^1(f'')^2\,ds\ge0.
$$

积分严格正，向量任意，故得 (15)。证毕。

这给当前五族完整混合原式的真实 PSD 必要门。只对 pure 尾的投影无法替代 (15)。

## 6. 加速度矩阵零点的面积项也必须为零

**推论 4。** 若某状态 $S_0$ 满足 $A_\lambda(S_0)=0$，则

$$
\boxed{\lambda(H_1(S_0))=\lambda(H_2(S_0))=0.}
\tag{17}
$$

**证明。** 由 (15)，每个固定向量 v 的标量函数 $v^TA_\lambda(S)v$ 在 $S_0$ 取局部最小值零，其全部一阶状态导数为零。用 $v=(1,0),(0,1),(1,1)$ 极化可得整个矩阵的一阶状态导数在 $S_0$ 为零。因此在小邻域中

$$
A_\lambda(S_0+\Delta S)=O(|\Delta S|^2).
\tag{18}
$$

取非零、非负、偶函数 $\chi\in C_c^\infty(-1,1)$。第一条微幅路径指定

$$
u=\varepsilon\chi,\qquad w=\varepsilon\chi',
$$

从 $S_0$ 积分 h、k、ω。首末分别为常值 germs，但不要求相同；这正是 (9) 已支付的开端口范围。$S_\varepsilon-S_0=O(\varepsilon)$。由 (18)，加速度二次项是 $O(\varepsilon^4)$；速度四次项同样为 $O(\varepsilon^4)$。三次首项为

$$
\varepsilon^3\int_{-1}^1
(\lambda(H_1(S_0))\chi+\lambda(H_2(S_0))\chi')
\bigl(\chi\chi''-(\chi')^2\bigr)\,ds.
$$

H₂ 的积分因奇性为零；H₁ 的系数为

$$
\int\chi^2\chi''-\chi(\chi')^2
=-3\int\chi(\chi')^2<0.
\tag{19}
$$

(13) 对正负 ε 都成立，故 H₁ 的首项必须为零。交换 u、w 得同样非零的 H₂ 系数，迫 H₂ 为零。证毕。

这里只在整个二次矩阵为零的状态得出 (17)；没有对仅秩一退化的矩阵擅自消掉全部面积项。

## 7. 若整个加速度矩阵被杀，最高层剩下点态四次非负

若 $A_\lambda(S)\equiv0$，推论 4 给 $\lambda(H_1)=\lambda(H_2)\equiv0$。此时

$$
\int_P\lambda(L_4)\,ds
=\int_P\lambda(\widehat Q_4(S;u,w))\,ds.
$$

重复推论 3 的共线微幅路径，并除以 $\varepsilon^4$，得到

$$
\boxed{\lambda(\widehat Q_4(S;\alpha,\beta))\ge0
\quad\forall S,\ \forall(\alpha,\beta)\in\mathbb R^2.}
\tag{20}
$$

反过来，在 $A_\lambda\equiv0$、$\lambda(H_1)=\lambda(H_2)\equiv0$ 的前提下，(20) 确实保证最高导数层的路径积分非负。这只是最高层 (9) 的结论，不支付 L₀、L₂、完整路径或闭锥正性。

## 8. 范围与后用接口

本稿可与 R127 联用：若真实闭成本锥仍为真子锥，则它存在一个杀掉已付 R 及 G 轨道、平移不变且单一整权的非零正泛函；该泛函还必须满足 (15)、(17)，以及在相应退化情况下的 (20)。

任一真实状态或真实水平路径使这些必要条件失败，就排除那个候选正泛函。模素数的非零评价没有实数符号，因此不能代替这里的 PSD 或非负判断。

引理 1、快速路径与去 T 全部保留实际正长度、末 frame、八矩、scalar 与共同右锚。位置位移不在单桥中指定；实际闭合的既有四块构造若需使用，仍必须保留其各自作用范围。本稿只处理 universal 第四成本锥，不产生闭嵌入曲面。

对任意预先固定的窄 I 或受限 scalar 盒，只有当本稿有限补偿族和测试路径都被证明在该域内可用时，才能在该受限成本集合上使用同样推论。不能把 universal 可达性默认为受限域内可达。

完整成本锥是否等于 U、实际半群是否有逆元、完整 P₀/ruling 是否可同付、有限等距族与宏观厚度指标仍未由这些必要门完成。
