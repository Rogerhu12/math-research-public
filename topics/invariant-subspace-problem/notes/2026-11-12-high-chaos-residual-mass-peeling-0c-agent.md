# 高阶阈值覆盖不能控制残余平方和：星形反例与影响量剥离

日期：2026-11-12（UTC）。负责人：literature。预留 R96。

**状态：第 2—5 节的反例、精确最优残余量和剥离引理均已证明。** 本文不重复 R97 的 Fischer 乘积下界与碰撞估计，也不把尚需 R98 实际条件化估计的推论列为本稿独立结论。

R94 已从实际全部零矩推出：每个高位尾部中，超过 $e^{-c16^m}$ 的最高阶系数超图都有一致有界的顶点覆盖。本稿明确说明这一逐系数信息缺少什么，并给出下一步可以使用的定量分解。

## 1. 记号与准确问题

对可数指标集 $E$，记
$$
\mathcal R_p(E)=\ell^2([E]^p),\qquad
u=\sum_{|S|=p}u_Sx_S,\qquad x_i^2=0.
$$
这里 $x_S$ 也可等同于正交 Walsh 基向量。对 $B\subseteq E$，定义删去所有碰到 $B$ 的单项式后的核
$$
u^{\setminus B}
=\sum_{\substack{|S|=p\\S\cap B=\varnothing}}u_Sx_S,
\qquad
\mathsf M_u(B)=\|u^{\setminus B}\|_2^2.
\tag{1.1}
$$
这是残余系数的平方和，也称本稿的 HS 质量；不把它与 $\ell^1$ 系数和混用。

顶点影响量为
$$
I_i(u)=\sum_{S\ni i}|u_S|^2.
\tag{1.2}
$$
Tonelli 定理给出两个基本恒等式：
$$
\sum_{i\in E}I_i(u)=p\|u\|_2^2,\qquad
\|u^{\setminus\{i\}}\|_2^2=\|u\|_2^2-I_i(u).
\tag{1.3}
$$
以下所有删点都删除相应整行系数，而不是只删除一条边。

给定正的非增阈值 $\tau_m\downarrow0$，R94 类型的信息是：对每个 $m$，存在大小一致有界的 $B_m\subseteq[m,\infty)$，使
$$
S\subseteq[m,\infty)\setminus B_m
\quad\Longrightarrow\quad |u_S|\le\tau_m.
\tag{1.4}
$$
下面构造一个更强的反例：每个 $B_m$ 都可取空集，但即使重新选择最优的有限删点集，残余 HS 质量仍可远大于 $\tau_m^2$。

## 2. 对所有尾起点同时成立的二阶反例

**定理 2.1。** 对任意正的非增序列 $\tau_m\downarrow0$，存在非零
$u\in\mathcal R_2(\mathbb N)$ 及严格递增中心 $c_n$，满足：

1. 对每个 $m$，所有纯尾系数都满足
   $$
   i,j\ge m,\quad i\ne j
   \quad\Longrightarrow\quad |u_{\{i,j\}}|\le\tfrac12\tau_m.
   \tag{2.1}
   $$
   因而所有阈值以上的尾图都为空。
2. 在尾起点 $m=c_n$，对每个整数 $K\ge0$，精确有
   $$
   \boxed{
   \inf_{\substack{B\subseteq[c_n,\infty)\\|B|\le K}}
   \|u_{c_n}^{\setminus B}\|_2^2
   =\sum_{r=n+K}^{\infty}\frac1{r^2}.
   }
   \tag{2.2}
   $$
   这里 $u_{c_n}$ 是 $u$ 的纯尾部分。
3. 这些尾部同时具有分散影响量：
   $$
   \frac{\max_i I_i(u_{c_n})}{\|u_{c_n}\|_2^2}
   =\frac{n^{-2}}{\sum_{r=n}^{\infty}r^{-2}}
   \le\frac1n\longrightarrow0.
   \tag{2.3}
   $$

**构造。** 取 $c_1=0$。当 $c_n$ 已选定，取正整数
$$
L_n\ge \left(\frac{2}{n\tau_{c_n}}\right)^2,
\tag{2.4}
$$
令
$$
V_n=\{c_n+1,\ldots,c_n+L_n\},\qquad
c_{n+1}=c_n+L_n+1.
$$
因此各星形块 $\{c_n\}\cup V_n$ 两两不交，且整个第 $n$ 块严格位于第 $n+1$ 块之前。定义
$$
u=\sum_{n=1}^{\infty}
\frac1{n\sqrt{L_n}}\,
x_{c_n}\sum_{j\in V_n}x_j.
\tag{2.5}
$$
不同单项式正交，所以
$$
\|u\|_2^2
=\sum_n L_n\frac1{n^2L_n}
=\sum_n\frac1{n^2}<\infty.
\tag{2.6}
$$
这是合法的二阶无限秩 Walsh 核；无需点值收敛假设。

**证明 (2.1)。** 第 $n$ 块的每条边都含有其最小顶点 $c_n$。一条边完全位于 $[m,\infty)$ 时，必有 $c_n\ge m$。于是由 (2.4) 和阈值的单调性，
$$
\frac1{n\sqrt{L_n}}
\le\frac{\tau_{c_n}}2
\le\frac{\tau_m}2.
$$
注意这不是只在一个尾起点构造的小系数例子；同一个 $u$ 同时满足所有 $m$ 的条件。

**证明 (2.2)。** 在 $c_n$ 起始的尾部，恰好保留第 $n,n+1,\ldots$ 个完整星形块。第 $r$ 块的总质量是 $r^{-2}$。任意一个被删除的顶点只属于一个块；所以 $K$ 个顶点至多碰到 $K$ 个块，在每个被碰到的块中至多删除该块的全部质量。因此总共能删除的质量至多是最大的 $K$ 个块质量之和
$$
\sum_{r=n}^{n+K-1}r^{-2}.
$$
反过来，删除中心 $c_n,\ldots,c_{n+K-1}$ 正好达到这个上界。这证明了精确等式，而不只是某个特定删点方案的下界。

**证明 (2.3)。** 中心 $c_r$ 的影响量是 $r^{-2}$；每个叶子的影响量是 $(r^2L_r)^{-1}\le r^{-2}$。故第 $n$ 个尾部的最大影响量恰为 $n^{-2}$。又
$$
\sum_{r=n}^{\infty}r^{-2}\ge\int_n^\infty x^{-2}\,dx=\frac1n.
$$
定理得证。

### 2.1. 对当前超快阈值的明确后果

取 $\tau_m=e^{-a16^m}$，其中 $a>0$ 任意。由 (2.2)，
$$
\inf_{|B|\le K}
\|u_{c_n}^{\setminus B}\|_2
\ge\frac1{\sqrt{n+K}}.
\tag{2.7}
$$
固定的顶点覆盖预算当然不能把这个量压到 $e^{-a16^{c_n}}$。

更强地，若允许预算 $K_m$ 满足
$$
\log(1+K_m)=o(16^m),
\tag{2.8}
$$
则沿 $m=c_n$，因 $n\le c_n+1=m+1$，
$$
\log(n+K_{c_n})=o(16^{c_n}),
$$
从而
$$
\inf_{|B|\le K_{c_n}}
\|u_{c_n}^{\setminus B}\|_2
\ge \exp[-o(16^{c_n})].
\tag{2.9}
$$
因此即使删点预算远大于 $O(16^m)$，阈值覆盖本身仍不强迫实际误差尺度上的小残余。

这不是实际全零矩的反例。它只否定“R94 的阈值覆盖已经足够推出小 HS 尾”的逻辑步骤。事实上 (2.3) 使该例的高尾变得低影响；R97 的创建下界正会识别这种分散质量，所以额外的实际近核关系能够排除它。

### 2.2. 同一障碍适用于每个固定 $p\ge2$

可将每块的单个中心替换为 $p-1$ 个固定茎顶点，并令边由整根茎加上一个叶子组成。每条边仍有相同的最小茎顶点；删除一个茎顶点即可清空整块。选择块长使系数低于其最小顶点的阈值，前述所有证明不变。因此它是一般高阶的障碍，并非二阶的偶然现象。

## 3. 影响量剥离的有限定量二择一

这里给出可以接到 R97/R98 的正向工具。它本身只是正交质量的精确恒等式，不依赖 Pouzet 或任何无限维紧性。

**引理 3.1。** 给定 $p\ge1$、
$u\in\mathcal R_p(E)$、
$M\ge\|u\|_2$、
$0<\delta<M$ 和 $0<\rho<1$，存在有限集 $B\subseteq E$，满足
$$
|B|\le R:=
\left\lceil
\frac{2\log(M/\delta)}{-\log(1-\rho)}
\right\rceil
\le
\left\lceil\frac{2}{\rho}\log\frac M\delta\right\rceil,
\tag{3.1}
$$
且以下至少一项成立：

- 小残余：
  $$
  \|u^{\setminus B}\|_2\le\delta;
  \tag{3.2}
  $$
- 低影响残余：
  $$
  \|u^{\setminus B}\|_2>\delta,\qquad
  \sup_{i\notin B}I_i(u^{\setminus B})
  \le\rho\|u^{\setminus B}\|_2^2.
  \tag{3.3}
  $$

若初始 $\|u\|_2\le\delta$，直接取 $B=\varnothing$，无需使用 (3.1)。

**证明。** 从 $B_0=\varnothing$ 开始。若 (3.2) 或 (3.3) 已成立，就停止。否则存在 $i_r\notin B_r$，使
$$
I_{i_r}(u^{\setminus B_r})
>\rho\|u^{\setminus B_r}\|_2^2.
$$
把它加入 $B_r$。由 (1.3)，
$$
\|u^{\setminus B_{r+1}}\|_2^2
<
(1-\rho)\|u^{\setminus B_r}\|_2^2.
\tag{3.4}
$$
若一直未遇到 (3.3)，迭代 $R$ 次得到
$$
\|u^{\setminus B_R}\|_2^2
\le(1-\rho)^RM^2\le\delta^2.
$$
因为 $-\log(1-\rho)\ge\rho$，得到 (3.1) 的较粗上界。每一步只需选择一个超过阈值的顶点，不要求无限集合上的极值可取；这也避免了任何无穷贪心选择的隐含问题。证毕。

### 3.1. 在尾部及既有覆盖之外剥离

该引理可直接用在任意 $E=[m,\infty)\setminus B_0$。新增顶点都属于原来的高尾，且结论为
$$
u^{\setminus(B_0\cup B)}.
$$
预算只增加 $|B_0|$；它不依赖新增顶点的最大编号。因此若 R94 已提供一个固定大小的阈值覆盖，可先移除它，再作影响量剥离。但剥离引理本身也可从完整尾核直接启动，不必先使用 R94。

本引理并不声称剥离后必然小残余。定理 2.1 的反例在 $n$ 大时已经满足 (3.3)，所以算法可以在零步停止。这恰好指出必须借助实际近核去排除哪一个分支。

## 4. 与创建下界和实际条件化预算的明确接口

本节只整理本稿引理的参数，不重证 R97 或 R98 的算子估计。

### 4.1. 固定次数的影响阈值

对要测试的输入次数 $k\le q$，$q\ge1$，R97 的碰撞界使用常数
$$
D_{p,q}=2q{p+q-2\choose p-1}.
\tag{4.1}
$$
若选择
$$
\rho_{p,q}
=\frac1{2D_{p,q}}
=\frac1{4q{p+q-2\choose p-1}},
\tag{4.2}
$$
则 (3.3) 正是使 R97 在全部 $k\le q$ 上给出
$$
\|u^{\setminus B}\star v\|_2
\ge\frac{\|u^{\setminus B}\|_2}{\sqrt2}\|v\|_2
\tag{4.3}
$$
的充分条件。R97 的下界来源于经典 Fischer/Bombieri 乘积不等式，再扣除重复坐标项；本文不将该经典下界算作新结果。

于是，对任意目标 $\delta$，至多
$$
\frac{2}{\rho_{p,q}}\log(M/\delta)+1
\tag{4.4}
$$
个新增顶点后，若残余仍大于 $\delta$，创建映射就有统一左界 $\delta/\sqrt2$。这个结论不需要找到任何单个较大系数，也不受定理 2.1 的大星形块影响。

### 4.2. 保守尺度：$\delta_m=e^{-4^m}$

假设 $M$ 固定且 $\rho$ 固定。取
$$
\delta_m=e^{-4^m}.
$$
由 (3.1)，可取
$$
|B_m|=O_{\rho,M}(4^m).
\tag{4.5}
$$
因此任意固定常数 $b,d>0$ 所产生的损失
$$
e^{b|B_m|}\delta_m^{-d}
$$
至多为 $e^{O(4^m)}$。即使额外付出
$e^{O(|B_m|\log(2+|B_m|))}$，对数也只是 $O(m4^m)=o(16^m)$。这些都比
$$
e^{-\gamma16^m+o(16^m)},\qquad \gamma>0,
$$
的实际误差弱得多。

这个预算计算只说明在已建立相应条件化近核估计之后，有足够空间支付剥离损失；它没有代替条件化公式的证明。

### 4.3. 直接 $16^m$ 尺度的显式预算

若条件化损失确为 $e^{b|B_m|}$、反向递归的残余范数损失为 $\delta_m^{-d}$，其中 $b,d$ 固定，则也可直接取
$$
\delta_m=e^{-a16^m}.
$$
粗界 (3.1) 给
$$
|B_m|\le\frac{2a}{\rho}16^m+O_{\rho,M}(1).
$$
把损失乘到误差 $e^{-\gamma16^m+o(16^m)}$ 上，得到
$$
\exp\left[
-\left(\gamma-a\left(d+\frac{2b}{\rho}\right)\right)16^m
+o(16^m)
\right].
\tag{4.6}
$$
因此任意
$$
0<a<\frac{\gamma}{d+2b/\rho}
\tag{4.7}
$$
都保留严格负指数。例如取分母再乘 $2$，可保留至少 $\gamma/2$ 的余量。使用这一步时，必须先从实际估计中确认 $b,d$ 与 $m$ 无关；不能将任意未控制的条件化损失塞进这两个常数。

### 4.4. 顶阶系数不因高位物理零条件化改变

以下是纯 Walsh 代数事实。设 $f$ 的总次数至多 $p$，有限集 $B$ 全在所考虑的高位。把 $B$ 中每个物理位条件为 $0$，即把对应 Walsh 变量置为 $+1$，得到 $f_B$。若 $S\cap B=\varnothing$ 且 $|S|=p$，则
$$
\widehat{f_B}(S)
=\sum_{T\subseteq B}\widehat f(S\cup T)
=\widehat f(S),
\tag{4.8}
$$
因为 $T\ne\varnothing$ 时总次数超过 $p$。所以最高阶纯尾核恰是删点核 $u^{\setminus B}$；不存在新的顶阶交叉项。

同理，若 $g$ 的最高次数为 $q$，且固定 $q$ 元集合 $S_0$ 与 $B$ 不交，则
$$
\widehat{g_B}(S_0)=\widehat g(S_0).
\tag{4.9}
$$
因此一个固定的非零最高阶低位系数保证
$\|g_B\|_2\ge|\widehat g(S_0)|>0$。本事实可防止条件化后测试端无意坍缩为零；从实际 $A$ 的零矩获得 $f_B,g_B$ 的近核仍由 R98 的真实进位估计承担。

条件化本身是从有限次数空间到有限次数空间的有界算子，其粗范数不超过 $2^{|B|/2}$：按 $B$ 上 Walsh 系数分组后，对每个外部系数使用含 $2^{|B|}$ 项的 Cauchy–Schwarz，再求和即可。这与上述指数预算相容。

## 5. 文献边界与没有证明的事项

Pouzet 的原始定理是：

Maurice Pouzet, *When is the orbit algebra of a group an integral domain? Proof of a conjecture of P. J. Cameron*, RAIRO — Theoretical Informatics and Applications **42** (2008), 83–103，
[DOI 10.1051/ita:2007054](https://doi.org/10.1051/ita:2007054)，
[期刊全文](https://numdam.org/item/10.1051/ita:2007054.pdf)。

原文 Theorem 1.3，印刷页 86，控制的是**精确零乘积的支撑横截数**；R93 已准确引用并推导有限匹配的 Hilbert 左逆。它不直接给本稿所否定的“任意阈值图覆盖推出 HS 尾速率”。本次检索没有得到可直接替代此缺口的原始定量范数定理；不据此声称相关稳定性问题在所有文献中都未被研究。

R97 所用经典普通多项式乘积下界可核对：

Bruce Reznick, *An inequality for products of polynomials*, Proceedings of the American Mathematical Society **117** (1993), no. 4, 1063–1073，
[DOI 10.2307/2159535](https://doi.org/10.2307/2159535)，
[机构元数据](https://experts.illinois.edu/en/publications/an-inequality-for-products-of-polynomials/)，
[期刊扫描全文](https://citeseerx.ist.psu.edu/document?doi=0a53488d9b60a322fe8333ffabdf21fbf7f26672&repid=rep1&type=pdf)。

2026-11-12 已核对该文 Formula 3.7 和 Theorem 3.9，印刷页 1067–1068；其未按次数归一化的 Fischer 范数满足 $\|FG\|\ge\|F\|\|G\|$。平方零投影的碰撞损失需另算，不能直接把普通多项式下界转给平方零代数。

**本稿的准确终点：** 已给出对全部尾起点同时成立、并能精确计算最优删点残余的反例；也已给出可支付的有限剥离预算。尚未仅凭本稿推出一般有限 chaos 配对分离，更未决定实际 $A$ 的任意 $L^2$ 不变子空间。下一步需以 R97、R98 的真实近核排除低影响分支，并处理条件化后留下的较低次数结构。
