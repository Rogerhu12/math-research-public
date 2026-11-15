# R198：最右单 profile 段上的第四 period 对全部二阶 gauge 不变

日期：2026-11-15。完整纸面必要条件；没有新的 profile 积分、原式编译或几何研究计算。

来源：[R56 真实右锚恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R180 非零第三 hook](R180-fixed-circle-invisible-third-hook-and-signed-fourth-period-gauge.md)、[R181 原周期算子](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md)、[R183 导数分包圆](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R184 完整 joint 判据](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)，以及 [R193 冻结八包](R193-full-width-positive-obstruction-for-frozen-eight-derivative-packets.md)。

R181 已表明：f 在某开区间常值时，任意二阶齐次 gauge 只能在该区间改变第四 period 的仿射部分。本稿利用 R183 的一个更强、具体的右端结构：最右 g 下降段位于 f 的全部支撑右方。在该处 gauge 连仿射部分也不能改变；原完整 period 准确退为同一真实几何上一条纯四次单 profile 原根。

## 1. 固定几何、目标与允许改动

固定 R180/R183 或 R197 的一条真实闭 hook 几何 B，使用共同紧物理区间 $I=[l,r]$、右 collar 和同一个全局 s 起点。其全算子满足

$$
M_B=0,\qquad T_B=\kappa\mathfrak H,\qquad \kappa\ne0.
\tag{1}
$$

固定同一个第一圆及同一个目标：

$$
\phi_\theta=\cos\theta f+\sin\theta g,\qquad
g_\varepsilon=g_X+\varepsilon^2(dY_f)^2.
\tag{2}
$$

假设原 canonical 二、三阶恢复已经通过完整 range。记原第四 period 为 $V_\theta^0$。

允许 R184 中的任意全 I 二阶齐次 profile 家族 $w_\theta$，只要求其改动真实合法、相位光滑周期并保指定种子；不要求 w 支撑在一个包内，不把六条充分矩条件误作必要限制。也允许全部合法第三齐次改动。

R180/R184 的真实传递恒等式是

$$
\boxed{\widetilde V_\theta
=V_\theta^0+2\kappa L_f(w_\theta),\qquad
L_f(w)=\mathfrak H(w;f,f).}
\tag{3}
$$

整个 M=0 已消掉 gauge 平方及第三齐次项的周期贡献。第四 forcing 和 ruling 中这些项仍存在。

## 2. 在 f 支撑右方，完整响应严格为零

设 $b<r$ 满足

$$
f|_{[b,r]}=0.
\tag{4}
$$

R181 的同右锚原式为

$$
\begin{aligned}
L_f(w)(x)={}&-3w'(x)f''(x)^2
-\int_x^r w''f''^2\\
&+6\int_x^r(\eta-x)w''f''f'''
-6\int_x^r w''f'f'''.
\end{aligned}
\tag{5}
$$

因此对每个 $x\in[b,r]$，全部积分的被积函数及局部项都准确为零，无论 w 在 I 其他地方如何取值。故

$$
\boxed{L_f(w)|_{[b,r]}=0
\quad\text{对任意光滑全 I profile }w.}
\tag{6}
$$

这比一般常平台上的 $L_f(w)''=0$ 强。一般平台可能接收到其右方 f 包的仿射尾；这里整个右锚区间都没有 f，故不存在该尾，不能把两种情形混淆。

由 (3) 得到完整固定目标不变量

$$
\boxed{\widetilde V_\theta|_{[b,r]}
=V_\theta^0|_{[b,r]}.}
\tag{7}
$$

特别地，存在任何允许的二、三阶 gauge 使第四 range 成立，都必须有 $V_\theta^0=0$ 于此区间、对全部相位。单点准确非零即足以排除全部这些 gauge，而不只是 R195 的单边支撑子空间。

## 3. 右因果只涉及 profile 坐标，不删除 s 历史

R56 的 canonical 恢复由以下操作组成：固定 $\xi$ 的局部 profile 微分、乘法、同右锚 Volterra 原函数，以及从同一全局起点累计的真实 s 历史。几何系数、frame、实际 ds 和路径长度全部固定。

所以若两组输入 profiles 在 $[b,r]$ 一致，则它们的所有 canonical 二、三阶场、第四 forcing 及 period 在 $[b,r]$ 一致。证明按恢复阶数归纳：局部操作只读当前右区间，$\int_x^r$ 只读该右区间，而各 s 历史的初值相同、右端函数也相同；于是对全部 s 的累计值相同。

这不是把累计 second/third 历史设零。只要当前右区间的输入不为零，其沿整条 B 的历史仍完整保留。也没有在各几何段、各 profile 包或查询点重新选锚。

由此，在 (4) 的区间中，原问题可以准确用 f=0 的右端输入计算，尽管原固定目标在整个 I 上仍由非零 f 给定。

## 4. 一条纯四次原根及准确相位因子

记 $Z_B(q,q)$ 为 $H(Y_q,Y_q)$ 的 canonical second 恢复，再记

$$
U_B(q)=\mathcal I_B H(Y_q,Z_B(q,q)),
\tag{8}
$$

其中 $\mathcal I_B$ 使用同一个真实右锚和全局 s 起点。定义纯四次 period 原根

$$
\boxed{\mathcal P_B(q)=
\mathscr P_B\bigl(
-H(Z_B(q,q),Z_B(q,q))
-4H(Y_q,U_B(q))
\bigr).}
\tag{9}
$$

(8)、(9) 是原 canonical 算子的定义，不先要求单个 q 的全左 collar/ruling 已付。它们作为真实右锚形式恢复始终有定义；本稿只在其与已合法全圆场一致的右区间使用。

在 $[b,r]$，置 $s_\theta=\sin\theta$。因为 f 及其全部右端资料为零，

$$
Y_{\phi_\theta}=s_\theta Y_g,\qquad
Z_\theta=-s_\theta^2Z_B(g,g).
$$

第三 forcing 是 $-2H(Y_{\phi_\theta},Z_\theta)$，因此其同锚恢复为

$$
W_\theta=2s_\theta^3U_B(g).
$$

将它们代回完整第四 forcing，即得

$$
\boxed{
V_\theta^0(x)=\sin^4\theta\,\mathcal P_B(g)(x),
\qquad x\in[b,r].
}
\tag{10}
$$

该身份保全部历史和所有第四交叉项，不是仅提取一个常段的最高次数。

于是 (7) 的必要条件准确缩成

$$
\boxed{\mathcal P_B(g)|_{[b,r]}=0.}
\tag{11}
$$

只需取 $\theta=\pi/2$ 即得必要性；反过来，(11) 恰好支付本区间全部相位的 period 门，仍不支付其左方或任何第四 ruling。

如果沿用既有 $\zeta=e^{-i\theta}$ 模式规范，则此区间的三个原模式满足

$$
\boxed{
V_{-4}^0=\frac{\mathcal P_B(g)}{16},\qquad
V_{-2}^0=-\frac{\mathcal P_B(g)}4,\qquad
V_0^0=\frac{3\mathcal P_B(g)}8.
}
\tag{12}
$$

这是 $\sin^4\theta=(3-4\cos2\theta+\cos4\theta)/8$ 的准确系数。因此不需要重新生成两套 mixed 原根；已有的纯第四原根乘 16 就是本门的完整输入。

## 5. R193 冻结八包在最右端只剩一个有理下降 step

R193 的基础矩形使用

$$
\rho(t)=51480t^7(1-t)^7,\qquad
S(t)=\int_0^t\rho(v)\,dv\quad(0\le t\le1),
$$

在左、右侧分别延为 0、1，并取

$$
f_0(x)=S(x-8)-S(x-12),\qquad
g_0(x)=S(x-10)-S(x-14).
$$

三个补矩 bump 在矩形左方。八个平移包为 $x\mapsto x-20j$，幅度满足

$$
a_j^3=(-1)^j\binom7j.
$$

最后一个 $a_7=-1$。故在未窄化坐标中，全部 f 支撑位于 $x\le153$，而最右 g 下降发生在 $154<x<155$。对全部 $x>153$，

$$
\boxed{
g(x)=-\{1-S(x-154)\},\qquad f(x)=0.
}
\tag{13}
$$

右侧 $x\ge155$ 时二者为零。所有其他七包和三个左补矩，在该右端问题中都不出现。若把 (13) 单独作为原算子输入，可在 b 左方任取一个紧支撑延拓以保持左 collar；不同延拓在所研究右区间的值完全相同。没有把左方的常值延伸到整个 I 后误称为紧支撑 profile。

共同缩放宽度 $\lambda>0$ 后，对 $x>153\lambda$，

$$
\boxed{
g_\lambda(x)=
-\{1-S(x/\lambda-154)\},\qquad f_\lambda(x)=0.
}
\tag{14}
$$

若圆另有统一非零实归一化系数 a，则 (9) 只多乘 $a^4>0$；零与非零判定不变。最后包的负号也因四次齐次而不改变此判定。

因此冻结八包的这项必要 period 门，实际上只需要一个有理 C7 下降 step。没有 $\sqrt[3]7,\sqrt[3]{21},\sqrt[3]{35}$ 系数，也不需要重新积分左补矩或原八包。把右锚放在任意更靠右的原零 collar，结果相同。

仍须保持几何的共同物理区间能容纳实际支撑；(14) 不授任意 $\lambda$ 都能放入一个预给的固定 I。

## 6. 真正光滑圆的对应必要条件

R183/R193 的 C-infinity 实现保留各转换带的严格分离。只要平滑足够小，最后 f 转换带的右端仍严格位于最后 g 下降带的左端。令 b 选在两者之间，则 (4)--(12) 原封不动成立。

这时 (13)、(14) 中的 S 改为选定的真正光滑 step。我们没有把 C7 多项式原型冒称为已经光滑，也没有把某个多项式输入上的零恒等式自动转移到平滑后的输入。

若后续在 C7 原型的一个严格内点得到准确非零值，则固定真实几何下，相关有限阶右锚恢复和 period 对足够高阶 profile 拓扑连续；保支撑分离与准确矩补偿的充分小 C-infinity 扰动仍有该非零值。这是可以支付严格排除的方向。反之，原型上为零不提供这种开放性。

## 7. 最小后继目标及当前未付判断

本稿得到的是完整必要条件 (11)，尚未证明任何特定真实 B 的该原根为零或非零。R196 的 canonical 正字符作用于 universal 函数空间；除非另证它能通过此固定单 profile 右端限制分解，不能直接把其正值代成 $\mathcal P_B(g)$ 的非零证明。

后继只需消费已经定义的纯四次原根 (9)，输入 (14) 的单个右下降 step，并保整条 B 的实际 s 历史。可以对同一原根检查一个准确非零函数值，或其在下降段上的完整多项式系数；不需要重编原第四 forcing、不需要重新配八包，也不需要重跑既成的 R193 ruling 门。

若尚未冻结一条具体 B 的实际控制，则必须明确把目标写成原函数的符号限制、或先选定新的真实路径；不能用一个未指定的“典型几何”给出数值结论。若使用 universal 商上的原式关系，也必须保全部真实成本方向，不能仅因一个纯幂尾投影曾为零便宣 (11) 自动成立。

综上，这是一项对全部允许二阶 gauge 都不可改变的固定圆 period 门，覆盖有常段和无开常段的 hook 几何。它没有支付左侧 period、joint ruling、无限阶、收敛、嵌入或 reach。

