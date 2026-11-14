# R33：精确单位切向参数化、常速回缩与可见腰圈

2026-11-12，constructive-route。

**状态：完整证明的参数化与回缩结论。** 在具有本题四重旋转和
角反射对称的正则材料圆上，本文精确解掉
$P_{\ne0}|F_\theta|^2=0$，给出剩下两条真实方程、自由均值及 $C^2$
预算。有限个切向角系数定义的是带有无限位置 Fourier 尾的真实曲线。
还给出 $U_4/a=0.06$、严格凸、角向 $C^2$ 尾显式可控的非圆腰圈。
这些结论不假定余下方程已经可解，不构成闭面或固定帽的存在证明。

## 1. 周期原函数和对称类

角变量周期为 $2\pi$，$\langle f\rangle=(2\pi)^{-1}\int f$。定义
$\mathcal P f$ 为唯一的零均值周期函数，满足
$$
(\mathcal P f)_\theta=f-\langle f\rangle.
\tag{1.1}
$$
它对任意连续向量值 $f$ 都有定义，并且
$$
\|\mathcal P f\|_\infty\le\frac{\pi}{2}\|f\|_\infty.
\tag{1.2}
$$
例如用卷积核 $\pi-t$，$0<t<2\pi$：
$$
\mathcal P f(\theta)=\frac1{2\pi}
  \int_0^{2\pi}(\pi-t)f(\theta-t)\,dt.
$$
核的平均为零、分布导数为 $2\pi\delta_0-1$，
且其归一化 $L^1$ 范数为 $\pi/2$，证明 (1.1)–(1.2)。
此定义不要求被积函数本身具有零均值。

记 $R$ 为绕 $z$ 轴旋转 $\pi/2$，$S=\operatorname{diag}(1,-1,1)$。
考察材料圆
$$
F(r,\theta+\pi/2)=R F(r,\theta),\qquad
F(r,-\theta)=S F(r,\theta).
\tag{1.3}
$$
假设 $\ell=|F_\theta|>0$，令 $T=F_\theta/\ell$。则
$$
T(\theta+\pi/2)=R T(\theta),\qquad T(-\theta)=-S T(\theta).
\tag{1.4}
$$
第一条使 $T$ 的水平平均为零，第二条使其竖直平均为零，因此
$$\boxed{\langle T\rangle=0.} \tag{1.5}$$
这是单位化以后仍能闭圈的关键；任意闭曲线的单位切向平均
一般并不为零。

## 2. 对称候选到精确常速材料圆的回缩

设 $F$ 在有限圆柱 $I\times S^1$ 上满足 (1.3)，且
$\ell\ge m>0$。令
$$
a(r)=\langle\ell(r,\cdot)\rangle,\qquad
c(r)=\langle F(r,\cdot)\rangle,\qquad
Z=\mathcal P T,
$$
并定义
$$
\boxed{\mathcal R(F)=\widehat F=c+aZ.}                 \tag{2.1}
$$
由 (1.5) 得
$$
\widehat F_\theta=aT,\qquad
|\widehat F_\theta|^2=a(r)^2.                          \tag{2.2}
$$
所以角向度量的所有非零模被精确消去。$c$ 位于 $z$ 轴；
$Z$ 的唯一零均值原函数性质保证 (1.3) 仍成立。

若原候选已有 $\ell=a(r)$，则
$F=c+a\mathcal P T$，从而 $\mathcal R(F)=F$。特别
$$
\boxed{\mathcal R^2=\mathcal R.}                       \tag{2.3}
$$
这是一个真正的回缩，不只是角向约束的一阶修正。

令 $e=\ell-a$。因为
$\langle\ell T\rangle=\langle F_\theta\rangle=0$，
$\langle T\rangle=0$，有 $\langle eT\rangle=0$，并得到精确差值
$$
\boxed{\widehat F-F=-\mathcal P(eT).}                  \tag{2.4}
$$
若 $F$ 在一条开领圈上已经是旋转面
$a_0(r)e_r+z_0(r)e_z$，则该领圈上 $\mathcal R(F)=F$。
因此在具有真实旋转开领圈的候选上，本操作可以在那里与恒等操作
直接相接；它不会自行制造这种领圈。

若另有腰反射
$F(-r,\theta)=QF(r,\theta)$、
$Q=\operatorname{diag}(1,1,-1)$，则 $a$ 为偶函数，
$c_z$ 为奇函数，(2.1) 保持该反射。

### 2.1 只用二阶导数的 $C^2$ 正则性

公式 (2.1) 含 $F_\theta$，但并不因此损失一个径向导数。
设 $F\in C^2$，以下公式在光滑函数上先直接成立，并可由平滑逼近
延伸到 $C^2$。写
$$
G=F_\theta,\quad h=F_{r\theta},\quad u=F_{rr},\quad
\Pi=I-TT^{\mathsf T},\quad H=\frac{\Pi}{\ell}.
$$
则
$$
\begin{aligned}
T_r&=Hh,& T_\theta&=HF_{\theta\theta},\\
a'&=\langle T\cdot h\rangle,&
a''&=\left\langle\frac{|\Pi h|^2}{\ell}
                         -T_\theta\cdot u\right\rangle.       \tag{2.5}
\end{aligned}
$$
最后一式来自
$\ell_{rr}=|\Pi h|^2/\ell+T\cdot\partial_\theta u$，
再按 $\theta$ 积分分部。

令
$$
B=-\frac{2(T\cdot h)\Pi h+|\Pi h|^2T}{\ell^2}.
$$
形式上的 $T_{rr}=H\partial_\theta u+B$ 给出不含三阶导数的恒等式
$$
\boxed{
Z_{rr}=Hu-\langle Hu\rangle-\mathcal P(H_\theta u)+\mathcal P B.
}                                                            \tag{2.6}
$$
同时 $Z_r=\mathcal P(Hh)$、
$Z_{r\theta}=Hh$、$Z_{\theta\theta}=HF_{\theta\theta}$。
式 (2.6) 的右边连续。对称的光滑逼近 $F_j\to F$ 于 $C^2$，
并保持 $|F_{j,\theta}|\ge m/2$ 后，所有上述右边都一致收敛。
一阶公式和二阶公式由此共同证明 $a,Z,\widehat F\in C^2$。
也可在分布意义下先证明 (2.5)–(2.6)，再由连续右端恢复经典二阶导数。

以下给可直接核算的粗预算。记
$H_1=\|F_{r\theta}\|_\infty$、
$H_2=\|F_{\theta\theta}\|_\infty$、
$U_2=\|F_{rr}\|_\infty$。由
$$
\|H\|\le m^{-1},\qquad
\|H_\theta\|\le3H_2m^{-2},\qquad
\|B\|\le2H_1^2m^{-2}
$$
和 (1.2)，有
$$
\begin{aligned}
|a'|&\le H_1,&
|a''|&\le(H_1^2+H_2U_2)/m,\\
\|Z\|_\infty&\le\pi/2,&
\|Z_r\|_\infty&\le(\pi/2)H_1/m,\\
\|Z_{r\theta}\|_\infty&\le H_1/m,&
\|Z_{\theta\theta}\|_\infty&\le H_2/m,\\
\|Z_{rr}\|_\infty
&\le\frac{2U_2}{m}
  +\frac{\pi}{2m^2}(3H_2U_2+2H_1^2).                     \tag{2.7}
\end{aligned}
$$
最终使用
$$
\widehat F_{rr}=c''+a''Z+2a'Z_r+aZ_{rr},\quad
\widehat F_{r\theta}=a'T+aT_r,\quad
\widehat F_{\theta\theta}=aT_\theta.                      \tag{2.8}
$$
这也证明在 $\ell\ge m$ 的有界 $C^2$ 集上，本回缩
关于原候选的 $C^2$ 连续性。

### 2.2 光滑候选上的小修正预算

若实际候选足够光滑，以致以下量有界，记
$$
E_0=\|e\|,\quad E_r=\|e_r\|,\quad E_{rr}=\|e_{rr}\|,
\quad E_\theta=\|e_\theta\|,\qquad
K_r=\|T_r\|,\ K_{rr}=\|T_{rr}\|,\ K_\theta=\|T_\theta\|.
$$
对 $\Delta=\widehat F-F$，直接微分 (2.4) 给
$$
\begin{aligned}
\|\Delta\|&\le(\pi/2)E_0,&
\|\Delta_\theta\|&\le E_0,\\
\|\Delta_{\theta\theta}\|&\le E_\theta+E_0K_\theta,&
\|\Delta_r\|&\le(\pi/2)(E_r+E_0K_r),\\
\|\Delta_{r\theta}\|&\le E_r+E_0K_r,&
\|\Delta_{rr}\|&\le(\pi/2)(E_{rr}+2E_rK_r+E_0K_{rr}).
                                                               \tag{2.9}
\end{aligned}
$$
这些是给定材料坐标中的 $C^2$ 预算。用于 reach、曲率或 R1 的几何
稳定界时，仍须代入候选自己的度量下界和坐标转换常数。
特别，(2.2) 本身不保证 $\widehat F$ 仍浸入；若需要由接近性继承浸入、
嵌入或 reach，必须实付相应的一阶、二阶和全局距离预算。

### 2.3 回缩的精确线性化

对保持 (1.3) 的变分 $V$，有
$$
\dot c=\langle V\rangle,\quad
\dot a=\langle T\cdot V_\theta\rangle,\quad
\dot T=\frac{\Pi V_\theta}{\ell}.
$$
因此
$$
\boxed{
D\mathcal R_F[V]=\langle V\rangle+
\langle T\cdot V_\theta\rangle\,\mathcal P T+
a\,\mathcal P\!\left(\frac{\Pi V_\theta}{\ell}\right).
}                                                            \tag{2.10}
$$
在常速点 $\ell=a$，令 $f=T\cdot V_\theta$，化为
$$
D\mathcal R_F[V]=V-\mathcal P\!\left(T(f-\langle f\rangle)\right),
\qquad
2F_\theta\cdot\partial_\theta D\mathcal R_F[V]
       =2a\langle f\rangle.                              \tag{2.11}
$$
这里 $\langle T(f-\langle f\rangle)\rangle=0$：
由单位化后的对称恒等式 $\langle T\rangle=0$ 求变分，
$\langle\Pi V_\theta\rangle=0$；又
$\langle V_\theta\rangle=0$，所以 $\langle Tf\rangle=0$。
因此 (2.11) 的导数没有漏掉一个平均项。
它是真正投向角向度量线性约束切空间的投影；
$(D\mathcal R_F)^2=D\mathcal R_F$ 也由 (2.3) 求导得到。

## 3. 可直接计算的单位切向角参数化

现在直接把常速约束作为定义。取实函数
$$
B(r,\theta)=\sum_{j\ge1}\beta_j(r)\sin(4j\theta),\qquad
\psi(r,\theta)=\sum_{j\ge1}\gamma_j(r)\sin(4j\theta),
\quad \phi=\theta+\pi/2+B,
$$
并令
$$
T=(\cos\psi\cos\phi,\ \cos\psi\sin\phi,\ \sin\psi),\quad
F=z_0(r)e_z+a(r)\mathcal P T.                            \tag{3.1}
$$
有限和没有收敛问题；无限和须按所需阶数收敛。
这里 $|T|=1$ 恒等成立。$T_h=i e^{i\theta}\cos\psi\,e^{iB}$
的频率为 $1\bmod4$，而 $T_z=\sin\psi$ 关于 $\theta$ 为奇函数，
故 $\langle T\rangle=0$。因此 (3.1) 为真正闭圈，且
$F_\theta=aT$ 精确成立。

若 $\beta_j$ 关于 $r$ 为偶函数，$\gamma_j,z_0$ 为奇函数，
$a$ 为偶函数，则同时保留腰反射。特别腰处 $\psi=0$，
腰圈严格位于平面 $z=0$。

这个角表示是满足相关取向的单位切向场的一张局部坐标图：
例如当 $T_h\ne0$、水平角可选为
$\theta+\pi/2+$ 一个周期奇函数时可用。它不是对所有单位切向场的
全局球面坐标；$T_h=0$ 处应换图，不能假装 $\phi$ 仍有唯一光滑值。
前一节的回缩不需要这个球面坐标假设。

### 3.1 剩下的真实方程与输出均值

写 $Z=\mathcal P T$、$G=F_r$。则
$$
G=z_0'e_z+a'Z+a\mathcal P T_r.                          \tag{3.2}
$$
取单位球面切向基
$$
e_\phi=(-\sin\phi,\cos\phi,0),\qquad
e_\psi=(-\sin\psi\cos\phi,-\sin\psi\sin\phi,\cos\psi),
$$
有
$$T_r=\cos\psi\,B_r e_\phi+\psi_r e_\psi.                \tag{3.3}$$
故剩下的两条精确非均值度量方程为
$$
\boxed{G\cdot T=0,\qquad
       |G|^2-\langle|G|^2\rangle=0.}                    \tag{3.4}
$$
第一项关于 $\theta$ 为奇函数，故平均自动为零；
没有漏掉一个需另外指定的交叉均值。

令 $E(r)=\langle|G|^2\rangle$。若 (3.4) 成立并且
$E>0$、$a>0$，则
$$F^*e=E(r)\,dr^2+a(r)^2\,d\theta^2.                    \tag{3.5}$$
这正是允许径向平均度量自由输出的形式。以
$ds=\sqrt E\,dr$ 换参后得到 $ds^2+a(s)^2d\theta^2$。
不应先把 $E$ 锁定为背景值再宣称仍有同样的自由度。

在固定当前 $a,B,\psi$ 时，(3.2) 对
$z_0',a',\beta_j',\gamma_j'$ 线性，(3.4) 第一式为它们的线性
角方程，第二式为二次角方程。可据此构造真实约束 Newton 系统，
但这句话不提供其满射性、全频右逆或极点边界条件。

### 3.2 二阶切向 jets

记 $b=B_r$、$p=\psi_r$。在笛卡尔基中
$$
\begin{aligned}
T_{rr}={}&
  \cos\psi\,B_{rr}e_\phi+\psi_{rr}e_\psi
 -2\sin\psi\,bp\,e_\phi\\
&+\sin\psi\cos\psi\,b^2e_\psi
 -(\cos^2\psi\,b^2+p^2)T,\\
T_\theta={}&
\cos\psi(1+B_\theta)e_\phi+\psi_\theta e_\psi.
                                                               \tag{3.6}
\end{aligned}
$$
例如 $e_{\phi,r}=-\cos\psi\,bT+\sin\psi\,b e_\psi$、
$e_{\psi,r}=-pT-\sin\psi\,b e_\phi$，代入 (3.3) 即得。
因此有限角系数及其径向二阶 jets 可以直接生成
$T,T_r,T_{rr},T_\theta$，再对前三者分别施加 $\mathcal P$。
这些是定义对象的精确表达；实际 FFT 计算还需第 5 节的截断预算。

## 4. 显式严格凸的可见常速腰圈

在腰处令 $\psi=0$、$B=\beta\sin4\theta$。以复数表示水平位置：
$$
T_h=i e^{i\theta+i\beta\sin4\theta},\qquad
F_h=a\sum_{j\in\mathbb Z}
       \frac{J_j(\beta)}{1+4j}e^{i(1+4j)\theta}.          \tag{4.1}
$$
可在本文内部定义
$$
J_j(\beta)=\sum_{k\ge0}
 \frac{(-1)^k(\beta/2)^{2k+j}}{k!(k+j)!}\quad(j\ge0),
\qquad J_{-j}=(-1)^jJ_j.
$$
将
$e^{i\beta\sin t}=\exp((\beta/2)e^{it})\exp(-(\beta/2)e^{-it})$
展开并按频率收集，即证明 (4.1)，不需外用特殊函数恒等式。
全级数在有界复角带上一致绝对收敛，允许任意有限次角微分。

在旋转标架中，令
$F_h e^{-i\theta}=aJ_0+\sum_{j\ge1}
[U_{4j}\cos4j\theta+iT_{4j}\sin4j\theta]$。则
$$
\begin{aligned}
U_{4j}&=a\left(\frac{J_j}{1+4j}+\frac{J_{-j}}{1-4j}\right),\\
T_{4j}&=a\left(\frac{J_j}{1+4j}-\frac{J_{-j}}{1-4j}\right).
\end{aligned}                                                   \tag{4.2}
$$
特别
$$
\boxed{U_4=\frac{8a}{15}J_1(\beta),\qquad T_4=-U_4/4.} \tag{4.3}
$$

存在唯一 $\beta_*\in(9/40,23/100)$ 使 $U_4/a=3/50$。
证明如下。在 $\beta=9/40$，交错级数给
$J_1(\beta)<\beta/2$，所以 $8J_1/15<3/50$；
在 $\beta=23/100$，
$$J_1(\beta)\ge\beta/2-\beta^3/16$$
给 $8J_1/15>0.0609277>3/50$。而在 $0\le\beta\le1/4$，
交错导数级数给
$$
J_1'(\beta)\ge\frac12-\frac{3\beta^2}{16}>0.
$$
各交错项绝对值严格递减，可直接由相邻项比值验证，
故中值定理和严格单调性证明所述唯一性。

该腰圈的有向曲率为
$$
\kappa(\theta)=\frac{1+4\beta_*\cos4\theta}{a},
\qquad
\frac{0.08}{a}<\kappa(\theta)<\frac{1.92}{a}.            \tag{4.4}
$$
曲线闭合，切向角严格递增且整周增加 $2\pi$，所以它为严格凸的
简单闭曲线。可直接证明后一句：沿任一固定方向的投影导数恰有
两个零点，并分别为唯一极大与极小；每个切线因此为唯一支撑线，
整条曲线就是其凸包的边界。

对于正的小 $\beta$，$J_j(\beta)>0$（首项减去以后递减的交错尾），
且奇数 $j$ 的 $U_{4j}>0$。所以两个相差 $\pi/4$ 的相位在对齐
旋转标架后的径向分量差为
$$
2\sum_{j\ {\rm odd}}U_{4j}>2U_4=0.12a.                 \tag{4.5}
$$
这是腰圈本身的显式形状差。它尚不是整张闭面的 Hausdorff 下界，
也尚未支付 R18 中排除附近其他面片和固定握持配准所需的预算。

### 4.1 十六个位置模之后的严格角向尾界

当 $|\beta|\le1/4$，
$$
|J_j(\beta)|
\le e^{\beta^2/4}\frac{(|\beta|/2)^j}{j!}
\le\frac{64}{63}\frac{8^{-j}}{j!}\qquad(j\ge0).          \tag{4.6}
$$
第一界由定义级数取绝对值并用 $(k+j)!\ge j!$；
第二界用 $e^{1/64}\le(1-1/64)^{-1}$。
保留 $|j|\le16$ 后，位置及一、二阶角导数的余项都被
$$
2a\frac{64}{63}\sum_{j\ge17}(4j+1)\frac{8^{-j}}{j!}
                                                               \tag{4.7}
$$
控制。首项中 $17!>2^{48}$、$8^{-17}=2^{-51}$；
加权级数的相邻项比值至多
$(73/69)/144<1/136$。因此
$$
\boxed{\max_{0\le k\le2}
 \|\partial_\theta^k(F_h-F_h^{(|j|\le16)})\|_\infty
       <2^{-90}a.}                                      \tag{4.8}
$$
具体地，常数
$2(64/63)\,69(136/135)<2^8$，结合 $2^{-99}$ 甚至给出更强
的严格 $2^{-91}a$ 界；(4.8) 取了整数量级余量。
这证明本例所需的无限位置尾极小；有限位置截断仍只是近似，
不能把它替换为满足精确常速的定义对象。

## 5. 有限切向角系数所定义的无限位置尾

给定有限个 $\beta_j,\gamma_j$，(3.1) 的真实 $T$ 通常仍含无限多
Fourier 模。若在 $|\operatorname{Im}\theta|\le\sigma$ 上
$|B|\le b$、$|\psi|\le p$，则各水平笛卡尔分量可取界
$e^\sigma e^{b+p}$，竖直分量可取 $e^p$。
对任一分量，以其条带上界 $M$ 记，则 Cauchy 移线给
$$
|\widehat T_n|\le M e^{-\sigma|n|}.
$$
因为真实平均为零，$a\mathcal PT$ 的非零模为
$a\widehat T_n/(in)$。令 $q=e^{-\sigma}$，截去 $|n|>N$，
得到
$$
\begin{aligned}
\|\text{位置尾}\|_\infty
 &\le\frac{2aM q^{N+1}}{(N+1)(1-q)},\\
\|\text{一阶角尾}\|_\infty
 &\le\frac{2aM q^{N+1}}{1-q},\\
\|\text{二阶角尾}\|_\infty
 &\le2aM q^{N+1}
       \left(\frac{N+1}{1-q}+\frac{q}{(1-q)^2}\right).
                                                               \tag{5.1}
\end{aligned}
$$
向量 Euclidean 范数可逐分量加界，或以所有复分量绝对值之和的
条带界作为共同 $M$；不要把单分量界直接当成向量界。
对 $T_r,T_{rr}$ 使用 (3.3)、(3.6) 的条带范数后，同一证明给
$F_r,F_{rr}$ 的尾预算。

若用 $Q$ 个等距点的 FFT 取系数，还存在混叠。
对保留的 $|n|\le N<Q/2$，离散系数的精确混叠恒等式是
$$
\widetilde T_n-\widehat T_n
   =\sum_{k\in\mathbb Z\setminus\{0\}}\widehat T_{n+kQ},
$$
从而
$$
|\widetilde T_n-\widehat T_n|
\le\frac{2M q^{Q-|n|}}{1-q^Q}.                          \tag{5.2}
$$
因此有限 FFT 原函数与真实 $\mathcal PT$ 的差，要同时加入
(5.1) 的截断尾及 (5.2) 除以 $|n|$ 后的保留模误差；
第 $k$ 阶角导数则乘上 $|n|^k$。离散均值应按真实的零均值
恒等式置零，不应把一个微小混叠均值解释成闭圈障碍。
网格加倍的差值只能作为浮点实现诊断，不能替代上述解析上界。

## 6. 对闭面问题的准确接口

本结果允许从一个实际对称候选出发，先用 (2.1) 精确满足角向
度量条件，并用 (2.9) 计入修改；也允许从 (3.1) 直接求解剩余
两条真实方程。由此消去的是一整条代数角向约束，而不是改变
完整问题的精确等距要求。

有限圆柱上的 $\ell\ge m>0$ 不覆盖半径趋零的极点。
若在已有旋转开领圈处保持恒等，可继承那部分真实帽；
若非轴对称尾一直延伸到极点，必须另证相应的加权 $C^2$
消失阶、无皱嵌入和固定开帽。本文不以 $m\downarrow0$ 的失控预算
代替该证明，也未由单条腰圈推断整张闭面的 reach 或可见比例。
