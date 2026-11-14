# R172：原 norm-one Heegner 系数直线上的高度变化非退化

日期：2026-11-12。**已证明；指定两量的整非零仍未证明。**
[完整证明](../notes/2026-11-12-norm-one-height-variation-nondegeneracy.md)。

对原非扭 $R=D_pQ$，
$V_R=\mathbb Q_p[\Gamma]R$ 是一维
$K_p=\mathbb Q_p(\zeta_p)$ 空间。
在所有 p 完成保留实际对数，令
$$
 T(P,Q)=\sum_{v\mid p}\operatorname{Tr}_{L_v/\mathbb Q_p}
                    \bigl(\log_E(P)\log_E(Q)/p^2\bigr).
$$
则 **$T|_{V_R}$ 非退化**：

- p 在 F 分裂时，一个完成上的次数 p étale 代数 M
  可以是 $\mathbb Q_p^p$ 或未分歧次数 p 域。
  augmentation $I_M$ 为一维 $K_p$ 模；原非扭点的对数
  非零，故给 $V_R\simeq I_M$。
  另一完成由真实反射关系给相同贡献，完整配对为
  $2\operatorname{Tr}_M(xy)$。
- p 在 F 惰性时，L/F 在 p 完全 split。
  写 $q=z(\zeta_p)\in F_vK_p$ 并保 $cz=-z$，则
  $qq^*=-\operatorname{Nm}_{F_vK_p/K_p}(q)\ne0$；
  完整配对为这个非零标量乘
  $-(2/p)\operatorname{Tr}_{K_p/\mathbb Q_p}(fg^*)$。

R168 的两个同号 splitting 高度满足
$$
                h^L_\lambda-h^L_0=-\lambda p^2T .
$$
各高度的 radical 又是不可约 $\Gamma$ 模 $V_R$ 的子模，
故每个高度在此线要么零、要么非退化。
因此 $\lambda\ne0$ 时，两个高度至少一个非退化。
这一步保留了 $\Gamma$ 不变性，并非任意两个矩阵的断言。

原 $I_1,I_2$ 仍是指定权
$K_1(\zeta_p)=2p/D$、
$K_2(\zeta_p)=-24p/D^2-4p/D$ 的 trace，
$D=\zeta_p+\zeta_p^{-1}-2$。
惰性完成可进一步写 $q=\varpi^ku$、$\varpi^2=D$、
$k\ge1$。分裂完成则在原 augmentation 整格中构造自对偶
正规整基，得到同样的 q 与 k；构造只用
$\mathbb Z_p[C_p]$ 中 Gram 元的唯一平方根，不引入 p 分母。
两种情形都给原测试的准确范数版：
$$
    (\mathcal E_1,\mathcal E_2)\not\equiv(0,0)\pmod p
                              \iff k\le2 .
$$
$k=1$ 时 $\mathcal E_1\equiv\overline u^2\ne0$；
$k=2$ 时 $\mathcal E_1\equiv0$、
$\mathcal E_2\equiv\overline u^2\ne0$。
这是同一原第二矩判据的精确重写；
非退化仍未证明 $k\le2$，R164 的实际 $a\ge2$ 整深度仍须排除。

在原循环整格 $\mathcal O R$、$\mathcal O=\mathbb Z_p[\zeta_p]$
的任意 $\mathbb Z_p$ 基中，还准确有
$$
 v_p\det\bigl(T|_{\mathcal O R}\bigr)=2k-1 .
$$
这里保留不同于饱和 Mordell–Weil 整格的原点生成格。
因此原两量至少一项为单位等价于此行列式赋值至多 3。
若真实全局 $Q=\delta^aS$，则 $k=a+k_S$、$k_S\ge1$；
此式明确保留尚未控制的原始点局部深度，未从已知
Selmer 长度直接推出模 p 非零。

依赖：R130、R139、R157、R161、R164、R168。
