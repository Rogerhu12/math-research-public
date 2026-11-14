# R83：真实第四历史传递与零低阶历史的可调方向

日期：2026-11-14。**已证明。** 纸面推导，无新的数值或完整研究编译。使用 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md) 的同锚恢复和 [R78](R78-complete-phase-P1-symmetric-square-conditions.md) 的完整相位响应。

本稿提供实际有限路径的第四阶传递公式，并构造一族首末 scalar/frame 相同、二阶矩阵与完整第三算子恒零的真实路径，其第四阶变化有明确可调切向。它保留未知的第四基准和偶次项；没有把第四响应冒称为零基线的准确线性控制。

## 1. 固定目标、相位与三个真实输入历史

固定共同右 collar 为零的 profiles 和共同物理区间，所有实际路径上 $h>0,\xi+\omega>0$。固定目标 $F\in\operatorname{Sym}^2\mathcal P$、第一 profile $\phi$，记

$$D=F-\phi^2.$$

一条实际路径 $B$ 的数据记为

$$A_B=\Phi_{M_B},\qquad T_B(a;D),\qquad V_B(F,\phi).$$

$A_B$ 是完整 second 算子，$T_B$ 是 R71 的完整第三算子；$V_B$ 是从零传入 second/third scalar 历史开始，按真实完整 forcing 恢复得到的第四 scalar 积分。所有右原函数及 $s$ 起点一致，左尾保留。$V_B$ 是整个 $\xi$ 函数，而不是一个数。

令进入该路径的 second、third、fourth scalar 历史为 $w,u,v$。这些是固定的右 collar 零 profile 值；路径内部真实 $s$ 演化由恢复式生成，不能把传入值与其后续导数混同。

记零传入 second 场为 $Z_B(D)=\mathcal I_BH_D$，零传入物理 third 场为

$$W_B(\phi,D)=\mathcal I_B[-2H(Y_\phi,Z_B(D))].$$

实际传入 $w,u$ 后，线性恢复准确给

$$Z_2=Z_B(D)-Y_w,$$

$$Z_3=W_B(\phi,D)+2Z_B(\phi,w)-Y_u. \tag{1}$$

式 (1) 是整个向量场身份；含所有 normal、mixed 及真实 history 导数，非仅 scalar 形式类比。

## 2. 完整第四传递式

把 (1) 代入物理 forcing

$$H_4=-H(Z_2,Z_2)-2H(Y_\phi,Z_3).$$

由 range 的线性性，路径末三个历史准确为

$$\boxed{\begin{aligned}
w'={}&w+A_B(D),\\
u'={}&u-2T_B(\phi;D)+2A_B(\phi,w),\\
v'={}&v+V_B
+2T_B(w;D)-4T_B(\phi;\phi,w)\\
&-A_B(w,w)+2A_B(\phi,u).
\end{aligned}} \tag{2}$$

例如第四式中的 $2T_B(w;D)$ 来自第二场平方的交叉项；$-4T_B(\phi;\phi,w)$ 来自第三 forcing 恢复中的 $2Z_B(\phi,w)$；最后一项是真实传入 third profile 的作用。这里不能省掉 $w$ 或 $u$，也没有把桥成本当成与入历史无关。

对先走 $B_1$ 再走 $B_2$、零初值的组合，(2) 给

$$A_{21}=A_1+A_2,$$

$$T_{21}(a;D)=T_1(a;D)+T_2(a;D)-A_2(a,A_1D),$$

以及

$$\boxed{\begin{aligned}
V_{21}={}&V_1+V_2
+2T_2(A_1D;D)-4T_2(\phi;\phi,A_1D)\\
&-A_2(A_1D,A_1D)-4A_2(\phi,T_1(\phi;D)).
\end{aligned}} \tag{3}$$

这恢复 R71 的第三 composition，并给出其真实第四扩展。不是预设某个形式 Lie 群与几何路径相同。

## 3. 零矩路径的真实倒行：第四成本同号

现在假设 $M_B=0$，采用 R45/R71 的同 $k$ 真倒行；首末 frame 已在同一规范中，ambient 正交变换记为 $O$。有

$$Y^R=-O Y\circ\mathrm{rev},\qquad
Z_2^R=O Z_2\circ\mathrm{rev}.$$

令 $b=-2T_B(\phi;D)$ 为原路径的 third scalar 末值。第三 forcing 在倒行下为奇，故其 canonical scalar 是 $u_B(L-s)-b$。因此第三场准确为

$$Z_3^R=-O Z_3\circ\mathrm{rev}+Y^R_b. \tag{4}$$

这里最后一项是保持真实起点零锚所需的端历史修正，不能删去。将 (4) 代入第四 forcing，与原 forcing 的倒行拉回相比，只多出

$$-2H(Y_\phi,Y_b).$$

其周期积分是 $-2A_B(\phi,b)=0$，因为整个矩阵 $M_B$ 为零。故

$$\boxed{M_{B^R}=0,\qquad T_{B^R}=-T_B,
\qquad V_{B^R}=+V_B.} \tag{5}$$

特别地，若两路径都 $M=0$，(3) 中的全部交叉项消失，$V$ 直接相加；它们的第三算子仍可能非零。若再有 $T=0$，第四成本仍不能用倒行取负。第三阶已成功的“路径加另一条路径倒行以取差”的操作，不能未经修改照搬到第四阶。

## 4. 一族真实零二、三阶路径

取任意无迹矩阵算子 $P$。R70 给同一 scalar 常态、frame $I\to I$ 的一条实际光滑路径族 $A(t)$，满足

$$M_{A(t)}=tP.$$

参数只在固定小区间，所有辅助圈数与拼接方式固定。其真实 $T_{A(t)},V_{A(t)}$ 未知，完整保留。

再取任一已有的真实第三控制族 $L(\lambda)$，首末同一 scalar/frame，满足

$$M_{L(\lambda)}=0,\qquad T_{L(\lambda)}=\lambda\tau.$$

$\tau$ 可以是 R71、R77、R79 已实现的任一完整第三方向。$L(0)$ 一般不是空路径；它的第四成本也不置零。先固定一个允许范围内的 $\lambda$。

定义真实词

$$W(t,\lambda)=A(t)\,L(\lambda)\,A(-t)\,L(\lambda)^R. \tag{6}$$

由 (3)、(5)，

$$M_W=0,$$

$$\boxed{T_W=T_{A(t)}+T_{A(-t)}+t^2P\circ P,} \tag{7}$$

其中 $(P\circ P)(a;D)=P(a,PD)$。式 (7) 对 $t$ 为偶函数，并与 $\lambda$ 无关；这包括所有未知自身第三成本。

现在取

$$\boxed{Z(t,\lambda)=W(t,\lambda)\,W(-t,0)^R.} \tag{8}$$

第二条路径整体矩阵为零，故 (5) 合法适用。由 (7)，(8) 对全部小 $t$ 精确满足

$$\boxed{M_Z=0,\qquad T_Z=0.} \tag{9}$$

这是真实有穷拼接，端 scalar/frame 全部保持。空间末位移自由，可由同一个修改后的单 P 四块组装处理；没有指定单词自身位移为零。

## 5. 第四变化的准确奇部与保留的基准

令 $a=PD$。逐段代入 (2)，比较 $W(t,\lambda)$ 与 $W(t,0)$，准确得到

$$V_{W(t,\lambda)}-V_{W(t,0)}
=2\{V_{L(\lambda)}-V_{L(0)}\}+\lambda t\,K_{P,\tau}(F,\phi), \tag{10}$$

其中

$$\boxed{K_{P,\tau}(F,\phi)
=2\tau(PD;D)-4\tau(\phi;\phi,PD)
+4P(\phi,\tau(\phi;D)).} \tag{11}$$

式 (11) 的最后一项来自中间 $L(\lambda)$ 新增加的 third 历史在 $A(-t)$ 中的作用；忽略该项会改变控制方向。

由于 (8) 两条大块的矩阵都为零，第四成本相加。令

$$E(t)=V_{W(t,0)}+V_{W(-t,0)},\qquad E(-t)=E(t).$$

由 (5)、(10) 得到整个函数身份

$$\boxed{V_{Z(t,\lambda)}
=E(t)+2\{V_{L(\lambda)}-V_{L(0)}\}
+\lambda t\,K_{P,\tau}.} \tag{12}$$

因此

$$\boxed{\left.\partial_tV_{Z(t,\lambda)}\right|_{t=0}
=\lambda K_{P,\tau},} \tag{13}$$

并且准确奇部为

$$\boxed{V_{Z(t,\lambda)}-V_{Z(-t,\lambda)}
=2\lambda t K_{P,\tau}.} \tag{14}$$

这是由真实路径推出的可调第四切向；不是把 (14) 的函数差擅自说成可以靠再接一个倒行路径实现。倒行第四仍同号。

特别保留

$$V_{Z(0,\lambda)}=4V_{A(0)}+2V_{L(\lambda)}+2V_{L(0)}, \tag{15}$$

以及 $E(t)-E(0)=O(t^2)$。这些未知函数一般不为零。当前构造提供的是带实际基准的光滑可调族；要用有限维 IFT 支付具体 $P_0$，仍须匹配该基准并证明所选方向在所需函数范围的满秩条件。

## 6. 与完整 P1 响应的关系

式 (11) 恰是 R78 的第三控制对完整 P1 的桥响应，只是正 second 算子不必取特定的 $\mathcal A$，现在 $P$ 可以取任意实际八矩方向。因而已有两模式编译可以作为这些第四切向的准确代数输入。

这个联系不能倒过来把已经支付 P1 当成 P0 已支付：P1 计算中，第三控制的响应线性且可真实实现；本稿第四族还有 (15) 及偶项。所有相位还必须共用同一组真实参数，不能对某个 $\phi$ 单独选择路径。

更直接地，由 (2)，任意 $M=T=0$ 的插入块对任何传入 $(w,u,v)$ 都只作

$$(w,u,v)\longmapsto(w,u,v+V_Z).$$

所以插入 (8) 保持整个单 P 的 $M,T$ 及已经支付的全部 $P_1$，不产生新的外圈数 $N$ 耦合。在已经含有 $Z(0,\lambda)$ 的真实基准上，将它换为 $Z(t,\lambda)$，再对同一个修改后单 P 作 R45 四块组装，第四常项的准确变化是

$$\boxed{\Delta P_0=4\{E(t)-E(0)+\lambda tK_{P,\tau}\},\qquad
\left.\partial_t\Delta P_0\right|_0=4\lambda K_{P,\tau}.}$$

四块同一设计和 R58 的全历史约定保持；这提供的是实际基准附近的 $P_0$ 调节方向，没有减去 (15) 的未知基准成本。

对若干 $(P_j,\tau_j)$ 串联 (8)，每个大块的 $M,T$ 都为零，故第四成本直接相加，切向是这些 $K_{P_j,\tau_j}$ 的真实线性组合。但基准也一起相加，未取得自由的负基准或一个非平凡零第四成本环。

## 7. 已付与未付

已付真实输入历史传递、带原锚修正的倒行符号、精确零矩/零第三的有限控制族，以及第四切向的明确全相位函数。未知第四自身成本没有从公式中消失，只被限制到基准和偶部。

仍未付真正 $V=0$ 的非平凡基准、基准的正性/可控锥问题、完整 $P_0$ 的匹配、第四 ruling、无限阶、有限等距族、嵌入及 reach。是否存在严格正性泛函或可用其他真实设计抵消 (15)，应单独研究，不能用形式交换子名称代替证明。
