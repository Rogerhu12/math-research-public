# 相邻真实 germ 的三阶匹配与微小 cap 费用

2026-11-12，constructive-route。本文针对当前固定型别 R37 特征场，
证明如何在一个参考时间段中选一个真实 scalar germ 的解析延拓，
并明确支付实际跨 knot 的小段。它不把旧 δ₄ 时间网格改称 δ₅ 的
准确 knot 网格，也不把单个 germ 的 time-circle 场包直接授予整段。

## 1. 准确对象与需要匹配的量

固定一个实际参数值，例如已保存的准确 δ₅。保持同一准确 R33 图、
同一径向 target、同一真实正根 $t$、同一物理角及同一特征分支。
在物理单调支 $\tau\in(-\pi/2,\pi/2)$ 上写

$$
 r=t\sin\tau,\qquad \tau=c+h u,\quad h\ne0,
 \qquad -1\le u\le1.
 \tag{1}
$$

$h$ 可以为负；这不改变下述匹配，积分费用使用 $|h|$。
所有相邻 scalar germ 都必须用同一个 $(c,h,t)$ 作延拓，而不能各自
重新以另一个根或时间中心定义后直接相减。这里的原始物理速度记作
$f(u,\theta)=d\theta/d\tau$；有符号时间半宽尚未乘入。

当前准确输入的 base $b$、raw phase、radius shift 与各 mean radius
是五次 spline，所有内部 knot 的最低连续阶为 $C^4$。实际 phase
还保留固定 base 权重：先取 $\widetilde\beta=b^3\beta_{\rm raw}$、
$\widetilde\gamma=b^2\gamma_{\rm raw}$，再令
$\beta(r)=(\widetilde\beta(r)+\widetilde\beta(-r))/2$、
$\gamma(r)=(\widetilde\gamma(r)-\widetilde\gamma(-r))/2$。
因此实际 $\beta,\gamma$ 在公共 span 上一般不是五次多项式，但乘积
与显式对称化仍保持 $C^4$；$a$ 同样保持 $C^4$。$Z$ 的 primitive
最低为 $C^5$。这些是准确控制点、固定权重和 knot 的性质，不是节点抽查。
在全部 scalar 公共 knot 上，左右 germ 的以下 jet 因而准确匹配：

$$
 (a,\beta,\gamma):\quad\partial_r^j, 0\le j\le4;
 \qquad Z:\quad\partial_r^j, 0\le j\le5.
 \tag{2}
$$

公共分片可能含由近邻 binary64 knots 形成的极短区间；它们并不
破坏 (2)，也不能因为长度很小就直接删掉。

## 2. 为什么真实物理场匹配到二阶

在 R33 表示中

$$
 F=a\,\mathcal P_\theta T+Z e_z,\qquad
 T=(\cos\gamma\cos\phi,\cos\gamma\sin\phi,\sin\gamma),\quad
 \phi=\theta+\pi/2+\beta.
 \tag{3}
$$

有限 phase 的指数与三角函数在任意固定有限复角带上全纯；径向
$C^4$ 包络在紧邻域上一致。因此其角 Fourier 系数及前四阶径向
导数有一致指数尾，固定规范的线性角原函数可与这些径向导数交换。
由 (2)–(3)，$F$ 为径向 $C^4$，$X=F_r$ 为 $C^3$，且这些匹配
对全部复角成立。无需把有限 primitive 的导数当成无限图导数。

径向 target 由同一图给出

$$
 E(r)=\langle F_r\cdot F_r\rangle_\theta,\qquad
 g_0=E(r)\,dr^2+a(r)^2\,d\theta^2.
$$

因为 $F_r$ 为 $C^3$，角平均与前三阶径向导数可交换，故 $E$ 为
$C^3$。在 $a,E>0$ 的范围内，其曲率

$$
 K_0=\frac{a'E'}{2aE^2}-\frac{a''}{aE}
 \tag{4}
$$

为 $C^2$。所以相邻真实 target germ 在公共 knot 的 $K_0$ 值和
前两阶径向导数完全相同。

在非 turn 的严格负曲率区，取实轴为正的同一
$\sqrt{-K_0}$ 分支。它是负曲率值的解析函数，因而也匹配到 $C^2$。
R59 移动 frame 的 $D,M,W$ 由 $a,T,T_r,T_\theta,X$ 的有限代数式
构成，最低径向连续阶为 $C^3$；在已证明 $D\ne0$ 的共同复角域中
作除法后，R37 的物理特征速度至少为 $C^2$。例如可用统一符号写作

$$
 f_\sigma(u,\theta)
 =-t\cos(c+hu)\,
   \frac{M(r,\theta)+\sigma\sqrt{-K_0(r)}W(r,\theta)}
        {D(r,\theta)},\quad \sigma\in\{-1,1\}.
 \tag{5}
$$

若采用另一固定的分支符号约定，只重命名 $\sigma$，以下结论相同。
这里 $W=G_{\rm actual}/a^2$，不得换成目标面积。

令 $r_k$ 为相邻公共 scalar knot，在实际参数和同一根下定义

$$
 \tau_* =\arcsin(r_k/t),\qquad u_*=(\tau_*-c)/h.
 \tag{6}
$$

只对 $|r_k|<t$ 且严格非 turn 的交界使用 (6)。物理正弦支的单调性
保证这是实际 crossing。相邻两解析延拓 $f_-,f_+$ 在该点满足

$$
 \partial_u^j(f_+-f_-)(u_*,\theta)=0,\qquad j=0,1,2,
 \tag{7}
$$

对整个共同复角域的每个 $\theta$ 都成立。径向 $C^2$ 匹配经同一
解析变量变换给出实角上的等式；各式作为 $\theta$ 的全纯函数，再由
恒等定理推广到共同复角域。等价地，在共同解析邻域内存在全纯 $A$，

$$
 f_+(u,\theta)-f_-(u,\theta)=(u-u_*)^3A(u,\theta).
 \tag{8}
$$

这里匹配的是完整物理场，包含曲率、实际面积、原始二型与时间链式
因子；不能只检查 phase 多项式匹配后省掉 (4)–(5)。

## 3. 同一个参考复合仍有三重零

设同一参考 $Y(u,x)$ 在 $|u|<R$、某个初值标签复带上联合全纯。
假设 $f_-$ 与 $f_+$ 都在这个共同时间圆盘和所需物理角域上解析，
而整个 $Y$ 复像均包含在它们的共同角域中。令

$$
 F_\pm(u,x)=f_\pm(u,Y(u,x)).
$$

把 (8) 代入便得

$$
 F_+(u,x)-F_-(u,x)
 =(u-u_*)^3A(u,Y(u,x)).
 \tag{9}
$$

因此无需另付 $Y_u,Y_{uu}$ 来证明匹配。逐项链式法则也给同一结论：
(7) 是对整个角函数恒等为零，其全部角导数也为零，所以混合链式项
同时消失。若两边使用不同参考、不同时间坐标或不同根，此论证失效。

设在共同时间圆盘和完整标签带上有连续一致界

$$
 |F_-|\le M_-,\qquad |F_+|\le M_+.
 \tag{10}
$$

充分的实际输入是已证明 $|f_\pm|\le M_\pm$ 的全角 bidisc，外加
同一参考的完整复像包含关系。有限初值节点检查不代付 (10)。

## 4. 三重零的直接最大模界

写 $M=M_-+M_+$，$\rho=R-|u_*|>0$。以 $u_*$ 为中心的开圆盘
$|u-u_*|<\rho$ 包含在原时间圆盘内。由 (9)，

$$
 B(u,x)=\frac{F_+(u,x)-F_-(u,x)}{(u-u_*)^3}
$$

在中心可去奇并全纯。对任意 $0<s<\rho$，在圆周
$|u-u_*|=s$ 有 $|B|\le M/s^3$。最大模原理将同一界带到圆盘内部；
固定内部一点再令 $s\uparrow\rho$，得到

$$
 \boxed{|F_+(u,x)-F_-(u,x)|
       \le M\left(\frac{|u-u_*|}{\rho}\right)^3}
 \quad(|u-u_*|<\rho).
 \tag{11}
$$

由连续性也可取所用闭 cap。这里不需要把分母缩成
$\rho-\text{cap长度}$。若改用三阶导数的 Cauchy–Taylor 余项，则会
得到较松但仍正确的
$M|u-u_*|^3/(\rho-c)^3$（$c<\rho$）；(11) 保留三重零本身，
没有支付这项额外损失。

若当前时间证书的圆盘中心不是 0，而是 $u_0$，只需将
$\rho$ 改为 $R-|u_*-u_0|$。不同成功圆盘不能取外包矩形；必须有
一个实际证明的共同圆盘同时容纳两延拓及 $Y$ 的所需复像。

## 5. 只在实 cap 除以参考初值导数

对实时间上的实际小场与选用主 germ 的小场，令 $q=Y_x$。相同
$Y_u$ 准确相消：

$$
 g_\pm(u,x)=\frac{h f_\pm(u,Y)-Y_u}{q},
 \qquad g_+-g_-=\frac{h(F_+-F_-)}q.
 \tag{12}
$$

假设仅在所处理的**实时间 cap 和完整复标签带**上已证明
$|q|\ge m>0$。不需要为了本 cap 引理再证明 $q$ 在整个复时间圆盘
无零点。由 (11)，逐实时间的误差可取

$$
 \eta_{\rm cap}(u)
 =\frac{|h|M}{m\rho^3}|u-u_*|^3.
 \tag{13}
$$

对从 crossing 向一侧长度为 $c<\rho$ 的实际 cap，

$$
 \boxed{E_{\rm cap}=\int\eta_{\rm cap}(u)\,du
 \le\frac{|h|M}{4m\rho^3}c^4.}
 \tag{14}
$$

若所需区间在 crossing 的同侧，端点距离为 $d_1\le d_2$，可用更细的
$|h|M(d_2^4-d_1^4)/(4m\rho^3)$；若两侧都存在，则分别加其四次幂。
$|h|$ 是准确有符号半宽的模，不可在返回腿漏掉或重复乘入。若已将
证书的场定义为 $h f$，则在 (10) 的 $M_\pm$ 中已含该因子，(13)–(14)
不得再次乘 $|h|$。

R72 的近似场与真实场共用幅度包络也必须相应处理。若主 germ 近似
场已有 $\widehat M(u)$，可取真实共同包络
$M_{\rm all}(u)=\widehat M(u)+\eta_{\rm cap}(u)+\eta_{\rm other}(u)$。
cap 费用加入总 $E$，且其真实上界也进入 $A$。不能只把它放进端点误差
而继续沿用一个未包含实际场的 $M$。

本引理不代付近似主 germ 场的其它误差。若另用复时间 DFT 去构造
$1/q$ 或 $g_\pm$ 的近似，则该构造自身所需的复时间无零点域仍须支付；
(14) 只说明“实际跨 knot 的误差”这一步不需要它。

## 6. 实际 crossing 只被区间包住时

必须从准确公共 knot、同一真实根包与同一 $(c,h)$ 计算 (6)。设
有向计算给 $u_*\in[\ell,v]$，参考段端点为准确实数 $a<b$。
可以安全使用

$$
 U=\max(|\ell|,|v|),\qquad \rho_-=R-U>0.
$$

在右侧 cap，长度上界取 $c_+=\max(0,b-\ell)$；在左侧取
$c_-=\max(0,v-a)$。这些式子是对实际 crossing 的外包，不把区间中点
当成准确 knot。只要所用 $c_\pm<\rho_-$，(13)–(14) 中以
$\rho_-$、$c_\pm$ 和其它向外界替代即可。若区间不能确定是否真的
crossing，只会多付可能 cap，不能把可能跨越当成不存在。

原始时间端点可以含准确 $\pm\pi/2$；在本文非 turn 使用区间内部
的 crossing 时，同样保留准确 $q+p\pi$，不能先舍入端点再求 cap。

## 7. 多个微小公共 span 的相邻望远镜求和

一个参考段可能穿过多于一个公共 knot。按照实际 $u$ 的递增次序
列相邻延拓 $f_0,\ldots,f_J$；返回腿可能与径向顺序相反。
选其中一个作为主延拓 $f_k$。实际时间落在另一 germ 时，
$f_{\rm actual}-f_k$ 是它与主 germ 之间的**相邻差**之和。
每一相邻差只在其 crossing 的远离主 germ 的一侧需要计入。
因此可对各相邻 pair 分别用 (14) 或其细化式，然后求和。

每个 pair 都要有自己的真实共同域、同一实际 crossing 和匹配合同。
不能让非相邻两段在某一个 knot 处假装匹配，也不能在 telescoping
时删掉极短的中间 span。这个求和允许不为每一个微小 cap 单独构造
完整 time-circle 场包，但其既有全角/复时间域及 $M_\pm$ 仍须完整。

## 8. 排除 turn 以及实际结论边界

本文的 $C^2$ 速度匹配使用严格 $K_0<0$ 和同一解析平方根分支。
在真实 turn 上，未消根的 $\sqrt{-K_0}$ 不满足这些假设，不能直接
套用本文。当前已证明的 turn 区域使用 R65 的唯一真实 root germ
和 $Q$ 消根公式；只要实际时间区间保持在该 root germ 内，无需新增
跨 knot cap。若将来一个 turn 段确实跨出 root germ，必须另作准确
解析匹配及域证明，不能把普通段的三阶结论延伸过去。

本文完成匹配与误差证明，不宣称当前全部两腿的 $Y$ 复像、$q$ 下界、
所有 cap 几何及总 $E_{\rm cap}$ 已计算。后续实际报告应分别列出
主 germ、所有真实公共 knot、准确 crossing 外包、共同时间/角域、
$M_\pm$、$\rho_-$、cap 长度，以及尚需的 $Y$ 复像和实 cap $q$ 门。

