# R570 — 两条指定负矩的全局三极点 Cartier 行与显式原函数

日期：2026-11-14。**状态：已证明。**

本篇对 R549 的同一个负二 $f_4$ 矩、负五 $f_1$ 矩，选择固定的
**非 exact 乘子** $d\log(-x/y)$。两个实际原函数经此配对后，其整个
Cartier 输出都落在一条显示的固定微分线上，而且比例系数正是各自
原负矩的第一层值。

关键新增输入是固定二挠、三挠点处的全 theta 平移：两个原函数的
相应取值都由其最高 Frobenius 系数控制。因此一个目标系数为零
不再只是原点的观察，而等价于一条全局有理微分 exact，并有显示的
多项式原函数。这里只支付该等价，没有证明比例系数已非零。

## 1. 原来源及规范化原函数

首先使用 R540、R549、R565 的基 frame
$$
E_0:y^2=x^3+1,\quad
\omega_E=dx/(2y),\quad
D x=2y,\quad D y=3x^2,\quad
p=6s+1>19.
$$
$\pi=\psi_0(\mathfrak p)$ 是 $2\delta$-primary Frobenius，
$V=\bar\pi$，$\mathfrak h=\binom{3s}{s}$ 是它的非零微分标量。
本篇保持原完整有限角色 $\xi$，不作反射或更换普通地点。

用同一个 sigma frame 写
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6,\qquad
\sigma(Vz)=r(z)\sigma(z)^p,
$$
$$
q_4=r^6x(V),\qquad q_1=-r^6x(V)y(V).
$$
令
$$
m_4=p-3,\qquad m_1=p-6,\qquad
\boxed{\mathcal R_i=D^{m_i}q_i=P_i(X),\quad X=x^3,\quad i=4,1.}
\tag{1}
$$
[R549](R549-original-cartier-verschiebung-and-fixed-negative-moment-rows.md)
与 [paired-V 检查点](../notes/2026-11-14-paired-verschiebung-cartier-checkpoint.md)
已证明
$$
P_i\in\mathbf F_p[X],\quad\deg P_i\le p,\qquad
\mathcal C(\mathcal R_i\omega_E)=0.
\tag{2}
$$
记
$$
a_i=[X^p]P_i,\qquad
A_4=\Omega_{p,0}^2I_{4,0},\quad
A_1=\Omega_{p,0}^5I_{1,0}.
$$
目标仍是原单位域
$I_{4,0}=\int X^{-2}d\nu_{f_4}$、
$I_{1,0}=\int X^{-5}d\nu_{f_1}$。
它们的准确第一层为
$$
\boxed{a_4=A_4/\mathfrak h,\qquad
a_1=A_1/\mathfrak h^4\quad\text{在剩余域中}.}
\tag{3}
$$
这里所有被除的因子都是单位。

本篇先证明两个来源特有的全取值关系
$$
\boxed{P_i(0)=-2a_i,\qquad P_i(-1)=3a_i,\qquad i=4,1.}
\tag{4}
$$
它们不对任意满足 (2) 的多项式成立；下面使用原 $f_4,f_1$ 的完整平移支付。

## 2. 固定 torsion 处的完整平移，不删指数相位

对固定 $t\in E[6]\setminus\{O\}$ 使用与 R300/R533 相同的对称 lift
$$
\sigma_t(z)=e^{-\eta_t(z+t/2)}\sigma(z+t),\qquad
T_t^{(6)}F(z)=e^{-6\eta_t(z+t/2)}F(z+t),
$$
并记 $c_t=\sigma_t(0)$。
所有下面用到的点是非零二挠或非零 $\delta$-挠点。
$p>19$ 时这些固定 theta 局部 frame 都整，$c_t$ 是单位：
二挠处 $c_t^4=(3x(t)^2)^{-1}$；
非零 $\delta$-挠处，由 $\sigma(\delta z)=\delta x(z)\sigma(z)^3$
在该点求导可得 $c_t^6=1/(4b)$，此处 $b=1$。
符号在所用的六次幂中完整保留。

原 CM 准周期给 $\eta_{Vt}=\bar V\eta_t$，因此
$$
\eta_{Vt}Vz=p\eta_tz,\qquad
\eta_{Vt}Vt/2=p\eta_tt/2.
$$
所以**整个**指数因子精确相消，特征零即有
$$
\boxed{
r(z+t)=\frac{\sigma_{Vt}(Vz)}{\sigma_t(z)^p},\qquad
q_i(z+t)=\frac{(T_{Vt}^{(6)}f_i)(Vz)}
                   {\sigma_t(z)^{6p}}.
}
\tag{5}
$$
没有将一个挠点正式对数直接置零。

约化后 $D$ 杀掉分母的 $p$ 次幂。对 (1) 的原 $m_i$，
$$
\mathcal R_i(t)
=c_t^{-6p}\mathfrak h^{m_i}
  (T_{Vt}^{(6)}f_i)^{(m_i)}(0).
\tag{6}
$$
$Vt$ 仍是相同阶的固定 torsion 点，且 $T_{Vt}^{(6)}f_i$
属于整个原 $\mathcal S_6$，没有留下伴随 flat twist。

由 R533 的完整六基，$\mu_6$ 型 $1$ 和 $4$ 的子空间分别恰为
$\langle f_1\rangle$、$\langle f_4\rangle$。
因 $m_1\equiv1$、$m_4\equiv4\bmod6$，
(6) 的导数只读对应的完整型投影。
这是有限 theta 空间的全恒等式，不是根据高阶数值拟合对角系数。

## 3. 两条原来源有相同的 torsion 对角系数

设 $g_t=D\log\sigma_t=g(z+t)-\eta_t$。
在非零二挠点，$-t=t\bmod\Gamma$ 与奇性给 $g_t(0)=0$；
在非零 $\delta$-挠点，$\omega t=t\bmod\Gamma$，
而 $g-\eta$ 具有型 $-1$，同样给
$$
g_t(0)=0.
\tag{7}
$$
这里使用的是 canonical $g-\eta$，不是把未经规范化的复 zeta 值说成零。

R554/R565 的全微分身份
$$
D^3f_4=24f_1+216g^2(y+xg)\sigma^6
$$
在 $g=0$ 处再求一次导数，给
$$
\left.\frac{D^4f_4}{24\sigma^6}\right|_{g=0}
=\left.\frac{Df_1}{\sigma^6}\right|_{g=0}
=-(5x^3+2b).
\tag{8}
$$
因 $f_1=z+\cdots$、$f_4=z^4+\cdots$，(8) 完整确定两个
单重型投影：
$$
\boxed{
\Pi_iT_t^{(6)}f_i
=c_t^6d(t)f_i,\qquad
d(t)=
\begin{cases}
-2b,&x(t)=0,\\
3b,&t\in E[2]\setminus\{O\},
\end{cases}\quad i=4,1.
}
\tag{9}
$$
这一步精确解释了两个不同原负权为什么得到同一系数。

另一方面，$D(\sigma^{6p})=0$，所以原点有
$$
a_i=(\sigma^{6p}\mathcal R_i)(0)
=D^{m_i}(f_i(Vz))(0)
=\mathfrak h^{m_i}f_i^{(m_i)}(0).
\tag{10}
$$
前式使用 (2) 的完整极帽及 $x^{3p}\sigma^{6p}\to1$；
不允许另外添加 Frobenius 多项式来改变它。

将 (9)–(10) 代入 (6)，再用 (5) 的常数项，得到完整公式
$$
\boxed{
\mathcal R_i(t)=r(t)^6d(Vt)a_i.
}
\tag{11}
$$
所有平移相位都进入实际 $r(t)^6$，尚未把它当成一。

## 4. 两种固定 torsion 上 r(t)^6 的绝对值

在非零 $\delta$-挠点 $x=0$，
paired-V 的原规范给 $r(0)=\xi(\mathfrak p)$，而 R540 的完整角色满足
$\xi^3=1$，所以 $r(t)^6=1$。

在二挠点 $t=(e,0)$，$e^3=-1$。
标准原 division 多项式在此有精确闭式
$$
\boxed{
\psi_n(t)=(-1)^{(n-1)/2}
 (3e^2)^{(n^2-1)/4}\qquad(n\text{ 奇}).
}
\tag{12}
$$
例如 $\psi_3(t)=-(3e^2)^2$；将偶数 division 值为零代入
原奇数递推，即逐奇数归纳得到 (12)，包括该符号。
原规范 $\psi_p=r^p$，且 $e\in\mathbf F_p$，因而
$$
r(t)^6
=\left((-1)^{(p-1)/2}(3e^2)^{(p^2-1)/4}\right)^6
=1.
\tag{13}
$$
最后一步使用 $3(p^2-1)/2$ 是 $p-1$ 的整数倍。
这没有从若干小素数的相位认定一般情况。

$V$ 置换两类 torsion，(11)–(13) 于是证明 (4)。
特别，如果任一目标最高系数为零，同一原函数在
整个非零 $E[\delta]$ 和整个非零 $E[2]$ 上的值都准确为零。
这与 R565 的非零 $p$-torsion deck 相位并不矛盾：
本节使用的是固定的二、三挠点，未把原点消失搬到 $\ker V$。

## 5. 一个非 exact 配对的完整 Cartier 输出

取固定有理参数
$$
\tau=-x/y,\qquad
d\log\tau
=\left(\frac1{3X}-\frac1{2(X+b)}\right)dX,\qquad X=x^3.
\tag{14}
$$
先保任意 $\mathbf F_p^\times$ 中的 $b$；
本节的代数引理适用于所有满足
$P(0)=-2ba$、$P(-b)=3ba$、$a=[X^p]P$ 的多项式。

在商曲线 $\mathbf P^1_X$ 的 $0,-b,\infty$ 三处作完整部分分式：
$$
P(X)\left(\frac1{3X}-\frac1{2(X+b)}\right)
=\frac{P(0)}{3X}-\frac{P(-b)}{2(X+b)}+S(X).
$$
$S$ 的次数至多为 $p-1$，其最高系数是 $-a/6$。
Cartier 固定 $d\log X,d\log(X+b)$；
在 $S(X)dX$ 中只有 $X^{p-1}dX$ 项贡献。
所以这是**整个有理微分**的等式：
$$
\boxed{
\mathcal C(P(X)d\log\tau)
=-a\left(
 \frac16dX+\frac{2b}{3}d\log X+\frac{3b}{2}d\log(X+b)
 \right).
}
\tag{15}
$$
Cartier 与可分的 $E\to E/\mu_6=\mathbf P^1_X$ 拉回交换。
写成原椭圆函数即
$$
\boxed{
\mathcal C(P(X)d\log\tau)
=-a\,\Psi_b,\qquad
\Psi_b=
\left(x^2y+4b\frac yx+9b\frac{x^2}{y}\right)\omega_E.
}
\tag{16}
$$
$\Psi_b$ 的 $O$ 极点恰为七，另有固定二、三挠点上的简单极点。
其 $x^2y\omega_E=dX/6$ 系数是一，故始终非零。
所有三个坐标都已计算，不能把两个 logarithmic 分量删掉。

回到 (1)，(4) 使两个原函数都满足这一引理。
结合 (3)，在原基 frame 上严格得到
$$
\boxed{
\begin{aligned}
\mathcal C(\mathcal R_4d\log\tau)
 &=-\frac{\Omega_{p,0}^2I_{4,0}}{\mathfrak h}\,\Psi_1,\\
\mathcal C(\mathcal R_1d\log\tau)
 &=-\frac{\Omega_{p,0}^5I_{1,0}}{\mathfrak h^4}\,\Psi_1,
\end{aligned}\qquad\text{模 }p.
}
\tag{17}
$$
这是两条指定线性值的全局升级，非 R565 的双线性 Cartier 行。

等价地，原微分及其 Cartier 像在 $O$ 的留数均为 $13ba$，
在两个非零三挠点各为 $-2ba$，在三个非零二挠点各为 $-3ba$。
总留数 $13ba-4ba-9ba=0$。
当前 $p>19$，因而仅这个非 exact 配对的 $O$ 留数也精确读出 $a$。

## 6. 完整 exactness 判据与显示原函数

由 $\Psi_b\ne0$，(16) 的整个 Cartier 像为零当且仅当 $a=0$。
此时 (4) 给
$$
P(X)=X(X+b)Q(X),\qquad \deg Q\le p-3.
$$
于是
$$
P(X)d\log\tau=\frac{2b-X}{6}Q(X)\,dX.
$$
令右边的多项式系数为
$\sum_{j=0}^{p-2}s_jX^j\,dX$。原函数可明确取
$$
\boxed{
F_P(X)=\sum_{j=0}^{p-2}\frac{s_j}{j+1}X^{j+1},
\qquad dF_P=P(X)d\log\tau,\quad F_P(0)=0.
}
\tag{18}
$$
所有 $j+1$ 都小于 $p$，所以这是全局多项式，不含未支付的共振除法。
在原椭圆曲线上的极点至多为 $6p-6$。

对任意 $a$ 也有完整分解。定义同一个通用代表
$$
H_{p,b}(X)=X^p-6X-2b,\qquad
\eta_{p,b}=H_{p,b}(X)d\log\tau .
$$
因 $b^p=b$，
$H_{p,b}(0)=-2b$、$H_{p,b}(-b)=3b$。
所以 $P-aH_{p,b}$ 的次数至多 $p-1$，且被 $X(X+b)$ 整除。
用 (18) 的同一无共振除法得到
$$
\boxed{
P(X)d\log\tau=a\,\eta_{p,b}+dF,\qquad
\deg F\le p-1,\qquad
\mathcal C(\eta_{p,b})=-\Psi_b.
}
\tag{19}
$$
这给两条原行在有理微分模 exact 微分空间中的实际共同代表及全部 exact 部分；这里没有把带固定简单极点的微分当成完备椭圆曲线的无极点 de Rham 类。
两条行属于同一条线上，并未因此产生两个独立的非零限制。

因此对于每个原 $i$，完整等价为
$$
\boxed{
I_{i,0}\in p\mathcal O
\ \Longleftrightarrow\
\mathcal C(\mathcal R_i\,d\log\tau)=0
\ \Longleftrightarrow\
\mathcal R_i\,d\log\tau
\text{ 有 (18) 的全局多项式原函数}.
}
\tag{20}
$$
这里是第一层而非 $p$ 进数恰等于零。
若 $I_{i,0}=0$，当然满足左边；反向没有被证明，也没有被使用。

## 7. 与原 Cartier-zero 规范及 R565 的区别

(2) 的 $\mathcal C(\mathcal R_i\omega_E)=0$ 是原规范，
不是可随意添加 $AX^p+B$ 后仍成立的性质。
R565 (29a) 的分部配对对这些添加不敏感，因而不能单独读出目标。

本篇不同：$d\log\tau$ 非 exact，且整个输出 (16) 包含真正的
最高 Frobenius 系数。固定 torsion 的原来源关系 (4)
又使其余两个坐标与同一个系数相联，才得到全局 (20)。

另一方面，(20) 的原函数依赖 $p$，次数可达 $p-1$。
这不是特征零的有界测度原函数，也没有控制每个普通小球的范数，
更不把一个行的消失提升为 R418 所需的全部饱和 jet 改善。
R565 的非线性单位行仍未给出这里的 $a_4$ 或 $a_1$ 非零。
两行同时为零的可能性仍需新的实际算术或几何约束排除。

## 8. 返回原 b=17 的完整尺度

取 R540 的固定 $\vartheta^6=b=17$、$\phi:E_b\to E_0$，
$X_0=X_b/b$。始终运输同一个 CM 元素 $V$，
不把它暗换成 $\pi_{17}$ 对应的另一个标量。

R565 的 $r,q_i$ 同构及 $D_b=\vartheta D_0$ 给
$$
\boxed{
P_{i,b}(X)=b^{7s}P_{i,0}(X/b),\qquad
a_{i,b}=b^{s-1}a_{i,0}.
}
\tag{21}
$$
全部系数仍在 $\mathbf F_p$。
因为 $b^{6s}=b^{p-1}=1$，(4) 精确变成
$$
P_{i,b}(0)=-2b\,a_{i,b},\qquad
P_{i,b}(-b)=3b\,a_{i,b}.
$$
故 (15)–(20) 直接在原曲线上成立，不能只保一个零性口号。

原周期和矩的真实同构是
$$
\Omega_{p,b}=\vartheta^{-1}\Omega_{p,0},\quad
I_{4,b}=\vartheta^{-4}I_{4,0},\quad
I_{1,b}=\vartheta^{-1}I_{1,0}.
$$
所以 (17) 的原 $b=17$ 版本为
$$
\boxed{
\begin{aligned}
\mathcal C_b(\mathcal R_{4,b}d\log\tau_b)
 &=-\frac{b^s}{\mathfrak h}\Omega_{p,b}^2I_{4,b}\,\Psi_b,\\
\mathcal C_b(\mathcal R_{1,b}d\log\tau_b)
 &=-\frac{b^s}{\mathfrak h^4}\Omega_{p,b}^5I_{1,b}\,\Psi_b,
\end{aligned}\qquad\text{模 }p.
}
\tag{22}
$$
$\mathfrak h$ 仍指基曲线的 Hasse 值；$b^s$ 这个真实单位因子没有删除。
也可以直接从 Cartier 的自然性与 $p^{-1}$ 半线性核对 (22)。
因此原指定负矩的第一层、固定全局 Cartier 行以及显式原函数判据
使用的是同一个来源和同一个普通地点。

配套证书
[check-r570-global-negative-moment-cartier-lines.mjs](../scripts/check-r570-global-negative-moment-cartier-lines.mjs)
用 148 项精确检查核对两个完整 torsion 对角系数、原 division 函数六次相位、
规范 Cartier-zero、所有三极点输出和显式原函数。
只重用已有的 $13,19,31,61$ 四个小纤维，不扩充负矩素数扫描；
全素数结论来自正文的完整 theta 平移及有理 Cartier 证明。
