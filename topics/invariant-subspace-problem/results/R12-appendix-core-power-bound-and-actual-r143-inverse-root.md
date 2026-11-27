# 有界幂只需给在原图核心：R143 真实反根与分母平方核心

日期：2026-11-27（台北时间，UTC+8）。作者：literature_deddens / Astra-ISP-8542378f-20261127。

状态：以下图核心加强、原头像反根的闭实现及 R143 分母平方核心均完整。
原尾移位始终记为 $B_m$；R143 有界二阶头行列式稿中的另一个分母改记为 $D$。
二者不能混用。

## 1. 图核心上的自然幂界已足够

**定理 1.1。** 设 $T$ 在 Hilbert 空间 $H$ 上闭、稠密定义，满足
$$
\operatorname{Dom}T\subseteq\operatorname{Dom}T^*.
\tag{1.1}
$$
设 $\mathcal E$ 是 $T$ 的一个线性图核心，对某个整数 $q\ge2$ 有
$$
\mathcal E\subseteq\operatorname{Dom}T^q,
\qquad
\|T^q x\|\le K\|x\|\quad(x\in\mathcal E),
\qquad K<\infty.
\tag{1.2}
$$
则 $T$ 全域有界。不要求 $T\operatorname{Dom}T\subseteq\operatorname{Dom}T$。

**证明。** 已发布的伴随域引理给完整域上的实际图界
$$
\|T^*y\|\le a\|Ty\|+b\|y\|
\qquad(y\in\operatorname{Dom}T).
\tag{1.3}
$$
对固定 $x\in\mathcal E\subseteq\operatorname{Dom}T^q$，
每个 $T^jx$（$0\le j\le q-1$）都在 $\operatorname{Dom}T$ 内。
因此旧证明的逐步伴随计算仍有全部真实域，得到
$$
s_{j+1}^2\le a s_js_{j+2}+b s_js_{j+1},
\qquad s_j=\|T^jx\|,\quad 0\le j\le q-2.
\tag{1.4}
$$
相同比值归纳给 $\|Tx\|\le C\|x\|$ 于 $\mathcal E$，其中可取
$$
C=\max\left\{
2b\sum_{j=0}^{q-2}a^j,
2^{1-1/q}a^{(q-1)/2}K^{1/q}
\right\}\quad(a\ge1),
\tag{1.5}
$$
若 $a=0$ 则取 $C=b$；$q=2$ 时也可取
$$
C=\frac{b+\sqrt{b^2+4aK}}2.
\tag{1.6}
$$
旧证明中零 $s_j$ 的分支完全相同。

现在使用的是真正图核心：对任意 $y\in\operatorname{Dom}T$，
取 $x_n\in\mathcal E$ 使 $x_n\to y$、$Tx_n\to Ty$。
将上述通常范数界取极限，得 $\|Ty\|\le C\|y\|$。
稠密域加闭性再给 $\operatorname{Dom}T=H$。证毕。

特别，对非整除原全尾根，即使只在同一个真实图核心上满足
$T^q=\lambda(I_k\otimes B_m^p)$，伴随域包含仍会迫全域有界根，
与 $q\nmid pk$ 矛盾。核心身份因 $T$ 有界而扩展到全空间。

## 2. 原尾整幂在已存闭图上的图核心：准确像方向

令 $R$ 是有限放大原尾空间上的闭算子，其真实图被
$(I_k\otimes B_m)^{(2)}$ 保持，即原尾保持域并与 $R$ 域交换。
记 $\mathcal B=I_k\otimes B_m$。对每个整数 $r\ge1$，
$$
\boxed{\mathcal B^r\operatorname{Dom}R
\text{ 是 }R\text{ 的图核心}.}
\tag{2.1}
$$

确实，已证原尾强*单位可取为 $e_n(B_m)$，
其最低次数趋无穷，$\|e_n(B_m)\|\le1$，且 $e_n(B_m)\to I$ 强*。
对充分大 $n$，$e_n(z)=z^r q_n(z)$。
每个多项式 $q_n(\mathcal B)$ 保持原域；对 $x\in\operatorname{Dom}R$，
$$
x_n=e_n(\mathcal B)x
\in\mathcal B^r\operatorname{Dom}R,
\qquad
Rx_n=e_n(\mathcal B)Rx.
$$
所以 $x_n\to x$、$Rx_n\to Rx$，并且
$\|x_n\|_R\le\|x\|_R$。
这给同一实际图范数中的收缩逼近；不需要除法多项式 $q_n$ 的统一范数界。

同一证明适用于闭原尾不变空间 $K$ 上的闭图，只要该图确由
$B_m^{(2)}$ 保持。原多项式限制到 $K$，不另造一个模型。

(2.1) 的输入是 $\operatorname{Dom}R$ 内已有向量。
它不声称 $\operatorname{Ran}\mathcal B^r\subseteq\operatorname{Dom}R$。
对另一个慢行分母 $D$，本节的原尾整幂结论不能直接替换成 $D^r$。

## 3. R143 原头像方程确实产生一个闭稳定反根

这里先用 R143 主稿 §7 的实际头像，不引入任何分母假设。
设 R143 §7 的特殊跨核 $M$ 非零，并满足该处已证的两个坐标投影单射条件；此处不将任意普通不变空间直接识别为这种核。
该稿已经构造了同一个闭尾不变空间 $K$ 及闭、单射、稠密定义、稠密值域的
$$
T:\mathcal D\subseteq K\longrightarrow K,
\qquad
M=\{(x,Tx):x\in\mathcal D\}.
\tag{3.1}
$$
此处真实第一尾移位是
$$
(B_1h)(z)=\alpha_{1+v_2(z)}h(z-1),\qquad
A=\begin{pmatrix}0&B_1\\\alpha_0I&0\end{pmatrix}.
$$
原闭图方程是
$$
B_1\mathcal D\subseteq\mathcal D,
\quad TB_1x=B_1Tx,
\quad B_1Tx\in\mathcal D,
\quad TB_1Tx=\alpha_0x
\qquad(x\in\mathcal D).
\tag{3.2}
$$

定义真实逆算子
$$
S=T^{-1},\qquad
\operatorname{Dom}S=\operatorname{Ran}T\subseteq K.
\tag{3.3}
$$
交换闭图的两个坐标说明 $S$ 闭；$T$ 的单射和稠密像使 $S$ 单值、稠密定义。
对 $x\in\mathcal D$，(3.2) 给
$$
x=T(\alpha_0^{-1}B_1Tx)\in\operatorname{Ran}T,
\qquad
Sx=\alpha_0^{-1}B_1Tx.
\tag{3.4}
$$
所以 $\mathcal D\subseteq\operatorname{Dom}S$。

若 $y=Tx\in\operatorname{Dom}S$，则 $Sy=x\in\mathcal D\subseteq\operatorname{Dom}S$，
并由 (3.4) 得
$$
S^2y=Sx=\alpha_0^{-1}B_1Tx=\alpha_0^{-1}B_1y.
$$
因此这里没有自然平方域缺口：
$$
\boxed{
S\operatorname{Dom}S\subseteq\operatorname{Dom}S,
\qquad S^2=\alpha_0^{-1}B_1|_K
\text{ 于 }\operatorname{Dom}S.
}
\tag{3.5}
$$
同理，$B_1$ 保持 $\operatorname{Dom}S$，且 $SB_1=B_1S$ 于该域。

此外 (3.2) 对 $y=Tx$ 给
$B_1y\in\mathcal D$，故
$$
B_1\operatorname{Dom}S\subseteq\mathcal D
\subseteq\operatorname{Dom}S.
$$
应用 §2 的原尾整幂图核心，得到准确闭包
$$
\boxed{
\mathcal D\text{ 是 }S\text{ 的图核心},\qquad
S=\overline{\alpha_0^{-1}B_1T|_{\mathcal D}}.
}
\tag{3.6}
$$
这是从原未知核本身获得的闭根和同源图核心，不是由一般平坦理想猜测全域分母。

若以后实际证明
$$
\operatorname{Dom}S\subseteq\operatorname{Dom}S^*,
\tag{3.7}
$$
则已证伴随域引理给 $S\in B(K)$、$\operatorname{Dom}S=K$。
相应原第二头像已经闭且满整个底空间：
$$
P_1M=\operatorname{Ran}T=K,
\qquad
M=\{(Sy,y):y\in K\}.
\tag{3.8}
$$
这里的根是未知限制 $B_1|_K$ 的根。没有把 $K$ 认作全尾，也没有对它自动使用全尾根整除定理。

还可把 (3.7) 保持为原头像的准确范围条件。
对任何闭、单射、稠密定义且稠密值域的 $T$，
$$
(T^{-1})^*=(T^*)^{-1},
\qquad
\operatorname{Dom}(T^{-1})^*=\operatorname{Ran}T^*.
\tag{3.9}
$$
例如 $u=T^*v$ 时，对 $y=Tx$ 有
$\langle Sy,u\rangle=\langle x,T^*v\rangle=\langle y,v\rangle$；
反向的伴随域判据给 $u=T^*v$，且稠密值域使值唯一。
所以 (3.7) 等价于
$$
\operatorname{Ran}T\subseteq\operatorname{Ran}T^*.
\tag{3.10}
$$
此包含仍是必须额外验证的实际范围输入，不由 (3.2) 自动推出。

## 4. R143 行列式分母的 $D^2L$ 确是图核心，条件准确保留

现在转到 R143 的有界二阶头行列式附录。
为了与 $B_1$ 区别，将该稿的 $B$ 改记为 $D$：
$$
D=-2Z,
$$
其中 $Z$ 是由原最低头的第一阶尾行构成的有界乘子。
$D$ 属于尾范数代数、单射且全尾稠密像；它一般不是 $B_1$ 的一个整幂。
保留该稿的其他记号
$$
t=\eta_0\widehat N_1,\quad
\Delta=P^2-tD^2,\quad L=\ker\Delta,
\quad J=D^{-1}P,
\quad J_L=J|_{L\cap\operatorname{Dom}J}.
\tag{4.1}
$$
R143 附录 §3 的额外假设是：对每个有限 $d$ 和每个闭尾移位放大不变空间
$\mathcal M$，
$$
\overline{D^{(d)}\mathcal M}=\mathcal M.
\tag{4.2}
$$
它对该稿明确援引的 R140 快尾分母类已付；一般慢行分母没有这项结论。

在 (4.2) 下，该稿已给 $J_L$ 闭、稠密定义于 $L$、像仍在 $L$，
且其图 $\mathcal G(J_L)\subseteq\widehat H^2$ 是原尾二次放大不变空间。
这里不变算子是 $B_1^{(2)}$，不是把 $D$ 当成尾移位。
因此 (4.2) 适用于同一个图。

有界 $D^{(2)}$ 的像在该图稠密，平方像也稠密：
由 $\overline{D^{(2)}\mathcal G}=\mathcal G$ 和连续性，
$D^{(2)}\mathcal G\subseteq\overline{(D^{(2)})^2\mathcal G}$，再取闭包即可。
而域交换给
$$
(D^{(2)})^2(y,J_Ly)
=(D^2y,J_LD^2y).
$$
R143 附录 (4.1) 已逐域支付，对每个 $u\in L$，
$$
D^2u\in\operatorname{Dom}J_L^2,
\quad J_LD^2u=DPu,
\quad J_L^2D^2u=P^2u=tD^2u.
\tag{4.3}
$$
因此
$$
\boxed{D^2L\text{ 是 }J_L\text{ 的图核心},\qquad
D^2L\subseteq\operatorname{Dom}J_L^2,\qquad
J_L^2x=tx\quad(x\in D^2L).}
\tag{4.4}
$$
这是实际图核心，不只是 $D^2L$ 在 $L$ 的通常范数中稠密。

所以若另付
$$
\operatorname{Dom}J_L\subseteq\operatorname{Dom}J_L^*,
\tag{4.5}
$$
定理1.1直接给
$$
\boxed{J_L\in B(L),\quad\operatorname{Dom}J_L=L,
\quad J_L^2=t|_L.}
\tag{4.6}
$$
不需先证明 $J_L$ 的完整域稳定，也不需先将 $J_L^2$ 称为闭算子。
原核于是有真正有界图参数化
$M=\{(-J_Ly,y):y\in L\}$。

若特别知道 $D=B_1^rV$，其中 $V$ 为原尾范数代数中的可逆元素，
则 §2 的原强单位与 $V^{\pm1}$ 对每个原有限放大不变空间的保持性直接支付 (4.2)。
该结论包括纯原尾整幂；对任意慢行 $D$ 则不作此替换。

## 5. 已付和仍未付的实际边界

原 R143 头像已经无额外假设地支付 §3 的闭稳定根 $S$ 及其原域图核心。
行列式分母的 §4 则准确使用旧稿已明列的有限放大稠密性质；
满足该性质的分母，其 $D^2L$ 核心现已给出完整证明。

尚未自动获得的是各未知底空间上的通常伴随域包含 (3.7) 或 (4.5)。
全尾商的 $\widehat C$ 自伴性不能给出未知 $L$ 上的通常伴随同域，
尤其 $\widehat C L=L$ 没有得到证明。
一般慢第一行也不能借原尾 $B_1$ 的高次强单位取得 (4.2)。

本稿不把有界根在未知限制上的存在与全尾根的整除分类混为一谈，
也不把已经得到的图核心改写成全空间像包含。

## 已证来源

- [闭稳定根的伴随域包含与真实闭部分](../results/R12-appendix-stable-root-adjoint-domain-inclusion-and-actual-parts.md)；
- [原尾高最低次数的收缩强*单位](../results/R12-appendix-contractive-strong-star-density-in-every-odd-residue-class.md)；
- [R143 原跨核及头像方程，§7](../results/R143-quadratic-gauge-common-regularizers-and-kernel-graphs.md)；
- [R143 有界二阶头行列式、最大商与自然平方](../results/R143-appendix-bounded-quadratic-head-determinant.md)；
- [R140 快尾分母与全有限放大稠密性](../results/R140-invariant-subquotient-type-and-fixed-first-regularization.md)。
