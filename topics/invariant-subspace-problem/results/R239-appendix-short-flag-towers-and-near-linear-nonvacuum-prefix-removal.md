# R239 附录：联合核短塔与近一次非真空前缀消去

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。状态：以下核阶范数界、受限伴随误差、精确短塔及真实源小修复已证明；早期分支的完整最小能量及普通 Hilbert ISP 仍开放。

本稿接续[低孔 Fock 塔](../results/R239-appendix-low-hole-fock-tower-and-nonvacuum-primitive-prefix-removal.md)、[完整首个三维块分解](../results/R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)及 [R271 联合旗预算](../results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)。新点是从实际源已在的删除核开始，只建 $d$ 个高尾层。受限伴随与全空间伴随的差被显式保留并估计，因此没有把裸 $D^*$ 当作保核阶的创建算子。

## 1. 删除核上的范数只由核阶控制

先设一般有界算子 $D$ 满足
$$
[D,D^*]\le S I,\qquad S>0.
$$
记 $E_h=\ker D^h$。$E_h$ 对 $D$ 不变，令 $T=D|_{E_h}$。其压缩伴随为 $T^*=P_{E_h}D^*|_{E_h}$，所以
$$
[T,T^*]\le P_{E_h}[D,D^*]|_{E_h}\le S I.
\tag{1.1}
$$
第一不等式中的差恰含负的正交补投影项。

**引理 1.1。**
$$
\boxed{\|D|_{\ker D^h}\|^2\le(h-1)S.}
\tag{1.2}
$$

证明：对 $x\in E_h$ 令 $a_k=\|T^kx\|^2$。若 $a_{k-1},a_k>0$，(1.1) 和 Cauchy--Schwarz 给
$$
a_{k+1}\ge\|T^*T^kx\|^2-Sa_k
          \ge\frac{a_k^2}{a_{k-1}}-Sa_k.
$$
故 $a_{k+1}/a_k\ge a_k/a_{k-1}-S$。若某个单位 $x$ 有
$a_1>(h-1)S$，所有到 $a_h$ 的比值都保持正，矛盾于 $T^h=0$。
这也排除了范数上确界大于 $(h-1)S$，不要求范数取得。证毕。

反复应用于降低的核阶，得
$$
\|D^j x\|
\le
\sqrt{\frac{(h-1)!}{(h-1-j)!}}\,
 S^{j/2}\|x\|
\quad(0\le j<h,\ x\in E_h).
\tag{1.3}
$$
同时 $\|D^*x\|^2\le hS\|x\|^2$，但此范数界不声称
$D^*x\in E_{h+1}$。

## 2. 真实纯尾的创建泄漏

现在取原物理纯尾
$$
D=D_J=\sum_{j\ge J}a_jE_j,\qquad a_j=(j+1)^{-2},\qquad J\ge5,
$$
$$
S=\sum_{j\ge J}a_j^2,\quad
\epsilon=\frac{a_J^2}{S}\le\frac3{J+1},\quad
W=\sum_{j\ge J}a_j^2n_j,\quad
D_3=\sum_{j\ge J}a_j^3E_j.
$$
则
$$
[D,D^*]=S I-2W,\qquad [D,W]=D_3,\qquad [D,D_3]=0.
$$
对 $x\in\ker D^h$，有限交换子展开准确给
$$
\boxed{D^{h+1}D^*x=-h(h+1)D_3D^{h-1}x.}
\tag{2.1}
$$
推导为
$$
[D^r,D^*]=rS D^{r-1}
 -2\sum_{j=0}^{r-1}D^jWD^{r-1-j},
$$
以及
$D^jW=WD^j+jD_3D^{j-1}$；置 $r=h+1$ 后，所有含
$D^hx$ 的项都为零。

在恰好 $p$ 孔层记 $E_{h,p}=\ker D^h\cap\mathcal H_p$。若
$2p\epsilon\le1/2$，则直到 $p+1$ 层均有
$$
D_\ell D_\ell^*
=D_{\ell-1}^*D_{\ell-1}+S I-2W_{\ell-1}
\ge \tfrac12 S I.
$$
canonical 右逆 $R_\ell=D_\ell^*(D_\ell D_\ell^*)^{-1}$ 因而满足
$\|R_\ell\|\le\sqrt{2/S}$。把它们复合，得到
$D^{h+1}$ 在相关有限层的右逆，范数至多 $(2/S)^{(h+1)/2}$。
若 $h>p$，下面的创建泄漏本来为零；否则该复合从非负次数层开始，完全合法。

由 (1.3)、(2.1) 和到核的距离估计，
$$
\|(I-P_{E_{h+1,p+1}})D^*x\|
\le h(h+1)\sqrt{(h-1)!}\,2^{(h+1)/2}
       \frac{\|D_3\|}{S}\,\|x\|.
\tag{2.2}
$$
准确的物理系数给
$$
\|D_3\|\le\sum_{j\ge J}a_j^3\le\frac1{5J^5},
\qquad S\ge\frac1{3(J+1)^3},
$$
所以对 $J\ge5$，
$\|D_3\|/S^{3/2}\le4/\sqrt J$。因此可统一放宽成
$$
\boxed{
\|(I-P_{E_{h+1,p+1}})D^*|_{E_{h,p}}\|^2
\le S\,\frac{[16(h+1)]^{h+4}}{J}.
}
\tag{2.3}
$$
这里的 $J^{-1}$ 是实际物理尾系数产生的量，而不是形式 CCR 假设。

## 3. 必须保留的受限伴随项

固定整数 $d\ge1$、源次数 $s\ge0$，假设
$$
s+d\le\frac{J+1}{12}.
\tag{3.1}
$$
这保证前节的全层右逆在本节所需范围内有上述统一界。定义
$$
\mathcal E_t=E_{d+t,s+t}\quad(0\le t\le d),\qquad
B_t=D|_{\mathcal E_t}:\mathcal E_t\to\mathcal E_{t-1}
\quad(t\ge1).
$$
另令 $B_0=D_s|_{\mathcal E_0}$，其目标为
$E_{d-1,s-1}$；$s=0$ 时取零算子。

每个 $B_t$ 满射。确实，若 $x\in\mathcal E_{t-1}$，则
$R_{s+t}x\in\mathcal E_t$，因为
$D^{d+t}R_{s+t}x=D^{d+t-1}x=0$。全层最小原像已经落在受限域，因此其限制也正是 $B_t$ 的最小范数右逆。

在 $\mathcal E_{t-1}$ 上，置
$$
K_t=(I-P_{\mathcal E_t})D_{s+t}^*|_{\mathcal E_{t-1}}.
$$
真正受限伴随给准确恒等式
$$
\boxed{
B_tB_t^*
=B_{t-1}^*B_{t-1}+S I-F_t,
\quad
F_t=2P_{\mathcal E_{t-1}}W_{s+t-1}|_{\mathcal E_{t-1}}
      +K_t^*K_t.
}
\tag{3.2}
$$
其中 $F_t\ge0$。第二项 $K_t^*K_t$ 不能删除：这正是全 $D^*$ 不保核阶造成的差。

由 $W_p\le p a_J^2$、(2.3) 及 $d+t-1<2d$，
$$
\boxed{
\|F_t\|\le S\theta,\qquad
\theta=
2(s+d)\epsilon+
\frac{[16(2d+1)]^{2d+4}}{J}.
}
\tag{3.3}
$$
另外，引理 1.1 给基底频率
$$
Q=B_0^*B_0,\qquad 0\le Q\le(d-1)S I.
\tag{3.4}
$$
此界与源次数 $s$ 无关。

## 4. 只建 d 层的精确算子值 Fock 塔

在层 $t$ 使用外直和
$$
\mathfrak E_t=\mathcal E_0
 \oplus\bigoplus_{j=1}^t K_{s+j},
\qquad K_{s+j}=\ker D_{s+j}.
$$
定义 $\mathfrak a_t:\mathfrak E_t\to\mathfrak E_{t-1}$：
- 在旧基底 $\mathcal E_0$ 上，它为 $(Q+tS I)^{1/2}$；
- 在出生层 $K_{s+j}$、$j<t$ 上，它为
  $\sqrt{(t-j)S}$；
- 它杀去新生 $K_{s+t}$。

这些都是明确定义的正函数演算；在旧基底上的不同频率彼此交换。令
$\mathfrak a_0=B_0$。在 $\mathfrak E_{t-1}$ 上，
$$
\mathfrak a_t\mathfrak a_t^*
=\mathfrak a_{t-1}^*\mathfrak a_{t-1}+S I.
\tag{4.1}
$$
归一化后的正频率
$M_t=S^{-1}\mathfrak a_t\mathfrak a_t^*$ 满足
$$
I\le M_t\le2d I.
\tag{4.2}
$$

设 $\mathcal R_t=B_t^*(B_tB_t^*)^{-1}$，它就是前节全层 canonical 右逆在受限源上的限制。取 $V_0=I$，递归令 $V_t$ 在新生分量上为恒等，在旧塔上为
$$
V_t|_{\mathfrak E_{t-1}}
=\mathcal R_t V_{t-1}
  (\mathfrak a_t|_{\mathfrak E_{t-1}}).
\tag{4.3}
$$
因为 $\mathcal E_t=K_{s+t}\oplus^\perp\mathcal R_t\mathcal E_{t-1}$，
每个 $V_t:\mathfrak E_t\to\mathcal E_t$ 是有界同构，且
$$
\boxed{B_tV_t=V_{t-1}\mathfrak a_t.}
\tag{4.4}
$$

置
$$
T_d=32(2d+1),\qquad \Delta=\theta T_d^d,
\qquad
\Delta\le\frac1{100(2d+1)}.
\tag{4.5}
$$
则
$$
\boxed{
\|V_t^*V_t-I\|\le\Delta\quad(0\le t\le d),
\qquad
\|V_t\|\,\|V_t^{-1}\|
\le\kappa:=\sqrt{\frac{1+\Delta}{1-\Delta}}.
}
\tag{4.6}
$$

为完整支付累积，记 $G_t=V_t^*V_t$。与旧低孔塔同一有限 Gram 运算给
$$
(G_t)_{\rm old}=H_t^*C_t^{-1}H_t,
\quad H_t=M_t^{-1/2}G_{t-1}M_t^{1/2},
$$
$$
C_t=(SM_t)^{-1/2}
 \bigl[
  \mathfrak a_{t-1}^*G_{t-2}\mathfrak a_{t-1}
  +SG_{t-1}-V_{t-1}^*F_tV_{t-1}
 \bigr]
 (SM_t)^{-1/2}.
\tag{4.7}
$$
$t=1$ 时前一层是实际 $B_0$，相应 $G_{-1}=I$；$G_0=I$。
若此前误差不超过 $\delta$，(3.3)、(4.2) 给
$$
\|C_t-I\|\le2\delta+\theta(1+\delta),\qquad
\|H_t-I\|\le\sqrt{2d}\,\delta.
$$
在 (4.5) 下小量条件逐步自洽；使用
$\|H^*C^{-1}H-I\|\le3\|C-I\|+3\|H-I\|$
（两小量均不超过 $1/4$），得到
$$
\|G_t-I\|
\le(6+3\sqrt{2d})\delta+6\theta.
$$
从 $G_0=I$ 归纳即有
$\|G_t-I\|\le\theta T_d^t\le\Delta$。因此成本只累积 $d$ 次，
不再累积 $s+d$ 次。

## 5. 实际原始前缀与真实旗投影

回到原线性合法窗
$$
m\ge5,\quad d=2^m,\quad 4d\le q\le e^{d^3/4},
\quad L_m=A_m+D_m,\quad A_m^d=0,\quad\|A_m\|\le6.
$$
原实际误差满足
$$
E_m=L_m-T,\qquad
\|E_m\|\le26\eta_{m-1},\qquad
\eta_{m-1}\le e^{-80d^4}.
$$
取 $0\le s\le q/2$、$n=q-s$、$J=m+2n$，令
$\mathcal P_n$ 是前 $n$ 个相邻配对的原始投影，在余尾上恒等。
记 $C_n=\|\mathcal P_n\|\le e^{2/(m+1)}$。其前缀固定为 $n$ 孔，
并杀去此前缀删除；在其像上 $L_m=A_m+D_J$。以下去掉单位原始前缀作等距识别。

对实际 $w\in M$，令 $v=v_{m,q}(w)$、$r=L_mv$，并写
$v^\circ=\mathcal P_nv$、$w^\circ=\mathcal P_nw$。
$v^\circ$ 的远尾最高次数为 $s$，且
$$
D_J^dv^\circ=0,\qquad
\|v^\circ-P_{\le s}^{(J)}w^\circ\|
\le C_n e^{-74d^4}\|w\|.
\tag{5.1}
$$

未来层也有真正的联合核近似，不能只使用 (5.1) 的低部。
R271 联合旗预算 §5 已在同一 $q$ 的实际辅助常数内证明：
把 $w$ 投到 $V_{m,q+d}$ 所得 $\widehat v$ 满足
$$
D_m^d\widehat v=0,\qquad
\|\widehat v-P_{\le q+d}^{(m)}w\|
\le e^{-74d^4}\|w\|.
\tag{5.2}
$$
该证明使用 $R\le2048q^2$、$\log(2+R)\le d^3$，没有把外观
$q+d$ 偷代进原 $q\le e^{d^3/4}$ 的范围。

对 $t=0,\ldots,d$，定义
$$
u_t=P_{\mathcal E_t}w^\circ_{s+t},
\qquad
\mathcal E_t=E_{d+t,s+t}.
$$
(5.2) 的每个对应层甚至在 $E_{d,s+t}\subseteq\mathcal E_t$。
因此，所有层的一次正交投影给
$$
\boxed{
\left(\sum_{t=0}^d
 \|w^\circ_{s+t}-u_t\|^2\right)^{1/2}
\le C_n e^{-74d^4}\|w\|.
}
\tag{5.3}
$$
此外 $v_s^\circ\in\mathcal E_0$，故
$$
\|v_s^\circ-u_0\|\le C_n e^{-74d^4}\|w\|.
\tag{5.4}
$$

投影真实方程 $(A_m+D_J)w^\circ=\mathcal P_nE_mw$ 得
$$
A_mu_{t-1}+B_tu_t=e'_{t-1}\quad(1\le t\le d).
\tag{5.5}
$$
额外项是
$-P_{\mathcal E_{t-1}}D_J(I-P_{\mathcal E_t})w^\circ_{s+t}$。
用 $\|D_J\|\le1$、(5.3) 和各输出层正交性，
$$
\boxed{
\|e'\|
\le C_n(26\eta_{m-1}+e^{-74d^4})\|w\|.
}
\tag{5.6}
$$
没有另付 $\sqrt d$，也没有把投影后的向量假装仍是实际 $T$ 核。

## 6. 原宽 d 内的准确小修复

假设 (3.1)、(4.5) 对当前参数成立。变换 $u_t$ 为
$V_t^{-1}u_t$，并抽取旧基底 $\mathcal E_0$ 分量，记为 $y_t$。
因为 $V_0=I$，$y_0=u_0$。令
$$
\Omega_t=(Q+tS I)^{1/2},\qquad
\Pi_t=\Omega_t^{-1}\cdots\Omega_1^{-1},\qquad \Pi_0=I.
$$
这些算子都只作用于尾基底，因而与 $A_m$ 交换，且
$$
\|\Pi_t\|\le(t!S^t)^{-1/2}.
\tag{6.1}
$$
由 (4.4)、(5.5)，旧基底坐标满足
$$
A_my_{t-1}+\Omega_ty_t=\widetilde e_{t-1},
\qquad
\|\widetilde e\|\le2\|e'\|.
\tag{6.2}
$$

对 $1\le t<d$，令
$$
c_t=(-1)^{t-1}V_t
 \bigl[A_m^t\Pi_t v_s^\circ\bigr],
\tag{6.3}
$$
方括号作为 $\mathfrak E_t$ 的旧基底分量嵌入，其余分量为零。
把原始前缀补回，并令 $c=\sum_{t=1}^{d-1}c_t$。由精确交织与
$A_m^d=0$，
$$
\boxed{
L_mc=\mathcal P_nr,\qquad
c\in\operatorname{Ran}\mathcal P_n
  \cap\mathcal H_{[q+1,q+d-1]}^{(m)},\qquad D_m^dc=0.
}
\tag{6.4}
$$
最后一式也可由 $v^\circ-c\in\ker L_m$ 与 $D_m^dv^\circ=0$ 直接推出。

迭代 (6.2)，其误差矩阵的第 $(t,j)$ 项范数至多
$6^dS^{-d/2}$；全部高度的算子范数至多
$$
\Gamma_d=d6^dS^{-d/2}
\le d54^d q^{3d/2}\le e^{d^4}.
\tag{6.5}
$$
最后两式用 $J+1\le3q$、$S\ge[3(J+1)^3]^{-1}$、
$\log q\le d^3/4$ 和 $d\ge32$。初始误差 (5.4) 的延伸成本也至多
$\Gamma_d$。

旧基底投影是标准塔中的正交投影；$V_t$ 和逆的条件数至多 $\kappa$。
由 (5.4)--(5.6)、(6.2)--(6.5)，分别一次计入全部高度，可得
$$
\boxed{
\|c\|\le
\kappa C_n
 \|P_{[q+1,q+d-1]}^{(m)}w\|
 +C_n e^{-72d^4}\|w\|.
}
\tag{6.6}
$$
具体小项可先用
$2C_n\Gamma_d(52\eta_{m-1}+3e^{-74d^4})\|w\|$
控制，再吸收常数。该式同时支付真实进位、未来旗投影和原顶部投影；
没有未控制的受限伴随误差留在结论外。

## 7. 剩余非真空孔数可取 q 的近一次幂

沿原全整数 $m(q),d(q)$，令
$$
\mathfrak b_d=128(d+1),\qquad
s(q)=\left\lfloor\frac{q}{\mathfrak b_d^{d+4}}\right\rfloor,\qquad
n(q)=q-s(q).
\tag{7.1}
$$
因为 $d(q)\asymp(\log q)^{1/3}$，
$$
\boxed{s(q)=q^{1-o(1)},\qquad s(q)/q\to0,\qquad J=m+2n\sim2q.}
\tag{7.2}
$$
这里是明确的整数序列，不假定它在头长跳变处单调。

(3.1) 最终成立。又 $T_d\le \mathfrak b_d$、
$16(2d+1)\le \mathfrak b_d$、$\epsilon\le3/(J+1)$，故
$$
\Delta
\le
\frac{6(s+d)\mathfrak b_d^d}{J+1}
+\frac{\mathfrak b_d^{3d+4}}J
=O(\mathfrak b_d^{-4})+
 \frac{\exp(O(d\log d))}{q}
\longrightarrow0.
\tag{7.3}
$$
右边实际为 $o(d^{-1})$，所以 (4.5) 最终成立。于是
$\kappa\to1$、$C_n\to1$，(6.6) 给
$$
\boxed{
\|c_q\|\le(1+o(1))\tau_q(w)
          +e^{-71d(q)^4}\|w\|\longrightarrow0
\quad(w\in M).
}
\tag{7.4}
$$
这在原宽度 $d(q)$ 的真实修复空间内成立。

因此可消去的源现在是
$\mathcal P_{q-s(q)}r_q$：只固定前 $q-s(q)$ 个配对原始块，之后允许
$s(q)=q^{1-o(1)}$ 个局部剩余尾孔。与先前的
$s=O(\log q/\log\log q)$ 相比，增长来自真实联合核和准确受限伴随，
不是只调整原真空原像常数。

## 8. 完整能量中可删除的整个末段

对完整首个三维分解
$I=T_\infty+\sum_{i=1}^qT_i$，仍有
$$
\mathcal P_{q-s(q)}
=T_\infty+\sum_{i=q-s(q)+1}^qT_i.
$$
本稿修复 $c_q$ 位于其像中。一次完整分析界给
$$
\boxed{
\mu_\infty^{[h]}(r_q)^2+
 \sum_{i=q-s(q)+1}^q\mu_i^{[h]}(r_q)^2
\le A_q^2\|c_q\|^2\longrightarrow0
\qquad(h\ge d(q)).
}
\tag{8.1}
$$
没有 $\sqrt{s(q)}$ 损失。对原宽或双宽的准确最小算子，同样有
$$
\left|
\|F_h^\dagger r_q\|-
\|F_h^\dagger(I-\mathcal P_{q-s(q)})r_q\|
\right|\le\|c_q\|\longrightarrow0.
\tag{8.2}
$$

这仍然是完整分解的一个末段，而非全部方向；$s(q)/q\to0$ 已在 (7.2) 明示。早期三维分支、整个真正最优头跃迁通量及使倒数能量准则发散的统一增长控制仍未闭合。
本稿不由有限源可实现性、受限塔闭像或末段消去推断 $N=M$。


[完整工作源](../notes/2026-11-13-short-flag-towers-and-near-linear-nonvacuum-prefix-removal-boundary-resume.md)。
