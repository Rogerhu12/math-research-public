# R271 附录：原光滑核闭包内的全部幂稠密值域

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 状态：下面是原边界光滑核闭包上的准确稳定性；不识别该闭包与整个 $M$。

沿用[实际高位创建修复](R271-appendix-boundary-smooth-kernel-creation-repair-and-faithful-calkin-corners.md)：
$$
M=\ker T,\qquad N=\overline{BM},\qquad
K_\infty=\overline{M\cap\mathscr E_\infty}\subset N\subset M,
\qquad T=T_N\ \hbox{或完整 }T_Y.
\tag{1}
$$
固定的同一实际右逆为 $\mathcal G$。
对每个 $u\in M\cap\mathscr E_\infty$，该稿已经付清
$$
k_j(u)=E_j^*u-\mathcal G[T,E_j^*]u\in M\cap\mathscr E_\infty,
$$
$$
\|\mathcal G[T,E_j^*]u\|
\le C_*\delta_{j,\lambda_*}\|u\|_{\lambda_*},
\qquad
\sum_{j\ge1}\delta_{j,\lambda_*}<\infty.
\tag{2}
$$
以下只继续使用这些同源真核向量，不换纯尾或未付原像。

## 1. 全部固定幂的原像就在同一个光滑核内

**定理 1。** 对每个整数 $r\ge1$，
$$
\boxed{\overline{B^rK_\infty}=K_\infty.}
\tag{3}
$$
更精确地，每个光滑 $u\in M$ 有下面明确的光滑核原像序列。

原进位身份给
$$
\mathsf N_j=B^{2^j}/d_j
=E_j+\eta_jE_j^*\mathsf N_{j+1},
\qquad
\mathsf N_jE_j^*=E_jE_j^*=P_j^0,\qquad
\|\mathsf N_j\|=1.
\tag{4}
$$
第二个等式是准确的，因为高尾 $\mathsf N_{j+1}$ 与 $E_j^*$ 交换，
且 $(E_j^*)^2=0$。
选择 $j$ 使 $2^j\ge r$，定义
$$
v_{j,r}(u)=d_j^{-1}B^{\,2^j-r}k_j(u).
\tag{5}
$$
$B$ 保 $\mathscr E_\infty$ 并与 $T$ 交换，所以
$$
v_{j,r}(u)\in M\cap\mathscr E_\infty.
$$
每个 $j$ 的 $d_j$ 是实际非零标量；未声称这些原像范数一致有界。

由 (2)--(5)，
$$
B^rv_{j,r}(u)
=\mathsf N_jk_j(u)
=P_j^0u-\mathsf N_j\mathcal G[T,E_j^*]u.
\tag{6}
$$
因此同一实际输出误差满足
$$
\boxed{
\|B^rv_{j,r}(u)-u\|
\le
\|E_j u\|
+C_*\delta_{j,\lambda_*}\|u\|_{\lambda_*}
\longrightarrow0.
}
\tag{7}
$$
这里 $E_j\to0$ 强，且第二项由已付同源创建费用趋零。

这先给每个光滑核向量都在 $\overline{B^rK_\infty}$ 内。
它们在 $K_\infty$ 稠密；反向包含来自 $K_\infty$ 的 $B$ 不变性。
故 (3) 成立。

还可保留一个实际可和性：
$$
\sum_j\|E_ju\|^2
=\sum_{p\ge0}p\|\mathsf P_pu\|^2<\infty
\qquad (u\in\mathscr E_\infty).
$$
结合 (2)，对每个固定 $r$，(7) 的输出误差平方可和。
这是同一个 $u$ 的输出界，不是对 (5) 的原像范数界。

旧结论 $M\cap\mathscr E_\infty\subset N$ 只把原像放在整个 $M$ 的稳定像闭包里。
(5)--(7) 现在把所有固定幂的原像放回同一个光滑核本身，
因此给出 (3) 这个更强的闭子空间内部结论。

## 2. 非零解析芽在该实际限制上的范围和核

原 $B$ 拟幂零，且
$$
\ker B^r=\operatorname{span}\{e_0,\ldots,e_{r-1}\}.
$$
原 $T_N,T_Y$ 在有限整数支撑上均严格下降，
其第一下降系数在每一列都非零：
它来自 $a_0\mathsf N_0$，而其它项或完整 Cayley 的更高幂下降更多整数位置。
故最高非零整数坐标的三角回代给
$$
M\cap\ker B^r=\mathbb C e_0\qquad(r\ge1).
\tag{8}
$$
特别 $B|_{K_\infty}$ 有一维核，但 (3) 给它的值域稠密；
不能把它称作单射拟亲和。

取零点附近非恒定的解析芽 $f$，写
$$
f(z)-f(0)=z^r g(z),\qquad r\ge1,\qquad g(0)\ne0.
$$
在实际 $B$ 上，$g(B)$ 及其逆都由范数收敛幂级数给出，
并保持闭 $B$ 不变空间 $K_\infty$。
由 (3) 和 (8)，
$$
\boxed{
\overline{(f(B)-f(0)I)K_\infty}=K_\infty,
\qquad
\ker\big((f(B)-f(0)I)|_{K_\infty}\big)=\mathbb C e_0.
}
\tag{9}
$$
最后核等式用到了 $g(B)e_0=g(0)e_0$。
这里只处理具有正收敛半径的解析芽；
原慢符号 $T$ 的形式 $B$ 级数不属于这项额外假设，
不能把 $T|_{K_\infty}=0$ 与 (9) 混淆。

## 3. 对主问题的准确位置

(3) 说明 $K_\infty$ 已是一个真实的 $B$ 稠值稳定子空间，并且
$$
K_\infty\subset\bigcap_{r\ge1}\overline{B^rM}\subset N.
\tag{10}
$$
没有从 (10) 得到反向包含。
尤其 (3) 不说明 $B$ 在每个未知闭 $B$ 不变子空间上都有稠密值域；
$\mathbb Ce_0$ 本身就是不能作这种外推的实际子空间。

结合前稿的准确伴随来源身份，
$$
D(\mathcal G^*)\cap K_\infty^\perp=\operatorname{Ran}T^*,
\qquad
\overline{K_\infty^\perp\cap\mathscr E_\infty}=M^\perp,
$$
剩余问题仍是原 $M$ 中光滑核闭包以外的来源，
或者直接证明当前 $N=M$。
本稿没有给未知 $P_{K_\infty}$ 的正指数域保持、
真实 $W$ 的 $\Gamma$ 上界或原 Hilbert 核的光滑密度。
