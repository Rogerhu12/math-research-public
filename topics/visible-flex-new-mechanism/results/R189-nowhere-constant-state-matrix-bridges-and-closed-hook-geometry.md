# R189：无开常状态段的准确矩阵桥与闭合第三 hook 几何

日期：2026-11-15。**完整存在证明；没有新的控制拟合、几何积分或研究计算。** 复用 [R70 任意矩阵桥](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R73 点态八矩阵](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R71 真实第三交换子](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R72 frame 桥](R72-same-state-zero-second-third-arbitrary-frame-bridge.md) 与 [R180](R180-fixed-circle-invisible-third-hook-and-signed-fourth-period-gauge.md)。

本稿构造新的真实几何。它保留规定 frame/scalar 端点、完整矩阵及第三 hook，但没有任何正长度开区间使 $(k,h,\omega)$ 同时为常数。端点仍保留常态的全部 jets，所以有限拼接和真实倒行仍为 $C^\infty$。

这只移除 [R187 常状态段障碍](R187-narrow-derivative-packet-circle-constant-state-obstruction.md) 的一个前提，不证明第四 ruling 或 period 已可解。

## 1. 准确命题与端口约定

**桥命题。** 给定 R70 所允许的两个 frame、两个 scalar 常态端值及任意有限 $M_*\in\mathfrak{sl}_3(\mathbb R)$，存在有限长度的真实光滑桥，满足

$$F_s=F\Omega(k),\qquad h>0,\qquad \omega_s=\frac{k_s}{2h},$$

frame 和 scalar 端值准确匹配，矩阵积分准确为 $M_*$，并且：

1. 两端 $(k,h,\omega)$ 的全部正阶导数都为零；
2. 内部没有非空开区间使 $(k,h,\omega)$ 同时为常数。

这个桥可以在任何预先指定的有限阶 $C^m$ 精度下逼近所选的 R70 正则解。这里不要求保存原桥的空间位移，不把新桥当作原桥的重参数化。

“全部端 jets 等于常态”与“端点附近存在开常值 germ”在本稿中明确不同。后者被去掉，前者完整保留。

## 2. R70 解附近的八个正则矩阵参数

R70 以八个完整圆参数

$$p=(\alpha_1,\beta_1,\ldots,\alpha_4,\beta_4)$$

及固定的充分大有限整数 K 构造目标桥。其矩阵为

$$M(p)=K B(p)+C(p),$$

并在准确目标解 $p_*$ 处有

$$D_pM(p_*):\mathbb R^8\longrightarrow\mathfrak{sl}_3(\mathbb R)
\quad\text{可逆}. \tag{1}$$

这是 R70 的有限 IFT 本身给出的正则解：除以 K 后，其导数是 $DB+K^{-1}DC$，在所选大有限 K 下仍可逆。

该族的 frame 两端、scalar 两端及全部端 jets 对 p 都固定。每个完整圆按其真实周期走整数圈，连接按真实端数据光滑选择，所以 frame 匹配对邻近 p 准确成立，不只是导数层匹配。

把各条路径光滑拉到一个固定参数区间 $x\in[0,1]$，保留其真实长度及速度因子。可取全局 $x=s/L(p)$。记原数据为 $k_p(x),h_p(x)$；它们及移动分段位置按 p 光滑。因为原拼接有常值 germs，移动接点不会产生参数光滑性问题。常状态的有无不依赖这一正重参数化。

这条 R70 桥含从近 $k=1$ 到近 $k=-1$ 的连接，因此 $k_{p_*}'$ 不恒为零。选一个实 $\eta_\omega\in C_c^\infty(0,1)$，使

$$
c_\omega:=-\frac12\int_0^1
\frac{k_{p_*}'(x)\eta_\omega(x)}{h_{p_*}(x)^2}\,dx\ne0. \tag{2}
$$

例如在 $k_{p_*}'$ 符号固定的一个小区间内取非负 bump。这里不需要计算该积分的数值。

## 3. 自由 h 扰动与九参数准确补偿

令

$$
\mathcal X=\{\eta\in C^\infty([0,1]):
\eta^{(j)}(0)=\eta^{(j)}(1)=0\text{ 对所有 }j\ge0\}. \tag{3}
$$

这是闭 Fréchet 空间，因而是 Baire 空间。不是把 $C_c^\infty(0,1)$ 的并集误当作一个完备范数空间。

对小的 $\eta\in\mathcal X$ 和有限参数 $(p,\tau)$，定义

$$
\widehat h=h_p+\eta+\tau\eta_\omega,\qquad
\widehat k=k_p,
$$

$$
\widehat\omega(x)=\omega_0+
\int_0^x\frac{k_p'(t)}{2\widehat h(t)}\,dt. \tag{4}
$$

只在 $\widehat h$ 保持严格正的邻域中工作。frame 仍由原 $k_p$ 与原真实速度决定，所以对所有这些 h 扰动，其两个 frame 端点仍准确不变。全部 k、h 端 jets 仍固定；(4) 保证 omega 的全部正阶端 jets 为零。其末值暂时未固定，正由参数 $\tau$ 处理。

取 R73 的同一八维矩阵坐标，定义九个真实约束

$$
\mathcal F(p,\tau,\eta)
=\left(\widehat M-M_*,\ \widehat\omega(1)-\omega_1\right).
$$

在 $(p_*,0,0)$ 处，原 p 族已经保持 omega 终值，故

$$
D_{(p,\tau)}\mathcal F=
\begin{pmatrix}
D_pM & D_\tau\widehat M\\
0 & c_\omega
\end{pmatrix}, \tag{5}
$$

由 (1)、(2) 可逆。矩阵积分使用真实 $\widehat\omega$，并没有在 h 改动后继续偷用旧 omega。

这些约束只涉及有限阶几何 jets、正 h 的有理组合及真实有限积分，故在足够高的固定 $C^r$ 邻域中为光滑映射。带 Banach 参数的有限维 IFT 给

$$p=p(\eta),\qquad \tau=\tau(\eta), \tag{6}$$

使全部九个约束准确为零。将其限制到 (3) 中一个非空开邻域 $\mathcal U$，每个 $\eta\in\mathcal U$ 都给真正 $C^\infty$ 的桥。有限参数映射对 Fréchet 拓扑连续，且沿任何光滑有限方向可微。

这里可以固定 r 后再把 $\mathcal U$ 与任意给定有限阶 $C^m$ 小邻域相交。因此最终构造可以达到桥命题所述的任意有限阶逼近精度。辅助整数 K 在这一过程中保持固定。

## 4. 每个常状态坏集都闭且无内点

对有理端点 $0<a<b<1$，记 $J=[a,b]$，并定义

$$
\mathcal B_J=\{\eta\in\mathcal U:
\widehat k_\eta'\equiv0,\ \widehat h_\eta'\equiv0
\text{ 于 }J\}. \tag{7}
$$

因 (4)，这正是该区间上三个 scalar 状态都为常数的条件。由 $C^1$ 连续性，$\mathcal B_J$ 在 $\mathcal U$ 中闭。

现任取 $\eta_0\in\mathcal B_J$。在当前准确解处，先固定补偿参数，只改变自由扰动。对 $\psi\in C_c^\infty((a,b))$，其 omega 终值一阶变化为

$$
-\frac12\int_a^b
\frac{\widehat k_{\eta_0}'\psi}{\widehat h_{\eta_0}^2}=0. \tag{8}
$$

八个矩阵一阶变化是该无限维 bump 空间上的八个连续线性泛函。因此可以选择非零 $\psi$，使这八个变化也都为零。例如从九个互不交的小 bump 的线性组合中取一个非零核向量即可。

对曲线 $\eta(t)=\eta_0+t\psi$，(5)、(6) 和全部九个自由一阶变化为零给

$$p'(0)=0,\qquad \tau'(0)=0.$$

所以真实 h 的一阶变化恰为 $\psi$，真实 k 的一阶变化为零。非零紧支撑 $\psi$ 的导数不恒为零，选一点 $x_0\in(a,b)$ 使 $\psi'(x_0)\ne0$，则

$$
\widehat h_{\eta(t)}'(x_0)
=t\psi'(x_0)+o(t)\ne0
$$

对充分小的非零 t 成立。因此任意 $\eta_0$ 的邻域都含不属于 $\mathcal B_J$ 的准确解，$\mathcal B_J$ 无内点。

有理区间可数。Baire 定理给稠密集合

$$
\mathcal U\setminus\bigcup_J\mathcal B_J. \tag{9}
$$

其中任一解都没有开常状态段：若有一个非空开常状态区间，它包含一个有理闭子区间，就会落入某个 (7)。这完成桥命题。

这个论证保留了实际全矩阵与 omega 终值，不是先任意扰动后把残差称为小。扰动还可能改变真实中心线位移，下一节使用新路径的实际位移闭合。

## 5. 端点 jets 足以保留真实组合与倒行

R71 的真实 composition 来自共同右锚及前段 scalar 历史的传递：

$$
T_{21}(a;b,c)=T_1(a;b,c)+T_2(a;b,c)
-\Phi_{M_2}(a,\Phi_{M_1}(b,c)).
\tag{10}
$$

该恒等式不需要在接点附近留一段正长度常状态；需要的是所有场与几何系数平滑相接，以及同一个真实锚。全端 jets 相同正保证这两点。原矩阵分部积分的端项也由全平 jets 准确消去。

对首末 scalar 状态相同、frame $I\to A$ 的路径，真实倒行仍为

$$
F^{\rm rev}(s)=D A^TF(L-s)D,\qquad
D=\operatorname{diag}(-1,1,-1),
$$

$$
k^{\rm rev}(s)=k(L-s),\quad
h^{\rm rev}(s)=h(L-s),\quad
\omega^{\rm rev}(s)=\omega(L-s).
\tag{11}
$$

其 frame 为 $I\to DA^TD$，真实位移和中心线按同一反射、平移处理。式 (11) 逐点满足 frame 与 omega 方程；端 jets 的平坦性在倒行下保持。M=0 时，同右锚的第二恢复仍倒行偶，第三算子仍倒行取负。因此 R72 的 $M=T=0$ 任意 frame 桥也可用本稿的无开常段 M=0 桥重新构造。

有限拼接、ambient 左旋以及真实倒行都不会产生新的开常状态段：一个穿过接点的开区间仍含某条子路径内部的开区间。接点本身即使全平，也不是正长度的常状态段。

## 6. 固定有限第三 hook 的准确实现

这里只需固定有限条路径，不声称已构造对所有未指定参数同时无常段的无穷族。

例如给定固定有限 t 及两个矩阵 P、Q，用桥命题分别构造同 scalar、frame I 端口的四条路径

$$
A_+:\ M=tP,\quad A_-:\ M=-tP,\quad
B:\ M=Q,\quad C:\ M=-Q.
$$

每条都没有开常状态段。定义

$$
W_+=A_+BA_-C,\qquad W_-=A_-BA_+C.
$$

两词的路径自身第三成本之和完全相同；(10) 的交叉项之差正是

$$
T_{W_+}-T_{W_-}=2t[P,Q].
$$

两词本身 M=0，故接上 $W_-$ 的真实倒行得到准确 $M=0$、$T=2t[P,Q]$ 的有限环。这里不要求独立选择的 $A_+,A_-$ 来自一个已证明的全 t 光滑族；同两条固定路径在两个词中交换位置已经足够。

取 R81 的

$$
\mathfrak H=[P,S]-3[P,R],
$$

并使用有限条这样的词，就得到同端口、frame I、M=0、$T=\kappa\mathfrak H$ 的无开常段真实环，其中 $\kappa\ne0$ 是任意预先固定的有限实数。

## 7. 无开常段的闭 hook 几何与 R183 圆

再用 §5 的 $M=T=0$ frame 桥得到 R180 的两个 Klein 元素

$$g_1=\operatorname{diag}(1,-1,-1),\qquad
g_2=\operatorname{diag}(-1,1,-1).$$

把 hook 环接入第一种路径，按 R180 的 Klein 八边词组装。每种路径的实际新位移分别在四个左旋位置出现，且

$$I+g_1+g_2+g_1g_2=0.$$

因此真实中心线位移准确闭合，frame 和 scalar 全 jets 也闭合。先把环的 hook 幅度取为最终所需幅度的四分之一，就得到

$$
M=0,\qquad T=\kappa\mathfrak H\ne0
$$

的有限光滑闭浸入带，而且没有任何开常状态段。

有限构造完成后选择共同物理区间 I，使全路径 $h>0,\xi+\omega>0$。所有正上下界都有限；不声称 I 可以预先任意指定，也不约束空间位移、长度或 reach。

R183 的完整二、三阶证明只使用变量几何的真实 range、三矩平衡、导数分包的 hook 消去及八包有限差分，没有用常段。因此可在这条新几何上选同类真正重叠三矩圆，完整满足二、三阶 range，并保留 R180–R185 的周期 gauge 与六矩右逆。

## 8. 仍未支付的真实目标

R187 依赖一个非空开常状态段，在该段提取准确的空间 $\sigma^2$ 系数。本稿的新几何没有这种区间，所以不能直接使用该提取论证。这不表示原第四障碍已经被扰动消失，更不表示附近常段的误差很小就能解整个 range。

新几何的 canonical $V^0_\theta$ 和 $K^0_\theta$ 都会真实改变。接下来仍须在同一冻结几何、同一圆和同一锚下检验 R184 的完整周期方程与 ruling 商方程。R181 的退化 ODE、固定圆通量不变量及全部低阶合法性继续适用。

本稿给的是准确有限路径的存在与低阶相容构造，不是其数值实例，也不是第四形式校正、收敛的等距族、嵌入或厚度结论。

