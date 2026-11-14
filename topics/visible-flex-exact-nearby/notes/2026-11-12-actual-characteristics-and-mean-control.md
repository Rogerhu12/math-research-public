# 实际特征类型、GC 对称性及均值控制

2026-11-12，constructive-route。

**状态。** 第 1 节是实际样条的浮点诊断，不能作连续证书；
第 2–4 节是完整推导的结构和参数选择接口；尚未证明当前候选满足
其中完整返回映射或约束横截的定量输入。第 5 节说明 GC 加两种反射
本身不足以强迫固定双曲切口返回图有光滑正密度；它不是闭面不可能性。

## 1. 必须先从同一实际二 jet 确定类型

记实际第二基本形式系数为
$L=n\cdot F_{xx}$、$M=n\cdot F_{x\theta}$、$N=n\cdot F_{\theta\theta}$，
并始终使用同一个样条的导数；$n=(F_\theta\times F_x)/
|F_\theta\times F_x|$。下面没有用角平均度量的 Gaussian 曲率代换它们。

旧 fourfold_mu4_weighted_radius_m16_checkpoint.npz，物理幅度 .06，
128 个角点、半周期 $[0,\pi/2)$ 上的实际采样为：

| $x$ | $\det\mathrm{II}$ 最小/最大 | $N$ 最小/最大 |
|---|---|---|
| 0 | $-1.594415,\ 0.294785$ | $-8.100210,\ 0.0456012$ |
| .03 | $-2.386697,\ 0.948511$ | $-7.705718,\ 0.157942$ |

所以旧候选在腰部已经有真实角向类型混杂和 $N$ 变号。
不能把它当作参考径向势的“同一个双曲核心、两个简单转折”。
小的度量 $C^0$ 残差并不控制其二阶导数，因此也不控制实际曲率类型。

新 fourfold_overcollocation_m16n101_waist006_checkpoint.npz，
SHA256 598fc957bcc8cd2aa958da3bc2f69d779fd055f7ee9fce39d968d33e4ff306d6，
固定的是实际 $U_4(0)=.06$。256 角点、$x$ 步长 .01 的初次采样为：

| $x$ | $\det\mathrm{II}$ 最小/最大 | $N$ 最小/最大 |
|---|---|---|
| 0 | $-1.52429357,\ -.801508317$ | $-6.19449413,\ -.382977750$ |
| .20 | $-.517254106,\ -.201279431$ | $-2.88454997,\ -.368191999$ |
| .23 | $-.149679597,\ -.0170643682$ | $-2.3931461,\ -.424019617$ |
| .24 | $.00730666831,\ .141182760$ | $-2.27247632,\ -.473738169$ |

在这批点上，$0\le x\le.23$ 全角严格双曲，$N<0$；$x=.24$ 全角
已转椭圆，且 $N$ 在 $[0,.6]$ 全部采样处仍负。
新候选的类型比旧图明显规整，但这些是采样，不证明转折图的单根性。

可重用入口为 scripts/fourfold_characteristic_diagnostic.py。
它先重建真实样条并读取二 jet，再扫描 $\det\mathrm{II},N$；
可选的 ray 部分只计算固定内部切口的返回与实际均值灵敏度。
**该固定切口返回没有包含转折反射、椭圆帽或真实无限尾，不是 PDE
外部边界图，也不是完整返回映射的旋转数证书。**

## 2. 从实际均值场到特征速度的准确微分

以下不假设当前图已精确等距。对任意变分场 $V$，令
$b_i=n\cdot V_i$，使用实际诱导度量 $g_{ij}=F_i\cdot F_j$。微分
$n\cdot F_i=0$ 和 $n\cdot n=1$，准确得到
$$
\dot n=-g^{ij}b_iF_j,\qquad
\dot h_{ij}=n\cdot V_{ij}+\dot n\cdot F_{ij}
           =n\cdot(V_{ij}-\Gamma^k_{ij}V_k).                 \tag{2.1}
$$
这是实际 $F$ 的几何微分，没有借用参考法向。

对保反射均值场 $V=A(x)e_r+C(x)e_z$，同一圆柱正交标架中的五个导数是
$$
V_x=(A',0,C'),\quad V_\theta=(0,A,0),\quad
V_{xx}=(A'',0,C''),\quad V_{x\theta}=(0,A',0),\quad
V_{\theta\theta}=(-A,0,0).                                  \tag{2.2}
$$
在实际双曲区 $Q=\sqrt{M^2-LN}>0$、$N\ne0$，特征速度及其微分为
$$
c_\pm=\frac{-M\pm Q}{N},\qquad
\dot Q=\frac{2M\dot M-N\dot L-L\dot N}{2Q},
$$
$$
\boxed{\dot c_\pm=\frac{-\dot M\pm\dot Q}{N}
                       -c_\pm\frac{\dot N}{N}.}             \tag{2.3}
$$
结合 R29 (5.3)、(5.4)，这就是实际均值方向到固定切口返回图的准确
线性算子。它含真实 $A'',C''$，不是一个径向 action 积分。
若变分支撑离真实转折图有正距离，该变分不会直接改变转折处 jets；
若转折图也移动，则必须继续补上相应端点和转折传输变化。

保存非均值系数不动而改变均值时，$U_4(0)$ 以及 R18 的
$2\sum_{j\ {\rm odd}}U_j(0)$ 都准确不变。这一事实可以保振幅规范，
但它不保证整个非线性度量方程继续成立。沿真正解流形的参数导数
还必须包含为恢复方程而加入的非均值修正。

## 3. 约束保持的真实 Schur 方向

设实际有限个几何或核约束为
$C(\tau,\beta)=0$，其中 $\beta\in\mathbb R^k$，且在实际候选/解上
$B=\partial_\beta C$ 可逆。有限维隐函数定理给
$$\beta'(0)=-B^{-1}\partial_\tau C.$$
因此沿这条约束曲线，实际返回映射的导数恰为
$$
\boxed{
\dot R_C(\theta)=\partial_\tau R(\theta)
 -\partial_\beta R(\theta)B^{-1}\partial_\tau C.}             \tag{3.1}
$$
若需要同时保第四模非齐次兼容和振幅，必须让 $C$ 包含这两个实际约束。
若振幅已由线性消元固定，则该行已自动支付，不应重复加入一个伪独立列。
未求出真实非径向伴随核时，不能把径向 $y_4$ 的投影称为已经得到的
实际核约束；有限矩阵 Schur 值也不能代替全频输入。

可验证的正向目标是使 (3.1) 在全部角度上一致为正。
这比仅检查一个平均积分更强，却可以直接通过 (2.1)–(2.3) 和流微分
求出需要认证的连续函数；若成功，将给下一节不依赖旋转数可微性的
参数选择办法。

## 4. 不把 action 导数冒称旋转数导数的参数选择

### 4.1 真正可微共轭族的导数公式

若已知实际升举 $R_\tau$ 有可微族 $h_\tau$ 满足
$$h_\tau\circ R_\tau=h_\tau+\omega_\tau,\qquad
h_\tau(\theta+2\pi)=h_\tau(\theta)+2\pi,$$
则其不变概率密度是 $h_\tau'/(2\pi)$，且
$$
\boxed{\dot\omega=
\frac1{2\pi}\int_0^{2\pi}
h'(R(\theta))\,\dot R(\theta)\,h'(\theta)\,d\theta.}          \tag{4.1}
$$
证明：微分共轭式，按该不变密度积分；
$\dot h\circ R-\dot h$ 的积分为零。
这里的 $\dot R$ 必须是实际约束曲线上的 (3.1)，不是径向作用量导数。
若尚未得到共轭及其参数可微性，就不能直接使用 (4.1)。

### 4.2 一个完全避开旋转数可微性的覆盖命题

设 $R_\tau$ 为连续的保向圆微分同胚族，$\tau\in[-a,a]$，
升举选择连续。假设参考图 $R_*$ 有真实共轭
$h\circ R_*=h+\omega_*$，其中 $h'\ge m_h>0$。
若
$$
\|R_0-R_*\|_\infty\le\eta,\qquad
\partial_\tau R_\tau(\theta)\ge c>0
\quad\text{在整个参数窗和圆周上},
$$
并且 $ca>\eta$，那么该族的旋转角像包含区间
$$
[\omega_*-m_h(ca-\eta),\ \omega_*+m_h(ca-\eta)].             \tag{4.2}
$$

**证明。** 右端点有 $R_a\ge R_*+ca-\eta$，所以
$$h\circ R_a\circ h^{-1}(y)\ge y+\omega_*+m_h(ca-\eta).$$
逐次迭代此逐点不等式，旋转角至少是右边的常数位移。左端同理给
不超过 $\omega_*-m_h(ca-\eta)$。旋转数在保向圆同胚的均匀拓扑下连续，
故介值定理给 (4.2)。这里不要求整个族的旋转数严格单调或处处可微。
对连续性也可用有限迭代的上下平移数：任意升举 $f$，
$$
\inf_x\frac{f^n(x)-x}{n}\le\omega(f)\le
\sup_x\frac{f^n(x)-x}{n},
$$
上下界之差至多 $2\pi/n$；固定 $n$ 的迭代对 $f$ 连续，再令 $n$ 大，
即可得到所需连续性。

这一区间内可以选一个明确的 Diophantine 目标，再由介值性选参数；
不需要先证明 $\rho'$ 等于某个参考 action 导数。
但 $\eta,c,a$ 必须对真实完整返回图认证，目前固定切口浮点数据尚未支付它们。

### 4.3 靠近 $44/89$ 的显式有界型目标

令 $g=(\sqrt5-1)/2$，对整数 $A\ge1$ 取
$$
\rho_A=\frac{44(A+g)+1}{89(A+g)+2}
=[0;2,44,A,1,1,\ldots].
$$
有准确距离
$$
\rho_A-\frac{44}{89}
=\frac1{89[89(A+g)+2]}.                                  \tag{4.3}
$$
所有部分商至多 $B=\max(44,A)$，所以
$$
\|k\rho_A\|_{\mathbb R/\mathbb Z}>
\frac1{(B+2)|k|}\qquad(k\ne0).                            \tag{4.4}
$$
这由连分数的精确收敛分式误差公式
$|\rho-p_j/q_j|=[q_j(q_j\alpha_{j+1}+q_{j-1})]^{-1}$
及 $\alpha_{j+1}<B+1$ 得到；非收敛分式若误差小于 $1/(2q^2)$
即由 Legendre 判别成为收敛分式，否则该较弱下界已足够。
分母未约分的情形只改善 (4.4)。
因此不必采用一个量化常数极差的任意二次无理数扰动。
选目标后，实际 KAM/共轭和 PDE 转折估计仍需另付。

## 5. GC 加两种反射不自动给固定切口返回图的正密度

下面是一条结构判断，目的只在避免把 GC 和对称性当成未证明的
有限阶/保密度定理。它不涉及固定平帽或闭面完成标准。

### 5.1 一个真实 GC Cauchy 族

取固定径向度量
$$g=ds^2+\cosh^2s\,d\theta^2,\qquad K=-1.$$
在 $s=0$ 取常速平面闭曲线
$$
\gamma_\epsilon'(\theta)=
(-\sin\tau_\epsilon(\theta),\cos\tau_\epsilon(\theta),0),
\qquad
\tau_\epsilon=\theta+\frac\epsilon n\sin(n\theta),
$$
并固定 $\gamma_\epsilon$ 的角平均为零。$n\ge2$ 时，它的 $n$ 重
旋转对称性精确支付周期闭合；$|\epsilon|<1$ 时曲率为
$1+\epsilon\cos n\theta>0$，故它是简单严格凸闭曲线。
取 $F_s(0,\theta)=e_z$，外法向为
$(\cos\tau_\epsilon,\sin\tau_\epsilon,0)$。
初始第二形式是
$$M(0,\theta)=0,\qquad N(0,\theta)=-1-\epsilon\cos n\theta.$$
Gauss 决定 $L=-a^2/N$。

R29 (2.3) 是关于 $s$ 的解析一阶系统，且初始 $N$ 离零。
解析 Cauchy 定理给真实局部解。对足够小的 $\epsilon$，可在一个
固定短区间中依参数延拓参考旋转解；取初值的一个固定复角条带，
并令 $|\epsilon|e^{n\sigma}$ 足够小，可使这个区间不依赖于 $n$。
由 GC 的线性标架重建，得到同一精确度量的真实周期嵌入带。
周向周期来自周期系数和周期初始标架的径向 ODE 唯一性，不能只由
局部曲面定理省略 holonomy。嵌入性由参考紧带的 $C^1$ 开放性得到。

因 $a$ 偶、初始 $M=0$，唯一性给 $M$ 关于 $s$ 奇、$N$ 关于 $s$ 偶，
重建的面保留经线反射 $F(-s,\theta)=S_zF(s,\theta)$。
初始平面曲线的角反射同样由唯一性保持。
取 $n=4q$ 时也有本题的四重旋转对称性。

### 5.2 真正一阶返回系数

写参考 $h(s)=\sqrt{1-\sinh^2s}$，它在所用短区间为正。
参考第二形式是 $N_0=-ah$、$M_0=0$。令
$$t(s)=\int_0^s h(u)^{-1}\,du.$$
在一阶变分中写
$\dot M=m(s)\sin n\theta$、$\dot N=v(s)\cos n\theta$。
直接线性化 GC 得
$$
m_s=-nv/h^2-(a'/a)m,\qquad
v_s=nm+(a'/a+aa'/h^2)v,
$$
且 $m(0)=0,v(0)=-1$。
令 $x=m/a,\ y=v/(ah)$，转到实际光学变量 $t$：
$$
x_t=-ny-A(t)x,\qquad y_t=nx+B(t)y,
\quad A=2a'h/a,\quad B=2aa'/h.                              \tag{5.1}
$$
这里 $A(t)=2t+O(t^3)$、$B(t)=2t+O(t^3)$，由
$s_t=h$、$a=\cosh s$ 的 Taylor 展开直接得到。

固定正整数 $m_0$，令 $T=2\pi m_0/n$，切口取
$s_\pm=\pm s(T)$。参考返回角为 $\Delta=4T$。
将上述真实 $\dot M,\dot N$ 代入 R29 (5.5)，利用奇偶性和 $nT=2\pi m_0$，
得到准确的一阶式
$$
\dot R(\theta)=C_n\cos(n\theta),\qquad
C_n=4\int_0^T[x(t)\sin(nt)+y(t)\cos(nt)]\,dt.               \tag{5.2}
$$

令 $u=nt$、$\delta=n^{-2}$，在固定区间
$0\le u\le U=2\pi m_0$ 上作解析参数展开。式 (5.1) 给
$$
\begin{aligned}
x&=\sin u+\delta(u\cos u-\sin u)+O(\delta^2),\\
y&=-\cos u-\delta u\sin u+O(\delta^2).
\end{aligned}
$$
余项在该固定区间上一致：系数关于 $\delta$ 解析，有限维线性 ODE
对参数解析依赖。也可以将这些首两项代回方程，再用变常数公式估计余项。
因此
$$
x\sin u+y\cos u=-\cos(2u)-\delta\sin^2u+O(\delta^2),
$$
而 $U=2\pi m_0$，故
$$
\boxed{C_n=-\frac{4\pi m_0}{n^3}+O(n^{-5})\ne0
\quad\text{对所有充分大的 }n.}                           \tag{5.3}
$$
这个非零结论来自真正 GC 变分，不是任意指定一个圆映射后说它来自几何。

### 5.3 双曲周期点排除光滑正密度

取充分大的奇数 $q$，使 $(m_0,q)=1$，并取 $n=4q$。
参考返回角为 $\Delta=2\pi m_0/q$，且 $n\Delta=8\pi m_0$。
对每个固定这样的 $n$，真实返回图满足 $C^1$ 展开
$$
R_\epsilon^{\circ q}(\theta)
=\theta+2\pi m_0+\epsilon qC_n\cos(n\theta)+O(\epsilon^2).
$$
余弦的简单零点经隐函数定理给 $q$ 周期点，其乘子为
$1-\epsilon qnC_n\sin(n\theta)+O(\epsilon^2)\ne1$。
这些是真正的双曲周期点。

若存在严格正的连续不变密度 $\rho$，则
$\rho(R(\theta))R'(\theta)=\rho(\theta)$；沿一条 $q$ 周期轨道相乘，
会迫使 $(R^{\circ q})'=1$，矛盾。因此上述真实 GC、四重及两种反射
并存的例子不保光滑正密度，也不为有限阶圆作用。

**范围。** 这里是固定双曲切口的返回；没有包含实际转折反射和闭帽条件。
因此不能据此证明当前主课题失败，亦不能排除真实闭合另加了有用约束。
它只支付“不能单靠 GC 和反射自动宣称有限阶/保密度”的具体判断，
将后续工作准确推向实际均值控制或 Diophantine 参数路线。
# 追加：真实移动转折图的正则化与变分接口

以下接口仍只处理主特征的几何返回映射；它没有将转折振幅、Maslov
相位、低阶耦合或椭圆端 DtN 偷换成一个纯圆周平移。

为避免单位法向的无关除法，令
$$
C=F_\theta\times F_x,\quad
l=C\cdot F_{xx},\quad m=C\cdot F_{x\theta},\quad
n=C\cdot F_{\theta\theta},\quad \Delta=m^2-ln.
$$
主速度为 $c_\varepsilon=(-m+\varepsilon\sqrt\Delta)/n$。
假定真实候选具有腰反射、两个简单转折图 $x=\pm t(\theta)$，
$t>0$、$n\ne0$，且 $\Delta>0$ 恰在两图之间。这里 $t$ 由该
候选自己的 $\Delta$ 求根，并非角平均度量的转折。

设 $s=x/t(\theta)$，则
$$
\frac{d\theta}{ds}
 =\frac{t\,c_\varepsilon(st,\theta)}
        {1-s\,t_\theta c_\varepsilon(st,\theta)}.
$$
若分母在整个条带有正下界，这是真实的横截坐标变换。
由于 $\Delta(\pm t,\theta)=0$ 且简单，
$$
\bar\Delta(s,\theta)=\frac{\Delta(st(\theta),\theta)}{1-s^2}
$$
延伸为闭条带上的正函数。再取 $s=\sin\tau$，
$-\pi/2\le\tau\le\pi/2$，有
$$
q=\cos\tau\sqrt{\bar\Delta},\quad
c_\varepsilon=\frac{-m+\varepsilon q}{n},\quad
X=\frac{dx}{d\tau}
 =\frac{t\cos\tau}{1-s t_\theta c_\varepsilon},\quad
\theta_\tau=c_\varepsilon X.
$$
整个几何流在转折处具有正则系数。在正端，
$\bar\Delta(1,\theta)=-t\Delta_x(t,\theta)/2$；
负端相同，这是腰反射的结果。

具体变分可避免对转折图求二阶参数导数。下标 $\theta$ 和点导数
先都在固定 $x$ 取值。将速度导数乘以 $X$ 后，奇异项精确相消：
$$
\begin{aligned}
c_{\varepsilon,\theta}X
={}&X\left(-\frac{m_\theta}{n}
       +\frac{m n_\theta}{n^2}
       -\varepsilon\frac{q n_\theta}{n^2}\right)
 +\frac{\varepsilon t\Delta_\theta}
 {2n(1-s t_\theta c_\varepsilon)\sqrt{\bar\Delta}},\\
\dot c_\varepsilon X
={}&X\left(-\frac{\dot m}{n}
       +\frac{m\dot n}{n^2}
       -\varepsilon\frac{q\dot n}{n^2}\right)
 +\frac{\varepsilon t\dot\Delta}
 {2n(1-s t_\theta c_\varepsilon)\sqrt{\bar\Delta}}.
\end{aligned}
$$
这些右端包括两端都连续。沿轨道解
$$
J_\tau=(c_{\varepsilon,\theta}X)J,\qquad
Y_\tau=(c_{\varepsilon,\theta}X)Y+\dot c_\varepsilon X,
\quad J_{\rm in}=1,\ Y_{\rm in}=0.
$$
若本段从边界 $x=\sigma_{\rm in}t(\theta)$ 到
$x=\sigma_{\rm out}t(\theta)$，$\sigma_{\rm in/out}\in\{-1,1\}$，
定义 $P(\theta)$ 为终点角参数。则
$$
\begin{aligned}
P'(\theta)
 &=\frac{J(1-c_{\rm in}\sigma_{\rm in}t_{\theta,\rm in})}
        {1-c_{\rm out}\sigma_{\rm out}t_{\theta,\rm out}},\\
\dot P(\theta)
 &=\frac{-Jc_{\rm in}\sigma_{\rm in}\dot t_{\rm in}
                 +Y+c_{\rm out}\sigma_{\rm out}\dot t_{\rm out}}
        {1-c_{\rm out}\sigma_{\rm out}t_{\theta,\rm out}},\\
t_\theta&=-\Delta_\theta/\Delta_x,\qquad
\dot t=-\dot\Delta/\Delta_x\quad\text{在正转折图上}.
\end{aligned}
$$
证明：先在严格内部应用普通 ODE 的初始时刻和终止事件微分公式
$d\theta_{\rm out}
=J(d\theta_{\rm in}-c_{\rm in}dx_{\rm in})+Y\,da
+c_{\rm out}dx_{\rm out}$，代入
$dx=\sigma(t_\theta d\theta+\dot t\,da)$ 后解出。上述正则化使所有
系数积分在端点收敛，故可将内部切口推进真实转折图。
正、负两支串联时用普通链式法则即可。

实际均值列 $V=A(x)e_r+C_0(x)e_z$ 的原始二型导数无需 Christoffel
项或度量平均：$\dot C=V_\theta\times F_x+F_\theta\times V_x$，
$$
\dot l=\dot C\cdot F_{xx}+C\cdot V_{xx},\quad
\dot m=\dot C\cdot F_{x\theta}+C\cdot V_{x\theta},\quad
\dot n=\dot C\cdot F_{\theta\theta}+C\cdot V_{\theta\theta}.
$$
再取 $\dot\Delta=2m\dot m-n\dot l-l\dot n$。
这给真实移动转折图上的均值灵敏度，不是固定切口或径向作用量导数。
仍须由完整散射算子判断该主返回图是否正是最终逆问题的返回图。

### 旧 n101 图的独立有限差分复核（冻结）

2026-11-12，使用 SHA256
598fc957bcc8cd2aa958da3bc2f69d779fd055f7ee9fce39d968d33e4ff306d6，
在 $\theta=3\pi/32$ 重算不包含变分 ODE 的 geometry-only 返回。
角步长 $10^{-4}$ 给出导数 $0.76753420456$，原变分值为
$0.76754686011$，差 $-1.27\,10^{-5}$。
第二个原始 mean 参数取步长 $2\,10^{-5}$，独立差分为
$-11.82220287$，原变分值为 $-11.84548954$，差 $0.02328668$
（约 $0.197\%$）。ODE 相对容差为 $10^{-8}$。
这一检查确认了移动端点后该列相对于旧固定切口计算的反号，
但未提供高精度导数证书；不能抹去这个剩余误差。
输出完整保存在 2026-11-12-new-spline-turning-return-fd.json。
该候选的结果现被冻结；不向新的 phase24 图迁移其角映射或作用量。

