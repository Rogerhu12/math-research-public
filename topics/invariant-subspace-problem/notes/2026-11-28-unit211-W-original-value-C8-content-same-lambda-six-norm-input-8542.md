# 全 W：原 cofactor 共同乘子约分、完整 λ 内容与同点六维范数原输入

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

本输入沿用一般 LS、$\Delta=W=0$、原单值互异且物理 $D\ne0$ 的既有 W 余图。这里的权单位表都是各自已刊整支结论；“本次身份不使用 $D^{-1}$”不把这些结论外推到另一个 $D=0$ 碰撞图。

状态：下面的原理想推导已经证明；新固定内容、范数的次数、零与非零及执行状态尚待唯一首次运行。旧 C8/R5 已成功结论不以本次执行为发表条件。

## 1. 冻结原来源与真正的新输入

[两个原值四次的固定八次 cofactor 与首一六次商中的五次必要式](../results/R150-appendix-unit211-W-original-value-quartics-fixed-cofactor-and-lambda-five.md)给出固定非零 $C_8(e,k,\lambda)$ 及原身份

$$
C_8\in I_8,\qquad
I_8=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S,R_4,C_4).
\tag{1}
$$

它的原来源是已实际返回的三行 $N_1,q_4,r_3$ 的八项迹和固定 $3\times3$ 余子式。与原两值四次之间的换行仅用权单位。

[全 W 原物理首一六次定理](../results/R150-appendix-unit211-W-global-original-physical-lambda-monic-six.md)给出

$$
\chi(\lambda)=\lambda^6+\sum_{j=0}^5c_j\lambda^j\in I_4\subset I_8,
\qquad c_j\in A_W.
\tag{2}
$$

$A_W$ 只倒置已经支付的权因子。本次只为新的内容与范数输入再生固定 $C_8$ 的必要定义前缀；不会执行旧 C8/R5 除法、十八行泛型模块、十二阶结式、NS/PS 二参旧行列式或另一个既有原返回门。

## 2. 先约去共同原乘子，完整保留其零纤维

旧固定 $3\times3$ 多项式行矩阵记为 $\mathcal A_3$，三条已返回原行满足

$$
\mathcal A_3(1,x,y)^T=\mathcal T F_8,\qquad
\omega^T\mathcal A_3=(C_8,0,0).
\tag{3}
$$

本次先取三个**原乘子** $\omega_i$ 的完整多项式公因子 $h$；它允许依赖 $e,k,\lambda$，没有被称为单位。对每个乘子作精确整除并乘回，令 $\omega_i=h\omega_i'$，然后直接构成

$$
C_*=\sum_i\omega_i'(\mathcal A_3)_{i0}.
$$

在原多项式环里有下面的完整身份；新源逐列返回

$$
(\omega')^T\mathcal A_3=(C_*,0,0),\qquad hC_*=C_8.
\tag{4}
$$

由同一组原行迹，得到**新的全图原组合**

$$
C_*=\sum_i\omega_i'\mathcal T_iF_8\in I_8.
\tag{5}
$$

这不是从 $hC_*\in I_8$ 擅自约去 $h$；(5) 直接给出没有 $h^{-1}$ 的原理想来源。因此整个 $h=0$ 纤维也被新输入覆盖。没有单独展开巨大的最后八项迹；定义及全部构成的精确乘回已经足够。

## 3. 完整 λ 内容保留整零支

写 $C_*=\sum_{j=0}^{8}a_j(e,k)\lambda^j$（必要时补零系数）。取全九个系数的实际 QQ 多项式 gcd，按非零有理数正规化为 $g$，对所有系数逐项精确整除并乘回。再只剥 $g$ 中已经支付的权因子：

$$
g=UG,\qquad C_*=UGP,\qquad U\in A_W^\times.
\tag{6}
$$

$P$ 是该定义下的 λ 本原部分；它的 λ 首项没有被倒置。$G$ 保留所有未付权内容，无论其次数或因式形状是什么。

由这个分解和新的原组合 (5)，给出的是

$$
GP\in I_8,
\tag{7}
$$

不自动给出 $P\in I_8$。本输入始终保留整条 $G=0$ 权纤维，也不以多变量 gcd 等于 1 推断几何无解。

## 4. 真实首一六维环境

令

$$
B=A_W[z]/(\chi(z)).
$$

这是由单首一多项式定义的自由六维环境，基底为 $1,z,\ldots,z^5$。这里的自由性只属于这个明确的环境；没有假定原 Gram 商或原六个生成元自由。

用首一除法得到

$$
P=Q\chi+r,\qquad \deg_zr\le5.
\tag{8}
$$

由首一原关系与 $GP\in I_8$ 得 $Gr\in I_8$。若 $r$ 恒零，本次只有这个准确退化返回，没有新的权曲线。

对 $j=0,\ldots,5$，完整计算并返回

$$
z^jr=q_j\chi+m_j,\qquad \deg_zm_j\le5.
\tag{9}
$$

把 $m_j$ 的六个系数作为乘法矩阵 $\mathcal M$ 的第 $j$ 列，故 $\mathcal M$ 正是同一点、同一个首一商中乘以 $r$ 的矩阵。

每列只清已付分母、除已付共同权因子及非零有理常数，得到

$$
A=\mathcal M\,\operatorname{diag}(\sigma_0,\ldots,\sigma_5),
\qquad \sigma_j\in A_W^\times.
\tag{10}
$$

列中出现的新共同内容不被约去。每个六系数列换算都会实际乘回。

于是定义

$$
N=\det A
=\left(\prod_{j=0}^5\sigma_j\right)\operatorname{Norm}_{B/A_W}(r)
=\left(\prod_{j=0}^5\sigma_j\right)\operatorname{Norm}_{B/A_W}(P).
\tag{11}
$$

实际返回的 $N$ 是规范范数乘一个已付单位；不把它误写为没有尺度的范数。

## 5. 一列原 cofactor 给全图关系，不需要 G 可逆

新源对固定六阶多项式矩阵 $A$ 和一个增广常数目标 $e_0$ 作分式自由消元。每个除法都是 QQ 权多项式精确整除，逐项乘回；最后实际返回

$$
A\gamma=Ne_0
\tag{12}
$$

的全部六个系数。中间行交换和主元只是计算多项式余子式的方法，不成为新局部化条件。

令

$$
b(z)=\sum_{j=0}^5\sigma_j\gamma_jz^j,\qquad
t(z)=\sum_{j=0}^5\sigma_j\gamma_jq_j(z).
$$

由全部真实列除法、列尺度与最后六列 cofactor 返回，直接得到完整原商身份

$$
r(z)b(z)-N=\chi(z)t(z).
\tag{13}
$$

不需要把这个已经由原列组合证明的表达式再展开成巨大的来源缓存。

把 $C_*=UGP$ 与 $P=Q\chi+r$ 代入上一身份，有

$$
\boxed{
GN=U^{-1}bC_*-G\chi(Qb+t)\in I_8.
}
\tag{14}
$$

这正是本输入要返回的全图关系。特别地，它只乘了一次 $G$，并没有把 $G$ 或任一未付 λ 头当成单位。

若最后仅从 $N$ 剥已付权单位 $V$，写 $N=VH$，则

$$
GH\in I_8.
\tag{15}
$$

$G=0$ 与 $H=0$ 的全部权纤维继续保留。若 $N$ 恒零，则没有新权条件；若尚未完成最后的六列返回 (12)，不宣称范数非零或任何排除。仅在实际 $G,H$ 都为非零常数时，最后这个原理想关系才构成当前整个原图的矛盾。

## 6. 固定源、必要前缀和首次界限

新源（比未执行 85e7 版增加完整原乘子约分，首次只执行本加强版；不将旧未执行版记成失败）：

notes/2026-11-28-unit211-W-original-value-C8-content-same-lambda-six-norm-8542.py

Git blob：330a6cc5f9caec38a58c94814fa83ff33c5ae366。

SHA256：d2de905b2bedcc5cd007aa465123e33e0c44d2e30cde9b5f56c7cdf4fb1d1aed。

13770 字节；固定总墙钟 180 秒、地址空间 4 GiB。各依赖必要前缀自己设置的 alarm 在执行期间被上限钳制到本次最初的绝对截止时刻，不因后加载前缀而重置本次总预算。

直接依赖：

- C8 原源 dc173050e023489ba7502f1b9c640be4d2dcfca4，仅使用 7431 字节，前缀 SHA256 e4c8ad9e117867918300972a4b15366f7e3281dbf858463bd1b2f4968a9ac55c。截在旧首一除法构造之前。
- χ 原源 4ab79a61a35f942edb15cfecff2562ccc82e065f，仅使用 8601 字节，前缀 SHA256 ce868f00596f420d1a46a1503e2432be7bd13f0001e8ebc3e0cd68a53092fc7a。截在旧两个谱纤维处理之前。

传递依赖仍是已提交的三规则源 5dafa52c453a06b5cb2c03aa16742a4af8e3fca9、物理 λ 源 0b261ecc3cb4ef012ed9dce5b9403723edccd7e4、C9 原六规则源 a1a9d02a1602a47398ba9bbb9295b3da7d7ddd37；全部 basename 与 SHA 在必要前缀中固定。

保存仅限本源、原参数定义、真实 run/exit、次数、字节数、SHA 和小回执；不输出或保存可重算系数、矩阵、大迹、编码或分片。本稿不提前宣称首次执行成功。
