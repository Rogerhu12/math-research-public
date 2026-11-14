# R58：第四阶周期门的全部低阶 gauge 不变性与准确单 P 约简

日期：2026-11-14。literature推导；repo_sources独立全文核；root逐项对R45/R56真实恢复与反射复核。完整代数与对称证明，没有新的几何或profile数值研究。

本稿只针对 [R45](R45-reversal-four-block-third-period-cancellation.md) 的准确四块几何 $P,P,P^{\rm rev},P^{\rm rev}$，以及已通过完整第三阶的 profile 圆。它把第四阶**周期函数**的计算准确减为 canonical 单 P 计算，并证明任何合法第二、第三 profile gauge 都不能改变这个周期函数。它不声称逐 ruling 条件也 gauge 不变，更没有支付一个实际第四阶周期条件。

## 1. 真实模型与算子

保持 R45 的全部假设：P 的 frame 由 I 到 $D=\operatorname{diag}(-1,1,-1)$；标量首末为相同常值芽；单 P 的完整二阶周期算子 $M_P=0$。完整长度 $L=4\ell_P$，全局反射为

$$\tau(s,u)=(L-s,u),\qquad X\circ\tau=DX.$$

取固定 profile 圆 $\phi_\theta=\cos\theta f+\sin\theta g$，以及同一个目标

$$g_\epsilon=g_X+\epsilon^2(dY_f)^2.$$

以下逐个 theta 证明，不要求待比较的 gauges 只有有限个 theta 谐波。省略 theta 下标，记 $Y=Y_{\phi_\theta}$。普通对称双线性张量为

$$H(A,B)=\mathcal S(A,B)/2.$$

设 $\Pi_G(H)(\xi)$ 是在路径 G 上，以同一个右 collar 积分 rho 后得到的**完整** characteristic RHS 积分，亦即 R56 的整个周期函数；它对 H 线性。记全四块为 $\Pi$，单 P 为 $\Pi_P$。

R45 的 $M_P=0$ 及极化给

$$\Pi_P H(Y_a,Y_b)=0,\qquad
\Pi H(Y_a,Y_b)=0\tag{1}$$

对任意光滑紧支撑 profiles a、b 成立。这里不需要其交叉 ruling 矩为零；(1) 只支付周期门，不能取代另一条 range。

若 H 的两条完整 range 已支付，以全局 s 起点、零标量初值和右 collar 锚恢复场，记为 $\mathcal I H$。在证明涉及的场中，所需 ruling 条件会明确来自已假定存在的解，或已构造的第三阶圆。

## 2. 反射下的两条基本消去规则

R45 的真实无穷小场满足

$$Y_a\circ\tau=-DY_a.$$

canonical 二阶解

$$Z=\mathcal I\{H(Y_f,Y_f)-H(Y,Y)\}$$

满足 $Z\circ\tau=DZ$。这使用单 P 周期为零，使其标量 W 在每个 P 末端真正回零；不是逐段重置。

更一般地，若 $H(Y_a,Y_b)$ 的 ruling 条件成立，则其 canonical 恢复也满足

$$\mathcal I H(Y_a,Y_b)\circ\tau
=D\mathcal I H(Y_a,Y_b).\tag{2}$$

这是 R45 对平方 forcing 的同锚证明的双线性极化。P 上完整周期为零由 (1) 给出；右 collar 锚和反向两个端点的真实 W 值给 W 反号，最终向量场为偶。

任意 forcing 若满足 $\tau^*H=-H$，其右锚 rho 和完整 characteristic RHS 同为奇，因此

$$\Pi(H)=0.\tag{3}$$

(3) 本身不要求另一 collar 的 ruling 已支付。因此，由偶 Z、奇 $Y_a$ 和 (2)，

$$\Pi H(Z,Y_a)=0,$$

$$\Pi H(Y_b,\mathcal I H(Y_c,Y_d))=0\tag{4}$$

在相应恢复有定义时成立。这里的整个函数为零不来自 xi 采样。

## 3. 第四 period 对所有合法第二、第三 gauges 不变

假设已经有周期双 collar 的第三场 W，使

$$\mathcal L_XZ=H(Y_f,Y_f)-H(Y,Y),\qquad
\mathcal L_XW=-2H(Y,Z).\tag{5}$$

第四 forcing 为

$$F_4(Z,W)=-H(Z,Z)-2H(Y,W).\tag{6}$$

任取另一组满足同一 (5)、同一第一场和同一固定目标的周期双 collar 场 $\widetilde Z,\widetilde W$。由既有齐次场分类，存在光滑紧支撑 profile chi，使

$$\widetilde Z=Z+Y_\chi.$$

两条第三方程相减得

$$\mathcal L_X(\widetilde W-W)=-2H(Y,Y_\chi).$$

因此 $H(Y,Y_\chi)$ 的 ruling 必为零；周期门由 (1) 为零，故 $B_\chi=\mathcal I H(Y,Y_\chi)$ 确实是周期双 collar 解，而非未付相容性的形式对象。再次用齐次分类，

$$\widetilde W=W-2B_\chi+Y_\psi\tag{7}$$

对某个紧支撑 psi 成立。直接展开 (6)–(7)，

$$\begin{aligned}
\Pi\{F_4(\widetilde Z,\widetilde W)-F_4(Z,W)\}
={}&-2\Pi H(Z,Y_\chi)-\Pi H(Y_\chi,Y_\chi)\\
&+4\Pi H(Y,B_\chi)-2\Pi H(Y,Y_\psi).
\end{aligned}\tag{8}$$

第一、第三项由 (4) 为零；第二、第四项由 (1) 为零。所以

$$\boxed{\Pi F_4(\widetilde Z,\widetilde W)=\Pi F_4(Z,W).}\tag{9}$$

先与 canonical Z 比较即可证明任意两组合法解得到同一周期函数。它对全部 theta 分别成立，故即使 gauges 使用更多 theta 谐波，也不能改变 canonical 编译器给出的五个第四周期谐波。

**范围。** 结论不是“任意第二 gauge 都保第三可解”。证明只比较已经合法的两组二、三阶解；若某个 chi 破坏第三 ruling，它根本不属于比较对象。第四 ruling 的变化没有在 (8) 中被消去，所以 R56 的固定二阶解范围仍必须保留，不能据 (9) 删除其第二阶设计自由度。

## 4. 单 P 的真实第三历史与四块累计

以下取 canonical Z，以及第三场的全局零初始标量。完整第三 ruling 已支付，故其标量 primitive 和下面的段尾 profile 均在两个 collar 为零。

在第一个 P 上写第三 forcing 的恢复标量为

$$U_s=\mathcal R_{-2H(Y,Z)},\quad U(0,\xi)=0,
\qquad a(\xi)=U(\ell_P,\xi).\tag{10}$$

P 上的第三周期函数一般不为零；不能把 a 设为零。相同 P 的下一块具有相同 RHS，反向块则是该 RHS 的负反射。因此四块上的**实际连续**标量历史分别为

| 块 | 该块局部参数 $s\in[0,\ell_P]$ 上的标量历史 |
|---|---|
| P | $U(s)$ |
| P | $a+U(s)$ |
| $P^{\rm rev}$ | $a+U(\ell_P-s)$ |
| $P^{\rm rev}$ | $U(\ell_P-s)$ |

其端值依次为 $0,a,2a,a,0$。这张表没有隐去连接段，也没有为改善周期误差重锚。

恢复公式说明标量 U 加一个与 s 无关的 b 时，第三向量场准确增加

$$\frac Fz(b'/2,0,eb'/2-hb)=-Y_b.\tag{11}$$

因此，忽略不影响点积的共同空间刚体，第二 P 上第三场等于第一 P 上的 $W_P-Y_a$。第三反向块是第二 P 场的负反射，第四反向块是第一 P 场的负反射；第二场 Z 则始终作正反射。

## 5. 完整第四周期准确为四倍 canonical 单 P

令

$$F_{4,P}=-H(Z_P,Z_P)-2H(Y_P,W_P),$$

其中 $W_P$ 使用 (10) 的零段首值。第二 P 上 (11) 给

$$F_{4,P}^{(2)}=F_{4,P}+2H(Y_P,Y_a).\tag{12}$$

对应反向块的第四 forcing 为这些 forcing 的正 pullback；R45 的真实 rho、c、s 导数变换因此使 characteristic RHS 也为正反射。故四块求和为

$$\begin{aligned}
\Pi(F_4)
&=2\Pi_P(F_{4,P})+2\Pi_P(F_{4,P}^{(2)})\\
&=4\Pi_P(F_{4,P})+4\Pi_PH(Y_P,Y_a)\\
&=4\Pi_P(F_{4,P}),
\end{aligned}\tag{13}$$

最后一步来自 (1)，并使用 a 的真实紧支撑 collar 条件。因此

$$\boxed{\Pi(F_4)\equiv0
\quad\Longleftrightarrow\quad
\Pi_P(F_{4,P})\equiv0.}\tag{14}$$

这是**周期函数**的单 P 约简。逐 ruling 条件不能乘四或只检查一个整体积分：各段第三历史的 $Y_a$ 增量对 ruling 可能有真实作用。更不能用旧 Klein 八块的总 M 近零替代这里准确的单 P 零算子。

## 6. 对完整第四计算的直接用途

完整周期门可以只计算 canonical 单 P 的三条独立实/复第四谐波，并准确乘四。若某条整个周期函数非零，则任何合法第二、第三 profile gauge 都不能修复它；这个结论超出仅固定 canonical 二阶解的必要性范围。

若 canonical 周期门通过，还必须处理整个四块逐 ruling 条件。固定第二解时，R56 已给同一个全局 w 空间和六矩右逆的完整判据；改变第二解时，应把其额外作用保留为另一组真实未知量，而不是逐段独立选择 profile。

本稿没有计算或宣布任何实际第四周期为零。它给下一次单 P/profile 设计一个更小、且不遗漏第二 gauge 影响的周期目标，继续保留完整第四 ruling、所有更高阶、有限族、闭面嵌入及宏观 reach 未付。
