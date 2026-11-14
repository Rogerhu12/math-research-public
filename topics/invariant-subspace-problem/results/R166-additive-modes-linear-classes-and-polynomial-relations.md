# R166：有限加性慢模式的线性类与全部多项式关系

日期：2026-11-12（UTC）。作者：literature。

状态：完整自含证明。一般加性场论现象通过最小首单项式直接证明，并在本课题的忠实形式演算中实现。结论是代数独立性、关系理想及真实清分母接口；不把多变量非零演算自动宣称为单射稠密。

## 1. 设置与主定理

沿用 R32 的忠实代数嵌入
$$
\iota:\mathcal A\longrightarrow\mathbb C[[z]].
\tag{1.1}
$$
$\mathcal A$ 是实际 $A$ 的含单位范数多项式闭包，交换且无零因子。

沿用 R151：
$$
\mathcal G
=\left\{
E\in\mathcal A:
\begin{array}{l}
\exists\text{ 真正一元解析 }f_n,\ 
\|E-f_n(A)\|\to0,\\
\tau_4(E-f_n(A))\to\infty
\end{array}
\right\}.
\tag{1.2}
$$
本稿只需已证的三个性质：

- $\mathcal G$ 是含常数的交换无零因子子代数；
- $\mathcal G$ 在所有 dyadic gauge $\gamma_\zeta$ 下稳定；
- $\iota(\gamma_\zeta E)(z)=\iota(E)(\zeta z)$。

令
$$
K=\operatorname{Frac}\iota(\mathcal G)
\subseteq L:=\mathbb C((z)),
\tag{1.3}
$$
并在不致混淆时把 $\mathcal G$ 与其忠实像识别。
$K$ 是代数分式域；此定义不声称每个分式在 $H$ 上有界。

取有限个
$$
S_1,\ldots,S_d\in\mathcal A,\qquad
\sigma_i=\iota(S_i),
\tag{1.4}
$$
满足对每个 $\zeta\in\Gamma:=\mu_{2^\infty}$，
$$
\gamma_\zeta S_i-S_i\in\mathcal G.
\tag{1.5}
$$
等价地，记
$$
\alpha_\zeta f(z)=f(\zeta z),\qquad
h_{\zeta,i}=\alpha_\zeta\sigma_i-\sigma_i,
$$
则
$$
h_{\zeta,i}\in\iota(\mathcal G)\subseteq K.
\tag{1.6}
$$

**定理1.1。** 如果 $\sigma_1,\ldots,\sigma_d$ 在 $L/K$ 中的类对 $\mathbb C$ 线性无关，即
$$
\sum_{i=1}^dc_i\sigma_i\in K,\quad c_i\in\mathbb C
\quad\Longrightarrow\quad c_1=\cdots=c_d=0,
\tag{1.7}
$$
则 $\sigma_1,\ldots,\sigma_d$ 在 $K$ 上代数无关。

更一般，令
$$
r=\dim_{\mathbb C}
\operatorname{span}_{\mathbb C}\{[\sigma_1],\ldots,[\sigma_d]\}
\subseteq L/K.
\tag{1.8}
$$
则存在 $C=(C_{\nu i})\in GL_d(\mathbb C)$，使
$$
T_\nu=\sum_iC_{\nu i}S_i,\qquad
\tau_\nu=\iota(T_\nu)
\tag{1.9}
$$
满足：

1. $\tau_1,\ldots,\tau_r$ 在 $K$ 上代数无关；
2. $\tau_\nu=k_\nu\in K$，$r<\nu\le d$；
3. 在这些新变量中，全部 $K$ 系数多项式关系恰为
$$
\boxed{
\ker\!\left(K[v_1,\ldots,v_d]\to L,\ v_\nu\mapsto\tau_\nu\right)
=(v_{r+1}-k_{r+1},\ldots,v_d-k_d).
}
\tag{1.10}
$$

因此
$$
\boxed{
K(\sigma_1,\ldots,\sigma_d)
=K(\tau_1,\ldots,\tau_r),\qquad
\operatorname{trdeg}_K K(\sigma_1,\ldots,\sigma_d)=r.
}
\tag{1.11}
$$
这里右侧是纯超越扩张；$r=0$ 时就是 $K$。

下面完整证明固定域、首单项式最小化、平移符号、最高两层及真实清分母。

## 2. 固定域恰是 $\mathbb C$

由于 $\mathcal G$ gauge 稳定，每个 $\alpha_\zeta$ 都限制为 $K$ 的自同构。
显然常数被全部 $\alpha_\zeta$ 固定。

反之，设
$$
f(z)=\sum_{n\ge n_0}c_nz^n\in L
$$
在全部 $\zeta\in\Gamma$ 下固定。则
$$
(\zeta^n-1)c_n=0
\quad\text{对所有 }n,\zeta.
$$
若 $n\ne0$，可取充分高阶的 $2$ 次幂单位根，使 $\zeta^n\ne1$。
所以所有 $c_n$（$n\ne0$）为零。
负 Laurent 次数也由同一论证排除。
因此
$$
\boxed{
L^\Gamma=\mathbb C,\qquad K^\Gamma=\mathbb C.
}
\tag{2.1}
$$
本稿后面的“固定即常数”始终在这个具体场内使用，没有假定更大的扩张也没有新常数。

## 3. 关系理想上的准确半线性作用

记
$$
\operatorname{ev}_\sigma:
K[w_1,\ldots,w_d]\longrightarrow L,\qquad
P\longmapsto P(\sigma_1,\ldots,\sigma_d),
$$
及
$$
I=\ker\operatorname{ev}_\sigma.
\tag{3.1}
$$

令 $\alpha_\zeta P$ 表示只对系数施加 $\alpha_\zeta$。
定义
$$
\boxed{
\Lambda_\zeta P(w)
=(\alpha_\zeta P)(w+h_\zeta),
\qquad
h_\zeta=(h_{\zeta,1},\ldots,h_{\zeta,d}).
}
\tag{3.2}
$$
这是 $K[w]$ 的半线性自同构。
其平移号为正号，因为
$$
\sigma+h_\zeta=\alpha_\zeta\sigma.
$$
所以
$$
\begin{split}
(\Lambda_\zeta P)(\sigma)
&=(\alpha_\zeta P)(\sigma+h_\zeta)\\
&=(\alpha_\zeta P)(\alpha_\zeta\sigma)\\
&=\alpha_\zeta(P(\sigma)).
\end{split}
\tag{3.3}
$$
特别 $I$ 被每个 $\Lambda_\zeta$ 保持。

这些作用确实构成群作用。
由
$$
h_{\zeta\eta}
=h_\zeta+\alpha_\zeta h_\eta,
\tag{3.4}
$$
直接得到
$$
\Lambda_\zeta\Lambda_\eta=\Lambda_{\zeta\eta}.
$$
因此不是只得一个朝单向保持关系的替换操作。

## 4. 最小首单项式强迫关系精确不变

假设 $I\ne\{0\}$。
在 $\mathbb N^d$ 上固定一个按总次数优先的 graded lexicographic 单项式序。

这个序是良序：任意非空单项式集合先有最小总次数，而固定次数只有有限多个单项式。
每个非零有限多项式则有一个最大的首单项式。

从 $I\setminus\{0\}$ 的首单项式集合中取最小者，并选取相应多项式 $P$。
除以它的非零首系数，使其首系数为 $1$。

由于 $I$ 中不存在非零常数，$p:=\deg P\ge1$。

平移 $w\mapsto w+h_\zeta$ 只会从每个单项式产生更低总次数的附加项；
最高总次数层的各单项式和系数只受到 $\alpha_\zeta$ 作用。
首系数 $1$ 保持不变。因此
$$
\operatorname{LM}(\Lambda_\zeta P)=\operatorname{LM}(P)
$$
且两者首系数都为 $1$。

如果 $\Lambda_\zeta P-P\ne0$，它仍属于 $I$，
但其首单项式严格小于 $\operatorname{LM}(P)$。
这与选择最小性矛盾。
所以
$$
\boxed{\Lambda_\zeta P=P\quad\text{对全部 }\zeta\in\Gamma.}
\tag{4.1}
$$

这里不需要假设某个关系理想预先是主理想，
也不使用多个 gauge 方程在同一 Hilbert 核上同时成立的断言。
(4.1) 是形式关系理想中的精确多项式恒等式。

## 5. 最高两层产生常系数线性关系

把 $P$ 分成齐次层：
$$
P=P_p+P_{p-1}+\cdots+P_0.
$$

### 5.1. 最高齐次层的系数是常数

取 (4.1) 的总次数 $p$ 层，得到
$$
\alpha_\zeta P_p=P_p.
$$
由 $K^\Gamma=\mathbb C$，
$$
\boxed{
P_p(w)=\sum_{|\alpha|=p}c_\alpha w^\alpha,\qquad
c_\alpha\in\mathbb C.
}
\tag{5.1}
$$
而 $P_p\ne0$。

### 5.2. 次高层的精确式

平移 $P_p(w+h_\zeta)$ 的总次数 $p-1$ 层恰为
$$
\sum_{i=1}^dh_{\zeta,i}\partial_iP_p(w).
$$
平移 $P_{p-1}$ 在这一层只保留其原齐次项。
因此 (4.1) 给
$$
\boxed{
\alpha_\zeta P_{p-1}(w)
+\sum_{i=1}^dh_{\zeta,i}\partial_iP_p(w)
=P_{p-1}(w).
}
\tag{5.2}
$$

写
$$
P_{p-1}(w)=\sum_{|\beta|=p-1}b_\beta w^\beta,\qquad b_\beta\in K,
$$
并定义常数
$$
v_{\beta,i}=(\beta_i+1)c_{\beta+e_i},
\tag{5.3}
$$
其中未出现的 $c_\alpha$ 取零。
逐系数比较 (5.2)，有
$$
\alpha_\zeta b_\beta+\sum_iv_{\beta,i}h_{\zeta,i}=b_\beta.
\tag{5.4}
$$

由于 $P_p$ 是正次数、特征零域上的非零齐次多项式，至少一个偏导数非零。
故存在 $\beta$ 使向量
$$
v_\beta=(v_{\beta,1},\ldots,v_{\beta,d})\ne0.
\tag{5.5}
$$
固定这样的 $\beta$。
由 $h_{\zeta,i}=\alpha_\zeta\sigma_i-\sigma_i$，(5.4) 等价于
$$
\alpha_\zeta\left(b_\beta+\sum_iv_{\beta,i}\sigma_i\right)
=b_\beta+\sum_iv_{\beta,i}\sigma_i.
$$
括号内是 $L$ 的元素；由 $L^\Gamma=\mathbb C$，存在 $c\in\mathbb C$ 使
$$
b_\beta+\sum_iv_{\beta,i}\sigma_i=c.
$$
因此
$$
\boxed{
\sum_iv_{\beta,i}\sigma_i=c-b_\beta\in K,\qquad
v_\beta\ne0.
}
\tag{5.6}
$$

所以任何非零多项式关系都会迫使各 $\sigma_i$ 的类在 $L/K$ 中出现非零常系数线性关系。
其逆否命题正是定理1.1 的第一部分。

## 6. 一般关系的完整分类

在有限维 $\mathbb C$ 向量空间 $\mathbb C^d$ 上考虑线性映射
$$
(c_1,\ldots,c_d)\longmapsto\sum_ic_i[\sigma_i]\in L/K.
$$
其像维数为 $r$。
选取 $\mathbb C^d$ 的一组基，使前 $r$ 个基向量映到像的一组基，余下基向量形成核的基。
以它们为行得到 $C\in GL_d(\mathbb C)$，即 (1.9)。

于是 $[\tau_1],\ldots,[\tau_r]$ 对 $\mathbb C$ 线性无关，
而 $\tau_\nu=k_\nu\in K$（$\nu>r$）。
每个 $T_\nu$ 仍满足 (1.5)，因为 $\mathcal G$ 对常系数线性组合封闭。
定理第一部分因此给前 $r$ 个 $\tau_\nu$ 的 $K$ 代数独立性。

现在取 $P\in K[v_1,\ldots,v_d]$。
依次把 $v_\nu$（$\nu>r$）替换为 $k_\nu$，得到唯一余式
$$
R(v_1,\ldots,v_r).
$$
逐个一变量多项式除法给
$$
P
=R+\sum_{\nu=r+1}^d
Q_\nu(v)(v_\nu-k_\nu),
\qquad Q_\nu\in K[v].
\tag{6.1}
$$
若 $P(\tau)=0$，则 $R(\tau_1,\ldots,\tau_r)=0$。
代数独立性迫使 $R=0$。
反之右侧理想显然全部在关系核内。
这证明 (1.10)。

因此全部关系来自余下方向的 $K$ 仿射表达式，
而不是额外的高次不可约代数曲面。
(1.11) 也立即成立。

原变量中的关系由可逆常系数变换 $v=Cw$ 还原：
$$
\sum_iC_{\nu i}w_i-k_\nu,\qquad \nu>r.
\tag{6.2}
$$
这里的线性部分系数确为 $\mathbb C$ 常数；只允许常数项落在 $K$。

## 7. 回到实际有界算子：分母只作有限清除

### 7.1. $K$ 系数多项式的零关系可由有界演算检测

取
$$
P(w)=\sum_\alpha c_\alpha w^\alpha\in K[w].
$$
它只有有限多个系数。
可选非零 $b\in\mathcal G$，使每个 $bc_\alpha$ 都在 $\mathcal G$。
然后定义实际有界算子
$$
T_{bP}
=\sum_\alpha (bc_\alpha)S_1^{\alpha_1}\cdots S_d^{\alpha_d}
\in\mathcal A.
\tag{7.1}
$$
此处 $bc_\alpha$ 通过 $\mathcal G$ 的忠实嵌入识别为实际算子。
所有和及乘积均有限，不涉及无穷级数求值。

由 R32 的乘法忠实性，
$$
\iota(T_{bP})=\iota(b)P(\sigma).
$$
因为 $\iota(b)\ne0$，得到
$$
\boxed{
P(\sigma)=0
\quad\Longleftrightarrow\quad
T_{bP}=0.
}
\tag{7.2}
$$

此检测不依赖所选分母。
若另选 $b'\ne0$，则
$$
b'T_{bP}=bT_{b'P},
\tag{7.3}
$$
可由两边的形式系数或有限系数恒等式验证。
$\mathcal A$ 无零因子，所以一边的未乘分母算子为零当且仅当另一边为零。

本节没有在 $H$ 上使用有界的 $b^{-1}$；
分母只用于有限乘法和忠实消去。

### 7.2. 仿射关系在实际模型中成立

对每个 $\nu>r$，写
$$
k_\nu=\iota(a_\nu)/\iota(b_\nu),
\qquad a_\nu,b_\nu\in\mathcal G,\quad b_\nu\ne0.
$$
因为 $\tau_\nu=k_\nu$，
$$
\iota(b_\nu T_\nu-a_\nu)=0.
$$
故实际有界恒等式为
$$
\boxed{b_\nu T_\nu=a_\nu.}
\tag{7.4}
$$
这不是只在形式域中成立的关系。

### 7.3. $\mathcal G$ 系数关系理想须准确写成饱和

在新变量 $v$ 中置
$$
J_0=(b_\nu v_\nu-a_\nu:\nu>r)
\subseteq\mathcal G[v_1,\ldots,v_d],
$$
并令
$$
\mathcal S=\mathcal G\setminus\{0\}.
$$
则实际有界多项式演算的关系理想恰为
$$
\boxed{
\ker\!\left(\mathcal G[v]\to\mathcal A,\ 
v_\nu\mapsto T_\nu\right)
=
\{F:\exists s\in\mathcal S,\ sF\in J_0\}.
}
\tag{7.5}
$$

证明如下。
若 $sF\in J_0$，代入 (7.4) 得 $sF(T)=0$。
由 $s\ne0$ 和 $\mathcal A$ 无零因子，$F(T)=0$。

反之若 $F(T)=0$，则形式关系分类 (1.10) 给
$$
F=\sum_{\nu>r}Q_\nu(v)(v_\nu-k_\nu)
=\sum_{\nu>r}\frac{Q_\nu(v)}{b_\nu}
(b_\nu v_\nu-a_\nu)
$$
在 $K[v]$ 内成立。
右侧只有有限多个系数和分母。
取其共同非零分母 $s\in\mathcal G$，
即得 $sF\in J_0$。

所以在 $\mathcal G[v]$ 中不能省去饱和步骤，误称未饱和的有限生成理想已经等于全部关系理想。
(7.5) 正是实际清分母后可忠实取消的完整表述。

## 8. 与已证明的单方向核定理衔接

本节只记录严格可归约的范围。

### 8.1. $r=0$

此时所有 $S_i$ 都在代数域 $K$ 内。
任何实际有界多项式组合 $F(S)$ 也在 $K\cap\mathcal A$ 内。
若它非零，存在非零 $b,a\in\mathcal G$ 使
$$
bF(S)=a.
$$
R151、R153 已处理这些分母及其全部不变子商实现。
本稿没有为此另立新的域论结果。

### 8.2. $r=1$

其余变量的 $K$ 仿射式使任意非零实际
$\mathcal G$ 系数多项式 $F(S)$ 在乘某个非零
$b\in\mathcal G$ 后写成
$$
bF(S)=P(T_1),\qquad P\in\mathcal G[t].
\tag{8.1}
$$
$T_1$ 仍满足全部 gauge 增量在 $\mathcal G$ 中。
R152 给非零 $P(T_1)$ 在全 $H$ 上单射稠密。
由 (8.1)，$F(S)$ 单射；再由实际 $\mathcal A$ 的共同 $C$ 对称性，$F(S)$ 的值域稠密。

这只是已完成的一方向定理在常系数方向归约后的应用。
没有把其全空间稠密性改写成任意不变限制稠密性。

### 8.3. $r\ge2$

(1.10)、(7.2) 和 (7.5) 仍完整成立，
但它们只决定何时实际演算等于零算子。
对非零实际多变量多项式 $F(S)$，
其 Hilbert 核是否为零、其值域是否稠密，仍需额外分析。

尤其不能把多个不同 gauge 的像空间同时当成某个单一跨核配对中的共同核。
也不能因形式多项式互素，就在两个以上变量中默认存在标量或 $\mathcal G$ 单位的 Bézout 组合。

## 9. 特殊情形与边界

- $d=1$ 时，结论为：若 $\sigma$ 对 $K$ 代数，则 $\sigma\in K$。
  这与 R152 的一方向“代数即有理”分支一致。
- 如果某个 $\sigma_i$ 本来就是 $K$ 元素，它的类为零，应在 §6 先归入仿射方向，不可拿来声称代数独立。
- 本稿没有给定任意一组具体慢系数后，自动判定其类是否在 $L/K$ 中线性独立。
  这一输入仍需对具体模式证明。
- 全部主分类是有限变量多项式及代数分式域的陈述。
  任意多变量收敛解析芽的零关系、演算域和 Hilbert 核，未因本稿自动解决。
- 本稿只使用固定域 $L^\Gamma=\mathbb C$、增量位于稳定子域 $K$ 及特征零。
  最小首单项式证明是自含的加性场论接口，不声称这种一般现象首次出现。

## 10. 依赖

R32：实际 $\mathcal A$ 的忠实形式系数、交换性及无零因子。

R151：$\mathcal G$ 的子代数性质、gauge 稳定性及其实际分母性质。

R152：单个加性慢方向的 $\mathcal G$ 系数多项式核定理，仅用于 §8.2 的已知范围衔接。

R153：$\operatorname{Frac}\mathcal G$ 的实际闭分式与不变子商实现，仅用于 §8.1 的定位说明。

R166 的主代数分类、符号方向、最小单项式论证和实际饱和关系式均在本稿完整证明。


## 11. 附录：稳定理想、有限 gauge 轨道证书与共同核

本节补充一个可严格使用的多方向接口。
它只排除有限族的共同核，不排除每个成员自己的核。

### 11.1. 独立方向的半线性多项式环没有非零真稳定理想

先设 $\sigma_1,\ldots,\sigma_r$ 在 $L/K$ 中对 $\mathbb C$ 线性无关，
并在 $K[w_1,\ldots,w_r]$ 上使用 §3 的作用 $\Lambda_\zeta$。

**命题11.1。** 如果理想 $J\subseteq K[w]$ 满足
$$
\Lambda_\zeta J=J\quad(\zeta\in\Gamma),
$$
则 $J=0$ 或 $J=K[w]$。

证明：若 $J$ 非零且真，则它不含非零常数。
像 §4 一样，在 $J\setminus\{0\}$ 中选首单项式最小、首系数为 $1$ 的多项式 $P$。
稳定性保证 $\Lambda_\zeta P-P\in J$；
首项消去和最小性再次给 $\Lambda_\zeta P=P$。

令 $p=\deg P\ge1$。
§5 的最高层和次高层推导不曾使用 $P(\sigma)=0$，
而只使用这个精确不变式。
故仍得到
$$
\sum_{i=1}^rv_i\sigma_i\in K
$$
且某个 $v_i\in\mathbb C$ 非零，矛盾。
证毕。

因此对于任意非零 $P\in K[w]$，其完整 gauge 轨道生成的理想
$$
J_P=(\Lambda_\zeta P:\zeta\in\Gamma)
$$
是非零稳定理想，必为全环。
由生成理想的定义，存在有限个 $\zeta_1,\ldots,\zeta_m\in\Gamma$
及 $U_i\in K[w]$，使
$$
\boxed{
\sum_{i=1}^mU_i(w)\Lambda_{\zeta_i}P(w)=1.
}
\tag{11.1}
$$
无需把“有限”从无穷求和的收敛中推得；理想中的元素本来就是有限组合。
这些有限个 $\zeta_i$ 可以包含在某个有限 dyadic 子群中，给未使用的群元素配零系数即可。

### 11.2. 原 $\mathcal G$ 系数演算的真实有限证书

现在取原来的
$$
P\in\mathcal G[w_1,\ldots,w_r]\setminus\{0\},\qquad
T=P(S_1,\ldots,S_r)\in\mathcal A.
$$
由定理1.1，$T\ne0$。

$\Lambda_\zeta P$ 的所有系数仍在 $\mathcal G$ 中：
这是因为系数的 gauge 像在 $\mathcal G$，
每个 $h_{\zeta,i}$ 也在 $\mathcal G$，而平移多项式只产生有限和、积。

更关键的是，形式代入准确对应实际 gauge 演算。
由 $\gamma_\zeta S_i=S_i+h_{\zeta,i}$，
$$
\boxed{
(\Lambda_\zeta P)(S_1,\ldots,S_r)
=\gamma_\zeta\!\left(P(S_1,\ldots,S_r)\right)
=\gamma_\zeta T.
}
\tag{11.2}
$$
这是实际 $\mathcal A$ 中的有限多项式恒等式，不只在形式级数域成立。

在 (11.1) 的有限多个 $U_i$ 系数中取共同非零分母 $D\in\mathcal G$，
令 $V_i=DU_i\in\mathcal G[w]$。
清分母后代入实际算子，并用 (11.2)，得到
$$
\boxed{
D=\sum_{i=1}^mV_i(S)\,\gamma_{\zeta_i}T,
\qquad D\in\mathcal G\setminus\{0\}.
}
\tag{11.3}
$$
每个 $V_i(S)$ 都是 $\mathcal A$ 中的有界算子。

代数式 (11.1) 的右侧是 $1$；
实际有界式 (11.3) 的右侧目标是 $D$。
这里没有声称 $D^{-1}$ 有界，也没有把两种等式混同。
例如若 $\chi(T)=0$，全部 $\gamma_{\zeta_i}T$ 的字符仍为零，
其 $\mathcal A$ 系数有限组合不可能等于 $I$；
这与 (11.3) 及下面的强闭包结论完全一致。

### 11.3. 混合依赖方向先归约再清分母

对 §1 的一般 $d$ 个模式，设
$$
T=F(S_1,\ldots,S_d)\ne0,\qquad F\in\mathcal G[w].
$$
先使用 §6 的常系数变换和剩余方向
$\tau_\nu=k_\nu\in K$，
将 $F$ 归约为独立的 $r$ 个方向上的 $K$ 系数多项式。
再有限清分母，得到某个非零 $b\in\mathcal G$ 及
$$
P\in\mathcal G[v_1,\ldots,v_r]\setminus\{0\}
$$
满足实际恒等式
$$
bT=P(T_1,\ldots,T_r).
\tag{11.4}
$$

对右侧应用 (11.3)，
$$
D=\sum_iV_i(T_1,\ldots,T_r)\,
\gamma_{\zeta_i}(bT)
=\sum_i
\left[V_i(T_1,\ldots,T_r)\gamma_{\zeta_i}(b)\right]
\gamma_{\zeta_i}T.
\tag{11.5}
$$
括号内仍在 $\mathcal A$ 中。

若 $r=0$，$T\in K\cap\mathcal A$，
直接取 $bT=D\in\mathcal G\setminus\{0\}$ 即可。
因此以下有限实际证书对所有非零的原 $\mathcal G$ 系数多项式演算成立：
$$
\boxed{
D=\sum_{i=1}^mB_i\,\gamma_{\zeta_i}T,\qquad
0\ne D\in\mathcal G,\quad B_i\in\mathcal A.
}
\tag{11.6}
$$

### 11.4. 全部不变子商的共同核为零、总值域稠密

令 $Q=M/N$ 为任意非零闭 $A$ 不变子商，
$N\subseteq M\in\operatorname{Lat}A$。
因为所有参与算子属于 $\mathcal A$，
它们保持 $M,N$，并在 $Q$ 上诱导有界交换算子。
(11.6) 下降为
$$
D_Q=\sum_iB_{i,Q}(\gamma_{\zeta_i}T)_Q.
\tag{11.7}
$$
R151、R153 给非零 $D\in\mathcal G$ 在 $Q$ 上单射稠密。

于是
$$
\boxed{
\bigcap_{i=1}^m
\ker(\gamma_{\zeta_i}T)_Q=\{0\}.
}
\tag{11.8}
$$
另一方面，交换性使
$$
B_{i,Q}(\gamma_{\zeta_i}T)_Qx
=(\gamma_{\zeta_i}T)_Q B_{i,Q}x
\in\operatorname{Ran}(\gamma_{\zeta_i}T)_Q.
$$
所以
$$
\operatorname{Ran}D_Q
\subseteq\sum_i\operatorname{Ran}(\gamma_{\zeta_i}T)_Q,
$$
进而
$$
\boxed{
\overline{\sum_{i=1}^m
\operatorname{Ran}(\gamma_{\zeta_i}T)_Q}=Q.
}
\tag{11.9}
$$
同一个有限族适用于全部这些子商，而不是逐子商重新选择 gauge。

所有式子也可对角有限放大。
各参与算子都在相应 $A^{(n)}$ 的范数多项式闭包内，
故保持其任意闭不变子空间及子商。
R151 的有限放大结论或下节的强单位同样给 (11.8)—(11.9)。

### 11.5. 有限轨道理想的强闭包含单位

定义实际有限轨道理想
$$
\mathfrak I_T
=\left\{\sum_{i=1}^mC_i\,\gamma_{\zeta_i}T:
C_i\in\mathcal A\right\}.
\tag{11.10}
$$
由 (11.6)，$D\in\mathfrak I_T$。

R151 已证明非零 $D\in\mathcal G$ 的强主理想单位性质：
$$
I\in\overline{D\,\mathbb C[A]}^{\,\rm SOT}.
\tag{11.11}
$$
每个 $Dp(A)$ 都仍在 $\mathfrak I_T$ 中，因为
$$
Dp(A)=\sum_i[p(A)B_i]\,\gamma_{\zeta_i}T.
$$
故
$$
\boxed{
I\in\overline{\mathfrak I_T}^{\,\rm SOT}.
}
\tag{11.12}
$$

这个结论也可直接解释 (11.8)—(11.9)。
强近似单位保持 $M,N$，在正交代表 $M\ominus N$ 上压缩后仍强趋单位；
若所有有限轨道成员都杀掉某个子商向量，整个近似单位都杀掉它，因此向量为零。
近似单位的像又落在总值域之和的闭包内，故其总值域稠密。

### 11.6. 本附录没有完成的单核问题

(11.8) 不推出任一单独
$(\gamma_{\zeta_i}T)_Q$ 的核为零。
(11.9) 也不推出每个单独成员的值域稠密。

证明 (11.1) 使用了整个轨道生成的稳定理想；
它不提供任意指定的两个轨道成员之间的单位 Bézout 式。
同样，不同 $\zeta_i$ 对应的 Hilbert 空间核或跨核配对目标，
不能在没有额外证明时合并成一个共同被所有算子消去的空间。

因此本附录给出了真实的有限轨道共同核证书与强理想单位，
但多独立慢方向的单个非零多项式演算排核仍保持开放。
