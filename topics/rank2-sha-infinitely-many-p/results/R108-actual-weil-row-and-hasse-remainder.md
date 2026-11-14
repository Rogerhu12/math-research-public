# R108. 实际 Weil 行、Hasse 低权余式与 $p=7$ 的完整反例

日期：2026-11-12。**状态：已证明；不证明无限素数的中央非消失。**

## 1. 结论与精确整格

沿用 R53 的实际固定 theta 形式
\[
 F(\tau)=\sum_n a_nq^{n^2/578},\qquad
 a_n=\lambda(n)\zeta_{289}^{19n^2}\ (17\nmid n),\quad
 a_n=0\ (17\mid n),\quad\lambda(3)=-i.
\]
令 $R_n$ 为 R53 的完整 Serre 递推。
对 $p\equiv3\pmod4$、$p\ge7$，记
\[
 N_p=(p+1)/2,\quad\epsilon_p=(2/p),\quad
 V_p=\frac{R_{N_p}-\epsilon_p(E_{p-1}R_1+E_{p+1}F/24)}p.
\]
$V_p$ 是原固定 level、原 multiplier 上的整全纯模形式，
权为 $p+3/2$。

**定理。** 设低权空间是该固定 level/multiplier 上、在全部
cusps 整的经典全纯形式格之约化。若
\[
 \overline V_p=\overline E_{p-1}H+\overline E_{p+1}G,
 \qquad H\in\overline M_{5/2},\quad G\in\overline M_{1/2},
                                                               \tag{1}
\]
则原实际 $\tau=i$ 的 CM 纤维满足
\[
                         \overline V_p(x_{\rm CM})=0.          \tag{2}
\]
该结论允许整个 $M_{5/2}$，不预设 $H$ 是某个固定导数，
也不先要求 $G$ 是原 $F$ 的倍数。

准确的 CM 整格比较给
\[
 \boxed{\quad
 \overline V_p(x_{\rm CM})\ne0
       \iff b_{p+1}\not\equiv0\pmod p,
 \quad}                                                       \tag{3}
\]
其中 $A(z)=\sum b_mz^m$ 是 R51 的实际次数十七截面，$b_4=1$。
特别地 $b_8=1649/60$，故
\[
 \boxed{\quad
 \overline V_7\notin
 \overline E_6\,\overline M_{5/2}
       +\overline E_8\,\overline M_{1/2}.
 \quad}                                                       \tag{4}
\]
这排除了这个具体的全低权分解，范围严格强于只检验 $H=0$
或一个预选 unary theta 子空间。

对几何定义的全部 Katz 模 $p$ 低权形式，(1)$\Rightarrow$(2)
同样在一个固定有限例外集外成立。本结果未计算该集合，
所以 (4) 不额外声称排除 $p=7$ 的可能不能提升的权 $1/2$ 形式。

## 2. 完整有限 Weil 型与三个低权向量

置 $M=578$，取正二次型
$\mathcal D=\mathbb Z/1156$、$Q(r)=r^2/2312$ 的 Weil 表示 $\rho_M$。
其标准 theta 向量为
\[
 \Theta_M=\sum_{r\bmod1156}\sum_{n\equiv r(1156)}
               q^{n^2/2312}\mathbf e_r.
\]
保留全部标签的实际行是
\[
 \ell(\mathbf e_r)=a_{r/2}\quad(2\mid r),\qquad
 \ell(\mathbf e_r)=0\quad(2\nmid r).
\]
于是 $\ell\Theta_M=F$。
对全部分量使用同一 Serre 递推和除 $p$ 构造，得整向量
$\boldsymbol V_p$，满足 $\ell\boldsymbol V_p=V_p$。
所有平方 Fourier 指数均给同一个 $\epsilon_p$；
Weil 矩阵只在 $2,17$ 有分母，故不丢其他 cusps 的整性。

Bruinier–Schwagenscheidt **2017** Lemma 2.1 给全部权 $1/2$ 基
\[
 \Theta_M,\qquad\Theta_M^{\sigma_2},\qquad\Theta_2\mid U_{17}.
\]
其中 $\sigma_2r=579r\pmod{1156}$，固定所有偶 $r$；
$U_{17}$ 的向量只在 $17\mid r$ 有支撑。
因此这三个向量的实际行分别为
\[
                              F,\qquad F,\qquad0.              \tag{5}
\]
三个 Fourier 系数
$[q^{1/2312}\mathbf e_1]$、$[q^{1/2312}\mathbf e_{579}]$、
$[q^0\mathbf e_0]$ 给坐标矩阵
\[
 \begin{pmatrix}1&0&0\\0&1&0\\1&1&1\end{pmatrix}.
\]
行列式为一，故这组经典低权基在 Fourier 整格中饱和。

## 3. 标量分解必须保留实际行

在共同正规 metaplectic level 上，有限商 $\mathcal G$ 的群阶
只有素因子 $2,3,17$，所以所有所列 $p$ 都可作 Reynolds 平均。
令 $U=\rho_M^\vee$，取等变映射
\[
 \alpha(u)=u\boldsymbol V_p,\qquad
 L(H,G)=\overline E_{p-1}H+\overline E_{p+1}G.
\]
若 (1) 成立，令 $C=k[\mathcal G]\ell\subset U$。
$\alpha(C)\subset\operatorname{im}L$；Maschke 半单性给一个
$C\to X_H\oplus X_G$ 的等变提升，再用 $U\to C$ 等变投影。
所以 (1) 可以取为一个 $\rho_M$-值分解在 $\ell$ 下的像。

对经典整约化，等变 Hom 与约化交换：先任意提升线性映射，再以
$|\mathcal G|^{-1}$ 平均即可。其低权向量因而确实提升到特征零。
由 (5) 和饱和性，原标量等式必可写成
\[
 \overline V_p=\overline E_{p-1}H_\ell
                  +c_p\overline E_{p+1}\overline F.           \tag{6}
\]
在惰性 CM 点，Hasse 形式 $\overline E_{p-1}$ 为零，
而实际 $F(i)=0$ 精确成立。这证明 (2)。

对全部几何模 $p$ 形式，只需额外保证固定权 $1/2$ 空间的基变换。
固定紧化 level 曲线上的 theta-divisor 线丛，其相干上同调由一个
固定有限自由复形计算；删去该复形的有限消元分母后，$H^0$ 与
剩余域基变换交换。有限群不变量也交换。因此仅多出固定有限坏集，
不使用变动高权空间的任何基变换假设。

## 4. CM 整格：整性和精确范数一起使用

记 $\theta=\theta_3(0\mid i)$，并置
\[
 f_2=\partial_{1/2}^{2}F(i)/\theta^9=R_2(i)/\theta^9.
\]
$R_2$ 的全部 cusp 展开只在 $2,3,17$ 处分母。
取同权整数幂比 $R_2^4/(\theta_3^4)^9$，可直接在整数权的
几何整模型求值。theta 常数恒等式给
\[
 e_1-e_3=(\pi_{\mathbb C}/\Omega)^2\theta_3^4.
\]
按 Tate 微分规范，$\theta_3^4$ 的几何值为 $-4(e_1-e_3)$。
本题三个非零二挠横坐标为 $0,\sqrt{17},-\sqrt{17}$，
所以该值在所有 $p\ne2,17$ 上为单位，所有共轭标签亦然。
因此 $f_2$ 及其全部代数共轭在所有 $p\ge7$、$p\ne17$ 上整。

原实际有限向量与 raw $a_n$ 的共同标量为
$c=(\sqrt{17}/16)\mathfrak G(\lambda^{-1})\xi/17$，
$|\xi|=1$、$|\mathfrak G|^2=17$，故 $c\bar c=1/256$。
保留这个因子，Yang 的全部常数、Hermite 热方程和正实周期
\[
 \Omega_E=\pi_{\mathbb C}\theta^2/(\sqrt2\,17^{1/4})
\]
准确给
\[
 e_4=\frac{f_2\overline{f_2}}{144\,17^{27/4}},
 \qquad
 f_2\overline{f_2}=\frac{225}{32\,17^{13/4}}.                  \tag{7}
\]
最后一步用 R51 的精确 $e_4=25/(2^9 17^{10})$。
右边为 $p$ 单位，两个左因子已分别证明整，所以各自都是单位。

令 $\alpha=4-i$、
$h=\sqrt{\pi_{\mathbb C}/2}\,17/(\Omega_E\alpha)$。
则
\[
 C=(16\pi_{\mathbb C}h^2)\theta^4
     =16\,17^{5/2}/\alpha^2
\]
在所列 $p$ 上为单位。R53 的准确归一式成为
\[
 \frac{24C^{N_p-2}}{f_2}
       \frac{V_p(i)}{\theta^{4N_p+1}}
      =\frac{(p+1)!}{p}b_{p+1}.                              \tag{8}
\]
左边的比例是单位，$\theta_3^4$ 又给实际纤维的单位框架。
这证明 (3)，并且
$\frac{8!}{7}\frac{1649}{60}=158304\equiv6\pmod7$ 给 (4)。

## 5. 完整证明与已核来源

全部规范、两种模 $p$ 空间的区别及常数推导见
[实际 Weil/Hasse 完整笔记](../notes/2026-11-12-actual-weil-row-and-hasse-remainder.md)。

- J. H. Bruinier、M. Schwagenscheidt，Journal of Algebra **478** (2017),
  38–57，§2.1、Lemma 2.1：
  [作者全文](https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/bruinier/publikationen/UnaryThetaSeriesPaper-revision.pdf)。
- N. Ramsey，Ann. Inst. Fourier **56** (2006), 599–624，§3、Theorem 4.2：
  [出版全文](https://www.numdam.org/article/AIF_2006__56_3_599_0.pdf)。
- The Stacks Project（2026），Lemma 30.22.1、Remark 30.22.2：
  [Tag 07VJ](https://stacks.math.columbia.edu/tag/07VJ)。
- NIST DLMF（2026），[23.6.2–23.6.4](https://dlmf.nist.gov/23.6#E2)。
- Yang **1997** 的原平方公式、实际有限平均及正实周期已在
  [R46](R46-fixed-sigma-section-and-central-mellin-factors.md)、
  [实结构证明](../notes/2026-11-12-theta-real-structure-and-mellin-square.md)
  与 [R51](R51-explicit-theta-section-and-central-square-constant.md) 中逐项核定。
  本结果 (7) 另外保留 raw 权重相对于原向量的 $1/256$。

本结果给特定低权降阶方案的严格障碍及实际 CM 首层的整格接口。
它没有证明无穷多个 $p$ 的 $b_{p+1}$ 为单位，
也没有把一个 $p$ 的反例提升为对所有几何模 $p$ 形式的断言。
