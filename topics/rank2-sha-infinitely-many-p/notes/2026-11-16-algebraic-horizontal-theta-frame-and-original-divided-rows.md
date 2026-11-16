# 原热连接的固定代数水平格与四条指定除 p 行

日期：2026-11-16。**以下固定代数水平格、degree2 显式根式、原惰性素数处的全格零 p-curvature，以及四个实际来源的同一标量热算子表达均已证明。四条指定除 p 值不能同时为零仍未证明。**

本注沿用 [R855](../results/R855-original-full-heat-connection-and-canonical-divided-jet.md) 与 [R856](../results/R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)。这里的新有限覆盖位于**参数曲线**，不是把原 $z$ 曲线上的 $\mathcal P_{2,M}$ 换成一个固定有理函数。原 Frobenius 初始资料、CM13 frame、四个原输入和全部 carry 不变。

## 1. 参数曲线和同一个 whole 连接

保持
$$
E:\ y^2=x^3-\frac{g_2x}{4}-\frac{g_3}{4},\qquad
D x=2y,\quad D y=3x^2-\frac{g_2}{4},\qquad
\Delta=g_2^3-27g_3^2\ne0.
\tag{1}
$$
对正偶数 $m$，原格为
$$
\mathscr V_m=H^0(E,\mathcal O(mO)),\qquad
A_R(z)=\sigma(z)^mR(x(z),y(z)).
$$
其完整基包含
$$
x^a\quad(0\le a\le m/2),\qquad
yx^a\quad(0\le a\le(m-4)/2).
\tag{2}
$$
没有删除奇基。定义仍是
$$
L_2=6g_3\partial_{g_2}+\frac{g_2^2}{3}\partial_{g_3},\qquad
\mathcal Lx=2x^2-\frac{g_2}{3},\quad \mathcal Ly=3xy,
$$
$$
\boxed{\mathcal H_mR=\mathcal LR-\frac{m-1}{2}xR-\frac{D^2R}{2m}.}
\tag{3}
$$
系数函数上的 $\mathcal L$ 等于 $L_2$。R855 已证明它保持(2)，并且
$$
Q_m A_R=\sigma^m\mathcal H_mR,\qquad
Q_m=L_2-\frac{D^2}{2m}-\frac{mg_2z^2}{24}.
\tag{4}
$$
因此 $\mathcal H_m$ 是沿 $L_2$ 的同一代数连接：
$\mathcal H_m(fR)=(L_2f)R+f\mathcal H_mR$。

由 $L_2\Delta=0$，固定非零 $\Delta_0$ 后置
$$
X=\frac{g_2}{3},\qquad Y=g_3.
$$
参数曲线及其导子准确为
$$
\boxed{
E_{\Delta_0}^{\rm par}:\ Y^2=X^3-\Delta_0/27,\qquad
L_2X=2Y,\quad L_2Y=3X^2.
}
\tag{5}
$$
这条曲线的 $X,Y$ 与物理曲线(1)的 $x,y$ 不同。

## 2. 周期、准周期和水平 theta 的绝对倍率

先在复解析单连通参数片上取有向完整周期 $\lambda,\mu$，令
$$
\tau=\mu/\lambda,\quad \Im\tau>0,\qquad
\eta_\lambda=\zeta(z+\lambda)-\zeta(z),\quad q=\eta_\lambda/\lambda .
$$
R855 的实际公式
$$
L_2x=2x^2-g_2/3+\zeta D x,\qquad
L_2\zeta=-y-\zeta x+g_2z/12
$$
与周期性逐项比较，给
$$
L_2\lambda=-\eta_\lambda,\qquad
L_2\eta_\lambda=g_2\lambda/12.
$$
例如对 $x(z+\lambda)=x(z)$ 求参数导数，额外项正是
$(\eta_\lambda+L_2\lambda)Dx$；对 $\zeta$ 再比较便得到第二式。
Legendre 正规是 $\eta_\lambda\mu-\eta_\mu\lambda=2\pi i$，所以
$$
\boxed{
L_2\tau=\frac{2\pi i}{\lambda^2},\qquad
L_2q=q^2+\frac{g_2}{12},\qquad
L_2(z/\lambda)=qz/\lambda.
}
\tag{6}
$$

用变量 $u$ 的周期 $1,\tau$ 正规，定义
$$
\vartheta_{m,a}(\tau,u)
=\sum_{n\in\mathbf Z+a/m}
 \exp\!\left(\pi imn^2\tau+2\pi imnu\right),
\qquad a\in\mathbf Z/m\mathbf Z .
\tag{7}
$$
逐项求导给
$$
\partial_\tau\vartheta_{m,a}
=\frac{1}{4\pi im}\partial_u^2\vartheta_{m,a}.
\tag{8}
$$
$m$ 偶时，这 $m$ 条是标准 even degree-$m$ 的完整基：
$u\mapsto u+1$ 的因子为一，
$u\mapsto u+\tau$ 的因子为
$\exp(-\pi im\tau-2\pi imu)$，恰与 odd $\vartheta_1^m$ 的因子相同。

令 $\vartheta_1$ 使用同一周期 $1,\tau$，其绝对规范为
$$
\vartheta_1'(0;\tau)=2\pi\eta(\tau)^3,\qquad
\sigma(z)=
\lambda\,\frac{\vartheta_1(z/\lambda;\tau)}{\vartheta_1'(0;\tau)}
e^{qz^2/2}.
\tag{9}
$$
这里 $\eta$ 是 Dedekind eta；不能与准周期 $\eta_\lambda$ 混记。
本篇的判别式满足
$$
\boxed{\Delta=(2\pi/\lambda)^{12}\eta(\tau)^{24}.}
\tag{10}
$$

逐项使用(6)、(8)可得
$$
Q_m\!\left(e^{mqz^2/2}\vartheta_{m,a}(\tau,z/\lambda)\right)
=-\frac q2e^{mqz^2/2}\vartheta_{m,a}(\tau,z/\lambda).
$$
其中 $\partial_u^2$、$\partial_u$、$q^2z^2$ 和 $g_2z^2$ 项分别相消，
唯一余项是 $-q/2$。又
$L_2(\lambda^{-1/2})=(q/2)\lambda^{-1/2}$。
因此取
$$
\boxed{
F_{m,a}(z)
=\sqrt{2\pi}\,\lambda^{-1/2}
 e^{mqz^2/2}\vartheta_{m,a}(\tau,z/\lambda),\qquad
h_{m,a}=F_{m,a}/\sigma^m ,
}
\tag{11}
$$
便准确有
$$
\boxed{\mathcal H_mh_{m,a}=0.}
\tag{12}
$$
固定平方根按(10)和原 $q$ 展开相容选择；改变该选择只同时乘一个明确的固定根单位，不产生 $p$ 依赖。

最重要的是(11)的表面超越常数已经全消：
$$
\boxed{
f_{m,a}:=\varepsilon_m(h_{m,a})=F_{m,a}(0)
=\Delta^{1/24}\frac{\vartheta_{m,a}(\tau,0)}{\eta(\tau)}.
}
\tag{13}
$$
右端将被证明是固定代数函数。这里没有将
$\lambda^{-1/2}\eta$ 当成代数数而漏掉 $\sqrt{2\pi}$。

## 3. 固定代数覆盖：完整有限表示与每个 theta 除子

先证明(13)的代数性，而不假定一个未经核定的最小 congruence level。
置 $\xi_m=e^{2\pi i/m}$、$v_a=\vartheta_{m,a}(\tau,0)/\eta(\tau)$。
Poisson 求和与 $m$ 偶给准确两生成元：
$$
\boxed{
v_a(-1/\tau)=\frac1{\sqrt m}\sum_{b\bmod m}\xi_m^{-ab}v_b(\tau),\qquad
v_a(\tau+1)=e^{\pi i a^2/m-\pi i/12}v_a(\tau).
}
\tag{14}
$$
平方根在 theta 与 eta 两边按同一支相消。(14)保留了 eta 的
$e^{-\pi i/12}$，不是仅一个 projective 转换。

这两个矩阵生成有限群。自含的有限性证明如下。
位移矩阵 $Ue_a=e_{a+1}$ 与对角矩阵 $Ve_a=\xi_m^ae_a$，
连同所需 $\mu_{24m}$ 中心，生成有限 Heisenberg 群。
(14)的两个矩阵都正规化它；其共同中心化子只有标量，
因为 $V$ 的特征线互异而 $U$ 循环置换它们。
故生成群的 projective image 注入这个有限群的 automorphism group。
两个生成元的行列式均为根单位，故整个 determinant image 有限。
若标量 $\alpha I$ 在该群中，则 $\alpha^m$ 属于这个固定有限 determinant image，
因而标量核也有限。于是全 image 有限，不只是 projective image 有限。

每个 $v_a$ 在上半平面全纯，分母 eta 无零。
它在无穷 cusp 的展开只含固定分母的有理指数，
并有有限主部；其它 cusp 由(14)给同一性质。
取其有限 orbit 的单首多项式，系数为全 modular group 不变量，
在上半平面全纯、只在 cusp 有极，因而为 $j$ 的多项式。
这些系数的 $q$ 展开均属一个固定数域；
用 $j=q^{-1}+744+\cdots$ 的首项逐次消主部，得到多项式系数也在该数域。
所以
$$
v_a\text{ 代数于 }\overline{\mathbf Q}(j),\qquad
j=1728g_2^3/\Delta.
\tag{15}
$$
这同时给一个先于 $p$ 固定的有限覆盖，包含(14)的全部相位。

再证明 $h_{m,a}$ 真在原 whole 格，而不是新来源。
由(7)或单 theta 的零点式，其零除子为
$$
D_{m,a}
=\sum_{k=0}^{m-1}
\left[\frac{\lambda}{2m}
+\left(\frac12-\frac am\right)\mu+\frac{k\lambda}{m}\right].
\tag{16}
$$
它的每一点都是 $2m$ 挠点，彼此不同，均非 $O$。
这些点的和为
$m\lambda/2+(m/2-a)\mu$，对偶数 $m$ 属于周期格，
所以 $D_{m,a}-mO$ 为 principal divisor。
在有完整 $2m$ 挠结构的固定有限覆盖上，
存在唯一的有理函数 $r_{m,a}$，满足
$$
\operatorname{div}(r_{m,a})=D_{m,a}-mO,\qquad
r_{m,a}=z^{-m}+\cdots\quad\text{在 }O.
\tag{17}
$$
首系数也可用原代数参数 $-x/y=z+\cdots$ 定义，
故没有按 $p$ 改局部坐标。由(9)、(11)的 divisor 和首项，
$$
\boxed{h_{m,a}=f_{m,a}\,r_{m,a}.}
\tag{18}
$$
式(13)、(15)、(17)遂完全代数地定义(11)，包括其绝对倍率。

由 theta 的完整线性独立性，$(h_{m,a})_{a\bmod m}$ 是原
$\mathscr V_m$ 的全 $m$ 维基。
也可用(7)的不同 Fourier residue class 直接证明独立。
故所有原基列(2)都由它唯一表示。
$a\mapsto-a$ 满足
$$
h_{m,-a}(-z)=h_{m,a}(z),\qquad f_{m,-a}=f_{m,a}.
\tag{19}
$$
因此 odd 差 $h_{m,a}-h_{m,-a}$ 的质量恒零，
但它们仍是 whole 格的一部分；后文的偶 jet 不能把整个格误压成质量空间。

本篇可对有限集合
$$
\mathcal M=\{2,10,24,34,42,48,66,72,112,136\}
\tag{20}
$$
一次取上述覆盖的 compositum，同时容纳四个原 degree、共同 $A_{24}$ 和所有原伙伴。
覆盖及系数数域都先于 $p$ 固定。
这里只是固定代数扩标来表达同一来源，没有改变原中央条件，
也没有给原列格增加自由列或宣称覆盖的全局预算为零成本。

## 4. degree2 的完全根式水平基

这一小块不用任何 theta 记号即可核准标量规范确实可代数化。
设 $e_1,e_2,e_3$ 为物理曲线(1)的三个二挠 $x$ 根，取
$$
A^2=e_1-e_2,\qquad B^2=e_1-e_3,\qquad
q_\pm=e_1\pm AB,\qquad c_\pm^2=A\mp B.
\tag{21}
$$
所有差均非零；固定根选择只是固定代数覆盖。
逐次微分二挠方程给
$$
L_2e_i=2e_i^2-g_2/3,\qquad
L_2A=-e_3A,\quad L_2B=-e_2B .
$$
于是
$$
\boxed{
L_2q_\pm=q_\pm^2/2-5g_2/24,\qquad
L_2c_\pm=-q_\pm c_\pm/2.
}
\tag{22}
$$
从(3)直接有 $\mathcal H_2(1)=-x/2$、
$\mathcal H_2(x)=-5g_2/24$，故
$$
\mathcal H_2(x-q_\pm)=\frac{q_\pm}{2}(x-q_\pm).
$$
因此
$$
\boxed{\widehat h_\pm=c_\pm(x-q_\pm),\qquad
\mathcal H_2\widehat h_\pm=0}
\tag{23}
$$
是两个明确的代数水平列，行列式为
$c_+c_-(q_--q_+)=-2ABc_+c_-\ne0$。
它们与(11)的 $m=2$ 基相差一个沿 $L_2$ 常数的可逆矩阵；
无需把两个根式规范未经计算地相认成同一 theta label。

等价地，写水平列为 $a+bx$，则
$$
L_2a=\frac{5g_2}{24}b,\qquad L_2b=a/2,\qquad
\boxed{L_2^2b=\frac5{16}Xb.}
\tag{24}
$$
这是参数曲线上的 Lamé $n=1/4$ 方程。
(21)–(23)直接支付这里的代数解；
它与周期的 $L_2^2\lambda=-X\lambda/4$ 不同，不能把两者的单值性互换。

## 5. 固定整模型和原惰性素数的全格 p-curvature

固定(20)、原 $b$ 及原有限坏集。
上述有限覆盖在原好参数点附近无分歧：
解析 theta 分支在一张完整周期片上单值且全纯，
torsion 与 $\Delta^{1/24}$ 也在 $\Delta\ne0$ 的相应固定覆盖上 étale。
代数化后，取包含全部原 CM 纤维的一个这样的开集。

把全部有限方程、根单位、(17)的 rational functions、
水平基变换矩阵及其逆 spread out。
只须再删一个固定有限整数的素因子，便得到有限 étale 整模型，
各 $h_{m,a}$ 及基变换在该开集整且可逆。
这不是一个随 $p$ 选择的 cover、分母或 frame。
若只需原指定纤维，坏集亦可由这些固定非零值的数域范数给出。
本节不主张这个固定坏集已为最小。

现在取足够大的原 $p\equiv5\pmod6$。
参数曲线(5)在剩余特征中是超奇异 $j=0$ 曲线，
其不变导子准确满足
$$
L_2^p=0.
\tag{25}
$$
例如其 Hasse 系数为
$[X^{p-1}](X^3-\Delta_0/27)^{(p-1)/2}=0$，
因为 $p-1\equiv1\pmod3$。
在有限可分函数域扩张上，导子延拓唯一；
$L_2^p$ 是导子且在基域为零，所以(25)也在上述固定 étale cover 上成立。

由水平基，
$$
\mathcal H_m\!\left(\sum_a u_a h_{m,a}\right)
=\sum_a (L_2u_a)h_{m,a}.
$$
因此有 whole 格恒等式
$$
\boxed{\mathcal H_m^p=0,\qquad
(\nabla_m^\vee)^p=0\pmod p,\qquad m\in\mathcal M.}
\tag{26}
$$
这也就是原方向上的零 $p$-curvature，因为
$\mathcal H_{L_2^{[p]}}=0$。
(26)经过可逆 étale 扩标证明，故下降回原参数格。
它包含所有奇基；不是只在一个 CM 来源或偶质量上成立。

必须区分：(26)是 mod $p$ 的完整参数连接身份，
R856 的 $\mathcal R_p$ 是该类身份与热递推相容时的实际**除 $p$** 余项。
所以(26)不能令 $\mathcal R_p$、原 Bockstein 或它的横向单位消失。

## 6. 四个原来源的真实水平坐标

令 $m_\nu=(34,72,136,66)$，并保持 R856(29)的四个原双变量提升
$\widetilde R_\nu$。在同一个固定覆盖上唯一写成
$$
\boxed{\widetilde R_\nu=\sum_{a\bmod m_\nu}
c_{\nu,a}\,h_{m_\nu,a}.}
\tag{27}
$$
所有 $c_{\nu,a}$ 都是先于 $p$ 固定的代数函数。
这只是原四个完整多项式的可逆基变换；原 $H_{112}$ 的全部因子、
共同 $A_{24}$ 的六输入和所有其它伙伴均不作截断。
原输入偶，故由(19)有 $c_{\nu,a}=c_{\nu,-a}$，但 whole 格(26)并未删除 odd 列。

对水平质量 $f_{m,a}$ 定义同一个、与 $m$ 无关的标量算子
$$
T_0=1,\quad T_{-1}=0,\qquad
\boxed{
T_{r+1}=L_2T_r-\frac{r(2r-1)}{24}g_2T_{r-1}.
}
\tag{28}
$$
这里是非交换微分算子的递推；$L_2$ 对所有右侧参数完整求导。
R855 的精确热递推和(12)给
$$
\boxed{j_{m,2r}(h_{m,a})=(2m)^rT_rf_{m,a}.}
\tag{29}
$$
例如
$T_2=L_2^2-g_2/24$，
$T_3=L_2^3-7g_2L_2/24-g_3/4$；
没有将 $T_r$ 写成冻结后的 $L_2^r$。

四个原来源恒从 $z^6$ 起、首系数一，故(27)满足以下准确相容式：
$$
\boxed{
\sum_a c_{\nu,a}f_{m_\nu,a}=0,\quad
\sum_a c_{\nu,a}L_2f_{m_\nu,a}=0,\quad
\sum_a c_{\nu,a}L_2^2f_{m_\nu,a}=0,
}
\tag{30}
$$
$$
\boxed{
\sum_a c_{\nu,a}L_2^3f_{m_\nu,a}
=\frac{720}{(2m_\nu)^3}=\frac{90}{m_\nu^3}.
}
\tag{31}
$$
这些式子在特征零参数域中成立。
尤其 $c_{\nu,a}$ 依赖参数：不能把 $L_2$ 作用进(30)后，
删掉它对 $c_{\nu,a}$ 的导数，进而错误地使(31)为零。

## 7. 同一标量高算子上的原除 p 配对

置 $N=(p+1)/2$、$H=H_p$、$C_p=L_2H$，均取 R856 的指定特征零提升。
由 R856(27)作用于每个水平列，
$$
\boxed{
T_N f_{m,a}\equiv
\chi_p(2m)\left(HL_2+\frac{C_p}{2}\right)f_{m,a}\pmod p.
}
\tag{32}
$$
其中 $\chi_p$ 是 Legendre 符号。
确切倍率来自 $(2m)^{1-N}\equiv\chi_p(2m)$。

令 $\epsilon=\chi_p(2m)\in\{1,-1\}$，定义一个有理微分算子
$$
\boxed{
\mathcal Q_{p,\epsilon}
=\frac{T_N-\epsilon(HL_2+C_p/2)}p.
}
\tag{33}
$$
它未必在所有代数函数上整；(32)严格保证它在相应
$f_{m,a}$ 上整。固定的特征零水平基、$H,C_p$ 提升与(33)的除法均不可更换。

由于(30)的前两式**准确为零**，
$$
j_{m_\nu,p+1}(\widetilde R_\nu)/p
=(2m_\nu)^N\sum_a c_{\nu,a}
\mathcal Q_{p,\epsilon_\nu}f_{m_\nu,a}
$$
是特征零整恒等式。因此原 CM 点的四条 B 行准确为
$$
\boxed{
\mathfrak B_{m_\nu,p}(\bar R_\nu)
=2m_\nu\epsilon_\nu\left.
\sum_a c_{\nu,a}\mathcal Q_{p,\epsilon_\nu}f_{m_\nu,a}
\right|_{g_2=0,\ g_3=-4b}\pmod p.
}
\tag{34}
$$
四个实际符号分别为
$$
\boxed{
\epsilon_S=\epsilon_U=\left(\frac{17}{p}\right),\qquad
\epsilon_T=1,\qquad
\epsilon_V=\left(\frac{33}{p}\right).
}
\tag{35}
$$
(34)保整个实际系数函数，未任意把四符号同一化或添加未核 ray 条件。

这里能把 $(2m)^N$ 最后约成 $2m\epsilon$，
是因为(33)的每项已经整；原高幂的任何除 $p$ 修正若乘到被减去的
$HL_2+C_p/2$ 行，也由(30)准确相消。
这不是省掉一个未知 Fermat 商。

(30)–(34)把四首行固定成同一参数曲线有限代数来源上的两种
$\epsilon$ 标量除 $p$ 算子。它没有令这些配对非零，
也没有把(30)当成可以移过(33)的标量恒零。
R856 已付的 $\mathcal R_p/g_2^2$ 同权单位，
尚须与(34)的**实际** $c_{\nu,a},f_{m_\nu,a}$ 配对建立关系；
有限水平格和(26)本身不提供这一步。

## 8. 高标量算子的准确 Riccati 余项

为显示(28)仍保何种传播，取一个新的形式变量 $v$，
它不是原角变量 $t=-b/x^3$，也不是物理 $z$。
在特征零置
$$
\mathcal K_f(v)=\sum_{r\ge0}T_rf\,\frac{v^r}{r!}.
$$
把(28)逐项相加，得到精确一阶式
$$
\boxed{
\left(1+\frac{g_2v^2}{12}\right)\partial_v\mathcal K_f
=L_2\mathcal K_f-\frac{g_2v}{24}\mathcal K_f,\qquad
\mathcal K_f(0)=f.
}
\tag{36}
$$
因而相应特征方向中的 $v$ 满足
$v'=-1-g_2v^2/12$。
若 $\lambda''=-g_2\lambda/12$，则
$v=-\lambda/\lambda'$ 正好满足这个 Riccati 式。
这解释了为什么将水平基代数化后，(28)仍不等于裸参数 Taylor 递推：
完整的周期方程及其半密度项仍在(36)中。

同一算子的准确 Gauss–Manin 矩阵、普通环与真 Hurwitz 环的不同 $p$ 次幂，已在
[原 GM 半密度与完整 Hurwitz 接口](2026-11-16-original-gauss-manin-half-density-p-curvature-and-hurwitz-interface.md)
逐项证明；其中最高 $-\partial_v^p$ 必须保留。该接口同样没有判定(41)的除 $p$ 值。

所以本注的 fixed horizontal cover 不推翻原固定 torsion 注对
$\mathcal P_{2,M}$ 真极、完整 Frobenius 资料和 CM13 frame 的结论。
一者在参数方向代数化 whole heat connection，另一者固定物理 $z$ 方向的
Cartier 输入。原四 $\alpha_\nu=-\mathfrak B_{m_\nu,p}$ 及 R853 的加权
$\mathcal C^4$ 身份逐字不变。

本注未进行数学数值运行、目标素数扫描，也未增加任何算术中央条件。

### 依赖与规范来源

- [R855](../results/R855-original-full-heat-connection-and-canonical-divided-jet.md)：
  whole 热连接、完整双变量 jet、原共同 $A_{24}$ 和四伙伴。
- [R856](../results/R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)：
  全 Hurwitz Frobenius、四指定整商及 Hasse 除 $p$ forcing。
- [R853](../results/R853-original-weighted-cartier-return-and-fixed-logarithmic-line.md) 与
  [固定 torsion 全输入](2026-11-15-fixed-torsion-connection-and-original-frobenius-initial-data.md)。
- NIST DLMF [§23.6(i), (23.6.9)](https://dlmf.nist.gov/23.6.E9) 的 sigma–theta 规范、
  [§20.7(viii)](https://dlmf.nist.gov/20.7.viii) 的 theta 变换、
  [§23.18, (23.18.5)](https://dlmf.nist.gov/23.18.E5) 的 eta 变换。
  本注将 theta 自变量明确重标为周期 $1,\tau$，在(7)–(14)写出所用全部因子；
  有限单值性、代数性、整模型和实际来源配对在正文独立支付。

## 9. 同一原纤维的水平提升：四个固定代数三零函数

上述(27)为了保原双变量提升而使用参数函数 $c_{\nu,a}$。
若只读原 CM 纤维，可以进一步准确冻结**该纤维向量的坐标**，
但不能把(30)误当成冻结后的全参数恒等式。

固定原 $b$ 及
$$
P:\ (g_2,g_3)=(0,-4b),\qquad \Delta_0=-432b^2.
$$
在第3节固定覆盖上，先于 $p$ 选定一个位于 $P$ 上的点
$\widetilde P$。它和全部固定 torsion labels、根单位同在一个固定数域中。
令
$$
\gamma_{\nu,a}=c_{\nu,a}(\widetilde P)\in\overline{\mathbf Q},\qquad
R_\nu^{\rm flat}=\sum_a\gamma_{\nu,a}h_{m_\nu,a},\qquad
f_\nu^{\rm flat}=\sum_a\gamma_{\nu,a}f_{m_\nu,a}.
\tag{37}
$$
必要的固定分母及基矩阵行列式已由第5节的同一有限坏集排除。
$\gamma_{\nu,a}$ 不随 $p$ 改变；在每个好素数只取它们的相应嵌入与约化。

由构造，
$$
\mathcal H_{m_\nu}R_\nu^{\rm flat}=0,\qquad
R_\nu^{\rm flat}|_{\widetilde P}=R_\nu .
\tag{38}
$$
物理 $z$ 导数只读这一纤维的截面，所以对**所有** $k\ge0$，
$$
\boxed{
j_{m_\nu,k}(R_\nu^{\rm flat})|_{\widetilde P}
=j_{m_\nu,k}(R_\nu).
}
\tag{39}
$$
这不是只保持一个低截断，也没有改变原 $P_{2,M}$ 或 CM13 frame 的输入。
它是用另一个参数提升表示同一个原纤维向量。

现在 $\gamma_{\nu,a}$ 是真正的常数，故可以对(37)求参数导数。
由(29)和原 $j_0=j_2=j_4=0,\ j_6=720$，
$$
\boxed{
f_\nu^{\rm flat}(\widetilde P)
=L_2f_\nu^{\rm flat}(\widetilde P)
=L_2^2f_\nu^{\rm flat}(\widetilde P)=0,\qquad
L_2^3f_\nu^{\rm flat}(\widetilde P)=\frac{90}{m_\nu^3}\ne0.
}
\tag{40}
$$
在 $\widetilde P$，$L_2g_2=-24b$ 是单位，覆盖又 étale。
因此这四个固定代数函数在参数曲线的该点都**恰三阶为零**；
排除同一固定有限坏集后，约化仍恰三阶。
它们不是任意选择的测试函数，而是(38)的原四截面唯一水平提升的质量。

令 $N=(p+1)/2$。原四个指定值现在准确写成
$$
\boxed{
\mathfrak B_{m_\nu,p}(\bar R_\nu)
=(2m_\nu)^N
\frac{(T_Nf_\nu^{\rm flat})(\widetilde P)}p
\pmod p.
}
\tag{41}
$$
这里的分子在 $\widetilde P$ 整除 $p$，由(32)、$H(P)=0$ 及(40)证明。
**不声称** $T_Nf_\nu^{\rm flat}/p$ 在全参数曲线上整。
等价的逐项整表达是
$$
\boxed{
\mathfrak B_{m_\nu,p}(\bar R_\nu)
=2m_\nu\epsilon_\nu
(\mathcal Q_{p,\epsilon_\nu}f_\nu^{\rm flat})(\widetilde P)
\pmod p,
}
\tag{42}
$$
其中(33)的 subtraction 在该点恰为零，而在整曲线上仍完整保留。

于是(41)已把原四首行放在**同一个先于 $p$ 固定的代数参数覆盖上，
四个先于 $p$ 固定、具有指定非零第三导数的函数**中读取。
没有将参数系数移动进原全参数 syzygy，也没有引入随 $p$ 自由选择的函数。
剩下的真正问题仍是这四个实际函数在
$T_N$ 的完整半密度传播及其除 $p$ 余项下是否可能同时为零。
(36)的 Riccati 部分、R856 的 $\mathcal R_p$ 及所有模 $p^2$ 初始资料继续保留；
三阶零本身不推出(41)非零。
