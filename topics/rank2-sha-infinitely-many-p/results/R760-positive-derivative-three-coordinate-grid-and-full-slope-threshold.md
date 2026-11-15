# R760 — 原正阶导数的三坐标格、全普通整性与严格斜率门

日期：2026-11-15。**状态：以下三坐标独立性、全部饱和 jet 的局部范数、真实旗标乘积公式及条件门槛已证明。**

使用原 $S_{34},T_{72}$，并加入由 $S_{34}$ 的**正阶 z 导数**
构成的固定整函数。本篇的第三个坐标具有真实有界测度呈示，
因此普通位没有自由参数列所产生的导数损失。
所得三维门是
$$
a_I+3b_I<6,
$$
但无条件惰性成本仍为 $(a_I,b_I)=(0,3)$。
没有将原两个中央零传播到这个新增来源，也没有把旧二维
$\mathcal W_D$ 的 Smith 结论搬到新格。

## 1. 固定物理函数与一个新的六重不变坐标

保持 R418 的共同 $E_1:y^2=x^3+1$、同一个 sigma 和参数：
$$
t=-x^{-3},\qquad\Theta=x\sigma^2,\qquad w=z^6,
$$
$$
f(t)=\frac{t(t-1)(16t^2+4t+7)(1+8t)}7,
$$
$$
V_0(t)=(1-4t)(1-20t-8t^2)(1+96t+48t^2-64t^3).
$$
为完全区分导数变量，记物理函数为
$$
\mathscr S(z)=\Theta(z)^{17}f(t(z))=S(w),\qquad
\mathscr T(z)=\Theta(z)^{36}f(t(z))V_0(t(z))=T(w).
\tag{1}
$$
原 $S(w)=w+\cdots,\ T(w)=w+\cdots$。
定义
$$
\boxed{
\mathscr U(z)=(\partial_z\mathscr S(z))^6=U(w),\qquad
U(w)=6^6w^5\left(\frac{dS}{dw}\right)^6 .
}
\tag{2}
$$
这里没有把 $\partial_z$ 换成 $\partial_w$ 后删掉 $6z^5$。

因 $\mathscr S(\zeta z)=\mathscr S(z)$，$\zeta\in\mu_6$，
其 z 导数的类型为5，第六次幂仍为型零。
故 $U$ 是整个 w 平面上的整函数，系数在 $\mathbf Q$，
且
$$
U(w)=6^6w^5+\cdots .
\tag{3}
$$
三个原点值均为0。本文的 $U$ 是新定义的 (2)，
**不是**原第三条算术来源 $U_{136}$；后者的中央条件不被用于 (2)。

## 2. 三个真实坐标代数独立

先证明
$$
\operatorname{trdeg}_{\mathbf C}\mathbf C(t,\Theta,\zeta)=3,
\qquad \zeta=\sigma'/\sigma .
\tag{4}
$$
R418 已付 $t,\Theta$ 独立以及原 equianharmonic 格的
$$
\eta(\lambda)\lambda=\frac{\pi}{A_\Lambda}|\lambda|^2>0.
\tag{5}
$$
沿任一非零周期 $\lambda$，
$$
t(z+n\lambda)=t(z),\qquad
\zeta(z+n\lambda)=\zeta(z)+n\eta(\lambda),
$$
$$
\Theta(z+n\lambda)=\Theta(z)
 \exp\!\left(2n\eta(\lambda)z+n^2\eta(\lambda)\lambda\right).
\tag{6}
$$
若存在非零多项式关系
$\sum_{j=0}^M P_j(t,\zeta)\Theta^j=0$，
取 $P_M\ne0$，并选 $z_0$ 避开有限极点和零点，
使 $P_M(t(z_0),Z)$ 不是零多项式。
代入 (6) 后，每个 $P_j$ 都是 n 的多项式，
最高 j 项除去其指数后为非零多项式。
其余项相对它按 $\exp(-c n^2+O(n))$ 衰减，$c>0$；
非零多项式不可能被这些项抵消。
$M=0$ 时同样由 n 的无限多个值直接矛盾。
清分母后该论证覆盖所有代数关系，证明 (4)。

R418 的准确式
$$
\frac{S^{36}}{T^{17}}=\frac{f(t)^{19}}{V_0(t)^{17}}
\tag{7}
$$
表明 $\mathbf C(t,\Theta)$ 代数于 $\mathbf C(S,T)$。
另一方面 $\mathscr S=\sigma^{34}\phi_S(x)$，
其中 $\phi_S$ 是同一个原有理函数，且
$$
\partial_z\mathscr S
=34\zeta\,\mathscr S+
 2y\,\sigma^{34}\partial_x\phi_S(x).
\tag{8}
$$
(8) 的第二项代数于 $\mathbf C(t,\Theta)$：
$x^3=-1/t,\ y^2=x^3+1,\ \sigma^{34}=\Theta^{17}x^{-17}$。

若 $U=(\partial_z\mathscr S)^6$ 代数于 $\mathbf C(S,T)$，
则 $\partial_z\mathscr S$ 也代数于该域，
(8) 将使 $\zeta$ 代数于 $\mathbf C(t,\Theta)$，与 (4) 矛盾。
因此
$$
\boxed{\operatorname{trdeg}_{\mathbf Q}\mathbf Q(S,T,U)=3.}
\tag{9}
$$
这确是新增的第三个方向，不是将原 $U_{136}$ 或另一有限
theta 来源重复计数。它也不属于旧 $\mathbf Q(t,\Theta)$
的任何有限代数扩张，故不能借旧有限 conductor 将新列识别成旧列。

## 3. 完整真实格和饱和前缀

使用固定单项式整格
$$
E_D^{\partial}=
\bigoplus_{a+b+c\le D}\mathbf Z X^aY^bZ^c,\qquad
N_D=\binom{D+3}{3}.
\tag{10}
$$
这里的 $Z$ 是 (2) 的坐标标签，不是自由物理变量。
定义原普通系数评价
$$
r_k(P)=[w^k]P(S(w),T(w),U(w)),
$$
$$
K_{D,k}=
\ker_{\mathbf Q}(r_0,\ldots,r_{k-1})\cap E_D^\partial,\qquad
\varphi_D^k=r_k|_{K_{D,k}\otimes\mathbf Q}.
\tag{11}
$$
局部范数取 (10) 的最大系数范数，
实范数取同一基的 Euclidean 范数。
这些都是全部 D、全部 k 的真实饱和核，
不是先选一条 mod p 核再任意提升。

由 (9)，非零 $P$ 不可能使全部 $r_k(P)$ 为零。
所以旗标有准确 $N_D$ 个秩一跳跃，位置记为
$$
0\le k_1<\cdots<k_{N_D}.
\tag{12}
$$

## 4. 复侧仍为三分之一增长阶

R418 给原 $\mathscr S,\mathscr T$ 的有限型界
$\log\max(1,|\mathscr S(z)|,|\mathscr T(z)|)\le C(1+|z|^2)$。
对 $\mathscr S$ 用半径1的 Cauchy 导数估计，
其 z 导数仍满足同型界，固定第六次幂也一样。
于是
$$
\sup_{|w|\le R}\log\max(1,|S(w)|,|T(w)|,|U(w)|)
 \le C_0(1+R^{1/3}).
\tag{13}
$$
全部次数的同一 Cauchy 优化遂给
$$
\boxed{
\log\|\varphi_D^k\|_\infty
\le-3k\log k+3k\log D+O(k+D).
}
\tag{14}
$$
常数只依赖固定三个函数。单项式数 $N_D$ 的 Euclidean
换范数只添 $O(\log D)$，已在余项中。
没有将新坐标的完整 theta 次数204计成34；
它只改变固定型常数，不改变 (14) 的主系数。

## 5. 全部好普通位：新增导数仍是有界测度

取 R418 同一个普通整测度规范和单位周期 $\Omega_p$。
物理生成函数满足
$$
A_p(Z)=\mathscr S(\Omega_p\log(1+Z))\in\mathcal O[[Z]].
$$
准确链式法则给
$$
\boxed{
(\partial_z\mathscr S)(\Omega_p\log(1+Z))
=\Omega_p^{-1}(1+Z)\partial_Z A_p(Z)\in\mathcal O[[Z]].
}
\tag{15}
$$
形式导数只将系数乘整数；$\Omega_p$ 是单位。
因此 (2) 的完整第六次幂也整。

更具体地，若 $\nu_S$ 是原有界测度，真实新增测度为
$$
\boxed{
\nu_U=\Omega_p^{-6}\,
\Sigma_*\!\left((x_1\cdots x_6)\nu_S^{\otimes6}\right),
\qquad\Sigma=x_1+\cdots+x_6.
}
\tag{16}
$$
所以这是原 S 的六个正一阶矩的加法卷积。
所有输入都在 $\mathbf Z_p$，权的范数不超过一；
并未假定 Mellin 值对这个加法卷积具有乘法性。

任意 (10) 中局部系数范数不超过一的 P，
其真实生成函数仍是范数不超过一的有界测度 $\mu_P$，
且
$$
\mu_P(x^{6h})=\Omega_p^{6h}(6h)!r_h(P),\qquad
\mu_P(x^m)=0\quad(6\nmid m).
\tag{17}
$$
在同一个前缀 (11) 上，
下降阶乘 $\prod_{j=0}^{6k-1}(x-j)$ 的全部低阶矩为零。
它在 $\mathbf Z_p$ 上被 $(6k)!$ 整除，
故最高阶乘与 (17) 准确抵消：
$$
\boxed{\|\varphi_D^k\|_p\le1
\quad\text{对全部好普通 }p\equiv1\pmod6,\ D,k.}
\tag{18}
$$
这就是新格的全部普通饱和预算；没有额外 $k\log D$ 项。
(18) 来自正阶物理导数和完整卷积，
不同于在旧来源外添一个自由 w 坐标。

## 6. 全部惰性位：实际无条件包络没有减少

取 R418 的同一好惰性位与
$$
\rho_p=p^{-p/(p^2-1)} .
$$
对任意物理半径 $r<\rho_p$，
R418 已付
$$
\|\mathscr S\|_r,\|\mathscr T\|_r\le r^6.
$$
普通导数的 Gauss 范数满足
$\|\partial_z F\|_r\le r^{-1}\|F\|_r$，
因为 $|n|_p\le1$。因此
$$
\|\partial_z\mathscr S\|_r\le r^5,\qquad
\|\mathscr U\|_r\le r^{30}.
\tag{19}
$$
于是全部 P 的范数仍不超过一。
令 r 从内部趋于 $\rho_p$，得到对所有真实饱和层
$$
\boxed{
\log\|\varphi_D^k\|_p
\le e_p(k)\log p,\qquad
e_p(k)=\left\lfloor\frac{6kp}{p^2-1}\right\rfloor .
}
\tag{20}
$$
没有宣称 Gaussian 在临界圆周上收敛，
也没有删除其首极系数。

由同一个模六 Mertens 和，
$$
\boxed{
\sum_{p\equiv5(6)}e_p(k)\log p
=3k\log k+O(k).
}
\tag{21}
$$
固定坏位的实际三个函数都有正局部半径，全部成本为 $O(k+D)$。
所以新格的无条件惰性主系数仍是3。

## 7. 饱和旗标的完整乘积公式与新严格门

为明确量词，这里直接在 (10)–(12) 的同一格上使用乘积公式。
在每个秩一跳跃处，赋予
$K_{D,k}/K_{D,k+1}$ 原 Euclidean 商范数及各处的饱和商格。
$\varphi_D^k$ 的算子范数就是对应商线的范数。
选其整数生成元后，非零评价属于 $\mathbf Q$；
产品公式与商线协体积的望远镜相消给
$$
\boxed{
0=\sum_{j=1}^{N_D}
\left(\log\|\varphi_D^{k_j}\|_\infty+
      \sum_p\log\|\varphi_D^{k_j}\|_p\right).
}
\tag{22}
$$
标准单项式格的协体积为1，
每个有限位的饱和商生成元范数为1。
因此 (22) 没有把 mod p Smith 基当作有序有理核，
也不需要假设所有 $k_j=j-1$。

假设能在**这个同一新格**的全部非零层证明
$$
\sum_{p\equiv5(6)}\log\|\varphi_D^k\|_p
\le a_I k\log D+b_I k\log k+O(k+D),
\quad a_I,b_I\ge0.
\tag{23}
$$
令 $B_D=\sum_j k_j$。由 (12)，
$B_D\ge N_D(N_D-1)/2$。
凸性给
$$
\sum_j k_j\log k_j
\ge B_D\log(B_D/N_D)
\ge B_D(3\log D-O(1)).
\tag{24}
$$
约定 $0\log0=0$。将 (14)、(18)、(23)、(24) 代入 (22)，
在 $b_I<3$ 时得到
$$
0\le (a_I+3b_I-6)B_D\log D+O(B_D+N_DD).
\tag{25}
$$
而 $N_DD=o(B_D)$。所以
$$
\boxed{a_I+3b_I<6\quad\Longrightarrow\quad\text{矛盾}.}
\tag{26}
$$

若 (23) 是由原中央同时失败推出的，
则 (26) 才可用来排除该失败。
本文无条件证明了 (23) 的 $(0,3)$，它没有达到 (26)。
旧二维原格的 $a_I+2b_I<3$ 仍按其自身来源和全部旗标使用；
两格的局部改善不能混算。

## 8. 一个全 D 的截断后果及其准确范围

固定 $C>0$、$0\le\theta<2$。
若某个 D 的全部非零饱和层在每个好惰性
$p>CD^\theta$ 都整，则 (20) 与 Mertens 的上界给
$$
\sum_{p\equiv5(6)}\log\|\varphi_D^k\|_p
\le3\theta k\log D+O(k+D).
\tag{27}
$$
这里对小于 $\max(2,CD^\theta)$ 的素数直接求 (20) 的上界；
不把某个单层 cutoff 当成全层 cutoff。
隐常数对 D、k 一致，可以依赖 C。

取 $(a_I,b_I)=(3\theta,0)$，
同一个 (22)–(25) 表明 (27) 对充分大 D 不可能成立。
因此有准确的无条件反读：

**对每个固定 $C>0$、$0\le\theta<2$，
每个充分大的 D 都存在好惰性 $p>CD^\theta$、
一个真实非零跳跃 k 和整数 $P\in K_{D,k}$，使**
$$
\boxed{v_p([w^k]P(S,T,U))<0.}
\tag{28}
$$
由 (20)，该 k 必满足 $k\ge(p+1)/6$。
局部负范数可在饱和整数核的一组整数基中取到，
所以 (28) 确实可选全局整数 P，而非只有一个局部向量。

(28) 是新增固定来源格的大惰性负 jet，
并不是原 $J'_S,J'_T$ 的非零证书。
R581/R584 的长积分格有各自更高维的截断门及普通分布费用；
本篇不将那些积分列的成本转给 (2)，也不以 (28) 替代原算术传播。

## 9. 原中央、旧 canonical 格及下一步

新增坐标的实际来源是 (16)，所以任何原中央传播都必须保
六个原输入、加法和的单位域以及全部正权。
单独的 $J'_S(0)=0$ 不意味着该加法卷积的 Mellin 值或导数为零。
原 $J'_T,J'_{U_{136}}$ 同样没有被额外赋给它。

旧 $\mathcal W_D$ 的全部有理来源位于
$\mathbf Q(t,\Theta)$，而 (9) 严格增加了一个方向。
因此 R495/R743/R750 的十九角、单位块和指定 forcing
尚不是 (10) 的全层估计；旧共同因子、来源饱和和 Gaussian
都不能用一个有限列变换自动消掉这个区别。

现在可继续检验的具体问题是：
原完整中央失败能否给 (10)–(11) 的惰性改善 (23)，
并达到 (26)，或给严格小于二次的全层 cutoff。
需要的是这个实际格的有序饱和核，而非只计算一个归一化矩阵的单位秩。
原二维 \xi 留数与同一个 R 路线也继续保持其全部条件。

依赖：
[R418](R418-jzero-two-source-growth-and-full-degree-slope-budget.md)；
[R159](R159-degree-sensitive-direct-slope-boundary.md) 的旗标原理在第7节已对新格重写。
本篇没有执行新的数学计算，没有生成可重算输出。
