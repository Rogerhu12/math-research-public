# R1047 — 原 degree25 三阶条件矩的完整 finite5 点载体及两单位管一次项非零

日期：2026-11-27。**状态：已证明。** 本篇为 R1042 §10 的整个
$H_3$ 支付实际二、三、五处 Schwartz、标准奇半特征、全部 Hermite
平方常数及负一 Katz 值。其有限5部分有四条角色，权二导子都是
$25\delta$，根数均为负；BDP 的一般点公式允许点为零，因此不需要
另行证明这四个复导数非零。原负一项落入同一 $E_0$ 的有限点对数空间。
Fuchs–Pham 含加法常数的分离定理随后严格排除它与 R1042(79) 的非零
代数部分抵消，证明 R1042(77) 的完整一次系数非零。

这是原指定两单位管的结论。R1042 §11 的整个中间环及其它 unit
扇区仍保留；本篇没有得到原三 canonical 中央导数的跨素数非零。

## 1. 原实际输入及周期

使用
$$
K=\mathbf Q(\omega),\quad \delta=1+2\omega,\quad\delta^2=-3,\quad
E_b:y^2=x^3+b,\quad \omega_b=dx/(2y),
\qquad b=17 .
\tag{1}
$$
$\psi_0$ 是 $E_0:y^2=x^3+1$ 的原 type-$(1,0)$ 角色；
这里下标0指共同基曲线，不指参数 b=0。
沿用 $\sigma=z+\cdots,x=z^{-2}+\cdots,y=-z^{-3}+\cdots$。

R1042(72) 已对完整原双 sigma 证明
$$
\begin{aligned}
H_{3,b}(z)
&=\left.\partial_w^3
 \{\sigma_b(3z-4w)\sigma_b(4z+3w)\}\right|_{w=0}\\
&=432b\,\sigma_b^{25}x_b
 (-35X_b^3+84bX_b^2+84b^2X_b+208b^3),
\qquad X_b=x_b^3 .
\end{aligned}
\tag{2}
$$
其首项为 $-15120b z^5$。它在 standard odd $S_{25}$ 的型五空间；
该空间准确是
$$
\sigma_0^{25}x_0\,\overline{\mathbf Q}[X_0]_{\le3},
\qquad\text{可能首阶 }5,11,17,23.
\tag{3}
$$
(2) 不是 F0 的另一个 degree25 字，也不是 R761 的 degree34 来源。

令 $t^6=b$，取与原普通嵌入相容的同构。真实尺度是
$$
H_{3,b}(z)=tH_{3,1}(tz),\qquad
\Omega_{p,0}=t\Omega_p,\qquad
\nu_{H_{3,b}}=t\nu_{H_{3,1}} .
\tag{4}
$$
最后一式在同一个物理 $\mathbf Z_p$ 变量上成立。
若
$$
I_{3,b,p}=\int_{\mathbf Z_p^\times}x^{-1}\,d\nu_{H_{3,b}}(x),
$$
则
$$
\boxed{\Omega_p I_{3,b,p}=\Omega_{p,0}I_{3,1,p}.}
\tag{5}
$$
因此共同周期的负一值不附加一个新的 b 扭曲点域。

## 2. 原二、三处及 conductor-two 的五处模型

### 2.1 Hermitian 类和不变向量

使用 R290 的负有限加性角色
$\psi_{{\rm add},\ell}(x)=e^{-2\pi i\{x\}_\ell}$、
$\psi_K=\psi_{\rm add}\circ\operatorname{Tr}_{K/\mathbf Q}$，
和 $X=\mathbf Q\delta$ 极化。
本篇 Hermitian 代表为
$$
\boxed{\alpha=\frac{2}{25}.}
\tag{6}
$$
它与 R316 的 $\alpha=2$ 相差 $\operatorname N_{K/\mathbf Q}(1/5)$，
所以同属原二处及三处负的全局类。

在二处保 R316(5) 的实际奇向量
$$
\phi_2=\sum_{a=1,3,5,7}\chi_{-8}(a)
 \mathbf1_{a/4+2\mathbf Z_2},
\quad(\chi_{-8}(1),\chi_{-8}(3),\chi_{-8}(5),\chi_{-8}(7))
=(1,1,-1,-1).
\tag{7}
$$
将 Hermitian 尺度由2变为2/25的局部同构是乘5。
它只将 (7) 乘 $\chi_{-8}(5)=-1$；因此不变线及完整
$\mu_3,-1,g_*$ 作用均由 R316(6)–(9) 返回，而非重新假定 dyadic
偶向量。三处仍为原球
$$
\phi_3=\mathbf1_{3^{-1}\mathbf Z_3},\qquad
\|\phi_2\|^2=2,\quad\|\phi_3\|^2=3 .
\tag{8}
$$
其余尚未列出的有限处均取原标准球。

### 2.2 五处全部有限 torus

五处取
$$
V=\operatorname{Fun}(\mathbf Z/25\mathbf Z),\qquad
\phi_f=\sum_{a\bmod25} f(a)\mathbf1_{a+25\mathbf Z_5}.
\tag{9}
$$
自对偶 Haar 给
$\|\phi_f\|^2=25^{-1}\sum_a|f(a)|^2$。
本处是**偶导子 lattice model**；
Yang 1999 Proposition 1.2(2) 的未分歧基 splitting 平凡，
不能移入奇导子17处缺 quadratic 角色的公式。

写
$$
\mathcal T=(\mathcal O_K/25)^1,\qquad
g_5=-\omega(1+5\delta).
$$
则
$$
|\mathcal T|=30,\quad
g_5^5=-\omega^2,\quad g_5^{10}=\omega,\quad g_5^{15}=-1 .
\tag{10}
$$
原嵌入是
$$
\iota_\alpha(a+b\delta)=
\begin{pmatrix}a&18b/25\\-25b/6&a\end{pmatrix}.
$$
当 $b$ 在5处为单位时，原 Rao 核在 (9) 上给
$$
W(a+b\delta)_{uv}
=\frac15\zeta_{25}^{\,\frac3b\{a(u^2+v^2)-2uv\}},
\qquad
W(1)=I,\quad W(-1)f(u)=f(-u).
\tag{11}
$$
$b$ 非单位时使用同一个 Schrödinger 表示，而不在 (11) 中除以 b。
等价的整模型是 additive 参数6下的
$\begin{pmatrix}a&-3b\\b&a\end{pmatrix}$。
它固定 $v_{\rm old}=\mathbf1_{5\mathbf Z/25}$：
上三角相位、Fourier 和对角算子均逐项固定该向量。

完整 trace 为
$$
\boxed{
\operatorname{Tr}W(g)=
\begin{cases}
25,&g=1,\\
-5,&g\ne1,\quad g\equiv1\bmod5,\\
1,&g\not\equiv1\bmod5.
\end{cases}}
\tag{12}
$$
以下核定所有类。若 b 为单位，(11) 的对角和是模25的一维
非退化 Gauss 和，值5，故 trace1。若
$g=1+5v\delta$，$v\ne0\bmod5$，其整矩阵是
$U(-15v)L(5v)$；trace 可化成
$G_5(v)G_5(2v)=-5$。
这里每个模25和为五倍对应模5和，原 $1/25$ 正好抵消这两个五。
若 $g\equiv-1\bmod5$，在同一式中插入 reflection；
二变量相位的交叉项在5处为单位，
模25的二维和为25，除原25得1。
这些连同 $g=\pm1$ 覆盖全 $\mathcal T$。

令 $\theta_r(g_5)=\zeta_{30}^r$。
对 (12) 作完整30项角色正交，得到
$$
V=\mathbf Cv_{\rm old}\ \oplus\
 \bigoplus_{\theta_r|_{\mathcal T_1}\ne1}V_r,
\qquad \dim V_r=1,\quad|\mathcal T_1|=5 .
\tag{13}
$$
其它非平凡 tame 角色重数为零，故未遗漏旧支。

为固定每条非零原向量，令
$$
\Pi_r=\frac1{30}\sum_{k=0}^{29}\theta_r(g_5)^{-k}W(g_5^k),
\quad
f_r=\Pi_re_{a_r},\quad
a_r=\min\{a:\Pi_re_a\ne0\},\quad
n_r=\sum_a|f_r(a)|^2.
\tag{14}
$$
(13) 保证它有定义且 $n_r>0$。
$\overline{W(g)}=W(g^{-1})$ 说明 $\Pi_r$ 为实矩阵；
$\theta_r(-1)=1$ 时 $f_r$ 是实偶向量。
(14) 是完整固定有限求和的定义，本篇没有声称执行过新矩阵 producer。

### 2.3 半特征和型五四线的绝对方向

原有理支撑准确为 $x=n/12$、n奇。
五处坐标为 $12^{-1}n=23n\bmod25$，因此
$$
a_{r,n}=\chi_{-8}(n)f_r(23n),\qquad
F_r(Z)=\sum_{n\ {\rm odd}}a_{r,n}
 e^{\,\pi i(\delta/3)n^2/200+\pi inZ}.
\tag{15}
$$
置 $s_0=(1-\omega)^{-1}$。直接将 n 改为 n+50，得到
$$
F_r(Z+1)=-F_r(Z),\qquad
F_r(Z+s_0)=-e^{-25\pi is_0-50\pi iZ}F_r(Z).
\tag{16}
$$
第二式的相位来自
$i^n\chi_{-8}(n-50)=-i\chi_{-8}(n)$ 及
$s_0=(1+\delta/3)/2$；没有把这个奇半特征改为一个任意二挠 twist。
故
$$
S_r(Z)=e^{25\sqrt3\pi Z^2}F_r(Z)
\tag{17}
$$
属于最大整环格 $\Lambda=\mathbf Z+s_0\mathbf Z$ 的 standard
degree25 线束。有限 Fourier 系数非零即保证此截面非零。

完整 theta-group 交织将物理 $\omega$ 作用写为
$\omega W(\omega^2)$。其绝对标量可在固定旧向量核定：
$v_{\rm old}$ 使 n=5k，且
$\chi_{-8}(5k)=-\chi_{-8}(k)$，
所以其整 theta 正是 R316 原 sigma(5z) 的负倍数；
旧向量被 $W(\omega^2)$ 固定，而 sigma(5z) 的物理特征为 $\omega$。
因此型五要求
$\theta_r(\omega^2)=\omega$、$\theta_r(-1)=1$。
在 (10) 的准确生成元上，四条全部标签为
$$
\boxed{\mathcal R=\{2,8,14,26\}.}
\tag{18}
$$
$r=20$ 虽满足同一 tame 条件，却在 $\mathcal T_1$ 上平凡，
由 (13) 不出现。
四条 (17) 线性独立；它们都在 (3)，故穷尽整个型五空间。
这一步核的是原全有限环面，不是由两三个好位特征反猜全局角色。

## 3. 四条有限 Hecke 角色、完整 root number 和点域

定义有限角色 $\eta_r$ 的分歧单位表为
$$
\eta_{r,2}(u)=\operatorname{Teich}_{\mu_3}(u\bmod2),\qquad
\eta_{r,5}(u)=\theta_r(u/\bar u)^{-1}.
\tag{19}
$$
在指定 uniformizer 上
$\eta_{r,2}(2)=\eta_{r,5}(5)=\eta_{r,3}(\delta)=1$；
其他地方未分歧，其 Frobenius 值由主 idèle 条件决定。
$\omega$ 在两分歧处的值为 $\omega,\omega^2$，
$-1$ 的两个值都是1，故全局主单位相容。
又因 $\delta/\bar\delta=-1$ 且 $\theta_r(-1)=1$，
$\delta$ 的条件也准确相容。
这唯一指定类数一 K 上的实际有限角色，且
$$
\eta_r^c=\eta_r^{-1},\quad
\eta_r|_{\mathbf A_{\mathbf Q}^{\times}}=1,\quad
\mathfrak f_{\eta_r}=(50),\quad \operatorname{ord}\eta_r=15 .
\tag{20}
$$

令
$$
\nu_r=\psi_0\eta_r^{-1}.
\tag{21}
$$
以下 uniformizer 数值指其 unitary normalization。
其全部坏处为

| 地方 | 单位上的角色 | uniformizer 值 | conductor |
|---|---|---|---|
| 2 | 1 | −1 | 0 |
| 3 | $u\bmod\delta$ | $+i$ | $\delta$ |
| 5 | $\theta_r(u/\bar u)$ | −1 | $25$ |

所以
$$
\boxed{
\mathfrak f_{\nu_r}=(25\delta),\quad
N(\mathfrak f_{\nu_r})=1875,\quad
N_{\operatorname{AI}\nu_r}=5625.}
\tag{22}
$$
特别三处恰一次，而不是 wild $\delta^4$。
其中心角色是 $\epsilon_K\mathrm N$，即 BDP2(1-6)。

五处的绝对 Gauss 和也是可手付的。
令 $\chi$ 为表内单位角色或其逆。
它在 rational units 和 $\delta$ 上平凡。
写 $u=u_0(1+5v)$，$v\in\mathbf F_{25}$；
$\chi(1+5v)=\zeta_5^{\operatorname{Tr}(cv)}$，
其中 $c\ne0$、$\operatorname{Tr}c=0$。
在 $\psi_K/2$ 的 conductor-two Gauss 和中，
内层 v 和只在 $u_0=\pm2c$ 的唯一剩余类非零。
该类可选代表为 $k\delta$，
于是其角色值及剩余加性相位均为1，内层和为25。
故两个逆角色的原 Gauss 和都准确为 $+25$。
uniformizer 的 −1 此次取平方，五处 epsilon 为 +1。

沿 R316 原 $\psi_K/2$，二、三、五、无穷处的 epsilon 为
$$
(-1,-i,+1,i),\qquad
\boxed{w(\nu_r)=-1.}
\tag{23}
$$
这里二处是未分歧角色的真实 conductor-shift，不能误用分歧三次
Gauss 的二处 +1。三处原二次 Gauss 和 $i\sqrt3$ 与
$(+i)^2=-1$ 给 −i。

四条正权来源则是
$$
\Phi_{r,m}=\eta_r\psi_0^{\,2m+1},\qquad m\equiv5\bmod6 .
\tag{24}
$$
它们二处单位平凡，三处值 −i，
五处单位为 $\theta_r(u/\bar u)^{-1}$，uniformizer 仍 −1。
Yang dichotomy 在 $2,3,5,\infty$ 为
$(-1,-1,+1,+1)$，与 (6) 完全一致。
这里使用偶 conductor 的原 splitting，并保未分歧基角色
$\chi_0(5)=-1$。若 $g=x+y\delta\in\mathcal T_1$，则
$v_5(g-1)=v_5(y)$，Yang Proposition 1.2(2) 的两个实际因子
$\chi_0(\delta(g-1))=(-1)^{v_5(g-1)}$ 与
$(-3,-y)_5=(-1)^{v_5(y)}$ 恰好相消。
若 $g\notin\mathcal T_1$，原分段式没有这个 Hilbert 因子，
且 $\chi_0(\delta(g-1))=1$。故在整个环面上，相对这个原基
splitting 的比值均由
$\delta(g-1)/\overline{\delta(g-1)}=g$ 给为
$\theta_r(g)^{-1}$。
所以 (14) 的 $W$-特征 $\theta_r$ 正好给完整不变向量，
未漏掉深单位上的未分歧符号或 Hilbert 因子。

四角色满足
$$
\eta_8=\eta_2^4,\qquad \eta_{14}=\eta_2^7,\qquad
\eta_{26}=\eta_2^{13}.
$$
因此
$$
\boxed{
H=K^{\ker\eta_2}=K^{\ker\eta_r},\quad
\operatorname{Gal}(H/K)=C_{15},\quad
e_2=3,\ e_5=15,
}
\tag{25}
$$
其余有限处未分歧。
实际系数域 $E=K(\zeta_5)=\mathbf Q(\zeta_{15})$；
由完整5惯性值及主理想的 CRT 可得等号。
关联 $B_{\nu_r}/K$ 的维数是 $[E:K]=4$，
不能将四条高阶角色改称四条 $E/\mathbf Q$。
H 是点坐标域，E 是系数域，两者不混同。

## 4. 全 Hermite 平方、Haar 及代数线

置
$$
\kappa_\infty=\frac{6\sqrt3}{25},\qquad
h=\frac{\sqrt{6\sqrt3}}{60\pi i}.
$$
原 Hermite 规范
$\exp(xT-T^2/(8\pi))=\sum H_m(x)T^m/m!$
给
$$
b_{r,m}=\sum_{n\ {\rm odd}}a_{r,n}
 H_m(\sqrt{\kappa_\infty}n/12)
 e^{-\pi\sqrt3 n^2/600},\qquad
\sum_m b_{r,m}T^m/m!=S_r(hT).
\tag{26}
$$
这些 $b_{r,m}$ 是实数，只有 $m\equiv5\bmod6$ 非零。

原全有限范数为 $6n_r/25$；无穷范数为
$5m!/(\sqrt{12\sqrt3}(4\pi)^m)$。
因此
$$
\mathcal N_{r,m}=
\frac{6n_r}{5\sqrt{12\sqrt3}}\frac{m!}{(4\pi)^m}.
$$
Yang Theorem 1.11 的 $S_1$ 是 $\{5\}$，
$c(0)=(1+1/5)^{-1}=5/6$；类数一原 $\mu_6$ 体积比仍为6。
Theorems 2.6、2.15 于是给准确全权式
$$
\boxed{
L(\Phi_{r,m},m+1)=
 C_r\frac{(4\pi)^m}{m!}b_{r,m}^{\,2},\qquad
C_r=\frac{\pi\sqrt{12\sqrt3}}{9\sqrt3\,n_r}.}
\tag{27}
$$
这里没有把原有限范数换成1。

令 $\Omega_0>0$ 为共同 E0 实周期，$\varpi_0=s_0\Omega_0$。
存在唯一首项归一的截面 $D_r$ 与 $s_r\ne0$，使
$$
S_r(Z)=s_rD_r(\Omega_0Z),\qquad
[z^{o_r}]D_r=1,\qquad
o_r\in\{5,11,17,23\}.
\tag{28}
$$
它是实系数线，$s_r\in i\mathbf R^\times$。
此处不预先假定其代数性。先用 (27) 及 CM 临界值代数性，
对实际 Taylor 坐标
$$
t_{r,m}=\frac{b_{r,m}}{m!\,h^m\Omega_0^m}
$$
得到 $(t_{r,m}/t_{r,o_r})^2\in\overline{\mathbf Q}$。
所以这些比值本身代数。
(3) 中的有限多项式由四个 Taylor 坐标恢复，
而 $\sigma_0,x_0$ 的系数有理，
故 $D_r\in\sigma_0^{25}x_0\overline{\mathbf Q}[X_0]_{\le3}$。
该论证保留 h 和 m!，没有误将裸 $b_{r,m}$ 直接除 CM 周期。

写 $d_{r,m}=[z^m]D_r$，则
$b_{r,m}=m!s_r(\Omega_0h)^md_{r,m}$。
因为
$$
\frac{2\pi}{\sqrt3}\,4\pi h^2=-\frac1{75},\qquad
s_0^{-2m}=-\omega^2 3^m\quad(m\equiv5\bmod6),
$$
定义
$$
\begin{split}
c_r&=-\frac{\omega^2}{s_0}\frac{-C_rs_r^2}{\Omega_0}\\
&=25^{o_r}
\frac{(2\pi/\sqrt3)^{o_r}L(\Phi_{r,o_r},o_r+1)}
     {o_r!\,\varpi_0^{2o_r+1}}
\in\overline{\mathbf Q}^{\times}.
\end{split}
\tag{29}
$$
非零性由该真实首项及 (27) 给出。
所有合法权准确满足
$$
\boxed{
\frac{(2\pi/\sqrt3)^m L(\eta_r\psi_0^{\,2m+1},m+1)}
     {m!\,\varpi_0^{2m+1}}
=c_r25^{-m}d_{r,m}^{\,2}.}
\tag{30}
$$
$c_r$ 的 p-adic 估值没有在这里被规定为零。

因为四个 $D_r$ 是 (3) 的完整代数基，存在固定代数数 $a_r$ 使
$$
\boxed{H_{3,1}=\sum_{r\in\mathcal R}a_rD_r.}
\tag{31}
$$
这里只需完整基分解；不要求、也不虚称每个 $a_r$ 都非零。

## 5. 原 bounded 测度及负一 Katz 极限

取原射线上的普通素数 $p>1296$，尤其
$p\equiv1\bmod3$ 且 $p\nmid2\cdot3\cdot5\cdot17$。
保同一普通嵌入，令
$$
\alpha_p=\psi_0(\mathfrak p),\quad
\bar\alpha_p=\psi_0(\bar{\mathfrak p}),\quad
v_p(\alpha_p)=1,\ v_p(\bar\alpha_p)=0,\quad
\epsilon_{r,p}=\eta_r(\mathfrak p).
$$
(28) 的真实代数截面可直接写成
$
D_r=\sum_{k=0}^3 c_{r,k}\,
       \Theta_0^{\,1+3k}\sigma_0^{\,23-6k},
\qquad \Theta_0=x_0\sigma_0^2 .
$
四个 sigma 指数为 $23,17,11,5$，均非负。
所以 R300/R316 原 $\sigma_0,\Theta_0$ 的 bounded Amice 测度，
经有限卷积和这些固定代数系数，即给 $D_r$ 的 bounded 测度。
有限系数若有分母，可乘固定非零代数数清分母后应用整性，再除回；
不要求该数是 p 单位，也不另用一个未付的一般全纯整性断言。

置
$$
\nu_{r,m}=\eta_r\psi_0^{\,m+1}\bar\psi_0^{-m},\qquad
M_{r,m}=\Omega_{p,0}^{\,m}m!d_{r,m}.
$$
(30) 在原 primitive conductor $25\delta$ 的 Katz 规范中是
$$
\boxed{
\mathcal K_{25\delta}(\widehat\nu_{r,m})
=c_r\Omega_{p,0}25^{-m}
 \left(1-\epsilon_{r,p}
          \frac{\alpha_p^m}{\bar\alpha_p^{m+1}}\right)^2
 M_{r,m}^{\,2}.}
\tag{32}
$$
两个 Euler 因子相同来自 $\eta_r^c=\eta_r^{-1}$；
没有将原2处好 Euler 额外删掉，也没有将5处改为 imprimitive L。

取 $m_j=-1+(p-1)p^j$。
它们保持 $m_j\equiv5\bmod6$，趋于 −1；
非单位矩按 boundedness 趋于零，
(32) 的 Euler 因子趋于1。
单位上的 $x^{m_j}$ 则一致趋于 $x^{-1}$。
于是，若
$I_{r,p}=\int_{\mathbf Z_p^\times}x^{-1}d\nu_{D_r}(x)$，
则完整原值为
$$
\boxed{
\mathcal K_{25\delta}(\eta_r\widehat{\bar\psi}_0)
=25c_r\Omega_{p,0}I_{r,p}^{\,2}.}
\tag{33}
$$
没有用未经证明的 ordinary core 来取得这个平方；
这里仅用全正权插值和有界测度极限。

## 6. BDP2 的全部假设及实际有限点载体

本节直接用 BDP2 Theorem 2 和其 §3F/Theorem 3.32，
而非只覆盖 $\mathbf Q$ 上 CM 椭圆曲线解析秩一的 Rubin Theorem 1。
其条件逐项如下：

| BDP2 条件 | 本次实际输入 |
|---|---|
| infinity type $(1,0)$ | (21) |
| (1-6) 中心角色 $\epsilon_K\mathrm N$ | (20)、$\nu_r\nu_r^c=\mathrm N$ |
| (1-7) root number −1 | 原 Gauss 和给出的 (23) |
| (1-8) K 的判别式奇 | $D_K=-3$ |
| (1-9) 导子恰含 different 一次 | (22) 的 $25\delta$ |
| p 分裂且为好位 | 本篇 §5 的原普通 p |

因此该定理给 $P_{\nu_r}\in B_{\nu_r}(K)\otimes\mathbf Q$，
其 p-log 平方为原 $\mathcal K_{25\delta}(\bar\nu_r)$
乘非零代数因子及规定周期。
若 $L'(\nu_r,1)=0$，定理允许 $P_{\nu_r}=0$；
本篇不需要判断这个导数。

为支付共同 E0 和点域，使用 $\nu_r=\psi_0\eta_r^{-1}$：
$B_{\nu_r}$ 是 $\operatorname{Res}_{H/K}E_0$ 的实际
$\eta_r$-isotypic CM 因子（取有理 idempotent，再保系数嵌入）。
在 H 上它是 $E_0^4$ 的同源因子。
BDP2 §2B 的有限 twist、§3F 的 Weil restriction 和
Theorem 3.32 将上述点准确送到
$$
P_r\in
(E_0(H)\otimes_{\mathbf Z}\mathbf Q)
       \otimes_{K}\overline{\mathbf Q},
\qquad
g_{\rm pt}P_r=\eta_r(g)P_r .
\tag{34}
$$
作用只在点因子上；不能把系数域 E 的 Galois 作用与之混合。

以共同代数微分 $\omega_0=dx/(2y)$，
BDP2 Definition 2.13 的周期在这个实际 CM 同源下
是 $\Omega_{p,0}$ 的非零代数倍数。
其全部局部 Gauss、ordinary Euler、微分和同源尺度
保在某个 $\varepsilon_{r,p}\in\overline{\mathbf Q}^{\times}$ 内，
得到
$$
\mathcal K_{25\delta}(\eta_r\widehat{\bar\psi}_0)
=\varepsilon_{r,p}\Omega_{p,0}^{-1}
             \log_{\omega_0}(P_r)^2 .
\tag{35}
$$
这是非零意义的准确代数尺度身份，不声明
$v_p(\varepsilon_{r,p})=0$。
特别不能由 BDP 的 mod-$\overline{\mathbf Q}^{\times}$ 记号推导
点 log 的一个 p 因子不被原 Euler 消耗。

结合 (33)、(35)，按实际平方根选择符号，有
$$
\boxed{
\Omega_{p,0}I_{r,p}=A_{r,p}\log_{\omega_0}(P_r),\qquad
A_{r,p}^2=\frac{\varepsilon_{r,p}}{25c_r}
          \in\overline{\mathbf Q}^{\times}.}
\tag{36}
$$
零值时也成立。
于是 (5)、(31) 支付整个实际来源
$$
\boxed{
\Omega_p I_{3,b,p}
 =\sum_{r\in\mathcal R}a_rA_{r,p}
          \log_{\omega_0}(P_r).}
\tag{37}
$$
右边只有四个固定有限角色的点张量。
没有对一个无限 logarithm 展开实施 point-factor 投影。

## 7. 加法常数与有限椭圆点对数的严格分离

令
$$
\mathscr U_{E_0,p}
=\operatorname{span}_{\overline{\mathbf Q}}
  \{\log_{\omega_0}P:P\in E_0(\overline{\mathbf Q})\}.
$$
除 R749 所用的有限点 log 单射外，本次需要的准确加强是
$$
\boxed{\mathscr U_{E_0,p}\cap\overline{\mathbf Q}=\{0\}.}
\tag{38}
$$
这是 Fuchs–Pham, *Some applications of the p-adic analytic subgroup
theorem*, Theorem 2.1（337–338页）中包含常数1的结论。
它与仅说非零椭圆 log 超越不同：允许任意有限多个点、
任意代数系数，且允许这些点有 CM 线性关系。

为明确本次使用范围，也可直接从该文 Theorem 1.1 证明。
若
$a+\sum b_i\log P_i=0$，$a\ne0$ 代数，
把有限多个点同时乘整数，使它们进入实际小 exponential 域。
在
$\mathbf G_a\times E_0^r$ 的 Lie 代数中取
$a x_0+\sum b_i x_i/N=0$ 的代数超平面，
代数点 $(1,[N]P_i)$ 的非零 logarithm 落在该超平面。
Theorem 1.1 给包含此点且 Lie 代数位于该超平面的正维代数子群。
其连通分支投影到 $\mathbf G_a$ 非零：
取一个杀分支群的整数后，第一坐标仍为非零整数。
$\mathbf G_a$ 与阿贝尔簇之间没有非零代数群同态，
故该连通子群含 $\mathbf G_a\times\{0\}$。
其 Lie 方向 $(1,0,\ldots,0)$ 却不在上述超平面，矛盾。
这也证明 (38)，没有提出任何 p-adic valuation 下界。

## 8. 回到原十二支两单位管：完整一次项必非零

R1042 §10 已由全部12支、原四个 deep sigma 和真实 unit 核得到
$$
[T](\mathcal A_{T,\mathcal U}-\mathcal A_{S,\mathcal U})
=-\frac{d}{18144h_{\rm cf}^{\,6}ba'}
     \{A_p+B_p\Omega_p I_{3,b,p}\},
\tag{39}
$$
其中 $h_{\rm cf}=31/4$ 是共同 carry 尺度，
不与本篇 Hermite h 混用，$d=p-1$，
$a'=(15+19\delta)/50$，且
$$
\begin{aligned}
A_p={}&144q_3e_*^3S_0
       \frac{1+\lambda\kappa^2}{1+\lambda\kappa^3}
 -168q_4e_*^2S_1
       \frac{1+\lambda\kappa}{1+\lambda\kappa^2},\\
B_p={}&\frac{120q_6S_3}{1+\lambda},
\qquad e_*=\frac{93\omega}{50},\\
S_0={}&-166+178\omega,\quad
S_1=-428-439\omega,\quad S_3=334+368\omega .
\end{aligned}
\tag{40}
$$
$\lambda,\kappa,q_k$ 均为原 R1042 的值。
R1042(78)–(79) 已严格证明
$A_p\in\overline{\mathbf Q}^{\times}$、
$B_p\in\overline{\mathbf Q}^{\times}$，适用于全部当前 $p>1296$。

由 (37)–(38)，若 (39) 为零，将得到一个非零代数数
$-A_p/B_p$ 等于有限椭圆点 log 组合，矛盾。因此
$$
\boxed{
[T](\mathcal A_{T,\mathcal U}-\mathcal A_{S,\mathcal U})\ne0
\quad\text{对每个当前原普通射线 }p>1296.}
\tag{41}
$$
这里不需要四个 $I_{r,p}$ 中任何一个非零；
若四个均零，(39) 仍由 $A_p\ne0$ 保持非零。
也不需要假定原 canonical 导数为零。

记 (41) 的实际有限估值为 $\ell_p$。
R1042(80) 的完整 bounded 全尾给
$$
v_p\!\left(
  \int_{\mathcal U_n}(L_T-L_S)\overline h_n\,d\rho
 \right)=n+\ell_p
\qquad(n>\max\{0,\ell_p\}).
\tag{42}
$$
原常数项为零、完整返回的 $\beta^{5n}$ 为单位。
这是原同一管、同一平均和同一 unit cut 的深度，
不是裸 H3 的负一值的估值。

## 9. 完整补域和本篇新增范围

R1042(81) 始终保留
$$
\int(L_T-L_S)\overline h_n\,d\rho
=\int_{\mathcal U_n}(L_T-L_S)\overline h_n\,d\rho
+\int_{\operatorname{supp}\overline h_n\setminus\mathcal U_n}
        (L_T-L_S)\overline h_n\,d\rho .
\tag{43}
$$
R1042 §11 已进一步支付72支平均在整个 $D_1$ 上的真实两态表达。
其中估值为1的更强 S/T 差结论仅指 (90)–(91) 的**未旋转**
$h_n$；$n>1$ 时同一未旋转中间环 $D_1\setminus D_n$ 也为一位。
它不能转写成本篇 (43) 的 $\overline h_n$ 平均 S/T 差的估值。
平均仍保全部 $\mathsf B_\zeta$ 两态，未给这些 S/T 行赋零。
因此 (42) 不允许把整个中间环称作比本管更深的尾，
更不能由一条管非零推出 (43) 左边非零。
其它双 unit 及更多 unit 扇区仍须按原完整核处理。

本篇新增并完成的是：
原 H3 的全四有限5来源与标准半特征；
完整 Haar/Hermite/周期平方；
实际 root-negative BDP 点载体；
以及由加法常数分离得到的原十二支一次项非零。
它为后续完整有限首项的 point-factor 分离提供固定载体，
不把这种有限线性操作延长为未经证明的无限展开投影。
本篇全部新有限身份均给出手证，没有新数值执行或新 L′ consumer。

## 原文和仓库依赖

1. T. Yang, *Eigenfunctions of the Weil representation of unitary group of one
   variable*, Trans. Amer. Math. Soc. **350** (1998), 2393–2407，
   Theorem 0.1 的偶导子模型：
   <https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>。
2. T. Yang, *Nonvanishing of central Hecke L-values and rank of certain
   elliptic curves*, Compositio Math. **117** (1999), 337–359，
   Proposition 1.2(2)、Corollary 1.4、Proposition 1.6、Appendix：
   <https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
3. T. Yang, *Theta liftings and Hecke L-functions*, J. Reine Angew. Math.
   **485** (1997), 25–53，Theorems 1.11、2.6、2.15：
   <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
4. M. Bertolini, H. Darmon, K. Prasanna, *p-adic Rankin L-series and rational
   points on CM elliptic curves*, Pacific J. Math. **260** (2012), 261–303，
   Theorem 2（265页）、§2B、Definition 2.13、§3F/Theorem 3.32
   （299页）；正权代数性亦见 Theorem 2.12：
   <https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf>。
5. C. Fuchs, D. H. Pham, *Some applications of the p-adic analytic subgroup
   theorem*, Glasnik Mat. **51(71)** (2016), 335–343，
   Theorem 1.1（337页）、Theorem 2.1（337–338页）及其 §3.1 证明：
   <https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf>。
6. [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)，
   原 sigma Hermitian 类、二/三处完整生成元、bounded 测度及全 Euler 规范。
7. [R400](R400-full-square-interpolation-determines-core-and-e24-cmseven-phase.md)，
   原完整平方与 bounded-measure 极限；本篇负一极限不预用 core。
8. [R749](R749-point-factor-projectors-and-finite-character-extraction.md)，
   固定微分下的有限点张量空间；本篇另付含加法常数的 (38)。
9. [R1042](R1042-original-three-canonical-common-norm81-carry-and-positive-grid.md)，
   §10 的 H3、完整12支一次式72–81及 §11 的原中间环。
   §10 已发布于281f6ec，§11 已发布于b1e4d08；本篇不重算这些结果。
