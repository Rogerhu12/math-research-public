# R12 后续：原 Haar 二进幂的精确平方整除与一个新的闭稳定交换域

日期：2026-11-28（台北）。作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。

状态：以下二次来源、完整交换子中的非整除及最大自然闭域均已证明。构造所得闭算子的平方是同源有界算子 $Z$，不是原尾 $C$。本稿不把主理想的非半素性或新的闭域写成原平方根存在。

## 1. 固定原尾及实际幂费用

固定原 Haar 尾 $C=A^{(m)}$，置
$$
a_j=\alpha_{m+j},\qquad
\beta_n=\|C^n\|=\prod_{s=1}^n a_{v_2(s)},\qquad \beta_0=1.
\tag{1}
$$
$C$ 单射、稠密值域、拟幂零，$a_j$ 严格下降到零。这里始终是原 Haar 尾，非负整数边界移位。

所用原式及完整交换子 $\mathscr C=\{C\}'$ 的交换性见
[原尾重数与完整交换子](R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)。
[完整兼容喷射](R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md) 给每个兼容字符 $\chi$ 的代数同态
$$
j_\chi:\mathscr C\longrightarrow\mathbb C[[z]],\quad j_\chi(C)=z,
\qquad
|[z^r]j_\chi(A)|\,\beta_r\le\|A\|.
\tag{2}
$$
每个固定系数范数连续；在 $\mathcal A=\overline{\mathbb C[C]}^{\|\cdot\|}$ 上它正是原幂系数。

令 $N_j=2^j$。原二进计数直接给
$$
\beta_{N_j}=a_j\beta_{N_j-1},\qquad
\beta_{2N_j-1}=a_j\beta_{N_j-1}^{\,2},
\tag{3}
$$
以及对 $1\le i<j$，
$$
\beta_{N_i+N_j-1}=\beta_{N_j}\beta_{N_i-1}.
\tag{4}
$$
(3) 的第二式将 $1,\ldots,2N_j-1$ 分成两个长度 $N_j-1$ 的相同 ruler 段和中间因子 $a_j$；(4) 使用 $v_2(N_j+s)=v_2(s)$，$1\le s<N_i$。

全部 $N_i+N_j-1$ 为奇数，包括 $i=j$。故
$$
\beta_{N_i+N_j-2}=\beta_{N_i+N_j-1}/a_0.
\tag{5}
$$

## 2. 同一原来源的全部平方项

取
$$
t_j=2^{-j},\qquad
b_j=\frac{t_j}{\beta_{N_j-1}\sqrt{a_j}}\quad(j\ge1),
\qquad
W=\sum_{j\ge1}b_jC^{N_j}.
\tag{6}
$$
因为 $\|b_jC^{N_j}\|=t_j\sqrt{a_j}$ 且 $\sum t_j=1$，该级数在原算子范数绝对收敛，并有
$$
W\in\mathcal A,\qquad \|W\|\le\sqrt{a_1}.
\tag{7}
$$

定义完整的同源双和
$$
Z=\sum_{j\ge1}b_j^2C^{2N_j-2}
  +2\sum_{1\le i<j}b_ib_jC^{N_i+N_j-2}.
\tag{8}
$$
由 (3)--(5)，真实对角费用与全部交叉费用准确为
$$
b_j^2\beta_{2N_j-2}=\frac{t_j^2}{a_0},
\qquad
b_ib_j\beta_{N_i+N_j-2}
 =\frac{t_it_j}{a_0}\sqrt{\frac{a_j}{a_i}}\quad(i<j).
\tag{9}
$$
所以 (8) 绝对范数收敛，且
$$
Z\in\mathcal A,\quad \|Z\|\le a_0^{-1},\qquad
\boxed{W^2=C^2Z}.
\tag{10}
$$
等式先对有限和成立，再由上述同一双和的绝对收敛取极限，没有删掉交叉项或改用形式乘法。

再置 $Y=CZ$，同样由 (3)--(4) 直接得到
$$
Y\in\mathcal A,\quad \|Y\|\le1,\qquad W^2=CY.
\tag{11}
$$
$W,Y,Z$ 均非零，且保持函数正锥。后一句是实际正系数幂和的性质，不称它们为 Hilbert 空间中的正自伴算子。

## 3. 平方可除不付一次实际有界除法

若 $W=CA$ 对某个 $A\in\mathscr C$ 成立，则 (2) 强迫
$$
[z^{N_j-1}]j_\chi(A)=b_j,\qquad
\|A\|\ge b_j\beta_{N_j-1}
 =\frac{2^{-j}}{\sqrt{a_j}}\longrightarrow\infty.
\tag{12}
$$
原显式 $\alpha_{m+j}$ 比 $4^{-j}$ 衰减更快，所以矛盾。因此
$$
\boxed{W\notin C\mathscr C,\qquad W^2\in C^2\mathcal A\subset C\mathscr C.}
\tag{13}
$$
这尤其是原主理想 $C\mathscr C$ 非半素的显式见证；只用原权和已经付清的完整喷射，不调用外部抽象半素定理。

相同来源还给 $Z\notin C\mathscr C$。当 $j\ge2$，(8) 的 $C^{N_j}$ 系数恰为 $2b_1b_j$：两个二进幂的和等于 $N_j+2$ 只能是 $2+N_j$。若 $Z=CA$，则
$$
\|A\|\ge2b_1b_j\beta_{N_j-1}
 =2b_1\,2^{-j}a_j^{-1/2}\longrightarrow\infty.
\tag{14}
$$

## 4. 最大自然闭算子与稳定平方

使用实际值域定义
$$
\mathcal D=\{x\in H:Wx\in\operatorname{Ran}C\},\qquad
Lx=C^{-1}Wx\quad(x\in\mathcal D).
\tag{15}
$$
$C$ 单射使定义唯一。$\operatorname{Ran}C\subset\mathcal D$，并有
$$
LC=W.
\tag{16}
$$
故 $\mathcal D$ 稠密。若 $x_n\to x$、$Lx_n\to y$，则
$Wx_n=CLx_n$ 取极限得 $Wx=Cy$，所以 $x\in\mathcal D$、$Lx=y$；$L$ 闭。

每个 $A\in\mathscr C$ 都保持 $\mathcal D$，且
$$
LAx=ALx\quad(x\in\mathcal D).
\tag{17}
$$
证明只需 $WAx=AWx=CALx$，使用完整交换子的真实交换性。

给定 $x\in\mathcal D$、$y=Lx$，由 (10) 有
$$
CWy=WCy=W^2x=C^2Zx.
$$
消去单射 $C$，得到 $Wy=CZx$。因此 $y\in\mathcal D$、$Ly=Zx$。即
$$
\boxed{
L\mathcal D\subset\mathcal D,\quad
\operatorname{Dom}(L^2)=\mathcal D,\quad
L^2=Z|_{\mathcal D}.
}
\tag{18}
$$
这里是完整自然乘积定义域的等式，不把 $L^2$ 误写为全 $H$ 上的 $Z$。

$\mathcal D\ne H$：否则闭图定理及 (17) 给 $L\in\mathscr C$，再由 (15) 得 $W=CL$，违反 (13)。因此 $L$ 真正无界，$\mathcal D$ 是真稠密域。

## 5. 同域图核心与有界图空间作用

取原已付强单位 $Q_n\in C\mathscr C$，一致有界且 $Q_n\to I$ 强；可由
[R267 全部幂共同倍数](R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)
的固定分母及原强单位得到。写 $Q_n=CA_n$，$A_n\in\mathscr C$。对每个 $x\in\mathcal D$，
$$
Q_nx\to x,\qquad LQ_nx=Q_nLx\to Lx,
\tag{19}
$$
而 $Q_nx\in\operatorname{Ran}C$。故 $\operatorname{Ran}C$ 是 $L$ 的图核心。又由 (17)，$A_nx\in\mathcal D$，所以 (19) 还证明 $C|_{\mathcal D}$ 在图范数中值域稠密。使用同一共同全部幂分母，对每个固定 $r\ge1$，$C^r|_{\mathcal D}$ 同样有稠密值域。

置 $E=(\mathcal D,\|x\|_E^2=\|x\|^2+\|Lx\|^2)$。在这个真实 Hilbert 空间上
$$
C_E=C|_{\mathcal D},\quad L_E=L|_{\mathcal D}
$$
均为有界算子，且
$$
\|C_E^n\|\le\beta_n,\qquad
L_E^2=Z_E,\qquad Z_E=Z(C_E)\ \text{按 (8) 的同一绝对范数和}.
\tag{20}
$$
第一式使用 (17) 在图范数两分量上的同一个 $C^n$；第二式来自 (18)；
$L_E$ 的有界性由
$\|Lx\|_E^2=\|Lx\|^2+\|Zx\|^2\le(1+\|Z\|^2)\|x\|_E^2$。
所以 $C_E,Z_E,L_E$ 全部拟幂零。此处没有宣称 $L_E$ 单射或稠密像。

对任何已付固定全幂分母 $P=CR_1$，实际有
$$
PH\subset\mathcal D,\qquad LP=WR_1\in\mathscr C.
\tag{21}
$$
这是一个明确支付了全域包含和有界分子的正向原来源。

## 6. 新域的范围与仍未付的原二次目标

$L$ 的图是非零闭 $C\oplus C$ 不变空间。由
[原整数迹与全部较小交换域排除](R12-appendix-actual-walsh-graph-domain-integer-traces-sampling-and-single-boundary-chain.md)，
$\mathcal D$ 不可能包含于任何已研究的最大 Walsh 直和根域：该定理排除了域包含于这些域中的所有非零闭 $C$ 模图，而这里 (15)--(18) 确给实际非零闭图。此结论只区分这次构造的真实域，不通过它否定一般原根。

还可准确排除此新域作为原稳定平方根的域。若一个稠密定义的闭稳定算子 $R$ 满足
$R^2=C|_{\operatorname{Dom}R}$，且 $\operatorname{Ran}C\subset\operatorname{Dom}R$，
则 $V_0=RC$ 全域且由闭图定理有界。稳定平方身份使 $R$ 在其域上与 $C$ 交换，
所以 $V_0\in\mathscr C$ 且 $V_0^2=C^3$。任一 (2) 的兼容喷射于是给
$j_\chi(V_0)^2=z^3$，但非零形式幂级数平方的首阶为偶数，矛盾。
本次 $\mathcal D$ 含 $\operatorname{Ran}C$，故它是已构造出的不同闭稳定交换域，
同时也已排为原稳定平方根的候选域。这不排除使用平坦分母的其它域。

实际目标仍是同一个平坦分母 $P$ 与有界分子 $V$ 满足
$$
V^2=CP^2.
\tag{22}
$$
本稿 (10) 是 $W^2=C^2Z$；(21) 给 $(LP)^2=ZP^2$。两者都没有把 $Z$ 改成 $C$，也没有付未知普通旗商上的同一来源。因此原平方根及普通不变子空间问题继续开放。
