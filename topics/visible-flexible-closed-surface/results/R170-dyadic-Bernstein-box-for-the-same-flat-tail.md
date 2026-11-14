# R170 — 八段 Bernstein 子盒严格扩大同一平尾的充分控制域

本结果只扩大 R132 尾部的**充分参数域**。多项式、准确曲面积分、材料度量、参数维数以及所有角向导数和参数列均不改。它没有证明当前前缀满足 Gauss–Codazzi、拼缝、held 或全闭曲面 reach，也没有证明存在达到强幅度标准的解。

## 1. 同一尾函数与新的参数域

沿用 [R132](R132-positive-bernstein-controls-for-the-exact-flat-tail.md) 的准确定义，固定次数 $n=15$：

$$
 P_b(q)=\sum_{i=0}^{15}b_i B_i^{15}(q),\qquad
 f_b(q)=630\int_0^q t^4(1-t)^4P_b(t)\,dt.
$$

在 $q\le0$ 取 $f_b=0$，在 $q\ge1$ 取准确端值常数。标准几何参数为 $a=4/5,c=17/50,w=a-c=23/50$，并取

$$
 \alpha_b(y)=\operatorname{sgn}(y)f_b((|y|-c)/w),\quad
 X_b(y)=\int_0^y\cos\alpha_b(v)\,dv,\quad
 Z_b(y)=\int_0^y\sin\alpha_b(v)\,dv.
$$

尾曲面仍是

$$
 F_b(r,u)=(r\cos u,\ X_b(r\sin u),\ Z_c-Z_b(r\sin u)).
$$

对 $j=0,\ldots,7$，将同一个 $P_b$ 在 $I_j=[j/8,(j+1)/8]$ 上写为

$$
 P_b\left(\frac{j+t}{8}\right)=\sum_{k=0}^{15}c_{jk}B_k^{15}(t),
 \qquad c=Sb.
 \tag{1}
$$

定义

$$
 \mathcal B_0=[0,6/5]^{16},\qquad
 \mathcal B_8=\{b\in\mathbb R^{16}:0\le(Sb)_{jk}\le6/5\text{ for every }j,k\}.
 \tag{2}
$$

这里是 $128$ 条双边线性约束，即 $256$ 条单边线性不等式；不是增加 $128$ 个独立尾参数。仍只有原来的 $16$ 个 $b_i$。

**命题。** $\mathcal B_0\subsetneq\mathcal B_8$，且每个 $b\in\mathcal B_8$ 都满足 $0\le P_b(q)\le6/5$，$0\le q\le1$。因此 R132 的全部统一尾部几何预算以及 R130、R168 对这些预算的应用保持有效。

## 2. 准确限制矩阵与旧盒包含

令 $A=j/8,B=(j+1)/8$。次数 $15$ Bernstein 表示的极化函数，在 $15-k$ 个 $A$ 与 $k$ 个 $B$ 上取值，给出 $c_{jk}$。按选择其中 $r$ 个 $A$ 因子与 $s$ 个 $B$ 因子计数，得到

$$
 S_{(j,k),i}=
 \sum_{\substack{r+s=i\\0\le r\le15-k\\0\le s\le k}}
 \binom{15-k}{r}\binom{k}{s}
 A^r(1-A)^{15-k-r}B^s(1-B)^{k-s}.
 \tag{3}
$$

这也可由反复 de Casteljau 插值推出。为直接核对极化恒等式：在一个由 $15$ 个数 $t_1,\ldots,t_{15}$ 组成的表中，按子集 $J$ 求和

$$
 \sum_{J\subseteq\{1,\ldots,15\}} b_{|J|}
 \prod_{h\in J}t_h\prod_{h\notin J}(1-t_h)
$$

是分别仿射、对称的函数；令全部 $t_h=q$ 就恰得 $\sum_i b_i\binom{15}{i}q^i(1-q)^{15-i}$。在 $A/B$ 表上分组即得 (3)，从而得到 (1)，没有额外的 $\binom{15}{i}$ 分母。

(3) 每项非负，且对 $i$ 求和等于

$$
 (A+(1-A))^{15-k}(B+(1-B))^k=1.
$$

所以每行都是随机权向量。若 $b\in\mathcal B_0$，则 $c_{jk}\in[0,6/5]$，证明 $\mathcal B_0\subseteq\mathcal B_8$。若 $b\in\mathcal B_8$，则 (1) 与局部 Bernstein 基的非负性及和为一，逐段给出函数界。八个闭区间覆盖 $[0,1]$，包括全部接口。

此外，首个区间的限制映射已是单射：一个多项式若在该区间恒零，则恒等为零。因此 $S$ 的列秩是 $16$；新域没有隐含新增或删除任何参数。

## 3. 严格扩大：完整有理例子

取

$$
 P_*(q)=(q-1/2)^2+1/128.
$$

次数提升到 $15$ 后，其准确全局控制为

$$
 b_i^*=\frac{i(i-1)}{15\cdot14}-\frac{i}{15}+\frac{33}{128}.
 \tag{4}
$$

特别地，$b_7^*=b_8^*=-17/1920<0$，故 $b^*\notin\mathcal B_0$。

任取本划分中的区间 $[A,B]$。它不会跨过 $1/2$，因为 $1/2$ 本身是接口。记 $x=A-1/2,y=B-1/2$，则 $xy\ge0$，$|x|,|y|\le1/2$。该区间内的二次 Bernstein 控制为

$$
 x^2+1/128,\qquad xy+1/128,\qquad y^2+1/128.
$$

三者都在 $[1/128,33/128]$。从次数 $2$ 提升到次数 $15$ 是连续的凸组合操作，故所有 $c_{jk}^*$ 仍在此闭区间。因 $33/128<6/5$，例子属于 $\mathcal B_8$，证明严格包含。实现中的 binary64 例子是 (4) 各分量的明确舍入值，另用准确有理 $S$ 检查；不把它冒称 (4) 的逐字准确有理系数。

子盒仍只是函数界的充分条件，本结果不称其与全部非负多项式等价。

## 4. 原几何结论只需要函数界

在 $\mathcal B_8$ 上直接积分被积函数界，得

$$
 0\le f_b(q)\le\frac65 S_9(q),\qquad
 S_9'(q)=630q^4(1-q)^4,\qquad S_9(0)=0,\quad S_9(1)=1.
 \tag{5}
$$

因此 $0\le f_b\le6/5$，$\alpha_b$ 为奇函数且单调不减。总转角至多 $12/5<\pi$；$\cos\alpha_b\ge\cos(6/5)>0$。准确曲率为

$$
 \kappa_b(y)=\frac{630}{w}q^4(1-q)^4P_b(q)\ge0,
 \qquad \kappa_b\le\frac{315}{128w}\frac65=\frac{4725}{736}.
 \tag{6}
$$

这里 $q^4(1-q)^4\le1/256$。端点四阶零因子不变，故原准确 collar、$C^4$ 角函数及所需曲面的 $C^2$ 拼接正则性不变。没有对 $P_b'$ 或 $P_b''$ 加新符号条件。

由 $X_b'^2+Z_b'^2=1$，直接求导仍得 $F_b^*\langle\cdot,\cdot\rangle=dr^2+r^2du^2$。单调 $X_b$ 给出原嵌入证明。按原上半内向子午约定，完整二基本形式仍是

$$
 l=\kappa_b\sin^2u,\qquad
 m=-\kappa_b\sin u\cos u,\qquad
 n=\kappa_b\cos^2u.
 \tag{7}
$$

由于 $0\le\sin f_b\le f_b$ 及 $\int_0^1S_9(q)dq=1/2$，

$$
 0\le Z_b(y)\le\frac65\frac w2=\frac{69}{250}\quad (|y|\le a).
 \tag{8}
$$

前述单调转角、总转角小于 $\pi$ 与 (6)，逐项满足 [R130](R130-global-normal-balls-for-the-exact-flat-tail.md) 的完整曲线/完整广义柱法球定理。因此完整柱的 reach 至少 $736/4725$，并能使用其对子片点对的全域法球结论；没有把带边 annulus 本身的集合 reach 与完整柱混同。

原 R132 的 $|y|\le4/5$、半径平方 $\le(4/5)^2+Z_c^2$、真实 held 下界

$$
 \operatorname{dist}(p,F_b)^2\ge(A_q-4/5)^2+(Z_c-69/250)^2
 \tag{9}
$$

在原来要求的 $A_q\ge4/5$、$Z_c\ge69/250$ 条件下继续成立。故 [R168](R168-smaller-corner-caps-and-shorter-cylinder-window.md) 的两个充分帽窗可原样用于新尾域：标准 $D\le4$ 窗的真实尾平面高度仍需 $Z_c\in[0.916,1.16]$，$D\le3.75$ 窗仍需 $Z_c\in[0.853,1.05]$，并保留各自全部中央 $A_q$、活动位置、闭核 reach、held 球及拼接前提。新控制域不能代付任何未知的真实 $Z_c$ 或前缀几何。

R128 中特定单参数幅度族的 $h_2$ 单调性并非一般 $b$ 的结论，本命题不将其移用。R128 的准确度量、固定 collar、完整两 jet 与上述统一几何预算则只使用现已验证的条件。尾的纯相位族单独仍可能全等；整体含反射非全等量仍由完整固定帽/活动核论证承担。

## 5. 所有角 jet 与参数列保持同一数学公式

新的 tail 类不重建多项式，不拟合 $P$，也不把 $c=Sb$ 作为独立参数。对每个原始参数，仍有

$$
 \frac{\partial f_b(q)}{\partial b_i}
 =630\int_0^q t^4(1-t)^4B_i^{15}(t)dt.
$$

其任意内部角向导数、端点平接及位置积分的参数微分与旧族完全一致。对任意同一 $b$，旧公式与新公式的完整曲面函数、角 jet、参数 JVP 都相同；只有是否接受该 $b$ 的充分域改变。由于参数不变，原 tail/profile 链式项及当前半径 $a_\delta(s)\sin U(s,\xi)$ 依赖全部保留。

末切口原 R155 正 trace 的准确旁路只需要零 raw correction、$K=0$ 和实际尾的半正定二基本形式。(7) 与 $\kappa_b\ge0$ 正好给出该前提，包括 $n=0$ 或全零尾弧。因此可使用同一真实尾值和角向两 jet，不增设 $n>0$ 条件。没有因旁路而给 $h=0$ 指派一个未经证明的径向导数，也没有把平方根在所有域外方向称为可微。

## 6. 矩阵与有限计算的准确性边界

将 (3) 乘以 $8^{15}=2^{45}$，得到整数

$$
 N_{(j,k),i}=\sum_{r+s=i}\binom{15-k}{r}\binom{k}{s}
 j^r(8-j)^{15-k-r}(j+1)^s(7-j)^{k-s}.
 \tag{10}
$$

它非负，且每行整数和恰为 $2^{45}$，所以每个条目至多 $2^{45}$。这些整数及它们除以 $2^{45}$ 的结果都能由 binary64 准确表示。**这不使一般浮点 $S b$ 的加法/乘法自动准确。**

对已保存 binary64 控制，程序把每一分量解释为它准确表示的二进有理数，以公共整数分母计算 $N b/2^{45}$，并准确比较 $0$ 和 $6/5$。选域证书从未以样本值、舍入容差、浮点矩阵乘积或修改过的控制替代。QP 可用准确浮点矩阵及明确舍入的右端；真正数学域判定另由上述有理运算返回。

对增量 $d$，约束完整写作

$$
 -Sb\le Sd\le\frac65\mathbf1-Sb.
 \tag{11}
$$

它替换旧 tail 的逐分量盒，不能在添加 (11) 后仍保留 $b_i\ge0$，否则没有扩大域。原中央域、正度量域及其余约束不因此改变。

## 7. 明确的近可行参数收缩

需要修复因舍入或试步得到的域外控制时，可令 $a_*=(3/5)\mathbf1$ 并考虑准确线段

$$
 b(\theta)=(1-\theta)b+\theta a_*,\qquad 0\le\theta\le1.
$$

因为 $S\mathbf1=\mathbf1$，每行从 $c_h=(Sb)_h$ 线性移向 $3/5$。准确最小可行量为

$$
 \theta_* =\max\left(0,\max_{c_h<0}\frac{-c_h}{3/5-c_h},
       \max_{c_h>6/5}\frac{c_h-6/5}{c_h-3/5}\right).
 \tag{12}
$$

于是每个 $\theta\in[\theta_*,1]$ 都在准确子盒内。实现先取 $\theta_*$，将新系数舍入为 binary64 并准确重检。如果重检仍失败，明确记录后改取 $\theta=\theta_*+(1-\theta_*)\varepsilon$，依次令 $\varepsilon=2^{-52},2^{-51},\ldots,1$。最后一步是舍入后的常数 $3/5$，严格位于域内，所以这个有界过程终止。

保存的 binary64 向量一般不是准确线段上的同一个实数向量。报告同时保留准确 $\theta$、准确目标与保存系数的差、原系数与新系数的真实差、重新获得的域证书。该操作是**明确的新参数/新场**，不冒称原态通过，也不为其借用原有限残差或 normal 矩阵。

## 8. 实现与最薄集成边界

`scripts/fd2d_dyadic_bernstein_tail.py` 提供：

- `DyadicBernsteinControlBox`：准确矩阵定义、128 行有理域证书、绝对/增量线性约束和上述显式收缩；
- `DyadicBernsteinFlatDevelopableFamily`：真实独立新类，复用旧准确多项式/积分/jet 方法，构造时核新域；
- `strict_witness_controls`：式 (4) 的准确有理控制。

`scripts/fd2d_gc_dyadic_tail_native.py` 的新 schema 将**完整旧 parent native 定义**与**明确新 tail override**共同作为一个完整新场定义。它由正常旧 reader 加载合法 parent，保留其真实 raw P1、mesh、中央、profile、atlas、全部窗口，然后同时替换参数 tail 段和全部 plain lifting 副本中的 tail；新类重新以准确函数界核 PSD 切口条件。它没有将负系数传给旧 archive guard，没有临时伪造正参数，没有改旧类名或模块名，也没有把旧 archive 说成包含新参数。

`positive_bernstein` 这个旧字符串在继承的 `curvature_second_y` 中仅选择原多项式导数公式。新定义明确将该 **basis tag** 与新 domain/class/schema 分开。完整 reader 和 body dispatch 使用各自的新 schema；旧 reader 仍拒绝这些新定义。

当前求解入口尚有独立限制：`RawBumpDAE.parameter_domain` 的全局 min/max、父 tail-kind dispatch、`PositiveTraceBoundedSchur` 的逐系数 bounds，以及独立 native 的 kind/cut guard。未来求解器必须显式接新 tail factory、新域和 (11)，才可使用该扩大域。本结果不修改这些冻结入口，不运行 BVP 或 whole Jacobian。新的完整 field/body reader 是可消费定义，不是已经接好的新主求解器。

有限小核的真实输入、输出、退出回执与源码身份见本结果对应闭存 manifest；严格包含及几何传递已经由上述准确证明给出，不依赖小核采样。
