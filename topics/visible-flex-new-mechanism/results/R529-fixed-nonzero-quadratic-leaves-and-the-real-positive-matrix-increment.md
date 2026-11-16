# R529：固定非零平方零叶的原 $p_1$ 严格号与 R527 的真实非零矩阵输出

日期：2026-11-16。**完整原式纸面证明；没有执行符号、数值、profile、秩或新的科学任务。**

[R527](R527-finite-amplitude-same-gauge-ruling-paths-with-complete-matrix-memory.md) 已给同一母库、固定规范、真实八矩演化下的有限幅全相位 ruling 路径。其曲率换号并超过 $1$，$\omega$ 振幅也超过较弱的 $2/h_{\max}$ 门；这些幅度条件没有支付矩阵返回。

本文给出一个具体、完整的后继判定。在任意固定非零三矩向量定义的平方零曲面上，从 $k=0$ 常态出发的真实水平叶，原 $p_1$ 密度具有固定严格号；退化直线情形则由原 $t_1$ 密度直接排零矩。因此，不能仅沿这种固定非零零叶正向走动、反向走动或重复，来配平整个原八矩。

R527 的实际路径只贴近该零叶，并不字面位于零叶。但它的完整有限误差已足以判定：对该稿固定的非平凡参考弧，充分大的每一个有限前缀长度都给严格正的实际 $p_1$ 总值，所以这族实际路径本身不是 $M=0$ 返回。

这不是全 ruling 路径的普遍障碍。横穿不同平方曲面、非零初始曲率、改变主导 history 方向，或从起点令三个平方系数全部为零，均不在本文排除范围内。

## 1. 固定的是原八矩坐标与三个真实常数

实际几何始终满足
$$
h>0,\qquad \omega_s=\frac{k_s}{2h},\qquad d=h\omega-k.
\tag{1}
$$
固定一个常态入口
$$
S_c=(h_c,0,\omega_c),\qquad h_c>0.
\tag{2}
$$
把物理坐标仅记为 $y=x+\omega_c$，不改变实际路径、profiles、锚或任何规范。按 R73/R524，原真实八矩的相应固定坐标是
$$
\boxed{
p_1^{\,\omega_c}=k^2-kh(\omega-\omega_c)
=k(\omega_ch-d),
}
\tag{3}
$$
$$
\boxed{
8t_1^{\,\omega_c}
=2kh(\omega-\omega_c)-k^2-1-(h_s/h)^2.
}
\tag{4}
$$
全 $M_{\rm raw}$ 积分为零必使(3)(4)的积分均为零。这里没有改用删除端势的矩阵呈示。

令三个固定实数为 $(q_0,q_1,q_2)$，并假设
$$
(q_0,q_1,q_2)\ne(0,0,0),\qquad
(1+h_c^2\omega_c^2)q_0+2h_c^2\omega_cq_1+h_c^2q_2=0.
\tag{5}
$$
考虑其正高度零曲面
$$
\boxed{
q_0(1+d^2)+2q_1hd+q_2h^2=0.
}
\tag{6}
$$
对于 R527，这正是 $q_S(A_c)=0$，三个数来自完整原 physical 配对；下文不使用其 principal 近似或任何母形符号。

## 2. 非退化双曲线的完整水平第一积分

先设 $q_0\ne0$。置
$$
a=\frac{q_1}{q_0},\qquad
b^2=\frac{q_1^2-q_0q_2}{q_0^2}.
$$
由(5)，
$$
b^2=\frac{1+(h_c\omega_c+ah_c)^2}{h_c^2}>0.
$$
取 $b>0$。式(6)准确为
$$
(d+ah)^2+1=b^2h^2.
$$
全部正高度分支可用一个真实参数 $t$ 表示：
$$
\boxed{
h=\frac{\cosh t}{b},\qquad d=\sinh t-ah.
}
\tag{7}
$$
入口对应唯一 $t_c$，满足
$$
\cosh t_c=bh_c,\qquad
\sinh t_c=h_c(\omega_c+a).
\tag{8}
$$

由 $k=h\omega-d=h(\omega+a)-\sinh t$，原水平关系(1)给
$$
h\,d\omega=(\omega+a)\,dh-\cosh t\,dt.
$$
这里 $d\omega,dh,dt$ 是沿同一真实路径的微分。即使 $t_s$ 为零或换号，此微分身份仍逐点成立，未假设 $t$ 是单调时钟。

代入(7)并用
$$
\Theta(t)=\arctan(\sinh t),\qquad
\Theta'(t)=\operatorname{sech}t
$$
得到完整第一积分
$$
d\!\left(\frac{\omega+a}{\cosh t}\right)
=-b\,d\Theta(t).
\tag{9}
$$
定义
$$
\boxed{
f(t)=\Theta(t)+\frac{\sinh t}{\cosh^2t}.
}
\tag{10}
$$
入口 $k=0$ 使(9)的常数准确为 $bf(t_c)$，故整条水平叶满足
$$
\boxed{
\omega+a=b\cosh t\{f(t_c)-\Theta(t)\},
}
$$
$$
\boxed{
k=\cosh^2t\{f(t_c)-f(t)\}.
}
\tag{11}
$$
这不是只在入口作线性化。它保实际入口常数，并适用于同一叶上的任意有限往返、停顿与重复。

## 3. 原 $p_1$ 在非恒处严格为正

由(8)，
$$
\omega_ch-d
=(\omega_c+a)\frac{\cosh t}{b}-\sinh t
=\frac{\sinh(t_c-t)}{\cosh t_c}.
\tag{12}
$$
同时，直接微分(10)得到
$$
\boxed{f'(t)=2\operatorname{sech}^3t>0.}
\tag{13}
$$
因此 $f(t_c)-f(t)$ 与 $\sinh(t_c-t)$ 同号，并且二者同时为零当且仅当 $t=t_c$。

将(11)(12)代入原(3)，得到完整点态式
$$
\boxed{
p_1^{\,\omega_c}
=\frac{\cosh^2t}{\cosh t_c}
\{f(t_c)-f(t)\}\sinh(t_c-t)\ge0.
}
\tag{14}
$$
严格等号范围是
$$
p_1^{\,\omega_c}=0
\quad\Longleftrightarrow\quad t=t_c
\quad\Longleftrightarrow\quad S=S_c
$$
在这条由原入口确定的水平叶上成立。

所以任何正长度的非恒光滑路径，只要始终满足(6)并从(2)出发，就有
$$
\boxed{\int p_1^{\,\omega_c}\,ds>0.}
\tag{15}
$$
非恒性给一个真正开时间区间使 $t\ne t_c$，故最后为严格积分号。改变行进方向不改变(14)的密度号；在曲线两侧分别走正、负曲率也不能让这条矩阵坐标抵消。

若整段恰为常态，(4)则为 $t_1^{\,\omega_c}=-1/8$，其正长度积分仍非零。故该情形也不是原 $M=0$ 路径。

## 4. $q_0=0$ 的全部退化情形

若 $q_0=0$ 而三向量非零，因零曲面包含(2)，必有 $q_1\ne0$。否则(6)会给 $q_2h^2=0$，迫 $q_2=0$，与非零假设矛盾。

此时(5)(6)准确给
$$
d=\omega_ch.
$$
所以
$$
k=h(\omega-\omega_c).
$$
代入原水平关系，
$$
d\!\left(\frac{\omega-\omega_c}{h}\right)=0.
$$
入口 $k=0,\omega=\omega_c$ 迫整叶
$$
\boxed{k=0,\qquad\omega=\omega_c.}
\tag{16}
$$
$h$ 可以非恒，但原(4)成为
$$
\boxed{
t_1^{\,\omega_c}
=-\frac18\{1+(h_s/h)^2\}<0.
}
\tag{17}
$$
故任意正长度实际路径的总矩仍非零。

综上得到一个完整几何结论：

> 固定任意非零 $(q_0,q_1,q_2)$，其正高度零曲面通过原 $k=0$ 常态。任何从该常态出发、始终位于该零曲面上的正长度真实水平路径，都不可能有全 $M_{\rm raw}$ 积分为零。双曲情形由 $p_1$，退化直线情形由 $t_1$ 准确分离。

此结论没有使用第四 ruling，所以它适用于满足这些几何前提的任何母库与任何规范；也不能因此扩到不满足(6)的路径。

## 5. R527 的参考弧与实际有限误差

R527 选择
$$
(q_0,q_1,q_2)
=\kappa(1,-\omega_c,\omega_c^2-h_c^{-2}),
\qquad \kappa>0.
$$
故本稿(7)取 $a=-\omega_c$、$b=h_c^{-1}$、$t_c=0$。其参考弧正是
$$
h_0=h_c\cosh t,\quad
k_0=-\sinh t-\cosh^2t\,\arctan(\sinh t),
$$
$$
\omega_0=\omega_c-
h_c^{-1}\cosh t\,\arctan(\sinh t).
\tag{18}
$$
原 $p_1$ 的完整密度随之为
$$
\boxed{
p_{1,0}^{\,\omega_c}
=\sinh^2t+
\sinh t\,\cosh^2t\,\arctan(\sinh t)>0
\quad(t\ne0).
}
\tag{19}
$$
这保原物理 $h,k,\omega$，并非按主阶把矩阵截短。

固定 R527 的那条非平凡平端参考时钟 $t=t(s)$，令
$$
\delta=\int_0^L p_{1,0}^{\,\omega_c}(s)\,ds>0.
\tag{20}
$$
R527 的实际解满足
$$
S_\epsilon\longrightarrow S_0\quad\text{于 }C^1[0,L],
\qquad \epsilon=T_0^{-1}\downarrow0.
$$
因为(3)是当前 scalar 状态的光滑函数，原完整积分因此满足
$$
\int_0^L p_{1,\epsilon}^{\,\omega_c}\,ds
=\delta+O(\epsilon).
\tag{21}
$$
这里用的是已付实际路径误差，不把其小法向坐标
$q_S(A_c)=\epsilon z_0(s)$ 重新设为零。

真实前缀在 $S_c$ 上，其 $p_1^{\,\omega_c}$ 密度字面为零。于是对充分大的每一个有限 $T_0$，
$$
\boxed{
[p_1^{\,\omega_c}](M_{\rm total})
=\int_0^L p_{1,\epsilon}^{\,\omega_c}\,ds
>\delta/2>0.
}
\tag{22}
$$
所以 R527 的这族完整实际路径不能自身成为 $M=0$ 返回。其非零第二、第三历史与全部基准都未被删除。

本文不改 R527 已付的正向结果：同一规范的全相位 ruling、统一正则反馈、有限曲率换号，以及超过较弱 $2/h_{\max}$ 的实际 $\omega$ 振幅都仍成立。只是这些必要幅度条件不足以关闭当前这一真实八矩坐标。

## 6. 下一入口的准确范围

本稿排除了把一个固定非零平方零叶当成完整零矩桥的做法。它不排除从同一个固定母出发在更大的当前 history 方向中运动，也不排除一段真正横穿该零曲面的路径取得负的 $p_1$ 积分。

特别，若从起点额外取得
$$
q_0(A_c)=q_1(A_c)=q_2(A_c)=0,
\tag{23}
$$
则 $q_S(A_c)$ 在全部当前 scalar 状态上恒零，(6)不再限定几何曲面。本稿的单叶第一积分及严格号不适用。此时在固定合法状态、速度和真实 $B$ 紧盒内，长前缀后的完整次数式仍保
$$
F/T_0
=\ell_S(\gamma,\upsilon)
+2b_S(A_c,\Phi_B)+O(T_0^{-1}),
\qquad B'=M_{\rm raw}(S,\gamma,\upsilon),
$$
但它只是下一条真实历史控制系统的入口，不由(23)自动得到零矩或全闭路径。尤其 $B$ 的后续方向不能冻结。

原 frame、位置、完整 $T,V$、固定十三行与主几何条件仍保其原任务范围。本文完成的是(14)–(17)的全零叶分离，以及对 R527 实际有限路径的准确非零矩阵判定；没有将这个具体分支的阻断外推成全问题无解。

