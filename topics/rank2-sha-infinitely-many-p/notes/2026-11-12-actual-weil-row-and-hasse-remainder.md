# 实际 Weil 行对 Hasse 低权余式的约束

日期：2026-11-12。状态：下面的低权投影与条件命题已证明。
本篇不预设所讨论的 Hasse 分解存在，也不推出实际中央值恒为零。

## 1. 要检验的具体分解

沿用[临界热导数](2026-11-12-inert-critical-heat-derivative.md)的
$F,R_n,V_p$。对惰性素数 $p\ge7$，置
$N_p=(p+1)/2$、$\epsilon_p=(2/p)$，并记
\[
 A_p=E_{p-1},\qquad B_p=E_{p+1}.
\]
实际整形式为
\[
 V_p=\frac{R_{N_p}
       -\epsilon_p(A_pR_1+B_pF/24)}p,
 \qquad \mathrm{wt}(V_p)=p+\tfrac32.                 \tag{1}
\]
一个尚未建立的候选是：在原固定 level、原 multiplier 下，
\[
 \overline V_p
     =\overline A_p\,H+\overline B_p\,G,\qquad
 H\in M_{5/2},\quad G\in M_{1/2}.                    \tag{2}
\]
横线表示同权整形式的模 $p$ 约化。这里必须要求 $H,G$ 在所有
cusps 全纯；允许弱全纯形式会改变下述结论。

本篇证明：对经典整形式的约化，(2) 必迫使它的实际 CM 行为零。
对几何定义的全部模 $p$ 低权形式，同样结论在一个固定有限例外集
以外成立。理由不是假定 $G$ 一开始就在原单个 theta 的张成空间，
而是先保留完整有限 Weil 作用，再把标量分解平均成向量分解。

## 2. 不丢有限标签的实际行

为避免与 $N_p$ 混淆，固定写
\[
 M=578=2\cdot17^2,\qquad
 \mathcal D=\mathbb Z/1156\mathbb Z,\qquad
 Q(r)=\frac{r^2}{2312}\pmod{\mathbb Z}.
\]
其正定 rank-one Weil 表示记为 $\rho_M$，标准 theta 向量为
\[
 \Theta_M(\tau)=
 \sum_{r\bmod1156}\ \sum_{n\equiv r\ (1156)}
       q^{n^2/2312}\,\mathbf e_r.                   \tag{3}
\]
这就是偶格 $34\mathbb Z$、二次型 $x^2/2$ 的 theta 向量。

设原固定权重为
\[
 a_n=\lambda(n)\zeta_{289}^{19n^2}
 \quad(17\nmid n),\qquad a_n=0\quad(17\mid n),
 \qquad\lambda(3)=-i.
\]
它的周期为 $289$，且 $a_{-n}=a_n$。定义固定线性行
\[
 \ell(\mathbf e_r)=
 \begin{cases}
 a_{r/2},&2\mid r,\\
 0,&2\nmid r .
 \end{cases}                                      \tag{4}
\]
由于 $r/2$ 只差 $578$，这一定义良定。直接把 $r=2n$ 代入 (3)，得
\[
 \ell\Theta_M
   =\sum_{n\in\mathbb Z}a_nq^{n^2/578}=F.            \tag{5}
\]
因此 (4) 保留了原来的所有 $289$ 个有限余类、四次角色及二次相位；
没有把实际 $F$ 换成无角色参考 theta。

对 $\Theta_M$ 的每个分量使用 (1) 的同一 Serre 递推，得到向量
$\boldsymbol V_p$，并有
\[
 \ell\boldsymbol V_p=V_p.                           \tag{6}
\]
它确实是整的 $\rho_M$-值形式。因为每个 Fourier 指数都是
$n^2/(8\cdot17^2)$，原来的平方支撑计算给出同一个
$\epsilon_p=(2/p)$；逐分量有
$D^{N_p}\Theta_M\equiv\epsilon_pD\Theta_M\pmod p$。
Weil 矩阵的分母仅来自 $2,17$，所以同一整性在变换后的 cusps 保持。

## 3. 权 $1/2$ 的三项基及实际投影

Bruinier–Schwagenscheidt **2017** 的 Lemma 2.1 给出
$M_{1/2}(\rho_M)$ 的全部基，索引为 $M$ 的因子模 $c\sim M/c$。
此处可取 $c=1,2,17$，得到
\[
 \Theta_M,\qquad \Theta_M^{\sigma_2},\qquad
          \Theta_2\mid U_{17}.                     \tag{7}
\]
原文的 $\rho_M$ 是正二次型的 Weil 表示，正好与 (3) 一致；
不是其复共轭表示。

三个基向量的实际投影完全显式：

1. $\ell\Theta_M=F$。
2. $\sigma_2(r)\equiv-r\pmod4$、$\sigma_2(r)\equiv r\pmod{578}$，
   故 $\sigma_2(r)=579r\pmod{1156}$。
   当 $r$ 为偶数时它固定 $r$，当 $r$ 为奇数时 $\ell$ 本来为零。
   所以 $\ell\Theta_M^{\sigma_2}=F$。
3. $\Theta_2\mid U_{17}$ 只在 $17\mid r$ 的分量有支撑；
   (4) 在这些分量全部为零。因此
   $\ell(\Theta_2\mid U_{17})=0$。

于是
\[
 \boxed{\quad
 \ell M_{1/2}(\rho_M)=\mathbb C F.
 \quad}                                           \tag{8}
\]
这不是说任意标量低权形式都等于 $cF$；它是对完整 Weil 型的精确结论。

(7) 还给一个饱和的 Fourier 整格。
取系数 $[q^{1/2312}\mathbf e_1]$、
$[q^{1/2312}\mathbf e_{579}]$ 和 $[q^0\mathbf e_0]$，
三个基上的矩阵为
\[
 \begin{pmatrix}
 1&0&0\\0&1&0\\1&1&1
 \end{pmatrix},\qquad\det=1.                       \tag{9}
\]
因此经典 $\rho_M$-值形式若所有 Fourier 系数都在某个局部整数环，
它在 (7) 中的三个坐标也整；这里没有未知的大分母。

## 4. 从标量分解到 Weil 型分解

以下短引理处理 (2) 中没有事先要求的协变性。

**平均化引理。** 设 $k$ 的特征不整除一个有限群 $\mathcal G$ 的阶。
设 $U$ 是有限维 $k[\mathcal G]$-模，
$\alpha:U\to Y$ 是等变映射，
$L:X_1\oplus X_2\to Y$ 也是等变映射。
若 $u_0\in U$ 且 $\alpha(u_0)\in\operatorname{im}L$，
则存在等变映射 $\beta:U\to X_1\oplus X_2$，使
\[
 L\beta(u_0)=\alpha(u_0).                           \tag{10}
\]

**证明。** 令 $C=k[\mathcal G]u_0$。
由于 $\operatorname{im}L$ 稳定，$\alpha(C)$ 包含于其中。
Maschke 定理使 $C$ 为半单模，故映射
$C\to\operatorname{im}L$ 可穿过 $L$ 等变提升。
再取等变投影 $U\to C$，复合即得。这里没有要求
$L\beta=\alpha$ 在整个 $U$ 上成立，也没有要求 $U$ 不可约。$\square$

取一个固定正规 metaplectic congruence 子群
$\widetilde\Gamma\subset\ker\rho_M$，并同时细化原标量 level。
在特征不除有限商阶时，该商 $\mathcal G$ 作用于各权的模形式空间。
可在 (3) 的 level $2312$ 之上这样选择；需要排除的群阶素因子固定，
在这个自然 Weil level 上只有 $2,3,17$。

将引理用于
\[
 U=\rho_M^\vee,\quad u_0=\ell,\quad
 \alpha(u)=u\boldsymbol V_p,\quad
 L(H,G)=\overline A_pH+\overline B_pG.              \tag{11}
\]
两个 Eisenstein 因子是 level-one 形式，所以 $L$ 确实等变；
它们各自的权一起随 slash 作用变换，不能只在 Fourier 级数中
把 $\overline A_p$ 换成常数 $1$。

于是，若标量 (2) 成立，可以找到 $\rho_M$-值形式
$\boldsymbol H,\boldsymbol G$，使
\[
 \overline V_p
   =\overline A_p\,\ell\boldsymbol H
        +\overline B_p\,\ell\boldsymbol G.         \tag{12}
\]
若 $\boldsymbol G$ 属于 (7) 的约化空间，由 (8) 得到
\[
 \boxed{\quad
 \overline V_p
      =\overline A_p\,H_\ell
               +c_p\overline B_p\,\overline F .
 \quad}                                           \tag{13}
\]
$H_\ell$ 不要求等于某个 Serre 导数；整个 $M_{5/2}$ 都已允许。

## 5. 特征 $p$ 与固定有限例外集

这里有两种精确表述，不能混用。

**经典整约化。** 若 (2) 的低权空间指经典全纯形式、在全部 cusps
整的格之约化，则 (13) 对每个不除上述固定群阶及 level 的 $p$ 成立。
理由是有限群的 Reynolds 平均含分母 $|\mathcal G|$，在这些 $p$
处是单位；对自由整格 $U_{\mathcal O}$，
\[
 \operatorname{Hom}_{\mathcal G}
       (U_{\mathcal O},M_{1/2,\mathcal O})\otimes k
  \simeq
 \operatorname{Hom}_{\mathcal G}
       (U_k,M_{1/2,\mathcal O}\otimes k).           \tag{14}
\]
(14) 可直接由先任意提升线性映射、再平均证明。
所得到的向量低权形式确实提升到特征零，故可用 (7) 和饱和性 (9)。

**全部几何模 $p$ 形式。** 不能仅凭复数域基定理宣称每个 $p$ 都有 (7)。
不过存在一个与 $p$ 无关的有限集合 $\Sigma$，使 (7) 对所有
$p\notin\Sigma$ 的几何空间成立。具体地，在固定足够细的
compactified level 曲线上，半权形式由固定 theta divisor 的线丛描述；
Ramsey **2006** 的几何定义可用来取这一整模型。
固定 $M_{1/2}$ 的相干上同调是有限整模。由相干上同调的
derived base change，它可用一个固定有限自由复形计算。
删去这个复形在特征零消元时出现的有限分母后，$H^0$ 与剩余域
基变换交换。取有限群不变量也与约化交换，因为 $|\mathcal G|$ 可逆。
这证明所需有限 $\Sigma$；它仅用于固定低权空间，
没有依赖变动权 $p+3/2$ 的基变换断言。

本文未计算 $\Sigma$，所以不以此段单独排除某个小 $p$ 的
非提升几何形式。对经典整约化则不需要这项未计算的例外。

## 6. 真正的 CM 后果与边界

设 $x_{\mathrm{CM}}$ 是原 $\tau=i$ 的、带全部固定有限标签的
好约化点。所有值取在各自 Hodge/半权线的 fiber 内。
惰性 $p$ 时
\[
 \overline A_p(x_{\mathrm{CM}})=0,\qquad
 \overline F(x_{\mathrm{CM}})=0.                   \tag{15}
\]
第二式来自实际 $F(i)=0$，不是参考 theta 的值。
由 (13) 可得
\[
 \boxed{\qquad
 \text{若 (2) 成立，则 }
 \overline V_p(x_{\mathrm{CM}})=0.
 \qquad}                                         \tag{16}
\]
这使所提 Hasse 余式候选有了明确可检验的必要条件。
任何实际 CM 首层为单位的素数，在适用整格内都不可能有 (2)；
不能先证明 (2) 的存在，再期待其 $M_{1/2}$ 余项提供非零 CM 值。

(16) 只否定这种特定低权降阶作为非零证明的办法。
它不证明 (2) 存在，不证明 $V_p$ 本身为零，
也不否定其他固定几何对象、其他低权余式或完整高阶中央导数。
此前 $p=7$ 的非平方 Fourier 项检查只处理 $H=0$ 且原 unary
标量空间；本篇允许任意全纯 $H\in M_{5/2}$，
新增的约束来自原完整 Weil 型和实际行 (4)。

## 7. 准确的 CM 整格比较，以及 $p=7$ 的完整反例

本节补齐 (16) 与此前有理数值证书之间的整格比较。
不会仅由中央平方常数 $57800$ 推断某个未定 theta 标量为单位。
我们先证明一个实际同权模函数及其全部共轭整，再计算其精确乘积。

### 7.1 用 $\theta_3$ 的第四次幂固定几何整格

记
\[
 \theta=\theta_3(0\mid i)>0,\qquad
 f_2=\frac{\partial_{1/2}^{2}F(i)}{\theta^9}
     =\frac{R_2(i)}{\theta^9}.                    \tag{17}
\]
最后一式由临界热导数笔记的 (8) 及 $E_2^*(i)=0$ 得到。
对每个 $p\ge7$、$p\ne17$，$f_2$ 及它的全部代数共轭都在
$p$ 的各个上方素位整。证明如下。

先把固定 level 细化到同时包含 $\Theta_M$ 与 $\theta_3$ 的
multiplier 核。其素因子仍只有 $2,17$。
$R_2$ 的全部 cusp 展开整：有限 Weil 矩阵只除 $2,17$，
而 Serre 递推只再引入 $2,3$。取第四次幂，
\[
 \frac{R_2(\tau)^4}{\theta_3(0\mid\tau)^{36}}
                                                               \tag{18}
\]
就是一个经典整数权同权比，分子、分母的权都为 $18$。
因此可直接使用整数权的几何整模型及 $q$-expansion principle；
无需为一个抽象半权纤维另选未知共同比例。

若椭圆曲线的周期格为 $\Omega(\mathbb Z+\tau\mathbb Z)$，
DLMF 23.6.2–23.6.4 给
\[
 e_1-e_3=\frac{\pi_{\mathbb C}^{2}}{\Omega^2}
                   \theta_3(0\mid\tau)^4.          \tag{19}
\]
在标准 Tate 微分规范下，权二形式 $\theta_3^4$ 在代数微分
$\omega$ 上的值为 $-4(e_1-e_3)$。
在本题 $E$ 的好模型中，三个非零二挠点的横坐标是
$0,\sqrt{17},-\sqrt{17}$；它们在所有 $p\ne2,17$ 的约化中互异。
所以 (19) 的几何值是单位。任意共轭标签仅排列这些根，
仍给单位。由此 (18) 在全部这些 CM 整点处整。
其值为 $f_2^4$，故 $f_2$ 代数且整；同一论证适用于每个共轭。

上述过程也与 Ramsey **2006** §3、Theorem 4.2 的 theta-divisor
与 $q$-expansion 整模型一致。这里特别取第四次幂，是为了不把
解析半权框架与任意代数平方根框架的比例默认为单位。

### 7.2 不省略原有限向量的准确范数

本篇的 $a_n$ 是原 Gaussian 证明中删去共同常数后的 raw 权重。
[实结构证明](2026-11-12-theta-real-structure-and-mellin-square.md)
(12)、(15) 给原平均有限向量相对于它的共同标量 $c$：
\[
 A_0=\frac{\sqrt{17}}{16},\qquad
 c=\frac{A_0}{17}\,\mathfrak G(\lambda^{-1})\,\xi,
 \quad |\xi|_{\mathbb C}=1,
 \quad |\mathfrak G(\lambda^{-1})|^2=17.
\]
$2$ 处向量可明确取 $\mathbf1_{\mathbb Z_2}$，范数为一，
见 [dyadic 向量证明](2026-11-12-dyadic-vector-and-reference-theta.md)。
故准确地有
\[
                       c\overline c=\frac1{256}.    \tag{20}
\]
这不是任意重选有限向量后的规范。

原 Yang 平方公式、中央定义及 Hermite 热方程给
\[
 e_4=
 \frac{32\sqrt2\pi_{\mathbb C}}{17\Omega_E}
 \cdot\frac1{256}
 \left(\frac{\pi_{\mathbb C}}{2Nf\,\Omega_E^2}\right)^4
 B_4\overline{B_4},\qquad
 B_4=\frac{(16\pi_{\mathbb C})^2}{24}\,f_2\theta^9.
                                                               \tag{21}
\]
由 (19) 在 $E_0:y^2=x^3-x$ 上的正实规范，
\[
 \Omega_0=\frac{\pi_{\mathbb C}\theta^2}{\sqrt2},
 \qquad \Omega_E=\frac{\pi_{\mathbb C}\theta^2}
                         {\sqrt2\,17^{1/4}},
 \qquad Nf=8\cdot17^2.
\]
将这些量逐项代入 (21)，所有复周期消去，得到
\[
 e_4=\frac{f_2\overline{f_2}}{144\,17^{27/4}}.
\]
已有完整 $256$ 点精确迹证书给
$e_4=25/(2^9 17^{10})$，因而
\[
 \boxed{\quad
 f_2\overline{f_2}=\frac{225}{32\,17^{13/4}}.
 \quad}                                                   \tag{22}
\]
正实 $17^{1/4}$ 固定了这个复等式；它是代数数等式，
在任何有限位都可取赋值。§7.1 保证两个因子各自的赋值非负，
而 (22) 的右边在所有 $p\ge7$、$p\ne17$ 上为单位。
所以
\[
                         v_{\mathfrak p}(f_2)=0
 \quad(\mathfrak p\mid p,\ p\ge7,\ p\ne17).        \tag{23}
\]
这一步保留了两个因子的整性；单独知道乘积为单位是不够的。

### 7.3 真实 $V_p$ 纤维的单位判据

令 $\alpha=4-i$，沿用热导数笔记的
$h=\sqrt{\pi_{\mathbb C}/2}\,17/(\Omega_E\alpha)$。
置
\[
 C=(16\pi_{\mathbb C}h^2)\theta^4
   =\frac{16\,17^{5/2}}{\alpha^2}.                 \tag{24}
\]
它在所有 $p\ne2,17$ 上为单位。
对于 $N_p=(p+1)/2$，设实际归一纤维坐标
\[
 v_p^{\rm CM}=\frac{V_p(i)}{\theta^{4N_p+1}}.
\]
亦可只取其第四次幂：
$V_p^4/(\theta_3^4)^{4N_p+1}$ 是整数权同权比，
$\theta_3^4$ 在指定纤维为单位。
因此 $v_p^{\rm CM}$ 为单位等价于原 $\overline V_p$ 的该纤维非零。
热导数笔记 (16)–(17) 的有理归一准确给
\[
 \mathscr V_p=
       \frac{24C^{N_p-2}}{f_2}\,v_p^{\rm CM}
       =\frac{(p+1)!}{p}\,b_{p+1}.                 \tag{25}
\]
由 (23)–(24)，(25) 左边的比例在所列全部 $p$ 处是单位。
故本篇所需的几何比较已经完全付清：
\[
 \boxed{\quad
 \overline V_p(x_{\rm CM})\ne0
       \iff b_{p+1}\not\equiv0\pmod p
 \quad(p\equiv3\!\!\pmod4,\ p\ge7,\ p\ne17).
 \quad}                                                   \tag{26}
\]

最后取 $p=7$。实际截面证书给 $b_8=1649/60$，所以
\[
 \mathscr V_7=\frac{8!}{7}\frac{1649}{60}
              =158304\equiv6\pmod7.                \tag{27}
\]
因此原 $\overline V_7(x_{\rm CM})$ 非零。
结合 (16)，得到一个允许完整 $M_{5/2}$ 的明确反例：
\[
 \boxed{\quad
 \overline V_7\notin
 \overline E_6\,\overline M_{5/2}
       +\overline E_8\,\overline M_{1/2},
 \quad}                                                   \tag{28}
\]
其中横线低权空间指原固定 level/multiplier 上、全部 cusps 整的
经典全纯形式格之约化。$7$ 不除 §4 的有限群阶或 level。
(28) 不把 §5 未计算的几何基变换例外集排除在外：
它没有对可能不能提升的任意 Katz 权 $1/2$ 形式作额外断言。

## 8. 一手来源与核查位置

- J. H. Bruinier、M. Schwagenscheidt，
  *Algebraic formulas for the coefficients of mock theta functions and
  Weyl vectors of Borcherds products*，Journal of Algebra **478** (2017), 38–57。
  [作者全文](https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/bruinier/publikationen/UnaryThetaSeriesPaper-revision.pdf)。
  已亲读 §2.1，式 (3)–(5)、Lemma 2.1。
  该引理给特征零全部三项基；本篇的 (4)、(8)–(16) 是另行证明。
- N. Ramsey，*Geometric and p-adic Modular Forms of Half-Integral Weight*，
  Ann. Inst. Fourier **56** (2006), 599–624。
  [原出版全文](https://www.numdam.org/article/AIF_2006__56_3_599_0.pdf)。
  已亲读引言的 compactified $X_1(4N)$、theta divisor 与 $H^0$ 定义，
  及 §3、Theorem 4.2 的整模型与 $q$-expansion principle；
  细化固定 level 后仍是同一固定相干线丛问题。
- The Stacks Project（2026 年读取），
  [Lemma 30.22.1 与 Remark 30.22.2，Tag 07VJ](https://stacks.math.columbia.edu/tag/07VJ)。
  已亲读 proper、coherent、base-flat 的假设及固定 perfect complex
  的任意基变换结论。这里只用它证明存在固定有限坏素数集。

- NIST *Digital Library of Mathematical Functions*（2026 年读取），
  [23.6.2–23.6.4](https://dlmf.nist.gov/23.6#E2)。
  已亲读三个格根与 theta 常数公式；本篇 (19) 是其差。
  Yang **1997** 的原平方常数与实际有限向量已在
  [R46](../results/R46-fixed-sigma-section-and-central-mellin-factors.md)
  及上述实结构证明逐项核对；§7.2 保留 raw 权重的 $1/256$ 因子。
