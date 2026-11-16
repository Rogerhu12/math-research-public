# R865：原 Y 的真实 T₇ 对应与旧 Fourier 行的准确短矩阵接口

日期：2026-11-16。状态：**本篇的双陪集、半线性公式、短注入与准确消费判据已证明；尚未登记任何实际 T₇ 矩阵、特征多项式或活跃投影。**

本篇保留原 $p=41$、$Y=X_1/\mu_3$、$g(Y)=127$、$K=\mathbb Q(s)$、$s=1+2\zeta$、$s^2=-3$，以及原参考 cusp、$q_Y=\exp(2\pi i\tau/82)$。它接 [R864 的真实127维全纯基](R864-certified-original-canonical-holomorphic-basis.md)，为原 YP/Hecke 任务提供第一个明确可执行的全空间对应。既有 genus54 的 $X_{\rm ns}^+(41)$ Hecke 表不是这里的127维矩阵；[R862 的原 A 投影](R862-original-Rosati-projector-from-certified-Hom-correspondences.md)也不是原 Y 的活跃 $e_\eta$。

## 1. 既有来源与尺度

[R771](../notes/R771-original-quotient-RR-bases-method.md)、[R775](../notes/R775-original-K-defined-RR-bases-method.md)固定
$$
G=C_3\times N_{\mathsf T}(\mathbb F_{41})
\subset\operatorname{GL}_2(\mathbb Z/82),\qquad
H=G\cap\operatorname{SL}_2(\mathbb Z/82),\qquad |H|=252,
\tag{865.1}
$$
其中原环面为
$$
\mathsf T=\left\{\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}:
a^2+ab+b^2\ne0\right\}.
$$
令 $\Gamma$ 是 $H$ 在 $\operatorname{SL}_2(\mathbb Z)$ 中的原逆像。它不是 $\Gamma_0(1681)$ 或另一个同亏格群。令 $Z/\mathbb Q$ 为该完整 $G$ 的标准模曲线；原识别为
$$
\theta:Y_K\longrightarrow Z_K,\qquad
\theta^*(E_6/\eta^{12})=24s(2t_Y-1).
\tag{865.2}
$$

使用 R805/R786 的原146条权二截面 $e_i$。它们已经是 $e_i=82^2T_{1,i}$ 的整数尺度；源字段 `integer_qY_xi_coefficients` 直接给 $e_i$ 的展开，而不是另一个尚待乘 $82^2$ 的截面。记
$$
e_i=\sum_{n\ge0}a_{n,i}q_Y^n,
\qquad a_{n,i}=\sum_{r=0}^{39}a_{n,r,i}\xi^r,
\quad \xi=\zeta_{41},\quad \xi_{82}=-\xi^{21}.
\tag{865.3}
$$
已成 R786 原行包含 $0\le n\le128$；本篇只读取其中 $n\le91$。不重新生成 E1、迹、正常乘积或 q 尾。

R864 给准确矩阵 $B\in\mathbb Q^{146\times127}$，其第 $j$ 列是原 `original_V1_coefficients`。因此
$$
F_j=\sum_{i=0}^{145}e_i B_{ij},\qquad
\omega_j=82F_j\,\frac{dq_Y}{q_Y}
\tag{865.4}
$$
构成原 $H^0(Y_K,\Omega^1)$ 的基。$B$ 的有理性只是相对于这组原 $K$ 基的系数性质；并未自动给出 $\mathbb Q$ 固定微分基。

R866 将只计算一次共同矩阵
$$
\mathsf H_{40n+r,j}=\sum_i a_{n,r,i}B_{ij},
\qquad 0\le n\le13,
\tag{865.5}
$$
及它的一个准确127阶逆。$\mathsf H$ 就是 $F_j$ 的展开；微分系数是 $82\mathsf H$。来源 `matrix_integer_scale=6724` 记录 $e_i$ 的固有尺度，不能据此再乘或除 $82^2$。本篇后继直接消费已成 $\mathsf H$、选行和逆，不重算这三项。

## 2. 一个明确的原 level82 双陪集

取
$$
g_7=\begin{pmatrix}1&-2\\2&3\end{pmatrix},\qquad
\det g_7=7.
\tag{865.6}
$$
它的 mod2 分量为恒等，mod41 分量是原环面 $T(1,2)$。因此 $\bar g_7\in G$，且 $\det\bar g_7=7$。定义
$$
\Delta_7=\{A\in M_2(\mathbb Z):\det A=7,\ \bar A\in H\bar g_7\}.
\tag{865.7}
$$
因为 $H\lhd G$，这是一个 $\Gamma$ 双不变集合。

以下两矩阵是指定的整数 determinant-one 提升：
$$
\gamma_0=\begin{pmatrix}1&-12\\2&-23\end{pmatrix},\qquad
\gamma_\infty=\begin{pmatrix}47&-2\\-70&3\end{pmatrix}.
\tag{865.8}
$$
这里 $7^{-1}=47$ modulo82，且
$$
\bar\gamma_0=\bar g_7\operatorname{diag}(1,47),\qquad
\bar\gamma_\infty=\bar g_7\operatorname{diag}(47,1).
\tag{865.9}
$$
令
$$
m_\infty=\begin{pmatrix}7&0\\0&1\end{pmatrix},\qquad
m_b=\begin{pmatrix}1&82b\\0&7\end{pmatrix}\quad(0\le b<7),
\quad
\alpha_\infty=\gamma_\infty m_\infty,\quad
\alpha_b=\gamma_0m_b.
\tag{865.10}
$$
全部八个 $\alpha$ 的 mod82 像恰为 $\bar g_7$。

**命题865.1。** 原双陪集 $\Delta_7$ 的左 $\Gamma$ 陪集恰由 (865.10) 的八个矩阵代表。它们是同一个 $\Gamma$ 双陪集，而非八个无关的局部试探。

**证明。** determinant 为素数7的整数矩阵自动 primitive。其左 $\operatorname{SL}_2(\mathbb Z)$ 陪集具有 usual Hermite 代表 $m_\infty$ 及七个 $m_b$；用 $82b$ 代替 $b$ 仍覆盖全部模7余数。若 $A=\gamma m_i\in\Delta_7$，其 mod82 条件给
$$
\bar\gamma\in H\bar g_7\bar m_i^{-1}=H\bar\gamma_i.
$$
因此 $\gamma\gamma_i^{-1}\in\Gamma$，故 $\Gamma A=\Gamma\alpha_i$。八个陪集互异，因为其较大的左 $\operatorname{SL}_2(\mathbb Z)$ 陪集已经互异。又 $\Gamma$ 包含 $\Gamma(82)$，CRT 及 $\operatorname{SL}_2(\mathbb Z)$ 的约化满射说明 $\Gamma\to\operatorname{SL}_2(\mathbb F_7)$ 满射；其右作用在对应的 $\mathbb P^1(\mathbb F_7)$ 上传递，故八个左陪集组成一个双陪集。证毕。

在标准模曲线上，该对应的模意义是保留原 $G$-level82 结构并选一个循环7阶子群。源映射保留曲线，靶映射商掉该子群，并通过7-isogeny运输 prime-to-7 的82水平结构。因此它是定义在 $\mathbb Q$ 上的有限代数对应，不由 Fourier 数据猜造。

取权二归一
$$
(F|_2A)(\tau)=\det(A)(c\tau+d)^{-2}F(A\tau).
\tag{865.11}
$$
对微分的 pull-push 恰为
$$
T_7F=F|_2\alpha_\infty+\sum_{b=0}^6F|_2\alpha_b.
\tag{865.12}
$$
这里没有再除7，也没有再乘82。

## 3. 两个 Galois 方向的准确 Fourier 公式

Zywina 的 [Lemma4.3](https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf)规定原右作用：SL2 元素给 slash，$\operatorname{diag}(1,d)$ 给系数作用 $\sigma_d(\xi_{82})=\xi_{82}^d$。其 Lemma4.5 与 R775 的半线性迹说明所有 $e_i$、因而所有 $F_j$ 都被 $G$ 固定。对额外的 $K$ 系数，本篇的 $\sigma_d$ 固定 $s$；这由 $K\cap\mathbb Q(\xi)=\mathbb Q$ 唯一确定，绝不是 $c_Y$ 或实际复共轭。

由 (865.9) 和右作用的乘法次序，
$$
F|_2\gamma_0=\sigma_{47}(F).
\tag{865.13}
$$
对另一项，$\operatorname{diag}(47,1)=47I\operatorname{diag}(1,7)$ modulo82，而标量 $47I$ 在原 $G$ 内。因此
$$
F|_2\gamma_\infty=\sigma_7(F).
\tag{865.14}
$$
这两式只使用真实 $G$ 固定性，不要求单独的 $\sigma_7F=F$。

写 $F=\sum_{n\ge1}a_nq_Y^n$。有限七项中
$$
q_Y\bigl((\tau+82b)/7\bigr)=q_Y(\tau)^{1/7}\exp(2\pi ib/7).
$$
七项求和与 (865.11) 的 $1/7$ 恰好抵消，只留下7整除指数。无穷项为 $7\sigma_7(F)(7\tau)$。故
$$
\boxed{\quad
[q_Y^n]T_7F
=\sigma_{47}(a_{7n})+7\,\mathbf1_{7\mid n}\,\sigma_7(a_{n/7}).
\quad}
\tag{865.15}
$$
在原 $\xi=\zeta_{41}$ 坐标中，$47\equiv6\pmod{41}$，所以第一项是 $\xi\mapsto\xi^6$，第二项是 $\xi\mapsto\xi^7$。不能把两个方向都写成7，也不能删去第一项的逆。

令 $\Pi_d$ 是 $1,\xi,\ldots,\xi^{39}$ 中的准确整矩阵。对每个原基项，先取 $e=dr\bmod41$；若 $e<40$ 则放到第 $e$ 位，若 $e=40$ 则使用
$$
\xi^{40}=-\sum_{j=0}^{39}\xi^j.
\tag{865.16}
$$
于是全部新操作都是旧完整40坐标的准确整数线性组合，不是在一个有限域根上抽样。

## 4. 原 −3 扭曲与真正的 Q 定义性

[R802](R802-original-semilinear-parity-and-degree-seven-relations.md)在同一参考尖点证明
$$
\varepsilon(c_YF)(q_Y)=c_0(\varepsilon(F))(-q_Y),
\qquad c_0(s)=-s,\quad c_0(\xi)=\xi.
\tag{865.17}
$$
它来自 (865.2) 的原 $-3$ 扭曲；几何 involution 是 $\tau\mapsto\tau+41$、$t_Y\mapsto1-t_Y$。循环7-isogeny对应与该 involution 交换：模2标记的换位可以同时运输到源和靶。因而标准对应准确下降为原 $Y/\mathbb Q$ 的对应。

(865.15) 也直接核对这点。因为7为奇数，$(-1)^{7n}=(-1)^n$，而 $7\mid n$ 时 $(-1)^{n/7}=(-1)^n$；两 $\sigma_d$ 都与 $c_0$ 交换。因此
$$
T_7c_Y=c_YT_7.
\tag{865.18}
$$
本篇选择7还保留 $\chi_{-3}(7)=1$，所以与 [R330](R330-actual-discriminant-double-cover-and-persistent-central-zero.md) 中原 $-3$ 扭曲的远处 Hecke 特征规范一致。没有用未扭曲曲线替代原 $Y$，也没有把 mod2 sign 部分丢掉。

该对应的转置仍是自身。事实上，矩阵 $A$ 的对偶7-isogeny由 $7A^{-1}=\operatorname{adj}(A)$ 表示，仍为整 determinant7 矩阵；mod82 的像是 $7\bar A^{-1}\in G$，行列式仍为7，故仍在同一 $H\bar g_7$ 中。标量7已经属于原 $G$，所以没有遗漏 diamond 因子。于是 $T_7$ 是原 Jacobian 上的积分、Rosati 对称的实际对应。

## 5. 十三阶全局注入与准确矩阵恢复

[R778](R778-original-cusp-orbit-and-short-exact-recovery.md)已证明原二十尖点在 $Y_L$ 上单轨道，因此在较小的 $Y_K$ 上也单轨道。原 $\deg K_Y=252$。若一个 $K$ 定义全纯微分
$$
\omega=82F\,dq_Y/q_Y
$$
在参考 cusp 的 $a_1,\ldots,a_{13}$ 全部为零，则 $F$ 的阶至少14，$\omega$ 的零阶至少13。该零阶在全部二十个尖点相同。若 $\omega\ne0$，就有 $\deg(\omega)_0\ge260>252$，矛盾。因此
$$
\omega\longmapsto(a_{n,r})_{1\le n\le13,\ 0\le r<40}
\tag{865.19}
$$
在原127维全纯空间上单射。这里必须保留完整 $K(\xi)$ 系数；一个特征值代入不构成 (865.19)。

取已成 R866 的 $\mathsf H\in\mathbb Q^{560\times127}$，其第0至39行为真实零。令 $J\subset\{40,\ldots,559\}$ 是 R866 实际选出的127行，$U=\mathsf H_J^{-1}$ 是其已认证准确逆。本篇不再次选行或求逆。令 $\mathsf K\in\mathbb Q^{560\times127}$ 的 $q^0$ 行为零，其余行按 (865.15) 生成。定义
$$
\boxed{\quad M_7=U\mathsf K_J.\quad}
\tag{865.20}
$$
矩阵约定是 $T_7F_j=\sum_i F_i(M_7)_{ij}$。其准确成功出口是
$$
\mathsf H M_7=\mathsf K
\quad\text{全部 }560\times127\text{ 原坐标相等}.
\tag{865.21}
$$
由于 $T_7F_j$ 是已证明的原全纯微分，(865.19) 使 (865.21) 等价于全局 Hecke 等式。不能仅检验选中127行。

实际上这些坐标在 $\mathbb Q$ 中：$G$ 半线性固定形式构成标准 $\mathbb Q$ 模形式结构，$B$ 有理且 $T_7$ 保留它。也可由 $T_7F_j$ 的 $K$ 坐标、全部 Fourier 系数在 $\mathbb Q(\xi)$ 中及 $K\cap\mathbb Q(\xi)=\mathbb Q$ 推出。这个矩阵有理性不把 $\omega_j$ 误称原 $c_Y$ 固定基；转换到真正 $\mathbb Q$ 微分基时必须读取 R866 的实际固定基矩阵 $P$，使用 $P^{-1}M_7P$ 并保留其 $s$ 分量终验。

对于 (865.21)，目标 $n$ 最大为13，故原输入最大指数仅为 $7\cdot13=91$。所有原权二行已有 $n\le128$；不存在新的 Fourier 生成任务。

## 6. 有限谱信息能给什么

一旦 (865.21) 实际完成，可计算真正的 $\chi_7(X)=\det(XI-M_7)$。原对应是积分 Jacobian 自同态，其在 Betti 同调上的特征值是代数整数；$M_7$ 又有理，所以 $\chi_7\in\mathbb Z[X]$。Rosati 对称性使 $T_7$ 在正定极化 Hermitian 结构中可对角化。因此它的最小多项式正是 $\chi_7$ 的不同不可约因子之积，不含重因子。

若实际分解为 $\chi_7=\prod_i f_i^{m_i}$，令 $m_7=\prod_i f_i$。准确 Bézout/CRT 给多项式 $e_i(X)$，满足 $e_i\equiv1\bmod f_i$、$e_i\equiv0\bmod f_j$（$j\ne i$）。于是 $e_i(T_7)$ 是原 $\operatorname{End}^0(J_Y)$ 中相互正交的真实谱投影。将实际有理系数统一清分母，可给每个谱投影的一个真实整数对应倍数。这是由原有限 $T_7$ 对应的复合得到，不需要声称已经物化所有纤维积方程。

这些只按单个 $T_7$ 分谱。同一因子中仍可能有多个真正 Hecke 等型分量；也没有判断原 modified-diagonal 类 $\eta$ 在哪些投影下非零。没有该类的实际投影/消灭证书，就不能把某个 $e_i(T_7)$ 命名为 YP 的 $e_\eta$，不能填原 $d,N$，也不能把非 $p$ 各项分别置零。

## 7. 最小公开消费与恢复契约

首个消费者只需三条真实源链：R864 的完整127基；R866 已成的同基 $\mathsf H,J,U$、必要配置与源索引；旧 R786 的146条 $n\le128$ 原行（可从 R866 载体原样续传）。源的 run/artifact/configuration 与逐文件 bytes/SHA 仅在实际发布后填入；R866 未完成时请求保持 pending。

新算术分为：固定双陪集及 $\Pi_6/\Pi_7$ 的小准确证书；逐目标列的 (865.15) 完整目标块；使用旧 $U$ 的127个准确坐标列；(865.21) 全部乘回；然后按已约定首 scope 求特征多项式及其准确谱数据。每个完成块原子保存，只有同 source/tag 续接可以恢复。不能将复制旧 $\mathsf H$ 或旧 $U$ 登记为新矩阵求解。

新 tag 明确绑定原 $G,H,\Gamma$、右作用、八个矩阵、$q_Y$、$\Pi_6/\Pi_7$、已含 $82^2$ 的原截面尺度、(865.4) 的82微分尺度、原 R864 基、R866 逆及全部旧源行。预算和完成列游标不改变数学身份。所有新算术只在本公开仓库 Actions；本篇撰写未执行本地数学。

后继成功证书至少分开声明：原 $T_7$ 全矩阵/谱证书是否实际完成；真实 $\mathbb Q$ 基转换是否消费；单算子谱投影是否输出；完整 Hecke 等型分解、$e_\eta$、torsion-clearing $N$、principal 校正函数、非 $p$ 支持数值和高度均仍未完成。这样下一项能沿真实算子继续，而不再停在抽象“存在某个 Hecke 对应”的入口。

## 原规范文献

- D. Zywina, [Explicit open images for elliptic curves over Q](https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf), Lemmas4.3、4.5：原 GL2 右半线性作用及下降。
- D. Zywina, [Computing actions on cusp forms](https://davidzywina.github.io/papers/AtkinLehner/AtkinLehner.pdf), §1.1：$\det(A)^{k/2}$ 的 slash 规范。
- 原 R771/R775/R778/R802/R864 及同源 R866 完成产物：原群、参数、扭曲、尖点和共享短逆的来源；不得以另一个曲线的 Hecke 表替代。
