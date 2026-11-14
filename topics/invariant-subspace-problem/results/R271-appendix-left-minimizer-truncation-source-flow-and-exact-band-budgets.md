# R271 附录：左最小前驱的相容截断、原源 Riccati 递推与子窗两费用

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2116。

状态：**已证明。** 固定同一个原有限头和一个顶部源，本文证明其完整左最小前驱的每个较低物理截断仍是诱导源的真正左最小前驱。由此给出逐孔源流的准确正能量递推；在包含完整未来窗的每个切口，平坦链恰为同一原前驱的未来带投影，裸链也有准确投影式。两种费用的累计预算始终保持这个原源，不重新选择各子窗的向量。

本稿是左侧的实际源递推，与[已有右修复 Riccati](R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md)的空间和度量不同。没有证明统一耗散率或无权 $N=M$。

## 1. 原空间与嵌套零源核

固定原 $m\ge5,d=2^m$，记 $A=A_m,D=D_m,L=A+D$，全部孔投影均保持这个 $m$。对合法整数 $4d\le p\le e^{d^3/4}$，取
$$
V_p=\mathcal H_{\le p}^{(m)}\cap
\ker(P_{\le p-1}^{(m)}L),
\qquad E_pv=Av_p,
\tag{1.1}
$$
$$
\mathscr R_p=\bigoplus_{i=0}^{d-2}e_i
E_{d-i-1,p},\qquad E_{h,p}=\ker D^h\cap\mathcal H_p.
\tag{1.2}
$$
[原左源 Gram](../notes/2026-11-13-left-source-gram-and-paid-actual-dual-source-1cf.md)已证明 $E_p:V_p\to\mathscr R_p$ 满射并有有界右逆。因此
$$
J_p=E_pE_p^*>0,\qquad L_p=J_p^{-1},\qquad
\mu_p(r)^2=\|E_p^\dagger r\|^2=\langle L_pr,r\rangle.
\tag{1.3}
$$
本稿 $L_p$ 是左源度量，不是 $L=A+D$。

零源空间准确为
$$
V_{0,p}:=\ker E_p=\ker L\cap\mathcal H_{\le p}^{(m)}.
\tag{1.4}
$$
原因是 $V_p$ 已使所有低于 $p$ 的输出为零，唯一可能的剩余输出是第 $p$ 层的 $Av_p$。因此若 $s\le p$，将向量在高孔处补零后有
$$
V_{0,s}\subseteq V_{0,p}.
\tag{1.5}
$$

## 2. 每个物理截断仍是真正的左最小者

取一个固定的原顶部源 $r_q\in\mathscr R_q$，令
$$
v=E_q^\dagger r_q.
$$
对每个合法 $p\le q$，定义同一个向量所诱导的源
$$
r_p=Av_p.
\tag{2.1}
$$
则
$$
\boxed{P_{\le p}^{(m)}v=E_p^\dagger r_p.}
\tag{2.2}
$$

证明：由于 $L$ 仅保持或降低一孔，$P_{\le p}v$ 满足 $V_p$ 的所有低输出方程，顶部源是 (2.1)。又 $v\perp V_{0,q}$，而 (1.5) 给 $V_{0,p}\subseteq V_{0,q}$。对任意 $z\in V_{0,p}$，
$$
\langle P_{\le p}v,z\rangle=\langle v,z\rangle=0.
$$
所以该截断是同源可行仿射空间中唯一与零源核正交的向量，即真正最小前驱。证毕。

特别，对于合法 $s\le p\le q$，有准确的相容性和正能量差
$$
\boxed{
P_{\le s}E_p^\dagger r_p=E_s^\dagger r_s,
\qquad
\mu_p(r_p)^2-\mu_s(r_s)^2
=\sum_{n=s+1}^{p}\|v_n\|^2.
}
\tag{2.3}
$$
这是同一个 $r_q$ 决定的源族；不把两个独立选取的最小者作比较。

## 3. 完整联合旗中的逐孔左 Riccati

设 $p-1,p$ 均合法。第 $p$ 层的完整顶输入旗为
$$
\mathscr X_p=\bigoplus_{i=0}^{d-1}e_iE_{d-i,p}.
\tag{3.1}
$$
原逐头短核条件说明每个 $v\in V_p$ 的 $v_p$ 都在 (3.1) 内。定义保留真正受限伴随的两个算子
$$
A_p=A|_{\mathscr X_p}:\mathscr X_p\to\mathscr R_p,
\qquad
D_p=D|_{\mathscr X_p}:\mathscr X_p\to\mathscr R_{p-1}.
\tag{3.2}
$$
第二个值域由删除降低核阶一而成立；头 $e_{d-1}$ 上的 $E_{1,p}$ 被删除杀掉。

$A_p$ 满射。具体地，令
$$
A_0=A|_{e_0^\perp}:e_0^\perp\to\operatorname{Ran}A.
$$
原头严格上三角且第一条上对角线非零，所以 $A_0$ 是同构；其逆的第 $j$ 个头坐标只读取源头 $i\ge j-1$，这些源的核阶至多 $d-j$。故
$$
(A_0^{-1}\otimes I)\mathscr R_p\subseteq\mathscr X_p,
\qquad A_p(A_0^{-1}\otimes I)r=r.
\tag{3.3}
$$

给定顶向量 $x\in\mathscr X_p$，所有以它为第 $p$ 层的 $V_p$ 向量，其低部分恰是 $V_{p-1}$ 中源为 $-D_px$ 的可行向量。反向拼合亦成立，因为第 $p-1$ 层的方程正是
$A v_{p-1}+D_px=0$。因此
$$
\boxed{
\mu_p(r)^2
=\min_{\substack{x\in\mathscr X_p\\A_px=r}}
\left[\|x\|^2+\langle L_{p-1}D_px,D_px\rangle\right].
}
\tag{3.4}
$$
这里下半部也作真正完整最小化，不删任何首头自由坐标。

置
$$
W_p=I_{\mathscr X_p}+D_p^*L_{p-1}D_p\succeq I.
\tag{3.5}
$$
加权最小原像的准确公式给
$$
\boxed{
J_p=A_pW_p^{-1}A_p^*,
\qquad
X_p=W_p^{-1}A_p^*J_p^{-1}.
}
\tag{3.6}
$$
其中 $X_p r$ 就是 $E_p^\dagger r$ 的真实第 $p$ 层。所有逆在固定参数下有界严格正；不能将 $D_p^*L_{p-1}D_p$ 改成未经受限的环境压缩逆。

定义实际向下源流
$$
T_p=-D_pX_p:\mathscr R_p\to\mathscr R_{p-1}.
\tag{3.7}
$$
对 (2.1) 的同源族，有 $r_{p-1}=T_pr_p$。同时
$$
\boxed{X_p^*X_p+T_p^*L_{p-1}T_p=L_p.}
\tag{3.8}
$$
这是准确的正能量恒等式，不仅是一个未指定常数的比较。

若 $T_{s\leftarrow q}=T_{s+1}\cdots T_q$，且 $T_{q\leftarrow q}=I$，则逐次代入给
$$
\boxed{
L_q-T_{s\leftarrow q}^*L_sT_{s\leftarrow q}
=\sum_{p=s+1}^{q}
T_{p\leftarrow q}^*X_p^*X_pT_{p\leftarrow q}.
}
\tag{3.9}
$$
它为全部子窗保留同一个原输入 $r_q$；并未断言 $T_p$ 在普通源范数中收缩。

## 4. 同一头的首头自由变量可再准确消去

令 $\iota_0$ 是第零源头
$e_0E_{d-1,p-1}\hookrightarrow\mathscr R_{p-1}$ 的等距嵌入，令
$$
R_p^{\rm tail}=(D:\mathcal H_p\to\mathcal H_{p-1})^\dagger,
\qquad
K_{p-1}=(R_p^{\rm tail}|_{E_{d-1,p-1}})^*
(R_p^{\rm tail}|_{E_{d-1,p-1}}).
\tag{4.1}
$$
这里 $R_p^{\rm tail}$ 是整个孔层上的真正尾 MP 逆；当输入属于所列短核旗时，它的输出自动属于 $E_{d,p}$。
它正是[首源头右度量](R239-appendix-first-source-head-metric-splitting-and-middle-band-schur-amplification.md)的共同块。

给定源 $r\in\mathscr R_p$，置
$$
x_0=(A_0^{-1}\otimes I)r,\qquad b=-D_px_0.
$$
全部顶向量为 $x=x_0+e_0f$，$f\in E_{d,p}$。因两个头部分正交，且固定 $z=Df$ 后真正最小 $f$ 是 $R_p^{\rm tail}z$，(3.4) 等价于
$$
\boxed{
\mu_p(r)^2=\|x_0\|^2+
\min_{z\in E_{d-1,p-1}}
\left[\langle K_{p-1}z,z\rangle
+\langle L_{p-1}(b-\iota_0z),b-\iota_0z\rangle\right].
}
\tag{4.2}
$$
特别，最优 $f$ 的 primitive 自由部分准确为零。

写
$$
M_0=K_{p-1}+\iota_0^*L_{p-1}\iota_0>0,
$$
则
$$
\boxed{
z=M_0^{-1}\iota_0^*L_{p-1}b,
\quad
r_{p-1}=b-\iota_0z,
}
\tag{4.3}
$$
以及
$$
\boxed{
\mu_p(r)^2
=\|x_0\|^2+
\left\langle
\left[L_{p-1}-L_{p-1}\iota_0M_0^{-1}\iota_0^*L_{p-1}\right]b,b
\right\rangle.
}
\tag{4.4}
$$
这保留完整左交叉块。它是在逐孔递推中对真正首头自由坐标的最小化，不是把物理首源头直接置零，也不是把 (4.4) 的方括号误认成 $L_{p-1}$ 的普通头压缩。

## 5. 每个完整未来窗的平坦链是准确正交投影

仍固定 §2 的 $v=E_q^\dagger r_q$。取合法 $p$，并要求
$$
p+d\le q.
\tag{5.1}
$$
在第 $p$ 个原完整右旗中，写 $F_p:\ker S_p\to\mathscr R_p$ 为首输出，$G_p=F_pF_p^*$ 为完整右源 Gram。令
$$
\mathcal U_{f,p}=\operatorname{Ran}F_p^*
=\ker S_p\ominus\ker F_p
$$
嵌入原物理未来带 $[p+1,p+d]$，记该带中的正交投影为 $P_{f,p}$。

定义同一个诱导源的平坦链
$$
c_p^\flat=F_p^*L_pr_p.
$$
则有准确身份
$$
\boxed{c_p^\flat=P_{f,p}P_{[p+1,p+d]}^{(m)}v.}
\tag{5.2}
$$

证明：对任意 $h\in\mathscr R_p$，左最小前驱 $E_p^\dagger h$ 与完整右最小链 $F_p^\dagger h$ 的差是支持在 $\le p+d$ 的完整零源 $L$ 核。由 (5.1) 它属于 $V_{0,q}$，故与 $v$ 正交。因此用 (2.2)，
$$
\langle L_pr_p,h\rangle
=\langle P_{\le p}v,E_p^\dagger h\rangle
=\langle P_{[p+1,p+d]}v,F_p^\dagger h\rangle.
$$
即 $L_pr_p=(F_p^\dagger)^*P_{[p+1,p+d]}v$。再施加 $F_p^*$，利用
$F_p^*(F_p^\dagger)^*=P_{f,p}$，便得 (5.2)。证毕。

所以无需任何 carry 误差就有
$$
\boxed{\lambda_{{\rm flat},p}(r_p)^2
=\|P_{f,p}P_{[p+1,p+d]}v\|^2
\le\|P_{[p+1,p+d]}v\|^2.}
\tag{5.3}
$$
这不是把 $r_p^\flat$ 换成任意较小的源；$c_p^\flat$ 就是原完整左、右 Gram 定义的那个变换源的最小右链。

## 6. 同一未来带的裸投影与累计两费用

令 $P_{L,p}$ 为原右旗低出生投影，$Z_p=\ker S_{L,p}$，并记
$$
\mathcal U_{b,p}=Z_p\ominus\ker(F_p|_{Z_p}),
\qquad P_{b,p}=P_{\mathcal U_{b,p}}.
$$
则同一个未来带还有
$$
\boxed{
a_p(r_p)=-P_{b,p}P_{L,p}P_{[p+1,p+d]}v.
}
\tag{6.1}
$$

先核对可行性。每个 $v_{p+t}$ 逐头属于 $E_{d-i,p+t}$。低出生部分的核高度至少为 $t$，故其非零头指标自动满足 $i\le d-t$，正好落在原低输入联合旗。高出生部分在第 $t$ 段属于 $\ker D^{t-1}$；$A$ 保持该核阶，而下一段的高部分经 $D$ 仍属于 $\ker D^{t-1}$。因此高部分不产生低出生输出。原方程
$Av_{p+t}+Dv_{p+t+1}=0$ 于是给
$$
P_{L,p}P_{[p+1,p+d]}v\in Z_p.
$$
首段没有高出生分量，其首输出为
$$
Dv_{p+1}=-Av_p=-r_p.
$$
再投到真正裸最小者空间 $\mathcal U_{b,p}$ 即得 (6.1)。所以
$$
\boxed{\alpha_p(r_p)^2\le\|P_{[p+1,p+d]}v\|^2.}
\tag{6.2}
$$

置 $\chi_p(r_p)^2=\alpha_p(r_p)^2+\lambda_{{\rm flat},p}(r_p)^2$。两投影未被声称相互正交；正确的合计界是
$$
\boxed{\chi_p(r_p)^2\le2\|P_{[p+1,p+d]}v\|^2.}
\tag{6.3}
$$
对任意合法 $s\le t\le q-d$，每个物理孔层在这些长度 $d$ 的窗中出现至多 $d$ 次，故
$$
\boxed{
\sum_{p=s}^{t}\chi_p(r_p)^2
\le2d\,\|P_{[s+1,t+d]}v\|^2
\le2d\left[\mu_q(r_q)^2-\mu_s(r_s)^2\right].
}
\tag{6.4}
$$
最后一步用 (2.3)，并保留 $t+d\le q$。于是原顶部源的真实左能量下降同时支付全部子窗的两费用平方和。

## 7. 与中间自由带问题的关系和剩余量

深源合法最小补全所得 $\widehat v=E_q^\dagger\widehat r$ 仍满足本稿全部公式。因此可以对同一补全后的原源作严格相容的物理子窗递推，保留 (3.8)–(3.9) 的每一项正能量，不把下一孔层重选成另一个任意源。

式 (4.3) 还明确给出每一步由首头自由坐标产生的真实反馈：它通过 $K_{p-1}+\iota_0^*L_{p-1}\iota_0$ 的正逆，保留全部左交叉。该逆与中间自由带输出切分产生的 Schur 反馈均不能被省略。

(6.4) 是实际耗散预算，不是耗散下界。尚未证明左能量必须在指定长度内下降固定比例，也未证明原两费用足以用温和常数控制 $\mu_p(r_p)^2$。因此本稿不从子窗预算自动推出 $N=M$，也没有放宽普通复 Hilbert ISP 的完成标准。
