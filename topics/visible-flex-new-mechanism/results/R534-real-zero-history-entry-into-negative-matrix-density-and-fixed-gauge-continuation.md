# R534：同一正交库从真实零历史进入负矩密度区及固定规范延续

日期：2026-11-16。**原式纸证与奇异参数的完整 ODE 缩放；没有执行积分、符号程序、数值射击、旧秩复算或新的科学任务。**

本文使用 [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md) 的同一个固定正交库，并从 [R530](R530-two-sided-complete-ruling-feedback-and-four-real-even-endpoint-moments.md) 的真实双边反馈出发。它不使用 R520/R531 的另一份母库，也不把任意指定的奇偶几何称为 ruling 已付。

新的实际结论是：从 $k=0$、真实 $A=T=0$、$w=0$ 的端口出发，取一个一次固定的合法第三 Gram，可构造一段全相位完整 $K=0$ 路径，使原密度
$$
\rho=M_{p_1}=k^2-kh(\omega-\omega_c)
$$
严格变负。其来源是一个完整、可统一估计的重缩放 ODE，而不是形式上写出 $\sin t$。负密度的严格局部极小点位于一个新的加速度可逆域；在同一 $\chi$、同一真实累计下，可以光滑切换到 $\rho$ 恒为该负数的实际延续。

同时，进入负区以前的**累计** $p_1$ 仍严格为正：
$$
\int_0^{s_\delta}\rho\,ds=\frac{\pi}{4}\delta^7+O(\delta^9)>0.
$$
负密度最小值只有
$$
-\frac{a_*^2\pi^2}{8H^2}\delta^{10}+O(\delta^{12}).
$$
所以本文没有构造 $M=0$，也没有声称一个任意长的负累计段已经存在。切换以后一般离开双边奇偶族，必须重新保全部八矩，而不能继续只算四个偶矩。

## 1. 同一个库、真零锚与一次固定 Gram

保持 R521/R530 的全部实际 profiles、正幅副本、物理位置、宽度、原右锚以及第二、第三 ruling。固定
$$
S_c=(H,0,\omega_c),\qquad H>0,
$$
在同一实际窗口内满足
$$
x+\omega_c>0,\qquad H^2(x+\omega_c)^2>1
\tag{1}
$$
并有共同严格余量。以 $y=x+\omega_c$ 记同一 profiles，不在途中移动它们。

写 $\eta=\omega-\omega_c$，以及
$$
d=h\eta-k,\qquad
\mathbf w_y(S)=\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right).
\tag{2}
$$
R530 的强合法域在 $S_c$ 邻域给
$$
c_h:=C_h(S_c)<0,\qquad c_k:=C_k(S_c)>0.
\tag{3}
$$
整个构造的 scalar 状态留在这个**预先固定**的小紧域中；$\delta\to0$ 不另移动窗口、缩 profile 宽度或改变其归一。

取一个与原形式等距展开参数无关的小参数 $\delta>0$，中心初值为
$$
h=H,\quad k=\eta=\gamma=0,\quad \upsilon=k_s=\delta^2,
\qquad A_+=A_-=T_+=T_-=0.
\tag{4}
$$
R530 的双边解在中心光滑；本稿主要使用其 $s\ge0$ 部分。因此(4)在这段的真实左起点就是 canonical 零历史，**不需要任何先前未付的零矩阵桥**。第二规范全程取 $w_\theta=0$。

固定一个 $a_*>0$。用同一个 Gram 右逆取
$$
\mathbf I_y(\phi_\theta,\chi_\theta^\delta)
=\sin^2\theta\,\nu^\delta,
$$
$$
\boxed{
\nu^\delta=
\left(
2H\{\mathcal F(S_c,0,\delta^2,0,0)+c_h a_*\},
\frac{2c_k}{\delta^2},0
\right).
}
\tag{5}
$$
$\mathcal F$ 是原完整 ruling 的无加速度、无 $\chi$ 部分。由 R530 中心两条方程，(5)准确给
$$
h_{ss}(0)=a_*,\qquad k_{ss}(0)=0.
\tag{6}
$$
$\nu^\delta_0$ 在 $\delta\to0$ 时有界；只有 $\nu^\delta_1$ 按显示的 $\delta^{-2}$ 增大。

对每个最终固定的正 $\delta$，$\chi^\delta$ 是一条有限、真紧、光滑、周期且保 seed 的原允许 profile。它在整段及后面的切换中固定一次。本文的统一估计不会假装 $\|\chi^\delta\|$ 或所有第四成本在 $\delta\to0$ 时有界：它们的幅度必须保留，原第四字段也不被删掉。

## 2. 两个原式结构：加速度带速度，完整无加速度项只有二次速度

为使奇异系数(5)可审计，先列出缩放实际用到的全部原结构。

### 2.1 原第三密度的完整导数权

R73 的第三演化仍是
$$
A_s=\Phi_{M_{\rm raw}},\qquad
T_s=-\Phi_{M_{\rm raw}}\circ A+\mathcal C_s.
\tag{7}
$$
原 R77(2)、R79(2)对**完整** $\mathcal C_s$ 给导数权一、三分解。展开其中的真实全导数后，$\mathcal C_s$ 只含：

1. 对 $(h_s,k_s)$ 线性的项；
2. 一个速度乘一个加速度的项；
3. 三次速度项。

几何系数是在固定 $h>0$ 紧域上的光滑有限原 profile 算子。特别不存在“一个加速度但没有任何速度因子”的项；它也没有被投到 $W$ 后删去。

这一点可直接从 R56 原场再核：速度为零时，局部 second 的非零分量在 $N$，$Y$ 及其 $x$ 导数在 $T/B$，而 $\nabla_sY$ 在 $N$。加速度只进入 second 分子的 $T/B$ 分量；$-\lambda P_s$ 和 $-\gamma B_s/h^2$ 又各有一个速度因子。因此原 $\ell_s-\Psi_s$ 的加速度项确须带速度。这里没有把真实 $P_s,B_s$ 略去。

### 2.2 不消第三累计的完整 ruling

采用 R482 **未消第三历史**的(23)(24)，在 $w=0$ 时，
$$
\mathscr K
=\mathcal R+\mathcal L(AD)-\mathcal E(AD,AD)
-4\mathcal E\{\phi,T(\phi;D)\}
-2\mathcal E(\phi,\chi^\delta).
\tag{8}
$$
原 $\mathcal L$ 对速度线性、对 $A$ 线性。将已经显示的两条加速度行从 $\mathcal R$ 中抽出后，其余准确为
$$
\mathcal R_0(S)+\mathcal R_2(S;\gamma,\upsilon),
\tag{9}
$$
其中 $\mathcal R_2$ 是速度的二次式，不含速度一次项，也不含更高速度次。

(9)可从 R482(22)(27)直接逐类看出：second 分子的 $N$ 分量不含速度，$T/B$ 分量对速度线性；其平方只有零次和二次。原 $Y$–局部 third 项及变化-profile chain 在抽出加速度后也只有零次与二次，后者所用 $M_{\rm raw}$ 本来至多速度二次。没有删除真实的 chain、$P_s$、$B_s$ 或任何右积分常数。

有限正交平均只是原四次输入上的线性运算，所以(7)–(9)在 R521 的整个库上仍准确成立。它们是以下统一估计的来源，而非新增 profile 数值观察。

## 3. 正反时的矩阵与第三状态如何缩放

设重缩放时间为
$$
s=\delta t,
$$
并写
$$
h=H+\delta^2J,\quad \gamma=\delta V,\qquad
k=\delta^3K,\quad\upsilon=\delta^2W,\qquad
\eta=\delta^3Z .
\tag{10}
$$
因而
$$
J_t=V,\quad K_t=W,\quad
Z_t=\frac{W}{2h},\quad
a=h_{ss}=V_t,\quad
b=k_{ss}=\delta W_t .
\tag{11}
$$
这里 $b$ 是实际 $k_{ss}$，不与第三 scalar profile 混用。

### 3.1 全八矩：四偶一阶、四奇四阶

用 R530 的固定 $y$ 坐标分解
$$
\mathsf m_+=E+O,\qquad
\mathsf m_-=-E+O,
$$
其中 $E\in E_{\rm e}$、$O\in E_{\rm o}$。由原反时号，
$$
E_s=M_{\rm e},\qquad O_s=M_{\rm o}.
$$
R73 的逐点八矩式在(10)上准确给
$$
M_{\rm e}=M_c+O(\delta^2),\qquad
M_{\rm o}=O(\delta^3),
\tag{12}
$$
其中 $M_c=M_{\rm raw}(S_c,0,0)$。例如奇槽中的 $k,\eta$ 都是 $O(\delta^3)$，而
$\gamma d_s=O(\delta)\,O(\delta^2)=O(\delta^3)$；没有遗漏 $r_0,s_1$ 的速度乘积项。

因此引入
$$
\boxed{E=\delta\widetilde E,\qquad
O=\delta^4\widetilde O.}
\tag{13}
$$
它们的 $t$ 导数在 $\delta=0$ 有光滑有限延拓。特别 $A$ 的偶部分一般是 $O(\delta)$，绝不可以把整个第二累计只记成 $O(\delta^4)$。

### 3.2 完整第三：均值二阶、两侧差三阶

置
$$
T_{\rm av}=\frac{T_++T_-}{2},\qquad
T_{\rm df}=\frac{T_+-T_-}{2}.
$$
R530 的真正反时演化给
$$
(T_{\rm av})_s
=-\Phi_{M_{\rm e}}\circ\Phi_E-\Phi_{M_{\rm o}}\circ\Phi_O
+\frac{\mathcal C_+-\mathcal C_-}{2},
$$
$$
(T_{\rm df})_s
=-\Phi_{M_{\rm e}}\circ\Phi_O-\Phi_{M_{\rm o}}\circ\Phi_E
+\frac{\mathcal C_++\mathcal C_-}{2}.
\tag{14}
$$
各式的有序复合均保持 R73 原槽次序。

在负半段，实际速度为 $(-\gamma,\upsilon)$，实际加速度为 $(a,-b)$。第2节给出如下全部最低阶表：
$$
\begin{array}{c|c|c}
\text{原速度／加速度单项}
&\text{在(10)(11)中的阶数}
&\text{交换两半的主符号}\\ \hline
\gamma&\delta&-\\
\upsilon&\delta^2&+\\
\gamma a&\delta&-\\
\upsilon a,\ \gamma b&\delta^2&+\\
\upsilon b&\delta^3&-\\
\gamma^3&\delta^3&-\\
\gamma^2\upsilon&\delta^4&+\\
\gamma\upsilon^2&\delta^5&-\\
\upsilon^3&\delta^6&+
\end{array}
\tag{15}
$$
两半几何系数之差为 $O(\delta^3)$，只增加更高阶项。故完整地有
$$
\mathcal C_+-\mathcal C_-=O(\delta),\qquad
\mathcal C_++\mathcal C_-=O(\delta^2).
$$
与(12)(13)代入(14)，可取
$$
\boxed{
T_{\rm av}=\delta^2\widetilde T_{\rm av},\qquad
T_{\rm df}=\delta^3\widetilde T_{\rm df}.
}
\tag{16}
$$
这两个 rescaled 状态的原 ODE 同样在 $\delta=0$ 光滑；没有让完整第三历史为零。

## 4. 奇异 Gram 提出以后，真正的极限是一个正弦弧

以下所有 $O(\delta^j)$ 都是在同一固定有限 profile 算子空间、固定有限 $t$ 区间及其紧状态盒中的统一估计。全部原系数由有限代数运算与同锚 profile 积分给出，所以它们可在该盒内逐项求导。没有对不同 $\delta$ 改母、改右锚或重新归一。

### 4.1 无规范项的均值与差

用(8)(9)、(13)(16)逐项得到
$$
\frac{\mathcal F_++\mathcal F_-}{2}
=\mathcal F_c+O(\delta^2),
\qquad
\frac{\mathcal F_+-\mathcal F_-}{2}
=O(\delta^3).
\tag{17}
$$
这里 $\mathcal F_c=\mathcal F(S_c,0,0,0,0)$。第二个估计的具体来源为：

- $\mathcal R_0$ 两侧状态差为 $O(\delta^3)$；
- 二次速度中的奇交叉 $\gamma\upsilon$ 是 $O(\delta^3)$；
- $\gamma A_{\rm e}$ 在两侧同号，$\upsilon A_{\rm e}$ 的差是 $O(\delta^3)$，$\gamma A_{\rm o}$ 只给 $O(\delta^5)$；
- $A$ 的平方差至多 $O(\delta^5)$；
- 真第三项的差为 $O(\delta^3)$，由(16)支付。

所以(17)没有把一个可能同阶的 $YC$ 或 history 项藏入“较小量”。

### 4.2 两条完整方程的和与差

两半
$$
d_\pm=\pm\delta^3(hZ-K).
$$
(5)的奇异项在完整 ruling 中就是
$$
-d_\pm\nu^\delta_1
=\mp2c_k\delta(hZ-K).
\tag{18}
$$
它必须显式保留；不能拿一个对固定 $\nu$ 的普通小速度估计来处理它。

令
$$
\bar C_\alpha=(C_\alpha(S_+)+C_\alpha(S_-))/2,\qquad
\Delta C_\alpha=(C_\alpha(S_+)-C_\alpha(S_-))/2.
$$
有
$$
\bar C_h=c_h+O(\delta^2),\quad
\bar C_k=c_k+O(\delta^2),\quad
\Delta C_h,\Delta C_k=O(\delta^3).
$$
将 R530 两条完整 $K=0$ 方程相加，并将差除以 $\delta$。以 $(a,B)$ 为未知，其中 $B=b/\delta=W_t$，其系数矩阵在 $\delta=0$ 是
$\operatorname{diag}(c_h,c_k)$。由(5)(17)(18)，解出的完整式为
$$
\boxed{
a=a_*+O(\delta^2),\qquad
B=2(HZ-K)+O(\delta^2).
}
\tag{19}
$$
所有 remainder 均是 rescaled 全状态的光滑函数。原大系数 $\delta^{-2}$ 已全部在(18)准确消掉；其余原右尾、矩阵和第三累计通过(13)(16)留在相应方程中。

### 4.3 统一存在及真实首零

在 $\delta=0$，(11)(19)的几何部分闭合为
$$
J_{tt}=a_*,\qquad
K_{tt}=2(HZ-K),\qquad Z_t=K_t/(2H),
$$
其初值为
$$
J(0)=J_t(0)=K(0)=Z(0)=0,\qquad K_t(0)=1 .
$$
故唯一解是
$$
\boxed{
J(t)=\frac{a_*t^2}{2},\qquad
K(t)=\sin t,\qquad Z(t)=\frac{\sin t}{2H}.
}
\tag{20}
$$
极限矩阵与第三变量的方程是这些几何量驱动的有限光滑积分方程；它们在任何固定有限 $t$ 区间上有限。因此先在例如 $0\le t\le\pi+1/4$ 的极限解周围选一个有限紧盒，普通 ODE 的参数连续依赖给：全部充分小、但严格正的 $\delta$ 都有同区间的真实解，并且
$$
h=H+\frac{a_*}{2}\delta^2t^2+O(\delta^4),\qquad
h_s=a_*\delta t+O(\delta^3),
$$
$$
k=\delta^3\sin t+O(\delta^5),\qquad
k_s=\delta^2\cos t+O(\delta^4).
\tag{21}
$$
相应 rescaled $C^r$ 估计对每个固定有限 $r$ 成立。该证明同时使真实 scalar 状态留在(1)的固定合法紧邻域内，不以形式解存在代替实际延拓。

由 $K_t(\pi)=-1$，真实首个正零满足
$$
t_\delta=\pi+O(\delta^2),\qquad
s_\delta=\delta t_\delta,\qquad
k(s_\delta)=0,
$$
$$
k>0\quad(0<s<s_\delta),\qquad
k_s(s_\delta)=-\delta^2+O(\delta^4)<0.
\tag{22}
$$
还由 $h_{ss}=a_*+O(\delta^2)>0$ 得
$h_s>0$ 在整个 $(0,s_\delta]$，不只是远离中心的一段估计。

## 5. 真水平 holonomy 给严格正的末 $\eta$

真实关系 $\eta_s=k_s/(2h)$ 准确积分为
$$
\eta(s)-\frac{k(s)}{2h(s)}
=\frac12\int_0^s\frac{k h_s}{h^2}\,d\sigma
=:\zeta(s).
\tag{23}
$$
左边的起点值为零。不能把右边的真实面积删成端点项。

(22)与 $h_s>0$ 给
$$
\zeta(s)>0\quad(0<s\le s_\delta).
$$
在真首零处，$k=0$，由(21)得到
$$
\boxed{
\eta(s_\delta)
=\frac{a_*\pi}{2H^2}\delta^5+O(\delta^7)>0.
}
\tag{24}
$$
这里使用的是
$\int_0^\pi t\sin t\,dt=\pi$，以及真实零点 $t_\delta$ 的光滑扰动；没有将 $k$ 在一个预定但不是真零的时刻强行设成零。

原矩密度因此是
$$
\boxed{
\rho=k^2-kh\eta=\frac{k^2}{2}-kh\zeta.
}
\tag{25}
$$
当 $s$ 从左侧充分接近 $s_\delta$ 时，$k>0$ 趋于零，而 $h\zeta$ 有严格正端值。于是 $\rho<0$，这已经是该**实际完整 $K=0$ 路径**上的严格结论。

## 6. 负极小值与仍为正的前缀累计

设
$$
Z_*=\frac{a_*\pi}{2H^2}>0.
$$
为准确定位小负区，必须围绕真实首零 $s_\delta$ 放大，令
$$
s=s_\delta-\delta^3\xi .
$$
对固定有限 $\xi\ge0$，(21)–(24)及实际首零的 Taylor 式给
$$
k(s)=\delta^5\xi+O(\delta^7),\qquad
h(s)=H+O(\delta^2),
$$
$$
\eta(s)=\delta^5\left(Z_*+\frac{\xi}{2H}\right)
+O(\delta^7).
$$
这些式子对 $\xi$ 的前两阶导数一致。因而
$$
\boxed{
\delta^{-10}\rho(s_\delta-\delta^3\xi)
=\frac{\xi^2}{2}-HZ_*\xi+O(\delta^2)
}
\tag{26}
$$
在该紧 $\xi$ 区间为 $C^2$ 一致式。

右边的二次式在 $\xi=HZ_*$ 有唯一非退化极小。IFT 给一个真实严格局部极小点 $s_m\in(0,s_\delta)$，并有
$$
\xi_m=HZ_*+O(\delta^2),\qquad \rho_s(s_m)=0,
$$
$$
\boxed{
\rho(s_m)=-P_\delta,\qquad
P_\delta=\frac{a_*^2\pi^2}{8H^2}\delta^{10}
+O(\delta^{12})>0.
}
\tag{27}
$$
同时 $\rho_{ss}(s_m)=\delta^4(1+O(\delta^2))>0$。

但在整个前缀上，(21)(23)(25)给
$$
\boxed{
\int_0^{s_\delta}\rho(s)\,ds
=\frac{\pi}{4}\delta^7+O(\delta^9)>0.
}
\tag{28}
$$
负区非常短且弱；(27)绝不能被误读成这个前缀的总 $p_1$ 已经为负。其他原矩也未清，例如
$$
\int_0^{s_\delta}M_{p_2}\,ds=-H\delta^4+O(\delta^6),
\qquad
\int_0^{s_\delta}M_{t_1}\,ds=-\frac{\pi}{8}\delta+O(\delta^3).
\tag{29}
$$
这里从中心只取正半段，不能用另一半的奇偶积分替代实际前缀账目。

## 7. 负极小点处有真正可用的第二输入坐标

以下回到 R521 的**原单条**完整反馈，不再要求未来路径与另一半保持奇偶。全程仍是同一库、同一 $\chi^\delta$、同一 $w=0$、同一实际累计，不在 $s_m$ 归零 $A,T$。

直接微分原密度 $\rho=k^2-kh\eta$，得
$$
\rho_s=-k\eta\,\gamma+
\left(\frac{3k}{2}-h\eta\right)\upsilon .
\tag{30}
$$
再微分，
$$
\boxed{
\rho_{ss}=-k\eta\,h_{ss}
+\left(\frac{3k}{2}-h\eta\right)k_{ss}
+\upsilon^2-\left(2\eta+\frac{k}{2h}\right)\gamma\upsilon .
}
\tag{31}
$$
令 $B=3k/2-h\eta$。在 $s_m$，有
$$
k>0,\quad \eta>0,\quad \gamma>0,\quad\upsilon<0.
$$
由 $\rho_s=0$ 得
$$
B\upsilon=k\eta\gamma>0,\qquad \boxed{B<0.}
\tag{32}
$$
因此完整 $K$ 与规定 $\rho_{ss}$ 的两行矩阵
$$
\begin{pmatrix}C_h&C_k\\-k\eta&B\end{pmatrix}
$$
具有
$$
\boxed{
\Delta_\rho=C_hB+C_k k\eta>0.
}
\tag{33}
$$
这是原同一点上的严格非退化，不依赖另一个 profile 库的 principal rank。

(33)也说明这个点位于
$k>0,\eta>0,h\eta>3k/2$ 的实际开域。对本次小参数，其行列式可以很小；本文没有假装它具有一个与 $\delta$ 无关的下界。对每个已经固定的 $\delta>0$，它在该真实点附近有严格正下界，足以作下一步有限局部控制。

## 8. 不改规范、不重置历史的平滑负常密度延续

在(33)的实际邻域内，可以把真实自由输入换为一个给定光滑函数 $u(s)=\rho_{ss}(s)$：联立原完整 $K=0$ 与(31)，准确求解 $h_{ss},k_{ss}$，并继续积分原水平、八矩与第三方程。

这里没有引入一个独立的 $\rho$ 状态来强迫回填。若预定函数 $\widehat\rho$ 与初始真实 $\rho,\rho_s$ 相同，并给控制 $u=\widehat\rho_{ss}$，则正式解满足
$(\rho-\widehat\rho)_{ss}=0$ 与两个零初值，所以
$\rho\equiv\widehat\rho$。

为使切换保全部 jets，先把原双边解在 $s_m$ 之后短暂继续，记其密度为 $\rho_{\rm old}$。取一个固定光滑 cutoff $0\le\vartheta\le1$，在 $0$ 附近为 $1$，在 $1$ 附近为 $0$。对一个足够短但正的实际长度 $\ell$ 定义
$$
\widehat\rho(s_m+t)
=-P_\delta+
\vartheta(t/\ell)\{\rho_{\rm old}(s_m+t)+P_\delta\},
\quad 0\le t\le\ell.
\tag{34}
$$
因为 $\rho_{\rm old}(s_m)=-P_\delta$、$\rho_{{\rm old},s}(s_m)=0$，括号为 $O(t^2)$。因此对固定 $\delta$，$\widehat\rho_{ss}$ 的大小可在 $\ell\to0$ 时统一有界；cutoff 的两次微分没有制造 $\ell^{-2}$ 的无界值。其更高导数可增大，但它们不进入有限状态 ODE 的点态向量场。

取 $\ell$ 足够小，普通受控 ODE 的存在与连续依赖使实际解留在(33)的开域内。初段 $\vartheta=1$，故与原解所有 jets 完全相同；末段 $\vartheta=0$，故
$$
\boxed{\rho=-P_\delta,\qquad \rho_s=0}
\tag{35}
$$
并且所有后续 $\rho$ 导数均为零。继续取 $u=0$，得到一个正长度的真实负常密度延续。所有连接均为 $C^\infty$，原 frame 和位置按同一几何 ODE 恢复。

在这条常密度支上，水平关系本身给
$$
\boxed{
h=C\,\frac{(k^2+P_\delta)^{3/4}}{k},\qquad
\eta=\frac{(k^2+P_\delta)^{1/4}}{C},
}
\tag{36}
$$
其中 $C>0$ 由实际切换后的状态确定。它是原同一路径上的恒等式，不能据此任意重新指定 $k(s)$。在 $k^2\le2P_\delta$ 的分支，
$$
h_k\le0,\qquad
C_k+C_hh_k\ge C_k>0,
$$
所以原完整 $K=0$ 对此曲线上的 $k_{ss}$ 仍是非退化的真实方程，全部 $A,T$ 继续按原历史演化。

对任何已实际存在的短后续时长 $\tau$，其 $p_1$ 增量准确为
$$
\Delta m_{p_1}=-P_\delta\,\tau<0.
\tag{37}
$$
这是真实正时间段的负矩增量，不是一个有符号“负路径”。但本文只支付局部存在时长；它没有证明(36)可无限延拓、保持有界，或有足够时长抵消(28)。末 scalar、速度、八矩、第三、frame、位置和完整第四成本均随 $\tau$ 真实变化，不作为免费端口。

## 9. 哪些闭合条件仍必须完整追踪

本稿的实际路径从(4)的零历史出发，$\chi^\delta$ 从(5)一次选定，切换(34)不改变它。全段原三矩、第三 ruling 与完整第四 $K=0$ 均由同一 R521 库和原反馈支付。

切换以后一般不再是 R530 的双边奇偶解，故原总矩目标必须恢复为全部八坐标。尤其不能把(29)中的非零 $p_2$ 或其他奇槽从实际账面删除。第三累计也未归零；原 $T_s=-\Phi_{M_{\rm raw}}\circ A+\mathcal C_s$ 始终从同一个起点积分。

大 Gram 的完整 third 场及第四 characteristic 累计可能在 $\delta\to0$ 时增大。本稿的统一性只用于证明实际短弧及(24)–(28)，不声称存在一个有界成本的零参数极限。对最终固定 $\delta$ 的全部原成本必须按完整式保存；不由 ruling 为零推出整个 period 为零。

下一项仍是实际全局问题：在同一固定规范下，延长或改变已经进入的负区，获得足以配平前缀的真实矩增量，并同时支付其余七矩、端 germs、pose、第三及第四完整 period。本文既没有把两个母库拼接，也没有借原 R70 的无 ruling 桥来跳过这个问题。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：逐点八矩、变化-profile chain、完整第三累计；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)(2)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)(2)：完整局部第三密度的权一／权三结构；本文只用其原式，不使用其中未受当前 ruling 限制的桥；
- [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) 未消历史的(22)–(24)、(27)–(33)：完整 $K$、速度与加速度来源；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)、[R530](R530-two-sided-complete-ruling-feedback-and-four-real-even-endpoint-moments.md)：同一实际正交库、双边真实 ODE、固定 Gram 与原两行符号。

全篇使用原完整方程及显示的缩放，不以数值图像、少数样值或候选路径替代真实 ODE 存在与符号结论。
