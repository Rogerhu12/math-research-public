# R343 — 原三挠点的完整相位与两个真实 Faber 观察

日期：2026-11-13。**状态：原两行的全部 Faber 坐标、准确 Wronskian
二次型，以及实际三挠 division 函数确定的完整 Verschiebung 立方
相位均已证明。没有由这些行或核底部系数的单位性推断固定负矩
联合非零；主目标未完成。**

本结果接 [R336](R336-ordinary-original-zeta-as-verschiebung-and-two-full-negative-rows.md)。
固定 $p=6s+1>7$、$E_b:y^2=x^3+b$、$b=17$，所有以下模 $p$ 的
系数都在 R336 的原普通嵌入和同一不变微分中。
明确取 $D=d/dz$、$x=z^{-2}+\cdots$、$\sigma=z+\cdots$，
$$H=\binom{3s}{s}b^s,\qquad\Theta=x\sigma^2.$$
真实可分核多项式是 $f_V=P(x^3)$，其中
$V=[\bar\pi]\bmod p$、$V^*dz=Hdz$、$P$ monic degree $s$。

## 1. 真正消去 Laurent 坐标修正的基

令
$$
F_j(X)=\frac{D^{6j-2}x}{(6j-1)!},\qquad X=x^3,\quad1\le j\le s.
$$
它是 monic degree-$j$ 多项式；分母最高仅到 $(p-2)!$，是单位。
写入原 $z$ 坐标时，准确有
$$F_j(X(z))=z^{-6j}+F_{j,0}+O(z^6).$$
确实 $x=z^{-2}+\sum_{r\ge1}w_rz^{6r-2}$；当 $r<j$ 时，
$D^{6j-2}$ 把非负次单项式 $z^{6r-2}$ 完全杀掉，所以没有其他负次项。

把 R336 的实际核多项式写为
$$P(X)=\alpha_0+\sum_{j=1}^s\alpha_jF_j(X).$$
真实 CM pullback 的相同截断证明给
$$\boxed{\alpha_j=H^{-6j}c_{s-j},\qquad\alpha_s=1,}$$
其中 $\sigma(z)/z=\sum c_nz^{6n}$。因此第一个指定行就是
$$c_{s-1}=H^6\alpha_1.$$

这一步确实支付了原 $x(z)$ 的全部 Laurent 修正。它没有把 monomial
基里的 $P'(0)$ 偷换为 $\alpha_1$。

## 2. 第二原行是一个准确的二次型

R336 的 $xT_P$ 恰为 $W(P)=(DP)^2-PD^2P$。目标极阶
$p+7=6s+8$ 大于单个 $F_j$ 及其二阶导数所能给的极阶 $6s+2$。
所以在这一条系数上，regular 与 polar 的交叉项全部不贡献；只需
各 $F_j$ 的单个主部，得到
$$
\boxed{
d_{s-1}=H^6\sum_{j+k=s+1}
\left\{-18(j-k)^2-3(s+1)\right\}\alpha_j\alpha_k.
}
$$
求和按有序对计。公式来自
$(36jk-6k(6k+1))$ 对 $j,k$ 的对称平均，因而保留全部交叉项。
若 $\alpha_1=0$，$\alpha_s=1$ 的两个配对也消失，只剩
$2\le j,k\le s-1$ 的真实二次型。

同一原测度的两个负矩仍带原周期及阶乘：
$$
I_{\sigma,-5}\equiv\Omega_p^{p-6}(p-6)!H^6\alpha_1,\qquad
I_{\Theta,-6}\equiv\Omega_p^{p-7}(p-7)!H^6
\sum_{j+k=s+1}\{-18(j-k)^2-3(s+1)\}\alpha_j\alpha_k
\pmod p.
$$
全部外部因子为单位，但本篇没有把剩余两个值置为非零。

这解释了为什么仅知道最高系数为一、底部 $P(0),P'(0)$ 是单位，
并不能直接把第二行化为一个显然非零的数。

## 3. 原 norm-three 与整个 polynomial 方程

记 $B(q)=\Theta(z)$、$q=z^6$。原身份给
$$C(-27q)=C(q)B(q),\qquad C(q)=\sigma(z)/z.$$
在 $n=s-1$ 的准确模 $p$ 行是
$$d_n+\frac{28}{27}c_n+\sum_{j=1}^{n-1}c_jd_{n-j}=0.$$
如果两个指定行同零，较低项卷积也必须为零。该卷积不是本篇
已经证明非零的量。

真实核的整个方程比单个卷积关系更强：
$$
X^{2s}P\left(-\frac{(X+4b)^3}{27X^2}\right)=P(X)T_P(X),
$$
$$T_P=36X(X+b)(P'^2-PP'')-6(7X+4b)PP'.$$
R336 已证明它与原 CM 半特征、Gaussian、完整乘法常数一致，并且
$$
(HP(0))^3=1,\qquad
\frac{P'(0)}{P(0)}=-\frac{H^3b^{(p-1)/2}}{24b}.
$$
下一项实际问题是用这个完整方程控制上节二次型，而不是再次将
底部两个单位当作目标行。

## 4. 两个已有有限反例只排除各自恒为单位的猜测

这些系数由固定递推准确得到；这里不增加素数扫描。先取 $b=1$，
一般 $b$ 的第 $n$ 项乘 $b^n$。写 $W=z^2x$、$\sigma/z=\exp F$，则
$$
W_0=1,\quad W_1=-1/7,\quad
W_n=\frac{\sum_{j=1}^{n-1}W_jW_{n-j}}{(n-1)(6n+1)},\quad
F_n=-\frac{W_n}{6n(6n-1)},\quad \Theta=W\exp(2F).
$$
由此
$$
c_4=\frac{31}{77920092890640000},\qquad
d_4=\frac{23762}{608750725708125},
$$
$$
c_5=-\frac{9103}{956184731893555164000000},\qquad
d_5=-\frac{82436}{120486987385780640625}.
$$
$p=31$ 时 $s-1=4$，第一原行的首层为零，第二行非零。
$p=37$ 时 $s-1=5$，第二原行的首层为零，第一行非零。
所列分母在各自素数处为单位；$b=17$ 的尺度也为单位。

这既不证明固定负矩本身等于零，也不构成两行共同消失的例子。
它只排除“每条固定负矩总是单位”的猜测。

R339 已另以随 $p$ 改变的单位负矩构造同一原 $S$ 中实际非零深域。
因此本篇的联合首层问题不是一个可以无证假定的必要步骤；其
价值在于给真实固定负矩及原核几何一个准确、可继续消元的接口。

## 5. 标准 division 函数支付底部的实际立方相位

R336 的 $(HP(0))^3=1$ 可以进一步确定全部相位，而非任取三次单位根。
令 $Q=(0,\sqrt b)$、$t=2y(Q)$。原规范为 $x'=2y$、
$y\sim-z^{-3}$、$\sigma\sim z$，所以标准 division 函数的准确定义是
$$\psi_n=(-1)^{n-1}\frac{\sigma(nz)}{\sigma(z)^{n^2}}.$$
特别 $\psi_2=2y$，而原 sigma 身份是
$\sigma(2z)=-2y\sigma(z)^4$；偶数的负号必须保留。
对以下奇素数 $p$，$(-1)^{p-1}=1$，主结论不受该符号影响。
在这个实际三挠点，准确有
$$
\psi_n(Q)=
\begin{cases}
0,&3\mid n,\\
(-1)^{(n-1)/3}t^{(n^2-1)/3},&n\equiv1\pmod3,\\
(-1)^{(n-2)/3}t^{(n^2-1)/3},&n\equiv2\pmod3.
\end{cases}
\tag{1}
$$
这里首先是特征零的 division 函数恒等式，然后才在好约化处约化。
一个完全代数证明如下。初值为
$\psi_0=0,\psi_1=1,\psi_2=t,\psi_3=0,\psi_4=-t^5$。
对非零项提出 $t^{(n^2-1)/3}$ 后，剩余符号依次为
$(0,1,1,0,-1,-1)$，周期六。
在 Ward 恒等式
$$
\psi_{m+n}\psi_{m-n}
=\psi_{m+1}\psi_{m-1}\psi_n^2
-\psi_{n+1}\psi_{n-1}\psi_m^2
$$
中，每个非零项的 $t$ 指数均为 $(2m^2+2n^2-2)/3$，而周期六符号
满足同一个恒等式。更直接地，标准奇、偶递推准确为
$$
\psi_{2m+1}=\psi_{m+2}\psi_m^3-\psi_{m-1}\psi_{m+1}^3,
$$
$$
\psi_{2m}=\frac{\psi_m}{t}
 (\psi_{m+2}\psi_{m-1}^2-\psi_{m-2}\psi_{m+1}^2).
$$
记周期六符号为 $e_n$。六个剩余类分别给
$$e_{2m+1}=e_{m+2}e_m^3-e_{m-1}e_{m+1}^3,$$
$$e_{2m}=e_m(e_{m+2}e_{m-1}^2-e_{m-2}e_{m+1}^2).$$
在非零项中，前一式两个指数均为 $((2m+1)^2-1)/3$，后一式
在除去 $t$ 后均为 $((2m)^2-1)/3$。所以从上述初值强归纳证明
所有 $n$ 的 (1)。偶项只除以 $t\ne0$；没有在 $\psi_3(Q)=0$ 处
作非法除法。

在特征 $p$ 中，$[p]=V\circ\operatorname{Frob}$ 给
$$\boxed{\psi_p=Hf_V^p.}\tag{2}$$
非零 étale 核点各有重数 $p$，两边 divisor 相同；原点的标准
$p$-series 首项是 $H u^p$，所以其首 Laurent 系数准确为 $H$，
确定了 (2) 的常数，而不是只确定其 divisor。

$p=6s+1$ 时，(1) 中符号为一。又
$y(Q)^p=b^{(p-1)/2}y(Q)$，所以
$$
\psi_p(Q)=(2y(Q))^{2s(p+1)}
=(4b)^{2s}=(b/2)^{2s}.
$$
最后一次相等使用 $2^{6s}=1\pmod p$。$P$ 的系数在
$\mathbf F_p$，因此 (2) 给出完整的原剩余相位
$$
\boxed{HP(0)=(b/2)^{2s},\qquad
P(0)=H^{-1}(b/2)^{2s}.}\tag{3}
$$
它与 R336 的立方关系及 $(33)$ 一致。

一个可供低次 $C=y\sigma^3$ 原 trace 比较的实际数是
$$
\frac{b^{3s}}{HP(0)}=b^s2^{2s}.
\tag{4}
$$
右端是明确的六次/三次剩余角色组合。(4) 本身只是本固定
三挠点与实际 Verschiebung 的相位；没有因此把它认作未经原 trace
比较的特征零 $p$-core 标量，也没有从模 $p$ 自动唯一提升一个
$p$-adic 标量。

## 6. 精确证书

[脚本](../scripts/check-jzero-faber-rows-and-original-three-torsion-phase.py)
及 [JSON](../scripts/check-jzero-faber-rows-and-original-three-torsion-phase.json)
有 27 项精确检查，逐个核定全部六个符号剩余类、奇偶递推的
完整指数、两个 Faber 行及原三挠相位。唯一具体纤维复用 R336
已从 division polynomial 重建的 $p=13,b=17$ 数据，没有新增扫描。

R336 给本篇使用的整性、真实 Verschiebung 和全部 Laurent/CM
尺度证明；本篇给出的两项新结论分别是其观察行的完整 Faber
对角化，以及从标准三挠除法函数确定的全部原立方相位。
