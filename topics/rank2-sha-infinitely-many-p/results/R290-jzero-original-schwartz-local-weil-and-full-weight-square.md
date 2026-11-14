# R290 — 新 j=0 曲线的原 Schwartz、三处 Weil 向量与全权实平方

日期：2026-11-13。**状态：以下实际 Hecke 角色、Hermitian 类、2/3/17 三处 Schwartz 函数、全权 theta 平方公式及其六次对称性已证明。它们把 R288/R294 的固定精确秩二曲线接到 Yang 的真实来源；尚未证明任一原 p-adic 中央导数在无穷多个素数处非零。主目标未完成。**

本篇只处理
$$
E^{(0)}:y^2=x^3+17,\qquad
K=\mathbf Q(\delta),\quad \delta=\sqrt{-3}=1+2\omega,\quad
\operatorname{Im}\delta>0.
\tag{1}
$$
$\omega=e^{2\pi i/3}$。R288 已在不假定 Sha 的前提下证明 $\operatorname{rank}E^{(0)}(\mathbf Q)\ge2$，R294 的完整三次下降进一步给出精确秩二。本篇固定 Yang 的极化 $X=\mathbf Q\delta$，不会把 R288 中任意 $\theta_-^N$ 直接当作目标来源。

## 1. 实际 Hecke 角色，尤其十七处的方向

记 $\psi=\psi_{17}$ 为 (1) 取解析微分 CM type 的代数 Hecke 角色，并置
$$
\chi=\psi|\cdot|_K^{-1/2}.
\tag{2}
$$
这里 $|\cdot|_K$ 在理想上表示绝对范数；对 idèle 角色采用与 Yang 一致的对应，使 $\chi_\infty(z)=(z/|z|)^{-1}$。

Silverman–Stange 的已发表六次剩余公式（§6，Theorem 19 的证明）给
$$
\psi_k(\mathfrak p)=-\left(\frac{4k}{\mathfrak p}\right)_6^{-1}\pi,
\qquad \pi\equiv2\pmod3,
\qquad
\frac{\psi_{17}(\mathfrak p)}{\psi_1(\mathfrak p)}
=\left(\frac{17}{\mathfrak p}\right)_6^{-1}.
\tag{3}
$$
基曲线 $y^2=x^3+1$ 的导子是 $(2\delta)$。因 $h_K=1$ 且 $\mu_6\to(\mathcal O_K/2\delta)^\times$ 是同构，素于 $2\delta$ 的每个理想有唯一生成元 $\gamma\equiv1\pmod{2\delta}$，且 $\psi_1((\gamma))=\gamma$。

由主 idèle 积关系，原 $\chi$ 的坏点分量准确如下。

| 地方 | 单位上的角色 | 指定 uniformizer 的值 |
|---|---|---|
| $2$ | $\chi_2(u)=\operatorname{Teich}_{\mu_3}(u\bmod2)$ | $\chi_2(2)=-1$ |
| $3$ | $\chi_3(u)=u\bmod\delta\in\{\pm1\}$ | $\chi_3(\delta)=-i$ |
| $17$ | $\chi_{17}(u)=(u\bmod17)^{48}\in\mu_6\subset\mathbf F_{289}^\times$ | $\chi_{17}(17)=-1$ |

表中 $u\bmod17$ 只指剩余类，角色值取 $\mu_6$ 的唯一提升，不是对 $u$ 作复共轭。十七处的正号 $48$ 是 **idèle 单位分量**；它是理想六次剩余角色在主生成元上的逆。具体地，在 $\omega\bmod\mathfrak p=2$ 的范数七素理想处，
$$
\psi_1(\mathfrak p)=-3-2\omega=-2-\delta,
\qquad
\left(\frac{17}{\mathfrak p}\right)_6=1+\omega,
\qquad
\psi(\mathfrak p)=-2+\omega.
\tag{4}
$$
最后一项迹为 $-5$，和 R288 的 $\#E^{(0)}(\mathbf F_7)=13$ 一致。直接在 $\mathbf F_{289}=\mathbf F_{17}[\delta]$ 计算也给
$$
(-2-\delta)^{48}=(1+\delta)/2,
\qquad (-2-\delta)^{-48}=(1-\delta)/2.
$$
这固定了 (3) 与本地表格之间的逆向，不留下两个共轭候选。

表格还可直接从基角色及六次扭曲验证：$17$ 是 $\mathbf Q_2$ 中的六次幂，所以二处分量不变；三处扭曲为未分歧二次角色，把基值 $\chi_{1,3}(\delta)=i$ 改成 $-i$，但不改变单位角色。由表格可得
$$
\mathfrak f_\psi=(2\delta\cdot17),\qquad
\operatorname N\mathfrak f_\psi=3468,\qquad
N_{E^{(0)}}=3\operatorname N\mathfrak f_\psi=10404.
\tag{5}
$$

## 2. 真正的 Hermitian 类是 $\alpha=17$

固定标准全局加性角色
$$
\psi_{\mathrm{add},\infty}(x)=e^{2\pi ix},\qquad
\psi_{\mathrm{add},\ell}(x)=e^{-2\pi i\{x\}_\ell},\qquad
\psi_{K,v}=\psi_{\mathrm{add},v}\circ\operatorname{Tr}_{K_v/\mathbf Q_v}.
\tag{6}
$$
为区别 Hecke 角色，以下将加性角色始终写成 $\psi_{\mathrm{add}}$。Yang 的局部条件为
$$
\epsilon\left(\tfrac12,\chi_v,\tfrac12\psi_{K,v}\right)\chi_v(\delta)
=\epsilon_{K_v/\mathbf Q_v}(\alpha).
\tag{7}
$$
实际左边在 $2,3,17,\infty$ 分别是 $+1,-1,-1,+1$，其他地方为 $+1$。下面支付其中的 Gauss 因子。

十七处设 $\vartheta(z)=z^{48}$。其在 $\mathbf F_{17}^\times$ 上平凡，且 $\vartheta(\delta)=-1$。按 $z=x+y\delta$ 的 $x$ 分纤维，准确有
$$
\sum_{y:\,x+y\delta\ne0}\vartheta(x+y\delta)^{-1}
=\begin{cases}-16,&x=0,\\1,&x\ne0.\end{cases}
$$
因此
$$
\sum_{z\ne0}\vartheta(z)^{-1}
 e^{-2\pi i\operatorname{Tr}(z)/(2\cdot17)}=-17.
\tag{8}
$$
Tate 的本地 Gauss 式中 $\chi_{17}(17)=-1$、$\sqrt{\#\mathbf F_{289}}=17$，故 epsilon 因子为 $+1$，再乘 $\chi_{17}(\delta)=-1$ 得 (7) 的 $-1$。

二处的 $\mathbf F_4$ Gauss 和为 $1-\omega-\omega^2=2$。相对于 $\psi_K$，uniformizer 值 $-1$ 产生 epsilon $-1$；改用 $\psi_K/2$ 又乘 $\chi_2(1/2)=-1$，所以结果 $+1$。三处 $n(\psi_K/2)=-1$、$a(\chi_3)=1$，Tate 式取 $c=\delta^2$。其剩余二次 Gauss 和是 $i\sqrt3$，而 $\chi_3(\delta)^2=-1$，故 epsilon 为 $-i$；再乘 $\chi_3(\delta)=-i$ 得 $-1$。无穷处由 Yang 的 Hermite 公式得到正 Hermitian 类。

非分歧二次扩张 $K_{17}/\mathbf Q_{17}$ 的范数有偶数赋值，而 $17$ 的赋值为一；在分歧处 $K_3/\mathbf Q_3$，单位 $17\equiv-1\pmod3$ 不是范数。二处 $17$ 为单位范数，且 $17>0$。所以
$$
\boxed{\alpha=17}
\tag{9}
$$
满足全部 (7)，由局部–全局范数原理它确定了所需类。这里没有预先选择 $\alpha=1$。

在 Yang 的标准基 $\{\delta,1/(\Delta\alpha)\}$、$\Delta=\delta^2=-3$ 中，实际嵌入是
$$
\iota_{17}(x+y\delta)=
\begin{pmatrix}x&153y\\-y/51&x\end{pmatrix}.
\tag{10}
$$
这也是下述有限矩阵和 Gaussian 尺度的统一规范。

## 3. 十七处的偶三次向量：不能漏掉 quadratic splitting

这里
$$
n\left(\frac{17\delta}{4}\psi_K\right)=-1=2\cdot0-1.
$$
因此必须使用 Yang 的 **奇导子** lattice model：
$$
L=\delta\mathbf Z_{17}\oplus17^{-1}\mathbf Z_{17},\qquad
e_a=\mathbf1_{a/17+\mathbf Z_{17}},\quad a\in\mathbf F_{17}.
\tag{11}
$$
十七维有限 Weil 块缺少唯一二次环面角色 $\eta_0$。更重要的是，Yang 1999，Proposition 1.2(3) 给原 Hecke splitting 与这个 $\mu_4$ splitting 的差：对未分歧基角色，差正是 $\eta_0$。

Hilbert 90 写 $g=z/\bar z=z^{-16}$。由于真实单位角色是 $z^{48}$，相应环面角色为
$$
\eta(g)=g^{-3},\qquad
\xi(g)=\eta_0(g)\eta(g).
\tag{12}
$$
要求原 $\omega_{17,\chi}$ 不变，故在有限 $\mu_4$ 模型中必须取
$$
\tau=\xi^{-1}=\eta_0\eta^{-1},\qquad \tau(g)=g^{12}.
\tag{13}
$$
它是偶的三次角色。裸六次角色 $\eta$ 是奇的，但这不等于原不变向量是奇的。

取
$$
g_0=2+4\delta\in\mathbf F_{289}^1,
\qquad g_0^{18}=1,\qquad g_0^6=\omega,\qquad \tau(g_0)=\omega^2.
$$
令 $\zeta=e^{2\pi i/17}$、$s_{17}=\sqrt{17}>0$。在 (11) 的真实坐标中，对 $g=x+y\delta$、$y\ne0$，有限算子为
$$
W(g)_{ab}=-\frac{(y/17)}{s_{17}}
 \zeta^{\frac3{2y}\{x(a^2+b^2)-2ab\}},
\quad W(1)=1,\quad W(-1)e_a=e_{-a}.
\tag{14}
$$
所有指数都在 $\mathbf F_{17}$ 中读取。它由 Yang 1999 的 Proposition 1.5 及 Appendix (A6)–(A11) 的实际转模得到；$\Delta=-3$ 和 (6) 的负有限加性角色给出式中的正 $3$。有限 Gauss 合成也直接验证这是环面的表示。

将 $e_0$ 投到 (13)，再乘 $9s_{17}$，得到一个整代数向量 $f_{17}$：
$$
f_{17}=9s_{17}\cdot\frac1{18}
 \sum_{k=0}^{17}\omega^kW(g_0^k)e_0.
\tag{15}
$$
其每个坐标只有以下八项：
$$
\begin{aligned}
f_{17}(a)=s_{17}\mathbf1_{a=0}
-\big(&\omega\zeta^{5a^2}+\omega^2\zeta^{15a^2}
+\zeta^{10a^2}-\omega\zeta^{6a^2}
-\omega^2\zeta^{11a^2}\\
&+\zeta^{7a^2}+\omega\zeta^{2a^2}
+\omega^2\zeta^{12a^2}\big).
\end{aligned}
\tag{16}
$$
因此
$$
\boxed{
W(g_0)f_{17}=\omega^2f_{17},\quad
f_{17}(-a)=f_{17}(a)=\overline{f_{17}(a)},\quad
f_{17}(0)=s_{17}-1.}
\tag{17}
$$
共轭实性可直接由 (16) 中指数 $5,12$；$15,2$；$10,7$；$6,11$ 的配对看到。由正交投影或精确 Gauss 计算，
$$
\sum_{a\in\mathbf F_{17}}|f_{17}(a)|^2=9(17-s_{17}).
\tag{18}
$$
取原 Schwartz 函数
$$
\phi_{17}=\sum_{a\in\mathbf F_{17}}f_{17}(a)e_a.
\tag{19}
$$
它是非零的原 $\omega_{17,\chi}$ 不变向量，且在自对偶测度 $\operatorname{vol}(\mathbf Z_{17})=1$ 下范数平方为 (18)。

## 4. 二处：实际积分给四陪集向量

这一处不援引只对奇剩余特征陈述的 lattice 公式。直接用 Yang Appendix (A1)–(A3) 的 Schrödinger splitting：
$$
\omega_{17,\chi}(g)=\mu(g)r_S(\iota_{17}(g)),
\quad
\mu(g)=\chi_2(\delta(g-1))
 \gamma_2(17y(1-x)\psi_{\mathrm{add},2})
 (-3,-2y(1-x))_2.
\tag{20}
$$
写
$$
e_b=\mathbf1_{b/2+2\mathbf Z_2},\quad b=0,1,2,3,
\qquad f_A=e_0-e_2,\quad f_B=e_1+e_3,
\qquad t=\frac{1+\sqrt3}{\sqrt2}.
$$
则所需向量准确为
$$
\boxed{\phi_2=f_A+t f_B,\qquad
(v_2(0),v_2(1),v_2(2),v_2(3))=(1,t,-1,t).}
\tag{21}
$$

下面给出完整的生成元验证。取 $z_8=e^{\pi i/4}$ 和
$$
g_*={-11+4\delta\over13}={1+2\delta\over1-2\delta}.
$$
对于 (6) 的加性角色，若 $a=2^n u$、$u$ 为奇单位，二次 Weil 指数为：$n$ 偶时 $(1+i^{-u})/\sqrt2$；$n$ 奇时 $z_8^{-u}$。由有限二次 Gauss 和直接可得这些式子。代入 (20) 得
$$
\mu(\omega)=-\omega^2z_8,
\quad \mu(\omega^2)=-\omega z_8^{-1},
\quad \mu(g_*)=z_8^{-3}.
\tag{22}
$$
在 $(f_A,f_B)$ 基下，真实 $\omega$ 算子是
$$
M_\omega={\omega^2\over\sqrt2}
 \begin{pmatrix}-z_8&i\\i&iz_8\end{pmatrix},
\qquad
M_\omega\binom1t=\binom1t,
\quad\operatorname{char}_{M_\omega}(X)=(X-1)(X-\omega).
\tag{23}
$$
在 $e_0,e_1,e_2,e_3$ 基下，真实 $g_*$ 算子是
$$
M_*=
\begin{pmatrix}0&0&-1&0\\0&1&0&0\\-1&0&0&0\\0&0&0&1\end{pmatrix}.
\tag{24}
$$
它逐个固定 $f_A,f_B$。

为核实这里没有遗漏支撑，$r_S(\iota(\omega))$ 的核可在偶函数上写成
$$
{1\over\sqrt2}\int
 \psi_{\mathrm{add},2}\left({51\over2}(u^2-4uv+v^2)\right)\phi(v)\,dv.
$$
代入 $v=b/2+2a$ 后积分支撑先落在 $\tfrac14\mathbf Z_2$。对奇数 $c$ 的 $u=c/4$，$e_0-e_2$ 的两项相同而相消，$e_1+e_3$ 的两项相反而相消，所以最后支撑准确落在 $\tfrac12\mathbf Z_2$；留下的四陪集积分就是 (23)。对 $g_*$，同样展开后非零的条件为输出指标 $a\equiv3b+2\pmod4$，其四个相位为 $-1,1,-1,1$，即 (24)。负生成元 $-g_*$ 与 $g_*$ 在偶函数上的 Rao 核相同，而由 (20) 算得 $\mu(-g_*)=-z_8=z_8^{-3}$，因此 $-1$ 也固定这两列。

最后，$\mu_3$、$-1$ 与 $g_*$ 拓扑生成 $K_2^1$。事实上 $K_2^1\cap(1+4\mathcal O_{K_2})$ 经对数等于 $4\delta\mathbf Z_2$，而
$$
\log g_*=4\delta\left(1-4+\frac{144}{5}-\cdots\right)
$$
括号为二进单位。模四的范数条件说明归约到 $1\pmod2$ 的范数一元素只有 $\pm1$ 两个模四类。故以上生成元验证足够支付整个本地环面，(21) 是原不变向量。

每个 $e_b$ 的支撑体积为 $1/2$。于是
$$
\|\phi_2\|^2=1+t^2=3+\sqrt3.
\tag{25}
$$

## 5. 三处及其余地点

三处 $n((17\delta/4)\psi_K)=-2=2(-1)$。由 (7)、$a(\chi_3)=1$ 及 Yang 1999 Proposition 1.2(1)，这里的 splitting 差为平凡。其 Corollary 1.4 的实际 Schrödinger 转模给
$$
\boxed{\phi_3=\mathbf1_{3^{-1}\mathbf Z_3},\qquad \|\phi_3\|^2=3.}
\tag{26}
$$
这依赖于本篇的 $X=\mathbf Q\delta$ 极化，不能在同一 Gaussian 公式中换成 $\mathbf1_{\mathbf Z_3}$。

所有其他有限地点取 $\phi_\ell=\mathbf1_{\mathbf Z_\ell}$。好非分裂点这是 Yang Lemma 2.7 的原不变向量；好分裂点由 Corollary 2.14 的实际极化变换仍得到这个函数。有限整体函数为
$$
\phi_{\mathrm{fin}}=\bigotimes_{\ell<\infty}\phi_\ell.
\tag{27}
$$

## 6. 原全局系数与六次对称性

令
$$
\kappa=|\delta^3\alpha|=51\sqrt3.
\tag{28}
$$
Yang 1999 Lemma 1.1 的无穷处向量为 $\phi_\infty^{(m)}(x)=H_m(\sqrt\kappa x)e^{-\pi\kappa x^2}$，其中
$$
\sum_{m\ge0}H_m(x){T^m\over m!}
=\exp\left(xT-{T^2\over8\pi}\right),
\qquad H_0=1,\quad H_1=x.
\tag{29}
$$
由 (19)、(21)、(26)，有理支撑准确为 $x=n/102$。局部坐标分别为 $2x=n/51\equiv3n\pmod4$、$17x=n/6\equiv3n\pmod{17}$。由于 $v_2(3n)=v_2(n)$，原有限系数是
$$
\boxed{a_n=v_2(n\bmod4)f_{17}(3n\bmod17),\quad
a_{n+68}=a_n=a_{-n}=\overline{a_n}.}
\tag{30}
$$
所以实际 Hermite 系数为
$$
b_m=\sum_{n\in\mathbf Z}a_n
 H_m\left({\sqrt\kappa\,n\over102}\right)
 \exp\left(-{\pi\sqrt3\over204}n^2\right)\in\mathbf R.
\tag{31}
$$
这给出了整个原来源，没有从低阶拟合它的系数。其生成函数可写成
$$
\mathcal B(T)=\sum_{m\ge0}b_m{T^m\over m!}
=e^{-T^2/(8\pi)}F\left({\sqrt\kappa\over204\pi i}T\right),
$$
$$
F(Z)=\sum_{n\in\mathbf Z}a_n
 e^{\pi i(\delta/3)n^2/68+2\pi inZ}.
\tag{32}
$$

**准确的对称性是 $\mathcal B(T)\in\mathbf R[[T^6]]$。** 偶性已由 (30) 证明。对三次单位 $\omega$，原有限向量在每个地点均被原 $\omega_{17,\chi}(\omega)$ 固定：二处用 (23)，三处用 (26)，十七处用 (12)–(17)，其余地点用标准球。无穷处 Hermite 第 $m$ 型的特征为 $\omega^{\pm m}$。全局有理 $\omega$ 的 Weil 作用保持 theta 求和泛函，因此 $3\nmid m$ 时 $b_m=0$。这证明二阶、四阶及所有不合六次权的消失，不依赖数值小量。

## 7. 全权固定来源与完整平方常数

对 $m\ge0$，定义真正的全权角色
$$
\chi_m=\psi^{2m+1}|\cdot|_K^{-m-1/2}=\chi^{2m+1}.
\tag{33}
$$
在 $2$ 处单位角色不变要求 $3\mid m$；在 $3$ 处 uniformizer 值 $(-i)^{2m+1}$ 不变要求 $m$ 偶；十七处六次单位角色不变也要求 $3\mid m$。故
$$
\boxed{6\mid m}
\tag{34}
$$
是这些原有限坏点角色同时保持不变的准确公共周期。对 (34)，(27) 的同一有限 Schwartz 函数适用于 $\chi_m$。好分裂点的未分歧参数虽然随 $m$ 变化，Yang Corollary 2.14 的标准球仍相同；这里没有把完整 Hecke 角色误称为处处不变。无穷处取 (31) 的第 $m$ Hermite 向量。局部 dichotomy 仍是同一个 $\alpha=17$。

设
$$
C_{17}^{(0)}=
{\pi\sqrt{102\sqrt3}\over
153\sqrt3(3+\sqrt3)(17-\sqrt{17})}>0.
\tag{35}
$$
那么对每个 $m\ge0$、$6\mid m$，有准确的全权平方公式
$$
\boxed{
L(\psi^{2m+1},m+1)
=C_{17}^{(0)}\,{(4\pi)^m\over m!}\,b_m^2.}
\tag{36}
$$

**证明，包括测度和全部常数。** 自对偶加法测度下，(18)、(25)、(26) 及 Yang 的 Hermite 范数给原全局向量的平方范数
$$
\mathcal N_m=
{27(3+\sqrt3)(17-\sqrt{17})\over\sqrt{102\sqrt3}}
 {m!\over(4\pi)^m}.
\tag{37}
$$
将向量除以 $\sqrt{\mathcal N_m}$ 后可应用 Yang 1997 Theorem 2.6、Theorem 2.15 的规范化平方公式。其 Theorem 1.11 中的 $S_1$ 准确是两个非分歧但角色分歧的地方 $\{2,17\}$，无坏分裂点，故
$$
c(0)=(1+2^{-1})^{-1}(1+17^{-1})^{-1}=\frac{17}{27}.
\tag{38}
$$
由于 $h_K=1$，每个范数一 idèle 可乘一个全局范数一元素，把好分裂处的赋值全部移到单位群。剩余群由无穷处环面和有限极大紧子群组成；其与 $K^1$ 的交准确是 $\mu_6$。因此 Yang 公式所用的“紧子群体积乘积 / 商体积”之比为 $6$，且 theta 积分为原 $b_m/\sqrt{\mathcal N_m}$ 乘商体积。这一步同时说明未留下一个非平凡理想类求和。

代入 Yang (2.19)，并使用
$L(1,\epsilon_{K/\mathbf Q})=\pi/(3\sqrt3)$，得到
$$
L(\psi^{2m+1},m+1)
={2\over6c(0)}\,{\pi\over3\sqrt3}\,{b_m^2\over\mathcal N_m},
$$
即 (35)–(36)。$\square$

(30) 已证明 $b_m$ 是实数，因此 (36) 是 **同一个真实来源的平方**；没有额外引入一条独立共轭 Mellin 来源。但从平方公式转为 p-adic 中央平方根仍须保留自己的周期、Euler 因子与参数归一，(36) 本身不许可任意删去这些项。

## 8. 中央常数与实际线丛接口

CM 椭圆曲线的已发表 rank-zero 定理给 $L(E^{(0)},1)\ne0\Rightarrow\operatorname{rank}E^{(0)}(\mathbf Q)=0$。与 R288 的秩下界结合，$L(E^{(0)},1)=0$；再用 (36) 的 $m=0$ 得
$$
b_0=0,\qquad \operatorname{ord}_{T=0}\mathcal B(T)\ge6.
\tag{39}
$$
这里常项零使用一个已知 rank-zero 定理；二、四阶零使用上一节已付的全局 $\mu_6$ 对称性。没有把有限精度近零当作证明，也没有在本篇宣称六阶一定非零。

供后续实际几何运输使用，置
$$
\tau_0=\delta/3,\qquad s={1+\tau_0\over2},\qquad
\Lambda=\mathbf Z+s\mathbf Z.
$$
由 (21) 的准确恒等式
$$
v_2(n+2)(-1)^n=-v_2(n)
$$
及十七部分的周期，(32) 直接给
$$
F(Z+1)=F(Z),\qquad
F(Z+s)=e^{-\pi i34s-2\pi i34Z}F(Z).
\tag{40}
$$
所以它从矩形格的次数 $68$ 准确下降为最大整环格 $\Lambda$ 上的次数 $34$ 原截面。此格稳定于 $\omega$；其 quasi-period $\eta_1=2\sqrt3\pi$。设 $\sigma_\Lambda$ 为该格的 Weierstrass sigma，则
$$
S(Z)=e^{34\sqrt3\pi Z^2}F(Z)
\in H^0\bigl(\Lambda,\mathcal O(34O)\bigr),
\qquad
\mathcal B(T)=S\left({\sqrt\kappa\over204\pi i}T\right).
\tag{41}
$$
最后的 Gaussian 等式是准确的，因为
$34\sqrt3\pi(\sqrt\kappa/(204\pi i))^2=-1/(8\pi)$。在 (41) 的同一个原 reduced frame 中，$S$ 偶、$S(\omega Z)=S(Z)$、$S(0)=0$。因此
$$
S(Z)=\sigma_\Lambda(Z)^{34}\wp_\Lambda(Z)^2
 P_4\bigl(\wp_\Lambda(Z)^3\bigr),\qquad \deg P_4\le4,
\tag{42}
$$
其中 $P_4$ 不是本篇任取的多项式，而由 (16)、(21)、(32) 唯一指定。证明是：除以 $\sigma^{34}$ 后为偶椭圆函数，极点只在 $O$、阶至多 $34$，故为 $\wp$ 的至多十七次多项式；$\mu_3$ 角色强迫次数 $j\equiv2\pmod3$；$S(0)=0$ 再删除 $j=17$ 项。得到 $j=2,5,8,11,14$ 五项。

若要返回 (1) 的不变微分 $dz=dx/(2y)$，取实际周期尺度 $\Omega$ 满足其 period lattice 为 $\Omega\Lambda$，于是原变量是 $z=\Omega Z$。不能在下一步省略这个 $\Omega$ 或把 $P_4$ 替换为拟合候选。后继的线丛、三次同源和原多项式识别可在这个准确接口上继续。

## 9. 可复现证书与范围

- `scripts/check-jzero-original-local-weil-and-schwartz.py` 在 $\mathbf Q(\zeta_{51})$、$\mathbf Q(\zeta_{24})$ 中用精确有理多项式运算核实原矩阵、splitting、Gauss 和、向量实性与范数、全权常数。
- 同名 `.json` 保存十七向量全部 power-basis 坐标、八项表、二处原向量和矩阵，以及全局规范；它不含按素数扫描得来的经验判据。
- (42) 的五维空间是实际来源的精确位置；本篇没有从维数小、局部不变或平方公式推出原中央非消失。

## 文献与仓库依赖

1. T. Yang, *Theta liftings and Hecke L-functions*, J. Reine Angew. Math. **485** (1997), 25–53，特别 (2.7)、Theorem 1.11、Corollary 2.14、Theorems 2.6、2.15。作者全文：<https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
2. T. Yang, *Eigenfunctions of the Weil representation of unitary group of one variable*, Trans. Amer. Math. Soc. **350** (1998), 2393–2407，奇导子有限环面模型与缺失二次角色。作者全文：<https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>。
3. T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*, Compositio Math. **117** (1999), 337–359，Lemma 1.1、Proposition 1.2、Corollary 1.4、Proposition 1.5、Appendix (A1)–(A11)。作者全文：<https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
4. J. H. Silverman and K. E. Stange, *Amicable Pairs and Aliquot Cycles for Elliptic Curves*, Experimental Math. **20** (2011), 329–357，§6，Theorem 19 的证明；DOI: 10.1080/10586458.2011.565253。作者预印本：<https://arxiv.org/pdf/0912.1831>。
5. K. Rubin, *Elliptic curves with complex multiplication and the conjecture of Birch and Swinnerton-Dyer*, Invent. Math. **64** (1981), 455–470，Corollary 2.2；这里只使用非零复中央值迫 Mordell–Weil 秩零的方向，亦见上述 Yang 1999 引言及其 [Ru]。
6. [R288 — 原新曲线、秩下界与三次覆盖](R288-jzero-rank-two-cubic-isogeny-and-actual-first-carry.md)。

7. [R294 — 完整三次同源下降与精确秩二](R294-jzero-exact-rank-two-by-rational-three-isogeny.md)。
