# R236 附录：正常尾商的精确闭包、可见距离与有限放大实现

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的辅助结论。** 本稿把前稿的距离下界加强到 ultraweak 闭尾理想，并给出原有限秩正常见证直接产生的实际有限放大。没有免费把尾表示延伸到前一位，也未构造有界商代表。

## 1. 一次余式映射保 ultraweak 闭包

沿用[完整尾理想商费用](R236-appendix-full-tail-ideal-quotient-cost-and-normal-anchors.md)的真实一步模型
$$
\mathcal C_{\rm cur}=\mathcal C_{\rm next}\oplus N\mathcal C_{\rm next},
\qquad N^2=t=\eta N_{\rm next},
$$
$$
S=D(N+G),\quad D\in\mathcal B_{\rm next}^{\times},
\qquad Z=E+NF,
\qquad h=G^2-t,\quad k=E-GF.
$$
R236 已证的有界余式映射为
$$
\mathfrak r(a+Nb)=a-Gb.
\tag{1.1}
$$
$a,b$ 是实际物理块压缩，左乘固定 $G$ 在 $B(H)$ 上 ultraweak 连续，
故 $\mathfrak r$ 也是 ultraweak 连续的。
其在真实尾代数上为恒等，并且
$$
R-\mathfrak r(R)\in S\mathcal C_{\rm cur},
\qquad
S\mathcal C_{\rm cur}+Z\mathcal C_{\rm cur}
=\mathfrak r^{-1}(h\mathcal C_{\rm next}+k\mathcal C_{\rm next}).
$$

因此不仅范数闭包，而且准确有
$$
\boxed{
\overline{S\mathcal C_{\rm cur}+Z\mathcal C_{\rm cur}}^{\,uw}
=\mathfrak r^{-1}
\left(\overline{h\mathcal C_{\rm next}+k\mathcal C_{\rm next}}^{\,uw}\right).
}
\tag{1.2}
$$
一个包含由连续性给出。反向取任意 $R$，若
$\mathfrak r(R)$ 是右侧理想的 ultraweak 极限，将逼近网加上固定
$R-\mathfrak r(R)$ 即得当前理想中趋于 $R$ 的网。
此证明没有声称这些网存在统一范数或源费用。

对原固定理想 $\mathcal I=S_0\mathcal A'+Z_0\mathcal A'$，
逐次使用 (1.2) 得
$$
\widehat{\mathcal J}_j
:=\{b\in\mathcal C_j:I_{K_j}\otimes b\in\overline{\mathcal I}^{\,uw}\}
=\overline{\mathcal J_j'}^{\,uw},
\tag{1.3}
$$
其中 $\mathcal J_j'$ 是此前范数闭的完整尾交。
特别，
$$
\widehat{\mathcal J}_{j+1}
=\overline{h_j\mathcal C_{j+1}+k_j\mathcal C_{j+1}}^{\,uw}.
$$
所以这里没有任意交换“交”与“闭包”，而是由同一个连续余式映射证明了它们的准确关系。

## 2. 正交叉块给出一个小范数的实际迹类分离者

设原正常正密度 $\rho_0$ 湮灭 $\mathcal I$。
在第 $j$ 位取同一正部分迹 $\rho_j$，记
$$
\rho_j=\begin{pmatrix}\rho_{00}&B\\B^*&\rho_{11}\end{pmatrix},
\quad \sigma=\rho_{j+1}=\rho_{00}+\rho_{11},
\quad \tau=\operatorname{Tr}\rho_0,
$$
$$
r_j=\operatorname{Tr}(\rho_0P_{\chi_j})\longrightarrow0,
\qquad L_j=(I+t_j)/2.
$$
前稿的完整交叉块恒等式为
$$
\operatorname{Tr}(\sigma(G_j+L_j)R)
=-\operatorname{Tr}(A_jR),
$$
$$
A_j=B-\frac\sigma2+\left(B^*-\frac\sigma2\right)t_j,
\qquad
\|A_j\|_1\le(1+\eta_j)\sqrt{\tau r_j}.
\tag{2.1}
$$
定义实际迹类算子
$$
T_j=-A_j(I-t_j)^{-2}.
\tag{2.2}
$$
由 $\|t_j\|\le\eta_j<1$，
$$
\boxed{\|T_j\|_1\le
\frac{1+\eta_j}{(1-\eta_j)^2}\sqrt{\tau r_j}.}
\tag{2.3}
$$
对尾右因子 $R\in\mathcal C_{j+1}$，有
$$
\operatorname{Tr}(T_jR)
=\operatorname{Tr}\bigl(\sigma(G_j+L_j)(I-t_j)^{-2}R\bigr).
$$
同一 $\sigma$ 湮灭完整下一尾理想，故 $T_j$ 的正常泛函湮灭
$\widehat{\mathcal J}_{j+1}$。
并由 $G_j^2-t_j\in\mathcal J_{j+1}'$，
$$
\boxed{\operatorname{Tr}\bigl(T_j(G_j-L_j)\bigr)=-\tau/4.}
\tag{2.4}
$$
这里的迹类代表来自真正的交叉块，不能改用可能很大的
$\sigma(G_j+L_j)(I-t_j)^{-2}$ 的迹范数去冒充 (2.3)。

## 3. 距 ultraweak 完整尾理想也必须发散

对任意 $H\in\widehat{\mathcal J}_{j+1}$，(2.4) 不变。
由迹范数对偶，
$$
\boxed{
\operatorname{dist}(G_j-L_j,\widehat{\mathcal J}_{j+1})
\ge\frac{\tau}{4\|T_j\|_1}
\ge
\frac{(1-\eta_j)^2}{4(1+\eta_j)}
\sqrt{\frac\tau{r_j}}.
}
\tag{3.1}
$$
因此
$$
\operatorname{dist}(G_j,\widehat{\mathcal J}_{j+1})\longrightarrow\infty.
\tag{3.2}
$$
这不是只能由奇异泛函看见的范数商缺口；一个原正态产生的正常迹类泛函已经看见它。

相反，若
$\operatorname{dist}(G_j,\widehat{\mathcal J}_{j+1})$
沿无穷子列有界，则前稿的条件锚
$$
\Theta_{j,H}=2(N_j+G_j-H)(I+N_j)^{-2}
$$
可在 $\overline{\mathcal I}^{\,uw}$ 中选成统一有界、期望一、越来越远的尾算子。
它们 WOT 趋 $I$，不允许任何非零正常正湮灭者。
这比要求模范数闭尾理想的有界代表更弱。
本稿不从 ultraweak 归属自动提取统一有界的原代数理想源或逼近网。

## 4. 若原见证有限秩，距离在一个明确有限放大上实现

假设 $\operatorname{rank}\rho_0=R_0<\infty$。
则 $\operatorname{rank}\rho_j\le R_0 2^j$，
$\operatorname{rank}\sigma\le R_0 2^{j+1}$。
式 (2.1) 中 $A_j$ 的像包含在
$\operatorname{Ran}\rho_{00}+\operatorname{Ran}\rho_{11}
=\operatorname{Ran}\sigma$ 中，
右乘 $(I-t_j)^{-2}$ 不增加秩，故
$$
\boxed{d_j:=\operatorname{rank}T_j\le R_0 2^{j+1}.}
\tag{4.1}
$$
一般无限秩正常态只需可数放大，下面的有限秩情形不作这种扩大。

对 $T_j$ 作奇异值分解，并形成
$\xi,\upsilon\in\mathscr H_{j+1}^{\oplus d_j}$，使
$$
\operatorname{Tr}(T_jR)
=\langle R^{(d_j)}\xi,\upsilon\rangle,
\qquad
\|\xi\|^2=\|\upsilon\|^2=\|T_j\|_1.
\tag{4.2}
$$
在**原实际尾的这个有限放大**中定义
$$
M_j=\overline{\mathcal C_{j+1}^{(d_j)}\xi},
\qquad
N_j^{\rm sub}=
\overline{\widehat{\mathcal J}_{j+1}^{(d_j)}\xi},
\qquad
Q_j=M_j\ominus N_j^{\rm sub}.
\tag{4.3}
$$
$M_j,N_j^{\rm sub}$ 都对 $\mathcal C_{j+1}^{(d_j)}$ 不变，
而 (2.4) 确保 $Q_j\ne0$。
$\upsilon\perp N_j^{\rm sub}$ 来自 $T_j$ 湮灭该理想。
压缩
$$
\pi_j(R)=P_{Q_j}R^{(d_j)}|_{Q_j}
$$
是一个正常、含单位、完全契约的代数表示，且
$$
\pi_j(\widehat{\mathcal J}_{j+1})=0.
\tag{4.4}
$$
乘法性来自 $M_j,N_j^{\rm sub}$ 的不变性；对理想的零式来自
$\widehat{\mathcal J}_{j+1}M_j\subset N_j^{\rm sub}$。

将 (4.2) 的两向量投影到 $Q_j$ 后，配对不变、范数不增加。
所以
$$
\boxed{
\|\pi_j(G_j-L_j)\|
\ge\frac\tau{4\|T_j\|_1}
\ge
\frac{(1-\eta_j)^2}{4(1+\eta_j)}
\sqrt{\frac\tau{r_j}}.
}
\tag{4.5}
$$
同时精确保有
$$
\pi_j(G_j)^2=\pi_j(t_j),\qquad
\|\pi_j(t_j)\|\le\eta_j.
\tag{4.6}
$$
因此原有限秩正常见证会产生一个真正可见的大范数、平方很小的尾算子，
其放大次数至多 $R_0 2^{j+1}$；没有声称可任意降为一。

## 5. 这个尾表示为何还不能免费用于前一位

若一个表示已来自当前全理想的 Hilbert 不变子商，则
$S_j=D_j(N_j+G_j)$ 被杀掉时，有
$\pi(G_j)=-\pi(N_j)$，于是 $\|\pi(G_j)\|\le1$。
第 4 节的表示却只从下一尾理想构造，(4.5) 允许其 $G_j$ 范数很大。
因此它不可能总以原度量延伸成前一位的完全契约表示并同时杀掉 $S_j$。

可以在 $\mathbb C^2\otimes Q_j$ 上写出块算子
$\left(\begin{smallmatrix}0&\pi_j(t_j)\\I&0\end{smallmatrix}\right)$，
并取其加 $\pi_j(G_j)$ 的核图 $\{(-\pi_j(G_j)f,f)\}$。
但这会准确引入图度量
$I+\pi_j(G_j)^*\pi_j(G_j)$。
[具体 Volterra 模型](R236-appendix-square-root-tail-quotient-and-closed-graph-metric-model.md)已展示这种忠实正常图表示可以缩范数任意倍。
所以该操作不是所需的等距商实现，也不取消 (4.5) 的实际成本。

原问题仍须利用全部真实 dyadic 结构，证明一个可支付的有界代表，
或排除这组来源受控而条件数增长的尾半不变空间；平方关系与一般表示定理本身不够。
