# 原 Haar 普通不变格的共同坐标旗与闭稳定平方根

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127  
作者：stable_kernel_return；§7 原输入由 root 给出并联合核算；AI-assisted GPT-6 Astra Pro。

**状态：下面是全部普通闭不变空间的准确原模型结构定理。它将 R143 特定二阶核的图结构扩到任意普通不变空间，并给真实原旗上的反向构造。不构造或排除尚未知的闭根，也不宣称普通 ISP 完成。**

本稿始终使用原 Haar 尾 $A^{(m)}$，不使用负整数边界移位 $B=\pi_-(A)$。

[R7](R7-weak-projection-support-and-graph-criterion.md) 已给一般弱投影支撑、固定锚点与有界 Riccati/Sylvester 图判据；这些不重计。本文新内容是任意普通不变空间的共同实际坐标旗、原子商上的闭稳定根、首位 gauge 和的非闭性，以及有限尾层的穷尽。

## 1. 原尾及其真实子商

令 $H_m=L^2(\mathbb Z_2,\mu)$，
$$
(A^{(m)} f)(z)=\alpha_{m+v_2(z)}f(z-1),\qquad A^{(0)}=A,
$$
原权及所有尾均按
[原尾有界根与不变投影距离](R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md) §1。
最低物理位的原酉分解给
$$
H_m=H_{m+1}\oplus H_{m+1},\qquad
A^{(m)}=\begin{pmatrix}0&A^{(m+1)}\\ \alpha_m I&0\end{pmatrix},
\qquad
(A^{(m)})^2=\alpha_m(I_2\otimes A^{(m+1)}).
\tag{1}
$$
$\alpha_m>0$。

[原尾收缩强单位](R12-appendix-contractive-strong-star-density-in-every-odd-residue-class.md)
给每个 $A^{(m)}$ 的多项式 $u_n$：
$$
u_n(0)=0,\quad \|u_n(A^{(m)})\|\le1,\quad u_n(A^{(m)})\longrightarrow I
\quad\text{强收敛}.
\tag{2}
$$
这里只需这个已付版本，不需要逆像的一致费用。

因此，对任意闭 $A^{(m)}$ 不变旗 $K_-\subset K_+$，
其真实 Hilbert 子商
$$
Q=K_+/K_-,\qquad (A^{(m)})_Q
$$
仍单射且值域稠密。
确实，$u_n(A^{(m)})$ 保持旗，诱导算子在 $Q$ 上范数不超过一并强趋恒等。
写 $u_n(z)=zv_n(z)$，若 $(A^{(m)})_Qx=0$，则所有 $u_n((A^{(m)})_Q)x=0$，故 $x=0$；
而每个 $u_n((A^{(m)})_Q)x$ 都在 $\operatorname{Ran}(A^{(m)})_Q$，故该像稠密。
同样论证包括闭不变限制。
另有
$$
\|(A^{(m)})_Q^n\|\le\|(A^{(m)})^n\|,
$$
所以该子商拟幂零。若 $Q\ne0$，它必无限维：非零有限维单射拟幂零矩阵不存在。

这些事实也见 [R140 原不变子商](R140-invariant-subquotient-type-and-fixed-first-regularization.md)。
本稿没有将全空间稠值直接限制到未知空间；实际 (2) 正是逐旗的来源。

## 2. 任意普通不变空间的两个共同坐标空间

固定 $M\in\operatorname{Lat}A^{(m)}$，允许 $M=0,H_m$。
令
$$
K_0=\{x\in H_{m+1}:(x,0)\in M\},\qquad
K_1=\{y\in H_{m+1}:(0,y)\in M\},
$$
$$
L_0=\overline{P_0M},\qquad L_1=\overline{P_1M}.
$$
$K_i$ 闭；由 (1) 的平方，四个空间都为 $A^{(m+1)}$ 不变空间。

原一次不变性给
$$
K_0\subseteq K_1,\qquad A^{(m+1)}K_1\subseteq K_0.
$$
§1 已付 $\overline{A^{(m+1)}K_1}=K_1$，故
$$
\boxed{K_0=K_1=:K_-.}
\tag{3}
$$
另一方面，对每个 $(x,y)\in M$，
$(A^{(m+1)}y,\alpha_m x)\in M$，所以
$$
L_0\subseteq L_1,\qquad A^{(m+1)}L_1\subseteq L_0.
$$
再用同一个实际稠值事实，
$$
\boxed{L_0=L_1=:K_+.}
\tag{4}
$$
于是得到完全确定的原闭不变旗及夹层
$$
\boxed{K_-\subseteq K_+,\qquad K_-^{\oplus2}\subseteq M
\subseteq K_+^{\oplus2}.}
\tag{5}
$$
这里 $K_-$ 是两坐标的实际核，$K_+$ 是实际坐标像的闭包；
不要求像本身闭，不换成完整尾空间。

## 3. 真子商上的唯一闭稳定平方根

令
$$
Q=K_+/K_-,\qquad C=(A^{(m+1)})_Q.
$$
因为 $M$ 包含整个 $K_-^{\oplus2}$，
$$
\widetilde M=M/K_-^{\oplus2}\subseteq Q\oplus Q
$$
是闭子空间。
商上的原块算子为
$$
\mathcal A_Q=\begin{pmatrix}0&C\\\alpha_m I&0\end{pmatrix},
\qquad \mathcal A_Q\widetilde M\subseteq\widetilde M.
\tag{6}
$$

若 $(\bar x,0)\in\widetilde M$，可选择 $(x,y)\in M$ 且 $y\in K_-$。
减去 $(0,y)\in M$ 后得 $(x,0)\in M$，由 (3) 得 $x\in K_-$，
故 $\bar x=0$。另一个坐标同理。
因此 $\widetilde M$ 的两个坐标投影均单射。
(4) 则给两投影的像在 $Q$ 稠密。

若 $Q=0$，(5) 恰为
$$
\boxed{M=K_-^{\oplus2}.}
\tag{7}
$$
若 $Q\ne0$，取第二坐标为输入，存在唯一算子
$$
S:\mathcal D\subseteq Q\longrightarrow Q,\qquad
\widetilde M=\{(Sy,y):y\in\mathcal D\}.
\tag{8}
$$
它单射、稠密定义、值域稠密，且闭性来自同一个闭子空间 $\widetilde M$。

最关键的域关系直接来自 (6)：
对 $y\in\mathcal D$，
$$
(Cy,\alpha_m Sy)\in\widetilde M.
$$
因此
$$
Sy\in\mathcal D,\qquad S(\alpha_m Sy)=Cy,
$$
即
$$
\boxed{S\mathcal D\subseteq\mathcal D,\qquad
S^2y=\alpha_m^{-1}Cy\quad(y\in\mathcal D).}
\tag{9}
$$
由于已付域稳定，
$$
\operatorname{Dom}(S^2)
=\{y\in\mathcal D:Sy\in\mathcal D\}=\mathcal D.
\tag{10}
$$
(9) 是实际自然平方在完整自然域上的等式，
**不是** $\operatorname{Dom}(S^2)=Q$，也不意味着 $S$ 有界。
此外 $C\mathcal D\subseteq\mathcal D$ 且 $SC=CS$ 于 $\mathcal D$，
因为 $C=\alpha_mS^2$ 于该稳定域，逐次迭代合法。

这不使用 R143 的特殊核横截条件：
任意普通 $M$ 的真实坐标核已经通过原商 (5) 准确移去。
与 [R143 §7](R143-quadratic-gauge-common-regularizers-and-kernel-graphs.md)
及[其反根图核心附录](R12-appendix-core-power-bound-and-actual-r143-inverse-root.md)
的区别，就是本节覆盖全部普通不变空间，而不只特定二阶乘子的核。

## 4. 完整反向构造及旗的恢复

反过来，取任意实际闭 $A^{(m+1)}$ 不变旗
$K_-\subsetneq K_+$，令 $Q=K_+/K_-\ne0$、$C=(A^{(m+1)})_Q$。
假设在同一个 $Q$ 上给定闭、稠密定义的 $S$，
并在其完整域 $\mathcal D$ 上满足 (9)。

$C$ 单射使 $S$ 单射。
由于 $\mathcal D$ 稠密、$C$ 有界且像稠密，
$C\mathcal D$ 亦稠密；而
$C\mathcal D=\alpha_m S^2\mathcal D\subseteq\operatorname{Ran}S$，
故 $S$ 的像稠密。
于是其图满足前节全部性质。

记 $q:K_+\to Q$ 为实际商映射，定义
$$
\boxed{
M_S=\{(x,y)\in K_+^{\oplus2}:(qx,qy)\in\mathcal G(S)\},
\qquad
\mathcal G(S)=\{(Sy,y):y\in\mathcal D\}.
}
\tag{11}
$$
这是连续映射 $(q,q)$ 下闭图的原像，故在 $K_+^{\oplus2}$、继而在 $H_m$ 中闭。
由 (9)，
$$
\mathcal A_Q(Sy,y)=(Cy,\alpha_m Sy)
=(S(\alpha_m Sy),\alpha_m Sy)\in\mathcal G(S).
$$
(1) 的原块算子保持 $K_+^{\oplus2}$ 并诱导 (6)，因此
$$
A^{(m)}M_S\subseteq M_S.
$$
$M_S$ 非零，而且真：$\mathcal G(S)$ 非零，但不包含任何非零 $(x,0)$，
故不是整个 $Q^{\oplus2}$。

该构造恢复的两坐标核恰为 $K_-$，
因为 $S$ 单射且图没有垂直向量。
两个像闭包恰为 $K_+$：它们包含 $K_-$，
在商上的像分别为 $\operatorname{Ran}S$ 与 $\mathcal D$，都稠密。
闭子空间包含 $K_-$ 时，其商像闭，故这两个闭包不能小于 $K_+$。

因此 (3)–(11) 给出**准确可逆的原来源参数化**：
每个普通 $M$ 要么是 (7) 的纯两副本，
要么由唯一原旗和其真实子商上的唯一闭稳定平方根给出。
反向步骤不用旁边的模型核、形式根或没有来源的 Hilbert 空间同构。

## 5. 首位 gauge 的交、和及非闭性

令 $U=\operatorname{diag}(I,-I)$。
由 (1)，$UA^{(m)}=-A^{(m)}U$，所以 $UM$ 仍为 $A^{(m)}$ 不变。
原坐标直接给
$$
\boxed{M\cap UM=K_-^{\oplus2},\qquad
\overline{M+UM}=K_+^{\oplus2}.}
\tag{12}
$$
第一式中，对 $(x,y)$ 同时取加减得到 $(x,0),(0,y)\in M$；
第二式由同样加减及 (4) 得到。

若 $Q\ne0$，商上的两图准确满足
$$
\mathcal G(S)+U\mathcal G(S)
=\operatorname{Ran}S\oplus\mathcal D
\subseteq Q\oplus Q.
\tag{13}
$$
这里 $\oplus$ 指两坐标的直积：
对 $y,z\in\mathcal D$，和为 $(S(y+z),y-z)$，
而 $y+z,y-z$ 可独立遍历 $\mathcal D$。
两边的交为零。

(13) 稠密而不闭。
若它闭，则两坐标分别闭；由已付稠密性，
$\mathcal D=\operatorname{Ran}S=Q$。
$S$ 闭且全域，故有界；单射且满射再给有界逆。
于是 $C=\alpha_m S^2$ 有界可逆，
与非零 $Q$ 上的拟幂零性矛盾。
因为原和包含闭子空间 $K_-^{\oplus2}$，
它闭当且仅当相应商和闭。因此
$$
\boxed{Q\ne0\Longrightarrow M+UM\text{ 稠密于 }K_+^{\oplus2}
\text{ 而不闭}.}
\tag{14}
$$

还有真实的角退化见证。
若存在 $c>0$ 使 $\|Sy\|\ge c\|y\|$ 对所有 $y\in\mathcal D$ 成立，
域稳定允许迭代，得到对任意固定非零 $y\in\mathcal D$、
所有 $n\ge1$，
$$
\alpha_m^{-n}\|C^ny\|
=\|S^{2n}y\|\ge c^{2n}\|y\|.
$$
这违反 $r(C)=0$。故
$$
\inf_{0\ne y\in\mathcal D}\frac{\|Sy\|}{\|y\|}=0.
\tag{15}
$$
可取 $\|y_n\|=1$ 且 $Sy_n\to0$。
两图中的 $(Sy_n,y_n)$、$(-Sy_n,y_n)$ 范数趋一而差趋零，
与零交共同给 (14) 的直接 bounded-below 障碍。
这里只是商后的真实两图角；未将原共同交 $K_-^{\oplus2}$ 忽略。

## 6. 有限层必出现非零图子商

假设 $0\ne M\ne H_0$ 且 $AM\subseteq M$。
若 §3 的 $Q=0$，则 $M=H_{\mathrm{bit}\,0}\otimes M_1$，
其中 $M_1$ 是原 $A^{(1)}$ 的非零真闭不变空间。
对 $M_1$ 重复同一构造。

这不可能在全部层都只给 $Q=0$。
否则对每个 $r\ge1$ 都有
$$
M=\mathbb C^{2^r}\otimes M_r,\qquad
P_M=I_{2^r}\otimes P_{M_r}.
\tag{16}
$$
所以 $P_M$ 与每个有限头完整矩阵代数交换。
原 Haar 的这些局部矩阵生成不可约 UHF 表示，
故共同交换子只有标量，$P_M$ 只能是 $0$ 或 $I$，矛盾。
也可在有限柱稠密集上直接验证：
(16) 使任意两个有限柱的 $P_M$ 矩阵元等于同一标量
$\langle P_M1,1\rangle$ 乘其内积。

因此，任意非零真普通不变空间都会在某个**有限**原尾层 $m$
产生 §3 的非零、必无限维实际子商 $Q$ 及闭稳定根 $S$。

反方向，若某层 $m$ 的实际旗和闭根存在，
§4 给 $A^{(m)}$ 的非零真不变空间 $M_S$；
用原有限头分解
$$
A=J_m\otimes I+e_{0,2^m-1}\otimes A^{(m)}
$$
可直接将 $\mathbb C^{2^m}\otimes M_S$ 提升为原 $A$ 的非零真闭不变空间。
$m=0$ 无需提升。

所以得到候选本身的完整等价：
$$
\boxed{
\operatorname{Lat}A\ne\{0,H\}
\iff
\text{某个有限原尾层存在上述非零实际旗子商的闭稳定平方根。}
}
\tag{17}
$$
(17) 是原候选普通不变格的结构等价，不是已证明其中某一侧成立。

## 7. 全原尾标量乘合型闭根的排除

这节只排除一个具体的全尾构造类，不对 §3 的未知实际子商施加额外假设。
固定任意原 Haar 尾 $A^{(k)}$，记
$$
(A^{(k)}f)(z)=a_k(z)f(\tau z),\qquad
\tau z=z-1,\qquad a_k(z)=\alpha_{k+v_2(z)}>0\quad\text{a.e.}
$$
不存在如下稳定域平方根：$R$ 是 Haar 空间上可逆、双向 nonsingular 的可测变换，
$h$ 可测且 $0<|h|<\infty$ a.e.，闭稠密定义算子 $S$ 在其完整域 $\mathcal D$ 满足
$$
(Sf)(z)=h(z)f(Rz),\qquad S\mathcal D\subseteq\mathcal D,\qquad
S^2f=cA^{(k)}f\quad(f\in\mathcal D),
\tag{18}
$$
其中 $c\ne0$。不要求 $\mathcal D$ 一开始包含常数或柱函数。

令 $g=h\,(h\circ R)$。$R$ nonsingular 保证 $g$ 有限且非零 a.e.。
最大乘合算子
$$
Wf=g\,(f\circ R^2),\qquad
\operatorname{Dom}W=\{f\in L^2:g(f\circ R^2)\in L^2\}
$$
是闭的：若 $f_n\to f$、$Wf_n\to u$ 均在 $L^2$，
取同时逐点收敛的子列；由 $R^2$ nonsingular，
沿同一子列 $f_n\circ R^2\to f\circ R^2$ a.e.，
故 $u=g(f\circ R^2)$ a.e.。
由 (18)，$cA^{(k)}|_{\mathcal D}\subseteq W$。
$\mathcal D$ 稠密而 $cA^{(k)}$ 有界，闭性遂给
$$
cA^{(k)}\subseteq W.
$$
左侧已经全域，因而 $W=cA^{(k)}$，其域也等于整个 $L^2$。
现在可合法测试 $1$ 与所有柱指标函数。先得到
$g=c\,a_k$ a.e.，再因该函数非零而得到
$$
f\circ R^2=f\circ\tau
$$
对可数的全部柱指标成立。柱集分离 $\mathbb Z_2$ 中的点，因此
$$
R^2=\tau\quad\text{a.e.}
\tag{19}
$$

(19) 及 nonsingularity 给 $R\tau=\tau R$ a.e.。
取首位 parity
$$
\chi(z)=(-1)^{z\bmod 2},\qquad \chi\circ\tau=-\chi.
$$
则 $\psi=(\chi\circ R)/\chi$ 只取 $\pm1$，并满足
$$
\psi\circ\tau
=\frac{\chi\circ R\circ\tau}{\chi\circ\tau}
=\frac{\chi\circ\tau\circ R}{-\chi}=\psi.
$$
原 Haar odometer $\tau$ 遍历，所以 $\psi=\sigma$ a.e.，
其中 $\sigma\in\{1,-1\}$。
这里遍历性也可由有限柱直接验证：
每个深度 $n$ 的条件期望在被 $\tau$ 循环的 $2^n$ 个柱上相同，
再令 $n\to\infty$，任何 $\tau$ 不变函数均为常数。
于是 nonsingularity 允许再复合一次，得到
$$
\chi\circ R^2=\sigma^2\chi=\chi,
$$
与 (19) 的 $\chi\circ\tau=-\chi$ 矛盾。

这排除了全尾上通过单个标量权与点变换构造稳定闭平方根的路线。
它没有排除非局部闭算子根，也没有将未知旗子商 $Q$ 认作原测度空间，
更不提供任意闭根的乘合表示。

## 8. 真正未付的下一步

本文未证明任何新旗或闭根存在，也未排除它们。
全尾单拷贝上有界平方根已由原重数定理排除；
在未知实际子商 $Q$ 上不能直接使用那个整重数目标。
闭根的自然平方域准确为 $\mathcal D$，
不能从平方等于有界限制推出 $\mathcal D=Q$。
若另付实际伴随域包含，可用已刊闭根引理得到有界性，
但该包含仍是原同域来源问题。

负整数边界 $B,T_N,T_Y$ 的核、稳定像、光滑核或其闭根
均未进入 (17)。必须使用此处同一个原 Haar 旗、原子商及原闭域。

构造 (17) 中一个根会给这个原候选的普通不变空间；
排除所有这些实际根才会排除候选的全部非平凡普通空间。
前者只是处理本候选，仍不是“所有有界算子有不变空间”的一般定理。
本文不降低 README 完成标准。
