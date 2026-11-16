# R870 — 原三阶商上的低权模形式比值与严格椭圆坐标证书

日期：2026-11-16。

**状态：已证明。** 本篇给出原 $\Xi _0$ 的一个较小且可直接执行的坐标认证方法。它使用 $X_0(867)$ 上的模形式，不以原端点平面模型的总次数为重建参数。权 $2$ 时只需求 $120$ 维模形式空间中的两个向量，并核一条权 $18$ 的完整恒等式。这里尚未报告任何候选通过，未假设 $n=1$ 是整 Hom，也未算出原 R859 的非零 shadow。

来源始终是 [R862](R862-original-seventeen-torsion-product-and-complete-cubic-hom-matrix.md) 和 [R866](R866-original-modular-function-certificate-and-level-nine-model.md) 的同一个 $\Xi _0$。一旦它的一个整数倍得到认证，[R867](R867-original-single-hom-and-integral-hecke-three-basis.md) 的实际整 Hecke 操作恢复其余两条 Hom；没有另外选择椭圆商、形式微分或 Artin 分支。

## 1. 原曲线、微分与三阶商

记
$$
C=X_0(2601),\qquad D=X_0(867),\qquad
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0.
$$

R864 的固定三次数 $v$ 满足
$$
v^3+367395v^2+147v+\frac1{17}=0.
$$

沿 R866 使用
$$
E_v:\quad Y^2+vY=X^3,\qquad
\omega_v=\frac{dX}{2Y+v},\qquad
\Xi _0^*\omega_v=H_0(q)\frac{dq}{q}.
\tag{1}
$$

其中 $\Xi _0$ 是原准同态，$H_0$ 的全部系数已由原有限理想和指定，包含二处因子，且
$$
H_0(q)=q-2q^4+\cdots
=q\,f(Q),\qquad Q=q^3,\qquad f(0)=1.
\tag{2}
$$

所有非零指数都为 $1\bmod3$：原理想与 $\delta$ 互素，其范数模 $3$ 是一个非零平方。因此(2)是整条来源的恒等式，不是前缀观察。系数可在 $L=K(v)$ 中计算；R869 的实际共轭下降允许进一步用 $\mathbf Q(v)$，以下证明不依赖这一降域优化。

令
$$
R:z\longmapsto z+\frac13,\qquad z'=3z.
$$

取 $A_3=\operatorname{diag}(3,1)$。准确有
$$
A_3\Gamma _0(2601)A_3^{-1}
=\Gamma _0(867)\cap\Gamma ^0(3),
$$
$$
A_3\langle\Gamma _0(2601),R\rangle A_3^{-1}
=\Gamma _0(867).
\tag{3}
$$

第一等式直接比较矩阵上下角；右边的指数为 $3$，添入
$A_3RA_3^{-1}=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$
即得第二式。故 $z\mapsto3z$ 给真正三次商 $C\to D$，在 $K$ 上其 deck 群由 $R$ 生成。

由(2)，$H_0(z+1/3)=\omega H_0(z)$。目标上
$$
[\omega](X,Y)=(\omega X,Y),\qquad [\omega]^*\omega_v=\omega\omega_v.
$$

两边都以 $\infty\mapsto O$ 归一，微分注入给
$$
\Xi _0\circ R=[\omega]\circ\Xi _0
\quad\hbox{于原 }\operatorname{Hom}^0.
\tag{4}
$$

因此，若 $n\Xi _0$ 是真整同态，其 $Y$ 坐标下降到 $D$，其 $X$ 坐标为 $R$ 的 $\omega$ 特征。这里 $n$ 始终是待认证的正整数。

定义
$$
\mathfrak h(Q)=H_0(q)^3=Qf(Q)^3.
\tag{5}
$$

共轭群(3)、$R$ 的三次特征及各 cusp 的全纯性共同说明
$$
\mathfrak h\in S_6(\Gamma _0(867)).
\tag{6}
$$

(6)不是把任意三次形式缩短指数。它从原 $H_0$ 在指数三正规子群上的实际变换律下降；在每个 cusp，三次幂除掉有限特征，且原 cusp 消失阶仍为正。

## 2. 同一个 Kummer 曲面

为和 R866 的函数模型相接，记
$$
S=T_9(z),\qquad
T_9(z)=\left(\frac{\eta(z)}{\eta(9z)}\right)^3,
\qquad s=S+3.
$$

$R$ 固定 $\infty$，而 $S$ 是只有该点有一个单极的 Hauptmodul。比较
$S=q^{-1}-3+5q^2+\cdots$ 的首项和常数，得到
$$
s(Rz)=\omega^2s(z).
\tag{7}
$$

因此 $Z=sX$ 是不变坐标。原方程准确下降为
$$
\boxed{\quad Z^3=s^3Y(Y+v).\quad}
\tag{8}
$$

还可把底函数换成原 $X_0(3)$ 的 Hauptmodul：
$$
T_3(z')=\left(\frac{\eta(z')}{\eta(3z')}\right)^{12},
\qquad
s^3=T_3(3z)+27.
\tag{9}
$$

自含验证如下。$T_3(3z)=(\eta(3z)/\eta(9z))^{12}$ 在 $X_0(9)$ 的三个非无穷 cusp 各有一个零，只在 $\infty$ 有三阶极点。$(S+3)^3-27$ 也只在 $\infty$ 有极点。两者首部同为 $q^{-3}-12+O(q^3)$，故其差是射影直线上的常数且该常数为零。cusp 阶数可直接代 R866 所用的 eta-quotient 阶数公式。

下面不求(8)的高次数平面坐标；用同一 $Y$ 的模形式比值及原微分，直接恢复 $X$ 与 $Z$。

## 3. 低权空间的准确尺寸

$\Gamma _0(867)$ 无椭圆点。其指数、cusp 数及 genus 为
$$
\mu=1224,\qquad c_\infty=36,\qquad g(D)=85.
\tag{10}
$$

具体地，$867=3\cdot17^2$，指数为
$867(1+1/3)(1+1/17)=1224$；
各分母 $1,3,17,51,289,867$ 的 cusp 数为
$1,1,16,16,1,1$。
素数 $3$ 排除二阶椭圆点，$17\equiv2\bmod3$ 排除三阶椭圆点，故
$g=1+\mu/12-c_\infty/2=85$。

令 $\mathcal C$ 为全部 cusp 的约化除子。对偶数 $k\ge2$，权 $k$ 模形式是线丛
$$
\mathcal L_k=
\bigl(\Omega_D^1(\mathcal C)\bigr)^{\otimes k/2}
$$
的截面，并有
$$
\deg\mathcal L_k=102k,\qquad
\dim M_k(\Gamma _0(867))=102k-84.
\tag{11}
$$

第二式由 Riemann–Roch 及 $102k>2g-2=168$ 得到。特别
$$
\dim M_2=120,\qquad \dim M_4=324.
\tag{12}
$$

全非零权 $k$ 模形式在 $\infty$ 的阶至多 $102k$。所以前
$102k+1$ 个 Fourier 系数精确决定该形式。本篇所有零恒等式界都可直接由这一除子次数证明，不依赖近似模值。

## 4. 一条完整恒等式认证原 Hom

固定 $n\ge1$ 和偶数 $k\ge2$。取同一常数域中的
$$
A,B\in M_k(\Gamma _0(867)),\qquad B\ne0,
\qquad Y=\frac AB.
$$

以下 $D_Q=Q\,d/dQ$ 只指 Fourier 归一化的微分。置
$$
C_{A,B}=(D_QA)B-A(D_QB).
\tag{13}
$$

两项的非模部分准确相消，故
$$
C_{A,B}\in M_{2k+2}(\Gamma _0(867)).
\tag{14}
$$

假设 $Y$ 非恒定，并满足原无穷处主项
$$
Y=-n^{-3}Q^{-1}+O(1).
\tag{15}
$$

本篇的完整认证式为
$$
\boxed{
C_{A,B}^{\,3}
=n^3\mathfrak h\,
A^2(A+vB)^2B^2.
}
\tag{16}
$$

两边均是权 $6k+6$ 的全纯模形式。因此(16)只需在原数域中准确检查
$$
[Q^j]\left(
C_{A,B}^{\,3}
-n^3\mathfrak h A^2(A+vB)^2B^2
\right)=0
\quad
(0\le j\le612(k+1)).
\tag{17}
$$

这包含末端系数；不是只核较短重建前缀。

**结论。** 若(15)–(17)成立，则
$$
\boxed{
X=nH_0(q)\,
\frac{Y(Y+v)}{D_QY}
}
\tag{18}
$$
与 $Y$ 是原真态射 $n\Xi _0:C\to E_v$ 的准确坐标。

证明所有常数如下。由(13)–(16)，
$$
(D_QY)^3=n^3H_0(q)^3Y^2(Y+v)^2.
\tag{19}
$$

因为 $Y$ 非恒定，$D_QY$ 不恒为零，所以(18)定义真正有理函数。$H_0$ 与 $D_QY$ 都有权 $2$；前者在原 $C$ 上，后者从 $D$ 拉回。因此其比值是原 $C$ 上的有理函数，全部系数与原 $q$ 归一化相容。从(19)得
$$
X^3=Y(Y+v),\qquad
X^2=\frac{D_QY}{nH_0(q)}.
\tag{20}
$$

又因 $D_q=3D_Q$，
$$
D_qY=3nH_0(q)X^2.
$$

对(20)第一式求导，再取消非零有理函数 $3X^2$，得到
$$
D_qX=nH_0(q)(2Y+v).
\tag{21}
$$

故 $dX/(2Y+v)=nH_0\,dq/q$，正是(1)的整数 $n$ 倍。注意(19)没有额外 $3^3$：它已由 $D_q=3D_Q$ 与 $dY=3X^2\omega_v$ 抵消。

由(15)、(18)，$X\sim n^{-2}q^{-2}$，故无穷处映到 $O$。到射影光滑曲线 $E_v$ 的非恒定有理映射从原光滑 $C$ 全局延拓。它诱导以 $\infty$ 为基点的真 Jacobian 同态，其微分等于 $n\Xi _0$。特征零下 Hom 的微分表示单射，故该同态就是 $n\Xi _0$。这同时认证了整数性，未事先假设 $n=1$ 可积为全球态射。

权 $2$ 时，严格检查上界是
$$
612(2+1)=1836.
\tag{22}
$$

## 5. 有限线性重建与高维核的处理

设 $Y_{\rm form}$ 为第6节的原形式 germ。取
$$
M=204k+1.
$$

在已知的 $M_k$ 基中解有限线性条件
$$
B(0)=0,\qquad
A-Y_{\rm form}B=O(Q^M).
\tag{23}
$$

不强制 $B$ 的一次系数非零。允许 $A,B$ 在 $\infty$ 有共同零，也允许(23)的核维数大于1。

任意非零解自动有 $B\ne0$。否则 $A$ 的消失阶至少 $M>102k$，由第3节知 $A=0$。对非零 $B$，有
$\operatorname{ord}_\infty B\le102k$；因此
$$
\frac AB-Y_{\rm form}
=O(Q^{M-\operatorname{ord}_\infty B})
=O(Q^{102k+1}).
\tag{24}
$$

所以(15)及其常数项自动正确，且 $A/B$ 非恒定。

若 $(A_1,B_1)$、$(A_2,B_2)$ 为两个非零解，则
$A_1B_2-A_2B_1\in M_{2k}$ 的阶至少 $M>204k$，故
$$
A_1/B_1=A_2/B_2
\quad\hbox{作为原 }D\hbox{ 上的有理函数}.
\tag{25}
$$

因此高维核只是同一比值的不同表示，不产生不同来源；可从任意非零解进入严格(17)检查。低前缀本身不代替(17)。

权 $2$ 时 $M=409$。求(23)需保 $Q^{-1}$ 至 $Q^{408}$：由于 $Y_{\rm form}$ 有单极，$B$ 至少取至 $Q^{409}$。使用所有基到 $O(Q^{411})$ 和 $Y_{\rm form}$ 到 $O(Q^{410})$ 是安全的低阶段精度。

若严格证书通过，则
$$
\deg(n\Xi _0)=\deg(Y:D\to\mathbf P^1)\le102k.
\tag{26}
$$

等式由源商和目标商均为三次得到；不等式因 $Y$ 的极除子包含于 $B$ 的零除子。权 $2$ 的认证映射次数至多 $204$，共同零的取消可使实际次数更小。

反向，若原 $n\Xi _0$ 已是真态射，次数为 $d$，则其下降 $Y$ 的极除子 $\mathcal P$ 次数恰 $d$。Riemann–Roch 给
$$
h^0(\mathcal L_k(-\mathcal P))
\ge102k-d-84.
\tag{27}
$$

所以
$$
d\le102k-85
\tag{28}
$$
保证存在非零 $B$，使 $B,YB$ 都在 $M_k$ 中。这时(23)必有解，且(16)成立。权 $2$、权 $4$ 的保证范围分别为 $d\le119$、$d\le323$。

R862 已给某个整数 $n$ 和实际 Hom。因此逐个枚举有限对角的 $(n,k)$，并执行(23)、(17)，仍是保证终止的原坐标算法。只跑 $n=1,k=2$ 是该算法的首个具体候选；失败仅排当前低权比值，不排其他整数倍或权。

## 6. 保原周期的高效 germ

(1)上的标准局部参数为
$$
u=-X/Y.
$$

由椭圆方程直接解得
$$
X=\frac{1+\sqrt{1-4vu^3}}{2u^2},
\qquad
Y=-\frac{1+\sqrt{1-4vu^3}}{2u^3},
\qquad
\omega_v=\frac{du}{\sqrt{1-4vu^3}}.
\tag{29}
$$

所有平方根取常数项1。故原形式对数为
$$
\log_{E_v}(u)
=\sum_{j\ge0}\frac{\binom{2j}{j}}{3j+1}v^j u^{3j+1}.
\tag{30}
$$

要构造 $n\Xi _0$ 的 germ，准确解
$$
\log_{E_v}(u(q))
=n\sum_{m\ge1}\frac{[q^m]H_0}{m}q^m.
\tag{31}
$$

它有唯一 $u=nq+O(q^4)$。由(2)写
$$
u=nq\,E(Q),\qquad E(0)=1,\qquad t=n^3v.
$$

(29)–(31)等价于
$$
\boxed{
E+3QE'=f(Q)\sqrt{1-4tQE^3}.
}
\tag{32}
$$

若 $E=\sum e_mQ^m$，则逐项
$$
(3m+1)e_m
=[Q^m]\,f(Q)\sqrt{1-4tQE^3}.
\tag{33}
$$

右侧的非恒平方根在第 $m$ 项只用 $e_0,\ldots,e_{m-1}$，因此是严格三角递推。可以累计 $E^2,E^3$ 与平方根卷积，在 $Q$ 变量中作精确计算，无需先求三倍长度的一般反演。

最后
$$
\boxed{
Y_{\rm form}
=-\frac{1+\sqrt{1-4tQE^3}}{2n^3QE^3}.
}
\tag{34}
$$

特别由 $f_1=-2$ 得
$$
e_1=-\frac{1+n^3v}{2},\qquad
Y_{\rm form}
=-n^{-3}Q^{-1}-\frac{v+3n^{-3}}2+O(Q).
\tag{35}
$$

这些系数固定了原整数 $n$、$C_v$ 模型和微分尺度；不能独立把首项改成 $-Q^{-1}$ 后继续声称是同一个 $n$。

## 7. 公开 producer 的完整执行范围

数学执行仍只在本公开仓库的 Actions 中。新的 producer 可以按以下有限顺序执行：

1. 重建原 $H_0$、原 $v$，保 R866/R869 的完整理想和及同一嵌入；原低阶段至少生成(34)到 $Q^{409}$。
2. 在 $\mathbf Q$ 上求 $M_2(\Gamma_0(867))$ 的真基，核维数 $120$、基的 Fourier 秩，再扩常数域到原三次域。先用 $O(Q^{411})$ 解(23)，不更换 cusp 归一化。
3. 若核为零，记录准确低权失败；若核非零，保一个非零原解和全部规范系数的 SHA-256。由第5节，任意这样的解定义同一个候选比值。
4. 把该同一模形式基延长到至少 $O(Q^{1838})$。准确重建 $f(Q)$ 至 $Q^{1836}$，即原 $H_0$ 至 $q^{5509}$，并由(5)计算 $\mathfrak h$。
5. 完整核(17)的 $0\le j\le1836$。只有全部为零才输出原真 $n\Xi _0$ 已认证，并记录(18)、全 $A/B$ 系数和原 Hecke 后续规范。

(14)和全部基的模性是数学输入；不把任意截断向量放进一个同维空间后宣称具有该性质。标准模块符号/模形式基算法给的是已知全局空间中的实际基，扩精度须扩同一基而不能在两个独立 echelon 基之间错配系数。

可以把低阶段核与高阶段严格检查分开运行，但第二阶段必须使用第一阶段的同一 $A,B$。只保脚本、参数、run、输出哈希及数学结论，不入库可重算系数表。

## 8. 原来源返回与尚未计算部分

本证书绕开了 R866 的大端点多项式表示，但没有绕开原来源：

- $H_0$、$v$、$n$ 与 $\Xi _0$ 全部固定；
- $Q=q^3$ 是原实际 $R$ 商，(18)准确恢复原 $C$ 上的 $X$；
- 原 $\mathcal A_i=2^{11}\kappa\Xi _i$、R867 的共同清分母 $57n$、原 $q_0,q_2$ 与全部 Artin 系数保持；
- 只有严格(17)成功才付真坐标。尚不能从低核存在或形式 germ 推出原 shadow 非零，也不能把它移为 R814 的 canonical cycle。

模形式的空间、基与 $q$-展开实现可参考 Sage 官方文档：
[Generic spaces of modular forms](https://doc.sagemath.org/html/en/reference/modfrm/sage/modular/modform/space.html)
及
[Modular forms of weight 2](https://wstein.org/books/modform/modform/weight_two.html)。
次数界与零恒等式界已在第3–5节自含证明，不依赖软件判定一条未知全局恒等式。