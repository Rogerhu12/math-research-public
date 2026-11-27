# 原未平方 toric theta 生成函数与同源 Newton 来源

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

本注保持 R1049、原 weight5 Artin 基笔记的同一54图、完整 full9、
$Ph$、$e_{\eta_j}$和全部有限角色。所比较的是整个经典权生成函数，
不是从各个经典平方任取一个号。尤其同时保留真实无穷平移的二次相位
和三处 similitude 的 $\delta$ 提升；单独省掉其中任何一个都会误判六步号。

令 $t=2^{1/3}>0$，$\delta=1+2\omega$。沿原规范
$$
\Omega=\epsilon_0t\,\varpi_0,\qquad
\varpi_0=s_0\Omega_0,\qquad s_0=(1-\omega)^{-1},\quad
\Omega_0>0,\quad\epsilon_0\in\mu_6 .
\tag{1}
$$
$T_{j,k}$与 $B_j=(17\delta/9)T_{j,5}$使用
[共同相位笔记](2026-11-27-original-weight-five-toric-artin-basis-and-common-phase.md)
的定义；$D_j=D_{j,1}$和 $d_{j,m}=[z^m]D_j$使用 R806 的原
首 $z^4=1$规范。始终 $j=4,10,16$。

## 1. 结论和不能省略的源规范

对全部 $k\ge5$、$k\equiv5\bmod6$，置 $r=(k-5)/6$，则
$$
\boxed{
T_{j,k}=-(-1)^r A_kB_jd_{j,k-1},\qquad
A_k=\frac{\delta}{34}\,
3^{(k-5)/2}2^{-(k+1)/3}(k-1)! .
}
\tag{2}
$$
因此共同相位笔记中的 $\varepsilon_k$准确为 $-(-1)^r$。

更强地，定义原 toric 生成函数
$$
\mathscr G_j(Z)=
\sum_{r\ge0}\frac{T_{j,6r+5}}{(6r+4)!}\,Z^{6r+4}.
$$
它满足未平方的完整来源恒等式
$$
\boxed{
\mathscr G_j(Z)
=\frac{B_jt^4}{408\delta}\,
D_j\!\left(\frac{\delta}{t}Z\right).
}
\tag{3}
$$
右边的变量倍率是实际同源
$$
A=E_{27}\xrightarrow{I_{27}^{-1}}E_0
 \xrightarrow{[\delta]}E_0,\qquad
I_{27}(x,y)=(tx/2,(y-1)/2)
\tag{4}
$$
在原微分上的拉回倍率 $\delta/t$。这不是一个未指定的六次根。
(3)首先是原刚性化下的形式 theta 截面等式，也由下文的 Gaussian
生成函数给出整解析等式。其线丛是(4)对原 degree34 线丛的拉回，
次数为102；不把它无修正地重命名为 $A$ 上原 degree34 截面。

对 R1049 中全部前提成立的好惰性 $p$，其残余线性式进一步成为
$$
\boxed{
\overline a_{j,p}\,\overline h_{j,p}
=-[L:H]\,\overline B_j\,\overline K_{j,p}(0).
}
\tag{5}
$$
第8节另给真正全 $p$ 精度的 Newton **来源**等式。
它并不把最高 AJ 的全精度调节子直接命名为原椭圆 signed 坐标。

## 2. 使用的未平方 seesaw 及完整 characters

记
$$
\nu_0=\psi_0N_K^{-1/2},\qquad
\nu_{27}=\psi_{27}N_K^{-1/2}=\kappa\nu_0,\qquad
\kappa^3=1,\qquad m=k-1\equiv4\bmod6.
$$
这里所有角色使用 R806、R991 的完整 idèle 规范。
选固定 splitting 角色 $\mu=\nu_0$，其在有理 idèle 上为 $\chi_K$。
对 $U(1)=K^1$，以
$\widetilde\alpha(z)=\alpha(z/\bar z)$记 Hilbert90 拉回。
定义两个实际 norm-one characters
$$
\widetilde\alpha_{1,j,m}=\eta_j^{-1}\nu_0^{-2m},
\qquad
\widetilde\alpha_{2,j}=\eta_j\nu_{27}\nu_0 .
\tag{6}
$$
右边在有理 idèle 上均为1，所以这确实定义 characters。

取 split Hermitian plane，其两条 Hermitian 线依次为
$(-17,17)$。对于 étale algebra $\mathbf Q\times\mathbf Q$，
splittings 选择为
$$
\chi_{W,F}=\mu,\quad
\chi_{W,E}=(\mu,\mu)=\mu\circ N,\quad
\chi_{L,E}=(\mu,\mu),\quad
\chi_V=\mu^2 .
\tag{7}
$$
故原文所需两个相容条件逐个成立。
两条 rank-one theta lift 的完整 $L$ characters 是
$$
\begin{aligned}
\widetilde\alpha_{1,j,m}\mu^{-1}
 &=\eta_j^{-1}\nu_0^{-(2m+1)},\\
\widetilde\alpha_{2,j}\mu^{-1}
 &=\eta_j\nu_{27}.
\end{aligned}
\tag{8}
$$
它们是 R1049(98)的第二因子的共轭 unitary 角色和固定
$\beta_j$的 unitary 角色。第一条 Hermitian 线的负号与该共轭同时保留。

另一方面
$$
\widetilde\alpha_{1,j,m}\widetilde\alpha_{2,j}
=\kappa\nu_0^{2-2m}
=\nu_{27}^{-2m}\nu_0^2
=\widetilde{(\nu_{27}^{-m}\nu_0)|_{K^1}},
\tag{9}
$$
其中使用 $-2m\equiv1\bmod3$。这正是 binary theta lift 的
source character $\chi_m\mu$，$\chi_m=\nu_{27}^{-m}$；
其 GL2 表示为 $\operatorname{AI}(\nu_{27}^{-m})
=\operatorname{AI}(\nu_{27}^{m})$。
将理想逐个共轭，首 Fourier 系数为1的经典形式正是原
$\theta(\psi_{27}^m)$。

还须检查 toric 方向。在 physical norm-one torus 上，两个特征
的比给原 $\xi_{j,k}=\eta_j^{-1}\nu_{27}^{-k}$：
$$
\frac{\widetilde\alpha_{1,j,m}}
     {\widetilde\alpha_{2,j}}
=\eta_j^{-2}\kappa^{-1}\nu_0^{-2m-2}
=\widetilde{\xi_{j,k}|_{K^1}}.
\tag{10}
$$
这里 $-2m-2\equiv-1\bmod3$，没有改成相反 $\eta$。
中心延拓也不能省。在3处
$$
(\chi_m\mu)(\delta)=i^{1-m}
=-i^{-(m+1)}=\xi_{j,k}(\delta).
\tag{11}
$$
因此 norm-one 比较确延拓至原 $K_3^\times/\mathbf Q_3^\times$
的 $\delta$ 分量，而不只比较单位 torus。
这与 R1049(94)的原右 $D$ 延拓一致。

所用未平方恒等式是 Borade 等已发表论文 §4.2.2 的双积分交换：
对(7)的同一个 theta kernel，先对 source $U(1)$再对 target
$U(1)\times U(1)$积分，与相反次序积分相同。
其 §4.1.3(7)进一步把分解 Schwartz 的输出写成两个
rank-one theta lift 的乘积。这里所有 quotients 紧，交换绝对收敛；
没有借该文“存在某个非零向量”的定理认定本题指定向量。

## 3. 有限 Schwartz 为什么在整个六步支保持同一条线

binary theta lift 采用 Chan §7 的实际 Schwartz newvector：
无穷处为
$$
\overline z^{\,m}e^{-2\pi z\overline z},
\tag{12}
$$
有限未分歧处为球；在3处为
$\chi_m(z){\bf1}_{\mathcal O_{K_3}^{\times}}(z)$，连同她的
different 平移。因为 $\nu_{27}|_{\mathcal O_{K_3}^{\times}}$
通过 $\mu_6$，此有限函数对 $m\mapsto m+6$逐项不变。
首 Fourier 系数由 norm-one 单位积分给出；其 angular character
与(12)准确相消。按首系数1归一所需的实数为正，且不存在另一个
随 $m$变化的复相位。

仍作用 R1049(96)、(99)的**同一**有限算子：
2、17处所有邻点及原角色权；
3处 $e_{\theta^{-1}}\pi(\operatorname{diag}(3,1))$，
之后为原 $Ph$。所有 projector、全部243项和54邻点均不改变。

两处 inert 邻点的总 determinant 类为 $1/34$。
在 $\mathbf Q^\times/NK^\times$中
$$
\frac1{34}\equiv\frac{17}{2},
\qquad
\frac{1/34}{17/2}=\frac1{17^2}=N(1/17).
\tag{13}
$$
这个 determinant 计算可在原 global theta lift 上逐坐标实现，
不另造一个不能表示1的 quadratic form后再要求其首 Fourier 系数为1。
取真正有理矩阵 $\gamma=\operatorname{diag}(34,1)$。
将原有限向量左乘 $\gamma^{-1}$后，2、17处剩 determinant
valuation各为$-2$，分别取有理 $2^{-1}$、$17^{-1}$的 norm lift
再乘单位；$\nu_{27}^{-m}$在这些有理 lift 上为1。
在3处剩 determinant为$-3/17$，是$N\delta$乘一个 norm unit。
无穷 CM 点则变成$\tau'=\omega/34$。为避免将标准列与
Schrödinger 位置混用，下面给出实际换极化图。
先写
$$
(x_0,y_0)=u_0(\omega/34,1)+v_0(\bar\omega/34,1),\qquad
u_0=17u,\quad v_0=17v,\quad
(x_K,y_K)=(2x_0,y_0/17).
\tag{13a}
$$
于是$(x_K,y_K)=u(\omega,1)+v(\bar\omega,1)$，且
$$
\operatorname{Tr}(x_0\bar y_0'-y_0\bar x_0')
=\frac{17}{2}\operatorname{Tr}
 (x_K\bar y_K'-y_K\bar x_K').
\tag{13b}
$$
所以 rank-one 系数$(-1/17,1/17)$精确变成$(-17,17)$。
这同时给出§5的$a=17/2$，没有只按 Hermitian 平方类挑代表。

若以标准列的第二坐标作 Schrödinger 位置，则在(13a)前
同时把旧、新两极化作以下**固定**的全局 torus 换极化：
$$
R=\iota_{\tau'}(\omega)=
\begin{pmatrix}-1&-1/34\\34&0\end{pmatrix},\qquad
R\tau'=\tau',\qquad
R(\tau',1)=\omega(\tau',1).
\tag{13c}
$$
其新位置是$q=34x_0=17x_K$；因此原 coherent Gaussian
$e^{-\pi(\sqrt3+i)|q|^2/34}$成为
$e^{-\pi(17/2)(\sqrt3+i)|x_K|^2}$，coherent 参数的实尺度是17。
这里是对完整 Heisenberg kernel 的 metaplectic 共轭，必须同时
运输两极化和有限 Schwartz，不能只替换 Gaussian 的自变量。
(13c)是同一个全局$[\omega]$；在无穷处
$\varsigma_{\tau'}^{-1}R\varsigma_{\tau'}=r(-2\pi/3)$，
由 Chan Lemma7.3 其 weight-$k$因子为$\omega^{-k}=\omega$
（$k\equiv5\bmod6$），有限因子与之全局相消。
等价地，任何余下 coherent 单位旋转的六次幂为1，
在全部$m\equiv4\bmod6$上只给同一个固定 scalar，
由原$T_{j,5}$锚定；绝不贡献新的六步号。

由(13a)–(13c)，§5采用的 eigenvectors、正幅度和 chirp
都已回到同一原 Gaussian。2、17的 norm lifts及这里的正有理
尺度没有增添一个未记出的$m$相位。这解释了原 Yang 的代表17，
而非凭$L$因子相同任换 Hermitian 类。

在(8)的第一条 rank-one 因子，按实际共轭的负 Hermitian 模型，
有限函数正是 R806(19)的原向量：
$$
(f_A+t_-f_B)\ \otimes\
{\bf1}_{3^{-1}\mathbf Z_3}\ \otimes\
\sum_a f_j(a){\bf1}_{a/17+\mathbf Z_{17}} .
\tag{14}
$$
理由是完整(6)、(8)给原2处 dyadic 角色、3处所有主单位及
17处 $g_0$标签；负模型同时共轭 additive representation 和
splitting，原函数(14)本身是实函数。
所以这不是仅用一个 CM13 根识别来源。
Yang 的 (2.8)、Corollary2.4 对各 nonsplit place给对应
Schwartz eigenline的一维性；在其余未分歧处，实际球在固定
变极化下仍是球。故双 torus projector 把整个有限 kernel送入
(14)与固定 $\beta_j$因子的 tensor line。
各处剩余复比例只依赖 $j$和固定模型，不依赖 $m$。

可用已付的 $T_{j,5}\ne0$说明这些实际比例及固定 beta theta-null
均非零：若其中一个为零，完整未平方 seesaw 会使同一个
$T_{j,5}$为零。这没有用最终待证高权非零作为输入。

## 4. 三处 similitude 中唯一随六步改变的相位

前节尚未把 $\operatorname{diag}(3,1)$的 norm lift并入
“固定比例”。这是必须单列的一项。

Chan §6.1 的 similitude theta 定义，在 $\det g=N(h)$时含
source character $(\chi_m\mu)(h)$。
原 $\operatorname{diag}(3,1)$在3处使用真正的提升
$h=\delta$，$N\delta=3$。Weil splitting本身只含固定 $\mu$，
所以其中唯一随 $m$变化的 scalar为
$$
\boxed{\chi_m(\delta)=i^{-m}.}
\tag{15}
$$
若选 $\bar\delta$，与之相差的 source $-1$及 Weil action
同步变化，仍给同一实际值；不能只换其中一处。

其它有限操作没有漏掉另一个六步号：

| 原操作 | 对六步相位的精确影响 |
| --- | --- |
| 2、17全部邻点 | $\nu_{27}$在单位不分歧；有理 uniformizer 上为$-1$，而$m$为偶数；改用(13)仅有正实尺度 |
| 两处几何 weight $k$倍率 | $2^{k/2}$、$17^{k/2}$均为正实数 |
| $e_{\theta^{-1}}$、different 平移 | 固定 additive character、固定完整 compact型及固定 finite Weil operator |
| $Ph$ | determinant$-2$在$\mathbf Q_3^\times$为 norm unit；可取单位提升，$\chi_m$在该单位上的六步比为1 |
| 原$3^{k/2}$幅度 | 正实数 |
| 其它有限位 | 原球；无新的非平凡 translate |

特别(15)在 $m\mapsto m+6$时的比为 $-1$。
R1049(95)中右 $D$值$i^k$同时改变符号正是这一延拓的
Whittaker 表现；本注未把全部 $k\equiv5\bmod6$当作同一个
$k\bmod12$。

由于 $h_K=1$，norm-one torus 的理想部分可由
$\alpha/\bar\alpha$的全局点消去；剩下无穷圆和有限单位，
模固定的 $\mu_6$。故在 full toric 积分重排中也不会再引入
一个未知的有限 ideal-class scalar。所有 measure 比为正且固定。
(11)已检查剩下的 ramified $\delta$中心延拓。

## 5. 原 CM 点的完整实极变极化

本节直接计算一个 coherent kernel，避免将“Fourier变换送
holomorphic monomial到 Hermite”当作没有坐标的相位断言。

置 $a=17/2$、$G=6a\sqrt3=51\sqrt3$。
在 binary 模型中写 $z=x+iy$，而在原 torus 的两个 eigenspaces
上取
$$
e_+=(\omega,1),\quad e_-=(\bar\omega,1),\qquad
(x_K,y_K)=u e_++v e_- .
$$
于是
$$
u=(x_K-\bar\omega y_K)/\delta,\quad
v=(\omega y_K-x_K)/\delta .
\tag{16}
$$
用 $u=A+\delta r,\ v=B+\delta s$为两条 rank-one 模型的实极化。
原 symplectic form为 $a\operatorname{Tr}(x_K\bar y_K'
-y_K\bar x_K')$；由(16)变为
$a\operatorname{Tr}\delta(u\bar u'-v\bar v')$。
在 canonical momenta $2ay_R,2ay_I$与 $-6aA,6aB$下，
对应的 generating function是 $aS$，其中
$$
S=-2x^2-6(r-s)x+2\sqrt3(r+s)y-3r^2+12rs-3s^2 .
\tag{17}
$$
直接对 $x,y,r,s$求偏导即可核回全部四个 momenta，
所以这里的两个正负号不是任选的极化。

原无穷向量必须经过
$\varsigma_\infty=\left(\begin{smallmatrix}\sqrt3/2&-1/2\\0&1\end{smallmatrix}\right)$。
因此其 Gaussian为
$e^{-\pi a(\sqrt3+i)(x^2+y^2)}$，而非在$i$点的实 Gaussian。
考虑
$$
I(Z;r,s)=\int_{\mathbf R^2}
 e^{-\pi a(\sqrt3+i)(x^2+y^2)}
 e^{Z(x-iy)} e^{-2\pi iaS}\,dx\,dy .
\tag{18}
$$
令 $A_R=\sqrt3-3i,\ A_I=\sqrt3+i$。逐变量完成平方给
$$
I=C_a e^{-\pi G(r^2+s^2)}
 \exp\left(
 2(\omega-1)rZ+
 \frac{A_R^{-1}-A_I^{-1}}{4\pi a}Z^2
 \right),
\tag{19}
$$
$C_a\ne0$只依赖固定 Gaussian和 Haar normalization，不依赖
$Z$或$m$。其中完整恒等式是
$$
A_R^{-1}-A_I^{-1}
=-\frac{\sqrt3}{6}+\frac i2,\qquad
\frac{A_R^{-1}-A_I^{-1}}{4\pi a}
=-\frac{(2(\omega-1)/\sqrt G)^2}{8\pi}.
\tag{20}
$$

沿 R735/R806定义
$\exp(xT-T^2/(8\pi))=\sum_mH_m(x)T^m/m!$。
由(19)–(20)，monomial $\bar z^m$准确送到
$$
C_a\left(\frac{2(\omega-1)}{\sqrt G}\right)^m
 H_m(\sqrt G\,r)e^{-\pi G r^2}\,
 e^{-\pi G s^2}.
\tag{21}
$$
这显示第一因子是原 $H_m$，第二因子是真正固定 vacuum。
特别 coherent 参数包含 $\omega-1$，其六次幂为$-27$；
将这个因子称为“正实尺度”会错一个六步号。
$\varsigma_\infty$本身的 $y^{k/2}$正幅度和(101)的
$y^{-k/2}$相消，不影响(21)的相位。

## 6. 将全部相位合并后锁定原号

记原 Hermite theta 数
$$
b_{j,m}=m!s_j(\Omega_0h_\infty)^m d_{j,m},\qquad
h_\infty=\frac{\sqrt G}{204\pi i},\quad s_j\in\mathbf R^\times .
\tag{22}
$$
前述同一个未平方 theta kernel给
$$
T_{j,m+1}
=C_j^{\rm fin}R_m\,i^{-m}
 \left(\frac{2\pi i}{\Omega}\right)^{m+1}
 \left(\frac{2(\omega-1)}{\sqrt G}\right)^m b_{j,m},
\qquad R_m>0.
\tag{23}
$$
$C_j^{\rm fin}\ne0$为固定 finite projection、固定 beta theta-null、
固定 Haar及 $C_a$的乘积；$R_m$只含原 determinant、Gaussian
尺度及首 Whittaker coefficient的正实归一。
(23)不丢这些幅度：其绝对值已由 R1049(90)完整计算，
这里用未平方 kernel支付该平方不能决定的相位。
没有为每个权重新选择 $C_j^{\rm fin}$。

在相邻合法权间消去 $C_j^{\rm fin}$、$s_j$，所有复相位的
六步比由一个明确常数决定：
$$
\begin{aligned}
i^{-1}\frac{2\pi i}{\Omega}
 \frac{2(\omega-1)}{\sqrt G}\,\Omega_0h_\infty
&=-i\,\frac{\Omega_0}{\Omega}\frac{\omega-1}{51}\\
&=-\,\frac{i\epsilon_0^{-1}\omega}{17t},\\
\left(-\,\frac{i\epsilon_0^{-1}\omega}{17t}\right)^6
&=-\frac1{4\cdot17^6}<0 .
\end{aligned}
\tag{24}
$$
这里明确使用 $s_0^{-1}=1-\omega$与
$(1-\omega)(\omega-1)=3\omega$。
因此对任意 $m=4+6r$且 $d_{j,m}\ne0$，
$$
\frac{T_{j,m+1}/d_{j,m}}{T_{j,5}/d_{j,4}}
\quad\text{具有实符号 }(-1)^r .
\tag{25}
$$
若其中某个更早的系数为零，不必通过相邻比值跨过它：
(23)直接与固定 $m=4$比较，仍给(25)。

R1049的全权平方已给这个比值的绝对值为
$$
\frac{m!}{4!}\left(\frac{27}{4}\right)^r .
$$
结合(25)，得到
$$
T_{j,m+1}
=\frac{T_{j,5}}{24}\,
m!\left(-\frac{27}{4}\right)^r d_{j,m}.
\tag{26}
$$
若 $d_{j,m}=0$，完整平方同时给 $T_{j,m+1}=0$，(26)仍成立。
按原 $B_j$改写就是(2)。
由于 $\delta^6/t^6=-27/4$，逐项求和给(3)。
因此(3)保留全部 Heisenberg theta 截面和原同一个 Taylor
生成源，不只是某个孤立权的平方根比例。

## 7. 原全 Artin/Cor 和惰性残余线性值

(3)使用原外系数$j$；几何 Galois按 R1043(75)严格重标原54图。
所有 $T_{j,k}$和 $B_j$仍在原 $\eta_j$线，
而 $D_j$保持原首项及三个外系数共轭。
故 $e_\eta$平均仍为1、$\operatorname{Cor}_{L/H}$仍给$[L:H]$。
(3)没有增加或减少18、54或432。

对 $p=6u-1$，(2)给 $\varepsilon_p=(-1)^u$。
二次互反律在这条支上准确给
$$
\left(\frac3p\right)=(-1)^u .
$$
代入共同相位笔记(14)，
$s_p=-\varepsilon_p(3/p)=-1$，即得(5)。
因此对任意原三个系数 $r_{j,p}$，
$$
\sum_jr_{j,p}\overline h_{j,p}
=-[L:H]\sum_jr_{j,p}
 \frac{\overline B_j}{\overline a_{j,p}}\,
 \overline K_{j,p}(0).
\tag{27}
$$
原 Artin 基$a_{j,p}$未重选；原完整系数行和外部项没有消失。
本注没有由三项分别为单位推出(27)非零。

## 8. 实际同源变量下的全精度 Newton 来源

这是(3)对惰性原 theta completion 的直接消费。
固定一个好惰性$p$，记 $d=p+1$，
$$
c_{\sigma,p}=[z^d]\log(\sigma_0(z)/z),\quad
C_p=34c_{\sigma,p},\quad
\lambda=\delta/t,\quad R_j=B_jt^4/(408\delta).
$$
对 toric 源(3)使用其真正拉回 completion常数
$$
C_p^{\rm tor}=C_p\lambda^d .
\tag{28}
$$
以原 falling factorial $(v)_h$定义
$$
\begin{aligned}
a_{j,h}
 &=C_p^{-h}[z^{dh-2}]\bigl(D_j(z)e^{-C_pz^d}\bigr),\\
a^{\rm tor}_{j,h}
 &=(C_p^{\rm tor})^{-h}[Z^{dh-2}]
       \bigl(\mathscr G_j(Z)e^{-C_p^{\rm tor}Z^d}\bigr).
\end{aligned}
$$
对每个 $h$，在特征零逐项换元给
$$
a^{\rm tor}_{j,h}=R_j\lambda^{-2}a_{j,h}
=-\frac{B_j}{306\delta}\,a_{j,h}.
\tag{29}
$$
所以对原完整 Newton 函数、而非仅模$p$首项，
$$
\boxed{
J^{\rm tor}_{j,p}(v)
=-\frac{B_j}{306\delta}J_{j,p}(v),\qquad
K^{\rm tor}_{j,p}(v)
=-\frac{B_j}{306\delta}K_{j,p}(v).
}
\tag{30}
$$
收敛、$J\in pv\mathcal O\langle v\rangle$及全部高尾，
由已发布的原 negative-two Newton 笔记在同一逐系数等式下运输。
对固定坏集外的$p$，$\lambda$和$306\delta$均为$p$单位。
这是一个全精度、实际来源的同源恒等式。

不能把(28)免费改成 $102c_{\sigma,A,p}$。
由真正 $I_{27}$微分，
$$
c_{\sigma,A,p}=t^{-d}c_{\sigma,p},\qquad
C_p^{\rm tor}=34\delta^d c_{\sigma,A,p}.
\tag{31}
$$
虽然模$p$有 $\delta^{p+1}\equiv3$，特征零一般不等于3。
若另一来源选 $102c_{\sigma,A,p}$，
必须保留
$\exp(-(34\delta^d-102)c_{\sigma,A,p}Z^d)$的全部修正；
其模$p$相同不能推出全精度相同。
这里的 linebundle、刚性化和 completion均保(4)的实际拉回。

## 9. 对主目标的准确作用范围

(3)、(30)把原完整 toric 权族接到原 type4 的**同一个**
theta/Heisenberg 生成源，并锁定原 residual 三向量的统一负号。
它们不单独证明原指定负二端点非零，也不把新增 Picard 类、
固定54图的最高 AJ、椭圆单位 Soulé 类和 rank-two 曲线的
signed canonical 元视为同一个未比较的对象。

特别，(30)的 $J^{\rm tor}$按(28)是实际 theta source定义。
若要将它称为原几何 AJ 的全精度 regulator，仍须同一周期、
同一 integral local condition和同一 fixed cycle的 reciprocity；
R1049目前已付的首层式(5)不替代该额外等式。
原通常全 Sha 桥也仍只消费其已登记的实际 canonical $J$。

本注没有数学运行，没有重算$p=29$或任何旧原厚交作业。

### 原始文献及依赖

- N. Borade、J. Franzel、J. Girsch、W. Yao、Q. Yu、E. Zelingher，
  *On tori periods of Weil representations of unitary groups*，
  Selecta Math.31 (2025),49，§4.1.3(7)、§4.2.1、§4.2.2：
  <https://eprints.whiterose.ac.uk/id/eprint/227128/1/s00029-025-01047-4.pdf>。
- C. Chan，*Period identities of CM forms on quaternion algebras*，
  Forum Math. Sigma8 (2020),e25，§6.1 的 similitude theta定义、
  Theorem6.15及§7.1的实际 newvector：
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A307E84FB65A00F04D142EEAB168B2EE/S2050509420000213a.pdf/period_identities_of_cm_forms_on_quaternion_algebras.pdf>。
- T. Yang，*Theta liftings and Hecke L-functions*，
  J. reine angew. Math.485 (1997),25–53，(2.8)、Corollary2.4
  和原 full splitting：
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- [R806](../results/R806-original-type-four-order-eighteen-and-negative-two-katz.md)
  §§1–5、[R1006](../results/R1006-actual-full-nine-trace-and-original-katz-square.md)
  §§2–5、[R1049](../results/R1049-original-inert-syntomic-graphs-and-crystalline-lattice.md)
  §§12–14及原共同相位、negative-two Newton两篇笔记。

## 10. 同一个固定 weight3 来源的双变量核

前八节的 $\mathscr G_j$逐权改变 binary theta 的 source character。
为了把它接回原固定 $f=\theta(\psi_{27}^2)$，必须同时保留另一
rank-one theta 因子；不能只把 $k=-1$代入(3)。

仍用§5的 $a,G,A_R,A_I,S$。令
$$
I(Z,W;r,s)=\int_{\mathbf R^2}
e^{-\pi a(\sqrt3+i)(x^2+y^2)}
e^{Z(x-iy)+W(x+iy)}e^{-2\pi iaS}\,dx\,dy.
\tag{32}
$$
这是同一原 kernel 的两个 coherent 参数，未换 Gaussian、
极化或有限 Schwartz。两次完成平方准确给
$$
\begin{aligned}
I(Z,W;r,s)
={}&C_a e^{-\pi G(r^2+s^2)}
\exp\bigl(2(\omega-1)(rZ-sW)
+\kappa(Z^2+W^2)+cZW\bigr),\\
b={}&\frac{2(\omega-1)}{\sqrt G},\qquad
\kappa=-\frac{b^2}{8\pi},\\
c={}&\frac{A_R^{-1}+A_I^{-1}}{2\pi a}
=\frac1{2\pi a\sqrt3}
=\frac1{4\pi a\,\operatorname{Im}\omega}.
\end{aligned}
\tag{33}
$$
例如 $W$的一次项由 $y$积分与 $Z$情形反向，给
$-2(\omega-1)sW$；混合项取两逆矩阵的**和**，不是(20)的差。
于是正常排序后的核严格分解为
$$
\begin{aligned}
e^{-cZW}I(Z,W;r,s)
={}&C_a e^{-\pi G(r^2+s^2)}
\exp\left(\sqrt G\,r\,bZ-\frac{(bZ)^2}{8\pi}\right)\\
&\hspace{18mm}\cdot
\exp\left(\sqrt G\,s\,(-bW)-\frac{(-bW)^2}{8\pi}\right).
\end{aligned}
\tag{34}
$$
这是两个完整 Hermite coherent kernels 的乘积，非忽略交叉项
后的近似。

在 binary 变量中，相应的完整多项式为
$$
\mathcal L_{n,r}(z,\bar z)
=\sum_{\ell=0}^{\min(n,r)}
\frac{n!r!(-c)^\ell}
{\ell!(n-\ell)!(r-\ell)!}\,
\bar z^{\,n-\ell}z^{\,r-\ell}.
\tag{35}
$$
对原固定 weight3 来源取 $r=n+2$。令 $c(y)=1/(4\pi ay)$、$y=\operatorname{Im}\tau$；以下多项式先使用这个随 $y$ 的系数，最后在 $\tau=\omega$ 评价。在同一 quadratic form $a|z|^2$上有
$$
a^n\mathcal L_{n,n+2}
=z^2\sum_{j=0}^n
\binom nj\frac{(n+2)!}{(j+2)!}
\left(-\frac1{4\pi y}\right)^{n-j}(a|z|^2)^j.
\tag{36}
$$
右边正是 $\delta_3^n$逐项作用于
$z^2e^{2\pi i a|z|^2\tau}$时的多项式，采用
$\delta_k=(2\pi i)^{-1}(\partial_\tau+k/(\tau-\bar\tau))$。
证明可对 $n$归纳：对 $y^{-h}$求导给
$h/(4\pi)y^{-h-1}$，与随权 $3+2n$ 的第二项合并，
即得(36)的二项式递推。因此这一步确实返回同一个
$\theta(\psi_{27}^2)$的 raised vectors，而非另一个仅有相同
无穷型的形式。$a^n$是已指定坐标的 quadratic-form 尺度；
在 adelic 与几何微分值比较中必须保留，不能据(34)删去。

## 11. 固定来源上的完整有限角色及两个 Hermite 槽

本节只说明实际 finite source 和两个槽的身份，不预记一个
负整数的解析延拓。置
$$
\chi=\nu_{27}^{\,2},\qquad
\xi_{j,n}=\eta_j^{-1}\nu_{27}^{-(3+2n)},\qquad n\equiv4\pmod6.
$$
取与§2完全相同的 splitting $\mu=\nu_0$。
两个 rank-one Hilbert90 pullback 现在为
$$
\widetilde\alpha_1=\eta_j^{-1}\nu_{27}^{-(2n+1)}\nu_0,\qquad
\widetilde\alpha_2=\eta_j\nu_{27}^{\,2n+5}\nu_0.
\tag{37}
$$
逐项相乘、相除给
$$
\widetilde\alpha_1\widetilde\alpha_2
=\chi^2\mu^2,\qquad
\widetilde\alpha_1/\widetilde\alpha_2
=\widetilde{\xi_{j,n}|_{K^1}}.
\tag{38}
$$
完整中心延拓也保留：原 $\eta_j(\delta)=-1$，故
$$
(\chi\mu)(\delta)=-i,\qquad
\xi_{j,n}(\delta)=-i^{-(3+2n)}=-i
\quad(n\equiv4\bmod6).
$$
其与旧逐权 source 的不同 uniformizer 值由下方(39)的真实 similitude 同步处理；不能只比较 norm-one 单位。

除去共同 $\mu$后，第一因子是
$\eta_j^{-1}\nu_0^{-(2n+1)}$，因为 $3\mid2n+1$；
第二因子是 $\eta_j\kappa\nu_0^{2n+5}$。
所以第一条始终是原 R806 的 type4 finite source，
第二条始终是固定 $\beta_j=\eta_j\psi_{27}$的 type0 finite
source。其 Hermite 次数分别为 $n$和$n+2$。
有限单位、different、2/17全部邻点以及3处243项投影，
均为§3的同一组算子；没有换成两个任意存在的 theta vectors。

还须保留非单位 $\delta$的 similitude。
在 $\bar z^n z^r$上，这个真正的 lift 给
$i^{r-n}$，即在 coherent 参数中同时作
$$
Z\longmapsto-iZ,\qquad W\longmapsto iW.
\tag{39}
$$
故原固定 source 的 $r=n+2$槽给恒定相位 $-1$。
(34)的两条 Hermite 参数则同时变为 $-ibZ$与$-ibW$：
第二因子原有的负号不能遗漏。
(39)保持 $ZW$，所以完整收缩 $e^{-cZW}$也不变。
这直接解释为何单变量的六步号不能不经双变量核就套到固定
weight3 的 raised family。

这里所谓“固定 beta theta source”有具体含义：先对§3的同一个
有限 Schwartz 作用(37)的两个 torus projectors，然后按同一
全局变极化分解；第二因子就是所得 positive rank-one Schwartz。
它的 Hermite 真空非零需保新旧有限来源的接合，完整证明见
[原 full54 全精度交叉比较§3.1](2026-11-27-original-inert-full54-geometric-newton-cross-identity.md)。
准确地，旧 $m=4$的 binary character 与本节固定 character 之比为
$\nu_{27}^6$：原3处单位 Schwartz 逐点不变，唯一
$\operatorname{diag}(3,1)$字贡献共同$-1$；第一 rank-one character
完全相同，第二者之比$\nu_{27}^{12}$在全部坏处紧 torus及$\delta$上为1。
类数1的全 norm-one 理想重排保其余球向量及原无穷角色。
故旧$(4,0)$与新$(4,6)$槽之前确实是同一个 positive finite函数；
只有旧$(4,0)$和$T_{j,5}\ne0$用于支付这个真空，未把新第6槽当成真空。
以后读取 Taylor 系数始终使用此向量和同一$h_\infty$变量倍率，
不以任意另一个中心$L$值非零的向量替换。

在纯形式的槽标号上，$n=-2$是
$$
(\hbox{原 type4 的 }-2\hbox{ 槽},
 \ \hbox{原 beta 的 }0\hbox{ 槽}).
\tag{40}
$$
(40)只确定必须作正则化的两条实际来源。一个幂级数没有
$Z^{-2}$系数；因此(34)本身尚未给 Coleman/fp 值，
也不允许把其负槽定义成零。
