# 原 c0 帧到指定 Poincaré 纤维与 theta 修正截面

日期：2026-11-16。状态：**本文给出原层41的一项新的准确代数构造；没有执行新数值计算。** 输入已经包括实际成功的五个全局极理想表达式与原 c0 的六个范数、五组首项。新的对象是具体的刚性化 Poincaré 纤维点、主函数运输标量，以及完整修正线丛的原基点归一截面。本文不把它们的表达式当作已经求出的规范 Poincaré 对数、第二类周期或高度。

只使用原 $X,Y,\phi,c_0,c_1,q,A,\lambda_A$。记
$$
P_0=\phi(c_0),\qquad P_1=\phi(c_1),\qquad t=a^3,
\qquad J=J_X,\quad \gamma=[c_1-c_0].
\tag{RF.1}
$$
原 $\beta=q\gamma\in A$ 与 $P_Y=[P_1-P_0]\in J_Y$ 是不同对象，本文不互换二者。原 $c_1$ 参数仍是 $a-1$，$t$ 是原 $Y$ 上在 $P_0$ 的参数；不把它改成 R806 的正规基底坐标。

## 1. 已完成的准确来源与固定约定

原 [R791](../results/R791-certified-original-Hom-descent-and-eta-inputs.md) 给
$f=f_4$、$g_j=(1+T^j)f$、$\alpha_3=1-\zeta^2$、$s=1+2\zeta$，
以及 $f_R=[\alpha_3]f$、$g_{R,j}=[\alpha_3]g_j$，其中
$\alpha_3^3=3s$。全部极化、$\kappa=qq^\dagger$、五个 $h_j$ 与原有理次数比保持不变。置
$$
(p_j,q_j)=(165,67),(93,67),(100,67),(168,67),(371,134),
\qquad \delta_j=p_j-q_j.
\tag{RF.2}
$$
这里 $q_j$ 是有理数分母，不是商同态 $q$。

[GP 的完整极理想公式](R839-original-global-addition-polar-ideals-and-eta-DAG.md)
已经由公开 run
[43790410670](https://github.com/Rogerhu12/math-research-public/actions/runs/43790410670)
的准确表达式消费者实现；源提交
391191590dcb8bcc6f8f2d777610726fa79dc2a3，
最终证书 SHA256
b50df2dfd37a7610659fa5f9bc37b81078ba6e95508c9196f1056bef1c9c60b7。
原 c0 数据由 run
[43790534424](https://github.com/Rogerhu12/math-research-public/actions/runs/43790534424)
取得；源提交
a576ab9d3b6d155027ec6f52cb689205ee5e9b98，
最终证书 SHA256
775a07af76479e2b891caae410677a49265df34c0df02d979e74d33be663e09a。
两个证书均真实完成；全局坐标没有因此被展开。正式来源分别为
[R849 原全局函数与五极理想 DAG](../results/R849-certified-original-global-function-and-five-polar-ideal-DAGs.md)及
[R848 原 c0 Hodge jets 与比较首项](../results/R848-certified-original-c0-Hodge-jets-and-comparison-leading-coefficients.md)。

记真七次范数为 $N=N_{L/K}$。原嵌入分式理想及实际主函数为
$$
\begin{aligned}
\mathfrak L_j
 &=N(I_{E_{g_j}})^{q_j}N(I_{E_f})^{-p_j}
   =\mathcal O_Y(-Z_j),\\
\mathfrak L_j^R
 &=\mathcal O_Y(-Z_j^R)
   =\mathcal R_j\,\mathfrak L_j^{\otimes3},\\
Z_j^R&=3Z_j+\operatorname{div}(\mathcal R_j),\\
\mathcal R_j
 &=N(y_{g_j}^2-b)^{q_j}/N(y_f^2-b)^{p_j}.
\end{aligned}
\tag{RF.3}
$$
这是正乘 $\mathcal R_j$，不是其逆。所有 $\sigma(b)$、$\rho_j$ 和目标缩放仍来自原来源。

[原 c0 首项证明](2026-11-16-original-c0-Hom-nonramification-and-comparison-leading-terms.md)
给
$$
\begin{gathered}
\operatorname{mult}_{P_0}Z_j
 =\operatorname{mult}_{P_0}Z_j^R=-7\delta_j,\\
\mathcal R_j
 =\kappa_jt^{14\delta_j}(1+d_jt+O(t^2)),\\
M_h=N(\lambda_h^3)=N(108W_h(0)),\qquad
\kappa_j=M_f^{2p_j}/M_{g_j}^{2q_j}.
\end{gathered}
\tag{RF.4}
$$
$\lambda_h$ 是原 $h^*(dx/(2y))/da$ 在 $c_0$ 的值。实际消费者保留整数幂 DAG，并没有任取平方根或立方根。

由 R843 的原点非挠及其全部原 Hom 值分离，$f,g_j,f_R,g_{R,j}$ 及其共轭在 $c_1$ 均不取 $O$。因此 $P_1$ 不在 (RF.3) 各极除子的支撑中，$\mathfrak L_j,\mathfrak L_j^R$ 在 $P_1$ 的嵌入局部理想都是 $\mathcal O_{Y,P_1}$，其帧 $1$ 真实非零。这里使用原映射的值；没有用一个非零 Hom 字替代尚未经证明的点分离。

## 2. 从嵌入理想到实际刚性化 Poincaré 点

对任一度零线丛 $\mathcal L/Y$，定义
$$
\operatorname{Rig}_{P_0}(\mathcal L)
 =\mathcal L\otimes_k\mathcal L(P_0)^{-1}.
\tag{RF.5}
$$
其在 $P_0$ 的刚性化由一维空间与其对偶的评价给出。这里 $k$ 可先取 $K$；原有理下降随后保持，不任换原定义域或取单一扩域地方代全局求和。

令 $i_Y(P)=[P-P_0]$，保持 R593 的符号
$i_Y^*\lambda_Y(\xi)=-\xi$。设实际整点
$$
\xi_j=[Z_j],\qquad \xi_j^R=[Z_j^R]=3\xi_j
\quad\text{于 }J_Y(K).
\tag{RF.6}
$$
最后一个等式由 (RF.3) 的真实主除子成立，不仅在 $J_Y\otimes\mathbf Q$ 中成立。原 $\eta_{h_j}=\xi_j/q_j$ 的等式仍在原有理点空间中解释；此处没有选择一个未知的 $q_j$-除点。

R18 的基点刚性化泛性质，在本实际理想上给唯一同构
$$
\operatorname{Rig}_{P_0}(\mathfrak L_j)
 \simeq
(i_Y,\lambda_Y\xi_j)^*\mathcal P_Y,
\qquad
\operatorname{Rig}_{P_0}(\mathfrak L_j^R)
 \simeq
(i_Y,\lambda_Y\xi_j^R)^*\mathcal P_Y.
\tag{RF.7}
$$
这不是重新证明 R18 的一般接口；新的输入是已经给出的原完整嵌入理想及以下指定帧。

由 (RF.4)，取
$$
e_j=t^{-7\delta_j}\in(\mathfrak L_j)_{P_0},
\qquad
e_j^R=t^{-7\delta_j}\in(\mathfrak L_j^R)_{P_0}.
\tag{RF.8}
$$
它们在相应一维纤维中的类是真实非零向量。负幂是局部可逆模的生成元，不能将它当作一个“在 $P_0$ 无穷大、不可求值”的普通函数值。

在 $P_1$ 以帧 $1$ 定义
$$
\boxed{
v_j=1(P_1)\otimes e_j(P_0)^{-1},\qquad
v_j^R=1(P_1)\otimes e_j^R(P_0)^{-1}.}
\tag{RF.9}
$$
它们分别是实际非零 Poincaré 纤维
$\mathcal P_Y(P_Y,\lambda_Y\xi_j)$ 与
$\mathcal P_Y(P_Y,\lambda_Y\xi_j^R)$ 中的向量。
这个定义不需要先给 $\xi_j$ 一个标准 Jacobian 坐标，也不需要将闭点分裂或求主理想生成元。原两图理想及局部纤维商已经给出它们的有限准确表示。

以下也以 $v_j(P),v_j^R(P)$ 表示相同的有理截面
$1/e_j(P_0)$、$1/e_j^R(P_0)$；写在 $X$ 上时均沿原 $\phi$ 拉回。在 $P_1$ 的值才是 (RF.9) 的两个纤维点。

若以后需对一般度零除子 $\sum n_QQ$ 取纤维，可直接用
$\bigotimes_Q\operatorname{Nm}_{k(Q)/k}\mathcal L(Q)^{n_Q}$；
线丛同构的主函数运输仍按 R18 的范数规则保留。此处 $P_1-P_0$ 的两个点均为原有理点，没有新增支撑移动。

## 3. 三次同源的原纤维比较恰为 κ/R

乘 $\mathcal R_j$ 给真实同构
$$
m_{\mathcal R_j}:\mathfrak L_j^{\otimes3}
\longrightarrow\mathfrak L_j^R.
\tag{RF.10}
$$
在 $P_0$ 的帧 $e_j^{\otimes3}=t^{-21\delta_j}$、
$e_j^R=t^{-7\delta_j}$ 中，此同构的纤维标量是 $\kappa_j$。
在 $P_1$ 两边帧 $1$ 中，它的标量是 $\mathcal R_j(P_1)$。
因此对 (RF.5) 作同一同构，准确得到
$$
\operatorname{Rig}(m_{\mathcal R_j})
 \bigl(v_j^{\otimes3}\bigr)
=\frac{\mathcal R_j(P_1)}{\kappa_j}\,v_j^R.
\tag{RF.11}
$$

在 (RF.6) 对应的 Poincaré 双线性同构下，第一变量固定为 $P_Y$，第二变量从 $\lambda_Y\xi_j$ 变为 $3\lambda_Y\xi_j$。于是
$$
\boxed{
v_j^R=\frac{\kappa_j}{\mathcal R_j(P_1)}
       \,v_j^{\otimes3}.}
\tag{RF.12}
$$
右边的张量立方只在**第二个 Picard 槽**中取和。它不是固定扩张
$\mathcal P_{Y,\lambda_Y\xi_j}^{\times}$ 内的群乘三；后者还会把基底 $P_Y$ 改为 $3P_Y$。

对于同一个原地方 $\chi_v$-splitting，
$$
\tau_{Y,v}(v_j^R)
 =3\tau_{Y,v}(v_j)
  +\chi_v\!\left(\frac{\kappa_j}{\mathcal R_j(P_1)}\right).
\tag{RF.13}
$$
原 $c_1$ 盘内的代数比较标量对数导数为
$-\mathcal R_j'/\mathcal R_j$。R847 的五个导数非零只是这一标量的真实性质，不删去 (RF.13) 的共同 Poincaré 项。

**参数幂不能误删。** $P_0$ 处的形式单位是
$\mathcal R_j/(\kappa_jt^{14\delta_j})$。它用于记录 (RF.10) 在两个不同单项式帧中的单位，不是可任意替代全局同构的标量。
真正的刚性化运输是 (RF.11)。将形式单位直接拿到 $P_1$ 使用会额外引入 $t^{-14\delta_j}$；即便原 $t(P_1)=1$ 使其点值偶然相同，对 $t$ 的对数导数仍会多出 $-14\delta_j$。

## 4. 完整修正消除 theta 代表差，而非删除其 Picard 因子

先记录本次所需的精确代数事实。令 $i_X:X\to J$ 是原 Abel 映射。对 $J$ 上沿 $0$ 刚性化、且 $\deg i_X^*\mathcal S=0$ 的真实线丛，置
$$
k_{\mathcal S}=[i_X^*\mathcal S]\in J,\qquad
\operatorname{Corr}(\mathcal S)
=\mathcal S\otimes\mathcal P_{J,\lambda_Jk_{\mathcal S}}.
\tag{RF.14}
$$
由于 $i_X^*\lambda_J=-\mathrm{id}$，其曲线拉回是次数零平凡线丛；沿 $c_0$ 取值 $1$ 确定唯一无零截面。

若 $\mathcal S'=\mathcal S\otimes\mathcal M$，其中 $\mathcal M\in\operatorname{Pic}^0(J)$ 也沿 $0$ 刚性化，则
$$
k_{\mathcal S'}=k_{\mathcal S}+i_X^*\mathcal M,\qquad
\lambda_J(i_X^*\mathcal M)=-\mathcal M.
\tag{RF.15}
$$
Poincaré 的实际张量同构遂给
$\operatorname{Corr}(\mathcal S')\simeq\operatorname{Corr}(\mathcal S)$，保持原点刚性化及曲线归一截面。$\mathcal M$ 在对称部分与其**伴随 Picard 修正**中相消，不能只删第一个因子。

等价地，两个实际线丛若有相同 NS 类、曲线拉回均真实平凡且沿 $0$ 刚性化，则存在唯一保持刚性化的同构。其差在 $\operatorname{Pic}^0(J)$；Abel 拉回
$i_X^*:\operatorname{Pic}^0(J)\to\operatorname{Pic}^0(X)$ 是同构，故该差为零。几何连通射影 $J$ 上线丛自同构是常数，原点条件给唯一性。

这正保留原指定 theta 的问题：两个刚性化对称代表若给同一 $\lambda$，其差是 Picard 二挠。它在 (RF.15) 中有一个必须一起运输的反因子。也可使用原
$$
\mathcal S^{\otimes2}\simeq(1,\lambda_{\mathcal S})^*\mathcal P_J
\tag{RF.16}
$$
对整个 tensor 表示取同一偶倍后比较。不能将完整修正作 $[-1]$ 对称化，那会删去原 $\eta$ 项。

(RF.14) 的一般思想与 R14/R148 相同；以下构造是它在现在已经给出的原 Hom、极理想、Poincaré 帧上的实际实现。

## 5. 由原 Hom 构造对称源及其三次拉回

原 $q_R=vq:J\to B$ 与 $G_j=(1+T^j)q_R$ 来自 R791。先在 $K$ 上定义实际对称源
$$
\mathcal S_j
=G_j^*(\Theta_B^{\mathrm{ell}})^{\otimes q_j}
 \otimes q_R^*(\Theta_B^{\mathrm{ell}})^{\otimes(-p_j)}.
\tag{RF.17}
$$
这里 $\Theta_B^{\mathrm{ell}}$ 使用 R728 的七个原椭圆分量上
$\mathcal O_C(O)$ 的外积；各原点帧明确选为
$\xi^{-1}$，$\xi=-x/y$。如原指定 $\Theta_B$ 的对称代表与此相差二挠，该差按 §4 与完整修正一起运输，未默认为同一未标记 theta。

原 R791 次数表、极化伴随和 $h_j$ 给
$$
\deg i_X^*\mathcal S_j=0,\qquad
[\mathcal S_j]_{\rm NS}
=q_j[q^*\mathcal L_{h_j}]_{\rm NS}.
\tag{RF.18}
$$
这里保留 $v^\dagger v$ 与原 $\kappa$；不把 $\Theta_B$ 的乘积极化冒充原 $A$ 的极化。

令 $u_j$ 是 (RF.17) 各 $\mathcal O(O)$ 的原有理截面 $1$ 的 tensor 乘积。其沿曲线的除子为
$$
D_j^S
=q_j\sum_\tau g_{R,j,\tau}^*[O]
-p_j\sum_\tau f_{R,\tau}^*[O].
\tag{RF.19}
$$
R791 的完整重数恒等式逐项给
$$
3D_j^S=\phi^*Z_j^R,\qquad
\phi_*D_j^S=Z_j^R.
\tag{RF.20}
$$
这同时指定 $\mathcal S_j^{\otimes3}$ 曲线拉回与
$\phi^*(\mathfrak L_j^R)^{-1}$ 的实际 Cartier 同构：两边的有理截面 $1$ 对应。不是只比较度数或 Picard 有理类。

Jacobian 范数及拉回的原对偶关系给
$$
\operatorname{Corr}(\mathcal S_j)^{\otimes3}
\simeq
\mathcal S_j^{\otimes3}
\otimes\phi_*^*\mathcal P_{Y,\lambda_Y\xi_j^R}.
\tag{RF.21}
$$
因此沿 $X$，(RF.20) 与 (RF.7) 将右边两个实际线丛相消；余下的固定一维纤维由原 $c_0$ 刚性化确定。

若某一中间 $K$-表示不是原始的 $\mathbf Q$ tensor 表示，则保持上述完整线丛及同构下降。其 NS 类和原曲线平凡化均为原有理数据；§4 的唯一性使 Galois 下降 cocycle 自动相容。这个论证没有把单个非实 $g_j$ 称为实下降映射。

本应用还能将下面的地方求值全部留在真实 $\mathbf Q$ 纤维中。
原复共轭关系给
$c(g_{R,j})=T^{-j}g_{R,j}$、$c(f_R)=f_R$。
$T$ 的七个分量是置换与原目标缩放，故保持七个 $[O]$ 之和作为 Cartier 除子。
因此 (RF.17) 的 Cartier 表示及有理截面 $u_j$ 不变。
在原椭圆参数帧上，$T^*\bigotimes_\tau\xi_\tau^{-1}
=(N\rho)^{-1}\bigotimes_\tau\xi_\tau^{-1}$。
R791 的实际 $T^7=[\zeta^2]$ 在非零原 Hom 上给 $N\rho=\zeta^2$；
所以三次帧的共轭比较为 $1$。
这准确给出 $\mathcal S_j^{\otimes3},u_j^{\otimes3}$ 的原点刚性化 $\mathbf Q$ 下降。
同样，$c(g_j)=-[\zeta^2]T^{-j}g_j$ 使七项极除子和不变，
故 $\mathfrak L_j,\mathfrak L_j^R$ 及其原有理参数帧均在 $\mathbf Q$ 上下降。
这里没有将非实映射本身下降，只下降所需的完整 divisor/tensor 对象。

## 6. c0 数据给出原 theta 截面的完整归一常数

沿原参数 $a$，原 c0 结果给
$$
\xi_h(a)=\lambda_h a+\frac{\mu_h}{4}a^4+O(a^7),
\qquad
\frac{\mu_h}{\lambda_h}=\frac{W_h'(0)}{3W_h(0)}.
\tag{RF.22}
$$
$[\alpha_3]^*\omega_C=\alpha_3\omega_C$，所以
$\lambda_{h_R}=\alpha_3\lambda_h$、
$\mu_{h_R}=\alpha_3\mu_h$。在 (RF.17) 的原椭圆参数帧 $e_j^S$ 中，
$$
u_j(a)=\Xi_j(a)e_j^S(a),\qquad
\Xi_j(a)=
\prod_\tau
\frac{\xi_{g_{R,j,\tau}}(a)^{q_j}}
     {\xi_{f_{R,\tau}}(a)^{p_j}}.
\tag{RF.23}
$$
各 $e_j^S(0)$ 在该源的原点刚性化中都是 $1$。

定义非零的准确标量
$$
\boxed{
\nu_j
=\frac{N(\lambda_{f_R}^3)^{p_j}}
       {N(\lambda_{g_{R,j}}^3)^{q_j}}
=(3s)^{7\delta_j}\frac{M_f^{p_j}}{M_{g_j}^{q_j}}.}
\tag{RF.24}
$$
这是读取已成六个 $M_h$ 后的整数幂表达式；没有使用
$\sqrt{\kappa_j}$，也没有删除 $\alpha_3^3=3s$ 的标度。
从 (RF.22) 逐项取原 tensor 乘积得到
$$
\Xi_j(a)^3
=\nu_j^{-1}t^{-7\delta_j}
 \left(1-\frac{d_j}{2}t+O(t^2)\right).
\tag{RF.25}
$$
确切地，一次系数是
$\frac14(q_j\operatorname{Tr}(W_{g_j}'/W_{g_j})
-p_j\operatorname{Tr}(W_f'/W_f))=-d_j/2$。

沿曲线的 Picard 帧
$\widetilde e_j^R=t^{-7\delta_j}/e_j^R(P_0)$ 在 $c_0$ 是单位刚性化，且
$v_j^R=t^{7\delta_j}\widetilde e_j^R$。
所以 $u_j^{\otimes3}\otimes v_j^R$ 在 $c_0$ 的纤维值恰为
$\nu_j^{-1}$。完整归一截面由此是
$$
\boxed{
s_j^{(3)}
=\nu_j\,u_j^{\otimes3}\otimes v_j^R
=\frac{\nu_j\kappa_j}{\mathcal R_j}\,
  u_j^{\otimes3}\otimes v_j^{\otimes3}.}
\tag{RF.26}
$$
这里第二式使用 (RF.12) 的指定 Poincaré tensor 同构。两个表达式是同一个无零截面，且 $s_j^{(3)}(c_0)=1$；第一式在每个点的精确含义由 (RF.20) 的 Cartier 相消给出。

在 $e_j^{S\,\otimes3}\otimes\widetilde e_j^R$ 这个明确的代数乘积帧中，(RF.25) 给 $s_j^{(3)}$ 的首单位项
$1-\frac12d_jt+O(t^2)$。
若改在较小理想的三次 Picard 帧中，则规范帧比较本身为
$1+d_jt+O(t^2)$，截面系数相应为
$1-\frac32d_jt+O(t^2)$。两帧在 $c_0$ 的值相同，第一 jet 不同；这不是可以删掉的常数差，也不是规范高度的第一 jet。

实际 c0 输出还逐项记录 $M_h=s\,m_h$，$m_h\in\mathbf Q^\times$。
因此 (RF.24) 可不经扩域取根地写成
$$
N(\lambda_{h_R}^3)=3^{11}m_h,\qquad
\nu_j=3^{11\delta_j}\frac{m_f^{p_j}}{m_{g_j}^{q_j}},
\qquad
\kappa_j=(-3)^{\delta_j}
 \left(\frac{m_f^{p_j}}{m_{g_j}^{q_j}}\right)^2.
\tag{RF.27}
$$
这些式子是源中纯 $s$ 坐标与 $s^2=-3$ 的代数化简；本文没有展开任何大整数或执行新的范数计算。

## 7. 与原 N_h、C_h、指定 theta 和各地方高度的比较

保持 R593 的原实际 $\mathscr N_{h_j}$、无零截面 $s_{h_j}$、
$c_{\rm clear},c_{\rm triv},C_{h_j}=c_{\rm clear}c_{\rm triv}$。
其曲线拉回真实平凡，且 $s_{h_j}(c_0)=1$。
由 (RF.18)，以下两个实际线丛有相同 NS 类：
$$
\mathscr N_{h_j}^{\otimes3q_j},
\qquad
\operatorname{Corr}(\mathcal S_j)^{\otimes3C_{h_j}}.
\tag{RF.28}
$$
它们的曲线拉回都真实平凡。§4 的唯一性给保持原点刚性化的同构，并将
$s_{h_j}^{\otimes3q_j}$ 准确送到
$(s_j^{(3)})^{\otimes C_{h_j}}$。
这保留原 $C_h$，而非另定一个高度。原完整 $\mu_3$ 范数及其整数倍已经计入原 $C_h$；此处的第三次幂来自 (RF.20)，不能再额外漏乘或补乘一次范数。

所有度量、$\chi$、Poincaré splittings 及第二类补空间仍取 R724 的原数据。
对称源只用原 (RF.16) 的 Poincaré 平方同构求值；不能为七个椭圆分量各自任选另一套高度。若借用椭圆代表，应按 R724 §6 拉回同一 $J_X$ Poincaré 曲率与刚性化。
二挠代表差的比较可以对 (RF.28) 两侧一并再取平方；相同的原 canonical square 同构给等距比较，最后按相同因子除回。没有把一个未给出的二挠主函数设为 $1$。

为了不将一个仅在 $K$ 上给出的 theta 帧当作单一原有理地方的输入，
直接记 $z_j^{(3)}$ 为
$u_j^{\otimes6}$ 通过 $\mathcal S_j^{\otimes3}$ 的 (RF.16) 得到的实际非零向量
$$
z_j^{(3)}\in
\mathcal P_J\bigl(\gamma,3\lambda_{\mathcal S_j}\gamma\bigr)^\times(\mathbf Q).
\tag{RF.29}
$$
其真实 $\mathbf Q$ 下降由 §5 保证；同理 (RF.9) 的两个点也在原有理纤维中。
若辅助地定义 $u_j^{\otimes2}$ 的点 $z_j$，则 $z_j^{(3)}$ 是固定第一变量、第二槽的 tensor 立方，而不是扩张内乘三。
原 $\beta=q\gamma$、$\lambda_{\mathcal S_j}$ 中的 $v^\dagger v$ 和原极化保留于 (RF.29)；不是将 $\gamma$ 或 $\beta$ 换成 $P_Y$。

在每一个原地方 $v$，R724 的 tensor/标量及 theta 因子 $1/2$ 给
$$
\boxed{
\lambda_{v,h_j}(c_1)
=\frac1{3q_j}\left[
 \chi_v(\nu_j)
 +\frac12\,\tau_{J,v}(z_j^{(3)})
 +\tau_{Y,v}(v_j^R)
\right].}
\tag{RF.30}
$$
代入 (RF.13)，等价地
$$
\boxed{
\lambda_{v,h_j}(c_1)
=\frac1{3q_j}\left[
 \chi_v\!\left(\frac{\nu_j\kappa_j}{\mathcal R_j(P_1)}\right)
 +\frac12\,\tau_{J,v}(z_j^{(3)})
 +3\,\tau_{Y,v}(v_j)
\right].}
\tag{RF.31}
$$
两个式子均在同一个真实 $\mathbf Q$ tensor 表示下成立。若实现先在辅助定义域写分量，先按 §5 的原有理下降组成 (RF.29) 与 (RF.9)，再按 R724 的地方规则求值；不能以一个扩域的单一 $p$ 位替换原全局和。

特别地，局部 $p$ 项不能借乘积公式删掉
$\chi_p(\nu_j\kappa_j/\mathcal R_j(P_1))$。全局乘积公式只在保留同一有理纤维与全部地方后使用。R593/R724 的所有非 $p$ 局部项和已有坏处结论保持原样；这里没有新假定它们全部为零。

## 8. 最小新消费者及仍待准确求值的对象

本构造的新算术输入已缩为既有原源的以下组合：

| 对象 | 已成来源 | 新表达式 |
|---|---|---|
| 实际 Picard 点 $\xi_j,\xi_j^R$ | GP 五个两图理想、原三同源正乘 | 理想类及实际主同构；不选未知除点 |
| $v_j,v_j^R$ | 同两图理想、$P_1$ 帧 $1$、$P_0$ 帧 $t^{-7\delta_j}$ | (RF.9) 的一维纤维商 |
| 比较 $\kappa_j/\mathcal R_j(P_1)$ | c0 真范数 DAG、R844 原比较值 DAG | 第二 Picard 槽的原 tensor 运输 |
| theta 帧常数 $\nu_j$ | 同六个 $M_h$、原 $3s$ | (RF.24)，或实测纯 $s$ 形的 (RF.27) |
| $z_j^{(3)}$ | 原 $q_R,G_j,\Theta_B$ 与原点值 | 三次 theta 源的原 canonical square 有理 Poincaré 点 |
| 原归一截面 | 前五行与原 $C_h$ | (RF.26)、(RF.28)，两套具体帧的一阶同时保留 |

输出可以沿既有 DAG 方式保存这些有限准确对象，操作只需原理想纤维、固定局部帧、整数 tensor 幂、真 Galois 范数、Poincaré 部分张量同构与原 canonical square。没有要求先物化全部理想格、求 $\eta$ 的标准 Jacobian 代表或展开原2420阶单位解。

这个新代数接口关闭的是原基点归一标量及实际线丛/纤维的输入接缝。仍需按同一原 splitting 求
$\tau_{J,p}(z_j^{(3)})$、$\tau_{Y,p}(v_j)$ 及全局 Picard 线性校正
$2\ell_{h_j}(\log P_Y)$。R724 的精确群公式和既有 UE 全 jet 相消仍适用；这些真实 periods 没有被 (RF.31) 置零，也没有因为五个 $\mathcal R_j'$ 非零而被证明不相消。
本文不声称原 $\Lambda_{h_j}$、指定 $\mathscr T_p$、A.1 或全 $p$ 排除已经得到。

## 来源定位

- R593，(593R.13)–(593R.19)：原 autoduality 符号、完整修正、真正无零截面及原 $C_h$。
- R18 §§1–3、R148 §2：实际纤维范数和沿基点/对角线的规范线丛同构；本篇不将这些一般接口重登为新结论。
- R724 §§5–7：同一原 Poincaré 对数、canonical square 的 $1/2$、全 tensor 和非 $p$ 地方。
- R728 §1、R791 §§2–5：原椭圆外积 theta、真实同态/目标相位、极化尺度、实际五个 $h_j$ 和三次同源。
- [原 c0 完整证明](2026-11-16-original-c0-Hom-nonramification-and-comparison-leading-terms.md)：$\lambda^3=108W$、全部不分歧、原 $\kappa_j,d_j$ 及帧。
- [GP 完整理想与主函数](R839-original-global-addition-polar-ideals-and-eta-DAG.md)：原分式理想、负 Picard 类号及三同源正乘。本文所用两项公开成功的原 source/certificate 已在 §1 列明。
