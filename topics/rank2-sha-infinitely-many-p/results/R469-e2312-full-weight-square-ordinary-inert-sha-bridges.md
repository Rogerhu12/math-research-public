# R469 — E2312 的全权平方、普通与惰性完整 Sha 桥

日期：2026-11-14。**状态：已证明。** 本篇把 R466 的同一条新原
degree136 来源接到固定曲线
$$
E_D:y^2=x^3+D,\qquad D=2312=8\cdot17^2.
$$
R466 的完整二、三、十七处身份及两个独立有理点是本篇的输入。
这里重新支付其真实微分尺度、固定平方常数的代数性、普通整测度、
惰性整 signed 模、全部 Euler 因子和通常 Selmer 的完整余秩。
结论给第三条合法的完整中央条件；尚未证明它在无穷多个素数非零。

## 1. 同一个有理来源与目标曲线

记 $K=\mathbf Q(\delta)$、$\delta^2=-3$、$\omega=(-1+\delta)/2$，
$s=(1-\omega)^{-1}$。在 $E_b:y^2=x^3+b$ 的微分
$dz=dx/(2y)$ 下使用 $x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、
$\sigma=z+\cdots$。定义
$$
F_b(z)=\sigma_b(z)^{136}x_b(z)^2P_{21}(x_b(z)^3;b).
\tag{1}
$$
这里 $P_{21}$ 是 R466 精确投影所给的齐次多项式；其 $b=1$ 值为
$$
\begin{split}
P_{21}(X;1)={}&(X+1)(X^2+20X-8)(7X^2-4X+16)\\
&\cdot(X^4+40X^3+2112X^2+3136X+1792)\\
&\cdot(13X^4+52X^3+1536X^2+1024X+256)\\
&\cdot(X^8+1232X^7-58688X^6-49408X^5-439040X^4\\
&\hspace{24mm}-2111488X^3-1949696X^2-851968X-32768)/91.
\end{split}
\tag{2}
$$
每个 $r$ 次因子按 $X^j\mapsto b^{r-j}X^j$ 恢复，故
$P_{21}(X;b)=\sum_{j=0}^{21}c_jb^{21-j}X^j$，
$c_j\in\mathbf Z[1/91]$、$c_{21}=1$。因而
$$
F_b(z)=z^6+O(z^{12}),\qquad
F_b(z)=b^{-1}F_1(b^{1/6}z).
\tag{3}
$$
后一式不依赖六次根的选择，因为 $F_1$ 只含六的倍数次幂。

R466 从原 $R_2(z)C_{13}(2z)$ 和 $R_2(z)C_{15}(2z)$ 得到的
是 (1) 在 $b=17$ 的来源；其全部有限角色准确为 $E_D$ 的角色，
不以三处好素数的迹拟合替代。置
$$
u=136^{1/6},\qquad \theta=D^{1/6},\qquad
\Phi_D(z)=F_D(z)=u^{-6}F_{17}(uz)
          =D^{-1}F_1(\theta z)=\sum s_mz^m.
\tag{4}
$$
这和 $E_{17}\to E_D$ 的真实同构
$(x,y)\mapsto(u^2x,u^3y)$ 相容，其微分乘子为 $u^{-1}$。
若 $F_1=\sum\alpha_mz^m$，则
$$
s_m=D^{m/6-1}\alpha_m\quad(6\mid m),\qquad s_6=\alpha_6=1.
\tag{5}
$$
R466 的三次同源 Kummer 证明给
$r=\operatorname{rank}E_D(\mathbf Q)\ge2$。
本篇不预设 $r=2$。

## 2. 原 Hermite 尺度与全部复平方

R466 给实际 Hecke 特征 $\psi_D$ 的 primitive 导子
$$
\mathfrak f=(8\delta\cdot17),
\tag{6}
$$
同一个 Hermitian 类 $\alpha=17$、真实有限 Schwartz 向量及
全部权 $6\mid m$。其十七处向量记为
$f_2=9\sqrt{17}\,\Pi_{\tau_2}(e_1-e_{-1})$，
其中 $\tau_2=g^{15}$，令 $n_2=\|f_2\|^2>0$。
这是 R466 完整有限 Weil 投影的精确范数，不是未定局部单位。
二、三处范数均为三；Yang 的完整常数为
$$
C_2=\frac{\pi\sqrt{102\sqrt3}}{51\sqrt3\,n_2},\qquad
L(\psi_D^{2m+1},m+1)
 =C_2\frac{(4\pi)^m}{m!}\,b_m^2,\quad 6\mid m.
\tag{7}
$$
此处 $b_m$ 为同一实际 Hermite 来源的指数生成系数。
R466 同时给全局根数 $+1$，以及这些权上完整有限角色、
uniformizer 值和导子不变。

取正实周期 $\Omega_D$，使目标微分的周期格为
$\Omega_D\Lambda$，$\Lambda=s\mathcal O_K$。
实际 Hermite 变量是
$$
h=\frac{\sqrt{51\sqrt3}}{408\pi i},\qquad
\mathcal B(t)=C_{\mathrm{raw},D}\,\Phi_D(\Omega_Dht)
             =\sum_{m\ge0}b_m\frac{t^m}{m!}.
\tag{8}
$$
标量 $C_{\mathrm{raw},D}\ne0$ 由同一原 theta 线确定。因 $s_6=1$，
它准确等于 $b_6/(720(\Omega_Dh)^6)$。
这里没有声称原分析标量 $C_{\mathrm{raw},D}$ 本身是代数数。

原 Gaussian 与 degree136 frame 准确相合：
$$
136\sqrt3\pi h^2=-\frac1{8\pi},\qquad
4\pi h^2=-\frac{\sqrt3}{816\pi}.
\tag{9}
$$
因此 (7)–(8) 给
$$
\frac{(2\pi/\sqrt3)^mL(\psi_D^{2m+1},m+1)}
     {m!\Omega_D^{2m+1}}
 =\kappa_D\,408^{-m}s_m^2,\qquad
\kappa_D=\frac{C_2C_{\mathrm{raw},D}^2}{\Omega_D}\ne0.
\tag{10}
$$
真实 CM 格生成周期是 $\varpi_D=s\Omega_D$。
由于 $s^{2m}=3^{-m}$ 对 $6\mid m$ 成立，准确换算为
$$
\boxed{\mathscr E_{D,m}:=
\frac{(2\pi/\sqrt3)^mL(\psi_D^{2m+1},m+1)}
     {m!\varpi_D^{2m+1}}
 =\frac{\kappa_D}{s}\,136^{-m}s_m^2.}
\tag{11}
$$
实尺度 $408^{-m}$、CM 尺度 $136^{-m}$ 和 $s^{-1}$ 同时保留。
CM 临界值代数性及 $s_6=1$ 给
$$
\kappa_D=s\,136^6\mathscr E_{D,6}
          \in\overline{\mathbf Q}^{\times}.
\tag{12}
$$
非零由 (7) 和 (8) 的 $b_6\ne0$ 得到。
所以只有固定有限多个素数能使此常数不是单位；
下面中心阶比较只使用其非零，惰性主项赋值公式保留其实际赋值。

## 3. 普通素数的原整测度与整条 Katz 平方

本篇统一取 $p>19$。先设 $p\equiv1\pmod3$。
目标曲线在 $p$ 处好普通，(2) 的分母七、十三均为单位。
R295 §2 的 Mazur–Tate 唯一性证明适用于任意 $E_b$：
CM 自同构迫二次修正常数为零，故
$\sigma_D(\log_{E_D}t)\in t\mathbf Z_p[[t]]$。
每个 $\sigma_D^{136}x_D^{2+3j}$ 的 $t$ 阶为
$132-6j\ge6$，从而
$$
\Phi_D(\Omega_{p,D}\log(1+Z))
 =\int_{\mathbf Z_p}(1+Z)^x\,d\nu_{D,p}(x)
 \in R_p[[Z]]
\tag{13}
$$
给同一个有界整测度。这里 $\Omega_{p,D}$ 是与 $\varpi_D$
相容的单位普通周期，$R_p$ 可扩大以包含固定代数常数。
全部矩准确为
$$
M_m=\Omega_{p,D}^m m!s_m.
\tag{14}
$$
定义
$$
G_{D,p}(T)=\int_{\mathbf Z_p^\times}
(1+T)^{\log_p\langle x\rangle/\log_p(1+p)}\,d\nu_{D,p}(x).
\tag{15}
$$

令 $\pi=\psi_D(\mathfrak p)$、$\bar\pi=\psi_D(\bar{\mathfrak p})$，
$v_p(\pi)=1$、$v_p(\bar\pi)=0$、$\pi\bar\pi=p$。
这里使用目标曲线的实际 Frobenius；不从同 $b=17$ theta 的 core
符号推测 $\pi$。对正的 $p-1\mid m$，同一 Katz/de Shalit 分支给
$$
\mathcal K_{D,p}(t_m)
=\frac{\kappa_D}{s}\Omega_{p,D}\,136^{-m}
 \left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2 M_m^2,
\quad t_m=(1+p)^m-1.
\tag{16}
$$
两个 Euler 因子分别为
$1-\epsilon_m(\mathfrak p)/p$ 和
$1-\epsilon_m^{-1}(\bar{\mathfrak p})$，
$\epsilon_m=\psi_D^{m+1}\bar\psi_D^{-m}$；二者都等于式中所列因子。
导子仍是 (6)，其余坏位未被额外删除。该处代数字符未分歧，
故 $p$ Gauss 因子为一。两个阶乘由 Katz 与 (11) 准确合成 (14)
的平方。

同 R397 §4，非单位输出的 $m$ 阶矩赋值至少 $m$，
Euler 误差也至少 $m$。取
$m_j=m_0+(p-1)p^j$，它实趋于无穷而 $p$-adic 趋于 $m_0$，
再用权点趋于零的解析恒等定理，得到整条身份
$$
\boxed{\mathcal K_{D,p}(T)=
\frac{\kappa_D}{s}\Omega_{p,D}
(1+T)^{-a_{136,p}}G_{D,p}(T)^2,\qquad
a_{136,p}=\frac{\log_p\langle136\rangle}{\log_p(1+p)}.}
\tag{17}
$$
它不是逐权重新选择平方根所得的身份。
反向 Artin 规范须同时反演参数，仍保持中心零阶。

与原 $b=17$ 来源使用相容普通周期
$\Omega_{p,D}=u^{-1}\Omega_{p,17}$ 时，(4) 直接给
$$
\nu_{D,p}=136^{-1}\nu_{F_{17},p},\qquad
G_{D,p}=136^{-1}G_{F_{17},p}.
\tag{18}
$$
该尺度在当前素数为单位，没有隐藏的未知斜率。

## 4. 普通完整 Selmer 比较

$K$ 类数一，目标是最大整环 CM 的有理曲线，根数为正。
新 primitive 射线类次数准确为
$$
[K(\mathfrak f):K]
=\frac{64\cdot3\cdot17^2}{6}
  \left(1-\frac14\right)\left(1-\frac13\right)
  \left(1-\frac1{17^2}\right)
=4608=2^9\,3^2.
\tag{19}
$$
分母六来自只有恒等根单位同余一；当前 $p$ 与此次数互素。
因此 R397 §5 所用 Agboola–Howard
Theorem 2.4.17(1)(b),(c) 的实际假设在新曲线上仍满足：
通常单 CM Selmer 对偶 $X(D_\infty)$ 为 torsion，
其特征理想由 (17) 的相容 Katz 分支生成。
辅助理想可取 $(5)$，实际中心 Euler 值为 $-30$，在当前位为单位。
所以 $\mathcal K_{D,p}\ne0$，且其中心阶是通常 $X$ 的特征阶。

基层通常 Selmer 向塔上不变量的限制是单射。
证明和 R397 §5.2 相同：$\pi$ 连通挠点的一阶 tame inertia 像
阶为 $p-1$，pro-$p$ 塔不能杀掉它；故塔上无非零 $\pi$-初级挠点，
inflation–restriction 的限制核为零。所有地方的通常 Kummer
局部条件在限制下保留。
取对偶并有理化，得到
$$
\operatorname{corank}_{\mathbf Z_p}
\operatorname{Sel}_{\pi^\infty}(E_D/K)
\le\operatorname{ord}_0\mathcal K_{D,p}.
\tag{20}
$$

有理三次同源 $E_D\to E_{-27D}=E_D^{(-3)}$ 与对偶复合为 $[3]$。
当前 $p\ne2,3$，二次限制/核心限制、两特征投影及该三同源都
保持整个通常 $p^\infty$-Selmer 群的余秩。
两个 CM 分量由复共轭交换，所以若
$r_p=\operatorname{corank}_{\mathbf Z_p}\Sha(E_D/\mathbf Q)[p^\infty]$，
准确有
$$
\operatorname{corank}_{\mathbf Z_p}
\operatorname{Sel}_{\pi^\infty}(E_D/K)=r+r_p.
\tag{21}
$$
没有删除任何 Sha 自由方向。由 (17)、(20)、(21)，
$$
\boxed{G_{D,p}\ne0,\quad G_{D,p}(0)=0,\qquad
r+r_p\le2\operatorname{ord}_0G_{D,p}.}
\tag{22}
$$
特别
$$
\boxed{G'_{D,p}(0)\ne0\ \Longrightarrow\
r=2\text{ 且 }\Sha(E_D/\mathbf Q)[p^\infty]\text{ 有限}.}
\tag{23}
$$
余秩零推出有限，使用通常 Selmer 及其 Sha 商的有限余生成性。
这不是对有限初级群是否平凡的断言。

## 5. 惰性素数的同一完整解析半因子

现在设 $p>19$、$p\equiv5\pmod6$，令 $d=p+1$、
$\mathcal O=\mathbf Z_{p^2}$。使用底曲线 $E_1$ 上的 (1)–(2)，
记 $F_1=\sum\alpha_mz^m$，参考
$B=x\sigma^2=\sum\beta_mz^m$。置
$$
f=\log(\sigma/z),\quad c=[z^d]f,\quad
G_{136}=F_1e^{-136cz^d},\quad G_0=Be^{-2cz^d},
$$
$$
J_{136,p}(v)=\sum_{h\ge0}a_h(v)_h,\quad
a_h=[z^{dh}]G_{136}(136c)^{-h},
\qquad
J_{0,p}(v)=\sum_{h\ge0}[z^{dh}]G_0(2c)^{-h}(v)_h.
\tag{24}
$$
$R301$ 的底曲线形式对数、真实首分母和严格圆盘估计给
$$
v_p(c)=-1,\quad
pc\equiv-(-1)^{d/6}4^{-d/6}\binom{d/3}{d/6}\pmod p.
\tag{25}
$$
右侧为单位。这里 $c$ 完全固定，不能另选一个 Gaussian。

令 $W=z^2x$，$R=p^{-1/(2p)}$。同一个完整余项准确为
$$
G_{136}(z)=
\sum_{j=0}^{21}c_jz^{132-6j}W(z)^{2+3j}
          \exp\{136(f-cz^d)\}.
\tag{26}
$$
因为 $c_j\in\mathbf Z[1/91]$、$132-6j\ge6$，
R301 的 $\|W\|_R=1$ 和严格指数收敛界给
$\|G_{136}\|_R\le R^6$；参考余项范数至多一、质量一。
所以
$$
\boxed{v_p(a_h)\ge
\left\lceil\frac{h(p-1)+6}{2p}\right\rceil\ (h\ge1),\qquad
J_{136,p}\in pv\,\mathbf Z_p\langle v\rangle,\quad
J_{0,p}\in1+p\mathbf Z_p\langle v\rangle.}
\tag{27}
$$
二者都在 $|v|_p<p^{(p-1)/(2p)}$ 上解析。
对每个非负整数 $k$，真正有限卷积给
$$
\boxed{J_{136,p}(k)=k!(136c)^{-k}\alpha_{dk},\qquad
J_{0,p}(k)=k!(2c)^{-k}\beta_{dk}.}
\tag{28}
$$
因此所有 $\beta_{dk}$ 非零，赋值为 $-k-v_p(k!)$。
物理曲线上的 $c_{D,p}=\theta^d c$ 与 (4) 同时换算，在每个 Newton
系数上精确消去 $\theta$，得到
$$
J_{\Phi_D,p}=D^{-1}J_{136,p}.
\tag{29}
$$
该常数为当前单位；不能只换 $s_m$ 而不换 Gaussian。

## 6. 惰性完整 signed 格与全部周期比较

因 $6\mid p+1$，$\mathbf F_{p^2}^{\times6}$ 包含
$\mathbf F_p^\times$，故 Hensel 提升给
$\theta=D^{1/6}\in\mathcal O^\times$。
实际整同构
$$
E_1\longrightarrow E_D,\quad
(X,Y)\longmapsto(\theta^2X,\theta^3Y),\qquad
F_\theta^*\omega_D=\theta^{-1}\omega_1
\tag{30}
$$
保持光滑整模型、形式群及完整 CM Tate 格，逆映射也整。
其原始复周期满足 $\varpi_D=\varpi_1/\theta$。
两条 Hecke 角色的比为六次有限角色；当 $d\mid m$ 时，
$$
(\psi_D/\bar\psi_D)^m=(\psi_1/\bar\psi_1)^m
\tag{31}
$$
是同一反圆分塔的同一分支。其 $p$ 惯性 tame 指数
$(1-p)m$ 被 $p+1\mid m$ 消掉，其余有限六次角色由 $6\mid m$
消掉。取原始反圆分参数 $q\in1+p\mathcal O$，
$v_p(q-1)=1$，则 $x_{dk}=q^{dk}-1$ 满足
$v_p(x_{dk})=1+v_p(k)$。

R303 §3、R402 §4 的完整局部 Rubin 定理给
$M_j=M_j^+\oplus M_j^-$、$M_j^\pm\simeq\Lambda=\mathcal O[[T]]$。
式 (30) 给两个符号格的整同构，与局部指数、限制和
corestriction 相容。两曲线根数均正，原标准椭圆单位局部类
$\xi_j$ 均在正号模。参考的实际值为
$$
L(E_1,1)/\varpi_1=(1-\omega)/6\in\mathcal O^\times.
\tag{32}
$$
因此 BKO24 Corollary 4.11(i) 的证明使 $\xi_1$ 成为完整正号格
的整基，唯一有
$$
\boxed{F_\theta^*\xi_D=\mathcal A_{D,p}(T)\xi_1,\qquad
\mathcal A_{D,p}\in\Lambda,\quad\mathcal A_{D,p}\ne0.}
\tag{33}
$$
非零及特征理想来自 BKO21；不是从数值拟合得到。
新导子为 (6)，有限下降次数 (19) 与当前 $p$ 互素。

对同一个原标准类，R303 §4 的两条混合权特化路径都得到
$T_j^{-(2m+1)}(1+m)$。在原始 CM 基和共同 Tate 基下，两路径
同为 $\mathbf u_j\otimes b_j^{\otimes(2m+1)}\otimes\zeta^{\otimes m}$。
norm、twist、特化与局部化交换；因此可使用该节已经证明的
完整期比较，而非新增未证的高权 motivic 相容性。

为明确新输入，辅助惰性素数取
$\ell\equiv1\pmod p$、$\ell\nmid6\cdot17p$；
两曲线在 $(\ell)$ 的 Hecke 值均为 $-\ell$，
辅助算子两边同为 $\ell^2+\ell^{-1}\equiv2\pmod p$。
微分张量 $\theta^{-(2m+1)}$、导子幂、六次扭转次数和
射线类次数 4608 全是当前单位。
共同临界 Tate 因子 $(i\sqrt3)^m m!$ 中的阶乘在取比后才抵消。
两条曲线的惰性 $p$ Euler 因子也都准确为
$$
1-\frac{(-p)^{2m+1}}{(p^2)^{m+1}}=1+\frac1p,
\tag{34}
$$
其赋值为 $-1$，同样只能在取比后抵消。
参考始终保留其十七处的 primitive Euler 因子；
没有为共同层数把它额外删除。两条曲线各自的导子及
uniformizer 值在 $6\mid m$ 上不变。
这些正是 R303 比较中需要重新支付的全部改动，遂有
$$
v_p\mathcal A_{D,p}(x_m)
=v_p\mathscr E_{D,m}-v_p\mathscr E_{1,m}.
\tag{35}
$$

参考的真实全权平方为
$\mathscr E_{1,m}=(6s)^{-1}2^{-m}\beta_m^2$。
结合 (5)、(11)，先保留完整代数比
$$
\frac{\mathscr E_{D,m}}{\mathscr E_{1,m}}
=6\kappa_DD^{-2}\theta^{2m}68^{-m}
  \left(\frac{\alpha_m}{\beta_m}\right)^2.
\tag{36}
$$
对 $m=dk$，(28) 准确给
$\alpha_{dk}/\beta_{dk}=68^kJ_{136,p}(k)/J_{0,p}(k)$。
所有显示的 $D,\theta,68$ 均为单位，故
$$
\boxed{v_p\mathcal A_{D,p}(x_{dk})
=v_p(\kappa_D)+2v_pJ_{136,p}(k).}
\tag{37}
$$
固定常数的赋值没有未经证明地设为零。

若 $J_{136,p}$ 恒零，(37) 迫非零 $\mathcal A_{D,p}$ 在趋零的
$x_{dp^n}$ 上有无穷零，矛盾。设
$e=\operatorname{ord}_0J_{136,p}$、$j_e=[v^e]J_{136,p}$。
对充分大 $n$ 比较两边首项赋值中 $n$ 的系数与常数，得到
$$
\boxed{\operatorname{ord}_0\mathcal A_{D,p}=2e,\qquad
v_p([T^{2e}]\mathcal A_{D,p})
=v_p(\kappa_D)+2v_p(j_e)-2e.}
\tag{38}
$$

## 7. 惰性通常 Selmer 与第三条合法中央条件

BKO21 Theorems 6.1–6.2 用于根数正的 CM 曲线，基层比较是完整
通常 Selmer；平凡角色属于正号分支，不附加相反符号的一维项。
因此
$$
\operatorname{corank}_{\mathcal O}
\operatorname{Sel}_{p^\infty}(E_D/K)
\le\operatorname{ord}_0\mathcal A_{D,p}.
\tag{39}
$$
和 §4 一样，$E_D^{(-3)}$ 与 $E_D$ 的有理三同源、二次特征
分解及完整 Kummer 正合列给左侧准确为 $r+r_p$。
由 (38) 得
$$
\boxed{J_{136,p}\ne0,\qquad
r+r_p\le2\operatorname{ord}_0J_{136,p},\qquad
J'_{136,p}(0)\ne0\Longrightarrow
r=2,\ \Sha(E_D/\mathbf Q)[p^\infty]\text{ 有限}.}
\tag{40}
$$
这是同一固定曲线的整个初级群，未仅控制一个局部或严格 Selmer
商，也没有 p-adic 高度非退化前提。

新合法条件与原 S34、T72 一起放入固定有限池时，须在同一无穷
素数集合上证明至少一个完整导数非零，才能使用有限鸽笼。
现在可以在反证中同时假设第三个真实 $J'_{136,p}(0)=0$；
它是否给原高精度格独立的新条件，仍须由实际来源证明。
来源的存在、低阶首项或某个子域非零都没有完成这一步。

## 8. 同一个来源的有限证书

普通处令 $m_n=(p-1)p^n$。与 (14) 相同的阶乘规范给
$$
G'_{D,p}(0)\ne0
\quad\Longleftrightarrow\quad
\exists n\ge0:\ v_p(m_n!s_{m_n})<2n+2.
\tag{41}
$$
证明是 (15) 的整 Taylor 展开：$v_p(t_{m_n})=n+1$，
非单位输出误差至少 $m_n$，高于所读线性项。
若导数零则所有值至少 $2n+2$；若导数非零，充分大 $n$
的线性项严格支配，两个方向都保同一测度。

惰性处设
$$
L_H=\sum_{h=1}^{H}(-1)^{h-1}(h-1)!\,a_h,\qquad
M_H=\left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!).
\tag{42}
$$
式 (27) 给 $v_p(J'_{136,p}(0)-L_H)\ge M_H$，故
$$
\boxed{J'_{136,p}(0)\ne0
\Longleftrightarrow \exists H\ge1:\ v_p(L_H)<M_H.}
\tag{43}
$$
特别
$$
J'_{136,p}(0)/p\equiv\alpha_{p+1}/(136pc)\pmod p,
\tag{44}
$$
所以 $\alpha_{p+1}$ 为单位是准确的首层充分条件。
首层失败仍不能代替完整导数消失。

## 9. 一个准确惰性证书同时确定新曲线的秩

这里取单个 $p=23$，不作素数扫描。令 $w=z^6$，
$W=1+\sum_{n\ge1}X_nw^n$。原微分方程给
$$
X_1=-1/7,\qquad
\{(6n-2)(6n-3)-12\}X_n
 =6\sum_{i=1}^{n-1}X_iX_{n-i}\quad(n\ge2).
\tag{45}
$$
同时
$\log(\sigma/z)=-\sum_{n\ge1}X_nw^n/(6n(6n-1))$。
把这两个精确递推代入 (2)，实际前四项为
$$
F_1(z)=z^6+\frac{135218}{105}z^{12}
+\frac{21083507491}{1576575}z^{18}
+\frac{1377083080404572}{9435801375}z^{24}+O(z^{30}).
\tag{46}
$$
所有运算是有理数精确运算，使用原曲线方程和完整来源，
没有使用 L 值、解析秩或未知 Sha 阶。

式 (25)、(44) 因而给
$$
\alpha_{24}\equiv15,\qquad
23c\equiv15,\qquad
J'_{136,23}(0)/23\equiv11\pmod{23}.
\tag{47}
$$
物理曲线的 $s_{24}=D^3\alpha_{24}$ 及
$J_{\Phi_D,23}=D^{-1}J_{136,23}$ 则分别给余数 $22$ 和 $22$。
所以 (40) 的右边准确为二；结合 R466 的秩下界，得到
$$
\boxed{\operatorname{rank}E_{2312}(\mathbf Q)=2,\qquad
\Sha(E_{2312}/\mathbf Q)[23^\infty]\text{ 有限}.}
\tag{48}
$$
这确定新固定曲线的精确秩，也核实新桥至少有一个真实命中；
它本身仍是单素数结果，不是本课题所需的无穷性。
精确递推、$408/136$ 尺度、4608 与 (47) 的证书为
[check-r469-e2312-square-and-first-inert-certificate.py](../scripts/check-r469-e2312-square-and-first-inert-certificate.py)
及同名 JSON。

## 输入出处与范围

- [R466](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)：
  同一原二倍 division 来源、完整二/三/十七处有限角色、
  五条真实算术线、式 (1)–(2) 的精确投影及 $E_D$ 两点独立性。
- [R295](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)
  §2–5、[R397](R397-e24-original-ordinary-square-and-full-selmer-bridge.md)
  §3–6：所用普通 sigma、Katz 插值及通常 Selmer 控制的完整证明。
  新的 $136,408,4608,D$ 和全部尺度在本文重新支付。
- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
  [R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)
  §3–6、[R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)
  §4–6：同一底曲线的严格圆盘、整 signed 模及混合权周期比较。
  本文保留新增十七处 primitive Euler、4608 与固定 $\kappa_D$ 的赋值。
- A. Agboola, B. Howard, *Anticyclotomic Iwasawa theory of CM elliptic
  curves*, Ann. Inst. Fourier **56** (2006), 1001–1048，
  Theorem 2.1.1、Proposition 2.3.4、Theorem 2.4.17(1)(b),(c)；
  [出版全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
- A. Burungale, S. Kobayashi, K. Ota, *Rubin's conjecture on local units
  in the anticyclotomic tower at inert primes*, Annals of Mathematics
  **194** (2021), 943–966，Theorems 2.1、6.1、6.2；
  [原文](https://par.nsf.gov/servlets/purl/10336626)。
  同作者 *p-adic L-functions and rational points on CM elliptic curves
  at inert primes*, JIMJ **23** (2024), 1417–1460，
  §2.2.1、Proposition 3.1、Definition 3.13、Corollary 4.11(i)；
  [出版全文](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf)。
- K. Kato, *p-adic Hodge theory and values of zeta functions of modular
  forms*, Astérisque **295** (2004), 117–290，Theorem 12.5(1)、
  §15.8、Proposition 15.9、Lemma 15.11、(15.16.1)；
  [原文](https://www.numdam.org/article/AST_2004__295__117_0.pdf)。

主目标尚未完成。本文不把新曲线加入固定池这一事实当作跨素数
非零定理，也不宣称有限初级群已经平凡。
