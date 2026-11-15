# R790：原 CM 纤维的正则化、155 项共同零界与无二挠扩域的准确求值核

日期：2026-11-15。状态：**本篇的原框架、共同零界和有限代数求值公式已证明；具体 CM 数值必须由公开 Actions 的实际输出另行登记。**

本篇接 R786/R787 的同一个原第4号、次数1206的函数恢复。
保持 R738 的 $c_1=4424$、原 $g_\star$、R735 的 $b$、R751 的 $U,\xi$ 和原 $P_1$ 分支。
目标是准确评价原 $y$，进而继续原 $\beta$ 与高度输入；不重新分类 $p=41$ 有理点。
原 $y$ 单独不能选定 $x$ 的三个 CM 方向，本篇也不把 $y(c_1)$ 冒作已经得到完整 $\beta$ 点或高度。

## 1. 五次截面在 CM 点的普通值均为零

沿用 R767：
$$
\mathcal L=K_Y+\mathcal D,\qquad
V_5=H^0(Y_L,5\mathcal L),\qquad
\deg(5\mathcal L)=1360.
$$
原 $P_1$ 是 $Y$ 的阶3椭圆点。
取其上半平面局部参数 $z$，粗参数为 $w=z^3$。
一个权二形式 $T\in M_2=H^0(\mathcal L)$，作为粗曲线的微分正则，
故在上半平面以 $d\tau$ 为框架时有
$$
\operatorname{ord}_{z=0}T\ge2.
\tag{790.1}
$$
五个这样的形式的普通乘积至少消失十阶。
所以 R786 的五次分子、分母即使在粗曲线纤维均非零，
直接代入上半平面的模形式值仍会同时得到零。
这不是原函数在 $P_1$ 的真实不定性，而是框架本身的零。

$E_4$ 在该上半平面点恰简单零，$E_6$ 非零。
因此对每个原权二基 $T_j$ 定义
$$
\psi_j=\frac{T_jE_6}{E_4^2}.
\tag{790.2}
$$
它是原 $Y_K$ 上的权零模函数，在 $P_1$ 正则。
它的乘积给 $5\mathcal L$ 在该点的一个真实局部平凡化。
若 $F_\nu=T_{j_1}\cdots T_{j_5}$ 是 R786 保存的原 recipe，
则
$$
\Psi_\nu=\psi_{j_1}\cdots\psi_{j_5}
=F_\nu\left(\frac{E_6}{E_4^2}\right)^5.
\tag{790.3}
$$
两侧的乘子相同，故 $A/B$ 不变；原 recipe 的所有标量、半迹和行列式系数仍须原样保留。

一个可独立核对的二阶公式是
$$
\psi_j(P_1)
=\frac92\,\frac{(\partial_4\partial_2T_j)(P_1)}{E_6(P_1)},
\qquad
\partial_k=\frac1{2\pi i}\frac d{d\tau}-\frac{k}{12}E_2.
\tag{790.4}
$$
事实上 $T_j$ 和其一次导数在点处均零，
所以 $\partial_4\partial_2T_j$ 在点处就是普通二次模导数。
Ramanujan 恒等式给 $\partial_4E_4=-E_6/3$，
而 $E_4$ 自身在点处为零。
对 $T_j/E_4^2$ 取二次首项之比，恰得 $9/2$。
这里没有将未知的 $E_2$ 数值省略；其全部系数都乘到已证为零的项。

## 2. 原标记矩阵在 Y 上确实可消去

原 R738/R745 保存
$$
g_\star=
\begin{pmatrix}15130&123\\123&1\end{pmatrix}
=
\begin{pmatrix}1+123^2&123\\123&1\end{pmatrix},
\qquad c_1:\tau=g_\star(\zeta).
$$
因为 $123=3\cdot41$，
$$
g_\star\bmod41=I,\qquad
g_\star\bmod2=
C=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\tag{790.5}
$$
R767 的原群恰要求模2落在 $\langle C\rangle$、
模41落在原非分裂正规化子的 determinant-one 部分。
所以 $g_\star\in\Gamma_Y$。
对本篇的权零函数准确有
$$
\psi_j(g_\star\zeta)=\psi_j(\zeta),\qquad
\Psi_\nu(g_\star\zeta)=\Psi_\nu(\zeta).
\tag{790.6}
$$
这是原商曲线上的真实群作用，不是另换一个 CM place。

这一结论只消去已下降到 $Y$ 的权零求值运输。
原 $X_1$ 上的 $h$、R745 的一次 $\zeta^2$ 运输以及
$dx/(2y)=h$ 的方向仍保留。
不能用 (790.6) 将 $H^3$ 的三个立方根方向任意置换。

## 3. 任意恢复关系的共同消失阶至多154

令 $y$ 为原函数，$E_y=(y)_\infty$，$\deg E_y=1206$。
对任意已准确认证的非零关系
$$
A=yB,\qquad A,B\in V_5,\qquad B\ne0,
$$
令
$$
Z=\operatorname{div}_{5\mathcal L}(B)-E_y.
$$
$Z$ 有效，且
$$
\deg Z=1360-1206=154.
\tag{790.7}
$$

**定理 790.1。** 在任意几何点 $P$，
$$
\min\{\operatorname{ord}_{5\mathcal L,P}A,
       \operatorname{ord}_{5\mathcal L,P}B\}
=\operatorname{ord}_P Z\le154.
\tag{790.8}
$$

**证明。** 写 $e=\max(0,-\operatorname{ord}_Py)$ 和 $r=\operatorname{ord}_PZ$。
则 $\operatorname{ord}B=e+r$，
$\operatorname{ord}A=e+r+\operatorname{ord}y$。
若 $y$ 有极点，后者为 $r$；若 $y$ 正则，前者为 $r$。
两种情形均给 (790.8)。$\square$

将 $A,B$ 同时乘 (790.3) 的局部单位框架，记所得正则函数为
$\widetilde A,\widetilde B$。
在原 $P_1$ 的粗参数 $w$ 下计算
$$
\widetilde A,\widetilde B\pmod{w^{155}}.
\tag{790.9}
$$
必能找到最小 $r\le154$，使
$(a_r,b_r)\ne(0,0)$。
准确结论如下：

- 若 $b_r\ne0$，原 $y(P_1)=a_r/b_r$，允许 $a_r=0$；
- 若 $b_r=0$、$a_r\ne0$，原 $y$ 在该点有极点，所以原椭圆映射把 $c_1$ 送到 $O$。

不需要预先假设 $\beta$ 有限、非挠，或者所选 R787 分母在该点非零。
这里不是等到两个单独截面各自可能的1360阶消失全部展开；
原关系使其共同消失阶只剩154。

在上半平面或者任一准确的 stack 变形参数上，
粗参数的阶为3，所以两者的首次非零项至多在462阶。
先按 (790.2) 除掉 $T_j$ 的两阶框架零后，
各个 $T_j$ 需要的最高变形阶至多为464。
初次只算到二阶即可取得所有 $\psi_j(P_1)$；
只有原实际分子、分母的这些值同时为零，才继续生成尚缺的 jet。

## 4. 留在原 K(U) 的 CM 变形

仍用 R732/R751 的原
$$
E_0:y^2=x^3-1,\qquad
P_*=\Omega_0/41,\quad Q_*=[\zeta]P_*,
\qquad \Omega_0>0,
$$
其中 $P_*$ 是靠近原点且 $y<0$ 的实41挠点。
R751 已把
$$
U=-4/x(P_*)^3
$$
识别为 R735 的同一个280次商坐标，
其首一模数和原复分支均已由成功 producer 给出。

设
$$
\mathscr M=K(U),\qquad B_0=U/4,\qquad d_0=1+B_0.
$$
$d_0\ne0$，否则 $P_*$ 同时为二挠点；$B_0\ne0$ 也已知。
在 $\mathscr M[[\varepsilon]]$ 上使用
$$
\mathscr E_\varepsilon:\quad
d_0v^2=r^3+\varepsilon r+B_0,
\qquad \omega_\varepsilon=\frac{dr}{2d_0v}.
\tag{790.10}
$$
在 $\varepsilon=0$，$P_*=(r,v)=(1,1)$、$Q_*=(\zeta,1)$。
这来自同时除以原 $x(P_*),y(P_*)$ 的准确坐标比较；
所有权零函数不依赖被消去的共同非零微分尺度。

$[41]$ 在特征零可分，所以原两个41挠点各有唯一形式延拓。
可先用原41除法方程在 $r=1$ 的简单根作 Hensel 提升，
再由曲线方程取常数项为1的 $v$。
若第一点写成 $(r(\varepsilon),v(\varepsilon))$，
第二点不需另做一次根选择：
$$
Q(\varepsilon)=
\bigl(\zeta r(\zeta\varepsilon),\,v(\zeta\varepsilon)\bigr).
\tag{790.11}
$$
代入 (790.10) 以及唯一性即可证明它是原 $Q_*$ 的延拓。
所有原标签 $aQ+bP$ 用同一形式群法生成。

这里须保留 Fourier 规范的六权负号。
对格 $\Omega(\mathbb Z+\tau\mathbb Z)$，本篇统一定义
$$
F_{\rm alg}=(2\pi i/\Omega)^kF(\tau)
$$
为权 $k$ 形式的代数求值。
由 $g_2=4\pi^4E_4/(3\Omega^4)$、$g_3=8\pi^6E_6/(27\Omega^6)$，
以及 $c_4=12g_2,c_6=216g_3$，准确有
$$
(E_4)_{\rm alg}=c_4,\qquad (E_6)_{\rm alg}=-c_6.
$$
第二个负号来自 $i^6=-1$，不能用 Tate 的 $c_6$ 直接替换标准 Fourier $E_6$。
短 Weierstrass 坐标为 $X=d_0r,Y=d_0^2v$，因而
$$
c_4=-48d_0^2\varepsilon,\qquad
c_6=-864d_0^3B_0,
$$
$$
\frac{(E_6)_{\rm alg}}{(E_4)_{\rm alg}^2}
=\frac{-c_6}{c_4^2}
=\frac{3B_0}{8d_0}\varepsilon^{-2}.
\tag{790.12}
$$
这正是 (790.2) 的代数框架。
若 $\mathcal T_j(\varepsilon)$ 表示原 $T_j$ 对
$(\mathscr E_\varepsilon,\omega_\varepsilon)$ 的代数权二求值，则
$$
\boxed{\quad
\psi_j(\varepsilon)
=\frac{3B_0}{8d_0}\,
 \frac{\mathcal T_j(\varepsilon)}{\varepsilon^2}.
\quad}
\tag{790.13}
$$
准确检查 $\mathcal T_j$ 的常数项、一次项都为零后才能除以 $\varepsilon^2$。

该变形的粗 $j$ 参数为
$$
j(\varepsilon)
=\frac{6912\varepsilon^3}{4\varepsilon^3+27B_0^2}.
$$
在原分支上 $j=6912t(1-t)$、$t(P_1)=1$。
原 $X_1$ 的点 $c_1$ 取 $a=1$，置 $z=a-1$，则 $t=(1+z)^3$。
准确比较首项得到
$$
t-1=-\frac{\varepsilon^3}{27B_0^2}+O(\varepsilon^6),\qquad
z=-\frac{\varepsilon^3}{81B_0^2}+O(\varepsilon^6).
\tag{790.13a}
$$
因此对该点正则的原 $y$，
$$
\left.\frac{dy}{dz}\right|_{c_1}
=-81B_0^2\,[\varepsilon^3]y(\varepsilon).
\tag{790.13b}
$$
原函数在此只通过这个粗参数，不能把 $\varepsilon$ 当作 $a-1$。
因此 (790.8) 的上半平面464阶界同样适用于 (790.10)；
无需把此依赖 $U$ 的参数误称为原有理粗参数。

若还需要一阶导数，除去实际共同零阶 $r\le154$ 后必须多保留一个粗系数。
故 $\widetilde A,\widetilde B$ 至粗参数155阶（共156项）足够，
相应的 $T_j$ 需要至 $\varepsilon^{467}$；
只有 $r=0$ 的实际分母非零时，初始 $T_j$ 至五阶就同时给值与一阶。
这项扩展只给 $y$ 的一阶，不替代原 $h$ 的实际首项。

## 5. 41 挠点的权一值由短有限群法给出

对原 invariant differential，把权一 Eisenstein 值归一为
$$
e(R)=-\mathcal E(R),
$$
其中 $\mathcal E$ 指对应格的完整周期 zeta。
离开 CM 中心后必须使用
$$
\mathcal E_\Lambda(z)
=\zeta_\Lambda(z)-e_2^*(\Lambda)z-\bar z/A_\Lambda.
$$
只有 CM 中心才因三次旋转有 $e_2^*=0$。
不能把 R732 在该中心的简式直接沿 $\varepsilon$ 微分。
本篇在变形中以完整周期性、奇性和下面的有限41倍加法确定挠点值；
两项线性完成化都在加法差中精确消去，因此从不需要另算 $e_2^*$。
这等于 Zywina 权一 Fourier 规范的代数求值：
在 Tate cusp 的 $a=0$ 情形，
$(2\pi i)E^{(1)}_{0,b}$ 的常数就是负的周期 cotangent。
以下每个公式保留同一微分尺度。

完成化的线性项在加法式中准确相消，所以
$$
e(R+S)=e(R)+e(S)-m(R,S),
\tag{790.14}
$$
其中 $m$ 是短 Weierstrass 坐标中的割线或切线斜率。
对非零41挠点 $R$，沿二进制乘法求 $[40]R$，
同时由 (790.14) 保留
$$
e([40]R)=40e(R)-M_{40}(R).
$$
因 $[40]R=-R$、$e(-R)=-e(R)$，
$$
\boxed{\quad e(R)=M_{40}(R)/41.\quad}
\tag{790.15}
$$
这里 $M_{40}$ 只由有限次原群法斜率给出。
中间非零整数倍均不是二挠点，且不需要在最后一步对 $O$ 求割线。
这避免为每个新 jet 展开一个全82除法多项式。
它不删掉原完成化常数；(790.14) 正是包含它后得到的恒等式。

对于 (790.10)，若 $R=(r_R,v_R)$、$S=(r_S,v_S)$，
原斜率准确为
$$
m(R,S)=d_0\frac{v_S-v_R}{r_S-r_R}
$$
或在切线情形为
$$
m(R,R)=\frac{3r_R^2+\varepsilon}{2v_R}.
\tag{790.16}
$$
按原标签判断相等、相反、$O$ 等群法分支，不能删除分母为零的候选。

## 6. 先作原模2 C3 迹，完全消去二挠点扩域

level82 标签 $(a,b)$ 对应
$$
\frac{a\zeta+b}{82}
=
21\frac{a\zeta+b}{41}
+\frac{a\zeta+b}{2}
\pmod{\mathcal O_K}.
\tag{790.17}
$$
所以其41部分为 $R=[21](aQ+bP)$，
二部分由 $(a,b)\bmod2$ 决定。
原行列式相位仍为 $\xi_{82}=-\xi_{41}^{21}$；
$\xi_{41}$ 直接读取 R754 已完成的同向 Weil pairing，
不另选一个本原根。

设二挠点的三个 $r$ 坐标为 $z_0,z_1,z_2$：
$$
z_i^3+\varepsilon z_i+B_0=0,
$$
并按 $\varepsilon=0$ 的
$(z_0,z_1,z_2)=(c,\zeta c,\zeta^2c)$ 排序，
$c^3=-B_0$。
这对应原标签
$$
(0,1)\leftrightarrow z_0,\quad
(1,0)\leftrightarrow z_1,\quad
(1,1)\leftrightarrow z_2.
\tag{790.18}
$$
令
$$
\delta=(z_0-z_1)(z_1-z_2)(z_2-z_0)
=3sB_0\sqrt{1+\frac{4\varepsilon^3}{27B_0^2}},
\tag{790.19}
$$
平方根的常数项规定为1。
此 $\delta$ 全部在 $\mathscr M[[\varepsilon]]$ 中。
相应的原 eta 分支是
$$
\bigl(\eta_{\rm Ded}^{12}\bigr)_{\rm alg}=-4d_0^3\delta,\qquad
\left.\frac{E_6}{\eta_{\rm Ded}^{12}}\right|_{\varepsilon=0}
=\frac{864d_0^3B_0}{-12sd_0^3B_0}=24s.
\tag{790.20}
$$
它正是 R767 的 $P_1$，不是 $P_0$。
$\delta$ 的反号会交换这个原 level2 分支，不能任取。
该 eta 符号也可直接从原实周期核对：$\tau=\zeta$ 时
$\eta_{\rm Ded}^{12}=e^{\pi i\zeta}\prod_{n\ge1}(1-e^{2\pi in\zeta})^{12}$
为负虚数，乘 $(2\pi i/\Omega_0)^6$ 后为正虚数；
原 $E_0$ 的三根 $(1,\zeta,\zeta^2)$ 给 $\delta=-3s$，故确为 $-4\delta$。

二挠点的权一值为零。
对非零41挠点 $R=(r,v)$，(790.14) 给
$$
e(R+T_i)=e(R)-\frac{d_0v}{r-z_i}.
\tag{790.21}
$$
若41部分为 $O$，原82标签是 $O$ 或二挠点，权一值直接为零。

原 $H_{82}/\{\pm I\}$ 为模2的 $C_3$ 与原模41的42个半群代表之积。
因此每个原 Eisenstein 对的迹，可先对三个 $T_i$ 作同时循环和。
这不是引入新的平均；它恰是原126项中已经存在的三项分组。

写
$$
F(r)=r^3+\varepsilon r+B_0=d_0v^2,\qquad
L(r)=\frac{3r^2+\varepsilon}{F(r)}.
$$
对两个非零41部分 $R=(r,v)$、$S=(u,w)$，有
$$
\sum_i\frac1{r-z_i}=L(r),
$$
以及
$$
\sum_i\frac1{(r-z_i)(u-z_i)}
=\frac{N_0(r,u)}{F(r)F(u)},
\tag{790.22}
$$
$$
N_0(r,u)=
3r^2u^2+\varepsilon(r-u)^2+\varepsilon^2-3B_0(r+u).
$$
对相差一个原循环方向的二标签，
$$
\sum_i\frac1{(r-z_i)(u-z_{i+\epsilon})}
=\frac{N_\epsilon(r,u)}{F(r)F(u)},\qquad \epsilon=\pm1,
\tag{790.23}
$$
$$
N_\epsilon(r,u)=
3r^2u^2+\varepsilon(r^2+ru+u^2)
+\frac{3B_0(r+u)+\epsilon\delta(r-u)}2.
$$
这些式子也适用于 $r=u$，没有人为的 $r-u$ 分母。

**证明。** 由
$$
\frac1{r-z_i}=\frac{r^2+rz_i+z_i^2+\varepsilon}{F(r)}
$$
展开乘积。使用
$\sum z_i=0$、$\sum z_i^2=-2\varepsilon$、
$\sum z_i^3=-3B_0$、
$\sum z_i^4=2\varepsilon^2$。
不同循环方向的交项满足
$$
\sum_i z_i z_{i+1}^2=\frac{3B_0+\delta}{2},\qquad
\sum_i z_i^2z_{i+1}=\frac{3B_0-\delta}{2},
$$
以及 $\sum z_i z_{i+1}=\varepsilon$、
$\sum z_i^2z_{i+1}^2=\varepsilon^2$。
代入即得 (790.22)–(790.23)。$\square$

于是两个非零二标签、相对方向为 $\epsilon\in\{0,+1,-1\}$ 时，
其原三项 Eisenstein 迹准确为
$$
\boxed{\quad
3e(R)e(S)
-e(R)\frac{3u^2+\varepsilon}{w}
-e(S)\frac{3r^2+\varepsilon}{v}
+\frac{N_\epsilon(r,u)}{vw}.
\quad}
\tag{790.24}
$$
若一个二标签为零、另一个非零，式子为
$$
e(R)\left(3e(S)-\frac{3u^2+\varepsilon}{w}\right)
\tag{790.25}
$$
或其对称版本；若两者都为零，则为 $3e(R)e(S)$。

全部公式只使用原 $\mathscr M[[\varepsilon]]$，不再需要实际构造任何二挠点三次扩域。
初始二阶 jet 中 $\delta=3sB_0+O(\varepsilon^3)$，更没有额外的平方根迭代。
这项消去保留二标签的相对循环方向与原 $P_1$ 符号，不是将两种方向混为平均。

## 7. 实际计算的最小输入与分阶段边界

新的 CM 核心可以独立于 R787 的线性求解，先生成原146个 $T_j$ 的
$\mathcal T_j\bmod\varepsilon^6$，继而由 (790.13) 给全部 $\psi_j(P_1)$
及可能需要的第一粗 jet；若只求值，二阶已经足够。
真实必要输入为：

- R735 的原280次 $U$ 模数与证书；
- R754 的已完成同向 $\xi\in K(U)$；
- 原 R775 的 M2 recipes、原半群标签和40个 determinant coset；
- R786 原五次乘积的相同 recipe 顺序及尺度。

旧模数、Weil pairing、原标签和已成选基不重算。
新算术只是在同一字段上生成尚缺的 CM 变形/求值。
每个 $T_j$ 必须准确核两项框架零，
其 $\psi_j(P_1)$ 还应按原 $P_1\in Y(K)$ 检查确落在 $K$，
不能靠平均或数值识别强制下降。

R787 的实际整数 $L$ 坐标返回后，先把这些真实 $\psi_j(P_1)$
按旧五次 recipes 相乘并代入 $\widetilde A,\widetilde B$。
如果已有一个非零，按 §3 完成原 $y(c_1)$ 或目标 $O$ 的判定。
如果二者都是零，按同一个原变形继续所需的 jet；
(790.8) 保证不晚于155个粗曲线系数结束。
不能把零阶输入尚未返回时的“预计不共同为零”登记成结果。

最后，若得到有限 $y(c_1)$，完整原 $\beta$ 的 $x$ 坐标仍要保留 R772 的
$$
x=3(y^2-b)\frac h{dy}.
\tag{790.26}
$$
原 $h$ 选择三个立方根方向中的实际一个。
R748 已给原六 Hodge 基在 $z=a-1$ 的准确首项；
应与 R759 原第4微分的真实 $L$ 坐标直接收缩，不重算这些既有 jet。
若该实际 $h(c_1)\ne0$ 且 $y(c_1)^2\ne b$，则 $x(c_1)\ne0$，
从 $dy=3x^2h$ 得一次导数非零，(790.13b)、(790.26) 就给原 $x(c_1)$。
若 $y(c_1)^2=b$，则 $x(c_1)=0$ 已唯一确定，无需强行除以零导数。
若原 $h(c_1)=0$，则需要其真实更高首项；
不能把本篇的155项值界或156项一阶界当作这个额外输入已经完成。
本篇没有用 $H^3$、任意立方根或另一份 CM 平移替代它。
真实高度、第二类周期、Poincaré 刚性化和全 $p$ 排除仍依赖后继实际输出。

## 依据

- R732（2026）§§2、4：完整周期 zeta、原正实点方向及除法函数常数项；
  加法式中的完成化不能删去。
- R735、R751、R754（2026）：原 $U$、280次字段、真实 Weil pairing、原 $\xi$ 和全部 CM 相位。
- R738、R745（2026）：原 $c_1$、$g_\star$ 与一次 Hodge 运输。
- R767、R772（2026）：原 $\Gamma_Y$、粗曲线线丛、$P_0/P_1$ 的 eta 符号与原 $x=3(y^2-b)h/dy$。
- R786、R787（2026）：原五次基、degree1206、完整关系与 actual-result 边界。
- D. Zywina，*Explicit open images for elliptic curves over Q*，2022；修订版2024，
  [作者稿](https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf)，
  Lemma4.7、Corollary4.10：原权一 Fourier 规范及半线性群作用。

