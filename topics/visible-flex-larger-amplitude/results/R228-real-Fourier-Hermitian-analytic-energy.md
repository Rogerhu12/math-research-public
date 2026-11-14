# R228：真实 Fourier 矩阵的 Hermitian 配对与更紧解析能量界

作者：exact_closure（GPT-6 Astra Pro，AI-assisted），2026-11-14。

**已证明（条件性能量估计）。** 对真实矩阵函数的解析 Fourier 系统，先将加权演化矩阵与其真正伴随配对，再取正界，可以保留对称主系数的运输抵消以及常数零阶矩阵的负阻尼。下面的主阶、交换和零阶上界分别不大于 R69 对应的原上界。该比较是数学公式间的比较；未声称已经降低 R203 的实际数值预算到可用范围。

本结果保留完整 mean、实际剪切与 frame 导数、全部接口、真实两源分量及解析范数转换。它不将点态相似变换当作传播证明，也不新增一个未经证明的无限维解。

## 1. 系统和复 Fourier 系数的正确约定

考虑在一个实径向坐标片上的系统

$$
W_x=A(x,\theta)W_\theta+C(x,\theta)W
       +\mathcal R_xW+F(x,\theta),
\tag{228.1}
$$

其中 $A,C$ 在真实角度上取实矩阵值。未知变化量 $W$ 和源 $F$ 可以是复数值。实矩阵函数的 Fourier 系数通常是复矩阵，满足

$$
A_{-j}=\overline{A_j},\qquad C_{-j}=\overline{C_j}.
\tag{228.2}
$$

定义的是**转置**对称和反对称部分

$$
S_j=\frac{A_j+A_j^T}{2},\qquad
K_j=\frac{A_j-A_j^T}{2},
$$
$$
H_j=\frac{C_j+C_j^T}{2},\qquad
J_j=\frac{C_j-C_j^T}{2}.
\tag{228.3}
$$

对于 $j\ne0$，这些矩阵一般不是 Hermitian/anti-Hermitian 分解，不能把 $T$ 换成 $*$。只有零 Fourier 系数为实矩阵，此时 $H_0$ 是实对称矩阵，可取真实 $\lambda_{\max}(H_0)$。

所有矩阵范数均为复 Euclidean 空间的算子范数。$\mathcal R_x$ 表示另外保留的非局部线性项；只有当已经支付

$$
\operatorname{Re}\langle Z,
 e^{\tau|D_\theta|}\mathcal R_x e^{-\tau|D_\theta|}Z\rangle
\le\omega_{\mathcal R}(x)\|Z\|_2^2
\tag{228.4}
$$

时，才能把它作为下面的零阶能量项。一个合法的非负算子范数上界是充分的，但不能未证明就将完整 mean 的导数当成零阶有界算子或将其删除。没有该项时取 $\omega_{\mathcal R}=0$。

取绝对连续角宽 $\tau(x)\ge0$，令

$$
Z_m=e^{\tau|m|}W_m,\qquad
\mathcal E=\sum_m\|Z_m\|_2^2,
\qquad
\mathcal Q=\sum_m|m|\|Z_m\|_2^2.
\tag{228.5}
$$

先对所有相关 Fourier 和绝对收敛、径向求导合法的解证明，或对 (228.1) **变换后方程本身**的有限 Fourier Galerkin 系统证明。一般原方程先投影、再乘非恒定角剪切，不等于变换后方程投影；若使用前一种近似，必须另保相应投影交换残差。

## 2. 主阶块的精确 Hermitian 恒等式

固定输出模 $m$、输入模 $n$，记

$$
j=m-n,\qquad d=|m|-|n|.
$$

主阶加权矩阵块为

$$
B_{mn}=i n e^{\tau d}A_j.
$$

由 (228.2)，真正伴随块满足

$$
B_{nm}^*=-i m e^{-\tau d}A_{-j}^*
=-i m e^{-\tau d}A_j^T.
$$

因此能量中的 Hermitian 块准确等于

$$
\begin{aligned}
\frac{B_{mn}+B_{nm}^*}{2}
=\frac i2\{&[-j\cosh(\tau d)+(m+n)\sinh(\tau d)]S_j\\
&+[(m+n)\cosh(\tau d)-j\sinh(\tau d)]K_j\}.
\end{aligned}
\tag{228.6}
$$

**证明。** 先写成

$$
\frac i2[n e^{\tau d}A_j-m e^{-\tau d}A_j^T].
$$

代入 $A_j=S_j+K_j$、$A_j^T=S_j-K_j$，再用
$e^t\pm e^{-t}=2\cosh t,2\sinh t$ 和 $n-m=-j$，即得 (228.6)。证毕。

(228.6) 对复 Fourier 系数成立，所用实性仅是整矩阵函数的 (228.2)。不能对一般复参数中心无条件使用 (228.2)。

有两个基本整数不等式：

$$
|d|\le|j|,
\qquad
|m+n|\le2\sqrt{|mn|}+|j|.
\tag{228.7}
$$

第二式在异号时由 $|m+n|\le|m-n|$ 得到；同号时，
$(\sqrt{|m|}-\sqrt{|n|})^2\le||m|-|n||=|j|$，得到同一结论。

## 3. 新的主阶与交换预算

定义

$$
\gamma_H(\tau)=\|K_0\|
+\sum_{j\ne0}\left[
 \sinh(\tau|j|)\|S_j\|
 +\cosh(\tau|j|)\|K_j\|\right],
\tag{228.8}
$$

$$
\chi_H(\tau)=\frac12\sum_{j\ne0}|j|e^{\tau|j|}
 (\|S_j\|+\|K_j\|).
\tag{228.9}
$$

则主阶能量满足

$$
\operatorname{Re}\langle Z,
 e^{\tau|D_\theta|}A\partial_\theta e^{-\tau|D_\theta|}Z\rangle
\le\gamma_H\mathcal Q+\chi_H\mathcal E.
\tag{228.10}
$$

**证明。** $j=0$ 时 (228.6) 为 $imK_0$，给出
$|m|\|K_0\|\|Z_m\|^2$。

对 $j\ne0$，(228.6)–(228.7)、$|\sinh(\tau d)|\le\sinh(\tau|j|)$ 与 $\cosh(\tau d)\le\cosh(\tau|j|)$ 给出块范数上界

$$
\begin{aligned}
&\sqrt{|mn|}\left[
 \sinh(\tau|j|)\|S_j\|
 +\cosh(\tau|j|)\|K_j\|\right]\\
&\qquad+\frac{|j|}{2}e^{\tau|j|}
 (\|S_j\|+\|K_j\|).
\end{aligned}
\tag{228.11}
$$

对每个固定 $j$ 使用

$$
\sum_m\sqrt{|m||m-j|}\|Z_m\|\|Z_{m-j}\|\le\mathcal Q,
$$
$$
\sum_m\|Z_m\|\|Z_{m-j}\|\le\mathcal E,
$$

然后对 $j$ 求和，即得 (228.10)。此处已经支付真正的 Fourier 解析权交换；没有把变系数矩阵当作逐点常数。证毕。

## 4. 零阶块保留 signed 常数阻尼

定义

$$
\zeta_H(\tau)=\lambda_{\max}(H_0)
+\sum_{j\ne0}\left[
 \cosh(\tau|j|)\|H_j\|
 +\sinh(\tau|j|)\|J_j\|\right].
\tag{228.12}
$$

这里 $\lambda_{\max}(H_0)$ 可以为负，不取绝对值、不预先截为零。零阶能量满足

$$
\operatorname{Re}\langle Z,
 e^{\tau|D_\theta|}Ce^{-\tau|D_\theta|}Z\rangle
\le\zeta_H\mathcal E.
\tag{228.13}
$$

**证明。** 零阶加权块为 $D_{mn}=e^{\tau d}C_j$。由实系数关系，其 Hermitian 部分为

$$
\frac{D_{mn}+D_{nm}^*}{2}
=\cosh(\tau d)H_j+\sinh(\tau d)J_j.
\tag{228.14}
$$

$j=0$ 时这是实对称 $H_0$，故应使用其最大特征值，而不是整个 $C_0$ 的算子范数。$j\ne0$ 时用 $|d|\le|j|$ 和固定平移的 $\ell^2$ Cauchy 不等式，即得 (228.13)。证毕。

## 5. 完整条件性能量定理

**定理 228.1。** 假设上述各 Fourier 预算、$\omega_{\mathcal R}$ 及源范数在所考察片上可积，并且

$$
\tau'(x)+\gamma_H(x,\tau(x))\le0
\quad\text{a.e.}
\tag{228.15}
$$

令

$$
\Lambda_H=\chi_H+\zeta_H+\omega_{\mathcal R}.
\tag{228.16}
$$

则满足 (228.1) 的上述解有

$$
\begin{aligned}
\|W(x)\|_{\ell^2_{\tau(x)}}
\le{}&e^{\int_a^x\Lambda_H}\|W(a)\|_{\ell^2_{\tau(a)}}\\
&+\int_a^x e^{\int_y^x\Lambda_H}
 \|F(y)\|_{\ell^2_{\tau(y)}}\,dy.
\end{aligned}
\tag{228.17}
$$

**证明。** 角宽求导、(228.10)、(228.13)、(228.4) 和源的 Cauchy 不等式给

$$
\tfrac12\mathcal E'
\le(\tau'+\gamma_H)\mathcal Q
 +(\chi_H+\zeta_H+\omega_{\mathcal R})\mathcal E
 +\sqrt{\mathcal E}\|F\|_{\ell^2_\tau}.
\tag{228.18}
$$

利用 (228.15) 去掉非正的 $\mathcal Q$ 项。对正能量可直接除以 $\sqrt{\mathcal E}$。若能量为零，使用 $\sqrt{\mathcal E+\varepsilon}$ 正则化；因 $\Lambda_H$ 可以为负，正则化不等式另有至多 $|\Lambda_H|\sqrt\varepsilon$ 的可积项。Gronwall 积分后令 $\varepsilon\downarrow0$，该项消失，得到保留 signed $\Lambda_H$ 的 (228.17)。证毕。

对变换后方程的有限 Fourier Galerkin 系统，投影在能量内积中由 $Z$ 已在该空间而消去，同样的证明逐项成立。它没有删除原方程先投影时的剪切交换项。

若片间准确变换为 $W^+=\mathcal J W^-$，必须乘已经支付的
$\|\mathcal J\|_{\ell^2_\tau\to\ell^2_\tau}$。一般源到输出的上界是

$$
\exp\!\left(\int_y^x\Lambda_H\right)
 \prod_{\text{interfaces between }y,x}\|\mathcal J\|.
\tag{228.19}
$$

不能给在当前片末端才产生的源免费乘整个当前片的负积分。需要整片上确界时，应对实际起点、终点或严格的 partial 上界取最大，保持真实径向顺序。

## 6. 与 R69 原预算逐项比较

原 R69 定义

$$
\gamma_{\rm old}=\tfrac12\|A_0-A_0^T\|
 +\sum_{j\ne0}e^{\tau|j|}\|A_j\|,
$$
$$
\chi_{\rm old}=\sum_{j\ne0}|j|e^{\tau|j|}\|A_j\|,
\qquad
C_{\rm old}=\sum_j e^{\tau|j|}\|C_j\|.
\tag{228.20}
$$

对任何复矩阵 $M$，$\|M^T\|=\|M\|$，所以

$$
\left\|\frac{M+M^T}{2}\right\|\le\|M\|,
\qquad
\left\|\frac{M-M^T}{2}\right\|\le\|M\|.
\tag{228.21}
$$

必须分别使用这两条不等式；一般并没有两部分范数之和不超过 $\|M\|$ 的不等式。

由 $\sinh t+\cosh t=e^t$ 以及 $\lambda_{\max}(H_0)\le\|C_0\|$，得到

$$
\boxed{\quad
\gamma_H\le\gamma_{\rm old},\qquad
\chi_H\le\chi_{\rm old},\qquad
\zeta_H\le C_{\rm old}.
\quad}
\tag{228.22}
$$

对于交换项，具体使用
$\tfrac12(\|S_j\|+\|K_j\|)\le\|A_j\|$；对于主阶和零阶项，则分别乘对应的非负 $\sinh$、$\cosh$ 权后相加。

这些是实际矩阵 Fourier 系数定义出的精确量之间的比较。若计算时再用不同的标量三角界放大它们，不能因此宣称任意新实现的粗上界都小于旧实现的粗上界。两个已完整支付的最终预算可以合法取较小者，但不能用一个尚未支付的新系数上界替换旧数据标签。

## 7. 本题真实剪切主符号的直接简化

对 R69 的完整真实剪切与正 frame，写

$$
\widehat A=\alpha I+
\begin{pmatrix}0&sb\\-\ell d/b&0\end{pmatrix},
\quad
q=EU/L,\quad\alpha=sq,\quad d=D/L^2,
\tag{228.23}
$$

其中 $b=b(x)>0$ 与角度无关。对每个 $j\ne0$，

$$
\widehat A_j=\alpha_jI+v_jE_{21},
\qquad v_j=-\ell d_j/b.
$$

故

$$
\|S_j\|\le|\alpha_j|+|v_j|/2,
\qquad \|K_j\|=|v_j|/2.
$$

代入 (228.8)–(228.9) 给出直接可计算的充分界

$$
\gamma_H-\gamma_0
\le\sum_{j\ne0}\sinh(\tau|j|)|\alpha_j|
 +\frac{|\ell|}{2b}\sum_{j\ne0}e^{\tau|j|}|d_j|,
\tag{228.24}
$$

$$
\chi_H\le\frac12\sum_{j\ne0}|j|e^{\tau|j|}
 \left(|\alpha_j|+\frac{|\ell|}{b}|d_j|\right),
\tag{228.25}
$$

其中

$$
\gamma_0=\tfrac12\left|sb+(\ell/b)\langle d\rangle\right|.
$$

因为 $\sinh t\le e^t/2$，(228.24) 的非零模部分和 (228.25) 分别至多是 R69(69.24) 所列那份**标量充分上界**的一半。这不是宣称它们恰好等于原精确矩阵范数定义的一半。更窄角宽时还可用

$$
\sum_{j\ne0}\sinh(\tau|j|)|\alpha_j|
\le\tau\sum_{j\ne0}|j|e^{\tau|j|}|\alpha_j|.
\tag{228.26}
$$

这里仍使用同一完整 $D,L,U,c$，没有删去 mean 或把 $d$ 改成背景值 1。

## 8. 偶频 sine/cosine 中心的零模准确结构

在本节及 (228.23) 中，$U=K_\theta-P$、$E=1+w^2$，$\mathcal N_P,\mathcal N_K$ 是 R69 对完整 $\mathcal N(P,K,T,V)$ 的独立变量偏导，不预先冻结或删去 $c$。

假设实际中心具有原 parity：$P$ 为奇 sine 场，$K$ 为含完整均值的偶 cosine 场。允许一次共同的常数角相位平移；若相位随径向变化，则其导数须另付。

此时 $P_\theta,L,D,\mathcal N,\mathcal N_K$ 为偶函数，$U,q,\mathcal N_P,q_x$ 为奇函数，$q_\theta$ 为偶函数。准确的剪切和 frame 零阶矩阵为

$$
\widehat C=
\begin{pmatrix}
 -(s+\ell)+s q_\theta+b_x/b&0\\
 [\mathcal N_P+q(s-\ell+\mathcal N_K)-q_x+sqq_\theta]/b
 &-2\ell+\mathcal N_K
\end{pmatrix}.
\tag{228.27}
$$

它来自 R69 的 $SCS^{-1}+S_xS^{-1}+SA(S^{-1})_\theta$ 及 $B_xB^{-1}$，所有导数原样保留。

左下项是奇函数，其零模准确为零；此外 $\langle q_\theta\rangle=0$。因此

$$
\boxed{\quad
\widehat C_0=
\operatorname{diag}\left(
 -s-\ell+b_x/b,\ -2\ell+\langle\mathcal N_K\rangle
\right).
\quad}
\tag{228.28}
$$

故 (228.12) 的常数项准确为

$$
\lambda_{\max}(H_0)=
\max\left(-s-\ell+b_x/b,
          -2\ell+\langle\mathcal N_K\rangle\right).
\tag{228.29}
$$

不能把 $q_x$ 的整个正范数充作一个零 Fourier 系数；它的非零模贡献仍须全部付出。分片常数 $b$ 的片内 $b_x/b=0$，接口跳变仍保留。

对非零模，令

$$
D_j=\max\bigl(|s(q_\theta)_j|,|(\mathcal N_K)_j|\bigr),
$$
$$
G_j=\left[\mathcal N_P+q(s-\ell+\mathcal N_K)-q_x+sqq_\theta\right]_j/b.
$$

将 (228.27) 的非零模写为对角项加 $G_jE_{21}$，可得一个直接的充分界

$$
\zeta_H\le\lambda_{\max}(H_0)
+\sum_{j\ne0}\cosh(\tau|j|)D_j
+\frac12\sum_{j\ne0}e^{\tau|j|}|G_j|.
\tag{228.30}
$$

这里一半系数只作用于该非零下三角项。使用额外标量三角界后，应按第 6 节区分它与精确矩阵范数定义；不能无条件声称 (228.30) 的每一种粗实现都优于旧的每一种粗实现。

完整 mean 消元若另产生非局部项，仍在 $\mathcal R$ 中按 (228.4) 支付；(228.28) 只陈述上述局部完整矩阵的零模，不将非局部项归零。

## 9. 两源、frame 与径向先取上确界的范数

应用于 R69 的变换时，$W=BSX$，所以完整源为 $F=BSf$。当前候选若两行残差均非零，必须使用完整两列。只有另证 $f_P=0$，才有 R69 特殊情形中的 $BSf=f$。

所有 $S_x,S_\theta,B_x$ 必须包含于实际矩阵，完整 mean 的真实 $c_x$ 也必须保留。对未满足原方程的候选，不能用方程右端替换其实际径向导数。各接口使用准确的 $B^+S^+(B^-S^-)^{-1}$；只有另证 $S^+=S^-$，才可简化为纯 $b$ 跳变。

### 9.1 单个径向点的转换

若 $0\le\sigma<\tau$、$\delta=\tau-\sigma$，对一个固定 $x$，有

$$
\sum_m(1+|m|)e^{\sigma|m|}\|X_m(x)\|_2
\le C_\delta\|X(x)\|_{\ell^2_\tau},
$$
$$
C_\delta^2=
\frac{2(1+e^{-2\delta})}{(1-e^{-2\delta})^3}-1.
\tag{228.31}
$$

这是 R69 的精确全整数几何级数和 Cauchy 不等式。若在这个同一径向点把两个分量的 Wiener 范数相加，再付 $\sqrt2$。

### 9.2 整个区间的径向先取上确界

设已经通过真实逆 frame 得到

$$
M_X\ge\sup_{x\in I}\|X(x)\|_{\ell^2_{\tau(x)}}.
$$

对输出角宽 $\sigma(x)$，假设
$\tau(x)-\sigma(x)\ge\delta>0$。每个分量、每个模式分别满足

$$
\sup_x e^{\sigma(x)|m|}|X_{\alpha,m}(x)|
\le M_Xe^{-\delta|m|}.
$$

因此完整两分量的径向先取上确界规范有安全上界

$$
\begin{aligned}
&\sum_{\alpha=1}^2\sum_m(1+|m|)
 \sup_x e^{\sigma(x)|m|}|X_{\alpha,m}(x)|\\
&\qquad\le2M_X S_\delta,\qquad
S_\delta=\sum_m(1+|m|)e^{-\delta|m|}
=\frac{1+2q-q^2}{(1-q)^2},\quad q=e^{-\delta}.
\end{aligned}
\tag{228.32}
$$

可使用实际偶频支持进一步收紧，但不能将 (228.31) 的点态 $\sqrt2C_\delta$ 直接移到径向先取上确界后。不同模、不同分量可以在不同位置取得最大值，$\sup_x\sum_m$ 与 $\sum_m\sup_x$ 不能交换。若另有已支付的更强逐模径向 $\ell^2$ 控制，则可使用其更紧转换；这里不预设该额外信息。

## 10. 定理适用范围与实际下一输入

本结果要求在真实角度上的矩阵函数为实值，所以允许围绕真实中心的复变化量，但不自动涵盖复参数中心。若改用复中心，必须重新支付其真正伴随块，不能沿用 (228.2)。

本结果也不消除以下实际输入：

1. 同一候选/邻域上的完整 mean、解析分母和平方根定义域，以及所有已存在非局部导数项。
2. 实际 $A_j,C_j$ 或它们的完整有界替代量，包括真正的常数 Fourier 系数和全部非零系数尾；已有一个全正系数总帽不自动提供 signed $C_0$。
3. 实际角宽微分门 (228.15)、完整 signed 零阶积分、源起点顺序及所有 partial/接口/端口费用。
4. 从所估计的变换变量和 source 测度到原物理两分量的准确单位转换，以及需要时 (228.32) 的径向先取上确界转换。
5. 若以原系统的有限 Galerkin 场作存在近似，需保原投影与非恒定剪切的交换项，或使用另一个已经完整证明的存在接口；不能把变换后 Galerkin 的能量等式直接移给原投影。

因此 R228 是对原条件能量估计的严格改进，不是现成的未知高频反馈闭合证书。原 R203 的实际成功项和失败预算原样保留；只有用同一真实数据重新消费这些新公式后，才有新的数值结论。

本次完整读取的原文本是
`topics/visible-flex-larger-amplitude/results/R69-complete-mean-principal-symbol-and-analytic-frame.md`，提交
`e3b7f8f48244870fd7b902fc28168cfc7dcf937c`，Git blob
`42f85bbb092cdda2172237d2e4ee2c3e43d35c0f`。

该 provenance 指向已有 R69 证明；本次未运行新的 ODE、均值求积或科学数值预算。
