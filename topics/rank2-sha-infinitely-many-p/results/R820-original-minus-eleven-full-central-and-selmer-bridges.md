# R820 — 原 E−11 的完整普通／惰性中央与通常 Selmer 桥

后继：[R821 原第四来源与完整四块 carry](R821-original-four-central-axes-and-complete-four-block-carries.md)已以实际 Hurwitz 整性支付高尾四权化；本篇第10节的八权保守式可据此准确收紧，原算术独立与完整 Smith 接口仍开。

日期：2026-11-15。**状态：本篇完整桥已证明。** 固定曲线是
$$
E_-:y^2=x^3-11,\qquad K=\mathbf Q(\omega),\quad
\delta=1+2\omega,\quad\delta^2=-3,\quad s=(1-\omega)^{-1}.
$$
R816 已付该曲线的秩至少二、primitive 导子 $(66)$、完整二／三／十一
处 Schwartz 向量、标准 degree66 截面及全权平方。本篇对这个同一个
来源支付普通有界测度、整条 Katz 平方、惰性完整 signed 格、
混合权周期比较与**整个通常 Selmer 群**的余秩。

因此它确实可加入原固定曲线池，提供第四个合法完整中央条件。
这不等于已经得到原共同格中的第四个独立高精度方程；该接口及
实际 charge 成本在末节明确保留。

## 1. 原来源、微分和固定平方常数

所有曲线均用 $dz=dx/(2y)$，从而
$x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、$\sigma=z+\cdots$。
按 R816 固定
$$
V_1(z)=\sigma(z)^{66}\sum_{j=0}^{10}c_jx(z)^{3j}
      =\sum_{m\ge0}\alpha_mz^m,
\tag{1}
$$
其中按 $j=0,\ldots,10$ 的次序，
$$
(c_j)=
\left(0,\frac{262144}{7},\frac{393216}{7},159744,119808,
\frac{212736}{7},53376,-\frac{7248}{7},-\frac{18156}{7},
\frac{1515}{7},1\right).
\tag{2}
$$
它只含六的倍数次幂，原质量为零，$\alpha_6=1$。
对非零 $b$，真正齐次来源为
$$
V_b(z)=\sigma_b(z)^{66}\sum_{j=0}^{10}c_jb^{10-j}x_b(z)^{3j}
      =b^{-1}V_1(b^{1/6}z).
\tag{3}
$$
特别置
$$
D=-11,\qquad \theta^6=D,\qquad
\Phi_-(z)=V_D(z)=D^{-1}V_1(\theta z)=\sum_{m\ge0}s_mz^m.
\tag{4}
$$
因此 $s_m=D^{m/6-1}\alpha_m$，$s_6=1$。因只含六次幂，
(3)–(4) 的来源不依赖所选六次根；周期、微分及局部同构则始终
使用同一个相容的根。

R816 的 $\psi_-$ 是 $E_-$ 自身的 Hecke 角色，primitive 导子和
根数为
$$
\mathfrak f_-=(2\delta^2\cdot11)=(66),\qquad
W(E_-)=+1.
\tag{5}
$$
设 $\Omega_-=\Omega_1/\theta$，则真正 CM 格生成周期是
$\varpi_-=s\Omega_-$。这里 $\Omega_-$ 可为复数，不能改称正实周期。
R816 的完整 Hermite 比较已给固定常数
$\kappa_-\in\overline{\mathbf Q}^{\times}$，使
$$
\boxed{\mathscr E_{-,m}:=
\frac{(2\pi/\sqrt3)^mL(\psi_-^{\,2m+1},m+1)}
     {m!\varpi_-^{\,2m+1}}
=\frac{\kappa_-}{s}\,66^{-m}s_m^2
\quad(m\ge0,\ 6\mid m).}
\tag{6}
$$
实／复尺度的前一步是 $198^{-m}$；变为 CM 格生成周期后才是
$66^{-m}$。原无限 Schwartz、三处 odd 相位和十一处有限范数均在
$\kappa_-$ 中固定，并非逐权选择平方根。
由 $s_6=1$，
$$
\kappa_-=s\,66^6\mathscr E_{-,6}\in\overline{\mathbf Q}^{\times}.
\tag{7}
$$
本篇不把它在每个 $p$ 的赋值无证设为零。

记
$$
r=\operatorname{rank}E_-(\mathbf Q)\ge2,\qquad
r_p=\operatorname{corank}_{\mathbf Z_p}
              \Sha(E_-/\mathbf Q)[p^\infty].
\tag{8}
$$
秩下界来自 R816 的两个实际点 $(3,4),(15,58)$ 在模5及模17的
独立二下降；本篇不预设秩恰为二。

以下统一 $p>19$。这样 $2,3,5,7,11$ 及后述射线次数都是单位。
除非另有明确说明，所有等式都保当前嵌入及固定常数的实际赋值；
无需增加普通射线同余。

## 2. 普通 sigma 与同一整测度

先设 $p\equiv1\pmod3$。$E_-$ 在 $p$ 处好普通。
Mazur–Tate 普通 sigma 的唯一性给奇整级数 $\Sigma_p$ 以及
常数 $c_p$，满足 $D_E^2\log\Sigma_p=-x-c_p$。
CM 自同构 $[\omega]$ 把常数变为 $\omega^2c_p$，同时保持奇性、
整性和首项，故 $c_p=0$。因此 R295／R397 的原证明在这里给
$$
\sigma_D(\log_{E_D}t)\in t\mathbf Z_p[[t]].
\tag{9}
$$
每项 $\sigma_D^{66}x_D^{3j}$ 的形式参数阶是
$66-6j\ge6$，而 (2) 唯一分母7为单位。所以
$\Phi_-(\log_{E_D}t)$ 是同一个整形式来源。

在完备最大不分歧整数环上取与 $\varpi_-$ 相容的高度一正式群
同构，以其微分定义单位普通周期 $\Omega_{p,-}$。Amice 对应给
$$
\boxed{\Phi_-(\Omega_{p,-}\log(1+Z))
  =\int_{\mathbf Z_p}(1+Z)^x\,d\nu_{-,p}(x)\in R_p[[Z]],}
\qquad
M_m=\int x^m\,d\nu_{-,p}=\Omega_{p,-}^{m}m!s_m.
\tag{10}
$$
这里 $R_p$ 可包含固定代数常数；测度本身有界且整。
定义原单位 principal Mellin 函数
$$
G_{-,p}(T)=\int_{\mathbf Z_p^\times}
 (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}\,d\nu_{-,p}(x).
\tag{11}
$$
其 Taylor 系数在 $R_p$ 中。原全质量为零尚不单独推出
$G_{-,p}(0)=0$；后者由完整 Selmer 比较得到。

为和旧 $b=17$ 的真实来源相接，取 $u^6=-11/17$ 及相容周期
$\Omega_{p,-}=u^{-1}\Omega_{p,17}$。式 (3) 逐项给
$$
\boxed{\nu_{-,p}=u^{-6}\nu_{V_{17},p}
=-\frac{17}{11}\nu_{V_{17},p},\qquad
G_{-,p}=-\frac{17}{11}G_{V_{17},p}.}
\tag{12}
$$
这是明确单位缩放，不是由某个旧 core 符号猜测的比较。

## 3. 全部普通 Euler 因子与整条平方

令
$$
\pi=\psi_-(\mathfrak p),\qquad
\bar\pi=\psi_-(\bar{\mathfrak p}),\qquad
v_p(\pi)=1,\quad v_p(\bar\pi)=0,\quad\pi\bar\pi=p.
$$
使用目标曲线的实际 Frobenius。对正的 $p-1\mid m$，
$\epsilon_m=\psi_-^{m+1}\bar\psi_-^{-m}$ 的完整有限导子仍是
$(66)$；这使用 R816 的单位群及 uniformizer 全表。
两个 Katz Euler 因子准确为
$$
1-\epsilon_m(\mathfrak p)/p
=1-\epsilon_m^{-1}(\bar{\mathfrak p})
=1-\frac{\pi^m}{\bar\pi^{m+1}}.
\tag{13}
$$
该代数字符在 $p$ 未分歧，故相应 $p$ Gauss 因子为一。
其余坏处保原 primitive Euler 乘积，未因共用塔而额外删除。

按 R397 §4 的同一 Katz／de Shalit 周期规范，
$t_m=(1+p)^m-1$ 处的完整插值为
$$
\mathcal K_{-,p}(t_m)
=\frac{\kappa_-}{s}\Omega_{p,-}\,66^{-m}
 \left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2M_m^2.
\tag{14}
$$
Katz 的阶乘与 (6) 的阶乘恰合成 $(m!s_m)^2$，没有删掉其中一个。

整性给非单位输出矩的赋值至少 $m$，(13) 与一之差也至少 $m$。
固定 $p-1\mid m_0\ge0$，沿
$m_j=m_0+(p-1)p^j$ 取实无穷、$p$-adic 有限极限，得到单位矩；
然后用互异权点趋零的解析恒等定理，严格有
$$
\boxed{\mathcal K_{-,p}(T)=
\frac{\kappa_-}{s}\Omega_{p,-}
(1+T)^{-a_{66,p}}G_{-,p}(T)^2,\qquad
a_{66,p}=\frac{\log_p\langle66\rangle}{\log_p(1+p)}.}
\tag{15}
$$
反向 Artin 规范须同时反演 $T$，只改变非零切向坐标，
不改变中心消失阶。(15) 是整条同来源身份，不是逐权重的模单位平方。

## 4. 射线次数360与普通通常 Selmer

$K$ 类数一，$E_-/K$ 具有最大整环 CM。
由 $(66)=(2)\delta^2(11)$ 及只有恒等根单位同余于一，
$$
\boxed{[K(\mathfrak f_-):K]
=\frac{(4-1)(9-3)(121-1)}6
=360=2^3\cdot3^2\cdot5.}
\tag{16}
$$
所以当前 $p$ 不整除此次数；三处较深的 $\delta^2$ 导子并未
换成参考曲线的 $\delta$。

Agboola–Howard Theorem2.4.17(1)(b),(c) 的具体假设为类数一、
最大整环 CM、有理曲线、好普通 $p$、根数正；
整下降还要求 $p\nmid[K(\mathfrak f_-):K]$。它们全部满足。
该定理给反圆 $\mathbf Z_p$ 塔上的**通常单 CM Selmer** 对偶
$X(D_\infty)$ 为 torsion，且其特征理想由 (15) 的相容 Katz
分支生成。这里不是严格局部 Selmer。
若用辅助理想版本，可取 $(5)$：$5$ 惰性、好约化，实际
$\psi_-((5))=-5$、$\mathrm N(5)=25$，中心辅助值 $-30$ 是单位。
因此辅助算子不添中心零，也不引入未知的逐权因子。
特别 $\mathcal K_{-,p}\ne0$。

基层通常 Selmer 限制到塔上不变量是单射：
$\pi$ 连通挠点的一阶 tame inertia 像阶为 $p-1$，pro-$p$ 塔
不能使它平凡，所以塔上没有非零 $\pi$-初级挠点。
Inflation–restriction 的核遂为零，所有通常 Kummer 局部条件
都在限制下保持。取对偶并有理化给
$$
\operatorname{corank}_{\mathbf Z_p}
 \operatorname{Sel}_{\pi^\infty}(E_-/K)
\le\operatorname{ord}_{T=0}\mathcal K_{-,p}.
\tag{17}
$$
右侧使用 torsion Iwasawa 模的中心特征阶，未把各块长度改成
Mordell–Weil 维数。

目标的 $-3$ 二次扭转是 $y^2=x^3+297$，与 $E_-$ 有理三同源，
同源和对偶的复合为 $[3]$。因为 $p\ne2,3$，二次限制／核心限制、
两特征投影及三同源都保持完整通常 Selmer 的余秩。
复共轭交换两个 CM 分量。因此准确地
$$
\operatorname{corank}_{\mathbf Z_p}
 \operatorname{Sel}_{\pi^\infty}(E_-/K)=r+r_p.
\tag{18}
$$
全部潜在 Sha 自由方向均在其中。

由 (15)、(17)、(18)，
$$
\boxed{G_{-,p}\ne0,\quad G_{-,p}(0)=0,\qquad
r+r_p\le2\operatorname{ord}_0G_{-,p}.}
\tag{19}
$$
于是
$$
\boxed{G'_{-,p}(0)\ne0\ \Longrightarrow\
r=2,\qquad \Sha(E_-/\mathbf Q)[p^\infty]\text{ 有限}.}
\tag{20}
$$
余秩零推出有限，使用通常 Selmer 及其 Sha 商的有限余生成性；
这不声称初级群平凡，也不声称判据的逆命题。

## 5. 惰性处的完整原 Gaussian 半因子

现在 $p\equiv5\pmod6$，令
$d=p+1$、$\mathcal O=\mathbf Z_{p^2}$，仍取 $p>19$。
在底曲线 $E_1$ 上定义
$$
f=\log(\sigma/z),\qquad c=[z^d]f,\qquad
B=x\sigma^2=\sum_{m\ge0}\beta_mz^m,
$$
$$
G_{66}=V_1e^{-66cz^d},\quad
a_h=[z^{dh}]G_{66}(66c)^{-h},\quad
J_{66,p}(v)=\sum_{h\ge0}a_h(v)_h,
$$
$$
G_0=Be^{-2cz^d},\quad
J_{0,p}(v)=\sum_{h\ge0}[z^{dh}]G_0(2c)^{-h}(v)_h.
\tag{21}
$$
$(v)_h=v(v-1)\cdots(v-h+1)$。R301 的同一个首分母计算给
$$
v_p(c)=-1,\qquad
pc\equiv-(-1)^{d/6}4^{-d/6}
             \binom{d/3}{d/6}\pmod p.
\tag{22}
$$
此值为单位，$c$ 完全固定，不能另选 Gaussian。

置 $W=z^2x$、$R=p^{-1/(2p)}$。原完整余项是
$$
G_{66}(z)=\sum_{j=0}^{10}c_j z^{66-6j}W(z)^{3j}
             \exp\{66(f-cz^d)\}.
\tag{23}
$$
R301 的严格圆盘上 $\|W\|_R=1$，修正指数收敛且范数至多一；
因 $66-6j\ge6$ 及分母7为单位，$\|G_{66}\|_R\le R^6$。
参考余项范数至多一、质量一。逐项 Cauchy 界给
$$
\boxed{v_p(a_h)\ge
\left\lceil\frac{h(p-1)+6}{2p}\right\rceil\quad(h\ge1),\qquad
J_{66,p}\in pv\,\mathbf Z_p\langle v\rangle,\quad
J_{0,p}\in1+p\mathbf Z_p\langle v\rangle.}
\tag{24}
$$
二者解析于 $|v|_p<p^{(p-1)/(2p)}$，不是仅形式 Newton 级数。
真正有限卷积给所有整数 $k\ge0$ 的准确等式
$$
\boxed{J_{66,p}(k)=k!(66c)^{-k}\alpha_{dk},\qquad
J_{0,p}(k)=k!(2c)^{-k}\beta_{dk}.}
\tag{25}
$$
所以全部 $\beta_{dk}$ 非零，赋值为 $-k-v_p(k!)$。

在物理曲线 $E_-$ 上 $c_{-,p}=\theta^dc$。
把 (4) 与该 Gaussian 同时运输，每个 Newton 系数中的
$\theta^{dh}$ 准确相消，从而
$$
\boxed{J_{\Phi_-,p}=D^{-1}J_{66,p}=-\frac1{11}J_{66,p}.}
\tag{26}
$$
这与只改 Taylor 系数、却冻结原 Gaussian 不同。

## 6. 完整 signed 模、负 D 微分和共同分支

因为 $6\mid p+1$，$\mathbf F_{p^2}^{\times6}$ 包含
$\mathbf F_p^\times$；Hensel 提升给 $\theta^6=-11$ 的相容根
$\theta\in\mathcal O^\times$。于是
$$
F_\theta:E_1\longrightarrow E_-,\quad
(X,Y)\longmapsto(\theta^2X,\theta^3Y),\qquad
F_\theta^*\omega_-=\theta^{-1}\omega_1
\tag{27}
$$
是光滑整模型、形式群及完整 CM Tate 格的同构，逆映射也整。
负 $D$ 没有额外的非单位微分因子；复周期仍按 (4) 的同一根运输。

$\psi_-/\psi_1$ 是六次有限角色。当 $d\mid m$ 时，
$$
(\psi_-/\bar\psi_-)^m=(\psi_1/\bar\psi_1)^m
\tag{28}
$$
是同一反圆分 $\mathbf Z_p$ 塔的同一角色：
$p$ 处 tame 指数 $(1-p)m$ 由 $p+1\mid m$ 消掉，
其余有限六次角色由 $6\mid m$ 消掉。
取原始反圆分参数 $q_{\rm ac}\in1+p\mathcal O$，
$v_p(q_{\rm ac}-1)=1$，并记
$$
x_m=q_{\rm ac}^{\,m}-1,\qquad
v_p(x_{dk})=1+v_p(k).
\tag{29}
$$

BKO21 的局部 Rubin 定理及 BKO24 §2.2.1 给原局部上同调模的
完整整分解
$$
M_j=M_j^+\oplus M_j^-,\qquad
M_j^\pm\simeq\Lambda=\mathcal O[[T]],
\quad j=1,-.
\tag{30}
$$
这些是完整格，不是删去有限模的伪同构。(27) 和限制、
corestriction、dual exponential 相容，故同样给两个符号格的整同构。

两个曲线根数均正，原标准椭圆单位局部类 $\xi_j$ 都在正号格。
参考曲线原值
$$
L(E_1,1)/\varpi_1=(1-\omega)/6\in\mathcal O^\times
\tag{31}
$$
由 R302 的完整 Kronecker 和给出。
BKO24 Corollary4.11(i) 的证明使参考类成为正号格的整基。
因此有唯一
$$
\boxed{F_\theta^*\xi_-=\mathcal A_{-,p}(T)\xi_1,\qquad
\mathcal A_{-,p}\in\mathcal O[[T]],\quad
\mathcal A_{-,p}\ne0.}
\tag{32}
$$
非零性及特征理想来自 BKO21。
本曲线的新有限导子下降次数360和六次扭转次数均与当前 $p$ 互素。
改变原始 signed 基只乘 $\Lambda^\times$；本步没有把未知
局部周期任意规定为单位。

## 7. 同一椭圆单位的混合权与全部非单位因子

沿原完整射线类塔的同一个标准椭圆单位系统，R303 §4 已证明
两条特化路径都给
$$
T_j^{-(2m+1)}(1+m),\qquad
\psi_j^{-(2m+1)}\chi_{\rm cyc}^{\,1+m}.
\tag{33}
$$
第一条先构造 $T_j^{-1}(1)$ 再作反圆分特化；第二条先作高权
CM 张量再作 cyclotomic 临界特化。
在相容原始 CM 基及共同 Tate 基下，两者的向量都是
$\mathbf u_j\otimes b_j^{\otimes(2m+1)}\otimes\zeta^{\otimes m}$。
Norm、twist、特化与局部化交换。
Kato §15.8、两张 §15.11 定义性 period 图、(15.16.1) 及
Theorem12.5(1) 以 $k=2m+2,r_{\rm crit}=m+1$ 给同一个实际高权类。
这里用的是同一 CM 秩一张量比较，不使用其未证明的一般高权
motivic 相容性。

新曲线的全部改动如下，均在原比较中明确支付。

1. Primitive 导子分别为 $(66)$ 和 $(2\delta)$。固定二／三／十一
   处的全部 uniformizer 值保留；导子幂、有限度数360和六次
   同构度数都是当前单位。
2. 可选惰性辅助素数 $\ell\equiv1\pmod p$、
   $\ell\nmid66p$。两曲线在 $(\ell)$ 的 Hecke 值均为 $-\ell$；
   最后辅助除法同为
   $\ell^2+\ell^{-1}\equiv2\pmod p$，故为整单位除法。
3. 真微分张量是
   $F_\theta^*\omega_-^{\otimes(2m+1)}
     =\theta^{-(2m+1)}\omega_1^{\otimes(2m+1)}$。
   全部 CM 张量在秩一格上作，没有对称幂阶乘分母。
4. 共同临界 Tate／Gamma 规范含 $(i\sqrt3)^m m!$。
   $m!$ 可以非单位，必须在两曲线的比中才消去。
5. 惰性好位的两个原 Euler 因子都准确为
   $$
   1-\frac{(-p)^{2m+1}}{(p^2)^{m+1}}
   =1+\frac1p,\qquad v_p(1+1/p)=-1.
   \tag{34}
   $$
   它也只在比中抵消。参考在十一处的原好 Euler 因子完整保留：因为
   $\psi_1((11))=-11$，每个本中央权的该因子都是
   $1-(-11)^{2m+1}/121^{m+1}=12/11$，在当前 $p>19$ 为单位。
   没有为共同射线模数人为删掉它；三处的各自 primitive
   约化同样保持。

这正是 R303／R402／R469 的完整相对期比较所需条件，故
$$
\boxed{v_p\mathcal A_{-,p}(x_m)
=v_p\mathscr E_{-,m}-v_p\mathscr E_{1,m}
\quad(m>0,\ d\mid m).}
\tag{35}
$$
参考非零由 (24)–(25) 保证；取比合法。
本论证只需要每权的准确赋值，不假定剩余单位随权解析。

参考的全权平方是
$\mathscr E_{1,m}=(6s)^{-1}2^{-m}\beta_m^2$。
由 (4)、(6)，完整代数比为
$$
\frac{\mathscr E_{-,m}}{\mathscr E_{1,m}}
=6\kappa_-D^{-2}\theta^{2m}33^{-m}
       \left(\frac{\alpha_m}{\beta_m}\right)^2.
\tag{36}
$$
对 $m=dk$，(25) 给
$\alpha_{dk}/\beta_{dk}=33^kJ_{66,p}(k)/J_{0,p}(k)$；
两个 $k!$ 和两个首分母均在此式中准确保留。
$D,\theta,33$ 是单位，故
$$
\boxed{v_p\mathcal A_{-,p}(x_{dk})
=v_p(\kappa_-)+2v_pJ_{66,p}(k).}
\tag{37}
$$

若 $J_{66,p}$ 恒零，非零 $\mathcal A_{-,p}$ 会在
$x_{dp^n}\to0$ 的无穷点上为零，矛盾。
令 $e=\operatorname{ord}_0J_{66,p}$、
$j_e=[v^e]J_{66,p}$。
沿 $k=p^n$ 比较两边首项赋值中 $n$ 的系数与常数，得到
$$
\boxed{\operatorname{ord}_0\mathcal A_{-,p}=2e,\qquad
v_p([T^{2e}]\mathcal A_{-,p})
=v_p(\kappa_-)+2v_p(j_e)-2e.}
\tag{38}
$$
固定常数的实际赋值未省掉；不需要先删除使它非单位的有限素数。

## 8. 惰性通常 Selmer 与整个 Sha 初级群

BKO21 Theorems6.1–6.2 在根数正的 CM 曲线上比较的是基层
**完整通常 Selmer 群**；平凡角色属于正号分支，没有相反符号
产生的一维附加项。因此
$$
\operatorname{corank}_{\mathcal O}
 \operatorname{Sel}_{p^\infty}(E_-/K)
\le\operatorname{ord}_0\mathcal A_{-,p}.
\tag{39}
$$
同 §4，二次特征分解与有理三同源把左侧准确识别为 $r+r_p$：
先在 $\mathbf Z_p$ 上得到两倍余秩，再以
$[\mathcal O:\mathbf Z_p]=2$ 还原。
没有删除严格局部核或潜在 Sha 自由方向，也不假设高度非退化。

所以
$$
\boxed{J_{66,p}\ne0,\qquad
r+r_p\le2\operatorname{ord}_0J_{66,p},\qquad
J'_{66,p}(0)\ne0\Longrightarrow
r=2,\ \Sha(E_-/\mathbf Q)[p^\infty]\text{ 有限}.}
\tag{40}
$$
由 (26) 可等价使用目标曲线的物理半因子。

## 9. 同一来源的完整有限证书

普通处令 $m_n=(p-1)p^n$。
$t_{m_n}$ 的赋值是 $n+1$，非单位输出误差至少 $m_n$；
由 $G(0)=0$ 和整性，准确有
$$
\boxed{G'_{-,p}(0)\ne0
\ \Longleftrightarrow\
\exists n\ge0:\ 
v_p\!\left(m_n!s_{m_n}\right)<2n+2.}
\tag{41}
$$
若导数为零，所有高项至少 $2n+2$；若导数非零，充分大 $n$
的线性项严格支配。单位普通周期不改变赋值，
所以证书不需要知道它的数值。

惰性处，令
$$
L_H=\sum_{h=1}^{H}(-1)^{h-1}(h-1)!\,a_h,\qquad
M_H=\left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!).
$$
式 (24) 给 $v_p(J'_{66,p}(0)-L_H)\ge M_H$，从而
$$
\boxed{J'_{66,p}(0)\ne0
\ \Longleftrightarrow\
\exists H\ge1:\ v_p(L_H)<M_H.}
\tag{42}
$$
特别
$$
J'_{66,p}(0)/p\equiv\alpha_{p+1}/(66pc)\pmod p.
\tag{43}
$$
原系数为单位是严格首层充分条件；首层失败不等于完整导数消失。

## 10. 新第四中央、真实 charge 与尚未支付的同像独立性

令 $\Theta=x\sigma^2$、$t=-b/x^3$。R816 的原角式是
$$
V_b=b^{-1}\Theta_b^{33}f_V(t),\qquad
f_V(t)=\sum_{j=0}^{10}c_j(-t)^{11-j}.
\tag{44}
$$
相对原 $S_{34}$ 的真实 Gaussian charge 为 $33/17$。
本篇证明：若要反证固定池的无穷性，可在相应共同素数集合上
合法添加这个同一原来源的完整中央导数为零。
新源仍与旧源处于 $\mathbf Q(t,\Theta)$ 的二元函数域；
四条曲线并不变成四个代数独立生成元。

惰性高精度接口必须保持实际原系数。若用同一个 admissible
Gaussian $\kappa$、$a=p\kappa\in\mathcal O^\times$，写各真实
余项的第 $h$ 行为 $c_{\nu,h}$、charge 比为 $q_\nu$，
则完整 Newton 导数贡献为
$$
\frac{a}{p}J'_\nu(0)
=\sum_{h\ge1}(-1)^{h-1}(h-1)!
 \frac{p^{h-1}}{q_\nu^h a^{h-1}}c_{\nu,h}.
\tag{45}
$$
四来源的比是 $1,36/17,4,33/17$。
要读 (45) 模 $p^4$，不能从旧三精度公式无证只保头四行：
原严格圆盘仅统一保证 $h\ge9$ 的 $J'$ 项至少 $p^5$，
而 $h=7,8$ 的项仍可能是 $p^4$，除以 $p$ 后会贡献。
所以在没有另付改进尾界前，至少保完整 $h=1,\ldots,8$、
全部 Gaussian 修正及原13个 carry。

本篇尚未把 (44) 加入原共同 $M$ 后证明第四行独立，
也未声称它改善原全局严格预算。
实际角因子、归一化成员关系和四个高轴的完整系数比较，
应从同一 (1) 生成并另行支付。
来源的质量为零、秩下界、有限 CM 本征值或新中央桥，
都不能单独替代这项工作。

## 11. 证明输入与复现范围

本文是原来源的解析／整模比较，不依赖新的数值素数扫描，
也没有新增可重算输出数据。
来源 (1)–(7) 的完整有限规范与精确矩阵证书见：

- [R816](R816-original-minus-eleven-rank-two-schwartz-and-degree66-source.md)：
  同曲线秩至少二、导子、全部局部 Schwartz／半特征及全权平方。
- [R295](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)
  与 [R397](R397-e24-original-ordinary-square-and-full-selmer-bridge.md)：
  普通 sigma 唯一性、Katz 插值和通常 Selmer 的原完整比较。
- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)：
  原首分母、严格圆盘与全部 Newton 尾界。
- [R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)：
  参考 $x\sigma^2$ 的完整角色、原值和全权平方。
- [R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)：
  同一个标准椭圆单位的混合权路径和准确整周期比较。
- [R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)
  及 [R469](R469-e2312-full-weight-square-ordinary-inert-sha-bridges.md)：
  该比较对不同 primitive CM 导子的完整逐项版本。

一手定理及本篇具体使用范围：

1. A. Agboola、B. Howard，*Anticyclotomic Iwasawa theory of CM
   elliptic curves*，Ann. Inst. Fourier56 (2006)，1001–1048，
   Theorem2.1.1、Proposition2.3.4、
   Theorem2.4.17(1)(b),(c)；
   [出版全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
   用于 §3–4 的 primitive Katz 分支、非零和通常 Selmer 特征理想；
   新射线次数360已在 (16) 完整核定。
2. A. Burungale、S. Kobayashi、K. Ota，*Rubin's conjecture on local
   units in the anticyclotomic tower at inert primes*，Annals194 (2021)，
   943–966，Theorems2.1、6.1、6.2；
   [出版页](https://annals.math.princeton.edu/2021/194-3/p08)，
   [作者公开稿](https://par.nsf.gov/servlets/purl/10336626)。
   用于 §6、§8 的完整整分解、非零和通常 Selmer 控制。
3. 同三位作者，*p-adic L-functions and rational points on CM elliptic
   curves at inert primes*，JIMJ23 (2024)，1417–1460，
   §2.2.1、Proposition3.1、Definition3.13、Corollary4.11(i) 的证明；
   [出版全文](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf)。
   用于实际标准类、符号和参考正号格整基。
4. K. Kato，*p-adic Hodge theory and values of zeta functions of modular
   forms*，Astérisque295 (2004)，117–290，
   Theorem12.5(1)、§15.8、Proposition15.9、Lemma15.11、(15.16.1)；
   [原文](https://www.numdam.org/article/AST_2004__295__117_0.pdf)。
   本文只按 R303 的完整证明使用同类特化及定义性 period 图，
   不添加未证明的高权 motivic 相容性。

主目标的跨素数非零仍须证明。本篇新增的是同一固定曲线的合法
完整中央条件及其准确有限证书，尚非无穷性结论。
