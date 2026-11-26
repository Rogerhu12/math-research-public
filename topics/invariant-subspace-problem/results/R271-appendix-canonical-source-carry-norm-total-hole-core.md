# 规范形式原像的真实 carry 范数与总孔图核心

日期：2026-11-27（Asia/Taipei）；2026-11-26（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下条件定理及实际范数估计已证明；未证明真正的 $W$ 来源自动满足该条件，$N=M$ 仍开。**

本文接[负前缀条件核心](R271-appendix-negative-prefix-extension-and-output-conditioned-division-graph-core.md)，但不重复其分别控制纯对角项与首次补孔项的判据。新的输入是 R238 已证的规范原像每个**总物理孔层**都在 Hilbert 空间；新的估计保留真实 carry 在首缺位 $q$ 上的 $\eta_{q-1}$，而不将它放大成旧的 $O((q+1)^{-2})$。这样可以改用总孔截断，整个纯创建项由准确升一次数的恒等式支付。

## 1. 实际对象及两种不同分级

沿用原两型
$$
B e_n=\alpha_{v_2(n)}e_{n-1},\quad Be_0=0,
\quad S=B^*,\quad
N_i=B^{2^i}/d_i,
$$
$$
T_N=\sum_{i\ge0}a_iN_i,\qquad
T_Y=\sum_{i\ge0}a_iN_i(I+N_i)^{-1},
\qquad a_i=(i+1)^{-2}.
$$
令
$$
D^*=\sum_{i\ge0}a_iE_i^*,\qquad
K_N=T_N^*-D^*,\quad K_Y=T_Y^*-D^*.
\tag{1.1}
$$
$E_i^*$ 是第 $i$ 个物理位的纯孔创建。所有算子在原边界 Hilbert 空间上作用；下面不删除任何 carry。

用 $P_q$ 表示首缺位恰为 $q$ 的投影，即前 $q$ 位全占据、第 $q$ 位真空，其余位全部保留。它与总孔投影不同。用 $\mathsf P_p$ 表示**全部物理位**恰有 $p$ 孔的投影。

真实比例为
$$
\eta_i=\frac{\alpha_{i+1}}{\alpha_i},\qquad
-\log\eta_i=1400\,16^i-630\,8^i+300\,2^i.
\tag{1.2}
$$
特别
$$
0<\eta_i<\frac1{16},\qquad
\eta_{i+1}\le\frac14\eta_i.
\tag{1.3}
$$
第二式由两相邻负对数之差
$21000\,16^i-4410\,8^i+300\,2^i>\log4$ 直接给出。

定义真实 carry 权
$$
b_0=\eta_0,\qquad
b_q=a_{q-1}\eta_{q-1}=q^{-2}\frac{\alpha_q}{\alpha_{q-1}}
\quad(q\ge1).
\tag{1.4}
$$
它并非 $\alpha_q$，而只丢失一个前位的权。

## 2. N 型的准确正交 carry 列

首先分清三个位置关系。由真实二进位加法，
$$
(N_i^*-E_i^*)P_i=0.
\tag{2.1}
$$
若 $q>i$，则 $E_i^*P_q=0$，而 $N_i^*P_q$ 是系数 $\alpha_q/\alpha_i$ 乘一个等距：它将第 $i,\ldots,q-1$ 位从占据重置为真空，将第 $q$ 位从真空置为占据。于是
$$
\|N_i^*P_qx\|=\frac{\alpha_q}{\alpha_i}\|P_qx\|.
\tag{2.2}
$$
其输出首缺位为 $i$，该位之后的第一个占据位为 $q$。因此不同有序对 $(i,q)$（$i<q$）的这些输出空间两两正交。

若 $q<i$，不能把 carry 删掉；不过 $N_i^*-E_i^*$ 不改变第 $q$ 位及其以下各位，故保 $P_q\mathcal H$，而
$$
\|(N_i^*-E_i^*)P_q\|\le\eta_i.
\tag{2.3}
$$

据此，先在有限首缺位块上写
$$
K_N=K_{\downarrow}+K_{\rm diag},
$$
$$
K_{\downarrow}x=\sum_{q\ge1}\sum_{i<q}a_iN_i^*P_qx,
\qquad
K_{\rm diag}x=\sum_{q\ge0}\sum_{i>q}a_i(N_i^*-E_i^*)P_qx.
\tag{2.4}
$$
定义
$$
c_q^2=\sum_{i<q}a_i^2\left(\frac{\alpha_q}{\alpha_i}\right)^2,
\qquad
s_q=\sum_{i>q}a_i\eta_i,
\qquad
\rho_q=(c_q^2+s_q^2)^{1/2},
\tag{2.5}
$$
其中 $c_0=0$。由 (2.2) 的全输出正交性，准确有
$$
\boxed{\|K_{\downarrow}x\|^2
=\sum_{q\ge1}c_q^2\|P_qx\|^2.}
\tag{2.6}
$$
由 (2.3) 及不同 $q$ 的输出仍在正交 $P_q$ 块中，
$$
\|K_{\rm diag}x\|^2
\le\sum_{q\ge0}s_q^2\|P_qx\|^2.
\tag{2.7}
$$
两类输出之间不声称正交。只用三角不等式和二元 Cauchy–Schwarz，即得
$$
\boxed{
\|K_Nx\|\le\sqrt2
\left(\sum_{q\ge0}\rho_q^2\|P_qx\|^2\right)^{1/2}.}
\tag{2.8}
$$

这里每个 $\rho_q$ 都严格为正。对 $q\ge1$，
$$
\boxed{b_q\le\rho_q\le3b_q.}
\tag{2.9}
$$
下界来自 $c_q$ 中的 $i=q-1$ 项。上界可逐项支付：置
$L_q=\sum_{i<q}a_i\alpha_q/\alpha_i$，将 $i=q-1-k$，则
$$
\frac{L_q}{b_q}
\le\sum_{k\ge0}(k+1)^2 16^{-k}
=\frac{1+1/16}{(1-1/16)^3}<2.
\tag{2.10}
$$
这里用 $q/(q-k)\le k+1$ 和 (1.3)。又
$$
s_q\le\frac43a_{q+1}\eta_{q+1}
\le\frac1{12}b_q.
\tag{2.11}
$$
因此 $\rho_q\le c_q+s_q\le L_q+s_q<3b_q$。$q=0$ 只需保留固定正数 $\rho_0=s_0$。

## 3. Y 型的全部真实 Cayley 项

不把 $Y_i^*$ 换成 $N_i^*$。原实际关系给
$$
Y_i^*-N_i^*
=-\eta_i(I+N_i^*)^{-1}N_{i+1}^*,
\qquad \|(I+N_i^*)^{-1}\|\le3.
\tag{3.1}
$$
若 $q>i+1$，由 (2.2) 的下一位版本，
$$
\eta_i\|N_{i+1}^*P_q\|=\frac{\alpha_q}{\alpha_i}.
$$
若 $q\le i+1$，用真实全空间范数 $\|N_{i+1}^*\|=1$。所以对 $q\ge1$，
$$
\begin{aligned}
\|(T_Y^*-T_N^*)P_q\|
&\le3\sum_{i<q-1}a_i\frac{\alpha_q}{\alpha_i}
 +3\sum_{i\ge q-1}a_i\eta_i\\
&\le3(L_q-b_q)+4b_q.
\end{aligned}
\tag{3.2}
$$
连同 $\|K_NP_q\|\le L_q+s_q$，(2.10)–(2.11) 给
$$
\|K_YP_q\|\le4L_q+s_q+b_q<10b_q.
\tag{3.3}
$$
$q=0$ 时，$\|K_NP_0\|\le s_0\le\eta_0/3$，而 (3.1) 的全和至多 $4\eta_0$，故同样得到
$$
\boxed{\|K_YP_q\|\le10b_q\quad(q\ge0).}
\tag{3.4}
$$
因此在真正的块 Banach 空间
$$
\mathcal C_b=
\left\{h:\ P_qh\in\mathcal H\ (q\ge0),\quad
\sum_{q\ge0}b_q\|P_qh\|<\infty\right\}
\tag{3.5}
$$
上，$K_Yh=\sum_qK_YP_qh$ 按 Hilbert 范数绝对收敛，且范数至多右侧的 $10$ 倍。此结论也适用于 N 型。

N 型还有真正较大的 Hilbert 来源空间
$$
\mathcal C_{N,2}=
\left\{h:\sum_{q\ge0}\rho_q^2\|P_qh\|^2<\infty\right\},
\tag{3.6}
$$
其 $K_N$ 延拓由 (2.8) 支付。本文不把 Y 型各列重叠的输出擅自当成 (2.6) 的正交输出。

若希望 Y 型也写成平方和充分条件，任意 $\delta>0$ 下
$$
\boxed{
\sum_{q\ge0}b_q^2(q+1)(\log(q+2))^{1+\delta}
\|P_qh\|^2<\infty
\quad\Longrightarrow\quad h\in\mathcal C_b.}
\tag{3.7}
$$
证明就是对 $q$ 作 Cauchy–Schwarz，并用
$\sum_q[(q+1)(\log(q+2))^{1+\delta}]^{-1}<\infty$。

## 4. 规范来源的总孔截断给实际图收敛

**定理。** 设 $f\in\mathcal H$、$f_0=0$，并令 $h$ 为该实际模型唯一的规范逐行形式解
$$
T^*h=f.
\tag{4.1}
$$
若满足下列对应条件之一：

- N 型：$h\in\mathcal C_{N,2}$；
- Y 型：$h\in\mathcal C_b$；

则总孔截断
$$
h^{\le p}=\sum_{j=0}^{p}\mathsf P_jh
\tag{4.2}
$$
是实际 Hilbert 向量，而且
$$
\boxed{T^*h^{\le p}\longrightarrow f\quad\text{在原 Hilbert 范数中}.}
\tag{4.3}
$$
同时 $y=Sh\in\mathcal H$，且
$$
\boxed{Sh^{\le p}\longrightarrow y.}
\tag{4.4}
$$

**证明。** [R238](R238-actual-slow-formal-inverse-fixed-hole-layers-and-canonical-right-inverses.md) 定理 1.1 已在原 N/Y 权下证明：只要 (4.1) 的输出 $f\in\mathcal H$，每个固定总孔层 $\mathsf P_jh$ 都在 $\mathcal H$。因此 (4.2) 的确是 Hilbert 向量；这一步不由首缺位的局部平方和替代。

$P_q$ 和总孔截断交换。在 (3.6) 的平方和或 (3.5) 的正数和中作支配收敛，得到
$$
h^{\le p}\longrightarrow h
\quad\text{在对应的真实 carry 来源范数中}.
\tag{4.5}
$$
于是 (2.8) 或 (3.4) 给
$$
Kh^{\le p}\longrightarrow \widetilde Kh\in\mathcal H.
\tag{4.6}
$$
该极限与逐行形式 $Kh$ 一致：每个固定整数输出坐标，对 $T^*$、$D^*$ 以及它们之差都只涉及有限个输入整数坐标；总孔截断最终保留这些输入。因此 (4.1) 意味着
$$
D^*h=f-\widetilde Kh\in\mathcal H
\tag{4.7}
$$
是一个真实 Hilbert 向量。

现在才使用纯创建恰好升一个**总物理孔次数**的准确恒等式：
$$
D^*h^{\le p}
=\mathsf P_{\le p+1}(D^*h).
\tag{4.8}
$$
右侧由 (4.7) 在 Hilbert 范数中趋于 $D^*h$。与 (4.6) 相加便得到 (4.3)。没有要求 $h\in\mathcal H$，没有把纯核当真核，也没有交换未证明收敛的完整 $\langle h,Tw\rangle$。

最后，$S$ 在不同首缺位块上的输出正交，并准确满足
$$
\|SP_qh\|=\alpha_q\|P_qh\|.
\tag{4.9}
$$
对 $q\ge1$，由 (2.9) 及 (1.4)，
$$
\frac{\alpha_q}{\rho_q}\le q^2\alpha_{q-1},\qquad
\frac{\alpha_q}{b_q}=q^2\alpha_{q-1}.
\tag{4.10}
$$
右侧有有限上界；$q=0$ 只是一个固定有限比。因此 $S$ 从 (3.6) 或 (3.5) 有界到 $\mathcal H$。(4.5) 给 (4.4)。证毕。

## 5. 真正的形式单位图与 W 的同源结论

令 $G_0=TJ_B$ 为[实际闭关系稿](R271-appendix-actual-formal-division-closed-relation-and-two-range-cores.md)中的有限支撑除法。其最大伴随满足
$$
S G_0^*y=T^*y,
\qquad G_0^*S=T^*.
$$
在定理 4 的条件下，逐行等式与 $T^*S=ST^*$ 给 $T^*y=Sf$。因此
$$
y\in\mathcal D(G_0^*),\qquad G_0^*y=f.
$$
由 (4.3)–(4.4)，图中真实的点
$$
\big(Sh^{\le p},\ G_0^*Sh^{\le p}\big)
=\big(Sh^{\le p},\ T^*h^{\le p}\big)
$$
趋于 $(y,f)$。所以这是 $S\mathcal H$ 在最大形式图中的一条实际核心途径，而不只是闭包值域的一条抽象包含。

对主问题，令
$$
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
$$
已证 $e_0\in N$，故每个 $w\in W$ 都有 $w_0=0$，其规范 $h(w)$ 存在。将定理 4 用于**同一个** $f=w$，得到
$$
\boxed{
\begin{array}{ll}
T=T_N,\quad h(w)\in\mathcal C_{N,2}&\Longrightarrow w=0,\\
T=T_Y,\quad h(w)\in\mathcal C_b&\Longrightarrow w=0.
\end{array}}
\tag{5.1}
$$
因为 (4.3) 给 $w\in\overline{\operatorname{Ran}T^*}=M^\perp$，而 $w\in M$。

这仍是条件结论。本文没有由 $Sw\in\overline{\operatorname{Ran}T^*}$ 推出 $Sw\in\operatorname{Ran}T^*$，也没有证明全部 $W$ 的规范来源满足 (3.5) 或 (3.6)。两道闭包范围核心仍不能无条件合并。

## 6. 新来源尺度及严格扩大

由 (1.2)、(1.4)，
$$
-\log b_q
=2\log q+1400\,16^{q-1}-630\,8^{q-1}+300\,2^{q-1}
\quad(q\ge1),
$$
所以
$$
\boxed{\lim_{q\to\infty}\frac{-\log b_q}{16^q}=\frac{175}{2}=87.5.}
\tag{6.1}
$$
因而对任意 $\theta<175/2$，如果该规范来源的每个首缺位块都在 $\mathcal H$，并且
$$
\|P_qh\|\le C\exp(\theta16^q)
\quad(q\ge0),
\tag{6.2}
$$
则两型都满足 (3.5)，从而 (5.1) 排除相应非零 $w$。这里 $\theta$ 可以是任意有限负数、零或小于 $175/2$ 的正数。相比之下，仅有 $Sh\in\mathcal H$ 允许 $\alpha_q^{-1}$ 级的块增长，其主指数为 $280/3$；本文仍未付清这两者之间的差，也未证明 $Sh(w)\in\mathcal H$。

新图核心确实超出旧的条件 $\sum_q a_q\|P_qh\|<\infty$，即使保留真实输出在 $\mathcal H$。一个直接的两型共同例子是
$$
h=\sum_{q\ge2}\frac{q}{\log(q+1)}e_{2^q-1}.
\tag{6.3}
$$
此处每项的首缺位与总孔数都是 $q$。它满足 (3.5)，但
$$
\sum_q a_q\|P_qh\|
\asymp\sum_{q\ge2}\frac1{q\log(q+1)}=\infty.
\tag{6.4}
$$
另一方面，各 $D^*e_{2^q-1}$ 在不同总孔层，且
$$
\|D^*e_{2^q-1}\|^2
=\sum_{i\ge q}(i+1)^{-4}\le\frac1{3q^3}.
$$
因此
$$
\|D^*h\|^2
\le\frac13\sum_{q\ge2}\frac1{q(\log(q+1))^2}<\infty.
\tag{6.5}
$$
(3.4) 或 (2.8) 已使真实 $Kh\in\mathcal H$，故 $f=T^*h=D^*h+Kh$ 确实在 $\mathcal H$；它的首坐标为零，且 (6.3) 是该 $f$ 的唯一规范形式原像。这样 (6.4) 的严格扩大并未使用一个输出不在 Hilbert 空间的假例子。该 $f$ 属于 $M^\perp$，不将它误作 $W$ 的非零见证。

本文付清的是可由 R238 和真实首缺位 carry 直接复用的一条同源图桥；剩余任务是从实际 $W$ 正交性取得它所需的来源费用，或另付第二道范围核心。
