# R476：完整十八维第三核在不交 rank-one 圆上逐函数不可见，并消去真实第三 prototype 的全部重复漂移

日期：2026-11-16。**新的纸面推论；没有执行符号程序、原根恢复、profile 求积、数值秩、开发检查或科学任务。**

本稿处理 [R472](R472-two-level-prefix-reset-and-unavoidable-ruling-in-actual-return-bridges.md)(34) 的一个完整实际分支。结论比三个 outer 矩为零更强：对当前真紧、严格不交的 rank-one 母包库，原完整第三对角核 $Z$ 的每个成员在整个 profile 平面的三个槽上都为零。因此，一个真实 $A_B=0,\ T_B\in Z$ 的第三 prototype，即使 $T_B$ 作为 universal 算子非零，也不改变该圆的完整第三传入 profile；其任意有限重复的所有内部 ruling 函数均相同。

这里使用的是 [R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md) 已付的完整同锚局部算子身份。不是把 R183/R326 的 cubic 八副本消去外推到 quartic 条件，也不删任何左尾。对整个 $W/Z$ 的剩余第三方向，本稿只给准确有限门，尚不宣它们在旧冻结库上已经支付；从起点增强有限观测的全 $W$ 版本另行处理。

## 1. 原空间、真实母包与完整右锚

沿 [R254](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md) 和 R261，令 $W$ 为原完整三槽第三空间，
$$
\Delta\tau(u)=\tau(u;u,u),\qquad Z=\ker\Delta.
\tag{1}
$$
这里 $\tau$ 对后二槽对称，所有算子使用同一个真实右锚
$$
Jv(x)=\int_x^{r_*}v(\xi)\,d\xi .
$$
已付结论是 $\dim Z=18$；它由原十维 $Z_{71}$ 与八个完整 $\chi_j$ 构成。这是原完整算子的核，不是只看对角主项或丢尾后的核。

取有限个真实 $u_i\in C_c^\infty((\ell,r_*))$，其闭支撑彼此不交，支撑之间有开间隙。设
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
\mathcal P=\operatorname{span}_{\mathbb R}\{f,g\}.
\tag{2}
$$
各 $u_i$ 可以形状不同、平移不同、宽度不同；此处不要求共同母形、偶性或任何面积条件。关键是：在每个包内，$\mathcal P$ 的任意函数及其全部 jets 都是该 $u_i$ 的一个常数倍。

原圆和二次槽保持
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
\tag{3}
$$
当前 [R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md) 及后继同 cap 母库满足(2)。母包内部可以有多个简单 $u_i'=0$；本证明不要求单峰，也不使用 $A_{u_i}$ 零点的数目。

非零常平台、仅导数不交而函数值不交条件失败的其它类，不由下面的全 $Z$ 论证自动覆盖。[R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md) 对 $\mathfrak H$ 的更宽导数分包结论应保留其自己的范围。

## 2. R261 原完整表示中的两个必要性质

对任意 $\tau\in Z$，R261(3)–(5) 给
$$
K_v^\tau(w):=\tau(w;v,v)
=-J^3\bigl(\mathscr A_{\tau,v}w\bigr),
\tag{4}
$$
$$
\mathscr A_{\tau,v}
=D_x^2(a_{\tau,v}D_x^2)+D_x(b_{\tau,v}D_x)+c_{\tau,v},
\qquad
\mathscr A_{\tau,v}v=0.
\tag{5}
$$
系数都是有限、局部的 $v$-jet 多项式，并且对 $v$ 齐次二次。后者既可从 R261 全系数表读出，也由原 $K_v^\tau$ 对 $v$ 二次的槽结构得到。

因此，在任意开区间上若 $v=\beta u,\ w=\alpha u$，$\alpha,\beta$ 为常数，则完整微分算子有
$$
\mathscr A_{\tau,v}w
=\alpha\beta^2\mathscr A_{\tau,u}u=0.
\tag{6}
$$
这包括 $\alpha=0$ 或 $\beta=0$；没有除以幅度或 profile 值。

(4)包含原右零 collar 的三个初值
$$
K_v^\tau(w)(r_*)=\partial_xK_v^\tau(w)(r_*)
=\partial_x^2K_v^\tau(w)(r_*)=0.
\tag{7}
$$
所以“三阶导为零”在这里确实推出完整原函数为零。若不保(7)，只能得到一个未定二次多项式，不能作下节结论。左侧的值不是另外归零；它由同一个(4)决定。

## 3. 全部三个槽的逐函数消失

**定理 1。** 在(2)的真实 profile 平面上，
$$
\boxed{\tau(a;b,c)=0
\quad\text{作为整个 }[\ell,r_*]\text{ 上的函数，}
\quad a,b,c\in\mathcal P,\quad\tau\in Z.}
\tag{8}
$$

**证明。** 先取 $a,b\in\mathcal P$。在第 $i$ 个包的邻域写
$a=\alpha_i u_i,\ b=\beta_i u_i$。由(6)，
$\mathscr A_{\tau,b}a=0$。所有包之间，$a,b$ 及其全部 jets 为零，局部齐次二次系数也为零。包端点真平，故这些逐区间等式拼成整个区间上的光滑函数恒等
$$
\mathscr A_{\tau,b}a=0.
$$
没有分布边项，也没有把不连续的系数比值拿来微分。

代入完整(4)–(7)，得到 $\tau(a;b,b)=0$。对后二槽作真实极化，
$$
2\tau(a;b,c)
=\tau(a;b+c,b+c)-\tau(a;b,b)-\tau(a;c,c)=0.
$$
这证明(8)。证毕。

因此原八个新 $\chi_j$ 与原十维 $Z_{71}$ 在此平面上共同不可见。它们在 universal 第三空间中仍是十八个真实非零方向；(8)只是对这一个明确 profile 类的完整限制，不是把 $Z$ 本身商掉。

由(3)、(8)立即得到
$$
\boxed{\tau(\phi_\theta;D_\theta)=0
\quad\text{对全部 }\theta,\quad\tau\in Z.}
\tag{9}
$$
同样，$\tau(g;f,f)$、$\tau(f;g,g)$ 等完整 mixed 槽也为零。整个相位恒等直接来自三线性限制，不是有限角采样。

## 4. 三个真实 outer 矩与 R472 重复系数

保原配对
$$
\begin{aligned}
I_0(u,v)&=\int u''v'',\\
I_1(u,v)&=\int xu''v'',\\
I_2(u,v)&=\int\{x^2u''v''+2u'v'\}.
\end{aligned}
\tag{10}
$$
对一槽紧的物理第一场配对，原 [R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md) 给
$$
\mathcal E_s(u,v)
=\frac{1+d(s)^2}{4h(s)}I_0(u,v)
+\frac{d(s)}2 I_1(u,v)
+\frac{h(s)}4 I_2(u,v),
\quad d=h\omega-k.
\tag{11}
$$
(9)当然使三个原矩及整个物理配对为零。事实上本节不需要用(11)消尾：第二输入在(9)中已经是完整零函数。

对一个真实回到相同 scalar/frame 的块 $B$，原 R472(34) 在 $A_B=0$ 时是
$$
\mathscr C_2=0,\qquad
\mathscr C_1(s,\theta)
=-4\mathcal E_s\{\phi_\theta,T_B(\phi_\theta;D_\theta)\}.
\tag{12}
$$
若 $T_B\in Z$，由(9)得到
$$
\boxed{\mathscr C_1=\mathscr C_2=0
\quad\text{对该块的全部内部 }s\text{ 与全部相位。}}
\tag{13}
$$
这里 $s$ 可以位于非恒 $\omega$ 的返回桥内；没有把几何限制为已付 rational germ。

特别，原非零 hook $\mathfrak H=[P,S]-3[P,R]\in Z$ 自动满足(13)。这是从完整十八维局部表示推出的统一结论，无需对 $\mathfrak H$ 重新计算三个 quartic 外矩。

## 5. 更强的真实传入不变性与唯一规范

原 R472 的完整传递为
$$
\begin{aligned}
a'&=a+A_BD_\theta,\\
b'&=b-2T_B(\phi_\theta;D_\theta)+2A_B(\phi_\theta,a).
\end{aligned}
\tag{14}
$$
因此 $A_B=0,\ T_B\in Z$ 时，
$$
\boxed{a'=a,\qquad b'=b}
\tag{15}
$$
对任意原允许的完整 incoming $a,b$ 都成立；不要求 $a$ 或 $b$ 属于 $\mathcal P$。

于是有限次重复同一个真实 $B$，每次入口的整个二、三阶历史一致。对每个相同局部位置，原零入口场以及同一个真实 $a,b$ 给出的物理二、三阶场也相同，至多有共同环境刚体位移或转动。因此不仅(13)成立，而且
$$
\boxed{\mathscr K_j(s,\theta)=\mathscr K_0(s,\theta)}
\tag{16}
$$
对所有实际副本精确成立。

这里从头到尾只有一个最终全局 $w_\theta,\chi_\theta$。若第一次入口来自真实前缀 $(A_{\rm pre},T_{\rm pre})$，其值仍为
$$
a=w_\theta+A_{\rm pre}D_\theta,\qquad
b=-\chi_\theta-2T_{\rm pre}(\phi_\theta;D_\theta)
+2A_{\rm pre}(\phi_\theta,w_\theta).
\tag{17}
$$
本稿没有在每个块入口重新给三个第三 Gram 矩。对任意最终选定的这个规范，(15)(16)都成立；共同 $\mathscr K_0$ 是否为零仍是原未付局部方程。

更一般，串联若干不同的 $A_{B_i}=0,\ T_{B_i}\in Z$ 块，它们之间也没有二、三阶 incoming 漂移。不同块自身的 $\mathscr K_{B_i}^{(a,b)}$ 可以不同，必须在同一规范下分别支付；不能由传入一致推出各块内部 ruling 零。

## 6. 第四基准没有随第三不可见性消失

原完整第四传递在 $A_B=0$ 时仍是
$$
\boxed{
c'=c+V_B
+2T_B(a;D_\theta)-4T_B(\phi_\theta;\phi_\theta,a).
}
\tag{18}
$$
任意允许的 $a=w_\theta+A_{\rm pre}D_\theta$ 通常不在 $\mathcal P$；(8)不能用于删除(18)后两项。即使某个特殊 $a\in\mathcal P$ 使这两项为零，完整 $V_B$ 仍然保留。

对 $n$ 次同块重复，由(15)可准确写
$$
c_n=c_0+n\{V_B+2T_B(a;D_\theta)
-4T_B(\phi_\theta;\phi_\theta,a)\}.
\tag{19}
$$
这是同一真实有限词的第四增量，不把 $n$ 大解释成某个基准可忽略，也不把真倒行视为负成本。

不同 $A=0$ 块的 canonical $V$ 与 $T$ 在原完整合成中分别相加；总第四规范项按(18)随总 $T$ 相加。若最终指定总 $T=\tau\mathfrak H$，(18)正是原固定非零 $\tau$ 下 period 方程必须保留的项，不能因 $\mathfrak H$ 在 $\mathcal P$ 三槽上盲而丢掉它对一般 $w_\theta$ 的作用。

只有在同一最终背景、全部桥及 prototypes 已被纳入原 R468/R467 的联合目标后，才能使用其条件实际截面支付相应完整 $V$ 与最高行。本稿既不替代该条件，也不声称新增块的内部 ruling 已由成本观测支付。

## 7. 这确实可以作为真实第三分配，而不只是 formal 方向

[R80](R80-complete-third-affine-class-and-P1-endpoint-obstruction.md) 对原常数 scalar 端口给真实有限第三可控性：在固定返回 frame、整 $A=0$ 的类中，每个指定 $T\in W$ 都可由原有限控制词实现，所有第四基准保留。因而每个指定 $\tau_i\in Z$ 也有这样的真实块。

例如，对任意预先固定的有限个 $\tau_1,\ldots,\tau_m\in Z$ 和最终非零系数 $\tau$，取最后一个第三目标
$$
\tau_{m+1}=\tau\mathfrak H-\sum_{i=1}^m\tau_i\in Z.
\tag{20}
$$
按原 R80 分别实现，并在同一个已选共同窗口中串联；整 $A=0$ 使第三合成无额外 $A_2\circ A_1$ 项，故最终完整第三正是 $\tau\mathfrak H$。每个完成块都满足(15)，所以这个真实分配不会产生 R472(34) 的重复漂移。

这是有限实际分配的结论，不要求每个 universal $\tau_i$ 为零，也不要求以负时间实现负系数。参数若在一个有限紧盒中变化，使用原第三截面的同一真实基准和桥，并从起点固定共同合法窗口；未增加任意路径上的控制许可。

但实现一个 $\tau_i$ 的 R70/R71/R77/R79 子词内部可以含 $A\ne0$ 或第三前缀不在 $Z$ 的段。(15)只在完成整个指定块时给真实入口传递。其内部依然必须代入 R472(29)；本稿不能把整块结论下放给每座尚未闭合的子桥。

同样，在已经冻结的一条实际总词中，不能仅凭其总 $T=\tau\mathfrak H$ 把原有各块的 $T_B$ 改称属于 $Z$。若要采用(20)，需真实重新安排这些完整块，并重新保留最终的全部 $V$、窗口及同一个规范。

## 8. 一般完整第三只剩商像门，本稿不预授它已为零

对固定(2)定义真实线性映射
$$
\Theta_{\mathcal P}(T)
=\left(\theta\longmapsto
\mathbf I\{\phi_\theta,T(\phi_\theta;D_\theta)\}\right).
\tag{21}
$$
定理1证明
$$
Z\subset\ker\Theta_{\mathcal P}.
\tag{22}
$$
所以它经过原完整商 $W/Z\simeq\Delta W$ 因子化；已付的 $\dim\Delta W=18$ 是来源中的空间维数，不是本稿计算的 $\Theta$ 秩。

由于原槽次数，(21)的每个分量只含
$\cos^3\theta\sin\theta,\cos^2\theta\sin^2\theta,
\cos\theta\sin^3\theta,\sin^4\theta$。
三个外矩与一个十八维商基至多给 $18\cdot3\cdot4$ 个生成系数，可以冗余，不能据此声明秩为216。

若 $T_B$ 不在 $Z$，是否满足(12)必须按真实 $\Theta_{\mathcal P}(T_B)$ 和真实几何权判断。原 R326 的 $I_j(a,X(b,c))$ 为 cubic，不能作为(21)这个 quartic 门的零证。原六个 Gaussian pair 的外矩也不能在未证明张成关系时冒作整个十八维商已经支付。

本稿已经闭合的部分是：完整 $Z$ 对当前不交 rank-one 圆逐函数不可见、对应真实第三 prototype 的全部重复漂移精确为零、且这个分配可经原实际第三控制实现。未闭合的是剩余商方向、每一实际块自身的 $\mathscr K_0$、$A\ne0$ 子桥及同一个十三行规范下的全路径联合解。后续的全 $W$ 处理必须明确给出额外原式或从起点增强的有限观测，不能回写成旧冻结母库本来就具备的身份。
