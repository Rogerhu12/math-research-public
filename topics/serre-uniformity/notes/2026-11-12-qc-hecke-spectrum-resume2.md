# O5 续研：实际坏高度、Hecke 谱与潜在好约化

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

本笔记承接 R54–R55。父会话负责同步和共享索引；本分支只写独立文件。此次完整新结果为 [R57](../results/R57-new-hecke-spectrum-does-not-kill-bad-height.md)。尚未证明随层辅助共同根排除，O5 仍开放。

## 1. 所检验的具体推论

R33 的几何分量按超奇异 $j$ 标号，小 Hecke 的纤维多次数与 level-$p$ Brandt 矩阵有关；另一方面 R45 的真实 Heegner 商 $A$ 来自 level-$p^2$ 的新部分。自然的问题是：能否以不同水平的新旧谱分离，证明全部实际垂直修正 $\Phi_A$ 消失，从而把 R54 的有限靶集缩成一个点？

这个推论缺少一个本质接口。实际系数是
$$k_j(F)=6n+d\left[e_j(H_{jj}(F)-\nu_j(F))-2\tau_j(F)\right],$$
其中有对角拉回 $\nu_j$ 和尖点范数 $\tau_j$。$F\mapsto k(F)$ 的加法性并非一个 Hecke 模同态性质；取矩阵对角、对应对角拉回以及规范平移都需要独立核实与复合的相容性。尤其 trace-zero 超平面本身一般不在 Hecke 乘法下稳定。

这一缺口并非仅靠补一条标准引理就能消除：R57 在 $p=41$ 的真实 $A=J$ 上给出了非零实际坏高度，故拟议的全面谱消失结论确实为假。

## 2. 从 $p=17$ 的文献现象到 $p=41$ 的实际反例

Balakrishnan–Dogra–Müller–Tuitman–Vonk, *Quadratic Chabauty for modular curves: algorithms and examples*, Compositio Mathematica 159 (2023), §5.5，已经讨论 $X_{\rm ns}^+(17)$ 的非平凡坏高度。其 $H^1$ 按惯性型分为维数对应 $1,2,3$ 的三个部分；环面因子维数为 $1$。这首先说明完整平方水平新 Jacobian 不会自动有常坏高度。

但课题所要处理的是 $p>37$，所以不能只引用 $17$ 结束这个检验。此次采用同一结构而完全重做图计算，取 $p=41$。需要解决四个实际接口：

1. 不能把局部 Raynaud 投影擅自称为有理 Hecke 幂等元；
2. 不能把分歧稳定 Drinfeld 分量与 R55 的未分歧重数一末端混同；
3. 不能混用整数节点厚度、$v_p(p)=1$ 长度和高度字符；
4. 必须有 $A=J$ 的无条件非消失输入。

R57 分别在 §§1、5、3与6、7.1 解决这些问题。

## 3. 真正全局的潜在环面投影

若 $A_f$ 的维数是 $d_f=[K_f:\mathbb Q]$，则 $K_f$ 对半稳定环面特征空间的作用含单位。非零特征空间为一个 $K_f$ 向量空间，故其有理维数是 $d_f$ 的倍数；另一方面环面秩至多 $d_f$。因此一个全局新形式因子在半稳定扩域上要么完全环面，要么好约化。

选择所有完全环面因子的完整 Galois 轨道，就在
$$\mathbb T_{\mathbb Q}=\prod_{[f]}K_f$$
中取得 $e_{\rm tor}$。这是全局因子选择，因而定义于 $\mathbb Q$，且保持 Rosati 对称性。它在图同调上恒等，在全部分量 Jacobian 的上同调上为零。

对于 $p\equiv5\pmod {12}$，已知
$$r=\frac{p-5}{12},\qquad g=\frac{(p-5)^2}{24}.$$
令
$$F=\frac gr e_{\rm tor}-1=\frac{p-5}{2}e_{\rm tor}-1.$$
这就在完整 Jacobian 上给一个真正的 trace-zero Hecke 方向，不需要计算高次数投影多项式。

## 4. 数值系数审计与闭式公式

正确图有两条 Igusa 竖分量，以及每个超奇异标号对应的一条两半边路径。每条一般半边长度
$$L=\frac4{p^2-1};$$
$j=0$ 的半边长为 $3L$。原文的整数节点厚度为 $2$ 或 $6$，全分歧度 $(p^2-1)/2$；分歧因子不能遗漏。

这里特别使用 Betts–Duque-Rosero–Hashimoto–Spelier, *Local heights on hyperelliptic curves and quadratic Chabauty*, arXiv:2401.05228v3，Theorem 3.11 的更正公式。它在脚注明说更正原 Betts–Dogra Corollary 12.1.3 的系数问题。原公式不能不加调整地直接用于本次数值结论。

令 $\widehat h$ 为整数交数除以分歧度，所有长度均用 $v_p(p)=1$。则边密度与顶点质量的计算给
$$\widehat h_F(D_j)-\widehat h_F(D_0)
=-\frac{2(p-5)}{p^2-1}\qquad(j\ne0).$$
R43 的准确符号为
$$h^{\rm Nek}_{F,p,b}=-\log_\ell(p)\widehat h_F,\qquad
h^{\rm Nek}_{F,p,b}=\frac{k_j(F)-k_0(F)}{2d^2}\log_\ell(p),$$
其中 $d=(p-1)/2$。所以
$$k_j(F)-k_0(F)=\frac{(p-1)(p-5)}{p+1}.$$

这里 $k(F)$ 已由实际线 $(u_D,2h_{D,F}u_D)^*\mathcal P^{\rm ext}$ 定义，故没有第二次把图算子翻倍。若改用 R54 的 $G=2F$，则实际高度和图算子都线性翻倍，而 $k(F)$ 的既定含义不变。

在 $p=17$，同一公式给 $\widehat h$ 差 $-1/12$、$k$ 差 $32/3$，与必须先清 Hecke 分母的事实一致。在 $p=41$，它给
$$\widehat h\text{ 差}=-3/70,\qquad k\text{ 差}=240/7.$$
有理方向的分数系数没有违反实际 Cartier 除子整性：乘 $N$ 进入容许整数格后，所有实际系数同步乘 $N$。

## 5. 从稳定顶点回到 R55 的可达末端

Edixhoven–Parent (2024) 的商奇点解消给一个具体局部坐标，而不只给关联图。在一般标号的稳定 Drinfeld 原点，参数 $y$ 与 $\pi_1=p^{1/(p+1)}$ 具有同一惯性权。重数一末端的有限坐标为 $Z=y/\pi_1$。

在 $j=0$ 的特殊自同构商，参数 $Y$ 与 $\pi'_1=p^{3/(p+1)}$ 具有同一惯性权；末端坐标为 $Z=Y/\pi'_1$。两种末端均只在 $Z=\infty$ 与其余特殊纤维相交。

所以真正未分歧局部点若落在末端光滑开集，其 $Z$ 为整数，稳定基变换后参数趋于零，特化在相应 $D_j$ 的光滑原点。它不会落在图的边内部。这使高度图函数中的顶点值准确对应 R43 的 $k_j$。

引用位置：该文 (3.6)–(3.7)，pp.1025–1026；Theorem 3.2 证明 pp.1028–1029；粗模 $j=0$ 的处理 p.1042；最终收缩是 R55 已用 Corollary 3.2。

## 6. $p=41$ 非消失输入的可信度

Dogra–Le Fourn 的出版版 §5.3、p.429 明确给出所有 $N\le53$ 的相关特征形式 $L'(f,1)\ne0$，并说明先按 Galois 轨道计算，再利用 Gross–Zagier 的共轭非消失性质。它将这项 MAGMA 核验作为无条件结果，并用 Proposition 8 得秩等于维数。

本次没有自行生成那些 L 值的区间证书，也没有把浮点小数升级为证明；所用输入就是原论文明确断言的已验证非消失。它使 R45 按非消失选取的商在 $p=41$ 为全部 $J$。如果将来追查该有限计算的实现，可以回溯其 MAGMA 脚本与误差控制；这不是此处新添加一个 BSD 或秩猜测假设。

为了不再引入一个类数计算，R57 直接在 $\mathbb F_{41}$ 数点验证 $j=0$ 与 $j=28$ 都超奇异。由 R55，它们都有真正 $\mathbb Q_{41}$ 点。这给 $\Phi_A\ne0$，也给 R54 的 $\beta_{28}\ne\beta_0$。

## 7. 比非零反例更一般的实际接口

R57 §4.1 同时推导了任意 trace-zero Hecke 方向 $G$ 的公式：
$$k_j(G)-k_i(G)
=-d^2\left[L_j\tau_j(G)-L_i\tau_i(G)+2Q_j(G)-2Q_i(G)\right],$$
其中
$$\tau_j(G)=\operatorname{Tr}(P_{D_j}G\mid\operatorname{gr}_1^MH^1),\qquad
Q_j(G)=\langle e_j,G_\Gamma\pi(e_j)\rangle.$$
它不需要两个 Igusa 顶点的值相等，也不需要一般 Hecke 算子保持单个 Drinfeld 上同调块。

若 $G$ 通过潜在好约化因子，则图作用为零，简化为
$$k_j(G)-k_i(G)
=-\frac{p-1}{p+1}
\bigl[a_j\tau_j(G)-a_i\tau_i(G)\bigr].$$
这是一个真实的有限维算术计算目标：将全局 Hecke 因子作用搬到规范单值分次，求出各 Drinfeld 部分迹，再用 R54 的迹配对识别 $\beta_j$。现有工作还没有得到这些部分迹随全部大层的闭式式子。

## 8. 潜在好约化到底能给什么

对 $p>37$，Edixhoven–Parent (2021), Theorem 3.5 给：

- $p\equiv1\pmod4$ 时潜在环面秩为 $g(X_0(p))>0$，故 $J_{\rm ns}^+(p)$ 不是潜在好约化；
- $p\equiv3\pmod4$ 时图为树，Jacobian 潜在好约化。

后一个条件不能单独使 QC 坏高度为常数。树没有边上的二次密度，但仍有
$$\nabla^2\widehat h_G=\sum_v\tau_v(G)\delta_v.$$
函数在整棵树上为常数，当且仅当每一个顶点质量为零；总体 trace-zero 只给这些质量之和为零。原 Betts–Dogra §12.2.1 讨论 $X_{\rm ns}^+(p)$ 的树情形时，也准确要求各分量迹为零。

这也解释必须区分“曲线潜在好约化”和“Jacobian 潜在好约化”。前者的稳定图只有一个有正亏格的顶点，trace-zero 即足以；后者可有多个正亏格顶点，彼此间的分段仿射高度仍会变化。

文献中的实际例子可见 Balakrishnan–Dogra–Müller–Tuitman–Vonk (2023), Example 3.3 与 Example 5.18：$C_{188}$ 在 $2$ 处经过分歧扩张有树形、两个亏格一顶点的约化，而真实坏高度取多个值。这里只把它用作该区分的已发表例证，R57 的反例不依赖它。

## 9. 下一项正在检验的算术结构

还有一个值得进一步核查的现象：潜在全环面新形式通常与 level-$p$ Steinberg 形式的二次扭曲相关。若要把图作用与 Brandt 模块比较，可能出现 $\left(\frac qp\right)T_q$ 而不是普通 $T_q$。这会从表示论上说明为什么平方水平新谱并不被普通 Brandt 谱消失论证杀掉。

目前仅把这条写为待核查结构，尚未登记结论。需给出以下之一：

1. 全局新形式的精确二次扭曲分类及 Fricke 符号，然后用单值表示识别；
2. 在 Edixhoven–Parent 模型上，跟踪真实 $T_q$ 对两条 Igusa 分量及路径方向的作用，证明是否出现 Legendre 符号。

不以“这应当是某个 twist”替代实际 Hecke 模同态。即便证明该环面块的扭曲 Brandt 识别，R57 (4.6) 的 Drinfeld 部分迹仍然存在，不能自动推出 $\Phi_A$ 消失或辅助共同根排除。

## 10. 本轮后仍未解决的核心

R55 已把真实可达靶数降到 $O(\sqrt p\log p)$；R57 证明该靶集一般确实有不同的值，且给其精确单值上同调接口。接下来需要实际控制 $\Delta_\ell$ 对这些靶的逆像，或引入有理点独有的跨素数条件。代数独立、次数增长、单个坏素数的有限靶、局部可达性均不能单独排除额外共同根。上述限制是数学上尚缺的结论，不是等待批准或结束研究的门槛。
