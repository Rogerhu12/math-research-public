# R236 附录：固定正常尾表示的全部未来界与尾保持单位提升费用

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的实际归约与费用恒等式。** 本稿固定同一个原有限放大中的正常半不变表示，准确说明全部未来商变量虽在该表示中有界，仍不能把正交叉块估计的原范数换成表示范数。没有使用一般 Volterra 模型代替原 dyadic 结构。

## 1. 固定一个实际表示，不逐层换空间

固定由[正常尾商的有限放大](R236-appendix-normal-tail-ideal-closure-and-finite-amplification.md)实际构造得到的
$$
\pi=\pi_j:\mathcal C_{j+1}\longrightarrow B(Q),
\qquad
\pi(\widehat{\mathcal J}_{j+1})=0,
$$
其中 $Q$ 是原尾 $\mathscr H_{j+1}^{\oplus d}$ 中的半不变空间，
$\pi$ 正常、含单位、完全契约，$d$ 有前稿的明确有限上界。

对每个 $l\ge j+1$，原完整尾交嵌套给
$S_l\in\widehat{\mathcal J}_{j+1}$。
真实因式为
$$
S_l=D_l(N_l+G_l),\qquad D_l^{-1}\in\mathcal B_{l+1}.
$$
表示保持这个实际双侧逆，故
$$
\boxed{\pi(G_l)=-\pi(N_l),\qquad \|\pi(G_l)\|\le1.}
\tag{1.1}
$$
全都在同一个 $Q$、同一个原 Hilbert 度量中成立。
令 $T_l=\pi(N_l)$，则
$$
T_l^2=\eta_lT_{l+1},\quad \|T_l\|\le1,
\qquad T_l\longrightarrow I_Q/2\quad\text{WOT}.
\tag{1.2}
$$
最后的弱极限来自实际远尾弱单位以及正常的有限放大压缩。

这并不包含前一步 $G_j$ 的界，因为 $S_j$ 尚未被这个尾表示的定义域包括。

## 2. 在同一物理表示中选择一个固定正常状态

固定任意单位向量 $v\in Q$，仍把它看作
$\mathscr H_{j+1}^{\oplus d}$ 的实际向量。
每个 $l$ 都由同一个 $|v\rangle\langle v|$ 取物理正部分迹，
并记
$$
r_l(v)=\langle P_{\chi_l}^{(d)}v,v\rangle\longrightarrow0,
\qquad L_l=(I+t_l)/2,\quad t_l=\eta_lN_{l+1}.
$$
$v$ 的正泛函湮灭全部 $S_l\mathcal C_l$：压缩乘法性和 $\pi(S_l)=0$ 保证这一点。
因此原实际交叉块证明给尾泛函
$$
\psi_l(R)
=\langle\pi((G_l+L_l)R)v,v\rangle,
\qquad R\in\mathcal C_{l+1},
$$
以及
$$
\boxed{
\sup_{\substack{R\in\mathcal C_{l+1}\\\|R\|\le1}}
|\psi_l(R)|
\le e_l:=(1+\eta_l)\sqrt{r_l(v)}\longrightarrow0.
}
\tag{2.1}
$$
该估计的归一化是原实际尾算子范数 $\|R\|$。
下面用同一表示中的明确单位说明，不能将它改为 $\|\pi(R)\|$。

## 3. 未来界给出一个表示内便宜、原尾却昂贵的单位

真实 $G_l$ 的常数字符零，$L_l$ 的字符为 $1/2$，所以
$$
U_l=(G_l+L_l)^{-1}\in\mathcal B_{l+1}
\tag{3.1}
$$
是实际有界尾单位。
由 (1.1)–(1.2)，
$$
\pi(G_l+L_l)
=-T_l+\frac{I+T_l^2}{2}
=\frac{(I-T_l)^2}{2}.
$$
因此
$$
\boxed{
\pi(U_l)=2(I-T_l)^{-2},\qquad
\|\pi(U_l)\|\le\frac8{(1-\eta_l)^2}.
}
\tag{3.2}
$$
逆的范数用
$(I-T_l)^{-1}=(I+T_l)(I-T_l^2)^{-1}$，没有假设 $\|T_l\|<1$。
但同时
$$
\boxed{\psi_l(U_l)=1.}
\tag{3.3}
$$

由 $\psi_l(U_l)=1$ 和 (2.1) 知 $e_l>0$；否则真正常见证的假设已经矛盾。令 $K_{l+1}=\ker(\pi|_{\mathcal C_{l+1}})$。
$\psi_l$ 湮灭这个完整核，所以对任意 $H\in K_{l+1}$，(3.3) 保持不变。
由 (2.1)，
$$
\boxed{
\operatorname{dist}(U_l,K_{l+1})\ge e_l^{-1}.
}
\tag{3.4}
$$
于是自然的忠实尾商映射
$$
\mathcal C_{l+1}/K_{l+1}\longrightarrow\pi(\mathcal C_{l+1})
$$
若在其像上取逆，该逆在这个明确元素上的范数比至少为
$$
\boxed{\frac{(1-\eta_l)^2}{8e_l}\longrightarrow\infty.}
\tag{3.5}
$$
这已经发生在同一个固定正常表示 $\pi$ 中，不是换成一般反例。
由于 $\widehat{\mathcal J}_{l+1}\subset K_{l+1}$，
模原完整尾理想的提升也至少支付同样的下界。

等价地，$\psi_l$ 在表示像上的对应泛函范数至少
$(1-\eta_l)^2/8$，而其拉回到原尾单位球的范数至多 $e_l\to0$。
正部分迹小误差没有变成表示像单位球上的小误差。

## 4. 去掉尾位置限制确实有便宜提升，但它不能代替下一尾提升

在当前第 $l$ 位的原实际代数中，令
$$
W_l=2(I-N_l)^{-2}.
$$
它有统一的原范数上界
$$
\|W_l\|\le\frac8{(1-\eta_l)^2},\qquad
\pi(W_l)=\pi(U_l).
\tag{4.1}
$$
这里 $W_l\in\mathcal C_l$，通常不属于下一尾 $\mathcal C_{l+1}$。
两者的差实际上属于当前完整原理想：
令
$Y_l=(I-N_l)^2/2$，则
$$
(G_l+L_l)-Y_l=G_l+N_l=D_l^{-1}S_l.
$$
两者都是实际单位，使用准确逆差恒等式得
$$
U_l-W_l
=-(G_l+L_l)^{-1}D_l^{-1}S_lY_l^{-1}
\in S_l\mathcal C_l.
\tag{4.2}
$$
所以前一位的便宜代表已存在；缺的是把它放回**下一真实尾**并保费用。
对 $W_l$ 直接套 (2.1) 不合法，因为它仍作用于被取正部分迹的第 $l$ 位。
对应物理条件压缩也不保持当前理想，不能借此删除该位。

## 5. 全部未来恒等式为何还没反向控制 $G_j$

未来 $G_l$ 的表示范数有界，而其实际偶、奇块 $C_l,D_l$ 的表示范数未因此得到界。
原偶、奇块提取是具体物理头的块压缩；它们未被证明能在这个半不变表示上按相同范数下降。
特别，$\pi(G_l)=-T_l$ 不能先代进一个物理块提取公式，再把提取结果认作
$\pi(C_{l+1}),\pi(D_{l+1})$。

精确缺失的是一个**保持下一尾位置**的提升或归一化：
把表示中范数有界的所需右因子，提升为原 $\mathcal C_{l+1}$ 中同样有界的代表，
或者直接构造 $G_j-H_j$ 的有界代表。
(3.4)–(3.5) 说明在真正常见证存在的假设下，对任意未来单位 $U_l$ 的统一尾提升绝不成立。
若能用原 dyadic 结构证明某个足够的尾提升必然成立，才会产生所需矛盾。

这份归约保留同一个 $Q$、同一个正常物理状态和全部实际逆。
当前没有得到前一步 $G_j$ 的商上界，也没有把 (1.1) 中的表示范数当作原完整尾商范数。
