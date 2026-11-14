# 六模式立方的完整第三矩消元与匹配 Bell 分母

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：**已证明。** 下述完整有限恒等式、非退化第三矩消元及匹配分母理想等价成立；尚未证明新的 Jacobian 归属或 $F^3e^w$ 循环性。

本稿继续原六模式
$$
F=g_6+i g_7+g_8,\qquad x_j=U_{j+1},
$$
并沿用[原完整矩计算](../notes/2026-11-13-complete-ordinary-bell-curve-critical-locus-and-symbol-denominator-boundary-1cf.md)的实化 $x_j=i^j y_j$。
当前标量二次式为
$$
F_0(y)=g_6(y)-g_7(y)-g_8(y)=\frac12y^{\mathsf T}Ky,
$$
$$
K=
\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
$$
所有换元都是已付的固定非零标量缩放，保留原物理合并键。

## 1. 完整 ordinary 多项式只需前三层矩

记 $v(z)=(1,z,\ldots,z^5)$。
原二次关系给 $F_0(v(z))=0$，从而
$$
F_0(y+s v(z))=F_0(y)+s\,v(z)^{\mathsf T}Ky.
$$
因此 $(v(z)\cdot\nabla)^dF_0^3=0$ 对 $d>3$ 成立。
比较 $z$ 的全部有限系数，原所有相应合并微分算子也分别把 $F_0^3$ 送为零。
所以高于三阶的 ordinary 矩在完整 $\mathcal Q_{F_0^3}$ 中准确消失。

保留十一条二阶矩 $H_0,\ldots,H_{10}$ 和十六条三阶矩 $V_0,\ldots,V_{15}$，写
$$
H=(H_{i+j})_{0\le i,j\le5},\qquad p=Ky.
$$
有限微分算子为
$$
L_2=-\sum_{i,j}H_{i+j}\partial_i\partial_j,\qquad
L_3=\frac23\sum_{i,j,k}V_{i+j+k}\partial_i\partial_j\partial_k.
\tag{1.1}
$$
有序指标在这里全部保留。
完整多项式是
$$
\mathcal Q_3=e^{L_2+L_3}F_0^3.
$$
次数直接给准确展开
$$
\mathcal Q_3=
F_0^3+L_2F_0^3+\frac12L_2^2F_0^3+\frac16L_2^3F_0^3
+L_3F_0^3+L_2L_3F_0^3+\frac12L_3^2F_0^3.
\tag{1.2}
$$
本稿不删除实际快累积量修正；(1.2) 是供真实逆分母定理使用的完整 ordinary 代数对象。

## 2. 不含三阶矩的全部项

每条 $K$ 反对角线的和为零，故 $\operatorname{tr}(KH)=0$。
定义
$$
b=p^{\mathsf T}Hp,\quad
c=p^{\mathsf T}HKHp,\quad
\tau_2=\operatorname{tr}((KH)^2),\quad
\tau_3=\operatorname{tr}((KH)^3).
$$
逐次求导得到
$$
L_2F_0^3=-6F_0b,\qquad
L_2^2F_0^3=12F_0\tau_2+24c,\qquad
L_2^3F_0^3=-48\tau_3.
$$
因此完整低矩部分为
$$
\boxed{
G_6(y,H)=F_0^3-6F_0b+6F_0\tau_2+12c-8\tau_3.
}
\tag{2.1}
$$
这里 $\tau_2,\tau_3$ 是矩阵乘积幂的迹。
$H$ 的权为二，$y$ 的权为一，(2.1) 每项的权都为六。

## 3. 十六个三阶矩的完整线性项

定义十六维列
$$
d_m(y)=[z^m]\big(p^{\mathsf T}v(z)\big)^3,
$$
$$
e_m(y,H)=[z^m]
\big(v(z)^{\mathsf T}KHKv(z)\big)\big(p^{\mathsf T}v(z)\big),
\qquad
\ell=d-6e.
\tag{3.1}
$$
因 $K$ 的各反对角和为零，三阶求导中含 $F_0K_{ij}p_k$ 的部分在每个真实合并键内消去。
准确有
$$
L_3F_0^3=4d^{\mathsf T}V,\qquad
L_2L_3F_0^3=-24e^{\mathsf T}V.
\tag{3.2}
$$
于是三阶矩的整个线性部分为 $4\ell^{\mathsf T}V$。
$\ell_m$ 的权为三；它同时含一次 $y$ 乘一次 $H$ 的项，不能只保留 $d_m(y)$。

## 4. 原常数 Hessian 及精确逆

置
$$
k(z,\zeta)=v(z)^{\mathsf T}K v(\zeta),\qquad
(J_3)_{mn}=[z^m\zeta^n]k(z,\zeta)^3
\quad(0\le m,n\le15).
\tag{4.1}
$$
由
$$
F_0(sv(z)+t v(\zeta))^3=s^3t^3 k(z,\zeta)^3
$$
可直接核验全部六阶导数。
(1.1) 中的 $(2/3)^2$ 与 $3!^2$ 给
$$
\frac12L_3^2F_0^3=8V^{\mathsf T}J_3V,
\qquad
\nabla_V^2\mathcal Q_3=16J_3.
\tag{4.2}
$$
这两个系数不能混同。

用原整数 $K$ 卷积构造全部256个条目，再用整数 Bareiss 消元，得到
$$
\boxed{
\det J_3=
23366320238786911411830138211362846399922176000\ne0.
}
\tag{4.3}
$$
[精确矩阵数据](../notes/2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json)
同时列出 $J_3$、全部 $\operatorname{adj}J_3$ 及 (4.3)；
左右乘的全部512个条目均严格等于 $\det(J_3)I$。
因此
$$
J_3^{-1}=\frac{\operatorname{adj}J_3}{\det J_3}
$$
是明确的有理矩阵。

作为原数据的交叉核验，同一卷积程序重算 $k(z,\zeta)^2$ 的十一阶系数矩阵，得到已发布的
$$
\det J_2=-64701092257700249600.
$$

## 5. 准确消到十七个低矩变量

合并 (2.1)、(3.2)、(4.2)，完整式为
$$
\boxed{
\mathcal Q_3=G_6+4\ell^{\mathsf T}V+8V^{\mathsf T}J_3V.
}
\tag{5.1}
$$
作多项式三角换元
$$
Z=V+\frac14J_3^{-1}\ell(y,H).
$$
则
$$
\boxed{
\mathcal Q_3=R_3(y,H)+8Z^{\mathsf T}J_3Z,\qquad
R_3=G_6-\frac12\ell^{\mathsf T}J_3^{-1}\ell.
}
\tag{5.2}
$$
$R_3$ 是六个 $y_i$ 与十一个 $H_m$ 的明确加权六次多项式。
没有展开新的大次数 Macaulay 矩阵，也没有引入任何新素数。
(5.2) 连同 (2.1)、(3.1) 和精确 $J_3^{-1}$ 已确定它的全部系数。

对任一低矩坐标 $u\in\{y_i,H_m\}$，保持原 $V$ 不动求导，
$$
\partial_V\mathcal Q_3=16J_3Z,\qquad
\partial_uR_3=\partial_u\mathcal Q_3-4(\partial_u\ell)^{\mathsf T}Z.
\tag{5.3}
$$
所以在这次多项式换元下，完整梯度理想准确对应
$$
(\nabla\mathcal Q_3)=(Z,\nabla R_3).
\tag{5.4}
$$
这只是有限标量理想的等价，并不把 $R_3$ 自动认作原规范目标算子。

权 Euler 恒等式还给
$$
6R_3=\sum_i y_i\partial_{y_i}R_3+
2\sum_m H_m\partial_{H_m}R_3.
$$
故零纤维理想 $(R_3,\nabla R_3)$ 与 $(\nabla R_3)$ 相同。

## 6. 匹配的完整 first Bell 立方

取任意固定标量列 $r\in\mathbb C^6$，写
$$
a_r(y)=r\cdot y,\qquad
h_r=r^{\mathsf T}Hr,\qquad
c_m(r)=\sum_{i+j+k=m}r_i r_j r_k.
$$
完整 ordinary Bell 立方为
$$
\boxed{
S_r=\mathcal Q_{a_r^3}
=(r\cdot y)^3-6(r\cdot y)h_r+4c(r)^{\mathsf T}V.
}
\tag{6.1}
$$
代入相同的消元，
$$
S_r=B_r+4c(r)^{\mathsf T}Z,
$$
$$
\boxed{
B_r(y,H)=(r\cdot y)^3-6(r\cdot y)h_r
-c(r)^{\mathsf T}J_3^{-1}\ell(y,H).
}
\tag{6.2}
$$
$B_r$ 的权为三，且准确保留全部二阶矩。

由 (5.4)，对每个整数 $N\ge1$，
$$
\boxed{
S_r^N\in(\nabla\mathcal Q_3)
\quad\Longleftrightarrow\quad
B_r^N\in(\nabla R_3).
}
\tag{6.3}
$$
这里均为自然代数幂，不是 first 的第 $3N$ 次 ordinary Bell 多项式。

如果未来取得明确恒等式
$$
B_r^N=\sum_u C_u\,\partial_uR_3,
$$
则令 $T_N=\sum_{j=0}^{N-1}S_r^{N-1-j}B_r^j$，
(5.3) 立即给完整提升
$$
\boxed{
S_r^N=
\sum_u C_u\partial_u\mathcal Q_3+
\frac14
\left(c(r)T_N-\sum_u C_u\partial_u\ell\right)^{\mathsf T}
J_3^{-1}\partial_V\mathcal Q_3.
}
\tag{6.4}
$$
这保留原全部偏导坐标，并且没有 $\mathcal Q_3$ 本身的倍数。
(6.4) 只是准确接口；本稿没有声称右侧所需 $C_u,N,r$ 已找到。

## 7. 可供后续使用的实际有界逆

原平方证书中的选择
$$
r=(A,B,0,0,0,1),\qquad A,B\in\mathbb R,
$$
对应原 first
$$
a=iA\,U_1+B\,U_2+U_6=i(r\cdot y).
$$
它的物理行仍是
$$
\frac{\log^5(p+2)+B\log(p+2)+iA}{p+2},
$$
正实相位缺陷可和，所以既有原 first 空谱定理适用；合法指数权只产生已经支付的有界交换扰动。

设该实际倾斜 first 为 $D$，$L=D^{-1}\in A'$。
完整 Bell 立方的原规范实现具有形式
$$
D^3+C_2D^2+C_1D+C_0
=(I+C_2L+C_1L^2+C_0L^3)D^3
\quad\text{于 }\operatorname{Dom}D^3.
$$
这里 $C_j$ 是实际有界交换系数，不删除低 Bell 项。
$L$ 拟幂零，括号是有界单位，因此逆为
$$
L^3(I+C_2L+C_1L^2+C_0L^3)^{-1}.
$$
完整自然域及原规范图的识别正是[单 first 完整 Bell 逆](../results/R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md) §4 的已有结论。

由于 $a=i a_r$，
$$
\mathcal Q_{a^3}=-iS_r.
$$
所以这些 $S_r$ 确有实际全域有界交换逆。
若未来 (6.3) 的左侧得到证书，便可代入[真实 Bell 逆分母定理](../results/R150-appendix-jacobian-certificates-with-actual-bell-inverse-denominators.md)；
但实际有界逆本身不提供 (6.3) 的代数归属。

## 8. 精确核验与未闭部分

[自含整数验证器](../notes/2026-11-13-six-mode-cubic-bell-third-moment-verify.js)
从原 $F_0^3$ 逐次求偏导，独立核验：

- 完整二阶矩部分的全部1332项；
- 十六个包含低矩修正的三阶矩线性部分；
- 全部256个六阶导数与三阶矩 Hessian 条目；
- 两个已述行列式，以及 $J_3$ 的左右伴随矩阵恒等式。

所有计算使用 BigInt，实际结果为完整通过。
本稿没有启动新大次数理想矩阵、有限域归属筛选或有理恢复。
剩余明确问题是：对一个已付实际逆的匹配 $B_r$，是否存在 $N$ 使 $B_r^N\in(\nabla R_3)$，或能否从这个具体加权六次结构找到别的真实证书。
原六模式 $F^3$ 的零参数及更高点态幂仍未由本稿关闭。

