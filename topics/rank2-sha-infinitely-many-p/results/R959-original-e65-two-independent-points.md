# R959 — 新固定 E65 的独立点、全部局部 Schwartz 与 degree390 真来源

日期：2026-11-26。**已证明：秩至少二、全部有限角色与局部 Schwartz、真实 degree390 的非零 theta 来源和全权平方身份。** 完整66维 CM 矩阵、唯一源向量与六低 jet 的公开计算尚待执行；普通/惰性通常全 Sha 桥继续接入。本篇保持这些门的不同状态，主目标未完成。

## 1. 同一固定曲线及两个实际点

固定
$$
E_{65}/\mathbf Q:\quad y^2=x^3+65,\qquad
P=(-4,1),\quad Q=(-1,8).
\tag{1}
$$
两点直接满足原方程。以下给出不依赖秩表、BSD、数值高度或素数扫描的证明：
$$
\boxed{\operatorname{rank}E_{65}(\mathbf Q)\ge2.}
\tag{2}
$$

使用的下降域是实二次域
$$
F=\mathbf Q(r),\qquad r^2=65,\quad r>0.
\tag{3}
$$
它只是本节下降计算的域，不是后续曲线的 CM 域 $\mathbf Q(\omega)$。

## 2. 直接证明下降行是群同态

定义
$$
\delta:E_{65}(\mathbf Q)\longrightarrow F^\times/F^{\times3},
\qquad
\delta(O)=1,\quad \delta(x,y)=[y+r].
\tag{4}
$$
有限有理点的 $x,y$ 都不为零：$x=0$ 需要 $65$ 是有理平方，$y=0$ 需要 $-65$ 是有理立方。特别 $y+r\ne0$。

若一条非垂直有理弦或切线为 $y=mx+n$，其三个交点按重数记为 $R_1,R_2,R_3$。它们满足 $R_1+R_2+R_3=O$，横坐标是
$$
f(X)=X^3-(mX+n)^2+65
$$
的全部根。若 $m\ne0$，在 $X_0=-(n+r)/m$ 代入，得到 $f(X_0)=X_0^3$，因而
$$
\prod_{i=1}^{3}(y(R_i)+r)
=m^3\prod_i(x(R_i)-X_0)
=-m^3f(X_0)=(n+r)^3.
\tag{5}
$$
重根也由同一个多项式恒等式包含。若 $m=0$，三因子均为 $n+r$，(5) 仍成立。

另一方面，对任何有限有理 $R=(x,y)$，
$$
(y+r)(-y+r)=65-y^2=-x^3.
\tag{6}
$$
故 $\delta(-R)=\delta(R)^{-1}$。结合 (5)，包括切线重交及垂直线的情形，准确有
$$
\boxed{\delta(R+R')=\delta(R)\delta(R').}
\tag{7}
$$
目标是指数三群，所以此同态杀掉 $3E_{65}(\mathbf Q)$。

这只使用原曲线的全部群律，没有把某个局部检验当成完整下降像或完整 Selmer 计算。证明秩下界只需显示两个原点的像独立。

## 3. 两个二处赋值准确区分 P 的像

由于 $65$ 平方自由且 $65\equiv1\bmod4$，
$$
\mathcal O_F=\mathbf Z[\omega_F],\qquad
\omega_F=(1+r)/2,\qquad
\omega_F^2-\omega_F-16=0.
\tag{8}
$$
这里用下标区分实二次整元 $\omega_F$ 和后续的三次单位根。

最小式模二为 $X(X-1)$，两根互异。因此
$$
(2)=\mathfrak p_0\mathfrak p_1,\qquad
\mathfrak p_0=(2,\omega_F),\quad
\mathfrak p_1=(2,\omega_F-1),
$$
两素理想的范数都为二。由
$$
N_{F/\mathbf Q}(\omega_F)=-16,\qquad
\omega_F\notin\mathfrak p_1
$$
得
$$
v_{\mathfrak p_0}(\omega_F)=4,\qquad
v_{\mathfrak p_1}(\omega_F)=0.
\tag{9}
$$
这是完整理想赋值：范数只有二的因子，且另一二素理想处为单位。

原点 $P$ 的下降值为
$$
1+r=2\omega_F.
$$
故
$$
\boxed{
(v_{\mathfrak p_0}(\delta(P)),v_{\mathfrak p_1}(\delta(P)))
=(5,1)\pmod3.}
\tag{10}
$$
特别其立方类非零，且任何单位的立方类不能抵消它的非零二处赋值。

## 4. Q 的下降值是非立方根本单位

置
$$
\varepsilon=8+r,\qquad N_{F/\mathbf Q}(\varepsilon)=-1.
\tag{11}
$$
它是正单位，且 $\delta(Q)=[\varepsilon]$。下面完整证明
$$
\mathcal O_F^\times=\{\pm\varepsilon^n:n\in\mathbf Z\}.
\tag{12}
$$

若有单位 $1<u<\varepsilon$，写
$$
u=(x+yr)/2,\qquad x,y\in\mathbf Z,\quad x\equiv y\pmod2.
$$
共轭 $u'=\pm u^{-1}$，所以 $x=u+u'>0$、$yr=u-u'>0$。若范数为负一，则
$$
0<y=(u+u^{-1})/r<(\varepsilon+\varepsilon^{-1})/r=2.
$$
若范数为正一，则
$$
0<y=(u-u^{-1})/r<(\varepsilon-\varepsilon^{-1})/r
=16/r<2.
$$
因此 $y=1$。但单位范数方程给
$$
x^2-65=\pm4,
$$
即 $x^2=61$ 或 $69$，都不可能。故不存在这样的 $u$。

任意正单位乘一个 $\varepsilon$ 的整数次幂后可落在 $[1,\varepsilon)$，只能为一；再用符号和逆元处理其他单位，即得 (12)。因此 $\varepsilon$ 与 $\varepsilon^2$ 均不是 $F^\times$ 中的立方：若 $\alpha^3$ 是单位，则所有有限赋值给 $\alpha$ 也是整单位，再用 (12) 比较指数。

## 5. 两个立方类独立，且没有有理三挠

设 $a,b\in\{0,1,2\}$ 并有
$$
(1+r)^a(8+r)^b\in F^{\times3}.
\tag{13}
$$
在 $\mathfrak p_1$ 取赋值，由 (10)、(11) 得 $a\equiv0\bmod3$，故 $a=0$。再由 (12) 得 $b=0$。所以
$$
\boxed{\delta(P),\delta(Q)\text{ 在 }F^\times/F^{\times3}
\text{ 中线性独立。}}
\tag{14}
$$

还须排除把这两维错误记为有理三挠。若 $R=(x,y)\ne O$ 满足 $3R=O$，则 $2R=-R$，其切线斜率 $m=3x^2/(2y)$ 必满足
$$
x(2R)=m^2-2x=x,\qquad
9x^4=12x(x^3+65).
$$
故
$$
3x(x^3+260)=0.
\tag{15}
$$
$x=0$ 不是有理点；$x^3=-260$ 也不可能，因为一个有理数的立方在素数五处赋值是三的倍数，而 $-260$ 的五赋值为一。因此
$$
E_{65}(\mathbf Q)[3]=0.
\tag{16}
$$

由 Mordell–Weil 有限生成性，$E_{65}(\mathbf Q)/3E_{65}(\mathbf Q)$ 的 $\mathbf F_3$-维数恰为有理秩。式 (7)、(14) 表明这个商至少二维；结合 (16) 即得 (2)。两个原点也确实在自由部分独立：任何非零整数关系都可先除去两系数的共同三幂，再用 (14) 排除。

## 6. 在后续来源构造中的准确位置

原五固定曲线和原五中央没有被此新输入替换。若构造并验证 $E_{65}$ 的第六完整来源，其用途是提供一个真正不同的固定曲线输入，继续检验完整低 jet 矩阵及同源中央消费。

前五节只用原曲线证明两个点独立；以下另行证明这条曲线自己的全部有限角色、Hermitian 参数、Schwartz、degree390 来源及平方身份。三处导子与分裂十三处均直接核算，未从 E89 搬用。最后再明确列出尚待运行的整个 CM 核及后继通常 Selmer 比较门。

秩下界为显示证明，无需数学数值执行。以下局部完整有限表示与整个 CM 来源的源码另行固定；不保存可重算表。

## 7. 原 E65 的完整有限角色与 Hermitian 类

以下仍是同一 $E_{65}$，但 CM 域固定为
$K=\mathbf Q(\omega)$、$\omega^2+\omega+1=0$、
$\delta=1+2\omega$、$\delta^2=-3$，$\operatorname{Im}\delta>0$。
单位 Hecke 角色为 $\chi=\psi_{65}|\cdot|_K^{-1/2}$；
$\chi_\infty(z)=(z/|z|)^{-1}$。全局加性角色保持 R290：
$\psi_{\infty}(x)=e^{2\pi ix}$、$\psi_\ell(x)=e^{-2\pi i\{x\}_\ell}$。

### 7.1 最小导子与全部单位、uniformizer

短模型判别式为 $-432\cdot65^2$。二处用 $y=Y+1$ 得
$Y^2+2Y=X^3+64$，Tate 算法的 IV 步给 $v_2(\Delta)=4,f_2=2$；
也可由 $65\equiv1\bmod8$ 是 $\mathbf Q_2$ 中六次幂，将原 $E_1$
的完整局部模型运输过来。三处用 $x=X+1$ 得
$$
Y^2=X^3+3X^2+3X+66.
$$
$a_6$ 的三赋值是一，故为 II；$v_3(\Delta_{\min})=3$，
Ogg 公式给 $f_3=3$。五、十三处的六次扭转参数各有赋值一，
均为 II，$v_\ell(\Delta_{\min})=2,f_\ell=2$。这些判别式赋值
均小于十二，模型不可再整降。因此
$$
N(E_{65})=2^2\,3^3\,5^2\,13^2=456300,\qquad
\mathfrak f_{65}=(2\delta^2\cdot5\cdot13)=(390).
\tag{17}
$$
特别三处不能用原 E17/E89 的 $\delta$ 导子代替。

在十三处取 $\pi_{13}=4+\omega$、$\bar\pi_{13}=3-\omega$。
在 $(\pi_{13})$ 的剩余嵌入中 $\omega=9,\delta=6$；
在另一处 $\omega=3,\delta=-6$。对单位，符号
$u^2\in\mu_6$ 表示按各自剩余嵌入提升后，再取固定复嵌入。
原全部局部数据为
$$
\begin{array}{c|c|c|c}
v&\chi_v\text{ 在单位上}&\text{指定 uniformizer}&a(\chi_v)\\ \hline
2&\operatorname{Teich}_{\mu_3}(u\bmod2)&\chi_2(2)=-1&1\\
3&\chi_3(\epsilon\omega^a)=\epsilon\omega^a&
       \chi_3(\delta)=-i&2\\
5&(u\bmod5)^4\in\mu_6\subset\mathbf F_{25}&\chi_5(5)=-1&1\\
\pi_{13}&(u\bmod\pi_{13})^2\in\mu_6&
       \chi_{\pi_{13}}(\pi_{13})=-\pi_{13}/\sqrt{13}&1\\
\bar\pi_{13}&(u\bmod\bar\pi_{13})^2\in\mu_6&
       \chi_{\bar\pi_{13}}(\bar\pi_{13})=-\bar\pi_{13}/\sqrt{13}&1.
\end{array}
\tag{18}
$$
三处模 $\delta^2$ 的每个单位唯一写成 $\epsilon\omega^a$。
这里的正指数是 idèle 单位方向；Silverman–Stange §6 的理想角色
公式仍为
$\psi_{65}(\mathfrak q)/\psi_1(\mathfrak q)=(65/\mathfrak q)_6^{-1}$。

下面核定表中的绝对值，避免以两个好素数猜角色。
$65$ 在二处是六次幂，所以该分量与 E1 完全相同。
五处和十三的两个分裂素理想分别给 tame 指数四、二、二。
于是全局 $\omega$ 在二、五、十三合并处的值分别都是 $\omega$，
其乘积为一；无穷分量为 $\omega^2$，迫三处的值为 $\omega$。
全局 $-1$ 同样迫三处符号为负。全局 $\delta$ 在二、五、
十三合并处的值为 $1,-1,1$，故三处值必须是 $-i$。
全局有理数二、五给表中两个 $-1$。

最后，全局 $\pi_{13}$ 在二、三、五、另一十三处的值依次为
$\omega,-\omega^2,-\omega^2,-\omega$，乘积为 $-1$；
无穷值为 $\bar\pi_{13}/\sqrt{13}$。乘积公式给表中
$\chi_{\pi_{13}}(\pi_{13})$；共轭计算给另一值。
这同时保留了两个分裂支，未把十三处仅记为一个无方向的导子。

射线类次数为
$$
[K(\mathfrak f_{65}):K]
=\frac{(4-1)(9-3)(25-1)(13-1)^2}{6}
=10368=2^7\,3^4.
\tag{19}
$$
分母六来自完整根单位商；$K$ 类数为一。

### 7.2 根数与有意选择的有理参数

五处的单位角色 $\vartheta(z)=z^4$ 在 $\mathbf F_5^\times$
上平凡，且 $\vartheta(\delta)=-1$。原负加性角色的全 Gauss 和
是 $-5$；$\chi_5(5)=-1$ 使 epsilon 为一，dichotomy 为负。
三处和 R816 的六项和同为 $-3$，但本篇
$\chi_3(\delta)^3=i$，故 epsilon 为 $-i$，乘
$\chi_3(\delta)=-i$ 后 dichotomy 仍为负。
二处 epsilon 与 dichotomy 都为正。十三分裂处的两角色互逆，
其 epsilon 乘积为 $\chi_{\pi_{13}}(-1)=1$，而
$\chi_{13}(\delta)=1$。无穷处 epsilon 为 $i$，dichotomy 为正。
因此根数为正；在 $2,3,5,13,\infty$ 的 dichotomy 符号为
$(+,-,-,+,+)$。

$\alpha=5$ 代表这一 Hermitian 类。为取得实际小支撑，
本篇固定另一个同类代表
$$
\boxed{\alpha=15/13,\qquad
\alpha/5=N_{K/\mathbf Q}(\delta/\pi_{13}),\qquad
\kappa=|\delta^3\alpha|=45\sqrt3/13.}
\tag{20}
$$
不是把有理导子 390 当作 Hermitian 参数。
原嵌入为
$\iota_\alpha(x+y\delta)=
 \left(\begin{smallmatrix}x&9\alpha y\\-y/(3\alpha)&x\end{smallmatrix}\right)$。
下一节所有转模与 Gaussian 都使用这个同一个 $\alpha$。

## 8. 四个坏有理位的实际 Schwartz

### 8.1 二处的新偶向量

令 $e_j=\mathbf1_{j/2+2\mathbf Z_2}$，
$f_A=e_0-e_2,f_B=e_1+e_3$，$\zeta_8=e^{2\pi i/8}$。
因 $\alpha\equiv3\bmod8$，R290 的同一原积分给
$$
\mu(\omega)=-\omega^2\zeta_8^{-1},\qquad
M_\omega=-\frac{\omega^2\zeta_8^{-1}}{\sqrt2}
 \begin{pmatrix}1&\zeta_8^{-1}\\\zeta_8^{-1}&i\end{pmatrix}.
\tag{21}
$$
具体地，对输入 $v=j/2+2\mathbf Z_2$、输出 $u=b/2$，
核为
$\mu(\omega)(2\sqrt2)^{-1}
 \zeta_8^{-3\alpha(b^2+j^2-4bj)}$。
指数按二进单位模八读取。原四分之一环带的消项仍逐项成立，
所以没有漏掉外支撑。

对 R290 的完整 pro-2 生成元 $g_*=(-11+4\delta)/13$，
$\mu(g_*)=\mu(-g_*)=\zeta_8^{-1}$。
唯一非零坐标为 $a=3b+2\bmod4$，其相位是
$$
\zeta_8^{-1}\,
 \zeta_8^{-3\alpha(11a^2-26ab+11b^2)/4}.
$$
括号分子是四的倍数；四列相位准确为 $-1,1,-1,1$。
所以完整 $g_*$ 矩阵仍为 R290 的
$\left(\begin{smallmatrix}
0&0&-1&0\\0&1&0&0\\-1&0&0&0\\0&0&0&1
\end{smallmatrix}\right)$。
$\omega,-1,g_*$ 拓扑生成整个 $K_2^1$，因此
$$
\boxed{\phi_2=f_A+t_-f_B,\qquad
t_-=(\sqrt3-1)/\sqrt2,\qquad
\|\phi_2\|^2=3-\sqrt3.}
\tag{22}
$$
这不是旧 $t_+$ 向量的免费运输；(21) 直接给本篇的特征一。

### 8.2 三处必须取 even 的 $\delta^2$ 方向

原 $n((\alpha\delta/4)\psi_K)=-4$、
$L=\delta^{-2}\mathcal O_{K_3}$、$v=\delta^{-3}$。
相对基角色
$\chi_3^0(\epsilon\omega^a)=\epsilon,\chi_3^0(\delta)=-i$，
Yang 的 splitting 比平凡。原中心相位
$\psi_3(\alpha/36)=\psi_3(5/156)=\omega$。
故 R776 的全部三维矩阵仍准确为
$W_3(\omega)=\operatorname{diag}(1,\omega,\omega)$、
$W_3(-1)(f_0,f_v,f_{-v})=(f_0,f_{-v},f_v)$；
$G_2=G_3$ 在全块上平凡。

(18) 对应其 even 特征
$\tau_e(\omega)=\omega,\tau_e(-1)=1$。原 intertwiner 给
$$
\boxed{\phi_3=
 \mathbf1_{\frac19+\frac13\mathbf Z_3}
+\mathbf1_{-\frac19+\frac13\mathbf Z_3},\qquad
\|\phi_3\|^2=6.}
\tag{23}
$$
负号将改为 E−11 的 $+i$ uniformizer，不能在这里使用。

### 8.3 五处完整非分裂环面

取 $\zeta_5=e^{2\pi i/5}$、
$T_5=\{x+y\delta:x^2+3y^2=1\}\subset\mathbf F_{25}$，
基 $e_a^{(5)}=\mathbf1_{a/5+\mathbf Z_5}$。
$\beta=-\Delta(\alpha/5)=9/13\equiv3\bmod5$，所以原有限
$\mu_4$ 模型是
$$
W_5(g)_{ab}=\frac{(\frac y5)}{\sqrt5}
 \zeta_5^{\,4\{x(a^2+b^2)-2ab\}/y}\quad(y\ne0),
\qquad W_5(-1)e_a=e_{-a}.
\tag{24}
$$
完整乘法由原有限二次 Gauss 合成给出。
Hilbert90 写 $g=z^{-4}$，故 Hecke 单位角色对应
$\eta(g)=g^{-1}$；quadratic splitting 是 $g^3$。
真正不变线在 (24) 中的角色为 $\tau(g)=g^4$，不是缺失的二次角色。

令 $\Pi_5=6^{-1}\sum_{g\in T_5}\tau(g)^{-1}W_5(g)$，固定
$f_5=3\sqrt5\,\Pi_5 e_0$。四个非 $\pm1$ 元素直接给
$$
\boxed{
f_5(a)=\sqrt5\,\mathbf1_{a=0}
-\omega^2\zeta_5^{a^2}-\omega\zeta_5^{-a^2},\quad
f_5(0)=\sqrt5+1,\quad
n_5=\|\phi_5\|^2=3(5+\sqrt5),}
\tag{25}
$$
其中 $\phi_5=\sum_a f_5(a)e_a^{(5)}$。
它实、偶且非零；完整投影的秩为一。

### 8.4 十三处的两个 split 支与准确投影成本

固定 $\delta_0\in\mathbf Q_{13}$ 为 $\delta_0^2=-3$、
$\delta_0\equiv6\bmod13$ 的根，并以
$K\otimes\mathbf Q_{13}\simeq\mathbf Q_{13}\oplus\mathbf Q_{13}$
使 $\delta=(\delta_0,-\delta_0)$。
记 $\vartheta(u)=\chi_{\pi_{13}}(u)$；在单位上为模十三二次幂的
$\mu_6$ 提升，另一分量是 $\vartheta^{-1}$。
在 Yang 1997 的自然极化中，完整作用为
$$
\omega_\chi(g)\phi(y)=\vartheta(g)|g|^{1/2}\phi(yg),
\quad g\in\mathbf Q_{13}^\times.
$$
因此 $\vartheta^{-1}\mathbf1_{\mathbf Z_{13}^{\times}}$
被全部紧单位环面固定。不能声称它被非紧 uniformizer 固定；
非零赋值的作用移到不交环带，其矩阵系数为零。

用该文 (2.28) 的原 isometry
$$
\rho_\alpha\phi(x)=|A|^{1/2}\psi_{13}(Ax^2/2)
 \int\psi_{13}(Axy+Ay^2/4)\phi(y)\,dy,\qquad
A=\delta_0^3\alpha .
\tag{26}
$$
这里 $v_{13}(A)=-1$、$13A\equiv3\bmod13$。
在单位陪集上积分，非零输出恰在 $\mathbf Z_{13}$，并对
$13\mathbf Z_{13}$ 平移不变。全有限块因此是
$$
e_a^{(13)}=\mathbf1_{a+13\mathbf Z_{13}},\qquad a\in\mathbf F_{13},
\tag{27}
$$
每个基向量的平方范数为 $1/13$，不是一。
例如在这个块上，(26) 的全部坐标是
$$
13^{-1/2}\zeta_{13}^{5a^2}
 \sum_{b\in\mathbf F_{13}^{\times}}
 \vartheta(b)^{-1}\zeta_{13}^{9b^2-3ab}.
\tag{28}
$$
这是一条实线乘一个共同非零标量，不是逐坐标任意取实部。

把 split 环面写成 $t=x+6y\in\mathbf F_{13}^{\times}$。
原 $\mu_4$ 有限模型为
$$
W_{13}(g)_{ab}=\frac{(\frac y{13})}{\sqrt{13}}\,
 \zeta_{13}^{\,3\{x(a^2+b^2)-2ab\}/y}\quad(y\ne0),
\qquad W_{13}(-1)e_a=e_{-a}.
\tag{29}
$$
其自然极化的二次 splitting 为 $t^6$，而真实单位角色为
$t^2$；故 (28) 的线在 (29) 上的特征准确为 $\tau(t)=t^4$。
split 有限 Weil 表示的二次角色重数二，其余角色重数一；
这里是非二次角色。

取 $g_0=(11,5)$，即 $t=2$，它的阶为十二，
$\tau(g_0)=\omega^2$。令
$\Pi_{13}=12^{-1}\sum_{j=0}^{11}\omega^jW_{13}(g_0^j)$、
$f_{13}=6\sqrt{13}\,\Pi_{13}e_0$。前五个非中央幂的
$(\frac y{13})$ 是 $(-1,-1,1,-1,-1)$，
$3x/y$ 是 $(4,10,0,3,9)$，故准确有
$$
\boxed{\begin{aligned}
f_{13}(a)={}&\sqrt{13}\,\mathbf1_{a=0}+1\\
&-\omega(\zeta_{13}^{4a^2}+\zeta_{13}^{3a^2})
-\omega^2(\zeta_{13}^{10a^2}+\zeta_{13}^{9a^2}),\\
f_{13}(0)={}&\sqrt{13}+3,\qquad
n_{13}:=\|\phi_{13}\|^2=\frac{6(13+3\sqrt{13})}{13},
\end{aligned}}
\tag{30}
$$
$\phi_{13}=\sum_a f_{13}(a)e_a^{(13)}$。
配对指数证明它实且偶；零坐标非零直接支付原投影非零。
(26)–(29) 以及一维性将此线准确认回原两个 split 支。

还须保 Yang 的局部范数常数。
该文 Corollary2.13 的原单位范数向量是
$\sqrt{13}\,\mathbf1_{1+13\mathbf Z_{13}}$。
将其在完整紧单位群上平均，得到
$(\sqrt{13}/12)\vartheta^{-1}\mathbf1_{\mathbf Z_{13}^{\times}}$，
其平方范数为 $1/12$；平均不改变 theta 积分。
把投影归一到范数一，theta 积分因而乘 $\sqrt{12}$。
Theorem1.11 原 split 因子
$13^{-1}(1-13^{-1})^{-2}=13/144$ 必须同时乘十二，
成为
$$
\boxed{c_{13}(0)=13/12.}
\tag{31}
$$
本篇既没有漏掉十二，也没有把 split 处当成非分裂的缺失二次角色。

## 9. 真正 degree390、全权实平方与原中央质量

置 $v_2=(1,t_-,-1,t_-)$、$v_3=(0,1,1)$。
上述原支撑的有理点恰为 $x=n/90$，四个实际坐标依次为
$$
2x\leftrightarrow n\bmod4,\qquad
9x\leftrightarrow n\bmod3,\qquad
5x\leftrightarrow2n\bmod5,\qquad
x\leftrightarrow-n\bmod13.
$$
定义完整系数
$$
a_n=v_2(n\bmod4)v_3(n\bmod3)
       f_5(2n\bmod5)f_{13}(-n\bmod13).
\tag{32}
$$
CRT 与 (22)–(30) 给它们不全零，并准确满足
$$
a_{-n}=a_n=\overline{a_n},\qquad
a_{n+780}=a_n,\qquad
(-1)^na_{n+390}=-a_n.
\tag{33}
$$
令 $s_0=(1-\omega)^{-1}$、$\Lambda=\mathbf Z+s_0\mathbf Z$，
$$
F(Z)=\sum_{n\in\mathbf Z}a_n
 \exp\!\left(\pi i\frac{\delta}{3}\frac{n^2}{780}+2\pi inZ\right),
\qquad S_{\rm raw}(Z)=e^{390\sqrt3\pi Z^2}F(Z).
\tag{34}
$$
换指标得
$F(Z+1)=F(Z)$、
$F(Z+s_0)=e^{-390\pi i s_0-780\pi iZ}F(Z)$。
故 $S_{\rm raw}$ 是标准 $\mathcal O(390[0])$ 的非零截面，
没有 flat twist。真实 Gaussian charge 为 $195$；不是候选65。

用 $\sum H_m(x)T^m/m!=e^{xT-T^2/(8\pi)}$，
置
$$
b_m=\sum_n a_nH_m(\sqrt\kappa\,n/90)e^{-\pi\kappa n^2/90^2},
\qquad h=\sqrt\kappa/(180\pi i).
$$
则
$$
\sum_m b_mT^m/m!=S_{\rm raw}(hT),\qquad
390\sqrt3\pi h^2=-1/(8\pi).
\tag{35}
$$
原全局 $\mu_6$ 和四处真实不变性给 $b_m=0$ 若 $6\nmid m$；
所有 $b_m$ 为实数。

对 $6\mid m$，(18) 的所有坏单位角色保持。
三处 uniformizer 由 $m$ 偶保持；十三处的非紧 uniformizer
确实随 $2m+1$ 改变，不能说它不变。
但是 (26) 的单位环带和其矩阵系数只使用同一个单位角色，
并在所有非零赋值环带为零，所以同一 Schwartz 与 (31)
仍完整适用，未删除那两个实际 uniformizer。

记
$$
n_2=3-\sqrt3,\quad n_3=6,\quad
c(0)=(1+1/2)^{-1}(1+1/5)^{-1}(1-1/13)^{-1}
=65/108.
$$
完整范数为
$$
\mathcal N_m=\frac{n_2n_3n_5n_{13}}{\sqrt{2\kappa}}\,
             \frac{m!}{(4\pi)^m}.
$$
$K$ 类数一，原紧子群体积积与商体积比为六。
Yang Theorems1.11、2.6、2.15 加上已付 (31) 给
$$
\boxed{
L(\psi_{65}^{\,2m+1},m+1)
=C_{65}\frac{(4\pi)^m}{m!}\,b_m^2,\qquad
C_{65}=\frac{2}{6c(0)}
 \frac{\pi}{3\sqrt3}
 \frac{\sqrt{2\kappa}}{n_2n_3n_5n_{13}}>0.}
\tag{36}
$$
这是同一实来源的完整平方，不是模单位的逐权式。
原秩下界与 Rubin 的 CM rank-zero 方向给
$L(E_{65},1)=0$，所以 $b_0=0$，实际来源从至少六阶起。

## 10. 有限完整 CM 识别的准确入口

在 $E_1:y^2=x^3+1$、$dz=dx/(2y)$ 上，原标准 type0 全空间为
$$
\mathcal V_{390}
=\sigma^{390}K[X]_{\le65},\qquad X=x^3,\qquad
\dim_K\mathcal V_{390}=66 .
\tag{37}
$$
第六十六列是质量列，不能删掉。
本篇的真实来源线在这个全空间内。

这条线先于待运行矩阵已是代数的，具体比较如下。
在标准 $\tau=s_0$、degree390 Fourier frame 中置
$
d_n=a_n\zeta_{1560}^{-n^2}.
\tag{37a}
$
因为标准指数 $\pi i s_0n^2/390$ 与 (34) 的指数相差
$\pi i n^2/780$，这恰是同一解析来源的坐标变换。
(33) 给 $d_{n+390}=d_n$；全部390个坐标都在一个固定代数数域中。
原 $1/390$ 和 $s_0/390$ 平移在这组有限坐标中由根单位对角矩阵
和循环移位表示，交换子为原 primitive $390$ 次单位根。

在同一实际椭圆曲线 $E_1$ 及其真实390挠点上，
$\mathcal L=\mathcal O(390[0])$ 的 theta group 定义在
$\overline{\mathbf Q}$；原平移的提升也可在该域选择。
各提升乘一个代数390次根，使其390次幂与上述解析提升准确一致。
两个对应提升的比遂为390次根，仍代数。完整390维 Heisenberg
表示绝对不可约：根单位对角矩阵有390个互异特征值，循环移位
传递地置换全部特征线。故两模型间 intertwiner 的 Hom 由代数
线性方程给出一维空间。真实解析 Fourier 同构是其中非零元，
只差一个共同复标量于代数 intertwiner。于是整个代数坐标向量
$(d_r)_{0\le r<390}$ 给出 $H^0(E_1,\mathcal L)$ 中的代数线。
Gaussian 只是同一线丛的 frame 变换；此证明不使用待计算的共同核、
六低 jet 或 Katz 身份，也不把分析的 $C_{\rm raw}$ 本身称为代数数。

取原 $\gamma_7=3+\omega$、$\gamma_{19}=4+\delta$，
$\mathscr N_\gamma=[\gamma]_*[\bar\gamma]^*/\gamma$。
它们的整个66列使用原 sigma division 比的390次方和完整纤维迹：
$$
\left.\frac{\mathscr N_\gamma(\sigma^{390}P(X))}
 {\sigma^{390}}\right|_{x=a}
=\gamma^{-1}\operatorname{Tr}_{(N_\gamma-aD_\gamma)^{\rm monic}}
 [(Q_{\bar\gamma}/Q_\gamma)^{390}P(x(\bar\gamma z)^3)].
\tag{38}
$$
$66$ 个固定全纤维 $a=1,\ldots,66$ 和两个额外完整返回纤维
$a=67,68$ 逐列确定并回核矩阵；真实 pull/trace 稳定性付其次数帽。
Norm13 是本曲线的坏处，不能代替 norm19。

绝对本征值也可先核，免以计算谱选择一个新来源。
R400 的完整平方—整测度引理适用于 (36) 的所有六次权。
在好普通七、十九处，代数线先整体清一次有限分母，使原 sigma
来源整；固定缩放不改变原核心身份。原质量与 Katz 单位质量
都为零，故该引理消去全部 Dirac 项。
同一原 trace 身份因此给
$\mathscr N_\gamma\Phi=(\psi_{65}((\gamma))/\gamma)\Phi$。
这里 $\mu_6$ type0 使改变 $\gamma$ 的根单位不改变未除 $\gamma$
的实际 pull/trace；全部 sigma carrier 同时改变，不能只改函数值。

具体地，
$\psi_1((3+\omega))=\omega(3+\omega)$，且模该素理想
$\omega=4,\ 65\equiv2=\omega^2$，所以
$\psi_{65}((3+\omega))/(3+\omega)=\omega^2$。
对 $4+\delta$，它已是原 primary 生成元，模该素理想
$\omega=7,\ 65\equiv8,\ 8^3=-1$，故另一单位是 $-1$：
$$
\boxed{\mathscr N_7\Phi=\omega^2\Phi,\qquad
       \mathscr N_{19}\Phi=-\Phi.}
\tag{39}
$$
这使用 (18)、(36) 的同一算术来源；不是只数两个 Frobenius
就冒充完整局部证明。

待公开运行的精确门为：全矩阵交换；(39) 的完整共同核恰为一维；
该核归一后全部系数有理，$X^{65}$ 系数零、$X^{64}$ 系数一；
全部66坐标回乘两矩阵；随后重生原五来源并核真实六低 jet
行列式非零。本节目前没有预记这些有限门为 PASS。
若共同核不止一维，必须继续加实际完整算子或本地 projector，
不能任选核向量作为 $\Phi$。

一旦这些门实际通过，令其全向量为 $(c_0,\ldots,c_{64},0)$。
准确齐次来源为
$$
F_{65,b}(z)=\sigma_b^{390}
 \sum_{j=0}^{64}c_j b^{64-j}x_b^{3j}
=b^{-1}F_{65,1}(b^{1/6}z).
\tag{40}
$$
其物理来源为 $b=65$；共同 $E_1$ 上的真实角权为195。
首项归一给 $[z^6]=1$；全部原点阶、系数及低 jet 仍须由上述
公开完整回执读取，而非本文凭维数宣称。

## 11. 新 split 坏处在后继原 Selmer 比较中的费用

本节只先把新十三处的费用付清，不提前宣告第六中央或其独立性。
普通与惰性桥可沿 R820/R943 的同一完整模板继续，但都必须保持
degree390、(18)、(19)、(31) 和真实微分缩放。

真正复周期为 $\varpi_{65}=s_0\Omega_{65}$。
(35)–(36) 的前一步尺度是 $1170^{-m}$，再用
$s_0^{2m}=3^{-m}$ 才得到
$$
\mathscr E_{65,m}
=\frac{\kappa_{65}}{s_0}\,390^{-m}s_m^2,\qquad
\kappa_{65}=C_{65}C_{\rm raw}^2/\Omega_{65}\ne0 .
\tag{41}
$$
在首个非零代数 Taylor 系数处用 CM 临界值代数性，
给固定 $\kappa_{65}\in\overline{\mathbf Q}^{\times}$；
其实际 $p$ 赋值始终保留。

参考 $E_1$ 在十三处是好分裂约化，不再有旧惰性坏处的恒定
Euler 因子。写
$\rho=\psi_1((\pi_{13}))=-\omega^2\pi_{13}$，
$\rho\bar\rho=13$、$\rho+\bar\rho=2$，其完整原因子为
$$
E_{13}(m)=
 (1-\rho^{2m+1}/13^{m+1})
 (1-\bar\rho^{2m+1}/13^{m+1}).
\tag{42}
$$
普通 $p$ 时取 $p-1\mid m$，惰性 $p$ 时取 $p+1\mid m$；
在当前 CM 嵌入内 $(\rho/\bar\rho)^m\equiv1\bmod p$。
故对整条各自允许的权支，
$$
\boxed{E_{13}(m)\equiv E_{13}(0)=12/13\bmod p.}
\tag{43}
$$
所以在 $p>211$ 它为单位，但不是常数，也没有被删除。
参考五处的完整因子为 $6/5$。射线度10368、这两个中心因子、
固定坏位与六次微分缩放都在统一有限坏集之外为单位。
因此新 split 处不会制造未付的随权非单位费用。

后继仍须在实际完整来源及六低 jet 回执通过后，将
(41)–(43) 接到相同的普通 Katz 分支、惰性完整 signed 格和
全部通常 Selmer 余秩；不能以本节的单位估计代替这些身份。
本节没有把中央泛函当成来源环上的乘法同态。

### 本次新增的原文依据

- Yang, *Theta liftings and Hecke L-functions* (1997)，Theorem1.11、
  §2.2 的 Corollaries2.10、2.13–2.14 及 (2.28)–(2.30)；
  split 投影的十二因子由正文直接计算：
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- Yang, *Eigenfunctions of the Weil representation of unitary group of
  one variable* (1998)，完整 finite Weil 和 lattice 模型：
  <https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>。
- Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic
  curves* (1999)，§1、Appendix 的原 splitting 与转模：
  <https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- Silverman–Stange，§6、Theorem19 证明的原六次剩余公式：
  <https://arxiv.org/pdf/0912.1831>。
- R290、R776、R400：分别为二处完整原积分、三处全部 even/odd
  方向，以及全平方恢复原普通 core 的完整论证。


## 12. 本次原输入公开执行的固定源码

本次只执行原 E65 的完整局部表示、两个66列 CM 算子，以及同次
重生旧 E89 后的真实六低 jet；不启动第二份原306正规化。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `scripts/original_e65_local_schwartz.py` | 13148 | `b13ad04a3b12dd28e4e749a9b92f9bd3fcfe6bc976201f1057a5a58cf8c765d5` |
| `scripts/check-original-e65-full-cm-sixth-axis.py` | 14844 | `3b86818494ee50fd84cc6f3f8cc3a3cd9d4a35bae10b598ba860b188b54caf1e` |
| `ci/e65-full-cm-source-request.json` | 762 | `622e86a14a11cafd3b71f33cdde7694e66f9428e04bb1d916d1d153c26801ce1` |
| `.github/workflows/rank2-sha-e65-full-cm-source.yml` | 5427 | `cd45a4d981a544bdedb9e39de7b1d0672e04b95088b7f9d4d8c9d583d655e41c` |

前三路径相对本课题。request固定degree390、CM7/19、4 workers、
python-flint0.9.0、同次完整 E89 重建及六实际轴独立门。
全部10源含 workflow/request 进入 manifest，8份 Python 源先做
AST 读取；六个旧依赖与新 local helper 的 SHA256 在主程序中逐项核定。
每个算子用68条完整原纤维，保66×66全矩阵和两条额外返回；
共同核由完整264×132有理矩阵忠实读取，全部实/虚行及所有核向量回乘。
只在共同 $K$ 线确为一维、首阶为六、全系数有理后才归一源向量。
旧 E89 的29项系数只由本次子进程完整 CM 生产器取得，不读旧输出表。
局部检查先核所有完整有限环面矩阵、投影、十三处真实 $\rho_\alpha$
全部13坐标返回与原 Haar 范数。尚无实际 PASS 回执；源码不代结果。
