# R254 第五附录：纯尾高阶核与低孔混合方程的同时正交逼近

日期：2026-11-13（UTC）。作者：boundary。状态：已证明的中间结论；root及normal_states已全文核验带宽兼容性和真实交集预算。

本稿接续 [R254 第三附录](R254-appendix-high-order-pure-tail-kernel-constraint-without-similarity.md)的高阶纯尾约束，以及[第四附录](R254-appendix-mixed-finite-hole-right-inverse-and-equation-repair.md)的真实有限孔右逆。它不交换两个未经证明可交换的核投影，而是用伴随多项式的有限次数带宽，构造同时满足两组约束的实际向量。

## 1. 精确输入和记号

保留去掉原首位后的全部真实模型。前 $m$ 个尾位对应原物理位 $1,\ldots,m$，$d=2^m$，$m\ge2$。纯高尾删除算子为
$$
D=\sum_{j\ge m}(j+2)^{-2}E_j.
$$
记 $P_{\le q}$、$P_{>q}$ 为高尾孔次数的正交投影；它们包含有限头恒等。

实际平方符号 $P$ 与保留全部混合项的模型 $P_m$ 分别为
$$
P=A^2-\eta C,\qquad P_m=(A_m+D)^2-\eta C_m
\quad(N),
$$
$$
P=A^2-\eta C(I+A)^2,\qquad
P_m=(A_m+D)^2-\eta C_m(I+A_m+D)^2
\quad(Y).
$$
这里 $\eta=\eta_0$。$Y$ 型已乘实际有界可逆单位，所以 $\ker P$ 仍是原平方核 $K$；本稿不据此保持旧形式伴随源。

已有真实界为
$$
P_m=D^2+Q_m,\quad \|Q_m\|<\tfrac12,\quad
\|P_m\|<1,
$$
$$
Q_m=\sum_{\ell=1}^{d-1}C_m^\ell R_{\ell,m}(D),
\qquad \deg R_{\ell,m}\le2,\qquad Q_m^d=0,
\tag{1.1}
$$
$$
\|P-P_m\|\le36\eta_m,\qquad
-\log\eta_m=1400d^4-630d^3+300d.
\tag{1.2}
$$
因此 $P_m$ 在尾孔次数上只下降 $0,1,2$。

令
$$
\Pi=\text{正交投影到 }\ker D^{2d}.
$$
$D^{2d}$ 严格下降 $2d$ 次，故其核按尾孔次数分解，$\Pi$ 与各 $P_q$ 交换。没有断言 $\Pi$ 与 $D$ 或 $P_m$ 交换。

R254 第三附录给每个实际 $u\in K$ 的窗口估计
$$
\boxed{
\|P_{\le q}(I-\Pi)u\|
\le\epsilon_{m,q}\|u\|,
}
\tag{1.3}
$$
其中可取
$$
\epsilon_{m,q}
=36d\,2^{1-d}\eta_m
 18^{2d}(m+q+1)^{3d}e^{14dq}.
\tag{1.4}
$$
以下取 $q\ge2d$。另令 $\tau_q(u)$ 为去掉原首位后按全部孔次数定义的普通 Hilbert 尾。
高尾孔数超过 $q$ 必使全部孔数超过 $q$，所以
$$
\|P_{>q}u\|\le\tau_q(u).
\tag{1.5}
$$

## 2. 两个不同用途的有限多项式

首先定义原有的伴随多项式
$$
\mathcal A_m
=\sum_{k=0}^{d-1}(-Q_m)^kD^{2(d-1-k)}.
$$
由于 $Q_m$ 与 $D$ 交换，
$$
\boxed{\mathcal A_mP_m=D^{2d}.}
\tag{2.1}
$$
(1.1) 还给出本稿需要的准确带宽：
$$
\boxed{
\mathcal A_m
\text{ 在尾孔次数上只下降 }0,\ldots,2d-2.
}
\tag{2.2}
$$
确实，$Q_m^k$ 关于 $D$ 的次数至多 $2k$，再乘 $D^{2(d-1-k)}$ 后次数至多 $2d-2$。头系数只作用头，不改变尾次数。

其次用完整纯尾层上的真实二次右逆 $H$，定义
$$
\mathcal G_m
=H\sum_{k=0}^{d-1}(-Q_mH)^k.
$$
这里 $H\mathcal H_j\subseteq\mathcal H_{j+2}$、$D^2H=I$。
虽然 $H$ 未必与 $Q_m$ 交换，严格正头次数保证 $(Q_mH)^d=0$，因此
$$
\boxed{P_m\mathcal G_m=I}
\tag{2.3}
$$
于有限孔输入成立。
输入次数不超过 $s$ 时，输出不超过 $s+2d$，且
$$
\|\mathcal G_m|_{\mathcal H_{\le s}}\|\le B_{m,s},
$$
$$
\boxed{
\log B_{m,s}
=14ds+14d^2+
3d\log(m+s+2d+1)+d\log324+\log d.
}
\tag{2.4}
$$
可取 $B_{m,s}\ge1$。本稿对 $\mathcal A_m$ 与 $\mathcal G_m$ 使用不同记号：前者是有限伴随多项式，后者是真实右逆；二者不能混同。

## 3. 有限带宽将兼容性缺陷推到窗口上方

下面是核心兼容性引理。

取任意 $x\in\ker D^{2d}$，置
$$
s=q-2,\qquad r=P_{\le s}P_mx,\qquad c=\mathcal G_mr.
\tag{3.1}
$$
$r$ 是完整有限孔空间中的实际向量，所以 $c$ 有意义，且
$$
P_mc=r,\qquad c\in\mathcal H_{\le q+2d-2}.
$$

由 (2.1) 及 $D^{2d}x=0$，
$$
\mathcal A_mr
=-\mathcal A_mP_{>s}P_mx.
$$
$P_{>s}$ 的源次数至少为 $q-1$，而 (2.2) 最多降低 $2d-2$，故
$$
P_{<q-2d+1}\mathcal A_mr=0.
\tag{3.2}
$$
再由 $D^{2d}c=\mathcal A_mP_mc=\mathcal A_mr$，以及 $D^{2d}$ 的严格分级性，(3.2) 推出
$$
\boxed{P_{\le q}c\in\ker D^{2d}.}
\tag{3.3}
$$
这不是把 $\Pi$ 与 $\mathcal G_m$ 交换；它只使用了每一孔层的准确去向。

于是
$$
y=x-P_{\le q}c
\tag{3.4}
$$
仍在 $\ker D^{2d}$ 中。
$P_{>q}c$ 的源次数至少 $q+1$，而 $P_m$ 最多降低 $2$，所以
$$
P_{\le q-2}P_mP_{>q}c=0.
$$
结合 $P_mc=r$，得到
$$
\boxed{
y\in\ker D^{2d},\qquad
P_{\le q-2}P_my=0.
}
\tag{3.5}
$$
同时 $y$ 与 $x$ 在次数 $>q$ 处完全相同。

## 4. 对实际平方核向量的误差

现在取实际 $u\in K=\ker P$，并在 §3 中令 $x=\Pi u$。
低孔残量为
$$
r=P_{\le q-2}P_m\Pi u.
$$
由 (1.2)，第一项 $P_{\le q-2}P_mu$ 范数不超过 $36\eta_m\|u\|$。
由于 $P_m$ 最多降低两次，
$$
P_{\le q-2}P_m(I-\Pi)u
=P_{\le q-2}P_mP_{\le q}(I-\Pi)u.
$$
再用 $\|P_m\|<1$ 和 (1.3)，得到
$$
\boxed{
\|r\|\le(36\eta_m+\epsilon_{m,q})\|u\|.
}
\tag{4.1}
$$
未知高孔尾没有乘任何右逆常数。

构造 (3.4) 的 $y$。在低孔部分，
$$
\begin{aligned}
\|P_{\le q}(u-y)\|
&\le\|P_{\le q}(I-\Pi)u\|+\|P_{\le q}c\|\\
&\le\left[\epsilon_{m,q}
+B_{m,q-2}(36\eta_m+\epsilon_{m,q})\right]\|u\|.
\end{aligned}
$$
由 (1.4) 直接可见 $\epsilon_{m,q}\ge36\eta_m$，又 $B_{m,q-2}\ge1$，故
$$
\boxed{
\|P_{\le q}(u-y)\|
\le3B_{m,q-2}\epsilon_{m,q}\|u\|.
}
\tag{4.2}
$$
在高孔部分，$y=x=\Pi u$，所以
$$
\|P_{>q}(u-y)\|
=\|P_{>q}(I-\Pi)u\|
\le\tau_q(u).
\tag{4.3}
$$
两个部分正交，由此得到真正的同时逼近：
$$
\boxed{
\|u-y\|^2
\le\tau_q(u)^2+
9B_{m,q-2}^2\epsilon_{m,q}^2\|u\|^2.
}
\tag{4.4}
$$
其中 $y$ 同时满足 (3.5)。未知 Hilbert 尾的平方系数准确为 $1$。

## 5. 统一数值窗口

取
$$
q=25d^3,\qquad m\ge2.
$$
由 (1.4)、(2.4)，丢掉可用负项后，
$$
\begin{aligned}
\log(3B_{m,q-2}\epsilon_{m,q})
\le{}&
-700d^4+630d^3+14d^2\\
&+6d\log(m+25d^3+2d+1)
+4d\log18+\log(108d^2).
\end{aligned}
\tag{5.1}
$$
因为 $d\ge4$，
$$
m+25d^3+2d+1\le27d^3,\quad
\log27<4,\quad 4\log18<12,
$$
$$
\log(108d^2)\le4d,\qquad \log d\le d/2.
$$
所以正余量至多
$$
630d^3+23d^2+40d<200d^4.
$$
因此
$$
\boxed{
3B_{m,q-2}\epsilon_{m,q}\le e^{-500d^4}.
}
\tag{5.2}
$$
把它代入 (4.4)：
$$
\boxed{
\operatorname{dist}\!\left(
u,\ \ker D^{2d}\cap\ker(P_{\le25d^3-2}P_m)
\right)^2
\le
\tau_{25d^3}(u)^2+e^{-1000d^4}\|u\|^2.
}
\tag{5.3}
$$

## 6. 真实收缩投影及精确边界

令
$$
\mathcal V_{m,q}
=\ker D^{2d}\cap\ker(P_{\le q-2}P_m),
$$
并以 $\mathsf V_{m,q}$ 表示它的正交投影。
该空间闭，故由最佳逼近性，(4.4) 和 (5.3) 对
$y=\mathsf V_{m,q}u$ 同样成立。

还有一个准确的粗分块性质。$\ker D^{2d}$ 按尾次数分解，而低方程只依赖次数不超过 $q$ 的源，所以
$$
\mathcal V_{m,q}
=
\bigl(\mathcal V_{m,q}\cap\mathcal H_{\le q}\bigr)
\oplus
\bigl(\ker D^{2d}\cap\mathcal H_{>q}\bigr).
$$
因此
$$
[\mathsf V_{m,q},P_{\le q}]=0,\qquad
\mathsf V_{m,q}P_{>q}=\Pi P_{>q}.
\tag{6.1}
$$
这仅是与一个粗次数截断的交换；没有断言与每一单层、与 $D$ 或与 $P_m$ 交换。

若 $v$ 属于 $\mathcal V_{m,q}\cap\mathcal H_{\le q}$，则
$$
P_mv\in\ker D^{2d}\cap(\mathcal H_{q-1}\oplus\mathcal H_q).
\tag{6.2}
$$
第一项来自 $P_mD^{2d}=D^{2d}P_m$，两层支撑来自模型不升次数及低输出方程。故剩余误差准确集中在有限模块的最上两层。

本稿把 R254 第三附录的纯尾核约束与保混合项低方程合并成了真实交集逼近，不再只分别知道接近两个可能有小夹角的空间。仍未把 (6.2) 的两层边界输出消掉；$\mathcal V_{m,q}$ 不是 $\ker P_m$，更不是实际稳定像 $N$。不能据此宣布 $N=M$。下一步是支付这两层的正能量或核内原像，而不在未知高尾前重新引入条件数。
