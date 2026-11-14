# 同一二次核内的固定盘逆：稀疏线性偏离与首位遗漏的慢背景

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065。
状态：完整证明的新充分条件。主工具仍是原自然域、实际进位与有界高位弱平均；新的输入是二次核内拟幂零 first 的固定参数盘逆。没有使用主 first 的全空间空谱或增生性，也不要求辅助的全空间预解预算。普通 ISP 仍开放。

## 1. 任意复主行与辅助行

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
w=b_*+\sum_{j\ge0}b_j\chi_j,\qquad a,b\in\ell^2(\mathbb C),
$$
其中主行允许有限或无限支撑。
另取任意
$$
c\in\ell^1(\mathbb C).
$$
辅助可在 $a_j=0$ 的位置非零，也可在全部物理位非零；
不要求 $c$ 与 $a$ 的相位、排序或大小在全体位置关联。

令
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad X=X_b,
$$
$$
Y=\sum_jc_j(R_j-I),\qquad
B=\sum_ja_j^2(R_j-I)^2,\qquad
T=X^2+Y-B.
\tag{1.1}
$$
$Y,B\in\mathcal A$ 按原物理位范数绝对收敛，
$T$ 取 R176 的准确自然域 $\operatorname{Dom}X^2$。
真实作用为
$$
Te^w=
\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w.
\tag{1.2}
$$

假设存在无限集合 $S\subseteq\{j:c_j\ne0\}$，
以及固定 $K<\infty$，使对充分大的物理位 $j\in S$，
$$
\boxed{|a_j/c_j|\le K.}
\tag{1.3}
$$
若 $a_j=0$，比值按0解释。
将 $S$ 上的非零辅助幅度 $|c_j|$ 作非增重排，记为 $\rho_n^{c,S}$。
沿某个无穷整数子序列 $N$，要求
$$
\boxed{
L_N:=1+\log^+\big((\rho_N^{c,S})^{-1}\big)=O(N^{3/2}).
}
\tag{1.4}
$$

**定理 1。** 在 (1.3)–(1.4) 下，
$$
\boxed{\ker T=0,\qquad\overline{\operatorname{Ran}T}=H,}
$$
因而 (1.2) 的向量非零且对原实际 $A$ 循环。

条件 (1.3) 只施加于一个无限选位集合。
$c$ 在 $S^c$ 上可以是任意 $\ell^1$ 行；
它可以恰好等于高阶近共振偏离，也可以与主行独立。
$X_b$ 不需要在全 $H$ 有有界预解式。
特别允许其未倾斜 first 属于 R138 的全平面连续谱类，
并允许任意复 $\ell^2$ 指数权。

## 2. 同一真实核内的拟幂零 first

若全部主系数为零，则 $X=a_*I$ 的自然幂域均为 $H$，本节的闭性、域和图核心事实直接成立；其余情形使用 R176 的非零主行版本。

由 [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)，
$T$ 在 $\operatorname{Dom}X^2$ 上闭且 $C$ 自伴，
$e^w$ 属于全部自然幂域并给所需图核心。
若
$$
M=\ker T,
$$
则
$$
M\subseteq\mathcal D_\infty:=\bigcap_{n\ge0}\operatorname{Dom}X^n,
\qquad X_M:=X|_M\in B(M),
$$
$$
X_M^2=(B-Y)|_M.
\tag{2.1}
$$
全部 $\mathcal A$ 系数保持 $M$ 并与 $X_M$ 交换。

$B-Y$ 属于 $\mathcal A$ 且字符为零，
故在全 $H$ 上拟幂零。
因为 $M$ 被其保持，
$$
\|(B-Y)^n|_M\|\le\|(B-Y)^n\|.
$$
由 (2.1)，
$$
\lim_{n\to\infty}\|X_M^{2n}\|^{1/(2n)}=0,
$$
从而
$$
\boxed{r(X_M)=0.}
\tag{2.2}
$$
这里谱半径只针对已经证明为全域有界的 $X_M$；
没有把完整无界 $X_b$ 说成拟幂零或空谱。

## 3. 固定参数盘上真实逆，只支付几何幂成本

由 (2.2)，对每个固定 $R<\infty$，
$$
\sum_{n\ge0}R^n\|X_M^n\|<\infty.
$$
所以
$$
(I+zX_M)^{-1}=\sum_{n\ge0}(-zX_M)^n
\tag{3.1}
$$
在 $|z|\le R$ 上按真实算子范数一致绝对收敛。
这是整个复参数平面上的算子值整函数，
但以下只使用固定盘 $|z|\le2K$。

设
$$
C_M=\sup_{|z|\le2K}\|(I+zX_M)^{-1}\|<\infty.
\tag{3.2}
$$
若 $K=0$，该常数取1。
对满足 (1.3) 的 $j\in S$，
实际线性系数
$$
L_j=8a_jX_M+4c_jI_M
=4c_j\left(I_M+2(a_j/c_j)X_M\right)
$$
在同一个 $M$ 上双射，且
$$
\boxed{\|L_j^{-1}\|\le C_M/(4|c_j|).}
\tag{3.3}
$$
特别 $a_j=0$ 时是准确标量逆 $(4c_j)^{-1}I_M$，
没有除以 $a_j$。

这些逆彼此交换，并与 $X_M$、$\mathcal A|_M$ 交换。
对有限 $F\subset S$ 定义
$$
\mathfrak R_F=\prod_{j\in F}L_j^{-1}\in B(M).
$$
则
$$
\boxed{
\left(\prod_{j\in F}L_j\right)\mathfrak R_F=I_M,\qquad
\|\mathfrak R_F\|
\le (C_M/4)^{|F|}\prod_{j\in F}|c_j|^{-1}.
}
\tag{3.4}
$$

本节没有在全 $H$ 上给 $L_j$ 求逆。
也没有把仅知单射的算子当成有界双射：
实际逆来自 (3.1)，其存在性先由 (2.1)–(2.2) 证明。
$C_M$ 可很大、可依赖假想核，但它固定，
只产生 $O(r)$ 的对数成本。

## 4. 同时选辅助大位、排主行大位、排物理低位

令 $\delta_N=\rho_N^{c,S}$。
先取 $S$ 中辅助幅度最大的 $N$ 个实际物理位，
并固定任意并列选择规则。

从中删去完整主行 $a$ 的全局最大
$\lfloor N/4\rfloor$ 个非零幅度所占的物理位；
主行不足这些项时删其全部非零位。
再删去物理位小于 $m_N=\lfloor N/4\rfloor$ 的项。
每次至多删 $\lfloor N/4\rfloor$ 项，
所以可以从剩余集合中取
$$
I_N\subset S,\qquad
|I_N|=Q_N=\lfloor N/2\rfloor.
$$
于是
$$
\min I_N\ge m_N,\qquad
|c_j|\ge\delta_N,\qquad
|a_j|\le2\|a\|_2/\sqrt N
\quad(j\in I_N).
\tag{4.1}
$$
充分大 $N$ 后，全部选位也满足 (1.3)。
$c$ 的排序和 $a$ 的排序可以完全不同；
这个双删除计数正是处理其独立性的步骤。

固定小参数 $\theta>0$，令
$$
r=\lceil\sqrt{N/\theta}\rceil.
$$
对所有 $r$ 元 $F\subset I_N$，
$$
\sum_F|a_j|\le2\|a\|_2r/\sqrt N=O_\theta(1),
\qquad
\sum_F|a_j|^2=O_\theta(N^{-1/2}).
\tag{4.2}
$$
又有
$$
\sum_F|c_j|
\le\sum_{j\ge m_N}|c_j|\longrightarrow0.
\tag{4.3}
$$
不需要 (4.3) 的任何定量速度；
统一准则的有限词与核内系数预算只要求其有界。

由 (3.4)、(4.1)，
$$
\boxed{
\log^+\|\mathfrak R_F\|
\le rL_N+C'_Mr.
}
\tag{4.4}
$$
没有 $N^2$ 级的全空间辅助预解成本。

## 5. 真实反射与深域 jets 仍完整适用

以下沿 [近共振统一准则](../results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)
的实际证明，说明它为何只需 (4.2)–(4.3) 和新的核内逆。

令 $J_F=\prod_{j\in F}M_{\chi_j}$，
$\gamma_F=\operatorname{Ad}J_F$，并只在 $F$ 内改变
$R_j=V(t_jN_j)$ 的参数符号。
定义
$$
\widehat X=X+\sum_Fa_j[V(-t_jN_j)-R_j],
$$
$$
\widehat Y=\sum_jc_j(\widehat R_j-I),\qquad
\widehat B=\sum_ja_j^2(\widehat R_j-I)^2.
$$
[R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)
的最高物理位壳层只使用
$a\in\ell^2$、$a^2\in\ell^1$、$c\in\ell^1$，
给各阶导数误差
$$
\|\delta_X^s(\gamma_FX-\widehat X)\|
+\|\delta_X^s(\gamma_FY-\widehat Y)\|
+\|\delta_X^s(\gamma_FB-\widehat B)\|
\le s!\epsilon_N,
$$
$$
\epsilon_N\le Ce^{-385\,16^{m_N-1}}.
\tag{5.1}
$$
最大物理位不限。
这里的385是实际进位的粗上界常数，不是对真实系数的错误等式。

各 $J_F$ 双向保持 $\mathcal D_\infty$。
对 $f_F=\mathfrak R_Ff\in M$，
$\|X^kf_F\|\le\|X_M\|^k\|f_F\|$。
(4.2) 给 $\widehat X-X$ 的全空间统一有界性；
结合 (5.1) 正规排序有限词，得到固定 $R_{M,\theta}$ 使
$$
\|X^kJ_Ff_F\|\le2R_{M,\theta}^k\|f_F\|
\quad(0\le k\le4r).
\tag{5.2}
$$
带误差词的全部排序成本不超过
$\epsilon_Ne^{C_\theta r\log(r+2)}$。
本步骤既不要求 $c_j\le C|a_j|^\kappa$，
也不要求对任意复指数权作半平面限制。

准确符号差为
$$
\widehat B-B
=\sum_F16a_j^2(t_jN_j)^3(I-t_j^2N_j^2)^{-2}.
\tag{5.3}
$$
因此没有 Boolean 一次项。
$N_j^3=\eta_jN_jN_{j+1}$ 真实支付余项；
$(\widehat X^2+\widehat Y-\widehat B)-T$
在同一 $M$ 上的主项是
$$
\widetilde A_F=
8X\sum_Fa_jt_jN_j
+16\left(\sum_Fa_jt_jN_j\right)^2
+4\sum_Fc_jt_jN_j.
\tag{5.4}
$$
其系数绝对范数和由 (4.2)–(4.3) 一致控制。
一次系数仍准确等于 $t_jL_j$，故
$$
\widetilde A_F^r
\equiv r!t_FN_F\prod_{j\in F}L_j
\pmod{(N_j^2:j\in F)}.
\tag{5.5}
$$

正确顺序仍为
$$
T^rJ_F\mathfrak R_Ff
=J_F(\gamma_FT)^r\mathfrak R_Ff.
$$
在 $M$ 内先用 (3.4) 取消线性系数乘积，再在左侧作用反射。
没有声称 $J_FM\subset M$，
也没有把核内逆移到反射左边。

## 6. 平均、四次支付与完整配对

令
$$
\mathcal V_N=(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F.
$$
其像在 $\mathcal D_\infty$。
组合数给
$$
\|\mathcal V_N\|\le A_N,\qquad
A_N=\frac{(2L_b)^r}{r!}\sup_F\|\mathfrak R_F\|,
$$
其中 $L_b=\max(1,\sup_j|t_j|^{-1})<\infty$。
由 (4.4)，
$$
\log^+A_N\le rL_N+C_M''r+C.
\tag{6.1}
$$

(5.1)–(5.5) 给
$$
\left\|T^r\mathcal V_Nf-
\left(\frac2{Q_N}\sum_{j\in I_N}E_j\right)^rf\right\|
\le
[\epsilon_Ne^{C_\theta r\log(r+2)}A_N
+2^rr\eta_{m_N}]\|f\|\to0.
\tag{6.2}
$$
真实物理进位压过全部 $rL_N=O(N^2)$ 成本。
纯提升算子有统一全空间范数界，
且有限柱矩阵元的系数为 $(Q_N)_r/Q_N^r$。
因此
$$
\boxed{T^r\mathcal V_Nf\rightharpoonup e^{-1/\theta}f.}
\tag{6.3}
$$
这是固定非零倍数的弱极限，未使用未知核向量的尾速率。

对固定局部矩阵 $D$，
完整 $X$ 的有限物理头、$Y$ 的有限头及 $B$ 的有限头
各自保留真实 $A$ 因子，
闭尾与 $D$ 完整域交换。
同一深域计算和 R109 四次幂界给
$$
\|(\operatorname{ad}_T^rD)\mathcal V_Nf\|
\le
2\|D\|A_NC_{D,M,\theta}^r
e^{-5r^4/6+105r^3}\|f\|.
\tag{6.4}
$$
不能把全部慢 $Y$ 除以 $A$；这里只分解固定有限头。
也不声称 (6.4) 中的交换子在全 $H$ 上有界。

若 $L_N\le C_LN^{3/2}$，则
$$
\limsup\frac{\log A_N}{r^4}
\le C_L\theta^{3/2}.
$$
先固定足够小的 $\theta$，使此数小于 $1/4$。
$C_M''r$、$r\log r$ 和局部测试常数的 $r$ 次成本除以 $r^4$ 都趋零，
所以 (6.4) 趋零。

对 $f,g\in M$，自然域 Leibniz 与完整 $C$ 双线性配对给
$$
\mathcal B(DT^r\mathcal V_Nf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD)\mathcal V_Nf,g).
$$
由 (6.3)–(6.4)，
$\mathcal B(Df,g)=0$ 对所有局部全矩阵成立。
局部矩阵代数不可约，迫 $M=0$。
$C$ 自伴性给稠密像，R176 的真实图核心及 (1.2) 给循环性。
定理 1 得证。

## 7. 交替慢幂与指数稀疏线性偏离：辅助仅缺首位

固定
$$
\frac12<\sigma<1,\qquad
a_j=(-1)^j(j+1)^{-\sigma},
\qquad a_*\in\mathbb C.
\tag{7.1}
$$
每个相位方向的缺陷都发散，故 R138 将这个完整主 first 归入
全平面连续谱分支；不是同射线空谱的旧例。

取
$$
S=\{2^k-1:k\ge1\}.
\tag{7.2}
$$
固定任意 $\kappa>2$、$\beta,\gamma\in\mathbb C\setminus\{0\}$，
以及任意单位相位 $\omega_j$，定义
$$
\boxed{
c_j=
\begin{cases}
0,&j=0,\\
\gamma a_j,&j\in S,\\
\beta|a_j|^\kappa\omega_j,&j\ge1,\ j\notin S.
\end{cases}}
\tag{7.3}
$$
该辅助恰好只在物理首位为零；所有 $j\ge1$ 均非零。
于是主首支撑 $j_a=0$，辅助首支撑 $j_c=1$。
这不满足另稿首支撑有序定理的 $j_c\le j_a$，
因此此例保留固定盘核内逆方法的独立范围。
因为 $\kappa\sigma>1$，
$$
\sum_{j\notin S}|c_j|<\infty,\qquad
\sum_{j\in S}|c_j|
=|\gamma|\sum_{k\ge1}2^{-\sigma k}<\infty.
$$
故 $c\in\ell^1$。

在 $S$ 上，
$$
a_j/c_j=\gamma^{-1},\qquad
\rho_N^{c,S}=|\gamma|\,2^{-\sigma N},
$$
所以 (1.3) 与 $L_N=O(N)$ 同时成立。
定理给，对任意复 $b\in\ell^2$、任意 $b_*$，
$$
\boxed{
\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w
\text{ 非零且循环}.
}
\tag{7.4}
$$
尤其允许 $a_*=0$。

在这个例子中甚至有同一个固定核内逆：
$$
L_j=8a_j(X_M+\gamma I/2)\quad(j\in S),
$$
而 $X_M+\gamma I/2$ 因 (2.2) 实际可逆。
不随 $N$ 缩小的这个参数是消去原共同圆周大成本的原因。

(7.3) 在 $j\ge1$ 中除指数稀疏集合外的位置保持 $\kappa$ 阶近共振；
在 $S$ 上改为与主系数线性同阶的偏离，另在首位令偏离为零。
该辅助仍有慢幂尾：
$S^c$ 密度为1，故其非零幅度重排至少具有常数倍
$n^{-\kappa\sigma}$ 的下界，
不能属于 R270E 的超三次快类。
从全位高阶近共振改到 (7.3) 的稀疏修正本身，
其排序幅度也只按 $2^{-\sigma k}$ 下降，而非超三次。
所以不能以已有快辅助定理替代本稿的核内逆证明。

## 8. 边界与真正剩余问题

这条固定盘逆准则允许任意主相位、任意复指数权，
并在首位偏离遗漏的慢背景中给出 (7.3)。

另稿
[首支撑有序的二次偏离](2026-11-13-earliest-support-dyadic-quadratic-cyclicity-central-review.md)
证明：若首个非零偏离不晚于首个非零主系数，
则任意可和偏离都能用有限 dyadic 差排核。
所以辅助全位非零、主首位非零的纯高阶偏离，
现在可由该有限头机制处理，不再作为本稿的剩余例。
本稿 §7 特意取 $c_0=0$、$a_0\ne0$，
避免将这一已覆盖情形重复计为固定盘方法的新范围。

一般首位遗漏仍不能仅由 (1.3) 解决。
例如仍取 (7.1)，但改成
$$
c_0=0,\qquad
c_j=\beta |a_j|^\kappa\omega_j\quad(j\ge1),
\tag{8.1}
$$
不再加入稀疏线性偏离。
此时对任何无限物理位集合，
$$
|a_j/c_j|
=
|\beta|^{-1}|a_j|^{1-\kappa}
\longrightarrow\infty.
$$
所以 (1.3) 不成立；
不能把 (3.2) 的固定盘常数用到半径随 $N$ 发散的盘。
同时 $j_c>j_a$，首支撑有序机制也不直接适用。

(8.1) 的全空间共同圆预算指数仍为
$$
\frac{2\sigma(\kappa-1)}{\kappa\sigma-1}>2,
$$
现有有界弱平均无法直接支付。
R259 的原点解析 Bell 分支不提供分歧平方根的有界核内求值；
R270C/D 的全空间单射及循环 iff 也不提供未知限制的稠密像；
R196/R197 的双逆关系与多坐标独立不等于
任意混合多项式在未知子空间上的单射。
本稿没有闭合这一一般首位遗漏的纯高阶分支。
