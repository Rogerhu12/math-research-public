# O5 接续：惯性阶、CM 靶值及 Hecke 对局部共同根的实际作用

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

本笔记接续 R57、R59。已完成的新结论见 [R64](../results/R64-inertial-order-traces-and-cm-type-targets.md)。父会话统一处理 git、README 差异、HANDOFF 和索引；本文件记录新的独立探索。主目标及 O5 的随层共同根排除尚未完成。

## 1. R64 完整证明中的三个关键检查

一般 Drinfeld 分量的有限惯性必须使用完整 $\mathbb F_{p^2}^{\times}$ 经过 $u\mapsto u^{p-1}$ 给的 $\mu_{p+1}$，而不是再取范数一子群后所得的较小作用。在
$$Y^2=X(X^{(p+1)/2}+a)$$
上，$\zeta$ 作用为 $(X,Y)\mapsto(\zeta^2X,\zeta Y)$。微分 $X^i dX/Y$ 的字符为 $\zeta^{2i+1}$；加上逆字符后，得到全部奇指数，且在 $p\equiv1\bmod4$ 去掉二次字符。故精确阶 $d$ 的 $H^1$ 迹是 $\varphi(d)$，不是 $\varphi(d)/2$。阿贝尔维数才除以二。

$j=0$ 的额外自同构在 EP 原文 p.251 恰是这个作用中的 $\mu_3$。其不变量条件为 $3\mid k$，等价于 $d\mid(p+1)/3$。$j=1728$ 的商为 $\mathbb P^1$。这两个特殊处理决定了类型坏靶值是否相同，不能只按一般 Drinfeld 亏格推断。

完整 $J$ 上的阶投影 $e_d$ 在全部该阶惯性空间上为恒等，因此其每个分量部分迹可由字符直接求出。真正 $A$ 上的 $e_Ae_d$ 一般只保留其中一部分全局因子；它可能混合不同分量，不能继续把部分迹写成 $\varphi(d)$。R64 的实际 QC 应用使用 $W_A\cap Z^{\rm type}$。

对 $41\le p\le997$ 的全部素数做过精确整数检查：逐个枚举奇指数的阶，核对每阶字符数及 $j=0$ 不变量数与公式一致。这只是核对实现记号的辅助检查；证明是 R64 的完整字符计算，不依赖有限枚举。

## 2. 新的全局 CM 靶值识别

R64 将类型标量方向的坏秩精确算为 $0,1,1,2$（对应 $p\bmod12=1,5,7,11$），并证明后三类的每个坏靶值分别由
$$\{0,54000\},\qquad \{1728,287496\},\qquad
\{0,1728,54000\}$$
中的实际有理 CM 点实现。所用四个模型只有 $2,3$ 处可能坏约化；明确整数分解排除了其 $j$ 值模 $p>37$ 意外变成另一个特殊标号。

这给真实辅助函数的准确有限联合条件
$$\mathcal Q_F(x)=\mathcal Q_F(c)\quad\text{对全部 }F\in W_A\cap Z^{\rm type},$$
其中同一个 $c$ 从上述有限集选择。它不是把每条方程独立选择一个常数。其作用在于把未知的坏靶向量改成确定全球 CM 点上的实际函数值；下一步需要识别这些共同函数值纤维。

## 3. 明确 CM 基准点的 Hecke 关系（已证明）

令 $c_\Delta$ 为 CM 判别式 $\Delta$ 的规范非分裂 Cartan 正规化子点，且假设 $p>37$ 惰于相应 CM 域。则有几何有效除子恒等式
$$\boxed{T_2(c_{-3})=3c_{-12},\qquad
T_2(c_{-4})=c_{-4}+2c_{-16}.}\tag{3.1}$$

**证明。** 对椭圆曲线 $E$，$T_2$ 按三个循环二子群计数。其输运的 $p$-Cartan 结构由二同源在 $E[p]$ 上的同构给出。因为 $2\ne p$，同一 CM 域的整环在 $p$ 处相等，所以输运后仍是目标曲线的规范 CM Cartan 结构。

对于 $\mathcal O_{-3}=\mathbb Z[\zeta_3]$，$2$ 惰性。因此没有 $\mathcal O_{-3}$ 稳定的二子群，三个商都具有导子二的整环 $\mathcal O_{-12}$。这些整环类数为一，所有目标都有 $j=54000$。也可直接看 $\zeta_3$ 在 $E[2]\simeq\mathbb F_2^2$ 的三个非零向量上循环置换；故三个二子群在源自同构作用下给同一个粗模目标。相同目标按三个子群的重数计，得到第一式。

对于 $\mathcal O_{-4}=\mathbb Z[i]$，$2=(1+i)(1-i)$ 分歧。恰有一个 $\mathcal O_{-4}$ 稳定的二子群，即 $\ker(1+i)$；对应商仍为 $c_{-4}$。另外两个子群交换于 $i$ 的作用，商的乘子环为 $\mathbb Z+2\mathbb Z[i]=\mathcal O_{-16}$，类数一给同一个 $j=287496$ 目标，按两个子群计重。得到第二式。

所用关于商整环的断言可以直接在复格中核对：阶二子群对应含 $\mathcal O$ 且指数二的格 $L$，其乘子环为 $\{a\in K:aL\subset L\}$；非 $\mathcal O$ 稳定时该环恰为 $\mathbb Z+2\mathcal O$。例如 $\mathcal O=\mathbb Z[i]$ 的两个非稳定格可取 $\mathbb Z+\tfrac i2\mathbb Z$ 及 $\tfrac12\mathbb Z+i\mathbb Z$，二者由乘 $i$ 互换，逐个乘子计算得判别式 $-16$；第三个格 $\mathbb Z+\tfrac{1+i}2\mathbb Z$ 则为 $\mathbb Z[i]$ 稳定格，对应分歧核。在 $\mathbb Z[\zeta_3]$ 中三个格被单位置换，一个代表 $\mathbb Z+\tfrac{\zeta_3}2\mathbb Z$ 的乘子环为 $\mathbb Z+2\mathbb Z[\zeta_3]$。证毕。

这是经典 CM Hecke 分配关系的此处具体版本。已核验原始来源：D. Kohen and A. Pacetti, *Heegner Points on Cartan Non-split Curves*, Canadian Journal of Mathematics **68** (2016), 422–444，DOI [10.4153/CJM-2015-047-6](https://doi.org/10.4153/CJM-2015-047-6)，§3.1，p.438，公式 (3.1) 直接按指数素数的 CM 格求和。这里给出完整的特殊自同构与重数证明，不把其一般 Euler 系统公式在单位数变化时直接套用。

### 3.1 无基点 Abel–Jacobi 类没有遗失尖点平移

令 $D$ 为全部尖点除子，$\delta=(p-1)/2$，$u_D(x)=[\delta x-D]$。R33 (2.3) 已证明
$$T_2D=3D$$
是实际除子等式，原因是全部尖点为一个 Galois 轨道且 Hecke 保持尖点、总次数为三。因此 (3.1) 准确给
$$\boxed{T_2u_D(c_{-3})=3u_D(c_{-12}),\qquad
(T_2-1)u_D(c_{-4})=2u_D(c_{-16}).}\tag{3.2}$$
这不是仅模去一个未知尖点类或挠点后的等式。

对 R47 的实际 $f$ 坐标，因投影和 $\ell$ 进对数都与 Hecke 相容，有
$$z_f(c_{-12})=\frac{a_2(f)}3z_f(c_{-3}),\qquad
z_f(c_{-16})=\frac{a_2(f)-1}2z_f(c_{-4}).\tag{3.3}$$
这里在特征零中除以 $2,3$，没有添加辅助素数单位假设。即使某个 CM 点在一个因子上的投影为零，式子仍成立；不能反过来从式子断言所有投影非零。

## 4. 为什么点值 Hecke 关系还没有给出 QC 函数恒等式

设一个局部 Hecke 纤维有分支 $x_1,\ldots,x_{q+1}$，用相同规范基准记其对数向量为 $z_r=z(x_r)$。确有
$$\sum_rz_r=T_qz(x),\tag{4.1}$$
但真实 QC 的全局项包含二次项。若 $B$ 是 R47 由全球高度延拓的对称 Hecke 平衡双线性形式，$F$ 自伴，则
$$2B\left(\sum_rz_r,F\sum_rz_r\right)
=2\sum_rB(z_r,Fz_r)+4\sum_{r<s}B(z_r,Fz_s).
\tag{4.2}$$
所以逐支 QC 函数求和会留下 (4.2) 的交叉项，不能只用 (4.1) 把它变成某个 $T_qF$ 方向的 QC 函数。Poincaré 双扩张群律在局部高度侧也产生对应的交叉双扩张项；除非把它们连同规范平移与实际截面都算出，不能删去。

特别地，(3.3) 能计算两个 CM 点之间全球二次项的差，但不控制各自附近的全部解析函数。若 $z(c')=uz(c)$，R54 的全局部分之差准确为
$$\sum_f\operatorname{Tr}\left(c_f\left[
2F_f(u_f^2-1)z_f(c)^2
-\xi_{2F,f}(u_f-1)z_f(c)\right]\right).
\tag{4.3}$$
其中平移项 $\xi_{2F,f}$ 必须保留。真实辅助局部高度之差还需要减去相应 QC 值差；后者由 R54、R64 精确等于 $-\log_\ell(p)$ 倍该方向的坏分量差。

## 5. 正在推进的局部接口

Hecke 覆盖在特殊 CM 点有源自同构造成的分歧。例如第一式中源 $c_{-3}$ 的三个二子群被三阶自同构循环置换，而目标 $c_{-12}$ 没有额外自同构。局部覆盖参数 $t$ 与源粗模参数 $s$ 的关系为 $s=t^3$（乘一个单位后）；三个分支由 $t,\zeta_3t,\zeta_3^2t$ 表示。对全纯积分求和只保留 $t$ 的三倍数次项。

因此形式上的 Hecke 迹关系并不直接给目标 CM 点处的一阶、二阶积分系数；它首先关系到三阶项。这正是需要明确计算的地方，不能把 Hecke 对角线的横截性当作 QC 函数的简单根。

Hashimoto–Lido–Lombardo–Mascot–Parent 的 2026 equationless 文献 §5.3 的 Hecke 对角横截性用于对应的代数交数。其 §6.10 的 Hensel 步骤则明确另行假设某真实函数导数模辅助素数非零；两者不是同一个命题。本文接下来直接研究实际 CM 基准函数的 jet 与双扩张交叉项，不把一个横截性结果偷换成另一个。

来源核查：该文 [arXiv:2608.10919v1](https://arxiv.org/html/2608.10919v1)，Lemma 5.3.3（下载 PDF pp.39–40）与 §6.10（PDF pp.63–64）。尚未发表的新论证仅用于确定计算接口；本笔记 (3.1)–(4.3) 的证明不依赖其未发表结论。

## 6. 对真实 $A$ 的 Poincaré 群律：交叉项不能由迹点恢复

本节对任意实际 $0\ne F\in W_A$ 工作，不要求 $A$ 包含一个完整惯性类型块。令 $f:A\to A^\vee$ 为其对称同态，并在有理线丛群中记
$$\mathcal B_F=(\operatorname{id},f)^*\mathcal P_A.$$
它满足 $\phi_{\mathcal B_F}=2f$。对 $A^m$ 的投影 $\operatorname{pr}_r$ 和加法 $S=\sum_r\operatorname{pr}_r$，双扩张群律准确给
$$S^*\mathcal B_F\simeq
\bigotimes_r\operatorname{pr}_r^*\mathcal B_F
\otimes\bigotimes_{r<s}
\left[(\operatorname{pr}_r,f\operatorname{pr}_s)^*\mathcal P_A
\otimes(\operatorname{pr}_s,f\operatorname{pr}_r)^*\mathcal P_A\right].
\tag{6.1}$$
因为 $f$ 对称，方括号内两项在交换变量后相同；仍保留两项可避免误漏二倍。所有等式可先清除 $f$ 的有限分母后作为实际线丛等式使用。

### 引理：方差线丛确实非平凡

当 $m\ge2$ 时，定义
$$\mathcal V_{F,m}=
\left(\bigotimes_r\operatorname{pr}_r^*\mathcal B_F\right)^{\otimes m}
\otimes(S^*\mathcal B_F)^{-1}.
\tag{6.2}$$
它的 NS 类非零，且不能从加法映射 $S$ 拉回一个线丛。

**证明。** 沿反对角嵌入
$$a:A\longrightarrow A^m,\qquad P\longmapsto(P,-P,0,\ldots,0)$$
拉回。$S\circ a=0$，而对称线丛满足 $[-1]^*\mathcal B_F\simeq\mathcal B_F$（刚性化下取相容同构），所以
$$a^*\mathcal V_{F,m}\simeq\mathcal B_F^{\otimes2m}.$$
其对应同态为 $4mf\ne0$，故 NS 类非零。若 (6.2) 来自 $S$ 的拉回，则沿 $a$ 的拉回为常数线，NS 类应为零，矛盾。证毕。

这在实际 $A$ 的代数 Poincaré 双扩张层面排除了“只要知道所有 Hecke 邻居的和，就知道其二次高度之和”的形式推理，不是仅拿任意解析函数作比喻。

### 6.1 有理 Hecke 迹点与非有理方差点

若 $x\in X(\mathbb Q)$，取有限 Galois 域 $L$ 使其全部 $m=q+1$ 个 Hecke 邻居 $x_r$ 定义于 $L$。令
$$P_r=e_Au_D(x_r),\qquad S=\sum_rP_r=T_qe_Au_D(x)\in A(\mathbb Q).$$
在 $A(L)\otimes\mathbb Q$ 中置 $R_r=P_r-S/m$，则 $\sum_rR_r=0$。对在 $L$ 上相容归一化的全球双线性高度 $h_L$，有恒等式
$$\sum_r h_L(P_r,FP_r)
=\frac1m h_L(S,FS)+\sum_rh_L(R_r,FR_r).
\tag{6.3}$$
线性项对 $R_r$ 求和为零；二次交叉项因 $\sum R_r=0$ 消去，即得证明。

第一项可由 R47 的有理 Mordell–Weil 高度矩阵求得。第二项属于实际非有理迹零点的高度；R47 只证明 $A(\mathbb Q)$ 在 Lie 代数中满秩，并未给出 $A(L)$ 的全部 Mordell–Weil 高度矩阵。于是不能把 $h_L(P_r,FP_r)$ 逐个替换为 R47 在 $A(\mathbb Q)$ 上拟合的同一二次多项式。

即使对 $L/\mathbb Q$ 作范数，(6.1) 的交叉双扩张项仍然存在；(6.2) 说明没有一个只依赖迹点的普遍线丛消去。若某个特殊 Hecke 纤维在原曲线上另有额外消去，必须证明那个特殊拉回等式，不能从加法律本身得到。

因此当前通过 Hecke 纤维增加方程的具体缺项已经明确：要么求出这些迹零点的额外全球高度，要么证明相应交叉线丛沿实际模曲线族有额外平凡化。两者目前都没有随层的已证明输入。此检验不把重新参数化的原有二层条件计作新增根约束。
