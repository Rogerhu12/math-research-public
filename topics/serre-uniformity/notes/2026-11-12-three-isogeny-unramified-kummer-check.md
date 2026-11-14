# R46 在 3 处的局部步骤：独立核验与精确 Kummer 像

日期：2026-11-12；会话：nonsplit-frobenius。
状态：证明完整；是 R46 §4、§5.3 的补充核验，不另计结果编号。

令 $R=\mathbb Z_3$，$K=\mathbb Q_3$，$k=\mathbb F_3$，且 $a\in R^\times$。定义

$$
B:y^2=x^3+a,\qquad D:V^2=U^3-27a,
$$

以及自然三同源

$$
\phi(x,y)=
\left(\frac{x^3+4a}{x^2},
\frac{y(x^3-8a)}{x^3}\right).
$$

记 $M=B[\phi]$，$\mathcal B^0,\mathcal D^0$ 为 Néron 恒等分量，记
$B_0(K)=\mathcal B^0(R)$、$D_0(K)=\mathcal D^0(R)$。

## 1. 结论

R46 所用的包含完全成立。事实上有更精确的等式

$$
\boxed{\quad
\delta_K(D_0(K))
=
H^1_{\mathrm{nr}}(K,M).
\quad}
\tag{1}
$$

这个空间为

$$
H^1_{\mathrm{nr}}(K,M)
\simeq
\begin{cases}
\mathbb F_3,&a\equiv1\pmod3,\\
0,&a\equiv-1\pmod3.
\end{cases}
\tag{2}
$$

当 $a\equiv1\pmod3$，取 $v\in R^\times$ 满足
$v^2=1-27a$、$v\equiv1\pmod3$，则

$$
P=(1,v)\in D_0(K)
\tag{3}
$$

的 Kummer 类是 (2) 中的一个生成元。另一个非零类由 $-P$ 给出。

**没有 $a\equiv\pm1\pmod9$ 的最小性或核闭包例外。**
这些细分类可能改变 Kodaira 符号或分量群，但下述最小性、核的
有限 étale 延拓、(1) 和 (2) 对全部 $3$ 进单位成立。

## 2. 极小模型与极小微分

短模型给

$$
v_3(\Delta_B)=v_3(-432a^2)=3,\qquad
v_3(\Delta_D)=v_3(-432\cdot729a^2)=9.
$$

它们都是整模型。任何两个整 Weierstrass 模型的判别式赋值相差
$12v_3(u)$；若其中一个非极小，就存在整模型使判别式赋值至少减少 $12$。
由于整模型的非零判别式赋值非负，显示的 $3$、$9$ 均不可能再减小。
因此两个模型都是极小的；此论证不使用 $a\bmod9$。

令 $\omega_B=dx/(2y)$、$\omega_D=dU/(2V)$。直接微分得

$$
dU=(1-8a/x^3)\,dx,\qquad
V=y(1-8a/x^3),
$$

从而

$$
\phi^*\omega_D=\omega_B.
\tag{4}
$$

这是两个 Néron 极小不变微分之间的等式。
因此延拓的 $\Phi^0:\mathcal B^0\to\mathcal D^0$
在恒等截面处相对微分为单位；群平移使它处处如此。
两个模型均光滑、相对维数相同，所以 $\Phi^0$ 为 étale 态射。

## 3. 核的有限 étale 闭包

因为 $a$ 是单位，$T^2-a$ 的根至多需要一个未分歧二次扩张：
若 $\bar a=1$，由 Hensel 已在 $R$ 有根；
若 $\bar a=-1$，多项式模 $3$ 不可约而且可分，给未分歧二次扩张。
令 $R'/R$ 为这个有限 étale 扩张，在 $R'$ 上记根为 $b$。

三个核点

$$
O,\quad P_+=(0,b),\quad P_-=(0,-b)
$$

延拓为 Néron 模型的三个截面。
后两个点在整 Weierstrass 模型上都有单位 $y$ 坐标，模 $3$ 的偏导数
$2y$ 非零，故确实落在光滑部分。它们的残点互异，也都不同于 $O$。

特殊纤维的 Weierstrass 方程是一个尖点三次曲线，光滑部分连通；
极小 Weierstrass 模型的光滑部分正是 $\mathcal B^0$。
故三截面都在 $\mathcal B^0_{R'}$ 内。
分离性使每个截面为闭浸入，而残点互异使它们互不相交。
其并是秩 $3$ 的有限 étale 闭子概形。

群运算保持这三个截面：等式在泛纤维成立，继而由分离性在整底上成立。
Galois 作用只可能交换 $P_+$ 和 $P_-$，所以该子群可下降到
$\mathcal B^0$ 内的有限 étale 闭子群 $\mathcal M$。
其泛纤维为 $M$，又因平坦而无仅在特殊纤维的附加分量，正是所需核闭包。

这已验证 R46 引理 46.1 的全部假设。

## 4. R46 的 pushout 证明为何足够

有限 étale $R$-群概形与未分歧 $G_K$-模的对应给

$$
H^1(R,\mathcal M)
\ \simeq\
H^1(k,\mathcal M_k)
\ \simeq\
H^1_{\mathrm{nr}}(K,M).
\tag{5}
$$

给定此群中的 torsor $T$，沿 $\mathcal M\hookrightarrow\mathcal B^0$
推出，得到

$$
\mathcal T=T\times^{\mathcal M}\mathcal B^0.
$$

它是 $\mathcal B^0$-torsor，光滑。这里无需预先识别任何
$\mathcal B^0/\mathcal M$：pushout 只是对 $\mathcal B^0$
进行有限 étale 扭曲。$\mathcal B^0$ 是准射影的，有限群作用可用
张量积得到不变相对丰沛束，故该 contracted product 可表示为光滑概形；
即使采用代数空间表述，后面的提升结论也不变。

$\mathcal T_k$ 是连通光滑 $k$-群 $\mathcal B_k^0$ 的 torsor。
Lang 定理给出 $\mathcal T_k(k)\ne\varnothing$，而光滑 Hensel 提升给
$\mathcal T(R)\ne\varnothing$。在本题特殊纤维为 $\mathbb G_a$，
Lang 消失甚至就是加性 Hilbert 90。

所以原来的未分歧类在 $H^1(K,B)$ 中为零。
泛纤维同源正合列

$$
0\longrightarrow M\longrightarrow B
\xrightarrow{\phi}D\longrightarrow0
$$

立即给出它属于 $\delta_K(D(K))$。这完整证明 R46 所需的包含；
**不需要把商 Néron 模型当作一个额外假设。**

作为来源定位，有限 étale 对应见
[Stacks, Lemma 10.153.7, Tag 04GK](https://stacks.math.columbia.edu/tag/04GK)；
光滑 Hensel 提升见
[Stacks, Lemma 15.13.3, Tag 0H74](https://stacks.math.columbia.edu/tag/0H74)；
Lang 的原始论文为
S. Lang, *Algebraic groups over finite fields*,
Amer. J. Math. **78** (1956), 555–563，
[原文托管](https://wstein.org/papers/bib/Lang-Algebraic_Groups_Over_Finite_Fields.pdf)。

## 5. 显式特殊纤维：一个独立的有限 étale 商核对

以下给出比 R46 所需更强的直接模型核对。

设 $\bar a\in\mathbb F_3^\times$。因为 $\bar a^3=\bar a$，
$B$ 的特殊纤维可写为

$$
y^2=(x+\bar a)^3.
$$

其光滑部分取加性坐标

$$
t=\frac{x+\bar a}{y},\qquad t(O)=0.
$$

在 $t\ne0$ 上有

$$
x=t^{-2}-\bar a,\qquad y=t^{-3}.
$$

$D$ 的特殊纤维为 $V^2=U^3$，光滑部分取

$$
u=\frac UV,\qquad u(O)=0.
$$

将同源公式约化后，在稠密开集上消去公共因子：

$$
\overline U=\frac{y^2}{x^2},\qquad
\overline V=\frac{y^3}{x^3},\qquad
u=\frac xy=t-\bar a t^3.
$$

因而在整个特殊恒等分量上

$$
\boxed{\quad
\Phi_k^0:\mathbb G_a\longrightarrow\mathbb G_a,
\qquad t\longmapsto t-\bar a t^3.
\quad}
\tag{6}
$$

这个多项式次数为 $3$，导数为 $1$，是有限 étale 的加性同源。
其三个几何核点为

$$
t=0,\qquad t=\pm\sqrt{\bar a},
$$

恰是第 3 节三个核截面的残点。

由 (4)，$\Phi^0$ étale；其泛纤维和特殊纤维都满射，
所以 $\Phi^0$ 忠实平坦。
核概形亦 étale，且 $\mathcal M$ 在泛纤维和特殊纤维上都给出全部核，
故 $\ker\Phi^0=\mathcal M$。
群差映射给

$$
\mathcal B^0\times\mathcal M
\xrightarrow{\sim}
\mathcal B^0\times_{\mathcal D^0}\mathcal B^0.
$$

所以 $\Phi^0$ 是一个 $\mathcal M$-torsor。有限 étale 性可对忠实平坦底变
下降，由右式可见 $\Phi^0$ 确实有限 étale，秩为 $3$。
这就证明了整模型精确列

$$
0\longrightarrow\mathcal M\longrightarrow
\mathcal B^0\xrightarrow{\Phi^0}\mathcal D^0
\longrightarrow0.
\tag{7}
$$

利用第 4 节的 $H^1(R,\mathcal B^0)=0$，由 (7) 得

$$
D_0(K)/\phi B_0(K)\simeq H^1(R,\mathcal M).
\tag{8}
$$

(5) 中向泛纤维的映射是单射，因此 (8) 在通常 Kummer 映射下仍为单射。
这证明 (1)，也表明来自 $B(K)\setminus B_0(K)$ 的点不会额外杀掉
(8) 中的非零类。

## 6. 未分歧类的精确大小与显式代表

$M\simeq\mathbb F_3(\chi_a)$；其 Frobenius 在 $\sqrt a$ 上的作用为

$$
\operatorname{Frob}_3|_M=
\begin{cases}
+1,&\bar a=1,\\
-1,&\bar a=-1.
\end{cases}
$$

于是未分歧一阶上同调的标准公式

$$
H^1_{\mathrm{nr}}(K,M)
=
M/(\operatorname{Frob}_3-1)M
$$

立即给 (2)。

也可完全从局部点群看出这一点：
(4) 表明形式群同态的线性项是单位 $1$，故

$$
\phi:B_1(K)\xrightarrow{\sim}D_1(K).
$$

在剩余域有 $t^3=t$，故 (6) 对 $k$ 点的作用是
$t\mapsto(1-\bar a)t$。
因此 $D_0(K)/\phi B_0(K)$ 分别是 $\mathbb F_3$ 或 $0$，
与 (2) 一致。

最后，$1-27a\equiv1\pmod3$，Hensel 给唯一
$v\equiv1\pmod3$ 满足 $v^2=1-27a$。
点 $P=(1,v)$ 在特殊纤维的加性坐标为 $u=1$。
当 $\bar a=1$ 时，(6) 在 $\mathbb F_3$ 点上的像为 $0$，
所以 $P$ 在 (8) 中非零，生成全部未分歧类。
相应的模 $3$ 逆像方程是

$$
t-t^3=1.
$$

它在 $\mathbb F_3$ 无根，因而是不可约可分三次式；
有限 étale 提升显示 $\phi^{-1}(P)$ 就是一个未分歧三次 torsor。
这提供了不依赖抽象上同调大小计算的具体局部核验。

## 7. 对 R46 文本的核查意见

R46 §4 与 §5.3 的论证有效，无需增加同源商整模型的假设。
可以用一句话明确有限 étale 扭曲的光滑性与 Hensel 提升，
并用 (6) 核对“恒等分量映射 étale、核闭包一致”这一句。
最小性和核位置没有模 $9$ 例外，不需按 $a\equiv\pm1\pmod9$ 分支修改。
