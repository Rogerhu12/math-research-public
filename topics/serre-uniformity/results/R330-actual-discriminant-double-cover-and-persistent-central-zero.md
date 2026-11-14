# R330：实际二除判别式二层的完整谱与持续中心零

**状态：已证明。** 将实际判别式平方类 $-3$ 加到 $X_{\rm ns}^+(p)$ 上，确实得到一个新的全局二层。它的反不变部分来自层 $4p^2$ 的新形式，而不是层 $2p^2$。未扭曲时这些新形式的根号为 $+1$；但是实际有理点所需的 $-3$ 扭曲将它们的根号全部改回 $-1$。基底 Jacobian 的因子也具有根号 $-1$。

因此，该二除标记本身没有给出中心 $L$ 值非零的有理商。本文不把中心零冒作无条件的算术秩正性，也不声称关闭原异常分支。证明包括准确的二层、几何分歧、全部旧部分的消去、$W_4$ 的直接矩阵符号，以及实际扭曲的两项 Fourier 推导。

## 1. 实际二层及其有理标记

令 $p>3$ 为素数，

$$
X=X_{\rm ns}^+(p)/\mathbb Q,\qquad
j:X\longrightarrow\mathbb P^1
$$

为标准 $j$ 映射。令 $Y^+$、$Y^{-3}$ 分别为以下函数域扩张的光滑射影规范化：

$$
Y^+:\ s^2=j-1728,\qquad
Y^{-3}:\ j=1728-3t^2.
\tag{330.1}
$$

两者均是几何连通的二层，甲板对合记为 $\iota$。

先确认这不是任取的二次覆盖。对 Legendre 参数 $\lambda$，

$$
j(\lambda)=
256\frac{(\lambda^2-\lambda+1)^3}{\lambda^2(\lambda-1)^2},
\qquad
j(\lambda)-1728=
\left(
8\frac{(\lambda+1)(\lambda-2)(2\lambda-1)}
        {\lambda(\lambda-1)}
\right)^2.
\tag{330.2}
$$

右侧平方根在 $S_3\simeq\mathrm {GL}_2(\mathbb F_2)$ 的换位下变号、在 $A_3$ 下不变。因此 $Y^+$ 是将 $X(2)/A_3\to X(1)$ 拉回 $X$ 并规范化所得的标准模二层。模 $2$ 和模 $p$ 的满级结构由中国剩余定理独立，且定义 $X$ 的同余群在模二仍满射到 $S_3$，故该拉回几何连通。

对任意非特殊 $j$ 的椭圆曲线，

$$
j-1728=\frac{c_6^2}{\Delta}.
\tag{330.3}
$$

二除多项式的判别式与 $\Delta$ 有相同的平方类。所以判别式平方类为 $-3$ 的实际曲线给出 $Y^{-3}$ 上的有理点，而不是通常 $Y^+$ 上的有理点。

R263/R289 的实际共同二、三除域整数族满足

$$
a^3+db^3=1,\qquad
j=6912a^3(1-a^3)
  =1728-3\bigl(24(2a^3-1)\bigr)^2.
\tag{330.4}
$$

因而其标记可准确取

$$
t=24(2a^3-1).
\tag{330.5}
$$

若 $p\equiv2\pmod3$，基底上有 $j=0$ 的有理 CM 点。其在实际二层上的两个标记为 $t=\pm24$；在未扭曲二层上却为 $s=\pm24\sqrt{-3}$。两者不能互换。

## 2. 分歧、亏格与 CM 点处的局部性质

记 $g=g(X)$，$\chi_4(p)=\left(\frac{-1}{p}\right)$。二层在每个基底尖点以及每个二阶椭圆点处分歧；除此以外不分歧。

证明如下。$j-1728$ 在尖点的极点阶等于该尖点宽度。非分裂正规化子的阶与 $p$ 互素，所以非平凡模 $p$ 幺幂元不属于它，每个尖点宽度恰为 $p$，为奇数。基底到 $j$ 线的度为 $p(p-1)/2$，故尖点数为

$$
c=(p-1)/2.
\tag{330.6}
$$

在 $j=1728$ 上，二阶椭圆点的局部映射次数为一，其他点的局部映射次数为二，恰前者给二层分歧。在 $j=0$ 上，$j-1728$ 为单位；它没有零或极点。

二阶椭圆点数可直接数群元素，不需要额外的亏格表。令
$G=\mathrm {GL}_2(\mathbb F_p)$，
$H=C_{\rm ns}\rtimes\langle\sigma\rangle$，
$\sigma(z)=z^p$。对
$S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$，
椭圆点数为其在 $G/H$ 上的固定点数：

$$
e_2=\frac{|C_G(S)|\,|S^G\cap H|}{|H|}.
\tag{330.7}
$$

外陪集元素 $z\mapsto az^p$ 的迹为零、行列式为 $-\mathrm N(a)$；满足行列式一者有 $p+1$ 个。它们均具有特征多项式 $T^2+1$。在 Cartan 内，当 $\chi_4(p)=-1$ 时另有两个根 $\pm i$；当 $\chi_4(p)=1$ 时没有，因为标量 $\pm i$ 的迹不为零。相应中心化子阶分别为 $p^2-1$ 与 $(p-1)^2$，故

$$
e_2=
\begin{cases}
(p-1)/2,&p\equiv1\pmod4,\\
(p+3)/2,&p\equiv3\pmod4.
\end{cases}
\tag{330.8}
$$

总分歧点数为

$$
b_2=c+e_2=p-\chi_4(p).
\tag{330.9}
$$

Riemann–Hurwitz 给

$$
g(Y^+)=g(Y^{-3})=
2g-1+\frac{p-\chi_4(p)}2.
\tag{330.10}
$$

反不变 Prym 的维数为

$$
g-1+\frac{p-\chi_4(p)}2.
\tag{330.11}
$$

在 $p>3$ 的 $j=0,t=\pm24$ 邻域，(330.1) 的导数 $-6t=\mp144$ 是 $p$ 进单位。故所加二层在这里有限 étale；例如 $t\equiv24\pmod p$ 时，

$$
v_p(t-24)=v_p(j)
\tag{330.12}
$$

因为 $j=-3(t-24)(t+24)$ 且 $t+24$ 为单位。式 (330.12) 不识别基底非分裂水平的稳定模型分支，也不提供尚未证明的 cotangent 注入。

## 3. 保留模二 sign 的 Chen 关系

在有理同源范畴中工作。令 $J(2p)$ 为全级模曲线所有几何分量的 Picard 簇所组成的有理 abelian variety；它有

$$
G_2\times G_p
=\mathrm {GL}_2(\mathbb F_2)\times
\mathrm {GL}_2(\mathbb F_p)
$$

的交换作用。模二 sign 投影为

$$
e_{\rm sgn}
=\frac16\sum_{\gamma\in S_3}
\operatorname {sgn}(\gamma)\gamma,\qquad
M=e_{\rm sgn}J(2p).
\tag{330.13}
$$

它在 $\mathbb Q$ 上定义，与 $G_p$ 及所有 $T_\ell$（$\ell\nmid2p$）交换。$G_2/A_3$ 的非平凡特征就是 sign，故 $Y^+$ 的反不变 Prym 为

$$
P_p=M^{N_{\rm ns}}.
\tag{330.14}
$$

令 $N_{\rm sp}$ 为分裂 Cartan 正规化子，$B_p$ 为 Borel。de Smit–Edixhoven（2000）Theorem 2(2) 是任意带 $G_p$ 作用的有理线性加法范畴对象的函子性恒等式：

$$
M^{N_{\rm sp}}\oplus M^{G_p}
\simeq M^{N_{\rm ns}}\oplus M^{B_p}.
\tag{330.15}
$$

这里 $M^{G_p}$ 是 $J(2)$ 的 sign 部分，而 $X(2)$ 亏格零，所以它为零。于是

$$
M^{N_{\rm sp}}\simeq P_p\oplus M^{B_p}.
\tag{330.16}
$$

这一步用的是一般对象的原始定理，而不是把仅有素数层的 Jacobian 同源未经证明地套到混合层。

还需跟踪模二标记。通常把两个有序互补 $p$ 子群变成一个阶 $p^2$ 循环子群的模构造，使用一个 $p$ 次同源及其对偶。因 $p$ 为奇数，它们在二挠点上给同构，复合为 $[p]=1$。因此这套构造连同完整模二标记在 $\mathbb Q$ 上成立，交换两个 $p$ 子群恰给部分 Atkin–Lehner $W_{p^2}$，没有额外的模二换位。

故 $M^{N_{\rm sp}}$ 对应

$$
S_2\bigl(\Gamma(2)\cap\Gamma_0(p^2)\bigr)_{\rm sgn}^{W_{p^2}=+1},
\tag{330.17}
$$

而 $M^{B_p}$ 对应

$$
S_2\bigl(\Gamma(2)\cap\Gamma_0(p)\bigr)_{\rm sgn}.
\tag{330.18}
$$

这些对应与远离 $2p$ 的 Hecke 算子相容。

## 4. 为什么准确新层是 4p²，以及 W4 的固定符号

采用归一化的权二右作用

$$
(f|_2\gamma)(z)=
\det(\gamma)(cz+d)^{-2}f(\gamma z).
\tag{330.19}
$$

正标量矩阵作用平凡，标准 Atkin–Lehner 算子为对合。对于任意奇数 $m$，令

$$
D=\begin{pmatrix}2&0\\0&1\end{pmatrix}.
$$

直接核矩阵条目可得正确方向的群共轭

$$
D\Gamma_0(4m)D^{-1}
=\Gamma(2)\cap\Gamma_0(m).
\tag{330.20}
$$

所以 $h\mapsto h|_2D$ 将右边群的形式带到 $S_2(\Gamma_0(4m))$。商群
$\Gamma_0(m)/(\Gamma(2)\cap\Gamma_0(m))$ 是 $S_3$。

### 4.1 完整排除二处旧部分

固定一个远离二的归一化 Hecke 特征系，并逐个复嵌入考虑。Atkin–Lehner 新旧分解给出以下有限 $S_3$ 模；其分解也可从维数直接恢复：

| 该特征系在二处的原始导子指数 | 层 $4m$ 的当地空间维数 | $S_3$ 不变量维数 | 一个 Borel $C_2$ 的不变量维数 | $S_3$ 模 |
|---|---:|---:|---:|---|
| $0$ | $3$ | $1$ | $2$ | $1\oplus\mathrm {Std}$ |
| $1$ | $2$ | $0$ | $1$ | $\mathrm {Std}$ |
| $2$ | $1$ | $0$ | $0$ | $\mathrm {sgn}$ |

说明其维数：从原始层提升到二指数为二的层，有通常的 $f(z),f(2z),f(4z)$ 三条退化，或其中的两条、一条。$S_3$ 不变量是遗忘模二结构的原始奇层；一个 Borel 的不变量是保留一个非零二挠点的中间层。新形式在其原始层以下没有该 Hecke 特征系。

最后，$S_3$ 的三个不可约表示仅为 $1,\mathrm {sgn},\mathrm {Std}$，维数为 $1,1,2$；其 $S_3$ 不变量维数为 $1,0,0$，$C_2$ 不变量维数为 $1,0,1$。表中的数值唯一决定最后一列。这也证明没有隐藏的二处旧形式留在 sign 投影中。若在奇数处还有多条旧退化，每条仅给相同的上述当地模，不改变结论。

因此，sign 投影准确等于二指数恰为二的新部分；它不含层 $m$ 或 $2m$ 的旧贡献。

### 4.2 不经过局部根号表的 W4 计算

取任意整数 $A,B,C,E$ 满足

$$
4AE-mBC=1.
$$

部分 Atkin–Lehner 可取

$$
W_4=\begin{pmatrix}4A&B\\4mC&4E\end{pmatrix},
\qquad \det W_4=4.
\tag{330.21}
$$

式 (330.20) 下，

$$
\frac12DW_4D^{-1}
=\begin{pmatrix}2A&B\\mC&2E\end{pmatrix}
=\delta\in\Gamma_0(m).
\tag{330.22}
$$

$B,C$ 都是奇数，故 $\delta$ 模二恰为换位
$\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$。若 $h$ 属于 sign 分量，$h|_2\delta=-h$，因此

$$
(h|_2D)|_2W_4=-h|_2D.
\tag{330.23}
$$

所以所有该分量中的新形式满足

$$
W_4=-1.
\tag{330.24}
$$

这同时检查了局部导子为 $2^2$，以及实际使用的归一化符号。不能把这个 sign 类型当作导子仅含 $2^1$ 的 Steinberg 类型。

## 5. p 处旧部分的准确消去

设 $\mathcal F_p$ 为层恰为 $4p^2$、平凡 nebentypus、权二的新形式的 Galois 轨道，其中保留

$$
W_4 f=-f,\qquad W_{p^2}f=f.
\tag{330.25}
$$

由第四节，$W_4=-1$ 对其中所有二处新形式实际上自动成立。若 $A_f$ 为该新形式轨道的标准模 abelian variety，则有 Hecke 相容的有理同源

$$
P_p\sim_{\mathbb Q}\prod_{[f]\in\mathcal F_p}A_f.
\tag{330.26}
$$

以下核对没有漏留旧部分。先在 (330.17)–(330.18) 中取模二 sign，再作 (330.20)。二处原始指数已严格为二，可能的原始层只有 $4,4p,4p^2$。层 $4$ 的权二尖点空间为零，因为 $X_0(4)\simeq X(2)$ 亏格零。

对原始层 $4p$ 的一个新形式，在层 $4p^2$ 有两条 $p$ 退化。用归一化的旧基 $f$、$f|_2\left(\begin{smallmatrix}p&0\\0&1\end{smallmatrix}\right)$，部分 $W_{p^2}$ 交换这两个方向，并乘相同的 $W_p$ 符号。因而该二维空间中的 $W_{p^2}=+1$ 部分准确为一维。这可以直接从当地矩阵

$$
\begin{pmatrix}0&-1\\p^2&0\end{pmatrix}
=
\begin{pmatrix}0&-1\\p&0\end{pmatrix}
\begin{pmatrix}p&0\\0&1\end{pmatrix},
\qquad
\begin{pmatrix}p&0\\0&1\end{pmatrix}
\begin{pmatrix}0&-1\\p^2&0\end{pmatrix}
=p\begin{pmatrix}0&-1\\p&0\end{pmatrix}
\tag{330.27}
$$

读出；相应的全局部分算子在二处保留模二标记。退化与该标记的作用交换。

所以 (330.17) 的 $p$ 旧部分恰由每个层 $4p$ 新形式贡献一份，恰好是 (330.18) 的整个空间；二处更低的层已被 sign 杀掉，层 $4$ 也为空。它们在有理同源范畴的 (330.16) 中逐个 Hecke 特征系相消，留下且只留下 (330.25)，证明 (330.26)。

同样，对基底 $X$ 应用 (330.15) 而不取模二 sign，层一的旧贡献为零，层 $p$ 的一份 $W_{p^2}=+1$ 旧贡献被 $M^{B_p}$ 消去。得到通常的

$$
J_X\sim_{\mathbb Q}
\prod_{\substack{[h]\text{ new of level }p^2\\W_{p^2}h=h}}A_h.
\tag{330.28}
$$

全部新形式均有平凡 nebentypus。归一化权二 Fricke 特征值 $\lambda_N$ 的函数方程根号为 $-\lambda_N$；这一符号可直接对
$\int_0^\infty f(iy/\sqrt N)y^{s-1}\,dy$ 作 $y\mapsto1/y$ 变换得到。由互素部分 Atkin–Lehner 的乘法性，

$$
\lambda_{4p^2}(f)=\lambda_4(f)\lambda_{p^2}(f)=-1
\quad([f]\in\mathcal F_p).
\tag{330.29}
$$

故未扭曲 Prym 的每个新形式根号为 $+1$。相比之下，(330.28) 的每个 $h$ 根号为 $-1$，因而 $L(h,1)=0$。下一节说明实际 Prym 也被迫中心为零。

## 6. 实际 −3 扭曲与两项 Gauss 和的符号证明

### 6.1 有理下降只扭曲反不变部分

在 $\mathbb Q(\sqrt{-3})$ 上，(330.1) 的两条曲线由 $s=\sqrt{-3}\,t$ 识别，非平凡 Galois 元的下降余循环是 $\iota$。有理同源分解

$$
J_{Y^+}\sim_{\mathbb Q}J_X\times P_p
\tag{330.30}
$$

由 $(1+\iota)/2$、$(1-\iota)/2$ 两个投影给出。$\iota$ 在前一因子作用为一，在后一因子作用为负一。因此实际下降精确为

$$
J_{Y^{-3}}\sim_{\mathbb Q}
J_X\times P_p^{(\chi_{-3})}
\sim_{\mathbb Q}
J_X\times\prod_{[f]\in\mathcal F_p}A_{f\otimes\chi_{-3}}.
\tag{330.31}
$$

这里没有把整个 $J_X$ 也扭曲。

### 6.2 直接计算 Fricke 翻号

为避免没有核准的扭曲根号约定，下面直接证明本题所需的公式。令
$N=4p^2$，$\chi=\chi_{-3}$ 为模三的非平凡二次特征，
$\tau(\chi)=e^{2\pi i/3}-e^{4\pi i/3}=i\sqrt3$。对于 (330.25) 的新形式 $f$，置

$$
g(z)=\frac{f(z+1/3)-f(z+2/3)}{\tau(\chi)}
    =\sum_{n\ge1}\chi(n)a_n(f)e^{2\pi inz}.
\tag{330.32}
$$

它是 $\Gamma_0(9N)$ 上的权二尖点形式。也可直接检查这点：若
$\gamma=\left(\begin{smallmatrix}a&b\\9Nc&d\end{smallmatrix}\right)$，
则 $a\equiv d\pmod3$，所以
$T_{u/3}\gamma T_{u/3}^{-1}\in\Gamma_0(N)$，
其中 $T_{u/3}=\left(\begin{smallmatrix}1&u/3\\0&1\end{smallmatrix}\right)$，
$u=1,2$。平移保持各尖点的尖点性。有限 Gauss 和给 (330.32) 的精确系数。

对 $u\in\{1,2\}$，选 $v\in\{1,2\}$ 使
$Nuv\equiv-1\pmod3$，并令

$$
\gamma_u=
\begin{pmatrix}
(1+Nuv)/3&u\\Nv&3
\end{pmatrix}\in\Gamma_0(N).
\tag{330.33}
$$

行列式为一，而且有逐项可核的恒等式

$$
T_{u/3}
\begin{pmatrix}0&-1\\9N&0\end{pmatrix}
=
3\gamma_u
\begin{pmatrix}0&-1\\N&0\end{pmatrix}
T_{v/3}.
\tag{330.34}
$$

若 $f|_2W_N=\lambda_N f$，利用正标量三作用平凡及
$\chi(u)=\chi(-N)\chi(v)$，对两项求和得到

$$
g|_2W_{9N}=\lambda_N\chi(-N)g.
\tag{330.35}
$$

本题 $N=4p^2$ 是与三互素的平方，故

$$
\chi(-N)=-1,\qquad\lambda_N=-1,
\qquad g|_2W_{36p^2}=g.
\tag{330.36}
$$

因此 $g=f\otimes\chi_{-3}$ 的中心根号为 $-1$，严格有

$$
L(f\otimes\chi_{-3},1)=0
\quad([f]\in\mathcal F_p).
\tag{330.37}
$$

这里准确新层为 $9N=36p^2$。在三处，原形式的不分歧二维 Weil 表示乘以导子指数一的非平凡温和二次特征，没有惯性不变量，Swan 项为零，故导子指数恰为二。在二、$p$ 处只作不分歧扭曲，导子指数仍为二；别处不变。这个导子检查也排除了将 (330.32) 错认成某个更低层旧形式而丢失真实谱的可能。

全部上述恒等式对每个系数域嵌入均成立，因为特征值为有理数 $\pm1$，$\chi$ 也为有理值。

## 7. 严格结论与仍然缺少的输入

合并 (330.28)、(330.31)、(330.37)，$J_{Y^{-3}}$ 的每个有理简单模因子的每个新形式分量均满足中心 $L$ 值为零。因此：

1. $J_{Y^{-3}}$ 没有由中心 $L$ 值非零的新形式组成的非零商；其通常的解析秩零绕行商为零。
2. 对任何非零有理商 $B$，其标准 $L$ 函数满足 $L(B,1)=0$。其解析消失阶至少为 $\dim B$，因为每个系数域嵌入都至少贡献一阶。
3. 不能把未扭曲 $P_p$ 中可能非零的 $L(f,1)$ 直接用于实际判别式 $-3$ 分支；实际需要的是 (330.37) 中已被根号强迫为零的扭曲值。

第二点是解析断言。本文没有从它无条件推得 $\operatorname {rank} B(\mathbb Q)>0$，没有假定 BSD，也没有完成在实际 $p$ 进 CM 点处的形式浸入。

这条路线仍可研究中心导数、正秩商的高度，或再加入真正不同的全局结构；但“只加二除判别式标记即可恢复中心值非零的商”已经被完整排除。R326 的精确全局同余整数仍可能具有随参数增长的素因子，本文没有给它统一上界。主目标保持 OPEN。

## 8. 来源与证明范围

- Bart de Smit, Bas Edixhoven, *Sur un résultat d'Imin Chen*, Mathematical Research Letters **7** (2000), 147–154，Theorem 2(2)；作者原稿第 2 页列出一般对象的函子性恒等式，第 2–3 页以有理置换模给出证明。已直接读取：[作者原文](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。本文将其用于交换的模二 sign 投影，并逐项证明混合层的模解释及旧部分消去。
- Bas Edixhoven, *On a result of Imin Chen*, (1.0.3)–(1.0.4) 及紧接的说明：有序两个 $p$ 子群、阶 $p^2$ 循环子群和 $W_{p^2}$ 的对应；已直接读取[作者原稿](https://arxiv.org/pdf/alg-geom/9604008)。该原稿的群论方法由上述已发表文献给出一般定理；本文另外核对二挠点运输，未将混合层当作不加说明的现成推论。
- A. O. L. Atkin, J. Lehner, *Hecke operators on Γ0(m)*, Mathematische Annalen **185** (1970), 134–160，标准新旧分解；Wen-Ch'ing Winnie Li, *Newforms and functional equations*, Mathematische Annalen **212** (1975), 285–315。本文使用已发表的新形式/退化分解这一标准输入。所需的精确维数及两个素数处旧空间如何消去，已在第四、五节列明。
- 新旧分解的明确式及退化与 Fricke 交换公式也已逐式核对 David Zywina, *Computing actions on cusp forms*, §4.4 式 (4.4)、Lemma 4.5（作者原稿第 13–14 页）；[作者全文](https://davidzywina.github.io/papers/AtkinLehner/AtkinLehner.pdf)。这里只核对上项已发表的标准理论，没有使用其尚未计算的算法输出；其 $W_N$ 额外带 $N^{k/2}$ 的约定与本文不同，本文始终采用 (330.19)。
- R263/R289：实际判别式平方类及 (330.4)；R294/R315：实际 $p$ 进深度与标量特殊纤维映射。本条没有借此断言非分裂层的同一稳定分支点。

本条新的根号判断不依赖未取到全文的 Atkin–Li 扭曲公式：所用的 $W_4$ 符号及 $\chi_{-3}$ 翻号均已由 (330.21)–(330.24)、(330.32)–(330.36) 直接证明。所有产物均为纯证明，无数值扫描或未声明的秩计算。
