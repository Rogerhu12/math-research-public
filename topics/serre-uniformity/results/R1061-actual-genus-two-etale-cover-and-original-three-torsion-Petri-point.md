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


## 15. 退化有限域 Dixon 的完整双数字读数与实际半截边界

这一节核清一种可能误用的全 $q=p^2$ 输入，并得到半截多项式的一个
**真实加权矩单位**。它没有将该单位替换成 (1061.35) 的无权半和。
沿用 $p=6k-1$、$N=k-1$、$n=2k-1$，置
$
D_N(z)=\sum_{r=0}^N t_rz^r,\qquad
t_r=\frac{(2/3)_r^2(1/6)_r}{(r!)^2(3/2)_r}
\quad(0\le r\le n).
$
(1061.35) 的目标仍是 $D_N(1)$。

### 15.1 含退化项的全有限域函数

置 $q=p^2$，令 $\omega_q$ 为 Teichmüller character，
$\sigma=\omega_q^{-(q-1)/6}$。
Gauss 和使用 $g(\chi)=\sum_{x\in\mathbf F_q}\chi(x)\zeta_p^{\operatorname{Tr}(x)}$，
包括 $g(\varepsilon)=-1$。
定义 McCarthy 的规范函数
$
\mathcal H_q={}_3F_2^*
 \left(\begin{matrix}\sigma^4,\sigma^4,\sigma\\
 \varepsilon,\sigma^3\end{matrix};1\right)_q.
$
这里 $A=B=\sigma^4,C=\sigma$ 恰满足 $(BC)^2=A$，
所以不能直接用 McCarthy Theorem 1.11。
其 §4 Theorem 4.2 保留了这一退化情形；因为
$A\ne BC$ 且 $B,C\ne\varepsilon$，适用的准确式是
$
\mathcal H_q=
\sum_{R^2=A}
\frac{g(A^{-1}BC)g(RB^{-1})g(RC^{-1})g(R)g(R^{-1}BC)}
 {g(AB^{-1})g(AC^{-1})g(A)\,BC(-1)\,q}.
\tag{1061.37}
$
式中最后一个 Gauss 因子可能为 $g(\varepsilon)$，
不得用非平凡 character 的乘积公式除掉它。

对任意非平凡且阶整除 $p+1$ 的 $\chi$，它在
$\mathbf F_p^\times$ 上平凡。取 $\operatorname{Tr}(a)=0$、$a\ne0$。
trace-zero 纤维的 character 和为 $(p-1)\chi(a)$；
每个非零 trace 纤维的和相同，而总和为零，故其和为 $-\chi(a)$。
因此直接有 $g(\chi)=p\chi(a)$。
在本次六阶 characters 上，
$
g(\sigma)=g(\sigma^5)=g(\sigma^3)=(-1)^kp,\qquad
g(\sigma^2)=g(\sigma^4)=p.
$
又 $\sigma(-1)=1$。将 $R=\sigma^2,\sigma^5$ 逐项代入 (1061.37)，得
$
\boxed{\quad
\mathcal H_q=\frac{g(\sigma)^2}{q}
 \left(\frac{g(\sigma^5)}{g(\sigma^3)}-g(\sigma^2)\right)=1-p.
\quad}
\tag{1061.38}
$
这是完整 $q$ 函数的值，尚未是原 $D_N(1)$ 的任何范数式。

### 15.2 所有单位项的两个实际数字矩形

现在从定义读取 (1061.38) 模 $p$ 的每一个单位项。
置
$
a=2(q-1)/3,\quad c=(q-1)/6,\quad h=(q-1)/2,
$
并写 $g_b=g(\omega_q^{-b})$，下标一律模 $q-1$。
原定义准确成为
$
\mathcal H_q
=-\frac1{p^4(q-1)}
 \sum_{j=0}^{q-2}(-1)^j
 g_{a+j}^{\,2}g_{c+j}g_{-j}^{\,2}g_{h-j}.
\tag{1061.39}
$
分母 $p^4$ 是上一步已经精确计算的
$g_a^2g_cg_h$，不是仅给其赋值。

取 $\varpi^{p-1}=-p$ 的 Gross–Koblitz 标准根。
若 $b=b_0+pb_1$ 是 $0\le b<q-1$ 的两个数字，则该公式和
$\Gamma_p(-b_i)\equiv1/b_i!\pmod p$ 给
$
\frac{g_b}{-\varpi^{b_0+b_1}}
 \equiv\frac1{b_0!\,b_1!}\pmod p.
\tag{1061.40}
$
此式含 $b=0$，并保留完整循环数字。

为核尽所有 carry，对 $j>0$ 设
$x=j/(q-1)$、$y=(pj\bmod(q-1))/(q-1)$。
(1061.39) 中该项的 $p$ 赋值为 $f(x)+f^\vee(y)-4$，其中
$
\begin{aligned}
f(x)&=2\langle2/3+x\rangle+\langle1/6+x\rangle
       +2\langle-x\rangle+\langle1/2-x\rangle,\\
f^\vee(y)&=2\langle1/3+y\rangle+\langle5/6+y\rangle
       +2\langle-y\rangle+\langle1/2-y\rangle.
\end{aligned}
$
两者均至少为二；分别取最小值的准确区间是
$[1/3,1/2]\cup[5/6,1)$ 和 $[2/3,1)$。
所有阈值端点在这里已经包含，$1/2$ 处仍取低值。
因此除 $j=0$ 外，单位项准确对应
$
j\in[(q-1)/3,h]\cup[5c,q-2],\qquad
pj\bmod(q-1)\ge a.
$
写 $j=j_0+pj_1$，得到两个矩形
$
\begin{array}{c|cc}
 &j_0&j_1\\ \hline
{\rm I}&4k-1+r&2k-1+s\\
{\rm II}&4k-1+r&5k-1+s
\end{array}
\qquad
0\le r\le n,\quad0\le s\le N.
\tag{1061.41}
$
II 的最后一个角 $(r,s)=(n,N)$ 表示 $j=q-1$，
恰用来代替原来的 $j=0$；它只能计一次。
其余全部项的赋值为正，所以不贡献模 $p$ 读数。

按“低数字、高数字”的顺序，四个下标的数字为
$
\begin{array}{c|c|c}
 &{\rm I}&{\rm II}\\ \hline
a+j &(r,s)&(r,3k+s)\\
c+j &(3k-1+r,3k-1+s)&(3k+r,s)\\
-j &(n-r,4k-1-s)&(n-r,N-s)\\
h-j &(5k-1-r,N-s)&(5k-2-r,4k-2-s).
\end{array}
\tag{1061.42}
$
表中每个数字均位于 $0,\ldots,p-1$；末角也准确给原 $j=0$
的四组数字。没有略去第一位与第二位间的进位。

### 15.3 全函数只给加权半截矩

定义以下完全在 $\mathbf F_p$ 中的单位：
$
\begin{aligned}
R_r&=\frac{(-1)^r}
 {(r!)^2(3k-1+r)!\,(n-r)!^2(5k-1-r)!},\\
S_s&=\frac{(-1)^s}
 {(s!)^2(3k-1+s)!\,(4k-1-s)!^2(N-s)!},\\
R'_r&=R_r\,\frac{5k-1-r}{3k+r},\\
S'_s&=(-1)^N S_{N-s}.
\end{aligned}
$
由 (1061.39)–(1061.42)，I 的总贡献为
$(\sum R_r)(\sum S_s)$；II 为
$(-1)^k(\sum R'_r)(\sum S'_s)$。
因 $k+N=2k-1$ 为奇数，精确得到
$
1=\mathcal H_q\bmod p
 =\left(\sum_{s=0}^N S_s\right)
  \left(\sum_{r=0}^n(R_r-R'_r)\right).
\tag{1061.43}
$
逐项比值给
$
R_r=R_0(2r+1)t_r,\qquad
R'_r=-2R_0(k+r)t_r.
$
另一方面
$
\frac{S_s}{S_0}
=\frac{(2k)_s^2(-N)_s}{(s!)^2(3k)_s}.
$
这是一个真正以 $-N$ 终止的 Dixon 和，分母全部为单位。
其有限式由 Dixon 恒等式先固定 $c=-N$、在无极点的开集化成
Pochhammer 有理恒等式，再代 $a=b=2k$ 得到；
不是在本次参数的 Gamma 极点处直接相除。准确为
$
\sum_{s=0}^N S_s
=S_0(-1)^N\frac{(2k+1)_N}{(k+1)_N}\ne0.
\tag{1061.44}
$
所以 (1061.43) 的实际剩余因子是
$
R_0\sum_{r=0}^n(4r+4/3)t_r.
$
§14 的完整奇终止身份给 $t_{n-r}=-t_r$，
而 $4(n-r)+4/3=-(4r+4/3)$ 于 $\mathbf F_p$。
配对后得到准确单位式
$
\boxed{
4D_N'(1)+\frac43D_N(1)
=\frac{(-1)^N(k+1)_N}
 {2R_0S_0(2k+1)_N}\ne0.}
\tag{1061.45}
$
特别地，
$
D_N(1)=0\ \Longrightarrow\ D_N'(1)\ne0.
$

这个结论保留了所读对象：有限域 character 将 $3/2$ 与 $1/2$
识别，但在原有限和中
$(3/2)_r=(2r+1)(1/2)_r$，该权不能删除。
(1061.38) 的单位并不是 $D_N(1)$ 的范数；
完整双数字展开准确给 (1061.45)，而不是原目标非零。
此处 $z$ 是所显示半截多项式的参数，尚未将它与原曲线的
CM/deformation 参数识别，故也不能从这一导数直接声称原 theta 点光滑。

本节使用 McCarthy
[原文](https://dermotmccarthymath.github.io/publications/Hyp%20Trans.pdf)
Definition 1.4、Theorem 4.2 及其证明 (4.5)–(4.7)，明确保留退化项。
(1061.44) 使用 [DLMF 16.4.4](https://dlmf.nist.gov/16.4.E4)
的上述有限有理特例。
Gross–Koblitz 的约定见 A. M. Robert,
*The Gross–Koblitz formula revisited*, Rend. Sem. Mat. Univ. Padova
**105** (2001), 157–170，
[原文](https://www.numdam.org/article/RSMUP_2001__105__157_0.pdf)，
Theorem 4；(1061.40) 的阶乘约化已在上文给出。
root 推导全 $q$ 公式和两个数字矩形；o1_theta 独立逐项核
阈值、四组 carry、末角、阶乘比与完整/半截边界。无数学执行。



## 16. 原 Cartier 映射的完整 FM 线与指定系数

令 $N=\mathcal O_E(O)$，保持原 $\omega$、
相对 $F:E\to E^{(p)}$ 及 $N_p=\mathcal O_{E^{(p)}}(O)$。
有限平坦对偶用这两条不变微分刚化后，准确给
$
\operatorname{Hom}(F_*N,N_p)
 =H^0(E,N^{p-1})=L((p-1)O),\qquad
f\longmapsto\mathscr C_{\rm rel}\circ f.
\tag{1061.46}
$
右边的 $f$ 作为有理函数在 $O$ 的极阶至多 $p-1$；
$f=U^m$ 正是 (1061.18) 的原映射，未换双覆盖分支线。

取规范 Poincaré 的 Fourier–Mukai 变换。
对任意 degree-zero twist，两原丛的 $H^1$ 均为零、$H^0$ 均为一，
所以它们的变换是两条线丛 $\widehat{F_*N},\widehat{N_p}$，
度数分别为 $-p,-1$。
也可用 isogeny 相容
$\widehat{F_*N}=V_E^*\widehat N$ 和
$\widehat N\simeq N^{-1}$ 直接读出这两个度。
因此
$
\mathcal M=
\mathcal Hom(\widehat{F_*N},\widehat{N_p}),\qquad
\deg\mathcal M=p-1.
\tag{1061.47}
$
Mukai 的全忠实性使每个非零 $f$ 给出非零截面 $s_f$。

必须固定 $\mathcal M$ 的有理帧。对 $P\ne O$，
在 §9.2 已付的两条真实生成元中，$s_f$ 的 Cartier scalar 为
$
M_f(P)=
\frac{\mathscr C_{\rm rel}(f(T)g_P(T)\omega_T)}{\omega'}.
$
当 $f=1$ 时，原刚化给
$g_P=z_O^{p-1}(1+\cdots)$、$\omega=(1+\cdots)dz_O$。
这个 meromorphic differential 只可能在 $P$ 有至多 $p$ 阶极；
唯一留数为零，故 Cartier 后没有极点，是全纯常数。
读取 $z_O^{p-1}dz_O$ 的系数准确得到 $M_0=1$。

§9.2 的源、靶生成元在非零 Picard 点都非零，
所以 $s_1$ 在这些点没有零。结合 (1061.47)，
$
\operatorname{div}(s_1)=(p-1)O,\qquad
\mathcal M\simeq\mathcal O((p-1)O).
\tag{1061.48}
$
令 $t_f=s_f/s_1$。
原生成元的比较因子在这个 ratio 中完全相消，故
$
t_f(FP)=M_f(P).
\tag{1061.49}
$
该式保持相对参数 $FP$，未把 $a^p$ 直接改成 $a$。

在原 $\mathbf F_p$ 模型上作系数 Frobenius 逆识别，
定义
$
\phi_f(P)=t_f(FP)^{1/p}
 =\frac{\mathscr C_{\rm abs}(f(T)g_P(T)\omega_T)}{\omega},
\qquad
\phi_f\in L((p-1)O).
\tag{1061.50}
$
一般系数下这是半线性变换；$f\in\mathbf F_p(E)$ 时，
$\phi_f$ 在 $\mathbf F_p$ 上定义。
这里使用的是完整函数族的 Frobenius 识别，
不是让相对 Cartier 对变动参数取根。
作为线空间的变换它是半线性同构；
非零来自原 Hom 的全忠实，而非指定点值。

设 $\zeta^3=1$，其作用为 $(U,V)\mapsto(\zeta U,V)$。
原 divisor 和 $O$ 首项归一给
$
g_{\zeta P}(\zeta T)=\zeta^{p-1}g_P(T).
$
保 $\omega\mapsto\zeta\omega$、Cartier 半线性及
$p\equiv-1\pmod3$，得到
$
\phi_{U^j}(\zeta P)=\zeta^{-j}\phi_{U^j}(P).
\tag{1061.51}
$
同理 $[-1]$ 给 $\phi_{U^j}(-P)=\phi_{U^j}(P)$。
偶性使其为 $U$ 的多项式；极阶及 $\mu_3$ 角色
使原 $m=3N+2$ 的函数准确形如
$
\boxed{\quad
\phi_{U^m}(P)=U(P)H_p(U(P)^3),\qquad
0\ne H_p\in\mathbf F_p[X],\quad\deg H_p\le N.
\quad}
\tag{1061.52}
$

原 $P=Q+A$、$a=z_O(A)$ 下，(1061.34) 给
$M_m(Q+A)=e a^p+O(a^{2p})$。
绝对识别后为
$\phi_{U^m}(Q+A)=e^{1/p}a+O(a^2)$；
同时 $U(Q+A)=2va+O(a^2)$。所以
$
\boxed{\quad
H_p(0)=\frac{e^{1/p}}{2v}=-\frac e{2v}.
\quad}
\tag{1061.53}
$
最后使用原 $e^p=-e$。这是已固定全部有理帧后的准确常数。

若 $r_H=\operatorname{ord}_{X=0}H_p$，
截面 $s_{U^m}$（即实际 $\Theta_{\mathcal A^\vee}$ 的方程）
在 $\pm Q$ 的消失阶恰为 $1+3r_H$；
在 $O$ 的阶为
$
6(N-\deg H_p)+2\ge2.
\tag{1061.54}
$
这里的 $O$ 阶只属于 $s_{U^m}$，
不是整个 $\Theta_{B_C}$ 限制的 $O$ 阶：
在 $O$ 处还须保留 $B_E$ 因子。
在 $\pm Q$ 处该因子为单位，§9.3 因而把
$1+3r_H$ 准确传回原指定 theta 点。

未证 $H_p$ 最高系数非零时，不称 (1061.54) 恰为二。
$e=0$ 只会使指定点的阶至少四；本节尚未排除它，
不能以全局截面非零代替原 $S_n$ 单位。

原始来源：S. Mukai, *Duality between D(X) and D(X) with its application
to Picard sheaves*, Nagoya Math. J. **81** (1981), 153–175，
[原文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDBEBAC584BE15236C2D62C383A34245/S002776300001922Xa.pdf/duality-between-dx-and-with-its-application-to-picard-sheaves.pdf)。
实读 Theorem 2.2、Corollary 2.5、(3.4)、(3.10) 和
Proposition 3.11 的 principal-polarization 情形。
原 Miller 帧、$s_1$ divisor、半线性角色与 (1061.53)
由本节自证；o1_theta 推导，root 独立核准。无数学程序执行。




## 17. 同一个原 Miller 核的严格互易式

把原 $O$ 首项归一的 $g_P(T)$ 看作 $E_T\times E_P$
上的有理函数。它在第二变量的普通导数为零：
对一般 $P_0$，§7 的证明仍适用，
因为 $[p](P_0+A)$ 到 $a^{p^2}$ 才变、
移动的 $p$ 重极点到 $a^p$ 才变，而 $O$ 的首项恒为一。
故次数 $1,\ldots,p-1$ 的变分全为零，
在函数域中存在唯一实际下降
$
g_P(T)=K(T,FP),\qquad R=FP.
\tag{1061.55}
$
这里沿第二变量的相对 Frobenius 下降；
没有把集合意义的 $F^{-1}$ 当作可分映射。

必须先核整个曲面 divisor。非 vertical 的分量由一般 $P$
的原 divisor 决定：图 $T=[p]P$、对角线 $T=P$、
以及 $T=O$，重数分别为 $1,-p,p-1$。
不存在 $P=P_0\ne O$ 的额外 vertical 分量：
本曲线 supersingular，所以 $[p]P_0\ne O$；
两条 moving graphs 都避开 $(O,P_0)$，
而 $g/z_O^{p-1}$ 在 $T=O$ 的刚化首值恒一。
其沿该 vertical 的 valuation 因而为零。

唯一剩下的 vertical 是 $P=O$。
限制到一般 $T$，图 $T=[p]P$ 的 degree 是 $p^2$，
$p$ 倍对角线的 degree 是 $p$；主 divisor 总 degree 为零，
故这个 vertical 的重数准确为 $-p(p-1)$。
于是全曲面上
$
\operatorname{div}(g)=
\Gamma_{T=[p]P}-p\Delta_{T=P}
 +(p-1)(O\times E)-p(p-1)(E\times O).
\tag{1061.56}
$
支持和重数都已确定，没有留下任意 base function。

用原 $[p]=-F^2$，沿 $\operatorname{id}\times F$ 下降，得到
$
\boxed{\quad
\operatorname{div}(K)=
\Gamma_{T=-FR}-\Gamma_{R=FT}
 +(p-1)(O\times E-E\times O).
\quad}
\tag{1061.57}
$
第一个 graph 拉回为 $T=-F^2P$，重数一；
第二个拉回 $FP=FT$ 是 $p$ 倍对角线；
$R=O$ 拉回为 $p(P=O)$。
这核准全部 inseparable scheme multiplicities。

令 $\iota(T,R)=(R,-T)$。由 (1061.57) 逐项可见
$\iota^*\operatorname{div}(K)=-\operatorname{div}(K)$。
$E^2$ 完备且几何连通，故
$K(T,R)K(R,-T)$ 是非零常数。
该常数也须由原规范计算。

令 $k=N+1$，则 $p=6k-1$、$m=3k-1$。
取唯一满足 $e_2^3=108=-v^2$ 的 $e_2\in\mathbf F_p$，
令 $T_2=(e_2,0)$ 为实际非零二挠点。
因为 $FT_2=T_2=-T_2$、$FQ=-Q$，
在 $T=T_2,R=-Q$ 处，原 $g_Q$ 给
$
K(T_2,-Q)=g_Q(T_2)=\frac{e_2}{v^{2k}}.
$
另一方面 $[p]T_2=T_2$，所以
$
g_{T_2}(S)=(U(S)-e_2)^{-m}.
$
这个式子的 divisor 与 $O$ 首项一都符合原规范。
由此
$
K(-Q,-T_2)=g_{T_2}(-Q)=(-e_2)^{-m}.
$
两个值的乘积为 $-e_2^2/v^{4k}$。
原 $v^p=-v$ 给 $v^{6k}=-v^2$，
故 $(v^{4k})^3=e_2^6$；
$v^{4k}$、$e_2^2$ 都在 $\mathbf F_p$，
且立方在该域为双射。因此 $v^{4k}=e_2^2$，最终
$
\boxed{\qquad K(T,R)K(R,-T)=-1.\qquad}
\tag{1061.58}
$

这是同一原 Miller 核的全局有理恒等式，
保相对变量 $R=FP$、全部 vertical 重数与固定符号。
它本身没有把原 Cartier 的指定 matrix coefficient 变成单位；
也未在尚无比较时推出 §16 的标量变换平方为恒等。
后继须继续原核的实际伴随与指定读数。

o1_theta 推导；root 独立核整个曲面 divisor、$p/p^2$
重数、$\iota$ 的两个 graph 交换及原二挠点的常数 $-1$。
全篇纸面证明，无数学程序执行。




## 18. 原 Cartier–FM 变换的 F/V 互逆与准确平方

继续 §16 的全部原归一。
令 $F:E\to E^{(p)}$ 为 relative Frobenius，
$V:E^{(p)}\to E$ 为 dual isogeny，
$N=\mathcal O_E(O)$、$N_p=\mathcal O_{E^{(p)}}(O)$。
在本文 $\mathbf F_p$ 模型的识别下
$V=\iota\circ F$，其中 $\iota=[-1]$。
以下 $\mathscr T_F$ 指 $k$-linear relative 变换
$
\mathscr T_F(f)=s_f/s_1,
$
其参数在 $E^{(p)}$，不是先对 relative 参数取根的绝对算子。
§16 的原 $M_0=1$ 固定此 ratio，特别 $\mathscr T_F(1)=1$。
对 $V$ 以同样的原点刚化及 ratio 定义 $\mathscr T_V$。

在这些实际标架和 $\mathbf F_p$ 模型识别中，有
$
\boxed{\quad
\mathscr T_V\mathscr T_F=\operatorname{Id},\qquad
\mathscr T_V=\iota^*\mathscr T_F,\qquad
\mathscr T_F^2=\iota^*.
\quad}
\tag{1061.59}
$
所以 $\mathscr T_F^4=\operatorname{Id}$。
对 $\mathbf F_p$ 定义的输入，§16 的绝对变换 $\Phi$
也满足 $\Phi^2(f)=\iota^*f$。
一般 $k$ 系数下，$\Phi$ 是 $p^{-1}$-semilinear，
准确式为
$
\Phi^2(f)=\iota^*(f^{(-p^2)}),
$
其中 $f^{(-p^2)}$ 只对本文 $\mathbf F_p$ 有理函数基的系数
取 $p^2$ 次根；不能改写成一般 $k$-linear identity。

### 18.1 两次实际 Hom 映射及 adjunction

令 $\mathcal S$ 为规范 Poincaré kernel 的 derived FM functor，
$\mathbb D=R\mathcal Hom(-,\mathcal O)$，并置
$\mathcal A=\mathbb D\mathcal S$。
$\mathbb D$ 不含额外的 $[1]$。
Grothendieck–Serre duality 给
$
\mathbb D\mathcal S
 \simeq\iota^*\mathcal S\mathbb D[1].
$
具体地，对 $p_2:E\times E\to E$ 用
$p_2^!\mathcal O=p_1^*\omega_E[1]$，再用指定不变微分
和 Poincaré 的 $\mathcal P^\vee=(1\times\iota)^*\mathcal P$，
即得该式。因此 Mukai Theorem 2.2 给
$
\mathcal A^2
 \simeq\iota^*\mathcal S^2[1]
 \simeq\operatorname{Id}.
\tag{1061.60}
$
这里 $[1]$ 与 $\mathcal S^2\simeq\iota^*[-1]$ 准确相消。

Mukai (3.4) 的 isogeny exchange 给
$
\mathcal A F_*\simeq V^*\mathcal A,\qquad
\mathcal A V_*\simeq F^*\mathcal A,
$
同时 $\mathcal A(N)\simeq N$、
$\mathcal A(N_p)\simeq N_p$。
指定 $\omega,\omega'$ 刚化 finite dualizing 线，得到
$V^!N\simeq V^*N$ 和 $F^!N_p\simeq F^*N_p$。
所用的是
$\omega_{\rm source}\otimes f^*\omega_{\rm target}^{-1}$
的两个指定生成元，不是 inseparable morphism 的零微分。

第一遍全部 Hom 映射为
$
\operatorname{Hom}(F_*N,N_p)
 \xrightarrow{\mathcal A}
\operatorname{Hom}(N_p,V^*N)
 \xrightarrow{\operatorname{Adj}_V^{-1}}
\operatorname{Hom}(V_*N_p,N),
\tag{1061.61}
$
第二遍为
$
\operatorname{Hom}(V_*N_p,N)
 \xrightarrow{\mathcal A}
\operatorname{Hom}(N,F^*N_p)
 \xrightarrow{\operatorname{Adj}_F^{-1}}
\operatorname{Hom}(F_*N,N_p).
\tag{1061.62}
$
$\operatorname{Adj}_V,\operatorname{Adj}_F$
是标准 finite Grothendieck-duality adjunction，
不是任意向量空间同构。

将 $V_*\dashv V^!$ 经反等价 $\mathcal A$ 运输，
得到 $F_*\dashv F^!$：
反等价反转 adjunction 两边，上述 exchange 将
$V^!$ 送到 $F_*$，将 $V_*$ 送到 $F^!$。
这些比较的 kernel 是同一 graph $\Gamma_F$ 或 $\Gamma_V$。
更换该 kernel isomorphism 只能乘全局常数，因为
$
\operatorname{End}(\mathcal O_{\Gamma_F})
 =H^0(E,\mathcal O_E)=k,\qquad
\operatorname{End}(\mathcal O_{\Gamma_V})=k.
$
等价地，finite pullback tensor functor 的自然 automorphism
来自 source 上的全局单位；source proper connected，只有 $k^\times$。
所以 (1061.61)–(1061.62) 的复合由 (1061.60)
为同一个 scalar 乘 identity，不可能多出依赖 $f$ 的矩阵。

在 §16 的实际 Hom–section 识别中，
(1061.61) 的 section 与 $s_f$ 只差这个共同 scalar：
对偶两个 line maps 不改变 $s_f/s_1$，
finite adjunction 也保同一乘法 section。
各次以原 $f=1$ 的 $s_1$ 归一后，
所得正是 $\mathscr T_F,\mathscr T_V$。
两者都把 $1$ 送到 $1$，复合 scalar 必为一，
证明 (1061.59) 第一式。

### 18.2 V 等于负 F 的原参数与 trace 号

对一般 $P$，$F$-构造在 Picard 参数 $FP$
使用的 source section 是 $g_P\ell_P^p s_O$，
其 divisor 为 $[p]P$。
$V$-构造在参数 $VP=-FP$ 使用的 source divisor 仍为
$[p]P$，因为 $\widehat V=F$。
同一个 $O$ 首项归一因此仍给同一个 $g_P$，
没有任意 $P$-依赖的乘法常数。

从 $F$ 改为 $V=\iota\circ F$，
target section 经 $\iota$ 运输，Picard 参数改为 $-FP$。
在指定微分上 $\iota^*\omega=-\omega$，
raw Cartier trace 出现整体号；
该号对任意 $f$ 与 $f=1$ 相同，在 ratio 中相消。
故
$
(\mathscr T_Vf)(-FP)=(\mathscr T_Ff)(FP).
\tag{1061.63}
$
$F$ 满射，遂 $\mathscr T_V=\iota^*\mathscr T_F$，
与第一式合并证明准确平方。

### 18.3 原函数空间中的后果与未付的指定系数

特别，对已证 $\Phi(U)=\delta\mathcal R(U)$ 再作一次变换，
有
$
\Phi(\mathcal R(U))=\delta^{-1}U,\qquad
\Phi^2(V)=-V.
\tag{1061.64}
$
这些均为原函数空间内的精确身份。
它们未证明 $U$-单项式基下矩阵对称，也未证明特定矩阵元非零。
目标仍为
$\Phi(U^m)=UH_p(U^3)$ 的指定
$H_p(0)=-e/(2v)$。
全局可逆性不替代这个读数的单位性。

来源同 §16 的 Mukai 原文，Theorem 2.2、(3.4)、(3.8)；
本节将两次 finite adjunction、全部 shifts 和 $f=1$ 归一展开。
o1_theta 推导，root 独立核准；无数学程序执行。


## 来源与本次核对

- [R1059](R1059-original-fN-actual-X108-Raynaud-pairing-and-inverse-central-sum.md)：原 $X_0(108)$ 函数、good 模型、固定微分尺度和 $S_n$ 配对。
- [R1060](R1060-actual-X108-nonCM-Cartier-and-nine-torsion-ordinary-input.md)：六条 CM 核、四条非 CM ordinary 输入及准确 Euler 标量。
- Jilong Tong, *Diviseur thêta et formes différentielles*, Math. Z. 264 (2010), 521–569，DOI 10.1007/s00209-009-0478-y；[作者原文](https://www.math.u-bordeaux.fr/~jtong/Recherche/Theta.pdf)，Proposition 2.2.1、Corollary 2.2.2（印刷541–542页），§4.2。此处只使用其准确光滑判据，不假设本固定曲线一般。

o1_theta给实际覆盖、三挠线和配对下降；o2_high_coefficient独立核角色、第一椭圆因子与分支线；root实读Tong所引原文，并手核全部函数域次数、无分歧性、两微分、divisor、角色、Frobenius及有序标量。无数学程序或窗口执行。

补充§§6–8：o2_high_coefficient给规范Ψ递推和完整first-p Cartier系数；root独立推Miller首变分和Ψ加法律，o1_theta独立核两式；root逐项核U/V两坐标的全部次数、Q处极阶、半线性及完整slope消去。Frobenius特征方程可见Andrew Sutherland [MIT 18.783 Lecture 8](https://math.mit.edu/classes/18.783/2022/LectureSlides8.pdf)第5张幻灯片。无数学执行。

补充§9：o1_theta给实际双覆盖/dual Cartier/Poincaré frame的非零桥，root独核相对Cartier的base线性、FQ参数、两个生成元、B_E单位因子及切向因子2，明确纠正relative/absolute标量约定。§10由root给原η的直接primitive与K=−sS，o2独核分部积分的K₂，所有不同权保留。全文无数学执行。

补充§§11–12：o1_theta给实际三平移、有界第一原函数和h的阶乘证明；root独核原参数、完整相对Cartier和分部积分，提出并证明实际空间上的单位Cartier读数与核维数，o1逐式独核。由此支付二次有界primitive的必要充分性；没有从极阶小于p直接假设原函数也有界。无数学程序执行。

补充§§13–14：o1_theta推原全参数Miller对数导数和Lamé源；root实读本篇原S递推并独核第一矩形Cartier、两处留数及Ψ²恒等式。root推完整M/N伴随递推、原Q处A/B变分和e=δA_N，o1独核全部pole范围、初值及半截身份。双方独立确认完整奇Dixon和的反对称性不支付半和单位。无数学程序执行。
