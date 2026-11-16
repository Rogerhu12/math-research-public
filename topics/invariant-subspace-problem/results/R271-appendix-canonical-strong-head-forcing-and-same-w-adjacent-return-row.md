# R271 附录：规范强头 forcing 与同一个 w 的相邻返回整行

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文把前稿两个低 forcing 的相邻配对，运输回同一个原 $w\in W$ 的实际投影向量。两条交叉误差使用已付删除／创建弱行；只有尾误差对尾误差需要环境费用。对这一项，真实硬核层的有限头 $\ell^1$ 界和后尾 bosonic Cauchy 给出对数费用。再用原 actual 投影的准确 carry 误差，可把主界锐化为直接的截断通量界。由此得到原母窗上的显式整行界，以及不假设 $w$ 尾速率的合法慢窗。

所有空间均是原负整数边界的同一个物理 $\ell^2(\mathbb N_0)$。本文不把它与另一个无限张量积参考向量或普通 Haar 表示混同，也不宣称完成普通不变子空间问题。

依据：

- [原两边界算子及标准物理基](R200-boundary-right-shift-domains-and-forward-division-saturation.md)，§1；
- [真实投影缺陷及统一母窗](R271-appendix-actual-projection-defect-two-sided-generator-and-all-dark-moments.md)，§5(5.2)--(5.4)；
- [真实最小投影带权窗口](R271-appendix-true-minimal-projection-weighted-window.md)，§1(1.4)、§4；
- [删除正 Gram 的弱行](R271-appendix-actual-low-end-forcing-positive-deletion-grams-and-compressed-adjoint-descendants.md)，§5(5.5)；
- [创建合成与相邻旗返回](R271-appendix-adjoint-creation-synthesis-and-common-source-adjacent-flag-return.md)，§§3、6。

## 1. 规范强头截断就在原共同物理空间内

R200 §1 的两种原算子 $T_N,T_Y$ 都作用于同一个
$$
\mathcal H_-=\ell^2(\mathbb N_0)
$$
及其标准正交基 $(e_n)_{n\ge0}$。用整数 $n$ 的二进位作原物理位分解；尾参考为所有这些位的 $0$。于是，对整数 $x\ge1$，强头张量远尾真空投影准确是
$$
\boxed{
P_x=\sum_{0\le n<2^x}|e_n\rangle\langle e_n|.
}
\tag{1.1}
$$
它不是换了参考后的 Haar 条件期望。有限支撑序列在 $\mathcal H_-$ 稠密，所以
$$
P_x\longrightarrow I\quad\text{强收敛}.
\tag{1.2}
$$

固定原 $w\in W=M\ominus N$。下文取
$$
d=2^m,\qquad R=d,\qquad x=m+d,\qquad h=2d,
$$
并定义
$$
f_m=P_xw=i_0g_m,\qquad r_m=(I-P_x)w,\qquad
\tau_m=\|r_m\|,\qquad W_0=\|w\|.
\tag{1.3}
$$
$g_m$ 是原共同强头空间中的整个向量；没有强行把它限制在固定几个坐标。前稿的完整源算子不等式对这个空间一致，因此允许该规范来源随 $m$ 变化。由 (1.2)，$\tau_m\to0$，且 $\|g_m\|\le W_0$。

对原 cut $q$，始终记
$$
u_{w,q}=P_{U_{m,q}}w,\qquad
u_{g_m,q}=P_{U_{m,q}}f_m,\qquad
\delta u_{m,q}=P_{U_{m,q}}r_m .
\tag{1.4}
$$
故 $u_{w,q}=u_{g_m,q}+\delta u_{m,q}$，并且
$\|\delta u_{m,q}\|\le\tau_m$。这里不把左边的实际来源换成右边的近似来源，而是保留其准确误差。

## 2. 真实硬核有限孔的调和费用

对任意 $v$ 支撑于原总尾孔数 $\le Q$、任意物理 $z$，定义弱行
$$
\mathcal B_x(v,z)
=\left(\frac{\langle E_iv,z\rangle}{\sqrt{i+1}}\right)_{i\ge x}.
$$
取任意有限标量族 $(a_i)$，$\sum_i|a_i|^2\le1$，及整数 $L\ge0$。前 $L$ 个远位只用各 $\|E_i\|\le1$，得到
$$
\left\|\sum_{x\le i<x+L}\frac{a_iE_i}{\sqrt{i+1}}\right\|
\le
\left(\sum_{i=x}^{x+L-1}\frac1{i+1}\right)^{1/2}
\left(\sum_{x\le i<x+L}|a_i|^2\right)^{1/2}.
\tag{2.1}
$$
后尾则保真实孔上界。对任意平方可和系数 $c_i$，
$$
\left\|\sum_i c_i E_i\right\|_{\{\text{远孔}\le Q\}}
\le\sqrt Q\,\|(c_i)\|_2 .
\tag{2.2}
$$
可逐孔自足证明：在 $n$ 孔层，输出集合 $J$ 的系数为
$\sum_{i\notin J}c_i v_{J\cup\{i\}}$；Cauchy 后对 $J$ 求和，每个输入集合出现恰 $n$ 次，给 $n\sum_i|c_i|^2\|v\|^2$。不同孔层的输出正交，所以直和到 $n\le Q$ 得 (2.2)。原强头的向量系数不改变此证明。也可视为真实 bosonic annihilator 在硬核子空间上的压缩，但无需此解释。

对 $i\ge x+L$ 应用 (2.2)，再把前后两段的标量 $\ell^2$ 范数共同作一次 Cauchy，得到
$$
\left\|\sum_{i\ge x}\frac{a_iE_i}{\sqrt{i+1}}\right\|_{\{\text{总尾孔}\le Q\}}^2
\le
\sum_{i=x}^{x+L-1}\frac1{i+1}+\frac{Q}{x+L+1}.
\tag{2.3}
$$
取 $L=Q$，定义
$$
\mathfrak c(Q,x)=
\sum_{i=x}^{x+Q-1}\frac1{i+1}
+\frac{Q}{x+Q+1}
\le1+\log\left(1+\frac Qx\right).
\tag{2.4}
$$
由有限标量族对偶及非负极限，得
$$
\boxed{
\|\mathcal B_x(v,z)\|_{\ell^2}
\le\sqrt{\mathfrak c(Q,x)}\,\|v\|\,\|z\|.
}
\tag{2.5}
$$
(2.5) 不要求 $z$ 有有限孔支持。它也没有将全硬核 Fock 上无界的总删除行当成有界算子；$v$ 的真实 $Q$ cut 是必要条件。

## 3. 两条交叉误差不乘调和费用

以下要求 $Q$ 和 $Q-1$ 都在原合法母窗，并且
$Q\ge R+h+2$。标准 $m\ge10$ 时，只需后文的
$Q\ge4d+1$ 即涵盖后一条件。

置
$$
\Delta_q=\|f_m-u_{g_m,q}\|,\qquad
\eta_{m,Q}(w)=
\max\{\|(I-P_{U_{m,Q}})w\|,
       \|(I-P_{U_{m,Q-1}})w\|\}.
$$
投影收缩给
$$
\Delta_Q,\Delta_{Q-1}\le\tau_m+\eta_{m,Q}(w).
\tag{3.1}
$$

对两个规范来源，前稿 (6.3) 给
$$
\|\mathcal B_x(u_{g_m,Q},u_{g_m,Q-1})\|_2
\le
2\Delta_Q\Delta_{Q-1}
+\frac{1+\sqrt2}{\sqrt{x+1}}\,
W_0\Delta_Q.
\tag{3.2}
$$
其中完整方差参数只依赖 $m,x,g_m$，在所有后续 cut 之前选择；第二个 $u$ 不受其选择影响。

旧删除弱行对任意物理目标适用，故
$$
\|\mathcal B_x(u_{g_m,Q},\delta u_{m,Q-1})\|_2
\le\sqrt{\frac83}\,\Delta_Q\,\tau_m .
\tag{3.3}
$$
反过来的交叉项由新创建弱行支付：
$$
\|\mathcal B_x(\delta u_{m,Q},u_{g_m,Q-1})\|_2
\le
\left[
\frac{W_0}{\sqrt{x+1}}+2\Delta_{Q-1}
\right]\tau_m .
\tag{3.4}
$$
因此两条交叉都保原缺陷，没有把任意尾向量冒充新的 far-vac forcing。

只有两侧都为真实尾误差时才应用 (2.5)：
$$
\|\mathcal B_x(\delta u_{m,Q},\delta u_{m,Q-1})\|_2
\le\sqrt{\mathfrak c(Q,x)}\,\tau_m^2.
\tag{3.5}
$$
平方尾误差而非单尾误差出现在这里，是保留四项联合展开的实际收益。

## 4. 原同一个 w 的完整行估计

将 (1.4) 在两端同时展开，使用 (3.1)--(3.5)，并记
$\varepsilon_{m,Q}=\tau_m+\eta_{m,Q}(w)$，得到
$$
\boxed{
\begin{split}
&\left(\sum_{i\ge x}
\frac{|\langle E_i u_{w,Q},u_{w,Q-1}\rangle|^2}{i+1}
\right)^{1/2}\\
&\quad\le
6\varepsilon_{m,Q}^2
+\frac{4W_0\,\varepsilon_{m,Q}}{\sqrt{x+1}}
+\sqrt{1+\log(1+Q/x)}\,\tau_m^2 .
\end{split}
}
\tag{4.1}
$$
常数核对如下：主项为 $2\Delta_Q\Delta_{Q-1}$，两条交叉的缺陷系数分别至多 $2\Delta_Q\tau_m$、$2\Delta_{Q-1}\tau_m$，合计至多 $6\varepsilon_{m,Q}^2$；源范数系数 $1+\sqrt2+1=2+\sqrt2<4$。

(4.1) 左边始终是同一个原 $w$ 的真实 $u_{w,Q},u_{w,Q-1}$。没有用逐列强收敛后再相加，也没有删除任何相邻真核反馈。无限移动行已经由 (2.5)、已付两种弱行及非负极限共同定义。

## 4a. 原 actual carry 给更锐的直接截断通量界

对同一个原总尾孔 cut，令
$$
p_q=P_{\mathrm{tail}(m)\le q},\qquad
\epsilon_q=u_{w,q}-p_qw .
$$
在下节的原母窗内，已付实际投影定理准确给
$$
\|\epsilon_q\|\le2e^{-6d^4}W_0,\qquad
\epsilon_q\text{ 支撑于总尾孔 }\le q .
\tag{4.2}
$$
令 $f=P_xw$。因为 $f$ 的原尾孔数至多 $R$，而 $Q-1\ge R$，有
$p_Qf=p_{Q-1}f=f$。两个截断都是同一物理基上的对角投影，故
$$
p_qw=f+r_q,\qquad
r_q=p_q(I-P_x)w,\qquad \|r_q\|\le\tau_m .
$$
每个 $i\ge x$ 都满足 $E_if=0$，所以
$$
\mathcal B_x(p_Qw,p_{Q-1}w)
=\mathcal B_x(r_Q,f)+\mathcal B_x(r_Q,r_{Q-1}).
$$
第一项由真正的真空创建列正交性支付：$E_i^*f$ 在不同 $i$ 上互相正交，范数均为 $\|f\|$。因此 Bessel 不等式给
$$
\|\mathcal B_x(r_Q,f)\|_2
\le\frac{\|f\|\,\|r_Q\|}{\sqrt{x+1}}
\le\frac{W_0\tau_m}{\sqrt{x+1}}.
$$
第二项用 (2.5)，至多 $\sqrt{\mathfrak c(Q,x)}\,\tau_m^2$。

最后，真实投影与理想截断的差严格写成两项
$$
\begin{split}
&\mathcal B_x(u_{w,Q},u_{w,Q-1})
-\mathcal B_x(p_Qw,p_{Q-1}w)\\
&\qquad=
\mathcal B_x(\epsilon_Q,u_{w,Q-1})
+\mathcal B_x(p_Qw,\epsilon_{Q-1}).
\end{split}
$$
两项第一变量都支撑于总尾孔 $\le Q$，其余向量范数至多 $W_0$。由 (2.5)、(4.2)，准确得到
$$
\boxed{
\begin{split}
&\left(\sum_{i\ge x}
\frac{|\langle E_i u_{w,Q},u_{w,Q-1}\rangle|^2}{i+1}
\right)^{1/2}\\
&\quad\le
\frac{W_0\tau_m}{\sqrt{x+1}}
+\sqrt{1+\log(1+Q/x)}
 \left(\tau_m^2+4e^{-6d^4}W_0^2\right).
\end{split}
}
\tag{4.3}
$$
这个加强直接保同一个 $w$ 和原物理投影。它不需要对尾误差另套低 forcing 的正 Gram，也不需要 (4.1) 中的 $\eta_{m,Q}$。前面的四项运输证明仍给出：在只能使用原缺陷估计而未调用这条更锐 actual carry 逼近时，具体哪些误差由删除／创建弱行支付。

## 5. 整个原母窗上的 sup 与合法慢窗

明确取旧已付带权母窗的整数子区间
$$
\mathcal I_m=
\left\{Q\in\mathbb N:
4d+1\le Q\le
\exp\left(\frac{1601}{64}d^3\right)\right\},
\qquad m\ge10 .
\tag{5.1}
$$
因而 $Q-1$ 仍满足旧下界 $4d$。定义真正的全窗误差
$$
\eta_m(w)=
\sup_{Q\in\mathcal I_m}
\max\{\|(I-P_{U_{m,Q}})w\|,
       \|(I-P_{U_{m,Q-1}})w\|\}.
\tag{5.2}
$$
旧实际投影定理对每个这些 cut 给
$$
\|P_{U_{m,q}}w-P_{\mathrm{tail}(m)\le q}w\|
\le2e^{-6d^4}W_0.
$$
因此不是仅固定 cut，而是准确有
$$
\boxed{
\eta_m(w)\le
\|(I-P_m)w\|+2e^{-6d^4}W_0
\longrightarrow0.
}
\tag{5.3}
$$
这里 $P_m$ 正是 (1.1) 中的同物理尾真空投影。强位重分组不改变原 $P_U$。

故 (4.1) 对整个 (5.1) 同时成立，可把其
$\varepsilon_{m,Q}$ 统一放宽为 $\tau_m+\eta_m(w)$。
更锐的 (4.3) 也对全窗成立；其中 carry 项在该全窗一致趋零，因为
$$
\sqrt{1+\log(1+Q/x)}\,e^{-6d^4}
\le
\sqrt{1+\log2+\tfrac{1601}{64}d^3}\,e^{-6d^4}
\longrightarrow0 .
$$
仍须保留 $\sqrt{1+\log(1+Q/x)}\,\tau_m^2$。没有尾速率时，本文不据此称整个指数母窗上的该行一致趋零。

在任何 $Q/x$ 一致有界的合法子窗，(4.3) 已给原实际整行一致趋零。若需要 $Q/h\to\infty$，则可不假设任何尾速率地选同 $w$ 的慢窗。$W_0=0$ 时结论平凡；否则令
$$
\theta_m=\tau_m/W_0,\qquad
L_m=
\begin{cases}
\exp\{\min(\log d,\theta_m^{-2})\},&\theta_m>0,\\
d,&\theta_m=0,
\end{cases}
\qquad
Q_m=\lceil8dL_m\rceil .
\tag{5.4}
$$
由于 $\theta_m\to0$，有
$$
L_m\to\infty,\quad 1\le L_m\le d,\quad
Q_m\le8d^2+1,\quad
\frac{Q_m}{h}\ge4L_m\longrightarrow\infty .
$$
因此 $Q_m,Q_m-1$ 都在 (5.1) 内，且所有强头／新增一位来源的门都成立。原 carry 母窗没有被扩大。

又因 $x\ge d$，
$$
\begin{split}
\tau_m^2\sqrt{1+\log(1+Q_m/x)}
&\le W_0^2\theta_m^2
 \sqrt{1+\log(1+9L_m)}\\
&\le W_0^2\theta_m^2
 \sqrt{1+\log10+\theta_m^{-2}}
\longrightarrow0 .
\end{split}
$$
结合全窗 carry 小量，(4.3) 遂给
$$
\boxed{
\sum_{i\ge m+2^m}
\frac{|\langle E_i u_{w,Q_m},u_{w,Q_m-1}\rangle|^2}{i+1}
\longrightarrow0 .
}
\tag{5.5}
$$
参数选择针对同一个原 $w$，来源始终是其规范强头截断；实际被估计的仍是原 $u_w$。它不要求 $\|(I-P_x)w\|$ 具有预设速率，也没有在原核空间之外另选一条可行链。

## 6. 未支付的边界

(5.5) 只是准确相邻 cut 的标量删除配对行。要将其用于普通 $N=M$，仍需从原同 $w$ 约束导出与这些系数相容的非零下界，或把它们准确接到完整返回／顺次 MP 的两端部分和。

本文没有得到 $\sum_i\|E_i u_{w,Q}\|^2$，也没有以 (5.5) 代替完整高旗、普通右旗或原 Haar 表示的桥梁。它解决的是从两个合法低 forcing 到同一个实际无限 $w$ 的整行运输，并准确列出当前允许的窗口。
