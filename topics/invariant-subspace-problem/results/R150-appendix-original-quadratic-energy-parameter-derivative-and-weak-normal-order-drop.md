# R150 补篇：原二次能量及真参数导数的十七式来源，与唯一弱正常方向的一次降阶

日期：2026-11-15。作者：Astra-ISP-789f / literature_audit；AI 辅助：GPT-6 Astra Pro。

## 1. 两个不需要对理想求导的原来源恒等式

始终使用原 $K,J_2,J_3$ 和原 Hankel 二阶变量 $M$。令
$$
y=v(s),\qquad u=v'(s),\qquad p=Ky,\qquad r=Ku,
$$
$$
Y=yy^{\mathsf T},\qquad T=yu^{\mathsf T}+uy^{\mathsf T}.
$$
对二阶矩阵使用原配对
$$
\langle X,Z\rangle_K=\operatorname{tr}(KXKZ).
$$
若两者为 Hankel，该配对的坐标矩阵正是 $J_2$。以下所有导数首先保持原 $M$ 固定，而非保持随参数移动的正常坐标固定。

沿用[原完整中心归约](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md)，写
$$
L=\mathcal L_y(M),\qquad A_yM=L_p,\qquad
Q_y(M)=\langle M,A_yM\rangle_K.
$$
全部原方程为十一条 $N$ 的极线系数和六条 $\Gamma$ 坐标，其中
$$
N=4MKM+6A_yM,
$$
$$
\Gamma=2\operatorname{tr}((KM)^2)y
+8MKMp-12L:(KMK).
\tag{1.1}
$$

两个精确恒等式是
$$
\boxed{12Q_y(M)=2\langle N,Y\rangle_K-p^{\mathsf T}\Gamma,}
\tag{1.2}
$$
$$
\boxed{
6\left.\frac{\partial Q_{v(s)}(M)}{\partial s}\right|_{M\ {\rm fixed}}
=\langle N,T\rangle_K-r^{\mathsf T}\Gamma.}
\tag{1.3}
$$
因此 $Q_y$ 与这个真参数导数都属于原十七式的多项式参数线性包，所用的 $M$ 来源乘子次数为零。式 (1.3) 不是把一个已知理想成员随参数求导后，假定导数仍在理想中。

若记十一条原极线系数为
$$
n_i(s,M)=[z^i]\,v(z)^{\mathsf T}KNKv(z),\qquad 0\le i\le10,
$$
则这两个来源完全显式：
$$
12Q_y=2\sum_{i=0}^{10}s^i n_i-\sum_{\ell=0}^5p_\ell\Gamma_\ell,
\tag{1.4}
$$
$$
6\partial_s Q_y
=\sum_{i=1}^{10}i s^{i-1}n_i-\sum_{\ell=0}^5r_\ell\Gamma_\ell.
\tag{1.5}
$$
这里对 $n_i$ 取的是极线变量 $z$ 的值或一阶导数，不是对其参数系数求导。原固定清分母及 primitive 常数比例只改变 (1.4)–(1.5) 的非零有理常数；没有增加 $M$ 乘子次数。参数系数次数分别至多十和九。

## 2. 对第一条恒等式的逐项证明

原曲线的二次极式恒零，故
$$
y^{\mathsf T}Ky=y^{\mathsf T}Ku=0.
\tag{2.1}
$$
原物理恒等式还给
$$
A_yY=A_yT=0,
\tag{2.2}
$$
而
$$
J_2A_y=J_2B_p^{\mathsf T}J_3^{-1}B_pJ_2
$$
对称。于是
$$
\langle A_yM,Y\rangle_K
=\langle A_yM,T\rangle_K=0.
\tag{2.3}
$$

令 $c_M=p^{\mathsf T}MKMp$。式 (1.1) 给
$$
\langle N,Y\rangle_K=4c_M.
\tag{2.4}
$$
另一方面，向量 $\Gamma$ 与 $p$ 的配对中，第一项由 (2.1) 消失；最后一项严格为
$$
p^{\mathsf T}[L:(KMK)]
=L_p:(KMK)=\langle A_yM,M\rangle_K=Q_y(M).
$$
故
$$
p^{\mathsf T}\Gamma=8c_M-12Q_y(M).
\tag{2.5}
$$
将 (2.4)–(2.5) 相减即得 (1.2)。没有丢弃原 $N$ 的非 Hankel 二次项：它与物理 $Y$ 的配对恰由十一条原极线系数读出。

## 3. 真参数导数的逐项证明

映射 $\mathcal L_y$ 对 $y$ 线性，所以在固定原 $M$ 时
$$
\frac{d}{ds}\mathcal L_y(M)=\mathcal L_u(M).
$$
利用 $B_pJ_2M=J_3\mathcal L_y(M)$，有
$$
Q_y(M)
=(B_pJ_2M)^{\mathsf T}J_3^{-1}(B_pJ_2M).
$$
因此
$$
\partial_sQ_y(M)
=2(B_rJ_2M)^{\mathsf T}J_3^{-1}(B_pJ_2M)
=2L_r:(KMK).
\tag{3.1}
$$

设 $b_M=u^{\mathsf T}KMKMp$。由 (2.3)，
$$
\langle N,T\rangle_K=8b_M.
\tag{3.2}
$$
而原全部 $\Gamma$ 坐标给
$$
r^{\mathsf T}\Gamma
=8b_M-12L_r:(KMK);
\tag{3.3}
$$
其中含 $\operatorname{tr}((KM)^2)$ 的项由 $u^{\mathsf T}Ky=0$ 精确消失。

联立 (3.1)–(3.3) 得
$$
\langle N,T\rangle_K-r^{\mathsf T}\Gamma
=12L_r:(KMK)=6\partial_sQ_y(M),
$$
即 (1.3)。这条证明在每个有限参数上同时成立，包括 $s=2$ 和线性退化点；不需要 $A_y$ 的逆。

## 4. 唯一弱正常方向的真实降一阶系数

[原线性确定因子](R150-appendix-exact-characteristic-zero-linear-divisor-and-minimal-inverse.md)已经证明
$$
D_{\rm lin}
=s^8(s-2)^2(s+6)^2F_+^3F_-^3E_8^2.
\tag{4.1}
$$
在每个根处，正常九维对称块只降一秩，八阶子式中有局部单位。因此该点唯一的正线性 Smith 指数恰为相应的 $D_{\rm lin}$ 重数。

令 $s=\theta+t$，在特征零根域的 $R=\mathbb Q(\theta)[[t]]$ 中讨论。原两个切向列可用行列式为一的多项式补空间分开。正常对称九阶块有一个可逆八阶子块；对它作完整 Schur 后，局部单位合同将二次型写为
$$
Q_y(M)=x^{\mathsf T}U(t)x+t^a\varepsilon(t)z^2,
\qquad
U(t)\in\mathrm{GL}_8(R),\quad \varepsilon(0)\ne0.
\tag{4.2}
$$
这里 $a$ 是唯一正线性指数。合同保留整个原配对；并未把某个普通头子式当作全域逆。

令 $\zeta(t)$ 是 (4.2) 中弱坐标 $z$ 对应的真实原 $M$ 列，记
$$
H(t)=J_2A_{v(\theta+t)}.
$$
合同消元给出
$$
\zeta(t)^{\mathsf T}H(t)\zeta(t)=t^a\varepsilon(t),
\qquad H(t)\zeta(t)=t^a w(t)
\tag{4.3}
$$
对某个完整原列 $w(t)$ 成立。第二式在全部十一行成立：两个切向行由原核恒等式消失，其余九行是同一真实 Schur。

对 (4.3) 求导后，只在这一有限矩阵恒等式中使用乘法法则：
$$
\zeta^{\mathsf T}H'\zeta
=a t^{a-1}\varepsilon(t)+t^a\varepsilon'(t)
-2\zeta'^{\mathsf T}H\zeta.
$$
由第二个 (4.3)，最后一项属于 $t^aR$，因此
$$
\boxed{
\zeta(t)^{\mathsf T}H'(t)\zeta(t)
=a\varepsilon(0)t^{a-1}+O(t^a).}
\tag{4.4}
$$
特征零下 $a\varepsilon(0)\ne0$。所以原来源二次式 $\partial_sQ_y$ 在这个弱原列上的系数，准确比一般线性逆的唯一正指数低一阶。

特别地，在 $s=2$ 有 $a=2$，从而存在真实弱列 $\zeta(t)$ 使
$$
\left.(\partial_sQ_y)(z\zeta(t))\right|_{s=2+t}
=t\,\eta(t)z^2,\qquad \eta(0)\ne0.
\tag{4.5}
$$
在 $F_\pm$ 的根处对应指数为二，在 $E_8$ 的根处对应指数为一。这与已经分别支付的局部目标因子量级相容，但本节不是那些完整目标来源的替代证明。

式 (4.5) 只是原二次式在一个真实弱列上的限制。原二次式仍有可逆正常方向的平方项和交叉项，原方程仍有正常三次反馈。未经联合消去这些项，不能将 (4.5) 升级为 $t z^2$、更不能将九个原 $t\,n_j^2$ 都宣布属于原来源像。

## 5. 共动坐标下不能省去的三次项

令原 $M=\mathcal T(s)n$，其中 $\mathcal T(s)$ 为完整二项式 moment 变换，记
$$
\dot M=\mathcal T'(s)n,\qquad
\widehat Q(s,n)=Q_{v(s)}(\mathcal T(s)n).
$$
链式法则准确给
$$
\partial_s\widehat Q
=(\partial_sQ_y)(M)+2\langle A_yM,\dot M\rangle_K.
$$
使用原 $N=4MKM+6A_yM$，得到
$$
\boxed{
\partial_s\widehat Q
=(\partial_sQ_y)(M)
+\frac13\langle N,\dot M\rangle_K
-\frac43\langle MKM,\dot M\rangle_K.}
\tag{5.1}
$$
其中 $\dot M$ 仍为物理 Hankel 二阶矩阵，且对 $M$ 线性，故中间一项是合法的一次 $M$ 来源乘子。最后一项是完整三次多项式
$$
\operatorname{tr}(KMKMK\dot M).
$$
本篇没有证明它可免费删掉。尤其不能把共动正常 Gram 的裸导数直接替代 (1.3) 的固定原 $M$ 导数，或由线性 Smith 的 (4.4) 忽略其他正常项。

这给出目前 $s=2$ 一次目标费用的准确解析接口：原十七式确已提供一个弱方向系数恰为一次的二次式，且其来源完全明确；剩余工作是对九个真实平方同时支付其余二次项和 (5.1) 的三次反馈。与此同时，原定向 left2 入口只在实际完整原乘回且非零目标配对后才可宣布障碍，零读数不替代这项来源工作。
