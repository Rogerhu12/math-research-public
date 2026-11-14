# 全层 Witt 鬼分量、真实 CM 半线与完整整格

日期：2026-11-12。状态：全部恒等式、有限精度输入、Cartier 迭代、
首个模参数系数及两步 Frobenius 格均已证明。
没有证明新的中央非零或无穷素数结论。

固定惰性 $p\ge7$。令 $\mathcal O$ 为容纳 R66/R71 实际固定系数的
未分歧完成环；坏位 $\{2,3,5,17\}$ 均不在范围内。
$\sigma$ 表示系数 Frobenius，
$\phi_t(a)(t)=a^\sigma(t^p)$，
$\Phi(a)(t,Z)=a^\sigma(t^p,Z^p)$。
这是明确选择的局部形式 lift；并非声称存在相同公式的
特征零椭圆曲线自同源。

## 1. 保留实际单位与奇偶角色

使用 [R71](../results/R71-actual-kummer-frobenius-and-compensated-critical-jet.md)
的两个归一除法单位 $R_{\mathcal S},R_{\rm rot}\in
1+Z\mathcal O[[t,Z]]$，令 $H_{\mathcal S}=\log R_{\mathcal S}$、
$H_{\rm rot}=\log R_{\rm rot}$。设 $N=68$，准确半线为

$$
h_e=-\frac{c_e}{2N^2}(H_{\mathcal S}-iH_{\rm rot}),\qquad
h_o=-\frac{c_o}{2N^2}(H_{\mathcal S}+iH_{\rm rot}),
\tag{1.1}
$$

$$
c_e=\frac{\sqrt2\,17^{17/4}}{4800f},\qquad
c_o=\frac{i\sqrt2\,17^{7/4}}{32f},\qquad f=34(1+i).
$$

所有显示的固定标量都为当前 $p$ 的单位。原归一准确给

$$
[Z]h_e=M_e=M_1=t^4+\tfrac72t^6+\cdots,\qquad
[Z]h_o=M_o=t+\tfrac12t^3+\cdots.
\tag{1.2}
$$

对每个单位 $R$，定义真实整 Kummer 修正

$$
B_R=\frac1p\log\frac{\Phi(R)}{R^p}\in\mathcal O[[t,Z]].
$$

$B_e,B_o$ 使用与 (1.1) 相同的线性组合。
这些单位和半线均固定；以下的 $r$ 只表示鬼分量层数。

## 2. 真实单位的精确大 Witt 展开

对任意 $R\in1+Z\mathcal O[[t,Z]]$，存在唯一的整坐标
$w_n(R)\in\mathcal O[[t]]$ 使

$$
R(t,Z)=\prod_{n\ge1}(1-w_n(R)(t)Z^n)^{-1}.
\tag{2.1}
$$

这是形式 $Z$ 进乘积。证明不需除法：依次确定 $w_n$，
因为确定前 $n-1$ 个因子后，第 $n$ 次系数只由新变量 $w_n$ 以系数一改变。
因此每个 $w_n$ 都是 $R$ 的前 $n$ 个系数的整系数多项式。

对 (2.1) 取形式对数，在任意次数只有有限项参与，得到

$$
n[Z^n]\log R=\sum_{d\mid n}d\,w_d(R)^{n/d}.
$$

特别令

$$
\lambda_{R,r}=p^r[Z^{p^r}]\log R\qquad(r\ge0),
$$

则

$$
\boxed{\quad
\lambda_{R,r}=\sum_{j=0}^r p^j
 w_{p^j}(R)^{p^{r-j}}\in\mathcal O[[t]].
\quad}
\tag{2.2}
$$

所以任意精度 $p^s$ 的实际鬼分量只需有限数据

$$
\boxed{\quad
\lambda_{R,r}\equiv
 \sum_{j=0}^{\min(r,s-1)}p^j w_{p^j}(R)^{p^{r-j}}
 \pmod{p^s}.
\quad}
\tag{2.3}
$$

若还只需模参数的 $D$ 阶 jet，则每个 $w_{p^j}$ 也只读到 $t^D$；
该项只需绝对精度 $p^{s-j}$。
因此所需单位的纤维系数不超过次数
$p^{\min(r,s-1)}$。这个界独立于超过 $s-1$ 的更深鬼层，
但仍随精度 $s$ 增长；没有声称完整对象已降成固定维数。

(2.2) 对两个实际单位分别成立，再按 (1.1) 作线性组合。
不能先把 $h_e$ 当成某个未经构造的单一全局单位的对数，
也不能对其线性组合直接套一个未经定义的乘法 Witt 坐标。

## 3. 精确 Frobenius 差及惰性半线交换

由 $\Phi(R)\equiv R^p\pmod p$，$B_R$ 完整地整。
对 $r\ge1$ 取第 $Z^{p^r}$ 次系数，准确有

$$
\boxed{\quad
\lambda_{R,r}
=\phi_t(\lambda_{R,r-1})-p^r[Z^{p^r}]B_R.
\quad}
\tag{3.1}
$$

这也直接给 $\lambda_{R,r}\equiv\phi_t\lambda_{R,r-1}\pmod{p^r}$。
从 (2.2) 可独立核查：若 $x\equiv y\pmod p$，则
$x^{p^a}\equiv y^{p^a}\pmod{p^{a+1}}$；
逐项应用于 $w^p$ 与 $\phi_t(w)$，得到相同精度。
这里使用的是整的 ghost Frobenius 差，不是分别声称各个对数系数整。

定义实际半线鬼分量和 Kummer 系数

$$
\Lambda_{e,r}=p^r[Z^{p^r}]h_e,\quad
\Lambda_{o,r}=p^r[Z^{p^r}]h_o,\qquad
b_{e,r}=[Z^{p^r}]B_e,\quad b_{o,r}=[Z^{p^r}]B_o.
$$

它们全部在 $\mathcal O[[t]]$ 中。设

$$
\eta=\frac{c_e}{c_o^\sigma},\qquad
\theta=\frac{c_o}{c_e^\sigma},\qquad
A=\begin{pmatrix}0&\eta\\\theta&0\end{pmatrix}.
$$

因 $\sigma(i)=-i$，(3.1) 的准确向量形式是

$$
\boxed{\quad
\begin{pmatrix}\Lambda_{e,r}\\\Lambda_{o,r}\end{pmatrix}
=A\,\phi_t
 \begin{pmatrix}\Lambda_{e,r-1}\\\Lambda_{o,r-1}\end{pmatrix}
-p^r\begin{pmatrix}b_{e,r}\\b_{o,r}\end{pmatrix}.
\quad}
\tag{3.2}
$$

初值为 $(M_e,M_o)^t$。两步迭代因而准确等于

$$
\begin{aligned}
\begin{pmatrix}\Lambda_{e,r}\\\Lambda_{o,r}\end{pmatrix}
={}&
\begin{pmatrix}c_e/c_e^{\sigma^2}&0\\0&c_o/c_o^{\sigma^2}\end{pmatrix}
\phi_t^2
 \begin{pmatrix}\Lambda_{e,r-2}\\\Lambda_{o,r-2}\end{pmatrix}\\
&-p^{r-1}A\phi_t
 \begin{pmatrix}b_{e,r-1}\\b_{o,r-1}\end{pmatrix}
-p^r\begin{pmatrix}b_{e,r}\\b_{o,r}\end{pmatrix},
\qquad r\ge2.
\end{aligned}
\tag{3.3}
$$

所以直接得到的两步余项在 $p^{r-1}$ 中。
没有理由仅因“迭代两次”就把它改成 $p^r$ 或额外再除一个 $p$。
(3.3) 正是完整 cochain 中 $pB+\Phi(B)$ 的真实格，
与 [加权两步 Frobenius 笔记](2026-11-12-weighted-two-step-frobenius-and-kummer-iteration.md)
的归一迭代相容。

## 4. 全层模 $p$ 公式与实际 Cartier 因子

令 $\omega(t,Z)$ 为实际椭圆族的归一不变微分，
$\omega(t,0)=dZ$；写

$$
z(t,Z)=\int_0^Z\omega,\qquad
a_r(t)=p^r[Z^{p^r}]z=[Z^{p^r-1}](\omega/dZ)\in\mathcal O[[t]],
\qquad a_0=1.
\tag{4.1}
$$

记 $\mathsf H_p=a_1\bmod p$ 为该规范的 Hasse 系数。
Cartier 迭代在整个光滑家族上给

$$
\boxed{\quad
a_r\equiv
\mathsf H_p^{\,1+p+\cdots+p^{r-1}}\pmod p.
\quad}
\tag{4.2}
$$

这里没有反转 $\mathsf H_p$，所以也包括本题的 supersingular 中心。

为完整说明 (4.2)，可先把特殊纤维基域扩到其完美闭包。
genus 一曲线的正则一形式空间为一维，Cartier 算子满足
$C(\omega)=\mathsf H_p^{1/p}\omega$：
比较 $Z=0$ 处的常数系数即可核定这个标量。
迭代 $r$ 次后，标量为
$\mathsf H_p^{1/p+\cdots+1/p^r}$。
另一方面 $C^r(\omega)$ 的常数系数为 $a_r^{1/p^r}$。
取 $p^r$ 次幂即得 (4.2)，两边都在原基环中，故等式下降。

设 $\epsilon_r=e$ 当 $r$ 偶、$\epsilon_r=o$ 当 $r$ 奇，
$\eta_r=c_e/c_{\epsilon_r}^{\sigma^r}$。
从 (3.2) 模 $p$ 逐次迭代，或由 (2.2) 仅保留 $j=0$ 项，得到

$$
\Lambda_{e,r}\equiv
\eta_r\,M_{\epsilon_r}(t^{p^r})\pmod p.
\tag{4.3}
$$

因 $M_e,M_o$ 系数有理，右边无需再写它们的系数共轭；
固定归一标量的共轭仍完整保留在 $\eta_r$ 中。

现在定义真实全层“去不变微分”鬼分量

$$
W_{e,r}=p^r[Z^{p^r}](h_e-M_ez)
=\Lambda_{e,r}-a_rM_e\in\mathcal O[[t]].
$$

综合 (4.2)–(4.3) 得

$$
\boxed{\quad
W_{e,r}\equiv
\eta_rM_{\epsilon_r}(t^{p^r})
-\mathsf H_p^{\,1+p+\cdots+p^{r-1}}M_e
\pmod p.
\quad}
\tag{4.4}
$$

$r=1$ 正是 R74 的实际第一 Witt 余项；这里的式子对每层成立，
但更高层的模 $p$ 式仍由第一系数与 Cartier 迭代决定。
新的精度信息应从 (2.3)、(3.2) 的整修正读取，不能把 (4.4)
当成一组彼此独立的非零约束。

## 5. 每一全层余项的准确首个模参数系数

本题的 Hasse 系数在 CM 中心有简单零点：

$$
\mathsf H_p(t)=h_pt+O(t^3),\qquad h_p\in(\mathcal O/p)^\times.
$$

这已在
[R74](../results/R74-first-modulus-and-divided-witt-critical-projection.md)
由奇数阶 Legendre 多项式的原点导数核定。
令 $q_r=(p^r-1)/(p-1)$。由 $M_e=t^4+\cdots$，(4.4) 第二项
首次数为 $q_r+4$，首系数为 $-h_p^{q_r}$。
第一项的首次数在奇数 $r$ 时为 $p^r$，偶数 $r$ 时为 $4p^r$。
对 $p\ge7,r\ge1$，准确有 $q_r+4<p^r$，所以

$$
\boxed{\quad
\operatorname{ord}_t(W_{e,r}\bmod p)=q_r+4,\qquad
[t^{q_r+4}]W_{e,r}\equiv-h_p^{q_r}\ne0\pmod p.
\quad}
\tag{5.1}
$$

因而所有这些实际整鬼分量作为模参数函数确实非零，
并有明确的第一项。这是整个固定单位代表的结论；
不能据此断言移动中央投影也非零。
R78 已展示首层精确 GM 投影中有自动相消，而完整高权证书也始终保留
指定权的矩阵因子和系数提取。

## 6. 与完整短输入证书的准确关系

前两篇笔记已给 $m=(p+1)p^n$ 的完整测试：
$J_p'(0)\ne0$ 当且仅当某层
$p^{p^n}C_m\not\equiv0\pmod{p^{4n+4}}$。
其真实二次 GM Frobenius 输入可缩至 $O(p(n+1))$ 阶，
绝对精度 $4n+4$；$M_e$ 输入精度为 $4n+3$。

本篇补上的是，同一固定单位的任意垂直鬼层也有 (2.3) 的
有限精度模型，并有 (3.3) 的准确两步格。
这允许把真实 Hecke/isogeny norm 关系逐层代入同一个模型，
不需要虚构一个可全盘除 $p^2$ 的 Kummer 代表。

尚未证明的是：完整 Hecke trace 对应中全部分支所给的关系，
如何约束该指定中央投影，使其在无穷多个 $p$ 上非零。
单个形式 $\Phi^2$ 分支、(5.1) 的非零首项、或符号上消去第一 Hasse 因子，
都尚未支付这一步。
