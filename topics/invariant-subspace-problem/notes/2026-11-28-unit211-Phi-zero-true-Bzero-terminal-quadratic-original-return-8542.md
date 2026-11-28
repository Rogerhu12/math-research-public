# 新输入：C76 的完整二次权域及原正单位目标

日期：2026-11-28（Asia/Taipei）。尚未执行；源 SHA256 a60dbe5808c0b2408ad4d3a0ac40f8c801ce9ade6fb3eb316a2d7bce7c059c4a。120 秒、1 GiB，必要前缀共用最初绝对截止。

## 1. 唯一新权因子

[正确整 B 的终端四原乘子](../results/R150-appendix-unit211-Phi-zero-true-Bzero-terminal-C76-original-ideal-cover.md)已完整返回
$C_{76}\in I_4$，并实际分解出次数 $2,34,40$ 的三个一次因子。本输入只处理
$$
\phi_2(x)=2x^2+4x-1.
$$
其判别式为 24，故
$$
K=\mathbb Q[x]/(\phi_2)
$$
是完整二维有理域，保两个复嵌入。它不是旧已闭斜率因子
$23x^2-11x+2$。本次不再生成 C76、C315 或其高次因子。

在 K 中 $x^2=-2x+1/2$，共轭为 $x\mapsto-2-x$。对 $a+bx$ 使用真实全代数逆
$$
(a+bx)^{-1}=
\frac{a-2b-bx}{a^2-2ab-b^2/2}.
$$
每次倒数都逐二坐标乘回；分母非零为实际断言。所有原权和中心坐标分母先在整个 K 中验证为单位，不在某个复根上择支。

## 2. 原 I6 重新特化，保所有 lambda 及 omega

只取既有整 B 源在 newValues 定义前的必要原 Gram、四式、中心坐标和首一
$$
q(\omega)=\omega^2+q_1(\lambda)\omega+q_0(\lambda)
$$
定义。旧源后面的十二行门与三个 cofactor 不执行。

先把原系数准确映入 K，再在 $K[\lambda,\omega]/(q)$ 中计算完整 NS、PS 的两列余式。四个原二次的余式逐项与既有四原线性余式核回。因此得到同一点六条真实原行
$$
r_i=a_i(\lambda)+b_i(\lambda)\omega,\qquad 0\le i\le5.
$$
不存在原模自由假设；首一 q 的原来源和已付两向中心坐标保持原理想呈示。

对原行对构造新的
$$
c_{ij}=a_i b_j-b_i a_j
      =b_jr_i-b_ir_j.
$$
每个两坐标身份实际乘回。对这些 $K[\lambda]$ 多项式作完整 Euclid 和 Bézout，返回首一
$$
g(\lambda)=\sum \eta_{ij}c_{ij}
          =\sum_{i=0}^5\zeta_i r_i.
$$
最后一式全两坐标返回，不仅报告 gcd 次数。

若 g 是 1，当前整个二次权域已由原单位排除。若所有 cofactor 为零，则不付 lambda 有限模型，也不称闭合。其余情况下，所有被倒置的 lambda 首项只是已实际核逆的 K 单位，故对两个复嵌入均无降次遗漏。

## 3. 完整有限代数和正目标

若 $\deg_\lambda g=d>0$，使用真实代数
$$
\mathcal A=K[\lambda,\omega]/(g,q),
\qquad \dim_\mathbb Q\mathcal A=4d.
$$
g、q 均首一；所有 lambda、omega 重根与幂零保留。原 I6 在此代数中的理想由六原行乘完整 $4d$ 个有理基向量生成。

把全部真实原乘积写成 $4d$ 行、$24d$ 列 QQ 矩阵。RREF 只选原列，选定方阵双向乘回；全部原理想列也用所选列完整返回。目标属于原列空间时，最后必须完整返回全部 $4d$ 坐标的原组合。

测试
$$
U^n,\quad U=\lambda tD_{\mathrm{val}},\quad
D_{\mathrm{val}}=\ell(2\lambda^2-2\lambda+1)-T^2,
\qquad 0\le n\le4d.
$$
t、T、D 都由同一点原中心坐标映入 $\mathcal A$。原值点上
$$
D_{\mathrm{val}}=\ell A_2-T^2=bc(h-k)^2.
$$
只作正乘法，不倒 D 或其范数。当前范围已由非零孤立均值、正确整 t=0 排除及物理 distinct-singleton 图支付 $\lambda tD_{\mathrm{val}}\ne0$。

只有实际返回某个 $U^n$ 属于原理想，才排除整个二次权域；即使 n 达到维数而仍未返，也只保未决，不用抽象幂零猜测代替实际身份。g 的原 Bézout 来源和 q 的原来源把有限代数中的目标组合提升回原 I6。

## 4. 结果边界与依赖

若该域关闭，C76 的其余 34、40 次因子完整保留，不同 $(u,Q)$ 权对上界可降至 74。没有据此关闭整 B，也不把原物理单位的排除扩大到裸理想或原 D=0 碰撞图。

规范 stem：
2026-11-28-unit211-Phi-zero-true-Bzero-terminal-quadratic-original-return-8542。

仅两源码依赖：

- 2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py，SHA b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56；
- 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py，SHA 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。

没有 JSON 系数载荷、旧终端清 LCM、旧高次投影或已闭 C2 重跑。
