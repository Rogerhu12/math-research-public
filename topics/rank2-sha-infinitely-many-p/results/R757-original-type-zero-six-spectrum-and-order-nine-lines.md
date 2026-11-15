# R757 — 原 degree34 型零的完整六谱、三条九次环面线与中央质量

日期：2026-11-15。**状态：已证明。**

本篇在原 $H^0(E_b,\mathcal O(34[0]))$ 中完成整个型零六维空间的有限谱和实际 Hecke 身份。三条来源是已付的 $E_{17},E_{17^3},E_{17^5}$；其余三条具有 primitive order-$9$ 的十七处环面角色，对应值域 $\mathbf Q(\zeta_9)$ 的同一 Galois 轨道，而不是三条额外的有理椭圆曲线。

全部六条 CM13 本征线单重。只有原 $S$ 的原点质量为零；另五条均非零。后三条的真实权一中心值非零，但这不给任何一条参考的普通中央导数赋零，更不把它们的非零传给原 $S$。原 $T_{72},U_{136}$ 属于别的线丛，未并入这个六维空间。

## 1. 原空间、绝对规范和两处有限模型

沿用 [R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)、
[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)、
[R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md) 的规范：
$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,\qquad
\delta=1+2\omega,\qquad
E_b:y^2=x^3+b,\qquad b=17.
\tag{1}
$$
$x=z^{-2}+\cdots,\ y=-z^{-3}+\cdots,\ \sigma=z+\cdots$。
记 $X=x^3$。整个型零空间准确为
$$
\mathcal H_0=\sigma^{34}x^2 K[X]_{\le5}.
\tag{2}
$$
其维数为6。标准有理基可以取
$e_a=4^{-a}\sigma^{34}x^{2+3a}$，$0\le a\le5$；
原质量是 $4^{-5}$ 乘第六个坐标。

十七处取原 norm-one 生成元
$$
g_0=2+4\delta\in\mathbf F_{289}^1,\qquad
g_0^{18}=1,\qquad g_0^6=\omega .
$$
固定 $\zeta_{18}=e^{\pi i/9}$，其约化对应 $g_0$；
令
$$
\tau_j(g_0)=\zeta_{18}^j,\qquad j\in\mathbf Z/18\mathbf Z.
\tag{3}
$$
本篇使用 R290 的 $g_0$ 方向，原 $S$ 的标签是 $j=12$。若改用逆生成元，它才变成 $j=6$；不能混用两套标签。

原十七维有限 Weil 模缺少唯一二次角色 $j=9$，其余17个角色各出现一次。其完整算子仍为
$$
W(x+y\delta)_{ab}
=-\frac{(y/17)}{\sqrt{17}}\,
 \zeta_{17}^{\,\frac3{2y}\{x(a^2+b^2)-2ab\}},
\qquad W(-1)e_a=e_{-a}.
\tag{4}
$$
这包含原加性角色、极化和 quadratic splitting，未用裸置换模型替换。

在原 dyadic 两维下降空间取
$$
f_A=e_0-e_2,\qquad f_B=e_1+e_3,\qquad
t_\pm=\frac{1\pm\sqrt3}{\sqrt2},\qquad
v_\pm=f_A+t_\pm f_B .
\tag{5}
$$
原矩阵满足
$$
M_\omega^{\rm old}v_+=v_+,\qquad
M_\omega^{\rm old}v_-=\omega v_- .
\tag{6}
$$
几何 $z\mapsto\omega z$ 的实际局部标签是 $\omega^2=g_0^{12}$。
因此其 dyadic 特征在 $v_+,v_-$ 上依次为 $1,\omega^2$。
两个 $v_\pm$ 都偶；全局奇偶只由十七处 $\tau_j(-1)=(-1)^j$ 决定。

### 1.1 六条线的完整角型判定

型零同时要求偶和几何 $\mu_3$ 特征1。因此
$$
\boxed{
\begin{array}{c|c}
\text{dyadic 向量}&\text{允许的十七处标签}\\ \hline
v_+&j=0,6,12\\
v_-&j=2,8,14 .
\end{array}}
\tag{7}
$$
证明是：$j$ 必须偶；在 $v_+$ 上要求 $\zeta_{18}^{12j}=1$，
在 $v_-$ 上要求 $\omega^2\zeta_{18}^{12j}=1$。

每条有限线非零且单重；原半特征下降把它送入同一个标准 degree34 模。
原 Fourier theta 映射单射，所以六条像都非零。由 (2) 的维数，它们正好穷尽整个型零空间，不留下未列出的第七条来源。

## 2. 三条已有 sextic 线及准确秩

令 $\psi_k$ 是 $E_{17^k}:y^2=x^3+17^k$ 的真实解析 CM-type Hecke 角色。由
[R306](R306-jzero-three-sextic-original-local-data-and-full-weight-squares.md)、
[R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)，
(7) 的 plus 部分准确为
$$
\begin{array}{c|c|c|c}
j&\text{曲线/Hecke角色}&\text{共同框来源}&\text{原点质量}\\ \hline
12&E_{17},\ \psi_1&S&0,\quad[z^6]S=1\\
0&E_{17^3},\ \psi_3&H_3&1\\
6&E_{17^5},\ \psi_5&H_5&1 .
\end{array}
\tag{8}
$$
固定实微分周期下，R307 的原完整 Kronecker 和给
$$
\frac{L(E_{17^3},1)}{\Omega_{17^3}}=3,\qquad
\frac{L(E_{17^5},1)}{\Omega_{17^5}}=6.
\tag{9}
$$
它们由已发表的 CM rank-zero 定理得到秩0。$E_{17^5}$ 不是另一个秩二目标；这里只原 $E_{17}$ 是已付的秩二曲线。

这些是真正不同 Hecke 角色。把它们的 sigma 形式通过固定六次伸缩放在同一个 $b=17$ 框中，不把 Euler、period 或完整普通分支相认。

## 3. 其余三条的全局 Hecke 角色

以后
$$
j\in\{2,8,14\},\qquad l_j=j-9\in\{-7,-1,5\}.
\tag{10}
$$
记 $\psi_{\mathrm{base}}$ 为 $E_1:y^2=x^3+1$ 的原角色。
在 $\mathbf F_{289}^{\times}$ 上定义
$$
\vartheta_l(a)=a^{16l}
$$
的唯一 $\mu_{18}$ 提升，采用 (3) 的同一嵌入。它在
$\mathbf F_{17}^{\times}$ 上平凡，且
$$
\vartheta_l(\delta)=-1,\qquad
\vartheta_l(\omega)=\omega^2 .
\tag{11}
$$
三个 $l$ 都与18互素，所以 $\vartheta_l$ 的阶准确为18。

对素于 $34\delta$ 的 $a\in\mathcal O_K$，令
$$
\varepsilon_j(a)=
 \operatorname{Teich}_{\mu_3}(a\bmod2)^{-1}
 \,(a\bmod\delta)\,\vartheta_{l_j}(a\bmod17).
\tag{12}
$$
中间因子取 $\{\pm1\}$ 的提升。直接对 $\omega,-1$ 检查，
$$
\varepsilon_j(u)=u\qquad(u\in\mu_6).
\tag{13}
$$
例如在 $\omega$ 上，三个因子分别为 $\omega^2,1,\omega^2$，
乘积为 $\omega$；在 $-1$ 上为 $1,-1,1$。

因 $h_K=1$，公式
$$
\boxed{\Psi_j((a))=a\,\varepsilon_j(a)^{-1}}
\tag{14}
$$
因而与主生成元的选择无关，定义真实的 type-$(1,0)$ Hecke 角色。
它不是由几个好素数的特征猜出的角色。

### 3.1 完整坏处、导子和有限扭曲

置 $\chi_j=\Psi_j\mathrm N^{-1/2}$。在与原题相同的 idèle 约定中，
$$
\boxed{
\begin{array}{c|c|c}
v&\chi_{j,v}\text{ 在单位上的值}&\text{指定 uniformizer 值}\\ \hline
2&\operatorname{Teich}_{\mu_3}^{-1}&-1\text{ 于 }2\\
3&u\bmod\delta\in\{\pm1\}&-i\text{ 于 }\delta\\
17&(u\bmod17)^{16l_j}&-1\text{ 于 }17 .
\end{array}}
\tag{15}
$$
uniformizer 值不能另选。例如主 idèle $2$ 在三处给 $-1$，
而17角色在有理单位上平凡，故二处为 $-1$。主 idèle17同理。
主 idèle $\delta$ 的无穷相位为 $-i$、17相位为 $-1$、
二处为1，所以三处值是 $-i$。

三个单位角色分别真正具有导子 $2,\delta,17$，故
$$
\mathfrak f_{\Psi_j}=(34\delta),\qquad
\mathrm N\mathfrak f_{\Psi_j}=3468 .
\tag{16}
$$
定义
$$
\eta_j=\Psi_j/\psi_{\mathrm{base}} .
\tag{17}
$$
它是**阶恰为18**的有限反圆分 Hecke 角色，导子为 $(34)$。
其三处分量不分歧，但在 $\delta$ 上为 $-1$；不能因为导子不含3就删掉该值。
(15) 还给 $\Psi_j\Psi_j^c=\mathrm N$。

### 3.2 真正的角色值域和新形式系数域

(14) 的值都在
$$
E=K(\zeta_{18})=\mathbf Q(\zeta_9)
\tag{18}
$$
中。素于导子的 $a\equiv1\bmod34\delta$ 给 $\Psi_j((a))=a$，所以值域已经包含 $K$。
再用 CRT 选择 $a\equiv1\bmod2\delta$ 且17处为指定单位，
$\Psi_j((a))/a$ 读出全部 $\mu_{18}$，故值域恰为 $E$。
三条 $\Psi_j$ 是 $\operatorname{Gal}(E/K)$ 的一个完整三元轨道；
在指数 $l$ 上，它是乘以 $1,7,13\bmod18$ 的轨道。

其 CM 自守诱导为权2、level10404、平凡中心有限角色的共轭新形式。
系数落在
$$
E^+=\mathbf Q(\zeta_9+\zeta_9^{-1}).
\tag{19}
$$
这个域准确为三次，非仅包含关系。确实，下面的 CM13 公式给
$$
a_{13,j}=\gamma_{13}\lambda_j+
 \bar\gamma_{13}\lambda_j^{-1},\qquad
\lambda_j\in\{\zeta_{18},\zeta_{18}^7,\zeta_{18}^{13}\}.
\tag{20}
$$
若两项相同，则不同的单位根 $\lambda,\lambda'$ 满足
$\gamma_{13}/\bar\gamma_{13}=(\lambda\lambda')^{-1}$；
这不可能，因为左边在两个13处的赋值不同，而右边为单位根。
所以三个实共轭值不同，已经生成 (19)。

因此这三条不对应三条 $E/\mathbf Q$ 的有理新形式。
本篇不把高维 CM 自守对象的秩或高度结论冒充原椭圆曲线的结论。

## 4. 全 Schwartz、Hermitian 类和真正的六维 CM13 谱

### 4.1 实际向量，不只角型

在原十七维模中取
$$
\Pi_j=\frac1{18}\sum_{a=0}^{17}\tau_j(g_0)^{-a}W(g_0^a).
\tag{21}
$$
它的秩为1。为完全固定非零向量，可取最小的
$a_j\in\{0,\ldots,16\}$ 使 $\Pi_j e_{a_j}\ne0$，
并令 $f_j=\Pi_j e_{a_j}$。这是固定有限代数定义，不依赖目标 $p$。
记
$$
n_j=\sum_{a=0}^{16}|f_j(a)|^2>0 .
\tag{22}
$$
由 $\overline{W(g)}=W(g^{-1})$ 得
$\overline{\Pi_j e_a}=\Pi_j e_a$；由 $\tau_j(-1)=1$ 得 $f_j$ 偶。
所以 $f_j$ 是实际非零实偶向量。

十七处取 $\sum_a f_j(a)\mathbf1_{a/17+\mathbf Z_{17}}$，
二处取 $v_-$，三处取原 $\mathbf1_{3^{-1}\mathbf Z_3}$，
其余有限处取原球。Hilbert90 写 $g=z/\bar z=z^{-16}$：
(15) 的环面角色为 $g^{-l_j}$，连同 quadratic splitting，
所需不变向量的有限标签准确为
$$
g^{9+l_j}=g^j .
\tag{23}
$$
二处 (15) 与 R735 的 inverse cubic 角色相同，完整 $\mu_3,-1,g_*$ 生成元验证给 $v_-$。
三处与 R290 完全相同。故这是整个局部环面的验证，不只验证一个单位。

十七处的完整 Gauss 和仍为 $-17$。
证明是其角色在 $\mathbf F_{17}^{\times}$ 上平凡且在 $\delta$ 上为 $-1$：
$x=0$ 的纤维和为 $-16$，每个 $x\ne0$ 的纤维和为1。
dyadic inverse cubic 的原 $\mathbf F_4$ Gauss 和仍为2，三处为 $i\sqrt3$。
因此 Yang dichotomy 在 $2,3,17,\infty$ 为
$$
(+1,-1,-1,+1),
$$
Hermitian 类仍准确为 $\alpha=17$，原 Gaussian 为 $51\sqrt3$。
权一的完整 epsilon 因子依次为
$$
(+1,-i,+1,i),
$$
所以
$$
w(\Psi_j)=+1 .
\tag{24}
$$

全 Fourier 序列为
$$
a_{j,n}=v_-(n\bmod4)f_j(3n\bmod17),
\qquad v_-=(1,t_-,-1,t_-).
\tag{25}
$$
它非零、实、偶，并满足
$(-1)^n a_{j,n+34}=-a_{j,n}$。
因此原 half-character 计算仍准确下降到标准 degree34，未增加二挠 twist。
(7) 又证明它的全部 Taylor 次数均为6的倍数。

### 4.2 完整且绝对定标的 CM13 特征

令
$$
\gamma_{13}=4+\omega,\qquad
N_{13}=\gamma_{13}^{-1}[\gamma_{13}]_*[\bar\gamma_{13}]^* .
\tag{26}
$$
R297/R735 已用原 $S$ 定出整个 Heisenberg 交织子的公共标量 $-\omega^2$；
CM13 的实际 dyadic 标签为 $\omega^2$，17标签为 $g_0^{14}$。
故六线的完整表为
$$
\boxed{
\begin{array}{c|c|c|c}
\text{dyadic}&j&N_{13}\text{ 特征}&\text{来源}\\ \hline
+&0&-\omega^2&H_3\\
+&6&-\omega&H_5\\
+&12&-1&S\\
-&2&\zeta_{18}^7&H_{-,2}\\
-&8&\zeta_{18}&H_{-,8}\\
-&14&\zeta_{18}^{13}&H_{-,14}.
\end{array}}
\tag{27}
$$
后三行使用 $-\omega^2\cdot\omega^2\tau_j(g_0)^{14}
=-\omega\tau_j(g_0)^{14}$。第一、第二行的顺序由实际标签固定，不是只列无序根。

也可直接从 (14) 检查：
$\gamma_{13}\bmod2=\omega$，$\gamma_{13}\bmod\delta=-1$，
$\gamma_{13}/\bar\gamma_{13}=g_0^{14}\bmod17$，所以
$$
\frac{\Psi_j((\gamma_{13}))}{\gamma_{13}}
=-\omega\,\zeta_{18}^{14l_j}
=-\omega\,\zeta_{18}^{14j}.
\tag{28}
$$
这与 (27) 的真实 whole trace 绝对相位相同。

所有特征两两不同，且
$$
\boxed{\det(X-N_{13}\mid\mathcal H_0)
=(X^3+1)(X^3+\omega^2).}
\tag{29}
$$
该式来自完整有限模型和已付的全局锚，不是由几个目标素数样本推断。
两个真实三维投影可以写成
$$
P_+=\frac{N_{13}^3+\omega^2 I}{\omega^2-1},\qquad
P_-=\frac{N_{13}^3+I}{1-\omega^2}.
\tag{30}
$$

## 5. 唯一零质量线，以及后三条的确切原点非零

R297 已对同一完整六维矩阵证明
$$
\ker\begin{pmatrix}
\mathrm{ev}_0\\
\mathrm{ev}_0N_{13}\\
\vdots\\
\mathrm{ev}_0N_{13}^5
\end{pmatrix}=K S ,
\qquad \text{观察矩阵秩}=5.
\tag{31}
$$
把标量域扩张到 $E$ 不改变秩或核。
若另一条本征线有质量零，则其每个 $N_{13}$ 幂的质量都零，
便由 (31) 属于 $ES$，与 (27) 的不同特征矛盾。

故 (27) 中**只有** $S$ 的质量为零。
可将后三条唯一规范为
$$
H_{-,j,b}(0)=1 .
\tag{32}
$$
它们是实际有限 Schwartz 来源，不是任取的同次数向量。

这个规范可纯代数地实现：在 R297 已付的六维矩阵中，
$H_{-,j,1}$ 是方程
$$
(N_{13}-\lambda_jI)v=0,\qquad \mathrm{ev}_0(v)=1
\tag{33}
$$
的唯一解。它的系数在 $E$ 中。另一方面 (25) 的实性及原实周期给
$H_{-,j,1}$ 在实轴实值，因此其 sigma 多项式系数在 $E^+$ 中。
该系数域不能是 $\mathbf Q$：若是，(33) 与原 $K$ 矩阵将使
$\lambda_j=\mathrm{ev}_0(N_{13}v)$ 落在 $K$，而 (27) 不允许。
由于 $[E^+:\mathbf Q]=3$，系数域准确为 $E^+$。

写
$$
H_{-,j,1}=\sigma_1^{34}x_1^2\sum_{a=0}^5 c_{j,a}X_1^a,
\qquad c_{j,5}=1 .
$$
回到原 $b=17$ 的完整式是
$$
\boxed{
H_{-,j,b}(z)
=H_{-,j,1}(b^{1/6}z)
=\sigma_b^{34}x_b^2
 \sum_{a=0}^5 c_{j,a}b^{5-a}X_b^a .
}
\tag{34}
$$
这里质量没有变为一个未显示的 period 倍数。

## 6. 全权来源：必须保留阶18有限角色

设
$$
\Phi_{j,n}=\eta_j\,\psi_{\mathrm{base}}^{\,2n+1},
\qquad n\ge0,\quad n\equiv0\bmod6 .
\tag{35}
$$
这些角色的全部坏处有限分量正好是 (15)，所以同一个有限 Schwartz 适用于全部这些权。好分裂处的球按 Yang 的原极化公式保持；没有声称其未分歧参数不变。

**必要的区别是**
$$
\boxed{
\Phi_{j,n}
=\Psi_j^{\,2n+1}\eta_j^{-2n},
\qquad
\Phi_{j,n}=\Psi_j^{\,2n+1}
\iff n\equiv0\bmod18
\quad(n\equiv0\bmod6).
}
\tag{36}
$$
若只写 $\Psi_j^{2n+1}$，就会在 $n\equiv6,12\bmod18$ 错换原十七处分量。
这种错误不能用同一型零 Taylor 支撑弥补。

令 $S_{j,\Lambda}$ 为 (25) 的原 reduced theta，
$\Omega_0$ 为 $E_1$ 的原实周期，写
$$
S_{j,\Lambda}(Z)=s_jH_{-,j,1}(\Omega_0Z).
$$
由 (32) 得 $s_j\in\mathbf R^\times$。
原 Hermite 尺度仍是
$$
h_\infty=\frac{\sqrt{51\sqrt3}}{204\pi i}.
$$
若 $d_{j,n}=[z^n]H_{-,j,1}$，完整 Hermite 和为
$$
b_{j,n}=n!\,s_j(\Omega_0h_\infty)^n d_{j,n}.
\tag{37}
$$
有限范数为 $(3-\sqrt3)\cdot3\cdot n_j$；
全部测度和原体积给
$$
\boxed{
L(\Phi_{j,n},n+1)
=C_j\,\frac{(4\pi)^n}{n!}\,b_{j,n}^2,\qquad
C_j=\frac{\pi\sqrt{102\sqrt3}}
 {17\sqrt3(3-\sqrt3)n_j}>0 .
}
\tag{38}
$$
这沿用 Yang 原完整范数公式及 R290/R735 已付的 Haar 规范，
没有把 $n_j$ 或 dyadic 范数约成1。

特别 $n=0$，$b_{j,0}=s_j\ne0$，所以
$$
\boxed{L(\Psi_j,1)=C_js_j^2>0.}
\tag{39}
$$
这是同一原 theta 来源的确切非零性，不借数值解析秩或 BSD。
本篇不需要把 (39) 加工为某个新 abelian variety 的秩断言。

为保共同周期，置 $\varpi_0=s_0\Omega_0$、
$s_0=(1-\omega)^{-1}$，并令
$$
\kappa_j=\frac{L(\Psi_j,1)}{\Omega_0},\qquad
c_j=\kappa_j/s_0\in\overline{\mathbf Q}^{\times}.
$$
此处的 $c_j$ 是全局平方常数，区别于 (34) 的 $c_{j,a}$。
CM 临界值代数性与 (38) 给
$$
\boxed{
\frac{(2\pi/\sqrt3)^nL(\Phi_{j,n},n+1)}
 {n!\varpi_0^{\,2n+1}}
=c_j\,34^{-n}d_{j,n}^2,\qquad6\mid n .
}
\tag{40}
$$
原 $b=17$ 测度使用 $\Omega_{p,0}=17^{1/6}\Omega_p$；
(34) 在同一物理变量上给
$\nu_{H_{-,j,1}}=\nu_{H_{-,j,17}}$。这里的两测度分别用自己的刚才显示周期，不作单位域伸缩。

## 7. 普通零权与实际中央导数的范围

原 ray 的 primary $\pi_0$ 满足 $\pi_0\bmod17=\delta$。
由 (12)–(15)，
$$
\Psi_j(\mathfrak p)=-\pi_0,\qquad
\Psi_j(\bar{\mathfrak p})=-\bar\pi_0 ,
\tag{41}
$$
所以后三条在这个 ray 上的 ordinary Euler 与原 $S$ 具有相同的实际 root。
这只是已固定 ray 上的结论，不将 $\Psi_j$ 全局认成 $\psi_{17}$。

原 whole degree34 core 是 $\lambda R_Y$；型零为偶，
故本篇每个质量一来源的单位质量准确为
$$
J_{-,j}(0)=1-\lambda .
\tag{42}
$$
原 R410 好素数范围已保证 $1-\lambda$ 是单位。
也可把 (40) 的零权 primitive Katz 插值连同两个相同 ordinary Euler 因子写为
$$
\mathcal K^{\rm prim}_{p,34\delta}(\widehat\Psi_j)
=c_j\Omega_{p,0}(1-\lambda)^2\ne0 .
\tag{43}
$$
(43) 保留了 primitive 坏点规范，没有将不同完整 Hecke 角色的 Katz 函数相认。

在一般原 weight 变量上，(35) 对应
$$
\eta_j\,
\psi_{\mathrm{base}}^{\,n+1}\bar\psi_{\mathrm{base}}^{-n}.
\tag{44}
$$
它是固定阶18角色乘原基础 norm-weight-one 族。
只有在 (36) 的相应权子类才可改写为 $\Psi_j$ 的裸幂族。
(42)–(43) 是零阶参考值；它们不给 $J_{-,j}'(0)$ 赋零，也没有给它一个未证明的点 logarithm 表达。

任意型零原截面现在有唯一有限分解
$$
F=aS+a_3H_3+a_5H_5+
 \sum_{j=2,8,14}a_jH_{-,j}.
\tag{45}
$$
于是
$$
F(0)=a_3+a_5+a_2+a_8+a_{14}.
\tag{46}
$$
零质量只给 (46) 的一个线性关系。它不删除另五个真实 Mellin 分量。
只有当整个 CM13 质量轨道也为零时，(31) 才迫 $F\in KS$。

如果要把原中央 $J_S'(0)=0$ 传播到物理剪切，仍须付
[实际中央剪切 note](../notes/2026-11-15-actual-central-shear-and-fixed-representation-gate.md)
中固定表示、完整连接和局部 unit 的式(18)；(45) 的维数或 (39) 的参考非零都不能代替它。
原 $J_T',J_U'$ 也不会因位于别的原 theta 线丛而自动控制 (45) 中的未知导数。

## 8. 证明来源与复现范围

本篇没有执行新的数值或精确矩阵计算。使用的整矩阵、绝对锚与观察秩均是已付的 R297；本篇的特征表由原有限作用、半特征与全部局部角色逐项推得。
(33) 给出可直接从已提交矩阵重建全部新多项式的唯一代数定义，不需要另存可重算数据。

- R290、R297：原 whole degree34、完整 $2/3/17$ splitting、CM13 全纤维矩阵及质量观察核。
- R306、R307：三条 plus 来源的全部有限角色、固定周期和精确秩零中央值。
- R735、R751：同一 dyadic minus/plus 的完整局部生成元、原 Heisenberg 绝对标量及 half-character 下降。
- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math. 485 (1997), 25–53，原全权范数和全局平方公式：
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*, Compositio Math. 117 (1999), 337–359，原 lattice model、splitting 和 Schrödinger 转模：
  <https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。

原 rank-two 无穷素数结论仍未由本篇得到；本篇完整确定的是原六维中央来源真正包含哪些算术角色、哪些质量可用，以及不能遗漏的阶18全权补偿。
