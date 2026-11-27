# 六位出生二 S2：完整二子集坐标与实际十五维上逆

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f / stable_kernel_return。

**状态：下面坐标与费用恒等式已纸面证明；新源码尚未运行，六位出生二 S2 尚未证明。** 上来源为原九维 $K_2$，低来源为原五维 $K_1$，上出生合法高度为二。本输入不套五位奇数硬端 Ward 消逆。

## 1. 原物理二子集的完整相似

设 $z_i=b_i^2>0$，$1\le i\le6$。在二孔层先用物理去权坐标，内积为 $\operatorname{diag}(z_i z_j)$。取十五个对称二元多项式
$$
f_{ab}(x,y)=\frac{x^ay^b-x^by^a}{y-x},
\qquad 0\le a<b\le5.
$$
在互异根上，其求值矩阵为单根 Vandermonde 的二阶外幂再逐行除以 $z_j-z_i$，所以行列式为 Vandermonde 的四次幂，确可逆。

令 $T$ 为六次单根 companion 矩阵，$v_k=T^k e_0$。乘 $x+y$ 在上述二子集基中是
$$
U_{\mathrm{sum}}=(T\otimes I+I\otimes T)|_{\wedge^2}.
$$
原删除 $R=d:\mathcal H_2\to\mathcal H_1$ 在去权坐标中为
$(Rf)_i=\sum_{j\ne i}z_j f(z_i,z_j)$，故其完整列为
$$
Rf_{ab}
=\sum_{r=0}^{b-a-1}p_{b-r}x^{a+r}
-(b-a)x^{a+b}\pmod{\prod_i(x-z_i)},
\qquad p_k=\sum_i z_i^k.
$$
原物理伴随为 $(R^*g)_{ij}=g_i+g_j$，因此它的第 $k$ 列在外幂坐标中准确为
$$
e_0\wedge v_{k+1}-e_1\wedge v_k.
$$
特别 $k=0$ 给 $2e_0\wedge e_1$，没有漏常数。

三次下降 $C=\sum b_i^3E_i$ 与其真正物理伴随分别为
$$
C=RU_{\mathrm{sum}}-TR,\qquad
C^*=U_{\mathrm{sum}}R^*-R^*T.
$$
这些式子不是普通矩阵转置。完整物理 Gram 为
$$
F_1=RR^*,\qquad
F_U=d_3d_3^*=SI_{15}-2U_{\mathrm{sum}}+R^*R,
\qquad RF_UR^*=4F_2,
$$
其中 $F_2=(d^2/2)(d^2/2)^*|_{\mathcal H_1}$。源码逐项核后两个完整低层身份。

这些坐标恒等式已由另一代理独立纸面核过；另一次只限 $z=(1,2,3,4,5,6)$ 的 BigInt 五身份校准用时 2 毫秒，仅用于核方向，不当作一般证明。

## 2. 同一上源的完整 MP 与精度

置
$$
P_K=I-R^*F_1^{-1}R,\qquad
G_u=P_KF_U^{-1}|_{K_2},\qquad C_u=G_u^{-1},
\quad B=C|_{K_2}.
$$
$F_U$ 是整个十五维 $d_3d_3^*>0$，源码先形成其完整 adjugate 和行列式，再压到实际 $K_2$。完整 Schur 给零延拓
$$
C_u=F_U-\frac14F_UR^*F_2^{-1}RF_U.
$$
在同一个低源 $L=K_1$ 上的三块恰为
$$
K_{bb}=BB^*,\qquad K_{bc}=BC_uB^*,\qquad K_{bg}=BG_uB^*.
$$
具体使用
$$
K_{bb}=P_L(C C^*-C R^*F_1^{-1}R C^*)|_L,
$$
$$
K_{bc}=P_L\left(CF_UC^*-\tfrac14CF_UR^*F_2^{-1}RF_UC^*\right)|_L,
$$
$$
K_{bg}=P_L(C-C R^*F_1^{-1}R)F_U^{-1}
(C^*-R^*F_1^{-1}R C^*)|_L.
$$
全部上核分量和真实物理逆均保留，没有先把维数压到某个短塔。

## 3. 完整 S2 四项费用

令原低出生 $L_j=\Gamma_{j,1}$，$E=L_3^{-1}$，$X=L_2EL_2$。原 R275 的
$$
A=\tfrac12(C_uB^*L_2+B^*X)
$$
给精确展开
$$
\boxed{
A^*G_uA=\tfrac14\left(
L_2K_{bc}L_2+L_2K_{bb}X+XK_{bb}L_2+XK_{bg}X
\right).
}
$$
两个混合项完整保留。低层 $L_2=P_LF_2^{-1}|_L$，以及
$E=F_3-P_3(T)QP_3(T)/e_4$ 都用已经核实的完整精度式。

若能证明这个同一正费用 $\mathsf K$ 满足
$\operatorname{Tr}_L(\mathsf K^2)<1/4$，则 $\mathsf K<I_L/2$；
已付同六位低源的首边 half 再给真正 S2。这里的迹是实际五维 $L$ 的算子迹，完整六维零延拓只用于计算，不能换作 companion 的 Frobenius 范数。

## 4. 单次原计算与范围

源码固定内层 180 秒、4 GiB；十五维上逆的每个 Faddeev 阶保存完整继续矩阵，完成费用后先写完整费用检查点，之后才算平方迹。所有实际分母来自正 $F_1,F_2,F_U$ 的完整行列式、$S,e_4$ 和正整数。只消去已经记录的完整因子，不假定未知因子的符号。

未返回完整标量以前不宣称费用已付；保存混符号 elementary 数据后仍须证明同一原正权多项式正性。本输入仅处理六位整个 S2；旧六位上源的 S1、同一低源内部第二边和七位完整首边分别有各自费用，不能仅由此宣布闭合。
