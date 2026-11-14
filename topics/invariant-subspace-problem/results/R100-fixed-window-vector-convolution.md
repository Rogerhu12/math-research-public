# R100：固定头窗口的真实尾向量卷积

日期：2026-11-12
作者：Astra-ISP-0c017065 / l2_moments
状态：已证明；正式结果 R100，已独立交叉核验。本稿给出真实算子到任意固定有限头窗口的完整向量卷积接口，不声称该卷积系统的所有一般有限次数解已经排除。

依赖：R84 的有限次数 $\ell^2$ 合成；R40 的近周期有限链机制。以下把条件化、卷积系数、全部尾测试、误差排列和固定系数锚逐项写出。与 R94/R98 的全部 $2^m$ 维头恢复相比，此处不使用头 Walsh 插值多项式，因而没有 $2^{2^m}$ 因子。

## 1. 模型、记号和主定理

沿用实际算子 $A$、权 $\alpha_m^{\rm op}$、归一化幂 $N_j$ 和双线性型
$$
B(f,g)=\int f(y)g(-1-y)\,d\mu(y).
$$
记
$$
W_n=\|A^n\|=\prod_{\ell=1}^n\alpha^{\rm op}_{v_2(\ell)},
\qquad W_0=1,
\qquad N=2^m,\qquad C_m=W_{N-1}.
\tag{1.1}
$$
$A_m$ 是只作用于低 $m$ 位的有限链；第 $j$ 位的独立模型为 $E_j=e_{10}$。令
$$
T_j=2N_j-I,\qquad S_j=2E_j-I,\qquad
\|N_j-E_j\|=\eta_j.
\tag{1.2}
$$
本题实际权满足
$$
\|A^n-A_m^n\|\le n\alpha_m^{\rm op},
\qquad
\log\frac{\alpha_m^{\rm op}}{C_m}
=-\frac{260}{3}16^m+75\,8^m+O(m2^m),
\tag{1.3}
$$
以及 $\eta_m\le e^{-770\,16^m}$。

设
$$
f\in H_{\le p},\qquad g\in H_{\le q},\qquad
B(A^nf,g)=0\quad(n\ge0).
\tag{1.4}
$$
$p,q$ 可以只是次数上界；本稿的主估计不要求它们恰为实际次数。

固定任意有限 $B_0\subseteq[m,\infty)$，写
$$
s=|B_0|,\qquad E=[m,\infty)\setminus B_0.
\tag{1.5}
$$
把 $B_0$ 上的物理位固定为零，并把低 $m$ 位固定为整数 $i\in\{0,\ldots,N-1\}$，所得 $E$ 上的列向量记为
$$
F_i=f|_{[0,m)=i,\ B_0=0},\qquad
G_i=g|_{[0,m)=i,\ B_0=0}.
\tag{1.6}
$$
这是有限坐标条件化，精确定义和范数见 §2。

对 $F\in H_{\le p}(E)$，定义独立尾模型乘法
$$
\mathcal M_F v
=\sum_{k=0}^p(-1)^k\mathscr S_k(F_k)v
=\sum_{\substack{J\subseteq E\\|J|\le p}}
(-1)^{|J|}\widehat F(J)S_Jv.
\tag{1.7}
$$
后一个和按 R84 在每个有限次数输入空间上连续收敛，而不是声称它在全部 $H$ 上有界。其性质在 §3 证明。

对 $0\le r<N$，定义完整尾向量
$$
\boxed{
v_r=\sum_{i=0}^r
\frac{\mathcal M_{F_i}G_{r-i}}{W_iW_{r-i}}
\in H_{\le p+q}(E).
}
\tag{1.8}
$$

**定理 1.1。** 存在只依赖 $p,q$ 的常数 $K_{p,q}$，对全部 $m$、任意有限 $B_0\subseteq[m,\infty)$ 及 $0\le r<N$，
$$
\boxed{
\|v_r\|_2
\le K_{p,q}2^s
\left[
\frac{N(N-1-r)\alpha_m^{\rm op}}{C_m}
+\frac{N(s+1)\eta_m}{W_r}
\right]\|f\|_2\|g\|_2.
}
\tag{1.9}
$$
因此对任意固定窗口长度 $R$，当 $N>R$ 时，
$$
\boxed{
\max_{0\le r\le R}\|v_r\|_2
\le K_{p,q,R}2^s
\left[
\frac{N^2\alpha_m^{\rm op}}{C_m}
+(s+1)N\eta_m
\right]\|f\|_2\|g\|_2.
}
\tag{1.10}
$$
固定窗口的联合直和范数也满足同型界，仅多出固定因子 $\sqrt{R+1}$。
所有常数都不依赖被条件化顶点的最大编号。

主项的对数为
$$
-\frac{260}{3}16^m+s\log2+\log(s+1)
+O_{p,q,R}(8^m+m2^m).
\tag{1.11}
$$
特别地，$s=O(4^m)$ 时仍是
$\exp[-(260/3)16^m+o(16^m)]$；
若 $s\le b16^m+O(1)$，则主指数至多为
$-[260/3-b\log2]16^m+o(16^m)$。

## 2. 有限条件列的意义与范数

令 $I=[0,m)\cup B_0$。按 $I$ 上的 Walsh 系数分组，
$$
f=\sum_{\substack{K\subseteq I\\|K|\le p}}\chi_Kf_K,
\qquad
\sum_K\|f_K\|_2^2=\|f\|_2^2,
$$
其中每个 $f_K$ 只依赖剩余位 $E$。给定 $I$ 上的任意物理取值，只是用 $\pm1$ 替换有限个 $\chi_j$，所以
$$
\|F_i\|_2
\le D_p(m+s)\|f\|_2,
\qquad
D_p(t)=\left(\sum_{k=0}^p\binom tk\right)^{1/2}
\le C_p(t+1)^{p/2}.
\tag{2.1}
$$
同理，
$$
\|G_i\|_2\le D_q(m+s)\|g\|_2.
\tag{2.2}
$$
这些估计与 $i$、被条件化坐标的编号无关。条件列的总剩余 Walsh 次数分别不超过 $p,q$。

本稿没有在无穷多个位上取点值，也没有要求整数点迹存在或列均值随 $m$ 收敛。

## 3. 完整独立尾乘法与双线性对偶

对有限支撑 $h=\sum_{|J|\le L}h_J\chi_J$，$J\subseteq E$，定义
$$
P_h(A)=\sum_{|J|\le L}(-1)^{|J|}h_JT_J,\qquad
\widetilde P_h=\sum_{|J|\le L}(-1)^{|J|}h_JS_J.
\tag{3.1}
$$
因为 $S_j1=-\chi_j$，有
$$
\widetilde P_h1=h.
\tag{3.2}
$$
R84 给出只依赖 $p,L$ 的常数 $U_{p,L},V_{p,L}$，使
$$
\|\widetilde P_h f\|_2\le U_{p,L}\|h\|_2\|f\|_2,
\tag{3.3}
$$
$$
\|(P_h(A)-\widetilde P_h)f\|_2
\le V_{p,L}\eta_m\|h\|_2\|f\|_2.
\tag{3.4}
$$
例如可取
$$
U_{p,L}=\left(\sum_{k=0}^LC_{p,k}^2\right)^{1/2},
\qquad
V_{p,L}=\left(\sum_{k=0}^LD_{p,k}^2\right)^{1/2},
\tag{3.5}
$$
其中 $C_{p,k},D_{p,k}$ 是 R84 的常数，$D_{p,0}=0$。
限制合成指标避开 $B_0$ 不会增加这些常数。
这里直接对原全空间的有限次数向量 $f$ 调用 R84，
仅把测试系数在不允许的指标集合上设为零。
实际 $N_j$ 可能进位到 $B_0$ 中更高的位，并未被当作在 $B_0$ 上张量恒等；
只有纯模型 $S_j$ 可以把不作用的位视为 Hilbert 系数。
因此 (3.3)—(3.4) 都始终作用于原向量 $f$。

(1.7) 同样由 R84 定义，并满足
$$
\mathcal M_F1=F,\qquad
\|\mathcal M_FG\|_2\le K_{p,q}'\|F\|_2\|G\|_2.
\tag{3.6}
$$
其输出次数至多 $p+q$。有限和中各 $S_j$ 彼此交换，且对剩余双线性型
$$
B_E(u,v)=\int u(x)v(\bar x)\,d\mu_E(x)
$$
对称，这里 $\bar x$ 是每一剩余位的物理补位。因此有限和先有
$$
B_E(\widetilde P_hF,G)
=B_E(h,\mathcal M_FG).
\tag{3.7}
$$
对 $F$ 作有限系数截断，再使用 R84 在所需的各个固定次数层上的连续性，即把 (3.7) 延拓到任意 $F\in H_{\le p}(E)$。
在这个论证中，$\mathcal M_F$ 仅作用于有限次数向量，不涉及全部 $H$ 上的乘法定义域。

## 4. 近周期有限链的精确卷积

令 $n=N-1-r$。有限链在物理头坐标上满足
$$
(A_m^nu)(j)=
\begin{cases}
\dfrac{W_j}{W_{j-n}}u(j-n),&j\ge n,\\
0,&j<n.
\end{cases}
\tag{4.1}
$$
对 $0\le t<N$，由
$v_2(N-\ell)=v_2(\ell)$（$1\le\ell<N$）可得
$$
W_{N-1-t}=\frac{C_m}{W_t}.
\tag{4.2}
$$
特别地，
$$
W_n=\frac{C_m}{W_r}.
\tag{4.3}
$$

写
$$
N_{B_0}=\prod_{j\in B_0}N_j,\qquad
E_{B_0}=\prod_{j\in B_0}E_j.
$$
逐位有
$$
B(E_ju,v)=\tfrac12 B_{\rm remaining}(u|_{b_j=0},v|_{b_j=0}).
\tag{4.4}
$$
故 $E_{B_0}$ 将两端的 $B_0$ 位都固定为物理零，贡献因子 $2^{-s}$。
又 $\widetilde P_h$ 不作用于头或 $B_0$。在 $B$ 的头配对中，
物理索引 $j$ 与 $N-1-j$ 配对。代入 (4.1)，再置 $i=j-n$，得到
$$
\begin{aligned}
B(A_m^nE_{B_0}\widetilde P_hf,g)
&=\frac{2^{-s}}N
\sum_{i=0}^r\frac{W_{n+i}}{W_i}
B_E(\widetilde P_hF_i,G_{r-i})\\
&=\frac{2^{-s}C_m}N
\sum_{i=0}^r
\frac{B_E(\widetilde P_hF_i,G_{r-i})}{W_iW_{r-i}}\\
&=\frac{2^{-s}C_m}N B_E(h,v_r).
\end{aligned}
\tag{4.5}
$$
最后一步正是 (3.7)。这是完整尾向量卷积的精确模型恒等式，不只是标量均值关系。

删去任意不连续的高位集 $B_0$ 不影响公式：反射在每个位上独立补位，剩余位上的 $B_E$ 仍是标准保范数双线性配对。

## 5. 真实算子替换：把合成留在原向量上

所有 $P_h(A)$、$N_j$ 与 $A$ 交换。因此
$A^nN_{B_0}P_h(A)$ 是 $A$ 的多项式，其与 $f,g$ 的配对由 (1.4) 为零。
另一方面，
$$
\|N_{B_0}\|\le1,\qquad
\|N_{B_0}-E_{B_0}\|
\le\sum_{j\in B_0}\eta_j\le s\eta_m.
\tag{5.1}
$$

使用如下准确排列：
$$
\begin{aligned}
&A^nN_{B_0}P_h(A)-A_m^nE_{B_0}\widetilde P_h\\
&\quad=
A^nN_{B_0}(P_h(A)-\widetilde P_h)
+A^n(N_{B_0}-E_{B_0})\widetilde P_h
+(A^n-A_m^n)E_{B_0}\widetilde P_h.
\end{aligned}
\tag{5.2}
$$
不要求 $N_{B_0}$ 与 $\widetilde P_h$ 交换。
每个合成估计都先作用于原来的有限次数 $f$；
尤其没有把 $N_{B_0}f$ 或 $A^nf$ 当作有限 chaos。

将 (3.3)—(3.4)、(5.1)、(1.3) 和 $\|A^n\|=W_n$ 代入：
$$
\begin{aligned}
&\|(A^nN_{B_0}P_h(A)-A_m^nE_{B_0}\widetilde P_h)f\|_2\\
&\quad\le
\left[
W_n(V_{p,L}+sU_{p,L})\eta_m
+n\alpha_m^{\rm op}U_{p,L}
\right]\|h\|_2\|f\|_2.
\end{aligned}
\tag{5.3}
$$
这里 $L=p+q$ 已足以恢复 (1.8) 的全部输出次数。

结合实际矩为零和模型恒等式 (4.5)，并使用 $W_n=C_m/W_r$，
$$
\begin{aligned}
|B_E(h,v_r)|
\le 2^s
\left[
\frac{N(V_{p,L}+sU_{p,L})\eta_m}{W_r}
+\frac{Nn\alpha_m^{\rm op}U_{p,L}}{C_m}
\right]
\|h\|_2\|f\|_2\|g\|_2.
\end{aligned}
\tag{5.4}
$$
有限支撑尾测试在 $H_{\le p+q}(E)$ 中稠密，而 $v_r$ 位于该空间；
$B_E$ 由保范数反线性对合实现，因此对全部 $\|h\|_2\le1$ 取上确界，得到 (1.9)。

固定 $R$ 时，$1/W_r\le1/W_R$，于是得到 (1.10)。
再代入实际权 (1.3)，得到 (1.11)。$\eta_m$ 项比
$\alpha_m^{\rm op}/C_m$ 项衰减更快。
联合直和估计可对各行平方求和；窗口有限，只损失固定常数。

## 6. 固定最高系数的列均值锚

这里另假设 $p$ 是 $f\ne0$ 的实际最高次数。
选固定 $p$ 元集合 $S_f$，满足 $\widehat f(S_f)\ne0$，
并取 $m>\max S_f$。对 $T\subseteq S_f$，令
$$
i_T=\sum_{j\in T}2^j,\qquad
a_{i,m,B_0}=\int_E F_i.
$$
则对每个允许的 $B_0$，精确有
$$
\boxed{
2^{-p}\sum_{T\subseteq S_f}(-1)^{|T|}
a_{i_T,m,B_0}
=\widehat f(S_f).
}
\tag{6.1}
$$
证明：条件化后再对剩余位求均值，只保留原支撑于
$[0,m)\cup B_0$ 的 Walsh 系数。
对 $S_f$ 上的 $2^p$ 个物理取值作带符号平均，
只保留包含 $S_f$ 的原支撑。
但原总次数不超过 $p=|S_f|$，
所以唯一可能支撑恰为 $S_f$。
这也说明新增高位条件化不会污染右端。

因此
$$
\max_{T\subseteq S_f}|a_{i_T,m,B_0}|
\ge|\widehat f(S_f)|>0.
\tag{6.2}
$$
这些列索引都落在固定窗口
$0\le i\le\sum_{j\in S_f}2^j$ 中，与 $m,s$ 及高位的位置无关。
对 $g$ 的实际最高系数完全同理。
这给出有限窗口的非坍缩标量锚，不要求任何单个列均值有极限。

若一端实际为常数，则其均值本身就是相应锚。

## 7. 共同最高尾核和头卷积的预处理

每个 $F_i$ 的纯尾 $p$ 阶部分都相同：
$$
(F_i)_p=
\sum_{\substack{S\subseteq E\\|S|=p}}\widehat f(S)\chi_S.
\tag{7.1}
$$
因为原次数不超过 $p$，含任何已条件化头位或 $B_0$ 位的项都不可能还留有 $p$ 个剩余尾位。因此
$$
F_i-F_j\in H_{\le p-1}(E)
\tag{7.2}
$$
对所有 $i,j$ 精确成立；同样的陈述适用于 $G$。

进一步，在任意固定形式窗口 $0\le r\le R$，
定义标量幂级数的截断逆
$$
b(z)=\sum_{i=0}^R\frac{z^i}{W_i},
\qquad
\beta(z)b(z)\equiv1\pmod{z^{R+1}},
\tag{7.3}
$$
以及
$$
c_r=\sum_{i=0}^r\beta_{r-i}\frac{F_i}{W_i}.
\tag{7.4}
$$
这些系数只使用固定的 $W_0,\ldots,W_R$，故变换和逆变换在固定窗口上的常数不依赖 $m$。
由 (7.1)，
$$
(c_0)_p=(F_0)_p,\qquad (c_r)_p=0\quad(1\le r\le R).
\tag{7.5}
$$
对 (1.8) 的输出向量序列作同一标量卷积，得到
$$
\sum_{k=0}^r\beta_{r-k}v_k
=\sum_{i=0}^r
\mathcal M_{c_i}\frac{G_{r-i}}{W_{r-i}}.
\tag{7.6}
$$
左右两侧是实际定义的有限次数向量，(7.6) 来自有限和的双线性，不涉及形式级数的收敛问题。

所以在固定窗口内，最高尾次数只需留在零号系数，其余头系数的尾次数严格下降。这是后续有限 Toeplitz 向量卷积分析的可用输入；本稿不预设该系统具有统一左逆。

## 8. 本条解决的接口与准确边界

本稿恢复了每一个固定头窗口中的全部尾向量卷积，误差与最高删位编号无关，只有明确的 $2^s$ 和线性 $s+1$ 代价。
它完整保留有限次数下降项，且能与 R96/R97 的影响量剥离和创建左界结合。
固定最高系数给非坍缩窗口锚，共同最高核则给 (7.5) 的下降结构。

这一接口在 R99 中已用于完成二阶端点的全部有限次数配对；一般次数的闭合须调用相应后续分层证明，不能只从本接口跳步。
本稿没有由零矩在稠密类成立推出闭包成立，也没有把局部列范数的多项式增长替代统一有界性。


**后续闭合：** [R101](R101-all-finite-chaos-moment-separation.md) 已用完整嵌套窗口和逐层冻结污染的证明，完成任意两个有限全局 Walsh 次数向量的配对分离。本文保留其自身独立的工具与适用边界；任意 L² 端点仍未由此解决。
