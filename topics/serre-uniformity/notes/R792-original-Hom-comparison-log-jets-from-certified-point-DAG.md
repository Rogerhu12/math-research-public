# 原比较函数在 c1 的对数一阶项：消费已成 Hom 点与十二切向

日期：2026-11-16。状态：准确接口已证明；以下没有声称新的一阶节点已实际运行。它消费 [R844](../results/R844-certified-original-five-Hom-word-points-and-comparison-values.md) 已成的五个原加法点及比较函数值，而不改写该次工作流或重新计算其529个节点。

## 1. 原参数、微分和点值

保持原 $C_b:y^2=x^3+b$、$s=1+2\zeta$ 和同一个 $L$。原点为 $c_1$，原 $\mathbf Q$ 定义的一次参数为
$$
z=a-1.
\tag{J1}
$$
[R791](../results/R791-certified-original-Hom-descent-and-eta-inputs.md) §6 已准确计算十二个原整数 Hom 基的值
$$
h_i=\left.\frac{f_i^*(dx/(2y))}{dz}\right|_{c_1}\in L.
\tag{J2}
$$
本篇只读这些值；不再收缩 R748 的六个微分，不再乘一次 $\zeta^2$，也不把 $dx/(2y)$ 换成别的微分规范。数据中的历史键 `actual_L_coefficients_h_i_over_ds_at_c1` 所指的粗参数在数学上就是 (J1)，其 `ds` 不指本篇的数域常数 $s$。

对实际整数 Hom 字 $u=(u_i)$，记
$$
f_u=\sum_i u_i f_i,\qquad h_u=\sum_i u_i h_i,
\qquad P_u=f_u(c_1)=(x_u,y_u).
\tag{J3}
$$
这里的 $u_i$ 是原整数 Hom 矩阵中的坐标，不是随意的 $L$ 线性微分组合。[R843](../results/R843-certified-original-CM-point-nontorsion-and-Hom-value-separation.md) 已证明每个非零原 Hom 字在这个同一点的值非挠，故它有限且不属于 $C_b[2]$ 或 $\ker(1-\zeta)$；特别是
$$
x_u\ne0,\quad y_u\ne0,\quad y_u^2-b=x_u^3\ne0
\qquad(u\ne0).
\tag{J4}
$$
R844 的 $f$、五个 $g_j=(1+T^j)f$ 及它们的指定实下降 Hom 字都非零，并已逐个源绑定。因而 (J4) 对本篇所有分母均适用，不要求准确展开点坐标。

## 2. 点表达式直接给一阶项

由 (J2)--(J3) 的原微分规范和曲线方程，在 $c_1$ 有
$$
\frac{dx_u}{dz}=2y_u h_u,
\qquad
\frac{dy_u}{dz}=3x_u^2h_u.
\tag{J5}
$$
第一式是定义；第二式由 $2y_u y'_u=3x_u^2x'_u$ 及 (J4) 得到。于是
$$
\left.\frac{d}{dz}\log(y_u^2-b)\right|_{c_1}
 =\frac{2y_u\,3x_u^2h_u}{x_u^3}
 =\boxed{\frac{6y_u h_u}{x_u}}.
\tag{J6}
$$
这里的 $\log$ 只表示代数对数导数 $F'/F$，没有选择复或 $p$ 进对数分支。右端只使用 R844 的准确点 DAG、原 (J2) 的有限线性组合，以及由 (J4) 证明合法的一个倒数。因此它是准确 $L$ 元素的表达式；不以有限精度相等或有理重构候选作为输入。

对原三同源 $[\alpha_3]$，$\alpha_3=1-\zeta^2$，原微分满足
$$
h_{[\alpha_3]u}=\alpha_3h_u.
\tag{J7}
$$
它可直接与 R844 已成的下降点节点代入 (J5)--(J6)，没有另求立方根或省略三同源常数。

## 3. 原七共轭 Norm 的导数

$c_1$ 与 $z$ 均在 $\mathbf Q$ 上定义，所以原 $\sigma\in\operatorname{Gal}(L/K)$ 与 (J1) 的求导交换。对任意非零原函数 $F$，在本点有
$$
\frac{(N_{L/K}F)'}{N_{L/K}F}
 =\sum_{k=0}^{6}\sigma^k\!\left(\frac{F'}F\right).
\tag{J8}
$$
这是真实七个域共轭的和；对 DAG 的 $\sigma^k$ 必须作用于所有原数域常数、隐式单位图叶及右端，沿 R844 的完整自动同构语义。

记 R791/R844 原 $r_j=a_j/b_j$，$b_j>0$，保持实际比较函数
$$
\mathcal R_j=
\frac{N_{L/K}(y_{g_j}^2-b)^{b_j}}
{N_{L/K}(y_f^2-b)^{2b_j+a_j}}.
\tag{J9}
$$
由 (J6)--(J8)，准确的一阶对数项为
$$
\boxed{
\left.\frac{\mathcal R'_j}{\mathcal R_j}\right|_{c_1}
=6\left[
b_j\operatorname{Tr}_{L/K}\!\left(\frac{y_{g_j}h_{g_j}}{x_{g_j}}\right)
-(2b_j+a_j)\operatorname{Tr}_{L/K}\!\left(\frac{y_fh_f}{x_f}\right)
\right].}
\tag{J10}
$$
原比较函数值在 R844 已是非零的准确 DAG，所以还可形成
$$
\mathcal R'_j(c_1)=\mathcal R_j(c_1)
\left(\mathcal R'_j/\mathcal R_j\right)(c_1).
\tag{J11}
$$
不需要先展开任何一个 Norm。若为了表示使用同靶 $T$ 乘积，原 $N_{L/K}(b)/b^7$ 比较常数在 (J9) 的值中仍须保留；它的导数为零不能授权从原值 DAG 删除它。本接口优先沿已成七个真实 $\sigma$ 分量，不另引入这一改写。

## 4. 可执行的最小来源和输出边界

首消费者只需两组已完成来源：

1. R844 实际 run `43780702248`、source `5ebcfafb1c0bf72618a50de1f974c5d46d13ff58` 的证书、529节点程序、原归一化和完整源绑定。程序为68403字节，SHA `97a8fb3f185660468e6637358c9c29b34bfe8630599f36fa7e7f58ef6acb582b`；原全部节点必须按原内容哈希导入，不重做五次加法或七共轭值。
2. 该次一日载体中已携带的 R791 原 `R791-original-twelve-CM-tangents.json.gz`，20760字节，SHA `32be372f46560ce7cfc0af40666cdc32b39170bfc7b6ec32b92ea747a0629e7e`，以及其原 cert/manifest/run 身份。只按 R844 已认证的原 Hom 字计算 (J3)。

新的节点只包括原切向量线性组合、(J5)--(J6)、七项 trace 和 (J10)--(J11)。每个新增倒数应携带原非零 Hom 字与 R843 同点非挠证书的引用；禁止通过对未展开表达式的数值试探选择分支。

输出应区分 `original_comparison_logarithmic_first_jets_as_exact_expressions=true` 与 `expanded_coordinates_exactly_certified=false`。本篇没有新增准确数域展开坐标，也没有证明任一个对数一阶值非零。

这条接口不会给 $c_0$ 的原刚性化常数、全局五个加法极除子、抽象 $A$ 中同源核前像、$\eta_h$ 或 $p$ 进高度。它只把已成的原点与切向数据接到原比较函数在同一个 $c_1$ 的准确一阶表达式；这些其余任务保留各自的准确来源和零判条件。

全部新增算术仅公开 Actions。源码、参数、纸面证明及简明 run/SHA 可入 Git；机器节点与回执只在一日 active artifact/carrier 续传。
