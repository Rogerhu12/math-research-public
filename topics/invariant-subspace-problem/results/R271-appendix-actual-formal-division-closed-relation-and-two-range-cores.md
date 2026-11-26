# 原形式单位的实际闭图：唯一多值方向与两道除法核心

日期：2026-11-27（Asia/Taipei）；2026-11-26（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：本稿闭关系身份均已证明；$N=M$ 仍未证明。**
本稿只处理原两种实际边界算子，不删除 carry。它与 R187 的循环主理想陈述不同：这里把形式 $F(z)/z$ 的最小图闭包、最大形式乘法域和真实闭包范围分别具体化，指出还需支付的两个核心，而不由循环性推出未知缺陷维数。

## 1. 原对象与有限支撑除法

沿用
$$
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),\qquad Be_0=0,
\qquad d_j=\prod_{\nu=1}^{2^j}\alpha_{v_2(\nu)},
$$
$$
T_N=\sum_{j\ge0}a_j\mathsf N_j,
\qquad T_Y=\sum_{j\ge0}a_j\mathsf N_j(I+\mathsf N_j)^{-1},
\qquad \mathsf N_j=B^{2^j}/d_j,\quad a_j=(j+1)^{-2}.
$$
以下 $T$ 可取任一种，$M=\ker T$、$N=\overline{BM}$、$S=B^*$，并记
$$
\mathcal I=M^\perp=\overline{\operatorname{Ran}T^*},
\qquad P_0=I-e_0\otimes e_0.
$$
这里 $P_0$ 投去真空，并非有限头投影。

记 $\mathcal P$ 为有限支撑向量空间，令
$$
J_B e_n=\alpha_{v_2(n+1)}^{-1}e_{n+1}.
$$
$J_B$ 是最大定义域 $\operatorname{Ran}B$ 上的闭右移，值域在 $e_0^\perp$；在 $\mathcal P$ 上没有域问题。定义
$$
G_0=TJ_B:\mathcal P\longrightarrow\mathcal P.
\tag{1.1}
$$
所有实际级数在有限支撑上终止。$B,T$ 交换，且 $Te_0=0$，所以
$$
G_0 Bx=Tx,\qquad BG_0x=Tx\qquad(x\in\mathcal P).
\tag{1.2}
$$
在 R200 的加权形式级数实现中，$T^*=M_F$，故 $G_0$ 的形式伴随符号正是 $G=F/z$。以下并不以这个形式单位替代图收敛。

## 2. 图闭包的多值部恰为真空

令
$$
\mathcal R=\overline{\operatorname{Graph}G_0}
\subset\mathcal H\oplus\mathcal H.
$$
由 $B\mathcal P=\mathcal P$、$\ker B\subset\ker T$ 及 (1.2)，有准确身份
$$
\boxed{
\mathcal R=
\overline{\{(Bx,Tx):x\in\mathcal H\}}.
}
\tag{2.1}
$$
最后一步只用 $x\mapsto(Bx,Tx)$ 有界和 $\mathcal P$ 稠密，不把这个柱算子的值域称为闭值域。

对 $(u,v)\in\mathcal R$，由连续性恒有 $Bv=Tu$。因此
$$
\operatorname{mul}\mathcal R
:=\{v:(0,v)\in\mathcal R\}
\subset\ker B=\mathbb Ce_0.
\tag{2.2}
$$

为证明反向包含，取真实向量
$$
x_j=a_j^{-1}e_{2^j}\qquad(j\ge1).
$$
准确权乘积给
$$
\mathsf N_j e_{2^j}=e_0,\qquad
\mathsf N_i e_{2^j}
=\frac{\alpha_j}{\alpha_i}e_{2^j-2^i}\quad(0\le i<j),
\qquad \mathsf N_i e_{2^j}=0\quad(i>j).
\tag{2.3}
$$
N 型于是满足
$$
\|T_Nx_j-e_0\|
\le \frac{2\eta_{j-1}}{a_j},
\qquad \eta_{j-1}=\alpha_j/\alpha_{j-1}.
$$
Y 型使用 $\|(I+\mathsf N_i)^{-1}\|\le3$；当 $i=j$ 时 $\mathsf N_j^2e_{2^j}=0$，所以该项仍准确为 $e_0$。其余低项给
$$
\|T_Yx_j-e_0\|
\le \frac{6\eta_{j-1}}{a_j}.
\tag{2.4}
$$
这里用 $\sum_i a_i<2$，所有低项的比例均不超过 $\eta_{j-1}$。
同时
$$
\|Bx_j\|=\frac{\alpha_j}{a_j}\longrightarrow0,
\qquad
\frac{\eta_{j-1}}{a_j}\le(j+1)^2e^{-770\,16^{j-1}}\longrightarrow0.
$$
因此 $(0,e_0)\in\mathcal R$。结合 (2.2)，得到
$$
\boxed{\operatorname{mul}\mathcal R=\mathbb Ce_0.}
\tag{2.5}
$$
特别，原 $G_0$ **不可闭**；把它直接称为闭可逆的形式单位会先在这一处失效。

## 3. 投去多值方向后的最小、最大闭算子

由于 $\{0\}\oplus\mathbb Ce_0\subset\mathcal R$，准确有
$$
(I\oplus P_0)\mathcal R
=\mathcal R\cap(\mathcal H\oplus e_0^\perp).
$$
右侧是闭子空间，而且零输入只对应零输出，故它是一个闭算子的图。记该算子为 $A_{\min}$。连续投影与稠密性也给
$$
\boxed{A_{\min}=\overline{P_0G_0}.}
\tag{3.1}
$$
于是 $P_0G_0$ 可闭；这一操作明确移除了 (2.5) 的唯一多值方向。

另定义
$$
A_{\max}=J_BT,
\qquad
\mathcal D(A_{\max})
=\{u\in\mathcal H:Tu\in\operatorname{Ran}B\}.
\tag{3.2}
$$
它是从 $\mathcal H$ 到 $e_0^\perp$ 的闭算子：若 $u_n\to u$、$J_BTu_n\to v$，则 $Tu_n\to Tu$，由 $J_B$ 闭性得到 $u\in\mathcal D(A_{\max})$ 和 $J_BTu=v$。从 (1.2) 得
$$
\boxed{A_{\min}\subset A_{\max},\qquad\ker A_{\max}=M.}
\tag{3.3}
$$

对所有 $x\in\mathcal H$，以有限支撑 $x_n\to x$ 代入 (1.2)，有
$$
\boxed{Bx\in\mathcal D(A_{\min}),\qquad A_{\min}Bx=P_0Tx.}
\tag{3.4}
$$
因此 $BM\subset\ker A_{\min}$。核闭，故
$$
\boxed{N\subset\ker A_{\min}\subset M.}
\tag{3.5}
$$
两端可以写成明确算子核，中间仍不能自动消失。

## 4. 真实伴随域：最大形式乘法的准确含义

$G_0^*$ 的定义直接给
$$
y\in\mathcal D(G_0^*)
\iff\exists z\in\mathcal H:\ T^*y=S z.
$$
这里 $S$ 单射，所以 $z$ 唯一。于是
$$
\boxed{
\mathcal D(G_0^*)
=\{y:T^*y\in\operatorname{Ran}S\},
\qquad SG_0^*y=T^*y.
}
\tag{4.1}
$$
在加权形式级数中，这恰是最大乘法域
$$
\mathcal D(G_0^*)=\{y:Gy\in\mathcal H\},\qquad G_0^*y=Gy.
\tag{4.2}
$$
(4.2) 的 Hilbert 条件不可删除。

由 (2.5)，$\mathcal D(G_0^*)\subset e_0^\perp$。另一方面 $T^*S=ST^*$，所以
$$
\boxed{
S\mathcal H\subset\mathcal D(G_0^*),
\qquad G_0^*S=T^*.
}
\tag{4.3}
$$
因为 $\overline{S\mathcal H}=e_0^\perp$，得到
$$
\boxed{\overline{\mathcal D(G_0^*)}=e_0^\perp.}
\tag{4.4}
$$
把 $A_{\min}$ 视为 $\mathcal H\to e_0^\perp$ 的稠密定义闭算子时，其伴随就是上述 $G_0^*$，定义域按 $e_0^\perp$ 中的稠密域理解。

## 5. 两个不能混淆的闭包范围核心

令
$$
\mathcal J=\overline{\operatorname{Ran}G_0^*}.
$$
(4.3) 给 $\mathcal I\subset\mathcal J$。若 $z=G_0^*y$，则 $Sz=T^*y\in\mathcal I$。R200 的真实身份
$$
N^\perp=\{z:Sz\in\mathcal I\}
$$
于是给反向上界。合起来是
$$
\boxed{
\mathcal I\subset\mathcal J\subset N^\perp,
\qquad
\ker A_{\min}=\mathcal J^\perp.
}
\tag{5.1}
$$
这正是 (3.5) 的对偶。

因此，若把这条实际闭图作为终端，所需的是两道真实核心：

1. $\mathcal J=\mathcal I$，等价于 $\ker A_{\min}=M$。一个充分输入是 $S\mathcal H$ 在 (4.1) 的图范数中为核心，因为其像由 (4.3) 正是 $\operatorname{Ran}T^*$。
2. $\mathcal J=N^\perp$，等价于 $\ker A_{\min}=N$。它要求精确可除的 $T^*$ 值域在全部闭包可除源中足够稠密，不能由 $\overline{\operatorname{Ran}T^*}=\mathcal I$ 直接换序得到。

两道都成立才从 (5.1) 得到 $N=M$；单独证明第一道仍只得到最小图核等于最大图核，不能自动识别为稳定范围。单独证明第二道也没有给出整个 $M$ 的图核心。

这里“多值部一维”和 R187 的“主理想循环”均没有限制 $\dim(M\ominus N)$。新的作用是把被隐藏的闭图对象和两次闭包换序分别写清，并给两种原模型共同的精确多值方向与显式趋近列。
