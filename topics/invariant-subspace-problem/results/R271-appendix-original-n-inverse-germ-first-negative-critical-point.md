# 原 N 头逆芽的负实临界点：12.5 首项的真实上界

Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro；2026-11-15。

本稿只讨论原 $N$ 有限头。它给原零点逆芽本身的不可移除分支点，不把其它分支的临界值当成本支的障碍。$Y$ 模型不包含在本条结论内。

原系数见[十二点五半径稿](../notes/2026-11-14-true-head-inverse-germ-twelve-half-radius-and-weighted-coefficients-789f-next.md)。取 $m\ge10$、$d=2^m$，记

$$
q_i=2^i,\quad b_i=(i+1)^{-2},\quad
d_i=e^{-\Lambda_i},\quad
\Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i,
$$

$$
F(z)=F_{N,m}(z)=\sum_{i<m}\frac{b_i}{d_i}z^{q_i},
\qquad \beta=F'(0)=d_0^{-1}=e^{20}.
$$

令 $\psi$ 为 $F(\psi(w))=w$、$\psi(0)=0$ 的原逆芽，$R_\psi$ 为其以零为中心的 Taylor 收敛半径。

## 1. 原分支上的第一个实临界点

对 $r\ge0$，

$$
F'(-r)=\beta-\sum_{i=1}^{m-1}
\frac{q_i b_i}{d_i}r^{q_i-1}.
\tag{1.1}
$$

右边从 $\beta$ 严格下降到负无穷。因此有唯一 $r_c>0$ 满足 $F'(-r_c)=0$；在 $0\le r<r_c$ 上导数为正。且

$$
F''(-r_c)=\sum_{i=1}^{m-1}
\frac{q_i(q_i-1)b_i}{d_i}r_c^{q_i-2}>0.
\tag{1.2}
$$

所以该临界点是简单的。任何复临界点 $z$ 都满足

$$
\beta\le\sum_{i=1}^{m-1}\frac{q_i b_i}{d_i}|z|^{q_i-1},
$$

故 $|z|\ge r_c$。本条半径上界实际只需负实点，不依赖这个额外最小模结论。

置 $w_c=F(-r_c)$。用 (1.1) 乘 $r_c$，

$$
w_c=-\sum_{i=1}^{m-1}
(q_i-1)\frac{b_i}{d_i}r_c^{q_i}<0.
$$

令 $q=2^{m-1}$，便有

$$
\frac{\beta r_c}{2}
\le |w_c|
\le \left(1-\frac1q\right)\beta r_c
<\beta r_c.
\tag{1.3}
$$

## 2. 临界值确实阻断原零点逆芽

当 $r$ 从 $0$ 增至 $r_c$，$F(-r)$ 严格从 $0$ 降至 $w_c$。原逆芽沿这段实轴的解析延拓准确为

$$
\psi(F(-r))=-r,\qquad 0\le r<r_c.
$$

如果原 Taylor 逆芽在一个包含 $w_c$ 的圆盘内解析，则连续性给 $\psi(w_c)=-r_c$。在该点对 $F(\psi(w))=w$ 求导，将得到

$$
F'(-r_c)\psi'(w_c)=1,
$$

与 $F'(-r_c)=0$ 矛盾。因此

$$
\boxed{R_\psi\le |w_c|<\beta r_c.}
\tag{2.1}
$$

由 (1.2)，局部反演确为二次临界产生的平方根分支；不存在把本点当可去奇点的余地。证明不假定原 Taylor 圆盘内没有更近的其它奇点；如有，只会使上界更强。

## 3. 原最高位给出的显式上界

(1.1) 的每个求和项非负，所以最高位单项给

$$
r_c\le
r_*=
\left(\frac{\beta d_{m-1}}{q\,b_{m-1}}\right)^{1/(q-1)}.
$$

从而

$$
\boxed{
R_\psi<
d_0^{-1}
\left(\frac{d_{m-1}}{d_0\,q\,b_{m-1}}\right)^{1/(q-1)}.
}
\tag{3.1}
$$

写

$$
\tau_*=-\log r_*
=\frac{\Lambda_{m-1}+\log(q/m^2)-20}{q-1}.
$$

准确多项式除法给

$$
\frac{\Lambda_{m-1}}{q-1}
=
\frac{25}{2}d^3-\frac54d^2-\frac52d
+150m-130+\frac{300m-260}{d-2}.
\tag{3.2}
$$

因此

$$
-\log R_\psi\ge
\tau_*-20
=\frac{25}{2}d^3-\frac54d^2+O(d+m).
\tag{3.3}
$$

特别，对任意固定 $c<25/2$，当 $m$ 充分大时，

$$
R_\psi<e^{-c d^3}.
$$

所以不能把已付逆芽预算中的主三次系数 $25/2=12.5$ 改成任意固定更小常数，并仍声称有同量级的完整原逆芽圆盘。次阶 $d^2$ 改进没有被排除。

原稿用 $B$ 变量圆盘半径 $\rho$ 推出 $w$ 变量半径 $\rho/(2d_0)$；这两个尺度只差固定因子。本条同样排除在保持该完整逆圆盘结论时，把 $\rho$ 的领先指数系数固定降到 $12.5$ 以下。本稿不估原来源 Schur 或固定 Green 列，也不据此关闭 $N=M$。
