# R78：准确 Wronskian 与真实 Kummer 临界相消

日期：2026-11-12。状态：下列特征零恒等式及模平方公式已证明。
完整证明见[Wronskian 与导数行](../notes/2026-11-12-exact-gm-wronskian-and-kummer-derivative-row.md)。

固定惰性 $p\ge7$，用 R68 的实际整 $U,V$，令
$s=1-4t^2$、$s_\phi=1-4t^{2p}$、$ab=-1$、$\zeta=U/V$、$B=t\zeta$。

## 1. 保留全部精度的准确投影

实际 Wronskian 为

$$
UV'-U'V=\frac1{s s_\phi}
-p^2\frac ab\frac{t^{p-1}U^2}{s_\phi}
+8p\frac{t^{2p-1}UV}{s_\phi}
+\frac ba t^{p-1}V^2.
$$

对任意整 $f=\sum f_jt^j$，R74 的真实临界投影准确等于

$$
\mathcal P_p(f)
=\frac1{p+2}[t^{p+1}]f'B^{p+2}
-\frac ba f_1
+p^2\frac ab\bigl(f_3-(p+3)f_1\bigr).
$$

令 $D=[t^{p+1}]f'B^2$、$E=[t^{p+1}]f'B^2\log B$，则

$$
\mathcal P_p(f)\equiv
\frac12D-\frac ba f_1+\frac p2E-\frac p4D\pmod{p^2}.
$$

这是带真实参考和周期权重的分部积分；不能用裸 de Rham 类替代。
其他相邻投影另有 $-\frac p2[t^p]f\zeta^2$，除 $p$ 以前不能丢弃。

## 2. 实际单位的导数行与显式单位的自动相消

选择允许的局部 lift $\phi Z=Z^p$，令 $f=[Z^p]B_e$，其中
$B_e$ 是 R71 的实际整 Kummer 修正；$h_e$ 是固定偶半线的单位对数。
则

$$
f'=\eta t^{p-1}M_o'(t^p)-[Z^p]\partial_t h_e.
$$

代入上式给出特征零完全相等的

$$
\mathcal P_p(f)=-\eta
-\frac1{p+2}[Z^pt^{p+1}](\partial_t h_e)B^{p+2}
-\frac ba f_1
+p^2\frac ab\bigl(f_3-(p+3)f_1\bigr).
$$

$\partial_t h_e$ 是固定代数对数导数，但 $Z^p$ 指标和 GM 权重仍随素数变化。
实际第二 Witt 余项满足
$E_e=-f-(b_p-H_p)M_e/p$。
所以 R74 公式中看似独立的 $-\eta$，代入真实关系后与
$-\mathcal P_p(f)$ 内的 $+\eta$ **自动相消**。
它不能充当目标非零的独立输入。

**剩余任务：** 对保留真实 GM 权重的固定代数导数证明独立的全局约束；
原 Kummer 定义式及这次分部积分本身没有增加非零信息。
