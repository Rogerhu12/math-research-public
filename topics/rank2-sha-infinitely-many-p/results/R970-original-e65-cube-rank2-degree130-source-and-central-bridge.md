# R970 — 固定 E65³ 的精确秩二与 degree130 原算术来源

日期：2026-11-26。**已证明：固定曲线 $E_*:y^2=x^3+65^3$ 的有理秩恰为二；全部 $2,3,5,13$ 局部角色、实际 Schwartz、degree130 的同一全权实平方，以及普通与惰性原中央到通常 Selmer 的桥。** 新来源由本文的全部有限向量唯一指定，未由两个好素数任选本征线。R966 §8 的非零 $\mathscr H_{130}$ 是待消费的原输入；本文尚未声称它本身等于本算术来源，也未声称其向本算术线的 CM 投影非零。完整22列的同次390限制消费另行保留实际回执。

本篇使用 $K=\mathbf Q(\omega)$、$\delta=1+2\omega$、$\delta^2=-3$，固定 $\operatorname{Im}\delta>0$，以及 R290、R959 的原加性角色
$\psi_\infty(x)=e^{2\pi ix}$、$\psi_\ell(x)=e^{-2\pi i\{x\}_\ell}$。
新固定曲线不是 $E_{65}$；有限扭曲的立方只作用于相对基曲线的扭曲角色，不能立方已含权一基角色的整个 Hecke 值。

## 1. 两个真实二同源下降像给无条件秩至少二

置 $d=65$、$b_*=d^3=274625$。将原短模型的 $x$ 换成 $X=x+d$，得
$$
 E:\quad Y^2=X^3-3dX^2+3d^2X,
 \qquad a=-195,\quad b=12675=3d^2.
 \tag{1}
$$
其二同源曲线为
$$
 E':\quad Y'^2=X'^3+6dX'^2-3d^2X',
 \qquad a'=390,\quad b'=-12675=-3d^2.
 \tag{2}
$$
这里两个有理二挠点分别是 $(0,0)$。非零二次因子的判别式分别为
$-3d^2$ 和 $48d^2$，均非有理平方，所以两曲线的有理二挠群都恰有两个元素。

采用实际二同源及其对偶
$$
 \phi(X,Y)=\left(\frac{Y^2}{X^2},
                 \frac{Y(b-X^2)}{X^2}\right),\qquad
 \widehat\phi(X',Y')=
 \left(\frac{Y'^2}{4X'^2},
       \frac{Y'(b'-X'^2)}{8X'^2}\right).
 \tag{3}
$$
两式在 $O,(0,0)$ 处按延拓读取，且
$\widehat\phi\phi=[2]$。相应下降同态为
$$
 \alpha_E(O)=1,\quad \alpha_E((0,0))=b,\quad
 \alpha_E(X,Y)=X\pmod{\mathbf Q^{\times2}},
 \tag{4}
$$
另一曲线相同，以 $b'$ 代 $b$。
其核分别为 $\widehat\phi E'(\mathbf Q)$ 和 $\phi E(\mathbf Q)$；
这是二同源的标准 Kummer 映射，也可由 (3) 的原平方坐标直接核定。

现在原两个点为
$$
 P=(325,4225)\in E(\mathbf Q),\qquad
 P'=(325,8450)\in E'(\mathbf Q).
 \tag{5}
$$
不用数值扫描：除以 $X^2=325^2$ 后，两个曲线方程分别成为
$$
 (4225/325)^2=325-195+12675/325=169,
$$
$$
 (8450/325)^2=325+390-12675/325=676.
$$
因此
$$
 \alpha_E(E(\mathbf Q))\supset\langle3,13\rangle,\qquad
 \alpha_{E'}(E'(\mathbf Q))\supset\langle-3,13\rangle .
 \tag{6}
$$
每对平方类独立：第一对可由3、13的赋值分别检测，第二对再保实符号，
两像各至少有四个元素。因 $\alpha_{E'}((0,0))=-3\ne1$，
$\ker\widehat\phi$ 不包含于 $\phi E(\mathbf Q)$。
故
$$
 [E:2E]
 =[E:\widehat\phi E']\,[E':\phi E+\ker\widehat\phi]
 =|\alpha_E(E)|\,|\alpha_{E'}(E')|/2.
$$
左边为 $2^{r+1}$，从而
$$
 \boxed{2^r=|\alpha_E(E)|\,|\alpha_{E'}(E')|/4\ge4,\qquad r\ge2.}
 \tag{7}
$$
这是实际有理点的下降像，不是 Selmer 上界，不假定任何 Sha 有限性或 BSD。
在原短模型上可同时显示两个点
$$
 (260,4225),\qquad (104,-1183);
$$
后一个是 $\widehat\phi(P')=(169,-1183)$ 平移返回所得。
秩证明使用 (6)–(7)，没有用“找到两个点”代替独立性。

### 1.1 原两像的全部局部排除：精确秩二

上述下界还可完全封闭。对一般 $Y^2=X^3+aX^2+bX$，
若素数 $\ell\nmid b$ 且 $v_\ell(X)\ne0$，则 $v_\ell(X)<0$
时 $X^3$ 是右边唯一最小赋值项，$v_\ell(X)>0$ 时
$bX$ 是唯一最小赋值项；因右边为平方，两种情况都迫
$v_\ell(X)$ 为偶数。因此 $\alpha_E$ 的平方类可取
$b$ 的有符号平方自由因子。
对非零此类 $d_0$，写 $X=d_0(M/e)^2$、$(M,e)=1$，
曲线方程给整数 $N$ 满足
$
 N^2=d_0M^4+aM^2e^2+(b/d_0)e^4.
 \tag{7a}
$
$N$ 的整性由其平方为整数直接给出。

对 (1)，二次因子 $X^2-195X+12675$ 在实数上恒正，
所以非挠点 $X>0$。全部候选正平方类为
$\{1,3,5,13,15,39,65,195\}$。
已知 $\langle3,13\rangle$ 有四元，余下只有它的5陪集。
若5在像中，(7a) 成为
$
 N^2=5(M^4-39M^2e^2+507e^4).
 \tag{7b}
$
若 $5\mid e$，因 $(M,e)=1$，括号模5非零。
若 $5\nmid e$，令 $t=M^2/e^2\in\{0,1,4\}\bmod5$，
括号除以 $e^4$ 后为 $t^2+t+2$，三值分别为 $2,4,2$，
也非零。故右边的5赋值恰一，矛盾。于是
$
 \alpha_E(E(\mathbf Q))=\langle3,13\rangle.
 \tag{7c}
$

对 (2)，全部有符号候选由 $-1,3,5,13$ 生成。
乘已知 $\langle-3,13\rangle$ 后，每个带5的类可归入
$d_0=5$ 或 $d_0=-5$。这两条 (7a) 分别为
$
 N^2=5(M^4+78M^2e^2-507e^4),\qquad
 N^2=5(-M^4+78M^2e^2+507e^4).
 \tag{7d}
$
$5\mid e$ 时同样立即矛盾。否则，在
$t\in\{0,1,4\}$ 上，两括号除以 $e^4$ 分别为
$t^2+3t+3$ 和 $-t^2+3t+2$，取值为
$(3,2,1)$ 和 $(2,4,3)$，全部非零。
所以所有带5的类均不在像中。

剩下未知陪集只需排 $-1$。其方程为
$
 N^2=-M^4+390M^2e^2+12675e^4.
 \tag{7e}
$
模3先迫 $3\mid M$，故 $3\nmid e$。
右边三项的3赋值依次至少四、至少三、恰一，
所以总赋值恰一，再与平方矛盾。故
$
 \alpha_{E'}(E'(\mathbf Q))=\langle-3,13\rangle.
 \tag{7f}
$
将两完整四元像代入 (7)，得无条件精确结论
$
 \boxed{\operatorname{rank}E_*(\mathbf Q)=2.}
 \tag{7g}
$
全部排除只用了两个原下降 quartic 的模3、模5赋值，
没有调用点扫描、数据库秩、Sha 或 BSD 假设。

## 2. 原完整 Hecke 角色与 Hermitian 类

记 $\psi_*=\psi_{65^3}$，单位化角色
$\chi=\psi_*|\cdot|_K^{-1/2}$，故
$\chi_\infty(z)=(z/|z|)^{-1}$。在素于 $2\cdot3\cdot5\cdot13$ 的理想上，
Silverman–Stange §6 的同一六次剩余公式给
$$
 \frac{\psi_*}{\psi_1}=(65/\mathord\cdot)_6^{-3}.
 \tag{8}
$$
这是有限二次角色；基角色 $\psi_1$ 没有取三次幂。

$65^3\equiv1\bmod8$、$65^3\equiv-1\bmod9$。
所以二、三处分别与 R290 的 $E_{17}$ 完整六次局部类相同。
五、十三处扭曲参数的赋值为三，短模型为 $I_0^*$，
最小判别式赋值六、导子指数二；不能沿用 $E_{65}$ 的 II 型。
于是
$$
 N(E_*)=2^2\,3^2\,5^2\,13^2=152100,\qquad
 \mathfrak f_*=(2\delta\cdot5\cdot13)=(130\delta).
 \tag{9}
$$
最大整环 CM 和原有理不变微分保持。

固定 $\pi_{13}=4+\omega$、$\bar\pi_{13}=3-\omega$。
在两剩余嵌入中分别有 $\omega=9,3$、$\delta=6,-6$。
全部坏处数据为
$$
\begin{array}{c|c|c|c}
v&\chi_v\text{ 在单位上}&\text{指定 uniformizer 的值}&a(\chi_v)\\ \hline
2&\operatorname{Teich}_{\mu_3}(u\bmod2)&\chi_2(2)=-1&1\\
3&u\bmod\delta\in\{\pm1\}&\chi_3(\delta)=-i&1\\
5&(u\bmod5)^{12}\in\{\pm1\}\subset\mathbf F_{25}
    &\chi_5(5)=-1&1\\
\pi_{13}&(u\bmod\pi_{13})^6
    &\chi_{\pi_{13}}(\pi_{13})=-\omega^2\pi_{13}/\sqrt{13}&1\\
\bar\pi_{13}&(u\bmod\bar\pi_{13})^6
    &\chi_{\bar\pi_{13}}(\bar\pi_{13})=-\omega\bar\pi_{13}/\sqrt{13}&1 .
\end{array}
\tag{10}
$$
这些正指数是 idèle 单位方向，与 (8) 的理想方向互逆。
五处全局有理数五给所示 $-1$；也可由二次扭曲的局部范数读取，
因为 $N_{K_5/\mathbf Q_5}(5)=25$ 是平方。
为核定十三处的绝对值，全局 $\pi_{13}$ 在二、三、五、
另一十三处的值依次为 $\omega,-1,-1,-1$，乘积 $-\omega$；
乘其无穷分量 $\bar\pi_{13}/\sqrt{13}$ 后，乘积公式给 (10)。
共轭计算给另一支。不能把这两个值换成 R959 的 $-\pi_{13}/\sqrt{13}$。

五处 $\vartheta(z)=z^{12}$ 在 $\mathbf F_5^\times$ 上平凡，
且 $\vartheta(\delta)=-1$。按 $z=x+y\delta$ 的 $x$ 分纤维，
其和在 $x=0$ 为 $-4$，在每个 $x\ne0$ 为1，
所以负加性角色的完整 Gauss 和为 $-5$；
结合 $\chi_5(5)=-1$，epsilon 为1，dichotomy 为 $-1$。
三处是 R290 的导子一 Gauss 和 $i\sqrt3$：
epsilon 为 $-i$，乘 $\chi_3(\delta)=-i$ 后仍是 $-1$。
二处 dichotomy 为正；十三两个 split epsilon 的乘积是
$\chi_{\pi_{13}}(-1)=1$，且两支 $\chi_{13}(\delta)$ 的乘积为1。
无穷处 Hermitian 符号正。因此整体根数正，局部 dichotomy 在
$2,3,5,13,\infty$ 分别为 $(+,-,-,+,+)$。

固定小支撑代表
$$
 \boxed{\alpha=5/13,\qquad
 \alpha/5=N_{K/\mathbf Q}(1/\pi_{13}),\qquad
 \kappa=|\delta^3\alpha|=15\sqrt3/13.}
 \tag{11}
$$
它与 $65$ 也同类，因为 $65/\alpha=13^2=N(13)$。
嵌入始终为
$$
 \iota_\alpha(x+y\delta)=
 \begin{pmatrix}x&9\alpha y\\-y/(3\alpha)&x\end{pmatrix}.
$$
特别 $\alpha\equiv1\bmod8$，而 R959 的 $15/13\equiv3\bmod8$；
二处的向量必须重新选对。射线类次数为
$$
 [K(\mathfrak f_*):K]
 =\frac{(4-1)(3-1)(25-1)(13-1)^2}{6}
 =3456=2^7\,3^3.
 \tag{12}
$$

## 3. 全部实际有限 Schwartz

### 3.1 二、三处

二处取 $e_j=\mathbf1_{j/2+2\mathbf Z_2}$、
$f_A=e_0-e_2$、$f_B=e_1+e_3$。因 $\alpha\equiv1\bmod8$
且完整 $\chi_2$ 与 R290 相同，原 $\omega,-1,
g_*=(-11+4\delta)/13$ 的积分核逐相位等于 R290 (22)–(24)。
这些元素生成整个紧环面；四分之一环带的外支撑相消也相同。
因此
$$
 \boxed{\phi_2=f_A+t_+f_B,\qquad
 t_+=(1+\sqrt3)/\sqrt2,\qquad n_2=3+\sqrt3.}
 \tag{13}
$$
这不是 R959 的 $t_-$。
三处 $n((\alpha\delta/4)\psi_K)=-2$，完整 $\chi_3$ 是
R290 的导子一方向，Yang splitting 差平凡，实际 Schrödinger 转模给
$$
 \boxed{\phi_3=\mathbf1_{\mathbf Z_3/3},\qquad n_3=3.}
 \tag{14}
$$

### 3.2 五处：原 quadratic 角色对应 trivial 有限环面线

取 $T_5=\{x+y\delta:x^2+3y^2=1\}\subset\mathbf F_{25}$，
基 $e_a^{(5)}=\mathbf1_{a/5+\mathbf Z_5}$。
原参数 $\beta=-\Delta\alpha/5=3/13\equiv1\bmod5$。
在负加性角色和上述极化中，完整有限表示为
$$
 W_5(g)_{ab}=-\frac{(\frac y5)}{\sqrt5}
 \zeta_5^{\,3\{x(a^2+b^2)-2ab\}/y}\quad(y\ne0),\qquad
 W_5(-1)e_a=e_{-a}.
 \tag{15}
$$
这里的负号不可从 R959 原式抄去：一般 prefactor 是
$(\frac{-2\beta}5)(\frac y5)$，现在 $(\frac{-2}5)=-1$。
原全有限 Gauss 合成给完整群乘法。

Hilbert90 写 $g=z^{-4}$，(10) 的 $\chi_5(z)=z^{12}$
对应环面角色 $\eta(g)=g^{-3}=g^3$。
quadratic splitting 也是 $g^3$，故原不变向量在 (15)
必须取 $\tau=\eta_0\eta^{-1}=1$。
它不是非分裂 Weil 表示缺少的 quadratic 角色 $g^3$。

令 $\Pi_5=6^{-1}\sum_{g\in T_5}W_5(g)$，取
$$
 \boxed{f_5(a)=3\sqrt5(\Pi_5e_0)(a)
 =\sqrt5\,\mathbf1_{a=0}+\zeta_5^{2a^2}+\zeta_5^{-2a^2}.}
 \tag{16}
$$
四个非中央元素的 $y$ 均为非平方，其指数分别是
$2a^2,2a^2,-2a^2,-2a^2$，所以 (16) 是全群投影。
它实、偶，$f_5(0)=\sqrt5+2\ne0$，
$f_5(a)=-(1+\sqrt5)/2$ 对 $a\ne0$。
由这些实际值或正交投影，
$$
 \phi_5=\sum_a f_5(a)e_a^{(5)},\qquad
 \boxed{n_5=\|\phi_5\|^2=3(5+2\sqrt5).}
 \tag{17}
$$
原 additive Haar 为 $\operatorname{vol}\mathbf Z_5=1$。
完整 trivial 环面线维数一。

### 3.3 十三处：两 split 支与真实 Haar 费用

固定 $\delta_0^2=-3$、$\delta_0\equiv6\bmod13$，
写 split 环面参数 $t=x+6y\in\mathbf F_{13}^\times$。
在 Yang 的自然极化中，紧单位固定向量为
$\vartheta^{-1}\mathbf1_{\mathbf Z_{13}^\times}$，
$\vartheta(u)=(u/13)$。
完整非紧作用仍是
$\omega_\chi(g)\phi(y)=\vartheta(g)|g|^{1/2}\phi(yg)$；
uniformizer 移到不交环带，不能称为逐向量不变。

原 isometry 为
$$
 \rho_\alpha\phi(x)=|A|^{1/2}\psi_{13}(Ax^2/2)
 \int\psi_{13}(Axy+Ay^2/4)\phi(y)\,dy,\quad
 A=\delta_0^3\alpha,\quad13A\equiv1\bmod13.
 \tag{18}
$$
它将单位环带送入完整块
$e_a^{(13)}=\mathbf1_{a+13\mathbf Z_{13}}$，每列范数平方 $1/13$。
例如 (18) 的全坐标为
$$
 13^{-1/2}\zeta_{13}^{6a^2}
 \sum_{b\in\mathbf F_{13}^\times}
 (\tfrac b{13})\zeta_{13}^{3b^2-ab}.
 \tag{19}
$$
有限 $\mu_4$ 模型的完整矩阵是
$$
 W_{13}(g)_{ab}=\frac{(\frac y{13})}{\sqrt{13}}
 \zeta_{13}^{\,\{x(a^2+b^2)-2ab\}/y}\quad(y\ne0),\qquad
 W_{13}(-1)e_a=e_{-a}.
 \tag{20}
$$
其 splitting $t^6$ 与 (10) 的实际单位角色 $t^6$ 相抵；
所需有限角色仍为 trivial，而非重数二的 quadratic 角色。

令 $\Pi_{13}=12^{-1}\sum_gW_{13}(g)$，取
$$
 \boxed{f_{13}(a)=6\sqrt{13}(\Pi_{13}e_0)(a)
 =\sqrt{13}\,\mathbf1_{a=0}+1
 -\zeta_{13}^{10a^2}-\zeta_{13}^{12a^2}
 -\zeta_{13}^{a^2}-\zeta_{13}^{3a^2}.}
 \tag{21}
$$
非中央元素的 $x/y$ 为 $0,\pm1,\pm3$；
零指数的两项 Legendre 符号正，其他八项负，给该完整投影。
$f_{13}$ 实且偶，$f_{13}(0)=\sqrt{13}-3\ne0$。
(19) 与 (21) 是同一非零原不变线：原 isometry 保非零，
而对应非 quadratic 有限线维数一。没有逐坐标取实部。
正交投影和实际 Haar 给
$$
 \phi_{13}=\sum_a f_{13}(a)e_a^{(13)},\qquad
 \boxed{n_{13}=\|\phi_{13}\|^2
       =6(13-3\sqrt{13})/13.}
 \tag{22}
$$
不能遗漏分母13。

R959 §8.4 的完整 split 局部范数比较在本 quadratic 角色上仍逐项成立：
Yang Corollary2.13 的单位范数向量
$\sqrt{13}\mathbf1_{1+13\mathbf Z_{13}}$ 经过紧单位平均，
范数平方为 $1/12$，平均保持 theta 积分。
归一向量后 theta 积分平方多十二，原因子 $13/144$ 变为
$$
 c_{13}(0)=13/12.
 \tag{23}
$$
本篇保留两支、非紧作用及全部十二费用。其他有限位取原标准球。

## 4. 真 degree130、同一全权实平方与质量零

有理支撑准确是 $x=n/30$。二处 $2x=n/15\equiv3n\bmod4$，
五处 $5x=n/6\equiv n\bmod5$，十三处
$x=n/30\equiv10n\bmod13$。
令 $v_2=(1,t_+,-1,t_+)$，定义完整来源系数
$$
 a_n=v_2(n\bmod4)f_5(n\bmod5)f_{13}(10n\bmod13).
 \tag{24}
$$
CRT 给非零，(16)、(21) 给实偶，并且
$$
 a_{n+260}=a_n,\qquad (-1)^na_{n+130}=-a_n.
 \tag{25}
$$
置 $s_0=(1-\omega)^{-1}=(2+\omega)/3$、$\Lambda=\mathbf Z+s_0\mathbf Z$，
$$
 F(Z)=\sum_{n\in\mathbf Z}a_n
 e^{\pi i(\delta/3)n^2/260+2\pi inZ},\qquad
 S_{\rm raw}(Z)=e^{130\sqrt3\pi Z^2}F(Z).
 \tag{26}
$$
完整换指标给
$$
 F(Z+1)=F(Z),\qquad
 F(Z+s_0)=e^{-130\pi i s_0-260\pi iZ}F(Z).
$$
所以 $S_{\rm raw}$ 是标准 $\mathcal O(130[0])$ 的非零截面，
无额外 flat twist，真实 Gaussian charge 是65。

采用 R290 的 Hermite 规范，令
$$
 b_m=\sum_n a_n H_m(\sqrt\kappa\,n/30)e^{-\pi\kappa n^2/30^2},
 \qquad h=\sqrt\kappa/(60\pi i).
$$
则
$$
 \sum_m b_mT^m/m!=S_{\rm raw}(hT),\qquad
 130\sqrt3\pi h^2=-1/(8\pi).
 \tag{27}
$$
各有限完整不变性与原全局 $\mu_6$ 给
$b_m=0$ 若 $6\nmid m$，且所有 $b_m$ 实。
这里用到了 (13)，不能用 $t_-$ 得到一条相同来源。

对所有 $6\mid m$，(10) 的坏单位角色保持；
二、三、五指定 uniformizer 值也保持。
十三的非紧参数随 $2m+1$ 变化，但 (18) 的单位环带及其
矩阵系数只使用同一个单位角色，非零赋值环带系数为零。
因此所有这些权均用同一 $\phi_{\rm fin}$，并保持 (23)。

置
$$
 c(0)=(1+1/2)^{-1}(1+1/5)^{-1}(1-1/13)^{-1}=65/108,
$$
$$
 \mathcal N_m=
 \frac{n_2n_3n_5n_{13}}{\sqrt{2\kappa}}\frac{m!}{(4\pi)^m},
 \qquad
 C_*=\frac{2}{6c(0)}\frac{\pi}{3\sqrt3}
       \frac{\sqrt{2\kappa}}{n_2n_3n_5n_{13}}>0.
$$
类数一使紧子群体积乘积与商体积的比仍是六；未留下未付类群和。
Yang Theorems1.11、2.6、2.15，连同 (23)，给准确身份
$$
 \boxed{L(\psi_*^{\,2m+1},m+1)
       =C_*\frac{(4\pi)^m}{m!}b_m^2\qquad(6\mid m).}
 \tag{28}
$$
这是同一个真实来源的完整平方。由 §1 的秩下界及 CM rank-zero
定理的逆否命题，$L(E_*,1)=0$，所以 $b_0=0$。
全部 $\mu_6$ 对称性再给
$\operatorname{ord}_0S_{\rm raw}\ge6$；
此处尚不宣称六阶非零。

## 5. 代数原线、绝对 CM7/19 与22列识别

在同一 $E_1:y^2=x^3+1,\ dz=dx/(2y)$ 上，完整主型空间为
$$
 V_{130}=\sigma^{130}x^2K[X]_{\le21},\qquad X=x^3,\qquad\dim_KV_{130}=22.
 \tag{29}
$$
第21次 $X$ 列是质量列，必须保留。
真实来源因质量零落在 $j\le20$ 的21维帽中。

来源的代数性先于 CM 矩阵。标准 Fourier 坐标是
$$
 d_n=a_n\zeta_{520}^{-n^2},\qquad d_{n+130}=d_n.
 \tag{30}
$$
它们在一个固定代数数域中。按 R959 §10 已付的同一 theta-group
论证，两个真实130挠平移的完整 Heisenberg 表示不可约，
有限 Fourier 模型与 $H^0(E_1,\mathcal O(130O))$ 的 intertwiner
由代数线性方程确定一条代数线，解析同构只差一个共同复标量。
故 (24)–(26) 给一条固定代数来源线，不是假定待算共同核后再宣称代数。
选该线上的非零代数向量
$$
 \Phi_{*,1}=\sigma_1^{130}x_1^2\sum_{j=0}^{20}u_jX_1^j.
 \tag{31}
$$
未算出唯一归一前，不预设 $u_{20}=1$ 或它们全有理。
固定一次代数整数清分母 $D_*\ne0$，使
$\widehat u_j=D_*u_j$ 全为代数整数，并置 $\widehat\Phi=D_*\Phi$。
全程保留这一固定缩放的赋值；不将可重算系数表作为源码。

采用原规范
$\mathscr N_\gamma=[\gamma]_*[\bar\gamma]^*/\gamma$、
$\gamma_7=3+\omega,\ \gamma_{19}=4+\delta$。
(28) 与 R400 的完整平方—整测度引理给
$$
 \mathscr N_\gamma\Phi_{*,1}
 =(\psi_*((\gamma))/\gamma)\Phi_{*,1}.
$$
原质量与 Katz 单位质量零消去 Dirac 项。
具体地，$\psi_1((3+\omega))/(3+\omega)=\omega$，
$65\bmod(3+\omega)=2$，相对扭曲的立方为 $2^{-3}=1\bmod7$。
在十九处 $\gamma_{19}$ 是原 primary 生成元，$65\equiv8$，
$8^3=-1$，立方相对扭曲仍是 $-1$。所以
$$
 \boxed{\mathscr N_7\Phi_{*,1}=\omega\Phi_{*,1},\qquad
        \mathscr N_{19}\Phi_{*,1}=-\Phi_{*,1}.}
 \tag{32}
$$
把旧 E65 的绝对本征值 $\omega^2$ 整体立方会错成1；
那会同时错误地立方基角色。

R966 §8 给标准22列的完整整嵌入
$$
 [\delta]^*(\sigma^{130}x^2X^j)=\sigma^{390}I_j(X),\quad
 I_j=(-1)^{j+1}3^{63-3j}X^{42-2j}(X+4)^{3j+2},
 \quad0\le j\le21.
 \tag{33}
$$
其次数 $44+j$ 三角，最高项系数在 $p>3$ 为单位。
因 $(\delta,\gamma_7\gamma_{19})=1$，完整有限纤维的重排、
原 pull 与 trace 的基变换给
$$
 \mathscr N_{\gamma,390}[\delta]^*
   =[\delta]^*\mathscr N_{\gamma,130}.
 \tag{34}
$$
所有 sigma carrier 和除数 $\gamma$ 同时保留。
因此下一次完整390生产器的一对66列矩阵，可以直接按 (33)
**全列**限制到22列，不需另生产 degree130 CM 算子。
必须回乘整个嵌入矩阵、两算子、完整质量列；
若 (32) 的共同核不是一维，不能任选线认作 (31)。
若是一维，(31) 的先验非零和 (32) 才唯一识别算术来源。
这些是公开消费的接受门，尚未冒充执行回执。

## 6. 真实周期、物理模型与中央桥

此节说明新来源怎样成为合法原中央，而非只提供一条 CM 本征线。
固定系数域及其整数环；以下在其固定有限坏集之外取 $p>211$，
选择相容的 $p$-adic 嵌入。清分母 $D_*$ 及平方常数的赋值均保留。
因全部省去的集合固定且有限，这一范围适用于题目的无穷素数量词。

对于任意非零 $b$，令 $\theta_b^6=b$，准确齐次来源为
$$
 \Phi_{*,b}(z)=
 \sigma_b^{130}x_b^2\sum_{j=0}^{20}u_j b^{20-j}x_b^{3j}
 =b^{-1}\Phi_{*,1}(\theta_bz).
 \tag{35}
$$
真正物理 $b=b_*=65^3$，共同模型是 $b=17$。
不把 Hermitian 参数 $5/13$、degree130 或原微分尺度混为一项。
采用原 $\varpi_*=s_0\Omega_*$，(27)–(28) 的同一周期计算给
$$
 \mathscr E_{*,m}
 =\frac{\widehat\kappa_*}{s_0}\,130^{-m}\widehat s_m^{\,2},
 \qquad \widehat\Phi_{*,b_*}(z)=\sum_m\widehat s_mz^m,\quad6\mid m,
 \tag{36}
$$
其中固定 $\widehat\kappa_*\in\overline{\mathbf Q}^{\times}$。
其非零代数性在 (31) 第一个非零 Taylor 系数处由 CM 临界值代数性取得；
没有逐权重新选择平方根。若未清分母常数为 $\kappa_*$，
则 $\widehat\kappa_*=\kappa_*/D_*^2$。

### 6.1 普通完整测度与通常 Selmer

对 $p\equiv1\bmod3$，R295/R397 的 CM sigma 唯一性给
$\sigma_{b_*}(\log_Et)\in t\mathcal O[[t]]$。
(35) 每项的真实阶为 $126-6j\ge6$，故清分母后给同一个
有界整 Amice 测度 $\widehat\nu_{*,p}$。
取相容单位普通周期 $\Omega_{p,*}$，其完整矩为
$\widehat M_m=\Omega_{p,*}^m m!\widehat s_m$。
记原单位切域分支
$$
 \widehat G_{*,p}(T)=\int_{\mathbf Z_p^\times}
 (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}
 \,d\widehat\nu_{*,p}(x).
 \tag{37}
$$
全部系数整。

对正的 $p-1\mid m$，坏处单位角色保持；
两个 Katz Euler 因子均为
$1-\pi^m/\bar\pi^{m+1}$，其中
$\pi=\psi_*(\mathfrak p),\ \bar\pi=\psi_*(\bar{\mathfrak p})$。
由 (36) 的全权固定平方、沿 $m_0+(p-1)p^n$ 的单位矩极限和
解析唯一性，准确有
$$
 \mathcal K_{*,p}(T)
 =\frac{\widehat\kappa_*}{s_0}\Omega_{p,*}
   (1+T)^{-a_{130,p}}\widehat G_{*,p}(T)^2,\qquad
 a_{130,p}=\frac{\log_p\langle130\rangle}{\log_p(1+p)}.
 \tag{38}
$$
主角色中央质量为零，因此 $\widehat G_{*,p}(0)=0$；
不能单从全质量零推单位质量零。

Agboola–Howard 的同一通常单 CM Selmer 定理适用：
最大整环 CM、正根数、好普通均已付，射线次数3456与 $p$ 互素。
可用辅助好惰性理想 $(11)$，中心辅助值 $-132$ 是单位；
原2、3、5及两个13 primitive 参数保持。
惯性上的阶 $p-1$ 像排除塔上 $\pi$-初级挠点；
与 R943/R959 同一控制和二次分解、三同源给
$$
 r+r_p\le2\operatorname{ord}_0\widehat G_{*,p}.
$$
结合 (7)，
$$
 \boxed{\widehat G'_{*,p}(0)\ne0
 \ \Longrightarrow\ r=2,\quad
 \Sha(E_*/\mathbf Q)[p^\infty]\text{有限}.}
 \tag{39}
$$
若选择有限系数扩张，先作平坦标量扩张再还原 corank，
不会把 $[\mathcal O:\mathbf Z_p]$ 当成额外的秩。

### 6.2 惰性完整 Newton、原 signed 格与通常 Selmer

令 $p=6s-1>211,\ d=p+1$，在共同 $E_1$ 上固定
$f=\log(\sigma/z),\ c=[z^d]f$，R301 已付 $v_p(c)=-1$。
原 Gaussian 和完整 Newton 函数为
$$
 \widehat F_{130}=\widehat\Phi_{*,1},\quad
 \widehat G_{130}=\widehat F_{130}e^{-130cz^d},
$$
$$
 a_h=(130c)^{-h}[z^{dh}]\widehat G_{130},\qquad
 \widehat J_{130,p}(v)=\sum_{h\ge0}a_h(v)_h.
 \tag{40}
$$
不另选一个参考 Gaussian。写 $\mathcal W=z^2x$，完整余项是
$$
 \widehat G_{130}
 =\sum_{j=0}^{20}\widehat u_j
 z^{126-6j}\mathcal W^{2+3j}\exp\{130(f-cz^d)\}.
$$
在 R301 的严格圆盘 $R=p^{-1/(2p)}$ 上范数至多 $R^6$，因此
$$
 v_p(a_h)\ge
 \left\lceil\frac{h(p-1)+6}{2p}\right\rceil,\qquad
 \widehat J_{130,p}\in pv\,\mathcal O\langle v\rangle.
 \tag{41}
$$
完整有限 Gaussian 卷积给
$$
 \widehat J_{130,p}(k)=k!(130c)^{-k}\widehat u^{\,\rm Tay}_{dk}
 \quad(k\ge0).
 \tag{42}
$$
这里 $\widehat u^{\,\rm Tay}_n=[z^n]\widehat F_{130}$，
与多项式坐标 $\widehat u_j$ 明确区分。

$b_* \in\mathbf F_p^\times\subset\mathbf F_{p^2}^{\times6}$，
故可取 $\theta^6=b_*$ 的单位 Hensel 提升。
原整模型同构
$$
 F_\theta:E_1\longrightarrow E_*,\quad
 (X,Y)\longmapsto(\theta^2X,\theta^3Y),\qquad
 F_\theta^*\omega_*=\theta^{-1}\omega_1
 \tag{43}
$$
同时运输物理 Gaussian 为 $\theta^dc$。
Newton 系数中的 $\theta^{dh}$ 完全相消，
所以物理半因子为 $b_*^{-1}\widehat J_{130,p}$，
共同 $b=17$ 模型为 $17^{-1}\widehat J_{130,p}$。

完整 BKO signed 格、参考 $E_1$ 的正号整基及同一 primitive
椭圆单位类，按 R303/R943/R959 的已付控制给
$0\ne\mathcal A_{*,p}\in\mathcal O[[T]]$。
其新费用逐项是：primitive 导子 $130\delta$；
射线次数3456；(43) 的真实微分张量；
两边同阶的 Tate/Gamma 因子与 $m!$；相同的
$p$ 处两个 $1+1/p$ Euler 因子。后两类非单位只在比中消去。
辅助惰性好素数 $\ell\equiv1\bmod p$ 给
$\ell^2+\ell^{-1}\equiv2\bmod p$ 的整除法。

参考五处完整因子为 $6/5$。十三处必须保留
$$
 E_{13}(m)=
 (1-\rho^{2m+1}/13^{m+1})
 (1-\bar\rho^{2m+1}/13^{m+1}),\qquad
 \rho=-\omega^2\pi_{13},\quad\rho+\bar\rho=2.
 \tag{44}
$$
对当前 $d\mid m$，
$E_{13}(m)\equiv12/13\bmod p$；普通 $p-1\mid m$ 亦同。
它在整条允许支上为单位，但不是被偷换的常数。
两条混合权特化来自同一标准类，Kato 的 period 图按同一秩一
CM/Tate 张量相容，故
$$
 v_p\mathcal A_{*,p}(x_m)
 =v_p\mathscr E_{*,m}-v_p\mathscr E_{1,m}.
$$
取 $x_m=q_{\rm ac}^m-1,\ v_p(q_{\rm ac}-1)=1$，
比较参考 $J_{0,p}\in1+p\mathcal O\langle v\rangle$ 与 (42)，
准确得到
$$
 \boxed{v_p\mathcal A_{*,p}(x_{dk})
       =v_p(\widehat\kappa_*)+2v_p\widehat J_{130,p}(k).}
 \tag{45}
$$
被约掉的固定单位是 $b_*,\theta,65$ 和 $J_0(k)$；
$\widehat\kappa_*$ 的赋值始终保留。
此处使用每权真实赋值身份，不假设剩余单位随权解析。

若 $e=\operatorname{ord}_0\widehat J_{130,p}$，
沿 $k=p^n$ 比较 $n$ 的系数，得
$\operatorname{ord}_0\mathcal A_{*,p}=2e$；
非零 $\mathcal A$ 亦排除 $\widehat J\equiv0$。
BKO 基层通常 Selmer 控制于是给
$$
 \boxed{r+r_p\le2e,\qquad
 \widehat J'_{130,p}(0)\ne0
 \ \Longrightarrow\ r=2,\quad
 \Sha(E_*/\mathbf Q)[p^\infty]\text{有限}.}
 \tag{46}
$$
平凡特征在正号格，无相反符号的一维加项。

完整有限证书也保持：令
$$
 L_H=\sum_{h=1}^{H}(-1)^{h-1}(h-1)!\,a_h,\qquad
 M_H=\left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!).
$$
则 $v_p(\widehat J'(0)-L_H)\ge M_H\to\infty$，所以
$$
 \widehat J'_{130,p}(0)\ne0
 \Longleftrightarrow\exists H:\ v_p(L_H)<M_H.
 \tag{47}
$$
首位仅为
$\widehat J'(0)/p\equiv\widehat u^{\rm Tay}_{p+1}/(130pc)\bmod p$，
不能用首位失败替代完整导数失败。
普通证书相应是 $m_n=(p-1)p^n$ 时存在
$v_p(m_n!\widehat s_{m_n})<2n+2$，保同一单位矩切域。

## 7. 与原非零 H130 的下一项实际消费

R966 §8 已从原第六来源 $Z_{390}$ 和 $S=X(X-8)/Q_2$ 得到
$$
 \mathscr H_{130}=T_{\delta,130}(SZ),\qquad
 \Pi_\delta^{390}(SZ)=\tfrac13[\delta]^*\mathscr H_{130}.
 \tag{48}
$$
其真实首项是
$$
 [z^6]\mathscr H_{130}
 =\frac{[X]P_Z}{27\cdot2^{124}}-\frac1{189}\ne0.
$$
非零已由同次原390回执的准确分母位数证明，见 R966 §8；
没有再把生成系数表存作输入。它是实际
$\sigma^{130}x^2\mathbf Q[X]_{\le20}$ 中的来源。

本篇新增的是另一条已付 rank≥2 和全部算术桥的固定来源线 (31)，
现在可以用同次全390矩阵、(33)–(34) 和目标 (32) 比较二者。
还须实际确定完整共同核、原 CM 多项式投影以及
$\Pi_{(\omega,-1)}\mathscr H_{130}$。
即使该投影非零，也须在原测度/完整 cut 上保持投影次序，
不能把 $\mathscr H_{130}$ 本身或其所有乘积赋予新的中央零。
另一个实际 norm130 六 sigma 来源的投影由 R971 协同消费；
二者只共用同一新算术线和同次矩阵，不合并为未经证明的来源身份。

## 依据与已付通用桥

- 二同源下降使用标准原 Kummer 映射；本文 (3)–(7) 已保完整指数与二挠修正。可参 Dujella, *Number Theory*, §15.5 的原二同源下降公式：<https://web.math.pmf.unizg.hr/~duje/pdf/section15-5.pdf>。
- Silverman–Stange, §6、Theorem19 证明的六次剩余方向：<https://arxiv.org/pdf/0912.1831>。
- Yang, *Theta liftings and Hecke L-functions* (1997), Theorem1.11、§2.2 Corollaries2.10、2.13–2.14、(2.28)–(2.30)、Theorems2.6、2.15：<https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- Yang, *Eigenfunctions of the Weil representation of unitary group of one variable* (1998)：<https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>；及 *Nonvanishing of central Hecke L-values and rank of certain elliptic curves* (1999)，Proposition1.2、Corollary1.4、Proposition1.5、Appendix：<https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- R290：同一二处生成元积分、三处原转模和全局体积；R400：全平方恢复原 core；R959 §§7–16：完整 split13 费用、代数 theta-group 比较和原普通/signed 桥。本文对这些通用步骤只支付新角色、参数、Gaussian 和原格费用，没有重新登记它们。
- Agboola–Howard, Theorem2.1.1、Theorem2.4.17(1)(b),(c)：<https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf>；BKO (2021), Theorems2.1、6.1–6.2：<https://annals.math.princeton.edu/2021/194-3/p08>；BKO (2024), §2.2.1、Corollary4.11(i)、Proposition4.12：<https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf>；Kato §15.8、§15.11 period 图：<https://www.numdam.org/article/AST_2004__295__117_0.pdf>。采用这些原文在 R303/R943/R959 已核的完整通常 Selmer 范围。
