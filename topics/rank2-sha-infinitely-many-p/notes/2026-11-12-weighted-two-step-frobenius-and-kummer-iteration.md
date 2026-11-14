# 二次 Frobenius 的加权精度与实际 Kummer 迭代格

日期：2026-11-12。状态：加权矩阵估计、短输入精度加强、实际
Kummer 迭代及指定投影的整性均已证明。
没有证明新的跨素数非零结论。

本篇接续
[迭代 GM 与完整惰性证书](2026-11-12-iterated-gm-frobenius-and-complete-inert-jets.md)。
始终取 $p\ge7$、$p\equiv3\pmod4$，
$\rho=p^{-1/(p+1)}$。模参数为 $t$，纤维正式参数为 $Z$；
两者不得混同。

## 1. 只有第一个归一化 GM 因子付出加权非整代价

前篇已证明真实且有理的矩阵

$$
G_p(t)=-pY(t^{p^2})Y(t)^{-1}
 \in M_2(\mathbb Q[[t]])\cap M_2(\mathbb Z_p[[t]]),
\qquad G_p(0)=-pI.
\tag{1.1}
$$

令

$$
A_j(t)=-G_p(t^{p^{2j}})/p
 =Y(t^{p^{2j+2}})Y(t^{p^{2j}})^{-1}.
\tag{1.2}
$$

矩阵 Gauss 范数取各条目范数的最大值。准确有

$$
\boxed{\qquad
\|A_0\|_\rho\le\rho^{-1},\qquad
\|A_j\|_\rho=1\quad(j\ge1).
\qquad}
\tag{1.3}
$$

**证明。** 前篇的周期计数给

$$
\|K\|_\rho\le1,\quad \|L\|_\rho=\rho,\quad
\|K'\|_\rho\le\rho^{-1},\quad\|L'\|_\rho\le1.
$$

因 $Y^{-1}=s\begin{pmatrix}L'&-L\\-K'&K\end{pmatrix}$、
$s=1-4t^2$，所以 $\|Y^{-1}\|_\rho\le\rho^{-1}$。
$Y-I$ 没有常数项，故对 $r<\rho$，

$$
\|Y-I\|_r\le r\rho^{-2}.
\tag{1.4}
$$

当 $r=\rho^{p^{2j}}$、$j\ge1$ 时，右端严格小于一。
所以在这些较小盘上 $Y$ 和 $Y^{-1}$ 的范数均为一。
(1.2) 立即给出 (1.3)；常数矩阵为 $I$，使后一个等号准确成立。$\square$

$A_0$ 一般不是系数整矩阵。事实上前篇锐界给它在 $t^p$ 的
$(2,1)$ 系数赋值为 $-1$，该项的加权范数正好是 $\rho^{-1}$。
因此 (1.3) 没有声称 $G_p/p$ 是原系数格上的免费整基变换。

## 2. 所有迭代层统一只损失一层输入精度

设 $\widetilde G_p$ 给出 $G_p$ 的一个有限 jet，所有非恒定系数
绝对误差都在 $p^N\mathbb Z_p$，并将已知常数项准确置为 $-pI$。
在实际使用的有限截断代数中置
$\widetilde A_j=-\widetilde G_p(t^{p^{2j}})/p$。
则

$$
\|\widetilde A_j-A_j\|_\rho
 \le p^{-(N-1)}\rho^{p^{2j}}.
\tag{2.1}
$$

当 $N\ge1$ 时，近似矩阵满足与 (1.3) 相同的上界。
令

$$
Q_a=A_{a-1}\cdots A_0,\qquad
\widetilde Q_a=\widetilde A_{a-1}\cdots\widetilde A_0.
$$

逐因子展开两个乘积的差：$j=0$ 的项不含另一个 $A_0$；
每个 $j\ge1$ 的项至多额外付出一个 $\rho^{-1}$。
因为 $p^{2j}-1\ge1$，得到与迭代次数无关的界

$$
\boxed{\qquad
\|\widetilde Q_a-Q_a\|_\rho
 \le p^{-(N-1)}\rho .
\qquad}
\tag{2.2}
$$

两者常数矩阵准确为 $I$，所以其 $(1,2)$ 差项可除以 $t$。
恢复 $\mathcal K=(Q_a)_{22}$、$\mathcal L=-(Q_a)_{12}/t$ 时，

$$
\|\Delta\mathcal K\|_\rho\le p^{-(N-1)}\rho,\qquad
\|\Delta\mathcal L\|_\rho\le p^{-(N-1)}.
\tag{2.3}
$$

这是加权范数中的准确损失；它不否定前篇按绝对系数精度计算的
$p^a$ 分母。非恒定误差被 $t\mapsto t^{p^{2j}}$ 推到较高次数，
且每条乘积误差至多遇到一个非整首因子，正是 (2.2) 改善的原因。

### 2.1 完整中央测试的加强输入范围

令

$$
m=(p+1)p^n,\quad P=4n+4,\quad L=P-1,\quad
D=\min\{m,\,2(p+1)L+4\},
$$

并取最小的 $a\ge1$ 使 $p^{2a}>D-3$。
前篇证明：只需 $M_1$ 到次数 $D$、周期到次数 $D-4$，
就可确定 $S_{p,n}=p^{p^n}C_m$ 模 $p^P$。

利用 (2.3)，这一测试现在只需

$$
\boxed{
\begin{array}{ll}
G_p\text{ 到次数 }D-3\text{，绝对精度 }p^{\,4n+4},\\
M_1\text{ 到次数 }D\text{，绝对精度 }p^{\,4n+3}.
\end{array}}
\tag{2.4}
$$

第 $j$ 个因子实际仅使用到 $\lfloor(D-3)/p^{2j}\rfloor$ 次。
证明是取 $N=P$：两个恢复周期的 Gauss 误差至多为 $p^{-L}$。
$M_1$ 误差至多为 $p^{-L}\rho^4$，
所以高权表达式误差仍至多为 $p^{-L}\rho^4$。
取第 $m$ 次系数再乘 $p^{p^n}$，误差赋值至少

$$
L+p^n-\frac{m-4}{p+1}=L+\frac4{p+1},
$$

因赋值为整数，至少为 $P$。
截断尾项已由前篇的同一 Gauss 估计处理。
因此 (2.4) 保留完整判据

$$
J_p'(0)\ne0
\iff \exists n\ge0:\quad S_{p,n}\not\equiv0\pmod{p^{4n+4}}.
\tag{2.5}
$$

这里仍只把 (2.5) 用作惰性 $\Sha[p^\infty]$ 有限的充分判据。
输出仍是高权系数提取；输入长度和精度的改善并不自动给出跨素数成功率。

## 3. 实际 Kummer 两次迭代的正确格

使用 [R71](../results/R71-actual-kummer-frobenius-and-compensated-critical-jet.md)
的两个实际单位、对数半线 $h_e,h_o$ 与整修正 $B_e,B_o$。
完整规范见 [Kummer 垂直 jet 与 GM 配对](2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)。
它们满足

$$
\partial_Zh_e(t,0)=M_e=M_1,\qquad
\partial_Zh_o(t,0)=M_o=t+t^3/2+\cdots.
$$

本节明确采用合法的局部形式 lift

$$
\phi(t)=t^p,\qquad \phi(Z)=Z^p
\tag{3.1}
$$

及系数 Witt Frobenius $\sigma$，记完整作用为 $\Phi$。
这没有把该形式 lift 声称为特征零椭圆曲线的次数 $p$ 自同源。

对实际归一单位 $r\in1+Z\mathcal O[[t,Z]]$，

$$
B_r=\frac1p\log\frac{\Phi(r)}{r^p}
 \in\mathcal O[[t,Z]],\qquad B_r(t,0)=0.
$$

所以原对数的 $h$ 次迭代准确为

$$
\Phi^h(\log r)-p^h\log r
 =p\sum_{j=0}^{h-1}p^{h-1-j}\Phi^j(B_r).
\tag{3.2}
$$

特别两次的整修正是 $pB_r+\Phi(B_r)$。
若再除 $p$，所得 $B_r+\Phi(B_r)/p$ 不自动整。

对实际偶半线，令 $\epsilon_j=e$ 当 $j$ 为偶数、$\epsilon_j=o$
当 $j$ 为奇数，并置
$\eta_j=c_e/c_{\epsilon_j}^{\sigma^j}\in\mathcal O^\times$。
保持 R71 已证明的系数共轭方向，正确的归一迭代为

$$
\boxed{\quad
\mathcal D_{e,h}
=\frac{\eta_h\Phi^h(h_{\epsilon_h})-p^h h_e}{p^h}
=\sum_{j=0}^{h-1}p^{-j}\eta_j\Phi^j(B_{\epsilon_j}).
\quad}
\tag{3.3}
$$

证明可直接把 R71 的两个单位对数代入 (3.2)；
$\sigma(i)=-i$ 恰在奇数层交换两半线。
$\eta_0=1$，所以首项为 $B_e$。
(3.3) 的完整整结论只有 $p^{h-1}\mathcal D_{e,h}$ 整；
不能从两个单位斜率直接把 $\mathcal D_{e,h}$ 认作整 cochain。

## 4. 第一个非整垂直 jet 及其准确 GM 投影

在 (3.1) 的规范下，R71 的一阶式简化为

$$
[Z]B_e=-M_e,\qquad [Z]B_o=-M_o.
\tag{4.1}
$$

对每个 $h\ge2$，(3.3) 中 $j\ge2$ 的项从 $Z^{p^2}$ 才开始，
因此

$$
\boxed{\quad
[Z^p]\mathcal D_{e,h}
=[Z^p]B_e-\frac{\eta_1}{p}M_o(t^p).
\quad}
\tag{4.2}
$$

次数小于 $p$ 的所有垂直 jet 均整。
但 (4.2) 的 $t^p$ 系数赋值准确为 $-1$，其乘 $p$ 后为
$-\eta_1\pmod p$。
由于 $B_e,B_o$ 均属于 $(t,Z)^2\mathcal O[[t,Z]]$，
更可准确说：$\mathcal D_{e,h}$ 的总次数小于 $2p$ 的系数均整，
而 $t^pZ^p$ 在总次数 $2p$ 给出真正的首个分母。
没有把这一失败隐藏在一个任意选择的 cochain 代表中。

该非整行的实际模块 Gauss 范数恰为

$$
\big\|[Z^p]\mathcal D_{e,h}\big\|_\rho=\rho^{-1}.
\tag{4.3}
$$

事实上 $[Z^p]B_e$ 整，范数至多一；而
$\|M_o(t^p)/p\|_\rho=p\rho^p=\rho^{-1}>1$。
这与 (1.3) 首个归一 GM 因子的真实加权代价相同。

另一方面，[R74](../results/R74-first-modulus-and-divided-witt-critical-projection.md)
的实际整投影为

$$
\mathcal P_p(F)=[t^{p+1}]F\,F_i/V,\qquad
F_i=\frac{U^{p+1}}{s(V/t)^{p+2}}.
$$

同一全文亦见
[一阶模数与实际临界投影](2026-11-12-first-modulus-vectorial-extension-and-critical-projection.md)。
已证明的完全精度公式是 $\mathcal P_p(M_o(t^p))=-p$。
因此 (4.2) 给

$$
\boxed{\quad
\mathcal P_p([Z^p]\mathcal D_{e,h})
=\mathcal P_p([Z^p]B_e)+\eta_1\in\mathcal O.
\quad}
\tag{4.4}
$$

$\mathcal P_p$ 将整级数送到整系数，因为 $V=t$ 乘一个整单位。
所以这里确实发生了指定行上的整除恢复，并留下一个已知单位。
右边另一个项仍是实际的未知投影。
[R78](../results/R78-exact-wronskian-and-kummer-critical-cancellation.md)
已进一步证明，该投影内部恰有 $-\eta_1$，与 (4.4) 的显式单位自动相消。
具体地，置 $f=[Z^p]B_e$、$f_j=[t^j]f$、$B=tU/V$，
并写实际初值为 $F_0=\begin{pmatrix}0&p\alpha\\\beta&0\end{pmatrix}$、
$\alpha\beta=-1$，则

$$
\begin{aligned}
\mathcal P_p([Z^p]\mathcal D_{e,h})={}&
-\frac1{p+2}[Z^pt^{p+1}](\partial_t h_e)B^{p+2}
-\frac\beta\alpha f_1\\
&+p^2\frac\alpha\beta\bigl(f_3-(p+3)f_1\bigr).
\end{aligned}
\tag{4.5}
$$

所以该整化不产生一个独立非零单位；它保留的是带全部 GM 权重的
固定代数对数导数及其初值项。
(4.4)–(4.5) 使用首个临界投影，未将其未经比较推广成所有高权的同一单位公式。

## 5. 可联合使用的有界二变量格

取纤维半径 $\tau=p^{-1/(2p)}$，则 $\rho<\tau$。
由于 $B_e,B_o$ 的总零阶至少二，

$$
\|\Phi^j(B_{\epsilon_j})\|_{\rho,\tau}
 \le\tau^{2p^j}.
$$

因此 (3.3) 给与 $h$ 无关的完整界

$$
\boxed{\quad
\|\mathcal D_{e,h}\|_{\rho,\tau}\le1.
\quad}
\tag{5.1}
$$

确实 $j=0$ 的上界为 $\tau^2<1$，$j=1$ 的上界为
$p\tau^{2p}=1$，$j\ge2$ 的上界是
$p^{\,j-p^{j-1}}<1$。
这是在明确的二变量 Gauss 格中成立的有界性，不是原系数格中的整性。


还有一个直接的固定原函数解释。由于 $h_e(t,0)=h_o(t,0)=0$，
(3.3) 定义式中的 $\Phi^h(h_{\epsilon_h})$ 从 $Z^{p^h}$ 才开始，
所以

$$
\mathcal D_{e,h}\equiv-h_e\pmod{Z^{p^h}}.
\tag{5.2}
$$

特别 $h\ge2$ 时，
$[Z^p]\mathcal D_{e,h}=-[Z^p]h_e$，与 (4.2) 完全一致。
此外，归一单位的对数在
$(\rho^{p^h},\tau^{p^h})$ 上对充分大的 $h$ 的范数至多为
$\tau^{p^h}$；这是 $\log(1+x)$ 在严格小于
$p^{-1/(p-1)}$ 的盘上的直接等距估计。
固定线性组合的系数和 $\eta_h$ 均为单位，故

$$
\left\|\frac{\eta_h\Phi^h(h_{\epsilon_h})}{p^h}\right\|_{\rho,\tau}
 \le p^h\tau^{p^h}\longrightarrow0.
$$

于是 $\mathcal D_{e,h}$ 在同一闭双圆盘上一致收敛到固定的 $-h_e$。
这说明迭代 cochain 的极限确是原单位的固定对数原函数，
不是新产生的独立中央非零输入。

至此，短输入矩阵 (2.4) 与实际 Kummer 迭代 (3.3) 都有完整精度和
明确格代价；(4.4) 还保留了实际 GM 行上的精确单位补偿。
下一步仍须控制这个补偿与其余项的相消，或构造完整高权投影的额外关系。
本篇没有由 bounded norm、首项非零或形式 lift 的选择推得主问题完成。
