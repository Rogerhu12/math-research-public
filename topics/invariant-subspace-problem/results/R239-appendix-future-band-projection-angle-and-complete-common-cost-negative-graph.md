# R239 附录：同一未来带的双投影角、全部共同费用负图与高谱带校正

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文从真实未来带的裸/完整平坦两个投影，导出精确的正角算子关系。实际前缀源不仅满足核头负图，还在全部裸费等于完整右费的方向满足负图；更一般的高角谱带缺陷由同一个未来带能量支付。完整正 resolvent 可将实际族送入这个更强负图，保全部原核头条件、同一强极限与累计两费用。低 C 谱补上的完整左 Schur 比较仍未闭合，普通 ISP 与 $N=M$ 仍为 OPEN。

本稿适用于原 regular 有限头及天然四块退化模型。所有右空间都保持各自已经指定的完整物理右旗、低出生裸旗及天然源限制；不替换为 Jordan 度量。

## 1. 同一个物理右带内的两种最小者

在一个固定参数的闭源空间 $\mathscr R$ 上，记裸最小链映射为
$$
A_b:\mathscr R\to\mathscr U_b,
\qquad B=A_b^*A_b>0,
$$
完整右映射为 $F:\mathscr C\to\mathscr R$，其最小链为 $F^\dagger r$，且
$$
G=FF^*>0,\qquad (F^\dagger)^*F^\dagger=G^{-1}.
$$
$\mathscr U_b$ 是低出生物理右空间中的闭子空间；$\mathscr U_f=\operatorname{Ran}F^*$ 是完整最小右空间。两者均嵌入同一个物理右带，投影分别为 $P_b,P_f$。

任意完整可行链 $F^\dagger s$ 的低出生投影都是源 $s$ 的裸可行链。它与裸最小者之差属于裸零源核。因此有准确向量恒等式
$$
\boxed{P_bF^\dagger s=A_bs.}
\tag{1.1}
$$
这里 $P_bP_L=P_b$ 已使用；没有将完整链本身误放进裸低输入空间。于是
$$
A_b^*F^\dagger=B,\qquad B\preceq G^{-1}.
\tag{1.2}
$$

定义裸归一的角算子
$$
\boxed{C=B^{1/2}GB^{1/2},\qquad 0<C\preceq I.}
\tag{1.3}
$$
固定参数下 $C$ 严格正，但 $I-C$ 不要求严格正或有闭值域。

## 2. 保持非交换顺序的两等距映射

定义
$$
V_b=A_bB^{-1/2},\qquad
V_f=F^\dagger B^{-1/2}C^{1/2}.
\tag{2.1}
$$
它们分别是同一个源 Hilbert 空间到 $\mathscr U_b,\mathscr U_f$ 的等距同构。第二个等距性准确使用
$$
B^{-1/2}G^{-1}B^{-1/2}=C^{-1},
$$
而不是交换 $B$ 与 $G$。由 (1.1)，
$$
\boxed{V_b^*V_f=C^{1/2}.}
\tag{2.2}
$$

令 $W=(I-P_b)V_f$。则
$$
W^*W=I-C.
$$
其极分解可以写成
$$
W=V_\perp(I-C)^{1/2},
\tag{2.3}
$$
其中 $V_\perp$ 是从 $\overline{\operatorname{Ran}(I-C)}$ 到
$\overline{\operatorname{Ran}W}\subseteq\mathscr U_b^\perp$ 的等距映射，在其正交补上取零。因此
$$
\boxed{V_f=V_bC^{1/2}+V_\perp(I-C)^{1/2}.}
\tag{2.4}
$$
这个形式允许 $C=1$ 的共同方向和 $I-C$ 非闭值域，不隐含有界逆。

## 3. 同一未来带迫使一个精确的加号关系

令 $L=J_{\rm left}^{-1}$，并记
$$
u=B^{1/2}r,\qquad H=B^{-1/2}LB^{-1/2}\succeq0.
$$
假设 $r$ 是某个更高真正左最小者 $v_{\rm top}$ 的前缀源，并且它的完整未来带包含在顶部支持内。记该同一未来带为 $y$。前缀最小性与全部完整测试已经给
$$
\boxed{A_br=-P_by,\qquad c^\flat(r)=F^*Lr=P_fy.}
\tag{3.1}
$$
第一式包含真实低出生投影，因为 $P_bP_L=P_b$。这是实际来源条件，不对任意独立选取的源免费假定。

由 (2.1)、(3.1)，
$$
V_b^*y=-u,\qquad
V_f^*y=C^{1/2}Hu.
\tag{3.2}
$$
后一式使用
$(F^\dagger)^*F^*=I_{\mathscr R}$。将 (2.4) 代入，令
$$
z=V_\perp^*y\in\overline{\operatorname{Ran}(I-C)},
$$
得到
$$
\boxed{(I-C)^{1/2}z=C^{1/2}(I+H)u.}
\tag{3.3}
$$
这里必须是 $I+H$：裸投影的负号使两项相加，不能将它改成 $I-H$。

由于 $V_b$ 与 $V_\perp$ 的像正交，
$$
\boxed{\|u\|^2+\|z\|^2\le\|y\|^2.}
\tag{3.4}
$$
这是一条比单独相加两个投影范数更精确的同向量预算。

## 4. 全部共同费用方向的准确负图

定义
$$
\mathscr E_1=\ker(I-C),\qquad P_1=P_{\mathscr E_1}.
$$
式 (3.3) 立即迫
$$
\boxed{P_1(I+H)u=0.}
\tag{4.1}
$$

这些方向在原源中准确对应
$$
\mathscr S_{\rm eq}=\ker(G^{-1}-B),\qquad
\mathscr E_1=B^{1/2}\mathscr S_{\rm eq}.
\tag{4.2}
$$
因为 $C B^{1/2}s=B^{1/2}s$ 等价于 $GBs=s$。在这些源方向上，裸最小链与完整最小链是同一个物理向量；反之，若两费用相等，则完整链的高出生部分以及低部分的裸零源余量都必须为零，因此两个最小链相同。

故 (4.1) 的原源形式是
$$
\boxed{\langle(L+B)r,s\rangle=0
\quad\text{对全部 }s\in\mathscr S_{\rm eq}.}
\tag{4.3}
$$
对原头或模型，先前全部核头源空间
$\mathscr S_0=\ker T\cap\mathscr R$ 满足
$Bs=G^{-1}s$，故包含在 $\mathscr S_{\rm eq}$。因此 (4.3) 保留完整核头负图，并可能严格加强它。本文不声称 (4.3) 单独刻画某个有限步源流的像。

还有准确值域信息：
$$
C^{1/2}(I+H)u\in\operatorname{Ran}(I-C)^{1/2}.
\tag{4.4}
$$
在 $\mathscr E_1^\perp$ 上的可能无界逆作用于这个已证明属于其域的向量，并有
$$
\boxed{
\|u\|^2+
\left\|(I-C)^{-1/2}C^{1/2}(I+H)u\right\|^2
\le\|y\|^2.
}
\tag{4.5}
$$
不把 $(I-C)^{-1/2}$ 称为有界算子。

## 5. 高 C 谱带缺陷的同未来带支付

对固定 $0<c<1$，令
$$
E_c=1_{[c,1]}(C),\qquad
d_c=E_c(I+H)u,\qquad
\varphi_c=\sqrt{(1-c)/c}.
$$
由 (3.3) 的谱演算以及 (4.1) 的端点条件，
$$
d_c=E_c C^{-1/2}(I-C)^{1/2}z.
$$
所以
$$
\boxed{\|d_c\|\le\varphi_c\|z\|
\le\varphi_c\|y\|.}
\tag{5.1}
$$
这不要求 $E_c$ 与 $H$ 交换，也不由物理头的支撑推得。

现在使用完整正 resolvent，定义
$$
t_c=B^{-1/2}(I+H)^{-1}d_c,\qquad r_c=r-t_c.
\tag{5.2}
$$
因为 $C\preceq I$，同一个正算子证明给
$$
\boxed{
E_c(I+H)B^{1/2}r_c=0,
}
\tag{5.3}
$$
$$
\boxed{
\chi(t_c)^2+2\mu(t_c)^2\le\|d_c\|^2,\qquad
\mu(t_c)\le\tfrac12\|d_c\|
\le\tfrac12\varphi_c\|y\|.
}
\tag{5.4}
$$
由于 $\mathscr E_1\subseteq E_c\mathscr R$，校正后的源仍满足 (4.3)，因而也保留全部真实核头负图。普通完整右费没有由 (5.4) 控制。

又由原两投影 $\chi(r)\le\sqrt2\|y\|$，
$$
\boxed{\chi(r_c)\le(\sqrt2+\varphi_c)\|y\|.}
\tag{5.5}
$$
这给可逐窗求和的实际预算，而非只把源送到一个未付费用的图。

## 6. 单一顶部模型族的准确运输预算

将 §5 逐窗用于退化头完整源流稿中的同一个天然模型顶部 $v_\square$。对
$s\in I_m^\square=\{4d,\ldots,Q-2d\}$，记
$$
y_s=P_{[s+1,s+d]}v_\square.
$$
该稿已证明
$$
\sum_s\|y_s\|^2\le d(t_m+\zeta_m)^2\|w\|^2,
\qquad
\sup_s\|y_s\|\le(t_m+\zeta_m)\|w\|,
$$
以及 $\mu_s(r_s)\ge\theta_m\|w\|$、$\theta_m\to1$。

对每窗使用该窗自己的 $B_s,H_s,C_s,E_{c,s}$ 和相同固定阈值 $c$，得到 $r_{c,s}$。则
$$
\boxed{
\sum_s\chi_s(r_{c,s})^2
\le(\sqrt2+\varphi_c)^2
d(t_m+\zeta_m)^2\|w\|^2,
}
\tag{6.1}
$$
其中 $(\sqrt2+\varphi_c)^2\le4/c$，所以累计平方费用明确付至多 $1/c$ 阶损失，未将它隐藏在固定常数内。

$$
\boxed{
\mu_s(r_{c,s})\ge
\left[\theta_m-\tfrac12\varphi_c(t_m+\zeta_m)\right]\|w\|.
}
\tag{6.2}
$$
同时真正左向量仍对窗口一致趋于同一个 $w$：
$$
\boxed{
\sup_s\|E_{\square,s}^\dagger r_{c,s}-w\|
\le(1+\tfrac12\varphi_c)(t_m+\zeta_m)\|w\|
\longrightarrow0.
}
\tag{6.3}
$$
所有校正源继续满足完整四核头负图及更强的 (5.3)。它们不被声明还共同组成逐孔源流；求和只用同一旧顶部未来带及每窗已经付清的校正。

例如取 $c=1/2$，则 $\varphi_c=1$，不付任何随 $m,q$ 增长的常数。阈值若随参数趋零，必须保留 (6.1)–(6.3) 中实际的 $\varphi_c$，不可免费令 $c\downarrow0$。

## 7. 余条件是低谱块上的完整左 Schur，不是支撑消失

为显示确切剩余量，在裸归一中按 $E=E_c$、$F=I-E$ 分块
$$
H=\begin{pmatrix}H_{EE}&H_{EF}\\H_{FE}&H_{FF}\end{pmatrix},
\qquad
C=C_E\oplus C_F.
$$
对校正后的 $u=B^{1/2}r_c$，(5.3) 准确给
$$
u_E=-(I+H_{EE})^{-1}H_{EF}u_F.
\tag{7.1}
$$
定义
$$
S_c^-=H_{FF}-H_{FE}(I+H_{EE})^{-1}H_{EF}.
$$
则保留全部交叉块的费用恒等式为
$$
\boxed{
\mu(r_c)^2=\langle S_c^-u_F,u_F\rangle-\|u_E\|^2,
}
\tag{7.2}
$$
$$
\boxed{
\chi(r_c)^2=
\|u_F\|^2+\langle(I+C_E)u_E,u_E\rangle
+\|C_F^{1/2}S_c^-u_F\|^2.
}
\tag{7.3}
$$
其中 $C_E\succeq cI$、$0<C_F<cI$；后者可以有很小的特征值。没有把 $u_E$ 设为零，也没有把 $S_c^-$ 换成 $H_{FF}$。

尚缺的是这些实际校正族上 (7.2) 被 (7.3) 以原合法窗可承受常数控制的估计。本文的新信息是：全部共同 bare/full 方向和任一固定高 C 谱带已被同一个真实未来带支付，剩余问题可精确放在低 C 谱块及其完整左 Schur 反馈上。


## 已付来源入口

完整物理未来带及模型实际窗族见[退化头完整源流](R239-appendix-degenerate-head-full-source-flow-and-model-window-family.md)；正resolvent费用见[完整负图缺陷校正](R239-appendix-positive-resolvent-negative-source-defect-correction.md)。本文保留这些稿件的完整右空间和原物理范数。
