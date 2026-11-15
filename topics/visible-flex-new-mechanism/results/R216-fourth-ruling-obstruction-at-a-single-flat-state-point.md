# R216：常状态第四 ruling 障碍已在一个四阶平点出现

日期：2026-11-15。作者及推导责任：tail_cost；root 阅读后登记。**完整纸面证明；没有新的 profile 求积、原式编译或几何计算。**

来源：[R49 常段最高项](R49-fourth-ruling-leading-coefficient-and-narrow-packets.md)、[R53 完整复相位系数](R53-overlapping-profile-fourth-leading-gate-existence.md)、[R54 常状态迁移](R54-constant-state-helicoid-transfer-and-first-ruling-gauge.md)、[R56 真实变系数递推](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R184 全部二、三阶 gauge 的联合 range](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R187 窄化障碍](R187-narrow-derivative-packet-circle-constant-state-obstruction.md)、[R193 原八包的全宽度正性](R193-full-width-positive-obstruction-for-frozen-eight-derivative-packets.md)及 [R214 无开常段 pure 零闭 hook](R214-nowhere-constant-closed-hook-with-exact-universal-pure-zero.md)。

本稿指出一个比“有没有开常段”更局部的必要门。对当前光滑形式恢复，第四 ruling 的二阶 s jet 只需要几何状态至四阶 jet。若一个点的这些状态 jets 与常状态相同，则该点已经保留常段的整个二次最高项，任意真实入历史和允许的二、三阶齐次 gauge 都不能改变它。

因此，R214 去掉开常段并没有绕过 R187/R193 的这一障碍。R214 的 pure 控制及闭 hook 定理仍成立；它本来没有宣称完整第四 ruling 可解。本稿精确收紧其用于原冻结 profile 圆的后续范围。

## 1. 固定数据与“四阶平点”

沿真实几何使用同一 s 参数、同一物理 profile 区间 $I=[\ell,r]$，并保持

$$
h>0,\qquad \xi+\omega(s)>0,\qquad
\omega_s=\frac{k_s}{2h}.
\tag{1}
$$

所有 profiles 使用同一个右端 r 的 Volterra 锚。设第一圆为

$$
\phi_\theta=\cos\theta\,f+\sin\theta\,g,
$$

目标固定为 $g_X+\varepsilon^2(dY_f)^2$。假设至第三阶的真实周期、双 collar range 已付，允许 R184 的全部光滑相位二阶 gauge 及全部第三阶齐次 gauge。本稿不把二阶 gauge 限制为有限模板、六个充分矩条件或某个固定相位谐波。

称一个点 $s_*$ 为状态的**四阶平点**，若

$$
h^{(j)}(s_*)=k^{(j)}(s_*)=0,
\qquad 1\le j\le4.
\tag{2}
$$

由 (1)，同时有

$$
\omega^{(j)}(s_*)=0,\qquad 1\le j\le4.
\tag{3}
$$

这里不要求任何邻域的状态恒定。特别，全正阶 jets 为零的光滑拼接点满足 (2)，即使它附近没有任何常状态开区间。

记该点状态为

$$
(h_*,k_*,\omega_*)=(h(s_*),k(s_*),\omega(s_*)).
$$

用这一状态建立一个仅用于比较 jets 的冻结常状态模型；它不是对真实几何插入常段，也不是另一条待选物理路径。

## 2. R56 递推所需的有限 jet 阶数

用 R56 记号，将每个场写成

$$
Z_i=F\,V_i/z,\qquad z=\xi+\omega,\qquad
\nabla_sV_i=(V_i)_s+\Omega(k)V_i.
$$

对于已知场的对称双线性 forcing，定义

$$
J=\sum C_{ij}V_i\cdot V_j,\qquad
T_\xi=\sum C_{ij}(V_i)_\xi\cdot(V_j)_\xi.
$$

完整 ruling 是

$$
\mathscr K(H)(s)
=\frac1{h(s)}\int_I T_\xi(s,\xi)\,d\xi.
\tag{4}
$$

它不需要先求第四阶恢复场。对当前第四 forcing，只用第二、第三阶场即可评价 (4)。

R56 的恢复仍保留

$$
B=\frac J{2h},\qquad
P=-\frac1{2h}\int_r^\xi T_\xi(s,\eta)\,d\eta,
$$

$$
\begin{aligned}
\mathcal R_H={}&\frac{T_s}{2h^2}
+\left(kz^2-\frac{k^2+1}{h}z\right)P
-\frac{h_sz-h\omega_s}{h^2}P_s\\
&+\left(kz-\frac{k^2+1}{h}\right)B
-\frac{h_s}{h^2}B_s,
\end{aligned}
\tag{5}
$$

$$
\eta_0=-\frac{T_{s\xi}}{2h}
+\frac{h_sz-h\omega_s}{2h}P_\xi
+\frac{h_s}{2h}B_\xi-\frac12P_s,
\tag{6}
$$

$$
W_s=\mathcal R_H,\qquad
A=\frac12W_\xi+\frac{\eta_0}{h},\qquad
V_{\rm new}=(A,zP+B,(hz-k)A-hW).
\tag{7}
$$

以上是完整逐点公式，未删除 s 总导数或任何原函数尾。

为避免把积分历史当局部几何函数，分别记二、三阶 characteristic 历史为 $W_2(s,\xi)$、$W_3(s,\xi)$；它们在 $s_*$ 的整个 profile 值保持为真实入值。对有限个相位通道逐一使用同一记号即可。

从 (5)–(7) 直接得到下表。表中的“状态阶数”只计算 h、k、omega 的最高 s 导数；W 的真实值另外保留，W 的 s 导数必须由自身 ODE 代入。

| 对象 | 所需最高状态阶数 | 保留的真实历史 |
|---|---:|---|
| 第一阶分子 $V_1$ | 0 | 无 |
| 二阶 $\mathcal R_2$ | 1 | 无 |
| 二阶分子 $V_2$ | 1 | $W_2$ |
| 三阶 $\mathcal R_3$ | 2 | $W_2$ |
| 三阶分子 $V_3$ | 2 | $W_2,W_3$ |
| 第四 ruling $\mathscr K_4$ | 2 | $W_2,W_3$ |
| $\partial_s^2\mathscr K_4$，消去历史的 s 导数后 | 4 | $W_2,W_3$ |

逐行理由如下。

第一阶分子是

$$
V_1(\phi)=\left(-\frac{\phi'}2,\ 0,\
h\phi-(hz-k)\frac{\phi'}2\right).
\tag{8}
$$

它只含状态零阶。由第一阶平方或极化形成的 P、B 也只含零阶；$T_s,T_{s\xi},P_s,B_s$ 至多含一阶。因此二阶 $\mathcal R_2$ 与恢复中的 $\eta_{0,2}$ 至多含状态一阶，$V_2$ 另含真实 $W_2$。

第三 forcing 是第一、第二阶场的双线性配对。P、B 至多含一阶与 $W_2$；它们的一次 s 微分，以及 $\nabla_sV_2$，至多含二阶与 $(W_2)_s$。以 $(W_2)_s=\mathcal R_2$ 代入，得到三阶两行。

第四 ruling (4) 只涉及 $V_2,V_2$ 及 $V_1,V_3$ 的 xi 导数，不引入新的 s 微分。因此它至多含二阶状态。再取两个 s 导数最多到四阶；所需 $(W_2)_s,(W_2)_{ss},(W_3)_s,(W_3)_{ss}$ 分别用 (5) 及其一次导数代入即可，不产生新的独立历史常数。

这给一个明确充分的四阶 jet 上界。本文不声称每个最高阶项都不发生进一步相消，也不声称四阶条件是最弱可能假设。

## 3. 同右锚、同真实入值的 jet 冻结引理

在 $\sigma=s-s_*$ 的冻结模型中，固定 h、k、omega 为 $h_*,k_*,\omega_*$。令其 frame 从真实 $F(s_*)$ 出发，按常矩阵 $\Omega(k_*)$ 演化。把其二、三阶 characteristic 初值规定为

$$
\widehat W_2(0,\xi)=W_2(s_*,\xi),\qquad
\widehat W_3(0,\xi)=W_3(s_*,\xi).
\tag{9}
$$

冻结模型与真实模型采用同一 profiles、目标、右锚 r，并用 (5)–(7) 递推。没有把 (9) 设为零，没有逐包重置原函数，也没有假设这些初值与几何控制无关。

**引理。** 若 (2) 成立，则真实第四 ruling 与这个冻结模型满足

$$
\boxed{
\partial_s^j\mathscr K_4(s_*,\theta)
=
\partial_\sigma^j\widehat{\mathscr K}_4(0,\theta),
\qquad j=0,1,2.
}
\tag{10}
$$

**证明。** 状态四阶 jets 相同，使 (8) 的 s jets 至四阶相同。由 (5) 的二阶 forcing 版本，$\mathcal R_2$ 的 jets 至三阶相同；结合 (9)，$W_2$ 的 jets 至四阶相同。由 (6)–(7)，$V_2$ 的 jets 至三阶相同。

三阶 $\mathcal R_3$ 的 jets 至二阶于是相同；结合第二个初值 (9)，$W_3$ 的 jets 至三阶相同。三阶恢复中只再出现一次已有场的 s 微分，故 $V_3$ 的 jets 至二阶相同。

最后将 $V_2,V_1,V_3$ 代入 (4)，即得 (10)。固定 I 上的 xi 微分、同锚积分与上述有限 s 微分可交换。两模型的旋转 frame 在点积中完全消去；若直接比较空间场，frame ODE 给出的相同 jets 也产生同一结论。$\square$

这个引理是对真实递推的有限 jet 比较，不是用常段多项式拟合一般变系数函数。冻结模型只需在 $\sigma=0$ 的邻域作为准确恢复表达式存在；不为它额外声称整圈闭合或重新支付第三 range。

## 4. 冻结模型的二次项与任意入历史无关

固定相位，记常状态上的对称 characteristic 双线性算子为 $\mathcal R_*$，ruling 双线性能量为

$$
E_*(a,b)=\int(Y_a)_u\cdot(Y_b)_u\,du.
$$

设

$$
R_\theta=\mathcal R_*(f,f)
-\mathcal R_*(\phi_\theta,\phi_\theta).
\tag{11}
$$

R49 的完整恢复说明，保任意真实二阶入值后，二阶场在旋转标架中的精确最高项为

$$
\widehat Z_\theta
=-\sigma Y_{R_\theta}+O_{\le0}(\sigma).
\tag{12}
$$

这里 $O_{\le j}$ 表示次数至多 j 的准确标架多项式，不是渐近误差。二阶 normal 分量与 $\sigma$ 无关。

由第三 forcing $-2H(Y_{\phi_\theta},Z_\theta)$ 的一次项，第三场的最高项为

$$
\widehat U_\theta
=-\sigma^2Y_{\mathcal R_*(\phi_\theta,R_\theta)}
+O_{\le1}(\sigma).
\tag{13}
$$

初值 (9)、真实 normal 恢复及任意第三齐次 profile 全部只进入较低次数。因此

$$
\widehat{\mathscr K}_4(\sigma,\theta)
=c_0(\theta)+c_1(\theta)\sigma+K_*(\theta)\sigma^2,
\tag{14}
$$

其中

$$
\boxed{
K_*(\theta)
=-E_*(R_\theta,R_\theta)
+2E_*\!\left(
\phi_\theta,\mathcal R_*(\phi_\theta,R_\theta)
\right).
}
\tag{15}
$$

这里 $c_0,c_1$ 可以依赖全部真实历史；$K_*$ 不依赖它们。

对于任意允许的二阶 gauge $Y_{w_\theta}$，(12) 只改变常数项。其真实第三补偿是 R184 的 $2Z_B(\phi_\theta,w_\theta)$，在冻结模型至多一次；第三齐次 profile 是常数项。因此所有二、三阶 gauge 都不改变 (15)。这一断言对每个相位分别成立，所以也覆盖任意光滑相位家族，不依赖有限谐波截断。

结合 (10)、(14)，得到本稿的核心身份：

$$
\boxed{
\partial_s^2\mathscr K_4(s_*,\theta)
=2K_*(\theta)
}
\tag{16}
$$

对任何同一第一圆、同一目标和任意合法二、三阶 gauge 的第四 forcing 成立。

## 5. 单点 jet 给出真实 joint 商障碍

R184 的三矩几何像是

$$
\mathcal W=
\{\mathbf w(s)\cdot v:v\in\mathbb R^3\},
$$

$$
\mathbf w(s)=
\left(
\frac{(h\omega-k)^2+1}{4h},\
\frac{h\omega-k}{2},\
\frac h4
\right).
\tag{17}
$$

在 (2) 下，$\mathbf w''(s_*)=0$。所以固定线性泛函

$$
\Lambda_{s_*}:C^\infty(S^1_s)\longrightarrow\mathbb R,
\qquad
\Lambda_{s_*}(a)=a''(s_*),
\tag{18}
$$

准确杀掉整个 $\mathcal W$，因而下降为 ruling 商空间上的真实泛函。

它也杀掉 R184 全部二阶线性 ruling 响应 $\mathcal B_\theta(w)$。这是 (12) 的同一次数论证：冻结模型中的

$$
2\int Z_{\theta,u}Y_{w,u}\,du
-4\int Y_{\phi_\theta,u}Z_B(\phi_\theta,w)_u\,du
$$

至多一次。由第 3 节的 jet 比较，其真实二阶 s 导数在 $s_*$ 仍为零。gauge 平方和第三齐次项已在 (17) 的像中，也被 (18) 消去。

故完整联合 range 存在的必要条件为

$$
\boxed{K_*(\theta)=0\quad\text{对全部 }\theta.}
\tag{19}
$$

这一门只用一个四阶平点，无需常状态开区间。即使整个第四 period 已被某种办法清零，只要 (19) 失败，仍不可能用同一或其他合法 w 支付第四 ruling。

## 6. 标准平点上的原八包全宽度排除

现取

$$
(k_*,h_*,\omega_*)=(0,1,0).
\tag{20}
$$

R53 用 $q=f+ig$、$\zeta=e^{-2i\theta}$ 把 (15) 写成

$$
K_*(\theta)
=K_0+\operatorname{Re}\{\zeta K_2+\zeta^2K_4\},
\qquad
K_4=-\frac18\mathcal F(q).
\tag{21}
$$

这里使用普通复双线性乘法，所有“复幅”都按 (21) 的 $\operatorname{Re}$ 约定，而非把它和单个 Fourier 系数混用。由 (16)，二阶 s jet 的 $e^{-4i\theta}$ 复幅为

$$
\boxed{-\frac14\mathcal F(q).}
\tag{22}
$$

因此它必须为零。

R193 对**同一个冻结原八包**、仅改变共同宽度的

$$
q_\lambda(x)=q_{\rm raw}(x/\lambda)
$$

已经准确证明

$$
\lambda^7\operatorname{Re}\mathcal F(q_\lambda)
=c_0+c_2\lambda^2+c_4\lambda^4+c_6\lambda^6,
\qquad c_j>0.
\tag{23}
$$

四个系数的完整实代数值及 16 个严格正有理槽见 R193 §3；本稿直接引用该已付证明，不重新积分或近似符号。其公开实际 run 为 43680023529，source 为 9b7c07f25514808595dcf4efe7e79220fc57a8d6；源码及准确参数也已列于 R193。

由 (23)，对每个实际允许的 $\lambda>0$，

$$
\operatorname{Re}\mathcal F(q_\lambda)>0.
\tag{24}
$$

**结论 A。** 任何具有一个标准状态四阶平点的光滑真实几何，配合同一 R193 原八包圆及同一指定目标，都不能通过完整第四 range；这一排除覆盖所有能放进共同物理 I 的正宽度，以及 R184 的全部允许二、三阶 gauge。

条件是支撑确在 I 内，例如原冻结输入须

$$
[\lambda,155\lambda]\Subset I.
$$

没有把代数上任意正宽度当作都能放进同一个固定物理区间。共同正实圆归一化只乘正四次幂，不改变 (24)。

R193 §5 已给一个统一的、准确重补三复矩的 $C^\infty$ 平滑邻域，其中四个系数仍同时为正。因此结论 A 同样覆盖该已付的光滑邻域；不局限于 C7 计算原型。

## 7. 任意固定状态平点的共同窄化版本

对一般 $(h_*,k_*,\omega_*)$，R187 使用同一个原轴向导数分包 raw 圆。在物理内部点 c 作共同窄化

$$
q_\lambda(\xi)
=q_{\rm raw}\!\left(\frac{\xi-c}{\lambda}\right).
$$

记

$$
e_c=h_*(c+\omega_*)-k_*,
\qquad
I_4=\int(q_{\rm raw}'')^4>0.
$$

取 c 避开 R54 标准图的极点 $1-k_*e_c=0$。R187 的完整迁移及同锚尾处理已证明常状态的最高复幅为

$$
K_{4,*}(q_\lambda)
=
-\frac{(1+k_*^2)^2(1+e_c^2)^3}
{12288\,h_*^5\,\lambda^7}\,I_4
+O(\lambda^{-6}).
\tag{25}
$$

由 (16)，单点二阶 s jet 的对应复幅等于其两倍：

$$
-\frac{(1+k_*^2)^2(1+e_c^2)^3}
{6144\,h_*^5\,\lambda^7}\,I_4
+O(\lambda^{-6}).
\tag{26}
$$

其真实部对全部充分小的正 $\lambda$ 严格为负。

**结论 B。** 对任意固定的状态四阶平点，R187 的同一轴向导数分包圆在充分共同窄化时已经不可能延拓到第四阶；无需该点附近有任何常段。

对有限个平点可以先选一个共同 c 避开有限个图极点，再统一取小宽度。但排除整条几何只需其中一个点。该结论不把 R193 的标准态全宽度表推广为任意状态的全宽度正性。

## 8. 对 R214 及后继构造的准确影响

R214 的所有有限拼接口仍保所有正阶 scalar jets 为零。它以完整低阶词恒等式、全 P 非线性 IFT 和 Baire 精确去掉开常段，同时保闭合、非零 hook 与 universal pure 零；这些结论均不受本稿影响。

但若选择标准共同端口，则其中任意一个拼接口满足 (20) 及 (2)。所以：

- R214 配 R193 原冻结八包及其已付光滑邻域，在任何允许正宽度下仍被结论 A 排除；
- 改成其他固定平端口，仍不能在 R187 充分共同窄化的轴向导数分包类中避开结论 B；
- “没有开常段”不能再单独作为离开这些已排实例的理由。

本稿不排除改变 profile 圆使 (19) 准确成立。R53 已证明特定其他多相位重叠圆可支付标准常状态的整个二次最高项，说明这一必要门并非对全部圆的普遍正障碍；它仍未支付一般状态、较低 jets 或完整 joint range。

R199 的新忠实末 step 圆也必须按其实际完整 q 检查 (19)，不能继承 R193 原冻结圆的正性，亦不能因它和 R214 相配就声称该门自动为零。本文没有对这个新圆重新求积。

另一可能方向是改变实际拼接类别，使几何不再有满足 (2) 的点；这需要重新支付低阶词、端 jets、全 pure 校正和空间闭合，不能把 R214 已证明的平端口类别直接替换为任意非平 jets。

以上都是当前光滑固定圆形式机制的准确范围。它不构成对任意 C2 等距族、其他目标度量或所有闭曲面新机制的不可能性证明。

## 9. 已完成与未完成

已证明的是一个新的、可直接使用的 ruling 商泛函：在状态四阶平点，$\partial_s^2|_{s_*}$ 杀掉所有允许 gauge 的 ruling 改变量，却准确读出常段二次最高项的两倍。标准原八包的全宽度严格符号因而在单点已经构成障碍。

本结论没有产生新的可重算机器输出，也不需要重跑 R193 或任何 pure 投影。全 pure 控制已付而该 fixed-circle ruling 门仍可能失败，二者属于不同必要条件。下一有效构造必须明确支付单点最高项，或实际离开四阶平点前提；通过这一门以后仍须同时支付 mixed period 与同一个 w 的完整 ruling。

