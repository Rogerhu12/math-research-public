# R140：完整真实第四成本正性与单一八矩 action 乘子的等价

日期：2026-11-14。**纸面已证明。** 本稿把 R119 的静态表乘子推广到完整真实平端路径，并保留全部导数、连接与累计历史。它给出闭成本锥正性的准确对偶表述，不证明该锥已经充满，也不把闭锥等同于实际成本半群。

依据 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R112](R112-local-fourth-geometric-derivative-weights.md)、[R119](R119-positive-static-cone-and-linear-multipliers.md)、[R120](R120-G-lineality-of-the-closed-fourth-cost-cone.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md) 及 [R137](R137-real-fast-pulse-positivity-and-acceleration-PSD.md)。

## 1. 空间、路径与局部积分

沿用 R127 的 universal 真实算子空间：

$$
U=\mathcal U_4,\qquad R=\mathcal R_8,\qquad
C=\overline{\operatorname{cone}\{V_B:M_B=T_B=0,\ F_B=I,\ B\text{ 同 scalar germ}\}}\subset U.
\tag{1}
$$

起始 scalar germ 任意固定；R105/R120 已证明 U、C 不依赖它。闭包在有限维真实函数空间中取，不在冗余原式系数空间中取。

取包含完整局部系数及 U 的有限维真实环境 E。固定 $\lambda\in U^*$，任取线性延拓 $\widetilde\lambda\in E^*$。记

$$
L=L_0+L_2+L_4,\qquad m=m_0+m_2,
$$

$$
I(P)=\int_P\widetilde\lambda(L)\,ds,\qquad
M(P)=\int_Pm\,ds\in E_8.
\tag{2}
$$

P 是任一光滑有限水平平端 scalar 路径，

$$
h>0,\qquad \omega_s=\frac{k_s}{2h},
\tag{3}
$$

两端可以不同。起始 frame 可取 I，末 frame 由真实 ODE 决定，未指定空间位置终点。L 不含累计二、三阶历史，因此 (2) 的积分准确拼接可加。

对同 scalar germ、frame I、M=0 的完整路径，R105/R83 先保证其 V 属于 U（T 可以非零）。若 $\lambda(R)=0$，R109 给

$$
I(P)=\lambda(V_P).
\tag{4}
$$

这个等式不要求 T=0；但一般 M≠0 时不把 I 当作完整第四 V。

所有表达式共用同一 canonical 目标和右锚。证明涉及任一有限路径表时，先固定这些路径及有限辅助族，后取共同物理 I；不预先承诺任意窄区间或统一总长下都能实施全部补偿。

## 2. 定理

以下两项等价：

1. $\lambda\in C^*$，即 λ 对全部真实第四成本闭锥非负；
2. $\lambda(R)=0$，且存在一个固定的实线性八矩乘子 $\mu\in E_8^*$，使对**每条**真实开或闭 scalar 的平端路径 P，

$$
\boxed{
\int_P\bigl(\widetilde\lambda(L)-\mu(m)\bigr)\,ds\ge0.
}
\tag{5}
$$

乘子 μ 不依赖 P、起止 scalar germ、frame 或时长。不存在未写出的端点势差；这比仅对闭 scalar 路径的积分不等式更强。

(5) 是完整路径积分条件，不是原密度逐点非负的断言。尤其不能把它替成对每个自由 jet 单项逐项要求非负。

定理对任意固定的延拓 $\widetilde\lambda$ 都成立。更换延拓只改变允许的矩阵乘子，不改变 λ 在真实成本锥上的正性。

## 3. 零矩/恒等 frame 路径可先去掉 T 条件

先假设 $\lambda\in C^*$。由 R120 的 lineality，

$$
\lambda(R)=0.
\tag{6}
$$

设 B 是同 scalar germ、frame I、M=0 的实际平端路径，允许 T 非零。R83 的真实倒行给

$$
M_{B^R}=0,\quad F_{B^R}=I,\quad
T_{B^R}=-T_B,\quad V_{B^R}=V_B.
$$

故 $BB^R$ 满足定义 (1) 的全部低阶条件，且

$$
V_{BB^R}=2V_B.
$$

由 (4) 得

$$
\boxed{I(B)\ge0
\quad\text{对同 germ、frame I、M=0 的全部实际 B}.}
\tag{7}
$$

这里没有给 V 使用负号，也没有忽略第三累计成本。

## 4. 任意正实权零矩路径表的真实非负性

**引理。** 对任意有限组真实开平端路径 $P_1,\ldots,P_q$ 和正实数 $a_1,\ldots,a_q$，若

$$
\sum_i a_iM(P_i)=0,
\tag{8}
$$

则

$$
\boxed{\sum_i a_i I(P_i)\ge0.}
\tag{9}
$$

**证明。** 零权项可删。固定一个共同基 germ g。记 $A_i$ 为 $P_i$ 的实际末 frame。取 R83 的同 k 真倒行

$$
F_i^R(s)=D A_i^TF_i(L_i-s)D,\qquad D=\operatorname{diag}(-1,1,-1).
$$

其 scalar 是 $S_i(L_i-s)$。R112 中 m 的导数权为 0、2，L 的导数权为 0、2、4，故局部式准确满足

$$
M(P_i^R)=M(P_i),\qquad I(P_i^R)=I(P_i).
\tag{10}
$$

$Q_i=P_iP_i^R$ 是 scalar 闭路径，首末为 $P_i$ 的首 germ，但末 frame 通常是

$$
A_iDA_i^TD,
$$

不必为 I。重复 Q_i 时真实 frame 连乘，不能在接缝重置；其 scalar、矩阵和局部成本仍分别闭合、相加：

$$
M(Q_i^{n_i})=2n_iM(P_i),\qquad I(Q_i^{n_i})=2n_iI(P_i).
\tag{11}
$$

按 R70 用固定 M=0、相对 frame I 的平端桥，从共同 g 接到每个 Q_i 的 germ，重复该块后再接回 g。第二条桥在当时的真实末 frame 左旋转后接续；其相对 frame I 不会抹掉前面的旋转。固定环境旋转不改变 m 或 L。每一类块只付一次入桥和出桥，其局部成本总和与 $n_i$ 无关。

对大整数 n，取

$$
n_i=\lfloor n a_i\rfloor.
$$

串接这些有限块后的矩阵为

$$
M_n=2\sum_i n_iM(P_i)
=-2\sum_i\{na_i\}M(P_i).
\tag{12}
$$

由 (8)，它落在一个固定紧矩阵盒中。末 frame 可以随 n 变化，但始终属于紧群 SO(3)。

R70 的局部平滑截面及对紧参数盒×SO(3)的有限覆盖，给出同 g、目标矩阵 $-M_n$、目标相对末 frame 为当前 frame 逆的真实补偿族。取覆盖内较小的紧片后，其 scalar 值、正时长、有限 jets 及局部积分都有统一界。辅助整圈数和各片拼接数固定；没有把端点修正的累计完整 V 估成 O(1)。

现在得到同 g、frame I、M=0 的完整路径 B_n。全部固定进出桥和紧补偿族只贡献一个有界局部积分余项，因此

$$
I(B_n)=2\sum_i\lfloor na_i\rfloor I(P_i)+O(1).
\tag{13}
$$

由 (7) 该式非负。除以正数 2n，再取 n→∞，得到 (9)。

每个 B_n 是真实有限正长度路径。所有 scalar 包络来自有限原路径、其倒行和有限辅助紧族，重复数不会扩大值域，故一个共同物理区间可在构造这些族后固定。位置位移没有被单桥指定，也没有被用于代替 frame 或矩阵条件。证毕。

(13) 只关于真实局部 I。完整 V 可能含二次、三次重复数的历史项；零矩整字形成后，(4) 才利用 λ 杀 R109 的真实 R 差，将完整成本与 I 精确对齐。因此这些高阶项没有被静默当成 O(1)。

## 5. 真实正表的有限次线性下包络

对 $M\in E_8$ 定义

$$
f(M)=
\inf\left\{
\sum_{i=1}^q a_iI(P_i):
q<\infty,\ a_i\ge0,\ \sum_i a_iM(P_i)=M
\right\}.
\tag{14}
$$

空表允许并给 $f(0)\le0$。引理给所有零矩正表的成本非负，因此

$$
f(0)=0.
\tag{15}
$$

这里未假设 inf 被某条真实路径或某个表取到。

对每个 M，R70 真实实现一个矩阵为 M 的平端路径，故 (14) 非空且有有限上界。再固定一条矩阵为 −M 的真实路径 $P_{-M}$。把它加到 (14) 任意 admissible 表中，得到零矩正表；由 (9)，

$$
\sum_i a_iI(P_i)\ge-I(P_{-M}).
$$

因此

$$
-\infty<f(M)<+\infty.
\tag{16}
$$

任意 t>0，正表权重同时乘 t 给 $f(tM)=tf(M)$；任意两个近似极小表拼合给

$$
f(M+N)\le f(M)+f(N).
\tag{17}
$$

所以 f 是有限次线性函数。其有限维连续性也可直接见出：以固定真实矩阵 $\pm E_i$ 路径组成任意 M 的表，给 $f(M)\le c\|M\|$；(15)、(17) 又给 $f(M)\ge-f(-M)\ge-c\|M\|$，并由次可加性得到全局 Lipschitz 界。

这些表是为对偶证明引入的正权表；没有把任意实权表直接宣称为一条准确有限物理路径。第 4 节仅在零矩表上通过 floor 重复和真实有界补偿取得所需非负性。

## 6. 单一矩阵乘子及反向蕴含

由有限次线性 f 的 Hahn–Banach 支撑定理，存在实线性

$$
\mu:E_8\to\mathbb R,\qquad \mu(M)\le f(M)\quad\forall M.
\tag{18}
$$

单路径 P 本身是 (14) 的 admissible 表，故

$$
I(P)\ge f(M(P))\ge\mu(M(P)).
$$

这就是 (5)。它适用于所有开平端 P，所以乘子不依赖其端口。没有将不同端口的边界势丢掉，而是第 4 节使用各自真实倒行和固定进出桥后直接把它们纳入同一全路径表。

反过来，假设 $\lambda(R)=0$ 且存在 μ 满足 (5)。对 (1) 中任一实际 $M=T=0$ 成本，由 (4)，

$$
\lambda(V_B)=I(B)\ge\mu(0)=0.
$$

线性性与连续性使 λ 在其闭凸锥上非负。等价性得证。

若更换延拓为 $\widetilde\lambda+\kappa$，其中 $\kappa(U)=0$，R130 的完整湮灭子定理给一个固定 $\mu_\kappa$，满足

$$
\int_P\kappa(L)\,ds=\mu_\kappa(M(P))
$$

对所有开平端 P 成立。因此 (5) 中只需把 μ 改成 $\mu+\mu_\kappa$，准确说明了延拓无关性。

## 7. 对每条路径的三个导数权积分的准确耦合

固定 (5) 的 μ，并对任一平端 P 定义

$$
A(P)=\int_P(\widetilde\lambda(L_0)-\mu(m_0))\,ds,
$$

$$
B(P)=\int_P(\widetilde\lambda(L_2)-\mu(m_2))\,ds,\qquad
C_4(P)=\int_P\widetilde\lambda(L_4)\,ds.
\tag{19}
$$

把 P 的时长乘任意 δ>0，不假设其 frame 不变。它仍是定理所允许的开平端路径，所以 (5) 与 R112 给

$$
\delta A(P)+\delta^{-1}B(P)+\delta^{-3}C_4(P)\ge0
\quad\forall\delta>0.
\tag{20}
$$

令 t=δ²，等价于

$$
A(P)t^2+B(P)t+C_4(P)\ge0\quad\forall t>0.
$$

因此准确等价的三个标量条件是

$$
\boxed{
A(P)\ge0,\qquad C_4(P)\ge0,\qquad
B(P)+2\sqrt{A(P)C_4(P)}\ge0.
}
\tag{21}
$$

若 A 或 C₄ 为零，最后一式即 B≥0。一般 B 可以为负，不能凭 (20) 擅自把导数权二的积分单独判为非负。

对常态路径 (21) 给出逐状态的 R119 静态乘子不等式

$$
\widetilde\lambda(L_0(S))-\mu(m_0(S))\ge0.
$$

最高项 $C_4(P)\ge0$ 则恢复 R137 的完整快速脉冲门与加速度 PSD。这里是同一个 μ 同时对全部路径控制静态项和速度二次项，不是每条路径独立重选乘子。

若反过来存在一个 μ，使 (21) 对全部 P 成立，则取 t=1 得 (5)，因而这也是完整正性的准确表述。但它仍是所有真实水平路径的积分条件，不是一个已经求解的有限正性问题。

## 8. 范围

本稿把真实端口、frame 与 M/T 条件下的成本正性，等价地化为单一八维乘子的完整自由端口 action 不等式。它允许将静态表、R137 的加速度矩阵和剩余速度层放在同一个对偶问题中，不再只列互不相关的必要条件。

没有声称找到实际非零正泛函、完整闭锥为真子锥或全空间；没有把正表 inf 当作取得的最优真实路径，也没有从闭凸锥或次线性包络制造实际逆元。

对固定窄物理 I、统一 scalar 盒、总长/厚度约束的受限模型，第 4 节所需的全部有限辅助族必须另行证明可用。这里的 universal 等价不能自动转成该受限模型的等价。

完整函数成本及 ruling 的联合支付、有限等距族、高阶收敛、闭嵌入与宏观 reach/握持要求继续保留。
