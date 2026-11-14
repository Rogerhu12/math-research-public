# R145：同一实际直母线片的连续共同度量与真实曲率证书

2026-11-12，fd2d geometry，接 R136、R137、R139。

**已证明。** 对 R137 保存的同一个有限 Cartesian 直母线位置图，整个角圈、整个径向范围上的诱导度量相对其原 flat-coast 度量的算子误差严格小于
$$
\frac{71}{2000000000}=3.55\times10^{-8},
\tag{1}
$$
实际曲面处处浸入，且两个实际主曲率满足
$$
\max_i|\kappa_i|<\frac{73}{10}<\frac{125}{17}=\frac1{.136}.
\tag{2}
$$
证明没有假设保存的标架准确正交、入口角结构方程准确相容或有限 Gauss–Codazzi 残差为零。本文只认证原基准 $\delta=0$ 的这段实际位置图，不将证书转给 R144 或其它非零 $\delta$ 外设计后的未知场。它也不单独证明全核闭合、嵌入、非局部 reach 或无限维精确解存在。

## 1. 唯一输入与实际位置图

输入是
`notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz`，SHA256
`ed69b9a6599ef75f36f2d5bc094d152d993baeb078f4852a392648b85f6c9c3a`。
它由 R137 从已保存的新34轨道在共享入口 $s_c\simeq.592$ 被动重建得到；不是把原 DOP 求解器没有保存的中间位置状态冒作现存数据。

令 $\phi$ 是固定 balanced seed 法向角，材料入口角为 $t=U_0(\phi)$，
$$
h(\phi)=U_0'(\phi)=\rho_*(\phi)/a_0>0.
$$
保存的 $X,e_1,e_2$ 是明确的有限 Fourier 多项式，最高整数波数384；保存的 n、m 是明确的实偶/奇有限 Fourier 多项式，最高波数190。所有系数取其保存 binary64 字节所定义的准确二进制有理值。零模、Nyquist 模的权重及实部约定与 R137 provider 完全一致。

记
$$
k=m/n,\quad G=e_1-ke_2,\quad
F(\phi,w)=X(\phi)+wG(\phi),\qquad0\le w\le W(\phi).
\tag{3}
$$
正标量 a、v、L 是同一 R137 coast 输入，数值约为
$$
a=1.029181699754392,\quad v=.2587478542495509,\quad
L=.2755434451024161.
$$
实际严格计算的 a 区间同时包含准确 $a_0$ 加共享 jet 所给的半径与保存的数值半径；v 同样覆盖共享速度和保存值。其完整二进制区间绑定原 ruling 证书，没有用短小数取代定义。

设 $\rho_c=a/v$。完整径向边界为
$$
W=\frac{L(2\rho_c+L)}{\rho_c+
\sqrt{\rho_c^2+(1+k^2)L(2\rho_c+L)}}.
\tag{4}
$$
由 $1+k^2\ge1$ 直接得到 $0<W\le L$。

R137 已闭的全角 Arb 证书对同一 n、m、h 给出 $n>19/100$、
$$
D=a+w\left(v(1+k^2)-k_\phi/h\right)>1/20
\tag{5}
$$
以及全角 ruling 坐标的严格单值逆。D 关于 w 仿射，所以其全径向下界由两个端点给出。R139 的形式曲率在本文只作为某些标量恒等式的现成区间输入，绝不代替 (3) 的实际曲率。

## 2. 目标度量在直母线坐标中的矩阵

目标是原来的
$$
g=d\sigma^2+(a+v\sigma)^2du^2.
\tag{6}
$$
R137 明确给出 $(\phi,w)\leftrightarrow(\sigma,u)$ 的坐标变换。也可将其发展到平面：在角度 $vt$ 的局部平面正交基中，位置为
$$
(\rho_c+w)e_r(vt)-wk e_\theta(vt).
$$
这张平面图的两个导数列，在同一旋转正交基中的分量是
$$
z=\binom{1}{-k},\qquad
y=\binom{vhwk}{h(a+vw)-wk_\phi},\qquad J_0=(z\ y).
\tag{7}
$$
因此 (6) 拉回 $(w,\phi)$ 后的矩阵准确为 $J_0^TJ_0$，而
$$
\det J_0=hD>0,\qquad
e_2^TJ_0^{-1}=\frac{(k,1)}{hD}=:b.
\tag{8}
$$
这里的平面正交基只是计算目标度量的表示；不假设实际 $e_1,e_2$ 正交。

## 3. 先相消再估计的真实 metric 恒等式

令 $M=(e_1\ e_2)$，定义以下实际有限场的缺陷：
$$
\begin{aligned}
H&=M^TM-I,\\
C&=X_\phi-ah e_2,\\
B&=n(e_1)_\phi-m(e_2)_\phi-vh(me_1+ne_2),\\
d&=C+\frac wnB.
\end{aligned}
\tag{9}
$$
B 的定义已将准确相容公式中会相消的法向项消去；它是实际多项式表达式，不是把误差设为零。

直接微分 (3)，使用 $m/n=k$，逐项整理得
$$
F_w=Mz,\qquad F_\phi=My+d.
$$
所以按目标正交坐标归一后的实际微分为
$$
(F_w\ F_\phi)J_0^{-1}=M+db.
\tag{10}
$$
置 $q=M^Td$，则实际相对度量误差矩阵准确等于
$$
\boxed{(M+db)^T(M+db)-I
=H+qb+b^Tq^T+|d|^2b^Tb.}
\tag{11}
$$
特别地
$$
\|g^{-1/2}(F^*\langle\cdot,\cdot\rangle-g)g^{-1/2}\|_{op}
\le\|H\|_{op}+2|q|\,|b|+|d|^2|b|^2.
\tag{12}
$$
这是同一个实际 F 的诱导度量。由于 (10) 中的归一基在目标度量下正交，所得算子范数正是目标相对误差，未用坐标分量误差替代它。

### 3.1 径向与标量盒的完整预算

记全角严格上界
$$
\begin{aligned}
H_*&\ge\|H\|_{op},& C_*&\ge|C|,& B_*&\ge|B|,\\
Q_C&\ge|M^TC|,& Q_B&\ge|M^TB|.
\end{aligned}
$$
在一个已认证标量角盒中，用 $n\ge n_*>0$、$h\ge h_*>0$、$D\ge D_*>0$。
令 $S_0=n(1+k^2)$；这只是代数标量，虽然原文件把它称作兼容情形的入口曲率，此处不将它当成实际曲率。若 $S_0\le S_*$，则
$$
|b|\le\beta:=\frac{\sqrt{S_*/n_*}}{h_*D_*},
\quad |q|\le Q_C+\frac L{n_*}Q_B,
\quad |d|\le C_*+\frac L{n_*}B_*.
$$
代入 (12) 得到完整径向界
$$
U_{box}=H_*+2\beta\left(Q_C+\frac L{n_*}Q_B\right)
+\beta^2\left(C_*+\frac L{n_*}B_*\right)^2.
\tag{13}
$$
原 ruling 证书的每个角盒给出 n、$\rho_*=a_0h$、入口 $S_0$ 和末端 D 的区间；取 $D_*=\min(a_{low},D_{end,low})$ 即覆盖全部 w。n、m、h 的准确 D2 对称性使其四分之一角圈证书覆盖整圈。另一方面，本节所有实际 Cartesian 多项式残差都作全角 Fourier 系数界，不假设近似位置标架也具有准确对称性。

## 4. 完整 Fourier 卷积与材料图册无限尾

准确材料图册已有
$$
h=1+2\sum_{j\ge1}\mu_j\cos(2j\phi),
\quad \mu_j=\frac1{2\pi a_0}\int_0^{2\pi}\rho_*(\phi)\cos(2j\phi)\,d\phi.
\tag{14}
$$
使用已经发布的512个准确均值区间：
`2026-11-12-fd2d-balanced-weighted-means-512-02.json.gz`，SHA256
`41bb9029e103d2a4d93ea635e77fbab5d1a42d9764eeeac6052c91d08b33b4e3`。
这些区间已经包含梯形混叠误差及准确矩的不确定度。

`2026-11-12-fd2d-balanced-chart-512-proof.md` 已证明在解析带宽 $1/20$ 下
$|\mu_j|\le M e^{-j/10}$，$M=(r+D_{seed})/a_0$，对 $j>2$ 有效。
所以有限 h 多项式以外的全部无限尾满足
$$
\epsilon_h\le\frac{2M e^{-513/10}}{1-e^{-1/10}}
<3.482\times10^{-21}.
\tag{15}
$$
程序直接消费每个均值的完整区间，不先舍入成新的浮点系数；因此 (15) 只须支付无限尾，没有遗漏有限均值区间误差。

所有保存的 Fourier 场转换成复 Laurent 多项式后，在 Acb192 位区间算术中先完成 (9) 的卷积和相消，再估计系数范数。没有频率截断或 FFT 混叠。$M^TB$ 的最高可能整数波数为1982，整个有限乘积均保留。

对有限 Laurent 多项式 $P=\sum c_j e^{ij\phi}$，使用
$$
\sup_\phi|P|\le\sum_j\bigl(|\operatorname{Re}c_j|+|\operatorname{Im}c_j|\bigr).
\tag{16}
$$
区间端点向外取界，所以这包括每次卷积运算的舍入。向量分量再取平方和上界，H 用对称 $2\times2$ 矩阵的最大行和上界。

令 $\Delta h$ 是 (15) 的尾。未进入有限卷积的贡献准确为
$$
\Delta C=-a\Delta h\,e_2,\qquad
\Delta B=-v\Delta h\,(me_1+ne_2).
$$
对切向投影还使用
$$
\Delta(e_i\cdot C)=-a\Delta h\,(e_i\cdot e_2),
$$
$$
\Delta(e_i\cdot B)=-v\Delta h\,[m(e_i\cdot e_1)+n(e_i\cdot e_2)].
\tag{17}
$$
各点积以已求 H 的界支付。这样保留了切向缺陷远小于完整三维缺陷的真实相消，未将小的法向缺陷不必要地线性加入 metric。

### 4.1 实际连续 metric 结果

源码 `scripts/fd2d_k0_ruling_metric_convolution.py`，SHA256
`650d4d32ac5a51a8866c362171ed7f2daf1564af7dde6c3aa0b2cb4336a3a3f1`。
真实 session19051 / 最终 chunk `0d1440` / 自然 exit0，4.952587145秒。

向外取短小数的严格充分界为
$$
\begin{aligned}
H_*&<2.612\times10^{-14},\\
C_*&<3.044\times10^{-9},&B_*&<2.179\times10^{-8},\\
Q_C&<1.609\times10^{-11},&Q_B&<1.820\times10^{-9}.
\end{aligned}
$$
每个角盒按 (13) 另行使用其严格标量界，最大值的准确二进制上界约为
$3.547080323121506\times10^{-8}$。该准确有理数小于 (1)，故得到 (1)。

报告 `notes/2026-11-12-fd2d-k0-ruling-metric-convolution-01.json`，SHA256
`1db13655fe83e9a9430dc16a647765477438024e574d66f04c4c58d90d5671ec`。
真正的上下界位于报告的二进制字段；其短小数 display 本身不承担向外舍入。

## 5. 从实际 Cartesian 两 jet 求实际曲率

本节完全不使用 (9) 缺陷小或准确 Gauss–Codazzi 相容的假设。
以 $\phi$ 为导数记号，直接由 (3) 得
$$
F_w=G,\quad F_\phi=X'+wG',\quad
F_{ww}=0,\quad F_{w\phi}=G',\quad F_{\phi\phi}=X''+wG''.
$$
设
$$
C_0=G\times X',\quad C_1=G\times G',\quad
C_w=C_0+wC_1,\quad A(w)=|C_w|^2.
$$
当 $A>0$，实际单位法向是 $N=C_w/\sqrt A$。令
$$
E=|G|^2,\quad F_1=G\cdot(X'+wG'),\quad f_0=C_0\cdot G'.
$$
由于 $C_1\cdot G'=0$，真实第二基本形式的混合项为 $f_0/\sqrt A$，径向项为零。定义
$$
P(w)=E\,C_w\cdot(X''+wG'')-2F_1f_0.
\tag{18}
$$
A 和 P 均为 w 的二次多项式。实际形算子的迹与行列式准确为
$$
T=\frac{P(w)}{A(w)^{3/2}},\qquad
\det S=-\frac{f_0^2}{A(w)^2}.
$$
因此两个真实主曲率绝对值的最大值是
$$
\boxed{\max_i|\kappa_i|
=\frac{|P|+\sqrt{P^2+4f_0^2A}}{2A^{3/2}}.}
\tag{19}
$$
这里实际高斯曲率可为微小负值，没有将有限曲面强行替换成准确可展曲面。

若某连续盒内 $0<A_-\le A\le A_+$、$|P|\le P_+$、$|f_0|\le f_+$，则
$$
\max_i|\kappa_i|\le
\frac{P_++\sqrt{P_+^2+4f_+^2A_+}}{2A_-^{3/2}}.
\tag{20}
$$
程序只在严格正的 $A_-$ 上使用这个式子；它同时认证实际浸入。报告中的 `curvature_upper` 是 (20) 所算**上界值的包含区间**，其下端不宣称是实际曲率的下界。

## 6. 曲率区间的完整角向和径向覆盖

Cartesian Fourier 逐分量显式评价前96波，余下有限波数97至384的第 d 阶导数以
$$
\sum_{j>96}j^d(|a_j|+|b_j|),\qquad d=0,1,2,3,4,
\tag{21}
$$
包围，没有丢弃它们。n、m 的全部保存模逐项评价。

先以实际 Fourier 四阶导数构造区间 Taylor jet，系数约定为导数除以阶乘。乘法用有限卷积；倒数按
$$
b_0=1/a_0,\qquad
b_j=-a_0^{-1}\sum_{i=1}^j a_i b_{j-i}
$$
递推，仅在已证明 n 正的角盒上应用。故 k、G 及 (18) 的各径向系数的全部二阶角导数都有完整包含式。

对角盒中点 c 和 $\Delta=\phi-c$，每个最终二次多项式系数 f 使用
$$
f(\phi)\in f(c)+f'(c)\Delta+\tfrac12f''(I)\Delta^2.
\tag{22}
$$
这先保留真实代数相消，再包围角间变化；余项由完整四阶原始 Fourier 导数支付。对跨零区间 $\Delta$ 使用显式乘积 $\Delta\cdot\Delta$，允许其区间比真正平方更宽，但始终包含真值。

径向取 $\tau=w/W(\phi)\in[0,1]$ 的16个等分条带。每个条带的完整 w 范围以向外端点包围。对二次多项式 $p_0+p_1w+p_2w^2$ 在 $[l,r]$ 上，使用三个 Bernstein 系数
$$
p(l),\qquad p(l)+\frac{r-l}{2}p'(l),\qquad p(r)
$$
的凸包。因为相应 Bernstein 基函数非负、和为1，这给出 A、P 在该完整径向条带上的区间。

最终实际运行使用 Arb160 位，516个角盒不留空隙地覆盖 $[0,2\pi]$，每个角盒16个完整径向条带，共8256盒。所有盒严格通过 $A>0$ 和 (20) 小于 $73/10$，没有未决盒。因此 (2) 成立。

源码：

- `scripts/fd2d_k0_ruling_actual_curvature_taylor.py`，SHA256 `1cee03ba2044040811d4b115fc7c954638e9cbb30bd382629e151567d7a5135c`；
- 其实际代数 helper `scripts/fd2d_k0_ruling_actual_curvature_certificate.py`，SHA256 `85f71d57d298a3308962fdbd452465025ebecf096d831cb10dcac39cd6e47dd4`。

真实 session63760 / 最终 chunk `b5a130` / 自然 exit0，67.838855303秒。
报告 `notes/2026-11-12-fd2d-k0-ruling-actual-curvature-certificate-05.json.gz`，SHA256
`49757e19101aeed2167b27432cab93725c4c84dd29c92a53ef7f1354494ae6fe`。
它只保留各角盒的径向聚合严格界，小于190KB；未分配角对矩阵。

早期粗区间、跨零通用幂和一个非有限诊断区间造成的真实停止/失败另存为尝试记录。它们没有被改写成几何不可能性。最终完整证书绑定上述实际通过的源和输入，未借用失败计算的状态。

## 7. 全时范围、近对角条件及仍缺的闭图工作

若对这段同一基准曲面使用材料相位族 $F_\alpha=R_\alpha F\tau_{-\alpha}$，目标度量 (6) 对材料角平移不变，空间旋转也不改变 metric、曲率或浸入性，所以 (1)–(2) 对全部相位准确保留。该陈述只覆盖这段已定义的曲面片，不自动接合其它未知部分。

(2) 给这段的局部主曲率半径严格大于 $10/73>.136$。全局 reach 仍须排除非局部靠近；即使整个曲面都满足曲率界，也不能单凭 (2) 宣称 reach。

一个可供后续近对角覆盖使用的准确条件是：若 P、Q 有长度 $\ell\le\pi/(2K)$ 的单位速曲面测地线相连，且沿线实际主曲率绝对值不超过 K，则
$$
|Q-P|^2\ge\frac{4\sin^2(K\ell/2)}{K^2},\qquad
|N_P\cdot(Q-P)|\le\frac{1-\cos(K\ell)}K.
$$
证明：测地线作为空间曲线的曲率不超过 K；切向量之间的夹角不超过 K 乘弧长差，二重积分其内积给第一式。初始切向垂直 $N_P$，沿途切向在 $N_P$ 方向的分量绝对值不超过 $\sin(Ks)$，积分给第二式。因此两向正常球半径 $1/K$ 的条件成立。**patch 边界可能使这样的短测地线离开已认证域**，所以这个存在或延拓前提必须另行支付，本文不将它冒作全部近角径向对已付。

已经完成的连续位置证书、正常球凸二次归约及严格镜像分离仍可分别使用。当前片尚缺与其它上片的接合和跨片正常球、同片全部角对的连续球排除，以及完整新闭核的实际同 g 加密与网格。一个已验证有限片不会替代 README 的完整强目标；也没有从 (1) 单独推出准确等距解或无限 C² 收敛。
