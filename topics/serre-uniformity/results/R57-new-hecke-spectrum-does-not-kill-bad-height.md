# R57. 平方水平新 Hecke 谱并不消去真实坏高度

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明。** 本文给出一个真正来自全局有理 Hecke 代数的方向，并算出它的坏分量高度差。它说明不能用“Brandt 模块对应素数水平，而 Heegner 商属于平方水平新部分”直接推出 R45 的 $\Phi_A=0$。

精确结论分两层：

1. 对任意素数 $p>37$、$p\equiv5\pmod {12}$，在完整 $J=J_{\rm ns}^+(p)$ 上存在 Rosati 对称、trace-zero 的有理 Hecke 算子
   $$F=\frac{p-5}{2}e_{\rm tor}-1.$$
   这里 $e_{\rm tor}$ 是定义于 $\mathbb Q$ 的全局 Hecke 幂等元。对任意几何超奇异 $j\ne0$，R43 的实际垂直系数满足
   $$\boxed{\quad k_j(F)-k_0(F)=\frac{(p-1)(p-5)}{p+1}\ne0.\quad}\tag{0.1}$$
   有理方向的 $k$ 指整数方向系数差的 $\mathbb Q$ 线性延拓。
2. 当 $p=41$，Dogra–Le Fourn 已发表的非消失计算给 $A=J$。此时 $F=18e_{\rm tor}-1$ 是真正 Heegner 商的方向，且 $j=0,28$ 两个分量都有 $\mathbb Q_{41}$ 点；于是
   $$k_{28}(F)-k_0(F)=\frac{240}{7},\qquad
   h^{\rm Nek}_{F,41,b}(x)=\frac3{70}\log_\ell(41)
   \tag{0.2}$$
   对分别位于 $j=0,28$ 分量的 $b,x$ 成立。乘一个正整数使 $NF\in\Lambda_A$ 后，两边同步乘 $N$，仍非零。因此 $\Phi_A$ 及其在真正 $\mathbb Q_{41}$ 可达分量上的点值映射均非零，R55 的有限靶集并非单点。

这不是任意大层上的非零性定理：第一项在完整 Jacobian 上，第二项才使用一个明确层的 $A=J$。它排除的是一个拟议的形式性谱消失推论，不排除某些其他层或特定方向发生额外消失。

## 1. 全局有理的潜在全环面幂等元

### 引理 1

设 $B$ 为定义于数域的 $d$ 维阿贝尔簇，且一个 $d$ 次数域 $K$ 以含单位的方式嵌入 $\operatorname{End}^0(B)$。在一个使 $B$ 获得半稳定约化的局部扩张上，若其约化环面秩为 $t$，则 $t=0$ 或 $t=d$。

**证明。** 将环面分裂后，记其特征空间为
$$M=X^*(T)\otimes_{\mathbb Z}\mathbb Q,\qquad\dim_{\mathbb Q}M=t.$$
Néron 模型的函子性使每个实际端同态作用于恒等分量及其最大环面；清分母后得到 $K$ 在 $M$ 上的有理作用。如果 $t>0$，此作用含单位，因此从域 $K$ 出发的作用同态为单射。于是 $M$ 为非零 $K$ 向量空间，$d=[K:\mathbb Q]$ 整除 $t$。又 $t\le\dim B=d$，所以 $t=d$。若 $t=0$，半稳定恒等分量就是阿贝尔簇，故该扩张上为好约化。证毕。

沿用 R45 的 Hecke 相容重数一分解：
$$J\sim_{\mathbb Q}\prod_{[f]}A_f,\qquad
\mathbb T_{\mathbb Q}=\prod_{[f]}K_f,\qquad
\dim A_f=[K_f:\mathbb Q].
\tag{1.1}$$
在共同的半稳定扩张上对每个 $A_f$ 使用引理 1。令 $\mathcal F_{\rm tor}$ 为潜在环面秩等于 $\dim A_f$ 的那些完整 Galois 轨道，定义
$$e_{\rm tor}=(\varepsilon_f)_f\in\mathbb T_{\mathbb Q},
\qquad
\varepsilon_f=
\begin{cases}1,&[f]\in\mathcal F_{\rm tor},\\0,&[f]\notin\mathcal F_{\rm tor}.\end{cases}
\tag{1.2}$$
这是通过**全局因子选择**得到的有理 Hecke 幂等元，而不是先在局部 Raynaud 分解中选择投影、再假设该投影能提升。它定义于 $\mathbb Q$；R45 所用 Hecke 代数的 Rosati 对称性使它自伴。

令 $\Gamma$ 为半稳定图。半稳定约化的单值滤过给
$$\operatorname{gr}_0^M H^1=H^1(\Gamma),\quad
\operatorname{gr}_1^M H^1=\bigoplus_v H^1(C_v),\quad
\operatorname{gr}_2^M H^1=H_1(\Gamma)(-1).
\tag{1.3}$$
由引理 1，$e_{\rm tor}$ 在两个图同调分次上为恒等，在中间的分量上同调之和上为零。若 $r=b_1(\Gamma)$，它在 $H^0(J,\Omega^1)$ 上的迹为 $r$。

Edixhoven–Parent (2021), Theorem 3.5 在 $p\equiv5\pmod {12}$ 时给
$$r=\frac{p-5}{12},\qquad
g=\frac{(p-5)^2}{24}.
\tag{1.4}$$
因此令
$$c=\frac gr=\frac{p-5}{2},\qquad F=ce_{\rm tor}-1,\qquad
\lambda=c-1=\frac{p-7}{2}.
\tag{1.5}$$
便有 $\operatorname{Tr}(F|H^0(J,\Omega^1))=cr-g=0$。该 $F$ 在图同调上为 $\lambda$ 倍恒等，而在每个 $H^1(C_v)$ 上为 $-1$，所以其分量部分迹为
$$\operatorname{tr}_v(F)=-2g(C_v).\tag{1.6}$$
这里不需要为一般 Hecke 对应构造 Brandt 模型上的作用：实际上同调作用已由全局因子和单值滤过确定。

## 2. 半稳定图及其准确长度

仍设 $p\equiv5\pmod {12}$、$p>37$。Edixhoven–Parent (2021), Theorem 3.5、Remark 3.8 给下列几何半稳定图：

- 两个 Igusa 顶点 $I_1,I_2$，各亏格 $(p-5)(p-17)/96$；
- $n=(p+7)/12$ 个 Drinfeld 顶点 $D_j$，每个分别用一条边连接到 $I_1$ 和 $I_2$；
- $j=0$ 的顶点亏格 $g_0=(p-5)/12$；其余顶点亏格 $g_j=(p-1)/4$。此剩余类中 $1728$ 普通，故没有另一个特殊超奇异标号。

文献的全分歧扩张度是
$$E=\frac{p^2-1}{2}.$$
令 $\pi_0$ 为该扩张的整数归一化素元。节点方程为
$$xy=\pi_0^{\,2a_j},\qquad
a_j=\begin{cases}3,&j=0,\\1,&j\ne0.\end{cases}
\tag{2.1}$$
所以在全文统一使用的 $v_p(p)=1$ 尺度下，每条半边的长度为
$$L_j=\frac{2a_j}{E}=a_jL,\qquad L=\frac4{p^2-1}.
\tag{2.2}$$
一条 $I_1\!-\!D_j\!-\!I_2$ 路径的总长度是 $2L_j$。不得把这个路径长度再当作单条半边长度，亦不得把 $\operatorname{ord}_{\pi_0}$ 的节点厚度直接代入 $v_p$ 归一化的高度。

## 3. 图高度与分歧基变换的尺度

选取一个半稳定分裂扩域 $K/\mathbb Q_p$，分歧度为 $e$。对 R43 §4 的对应除子 $Z$ 和局部基点 $b$，令
$$D_Z(b,x)=\Delta^*Z-Z|_{\{b\}\times X}-Z|_{X\times\{x\}}.
\tag{3.1}$$
因 $Z$ 对称，此处与 R43 的 $D_{Z^\top}(x,b)$ 相同。将其加垂直修正到对各分量次数为零，记为 $\mathcal D_Z(b,x)$。定义
$$\widehat h_F(x)
=\frac1e\,(\overline{x}-\overline b)\cdot\mathcal D_Z(b,x),
\tag{3.2}$$
其中右侧交数先使用 $\operatorname{ord}_K(\pi_K)=1$ 的整数尺度。这个 $1/e$ 必须保留。

确实，有限分歧基变换使同一水平除子交数乘 $e$；之后解奇点不改变已作垂直正交修正的 Néron 配对。也可直接从 R43 的积分双扩张看：一个基底标量 $p^m$ 在扩域上阶为 $em$，除以 $e$ 恢复其原阶。由唯一局部 splitting，所得归一化与原 $\mathbb Q_p$ 高度相同。

等价地，把 R43 的字符扩展为
$$\chi_K(a)=-v_p(a)\log_\ell(p),\qquad
\chi_K(\pi_K)=-\frac1e\log_\ell(p).
\tag{3.3}$$
于是 R43 的基点 Nekovář 高度满足
$$h^{\rm Nek}_{F,p,b}(x)=-\log_\ell(p)\,\widehat h_F(x).
\tag{3.4}$$

Betts–Duque-Rosero–Hashimoto–Spelier 的局部高度公式（作者版 v3, Theorem 3.11；已发表于 2026 年）使用边长配对
$$\langle e,e\rangle=L_e,\qquad
\pi:C_1(\Gamma,\mathbb R)\to H_1(\Gamma,\mathbb R)$$
和其正交投影。用 (3.2) 的归一化，公式是
$$\nabla^2\widehat h_F
=2\sum_{e\in E(\Gamma)^+}\frac{\langle e,F\pi(e)\rangle}{L_e^2}|ds_e|
+\sum_v\operatorname{tr}_v(F)\delta_v.
\tag{3.5}$$
这里
$$\nabla^2h=-\sum_eh''|ds_e|
-\sum_v\left(\sum_{\vec v}D_{\vec v}h(v)\right)\delta_v.
\tag{3.6}$$
图高度由 (3.5) 和 $\widehat h_F(b)=0$ 唯一确定。

为避免混用原文 §1 的 $v_p(p)=1$ 与 §3 的整数交数记法，可以先在整数边长 $\operatorname{ord}_K(\text{节点参数})$ 下应用公式，然后把全部边长和函数值同时除以 $e$。投影 $\pi$ 不变，长度配对除以 $e$，密度相应乘 $e$，顶点质量不变；逐项即得到 (3.5)。这正是 (3.2)，没有遗失另一个分歧因子。

该文脚注明确更正了 Betts–Dogra (2020), Corollary 12.1.3 的系数与长度错误；不能直接照抄旧公式。其 Remark 3.13 区分上同调作用与另行定义的图对应作用。本文只使用原始上同调形式，并且 (1.5)–(1.6) 在规范单值分次上为标量，因而不依赖一般图对应的推拉相容性接口。

## 4. 完整的图计算

置
$$S=\sum_j\frac1{L_j},\qquad q_j=\frac{1/L_j}{S},\qquad\sum_jq_j=1.$$

### 引理 2

对连接 $I_1$ 与 $D_j$ 的半边 $e$（另一条半边相同），
$$\langle e,\pi(e)\rangle=\frac{L_j}{2}(1-q_j).\tag{4.1}$$

**证明。** 将每条完整路径定向为 $I_1\to D_j\to I_2$。闭链恰为各路径上的常系数 $a_j$，满足 $\sum_ja_j=0$，其长度范数为 $\sum_j2L_ja_j^2$。半边 $e$ 首先正交投影到第 $j$ 条完整路径的 $1/2$ 倍。约束 $\sum_ja_j=0$ 的正交补由向量 $(1/L_j)_j$ 生成。减去该正交补分量后，第 $j$ 坐标为 $(1-q_j)/2$。与原半边取长度配对就给 (4.1)。证毕。

由 (1.5)、(3.5)、(4.1)，两条第 $j$ 半边上的密度都为
$$\gamma_j=\frac{\lambda}{L_j}(1-q_j),\qquad
\widehat h_F''=-\gamma_j.
\tag{4.2}$$
交换 $I_1,I_2$ 保持图和整个位势测度，因此唯一性使两点函数值相同，记为 $u$。以 $t\in[0,L_j]$ 从 $I_1$ 指向 $D_j$ 参数化，则
$$\widehat h_F(t)=u+\alpha_jt-\tfrac12\gamma_jt^2.$$
顶点 $D_j$ 有两条对称半边，(1.6)、(3.6) 给
$$2\widehat h_F'(L_j)=-2g_j,\qquad
\alpha_j-\gamma_jL_j=-g_j.$$
故
$$\widehat h_F(D_j)-u
=\frac{L_j}{2}\bigl(\lambda-2g_j\bigr)-\frac{\lambda}{2S}.
\tag{4.3}$$
最后一项对所有 $j$ 相同。对于 $j\ne0$，代入 $L_j=L$、$L_0=3L$ 以及两种亏格得
$$\begin{aligned}
\widehat h_F(D_j)-\widehat h_F(D_0)
&=\frac L2\left[
\lambda-\frac{p-1}{2}
-3\left(\lambda-\frac{p-5}{6}\right)\right]\\
&=-\frac{p-5}{2}L
=-\frac{2(p-5)}{p^2-1}.
\end{aligned}\tag{4.4}$$
这也给出所有一般超奇异标号上的值相同，并与 $j=0$ 值不同。

### 4.1 对任意真实方向的部分迹公式

上述图还给一个不要求 $F$ 为 (1.5) 的精确接口。设 $G$ 为任意 Rosati 对称、trace-zero 的有理 Hecke 方向，包括 R45 中通过 $A$ 的方向。记其图作用为 $G_\Gamma$，Drinfeld 部分迹为
$$\tau_j(G)=\operatorname{Tr}\bigl(P_{D_j}G\mid\operatorname{gr}_1^MH^1\bigr),$$
其中 $P_{D_j}$ 是中间分次中到 $H^1(D_j)$ 的规范直和投影；这一定义取 $G$ 的相应对角块之迹，不要求 $G$ 保持每个分量的上同调。

令 $e_j$ 为第 $j$ 条路径的任意一条定向半边，置
$$Q_j(G)=\langle e_j,G_\Gamma\pi(e_j)\rangle.
$$
两条同向半边在 $H_1$ 上的投影相同；对一个闭链，它们的系数也相同，所以所得 $Q_j$ 与半边选择无关。边密度为 $2Q_j/L_j^2$。不要求两个 Igusa 顶点的函数值相等，直接把两条边在 $D_j$ 的外向导数相加，得到
$$\widehat h_G(D_j)-\frac{\widehat h_G(I_1)+\widehat h_G(I_2)}2
=\frac{L_j}2\tau_j(G)+Q_j(G).
\tag{4.5}$$
因此经第 5–6 节同一个模型及尺度比较，对任意两个标签 $i,j$ 有
$$\boxed{\quad
k_j(G)-k_i(G)
=-d^2\left[L_j\tau_j(G)-L_i\tau_i(G)
+2Q_j(G)-2Q_i(G)\right].
\quad}\tag{4.6}$$

特别地，若 $G$ 通过潜在好约化因子的乘积，则 $G_\Gamma=0$，于是
$$k_j(G)-k_i(G)
=-\frac{p-1}{p+1}
\left[a_j\tau_j(G)-a_i\tau_i(G)\right].
\tag{4.7}$$
若 $G$ 只通过潜在全环面因子，则所有 $\tau_j=0$，只保留 (4.6) 的图项。一般方向的等式右边按两个全局因子作线性拆分；它的两个投影未必分别 trace-zero，因此这里仅拆分右侧泛函，不为各投影另行断言存在一个基点 QC 高度。这把实际范数修正的最终结果表达为真实单值分次上的线性泛函；它没有把任一项重新标作普通 Brandt 模块。

公式 (4.6) 给 R54 的 $\beta_j-\beta_i$ 的完整有限维算术接口：在 $A$ 的每个全局 Hecke 特征因子上计算实际的部分迹及图作用，然后用迹配对求其唯一表示。它仍需要这些真正的作用数据，不能以部分迹的总和或一个维数界代替。

## 5. 未分歧模型的末端分量确实映到这些顶点

现在把计算接回 R28、R43、R55 的确切未分歧正则模型。不能直接把其中重数一的末端 $F_j$ 叫作稳定模型的 Drinfeld 分量；这里要证明点的稳定特化位置。

Edixhoven–Parent (2024), Theorem 3.2 的证明，pp.1028–1029，在一般超奇异标号处使用
$$Y^2=X\bigl(X^{(p+1)/2}+a\bigr),\qquad a\ne0.$$
原点 $(0,0)$ 是光滑点，$Y$ 为局部参数。惯性在参数上的作用为 $Y\mapsto u^{p-1}Y$；消掉作用平凡的子群后，局部形式正是该文 (3.6) 的同权作用
$$\pi_1\longmapsto\zeta\pi_1,\qquad
y\longmapsto\zeta y,\qquad \pi_1^{p+1}=p.$$
其商奇点的解消中，重数一末端的仿射坐标是
$$Z=y/\pi_1,
\tag{5.1}$$
见该文 pp.1025–1026 的 (3.6)–(3.7) 及紧随其后的两个仿射图。末端只在 $Z=\infty$ 与其余纤维相交。

在 $j=0$，该文 p.1042 处理了额外自同构：曲线是
$$Y^2=X\bigl(X^{(p+1)/6}+a\bigr),$$
参数作用为 $Y\mapsto u^{3(p-1)}Y$。同样在去掉平凡子群后，用
$$\pi'_1=p^{3/(p+1)},\qquad Z=Y/\pi'_1
\tag{5.2}$$
得到唯一重数一末端的有限仿射图；其余固定轨道产生的是另一种重数的分量，并不是这里的末端。

因此若未分歧扩域上的点落在 R55 的 $U_j=F_j\setminus\{\infty\}$，则 $Z$ 为整数。将它送到半稳定扩域时，(5.1) 或 (5.2) 给 $y=\pi_1Z$ 或 $Y=\pi'_1Z$，所以其稳定特化为 $D_j$ 上的光滑原点。它不会落在连接 Igusa 的节点或边内部。

R55 所用的最终收缩在这个末端开集上为同构，因此该结论适用于收缩后真正的 $U_j$。由 R55，全部 $\mathbb Q_p$ 点都在这些光滑开集上；对几何分量可先作有限未分歧扩张，每一个末端开集亦有可提升点。由此 (4.4) 确实比较了 R43 的实际分量高度，而非另一模型上不可达的顶点值。

## 6. 回到 R43 的实际 $k$，只乘一次 $2F$

令 $D$ 为全部尖点除子，$d=(p-1)/2$。R43 的 $k_i(F)$ 来自
$$\mathscr L_F=(u_D,\,2h_{D,F}u_D)^*\mathcal P^{\rm ext}
$$
及其实际截面 $s_{D,F}^{\otimes2}$。因此乘二已经包含在 $k_i(F)$ 的定义中，不能在应用 (3.5) 时又把 $F$ 换成 $2F$。

R43 (4.4) 与 (3.4) 给
$$\frac{k_j(F)-k_0(F)}{2d^2}\log_\ell(p)
=-\log_\ell(p)\left(\widehat h_F(D_j)-\widehat h_F(D_0)\right).
$$
对有理素数 $p\ne\ell$，$\log_\ell(p)\ne0$：在 $\mathbb Q_\ell^\times$ 上该对数的核为根单位乘 $\ell$ 的整数幂，另一个正有理素数不在其中。也可在符号赋值配对层面直接比较系数。用 (4.4) 得
$$\begin{aligned}
k_j(F)-k_0(F)
&=-2d^2\left(-\frac{2(p-5)}{p^2-1}\right)\\
&=\frac{(p-1)(p-5)}{p+1},
\end{aligned}
$$
即 (0.1)。这里的 $d^2$ 来自 R43 的实际基点比较，负号来自其 $D_Z=-E_x$ 的配对符号，分母 $2$ 则来自唯一的一次积分倍增。

上述式子先对实际整数对应成立，再以线性性延拓到 $\mathbb T_{\mathbb Q}$。因此有理分母并不与垂直 Cartier 系数为整数冲突：取 $NF$ 为容许整数方向时，所求差就是 $N$ 倍 (0.1)，必为整数。

## 7. $p=41$ 时属于真实 Heegner 商的非零反例

### 7.1 使用的非消失输入是什么

Dogra–Le Fourn, *Quadratic Chabauty for modular curves and modular forms of rank one*, §5.3、p.429，明确报告：对所有 $N\le53$ 的相关非分裂正规化子曲线，平方水平 $+,{\rm new}$ 空间的每个特征形式均满足 $L'(f,1)\ne0$。紧邻的段落说明其用 MAGMA 作足够精度的非消失核验；随后调用 Proposition 8 得到无条件的秩等于维数。

这里使用的是论文明确作为已验证结论给出的**有限非消失输入**，不是从 BSD 猜测推断秩，也不是本文新作的未认证小数实验。论文该段没有逐个刊登区间证书；本文不声称已重跑其 MAGMA 计算或取得这些区间。依照仓库对已发表数学结果的通常使用方式，以该已发表结论作为输入即可。它使 R45 中按 $L'(f,1)\ne0$ 定义的 $A$ 在 $p=41$ 等于完整 $J$。

### 7.2 两个标签都可由真实局部点达到

除了 R9 的 CM 判别，亦可作一个完全有限的验证。在 $\mathbb F_{41}$ 上取
$$E_0:y^2=x^3+1,\qquad E_{28}:y^2=x^3+26x+31.$$
判别式均非零；第二条曲线的 $j$ 为 $28$。第一条曲线因 $x\mapsto x^3$ 在 $\mathbb F_{41}$ 上是双射，二次字符和为零。第二条曲线上，$x^3+26x+31$ 为非零平方的 $x$ 恰为
$$\{0,2,5,7,9,10,11,12,14,16,19,20,21,23,27,31,33,34,38,40\},$$
为零的 $x$ 只有 $29$，其余 $20$ 个值为非平方。因此两曲线均有 $42$ 个点，即 Frobenius 迹为零，所以均超奇异。两标号在 $\mathbb F_{41}$ 中且不同。R55 的提升定理于是给 $b\in U_0$、$x\in U_{28}$ 的 $\mathbb Q_{41}$ 点。

### 7.3 真正的非零值

此时
$$g=54,\quad r=3,\quad c=18,\quad d=20,\quad L=\frac1{420}.$$
公式 (4.4) 为
$$\widehat h_F(D_{28})-\widehat h_F(D_0)=-\frac3{70}.$$
故
$$k_{28}(F)-k_0(F)=\frac{240}{7},\qquad
h^{\rm Nek}_{F,41,b}(x)=\frac3{70}\log_\ell(41)\ne0.
$$
因为 $A=J$，R45 的满秩容许格包含 $NF$，其中 $N$ 为某个正整数；这里无需额外的互补商 Chow–Heegner 条件。取这个实际整数方向得到
$$\Phi_A(NF)\ne0,\qquad
NF\notin\mathcal K_{41,\mathbb Q_{41}}.
$$
在 R54 的迹配对表示下，同样有
$$\operatorname{Tr}\bigl(F(\beta_{28}-\beta_0)\bigr)=\frac{240}{7},
$$
所以 $\beta_{28}\ne\beta_0$。这是对**真实高度及真实可达分量**的反例，不能由不同模型之间的符号选择或共同常数消掉。

## 8. 为什么 level-$p$ Brandt 谱不能取代本计算

R33 的实际系数一般为
$$k_j(F)=6n+d\left[a_j(H_{jj}(F)-\nu_j(F))-2\tau_j(F)\right].
\tag{8.1}$$
$H_{jj}$ 是纤维多次数的一部分，$\nu_j$ 来自实际对角拉回，$\tau_j$ 是尖点范数缺陷。只有 R33 指定的小次数条件下，某些项才有简化。$\Phi_A$ 是线性映射，但这并不使它成为到 Brandt 模块的 Hecke 模同态；其源 trace-zero 超平面一般也不是 Hecke 理想。

更直接地，半稳定图公式包含各顶点的部分迹。若 $P_v$ 是分量上同调的投影，则
$$\operatorname{tr}_v(F)=\operatorname{Tr}(P_vF).
$$
对任意算子 $T$，$\operatorname{Tr}(P_vTF)$ 包含不同分量之间的矩阵块，不能只由各 $\operatorname{Tr}(P_wF)$ 和一个未经证明的 Brandt 作用恢复。光有两个已知谱的互不相交，不给这种实际部分迹映射的 intertwining 性质。

尤其在 $p=41$，$J$ 已完全属于平方水平新部分，而第 7 节仍给真实的 $\Phi_A\ne0$。因此，从新旧谱分离直接推导坏高度消失的论证已被反例否定。要进一步减少 R55 的有限靶集，必须证明更具体的实际对应恒等式或算术约束。

## 9. 已核查的原始来源与结论边界

- B. Edixhoven and P. Parent, **Semistable reduction of modular curves associated with maximal subgroups in prime level**, *Documenta Mathematica* **26** (2021), 231–269，DOI [10.4171/DM/814](https://doi.org/10.4171/DM/814)，[作者保存的原刊 PDF](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)。Theorem 3.5，pp.249–251：实际图、两种 Drinfeld 方程、节点厚度与环面秩；Remark 3.8，pp.251–252：Igusa 与总亏格。
- B. Edixhoven and P. Parent, **Regular models of modular curves in prime level over $\mathbb Z_p^{\rm ur}$**, *Documenta Mathematica* **29** (2024), 1017–1058，DOI [10.4171/DM/974](https://doi.org/10.4171/DM/974)，[原刊 PDF](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)。pp.1025–1026 的 (3.6)–(3.7)、Theorem 3.2 证明 pp.1028–1029、$j=0$ 分析 p.1042：末端分量的实际坐标与稳定原点；Theorem 3.4、Corollary 3.2：未分歧模型与收缩。
- L. A. Betts, J. Duque-Rosero, S. Hashimoto and P. Spelier, **Local heights on hyperelliptic curves and quadratic Chabauty**, *Transactions of the American Mathematical Society, Series B* **13** (2026), 240–300，DOI [10.1090/btran/242](https://doi.org/10.1090/btran/242)。本次逐式核对的 [arXiv v3（2025-05-21）](https://arxiv.org/html/2401.05228v3) 的 §1–§3、Theorem 3.11、Remark 3.13，给归一化度量和更正后的局部高度公式；该公式适用于一般光滑曲线，后续算法的超椭圆限制不限制此处定理。
- L. A. Betts and N. Dogra, **The local theory of unipotent Kummer maps and refined Selmer schemes**，[arXiv v2](https://arxiv.org/abs/1909.05734v2)（2020），§12.1、Corollary 12.1.3、Remark 12.1.4：上同调形式与 Néron 配对接口。数值系数按上一条的更正版使用。
- N. Dogra and S. Le Fourn, **Quadratic Chabauty for modular curves and modular forms of rank one**, *Mathematische Annalen* **380** (2021), 393–448，DOI [10.1007/s00208-020-02112-3](https://doi.org/10.1007/s00208-020-02112-3)，[KCL 保存的出版版 PDF](https://kclpure.kcl.ac.uk/ws/portalfiles/portal/147929133/QuadraticChabautyForModular_DOGRA_Accepted_26_Oct_2020_GOLD_VoR.pdf)。§5.3，p.429（含封面 PDF 第 38 页）：所用 $N\le53$ 的全部新形式非消失；Proposition 8：从非消失到无条件秩结论。
- 仓库 R33、R43、R45、R54、R55：实际范数项、一次积分倍增和 $d^2$ 比较、全局 Hecke 格、有限谱靶、真正可达分量。

本文的贡献是明确的全局有理方向、相容于未分歧实际模型的闭式高度差，以及 $p>37$ 范围内真实 Heegner 商的非消失反例。它不证明 O5 的辅助素数共同根排除，也不把这一反例当作 Serre 一致性的反例。
