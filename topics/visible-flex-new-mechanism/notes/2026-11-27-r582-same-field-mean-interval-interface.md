# R582 同一当前/参考 a,z 两 jets 与完整无限高度尾

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。附属纯接口 [r582_same_field_mean_intervals_20261127.py](../scripts/r582_same_field_mean_intervals_20261127.py)，接 [同场材料/全角接口](2026-11-27-r582-same-field-radial-interval-interface.md) 和 R611 v2 的 `CompactGeometry` 高度积分对象。没有在本地执行科学，没有全域数值通过声明。原 22,813 B 材料模块保持不变。

## 1. 当前与参考完整实数公式

当前 q 的 `q[64:72]`、`q[72:80]` 和最后的 `q[96]` 分别控制原 log-radius spline、height spline 和末端帽高。`SameFieldMeanGeometry(design,height_provider,reference_q=None)` 默认比较原 `SOURCE_Q`；也可以明确传入实际 81q 或 97q 的 `reference_q`，只取它的 `64:80` 和最后帽高，建立**新的圆核心比较面**。两者都保留原固定 `mu,nu` compact-bump 项。当前核心半径输入必须为**同一 rounded ellipse 的准确归一周长**的区间，可直接取 `rounded_core_angular_boxes(...)["a0"]`；不把普通 `ellipe` 的一个浮点返回值当作认证。

新选择只控制 a/z 比较面。模块单独构造它的 `reference_alpha`，**绝不改动 `design.reference_alpha` 或材料 seed 商法使用的旧冻结半径**。把新的 q 本身作为 `reference_q` 时，新参考继承同一组全部 mean 控制和帽高，但 core 半径仍为 .38，角场取圆；共享 mean 差恰为零，只留下真正的核心周长差与当前角场。这不是把旧 R611 圆面证书转给新圆面。该新圆面的完整两 jets、正则性、真实曲率、z_s 条件、全法弦与 reach 均须在新公开 Actions scope 中真实支付；若正 z_s 等条件失败，就没有 R599 结论。R611 v2 `CompactGeometry` 对象在这里仅提供相同解析 H 的已实现有向积分方法，不提供新参考的曲率或全几何资格。

记 `b=chi_bg`、`r=rc+L-s`、`c=core_half+s`，`alpha` 和 `z_corr` 为完整原控制场，则

\[
a=e^\alpha((1-b)a_{\rm core}+br),\qquad
z=(1-b)c+b(H_q+H(s))+z_{\rm corr}.
\]

源码用乘积法则得到 a 的值、一阶、二阶；高度为

\[
\begin{aligned}
z_s&=1-b+b_s(H_q+H-c)+b w+(z_{\rm corr})_s,\\
z_{ss}&=-2b_s+b_{ss}(H_q+H-c)+2b_sw+bw_s+(z_{\rm corr})_{ss}.
\end{aligned}
\]

这里 `H_s=w`、`H_ss=w_s` 是**完整解析积分**的真实导数。核心 `[0,C]` 使用准确 `a=a_core,a_s=a_ss=0,z=core_half+s,z_s=1,z_ss=0`。跨 C 的区间必须先细分，不查询本来不参与 core 公式的外延高度。

## 2. 无限振荡尾不被数值零 suffix 截断

令 `delta=(L-s)/ell`，同一原场为

\[
w=A\exp\!\left(-\frac{2-\sin(\delta^{-2})}{\delta}\right),\qquad
H(s)=-A\ell\int_0^\delta
\exp\!\left(-\frac{2-\sin(t^{-2})}{t}\right)dt.
\]

在紧段，接口调用 hash 绑定的 R611 v2 `exact_tail_height`，即其 `A*ell` 系数先进入区间再相乘，保留已修复的求积 prefactor。w 与 w_s 由同一解析式直接向外求值。

若 `0<=delta<=h<=.08`，则

\[
\begin{aligned}
0\le w&\le A e^{-1/h},\\
|w_s|&\le\frac A\ell e^{-1/h}
       \left(3h^{-2}+2h^{-4}\right),\\
-A\ell h e^{-1/h}\le H&\le0.
\end{aligned}
\]

证明：`2-sin` 介于 1 和 3，`|cos|<=1`；对 `j=2,4`，`e^{-1/delta} delta^{-j}` 在 `delta<=.08<1/j` 上递增，因而可取右端 h。积分用正被积函数的上界。`delta=0` 由平坦极限给出零两 jets。

这些界覆盖**所有**内侧振荡，不执行高频相位采样，也不把高度、w 或 w_s 定义为零。改变的只是包络方式；材料 seed 的独立数值零 suffix 不改变 H 的数学定义。紧段/尾段范围跨越而尚不满足任何一条时，接口要求细分，不丢弃区间。

## 3. 直接同场差 jets 保留准确抵消

`boxes(left,right,current_core_radius)` 返回 `current`、`reference` 各六个区间，并额外给 `difference` 的准确同场差值包络。

共享的 H、固定 mu/nu 和中央 z 在差中可以**代数相消**；独立地做两个宽高度区间之差则会损失这一相关性。若 `Delta H_q` 是两个最后坐标的准确有理差，`Delta z_corr` 是原八个 height 系数差形成的同一 beta-spline，则

\[
\Delta z^{(k)}=b^{(k)}\Delta H_q+(\Delta z_{\rm corr})^{(k)},\qquad k=0,1,2.
\]

半径取 `Delta alpha` 为八个 alpha 系数的准确有理差形成的同一 beta-spline；固定 mu 消去。记参考 radius 为 a0、当前完整指数为 alpha1，`Delta abase=(1-b)(a_core1-a_core0)`，则

\[
\Delta a=a_0(e^{\Delta\alpha}-1)+e^{\alpha_1}\Delta a_{\rm base}.
\]

源码对这个恒等式也取同一乘积两 jets；若八个 alpha 坐标逐值相同，第一项准确删去，不把 `exp(0)-1` 的浮点取消误差当成实际扰动。形成系数差时先用 `Fraction` 保留两个原 binary64 参数的准确差，再向外转换，未先做一个未认证的普通减法。

因此 R604 driver 可以直接消费 `difference` 的六 jets 来计算 `da,das,dass,dz,dzs,dzss`，并继续使用 `current/reference` 各自区间计算真实连接系数和乘子。这些差是原精确曲面的代数差，不是从样本拟合出的新场。若 driver 仍独立相减各个区间，结果保持有效但可能更宽。

## 4. 帽、柱与使用范围

两块开圆盘的半径相同 rc，材料 Cartesian 坐标相同，只相差准确帽高 `Delta H_q`；其全域位移界为 `|Delta H_q|`，一阶差和参考协变二阶差都为零。`cap_disk_difference()` 仅报告这两个实际盘的范数，不把任何正宽度 body 环带替换成盘。原 C² 平坦接缝已在材料接口说明。中间柱使用 body 的准确 s=0 core 角圈及原直线 z；下半面用原镜像。

上述接口本身不宣布完整覆盖、嵌入或 reach。新的公开 Actions scope 必须核同一 q/mesh，处理完整材料分片与需要的细分，记录新成本，再将全角 u/v、当前/参考六 jets 及其精确差接至 R604。无限 kernel 的 DtN/ODE/C² 误差、固定 g 等距族与 README 宏观完成门仍保持原范围。

本地仅做 AST 与两条源码 hash 绑定检查，没有调用高度积分、区间科学、ODE 或优化。
