# R456 — 原三次接触首核的两条 carry 首提升不相容

日期：2026-11-14。**状态：已证明。** 本篇对 R453 的同一个实际计算格给出两项结果。其次数二导子的来源饱和范围可加强到 $f_D<p$；对一个明确的三次高接触因子，真实相对 $J$ 的两个 Gaussian 块对首次修正提出不相容的要求，规范后的差为单位 $5$。保因子的条件由同一预算中的实际修正空间给出，并有明确的结式充分界。此结论排除一类真正的相对 $p^2$ 提升；不把它说成全部 $D\asymp\sqrt p$ 临界矩阵已无缺陷，也不删除原 $m_{13}$ 的两条十三行 carry。

## 1. 同一个原来源及实际三块评价

采用 R403、R453 的共同 $E_1$、$p=6s-1>83$、
$1\le\ell<s-13$、$L=2s+\ell$，以及
$$
d=1+8t,\qquad h_7=7+4t+16t^2,\qquad
f=d\,t(t-1)h_7/7,\qquad
\mathscr R=\Theta^{17}d,\qquad T_0=\Theta^{36}f.
$$
继续使用 R453 的全部计算格
$$
\widetilde{\mathcal W}_{D,J}
=\bigoplus_{n=0}^D\bigoplus_{j=0}^J
\mathscr R^nq_n\mathcal O[t]_{\le e_{n+1}+6j}T_0^j,
\qquad 0\le J\le16.
\tag{1}
$$
原 $\mathcal W_{D,J}$ 通过 $P(t)T^j=P(t)V^jT_0^j$ 整嵌入 (1)。本篇始终使用这个相同的物理函数，未将 $T_0$ 另作中央零来源。

把 (1) 写在真实两个独立变量 $t,\Theta$ 中，每一列都是多项式：
$$
\mathscr R^nq_nP(t)T_0^j
=\Theta^{17n+36j}d^{n-C_n}(th_7)^{A_n}(t-1)^{B_n}f^jP(t).
$$
因为 $n-C_n\ge0$，没有清分母后另添来源。完整有限格包含于矩形多项式模
$$
\boxed{\deg_\Theta P\le N:=17D+36J,\qquad
\deg_t P\le M:=\lfloor11D/2\rfloor+4+11J.}
\tag{2}
$$
这里 $M$ 包括原 $V^j$ 所占的全部六次角成本；对原格和 (1) 是同一个上界。

在实际 regularized frame 中置
$$
\vartheta(w)=(g(w)/d(t(w)))^{1/17},\qquad
\Theta_{\rm phys}=\vartheta(w)e_2(a\epsilon/17),\qquad
w^s=p\epsilon,\quad a=p\kappa\in\mathcal O^\times.
\tag{3}
$$
根取常数项一。这里只读取原已付的三块整窗口；其中十七次根整且唯一。令
$$
\mathcal E=\frac{\Theta}{17}\partial_\Theta,
\qquad P_i(w)=(\mathcal E^iP)(t(w),\vartheta(w)),
\qquad \mathscr S F=\sum_{r\ge0}[w^{s+r}]F\,w^r.
$$
这一个 $\mathcal E$ 正是原相对 charge $n+(36/17)j$，不是只读 $n$。

从同一个 $e_2(a\epsilon\mathcal E)$ 逐项进位，得到完整整评价
$$
\boxed{J(P)=\left(
[P_0]_{<s},\quad
[aP_1+p\mathscr SP_0]_{<s},\quad
\left[\frac{a^2}{2}P_2+pa\mathscr SP_1+p^2\mathscr S^2P_0\right]_{<\ell}
\right).}
\tag{4}
$$
所有 $P_i$ 都是 (3) 的实际系数；$\mathscr SP_0$、$\mathscr SP_1$ 不是可选尾项。以下首次提升中的不相容正来自这两条真实进位。

## 2. 次数二来源导子的饱和范围加强到 fD 小于 p

R453 的闭合算子仍为
$$
\mathcal Q_2=W_2t\partial_t\quad(\mathscr R\text{ 固定}),\qquad
W_2=\mathscr R^2t(t-1)^2d h_7^2.
$$
其目标是 $\widetilde{\mathcal W}_{D+2,J}$。这里的来源、目标都是 R453 已明确的有限自由整模。

对 $0\le j\le16$，取唯一 $0\le E_j<p$ 满足
$17E_j\equiv19j\pmod p$，并令
$$
r_{n,j}=\langle-A_n-j\rangle_p,\qquad
u_{n,j}=\langle-B_n-j\rangle_p,\qquad
z_{n,j}=\langle C_n+E_j\rangle_p.
$$
与 R408 相同的真实常量域和逐 $(n,j)$ 独立性给准确核：
$$
\boxed{
\ker\bar{\mathcal Q}_2\big|_{(n,j)}
=\mathscr R^nq_nT_0^j
(th_7)^{r_{n,j}}(t-1)^{u_{n,j}}d^{z_{n,j}}
\left\{Q(t^p):\ p\deg Q+\mu_{n,j}\le e_{n+1}+6j\right\},}
\tag{5}
$$
其中 $\mu_{n,j}=3r_{n,j}+u_{n,j}+z_{n,j}$。确切常量域仍是 $k(\mathscr R)(\Theta^p)$；不能把它换成 $k(\mathscr R)^p$。式 (5) 只是分别解每个独立分量的对数导数后得到的多项式表示。

**证明。** 函数 $q_nP(t)T_0^j$ 的导数为零，准确要求
$$
\frac{P'}P
=-(A_n+j)\left(\frac1t+\frac{h_7'}{h_7}\right)
-\frac{B_n+j}{t-1}
+\left(C_n+\frac{19j}{17}\right)\frac8d.
$$
式 (5) 显示的最小剩余指数给一个解。商的导数为零，故商属于 $k(t^p)$；因为各有限零阶都小于 $p$，商不能有有限极，所以它属于 $k[t^p]$。固定除子 $t,t-1,h_7,d$ 在当前好特征平方自由、两两互素，已由 R408 的明确判别式和结式支付。次数截断给 (5)。

若
$$
\boxed{f_D=\lfloor9D/2\rfloor+4<p,}
\tag{6}
$$
则 $1\le j\le16$ 时 $0<A_n+j,B_n+j<p$。因而
$$
\begin{aligned}
\mu_{n,j}-(e_{n+1}+6j)
&\ge4p-f_n-C_n-10j\\
&>\frac{26}{9}p-160>0.
\end{aligned}
$$
这里用 $C_n<p/9$；没有从移掉 $V$ 的六根免费得到饱和。故全部非零 $j$ 分量的核为零。$j=0$ 时，$q_nP$ 在无穷处和 $-1/8$ 的极阶分别小于 $p$，导数为零只能是常数；原强迫零只留下 $n=0,1$ 的两列 $1,\mathscr R$。

特征零的核也是这两列：非零 $j$ 在 $d=0$ 的对数残数 $C_n+19j/17$ 非整数，排除有理解。比较两个特征的秩遂给
$$
\boxed{
\widetilde{\mathcal W}_{D,J}/\langle1,\mathscr R\rangle
\xrightarrow{\mathcal Q_2}
\widetilde{\mathcal W}_{D+2,J}
\text{ 的像为 }p\text{-饱和。}}
\tag{7}
$$
若 (6) 对所有经过的最大次数成立，反复连接和 R453 的一次原返回也保持原先证明的来源饱和。这个较宽范围包含固定 $J$、$D\asymp\sqrt p$ 的来源预算；它没有判定物理 $J$ 的 Smith 因子。$\square$

## 3. 一条真实三次因子的首核和首次修正

以下所有约化都在同一个剩余域 $k$。设一个非零实际来源的约化满足
$$
\bar P=F^3Q\in k[t,\Theta],\qquad
F\text{ 不可约},\qquad
F(0,1)=0,\quad F_\Theta(0,1)\ne0,\quad Q(0,1)\ne0.
\tag{8}
$$
写
$$
h=\operatorname{ord}_wF(t(w),\bar\vartheta(w)),\qquad1\le h<s.
\tag{9}
$$
所需的 $h<s$ 只读取原完整规范中已经固定的低轴。没有改变实际高轴或两中央参数。

由于 $\mathcal EF$ 在原点为单位，准确有
$$
\operatorname{ord}\bar P_0=3h,\qquad
\operatorname{ord}\bar P_1=2h,\qquad
\operatorname{ord}\bar P_2=h.
$$
因此由 (4)，
$$
\boxed{\bar P\in\ker\bar J\quad\Longleftrightarrow\quad
2h\ge s,\qquad h\ge\ell.}
\tag{10}
$$

现在假设存在一个**同一实际来源格**中的真正首次提升 $P^{(2)}$，使
$$
P^{(2)}\bmod p=F^3Q,\qquad J(P^{(2)})\in p^2\Gamma_L.
\tag{11}
$$
取保持双次数的多项式系数提升 $\widetilde F,\widetilde Q$。则
$$
\boxed{P^{(2)}=\widetilde F^3\widetilde Q+pR,\qquad
R\in\mathcal O[t,\Theta],\quad
\deg_\Theta R\le N,\quad\deg_tR\le M.}
\tag{12}
$$
这里不主张 $\widetilde F$、$\widetilde Q$ 或其积分别属于 (1)。若 $P^{\rm base}$ 是一个固定实际来源提升，允许的 $\bar R$ 准确落在
$$
\overline{(P^{\rm base}-\widetilde F^3\widetilde Q)/p}
+\overline{\widetilde{\mathcal W}_{D,J}},
\tag{13}
$$
而不是任意矩形多项式。下述必要条件先在这个真实仿射空间内成立；使用 (2) 只是给一个更大的、可完全核定的排除范围。

**引理 1。** (11) 必迫
$$
\boxed{\operatorname{ord}_w\bar R(t(w),\bar\vartheta(w))\ge s,
\qquad
\operatorname{ord}_w(\mathcal E\bar R)(t(w),\bar\vartheta(w))\ge h.}
\tag{14}
$$

**证明。** 令 $f(w)=\widetilde F(t(w),\vartheta(w))$、$e(w)=(\mathcal E\widetilde F)(t(w),\vartheta(w))$。可以准确写
$$
f=w^hu+p\xi,\qquad \xi\in\mathcal O[w]_{<h},\qquad
u(0),e(0)\in\mathcal O^\times.
\tag{15}
$$
式 (10) 给 $2h\ge s$。于是
$f^3\equiv w^{3h}u^3+3pw^{2h}u^2\xi\pmod{p^2}$，其 $w^s$ 以下项全被 $p^2$ 整除。$\widetilde Q$ 的 regularized 评价是整单位。由 (4) 第一块得 (14) 第一式。

第二块除以 $p$ 后，$\mathcal E(\widetilde F^3\widetilde Q)/p$ 在 $w^s$ 以下可能出现的项至少从 $w^h$ 起；其首个潜在项来自 $6w^hu\xi e\bar Q$。另一项 $\mathscr S(\bar F^3\bar Q)$ 从 $w^{3h-s}$ 起，而 $3h-s\ge h$。因此该块低于 $h$ 的全部修正只能是 $a\mathcal E\bar R$，其必须为零。这就是 (14) 第二式。$\square$

## 4. 保因子的准确结式条件

令
$$
a_F=\deg_tF,\qquad b_F=\deg_\Theta F,\qquad
B_0=b_FM+a_FN,\qquad B_1=B_0-2a_Fb_F.
\tag{16}
$$
**引理 2。** 若
$$
\boxed{s>B_0,\qquad h>B_1,}
\tag{17}
$$
则 (14) 迫使 $F^2\mid\bar R$。也可不用 (17)，直接在 (13) 的真实修正空间验证：满足 (14) 的元素全部被 $F^2$ 整除。下文只需这个实际保因子条件。

**证明。** 因 $F_\Theta(0,1)$ 为单位，有唯一正规分支 $\psi(t)\in k[[t]]$，满足 $F(t,\psi(t))=0$、$\psi(0)=1$。原 $t(w)$ 是严格参数的单位倍，所以
$$
\operatorname{ord}_t(\bar\vartheta-\psi)=h.
$$
由 (14)，$\bar R(t,\bar\vartheta)$ 的阶至少为 $s$，而 $\partial_\Theta\bar R(t,\bar\vartheta)$ 的阶至少为 $h$。在两个实际分支之间作多项式 Taylor 展开，余下二次项至少有 $2h$ 阶。因 $2h\ge s$，得到
$$
\boxed{\operatorname{ord}_t\bar R(t,\psi(t))\ge s.}
\tag{18}
$$
这里正是首次提升的导数条件把接触从 $h$ 提到 $s$；只用 $\bar R$ 的第一条接触而删去导数，不能得到 (18)。

若 $F\nmid\bar R$，则非零 $\operatorname{Res}_\Theta(F,\bar R)$ 的次数至多 $B_0$。同一个 Sylvester 整 Bézout 式在正规分支 $\Theta=\psi(t)$ 上给其消失阶至少 $s$，与 $s>B_0$ 矛盾。故写 $\bar R=FR_1$。

因为 $\mathcal EF$ 为单位，$\mathcal E\bar R=(\mathcal EF)R_1+F\mathcal ER_1$ 与 (14) 迫 $R_1(t,\bar\vartheta)$ 至少有 $h$ 阶；否则第一项的严格较低阶无法抵消。换到 $\psi$ 后仍至少有 $h$ 阶。此时 $R_1$ 的双次数至多 $(M-a_F,N-b_F)$，与 $F$ 的结式次数至多 $B_1$。由 $h>B_1$ 同样得 $F\mid R_1$。$\square$

(17) 是明确的充分条件，未声称每个原临界因子都满足它。其预算要按 (2)、(16) 逐一代入，不能用来源维数代替结式次数。

## 5. 两条真实 carry 对同一根修正的单位 5 障碍

**定理。** 假定 (8)–(10) 和上述实际保因子条件成立。令
$$
k=2h-s\ge0.
$$
若
$$
\boxed{k<\min(s-h,\ell),}
\tag{19}
$$
则 $F^3Q$ **没有**满足 (11) 的同格提升。因此它在相对首核中的 Bockstein 类非零，不能代表相对 $K_2^{\rm red}(J)$。

**证明。** 由保因子条件，(12) 可写成
$$
P^{(2)}\equiv\widetilde F^3\widetilde Q
+p\widetilde F^2H\pmod{p^2}.
$$
$\widetilde Q$ 的完整物理评价为单位，故可在同一个整目标中消去它。令
$$
\widehat F=\widetilde F+\frac{pH}{3\widetilde Q}.
$$
这是用于计算的局部整分式，不是新增的来源列；$Q(0,1)\ne0$ 保证其整个目标评价整。准确有
$$
J(P^{(2)})\equiv J(\widetilde Q)J(\widehat F)^3\pmod{p^2}.
\tag{20}
$$
所以 (11) 要求 $J(\widehat F)^3=0\pmod{p^2}$。

继续记 $f=\widehat F(t(w),\vartheta(w))=w^hu+p\xi$、
$e=(\mathcal E\widehat F)(t(w),\vartheta(w))$。
这次 $u,e$ 的约化首项仍是原单位；$\xi$ 包含实际高轴和本次真实首次修正。式 (4) 对 $\widehat F^3$ 第一块已自动满足。第二块除以 $p$、约化后，准确为
$$
\boxed{\left[w^hu\{6a\xi e+w^ku^2\}\right]_{<s}=0.}
\tag{21}
$$
这是 $a\mathcal E(\widehat F^3)/p$ 与 $\mathscr S(\widehat F^3)$ 的完整和；系数六来自 $3\cdot2$，不能改为一个。

第三块除以 $p$ 后，由 $h\ge\ell$ 得
$$
\boxed{\left[3ae\{a\xi e+w^ku^2\}\right]_{<\ell}=0.}
\tag{22}
$$
其中 $\mathcal E^2(\widehat F^3)=6\widehat F(\mathcal E\widehat F)^2+3\widehat F^2\mathcal E^2\widehat F$；后一项在所读低轴不贡献第一整商。另一个完整贡献是 $a\mathscr S\mathcal E(\widehat F^3)=3aw^ku^2e$。$p^2\mathscr S^2$ 项在这里的首次商中才合法消失。

式 (21) 等价于
$$
6a\xi e+w^ku^2=0\pmod{w^{s-h}},
$$
式 (22) 等价于
$$
a\xi e+w^ku^2=0\pmod{w^\ell}.
$$
由 (19)，两式都读取第 $k$ 个系数。第二式乘六并从第一式减去，得到
$$
-5w^ku^2=0\pmod{w^{\min(s-h,\ell)}},
$$
其第 $k$ 系数是 $-5u(0)^2\in k^\times$，矛盾。$\square$

这是原相对首次提升的具体不相容：同一个根修正 $\xi$ 不能分别为两条进位选择不同值。原 $a$、完整 $g$ 和两条真实尾都在计算中；它没有使用一个自由修改的高轴。

### 最小三次接触的准确边界

在保因子条件已付时，若 $h=\lceil s/2\rceil$、$\ell\le h$，则：

- $s$ 为偶数时 $k=0$，所有 $1\le\ell\le h$ 都被本定理排除。
- $s$ 为奇数时 $k=1$，所有 $2\le\ell\le h$ 都被排除。
- $s$ 为奇数、$\ell=1$ 时第二块之外的真实末块读不到第一个 $w$ 系数，本证明没有给出矛盾。

更一般，边界就是 (19) 的两个严格不等式。不能将 $k=\ell$ 或 $k=s-h$ 的截断外项当作可读行。

## 6. 返回原 M、完整基准和仍未付的范围

整个计算可以先应用于 (1)，再通过 R453 的真实包含和一次固定返回运输；其来源饱和现在可用 (6)。原矩阵始终为
$$
M^{\rm orig}=c_*U_0m_{13}J.
$$
本篇排除的是相对 $K_2^{\rm red}(J)$ 的指定三次方向。它不排除某个相对首提升落在原两条十三行 carry 像中，从而仍给 $K_2^{\rm red}(M)$ 的可能性。这个区别由 R449 的准确式
$$
K_2^{\rm red}(M)=\ker(\pi\beta_J),\qquad
G_2=C_2(J)/\overline H
$$
保持；不能把本篇单位五直接说成原全部 $C_2(M)$ 消失。全部 $P_{134}$、$U_0$、最初十三个自由行和二十六条原 carry 都保留。

原两条完整中央条件仍只属于 $S$ 和 $T=VT_0$，在同一规范下为
$$
a^2c_1-pa c_2+2p^2c_3=0,\qquad
\alpha^2a^2d_1-p\alpha a d_2+2p^2d_3=0\pmod{p^3}.
$$
本篇没有把它们分配给 $F$、$Q$、$T_0$ 或各来源幂。这里的排除甚至不需要假设这两条中央失败，因而不能反向宣称中央失败已经产生了一个满足 (8)、(17)、(19) 的三次因子。

真正余下的对象是：同一低预算中没有被上述因子判据覆盖的相对第二类，特别是一般不可约多接触来源、没有付清保因子的首次修正空间，以及它们与两条完整中央基准的实际相容性。没有扩大有限素数扫描，也没有把明确的因子范围冒称整个临界窗。

## 依赖和复算

R408 的真实分量核方法；R453 的计算格、全 floor 连接和一次整返回；R338/R403 的完整实际三块；R449 的相对第二余核及两条 carry 精确序列。`scripts/check-r456-cubic-two-carry.py` 检查固定多项式次数、最小核指数的对数残数、三次物理乘法与 (21)–(22) 的系数六/一，以及严格窗口的全部边界；跨参数证明在正文。
