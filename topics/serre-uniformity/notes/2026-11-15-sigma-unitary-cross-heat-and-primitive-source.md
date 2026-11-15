# 原三同源 unitary 家族、交叉 heat 与准确本原投影

日期：2026-11-15。会话：serre-public-astra-20261115 / sigma_uniform。

**已证明的结构接口；指定非零问题仍开放。** 下文构造原 CM 点上整个 degree $(6,6)$ theta 空间的一个不同模参数延拓，保留全部 $36$ 个截面。原点的整段函数是原 $\sigma^6\boxtimes\sigma^6$，不只匹配一个数值。交叉 heat 与首 $p$ Heisenberg 关系允许准确运输 R770 的本原掩码。本文没有证明投影后的原 $FG$ 分量非零，也没有完成原 Legendre test vector 的比较；不登记为 R835。

## 1. 原点、实际极化和三同源

始终固定原
$$
E_0:y^2=x^3-1,\qquad dz=dx/(2y),\qquad
\sigma=z+O(z^7),\quad(\log\sigma)''=-x,
$$
以及 $\zeta^2+\zeta+1=0$、$s=\zeta-\zeta^2$，故 $s^2=-3$。
原两个截面仍为
$$
F=x\sigma^6,\qquad G=-xy\sigma^6.
\tag{UH1}
$$

置
$$
H=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
J=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\qquad
C=\begin{pmatrix}1&\zeta\\1&\zeta^2\end{pmatrix}.
\tag{UH2}
$$
逐项相乘给
$$
J^2+J+I=0,\quad J^tHJ=H,\quad
C^\dagger C=H,\quad
CJ=\operatorname{diag}(\zeta,\zeta^2)C,\quad
\det C=-s.
\tag{UH3}
$$
这里 $C^\dagger=\bar C^t$。在 $E_0^2$ 上，$C$ 是实际 CM 同源，
次数为 $\operatorname N_{K/\mathbb Q}(-s)=3$，不是 degree-six 截面空间的自作用。

对任一椭圆曲线 $E$，矩阵 $H$ 给 $E^2$ 上 type $(1,3)$ 的极化。
它的核为 $\{(P,-P):P\in E[3]\}$。在带实际 cyclic-3 子群
$\mathcal C\subset E[3]$ 的家族上，取
$$
\mathcal K=\{(-Q,Q):Q\in\mathcal C\}.
$$
它是该极化核的极大各向同性子群：阶为三，交替 Weil 配对在循环子群上为一。
下降使用 theta-group 的线性化；所选循环各向同性子群在有限 level 覆盖上有提升。
具体是 Moonen, *The Theta group of a line bundle*, Theorem 8.10、Corollary 8.11、
Proposition 8.15 的同源下降，不能省略该线性化。因而商
$$
q:E^2\longrightarrow \mathcal A=E^2/\mathcal K
\tag{UH4}
$$
携带主极化 $\lambda_{\mathcal A}$，满足 $q^*\lambda_{\mathcal A}=\lambda_H$。
$J(-Q,Q)=(-Q,Q)$，故 $J$ 下降到 $\mathcal A$，Rosati 将 $J$ 送到 $J^{-1}$。
它在 Lie 空间的两个特征是 $\zeta,\zeta^2$，即 signature $(1,1)$。

在原 CM 点选 $\mathcal C=E_0[s]$。直接从 (UH2) 得
$$
\ker C=\{(-Q,Q):Q\in E_0[s]\}.
$$
所以 (UH4) 在该点由 $C$ 准确识别为原的主极化积 $E_0\times E_0$。
这一步同时固定微分：
$$
\begin{pmatrix}z\\t\end{pmatrix}
=C\begin{pmatrix}w_1\\w_2\end{pmatrix}.
\tag{UH5}
$$
右侧是在 $E^2$ 上由原 $dw_i$ 产生的坐标；在 CM 点，左侧正是两份
$dx/(2y)$ 的平坦变量，没有另选尺度。

在素于 $p$ 的有限 level 覆盖上固定对称主 theta 线丛、
其六次幂的 theta structure 和原点 rigidification。
使它们在这个 CM 点等于原的 product 标架；这是携带 level 数据的延拓，
不是事后以 CM 数值挑选标架。由于 $q$ 的核阶为三，
$A[6]$ 的标记可在 $E[18]$ 的有限标记覆盖上选择。
这些同源和 level 步骤的坏素数仅涉及二、三。

于是 $q^*\mathcal L_{\mathcal A}^{\,6}$ 是极化矩阵 $6H$ 的线丛，
其截面空间维数为 $108$；保持所选 $\mathcal K$ 线性化的子空间维数为 $36$。
在 CM 点，它正是
$$
C^*H^0(E_0^2,\mathcal O(6O)\boxtimes\mathcal O(6O)).
\tag{UH6}
$$
原 $36$ 个 product 截面都在其中，包括整段 $F(z)G(t)$。

entire-function 规范也可从乘子直接核对。
原 CM quasiperiod 满足 $\eta_\lambda=\bar\lambda/\mathcal A_0$。
将两个原 sigma 乘子沿 $C$ 拉回，得到的 Hermitian 矩阵是
$\bar C^tC=H$。六次幂消去 sigma 的符号特征。
这证明 (UH6) 的函数规范；没有插入一个自由的二次 Gaussian。

## 2. 原辅助曲线上的明确 heat 方程

使用 MH、FT、R812 的同一一般家族与辅助曲线：
$$
y^2=x^3-\frac a4x-\frac b4,\quad
L=6b\partial_a+\frac{a^2}{3}\partial_b,\quad
a=3X,\quad b=Y,
$$
$$
Y^2=X^3+16,\quad D=L,\quad DX=2Y,\quad DY=3X^2,\quad P_0=(0,4).
\tag{UH7}
$$
不同于固定椭圆曲线的 $D_z$，$D$ 作用于模参数。

为固定全部标量，直接使用 R812(812.14)–(812.16) 的 $q$ 规范：
$$
\lambda=d_0\eta^{-2},\quad d_0^{12}=-432,\quad
a=\lambda^4E_4/12,\quad b=-\lambda^6E_6/216,
$$
$$
D=\lambda^2\theta_q,\qquad D\lambda=-\lambda^3E_2/12.
\tag{UH8}
$$
对 $\rho\in\mathbb Z^2/(6H)\mathbb Z^2$，置
$$
\Psi_\rho(w)=
\eta^{-2}\exp\left(-\frac{E_2\lambda^2}{4}w^tHw\right)
\sum_{n\in\mathbb Z^2+(6H)^{-1}\rho}
q^{\,3n^tHn}\exp(6\lambda n^tHw).
\tag{UH9}
$$
这是完整的 $108$ 维 theta 向量，已包含 Gaussian。
由 $\theta_qE_2=(E_2^2-E_4)/12$、$\theta_q\log\eta=E_2/24$，
逐项求导得到
$$
D\Psi_\rho=
\left(\frac1{12}\partial_w^tH^{-1}\partial_w
+\frac{3X}{4}w^tHw\right)\Psi_\rho.
\tag{UH10}
$$
对一个频率项，常数、线性和二次项分别是
$3\lambda^2n^tHn-\lambda^2E_2/12$、$-\lambda^3E_2 n^tHw/2$、
$\lambda^4(E_2^2+E_4)w^tHw/48$；
它们与右侧完全相同。

选定 level/theta structure 后，$\mathcal K$ 的 theta-group 作用为常数矩阵，
所以 (UH10) 保持 (UH6) 的全部 $36$ 维子空间。
在代数值向量基 $\Phi$ 中写成
$$
(D-M)\Phi=
\left(\frac1{12}\partial_w^tH^{-1}\partial_w
+\frac{3X}{4}w^tHw\right)\Phi.
\tag{UH11}
$$
矩阵 $M$ 只作用于 $36$ 个有限截面，不作用于 $w$。
这里没有将旧八通道误当作交叉 heat 下稳定的子空间。

另一方面，$\bar C=\mathsf S C$，其中
$\mathsf S=\begin{pmatrix}0&1\\1&0\end{pmatrix}$。故
$$
C H^{-1}C^t=\mathsf S,\qquad
(C^{-1})^tHC^{-1}=\mathsf S.
$$
将 (UH11) 按 (UH5) 运输，得到
$$
\boxed{
\nabla\Phi=0,\qquad
\nabla=D-M-\frac16\partial_z\partial_t-\frac{3X}{2}zt .
}
\tag{UH12}
$$
这是新的 unitary family 的连接。在原点，$\Phi$ 可取为原 $36$ 个 product 截面。
旧 product family 的极化是 $6I$；这里在商前是 $6H$、商的次数为三。
因此 (UH12) 不是把旧 R808 的固定 $6I$ 连接改写坐标后
仍声称原 $FG$ 不变。

这里可以明确有限覆盖与整模型，不只援引“有限单值”。
格 $6H$ 的 discriminant group 有 $108$ 个元素，quadratic form 为
$$
q(\rho)=\frac{\rho_1^2+\rho_1\rho_2+\rho_2^2}{18}.
$$
其 level 是 $18$。Poisson 变换的 $S$ 矩阵是 $1/\sqrt{108}$ 乘有限
Fourier 矩阵和一个四次单位根，$T$ 矩阵的条目是十八次单位根。
Scheithauer, *The Weil representation of* $SL_2(\mathbb Z)$, Proposition 4.3
给 $\Gamma(18)$ 上表示平凡；同文 Proposition 6.1 平方给
$\eta^2$ 的乘子在 $\Gamma(12)$ 上平凡。
所以取 full level $72$ 已足以同时固定这些乘子和上述实际三、六层数据；
不需要最小 level。

在这个覆盖上，第 $n$ 阶 theta 导数的 weight $n+1$、
$\lambda^n$ 的 weight $-n$ 和 $\eta^{-2}$ 的 weight $-1$
按 (UH9) 的 Gaussian 变换准确相抵，所有 Hurwitz 系数是代数函数。
有限 theta-group 的标准基在 $p>3$ 仍是基：
其 Fourier 矩阵及逆矩阵只除二、三，线性化取不变部分只除三，
而 $\eta^2$ 在固定非零判别式的内部是单位。
这也可由 Moonen Theorem 8.28 的素于 $p$ theta-group 表示逐纤维核对。
因此这里使用的是在 $\mathbb Z[1/6]$ 上的实际有限 level 模型，
不是从特征零单值群猜一个未经检查的好约化集合。
局部选择代数截面基 $\Phi$，使它在 $P_0$ 为原 $36$ 个 product，
令 $\Psi^{\mathcal K}$ 为上述线性化不变部分所选的 $36$ 个 theta 基截面；
可用方阵基变换 $\Phi=U\Psi^{\mathcal K}$ 完成，$U$ 是 $36\times36$ 矩阵，在该点可逆且正则，
有限连接满足 $M=(DU)U^{-1}$。
从而 $D-M$ 在实际有限可分 level 覆盖上平凡化。
这只保持整个有限向量，不把某个 theta 常数或 Taylor 系数宣布为单位。

## 3. 精确的双向 Frobenius 关系

以下 $p=6N+5\ge41$，仍取原 Hasse 多项式 $A$ 及
$$
A(P_0)=0,\qquad B=DA(P_0)
=(-1)^{N+1}\binom{3N+2}{2N+1}\in\mathbb F_p^\times.
\tag{UH13}
$$
记 $B_0=DA$ 为辅助曲线上的函数，不把它在整个家族都当成常数 $B$。

Taylor 运算先在 Hurwitz 环中进行：
$\gamma_n(z)$ 的系数是普通导数，不除以不可逆的 $n!$。
(UH9) 的频率向量 $6Hn$ 为整向量。
在第 $p$ 个 Hurwitz 导数中，混合 binomial 系数消失；
二次 Gaussian 的 $p$ 次导数为零，因为 Hurwitz 环中 $z^p=t^p=0$。
再用 R812 的同权 $q$-expansion 恒等式
$$
A=\lambda^{p-1},\qquad B_0=A\lambda^2E_2/12,
$$
得到
$$
\partial_{w_i}^{\,p}\Phi
=A\partial_{w_i}\Phi+6B_0(Hw)_i\Phi.
\tag{UH14}
$$
这是整 Hurwitz 系数的同余，由同权的 $q$-expansion 原理下降到实际
theta 模型；没有在 supersingular 点代入 $\lambda^{-1}$。
tame level 素于 $p$，$q$ 系数的分母只涉及二、三。
等式对全部 Hurwitz 系数成立，因而可以先做线性代入再截断。

关键的 Frobenius 常数不能省略：由于 $p\equiv2\bmod3$，
$$
C^{(p)}=\bar C=\mathsf SC.
$$
将 (UH14) 运输到原特征坐标，准确得到
$$
\boxed{
\partial_z^{\,p}\Phi=A\partial_t\Phi+6B_0z\Phi,\qquad
\partial_t^{\,p}\Phi=A\partial_z\Phi+6B_0t\Phi .
}
\tag{UH15}
$$
在 $P_0$ 这回到原每个 degree-six 截面的
$\partial^p=6Bz$ Hurwitz 关系；在家族中则有不能删除的交叉 $A$ 项。

## 4. 首 p 矩形的全部边界

记向量普通导数
$$
a_{nm}=(\partial_z^n\partial_t^m\Phi)(0,0),
\qquad
P=\sum_{0\le n,m<p}a_{nm}\gamma_n(z)\gamma_m(t).
\tag{UH16}
$$
$n!,m!$ 都是单位，所以 $P$ 也可视为
$k(\widetilde E)[z,t]/(z^p,t^p)$ 中的普通多项式向量。
$\widetilde E$ 表示实际带 level 的辅助覆盖。

由 (UH15)，所需边界恰为
$$
a_{p,m}=A a_{0,m+1},\qquad a_{n,p}=A a_{n+1,0},
$$
$$
a_{0,p}=A a_{10},\qquad a_{p,0}=A a_{01},\qquad
a_{pp}=A^2a_{11}+6AB_0a_{00}.
\tag{UH17}
$$
最后一个角点必须单独计一次。

把 (UH12) 截断，并逐一保留 $\partial_z\partial_t$ 从矩形外带回的项：
$$
\boxed{
\begin{aligned}
\nabla P={\cal R}:={}&
\frac A6\gamma_{p-1}(z)
 \sum_{m=0}^{p-2}a_{0,m+2}\gamma_m(t)\\
&+\frac A6\gamma_{p-1}(t)
 \sum_{n=0}^{p-2}a_{n+2,0}\gamma_n(z)\\
&+\frac{A^2a_{11}+6AB_0a_{00}}6
 \gamma_{p-1}(z)\gamma_{p-1}(t).
\end{aligned}}
\tag{UH18}
$$
两条边的末项分别使用 $a_{0,p}=Aa_{10}$、$a_{p,0}=Aa_{01}$。
若把和式直接写成截断轴函数的二阶导数，这两个末项会漏掉。
普通幂基中 $\gamma_{p-1}=-z^{p-1}$，双角点则为正号；
(UH18) 使用 Hurwitz 基，已固定这些符号。

(UH18) 在 $P_0$ 为零，但横向导数一般不为零。
若 $E_z(t)=P(0,t)$、$E_t(z)=P(z,0)$，则
$$
(\nabla{\cal R})(P_0)=
\frac B6\{\gamma_{p-1}(z)E_z''(t)
+\gamma_{p-1}(t)E_t''(z)\}
+B^2a_{00}\gamma_{p-1}(z)\gamma_{p-1}(t).
\tag{UH19}
$$
因为 $\mathcal R(P_0)=0$，此处 $\nabla{\cal R}$ 与 $D{\cal R}$ 相同。
对原指定的 $FG$ 分量，两轴及 $a_{00}$ 在 $P_0$ 均为零，
所以 (UH19) 的该分量也为零。
这排除了“全 $36$ 向量有单位源，因此 $FG$ 的首源必为单位”的推法。

## 5. 曲率与五次 lift

定义
$$
L_z=A\partial_t+6B_0z,\qquad
L_t=A\partial_z+6B_0t.
\tag{UH20}
$$
利用 $D^2A=-XA/4$ 直接计算，得
$$
[\nabla,L_z]=[\nabla,L_t]=0,\qquad [L_z,L_t]=0.
\tag{UH21}
$$
例如第一个交换子中 $A'\partial_t$ 与
$[-\partial_z\partial_t/6,6A'z]$ 抵消，
剩余 $(6A''+3XA/2)z=0$。有限矩阵 $M$ 与这些变量算子交换。

在首 $p$ 矩形上，MH/FT 的 restricted oscillator 公式经 (UH2) 的
常数线性换元给
$$
\boxed{
\nabla^p=\frac16L_zL_t,\qquad
\nabla^p\big|_{P_0}=6B^2zt .
}
\tag{UH22}
$$
这里 $D^p=0$ 在辅助 E27 上已由原三次 CM 作用证明，
并延伸到实际有限可分 level 覆盖；有限连接 $D-M$ 的曲率为零。
公式只断言截断模块上的算子，不断言整个原 theta 级数无源水平。

取
$$
P^{(5)}=L_z^2L_t^3P.
$$
由 (UH18)、(UH21)，真实方程为
$$
\nabla P^{(5)}=L_z^2L_t^3{\cal R}.
\tag{UH23}
$$
两边、角点及 $A$ 的横向导数全部保留。
在原 $P_0$，$L_z=6Bz$、$L_t=6Bt$，所以原指定 $FG$ 分量满足
$$
[P^{(5)}_{FG}]_{\deg=p-1}
=(6B)^5\sum_{i=0}^{N-1}
 f_i g_{N-1-i}\,z^{6i+6}t^{p-7-6i}.
\tag{UH24}
$$
这回是原单项本身，未作 R808 中的 Krawtchouk 换基。

## 6. 实际本原掩码的相容延伸

令 $\ell\ge5$ 为 $p+1$ 的任一素因子，$q\in\mu_\ell$。
定义
$$
(T_qU)(z,t)=U(qz,q^{-1}t),\qquad
\Pi_\ell=\frac1\ell\sum_{q\in\mu_\ell}T_q.
\tag{UH25}
$$
交叉 heat、有限矩阵 $M$ 与 $T_q$ 交换。
此外 $q^p=q^{-1}$；逐项代入 (UH15) 可核
$T_q$ 保持这两条实际 Frobenius 关系。
因此 (UH18) 的两边及角点也按同一规则运输。
这是完整形式解／jet 空间的水平作用。它本身不证明实际 $36$ 维截面子空间稳定；
更不是只由 $\operatorname{diag}(\zeta,\zeta^2)$ 的有限 CM 对称性猜出大环面。

它也有真实 CM pullback 来源。用中国剩余定理取
$\alpha\in\mathbb Z[\zeta]$，使
$\alpha\equiv1\bmod6$、$\alpha\bmod p=q$。
则 $\bar\alpha\bmod p=q^{-1}$、$\operatorname N\alpha\equiv1\bmod p$。
家族 $\mathcal A$ 的实际 $\mathbb Z[\zeta]$ 作用在两个特征变量上为
$(z,t)\mapsto(\alpha z,\bar\alpha t)$。
它固定所选六层标记。拉回改变全局 theta 的 index 为
$6\operatorname N\alpha$；此 index 模 $p$ 等于六，
所以其合法首 $p$ jet 服从同一 heat 与 (UH15)。
原点 rigidification 固定 pullback 的常数。
我们在这个 jet 模块内相加，不把不同 degree 的拉回强称为同一
全局 $36$ 维截面空间的自作用。

在 (UH24) 的原中心单项上，置 $h=6i+7$，有
$$
T_q(z^{h-1}t^{p-h})
=q^{\,2h-(p+1)}z^{h-1}t^{p-h}
=q^{2h}z^{h-1}t^{p-h}.
$$
因为 $\ell$ 为奇数，$\Pi_\ell$ 恰选择 $\ell\mid h$。
而 $h\equiv1\bmod6$ 已排掉二、三。故
$$
\boxed{
\Pi_{\rm prim}:=\prod_{\substack{\ell\mid p+1\\\ell\ge5}}
 (1-\Pi_\ell)
}
\tag{UH26}
$$
在原 critical 中心子空间上**准确**等于
$\mathbf1_{\gcd(h,p+1)=1}$，并与 (UH23) 的连接交换。
这是 R770 的同一个本原集合；不拼两个不同标签上的单位。

本结论不要求先补出整个 projective nonsplit Cartan 的
determinant-nonsquare 分支。该分支的 metaplectic 相位与完整 Weil 标记
仍须另核；这里逐个奇素因子的实际子群已经足以给出原本原掩码。

## 7. 原 Legendre 权的有限逐链水平延伸

这一节不需要先证明完整 projective Cartan 的几何标记。
在首 $p$ 多项式模块内，$\partial_z\partial_t$ 与 $zt$ 都保持
**整数差** $d=n-m$，不只是模 $p+1$ 的差。
令 $V_d$ 由所有 $0\le n,m<p$、$n-m=d$ 的单项生成。
有限矩阵 $M$ 只作用截面指标，故 $\nabla$ 保持每个 $V_d$。

对偶数 $d$ 置 $h_d=(d+p+1)/2$。
若 $7\le h_d\le p-4$、$h_d\equiv1\bmod6$，定义
$$
w_d=\mathbf1_{\gcd(h_d,p+1)=1}P_{h_d-1}(1/s);
$$
对其余整数差置 $w_d=0$。
这些权属于 $\mathbb F_p$，因为出现的 Legendre 次数均为偶数。
定义 $\mathcal W|_{V_d}=w_d I$，则
$$
[\nabla,\mathcal W]=0,\qquad
[L_zL_t,\mathcal W]=0.
\tag{UH27}
$$
第二式也可直接看出：$L_z$ 将整数差加一，$L_t$ 将它减一。
不声称 $\mathcal W$ 与单独的 $L_z$、$L_t$ 交换。

置 $\mathcal S^{(5)}=L_z^2L_t^3\mathcal R$。
对完整 $36$ 通道使用 (UH22)–(UH23)、(UH27)，得到
$$
\nabla^{p-1}\bigl(\mathcal W\mathcal S^{(5)}\bigr)
=\frac16 L_zL_t\,\mathcal W P^{(5)}.
\tag{UH28}
$$
所有辅助 $D$ 导数先做完，最后才在 $P_0$ 取值。
取其原 $FG$ 分量及总次数 $p+1$，右侧由 (UH24) 准确给
$$
\boxed{
\begin{aligned}
&\left[
\left.\nabla^{p-1}
  \bigl(\mathcal W L_z^2L_t^3\mathcal R\bigr)
\right|_{P_0,FG}
\right]_{\deg=p+1}\\
&\quad =
6^6B^7
\sum_{\substack{0\le i<N\\(6i+7,p+1)=1}}
 P_{6i+6}(1/s) f_i g_{N-1-i}\,
 z^{6i+7}t^{p-6i-6}.
\end{aligned}}
\tag{UH29}
$$
$6^6B^7$ 是原已知单位。各个原目标单项不同；
$h=6i+7$ 位于 $7,\ldots,p-4$，所以乘 $zt$ 后两指数仍小于 $p$，
没有截断零或边界混合。因此 (UH29) 左侧非零，与存在同一个原真本原
$h$ 满足三个单位条件**等价**。这里保留的是向量多项式的非零，
没有把可能相消的总和当成等价条件。

$\mathcal W$ 只是这个有限截断连接的水平算子。
其权一般不按 $p+1$ 周期延伸，故它未被证明保持完整 Hurwitz 的
(UH15)，也未被证明来自原 $36$ 维全局 theta 空间的自同态。
这些额外解释不是有限等式 (UH28)–(UH29) 的前提。
它也没有删除任何 Hasse 边或角点：
左侧仍使用 (UH18) 的完整 $\mathcal R$ 和全部 $36$ 通道，
并在所有导数之后才取指定 $FG$ 分量。

这把非零问题准确收紧为 (UH29) 左侧的指定齐次源分量。
式子本身没有证明这个分量非零。

## 8. 尚未得到的指定源非零

(UH24)–(UH26) 只解决原本原筛在这个不同家族中的准确延伸。
R770 还要求同一 $h$ 的
$$
P_{h-1}(1/s)\,f_i g_{N-1-i}\ne0.
$$
原 R808 的 Gram 商、split 向量和原 toric 平均已经给出这个 Legendre
因子的表示含义；但不能只因这里也出现一个字符中心，
就认定实际 $36$ 维 theta 源与原有限 period 向量的标记和配对已相同。
若要作这种几何 test-vector 解释，完整比较仍缺。
有限逐链方法则已由 (UH29) 精确保留原 Legendre 权而不依赖该解释；
仍须独立证明其指定齐次源分量非零。

同样，(UH22) 的非零曲率不使任意原 section 的每个字符分量非零。
R739 的 $p=41,h=37$ 筛内反例仍有效。
在原 $FG$ 分量上，(UH19) 的首横向源本来就是零；
后继必须分析 (UH23) 的真实投影源，不能用整个 $36$ 维空间的非退化代替它。

本笔记没有证明未筛或筛后 critical 非零，没有重新计算任何有限素数窗口。
没有将完整非整普通 sigma 模 $p$ 化，也没有从高 Hurwitz 块重新提取已登记的同核条件。

### 8.1. 惰性族的中央链及其 Legendre 尺度

若 $p=12k+11$，则 $N=2k+1$。原 $P^{(5)}_{FG}(P_0)$ 的最低项
$(6B)^5z^6t^4$ 位于整数差 $d=2$ 的链。在 critical 总次数 $p-1$ 上，
该链唯一对应
$$
h=(p+3)/2=6k+7,\qquad i=j=k.
$$
因为 $h=(p+1)/2+1$ 且 $h$ 为奇数，
$\gcd(h,p+1)=\gcd(h,2)=1$。所以这个标签自动通过原本原筛；
它仍需要三个独立的实际单位
$$
f_k,\qquad g_k,\qquad P_{(p+1)/2}(1/s).
$$
最低项的单位与整条链保持性本身不证明这个高项的单位。

准确的 Legendre 约化是
$$
P_{(p+1)/2}(x)=P_{(p-3)/2}(x)\quad\text{in }\mathbb F_p[x].
\tag{UH30}
$$
它由 $P_n={}_2F_1(-n,n+1;1;(1-x)/2)$ 的有限多项式公式得到：
$n$ 与 $p-1-n$ 的两个参数模 $p$ 互换，较低次数后的系数为零。
令 $r=(p-1)/2$，Legendre 导数公式进一步给
$$
P_{r-1}(x)=xP_r(x)-2(1-x^2)P_r'(x)\quad\bmod p.
\tag{UH31}
$$
在原 $x=1/s$，有 $x^2=-1/3$。若用
$\lambda=(1-x)/2$ 把 $P_r$ 写成 Legendre 曲线的 Hasse 多项式，则
$$
\lambda(1-\lambda)=1/3,\qquad
j(\lambda)=
256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}
=\frac{2048}{3}.
\tag{UH32}
$$
这不是原 $j=0$ 曲线。原 $B=DA(P_0)$ 的单位性不能直接用于
(UH31) 的这个 Hasse 值或导数。

在该辅助曲线实际 supersingular 的素数处，
$P_r(x)=0$ 是单根，因而 (UH31) 确给中央 Legendre 因子非零。
这里的简单性也可直接由 Legendre 方程证明：$x^2\ne1$，
次数 $r<p$，一个共同零 $P_r=P_r'=0$ 将逐阶迫出全部 Taylor 系数为零。
但原允许条件并未证明这条 $j=2048/3$ 曲线总是 supersingular，
所以这不是全部惰性素数的中央单位定理。

现有精确输出须按其真实索引使用：
[R829](../results/R829-reused-prime47-original-critical-products.md)
在 $p=47$ 给中央 $f_3g_3=21\ne0$，只是一项已认证的原乘积；
该消费者没有计算中央 Legendre 因子。
[R706](../results/R706-exact-window-through-200000-and-original-sigma-zero.md)
在 $p=137147$ 给出的零为 $g_N=0$、$N=22857$，
不是这里 $k=11428$ 的中央系数。
这些已成记录既不证明、也不否定一般中央三单位命题。
本节没有执行新的素数计算。

## 原规范依赖

- 原 [R697](../results/R697-original-sigma-six-sections-and-integral-square-roots.md)：sigma-six、theta 标架、普通导数和原 CM 乘子。
- 原 [MH 笔记](2026-11-15-sigma-modular-heat-connection-and-odd-tame-trivialization.md)：一般家族、原 $D$、$A$、$B$、矩阵方向。
- 原 [FT 笔记](2026-11-15-sigma-full-heat-tame-trivialization-and-even-source.md)：有限连接与 restricted oscillator 曲率。
- 原 [R812](../results/R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)，§3：逐项使用的 $\lambda$、$\eta$、Gaussian、$A$ 和 $DA$。
- 原 [R770](../results/R770-same-primitive-label-square-and-finite-bilinear-pairing.md)：同一 critical 单项及实际本原掩码。
- 原 [R808](../results/R808-original-cuspidal-Gram-quotient-and-Howe-chain.md)、R810：原有限 period/Legendre 标记以及不能省略的 test-vector 范围。

- Moonen, *The Theta group of a line bundle*, Theorem 8.10、Corollary 8.11、
  Proposition 8.15、Theorem 8.28：
  https://www.math.ru.nl/personal/bmoonen/BookAV/ThetaGr.pdf
- Scheithauer, *The Weil representation of* $SL_2(\mathbb Z)$ *and some applications*,
  Proposition 4.3（PDF 第 14 页）、Proposition 6.1（第 29–30 页）：
  https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/scheithauer/publications/Weil_representation.pdf
