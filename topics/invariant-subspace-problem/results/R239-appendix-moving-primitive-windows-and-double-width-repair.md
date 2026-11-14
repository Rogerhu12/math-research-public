# R239 附录：移动原始窗口、真实自由坐标与双宽最小修复

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：本稿的移动窗口无权小修复及双宽最小能量判据已证明；真实剩余残量的完整能量、$N=M$ 和普通 Hilbert ISP 仍开放。

本稿接续[原始块无权消去](../results/R239-appendix-unweighted-primitive-removal-high-rank-blocks-and-full-projection-obstruction.md)、[原线性全部整数最小能量](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)以及[联合残量旗](../results/R271-appendix-orthogonal-residual-flags-and-exact-source-gram.md)。新点是允许原始块之前保留最多 $d$ 个自由尾位。修复保留真实 $w$ 在这些自由位上的全部坐标，因而不需要对自由位重新支付一个任意右逆的范数。

## 1. 参数、移动投影和待修复残量

对两个原实际边界均沿用
$$
M=\ker T,\qquad N=\overline{BM},\qquad
L_m=A_m+D_m,\qquad E_m=L_m-T.
$$
这里 $D_m=\sum_{j\ge m}a_jE_j$、$a_j=(j+1)^{-2}$，$d=2^m$，并有
$$
A_m^d=0,\quad \|A_m\|\le6,\quad
\|E_m\|\le26\eta_{m-1},\quad
\eta_{m-1}\le e^{-80d^4}.
\tag{1.1}
$$
取原全部整数头长
$$
m=m(q)=\max\left\{5,
 \left\lceil\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right\},
\qquad d=2^m,\qquad q\ge128.
\tag{1.2}
$$
故 $4d\le q\le e^{d^3/4}$，且 $d\asymp(\log q)^{1/3}$。
对固定 $w\in M$，记
$$
v=v_{m,q}=P_{\mathcal V_{m,q}}w,\qquad
\mathcal V_{m,q}=
 \mathcal H_{\le q}^{(m)}\cap\ker(P_{\le q-1}L_m),\qquad
r=L_mv=A_mv_q.
$$
已有的原 Hilbert 正交投影估计和层身份为
$$
\|v\|\le\|w\|,\qquad
\|v-P_{\le q}^{(m)}w\|\le\delta_m\|w\|,
\quad \delta_m=e^{-74d^4},\qquad D_m^dv=0.
\tag{1.3}
$$

现任选整数 $0\le k\le d$，把旧纯尾分成
$$
F=[m,m+k-1],\qquad
I=[m+k,m+k+2q-1],\qquad
[J,\infty),\quad J=m+k+2q.
\tag{1.4}
$$
空集 $F$ 对应 $k=0$。记相应删除算子为 $D_F,D_I,D_J$。

设 $P$ 是 $I$ 上的有界幂等算子，满足：
- 它的输入和输出都只在 $I$ 的恰好 $q$ 孔层；
- $D_IP=PD_I=0$。

将它在头、$F$ 和远尾上张量延拓为恒等算子，仍记作 $P$，并置 $C=\|P\|$。因 $P$ 保孔次数并与 $L_m$ 交换，$Pv\in\mathcal V_{m,q}$、$L_mPv=Pr$。$P$ 不必正交，也不假定它与实际 $T$ 交换。

一个具体选择是 $I$ 上的 $q$ 个相邻配对：
$$
h_i=\frac{b_i|10\rangle-a_i|01\rangle}{\sqrt{a_i^2+b_i^2}},
\qquad
g_i=\frac{a_i|10\rangle-b_i|01\rangle}{\sqrt{a_i^2+b_i^2}},
$$
其中 $a_i=a_{m+k+2i}$、$b_i=a_{m+k+2i+1}$、$0\le i<q$。
令 $h=\bigotimes h_i$、$g=\bigotimes g_i$、$\rho=\langle h,g\rangle$，则
$$
P=\frac{|h\rangle\langle g|}{\rho},\qquad
C=\rho^{-1}\le \exp\!\left(\frac2{m+k+1}\right).
\tag{1.5}
$$
故对全部 $0\le k\le d$ 一致有 $C=1+o(1)$。已证的受控高秩原始投影也可代入下面的同一证明。

## 2. 必须保留真实自由坐标

在 $\operatorname{Ran}P$ 上，$D_I$ 为零。置
$$
B=A_m+D_F,\qquad \nu=d+k.
\tag{2.1}
$$
$A_m$ 与 $D_F$ 交换，$D_F^{k+1}=0$，所以
$$
B^\nu=0,\qquad \|B\|\le7,\qquad \nu\le2d.
\tag{2.2}
$$
在此范围内 $L_m=B+D_J$。

以下用 $Q_t$ 表示远尾 $[J,\infty)$ 的恰好 $t$ 孔正交投影，用 $U_s$ 表示自由块 $F$ 的恰好 $s$ 孔正交投影。这些投影与 $P$ 交换。识别远尾真空因子后定义
$$
u=Q_0Pw,\qquad x_w=U_0u,\qquad x_v=Pv.
\tag{2.3}
$$
这里 $x_v$ 确实处于自由块和远尾的双真空：$P$ 的输出本身已经有 $q$ 个 $I$ 孔，而 $v$ 总旧尾孔数不超过 $q$。在 (2.3) 中把共同真空因子略去，$x_v,x_w$ 都在旧头与 $I$ 的原始块上。

由 (1.3)，
$$
e=x_v-x_w,\qquad \|e\|\le C\delta_m\|w\|.
\tag{2.4}
$$
把 $e$ 嵌入自由真空层，令
$$
u'=u+e.
\tag{2.5}
$$
于是
$$
U_0u'=x_v,\qquad U_su'=U_su\quad(1\le s\le k).
\tag{2.6}
$$
只改自由零孔坐标，真实 $w$ 的其余自由坐标完整保留。后者本来已经位于原尾总次数 $q+1,\ldots,q+k$，会作为合法高尾修复的初始层。

## 3. 相容真空 jets 与准确移动窗口修复

记
$$
S_J=\sum_{j\ge J}a_j^2,\qquad
\beta_t=\sqrt{t!}\,S_J^{t/2}.
\tag{3.1}
$$
只要 $J^{3/4}\ge2\nu$，已证的相容真空构造给 $b_t$，$0\le t<\nu$，满足
$$
b_0=\Omega_J,\qquad D_Jb_t=b_{t-1}\ (t\ge1),\qquad
b_t\in\mathcal H_t^{(J)},
$$
$$
\|b_t\|^2\le\frac{K}{\beta_t^2},\qquad
K=K_{J,\nu}:=
\exp\!\left(\frac{2\nu^2}{J^{3/4}}+
             \frac{8\nu}{J^{1/4}}\right).
\tag{3.2}
$$
因为 $\nu\le2d=O((\log q)^{1/3})$、$J\ge2q$，这个假设对充分大的 $q$ 一致成立，并且对 $0\le k\le d$ 一致有 $K=1+o(1)$。

定义
$$
\Phi(u')=\sum_{t=0}^{\nu-1}(-B)^tu'\otimes b_t,\qquad
c=Pv-\Phi(u').
\tag{3.3}
$$
相容关系和 $B^\nu=0$ 逐项消去，给
$$
L_m\Phi(u')=0,\qquad L_mc=Pr.
\tag{3.4}
$$
远尾零孔坐标为
$$
Q_0c=x_v-u'=-(I-U_0)u,
\tag{3.5}
$$
而 $Q_tc=-(-B)^tu'\otimes b_t$，$t\ge1$。由 (2.6)，(3.5) 的自由零孔坐标恰为零，其余坐标已有至少一孔。故 $c$ 没有尾总次数 $\le q$ 的成分。

还需核其最高次数，不能只相加 $\nu$ 与 $k$。展开
$$
B^t=\sum_{j=0}^t\binom tj A_m^jD_F^{\,t-j}.
\tag{3.6}
$$
起始自由孔数设为 $s\le k$。一个非零项的远尾孔数为 $t$，自由孔数为 $s-(t-j)$，所以这两部分的孔数和恰为
$$
s+j\le k+d-1.
\tag{3.7}
$$
最后不等式用了 $A_m^j=0$ 对 $j\ge d$。因此
$$
\boxed{c\in\mathcal H_{[q+1,q+d+k-1]}^{(m)}
       \subseteq\mathcal H_{[q+1,q+2d]}^{(m)}.}
\tag{3.8}
$$
由于 $D_mPv=0$，而 $L_m\Phi=0$ 蕴含
$D_m^d\Phi=(-A_m)^d\Phi=0$，也准确有
$$
\boxed{D_m^dc=0.}
\tag{3.9}
$$
这里用到的是 $D_I P=0$ 加自由、远尾真空来说明 $D_mPv=0$；没有把整个 $D_mP$ 错写成零。

## 4. 真实核方程控制全部自由坐标

真实 $Tw=0$ 给
$$
(B+D_J)Pw=PE_mw.
\tag{4.1}
$$
因 $B,D_J$ 交换，有限代数恒等式为
$$
B^t-(-D_J)^t
=\sum_{j=0}^{t-1} B^{t-1-j}(-D_J)^j(B+D_J).
\tag{4.2}
$$
取远尾真空坐标后，(4.1)--(4.2) 给
$$
B^tu=(-1)^tD_J^tQ_tPw+\epsilon_t,
$$
$$
\|\epsilon_t\|
\le26t\,7^{t-1}\eta_{m-1}C\|w\|.
\tag{4.3}
$$
这里 $\|D_J\|\le1$。从远尾 $t$ 孔层到真空的 $D_J^t$ 是一个标量行，其准确平方范数为
$(t!)^2e_t((a_j^2)_{j\ge J})\le t!S_J^t$。因此
$$
\frac{\|B^tu\|}{\beta_t}
\le\|Q_tPw\|+
 \frac{26t\,7^{t-1}\eta_{m-1}C}{\beta_t}\|w\|.
\tag{4.4}
$$

以下把极小实际进位与零孔微调都定量支付。因
$S_J\ge[3(J+1)^3]^{-1}$、$J+1\le3q$，对 $1\le t\le\nu\le2d$，
$$
\beta_t^{-1}\le(9q^{3/2})^t
\le
\exp\!\left(2d\log9+\tfrac34d^4\right)
\le e^{d^4}.
\tag{4.5}
$$
又对 $d\ge32$，
$$
\sqrt{2d}\,7^{2d}\le e^{d^4},
\qquad 26(2d)^{3/2}7^{2d}\le e^{d^4}.
$$
由 (1.1)、(2.4)、(4.3)--(4.5) 及 $\nu\le2d$，
$$
\left(\sum_{t=1}^{\nu-1}
 \frac{\|\epsilon_t\|^2}{\beta_t^2}\right)^{1/2}
\le C e^{-78d^4}\|w\|,
$$
$$
\left(\sum_{t=1}^{\nu-1}
 \frac{\|B^te\|^2}{\beta_t^2}\right)^{1/2}
\le C e^{-72d^4}\|w\|.
\tag{4.6}
$$
两项之和至多 $C e^{-71d^4}\|w\|$。

关键的观测量不会按 $t$ 重复收取同一个向量。确切地说，
$$
Q_0(I-U_0)P,\qquad Q_tP\quad(1\le t<\nu)
$$
分别作用于互相正交的远尾输入层，第一项还排除了自由零孔。$P$ 只作用于 $I$，且只接受 $I$ 的 $q$ 孔层。因此这些输入都落在旧尾总次数
$$
[q+1,q+k+\nu-1]=[q+1,q+d+2k-1]
$$
中，而且输入正交。即便不同 $t$ 对应同一个总孔次数，它们仍属于不同的远尾正交子层。于是
$$
\boxed{
\|(I-U_0)u\|^2+\sum_{t=1}^{\nu-1}\|Q_tPw\|^2
\le C^2
 \|P_{[q+1,q+d+2k]}^{(m)}w\|^2.
}
\tag{4.7}
$$
这一步只有一次 $C$，没有 $\sqrt{\nu}$ 或 $\sqrt{k}$。

(3.5) 的远尾各层也互相正交。使用 (3.2)、(4.4)、(4.6)、(4.7) 和有限 $\ell^2$ 和中的三角不等式，得到本稿主要估计：
$$
\boxed{
\|c\|\le
\sqrt{K_{J,d+k}}\,C
\left[
 \|P_{[q+1,q+d+2k]}^{(m)}w\|
 +e^{-71d^4}\|w\|
\right].
}
\tag{4.8}
$$
对配对投影 (1.5)，一致于 $0\le k\le d$，
$$
\boxed{
\|c\|\le(1+o(1))\,\tau_q(w)
       +e^{-70d^4}\|w\|\longrightarrow0,
}
\tag{4.9}
$$
其中 $\tau_q(w)=\|1_{\{\mathcal N>q\}}w\|$ 是原全部孔尾。旧尾孔数大于 $q$ 的向量必有全部孔数大于 $q$，所以 (4.8) 的局部带范数至多 $\tau_q(w)$。一般受控 $C$ 也给无权趋零；若 $C=1+o(1)$，首项常数仍趋于 $1$。

整个证明只对真正的 $PE_mw$ 使用 (4.3) 的有限恒等式并支付其归一化成本，没有从一个小算子误差直接推断任意小范数原像。

## 5. 双宽最小能量与实际逐头提升

为容纳 (3.8)，现在明确使用新的双宽最小值，避免与旧宽度 $d$ 的最小值混同。对同一实际 $r=L_mv$，定义
$$
\widetilde{\mathcal C}_q(w)=
\left\{c\in\mathcal H_{[q+1,q+2d]}^{(m)}:
 L_mc=r,\quad D_m^dc=0\right\},
\qquad
\widetilde\lambda_q(w)=\min_{c\in\widetilde{\mathcal C}_q(w)}\|c\|.
\tag{5.1}
$$
旧宽度 $d$ 的修复属于此集合，所以集合非空、闭，且
$$
\widetilde\lambda_q(w)\le\lambda_q(w)
 \le e^{F(m,q)}
 [\tau_{q-d}(w)+e^{-74d^4}\|w\|],
\qquad
\widetilde\lambda_q(w)\le e^{2d^4}\|w\|.
\tag{5.2}
$$
最后一个粗界也可直接使用 $\|v\|\le\|w\|$ 得到，不需从方括号估计再多付常数。最小元记作 $\widetilde c_q$。令
$$
\widetilde k_q=v-\widetilde c_q\in\ker L_m.
$$
它的旧尾孔数至多 $Q_0=q+2d$，且
$$
Q_0\le\tfrac32q\le e^{d^3/3},\qquad
\|\widetilde k_q\|\le2e^{2d^4}\|w\|.
\tag{5.3}
$$
因此原稿已独立证明的逐头实际提升
$$
\Lambda^{\rm lin,inc}_{m,Q_0}:
 \ker L_m\cap\mathcal H_{\le Q_0}^{(m)}\longrightarrow N,
\quad
\|\Lambda k-k\|\le e^{-75d^4}\|k\|
$$
仍在准确输入范围内。所得 $\widetilde n_q\in N$ 满足
$$
\|\widetilde n_q-(v-\widetilde c_q)\|
\le e^{-72d^4}\|w\|.
\tag{5.4}
$$
于是
$$
\widetilde n_q=w-\widetilde c_q+\widetilde\rho_q,\qquad
\sup_{q\ge Q}\|\widetilde\rho_q\|
\le\tau_Q(w)+2e^{-72d(Q)^4}\|w\|\longrightarrow0.
\tag{5.5}
$$
这里仍使用原位号 $\eta_{m-1}$ 及原逐头核阶重置；没有用平方模型替代原线性提升。

## 6. 双宽窗口的覆盖仍至多为 2

$\widetilde c_q$ 的原全部孔支撑包含于
$$
\widetilde I_q=[q+1,q+\widetilde\ell_q],
\qquad \widetilde\ell_q=2d(q)+m(q).
\tag{6.1}
$$
序列 $\widetilde\ell_q$ 单调。因 $m(q)\le d(q)/2$ 和 $q\ge4d(q)$，
$$
\widetilde\ell_q\le5q/8.
$$
若整数 $p\in\widetilde I_q$，则 $q<p\le13q/8<2q$。由 (1.2) 的准确取整式，$m(p)-m(q)\le1$，所以
$$
\widetilde\ell_p
 \le4d(q)+m(q)+1\le2\widetilde\ell_q.
\tag{6.2}
$$
另一方面 $p-\widetilde\ell_p\le q\le p-1$，可行整数 $q$ 至多 $\widetilde\ell_p$ 个。故
$$
\boxed{
\sum_{\substack{q\ge128\\p\in\widetilde I_q}}
 \frac1{\widetilde\ell_q}\le2.
}
\tag{6.3}
$$
特别，对任意单位向量 $h_q$ 支撑于 $\widetilde I_q$，
$$
\sum_{q\ge Q}\frac{|\langle h_q,w\rangle|^2}
                         {\widetilde\ell_q}
\le2\tau_Q(w)^2.
\tag{6.4}
$$

与原稿相同的有限正凸平均证明现在给准确的双宽判据
$$
\boxed{
\sum_{q\ge128}
 \frac1{\widetilde\ell_q(1+\widetilde\lambda_q(w)^2)}
 =\infty
\quad\Longrightarrow\quad w\in N.
}
\tag{6.5}
$$
具体地，令 $a_q=[\widetilde\ell_q(1+\widetilde\lambda_q^2)]^{-1}$、$A_{Q,R}=\sum_{Q\le q\le R}a_q$。(6.3) 给
$$
\left\|\sum_{q=Q}^Ra_q\widetilde c_q\right\|^2
\le2\sum_{q=Q}^Ra_q^2\widetilde\ell_q\widetilde\lambda_q^2
\le2A_{Q,R}.
$$
对 (5.5) 的 $\widetilde n_q\in N$ 作这些有限正权平均，先令 $R\to\infty$ 再令 $Q\to\infty$，即得 (6.5)。

若 $0\ne w\in M\ominus N$，(5.5) 给
$\langle\widetilde c_q,w\rangle\to\|w\|^2$。由 (6.4)，充分大的 $Q$ 满足
$$
\boxed{
\sum_{q\ge Q}
 \frac1{\widetilde\ell_q\,\widetilde\lambda_q(w)^2}
 \le\frac{8\tau_Q(w)^2}{\|w\|^4}.
}
\tag{6.6}
$$
因为 $\widetilde\ell_q=O((\log q)^{1/3})$，充分增长条件依然是
$$
\widetilde\lambda_q(w)^2
=O\!\left(q(\log q)^{2/3}\log\log q\right).
\tag{6.7}
$$
它蕴含 (6.5) 的发散。本稿未证明每个实际 $w$ 都满足 (6.7)。

## 7. 移动分量在准确最小能量中的消去

令 $\mathcal R_{m,q}=L_m\mathcal V_{m,q}$ 为已证的闭残量旗。对 $r'\in\mathcal R_{m,q}$，把宽度 $2d$ 的最小修复算子记作 $F_{2d}^{\dagger}r'$。它是线性的：每个最小元都与共同齐次核正交，且旧宽度 $d$ 的有界右逆保证固定 $m,q$ 下的有界性。相关常数允许依赖 $m,q$。

$P$ 保尾次数且与 $L_m,D_m$ 交换，故它保 $\mathcal V_{m,q}$、$\mathcal R_{m,q}$，也保已证的链旗。所以 $Pr,(I-P)r$ 都是合法旗残量，不需要把环境任意源误认作实际残量。这里双宽可行集始终按 (5.1) 定义；旧宽度 $d$ 的三角链旗没有被原样认作宽度 $2d$ 的链空间。由最小性和 (4.8)，
$$
\|F_{2d}^{\dagger}Pr\|\le\|c\|\longrightarrow0.
$$
从线性与三角不等式得到
$$
\boxed{
\left|
 \|F_{2d}^{\dagger}r\|-
 \|F_{2d}^{\dagger}(I-P)r\|
\right|
\le\|F_{2d}^{\dagger}Pr\|
\le\|c\|\longrightarrow0.
}
\tag{7.1}
$$
因此对真正 $w\in M$，任何上述受控移动原始块的残量分量都可从双宽最小能量中无权消去。$k=0$ 回到旧的固定前缀结论；$k>0$ 的自由坐标由真实源支付，并非假设它们是真空。

这还没有覆盖 $\mathcal R_{m,q}$ 的全部方向，也没有控制 (7.1) 中剩余分量的双宽能量。旧的局部 $\log^{4/3}$ 最小能量坏族在任意有限宽度乃至无限高尾仍成立；固定前缀完整原始投影的指数范数障碍也保持有效。尚需能够处理全部真实剩余残量的受控分解或新的源专属估计，不能把受控高秩或有限移动窗口族当作完备性证明。
