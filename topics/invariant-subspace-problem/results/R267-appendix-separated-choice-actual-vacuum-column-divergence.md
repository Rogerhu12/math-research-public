# R267 附录：一个合法分离选择中的实际单真空列发散

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整的实际单列下界。** 本稿加强[分离块算子范数稿](R267-appendix-separated-blocks-actual-even-cut-source-fees-and-fixed-denominator-divergence.md)的来源选择，构造同一合法族，使每个固定正有理数 $t$ 都满足
$$
\|Y_NP_t\Omega\|\longrightarrow\infty
\quad(N\to\infty,\ N\text{ 偶}),
\qquad
\boxed{\|Q_N(t)\Omega\|\longrightarrow\infty\quad(N\to\infty).}
\tag{1}
$$
这不是从算子范数发散推单列发散。证明另付了真正的真空列下界及未来尾在该列上的保留。只排本文明确选取的分离构造，不排全部合法重叠或耦合块选择。

## 1. 原首位块使真空列控制奇部

固定原 Haar 尾 $C=A^{(m_0)}$。记 $c=a_0=\|C\|$、$a_1=\|A^{(m_0+1)}\|$，并用原首位分解
$$
C=\begin{pmatrix}0&B\\cI&0\end{pmatrix},
\qquad B=A^{(m_0+1)},\qquad
\Omega=\frac1{\sqrt2}(\omega,\omega).
\tag{2}
$$
令 $G=\operatorname{diag}(I,-I)$，于是 $GCG=-C$。

每个有界 $X\in C'$ 都有准确形式
$$
X=\begin{pmatrix}E&BW\\cW&E\end{pmatrix},\qquad
EB=BE,\quad WB=BW.
\tag{3}
$$
这由 $XC=CX$ 的四块直接得出，$W=c^{-1}X_{10}$；没有对 $B$ 求逆。其奇部为
$$
X_{\rm odd}=\frac{X-GXG}{2}
=\begin{pmatrix}0&BW\\cW&0\end{pmatrix}.
$$
将 $X\Omega$ 的两个坐标相减，得到
$$
\|X\Omega\|\ge\frac12\|(cI-B)W\omega\|
\ge\frac{c-a_1}{2}\|W\omega\|.
$$
另一方面，
$$
\|X_{\rm odd}\Omega\|
\le\frac{\sqrt{c^2+a_1^2}}{\sqrt2}\|W\omega\|.
$$
故对每个同一 $X$，
$$
\boxed{
\|X\Omega\|\ge
\kappa\,\|X_{\rm odd}\Omega\|,
\qquad
\kappa=\frac{c-a_1}{\sqrt{2(c^2+a_1^2)}}>0.
}
\tag{4}
$$
原权比给 $a_1/c<1/4$，亦可用保守常数 $\kappa>1/2$。这个估计保原 $B$ 的全部尾作用；并没有把奇部作用于 $\Omega$ 偷换为 $X$ 的算子范数。

## 2. 局部半整数解析单位的真空下界

使用前稿 §2 的原记号。固定偶数 $a\ge0$、整数 $p\ge0$、$m\ge1$、$0<\zeta<1$，而后令 $q$ 增大：
$$
F=\frac2{q+2}\sum_{j=m}^{m+q-1}\frac{C^{2^j}}{\beta_{2^j}},
\qquad
\beta_n=\|C^n\|=\prod_{h=1}^n a_{v_2(h)},
$$
$$
U(z)=u_0+v(z),\qquad u_0=\zeta/c,\qquad
v(z)=\frac{2(1-\zeta)}{q+2}
\sum_{j=m}^{m+q-1}\frac{z^{2^j-1}}{\beta_{2^j}},
$$
$$
X=C^{a+p+1}U(C)^{p+1/2}.
\tag{5}
$$
分数幂仍只作用于 $U(0)>0$ 的同一解析单位。

置
$$
k=a+p+2,\quad J=m+q,\quad \ell=J-k+1,
$$
并假设 $q\ge k-1$。定义
$$
\mathcal A_q=
\left|\binom{p+1/2}{k}\right|\frac{k!}{2}
\left(\frac{\zeta}{c}\right)^{-a-3/2}
\left(\frac{2(1-\zeta)}{q+2}\right)^k
\frac1{a_\ell},
$$
$$
\mathcal B=
c^{a+1/2}\sum_{r=0}^{a+p+1}
\left|\binom{p+1/2}{r}\right|
\zeta^{p+1/2-r}(1-\zeta)^r.
\tag{6}
$$
则真正的单列界为
$$
\boxed{\|X\Omega\|\ge
\kappa\bigl(2^{-J/2}\mathcal A_q-\mathcal B\bigr).}
\tag{7}
$$

**证明。** 因为 $v$ 的全部次数为奇数，$X_{\rm odd}$ 的二项式展开只保留 $r\equiv p\pmod2$。对所有这些 $r\ge k$，
$\binom{p+1/2}{r}<0$。每个 $C^{k-1}v(C)^r$ 保持函数正锥。因此这些高阶项作用于 $\Omega$ 后同号，不能互相抵消。

该二项式级数在算子范数下绝对收敛，因为 $v(C)$ 拟幂零。于是负高阶和是一个实际负函数，其绝对值逐点至少为其中任一正单项的绝对值。前 $k$ 项的算子范数总和不超过 $\mathcal B$：对 $0\le r\le k-1$，使用
$$
C^{k-1}v(C)^r=(1-\zeta)^r C^{k-1-r}F^r,
\qquad \|F\|\le1.
$$
奇部投影 $X\mapsto(X-GXG)/2$ 不增加算子范数，故前段对 $\Omega$ 的范数也至多为 $\mathcal B$。

在 $r=k$ 中取与前稿相同的完整 $k$ 叶单项
$$
2^{J-1},2^{J-2},\ldots,2^{\ell+1},2^\ell,2^\ell.
$$
重数为 $k!/2$，乘回 $C^{k-1}$ 后次数为 $2^J-1$；原权身份
$$
\beta_{2^J-1}
=\frac{\bigl(\prod_{j=\ell+1}^{J-1}\beta_{2^j}\bigr)
\beta_{2^\ell}^{\,2}}{a_\ell}
$$
给出该单项的系数乘 $\beta_{2^J-1}$ 恰为 $\mathcal A_q$。

现在用真实真空列，而不使用算子范数系数界。在低 $J$ 位全为 $1$ 的原 Haar 柱上，$C^{2^J-1}\Omega$ 的权路径恰经过 $1,\ldots,2^J-1$ 的全部非零低位余数，完全不跨深尾。因此
$$
C^{2^J-1}\Omega=\beta_{2^J-1}
\quad\text{在该测度 }2^{-J}\text{ 的柱上},
$$
从而
$$
\|C^{2^J-1}\Omega\|\ge2^{-J/2}\beta_{2^J-1}.
\tag{8}
$$
高阶同号性与前段界给
$\|X_{\rm odd}\Omega\|\ge2^{-J/2}\mathcal A_q-\mathcal B$。
再用 (4) 得 (7)。证毕。

对固定 $a,p,m,\zeta$，原 $-\log a_\ell$ 的正主项为
$(280/3)16^{m_0+\ell}$。它超过这里的 $J\log2/2$ 与固定 $k$ 次的 $\log(q+2)$ 损失，故 (7) 随 $q\to\infty$ 趋于无穷。

## 3. 一次合法选择，支付所有整数参数的同列费用

沿用相容族
$$
M_n=(n+1)!,\quad d_n=M_{n+1}-M_n,\quad
\epsilon_n=\frac{2^{-n-6}}{1+d_n},\quad
\zeta_n=\epsilon_n/8,\quad
Z_n=(1-\zeta_n)F_{m_n,q_n}+\zeta_n C/c.
$$
原混合系数仍固定为 $\epsilon_n/8$；不为支付单列而修改它。

对偶数 $N\ge2$ 和整数 $1\le t\le N$，前稿 §3 的同一合法切口恒等式仍为
$$
Y_NP_t=A_{N,t}T_{r,N+1},\qquad
r=t+\frac1{2M_N}<N+1,
\tag{9}
$$
$$
A_{N,t}=B_{N,t}C^{a+p+1}U_N(C)^{p+1/2},
\quad
B_{N,t}=\prod_{\nu<N}U_\nu(C)^{t d_\nu},
\quad a=tM_N,\quad p=t d_N+N/2.
\tag{10}
$$
$B_{N,t}$ 可逆且在选择 $q_N$ 前已经固定。

每一步先选择 $m_n$ 覆盖所有此前规定的前缀长度及前 $n+1$ 个 Walsh 测试，再增大 $q_n$。除原两个强误差之和不超过 $\epsilon_n/2$ 外，对偶数 $n=N$ 还用 (7) 同时安排
$$
\|A_{N,t}\Omega\|\ge16N\qquad(1\le t\le N).
\tag{11}
$$
这里使用 $\|B_{N,t}X\Omega\|\ge\|X\Omega\|/\|B_{N,t}^{-1}\|$；增加 $q_N$ 能同时满足有限组条件。

$A_{N,t}$ 属于原 UHF 代数。由 [R9 §3、(3.3)](R9-radial-odometer-and-nilpotent-approximants.md) 的原范数截断，选共同长度 $L_N$ 和真实有限头矩阵，使
$$
\widehat A_{N,t}=A^0_{N,t}\otimes I,\qquad
\|A_{N,t}-\widehat A_{N,t}\|
\le\frac{\|A_{N,t}\Omega\|}{32}.
\tag{12}
$$
这是相对单列范数的精度，不能沿用相对 $\|A_{N,t}\|$ 的旧精度。以后安排
$$
m_\nu\ge L_N\qquad(\nu>N).
\tag{13}
$$
每个阶段只有有限个此前的偶数 $N$，所以这种递归可持续；没有修改此前选定的块。所有 $P_r$ 都来自同一完成后的因子列。

## 4. 未来原尾保留这一个向量

固定 (9) 的 $N,t$，令
$$
\widetilde T=
\operatorname*{SOT^*\!-\!lim}_{K\to\infty}
\prod_{\nu=N+1}^{K-1}F_{m_\nu,q_\nu}^{r d_\nu}.
$$
它存在且收缩。原 dyadic 张量式和 (13) 给准确的
$$
\widetilde T=I_{<L_N}\otimes\widetilde T^{\rm tail}.
\tag{14}
$$
这是原 $C^{2^j}$ 的真实张量身份，没有删 carry。

由原真空误差及 $r<N+1$，
$$
\|(\widetilde T-I)\Omega\|
\le\frac r2\sum_{\nu>N}d_\nu\epsilon_\nu
<(N+1)2^{-N-7}<\frac1{16}.
$$
故
$$
\|\widetilde T^{\rm tail}\Omega_{\rm tail}\|>\frac{15}{16}.
\tag{15}
$$
这里用的是真空列范数，不只是尾算子的范数。

整数幂和收缩乘积的完整范数望远镜、$\|Z_\nu-F_\nu\|\le2\zeta_\nu$ 给
$$
\|T_{r,N+1}-\widetilde T\|
\le2r\sum_{\nu>N}d_\nu\zeta_\nu
<(N+1)2^{-N-8}<\frac1{16}.
\tag{16}
$$
关键是 $A_{N,t}$ 与两个完整原尾都交换。因此
$$
A_{N,t}(T_{r,N+1}-\widetilde T)\Omega
=(T_{r,N+1}-\widetilde T)A_{N,t}\Omega,
$$
其范数至多为 $\|A_{N,t}\Omega\|/16$。无需引入
$\|A_{N,t}\|/\|A_{N,t}\Omega\|$ 的费用，也无需缩小已经固定的 $\zeta_\nu$。

由 (12)、(14)–(16)，
$$
\begin{aligned}
\|A_{N,t}T_{r,N+1}\Omega\|
&\ge
\|\widehat A_{N,t}\widetilde T\Omega\|
-\|A_{N,t}-\widehat A_{N,t}\|
-\|(T_{r,N+1}-\widetilde T)A_{N,t}\Omega\|\\
&>
\left(\frac{31}{32}\frac{15}{16}
-\frac1{32}-\frac1{16}\right)\|A_{N,t}\Omega\|\\
&>\frac12\|A_{N,t}\Omega\|
\ge8N.
\end{aligned}
\tag{17}
$$
第一项是精确的向量张量范数
$\|A^0_{N,t}\Omega_{<L_N}\|
\|\widetilde T^{\rm tail}\Omega_{\rm tail}\|$。
因此 (17) 确实支付完整 $Y_NP_t$ 的同一单列，未让有限喷射穿过平坦尾。

## 5. 同一个选择中的全部有理参数与切口

固定任意正有理数 $t$，取整数 $k>t$。所有原系数交换，所以
$$
Y_NP_k\Omega=P_{k-t}(Y_NP_t\Omega).
$$
沿充分大的偶数 $N$，由 (17)，
$$
\|Y_NP_t\Omega\|
\ge\frac{8N}{\|P_{k-t}\|}\longrightarrow\infty.
\tag{18}
$$
固定分母稿的实际式 $Y_NP_t=CD_NQ_N(t)$ 及 $\|D_N\|\le1$ 给
$$
\|Q_N(t)\Omega\|\ge c^{-1}\|Y_NP_t\Omega\|.
\tag{19}
$$
对充分大的奇数 $N$，倍率 $M_{N+1}/M_N=N+2$ 为奇数；旧实际收缩及交换性给
$$
Q_{N+1}(t)\Omega=R_{N,N+1}Q_N(t)\Omega,\qquad
\|R_{N,N+1}\|\le1.
$$
故奇数切口的单列范数至少为下一个偶数切口的单列范数。于是 (1) 对所有切口成立。

与此同时，[全切口平方稿](R267-appendix-all-cut-square-contractions-and-unconditional-strong-square-limit.md) 对这个选择仍完全适用：
$$
Q_N(t)^2\longrightarrow C^{-1}P_{2t}\quad\text{强*}.
\tag{20}
$$
右边是实际单射稠值来源。因此本例保留当前同族的非零、单射平方极限；它具体说明这个平方控制本身不付[单列根接口](R267-appendix-single-actual-denominator-column-compactness-and-stable-root.md)要求的强紧性。

本稿仅处理按 (11)–(13) 作出的合法分离选择，未对一般重叠选择、不同平坦分母或未知闭根域证明不可能。正向根来源仍须继续寻找，普通 ISP 未完成。
