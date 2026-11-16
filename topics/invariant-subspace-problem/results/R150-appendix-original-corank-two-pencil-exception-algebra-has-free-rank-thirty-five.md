# R150：原对称矩阵族的高亏秩例外代数有完整自由35基

作者：Astra-ISP-789f / root；normal_annihilator 核对矩阵复形。AI-assisted: GPT-6 Astra Pro。  
日期：2026-11-16（UTC）。  
**状态：已证明。**

## 1. 同一个原矩阵族与结论

沿用[原rank3关联及完整六次矩阵族](R150-appendix-original-rank-three-mean-incidence-and-complete-sextic-pencil.md)的固定数域、原参数双向运输和对称矩阵
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),
$$
$$
S=E[\mu_0,\mu_1,\mu_2,\mu_3],\qquad
A=T'(\mu)\in\operatorname{Sym}_6(S),\qquad I=I_5(A).
$$
各变量取普通次数一。前稿已完整证明：

- $\det A\ne0$；
- $I_4(A)=(\mu_0,\mu_1,\mu_2,\mu_3)^4$；
- 将全部21个对称五阶余因子限制到 $\mu_0=0$，其全部三变量五次系数方块在 $E$ 中可逆；合法 $127,d=100$ 约化的原行列式为103。

第三项给准确等式
$$
I+(\mu_0)=(\mu_0)+(\mu_1,\mu_2,\mu_3)^5.
\tag{1.1}
$$
前稿只由它得到仿射例外代数的维数至多35。本稿补上完整正合性，证明
$$
\boxed{
S/I\cong
\bigoplus_{\substack{a,b,c\ge0\\a+b+c\le4}}
E[\mu_0]\,\mu_1^a\mu_2^b\mu_3^c
}
\tag{1.2}
$$
为分次 $E[\mu_0]$ 模的自由基陈述。特别
$$
\boxed{
\dim_E E[\mu_1,\mu_2,\mu_3]/
I_5(T'(1,\mu_1,\mu_2,\mu_3))=35.
}
\tag{1.3}
$$
这35个原单项式自身就是基；没有换成未知的35元生成族。

因此原 projective rank4 例外子概形的长度恰为35，且非空。这里计入全部重数；没有声称它由35个互异点组成或在 $E$ 上分裂。

## 2. 35个原单项式生成与完整余维

由原21阶常数单位，将每个三变量五次单项式写成五阶余因子的常数线性组合加一个含 $\mu_0$ 的齐次五次项。因此在 $S/I$ 中
$$
\mu_1^a\mu_2^b\mu_3^c=\mu_0 q_{abc}(\mu),
\qquad a+b+c=5,\qquad \deg q_{abc}=4.
\tag{2.1}
$$
右边的每个单项式在 $\mu_1,\mu_2,\mu_3$ 上的次数至多4。

对更高三变量次数的单项式，取其中一个次数五因子，使用 (2.1)，再继续。每步严格降低这三个变量的总次数，故终止。于是 (1.2) 右边确有到 $S/I$ 的分次满射。

特别 $S/I$ 有限生成于 $E[\mu_0]$ 上，故其 Krull 维数至多一，得到
$$
\operatorname{ht} I\ge3.
\tag{2.2}
$$
目前还没有用生成性推出线性独立；该步将在 §5 由完整分辨率支付。

## 3. 原对称矩阵给出的完整自由复形

记 $\operatorname{Alt}_6(S)$ 为反对称矩阵模，
$\mathfrak{sl}_6(S)$ 为迹零矩阵模，$\operatorname{Sym}_6(S)$ 为对称矩阵模。三者的秩分别为15、35、21。

定义
$$
\begin{aligned}
d_3(Y)&=YA,\\
d_2(X)&=AX+X^{\mathsf T}A,\\
d_1(B)&=\operatorname{tr}(\operatorname{adj}(A)B).
\end{aligned}
\tag{3.1}
$$
原域特征零。由 $A^{\mathsf T}=A$、$Y^{\mathsf T}=-Y$，有
$\operatorname{tr}(YA)=0$，所以 $d_3$ 的目标确为迹零模。

又
$$
d_2d_3(Y)=AYA+(YA)^{\mathsf T}A=0,
$$
$$
d_1d_2(X)=2\det(A)\operatorname{tr}(X)=0.
$$
因此得到分次复形
$$
0\longrightarrow S(-7)^{15}
\xrightarrow{d_3}S(-6)^{35}
\xrightarrow{d_2}S(-5)^{21}
\xrightarrow{d_1}S.
\tag{3.2}
$$
最后像恰为 $I$：对角对称基给对角余因子，非对角对称基给两倍对应余因子，且2为单位。没有删去任何原五阶子式。

最左映射单射。若 $YA=0$，右乘 $\operatorname{adj}(A)$ 得
$Y\det(A)=0$；$S$ 是整环且原 $\det A\ne0$，故 $Y=0$。

还需证明中间正合，不能只核复合为零。

### 3.1 在全部余因子不同时为零处的准确秩

取任意 $\mathfrak p\not\supset I$。在其剩余域中，$A$ 的秩至少五。可作可逆合同变换并扩域计算线性映射的秩；这种变换不改变 (3.1) 三个映射的秩。

秩六时，$A$ 可逆，$d_3$ 单射，$d_1$ 非零，而 $d_2$ 的核准确是
$$
\{X:AX\text{ 反对称}\},
$$
维数15；这族自动迹零，因为对称矩阵与反对称矩阵之积的迹为零。因此 $d_2$ 秩为20。

秩五时，可取
$$
A=\operatorname{diag}(a_1,\ldots,a_5,0),\qquad a_i\ne0.
$$
$YA=0$ 强制 $Y$ 前五列为零，再由反对称性强制全部为零，故 $d_3$ 秩15。
$d_2(X)$ 的右下角为零，而其余20个对称坐标均可任意指定：前五阶对称块和最后交叉列由相应 $X_{ij}$ 取得，$X_{66}$ 自由补足迹零。故 $d_2$ 秩20。
$d_1$ 是右下角坐标乘 $\prod_{i=1}^5a_i$，故秩一。

因此在 $I$ 外三个映射的秩始终为
$$
15,\quad20,\quad1.
\tag{3.3}
$$
原局部环上相应最大子式是单位，Gaussian 消元使像成为直和因子。维数相加与复合为零给局部正合；两个中间余核分别为自由模秩20和秩一。

## 4. 由余维三排除全部支持在例外上的同调

这里给出正合性证明，不将一个通用矩阵分辨率未经检查地特化。

使用两个标准交换代数事实：

1. 若正则局部环 $R$ 的维数为 $t$，有限模有长度不超过 $\ell$ 的自由分辨率，则其深度至少 $t-\ell$。逐次应用短正合列的深度引理即可。
2. 有限模在整环上若对每个非零素理想的局部化均有正深度，则它无挠：非零挠子会给一个非零伴随素理想，而该点局部深度为零。

标准依据为 Stacks Project 的[深度引理，Lemma 10.72.6 / 00LX](https://stacks.math.columbia.edu/tag/00LX)、[局部深度的 Ext 刻画，Lemma 10.72.5 / 00LW](https://stacks.math.columbia.edu/tag/00LW)及[无挠模与伴随素理想，Lemma 15.22.8 / 0AUV](https://stacks.math.columbia.edu/tag/0AUV)，访问日期2026-11-16。前一事实从自由模深度为 $t$ 和短正合列逐步推出；后一事实也可直接对一个非零挠元的消去理想取伴随素理想证明。

先置
$$
M_2=\operatorname{coker}d_3.
$$
最左单射给长度一的自由分辨率。在每个 $\mathfrak p\supset I$ 处，(2.2) 与 $S_{\mathfrak p}$ 正则给
$$
\operatorname{depth}(M_2)_{\mathfrak p}
\ge\operatorname{ht}\mathfrak p-1\ge2.
$$
在 $I$ 外，§3.1 已给 $M_2$ 自由。因此它在每个非零素理想处深度至少一，是无挠模。

$d_2$ 诱导 $M_2\to S(-5)^{21}$。其核是 (3.2) 的第二同调；§3.1 说明它支持在 $V(I)$，尤其在分式域上为零，故是挠子模。无挠性强制这个核为零。

现在置
$$
M_1=\operatorname{coker}d_2.
$$
刚证明的中间正合性给长度二的自由分辨率。在 $\mathfrak p\supset I$ 处，
$$
\operatorname{depth}(M_1)_{\mathfrak p}
\ge\operatorname{ht}\mathfrak p-2\ge1.
$$
在 $I$ 外它是自由秩一。因此 $M_1$ 同样无挠。
$d_1$ 诱导的 $M_1\to S$ 的核只支持在 $V(I)$，是挠子模，遂也为零。

至此得到同一个原 $A$ 的完整分辨率
$$
\boxed{
0\longrightarrow S(-7)^{15}
\longrightarrow S(-6)^{35}
\longrightarrow S(-5)^{21}
\longrightarrow S
\longrightarrow S/I\longrightarrow0.
}
\tag{4.1}
$$
没有假设例外约化、一般位置、已知长度或平坦特化。

## 5. Hilbert 级数支付完整35项的线性独立

由 (4.1)，
$$
\begin{aligned}
\operatorname{Hilb}_{S/I}(t)
&=\frac{1-21t^5+35t^6-15t^7}{(1-t)^4}\\
&=\frac{1+3t+6t^2+10t^3+15t^4}{1-t}.
\end{aligned}
\tag{5.1}
$$
另一方面，§2 的原单项式满射的源为
$$
F=\bigoplus_{a+b+c\le4}E[\mu_0](-a-b-c),
$$
其 Hilbert 级数正是 (5.1) 的最后一式：三个变量次数
$0,1,2,3,4$ 的单项式数分别为 $1,3,6,10,15$。

这是分次满射 $F\to S/I$；源和目标在每个次数的维数相同，所以其每个齐次核分量均为零。满射严格是同构，证明 (1.2)。

特别 $\mu_0$ 是真正的非零因子；该结论没有预先作为正合性的假设。取商 $\mu_0=1$ 后，35个同一原单项式保持线性独立，证明 (1.3)。
更一般地，对任意 $c\in E$，取 $\mu_0=c$ 的纤维都由这35项自由组成。$c=0$ 的纤维正是三变量五次幂截断代数，故这里的自由35结论本身不包含约化性。

也可读出原分次 Hilbert 函数：
$$
\dim_E(S/I)_n=
1,4,10,20,35,35,35,\ldots\qquad(n=0,1,2,\ldots).
$$

## 6. 原全部高亏秩参数的准确几何范围

由 (1.1)，projective 例外完全位于 $\mu_0\ne0$，所以其全部坐标代数就是 (1.3)。它长度恰35，故在代数闭包上非空，几何支撑点的局部长度之和恰35。

又前稿已证 $I_4(A)=(\mu)^4$，故这些非零 projective 参数下秩恰四，没有混入更低秩。每个几何支撑点在原关联概形中都带有整个二维核的 projective 直线。其非约化结构和原 $y$ 的尺度仍必须保留。

长度35不等于35个互异的 $E$ 点，也不等于例外理想是根理想。若要继续检验约化性，可在本稿已经确定的同一35项基上构造原乘法矩阵，再用完整判准；本稿未执行这一新计算。

## 7. 原输入身份与后续范围

本稿是对已完成原矩阵族的纯代数证明，没有重新运行数域行列式或新增数值证据。唯一数据依赖均在前稿及其[原输入清单](../notes/2026-11-16-r150-original-rank-three-pencil-inputs-789f.json)、[实际三阶段执行身份](../notes/r150-nonrankone-execution-789f/20261116-local-original-rank-three-pencil-and-complete-exception-gates.json)中：

- 完整原规范矩阵族和84个六次系数，binding 39e2ef818d36588618292515fabf94615f3e7a64f1d047ea25c218e3987c9038；
- 全部四阶子式及21个五阶余因子的完整系数门，binding d73ed9dc675a00081cea88a34f47fcc617db89aba1c7df5e56427f9168c641ba。

前稿“至多35”的上界现被 (1.3) 的等式加强，其保留非约化例外的要求继续有效。

[全局9×56原临界表示](R150-appendix-complete-original-global-nine-generator-critical-presentation.md)中其余全部 $w,u$ 关系、原 Bell=1 条件以及 $M(y)$ 的rank4分支都未因本稿消失。普通 Hilbert ISP 仍未解决。
