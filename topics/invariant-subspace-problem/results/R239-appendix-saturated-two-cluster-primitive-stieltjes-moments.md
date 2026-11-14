# R239 附录：饱和两簇 primitive 固定线的正矩表示与相邻上界

日期：2026-11-13（UTC）。作者：central_review；AI-assisted，GPT-6 Astra Pro。
状态：完整证明，主会话已全文核验。仅指定群固定一维线，一般 primitive 算子序仍开。

本补充承接 [R271 两簇全阶最小逆](R271-appendix-two-cluster-minimal-inverses-and-squared-all-height-comparison-lower-bounds.md) 的有限公式。它证明该稿所用**饱和两簇、群固定 primitive 一维线**上的相邻上界，不证明一般 primitive Gram 的算子序。

## 1. 对象、真实逆及范围

取整数
$$
q\ge1,\qquad n>q,
$$
在共计 $q+n$ 个布尔位上，前 $q$ 位权为 $1$，后 $n$ 位权为任意
$$
\varepsilon>0.
$$
不要求 $\varepsilon<1$。令删除算子为
$$
D=D_{\rm s}+\varepsilon D_{\rm w}.
$$
第 $p$ 孔层记作 $\mathcal H_p$，物理集合向量为正交基。强、弱簇的规范对称向量为
$$
e_i=\binom qi^{-1/2}\sum_{|I|=i}e_I,\qquad
w_j=\binom nj^{-1/2}\sum_{|J|=j}e_J.
$$
因此
$$
D_{\rm s}e_i=\sqrt{i(q-i+1)}e_{i-1},\qquad
D_{\rm w}w_j=\sqrt{j(n-j+1)}w_{j-1}.
\tag{1.1}
$$

置
$$
K_q=\ker D\cap\mathcal H_q,\qquad
F_k=\frac{D^k(D^*)^k|_{\mathcal H_q}}{(k!)^2},\qquad
\Gamma_k=P_{K_q}F_k^{-1}|_{K_q},
\quad 0\le k\le n-q.
\tag{1.2}
$$
其中 $F_0=I$、$\Gamma_0=I$。逆先在整个 $\mathcal H_q$ 上取，再压到 $K_q$；不是先压 $F_k$ 再求逆。所列范围内 $D^k:\mathcal H_{q+k}\to\mathcal H_q$ 满射，故 $F_k$ 正可逆。这个有限满射事实由 R271 §6.1 的加权 Lefschetz 相似直接给出，也可先在全等权下逐 primitive 串核验，再用可逆对角相似保持秩。

令置换群为
$$
\mathfrak G=S_q\times S_n.
$$
$\mathcal H_q^{\mathfrak G}$ 的维数是 $q+1$，而其中 primitive 核是一维。其单位向量为
$$
Z_\varepsilon=\sum_{j=0}^q\binom{n-q+j}{j}\varepsilon^{2j},
$$
$$
g_\varepsilon=
Z_\varepsilon^{-1/2}
\sum_{j=0}^q(-\varepsilon)^j
\sqrt{\binom{n-q+j}{j}}\ e_jw_{q-j}.
\tag{1.3}
$$
相邻项使用 (1.1) 恰好相消，所以 $Dg_\varepsilon=0$。

全部 $F_k^{-1}$、$P_{K_q}$ 与 $\mathfrak G$ 交换。因此
$\Gamma_k$ 保持固定线 $\mathbb Cg_\varepsilon$。记其本征值为
$$
\Gamma_kg_\varepsilon=\gamma_kg_\varepsilon.
\tag{1.4}
$$

以下所有标量结论都指这条固定线。特别，不把它们称为同一权模型整个 $K_q$ 上的算子不等式。

## 2. 正概率矩表示

**定理。** 定义
$$
m_k=\frac{q!\,\gamma_k}{(q+k)!},
\qquad 0\le k\le n-q.
\tag{2.1}
$$
存在一个在 $(0,\infty)$ 上、与 $k$ 无关的概率测度 $\mu$，使
$$
\boxed{m_k=\int_0^\infty x^k\,d\mu(x).}
\tag{2.2}
$$
测度有一个正权重的连续部分，所以不是有限支撑测度。

具体地，令
$$
p_j=\frac{\binom{n-q+j}{j}\varepsilon^{2j}}{Z_\varepsilon},
\qquad 0\le j\le q.
\tag{2.3}
$$
先以概率 $p_j$ 选择 $j$。条件于此 $j$：

- 若 $j=0$，令 $U_j=1$；
- 若 $1\le j\le q$，令 $U_j$ 具有 Beta 参数
  $q-j+1,j$；
- 令 $V_j$ 具有 Gamma 形状参数 $n-q+j+1$、率参数 $1$，并与 $U_j$ 独立。

取
$$
X_j=\frac{U_j}{\varepsilon^2V_j}.
\tag{2.4}
$$
$\mu$ 就是 $X_j$ 的上述有限概率混合。

等价地，未乘 $q!$ 的序列
$\gamma_k/(q+k)!$ 是总质量 $1/q!$ 的正测度矩。这个常数不省略。

### 2.1 从真实最小解到标量公式

令 $v_k$ 是
$$
D^kv_k=g_\varepsilon
$$
在整个 $\mathcal H_{q+k}$ 中的最小范数解。R271 §3 的有限公式为
$$
v_k=
\frac1{\sqrt{Z_\varepsilon}}
\sum_{j=0}^q
(-1)^j\varepsilon^{j-k}
\binom{k+q-j}{q-j}
\sqrt{\frac{(q-j)!\,(n-q-k+j)!}
{j!\,(q+k-j)!\,(n-q)!}}\,
e_jw_{q+k-j}.
\tag{2.5}
$$
它对任意正 $\varepsilon$ 成立；该有限代数推导没有使用其小于 $1$。

为保留真正最小性的量词，简述其核验。用弱簇逐层右逆
$$
Rw_j=\frac{w_{j+1}}{\sqrt{(j+1)(n-j)}}
$$
以及强簇有限幂零级数，展开
$$
\varepsilon^{-k}R^k
\sum_{\ell=0}^q
(-1)^\ell\binom{k+\ell-1}{\ell}
\varepsilon^{-\ell}D_{\rm s}^{\ell}R^\ell
$$
并作用于 (1.3)，有限二项求和给 (2.5)，且 $D^kv_k=g_\varepsilon$。
$k=0$ 直接由 (1.3) 解释。

在第 $q+k$ 和第 $q$ 层的 $\mathfrak G$ 固定空间之间，
$D^k$ 是同维三角矩阵，其对角元为
$$
\varepsilon^k
\sqrt{\frac{(q+k-j)!}{(q-j)!}
\frac{(n-q+j)!}{(n-q-k+j)!}}>0,
\qquad 0\le j\le q.
\tag{2.6}
$$
故固定空间内的解唯一。任取完整核中的向量，将其作群平均所得向量仍在核中，并因 (2.6) 为零。由于 $v_k$ 本身固定，它正交于完整核；这证明它是全空间最小解，不只是某个指定子空间中的解。

由 (1.2)，准确有
$$
\gamma_k=(k!)^2\|v_k\|^2.
\tag{2.7}
$$
把 (2.5) 的正交和范数展开，阶乘整理为
$$
\begin{aligned}
\gamma_k
&=\frac1{Z_\varepsilon}
\sum_{j=0}^q
\varepsilon^{2j-2k}
\frac{(q+k-j)!\,(n-q-k+j)!}
{(q-j)!\,j!\,(n-q)!}\\
&=\varepsilon^{-2k}
\sum_{j=0}^q p_j
\frac{(q-j+1)^{\overline k}}
{(n-q+j)^{\underline k}}.
\end{aligned}
\tag{2.8}
$$
上升阶乘和下降阶乘均以零阶为 $1$。所有分母在
$0\le k\le n-q$ 内严格为正。

### 2.2 积分逐项核验

对 $j\ge1$，使用 Beta 密度
$$
\frac{q!}{(q-j)!\,(j-1)!}
u^{q-j}(1-u)^{j-1}\,\mathbf1_{(0,1)}(u),
$$
直接积分得
$$
\mathbb E U_j^k
=\frac{(q-j+1)^{\overline k}}{(q+1)^{\overline k}}.
\tag{2.9}
$$
$j=0$ 的退化定义 $U_0=1$ 也满足 (2.9)，无需写形状参数为零的 Beta 密度。

Gamma 密度为
$$
\frac{v^{n-q+j}e^{-v}}{(n-q+j)!}\,\mathbf1_{(0,\infty)}(v).
$$
对 $k\le n-q$，其负阶矩由同一个 Gamma 积分给出
$$
\mathbb E V_j^{-k}
=\frac{(n-q+j-k)!}{(n-q+j)!}
=\frac1{(n-q+j)^{\underline k}}.
\tag{2.10}
$$
这里严格使用 $k<n-q+j+1$；未向不收敛的阶数延拓。

独立性、(2.8)—(2.10) 及
$$
\frac{q!}{(q+k)!}=\frac1{(q+1)^{\overline k}}
$$
共同给
$$
\frac{q!\gamma_k}{(q+k)!}
=\sum_{j=0}^q p_j\mathbb E
\left(\frac{U_j}{\varepsilon^2V_j}\right)^k.
$$
这证明 (2.2)。因 $p_0>0$，且 $\varepsilon^{-2}V_0^{-1}$ 在整个正半轴上有正密度，测度具有所述连续部分。

## 3. 相邻比较及全部可用 Hankel 正性

对整数 $\ell,d\ge0$，若
$$
\ell+2d\le n-q,
$$
则
$$
\boxed{(m_{\ell+i+j})_{i,j=0}^d>0.}
\tag{3.1}
$$
确实，对任意非零复多项式 $p(x)=\sum_{i=0}^d z_ix^i$，
$$
\sum_{i,j=0}^d \overline{z_i}m_{\ell+i+j}z_j
=\int_0^\infty x^\ell|p(x)|^2\,d\mu(x)>0.
$$
有限矩条件保证积分有限；正半轴连续部分保证严格为正。

特别，对
$$
1\le k<n-q
$$
取相邻 $2\times2$ 矩阵，得到
$$
m_k^2<m_{k-1}m_{k+1}.
$$
还原 (2.1) 后，
$$
\boxed{
\gamma_k^2<
\frac{q+k}{q+k+1}\,
\gamma_{k-1}\gamma_{k+1}.
}
\tag{3.2}
$$
因此在 $\mathbb Cg_\varepsilon$ 上，
$$
\boxed{
\Gamma_k\Gamma_{k+1}^{-1}\Gamma_k
<
\frac{q+k}{q+k+1}\Gamma_{k-1}.
}
\tag{3.3}
$$
所有算子都在这一共同不变一维线上限制后解释。由于右侧系数小于 $1$，常数 $1$ 的比较在该线上也成立。

R271 使用未乘 $(k!)^2$ 的成本
$a_k=\|v_k\|^2$。同一式准确变成
$$
\frac{a_k^2}{a_{k-1}a_{k+1}}
<
\left(\frac{k+1}{k}\right)^2
\frac{q+k}{q+k+1}.
\tag{3.4}
$$
令 $k=h-1$，这是该指定一维源的全高度比较上界。它与 R271 的下界所需平方因子完全相容，但没有给其他源或原连续尾上的普遍上界。

## 4. 与七位精确反例相容

已证有限维强化反例的权为
$$
(3,3,3,3,3,1,1),\qquad s=2,\qquad k=2.
$$
为适用本补充，必须把两个权 $1$ 的位作为第一簇，取
$$
q=2,\qquad n=5,\qquad \varepsilon=3.
$$
不是取 $q=5$。

此时
$$
Z_\varepsilon=847,\qquad
(p_0,p_1,p_2)=\frac1{847}(1,36,810).
$$
由 (2.8) 直接得到
$$
\gamma_1=\frac{181}{7623},\qquad
\gamma_2=\frac{101}{68607},\qquad
\gamma_3=\frac{127}{617463},
$$
以及
$$
\frac{\gamma_2^2}{\gamma_1\gamma_3}
=\frac{10201}{22987}.
\tag{4.1}
$$
这个比值严格大于已否定的有限维因子
$$
\frac{s+k}{s+k+1}\,
\frac{(q+n)-2s-k}{(q+n)-2s-k+1}
=\frac25,
$$
却严格小于本补充证明的
$$
\frac{s+k}{s+k+1}=\frac45.
$$
所以正矩表示并不撤销反例，也没有把反例强化为对较弱比较的否定。

## 5. 尚未覆盖的比较

本补充没有证明：

1. 一般正异权布尔模型的 primitive Gram 序；
2. 一般 $s<\min(q,n)$ 时的两簇最小逆；
3. 同一饱和两簇模型中非群固定的 primitive 部分；
4. 多维 primitive 压缩后的非交换乘积比较；
5. 原连续尾、原窄 Schur 返回源的任何普遍上界。

一般候选
$$
\Gamma_k\Gamma_{k+1}^{-1}\Gamma_k
\le\frac{s+k}{s+k+1}\Gamma_{k-1}
$$
及其常数 $1$ 的弱式仍未在此解决。不能由标量正矩表示把各未知矩阵序列同时对角化，也不能用完整 $D^*$ 代替已定义的受限上升伴随。


## 6. 完整正矩表示不能推广到任意权：零孔层的精确边界

**与既有结果的关系。** [R271 全Hankel反例](R271-appendix-squared-factorial-primitive-grams-fail-full-hankel-positivity.md) 已在原连续尾上排除全阶正矩表示，且其出生阶乘归一补节覆盖这里尝试外推的归一。下列六位算例只作短有理校准，提供可手核的有限负向量；不将同一路线的失败重计为新的普遍结论。前文指定两簇固定线的正矩定理与此不冲突。

本节只限制上文的 Stieltjes 表示方法，不否定一般相邻
$2\times2$ primitive Gram 比较。

取六位实际有限布尔删除算子
$$
D=6E_1+6E_2+E_3+E_4+E_5+E_6,
\qquad s=0.
$$
此处 $K_0=\mathcal H_0$ 本身是一维。令权平方为
$$
z=(36,36,1,1,1,1),
$$
第 $k$ 个初等对称和为 $e_k(z)$。由于
$$
(D^*)^ke_\varnothing
=k!\sum_{|F|=k}\left(\prod_{j\in F}a_j\right)e_F,
$$
全空间真实 Gram 在零孔层上准确是
$$
F_k=e_k(z),\qquad
\gamma_k=\frac1{e_k(z)}.
\tag{6.1}
$$
所以待推广的归一序列为
$$
m_k=\frac{\gamma_k}{k!}=\frac1{k!e_k(z)},
\qquad 0\le k\le6.
$$

直接展开
$$
(1+36t)^2(1+t)^4
$$
给
$$
(e_0,e_1,\ldots,e_6)
=(1,76,1590,5620,8065,5256,1296),
$$
从而
$$
(m_0,m_1,\ldots,m_6)
=
\left(
1,\frac1{76},\frac1{3180},\frac1{33720},
\frac1{193560},\frac1{630720},\frac1{933120}
\right).
\tag{6.2}
$$
考虑其 $4\times4$ Hankel 矩阵
$$
H=(m_{i+j})_{i,j=0}^{3}.
$$
取短整数向量
$$
v=(-1,80,-500,300)^{\mathsf T}.
$$
用 (6.2) 的有理数直接计算得
$$
\boxed{
v^{\mathsf T}Hv
=-\frac{350372256737}{43181529342768}<0.
}
\tag{6.3}
$$
因此不存在正测度，使 (6.2) 的全部七个数同时成为其零至六阶矩。
若有该测度，(6.3) 左侧就应等于
$$
\int_0^\infty
|-1+80x-500x^2+300x^3|^2\,d\mu(x)\ge0,
$$
产生矛盾。

### 6.1 整数核验证书

(6.3) 可以不做矩阵求逆而直接检查。取全部 $m_k$ 分母的公倍数
$$
L=31090701126792960.
$$
以整数运算形成
$$
L\,v^{\mathsf T}Hv
=\sum_{i,j=0}^3v_iv_j(Lm_{i+j}),
$$
准确得到
$$
-252268024850640.
$$
约去公因子 $720$，就是 (6.3)。

作为另一份独立可核形式，按自然顺序对 $H$ 作单位下三角
$LDL^{\mathsf T}$ 消元，其四个主元为
$$
1,\qquad
\frac{649}{4591920},\qquad
\frac{192296157929}{417941934240263400},\qquad
-\frac{77816078579117747058757943}
{392884771524266880396997085698560}.
\tag{6.4}
$$
前三个严格正，最后一个严格负。证明只依赖精确有理数，
不使用浮点特征值判号。

### 6.2 与仍待证明的相邻比较分开

这一例的全部相邻 $2\times2$ 矩阵
$$
\begin{pmatrix}
m_{k-1}&m_k\\
m_k&m_{k+1}
\end{pmatrix},
\qquad 1\le k\le5,
$$
仍然正定，可直接由 (6.2) 交叉相乘核验。这也与零孔层的
Newton 不等式相容。

因此本节没有给
$$
\Gamma_k\Gamma_{k+1}^{-1}\Gamma_k
\le\frac{s+k}{s+k+1}\Gamma_{k-1}
$$
或常数 $1$ 弱式的反例。它准确排除的是把第 2 节的**完整正测度矩表示**
外推到任意权的证明路线。一般问题仍仅要求相邻
$2\times2$ 算子序；更高阶 Hankel 正性是严格更强的额外要求。


### 6.3 整层归一 Gram 的起点也已失败

另一个可能的推导，是先在整个 $\mathcal H_s$ 上证明
$$
G_{k+1}\le G_kG_{k-1}^{-1}G_k,\qquad
G_k=(s+k)!\,F_k,
$$
再考虑 primitive 短化。这个整层起点已经不成立。

取 $s=1$、七位权
$$
a=(1,1/10,1/10,1/10,1/10,1/10,1/10).
$$
在置换后六位的固定空间中，使用非规范基
$$
(e_0,\;s_{\rm w}),\qquad s_{\rm w}=\sum_{j=1}^6e_j,
$$
其 Gram 是 $\operatorname{diag}(1,6)$。完整整层算子限制为
$$
F_1=
\begin{pmatrix}3/50&3/5\\1/10&11/10\end{pmatrix},
\qquad
F_2=
\begin{pmatrix}3/2000&3/100\\1/200&103/1000\end{pmatrix}.
$$
这些矩阵相对于上述 Gram 自伴，不能改用普通欧氏内积。

对 $v=e_0-s_{\rm w}/10$，
$$
F_1v=-s_{\rm w}/100,\qquad
\langle F_1^2v,v\rangle=\frac3{5000},\qquad
\langle F_2v,v\rangle=\frac{21}{12500}.
$$
因 $G_0=I,G_1=2F_1,G_2=6F_2$，准确得到
$$
\boxed{
\langle(G_1G_0^{-1}G_1-G_2)v,v\rangle
=-\frac{24}{3125}<0.
}
$$
这里 $Dv=47/50\ne0$，所以此向量不是 primitive。该计算只排除
“整层 Newton 后再短化”的起点，不给真正
$\Gamma_k=P_{K_s}F_k^{-1}|_{K_s}$ 的反例。
后续仍须在保留完整求逆及 primitive 压缩的条件下证明或否定相邻算子序。
