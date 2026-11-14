# R89：常态 pair 的完整协变律、正长度多 pair 与七维物理二阶族

日期：2026-11-14。**已证明。** 本文转向 [R87](R87-exact-complete-P1-separation-and-smooth-moment-circles.md) 尚未排除的多个不同常态 pair。所有 pair 使用同一个全局 profile、同一个右锚以及同一个固定目标；它们可以有独立的真实内部桥。本文不允许把正 bulk 长度当作任意有符号系数。

结果来自真实曲面和逐阶 range 的相似变换，不是仅对某个 pure 对角公式作变量代换。它给出一个有限的完整两模式联合目标；尚未证明该目标可解，也未运行新的研究计算。

## 1. 整条真实路径的变换

先取任一已有真实路径，标量为 $h(s)>0,k(s),\omega(s)$，满足

$$\omega_s=\frac{k_s}{2h}.$$

正交标架满足

$$T_s=kN,\qquad N_s=-kT-B,\qquad B_s=N,$$

中心线为 $\alpha_s=h^2T$。使用全局 characteristic 坐标 $\xi$，记

$$u=\frac{h}{\xi+\omega},\qquad w=h^2-ku,\qquad X=\alpha+uN.$$

这里 $u$ 是实际 ruling 坐标。下面把新的 profile 坐标记作 $x$，避免与它混用。

固定常数 $H>0,d\in\mathbb R$，定义一条新真实路径

$$\widetilde h=Hh,\qquad \widetilde k=k,\qquad
\widetilde\omega=\frac{\omega+d}{H},\qquad
\widetilde\alpha=H^2\alpha,$$

标架不变。它准确满足

$$\widetilde\omega_s=\frac{\widetilde k_s}{2\widetilde h},\qquad
\widetilde\alpha_s=\widetilde h^2T.$$

在新路径的全局坐标 $\xi$ 上置

$$x=H\xi+d.$$

旧路径以 $x$ 为 characteristic 坐标。于是

$$\widetilde u(s,\xi)=H^2u(s,x),\qquad
\widetilde w(s,\xi)=H^2w(s,x),$$

$$\boxed{\widetilde X(s,\xi)=H^2X(s,H\xi+d).}\tag{1}$$

这是实际空间中的相似变换加参数变换；全部 frame 和 scalar 常值端芽、拼接关系、frame 端点都保留。中心线位移乘 $H^2$，不能假称单桥位移不变。

定义 profile 输运

$$(C_{H,d}\phi)(x)=\phi\!\left(\frac{x-d}{H}\right).$$

共同右端 $r$ 同时变为 $Hr+d$。准确链式法则是

$$C_{H,d}D_\xi=H D_xC_{H,d},\qquad
C_{H,d}I_\xi=H^{-1}I_xC_{H,d}.\tag{2}$$

不允许只把坐标多项式中的 $\xi$ 换掉，却漏掉导数和右积分的比例。

## 2. 全场、全历史和完整两模式的协变

无穷小场是

$$Y_\phi=uB\phi-\frac{uT+wB}{2h}\phi_\xi.$$

将 (1)–(2) 代入，直接得到

$$\boxed{\widetilde Y_\phi(s,\xi)
=H^2Y_{C_{H,d}\phi}(s,H\xi+d).}\tag{3}$$

固定同一右 collar、同一 $s$ 起点及 canonical 历史/gauge。线性化度量和全部高阶 forcing 在 (1)、(3) 下同乘真实相似变换并拉回。若旧的某阶校正场为 $Z_n$，则

$$\widetilde Z_n(s,\xi)=H^2Z_n(s,H\xi+d)\tag{4}$$

解相应的新方程，且具有变换后的同一锚与历史。可由 R56 的唯一 canonical 积分恢复逐阶确认：法向标量按空间长度乘 $H^2$，分解中 $-Y_W$ 的 profile 历史则仅作 $W(\xi)=W_0(H\xi+d)$。

因此，输出作为 profile scalar 的二阶算子、完整第三算子、第四周期 scalar 都没有额外的 $H$ 幅度因子。若 $\mathcal T_0$ 是旧路径的完整外槽第三算子，则新算子为

$$\boxed{\mathcal T_{H,d}(a;b,c)
=C_{H,d}^{-1}\mathcal T_0(C_{H,d}a;C_{H,d}b,C_{H,d}c).}\tag{5}$$

式 (5) 包括全部真实 $s$ 历史和右原函数常数，不以置零传入历史代替它们的导数。它也覆盖 R78 的 $\mathcal K,\mathcal L$ 和两个模式：只要全部输入同步输运，整个 $P_{1,-4},P_{1,-2}$ 都按输出 $C^{-1}$ 变换。

特别地，若不同 pair 都使用同一个全局 $f,g$，在各自标准坐标中使用的是 $C_{H_j,d_j}f,C_{H_j,d_j}g$。**不能为每个 pair 重新选择无关的 profile 圆。**

## 3. 真实第三仿射类与控制空间保持

标准互反端口为

$$h=1,\quad k=+1,-1,\quad\omega=+1,-1.$$

变换后正是

$$h=H,\quad k=+1,-1,\quad
\omega=\frac{d+1}{H},\frac{d-1}{H},\tag{6}$$

所以两端都具有同一个 $d=h\omega-k$。

变换给真实路径之间的双射：反变换用 $H^{-1}$ 和相应平移即可。它保 frame 端点，保 $M=0$，并按 (5) 输运第三仿射类。因此可取标准基准 $T_0^{\rm end}$ 的变换作为新端口的真实基准。

还需说明同一个 $\mathcal W$ 是否可以用于所有端口。设某真实 $M=0$、frame $I\to I$ 控制环在 scalar germ $g_1$ 上给第三改变量 $\tau$。取 R70 的真实 $M=0$、frame $I\to I$ 连接 $B:g_0\to g_1$。接 $B$、该环、$B$ 的真实倒行，则全部 $M=0$；第三算子准确相加，而 $T_{B^R}=-T_B$，所以合成在 $g_0$ 上仍给 $\tau$。位置位移自由，不参与此第三算子论证。

故完整第三改变量空间与常值基点无关。再用上述双射，得到

$$\boxed{C_{H,d}^{-1}\mathcal W(C_{H,d}\cdot;C_{H,d}\cdot,C_{H,d}\cdot)=\mathcal W.}\tag{7}$$

R87 已证明这个真实空间恰为 36 维。

特别地，标准的完整五段基准在消去其已证 $\mathcal W$ 分量后有一个有理代表 $T_{\rm rat}$。一般端口可直接取

$$T_{{\rm rat},H,d}=C_{H,d}^{-1}T_{\rm rat}(C_{H,d}\cdot;C_{H,d}\cdot,C_{H,d}\cdot).\tag{8}$$

当 $H,d$ 有理时，(8) 的原始 profile 表达式仍有理。无需为每个新端口重新遗漏或猜测 $\mathcal C_1$ 成本；完整端点成本由协变保留。

所有辅助控制和连接只需有限条。构造后其 scalar 轨迹紧，$h$ 有正下界；可以在全部有限路径许可的同一物理支上选共同 profile 区间。这里没有给任意外加的统一控制盒、固定最大长度或任意预先指定窄区间的可达性保证。新加的连接与控制环仍会改变 $P_0$。

## 4. 正常态二阶算子的准确八坐标

对 (6) 的正 $k=1$ 常态，令 $x=H\xi+d$，$Q=1+x^2$，$L=x^2-1$。其单位真实 $s$ 长度二阶算子为

$$\begin{aligned}
\mathcal A_{H,d}(f,g)={}&\frac{x}{2}fg-
\frac{Q}{4H}(fg'+f'g)+\frac{xQ}{4H^2}f'g'\\
&+\frac{L}{8H^3}\int_\xi^r
\{[1+(H\eta+d)^2]f''(\eta)g''(\eta)+2H^2f'(\eta)g'(\eta)\}\,d\eta.
\end{aligned}\tag{9}$$

这是 (2) 对标准 $\mathcal A_{1,0}$ 的直接共轭；负常态为 $-\mathcal A_{H,d}$。

按 $\mathcal P=(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$ 的实际 trace-zero 矩算子约定，(9) 的坐标准确为

$$\boxed{\begin{aligned}
p_0&=-\frac{1+d^2}{2H},&p_1&=-d,&p_2&=-\frac H2,\\
r_0&=\frac{d^4-1}{8H^3},&r_1&=\frac{d(1+d^2)}{4H^2},\\
s_0&=\frac{d(d^2-1)}{4H^2},&s_1&=\frac{d^2}{2H},&t_1&=\frac d4.
\end{aligned}}\tag{10}$$

例如 $H=1,d=0$ 回到已经使用的 $(-1/2,0,-1/2,-1/8,0,0,0,0)$。

这族有准确的线性限制

$$p_1+4t_1=0.\tag{11}$$

其线性 span 恰为七维，而不是八维。证明：设一个线性泛函在所有 (10) 上为零，乘 $8H^3$ 后按 $H,d$ 的多项式系数比较。$H^0d^4$ 先迫 $r_0$ 对偶系数为零；$Hd^3,Hd$ 迫 $r_1,s_0$ 对偶系数均为零；$H^2,H^2d^2$ 迫 $p_0,s_1$ 对偶系数为零；$H^4$ 迫 $p_2$ 对偶系数为零。只剩 $H^3d$ 的关系，恰是 (11)。所以 annihilator 一维。

固定任意 $H>0$、只变化 $d$ 时，(10) 为 $d$ 的四次多项式，五个系数向量独立：依次看 $p_2,p_1,s_1,r_1+s_0,r_0$ 即可，故此时 span 为五维。

另一个直接的正性限制是

$$p_2(\mathcal A_{H,d})=-H/2<0.$$

所以若 $\ell_j>0$，则 $\sum_j\ell_j\mathcal A_{H_j,d_j}$ 的 $p_2$ 坐标严格负。不能用两个合法正 bulk 状态冒充一对任意正负二阶系数。

## 5. 多 pair 的真实相加与连接成本

取有限个状态 $(H_j,d_j)$。第 $j$ 个 pair 由正 bulk、真实 $M=0$ 内部桥 $B_j$、同长负 bulk 组成。设每个 bulk 的真实长度为 $N\ell_j$，$\ell_j>0$。内部桥在 $N$ 变化时保持固定，scalar 端口为 (6)，frame 端点也真实支付。

相邻 pair 之间可用 R70 的真实 $M=0$ 连接，改变 scalar 常值 germ。它们通常具有非零第三成本、非零位移和非零第四成本；这里不删除这些量。

为何这些跨 pair 连接不新增 $P_1$：一个完整互反 pair 结束时，最高 second 历史 $w$ 和最高 third 历史 $v$ 都准确回零。$M=0$ 连接在 $w=v=0$ 时的第四 $N$ 一次项为零；其新增的 $U_0$ 在下一个正负 pair 的两段 bulk 中相消。这是 R70/R71 的真实历史递推，不是逐段重设零锚。连接内部的低阶历史和其第四成本仍进入 $P_0$。

所有 pair 与连接各有 $M=0$。最后可选一个真实 $M=0$ 连接，使单路径 $P$ 的 scalar 端芽回到初态、frame 由 $I$ 到 $D$；按 R45 的四块组装 $P,P,P^R,P^R$，真实 frame 与中心位移闭合。此时完整 $P_1$ 是以下和的四倍；闭合不要求每个单桥的位移预先指定。

令 $b_{H,d}$ 表示该状态常态目标加 (8) 的完整两模式响应，令 $\mathcal B_{\mathcal A_{H,d}}$ 是 R78 对第三控制的线性响应。则除去共同四块因子，总条件准确为

$$\boxed{\sum_j\ell_j\left[
b_{H_j,d_j}+\mathcal B_{\mathcal A_{H_j,d_j}}(S_j)\right]=0,
\qquad S_j\in\mathcal W.}\tag{12}$$

每一项都是两个完整复函数；两个模式以及全部 $\xi$ 使用同一组真实参数。不同 pair 的 $S_j$ 可以独立选择。

因为 $\mathcal W$ 是真实向量空间，固定的非零正 $\ell_j$ 可吸收到各 $S_j$ 中；所以控制响应空间是

$$\sum_j\mathcal B_{\mathcal A_{H_j,d_j}}(\mathcal W).\tag{13}$$

但基准目标仍是**正权和** $\sum_j\ell_jb_{H_j,d_j}$。式 (13) 不能把它变成任意有符号组合。若两状态完全相同，(12) 退化为同一单 pair 问题，增加重复 pair 不扩大该响应空间。

## 6. 完整圈数与正有理权

在 $k=\pm1$ 上，frame 的完整周期时长为

$$T=\frac{2\pi}{\sqrt2}=\sqrt2\pi,$$

与 $H,d$ 无关。为保持固定桥和整数参数 $N$ 的同一物理设计，可严格取

$$\ell_j=n_jT,\qquad n_j\in\mathbb N_{>0}.$$

如果准确代数先找到严格正的有理相对权重，可以共同清分母，得到这样的完整圈数；统一正比例不会改变零条件。本文不把任意实权自动解释成固定桥下的完整周期圈数，也不把一个负权解释成反向真实正长度。

最小的新联合目标可以直接取两个等长 pair：

$$\boxed{(H_1,d_1)=(1,0),\qquad(H_2,d_2)=(1,1),\qquad n_1=n_2=1.}\tag{14}$$

两个常态组的 $H$ 和 $d$ 有界，四个端口的 $\omega$ 分别为 $1,-1,2,0$。整条标准五段 scalar 路径只需整体平移 $\omega$ 即可产生第二组的端点代表；真实 $M$/frame 修复仍按已证空间支付，而不声称这些修复已有给定的小长度或 reach。

## 7. 可直接计算的有限联合目标

对已有 36 个标准模板 $T_i$，第 $j$ 个状态可用其真实共轭

$$T_{j,i}=C_{H_j,d_j}^{-1}T_i(C_{H_j,d_j}\cdot;C_{H_j,d_j}\cdot,C_{H_j,d_j}\cdot).$$

由 (7)，这些仍各自张成同一个真实 $\mathcal W$。于是 (14) 给至多 72 个联合响应列，目标为 $b_{1,0}+b_{1,1}$；两项权重严格为正。

原式实现可以只编译一次标准目标和标准响应，再作准确 pullback。对一个标准原始 monomial/primitive，规则是

$$x\mapsto H\xi+d,\qquad q_x^{(m)}\mapsto H^{-m}q_\xi^{(m)},\qquad
I_x(F)\mapsto H I_\xi(\operatorname{pullback}F).\tag{15}$$

全部颜色和原函数递归用同一规则，共同右锚同步变化。这保留同一全局 profile；无需重新编译变量几何 $\mathcal C_1$。

72 列**不预设真实独立**。下一准确算法应先在完整两模式上作有声的 word 消元，对每条丢列关系回到原始双模式表达式 fresh 验零，得到真实响应空间维数的上界 $r$。若发现正关系，必须从原式同时复核两个全函数。若只剩未消代表，再用同一真实有理 profile、同一右锚直接评价原式；只有模控制秩达到该已证明上界 $r$ 且有非零 $(r+1)$ 阶增广子式，才给真正非成员证书。

因此 R87 的单 pair 负结论没有被静默外推，也没有靠给同一单 pair 追加已属于其完整 36 维空间的列来重复尝试。这里改变的是两个不同的真实二阶 bulk 状态及其共同正权和。

## 8. 已付与未付

本文已付整路径/全场/完整外槽与两模式的协变律，实际第三仿射类的变换，正 bulk 族的七维精确 span，多 pair 的真实历史相加和正圈数约束，以及一个独立有限联合目标。

没有支付 (12)，没有把任何 word 负代表当成真实非成员；也没有让跨 pair 连接的 $P_0$、位移或长度消失。后续仍需处理完整 $P_0+NP_1$、第四 ruling、更多高阶、收敛、闭面嵌入、reach 与宏观幅度。
