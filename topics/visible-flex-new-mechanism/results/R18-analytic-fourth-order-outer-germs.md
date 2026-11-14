# R18：四阶有限外尾的实际解析存在与唯一相位

日期：2026-11-14。状态：以下是抽象周期方程 $Q=0$ 在简单端点处的完整局部存在定理。它加强四阶外尾的必要主平衡，但尚未连接两个端点，也没有实现闭曲面的几何系数。

## 1. 方程与结论

采用 [R8](../results/R8-flat-profile-period-equation.md) 的方程，记 $A=A_1$、$E=A_2$：

$$\begin{aligned}
Q[q]={}&(Aq+2Eq'-2Cq'')q^{(4)}-2C(q''')^2\\
&+\{2A'q+(2D+2A+4E')q'-4Wq''\}q'''
+3D(q'')^2.
\end{aligned}$$

这里系数在所论端点附近实解析，$D$ 为常数，且 $E=C'-W$。实际九系数的多项式当然满足这一正则性。设端点为 $e$，

$$C(e)=0,\qquad C'(e)\ne0,\qquad W(e)=-\frac87C'(e).\tag{1}$$

取朝活动区内部增加的坐标 $t\ge0$：左端 $t=x-e$，右端 $t=e-x$。

**定理。** 对每个复数 $a\ne0$，存在 $\delta>0$ 和唯一解析函数芽 $v_a$，满足

$$q_a(t)=t^4v_a(t),\qquad v_a(0)=a,\qquad Q[q_a]=0
\quad(0\le t<\delta).\tag{2}$$

并且 $v_a=a v_1$，其中 $v_1$ 为实解析且 $v_1(0)=1$。因此这一解析外尾类只有公共振幅与复相位自由度，不能从端点自行产生第二个相对相位分量。

这里的唯一性限定于 $q/t^4$ 在端点解析的函数芽。没有将它扩大为所有 $C^4$ 外尾，也没有排除内部的非解析全平相位开启。

## 2. 普适 Euler 主算子

令 $\theta=t\partial_t$，并定义

$$P_j(\theta)=\prod_{i=0}^{j-1}(\theta+4-i),\qquad
\partial_t^j(t^4v)=t^{4-j}P_j(\theta)v.$$

写 $C=t c(t)$，$c_0=c(0)=dC/dt(0)\ne0$。由 (1)，左端有 $E(e)=15c_0/7$、$W(e)=-8c_0/7$。将各项代入，$Q/t^3$ 是 $t,v,\theta v,\theta^2v,\theta^3v,\theta^4v$ 的解析函数。它在 $t=0$ 的部分为

$$\frac{c_0}{7}\{30(P_1v)(P_4v)-14(P_2v)(P_4v)
-14(P_3v)^2+32(P_2v)(P_3v)\}.\tag{3}$$

右端的 $\partial_x=-\partial_t$ 与 $dC/dt=-C'(e)$ 同时改变符号，仍得到完全相同的 (3)，其中 $c_0$ 始终按内向坐标定义。这避免将左右两端的 $C'$ 符号混用。

当 $v=a$ 为常数时，$P_1v=4a$、$P_2v=12a$、$P_3v=P_4v=24a$，(3) 恰为零。对 $v$ 作一阶变分，其线性化为

$$-\frac{48ac_0}{7}\,
\theta(\theta+4)^2(\theta+8)\,\dot v.\tag{4}$$

特别地，$\theta^4v$ 的系数为 $-48ac_0/7\ne0$，故解析隐函数定理可将原方程唯一解为

$$\theta^4v=F(t,v,\theta v,\theta^2v,\theta^3v)\tag{5}$$

在 $(t,v,\theta v,\theta^2v,\theta^3v)=(0,a,0,0,0)$ 附近的解析方程。这里只用了一个有限维非零系数，不是预设外尾已存在。

## 3. 解析收缩证明

置 $U=(v-a,\theta v,\theta^2v,\theta^3v)^\mathsf T$。由 (4)–(5)，一阶系统为

$$\theta U=JU+f(t,U),\qquad
J=\begin{pmatrix}
0&1&0&0\\0&0&1&0\\0&0&0&1\\0&-128&-80&-16
\end{pmatrix},\tag{6}$$

其中 $f$ 解析，$f(0,0)=0$、$D_Uf(0,0)=0$。于是，在一个固定小邻域有

$$|f(t,U)|\le K(|t|+|U|^2),\qquad
\|D_Uf(t,U)\|\le K(|t|+|U|).\tag{7}$$

$J$ 的特征多项式为 $\lambda(\lambda+4)^2(\lambda+8)$。对实 $0<s\le1$ 定义 $s^{-J}=\exp(-J\log s)$。其各 Jordan 分量至多为常数、$s^4(\log s)^j$ 或 $s^8(\log s)^j$；零特征值是单根。因此

$$K_J:=\int_0^1\|s^{-J}\|\,ds<\infty.\tag{8}$$

在复圆盘 $|t|\le\delta$ 上，取在内部全纯、闭盘连续并在零点为零的向量函数空间，赋范数

$$\|U\|_* =\sup_{0<|t|\le\delta}\frac{|U(t)|}{|t|}.$$

考虑映射

$$\mathcal T[U](t)=\int_0^1s^{-J-1}f(st,U(st))\,ds.\tag{9}$$

若 $\|U\|_*\le R$，(7)–(8) 给

$$\|\mathcal T[U]\|_*\le KK_J(1+R^2\delta).$$

先取 $R>2KK_J$，再将 $\delta$ 缩小到 $R\delta$ 留在解析邻域且右侧小于 $R$。对同一球中的 $U,V$，再次用 (7)，有

$$\|\mathcal T[U]-\mathcal T[V]\|_*
\le KK_J\delta(1+2R)\|U-V\|_*.$$

继续缩小 $\delta$ 即使该常数小于一。积分在零点由 (7)–(8) 一致收敛，保持全纯性。因此 Banach 收缩给唯一不动点 $U=O(t)$。

对 (9) 求导，或直接积分

$$\frac{d}{ds}\{s^{-J}U(st)\}=s^{-J-1}f(st,U(st)),$$

可知不动点满足 (6)。下端边界项确为零，因为 $U(st)=O(s)$，而 $s^{-J}$ 有界。系统前三式又保证 $U_1=\theta U_0$、$U_2=\theta^2U_0$、$U_3=\theta^3U_0$，故恢复的 $v=a+U_0$ 真正满足 (5) 及原方程。

解析函数芽的唯一性也可逐系数确认：写 $U=\sum_{n\ge1}U_nt^n$ 后，每阶要解

$$ (nI-J)U_n=[f(t,U)]_n.$$

右侧只含较低阶 $U_j$，因为 $D_Uf(0,0)=0$；而 $nI-J$ 对每个正整数 $n$ 可逆。所有解析解的 Taylor 系数相同，故函数芽相同。这个论证不要求任意另一个解析解事先落在选定的收缩球中。

## 4. 相位、边界正则性及匹配意义

当 $a=1$，实系数和解析唯一性使 $v_1$ 在实轴为实值。方程 $Q$ 对 $q$ 二次齐次，故 $a t^4v_1$ 是首项为 $a t^4$ 的解；唯一性给 $v_a=a v_1$。这证明固定复相位结论。

每个局部外尾在端点的前三阶导数都为零，零延拓为 $C^3$ profile。按 [R16](R16-C2-endpoint-profile-equation.md) 中对 $Y=U\phi+V\phi'$ 的逐项二阶链式法则，它给 $C^2$ 的零延拓无穷小弯曲场。

若要构造全局复 profile，可从左右各取这里的实解析单位外尾，分别赋公共复幅值，再在内部匹配。一个真非零全局解在 [R15](../results/R15-global-endpoint-moments.md) 的满秩条件下必须具有独立实部和虚部；因此内部相对相位变化仍需实际发生。外尾解析且内部相位非解析并不矛盾，[R13](../results/R13-local-smooth-complex-phase-opening.md) 已给抽象系数下的局部全平开启实例。

当前全局 BVP 的窗口试空间是在近似这种匹配，不是宣称有限次数已经给精确全局解。局部存在没有支付全局三矩、真实闭几何积分实现、第三阶以后等距条件或本课题的宏观厚度与位移要求。

## 5. 精确代数证据

`scripts/literature_outer_germ_certificate.py` 只用 `fractions.Fraction`，核对 (3) 在常数解的值、(4) 的完整多项式、最高 Euler 导数系数及前 16 个正整数递推分母。它不运行几何研究、优化或数值 ODE。输出在 `notes/literature-outer-germ-certificate-20261114.json`。解析收敛由 §3 证明，不由有限系数检查替代。
