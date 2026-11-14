# 真正常湮灭矩的块密度映射、完整残量与正性对偶证书

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065。

**状态：已证明的有限块接口；主问题仍开放。**
本稿将任意正正常密度的块矩写成准确线性映射，
保留完整实际 carry，并把 R235 的全部右测试限制成真正的有限块向量残量。
另外给出一个有限维正性优化的准确对偶：
若能找到预算内的理想右因子使其对偶证书有固定余量，
便与正常态的尾真空质量矛盾。
本文没有构造这样的证书，也没有把固定非湮灭态的特殊相干分量搬到未知见证上。

## 1. 任意块约化密度的准确矩向量

令 $B$ 是 $q$ 个物理位，$\rho\ge0$ 为原 $H$ 上迹类，
$\lambda=\operatorname{Tr}\rho$。
其准确块约化密度为
$$
\rho_B=\operatorname{Tr}_{B^c}\rho\ge0,\qquad
\operatorname{Tr}\rho_B=\lambda.
$$
纯块仍用 $D_j=I-2E_j$，$X_u^0=\sum_{F\subseteq B}u_FD_F$。
定义
$$
\boxed{
\mathcal L_B(\rho_B)
=\sum_{F\subseteq B}\operatorname{Tr}(\rho_BD_F^*)\chi_F
=:m_B.
}
\tag{1.1}
$$
内积在第一变量线性。由于 $\rho_B$ 自伴，
$$
\boxed{
\operatorname{Tr}(\rho X_u^0)=\langle u,m_B\rangle.
}
\tag{1.2}
$$
这里必须保留共轭：
$m_{B,F}=\overline{\operatorname{Tr}(\rho_BD_F)}$。
固定实例的矩恰为实数，不能据此省掉一般情形的共轭。

若 $\rho_B=\sum_\ell f_\ell\otimes f_\ell$，
纯块交换性给另一个准确式
$$
\boxed{m_B=\sum_\ell (X_{f_\ell}^0)^*f_\ell.}
\tag{1.3}
$$
这是正密度的总矩，未要求逐项分别满足配对域或零矩关系。

对任意可逆 $R\in\mathcal A_B^0$，$U=R^{-1}$，
完整纯有限 Gram 的对偶范数仍然准确为
$$
\boxed{
\sup_{u\ne0}
 \frac{|\operatorname{Tr}(\rho X_u^0)|}{\|Uu\|}
=\|R^*m_B\|.
}
\tag{1.4}
$$
最优列可取
$u=R(R^*m_B/\|R^*m_B\|)$，在分子非零时成立。
若 $R$ 收缩，则此列的原范数至多 $1$。
(1.4) 是真实 Hilbert Gram 的对偶，不是将正常矩矩阵当作正 Gram。

## 2. 映射的完整范数预算和正常尾的限制

单个位有 $\|D\|=1+\sqrt2$。
因此令
$$
K_q=(4+2\sqrt2)^{q/2},
$$
Cauchy--Schwarz 给
$$
\|X_u^0\|
\le\sum_F|u_F|(1+\sqrt2)^{|F|}
\le K_q\|u\|.
\tag{2.1}
$$
所以对自伴迹类块矩阵 $\sigma$，
$$
\boxed{\|\mathcal L_B(\sigma)\|\le K_q\|\sigma\|_1.}
\tag{2.2}
$$

还有一个准确的 Hilbert--Schmidt 公式。
将 $\mathcal L_B$ 以 (1.1) 线性延拓到所有块矩阵，
则单个位的行 Gram 是
$$
\mathcal L_1\mathcal L_1^*
=
\begin{pmatrix}2&2\\2&6\end{pmatrix}.
\tag{2.3}
$$
其特征值为 $4\pm2\sqrt2$。
张量性给
$$
\boxed{
\mathcal L_B\mathcal L_B^*
=
\begin{pmatrix}2&2\\2&6\end{pmatrix}^{\otimes q},
\qquad
\|\mathcal L_B\|_{\mathrm{HS}\to H_B}=K_q.
}
\tag{2.4}
$$
例如其逆行 Gram 为
$$
\left[
\frac18\begin{pmatrix}6&-2\\-2&2\end{pmatrix}
\right]^{\otimes q}.
$$
这可以准确求出给定矩的最小 Hilbert--Schmidt 线性原像，
但该原像不自动为自伴或正矩阵；
正密度条件不能由行 Gram 可逆替代。

若 $B$ 全在物理位 $m$ 之后，
令
$$
\delta_m=\operatorname{Tr}\rho(I-\Pi_m)\longrightarrow0
$$
为通常的头尾质量。
尾约化密度和其进一步约化的标准纯态迹距离界给
$$
\|\rho_B-\lambda\,\Omega_B\otimes\Omega_B\|_1
\le2\sqrt{\lambda\delta_m}.
$$
因此
$$
\boxed{
\|m_B-\lambda\Omega_B\|
\le2K_q\sqrt{\lambda\delta_m}.
}
\tag{2.5}
$$
(2.5) 显示确切的费用：
正常性只给 $\delta_m\to0$，没有统一速度，
不能让增长的 $K_q$ 免费消失。
另一方面，正性也未强迫 $m_B$ 带有某个固定相干张量分量。

## 3. 实际完整矩与纯块矩的欧氏误差

保持
$$
\|V_j-D_j\|\le8\eta_j,\qquad
\|V_j\|,\|D_j\|<3,\qquad
\eta_j\le e^{-770\,16^j}.
$$
对全部块列同时成立
$$
\boxed{
\|X_u-X_u^0\|\le d_B\|u\|,\qquad
d_B=8q(3\sqrt2)^q\eta_{\min B}.
}
\tag{3.1}
$$
证明是在每个有限乘积上 telescoping，
随后使用
$\sum_F|u_F|\le2^{q/2}\|u\|$。

定义实际矩向量
$$
\widehat m_B=
\sum_{F\subseteq B}
 \overline{\operatorname{Tr}(\rho V_F)}\,\chi_F.
$$
由 (1.2)、(3.1) 及有限维 Riesz 对偶，
$$
\boxed{
\|\widehat m_B-m_B\|\le\lambda d_B.
}
\tag{3.2}
$$
这是全部 $2^q$ 个列的一个欧氏范数界；
不能把单列误差在完整 Gram 中不加维数地复用。

## 4. 真湮灭者的完整右测试残量

沿用 R235：
$$
P_m\in S\mathcal A,\qquad
\|P_m-T_m\|\le e_m,\qquad
h_m=\langle T_m1,1\rangle>0,\qquad
\epsilon_m=e_m/h_m\longrightarrow0.
$$
若 $\rho$ 为真正常湮灭者，$\phi_\rho(SA')=0$，
则已证对全部实际 $G\in A'$，
$$
|\phi_\rho(T_mG)|/h_m
\le\lambda\epsilon_m\|G\|.
\tag{4.1}
$$

对有限位块 $B$，定义完整实际右测试向量
$$
\widehat r_{m,B}
=\sum_{F\subseteq B}
 \overline{\phi_\rho(T_mV_F)/h_m}\,\chi_F.
$$
由 (4.1)、(2.1)、(3.1)，
$$
\boxed{
\|\widehat r_{m,B}\|
\le\lambda\epsilon_m(K_q+d_B).
}
\tag{4.2}
$$
这将全 $G$ 约束完整转成有限块范数，而非只列出逐个 $F$ 的小量。

纯右列的向量为
$$
r^0_{m,B}
=\sum_{F\subseteq B}
 \overline{\phi_\rho(T_mD_F)/h_m}\,\chi_F.
$$
记 $\kappa_m=\|T_m\|/h_m$，则
$$
\boxed{
\|r^0_{m,B}\|
\le\lambda\bigl[
 \epsilon_m(K_q+d_B)+\kappa_m d_B
 \bigr].
}
\tag{4.3}
$$
这里 $\kappa_m$ 可能很大，已明确保留。

这个向量涉及一般非正交叉密度
$$
\operatorname{Tr}_{B^c}(\rho T_m)/h_m,
$$
不是单凭 $\rho_B$ 就能确定的量。
因为 $T_m$ 通常作用于块外，不能未经误差控制
把它写成某个纯块算子作用 $m_B$。

若另已构造 $K_B\in\mathcal A_B^0$，
在原全空间中确实满足
$$
\|T_m/h_m-K_B\|\le\tau_{m,B},
\tag{4.4}
$$
那么才有
$$
\boxed{
\|K_B^*m_B\|
\le\lambda\bigl[
 \epsilon_m(K_q+d_B)
 +\kappa_m d_B
 +\tau_{m,B}K_q
 \bigr].
}
\tag{4.5}
$$
(4.5) 的最后一项是完整函数演算与维数费用。
无限尾截断如果未支付这个相对算子范数，
不能把 (4.3) 当成 (4.5)。

## 5. 正性约束的准确有限维对偶

固定非零 $T\in\mathcal A_B^0$，假设其幂零理想常数项为零。
考虑正迹一块密度中所有完整右矩湮灭者：
$$
\mathcal C_B(T)=
\left\{
\sigma\ge0:\operatorname{Tr}\sigma=1,\quad
T^*\mathcal L_B(\sigma)=0
\right\}.
$$
由 (1.2)，最后一个条件等价于
$\operatorname{Tr}(\sigma TF)=0$
对所有 $F\in\mathcal A_B^0$ 成立。

令
$$
\alpha_B(T)=
\max_{\sigma\in\mathcal C_B(T)}
 \langle\sigma\Omega_B,\Omega_B\rangle.
\tag{5.1}
$$
这是一个准确有限维半定规划。
可行集非空且紧：$2^{-q}I$ 严格正，
而 $TF$ 对每个 $F\in\mathcal A_B^0$ 的物理矩阵对角为零，
所以规范迹确实可行。

它的对偶准确为
$$
\boxed{
\alpha_B(T)=
\inf_{\mu\in\mathbb R,\ u\in H_B}
\left\{
\mu:
\mu I-\Pi_{\Omega_B}
 +\operatorname{Re}(T X_u^0)\ge0
\right\}.
}
\tag{5.2}
$$
弱对偶直接对任一可行 $\sigma$ 取迹。
强对偶由有限维正锥分离得到：
规范迹给所有等式限制中的严格正可行点，
因此分离乘子不能只有一个非零正矩阵而没有目标乘子；
将目标乘子归一后恰得 (5.2)。
这也是有限维半定规划的 Slater 强对偶。
不要求某个指定右因子有预先的范数界。

如果 $(\mu,u)$ 满足 (5.2) 的正序，
对任意正 $\rho_B$、迹 $\lambda$，
$$
\langle\rho_B\Omega_B,\Omega_B\rangle
\le\mu\lambda+
 |\langle u,T^*m_B\rangle|
\le\mu\lambda+\|u\|\|T^*m_B\|.
\tag{5.3}
$$
因此，若 $B$ 在第 $m$ 位之后，
$$
\boxed{
\delta_m\ge
(1-\mu)\lambda-\|u\|\|T^*m_B\|.
}
\tag{5.4}
$$
结合实际残量 (4.5)，就得到一个明确、可复核的充分排除条件：
固定正余量 $1-\mu$，
同时让右端的残量乘 $\|u\|$ 趋零。
真正未证的是预算内证书，不是有限维每层的可解性。

## 6. 理想内近真空收缩给一个显式正性证书

有一个便于核对的充分构造。
若
$$
R=T X_v^0\in\mathcal A_B^0,\qquad
\|R\|\le1,\qquad
\|R\Omega_B-\Omega_B\|\le a<1,
\tag{6.1}
$$
则它的 $C$ 对称性及 $C\Omega_B=\Omega_B$
也给 $\|R^*\Omega_B-\Omega_B\|\le a$。
令 $H=\operatorname{Re}R$。
相对于 $\mathbb C\Omega_B\oplus\Omega_B^\perp$，
$H$ 的真空元至少 $1-a$，
交叉列范数至多 $a$，
其正交补压缩至少 $-I$。

对 $z\Omega_B+y$ 的交叉项用
$2a|z|\|y\|\le a|z|^2+a\|y\|^2$，得到
$$
H\ge(1-2a)\Pi_{\Omega_B}-(1+a)(I-\Pi_{\Omega_B})
=(2-a)\Pi_{\Omega_B}-(1+a)I.
$$
因此 (5.2) 有显式证书
$$
\boxed{
\mu=\frac{1+a}{2-a},\qquad
u=\frac{v}{2-a}.
}
\tag{6.2}
$$
当 $a<1/2$ 时有严格余量 $\mu<1$；
$a\to0$ 时 $\mu\to1/2$。

这说明一个理想内、实际预算内的近真空收缩
足以排正正常见证，而不需要让它有真空原像。
但 (6.1) 中的理想归属与右因子成本都不能省略。
R267 的无真空原像前向单位满足类似的收缩和真空接近性质，
却尚未证明属于慢 $S$ 的有界主理想；
本文没有替它补上该步骤。

## 7. 当前剩余点

一般正性并没有给出固定非湮灭例的相干张量分量。
$\rho_B$ 的全部矩准确由 (1.1) 给出，
而它与尾真空的距离在完整矩范数里支付 (2.5) 的指数费用。

真湮灭方程则给 (4.2)--(4.3) 的实际全部右测试残量。
只有支付完整的块外截断 (4.4)，才可把它与单个 $\rho_B$ 的
$K_B^*m_B$ 连接。之后必须进一步找到
(5.2) 中有正余量且成本可付的证书，
或以其他方式构造专属正则器使 R244 完整 Gram 一致有界。

这些接口尚未给一般正常湮灭者的排除，
也未完成普通 Hilbert ISP。

依赖：

- [R244 聚合逆图与完整 Gram](../results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)；
- [R235 真湮灭者全部实际右测试](../results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)；
- [R253 正部分迹与真实尾约化](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)；
- [R267 无真空原像的共同幂倍数](../results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)；
- [任意纯收缩块的完整 Gram](2026-11-13-arbitrary-contractive-block-complete-gram-and-source-obstruction-normal-complex.md)。
