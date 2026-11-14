# R56. 普通中心斜率的无周期有理极限

日期：2026-11-12。**状态：完整极限、误差与有限证书已证明；跨素数非零未证明。**

## 定理

沿用 R51 的实际固定截面 $A(z)=\sum b_mz^m$ 和实际普通 Mellin 因子 $J_p$。
对普通目标素数 $p\ge13$、$p\ne17$，令
$$
m_n=(p-1)p^n,\qquad C_{p,n}=(m_n-1)!b_{m_n}\in\mathbb Q,
$$
并令 $\mathsf H_p\in\mathbb F_p^\times$ 为相对于 $dz=dx/(2y)$ 的 Hasse invariant。
其 Teichmüller lift 记为 $\omega(\mathsf H_p)$。则
$$
\boxed{
C_{p,n}\in p\mathbb Z_p,\qquad
C_{p,n}\equiv\omega(\mathsf H_p)\log_p(1+p)J_p'(0)
                  \pmod{p^{n+2}}.
}
\tag{1}
$$
这里的实际规范还满足 $J_p'(0)\in\mathbb Z_p$，且
$$
\boxed{
\omega(\mathsf H_p)\log_p(1+p)J_p'(0)=\lim_{n\to\infty}C_{p,n}.
}
\tag{2}
$$
因此
$$
\boxed{
\Sha(E_{17}/\mathbb Q)[p^\infty]\text{有限}
\iff\exists n\ge0:\ v_p(C_{p,n})<n+2.
}
\tag{3}
$$
这是每个普通 $p$ 的完备有限证书族；没有断言对无穷多个 $p$ 已存在证书。

## 证明

实际普通周期取在 $\mathcal O_p=\widehat{\mathbb Z_p^{\mathrm{ur}}}$ 中，
$\Omega_p\in\mathcal O_p^\times$。该环的极大理想为 $p\mathcal O_p$，
以下同余均使用这一离散赋值，而非仅用 $\mathcal O_{\mathbb C_p}$ 的剩余域。

置 $L=\log_p(1+p)$、$T_n=(1+p)^{m_n}-1$。
R51 的真实单 Euler 分布给
$$
J_p(T_n)=E_n\Omega_p^{m_n}m_n!b_{m_n},\qquad
E_n=1-\frac{\pi^{m_n}}{\bar\pi^{m_n+1}}.
\tag{4}
$$
已知 $J_p\in\mathcal O_p[[T]]$、$J_p(0)=0$，且
$v_pT_n=n+1$、$v_pm_n=n$、$v_p(E_n-1)=m_n$。
由 (4) 先得 $C_{p,n}\in p\mathbb Z_p$。

若 $J_p(T)=a_1T+a_2T^2+\cdots$，指数级数及整系数给
$$
\frac{T_n}{m_n}\equiv L\pmod{p^{n+2}},\qquad
\frac{J_p(T_n)}{m_n}\equiv La_1\pmod{p^{n+2}\mathcal O_p}.
\tag{5}
$$
第一式中第 $k\ge2$ 项的估值为
$(k-1)n+k-v_p(k!)\ge n+2$；
第二式的高次项估值至少 $k(n+1)-n\ge n+2$。

为确定周期方向，在实际 Amice 坐标中写
$\delta_E=\Omega_p^{-1}\Theta$、$\Theta=(1+Z)d/dZ$。
约化上 $\Theta^p=\Theta$，而 $\delta_E^p=\mathsf H_p\delta_E$，所以
$$
\Omega_p^{1-p}\equiv\mathsf H_p\pmod{p\mathcal O_p}.
$$
故存在 $\eta\in\mathcal O_p$ 使
$$
\Omega_p^{p-1}=\omega(\mathsf H_p)^{-1}(1+p\eta),\qquad
\Omega_p^{m_n}\equiv\omega(\mathsf H_p)^{-1}
                        \pmod{p^{n+1}\mathcal O_p}.
\tag{6}
$$
由于 $C_{p,n}\in p\mathbb Z_p$，用 (6) 替换 (4) 中的周期只引入
$p^{n+2}$ 误差；Euler 误差更高。(4)–(6) 给出 (1)。

于是 $C_{p,n+1}\equiv C_{p,n}\pmod{p^{n+2}}$。
闭子域 $\mathbb Q_p\subset\operatorname{Frac}(\mathcal O_p)$ 包含该有理序列的极限，
故 (1) 还证明 $J_p'(0)\in\mathbb Q_p$；其原有整性给 $J_p'(0)\in\mathbb Z_p$。
这没有假定整个 $J_p$ 已经下降到 $\mathbb Q_p$。

若某层满足 (3) 的右侧，(1) 的极限非零。
反之，若极限的有限赋值为 $s$，任何 $n+2>s$ 的层都有
$v_pC_{p,n}=s<n+2$。
最后由 R40/R51 的准确等价
$\Sha[p^\infty]\text{有限}\iff J_p'(0)\ne0$ 得 (3)。证毕。

## 明确精度、平方版本与范围

只需 $C_{p,n}\bmod p^{n+2}$，便可恢复
$$
J_p'(0)\equiv
\frac{C_{p,n}/p}{\omega(\mathsf H_p)(\log_p(1+p)/p)}
\pmod{p^{n+1}}.
$$
R51 还给一个完全不选平方根的版本：
$$
C_{p,n}^2=
\frac{((m_n-1)!)^2(8\cdot17^3)^{m_n}}{57800}\,e_{m_n}.
$$
故 (3) 等价于某层右端的赋值小于 $2n+4$。

[完整笔记](../notes/2026-11-12-ordinary-slope-period-free-hurwitz-limit.md)
与[纯有理复算脚本](../scripts/check-ordinary-hurwitz-limit.py)已根端审查。
根端运行得到 $C_{13,0}=156\bmod13^2$、$C_{13,1}=832\bmod13^3$，
从而实际 $J_{13}'(0)=37\bmod13^2$；第一项与独立认证的 $b_{12}$ 一致。
这些有限计算只核对规范，证明为上述误差估计。

本证书消去有限精度周期输入，但权 $m_n=(p-1)p^n$ 指数增长；
R55 的 Newton 证书只需线性增长的最高权。两者提供不同的准确接口，
都仍需利用固定截面的额外算术来证明跨素数非零。
