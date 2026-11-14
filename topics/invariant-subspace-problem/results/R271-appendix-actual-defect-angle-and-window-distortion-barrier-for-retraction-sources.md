# R271 附录：实际缺陷来源的回缩角度与整窗必要失真

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2220；kernel_resume_2220 提出对有限零源差使用原实际核提升的配对。

状态：**已证明。** 对两个原实际边界的固定缺陷来源 $w\in W=M\ominus N$，原回缩左像的来源分离只需失真 $R\kappa$ 一致有界，不再要求它趋于一。更一般地，同一头的整组物理窗口若都能由这些回缩左像一致逼近同一个非零 $w$，则失真的倒平方和必须满足明确的带宽归一消失条件。

证明使用实际 $\ker L_m$ 到 $N$ 的已付提升，故本稿的加强只针对 $W$，不是对任意 $w\in H$ 的无条件加强。它允许模型保留真正高返回；不将模型源当作已来自实际 $W$，也没有证明剩余两费用比较或 $N=M$。

依赖：[原回缩左局域化](R271-appendix-retraction-left-localization-and-fixed-source-separation.md)、[原强位回缩](R271-appendix-original-tail-strong-bit-boson-retraction-and-same-source-high-schur-bound.md)、[完整远尾出生回缩](R271-appendix-shifted-primitive-retractions-and-paid-actual-source-removal.md)、[整段出生联合回缩](R271-appendix-joint-primitive-birth-window-retraction-without-count-loss.md)，以及 [R239 原线性实际核提升](R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md) §2。

## 1. 原核提升所覆盖的准确空间

固定任一实际边界 $T=T_N$ 或 $T_Y$，仍记
\[
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
\]
本稿的 $B$ 仅在这个显示式中表示原边界乘子；下文回缩截面写成 $\mathsf B$，以免混淆。

取原头 $m\ge5,d=2^m$，保持
\[
L_m=A_m+D_m,\qquad
4d\le q\le Q_m:=\lfloor e^{d^3/4}\rfloor.
\]
R239 原线性逐头提升给
\[
\Lambda_{m,q}:
\ker L_m\cap\mathcal H_{\le q}^{(m)}\longrightarrow N,
\]
\[
\boxed{\|\Lambda_{m,q}k-k\|\le\epsilon_m\|k\|,
\qquad \epsilon_m=e^{-75d^4}.}
\tag{1.1}
\]
其已证明的支持上界是 $q\le e^{d^3/3}$，因此覆盖本稿全部合法 $q$。这个结论适用于该空间的任意有限孔零源向量，不限一条指定 canonical 核。

对固定 $w\in W$，$w\perp N$，所以
\[
\boxed{|\langle w,k\rangle|
\le\epsilon_m\|w\|\,\|k\|
\quad(k\in\ker L_m\cap\mathcal H_{\le q}^{(m)}).}
\tag{1.2}
\]
这一步是本稿相对于对所有 Hilbert 向量成立的近等距分离的新增输入。没有把 $k$ 本身直接声明为实际 $N$ 中的向量。

## 2. 同源回缩最小者之差确实属于这个核

取上述任一原回缩，其分析、截面保全部原头、原核旗及完整左链方程，并满足
\[
\mathsf T\mathsf B=I,\qquad
\|\mathsf T\|\le R,\qquad \|\mathsf B\|\le\kappa,\qquad
\chi=R\kappa\ge1.
\]
令 $\mathscr E_q$ 是源截面的闭像。对任意
$r=\mathsf B\widehat r\in\mathscr E_q$，置
\[
v=E_q^\dagger r,\qquad
\widehat v=\widehat E^\dagger\widehat r,\qquad
v_0=\mathsf B_{\rm left}\widehat v .
\]
分析原真正最小者 $v$ 给模型同源可行者，故
\[
\|\widehat v\|\le R\|v\|,\qquad
\boxed{\|v_0\|\le\chi\|v\|.}
\tag{2.1}
\]
截面保完整左方程，因此 $v_0$ 与 $v$ 具有同一个原顶部源，且两者都支持于原孔层 $\le q$。于是
\[
\boxed{k=v_0-v\in\ker E_q
=\ker L_m\cap\mathcal H_{\le q}^{(m)}.}
\tag{2.2}
\]
真正最小性给 $v\perp k$，从而
\[
\boxed{\|k\|^2=\|v_0\|^2-\|v\|^2
\le(\chi^2-1)\|v\|^2.}
\tag{2.3}
\]
(2.2) 正好核对了使用 (1.1) 的源域与物理支持；没有省略一次实际 carry 提升。

原可行截面还具有精确的孔带支持。若其最小出生对应于顶部以下 $T$ 个 active 孔，则
\[
\boxed{\operatorname{supp}v_0\subseteq[q-T,q].}
\tag{2.4}
\]
具体包括：

- 原远尾真空回缩的 $q=n+s$，可取 $T=s$；
- 单个远尾出生 $b_{\rm far}$、$q=n+b_{\rm far}+t$，可取 $T=t$；
- 同一远尾联合出生 $[s-T,s-k+1]$，$q=n+s$，仍取该同一个 $T$。

这些支持都是原 $m$ 尾的物理孔数。模型左空间低于其固定出生时为零，截面逐层保孔数，故整个最小者的截面亦具有 (2.4)。不需要原真正最小者 $v$ 自身落在这个孔带。

## 3. 实际 W 对整个回缩左像的角度

记
\[
\mathscr U_{m,q}=E_q^\dagger\mathscr E_q.
\]
这是闭子空间：源像 $\mathscr E_q$ 闭，且 $E_q^\dagger$ 在源空间有界并以下界 $1/\|E_q\|$ 有界。

对任意 $v\in\mathscr U_{m,q}$，用 $v=v_0-k$、(2.4)、(1.2) 和 (2.3)，得
\[
|\langle w,v\rangle|
\le
\|P_{[q-T,q]}^{(m)}w\|\,\|v_0\|
+\epsilon_m\|w\|\,\|k\|.
\]
因此
\[
\boxed{
\|P_{\mathscr U_{m,q}}w\|
\le
\chi\|P_{[q-T,q]}^{(m)}w\|
+\epsilon_m\sqrt{\chi^2-1}\,\|w\|.
}
\tag{3.1}
\]
这是对整个原左像的角度界，允许其中所有原头自由及全部选中远尾 primitive 向量，不只测试一个源。

若 $m\to\infty$、$q-T\ge1$，且 $\sup_m\chi_m<\infty$，则
\[
\boxed{\|P_{\mathscr U_{m,q}}w\|\longrightarrow0,
\qquad
\operatorname{dist}(w,\mathscr U_{m,q})\longrightarrow\|w\|.}
\tag{3.2}
\]
证明不要求 $q-T\to\infty$：对任意固定 Hilbert 向量，
$P_{\{N_m\ge1\}}w\to0$，因为先用有限物理位向量逼近，再使尾起点越过它的支持即可。(2.4) 的带包含在 $\{N_m\ge1\}$ 中，故 (3.1) 的两项均趋零。

同样，如果一个已经合法取得的实际源族满足
$E_{q_m}^\dagger r_m\to w\ne0$，则
\[
\boxed{
\inf_{s\in\mathscr E_{q_m}}\mu_{q_m}(r_m-s)
=\operatorname{dist}(E_{q_m}^\dagger r_m,\mathscr U_{m,q_m})
\longrightarrow\|w\|.
}
\tag{3.3}
\]
任何已付 $\mu$ 小改动继续保留同一结论。

本节没有使用模型高输入为零的条件 $k\le t+1$。所以即使保留真正模型高返回，只要回缩失真有界且 (2.4) 离开尾真空层，它也不能成为固定非零实际 $W$ 来源的近似。这不排除用这些模型测试不带实际来源假设的全源形式。

## 4. 不一致失真的整窗必要条件

现在固定同一个 $m$，取任意非空有限整数切口集
\[
I_m\subseteq[4d,Q_m]\cap\mathbb Z.
\]
允许每个 $q$ 使用不同的已付回缩，记其失真与带宽为
$\chi_{m,q}\ge1$、$0\le T_{m,q}\le T_m$，并假设
\[
h_m:=\min_{q\in I_m}(q-T_{m,q})\ge1.
\tag{4.1}
\]
这些逐项回缩可以不同；本节并未把它们的源空间之和声明为一个具有统一范数的联合截面。

反设有 $v_{m,q}\in\mathscr U_{m,q}$，一致逼近同一个固定非零 $w\in W$：
\[
\sup_{q\in I_m}
\|v_{m,q}-w\|\le\rho_m\|w\|,
\qquad \rho_m\longrightarrow0.
\tag{4.2}
\]
充分大 $m$ 时 $\rho_m<1$，置
\[
a_m=\frac{1-\rho_m}{1+\rho_m}\longrightarrow1.
\]
由 (4.2)，
\[
\frac{|\langle w,v_{m,q}\rangle|}
{\|w\|\|v_{m,q}\|}
\ge a_m.
\tag{4.3}
\]
将 (3.1) 的逐向量版本除以 $\chi_{m,q}\|w\|$，并用
$\sqrt{\chi^2-1}/\chi\le1$，得到
\[
\boxed{
\frac{a_m}{\chi_{m,q}}
\le
\frac{\|P_{[q-T_{m,q},q]}^{(m)}w\|}{\|w\|}
+\epsilon_m.
}
\tag{4.4}
\]
先除失真再求和，因而不需要另加
$\epsilon_m\sup_q\chi_{m,q}\to0$。

各整数孔层至多进入 $T_m+1$ 个这样的带；所有带均在孔数 $\ge h_m$ 中。对 (4.4) 用有限序列的 Minkowski 不等式，得
\[
\boxed{
a_m\left(\sum_{q\in I_m}\chi_{m,q}^{-2}\right)^{1/2}
\le
\sqrt{T_m+1}\,
\frac{\|P_{\{N_m\ge h_m\}}w\|}{\|w\|}
+\epsilon_m\sqrt{|I_m|}.
}
\tag{4.5}
\]
这是实际原带支持及原核提升给出的准确预算，不是假设这些模型像彼此正交。

由于 $|I_m|\le Q_m+1$，原提升误差满足
\[
\epsilon_m\sqrt{|I_m|}
\le e^{-75d^4}\sqrt{e^{d^3/4}+1}\longrightarrow0.
\]
同时 (4.1) 及有限位逼近给
$\|P_{\{N_m\ge h_m\}}w\|\to0$。故 (4.5) 推出必要条件
\[
\boxed{
\frac1{T_m+1}\sum_{q\in I_m}\chi_{m,q}^{-2}
\longrightarrow0.
}
\tag{4.6}
\]

特别，若在一条无穷头子序列上有
\[
\boxed{
\sup_{q\in I_m}\chi_{m,q}^2
\le C\,\frac{|I_m|}{T_m+1}
}
\tag{4.7}
\]
且 $C$ 为固定常数，则 (4.6) 的左边至少为 $1/C$，矛盾。因而这种整族不能满足 (4.2)。若 $|I_m|\asymp Q_m$，即得到
$\chi^2=O(Q_m/(T_m+1))$ 仍不足以支持整组实际来源逼近的结论。

(4.7) 只是排除一个特定的回缩来源运输路线，不是原完整右费或实际高返回的下界；$\chi$ 是已选原分析/截面的失真参数。没有从失真大反推它的每个源都具有巨大真正最小费。

## 5. 与已付删除及相容整流的关系

原两费用投影删除和[不交窗顶部投影](R271-appendix-disjoint-window-top-projection-and-coherent-source-flow-removal.md)都保持实际左像趋于同一个 $w$。因此它们的残源同样受 (3.3)、(4.6) 的限制：不能把残源未经新费用就替换为上述移动模型像中的向量。

这与用回缩像作为廉价删除空间完全相容。删除项的左像已经由实际两费用证明趋零；本稿进一步表明，有限失真的这些像相对于固定 $W$ 本就具有趋零角度。真正非零来源留在准确余图中，而不是留在被删除的模型像里。

与此前来源分离的适用范围作准确区分：

- 对任意固定 $w\in H$，此前结论使用 $\chi\to1$，不需要实际 $W$；
- 对固定 $w\in W$，本稿用实际核提升将条件放宽为 $\chi$ 一致有界；
- 对逐窗不一致、可增长的 $\chi_{m,q}$，本稿给出 (4.5)–(4.6) 的带宽归一必要条件；
- 孔带包含尾真空层、无法支付原核提升的窗口、未证保原旗的模型均不在本稿范围内。

普通 ISP、实际边界 $N=M$、原高修复及其准确余源比较继续开放。
