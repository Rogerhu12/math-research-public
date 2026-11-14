# R382：原中央第三聚合、第二高轴修正与全矩阵第三精度

日期：2026-11-14。**状态：已证明。** 对当前 $j=0$ 原来源，完整中央导数模 $p^4$ 只剩前三个真实权。第六权的粗 Gauss 界不足以单独略去，本篇支付其准确的最坏一层分母；所有第七权以后的尾则由原完整界处理。同时用原确定系数给 R380 的剩余高轴一个显式修正，得到整个原三块矩阵逐项模 $p^3$ 的有理模型。该高轴修正不改变原 $d_2$，却在第三中央聚合中留下一个必须保留的指定配对。

## 1. 同一原来源、规范及记号

取原惰性好位
$$
p=6s-1>83,\qquad b=17,
\qquad S=\rho\,{a(t)\over7b}=z^6+\cdots,
$$
$$
t=-b/x^3,\qquad w=z^6,\qquad
a(t)=t(t-1)(16t^2+4t+7),\qquad
\rho=\Theta^{17}(1+8t).
$$
沿 R334、R338、R342 取同一个已付 Gaussian
$$
g=e^{-\kappa w^s}\rho,\qquad
a_p=p\kappa\in\mathcal O^\times,\qquad
\widehat S=g\,{a(t)\over7b}.
\tag{1}
$$
下文 $a_p$ 是实际径向常数，$a(t)$ 是角多项式。
定义
$$
c_h=[w^{hs}]\widehat S .
\tag{2}
$$
这些是原 regularized 来源的真实系数，没有分别赋予它们中央零。

R301 的完整插值函数在这一规范下为
$$
J_S(u)=\sum_{h\ge0}\kappa^{-h}c_h(u)_h,\qquad c_0=0,
$$
所以
$$
\boxed{
J_S'(0)=\sum_{h\ge1}(-1)^{h-1}(h-1)!
                       {p^h\over a_p^h}c_h .
}
\tag{3}
$$
R342 的合法 Gaussian 整重标通过完整正整数权及尾界支付；
因原质量为零，中央导数保持不变。
下文始终同时使用对应的 $g,a_p$，不只改变其中一个。
合法整重标也保留 R301 的 Gauss 界：在其 $R=p^{-1/(2p)}$ 圆盘上，
$\Delta z^{p+1}$ 的加权赋值至少 $(p+1)/(2p)>1/(p-1)$，
故相应指数与逆的范数均为一。

## 2. 第六权的实际分母

记原固定几何级数
$$
h(t)=\sum_{n\ge0}h_nt^n,\qquad
h_n={(1/2)_n\over n!(6n+1)},\qquad
w=(-t/b)h(t)^6 .
\tag{4}
$$

**引理1。** 对所有 $0\le n\le p$，$h_n\in\mathcal O$。
因此 $w(t)$ 与其逆 $t(w)$ 在至 $w^{p+1}$ 的对应窗口整，首项分别为 $-t/b$ 与 $-bw$。

**证明。** 当 $n<p$ 时，$n!$ 为单位；
$(1/2)_n$ 恰在 $n\ge3s=(p+1)/2$ 时包含一因子 $p$。
在 $0\le n\le p$ 中，$6n+1$ 被 $p$ 整除的唯一位置是
$$
n=5s-1,\qquad6n+1=5p .
$$
此处前述分子的一因子 $p$ 准确抵消。
当 $n=p$ 时，$n!$ 与 $(1/2)_n$ 各含一个 $p$，
而 $6p+1$ 为单位。所列范围没有 $p^2$ 因子。
于是全部 $h_n$ 整至 $n=p$；由于 (4) 还带一个首因子 $t$，
$w(t)$ 因而整至 $t^{p+1}$。它的首系数是 $-1/b$，
其逆由逐次代入递推亦整至 $w^{p+1}$。
$\square$

原对数系数为
$$
\log\Theta^{17}=\sum_{j\ge1}\ell_jt^j,\qquad
\ell_j={17\over3j}{(1/3)_j\over(5/6)_j}.
\tag{5}
$$
在 $1\le j\le p$ 内，分子 $(1/3)_j$ 从 $j=4s$ 起恰含一个 $p$；
分母 $(5/6)_j$ 从 $j=s$ 起恰含一个 $p$；
额外的 $j$ 仅在 $j=p$ 时再给一个 $p$。
因此
$$
\boxed{
v_p(\ell_j)
=\mathbf1_{j\ge4s}-\mathbf1_{j\ge s}-\mathbf1_{j=p}
\ge-1 .
}
\tag{6}
$$
所有固定坏素数按原约定排除。

**引理2。**
$$
\boxed{
c_h\in\mathcal O\quad(1\le h\le5),
\qquad c_6\in p^{-1}\mathcal O .
}
\tag{7}
$$

**证明。** R324、R334 已付原 $g$ 在 $w^p$ 之前整，
故 $\widehat S$ 也在该窗整；$hs<p$ 对 $h\le5$ 成立。

为了处理 $6s=p+1$，只需控制 $g$ 的第 $p$ 项：
引理1已付到 $w^{p+1}$，故角因子 $a(t)/(7b)=w+\cdots$
在这个完整窗口整且常数为零。
由 (4)–(6)，
$$
\log g=\log(1+8t(w))+\sum_{j\ge1}\ell_jt(w)^j-\kappa w^s
$$
的至 $w^p$ 系数赋值都至少 $-1$。
其低于 $w^p$ 的项事实上整，因为 $g$ 在该窗整且相应有限对数分母小于 $p$。
展开指数时，若使用唯一可能带 $p^{-1}$ 的第 $p$ 项，就不能再加入正次项
以影响第 $p$ 项；其余贡献仅由低阶整对数组成，阶乘最多含一个 $p$。
所以 $[w^p]g\in p^{-1}\mathcal O$。
乘回首阶一的原角因子得到 $c_6\in p^{-1}\mathcal O$。
$\square$

这里没有把粗 Gauss 下界三改作一个无证的整性断言；
真正用到的是第六权至多一个 $p$ 分母。

## 3. 完整中央第三聚合

R301 给全部原 Newton 系数的统一界
$$
v_p(\kappa^{-h}c_h)\ge
\left\lceil{h(p-1)+6\over2p}\right\rceil .
\tag{8}
$$
当 $h\ge7$ 时右边至少四，且随 $h$ 不减；
乘 $(h-1)!$ 只会增加赋值。
原已付收敛保证所有这些项的整个和属于 $p^4\mathcal O$。

对 $h=4,5$，(7) 分别给至少 $p^4,p^5$；
对 $h=6$，(7) 给
$$
\kappa^{-6}c_6\in p^5\mathcal O .
$$
因此 (3) 的全部尾已逐段支付。

**定理1。**
$$
\boxed{
J_S'(0)\equiv
{p\over a_p}c_1-{p^2\over a_p^2}c_2
+{2p^3\over a_p^3}c_3
\pmod{p^4}.
}
\tag{9}
$$
特别，原完整中央失败严格迫
$$
\boxed{
a_p^2c_1-pa_pc_2+2p^2c_3\equiv0\pmod{p^3}.
}
\tag{10}
$$

若已经使用 R334 的第二聚合
$a_pc_1-pc_2\in p^2\mathcal O$，则 (10) 也可准确写为
$$
\boxed{
\overline{{a_pc_1-pc_2\over p^2}}
=-{2\bar c_3\over\bar a_p}.
}
\tag{11}
$$
这是一个新的整商等式；并非令 $c_1,c_2,c_3$ 或其逐次商分别为零。
(9) 也给充分证书：若左侧显示的三项聚合赋值小于四，则原
$J_S'(0)\ne0$。这里没有声称此证书已对无穷多个 $p$ 命中。

## 4. 同一原高轴的完整线性与二次项

沿 R338 写同一实际分解
$$
g=g_<\exp(w^sH),\qquad
g_<=\exp([\log g]_{<s}),\qquad
\widehat S_<=g_<\,{a(t)\over7b}.
\tag{12}
$$
令
$$
c_{j,<}=[w^{js}]\widehat S_< .
$$
原点质量 $\widehat S_<(0)=0$ 使指数展开准确给
$$
\boxed{\begin{aligned}
c_1&=c_{1,<},\\
c_2&=c_{2,<}+[w^s](H\widehat S_<),\\
c_3&=c_{3,<}+[w^{2s}](H\widehat S_<)
                 +\frac12[w^s](H^2\widehat S_<).
\end{aligned}}
\tag{13}
$$
这里为得到 (10)，第二式需保模 $p^2$，第三式需保模 $p$。
$H$ 在这些窗口整，所用次数均低于 $p$。
没有将第三式的二次项删除，也没有把其两个线性读数视作同一个自由参数。

所以完整失败还准确给
$$
\boxed{\begin{aligned}
0\equiv\;&a_p^2c_{1,<}-pa_pc_{2,<}+2p^2c_{3,<}\\
&-pa_p[w^s](H\widehat S_<)
 +2p^2[w^{2s}](H\widehat S_<)
 +p^2[w^s](H^2\widehat S_<)
\pmod{p^3}.
\end{aligned}}
\tag{14}
$$
$H$ 仍由 R338 的原 $\ell_j,h(t)$、真实 $d_p$ 和固定 Miller forcing 确定。
(14) 是该同一高轴的新一层聚合，不增加一条独立 theta 来源。

## 5. R380 之后剩余高轴的确定修正

用 R377 的 $g^{[2]}=g_\kappa^{[2]}$，及 R380 的确切
$$
A_0(t)\in t\mathcal O[t]_{<s},\qquad
g^\star=g^{[2]}(1+p^2A_0(t)).
$$
R369 的实际 finite theta 比较给一个强于纯三块约化的事实：
$$
g^{[2]}\equiv g\pmod{p,w^{5s-1}}.
\tag{15}
$$
R377 增加的 $p\widetilde H_1$ 和准确常数不改变 (15)；
R380 的修正也不改变它。

原高窗对数完全可由已知有限有理式给出：
$$
\boxed{\begin{aligned}
\mathcal L^\kappa_{<2s}(t)=\bigg[
&\log(1+8t)+\sum_{j=1}^{2s-1}\ell_jt^j\\
&-\kappa(-t/b)^s h(t)^{p+1}
\bigg]_{<2s}.
\end{aligned}}
\tag{16}
$$
它属于 $t\mathcal O[t]/t^{2s}$。
整性可由 R334 的真实首分母相消直接读出：
对 $0\le n<s$，
$\ell_{s+n}/\ell_s\equiv h_n\bmod p$，
$p\ell_s$ 与 $p\kappa(-1/b)^s$ 相同模 $p$，
而 $h^{p+1}\equiv h\bmod(p,t^s)$。
因此 (16) 显示的所有 $p^{-1}$ 项准确消去。

置
$$
\boxed{
B_1(t)={1\over pt^s}
 \left[\mathcal L^\kappa_{<2s}(t)-\log g^\star(t)\right]_{[s,2s)}
\in\mathcal O[t]_{<s}.
}
\tag{17}
$$
(15) 保证分子这段系数被 $p$ 整除。
低于 $s$ 的差已由 $A_0$ 付至 $p^3$；
它不混入 (17) 的指定高段。

定义
$$
\boxed{
g^{[3]}=
g^{[2]}\{1+p^2A_0(t)+pt^sB_1(t)\}.
}
\tag{18}
$$
也可将两个括号相乘；差从 $p^3t^s$ 起，
在原三块中属于 $p^4\Gamma_T$。

**定理2。**
$$
\boxed{
g^{[3]}\equiv g\pmod{p^3\Gamma_T},\qquad T\le3s.
}
\tag{19}
$$

**证明。** 通过 (3) 的整单位换元，在普通系数中需要且只需要：
$$
\begin{array}{c|c}
\text{物理次数}&\text{所需精度}\\ \hline
0\le r<s&p^3\\
s\le r<2s&p^2\\
2s\le r<3s&p
\end{array}
\tag{20}
$$
第一行由 $A_0$ 保证。
第二行由 (17) 保证；在该段，$\log(1+pt^sB_1)$
准确只贡献 $pt^sB_1$，其二次项从 $t^{2s}$ 起。
第三行由 (15) 保证，而 (18) 的两个修正都被 $p$ 整除。
这正是 (19)，全部换元只向较高物理次数移动，不破坏表中精度。
$\square$

$B_1$ 不是自由高轴：它由原 (16) 和已经指定的有理模型唯一确定模 $p$。
另一方面，新增的修正
$$
pt^sB_1=p^2\epsilon\,(t/w)^sB_1
$$
在原首核上由 R380 的目标 Euler 身份消去。
所以它虽然使整个矩阵的系数更精确，却不改变 R380 已经正确识别的原 $d_2$。

## 6. 第三精度的坐标、Gaussian 与物理矩阵

为同步物理 Gaussian，继续使用 R377 的
$$
\widetilde Z_2=\widetilde Z+p\widetilde Z_1 .
$$
令
$$
W(t)=(-t/b)h(t)^6 .
$$
$W/\widetilde Z_2^6$ 在 $t=0$ 是单位，
其低窗属于 $1+p^2\mathcal O[[t]]$。
定义另一个完全确定的整多项式
$$
\boxed{
C_0(t)={1\over6p^2}
 \left[{W(t)\over\widetilde Z_2(t)^6}-1\right]_{<s}
\in\mathcal O[t]_{<s},
}
\tag{21}
$$
并置
$$
\boxed{
\widetilde Z_3=\widetilde Z_2(1+p^2C_0(t)),
\qquad \epsilon^{[3]}={\widetilde Z_3^{\,p+1}\over p}.
}
\tag{22}
$$
这里 $C_0(0)$ 一般非零；它准确补原线性坐标的第三位。
没有重新把旧首系数当作一。

由 (21) 的六次根展开及 R377 的全短窗整性，
$$
{\widetilde Z_3\over z}-1
\in p^3\mathcal O[[w]]+p^2w^s\mathcal O[[w]]
\quad\text{于所需窗口}.
$$
于是
$$
\boxed{
\epsilon^{[3]}\equiv\epsilon\pmod{p^3\Gamma_T}.
}
\tag{23}
$$
乘 $\epsilon$ 时使用的是同一个整除幂代数，
不将显示的 $1/p$ 另作一次免费除法。

整个原 canonical 列可准确取
$$
\boxed{
\mathcal S_{a,j}^{[3]}
=\left({g^{[3]}\over1+8t}\right)^N
 F_{a,j}(t)e_2(Na_p\epsilon^{[3]}),\qquad N=a+40 .
}
\tag{24}
$$
原角多项式 $F_{a,j}$ 含全部 $P_{134}$。
由 (19)、(23)，(24) 的矩阵逐项满足
$$
\boxed{M^{[3]}\equiv M^{\rm orig}\pmod{p^3}.}
\tag{25}
$$
它使用相同的来源、长度和目标基，保留 $U_0/G_0$、十三行及所有高尾。
(25) 加强的是矩阵代表精度，不是多了一组中央零。

如需整个矩阵的有理 Serre 代表，可在
$\widetilde Z_3=\widetilde Z(1+pA+p^2C_0)\bmod p^3$，
$A=\widetilde Z_1/\widetilde Z$ 下有限展开。
记 $d_r=6r+1$，准确取
$$
\boxed{\begin{aligned}
\Lambda_\lambda^{[3]}
=\sum_r\lambda_rp^{\lfloor r/s\rfloor}\widetilde Z^{-d_r}
\bigg\{&
D\widetilde Z
+p(D\widetilde Z_1-d_rA\,D\widetilde Z)\\
+p^2\big(&D(\widetilde ZC_0)-d_rA\,D\widetilde Z_1\\
&+[d_r(d_r+1)A^2/2-d_rC_0]D\widetilde Z\big)
\bigg\}dz .
\end{aligned}}
\tag{26}
$$
它仍是原 $w$ 对偶拉回后除以六的规范。
所有略项给 $p^3$ 倍整行变换；
原权 $p^{\lfloor r/s\rfloor}$ 保留了与来源系数分母的准确抵消。
(26) 不倒置 $1+pA+p^2C_0$，所以没有加它的零点作为新测试极。

新项只可能增加旧 $x=0$ 固定边界的极阶。
$A_0,C_0$ 都伴 $p^2$，可支付 Gaussian 至多 $p^{-2}$ 的分母。
$pt^sB_1$ 仅伴一个 $p$，但其 $t$ 次数小于 $2s$：
在 $x=0$，Gaussian 第二项使总零阶至少
$34N+2(p+1)-3(2s-1)>p+1$，
故能读到它的真实行必有 $r\ge s$，
其原对偶权再给一个 $p$。
因此这部分也整。
其余测试点与 R377 相同；三个二挠点的共同残数由全局和及 $3\in\mathcal O^\times$ 支付。
所有固定边界仍保留。

## 7. 同一模型准确读取三个中央系数

令
$$
\widehat S^{[3]}=g^{[3]}\,{a(t)\over7b},
\qquad c_j^{[3]}=[w^{js}]\widehat S^{[3]} .
$$
因为原角因子从 $w$ 起，表 (20) 准确给
$$
\boxed{
c_1^{[3]}\equiv c_1\pmod{p^3},\qquad
c_2^{[3]}\equiv c_2\pmod{p^2},\qquad
c_3^{[3]}\equiv c_3\pmod p .
}
\tag{27}
$$
第三式读取径向系数最多到 $w^{3s-1}$；
所以没有把第 $3s$ 行悄悄加入原 $C_2$ 的三块目标。
这是固定原 $S$ 首阶一所支付的明确边界，而非删除新末行。

设
$$
\widehat S^{[2]}=g^{[2]}\,{a(t)\over7b},\qquad
c_j^{[2]}=[w^{js}]\widehat S^{[2]},\qquad
\eta(t(w))=(t(w)/w)^s .
$$
从 (18) 逐项提取得
$$
\boxed{\begin{aligned}
&a_p^2c_1-pa_pc_2+2p^2c_3\\
&\quad\equiv
a_p^2c_1^{[2]}-pa_pc_2^{[2]}+2p^2c_3^{[2]}\\
&\qquad\quad+
p^2\left\{
 a_p^2[w^s](A_0\widehat S^{[2]})
-a_p[w^s](\eta B_1\widehat S^{[2]})
\right\}
\pmod{p^3}.
\end{aligned}}
\tag{28}
$$
括号中的两项只需约化模 $p$。
$A_0$ 的正是 R380 已进入原 $d_2$ 的确定低轴；
$B_1$ 的目标修正在原首核上消失，却仍被这一原中央聚合读取。
因此不能把后一个配对删掉，再将中央失败称为所有 $d_2$ 配对为零。

(28) 把这一区别落在两个完全指定的有限有理式上。
没有额外提升参数；若进一步要把中央条件传播到原核，
现在须使用 (16)、(17) 的实际关系控制这个 $B_1$ 配对。

## 8. 原中央及 d₂ 的全局边界仍须聚合

R380 已在同一 $P_2,\lambda_2$ 上给真正 $d_2$ 的有理残数公式；
(24)–(26) 现在也给逐项第三精度的代表。
原点残数除以 $p^2$ 以前，仍先使用真正 $K_2$ 条件保证整除；
全局上仍须把原全部非原点测试点、二挠点和 $x=0$ 点相加。

对于 (9)，可独立使用
$$
{p\over a_p}\operatorname{Res}_O
 {\widehat S^{[3]}\,dz\over z^{p+2}}
-{p^2\over a_p^2}\operatorname{Res}_O
 {\widehat S^{[3]}\,dz\over z^{2p+3}}
+{2p^3\over a_p^3}\operatorname{Res}_O
 {\widehat S^{[3]}\,dz\over z^{3p+4}},
\tag{29}
$$
其值模 $p^4$ 恰为 $J_S'(0)$。
要将 (29) 写成全局有理微分，按 (21)、(22) 换为
$\widetilde Z_3$，并按 (26) 有限展开。
第一个残数需坐标至模 $p^3$、第二个至模 $p^2$、
第三个至模 $p$；原系数行及 (27) 正好支付这些精度。
第一项中仍可能存在的 $p^2w^s$ 坐标误差乘原首阶 $w$ 后超出所读行，
这再次使用原 $S(0)=0$，没有免费提高整张坐标矩阵的精度。
全部固定边界和补项都保留，不把这三个残数分开置零。

由此，原完整中央第三聚合和原 $d_2$ 已使用同一个确定模型，
但它们仍是两个不同的指定配对。
本篇没有从它们共享模型就推断零传播，
也没有把 R366/R369 的局部单位子式代替这个共同整来源比较。

## 依赖与同步

- R301、R324、R334：完整 Newton 尾、原整性窗及 $\ell_j,h_j$ 的确切公式。
- R338、R342：同一高轴、完整中央聚合和合法 Gaussian 重标。
- R369、R377：强普通系数窗口、整个 theta 第一提升、真实坐标及固定边界。
- [R380](R380-original-low-axis-correction-and-full-second-bockstein-model.md)：
  确定 $A_0$、真正 $K_3/d_2$ 及同 $P_2,\lambda_2$ 配对。

本篇为全参数证明，没有目标素数扫描。
通过已授权 GitHub API 保存；核心登记与 HANDOFF 由根代理维护。
