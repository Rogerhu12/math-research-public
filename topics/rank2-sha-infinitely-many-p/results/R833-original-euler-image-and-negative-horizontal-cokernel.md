# R833 — 原 Euler 一阶算子的完整像与至多二维负水平余核

日期：2026-11-15。**状态：以下原全局像、实际零 charge 呈示及其 $r=2$ 余核界已证明。真正高前缀 $\mathcal B_h$／镜轴核上的像，以及指定 trace 的行依赖仍开放。**

本篇接原十九角 Euler lift 和 R550 的完整交概形。
对
$$
D_{\mathcal E}:H^0(C,N^2)\longrightarrow H^0(Z,N^2|_Z),
\qquad B_0\longmapsto(\mathcal EH)|_Z,
$$
不只估计维数，而是确定其像：
它恰为在真实负水平子概形 $Z_-=C\cap H_-$ 上消失的全部值。
原 $r=2$ profile 的平衡不等式进一步给
$\operatorname{length}Z_-\le2$。

同时给出 $\ker D_{\mathcal E}$ 的同预算整系数呈示，
把该核上的高前缀条件压到原 $\mathcal H_1$ 与至多五列零 charge 多项式。
这不是把原 $\mathcal B_h$ 或 $\ker\alpha_\eta$ 的评价认成满射。

## 1. 原几何、来源与零 charge 截面

保原固定十九角曲面 $X$、实际不可约因子 $F$ 及其严格变换 $C$。
记
$$
b=\deg_YF,\quad
u=\max_n(\deg_t f_n-4n),\quad
\kappa=C^2,\quad\chi=-K_XC,
$$
$$
N=\mathcal O_C(C),\qquad
\mathcal H_m=H^0(X,\mathcal O_X(mC)),\qquad
e=\mathcal EF,\quad \mathcal E=Y\partial_Y .
$$
$C$ 不等于任何边界，$C^2\ge0$，故 $C$ nef。
各链的实际重数 $\mu_{i,j}$ 因而非增、非负，且
$\sum_j\mu_{i,j}\le b$。

令 $H_-$ 为原负截面 $Y=0$ 的严格变换。
按 R815 的准确类，
$$
H_-=S_0-E_{d,1}^*-E_{\infty,1}^*,
$$
其中星号表示全变换基。
定义
$$
\boxed{
z_-=C\cdot H_-=u-\mu_{d,1}-\mu_{\infty,1}\ge0.
}
\tag{1}
$$
这里 $z_-$ 不是先前常数 charge 多项式的 $\deg H$；
它还包括负水平在固定角处可能留下的交数。

以原 $Y$ 次数分解 $\mathcal H_m$，记 charge 零空间为 $\mathcal H_m^0$。
**引理 1。** 原 Gauss 格准确给
$$
\boxed{
\mathcal H_m^0
=d^{m\mu_{d,1}}\,
k[t]_{\le m z_-},
\qquad
\dim\mathcal H_m^0=mz_-+1.
}
\tag{2}
$$
右端的次数帽作用在去掉显示 $d$ 因子后的多项式上。

证明如下。零 charge 系数在底无穷远的原帽是 $\deg_t\le mu$。
有限正角要求
$$
\operatorname{ord}_{d=0}f_0
\ge\max_j\left\lceil\frac{mV_j^{(d)}}j\right\rceil
=m\mu_{d,1},
$$
因为 $\mu_{d,j}$ 非增。
同样，无穷远正角要求
$\deg_t f_0\le m(u-\mu_{\infty,1})$。
各负角的局部系数为 $x^{mb}f_0(t)$；
其累计值至少 $mb$，而
$V_j(F)\le b$，所以这些角不增加零 charge 条件。
合起来正是 (2)，包含全部十九角。证毕。

在 $H_-\simeq\mathbf P^1$ 上，(2) 是整个
$H^0(H_-,\mathcal O_{H_-}(mC))$，其次数为 $mz_-$。
原 $F_0(t)=F(t,0)\ne0$ 是 $\mathcal H_1^0$ 中的实际截面。
去掉固定 $d^{\mu_{d,1}}$ 因子后，其次数可严格小于 $z_-$；
缺少的次数是 $H_-$ 上无穷远的真实零，不能先假设最高系数为单位。

## 2. 真 Euler 像与原 Koszul 商

原全来源满足 $3b+\deg_YQ\le D<p$，特别 $2b<p$。
十九角的逐框公式已在
[全 Euler／α 配对](../notes/2026-11-15-original-global-euler-frames-and-complete-alpha-residue-pair.md)
支付，所以 $\mathcal E\mathcal H_m\subseteq\mathcal H_m$。

对 $\mathcal H_2$ 的所有正 charge $1\le n\le2b$，$n$ 都为单位。
因而准确有
$$
\boxed{
\mathcal E\mathcal H_2=\mathcal H_2^{>0},\qquad
\mathcal H_2/\mathcal E\mathcal H_2\simeq\mathcal H_2^0.
}
\tag{3}
$$
逆算子只逐原 charge 除以 $n$，保同一 Gauss 帽；
没有将来源上的可逆性认成物理 $M$ 像饱和。

令
$$
Z=V(F,e),\qquad
\operatorname{length}Z=\kappa,\qquad P\notin Z .
$$
由原 Koszul 序列和 R495 的
$H^1(\mathcal O_X)=H^2(\mathcal O_X)=H^1(\mathcal O_X(C))=0$，
准确有
$$
\boxed{
\mathcal H_2\longrightarrow H^0(Z,N^2|_Z)\text{ 满射},\qquad
\ker=F\mathcal H_1+e\mathcal H_1 .
}
\tag{4}
$$
同样 $\mathcal H_2\to H^0(C,N^2)$ 满射，核为 $F\mathcal H_1$。

对 $B_0\in H^0(C,N^2)$ 取原提升 $H\in\mathcal H_2$，
$$
D_{\mathcal E}(B_0)=(\mathcal EH)|_Z
$$
与提升无关，因为
$\mathcal E(FL)=eL+F\mathcal EL$ 在 $Z$ 为零。
它仍读取真正一阶 jet，不只读取 $B_0|_Z$。

由 (3)、(4) 得
$$
\begin{aligned}
\operatorname{coker}D_{\mathcal E}
&\simeq
\mathcal H_2/
(\mathcal E\mathcal H_2+F\mathcal H_1+e\mathcal H_1)\\
&\simeq
\mathcal H_2^0/(F_0\mathcal H_1^0).
\end{aligned}
\tag{5}
$$
第二步取原 charge 零投影：
$e$ 没有零 charge，故
$(e\mathcal H_1)^0=0$；
$(F\mathcal H_1)^0=F_0\mathcal H_1^0$。
没有另添扭层或把某个投影空间当成整个物理来源。

## 3. 余核就是负水平的实际值商

定义有限交概形
$$
\boxed{Z_-=C\cap H_-.}
\tag{6}
$$
$\mathcal E$ 的原线性化在整个 $H_-$ 上权为零。
这可在未吹起的稠密 $Y=0$ 开集直接读取，再沿同一个全局线束延拓；
因此 $e|_{H_-}=0$，
且 $(\mathcal EH)|_{H_-}=0$ 对全部 $H\in\mathcal H_2$ 成立。
于是 $Z_-\subset Z$ 是概形包含，并且
$$
\operatorname{im}D_{\mathcal E}
\subseteq
\ker\bigl[
H^0(Z,N^2|_Z)\to H^0(Z_-,N^2|_{Z_-})
\bigr].
\tag{7}
$$

另一方面，(2) 在 $H_-$ 上给完整限制。
对 $F_0|_{H_-}$ 的零除子 $Z_-$，序列
$$
0\to\mathcal O_{H_-}(C)
\xrightarrow{\ F_0\ }
\mathcal O_{H_-}(2C)
\to\mathcal O_{Z_-}(2C)\to0
$$
以及 $H^1(\mathbf P^1,\mathcal O(z_-))=0$ 给
$$
\boxed{
\mathcal H_2^0/(F_0\mathcal H_1^0)
\simeq H^0(Z_-,N^2|_{Z_-}).
}
\tag{8}
$$
这是自然限制映射，而非仅维数相等。

**定理 1。** 原全局算子有准确短正合列
$$
\boxed{
H^0(C,N^2)\xrightarrow{D_{\mathcal E}}
H^0(Z,N^2|_Z)\longrightarrow
H^0(Z_-,N^2|_{Z_-})\longrightarrow0.
}
\tag{9}
$$
特别
$$
\boxed{
\operatorname{im}D_{\mathcal E}
=\ker(\operatorname{res}_{Z_-}),\qquad
\operatorname{rank}D_{\mathcal E}=\kappa-z_-.
}
\tag{10}
$$
$Z_-$ 可以不约化、可以含非有理点或原固定角，
(8) 保其完整长度，不把它拆成任意独立的点值。

## 4. 原 r=2 全 profile 使余核长度至多二

此节明确加上 R792/R797/R827 已付的原 $r=2$ 完整 profile。
其中 $m_0=C\cdot f_0=3$，
四个负链长度是 $4,4,4,3$，
两个正链长度都是 $2$。
写
$$
s_i=\sum_j\mu_{i,j},\quad
m_i=b-s_i,\quad
\delta=2u-\sum_{\text{正链}}s_i,\quad
\tau=\sum_{\text{负链}}\frac{m_i}{n_i}+\frac{\delta}{2}.
$$
R827 对实际全部 masks 证明 $\tau\le13/4$。
由 (1) 与正链非增性，
$$
\frac{\delta}{2}
=z_-+
\frac{(\mu_{d,1}-\mu_{d,2})
+(\mu_{\infty,1}-\mu_{\infty,2})}{2}
\ge z_-.
$$
其余负链 $m_i\ge0$，而 $m_0=3$ 位于四步链，故
$$
\frac34+z_-\le\tau\le\frac{13}{4}.
$$
$z_-$ 为整数，得到
$$
\boxed{
0\le z_-\le2,\qquad
\operatorname{rank}D_{\mathcal E}\ge\kappa-2.
}
\tag{11}
$$
这里没有把 $\deg H\le2$ 直接当成 $z_-\le2$；
固定角留下的负水平交数是由完整平衡不等式一并控制的。

余核 (8) 可用原 $F_0$ 的实际二元齐次化写成至多
$5\times3$ 的乘法商。
重根、无穷远零或不分裂二次点都保在同一个原小矩阵里，
没有以任选两个补向量替换它。

## 5. 核的同预算实际呈示

令 $\mathcal E_+^{-1}$ 是正 charge 上逐项除以 $n$ 的原单位逆。
定义
$$
\mathcal I_F(L)=\mathcal E_+^{-1}(eL)\in\mathcal H_2,
\qquad L\in\mathcal H_1.
\tag{12}
$$
$eL$ 的零 charge 为零，所以定义无歧义，
并且准确有 $\mathcal E\mathcal I_F(L)=eL$。
所有分母 $n\le2b<p$ 都为单位。

对 $V\in\mathcal H_2^0$ 定义
$$
\Phi(L,V)=\bigl(\mathcal I_F(L)+V\bigr)|_C.
\tag{13}
$$

**定理 2。** 同一个实际核有准确呈示
$$
\boxed{
0\longrightarrow k\oplus\mathcal H_1^0
\xrightarrow{\ \iota\ }
\mathcal H_1\oplus\mathcal H_2^0
\xrightarrow{\ \Phi\ }
\ker D_{\mathcal E}\longrightarrow0,
}
\tag{14}
$$
其中
$$
\boxed{
\iota(c,L_0)=
\bigl(2cF+L_0,\ cF_0^2+F_0L_0\bigr).
}
\tag{15}
$$

证明。若 $D_{\mathcal E}(B_0)=0$，取原提升 $H$。
由 (4)，$\mathcal EH=F A+eB$，$A,B\in\mathcal H_1$。
取零 charge 得 $F_0A_0=0$，所以 $A_0=0$。
用原正 charge 逆写 $A=\mathcal EK$。
则
$$
\mathcal E(H-FK)=e(B-K),
$$
故 $H-FK=\mathcal I_F(B-K)+V$，$V\in\mathcal H_2^0$，
证明 (13) 满到整个核。

若 $\Phi(L,V)=0$，则
$\mathcal I_F(L)+V=FK$，$K\in\mathcal H_1$。
施 $\mathcal E$ 得
$$
e(L-K)=F\mathcal EK.
$$
$C$ 整且 $e|_C\ne0$，故 $L-K=cF$。
继而 $\mathcal E K=ce$，所以 $K=cF+L_0$，
$L_0\in\mathcal H_1^0$，从而 $L=2cF+L_0$。
最后用
$$
\mathcal I_F(2cF)=c(F^2-F_0^2),\qquad
\mathcal I_F(L_0)=FL_0-F_0L_0
$$
得到 (15) 的 $V$。
反向直接代入；因 $F$ 有正 charge，$\iota$ 单射。证毕。

维数随之准确为
$$
\boxed{
\dim\ker D_{\mathcal E}
=\dim\mathcal H_1+z_--1
=\frac{\kappa+\chi}{2}+z_-.
}
\tag{16}
$$
这是全局来源算子的核，仍未加入任何原物理高前缀。

## 6. 真高前缀与镜轴条件不能省

取实际
$$
\mathcal B_h=H^0(C,N^2(-hP)).
$$
定理 2 给其与 $\ker D_{\mathcal E}$ 的准确小呈示：
$$
\boxed{
\Phi(L,V)\in\mathcal B_h
\iff
\pi_h\bigl[
\mathcal I_F(L)(t,g(t))+V(t)
\bigr]=0.
}
\tag{17}
$$
因为原 $g-\psi$ 的阶为 $h$，
在长度严格小于 $h$ 的前缀中可用 $g$ 替换 $\psi$；
这里没有增加一行未付精度。
在原 $r=2$ 全 profile 中，
$V$ 的原空间至多五维，其余是整个真 $\mathcal H_1$；
并非另造任意可选函数。

若还要求 $\Phi(L,V)\in\ker\alpha_\eta$，仍须同一个镜轴长度 $q=T-h$。
(12) 的真正全局恒等式给
$$
(\mathcal E(\mathcal I_F(L)+V))|_C=e\,L|_C.
$$
因此原 R524 连接在这个核上准确简化为
$$
\boxed{
\alpha_\eta(B_0)
=\left[\frac{B_0}{2\eta e}\right]
\in\operatorname{coker}E_q ,
\qquad B_0\in\ker D_{\mathcal E}\cap\mathcal B_h.
}
\tag{18}
$$
$L|_C$ 是同一个原 $E_q$ 像，故可在该商中去掉；
这不允许删除其它 $B_0$ 的 normal 项。

式 (17)、(18) 以及指定 trace 在这些真实列上的值仍须联立判断。
(11) 没有证明
$D_{\mathcal E}(\mathcal B_h)$ 等于 (10) 的全像，
更没有证明 $\ker\alpha_\eta$ 可以给任意 $Z$ 值。
高前缀可能缩小这个像，所有余条件都依赖同一个 $L,V,H,R$。

## 7. 与原 α 转置、完整 M 的范围

全局配对继续是
$$
\alpha_\eta^*\omega(B_0)
=
\operatorname{Res}_P\frac{B_0\omega}{2\eta e}
-\langle D_{\mathcal E}(B_0),\omega|_Z\rangle_Z.
$$
本篇支付了第二项中 $D_{\mathcal E}$ 的完整未加前缀像，
以及其核的实际较小呈示。
第一项、允许全局 $\omega$ 的十九角／conductor 条件，
和两项必须来自同一个 $\omega$ 的相关性都没有改变。

原 $P_{134}/U_0$、同一个 $P^{\rm fact}+pR$、
全部原 $\mathcal W_D$ 余列、两条十三行 carry 和下一位仍保。
来源端逐 charge 的单位逆不是原物理像饱和，
几何余核长度至多二不是原 $M$ 只剩两个自由障碍。
指定 forcing 与主目标均未完成。

依赖：
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R550](R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)；
[R815](R815-complete-original-mori-nef-cones-and-s-fibration.md)；
R827 的原平衡恒等式与全 $r=2$ profile 上界；
[十九角 Euler／α 配对](../notes/2026-11-15-original-global-euler-frames-and-complete-alpha-residue-pair.md)。
本篇只用原有限 Gauss 格、同一个 Koszul 序列和完整 Serre 接口，没有新程序运行。
