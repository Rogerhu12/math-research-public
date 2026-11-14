# R246：规范交替调和行的真实整轨道椭圆与活动碰撞根排除

日期：2026-11-13（UTC+8）。作者：kernel；Astra-ISP-1cf8c51d 复核。状态：已证明。本文的椭圆首先是实际有限柱整轨道的范数指示图形；它只通过额外的有限谱限制论证约束未知 Bell 核，不是原无界算子谱的闭包。

## 1. 主结论与保留的危险点

固定原 Haar 模型中的规范行
$$
u=\sum_{j\ge0}\frac{(-1)^j}{j+1}\chi_j,\qquad
X=X_u,\qquad
s=\sum_{j\ge0}\frac{(-1)^j}{j+1}=\log2.
\tag{1.1}
$$
对每个固定有限柱 $f\ne0$，实际自然幂级数
$$
\mathcal E(z)f
=\sum_{p=0}^\infty\frac{z^p}{p!}(X-sI)^pf
\tag{1.2}
$$
定义一个 $H$ 值整函数，且
$$
\boxed{
\lim_{r\to\infty}\frac1r
 \log\|\mathcal E(re^{i\theta})f\|
=h(\theta):=\frac\pi2\sqrt{1+\sin^2\theta}.
}
\tag{1.3}
$$
在每个固定前 $n$ 位柱空间的单位球上、以及所有角度 $\theta$ 上，该极限一致。这里不把 $\mathcal E(z)$ 当作全 $H$ 上的有界算子。

由此，任何非零闭有界 $X$ 不变分支如果具有有限谱，其谱必须包含在椭圆
$$
\boxed{
\mathfrak E=
\left\{x+iy:
\frac{4(x-\log2)^2}{\pi^2}
+\frac{2y^2}{\pi^2}\le1\right\}.
}
\tag{1.4}
$$
原 $X$ 的谱仍是 R138 的整个复平面连续谱；(1.4) 不改写这个事实。

定义多项式发生首位平移碰撞的根集
$$
\Gamma(q)=\{c:q(c)=q(c-2)=0\}.
\tag{1.5}
$$
结合 [R144](R144-first-mode-shift-resultant-cyclicity.md)/[R147](R147-exponential-weighted-first-mode-polynomial-cyclicity.md) 的真实有界除法，可以进一步证明
$$
\boxed{
\Gamma(q)\cap\mathfrak E=\varnothing
\quad\Longrightarrow\quad
q(u)e^w\text{ 对 }A\text{ 循环},
}
\tag{1.6}
$$
其中 $q$ 是任意非零标量多项式，
$w=c_*+\sum b_j\chi_j$、$b\in\ell^2$ 任意。

特别，
$$
\boxed{\bigl((u-2)^2-1\bigr)e^w
\quad\text{和}\quad
\bigl((u+2)^2-1\bigr)e^w
\text{ 都循环}.}
\tag{1.7}
$$
它们的标量根仍有差 2，故不是 R144/R147 原来的全根互素情形。

对于本课题核心 $u^2-1$，$\Gamma(q)=\{1\}$，而 $1\in\mathfrak E$。本稿没有关闭这个核。点 $-1$ 位于椭圆外，点 $+1$ 位于其内，二者必须区分。

## 2. 实际整轨道及真尾／纯尾比较

令
$$
a_j=(-1)^j/(j+1),\quad
s_m=\sum_{j<m}a_j,\quad
\tau_m=s-s_m,\quad
g_m=\|a_{\ge m}\|_2.
$$
有 $|\tau_m|\le1/(m+1)$、$g_m^2\le1/m$（$m\ge1$）。

写真实分解
$$
X-s_mI=H_m+Z_m,\qquad
H_m=\sum_{j<m}a_j(V_j-I).
\tag{2.1}
$$
$H_m$ 有界且与 $Z_m$ 的完整自然域交换。R207 附录给固定 $C$（可取 17），使
$$
\|Z_m^pQ_m\|\le(Cg_m\sqrt p)^p.
\tag{2.2}
$$
因此在具体有限柱输入上，尾自然幂级数按算子范数局部一致收敛，且真实二项式给
$$
\mathcal E(z)Q_n
=e^{zH_m}e^{-z\tau_m}\mathcal E_{Z_m}(z)Q_n,
\qquad m\ge n.
\tag{2.3}
$$
没有要求一般无界算子具有全空间有界指数。

记纯尾
$$
Z_m^0=\overline{\sum_{j\ge m}a_jS_j},\qquad
S_j=I-2E_j,\qquad Z_m=Z_m^0+K_m.
$$
R171/R181 及 R207 附录 A 的真实局部 carry 展开给：在所有尾次数权空间
$\mathcal H_{m,t}$、$0\le t\le1$ 上，
$$
\|K_m:\mathcal H_{m,t}\to\mathcal H_{m,t}\|
\le \kappa_m,\qquad
\kappa_m=
\frac{18e^2}{1-e\eta_*}\sum_{j\ge m}|a_j|\eta_j
\le C_0g_m\|\eta_{\ge m}\|_2.
\tag{2.4}
$$
这里 $C_0$ 固定，且 $\eta_j\le e^{-770\,16^j}$。纯尾和真尾在损失 $\delta$ 的次数权尺度上都可用同一个 $Cg_m\delta^{-1/2}$ 上界。

对尾真空 $\Omega$ 和整数 $p\ge1$，在尺度 $1\to0$ 中逐步展开幂差。每个项有一个保持权的 $K_m$，其余 $p-1$ 个因子各损失 $1/p$，所以每一步都在真实域中。望远镜和给
$$
\|(Z_m^p-(Z_m^0)^p)\Omega\|
\le p\kappa_m(Cg_m\sqrt p)^{p-1}.
\tag{2.5}
$$
这不是在不明域中套形式幂恒等式。

令 $R=|z|$。由 (2.5) 的绝对收敛级数，
$$
\boxed{
\|(\mathcal E_{Z_m}(z)-\mathcal E_{Z_m^0}(z))\Omega\|
\le e\sqrt2\,\kappa_m R
 \exp(e^2C^2g_m^2R^2).
}
\tag{2.6}
$$
确切地，设 $x=Cg_mR$，第 $p$ 项由 $p!\ge(p/e)^p$ 至多为
$$
e\kappa_mR\,
\frac{(ex)^{p-1}}{p^{(p-1)/2}}
\le e\kappa_mR\,
\frac{(ex)^{p-1}}{\sqrt{(p-1)!}}.
$$
再用 $\sum_{k\ge0}t^k/\sqrt{k!}\le\sqrt2e^{t^2}$ 即得 (2.6)。

## 3. 增长低头的双向预算是真正的 type 0

选取
$$
m=m(R)=\lfloor\sqrt R\rfloor.
\tag{3.1}
$$
当 $R\to\infty$ 时，$m\ge n$ 对每个固定 $n$ 最终成立。

[R241](R241-carry-head-powers-and-drifting-first-polynomial-cyclicity.md) 的实际进位计数证明
$$
\|H_m^k\|\le(6B_m)^k,\qquad
\|H_m^k\|\le(6B_m)^k e^{-\gamma k^4}
\quad(k\ge\max(2m,16)),
\tag{3.2}
$$
其中 $B_m=\sum_{j<m}|a_j|$、$\gamma=770/16^4$。因此指数级数在 $k<2m$ 与 $k\ge2m$ 分开后给
$$
\|e^{\pm zH_m}\|\le e^{F_m(R)}\qquad(|z|=R),
\tag{3.3}
$$
并可显式取
$$
\begin{aligned}
F_m(R)={}&\log(2m+C_\gamma)
+2m\log(1+6B_mR)\\
&+c_\gamma[\log(1+6B_mR)]^{4/3},
\end{aligned}
$$
$$
C_\gamma=\sum_{k\ge0}e^{-\gamma k^4/2},\qquad
c_\gamma=\frac3{4(2\gamma)^{1/3}}.
$$
这是逐项使用
$kL-\gamma k^4\le c_\gamma L^{4/3}-\gamma k^4/2$
得到的真实界。因 $m\le\sqrt R$、$B_m\le\|a\|_2\sqrt m$，
$$
\boxed{F_m(R)=o(R).}
\tag{3.4}
$$

另一方面，由 (2.4)、$\|\eta_{\ge m}\|_2\le2e^{-770\,16^m}$、$g_m^2\le1/m$，(2.6) 在 (3.1) 下的右端满足
$$
\log\text{(右端)}
\le-770\,16^m+O(R^{3/2}+\log R).
$$
乘上 $e^{-z\tau_m}$ 的范数因子只再付 $R|\tau_m|=O(\sqrt R)$。所以充分大时，
$$
\boxed{
\|e^{-z\tau_m}
(\mathcal E_{Z_m}(z)-\mathcal E_{Z_m^0}(z))\Omega\|
\le e^{-R^2}
}
\tag{3.5}
$$
对所有 $|z|=R$ 一致成立。

(3.3) 同时控制因子与逆，所以在 (2.3) 中既可取上界也可取下界。固定非零有限柱 $f$ 后，
$$
\begin{aligned}
e^{-F_m(R)}\|f\|\,
\|e^{-z\tau_m}\mathcal E_{Z_m}(z)\Omega\|
&\le \|\mathcal E(z)f\|\\
&\le e^{F_m(R)}\|f\|\,
\|e^{-z\tau_m}\mathcal E_{Z_m}(z)\Omega\|.
\end{aligned}
\tag{3.6}
$$
作用前的低头与尾真空轨道是张量积，故其中的 $\|f\|$ 因子准确。

因此只需计算纯尾的范数指示函数。有限的非零 carry 没有被写成“固定 tiny 常数乘 $R$，所以是 $o(R)$”；真正的 $o(R)$ 来自整个增长低头的 (3.2)–(3.4)。

## 4. 纯尾范数的准确无穷乘积

物理单个位上 $\Omega=(e_0+e_1)/\sqrt2$，
$$
e^{zaS}\Omega=e^{za}(I-2zaE)\Omega,
$$
所以
$$
\|e^{zaS}\Omega\|^2
=e^{2\operatorname{Re}(za)}
\left(1-2\operatorname{Re}(za)+2|za|^2\right).
\tag{4.1}
$$
有限不同位的纯算子彼此作用在独立张量上，故范数相乘。有限乘积在尾真空上按 $H$ 范数局部一致趋于纯尾整轨道；也可由 (2.2) 的纯版本逐系数识别。

由于 $\sum_{j\ge m}a_j=\tau_m$，中心化后准确有
$$
\log\|e^{-z\tau_m}\mathcal E_{Z_m^0}(z)\Omega\|
=\frac12\sum_{j\ge m}
 \log\left(1-2\operatorname{Re}(za_j)+2|za_j|^2\right).
\tag{4.2}
$$
该条件乘积保持原来的相邻顺序：高位项的对数为
$-\operatorname{Re}(za_j)+O_z(a_j^2)$，第一部分按原交错和收敛，第二部分绝对收敛。

设 $z=Re^{i\theta}$，定义实变量函数
$$
f_\theta(x)=\frac12\log(1-2x\cos\theta+2x^2).
$$
其对数内项始终至少 $1/2$。对 $x\ge0$，
$$
|f_\theta'(x)|\le\frac{16}{1+x}
\tag{4.3}
$$
可由
$1-2x\cos\theta+2x^2\ge(1+x^2)/4$
直接得到。

将每对相邻系数
$1/(2k-1),-1/(2k)$ 替换为
$1/(2k),-1/(2k)$，只改变正系数项。由 (4.3)，该对误差至多
$$
16\log\frac{1+R/(2k-1)}{1+R/(2k)}
\le\frac{16R}{(2k-1)(2k+R)}.
\tag{4.4}
$$
从尾起点求和，其总量为 $O(\log(2+R))$，对 $\theta$ 一致。首个不成对项至多再付 $O(\log(2+R))$。

每个等幅正负对的准确对数范数为
$$
f_\theta(x)+f_\theta(-x)
=\frac12\log(1+4\sin^2\theta\,x^2+4x^4).
\tag{4.5}
$$
把被删的前 $O(m)$ 对补回，只付
$O(m\log(2+R))=o(R)$。因此 (4.2) 与
$$
P(R,\theta)=
\frac12\sum_{k\ge1}
\log\left(1+\frac{4\sin^2\theta}{(2k/R)^2}
+\frac4{(2k/R)^4}\right)
\tag{4.6}
$$
相差 $o(R)$，一致于 $\theta$。

## 5. 积分计算及精确指示函数

函数
$$
\Phi_\theta(v)=\frac12
\log(1+4\sin^2\theta/v^2+4/v^4)
$$
对 $v>0$ 非负、递减，在 0 附近为 $O(1+|\log v|)$，在无穷远为 $O(v^{-2})$，均可对 $\theta$ 统一取界。单调 Riemann 和遂给
$$
\frac{P(R,\theta)}R\longrightarrow
\frac14\int_0^\infty
\log(1+4\sin^2\theta/v^2+4/v^4)\,dv,
\tag{5.1}
$$
且对 $\theta$ 一致。误差可由首个长度 $2/R$ 的积分控制，为 $O(\log R/R)$。

为完全计算此积分，置
$$
I(t)=\int_0^\infty\log(1+4t/v^2+4/v^4)\,dv,\qquad0\le t\le1.
$$
对参数求导的被积函数在 0 和无穷远分别有统一 $O(v^2)$、$O(v^{-2})$ 控制，因此
$$
I'(t)=4\int_0^\infty\frac{v^2}{v^4+4tv^2+4}\,dv
=2\sqrt2\int_0^\infty\frac{x^2}{x^4+2tx^2+1}\,dx.
$$
令最后积分为 $J(t)$。用 $x\mapsto1/x$ 得
$$
2J(t)=\int_0^\infty\frac{1+x^2}{x^4+2tx^2+1}\,dx.
$$
再置 $y=x-1/x$，得到
$$
2J(t)=\int_{-\infty}^\infty\frac{dy}{y^2+2(t+1)}
=\frac\pi{\sqrt{2(t+1)}}.
$$
故
$$
I'(t)=\frac\pi{\sqrt{1+t}}.
$$
在 $t=1$ 时，
$$
I(1)=2\int_0^\infty\log(1+2/v^2)\,dv=2\pi\sqrt2;
$$
最后一个等式也可直接分部积分得到。于是
$$
I(t)=2\pi\sqrt{1+t}.
$$
将 $t=\sin^2\theta$ 代入 (5.1)，得
$$
\boxed{h(\theta)=\frac\pi2\sqrt{1+\sin^2\theta}.}
\tag{5.2}
$$

由 (3.5)，实际尾与纯尾的差比 $e^{-R^2}$ 更小；纯尾范数的指数率至少 $\pi/2$，所以它不受这个误差改变。再用 (3.6) 和 $F_m(R)=o(R)$，得到 (1.3) 的上下界，且对固定 $Q_n$ 单位球与全部角度一致。

## 6. 从整轨道到有限谱有界分支的真实约束

设 $0\ne M$ 闭，
$$
M\subseteq\operatorname{Dom}X,\qquad XM\subseteq M,
$$
并令 $Y=X|_M\in B(M)$。暂假设 $\sigma(Y)=\{\lambda\}$。

通常伴随域恒等式
$$
P_MX^*=Y^*P_M
$$
可在每个有限柱的全部自然幂域中迭代，并可对绝对收敛整级数逐项作用。因此
$$
P_M\mathcal E_{X^*-sI}(z)Q_n
=e^{z(Y^*-sI)}P_MQ_n.
\tag{6.1}
$$
因为 $C$ 保持 $Q_nH$，$X^*=CXC$，且 $h(-\theta)=h(\theta)$，伴随整轨道具有同一个 (5.2) 指示函数。

写 $Y^*=\overline\lambda I+Q$，其中 $Q$ 有界拟幂零。对每个 $\epsilon>0$，幂的谱半径公式给常数 $C_\epsilon$，使
$$
\|e^{-zQ}\|\le C_\epsilon e^{\epsilon|z|}.
\tag{6.2}
$$
如果某个方向满足
$$
\operatorname{Re}\bigl(e^{i\theta}(\overline\lambda-s)\bigr)>h(\theta),
$$
则由 (6.1)、(6.2) 和伴随轨道的上界，让 $z=Re^{i\theta}$、$R\to\infty$，得到 $P_MQ_n=0$。所有 $n$ 都如此，$Q_n\to I$ 强迫 $M=0$，矛盾。因此非零分支必须满足
$$
\operatorname{Re}\bigl(e^{i\theta}(\overline\lambda-s)\bigr)
\le h(\theta)\qquad(\theta\in\mathbb R).
\tag{6.3}
$$
$h$ 正好是实半轴 $\pi/2$、虚半轴 $\pi/\sqrt2$ 的中心椭圆的支持函数，故 (6.3) 等价于 $\lambda\in\mathfrak E$。

若 $\sigma(Y)$ 有限，对每个非零 Riesz 谱子空间重复本节，便得
$$
\boxed{\sigma(Y)\subseteq\mathfrak E.}
\tag{6.4}
$$
这些 Riesz 子空间本身确在 $\operatorname{Dom}X$ 内并被 $X$ 保持。这里没有把有限柱整轨道的增长率直接当成原 $X$ 的谱，也没有对一般无限谱有界限制断言 (6.4)。

## 7. 只需排椭圆内实际会发生碰撞的根

先取 $w=0$。R176 给 $q(u)$ 的准确 Bell 自然多项式 $P(X)$；若 $M=\ker P(X)\ne0$，则
$$
M\subseteq\bigcap_{r\ge1}\operatorname{Dom}X^r,\qquad
Y=X|_M\in B(M),\qquad
\sigma(Y)\subseteq q^{-1}(\{0\})\cap\mathfrak E.
\tag{7.1}
$$
其谱有限。

对任意非平凡 dyadic $\zeta$，R144 的实际有界余数除法给
$$
Q_\zeta(z)-P(z)=A L_\zeta(z),\qquad L_\zeta\in\mathcal A[z],
$$
$$
\chi(L_\zeta(z))
=\frac{\zeta-1}{d_0}\,[q(z-2)-q(z)].
\tag{7.2}
$$
$Q_\zeta(X)$ 是 $P(X)$ 的真实 gauge 共轭，故
$Q_\zeta(X)U_\zeta M=0$。

设 $\Gamma(q)\cap\mathfrak E=\varnothing$。则对每个
$\lambda\in\sigma(Y)$，由 $q(\lambda)=0$ 和 (7.1)，有
$q(\lambda-2)\ne0$。因此标量系数多项式
$\ell_\zeta(z)=\chi(L_\zeta(z))$
在 $\sigma(Y)$ 上无零点，$\ell_\zeta(Y)$ 可逆。

实际算子 $L_\zeta(X)|_M$ 等于 $L_\zeta(Y)$，它与
$\ell_\zeta(Y)$ 之差是有限个彼此交换的拟幂零算子之和：
各项形如
$(E|_M-\chi(E)I)Y^k$、$E\in\mathcal A$。所以该差拟幂零，并与
$\ell_\zeta(Y)$ 及其逆交换。于是
$$
\boxed{L_\zeta(Y)\text{ 在同一个 }M\text{ 上是真正有界单位}.}
\tag{7.3}
$$
这一步不要求它在整个 $H$ 上可逆，也不要求未知限制的慢 Bell 尾像已稠密。

对 $x\in M$、$y\in U_\zeta M$，两者都在全部所需自然幂域。自然多项式的 $B$ 对称性及 (7.2) 给
$$
B(A L_\zeta(Y)x,y)
=B((Q_\zeta(X)-P(X))x,y)
=B(x,Q_\zeta(X)y)=0.
$$
由 (7.3) 和 R23 的 $\overline{AM}=M$，得到
$$
B(M,U_\zeta M)=0\qquad(\zeta\ne1).
\tag{7.4}
$$
R125/R144 已证的 Fourier 核机制把 (7.4) 压成维数至多 1；单射拟幂零 $A$ 不容许非零这样的不变空间。因此 $M=0$。R176 的完整 $C$ 自伴与图核心接口遂给 $q(u)$ 循环。

这里用到了核上已经支付的有限谱信息，以得到 (7.3) 的实际单位；没有用全空间 dense range 代替未知限制 dense range。

## 8. 任意第一阶指数权保留同一碰撞集

取
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$
为避免不必要的域替换，直接使用 R147 的原 $X$ 表示。该文构造有界交换单位 $B_*$、循环基向量
$\xi=B_*^{-1}e^w\in\bigcap_n\operatorname{Dom}X^n$，以及最高系数为 1 的 $\mathcal A$ 系数多项式 $P$，使
$$
q(u)e^w=B_*P(X)\xi,\qquad \chi(P)=q.
\tag{8.1}
$$
R176 已补全此自然多项式的闭性、最大图、完整 $C$ 伴随域及循环基图核心。其非零核仍有 (7.1) 的有限谱限制。

R147 (7.5)–(7.6) 给相同的真实除法和准确首字符：
$$
Q_\zeta(z)-P(z)=A L_\zeta(z),\qquad
\chi(L_\zeta(z))
=\frac{e^{-2b_0}(\zeta-1)}{d_0}
 [q(z-2)-q(z)].
\tag{8.2}
$$
因 $e^{-2b_0}\ne0$，椭圆内没有碰撞根时，§7 的实际核上单位及跨核配对证明原样成立。故 $P(X)$ 单射稠密，$P(X)\xi$ 循环；$B_*$ 是有界交换单位，因而 $q(u)e^w$ 循环。这完成 (1.6)。

## 9. 明确的新 canonical 碰撞实例与剩余点

对
$$
q_\rho(z)=(z-\rho)^2-1
$$
有 $\Gamma(q_\rho)=\{\rho+1\}$。因此
$$
\boxed{
\frac{4(\operatorname{Re}\rho+1-\log2)^2}{\pi^2}
+\frac{2(\operatorname{Im}\rho)^2}{\pi^2}>1
\Longrightarrow
\bigl((u-\rho)^2-1\bigr)e^w\text{ 循环}.
}
\tag{9.1}
$$
当 $\rho$ 为实时，明确充分区域是
$$
\rho<\log2-1-\pi/2
\quad\text{或}\quad
\rho>\log2-1+\pi/2.
\tag{9.2}
$$
所以 $\rho=\pm2$ 均给 (1.7)。在 $\rho=2$ 时根 $1$ 仍在椭圆内，但它不满足 $q(1-2)=0$；真正发生平移碰撞的根 $3$ 已在椭圆外。这正是只检查 $\Gamma(q)$ 而不是要求全部根在椭圆外的加强。

原危险平方对应 $\rho=0$。其碰撞根 $1$ 满足
$|1-\log2|<\pi/2$，仍位于椭圆内部。另一方面
$|-1-\log2|>\pi/2$，所以 $-1$ 被有限谱轨道论证排除；这与已有安全分支结论一致，不能替代对 $+1$ 分支的处理。

边界等号不由本稿的严格指数分离排除。多次有限 gauge 给的有界零字符扰动，其指数型本身为 0，也不会仅凭这一指示函数自动缩小椭圆。规范 $u^2-1$、一般未知限制的稠密像和完整 Hilbert ISP 仍然开放。

