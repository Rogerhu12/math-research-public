# 一个真闭圈、正宽、非刚体等距可变的显式鞍环

**状态：完整作者证明，待未参与者全文独审；恢复文本 v2。**

本文件以新路径从会话中保留的完整正文生成文本恢复，未声称从失联磁盘重新
读回。与原生成正文相比，新增本段来源说明、$\pi<22/7$ 的积分证明、
reach 段局部坐标记号澄清，以及末尾经典表示的文献背景；数学构造与结论
不变。恢复保存本身不是程序执行，也不是独立重跑。

原环境中纯符号程序的真实工具执行为 c1bd82，退出码 0，报告含 31 个精确
恒等式和 23 个有理门。该报告早于完整正文文件生成，其源哈希没有绑定
本恢复版；不把旧执行算作新正文的哈希绑定、完整 execution receipt 或
独立审查。新文本的 commit/blob 是恢复存证；新的可执行来源封存及独立
重跑仍未付。本文件没有恢复或传送数值数组。

作者：独立几何分工，2026-11-09。
全 $\mathrm E(3)$ 非全等的“内在等距分类加解析延拓”证明途径由 root
提出并参与；这部分不将 root 的后续核查称为独立来源。
本稿没有读取主候选优化数据，没有运行 BVP、tail 或 RK。
R43 和 Enneper 入口试验的原稿、程序、报告均保持封存。

本稿给出一个实际存在的 $C^\infty$ 共同度量弯曲族，而不只是单张鞍环，
也不只是列出未来需要满足的条件。基础位置式完全显式；可变族通过一个
具体的四维约束映射和已证明可逆的 Jacobian 构造。所有时间都有统一正宽
嵌入和一个有边曲面 reach 下界。固定区域具有足够大的直径，而且非零的
小参数像在包含反射的全欧氏群下都不全等。

**严格范围：** 参数域仍是有两个边界的环带，不是闭曲面；没有给出有效的
弯曲参数区间数值或 $0.05D$ 位移界。固定 $b>0$ 时本环带处处 $K<0$，
不能直接接到 R43 的平端，也不能直接匹配水平活动核心的两 jet。
本稿末尾单列这些真实缺口。

## 1. 明确的球面方向曲线

固定尺度 $b>0$，并记

$$
\eta=-3+2\sqrt2,\qquad
\sigma=\sqrt{1-\eta^2}>0,\qquad
\omega=\frac{2\pi}{3}.
\tag{1}
$$

因此 $-1<\eta<0$、$\eta^2+6\eta+1=0$。
令 $R_z(\theta)$ 是绕竖轴的标准旋转，$R_y(\gamma)$ 的约定为
$(x,y,z)\mapsto(\cos\gamma\,x+\sin\gamma\,z,y,
-\sin\gamma\,x+\cos\gamma\,z)$，其中 $\cos\gamma=\eta$、
$\sin\gamma=\sigma$。定义

$$
d_0(\theta)=R_z(\theta)R_y(\gamma)
  (\cos3\theta,\sin3\theta,0).
\tag{2}
$$

它是实解析单位向量曲线。把水平分量写成复数 $W=x+iy$，则

$$
(d_0)_W=\frac{\eta+1}{2}e^{4i\theta}
        +\frac{\eta-1}{2}e^{-2i\theta},\qquad
(d_0)_z=-\sigma\cos3\theta.
\tag{3}
$$

尤其

$$
d_0(\theta+\omega)=R_z(\omega)d_0(\theta).
\tag{4}
$$

令 $k_0=|d_0'|$。直接求导并用 (1) 消去 $\eta^2$ 得

$$
k_0^2=10+6\eta-\sigma^2\cos^23\theta
     =8+\sigma^2\sin^23\theta,\qquad
2\sqrt2\le k_0<3.
\tag{5}
$$

因此整个球面方向曲线无不正则点。它可能在球面上自交；下面的空间中心曲线
和环带嵌入证明不要求球面方向曲线单射。

## 2. 向量面积恰为零，中心曲线真实闭合

设 $A=(\eta+1)/2$、$B=(\eta-1)/2$。由实际叉乘得到

$$
\begin{aligned}
(d_0\times d_0')_W
 &=\frac{\sigma(\eta+6)}2e^{i\theta}
   +\frac{\sigma(\eta+1)}4e^{7i\theta}
   +\frac{\sigma(\eta-1)}4e^{-5i\theta},\\
(d_0\times d_0')_z
 &=\frac{\eta^2+6\eta+1}{2}+2AB\cos6\theta\\
 &=-\frac{\sigma^2}{2}\cos6\theta.
\end{aligned}
\tag{6}
$$

所有分量的零 Fourier 系数都为零，故不是仅有旋转对称，而是精确满足

$$
\int_0^{2\pi}d_0\times d_0'\,d\theta=0.
\tag{7}
$$

取零平均原函数 $c_0'=b\,d_0\times d_0'$：

$$
\begin{aligned}
(c_0)_W
 &=-\frac{ib\sigma(\eta+6)}2e^{i\theta}
   -\frac{ib\sigma(\eta+1)}{28}e^{7i\theta}
   +\frac{ib\sigma(\eta-1)}{20}e^{-5i\theta},\\
(c_0)_z
 &=-\frac{b\sigma^2}{12}\sin6\theta .
\end{aligned}
\tag{8}
$$

这条空间曲线恰为 $2\pi$ 周期，并且

$$
c_0(\theta+\omega)=R_z(\omega)c_0(\theta).
\tag{9}
$$

没有位置 monodromy 剩余。下面还会直接证明 $c_0$ 单射。令

$$
R=\frac{b\sigma(\eta+6)}2,\qquad
P=\frac{b\sigma(\eta+1)}{28},\qquad
Q=\frac{b\sigma(1-\eta)}{20}.
\tag{10}
$$

三个量均正；对水平坐标作一次固定的 $90^\circ$ 旋转后，

$$
i(c_0)_W=Re^{i\theta}+Pe^{7i\theta}+Qe^{-5i\theta}.
\tag{11}
$$

两个对后面估计有用的精确等式为

$$
7P+5Q=\frac{b\sigma}{2},\qquad
49P+25Q=R.
\tag{12}
$$

## 3. 真实位置式、共同径向度量和第二基本形式

先定义基础全圈直纹面

$$
\widetilde F_0(v,\theta)=c_0(\theta)+v\,d_0(\theta).
\tag{13}
$$

由 $|d_0|=1$、$d_0\cdot d_0'=0$ 和 (8)，

$$
|\partial_v\widetilde F_0|^2=1,\qquad
\partial_v\widetilde F_0\cdot\partial_\theta\widetilde F_0=0,\qquad
|\partial_\theta\widetilde F_0|^2=(b^2+v^2)k_0^2.
\tag{14}
$$

定义球面弧长坐标及全长

$$
u_0(\theta)=\int_0^\theta k_0(x)\,dx,\qquad
\ell=u_0(2\pi),\qquad
u\in\mathbb R/\ell\mathbb Z.
\tag{15}
$$

$u_0$ 严格递增且实解析；其逆 $\theta_0(u)$ 实解析。令

$$
F_0(v,u)=\widetilde F_0(v,\theta_0(u)).
\tag{16}
$$

则诱导度量恰为

$$
\boxed{g=dv^2+(b^2+v^2)\,du^2.}
\tag{17}
$$

若希望材料角的周期是 $2\pi$，令 $\vartheta=2\pi u/\ell$、
$q=\ell/(2\pi)$，则 $g=dv^2+q^2(b^2+v^2)d\vartheta^2$，
其中 $2\sqrt2<q<3$。由 (5)，每个 $\omega$ 扇区的球面弧长都是
$\ell/3$；因此 $u\mapsto u+\ell/3$ 是材料 $C_3$ 动作。

在单位球面弧长下写

$$
T=d_u,\quad n=d\times T,\quad
T_u=-d+\kappa n,\quad n_u=-\kappa T.
\tag{18}
$$

一般地，只要 $d$ 是单位速球面曲线且 $c_u=bn$，
$F=c+vd$ 就有 (17)。取 $a=\sqrt{b^2+v^2}$，单位法向为

$$
N=\frac{v n-bT}{a}.
\tag{19}
$$

在坐标 $(v,u)$ 中，其第二基本形式系数为

$$
L=0,\qquad M=-\frac ba,\qquad N_{\!II}=\kappa a,\qquad
\boxed{K=-\frac{b^2}{(b^2+v^2)^2}<0.}
\tag{20}
$$

例如 $F_{uu}=-v d-b\kappa T+v\kappa n$，立刻给出
$F_{uu}\cdot N=\kappa a$。因此 (20) 不需除以角向第二基本形式。

基础方向曲线的球面测地曲率为

$$
\begin{aligned}
X(\theta)&=\sigma^2\sin^23\theta,\\
\det(d_0,d_0',d_0'')
   &=(d_0)_z\bigl(17+3\eta+X(\theta)\bigr),\\
\kappa_0(\theta)
   &=\frac{(d_0)_z(\theta)\bigl(17+3\eta+X(\theta)\bigr)}
           {(8+X(\theta))^{3/2}}.
\end{aligned}
\tag{21}
$$

特别地，$\kappa_0$ 在 $\cos3\theta=0$ 的六条角射线上为零，且变号。
这些点的 $M=-b/a$ 仍非零，整个位置图仍正则，$K$ 仍严格负。
所以不能把本例塞入假定角向系数恒正的 chart；这些角零点已经由实际位置式
完整覆盖。

## 4. 基础中心曲线的全局弦长和法向管界

以下估计只用有理数门，不用采样。由

$$
\frac{113}{80}<\sqrt2<\frac{17}{12}
$$

得到

$$
-\frac7{40}<\eta<-\frac16,\qquad
\frac{49}{50}<\sigma<1,\qquad
\frac{57}{20}b<R<3b.
\tag{22}
$$

例如 $\sigma>49/50$ 由 $(49/50)^2<1-(7/40)^2$ 得到。
更精确的半径下界为 $R/b>11417/4000>57/20$。

把 (11) 的主圆 $Re^{i\theta}$ 看作中心曲线的平面主项。其余水平项的
一阶导数范数至多 $7P+5Q=b\sigma/2$，竖直项的一阶导数范数至多
$b\sigma^2/2$，故联合余项 $e$ 满足

$$
\|e'\|_\infty
 \le\frac b2\sqrt{\sigma^2+\sigma^4}<\frac{3b}{4}.
\tag{23}
$$

对两角的最短圆周距离 $\delta\in[0,\pi]$，沿最短参数弧积分余项，
并用 $\sin(\delta/2)\ge\delta/\pi$ 及 $\pi<22/7$，有

$$
\begin{aligned}
|c_0(\theta)-c_0(\phi)|
 &\ge 2R\sin(\delta/2)-\|e'\|_\infty\delta\\
 &>\left(\frac{2(57/20)}{22/7}-\frac34\right)b\delta
  =\frac{117}{110}b\delta>b\delta .
\end{aligned}
\tag{24}
$$

严格不等式在 $\delta>0$ 时理解；$\delta=0$ 时两边同为零。
因此 $c_0$ 是嵌入圆周，而不是一个可能重走或自交的闭参数图。
这里的 $\pi<22/7$ 可直接由
$22/7-\pi=\int_0^1 x^4(1-x)^4/(1+x^2)\,dx>0$ 得到。

由 (12)，中心曲线的水平二阶导数范数至多
$R+49P+25Q=2R<6b$，竖直二阶导数范数小于 $3b$。故

$$
\|c_0''\|_\infty<3\sqrt5\,b<\frac{27}{4}b<7b.
\tag{25}
$$

在 $p=c_0(\theta)$ 处取任意单位法向量 $\nu\perp c_0'(\theta)$。
对最短参数弧作二阶 Taylor 积分，利用 (24)，得到

$$
2|\nu\cdot(q-p)|
 \le 7b\delta^2\le\frac7b|q-p|^2
\quad (q=c_0(\phi)).
\tag{26}
$$

这直接证明 $\operatorname{reach}(c_0)\ge b/7$：
若 $p$ 是离某点 $x$ 最近的中心曲线点，曲线无边，所以
$x-p\perp c_0'(\theta)$；令 $r=|x-p|<b/7$，则对任何 $q\ne p$，

$$
|x-q|^2-|x-p|^2
 =|q-p|^2-2(x-p)\cdot(q-p)
 \ge(1-7r/b)|q-p|^2>0.
\tag{27}
$$

最近点存在由紧性保证，故半径 $b/7$ 内最近点唯一。

取环带半宽

$$
w=\frac b{20},\qquad M=[-w,w]\times(\mathbb R/\ell\mathbb Z).
\tag{28}
$$

由于 $d_0\perp c_0'$ 且 $|d_0|=1$，(26)–(27) 说明
$c_0(\theta)$ 是 $\widetilde F_0(v,\theta)$ 的唯一中心曲线最近点，
对全部 $|v|\le w$ 成立。若两个环带位置相等，其中心曲线最近点相等，
由 (24) 得角相同，再由 $|d_0|=1$ 得 $v$ 相同。
结合 (14) 的满秩及参数域紧性，$F_0:M\to\mathbb R^3$ 是一个实际
正宽的 $C^\infty$ 嵌入，含其两条边界。

## 5. 保持闭合和同一弧长的具体可变球面族

仅有一个零向量面积方向曲线还不构成弯曲族。本节给出实际非零维的约束族。

### 5.1 明确的自由方向和四个控制方向

在第一扇区 $[0,\omega]$ 内，选两段不交开区间

$$
J_0=(\omega/8,\omega/4),\qquad
J_1=(3\omega/8,5\omega/8).
\tag{29}
$$

对 $p<q$ 定义归一化光滑 bump

$$
B_{p,q}(\theta)=
\begin{cases}
\displaystyle
\exp\!\left(1-\frac{(q-p)^2}{4(\theta-p)(q-\theta)}\right),
       &p<\theta<q,\\
0,&\text{其他}.
\end{cases}
\tag{30}
$$

它在端点平坦、内部严格正、中点等于 $1$。令 $h=B_{J_0}$、
$\chi=B_{J_1}$。设

$$
g_1=(d_0)_x,\quad g_2=(d_0)_y,\quad
g_3=(d_0)_z,\quad g_4=\kappa_0,\qquad
f_j=\chi g_j.
\tag{31}
$$

(31) 首先只在第一扇区定义；然后把 $h$ 及四个 $f_j$ 按 $\omega$ 周期
重复到全圈。因为支撑远离扇区端点，这一重复是 $C^\infty$ 的。
**不能**把全球的 $(d_0)_x,(d_0)_y$ 直接当成周期标量控制；
这里使用的是第一扇区函数的周期复制。

令 $n_0=d_0\times d_0'/k_0$。对实参数 $\tau$ 和
$\alpha=(\alpha_1,\ldots,\alpha_4)$，定义

$$
\begin{aligned}
f_{\tau,\alpha}&=\tau h+\sum_{j=1}^4\alpha_j f_j,\\
d_{\tau,\alpha}
 &=\cos(f_{\tau,\alpha})d_0+\sin(f_{\tau,\alpha})n_0.
\end{aligned}
\tag{32}
$$

该式恒为单位向量，恒有 (4) 的 $C_3$ 等变性，并在参数充分小时正则。
在三个扇区端点的固定开邻域，它逐点等于 $d_0$。

### 5.2 四个实际约束及 Jacobian

对第一扇区定义向量面积和球面长度

$$
\mathcal A(d)=\int_0^\omega d\times d'\,d\theta\in\mathbb R^3,\qquad
\mathcal L(d)=\int_0^\omega |d'|\,d\theta.
\tag{33}
$$

我们要求四个实等式

$$
\mathcal A(d_{\tau,\alpha})=\mathcal A(d_0),\qquad
\mathcal L(d_{\tau,\alpha})=\mathcal L(d_0).
\tag{34}
$$

固定整个扇区向量面积比仅固定全圈竖直向量面积更强；它用于保持 C3 轴、
位置锚点及三个固定材料片，不是额外留待验证的假设。

若 $\delta d=f n_0$ 且 $f$ 在端点附近为零，分部积分和 (18) 给

$$
\begin{aligned}
\delta\mathcal A
 &=\int_0^\omega(\delta d\times d_0'
                   +d_0\times\delta d')\,d\theta
   =-2\int_0^\omega f k_0d_0\,d\theta,\\
\delta\mathcal L
 &=-\int_0^\omega f k_0\kappa_0\,d\theta .
\end{aligned}
\tag{35}
$$

因此 (34) 的左端减右端对 $\alpha$ 的 Jacobian，在 $(0,0)$ 处为

$$
-\operatorname{diag}(2,2,2,1)\,G,\qquad
G_{ij}=\int_0^\omega\chi k_0g_i g_j\,d\theta .
\tag{36}
$$

下面证明 $G$ 严格正定，避免用一次浮点行列式替代可逆性。

### 5.3 四个函数的解析线性无关性

若 $\sum_{j=1}^4\lambda_jg_j=0$ 在 $J_1$ 的某开区间成立，
各 $g_j$ 都实解析，故关系延至全圈。对 $\theta,\theta+\omega,
\theta+2\omega$ 的关系相加，由 (4) 及 $\kappa_0$ 的 $\omega$ 周期性，
有 $\lambda_3(d_0)_z+\lambda_4\kappa_0=0$。余下
$\lambda_1(d_0)_x+\lambda_2(d_0)_y=0$；取 $\theta=0,\omega$，
因 $\eta\ne0$，相应水平向量线性无关，故 $\lambda_1=\lambda_2=0$。

在 $(d_0)_z\ne0$ 处，由 (21)

$$
\frac{\kappa_0}{(d_0)_z}
 =\frac{17+3\eta+X}{(8+X)^{3/2}}=:\Phi(X).
\tag{37}
$$

并且

$$
\Phi'(X)
 =\frac{8-\tfrac32(17+3\eta)-X/2}{(8+X)^{5/2}}<0
\quad (0\le X\le\sigma^2).
\tag{38}
$$

$X(\theta)$ 不恒定，因此 (37) 不恒定，迫使
$\lambda_3=\lambda_4=0$。四个函数在任一非空开区间线性无关。

现在对任意非零向量 $\lambda\in\mathbb R^4$，

$$
\lambda^TG\lambda
 =\int_{J_1}\chi k_0\left(\sum\lambda_jg_j\right)^2d\theta>0.
\tag{39}
$$

权函数在 $J_1$ 内严格正；若积分零，则解析组合在该区间恒零，与刚证的
无关性矛盾。这证明 (36) 可逆。

### 5.4 得到真实连续族

(33)–(34) 定义的是一个具体 $C^\infty$ 有限维映射
$\mathbb R\times\mathbb R^4\to\mathbb R^4$。
由可逆的 (36)，通常的有限维隐函数定理给出 $\varepsilon>0$ 和唯一的
局部 $C^\infty$ 函数 $\alpha(\tau)$，满足

$$
\alpha(0)=0,\qquad
|\tau|<\varepsilon\Longrightarrow\text{(34) 成立}.
\tag{40}
$$

这不是“若找到某个可逆控制则存在”的条件陈述：控制、约束及严格可逆性
都已经指定并证明。记 $d_\tau=d_{\tau,\alpha(\tau)}$、
$k_\tau=|d_\tau'|$。当前证明不提供有效的 $\varepsilon$ 数值；不能据此
任意挑选一个数值振幅并声称已经验证。

## 6. 变形后的真实位置闭合与共同材料 gauge

以基础中心曲线的同一个空间点为锚，定义

$$
c_\tau(\theta)
 =c_0(0)+b\int_0^\theta d_\tau\times d_\tau'\,dx.
\tag{41}
$$

由 (34)，

$$
c_\tau(\omega)
 =c_0(0)+b\mathcal A(d_0)=c_0(\omega)=R_z(\omega)c_0(0).
\tag{42}
$$

又因 $d_\tau\times d_\tau'$ 对 $\omega$ 移位按 $R_z(\omega)$ 变换，
两边对 $\theta$ 求导并在 $\theta=0$ 比较，得

$$
c_\tau(\theta+\omega)=R_z(\omega)c_\tau(\theta).
\tag{43}
$$

重复三次给 $c_\tau(\theta+2\pi)=c_\tau(\theta)$。因此每个时间的全圈
位置都闭合，且 C3 轴、原点与锚点固定。

再令

$$
u_\tau(\theta)=\int_0^\theta k_\tau(x)\,dx.
\tag{44}
$$

长度约束给

$$
u_\tau(\theta+\omega)=u_\tau(\theta)+\ell/3,\qquad
u_\tau(\theta+2\pi)=u_\tau(\theta)+\ell .
\tag{45}
$$

取逆函数 $\theta_\tau(u)$，在固定域 (28) 定义

$$
\boxed{F_\tau(v,u)=
c_\tau(\theta_\tau(u))+v\,d_\tau(\theta_\tau(u)).}
\tag{46}
$$

所有 $F_\tau$ 恰诱导同一个 (17)，并满足

$$
F_\tau(v,u+\ell/3)=R_z(\omega)F_\tau(v,u).
\tag{47}
$$

该族关于 $(\tau,v,u)$ 联合 $C^\infty$。所有时间的等距误差在精确数学中
为零，而不是某个薄宽、频率或层数极限下才消失的缺陷。

## 7. 全时间正宽嵌入以及有边曲面的 reach

由 $C^\infty$ 连续依赖，把 $\varepsilon$ 缩小，使全部时间满足

$$
\|c_\tau'-c_0'\|_\infty\le b/40,\qquad
\|c_\tau''-c_0''\|_\infty\le b/4.
\tag{48}
$$

注意这些导数都是原角 $\theta$ 的导数。用同一最短角弧，在 (24) 中减去
$(b/40)\delta$，得到

$$
|c_\tau(\theta)-c_\tau(\phi)|\ge b\delta,\qquad
\|c_\tau''\|_\infty<7b.
\tag{49}
$$

其中余量由 $117/110-1/40>1$ 及 $27/4+1/4=7$ 保证。
(26)–(27) 的全部证明逐字适用每个 $c_\tau$，故其 reach 统一至少 $b/7$。
又有 $d_\tau\perp c_\tau'$，所以全部 $F_\tau$ 在相同正半宽 $w=b/20$
上都是嵌入。这里没有通过“嵌入开性”暗中令宽度随时间趋零。

下面给出环带本身的一个粗但明确的 reach 界，并包含边界最近点条件。
基础曲线满足 $|d_0'|<3$；由 (2) 连续求导，
$|d_0''|\le1+6+9=16$。再缩小 $\varepsilon$ 可令

$$
|d_\tau'|\le4,\qquad |d_\tau''|\le20
\tag{50}
$$

对全部时间和角成立。

令 $x=p+v d_\tau(\theta)$、$y=q+\widehat v d_\tau(\phi)$，
其中 $p=c_\tau(\theta)$、$q=c_\tau(\phi)$。
分别在 $p,q$ 用 (26) 的法向弦估计，得到

$$
(x-y)\cdot(p-q)
 \ge(1-7w/b)|p-q|^2=\frac{13}{20}|p-q|^2.
\tag{51}
$$

故 $|p-q|\le(20/13)|x-y|$。再用 (49)–(50)，

$$
\begin{aligned}
b\delta&\le\frac{20}{13}|x-y|,\\
|v-\widehat v|
 &\le |x-y|+|p-q|+w|d_\tau(\theta)-d_\tau(\phi)|\\
 &\le |x-y|+(1+4w/b)|p-q|
 \le\frac{37}{13}|x-y|.
\end{aligned}
\tag{52}
$$

在缩放参数 $\zeta=b\theta$ 下，最短参数线段的位移 $h$ 因而满足

$$
|h|^2=(v-\widehat v)^2+b^2\delta^2
 \le\frac{1769}{169}|x-y|^2.
\tag{53}
$$

位置式 $\widetilde F_\tau(v,\zeta)=c_\tau(\zeta/b)+v d_\tau(\zeta/b)$ 的
Hessian 有

$$
\widetilde F_{vv}=0,\quad
|\widetilde F_{v\zeta}|\le4/b,\quad
|\widetilde F_{\zeta\zeta}|\le8/b.
\tag{54}
$$

其任意单位方向二阶导数范数至多
$(4+4\sqrt2)/b<10/b$。这是对方向二次型的界，非逐项相加漏掉混合项。

取任意空间点 $z$，令 $p=F_\tau(P)$ 为一个最近环带点、$r=|z-p|$。
对任意另一参数点 $Q$，取最短角 lift 并把径向坐标线性插值。
以下在这一 lift 中把 $P,Q$ 也表示为 $(v,\zeta)$ 坐标，令 $h=Q-P$。
整个参数线段留在闭条带 $[-w,w]$ 内。
即便 $P$ 在边界 $v=\pm w$，距离平方在该可行线段起点的右导数也非负，
所以

$$
(z-p)\cdot D\widetilde F_\tau(P)h\le0.
\tag{55}
$$

这里没有把 $z-p$ 错当成边界处仅一维的曲面法向，也没有套用无边曲面的
法锥论证。结合 Taylor 余项 (54) 和空间弦长换元 (53)，

$$
(z-p)\cdot(F_\tau(Q)-p)
 \le \frac r2\,\frac{10}{b}\,\frac{1769}{169}
       |F_\tau(Q)-p|^2 .
\tag{56}
$$

因此若 $r<169b/17690$，每个 $Q\ne P$ 都给严格更大的距离。
紧性保证最近点存在，故

$$
\boxed{\operatorname{reach}(F_\tau(M))
\ge \frac{169}{17690}b\quad\text{对所有 }|\tau|<\varepsilon.}
\tag{57}
$$

(53) 中的 co-Lipschitz 常数在 (56) 中必须取平方；(57) 已包含该平方。
这只是保守的已证下界，不足以支付题目按整个直径归一的 $0.03D$ 门，
也不声称实际 reach 只有这个大小。

## 8. 真正固定的材料片及其直径

由于两个 bump 支撑都避开各扇区端点，且 (34) 固定每个扇区的总向量面积
和总长度，(41)、(44) 在各 $\theta=j\omega$ 的小开邻域与基础函数完全
相同。特别是在

$$
|\theta-j\omega|\le\omega/32,\qquad j=0,1,2
\tag{58}
$$

所代表的三个闭角区，$d_\tau=d_0$、$c_\tau=c_0$、
$u_\tau=u_0$。对 $\theta=0$ 的跨周期邻域也成立：可向负角积分，或用
完整扇区约束和周期性。

取固定材料闭集

$$
H=\left\{(v,u_0(\theta)):
 |v|\le w/2,\
 \theta\text{ 属于 (58) 的三个角区}\right\}.
\tag{59}
$$

$H$ 有非空内部，并对所有时间逐点满足 $F_\tau|_H=F_0|_H$。
它包含三个中心线点 $c_0(j\omega)$，这些点高度为零，水平半径为
$R+P+Q>57b/20$。任意两点距离为 $\sqrt3(R+P+Q)$，故

$$
\operatorname{diam}F_0(H)>\frac{171}{40}b.
\tag{60}
$$

另一方面，$P+Q<b/10$、$|(c_0)_z|<b/10$、$R<3b$，
且 $w=b/20$，所以整个基础环带直径 $D$ 满足

$$
D<2(3+1/10+1/10+1/20)b=\frac{13}{2}b.
\tag{61}
$$

由此

$$
\frac{\operatorname{diam}F_0(H)}D>\frac{171}{260}>\frac15.
\tag{62}
$$

该直径用的是整个环带的 $D$；未以环宽或中心线长度偷换归一量。

## 9. 非刚体且两像在全 E(3) 下不全等

### 9.1 材料位置族确实不恒定

在 $J_0$ 内，四个控制方向全部为零；取其中 $h(\theta_*)>0$ 的一点。
由 (32)，在 $\tau=0$ 的方向曲线变分为
$h(\theta_*)n_0(\theta_*)$。改为固定材料弧长
$u_*=u_0(\theta_*)$ 后，重参数化的一阶变化只加上
$d_0'(\theta_*)$ 的倍数，故仍有

$$
n_0(\theta_*)\cdot
\left.\frac{d}{d\tau}
d_\tau(\theta_\tau(u_*))\right|_{\tau=0}
=h(\theta_*)>0.
\tag{63}
$$

再次缩小 $\varepsilon$，对每个 $0<|\tau|<\varepsilon$，
$\partial_vF_\tau$ 不等于 $\partial_vF_0$，因此 $F_\tau\ne F_0$。
这不是材料点沿同一个像任意滑动的证明；像不全等需要下一步。

### 9.2 共同环带度量的全部内在自等距

令 $\Psi:M\to M$ 是 (17) 的任一光滑自等距。由 (20)，$K(v)$ 严格决定
$|v|$，所以它的第一坐标的绝对值等于 $|v|$。
在两个连通半环带分别只能选一个符号；跨 $v=0$ 的光滑性与可逆性迫使
两侧符号一致。因此其第一坐标为 $\epsilon v$，$\epsilon=\pm1$。

将第二坐标局部 lift 写为 $U(v,u)$。比较 $dv^2$ 系数：

$$
1+(b^2+v^2)U_v^2=1,
$$

所以 $U_v=0$。再比较 $du^2$ 系数得 $U_u^2=1$；
其符号在连通域上恒定。于是全部自等距恰为

$$
\Psi(v,u)=(\epsilon v,\rho u+\beta),
\qquad \epsilon,\rho\in\{1,-1\},\
\beta\in\mathbb R/\ell\mathbb Z.
\tag{64}
$$

这也包含交换两条边界、角向反射等情况。

### 9.3 刚体全等会迫使整张材料图相同

若存在任意欧氏等距 $A\in\mathrm E(3)$，使
$A(F_\tau(M))=F_0(M)$，因两图嵌入，
$\Psi=F_0^{-1}\circ A\circ F_\tau$ 是 (17) 的内在自等距，故有 (64)。
在固定开片 $\operatorname{int}H$ 上，

$$
A\circ F_0=F_0\circ\Psi.
\tag{65}
$$

$F_0$ 在 $(v,u)$ 上实解析，$\Psi$ 的式 (64) 也实解析。
因此 (65) 从非空开片解析延拓到整个连通环带内部，再由连续性到边界。
而 $A\circ F_\tau=F_0\circ\Psi$ 本来就处处成立，所以
$A\circ F_\tau=A\circ F_0$，即 $F_\tau=F_0$，与 (63) 矛盾。

故对全部充分小的非零 $\tau$，

$$
F_\tau(M)\ \text{与}\ F_0(M)\ \text{在全 }\mathrm E(3)
\text{ 下不全等}.
\tag{66}
$$

这里没有只排除保持材料标号的刚体，也没有漏掉反射。
对两紧像，欧氏群上的 Hausdorff 距离下确界可以限制到有界平移及紧正交群，
所以最小值能取到；若最小值为零就会全等。因此 (66) 严格给
$\min_A d_H(AF_\tau(M),F_0(M))>0$。不作刚体对齐的像 Hausdorff
距离也严格正。当前没有证明其达到 $0.05D$，材料点的一阶移动没有被冒充
成所需像位移下界。

如需标准时间区间，可任取 $0<\tau_*<\varepsilon$，再令
$\tau=\tau_*t$、$t\in[0,1]$。全部上述性质保持；$\tau_*$ 的有效数值与
可见振幅仍是下一项定量任务。

## 10. 真实接合缺口

本构造已经提供：

- 一条明确的闭合嵌入空间中心曲线；
- 正半宽 $b/20$ 的全圈 $C^\infty$ 嵌入环带；
- 指定控制和严格可逆 Jacobian 产生的实际非刚体连续族；
- 同一个精确径向共同度量、材料 C3、逐点固定的三片开放握持区；
- 全时间正宽嵌入和包含边界的统一 reach 下界；
- 包含反射的全欧氏群下的严格像非全等。

但固定 $b>0$ 时，(20) 对全部有限 $v$ 都严格负。
R43 的整个三柱弯圆盘内在平坦；一个 $C^2$ 正则接合的高斯曲率须连续。
因此本稿不能把任何边界直接当作 R43 的共同两 jet 接缝。
令 $|v|\to\infty$ 才使 $K\to0$ 也不是一个有限位置、有限度量的已完成端点。
更改 $b$ 为径向函数会破坏本稿的等距与闭合推导，需另行实际构造。

基础环带的任何常 $v$ 材料圈也不在任一平面内：其水平坐标中频率 $1$
的系数由 (8) 非零，竖直坐标只有频率 $3,6$；任何平面方程的频率 $1$
项先迫使水平法向为零，而非零的 $\sin6\theta$ 项再迫使竖直法向为零。
所以也不能经刚体对齐就把它当作水平活动核心的边圈；当前没有核心位置、
一 jet 或两 jet 的接合。

若之后保留 R38 的特定 $a=1+A_4s^4>1$ 鞍领来接小半径平环，已有径向
转折要求仍适用于那条接线。本稿没有把该要求推广到所有可能的新中段。

本稿不声称封闭曲面已存在，也不支付题目中的闭性、可见像振幅或
$0.03D$ reach 门。它新增的是一个实际闭圈、正宽且可变的负曲率中段模块；
两侧连接和可见幅度仍必须在同一个精确几何中完成。

## 11. 可复现检查与证据边界

原环境附属程序的路径为
scripts/db6f-geometry-explicit-ruled-saddle-annulus.py。
该程序与当时报告的持久可读性须在环境恢复后重新核实，以下仅记录它已观测的
检查范围与原运行方式，不把路径文字当作已封存源码。
程序
在 Laurent 多项式环中直接从 (3) 重建单位范数、速度、叉乘、零向量面积、
闭曲线原函数、三项度量和曲率三重积；另核移动标架、变分公式、导数消元及
上述有理门。调用方式为：

    python topics/visible-flexible-closed-surface/scripts/db6f-geometry-explicit-ruled-saddle-annulus.py --output topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-geometry-explicit-ruled-saddle-annulus.json

程序报告记录源文件哈希，且明确区分已机核的有限恒等式与本文的解析证明。
Gram 严格正定、隐函数族、全局嵌入、边界 reach 和全 $\mathrm E(3)$
非全等依赖本文完整论证；程序没有用浮点试验替代这些论证，也没有生成一个
未经有效参数半径验证的数值时间区间。此脚本不读主候选，不做 BVP、
tail、RK 或优化，不生成网格。

本稿各项专用于本构造的闭合、嵌入、约束可解和非全等论证均已写出，
其通用分析工具为有限维隐函数定理及实解析恒等原则。

恢复期间另核了经典背景：$c'=b\,d\times d'$ 是 Koenigs–Darboux
表示的一种参数形式，见 Larry M. Bates、O. Michael Melko，
*On curves of constant torsion I*（2012），§1 式 (1.1)、§1.1
Proposition 1.1；[原论文 HTML](https://arxiv.org/html/1206.7086v1)。
该文 §2 还用另一些球面 epicycle 构造闭曲线，其中有处处正曲率的例子，
所以不能泛称闭常挠率曲线必有拐点。本稿不借该文的图示替代 (24) 的嵌入
证明，也不把其单曲线构造当作本稿四约束等距族的证明。此次只在线读 HTML，
未下载或渲染 PDF。
