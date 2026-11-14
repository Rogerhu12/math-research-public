# 普通斜率的无周期有理极限与完备单权证书

日期：2026-11-12。状态：已证明，未提供跨素数非消失。
本篇继续使用 R51 的实际 $A(z)=\sum b_mz^m$ 和 $J_p$，
不是另选单位倍数后的抽象 Iwasawa 生成元。

## 1. 陈述

取普通目标素数 $p\ge13$、$p\ne17$，设
$$
m_n=(p-1)p^n,\qquad
C_{p,n}=(m_n-1)!\,b_{m_n}\in\mathbb Q,\qquad n\ge0.
\tag{1}
$$
令 $\mathsf H_p\in\mathbb F_p^\times$ 为相对于 $dz$ 的 Hasse invariant，
$\omega(\mathsf H_p)\in\mathbb Z_p^\times$ 为其 Teichmüller lift。
则
$$
\boxed{
C_{p,n}\in p\mathbb Z_p,\qquad
C_{p,n}\equiv
\omega(\mathsf H_p)\log_p(1+p)J_p'(0)
\pmod{p^{n+2}\mathcal O_p}.
}
\tag{2}
$$
特别是，在 R51 的实际规范下，
$$
\boxed{
J_p'(0)\in\mathbb Z_p,\qquad
\omega(\mathsf H_p)\log_p(1+p)J_p'(0)
=\lim_{n\to\infty}C_{p,n}.
}
\tag{3}
$$
这里可以统一取 $\mathcal O_p=\widehat{\mathbb Z_p^{\mathrm{ur}}}$，
实际普通周期满足 $\Omega_p\in\mathcal O_p^\times$。
此环的极大理想就是 $p\mathcal O_p$；
本文所有模 $p^a$ 均指 $p^a\mathcal O_p$，不是仅在
$\mathcal O_{\mathbb C_p}$ 的极大理想意义下的约化。
由于右侧有理数的极限在 $\mathbb Q_p$ 中，(3) 的下降不是预先假定的。

进而 R40/R51 的有限性接口给出一个**完备的单权有限证书族**：
$$
\boxed{
\Sha(E_{17}/\mathbb Q)[p^\infty]\text{有限}
\ \Longleftrightarrow\
\exists n\ge0:\ v_p\bigl((m_n-1)!b_{m_n}\bigr)<n+2.
}
\tag{4}
$$
称其完备，是指只要固定 $p$ 处导数非零，总有一个有限 $n$ 检出；
不是说已经证明对无穷多个 $p$ 存在这样的 $n$。

## 2. 实际矩与其 Taylor 误差

记 $L=\log_p(1+p)$，$T_n=(1+p)^{m_n}-1$。
由真实单位测度的 single-Euler 关系，
$$
J_p(T_n)
=E_n\,\Omega_p^{m_n}\,m_n!\,b_{m_n},\qquad
E_n=1-\frac{\pi^{m_n}}{\bar\pi^{m_n+1}}.
\tag{5}
$$
我们有 $v_p(T_n)=n+1$、$v_p(m_n)=n$、$v_p(E_n-1)=m_n$。
而 $J_p\in\mathcal O_p[[T]]$ 且 $J_p(0)=0$，
所以由 (5) 先得 $v_p(C_{p,n})\ge1$。
这在后面乘以周期误差时很重要。

写 $J_p(T)=a_1T+a_2T^2+\cdots$。指数级数给
$$
\frac{T_n}{m_n}\equiv L\pmod{p^{n+2}\mathbb Z_p}.
\tag{6}
$$
确切地，其第 $k\ge2$ 项的估值为
$(k-1)n+k-v_p(k!)\ge n+2$。
另一方面，对所有 $k\ge2$，
$$
v_p\left(\frac{a_kT_n^k}{m_n}\right)
\ge k(n+1)-n\ge n+2.
$$
因此
$$
E_n\Omega_p^{m_n}C_{p,n}
\equiv L J_p'(0)\pmod{p^{n+2}\mathcal O_p}.
\tag{7}
$$

## 3. 为什么周期在这个权序列上消失

[principal 权阶梯笔记](2026-11-12-ordinary-principal-weight-ladder.md)
已以不变导子核定
$$
\Omega_p^{1-p}\equiv\mathsf H_p\pmod p.
\tag{8}
$$
故 $u=\Omega_p^{p-1}$ 的剩余属于 $\mathbb F_p^\times$，而非任意的
$\overline{\mathbb F}_p^\times$。可唯一写成
$$
u=\omega(\mathsf H_p)^{-1}(1+p\eta),\qquad
\eta\in\mathcal O_p.
$$
由 $p$-进二项式或 logarithm 估计，
$$
\Omega_p^{m_n}=u^{p^n}
\equiv\omega(\mathsf H_p)^{-1}\pmod{p^{n+1}\mathcal O_p}.
\tag{9}
$$
注意 $\omega(\mathsf H_p)^{p^n}=\omega(\mathsf H_p)$。
又因为 $C_{p,n}\in p\mathbb Z_p$，(9) 引入的乘法误差在
$p^{n+2}\mathcal O_p$ 中；$E_n-1$ 的贡献更小。
将其代入 (7)，便得到 (2)。

所以
$$
C_{p,n+1}\equiv C_{p,n}\pmod{p^{n+2}\mathbb Z_p}.
\tag{10}
$$
这些元素都属于闭子域 $\mathbb Q_p\subset\operatorname{Frac}(\mathcal O_p)$，
极限因而也在 $\mathbb Q_p$。由 (2)–(3) 得
$J_p'(0)\in\mathbb Q_p$；原有整性再给 $J_p'(0)\in\mathbb Z_p$。
没有声称整个 $J_p(T)$ 的全部系数均已降到 $\mathbb Q_p$。

## 4. 完备性、精度及中央迹版本

若某个 $n$ 满足 (4) 的右侧，则 (2) 的主项非零。
反之，若 $J_p'(0)\ne0$，令
$s=v_p(\omega(\mathsf H_p)LJ_p'(0))<\infty$。
当 $n+2>s$ 时，(2) 强制 $v_p(C_{p,n})=s<n+2$，证明 (4)。
如果导数为零，(2) 则对每个 $n$ 都给 $v_p(C_{p,n})\ge n+2$。

知道 $C_{p,n}\bmod p^{n+2}$，就知道
$$
J_p'(0)\equiv
\frac{C_{p,n}/p}
{\omega(\mathsf H_p)\bigl(\log_p(1+p)/p\bigr)}
\pmod{p^{n+1}}.
\tag{11}
$$
分母是明确的 $\mathbb Z_p$ 单位。

也可以完全用 R51 的有理中央迹：
$$
C_{p,n}^{\,2}
=\frac{((m_n-1)!)^2(8\cdot17^3)^{m_n}}{57800}\,e_{m_n}.
\tag{12}
$$
故 (4) 等价于对某个 $n$，(12) 的右端估值严格小于 $2n+4$。
实际目标素数不整除 $57800$ 或 $8\cdot17^3$。
此处不用给平方根按不同权重新选符号。

与前一篇的 Newton 证书相比，(4) 消去了所有有限精度的周期输入，
但最高权从线性级别改成了 $(p-1)p^n$。
因此它的作用是提供准确的有理极限与全精度等价式；
没有把权增长带来的计算代价隐藏起来。

## 5. 一次有理计算核查

[无周期极限脚本](../scripts/check-ordinary-hurwitz-limit.py)
直接用固定 $F,\Theta,q$ 的有理递推及 residue 换元，
不输入 $p$-进 $L$ 值或 CLS 数据。
在 $p=13$，得到
$$
C_{13,0}\equiv156\pmod{13^2},\qquad
C_{13,1}\equiv832\pmod{13^3}.
$$
第二个余数模 $13^2$ 仍为 $156$，核对 (10)。
相对于 $\mathsf H_{13}=7$ 的实际规范，(11) 给
$$
J_{13}'(0)\equiv11\pmod{13},\qquad
J_{13}'(0)\equiv37\pmod{13^2}.
$$
第一权还与已认证的 $b_{12}=9313603/50400$ 独立核对。
这些样例只检查归一化；定理的证明是 (5)–(10)。
