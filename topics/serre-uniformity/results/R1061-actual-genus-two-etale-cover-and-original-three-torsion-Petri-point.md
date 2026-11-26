# R1061：原有限和的实际无分歧九次覆盖与固定三挠 theta 点

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o1_theta / o2_high_coefficient / root。

**已证明：原 $S_n$ 是一条固定亏格二曲线上、一个明确三挠点处的 Raynaud–Petri 读数；其非零准确等价于该点的 Raynaud theta 除子光滑。** 覆盖、分支、三挠线、Frobenius 交换及实际微分尺度全部保留。光滑性本身尚未证明；相邻角色的 ordinary 性不自动给这一结论。

## 1. 同一个原曲线的实际九次覆盖

保持 R1059–R1060 的原函数与微分：
$$
p=6N+5\ge41,\quad n=(p-2)/3,\quad
s^2=-3,\quad\kappa=3s,
$$
$$
X=X_0(108):\quad z^3=1-\kappa x^3,\qquad
w^3=1+\kappa x^3,\qquad
\Omega=\frac{dx}{z^2w^2}.
$$
这里 $w$ 是 R1059 的 $w_0$，不是原深盘参数。
在代数闭域上令 $(\mu_3)^3$ 逐坐标作用，指数记为
$(a,b,c)\in\mathbf F_3^3$。取实际子群
$$
H=\{2a+b+c=0\},\qquad |H|=9.
$$
设 $t=x^3$、$v=x^2zw$，则它们均为 $H$ 不变量，并满足
$$
v^3=t^2(1+27t^2).
$$
三个 Kummer 根 $x,z,w$ 在 $t=0,\kappa^{-1},-\kappa^{-1}$
分别有独立的非三倍赋值，故 $[k(X):k(t)]=27$；
$v$ 的三次方在零点有二阶零，不是立方，故
$[k(t,v):k(t)]=3$。于是 $k(t,v)=k(X)^H$。

置
$$
R=v/t=zw/x,\qquad Y=54t-R^3=27x^3-x^{-3}.
$$
由 $R^3=t^{-1}+27t$ 得
$$
\boxed{\quad C:\ Y^2=R^6-108,\qquad \pi:X\longrightarrow C.\quad}
\tag{1061.1}
$$
反式 $t=(Y+R^3)/54$、$v=Rt$ 证明这是准确商函数域。
$p>3$ 时 $C$ 光滑、亏格二；R1059 的实际 $X$ 亏格十。
$\pi$ 可分且次数九，Riemann–Hurwitz 给
$2\cdot10-2=9(2\cdot2-2)$，总分歧除子为零。
所以 $\pi$ 是原曲线上的实际无分歧 $H$-覆盖。

直接微分，不留待定常数：
$$
\frac{dR}{dx}=\frac{27x^6-1}{x^2(zw)^2},\qquad
Y=\frac{27x^6-1}{x^3},
$$
因而
$$
\boxed{\quad
\pi^*(dR/Y)=x\Omega,\qquad
\pi^*(R\,dR/Y)=zw\Omega.
\quad}
\tag{1061.2}
$$
它们分别是 R1059 的实际 $c\,dq/q$ 和 $h\,dq/q$。

## 2. 原互逆角色对应的明确三挠线

令 $P_+,P_-$ 是 $C$ 的两个无穷点，以 $Y/R^3\to\pm1$ 标号；
令
$$
Q_z=(0,-6s),\qquad Q_w=(0,6s).
$$
$t=(Y+R^3)/54$ 满足
$$
\operatorname{div}(t)=3(P_--P_+),\quad
\operatorname{div}(1-\kappa t)=3(Q_z-P_+),\quad
\operatorname{div}(1+\kappa t)=3(Q_w-P_+).
$$
例如在 $t=\kappa^{-1}$，$R^3=t^{-1}+27t$ 对 $t$ 的导数为 $54$，
所以 $1-\kappa t$ 在 $Q_z$ 有准确三阶零。又
$$
\operatorname{div}(R)=Q_z+Q_w-P_+-P_-.
$$
因此
$$
D_\chi=Q_z-Q_w,\qquad
3D_\chi=\operatorname{div}
\left(\frac{1-\kappa t}{1+\kappa t}\right),\qquad
(z/w)^3=\frac{1-\kappa t}{1+\kappa t}.
\tag{1061.3}
$$
这是原覆盖内的具体 Kummer 线，不是任取三挠点。

它还来自实际二次椭圆映射
$$
q:C\longrightarrow E,\qquad
E:V^2=U^3-108,\quad U=R^2,\quad V=Y.
$$
令 $Q=(0,-6s)\in E$，则水平切线 $V=-6s$ 与三次曲线在 $Q$
有三重交点，所以 $Q$ 的阶恰为三。
$q^*Q=2Q_z$，$q^*O=P_++P_-$，结合 $\operatorname{div}(R)$ 得
$$
\boxed{\quad [D_\chi]=q^*[Q-O]\ne0.\quad}
\tag{1061.4}
$$
非零也可由 $\operatorname{Nm}_q q^*=[2]$ 在三挠上可逆直接确认。
$q$ 的分支点恰为 $Q,-Q$；
$\operatorname{div}(U)=Q+(-Q)-2O$，故双覆盖的分支平方根线是
$\mathcal O_E(O)$。实际微分满足
$$
q^*\left(\frac{dU}{2V}\right)=R\,dR/Y.
$$
此处使用的是 $U=R^2,V=Y$ 这个因子，没有换成 $R^{-2}$ 的另一椭圆因子。

因 $s^p=-s$，Frobenius 交换 $Q_z,Q_w$，故
$D_\chi^{(p)}=-D_\chi$。下文始终保留无序 pair
$\{\mathcal O(D_\chi),\mathcal O(-D_\chi)\}$ 的实际 Frobenius twist。

## 3. 八个非平凡角色的全部微分和 Cartier 输入

在 $H$ 内写 $c=a-b$。十条实际正则微分的角色为：

| 微分 | $H$ 指数角色 |
| --- | --- |
| $x\Omega,\ zw\Omega$ | $0$ |
| $\Omega,\ x^2\Omega$ | $2a,\ a$ |
| $z^2\Omega,\ w^2\Omega$ | $-(a+b),\ a+b$ |
| $z\Omega,\ w\Omega,\ xz\Omega,\ xw\Omega$ | $2a+b,\ -b,\ b,\ a-b$ |

八个非平凡角色各出现一次。也可直接由无分歧覆盖和 Riemann–Roch：
非平凡度零线 $\mathcal L$ 满足
$h^0(C,\Omega_C^1\otimes\mathcal L)=1$。

在指数记号下 $a=b+c$，原有序两条微分
$$
u=z^2\Omega=(a(q)-\zeta b(q))\,dq/q,\qquad
\nu=w^2\Omega=(a(q)-\zeta^2b(q))\,dq/q
$$
的角色正是 $b-c$、$c-b$，与 $z/w$ 互逆。
此处右侧 $a(q),b(q)$ 是 R1059 的固定形式，区别于本节的角色指数。
所以 (1061.3) 定位的正是原 $S_n$ 所用的两条线。

R1060 已给六条 CM 微分的 Cartier 为零；
在原 $p\bmod9\in\{2,5\}$ 范围，另外四条非 CM 微分的 Cartier 可逆。
因此上述四条非平凡 CM 角色各有一维 exact 微分空间，
四条非 CM 角色则没有 exact 微分。

底曲线 $C$ 本身的 Cartier 矩阵也准确为零：
$$
Y^{-1}=Y^{-p}(R^6-108)^{(p-1)/2}.
$$
以 $dR/Y,R\,dR/Y$ 为基，矩阵读取指数
$p-1,p-2,2p-1,2p-2$。它们模六分别为 $4,3,3,2$，
而所写多项式只含六倍数次项，故全部为零。
所以该亏格二曲线是 superspecial；它不是 ordinary 曲线。

## 4. 原 Raynaud–Petri 读数的严格下降

令 $F_C:C\to C^{(p)}$ 为相对 Frobenius，
$B_C$ 是 locally exact differential bundle：
$$
0\longrightarrow\mathcal O_{C^{(p)}}
\longrightarrow F_{C*}\mathcal O_C
\longrightarrow B_C\longrightarrow0.
$$
无分歧覆盖的 Frobenius base change 给
$\pi^{(p)*}B_C\simeq B_X$。
分解 $\pi^{(p)}_*\mathcal O_{X^{(p)}}$ 的实际 $H$ 角色后，
$u,\nu$ 正给
$$
H^0(C^{(p)},B_C\otimes\mathcal L),\qquad
H^0(C^{(p)},B_C\otimes\mathcal L^{-1})
$$
的各一维空间，其中
$$
\{\mathcal L,\mathcal L^{-1}\}
=\{\mathcal O(D_\chi),\mathcal O(-D_\chi)\}^{(p)}.
$$
上述维数一来自实际角色及 Cartier 核，未借助待证的 theta 光滑性。

用 R1059 的原有序配对规范
$\beta(\omega,\eta)=\mathscr C(F_\omega\eta)$、$dF_\omega=\omega$。
R1060 的已付 Euler 身份为
$$
s\kappa^n=(-1)^{N+1}3^{(p-1)/2}=1,
$$
因为 $(3/p)=(-1)^{N+1}$。
所以 $\kappa^n=1/s$，不是另一次单位重标。
R1059 的准确半线性给
$$
\beta_X(\nu,u)=(\kappa^nS_n)^{1/p}zw\Omega
=-\frac{S_n}{s}zw\Omega,
$$
$$
\boxed{\quad
\beta_X(u,\nu)=\frac{S_n}{s}zw\Omega
=\pi^*\left(\frac{S_n}{s}R\,dR/Y\right).
\quad}
\tag{1061.5}
$$
逆角色乘积按原覆盖的乘法下降，故 (1061.5) 就是 $C$ 上这两个
一维空间的 Raynaud 乘法。$C$ 的模型在 $\mathbf F_p$，
上式在相对 Frobenius 模型下采用同一坐标识别。
若交换输入顺序，符号随之改变；没有省去 $\mathbf F_{p^2}$ 半线性。

## 5. 精确的 theta 光滑性判据和剩余问题

令 $\Theta_{B_C}\subset\operatorname{Jac}(C^{(p)})$
为 $B_C$ 的 determinant theta 除子。
Tong 的 Proposition 2.2.1、Corollary 2.2.2 说明：
在给定线 $\mathcal L$ 处，它光滑当且仅当
$h^0(B_C\otimes\mathcal L)=1$，且与逆线的一维空间乘法非零；
光滑时，切空间是该乘法输出微分的 annihilator。

本文已支付维数一及实际输出，故
$$
\boxed{\quad
S_n\ne0
\quad\Longleftrightarrow\quad
\Theta_{B_C}\text{ 在原实际三挠点 }\mathcal L\text{ 光滑}.
\quad}
\tag{1061.6}
$$
逆点给同一个条件。若光滑，其切线准确是
$H^1(C^{(p)},\mathcal O)$ 中 $R\,dR/Y$ 的 annihilator。
结合 R1059–R1060，
$$
A_p=-S_n/3,\qquad
f_N=\frac{t_{\rm CM}^2\delta'_p}{4(p+1)}A_p,\quad t_{\rm CM}^3=4,
$$
这仍是原 $f_N$ 的具体问题。

在 $p\bmod9\in\{2,5\}$，另外两条非 CM 角色直线上的四个三挠点不在
$\Theta_{B_C}$，由 R1060 ordinary 输入得到；这不推出目标点光滑。
Tong §4.2 的相应特殊光滑定理讨论 $p$ 挠点及指定的
ordinary / $p$-rank 条件，不能套给本 superspecial 曲线的三挠点。
后续须继续支付 (1061.6) 的右侧，或在同一实际双覆盖上求其
twisted-Cartier 导数；原同一本原标签筛选和 O0 仍未关闭。

## 6. 同一椭圆模型的规范 $p$ 极原函数

保持 $E:V^2=U^3-108$、$\omega=dU/(2V)$，
并记 $z_O=-U/V$ 为 $O$ 处参数，避免与§1的 $t$ 混淆。
置 $m=3N+2=(p-1)/2$、$\ell=2N+2$。
唯一取定
$
S(T)=\sum_{j=0}^N a_jT^j,\qquad a_N=-1,\qquad
\frac{a_j}{a_{j-1}}=\frac{6j-1}{108(6j+2)}\quad(1\le j\le N),
$
$
\Psi(P)=V U S(U^3),\qquad \delta=-216a_0.
\tag{1061.7}
$
所有分子、分母在 $p$ 中非零，所以 $\delta$ 是单位。
用 $D=d/\omega$，$DU=2V,DV=3U^2$，直接算得
$
D\Psi=(5T-216)S+6T(T-108)S'=\delta.
$
中间各项由递推消去，最高项因 $6N+5=p$ 消失。因此
$
\boxed{d\Psi=\delta\omega,\quad
\operatorname{PP}_O\Psi=z_O^{-p},\quad \Psi(-P)=-\Psi(P).}
\tag{1061.8}
$
$\Psi$ 只在 $O$ 有准确 $p$ 阶极，最高系数为一。
因为其微分全纯，其所有负 Laurent 指数必须为 $p$ 的倍数；
故所写 principal part 完整，且奇性令常数项为零。

对一般 $Q'\ne O$，定义普通 chord slope
$
M(P,Q')=\frac{V(P)-V(Q')}{U(P)-U(Q')}.
$
有全有理加法律
$
\boxed{\Psi(P+Q')=\Psi(P)+\Psi(Q')+M(P,Q')^p.}
\tag{1061.9}
$
证明：两侧之差对 $P$ 的微分为零。
仅有的潜在极点是 $O,-Q'$，其 $p$ 阶主部由 slope 的
$-z_O^{-1}$ 和 $z_{-Q'}^{-1}$ 首项准确消去。
余下差全局正则；在 $O$ 读常数为零。一般点的恒等式给全有理恒等式，
切线情形按延拓解释。没有将零导数函数未经极点检验当作常数。

## 7. 原 Miller 函数的完整首 $a^p$ 变分

固定原 $Q=(0,v_0)$，$v_0=-6s$。取
$
g_Q(P)=\frac{U(P)}{(V(P)-v_0)^\ell}.
$
由实际 divisor，
$
\operatorname{div}(g_Q)=(-Q)-p(Q)+(p-1)(O),
\qquad g_Q=z_O^{p-1}(1+O(z_O)).
\tag{1061.10}
$
后一个首项为一，因为 $\ell$ 偶。还可直接核
$
d\log g_Q=\frac{V-v_0}{U}\,\omega.
$

对 $Q$ 的形式邻域中一般点 $Q+A$，令 $a=z_O(A)$。
按相同 $O$ 首项归一，$g_{Q+A}$ 唯一由
$
\operatorname{div}(g_{Q+A})
=([p](Q+A))-p(Q+A)+(p-1)(O)
$
确定。这个 degree-zero divisor 在 $\operatorname{Pic}^0(E)$ 中为零；
局部基变换及首项刚化给所用形式族。

这里须区分 $[p]$、相对 Frobenius 和 Picard 上的拉回。
当前 $E/\mathbf F_p$ 中，立方在 $\mathbf F_p$ 上为双射，
故直接点数和给 $a_p(E)=0$。
标准椭圆 Frobenius 方程于是给实际 endomorphism
$F^2+[p]=0$。因此在这个明确的 $\mathbf F_p$ 模型里，
$[p]A=-F^2A$ 的参数变化始于 $a^{p^2}$。
这一步没有把一般线丛的相对 Frobenius 拉回写作点的 $p$ 倍。

准确首项是
$
\boxed{
\frac{g_{Q+A}(P)}{g_Q(P)}
=1+a^p\{\Psi(P-Q)-\Psi(-Q)\}+O(a^{p+1}).
}
\tag{1061.11}
$
证明分三步。首先，移动的 $p$ 重极点在局部是一个单位乘
$z_{Q+A}^{-p}$，其比值的非平凡变化最早出现在 $a^p$；
简单零点 $[p](Q+A)$ 则到 $a^{p^2}$ 才动。
所以 $1\le j<p$ 的系数无任何极点，由 $O$ 首项归一全为零。
其次，$a^p$ 系数记为 $H(P)$，它只在 $Q$ 有至多 $p$ 阶极，
主项为 $z_Q^{-p}$。$d\log g_{Q+A}$ 的极点只有
$O,[p](Q+A)$；到 $a^p$ 阶其主部不变，故 $dH$ 全纯。
最后，$H-\Psi(P-Q)$ 的最高极部消去，剩余极阶小于 $p$，
而其微分全纯，迫所有剩余极部为零。于是差为常数；
$H(O)=0$ 将它固定为 $-\Psi(-Q)$，得到 (1061.11)。

原 $Q$ 处 $\Psi(Q)=\Psi(-Q)=0$。
由 (1061.9)，首变分还可准确写作
$
H(P)=\Psi(P)+
\left(\frac{V(P)+v_0}{U(P)}\right)^p.
\tag{1061.12}
$
全部原尺度已付；这仍不等于目标 Petri 读数已为单位。

## 8. 首变分来源的完整 Cartier 单系数

定义同一原有理来源
$
F_Q=U^m g_Q
=\left(\frac{V+v_0}{V-v_0}\right)^{N+1}.
$
由于 $\omega=dV/(3U^2)$、$p-2=3(2N+1)$，
$
F_Q\omega=
\frac{(V-v_0)^N(V+v_0)^m}{3U^p}\,dV.
$
分子次数 $4N+2<p-1$，所以
$
\mathscr C(F_Q\omega)=0.
\tag{1061.13}
$
故 (1061.12) 中的整个 slope 项在这次准确 Cartier 读取中消失：
$
\mathscr C(F_QH\,\omega)=\mathscr C(F_Q\Psi\,\omega).
$
这里的消失有 (1061.13) 的完整次数证明，不是任意丢掉 $p$ 次修正。

令 $M=4N+3$，用 $V^2=T-108$ 唯一写
$
(V-v_0)^M=E_N(T)+V O_N(T),
\qquad \deg E_N,\deg O_N\le2N+1 .
$
$\alpha=F_Q\Psi\omega$ 准确为
$
\alpha=\frac{U^{3N+4}S(U^3)}
{2(V-v_0)^p}
\{E_N(U^3)+V O_N(U^3)\}\,dU.
$
置
$
e=[T^N]S(T)E_N(T),\quad
o=[T^N]S(T)(T-108)^{3N+3}O_N(T).
\tag{1061.14}
$
even 项的最高 $U$ 次为 $12N+7=2p-3$，全部指数为 $1\bmod3$，
Cartier 仅读取 $p-1$ 次。odd 项使用
$V=V^{-p}(T-108)^{3N+3}$；其最高次为
$21N+16<4p-1$，全部指数仍为 $1\bmod3$。
可读的 $jp-1$ 必须有 $j=1\bmod3$，故此项也只有 $p-1$ 次。
因此保留全部半线性后，
$
\mathscr C(\alpha)=
\frac{e^{1/p}V+o^{1/p}}{V-v_0}\,\omega.
$
在 $Q$，原 $\alpha$ 的极阶是
$p-m-1=m<p$，故 Cartier 之后极阶至多一。
但 $V-v_0$ 在 $Q$ 有三阶零；若上式分子在 $Q$ 非零，
便产生三阶极，矛盾。于是 $o^{1/p}=-v_0e^{1/p}$，从而
$
\boxed{\mathscr C(F_QH\,\omega)
=\mathscr C(F_Q\Psi\,\omega)=e^{1/p}\omega=-e\,\omega.}
\tag{1061.15}
$
最后一式因为 $S\in\mathbf F_p[T]$，
$M$ 奇使 $E_N$ 的每个系数都是 $v_0$ 的奇次幂乘
$\mathbf F_p$ 元素，故 $e^p=-e$。
所有 scalar 都由原有理函数确定。

这是 (1061.11) 的完整首变分经过指定 Cartier 来源后的实际有限系数，
不是只读 primitive 的 $\delta$。
虽然 $\delta$ 及
$E_N(0)=(-2v_0)^M/2$ 都是单位，(1061.14) 的完整卷积
$e$ 非零仍须证明。本文也未省略后续将该形式族作为 Picard 参数时的
相对 Frobenius 记号；不能把某个错误的平移参数据此称作已付导数。


## 9. 新系数 $e$ 与原 $S_n$ 的实际非零等价

本节严格支付几何参数与局部生成元，证明
$
\boxed{\quad e\ne0\ \Longleftrightarrow\ S_n\ne0.\quad}
\tag{1061.16}
$
这不是数值恒等式 $e=cS_n$ 的猜测，亦不从其中一个较低系数的单位推出两者非零。

### 9.1 原双覆盖的两个实际 summand

在 $E$ 上记 $N=\mathcal O_E(O)$，在相对 Frobenius twist 上记 $N_p$。
§2的原双覆盖给
$q_*\mathcal O_C=\mathcal O_E\oplus N^{-1}$。
将 locally exact bundle 的定义推到 $E^{(p)}$，
按覆盖 involution 的正负角色分解，得
$
q^{(p)}_*B_C=B_E\oplus\mathcal A,\qquad
0\longrightarrow N_p^{-1}
\longrightarrow F_*N^{-1}
\longrightarrow\mathcal A\longrightarrow0.
\tag{1061.17}
$
负角色的包含准确来自 $R^p=R\,U^m$；$\mathcal A$ 是秩 $p-1$、
度零的向量丛。

Grothendieck duality（以原 $\omega$ 刚化）给
$
0\longrightarrow\mathcal A^\vee
\longrightarrow F_*N
\xrightarrow{\ \mathscr C_{\rm rel}\circ U^m\ }N_p
\longrightarrow0.
\tag{1061.18}
$
该映射可在局部 $1,U,\ldots,U^{p-1}$ 基上直接核：
Frobenius dual trace 正是 $U^{p-1}dU$ 的系数读取。
它也由原 odd 微分
$f\omega/R$ 的
$\mathscr C(f\omega/R)=\mathscr C(fU^m\omega)/R$
得到，所以没有另换双覆盖或 branch 平方根。

对任意度零 $\mathcal L$，(1061.18) 两端的 $H^0$ 都是一维，
相应 $H^1$ 都为零，因为实际线丛
$N\otimes F^*\mathcal L$、$N_p\otimes\mathcal L$ 的度都是一。
两条线丛间的局部行列式记为 $\phi$，它是
$\Theta_{\mathcal A^\vee}$ 的实际局部方程。

这里没有由“秩一”假设该行列式非零。
例如 Tong Lemma 4.2.3.1(1) 从上述所有 twist 的
$h^0=1,h^1=0$ 给 $F_*N$ 稳定，其对偶 $F_*N^{-1}$ 稳定。
若 $\mathcal A$ 有正度真子丛，其在 $F_*N^{-1}$ 中的原像
度至少零、秩小于 $p$，违反斜率 $-1/p$ 的稳定性。
故 $\mathcal A$ 半稳定、度零；椭圆曲线上这类丛的一般度零 twist
无截面，所以其 determinant theta section 并非恒零。
这只支付存在性，不支付目标点的简单性。

### 9.2 相对 Frobenius 参数与原 Miller 刚化

令 $F:E\to E^{(p)}$，$V_E:E^{(p)}\to E$ 为 dual isogeny。
对实际 Picard 点 $FP$，
$
F^*\mathcal L_{FP}=\mathcal L_{V_EFP}=\mathcal L_{[p]P}.
$
选择 Poincaré 的有理 frame $\ell_P$，
其 divisor 为 $(P)-(O)$、在 $O$ 的极首项为 $1/z_O$。
再乘 $N$ 的 canonical section $s_O$，则
$
g_P\,\ell_P^p\,s_O
$
是 $H^0(N\otimes F^*\mathcal L_{FP})$ 的真实局部生成元：
其 divisor 是 $([p]P)$，且在 $O$ 的值为一。
目标生成元 $\ell_{FP}s_O$ 也在 $O$ 的值为一。
因此该具体 Cartier 标量与 $\phi(FP)$ 的比较因子是局部单位，
不是尚未证明非零的 period。

现在 $P=Q+A$，源参数 $a=z_O(A)$，
目标 $FP$ 相对 $FQ=-Q$ 的局部参数为 $a^p$。
必须用对 $k[[a]]$ 线性的相对 Cartier；不能对参数 $a$ 取 $p$ 次根。
在 $E^{(p)}$ 的坐标 $U',V'$ 中，§8的同一次读取给
$
\mathscr C_{\rm rel}(F_Q\Psi\omega)=e\,\omega^{(p)}.
$
具体分母为 $V'-v_0^p=V'+v_0$，分子为
$eV'+o=e(V'+v_0)$，因为 (1061.15) 的等价关系是 $o=v_0e$。
本文先前固定的 absolute Cartier 经标量 Frobenius 逆识别后才写成
$e^{1/p}\omega$。这两个表达不可混同为同一线性算子。

由 (1061.11)–(1061.15)，$\phi(FP)$ 的 $a^p$ 系数是
单位乘 $e$；常数项为零，任何生成元的换标在此只乘非零常数。
因此
$
e\ne0
\quad\Longleftrightarrow\quad
\phi\text{ 在 }FQ=-Q\text{ 有简单零}.
\tag{1061.19}
$

### 9.3 回到原 Petri 点，保留切向

Serre 对偶给
$\Theta_{\mathcal A^\vee}=[-1]^*\Theta_{\mathcal A}$，
所以 (1061.19) 等价于 $\Theta_{\mathcal A}$ 在 $Q$ 简单。
对原非零三挠线，$B_E$ 因子局部为单位：
因为 $\mathcal L$ 及 $F^*\mathcal L$ 都非平凡，
定义序列直接给 $H^0(B_E\otimes\mathcal L)=H^1(B_E\otimes\mathcal L)=0$。
由 (1061.17)，$\Theta_{B_C}$ 限制到实际 $q^*E$ 后，
其在 $q^*Q$ 的局部方程因而与 $\Theta_{\mathcal A}$ 相差单位。

在§4固定的 Cartier 识别中，实际 Petri 输出是 $(S_n/s)q^*\omega$。
它在 $q^*E$ 切向上的读取通过
$\operatorname{Nm}_q\circ q^*=[2]$ 正好为
$2S_n/s$ 乘原非零切向；相对版本取相应 Frobenius twist，非零条件完全一致。
所以这个限制的零点简单当且仅当 $S_n\ne0$；
结合 (1061.19) 得 (1061.16)。
这也排除了“环境 theta 光滑但所取限制正好相切”的遗漏。

## 10. 同一个原配对的另一条完整有限 primitive

以下式子可独立比较§8的来源，绝不把两个不同卷积擅自相等。
记 $\eta=z/w$，原 $u=\eta h,\nu=\eta^{-1}h$，且 $h=q^*\omega$。
由§1的实际函数，
$
(\eta^3)^2=\frac{V-v_0}{V+v_0}.
$
由于 $\ell$ 偶，准确有
$
\nu=\eta^p F_Q\omega,\qquad
u=\eta^{-p}F_Q^{-1}\omega
$
（等式在原覆盖上拉回）。

任选多项式 $I(V)$ 满足
$
I'(V)=(V-v_0)^N(V+v_0)^m,\qquad \deg I=4N+3<p.
$
全部积分分母都为单位，且
$
H_+(P)=\frac{I(V)}{3U^p},\qquad dH_+=F_Q\omega.
$
故 $\eta^pH_+$ 是原 $\nu$ 的真实有理 primitive。
其与 $u$ 相乘后，两个 $\eta$ 的 $p$ 次幂准确消去。
置
$
K=[V^{p-1}]\,I(V)(V-v_0)^m(V+v_0)^N.
$
源的总次数为 $8N+5<2p-1$，只读 $p-1$ 次，于是
$
\beta_X(\nu,u)=\pi^*q^*
\left(\frac{K^{1/p}}3\,\omega\right).
$
与原 (1061.5) 的有序符号比较，得到
$
\boxed{\quad K=-sS_n.\quad}
\tag{1061.20}
$
$I$ 的任意常数不影响 $K$，因为附乘多项式次数 $4N+2<p-1$。

另外，完全安全的 beta 积分给
$
I(v_0)-I(-v_0)
=(-1)^N(2v_0)^{4N+3}\frac{N!\,m!}{(4N+3)!}\ne0.
$
这是端点差的单位，不是 (1061.20) 的系数单位。
同样，分部积分仅给另一个真实系数
$
K_2=[V^{p-1}]\,I(V)(V^2-v_0^2)^{2N+1},\qquad
e=-\delta K_2/3.
$
它的权与 $K$ 不同。§9已经几何地支付 $e\ne0\iff S_n\ne0$，
但没有据此编造数值身份 $K_2=K$，也没有从端点差排除任一卷积相消。



## 11. 同一个指定值的有界第一原函数及准确常数

保持本篇原模型 $E:V^2=U^3+v^2$，
$v=-6s$、$v^2=-108$、$\omega=dU/(2V)$。
以下写 $\mathscr D=d/\omega$，并置
$
p=6k-1,\quad k=N+1,\quad m=3k-1=(p-1)/2,\quad
z=(1-V/v)/2,\quad K=\mathbf F_p(v).
$
本节的 $z$ 仅为 $E$ 上这个仿射函数，整数 $k$ 不表示底域。
全部 Cartier 等式采用§§9–10固定的相对 Cartier；
输出微分为 $\omega'$，底域常数不取额外 $p$ 次根。
既有规范是
$
\mathscr D U=2V,\quad \mathscr D V=3U^2,\quad
\mathscr D\Psi=\delta,\quad
\mathscr C_{\rm rel}(F_Q\Psi\omega)=e\omega'.
$

存在唯一 $P\in K[V]$、$\deg P\le k-1=N$，使
$
3(V^2-v^2)P'(V)+2VP(V)=z^k-h,\qquad
h=\frac{(1/3)_k}{(2/3)_k}.
\tag{1061.21}
$
这里没有从 $h$ 非零猜测原函数。
令 $L_1=3(V^2-v^2)\partial_V+2V$，则
$
L_1(V^j)=(3j+2)V^{j+1}-3jv^2V^{j-1}.
$
对 $0\le j\le k-1$，最高系数 $3j+2$ 都是单位，
故 $L_1$ 从次数至多 $k-1$ 到次数至多 $k$ 的像有余维一。
其归一余核泛函 $\lambda(1)=1$ 由
$
\lambda(V^{2r+1})=0,\qquad
\lambda(V^{2r})=v^{2r}\frac{(1/2)_r}{(5/6)_r}
$
给出。在次数至多 $k$ 的范围，所有分母 $6r-1\le3k-1<p$。

为计算 $\lambda(z^k)$，可先在有理系数域用归一 Beta 积分
$
\lambda(f)=
\frac{\int_0^1 f(v(1-2z))z^{-2/3}(1-z)^{-2/3}\,dz}
     {B(1/3,1/3)}.
$
若 $w(z)=z^{-2/3}(1-z)^{-2/3}$，则
$(3z(1-z)w(z))'=(1-2z)w(z)$，且端点边界项为零。
分部积分遂给 $\lambda(L_1P)=0$，并且
$
\lambda(z^k)
 =B(k+1/3,1/3)/B(1/3,1/3)
 =(1/3)_k/(2/3)_k.
$
这是有限有理恒等式的证明；上述安全分母允许直接约到原特征 $p$。
故 $z^k-h$ 恰在像中，存在唯一所述 $P$。
特别地，令 $G=UP(V)$，则
$
\mathscr D G=z^k-h.
\tag{1061.22}
$

原常数 $h$ 可完全初等地化为原立方根。令
$
A_f=(3k-1)!,\qquad B_f=(k-1)!,\qquad C_f=(2k-1)!.
$
由于 $1/3=2k$、$2/3=4k$ 于 $\mathbf F_p$，逐项反射给
$
(1/3)_k=A_f/C_f,\qquad
(2/3)_k=(-1)^kC_f/B_f,\qquad
h=(-1)^k A_fB_f/C_f^2.
$
另一方面
$
C_f=2^{k-1}B_f\prod_{j=1}^k(2j-1),\qquad
\prod_{j=1}^k(2j-1)=(-2)^kA_f/C_f;
$
第二式逐项使用 $p-(2j-1)=2(3k-j)$。
所以
$
\boxed{\quad h=2^{1-2k}=2^{4k-1},\qquad h^3=2.\quad}
\tag{1061.23}
$
全过程的阶乘指标均小于 $p$。
在已固定的原 $\mathbf F_p$ 立方根规范下，
$t_{\rm CM}^3=4$ 的残值与立方映射双射给
$\overline{t_{\rm CM}}=h^2$。
这只确定第一原函数中的常数，本身不证明 $e$ 或 $S_n$ 非零。

还须把该有界原函数接回原 $e$。
原加法律和 $Q=(0,v)$、$3Q=O$ 给
$
\tau_Q^*F_Q=z^k,\qquad
\tau_Q^*\Psi=\Psi+((V-v)/U)^p.
$
第一式亦可由原 divisor 及在 $-Q$ 处的 leading value 一核确定：
两边 divisor 均为 $3k(Q-O)$，在 $-Q$ 的值均为一。
相对 Cartier 与该平移相容，目标上是 $\tau_{FQ}$；
它固定 $\omega'$。
由于 $\mathscr C_{\rm rel}(F_Q\omega)=0$，
新增的 $p$ 次幂斜率项准确消去，得到
$
\mathscr C_{\rm rel}(z^k\Psi\omega)=e\omega'.
$
由 (1061.22)，$W=G+h\Psi/\delta$ 满足 $dW=z^k\omega$。
另外 $\Psi\omega=\tfrac12 U S(U^3)dU$
是次数 $3N+1<p-1$ 的多项式微分，故其 Cartier 为零。
对 $d(W\Psi)$ 施 Cartier，严格得到
$
\boxed{\quad e\omega'=-\delta\,\mathscr C_{\rm rel}(G\omega).\quad}
\tag{1061.24}
$
这里 $\delta\in\mathbf F_p^\times$ 为原固定常数；
没有混用相对参数线性与绝对 Cartier 的 $p$ 次根。

## 12. 指定值为零与真实二次积分的精确等价

定义 $K$-线性空间
$
\mathcal W=\{UP(V)\omega:\deg P\le N\}.
$
其维数为 $N+1$；每条微分只在 $O$ 有极，
极阶至多 $3N+2=m<p$，而唯一可能的留数由全局留数定理为零。
Cartier 的局部指数公式遂给
$\mathscr C_{\rm rel}(\mathcal W)\subset K\omega'$。

这个线性泛函确实非零，不能从一般的完美配对代替。
直接写
$
U\omega=\frac{U(U^3+v^2)^m}{2V^p}\,dU.
$
分子最高次数 $3m+1<2p-1$；
唯一 Cartier 指数 $p-1$ 对应 $3j+1=p-1$，即 $j=2N+1$。
故
$
\mathscr C_{\rm rel}(U\omega)
 =\binom m{2N+1}(v^2)^{N+1}\omega'.
\tag{1061.25}
$
右侧为单位，所有阶乘指标都小于 $p$。
因此 $\ker(\mathscr C_{\rm rel}|_{\mathcal W})$ 的维数恰为 $N$。

对 $\deg R\le N-1$，实际微分为
$
d(U^2R(V))
 =U\{3(V^2-v^2)R'(V)+4VR(V)\}\omega.
$
记 $L_2=3(V^2-v^2)\partial_V+4V$。
其在 $V^j$ 上的最高项系数为 $3j+4$，
对 $0\le j\le N-1$ 全部为单位，所以该 $N$ 维像是单射，
且因其为 exact differential 全部落在上述 Cartier 核中。
两边维数相同，得到
$
\ker(\mathscr C_{\rm rel}|_{\mathcal W})
 =\{d(U^2R(V)):\deg R\le N-1\}.
\tag{1061.26}
$
这个证明支付了有界原函数的存在性。
一般的 Cartier 为零不允许无条件压低原函数极阶，
例如 $\omega$ 的原函数 $\Psi/\delta$ 有 $p$ 阶极；
本式使用实际空间及明确非零的 Cartier 泛函。

综合 (1061.21)、(1061.24)、(1061.26)，得到保留原来源的等价条件：
$
\boxed{
\begin{aligned}
e=0\quad\Longleftrightarrow\quad&
 \exists R\in K[V],\quad\deg R\le N-1,\\
&9(V^2-v^2)^2R''+36V(V^2-v^2)R'
 +(20V^2-12v^2)R=z^k-h.
\end{aligned}}
\tag{1061.27}
$
必要性由 $P=L_2R$ 得到；
充分性由 $L_1$ 在所需次数范围的单射性，
迫给定第一原函数 $P$ 就是 $L_2R$。
展开 $L_1L_2$ 时 $R'$ 系数准确为 $36V(V^2-v^2)$，
常数项为 $20V^2-12v^2$；所需 $R$ 若存在则唯一。

这是实际函数的二次积分方程。
当前仍须排除该多项式解，或另由原输入证明 $e\ne0$。
$h^3=2$、$h$ 的单位性及 (1061.25) 的另一非零读数，
均不能替代指定 $P$ 的非零读数。
由§9，(1061.27)也等价于原 $S_n=0$，本节尚未排除它。


## 13. 实际 Miller 函数的全参数 Lamé 恒等式

本节仍在同一 $E:V^2=U^3+v^2$、$v^2=-108$ 上，
使用原 $\omega=dU/(2V)$、$\mathscr D=d/\omega$。
另一个点写为 $R=(u_R,v_R)$，避免与固定常数 $v$ 混同。定义
$
r_R(T)=\frac{V(T)+v_R}{U(T)-u_R}.
$
一般 $R$ 时，$r_R\omega$ 的唯一极为 $R,O$，
留数分别为 $1,-1$；以下恒等式从一般点作有理延拓。
准确 Cartier 式为
$
\begin{aligned}
\mathscr C_{\rm rel}(r_R\omega)
 &=\{r_{R^{(p)}}-\Psi(R)\}\omega',\\
\mathscr C_{\rm abs}(r_R\omega)
 &=\{r_R-\Psi(R)^{1/p}\}\omega.
\end{aligned}
\tag{1061.28}
$
第一式 $r_{R^{(p)}}=(V'+v_R^p)/(U'-u_R^p)$；
第二式在固定几何点上作绝对 Cartier，两者不可混用。

直接写
$
r_R\omega=\frac12\frac{dU}{U-u_R}
       +v_R\frac{\omega}{U-u_R},\qquad
\frac{\omega}{U-u_R}
 =\frac{(U-u_R)^{p-1}(U^3+v^2)^m}
        {2V^p(U-u_R)^p}\,dU.
$
后一个分子最高次数 $(5p-5)/2<3p-1$，
所以相对 Cartier 只读 $U^{p-1},U^{2p-1}$。
设二者系数为 $A_R,B_R$，则
$
\mathscr C_{\rm rel}\!\left(\frac{\omega}{U-u_R}\right)
 =\frac{A_R+B_RU'}{U'-u_R^p}\,\omega'.
$
由 $(U-u_R)^{p-1}=\sum_{a=0}^{p-1}u_R^{p-1-a}U^a$，
第二系数准确为
$
B_R=\sum_{i=0}^N\binom m{2k+i}(v^2)^{N-i}u_R^{3i+1}
   =-u_RS(u_R^3).
$
最高系数为 $1=-a_N$；相邻系数比为
$
\frac{k-i}{(2k+i)v^2}
 =\frac{6i-1}{108(6i+2)},
$
与 (1061.7) 的 $a_i/a_{i-1}$ 相同，全部分母为单位。
两个真实留数固定相对 Cartier 在 $R^{(p)},O$ 的主部，
故与 $r_{R^{(p)}}\omega'$ 的差是正则常数倍。
上式的 $U'$ 系数把常数准确定为
$v_RB_R=-\Psi(R)$，证明第一式；取底域常数的 $p$ 次根给第二式。
这里仅作有限第一矩形计算，没有在整个解析 sigma 展开中删去 $p$ 分母。

对一般 $P\ne O$，取本篇 $O$ 首项为 $z_O^{p-1}$ 的原 Miller 函数
$g_P$，其 divisor 为 $([p]P)-p(P)+(p-1)(O)$。则
$
\boxed{\quad
\mathscr D\log g_P(T)=r_{[p]P}(T)+\Psi(P)^p.
\quad}
\tag{1061.29}
$
证明先在固定几何点 $P$ 用绝对 Cartier：
$d\log g_P-r_{[p]P}\omega$ 无极，故为常数 $c(P)\omega$。
对数微分被绝对 Cartier 固定，而 $\mathscr C_{\rm abs}(\omega)=0$；
(1061.28) 迫 $c(P)=-\Psi([p]P)^{1/p}$。
原 $[p]P=-P^{(p^2)}$、$\Psi$ 的奇性及 $\mathbf F_p$ 系数，
给 $c(P)=\Psi(P)^p$。
它在所有一般几何点成立，故是实际有理函数族的恒等式；
没有把绝对 Cartier 对变动底参数误当线性。

定义固定全部常数的多项式
$
\mathcal R(U)=\sum_{j=0}^N\frac{a_j}{2(3j+2)}U^{3j+2}.
$
全部 $3j+2\le m<p$，并有
$
\mathcal R'(U)=\tfrac12 US(U^3),\qquad
\mathscr D\mathcal R=\Psi,\qquad
\boxed{\Psi^2=U^p+2\delta\mathcal R(U).}
\tag{1061.30}
$
最后一式：$\partial_U(\Psi^2)=\delta US(U^3)$，
且 $\Psi^2$ 最高项为 $U^p$。
减去 $U^p+2\delta\mathcal R$ 后，次数小于 $p$、导数为零；
在 $U=0$ 值为零，故恒零。
$\mathcal R$ 最高系数为 $-1/(2m)=1$，所以首项为 $U^m$。

曲线方程直接给 $\mathscr D r_R+r_R^2=2U+u_R$。
置
$
c(P)=\Psi(P)^p,\qquad t(P)=\delta\mathcal R(P)^p.
$
由 (1061.29)、$U([p]P)=U(P)^{p^2}$ 及 (1061.30)，
同一实际 Miller 函数满足
$
\boxed{\quad
(\mathscr D^2-2c(P)\mathscr D)g_P
 =2\{U-t(P)\}g_P.
\quad}
\tag{1061.31}
$
这是原 Miller divisor 和 Cartier 推出的 Lamé 恒等式，
参数、常数和函数均已指定。

## 14. 原目标的 Lamé moments 与完整半截边界

在上述 $O$ 首项归一的有理函数帧中，定义
$
M_j(P)\omega'=\mathscr C_{\rm rel}(U^jg_P\omega),\qquad
N_j(P)\omega'=\mathscr C_{\rm rel}(U^jVg_P\omega).
\tag{1061.32}
$
$0\le j\le m$ 的 $M_j$ 及 $0\le j\le m-2$ 的 $N_j$ 确为标量：
输入在 $O$ 正则，只可能在 $P$ 有至多 $p$ 阶极；
唯一极的留数为零，Cartier 后无极。
更高 moments 或所有 $g_P\Psi$ moments 不自动有此性质。

$g_P=z_O^{p-1}(1+\cdots)$、
$\omega=(1+\cdots)dz_O$ 的首项给 $M_0=1$。
对 (1061.31) 取 Cartier，又给真实旁读数 $M_1=t(P)$；
它始终与目标 $M_m$ 区别。

Cartier 消去 exact differential，分部积分允许把
(1061.31) 的形式伴随
$\mathscr D^2+2c\mathscr D-2U+2t$
分别作用于 $U^j,U^jV$。由
$
\mathscr D^2(U^j)
 =2j(2j+1)U^{j+1}+4j(j-1)v^2U^{j-2},
$
$
\mathscr D(U^jV)=(2j+3)U^{j+2}+2jv^2U^{j-1},
$
得到
$
\begin{aligned}
&(2j-1)(j+1)M_{j+1}+2cjN_{j-1}
 +2j(j-1)v^2M_{j-2}+tM_j=0,\\
&(2j+5)(j+1)N_{j+1}+c(2j+3)M_{j+2}
 +2cjv^2M_{j-1}+2j(j-1)v^2N_{j-2}+tN_j=0.
\end{aligned}
\tag{1061.33}
$
第一行取 $0\le j\le m-1$，第二行取 $0\le j\le m-3$；
带零整数系数的负指标项省略。
每个参与的 moment 都在已证明的正则范围内。

在原 $Q=(0,v)$，$c=t=0$，并有
$
M_0(Q)=1,\quad M_1(Q)=M_2(Q)=0,\quad
N_0(Q)=v/3,\quad N_1(Q)=N_2(Q)=0.
$
$N_0$ 的常数来自真实展开
$
\begin{aligned}
g_Q&=z_O^{p-1}\{1-(v/3)z_O^3+O(z_O^6)\},\\
V&=-z_O^{-3}(1+O(z_O^6)),\qquad
\omega=(1+O(z_O^6))dz_O.
\end{aligned}
$
所以 $Vg_Q\omega$ 的 $z_O^{p-1}dz_O$ 系数准确为 $v/3$。
其余四个零值由 (1061.33) 的首两步得到。

令 $P=Q+A$、$a=z_O(A)$ 为本篇同一平移参数。
由 $\mathscr D\Psi=\delta$、$\Psi(Q)=0$、
$\mathscr D\mathcal R=\Psi$、$\mathcal R(Q)=0$，
$
c(P)=\delta a^p+O(a^{2p}),\qquad t(P)=O(a^{2p}).
$
对 $0\le i\le N$，定义
$
B_i=N_{3i}(Q),\qquad
A_i=\delta^{-1}[a^p]M_{3i+2}(Q+A).
$
这是沿实际 $a^p$ 方向的导数，没有把 $c,t$ 当作独立自由变形。
$M_{3i+2}(Q)=0$ 由三步递推得到；
Miller 首变分保证低于 $a^p$ 的变分均为零。
原目标 $M_m$ 的首 $a^p$ 系数就是 $e$：
其 slope 的 $p$ 次幂修正乘
$\mathscr C_{\rm rel}(U^mg_Q\omega)=0$ 而准确消失。因此
$
\boxed{e=\delta A_N.}
\tag{1061.34}
$

由 (1061.33) 读基点与一阶项，得
$
B_0=v/3,\qquad A_0=-v/3,
$
$
\begin{aligned}
3i(6i+3)B_i+2(3i-1)(3i-2)v^2B_{i-1}&=0,\\
(6i+1)(3i+2)A_i+2(3i+1)B_i
 +6i(3i+1)v^2A_{i-1}&=0\quad(1\le i\le N).
\end{aligned}
\tag{1061.35}
$
所有需要除的整数非零模 $p$：
最大线性因子分别为 $6N+3=p-2$、
$6N+1=p-4$、$3N+2=m$。
第一行有准确积式
$
B_i=\frac v3(-v^2)^i
 \frac{(1/3)_i(2/3)_i}{(1)_i(3/2)_i}.
$
这给每个 $B_i$ 的单位性，不直接给非齐次第二行的 $A_i$ 单位。

置
$
H_i=(-v^2)^i\frac{(1)_i(4/3)_i}{(5/3)_i(7/6)_i}.
$
它满足第二行的齐次比例
$H_i/H_{i-1}=-6i(3i+1)v^2/((6i+1)(3i+2))$。
逐步除以 $H_i$ 并保留 $A_0=-v/3$，得到
$
\boxed{\quad
A_i=-\frac v3H_i
 \sum_{r=0}^i\frac{(2/3)_r^2(1/6)_r}{(r!)^2(3/2)_r}.
\quad}
\tag{1061.36}
$
简化准确使用
$
\frac{2(3r+1)}{(3r+2)(6r+1)}\frac{B_r}{H_r}
 =\frac v3\frac{(2/3)_r^2(1/6)_r}{(r!)^2(3/2)_r}.
$
对 $i\le N$，所有 Pochhammer 分母的整数因子仍小于 $p$，
$H_i$ 为单位。故 $e\ne0$ 等价于 $i=N$ 的指定半截和非零。

完整 Dixon 和不能替代这个半截。令 $n=2k-1=2N+1$，
在 $0\le r\le n$ 上有
$
\frac{(2/3)_r^2(1/6)_r}{(r!)^2(3/2)_r}
 \equiv
\frac{(-n)_r^2(k)_r}{(r!)^2(1-n-k)_r}\pmod p.
$
右侧为有理数域中良定的奇终止 Dixon 型项；
所有相关分母在该范围也非零模 $p$。
第 $n-r$ 项恰为第 $r$ 项的负数：
由 $(1-n-k)_n=(-1)^n(k)_n$ 及
$\binom n{n-r}=\binom nr$ 逐项即得。
从零到 $n$ 的完整和因而为零。
原目标只到 $N=k-1$，保留其中一半；
不能用完整 Gamma 求和给原半和单位。

全参数 Lamé、实际 moments 和半截身份均来自同一原 Miller/Cartier。
它们没有排除 (1061.27) 的多项式解，也未证明原 $S_n$ 非零；
$M_1$、$B_i$ 或整段 Dixon 和不能代替目标 $M_m$ 的首变分。

## 来源与本次核对

- [R1059](R1059-original-fN-actual-X108-Raynaud-pairing-and-inverse-central-sum.md)：原 $X_0(108)$ 函数、good 模型、固定微分尺度和 $S_n$ 配对。
- [R1060](R1060-actual-X108-nonCM-Cartier-and-nine-torsion-ordinary-input.md)：六条 CM 核、四条非 CM ordinary 输入及准确 Euler 标量。
- Jilong Tong, *Diviseur thêta et formes différentielles*, Math. Z. 264 (2010), 521–569，DOI 10.1007/s00209-009-0478-y；[作者原文](https://www.math.u-bordeaux.fr/~jtong/Recherche/Theta.pdf)，Proposition 2.2.1、Corollary 2.2.2（印刷541–542页），§4.2。此处只使用其准确光滑判据，不假设本固定曲线一般。

o1_theta给实际覆盖、三挠线和配对下降；o2_high_coefficient独立核角色、第一椭圆因子与分支线；root实读Tong所引原文，并手核全部函数域次数、无分歧性、两微分、divisor、角色、Frobenius及有序标量。无数学程序或窗口执行。

补充§§6–8：o2_high_coefficient给规范Ψ递推和完整first-p Cartier系数；root独立推Miller首变分和Ψ加法律，o1_theta独立核两式；root逐项核U/V两坐标的全部次数、Q处极阶、半线性及完整slope消去。Frobenius特征方程可见Andrew Sutherland [MIT 18.783 Lecture 8](https://math.mit.edu/classes/18.783/2022/LectureSlides8.pdf)第5张幻灯片。无数学执行。

补充§9：o1_theta给实际双覆盖/dual Cartier/Poincaré frame的非零桥，root独核相对Cartier的base线性、FQ参数、两个生成元、B_E单位因子及切向因子2，明确纠正relative/absolute标量约定。§10由root给原η的直接primitive与K=−sS，o2独核分部积分的K₂，所有不同权保留。全文无数学执行。

补充§§11–12：o1_theta给实际三平移、有界第一原函数和h的阶乘证明；root独核原参数、完整相对Cartier和分部积分，提出并证明实际空间上的单位Cartier读数与核维数，o1逐式独核。由此支付二次有界primitive的必要充分性；没有从极阶小于p直接假设原函数也有界。无数学程序执行。

补充§§13–14：o1_theta推原全参数Miller对数导数和Lamé源；root实读本篇原S递推并独核第一矩形Cartier、两处留数及Ψ²恒等式。root推完整M/N伴随递推、原Q处A/B变分和e=δA_N，o1独核全部pole范围、初值及半截身份。双方独立确认完整奇Dixon和的反对称性不支付半和单位。无数学程序执行。
