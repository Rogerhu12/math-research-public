# R78：完整第四 P1 的对称平方公式与四个全函数条件

日期：2026-11-14。**已证明。** 本文把 [R62](../results/R62-reciprocal-constant-states-and-fourth-local-drift.md) 的真实常态漂移和 [R71](../results/R71-third-holonomy-commutators-and-complete-fourth-P1.md) 的真实零矩桥公式合并。它不需要新的数值或完整符号目标计算。特别保留第三算子的外槽；只知道对角三次函数不够支付完整相位圆。

## 1. 同一 profile 空间、目标和实际桥

固定共同紧物理区间 $I$，全部真实路径上 $h>0$、$\xi+\omega\geq\delta>0$。profile 在共同右 collar 恒为零，所有右原函数使用同一锚；本稿允许尚未支付的左尾。先用实光滑 profile 空间 $\mathcal P$，随后作普通复双线性延拓，不使用 Hermitian 配对。

令 $E=\operatorname{Sym}^2\mathcal P$，约定

$$x\odot y=(x\otimes y+y\otimes x)/2,\qquad x^2=x\odot x.$$

任何对称双线性算子按线性延拓作用于 $E$。特别地，$H_{x\odot y}=H(Y_x,Y_y)$，其中 $H=\mathcal S/2$；对 $D=\sum_j a_jx_j\odot y_j$，$H_D=\sum_j a_jH(Y_{x_j},Y_{y_j})$。因此 $2x\odot y$ 对应 $2H(Y_x,Y_y)$，没有省略极化因子。

取同 $(h,d)$ 的 $k=+1,-1$ 常态，每段真实长度为 $N\ell$。正段单位长度 second 算子为 $r_+$，负段为 $-r_+$；记

$$\mathcal A=\ell r_+:E\longrightarrow\mathcal P.$$

两段之间是一座真实、固定的 $M=0$ 桥 $\mathcal B$；其 scalar 端口是上述两个常态，frame 端口也真实支付。它的第三算子是

$$\mathcal T(x;D)=\int_{\mathcal B}R\bigl(H(Y_x,Z_{\mathcal B}(D))\bigr)\,ds,$$

其中 $Z_{\mathcal B}(D)=\mathcal I_{\mathcal B}H_D$ 使用桥首的零 second scalar 历史和共同右 collar。$\mathcal T$ 对 $x$ 和 $D$ 线性，内槽对称；**不把外槽与内槽任意交换**。这正是 R71 的真实第三算子，不是只有 $\tau(q)=\mathcal T(q;q^2)$ 的对角替代品。

固定二阶目标 $F\in E$，第一 profile 为 $\phi$，令

$$D=F-\phi^2.$$

当 $F=f^2$ 时，目标度量是原来的 $g_X+\varepsilon^2dY_f^2$，$\phi=\cos\theta f+\sin\theta g$。本文的主要结论针对这个固定目标、固定 profile 平面和同一实际桥。改变目标、profile 或桥会改变相应条件。

## 2. 常态漂移的两个完整极化槽

在每个常态 $k$ 上，先按完整恢复式生成

$$Z_k(D)=\mathcal I_kH_D,\qquad U_k(x;D)=\mathcal I_kH(Y_x,Z_k(D)).$$

这里采用正号的 $\mathcal I$。物理第三 forcing 是 $-2H(Y_\phi,Z_k(D))$，所以物理第三场是 $-2U_k(\phi;D)$。记 $[\ \cdot\ ]_0$ 为：**先取包含全部真实历史 RHS 的 $s$ 导数，再把传入的 second、third scalar 历史值置为零**。该操作不把它们的 $s$ 导数置零，也不删除右 $\xi$ 原函数。

定义

$$\mathcal J_k^A(D_1,D_2)=\bigl[R_k\{-H(Z_k(D_1),Z_k(D_2))\}\bigr]_0, \tag{1}$$

$$\begin{aligned}
\mathcal J_k^B(x\odot y,D)=2\bigl[R_k\{&H(Y_x,U_k(y;D))\\
&+H(Y_y,U_k(x;D))\}\bigr]_0. \tag{2}
\end{aligned}$$

$\mathcal J_k^A$ 是 $E\times E$ 上的对称双线性型，$\mathcal J_k^B$ 对两个 $E$ 槽分别线性，第一槽由 $x,y$ 的对称式唯一确定。对 $(\phi^2,D)$，(2) 准确是 $4R_kH(Y_\phi,U_k(\phi;D))$，因此真实 fourth drift 为

$$\mathcal J_k(F,\phi)=\mathcal J_k^A(D,D)+\mathcal J_k^B(\phi^2,D). \tag{3}$$

式 (3) 也可直接从 R62 的 $r_D,d_D,\eta_*$ 核对：$r_D,d_D$ 对 $D$ 线性；$\eta_*$ 对 $(\phi,D)$ 双线性；$-r_{D,u}^2$ 及第二场平方给 (1)，与第一场和第三局部场的配对给 (2)。全部真实 $W_s$ 项仍在 (1)、(2) 中。不存在以“传入历史为零”为理由删掉 $Y_{W_s}$ 的操作。

## 3. 完整 P1 的两张双线性表

把 (1)、(2) 的两个常态和记为 $\sum_k$。定义

$$\boxed{\begin{aligned}
\mathcal K(D_1,D_2)={}&\ell\sum_{k=\pm1}\mathcal J_k^A(D_1,D_2)\\
&+\mathcal T(\mathcal A D_1;D_2)+\mathcal T(\mathcal A D_2;D_1),
\end{aligned}} \tag{4}$$

以及

$$\boxed{\begin{aligned}
\mathcal L(x\odot y,D)={}&\ell\sum_{k=\pm1}\mathcal J_k^B(x\odot y,D)\\
&-2\mathcal T(x;y\odot\mathcal A D)-2\mathcal T(y;x\odot\mathcal A D)\\
&+2\mathcal A\bigl(x,\mathcal T(y;D)\bigr)
+2\mathcal A\bigl(y,\mathcal T(x;D)\bigr).
\end{aligned}} \tag{5}$$

$\mathcal K$ 对称，$\mathcal L$ 一般不对称。两者的值都是**整个 $\xi$ 函数**，不是有限采样值。则一对 bulk 加其真实内部桥的完整 $N$ 一次系数为

$$\boxed{P_{1,\mathrm{pair}}(F,\phi)=\mathcal K(D,D)+\mathcal L(\phi^2,D).} \tag{6}$$

**证明。** R71 的准确公式对一般 $D$ 直接写成

$$\begin{aligned}
P_{1,\mathrm{pair}}={}&\ell\sum_k\mathcal J_k(F,\phi)
+2\mathcal T(\mathcal A D;D)\\
&-4\mathcal T(\phi;\phi\odot\mathcal A D)
+4\mathcal A\bigl(\phi,\mathcal T(\phi;D)\bigr).
\end{aligned}$$

第一行的后二、三历史桥项来自真实 $Z_2=Z_D-NY_{\mathcal A D}$；第二行还包含桥增加的 third scalar 在负 bulk 的作用。任意已有 $U_0$ 在正负两个 bulk 中相消，但桥新增加的 $-2\mathcal T(\phi;D)$ 不能删除。代 (3) 即得 (4)–(6)。这是 R71 的完整 pair 公式的极化，没有增加 collar 相容假设。$\square$

多个 pair 使用不同 $\mathcal A_j,\mathcal T_j$ 时，定义 $\mathcal K=\sum_j\mathcal K_j$、$\mathcal L=\sum_j\mathcal L_j$，(6) 仍给总 $P_1$。因此逐 pair 令零是充分选择，不是总周期为零的必要条件。R45 的四块倒行在 R70/R71 的同锚零矩条件下把此总值乘四；乘四不改变零条件。

定义对称型

$$\mathcal Q=\mathcal K-\operatorname{Sym}\mathcal L,\qquad
\operatorname{Sym}\mathcal L(D_1,D_2)=\frac{\mathcal L(D_1,D_2)+\mathcal L(D_2,D_1)}2.$$

由于 $\phi^2=F-D$，完整公式等价于

$$\boxed{P_1(F,\phi)=\mathcal L(F,D)+\mathcal Q(D,D).} \tag{7}$$

这一步保留了 $\mathcal L$ 的非对称部分。不能用对角 $\mathcal L(D,D)$ 反推出所有外槽资料。

## 4. 固定相位圆的四个必要充分条件

现在固定 $F=f^2$，$\phi_\theta=c f+s g$，其中 $c=\cos\theta,s=\sin\theta$。记

$$d=f^2-g^2,\qquad e=2f\odot g,\qquad D_\theta=s^2d-cs e.$$

令 $X=s^2$、$Y=cs$，则 $Y^2=X(1-X)$。把 (7) 展开得

$$\boxed{\begin{aligned}
P_1(\theta)={}&X\{\mathcal L(F,d)+\mathcal Q(e,e)\}\\
&+X^2\{\mathcal Q(d,d)-\mathcal Q(e,e)\}\\
&-Y\{\mathcal L(F,e)+2X\mathcal Q(d,e)\}.
\end{aligned}} \tag{8}$$

因此 $P_1(\theta)$ 对全部实 $\theta$ 恒为零，**当且仅当**下列四个函数在整个共同 $I$ 上恒为零：

$$\boxed{\begin{aligned}
\mathcal L(F,e)&=0,\\
\mathcal Q(d,e)&=0,\\
\mathcal L(F,d)+\mathcal Q(e,e)&=0,\\
\mathcal Q(d,d)-\mathcal Q(e,e)&=0.
\end{aligned}} \tag{9}$$

必要性不使用 profile 独立性。对同一个 $0<X<1$，$Y$ 有正负两个值；两相位的差使 (8) 最后一行恒零，故其两个系数分别零。两相位的和再给 $X A+X^2B=0$，从连续的 $X$ 得 $A=B=0$。充分性直接代入。整个论证对函数值向量空间成立，故不是点采样条件。

## 5. 两个复谐波与遗漏的条件

令 $q=f+ig$，则

$$q^2=d+ie,\qquad \bar q^2=d-ie.$$

式 (9) 可写成两个复函数恒等式

$$\boxed{\mathcal Q(q^2,q^2)=0,\qquad
\mathcal L(F,q^2)+\mathcal Q(d,q^2)=0.} \tag{10}$$

第一式等价于 (9) 的第二、四行。第二式在第一式成立后，恰等价于其余两行；没有额外全对称假设。

更直接地，置 $\zeta=e^{-i\theta}$，则

$$\phi_\theta=(\zeta q+\zeta^{-1}\bar q)/2,$$

$$D_\theta=\{(1-\zeta^2)q^2+(1-\zeta^{-2})\bar q^2\}/4.$$

因此完整 Laurent 模式准确是

$$\boxed{P_{1,-4}=\frac1{16}\mathcal Q(q^2,q^2),\qquad
P_{1,-2}=-\frac14\{\mathcal L(F,q^2)+\mathcal Q(d,q^2)\}.} \tag{11}$$

其余非零模式为共轭；常数模式由 $P_1(0)=0$ 决定。所以 (11) 的两个复零条件正是全部相位条件。原 pure producer 的目标 $-H(B,B)/16-H(Y_q,U)/4$ 对应第一式，因 $\mathcal J^B(q^2,q^2)=4R H(Y_q,U)$；式 (11) 与 R71 的 $1/8$ Lie bracket 响应完全相符。

即使对**所有**复 $q$ 已证明第一式，也不能把 $\mathcal Q$ 当作 $E\times E$ 上的零型。一个纯代数例子是二维 profile 子空间：在 $D=a f^2+b f\odot g+c g^2$ 上令 $\mathcal Q(D,D)=ac-b^2/4$。每个 $D=(uf+vg)^2$ 都使其为零，但这个对称双线性型本身非零。这说明 universal pure 恒等式也不足以免除第二组槽条件。

## 6. 可实际控制的第三算子与编译范围

对一条实际同端口 $M=0$ 控制环，其完整第三改变量记为 $\Delta\mathcal T$。式 (4)、(5) 给准确线性响应

$$\Delta\mathcal K(D_1,D_2)=\Delta\mathcal T(\mathcal A D_1;D_2)+\Delta\mathcal T(\mathcal A D_2;D_1),$$

$$\begin{aligned}
\Delta\mathcal L(x\odot y,D)={}&-2\Delta\mathcal T(x;y\odot\mathcal A D)-2\Delta\mathcal T(y;x\odot\mathcal A D)\\
&+2\mathcal A(x,\Delta\mathcal T(y;D))+2\mathcal A(y,\Delta\mathcal T(x;D)).
\end{aligned}$$

R71 的真实交换子环以及 R77 的完整三次速度局部算子都可作为这种 $\Delta\mathcal T$。它们必须同时代入 (9) 的四个函数，不可为 $-4$、$-2$ 模式分别选择不相容的桥参数。

后续准确编译应有独立的外 profile 和对称内 profile 两槽：生成 $\mathcal T(x;y,z)$ 后，再作需要的替换和共轭。对角函数 $\tau(q)$ 的普通三次极化只能恢复第三算子的全对称部分；它不能确定本稿所需的全部 $\mathcal T(x;y,z)$。相同地，已完成的 diagonal $\mathcal C_1$ 商空间检验不得直接升级为完整第三或完整 P1 的商空间检验。

用固定有限可达算子表时，四个函数的联合匹配仍是准确线性关系问题。任何正关系都应回到原始有锚表达式验证；没有找到关系只说明该次算法未产出证明，不是函数非成员定理。

## 7. 已付与仍未付

本文已付完整相位 P1 的极化、真实桥线性响应、四个必要充分全函数条件，以及 pure 条件为什么不充分。没有构造满足 (9) 的具体真实桥或共同 profile，也没有把已有 pure formal 正关系自动升级为全相位解。

即使随后 (9) 全部支付，$P_0$、第四 ruling、低阶双 collar、更多高阶及收敛仍需支付。R71/R77 的实际控制环会改变 $P_0$，且一般无嵌入、reach 或宏观幅度保证。本文不改变主课题完成标准。
