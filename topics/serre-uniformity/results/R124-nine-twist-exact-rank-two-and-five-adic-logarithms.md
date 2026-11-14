# R124：九级固定扭曲的精确秩二、实乘法与实际五进对数基

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明。** 对 [R120](R120-nine-cartan-twist-and-explicit-cubic-cover.md) 的固定曲线
$$
\mathcal C:\quad y^2=7x^6+12x^5-36x^4-10x^3+84x^2-72x+19,
\qquad J=\operatorname{Jac}\mathcal C,
$$
有
$$
\boxed{\operatorname{rank}J(\mathbb Q)=2,
\qquad \mathbb Q(\sqrt3)\hookrightarrow\operatorname{End}^0_{\mathbb Q}(J),
\qquad \rho_{\mathbb Q}(J)\ge2.}
\tag{124.1}
$$
这把 R120 的秩下界升级为准确的秩；解析输入使用有理数不等式，未以浮点 $L$ 值或 BSD 猜想代替证明。此外，R120 的两个明确有理除子生成一个有限指数子群，且其在好普通素数 $5$ 处的对数矩阵已经算出，行列式非零。

于是这条实际曲线满足二次 Chabauty 的秩条件。本文**尚未**计算全局/局部高度、二次 Chabauty 零点或 Mordell–Weil 筛，因而不声称已经分类 $\mathcal C(\mathbb Q)$，也不声称排除了原问题的九次幂分母支。

## 1. 逐元素角色证书给出的真实模 Jacobian

令 $R=\mathbb Z/9\mathbb Z$、$G=\operatorname{GL}_2(R)$，$\#G=3888$。除 R120 的非分裂 Cartan 群
$$C=\{(\begin{smallmatrix}a&-b\\b&a\end{smallmatrix}):a^2+b^2\in R^\times\},$$
再定义
$$
\begin{aligned}
B_0&=\{g\in G:g_{21}\equiv0\pmod3\},\\
B_1&=\{g\in G:g_{12}\equiv0\pmod3,\ g_{21}=0\},\\
T_1&=\{g\in G:g_{12}\equiv g_{21}\equiv0\pmod3\},\\
T_2&=\{g\in G:g_{12}=g_{21}=0\}.
\end{aligned}
$$
其阶和指数是：

| $H$ | $\#H$ | $[G:H]$ | $X(9)/H$ 的有理模解释 |
|---|---:|---:|---|
| $C$ | $72$ | $54$ | $X_{\rm ns}(9)$ |
| $B_0$ | $972$ | $4$ | $X_0(3)$ |
| $B_1$ | $108$ | $36$ | $X_0(27)$ |
| $T_1$ | $324$ | $12$ | $X_0(9)$ |
| $T_2$ | $36$ | $108$ | $X_0(81)$ |

例如 $B_1$ 稳定一个阶 $9$ 循环子群和一个与它不交的阶 $3$ 循环子群。将曲线按后者取商，并取对偶同源下前者的原像，得到阶 $27$ 的循环子群。反向从一个阶 $27$ 循环子群取其阶 $3$ 子群的商，即恢复这对不交子群。这些构造在 $\mathbb Q$ 上定义。$T_1,T_2$ 是同一构造在两个相同阶数 $3,9$ 上的情形；所以这里的识别不只是复解析曲线的偶然同构。

有准确的有理置换表示恒等式
$$
\boxed{
\operatorname{Ind}_{C}^{G}1+2\operatorname{Ind}_{B_0}^{G}1
+2\operatorname{Ind}_{B_1}^{G}1
=\operatorname{Ind}_{T_2}^{G}1+2\operatorname{Ind}_{T_1}^{G}1+2\cdot1.}
\tag{124.2}
$$
配套标准库程序枚举全部 $3888$ 个矩阵及五组左陪集；对**每个** $g\in G$，分别计算它在各陪集集合上的不动点数，再核对 (124.2)。没有用少数 Frobenius 迹猜测这条恒等式。输出证书保存全部五元角色值的直方图。

这里也说明从表示到 Jacobian 的步骤。对一个有限群作用的光滑射影曲线 $X$，在有理同源范畴内令
$$e_H=\frac1{\#H}\sum_{h\in H}h.$$
商映射的拉回与范数给出 $e_H\operatorname{Pic}^0(X)\sim\operatorname{Pic}^0(X/H)$。有理置换表示同构可由有理群代数中的矩阵实现，清去分母就给这些直和的互逆有理同源。这对几何上不连通的全级曲线 $X(9)$ 同样成立：先取各连通分支 Picard 簇的乘积。因而 (124.2) 给
$$
\operatorname{Jac}X_{\rm ns}(9)\times J_0(3)^2\times J_0(27)^2
\sim_{\mathbb Q} J_0(81)\times J_0(9)^2.
$$
$X_0(3),X_0(9)$ 的亏格为 $0$；$X_0(27)$ 的亏格为 $1$，$X_0(81)$ 的亏格为 $4$。后者旧部分准确为 $J_0(27)^2$。由有理同源范畴中的消去得到
$$
\operatorname{Jac}X_{\rm ns}(9)\sim_{\mathbb Q}J_0(81)^{\rm new}.
\tag{124.3}
$$
这是本例的有限群证明；没有将只适用于素数层的 Chen 同源直接替换成模九命题。

## 2. 唯一新形式的完整 eta 证书

设 $\eta$ 为 Dedekind eta 函数，定义
$$
e_1=\frac{\eta(9\tau)^6}{\eta(3\tau)\eta(27\tau)},
\qquad e_2=\eta(3\tau)\eta(9\tau)^2\eta(27\tau),
$$
$$h=\eta(3\tau)^2\eta(9\tau)^2,\qquad h_3=h(3\tau).$$
它们都是层 $81$、权 $2$、平凡角色的尖点形式。为完整核验，按约数 $d=1,3,9,27,81$ 排列 eta 指数 $r_d$，四组分别为
$$
(0,-1,6,-1,0),\quad(0,1,2,1,0),\quad
(0,2,2,0,0),\quad(0,0,2,2,0).
$$
它们满足 $\sum r_d=4$、$\sum dr_d\equiv\sum(81/d)r_d\equiv0\pmod{24}$，且 $\prod d^{r_d}$ 是平方；Newman 的 eta 判据给出上述权与角色。由 eta 变换公式，尖点分母 $c\mid81$ 处的阶为
$$
\frac{81}{24\gcd(c,81/c)c}
\sum_{d\mid81}\frac{\gcd(c,d)^2r_d}{d}.
\tag{124.4}
$$
对应的完整五列是

| 形式 | $c=1$ | $3$ | $9$ | $27$ | $81$ |
|---|---:|---:|---:|---:|---:|
| $e_1$ | $1$ | $1$ | $2$ | $1$ | $1$ |
| $e_2$ | $2$ | $2$ | $1$ | $2$ | $2$ |
| $h$ | $3$ | $3$ | $1$ | $1$ | $1$ |
| $h_3$ | $1$ | $1$ | $1$ | $3$ | $3$ |

所有阶都正。四者的前四个 Fourier 系数已线性独立；而 $\dim S_2(\Gamma_0(81))=4$，所以它们组成基。

该层的 Sturm 界是
$$\left\lfloor\frac2{12}[\operatorname{SL}_2(\mathbb Z):\Gamma_0(81)]\right\rfloor
=\frac{2\cdot108}{12}=18.$$
将四个 eta 乘积展开到 $q^{36}$，按
$$a_n(T_2e)=a_{2n}(e)+2a_{n/2}(e),\qquad a_{n/2}=0\ (2\nmid n),$$
逐项验证到 $q^{18}$，得到完整恒等式
$$T_2e_1=3e_2,\qquad T_2e_2=e_1,\qquad T_2h=T_2h_3=0.
\tag{124.5}
$$
$h,h_3$ 张成旧空间，$T_2$ 自伴；故 $e_1,e_2$ 张成新空间。它们的 $T_2$ 特征多项式为 $X^2-3$，由维数和交换的 Hecke 算子可知该新空间只有一个 Galois 轨道，两个正规化新形式为
$$f_\pm=e_1\pm\sqrt3 e_2.$$
系数域准确为 $\mathbb Q(\sqrt3)$。

Fricke 符号也可直接确定。对权二 eta 商，$W_{81}$ 把指数 $r_d$ 反转为 $r_{81/d}$，并给标量
$$-\frac{81}{\sqrt{\prod d^{r_d}}}.$$
$e_1,e_2$ 的指数均对称，且乘积都是 $81^2$，所以
$$f_\pm|W_{81}=-f_\pm.$$
采用权二函数方程根数 $w(f)=-\lambda_{W}(f)$ 的约定，有 $w(f_\pm)=+1$。

## 3. 扭曲后的准确层、符号和模因子

R120 给出 $X_{\rm ns}(9):y_0^2=-S(x)$，而 $\mathcal C:y^2=S(x)$ 是其关于 $\mathbb Q(i)$ 的扭曲。超椭圆对合在 Jacobian 上作用为 $-1$。因此 (124.3) 扭曲后得到
$$J\sim_{\mathbb Q} A_g,\qquad g=f_+\otimes\chi_{-4}.
\tag{124.6}
$$
$g$ 是层 $1296=16\cdot81$、权二、平凡角色的新形式，其系数域仍为 $\mathbb Q(\sqrt3)$：例如 $a_5(g)=-\sqrt3$。

准确层可由局部导子核实。$f_+$ 在 $2$ 不分歧，$\chi_{-4}$ 的二进导子指数是 $2$；二维不分歧表示乘此角色后的导子指数恰为 $4$。在 $3$ 只作不分歧扭曲，导子指数仍为 $4$；其他素数没有新分歧。标准互素导子二次扭曲公式给
$$w(g)=\chi_{-4}(-81)w(f_+)=-1.
\tag{124.7}
$$
也可从 $g=(f_+(\tau+1/4)-f_+(\tau+3/4))/(2i)$ 及 eta 的 Fricke 变换导出同一符号。其共轭 $\bar g$ 也有根数 $-1$，所以两者在 $s=1$ 都消失。

eta 乘积的指数支撑给 $a_n(f_\pm)=0$ 当 $3\mid n$；扭曲再杀去所有偶数项。因此
$$a_1(g)=1,\qquad a_n(g)=0\quad\text{若 }(n,6)>1.
\tag{124.8}
$$
对两个实嵌入均有 Deligne 界 $|a_n(g)|\le d(n)\sqrt n$。

## 4. 两个中心导数的严格有理数下界

令 $c=2\pi/\sqrt{1296}=\pi/18$，并定义
$$E_1(z)=\int_z^\infty\frac{e^{-t}}t\,dt.$$
将 Mellin 积分在 $1$ 处分开，利用根数 $-1$，有
$$
\Lambda_g(s)=\int_1^\infty g(it/36)
(t^{s-1}-t^{1-s})\,dt,
\quad \Lambda_g(s)=(36/2\pi)^s\Gamma(s)L(g,s).
$$
逐项积分绝对收敛。因 $L(g,1)=0$，在中心求导得到
$$L'(g,1)=2\sum_{n\ge1}\frac{a_n(g)}n E_1(cn).
\tag{124.9}
$$
该公式对 $\bar g$ 相同。

### 4.1 主项

使用 $17/100<c<9/50$ 和 $e^{-t}>1-t$（$t>0$），有
$$E_1(c)>\int_c^1\frac{1-t}t\,dt
=\log(1/c)-1+c
>\log(50/9)-41/50.$$
再以正项展开
$$\log(50/9)=2\sum_{k\ge0}\frac{(41/59)^{2k+1}}{2k+1},$$
只取前 $20$ 项即可在有理数中验证
$$2E_1(c)>\frac{178}{100}.
\tag{124.10}
$$

### 4.2 全部尾项

由 (124.8)，尾项从 $n=5$ 开始，且只取 $(n,6)=1$。利用
$$E_1(cn)<\frac{e^{-cn}}{cn},$$
得到
$$
2\sum_{\substack{n\ge5\\(n,6)=1}}
\frac{|a_n(g)|}{n}E_1(cn)
<\frac{200}{17}\sum_{\substack{n\ge5\\(n,6)=1}}
\frac{d(n)e^{-17n/100}}{n\sqrt n}.
\tag{124.11}
$$
对 $5\le n\le40$，用
$$\sqrt n\ge \frac{\lfloor1000\sqrt n\rfloor}{1000},\qquad
e^{-t}<\left(\sum_{k=0}^{48}\frac{t^k}{k!}\right)^{-1}$$
求每项的有理上界，再各向上舍入到 $10^{-6}$。这里的向上舍入由整数除法实现，而不是浮点四舍五入。

对 $n\ge41$，用 $d(n)\le2\sqrt n$，并放宽到所有整数 $n$。因
$$e^{-17/100}<\frac{100}{117}=r,$$
余项小于
$$\frac{400}{17\cdot41}\frac{r^{41}}{1-r}.
\tag{124.12}
$$
配套程序在有理数中验证上述有限项和余项之和严格小于 $3/2$。所以
$$\boxed{L'(g,1)>\frac7{25}>0,\qquad
L'(\bar g,1)>\frac7{25}>0.}
\tag{124.13}
$$
这个估计只需要正规化首项、支撑、Deligne 界和准确根数。它涵盖无限尾项，既不是数值精度假设，也不是从一次解析程序输出推断非零。

## 5. 已发表秩定理及实乘法

使用已发表的 Gross–Zagier–Kolyvagin–Logachëv 定理的如下形式：若 $A/\mathbb Q$ 是简单模阿贝尔簇，维数为 $d$，且 $\operatorname{ord}_{s=1}L(A,s)\in\{0,d\}$，则其代数秩等于该解析秩。一个可直接核对、**不限制层为奇数**的准确陈述是 Adžaga–Chidambaram–Keller–Padurariu，*Research in Number Theory* **8** (2022), 87，Theorem 2.1。

这里 $A_g$ 是一个真正的简单模因子，$d=[\mathbb Q(\sqrt3):\mathbb Q]=2$，且
$$L(A_g,s)=L(g,s)L(\bar g,s).$$
式 (124.7)、(124.13) 证明解析秩准确为 $2$。该定理与 (124.6) 遂给
$$\operatorname{rank}J(\mathbb Q)=2.$$
注意 Dogra–Le Fourn 的相关附录 Proposition 8 在开头把层限制为奇数；本文没有直接把该限制略去后用在 $1296$。上述无奇层限制的已发表陈述才是这里引用的接口。本文也没有使用任何 $p$-converse 或对 $\Sha$ 可除部分的猜测。

Hecke 系数域给
$$\mathbb Q(\sqrt3)\subset\operatorname{End}^0_{\mathbb Q}(A_g).$$
对应的 Hecke 算子在模极化的 Rosati 对合下自伴。将该极化沿有理同源搬运到 $J$，得到这个极化下的二维对称子空间；Néron–Severi 群的维数不依赖极化的选择。由对称同态与 Néron–Severi 群的关系，有 $\rho_{\mathbb Q}(J)\ge2$。这里无需声称任意实二次域嵌入都被任意 Rosati 对合保持。

于是 $2=\operatorname{rank}J<2+\rho_{\mathbb Q}(J)-1$。对好约化素数 $\ell$，标准二次 Chabauty 定理给 $\mathcal C(\mathbb Q_\ell)_2$ 有限。这是有限性的有效计算入口，**不是**其零点已经列出。

## 6. 实际五进全秩对数：可直接用的有限指数除子格

保持 R120 的记号
$$P_\pm=(-1,\pm12),\qquad Q_\pm=(1,\pm2),$$
$$D_1=[P_+-P_-],\qquad D_2=[Q_+-P_+].$$
R120 已证明 $D_1,D_2$ 独立，故由准确秩二知它们生成 $J(\mathbb Q)$ 的有限指数子群。没有由此声称其指数为 $1$。

为了实际核验五进对数，取 R120 的覆盖定义域 $K=\mathbb Q(w)$、$w^2=-3$，及曲线
$$E_0:\ V^2=U^3+A_4U+A_6,
\quad A_4=-(21+27w)/2,\quad A_6=28w-10.$$
该模型在 $5$ 好约化；$K_5/\mathbb Q_5$ 是未分歧二次扩张。逐一枚举 $25$ 个剩余域元素，得到
$$\#E_0(\mathbb F_{25})=33.$$
其迹为 $-7$，所以是普通约化。$J$ 也在 $5$ 好普通约化；其 Euler 因子可由 $a_5(g)=-\sqrt3$ 写为 $1+7T^2+25T^4$。

R120 的两个椭圆点为
$$P_H=((7-w)/2,4w-4),\qquad
P_2=((1+w)/2,2w+4).$$
在 $K$ 上用分数二元数对执行准确倍点，得到 $[33]P_H,[33]P_2$ 的坐标赋值均为
$$v_5(U)=-2,\qquad v_5(V)=-3.$$
因而它们在形式群中，参数 $t=-U/V$ 的赋值为 $1$。精确约化给
$$
\frac{t([33]P_H)}5\equiv35+21w,\qquad
\frac{t([33]P_2)}5\equiv6+118w\pmod{125}.
\tag{124.14}
$$
这一步的倍点是全局有理数运算；没有在分母不可逆的局部加法式中强行相除。

短 Weierstrass 模型的形式对数满足
$$\log_{E_0}(t)=t+\frac{2A_4}{5}t^5+\frac{3A_6}{7}t^7+\cdots.$$
形式不变微分有整系数，故一般第 $n$ 项除以 $t^n$ 的分母至多来自 $n$。对 $v_5(t)=1$，上述非线性项除以 $5$ 后均为 $125$ 的倍数。于是 (124.14) 同样计算了 $\log([33]P)/5\pmod{125}$。

覆盖推前满足
$$\phi_*D_1=4P_H,\qquad \phi_*D_2=P_2-2P_H,$$
且
$$
\phi^*\frac{dU}{2V}
=\frac32\left(x-\frac{1-w}{2}\right)\frac{dx}{y}
=\frac32\omega_1-\frac34\omega_0+\frac34w\omega_0,
$$
其中 $\omega_0=dx/y$、$\omega_1=x\,dx/y$。若对应的椭圆对数为 $a+bw$，Jacobian 的两坐标就是
$$L_0=\frac43b,\qquad L_1=\frac23(a+b).$$
将 (124.14) 按两个除子的像线性组合，再除以 $33$，得到
$$
\boxed{
\frac15
\begin{pmatrix}
\int_{D_1}\omega_0&\int_{D_2}\omega_0\\
\int_{D_1}\omega_1&\int_{D_2}\omega_1
\end{pmatrix}
\equiv
\begin{pmatrix}64&46\\2&76\end{pmatrix}
\pmod{125}.}
\tag{124.15}
$$
该矩阵的行列式模 $5$ 为 $2$。这证明两条有理除子的五进对数确实张满 $\operatorname{Lie}(J)(\mathbb Q_5)$；不只是一般秩条件给出的存在性陈述。

特别地，已经具备一个明确的有限指数 Mordell–Weil 除子格、好普通素数 $5$ 和其非奇异的对数矩阵。全基饱和性、非五进局部高度集合、五进高度函数及最终零点/筛仍须分别计算。

## 7. 完整证书与继续工作的准确边界

```sh
python3 -B topics/serre-uniformity/notes/verify_r124_nine_twist_rank.py --check
```

程序只用 Python 标准库，并复用 R120 的分数数域运算。它从零核验全部角色等式、eta 指数/尖点阶和 Sturm 比较、无限尾项的严格有理界，以及有限域枚举、实际倍点和 (124.15)。

- [核验程序](../notes/verify_r124_nine_twist_rank.py)。
- [小证书](../notes/r124_nine_twist_rank_certificate.json)，SHA256 `6585f076779d3bac8e78bd08ffc9e15a43df4d142018b4d8e9ce092886c7d651`。

R120 的真正剩余有理点问题和必要原始分母系统
$$z^2=S_h(u,v),\qquad u^3-3uv^2+v^3=\pm3^\epsilon Y^p$$
仍保留。本文闭合的是该固定曲线的秩、实乘法和五进对数输入，不把有限性或 QC 门槛当成全部有理点分类。

### 来源

1. B. de Smit、B. Edixhoven，*Sur un résultat d'Imin Chen*，Mathematical Research Letters **7** (2000), 147–154，[作者全文](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。一般有理表示到同源的论证；本文另行验证模九所需的准确群恒等式。
2. M. Newman，*Construction and Application of a Class of Modular Functions (II)*，Proceedings of the London Mathematical Society **9** (1959), 373–387，[DOI](https://doi.org/10.1112/plms/s3-9.3.373)；G. Ligozat，*Courbes modulaires de genre 1*，Mémoire SMF **43** (1975)，[全文](https://www.numdam.org/article/MSMF_1975__43__5_0.pdf)。eta 判据与尖点阶。
3. A. O. L. Atkin、W.-C. Li，*Twists of newforms and pseudo-eigenvalues of W-operators*，Inventiones Mathematicae **48** (1978), 221–243，[DOI](https://doi.org/10.1007/BF01390245)。互素导子扭曲的层和 Fricke 符号。
4. N. Adžaga、S. Chidambaram、T. Keller、O. Padurariu，*Rational points on hyperelliptic Atkin-Lehner quotients of modular curves and their coverings*，Research in Number Theory **8** (2022), 87，**Theorem 2.1**，[已发表全文](https://link.springer.com/article/10.1007/s40993-022-00388-9)。本文使用其无奇层限制的 Gross–Zagier–Kolyvagin–Logachëv 秩定理准确陈述。
5. N. Dogra、S. Le Fourn，*Quadratic Chabauty for modular curves and modular forms of rank one*，Mathematische Annalen **380** (2021), 393–448，**Lemma 1**，[已发表全文](https://link.springer.com/article/10.1007/s00208-020-02112-3)。二次 Chabauty 的 $r<g+\rho-1$ 门槛；其附录的奇层约定不用于第 5 节的偶层秩结论。
