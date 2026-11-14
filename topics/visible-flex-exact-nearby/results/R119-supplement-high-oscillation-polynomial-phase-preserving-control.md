# R119 续篇：真实高振荡负坡的多项式相位保持 Wronskian 控制

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 在同一个受控新尾上，只要实际未占用四次坡区间含有
足够多的本征波长，并且 $|m|/\sqrt{\mathcal B}$ 足够大，真实固定两端
Robin Wronskian 有一个两相位保持、紧支、$C^4$ 范数不超过1的方向，
其导数有显式的多项式下界。这比此前统一复延拓门在该频段给出的
指数下界更强。结论含实际径向测度、左右真实 wave 单位、完整补偿和
一个有限参数区间；不把它称作非径向中矩阵的逆。

## 1. 对象、固定端口与真正频率条件

采用[控制后全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)、
[完整相位补偿与 Hessian](R119-supplement-radial-phase-compensation-and-full-Wronskian-Hessian.md)
的同一实际径向对象。允许已选择的紧支形状位于当前区间之外。
取一个未占用闭区间 $I\subset J=[7/16,15/32]$，并要求它有非零长度。
在 $I$ 以及其真实邻域，准确有
$$
 a=\eta_j/\sqrt{12},\quad
 \Delta>80,\quad B=\Delta/a>2^{190},\quad
 Q=7+Bf(x),\quad f(x)=30x^2(1-x)^2,\quad dt=a\,dx .
 \tag{H.1}
$$
这里的 $a$ 是实际短坡长度，不是标签。$j\ge8193$，
$\delta_j=(2/25)2^{-j}$，并使用已证
$$
 \delta^{3/2}/32<a<\delta^{3/2}/16,\qquad
 \Delta<3J_0,\quad J_0=j+5 .
 \tag{H.2}
$$
两个完整真实 Robin 方向已搬到原 $Q=7$ 缓冲的固定端点；这些端点及
物理两迹恢复矩阵固定。对 $M=|m|\in4\mathbb N$，写
$$
 k=\sqrt{7M^2-16},\quad
 Y=(\sqrt{k}\,u,u_t/\sqrt{k}),\qquad u=\sqrt{\mu}\,h,
 \quad \mu_t/\mu=-1-Q .
$$
沿整个实际控制窗的正、反齐次传播有原全频门
$$
 \|C(t,s)\|\le K_j,\qquad K_j=2^{6000}J_0^8\delta^{-16}.
 \tag{H.3}
$$
这是第52–54束的同一固定 wave 规范，不是任意归一高度。

令
$$
 r=\sqrt B/M,\qquad N=aM\sqrt B=\Delta/r .
$$
本篇真正频率条件为
$$
 \boxed{\quad r\le2^{-512},\qquad N|I|\ge8.\quad} \tag{H.4}
$$
它们只用于当前高振荡频段；没有将其冒称覆盖原整个移动中频。
对很短的逐频带支集，第二个条件须保留。

对真实左端单位向量 $l$、右端单位向量 $r_R$，置
$\mathscr W_m=[r_R,C_m l]$。在准确共振 $C_m l=\alpha r_R$ 处，
存在实紧支 $C^9$ 方向 $\psi$，满足
$$
 \sum_{\ell=0}^4\|\partial_x^\ell\psi\|_\infty\le1,\qquad
 D\Theta[\psi]=D\beta[\psi]=0 ,
$$
且在第54束的真实两 bump 补偿曲线上
$$
 \boxed{\quad
 |\partial_\varepsilon\mathscr W_m(0)|
 \ge L_m:=2^{-2048}K_j^{-3}a^{-1}\Delta^{-3}M^{-3}
 >2^{-20064}\delta^{47}J_0^{-27}M^{-3}.
 \quad} \tag{H.5}
$$
以下证明所有归一及常数。独立 mean 不在 $m\ne0$ 的断言中删除。

## 2. 准确 scaled-density 方程和核

在 $I$ 的中点 $x_c$ 引入 $\xi=N(x-x_c)$，令 $y(\xi)=u(x)$。
原准确方程是
$$
 u_{xx}+\left[M^2a(7a+\Delta f)
       +\frac{\Delta}{2}f_x-\frac{(8a+\Delta f)^2}{4}\right]u=0 .
$$
记 $F=f+7/B$、$H=F+1/B$，它准确成为
$$
 y_{\xi\xi}+q(\xi)y=0,\qquad
 q=F+r^2\left(\frac{f_x}{2\Delta}-\frac{H^2}{4}\right).
 \tag{H.6}
$$
$3/2<q<3$，而 $7/4<F<2$。
在每个实点、对 $1\le l\le8$，
$$
 |q^{(l)}_\xi|\le2^{44}N^{-l};
 \qquad q^{(l)}_\xi=0\quad(l>8).
 \tag{H.7}
$$
一个直接检查方法是用 $f$ 的系数绝对和120、
$f_x$ 的系数绝对和360、$H^2$ 的系数绝对和小于 $121^2$；
至八阶的导数系数和小于 $8!\,121^2<2^{30}$。
(H.7) 取了充分余量，并保留每次径向换元的 $N^{-1}$。

真正相位保持变分核为
$$
 \mathcal K=\mu(h_t^2-2M^2hh_t+M^2h^2).
$$
令 $z=y_\xi$。由 $h_t=\mu^{-1/2}(u_t+(1+Q)u/2)$ 得准确恒等式
$$
 g(\xi):=F^{9/2}\frac{a}{M^2N}\mathcal K
 =F^{9/2}\left[
 rz^2+(-2+r^2H)yz+
       \left(-rF+\frac{r^3H^2}{4}\right)y^2\right].
 \tag{H.8}
$$
主项是 $-2F^{9/2}yz$，不是一个可能被投影掉的常数能量。
(H.6)、(H.8) 的所有 $a,B,M$ 单位由程序作准确 Laurent 核算。

## 3. 二十一阶真实 jet 控制，不付复大盘指数

在一个实点置
$$
 Z=(y^2,yz,z^2)^T,\quad
 \mathsf B(q)=\begin{pmatrix}0&2&0\\-q&0&1\\0&-2q&0\end{pmatrix},
 \qquad Z_\xi=\mathsf B(q)Z .
$$
以该点的 $q_0$ 冻结 $\mathsf B_0$，并令
$E=z^2+q_0y^2$。则 $\|Z\|_\infty\le E$、
$\|\mathsf B_0\|_\infty\le6$。
对归一 Taylor 系数 $Z_l=Z^{(l)}/l!$，准确递推
$$
 (l+1)Z_{l+1}=\sum_{\nu=0}^l\mathsf B_\nu Z_{l-\nu}
$$
及 (H.7) 给，至 $l=22$，
$$
 \|Z_l\|\le8^lE,\qquad
 \left\|Z_l-\frac{\mathsf B_0^lZ_0}{l!}\right\|
                \le\frac{2^{50}}N16^lE .
 \tag{H.9}
$$
第二式的归纳上界只用
$$
 \frac{6\,2^{50}16^l+
       2^{45}\sum_{\nu=1}^{\min(8,l)}8^{l-\nu}}{l+1}
            <2^{50}16^{l+1};
$$
第一式也逐阶以同一实际 $N\ge80\,2^{512}$ 检查。
这里没有对未知解假定一个未付的高径向解析范数。

为估计 (H.8) 的系数，可在实 $J$ 每点使用半径 $1/8$ 的复 $x$ 盘。
$7+Bf$ 的根实部均不在 $(0,1)$；此盘中选定与正实轴一致的
$F^{9/2}$ 分支，且 $|F|<17$、$|F^{9/2}|<2^{20}$。
因此其归一 $\xi$ 系数至22阶小于 $2^{20}(8/N)^l$。
写 (H.8) 为 $g=\mathsf A(\xi)Z$，并置
$\mathsf L=(0,-2F_0^{9/2},0)$。
在 $l=0$ 的系数差小于 $2^8r$；在 $1\le l\le22$，
$\|\mathsf A_l\|\le2^{23}(8/N)^l$。
将这些和 (H.9) 逐项代入，使用 $22!<2^{70}$，得到
$$
 |g^{(l)}-\mathsf L\mathsf B_0^lZ_0|
              <2^{256}(r+N^{-1})E,\qquad 0\le l\le21 .
 \tag{H.10}
$$
完整有限 jet 的误差是 $r+N^{-1}$；没有
$\exp(CM\sqrt{a\Delta})$。

冻结系统的两行准确为
$$
 (yz)^{(20)}=(4q_0)^{10}yz,\qquad
 (yz)^{(21)}=(4q_0)^{10}(z^2-q_0y^2).
 \tag{H.11}
$$
程序同时核查这两个完整矩阵幂，避免只用一个 height 近似。
由 (H.10)，在实邻域有 $|g^{(21)}|<2^{63}E$。

## 4. 找到真实振荡见证并固定紧支半径

由 (H.4)，$|\xi|\le3$ 严格位于 $I$ 内。
令 $E(\xi)=z^2+q(\xi)y^2$，$E_c=E(0)>0$。
准确恒等式 $E_\xi=q_\xi y^2$ 和 (H.7) 给
$$
                  E_c/2<E(\xi)<2E_c,\qquad |\xi|\le3.
 \tag{H.12}
$$
取真实 Prüfer 角 $\vartheta=\arg(z+iy)$ 的连续 lift，
$$
 \vartheta_\xi=\frac{z^2+qy^2}{z^2+y^2}\ge1 .
$$
它在 $[-2,2]$ 的增量至少4，故有一实点 $\xi_0$ 满足
$|y|=|z|$。于是
$|yz|=E(\xi_0)/(1+q(\xi_0))>E_c/8$。
(H.10) 的误差小于 $2^{-254}E_c$；
(H.11) 因而给
$$
 |g^{(20)}(\xi_0)|>E_c/8,\qquad
 \sup_{|\xi|\le3}|g^{(21)}(\xi)|<2^{64}E_c .
$$
取
$$
                 \rho_\xi=2^{-72},\qquad
                 \rho_x=2^{-72}/N .                    \tag{H.13}
$$
在 $|\xi-\xi_0|\le\rho_\xi$ 上，$g^{(20)}$ 符号固定且模大于
$E_c/16$。支集严格处于 $I$ 内，不因 witness 在原区间端点而越界。

## 5. 一个准确消去全部 phase 核的 $C^4$ 方向

设
$$
 b(s)=(1-s^2)_+^{30},\qquad
 f_0(x)=\rho_x^{24}b((x-x_0)/\rho_x),
$$
其中 $x_0=x_c+\xi_0/N$。用 $g^{(20)}$ 的真实符号 $\sigma_0$ 定义
$$
 \boxed{\qquad
 \psi(x)=\frac{\sigma_0 F(x)^{9/2}f_0^{(20)}(x)}{2^{220}} .
 \qquad}                                                \tag{H.14}
$$
$b$ 的零延拓为 $C^{29}$，故 $\psi$ 为实紧支 $C^9$。
由上节小盘 Cauchy，$F^{9/2}$ 的前四导数小于 $2^{37}$。
$b$ 的至24阶导数小于
$2^{30}60^{24}<2^{174}$，每一 Leibniz 项留下
$\rho_x^{4-l+\nu}\le1$。所以完整 sum 范数满足
$$
 \sum_{l=0}^4\|\psi^{(l)}\|_\infty
 \le2^{-220}\,80\,2^{37}2^{174}<1 .                       \tag{H.15}
$$

实际两个 phase 核仍分别是 $P(x)/Q(x)^{9/2}$、$\deg P\le19$。
因为 $F^{9/2}=B^{-9/2}Q^{9/2}$，二十次真实分部积分给
$$
 \int_I\frac{P}{Q^{9/2}}\psi\,dx=0 .
 \tag{H.16}
$$
全部端 jets 消失。乘原 $dt=a\,dx$ 后仍准确为0，因此这确实属于
第54束的 phase-annihilator，而非一个近似投影方向。

## 6. 原测度、真实幅度及固定端 Wronskian

由 (H.8) 和 (H.13)，
$$
 \left|\partial_x^{20}(F^{9/2}\mathcal K)\right|
 >\frac{M^2N^{21}}{16a}E_c
$$
在整个支集符号固定。又
$\int_{-1}^1b(s)ds\ge(3/4)^{30}>2^{-15}$。
对 (H.14) 二十次分部积分，保留 $dt=a\,dx$，得到
$$
 \left|\int_I\mathcal K\psi\,dt\right|
 >2^{-2039}M^2E_cN^{-4}.                                \tag{H.17}
$$
二进制费用准确为 $220+4+15+25\cdot72=2039$。
短坡的 $a$ 在此由原测度与核的准确 $a^{-1}$ 相消；
不是先把 $dt$ 改成 $dx$ 而漏费。

从真实左单位 wave 传播到 $x_c$，(H.3) 给 $|Y(x_c)|\ge K_j^{-1}$。
由于 $2M<k<3M$、$B>3$，
$$
 |Y|^2=ky^2+\frac{M^2B}{k}z^2
       \le MB(y^2+z^2)\le MB E_c .
$$
所以 $E_c\ge(MBK_j^2)^{-1}$。

在准确共振 $C_m l=\alpha r_R$ 处，$|\alpha|\le K_j$。
完整 determinant-one wave 变换及真实 Green identity给
$$
 \alpha\,\partial_\varepsilon\mathscr W_m(0)
                         =\int_I\mathcal K\psi\,dt .
 \tag{H.18}
$$
两 bump 补偿的一阶导数因 (H.16) 准确为0，故没有漏掉它们的 first-order
贡献。将 (H.17) 和 $N=aM\sqrt B$ 代入，严格得到 (H.5) 的首式；
所用恒等式是
$$
 \frac{M}{BN^4}=a^{-4}B^{-3}M^{-3}
                         =a^{-1}\Delta^{-3}M^{-3}.
$$
再以 (H.2)、(H.3) 放宽，未舍入值严格大于
$2^{-20053}\delta^{93/2}J_0^{-27}M^{-3}$；
由于 $0<\delta<1$，(H.5) 的尾界成立。

## 7. 有限参数区间及近共振行

本方向可以叠加在之前所有支集均离开 $I$ 的已补偿形状上。
第54束的真实参数逆使 $\Theta,\beta$ 沿
$p_\varepsilon=p\,e^{\varepsilon\psi}$ 的完整两 bump 补偿曲线准确不变。
所有新旧前四端 jets、两根及正型 profile 保持。
只要完整形状仍在其 $2^{-64}$ 真复球中，
$$
 |\partial_\varepsilon^2\mathscr W_m|
 <2^{22}K_j^3(M+B/M)^2<2^{24}K_j^3M^2 .
$$
因此在原可用参数余半径 $r_{\rm free}$ 内，取
$$
 |\varepsilon|\le
 \min\{r_{\rm free},\
        2^{-2074}K_j^{-6}a^{-1}\Delta^{-3}M^{-5}\}
 \tag{H.19}
$$
即保证导数与其原值相差小于 $L_m/4$，所以方向及下界
$|\partial_\varepsilon\mathscr W_m|>L_m/2$ 保持。
这是一个实际有限区间；未只停在非零导数。

还可直接用于当前小非零 radial Wronskian。
把右单位线投影到 $C_m l$ 的方向，距离不超过
$2K_j|\mathscr W_m|$。真实 $DC_m$ 界小于 $4K_j^2M$，
故两条 Wr 导数差不超过 $8K_j^3M|\mathscr W_m|$。
若
$$
 |\mathscr W_m|\le L_m/(32K_j^3M),                       \tag{H.20}
$$
对投影共振线构造的同一 $\psi$ 对原真实线仍给导数大于 $L_m/2$。
因为 (H.4) 还给 $L_m<1$，此处投影的连续取向和小角条件确实满足。
原线、原 two-bump family 和参数依赖均未换成一个新的外边界问题。

## 8. 严格权限及当前非径向缺口

本篇改变的是高振荡 radial 控制费用。在真实原频率
$M\ge2^{512}\sqrt B$ 且支集容得下八个 scaled 单位时，
完整下界已不含 $\exp(-CM\sqrt{a\Delta})$。
较低 scaled 频段继续使用已证明的统一 kernel/compact 门。

这不证明非径向中矩阵的对应导数有同一符号或下界。
现有全非径向余项为 $H^s\to H^{s+4/3}$；
它与本篇 $M^{-3}$ 控制尺度仍须真实比较。
自伴、实性和两个转向根本身也不排除更高返回相位的二阶项。
若要将完整 paired-root 相位推进到三阶，必须计算真实二阶 symbol、
其共轭及不可去掉的平均量，不能由两个 $4/3$ 界相减得到。

本篇固定两侧真实 Robin 行。若将右行改成随其它外层参数变化的
global regular line，必须加入该行的 first/second derivatives。
ordinary/weak source 的两个分量、total/bare 端迹差和所有 mean
仍沿第53–55束的完整合同保留；phase-annihilator 不使 mean resistance、
平均高度或参数 metric-source 消失。
没有把当前径向控制选择称作完整 $\mathcal F_c=0$ 的闭合。

[新严格预算](../scripts/fourfold_high_oscillation_polynomial_phase_control_20261114.js)
与[实际执行记录](../notes/2026-11-14-R119-high-oscillation-polynomial-phase-control-budget.json)
核查准确 scaled 方程/核、完整对称平方矩阵幂、全部有限 jet 递推、
支集范数、原测度与实际 Wronskian 指数。计算是新的纯 V8/BigInt，
不冒称失去的 Python/native 已恢复。
