# R11. 相位族的全时间法向弦检验：消去时间变量

2026-11-10，visible-larger-astra-20261110。**状态：已证明，条件工具。**

本文把绕固定轴旋转的曲面片与固定端帽之间的全时间点对检验，准确化为不含时间的标量不等式。它不从有限空间样本推出连续曲面的 reach，也不构造尚缺的无限尾或端帽。归一化中的 $D$ 仍是原题定义的 $\operatorname{diam}F_0(M)$。

## 1. 闭曲面的法向弦充分条件

设 $S\subset\mathbb R^3$ 是紧的、无边界的 $C^2$ 嵌入曲面，$\tau>0$。在每个点任取一个单位法向 $n_p$。假定对所有不同的 $p,q\in S$，

$$
 |q-p|^2\ge 2\tau\,|(q-p)\cdot n_p|. \tag{1}
$$

则 $\operatorname{reach}(S)\ge\tau$。

**证明。** 设 $x$ 到 $S$ 的距离为 $d<\tau$。紧性保证存在最近点。若存在两个不同的最近点 $p,q$，无边界曲面的最近点一阶条件给 $x-p=\lambda n_p$，其中 $|\lambda|=d$。由 $|x-q|^2=|x-p|^2$，

$$
 |q-p|^2=2(x-p)\cdot(q-p)
 \le 2d\,|n_p\cdot(q-p)|
 \le \frac d\tau |q-p|^2.
$$

因 $d<\tau$ 且 $p\ne q$，矛盾。所以距离小于 $\tau$ 的每个点都有唯一最近点，这正是所需 reach 下界。证毕。

检验无序点对时，可以同时使用两端法向，把 (1) 写成

$$
 |q-p|^2\ge 2\tau\max\{|(q-p)\cdot n_p|,
                                  |(q-p)\cdot n_q|\}. \tag{2}
$$

法向的正负选择不影响不等式。对角线 $p=q$ 上等式为 $0=0$；连续域证书还必须控制趋近对角线的点对，不能以有限样本避开局部曲率要求。

## 2. 一个移动点与一个固定点的精确全相位公式

令 $R_\varphi$ 为绕 $z$ 轴旋转角度 $\varphi$ 的刚体运动。移动点及其法向为 $(R_\varphi p,R_\varphi n)$，固定点及其法向为 $(q,m)$。写

$$
 p=(x,z),\quad q=(y,w),\quad n=(a,c),\quad m=(b,e),
 \qquad x,y,a,b\in\mathbb R^2.
$$

令 $J(u_1,u_2)=(-u_2,u_1)$，$\Delta=w-z$，并定义

$$
 A=|x|^2+|y|^2+\Delta^2,
 \qquad B=y\cdot x,\qquad C=y\cdot Jx. \tag{3}
$$

两端法向分别给出三个系数：

$$
\begin{array}{c|ccc}
 &d_0&d_c&d_s\\\hline
\text{移动端 }n&\Delta c-x\cdot a&y\cdot a&y\cdot Ja\\
\text{固定端 }m&y\cdot b+\Delta e&-x\cdot b&-(Jx)\cdot b
\end{array} \tag{4}
$$

对表中的每一行 $v\in\{n,m\}$ 和每个 $\epsilon\in\{-1,1\}$，定义

$$
 \mathcal M_{v,\epsilon}(p,q;\tau)
 =A-2\tau\epsilon d_{0,v}
 -2\sqrt{(B+\tau\epsilon d_{c,v})^2
              +(C+\tau\epsilon d_{s,v})^2}. \tag{5}
$$

**定理 2.** 下列两件事等价：

1. 对所有 $\varphi\in[0,2\pi]$，移动—固定点对满足 (2)。
2. (5) 的四个数全部非负。

更准确地，四个数的最小值等于

$$
 \min_\varphi\left\{|q-R_\varphi p|^2
 -2\tau\max\bigl(|(q-R_\varphi p)\cdot R_\varphi n|,
                  |(q-R_\varphi p)\cdot m|\bigr)\right\}. \tag{6}
$$

**证明。** 直接展开，得到

$$
 |q-R_\varphi p|^2=A-2B\cos\varphi-2C\sin\varphi. \tag{7}
$$

对移动端法向，利用 $R_\varphi x\cdot R_\varphi a=x\cdot a$，有

$$
 (q-R_\varphi p)\cdot R_\varphi n
 =y\cdot R_\varphi a-x\cdot a+\Delta c.
$$

对固定端，

$$
 (q-R_\varphi p)\cdot m
 =y\cdot b-(R_\varphi x)\cdot b+\Delta e.
$$

二式正好是表 (4) 中的 $d_0+d_c\cos\varphi+d_s\sin\varphi$。绝对值不等式等价于同时取 $\epsilon=\pm1$。由

$$
 \min_\varphi\{u-2v\cos\varphi-2w\sin\varphi\}
 =u-2\sqrt{v^2+w^2},
$$

每一端、每一符号的最小值恰为 (5)。有限次最小值与对紧圆周的最小值可交换，故得到 (6) 及等价性。证毕。

公式不需要 $p$ 或 $q$ 离开旋转轴。若实际时间只覆盖部分相位，四个非负条件仍然充分，但不一定必要。对完整相位圆周则没有时间离散误差。

## 3. 全曲面分块约化

设 $S_\varphi$ 是已经装配并证明为 $C^2$ 嵌入的闭曲面，其像可写成

$$
 S_\varphi=R_\varphi A_0\cup B, \tag{8}
$$

其中 $B$ 固定，接缝的法向来自共同的 $C^2$ 曲面。块允许在接缝重叠；(8) 不意味着可把任意有边片直接拼起来。

若对某个 $\tau>0$：

- $A_0$ 内所有点对满足 (2)；
- $B$ 内所有点对满足 (2)；
- 所有 $p\in A_0,q\in B$ 满足 (5) 的四个不等式；

则每个 $\varphi$ 都有 $\operatorname{reach}(S_\varphi)\ge\tau$。

**证明。** $R_\varphi$ 是刚体运动，故 $A_0$ 内的弦长和弦—法向内积不变。固定块的点对也不变。混合点对由定理 2 支付全部相位。因此每个闭曲面上的全部点对满足 (2)，第 1 节给出结论。证毕。

此约化只消去了**时间变量**。若 $A_0,B$ 仅由离散点云表示，所得仍是点云诊断；空间连续性、局部曲率、缝附近点对及离散化误差仍需真实控制。

## 4. 旋转端帽与固定标记的更便宜充分条件

可进一步写 $B=C\cup P$，其中 $P$ 包括所有破坏旋转对称的固定标记。允许 $C$ 是一个旋转对称参考曲面 $\overline C$ 的子集；其法向须与 $\overline C$ 的法向一致到符号。这样即使给标记挖去局部支撑，$C$ 本身不再旋转不变，也不影响以下论证。

若 $\overline C$ 连同其无定向单位法向场在旋转下不变，那么对 $A_0\times\overline C$ 的单一静态点对检验，就充分控制全部 $R_\varphi A_0\times C$：同时施加 $R_{-\varphi}$ 后，第二点和其法向仍属于参考曲面。

剩下的 $A$—$P$ 点对可以使用精确公式 (5)，也可使用径高平面的屏障。定义

$$
 \Pi(p)=(\sqrt{p_x^2+p_y^2},p_z).
$$

有准确恒等式

$$
 \inf_{\varphi,p\in A_0,q\in P}|R_\varphi p-q|
 =\operatorname{dist}(\Pi(A_0),\Pi(P)). \tag{9}
$$

**证明。** 固定 $p,q$，旋转可以把两水平投影的方向对齐，最小距离平方是 $(|x|-|y|)^2+(z-w)^2$；若某个水平投影为零，公式照旧成立。再对两点取下确界即得 (9)。证毕。

若右侧至少为 $2\tau$，则所有相位的混合弦长 $d\ge2\tau$。由于 $|n\cdot\text{弦}|\le d$，有 $d^2\ge2\tau d\ge2\tau|n\cdot\text{弦}|$，故两端法向不等式自动成立。这也是无自交的严格空间分离屏障，但固定块自身、接缝与移动块内部的检查仍不能省略。

若只掌握两块的半径区间 $I_A,I_P$ 和高度区间 $Z_A,Z_P$，一个更保守的可计算下界为

$$
 \operatorname{dist}(\Pi(A_0),\Pi(P))
 \ge\sqrt{\operatorname{dist}(I_A,I_P)^2+
           \operatorname{dist}(Z_A,Z_P)^2}. \tag{10}
$$

## 5. 计算接口及适用边界

`computations/root_phase_reach.py` 实现 (3)–(6)、点对的全相位距离范围及批量点云筛查；它显式返回最坏的端点、符号和相位，便于回到原始三维点与法向复算。脚本不会把样本输出标记为连续 reach 证书。

本题的最终目标需要取 $\tau\ge.03D$，同时另行支付闭合、同度量真加密、固定握持区及实际 Hausdorff 位移。本文不把开放前缀的相位旋转当成已经完成的闭等距族，也不把固定 taper 的误差消掉。
