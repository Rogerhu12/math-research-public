# R239 附录：完整源 Schur 坐标中的增长头观测与裸项补方向

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。
状态：以下完整零源旗、源坐标逆、全零源 Schur 消元及增长头测试的坐标身份已证明。未给真实全源的温和三 Gram 上界。

本文继续[R271 完整左 primitive 坐标](R271-appendix-full-left-primitive-coordinates-and-boundary-schur.md)和[R239 增长头观测](R239-appendix-growing-head-intertwining-and-full-short-kernel-observation.md)。[R271 源 jets 与全部自由旗](R271-appendix-source-primitive-jets-and-sequential-right-chain.md)已经给出全部零源旗、强制坐标及一次 Schur 度量；本文 §§2–4 保留完整证明并以 Γ、𝓖 重述这些共同接口，不将其重复登记为新结论。新增部分是将增长头测试准确写入同一度量，给出受限上界、完整右能量下界及由裸项支付的明确补方向，并记录原头作用与降孔的收缩身份。

## 1. 原记号

固定原 $m\ge5,d=2^m$ 及 $4d\le q\le e^{d^3/4}$。写 $A=A_m,D=D_m$、$P_0=P_{\ker D}$、$K_n=\ker D\cap\mathcal H_n$。

沿 R271，primitive 坐标空间、完整左坐标化及其度量为
$$
\mathscr P_q=\mathbb C^d\otimes\bigoplus_{n=0}^{q}K_n,
\quad
\mathcal E p=P_{\le q}\sum_{t=0}^{d-1}(-A)^tQ_tp,
\quad
\mathcal D=\mathcal E^*\mathcal E\succeq I.
$$
$\mathcal E:\mathscr P_q\to\mathscr V_q$ 为有界双射，逆为 $P_0$。
$Q_t$ 是同一个原尾上顺次单步 Moore--Penrose 原像，对 primitive 输入有
$$
DQ_t=Q_{t-1},\quad P_0Q_t=0\ (t>0),\quad Q_0=I.
$$
真正源映射为
$$
\mathcal B=E_q\mathcal E,
\qquad
\mathcal Bp=\sum_{t=0}^{d-2}(-1)^tA^{t+1}Q_tp_{q-t}.
\tag{1.1}
$$
完整源空间仍是原 $\mathscr R_q$，源 Gram 为 $J_q=E_qE_q^*$，完整右 Gram 为 $G_q=F_{\rm flag}F_{\rm flag}^*$。下文用 $\mathcal G$ 表示新的坐标 Schur 补，与 $G_q$ 区别。

## 2. 全部零源坐标的准确旗

**定理。** 原完整零源坐标为
$$
\boxed{
\mathscr K_q:=\ker\mathcal B
=\bigoplus_{n=0}^{q}
\left(\ker A^{q-n+1}\otimes K_n\right).
}
\tag{2.1}
$$
当指数至少为 $d$ 时，头因子为整个 $\mathbb C^d$。

证明。若 $\mathcal Bp=0$，则 $v=\mathcal E p$ 是支撑在 $[0,q]$ 的整个 $L=A+D$ 核向量。顶端给 $Av_q=0$。再由
$$
Av_n=-Dv_{n+1}
$$
向下归纳，因头尾交换，有
$$
A^{q-n+1}v_n=0.
$$
$P_0$ 与 $A$ 交换，所以 $p_n=P_0v_n\in\ker A^{q-n+1}$。

反之，若右侧的旗成立，完整核展开中从第 $n$ 层出发的第 $t$ 项为 $(-A)^tQ_tp_n$。当 $n+t>q$ 时，$t\ge q-n+1$，所以这一项逐项为零。故完整核展开没有 $q$ 以上输出，$\mathcal E p$ 本身是整个 $L$ 核，因而 $\mathcal Bp=0$。证毕。

原 $A$ 严格上三角且第一条上对角线处处非零，因此
$$
\ker A^\ell=\operatorname{span}\{e_0,\ldots,e_{\ell-1}\}
\quad(1\le\ell\le d).
\tag{2.2}
$$
定义完整独立源坐标的物理正交补
$$
\mathscr U_q=\mathscr K_q^\perp
=\bigoplus_{t=0}^{d-2}
\left(H_{\ge t+1}\otimes K_{q-t}\right),
\quad
H_{\ge t+1}=\operatorname{span}\{e_{t+1},\ldots,e_{d-1}\}.
\tag{2.3}
$$
它只包含最后 $d-1$ 个 primitive 孔层，但还明确删掉每层的低头零源旗。R271 的末段 Schur 只消去了全部低孔坐标；这里精确识别它尚留着的那部分核。

## 3. 不用尾右逆的完整源坐标逆

对 $0\le t\le d-2$，令
$$
C_t=
\left(A^{t+1}|_{H_{\ge t+1}}:
H_{\ge t+1}\longrightarrow H_{\le d-t-2}\right)^{-1}.
\tag{3.1}
$$
这个方阵可逆：在原基中其对应对角线是连续 $t+1$ 个非零第一上对角线权的乘积。它是实际头逆，不隐去其范数。

原顺次最小原像满足全部准确身份
$$
\boxed{P_0D^tQ_s|_{K_{q-s}}=\delta_{ts}I}
\tag{3.2}
$$
（非零时输出在 $K_{q-t}$）。若 $t<s$，用 $D^tQ_s=Q_{s-t}$ 再用 $P_0Q_{s-t}=0$；若 $t>s$，剩余 $D$ 杀掉 primitive 输入。

将 (3.2) 用于 (1.1)，得到
$$
\boxed{P_0D^t\mathcal Bp=(-1)^tA^{t+1}p_{q-t}.}
\tag{3.3}
$$
对于原完整源 $r\in\mathscr R_q$，其 $P_0D^tr$ 的头支撑确在 $H_{\le d-t-2}$：更高头的允许尾核阶不超过 $t$，所以已经为零。因此可以定义
$$
\boxed{
(\Gamma_qr)_t=(-1)^tC_tP_0D^tr,
\qquad 0\le t\le d-2.
}
\tag{3.4}
$$
这是到 (2.3) 的真实有界映射，且
$$
\|\Gamma_q\|^2
\le\sum_{t=0}^{d-2}\|C_t\|^2\|D_m\|^{2t}.
\tag{3.5}
$$
该明确界不含 $q$，但可能含很大的实际头逆。

记 $B_U=\mathcal B|_{\mathscr U_q}$。由 (3.3) 有
$$
\boxed{\Gamma_q\mathcal B=P_{\mathscr U_q}.}
\tag{3.6}
$$
又 $\mathcal B$ 已到整个 $\mathscr R_q$ 满射，故
$$
\boxed{B_U\Gamma_q=I_{\mathscr R_q},\qquad
\Gamma_qB_U=I_{\mathscr U_q}.}
\tag{3.7}
$$
所以 $B_U$ 为有界双射，$\Gamma_q$ 是它的完整逆。不同 $Q_tK_{q-t}$ 的物理 Gram 一般不正交；本节没有用 (3.2) 把完整源内积改成系数平方和。

## 4. 消去所有零源后的真正 Schur 补

按 $\mathscr P_q=\mathscr K_q\oplus\mathscr U_q$ 写
$$
\mathcal D=
\begin{pmatrix}D_{KK}&D_{KU}\\D_{UK}&D_{UU}\end{pmatrix}.
$$
$D_{KK}\succeq I$，故其逆有界。定义
$$
\boxed{\mathcal G_q=D_{UU}-D_{UK}D_{KK}^{-1}D_{KU}\succeq I.}
\tag{4.1}
$$
该式也可分两次取得：先用 R271 的 $D_{\rm eff}$ 消去低孔空间，再在末段中按 (2.1) 消去剩余零源头旗。二者相同，因为同一正二次型先对低孔、再对末段零源变量取最小，等于一次对其正交直和取最小。

给定原源 $r$，独立坐标准确为 $a=\Gamma_qr$。最小左原像的全部 primitive 坐标为
$$
\boxed{
p=(-D_{KK}^{-1}D_{KU}a,\ a).
}
\tag{4.2}
$$
其真实左费用与源 Gram 因而满足
$$
\boxed{
\mu_q(r)^2=\langle\mathcal G_q\Gamma_qr,\Gamma_qr\rangle,
\qquad
J_q=B_U\mathcal G_q^{-1}B_U^*,
\qquad
J_q^{-1}=\Gamma_q^*\mathcal G_q\Gamma_q.
}
\tag{4.3}
$$
没有将被消去的坐标置零，也没有以 $\mathcal G_q\succeq I$ 代替其上界。


### 4.1 顶端 primitive 层的度量准确是单位

若 $p$ 只在第 $q$ 个 primitive 孔层非零，则 $\mathcal E p=p$，因为全部 $t\ge1$ 项已在 $q$ 以上。因此 $\mathcal C_Lp=0$，原 $\mathcal D=I+\mathcal C_L^*\mathcal C_L$ 在这整个顶层上是单位，且与其余坐标的交叉块为零。消去零源旗只去掉其中的第零头，不改变这个事实。所以
$$
\boxed{\mathcal G_q=I_{H_{\ge1}\otimes K_q}\oplus\mathcal G_{q,+}.}
\tag{4.4}
$$
对任意原源的 $a=\Gamma_qr=(a_0,a_+)$，准确有
$$
\mu_q(r)^2=\|a_0\|^2+\langle\mathcal G_{q,+}a_+,a_+\rangle,
\qquad P_0r=Aa_0.
\tag{4.5}
$$
由于原最后第一上对角线为一，第 $d-2$ 个源头只读取 $a_0$ 的最后一个头坐标，故
$$
\boxed{\|(a_0)_{d-1}\|
=\|(P_0r)_{d-2}\|\le\|r\|\le\|D_m\|\alpha_q(r).}
\tag{4.6}
$$
这是原裸源已经支付的一个真实补方向；没有把整个 $a_0$ 的头逆范数省掉。

## 5. 完整三 Gram 问题在独立坐标中的准确形式

令 $J_{{\rm bare},q}$ 为原裸低链源 Gram，使
$\alpha_q(r)^2=\langle J_{{\rm bare},q}^{-1}r,r\rangle$。定义
$$
\mathcal F_q=B_U^*J_{{\rm bare},q}^{-1}B_U,
\qquad
\mathcal H_q=\Gamma_qG_q\Gamma_q^*.
\tag{5.1}
$$
二者均为原完整 Hilbert 空间中的正算子。对 $a=\Gamma_qr$，由 (4.3)，
$$
\boxed{
\alpha_q(r)^2=\langle\mathcal F_qa,a\rangle,
\quad
\lambda_q(G_qJ_q^{-1}r)^2
=\langle\mathcal H_q\mathcal G_qa,\mathcal G_qa\rangle.
}
\tag{5.2}
$$
因此全源三 Gram 估计准确等价于
$$
\boxed{
\mathcal G_q\preceq C_m
\left(\mathcal F_q+\mathcal G_q\mathcal H_q\mathcal G_q\right).
}
\tag{5.3}
$$
若只需原真实来源，则只须 (5.3) 的二次型在对应的 $a=\Gamma_qr(w)$ 或已付同源规范坐标上成立。它不要求先证明整个环境版本。

原两侧窄通量并没有在这里消失。例如对已付的
$$
r_{\rm two}=\mathsf f(I+\mathcal Q)^{-1}
 B_A^*(H^{\rm two})^{-1}\overline f,
$$
其独立坐标必须仍按同一公式取
$$
\boxed{
a_{\rm two}^{\rm prim}
=\Gamma_q\mathsf f(I+\mathcal Q)^{-1}
 B_A^*(H^{\rm two})^{-1}\overline f.
}
\tag{5.4}
$$
没有以旧有效源 $\sigma$、一个环境向量或 $P_{\mathscr G}w$ 替换真实 $\overline f$。

## 6. 增长头测试进入同一 Schur 坐标

取增长头稿中任一已付参数范围。以下把其低头位数写作 $s$，维数为 $K=2^s$，避免与源 $r$ 混淆。设其输入闭 Hilbert 空间为
$$
\mathscr Z=\ker(A_s+D_m)\cap(H_s\otimes\mathcal H_{\le q}^{(m)}),
$$
等距高块嵌入为 $U=H_{m,s}\otimes I$，精确修正为 $\mathcal C=\mathcal C_L+\mathcal C_R$。原稿已完整证明
$$
\mathcal Z_{\rm full}=U-\mathcal C,\quad
L_m\mathcal Z_{\rm full}=0,\quad
\|\mathcal C\|\le\varepsilon,
$$
且跨 $q$ 切开后
$$
F_{\rm test}:=U-\mathcal C_L:\mathscr Z\to\mathscr V_q,
\qquad
\mathcal C_R:\mathscr Z\to\ker S.
$$
这里 $\varepsilon$ 是该稿实际预算；例如 $K\le d/4,q\le e^{d^3/8}$ 时 $\varepsilon\le e^{-d^4/20}$。

完整核的边界方程给同一个真正测试源
$$
r_{\rm test}=E_qF_{\rm test}=F_{\rm flag}\mathcal C_R.
\tag{6.1}
$$
定义独立源测试映射
$$
\boxed{
S_{m,s,q}:=\Gamma_qF_{\rm flag}\mathcal C_R
=P_{\mathscr U_q}P_0(U-\mathcal C_L).
}
\tag{6.2}
$$
第二式由 $F_{\rm test}\in\mathscr V_q$、$\mathcal E^{-1}=P_0$ 和 (3.6) 准确推出。由于相容 $R_j$ 不必是最小原像，一般 $P_0\mathcal C_L$ 不为零；它已显式保留，没有直接把测试坐标改成 $H_{m,s}P_0z$。

对任意原源 $r$，写 $a=\Gamma_qr$、$c^\flat=F_{\rm flag}^*J_q^{-1}r$。由 (4.3)、(6.2)，得到准确身份
$$
\boxed{S_{m,s,q}^*\mathcal G_qa=\mathcal C_R^*c^\flat.}
\tag{6.3}
$$
特别
$$
\boxed{
\|S_{m,s,q}^*\mathcal G_q\Gamma_qr\|
\le\varepsilon\,\lambda_q(r^\flat).
}
\tag{6.4}
$$
与未修正的物理高块投影不同，(6.4) 右侧没有 $\mu_q(r)$ 项；代价是必须使用 (6.2) 的真正测试坐标，保留 $P_0\mathcal C_L$。

## 7. 它确实给出的两种算子序及准确未覆盖方向

从 $F_{\rm test}$ 是源 $r_{\rm test}$ 的合法左原像，且 $\|F_{\rm test}\|\le1+\varepsilon$，得到真实的受限上界
$$
\boxed{S_{m,s,q}^*\mathcal G_qS_{m,s,q}
\preceq(1+\varepsilon)^2I_{\mathscr Z}.}
\tag{7.1}
$$
从 (6.2) 与 $\|\mathcal C_R\|\le\varepsilon$，还有
$$
\boxed{S_{m,s,q}S_{m,s,q}^*
\preceq\varepsilon^2\mathcal H_q.}
\tag{7.2}
$$
所以这一族对完整右度量给的是下界
$$
\lambda_q(r^\flat)^2
\ge\varepsilon^{-2}
\|S_{m,s,q}^*\mathcal G_qa\|^2.
\tag{7.3}
$$
(7.1) 的上界只在 $\operatorname{Ran}S_{m,s,q}$ 的受控原像上成立；它不是整个 $\mathcal G_q$ 的上界。要由 (7.3) 重建整个 $\mu_q(r)$，仍须额外的测试下框架界或与真实裸能量 $\mathcal F_q$ 的互补估计。

这里的正交补可以准确指出，而不依赖抽象反例。增长头稿的 $U$ 输出头指标至多为
$$
T=d/2+K-1,
$$
修正 $\mathcal C_L$ 的头指标至多为 $T-1$。因此 (6.2) 给
$$
\operatorname{Ran}S_{m,s,q}
\subseteq\mathscr U_q\cap
\left(H_{\le T}\otimes\bigoplus_nK_n\right).
\tag{7.4}
$$
整个已付家族 $K\le d/4$ 都有 $T\le3d/4-1$。

取任意单位 $g\in K_q$，令 $b$ 为独立坐标中第 $t=0$ 层的 $e_{d-1}\otimes g$，其他层为零。这样的 $g$ 存在：在任意 $2q$ 个尾位上，将每个不交对的加权单孔 primitive 向量张量相乘即可。由 (7.4)，全部这些增长头测试均满足 $S_{m,s,q}^*b=0$。

由 (4.4)，$\mathcal G_qb=b$。因此可明确取
$$
a_*:=b,\qquad r_*:=B_Ub=Ae_{d-1}\otimes g.
$$
这是同一个原完整源空间中的非零合法源，且
$$
\mu_q(r_*)^2=1,
\qquad
S_{m,s,q}^*\mathcal G_q\Gamma_qr_*=0
\quad\text{对全部上述 }s.
\tag{7.5}
$$
因此该增长头测试族单独不可能具有整个原左源空间上的严格正下框架界。
本例没有把 $r_*$ 认成真实 $W$ 来源。事实上 (4.6) 给 $\alpha_q(r_*)\ge\|D_m\|^{-1}$，所以这个明确的未检出方向恰被裸项支付；没有给 $\lambda(r_*^\flat)$ 的上界，尤其不是 (5.3) 的反例。真正尚欠的是全部补方向与裸项的共同估计。

## 8. 原头理想生成元在这些坐标上的准确收缩

设 $Q$ 是保持原头旗、与 $A$ 交换的原头算子；特别可以取 $Q=N_j^{[m]}$。定义
$$
Q_U=\bigoplus_{t=0}^{d-2}
\left(P_{H_{\ge t+1}}Q|_{H_{\ge t+1}}\otimes I_{K_{q-t}}\right).
$$
由 (3.4) 和 $[Q,A]=0$，准确有
$$
\boxed{\Gamma_qQr=Q_U\Gamma_qr,\qquad \|Q_U\|\le\|Q\|.}
\tag{8.1}
$$
这是普通正交商头作用，未把完整 $\mathcal G_q$ 换成单位度量。

因为 $Q\mathscr V_q\subseteq\mathscr V_q$，且 $E_qQ=QE_q$，对任意原源有
$\mu_q(Qr)\le\|Q\|\mu_q(r)$。因此
$$
\boxed{Q_U^*\mathcal G_qQ_U\preceq\|Q\|^2\mathcal G_q.}
\tag{8.2}
$$
对真实头 $N_j^{[m]}$，右侧系数至多为一。

同理，若 $q-1$ 仍在原合法窗口，则纯尾删除把 $\mathscr V_q$ 送到 $\mathscr V_{q-1}$，并给源 $Dr$。其独立坐标准确满足
$$
\boxed{
(\Gamma_{q-1}Dr)_t
=-P_{H_{\ge t+1}}A(\Gamma_qr)_{t+1}
\quad(0\le t\le d-3),
\qquad
(\Gamma_{q-1}Dr)_{d-2}=0.
}
\tag{8.3}
$$
记右侧为 $R_qa$，则
$$
\boxed{R_q^*\mathcal G_{q-1}R_q
\preceq\|D_m\|^2\mathcal G_q.}
\tag{8.4}
$$
(8.1)–(8.4) 都保留了完整零源 Schur 度量。它们不允许将实际 $Qw$、$Dw$ 的窄通量直接换成 $w$ 的同一源；相应原来源运输仍须使用已付的完整公式。

## 9. 当前明确剩余输入

现在真实全左费用的未知量已准确落在 (5.3)，对实际两侧来源则落在 (5.4) 的同一个坐标。增长头构造支付了 (6.3)–(7.3)，并明确留下 (7.4) 的高头余项；头理想作用给 (8.2)，但没有给出补空间的能量上界。

尚需证明真实裸项 $\mathcal F_q$ 与这些受控源观测共同覆盖 $\mathcal G_q$，或利用原 $\overline f$ 的相容来源排除 (7.5) 一类未检出方向。普通环境源、源投影或仅有 $\mathcal G_q\succeq I$ 均不提供这一输入。无权 $N=M$ 和普通 ISP 继续开放。
