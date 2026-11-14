# R271 附录：原裸最小链的最低深度 primitive 源与 Euler 压缩

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_continue。

状态：**已证明。** 本文接续[真幂 MP 首段参数化](R271-appendix-bare-low-chain-parametrization-by-true-power-inverses.md)，将原裸最小者的全部首段 primitive 自由度准确消去。原高出生返回只由各低输入段的最低允许核深度部分产生；这些部分的真实滤波 primitive 源是一个显式正交投影后的 tuple。这个投影保留同一原首源、全部头旗和完整孔层 Gram。本文没有控制高链逆作用后的费用。

## 1. 原首段度量与实际 primitive Gram

固定原 $m\ge5$、$d=2^m$ 和合法 $q$，记 $A=A_m,D=D_m,p=q+1$。沿用
$$
E_{h,\ell}=\ker(D^h|_{\mathcal H_\ell}),\qquad
W_{h,\ell}=E_{h,\ell}\ominus E_{h-1,\ell},\qquad K_\ell=E_{1,\ell}.
$$
完整首段空间及首源空间分别是
$$
\mathscr X_q=\bigoplus_{i=0}^{d-1}e_iE_{d-i,p},\qquad
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,p-1}.
\tag{1.1}
$$
记 $D_X=D|_{\mathscr X_q}:\mathscr X_q\to\mathscr R_q$，以及
$$
U_j=(D^j|_{\mathcal H_{p+j}})^\dagger:
\mathcal H_p\longrightarrow\mathcal H_{p+j},\qquad U_0=I.
$$
前稿已在完整原旗中证明
$$
(\mathcal T x)_{j+1}=(-1)^jU_jA^jx,\qquad 0\le j<d,
\tag{1.2}
$$
给出 $\mathscr X_q$ 到原裸低链核 $Z_q=\ker S_L$ 的有界双射，且
$$
\alpha_q(r)^2=\min_{D_Xx=r}\|\mathcal T x\|^2.
\tag{1.3}
$$
所有核、正交补和范数均来自原 Hilbert 空间。

令 $K=K_p$。在**整个**源孔层 $\mathcal H_p$ 上先定义
$$
F_j=D^j(D^*)^j,\qquad F_0=I,
$$
再定义真正 primitive 最小逆及其 Gram
$$
J_j=U_j|_K,\qquad
H_j=J_j^*J_j=P_KF_j^{-1}|_K,\qquad H_0=I_K.
\tag{1.4}
$$
原尾固定有限孔层上的幂删除满射，因此这些逆有界；本文只使用有限多个这样的层。这里没有先压缩 $F_j$ 再取逆，$H_j$ 也没有乘阶乘正规化。

$J_j$ 是 $K$ 到 $W_{j+1,p+j}$ 的有界双射。事实上，$D^jJ_j=I$，$J_jK\perp E_{j,p+j}$，且 $D^{j+1}J_jK=0$。反过来，对 $w\in W_{j+1,p+j}$，有 $D^jw\in K$；由正交最小原像唯一性，$w=J_jD^jw$。特别
$$
H_j\succeq\|D^j|_{\mathcal H_{p+j}}\|^{-2}I_K
$$
（$j=0$ 直接为恒等），所以每个 $H_j^{-1}$ 有界，并且
$$
P_{W_{j+1,p+j}}=J_jH_j^{-1}J_j^*.
\tag{1.5}
$$

## 2. 最低允许核深度的真实源坐标

第 $j+1$ 段低输入的尾核深度至少为 $j+1$。定义它的最低深度直和
$$
\mathscr L_{\min}
=\bigoplus_{j=0}^{d-1}
\bigoplus_{i=0}^{d-j-1}e_iW_{j+1,p+j}
\ \subseteq\ \mathscr X_{L,q},
\tag{2.1}
$$
并记其在原低输入空间中的正交投影为 $P_{\min}$。

使用等距源空间
$$
\mathcal E_j=\operatorname{span}\{e_0,\ldots,e_{d-j-1}\}\otimes K,
\qquad
\mathcal E=\bigoplus_{j=0}^{d-1}\mathcal E_j.
$$
定义 $\mathcal I:\mathcal E\to\mathscr L_{\min}$：
$$
(\mathcal I\xi)_{j+1}=(-1)^jJ_jH_j^{-1/2}\xi_j.
\tag{2.2}
$$
由 (1.4)，每个 $J_jH_j^{-1/2}$ 是等距满射；故 $\mathcal I$ 是等距满射。

对 $x\in\mathscr X_q$，定义**实际滤波源**
$$
\rho_j(x)=P_KF_j^{-1}A^jx,
\qquad
\xi_j(x)=H_j^{-1/2}\rho_j(x).
\tag{2.3}
$$
$A^j$ 将头指标至少降低 $j$，所以这些向量确实属于所显示的头空间。由于
$$
J_j^*U_j=P_KU_j^*U_j=P_KF_j^{-1},
$$
(1.5) 给出
$$
\boxed{P_{\min}\mathcal T x=\mathcal I\xi(x).}
\tag{2.4}
$$
因此
$$
\boxed{\sum_{j=0}^{d-1}\|\xi_j(x)\|^2\le\|\mathcal T x\|^2.}
\tag{2.5}
$$
这里 $\rho_j(x)$ 先经过完整 $F_j^{-1}$ 再取 primitive 投影；一般不能替换为 $A^jP_Kx$。也没有声称 $P_{\min}$ 保持 $Z_q$。

## 3. 首段零源自由度全部落在最低深度

首段零源空间准确为
$$
\mathscr K:=\ker D_X=\mathbb C^d\otimes K.
\tag{3.1}
$$
定义有界行算子 $Q:\mathcal E\to\mathscr K$，
$$
Q\xi=\sum_{j=0}^{d-1}(A^j)^*H_j^{1/2}\xi_j.
\tag{3.2}
$$
头算子与各尾算子交换；$Q^*$ 的第 $j$ 分量为 $H_j^{1/2}A^jg$，自动满足 $\mathcal E_j$ 的头旗。因此
$$
QQ^*=\sum_{j=0}^{d-1}(A^j)^*H_jA^j\succeq I_{\mathscr K}.
\tag{3.3}
$$
该算子有有界逆，且正是完整首段度量 $\mathcal T^*\mathcal T$ 在 $\mathscr K$ 上的真实压缩。

对任意 $g\in\mathscr K$，$A^jg$ 仍是 primitive。故 $U_jA^jg=J_jA^jg$，(1.2) 与 (2.2) 立即给
$$
\boxed{\mathcal T g=\mathcal I Q^*g.}
\tag{3.4}
$$
特别，首段的全部零源自由修正只改变 (2.1) 中的最低深度部分；它不能改变低输入其余深度部分。这是原完整链与首段自由坐标之间的准确关系。

## 4. 裸最小者的 Euler 方程与显式源投影

给定原首源 $r\in\mathscr R_q$，令
$$
x_0=D_X^\dagger r,
\qquad \xi^0=\xi(x_0),
\qquad b_0=(I-P_{\min})\mathcal T x_0.
$$
所有可行首段恰为 $x_0+g$，$g\in\mathscr K$。由 (2.4)、(3.4) 和正交分解，
$$
\|\mathcal T(x_0+g)\|^2
=\|b_0\|^2+\|\xi^0+Q^*g\|^2.
\tag{4.1}
$$
定义 $\mathcal E$ 上的正交投影
$$
\Pi=I_{\mathcal E}-Q^*(QQ^*)^{-1}Q,
\qquad\operatorname{Ran}\Pi=\ker Q.
\tag{4.2}
$$
由 (3.3)，(4.1) 的最小者唯一，且精确为
$$
\boxed{
x_r=x_0-(QQ^*)^{-1}Q\xi^0,
\qquad\xi(x_r)=\Pi\xi^0.
}
\tag{4.3}
$$
第一式中的修正向量按 (3.1) 嵌入原 $\mathscr X_q$。因而
$$
\boxed{
\alpha_q(r)^2=\|b_0\|^2+\|\Pi\xi^0\|^2.
}
\tag{4.4}
$$
这也说明普通首段最小原像 $x_0$ 一般不等于原裸链最小者的首段 $x_r$。

最小者的 Euler 方程为
$$
\boxed{Q\xi(x_r)=0,}
\tag{4.5}
$$
即
$$
P_Kx_r+
\sum_{j=1}^{d-1}(A^j)^*P_KF_j^{-1}A^jx_r=0.
\tag{4.6}
$$
该式耦合的是同一个 $x_r$ 产生的实际滤波源，没有逐高度另选输入。

若使用原始坐标 $\rho_j=H_j^{1/2}\xi_j$，则其内积是
$\sum_j\langle H_j^{-1}\rho_j,\rho_j\rangle$。令
$\widetilde Q\rho=\sum_j(A^j)^*\rho_j$，对应投影准确为
$$
I-\operatorname{diag}(H_j)\widetilde Q^*
\left[\sum_j(A^j)^*H_jA^j\right]^{-1}\widetilde Q.
\tag{4.7}
$$
(4.7) 在刚才显示的加权内积中正交，不能把它当成原始 $\rho$ 坐标的普通 Euclidean 正交投影。

## 5. 原高出生返回只读取这个投影后的源

纯尾的两带删除结构是
$$
DW_{h,\ell}\subseteq W_{h-1,\ell-1}\oplus W_{h-2,\ell-1}.
\tag{5.1}
$$
它由 $\operatorname{ad}_D^3(D^*)=0$ 给出；见[占据交换子稿 §4](R271-appendix-occupation-commutator-known-source-minimum-energy.md)。记第二下降块为
$$
\mathcal B_{h,\ell}=P_{W_{h-2,\ell-1}}D|_{W_{h,\ell}}.
$$
原高输出第 $j$ 段为
$$
\mathscr Y_{H,q,j}
=\bigoplus_{i=0}^{d-j-1}e_iE_{\min\{d-i-1,j-1\},q+j}
\qquad(1\le j<d).
\tag{5.2}
$$
第 $j$ 个低输入段的深度至少为 $j$；$A$ 保持尾深度，因此它对 (5.2) 的投影为零。第 $j+1$ 个低输入段的深度至少为 $j+1$；由 (5.1)，只有深度恰为 $j+1$ 的第二下降能进入 (5.2)，其余深度的输出仍至少为 $j$。显示的头上界同时保证这一第二下降落在原高输出旗内。

因此定义实际返回算子 $\mathcal R:\mathcal E\to\mathscr Y_{H,q}$：
$$
(\mathcal R\xi)_j
=(-1)^j\mathcal B_{j+1,p+j}J_jH_j^{-1/2}\xi_j,
\qquad1\le j<d.
\tag{5.3}
$$
其中 $j=1$ 项为零。若 $B_q=P_{\mathscr Y_H}S|_{Z_q}$，上述逐段投影计算给
$$
\boxed{B_q\mathcal T x=\mathcal R\xi(x).}
\tag{5.4}
$$
将 (4.3) 代入，原裸最小链 $a_q(r)=\mathcal T x_r$ 的高出生返回精确为
$$
\boxed{B_qa_q(r)=\mathcal R\Pi\xi^0.}
\tag{5.5}
$$
本证明只对实际内部输出取高出生投影；没有先断言 $P_{\min}\mathcal T x\in Z_q$。这避免了把最低深度部分错误地当成独立可行链。

### 5.1 完整 Gram 滤波和 $D_3$ 的准确次序

令 $C=D_3=\sum_{\ell\ge m}a_\ell^3E_\ell$，并记其真正 primitive 限制
$$
C_K=C|_{K_{p+1}}:K_{p+1}\longrightarrow K_p.
$$
由 $[D,C]=0$，该限制合法。令 $K_j^{\rm def}=DU_j-U_{j-1}$。前稿给
$\operatorname{Ran}K_j^{\rm def}\subseteq E_{j-1,p+j-1}$，且 $K_1^{\rm def}=0$。对 $j\ge2$，有
$$
(K_j^{\rm def})^*
=-j(j-1)F_j^{-1}CD^{j-2}P_{E_{j-1,p+j-1}}.
\tag{5.6}
$$
证明如下。对 $y\in E_{j-1,p+j-1}$，$U_{j-1}^*y=0$；又
$$
D^jD^*
=D^*D^j+j[D,D^*]D^{j-1}-j(j-1)CD^{j-2}.
$$
前两项作用于 $y$ 后为零，而 $U_j^*=F_j^{-1}D^j$，所以得到 (5.6)。对一般 $y$ 先投影到这个真实范围即可。

在 (5.6) 中 $D^{j-2}P_{E_{j-1}}$ 的值域是 $K_{p+1}$。取真正受限伴随后，(5.3) 等价于
$$
\boxed{
(\mathcal R\xi)_j
=(-1)^{j+1}j(j-1)
P_{W_{j-1,p+j-1}}(D^*)^{j-2}C_K^*H_j^{1/2}\xi_j.
}
\tag{5.7}
$$
这里确为 $H_j^{1/2}$：将 (5.6) 作用于 primitive 输入 $H_j^{-1/2}\xi_j$ 时，真实压缩 $P_KF_j^{-1}|_K=H_j$ 使其变为 $H_j^{1/2}\xi_j$。$C_K^*$ 含 $K_{p+1}$ 的正交投影，不能替换为不受限的 $C^*$。

对原始源 $x$，(5.7) 中的 $H_j^{1/2}\xi_j(x)$ 正是 $P_KF_j^{-1}A^jx$。因此这个式子保留了完整层的 inverse Gram 滤波；它不把任意 $D_3$ 像的已付原像估计，直接套到被滤波的源上。

## 6. 尚需支付的原同源量

原高链修复要控制的对象仍是
$$
\boxed{S_H^\dagger\mathcal R\Pi\xi^0.}
\tag{6.1}
$$
本文给出真实最小者的源限制 $\Pi\xi^0\in\ker Q$ 及同源预算
$\|\Pi\xi^0\|\le\alpha_q(r)$。它没有给 (6.1) 一个温和范数界；原左完整源度量及其最小费用也未被替换。

此外，$\xi^0$ 仍由同一个原首源 $r$ 经 $x_0=D_X^\dagger r$ 和 (2.3) 产生。本文没有声称 $\ker Q$ 中每个 tuple 都可由实际首源实现。若能在整个 $\ker Q$ 上控制 (6.1)，那将是充分的更强估计；此处既未假定它，也未将它作为已经证明的等价命题。

本文结论是 (4.3)--(4.6)、(5.5) 的原最小者准确压缩。它不推出一般相邻 primitive Gram 常数、顺次单步逆与真幂逆的一致比较，或无权 $N=M$。
