# R316 — 原低次 sigma 来源、两条完整 p-core 与四因子全部相加 carry

日期：2026-11-13。**状态：以下 degree 1 原 Schwartz 来源、精确全权常数、同一 $E_{17}$ frame 的两条完整测度恒等式，以及 R311 四因子所有输入环带、单位相加 carry 和原有限三线返回均已证明。最后的返回保留两个实际秩零参考的完整斜率；没有把它们或一个非零一阶矩替成目标中央导数。主目标仍未完成。**

沿用 R311 的 $b=17$、$E_b:y^2=x^3+b$、$K=\mathbf Q(\delta)$、
$\delta^2=-3$、$\omega=(-1+\delta)/2$。所有 sigma 都取
$x=z^{-2}+\cdots,y=-z^{-3}+\cdots,\sigma=z+\cdots$，并置
$$\Theta=x\sigma^2,\quad F=\Theta^{17},\quad
C_X=\frac{\Theta(z)\Theta(2z)^2\sigma(4z)}{2240b},\quad
B=\nabla_FC_X=H_1+\frac{H_3}{336b}-\frac{H_5}{840b}.\tag{1}$$
$H_1,H_3,H_5$ 始终是 R307 的三条原来源；它们的原点质量为 $0,1,1$。

## 1. degree 1 的来源必须另付：原 Hermitian 类是二

先在 $E_0:y^2=x^3+1$ 上工作，记实际 Hecke 角色为 $\psi_0$。
它是 R302 的 $\psi_1$，不是本篇目标 $b=17$ 的角色。
对于
$$m\ge0,\qquad m\equiv1\pmod6,\qquad
\chi_m=\psi_0^{2m+1}|\cdot|_K^{-m-1/2},\tag{2}$$
其二处分量在单位上平凡，$\chi_{m,2}(2)=-1$；三处单位角色仍为
$u\bmod\delta$，而 $\chi_{m,3}(\delta)=-i$。原导子是 $(\delta)$。
这与 R302 偶权族在二处的三次单位角色、三处的 $+i$ 都不同。

采用 R290 的加性角色和极化。Yang 的 epsilon 条件
$$\epsilon(1/2,\chi_{m,v},\psi_{K,v}/2)\chi_{m,v}(\delta)
=\epsilon_{K_v/\mathbf Q_v}(\alpha)\tag{3}$$
在二、三处的左端均为 $-1$，其他有限处为 $+1$，无穷处要求正类。
二处这里是**未分歧**角色，$\psi_K/2$ 的奇 conductor 改变给 $-1$；
不能沿用 R302 分歧三次角色的 Gauss 和。三处原剩余 Gauss 和仍为
$i\sqrt3$，epsilon 为 $-i$，再乘 $-i$ 得 $-1$。
因此一个准确的全局代表是
$$\boxed{\alpha=2.}\tag{4}$$

### 1.1 原 dyadic 向量及完整环面

令 $\chi_{-8}$ 是模八的奇二次角色。实际向量为
$$\phi_{\sigma,2}=\sum_{a\in\{1,3,5,7\}}
\chi_{-8}(a)\mathbf1_{a/4+2\mathbf Z_2},\qquad
(\chi_{-8}(1),\chi_{-8}(3),\chi_{-8}(5),\chi_{-8}(7))=(1,1,-1,-1).
\tag{5}$$
其自对偶范数平方为二。以下核定整个环面，不只核定一个偶向量的矩阵。
取 $g_*=(-11+4\delta)/13$、$z_8=e^{\pi i/4}$。R290 的实际 splitting
公式在 $\alpha=2$、二处未分歧 $\chi$ 下给
$$\mu(\omega)=z_8,\qquad \mu(g_*)=z_8,\qquad
\mu(-g_*)=-z_8.\tag{6}$$
例如第一项的二次 Weil 指数为 $z_8^{-3}$，Hilbert 因子为 $-1$，
故乘积确为 $z_8$。主生成元的 Weil 指数为 $z_8$、Hilbert 因子为一。

这里 Rao 核的交叉项须用原正号：在 $\omega$ 处是
$$\frac12\int\psi_2\bigl(3(u^2+4uv+v^2)\bigr)\phi(v)\,dv.\tag{7}$$
不能像处理 R302 偶向量时那样只换 $v\mapsto-v$ 而不支付负号。
设 $z_{64}=e^{2\pi i/64}$。输出先落在 $\tfrac18\mathbf Z_2$；
在 $u=a/8$ 处，完整值是
$$\frac{z_8}{4}\sum_{c=1,3,5,7}\chi_{-8}(c)
z_{64}^{-3(a^2+8ac+4c^2)}.
\tag{8}$$
对十六个 $a\bmod16$，它在奇 $a$ 全部为零，在偶 $a$ 准确等于
$\chi_{-8}(a/2)$（偶参数的角色值取零）。在 $g_*$ 处，输出支撑为
$\tfrac14\mathbf Z_2$，驻相条件是 $a\equiv c\bmod4$，完整值为
$$\frac{z_8\sqrt2}{2}
\sum_{\substack{c=1,3,5,7\\c\equiv a\ (4)}}
\chi_{-8}(c)z_{64}^{-3(11a^2+26ac+11c^2)}
=\chi_{-8}(a).\tag{9}$$
负生成元反射这个奇向量的负号由 (6) 准确补偿。R290 已证明
$\mu_3,-1,g_*$ 拓扑生成 $K_2^1$，所以 (5) 是原完整环面的不变向量。
(8)–(9) 都是有限圆分恒等式，证书逐项在 $\mathbf Q(\zeta_{64})$ 中核定。

三处 $n((2\delta/4)\psi_K)=-2$；Yang 1999 Proposition 1.2(1)、
Corollary 1.4 的原转模仍给
$$\phi_{\sigma,3}=\mathbf1_{3^{-1}\mathbf Z_3},\qquad
\|\phi_{\sigma,3}\|^2=3.\tag{10}$$
其余有限处是标准球。因此原 finite norm 恰为六，且所有数据对 (2)
的整个权族保持不变。

## 2. Jacobi 身份、精确常数与全部权

令 $s=(1-\omega)^{-1}=(3+\delta)/6$，$\Omega_0>0$ 是 $E_0$ 的实周期，
则 $\Gamma_0=\Omega_0(\mathbf Z+s\mathbf Z)$。实际有理支撑是
$x=n/12$、$n$ 奇；二处的 $\chi_{-8}(3n)=\chi_{-8}(n)$ 已保留。
置 $\kappa_\infty=6\sqrt3$，用 R290 的 Hermite 规范，得到
$$b_m^\sigma=\sum_{n\text{ 奇}}\chi_{-8}(n)
H_m\left(\frac{\sqrt{6\sqrt3}}{12}n\right)
e^{-\pi\sqrt3n^2/24}.
\tag{11}$$
这些系数为实数。设 $\tau_0=\delta/3$、
$$F_\sigma(Z)=\sum_{n\text{ 奇}}\chi_{-8}(n)
e^{\pi i\tau_0n^2/8+\pi inZ},\qquad
h_\sigma=\frac{\sqrt{6\sqrt3}}{12\pi i}.
\tag{12}$$
则 Hermite 生成函数是 $e^{-T^2/(8\pi)}F_\sigma(h_\sigma T)$。
原有限系数满足
$$(-1)^{(n-1)/2}e^{\pi in^2/8}=e^{\pi i/8}\chi_{-8}(n),\tag{13}$$
所以 $F_\sigma$ 是模数 $s$ 的原 odd Jacobi theta 的非零常数倍。
由于 $\eta_1=2\sqrt3\pi$，
$$e^{\sqrt3\pi Z^2}F_\sigma(Z)\in
\sigma_\Lambda L(O),\qquad
\sqrt3\pi h_\sigma^2=-\frac1{8\pi}.\tag{14}$$
这个一维空间只有原 sigma 线。因此存在固定纯虚 $C\ne0$，使
$$\sum b_m^\sigma T^m/m!=C\sigma_0(\Omega_0h_\sigma T).\tag{15}$$
这同时支付 degree 一、奇半特征、全部 Gaussian 和首阶一；没有按
Taylor 小数拟合原来源。

Yang Theorem 1.11 此时 $S_1$ 为空，$c(0)=1$。由 (10)–(11) 和原
$\mu_6$ 商的体积六，Theorems 2.6、2.15 给
$$L(\psi_0^{2m+1},m+1)=
\frac{\pi\sqrt{12\sqrt3}}{54\sqrt3}
\frac{(4\pi)^m}{m!}(b_m^\sigma)^2,qquad m\equiv1\pmod6.
\tag{16}$$
原实权因子是 $((2\pi/\sqrt3)4\pi h_\sigma^2)^m=(-1/3)^m$。
$C^2<0$ 与合法奇权的负号相消，故 (16) 的固定正常数可由第一权支付。

### 2.1 原导子两点给 $1/9$

写 $\varpi_0=s\Omega_0$、$P=\varpi_0/\delta$。
因为 $s/\delta=2/3-s$，原分支准确是 $P=(0,1)$；R302 已核实这个实
三挠分支。三次 CM 固定性给 reduced $\xi(P)=0$。
R298 的原 Kronecker 展开在 $[zw]$ 给
$$c_{11}(P)=-\xi(P)x(P)-y(P)=-1,\qquad c_{11}(-P)=1.\tag{17}$$
角色 $\psi_0^3$ 的原导子是 $\delta$，两个非零陪集的有限权分别为
$1,-1$。完整 $\mu_6$ 除数、面积和阶乘都按 R298 保留，故
$$\frac{(2\pi/\sqrt3)L(\psi_0^3,2)}{\varpi_0^3}
=\frac{\bar\delta}{6\delta^2}\,(-2)=-\frac\delta9.
\tag{18}$$
$s^3=\delta/9$ 与 $-\omega(1-\omega)=-\delta$ 因而给出全部权的准确式。
若 $\sigma_0=\sum a_mz^m$，则
$$\boxed{
\frac{(2\pi/\sqrt3)^mL(\psi_0^{2m+1},m+1)}{m!\Omega_0^{2m+1}}
=\frac19\,3^{-m}a_m^2,qquad m\equiv1\pmod6,}
\tag{19}$$
$$\boxed{
\frac{(2\pi/\sqrt3)^mL(\psi_0^{2m+1},m+1)}{m!\varpi_0^{2m+1}}
=\frac{-\omega(1-\omega)}9\,a_m^2.}
\tag{20}$$
特别第一权不为零。这个 weight-four 临界值只用于支付真实测度及其
尺度，不被当成目标 $H_1$ 的中央导数。

## 3. 同一 $E_{17}$ frame 的两条完整 p-core

固定 $p>7,p\equiv1\pmod3$，取与 R300 相同的普通嵌入及
$$\pi=\psi_{17}(\mathfrak p),\quad \bar\pi=\psi_{17}(\bar{\mathfrak p}),
\quad\pi\bar\pi=p,\quad
\varepsilon=\frac{\psi_0(\mathfrak p)}{\psi_{17}(\mathfrak p)}
=\left(\frac{17}{\mathfrak p}\right)_6\in\mu_6.
\tag{21}$$
令 $\Omega_p$ 是同一个 $E_{17}$ 形式群周期，$\nu_\Theta,\nu_\sigma$
的原 Amice 变换为 $\Theta(\Omega_p\log(1+Z))$、
$\sigma(\Omega_p\log(1+Z))$。二者整且有界，由 R300 的真实
Mazur–Tate sigma 整性给出，Gaussian 修正仍因三次 CM 为零。
记
$$T_p=\bar\pi[\bar\pi^2]_*\psi_p,\quad
\varkappa=p/\bar\pi^2,\quad
\lambda_\Theta=\varepsilon/\bar\pi,\quad
\lambda_\sigma=\varepsilon^3/\bar\pi.
\tag{22}$$

**定理 1。** 完整测度身份是
$$\boxed{T_p\nu_\Theta=\varepsilon\nu_\Theta,qquad
T_p\nu_\sigma=\varepsilon^3\nu_\sigma,}
\tag{23}$$
$$\boxed{\nu_\Theta|_{p\mathbf Z_p}=
\lambda_\Theta[\varkappa]_*\nu_\Theta,qquad
\nu_\sigma|_{p\mathbf Z_p}=
\lambda_\sigma[\varkappa]_*\nu_\sigma.}
\tag{24}$$

**证明。** 先用 $E_0$ 自己的 $\pi_0=\psi_0(\mathfrak p)$。
R300 的 division 函数 $r_a=\sigma(az)/\sigma(z)^{Na}$ 对奇 $Na$ 仍是
椭圆函数。其半特征的核定不要求 $N$ 偶，因此同一个原逐支计算给
$$T_{p,0}(\sigma_0^Nf)=\frac{\bar\pi_0}{p}\sigma_0^N
\operatorname{Tr}_{[\pi_0]}
\left[(r_{\bar\pi_0}/r_{\pi_0})^Nf\circ[\bar\pi_0]\right]
\tag{25}$$
对 $N=1,2$ 都成立。它保持完整的 $\sigma_0L(O)$、$\sigma_0^2L(2O)$。
前者一维；后者的 $\mu_6$ 不变线准确是 $\Theta_0$。
两条标量由整性及原首阶一/质量一都是整的。

R302 的 (4) 和本篇 (20) 分别给两条真正的正权 Katz 平方。
采用 R295–300 的密集正权极限，非单位矩的赋值至少为权，先得到
完整单位 Mellin 的平方；这个步骤不使用所求 core。
再使用 (25) 的整标量 $c$，在非零正权比较
$1-ce_m$ 与原 Euler $1-e_m$，得到
$(c-1)e_m(2-(c+1)e_m)=0$。正权 $v_p(e_m)>0$、$p>7$，最后因子是单位，
故两条标量均为一。sigma 可直接用其第一权；Theta 的非零中央值与
密集正权保证至少一个非零正权。这样符号也已确定。

最后令 $\theta=17^{1/6}>0$，并固定其普通嵌入。真实同构给
$$\Omega_{p,0}=\theta\Omega_p,\quad
\Theta_b(z)=\Theta_0(\theta z),\quad
\sigma_b(z)=\theta^{-1}\sigma_0(\theta z).\tag{26}$$
这是真正形式群同构，不是在 $\mathbf Z_p$ 的测度变量上任意乘 $\theta$。
因为 $\pi_0=\varepsilon\pi$、$\bar\pi_0=\varepsilon^{-1}\bar\pi$，
原 $E_0$ core 的变量缩放是 $\varepsilon^2\varkappa$。
真实 $\mu_6$ 型给 $[u]_*\nu_\Theta=\nu_\Theta$、
$[u]_*\nu_\sigma=u\nu_\sigma$。故前者留下 $\varepsilon$，后者留下
$\varepsilon\varepsilon^2=\varepsilon^3$，即 (23)–(24)。$\square$

一个独立的有限规范核定是：令 $\gamma=4+\omega$，R297 原两个
CM13 division 函数的完整纤维迹给
$$\mathscr M_\gamma\sigma=-\gamma\sigma,qquad
\mathscr M_\gamma\Theta=-\omega^2\gamma\Theta.\tag{27}$$
目标实际 Frobenius 为 $-\gamma$，$\varepsilon=\omega^2$，所以 (27)
与 (23) 完全一致。负号必须同时在 pull 和 trace 两侧换元；
$\mathscr M_{-\gamma}=\mathscr M_\gamma$ 对 sigma 奇线也成立。

## 4. 全部矩、tame、两条 Katz 斜率及真实质量

设 $\Theta=\sum r_mz^m$、$\sigma=\sum a_mz^m$。由完整 (24) 得
$$\int_{\mathbf Z_p^\times}x^m\,d\nu_\Theta
=\left(1-\varepsilon\frac{\pi^m}{\bar\pi^{m+1}}\right)
\Omega_p^m m!r_m,
\tag{28}$$
$$\int_{\mathbf Z_p^\times}x^m\,d\nu_\sigma
=\left(1-\varepsilon^3\frac{\pi^m}{\bar\pi^{m+1}}\right)
\Omega_p^m m!a_m.
\tag{29}$$
这包括全部整数权；不合 $m\equiv0$ 或 $1\pmod6$ 的矩为零。
对任意 tame 指数 $j$，把第 $n$ 环带变量归一为 $x/p^n$，则其 Mellin
准确是 $\lambda_G^n\tau(\bar\pi)^{-2nj}
\langle\bar\pi\rangle^{-2ndu}$ 乘单位 Mellin，其中 $d=p-1$。
因此全部环带的质量、对数尺度和 tame 均由 (24) 给出。

特别置
$$V(u)=\int_{\mathbf Z_p^\times}\langle x\rangle^{du}\,d\nu_\Theta,qquad
U(u)=\int_{\mathbf Z_p^\times}x\langle x\rangle^{du}\,d\nu_\sigma.
\tag{30}$$
其中心是
$$\boxed{V(0)=1-\varepsilon/\bar\pi,qquad
U(0)=\Omega_p\left(1-\varepsilon^3\pi/\bar\pi^2\right).}
\tag{31}$$
二者都是单位。第二条显然；第一条等于 $1-\bar\pi_0^{-1}$。
$E_0$ 有有理二挠，故 $a_p(E_0)$ 偶。Hasse 界在 $p>7$ 排除
$a_p\equiv1\bmod p$ 的其他代表，而偶性排除一，所以第一条也为单位。

原 primitive Katz 分支及全部周期给
$$\boxed{\mathcal K_\Theta(u)=
\frac{\theta(1-\omega)\Omega_p}{6}
\langle2\rangle^{-du}V(u)^2,\qquad
\mathcal K_\sigma(u)=
\frac{-\omega(1-\omega)\sqrt{17}\,\Omega_p}{9}U(u)^2.}
\tag{32}$$
第一条使用 R302 的 CM 权二；第二条使用 (20) 的 CM 权一。
在 (26) 中，sigma 的总矩还乘 $\theta$，Katz 周期再乘 $\theta$，所以
第二常数是 $\theta^3=\sqrt{17}$，不能写成 $\theta$。
两条原辅助理想 $(5)$ 的平滑值都是 $-30$，对当前 $p$ 为单位；
没有引入不同的 imprimitive 中央因子。
于是
$$\frac{V'(0)}{V(0)}=\frac12
\left(\frac{\mathcal K_\Theta'(0)}{\mathcal K_\Theta(0)}+d\log_p2\right),
\quad
\frac{U'(0)}{U(0)}=\frac12
\frac{\mathcal K_\sigma'(0)}{\mathcal K_\sigma(0)}.
\tag{33}$$
原倍点因子的单位行分别为
$\langle2\rangle^{du}V(u)$ 与 $4\langle4\rangle^{du}U(u)$。
因此其导数分别增加 $d\log2\,V(0)$ 与 $4d\log4\,U(0)$。
这些是准确尺度项；(33) 不给两个完整 Katz 对数导数赋值。

## 5. 四变量的全部输入环带：质量一必须保留

写 $\nu_G^\times=\nu_G|_{\mathbf Z_p^\times}$。
$\nu_\sigma$ 的总质量为零，但 $\nu_\Theta$ 的总质量为一，且
$\nu_\Theta(p^n\mathbf Z_p)=\lambda_\Theta^n$ 不趋于零。
因此不能直接写一个没有边界项的四重环带无穷和。
正确的完整重构是
$$\eta_\Theta=\nu_\Theta^\times-(1-\lambda_\Theta)\delta_0,
\quad\eta_\sigma=\nu_\sigma^\times,
\tag{34}$$
$$\boxed{\nu_\Theta=\delta_0+
\sum_{n\ge0}\lambda_\Theta^n[\varkappa^n]_*\eta_\Theta,qquad
\nu_\sigma=\sum_{n\ge0}\lambda_\sigma^n[\varkappa^n]_*\eta_\sigma.}
\tag{35}$$
两条 $\eta$ 的质量都为零。有限项望远镜求和后，余项是
$\lambda_G^N[\varkappa^N]_*(\nu_G-\nu_G(\mathbf Z_p)\delta_0)$，
它在任意连续测试函数上趋于零，证明 (35)。这是有界测度的弱收敛，
并没有假设 $p$ 进测度对任意可数分割具有实测度式的可加性。

在 R311 原四变量中置
$$y=x_1+2x_2+2x_3+4x_4,\quad
K_u(x)=\mathbf1_{y\in\mathbf Z_p^\times}
(y-17x_1)\langle y\rangle^{du}.
\tag{36}$$
完整的实际中央行就是
$$I(u)=\frac1{2240b\Omega_p}\int K_u\,
d(\nu_\Theta^{\otimes3}\otimes\nu_\sigma)
=J_1(u)+\frac{J_3(u)}{336b}-\frac{J_5(u)}{840b}.
\tag{37}$$
将 (35) 代入得到一份收敛的、包括所有输入环带的明确表达：
对 $A\subseteq\{1,2,3\}$，令未在 $A$ 的变量为零；
对 $i\in A\cup\{4\}$ 取 $n_i\ge0$，在 $K_u$ 中代入
$x_i=\varkappa^{n_i}t_i$，以
$$\lambda_\Theta^{\sum_{i\in A}n_i}\lambda_\sigma^{n_4}
\bigotimes_{i\in A}\eta_\Theta(t_i)\otimes\eta_\sigma(t_4)
\tag{38}$$
积分并求和，再除以 $2240b\Omega_p$。只有 $\min n_i=0$ 的项可贡献。

**完整尾界。** 将每条质量零测度改写为测试函数减去该变量为零的值。
若 $n_i>0$，此有限差分不改变 (36) 的单位条件；在每个单位剩余圆盘上
$K_u$ 关于这些变量解析，至多四次混合导数的范数不超过一。
每个这样的差分至少贡献 $p^{n_i}$，所以 (38) 的项在同一个 $u$ 的
单位闭盘上赋值至少 $\sum n_i$。同样的结论适用于 $u$ 导数。
故总指标至少 $N$ 的尾赋值至少 $N$，允许逐项求原中央导数。
所有单位相加后落入 $p\mathbf Z_p$ 的情况仍在 (36) 的指示函数中；
没有按各输入是否为单位来替换输出条件。

## 6. 真实相加 carry 准确返回原三线

这一部分利用 (24) 的特殊相位，进一步将全部**聚合的**输出环带返回
已经付清的原来源，不引入任意全纯角格。
令 $\mathcal D=\mathbf Z_p^4\setminus(p\mathbf Z_p)^4$，即至少一个输入为
单位，$\nu=\nu_\Theta^{\otimes3}\otimes\nu_\sigma$。
四个输入全在 $p\mathbf Z_p$ 的系数准确为
$$\boxed{\lambda_\Theta^3\lambda_\sigma=\bar\pi^{-4}.}
\tag{39}$$
原 $\varepsilon$ 的六次相位完全相消。若还乘原权
$(y-17x_1)/\Omega_p$，同时缩放四输入另贡献 $\varkappa$；
系数因此是 $p/\bar\pi^6$，这一个 $p$ 不能删去。

定义两个真实 carry 测度（输出变量已经除以 $p^n$）：
$$\mathfrak C_n=\frac1{2240b}
(y/p^n)_*\left(\mathbf1_{\mathcal D,\ v_p(y)=n}\nu\right),
\tag{40}$$
$$\mathfrak B_n=\frac1{2240b\Omega_p}
(y/p^n)_*\left(\mathbf1_{\mathcal D,\ v_p(y)=n}
(y-17x_1)\nu\right).
\tag{41}$$
它们都支撑在单位群。第零层准确为
$\mathfrak C_0=\nu_{C_X}^\times$、$\mathfrak B_0=\nu_B^\times$。

**定理 2。** 对全部 $n\ge1$，完整测度等式为
$$\boxed{\mathfrak C_n=\bar\pi^{-n}[\bar\pi^{-2n}]_*
\left((T_p^n-\bar\pi^{-3}T_p^{n-1})\nu_{C_X}\right)^\times,}
\tag{42}$$
$$\boxed{\mathfrak B_n=\bar\pi^{-n}[\bar\pi^{-2n}]_*
\left((T_p^n-p\bar\pi^{-5}T_p^{n-1})\nu_B\right)^\times.}
\tag{43}$$

**证明。** 由定义 $\nu_G|_{p^n}=\bar\pi^{-n}[\varkappa^n]_*T_p^n\nu_G$。
先将输出第 $n$ 环带取出并除以 $p^n$。再减去四输入全在 $p$ 内的
部分；由 (39)，它分别是第 $n-1$ 输出环带的
$\bar\pi^{-4}[\varkappa]_*$ 或 $p\bar\pi^{-6}[\varkappa]_*$。
这给 (42)、(43) 的第二项。原 R311 卷积和权身份保证这里始终是同一
$C_X,B$；没有将原加法卷积换成 Mellin 乘积。$\square$

R311 已付
$$C_X=\sum_{j=5,11,17}a_jY_j,qquad
a_j=-\frac{T_j^2+T_j-8}{10080b},\qquad T_j^3-3T_j-1=0.
\tag{44}$$
三条真实 $T_p$ 特征值为 $c_j=\xi_j(\mathfrak p)$。
其原有限公式给 $c_j^3=\chi_{17}(\pi)^{-j}$。
因为 $\psi_{17}((\pi))=\pi$，有
$\chi_{17}(\pi)=\varepsilon$；而 $j\equiv5\pmod6$，所以
$$\boxed{T_p^3\nu_{C_X}=\varepsilon\nu_{C_X}.}\tag{45}$$
另一方面令 $c_1=1,c_3=\varepsilon^{-2},c_5=\varepsilon^{-4}$。
R308 的原三个来源满足
$$\boxed{T_p\nu_{H_k}=c_k\nu_{H_k},\qquad T_p^3\nu_B=\nu_B.}\tag{46}$$
故 (42) 的所有环带都在原 odd 三线，(43) 的所有环带都在原 even 三线。
这给真正的有限返回，而不只是一个 ambient 矩阵的可逆性。
例如对 $n\ge1$，
$$\mathfrak C_{n+3}=\varepsilon\bar\pi^{-3}[\bar\pi^{-6}]_*\mathfrak C_n,
\qquad
\mathfrak B_{n+3}=\bar\pi^{-3}[\bar\pi^{-6}]_*\mathfrak B_n.
\tag{47}$$

### 6.1 全部中央导数，含每层质量

记 $\alpha_1=1,\alpha_3=1/(336b),\alpha_5=-1/(840b)$，
$J_k$ 是原 principal 单位 Mellin；$U_j$ 是 R311 的原 tame-one 单位行。
则 $n\ge1$ 时，(42) 的 $x\langle x\rangle^{du}$ 行和 (43) 的
$\langle x\rangle^{du}$ 行准确为
$$\bar\pi^{-3n}\langle\bar\pi\rangle^{-2ndu}
\sum_j a_j(c_j^n-\bar\pi^{-3}c_j^{n-1})U_j(u),\tag{48}$$
$$\bar\pi^{-n}\langle\bar\pi\rangle^{-2ndu}
\sum_{k=1,3,5}\alpha_k(c_k^n-p\bar\pi^{-5}c_k^{n-1})J_k(u).
\tag{49}$$
因此其中央导数分别将方括号中的原 $U_j',J_k'$ 替为
$$U_j'(0)-2nd\log_p\bar\pi\,U_j(0),\qquad
J_k'(0)-2nd\log_p\bar\pi\,J_k(0).
\tag{50}$$
全部原质量已经确定：
$$J_1(0)=0,\quad m_3:=J_3(0)=1-\varepsilon^{-2}/\bar\pi,\quad
m_5:=J_5(0)=1-\varepsilon^{-4}/\bar\pi,
\quad U_j(0)=\Omega_p(1-c_j\pi/\bar\pi^2).
\tag{51}$$
特别
$$\boxed{I(0)=\frac{3-(5\varepsilon^4-2\varepsilon^2)/\bar\pi}{1680b}.}
\tag{52}$$
$m_3$ 由 R308 是单位；$m_5$ 可能损一 $p$，这里没有把它除成单位。

若 $\varepsilon^2\ne1$，原三条 $c_1,c_3,c_5$ 不同。
将 (49) 乘回 $\bar\pi^n\langle\bar\pi\rangle^{2ndu}$ 后，
第 $1,2,3$ 层是一个真实 Vandermonde 观察；
$c_k-p\bar\pi^{-5}$ 都是单位，所以它完整恢复同一三条 $J_k$。
若 $\varepsilon^2=1$，三条 $c_k$ 同为一，全部层只能读同一组合 $I$。
这两个实际情况都不允许把每个 carry 的中央导数另行置零。

### 6.2 同一三线中的真实五因子行

同一实际倍点参考还有一个可以用本篇同样方法支付的行：
$$U=\Theta(z)\Theta(2z)^4
=\frac{-336bH_1+5H_3+4H_5}{9}.\tag{52a}$$
此身份直接由
$(-336bP_1+5P_3+4P_5)/9=X(X-8b)^4$ 核定。
五输入的原求和变量是 $y_5=x_1+2x_2+2x_3+2x_4+2x_5$。
其全非单位输入系数为 $\varepsilon^5/\bar\pi^5$，所以对应
$\mathcal D_5$、$v_p(y_5)=n\ge1$ 的 primitive-input carry 准确是
$$\boxed{\bar\pi^{-n}[\bar\pi^{-2n}]_*
\left((T_p^n-\varepsilon^5\bar\pi^{-4}T_p^{n-1})\nu_U\right)^\times.}
\tag{52b}$$
这里 $T_p^3\nu_U=\nu_U$，单位质量为 $(5m_3+4m_5)/9$。
这是另一条实际原三线返回，其全部质量和导数仍按 (50) 保留。
$U^2$ 的十输入全非单位系数为 $\varepsilon^{10}/\bar\pi^{10}$，
但 (52b) 的三线周期不能通过乘法转给 $U^2$。

## 7. 与原参考相对斜率的准确比较

本篇所有低次常数和 $\log2,\log4$ 都已支付，但它们不是孤立的非零
右端。为了明确同一中央核究竟还读什么，令
$$\ell_3=J_3'(0)/m_3,\qquad \ell_5=J_5'(0)/m_5,
\qquad R(u)=I(u)/J_3(u).
\tag{53}$$
$m_5\ne0$，即使它不是单位此记号也合法；以下总以 $m_5\ell_5$ 组合出现。
由原 (37) 直接得到
$$\boxed{\frac{J_1'(0)}{m_3}
=R'(0)+\frac{m_5}{840b\,m_3}(\ell_5-\ell_3).}
\tag{54}$$
$R'$ 的完整核由 (34)–(38) 给出，或由所有 (43)–(50) 的原返回读取。
这已准确消掉共同参考的单独斜率，而没有让 $\ell_5-\ell_3$ 消失。

例如在同一个积分中写 $z=y/4$、
$\widetilde w=z-17x_1/4$，则
$$I(u)=\frac{4\langle4\rangle^{du}}{2240b\Omega_p}
\int_{z\in\mathbf Z_p^\times}\widetilde w\langle z\rangle^{du}\,d\nu.
\tag{55}$$
于是明确的尺度项为 $d\log4\,R(0)$，而完整余项是
$$R'(0)=d\log4\,R(0)
+\frac4{2240b\Omega_p m_3}
\int_{z\in\mathbf Z_p^\times}\widetilde w
\bigl(d\log_p z-\ell_3\bigr)\,d\nu.
\tag{56}$$
它仍有原输出单位条件及相加对数，(38) 给它可逐项求导的全部环带。
(33) 中的 $\log2$ 同样只在各自真正 Katz 规范中出现。

在 $\varepsilon^2\ne1$ 的情形，(49) 的三层恢复原三行，所以仅给
$J_1'(0)=0$ 还留下两个实际参考斜率；在 $\varepsilon^2=1$ 的情形，
环带返回只给同一 $I$，并不产生一个新原中央约束。
因此本篇没有从低次因子的单位首矩、固定尺度对数或有限返回断言
$J_1'(0)\ne0$。尚须在 (54) 的同一个完整观察上证明新的非零或消去关系。
这也说明为什么保留 (50)、(56) 的质量及相加 carry 是必要的。

## 8. 证书与文献

`scripts/check-jzero-low-degree-core-and-four-factor-carry.py/.json` 给出原
$\mathbf Q(\zeta_{64})$ 所有支撑和相位、Jacobi/Gaussian、真实两点
Kronecker 常数、两条完整 CM13 纤维、全四因子相位及原返回质量的精确证书。
普通测度、无限环带收敛和完整中央式由正文证明，有限证书不替代它们。

- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math.
  **485** (1997), 25–53，Theorems 1.11、2.6、2.15；
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic
  curves*, Compositio Math. **117** (1999), 337–359，Lemma 1.1、
  Proposition 1.2、Corollary 1.4 及 Appendix 的原 splitting；
  <https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- K. Bannai–S. Kobayashi, *Algebraic theta functions and the p-adic interpolation
  of Eisenstein–Kronecker numbers*, Duke Math. J. **153** (2010), 229–295，
  Theorem 1.17；<https://arxiv.org/pdf/math/0610163>。

实际依赖：[R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)、
[R295](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)、
[R298](R298-jzero-exact-central-constant-and-original-kronecker-resolvent.md)、
[R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
[R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)、
[R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)、
[R308](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)、
[R311](R311-jzero-original-odd-six-tame-one-core-and-pure-dyadic-companion.md)。
