# Bertrand 单点高度与完成后的严格 Mordell–Weil 线

**可信度：下述局部及基变换命题已证明；文献应用范围核查。** 日期：2026-11-12。记号同 R34–R36。本笔记不给新的跨素数非零结论。

## 1. 严格线不能通过有限基变换变成一个实际点

取 $E:y^2=x^3-17x$，$K=\mathbb Q(i)$，普通分裂素数 $p\ge13$、$p\ne17$，固定 $K\hookrightarrow K_{\mathfrak p}=\mathbb Q_p$。置 $V_\pi=T_\pi E\otimes\mathbb Q_p$，并令
$$
v_p=\ell_Q\kappa_\pi(P)-\ell_P\kappa_\pi(Q),
\qquad \ell_R=\log_E(R),
\quad P=(-1,4),\ Q=(9,24).
$$
R35 证明 $v_p\ne0$，且 $\operatorname{loc}_{\mathfrak p}(v_p)=0$。

**命题。** 对任意有限扩张 $F/K$、任意 $w\mid\mathfrak p$ 和任意非挠点 $R\in E(F)$，其有理化 $\pi$-Tate–Kummer 类不属于
$$
\mathbb Q_p\operatorname{res}_{F/K}(v_p)
\subset H^1(F,V_\pi).
\tag{1.1}
$$

**证明。** 在局部域 $F_w$ 中，$E(F_w)$ 是紧的 $p$-进 Lie 群。取其一个足够小的开子群，使形式对数在该子群上单射；该子群的指数有限。故局部椭圆对数的核恰为挠子：若 $\log_E R=0$，先以一个整数将 $R$ 移入这个开子群，再由形式对数单射得到该倍数为零。

在所选 $w$ 处，$[\pi]$ 在 Lie 代数上是乘以非单位 $\pi$。因此 $\pi$-完备化张量 $\mathbb Q_p$ 后由形式对数识别为 $F_w$；有限分支群和有限挠子不贡献。局部 Kummer 映射
$$
E(F_w)^{\wedge\pi}\otimes\mathbb Q_p
\hookrightarrow H^1(F_w,V_\pi)
$$
是单射。非挠 $R$ 在 $E(F_w)$ 中仍非挠，所以它的局部 Kummer 类非零。

但 (1.1) 的每个元素在 $w$ 处局部化为零，由限制与局部化的相容性即得矛盾。另由 $\operatorname{cor}\operatorname{res}=[F:K]$，$v_p$ 的限制在有理化上仍非零。证毕。

特别地，更换有限数域不能把这个严格完成方向变成 Bertrand 单点定理的输入。这里的限制来自局部化为零，不是没有找到合适的代数点。

## 2. 代数系数也不能表示这条方向

supersingular-attempt 笔记 §5.2 已由 Fuchs–Pham 的 $p$-adic 解析子群定理证明：两个 $\ell_P,\ell_Q$ 在所选 $\overline{\mathbb Q}\hookrightarrow\mathbb C_p$ 上线性无关。该论证只要求两个点在 $\operatorname{End}(E)=\mathbb Z[i]$ 上独立，亦适用于这里的普通素数。因此
$$
\ell_Q/\ell_P\notin\overline{\mathbb Q},
\qquad
\mathbb C_p v_p\cap
\bigl(\overline{\mathbb Q}\kappa_\pi(P)
+\overline{\mathbb Q}\kappa_\pi(Q)\bigr)=\{0\}.
\tag{2.1}
$$
第二式由比较 $P,Q$ 两个坐标立即推出。这比“没有固定有理方向”更强：对每一个所列 $p$，该线本身都没有非零代数坐标向量。它不排除某个高度值通过另一种恒等式化为代数系数的线性形式；这样的恒等式需要另证。

## 3. Rubin Appendix A 的实际输入

Agboola–Howard 的已出版论文附 Rubin 的 Appendix A。其 Theorem A.1 引用 Bertrand：CM 普通设置下，实际非挠代数点的单 $\mathfrak p$ 方向高度非零。Lemma A.2 比较 cyclotomic、anticyclotomic 和单 $\mathfrak p$ 三个高度。Theorem B 的证明另外使用根数 $-1$：在足够高的反圆分层找到实际非挠点，其两个 Tate 分量均为普遍范数；反圆分高度为零，再由 Bertrand 推出 cyclotomic 高度非零。

本题曲线的根数为 $+1$，且 (1.1) 证明严格线不能以这种实际点替换。Appendix A 的开头也明确区分单点非零和整个配对非退化。故本文没有从该定理推出 $G_p(p)\ne0$，也没有推出严格高度的非零。

对任意实际双线性高度 $h_p$，在 $P,Q$ 上写矩阵 $H_p=(h_p(P_i,P_j))$，则严格向量的自配对只能先写为
$$
h_p(v_p,v_p)=
\ell_Q^2H_{11}
-\ell_P\ell_Q(H_{12}+H_{21})
+\ell_P^2H_{22}.
\tag{3.1}
$$
若配对对称，中间项为 $-2\ell_P\ell_QH_{12}$。这不是已知的代数系数对数线性形式；(2.1) 尤其不允许把严格向量的两个系数视为代数常数。R36 的 $G_p(p)$ 与完整高度 regulator 的比较仍须保留各自定理的 Selmer 和非退化条件，不能仅由形式上的“二阶”将二者认作无条件相等。

## 来源

- A. Agboola、B. Howard，附 K. Rubin，*Anticyclotomic Iwasawa theory of CM elliptic curves*，Ann. Inst. Fourier **56** (2006)，1001–1048，Appendix A，Theorem A.1、Lemmas A.2/A.4、Proposition A.8 及 Theorem B 的证明。[出版页](https://www.numdam.org/item/?id=AIF_2006__56_4_1001_0)；[作者全文](https://web.math.ucsb.edu/~agboola/papers/cm1-final.pdf)。作者版 pp.32–35。
- D. Bertrand，*Propriétés arithmétiques de fonctions thêta à plusieurs variables*，*Number theory, Noordwijkerhout 1983*，Lecture Notes in Math. **1068** (1984)，17–22。这里使用前条已发表 Appendix A 的准确定理陈述，不声称重新证明 Bertrand 的超越性定理。
- C. Fuchs、D. H. Pham，*Some applications of the p-adic analytic subgroup theorem*，Theorems 1.1、2.2，[作者全文](https://arxiv.org/pdf/1412.1248)。具体点的独立性及应用已写在 supersingular-attempt 笔记 §5.2。
