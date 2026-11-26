# R271 附录：任意新增强位的完整最小源与绝对物理孔权

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下绝对加权完整源界、同源比较及强极限已证明。**
本稿一次保留任意多个新增真实硬核位，把完整有限 Gram 的原最小者运输到原物理孔权中。
全过程仍使用未加权的原正交投影与完整 inverse；没有分别求一串不同来源后把它们相加。

在原模型中取 $y=m+2^m$、辅助方差 $s\ge2^{24}/y$，则对任意
$x\ge y$ 和任意完整有限高度 $J\ge0$，原
$a_x=H_{C_x,J}(s)^{-1}(g\otimes\Omega_{[y,x)})$ 满足
$$
 \|32^{\mathcal N_{[y,x)}}a_x\|\le\frac{16}{15}\|g\|.
$$
其整个有限 Fock 最小列有同一新增强孔界。
新增强孔加辅助孔的总权只多付基头幂零阶数的 $32^{h_y-1}$，常数不含 $x-y$。

这是大辅助方差下完整空间的原源定理。
本稿不将 $s\ge2^{24}/y$ 改称实际 $S_x$，也不把完整 inverse
换成未知 $F_0$ 上的压缩 inverse。

## 1. 同一完整有限列

令 $C$ 为 Hilbert 头空间 $\mathcal H_0$ 上的有界算子，$C^h=0$，$h\ge1$。
令 $\mathcal B$ 为任意有限个真实 Boolean 位的完整物理空间，并置
$$
 D=\sum_{i\in I}b_iE_i,\qquad b_i>0.
$$
$C$ 与 $D$ 作用于不同张量因子。新增位数记为 $L=|I|$，
所以 $D^{L+1}=0$、$(C+D)^{h+L}=0$。
所有旧头 carry 仍在原 $C$ 内，没有使用它的 Jordan 相似。

取 $s>0$、任意整数 $J\ge0$。在一个标准辅助 Fock 模式上，定义
$$
 \mathcal R_{X,J}(s)v
 =\sum_{j=0}^{J}\frac{(-X)^jv}{\sqrt{j!s^j}}\otimes e_j,
 \quad
 H_{X,J}(s)=\sum_{j=0}^{J}\frac{(X^*)^jX^j}{j!s^j},
 \quad X=C,C+D.
 \tag{1.1}
$$
旧 $C$ 在 $\mathcal B$ 上按恒等延拓。
两列的第零分量都是恒等，因此它们有闭像且 $H_{X,J}\succeq I$。
记这两个完整列空间为 $\mathscr E_0,\mathscr E_1$。
旧空间准确为旧头列空间张量整个 $\mathcal B$，并支撑辅助次数
$$
 0\le j\le\min(J,h-1).
 \tag{1.2}
$$

固定原同一个 forcing
$$
 f=g\otimes\Omega_I\otimes e_0,
 \qquad g\in\mathcal H_0.
 \tag{1.3}
$$
令 $k_\nu=P_{\mathscr E_\nu}f$。其第零辅助分量分别就是
$H_{C,J}^{-1}(g\otimes\Omega_I)$ 与
$H_{C+D,J}^{-1}(g\otimes\Omega_I)$，没有删任何新增位源。

若 $J\ge h+L-1$，$\mathscr E_1$ 就是闭算子
$C+D+\sqrt s\,a$ 的整个核；$\mathscr E_0$ 同样是
$C+\sqrt s\,a$ 的整个核。辅助 annihilation 取其标准自然域；
头算子有界，所以这两个和闭。逐层核方程与幂零性说明全部核向量都是上述有限列。
当 $J$ 较小时，只使用准确的有限列闭像，不把它冒称完整核。

## 2. 低辅助次数上的 creation 乘子界

记 $a^*e_j=\sqrt{j+1}e_{j+1}$，并令 $P_{<h}$ 为辅助次数小于 $h$ 的投影。
对任意有界系数算子 $D$，置
$$
 M=\exp(-D a^*/\sqrt s),\qquad
 \alpha=\frac{\|D\|}{\sqrt s},\qquad
 \theta_h(u)=u\sqrt h+\frac{u^2}{2}.
$$
这里只需把 $M$ 作用在辅助次数小于 $h$ 的向量上；
在本稿的有限 Boolean 模型中，$D$ 幂零，展开本来就是有限和。
证明如下统一界：
$$
 \boxed{
 \|(M-I)P_{<h}\|\le e^{\theta_h(\alpha)}-1,
 \qquad \|MP_{<h}\|\le e^{\theta_h(\alpha)}.
 }
 \tag{2.1}
$$

### 2.1 自含的标量 Fock 估计

使用 Bargmann 规范 $e_j(z)=z^j/\sqrt{j!}$，内积由
$\pi^{-1}e^{-|z|^2}\,d^2z$ 给出。
对实 $t\ge0$，定义
$$
 (W_t p)(z)=e^{tz-t^2/2}p(z-t).
$$
在高斯积分中换元直接证明 $W_t$ 酉。多项式上有
$$
 e^{t a^*}=e^{t^2/2}W_t e^{ta},\qquad
 a^*W_t=W_t(a^*+tI).
 \tag{2.2}
$$
而在次数小于 $h$ 的空间上，$\|a\|\le\sqrt{h-1}$，
$a^*$ 向整个 Fock 的范数至多 $\sqrt h$。故
$$
 \|a^*e^{ta^*}P_{<h}\|
 \le(\sqrt h+t)e^{t^2/2+t\sqrt{h-1}}
 \le(\sqrt h+t)e^{t^2/2+t\sqrt h}.
$$
对 $0\le t\le\alpha$ 积分，得到
$$
 \|(e^{\alpha a^*}-I)P_{<h}\|
 \le e^{\alpha\sqrt h+\alpha^2/2}-1.
 \tag{2.3}
$$

### 2.2 算子系数不要求正规

若 $v=\sum_{j<h}v_j\otimes e_j$，则 $(M-I)v$ 的第 $n$ 个系数范数至多
$$
 \sum_{j<\min(h,n)}
 \frac{\alpha^{n-j}}{(n-j)!}\sqrt{\frac{n!}{j!}}\,\|v_j\|.
$$
这正是标量正系数算子 $e^{\alpha a^*}-I$ 对
$\sum_{j<h}\|v_j\|e_j$ 的第 $n$ 个系数。
逐系数平方求和再用 (2.3)，证明 (2.1)。
因此没有把非正规的 $D$ 当作标量 Weyl 位移。

## 3. 任意新增位一次进入同一个完整投影

令 $P_J$ 为辅助次数 $\le J$ 的正交投影，定义
$$
 B=P_JM|_{\mathscr E_0}:\mathscr E_0\longrightarrow\mathscr H.
 \tag{3.1}
$$
因 $[C,D]=0$，Bargmann 系数的准确恒等式给
$$
 \boxed{B\mathcal R_{C,J}v=\mathcal R_{C+D,J}v.}
 \tag{3.2}
$$
只读取次数 $\le J$，所以旧列在该次数以后的截断不会留下缺项。
这证明 $B$ 将整个 $\mathscr E_0$ 双射到整个 $\mathscr E_1$：
满射来自每个头源 $v$ 的 (3.2)，单射来自第零系数仍为 $v$。
特别，满射不依赖对新核偷用旧 $h$ 次数界。

以 $i:\mathscr E_0\hookrightarrow\mathscr H$ 记自然包含，置
$$
 K=B^*B.
 \tag{3.3}
$$
后面的条件保证 $K$ 有界可逆，于是准确完整投影为
$$
 P_{\mathscr E_1}=BK^{-1}B^*.
 \tag{3.4}
$$
由于 $M$ 只增加辅助次数，其第零行恒等，故
$$
 B^*f=P_{\mathscr E_0}f=k_0.
 \tag{3.5}
$$
$k_0$ 在全部新增位上仍是真空，$Dk_0=0$，所以又有
$$
 \boxed{Bk_0=k_0,\qquad k_1=BK^{-1}k_0.}
 \tag{3.6}
$$
这两个来源恒等式同时保留；没有给新源指定一个不同的 forcing。
记旧完整源的正辅助高度能量为
$$
 \varepsilon_0=\|P_{\{\mathcal N_a\ge1\}}k_0\|^2
 =\sum_{j=1}^{J}\frac{\|C^ja_0\|^2}{j!s^j},
 \qquad a_0=H_{C,J}(s)^{-1}(g\otimes\Omega_I).
 \tag{3.7}
$$

## 4. 两向孔权及原未加权最小者

设 $0<\gamma\le1$，令
$$
 \Gamma=\gamma^{-\mathcal N_I}
$$
只计新增真实 Boolean 位。旧空间 $\mathscr E_0$ 的投影与 $\Gamma$ 交换；
记其在旧空间的限制为 $\Gamma_0$。实际删除恒等式为
$$
 \Gamma D\Gamma^{-1}=\gamma D,
 \qquad \Gamma^{-1}D\Gamma=\gamma^{-1}D.
$$
令
$$
 B_+=\Gamma B\Gamma_0^{-1},\qquad
 B_-=\Gamma^{-1}B\Gamma_0,
$$
$$
 \theta_+=\theta_h(\gamma\alpha),\qquad
 \theta_-=\theta_h(\gamma^{-1}\alpha),\qquad
 \Theta=\theta_++\theta_-.
$$
由 (2.1)，且 $P_J$ 与孔权交换，
$$
 \|B_\pm-i\|\le\delta_\pm:=e^{\theta_\pm}-1,
 \qquad \|B_\pm\|\le e^{\theta_\pm}.
 \tag{4.1}
$$
最关键的是完整原 Gram 的准确共轭：
$$
 \boxed{\Gamma_0K\Gamma_0^{-1}=B_-^*B_+.}
 \tag{4.2}
$$
因此
$$
 \|\Gamma_0K\Gamma_0^{-1}-I\|
 \le\delta_-+\delta_++\delta_-\delta_+
 =e^\Theta-1.
 \tag{4.3}
$$
若 $\Theta<\log2$，Neumann 级数给
$$
 \boxed{\|\Gamma_0K^{-1}\Gamma_0^{-1}\|
 \le\frac1{2-e^\Theta}.}
 \tag{4.4}
$$
这同时证明 $K$ 可逆以及 (3.4) 的闭范围所需下界。
也可直接由 $\|B-i\|\le e^{\theta_h(\alpha)}-1<1$ 得下界。
这里始终是原 $K^{-1}$，不是改用加权最小化之后的另一个 inverse。

$\Gamma_0k_0=k_0$，故 (3.6)、(4.4) 给绝对来源界
$$
 \boxed{\|\Gamma k_1\|
 \le\frac{e^{\theta_+}}{2-e^\Theta}\|k_0\|
 \le\frac{e^{\theta_+}}{2-e^\Theta}\|g\|.}
 \tag{4.5}
$$
还有保原同一来源的差界
$$
 \boxed{\|\Gamma(k_1-k_0)\|
 \le\frac{e^{\theta_+}(e^{\theta_-}-1)}{2-e^\Theta}\sqrt{\varepsilon_0}.}
 \tag{4.6}
$$
确实 $B_+k_0=k_0$，所以
$(I-B_-^*B_+)k_0=(i^*-B_-^*)k_0$。
此外 $B_-^*-i^*=P_{\mathscr E_0}(M_-^*P_J-I)$，其中
$M_-=\exp(-\gamma^{-1}Da^*/\sqrt s)$。
其非恒等项都含一个辅助 annihilation，因此这个有界伴随差在整个辅助真空上为零。
故
$$
 (i^*-B_-^*)k_0=(i^*-B_-^*)P_{\{\mathcal N_a\ge1\}}k_0,
 \qquad
 \|(i^*-B_-^*)k_0\|\le\delta_-\sqrt{\varepsilon_0}.
$$
再用 $k_1-k_0=B(K^{-1}-I)k_0$ 即得 (4.6)。
第零辅助分量的实际完整 inverse 列也满足 (4.5)--(4.6)。

## 5. 新增强孔与全部辅助孔一起计数

令 $\mathcal N_a$ 为辅助 Fock 占据。因为 $D$ 每次删一个新增位而 $a^*$ 增加一个辅助孔，
$$
 [M,\mathcal N_I+\mathcal N_a]=0.
 \tag{5.1}
$$
$P_J$ 也与这一总孔权交换。
令 $v=K^{-1}k_0\in\mathscr E_0$。它的辅助次数仍小于 $h$，所以
$$
 \|\gamma^{-(\mathcal N_I+\mathcal N_a)}v\|
 \le\gamma^{-(h-1)}\|\Gamma_0v\|
 \le\frac{\gamma^{-(h-1)}}{2-e^\Theta}\|k_0\|.
$$
孔权后的 $v$ 未必仍在 $\mathscr E_0$，但它仍属于辅助次数小于 $h$ 的整个空间。
因此可合法使用 (2.1)，而不把它当作核保持性：
$$
 \boxed{
 \|\gamma^{-(\mathcal N_I+\mathcal N_a)}k_1\|
 \le\frac{e^{\theta_h(\alpha)}}{2-e^\Theta}
       \gamma^{-(h-1)}\|k_0\|.
 }
 \tag{5.2}
$$
这一步没有对新核的辅助次数作 $<h$ 的错误假设。

## 6. 原连续强位上的明确选择

回到原 N 或 Y 模型。取
$$
 m\ge10,\quad d=2^m,\quad y=m+d,\quad
 C_y=A_m+D_{[m,y)},\quad h=d+y-m=2d\le2y.
$$
对任意整数 $x\ge y$，保全部新增硬位
$$
 D=D_{[y,x)},\qquad C_x=C_y+D,
 \qquad\|D\|\le\sum_{i=y}^{x-1}(i+1)^{-2}\le\frac1y.
 \tag{6.1}
$$
取
$$
 \boxed{\gamma=1/32,\qquad s\ge2^{24}/y.}
 \tag{6.2}
$$
于是
$$
 \alpha\sqrt h\le\frac{\sqrt2}{4096}<\frac1{2048},
 \qquad \alpha^2\le2^{-24}.
$$
因此
$$
 \Theta=(\gamma+\gamma^{-1})\alpha\sqrt h
       +\tfrac12(\gamma^2+\gamma^{-2})\alpha^2
 <\frac{33}{2048}+\frac{1025}{2^{25}}<\frac1{32}.
 \tag{6.3}
$$
由 $e^\Theta\le(1-\Theta)^{-1}\le32/31$，
且 $\theta_+,\theta_h(\alpha)\le\Theta$，
$$
 \frac{e^{\theta_+}}{2-e^\Theta},\quad
 \frac{e^{\theta_h(\alpha)}}{2-e^\Theta}
 \le\frac{16}{15}.
 \tag{6.4}
$$

将同一个 $g\in\mathcal H_{<y}$ 在 $[y,x)$ 补真空，令
$$
 a_x=H_{C_x,J}(s)^{-1}(g\otimes\Omega_{[y,x)}),
 \qquad k_x=\mathcal R_{C_x,J}(s)a_x.
$$
对每一个 $J\ge0$，得到
$$
 \boxed{
 \|32^{\mathcal N_{[y,x)}}a_x\|,
 \quad\|32^{\mathcal N_{[y,x)}}k_x\|
 \le\frac{16}{15}\|g\|,
 }
 \tag{6.5}
$$
$$
 \boxed{
 \|32^{\mathcal N_{[y,x)}+\mathcal N_a}k_x\|
 \le\frac{16}{15}\,32^{h-1}\|g\|.
 }
 \tag{6.6}
$$
原前 $y$ 位至多有 $y$ 个物理孔，所以进一步
$$
 \boxed{
 \|32^{\mathcal N_{<x}}a_x\|
 \le\frac{16}{15}32^y\|g\|,
 \qquad
 \|32^{\mathcal N_{<x}+\mathcal N_a}k_x\|
 \le\frac{16}{15}32^{y+h-1}\|g\|.
 }
 \tag{6.7}
$$
这些是原完整未加权 inverse 所产生的实际最小列，不是另选的可行列。
费用与新增强位数 $x-y$ 无关。

例如对任何 $A_0$，(6.5) 直接给
$$
 \|P_{\{\mathcal N_{<x}\ge A_0\}}a_x\|
 \le\frac{16}{15}\,32^{y-A_0}\|g\|.
 \tag{6.8}
$$

## 7. 保原 V/K 来源的真实物理代表

令 $S_x=\sum_{i\ge x}(i+1)^{-4}$，$\omega_j=(D_x^*)^j\Omega$。
当前 $s\ge2^{24}/y$ 且 $x\ge y$，当然有 $s\ge S_x$。
定义原阻尼物理列
$$
 f_{x,s,J}=\sum_{j=0}^{J}
 \frac{(-C_x)^ja_x\otimes\omega_j}{s^j j!}.
 \tag{7.1}
$$
从辅助 Fock 到物理远尾的逐级映射为
$$
 e_j\longmapsto\frac{\omega_j}{\sqrt{j!s^j}}.
$$
它的第 $j$ 层范数平方为
$j!e_j((b_i^2)_{i\ge x})/s^j\le(S_x/s)^j\le1$。
不同孔层正交，并且该映射保孔数，所以它也在相同指数孔权下收缩。
(6.7) 因此给真正物理的绝对界
$$
 \boxed{\|32^{\mathcal N_{\rm all}}f_{x,s,J}\|
 \le\frac{16}{15}32^{y+h-1}\|g\|.}
 \tag{7.2}
$$

使用[原放大方差同源稿](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)
§4 的准确逐列身份。若 $R=x-m$、$Q\ge R+J$，则
$$
 P_{V_Q}f_{x,s,J}=P_{V_Q}i_0g,
 \qquad P_{K_Q}f_{x,s,J}=P_{K_Q}i_0g.
 \tag{7.3}
$$
所以原同一个 $u_g=(P_{V_Q}-P_{K_Q})i_0g$ 及由它产生的内部顶部、两端 partial 全部保持。
其余 joined/full 投影仍必须满足自己的逐列身份与原内部 cut 条件。
本稿没有将 $P_{V_Q}$ 或 $P_{K_Q}$ 视作物理孔权下的收缩。

若需要 c26 母提升，另取例如
$x+1\le e^{26d^3}/4$、$J\le d+x-m-1$。此时
$R+J<3(x+1)<e^{26d^3}$，可同时选原合法整数 $Q$。
(6.5)--(7.2) 本身不要求这个上限；上限只在原母提升处使用。

## 8. 不同强头的原来源比较与任意长度极限

更一般地令 $s=K/y$，$K\ge2^{24}$。§4 的差界仍适用。
在 (6.3) 的范围内，
$$
 \frac{e^{\theta_+}(e^{\theta_-}-1)}{2-e^\Theta}
 \le2\theta_-
 \le64\sqrt{\frac2K}+\frac{1024}{Ky}.
 \tag{8.1}
$$
例如第一步使用 (6.4) 及
$e^{\theta_-}-1\le(32/31)\theta_-$，所得系数小于 $2$。

令 $k_y$ 是同高度 $J$、同方差 $s$、同 forcing $g$ 的旧头完整列，并在新增位补真空。
记其正辅助高度能量为 $\varepsilon_y$，如 (3.7)。
则对任意 $x\ge y$
$$
 \boxed{
 \|32^{\mathcal N_{[y,x)}}(k_x-k_y)\|
 \le\left(64\sqrt{2/K}+\frac{1024}{Ky}\right)\sqrt{\varepsilon_y}.
 }
 \tag{8.2}
$$
其第零辅助分量 $a_x-a_y$ 也满足同一界。
这比较的是实际两个完整最小者，不是固定头算子的形式反馈树。

取 $m\to\infty$、$y_m=m+2^m$，并选择
$$
 K_m\ge2^{24},\qquad K_m/y_m\to0,\qquad
 s_m=K_m/y_m.
$$
特别允许确定的常数选择 $K_m=2^{24}$。
令 $x_m\ge y_m$ 任意，$J_m\ge1$ 任意；超过相应幂零阶数的 Gram 项按零处理。
旧头 $C_{y_m}$ 处于原已付实际方差窗口，且
$s_m\ge S_{y_m}$、$s_m\to0$。
因此[实际方差完整源极限](R271-appendix-exponential-strong-prefix-actual-variance-source-limit.md)
给同一个固定有限物理 $f$ 的旧完整列强趋 $P_Mf\otimes e_0$。
若 $J_m>h-1$，旧列和 Gram 已稳定在 $h-1$，所以同一结论仍成立。
同时 $\varepsilon_{y_m}\to0$，不要求其速率。
(8.2) 的系数在全部 $K_m\ge2^{24}$ 上一致有界，因此得到
$$
 \boxed{a_{x_m}\longrightarrow P_Mf,\qquad
 k_{x_m}\longrightarrow P_Mf\otimes e_0
 \quad\text{强收敛}.
 }
 \tag{8.3}
$$
这里允许任意增长的 $x_m$；抽象完整源的证明不需要把 $x_m$ 放入母窗口。
若要把这些列用于原母提升或原固定 $Q$ 的来源，则仍逐项施加 §7 的支持与 c26 上限。
原物理列 (7.1) 也由逐级收缩与 (8.3) 强趋 $P_Mf$。

## 9. 与最高 carry 真核问题的边界

本稿在上述大辅助方差下，为实际完整未加权最小源支付新增强孔的
$\gamma=1/32$ 绝对权，并给不同强头、同 forcing 的真实比较。
关键输入是旧完整列空间在新增位上为恒等张量，故其正交投影与 $\Gamma$ 交换。

若另把头源限制到
$F_0=\lim_{t\downarrow0}\ker C_t^r$，这个张量结构尚未建立；
也没有理由令其正交投影与 $\Gamma$ 交换。
同样，$s\ge2^{24}/y$ 通常远大于实际 $S_x$。
因此本稿不声称已得该真核 Galerkin 残余
$\xi_0(S_x)$ 的绝对 $\mathcal Z_{1/32}$，不将原全部 MP 返回或其自然域费用删除。
