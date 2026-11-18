# R48：升模时完整参考补偿的代数恒等式

**状态：已证明；尚未宣称生产升模已经执行。** 本文承接 [R47](R47-fixed-slot-nested-circle-homotopy.md) 的固定控制槽，给出不同 Fourier 截断阶数之间应当使用的状态补偿。结论是连续表示的恒等式，不是新 BVP、误差收敛或浮点逐位等价结论。

## 1. 必须共同保留的对象

固定同一同伦值 $\lambda$、定义核 $\Gamma$、材料角图 $u$、背景 $G_{\rm bg}$、数值 gauge $q_g\ne0$、物理轮廓和完整控制。R47 的控制补零可以保持定义核；这里另外要求状态的角基确实嵌套。

令 $\mathcal B_M(u)$ 为旧状态系数到三维位置修正的线性合成算子，$\mathcal B_N(u)$ 为新算子，$N\ge M$。令 $E=E_{N\leftarrow M}$ 为按实际分量布局定义的线性嵌入，要求

$$
\mathcal B_N(u)E=\mathcal B_M(u). \tag{1}
$$

式 (1) 是函数恒等式，不能由两个数组长度之差推断。若状态包含不同的 Cartesian 块或特别的常数列，必须逐块编码旧系数；把整条旧数组末尾补零未必给出这个 $E$。这里固定材料角图，否则即便 Fourier 频率编号相同，也不能使用式 (1)。

记 $I_M,I_N$ 为两个截断中实际使用的入口系数，$b(u)$ 为共同背景入口。定义

$$
h(s)=a(s)\chi(s),\qquad
\Delta I=I_N-EI_M. \tag{2}
$$

这里的因子是 **$a\chi$，不是只有 $\chi$**。它与原 `exact_core_lift.py` 的 `h=aa*chi` 完全对应。入口系数可以是各自已有的有限投影值；下述恒等式对任意给定的 $I_M,I_N$ 都成立，不要求它们满足额外的精确积分恒等式。

把尚需独立处理的公共竖直均值写成 $m(s)e_3$。对应的完整位置表示为

$$
\begin{aligned}
F_M(s,u)={}&G_{\rm bg}(s,u)+m(s)e_3+q_g\mathcal B_M(u)Z_M(s)\\
&+\lambda h(s)\bigl(\Gamma(u)-b(u)-q_g\mathcal B_M(u)I_M\bigr).
\end{aligned} \tag{3}
$$

背景中若已经包含该均值，应把 $m$ 取零，避免重复加入。本文单独列出它，是为了不把平面 lift 的恒等式误认为已经完成了原 mean-height 积分。

## 2. 精确补偿定理

**定理。** 在式 (1)—(3) 的同一物理定义下，保持同一个 $m$，并定义

$$
Z_N(s)=EZ_M(s)+\lambda h(s)\Delta I. \tag{4}
$$

在式 (3) 中以 $N,I_N,Z_N$ 替代 $M,I_M,Z_M$，得到的 $F_N$ 满足

$$
F_N(s,u)=F_M(s,u). \tag{5}
$$

因此它们所有存在的共同偏导相同；特别地，在 $C^2$ 正则性下，位置、两个一阶导数、三个二阶导数及其第一基本形式相同。

**证明。** 由式 (1) 和式 (4)，状态项变化为

$$
q_g\bigl(\mathcal B_N Z_N-\mathcal B_M Z_M\bigr)
=\lambda h q_g\mathcal B_N\Delta I.
$$

参考 lift 的变化恰为

$$
-\lambda h q_g\bigl(\mathcal B_N I_N-\mathcal B_M I_M\bigr)
=-\lambda h q_g\mathcal B_N\Delta I.
$$

两项逐点抵消；其余项相同。这证明式 (5)。对同一函数恒等式求存在的偏导即得 jets 及度量恒等式。证毕。

实际初始化若还需要径向导数，应同时使用

$$
\begin{aligned}
Z_N'&=EZ_M'+\lambda(a'\chi+a\chi')\Delta I,\\
Z_N''&=EZ_M''+\lambda(a''\chi+2a'\chi'+a\chi'')\Delta I.
\end{aligned} \tag{6}
$$

这不是将位置补偿后再把旧径向导数原封不动复制的规则。角导数由同一角合成算子求导，不另作一个不相容的回投。

## 3. 为什么完整端点可以同时保持标准入口

假设 $h(0)=1$、旧标准入口为 $Z_M(0)=I_M$，并保留原共同归一化 $G_{\rm bg}(0,u)+m(0)e_3=b(u)$。式 (4) 给出

$$
Z_N(0)=EI_M+\lambda\Delta I
=I_N-(1-\lambda)\Delta I. \tag{7}
$$

因此在 **$\lambda=1$** 时，补偿后的状态也精确满足新标准入口 $Z_N(0)=I_N$，并且两者入口位置都等于同一 $\Gamma$。端点的“保整张表示”和“满足新标准入口”在这个代数层面相容。

在 $0\le\lambda<1$ 时，式 (4) 通常不满足新标准入口。若强制把新入口改成 $I_N$，入口位置随之改变

$$
(1-\lambda)q_g\mathcal B_N\Delta I
=(1-\lambda)q_g\bigl(\mathcal B_N I_N-\mathcal B_M I_M\bigr), \tag{8}
$$

正是 R47 已指出的有限入口差。它可以因特殊的 $\Delta I$ 而消失；不能只由控制核嵌套就认为一般消失。这里没有在中间同伦中新增“升模保持整个物理入口”的假设。

## 4. 原切口与有限插值的边界

若原 lift 窗在切口附近有 $\chi=\chi'=\chi''=0$，则 $h,h',h''$ 也为零。式 (4)、(6) 在切口给出旧状态及两阶径向导数的正确逐块嵌入。保持共同均值后，完整 Cartesian 切口两 jet 因而也保持。对于同一 Fourier 频率按分量作标准系数嵌入的情形，新增模数的系数为零。

这个结论没有支付一个新增模式数的实际尾：新的尾离散、额外端口方程、边界 Jacobian 和原停止门仍应按自己的实际输入计算。它也没有授权把旧的有限尾响应伪造成更高维响应。

式 (4) 定义的是一个连续初值函数。即使 $Z_M$ 已以分段 quintic 保存，$a\chi\Delta I$ 未必位于同一分段 quintic 空间。只在节点上取值再生成一个新插值，不能冒称式 (5) 在所有径向位置仍严格成立。可在初始化时直接求式 (4)、(6) 的值；求解器返回的有限表示及最终物理导出仍须实际审计。

完整 mean-height 同样有独立的边界：定理在共同给定 $m$ 时给出恒等式，不把旧 mean 文件直接变成新求解的审计。若要证明重新积分仍给相同 $m$，还必须证明所用 mean 速度函数、归一常数和实际积分输入保持；本条不把这一点藏在平面 lift 之内。

## 5. 对后续固定设计精化的用途和限制

R47 固定槽先保持同一 $\Gamma$；式 (1) 另行落实状态角基嵌入；式 (4) 则把两个有限参考 lift 的差精确抵消。在 $\lambda=1$，这提供同时保留已有位置表示和标准新入口的连续初值，不需要改变物理幅值、gauge、轮廓或控制来掩盖投影差。

它不证明新离散方程已经满足：新角模式会增加新的方程，Galerkin 投影、求解器和舍入仍有各自误差。它也不证明 BVP Jacobian 可逆、全角正性、严格等距、全时闭合或 reach。课题要求的固定完整 $g$、参数和时间范围下的空间/频率/时间加密下降，仍须由实际结果完成。

本条只作代数推导，没有重算旧积分、BVP、metric 或任何已登记的数值证书。定义依据为 [R45](R45-finite-trace-homotopy-and-synchronous-lift.md)、[R47](R47-fixed-slot-nested-circle-homotopy.md) 和原 [完整 lift 源](../scripts/resume_m3/round_raw_lib/exact_core_lift.py)。
