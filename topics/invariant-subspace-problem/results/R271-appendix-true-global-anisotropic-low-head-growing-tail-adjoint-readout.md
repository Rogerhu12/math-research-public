# R271 附录：原算子的低早孔—增长远孔右逆与完整伴随读数

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文把[增长远孔窗口的真实局部读数](R271-appendix-growing-far-hole-window-low-head-adjoint-readout-with-full-kernel.md)传到原算子 $T_N,T_Y$，而非只停在有限头加纯尾模型。关键是保留初始右逆的实际输出孔数，再将全部跨头 carry 放进已付的指数次数空间，用一个真实右逆作一次精确修正。

对固定早孔上限 $s$，所得成本随允许的远孔数 $N$ 仅为 $\exp[O_s((\log(N+2))^{4/3})]$。这是一族带位置条件的乘积窗口；不声称全部总孔 $\le N$ 输入都有这个成本。完整 $T$ 核投影保留，原 $W$ 的特殊 forcing 尚未被证明属于实际伴随像。

## 1. 原模型、窗口和已付输入

在原边界 Hilbert 空间 $\mathcal H=\ell^2(\mathbb N_0)$ 中，令 $\mathsf P_q$ 为总物理孔数恰等于 $q$ 的投影。两个实际算子分别为
$$
T_N=\sum_{i\ge0}b_i\mathsf N_i,\qquad
T_Y=\sum_{i\ge0}b_i\mathsf N_i(I+\mathsf N_i)^{-1},
\qquad b_i=(i+1)^{-2}.
\tag{1.1}
$$
以下 $T$ 分别取这两个算子，不改变原权。

令 $s,N$ 为任意非负整数，选择
$$
u=N+s+1024,\qquad
m=\lceil\log_2u\rceil,\qquad d=2^m,\qquad
x=48u,\qquad R=x-m,\qquad h=d+R.
\tag{1.2}
$$
于是
$$
m\ge10,\quad u\le d<2u,\quad R\ge0,\quad
x\ge3072+48s,\quad N\le\lfloor x/48\rfloor.
\tag{1.3}
$$
以 $A_m=T|_{\operatorname{span}\{e_0,\ldots,e_{d-1}\}}$ 为原有限头，定义
$$
D_<=\sum_{m\le i<x}b_iE_i,\qquad
D_x=\sum_{i\ge x}b_iE_i,\qquad C=A_m+D_<,
$$
$$
\mathcal L_m=C+D_x=A_m+D_{\ge m},\qquad
A_m^d=0,\qquad C^h=0.
\tag{1.4}
$$
$E_i$ 是第 $i$ 位的物理孔删除算子。将前 $x$ 位视为强头，但不改变其中任何系数。

令
$$
\Pi=\Pi_{s,N}^{(x)}
=P_{\{\text{前 }x\text{ 位孔数}\le s\}}\,
 P_{\{\text{位 }i\ge x\text{ 孔数}\le N\}}.
\tag{1.5}
$$
输入允许在无限远位有支撑；这里只截断两个实际孔计数。

保持前稿的常数
$$
S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
\tau_x=\log\!\left(7\sqrt{2/S_x}\right),
$$
$$
\mathcal B_s(x)=(s+3)\sqrt{2/S_x}\,
                    \exp\!\left(s\tau_x+\tau_x^{4/3}\right).
\tag{1.6}
$$
已有增长窗口定理给出同一个逐层远尾右逆 $\mathcal Q_x$，每次准确增加一个远孔，满足
$$
D_x\mathcal Q_x=I
$$
于所需各层，并给出
$$
G_0=\sum_{k=0}^{h-1}(-C)^k\mathcal Q_x^{\,k+1}\Pi,
\qquad
\mathcal L_mG_0=\Pi,\qquad
\|G_0\|\le\mathcal B_s(x).
\tag{1.7}
$$
这里所有层的真实自然域和高幂费用已在前稿付清；没有改成环境伪逆或逐项标量逆。

另使用 [R239 指数次数右逆附录](R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md) A.11 的改进阈值
$$
\kappa_{**}=2+2\log(3/2)<3.
$$
所以对每个原模型，已经存在一个固定的有界线性算子
$$
G_3:\mathscr X_3\longrightarrow\mathcal H,\qquad TG_3=I_{\mathscr X_3},
$$
$$
\mathscr X_3=
\left\{z:\|z\|_{\mathscr X_3}
=\sum_{q\ge0}e^{3q}\|\mathsf P_qz\|<\infty\right\},
\qquad C_3=\|G_3\|_{\mathscr X_3\to\mathcal H}<\infty.
\tag{1.8}
$$
$G_3,C_3$ 一经选定，就不随 $s,N,m,x$ 改变。这里确实使用 A.11 的阈值；前面较弱的 $2+2\log2$ 不能直接允许 $\kappa=3$。

## 2. 主结论

存在真实 Hilbert 有界算子 $G^{\rm true}_{s,N}:\mathcal H\to\mathcal H$，其输入已乘 $\Pi$，满足
$$
\boxed{
TG^{\rm true}_{s,N}=\Pi,\qquad
\|G^{\rm true}_{s,N}\|
\le\mathcal B^\#_{s,N}
:=\left(1+C_3e^{-40u^4}\right)\mathcal B_s(48u).
}
\tag{2.1}
$$
因此对所有实际 $y\in\mathcal H$，
$$
\boxed{
\|\Pi y\|\le\mathcal B^\#_{s,N}\|T^*y\|.
}
\tag{2.2}
$$
若 $M=\ker T$，则在完整 MP 自然域
$$
f\in\operatorname{Dom}(T^*)^\dagger
=\operatorname{Ran}T^*\oplus M
$$
上，有准确身份
$$
\boxed{
\Pi(T^*)^\dagger f
=(G^{\rm true}_{s,N})^*(I-P_M)f.
}
\tag{2.3}
$$
右边在全部 Hilbert 输入上有唯一的有界延拓，范数不超过 $\mathcal B^\#_{s,N}$。它仍读取完整最小解，保全部原核 forcing。

对每个固定 $s$，
$$
\log\mathcal B^\#_{s,N}
=O_s\!\left(1+(\log(N+2))^{4/3}\right).
\tag{2.4}
$$
常数还可依赖所选原模型的固定 $C_3$。本文不把 (2.4) 改称固定多项式成本。

## 3. 初始右逆的真实输出孔数

证明 carry 修正前，先给出比单纯 $h$ 段支撑更准确的孔数界：
$$
\boxed{
\operatorname{Ran}G_0\subseteq
\mathcal H_{\le q_0},\qquad
q_0=N+s+m+d<4u.
}
\tag{3.1}
$$

由于 $A_m$ 与 $D_<$ 作用于不同张量因子，
$$
C^k=\sum_{a+b=k}\binom{k}{a}A_m^aD_<^b.
\tag{3.2}
$$
非零项必有 $a<d$。对输入窗口 (1.5)，$D_<^b$ 将新增强位中的孔数准确降低 $b$；所以非零项的新强位输出孔数至多 $s-b$。旧 $m$ 位经过任意 $A_m^a$ 后，物理孔数至多 $m$。同时 $\mathcal Q_x^{k+1}$ 将远孔数至多 $N$ 的输入送到远孔数至多
$$
N+k+1=N+a+b+1.
$$
三部分相加，输出总孔数至多
$$
m+(s-b)+(N+a+b+1)
=N+s+m+a+1\le N+s+m+d.
\tag{3.3}
$$
有限求和保持同一支撑界。最后由 $N+s<u$、$m\le u$ 和 $d<2u$ 得 $q_0<4u$。

这个论证没有假定 $A_m$ 只降一个孔，也没有把 Y 型 Cayley 项当作孔齐次算子。两个模型都只使用原有限头不越出前 $m$ 位、$A_m^d=0$ 及纯 $D_<$ 的准确降孔性质。因此 (3.1) 对 N/Y 两者统一成立。

## 4. 所有 carry 片在 $\mathscr X_3$ 中的总预算

[R234 原右逆证明](R234-slow-boundary-right-inverses-on-cubic-hole-degree-space.md) §2 给出原式
$$
T-\mathcal L_m=\sum_{L\ge m}K_L,\qquad
K_L=\mathcal L_{L+1}-\mathcal L_L,
$$
$$
\|K_L\|\le52e^{-770\,16^{L-1}},
\qquad
K_L\mathcal H_{\le q}\subseteq\mathcal H_{\le q+L+1}.
\tag{4.1}
$$
每片仅作用前 $L+1$ 位，级数在 Hilbert 算子范数中收敛。后一个局部支撑条件与小范数一样必要。

对总孔支撑 $\le b$ 的任何向量 $z$，各孔层正交，故
$$
\|z\|_{\mathscr X_3}
\le e^{3b}\sum_{q=0}^{b}\|\mathsf P_qz\|
\le\sqrt{b+1}\,e^{3b}\|z\|.
\tag{4.2}
$$
将 (3.1) 和 (4.1) 代入，得
$$
\|K_LG_0\|_{\mathcal H\to\mathscr X_3}
\le52\mathcal B_s(x)
\sqrt{q_0+L+2}\,
\exp\!\left[3(q_0+L+1)-770\,16^{L-1}\right].
\tag{4.3}
$$
这保留了实际层数的平方根以及指数次数权，未以无权小误差代替带权收敛。

令 $L=m+t$，$t\ge0$，并记 $b=q_0+m+t+1$。因 $u\ge1024$、$q_0<4u$、$m\le u$，
$$
b+1\le6u(t+1).
$$
初等估计给
$$
\log52+\tfrac12\log(b+1)+3b
\le20u(t+1)\le20u\,16^t.
\tag{4.4}
$$
例如 $\log52+\tfrac12\log(6u)\le u$，且 $\log(t+1)\le t$；其余 $3b$ 可用 $18u(t+1)$ 支配。

另一方面，
$$
770\,16^{L-1}=\frac{770}{16}d^4\,16^t
\ge48.125\,u^4\,16^t.
$$
对 $u\ge1024$，$48.125u^4-20u\ge41u^4$，所以 (4.3) 给
$$
\|K_{m+t}G_0\|_{\mathcal H\to\mathscr X_3}
\le\mathcal B_s(x)e^{-41u^4\,16^t}.
\tag{4.5}
$$
全部 $t$ 求和绝对收敛；使用
$\sum_{t\ge0}e^{-41u^4\,16^t}\le2e^{-41u^4}\le e^{-40u^4}$，得到
$$
\boxed{
\|(T-\mathcal L_m)G_0\|_{\mathcal H\to\mathscr X_3}
\le e^{-40u^4}\mathcal B_s(x).
}
\tag{4.6}
$$
因此这个残量确实落在 (1.8) 的真实定义域。极限在 $\mathscr X_3$ 与 $\mathcal H$ 中一致，故它就是原算子差作用，而非另一形式级数。

## 5. 一次精确修正及完整 MP 读数

定义
$$
\boxed{
G^{\rm true}_{s,N}
=G_0-G_3(T-\mathcal L_m)G_0.
}
\tag{5.1}
$$
(4.6) 付清第二项的自然域及范数。由 (1.7)、(1.8)，
$$
\begin{aligned}
TG^{\rm true}_{s,N}
&=TG_0-(T-\mathcal L_m)G_0\\
&=\mathcal L_mG_0=\Pi.
\end{aligned}
\tag{5.2}
$$
这不是近似方程，也无需再迭代。范数估计直接给 (2.1)。

对 (5.2) 取通常 Hilbert 伴随，
$$
\Pi=(G^{\rm true}_{s,N})^*T^*,
\tag{5.3}
$$
得 (2.2)。若 $f\in\operatorname{Ran}T^*\oplus M$，则
$$
T^*(T^*)^\dagger f=(I-P_M)f,
$$
代入 (5.3) 得 (2.3)。

若 $\widetilde G$ 是同一 $\Pi$ 的另一个有界可行右逆，则
$$
\operatorname{Ran}(G^{\rm true}_{s,N}-\widetilde G)\subseteq M,
$$
所以
$$
(G^{\rm true}_{s,N}-\widetilde G)^*(I-P_M)=0.
$$
因此 (2.3) 的有界延拓与可行右逆的选择无关。这里没有预先压缩 $T$ 的完整核，也没有以 $G_0$ 或修正候选代替完整 MP。

最后，$S_x$ 的真实积分界
$$
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3}
$$
使 $\tau_x=O(\log(x+1))$；结合 $x=48(N+s+1024)$ 即得 (2.4)。

## 6. 新范围与原返回接口

旧 R239 指数次数右逆已控制整个固定总孔层，其一般成本为 $e^{\kappa q}$。本文没有改善那个无位置限制的全层常数；新增范围是 (1.5) 的乘积窗口：前约 $48N$ 位只许固定 $s$ 孔，但更远的孔数可达 $N$，代价为 (2.4)。它与纯创建逆的全层指数下界不冲突。

本文真正付清了原 $T-\mathcal L_m$ 的全部跨位 carry，而非只给有限头模型的读数或重复稠密值域。但以下条件仍保持：

1. (2.3) 对原 $T^*$ 的真实像及其标准 MP 自然域成立；它不证明未知的 $W=M\ominus\overline{BM}$ 向量已经进入 $\operatorname{Ran}T^*$。
2. 全部输入上的延拓始终是 $(G^{\rm true}_{s,N})^*(I-P_M)$，不能删除 $I-P_M$，也不能把它改成只投影 $\Pi f$。
3. 原返回列满足的是正向方程，其真实测试还含 $P_{\widehat{\mathscr E}}$、零源旗和完整高返回。这里没有证明该投影保 (1.5) 的窗口，也没有把正向残量乘以 (2.2) 当作返回范数。
4. 一般原同源高出生窗口 $n\asymp Q\gg x$ 与整个 $h$ 段仍不在本窗口内。需要由真实 forcing 或共同配对产生的额外局部化，才能接回该缺口。

所以本结论是原算子上的定量局部伴随读数；普通封口、返回混合配对及 $N=M$ 继续开放。
