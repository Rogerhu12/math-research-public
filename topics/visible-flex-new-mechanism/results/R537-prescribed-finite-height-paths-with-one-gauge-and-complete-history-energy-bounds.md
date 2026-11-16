# R537：同一固定规范下任意预选有限高度路径的真实全段延续

日期：2026-11-16。**完整原式与 ODE 先验界的纸面证明；没有执行数值、求积、符号、profile、秩或开发检查。**

本稿接 [R535](R535-fixed-geometric-d-and-uniform-negative-matrix-increment-with-one-gauge.md)。母库、物理区间、所有实际 copy、原右锚、第二规范 $w=0$ 以及 R534 一次选定的 $\chi^\delta$ 全部保留。新的结论不是让一个未知局部解自行延长：可以先固定一个有限时长和一条合法的光滑高度路径，再取充分小的 $\delta>0$，用同一个完整 ruling 解出其余真实 scalar、八矩和第三历史，覆盖该整个区间。

证明中的大 Gram 产生一个正频率的快振子。要作全段能量估计，必须先从**完整**第三历史中准确抽走 $k''$，否则所谓“慢状态”的导数会暗含未控制的大量。本稿直接使用 R77 的原权三恒等式完成这一步。随后先给八矩及慢第三状态的顺次积分界，再建立修改能量，避免把局部 ODE 存在循环用作全段先验条件。

结果只控制高度与有限区间延续。其余 scalar 端口、全部八矩、frame、位置及 period 都是真实输出。特别，本稿近 $k=0$ 的极限仍有严格负的总 $t_1$，不是 $M=0$ 路径。新 $p_1$ 为 $O(\delta^4)$；这里不猜其均值或符号。

## 1. 先固定高度路径，后选小参数

保持 R534/R535 的
$$
S_c=(H,0,\omega_c),\qquad y=x+\omega_c>0,\qquad H^2y^2>1
$$
及全部原 profile 数据。记 R535 的统一正时长为 $T_*>0$，其固定 $d$ 真解的高度为 $h_\delta^{\rm old}(t)$，极限高度为 $h_*^{\rm old}(t)$。

先取一个固定 $0<\tau_0<T_*/4$，再固定任意有限的 $T>2\tau_0$。允许的目标高度 $\bar h$ 满足：

- $\bar h\in C^\infty([0,T])$，并在 $0\le t\le2\tau_0$ 等于 $h_*^{\rm old}$；
- 有预先固定的正数 $h_-,h_+$，使
  $h_-\le\bar h\le h_+$；
- 在整个真实物理区间有
$$
h_-\min_{x\in I}y>1 .
\tag{1}
$$

后半段可以到达任意预选的有限高度，可以返回某个高度，也可以预先给定高度的末 germ；只须保(1)。这里并未指定 $k,\omega$ 的末 germ。

选一个固定 cutoff $\zeta$，在 $[0,\tau_0]$ 为1，在 $[2\tau_0,T]$ 为0，$0\le\zeta\le1$。给本次真实方程规定的高度是
$$
h_\delta(t)=
\bar h(t)+\zeta(t)\{h_\delta^{\rm old}(t)-h_*^{\rm old}(t)\}.
\tag{2}
$$
只在 $[0,2\tau_0]$ 使用括号中的原真解。由 R535 的正规 ODE，
$h_\delta^{\rm old}\to h_*^{\rm old}$ 在这段上对每个固定有限时间导数成立。因此(2)具有统一的有限 $C^3$ 界，充分小 $\delta$ 下保(1)的严格余量，并且在初始开放区间与原路径逐 germ 相同。最终 $h_\delta=\bar h$ 逐函数准确成立。

下文把
$$
\gamma=h_\delta',\qquad a=h_\delta''
$$
当作已经规定的真实高度输入。它们不是随意代回一条已经求好的路径；我们将解完整剩余方程。

选择顺序始终是：固定母库、有限 $T$、高度路径和其紧参数盒，再选 $\delta$。所有常数可依赖这些先固定数据。没有将本定理扩成 $T=T(\delta)\to\infty$ 或 $h_+=h_+(\delta)\to\infty$ 的估计。

## 2. 原几何变量中准确的快慢分离

沿用
$$
\eta=\omega-\omega_c,\qquad d=h\eta-k,\qquad
\upsilon=k_s,\qquad \eta_s=\frac{\upsilon}{2h}.
$$
为除去慢状态中的 $d_s$，定义
$$
j=\frac{\eta}{h}+\frac d{h^2}.
\tag{3}
$$
由真实水平关系逐式得
$$
\boxed{
j_s=-\frac{2d\gamma}{h^3},\qquad
\eta=hj-\frac dh,\qquad k=h^2j-2d.
}
\tag{4}
$$
置 $v=d_s$，则
$$
\upsilon=2\eta\gamma-2v,
$$
$$
k_{ss}=2\eta a+2(\eta/h)\gamma^2
-\frac{2\gamma v}{h}-2d_{ss}.
\tag{5}
$$
这些是原 scalar 关系的恒等式，不是新的独立动力学假设。

R535 从原 R521 两加速度行已经证明
$$
C_h+2\eta C_k=-B(h,d),
\tag{6}
$$
其中
$$
B(h,d)=\frac{|\mathcal G|}{3072h^6}
\sum_\nu w_\nu\rho_\nu^4
\int_I \{h^2y^2-(1+d^2)\}
\frac{F_{u_\nu}(h,d)^4}{Q(h,d)^2}\,dx>0
\tag{7}
$$
于 $hy>\sqrt{1+d^2}$，且
$$
C_k(h,d)=\frac{|\mathcal G|}{3072h^5}
\sum_\nu w_\nu\rho_\nu^4\int_I
(hy+d)\frac{F_{u_\nu}^4}{Q^2}\,dx>0.
\tag{8}
$$
两者只依赖 $h,d$，不依赖 $j,A,T$。这里
$$
Q=1+(hy+d)^2,\qquad
F_u=Q u''-2h(hy+d)u'+2h^2u.
$$
所有实际正权、振幅和原母因子都保留。

完整第四 ruling 为
$$
C_h a+C_k k_{ss}
+\mathcal F(S,\gamma,\upsilon,A,T)
-\frac{\nu^\delta_0(1+d^2)}{2h}
-\frac{2c_k}{\delta^2}d=0,
\tag{9}
$$
$c_k=C_k(S_c)>0$，$\nu^\delta_0$ 有统一有限界。代入(5)(6)，准确得到
$$
\boxed{
d_{ss}+\frac{\alpha(t,d)}{\delta^2}\,d
=G(t,d,v,j,A,T),
\qquad
\alpha(t,d)=\frac{c_k}{C_k(h_\delta(t),d)}>0,
}
\tag{10}
$$
其中
$$
\begin{aligned}
G={}&
\frac{\mathcal F(S,\gamma,2\eta\gamma-2v,A,T)
-\nu^\delta_0(1+d^2)/(2h)-B(h,d)a}
{2C_k(h,d)}\\
&+\frac{\eta}{h}\gamma^2-\frac{\gamma v}{h}.
\end{aligned}
\tag{11}
$$
几何 $S$ 按(4)读取。除了显示的正频率项，(11)中没有 $\delta^{-2}$。然而此时 $T_s$ 仍会含 $k_{ss}$，所以还不能直接称它是一个普通慢状态。

## 3. 从完整第三历史中准确抽走快加速度

R73 的真实演化是
$$
A_s=\Phi_{M_{\rm raw}},\qquad
T_s=-\Phi_{M_{\rm raw}}\circ A+\mathcal C_s.
\tag{12}
$$
R77(2)对完整三阶密度给
$$
\mathcal C_s^{[3]}
=D_sP_{\rm acc}
+\mathcal A(S)(\upsilon h_{ss}-\gamma k_{ss})
+\sum_{q=0}^3\mathcal B_q(S)\gamma^{3-q}\upsilon^q.
\tag{13}
$$
$P_{\rm acc}$ 是速度二次势，$\mathcal A,\mathcal B_q$ 是固定有限空间内的原完整三线性 profile 算子。权一项 $\mathcal C_s^{[1]}$ 对速度线性。此处不将任何一项投到 $W$ 后删除。

定义实际重写的第三状态
$$
\boxed{
\widetilde T=T-P_{\rm acc}(S,\gamma,\upsilon)
+\mathcal A(S)\gamma\upsilon .
}
\tag{14}
$$
它的初值由 R535 的同一个真实 $T_0$、速度和 scalar 算出，不是另设零值。

准确微分(14)，其中
$$
D_s\mathcal A=(X\mathcal A)\gamma+(Y\mathcal A)\upsilon,\quad
X=\partial_h,\quad Y=\partial_k+\frac1{2h}\partial_\omega,
$$
得到
$$
\boxed{
\begin{aligned}
\widetilde T_s={}&-\Phi_{M_{\rm raw}}\circ A
+\mathcal C_s^{[1]}
+2\mathcal A\,a\upsilon\\
&+\{(X\mathcal A)\gamma+(Y\mathcal A)\upsilon\}
\gamma\upsilon
+\sum_{q=0}^3\mathcal B_q\gamma^{3-q}\upsilon^q .
\end{aligned}}
\tag{15}
$$
原 $-\mathcal A\gamma k_{ss}$ 与
$D_s(\mathcal A\gamma\upsilon)$ 中的
$+\mathcal A\gamma k_{ss}$ 逐项抵消。剩下两个
$\mathcal A a\upsilon$ 均保留，因子准确为2。

现在(15)不含 $d_{ss}$、$k_{ss}$ 或任何未控快导数。它不依赖 $\widetilde T$ 本身，并且对累计 $A$ 至多一次。真实第三仍可准确恢复：
$$
T=\widetilde T+P_{\rm acc}-\mathcal A\gamma\upsilon .
\tag{16}
$$
势的两端值不被删除。这个重写不改变原输出、第三 period 或后续第四成本。

以后把(16)代入(11)，仍记所得光滑函数为 $G$。令
$$
Z=(j,A,\widetilde T).
$$
完整系统遂是
$$
d_s=v,\qquad
v_s=-\delta^{-2}\alpha(t,d)d+G(t,d,v,Z),
$$
$$
\boxed{Z_s=\mathcal H(t,d,v,Z),}
\tag{17}
$$
其中 $\mathcal H$ 由(4)(12)(15)给出，不含快加速度，也没有 $\delta^{-2}$ 系数。所有 $t$ 依赖来自预给高度及其至多二阶导数。

## 4. 全段先验盒先于振子估计

这里先作不使用未知长期存在的顺次估计。给定第1节的有限路径和 $T$ 后，选一个小常数 $d_*>0$，使
$$
h_- \min_I y>\sqrt{1+d_*^2}
$$
并有严格余量。再将 $d_*$ 缩小，使由
$$
|j(t)|\le |j_0|+
2d_*T\,\|\gamma\|_\infty/h_-^3
\tag{18}
$$
得到的 $j$ 范围保证(4)中的 scalar 仍在一个固定合法紧域，尤其 $x+\omega$ 有正下界。这一步允许常数依赖先固定的 $T$；没有要求一份盒适用于所有无界时长。

考虑最大存在区间中满足
$$
|d|<d_*,\qquad |v|<1
\tag{19}
$$
的连通初段。此时(18)、预给 $h,\gamma,a$ 及(4)(5)使
$S,\gamma,\upsilon$ 全部处于固定紧集。原 $M_{\rm raw}$ 只含这些数据且对速度至多二次，故先得
$$
\|A(t)\|\le \|A_0\|+C_M T.
\tag{20}
$$
这不是一个待证明的 $A$ 小量；右边是已经确定的有限界。

再由(15)，在这个盒内有
$$
\|\widetilde T_s\|\le C_T(1+\|A\|),
$$
从而
$$
\|\widetilde T(t)\|
\le\|\widetilde T_0\|
+C_T\{T+\|A_0\|T+C_MT^2/2\}.
\tag{21}
$$
$\widetilde T_0=O(\delta^2)$，$A_0=O(\delta)$，均由 R535 的真实入值和(14)给出。因此(20)(21)是一组与充分小 $\delta$ 无关的先验有限界。

固定一个严格包含这些界的慢状态紧盒。则 $G,\mathcal H$、它们在该盒中的所需偏导，以及 $\alpha,\alpha_t$ 都有确定有限界；$\alpha$ 还有严格正下界
$$
0<\alpha_-\le\alpha(t,d)\le\alpha_+.
\tag{22}
$$
(20)(21)的取得没有用 $v_s$ 的界，故没有将快振子的结论循环放进慢状态假设。

## 5. 修改能量如何处理全部慢历史

定义
$$
f(t,Z)=G(t,0,0,Z),\qquad
V(t,d)=\int_0^d\alpha(t,z)\,z\,dz .
\tag{23}
$$
$f$ 明确包含同一个慢 $A,\widetilde T$，但不把实际 $d,v$ 带进其定义。由(22)，
$$
\alpha_-d^2/2\le V(t,d)\le\alpha_+d^2/2,
\qquad |V_t(t,d)|\le C d^2 .
\tag{24}
$$
这些式子对正负 $d$ 均成立。

沿实际慢状态，
$$
\frac d{dt}f(t,Z(t))
=f_t+f_Z\,\mathcal H(t,d,v,Z)
\tag{25}
$$
有统一有限界。其时间偏导只读预给 $h,\gamma,a$ 及至多 $h'''$；
$\mathcal H$ 已由(15)证明不含 $k_{ss}$。这正是不能省略第3节的原因。
原 $f$ 可以依赖 $A,\widetilde T$，(25)并未把它们冻结。

取一个充分大的固定常数 $C_E$，定义
$$
\boxed{
\mathscr E(t)=\frac12v^2+\delta^{-2}V(t,d)
-f(t,Z)d+C_E\delta^2 .
}
\tag{26}
$$
用 $f$ 的有限上界和 Young 不等式，可一次选 $C_E$，使
$$
\mathscr E\ge
\frac12v^2+\frac{\alpha_-}{4\delta^2}d^2+\delta^2,
$$
$$
\mathscr E\le
C\{v^2+\delta^{-2}d^2+\delta^2\}.
\tag{27}
$$
初值为 R535 固定 $d$ 支的真实入值，故
$d_0=O(\delta^5),v_0=0$，并有
$$
\mathscr E(0)\le C_0\delta^2 .
\tag{28}
$$

按(17)逐项微分(26)，快频率项完全相消：
$$
\boxed{
\mathscr E_s
=v\{G(t,d,v,Z)-f(t,Z)\}
+\delta^{-2}V_t
-\{f_t+f_Z\mathcal H\}d .
}
\tag{29}
$$
同一慢盒上
$$
|G-f|\le C(|d|+|v|).
$$
由(24)(25)(27)，
$$
\mathscr E_s
\le C\mathscr E+C\delta\sqrt{\mathscr E}
\le C'\mathscr E,
\tag{30}
$$
最后一步用 $\mathscr E\ge\delta^2$。因此在(19)的最大初段上，
$$
\mathscr E(t)\le C_0e^{C'T}\delta^2 .
$$
从而准确得到
$$
\boxed{
|d_s|\le C_*\delta,\qquad
|d|\le C_*\delta^2
\quad(0\le t\le T).
}
\tag{31}
$$
常数只依赖预先固定的有限数据。

取 $\delta$ 充分小，(31)严格改进(19)，而(20)(21)始终在已取的慢盒内部。所有状态有限且 scalar 合法，普通 ODE 的延拓准则于是把解延至整个 $[0,T]$。这完成最大区间论证，而非先假定存在到 $T$ 再使用 Gronwall。

由(10)(11)(31)，还可在结论之后读取
$$
d_{ss}=O(1),\qquad k_{ss}=O(1).
\tag{32}
$$
本稿不授更高时间导数的一致小量；快振动可以使它们增大。

## 6. 同一个真实入端、同一个规范及完整恢复

在初始开放区间，(2)与原固定 $d$ 路径完全相同，初值也是同一个真实
$(S,\gamma,\upsilon,A,T)$。原路径满足(17)，故唯一性使新解与它在该开放区间逐 germ 相同。没有在接点改规范、改 $T$ 初值或另补一个无 ruling 桥。

整个区间上，我们是从原(9)推得(17)，所以实际解逐点满足原全部相位的
$$
\mathscr K(s,\theta)=0 .
\tag{33}
$$
母库原已付的二、三阶条件继续成立。$T$ 按(16)精确恢复；frame、位置和第四字段按原同锚方程积分。它们在每个固定 $\delta>0$ 上都是真实有限光滑字段，不能用快慢记号抹掉其端口或成本。

同一结论可用于一份先固定、联合光滑的有限维紧参数族 $\bar h_\lambda$：只要共同保(1)、初始 germ 和有限 $C^3$ 界，以上所有盒、常数及充分小的 $\delta$ 可统一选择。随后对这个固定正 $\delta$，原 ODE 给对参数光滑依赖的实际 family，且整份 family 使用同一个 $\chi^\delta$。这里没有像逐点选择 Gram 那样让最终规范随目标高度参数改变。

这给一个真正的全段高度控制接口：例如可在同一规范下准确给出有限个高度末 jet 的小开邻域。其余 scalar、历史和 pose 输出照常联动，没有被当成额外自由量。

## 7. 原矩的真实尺度与没有支付的门

由(4)(31)和 $j_0=O(\delta^5)$，
$$
j=O(\delta^2),\qquad
k=O(\delta^2),\qquad
\eta=O(\delta^2),\qquad
\upsilon=O(\delta).
\tag{34}
$$
因此原 $p_1$ 密度只有如下已付结论：
$$
M_{p_1}=-kd=O(\delta^4),\qquad
\int_0^T M_{p_1}\,ds=O(\delta^4).
\tag{35}
$$
(31)本身不足以给 $d/\delta^2$ 的逐点极限或振子平均，所以本稿没有写出一个未经证明的 $\delta^4$ 系数，更不说其为负。这个量级大于 R534 的正前缀 $\delta^7$，但大小关系不是符号关系。

另一个原矩已有严格结论。R524/R73 的恒等式给
$$
8M_{t_1}=2kh\eta-k^2-1-(\gamma/h)^2.
$$
由(34)，在整个预给区间上
$$
8M_{t_1}
=-1-(h_\delta'/h_\delta)^2+O(\delta^4).
\tag{36}
$$
故充分小 $\delta$ 时，本段的总 $t_1$ 严格负，且其极限为
$$
-\frac18\int_0^T
\{1+(\bar h'/\bar h)^2\}\,dt<0 .
\tag{37}
$$
原八矩演化全部保存；近 $k=0$ 的这个全段跟踪机制不能单独给 $M=0$。

高度的末 germ 按(2)准确达到，并不使 $k,\omega$ 的末值或末 jets 准确回到原值；它们目前只是(34)的小量。原 $A,T$ 不必小，也没有返回。frame、位置、第四 period 和同一十三规范仍须分别支付。有限时长可以任意先指定，不等于一份已经冻结的 $\delta$ 解可以跟踪任意无界时长。

## 8. 后继真实问题

相较 R535 的一条自主高度弧，本稿允许在同一固定规范下先选择一整条有限高度路径，然后真实解出其余场。关键代价已完整保留：第三状态的两个端点势、原有序复合、快振子与全部慢历史，以及先固定路径后选小参数的顺序。

下一项可直接围绕(10)(11)研究真正的 $p_1$ 四阶尺度符号或更大的 $k$ 状态，但必须先付相应精细渐近或有限幅轨道；不能从(35)猜它能配平正前缀。若要令高度或时长依赖 $\delta$ 增长，则必须重新控制这里的常数，尤其(20)(21)(25)的全历史界。当前证明没有替这一步预支可达性。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：原八矩及真实有序第三累计；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)(2)：完整权三密度、对称加速度势与速度面积；
- [R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)(2)：原权一结构；本稿不使用其中未受当前 ruling 限制的控制桥；
- [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) 未消历史的原式：完整 $\mathcal F$ 与固定第三规范的作用；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：同一正交库和两条完整加速度行；
- [R534](R534-real-zero-history-entry-into-negative-matrix-density-and-fixed-gauge-continuation.md)、[R535](R535-fixed-geometric-d-and-uniform-negative-matrix-increment-with-one-gauge.md)：同一真实零历史前缀、固定 Gram、负区与共同入端。

全稿没有新科学执行，也没有把数学上的能量估计包装成已运行的数值验收。

root全文纸核已核j的准确水平变换、正快频率号、完整第三中2𝒜aυ、顺次慢状态盒及含真实历史的修改能量；未增加科学执行或独立重跑。高度下界h₋取在目标路径共同合法余量内部，必要时先略缩小，故(2)的小修正仍保全段同一严格下界。
