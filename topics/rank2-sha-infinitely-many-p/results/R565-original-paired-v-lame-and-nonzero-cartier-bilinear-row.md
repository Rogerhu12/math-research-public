# R565 — 原 D/∇ 差、完整 deck 相位与非零十二度 Cartier 双线性行

日期：2026-11-14。**状态：已证明。**

本篇在 R549 与 paired-V 检查点的同一 Verschiebung 上，给出两条原负矩来源的完整差多项式、它在全部 étale 纤维上的相位及共同除子，并计算一条非零的 Cartier 双线性行。该行的输出恰在固定三维空间 $\langle1,x^3,x^6\rangle\omega_E$ 中，最高系数是单位。

这不是把形式协变关系登记为新非消失：下述非零输出及其绝对符号均完整计算。另一方面，它是双线性行，不是 R549 指定的二次／五次两条线性 Cartier 观察；本篇不由此断言 $I_4,I_1$ 不同时零。

## 1. 固定基 frame 与原两行

本篇先固定 [R540](R540-original-degree-six-schwartz-full-weight-and-negative-two-katz.md) 的
$$
E_0:y^2=x^3+1,\quad \omega_E=\frac{dx}{2y},\quad
Dx=2y,\quad Dy=3x^2,\quad
D\log\sigma=g,\quad Dg=-x.
\tag{1}
$$
中间特征零恒等式也允许 $y^2=x^3+b$，随后再令 $b=1$。
这里 $\pi=\psi_0(\mathfrak p)$ 是 $E_0$ 的原 $2\delta$-primary Frobenius，
不是原 rank-two 曲线的 Frobenius。

这个规范与当前射线相同：
[R410 §1](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)
明确规定 $\pi_0=\psi_0(\mathfrak p)$，而 $\pi_{17}=\pi_{24}=-\pi_0$。
当前细分仍有
$$
\pi\bmod24=(7,18),\quad N\pi\equiv7,\quad \pi^2\equiv13,\quad
\boxed{g_\pi=\pi/\bar\pi\equiv19\pmod{24}.}
\tag{2}
$$
所有旧坏集及大素数门保留。置
$$
p=6s+1>19,\qquad \mathfrak h=\binom{3s}{s}\in\mathbf F_p^\times,
\qquad V=\bar\pi,\quad dV=\mathfrak h,
$$
$$
\lambda=-\bar\pi^{-1},\quad \beta=-\lambda,\quad
\kappa=p/\bar\pi^2.
\tag{3}
$$
$V$ 在 $E_0$ 的约化上是原 étale Verschiebung；
$D^p=\mathfrak hD$、$\mathcal C(\omega_E)=\mathfrak h\omega_E$。

沿用 [R549](R549-original-cartier-verschiebung-and-fixed-negative-moment-rows.md)
及 [paired-V 检查点](../notes/2026-11-14-paired-verschiebung-cartier-checkpoint.md) 的精确有理式
$$
\sigma(Vz)=r(z)\sigma(z)^p,\qquad
x(Vz)=\frac{N(x)}{r(x)^2},\qquad
y(Vz)=\frac{M(x)y}{r(x)^3},
$$
$$
r\in\mathbf F_p[x^3],\quad \deg_x r=\frac{p-1}{2},\quad
N\text{ monic},\quad\deg_xN=p,\qquad
M=\frac{rN_x-2Nr_x}{\mathfrak h}.
\tag{4}
$$
$r$ 的首系数为 $\mathfrak h$，常数为原完整有限角色
$\xi(\mathfrak p)$；没有更换该角色。
定义
$$
q_4=r^6x(V)=r^4N,\qquad
q_1=-r^6x(V)y(V)=-rNM\,y,
$$
$$
\mathcal R_4=D^{p-3}q_4,\qquad
\mathcal R_1=D^{p-6}q_1.
\tag{5}
$$
这仍是原 $I_4=I_{-2}(f_4)$、$I_1=I_{-5}(f_1)$ 的两条线性行，
其准确最高系数关系在 §8 保留。

## 2. 同一固定有界来源的 Lamé 两列

在特征零，记
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6,\qquad
\Theta=x\sigma^2,\qquad
\boxed{\ \mathcal Z_6=(y+xg)\sigma^6=\frac12\sigma^4\Theta'.\ }
\tag{6}
$$
最后一式使 $\mathcal Z_6$ 是实际有界整来源：
按原周期 $\Omega$，
$$
\nu_{\mathcal Z_6}
=\frac1{2\Omega}\,
  \nu_\sigma^{*4}*(X\,\nu_\Theta).
\tag{7}
$$
没有把单独的 $g$ 当作有界测度。
$\mathcal Z_6=-2bz^9/5+O(z^{15})$，但它不是一条标准六度 theta 线；
不能给它套用整个 $\mathcal S_6$ 的 scalar 核。

令 $\nabla_6=D-6g$。直接求导给
$$
(\nabla_6^2-6x)f_4=0,\qquad
(\nabla_6^2-6x)\mathcal Z_6=0,
$$
$$
\boxed{\,f_4D\mathcal Z_6-\mathcal Z_6Df_4=-2b\sigma^{12}.\,}
\tag{8}
$$
证明可完全消去 sigma：$u=y+xg$ 满足
$$
Du=2x^2+2yg,\qquad D^2u=6xu,\qquad
xDu-uDx=2x^3-2y^2=-2b.
$$
两列乘同一个 $\sigma^6$ 后，Wronskian 中的 $6g$ 项精确相消。

R554 的完整差现在写成
$$
\boxed{
D^3f_4-24f_1=216g^2\mathcal Z_6
=108\sigma^2(\sigma')^2\Theta'.
}
\tag{9}
$$
最右端是已经支付的五个原输入及正加权来源。
(8) 与 (9) 合用时必须保留该来源，不能删除 $g^2\mathcal Z_6$。

## 3. V 上的差是真多项式

在特征 $p$ 置
$$
c_V=D\log r,\qquad \nabla_V=D-6c_V=r^6Dr^{-6}.
$$
(4) 的对数微分给
$$
Dc_V=-\mathfrak h^2x(V),\qquad
D^2c_V=-2\mathfrak h^3y(V).
\tag{10}
$$
其中特征零公式中的 $p\,x$ 项在本节才约化为零。
定义真正的第二列
$$
z_V=r^6\{\mathfrak h\,y(V)+c_Vx(V)\}.
$$
使用 (4) 后，所有分母及对数导数消去：
$$
\boxed{\ z_V=r^4yN_x.\ }
\tag{11}
$$
因此两列都属于原曲线函数域，不是在另一个形式扩张中猜测。

完整差与 Wronskian 为
$$
\boxed{
Q_V:=D^3q_4-24\mathfrak h^3q_1
=216c_V^2z_V
=864\,r^2y^3r_x^2N_x,
}
\tag{12}
$$
$$
\boxed{
q_4Dz_V-z_VDq_4=-2b\mathfrak h^2r^{12}.
}
\tag{13}
$$
此处亦可暂保任意单位 $b$；后文固定数值 Cartier 输出取 $b=1$。
相反，协变三阶关系的符号是
$$
\nabla_V^3q_4=-24\mathfrak h^3q_1,\qquad
\nabla_V^p=\mathfrak h\nabla_V.
\tag{14}
$$
(12) 与 (14) 的差正是本篇所保的非零多项式，不能把 $D$ 换成 $\nabla_V$。

两条可逐系数复核的除法多项式恒等式是
$$
2r(3x^2r_x+2(x^3+b)r_{xx})-4(x^3+b)r_x^2
=-\mathfrak h^2N,
$$
$$
\boxed{
N(3x^2N_x+2(x^3+b)N_{xx})
-2(x^3+b)N_x^2=-2b\mathfrak h^2r^4.
}
\tag{15}
$$
第一式是 (10)，第二式是 (13) 除以 $r^8$。
它们在整个函数域成立，不仅在 $O$ 的若干项成立。

例如 (15) 最高项确定
$$
N=x^p-\frac{2b\mathfrak h^6}{15}x^{p-3}+\cdots,\qquad
N_x=\frac{2b\mathfrak h^6}{5}x^{p-4}+\cdots.
\tag{16}
$$
所以 $q_4,z_V,Q_V$ 在 $O$ 的极点阶分别恰为
$6p-4,6p-9,6p-7$。这些是确切极帽，不是忽略相位后的预算。

## 4. 全部 étale deck 相位与共同除子

paired-V 检查点已经完整支付：对 $T\in\ker V$，
$$
m_T(z)=\frac{r(z+T)}{r(z)},\qquad
D\log m_T=a_T,\qquad
a_T^p=\mathfrak h a_T,
$$
$$
T\longmapsto a_T
\text{ 是 }\ker V\longrightarrow
\{a:a^p=\mathfrak h a\}\text{ 的加法群同构}.
\tag{17}
$$
本篇从真实 $N$ 得到所有这些相位的显示公式：
$$
\boxed{
a_T=\frac{y(T)N_x(T)}{N(T)}
\qquad(T\in\ker V\setminus\{O\}).
}
\tag{18}
$$

证明：由 (11)，
$$
\frac{z_V}{q_4}
=\frac{yN_x}{N}
=\mathfrak h\frac{y(V)}{x(V)}+c_V.
$$
在 $O$ 取奇参数 $\tau=-x/y$。
$c_V=\tau^{-1}+O(\tau)$，而
$\mathfrak h\,y(V)/x(V)=-\tau^{-1}+O(\tau)$；
$V$ 的奇性排除了常数项。
平移到 $T$，(17) 使前式的常数项增加且只增加 $a_T$。
$r(T)=0$，但 $N(T),y(T)$ 非零，故取值即 (18)。

特别 $N_x$ 在整个非零 étale 纤维处处非零。
不能把 (18) 的相位换成零，或把原点的一条消失传到所有 $T$。
例如由 (17)–(18) 有准确的非零纤维式
$$
\sum_{T\ne O}
 \left(\frac{y(T)N_x(T)}{N(T)}\right)^{p-1}
=-\mathfrak h.
\tag{19}
$$

还有完整共同除子：
$$
\boxed{
\gcd(r,r_x)=\gcd(r,N_x)=\gcd(N,N_x)=1,\qquad
\gcd(N,r_x)=x
}
\tag{20}
$$
（gcd 取 monic，固定 $b=1$）。
$r$ 的根是非零 $\ker V$ 的 $\pm$ 对，均简单。
$N$ 的根则是 $x(V)=0$ 的两条 étale 纤维的 $\pm$ 对，也均简单。
它们与二挠点不交。

为核 (20) 的最后一式，保 R549 的完整 Artin–Schreier 关系
$$
c_V^p-\mathfrak h c_V=-\mathfrak h^2\zeta_p(V).
$$
在 $x(V)=0$ 的纤维上，$\zeta_p(V)=0$。
(17) 使 $c_V$ 的值遍历该方程全部 $p$ 个根，故恰一项为零。
原非零 $\delta$-挠点 $x=0$ 本来就在该纤维，且
$r_x(0)=0$、$r(0)\ne0$，所以这一项就是它。
取 $\pm$ 商便恰得 $x$，没有其他共同根。
由 (10)，$c_V$ 在该点恰为二重零，因此 $r_x$ 的零阶也准确为二。

将 (12) 除去显示的 $y$，于是
$$
\boxed{\ \gcd\bigl(q_4,Q_V/y\bigr)=\operatorname{monic}(r^2x).\ }
\tag{21}
$$
在非零 $\ker V$，$Q_V$ 的零阶准确为二，且
$Q_V/q_4$ 的二阶主项为 $216a_T/\tau_T^2$。
这是同一两条来源差的全纤维约束；它尚未声称高阶 $D$ 或 Cartier
保持这些 gcd。

## 5. 从完整普通核到有理 Cartier 的绝对归一

本节支付 (25) 的号，不能仅因两个 Heisenberg 交织相同就跳过。
完整普通核的定义使用 [R300 §2–2.1](R300-jzero-full-theta-prime-core-and-single-euler-measure.md) 的真实同源迹与全部挠点平均；该证明对本篇的偶数度数 $12$ 原样适用。

令 $\iota:\widehat{\mathbf G}_m\to\widehat E_0$ 为原形式群同构，
$$
\iota^*\omega_E=\Omega\,\frac{dT}{1+T}.
$$
在约化上，$[p]=V\circ\mathrm{Frob}$ 给
$$
\boxed{\ \iota^{(1/p)}=V\circ\iota,\qquad
\Omega^{1/p}=\mathfrak h\Omega.\ }
\tag{22}
$$
这里上标表示系数逐项取 $p$ 次根，CM endomorphism $V$ 定义于
$\mathbf F_p$。这也固定了原 ordinary 周期的 Frobenius 因子。

设标准 degree $N$ 整来源 $F=\sigma^Nf$ 的完整普通核为
$$
\nu_F|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_{K_NF}.
$$
对本篇所用 $N=1,12$，$K_N$ 在原有理 theta 基上的系数都在
$\mathbf F_p$。将 Amice 按输入模 $p$ 分解：
$$
F(\iota(T))=\sum_{i=0}^{p-1}(1+T)^iA_i(T^p),\qquad
A_0(T)=\lambda(K_NF)(\iota([\bar\pi^{-2}]T)).
$$
Cartier 杀掉 $i\ne0$ 项，并把 $A_0(T^p)dT/(1+T)$ 送到
$A_0^{(1/p)}(T)dT/(1+T)$。
用 (22) 及 $\lambda\bmod p=-\mathfrak h^{-1}$，准确得到
$$
\mathcal C(F\omega_E)=-(K_NF)(V^{-1}z)\,\omega_E
$$
作为原形式邻域的等式。
再用 Cartier 与 étale $V$ 的拉回交换，以及
$r^Nf(V)=F(V)/\sigma^{Np}$，得到真正有理式
$$
\boxed{
\mathcal C\bigl(r^N f(V)\omega_E\bigr)
=-\frac{K_NF}{\sigma^N}\,\omega_E.
}
\tag{23}
$$
两边都是全局有理微分，所以局部恒等即全局恒等。
特别原 sigma 的 $K_1=-I$ 给
$\mathcal C(r\omega_E)=\omega_E$。
这不是未定非零标量的锚。

## 6. 整个 degree12 核及固定三维 Cartier 输出

令
$$
A_{12}=\frac12\sum_{t\in E[2]}T_t^{(12)}.
$$
在标准十二维 Schrödinger 基 $e_j$ 上，
两生成平移为 $De_j=(-1)^je_j$、$Xe_j=e_{j+6}$。
因为 $N/4=3$，第三个 canonical 平移为 $-DX$，故
$$
A_{12}=(I+D+X-DX)/2,\qquad
\boxed{\ A_{12}e_j=e_{7j}.\ }
$$
(2) 中 $19=13\cdot7\bmod24$；
$13$ 的中心校正 $(13^2-1)/12=14$ 为偶数，
所以这是完整中心上的同一个交织。

绝对锚取 $\sigma(2\delta z)\in\mathcal S_{12}$。
其三个非零半周期 lift 均为 $-1$：
$\delta\equiv1\bmod2$ 保原 odd sigma 半特征。
因此 $A_{12}$ 在该锚上为 $-1$；
原 sigma 的真实核心是 $\beta=-\lambda$，同一固定 CM 拉回亦然。
由完整 Heisenberg 不可约性，绝对标量遂确定为
$$
\boxed{\ K_{12}=A_{12},\qquad
\mathcal C_{12}=-A_{12}.\ }
\tag{24}
$$
最后一式是 (23)，不是另猜的符号。

对非零半周期 $t$，令 $e=x(t)$，$e^3=-b$。
原 sigma 平移公式给
$$
\frac{T_t^{(12)}\sigma^{12}}{\sigma^{12}}
=\frac{(x-e)^6}{27e^6}.
$$
因为
$\sum_{e^3=-b}(x-e)^6=3x^6+60bx^3+3b^2$，
$$
\frac{A_{12}\sigma^{12}}{\sigma^{12}}
=\frac{x^6+20bx^3+10b^2}{18b^2}.
$$
特别在本篇的固定 $b=1$ 基 frame，
$$
\boxed{
\mathcal C(r^{12}\omega_E)
=-\frac{x^6+20x^3+10}{18}\,\omega_E.
}
\tag{25}
$$
其 $x^6$ 系数为 $-1/18$，是当前所有普通处的单位。
全部三个坐标均保留，没有只取质量。

## 7. 原两列的非零 Cartier 双线性行

由 (13) 以及
$\mathcal C(d(q_4z_V))=0$，解两个和差式得到
$$
\mathcal C(q_4Dz_V\,\omega_E)
=-\mathfrak h^2\mathcal C(r^{12}\omega_E),
$$
$$
\boxed{
\begin{aligned}
\mathcal C(q_4Dz_V\,\omega_E)
 &=\frac{\mathfrak h^2}{18}(x^6+20x^3+10)\omega_E,\\
\mathcal C(z_VDq_4\,\omega_E)
 &=-\frac{\mathfrak h^2}{18}(x^6+20x^3+10)\omega_E.
\end{aligned}}
\tag{26}
$$
特别它们不为零，且最高系数是单位。
输入仍是 (5)、(11) 的实际两个多项式列。
利用 (12)，第二列也可以准确写成
$(D^3q_4-24\mathfrak h^3q_1)/(216c_V^2)$；
这个商由 (11) 全局消去，不允许在 $c_V=0$ 时丢掉可去点。

等价地，所有对数导数消去后还有
$$
\mathcal C\left(
 \bigl((Dq_4)^2-2\mathfrak h^2r^6N^3\bigr)\omega_E
 \right)
=2\mathfrak h^2\mathcal C(r^{12}\omega_E).
\tag{27}
$$
(26) 比形式的 $\nabla_V$ 共轭强：它确定了一个实际有理
Cartier 行的全部有限输出，并且支付了非零单位坐标。

## 8. 原两负矩、完整差及仍未闭合的地方

paired-V 检查点给
$$
A_4=\Omega_{p,0}^2I_{4,0},\qquad A_1=\Omega_{p,0}^5I_{1,0},
$$
$$
[x^{3p}]\mathcal R_4=A_4/\mathfrak h,\qquad
[x^{3p}]\mathcal R_1=A_1/\mathfrak h^4.
\tag{28}
$$
(12) 准确支付同一差，而不是另换原函数：
$$
\boxed{
D^{p-6}Q_V
=\mathcal R_4-24\mathfrak h^3\mathcal R_1.
}
\tag{29}
$$
如果 (28) 两个系数同时为零，已有的确切次顶项仍使 (29)
成为一个极点恰为 $6p-12$ 的非零函数。

本篇新增的 (18)、(21)、(26) 对这个情形仍全部成立。
它们没有造成矛盾：Cartier 不是乘法同态；
$\mathcal C(q_4Dz_V\omega_E)$ 也不是 (28) 两个数的乘积。
(20)–(21) 是微分前来源的真实 gcd，不能自由穿过 $D^{p-6}$。
更具体地，由 paired-V 的原式
$D^2\mathcal R_4=\mathfrak h q_4-\xi x^p$，
Cartier 分部两次给
$
\mathcal C(q_4Dz_V\,\omega_E)
=\mathfrak h^{-1}\mathcal C(\mathcal R_4D^3z_V\,\omega_E).
\tag{29a}
$
$x^pDz_V\,\omega_E=x^p\,dz_V$ 的 Cartier 为零。
(29a) 对 $\mathcal R_4$ 加任意 Frobenius 函数都不变，
特别看不见 $Ax^{3p}+B$；因为
$\mathcal C(D^3z_V\,\omega_E)=0$。
这样的添加一般破坏原规范 $\mathcal C(\mathcal R_4\omega_E)=0$，
所以它不是另造实际来源的反例，而是精确指出：
新双线性行必须再结合该规范条件，不能单凭分部积分读出 (28)。

仍需把这条非零双线性行与指定两条线性观察接成实际新关系，
或将它纳入原完整中央来源及补域，才可能推进非消失。

## 9. 回到原 b=17，保 Frobenius 根单位

取固定 $\vartheta^6=17$、$\phi:E_{17}\to E_0$，
$$
\phi(x_b,y_b)=(x_b/\vartheta^2,y_b/\vartheta^3),\qquad
\phi^*\omega_0=\vartheta\omega_b.
$$
令 $V_b=\phi^{-1}V\phi$，并以同一个复 CM 元素规定原除法函数。
则
$$
r_b=\vartheta^{p-1}(r_0\circ\phi),\quad
q_{4,b}=\vartheta^{6p-4}(q_{4,0}\circ\phi),\quad
z_{V,b}=\vartheta^{6p-3}(z_{V,0}\circ\phi).
\tag{30}
$$
Cartier 的 $p^{-1}$ 半线性和自然性因此给准确的原微分式
$$
\boxed{
\mathcal C_b(q_{4,b}D_bz_{V,b}\,\omega_b)
=\vartheta^{\,12-7/p}\,
 \phi^*\left[
 \frac{\mathfrak h^2}{18}(x_0^6+20x_0^3+10)\omega_0
 \right].
}
\tag{31}
$$
分数指数表示在完美剩余域中唯一的 $p$ 次根。
$x_b^6\omega_b$ 的系数为
$\vartheta^{\,1-7/p}\mathfrak h^2/18$，仍是单位。
没有把这个 Frobenius 根因子改成一。

原实际矩则按 R540 §7.3 有
$$
I_{4,b}=\vartheta^{-4}I_{4,0},\quad
I_{1,b}=\vartheta^{-1}I_{1,0},\quad
\Omega_{p,b}=\vartheta^{-1}\Omega_{p,0}.
\tag{32}
$$
因此两条目标的零性及单位性完整保持。
(31) 支付了新的原 Cartier 输出，但不改变 §8 的未闭合边界。

配套精确证书
[check-r565-paired-v-lame-cartier-row.mjs](../scripts/check-r565-paired-v-lame-cartier-row.mjs)
核对特征零 Lamé/Wronskian、完整十二维中心与半周期多项式、
原除法多项式的 (12)、(15)、(20)–(21)，以及 Cartier 行。
使用已存在的 $13,19,61$ 小纤维和同一已有素数表中的 $31$
作一个 $g_\pi=19\bmod24$ 的绝对归一检查；有限检查不代替上述全证明，
也不作为两负矩的无穷非消失证据。
