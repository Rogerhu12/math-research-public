# R150：秩一截面的九平方来源、匹配 Bell 十六次幂与全局 Jacobian 边界

日期：2026-11-15 UTC。作者：Astra-ISP-789f / normal_annihilator；AI-assisted（GPT-6 Astra Pro）。

状态：原方程上的代数推论及明确来源公式。本文不把尚未确定的外部乘子写成常数，不把秩一均值截面的理想换成全部十七变量的 Jacobian 理想，也不把标量参数分母当作实际算子有界逆。没有新运行矩阵计算。

## 1. 原方程、截面及真正 Bell 余式

令 $\mathcal J=(\nabla R_3)\subset\mathbb C[y_0,\ldots,y_5,H_0,\ldots,H_{10}]$，其中 $R_3$、原矩阵 $K$、$J_3$ 和匹配余式 $B_r$ 始终取自[完整第三矩 Schur 归约](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)。特别地
$$
B_r(y,H)=(r\cdot y)^3-6(r\cdot y)r^{\mathsf T}Hr
-c(r)^{\mathsf T}J_3^{-1}\ell(y,H).
\tag{1.1}
$$
这里 $c_m(r)=\sum_{i+j+k=m}r_i r_j r_k$。$B_r$ 是权三的完整余式，并非裸 first 的立方。

现在只取归一化的秩一均值截面
$$
y=v(s)=(1,s,\ldots,s^5),\qquad H=M+\frac12y^2.
$$
令 $I\subset k[s,m_0,\ldots,m_{10}]$ 为原十七条方程生成的理想；$k$ 可以取 $\mathbb Q$ 加入固定 $r$ 的坐标，也可以将这些坐标暂作独立参数。十七条方程是
$$
[v(z)^{\mathsf T}K(4MKM+6A_yM)Kv(z)]_{z^i},\quad 0\le i\le10,
$$
以及
$$
\Gamma=2\operatorname{tr}((KM)^2)y+8MKMKy-12L_y(M):(KMK)
$$
的六个原坐标。所有固定非零有理行比例均可还原；没有将十一条极线方程加强为完整矩阵等式。

[原中心归约](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md)已逐项证明
$$
L_y=J_3^{-1}B_yJ_2,\quad
V=\frac32L_y(M)+\frac12y^3,\quad
T_3=6(L_y(M)-yM).
\tag{1.2}
$$
因此 (1.1) 在本截面上的拉回恰为
$$
b_r(s,M):=B_r\!\left(v(s),M+\frac12v(s)^2\right)
=6(L_y(M)-yM)(r,r,r).
\tag{1.3}
$$
此式在整个参数环中成立，不需要先模去 $I$。

采用原共动多项式单位变换
$$
m_i=\sum_{j=0}^{i}\binom ij s^{i-j}z_j.
$$
$L_y-y(\cdot)$ 的核恰为 $z_0,z_1$ 对应的物理切向二次空间。因此
$$
\boxed{b_r=\sum_{j=2}^{10}b_{r,j}(s)z_j.}
\tag{1.4}
$$
这些系数由同一个 $K,J_2,J_3^{-1}$ 直接确定；其分母只有固定非零有理数，没有引入参数极点。

## 2. 当前九平方来源的准确输入

使用同一归一化，记
$$
h_*=s^3F_+^2F_-^2E_8,\qquad q=sF_+F_-E_8.
\tag{2.1}
$$
三个因子的常数归一与已有 $h_*$ 一致。它们与 $s$ 两两互素；$E_8$ 无重根，两个三次的根也互异。因此 $q$ 无重因子，且
$$
\frac{q^3}{h_*}=F_+F_-E_8^2\in\mathbb Q[s].
\tag{2.2}
$$

令 $\mu(s)\ne0$ 是一个已有来源的共同乘子，假设九个原身份
$$
\mu h_*z_j^2=\sum_{\nu=1}^{17}C_{\nu j}(s,m)\mathcal F_\nu(s,m),
\qquad 2\le j\le10
\tag{2.3}
$$
成立。这里 $\mathcal F_\nu$ 是第1节的原方程。当前[外投影差长定理](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md)已经证明可取
$$
\mu=R_{\rm out}/\Omega.
$$
结合[完整系数五层与仿射界300](R150-appendix-root2-coefficient31-spectrum-through-five-and-affine-degree300.md)，有 $\deg\mu\le142-\deg\Omega$。这给出 (2.3) 的原多项式来源存在性，而未给出展开系数或 $\mu=1$。任何后续关于 $\Omega$ 或饱和缺陷 $J$ 的计算，仍须以其实际证明决定是否能令 $\mu$ 为常数。

若使用目前次数至多三的原来源模块，则可令每个 $C_{\nu j}$ 的 $m$ 次数至多三。以下构造会增加乘子的 $m$ 次数，所得结论属于普通多项式理想 $I$；它不再声称仍在原 $6188$ 列、次数至多三的截断模块中。

## 3. 九平方给出明确的十次来源

展开 (1.4) 的十次幂：
$$
b_r^{10}
=\sum_{|\alpha|=10}\binom{10}{\alpha}
\left(\prod_{j=2}^{10}b_{r,j}(s)^{\alpha_j}\right)z^\alpha.
$$
九个指数之和为十，每个这样的单项式至少有一个 $\alpha_j\ge2$。将该项指定给最小的此类 $j$，便确定九个多项式 $Q_j$，满足
$$
b_r^{10}=\sum_{j=2}^{10}Q_jz_j^2,\qquad \deg_mQ_j=8
\tag{3.1}
$$
（零项可略去）。这是一条确定的有限生成规则，不依赖解集或近似计算。

代入 (2.3)，得到
$$
\mu h_*b_r^{10}=\sum_\nu A_\nu\mathcal F_\nu,\qquad
A_\nu=\sum_{j=2}^{10}Q_jC_{\nu j}.
\tag{3.2}
$$
若原 $C_{\nu j}$ 的 $m$ 次数至多三，则 $\deg_mA_\nu\le11$。

本步没有将不同 $z_j$ 的混合二次项免费放进原截断像，也没有通过除以 $h_*$ 删除它的零点。

## 4. 四组已完成纤维消去已知参数因子

以下使用的是原固定纤维中整个 $W=(z_2,\ldots,z_{10})^2_{\le5}$ 属于原来源空间的结论，不只是局部参数长度或理想根式结论：

- [物理参数零](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md)第5节；
- [全部 $F_+$ 共轭均值](R150-appendix-rank-one-Pplus-means-complete-critical-classification.md)第4节；
- [全部 $F_-$ 共轭均值](R150-appendix-rank-one-Pminus-means-complete-critical-classification.md)第4节；
- [全部 $E_8$ 共轭均值](R150-appendix-rank-one-E8-means-complete-critical-classification.md)第5节。

由于 $b_r$ 是九个横向变量的一次式，$b_r^2\in W$。故对
$$
f\in\{s,F_+,F_-,E_8\}
$$
分别有
$$
b_r^2\in I+(f).
\tag{4.1}
$$
数域证书基变换到含 $r$ 的系数域后仍成立。所有共轭都已覆盖，不是在一个剩余根上猜测特征零归属。

四个参数多项式两两互素，所以商环 $(k[s,m]/I)$ 中的四个主理想仍两两互素；其交等于其积。由中国剩余定理，
$$
\boxed{b_r^2=\sum_{\nu=1}^{17}D_\nu\mathcal F_\nu+qE}
\tag{4.2}
$$
可在原多项式环中成立。其来源可从四个纤维的次数至多三系数逐系数作 CRT，再对 $q$ 精确除法获得。可以保 $\deg_mD_\nu\le3$ 和 $\deg_mE\le5$。原纤维中来源的存在及有限维有理解已付；本文没有声称这些四组系数刚被展开或运行。

## 5. 原秩一截面的十六次恒等式

置
$$
K_r=b_r^4+b_r^2qE+q^2E^2,\qquad R_q=q^3/h_*.
$$
由差立方恒等式，
$$
b_r^6-q^3E^3
=(b_r^2-qE)K_r
=\sum_\nu D_\nu K_r\mathcal F_\nu.
$$
乘上 $\mu b_r^{10}$ 并使用 (3.2)，得到完整原来源公式
$$
\boxed{
\mu b_r^{16}
=\sum_{\nu=1}^{17}
\left(R_qE^3A_\nu+\mu b_r^{10}K_rD_\nu\right)\mathcal F_\nu.
}
\tag{5.1}
$$
第一项使用 $R_qE^3(\mu h_*b_r^{10})$，没有将 $\mu$、$h_*$ 或某个参数值倒置。

在第2节的次数至多三原来源输入下，(5.1) 中的乘子 $m$ 次数至多二十六。这只是一个可复现的粗界；没有声称它最优，也没有将旧参数成本直接当作此新增高次数来源的成本。

因此已经得到两个分开的准确结论：

1. 对目前已证明存在的 $\mu=R_{\rm out}/\Omega$，有真实原理想成员性 $\mu b_r^{16}\in I$。
2. 若以后九个 $h_*z_j^2$ 自身的全局原来源得到证明，则可令 $\mu=1$，从而对每个固定 $r$ 有明确的自然代数幂
   $$
   b_r^{16}\in I.
   $$

第二条尚以九平方无额外乘子成员性为前提。它不是仅用 Nullstellensatz 得到一个未知幂次，而是给出保全部原生成元的具体合成公式。

## 6. 从此截面到全部 Jacobian 仍缺什么

(5.1) 的变量是 $s$ 和十一条 $M$ 系数。它是原完整临界系统在 $y=v(s)$ 上的拉回身份，不能把 $s$ 当作原六个独立 $y_i$ 中的一个坐标后直接删除其余秩一关系。

非零振幅 $y=a\,v(s)$ 由权重 $(1,2,3)$ 恢复；归一化包含 $M/a^2$，首先只给 $a\ne0$ 图上的原身份。无穷物理均值另由[完整无穷纤维](R150-appendix-rank-one-physical-mean-at-infinity-full-critical-emptiness.md)覆盖。$y=0$ 时 (1.1) 的 $B_r$ 本身恒零。

因此，若第5节第二条的前提成立，所有秩至多一的均值上的完整临界点都有 $B_r=0$。这可通过 Nullstellensatz给出
$$
B_r\in\sqrt{\mathcal J+\mathcal C_1},
\tag{6.1}
$$
其中 $\mathcal C_1$ 是物理有理正规曲线锥的均值关系理想。式 (6.1) 中必须保留 $\mathcal C_1$；它不等于 $B_r\in\sqrt{\mathcal J}$，也不将截面中的十六次指数自动下降为全原变量的同一指数。

[全部本质三次维数至多三的定理](R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md)已经使三个原匹配方向在那部分完整临界点上为零。若秩一分支闭合，剩余全局点值问题仍包括非秩一均值、$\operatorname{ess}(T_3)\ge4$ 的全部尚未覆盖分支。必须在它们上证明至少一个固定、已有实际逆的匹配 $B_r$ 全部消失，或直接构造其完整 Jacobian 恒等式。

若对一个固定 $r$ 真正证明了所有复临界点上 $B_r=0$，Hilbert Nullstellensatz 才给某个有限 $N$ 及多项式 $C_u$：
$$
B_r^N=\sum_u C_u\,\partial_uR_3.
\tag{6.2}
$$
这给有限原来源的存在性，但不会给本文的十六次指数、展开系数、系数高度或自然词费用。若需要可执行系数证书，应再恢复并逐原式核验 (6.2)；不能把有限域成员性、单个纤维的消失或只在局部环可逆的分母作为替代。

## 7. 已支付的真实 Bell 逆桥

原方向
$$
r=(A,B,0,0,0,1),\qquad A,B\in\mathbb R
$$
对应原 first $iA\,U_1+B\,U_2+U_6$。对已付方向，完整 ordinary Bell 立方 $S_r$ 的原最大闭实现有全空间有界交换逆；该结论保留全部 Bell 修正和自然域。

记完整第三矩消元变量为 $Z$。原 Schur 恒等式给
$$
S_r=B_r+4c(r)^{\mathsf T}Z,\qquad
(\nabla\mathcal Q_3)=(Z,\nabla R_3).
$$
只有在完整原变量中的 (6.2) 成立后，才可令
$$
T_N=\sum_{j=0}^{N-1}S_r^{N-1-j}B_r^j
$$
并使用已证明的原来源提升
$$
S_r^N=
\sum_u C_u\partial_u\mathcal Q_3+
\frac14\left(c(r)T_N-\sum_uC_u\partial_u\ell\right)^{\mathsf T}
J_3^{-1}\partial_V\mathcal Q_3.
\tag{7.1}
$$
于是[真实 Bell 逆分母定理](R150-appendix-jacobian-certificates-with-actual-bell-inverse-denominators.md)的有限来源与真实有界逆两个条件才同时具备。

这里 $S_r^N$ 是同一完整 Bell 算子的自然代数幂，不是 first 的第 $3N$ 次 ordinary Bell 多项式。$h_*(s)$、$\mu(s)$、均值图中的 $a$，以及任何局部 CRT 参数分母均未取得对应实际算子逆，不能将其倒数插入 (7.1)。

## 8. 原来源接口与完成范围

当前外投影计算处理的是原截断模块中的九平方。完成它能消去一个具体有限参数障碍，并在上述前提下给秩一截面的十六次原身份。其后仍需保全非秩一完整临界分支和同一固定 $r$ 的全局 Jacobian 归属，再由 (7.1) 接真实逆定理。

本文没有新增矩阵或数域运行；四纤维原证据、九平方输入和全部代数合成的角色已分别标出。不将这一推进记成原六模式 $F^3$、更高普通点态幂或普通 Hilbert 不变子空间问题的最终完成。
