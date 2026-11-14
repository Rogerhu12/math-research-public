# R778：原二十尖点的算术轨道与143阶函数恢复证书

日期：2026-11-14。状态：**已证明**。本篇不执行新的数学计算。

原 \(Y/L\) 的二十个尖点构成一个 Galois 轨道。因此，原 degree1206 映射的准确恢复不必机械展开到 R767 的2847个 Laurent 阶：在原 \(L\) 系数与完整尖点系数域 \(M\) 下，连续143个 Laurent 系数已经给出同一个全球关系。实际 R774 证书给 \(e=1\)，故所需原 Hodge 前缀止于 \(Q^{427}\)，严格包含在已经完成的 R745 的800前缀中。

本篇同时给出 \(M_2,M_6,M_{12}\) 的算术短展开注入界 \(13,41,82\)。它使用的是完整 \(\xi\) 坐标，不允许仅在某个模739嵌入上看到143个数就宣布全球恒等。

## 1. 原曲线、算术模型和尖点

保留 R762/R767/R772 的原记号：
\[
K=\mathbf Q(\zeta),\quad s=1+2\zeta,\quad s^2=-3,
\quad L=K(b),\quad M=L(\xi_{41}).
\]
原 \(b\) 不替换，\([L:K]=7\)、\([M:L]=40\)。原商曲线 \(Y\) 的 genus 为127，二十个尖点均具有宽度82，参考参数
\[
q_Y=Q^3=\exp(2\pi i\tau/82).
\tag{778.1}
\]
标准模曲线的算术群是
\[
G=C_3\times N_{\operatorname{GL}_2(\mathbf F_{41})}
\subset\operatorname{GL}_2(\mathbf Z/82\mathbf Z),
\]
其 determinant-one 子群为原 \(H=H_{82}\)。这里 mod2 的 \(C_3\) 和 mod41 的非分裂环面都是 R771/R775 实际使用的那一个。

R772 的
\[
u=E_6/\eta_{\rm Ded}^{12}=24s(2t-1)
\tag{778.2}
\]
把标准 \(G\) 模型在 \(K\) 上与原 \(Y_K\) 识别。它是 \(K\) 上的识别，不会改变 \(\operatorname{Gal}(\overline L/L)\) 对尖点的轨道。

## 2. 原二十个几何尖点的明确标签

全 level82 的尖点可用原始列向量
\[
v=(x,y)^t\in(\mathbf Z/82\mathbf Z)^2
\]
模正负号表示。所谓原始，等价于 mod2 与 mod41 分量都非零。因为 \(-I\in H\)，直接取 \(H\) 轨道即可。

在 mod41 的列向量上置
\[
\mathcal Q(x,y)=x^2+xy+y^2.
\tag{778.3}
\]
其判别式 \(-3\) 在 \(\mathbf F_{41}\) 中非平方，故非零列向量的 \(\mathcal Q\) 值非零。原环面矩阵和反射为
\[
T(a,b)=
\begin{pmatrix}a&-b\\b&a+b\end{pmatrix},
\qquad
J=\begin{pmatrix}-1&-1\\0&1\end{pmatrix}.
\]
直接展开给
\[
\mathcal Q(T(a,b)v)=(a^2+ab+b^2)\mathcal Q(v),
\quad
\det T(a,b)=a^2+ab+b^2,
\quad
\mathcal Q(Jv)=\mathcal Q(v),\quad\det J=-1.
\tag{778.4}
\]

原 \(H_{41}\) 是 norm-one 环面与 \(J\) 乘 norm-minus-one 环面的并。norm-one 群在每个非零范数纤维上单传递；第二部分把范数 \(n\) 的纤维送到范数 \(-n\) 的纤维。因此其轨道准确标为
\[
\{n,-n\}\in\mathbf F_{41}^{\times}/\{\pm1\}.
\tag{778.5}
\]
原 mod2 的 \(C_3\) 在三个非零列向量上传递。CRT 后，每个 (778.5) 给一个原尖点，一共二十个。这里用的是列向量；若改用对偶行向量，二次式会写成 \(x^2-xy+y^2\)，不能把两种标签约定的矩阵直接混写。

## 3. 精确的 Galois 作用，而非几何 deck 作用

标准算术尖点公式为
\[
C_G=G\backslash\operatorname{GL}_2(\mathbf Z/82\mathbf Z)/U_{82},
\]
其中 \(U_{82}\) 是由 \(-I\) 与上三角幺幂元生成的 cusp stabilizer。对
\(\sigma_m(\xi_{82})=\xi_{82}^m\)，
\[
\sigma_m(GAU_{82})
=GA\begin{pmatrix}1&0\\0&m\end{pmatrix}U_{82}.
\tag{778.6}
\]
原来源是 Zywina, *Explicit open images for elliptic curves over Q*, §5.2, Lemma5.2：
https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf
。该文说明尖点定义在 \(\mathbf Q(\xi_{82})\) 中，并给出 (778.6)。

为把它明确运输到 (778.5)，取 \(A\in\operatorname{SL}_2\) 代表该 cusp，并在原环面中选 \(\det g_m=m\)、mod2为恒等的 \(g_m\)。则
\[
A'=g_m^{-1}A\operatorname{diag}(1,m)
\in\operatorname{SL}_2(\mathbf Z/82\mathbf Z)
\]
表示右侧尖点。它的第一列是 \(g_m^{-1}v\)，所以 (778.4) 给
\[
\boxed{\quad \{n,-n\}\longmapsto\{m^{-1}n,-m^{-1}n\}.\quad}
\tag{778.7}
\]
这个逆元来自左侧用 \(g_m^{-1}\) 恢复 determinant one，不能把它误记为普通几何 deck 变换。

于是二十尖点在 \(\operatorname{Gal}(\mathbf Q(\xi_{41})/\mathbf Q)\) 下单传递，每个 stabilizer 恰为 \(\{\pm1\}\)。标准模型上其 residue field 是 \(\mathbf Q(\xi_{41})^+\)。

由 \([M:L]=40=[\mathbf Q(\xi_{41}):\mathbf Q]\)，有
\[
L\cap\mathbf Q(\xi_{41})=\mathbf Q.
\]
故在原 \(L\) 上，完整的四十个 cyclotomic automorphism 仍存在。结合 (778.2)，得到
\[
\boxed{\text{原 }Y_L\text{ 的二十尖点构成一个 degree20 的闭点。}}
\tag{778.8}
\]

这没有将参考尖点的全 Fourier 系数域降成实二十次域。参数本身可以带非平凡的切向 Galois 因子。下文只运输消失阶，这不受局部参数乘一个单位的影响；系数方程仍保留原 \(M/L\) 四十坐标。

## 4. 原 map 在全部尖点具有同一极点阶

R759 给出原第4号整周期微分 \(h\) 和 degree1206映射；R764 的真实树边/degree证书给
\[
f_P=f_0,\qquad f_0(c)=O
\quad\text{对全部二十个 cusp }c.
\tag{778.9}
\]
原 \(y\in L(Y)\) 的极点除子记作 \(E_y\)，则
\[
\deg E_y=1206.
\tag{778.10}
\]

令 \(e\) 为原参考 cusp 处零常数 Abel primitive 的 \(Q\) 首阶。原 \(\mu_3\) 等变性给 \(e\equiv1\pmod3\)，R745/R767 给 \(e\le19\)。在原 elliptic 坐标中 \(y\) 的 Abel 展开首项为 \(-J^{-3}\)，所以在 \(q_Y=Q^3\) 上它恰有 \(e\) 阶极点。

因为 \(y\) 定义在 \(L\) 上，(778.8) 将这个极点阶传到所有 cusp。若
\[
C_{\rm cusp}=\sum_{c\text{ cusp}}c,
\]
则
\[
E_y=eC_{\rm cusp}+E',\qquad
\deg E'=1206-20e,\qquad
\operatorname{supp}(E')\cap C_{\rm cusp}=\varnothing.
\tag{778.11}
\]

本次已完成的 R774 实际小证书
[run43631427773的原立方证书](../computations/R774-original-p41-Hodge-cube/43631427773-1/p41-original-Hodge-cube-certificate.json)
给准确 \(e=1\)，SHA256
aea27ac34e9a82203f723af27265db3cbd8d75e615247e11e0591fb2ed249b59。
这是以原第4号微分的精确特征零首系数求得，未由 degree1206 反推。

## 5. 143个 Laurent 阶已经等价于全球关系

令
\[
D=2(t)_0,\qquad\deg D=1640,\qquad
V_D=H^0(Y_L,\mathcal O(D)).
\]
原 \(t\) 在 cusp 处为极点，故 \(D\) 与所有 cusp 不相交。R767/R771 给 \(\dim_LV_D=1514\)。

取任意 \(A,B\in V_D\)，**其展开系数相对于原 \(K\) 定义基都在 \(L\) 中**。考虑
\[
F=A-yB.
\]
它的极点除子至多为 \(D+E_y\)。若在原参考 cusp 的完整 \(M\)-值 Laurent 展开中有
\[
\boxed{
[q_Y^n](A-yB)=0,\qquad -e\le n\le142-e,
}
\tag{778.12}
\]
则参考 cusp 的消失阶至少为 \(143-e>0\)。由 \(L\) 定义性和 (778.8)，每一个 cusp 都有该消失阶。于是 \(F\) 在全部 cusp 已无极点，且若 \(F\ne0\)，其零、极点次数分别满足
\[
\deg(F)_0\ge20(143-e)=2860-20e,
\]
\[
\deg(F)_\infty\le\deg(D+E_y-eC_{\rm cusp})
=2846-20e.
\tag{778.13}
\]
两者相差至少14，违背非零有理函数的主除子次数为零。因此
\[
\boxed{(778.12)\quad\Longleftrightarrow\quad A=yB\text{ 全局成立}.}
\tag{778.14}
\]

这是连续143个 Laurent 阶，每个系数属于 \(M\)。把它按 \(1,\xi,\ldots,\xi^{39}\) 展开后，得到最多5720个 \(L\) 线性方程。若只在一个有限域点代入 \(\xi\)，就没有验证 (778.12)，也不能据此应用 (778.14)。

其核准确为
\[
\{(yB,B):B\in H^0(D-E_y)\}.
\]
因为 \(\deg(D-E_y)=434>2g-2=252\)，Riemann–Roch给
\[
\boxed{\dim_L\ker=308,\qquad\operatorname{rank}_L=3028-308=2720.}
\tag{778.15}
\]
这保留 R772 的真实全球核，并把一个保证达到它的前缀缩短到143阶。

对实际 \(e=1\)，所需 Laurent 指数恰是
\[
-1,0,1,\ldots,141.
\tag{778.16}
\]
一个非零准确核向量必有 \(B\ne0\)，否则 \(A=0\)。因此若已经得到一个候选 \((A,B)\)，准确验证所有 (778.12) 就能认证 \(A/B\) 是原 \(y\)，无需为了验证这一向量另外求完整308维核。数值重构候选也必须通过同一个特征零精确验证。

## 6. 所需 basis 前缀与原 Hodge 前缀

在 (778.12) 中，\(y\) 的最低次数是 \(-e\)，故 \(B\) 只需到
\[
(142-e)+e=142.
\]
\(A\) 甚至只需到 \(142-e\)。所以统一可取
\[
\boxed{\text{原 RR basis 前缀至 }q_Y^{142}.}
\tag{778.17}
\]

实际计算还可直接使用权十二 numerator 基。若
\[
A=A_{\rm num}/D_\star,\quad B=B_{\rm num}/D_\star,
\quad
D_\star=(\eta_{\rm Ded}^{12}/2-sE_6/144)^2,
\]
则 \(D_\star\) 在 cusp 的常数为 \(-1/6912\ne0\)。所以
\(A-yB\) 与 \(A_{\rm num}-yB_{\rm num}\) 在 cusp 具有相同的消失阶。无需为建立这个关系矩阵额外生成全部除以 \(D_\star\) 的函数系数。

为生成 \(y\) 到 \(q_Y^{142-e}\)，写原 primitive
\[
J(Q)=\alpha Q^e J_0(q_Y),\qquad J_0(0)\ne0.
\]
原 equianharmonic Abel 展开是
\[
y(J)=-J^{-3}+\sum_{m\ge1}c_m b^mJ^{6m-3},
\qquad c_m\in\mathbf Q.
\tag{778.18}
\]
每项都是 \(J^3=4q_Y^eJ_0^3\) 的整数幂。其所需最高相对次数为142，故只须 \(J_0\) 至 \(q_Y^{142}\)，也即原 \(J\) 及 \(h=dJ\) 的 Fourier 分子至
\[
\boxed{Q^{426+e}\le Q^{445}.}
\tag{778.19}
\]
逐项积分保留真正的除数 \(n\) 和原 \(\alpha/7\)，不得用另一个归一的微分。

实际 \(e=1\) 时，上界为 **427**。已有 R745 的完整800前缀足够，不需要新一轮 newform、period 或长 Hodge 计算。也可直接复用已完成 R774 的准确 \(H^3\) 前缀：其到 \(q_Y^{142+e}\) 即足以产生所需 \(y\)，实际只到143；原820前缀仍完整保留作为后续可用产物，不能重算。

## 7. 三个模形式空间的算术短展开注入界

设 \(\mathcal W_k\) 是 R767 的相应模形式线丛，定义在原 \(K\) 上。其在 cusp 处的标准 modular-form 展开次数等于截面的零阶，因为 cusp 对数微分框架在该线丛中为单位。若某个 \(L\) 定义截面的完整 \(M\)-值 \(q_Y^0,\ldots,q_Y^B\) 全为零，则全部二十 cusp 的零阶都至少 \(B+1\)。因而只要
\[
20(B+1)>\deg\mathcal W_k,
\tag{778.20}
\]
该截面必为零。

这给出：

| 空间 | 原线丛次数 | 维数 | 足够的完整参考 cusp 前缀 |
|---|---:|---:|---|
| \(M_2\) | 272 | 146 | \(q_Y^0,\ldots,q_Y^{13}\) |
| \(M_6\) | 820 | 694 | \(q_Y^0,\ldots,q_Y^{41}\) |
| \(M_{12}\) | 1640 | 1514 | \(q_Y^0,\ldots,q_Y^{82}\) |

这些都是 \(L\) 或 \(K\) 定义截面的注入界；对一个定义在任意更大系数域、无同一 Galois 不变性的候选，不能这样把一个 cusp 的零同时乘二十。

R775 的原配方所含 scalars、E1、E4、E6、eta12 使 raw modular-form Fourier 系数在 \(\mathbf Q(\xi_{41})\) 中。故对它的694个 \(K\) 定义 \(M_6\) 基，把 \(0\le n\le41\) 的每个系数拆成四十个 \(\xi\) 坐标，得到一个 \(1680\times694\) 的有理矩阵，列秩准确为694。可实际选取694个原坐标行形成可逆有理子矩阵。

原 \(H^3\in M_6(Y/L)\) 已由 R772 证明。将其按
\[
1,b,\ldots,b^6,\quad s,sb,\ldots,sb^6
\]
拆成十四个有理右端，对上述同一个694阶有理矩阵准确求解，即给出它的真实 \(L\) 系数。由于该坐标映射在原空间上已单射，准确代回所选可逆子矩阵就足以识别原全球 \(H^3\)；不用重新计算821阶才知道该解正确。有限域子式可用于选择真实行，最后仍须准确有理解和代回。

## 8. 适用范围

本篇没有给出实际 \(A,B\) 或 \(\beta\) 坐标。它使已经授权的 R777 函数恢复变为明确的短前缀任务：原 \(K\) 定义 basis、准确 \(L\) 系数、完整四十 cusp 坐标、143阶全球验证，全部原模型/微分/平移保持。

如果数值工作暂时未得到足够独立行，只能继续或修复那个实际计算；不能把理论秩2720登记成输出。真实高度、第二类周期、Poincaré 对数及 R724 的有限 Bézout/完整尾仍在之后，绝对 Serre 一致性目标仍开放。
