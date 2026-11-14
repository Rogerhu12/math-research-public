# 实际 GM Wronskian 与完整 Kummer 导数行

日期：2026-11-12。状态：本文的 Wronskian、完整精度积分分部、
模 $p^2$ 公式及实际 Kummer 专门化均已证明。
它们把一个增长阶数的对数原函数 jet 换成固定单位的代数对数导数，
但没有证明所需中央行在无穷多个素数处非零。

全篇取 $p\equiv3\pmod4$、$p\ge7$。使用
[实际整 GM Frobenius](2026-11-12-integral-gm-frobenius-critical-row.md)
的同一行约定、整基及实际 Frobenius 常数
$$
F(0)=\begin{pmatrix}0&pa\\ b&0\end{pmatrix},
\qquad a,b\in\mathbb Z_p^\times,\qquad ab=-1.
\tag{1}
$$
这里 $a,b$ 不是曲线的 Frobenius trace。
令
$$
s=1-4t^2,\quad s_\phi=1-4t^{2p},\quad
q=\frac b{pa},\quad r=\frac{pa}b=q^{-1}.
$$
固定周期 $K,L$ 满足
$$
sy''-8ty'-y=0,\qquad
K(0)=L'(0)=1,\quad K'(0)=L(0)=0,\quad
KL'-K'L=s^{-1}.
\tag{2}
$$
实际整函数为
$$
\begin{aligned}
U&=K(t^p)K-qL(t^p)L,\\
V&=L'(t^p)L-rK'(t^p)K.
\end{aligned}
\tag{3}
$$
先求导再代入的 $L'(t^p)$ 与 $dL(t^p)/dt$ 必须区分。
整性 $U,V\in\mathbb Z_p[[t]]$ 已由上述整 Frobenius 证明，
不是从 (3) 各项分别整推得。置
$$
H=V/t,\qquad B=U/H,\qquad \zeta=U/V=B/t.
\tag{4}
$$
它们满足
$$
U=1+\tfrac12t^2+\cdots,\quad
H=1+\tfrac32t^2+\cdots,\quad
B=1-t^2+\cdots.
\tag{5}
$$
$U,H,B$ 都是偶级数；$\zeta=t^{-1}-t+\cdots$ 是奇 Laurent 级数。

## 1. 完整 Wronskian

准确的特征零恒等式为
$$
\boxed{
UV'-U'V
=\frac1{s s_\phi}
-p^2\frac ab\,\frac{t^{p-1}U^2}{s_\phi}
+\frac{8p\,t^{2p-1}UV}{s_\phi}
+\frac ba\,t^{p-1}V^2.}
\tag{6}
$$

证明保留 (3) 中可变系数的导数。写
$$
\binom UV=T(t)\binom KL,\qquad
T=\begin{pmatrix}K(t^p)&-qL(t^p)\\
                 -rK'(t^p)&L'(t^p)\end{pmatrix}.
$$
由 (2)，$\det T=s_\phi^{-1}$，并且
$$
T'T^{-1}
=\begin{pmatrix}
0&-qpt^{p-1}\\
-rpt^{p-1}/s_\phi&8pt^{2p-1}/s_\phi
\end{pmatrix}.
\tag{7}
$$
例如第二行使用
$y''(t^p)=(y(t^p)+8t^py'(t^p))/s_\phi$；
所以 (7) 并不把 $T$ 当成常矩阵。
原周期 Wronskian 对 (6) 的贡献是
$\det T\,(KL'-K'L)=1/(s s_\phi)$。
若记 (7) 为 $(m_{ij})$，其余贡献为
$m_{21}U^2+(m_{22}-m_{11})UV-m_{12}V^2$，
立即得到 (6)。

由 $\zeta'=-(UV'-U'V)/V^2$，(6) 等价于
$$
\boxed{
\frac{U}{sV^3}
=-\frac{s_\phi}{2}(\zeta^2)'
+p^2\frac ab\,t^{p-1}\zeta^3
-8pt^{2p-1}\zeta^2
-\frac ba\,s_\phi t^{p-1}\zeta.}
\tag{8}
$$
特别，不能把 $U/(sV^3)\,dt$ 在整个形式盘中无修正地换成
$-\tfrac12d\zeta^2$。

## 2. 完整临界行只需 $f'$ 及两个低次系数

沿用[一阶模数与临界投影](2026-11-12-first-modulus-vectorial-extension-and-critical-projection.md)
的实际泛函
$$
F_i=\frac{U^{p+1}}{sH^{p+2}},\qquad
\mathcal P_p(f)=[t^{p+1}]\frac{fF_i}{V}.
\tag{9}
$$
若 $f\in\mathcal O[[t]]$，其中 $\mathcal O$ 为任意包含实际系数的
未分歧整扩张，则 (9) 仍在 $\mathcal O$ 中。
它有精确留数表达
$$
\mathcal P_p(f)
=\operatorname{Res}_{t=0}
 f\zeta^p\frac{U}{sV^3}\,dt.
\tag{10}
$$
记 $f_j=[t^j]f$。核心公式是
$$
\boxed{\quad
\mathcal P_p(f)
=\frac1{p+2}[t^{p+1}]f'B^{p+2}
-\frac ba f_1
+p^2\frac ab\bigl(f_3-(p+3)f_1\bigr).
\quad}
\tag{11}
$$
这是特征零完全相等，不是一个忽略除 $p$ 精度的同余。

将 (8) 代入 (10)。第一项为
$$
-\operatorname{Res}s_\phi f\zeta^{p+1}d\zeta
=\frac1{p+2}\operatorname{Res}(s_\phi f)'\zeta^{p+2}\,dt.
\tag{12}
$$
因 $s_\phi-1$ 从次数 $2p$ 开始，其修正的最低次数至少为
$2p-1-(p+2)=p-3\ge4$，不能贡献留数。
所以 (12) 是 (11) 的第一项。这里使用的除数是单位 $p+2$。

(8) 中第三项乘 $\zeta^p$ 后也从次数 $p-3$ 开始，没有留数。
第二、四项分别给
$$
\begin{aligned}
p^2\frac ab\operatorname{Res}
 f t^{p-1}\zeta^{p+3}dt
 &=p^2\frac ab[t^3]fB^{p+3}
 =p^2\frac ab\bigl(f_3-(p+3)f_1\bigr),\\
-\frac ba\operatorname{Res}
 s_\phi f t^{p-1}\zeta^{p+1}dt
 &=-\frac ba[t]fB^{p+1}=-\frac ba f_1.
\end{aligned}
$$
已使用 (5) 及 $B$ 的偶性；$s_\phi-1$ 的项仍然过高。
这证明 (11)，不要求 $f$ 有任何额外消失阶。

## 3. 模 $p^2$ 精度及先做 Cartier 时的修正

令
$$
D_p(f)=[t^{p+1}]f'B^2,\qquad
E_p(f)=[t^{p+1}]f'B^2\log B.
\tag{13}
$$
这些所需截断都整：$B-1$ 从次数二开始，
所以 $\log B$ 到次数 $p+1$ 只用到分母
$1,\ldots,(p+1)/2$，全为 $p$ 单位。
同理，截断中
$B^p\equiv1+p\log B\pmod{p^2}$。
由 (11) 得
$$
\boxed{
\mathcal P_p(f)\equiv
\frac12D_p(f)-\frac ba f_1
+\frac p2E_p(f)-\frac p4D_p(f)
\pmod{p^2}.}
\tag{14}
$$
在需要把一个已被 $p$ 整除的表达式再除以 $p$ 时，
(14) 的最后两项不能删掉。

为与先做模 $p$ Cartier 的计算直接比较，另置
$$
\mathcal Q_p(f)=[t^{p-1}]f\,\frac{U}{sV^3}.
$$
对 (8) 逐项取系数，完整精度得到
$$
\mathcal Q_p(f)=
\frac12[t^{p-1}]f'\zeta^2
-\frac p2[t^p]f\zeta^2
-\frac ba f_1
+p^2\frac ab(f_3-3f_1).
\tag{15}
$$
特别第二项 $-\tfrac p2[t^p]f\zeta^2$ 不能在除 $p$ 前省去。
另一方面 $B^p\equiv1+O(t^{2p})\pmod p$，故 (10) 给
$\mathcal P_p(f)\equiv\mathcal Q_p(f)\pmod p$。
一致地，(11) 或 (15) 都给
$$
\mathcal P_p(f)\equiv
\frac12[t^{p-1}]f'\zeta^2-\frac ba f_1
\pmod p.
\tag{16}
$$
完整 (11) 已把 (15) 的两类积分分部项合并，因此使用它时
不需要额外保留一个未计算的 $\mathcal P_p-\mathcal Q_p$。

## 4. 专门化为实际固定除法单位

使用[实际 Kummer 垂直 jet](2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)
的同一 $h_e,h_o,M_e,M_o$ 及 $\eta=c_e/c_o^\sigma$。
取局部 Frobenius lift
$\phi(t)=t^p,\ \phi(Z)=Z^p$，并写
$$
f(t)=[Z^p]B_e(t,Z).
\tag{17}
$$
$B_e$ 是已证明整的归一 Kummer Frobenius 对数 cochain，
所以 $f$ 满足上文的整性假设。
系数 Frobenius 在惰性处交换两条 CM 半线。
逐项对基参数求导准确得到
$$
f'(t)
=\eta\,t^{p-1}M_o'(t^p)-R_p(t),\qquad
R_p(t):=[Z^p]\partial_t h_e(t,Z).
\tag{18}
$$
这里 $\partial_t h_e$ 是固定两个有理单位的代数对数导数的固定
线性组合。它作为 $(t,Z)$ 的代数函数是固定的；
取 $[Z^p]$ 的指数仍然随 $p$ 增长。

由 $M_o(t)=t+O(t^3)$、$[t^2]B^{p+2}=-(p+2)$，(11) 给更具体的
**完整精度**公式
$$
\boxed{
\mathcal P_p(f)=
-\eta-\frac1{p+2}[Z^p t^{p+1}]
          (\partial_t h_e)B^{p+2}
-\frac ba f_1
+p^2\frac ab\bigl(f_3-(p+3)f_1\bigr).}
\tag{19}
$$
特别模 $p$ 后
$$
\mathcal P_p(f)\equiv
-\eta-\frac12[Z^p t^{p-1}]
             (\partial_t h_e)\zeta^2
-\frac ba f_1\pmod p.
\tag{20}
$$
亦可由 (16) 及 $[t^0]\zeta^2=-2$ 直接复核符号。

还应保留一项实际取消。前述一阶模数稿定义
$$
E_{e,p}=-f-\frac{b_p-H_p}{p}M_e.
$$
其中央比较为
$$
h_p\,C_{p+1}/p\equiv
-\eta-\mathcal P_p(W_{e,p})/p+\mathcal P_p(E_{e,p})
\pmod p.
$$
把 (20) 代入 $-\mathcal P_p(f)$ 后产生的 $+\eta$，
恰好抵消该比较原有的 $-\eta$。
所以这个已知单位不是一个独立的非零贡献。

本篇的正面变化是 (19)：真实临界泛函可用固定代数
$\partial_t h_e$、真实整 Frobenius 的 $B$，以及两个低次系数
完整计算；没有丢弃第二 Witt 层或 Frobenius Wronskian 修正。
但目前没有证明该联合行下降为一个固定维数、已有非零定理的
Frobenius 条目，也没有证明 (19) 中剩余项不能相消。

## 验证与输入范围

- 只用已经证明的实际整 crystalline Frobenius、固定周期方程、
  实际 Kummer 共链及其明确规范；链接见正文。
- (6)、(11) 另以有理数截断周期独立检查了 $p=7,11$。
  检查使用 $a=1,b=-1$ 的代数参数，只校准恒等式的符号与系数，
  不用该任意选择宣称实际 $U,V$ 的整性；一般证明是 §1–2。
- 对数导数代数性不把 $[Z^p]$ 变为固定指数，
  也不把 $B$ 当成独立于 $p$ 的代数函数。
