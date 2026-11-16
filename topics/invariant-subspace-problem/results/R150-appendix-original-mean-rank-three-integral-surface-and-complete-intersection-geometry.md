# R150 附录：原 mean 秩三概形是整曲面，并具有完整交与确定的数值不变量

日期：2026-11-16  
作者：OpenAI ChatGPT（AI 协作研究）

## 1. 原对象与已经完成的输入

本附录只使用已发表的原模型矩阵恒等式和概形结论，不运行新的矩阵计算。基域固定为

$$
E=\mathbb Q[d]\big/
\bigl(3725d^3-43931504d^2+6080833024d+52565262336\bigr).
$$

令 $T'_0,T'_1,T'_2,T'_3$ 为原四个 mean 对称矩阵经过已验证的常数可逆换基后得到的 $6\times6$ 矩阵，置

$$
A(\mu)=\sum_{i=0}^3\mu_iT'_i,\qquad
\Delta(\mu)=\det A(\mu).
$$

相应的 $6\times4$ 线性矩阵记为

$$
M'(y)=[T'_0y,T'_1y,T'_2y,T'_3y].
$$

它与原矩阵 $M(y)$ 相差一个在 $E$ 上可逆的右乘矩阵，故所有 determinantal ideals 不变。下文简写为 $M(y)$。定义

$$
Y=V(I_4(M))\subset\mathbb P^5_E,\qquad
X=V(A(\mu)y)\subset\mathbb P^3_E\times\mathbb P^5_E.
$$

这里 $X$ 由原六个双线性方程定义，$Y$ 由原全部十五个最大子式定义，均保留概形结构。三个父结果提供以下输入。

1. [原秩三 mean incidence 与完整六次 pencil](R150-appendix-original-rank-three-mean-incidence-and-complete-sextic-pencil.md) 证明：$\Delta$ 在 $E[\mu]$ 中不可约；$I_4(A)=(\mu_0,\mu_1,\mu_2,\mu_3)^4$；第二投影给出概形同构 $X\simeq Y$。
2. [原 corank-two 例外代数自由秩三十五](R150-appendix-original-corank-two-pencil-exception-algebra-has-free-rank-thirty-five.md) 证明：$Z=V(I_5(A))\subset\mathbb P^3_E$ 全部落在 $\mu_0\ne0$，并且是长度恰为 $35$ 的有限概形；其齐次坐标环在 $E[\mu_0]$ 上自由秩为 $35$。此输入没有把 $Z$ 替换为约化点集。
3. [原 mean 三阶子式理想恰为 mean 理想的三次幂](R150-appendix-original-mean-three-minor-ideal-is-the-cube-of-the-mean-ideal.md) 证明 $I_3(M)=(y_0,\ldots,y_5)^3$。因此任何非零几何 $y$ 上 $M(y)$ 的秩至少为 $3$。

原四矩阵的换基、全部子式和有限概形身份都来自上述父结果。特别地，本附录使用的是原 mean 关系的退化概形，没有将剩余 Bell 或梯度方程删掉后声称原临界问题已经解决。

## 2. 两个投影的完整局部概形描述

记第一投影为 $\pi:X\to\mathbb P^3_E$，第二投影为 $\rho:X\to\mathbb P^5_E$。

先有 $\pi$ 在概形意义上经过六次超曲面

$$
D=V(\Delta)\subset\mathbb P^3_E.
$$

事实上，原恒等式 $\operatorname{adj}(A)Ay=\Delta y$ 在 $X$ 上给出 $\Delta y_i=0$。每个射影坐标开集上至少一个 $y_i$ 可逆，故 $\Delta=0$，而不只是 $\Delta$ 在闭点上为零。

在 $D\setminus Z$ 上有一个 $5\times5$ 子式可逆。对该开集作可逆行、列变换，把 $A$ 化为一个五阶单位块加一个一阶 Schur 块。该 Schur 块等于 $\Delta$ 乘一个单位。因此在 $D$ 上它严格为零，原核是秩一向量丛，给出

$$
\pi^{-1}(D\setminus Z)\simeq D\setminus Z
$$

的概形同构。另一方面，$I_4(A)=(\mu)^4$ 保证所有几何点的秩至少为 $4$。所以第一投影的几何纤维在 $D\setminus Z$ 上为一个点，在 $Z$ 的几何点上为一条 $\mathbb P^1$，没有更高维纤维。

第二投影的概形同构可在原单位块上直接复核。取 $M(y)$ 的一个可逆 $3\times3$ 子块，重排行、列后写为

$$
M(y)=
\begin{pmatrix}
U&b\\
C&e
\end{pmatrix},
\qquad U\in\operatorname{GL}_3.
$$

在此开集，全部最大子式生成的理想正是三项 Schur 向量

$$
e-CU^{-1}b
$$

的分量理想。若 $M(y)\mu=0$，则 $\mu$ 的最后一个坐标不能为零，否则 $U$ 可逆迫使 $\mu=0$。将它归一为 $1$ 后，前三个坐标唯一等于 $-U^{-1}b$，剩下的方程恰为上述三项 Schur 方程。因此这里的 incidence 是 $Y$ 的图，包含所有幂零信息。

由 $I_3(M)=(y)^3$，这些三阶单位块开集覆盖 $Y$，故 $\rho$ 确实给出全概形同构 $X\simeq Y$，并且是到 $\mathbb P^5_E$ 的闭浸入。

## 3. $X$ 是 $E$ 上的整曲面与六个双线性式的完整交

环境 $\mathbb P^3_E\times\mathbb P^5_E$ 是维数 $8$ 的正则概形，而 $X$ 由六个方程定义。因此 $X$ 的每个不可约分支维数至少为 $2$。

任取一个不可约分支 $W$。第一投影是射影态射，故 $\pi(W)$ 是 $D$ 的闭不可约子集。若它不支配 $D$，其维数至多为 $1$。在 $D\setminus Z$ 上投影是同构，而 $Z$ 是有限概形，所有其上的几何纤维至多一维。因此这样的 $W$ 的维数至多为 $1$，与前述下界矛盾。

于是每个分支均支配 $D$。但 $\Delta$ 在 $E[\mu]$ 中不可约，故 $D$ 是整曲面；其通有点不在有限概形 $Z$ 上。该通有点上的 incidence 纤维为唯一的点，且其概形为 $\operatorname{Spec}E(D)$。所以 $X$ 只有一个不可约分支，维数恰为 $2$。

现可确定正则序列性质。$X$ 在八维正则环境中具有纯余维 $6$，定义理想由六个局部函数生成。在每个相关正则局部环中，这六个生成元的理想高度为 $6$；由 Cohen–Macaulay 环中高度等于生成元数的正则序列准则，它们构成正则序列。因此：

$$
X\text{ 是六个 }(1,1)\text{ 截面的局部完整交，且是 Cohen–Macaulay 概形。}
$$

完整交没有嵌入关联点。又由第 2 节，$X$ 的稠密开集与整概形 $D\setminus Z$ 同构，所以 $X$ 通有约化。若 $X$ 有非零幂零理想，其非零关联点必须是 $\mathcal O_X$ 的关联点；没有嵌入关联点又迫使它出现在唯一的通有点上，这与通有约化矛盾。故 $X$ 约化。

综上，

$$
\boxed{X\simeq Y\text{ 是 }E\text{ 上的整射影曲面。}}
$$

这里的“整”是对基域 $E$ 的结论。证明没有使用或宣称 $\Delta$ 绝对不可约，也不把该结论改写为几何整性、光滑性或正规性。

## 4. Koszul 推前中的 $d_4$ 与 $\mathbb P^5$ 上的层分解

设 $p:\mathbb P^3_E\times\mathbb P^5_E\to\mathbb P^5_E$。第 3 节的正则序列给出 $\mathcal O_X$ 的完整 Koszul 分解，其第 $-k$ 项为

$$
K^{-k}=\bigwedge^k E^6\otimes\mathcal O(-k,-k),
\qquad 0\le k\le6.
$$

对 $p$ 作导出推前。所需射影空间上同调见 [Stacks Project, Section 30.8](https://stacks.math.columbia.edu/tag/01XS)；正则序列的 Koszul 正合性见 [Lemma 15.31.2](https://stacks.math.columbia.edu/tag/062F)。本次非零项只有：

| Koszul 位置 | 相对上同调 | 推前所得层 |
|---|---|---|
| $k=0$ | $R^0p_*$ | $\mathcal O$ |
| $k=4$ | $R^3p_*$ | $\mathcal O(-4)^{15}$ |
| $k=5$ | $R^3p_*$ | $\mathcal O(-5)^{24}$ |
| $k=6$ | $R^3p_*$ | $\mathcal O(-6)^{10}$ |

其中 $H^3(\mathbb P^3,\mathcal O(-4))$、$H^3(\mathbb P^3,\mathcal O(-5))$、$H^3(\mathbb P^3,\mathcal O(-6))$ 的维数依次为 $1,4,10$；乘上 Koszul 外幂维数 $15,6,1$ 得到表中的重数。$k=1,2,3$ 的相对上同调全部为零。

这里不能把“逐项普通推前”当作最终分解。谱序列

$$
E_1^{a,b}=R^bp_*K^a
\Longrightarrow
\mathcal H^{a+b}(Rp_*\mathcal O_X)
$$

在第三行留下

$$
\mathcal O(-6)^{10}\longrightarrow
\mathcal O(-5)^{24}\longrightarrow
\mathcal O(-4)^{15},
$$

还必须保留从位置 $(-4,3)$ 到 $(0,0)$ 的 $d_4$ 连接映射。

由第 2 节，$p|_X$ 就是闭浸入 $i:Y\hookrightarrow\mathbb P^5_E$，所以 $Rp_*\mathcal O_X=i_*\mathcal O_Y$ 只在总次数 $0$ 非零。第三行前两处的 $E_2$ 项没有其他可能的入射或出射微分，故必须为零。第三行最后的余核经 $d_4$ 单射到 $\mathcal O$，其余核正是 $i_*\mathcal O_Y$。因此获得真正的正合层分解

$$
\boxed{
0\longrightarrow\mathcal O(-6)^{10}
\longrightarrow\mathcal O(-5)^{24}
\longrightarrow\mathcal O(-4)^{15}
\longrightarrow\mathcal O
\longrightarrow i_*\mathcal O_Y
\longrightarrow0.
}
$$

最后一个到 $\mathcal O$ 的映射是上述 $d_4$ 与余核映射的复合。在第 2 节的三阶单位块开集，它的像就是 $e-CU^{-1}b$ 的三项理想；这恰为全部原最大子式所定义的理想。因而这里的正合性和像理想都是概形意义的结论，没有将理想换成根式。

本附录只需要此层分解，不额外把它称为未经验证的齐次坐标环自由分解。

## 5. Hilbert 多项式、上同调与截面算术亏格

用 $\mathcal O_Y(1)=\mathcal O_X(0,1)$ 作极化。由第 4 节正合层分解，所有整数 $n$ 上的 Euler 特征由同一个多项式给出：

$$
\begin{aligned}
\chi(\mathcal O_Y(n))
&=\binom{n+5}{5}
-15\binom{n+1}{5}
+24\binom{n}{5}
-10\binom{n-1}{5}\\
&=10n^2-15n+11.
\end{aligned}
$$

二项式在此按多项式解释。因此

$$
\boxed{\deg_{\mathbb P^5}Y=20,\qquad \chi(\mathcal O_Y)=11.}
$$

对整体上同调，也可以直接使用 product 上的同一 Koszul 分解。对于 $1\le k\le5$，$\mathcal O_{\mathbb P^5}(-k)$ 全部上同调为零，所以 $\mathcal O(-k,-k)$ 全部上同调为零。除 $k=0$ 的 $H^0=E$ 外，只剩 $k=6$ 的

$$
H^8\bigl(\mathbb P^3\times\mathbb P^5,\mathcal O(-6,-6)\bigr)
=
H^3(\mathbb P^3,\mathcal O(-6))
\otimes_E H^5(\mathbb P^5,\mathcal O(-6)),
$$

其维数为 $10$。它位于 Koszul 总次数 $8-6=2$，没有其他非零项可与之连接。故

$$
\boxed{
h^0(\mathcal O_X)=1,\qquad
h^1(\mathcal O_X)=0,\qquad
h^2(\mathcal O_X)=10.
}
$$

若超平面不包含整曲面 $Y$，其截面 $C$ 是有效 Cartier 截面。由

$$
0\longrightarrow\mathcal O_Y(n-1)
\longrightarrow\mathcal O_Y(n)
\longrightarrow\mathcal O_C(n)
\longrightarrow0
$$

可得

$$
\chi(\mathcal O_C(n))
=(10n^2-15n+11)
-\bigl(10(n-1)^2-15(n-1)+11\bigr)
=20n-25.
$$

因此此极化的截面算术亏格为

$$
\boxed{p_a(C)=26.}
$$

这是算术亏格，没有加入截面光滑或几何整的断言。

## 6. 对偶化层与完整交交数

环境的对偶化层是 $\mathcal O(-4,-6)$。六个定义截面的法丛行列式为 $\mathcal O_X(6,6)$。局部完整交的伴随公式因此给出可逆对偶化层

$$
\boxed{\omega_{X/E}\simeq\mathcal O_X(2,0).}
$$

令 $u=c_1(\mathcal O_X(1,0))$，$v=c_1(\mathcal O_X(0,1))$。在环境 Chow 环

$$
\mathbb Z[u,v]/(u^4,v^6)
$$

中，完整交的基本类为

$$
[X]=(u+v)^6.
$$

以 $\int_{\mathbb P^3\times\mathbb P^5}u^3v^5=1$ 计算，可得

$$
\boxed{\int_Xu^2=6,\qquad
\int_Xuv=15,\qquad
\int_Xv^2=20.}
$$

由于 $c_1(\omega_X)=2u$，

$$
\boxed{c_1(\omega_X)^2=24.}
$$

这些是原局部完整交曲面上的交数；其成立不要求先证明曲面光滑。这里也没有将第一投影称为一个已经证明光滑或正规的 resolution。

## 7. 整个长度三十五例外概形上的真实 $\mathbb P^1$ 丛

把原矩阵限制到 $Z=V(I_5(A))$。由 $I_4(A)=(\mu)^4$，$Z$ 可由四阶子式为单位的开集覆盖。在这样的开集写

$$
A=
\begin{pmatrix}
U&B\\
C&D
\end{pmatrix},
\qquad U\in\operatorname{GL}_4.
$$

包含 $U$ 的五阶子式等于 $\det(U)$ 乘以 $D-CU^{-1}B$ 的相应分量。它们在 $\mathcal O_Z$ 中全部严格为零，而 $\det(U)$ 是单位，故

$$
D-CU^{-1}B=0\quad\text{于 }\mathcal O_Z.
$$

这一步保留 $Z$ 中的幂零元，不只是几何闭点上的秩判断。因此

$$
\mathcal K=\ker\bigl(A|_Z:\mathcal O_Z^6\to\mathcal O_Z(1)^6\bigr)
$$

是秩二局部自由层；在上述局部平凡化中，其向量为 $(-U^{-1}B\,v,v)$，$v\in\mathcal O_Z^2$。

于是整个概形原像满足

$$
\boxed{X\times_D Z\simeq\mathbb P_Z^{\mathrm{lines}}(\mathcal K).}
$$

这里 $\mathbb P^{\mathrm{lines}}$ 表示向量丛中的一维子空间，即 $\operatorname{Proj}_Z\operatorname{Sym}(\mathcal K^\vee)$。故它是真正的 $\mathbb P^1$ 丛，基底为完整的长度 $35$ 有限概形 $Z$。

每个几何点上的纤维，在第二投影下是其二维原核给出的一条线性直线。不同几何点的纤维在 $\mathbb P^5$ 中互不相交：若同一个非零 $y$ 位于两条这样的核线，$M(y)$ 就有两个独立的右核向量，与所有非零 $y$ 上 $\operatorname{rank}M(y)\ge3$ 矛盾。这也与第二投影的闭浸入一致。

这里不能把长度 $35$ 改写成“三十五条互异几何直线”。若 $Z$ 非约化或有高次剩余域，长度包含相应的概形重数和域次数；本定理不删除这些信息。

## 8. 已完成范围与后续原问题

本附录由原三个父结果严格推出：

- 原 mean 秩三概形在 $E$ 上是整曲面；
- 它与原 incidence 概形同构，并在 $\mathbb P^3\times\mathbb P^5$ 中是六个 $(1,1)$ 式的完整交；
- 它在 $\mathbb P^5$ 中有第 4 节的正合层分解、Hilbert 多项式 $10n^2-15n+11$、次数 $20$ 和截面算术亏格 $26$；
- 其 $\mathcal O$ 上同调为 $(1,0,10)$，对偶化层为 $\mathcal O_X(2,0)$，交数为 $(u^2,uv,v^2)=(6,15,20)$，$c_1(\omega_X)^2=24$；
- 整个 corank-two 例外概形的原像是长度 $35$ 基底上的秩二核丛的射影化。

这些结论没有判断曲面的所有奇点，也没有声称正规、光滑、几何整或 crepant resolution。它们没有解决原 Bell 剩余关系、完整梯度理想的后续问题或普通不变子空间问题。

### 来源身份

三个原父文件的冻结 Git blob 分别为：

- 原 incidence 与六次 pencil：`1f8949c88ef6ffb59ace7ecb00fb203ba3e98431`；
- 原例外代数自由秩三十五：`b7f8ee8978fd4cc017a3fd507c3c1410fcea9223`；
- 原 mean 三阶子式理想：`5ce9692361f433e59bae10247b46abb57bf6a66c`。

本附录没有新运行身份；它是对上述已核输入的独立概形论与上同调推导。
