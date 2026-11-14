# R239 附录：真实局部最小能量的 4/3 下界与投影范围约束

日期：2026-11-13（UTC）。状态：已证明；无权 $N=M$ 与普通 ISP 仍开放。
完整证明见[配对纯核见证与真实范围](../notes/2026-11-13-paired-primitive-witnesses-local-minimal-energy-lower-bound-and-true-range-suppression-boundary-resume.md)。
沿用[全整数原线性窗口](R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)
及[实际完整 Gram](R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)。

## 1. 真正最小元与所有修复必须满足的链

固定原头 $m\ge5$、$d=2^m$，写
$$
A=A_m,\quad D=\sum_{j\ge m}a_jE_j,\quad a_j=(j+1)^{-2},
\quad L=A+D,\quad A^d=0.
$$
在
$$
\mathscr V_{m,q}
=\mathcal H_{\le q}^{(m)}\cap\ker(P_{\le q-1}^{(m)}L)
$$
取 $v$。真实顶部残量为
$$
r=Lv=Av_q,\qquad D^kr=(-1)^kA^{k+1}v_{q-k}.
\tag{1.1}
$$
令 $\lambda^{\rm loc}_{m,q}(v)$ 为原闭仿射集
$$
\{c\in\mathcal H_{[q+1,q+d]}^{(m)}:Lc=r,\ D^dc=0\}
$$
的最小范数。相容右逆保证其非空，故最小元存在且唯一。
对任何可行修复 $c=\sum_{t=1}^dc_t$，
$$
Dc_1=r,\quad Dc_t=-Ac_{t-1},\quad Ac_d=0,
\qquad D^tc_t=(-1)^{t-1}A^tv_q.
\tag{1.2}
$$
下文约束所有可行修复，因此并非指定右逆的粗范数下界。

## 2. 配对纯核与全部最小元的观测下界

在相邻尾位 $j,j+1$，定义一孔单位向量
$$
h_j=\frac{a_{j+1}|10\rangle-a_j|01\rangle}{(a_j^2+a_{j+1}^2)^{1/2}},
\qquad
g_j=\frac{a_j|10\rangle-a_{j+1}|01\rangle}{(a_j^2+a_{j+1}^2)^{1/2}}.
$$
对前 $2q$ 个尾位取 $q$ 对张量积，后尾取真空，得到 $h_{m,q},g_{m,q}$。
令 $J=m+2q$，则
$$
Dh_{m,q}=0,\quad D_{<J}^*g_{m,q}=0,\qquad
\rho_{m,q}=\langle h_{m,q},g_{m,q}\rangle\ge e^{-1/3}.
\tag{2.1}
$$
最后一界来自相邻权比的 $\log\cosh$ 可和缺陷。

置 $S_J=\sum_{j\ge J}a_j^2$。实际无限尾满足
$$
\frac1{3(J+1)^3}\le S_J\le\frac1{3J^3},\qquad
\|(D^*)^tg_{m,q}\|\le B_{m,q,t}:=\sqrt{t!}\,S_J^{t/2}.
\tag{2.2}
$$
这是后尾基本对称多项式 $(t!)^2e_t(a_j^2)$ 的准确计算与上界。

对一般 $v$ 定义原头观测
$$
x_g(v)=(I_{\rm head}\otimes\langle g_{m,q},\cdot\rangle)v_q.
$$
将 (1.2) 与 $y\otimes g_{m,q}$ 配对，选最佳头单位向量 $y$，
再按正交尾层求和：
$$
\boxed{\ 
\lambda^{\rm loc}_{m,q}(v)^2
\ge\sum_{t=1}^d\frac{\|A^t x_g(v)\|^2}{t!\,S_J^t}.\ }
\tag{2.3}
$$
对 $v=x\otimes h_{m,q}$、$\|x\|=1$，低方程准确成立，且
$$
\lambda^{\rm loc}_{m,q}(v)
\ge\frac{e^{-1/3}\|A^tx\|}{\sqrt{t!}\,S_J^{t/2}}.
\tag{2.4}
$$

## 3. 两个实际头中的路径下界

按二进整数编号原有限头基 $e_0,\ldots,e_{d-1}$。
真实递推给
$$
N_0^{[m]}e_n
=\left(\prod_{j<v_2(n)}\eta_j\right)e_{n-1}.
$$
两个实际头 $A_m^{(N)},A_m^{(Y)}$ 均为 $N_0^{[m]}$ 的有限多项式，
一次系数准确为1。故
$$
A_m^t e_t=(N_0^{[m]})^t e_t=\kappa_t e_0,\qquad
\kappa_t=\prod_{j\ge0}\eta_j^{\lfloor t/2^{j+1}\rfloor}.
\tag{3.1}
$$
更高幂对 $e_t$ 都为零，因此 $Y$ 型的交错符号不导致取消。

真实系数
$$
-\log\eta_j=1400\,16^j-630\,8^j+300\,2^j\le1400\,16^j
$$
给
$$
-\log\kappa_t
\le1400\sum_{j<\lfloor\log_2t\rfloor}\frac{t}{2^{j+1}}16^j
\le100t^4,
\qquad \|A_m^t e_t\|\ge e^{-100t^4}.
\tag{3.2}
$$
此处始终在原有限头内计算，没有用全空间幂范数代替。

## 4. 最小局部能量的对数阶不可降低

取原全整数选择
$$
m(q)=\max\left(5,\left\lceil\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right),
\quad d(q)=2^{m(q)},\quad
t(q)=\left\lfloor(3\log q/800)^{1/3}\right\rfloor .
$$
令单位输入 $v_q^{\rm bad}=e_{t(q)}\otimes h_{m(q),q}$。
由 (2.2)、(2.4)、(3.2)，
$$
\log\lambda^{\rm loc}(v_q^{\rm bad})
\ge-\tfrac13-100t^4+\tfrac32t\log(m+2q)
+\tfrac12t\log3-\tfrac12\log(t!).
$$
所以
$$
\liminf_q\frac{\log\lambda^{\rm loc}(v_q^{\rm bad})}{(\log q)^{4/3}}
\ge c_0:=\frac{3(3/2)^{4/3}}{4^{4/3}100^{1/3}}
=0.1747818284\ldots .
\tag{4.1}
$$
原相容候选的上界只用 (1.1)，对整个低输出单位球都成立。
若 $\Lambda_q$ 是该球上的最小修复算子范数，则
$$
c_0\le\liminf_q\frac{\log\Lambda_q}{(\log q)^{4/3}}
\le\limsup_q\frac{\log\Lambda_q}{(\log q)^{4/3}}
\le K_*:=3(16/770)^{1/3}.
\tag{4.2}
$$

**加宽到无限高尾仍不能降低该阶。**
(2.3) 只用前 $t$ 段链，不用末端 $Ac_d=0$。
把支撑改为任意 $[q+1,q+h]$、$h\ge d$，乃至 $[q+1,\infty)$，
下界 (4.1) 仍成立。$D^d$ 条件自动保留：
$t\le d$ 用 (1.1)，$t>d$ 用 $D^dc_t=(-A)^dc_{t-d}=0$。
原有限长度候选仍给无限问题的上界，故无限高尾的最小算子范数
也满足 (4.2)。这不是窗口长度造成的障碍。

## 5. 真实核投影满足更强的消灭条件

回到真实 $w\in M=\ker T$ 和原低输出投影 $v=v_{m,q}(w)$。
在合法窗 $4d\le q\le e^{d^3/4}$，令 $E_m=L-T$。
有
$$
Lw=E_mw,\quad \|E_m\|\le26\eta_{m-1},\quad
\|v-P_{\le q}^{(m)}w\|\le e^{-74d^4}\|w\|.
$$
使用真实有限恒等式
$$
A^t-(-D)^t=\sum_{j=0}^{t-1}A^{t-1-j}(-D)^j(A+D),
$$
不假设 $E_m$ 与 $A,D$ 交换，得到
$$
\|A^t x_g(v)\|
\le B_{m,q,t}\|P_{q+t}^{(m)}w\|+e^{-73d^4}\|w\|.
$$
还须支付很小的分母：(2.2) 及合法窗给
$\log B_{m,q,t}^{-1}\le d\log9+3d^4/8\le d^4/2$。
因此
$$
\boxed{\ 
\sum_{t=1}^d
\frac{\|A^t x_g(v_{m,q}(w))\|^2}{t!\,S_J^t}
\le2\tau_q(w)^2+e^{-143d^4}\|w\|^2.\ }
\tag{5.1}
$$
尾孔超过 $q$ 必使总孔超过 $q$，所以右侧是原总孔尾。

若 $v_{m(q),q}(w)=v_q^{\rm bad}$，必须
$$
\|w\|\ge\exp[(c_0-o(1))(\log q)^{4/3}].
\tag{5.2}
$$
证明用具体观测 $Z_t=\|A^t x_g(v)\|/B_{m,q,t}$ 的下界，
而非把 $\lambda\ge Z_t$ 错反成上界。
投影无解时最小原像范数为无穷；本文未声称坏输入不在真实投影的线性像。

(5.1) 控制的是一族对偶观测，不是完整 $\lambda_q(w)$ 的上界。
下一缺口是把真实全局核条件推广到压缩 Gram 的全部逆能量。
仅用低输出方程、有限核阶、相容原像或加宽修复窗口，都不能绕过 (4.2)。
