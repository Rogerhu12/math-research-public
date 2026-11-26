# R271 附录：全部正远孔的移动 coherent 整行、准确层权与完整 matched 来源费用

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿把原第一远孔 Bessel 行扩为全部正远孔的同一有界整行。不同远孔数之间的交叉没有被删掉；一个由原连续尾确定的准确层权支付这些交叉。其逆权在 $p\le2x$ 内只付 $O(p)$ 的平方费用。随后把全部幂行同时接到原同一 $w/u$ 的 matched 完整 Schur 配对，给真正有限头 MP 的最优费用表达。物理层权、旧头强位、原全部右段和 partial 支撑均保留。该 MP 的实际最低源上界以及稳定范围端点仍须另外支付。

依据：

- [原第一远孔整行及同源 matched 配对](R271-appendix-moving-first-far-coherent-row-bessel-and-matched-source-cost.md)。
- [强尾重分组和同一个顶部来源](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。
- [原完整头源及实际方差极限](R271-appendix-exponential-strong-prefix-actual-variance-source-limit.md)。

内积对第一变量线性。所有尾位都是原 N/Y 二进制物理位，不改无限张量积参考。

## 1. 全部正远孔的准确相干读行

沿原连续尾记
$$
b_i=(i+1)^{-2},\qquad a_i=b_i^2,\qquad
S_x=\sum_{i\ge x}a_i,\qquad D_x=\sum_{i\ge x}b_iE_i,\qquad x\ge1.
$$
对 $p\ge0$ 定义原初等对称和
$$
e_p(x)=\sum_{\substack{I\subset\{x,x+1,\ldots\}\\|I|=p}}\prod_{i\in I}a_i,
\qquad e_0(x)=1 .
\tag{1.1}
$$
因为 $a\in\ell^1$，有 $0<e_p(x)\le S_x^p/p!$。特别所有以下规范化均合法。

令
$$
\nu_{x,p}=p!\sqrt{e_p(x)},\qquad
\varphi_{x,p}=\frac{(D_x^*)^p\Omega}{\nu_{x,p}}
=\frac{\sum_{|I|=p,\ I\ge x}(\prod_{i\in I}b_i)e_I}{\sqrt{e_p(x)}},
\qquad p\ge1.
$$
每个 $\varphi_{x,p}$ 都是原远尾第 $p$ 孔层中的单位向量。定义整头读行
$$
\beta_{x,p}
=\nu_{x,p}^{-1}D_x^pP_{\{\mathcal N_{\ge x}=p\}}
:\mathcal H\longrightarrow\mathcal H_{<x}.
\tag{1.2}
$$
其伴随准确为
$\beta_{x,p}^*z=z\otimes\varphi_{x,p}$，故
$\beta_{x,p}\beta_{x,p}^*=I$、$\|\beta_{x,p}\|=1$。
不同 $p$ 的伴随范围正交。这些是原整个头空间上的行，不是固定一个头坐标。

取准确层权
$$
\boxed{
\omega_{x,p}^2=\frac{S_{x+p-1}}{pS_x},\qquad p\ge1.
}
\tag{1.3}
$$
有 $0<\omega_{x,p}\le p^{-1/2}\le1$，且 $\omega_{x,1}=1$。
在同一个定义域 $\mathcal H$ 上，堆叠全部正孔行：
$$
\boxed{
\mathcal B_x w=(\omega_{x,p}\beta_{x,p}w)_{p\ge1}
\in\bigoplus_{p\ge1}\mathcal H_{<x}.
}
\tag{1.4}
$$
正交性直接给 $\|\mathcal B_x\|\le1$。
所有无限直和均按平方可和范数定义。

## 2. 一个保留全部孔数的尾占据估计

对 $y>x$，令 $P_y^+=P_{\{\mathcal N_{\ge y}\ge1\}}$。
在固定 $p$ 的相干概率分布 $a_I/e_p(x)$ 下，至少一孔落在 $[y,\infty)$ 的概率满足
$$
\begin{aligned}
\|P_y^+\varphi_{x,p}\|^2
&\le\frac1{e_p(x)}
  \sum_{i\ge y}a_i\,e_{p-1}(\{a_j:j\ge x,\ j\ne i\})\\
&\le S_y\,\frac{e_{p-1}(x)}{e_p(x)}.
\end{aligned}
\tag{2.1}
$$
第一步只用逐集合的 union bound；集合含多个远孔时允许重复计数。

另一方面，正项逐次计数给
$$
p\,e_p(x)=
\sum_{\substack{|J|=p-1\\J\ge x}}
a_J\sum_{\substack{i\ge x\\i\notin J}}a_i
\ge S_{x+p-1}\,e_{p-1}(x).
\tag{2.2}
$$
原因是 $a_i$ 随 $i$ 递减，去掉任意 $p-1$ 个位置后，剩余总和至少为
$S_{x+p-1}$。各和绝对收敛，非负求和允许直接换序。
因此
$$
\boxed{
\|P_y^+\varphi_{x,p}\|^2
\le\min\left\{1,\frac{pS_y}{S_{x+p-1}}\right\}.
}
\tag{2.3}
$$
不要求 $p/x$ 小，也没有用低孔近似替代真实初等对称和。

因为 $P_y^+$ 与原 $\mathcal N_{\ge x}$ 的各层投影交换，
(1.3)、(2.3) 在整个直和上给
$$
\boxed{
\|\mathcal B_xP_y^+\|\le\sqrt{S_y/S_x}.
}
\tag{2.4}
$$
具体地，各 $p$ 块的范数平方不超过
$\omega_{x,p}^2pS_y/S_{x+p-1}=S_y/S_x$；
这些块的定义域彼此正交，所以只取上确界，不再付一个孔层数。

## 3. 全高度交叉与整行 Bessel 定理

$\operatorname{Ran}\mathcal B_y^*$ 全部位于
$\{\mathcal N_{\ge y}\ge1\}$。故 (2.4) 给
$$
\boxed{
\|\mathcal B_x\mathcal B_y^*\|
\le\sqrt{S_y/S_x}\qquad(x<y).
}
\tag{3.1}
$$
这条证明保留了所有 $p\ne q$ 交叉：$\mathcal B_y^*$ 的头输入可以在
$[x,y)$ 占据任意孔，其产生的层间混合已包含在 $P_y^+$ 中。
不能把本式解释成各固定 $p$ Bessel 界的无代价求和。

设整数起点满足
$$
x_{\ell+1}\ge\lambda(x_\ell+1),\qquad\lambda>1,\qquad
\rho=\lambda^{-3/2}.
$$
原积分比较
$$
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3}
$$
使 $\|\mathcal B_{x_\ell}\mathcal B_{x_k}^*\|
\le\rho^{|\ell-k|}$。
和旧单孔证明一样，对有限直和用块范数行和，再以非负单调极限，得到
$$
\boxed{
\sum_\ell\sum_{p\ge1}
\frac{S_{x_\ell+p-1}}{pS_{x_\ell}}\,
\|\beta_{x_\ell,p}w\|^2
\le\mathcal B_\lambda\|w\|^2,\qquad
\mathcal B_\lambda=\frac{1+\lambda^{-3/2}}{1-\lambda^{-3/2}} .
}
\tag{3.2}
$$
同一分析算子的伴随给完整合成界
$$
\left\|\sum_\ell\mathcal B_{x_\ell}^*z_\ell\right\|^2
\le\mathcal B_\lambda\sum_\ell\|z_\ell\|^2.
\tag{3.3}
$$
对平方可和的整个来源族，级数在原物理范数中收敛。

准确逆权还满足
$$
\boxed{
\omega_{x,p}^{-2}
=\frac{pS_x}{S_{x+p-1}}
\le p(1+p/x)^3.
}
\tag{3.4}
$$
因此 $p\le J\le2x$ 时仅有
$\omega_{x,p}^{-2}\le27p\le27J$。
特别，任取随起点变化的正整数 $1\le J_\ell\le2x_\ell$，
$$
\sum_\ell\frac1{J_\ell}
\sum_{p=1}^{J_\ell}\|\beta_{x_\ell,p}w\|^2
\le27\mathcal B_\lambda\|w\|^2 .
\tag{3.5}
$$
这正是全部远孔层、完整增长头的 $O(J_\ell)$ 平方费用。

## 4. 原同一 $w/u$ 的全部幂行 matched 配对

取一列原合法参数 $m,R,Q$，置
$$
d=2^m,\qquad x=m+R,\qquad h=d+R,\qquad
C=A_m+D_{[m,x)}.
$$
保原同一个 $w\in W$ 和
$$
u=(P_{V_{m,Q}}-P_{K_{m,Q}})w,\qquad
\|u-P_{\mathcal N\le Q}w\|\le2\eta_m\|w\|,\qquad
\eta_m=e^{-6d^4}.
\tag{4.1}
$$
$\mathcal N$ 仍是原 $m$ 后总尾孔数。

使用依赖稿的同一原匹配记号：
$r_n=Cu_n$，完整左最小列 $U_n$，完整／裸右费 $H_n,B_n$，以及
$$
\mathcal P_n=(L_n+H_n)^{-1}(H_n-B_n),\qquad
a_n=r_n-\mathcal P_nr_n,\qquad
Y_n=(u_{n+1},\ldots,u_{n+h}).
$$
原完整投影恒等式为
$$
\mathfrak M_n(g)=\langle U_n\mathcal P_nr_n,i_0g\rangle,\qquad
U_nr_n=u_{\le n},\qquad
\|U_na_n\|\le\|Y_n\|.
\tag{4.2}
$$

现在在本个强头中、所有 cut 之前固定一个真实分解
$$
\boxed{
g=g_{\rm ker}+\sum_{p=1}^J(C^*)^pt_p,\qquad
g_{\rm ker}\in\ker C,\qquad 1\le J\le h-1.
}
\tag{4.3}
$$
不把 $t_p$ 改成逐 cut 重新选择的来源。
对 $n\ge J$ 且 $n+h+R<Q$，
$v=U_n\mathcal P_nr_n$ 属于原真左空间，并正交于其零源核。
故 $i_0g_{\rm ker}$ 在配对中准确消失；
原逐层低方程给
$C^pv_0=(-D_x)^pv_p$，对全部 $1\le p\le J$ 同时成立。
于是
$$
\mathfrak M_n(g)
=\sum_{p=1}^J(-1)^p\nu_{x,p}
   \langle\beta_{x,p}v,t_p\rangle
=\langle\mathcal B_xv,z\rangle,
\tag{4.4}
$$
其中
$$
z_p=(-1)^p\frac{\nu_{x,p}}{\omega_{x,p}}t_p\quad(1\le p\le J),
\qquad z_p=0\quad(p>J),
$$
$$
\boxed{
\Gamma^2=\|z\|^2
=\sum_{p=1}^J
  \frac{(p!)^2e_p(x)}{\omega_{x,p}^2}\|t_p\|^2 .
}
\tag{4.5}
$$

在 $Q\ge R+J$ 下，每条 $\beta_{x,p}^*$ 的原总尾孔支撑不超过 $R+p$，
所以 $\beta_{x,p}P_{\mathcal N\le Q}=\beta_{x,p}$ 对这些 $p$ 准确成立。
结合 (4.1)--(4.4)、$v=u_{\le n}-U_na_n$ 和 $\|\mathcal B_x\|\le1$，得到
$$
\boxed{
\left|\mathfrak M_n(g)-\langle\mathcal B_xw,z\rangle\right|
\le\Gamma\big(\|Y_n\|+2\eta_m\|w\|\big).
}
\tag{4.6}
$$
这保留所有原强位和全部 $h$ 段。没有只取一个远孔层，也没有把一个 partial 的来源移给另一个 cut。

## 5. 同一来源平均与全高度必要费用

取
$$
\mathcal I_\ell=\{n:n_{0,\ell}\le n\le Q_\ell-R_\ell-h_\ell-1\},
\quad N_\ell=|\mathcal I_\ell|>0,\quad n_{0,\ell}\ge J_\ell .
$$
令
$$
b_\ell=\|P_{\{\mathcal N_{\ge x_\ell}>n_{0,\ell}\}}u_\ell\|,\qquad
e_\ell=2\eta_{m_\ell}\|w\|
 +\sqrt{h_\ell/N_\ell}\,b_\ell,\qquad
\Phi_\ell=\frac1{N_\ell}\sum_{n\in\mathcal I_\ell}\mathfrak M_n(g_\ell).
$$
每个远孔层在未来带中最多出现 $h_\ell$ 次，故 (4.6) 平均给
$$
|\Phi_\ell-\langle\mathcal B_{x_\ell}w,z_\ell\rangle|
\le\Gamma_\ell e_\ell.
\tag{5.1}
$$
若 $\Gamma_\ell>0$，由 (3.2) 及 Cauchy，
$$
\boxed{
\sum_\ell\frac{|\Phi_\ell|^2}{\Gamma_\ell^2}
\le2\mathcal B_\lambda\|w\|^2+2\sum_\ell e_\ell^2 .
}
\tag{5.2}
$$
若某个 $\Gamma_\ell=0$，(4.3) 只剩零源核部分，因而其 $\Phi_\ell=0$，该项省去。

因此，在原 $\sum_\ell e_\ell^2<\infty$ 的母窗内，任何满足
$|\Phi_\ell|\ge c>0$ 的同源非零锚必须支付
$\sum_\ell\Gamma_\ell^{-2}<\infty$。
这是一条保留全部幂行的必要费用，不是 MP 成本上界。

## 6. 全部幂来源的真正最优有限头费用

在固定有限强头和 $J\ge1$ 中，令
$$
\mathscr G_{x,J}
=\sum_{p=1}^J
\frac{\omega_{x,p}^2}{(p!)^2e_p(x)}(C^*)^pC^p .
\tag{6.1}
$$
其核准确为 $\ker C$，因为每项非负且第一项系数为正。
令 $g_\perp=(I-P_{\ker C})g$。以 (4.3) 为约束，
(4.5) 的真正最小值为
$$
\boxed{
\inf\Gamma^2
=\langle\mathscr G_{x,J}^{\dagger}g_\perp,g_\perp\rangle .
}
\tag{6.2}
$$
证明：从直和头空间定义
$\mathscr A(\zeta)=\sum_{p=1}^J(\omega_{x,p}/\nu_{x,p})(C^*)^p\zeta_p$。
这里 $\zeta_p=\nu_{x,p}t_p/\omega_{x,p}$，与 (4.4) 的 $z_p$ 只差对角符号 $(-1)^p$，故范数相同。
其 $\mathscr A\mathscr A^*=\mathscr G_{x,J}$，
像为 $(\ker C)^\perp$，而求 (4.5) 正是同一个 $\mathscr A$ 的最小范数原像。
这里全部空间有限维，MP 的范围和核都已明确，不以环境逆替换真源逆。
达到最小值的同一 $t_p$ 可以在本强头全部 cut 之前固定。

若 $J\le2x$，由 $p!e_p(x)\le S_x^p$ 及 (3.4)，
$$
\mathscr G_{x,J}
\succeq\frac1{27J}
\sum_{p=1}^J\frac{(C^*)^pC^p}{p!S_x^p}.
\tag{6.3}
$$
这是一个合法的原正算子比较；它没有声称右端在
$(\ker C)^\perp$ 上具有一致谱隙。

## 7. 与原完整正能量的准确接点

取同一完整头 forcing $f$、$s\ge S_x$、$1\le J\le h-1$，令
$$
H_{C,J}(s)=I+\sum_{p=1}^J\frac{(C^*)^pC^p}{p!s^p},\qquad
a=H_{C,J}(s)^{-1}f,\qquad
E_p=\frac{\|C^pa\|^2}{p!s^p},\qquad
\mu_1=\sum_{p=1}^JpE_p .
$$
原全空间正规方程准确给
$$
f-a=\sum_{p=1}^J(C^*)^pt_p,\qquad
t_p=\frac{C^pa}{p!s^p}.
\tag{7.1}
$$
不能将这一未压缩身份免费移到未知 $F_0$。

代入真实 (4.5)，得到
$$
\Gamma^2
=\sum_{p=1}^J
\frac{p!e_p(x)}{s^p}\frac{E_p}{\omega_{x,p}^2}
\le\sum_{p=1}^Jp(1+p/x)^3E_p.
$$
因此
$$
\boxed{
\Gamma^2\le(1+J/x)^3\mu_1\le27\mu_1
\qquad(J\le2x).
}
\tag{7.2}
$$
这支付了同一个完整源 $f-a$ 的全部幂行，不付任何新的 $C^*$ 环境逆。

对应的原正高度物理相干列为
$$
F_{x,s}^{+}
=\sum_{p=1}^J\frac{(-C)^pa\otimes(D_x^*)^p\Omega}{p!s^p}
=\mathcal B_x^*z
$

其中 $z$ 与 (4.4)、(7.1) 完全同一。因此对几何增长的合法起点，
$$
\boxed{
\left\|\sum_\ell F_{x_\ell,s_\ell}^{+}\right\|^2
\le27\mathcal B_\lambda\sum_\ell\mu_{1,\ell}
}
\tag{7.3}
$$
先对有限族成立；右端有限时得到整个物理级数的收敛。
这比将各固定正高度的 Bessel 界形式相加保留了更多交叉信息。

对全高度 $J=h-1$，可在 $s\in[S_x,2S_x]$ 中只选一次方差：
由原 $dq/d\log s=\mu_1$，
$$
\mu_1(s)\le
\frac{q(2S_x)-q(S_x)}{\log2}.
\tag{7.4}
$$
沿已付指数强前缀，这个右端趋零。可在一个子列上令其可和；
同一次选择仍对所有合法 $Q$、全部 cut 和 partial 使用，不随它们再变。
这只说明 (7.2)--(7.3) 的实际来源范围，不把 $f-a$ 当成具有非零锚的 $f$。
对于 $w\in\ker T$，已有 $a\to P_{\ker T}f$ 恰使
$\langle w,f-a\rangle\to0$。

最后，(6.2) 中若改回真正有锚的 $g_\ell$，仍须实际估计该同一完整最优费用。
本稿没有把 (7.2) 对 $f-a$ 的界转给 $f$、
$a-P_{\ker C}f$、核外第二 Green 来源或真 $F_0$ 残余。
