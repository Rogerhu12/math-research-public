# R119：五函数全盒控制下的公共径向有限阶逆

2026-11-14，visible-exact-astra-ac0d。

**已证明。** [全尺度五函数有限盒定理](R119-supplement-all-scaled-five-function-finite-box-generator.md)给出的完整正定 generator，使同一原允许族中的一次公共选择满足

\[
\boxed{\quad
 \|(I-U_M)^{-1}\|_{\ell^2\to\ell^2}
 <2^{175007}d_M M^{1893}<2^{175007}M^{1894}.
\quad} \tag{F.1}
\]

频率范围仍为原完整径向网络的 $M\in4\mathbb N$、$M\ge M_*>2^{984}$；端口仍是全部原 canonical incoming 单位。以前的局部双侧角权、固定接线及概率余量同时保留。该结论加强在原允许族中的存在选择，不把此前任意数值 profile 自动升级为这个选择。

## 1. 新 generator 接入原完整网络

沿用[公共径向逆定理](R119-supplement-common-radial-polynomial-resolvent-in-original-port-units.md)的真实网络、$\mathcal I_M$、$d_M=2|\mathcal I_M|$、固定接线 $P_M$、原补偿约束及谱平均。现将每层每个实际 dyadic band 的方向和完整半径换为全盒五函数定理 (B.9)–(B.17) 及其最终结论中的已经付费的方向与半径。每个坐标的实际幅度包含 $r_U/N_{j,U}$，不删去频率数或补偿 Hessian。

同一个 $\theta_M\in[-1,1]$ 同时作用于所有 $j\in\mathcal I_M$，其它频率坐标固定。所有变化支撑在各 retained negative window 内；完整两端相位仍由原两个补偿 bump 精确保留。正段、两端原允许线、其端口单位和 normal shear 对这一坐标固定，因此仍准确有

\[
U_M=P_M\bigoplus_{j\in\mathcal I_M}S_{j,M},\qquad
\partial_{\theta_M}P_M=0,
\]
\[
-iU_M^*\partial_{\theta_M}U_M
 =\bigoplus_j(-iS_{j,M}^*\partial_{\theta_M}S_{j,M})
 \ge D_M>a_M^0 I,
\qquad a_M^0=2^{-175000}M^{-1891}. \tag{F.2}
\]

新全盒定理已对所有实际 $\kappa=M/\sqrt B$ 证明 (F.2)，包括低尺度窗口、全部其它坐标同时变化和两补偿的非线性影响；没有把局部中心处的导数当作整个盒的下界。一阶上界也保留真实新半径：全盒定理给 $r_U=d_U/[2^{36}K_j^6(U+B)^2]$ 和 $d_U<2^{-22050}/U$。将原完整散射一阶界宽放为 $2^{10}K_j^2(U+B)$，乘以实际幅度 $r_U/N_{j,U}$ 后严格小于 $2^{-26}d_U/[N_{j,U}K_j^4(U+B)]<2^{-22076}<2^{-33}<1/8$。完整直和 generator 取各块范数上确界，不另乘窗口数。真实 high 前缀、无限 low 尾、正段和仿射源仍通过原准确消元留在网络及右端。

## 2. 一次公共选择及准确次数

令 $a_M=\min_j D_{j,M}>a_M^0$、$\varepsilon_M=(128d_MM^2)^{-1}$，在原谱平均中取

\[
\xi_M=a_M\varepsilon_M,\qquad
L_M=1+\log(512d_MM^2/a_M),\qquad
\mathcal T_M=128d_MM^2L_M. \tag{F.3}
\]

已证完整酉路径谱平均同时保留

\[
\operatorname{dist}(1,\sigma(U_M))\ge\xi_M,
\qquad
\|D_M^{1/2}(I-U_M)^{-1}D_M^{1/2}\|\le\mathcal T_M,
\]

条件坏集概率小于 $1/(32M^2)$。重根由其完整 eigenspace 上的正定 generator 控制，不需要其它 eigenphase 的最小间距或二阶导数。正规性立即给

\[
\|(I-U_M)^{-1}\|\le\xi_M^{-1}
 <128d_MM^2(a_M^0)^{-1}
 =2^{175007}d_MM^{1893}. \tag{F.4}
\]

原全部频率范围已经证明 $d_M<M$，所以得到 (F.1)。这里的次数变化准确为 $1891+2+1=1894$，没有再为一个任选 rank-one 向量支付两端口条件数。

对所有 $M$ 和外 bump 参数取原产品测度。条件估计在整个其它参数盒上统一成立，因此原 Fubini 论证、可数求和及原 good-$t$ 条件仍给联合好集测度

\[
>1-\sum_{M\in4\mathbb N}\frac1{32M^2}-\frac{83}{16384}
>1-\frac{147}{16384}>0. \tag{F.5}
\]

存在同一个完整 profile 与同一个 $t$，同时满足全部频率结论。原闭条件和乘积紧性也保留按坐标最小值准确指定该选择的方式；这不声称已经计算了一个无限参数数组。

## 3. 原局部角权仍由同一个选择满足

记原层号 $J=j+5$。原真实范围给 $\log M<1024J$、$J\ge8198$。新的有限常数满足

\[
175000<512\cdot8198,\qquad
1891\cdot1024+512=1936896<2^{21}.
\]

因此

\[
-\log D_{j,M}<175000+1891\log M<2^{21}J
<2^{-800}Mh_j. \tag{F.6}
\]

最后一步仍是原层号分块比较；原证明已支付更大的 $2^{25}J$。同样，写 $\log_2M=984+q+r$、$0\le r<1$，则

\[
175000+985\cdot1891=2037635<2^{21}
\]

保证 $-\log a_M<M/4$。于是原 $L_M<2M$、$\mathcal T_M<256M^4$ 和 $\log\mathcal T_M<2^{-803}Mh_j$ 不变。对原权

\[
W_M=\operatorname{diag}_j(e^{2^{-800}Mh_j}I_2)
\]

仍有 $W_M^2\ge\mathcal T_M D_M^{-1}$，故同一选择满足

\[
\|W_M^{-1}(I-U_M)^{-1}W_M^{-1}\|\le1. \tag{F.7}
\]

没有重定义原标签、源权、端口归一化或角解析宽度。

## 4. 全端口源映射和剩余物理问题

用原完整端口范数

\[
\|g\|_{\sigma,s}^{\rm port}
=\sum_{M\in4\mathbb N,\ M\ge M_*}
 e^{\sigma M}M^s\|g_M\|_{\ell^2(\mathbb C^{d_M})},
\]

则只要右侧有限，完整径向网络解唯一，且

\[
\boxed{\quad
\|x\|_{\sigma,s}^{\rm port}
\le2^{175007}\|g\|_{\sigma,s+1894}^{\rm port}.
\quad} \tag{F.8}
\]

角宽 $\sigma$ 完全保留，负频率按真实共轭处理。对**已经证明转成原 $N_M$ 单位的完整端口列**，原界 $N_M<C_\zeta e^{-\tau_\infty M}M^{-30960}$ 与 (F.1) 合并后剩余次数为

\[
30960-1894=29066,
\qquad
\|x_M\|<2^{175007}C_\zeta e^{-\tau_\infty M}M^{-29066}. \tag{F.9}
\]

常数 $2^{175007}C_\zeta$ 保留。任意 ordinary/weak 物理源、标签取值泛函和总通量源仍须证明其真实 source-to-port 转换；不能因为 (F.9) 有很大多项式余量就免除材料密度、Jacobian、端荷、normal shear 或全物理重建。零模和 $M<M_*$ 的巨大有限频段仍走各自的完整方程。

此处是径向网络的结论。实际非径向背景下的混频簇、完整参数端图导数和全源算子还须继续；不能把绝对扰动直接除以 (F.2) 的小间隙而宣称完成。非线性精确解和最终闭曲面族均未由本篇获得。

## 5. 新有限预算

[新预算源码](../scripts/fourfold_five_function_common_radial_resolvent.py)只计算本篇新常数、次数和原单位源列的剩余幂，并绑定两篇实际输入定理的 SHA256。它不重跑旧公共网络证明的 31 个既成门，也不以有限频率样本替代上述无限范围证明。[实际原生报告](../notes/2026-11-14-R119-five-function-common-radial-resolvent-budget.json)记录真实执行结果。
