# 参数区间的完整 scalar germ 与根 collar

## 1. 同一家族的两种严格包含表示

固定 exact affine 第三步中心
\(\delta_3=-7832869216826619/4611686018427387904\)，
取明确测试盒
\[
\Delta_8=[\delta_3-10^{-8},\delta_3+10^{-8}].
\]
它不是被预先授予的最终 KAM 盒。

第一种实现把区间 \(c_0+\Delta_8v\) 放进每个 raw B-spline control，
再形成径向多项式和高阶 jet。这个实现给严格包含界，但区间运算会
丢失多个 control 共享同一参数的抵消；求高阶径向导数时，依赖损失很大。

第二种实现先分别计算准确 origin 和 direction 的完整物理 scalar germ，
然后才形成区间 affine 组合。这没有改变定义的图，也不把非线性的
\(F(\delta)\) 近似成 \(F(0)+\delta F_\delta(0)\)。
只对原本准确 affine 的 scalar 层作恒等重排；后面的 sin/cos、
primitive、E、曲率和 R37 密度仍全部按真实非线性运算计算。

## 2. 准确恒等式

用 \(b_0^\pm\) 表示固定 base 的正、负径向 germ，
\(p_0^\pm,v^\pm\) 表示 raw origin/direction germ。物理相位方向为
\[
(\beta_j)_\delta
 =\frac{v_{j,0}^+(b_0^+)^3+v_{j,0}^-(b_0^-)^3}{2},
\]
\[
(\gamma_j)_\delta
 =\frac{v_{j,1}^+(b_0^+)^2-v_{j,1}^-(b_0^-)^2}{2}.
\]
半径和高度的方向分别为
\[
a_\delta=\sum_\nu
w_\nu\frac{m_\nu^++m_\nu^-}{2},
\qquad
Z_\delta=\sum_\nu
w_\nu\frac{I_\nu^+-I_\nu^-}{2},
\]
其中 \(I_\nu\) 是准确 slope 原函数。
因此每个物理 scalar 都严格等于 origin 加 \(\delta\) 乘该方向。

B-spline 在 coefficients 上线性，乘固定 base 和明确奇偶对称也线性，
故上述恒等式对整个选定多项式的复延拓成立。
先取完整多项式再组合参数保留了高阶径向抵消。
最高 degree 为20，所以先保留21个系数；不能先截断到3 jet再移动中心。
在 bulk 中仍以准确 Fraction common span 选择多项式，
包含全部正、负 binary knots 和微小非空 span。

新的入口为
[scripts/fourfold_phase_beta_parameter_germ.py](../scripts/fourfold_phase_beta_parameter_germ.py)，
SHA256
e73a534ba9e8ccc39abfa69559f41b168481ba5fe509241f24e5411c998009b2。
其 direction_scalars 方法也直接给固定物理 r 的准确参数一 jet。
普通 interval 算术之后仍可能丢失相关性；
本方法只消除了在 B-spline 高阶导数形成前过早拆散参数的主要损失，
不声称保存所有非线性依赖。

## 3. 统一真根的意义

已有 R57 全参数共同简单根证书，对每个 \(\delta\in\Delta_8\)
给唯一真实根 \(t(\delta)\)。native interval Newton 从该共同 bracket
出发；每一步以真实含无限 primitive 尾的 \(C,C_r\) 作均值定理交，
所以保留所有参数的真根，而非只保留中心参数的根。

较大盒
\[
\Delta_5=[\delta_3-10^{-5},\delta_3+10^{-5}]
\]
也完成同一根步骤，得到严格
\[
.23839687233851576762<t(\delta)
 <.23839687512096409839
 \qquad(\delta\in\Delta_5).
\]
这只支付 \(\Delta_5\) 的根，没有支付其完整 beta。

在 \(\Delta_8\) 的 512-node collar 中进一步收紧后，
\[
.23839687372838191735031524798663
<t(\delta)<
.23839687373109794850599250795945.
\]
其半径不超过 \(1.358016\,10^{-12}\)。
256-node root 报告的较大半径含其已付无限 E 尾；
不能把两种节点数产生的区间差当误差证书。

## 4. 真根 deflation 在整个参数盒上仍正确

对每个实际参数，\(K(t(\delta),\delta)=0\) 是准确恒等式。
因此在 interval Taylor 中先包含所有可能的 \((t,\delta)\)，
再将 \(K\) 的常项置为准确零，保留的是这些盒中真正满足根恒等式的点，
不是任意把残差删掉。其余系数继续用共同 interval 包含界。

每个参数的
\[
-\frac{K(t-\rho,\delta)}{\rho}
=\int_0^1 K_r(t-u\rho,\delta)\,du
\]
都有同一复圆盘表示，分母和根号支在整个参数盒上同时验证。
固定 cut 使用中心点 collar 的准确有理数
\[
b=268136140016943/1125899906842624,
\]
且其小于所有参数的根；从 b 到所有根都在同一 scalar span 内。
真根移动包含在 \(\eta=t(\delta)-b\) 的区间中，
并没有冻结到中心 t。

## 5. 两种包含表示的已完成比较

两种方法对同一 \(\Delta_8\)、同一 cut 使用相同 native 几何和尾公式。
在 192 bits、512 quarter nodes、2048 angular nodes、degree24/
precision72 的 collar 层得到：

| 项 | control 区间先组合 | 完整 germ 后组合 |
|---|---:|---:|
| collar 中真根半径上界 | \(3.450384\,10^{-10}\) | \(1.358016\,10^{-12}\) |
| \(g_0\) 系数球半径上界 | \(2.601958\,10^{-6}\) | \(4.708091\,10^{-8}\) |
| collar 有限部总半径上界 | \(0.597063744\) | \(0.010688339\) |
| 径向解析尾上界 | \(1.525192\,10^{-7}\) | \(1.514681\,10^{-7}\) |

完整 germ 的 uniform collar 严格满足
\[
1307.19828862198
<I_{\rm collar}(\delta)
<1307.21966529806
\qquad(\delta\in\Delta_8).
\]
完整角误差不超过 \(1.341303\,10^{-13}\)。
新的总半径改善约56倍；大部分改善来自有效保留实际参数方向，
不是增加浮点精度或漏掉原有尾项。

旧 control 表示的结果仍是有效区间；它只是太宽，不能满足后续
危险格预算。因此保留旧源码和报告作为失败诊断，不修改成新的结果。

## 6. 全 bulk 的统一计算接口

[scripts/fourfold_phase_beta_parameter_bulk.py](../scripts/fourfold_phase_beta_parameter_bulk.py)
沿同一 \(\Delta_8\) 计算完整 bulk，使用相同的方向 germ 入口。
它保留所有实际无限尾、连续角间隙、复根号支和精确 knot 分区。

每个固定实参数的 integrand 在被接受复 r 域上解析。
共同 interval callback 同时包含全部成员；
Arb 的径向验证积分因而对每个参数都成立。
这一步不要求参数本身复解析，也不从中心点误差推断参数邻域误差。

为容纳实际参数宽度，在每原始 span 的 \(0.0002\) 基础上，
将额外总预算 \(0.04\) 以靠近 root 的 \((t_{\rm floor}-r)^{-3/2}\)
权重差分配。该分配只是要求的数值精度：
每个叶片仍必须实际证明其完整误差球满足分配值；
预算不是对未计算误差的假定上界。
权重用一个确定的 root 下端点，和真实密度是否恰好呈该大小无关。

完整 beta 必须等所有真实 span 通过后，使用
[scripts/fourfold_phase_beta_parameter_combine.py](../scripts/fourfold_phase_beta_parameter_combine.py)
校验同一参数盒、源 hash、cut、腰部与准确全部端点覆盖，再合并 collar。
当前两份 bulk 正在运行；本说明不预支其结果。

## 7. 已完成报告身份

| 报告 | SHA256 |
|---|---|
| beta-step3-parameter-collar-h1e8.json，旧表示 | 0378eaa98ee17b8fcd321acb75ec643f3b5c0a3820748b5233b5d5a89d142f42 |
| beta-step3-germ-root-h1e8.json | 56bafefb728243fc340490c2504f60fd593716ae71f3aaaad32f43ad8b790e04 |
| beta-step3-germ-root-h1e5.json | 55fb389d5c9937aff04f6b08ee75dea851c1718aed7619c0968e7dd03865669f |
| beta-step3-germ-collar-h1e8.json | 9c97251943c911ac7a2dbde0665b9bbc7ca5a2a9dcbfc017d8792854cd7462cd |

表中的报告均在本 notes/ 目录，包含完整输入和依赖 hash。
这些明确测试盒尚未等同于最终实际 KAM 参数区间；
后续若中心改变，须重锚或使用已付导数预算迁移。
