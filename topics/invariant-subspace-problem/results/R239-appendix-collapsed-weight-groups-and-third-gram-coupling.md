# R239 附录：合并等权组强制的第三耦合恒等式

- 日期：2026-11-13。
- 作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
- 状态：本文证明实际二维 primitive 族的合并组共同合同对角化，以及由此得到的全异常权 commutator 恒等式。它是前两条 Pearson 关系之外的额外实际约束；本文不把四次式正性当成已完成。
- 独立精确核验：[280 个实际有理例及两硬端](../notes/2026-11-13-collapsed-groups-commutator-exact-check-0c.py)；不代替下文结构证明。
- 输入：[完整真实 MP / 同源 shear](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)、[实际 Pearson 双对角身份](R239-appendix-actual-binomial-pearson-bidiagonal-and-full-shear-elimination.md)。全文保持完整出生源和真实逆。

## 1. 实际模型与两次等权合并

普通短组长为 $q_0$，权平方为 $z>0$；单位池长 $L\ge q_0$；异常位权平方为 $w>0$。固定真正二维的相对出生
$$
1\le t_0\le q_0,\qquad \delta=q_0-t_0,\qquad
h=q_0+L+1-2t_0\ge2.
$$
令 $H_j(w)$ 是已经付全物理 Gram 逆、再压缩到整个二维 primitive 源所得的 MP Gram，$0\le j\le h$。使用同一个源坐标 $(\alpha,\beta)$，它具有
$$
H_j=\begin{pmatrix}A_j+B_jk_j^2&-B_jk_j\\-B_jk_j&B_j\end{pmatrix},
\qquad A_j=a_j+w a_{j+1}.
\tag{1.1}
$$
内部 $B_j=w b_{j-1}b_j/(b_{j-1}+w b_j)$，硬端 $B_0=wb_0$、$B_h=b_{h-1}$。

**合并引理。** 分别固定 $w=1$ 或 $w=z$ 时，存在一个与 $j$ 无关的可逆二维源变换，使全部 $H_j$ 同时合同对角化。两次合并所需的源变换无需相同。

**证明。** 记 $V_s$ 为长 $s$ 的标准对称串。两条同权串 $V_s\otimes V_1$ 有标准正交分解
$$
V_s\otimes V_1=V_{s+1}\oplus V_{s-1},
\tag{1.2}
$$
其中第二支的原始出生次数比第一支多一。可直接将总降算子与其伴随生成的有限 $\mathfrak{sl}_2$ 串正交分解，或对完全对称方向及其正交 primitive 方向作逐阶提升，得到 (1.2)。这一分解是整个分次空间的正交分解，且同时约化降算子及其伴随。

$w=1$ 时将池与异常位合并：
$$
V_{q_0}\otimes(V_L\otimes V_1)
=(V_{q_0}\otimes V_{L+1})\oplus
 (V_{q_0}\otimes V_{L-1}).
$$
两支的相对出生分别为 $t_0$ 和 $t_0-1$，最终高度都等于 $h$。第一支合法，因为 $t_0\le q_0\le L+1$；第二支合法，因为 $0\le t_0-1\le q_0-1\le L-1$。每支在所指出生有且只有一个 primitive 方向。

$w=z$ 时将短组与异常位合并：
$$
(V_{q_0}\otimes V_1)\otimes V_L
=(V_{q_0+1}\otimes V_L)\oplus
 (V_{q_0-1}\otimes V_L).
$$
同样，两支相对出生为 $t_0,t_0-1$，均合法且高度均为 $h$。即使 $L=q_0$ 或 $t_0=q_0$，上述次数范围仍成立。

在任一合并情形，完整物理 Gram $D^j(D^*)^j/(j!)^2$、它的真实逆及对整个 primitive 源的压缩，都尊重这两个固定正交约化分量。因此用两支源向量作为同一个源基，所有 $H_j$ 都对角。回到 $(\alpha,\beta)$ 是一次与 $j$ 无关的合同变换，证明完毕。

这一步不能用某个标量分支或预先压缩的 Gram 代替真实逆；它成立是因为上述分解约化完整物理算子。

## 2. 同时合同对角化强制的局部方程

固定 $1\le n<h$。对三个源 Gram 作同一个剪切，使 $k_n=0$，并记
$$
x=k_{n-1}-k_n,\qquad y=k_{n+1}-k_n.
$$
于是
$$
H_-=\begin{pmatrix}A_-+B_-x^2&-B_-x\\-B_-x&B_-\end{pmatrix},\quad
H_0=\operatorname{diag}(A_0,B_0),\quad
H_+=\begin{pmatrix}A_++B_+y^2&-B_+y\\-B_+y&B_+\end{pmatrix}.
$$
若这三个矩阵同时合同对角化，则 $H_-H_0^{-1}H_+$ 自伴。因为当 $H_i=C^*\Delta_iC$、$\Delta_i$ 为实正对角时，该乘积为 $C^*\Delta_-\Delta_0^{-1}\Delta_+C$。

直接相减两个非对角元给
$$
(H_-H_0^{-1}H_+)_{12}-(H_-H_0^{-1}H_+)_{21}
=\frac{B_-B_+}{A_0}\,\mathcal C(w),
$$
其中
$$
\boxed{\mathcal C(w)=x\frac{A_+}{B_+}-y\frac{A_-}{B_-}
+(y-x)\left(xy+\frac{A_0}{B_0}\right).}
\tag{2.1}
$$
因此合并引理严格给
$$
\mathcal C(1)=\mathcal C(z)=0.
\tag{2.2}
$$

## 3. Pearson 关系确定全部 $w$ 依赖

写局部原首一范数
$$
a=a_{n-1},\ b=a_n,\ c=a_{n+1},\ d=a_{n+2},\quad
p=b_{n-2},\ q=b_{n-1},\ r=b_n,\ s=b_{n+1}.
$$
局部 $q$ 不是头数，$s$ 不是出生次数。则
$$
\frac{A_-}{B_-}=\frac{a}{wq}+\frac ap+\frac bq+\frac{wb}p,
$$
$$
\frac{A_0}{B_0}=\frac{b}{wr}+\frac bq+\frac cr+\frac{wc}q,
$$
$$
\frac{A_+}{B_+}=\frac{c}{ws}+\frac cr+\frac ds+\frac{wd}r.
\tag{3.1}
$$
端点 $p=\infty$ 或 $s=\infty$ 只表示相应倒数项为零，(3.1) 与真实硬端 $B$ 完全一致。

已证正向与反向 Pearson 身份为
$$
x=\frac{z-1}{n}(b/p-c/q)
=\frac{z-1}{z(h+1-n)}(b/r-a/q),
$$
$$
y=\frac{z-1}{n+1}(d/r-c/q)
=\frac{z-1}{z(h-n)}(b/r-c/s).
\tag{3.2}
$$
先取 $z\ne1$。代入 (3.1)，$\mathcal C(w)$ 的 $w$ 系数准确为
$$
x(d/r-c/q)+y(c/q-b/p)=\frac{xy}{z-1},
$$
其 $w^{-1}$ 系数准确为
$$
x(c/s-b/r)+y(b/r-a/q)=\frac{zxy}{z-1}.
$$
常数项为
$$
\mathcal C_0=x(d/s-b/q)+y(c/r-a/p)+(y-x)xy.
$$
因此两条合并方程实际上只给同一个新增约束：
$$
\boxed{x(d/s-b/q)+y(c/r-a/p)+(y-x)xy
+\frac{z+1}{z-1}xy=0.}
\tag{3.3}
$$
把它代回得到整个异常权轴上的准确身份
$$
\boxed{\mathcal C(w)=\frac{xy(w-1)(w-z)}{(z-1)w}.}
\tag{3.4}
$$
(3.3) 含 shear 的三次项，因而不能从两条只在线性范数比中出现的 Pearson 关系随意省略。以上推导没有除以 $xy$，所以也适用于某个 shear 恰为零的退化参数。$z=1$ 本来就属于已付两权情形；(3.4) 在需要时可按实际 Gram 的解析性取极限，不能单独保留分母而忽略 $xy$ 的消失。

## 4. 无量纲局部消元

这里只为后续四次式代数固定符号。将全部原范数同时缩放，使局部 $q=1$，并写
$$
p=1/P,\quad r=R,\quad s=RT,\qquad
b=\beta,\ c=\beta\alpha,\ a=\beta A,\ d=\beta B.
$$
令 $m=h-n$。两条 Pearson 关系给
$$
A=1/R+z(m+1)(\alpha-P)/n,
$$
$$
B=\alpha R+(n+1)(1-\alpha/T)/(zm).
$$
写 $x=\beta X,y=\beta Y$，其中
$$
X=\frac{z-1}{n}(P-\alpha),\qquad
Y=\frac{z-1}{zmR}(1-\alpha/T).
$$
若 $XY(Y-X)\ne0$，(3.3) 等价于
$$
\boxed{\beta=-\frac{X(B/(RT)-1)+Y(\alpha/R-AP)
+XY(z+1)/(z-1)}{(Y-X)XY}.}
\tag{4.1}
$$
实际 $z>1$ 的非平凡矩形可用[已自足证明的严格 Turán 导数单调性](R239-appendix-rectangular-turan-endpoints-and-sharp-curvature-caps.md)得 $X<0<Y$，但单纯写 (3.3) 不需要借助该严格性。式 (4.1) 精确固定了此前松弛中可以任取的曲率尺度 $\beta$。

(3.3)–(3.4) 和 (4.1) 是新增的必要耦合身份。要完成异常位统一比较，仍须在它们和全部真实标量结构下支付完整四次式；不能仅以合并点的对角性替代所有 $w>0$ 的比较。
