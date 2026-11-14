# R236 附录：旧多值图的正则部分、再次中央值域与真实相对估计

日期：2026-11-12。独占作者：critical_kernel。

**状态：完整的实际图域识别与条件等价。** 本稿接 R233、R236。在旧中央算子单射的分支中，把旧不可闭图的多值部分准确商掉，得到新中央闭值域的一个明确图表示。随后将 R236 的“$D_H$ 是否闭”改写为一个实际中央耦合的相对范数估计，并列出两支必须满足的真实算子关系。本稿不判定该相对估计成立与否，不声称排除原慢核。

## A. 设置与固定记号

保留 R236 的实际算子
$$
T=X-Y,\qquad 0\ne M=\ker T,\qquad M\perp CM,
$$
并假设旧中央算子单射：
$$
K=(M\oplus CM)^\perp,\qquad \ker T_K=0.
\tag{A.1}
$$
全部定义域、自然幂、$C$ 自伴性质及共同有界正则器均取 R212、R233、R236 已证明的真实实现。

在正交分解 $H=M\oplus K\oplus CM$ 上，
$$
\operatorname{Dom}T=M\oplus\mathcal D_K\oplus CM,
\qquad
T=
\begin{pmatrix}
0&F&D\\
0&T_K&H_1\\
0&0&0
\end{pmatrix}.
\tag{A.2}
$$
这里 $F,D,H_1$ 全有界，
$$
H_1=C_KF^*C|_{CM},\qquad C_K=C|_K,
$$
$T_K$ 闭、$C_K$ 自伴、单射且稠密像。$D$ 在本稿始终指 (A.2) 的有界外块，不是某个定义域。

置
$$
M_2=\ker T^2,\qquad
N=M\cap\overline{\operatorname{Ran}T^2},\qquad
M_0=M\ominus N.
\tag{A.3}
$$
R233 给 $0\ne N\subset M$。定义
$$
D_H=\{c\in CM:H_1c\in\operatorname{Ran}T_K\},
\qquad J_Hc=T_K^{-1}H_1c.
\tag{A.4}
$$
$J_H$ 是从 $CM$ 到 $K$ 的闭算子；其域不被假定在 $CM$ 中稠密。准确结论是
$$
\overline{D_H}=CM_0.
\tag{A.5}
$$
因此，今后把 $J_H$ 视为从 $CM_0$ 到 $K$ 的闭稠密定义算子，不改变任何原有域向量或取值。

再置
$$
K_N=(N\oplus CN)^\perp=M_0\oplus K\oplus CM_0.
\tag{A.6}
$$
在 $K_N$ 上，R236 的新中央算子记为 $S$，新核与闭像记为
$$
E=\ker S=M_2\ominus N,\qquad
R=\overline{\operatorname{Ran}S}.
\tag{A.7}
$$
已有的精确核图是
$$
\boxed{
E=M_0\oplus
\{(0,-J_Hc,c):c\in D_H\}.
}
\tag{A.8}
$$
双线性形式为 $\mathcal B(u,v)=\langle u,Cv\rangle$，Hilbert 内积对第一变量线性。$C_N=C|_{K_N}$。

下文只在讨论 $M_0\ne0$ 时称“新核非零分支”；$M_0=0$ 的情况保留到第 F 节单独说明。

## B. 旧不可闭图商掉多值部分后，确实得到一个闭算子

R233 中的旧图为
$$
G=FT_K^{-1}:\operatorname{Ran}T_K\subset K\longrightarrow M.
\tag{B.1}
$$
其伴随的完整域和取值为
$$
\operatorname{Dom}G^*=CD_H,\qquad
G^*m=C_KJ_HCm.
\tag{B.2}
$$
因此 $\overline{\operatorname{Dom}G^*}=M_0$；$G$ 在 $K\to M$ 的意义下不可闭，其闭图关系的多值部分正好是 $N$。

令
$$
A_0:D(A_0)=CD_H\subset M_0\longrightarrow K,
\qquad A_0m=C_KJ_HCm.
\tag{B.3}
$$
两个 $C$ 的复合使 $A_0$ 为线性算子。由 $J_H$ 的闭性与 (A.5)，$A_0$ 闭且在 $M_0$ 中稠密定义。定义
$$
\boxed{Q=A_0^*:D(Q)\subset K\longrightarrow M_0.}
\tag{B.4}
$$
因此 $Q$ 是闭稠密定义算子，且
$$
Q^*=A_0,\qquad
Q=CJ_H^*C_K
\tag{B.5}
$$
在相应完整伴随域上成立。式 (B.5) 中左侧的 $C$ 从 $CM_0$ 映到 $M_0$，不会被误认成保持 $M_0$ 的共轭。

### B.1 一个真实最小图识别

在 $\operatorname{Ran}T_K$ 上定义
$$
G_0=P_{M_0}FT_K^{-1}:K\supset\operatorname{Ran}T_K\to M_0.
$$
对 $m\in M_0$，有
$$
m\in D(G_0^*)
\iff
\exists k\in K\ 
\langle P_{M_0}Fx,m\rangle
=\langle T_Kx,k\rangle
\quad(x\in\mathcal D_K).
$$
这与 $m\in D(G^*)$ 完全相同，而且伴随取值一致。所以
$$
G_0^*=A_0.
$$
$D(A_0)$ 在 $M_0$ 中稠密，故 $G_0$ 可闭，并且
$$
\boxed{
\overline{G_0}=Q.
}
\tag{B.6}
$$

原来的多值图因而有准确的正交分解
$$
\boxed{
\overline{\operatorname{Graph}G}
=
\{(k,Qk+n):k\in D(Q),\ n\in N\}
\subset K\oplus M.
}
\tag{B.7}
$$

可直接用闭关系的双重正交补核验 (B.7)。一个向量 $(k,m)$ 在 $\overline{\operatorname{Graph}G}$ 中，当且仅当
$$
\langle m,u\rangle=\langle k,G^*u\rangle
\qquad(u\in D(G^*)).
$$
这些测试 $u$ 都属于 $M_0$，故 $P_Nm$ 完全自由；其余条件恰为
$k\in D(Q)$、$P_{M_0}m=Qk$。

这里的操作是先取真实伴随，再改变伴随的源空间为其域的闭包；没有把一个任意图的正交投影自动当作闭图。

### B.2 固定有界参数图核心

取一个固定共同正则器 $R(t)$，在旧中央空间上的算子记为 $R_K(t)$，并置
$$
S_K(t)=T_KR_K(t)\in B(K),\qquad F_0=P_{M_0}F.
$$
R233 已证明
$$
\overline{\operatorname{Graph}G}
=
\overline{\{(S_K(t)z,FR_K(t)z):z\in K\}}.
$$
结合 (B.6)，或先在原图上作同一正则化再取闭包，得到
$$
\boxed{
\operatorname{Graph}Q
=
\overline{\{(S_K(t)z,F_0R_K(t)z):z\in K\}}.
}
\tag{B.8}
$$
特别，
$$
QS_K(t)=F_0R_K(t)
\tag{B.9}
$$
是全 $K$ 上的真实有界恒等式；$S_K(t)K$ 是 $Q$ 的图核心。

$S_K(t)$ 单射且稠密像：单射由 $T_K,R_K(t)$ 单射给出；稠密像由
$R_K(t)K$ 是 $T_K$ 图核心和 $\overline{\operatorname{Ran}T_K}=K$ 给出。

还可把参数乘以任意固定 $R_K(s)^p$，其中 $p$ 为非负整数：
$$
\operatorname{Graph}Q
=
\overline{\left\{
\left(S_K(t)R_K(s)^pz,\ F_0R_K(t)R_K(s)^pz\right):z\in K
\right\}}.
\tag{B.10}
$$
理由仅是 $R_K(s)^pK$ 在 $K$ 中稠密，以及两个参数算子均有界。

对 $p\ge1$，(B.10) 的第一坐标还在真实 $\operatorname{Dom}T_K^p$ 中。确实，
$R_K(s)$ 保持 $\operatorname{Dom}T_K$、与 $T_K$ 在该域交换，并使 $T_KR_K(s)$ 有界；
由此逐次归纳可得 $R_K(s)^pK\subset\operatorname{Dom}T_K^p$，而额外的
$S_K(t)=T_KR_K(t)$ 与这些有界正则器交换。等价地可把一次 $T_K$ 放到固定
$R_K(t)$ 上，保留右侧 $R_K(s)^p$ 的全部正则阶数。

所以对每个固定有限 $p$，$D(Q)\cap\operatorname{Dom}T_K^p$ 包含一个 $Q$ 图核心。
本稿不把每个有限 $p$ 的这条结论换成未经证明的“同一个全幂核心”，更不由此声称 $D(Q)=K$。

## C. 新中央闭值域的完整图表示

由 $S$ 的 $C_N$ 自伴性质，
$$
R=(C_NE)^\perp.
\tag{C.1}
$$
取 $r=(m,k,c_0)\in K_N$。若 $r\perp C_NE$，首先对 $C_NM_0=CM_0$ 测试，得到 $c_0=0$。

再对 (A.8) 的第二类向量测试：
$$
C_N(0,-J_Hc,c)=(Cc,-C_KJ_Hc,0).
$$
正交条件成为
$$
\langle m,Cc\rangle
=\langle k,C_KJ_Hc\rangle
\qquad(c\in D_H).
\tag{C.2}
$$
置 $u=Cc\in D(A_0)$，(C.2) 就是
$$
\langle m,u\rangle=\langle k,A_0u\rangle.
$$
取复共轭后，这是通常伴随 $A_0^*$ 的定义；因此
$k\in D(Q)$ 且 $m=Qk$。反向逐项代入也成立。

于是
$$
\boxed{
R=\{(Qk,k,0):k\in D(Q)\}.
}
\tag{C.3}
$$
这不是近似图，也不只是一边包含。

式 (C.3) 与 (A.8) 显示，新非退化核及新闭值域由一对互相伴随的真实闭图控制：
$$
J_H:CM_0\supset D_H\to K,\qquad
Q=(C_KJ_HC)^*:K\supset D(Q)\to M_0.
$$

## D. 斜投影的准确域、取值与闭性判据

R236 的闭斜投影沿 $R$ 投到 $E$。用 (A.8)、(C.3) 可直接求出其完整域：
$$
\boxed{
(m,k,c)\in D(\Pi)
\iff
c\in D_H,\quad k+J_Hc\in D(Q).
}
\tag{D.1}
$$
这里 $m\in M_0$ 任意。记 $z=k+J_Hc$，则唯一分解为
$$
(m,k,c)
=
(m-Qz,-J_Hc,c)+(Qz,z,0),
$$
前项在 $E$，后项在 $R$。所以
$$
\boxed{
\Pi(m,k,c)
=
\bigl(m-Q(k+J_Hc),\ -J_Hc,\ c\bigr).
}
\tag{D.2}
$$
特别，在旧低侧 $M_0\oplus K\oplus0$ 上，
$$
D(\Pi)\cap(M_0\oplus K\oplus0)
=M_0\oplus D(Q)\oplus0,
\tag{D.3}
$$
$$
\Pi(m,k,0)=(m-Qk,0,0).
\tag{D.4}
$$

已有的 $C_N$ 自伴性及“非闭直和时全平面谱”仍按 R236 的完整伴随域理解。
本稿不另改该结论，也不把 $\Pi$ 的 $C_N$ 自伴性误写为通常伴随同域。

### D.1 四个等价的实际条件

下列条件等价：

1. $D_H$ 在 $CM$ 中闭，即 $D_H=CM_0$。
2. $J_H:CM_0\to K$ 全域有界。
3. $Q:K\to M_0$ 全域有界。
4. 存在有限常数 $C_0$，对全部 $x\in\mathcal D_K$ 有
   $$
   \boxed{
   \|P_{M_0}Fx\|\le C_0\|T_Kx\|.
   }
   \tag{D.5}
   $$

前两个条件由闭图定理等价。由 (B.3)–(B.5)，$J_H$ 全域有界恰等价于 $A_0$ 全域有界，继而等价于 $Q=A_0^*$ 全域有界。

若 $Q$ 有界，$Q T_Kx=F_0x$ 给 (D.5)。反之，(D.5) 使
$F_0T_K^{-1}$ 在稠密的 $\operatorname{Ran}T_K$ 上有界，故延拓为全 $K$ 上有界算子。
其图闭包是 (B.6) 的 $Q$，因此 $Q$ 全域有界。

这些又与 R236 的以下条件等价：
$$
E+R=K_N\ \text{为闭直和},
\qquad
\Pi\in B(K_N),
\tag{D.6}
$$
以及 $E$ 上的 $\mathcal B_N$ 一致非退化。

式 (D.5) 是一项具体的实际相对估计。它只要求控制耦合输出在 $M/N$ 中的部分；
整个 $F$ 不可能满足同样估计，因为 R233 已证明 $FT_K^{-1}$ 不可闭。

### D.2 相对估计失败时，能够且只能立即得到什么

若 $Q$ 无界，则对任意 $n$ 可选 $x_n\in\mathcal D_K$，使
$$
\|P_{M_0}Fx_n\|=1,\qquad
\|T_Kx_n\|<1/n.
\tag{D.7}
$$
这只是把 (D.5) 的失败归一化。

不能顺便要求 $(x_n)$ 在 $K$ 中有界，也不能要求
$P_{M_0}Fx_n$ 在范数中趋向一个固定非零向量。
后一要求事实上与 $G_0$ 可闭相冲突：若二者同时满足，则
$(T_Kx_n,P_{M_0}Fx_n)\to(0,m_0\ne0)$ 会使 $Q$ 的闭图含非零竖直向量。
故新正则部分的失控与旧图的真正多值部分，具有不同的量词。

## E. 共同正则器和移位只给非齐次图关系

把一个共同正则器或固定单位比算子限制到实际不变子商
$L/N$，其中 $L=(CM)^\perp=M\oplus K$。在 $M_0\oplus K$ 上，它有有界上三角块
$$
\mathcal R=
\begin{pmatrix}
R_0&U_R\\
0&R_K
\end{pmatrix}.
\tag{E.1}
$$
这里 $R_0$ 是该算子在 $M/N$ 上的真实商，而不是无条件的原空间限制。

由于这些全局算子保持 $\overline{\operatorname{Ran}T^2}$，也保持 R236 中的
$R=\overline{\operatorname{Ran}S}$，对 (C.3) 作用后有
$$
R_KD(Q)\subset D(Q),
$$
$$
\boxed{
Q R_Kx=R_0Qx+U_Rx
\qquad(x\in D(Q)).
}
\tag{E.2}
$$
这是非齐次图关系。不能省略 $U_R$ 而称 $Q$ 与两个对角块通常交织。

对 $R(s)\to I$，有
$$
R_K(s)x\to x,\qquad
Q R_K(s)x\to Qx
\qquad(x\in D(Q)),
\tag{E.3}
$$
因为 $R_0(s)\to I$、$U_R(s)\to0$ 强收敛。固定单位比关系
$R(s)=R(t)U(s,t)$ 还给 $R_K(t)D(Q)$ 是 $Q$ 的图核心。

这些结论始终从原有的 $x\in D(Q)$ 出发。它们不推出
$$
R_K(t)K\subset D(Q).
\tag{E.4}
$$
已知无条件入域的分母是 (B.8) 的
$S_K(t)=T_KR_K(t)$；把它替换为 $R_K(t)$，相当于无成本删除一次 $T_K$，
正是当前没有证明的实际值域步骤。

对实际移位也一样。记
$$
A|_{L/N}=
\begin{pmatrix}
A_0^{\rm sh}&U_0\\
0&A_K
\end{pmatrix}.
$$
由 $R$ 的 $A_N$ 不变性，
$$
\boxed{
A_KD(Q)\subset D(Q),\qquad
QA_K=A_0^{\rm sh}Q+U_0
\quad\text{于 }D(Q).
}
\tag{E.5}
$$
本节的 $A_0^{\rm sh}$ 不同于 (B.3) 的伴随参数算子 $A_0$。

## F. $N=M$ 分支中的真实稠密像与单射

若 $N=M$，则 $M_0=0$，由 (A.5) 得
$$
D_H=\{0\},\qquad M_2=M.
\tag{F.1}
$$
此时 $Q$ 是从 $K$ 到零空间的零算子，新中央约化就是旧中央约化。

该分支还迫使两个旧有界耦合满足
$$
\boxed{
\overline{\operatorname{Ran}F}=M,\qquad
\ker H_1=0.
}
\tag{F.2}
$$
证明如下。若 $c\in\ker H_1$，则 $H_1c=0\in\operatorname{Ran}T_K$，
故 $c\in D_H=\{0\}$。所以 $H_1$ 单射。由
$H_1=C_KF^*C$ 得 $\ker F^*=0$，即 $F$ 稠密像。

因此，$N=M$ 不只是“多值部分很大”：它要求整个有界耦合 $F$ 稠密地覆盖原核，
而镜像耦合 $H_1$ 单射，其非零输出全部避开真实 $\operatorname{Ran}T_K$。
这与 $\operatorname{Ran}T_K$ 稠密或 $H_1$ 非紧没有逻辑冲突；即使两个算子值域都稠密，也不能自动推出非零交集。

本稿未证明 $\ker F=0$，未证明 $\overline{\operatorname{Ran}H_1}=K$，
也未把稠密算子值域的交集当成自动稠密。

## G. $N\subsetneq M$ 且图域闭时，出现一个真实有界单射镜像交织

现在假设 $M_0\ne0$，并假设第 D 节的等价条件成立。于是 $D_H=CM_0$，
$J_H$ 全域有界。

定义
$$
\delta:CM_0\longrightarrow N,\qquad
\delta c=Dc-FJ_Hc.
\tag{G.1}
$$
这确实是有界且取值在 $N$ 的实际算子。对
$$
h(c)=(0,-J_Hc,c)\in M_2
$$
用 (A.2) 得
$$
Th(c)=(Dc-FJ_Hc,0,0).
\tag{G.2}
$$
R236 的 $TM_2\subset N$ 支付了值域断言。

若 $\delta c=0$，则 $Th(c)=0$，故 $h(c)\in M$。而 $h(c)\perp M$，于是 $h(c)=0$，
特别 $c=0$。因此
$$
\boxed{\delta\ \text{有界且单射}.}
\tag{G.3}
$$

令 $A_{CM_0}$ 是 $A$ 在旧末块中对 $CM_0$ 的真实不变限制。
它存在，因为 $D_H$ 在该末块移位下不变，且 $D_H=CM_0$；也可由
$N\subset M$ 的不变旗及 $A$ 的 $C$ 对称性直接核对。
若 $A_{M_0}$ 是实际子商 $M/N$ 上的移位，则
$$
A_{CM_0}=C A_{M_0}^*C.
\tag{G.4}
$$

$AM_2\subset M_2$，且 $Ah(c)$ 与 $h(A_{CM_0}c)$ 的末坐标相同。
由 R233 的 $M_2\cap L=M$，二者之差在 $M$ 中。对该差作用 $T$，
再用真实域交换 $TA=AT$，得到
$$
\boxed{
\delta A_{CM_0}=A|_N\,\delta.
}
\tag{G.5}
$$
所以 $N$ 含有一个与 $M/N$ 的镜像伴随移位相交织的有界单射像。

设 $N_0=\overline{\delta(CM_0)}$。则 $N_0$ 是非零闭 $A$ 不变子空间，
$\delta:CM_0\to N_0$ 单射且稠密像。这里使用 R140 §§1–3 已证明的实际 Haar 不变子商结论：相应 $A_Q$ 单射、稠密像且拟幂零；其中单射性由 R23 的实际归一化高幂逼近经不变旗的 lift 证明，并非从全 $H$ 单射直接下推。非零有限维空间上的单射算子可逆，与拟幂零矛盾。因此 $CM_0$ 与 $N_0$ 都是无限维的。

此外，(G.1) 的 $M_0$ 分量必须严格为零：
$$
\boxed{
P_{M_0}D|_{CM_0}
=F_0J_H
=QH_1|_{CM_0}.
}
\tag{G.6}
$$
最后一个等号只在已证明的真实域中使用：
$T_KJ_Hc=H_1c$ 且 $QT_Kx=F_0x$ 对 $x\in\mathcal D_K$ 成立。

式 (G.5)–(G.6) 没有给 $\delta$ 下方有界，也没有给 $N_0=N$。
不能把有界单射交织、两边的精确四次型，或其稠密像，单独升级为有界逆。
目前尚未由这些关系得到与实际模型不相容的结论。

## H. 准确留下的分叉

本附录把几个不同问题分开：

- 旧不可闭 $G$ 的多值部分是 $N$；商掉它后的 $Q$ 始终是闭稠密定义算子。
- 新闭值域恰为 $\operatorname{Graph}Q$；新斜投影的完整域由 (D.1) 给出。
- 新投影是否有界，恰是实际相对估计 (D.5)，并不跟随共同正则器的图核心。
- 若 $N=M$，必须有 (F.2) 的稠密耦合与单射镜像，并且没有非零二阶广义核新增向量。
- 若 $N\subsetneq M$ 且 (D.5) 成立，必须有 (G.3)–(G.6) 的真实镜像交织与精确块消去。
- 若 $N\subsetneq M$ 且 (D.5) 失败，只能立即得到 (D.7)；不能附送有界输入序列或固定非零竖直极限。

下一项需要的是实际 $M$ 方程提供的上界、反向成本或可控原像，
足以决定 (D.5) 或 $N=M$。本稿没有用全空间循环性代替限制值域，
没有把形式除法当有界，也没有把闭斜投影的全平面谱当成排核。
