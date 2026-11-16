# 原 c0 的全部 Hom 不分歧与五个比较主函数首项

日期：2026-11-16。状态：**以下原 p41 纸面命题及四行求值公式已证明；数值坐标由后续公开 Actions 消费者取得。**

本篇只使用已经完成的原 R791、R803、R837、R838。
固定原 $K=\mathbf Q(\zeta)$、$s=1+2\zeta$、$L=K(b)$、
$C:y^2=x^3+b$、$f=f_4$ 及 $g_j=(1+T^j)f$。
全程保留原基点 $c_0$、一次参数 $a$ 和商参数
$$
t=a^3,\qquad P_0=\phi(c_0).
\tag{C0.1}
$$
这里的 $t$ 不是 R806 的全局 primitive 元，也不是 $c_1$ 的参数 $a-1$。
不改变同靶运输、真实七次 Galois 作用、$82$ 的尺度或任一个非零常数。

## 1. 已成的 P0 不在 D 推出全部实际 Hom 在 c0 不分歧

[R762 §§1–2](../results/R762-original-mu3-quotient-and-single-function-map-recovery.md)
给原 $\delta(a)=\zeta a$，$c_0$ 是唯一有限固定点，$a$ 是其一次参数；
原模型及此唯一点定义于 $\mathbf Q$，商上的 $t$ 是 $P_0$ 的一次参数。
[R805 定理805.3](../results/R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)
在整个原整数 Hom 格上给
$$
E_g=(y_g)_\infty=\mathcal B+3D_g,\qquad
\mathcal B=\mathcal D_{\rm cusp}+P_0.
\tag{C0.2}
$$
若 $g$ 在 $c_0$ 的局部次数为 $1+3k$，则 $D_g$ 在 $P_0$ 的重数为 $k$。

[R838](../results/R838-certified-original-second-derivative-ideal-and-minimal-order3.md)
已经实际证明原 $D_f$ 不含 $P_0$。
因此 $f$ 在 $c_0$ 不分歧。此处引用该已成结论，不重跑原导数理想。

令 $V=\mathcal H\otimes_{\mathbf Z}\mathbf Q$ 是 R791 的原 Hom 空间，
并定义
$$
\lambda_0(u)=
\left.\frac{u^*(dx/(2y))}{da}\right|_{c_0}\in L.
\tag{C0.3}
$$
[R791 定理791.1及(791R.15)](../results/R791-certified-original-Hom-descent-and-eta-inputs.md)
的原半线性作用在这个 $\mathbf Q$ 有理点和 $\mathbf Q$ 参数上同样给
$$
\lambda_0(Tu)=\rho\,\sigma(\lambda_0(u)).
\tag{C0.4}
$$
这不是把 $c_1$ 的数值搬到 $c_0$：这里只使用同一个原 $T$ 的定义。

$\lambda_0$ 是 $K$ 线性映射。由(C0.4)，其核为 $K[T]$ 子模。
原
$$
K[T]\simeq K[U]\big/\left((U^7-\zeta^2)/(U-\zeta^2)\right)
\tag{C0.5}
$$
是六次域，且 $\dim_KV=6$，故 $V$ 是其秩一模。
核只能是零或整个 $V$；R838 给 $\lambda_0(f)\ne0$，排除后一种。

**命题 C0.1。** 所有非零实际原 $L$-Hom 对应的曲线映射均在 $c_0$ 不分歧。
特别地，$f,g_1,\ldots,g_5$ 及其原三次同源像的 $y$ 极除子在 $P_0$ 均有重数1，
相应 $D_g$ 均不含 $P_0$。

这里的线性域是 $K$，不是把全部 $L$ 线性 Hodge 组合当成同态。
命题只针对原固定层41；没有证明全 $p$ 的单位或高度结论。

## 2. 六个原 M6 形式在 P0 的值和一阶只需末四行

[R803 的实际694维结果](../results/R803-certified-original-M6-mixed-Hodge-ratios.md)
已经给全部六个原形式
$$
U_0=H_f^3,\qquad U_j=H_{T^jf}H_f^2,\qquad
f^*\omega_C=2\pi iH_f\,d\tau
\tag{C0.6}
$$
的准确全局坐标。记
$$
V_j(t)=U_j/E_6,\qquad
U_j=\sum_{k=0}^{693}A_{jk}F_k,
\tag{C0.7}
$$
其中 $A_{jk}$ 必须读取原输出
**coefficients_in_unscaled_original_M6_basis**；
它们是原无尺度形式 $F_k$ 的系数。若使用另一套整数尺度系数，
须按既有 $82^6$ 关系转换，不能再次遗漏或重复尺度。

原末四行依次是
$$
F_{690}=E_4T_0,\quad F_{691}=E_4T_{73},\quad
F_{692}=E_6,\quad F_{693}=\eta_{\rm Ded}^{12}.
\tag{C0.8}
$$
[R837](../results/R837-certified-original-P0-evaluation-and-fixed-branch-pencil.md)
已给146个原正则函数在 $P_0$ 的值：
$$
\Phi_i=(82^2T_i)E_6/E_4^2.
\tag{C0.9}
$$
这些值自带 $82^2$，目标是 $P_0$，不是 $P_1$。

[R802 (802.6)](../results/R802-original-semilinear-parity-and-degree-seven-relations.md)
给原恒等式
$$
E_6/\eta_{\rm Ded}^{12}=24s(2t-1),\qquad
j=6912t(1-t).
\tag{C0.10}
$$
因此记
$$
R=E_4^3/E_6^2=1-(2t-1)^{-2},\qquad
e=\eta_{\rm Ded}^{12}/E_6=\frac1{24s(2t-1)},
$$
便有
$$
R(0)=0,\quad R'(0)=-4,\qquad
e(0)=-\frac1{24s},\quad e'(0)=-\frac1{12s}.
\tag{C0.11}
$$

前690行属于原普通 $V_3$。在 $P_0$，它们除以 $E_6$ 后至少二阶零：
对原三积，由(C0.9)直接得到
$$
\frac{T_uT_vT_w}{E_6}
=\frac{R^2}{82^6}\Phi_u\Phi_v\Phi_w=O(t^2);
\tag{C0.12}
$$
原线性组合保持此阶数。后两类则满足
$E_4T_i/E_6=R\Phi_i/82^2$。
于是
$$
\boxed{\begin{aligned}
V_j(0)&=A_{j,692}-\frac{A_{j,693}}{24s},\\
V_j'(0)&=-\frac4{82^2}
 \bigl(A_{j,690}\Phi_0(P_0)+A_{j,691}\Phi_{73}(P_0)\bigr)
 -\frac{A_{j,693}}{12s}.
\end{aligned}}
\tag{C0.13}
$$
导数是原 $t$ 导数。因为 $R(0)=0$，这里不需要 $\Phi_i'(P_0)$；
也不需要重新求690条三积值、原 M6 坐标或巨大 $A/B$。

## 3. 原一次参数与 Hodge 形式之间的常数恰为108

令 $\mathscr D=(2\pi i)^{-1}d/d\tau$。
由 Ramanujan 恒等式
$$
\mathscr DE_4=(E_2E_4-E_6)/3,\qquad
\mathscr DE_6=(E_2E_6-E_4^2)/2
$$
直接相减，得到
$$
\mathscr DR=(E_4^2/E_6)(R-1).
$$
另一方面(C0.11)的全局表达式给 $R'=4/(2t-1)^3$，
故
$$
\mathscr Dt=-\frac{(2t-1)E_4^2}{4E_6}.
$$
使用 $t=a^3$ 并立方，准确得到
$$
\boxed{\frac{(\mathscr Da)^3}{E_6}
       =\frac{(1-t)^2}{108(1-2t)}.}
\tag{C0.14}
$$
这是同一解析 $\tau$ 和同一原 $a$；没有重新选择三次根或 period。

对原六个映射 $h=f,g_1,\ldots,g_5$，令
$$
W_f=V_0,\qquad
W_{g_j}=\frac{(V_0+V_j)^3}{V_0^2}.
\tag{C0.15}
$$
由原微分加法及(C0.6)，这正是 $H_h^3/E_6$。
若
$$
h^*\omega_C=(\lambda_h+\mu_h a^3+O(a^6))\,da,
\tag{C0.16}
$$
则(C0.14)给
$$
\left(\frac{h^*\omega_C}{da}\right)^3
=108\,\frac{1-2t}{(1-t)^2}W_h(t).
\tag{C0.17}
$$
单位 $(1-2t)/(1-t)^2$ 在0的值为1、线性项为0。因此
$$
\boxed{\lambda_h^3=108W_h(0),\qquad
       \frac{\mu_h}{\lambda_h}
       =\frac{W_h'(0)}{3W_h(0)}.}
\tag{C0.18}
$$
命题C0.1保证所有分母非零。特别地
$$
\frac{\lambda_{g_j}}{\lambda_f}
 =1+\frac{V_j(0)}{V_0(0)}\ne0.
$$
后续只需要准确立方及上述比值，不任取立方根。

## 4. 原 y 的局部首项及平方主函数

目标原参数记为 $\xi=-x/y$，以免和 $t$ 混淆。
原方程 $y^2=x^3+b$ 逐项给
$$
x=\xi^{-2}-b\xi^4+O(\xi^{10}),\qquad
y=-\xi^{-3}+b\xi^3+O(\xi^9),\qquad
\omega_C=(1+3b\xi^6+O(\xi^{12}))d\xi.
\tag{C0.19}
$$
原 $\mu_3$ 等变性使(C0.16)只有 $a^{3n}$ 次系数。
(C0.19)与积分因此给
$$
\xi_h=\lambda_h a+\frac{\mu_h}{4}a^4+O(a^7).
$$
所以在原商参数 $t=a^3$ 下
$$
\boxed{
y_h^2-b=x_h^3
=(108W_h(0))^{-2}t^{-2}
\left(1-\frac12\frac{W_h'(0)}{W_h(0)}t+O(t^2)\right).
}
\tag{C0.20}
$$
这既保留了准确非零首项，也保留第一个单位项。
此处的形式单位对数导数是代数系数抽取，尚未施加 $p$ 进对数或局部高度。

## 5. 五个原比较函数的阶、常数和第一单位项

[R803 (803.23)–(803.26)](../results/R803-original-single-map-reuse-and-mixed-Hodge-ratios.md)
固定
$$
(p_j,q_j)=(165,67),(93,67),(100,67),(168,67),(371,134),
\qquad \delta_j=p_j-q_j>0,
$$
$$
\mathcal R_j=
\frac{N_{L/K}(y_{g_j}^2-b)^{q_j}}
     {N_{L/K}(y_f^2-b)^{p_j}}.
\tag{C0.21}
$$
所有 norm 均为真正的七个 $\sigma$ 共轭，特别包括 $\sigma(b)$；
原 $\sigma$ 固定 $t$。不把此 norm 换成同靶 $T$ 乘积，
也不删除二者之间的原常数。

置 $M_h=N_{L/K}(108W_h(0))\in K^\times$。
由(C0.20)，
$$
\boxed{\begin{aligned}
\operatorname{ord}_{P_0}\mathcal R_j&=14\delta_j,\\
\mathcal R_j&=\kappa_jt^{14\delta_j}
                  (1+d_jt+O(t^2)),\\
\kappa_j&=\frac{M_f^{2p_j}}{M_{g_j}^{2q_j}}\in K^\times,\\
d_j&=-\frac12\left[
 q_j\operatorname{Tr}_{L/K}\!\left(\frac{W_{g_j}'(0)}{W_{g_j}(0)}\right)
 -p_j\operatorname{Tr}_{L/K}\!\left(\frac{V_0'(0)}{V_0(0)}\right)
 \right].
\end{aligned}}
\tag{C0.22}
$$
另一个保全部常数的首项写法为
$$
\kappa_j=
N_{L/K}(108V_0(0))^{2\delta_j}
N_{L/K}\!\left(1+\frac{V_j(0)}{V_0(0)}\right)^{-6q_j}.
\tag{C0.23}
$$
而准确的一阶商只需
$$
\frac{W_{g_j}'(0)}{W_{g_j}(0)}
=3\frac{V_0'(0)+V_j'(0)}{V_0(0)+V_j(0)}
 -2\frac{V_0'(0)}{V_0(0)}.
\tag{C0.24}
$$

因此六个 $V_j$ 的值和一阶、六个准确 $K$ 范数及五个准确 $K$ 迹
就给出所有(C0.22)数据。整数幂可以保留为有限准确表达式；
不要求为得到 $\kappa_j$ 而展开巨大整数。
纸证只保证 $\kappa_j\ne0$，不预填 $d_j\ne0$。

## 6. 对原线丛比较纤维的准确含义

沿[原全局极理想命题](R839-original-global-addition-polar-ideals-and-eta-DAG.md)，
令
$$
\mathcal L_j=N(I_{E_{g_j}})^{q_j}N(I_{E_f})^{-p_j}
           =\mathcal O_Y(-Z_j).
$$
命题C0.1给 $\operatorname{mult}_{P_0}Z_j=-7\delta_j$，
故原 $\mathcal L_j$ 在 $P_0$ 的单项式局部生成元是 $t^{-7\delta_j}$。
原三次同源正号关系是
$$
\mathcal L_j^R=\mathcal R_j\mathcal L_j^3.
\tag{C0.25}
$$
由(C0.22)，$\mathcal L_j^R$ 的阶也为 $-7\delta_j$。
在源 $\mathcal L_j^3$ 的帧 $t^{-21\delta_j}$ 与目标
$\mathcal L_j^R$ 的帧 $t^{-7\delta_j}$ 下，乘 $\mathcal R_j$ 的单位为
$$
\kappa_j(1+d_jt+O(t^2)).
\tag{C0.26}
$$
所以 $\kappa_j$ 是这个指定原主函数比较在该帧中的准确纤维标量，
$d_j$ 是其第一个单位项。负理想类号、$q_j$ 与三次同源方向均未改变。

这一步没有选出 Jacobian 标准代表、规范对称 theta 线丛的二挠比较、
Poincaré 线丛的全部原刚性化或第二类 splitting。
(C0.26)是这些工作所需的一项具体原输入，不是完整刚性化或高度证书。

## 7. 后续公开消费者的有限范围

只消费原 R803 的六组694维坐标和原索引、末四 recipe，
原 R837 的 $\Phi_0(P_0),\Phi_{73}(P_0)$，
以及原 R791 的字段 $\sigma$ 与整数对 $(p_j,q_j)$。
各来源继续绑定原 producer/run/source/core、完整manifest、stage SHA和尺度。

新算术仅为(C0.13)、(C0.15)、(C0.18)、(C0.22)和(C0.24)的有限原域运算；
实际数值、分母非零、真 norm/trace 必须由本公开仓库 Actions 执行并保存。
旧 M6、CM、完整 Hodge、原 $A/B$ 和全局大矩阵不重新计算。
本篇没有得到规范高度、全 $p$ 排除或主目标的完成。
