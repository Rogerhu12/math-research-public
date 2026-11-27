# 原最高线与互素导子 Beilinson–Flach 输入

日期：2026-11-27；会话：Astra-rank2-Sha-0b097461-20261127。

这是 R1011 以后寻找固定循环跨素数非零输入的工作记录。不重新登记
原有对角 Euler system，不把一条类比较等式称为非零定理。

## 1. 新文献的准确用途

Raúl Alonso、Lois Omil-Pazos、Óscar Rivero，*Anticyclotomic diagonal
classes and Beilinson–Flach elements*，IMRN 2026(20), rnag236，
[发表页](https://doi.org/10.1093/imrn/rnag236)、
[公开 v1 全文](https://arxiv.org/pdf/2509.07564v1)。发表页日期为
2026-10-16；以下 v1 定理编号明确只指该版本。

正文把一条经过不规则权一 Eisenstein 点的 CM 家族作为辅助输入，
比较加权 Beilinson–Flach 类和对角类。两个保留下来的 cusp 家族
必须有互素 tame levels；发表稿 Assumption 5.0.1(i) 与 v1 §1.1
均明列这个条件。

v1 Theorem 1.1、Corollary 5.19 的全局类等式保留大 Selmer 模
无挠且秩一及相应大 $p$-adic $L$ 函数不恒零的前提。
v1 Corollary 5.25 的指定特化还保留该点的非零假设。
因此，即使能完成来源比较，也不能把大函数不恒零替换为本题
固定权、固定有限角色处在无穷多个 $p$ 非零。

## 2. 本题所有两个不可约因子 presentation 的共同导子障碍

下面的论证不依赖只检查某一组候选 newforms 的级别。
令 $K=\mathbf Q(\sqrt{-3})$，原最高字符为

$$
 \lambda=\eta_j^{-1}\chi_{27,\ell}^{\,3}\varepsilon_\ell^{-1}.
 \tag{1}
$$

它在 $K$ 的两嵌入处的 Tate 指数为 $(2,-1)$，差为 $3$；有限
角色不改变该差。取足够大的系数域，所有表示和字符都在其中定义。

**引理（已证明）。** 设 $U,W$ 是两个绝对不可约二维
$G_{\mathbf Q}$ 表示，来自 cusp newforms，并假定存在

$$
 \operatorname{Hom}_{G_K}
       \bigl(\lambda,U|_{G_K}\otimes W|_{G_K}(t)\bigr)\ne0
 \quad(t\in\mathbf Z).
 \tag{2}
$$

则 $U,W$ 都从 $G_K$ 的一维字符诱导。它们的导子都被 $3$ 整除。
特别在 $p\ne3$ 时，它们的 tame levels 不互素。

**证明。** 假设 $U|_{G_K}$ 不可约。张量–Hom 伴随把 (2) 变成
非零映射

$$
 U^*|_{G_K}\longrightarrow
 W|_{G_K}(t)\otimes\lambda^{-1}.
 \tag{3}
$$

源不可约而两边均二维，所以 (3) 是同构。取行列式，得到

$$
 \lambda^2=(\det U\cdot\det W\cdot\varepsilon_ell^{,2t})|_{G_K}.
 \tag{4}
$$

右边是一个 $G_{\mathbf Q}$ 字符的限制，它在 $K$ 的两嵌入处
有相同的 Hodge–Tate 指标。左边两个指标的差却为 $6$。
这是矛盾。因此 $U|_{G_K}$ 可约。

指数二正规子群上的 Clifford 分解给
$U\simeq\operatorname{Ind}_{G_K}^{G_{\mathbf Q}}\alpha$。
这里两个字符必须被非平凡共轭交换，否则其中一个一维子空间
已经被整个 $G_{\mathbf Q}$ 稳定，违反 $U$ 的不可约性。
把这个分解代回 (2)，可知 $W|_{G_K}$ 也含一维子表示；对 $W$
重复同一论证，得到所需的诱导表示。

最后在 $3$ 处选惯性元素 $s$，它在分歧二次扩张
$K_3/\mathbf Q_3$ 上的像非平凡。在诱导表示的两个陪集基中，
$s$ 交换这两个基线；其矩阵有非零的两个非对角元，因而不是
恒等矩阵。故两个表示在 $3$ 处的惯性作用都非平凡，Artin
导子指数均为正。对 newform 表示，这正说明其导子级别均含
$3$。当 $p\ne3$ 时，这个因子仍留在 tame level 中。证毕。

上面的绝对不可约假设与该文两个保留家族的剩余不可约条件相容；
不能用一个可约 Eisenstein 特化充当其中一个 cusp 因子而仍保留
该假设。辅助的权一 Eisenstein 因子是该文另外引入的第三因子，
不会消去 (2) 中两个因子的共同分歧。

## 3. 对当前工作留下的实际方向

R1011 的固定 $Y_{j,0}$ 与各 $p$-depletion 的严格 Chow 等式
保持。上面的引理只说明：直接套这份互素 tame level 比较来换成
两个 cusp 因子的 Beilinson–Flach 输入，需要新的共同分歧版本。
它不排除这样的推广，也不排除其他混合 CM 构造。

若走这条方向，须实际处理原共同 $3$ 型、原有限角色及两个
Selmer 条件，并另证固定点处的非零。当前没有用该文的比较式
删除这些条件，也没有把 R1009 的有限 $1$-motive 障碍扩大到
所有 Beilinson–Flach 或逆极限构造。
