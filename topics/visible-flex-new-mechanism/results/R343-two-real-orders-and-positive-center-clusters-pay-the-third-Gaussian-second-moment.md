# R343：两种真实排序与双中心群支付第三 Gaussian 面积的完整第二外矩

日期：2026-11-15。**完整原式纸面构造。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R341](R341-companion-directions-and-three-centers-pay-the-third-Gaussian-first-moment.md) 已在同一弱单 hook、真实 rank-two 圆上支付第三 Gaussian 面积 $A_{-1,-2}$ 的第零、第1外矩。本稿支付它的全部相位第2外矩，并保持两个旧完整面积、$\Psi$、三条 directed 行与此前指定完整一层。

新的模块全部位于强 hook 区。四种真实原型来自原两坡、两宽度族的两种合法次序和普通／伴随两种方向；其第一外矩向量有严格正核。完整 $[R,S]$ 第二外矩经原 self 和真实尾化成一个固定向量，不随新间距增长。因而四种原型的第二矩平移斜率也有严格正核。把它们复制到两个真实正中心群，给出一个四维正锥，可以在令新增第一矩准确为零的同时支付第二矩的任意实际残差。

最后以完整伸缩权 $-5,-4,-7$ 分别跟踪第一矩、第二矩与 $\Psi$，使这八个新强模块的正 $\Psi$ 成本任意小。R341 已付的三个弱块中心、第一中心矩和第二中心矩全部不动。最后的有限频率纠正仍只在原强控制器内进行。

主要来源：[R259 全部原面积矩](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R267 原 self 与实际母形状](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R269 真实重新排序](R269-reordered-real-masses-pay-a-complete-Gaussian-zero-moment.md)、[R275 原第一矩与有序有限和](R275-first-moment-obstruction-for-the-small-width-two-slope-family.md)、[R337 真实算子平移](R337-true-translation-excludes-the-same-sign-reflected-weak-block-architecture.md)、R341，以及 [R293 同有限观察的有限频率根](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)。

## 1. 同一规范与新增联合目标

保持 R341 的同一真实有限几何、弱单 hook 及共振 Gaussian 端芽。仍取
$$
0<t=\kappa^2<1/100,\qquad h_e>0,
$$
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\qquad
W_*=aR+bS,\quad Z_*=d_*L+e_*U,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d_*=\frac{6\kappa t}{h_e},\quad
e_*=-\frac{\kappa(15t+1)}{4h_e}.
\tag{1}
$$
对 $u=f\cos\theta+g\sin\theta$、$D=f\odot f-u\odot u$，记
$$
\mathcal M_j=I_j\{u,[W_*,P](u;D)\},\quad
\mathcal A_j=I_j\{u,[Z_*,P](u;D)\},
$$
$$
\mathcal B_j=I_j\{u,[Z_*,W_*](u;D)\},\quad
\mathcal R_j=I_j\{u,[R,S](u;D)\}.
\tag{2}
$$
原 $I_2$ 包含 $2u'w'$，不可仅取 $x^2u''w''$。

本稿构造同一个最终圆使
$$
\boxed{
\mathcal M_j=\mathcal A_j=\mathcal B_j=0
\quad(j=0,1,2),\qquad
\Psi=F_0=F_1=F_2=0
}
\tag{3}
$$
全部相位成立。所有量仍是原完整函数和真实积分；没有将它们改成 principal 条件。

## 2. B2 的完整平移式确实含新的 R2

令
$$
\chi_\kappa=\frac{\kappa(28t^2-35t-4)}{64h_e^3}\ne0.
$$
在原弱 hook、旧 $\mathcal M_j=0$ 下，R337 的完整 commutator 展开与
$$
I_2(T_su,T_sw)=I_2(u,w)+2sI_1(u,w)+s^2I_0(u,w)
$$
给出
$$
\boxed{
\begin{aligned}
\mathcal B_2^{(s)}
={}&\mathcal B_2+2s\mathcal B_1+s^2\mathcal B_0\\
&+(a+b)(s\mathcal A_2+2s^2\mathcal A_1+s^3\mathcal A_0)\\
&+\chi_\kappa(s\mathcal R_2+2s^2\mathcal R_1+s^3\mathcal R_0).
\end{aligned}}
\tag{4}
$$
二次 commutator 平移项由原 $[R,P],[S,P]$ 的全部三个旧外矩消去。外 $x^2$ 权和原 $2u'w'$ 项一起处理，才得到(4)。

即使当前 $\mathcal B_0=\mathcal B_1=\mathcal A_j=0$，也不能删去 $s\chi_\kappa\mathcal R_2$。本稿先准确识别新强模块的 $\mathcal R_2$，再使用(4)，不挪动 R341 已付的弱块中心。

## 3. R/S 的完整单包 self 与原尾

对任意实紧 $v$，写
$$
p=v',\qquad r=v'',\qquad A=J(r^2).
$$
原定义
$$
R(v,v)=p^2+xA,\qquad S(v,v)=J(xr^2)
$$
给
$$
R'=2pr+A-xr^2,\quad R''=2(p-xr)r',
$$
$$
S'=-xr^2,\quad S''=-r^2-2xrr'.
$$
对一般第二输入 $w$，
$$
R(v,w)''=r'w'+(p-xr)w'''-xr'w'',
$$
$$
S(v,w)''=-rw''-x(r'w''+rw''').
$$
代入并相减，得到
$$
\boxed{\tau:=[R,S](v;v^2),\qquad
\tau''=2(xr-p)rr'.}
\tag{5}
$$
真实右 collar 给
$$
\boxed{
\tau'=\frac23xr^3-pr^2-\frac13J(r^3).
}
\tag{6}
$$
最后的真实常尾保留。无需假设单包的三个原矩为零。

记
$$
C=\int r^4,\quad X_1=\int xr^4,\quad X_2=\int x^2r^4,
$$
$$
N_0=\int pr^3,\quad N_1=\int xpr^3,\quad
V_2=\int p^2r^2,\quad U_3=\int vr^3.
$$
由(5)、(6)，原 self 矩准确为
$$
\boxed{
\begin{aligned}
S_{R,S,0}(v)&=\frac C3,\\
S_{R,S,1}(v)&=-\frac23X_1+\frac43N_0,\\
S_{R,S,2}(v)&=-\frac53X_2+\frac{16}{3}N_1-4V_2-\frac43U_3,
\end{aligned}}
\quad S_{X,Y,j}=2I_j\{v,[X,Y](v;v^2)\}.
\tag{7}
$$
例如 $I_2$ 的 $x^2v''$ 项给
$-5X_2/6+4N_1/3$，$2v'\tau'$ 给
$4N_1/3-2V_2-2U_3/3$。后一步只用紧 outer 的
$\int v'J(r^3)=\int vr^3$，没有设 $J(r^3)$ 的左值为零。

此 pair 的原跨包核全部为零：
$$
\boxed{\Gamma_{R,S,j}=0,\qquad j=0,1,2.}
\tag{8}
$$
若 inner 包在 outer 右方，$R(v_{\rm in},v_{\rm in})$ 的真实左尾是
$\mu_0x$，$S(v_{\rm in},v_{\rm in})$ 的左尾是 $\mu_1$。恰有
$$
R(v_{\rm out},\mu_1)=0,\qquad
S(v_{\rm out},\mu_0x)=0.
$$
inner 在 outer 左方时两输出均已为零。剩余 nested 输出的二次原尾与另一个紧 outer 的 $I_j$ 正交。这是原式相消，不是把所有单包 inner 输出假称紧。

## 4. 四个原型共享一个实际 R2 向量

从 R267/R341 初始母包构造中选一个固定 even 实紧 $v_0$ 及其真实 TM3 伴随 $\widehat v_0$，满足
$$
v_0^{(p)}v_0^{(q)}
=\widehat v_0^{(p)}\widehat v_0^{(q)},\qquad
\mathbf I(v_0,\widehat v_0)=0,\qquad
\mathcal F_\kappa(v_0)=0.
\tag{9}
$$
该最后等式由真实正幅、正宽母参数和非零 minor 支付。此后母包固定；不假设它是最终控制器所需的最大秩点。

固定
$$
\alpha=\frac9{20},\qquad
\beta=\frac{5-\alpha}{1-\alpha}=\frac{91}{11},\qquad
q_0=\frac1{16(1-\alpha)^2}=\frac{25}{121}>\frac15,
\quad n=2^{11}.
\tag{10}
$$
采用原 $64n$ 低包、$n$ 高包及两宽度，幅度与 R267 完全相同。两组准确满足
$$
V_L-V_H=\nu(v_0)(1-q_0^2).
\tag{11}
$$
每个最小子包沿真实实 rank-one 方向，所以 full strong hook 为零。

对 $\eta_{w,\xi}=w^{3/2}v_0((x-\xi)/w)$，(7)的第三分量给
$$
S_{R,S,2}(\eta)
=-\frac{5C}{3w}\xi^2+w\,S_{R,S,2}(v_0).
$$
定义同一真实母包的有限数
$$
K_{RS}=-\frac53(X_2-C\nu)
+\frac{16}{3}N_1-4V_2-\frac43U_3.
\tag{12}
$$
不要求该数为零，也不将它当作独立自由量。

由(8)、原两坡系数恒等及(11)，八／十二包装后的未加倍 $\mathcal R_2$ even 向量恰为
$$
\boxed{
r_*=
\frac{\mathcal W}{2}n(\beta-1)\delta(1-q_0^2)
K_{RS}\,(\alpha\beta,1),
}
\tag{13}
$$
其中 $\mathcal W>0$ 是同一完整包装的实际四次权和。向量坐标依次为
$\cos^2\theta\sin^2\theta,\sin^4\theta$。

关键是：(13)不依赖两组中心的共同间距，不依赖下面两种次序，也不依赖普通／伴随选择。不同真实排序只要保持(11)，中心二阶项就准确消去。伴随在最细包仅翻转第二系数，所有 even local self 保持；odd 由十二完整副本清去。

## 5. 两种合法排序，全部原矩与尾都保留

第一种为原居中次序 $\rho=0$；第二种为 R269 的实际重新排序 $\rho=20$。在辅助 shape 坐标，低中心为
$$
t^L_{k,l}=64A(k-c)+A(l-31.5),\qquad c=(n-1)/2,
$$
高中心为
$$
t^H_k=B_\rho(k-c)+\rho A\sigma_k,\qquad
\sigma_k=(-1)^{\operatorname{popcount}(\lfloor k/4\rfloor)},
$$
$$
B_\rho^2=
\frac{A^2((64n)^2-1)-12\nu(1-q_0^2)-12\rho^2A^2}{n^2-1}.
\tag{14}
$$
实际中心为 $\xi_0+\delta t_i$，$\delta>0$ 是有限正宽。以下间距极限可先在任意固定 $\delta$ 上证明；其第一矩与 $\mathcal R_2$ 均同乘正因子 $\delta$，所以也可在有限 $A$ 固定后再选择这个公共正宽。

原 TM 符号 $\epsilon_k$ 与 $\sigma_k$ 满足
$$
\sum\sigma_k=\sum(k-c)\sigma_k=0,\quad \sigma_k^2=1,
$$
$$
\sum\epsilon_k\sigma_k=\sum k\epsilon_k\sigma_k=0.
\tag{15}
$$
因此 real 三矩由(11)支付，imaginary 三矩在展开实际一、二次中心后也准确为零。没有假设新高次符号矩仍与旧排列相同；高次 odd 全部使用同一个十二完整副本支付。

先取有限 $A>10+\sqrt\nu$。R269 的严格间隙给
$63A<B_{20}<64A$，原 $B_0>64A$。$\rho=20$ 的高包分别在本 cell 第12／13或52／53个低包之间；真实漂移小于 $A/100$。原居中高包在第32／33个低包之间。各排序是分别定义的严格不交族，没有让一个包沿路径穿过另一个包而继续使用旧公式。

每种排序都有普通与真伴随两个版本。原三矩、full strong hook、八副本的完整第三以及 R267 的全部两面积
$$
\mathcal M_j=\mathcal A_j=0,\qquad j=0,1,2
\tag{16}
$$
在所有这些实际对象上成立。这里用(9)的母形状方程，但不要求 R269 最后六能量分支的主 $\alpha$ 根。固定(10)后，(11)、(15)、(16)仍是原逐参数身份。

## 6. 四种 B1 向量的严格正锥

令 $v_{\rho,\pm}(A)$ 为四种完整包装后的未加倍 $\mathcal B_1$ even 向量。第二下标为普通／伴随，后面可按需要重命名。

### 6.1 每种排序的两个差方向反号

R341 的完整 self/Green 身份为
$$
E_{22}-E_{04}
=\operatorname{Re}S_{Z,W,1}(f+ig),
$$
$$
S_{Z,W,1}(q)
=\mathscr L_\kappa(q)+\frac{k_*}{2}\int[J(q''^2)]^2,\qquad
k_*=\frac{d_*b}{2}-e_*a\ne0.
\tag{17}
$$
$E$ 是 $2\mathcal B_1$ 的系数。真实 local 实部用(11)后不随 $A$ 改变。

写
$$
a_c=q_0(1-\alpha),\quad
\ell_c=2q_0\sqrt\alpha,\quad H_c=2\sqrt\beta.
$$
R269 的真实 ordered sum 给普通版
$$
\operatorname{Re}\sum_{i<j}z_i^2z_j^2(t_j-t_i)
=n\left[
A\{-a_c^2(21856+64\rho^2)+32\ell_c^2\}
+\frac{H_c^2B_\rho}{2}
\right].
\tag{18}
$$
$\rho=20$ 的括号严格大于 $281A/2$；$\rho=0$ 严格大于 $1109A/2$。所以普通版
$\operatorname{Re}\int[J(q''^2)]^2$ 的 $A$ 系数为负。全部单包自项只是与 $A$ 无关的真实常数。

伴随版的 imaginary primitive 在每个外包内真紧；其 real primitive 原式给
$$
\begin{aligned}
\operatorname{Re}\int[J(q''^2)]^2
=\delta\bigg\{&
nm^2a_c^2A(21856+64\rho^2)
-\frac{na_c^2\Delta_u}{2}(64q_0+4096)\\
&-4nK_u(64\alpha q_0^3+\beta)
\bigg\}.
\end{aligned}
\tag{19}
$$
$K_u,\Delta_u$ 是同一实际母包的完整 self 积分，不被省略。故在每种排序内，充分大有限 $A$ 给两个
$$
\Delta(v):=v_{22}-v_{04}
$$
严格相反的符号。其 $A^{-1}$ 归一极限也都严格非零。

### 6.2 两种排序的 sine-four 方向也反号

这一步使用 R275(13)、(14)的完整第一外矩，而不是用第6.1节的 pure 差猜测 sine-four。两种方向版本在 $\theta=\pi/2$ 的 quadratic/local 数据相同，故每个固定排序的 $v_{04}$ 相同。

按 R275 原记号，除共同正因子 $\delta n a_cm^2$ 外，其
$2\mathcal B_1(\pi/2)/k_*$ 的 $A$ 极限系数为
$$
z_\rho=
21840q_0+512-(64q_0+1/2)\rho^2
-\frac{16}{3}(64q_0+1)D_\rho,
$$
$$
D_\rho=\frac{4095-12\rho^2}{b_\rho+64},\qquad
b_\rho=\lim_{A\to\infty}B_\rho/A
=\sqrt{4096+\frac{4095-12\rho^2}{n^2-1}}.
\tag{20}
$$
原 finite-width self、母形状余项和 $\nu$ 全保留在有界余量中；母包固定后它们除以 $A$ 趋零。

对 $\rho=0$，$b_0>64$，所以
$$
\boxed{z_0>10920q_0+\frac{2731}{8}>0.}
\tag{21}
$$
对 $\rho=20$，$63<b_{20}<64$，准确重写为
$$
z_{20}=312-3760q_0+
\frac{3760(64q_0+1)}{b_{20}+64}.
$$
于是
$$
\boxed{
z_{20}<\frac{43384-236880q_0}{127}
<-\frac{3992}{127}<0,
}
\tag{22}
$$
最后使用 $q_0>1/5$。这些是原有限公式的严格极限余量。故一个足够大但有限的 $A$ 使两种实际 $v_{04}/k_*$ 分别严格为正、负，不把 $A=\infty$ 当成真实 profile。

### 6.3 正核与第二矩斜率

在坐标 $(v_{22}-v_{04},v_{04})$ 中，每种排序的两个原型有相同非零第二坐标、第一坐标反号。先在每组内部用正权令第一坐标为零，再用两组相反的第二坐标正幅相消，得到四列的严格正 kernel。四列秩为2。因此
$$
\operatorname{cone}\{v_1,v_2,v_3,v_4\}=\mathbb R^2.
\tag{23}
$$
所有系数都是实际正四次幅权。

由(13)，四种原型具有同一个实际 $\mathcal R_2$ 向量 $r_*$。定义
$$
s_\ell=2v_\ell+\chi_\kappa r_*,\qquad 1\le\ell\le4.
\tag{24}
$$
$A^{-1}v_\ell$ 的极限已在(17)–(22)逐项证明具有秩2和严格正 kernel，而 $A^{-1}r_*\to0$。故再增大一次有限 $A$，秩和严格正 kernel 的开放性给
$$
\boxed{\operatorname{cone}\{s_1,s_2,s_3,s_4\}=\mathbb R^2.}
\tag{25}
$$
这里不是从 span 自动推正锥：两套列都保留了具体严格正 kernel，有限扰动由一个固定非零 minor 纠正即可。

现在固定这个有限 $A$、实际母包、正宽 $\delta$ 及全部八／十二内部复制。以后不再改变四原型的形状或内部次序。

## 7. 原型中心的 B2 为零，最后物理平移是准确线性式

两种排序的中心均反射对称。因为 $n/4=2^9$，
$$
\sigma_{n-1-k}=-\sigma_k,
$$
所以(14)的高中心也按 $k\leftrightarrow n-1-k$ 成对反射。普通版 $f$ 奇、$g$ 偶；伴随版 $f,g$ 都奇。

原 $[Z_*,W_*]$ 的空间反射号为负，$I_2$ 的两项给同一个号；真实右锚产生的二次多项式按原 $I_2$ 正交准确消失。因此辅助中心的 $\mathcal B_2$ even 部分为零。原 $\mathcal B_0,\mathcal R_1$ even 也为零。

八副本和十二副本都取四次权中心零。各 translated 副本的 $\mathcal B_2$ even 新增项由(4)是其中心乘
$2v_\ell+\chi_\kappa r_*$；其中心正权和为零。odd 项由原十一差分消去。于是每个最终强原型准确满足
$$
\boxed{
\mathcal B_0=\mathcal R_0=\mathcal R_1=0,\qquad
\mathcal B_2(\text{辅助中心})=0,
}
$$
$$
\mathcal B_1=v_\ell,\qquad \mathcal R_2=r_*.
\tag{26}
$$
同时(16)全部保持，且其 $\Psi=\psi_\ell\sin^2\theta$，$\psi_\ell>0$。

由完整(4)，把第 $\ell$ 个原型放到实际中心 $X$ 后，
$$
\boxed{
(\mathcal B_1,\mathcal B_2)=(v_\ell,Xs_\ell).
}
\tag{27}
$$
该式保全部 local、ordered primitive 与 copy 方差；$r_*$ 并未被假定为零。

## 8. 两个正中心群给四维严格正锥

每个原型的有限包络已经固定。选四个固定间隔偏移 $d_\ell$，使同一中心群内四个包络严格不交。再选有限 $L>0$，使第一群中心
$$
\xi_\ell^-=L+d_\ell
$$
及其全部包络在正半轴内。第二群取
$$
\xi_\ell^+=T+d_\ell
$$
并令 $T$ 足够大，使两群严格分开。

令 $V$ 为列 $v_\ell$ 的 $2\times4$ 矩阵，$S$ 为列 $s_\ell$ 的矩阵。把第二矩坐标除以 $T$，八个真实列在 $T\to\infty$ 时趋于
$$
\mathscr M_\infty=
\begin{pmatrix}
V&V\\
0&S
\end{pmatrix}.
\tag{28}
$$
由(23)、(25)，$V,S$ 各秩2，故(28)秩4。

还需严格正 kernel。取 $z>0$ 使 $Sz=0$。因 $V$ 的正锥是整个平面，可选 $y>0$ 使
$$
Vy=-Vz.
$$
可先取一个非负表示，再加 $V$ 的严格正 kernel 保证所有分量严格正。于是
$$
\mathscr M_\infty(y,z)=0,\qquad (y,z)>0.
\tag{29}
$$

固定(28)的一个非零四列 minor。对足够大的有限 $T$，实际矩阵仍有该非零 minor；只在这四个分量上作一个趋零的线性纠正，便把(29)改成实际矩阵的严格正 kernel。正性与秩都保留。因而未归一的真实八列
$$
m_{\ell,\pm}=(v_\ell,\xi_\ell^\pm s_\ell)
$$
满足
$$
\boxed{\operatorname{cone}\{m_{\ell,\pm}\}=\mathbb R^4.}
\tag{30}
$$
这已经是有限、严格分离的两组实际位置，不要求取极限 profile。

正锥结论也可直接解释：任意有限四向量先由秩4解一个实线性表示，再加足够大的严格正 kernel，得到全部正四次权。这里所有列由同一个母包和两个实际次序给出，没有独立指定积分坐标。

## 9. 保持 R341 的全部中心，低成本支付 B2

消费 R341 第9节之后、尚未加入最后强控制器的完整部分。此时其两个负弱块、一个正弱块、六个强面积模块的实际位置和正权都已固定，满足
$$
\mathcal M_j=\mathcal A_j=0,\quad
\mathcal B_0=\mathcal B_1=0,
$$
$$
\Psi=-\Delta_0\sin^2\theta,\qquad \Delta_0>0.
\tag{31}
$$
这些位置此后完全不动。其当前真实 $\mathcal B_2$ 是一个有限 even 向量 $b\in\mathbb R^2$；全部 odd 已由实际包装清去。$b$ 包括 R341 两种弱块的完整中心三次项、所有 local、所有原尾及强模块贡献。

固定第8节的有限八列矩阵 $\mathscr M$、严格正 kernel $k>0$ 和一个真实线性右逆 $R_{\mathscr M}$。对新强原型作共同正伸缩 $H$，把最终实际中心取为
$$
X_{\ell,\pm}=H\xi_\ell^\pm.
$$
其内部相对位置和宽度同时按同一 $H$ 伸缩。

完整齐次次数为
$$
\mathcal B_1:H^{-5},\qquad
\mathcal B_2:H^{-4},\qquad
\Psi:H^{-7}.
\tag{32}
$$
前两式直接由原 $Z_*,W_*$ 的 $-1,-2$ 权及完整 $I_j$ 得出；$\Psi$ 是原八导数 local 四次全式。它们不是 principal 估计。

给每个伸缩块的正四次权取为 $H^5c_i(H)$，其中
$$
\boxed{
c(H)=k+R_{\mathscr M}(0,-b/H).
}
\tag{33}
$$
固定 $k$ 后，足够大的有限 $H$ 使全部 $c_i(H)>0$，且这些系数一致有界。原矩阵身份准确给
$$
\sum_i c_i(H)v_i=0,\qquad
\sum_i c_i(H)\xi_i s_i=-b/H.
$$
因此新八块对第一矩准确贡献零，对第二矩准确贡献 $-b$：
$$
\boxed{
\mathcal B_1^{\rm new}=0,\qquad
\mathcal B_2^{\rm new}=-b.
}
\tag{34}
$$
它们各自的两个旧完整面积和 $\mathcal B_0$ 已为零。因此加入后第三面积的三个完整外矩都准确为零。

新增 $\Psi$ 恰为
$$
H^{-2}\left(\sum_i c_i(H)\psi_i\right)\sin^2\theta.
\tag{35}
$$
括号有界且非负。选择一个足够大但有限的 $H$，使它小于 $\Delta_0/2$。这样仍有负储备
$$
\Psi=-\Delta_1\sin^2\theta,\qquad \Delta_1>\Delta_0/2>0.
\tag{36}
$$
没有用无限伸缩、负四次幅度或未计算的零成本方向。

第8节所有无量纲包络都在严格正半轴内。随 $H$ 增大，整个新八块包络移到固定 R341 部分的右方；彼此相对间隙同样乘 $H$，保持严格分离。可以一次选有限 $H$ 同时满足(33)、(35)及支撑要求。原 R341 的三个中心均未移动，原第一、第二中心矩支付没有被重做或破坏。

## 10. 最后 Psi 与三条完整行仍在同一 profile 上支付

从构造起点保留 R341 的真实有限
$$
\mathcal F_\star=(\mathcal F,\int(v'')^4)
$$
及其最大秩母包、非零 minor、固定纠正方向和两种 even 振荡形状。新四原型无须是这个 regular 母包；第9节八块此后全部固定。

在其余最终不交正包络中构造原 R280/R293 强控制宏块。它自己的全72面积准确为零，包含本稿第三面积的全部三个外矩。以真实正四次权准确支付(36)的负 $\Psi$。

只在该控制器内进行原同 $\mathcal F_\star$ 的有限频率纠正。完整实际三行仍有
$$
\mathbf F_N(\mathbf z)
=\mathbf F_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1).
\tag{37}
$$
基线包含 R341 固定弱部分、新八块、所有最终位置、实际 amplitudes、原尾与低阶项。R325 的真实三维正锥与严格正 balance 给一个有限 $N$ 的准确根
$$
F_0=F_1=F_2=0.
\tag{38}
$$
同 $\mathcal F_\star$ 保控制器全72面积及 quartic 值，故本文全部九个已列外矩和 $\Psi=0$ 都保持。新八块不参加该形状纠正。

由原完整一层恒等，还保留
$$
[\sigma h^{-2}j^0]\mathscr R_{-3,\theta}=0
\quad\text{全部 }\theta.
\tag{39}
$$
仍只授该完整必要系数，不授整个一层函数。

## 11. 全部真实依赖与加法范围

本稿的主要选择顺序是：

1. 固定真实几何及非零 $\kappa$，从起点固定最后控制器的 $\mathcal F_\star$ 接口。
2. 取 R341 已付 $\mathcal B_0,\mathcal B_1$ 且仍有负 $\Psi$ 的实际部分；其三个弱中心、所有旧幅度、原宽恢复和六个面积模块完全固定。
3. 独立选择第4节真实正宽母包及其伴随，固定(10)。按第5节准确方差分别定义两种合法次序。
4. 以第6节严格 finite-limit 余量一次选定一个有限 $A$，使四个第一矩列和四个第二矩斜率列都具有严格正 kernel。随后固定正 $\delta$、全部内部八／十二副本与四次权。
5. 固定第8节两个正中心群及实际四维矩阵、右逆和正 kernel；选第9节一个有限 $H$，同时实现全部准确值、低 $\Psi$ 成本和严格支撑。
6. 放入最后强控制器，固定所有位置、复制、权和实际基线。再选共同有限正 $I$ 及同一右锚，最后取有限 $N$。
7. 全部零式完成后只作共同正幅归一化，并固定新的 seed 目标 metric；不再平移或伸缩任何已付模块。

固定有限几何的 $h>0$、$\omega$ 有界，原合法条件在充分右半轴有统一正间隙。因此新有限包络可以直接安排在该半轴；最后只取包含既定坐标的有限 $I$。没有扩大旧冻结区间而声称原目标未变，也没有在(34)后整体搬移旧弱部分。

每个被相加的完整块都是原三矩圆，所以所有所用 $XD_\theta$ 真紧。两个完整块之间的同点 inner 乘积为零；同块 nested 输出的真实二次左尾与另一个紧 outer 的 $I_0,I_1,I_2$ 准确正交。故所有面积、两 directed 方向和三条 $F_i$ 都按完整原式相加。第6节微包的 ordered 项没有使用这条完整块局域性，仍全部保留在原有限和里。

原完整三阶由真实几何 $M=0,T=\kappa_H\mathfrak H$、弱单 hook、原八副本 full range、同一初值和右锚保持。新模块均在强区；旧弱核心的真实 rank-two 开段没有改变。没有增加一般不必要的第二 hook。

## 12. 准确新增结论与剩余门

同一个新的实际有限圆已经完成三个 Gaussian 面积
$$
A_{-2,-3},\qquad A_{-1,-3},\qquad A_{-1,-2}
$$
的全部三外矩、全部相位，同时保留原三矩、完整三阶、$\Psi$、三条完整 directed 行和指定完整一层(39)。

原 R337、R275 等特定架构的障碍均不撤回。本稿使用了 R339 真正异号弱部分以及新两种真实排序；新四原型只消费母形状和矩身份，不把旧六能量主根的参数冻结条件偷改成任意值。

其余 Gaussian 面积、其它对称乘积、零／一层完整函数、canonical 平台与退化通量、完整第四 period 和同一 gauge 的 joint 仍未支付。这里的九个外矩只是已完成条件的准确列举，不是独立秩声明。最后控制器自身的全72零仍没有扩成整个弱强圆的全72零。
