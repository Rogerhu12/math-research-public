# R236 补充：真实二阶通常伴随域与中央耦合的有界乘积

日期：2026-11-12（UTC）。独占作者：critical_kernel。

状态：以下为完整的真实闭域结论。它从 R161 已证明的完整图二次型出发，补出二阶自然域等式，并把它用于 R236 的三块中央分解。新结论是中央耦合的实际图正则性和若干有界乘积；不把进入中央算子定义域误写成进入其值域，不据此排除未知危险核。

## A. 一个完整二阶域引理

**引理 A.1。** 设 $S$ 稠密定义且闭，
$$
\mathscr D=\operatorname{Dom}S=\operatorname{Dom}S^*,
$$
并有有界自伴 $C_0$ 满足完整极化等式
$$
\langle Sf,Sg\rangle-\langle S^*f,S^*g\rangle
=\langle C_0f,g\rangle
\quad(f,g\in\mathscr D).
\tag{A.1}
$$
内积对第一变量线性。则
$$
\boxed{
\operatorname{Dom}S^2
=\operatorname{Dom}(S^*)^2
=\operatorname{Dom}(S^*S)
=\operatorname{Dom}(SS^*).
}
\tag{A.2}
$$
在这个共同域上有真实算子等式
$$
\boxed{S^*S-SS^*=C_0.}
\tag{A.3}
$$
这些等式只在共同二阶域上断言；不把左侧未经定义的算子差称为全域运算。

**证明。** 因两个一阶域相同，
$\operatorname{Dom}S^2=\operatorname{Dom}(S^*S)$，
以及
$\operatorname{Dom}(S^*)^2=\operatorname{Dom}(SS^*)$。
取 $f\in\operatorname{Dom}(S^*S)$。对任意 $g\in\mathscr D$，
(A.1) 给
$$
\langle S^*f,S^*g\rangle
=\langle S^*Sf-C_0f,g\rangle.
$$
按 $(S^*)^*=S$ 的完整伴随域判据，
$S^*f\in\operatorname{Dom}S$，且
$SS^*f=S^*Sf-C_0f$。
这证明一个域包含及 (A.3)。交换 $S,S^*$，同时把 $C_0$ 换成 $-C_0$，得到反向包含。证毕。

令 $c=\|C_0\|$。还可得到不依赖任何二阶图核心的图范数估计。对共同二阶域中的 $f$，置
$$
u=\|S^*Sf\|,\qquad v=\|S^2f\|,\qquad z=\|f\|.
$$
通常伴随关系和 (A.1) 在 $Sf$ 上的使用给
$$
\|Sf\|^2\le uz,\qquad |v^2-u^2|\le c\,uz.
$$
于是
$$
\boxed{
u\le v+cz,\qquad v\le u+\frac c2z.
}
\tag{A.4}
$$
第二式来自 $u^2+cuz\le(u+cz/2)^2$；第一式来自二次不等式
$u^2-cuz-v^2\le0$。

$S^*S$ 是通常的非负自伴闭算子，因此 (A.4) 也独立证明 $S^2$ 闭。对 $S^*$ 同理。结合 $SS^*=S^*S-C_0$，还得到两个自然平方图范数相互等价，例如
$$
\|(S^*)^2f\|\le\|S^2f\|+\frac{5c}{2}\|f\|,
\tag{A.5}
$$
及交换 $S,S^*$ 后的反向界。

本引理没有推出所有更高自然幂域相等；高阶需要另付交换子或图域条件。

## B. R161 的实际输入确在完整域成立

R161 §4 已证明
$$
\operatorname{Dom}X=\operatorname{Dom}X^*
$$
以及其 (4.2)：
$$
\langle Xf,Xg\rangle-\langle X^*f,X^*g\rangle
=\langle C_af,g\rangle
\quad(f,g\in\operatorname{Dom}X).
\tag{B.1}
$$
这里的 $C_a$ 是实际有限和自交换子在算子范数中的极限，
$$
\|C_a\|\le(4+\varepsilon_{\rm carry})\|a\|_2^2.
$$
所以引理 A.1 适用，严格给出
$$
\boxed{
\operatorname{Dom}X^2=\operatorname{Dom}(X^*)^2,\qquad
X^*X-XX^*=C_a
}
\tag{B.2}
$$
在准确的共同二阶域上成立。

这补充了 R161 §1 当时保留的二阶域问题。没有仅由有限柱核心上的二次型作未经闭包验证的推断；完整极化式是本节不可省略的输入。

## C. Bell 分支的真实伴随交换子

现在取
$$
B_2=\sum_{j\ge0}a_j^2(I-V_j^2),\qquad
Y=\phi(B_2)\in\mathcal A,\qquad T=X-Y,
\tag{C.1}
$$
其中 $a\in\ell^2$，$\phi$ 是在零点邻域解析的标量函数，代入采用通常全纯演算。$B_2$ 的谱为 $\{0\}$；不要求 $\|B_2\|$ 小于某个 Taylor 半径。

令
$$
g=\|a\|_2,\qquad
L_\eta=\frac{1+\eta_*}{1-\eta_*}.
$$
R161 §5 已在真实完整域证明
$$
[X^*,N_j]=D_j,\qquad
\left(\sum_j\|D_j\|^2\right)^{1/2}\le36L_\eta g.
\tag{C.2}
$$
$V_j=2(I+N_j)^{-1}-I$，且实际逆范数至多 $3$。因为这个逆属于 $\mathcal A$，它保持 $\operatorname{Dom}X=\operatorname{Dom}X^*$。实际逆交换子公式给
$$
G_j:=[X^*,V_j]
=-2(I+N_j)^{-1}D_j(I+N_j)^{-1},
$$
因而
$$
\boxed{
\left(\sum_j\|G_j\|^2\right)^{1/2}
\le648L_\eta g.
}
\tag{C.3}
$$

由 $\|V_j\|\le6$，
$$
K_2:=-\sum_j a_j^2(G_jV_j+V_jG_j)
\tag{C.4}
$$
按算子范数绝对收敛，并且
$$
\boxed{
\|K_2\|
\le7776L_\eta g
\left(\sum_j|a_j|^4\right)^{1/2}
\le7776L_\eta g^3.
}
\tag{C.5}
$$
有限截断满足真实域等式；对 $f\in\operatorname{Dom}X^*$，
截断 $B_{2,n}f\to B_2f$，同时
$$
X^*B_{2,n}f=B_{2,n}X^*f+K_{2,n}f
$$
右侧强收敛。$X^*$ 的闭性因此给
$$
B_2\operatorname{Dom}X^*\subseteq\operatorname{Dom}X^*,\qquad
[X^*,B_2]=K_2.
\tag{C.6}
$$

取固定闭轮廓 $\Gamma$ 包围 $0$，位于 $\phi$ 的解析域内并避开 $\sigma(B_2)$。
每个 $(zI-B_2)^{-1}\in\mathcal A$ 保持完整域，且
$$
[X^*,(zI-B_2)^{-1}]
=(zI-B_2)^{-1}K_2(zI-B_2)^{-1}.
$$
故
$$
\boxed{
K_Y:=[X^*,Y]
=\frac1{2\pi i}\int_\Gamma
\phi(z)(zI-B_2)^{-1}K_2(zI-B_2)^{-1}\,dz
\in B(H).
}
\tag{C.7}
$$
例如其范数由
$$
\frac{\operatorname{length}\Gamma}{2\pi}
\sup_\Gamma|\phi|\,
\sup_\Gamma\|(zI-B_2)^{-1}\|^2\,\|K_2\|
\tag{C.8}
$$
控制。有限的固定轮廓常数可以很大；不把它当成统一小量。

还需保留通常伴随方向。对 $f,g\in\operatorname{Dom}X$，由 (C.7)
$$
\langle Y^*f,X^*g\rangle
=\langle f,YX^*g\rangle
=\langle Y^*Xf-K_Y^*f,g\rangle.
$$
伴随域判据给
$$
\boxed{
Y^*\operatorname{Dom}X\subseteq\operatorname{Dom}X,\qquad
[X,Y^*]=-K_Y^*.
}
\tag{C.9}
$$
这一步没有把有界交换子与 $X$ 的域交换误传给其通常伴随。

## D. 危险分支本身的完整二阶域

因 $Y$ 有界且 $C$ 对称，$T=X-Y$ 闭、$C$ 自伴，并且
$$
\operatorname{Dom}T=\operatorname{Dom}T^*
=\operatorname{Dom}X.
$$
由 (B.1)、(C.7)、(C.9) 极化或直接展开，完整域上有
$$
\langle Tf,Tg\rangle-\langle T^*f,T^*g\rangle
=\langle C_Tf,g\rangle,
\tag{D.1}
$$
其中
$$
\boxed{
C_T=C_a-K_Y-K_Y^*+Y^*Y-YY^*,\qquad C_T=C_T^*\in B(H).
}
\tag{D.2}
$$
特别
$$
\|C_T\|\le\|C_a\|+2\|K_Y\|+2\|Y\|^2.
$$

引理 A.1 给
$$
\boxed{
\operatorname{Dom}T^2=\operatorname{Dom}(T^*)^2
=\operatorname{Dom}(T^*T)=\operatorname{Dom}(TT^*),
\qquad T^*T-TT^*=C_T.
}
\tag{D.3}
$$
二阶自然算子均真实闭。此处允许任意常数项 $a_*$；若要把 $M=\ker T$ 识别为 R208 §7 的原危险点态平方核，仍须保留那里另加的 $a_*=0$ 假设。

## E. 三块中央耦合的定量图正则性

假设 R236 的实际情形
$$
0\ne M=\ker T,\qquad M\perp CM.
$$
令
$$
K=(M\oplus CM)^\perp.
$$
R212/R236 的真实三块分解为
$$
T=
\begin{pmatrix}
0&F&D_0\\
0&T_K&H_1\\
0&0&0
\end{pmatrix},
\qquad
\operatorname{Dom}T=M\oplus\operatorname{Dom}T_K\oplus CM.
\tag{E.1}
$$
外块均有界，$T_K$ 闭、$C_K$ 自伴，且
$\operatorname{Dom}T_K=\operatorname{Dom}T_K^*$。
这里没有假设 $T_K$ 单射。

置 $c=\|C_T\|$。因为 $\ker T^*=CM$，对 $m\in M$ 和 $z\in CM$，
$$
\|T^*m\|^2=-\langle C_Tm,m\rangle\le c\|m\|^2,
\qquad
\|Tz\|^2=\langle C_Tz,z\rangle\le c\|z\|^2.
\tag{E.2}
$$
因此
$$
\boxed{\|F\|,\ \|D_0\|,\ \|H_1\|\le\sqrt c.}
\tag{E.3}
$$

关键的新域信息是：
$$
M\subseteq\operatorname{Dom}T^2=\operatorname{Dom}(T^*)^2,
\qquad
CM\subseteq\operatorname{Dom}(T^*)^2=\operatorname{Dom}T^2.
\tag{E.4}
$$
例如 $CM$ 首先因 $T^*z=0$ 属于 $(T^*)^2$ 的自然域，然后才由 (D.3) 转到 $T^2$；没有先把外块的像当作中央域向量。

对 $z\in CM$，(D.3) 给 $T^*Tz=C_Tz$。把 (D.1) 用于 $Tz$，得到
$$
\|T^2z\|^2
=\|T^*Tz\|^2+\langle C_TTz,Tz\rangle
\le2c^2\|z\|^2.
\tag{E.5}
$$
对 $m\in M$ 交换 $T,T^*$ 得
$\|(T^*)^2m\|\le\sqrt2\,c\|m\|$。
按照 (E.1) 逐块读出
$$
\boxed{
H_1(CM)\subseteq\operatorname{Dom}T_K,\qquad
F^*(M)\subseteq\operatorname{Dom}T_K^*,
}
\tag{E.6}
$$
并有真正的全域有界乘积
$$
\boxed{
\|T_KH_1\|\le\sqrt2\,c,\qquad
\|T_K^*F^*\|\le\sqrt2\,c.
}
\tag{E.7}
$$
由于中央一阶通常伴随同域，(E.6) 中的两像实际上同时属于
$\operatorname{Dom}T_K=\operatorname{Dom}T_K^*$。

另从 $TT^*m=-C_Tm$ 与 $T^*Tz=C_Tz$ 的中央行得到
$$
T_KF^*=-P_KC_T|_M-H_1D_0^*,
$$
$$
T_K^*H_1=P_KC_T|_{CM}-F^*D_0.
\tag{E.8}
$$
所以
$$
\boxed{
\|T_KF^*\|\le2c,\qquad \|T_K^*H_1\|\le2c.
}
\tag{E.9}
$$

(E.7) 的伴随还给一个有用的反方向：在 $\operatorname{Dom}T_K$ 上的
$FT_K$ 有有界延拓
$$
\boxed{
\widehat{FT_K}=(T_K^*F^*)^*,\qquad
\|\widehat{FT_K}\|\le\sqrt2\,c.
}
\tag{E.10}
$$
本式没有断言 $F^*$ 是某个未知中央逆的有界正则器；它只涉及已经有定义的中央算子乘积。

## F. 自然平方的域现在可完全分离

对 $(m,k,z)\in\operatorname{Dom}T$，
$$
T(m,k,z)=(Fk+D_0z,\ T_Kk+H_1z,\ 0).
$$
因 $H_1z\in\operatorname{Dom}T_K$，再作用一次的域条件准确等价于
$k\in\operatorname{Dom}T_K^2$。因此
$$
\boxed{
\operatorname{Dom}T^2
=M\oplus\operatorname{Dom}T_K^2\oplus CM,
}
\tag{F.1}
$$
并且
$$
\boxed{
T^2=
\begin{pmatrix}
0&\widehat{FT_K}&FH_1\\
0&T_K^2&T_KH_1\\
0&0&0
\end{pmatrix}
}
\tag{F.2}
$$
在 (F.1) 的完整自然域上成立。

中央的自交换子形式也可直接压缩：
$$
C_K=P_KC_T|_K-F^*F+H_1H_1^*,
\qquad \|C_K\|\le3c.
\tag{F.3}
$$
于是引理 A.1 同样给
$$
\operatorname{Dom}T_K^2=\operatorname{Dom}(T_K^*)^2,\qquad
T_K^*T_K-T_KT_K^*=C_K
\tag{F.4}
$$
在该共同域上成立。对 R236 再次约化中以 $N\subseteq M$ 为外核的三块分解，同样的证明逐字适用；所需的同域和外块有界性已经由真实投影域分解支付。

这不是将全部原空间算子性质自动传给任意商。这里只对已经建立了完整正交三块域式的那些具体中央约化应用引理。

## G. 对尚未关闭的 $D_H$ 分支的准确作用

再假设旧 $T_K$ 单射。沿用 R236 的定义
$$
D_H=\{z\in CM:H_1z\in\operatorname{Ran}T_K\},
\qquad
J_Hz=T_K^{-1}H_1z.
$$
(E.6) 使每个 $z\in D_H$ 实际满足
$$
J_Hz\in\operatorname{Dom}T_K^2,\qquad
T_K^2J_Hz=T_KH_1z.
\tag{G.1}
$$
因而
$$
\boxed{\|T_K^2J_Hz\|\le\sqrt2\,c\|z\|\quad(z\in D_H).}
\tag{G.2}
$$
这比只知道 $J_Hz\in\operatorname{Dom}T_K$ 强，但没有给出 $\|J_Hz\|$ 的上界。

若 $M_0=M\ominus N$ 且
$Q=\overline{P_{M_0}FT_K^{-1}}$ 是前附录的正则图算子，则对
$x\in\operatorname{Dom}T_K^2$，
$$
T_K^2x\in\operatorname{Dom}Q,\qquad
QT_K^2x=P_{M_0}FT_Kx.
$$
故此乘积也有范数至多 $\sqrt2\,c$ 的有界延拓。这里的 $Q$ 是矩形闭算子，不是正交投影。

仍须明确保留：

1. $H_1(CM)\subseteq\operatorname{Dom}T_K$ 不蕴含
   $H_1(CM)\subseteq\operatorname{Ran}T_K$。
2. (G.2) 不给 $T_K^2$ 的下方界，也不使 $J_H$ 自动有界。
3. $D_H$ 是否等于其闭包 $CM_0$，以及新核的斜投影是否有界，仍未由本稿判定。
4. 不对 $J_H$ 套用 R161 的闭平方根引理：它是两个不同 Hilbert 空间之间的闭商，并未具有那个引理所需的同域自交换子结构。
5. 不由二阶同域宣称所有自然高阶域相同，亦不由新增图正则性把真实值域替换成值域闭包。

本补充给出的实际新增接口是 (D.3)、(E.6)–(E.10) 与 (F.1)–(F.4)。后续若能从这些真实耦合的更强结构推出 (G.2) 所缺的通常范数控制，才可能关闭 R236 的闭图分支。

## 引用接口

- R161，第一阶通常伴随同域与完整极化形式，尤其 §§4–5。
- R176，实际最高系数为单位的自然多项式及闭图；本稿二阶闭性另由 A.4 独立支付。
- R208，$Y=\phi(B_2)$ 分支；具体危险点态平方核的识别使用 §7 的 $a_*=0$ 设置。
- R212 中央域附录，实际三块域与通常伴随。
- R236 主稿及正则图附录，$D_H,J_H,Q$ 的精确定义和真像/闭像边界。
