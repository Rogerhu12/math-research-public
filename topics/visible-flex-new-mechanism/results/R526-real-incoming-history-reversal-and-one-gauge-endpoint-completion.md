# R526：真实入历史倒行、同一规范下的第三端口抵消与准确闭合词

日期：2026-11-16。**原式纸证；没有执行几何试验、profile 求积、符号程序、数值秩或开发检查。**

本文接 [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md) 的同一个实际母库与 [R523](R523-real-reflection-segments-one-fixed-gauge-and-exact-third-endpoint-transfer.md) 的真实重锚。新增的充分机制是：

> 一条已经满足完整第四 ruling 的实际段，只要其原总第二矩阵为零，就可直接接上真实倒行；全词带入的第三历史恰好补掉倒行的 canonical 第三常数差。在同一固定 $w=0,\chi$ 下，两段完整字段按真反射配对，第三总端口准确为零。

这里不要求原段的第三端口先为零。这个区别来自真正的入历史，不能靠把倒行段又从全零历史开始来得到。

总矩阵为零的实际受约束段仍未构造。本文给出精确的矩阵零段完成规则、剩余 pose 条件和一个第三逐函数盲时的四段闭合词；它不把这些充分规则当成所需矩阵零段已经存在。第四 characteristic 累计是加倍或四倍，仍要支付整个函数为零。

## 1. 一个真实段、一个右锚和一次固定规范

固定 R521 的真实第一圆
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,
\tag{1}
$$
共同物理区间、右锚 $Jv(x)=\int_x^{r_*}v$ 及全部实际 profiles。几何仍是
$$
h>0,\quad \omega_s=\frac{k_s}{2h},\qquad
F_s=F\Omega(k),\qquad \alpha_s=h^2F e_1,
\tag{2}
$$
$$
\Omega(k)=
\begin{pmatrix}
0&-k&0\\
k&0&1\\
0&-1&0
\end{pmatrix}.
$$
同一个 $x+\omega>0$ 的合法窗口包含整个段及其倒行；倒行没有增加新的 scalar 值。

设 $P$ 是 $0\le s\le L$ 上的真实光滑段，长度 $L>0$。本稿的条件是：

1. 原 canonical 第二、第三历史在段左端为零；
2. 整段使用固定的 $w_\theta=0$ 和同一个双 collar 紧、相位光滑周期、在两个 seed 为零的 $\chi_\theta$；
3. 原完整第四 ruling $\mathscr K_P(s,\theta)$ 对所有 $s,\theta$ 为零；
4. 原完整总矩阵满足
   $$\boxed{\mathsf m_P(L)=0,\qquad A_P(L)=0,\quad A=\Phi_{\mathsf m};}$$
5. 用于反射拼接的 scalar germs 确实光滑匹配。

第5点的一个明确充分条件是两端都有开常值 scalar germs。这只是反射匹配的条件例，未断言当前 R521 库已经实现带这种 germ 的完整 $K=0$ 段。更弱而仍充分的是：$h,k,\omega$ 在相应端点的全部奇阶导数为零，从而其真实偶反射是 $C^\infty$。本文不把仅三个 scalar 端值相同当作完整 germ 匹配。

两端的 scalar 值可以不同。构造 $PP^R$ 时，第一段末端与倒行起端自然是同一个 scalar 值；整个两段最后回到原左端值。第7节的 $P^2(P^R)^2$ 还会明确增加两端同值、同 germ 的要求。

**本稿没有证明上述第3、4、5点可同时达到。** R523 给出的短反射段一般有非零总矩阵；它不能直接充当这里的 $P$。本稿的规范是 $w=0$，也不能把 R523 通常非零的 $w=-A_LD$ 默默丢掉。

## 2. 原有序复合与任意真实入历史

使用 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)(15)–(17)的完整算子：
$$
A_s=\Phi_{M_{\rm raw}(s)},\qquad
T_s=-A_s\circ A+\mathcal C_s,
\tag{3}
$$
$$
(A_1\circ A_2)(a;b,c)
=A_1\{a,A_2(b,c)\}.
\tag{4}
$$
$T$ 在本文表示第三传递算子；frame 切向量用 $Fe_1$ 表示。式(4)不是两个 $3\times3$ 矩阵的乘法。

$\mathcal C_s$ 包含原局部 third、变化-profile chain 和所有右原函数。R523 §2 从 R56/R73 逐槽证明：真实时间反射保 $M_{\rm raw}$ 为偶，使 $\mathcal C_s$ 为奇。所有 $s$ 导数固定同一个 $x$；加速度、$P_s,B_s$ 和原初端值均保留。

若一个 canonical 子段的输出为 $A_B(s),T_B(s)$，而真正全词进入它时已有 $A_0,T_0$，则从(3)逐项积分得
$$
\boxed{
A_{\rm glob}=A_0+A_B,\qquad
T_{\rm glob}=T_0+T_B-A_B\circ A_0.
}
\tag{5}
$$
交叉项的次序须保。它来自 $-A_{B,s}\circ A_0$，不能换成
$-A_0\circ A_B$。

在任意真实全局历史下，原 [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) 未消历史的(23)(24)为
$$
q_\theta=A_{\rm glob}D_\theta+w_\theta,
$$
$$
b_\theta
=-2T_{\rm glob}(\phi_\theta;D_\theta)
+2A_{\rm glob}(\phi_\theta,w_\theta)-\chi_\theta,
\tag{6}
$$
$$
\mathscr K
=\mathcal R+\mathcal L(q)-\mathcal E(q,q)
+2\mathcal E(\phi,b).
\tag{7}
$$
本文使用完整(6)(7)，没有取模 $W$，也没有以 natural total 代替完整字段。

例如，局部把(5)重新记成 canonical 子段时，必须同时使用有效规范
$$
w_{\rm eff}=w+A_0D,\qquad
\chi_{\rm eff}
=\chi+2T_0(\phi;D)-2A_0(\phi,w).
\tag{8}
$$
它只是同一个全局场的记账式，不授权在接头重新选择物理规范。

## 3. 真实倒行的完整 canonical 第二、第三响应

令 $P^R$ 的 scalar 函数为
$$
S_R(t)=S_P(L-t),\qquad 0\le t\le L,
\tag{9}
$$
同时按原(2)正向恢复它自己的 frame 和位置。它是正长度的真实段，不是把一个成本乘以负号。

暂不使用 $A_P(L)=0$。写
$$
A_*:=A_P(L),\qquad T_*:=T_P(L).
$$
由 $M$ 偶、$\mathcal C$ 奇，以及倒行 canonical 左端仍为零，
$$
\boxed{A_R(t)=A_*-A_P(L-t),}
\tag{10}
$$
$$
\boxed{
T_R(t)=T_P(L-t)-T_*-A_R(t)\circ A_*.
}
\tag{11}
$$
(11)可直接微分核对：
$$
(T_R)_t
=-T_{P,s}(L-t)-(A_R)_t\circ A_*
=-M_R\circ A_R-\mathcal C_P(L-t).
$$
这正是原倒行的(3)。在 $t=0$，右边的值为零，故也保真初端常数。

现在只用本文真正的矩阵零条件 $A_*=0$，则
$$
A_R(t)=-A_P(L-t),\qquad
T_R(t)=T_P(L-t)-T_*,
\tag{12}
$$
并且
$$
A_R(L)=0,\qquad T_R(L)=-T_*.
\tag{13}
$$
因此第三倒行总值变号，但它在内部不是简单的 $-T_P$；那个固定 $-T_*$ 仍必须保留。

## 4. 接上真实入历史后，全字段按反射配对

现在实际运行 $P$，随后直接运行 $P^R$。倒行入口已有
$$
A_0=A_*=0,\qquad T_0=T_*.
$$
由(5)(12)，倒行区间上的真实全局历史恰是
$$
\boxed{
A_{\rm glob}(L+t)=-A_P(L-t),\qquad
T_{\rm glob}(L+t)=T_P(L-t).
}
\tag{14}
$$
原第三入值 $T_*$ 与(12)中的 canonical 常数差精确相消。这里没有把原段的 $T_*$ 设零。

由于全词只使用同一个 $w=0,\chi$，(6)立即给
$$
\boxed{
q_R^{\rm glob}(t)=-q_P(L-t),\qquad
b_R^{\rm glob}(t)=b_P(L-t).
}
\tag{15}
$$
这是原 profile 函数身份，不只是在某个内积中相等。

令
$$
D_F=\operatorname{diag}(-1,1,-1),\qquad
D_F\Omega(k)D_F=-\Omega(k).
$$
在各自真实 frame 中，原 R56 分子恢复遂有
$$
V_Y^R=-D_FV_Y,\qquad
V_Z^R=D_FV_Z,\qquad
V_W^R=-D_FV_W,
\tag{16}
$$
右边取原段的 $L-t$。相应真实协变导数为
$D_F\nabla Y,-D_F\nabla Z,D_F\nabla W$。

其中 second 的局部项按 $D_F$ 变换，而(15)给其齐次项所需的反号；third 的 forcing、局部恢复与(15)的 $b$ 同时给第三式。所有右原函数仍在同一物理 $x$ 锚上，不发生 $x$ 反射，也不丢任何左尾。

第四 forcing 是原 second square 与 $Y$–third 配对。由(16)，其完整 ruling 不变，故
$$
\boxed{
\mathscr K_{PP^R}(s,\theta)=0
\quad(0\le s\le2L,\ \text{全部 }\theta).
}
\tag{17}
$$
整个词从头到尾只有一个固定 $\chi_\theta$；(14)使用的是运行第一段后真实获得的入历史。

### 规范与 collar 的合法性

$w=0$ 当然满足原二阶齐次规范的三条交叉矩。R521 已支付第一圆每个完整基本块的二阶三矩和第三四通道，因此 canonical 第二、第三字段在两外 collar 为零。加入原固定紧 $\chi$ 仍保持这些 collars。

倒行只重排真实 $s$，没有改变 profiles、右锚或每块的三矩。由(14)(15)，其全字段与已合法原字段直接对应，所以不另假“第三总 natural 零”来推紧性，也不需为倒行再选一个三矩补偿。

两个 seed 的 $D_\theta=0$ 和原 $\chi_\theta=0$ 也保持。接头的光滑性则使用第1节真正的反射匹配 germs；它与 collar 合法性是两个不同条件。

## 5. 第二、第三总端口和完整第四原累计

由(13)(14)，两段末端严格有
$$
\boxed{
A_{PP^R}=0,\qquad T_{PP^R}=0.
}
\tag{18}
$$
这是全算子身份。原 $T_*$ 可以很大，也可以不属于 $W$ 或某个固定 hook 子空间；(18)没有使用这种额外限制。

令 $\mathcal R_{4,P}(s,x,\theta)$ 是含固定 $\chi$ 的完整原第四 characteristic 密度。原 R56 的 $J,T_x,T_s,P,B$ 在(16)下为偶，真实 $P_s,B_s$ 为奇，$\lambda,\gamma$ 为奇。故倒行的真实密度满足
$$
\mathcal R_{4,PP^R}(L+t,x,\theta)
=\mathcal R_{4,P}(L-t,x,\theta).
\tag{19}
$$
从左端把第四齐次初值固定一次，原累计准确为
$$
\boxed{
V_{PP^R}(x,\theta)
=2V_P(x,\theta),\qquad
V_P=\int_0^L\mathcal R_{4,P}(s,x,\theta)\,ds .
}
\tag{20}
$$
第四源只读前面已经完整匹配的 $Y,Z,W$；第一段已经产生的第四齐次值不会反过来改变第四 forcing，所以(20)没有漏一个第四入值交叉项。

式(20)保留整个 $x,\theta$ 函数。它不是第四消去。即使下一节的几何端点也闭合，完整第四 period 仍要求 $V_P=0$；不能把反射、Klein 或 scalar 返回当成这一步。

若原机制要求特定非零第三目标 $\tau\mathfrak H$，(18)也不支付该目标。特别不能在 $T=0$ 上直接调用另一个固定非零 $\tau$ 的 period/gauge 公式。本稿减少的是构造真实零第三返回块的独立端条件。

## 6. 两段 pose 的准确闭合条件

规范第一段起 frame 为 $I$、起位置为 $0$，记其真实 Euclidean pose 为
$$
P_{\rm pose}=(G,v),\qquad G\in SO(3),\quad v\in\mathbb R^3.
$$
同一个整体刚体变换可恢复任意起 pose，不改变下面的相对条件。

由原 frame 方程，倒行从自身 $I,0$ 出发时为
$$
F_R(t)=D_FG^{-1}F_P(L-t)D_F,
$$
$$
\alpha_R(t)=D_FG^{-1}\{\alpha_P(L-t)-v\}.
\tag{21}
$$
它们直接微分为(2)，且 $t=0$ 值为 $I,0$。所以
$$
\boxed{
P_{\rm pose}^R=(D_FG^{-1}D_F,\,-D_FG^{-1}v).
}
\tag{22}
$$
记 $H=(D_F,0)$，则是 $P^R_{\rm pose}=HP_{\rm pose}^{-1}H$。

真实拼接的总 pose 为
$$
\boxed{
PP^R_{\rm pose}
=\left(GD_FG^{-1}D_F,\ (I-GD_FG^{-1})v\right).
}
\tag{23}
$$
它是两个真实半周转的乘积：一条轴是初始 $N$ 轴，另一条是该轴在 $P_{\rm pose}$ 下的像。两轴可能异面，因此一般留下非零 screw 位移。

由(23)，frame 和位置同时返回准确等价于
$$
\boxed{
GD_F=D_FG,\qquad (I-D_F)v=0.
}
\tag{24}
$$
第一式只要求 $G$ 保持初始 $N$ 轴这条无向直线；第二式要求真实 $v$ 平行该轴。两个条件都不是 $A_P=0$ 的推论。

如果(24)以及第1节两端反射匹配 germs 成立，$PP^R$ 就已经是真正 scalar/frame/位置/第二/第三全部返回、内部完整 ruling 为零的光滑闭词。其第四 period 仍是(20)。这是一个明确的充分完成规则；本文没有构造满足(24)的矩阵零段。

此处 $G$ 是原整段 $P$ 的末 frame，不是 R523 中“从中心到右端的半段 frame”。两种坐标不能混用。R523 的单个反射总 frame 不可能等于 $D_F$：以该稿半段 frame $G_c$ 写成 $D_FG_c^tD_FG_c$，若等于 $D_F$ 就迫 $G_c^tD_FG_c=I$，与 $D_F\ne I$ 矛盾。这并不与(24)相矛盾；本节没有在那个不可能目标上再做射击。

## 7. 第三逐函数盲时的四段实际 Klein 完成

另加如下准确条件：

- $P$ 两端 scalar 值和全部 germs 相同，并且可反射拼接；
- $G=D_F$；
- 同一圆上完整第三端口逐函数为零：
  $$\boxed{T_*(\phi_\theta;D_\theta)=0
  \quad\text{对全部 }x,\theta.} \tag{25}$$

不要求整个三线性算子 $T_*$ 为零。原段仍是第1节的实际 $M=0,K=0,w=0$ 段。

考虑正长度四段词
$$
\mathcal W=P\,P\,P^R\,P^R .
\tag{26}
$$
每个子段的总第二矩阵为零，故各接头第二入历史为零；第三入历史依次是
$$
0,\quad T_*,\quad 2T_*,\quad T_*.
$$
第2节的真实组合式没有第二交叉项。由(25)，这些入历史对(6)中正在使用的完整 profile $b_\theta$ 全部为零；因此每个正向子段的 $Z,W$ 与原段相同，每个倒行子段与原段按(16)配对。于是全词仍在**同一** $\chi$ 下满足完整 $\mathscr K=0$，并有
$$
A_{\mathcal W}=T_{\mathcal W}=0,\qquad
V_{\mathcal W}=4V_P.
\tag{27}
$$

对 pose，由 $G=D_F$ 和(22)，
$$
P_{\rm pose}=(D_F,v),\qquad P_{\rm pose}^R=(D_F,-v).
$$
所以
$$
P_{\rm pose}^2=(I,(I+D_F)v),\qquad
(P_{\rm pose}^R)^2=(I,-(I+D_F)v),
$$
两者正向相乘准确为单位 pose。**这里不再要求 $v$ 满足(24)**。原两端同 germs 保全部三个接头及最终识别光滑。

这证明了一个可用于真正控制块的完整规则：在第1节的实际矩阵零块上，若能把末 frame 付到 $D_F$，并把第三端口付到(25)的真实核，则四段完成 frame、位置、第二、第三与全部内部 ruling，而不删除任何第四成本。

仅有
$\mathcal E_S\{\phi,T_*(\phi;D)\}=0$ 时，可在相应实际状态上保护 ruling，但不必使整个 $W$ 场相同；其第四 characteristic 一般仍有附加交叉项。因此本文用更强的逐函数(25)来支付明确的 $4V_P$，不把一个 outer 零冒成全部 field 零。

### 当前 R521 库确有一个已付第三盲方向

R521 的每个最细微包都是 rank-one 导数包：
$(f',g')$ 在该包内是同一个紧 profile 导数的两个实常数倍。固定正交变换及正幅复制保留此事实。

[R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)(1)–(3)给原完整 hook
$$
\mathfrak H=[P,S]-3[P,R]
$$
的单层右积分式；每个被积项只含同一点三个输入的正阶导数，不留一个内层尾常数去乘另一包。因此
$$
\boxed{
\mathfrak H\big|_{\mathcal P\times\operatorname{Sym}^2\mathcal P}=0,
\qquad \mathcal P=\operatorname{span}\{f,g\}.
}
\tag{28}
$$
故 $T_*=\tau\mathfrak H$ 是(25)的真实充分目标，任意实 $\tau$ 均可，包括非零值。

式(28)只是已付原算子身份，不提供在完整 $K=0$ 约束下达到这个端口的路径。不能调用 R70/R180 的无逐点 ruling 桥来填入(26)。不同母库的成本截面或第三原型同样不能替代这一步。

## 8. 实际目标减少到哪里

两段规则(17)–(24)不需要把第三总端口单独控制为零：真实 incoming 精确支付该层。它把一个可能很大的完整第三输出留在原段内，随后由真正正长度倒行取消。原式的有序交叉项、固定 $\chi$、双 collar、seed 与第四成本全部保留。

四段规则(25)–(28)则允许只控制到当前圆的已知逐函数核，并以一个真正 $D_F$ 末 frame 代替位置端点控制。它使用同一固定规范，不是四段分别选规范或分别选择母库。

现在仍需首先构造同库、同规范的实际总 $M=0$ 段，并达到所选的真实 scalar germs 和 pose／第三核条件。R523 的短段没有这项总矩阵收据；原几何的必要振幅门也不能当成可达性。本文没有用少量轨道或新的 rank 代替这个主要控制问题。

即使这样的块已经取得，(20)或(27)的整个第四 period、其余全词规范、高阶与有限非零参数、嵌入、reach 和幅度仍须继续支付。本文给出的确切进展，是把第三返回从一个独立“先清零”的任务，改成可由真正入历史倒行准确完成的实际组合机制。

### 本稿直接使用的原来源

- R56(2)–(8)：完整分子、同锚恢复、ruling 与 characteristic 积分；
- R73(15)–(17)：变化-profile chain、全部第二密度与第三有序组合；
- R482 未消历史的(23)(24)：固定 $w,\chi$ 及真正全局 $q,b$；
- R521：本文同一第一圆、二阶三矩、第三四通道与实际反馈控制；
- R523 §§2、4–8：时间反射、重锚与 frame／位置／第四成本的准确范围；
- R183(1)–(3)：只对当前导数分包库授予的原 hook 逐函数盲性。

全稿以上述原式直接推导；没有新的科学执行，也没有把充分完成规则写成原主目标已经实现。
