# R87：完整高模两jet的 common-cut 预算及固定 g 的度量转移

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已证明的条件预算。** 本文对实际 Hermite 接合给显式位置、一阶、
二阶界，并在同一个固定目标度量的正交帧中控制 Gram 矩阵。
完整保留 warp 的 $\rho$ 与平流项；不从低模 DN 通过推断高模接缝已小。
本文没有新 DN/BVP 或数值候选，也没有新增完成门。

## 1. 输入和完整 Hermite 修正

在一个固定径向区间 $[s_0,s_1]$ 上，记 $\ell=s_1-s_0>0$、
$t=(s-s_0)/\ell$。令 $D_0(\psi),D_1(\psi),D_2(\psi)$ 为期望终端
Cartesian 位置、$s$ 一阶、$s$ 二阶 jet 与原 prefix jet 的差。
它们包括所有角模式、三个 Cartesian 分量以及均值。
为讨论全部二阶界，可取有限 Fourier 数据，或一般 $C^2$ 角函数；
这只是本有限接合的数据类别，不给原问题增加全局 $C^3$ 条件。

定义
$$
\begin{aligned}
\phi_0(t)&=10t^3-15t^4+6t^5,\\
\phi_1(t)&=-4t^3+7t^4-3t^5,\\
\phi_2(t)&=\tfrac12t^3-t^4+\tfrac12t^5,
\end{aligned}
\qquad
C(s,\psi)=\phi_0D_0+\ell\phi_1D_1+\ell^2\phi_2D_2.
\tag{1}
$$
在左端，$C,C_s,C_{ss}$ 为零；在右端，分别为 $D_0,D_1,D_2$。
因此 $F+C$ 与所用真实终端数据接到全部两jet，包括由角求导决定的混合
和角 jet。向左补为零是 $C^2$ 的。证明只需对(1)求导并代入 $t=0,1$。
全局嵌入、metric 和 reach 不由这个插值事实自动得到。

## 2. 三个 Hermite 基的准确常数

令范数取 $0\le t\le1$ 上的绝对最大值。下表是准确值：

| 基函数 | $\|\phi_j\|_\infty$ | $\|\phi_j'\|_\infty$ | $\|\phi_j''\|_\infty$ |
| --- | ---: | ---: | ---: |
| $\phi_0$ | $1$ | $15/8$ | $10\sqrt3/3<6$ |
| $\phi_1$ | $16/81$ | $1$ | $(224+152\sqrt{19})/225<4$ |
| $\phi_2$ | $54/3125$ | $(9+24\sqrt6)/1000<17/250$ | $1$ |

**证明。** $\phi_0'=30t^2(1-t)^2\ge0$，其最大值在 $t=1/2$。
$\phi_0''=60t(1-t)(1-2t)$ 的极值在
$t=(3\pm\sqrt3)/6$，绝对值为 $10\sqrt3/3$。

$\phi_1=-t^3(1-t)(4-3t)\le0$；其内极小值在 $t=2/3$，为
$-16/81$。$\phi_1'=t^2(-12+28t-15t^2)$ 的内极小值在 $t=2/5$，
为 $-64/125$，端点最大值为1。$\phi_1''=-24t+84t^2-60t^3$
的两个内极值在 $t=(7\pm\sqrt{19})/15$，值为
$(224\pm152\sqrt{19})/225$；比较这些值与端点0即得表中范数及小于4。

$\phi_2=\tfrac12t^3(1-t)^2\ge0$，最大值在 $t=3/5$，为 $54/3125$。
$\phi_2'=\tfrac12t^2(1-t)(3-5t)$ 的两个内极值在
$t=(6\pm\sqrt6)/10$，分别为
$(24\sqrt6-9)/1000$ 和 $-(24\sqrt6+9)/1000$。
因为 $\sqrt6<59/24$，后者绝对值小于 $68/1000=17/250$。
最后 $\phi_2''=3t-12t^2+10t^3$ 的内极值为
$(3\sqrt6-2)/25$ 和 $-(3\sqrt6+2)/25$，端点值为0、1；故范数为1。
全部常数由有限多项式求导得到。证毕。

## 3. 直接可计算的完整 Fourier jet 预算

写真实 Cartesian Fourier 展开
$$
D_j(\psi)=\sum_{k\in\mathbb Z}d_{jk}e^{ik\psi},\qquad
d_{j,-k}=\overline{d_{jk}},
$$
并置
$$
U_j=\sum_k\|d_{jk}\|_2,\quad
V_j=\sum_k|k|\|d_{jk}\|_2,\quad
W_j=\sum_k k^2\|d_{jk}\|_2.
\tag{2}
$$
有限模式时这些是有限和；若使用无限输出，必须另给对应加权余项。
区间系数可逐件用向上范数界替代，所有以下不等式仍成立。

对任意非负三元组 $x=(x_0,x_1,x_2)$，定义
$$
\begin{aligned}
L_0(x)&=x_0+\frac{16}{81}\ell x_1+
\frac{54}{3125}\ell^2x_2,\\
L_1(x)&=\frac{15}{8\ell}x_0+x_1+
\frac{17}{250}\ell x_2,\\
L_2(x)&=\frac6{\ell^2}x_0+\frac4\ell x_1+x_2.
\end{aligned}
\tag{3}
$$
由第2节、逐项角求导及三角不等式，整块上有
$$
\begin{array}{lll}
\|C\|_\infty\le L_0(U),&
\|C_s\|_\infty\le L_1(U),&
\|C_{ss}\|_\infty\le L_2(U),\\
\|C_\psi\|_\infty\le L_0(V),&
\|C_{s\psi}\|_\infty\le L_1(V),&
\|C_{\psi\psi}\|_\infty\le L_0(W).
\end{array}
\tag{4}
$$
这是所有模式及均值的预算。均值进入 $U_j$，但不进入 $V_j,W_j$；
不能连它对径向导数的影响也删除。

如果数据采用当前圆柱向量基，必须先转成真正的 Cartesian 频率，或给
相应保守加权界。水平 $\cos(3j\psi)e_r(\psi)$、
$\sin(3j\psi)e_\theta(\psi)$ 产生频率 $1\pm3j$，不是只有 $3j$；
径向常数项 $e_r(\psi)$ 仍有频率1。竖直项的频率是 $3j$。
式(2)因此保留 R82 所指出的旋转基导数。

## 4. 转到同一个固定目标 g 的正交帧

在用来写(1)的同一参数中，允许目标写成
$$
g=\nu(s)^2ds^2+a(s)^2du^2,
\qquad u=\Theta(s,\psi),\quad \rho=\Theta_\psi>0,
\quad b=\Theta_s/\rho.
\tag{5}
$$
这里 $\nu>0$ 容纳真实桥/域重标量；若该参数已经是最终目标弧长，则
$\nu=1$。本节不把另一张图或另一参数的 $\lambda$ 代入当前目标。
实际正交帧为
$$
e_1=\nu^{-1}(\partial_s-b\partial_\psi),\qquad
e_2=(a\rho)^{-1}\partial_\psi.
\tag{6}
$$
假设整个修正支持上已知
$\nu\ge\nu_*>0$、$a\rho\ge A_*>0$、$|b|\le B_*$。
由(4)得到
$$
\|dC(e_1)\|\le
\varepsilon_1:=\frac{L_1(U)+B_*L_0(V)}{\nu_*},
\qquad
\|dC(e_2)\|\le\varepsilon_2:=\frac{L_0(V)}{A_*}.
\tag{7}
$$
于是 $\|dC\|_{g\to\mathbb R^3}\le
\varepsilon:=(\varepsilon_1^2+\varepsilon_2^2)^{1/2}$。
这保留了完整平流项及分母 $\rho$，不忽略目标的坐标交叉项。

当前 chart 的实际源码 `950f-prefix-adaptive-chart-bvp-v2.py::Flow.geo`
在 $s/s_{\rm end}=3/4$ **开始**衰减 warp：其因子为
$1-S(4s/s_{\rm end}-3)$，其中 $S(v)=10v^3-15v^4+6v^5$，自变量截在
$[0,1]$。它只在 $s=s_{\rm end}$ 达到零两jet，末四分之一的内部一般
仍非零。因此当前 common-cut 支持不能因位于该末段就简化成
$\rho=1,b=0$，应使用(7)的真实界。只有另已证明整块角图确实恒等时
才可这样简化。若域重标量使 $\nu\ne1$，也须保留当前 bridge 的真实
下界。已有代码的参数名不能代替这些坐标关系。

**固定 g 的 Gram 转移定理。** 若基图 $F$ 在这一块相对同一个最终
目标 $g$ 已满足
$$
\|g^{-1/2}(F^*\langle\cdot,\cdot\rangle-g)g^{-1/2}\|_{\rm op}
\le\eta,
\tag{8}
$$
则加上完整修正 $C$ 后，同一相对误差至多
$$
\boxed{\eta+2\varepsilon\sqrt{1+\eta}+\varepsilon^2.}
\tag{9}
$$
**证明。** 在正交帧(6)中，令 $A$ 的两列为 $dF(e_i)$，$B$ 的两列为
$dC(e_i)$。由(8)，$\|A\|\le\sqrt{1+\eta}$；由(7)，
$\|B\|\le\|B\|_{\rm Frobenius}\le\varepsilon$。准确展开
$$
(A+B)^T(A+B)-I=(A^TA-I)+A^TB+B^TA+B^TB
$$
并用算子范数乘法即得(9)。若同时 $\eta<1$ 且
$\varepsilon<\sqrt{1-\eta}$，最小奇异值至少为
$\sqrt{1-\eta}-\varepsilon>0$，故仍为浸入。这个局部结论不是全局
嵌入或 reach 结论。证毕。

(8)若只相对中间 frozen target 成立，不能直接称为最终同 $g$ 的界；
应先用该新图自己的 bridge/目标转移，或在其已知误差中完整计入目标差。
二阶表(4)可以供后续曲率/reach 检查使用，但本文不从小的一阶范数预支
reach。若整族数据在参数上连续、界统一，以上结论也对全部参数统一。

## 5. 真实高 W 输出应如何形成 D0/D1/D2

分开 prefix $M$ 与尾 $W$ 时，低模边界只使用 $P S_W(\iota H)$。
以下完整字段仍须由这次真实 W 输出提供，不能用该低模 view 替代：

1. **Prefix 完整端 jet。** 当前 prefix/shared-jet 的位置、一阶、二阶，
   包括准确均值积分；展开到共同全模基。现 common-cut 的来源为
   `raw['jets'][:,-1,:]` 与 `mean_increments`。
2. **尾完整 Cartesian 端 jet。** 由这次导出的 `IntegratedTail` 的真实
   位置积分端值，以及全部 `first[-1]`、`second[-1]`。保留全部
   `planar_modes`、`height_modes`、两个均值及背景项。形式高度
   `jets.height/slope/second` 是必要信息，但依 R85 不能自动替代
   实际 XYZ 表示的导数。
3. **这次桥和配准。** 实际 cut radius、background slope/second、
   $E,E'$、反射、均值高度配准与本图 `arclength_rescale`。按原程序先
   配准完整尾，再作
   $J_0=X$、$J_1=(k/\lambda)X_r$、
   $J_2=(k^2X_{rr}+k_2X_r)/\lambda^2$，其中
   $k=-1/\sqrt E$、$k_2=-E'/(2E^2)$，最后减去完整 prefix jets。

现 `78718-prefix-common-cut-storage-v1.py` 的 `cut_delta` 正是按这些
步骤形成的全部三层差；其共同基已经按真实最高 planar/height 模式扩展，
不能改成只看 $\max(M,W)$。从这一完整 `cut_delta` 转出(2)即可应用
(3)–(9)。高输入高度为零不意味着高坡度、二阶或水平 Cartesian 差为零。
如果边界值和输出含有区间误差，这些误差也进入同一 $D_j$ 包围。
实际 $\ell$ 取 mesh 终点减去 `correction_start_index` 对应节点；现
`searchsorted(end-width)` 选的是该位置之后的节点，因此实际宽度不大于
requested width，通常不恰好等于十进0.15。径向导数预算须用实际 $\ell$。

## 6. 固定宽度下一个可用的高模量级公式

下面只是明确的条件算式，**不是当前 W22 数据已经满足的断言**。
假设某一已分离出的修正只有竖直频率 $|k|\le66$，且它的 $D_0=0$；
另外已证明本窗口 $\nu=\rho=1,b=0,a\ge3/5,\ell=3/20$。
则 $V_j\le66U_j$，(7)给
$$
\varepsilon_1\le U_1+\frac{51}{5000}U_2,
\qquad
\varepsilon_2\le\frac{88}{27}U_1+\frac{2673}{62500}U_2.
\tag{10}
$$
两维向量的三角不等式及直接有理平方比较
$$
1+(88/27)^2<(7/2)^2,\qquad
(51/5000)^2+(2673/62500)^2<(11/250)^2
$$
进一步给简洁预算
$$
\varepsilon<\frac72U_1+\frac{11}{250}U_2
\tag{11}
$$
（右侧为零时取非严格等号）。这是固定宽度下高坡度与二阶的不同实际
影响，不能只用高度大小判断。

例如在上述条件下，$U_1\le10^{-10},U_2\le10^{-8}$ 给
$\varepsilon\le7.9\cdot10^{-10}$。只有该块自身的基图误差、其它模式、
水平位置差、均值差等也都计入后，才能用(9)与原 $2\cdot10^{-9}$ 门比较。
真实高 W 的完整 $D_0$ 通常不能因高非均值高度请求为零就设成零，所以
整体接缝应使用第3–5节的一般式。

这组公式不要求加大 prefix 模数，也不保证分离 M/W 后可通过。
它把实际高 W 数据到来后的接缝代价化成直接的完整 jet 计算，保留原
物理度量、原窗口与原完成标准。

