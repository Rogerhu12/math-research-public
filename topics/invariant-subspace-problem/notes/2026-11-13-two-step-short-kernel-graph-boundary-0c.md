# R239 附录：原近核双头的二阶短核图与真实缺陷的全尾非primitive观测

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。
状态：以下完整原模型图空间估计已证明。它增加非primitive的二阶短核图，不给整个左最小费用上界，也不宣称无权 $N=M$。

本稿是增长低头完整核定理之前的二阶证明，保留 m≥6 的明确费用；主要范围已纳入[增长头定理](../results/R239-appendix-growing-head-intertwining-and-full-short-kernel-observation.md)，不重复登记。

本稿承接[实际高孔观测笔记 §§10、14](../notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)、[实际首位矩阵](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)及[原线性逐头提升](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)。新的范围是同一原近核头附近的整个 $\ker D_m^2$ 图；原始方向 $h_m\otimes\ker D_m$ 已由高孔笔记 §14 支付，不重复计作新增范围。

## 1. 同一模型、原窗口和结论

取两个实际边界之一，$m\ge6$、$d=2^m$，并令
$$
4d\le q\le q_m:=\lfloor e^{d^3/4}\rfloor,
\qquad A=A_m,\qquad D=D_m=\sum_{j\ge m}(j+1)^{-2}E_j,
\qquad L=A+D.
$$
全部空间均用原物理 Hilbert 范数，$\|A\|<6$、$\nu_m:=\|D\|\le m^{-1}$。
令 $b_j=(j+1)^{-2}$，并保持高孔笔记中的同一个头
$$
p=d/4,\qquad
h_0=h_m=\frac{b_{m-1}e_p-b_{m-2}e_{2p}}
{\sqrt{b_{m-2}^2+b_{m-1}^2}},
\qquad h_1=E_0^*h_0.
\tag{1.1}
$$
$h_0$ 支持在两个偶数头，$h_1$ 支持在相应奇数头，因此两者严格正交且范数均为一。记
$$
\mathcal K_{2,q}=\ker D^2\cap\mathcal H_{\le q}^{(m)}.
$$
定义真实的二阶图嵌入
$$
\boxed{\mathcal J_{2,m,q}f=h_0\otimes f-h_1\otimes Df,
\qquad f\in\mathcal K_{2,q}.}
\tag{1.2}
$$
它满足
$$
\|\mathcal J_2f\|^2=\|f\|^2+\|Df\|^2,
\qquad \|f\|\le\|\mathcal J_2f\|\le\sqrt{1+\nu_m^2}\|f\|.
\tag{1.3}
$$
特别，$\mathcal G_{2,m,q}:=\operatorname{Ran}\mathcal J_2$ 为闭子空间。

**定理一（原缺陷上的图角度）。** 对 $W=M\ominus N$ 中的任意 $w$，
$$
\boxed{
\|\mathcal J_2^*w\|\le2e^{-d^4/20}\|w\|,
\qquad
\|P_{\mathcal G_{2,m,q}}w\|\le2e^{-d^4/20}\|w\|.
}
\tag{1.4}
$$
第一项在真实尾空间中准确写成
$$
\boxed{
\left\|P_{\mathcal K_{2,q}}
\left((h_0^*\otimes I)w-D^*(h_1^*\otimes I)w\right)\right\|
\le2e^{-d^4/20}\|w\|.
}
\tag{1.5}
$$
此处投影只作用于显示的联合观测；没有把 $w$ 投影后当成另一个合法源。

**定理二（任意原源的完整三 Gram 版本）。** 沿用原完整左、右源 Gram $J_q,G_q$，令
$$
y=J_q^{-1}r,\qquad v=E_q^\dagger r=E_q^*y,
\qquad r^\flat=G_qy,\qquad c^\flat=F_{\rm flag}^*y.
$$
则对每个原完整源 $r\in\mathscr R_q$，
$$
\boxed{
\|\mathcal J_2^*v\|^2,\ 
\|P_{\mathcal G_{2,m,q}}v\|^2
\le e^{-d^4/10}\left(\mu_q(r)^2+\lambda_q(r^\flat)^2\right).
}
\tag{1.6}
$$
它不要求 $r$ 本身是 primitive，也不压缩原 $J_q,G_q$。

## 2. 实际首位矩阵给近二阶头链

记 $\epsilon_m=\eta_{m-3}$。原高孔笔记 §10.2 已在两模型中准确证明
$$
\|Ah_0\|\le12\epsilon_m.
\tag{2.1}
$$
下面保留实际首位矩阵，支付将 $h_0$ 向上延长一步的误差。

按最低位写 $h_0=(g,0)$、$h_1=(0,g)$。在这个有限头内，记 $Z=N_1^{[m]}$ 的共同尾作用。原 dyadic 权积给
$$
N_1^{[m]}e_{2^n}
=\frac{\alpha_n}{\alpha_1}e_{2^n-2}
\quad(1\le n<m).
$$
对 $n=m-2,m-1$，两个输出正交，且 $\alpha_n/\alpha_1\le\eta_{m-3}$，故
$$
\boxed{\|Zg\|\le\epsilon_m.}
\tag{2.2}
$$
这里没有把 $N_1$ 替换为纯删除。

对 $N$ 型头，准确有
$$
A=\begin{pmatrix}U&I\\\eta_0Z&U\end{pmatrix}.
$$
因此 $Ah_1-h_0=(0,Ug)$，由 (2.1) 得 $\|Ah_1-h_0\|\le12\epsilon_m$。

对 $Y$ 型头，令
$$
R=(I-\eta_0Z)^{-1},\qquad
V=\sum_{j=1}^{m-1}b_jY_j^{[m]}-\eta_0ZR.
$$
原 Cayley 逆的准确式为
$$
A=\begin{pmatrix}V&R\\\eta_0ZR&V\end{pmatrix}.
\tag{2.3}
$$
故 $Ah_0=(Vg,\eta_0ZRg)$、$Ah_1-h_0=((R-I)g,Vg)$。由 $\eta_0=e^{-1070}<1/2$、(2.2) 及 (2.1)，
$$
\|(R-I)g\|\le\frac{\eta_0}{1-\eta_0}\|Zg\|<\epsilon_m,
\qquad \|Vg\|\le12\epsilon_m.
$$
两项在首位直和中正交。因此两个模型统一满足
$$
\boxed{
\|Ah_1-h_0\|\le13\epsilon_m,
\qquad
\|A^2h_1\|\le\|Ah_0\|+\|A\|\|Ah_1-h_0\|
\le90\epsilon_m.
}
\tag{2.4}
$$
这一步只反演范数小于一的 $\eta_0Z$，未使用实际大头的 Jordan 相似或微小第一上对角线的逆。

## 3. 整个二阶短核上的精确 L 核

置
$$
T=d/2+1,\qquad
\mathcal L=512\sqrt{q+2T+1}\,(m+q+2T+1)^{3/2}.
\tag{3.1}
$$
$h_1$ 只支持在头指标 $\le T$，故 $A^{T+1}h_1=0$。

使用高孔笔记 §14.2.A 在同一辅助头上构造的顺次单步最小原像，记为 $\widehat Q_t$。对当前完整域 $\mathcal K_{2,q}$ 及 $1\le t\le T-1$，它满足
$$
\widehat Q_0=I,\qquad
D\widehat Q_t=\widehat Q_{t-1},\qquad
D^{t+2}\widehat Q_t=0,
\tag{3.2}
$$
并增加恰好 $t$ 个尾孔，且
$$
\boxed{
\|\widehat Q_tf\|
\le2^{t-1}(t+1)\mathcal L^{t+1}\|f\|.
}
\tag{3.3}
$$
为明确域：该构造的共同输入上界取 $P=q+T$，最大原像阶取 $T$；于是对 $f\in\mathcal H_{\le q}$，全部中间孔数均不超过 $P$。一般核阶 $s=2$ 只在 $\mathcal L^{s+t-1}$ 中支付一次；这里没有把 $\widehat Q_t$ 认成 $(D^t)^\dagger$。

定义
$$
\boxed{
\mathcal Z_2 f
=Ah_1\otimes f-h_1\otimes Df
+\sum_{t=1}^{T-1}(-1)^t A^{t+1}h_1\otimes\widehat Q_tf.
}
\tag{3.4}
$$
先对首两项作用 $L=A+D$：两项混合部分抵消，剩余为
$A^2h_1\otimes f-h_1\otimes D^2f=A^2h_1\otimes f$。
求和的首个 $D$ 项恰为其负值；相邻 $A/D$ 项由 (3.2) 全部抵消；末端由 $A^{T+1}h_1=0$ 消失。因此
$$
\boxed{L\mathcal Z_2f=0.}
\tag{3.5}
$$
本式对整个闭空间 $\mathcal K_{2,q}$ 成立，位置支撑可以无限远。
其总尾孔数不超过 $q+T-1=q+d/2$。

## 4. 与真实非primitive图的距离及原窗口费用

(2.4)、(3.3) 给
$$
\begin{aligned}
\|(\mathcal Z_2-\mathcal J_2)f\|
&\le\epsilon_m\left[13+
90\mathcal L^2\sum_{t=1}^{T-1}(t+1)(12\mathcal L)^{t-1}\right]\|f\|\\
&\le\vartheta_{2,m,q}\|f\|,
\end{aligned}
$$
其中可明确取
$$
\boxed{
\vartheta_{2,m,q}
=128T^2\mathcal L^2(12\mathcal L)^{T-2}\eta_{m-3}.
}
\tag{4.1}
$$
最后只用了 $\mathcal L\ge1$、$T\ge2$ 和
$\sum_{t=1}^{T-1}(t+1)(12\mathcal L)^{t-1}
\le T(T-1)(12\mathcal L)^{T-2}$。
所有输入孔层一起估计，未按 $q$ 个层额外求和。

由 $q\ge4d$、$m+1\le d$ 及 $T=d/2+1$，有 $\mathcal L\le2048q^2$。再用原 $\eta$ 的准确式，
$$
\log\eta_{m-3}
=-\frac{175}{512}d^4+\frac{315}{256}d^3-\frac{75}{2}d,
$$
于是
$$
\begin{aligned}
\log\vartheta_{2,m,q}
\le{}&-\frac{47}{512}d^4+\frac{443}{256}d^3-\frac{75}{2}d\\
&+T\log24576+2\log T+\log(128/144).
\end{aligned}
\tag{4.2}
$$
这里 $(d+2)\log q\le d^4/4+d^3/2$；多出的 $d^3/2$ 正是一般核阶二所需的额外一阶原像费用，没有省去。
对 $d\ge64$，$\log24576<11$、$2\log T\le d$，所以上式的线性项与对数项之和为负。又
$$
\frac{47}{512}-\frac{443}{256d}
\ge\frac{1061}{16384}>\frac1{20}.
$$
故
$$
\boxed{\vartheta_{2,m,q}\le e^{-d^4/20}.}
\tag{4.3}
$$
这适用于原合法窗口内的全部 $q$，没有扩大 lift 的原范围。

## 5. 原 W 角度：完整提升，保实际来源

(3.5) 的核向量均在原有限孔空间 $\mathcal H_{\le q+d/2}$ 中，且
$q+d/2\le q_m+d<e^{d^3/3}$。
既有原线性提升 $\Lambda$ 因而给
$$
\Lambda\mathcal Z_2f\in N,
\qquad
\|(\Lambda-I)\mathcal Z_2f\|
\le\delta_m\|\mathcal Z_2f\|,
\qquad \delta_m=e^{-75d^4}.
\tag{5.1}
$$
其完整有限孔定理不要求有限位置支撑。
由 (1.3) 与 (4.3)，$\|\mathcal Z_2\|\le\sqrt{1+\nu_m^2}+\vartheta_{2,m,q}<3$。于是
$$
\|\Lambda\mathcal Z_2-\mathcal J_2\|
\le\vartheta_{2,m,q}+3\delta_m
\le2e^{-d^4/20}.
\tag{5.2}
$$
对 $w\in W=N^\perp\cap M$ 取伴随即得 (1.4) 的第一式及 (1.5)。

由 (1.3)，$\mathcal J_2^*\mathcal J_2\ge I$，且
$$
P_{\mathcal G_{2,m,q}}
=\mathcal J_2(\mathcal J_2^*\mathcal J_2)^{-1}\mathcal J_2^*.
$$
其中 $\|\mathcal J_2(\mathcal J_2^*\mathcal J_2)^{-1}\|\le1$。这证明 (1.4) 的第二式，未把 $\mathcal J_2$ 当成等距映射。

## 6. 任意原源：跨 q 切开后保全部输入旗

令 $z^- =P_{\le q}\mathcal Z_2 f$，$z^+=P_{[q+1,q+d]}\mathcal Z_2 f$。由 $L\mathcal Z_2f=0$，左块属于原 $\mathscr V_q$。

右块只有 (3.4) 中的求和项。若输入属于第 $n\le q$ 孔层，第 $t$ 项位于 $n+t=q+k$，所以 $t\ge k\ge1$。其头指标满足
$$
i\le T-t-1\le d-k,
$$
而由 (3.2)，尾核阶至多为 $t+2$。由于 $T\le d-1$，
$$
d-i\ge d-T+t+1\ge t+2.
$$
故每个右分量均在原旗 $e_i\ker D^{d-i}$ 内。内部方程直接继承 (3.5)，右端也准确消失，因此 $z^+\in\ker S$，并有
$$
E_qz^-+F_{\rm flag}z^+=0.
\tag{6.1}
$$
原左源旗亦由 $z^-\in\mathscr V_q$ 和 $q\ge d$ 自动满足；没有删去一般非primitive左块的低孔层。

对定理二的 $v,c^\flat$，置 $x=v+c^\flat$，按原左右孔层嵌入，则
$$
\|x\|^2=\mu_q(r)^2+\lambda_q(r^\flat)^2.
$$
由 (6.1) 及 $v=E_q^*y,c^\flat=F_{\rm flag}^*y$，有 $x\perp\operatorname{Ran}\mathcal Z_2$。而 $\mathcal J_2$ 的像全在左侧，故
$$
\mathcal J_2^*v=\mathcal J_2^*x
=-(\mathcal Z_2-\mathcal J_2)^*x.
$$
(4.3) 和上一节的闭图投影公式给 (1.6)。这一步对任意原源成立，未把它替换成图投影后的源。

## 7. 新增范围及保留的缺口

对 $f\in\ker D$，(1.2) 退化为 $h_0\otimes f$，正是高孔笔记 §14 已覆盖的方向。本稿的新部分为
$$
\mathcal J_2\left((\ker D^2\ominus\ker D)\cap\mathcal H_{\le q}\right).
$$
它与 $h_0\otimes(\ker D\cap\mathcal H_{\le q})$ 正交：第一头配对由尾正交消失，第二头与 $h_0$ 正交。固定层 $D$ 的已证满射还保证存在 $D^2f=0$ 而 $Df\ne0$ 的输入，所以这一图部分不是空的。

(1.5) 中的两个头和 $D^*$ 必须一起保留。它没有分别给出 $h_0\otimes\ker D^2$、$h_1\otimes\ker D$ 的投影上界；两项可以相消。一般 $\ker D^s$ 的更高图、全部头方向以及真实窄源的完整左费用仍未控制。特别，(1.6) 的右侧仍保留 $\mu_q(r)$，不能循环使用它推出三 Gram 上界。

本稿给出的是全尾位置、原实际来源和原合法窗口内的非primitive图观测。普通 ISP、无权 $N=M$ 及完整源比较均继续开放。
