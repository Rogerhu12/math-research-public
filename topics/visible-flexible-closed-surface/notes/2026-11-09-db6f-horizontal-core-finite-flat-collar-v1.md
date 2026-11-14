# 从实际水平核心出发：有限平坦领与全 jet 贴柱

**状态：完整作者推导，待独审。** 2026-11-09，独立几何分工。
这是新独立应用稿，不修改已冻结的正 C epicycle 稿或原固定 H 鞍环稿。
不读取主优化数组，不运行 BVP、tail、RK，不声称存在本稿的终端求解轨迹。

本文把有限平坦截止直接接在真实水平核心的位置和框架上。
给两种不同而明确的选择：一种从同一核心出发得到 $C^\infty$ 全 jet 贴柱；
另一种保留 R38 已审的特定四阶鞍领，在一个开内领上与其完全相同，
但贴原柱带处只沿用其已证的 $C^2$ 结论。
两种选择都到达有限正宽的平坦仿射领，且周期位置真实闭合。

出口仍有 $a>1$、小锥角和非零第二基本形式；不是 R43 的平圆环，也没有
闭曲面。这里的角解析族不提供固定开握持区。不能将这个新共同度量计入
任何既定主候选的网格加密或 G5 收敛序列。

## 1. 已固定的来源

- R38，[已审核心及四阶鞍领](../results/R38-ck-local-exact-isometric-collar.md)：
  实解析单位速率凸闭曲线 $\gamma$、初始 $F_s=e_z$、$M=0$、
  $C=\kappa_\gamma>0$ 及完整两 jet。
- [正 C epicycle 有限平坦领作者稿，固定提交 0239fffd](https://github.com/Rogerhu12/math-research/blob/0239fffd6e5206dfadb778db4ba5a057e01cfc5a/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-epicycle-finite-flat-collar-v1.md)，
  尤其 §§8–10 的统一解析尺度界、框架位置重构及有边弦长论证。
  本文仍把该稿当作作者证明，未提前宣称它已独审通过。
- Nishida，Orsay 78.02，
  *Nonlinear Hyperbolic Equations and Related Topics in Fluid Dynamics*，
  Chapter III §2，Hypothesis 2.1、Theorem 2.1，印刷 pp.64–65；
  pp.72–73 说明演化变量只需连续的一阶拟线性应用：
  [作者讲义正文](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/bb/b2/bbb2303a-1e17-4807-a319-290a5b030b2f/n_nishida-102.pdf)。
  仅在线读文本，未下载或渲染 PDF。

下文不把“Nishida 可用”留为条件清单：给出实际核心、实际度量、
分母下界、一致尺度估计的依赖、位置初值、完整周期和嵌入。

## 2. 一个具体的共同长度水平核心族

令 $\lambda\in[1/32,1/16]$。以外法向角 $\varphi$ 定义支持函数

$$
h_\lambda(\varphi)=1+\lambda\cos3\varphi,\qquad
\rho_\lambda=h_\lambda+h_\lambda''
=1-8\lambda\cos3\varphi.
\tag{1}
$$

因此 $1/2\le\rho_\lambda\le3/2$。实际平面曲线为

$$
\widetilde\gamma_\lambda(\varphi)
=h_\lambda e_r(\varphi)+h_\lambda' e_\varphi(\varphi).
\tag{2}
$$

它严格凸、解析、C3，并有
$\widetilde\gamma_\lambda'=\rho_\lambda e_\varphi$。
其周长恒为 $2\pi$，不是事后缩放。
真实单位速率材料角为

$$
\theta=\Theta_\lambda(\varphi)
=\varphi-\frac{8\lambda}{3}\sin3\varphi,\qquad
\gamma_\lambda(\theta)=
\widetilde\gamma_\lambda(\Theta_\lambda^{-1}(\theta)).
\tag{3}
$$

因 $\Theta_\lambda'=\rho_\lambda\ge1/2$，
逆函数及曲率
$\kappa_\lambda(\theta)=1/\rho_\lambda(\Theta_\lambda^{-1}(\theta))$
对 $\theta,\lambda$ 联合实解析，并有共同复邻域及

$$
|\gamma_\lambda'|=1,\qquad \frac23\le\kappa_\lambda\le2.
\tag{4}
$$

共同复邻域由紧参数区间和角圆周上的解析逆函数定理取得；
不存在把外法向角误当弧长材料角的步骤。
C3 移位满足
$\gamma_\lambda(\theta+2\pi/3)=R_{2\pi/3}\gamma_\lambda(\theta)$。

固定一个实际柱带

$$
F_\lambda^{\rm cyl}(s,\theta)=\gamma_\lambda(\theta)+s e_z,
\qquad -h_0\le s\le0,\quad h_0=1/10.
\tag{5}
$$

其共同精确度量为 $ds^2+d\theta^2$。任一已审 R38 的解析凸核心也可替换
这里的 $\gamma_\lambda$；本节给具体族，是为了使新存在结论有完整实例。
若实际接口在预先固定的高度 $z_0$，就在 (5)、(8) 的全部初始位置统一加
$z_0e_z$；同一个常数随解保留，不能在出口再独立改高度。
替换为 R38 相位族时，后述解仍只是整体旋转的活动族，
不能因此宣称 $\delta_E>0$；本文具体振幅族另在 §8 给非全等证明。

## 3. 全 jet 贴柱的明确 C∞ 度量

取 $E(s)=e^{-1/s^2}$（$s>0$），$E(s)=0$（$s\le0$）。
选固定光滑函数 $0\le\psi\le1$，在 $x\le1/4$ 为 $1$，
在 $x\ge3/4$ 为 $0$，可用前述 epicycle 稿 §7 的明确指数比公式。

对尚待选择的小 $\epsilon>0$ 定义

$$
a_\epsilon''(s)=E(s)\psi(s/\epsilon),\qquad
a_\epsilon(s)=1+\int_0^s(s-r)a_\epsilon''(r)\,dr.
\tag{6}
$$

于是：

- $a_\epsilon=1$ 在 $s\le0$，所有正向差 jet 在 $0$ 也为零；
- $a_\epsilon''>0$ 在 $0<s<3\epsilon/4$；
- $a_\epsilon$ 在 $s\ge3\epsilon/4$ 为严格正斜率的仿射函数；
- $a_\epsilon,a_\epsilon',a_\epsilon''$ 在固定窗 $|s|\le1/4$ 上满足
  $1\le a_\epsilon<2$、$|a_\epsilon'|<1$、
  $|a_\epsilon''|\le1$，与 $\epsilon$ 无关。

共同度量指定为

$$
g_\epsilon=ds^2+a_\epsilon(s)^2d\theta^2.
\tag{7}
$$

这是一个固定 $\epsilon$ 后全时间不变的精确度量。不要求高阶截止导数随
$\epsilon\to0$ 一致有界；它们不进入下面的统一寿命界。

## 4. 合法的角解析、径向光滑演化

以初始法向 $n_0=e_z\times\gamma_\lambda'$ 为内法向，
实际 Cauchy 位置与标架是

$$
F(0,\theta,\lambda)=\gamma_\lambda(\theta),\qquad
e_1=e_z,\quad e_2=\gamma_\lambda',\quad N=n_0.
\tag{8}
$$

第二形式初值为 $M_0=0,C_0=\kappa_\lambda>0$。
对 (7)，完整 Gauss–Codazzi 正常形为

$$
L=\frac{M^2-a_\epsilon a_\epsilon''}{C},\qquad
M_s=L_\theta-\frac{a_\epsilon'}{a_\epsilon}M,\qquad
C_s=M_\theta+\frac{a_\epsilon'}{a_\epsilon}C+
           a_\epsilon a_\epsilon' L.
\tag{9}
$$

这是一阶 $s$、一阶 $\theta$ 系统；没有对二阶角位置方程错误调用 CK。

给出统一性核验的具体依赖。初值 $\mathcal U_0=(0,\kappa_\lambda)$
在某个共同复角条带及复参数邻域全纯，较小条带上可令 $|C_0|\ge1/3$。
取 $c=1/6$、增量半径 $\mathcal R\le c$；于是球内 $|C|\ge c$。
令 $B$ 是稍宽条带上的初值范数，$B_1=B+\mathcal R$。
由 §3 的三个径向界，球内

$$
|L|\le L_*=(B_1^2+2)/c .
\tag{10}
$$

实际主矩阵和零阶项为

$$
A=
\begin{pmatrix}2M/C&-(M^2-aa'')/C^2\\1&0\end{pmatrix},
\qquad
B_0=
\binom{-(a'/a)M}{(a'/a)C+aa'(M^2-aa'')/C}.
\tag{11}
$$

它们及未知量一阶导数的界只依赖 $B_1,c$ 和 $a,a',a''$。
在周期解析上确界尺度 $X_\rho$ 上，
$\|\partial_\theta f\|_{\rho'}\le
\|f\|_\rho/(\rho-\rho')$，因此对增量右端有

$$
\|\mathcal F_\epsilon(s,V)-\mathcal F_\epsilon(s,W)\|_{\rho'}
\le\frac{C_*}{\rho-\rho'}\|V-W\|_\rho,\qquad
\|\mathcal F_\epsilon(s,0)\|_\rho\le K_* ,
\tag{12}
$$

其中 $C_*,K_*$ 对全部 $\epsilon$ 及全部本节参数一致。
例如与 epicycle 稿相同，可取
$\Lambda=100(1+B_1)^3(1+c^{-3})$，
$C_*=\Lambda(2+\mathcal R+B/\rho_0)$、
$K_*=\Lambda(1+B/\rho_0)$，其中初值在 $2\rho_0$ 条带有范数 $B$。
$\lambda$ 可作为全纯被动变量加入 Banach 空间；
也可用紧参数区间的有限复邻域覆盖和唯一性取得同一个时间。

(12)、球中分母下界及 $s$ 连续性验证了 Nishida Hypothesis 2.1。
其 Theorem 2.1 先给一个对所有截止共同的 $T_*>0$，
只依上述界和固定窗，不依 $a_\epsilon'''$ 或更高导数。
现在才选择

$$
0<\epsilon<\min(10^{-2},T_*/2).
\tag{13}
$$

因此整个有限平坦截止都包含在真正已解的区间中。
对固定 $\epsilon$，方程系数关于 $s$ 为 $C^\infty$；
在较小解析条带中微分方程即得联合 $C^\infty$ 解。
真实性、周期性及 C3 标量周期由唯一性保持。

这里初始 $a''(0)=0$ 不是障碍：正常形只除以 $C$，没有除以
高斯曲率或 $a''$。这不适用于 R43 的整开角区 $C=0$ 数据。

## 5. 全 jet 贴柱与真实周期位置

用 (8) 作实际初值，解径向标架和位置系统

$$
F_s=e_1,\quad
(e_1)_s=L N,\quad
(e_2)_s=(M/a)N,\quad
N_s=-L e_1-(M/a)e_2.
\tag{14}
$$

Gauss–Codazzi 保证角方程

$$
F_\theta=ae_2,\quad
(e_1)_\theta=a'e_2+MN,\quad
(e_2)_\theta=-a'e_1+(C/a)N,\quad
N_\theta=-M e_1-(C/a)e_2
\tag{15}
$$

成立：差量对 $s$ 满足齐次线性系统，初值由平面 Frenet 公式为零。
因此 (7) 的所有度量分量精确成立。
周期初值和周期系数使 (14) 逐点 ODE 的唯一性同时保持框架、位置周期；
位置不是另有一个未核对的沿角积分。
相同论证保持实际空间 C3 等变。

在 $s<0$，$a=1,a'=a''=0$，而 $M=0,C=\kappa_\lambda(\theta)$
是 (9) 的解。唯一性使它就是所解的同一解；
(14) 因而给 $F=\gamma_\lambda+s e_z$。
联合 $C^\infty$ 性说明在 $s=0$ 的每阶 Cartesian jet 都与柱面相同。
所以 (5) 与正向领的贴接是 $C^\infty$，没有只配二阶或平均值。
将负向精确柱带延到 $s=-h_0$ 时，重叠开带上位置完全相同。

此解既固定了核心位置，也固定了核心的一 jet 和两 jet。
它没有任意平移出口以匹配另一个几何模板的自由度。

## 6. 同一个正宽度上的全时间嵌入与边界 reach

先给出核心的统一全局弦长。对外法向角最短差
$\Delta_\varphi\le\pi$，把 (2) 的弦投影到角中点的切向，
利用 $\rho_\lambda\ge1/2$ 得

$$
|\gamma_\lambda(\theta)-\gamma_\lambda(\widehat\theta)|
\ge\sin(\Delta_\varphi/2)\ge\Delta_\varphi/\pi .
$$

最短材料差 $\Delta_\theta$ 不大于沿该外法向角弧的长度，
所以 $\Delta_\theta\le(3/2)\Delta_\varphi$。故

$$
|\gamma_\lambda(\theta)-\gamma_\lambda(\widehat\theta)|
\ge\frac{2}{3\pi}\Delta_\theta>\frac15\Delta_\theta.
\tag{16}
$$

直柱比较图 $B_\lambda(s,\theta)=\gamma_\lambda(\theta)+s e_z$
于是对全参数域有 co-Lipschitz 常数 $1/5$。

由 (14)，在新领 $0\le s\le\epsilon$ 上
$|F_s-e_z|\le L_*\epsilon$。
由 (15)，
$F_{\theta s}=a'e_2+MN$，初始 $F_\theta=\gamma_\lambda'$，
所以
$|F_\theta-\gamma_\lambda'|\le(1+B_1)\epsilon$。
令 $C_1=L_*+1+B_1$，进一步把同一个 $\epsilon$ 缩到

$$
\epsilon C_1<1/10.
\tag{17}
$$

在整个 $[-h_0,\epsilon]\times S^1$ 上，
导数差在负向柱带为零，在正向领满足该界。
沿最短角 lift 的可行参数直线段积分，
结合 (16) 得空间弦长至少参数距离的 $1/10$。
所以全部 $\lambda\in[1/32,1/16]$ 在同一固定材料域上嵌入。

由 (14)–(15)，方向 Hessian 范数可统一取
$M_*=L_*+4+3B_1$；负向柱带的 $\kappa_\lambda\le2$
也被这个界覆盖。最近点即使在 $s=-h_0$ 或 $s=\epsilon$ 的边界，
沿通向另一参数点的可行线段仍有单侧极小条件。
Taylor 余项与空间 co-Lipschitz 常数平方给

$$
\operatorname{reach}(F_\lambda)\ge\frac{1}{100M_*}>0
\quad\text{对全部 }\lambda.
\tag{18}
$$

具体地，若 $p=F(P)$ 最近于 $z$，单侧导数给
$(z-p)\cdot DF(P)h\le0$，
而 $|h|^2\le100|F(Q)-p|^2$；
于是
$2(z-p)\cdot(F(Q)-p)\le100|z-p|M_*|F(Q)-p|^2$，
小于所示半径时另一点不可能同样近。
这是有边曲面的最近点证明，不把单个无边法向界直接叫作 reach。
当前 $M_*$ 没有数值化，未声称达到归一直径的 $0.03$ 门。

## 7. 确实保留 R38 旧四阶领的另一个版本

若需要保留已经审定的 $a(s)=1+A_4s^4$、固定 $A_4>0$，
不要用 (6) 冒充该同一度量。另取

$$
a_\epsilon''(s)=12A_4s^2\psi(s/\epsilon),\qquad
a_\epsilon(0)=1,\quad a_\epsilon'(0)=0.
\tag{19}
$$

在 $0\le s\le\epsilon/4$ 上，(19) 恰等于 R38 的度量。
先在一个依赖已固定 $A_4$ 的小时间窗上界定 $a,a',a''$，
这些界仍与截止的高阶导数无关；
§4 的同一 Nishida 论证给共同 $T_*>0$，再选 $\epsilon<T_*/2$。
实际初始核心、标架和第二形式也与 R38 相同，
所以唯一性使整张位置图在开内领上与那一个 R38 解完全相同。

在柱面一侧换回原直柱面时，沿用 R38 已证的完整 $C^2$ 贴接；
不把这个四阶版本称为全 jet 相同。其正向出口在有限位置也恰为平坦仿射领，
斜率不超过 $4A_4\epsilon^3$，且 $a>1$。
嵌入与正 reach 同样通过统一小带的弦长/Hessian 余量取得。

因此本文有两项不同事实：
(6) 是从同一真实核心出发的全 jet 平坦入口；
(19) 是保留既有 R38 四阶鞍领的实际有限延拓。
两者不能被当作同一次固定度量计算的两个网格。

## 8. 具体振幅族的全 E(3) 非平凡性

对 §2 的核心，其平面围面积为

$$
\mathcal A(\gamma_\lambda)
=\frac12\int_0^{2\pi}h_\lambda\rho_\lambda\,d\varphi
=\pi(1-4\lambda^2).
\tag{20}
$$

它在指定正参数区间严格递减。
整个已接好的环带有两条边界，长度分别为
$2\pi$ 和 $2\pi a_\epsilon(\epsilon)>2\pi$，
这些长度对所有 $\lambda$ 相同。
任何两像间的空间刚体全等都必须诱导保持边界长度的内在等距，
因此必须把长度 $2\pi$ 的底边映到相同底边。
底边是平面凸曲线 $\gamma_\lambda-h_0e_z$；
欧氏全等（含反射）保持其围面积。
由 (20)，不同 $\lambda$ 的完整环带像不能全等。

所以可取明确时间区间
$\lambda(t)=1/32+t/32$、$t\in[0,1]$，
得到同一个 $g_\epsilon$ 上的非刚体等距族；
不是只有两个端点，也不是纯相位旋转。
最小刚体 Hausdorff 距离在紧像的有界对齐集合上取到，
故每个非初态的商像距离严格正。
这里没有给有效的像位移下界，且该族没有固定开握持区。

如果改用 R38 的原相位族，
$F_\alpha=R_\alpha F_0(s,\theta-\alpha)$，
则本次延拓也按唯一性满足同一相位式；
整个带边模块的 $\delta_E$ 仍为零。
这个范围与本文新的具体振幅族必须区分。

## 9. 接合到底前进到哪里

(6) 的出口斜率
$B_\epsilon=\int_0^{3\epsilon/4}a_\epsilon''(s)\,ds$
严格正，且

$$
B_\epsilon\le \epsilon e^{-1/\epsilon^2},\qquad
a_\epsilon(\epsilon)>1 .
$$

平坦领的锥角为 $2\pi B_\epsilon$，在 (13) 的参数范围内远小于 $2\pi$。
$C$ 保持正，所以第二基本形式即使在 $K=0$ 处也未归零。
这不是 R43 的欧氏平圆环或指定 Cartesian 两 jet，
也没有产生固定出口高度、固定外帽或混合点对证书。

(19) 的旧四阶版本同样保留 $a>1$。
若之后还要求它接到既定的小半径平环，既有径向转折缺口仍在；
不能因获得有限平坦领就说那条完整接线已完成。
这个说明限于本文实际指定的度量及所保留的 R38 分支。

本文真正支付的是：从已知水平核心的实际位置与框架起步，
用同一个精确度量得到真闭圈、全时间嵌入、有限径向的平坦仿射出口；
可选全 jet 贴柱，也可保留旧四阶鞍领。
未支付的是闭曲面、固定握持区、可见幅度、
目标归一 reach、R43 接合、数值网格和绑定脚本独立复算。
本文件只是一份新数学证明，不回填任何旧执行状态。
