# R249附录：真实跨头进位的直接相似预算

日期：2026-11-13（UTC+8）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：已证明，中间结论。

本文在 [R249](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) 的同一个实际平衡相似 $S_m$ 下，直接计算跨头进位的方向，而不使用一般不等式 $\|S_m^{-1}KS_m\|\le\kappa_m\|K\|$。对两个真实慢边界符号，全部局部变换误差仍有主指数 $-(175/2)d^4$，$d=2^m$。结合能量配对外部的一个 $\kappa_m$ 后，实际剩余主指数为 $-245d^4/3$。这是实际算子预算；没有证明 $N=M$。

## 1. 沿用 R249 的明确平衡矩阵

取 $m\ge2$、$d=2^m$，记
$$
\Lambda_j=-\log d_j
=100\,16^j-105\,8^j+(150j+25)2^j,\qquad
\omega_n=-\log W_n.
$$
令
$$
L=100\frac{(d/2)^4}{d/2-1},\qquad
\rho=e^{-L},\qquad
F(n)=Ln-\omega_n.
$$
R249 已证明 $F(n)$ 在 $0\le n<d$ 上非负且最大值为
$$
F_*:=F(d-1)=L(d-1)-\omega_{d-1}.
$$
令 $\widetilde g$ 为缩放后有限芽、$\widetilde h$ 为其模 $z^d$ 的复合逆。精确相似为
$$
S_m=E_mU_m,\qquad
E_m=\operatorname{diag}(e^{-F(n)}),\qquad
U_m=C_{\widetilde h}^{\top},
$$
$$
T_m=S_m(e^{20-L}J_d)S_m^{-1}.
$$
这里
$$
U_m^{-1}=C_{\widetilde g}^{\top},\qquad
\|U_m\|\le d6^d,\qquad \|U_m^{-1}\|\le d2^d.
\tag{1.1}
$$
定义便于使用的正数
$$
Q_d=d^2\,12^d,\qquad
\zeta_m=\Lambda_m-Ld,\qquad
u_m=d6^d e^{20-L},\qquad
v_m=Q_de^{-\zeta_m}.
\tag{1.2}
$$
R249 的条件数界是 $\kappa_m\le Q_de^{F_*}$。

所有 $S_m,E_m,U_m$ 下文均在高位尾上张量恒等作用。不同模型的换元矩阵可以不同，但上述明确预算统一适用。

## 2. 真正的跨头进位是一个确定方向的矩阵

固定 $i<m$，记 $s=2^i$。定义头上的部分等距
$$
V_i^{(m)}e_r=e_{d-s+r}\quad(0\le r<s),\qquad
V_i^{(m)}e_r=0\quad(s\le r<d).
$$
它把低头段 $[0,s-1]$ 送到高头段 $[d-s,d-1]$。

将 $\mathcal N_m$ 记为 $N_m$ 在第 $m$ 位及以后尾空间上的算子，故 $\|\mathcal N_m\|=1$。真实加权减法给准确恒等式
$$
\boxed{
N_i=N_i^{[m]}\otimes I+
\frac{\alpha_m}{\alpha_i}\,
V_i^{(m)}\otimes\mathcal N_m.
}
\tag{2.1}
$$
证明：输入低头余数 $r\ge s$ 时，减去 $s$ 不跨头，得到真实有限头 $N_i^{[m]}$；若 $r<s$，第 $i$ 位至第 $m-1$ 位全空，必须从高位尾借一。若尾整数的最低孔在其第 $\ell$ 位，真实系数是
$$
\alpha_{m+\ell}/\alpha_i
=(\alpha_m/\alpha_i)(\alpha_{m+\ell}/\alpha_m),
$$
低头输出为 $d-s+r$，后一个系数正是 $\mathcal N_m$ 的尾权。这付清 (2.1) 的全部基向量及实际 carry。

因为 $F$ 按 bits 加性，两个对应低头的差为
$$
F(d-s+r)-F(r)
=F(d-1)-F(s-1).
$$
所以
$$
\boxed{
E_m^{-1}V_i^{(m)}E_m
=e^{F(d-1)-F(s-1)}V_i^{(m)}.
}
\tag{2.2}
$$
它不是一个任意局部矩阵的条件数上界，而是精确的方向性系数。

此外，
$$
-\log(\alpha_m/\alpha_i)
=\Lambda_m-\Lambda_i-\omega_{d-1}+\omega_{s-1}.
$$
结合 (2.2)，
$$
\frac{\alpha_m}{\alpha_i}
e^{F(d-1)-F(s-1)}
=\exp[-\Lambda_m+\Lambda_i+L(d-s)]
\le e^{-\zeta_m},
\tag{2.3}
$$
最后用 $\Lambda_i\le Ls$。由 (1.1)、(2.1)，得到
$$
\boxed{
\|S_m^{-1}(N_i-N_i^{[m]}\otimes I)S_m\|
\le v_m\qquad(i<m).
}
\tag{2.4}
$$
这里没有额外乘 $\kappa_m$。

## 3. 变换后的低位 $N_i$ 确实很小，支付全部 Cayley 逆

相似的有限芽逆给
$$
S_m^{-1}B_mS_m=\rho\,\widetilde h(J_d).
\tag{3.1}
$$
因此
$$
S_m^{-1}N_i^{[m]}S_m
=\frac{\rho^s}{d_i}\widetilde h(J_d)^s.
$$
R249 的 Lagrange 系数预算对每个 $s<d$ 的整个多项式 $\widetilde h(z)^s\bmod z^d$ 都成立，每个系数绝对值至多 $6^d$。于是
$$
\|\widetilde h(J_d)^s\|\le d6^d.
$$
对 $i\ge1$，R249 系数界实际给 $\Lambda_i\le L(s-1)$；$i=0$ 时 $\Lambda_0=20$。故统一有
$$
\boxed{\|S_m^{-1}N_i^{[m]}S_m\|\le u_m\qquad(i<m).}
\tag{3.2}
$$
由 (2.4)，完整真实算子也满足
$$
\boxed{\|S_m^{-1}N_iS_m\|\le u_m+v_m.}
\tag{3.3}
$$

下面确认这些界足够进入实际 Neumann 逆，不能只把它称为“小”。对 $d\ge4$，
$$
L\ge\frac{25}{2}d^3,\qquad
\log(d6^d)+20\le8d\le L/2,
$$
所以 $u_m\le e^{-L/2}$。又
$$
\Lambda_m\ge100d^4-105d^3,\qquad Ld\le25d^4,
$$
故
$$
\zeta_m\ge75d^4-105d^3\ge\frac{195}{4}d^4.
$$
因 $\log Q_d<5d\le d^4$，
$$
v_m\le e^{-(191/4)d^4}.
$$
特别，全部 $m\ge2$ 均有
$$
u_m+2v_m<1/4.
\tag{3.4}
$$

于是变换后的完整 $N_i$ 和有限头 $N_i^{[m]}$ 的 $I+$ 逆范数都小于 $2$。用真实逆差恒等式，
$$
\boxed{
\|S_m^{-1}(Y_i-Y_i^{[m]}\otimes I)S_m\|
\le4v_m\qquad(i<m).
}
\tag{3.5}
$$
这里的逆界来自 (3.2)–(3.4)，没有使用旧的 $3\kappa_m$ 预算。因而 $Y$ 模型也没有暗中恢复被省掉的条件数。

## 4. 任意更大局部截断在同一个 $S_m$ 下的误差

固定 $\ell\ge m$。对 $i<m$，将 (2.1) 的头边界移到第 $\ell$ 位，跨头部分在前 $m$ 位仍为同一个 $V_i^{(m)}$；在第 $m$ 位至第 $\ell-1$ 位之间额外把全部空位改成孔，其部分等距范数为 $1$。真实系数相较第 $m$ 位边界再乘 $\alpha_\ell/\alpha_m$。所以
$$
\boxed{
\|S_m^{-1}(N_i-N_i^{[\ell]}\otimes I)S_m\|
\le v_m\frac{\alpha_\ell}{\alpha_m}
\qquad(i<m).
}
\tag{4.1}
$$
这还给
$$
\|S_m^{-1}N_i^{[\ell]}S_m\|
\le u_m+2v_m<1/4.
$$
因此变换后的这一个更大有限头的 $I+$ 逆也小于 $2$，并且
$$
\boxed{
\|S_m^{-1}(Y_i-Y_i^{[\ell]}\otimes I)S_m\|
\le4v_m\frac{\alpha_\ell}{\alpha_m}.
}
\tag{4.2}
$$
这一步逐个确认了更大截断的实际逆，未把 $S_\ell$ 和 $S_m$ 混用。

若 $m\le i<\ell$，相应算子完全作用在 $S_m$ 的尾上，故与 $S_m$ 交换。于是原真实有限链误差和逆界 $3$ 原样成立，不产生条件数。

令
$$
\mathcal E_\ell^{(m)}
=S_m^{-1}(T-T^{[\ell]})S_m.
$$
将 $i<m$、$m\le i<\ell$、$i\ge\ell$ 三段分别求和，使用 $\sum_i a_i<2$，得到对两模型统一的界
$$
\boxed{
\|\mathcal E_\ell^{(m)}\|
\le8v_m\frac{\alpha_\ell}{\alpha_m}
+26\eta_{\ell-1}.
}
\tag{4.3}
$$
其中第二项支付中间真实头及高位真／纯差；在 $\ell=m$ 时它仍是合法的宽松上界。

## 5. 全部变换后局部 carry 的加权和

令 $K_\ell=T^{[\ell+1]}-T^{[\ell]}$，并记
$$
\widehat K_\ell^{(m)}=S_m^{-1}K_\ell S_m.
$$
由 (4.3) 对 $\ell$ 与 $\ell+1$ 相减，
$$
\|\widehat K_\ell^{(m)}\|
\le16v_m\frac{\alpha_\ell}{\alpha_m}+52\eta_{\ell-1}.
\tag{5.1}
$$

利用真实恒等式 $\eta_{m-1}=d_m/d_{m-1}^2$，
$$
-\log\eta_{m-1}=\Lambda_m-2\Lambda_{m-1}.
$$
又 $2\Lambda_{m-1}\le Ld$，故 $\zeta_m\le-\log\eta_{m-1}$，从而 $v_m\ge\eta_{m-1}$。
对 $\ell\ge m$ 还有
$$
\frac{\alpha_\ell}{\alpha_m}\le
\frac{\eta_{\ell-1}}{\eta_{m-1}};
$$
$\ell=m$ 时两边等于 $1$，$\ell>m$ 时由 $\alpha_\ell/\alpha_m=\prod_{j=m}^{\ell-1}\eta_j$ 立即得到。因此
$$
\boxed{
\|\widehat K_\ell^{(m)}\|
\le68\frac{v_m}{\eta_{m-1}}\eta_{\ell-1}.
}
\tag{5.2}
$$

精确 $\eta$ 指数满足 $\eta_{m+t-1}\le\eta_{m-1}^{16^t}$。对任意固定 $a\ge0$，记
$$
C_a=\sum_{t\ge0}e^{at-1070(16^t-1)}<\infty.
$$
于是
$$
\boxed{
\sum_{\ell\ge m}e^{a(\ell-m)}
 \|\widehat K_\ell^{(m)}\|
\le68C_a\,v_m.
}
\tag{5.3}
$$
这同时控制所有局部输出次数可能支付的固定指数损失。

由 (1.2)，
$$
\log v_m=-\zeta_m+\log Q_d
=-\frac{175}{2}d^4+O(d^3+m d).
\tag{5.4}
$$
因此变换后误差仍保持真实的 $175/2$ 主衰减率，优于先乘一个一般条件数得到的预算。

## 6. 再支付能量配对外部的一个条件数

由 R249 的 $\kappa_m\le Q_de^{F_*}$，
$$
\kappa_m v_m\le e^{-\Theta_m},
$$
其中
$$
\Theta_m=\zeta_m-F_*-2\log Q_d
=\Lambda_m+\omega_{d-1}-L(2d-1)-2d\log12-4\log d.
$$
代入精确权，得到
$$
\boxed{
\begin{aligned}
\Theta_m={}&\frac{245}{3}d^4-120d^3
-\frac{75}{2}\frac{d^4}{d-2}\\
&+(300m-250-2\log12)d+\frac{850}{3}-4\log d.
\end{aligned}
}
\tag{6.1}
$$
所以
$$
\boxed{
\kappa_m\sum_{\ell\ge m}e^{a(\ell-m)}
 \|\widehat K_\ell^{(m)}\|
\le68C_a e^{-\Theta_m},
\qquad
\Theta_m=\frac{245}{3}d^4+O(d^3+m d).
}
\tag{6.2}
$$
还可给全部 $m\ge2$ 的统一粗余量：在 (6.1) 中最后一行非负，因 $2\log12<5$、$4\log d<3m$。于是
$$
\frac{\Theta_m}{d^4}
\ge\frac{245}{3}-\frac{120}{d}-\frac{75}{2(d-2)}
\ge\frac{395}{12}>32,
$$
即
$$
\boxed{
\kappa_m\sum_{\ell\ge m}e^{a(\ell-m)}
 \|\widehat K_\ell^{(m)}\|
\le68C_a e^{-32d^4}.
}
\tag{6.3}
$$
固定的 $e^{O(d)}$ 或 $d$ 的多项式因子不改变 $245/3$ 的主余量。

## 7. 代入实际移动头通量后的两个必要尾率

记 $M=\ker T$、$N=\overline{BM}$、$W=M\ominus N$，固定 $0\ne w\in W$，并令
$$
\tau_q=\|\mathsf P_{>q}w\|,\qquad c_*=2+2\log(3/2).
$$
这里 $\mathsf P_{>q}$ 是原物理孔次数尾投影。由 [R239指数附录](R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md)，每个 $c>c_*$ 都有规范形式原像 $h$，其完整孔层属于 Hilbert 空间，且
$$
T^*h=w,\qquad \|h_q\|\le H e^{c(q+1)},\qquad H=C_c\|w\|.
\tag{7.1}
$$
只按已证明的层展开使用这个方程，不把 $h$ 当成全空间 Hilbert 向量。

沿用 [移动头通量附录](R249-appendix-moving-head-energy-flux-and-defect-tail-rates.md) 的两个不同变换
$$
k=S_m^*h,\qquad y=S_m^{-1}w,\qquad G=S_m^*S_m.
$$
头链位置加尾孔数给新的分级。$\widehat K_\ell^{(m)}$ 只改变前 $\ell+1$ 位，而其前 $m$ 位链位置至多改变 $d-1$，所以新次数带宽仍至多
$$
b_{m,\ell}=d+\ell-m.
\tag{7.2}
$$
这条局部支撑性质没有因改进范数界而消失。

原附录的有限层错位恒等式和正度量尾项估计原样成立。只需在其逐项求和处直接使用本稿的 $\|\widehat K_\ell^{(m)}\|$，得到对 $n\ge d-1$
$$
\begin{aligned}
\|w\|^2\le{}&
 \kappa_m\tau_{n-d+1}^2\\
&+2H\|w\|\kappa_m\sqrt{d(m+1)}
 e^{c(n+m+1)}\,\Xi_m(c),
\end{aligned}
\tag{7.3}
$$
其中
$$
\Xi_m(c)=\sum_{\ell\ge m}
 \|\widehat K_\ell^{(m)}\|
 \sqrt{2b_{m,\ell}+1}\,e^{c b_{m,\ell}}.
\tag{7.4}
$$
保留下来的外层 $\kappa_m$ 来自 $k=S_m^*h$ 与 $y=S_m^{-1}w$ 的相反变换。正能量尾项也仍支付 $\kappa_m$。没有把两者省去；只是不再用 $\kappa_m\|K_\ell\|$ 估计已经准确计算的变换后 carry。

写 $t=\ell-m$，利用 $\sqrt{2(d+t)+1}\le\sqrt{2d+1}\,e^t$，(5.3) 给
$$
\boxed{
\Xi_m(c)\le68C_{c+1}\sqrt{2d+1}\,e^{cd}v_m.
}
\tag{7.5}
$$
它同时证明 (7.3) 中每个固定 $m,n$ 的全部局部项绝对可和，亦支付了 $b_{m,\ell}>n$ 时的完整有限窗。故仍符合原附录的形式方程使用约定。

归一化 $\|w\|=1$。置
$$
A=\frac{35}{6},\qquad B=\frac{175}{2},\qquad
B-A=\frac{245}{3}.
$$
由 R249 和 (5.4)，
$$
\log\kappa_m\le(A+o(1))d^4,\qquad
\log v_m=-(B+o(1))d^4.
$$
固定 $0<\lambda<(B-A)/c$，取
$$
n_m=\lfloor\lambda d^4\rfloor,\qquad q_m=n_m-d+1.
$$
(7.3) 的第二项由 (7.5) 至多为
$$
\exp\bigl((A+c\lambda-B+o(1))d^4\bigr)\longrightarrow0.
$$
因此
$$
\tau_{q_m}^2\ge(1-o(1))\kappa_m^{-1},\qquad
-\log\tau_{q_m}\le\left(\frac A2+o(1)\right)d^4.
\tag{7.6}
$$
这些尾均非零；若某个尾为零，后续所有尾也为零，与 (7.6) 矛盾。

由 $q_m/d^4\to\lambda$，再令 $\lambda\uparrow(B-A)/c$，得到
$$
\liminf_{q\to\infty}\frac{-\log\tau_q}{q}
\le\frac{Ac}{2(B-A)}=\frac c{28}.
\tag{7.7}
$$
子列界不能直接升级为全序列界。准确地 $q_{m+1}/q_m\to16$。若 $q_m\le q<q_{m+1}$，单调性给 $\tau_q\ge\tau_{q_{m+1}}$，归一化后 $-\log\tau_q\ge0$，故
$$
\frac{-\log\tau_q}{q}
\le\frac{-\log\tau_{q_{m+1}}}{q_m}.
$$
结合 (7.6)，再令 $\lambda$ 趋上端，得到
$$
\limsup_{q\to\infty}\frac{-\log\tau_q}{q}
\le\frac{16Ac}{2(B-A)}=\frac{4c}{7}.
\tag{7.8}
$$
(7.7)、(7.8) 对每个固定 $c>c_*$ 成立；令 $c\downarrow c_*$ 无需端点右逆常数一致。恢复未归一化向量只改变对数中的常数。因此最终有
$$
\boxed{
\liminf_{q\to\infty}\frac{-\log\tau_q}{q}\le\frac{c_*}{28},
\qquad
\limsup_{q\to\infty}\frac{-\log\tau_q}{q}\le\frac{4c_*}{7}.
}
\tag{7.9}
$$

## 8. 使用范围

本文省掉的是对实际 carry 作头相似时的一次一般条件数损失。关键输入是跨头部分等距的确定方向，以及变换后低位 $N_i$ 的实际小范数；两个 Cayley 逆均由这个小范数重新证明。

移动头能量的正度量截断仍有未知核向量的尾范数项。(7.9) 是非零缺陷必须满足的慢尾条件，一般 Hilbert 向量的多项式尾与之相容。尚未证明 $\kappa_m\tau_{q_m}^2\to0$ 或反能量尾级数发散，因此 $N=M$、其反面以及普通 ISP 均未由本附录决定。

