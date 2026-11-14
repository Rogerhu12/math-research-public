# 配对纯核见证、局部最小修复的 4/3 下界与真实投影范围的消灭条件

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：以下全部不等式已证明；原无权 $N=M$ 和普通 ISP 仍开放。

本稿承接[全整数原线性窗口](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)与[实际修复 Gram](../results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)。新的下界针对闭仿射集中的**真正最小范数**，并非某个预先指定的相容右逆。但坏输入只属于低输出精确核，尚未宣称来自一个有统一范数控制的真实 $w\in M$。最后一节恰好证明真实投影范围对这些坏方向有额外的定量消灭条件。

## 1. 局部最小能量及链式必要条件

固定原头长 $m\ge5$、$d=2^m$，写
$$
A=A_m,\quad D=\sum_{j\ge m}a_jE_j,\quad
a_j=(j+1)^{-2},\quad L=A+D.
$$
$A^d=0$、$\|A\|\le6$，$A,D$ 交换。令
$$
\mathscr V_{m,q}
=\mathcal H_{\le q}^{(m)}
 \cap\ker(P_{\le q-1}^{(m)}L).
$$
对任意 $v\in\mathscr V_{m,q}$，其顶部残量为
$$
r=Lv=A v_q,\qquad
D^kr=(-1)^kA^{k+1}v_{q-k}.
\tag{1.1}
$$
相容 $R_t$ 有限和保证下述闭仿射集非空：
$$
\mathscr C_{m,q}(v)=
\{c\in\mathcal H_{[q+1,q+d]}^{(m)}:
 Lc=r,\ D^dc=0\}.
$$
记其唯一最小元范数为 $\lambda^{\rm loc}_{m,q}(v)$。当
$v=v_{m,q}(w)$ 是原稿的真实低方程投影时，这就是原 $\lambda_{m,q}(w)$。

把任意可行修复分成 $c=\sum_{t=1}^dc_t$，其中 $c_t$ 在第 $q+t$ 尾孔层。它满足
$$
Dc_1=r,\qquad Dc_t=-Ac_{t-1}\ (2\le t\le d),
\qquad Ac_d=0.
$$
所以
$$
\boxed{
D^tc_t=(-1)^{t-1}A^t v_q\qquad(1\le t\le d).
}
\tag{1.2}
$$
以下下界对每一个可行 $c$ 成立，因此也对真正最小元成立。

## 2. 相邻两位构造的一对纯核向量

令 $J=m+2q$。对每对相邻尾位
$j=m+2i,\ j+1$（$0\le i<q$），在一孔层定义单位向量
$$
h_i=\frac{a_{j+1}|10\rangle-a_j|01\rangle}
          {\sqrt{a_j^2+a_{j+1}^2}},\qquad
g_i=\frac{a_j|10\rangle-a_{j+1}|01\rangle}
          {\sqrt{a_j^2+a_{j+1}^2}}.
$$
直接计算给
$$
(a_jE_j+a_{j+1}E_{j+1})h_i=0,\qquad
(a_jE_j^*+a_{j+1}E_{j+1}^*)g_i=0.
$$
在 $m,\ldots,J-1$ 上取张量积，其后全取真空：
$$
h_{m,q}=\bigotimes_{i<q}h_i,\qquad
g_{m,q}=\bigotimes_{i<q}g_i.
$$
二者均为单位 $q$ 孔向量。写 $D_{<J}=\sum_{m\le j<J}a_jE_j$，
则
$$
Dh_{m,q}=0,\qquad D_{<J}^*g_{m,q}=0.
\tag{2.1}
$$

其内积有统一正下界：
$$
\rho_{m,q}:=\langle h_{m,q},g_{m,q}\rangle
=\prod_{i<q}\frac{2a_{m+2i}a_{m+2i+1}}
 {a_{m+2i}^2+a_{m+2i+1}^2}
\ge e^{-1/3}.
\tag{2.2}
$$
证明：每个因子等于 $\operatorname{sech}\delta_i$，其中
$\delta_i=2\log(1+(m+2i+1)^{-1})\le2/(m+2i+1)$。
由 $\log\cosh x\le x^2/2$，
$$
-\log\rho_{m,q}
\le2\sum_{i\ge0}(m+2i+1)^{-2}
\le\frac1{m+1}+\frac2{(m+1)^2}
\le\frac2{m+1}\le\frac13.
$$

置
$$
S_J=\sum_{j\ge J}a_j^2.
$$
单调积分比较给
$$
\frac1{3(J+1)^3}\le S_J\le\frac1{3J^3}.
\tag{2.3}
$$
由于前缀创建算子杀死 $g_{m,q}$，且与后尾创建交换，
$$
(D^*)^t g_{m,q}
=g_{m,q}\otimes
 \left(\sum_{j\ge J}a_jE_j^*\right)^t\Omega.
$$
右边后尾向量的范数平方为
$(t!)^2e_t((a_j^2)_{j\ge J})$。用
$t!e_t((a_j^2))\le(\sum a_j^2)^t$，得到
$$
\boxed{
\|(D^*)^tg_{m,q}\|
\le B_{m,q,t}:=\sqrt{t!}\,S_J^{t/2}.
}
\tag{2.4}
$$
这些都是实际无限尾算子的等式或界，没有把有限位置模型当成完整孔层。

## 3. 对真正最小能量的头部观测下界

对一般 $v\in\mathscr V_{m,q}$ 定义一个原头向量
$$
x_g(v)=(I_{\rm head}\otimes\langle g_{m,q},\cdot\rangle)v_q.
$$
由 (1.2)，对任意头单位向量 $y$，
$$
\langle c_t,y\otimes(D^*)^tg_{m,q}\rangle
=(-1)^{t-1}\langle A^t x_g(v),y\rangle.
$$
取 $y$ 为相应头方向，使用 (2.4)，再把互相正交的 $c_t$ 范数平方相加：
$$
\boxed{
\lambda^{\rm loc}_{m,q}(v)^2
\ge
\sum_{t=1}^{d}
 \frac{\|A^t x_g(v)\|^2}{t!\,S_J^t}.
}
\tag{3.1}
$$
$t=d$ 项准确为零，可以保留。

特别地，对任意头单位向量 $x$，
$$
v=x\otimes h_{m,q}\in\mathscr V_{m,q},
\quad \|v\|=1,\quad x_g(v)=\rho_{m,q}x,
$$
因此
$$
\boxed{
\lambda^{\rm loc}_{m,q}(x\otimes h_{m,q})
\ge
\frac{e^{-1/3}\|A^t x\|}
 {\sqrt{t!}\,S_J^{t/2}}
\quad(1\le t<d).
}
\tag{3.2}
$$
这类 $v$ 只在第 $q$ 层非零，$Dv=0$，所以低方程和 (1.1) 的所有高阶恒等式均准确成立。修复集仍满足原 $D^d$ 条件，未通过放宽约束制造坏例。

## 4. 两个实际有限头的直接路径下界

在原 $m$ 位头上，以二进整数 $0,\ldots,d-1$ 编号标准基 $e_n$。
原递推
$$
N_j^{[m]}=E_j+\eta_jE_j^*N_{j+1}^{[m]}
$$
给
$$
N_0^{[m]}e_n
=\left(\prod_{j<v_2(n)}\eta_j\right)e_{n-1}
\quad(1\le n<d).
\tag{4.1}
$$
这里 $v_2(n)$ 是 $n$ 的二进赋值，空积为1。该路径全部位于原有限头内。

此外 $(N_j^{[m]})^2=\eta_jN_{j+1}^{[m]}$；归纳可知每个 $N_j^{[m]}$ 都是 $N_0^{[m]}$ 的常数倍 $2^j$ 次幂。因此
$$
A_m^{(N)}=\sum_{j<m}(j+1)^{-2}N_j^{[m]}
$$
以及
$$
A_m^{(Y)}
=\sum_{j<m}(j+1)^{-2}
 N_j^{[m]}(I+N_j^{[m]})^{-1}
$$
都是 $N_0^{[m]}$ 的有限真多项式，且一次系数准确为 $b_0=1$。
故对任意整数 $1\le t<d$，
$$
\boxed{
A_m^t e_t=(N_0^{[m]})^t e_t
=\kappa_t e_0,\qquad
\kappa_t=\prod_{j\ge0}
 \eta_j^{\lfloor t/2^{j+1}\rfloor}.
}
\tag{4.2}
$$
理由是 $A_m^t$ 的首个非零幂为 $(N_0^{[m]})^t$，系数1；所有更高次幂作用于 $e_t$ 都准确为零。这同时处理两型 $Y$ 中的交错符号，没有用全空间范数下界替代有限头证明。

实际物理系数满足
$$
-\log\eta_j
=1400\,16^j-630\,8^j+300\,2^j
\le1400\,16^j.
$$
令 $k=\lfloor\log_2t\rfloor$。于是
$$
\begin{aligned}
-\log\kappa_t
&\le1400\sum_{j=0}^{k-1}
 \frac{t}{2^{j+1}}16^j\\
&=100t(8^k-1)
\le100t^4.
\end{aligned}
$$
$t=1$ 时该和为空，结论同样成立。最终
$$
\boxed{\|A_m^t e_t\|=\kappa_t\ge e^{-100t^4}.}
\tag{4.3}
$$

## 5. 全低输出空间的最小能量确有 4/3 阶增长

采用原全整数选择
$$
m(q)=\max\!\left(5,
 \left\lceil\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right),
\quad d(q)=2^{m(q)}.
$$
对充分大的整数 $q$，取
$$
t(q)=\left\lfloor
 \left(\frac{3\log q}{800}\right)^{1/3}
\right\rfloor,
\qquad
v_q^{\rm bad}=e_{t(q)}\otimes h_{m(q),q}.
$$
有 $1\le t(q)<d(q)$，且 $\|v_q^{\rm bad}\|=1$。把 (2.3)、(3.2)、(4.3) 合并：
$$
\log\lambda^{\rm loc}_{m(q),q}(v_q^{\rm bad})
\ge
-\frac13-100t^4
+\frac32t\log(m+2q)+\frac12t\log3
-\frac12\log(t!).
\tag{5.1}
$$
$t\asymp(\log q)^{1/3}$，故阶乘和常数项为
$o((\log q)^{4/3})$。对 $a=3/2,b=100$，
$\sup_{s\ge0}(aLs-bs^4)
=3a^{4/3}L^{4/3}/(4^{4/3}b^{1/3})$；
上面的整数选择达到相同主阶。因此
$$
\boxed{
\liminf_{q\to\infty}
\frac{\log\lambda^{\rm loc}_{m(q),q}(v_q^{\rm bad})}
 {(\log q)^{4/3}}
\ge
c_0:=
\frac{3(3/2)^{4/3}}{4^{4/3}100^{1/3}}
=0.1747818284\ldots>0.
}
\tag{5.2}
$$

记整个低输出空间上的最小修复算子范数为
$$
\Lambda_q=\sup_{\substack{v\in\mathscr V_{m(q),q}\\\|v\|\le1}}
 \lambda^{\rm loc}_{m(q),q}(v).
$$
原相容修复上界的证明只需 (1.1)，故对这里任意 $v$ 同样给
$\Lambda_q\le e^{F_q}$：保留 $D^kr$ 后，将外部与输入头幂合并为
$A^{j+k+1}$，使用真实四次衰减并对至多 $d^2$ 项求和即可。
原稿已证 $F_q=(K_*+o(1))(\log q)^{4/3}$。所以
$$
\boxed{
c_0
\le\liminf_{q\to\infty}\frac{\log\Lambda_q}{(\log q)^{4/3}}
\le\limsup_{q\to\infty}\frac{\log\Lambda_q}{(\log q)^{4/3}}
\le K_*.
}
\tag{5.3}
$$
因此在**整个低输出空间**上，$4/3$ 对数阶不是指定 $R_t$ 的粗范数独自产生的现象；换成真正最小元也不能获得统一多项式 $q^C$ 上界。

### 5.1 任意加宽窗口和整个无限高尾仍有同一下界

把修复支撑放宽到 $[q+1,q+h]$（任意 $h\ge d$），或整个
$[q+1,\infty)$，并仍要求 $Lc=r$。这些闭仿射集非空，因为原长度 $d$ 的修复已经可行，故各有唯一最小元。

对任何加宽后可行修复，前 $t$ 段仍满足
$$
D^tc_t=(-1)^{t-1}A^tv_q.
$$
(3.1)–(5.2) 的下界只使用这些前段，并没有使用原末端条件
$Ac_d=0$，所以全部保持。原 $D^d$ 条件也没有丢失：对 $t\le d$ 用 (1.1) 推得
$D^dc_t=(-A)^{t-1}D^{d-t}r=0$；对 $t>d$ 则直接有
$D^dc_t=(-A)^dc_{t-d}=0$。

特别，记无限高尾最小值为 $\lambda_{m,q}^{[\infty]}(v)$，则
$$
\boxed{
\lambda_{m(q),q}^{[\infty]}(v_q^{\rm bad})
\ge\exp[(c_0-o(1))(\log q)^{4/3}].
}
\tag{5.4}
$$
有限长度 $d$ 的候选仍给无限高尾问题的上界，故对整个低输出单位球，允许任意宽度后最小修复算子范数的对数也仍为
$\Theta((\log q)^{4/3})$。这个障碍并非由修复窗口长度 $d$ 人为造成。

(5.2)–(5.4) 不排除真实投影范围上的更好界，也不构造真缺陷。

## 6. 真实核对上述对偶观测的额外消灭条件

现在回到真实 $w\in M=\ker T$，以及原低投影
$v=v_{m,q}(w)$。假设处于原全整数合法窗
$$
4d\le q\le e^{d^3/4}.
$$
令 $E_m=L-T$，则
$$
Lw=E_mw,\qquad \|E_m\|\le26\eta_{m-1}.
$$
有限多项式恒等式给
$$
A^t-(-D)^t
=\sum_{j=0}^{t-1}A^{t-1-j}(-D)^j(A+D).
\tag{6.1}
$$
这里 $A,D$ 交换；没有假定 $E_m$ 与二者交换。

写
$$
x_g(w)=(I\otimes\langle g_{m,q},\cdot\rangle)
 P_q^{(m)}w.
$$
对 (6.1) 作用于 $w$，利用 $\|D\|\le1$、(2.4) 及尾次数正交，得到
$$
\boxed{
\|A^t x_g(w)\|
\le B_{m,q,t}\|P_{q+t}^{(m)}w\|
 +26t\,6^{t-1}\eta_{m-1}\|w\|.
}
\tag{6.2}
$$
这是利用全部真实核方程得到的条件，不能仅从低方程推出。

原低投影误差给
$\|v-P_{\le q}^{(m)}w\|\le e^{-74d^4}\|w\|$。
又 $\eta_{m-1}\le e^{-80d^4}$。对 $1\le t\le d$、$d\ge32$，
$$
(1+26d)6^d\le e^{d^4},
$$
所以
$$
\boxed{
\|A^t x_g(v)\|
\le B_{m,q,t}\|P_{q+t}^{(m)}w\|
 +e^{-73d^4}\|w\|.
}
\tag{6.3}
$$

还需支付归一化分母，不能把极小的 $B_{m,q,t}$ 隐去。
由 $J+1=m+2q+1\le3q$ 与 (2.3)，
$$
B_{m,q,t}^{-1}
\le[3(J+1)^3]^{t/2}
\le9^t q^{3t/2}.
$$
合法窗内
$$
\log B_{m,q,t}^{-1}
\le d\log9+\frac38d^4\le\frac12d^4.
$$
因此对 $Z_t(v)=\|A^t x_g(v)\|/B_{m,q,t}$，
$$
Z_t(v)\le\|P_{q+t}^{(m)}w\|
 +e^{-72d^4}\|w\|.
\tag{6.4}
$$
平方求和后得到
$$
\boxed{
\sum_{t=1}^d
 \frac{\|A^t x_g(v_{m,q}(w))\|^2}{t!\,S_J^t}
\le
2\tau_q(w)^2+e^{-143d^4}\|w\|^2.
}
\tag{6.5}
$$
这里 $\tau_q$ 是原总孔尾；尾孔超过 $q$ 必使总孔超过 $q$，所以该替换方向正确。

(3.1) 的同一个对偶下界，在真实投影范围上被 (6.5) 控制为趋零。这不等于 $\lambda_q(w)$ 的上界：这些配对见证尚未构成全部最小能量的控制族。

它还给一个准确的范围条件。若某个 $w\in M$ 满足
$v_{m(q),q}(w)=v_q^{\rm bad}$，则
$Z_{t(q)}(v_q^{\rm bad})=\rho_{m,q}\kappa_{t(q)}/B_{m,q,t(q)}$，其下界正是 (5.1) 右边的指数。对这个具体观测应用 (6.4)，得到
$$
\|w\|
\ge\exp[(c_0-o(1))(\log q)^{4/3}].
\tag{6.6}
$$
若该投影方程无解，其最小原像范数按 $+\infty$ 解释。因此坏单位输入不能来自真实核单位球；本文没有声称它根本不属于真实投影的线性像。

当前缺口被进一步限定：必须把类似 (6.2) 的真实全局相容条件提升为对全部压缩 Gram 逆能量的控制。仅凭低输出链、$D^d$ 约束、相容原像，或全低输出空间上的统一估计，不能跨过 (5.3) 的实际最小能量障碍。
