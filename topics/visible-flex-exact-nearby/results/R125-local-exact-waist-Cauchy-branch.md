# R125：固定目标的真实腰部 Cauchy 分支与准确度量传播

2026-11-13，newton_source。**已证明：某个统一正宽度的精确等距腰环带。**

R124 的腰二阶修正不是孤立的形式 jet：它属于一个真实局部 PDE 分支。
本篇给出显式曲率演化方程，逐项核对解析 Cauchy 定理的假设，并证明三个
度量约束准确传播。于是，对原证书的整个辅助参数区间，存在某个共同
$\varepsilon>0$ 上的 $C^2$ 精确等距嵌入腰环带，且局部修正满足
R123 所用的原诱导材料范数档 $(0.001,0.01,0.7)$。

**范围：**这里的 $\varepsilon$ 尚无可用数值下界；环带有边，未处理 turning roots、
正帽或固定握持区的全局拼接。依本课题 README，这仍只是局部中间进展。
后附浮点演化不是本定理的证明，也不把本定理的未知 $\varepsilon$ 认作0.05或0.1。

## 1. 对象和固定目标

令 $I=[\delta_* -10^{-9},\delta_*+10^{-9}]$，
$\delta_*=-7789843107295549/4611686018427387904$。
对每个 $\delta\in I$，$F^{\rm old}_\delta$ 是 R120/R124 中同一确切 affine R33 对象，
其目标从初始几何一次性定义为

$$
g_{0,\delta}=E_\delta(r)\,dr^2+a_\delta(r)^2\,d\theta^2,
\qquad E_\delta=\langle |\partial_rF^{\rm old}_\delta|^2\rangle.
\tag{125.1}
$$

在一次演化中，(125.1) 完全固定，不由更新后的嵌入重新取均值。
这里 $\delta$ 是证书的辅助定位参数；不同 $\delta$ 的 $g_{0,\delta}$ 可以不同。
本篇**不**把这条辅助参数分支称为完成标准要求的同一度量等距弯曲族。

暂时省去 $\delta$ 下标。取实际的第一个正径向共同 scalar germ

$$
0\le r\le h_*:=\frac{2609037194989121}{1152921504606846976}.
$$

仅对解析存在证明，把这一侧的实际多项式 germ 解析延拓到零附近；
不宣称所有径向样条跨 knot 解析。$a,E$ 在该 germ 中解析，原因是：
有限 scalar 样条 germ 是多项式，R33 切向场由有限角相位的正弦、余弦复合得到，
角 primitive 的非零频率除法和完整收敛级数保持局部解析，
$E$ 的整角平均同样解析。参数 $\delta$ 在这些表达式中也解析。
R120 的完整复邻域及 Fourier 余项入口可复核这些解析对象；此处不以有限 FFT
代替无限 primitive。

记固定目标曲率

$$
K_0(r)=-\frac{a''}{aE}+\frac{a'E'}{2aE^2}.
\tag{125.2}
$$

初始数据选为 R124 的真实数据

$$
F(0,\theta)=F^{\rm old}(0,\theta)=:F_0(\theta),\qquad
F_r(0,\theta)=\sqrt{E(0)}\,e_z.
\tag{125.3}
$$

这不是任意初值：$F_0$ 平面、闭合、准确常速 $|F_{0,\theta}|=a(0)$，
$a'(0)=E'(0)=0$，且 R124 已证明
$|F_{0,\theta\theta}|^2>0.1563674870$。

## 2. 显式真实曲率演化

设

$$
P=F_r,\quad T=F_\theta,\quad U=P_\theta,\quad Q=T_\theta,
\quad C=T\times P,\quad G=C\cdot C,
\quad m=C\cdot U,\quad n=C\cdot Q.
$$

全部点积均是欧氏点积；解析延拓时使用其双线性复化，而不是 Hermitian 点积。
定义 $p=P\cdot P$、$t=T\cdot T$、$v=P\cdot T$、
$d=E'/2$、$e=-P\cdot U$，以及

$$
\alpha=\frac{td-ve}{G},\qquad
\beta=\frac{pe-vd}{G},\qquad
\lambda=\frac{m^2+K_0G^2}{nG}.
$$

演化方程为

$$
\boxed{F_{rr}=\Phi(r,P,T,U,Q):=\alpha P+\beta T+\lambda C.}
\tag{125.4}
$$

只要 $G\ne0,n\ne0$，它完全显式。直接点乘得

$$
P\cdot\Phi=\frac{E'}2,\qquad
T\cdot\Phi=-P\cdot P_\theta,\qquad
(C\cdot\Phi)n-m^2=K_0G^2.
\tag{125.5}
$$

第三式是真实 Gauss 方程；没有替换成旧径向背景或理想反射算子。
特别没有约去或丢掉均值通道。

在初始腰上，$G=Ea^2>1.4$，而
$n^2=Ea^2|F_{0,\theta\theta}|^2>1.4(0.156)$，故 $|n|>0.46$。
这些是 R124 完整角/全参数界的保守推论，足以给统一非特征初始面。
因为初始 $U=0$、$E'=a'=0$，(125.4) 的初始加速度为

$$
F_{rr}(0,\theta)
=-\frac{a(0)a''(0)}{|F_{0,\theta\theta}|^2}F_{0,\theta\theta},
\tag{125.6}
$$

准确重现 R124 的二阶修正。

## 3. 局部解析分支存在且具有统一宽度

把未知量取为九维向量 $(F,P,T)$，将 (125.4) 写成一阶系统

$$
F_r=P,\qquad T_r=P_\theta,\qquad
P_r=\Phi(r,P,T,P_\theta,T_\theta).
\tag{125.7}
$$

右边对未知量及其**一阶**角导数解析；它没有二阶角导数或待解的径向导数。
初始 $T=F_{0,\theta}$。这是标准的解析一阶非特征 Cauchy 系统。
采用 Tsogtgerel Gantumur 的原讲义定理：

> T. Gantumur, *Math 580 Lecture Notes 2: The Cauchy–Kovalevskaya Theorem*,
> 2011-10-03，Theorem 18，pp.9–10；非零解析初值与拼接参见 Corollary 20，p.11。
> [作者的 McGill 讲义](https://www.math.mcgill.ca/gantumur/math580f11/downloads/notes2.pdf)。

其输入是形如 $U_r=\mathscr F(r,x,U,D_xU)$ 的解析右端及解析初值；
结论是唯一的局部解析解。任意非零初值可先从 $U$ 中减去该解析初值。
在本问题中取切向变量 $x=(\theta,\delta)$，允许右端不依赖 $\partial_\delta U$。
由此同一个定理同时给出对辅助参数的解析依赖，而不必在事后另猜连续性。

所有分母在紧集 $\{r=0\}\times S^1\times I$ 上一致非零，初始数据和系数
在其某个复邻域解析。逐点使用上述定理，以唯一性在相交角图和参数图上拼接，
再取有限覆盖，就存在共同 $\varepsilon_1>0$，使解在
$[0,\varepsilon_1)\times S^1\times I$ 上定义。缩小至 $\varepsilon_1<h_*$，
保证正侧始终使用实际已安装 germ，而不是其穿越其他 knot 的虚构延拓。
初值的周期性和四重/角反射对称，由方程的欧氏协变性与解析唯一性继承。

还要核对引入 $T$ 没有额外解：由 (125.7)

$$
\partial_r(T-\partial_\theta F)
=P_\theta-\partial_\theta P=0,
$$

且初值为零，故整个局部解满足 $T=F_\theta$。
因此得到的是一个真实嵌入映射的 PDE 解。

## 4. 三个度量分量准确传播

(125.5) 的第一式给

$$
\partial_r(|P|^2-E)=0,
$$

其初值为零，故 $g_{rr}=E$。
第二式与 $T_r=P_\theta$ 给

$$
\partial_r(P\cdot T)=\Phi\cdot T+P\cdot P_\theta=0,
$$

初值也为零，故 $g_{r\theta}=0$。
因而诱导度量必为

$$
g_F=E(r)\,dr^2+H(r,\theta)\,d\theta^2,
\qquad H=|T|^2>0.
$$

令 $u=\sqrt H>0$。因为 $E$ 与角无关，该度量的准确 Gauss 曲率为

$$
K_{g_F}=-\frac{u_{rr}}{Eu}+\frac{E'u_r}{2E^2u}.
\tag{125.8}
$$

这个公式即便 $u$ 依赖 $\theta$ 也成立：把 $ds=\sqrt E\,dr$ 后计算
$ds^2+u(s,\theta)^2d\theta^2$ 的连接形式，得到 $K=-u_{ss}/u$；
角导数不产生额外项，因为它与 $d\theta$ 的外积为零。

另一方面，(125.5) 的第三式及真实曲面的 Gauss 公式给 $K_{g_F}=K_0$。
所以对每个固定 $\theta$，

$$
u_{rr}-\frac{E'}{2E}u_r+EK_0u=0.
\tag{125.9}
$$

初值由 (125.3) 给 $u(0,\theta)=a(0)$、$u_r(0,\theta)=0=a'(0)$。
目标 $a$ 本身由 (125.2) 满足同一个标量线性 ODE。
线性 ODE 的唯一性因此给 $u(r,\theta)=a(r)$，即

$$
\boxed{g_F=g_0\quad\text{在整个已存在的局部正侧环带上准确成立}.}
\tag{125.10}
$$

这一步使用真实解的方程，没有使用有限 Fourier 网格上的离散 Leibniz 法则。

## 5. 反射、嵌入和原诱导范数预算

原目标按构造为偶函数。令 $Q_z=\operatorname{diag}(1,1,-1)$，定义负侧

$$
F(r,\theta)=Q_zF(-r,\theta),\qquad r<0.
\tag{125.11}
$$

初值 $F_0$ 水平、$F_r(0)$ 竖直、(125.6) 水平，故 (125.11) 在零处的
零、一、二阶径向及混合 jet 全部匹配。于是全环带至少为 $C^2$，且负侧
仍准确诱导同一偶目标度量。这没有假设原样条穿过腰或其他 knot 后整体解析。

腰曲线是简单闭曲线。可直接从 R33 的单位切向式验证：
$T_h/a=i\exp(i\theta+iB(\theta))$，其中 $B$ 周期；(125.3) 的非零曲率
意味着 $1+B_\theta$ 无零点，且其均值为一，因而处处为正。
切向角一周严格增加 $2\pi$，R33 §4 的投影极值论证给严格凸和简单性。

由于 $F_r(0)=\sqrt E e_z$ 与这条平面曲线横截，缩小共同宽度后是嵌入，
而不仅是浸入。具体地，在平面腰曲线的管状邻域取最近点角坐标 $\vartheta$；
映射 $(r,\theta)\mapsto(\vartheta(F_h(r,\theta)),F_z(r,\theta)/\sqrt{E(0)})$
在腰上的导数是恒等映射（适当交换坐标顺序）。对紧集 $S^1\times I$ 统一缩小
宽度，使其提升到角覆盖空间后的导数距恒等小于 $1/2$，便为双 Lipschitz；
周期性降回环带后仍单射。因此 $F$ 也是嵌入。

最后令 $V=F-F^{\rm old}$，所有导数范数使用**原诱导度量**
$\gamma_\delta=g_{F^{\rm old}_\delta}$。
R124 的全参数腰界为

$$
V=0,\qquad |dV|_\gamma<1.205161\,10^{-5},\qquad
|\nabla_\gamma^2V|_{\rm HS}<0.406443414.
$$

这些量对 $(r,\theta,\delta)$ 连续，腰上的界有严格余量。
由紧致性，可再次统一缩小为某个 $\varepsilon>0$，得到

$$
\boxed{\quad
\|V\|_{C^0}<0.001,\qquad
\|dV\|_{\gamma,C^0}<0.01,\qquad
\|\nabla_\gamma^2V\|_{{\rm HS},C^0}<0.7
\quad}\tag{125.12}
$$

在 $[-\varepsilon,\varepsilon]\times S^1\times I$ 同时成立。
参数到嵌入的映射在该固定紧环带的 $C^2$ 拓扑中连续。
这给出真实局部分支及所需的局部范数档，没有把连续性推论误说成某个
指定径向长度的数值证书。

## 6. 后续定量问题和数值证据的边界

`scripts/fourfold_phase_waist_cauchy_evolution_probe.py` 和
`scripts/fourfold_phase_waist_cauchy_evolution_geometry_probe.py`
实现了同一 (125.4) 的有限角网格浮点演化。其意义是选择可继续验证的实际候选。
相关报告及初步分辨率比较放在 `notes/2026-11-13-waist-cauchy-*`；
它们没有验证角无限尾、时间积分误差或整个辅助参数区间。
近零曲率残差有一部分由 RHS 构造强制，不能作为独立的误差证书。

要沿实际核心继续到 turning roots，仍须给这个新分支的定量连续延拓、
实际系数范围及边界/返回条件。旧候选的 R101/R111/低块或高频证书
不能未经真实系数比较直接转移到更新分支。
本篇不把任意局部等距环带封口成精确闭面，也不据此宣称完成可见弯曲族。
