# 正源锚解析平滑的首系数正性与零字符障碍

日期：2026-11-12（UTC）。作者：literature。

状态：完整实际正性障碍，不编号。
本稿排除一种把慢符号送入 R199 正逆类的方案，
不构造原 Haar 不变子空间，也不否定慢符号的普遍限制稠密像。

这里“增生”始终指 Hilbert 二次型
$\operatorname{Re}\langle Tx,x\rangle\ge0$，
不指 Banach 格的正算子。

## 1. 正锚与结论

取
$$
a_j\ge0,\qquad a\in\ell^2\setminus\ell^1,\qquad
X=X_a,\qquad Z=I+X,\qquad L=Z^{-1}.
\tag{1.1}
$$
$X$ 是在有限柱初始域上闭包得到的真实一阶。
R125、R128、R138 给：

- $X$ 最大增生且空谱；
- $L\in\{A\}'$ 有界、单射、稠密像、拟幂零，$\|L\|\le1$；
- 每个有限柱属于 $Z$ 及 $Z^*$ 的全部真实自然幂域。

令 $\mathfrak U$ 为原物理 UHF 代数。

**定理1.1（单侧解析式的首系数正性）。**
设 $B_n\in\mathfrak U$，并存在 $\rho>0$ 使
$$
\sum_{n\ge0}\|B_n\|\rho^n<\infty.
\tag{1.2}
$$
设第一个非零系数为 $B_k$，并令
$$
T=\sum_{n\ge k}B_nL^n.
\tag{1.3}
$$
若 $T$ 增生，则 $B_k$ 也增生。
不要求这些系数彼此交换或与 $L$ 交换。
结论也对固定有限放大上的
$B_n\in M_d(\mathfrak U)$、$L^{(d)}$ 成立。

**推论1.2。**
若 $0\ne B\in\mathcal A$ 且 $\chi(B)=0$，
$\phi$ 是任意非零标量解析芽，则
$$
\boxed{
e^{i\theta}B\phi(L)\text{ 对任何实数 }\theta\text{ 都不增生}.
}
\tag{1.4}
$$
特别包括 $\phi(0)\ne0$、$\phi(w)=w^k$ 以及任意有限正阶首项。
此结论适用于实际慢符号 $S_N$、$S_Y$。

## 2. 高位 Walsh 的正实中心与全部固定幂域

由于 $a\ge0$ 且不可和，可选有限集合
$$
J_\nu\subseteq\{\nu,\nu+1,\ldots\},
\qquad
\lambda_\nu:=2\sum_{j\in J_\nu}a_j\ge2\nu.
\tag{2.1}
$$
令
$$
U_\nu=M_{\chi_{J_\nu}}.
$$
它是自伴酉算子，且每个 $U_\nu$ 保持有限柱。
$\lambda_\nu$ 为正实数并趋于无穷；
后面的二次型缩放会明确使用这个符号。

对每个固定有限柱向量 $v$ 和固定整数 $p\ge0$，
R181 §§2–3 的真实乘积参考态中心幂估计给
$$
\boxed{
U_\nu v\in\operatorname{Dom}Z^p,\qquad
\|(Z-\lambda_\nu I)^pU_\nu v\|\le C_{p,v}
}
\tag{2.2}
$$
对充分大的 $\nu$ 成立，常数与 $J_\nu$ 的长度无关。

为说明这个引用的适用范围，设 $v$ 只依赖前 $m$ 位。
先把 $v$ 展开为这 $m$ 位物理标准基与尾真空的有限线性组合。
对每个基向量，$U_\nu$ 只把 $J_\nu$ 位的尾真空改成 Walsh 向量 $\chi$。
一位纯矩阵 $S_j=I-2E_j$ 在物理标准基向量上的期望为1，
在尾真空上的期望为0，在 $\chi$ 上的期望为2。
故该乘积参考态下的 $X$ 中心为
$$
\sum_{j<m}a_j+\lambda_\nu.
$$
R181 的常数只依赖幂次数、$\|a\|_2$ 及实际 carry 支撑预算，
不依赖改变参考态的位数。
把固定的 $1+\sum_{j<m}a_j$ 用二项式吸收，
再取有限线性组合，就得到 (2.2)。
这也付清每个向量的真实自然幂域，未把形式幂当作闭算子作用。

共同共轭 $C$ 满足 $Z^*=CZC$，
且 $CU_\nu C=(-1)^{|J_\nu|}U_\nu$。
因此同一结论适用于 $Z^*$。

在自然幂域内使用标量二项式，
由 (2.2) 对每个固定 $k$ 得
$$
\boxed{
\lambda_\nu^{-k}U_\nu Z^kU_\nu v\longrightarrow v
\quad(v\text{ 为有限柱}).
}
\tag{2.3}
$$
因为差就是
$$
\sum_{p=1}^k\binom kp\lambda_\nu^{-p}
U_\nu(Z-\lambda_\nu I)^pU_\nu v,
$$
每项趋于零。$k=0$ 时 (2.3) 是恒等式。
不声称这里出现的无界算子在整个 $H$ 上一致有界，
也不把这个有限柱结论搬到未知子商。

## 3. 同一个序列的真实 UHF 边界

所有 $J_\nu$ 的最小位趋于无穷，所以对每个 $B\in\mathfrak U$，
$$
U_\nu B U_\nu\longrightarrow B\quad\text{按范数}.
\tag{3.1}
$$
先用有限头 UHF 算子范数逼近 $B$，
再利用足够高的任意长度 Walsh 乘积与该有限头严格交换即可。

另一方面，由 (2.2) 的 $p=1$，
$$
ZU_\nu v=\lambda_\nu U_\nu v+r_{\nu,v},
\qquad \|r_{\nu,v}\|\le C_{1,v}.
$$
左乘真实有界逆 $L$，得到
$$
\lambda_\nu\|LU_\nu v\|
\le\|v\|+\|L\|C_{1,v}.
$$
通常伴随同理。因此
$$
LU_\nu\longrightarrow0,\qquad L^*U_\nu\longrightarrow0
\quad\text{于 SOT},
$$
先在有限柱上证明，再用统一有界的 $L,L^*$ 延到全空间。
于是
$$
\boxed{U_\nu L U_\nu\longrightarrow0\quad\text{强*}.}
\tag{3.2}
$$
这是 R194 的实际边界，不是把小范数扰动当作核连续性。

由于 $L$ 拟幂零，对每个 $\delta>0$ 有
$\|L^n\|\le C_\delta\delta^n$。
取 $\delta<\rho$，(1.2) 保证 (1.3) 与每个固定移位级数都绝对范数收敛。
定义
$$
\Psi_k=\sum_{n\ge k}B_nL^{n-k}.
\tag{3.3}
$$
从右侧统一提取 $L^k$，
$$
T=\Psi_kL^k.
\tag{3.4}
$$
这一步不需要系数与 $L$ 交换。

对每个有限和，(3.1)—(3.2) 给强*极限；
绝对范数收敛保证可以再取无穷和。因此
$$
\boxed{U_\nu\Psi_kU_\nu\longrightarrow B_k\quad\text{强*}.}
\tag{3.5}
$$
这里收敛是在全部 $H$ 上，且 $\|\Psi_k\|$ 固定有限。

## 4. 二次型测试证明首系数结论

假设 $T$ 增生，固定有限柱 $v$。
令
$$
x_\nu=Z^kU_\nu v\in H.
$$
这些向量由 (2.2) 的真实自然幂域定义。
$L^kZ^kU_\nu v=U_\nu v$，故 (3.4) 给准确等式
$$
Tx_\nu=\Psi_kU_\nu v.
\tag{4.1}
$$
由于 $\lambda_\nu^k>0$，
$$
0\le
\lambda_\nu^{-k}\operatorname{Re}\langle Tx_\nu,x_\nu\rangle
=
\operatorname{Re}\left\langle
U_\nu\Psi_kU_\nu v,\,
\lambda_\nu^{-k}U_\nu Z^kU_\nu v
\right\rangle.
$$
由 (2.3)、(3.5)，右边趋于
$\operatorname{Re}\langle B_kv,v\rangle$。
所以该值非负。有限柱稠密且 $B_k$ 有界，得到
$\operatorname{Re}B_k\ge0$。

同一个证明逐坐标作用于有限放大；
测试向量取有限柱向量的有限列即可。
这证明定理1.1。

## 5. 字符为零的非零 Acal 符号的排除

对推论1.2，写
$$
\phi(w)=w^k\psi(w),\qquad c=\psi(0)\ne0.
$$
标量解析芽在拟幂零 $L$ 上范数收敛，
故定理1.1 使
$$
e^{i\theta}B\phi(L)\text{ 增生}
\quad\Longrightarrow\quad
\operatorname{Re}(e^{i\theta}cB)\ge0.
\tag{5.1}
$$

物理 UHF 有忠实乘积迹 $\tau$。
真实圆群 gauge 给
$$
\tau(F)=\chi(F)\qquad(F\in\mathcal A),
$$
先对 $A$ 多项式成立，再按范数延伸。
所以 $\chi(B)=0$ 使
$$
\tau(\operatorname{Re}(e^{i\theta}cB))=0.
$$
正性与迹的忠实性迫实部为零。
此时 $e^{i\theta}cB$ 为斜自伴，因而正规；
又因 $\chi(B)=0$，它拟幂零。
正规拟幂零算子只能为零，与 $B\ne0$ 矛盾。
这证明 (1.4)。

有限矩阵也有对应结论：
若定理1.1 的所有 $B_n$ 属于 $M_d(\mathcal A)$，
且每个条目的字符均为0，则任何非零这种解析式都不增生。
确实，首项 $B_k$ 的正实部在忠实矩阵乘积迹下迹为0，
故 $B_k$ 斜自伴。
另一方面，对 $\lambda\ne0$，
$\det(\lambda I-B_k)$ 在 $\mathcal A$ 的唯一字符下取值 $\lambda^d\ne0$，
因此是单位；伴随矩阵公式给 $\lambda I-B_k$ 可逆。
所以 $B_k$ 拟幂零，进而 $B_k=0$，矛盾。

## 6. 这条障碍具体排除什么

对原慢符号 $S_N$ 或 $S_Y$，
不能通过乘一个单正锚的非零标量解析因子 $\phi(L)$，
再旋转一个常数相位，把所得算子送入
$$
\operatorname{Re}T\ge\varepsilon T^*T\qquad(\varepsilon>0)
$$
这类 R199 正逆条件；该条件首先就要求增生。

这是全空间中一个可验证的正性障碍。
它不否定其他形式的强主理想逼近，
不判定一般非解析平滑因子，
也不排除含 $L^*$ 的非解析正表达式，例如 $L^*L$。
未知不变子商通常没有非零有限柱向量，
所以本稿的有限柱二次型测试不能直接宣称为所有子商上的同一必要条件。

内部来源：R125/R128/R138 的真实正一阶与有界逆，
R181 §§2–3 的乘积参考态中心幂界，
R194 的 UHF 边界；本稿第4节写全新增的首系数正性推理。


## 7. 有限个最终不交的正源锚

本节将结论扩大到有限个锚，同时明确能独立调节中心的假设。
取 $d\ge1$ 个非负行
$$
a^{(i)}\in\ell^2\setminus\ell^1,\qquad a^{(i)}_j\ge0,
\qquad 1\le i\le d.
$$
要求存在有限 $m_*$，使
$$
\operatorname{supp}a^{(i)}\cap[m_*,\infty)
\quad(1\le i\le d)
\quad\text{两两不交}.
\tag{7.1}
$$
令
$$
Z_i=I+X_{a^{(i)}},\qquad L_i=Z_i^{-1}.
\tag{7.2}
$$
全部 $L_i\in\mathfrak C=\{A\}'$ 有界、拟幂零，并两两交换。

固定正权向量 $r=(r_1,\ldots,r_d)$。
对趋于无穷的实参数 $t$，先选整数 $m(t)\to\infty$，
且 $m(t)\ge m_*$。
在第 $i$ 行自己的高尾上逐项累加到首次达到 $t^{r_i}/2$，
得到有限集合 $J_i(t)$，使
$$
\lambda_i(t):=2\sum_{j\in J_i(t)}a^{(i)}_j,
\qquad
t^{r_i}\le\lambda_i(t)
\le t^{r_i}+2\sup_{j\ge m(t)}a^{(i)}_j.
\tag{7.3}
$$
不可和性保证有限时刻达到目标；$\ell^2$ 性保证最后一个上跳量趋于0。
因此
$$
\lambda_i(t)=t^{r_i}+o(1),\qquad \lambda_i(t)>0.
\tag{7.4}
$$
没有把离散系数和误写为可以准确指定的任意实数。

这些集合两两不交，而且对 $k\ne i$，
$a^{(k)}_j=0$ 对全部 $j\in J_i(t)$ 成立。
置
$$
J(t)=\bigcup_iJ_i(t),\qquad U_t=M_{\chi_{J(t)}}.
\tag{7.5}
$$
这是同一个高位自伴酉序列，能同时实现全部独立的正实中心。
对每个 $B\in\mathfrak U$ 仍有
$$
\|U_tBU_t-B\|\longrightarrow0.
\tag{7.6}
$$
这里没有把若干先后强极限乘到移动向量上。

有限条不同的 R204 树路径满足 (7.1)：
两条不同路径只共用有限个节点，每个节点使用有限个位；
对有限条路径，可把全部共同节点置入同一个有限头。
因此下述结论同时适用于这种有限树路径族。
不允许把有限族直接替换为任意可数族的多变量解析式。

## 8. 同一序列上的真实混合中心词

记
$$
R_i(t)=Z_i-\lambda_i(t)I.
$$
对任意固定有限柱向量 $v$ 和任意固定有限词
$(i_1,\ldots,i_\ell)$，有
$$
\boxed{
U_tv\in
\operatorname{Dom}\bigl(R_{i_1}(t)\cdots R_{i_\ell}(t)\bigr),
\qquad
\|R_{i_1}(t)\cdots R_{i_\ell}(t)U_tv\|
\le C_{\ell,v}.
}
\tag{8.1}
$$
常数只需对固定的有限行族与固定词长度统一，
不依赖 $t$ 或 $|J(t)|$。

证明如下。设 $v$ 依赖前 $m$ 位，并展开为物理标准基与尾真空的有限和。
在每个这样的乘积参考态中，前 $m$ 位的纯局部期望均为1，
$J(t)$ 上均为2，其余尾位均为0。
由 (7.1)，第 $i$ 行的纯期望准确为
$$
\beta_i(t)=\sum_{j<m}a^{(i)}_j+\lambda_i(t).
$$
对这个共同参考态使用同一个激发次数算子 $\Lambda_h$。
R181 §§2–3 的逐行估计给
$$
\|\Lambda_h^s
(X_{a^{(i)}}-\beta_i(t)I)y\|
\le D_s\|a^{(i)}\|_2\|\Lambda_h^{s+1}y\|,
\tag{8.2}
$$
其中 $D_s$ 不依赖参考态。
真实 carry 的每个局部支撑项在同一 $\Lambda_h$ 中支付，
所以这里对不同的行无需改换权空间。

把固定标量 $1+\sum_{j<m}a^{(i)}_j$ 加回 (8.2)，
仍得到
$R_i(t):\operatorname{Dom}\Lambda_h^{s+1}
\to\operatorname{Dom}\Lambda_h^s$
的统一有界估计。
从相对真空开始，依次用 $s=\ell-1,\ldots,0$，
便得到 (8.1) 对每个乘积基向量的结论；
有限线性组合给一般有限柱 $v$。

这些是实际自然域：
有限局部截断的估计在上述加权算子范数中收敛，
逐次利用每个闭第一阶与 $\Lambda_h^s$ 的闭性识别极限。
所有有限截断是交换的真实 $V_j$ 多项式，
所以在这些共同光滑向量上，有限混合词也可交换次序。
本节不声称不同无界算子的任意最大自然积域都相等。

还需记录有界逆的域保持。
由 R88，任意 $B\in\mathfrak C$ 可用 $A$ 多项式在 SOT 中逼近。
每个 $Z_i$ 的闭图对 $\operatorname{diag}(A,A)$ 不变；
将同一逼近作用于图上的两个固定坐标，
闭性给
$$
B\operatorname{Dom}Z_i\subseteq\operatorname{Dom}Z_i,
\qquad Z_iBx=BZ_ix.
\tag{8.3}
$$
对每个有限混合自然词重复此论证，$B$ 也保持相应域并交换。
特别所有 $L_i$ 都满足这一性质。

## 9. 多逆单项式的定量高位展开

在 $\operatorname{Dom}Z_i^2$ 上有精确等式
$$
\boxed{
L_ix=\lambda_i^{-1}x+
\lambda_i^{-2}\bigl(-R_i(t)+L_iR_i(t)^2\bigr)x.
}
\tag{9.1}
$$
这是将
$L_ix=\lambda_i^{-1}x-\lambda_i^{-1}L_iR_i(t)x$
再使用一次所得。
这里只需两步，不把无界的 Neumann 级数当作范数收敛级数。

令
$$
D_i(t)=-R_i(t)+L_iR_i(t)^2.
$$
由 (8.1)、(8.3)，任意固定混合 $D_i(t)$ 词在 $U_tv$ 上统一有界：
展开后，全部有界 $L_i$ 可移到左边，
剩下的只是至多两倍长度的真实混合 $R_i(t)$ 词。
因此对每个固定 $\alpha\in\mathbb N^d$，
将 (9.1) 在真实共同域内作有限乘积展开，得到
$$
\boxed{
\|L^\alpha U_tv-\lambda(t)^{-\alpha}U_tv\|
\le
C_{\alpha,v}\lambda(t)^{-\alpha}
\sum_{i=1}^d\lambda_i(t)^{-1}.
}
\tag{9.2}
$$
充分大 $t$ 时全部 $\lambda_i\ge1$；
每个非首项至少含一个额外的 $\lambda_i^{-1}$，
其余额外负幂可直接以1控制。
这说明 (9.2) 的常数不随 $t$ 增长。

由 (7.4)，特别有
$$
\boxed{
t^{r\cdot\alpha}U_tL^\alpha U_tv\longrightarrow v,
\qquad
\|L^\alpha U_tv\|=O(t^{-r\cdot\alpha}).
}
\tag{9.3}
$$
$\alpha=0$ 时两式分别是恒等式与固定范数界。
本节只在有限柱输入上断言带 $t$ 放大的极限；
没有借此声称放大后的全算子范数一致有界。

## 10. 多变量解析首系数的正性

设 $B_\alpha\in\mathfrak U$，且对某个正多圆盘半径
$\rho=(\rho_1,\ldots,\rho_d)$，
$$
\sum_{\alpha\in\mathbb N^d}
\|B_\alpha\|\rho^\alpha<\infty.
\tag{10.1}
$$
这是一个 $\mathfrak U$ 值收敛解析芽的系数条件；
任意给定正收敛半径都可稍微缩小到满足此绝对和的半径。
定义
$$
T=\sum_\alpha B_\alpha L^\alpha.
\tag{10.2}
$$
由于每个 $L_i$ 拟幂零，
该级数及任意固定多指数移位的级数都绝对范数收敛。
无需系数彼此交换或与 $L_i$ 交换。

假设某个正权向量 $r$ 使非零系数支持具有唯一最小元：
$$
w_0=r\cdot\alpha_0
<
r\cdot\alpha
\quad
(B_\alpha\ne0,\ \alpha\ne\alpha_0).
\tag{10.3}
$$
这样的权总能选到：取 $r_i>0$ 且在 $\mathbb Q$ 上线性无关。
全部不同整数多指数的权便不同，
而任意固定权上界内只有有限个非负整数多指数；
任一非空支持所以确有唯一最小元。

**定理10.1。**
若 $T$ 增生，则 $B_{\alpha_0}$ 增生。
这一结论对每个满足 (10.3) 的正权成立，
并保持固定有限矩阵放大。

为完整控制无穷尾，选整数 $K_i$ 使
$$
K_ir_i>w_0\qquad(1\le i\le d).
$$
把级数按第一个超出矩形的坐标分组：
$$
T=
\sum_{0\le\alpha_i<K_i}B_\alpha L^\alpha
+
\sum_{i=1}^dG_i(L)L_i^{K_i},
\tag{10.4}
$$
其中
$$
G_i(L)=
\sum_{\substack{\alpha_j<K_j\ (j<i)\\ \alpha_i\ge K_i}}
B_\alpha L^{\alpha-K_ie_i}.
$$
每个 $G_i(L)$ 都是固定的有界算子。
此分组只在右侧提出 $L_i^{K_i}$，
因此仍不要求 $B_\alpha$ 与逆坐标交换。

由 (9.3)，每个余项满足
$$
t^{w_0}\|G_i(L)L_i^{K_i}U_tv\|
\le C_{i,v}\|G_i(L)\|\,t^{w_0-K_ir_i}
\longrightarrow0.
\tag{10.5}
$$
这控制的是整个余项算子在测试向量上的范数，
不是只估其中单个级数项。

矩形内只有有限项。
(9.3)、(10.3) 使除 $\alpha_0$ 外的项在 $t^{w_0}$ 缩放后消失；
(7.6) 又使首项的 UHF 系数按范数固定。
所以
$$
\boxed{
t^{w_0}U_tTU_tv\longrightarrow B_{\alpha_0}v
\quad(v\text{ 为有限柱}).
}
\tag{10.6}
$$
$w_0=0$ 的常数首项同样包含在内。

若 $T$ 增生，$t^{w_0}>0$ 给
$$
0\le
t^{w_0}\operatorname{Re}\langle TU_tv,U_tv\rangle
\longrightarrow
\operatorname{Re}\langle B_{\alpha_0}v,v\rangle.
$$
由有限柱稠密得到定理。有限放大逐坐标使用同一序列和同一证明。

## 11. 多锚平滑仍不能送入零字符正类

由定理10.1 和第5节的忠实 UHF 迹论证：

**推论11.1。**
在 (7.1)—(7.2) 的最终不交正源锚条件下，
对任意
$$
0\ne B\in\mathcal A,\qquad\chi(B)=0,
$$
任意非零标量收敛芽 $f(w_1,\ldots,w_d)$ 和任意实 $\theta$，
$$
\boxed{
e^{i\theta}Bf(L_1,\ldots,L_d)
\text{ 都不增生}.
}
\tag{11.1}
$$
确实，在 (10.3) 的唯一最低权处，
系数是 $e^{i\theta}c_{\alpha_0}B\ne0$，
其正实部不可能同时具有忠实迹0。

更一般，若 (10.1) 的每个矩阵系数属于 $M_s(\mathcal A)$，
每个条目的字符均为0，且至少一个系数非零，
则其实际值不增生。
因为选出的非零最低权矩阵若增生，
第5节的忠实矩阵迹与行列式拟幂零证明迫它为零。
特别这个非零系数级数的实际值也不可能等于零。

这精确排除：以有限个最终不交正源锚的任意解析因子，
把慢零字符符号 $S_N$ 或 $S_Y$ 转成 R199 所需的正实部类。
没有排除含 $L_i^*$ 的非解析表达式，
也没有声称慢符号在未知不变子商上不稠密。

## 12. 有界交换扰动与范围边界

上述多锚结论还允许将 (7.2) 改为
$$
Z_i=X_{a^{(i)}}+H_i,\qquad
H_i\in\mathfrak C\text{ 任意固定有界算子},
\qquad L_i=Z_i^{-1}.
\tag{12.1}
$$
R189 保证这些逆仍有界、拟幂零并属于 $\mathfrak C$。
这里“正源”仍指非负不可和系数行，
不把加入任意 $H_i$ 后的 $Z_i$ 额外称为增生算子。

只需补核 (8.1)：
先对没有 $H_i$ 的中心化实际第一阶用同一 $\Lambda_h$ 估计；
再在有限混合词中展开有界扰动。
由 (8.3)，所有 $H_i$ 保持每个第一阶的完整域及全部混合词域，
并与这些第一阶域交换。
$\mathfrak C$ 为交换代数，所以不同 $H_i$ 也交换。
于是每个展开项都可把 $H_i$ 的有界乘积移到左边，
其范数只多一个固定的 $\prod_i\|H_i\|^{k_i}$。
余下中心词由 (8.2) 控制，故仍得 (8.1)。

此后 (9.1)—(11.1) 原样成立。
这里不需要 $H_i\in\mathfrak U$：
证明只要求左系数 $B_\alpha$ 在高 Walsh 下按范数固定，
不要求 $U_tH_iU_t$ 有任何极限。
因此本节不是把 R197 的逐坐标 $C^*$ 反缩擅自扩大；
那种反缩若要在范数中固定其他逆，
仍需其原来的额外假设。

全篇只利用了可独立指定各正源中心的 (7.1)。
任意重叠非负行未被包含；
例如同一源的两个有界扰动不能自由选择两个不同增长率。
本文也未处理伴随变量、无正半径的形式级数、
或未知子商中不存在的有限柱测试。
