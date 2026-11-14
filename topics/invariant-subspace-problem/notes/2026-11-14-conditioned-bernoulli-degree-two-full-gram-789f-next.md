# 条件 Bernoulli 的完整二次商 Gram：显式算子误差及真实出生二精度

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：本稿全部定理已证明。** 新结论是整个常数、一次 primitive、二次 primitive 的共同空间上的条件 Gram 算子估计，并由完整低次数 Schur 推出真实出生二精度的渐近共同源表示。它不是逐条目局部中心极限定理，也不把单高度比较当成相邻加强 S1。原连续尾的相邻回归创新仍需另行运输。

## 1. 完整共同空间与定理

先取有限个相互独立的 Bernoulli 变量 $X_i$，参数 $0<p_i<1$，并设

$$
N=\sum_iX_i,\qquad \sum_ip_i=k\in\mathbb Z,
\qquad v_i=p_i(1-p_i),\quad a_i=\sqrt{v_i},\quad V=\sum_iv_i.
$$

乘积概率记为 $\pi$。局部标准正交基为 $1,\chi_i$，其中

$$
\chi_i=\frac{X_i-p_i}{a_i}.
$$

乘积 Fourier 基 $\chi_I=\prod_{i\in I}\chi_i$ 正交归一。记其齐次次数空间为 $\mathcal H_j$，并置

$$
d_a=\sum_i a_i E_i,\qquad K_j(a)=\ker d_a\cap\mathcal H_j,
\qquad \mathcal E=K_0(a)\oplus K_1(a)\oplus K_2(a).
\tag{1.1}
$$

这里 $E_i\chi_I=\chi_{I\setminus i}$（$i\in I$），其余为零。$\mathcal E$ 采用乘积概率的原正交内积。以条件概率 $\pi(\cdot\mid N=k)$ 定义同一空间上的 Gram 算子 $G$：

$$
\langle F,GH\rangle=\mathbb E_\pi[\overline F H\mid N=k].
$$

**定理 1.** 若 $V\ge8192$，则

$$
\boxed{\quad \|G-I_{\mathcal E}\|\le\frac{256}{\sqrt V}.\quad}
\tag{1.2}
$$

特别地，若 $V\ge2^{18}$，则 $\tfrac12 I\preceq G\preceq\tfrac32I$。常数与位数、各个 $p_i$、源 $F$ 无关。同一结论适用于可数多个变量，只要 $\sum p_i=k<\infty$。

估计保留了 $K_0,K_1,K_2$ 之间的全部交叉块；不能把它改读为三个独立的对角估计。

## 2. 原始逐位矩阵与主弧 Gauss 消去

令

$$
\phi_i(\theta)=1-p_i+p_i e^{i\theta},\qquad
\phi(\theta)=\prod_i\phi_i(\theta).
$$

乘法 $e^{i\theta X_i}$ 在局部基 $\{1,\chi_i\}$ 中的矩阵准确为

$$
M_i(\theta)=
\begin{pmatrix}
\phi_i&a_i(e^{i\theta}-1)\\
a_i(e^{i\theta}-1)&p_i+(1-p_i)e^{i\theta}
\end{pmatrix}.
\tag{2.1}
$$

只有在 $|\theta|\le1/4$ 的主弧上才使用以下分解。设

$$
\beta_i=\frac{a_i(e^{i\theta}-1)}{\phi_i},\qquad
\delta_i=\frac{e^{i\theta}}{\phi_i^2}.
$$

则逐位的下三角—对角—上三角分解给完整乘积

$$
\prod_iM_i(\theta)
=\phi(\theta)\exp(c_\beta)D_\delta\exp(d_\beta),
\tag{2.2}
$$

其中 $d_\beta=\sum\beta_iE_i$、$c_\beta=\sum\beta_iE_i^*$，而 $D_\delta\chi_I=\prod_{i\in I}\delta_i\chi_I$。由于 $\beta_i$ 可为复数，**$c_\beta$ 不是 $d_\beta$ 的 Hilbert 伴随**；(2.2) 只是精确矩阵乘积。

令 $P=P_{\mathcal E}$，$e_i=\beta_i-i\theta a_i$。所有下降算子两两交换，所有上升算子也两两交换；又有 $d_aP=0$、$Pc_a=0$。因此

$$
P\exp(c_\beta)D_\delta\exp(d_\beta)P
=P\exp(c_e)D_\delta\exp(d_e)P.
\tag{2.3}
$$

这一步在两侧同时精确消去了范数为 $|\theta|\sqrt V$ 的集体一阶项。

在主弧上 $|\phi_i|\ge\cos(1/8)>31/32$，直接用 $|e^{i\theta}-1-i\theta|\le\theta^2/2$ 得

$$
|e_i|\le2a_i\theta^2,\qquad r:=\|e\|_2\le2\sqrt V\,\theta^2.
\tag{2.4}
$$

在次数至多二的空间中，$\|d_e\|\le\sqrt2r$、$\|d_e^2\|\le\sqrt2r^2$，所以

$$
\|\exp(d_e)\|,\ \|P_{\le2}\exp(c_e)P_{\le2}\|
\le1+2r+r^2=(1+r)^2.
$$

此外 $|\delta_i'|\le4$、$|\delta_i|\le2$；对至多两个因子的乘积求导可得

$$
\|D_\delta-I\|_{\mathcal H_{\le2}}\le16|\theta|.
$$

由 (2.3) 及三角不等式，记其右侧压缩为 $H(\theta)$，便有

$$
\begin{aligned}
\|H(\theta)-I_{\mathcal E}\|
&\le16|\theta|+20r+30r^2+20r^3+5r^4\\
&\le16|\theta|+40\sqrt V\theta^2+120V\theta^4
+160V^{3/2}\theta^6+80V^2\theta^8.
\end{aligned}
\tag{2.5}
$$

没有对 $F$ 的单个系数求和；(2.5) 是整个共同空间的算子范数估计。

## 3. 尾弧：保原始矩阵，避免奇异分母

本节不使用 $\beta_i,\delta_i$。由 (2.1)，两个对角条目的绝对值都等于 $|\phi_i|$，而非对角条目绝对值为 $2a_i|\sin(\theta/2)|$。又

$$
|\phi_i|\le\exp[-2v_i\sin^2(\theta/2)].
$$

若 $|I|,|J|\le2$，至多删去 $I\triangle J$ 的四个位，其总方差至多一。因此原完整乘积的相应条目满足

$$
|\langle\chi_I,e^{i\theta N}\chi_J\rangle|
\le e^{-2(V-1)\sin^2(\theta/2)}
\prod_{i\in I\triangle J}2a_i.
\tag{3.1}
$$

右侧的正条目矩阵被

$$
B=P_{\le2}\exp(2c_a)\exp(2d_a)P_{\le2}
$$

逐条目支配：在其展开中，先删去 $J\setminus I$、再加入 $I\setminus J$ 的路径已恰给所列乘积，其余路径的系数非负。因而绝对值矩阵支配给真正的算子估计；对 $V\ge16$，

$$
\|B\|\le(1+2\sqrt{2V}+2\sqrt2V)^2\le16V^2,
$$

从而

$$
\boxed{
\|P_{\le2}e^{i\theta N}P_{\le2}\|
\le16V^2 e^{-2(V-1)\sin^2(\theta/2)}.
}
\tag{3.2}
$$

特别地，$p_i$ 接近 $1/2$、$\theta$ 接近 $\pi$ 时仍然有效；从未把可能出现的 $\phi_i^{-1}$ 单独有界化。

## 4. 条件概率与显式积分常数

置 $\psi(\theta)=e^{-ik\theta}\phi(\theta)$。对所有 $|\theta|\le\pi$，

$$
|\psi(\theta)|\le e^{-2V\sin^2(\theta/2)}\le e^{-V\theta^2/5}.
\tag{4.1}
$$

在 $|\theta|\le1/4$ 上，逐位 $\log\phi_i$ 的三阶导数绝对值至多 $2v_i$，故

$$
\log\psi(\theta)=-V\theta^2/2+R(\theta),\qquad
|R(\theta)|\le V|\theta|^3/3.
$$

于是主弧上的 $L^1$ Gaussian 误差至多

$$
\int_{\mathbb R}\frac{V|\theta|^3}{3}e^{-5V\theta^2/12}\,d\theta
=\frac{48}{25V}<\frac2V.
$$

由 (4.1) 估计其余两条尾弧和实 Gaussian 尾，得到

$$
\left|2\pi\mathbb P(N=k)-\sqrt{2\pi/V}\right|\le\frac{30}{V}.
\tag{4.2}
$$

因此 $V\ge4096$ 时

$$
\mathbb P(N=k)\ge\frac1{4\sqrt V}.
\tag{4.3}
$$

在主弧上还可用 $|\psi|\le e^{-V\theta^2/3}$。把 (2.5) 的五项分别积分到整条实线，用 $\sqrt\pi<2$、$\sqrt3<2$ 得

$$
\begin{aligned}
\int_{-1/4}^{1/4}|\psi|\|H-I\|\,d\theta
&\le \frac{48+240}{V}
+\frac{3240}{V^{3/2}}+\frac{32400}{V^2}
+\frac{170100}{V^{5/2}}\\
&\le\frac{352}{V}\qquad(V\ge4096).
\end{aligned}
\tag{4.4}
$$

尾弧上由 (3.2)、(4.1)、$V-1\ge V/2$，

$$
\begin{aligned}
&\int_{1/4\le|\theta|\le\pi}
\bigl(\|Pe^{i\theta N}P\|+|\phi(\theta)|\bigr)\,d\theta\\
&\hspace{15mm}\le680V e^{-V/160}\le\frac1V\qquad(V\ge4096).
\end{aligned}
\tag{4.5}
$$

最后一个实变量不等式在 $V=4096$ 已成立，且 $V^2e^{-V/160}$ 在这一区间递减。

Fourier 反演给

$$
G-I=\frac1{2\pi\mathbb P(N=k)}
\int_{-\pi}^{\pi}e^{-ik\theta}
\bigl(Pe^{i\theta N}P-\phi(\theta)I\bigr)\,d\theta.
$$

由 (4.3)–(4.5)，

$$
\|G-I\|\le\frac{706}{\pi\sqrt V}<\frac{256}{\sqrt V}.
$$

这证明有限情形；保留 $V\ge8192$ 的声明是为了可数极限无须处理阈值等号。

## 5. 可数无限情形

设 $\sum_i p_i=k<\infty$。取前 $M$ 个 odds $z_i=p_i/(1-p_i)$，乘共同参数 $t_M$ 使相应 Bernoulli 均值仍等于 $k$。对 $M>k$ 此参数唯一存在；$t_M\to1$，故 $p^{(M)}\to p$ 于 $\ell^1$，$a^{(M)}\to a$ 于 $\ell^2$，$V_M\to V$。

一次 primitive 投影显然连续。二次处用完整恒等式

$$
d_a d_a^*|_{\mathcal H_1}
=VI-2\operatorname{diag}(v_i)+aa^*\succeq(V-1/2)I.
\tag{5.1}
$$

故 $P_{K_2(a)}=I-d_a^*(d_a d_a^*)^{-1}d_a$ 在所列极限中强连续。先对有限支撑向量作这些投影，再用稠密性，得到 $\mathcal E$ 的有限头逼近。

条件概率及有限支撑函数的条件矩随 $\ell^1$ 参数极限收敛，因 $\mathbb P(N=k)>0$。由有限情形的统一算子界，极限推广到整个 $\mathcal E$，证明 (1.2)。这里没有假定无限完整逆自动有界；所需投影的有界逆正由 (5.1) 给出。

## 6. 全部次数至多二的商，不能只压最高次数

对于有限位数，记 $\mathscr P_{\le j}$ 为次数至多 $j$ 的多线性多项式。在 product Fourier 坐标下

$$
N-k=\sum_i a_i\chi_i.
$$

任意二次多项式的最高次系数可唯一写作 $F_2+d_a^*u$，其中 $F_2\in K_2(a)$；(5.1) 保证 $d_a^*$ 满列秩。减去 $(N-k)\sum u_i\chi_i$ 后，二次部分恰为 $F_2$。再减去 $(N-k)$ 的常数倍，可使一次部分属于 $K_1(a)$。因此

$$
\mathscr P_{\le2}=\mathcal E\ \dotplus\ (N-k)\mathscr P_{\le1}.
\tag{6.1}
$$

这是真正的完整切片商：主定理的严格下界（取 $V\ge2^{18}$）说明 $\mathcal E$ 的非零向量不会在 $N=k$ 上消失，故 (6.1) 不遗漏其他低次数核。全部常数与线性 nuisance 在 $\mathcal E$ 中正好对应 $K_0(a)\oplus K_1(a)$。它们与 $K_2(a)$ 的条件交叉块必须在极小化时保留。

## 7. 对真实出生二精度的共同源推论

现在取有限或可数正权 $b_i$，$z_i=b_i^2$，可数时假设 $\sum z_i<\infty$。选 $t>0$ 使

$$
p_i=\frac{tz_i}{1+tz_i},\quad
\sum_i p_i=k=n+2,\quad
V=\sum_i\frac{tz_i}{(1+tz_i)^2}\ge2^{18}.
$$

有限情形取合法高度 $0\le n\le M-4$。设 $K=K_2(b)$，物理源内积仍为原占据正交内积，$C_n=\Gamma_{n,2}^{-1}$ 使用**先完整 Moore–Penrose 逆、再压 primitive**的原定义。按 R296 的完整回归表示，

$$
\langle C_nf,f\rangle
=e_k(z)\inf_{q\in\mathscr P_{\le1}}
\mathbb E_{\mu_k}|\Phi_f-q|^2,
\qquad
\Phi_f=\sum_{i<j}\frac{f_{ij}}{b_ib_j}X_iX_j.
\tag{7.1}
$$

条件 Bernoulli 概率恰为 $\mu_k$。在 product Fourier 坐标中，$\Phi_f$ 的最高二次系数是 $D_tf$，其中完整 $\mathcal H_2$ 上的正对角算子为

$$
(D_tf)_{ij}=\frac{t f_{ij}}{(1+tz_i)(1+tz_j)}.
\tag{7.2}
$$

置 $a_i=\sqrt t\,b_i/(1+tz_i)$。完整对角变换精确把旧 nuisance 子空间送到新 nuisance 子空间：若 $(d_tu)_i=\sqrt t\,u_i/(1+tz_i)$，则

$$
D_t d_b^*u=d_a^*d_tu.
\tag{7.3}
$$

所以真实最高次商映射为

$$
T_t=P_{K_2(a)}D_t|_K,
\qquad
A_t=T_t^*T_t
=\bigl(P_KD_t^{-2}|_K\bigr)^{-1}.
\tag{7.4}
$$

最后等式是正对角算子的完整 shorting 身份：$\|T_tf\|^2=\inf_{h\in K^\perp}\|D_t(f+h)\|^2$。可数情形中 $D_t,d_t$ 都有正的统一对角上下界，所以闭包、商映射与所列逆也合法。

由第 6 节，(7.1) 恰为在共同 Gram $G$ 中保留最高系数 $T_tf$，再对全部 $K_0\oplus K_1$ 极小化。令 $\epsilon=256/\sqrt V\le1/2$；完整 Gram 的双侧界在该 Schur 极小化后给

$$
\boxed{
(1-\epsilon)e_k A_t\preceq C_n\preceq(1+\epsilon)e_k A_t.
}
\tag{7.5}
$$

等价地，在同一个原物理源 $K$ 上，

$$
\boxed{
\frac1{(1+\epsilon)e_k}\,P_KD_t^{-2}|_K
\preceq\Gamma_{n,2}\preceq
\frac1{(1-\epsilon)e_k}\,P_KD_t^{-2}|_K.
}
\tag{7.6}
$$

这里保留了因子 $e_k$、原 $b$-primitive 源以及所有低次数回归；没有把 $P_KD_t^2P_K$ 误用作真实精度。可数情形的 (7.1)–(7.6) 可先对有限头及有限物理源取极限，再由统一下界和闭包扩充；也可直接在上述有界商上作极小化。

## 8. 已证范围与下一接口

(1.2) 是任意 Bernoulli 参数在方差充分大时的完整 degree-two 条件 Gram 定理；(7.5) 是它对真实最小逆的单高度共同源应用。它允许相邻高度在同一个原 $K_2(b)$ 上比较相应对角 shorting，但**实际创新还包含相邻回归系数二阶差**。尚未由 (7.5) 单独推出加强 S1、原 graph $T^*T$ 的跨出生逆传播或主 ISP 结论。
