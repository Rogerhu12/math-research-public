# 半径 1/50 内全部负侧接口到原腰的 genuine 算子

在 [GJS.2](R149-supplement-two-signed-coefficients-for-every-genuine-negative-interface.md) 用原 576 个负侧接口和完整 $n=4|j|\ge388$。记 $w=[Dw_1]$、$U(a)f=\sum_j e^{4ijX}a^t\operatorname{diag}(1,n^{-1})\Psi_n(T)f_j$、$N=388$、$\mathsf N f_j=n f_j$。频率符号相关的向量 $a$ 分正负两组。在实 $r$ 的复角条 $|\Im\phi|\le h=1/32$ 上，由旧 M.8 的 $A_->4$、$A_+<23$、$G<23/10$、$|x|<81/80$、$|T_\phi|<7/1000$，有
\[
 4^{1/3}\sqrt{\rho}< |s|<23^{1/3}\sqrt{\rho},\qquad
 |t|=|sT_\phi|\le(7/1000)23^{1/3}\sqrt{\rho}.
\]
在虚条上 $A_-$ 指真实复模下界，$s=\sqrt\rho A^{1/3}$ 用原主支。它来自 [M 的 $A$ 下界与角宽](R133-supplement-actual-piecewise-root-radius-one-over-fifty-and-full-seams.md)。按 GJS.1 使用原同侧 $q,q_r,\eta,\gamma,\beta$、复条 $u,v$ 与已付全分量斜率跳，以及单独的均值跳。逐分量可与已经付过的自由首幅导数跳条界取小者；依 WUA.46 这两幅是同一向量。此处真正的剖面仍取 $\Psi_n$。[原自由幅的每缝记录](R133-supplement-actual-first-Airy-seams-and-six-forcing-windows.md)

令 $z=N^{-2/3}+23^{2/3}\rho_{\max}$，$\theta=\sqrt z$，$m(a)=\sup|a_1|+\theta\sup|a_2|$。原两真实相位角导在 $(79/80,81/80)$，所以 $\log(u_{\max}/u_{\min})<1/50$，其中 $u=-T$。依 [真实两行逐水平集分解](R149-supplement-all-frequency-two-ray-physical-bound-for-both-genuine-Airy-rows.md)，高度幅 $\sqrt{m_{\rm Ai}(n^{2/3}u)}<1$，导数幅至多 $\theta$。连同原 $Z_n$ 的 $6/5$ 升幅、$13/N$ 总变差，每个符号的两分支费为
\[
 \sqrt{160/79}[ (6/5)(1+5/(8\cdot50))+13/N]<2 .
\]
故 $\|U(a)\|\le2\sqrt2\,m(a)$，已经包括原两列、真实根剪切和两频率符号。若 $a$ 在频率只多一个因子 $V_n(T)$，可用 $290\,m(a)$ 代替 $m(a)$。确切地写 $V_n(T)=\chi(T)[v_n(0)+\int_0^{1/2000}{\bf1}_{-T>l}\partial_l v_n(-l)dl]$（当 $-T$ 超过支持端点，外侧 $\chi=0$）。真实 $0\le\chi\le1$、原解析部 $|v_n|\le276$、$|\partial_l v_n|\le26431$ 和公共物理指示给 $276+26431/2000<290$。没有对截断函数求导。[BPF.4](R149-supplement-whole-genuine-inverse-deformation-on-the-physical-Fourier-space.md)

设 $B=H_\epsilon^{-1}$ 是自由矩阵，$F=yE_{12}$，$y=T_\phi$。由 $\det H=-p_+p_-$、M.8 的 $|p_\pm-1|<1/80$、$|T|<4/25$，复条上 $B$ 在上述加权分量范数的费至多
\[
 H=(81/80+(7/1000)\max(\theta,(4/25)/\theta))/(79/80)^2,\qquad
 \|F\|\le (7/1000)/\theta=:E.
\]
上述实 $p_\pm$ 范围与复条 $|p_\pm-1|$ 的共同依据是 M 的完整复角变分方程，始终在同一原 $r$。WUA.30 精确给
\[
 U(a)\mathsf N=\partial U(Ba)-U((Ba)')+U(V_n FBa)\mathsf N^{-1}.
\]
将它用两次，仅展开无 $V_n$ 的项，得
\[
\begin{split}
 U(w)\mathsf N^2={}&\partial^2U(B^2w)
 -\partial U((B^2w)'+B(Bw)')+U((B(Bw)')')\\
 &+\partial U(V_n FB^2 w)\mathsf N^{-1}
  -U(V_n FB(Bw)')\mathsf N^{-1}+U(V_n FBw).
\end{split}
\]
括号内普通导仅施于同一物理振幅。$P\Lambda^{-2}$、$P\Lambda^{-2}\partial$、$P\Lambda^{-2}\partial^2$ 范数分别至多 $d=1/17,p=4/17,1$。给每个角导分配 $h/k$ 宽（$k$ 为该项角导数），得到
\[
 K=H^2(1+2p/h+4d/h^2)+290 E[dH+(p+d/h)H^2/N].
\]
于是 $\|PU(w)\mathsf N^2\|_{\ell^2\to H^{-2}}\le2\sqrt2\,m(w)K$。与零阶用同一 Fourier 尺度作 $5/6$ 插值，原带整输入的界面 $n^{1/6}$ 及 $H^{-4/3}$ 密度给
\[
 \|P U(w)\mathsf N^{1/6}\|_{H^{-4/3}\to H^{-5/3}}
 \le 2\sqrt2\,m(w)K^{5/6}N^{-1/6}(1+N^{-2})^{2/3}.
 \tag{GJR.1}
\]
完整权重 $\mathsf N$ 位于原输入端。外侧 $P$ 是实际高度投影；原 $U$ 的身体和 (GJS.1) 本身保有全部均值。这也允许用原每缝 $J:H^{-5/3}\to H^{-2/3}$ 的完整界。

用相同 $c_{PW}=r_+-1/200$ 分两段。其内的 mixed 原子直接到腰费 $2039$。在其外 $H^{-2/3}\hookrightarrow H^{-1}$ 收缩，SP.31–33 的同一任意有向时刻点注入应用到 $j$ 上，得 $192$（原记录的点态注入、全子区间传播和腰读，不乘径向长）。最后乘物理反射读 $.719$，公共输入 $N_i$ 的因子 $12.4$。这些因子皆来自 [GSW 的同一真输出](R149-supplement-first-genuine-source-through-the-physical-waist-and-common-input.md) 与 [SP 的点态仿射注入](R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md)。每个非零原子只出现一次。实际 GJR 数值汇总只涵盖所标 576 个负侧结点。
