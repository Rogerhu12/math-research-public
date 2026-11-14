# 固定 cut 高度对全局径向 alpha 的稳定性

状态：**解析条件引理及已审输入上的有理账本；新组合待独立审查。** 此项只支付网格高度采样中采用数值 $\alpha$ 代表值的贡献，不支付有限求积、反解或舍入误差，也不改变证明图。

作者：/root/tail_theory，2026-11-09。

## 1. 固定 cut 的参数化

用一个从 cuff 向 cut 递增的共同源坐标 $x\in[\xi_0,\xi_1]$；有限多个或可求和的分段可合并为此有序积分记号。源函数 $a(x),b(x),w(x)$ 不随 $\alpha$ 变，且

$$
a\ge0,\qquad b\ge0,\qquad 0\le w\le W,\qquad
q_\alpha=a+\alpha b>0
$$

在每个内部段成立。假设全部所用积分有限。固定外半径 $c$，定义

$$
R_\alpha(x)=c-\int_x^{\xi_1} q_\alpha(s)\,ds,\qquad
J_\alpha(x)=\int_x^{\xi_1} w(s)q_\alpha(s)\,ds.
$$

在 $R_\alpha([\xi_0,\xi_1])$ 内，令

$$
H_\alpha(r)=J_\alpha(R_\alpha^{-1}(r)).
$$

若 $r<R_\alpha(\xi_0)$，将 $H_\alpha$ 按 cuff 平面常值 $J_\alpha(\xi_0)$ 延拓。本文只比较 $r\le c$。记 $B=\int_{\xi_0}^{\xi_1} b(s)\,ds$。

**引理。** 对任意 $\alpha_1,\alpha_2$ 与共同物理半径 $r\le c$，

$$
|H_{\alpha_2}(r)-H_{\alpha_1}(r)|
\le W B\,|\alpha_2-\alpha_1|.
\tag{1}
$$

它只需要源积分的单调性与 $0\le w\le W$，不需要控制高阶径向导数或精确反解 $r(x)$。

## 2. 证明

不妨设 $\alpha_2\ge\alpha_1$，记 $\delta=\alpha_2-\alpha_1$。先设 $r$ 在两个实际径向像区间中，令 $x_i=R_{\alpha_i}^{-1}(r)$。因为 $R_{\alpha_2}(x)\le R_{\alpha_1}(x)$，所以 $x_2\ge x_1$。相同物理半径给出

$$
\int_{x_1}^{x_2}q_{\alpha_1}
 =\delta\int_{x_2}^{\xi_1} b.
\tag{2}
$$

高度差为

$$
H_{\alpha_2}(r)-H_{\alpha_1}(r)
 =\delta\int_{x_2}^{\xi_1} wb-\int_{x_1}^{x_2}wq_{\alpha_1}.
\tag{3}
$$

由 (2)，右侧两项都在 $[0,W\delta B]$ 内，所以其差的绝对值不超过 $W\delta B$。此处不能无端改成两项绝对值之和而多付一个系数 $2$。

若 $R_{\alpha_2}(\xi_0)\le r<R_{\alpha_1}(\xi_0)$，第一幅高度已按 cuff 常值延拓。令 $x_2=R_{\alpha_2}^{-1}(r)$，则

$$
0\le\int_{\xi_0}^{x_2}q_{\alpha_1}
=\delta\int_{x_2}^{\xi_1} b-\bigl(R_{\alpha_1}(\xi_0)-r\bigr)
\le\delta B.
$$

公式 (3) 以 $x_1=\xi_0$ 仍成立，且两项仍都位于 $[0,W\delta B]$ 中。若 $r<R_{\alpha_2}(\xi_0)$，两幅高度都为常值，其差等于 $\delta\int_{\xi_0}^{\xi_1} wb$，同样满足 (1)。所有情况已覆盖。

可求和的无限源可先在有限端截断，再用非负可积函数的积分极限通过上述等式与不等式；不要求人为在某个物理深度改动背景。证毕。

## 3. 当前冻结源上的贡献

已有独审紧 $\alpha$ 报告
notes/2026-11-09-db6f-tail-tight-alpha.json
给出全局 $B$ 的上界与精确 $\alpha_*$ 的包含区间，完整背景给 $W=16/15$。固定 cut 高度 helper 的槽位正是 $\int wA+\alpha\int wB$，其径向距离是 $\int A+\alpha\int B$；两者满足本引理的同源形式。

将报告中输出的 binary64 区间端点当作确切有理上/下界，原代表值 $\alpha_0=97.64534740777785$ 与 $\alpha_*$ 的距离由这些输出端点保守估计。纯 Fraction 账本得到

$$
|\alpha_0-\alpha_*|<2.372\cdot10^{-11},
$$
$$
\sup_{r\le c}|H_{\alpha_0}(r)-H_{\alpha_*}(r)|
<4.56\cdot10^{-14}.
\tag{4}
$$

这一界使用打印区间端点，略松于紧 $\alpha$ 脚本内部保留的更精细有理区间，故不挪用其内部更小的差值。

账本 notes/2026-11-09-db6f-tail-height-alpha-transfer.json 绑定紧 $\alpha$ 输入与 helper SHA，并保存有理分子/分母。这里只认证理想精确积分高度在改变 $\alpha$ 代表值时的差。helper 实际有限求积与二进累加、源函数数值求值和反解仍未因 (4) 而获得严格误差条；G7 网格仍应如实标为有限证明图的数值离散近似。
