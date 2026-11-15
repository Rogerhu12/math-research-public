# R655 — 原 $\sigma^5$ 的完整 Schwartz 身份、$E_{80}$ 共轭 Katz 点与负一单位矩非零

状态：已证明。本文支付 R653 中原 $\Sigma_5=\sigma_{17}^5$ 的固定负一单位矩，而不将 R653 的五输入门、其它两条标量行或全部 $W$ 失败支赋零。

## 0. 准确结论与原来源

沿本题普通 CM 规范，置
$$
K=\mathbf Q(\delta),\qquad \delta^2=-3,\qquad
\omega=\frac{-1+\delta}{2},\qquad s_0=(1-\omega)^{-1}.
$$
$\psi_0$ 是 $E_0:y^2=x^3+1$ 的 $2\delta$-primary Hecke 角色。原 sigma 规范是
$x_\wp=z^{-2}+\cdots$、$y_\wp=-z^{-3}+\cdots$、$\sigma_0=z+\cdots$。
记实周期为 $\Omega_0>0$，CM 生成周期为 $\varpi_0=s_0\Omega_0$。
所有普通形式群周期与 R540 的 $\Omega_{p,0}$ 同步。

R653 的实际来源和测试是
$$
\Sigma_{5,17}(z)=\sigma_{17}(z)^5,\qquad
I_{5,-1}=\int_{\mathbf Z_p^\times}q^{-1}\,d\nu_{\Sigma_{5,17}}(q).
\tag{1}
$$
它来自 $Q_5=c+2d,\ L_5=2c-d$ 的完整联合
$\sigma(q+2l)\sigma(2q-l)\in\mathcal S_5\otimes\mathcal S_5$。
本文不作额外物理尺度替换。

对 $u$ 素于二，令 $t_2(u)\in\mu_3$ 为其模二 Teichmüller 值。对 $u$ 素于五，
令 $[u]_5^4\in\mu_6$ 为 $u^4\in\mathbf F_{25}^\times$ 的唯一六次根提升。定义
$$
\chi((u))=\frac{[u]_5^4}{t_2(u)}.
\tag{2}
$$
该有限角色的准确导子为 $(10)$，且 $\chi^c=\chi^{-1}$。令
$$
A:\quad y^2+y=x^3+1
\quad\longleftrightarrow\quad E_{80}:y^2=x^3+80,
\qquad
\psi_A=\chi^{-1}\psi_0.
\tag{3}
$$
第 7 节将由完整导子分类证明 (3)，并证明 $A$ 的解析秩恰为一。

存在由第 5 节完全确定的固定 $c_5\in\overline{\mathbf Q}^{\times}$，使对每个
$m\ge0,\ m\equiv5\pmod6$，
$$
\boxed{\;
\frac{(2\pi/\sqrt3)^mL(\chi\psi_0^{2m+1},m+1)}
 {m!\varpi_0^{2m+1}}
 =c_5\,5^{-m}\bigl([z^m]\sigma_0(z)^5\bigr)^2.
\;}
\tag{4}
$$
设 $\theta=17^{1/6}$，固定其原普通嵌入；则对于所有 $p>5$、$p\equiv1\pmod3$，
原 primitive Katz 函数满足
$$
\boxed{\;
\mathcal L_{p,5\delta}^{\mathrm{prim}}(\overline{\psi_A})
 =5c_5\theta^{11}\Omega_p\,I_{5,-1}^{\,2}\ne0.
\;}
\tag{5}
$$
特别
$$
\boxed{I_{5,-1}\ne0.}
\tag{6}
$$
(6) 是非零结论，不声称该矩在所有 $p$ 都为单位。本文亦不由 (6) 推出原
rank-two 的某条完整中央导数非零。

主要引用是 Yang 的完整 Weil/Schwartz 公式和全权平方公式，以及
Bertolini–Darmon–Prasanna 2012 的 Theorem 1（Rubin 定理）与 Theorem 3.1。
所有有限计算由
[脚本](../scripts/check-r655-sigma-five-full-schwartz-and-rank-one.mjs)、
[准确证书](../scripts/check-r655-sigma-five-full-schwartz-and-rank-one.json)
复现；没有用少数 CM 特征或浮点 $L$ 值替代来源识别。

## 1. 全部有限角色与 Hermitian 代表

因为 $t_2(v)=v^4$、$[v]_5^4=v^4$ 对 $v\in\mu_6$ 成立，(2) 不依赖理想生成元。
它在 $(\mathcal O_K/10)^\times$ 的七十二个元素上乘法相容，在二、五处均非平凡，
阶恰为六。共轭分别取逆。其完整 idèle 分量是
$$
\begin{array}{c|cc}
 &\text{单位}&\text{uniformizer}\\ \hline
2&t_2(u)&\chi_2(2)=1\\
3&1&\chi_3(\delta)=-1\\
5&[u]_5^{-4}&\chi_5(5)=1.
\end{array}
\tag{7}
$$
其余点未分歧；三处的未分歧负号由全局主 idèle $\delta$ 的乘积公式给出。
有理主理想上 $\chi=1$。表中局部单位值与理想公式 (2) 互逆。

对 $m\equiv5\pmod6$，置
$$
\Phi_m=\chi\psi_0^{2m+1},\qquad
\chi_m=\Phi_m\mathrm N^{-m-1/2}.
\tag{8}
$$
R302 的基单位化角色 $\vartheta=\psi_0\mathrm N^{-1/2}$ 在二处单位为 $t_2$、
$\vartheta_2(2)=-1$；三处单位为模 $\delta$ 的符号、$\vartheta_3(\delta)=i$。
故 (8) 的完整有限数据是
$$
\begin{array}{c|cc|c}
 &\text{单位}&\text{uniformizer}&\text{导子指数}\\ \hline
2&1&-1&0\\
3&u\bmod\delta&i&1\\
5&[u]_5^{-4}&-1&1.
\end{array}
\tag{9}
$$
因此 $\Phi_m$ 的导子准确为 $5\delta$，而不是 $10\delta$。二处的实际取消是
$\sigma^5$ 身份的必要部分。

加性角色固定为 $\psi_\infty(x)=e^{2\pi ix}$、
$\psi_\ell(x)=e^{-2\pi i\{x\}_\ell}$，并取 $\psi_{K,v}=\psi_v\circ\operatorname{Tr}$。
Yang 的局部条件是
$$
\epsilon(1/2,\chi_{m,v},\psi_{K,v}/2)\chi_{m,v}(\delta)
 =\epsilon_{K_v/\mathbf Q_v}(\alpha).
\tag{10}
$$
二处的左边为 $-1$：角色未分歧、uniformizer 为 $-1$，而 $\psi_K/2$ 改变一次加性导子。
三处的剩余 Gauss 和为 $i\sqrt3$，epsilon 为 $-i$，乘 $\chi_{m,3}(\delta)=i$ 后为 $+1$。
五处的准确有限和为
$$
\sum_{u\in\mathbf F_{25}^{\times}}[u]_5^4
 \exp\!\left(-\frac{2\pi i}{5}\operatorname{Tr}_{\mathbf F_{25}/\mathbf F_5}u\right)=-5.
\tag{11}
$$
故 epsilon 为 $+1$，而 $\chi_{m,5}(\delta)=-1$，左边为 $-1$。
将加性角色再乘 $1/2$ 不改变 (11)，因为该有限角色在 $\mathbf F_5^\times$ 平凡。
其余有限点给 $+1$，无穷处取正 Hermitian 类。可选准确代表
$$
\boxed{\alpha=\frac52,\qquad
\iota_\alpha(x+y\delta)=
 \begin{pmatrix}x&9\alpha y\\-y/(3\alpha)&x\end{pmatrix},\qquad
\kappa_\infty=\frac{15\sqrt3}{2}.}
\tag{12}
$$
二、五处的范数奇偶和三处 $5/2\equiv1\bmod3$ 分别验证 (10)。

## 2. 二处的完整 Schwartz 向量

在奇数上取 $\chi_{-2}(1,3,5,7)=(1,1,-1,-1)$。实际向量是
$$
\boxed{\phi_2(x)=-\chi_{-2}(2x)\mathbf1_{v_2(x)=-1},\qquad
\|\phi_2\|^2=1.}
\tag{13}
$$
其四个陪集是 $b/2+4\mathbf Z_2$，$b=1,3,5,7$，各体积 $1/4$。
共同总负号仅固定第 5 节的 Fourier 系数规范。

令 $\zeta_j=e^{2\pi i/j}$，
$g_*=(-11+4\delta)/13=(1+2\delta)/(1-2\delta)$。
Yang Appendix (A1)–(A3)，包括 Hilbert 因子，给
$$
\mu(\omega)=-\zeta_8,\qquad
\mu(g_*)=\zeta_8,\qquad \mu(-g_*)=-\zeta_8.
\tag{14}
$$
例如 $\delta(\omega-1)=3\omega^2$，本篇二处单位角色平凡，
而 $(-3,-3/2)_2=-1$；在 $g_*$ 处
$\delta(g_*-1)=-12(1+2\delta)/13$ 的二赋值为二，
$(-3,-192/169)_2=1$。这确定原 splitting，不能只选一个使向量不变的标量。

省去共同负号，写 $v=(1,1,-1,-1)$。在 $\omega$ 处的完整核为
$$
-\zeta_8\int_{\mathbf Q_2}
 \psi_2\!\left(\frac{15}{4}(u^2+4uv+v^2)\right)\phi(v)\,dv.
$$
驻相先给 $u=k/4$；在该格上其值为
$$
-\frac{\zeta_8}{4}\sum_{b=1,3,5,7}
 v_b\,\zeta_{64}^{-15(k^2+8kb+4b^2)}.
\tag{15}
$$
(15) 对 $k\bmod16$ 的十六个完整值分别是原四个非零陪集的 $v_b$，
其余全零。因而没有遗漏四分之一支撑。

在 $g_*$ 处，核为
$$
2\sqrt2\,\zeta_8\int_{\mathbf Q_2}
 \psi_2\!\left(\frac{15}{16}(11u^2+26uv+11v^2)\right)\phi(v)\,dv.
$$
驻相迫 $u=a/2$、$a$ 奇，且 $13a+11b\equiv0\bmod4$。剩余准确和为
$$
\frac{\zeta_8}{\sqrt2}
 \sum_{\substack{b=1,3,5,7\\13a+11b\equiv0\ (4)}}
 v_b\,\zeta_{64}^{-15(11a^2+26ab+11b^2)}=v_a.
\tag{16}
$$
负生成元的交叉项反号；向量奇性与 (14) 的负号相消，所以它也固定 $\phi_2$。
$\mu_3,-1,g_*$ 拓扑生成整个 $K_2^1$：
$\log(g_*)/(4\delta)$ 是二进单位。故 (13) 是完整局部环面向量，
而不只是 $\omega$ 的一个本征向量。

## 3. 三处与五处的完整向量

### 3.1 三处

(9) 的三处角色与 R302 相同。$5/2$ 在 $\mathbf Q_3^\times$ 是平方单位，
且 $n((\delta\alpha/4)\psi_K)=-2$。
Yang Proposition 1.2(1)、Corollary 1.4(1) 在 (12) 的真实 Schrödinger 极化给
$$
\boxed{\phi_3=\mathbf1_{3^{-1}\mathbf Z_3},\qquad\|\phi_3\|^2=3.}
\tag{17}
$$
这里保留了原支撑 $3^{-1}\mathbf Z_3$，并未在不改变 Gaussian 的情况下换成标准球。

### 3.2 五处

令 $e_b=\mathbf1_{b/5+\mathbf Z_5}$，$b\in\mathbf F_5$。
完整 $\omega$ 矩阵为
$$
\boxed{\;
M_{ab}=\frac{\omega}{\sqrt5}
 \zeta_5^{-2(a^2+4ab+b^2)},\qquad a,b\in\mathbf F_5.
\;}
\tag{18}
$$
原 splitting 为 $\mu_5(\omega)=\omega$：
$\chi_{m,5}(3\omega^2)=\omega$，二次 Weil 指数和 Hilbert 因子均为一。
因 $v_5(\alpha)=1$，原 Rao 核的模因子为 $1/\sqrt5$。
在这五个陪集外驻相消失；故 (18) 是完整值，不是 Taylor 截断。

设
$$
v_5=\frac{I+M+M^2}{3}e_0,\qquad
\phi_5=\sum_{b\in\mathbf F_5}(v_5)_b e_b.
\tag{19}
$$
在 $\mathbf Q(\zeta_{15})$ 中直接得到
$$
M^3=I,\quad M^*M=I,\quad Mv_5=v_5,\quad
(v_5)_{-b}=(v_5)_b\in\mathbf R,
$$
$$
\boxed{\;
n_5:=\|\phi_5\|^2=(v_5)_0=\frac{1-1/\sqrt5}{3}>0.
\;}
\tag{20}
$$
$-1$ 的完整作用为正反射：Yang Proposition 1.2 的符号是
$\chi_{m,5}(-2\delta)(3/5)=(-1)(-1)=1$。
主五单位在该有限模型上平凡，剩余范数一群正是 $\mu_6$；
因此 $\omega$ 和 $-1$ 的检查支付整个 $K_5^1$。这也可直接由
Yang Proposition 1.2(3)–(4)、Proposition 1.5 的同一 lattice model 得到。

其余有限处用未分歧标准向量；好分裂点保 Yang Corollary 2.14 的实际极化比较。
完整 finite norm 是
$$
\boxed{\prod_{v<\infty}\|\phi_v\|^2=3n_5=1-\frac1{\sqrt5}.}
\tag{21}
$$

## 4. 完整来源确是 $\sigma^5$

Hermite 多项式采用
$$
\sum_{m\ge0}H_m(X)\frac{T^m}{m!}
 =e^{XT-T^2/(8\pi)}.
$$
(13)、(17)、(19) 的共同有理支撑是 $x=n/30$，$n$ 奇。
由于 $\chi_{-2}(15)=-1$、$6^{-1}\equiv1\bmod5$，原系数恰为
$$
a_n=\chi_{-2}(n)(v_5)_{n\bmod5},\qquad
b_m=\sum_{n\in\mathbf Z}a_n
 H_m\!\left(\frac{\sqrt{\kappa_\infty}}{30}n\right)
 e^{-\pi\sqrt3 n^2/120}.
\tag{22}
$$
偶数 $n$ 的 $a_n$ 为零。这是实际全 Schwartz 求和，不另作有限字符猜测。

置 $\tau_0=\delta/3$ 和
$$
F(Z)=\sum_n a_n e^{\pi i\tau_0 n^2/40+\pi inZ},
\qquad h=\frac{\sqrt{15\sqrt3/2}}{30\pi i}.
$$
则
$$
\mathcal B(T):=\sum_{m\ge0}b_mT^m/m!
 =e^{-T^2/(8\pi)}F(hT).
$$
准确有限关系为
$$
a_{-n}=-a_n,\quad a_{n+20}=-a_n,\quad
a_{n+10}=(-1)^{(n-1)/2}a_n\quad(n\ \text{奇}).
$$
逐项换元给
$$
F(Z+1)=-F(Z),\qquad
F(Z+s_0)=-e^{-5\pi i s_0-10\pi iZ}F(Z).
\tag{23}
$$
所以 $e^{5\sqrt3\pi Z^2}F(Z)$ 是 $\mathbf Z+s_0\mathbf Z$ 上的标准
odd $\mathcal S_5$，没有剩余 flat twist。并且
$$
5\sqrt3\pi h^2=-\frac1{8\pi}.
\tag{24}
$$

型的核对使用同一个基角色 $\vartheta$ 的 Weil 表示。相对本篇的 $\chi_m$ splitting，
二、五处的 $\omega$ 矩阵各乘 $\omega^2$，三处不变。因此 finite 向量的
基表示特征为 $\omega$。无穷第 $m$ Hermite 特征为 $\omega^m$，
global rational $\omega$ 不变性给 $m\equiv2\bmod3$。
(22) 的奇性进一步给 $m\equiv5\bmod6$。

完整空间
$$
\mathcal S_5=\sigma_0^5
 \operatorname{span}\{1,x_\wp,x_\wp^2,y_\wp,x_\wp y_\wp\}
$$
的五个型分别为 $5,3,1,2,0$；型五仅一维。
$a_5=-n_5\ne0$ 证明 Fourier 级数不恒零。由全线丛与全型，而非有限拟合，得到
$$
\boxed{\mathcal B(T)=C_5\sigma_0(\Omega_0hT)^5,\qquad
C_5=\frac{b_5}{5!(\Omega_0h)^5}\in i\mathbf R^\times.}
\tag{25}
$$

## 5. 全权 Yang 常数与两种周期

(9) 的所有坏局部数据对 $m\equiv5\bmod6$ 固定。
原向量范数为
$$
\mathcal N_m=
 \frac{3n_5}{\sqrt{15\sqrt3}}\frac{m!}{(4\pi)^m}.
\tag{26}
$$
Yang 1997 Theorem 1.11 中 $S_1=\{5\}$、$S_2=\varnothing$，
$c(0)=(1+5^{-1})^{-1}=5/6$。二处未分歧，不另删除二 Euler 因子；
三处是分歧点，不另添 $c(0)$ 因子。
同 R302 的全局 Haar 和 $\mu_6$ 规范给
$$
L(\Phi_m,m+1)=
 \frac{2}{6c(0)}\frac{\pi}{3\sqrt3}\frac{b_m^2}{\mathcal N_m}
 =C_{\rm Y}\frac{(4\pi)^m}{m!}b_m^2,
$$
$$
\boxed{C_{\rm Y}=\frac{2\pi\sqrt{15\sqrt3}}
 {15\sqrt3(1-1/\sqrt5)}>0.}
\tag{27}
$$
令
$$
\kappa_5=-\frac{C_{\rm Y}C_5^2}{\Omega_0}>0.
$$
因 $(2\pi/\sqrt3)\,4\pi h^2=-1/15$，而合法 $m$ 都为奇数，(25)–(27) 给
$$
\frac{(2\pi/\sqrt3)^mL(\Phi_m,m+1)}
 {m!\Omega_0^{2m+1}}
 =\kappa_5\,15^{-m}\bigl([z^m]\sigma_0^5\bigr)^2.
\tag{28}
$$
再由 $s_0^2=-\omega^2/3$、$s_0^{-2m}=-\omega^2\,3^m$，
$$
\boxed{c_5=-\omega^2\kappa_5/s_0}
\tag{29}
$$
准确得到 (4)。若 $\mathscr E_{5,5}$ 表示 (4) 左边的首权，
则 $c_5=5^5\mathscr E_{5,5}$；经典 CM 临界值代数性说明它是固定非零代数数。
所有尺度、范数和坏点因子已包含在 (25)–(29) 中。

## 6. 同一普通测度与完整 Katz 插值

$\sigma_0(\Omega_{p,0}\log(1+Z))^5$ 是原整 Amice 级数，故定义有界测度 $\nu_{5,0}$。
写 $a_m=[z^m]\sigma_0^5$，则
$$
M_m=\int_{\mathbf Z_p}x^m\,d\nu_{5,0}(x)
 =\Omega_{p,0}^m m!a_m.
\tag{30}
$$
正权上取同一 norm-weight-one 角色
$$
\nu_m=\chi\psi_0^{m+1}\bar\psi_0^{-m},\qquad m\equiv5\bmod6.
\tag{31}
$$
它的准确导子也是 $5\delta$，且 $\nu_m\nu_m^c=\mathrm N$。
R540 所用原 Katz 晶格周期公式、或 BDP Theorem 3.1 / Proposition 3.5 给
$$
\mathcal L_{p,5\delta}^{\rm prim}(\nu_m)
 =\Omega_{p,0}^{2m+1}m!\,
 \frac{(2\pi/\sqrt3)^m L(\Phi_m,m+1)}{\varpi_0^{2m+1}}
 \left(1-\chi(\mathfrak p)
 \frac{\pi_0^m}{\bar\pi_0^{m+1}}\right)^2.
\tag{32}
$$
两个普通 Euler 因子分别是
$1-\nu_m(\mathfrak p)/p$ 和 $1-\nu_m^{-1}(\bar{\mathfrak p})$，准确相等。
三、五处原角色分歧，primitive 公式没有额外删除；二处是好未分歧点。
若采用 Coleman 的辅助平滑，可取 $(2)$：$\nu_m((2))=-2$，
$\mathrm N(2)-\nu_m((2))=6$，在本篇素数为单位。

将 (4)、(30) 代入，得到
$$
\mathcal L_{p,5\delta}^{\rm prim}(\nu_m)
 =c_5\Omega_{p,0}5^{-m}
 \left(1-\chi(\mathfrak p)
 \frac{\pi_0^m}{\bar\pi_0^{m+1}}\right)^2 M_m^2.
\tag{33}
$$
取 $m_r=m_0+(p-1)p^r$，则实趋正无穷、$p$ 进趋 $m_0$，保持模六及 tame 型。
非单位部分的 $m_r$ 矩和 Euler 减一都趋零，故 (33) 的极限准确成为单位 Mellin 平方。
全部周期的变化幂已包含于 $M_m$ 中，不对任意 $\mathbf C_p$ 单位作未定义的变指数幂。

特别 $m_0=-1$，(31) 的真实负点是
$$
\boxed{\nu_{-1}=\chi\bar\psi_0=\overline{\psi_A},\qquad
\mathcal L_{p,5\delta}^{\rm prim}(\overline{\psi_A})
 =5c_5\Omega_{p,0}
 \left(\int_{\mathbf Z_p^\times}x^{-1}\,d\nu_{5,0}\right)^2.}
\tag{34}
$$
更一般，令 $d=p-1$，
$J(u)=\int x^{-1}\langle x\rangle^{du}d\nu_{5,0}$，
则同一真实分支是 $5c_5\Omega_{p,0}\langle5\rangle^{-du}J(u)^2$。

这也确定原完整 ordinary core，且没有循环假设。R300 的真实迹保型五的一维空间；
先由测度整性和首矩 $5!\Omega_{p,0}^5$ 知其标量整，再在 $m=5$ 比较 (33)
和刚证明的单位 Mellin 平方，另一可能符号由
$2-(c+\chi(\mathfrak p))\pi_0^5/\bar\pi_0^6$ 为单位排除。因此
$$
\boxed{\nu_{5,0}|_{p\mathbf Z_p}
 =\frac{\chi(\mathfrak p)}{\bar\pi_0}
 [p/\bar\pi_0^2]_*\,\nu_{5,0}.}
\tag{35}
$$
在本题当前 $\pi_0\equiv2\bmod5$ 的 ray 上，$\chi(\mathfrak p)=1$。
由 R410 的 $\lambda=-1/\bar\pi_0$，R653 的未定 odd-five 标量由此准确定为
$\chi_{65}=-1$，即 (35) 的外部核心为 $\beta=-\lambda$。

回到原 $b=17$：
$$
\sigma_{17}(z)^5=\theta^{-5}\sigma_0(\theta z)^5,\quad
\Omega_{p,0}=\theta\Omega_p,\quad
\nu_{5,0}=\theta^5\nu_{\Sigma_{5,17}}.
\tag{36}
$$
这是同一 $\mathbf Z_p$ 变量上的来源等式，没有对测试变量乘 $\theta$。
(34)、(36) 给 (5) 的完整系数 $5c_5\theta^{11}\Omega_p$。

## 7. 固定曲线身份与解析秩一的自含证明

### 7.1 完整导子识别，不以少数 Frobenius 猜角色

在 $A:y^2+y=x^3+1$ 上，$c_4=0,c_6=-1080,\Delta=-675$。
二处好约化。三处将奇点平移到原点，得到
$[a_1,a_2,a_3,a_4,a_6]=[0,3,3,3,0]$；
Tate 判据给 type III，$v_3(\Delta)=3$、导子指数二。
五处平移后为 $[0,0,5,0,-5]$，type II，导子指数二。
故原导子为 $225$，CM Hecke 导子准确为 $5\delta$。

所有取值于 $K$、型 $(1,0)$、该导子的角色可写成
$$
\psi((a))=\frac{a}{\operatorname{sgn}_\delta(a)[a]_5^k}.
\tag{37}
$$
有限值属于 $\mu_6$，所以 $4\mid k$；全 $\mu_6$ 单位兼容又迫 $k\equiv4\bmod6$。
因此完整候选只有 $k=4,16\bmod24$。本篇
$\chi^{-1}\psi_0$ 正是 $k=4$，二处字符已经完全取消。

取实际 primary $\pi_0=-1+2\omega$、$\mathrm N\pi_0=7$。
(2) 给 $\chi(\pi_0)=-\omega$，从而
$$
(\chi^{-1}\psi_0)(\mathfrak p_7)=-3-\omega,\qquad a_7=-5.
$$
另一个完整候选给 $a_7=+5$。直接计数 $A(\mathbf F_7)$ 恰有十三点，
准确选择 $k=4$。这是在穷尽全部有限角色后选择二者之一，
不从有限 prime 样本猜一个无限角色。于是 (3) 得证。
$[x:y]\mapsto[4x:8y+4]$ 给所写短方程，微分满足
$\omega_{\rm short}=\omega_{\rm min}/2$。

$\chi^6=1$ 还给
$\Phi_m=\psi_A^{2m+1}$ 对每个 $m\equiv5\bmod6$ 成立。
在负点却必须用 (34) 的共轭角色，不是把正权五直接当作 rank-one 中央值。

### 7.2 真根数与一个严格的 $L'$ 下界

$\psi_A\mathrm N^{-1/2}$ 的二、三、五处单位数据分别为
$1,\operatorname{sgn}_\delta,[u]_5^4$，
uniformizer 分别为 $-1,-i,-1$。
在同一 $\psi_K/2$ 规范，epsilon 分别为 $-1,-i,+1$；
三处的平方 uniformizer 与 (9) 相同，五处逆角色的 Gauss 和仍为 $-5$。
无穷角权一的 epsilon 为 $i$。因此完整 root number 是 $-1$。

令 $a_n(A)$ 是原权二新形式的系数，$c=2\pi/15$，
$E_1(x)=\int_x^\infty e^{-t}dt/t$。权二 functional equation 的积分给
$$
L'(A,1)=2\sum_{n\ge1}\frac{a_n(A)}n E_1(cn).
\tag{38}
$$
这里 $a_1=1,a_2=a_3=0$；Hasse 与乘法关系给
$|a_n|\le d(n)\sqrt n\le2n$。使用
$$
0.4188<c<0.419,\quad e^{-c}<0.658,\quad
\gamma_{\rm Euler}<0.578,\quad-\log(0.419)>0.869,
$$
以及 $E_1(x)>-\gamma_{\rm Euler}-\log x+x-x^2/4$，首项满足
$$
2E_1(c)>\frac{2663639}{2000000}.
$$
全部 $n\ge4$ 的尾绝对值至多
$$
4\sum_{n\ge4}\frac{e^{-cn}}{cn}
 \le\frac{0.658^4}{0.4188(1-0.658)}
 =\frac{11716114081}{8951850000}.
$$
故
$$
\boxed{L'(A,1)>
 \frac{8245372403}{358074000000}>\frac1{50}>0.}
\tag{39}
$$
所用对数界可由
$\log x=2\sum_{j\ge0}((x-1)/(x+1))^{2j+1}/(2j+1)$ 的正项下界得到；
$\gamma_{\rm Euler}$ 的界用 $H_{10}-\log10-1/20+1/1200$。
证书准确核了这些有理界。因此解析秩恰为一，无需浮点 $L'$ 或数据库判零。
LMFDB 的原记录 225.c2 可作独立来源对照：最小模型、导子和点 $(1,1)$ 全部一致。

## 8. 真正 rank-one 非零输入及 cyclotomic 区分

BDP 2012 Theorem 1 明确陈述 Rubin 1992 的结论：若一个 CM 椭圆曲线的
解析秩恰为一，$p$ 分裂且好约化，则存在无限阶的 $P_p\in A(\mathbf Q)$，使
$$
\mathcal L_{p,5\delta}^{\rm prim}(\overline{\psi_A})
 =\kappa_p\,\Omega_{p,A}^{-1}
       \log_{\omega_A}(P_p)^2,\qquad \kappa_p\in K^\times.
\tag{40}
$$
这里保留该定理的 $K^\times$ 歧义，不声称 $\kappa_p$ 与 $p$ 无关或处处为单位。
BDP Theorem 3.1 的 primitive Katz 插值正是 (32)；
其两周期同步变更不改变 Katz 函数。

具体地，令 $\rho=80^{1/6}$，选 $\omega_A=dx/(2y+1)$。
与本篇 CM 生成周期同步，可取
$$
\varpi_A=\frac{2\varpi_0}{\rho},\qquad
\Omega_{p,A}=\frac{2\Omega_{p,0}}{\rho}.
\tag{41}
$$
二者同乘 $2/\rho$，所以 (40) 与 (34) 使用同一个原 $p$ 地点、CM type 和 Katz 规范。

无限阶有理点在 $A(\mathbf Q_p)$ 的 formal logarithm 非零：
乘一个非零整数使其落在足够小的形式群球，在该球 logarithm 单射；
若 log 为零，则该整数倍为原点，反而迫原点为 torsion。
因此 (39)–(41) 给 (5) 的非零。

这里使用的是型 $(0,1)$ 的共轭 Katz **值**。Rubin 原证明通过
cyclotomic height/elliptic units 与 Heegner 点比较；BDP 的证明直接以
Heegner 点的 $p$-adic Gross–Zagier 公式得到它。
本篇没有把 norm-weight-one 家族的方向认作 cyclotomic，
也没有借一个未经证明的 rank-two regulator 非退化性。
裸复共轭一般不保持普通插值域；这里的跨域正是 (40) 的实质定理。

## 9. 对原任务的准确接口

R653 的 $\Sigma_5$ 负一项如今是一个已证明非零的固定原算术值。
在其原四个 $K$ 分离中，系数 $6b$、其它四输入、原门和所有 $W$ 失败支仍须全部保留。
同一空间的 $D_5=-x_\wp y_\wp\sigma^5$ 的 principal-log 行、
$Z_5=x_\wp^2\sigma^5$ 的正一次移权 log 行也不能由 (6) 赋值。
本篇不宣称这些行相消或不相消，更不宣称已经达到固定 rank-two 曲线的无穷 $p$ 完成标准。

## 10. 来源与证书

- R302：基 $E_0$ 角色、实际 Haar/周期和 Yang 全权规范。
- R540：同一 ordinary 原 Amice、有限导子 Katz 插值与无循环密集正权极限。
- R370、R439、R513、R551：原 odd-five core/半特征；本文用完整角色确定其当前 ray 的剩余符号。
- R653：本篇负一矩出现的确定五输入来源与完整未删补域。
- Tonghai Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math. 485 (1997), Theorem 1.11：
  [作者原文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
- Tonghai Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*,
  Compositio Math. 117 (1999), §1、Appendix (A1)–(A3)：
  [作者原文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)。
- Massimo Bertolini, Henri Darmon, Kartik Prasanna, *p-adic Rankin L-series and rational points
  on CM elliptic curves*, Pacific J. Math. 260 (2012), 261–307,
  Theorem 1、Theorem 3.1、Proposition 3.5：
  [已发表作者 PDF](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf)，
  DOI [10.2140/pjm.2012.260.261](https://doi.org/10.2140/pjm.2012.260.261)。
- [LMFDB 225.c2 原记录](https://www.lmfdb.org/EllipticCurve/Q/225/c/2)：
  仅作模型/导子/点的独立对照；本文的角色选择和 (39) 不以数值判零为前提。

脚本只用整数、既约有理数、$\mathbf Q(\zeta_{64})$ 与 $\mathbf Q(\zeta_{15})$ 的准确商环。
共 5468 项检查包括：二处全部输出支撑、$g_*$ 相位、五处完整矩阵/范数/Gauss 和、
七十二有限剩余的全部乘法与共轭、全 Fourier 周期、两导子候选及严格解析尾界。
