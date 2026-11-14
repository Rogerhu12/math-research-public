# R74. 层 41 的两个共同 Heegner 域及普通辅助素数 47

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明；模符号运算和有限域证书均已实算。** 本文完成 R68 在层 $p=41$ 留下的一项实际算术输入。令 $\mathcal F_{41}$ 为 level $1681=41^2$、权二、平凡 nebentype、new、Fricke $+$ 的全部归一化新形式，包括各系数共轭。则
$$|\mathcal F_{41}|=54,$$
并且对每个 $f\in\mathcal F_{41}$，同时有
$$\boxed{L(f\otimes\chi_{-43},1)\ne0,\qquad
L(f\otimes\chi_{-163},1)\ne0.}\tag{0.1}$$
此外，$47$ 在两个虚二次域中都分裂，所有 $54$ 个形式在 $47$ 的每个系数嵌入都普通。

非消失不是从浮点 $L$ 值判断：两个 $54\times54$ Krylov 矩阵的行列式模 $1009$ 分别是 $161$ 和 $415$。普通性由实际 $T_{47}$ 矩阵的行列式模 $47$ 等于 $28$ 证明。原始精确模符号脚本、两张小有限域矩阵以及只用 Python 标准库的独立验算程序均随文保存。

## 1. 三种符号必须分开

置 $N=1681$。在权二时，模符号空间为
$$M=\operatorname{Hom}_{\Gamma_0(N)}
\left(\operatorname{Div}^0(\mathbb P^1(\mathbb Q)),\mathbb Q\right).$$
写 $[r,s]$ 表示从 $r$ 到 $s$ 的有向模路径。本文的星号算子 $\iota$ 由
$$\begin{pmatrix}-1&0\\0&1\end{pmatrix}$$
作用在尖点上，即 $[r,s]\mapsto[-r,-s]$。它是模符号的 $+$、$-$ 分解，**不是** Fricke 符号。

另外，$w_N$ 是由 $z\mapsto-1/(Nz)$ 给出的 Fricke 对合。对权二微分 $\omega_f=2\pi i f(z)\,dz$，其拉回为
$$w_N^*\omega_f
=2\pi i\frac{f(-1/(Nz))}{Nz^2}\,dz,$$
正是通常的权二 Fricke slash 作用，没有额外负号。$w_N$ 与星号交换，也保持 old、new 子空间。

实际使用的空间是
$$\mathcal M=\left(M_{\rm cusp}^{\rm new}\right)^{\iota=-1,\,w_N=+1}.
\tag{1.1}$$
对每个 $f\in\mathcal F_{41}$，Eichler–Shimura 的模符号识别给 $\mathcal M\otimes\mathbb C$ 中一条 Hecke 特征线。它由全纯周期符号的星号负部分张成。这是标准有理模符号与全纯微分的对应；同一形式的星号正、负部分各出现一次。

更具体地，定义
$$\Phi_f([r,s])=\int_r^s\omega_f,\qquad
\Phi_f^-:=\frac{\Phi_f-\iota\Phi_f}{2}.
\tag{1.2}$$
这里 $\Phi_f^-\ne0$。平凡 nebentype 的特征形式系数在每个复嵌入均为实数，所以 $z\mapsto-\bar z$ 将其周期符号变成复共轭符号。若负部分为零，全纯周期类就属于复共轭不变的实上同调，而一个非零纯 $(1,0)$ 类不能是实类。这是 Hodge 分解及复共轭交换 $(1,0),(0,1)$ 的直接后果。

因此，只要某个线性泛函在 (1.1) 的每条 Hecke 特征线上非零，就能用下面的 Gauss 公式判断相应的每个扭曲 $L$ 值。无需先把各个特征形式的复周期数值近似出来。

## 2. 扭曲路径泛函及准确的 Gauss 因子

设 $D=-43$ 或 $-163$，$m=|D|$，$\chi_D$ 为 conductor $m$ 的本原二次 Dirichlet 字符。它是奇字符。定义有理线性泛函
$$\mathcal L_D(\phi)
=\sum_{a=1}^{m-1}\chi_D(a)\,
\phi([a/m,\infty]).
\tag{2.1}$$
其系数是整数；实际代码使用 `kronecker(D,a)`。

### 引理 1：星号负性

有 $\mathcal L_D(\iota\phi)=-\mathcal L_D(\phi)$，因而
$$\mathcal L_D(\Phi_f)=\mathcal L_D(\Phi_f^-).
\tag{2.2}$$

**证明。** 星号把 $a/m$ 变成 $-a/m$。模 $\Gamma_0(N)$ 中的平移 $z\mapsto z+1$，这条路径等于 $[(m-a)/m,\infty]$。重新编号后，$\chi_D(m-a)=\chi_D(-1)\chi_D(a)=-\chi_D(a)$，得第一式。代入 (1.2) 得 (2.2)，其中没有再乘一个 $2$。证毕。

### 引理 2：Mellin–Gauss 等式

令
$$\tau_D=\sum_{a\bmod m}\chi_D(a)e^{2\pi i a/m},\qquad
\tau_D^2=D=-m.$$
按 (1.2) 的 $2\pi i$ 和路径方向约定，
$$\boxed{\quad
\mathcal L_D(\Phi_f^-)
=-\tau_D L(f\otimes\chi_D,1).
\quad}\tag{2.3}$$
等价地，$L(f\otimes\chi_D,1)=\tau_D\mathcal L_D(\Phi_f^-)/m$。

**证明。** 写 $f(z)=\sum_{n\ge1}a_n e^{2\pi inz}$。本原 Gauss 和恒等式给
$$\sum_{a\bmod m}\chi_D(a)f(z+a/m)
=\tau_D\sum_{n\ge1}a_n\chi_D(n)e^{2\pi inz}.
\tag{2.4}$$
将两边乘 $2\pi i\,dz$ 后沿 $0\to i\infty$ 积分，左侧就是 (2.1) 对 $\Phi_f$ 的值。右侧由 Mellin 变换为 $-\tau_D L(f\otimes\chi_D,1)$：因为 $z=iy$ 时 $2\pi i\,dz=-2\pi\,dy$。可先从 $y=\varepsilon>0$ 积分，再令 $\varepsilon\to0$；尖点消失保证两边的端点积分收敛。最后使用 (2.2)。$\tau_D\ne0$，且 $-1/\tau_D=\tau_D/m$，得所列等价式。证毕。

这是 Manin (1972) §3.8 的扭曲路径公式在本文微分及路径规范下的写法。若对全部路径采用反向约定，两边的周期泛函同时变号；本文脚本和 (2.1) 均使用 `[a/m,oo]`，没有交换两个端点。

## 3. 精确空间、实际 Hecke 算子和基

使用官方 PARI/GP **2.19.0** 的有理模符号实现。以下是完整空间定义，不根据预期维数挑选一个抽象矩阵：

```gp
M = msinit(1681, 2, -1);
Nnew = msnew(M);
W = msatkinlehner(M, 1681, Nnew);
P = Nnew[1] * matker(W - matid(117));
T2 = mshecke(M, 2, P);
T3 = mshecke(M, 3, P);
H = T2 + 2*T3;
```

官方文档中 `msinit(...,-1)` 是 $\operatorname{diag}(-1,1)$ 的负特征空间，`msnew` 是真正的 new cuspidal 子空间，`msatkinlehner` 是指定精确除数的标准 Atkin–Lehner 作用。$P$ 的列是在原符号空间中的实际基。

脚本另外精确核验：
$$\begin{array}{c|r}
\text{空间或作用}&\text{结果}\\\hline
\dim M^-&143\\
\dim M_{\rm cusp}^{-,\rm new}&117\\
W^2&I_{117}\\
\dim\mathcal M&54\\
w_{1681}|_{\mathcal M}&I_{54}\\
T_2T_3-T_3T_2&0\\
\operatorname{den}(H)&6.
\end{array}\tag{3.1}$$
这些维数是对定义的核验；符号的识别来自实际算子的构造，而非维数匹配。

$H$ 的特征多项式无重根，在 $\mathbb Q$ 上有八个不可约因子，次数为
$$2,3,3,4,4,8,12,18.\tag{3.2}$$
因此它分离全部 $54$ 条 Hecke 特征线。完整因子系数随 JSON 证书保存；例如最小因子为 $X^2-2X-31$，它与二维因子上的 $a_2=1$、$a_3=\pm2\sqrt2$ 相符，但证明没有把数据库数据当作输入。

## 4. 两个 Krylov 行列式是严格非消失证书

在 $P$ 的有理基中写
$$v_D=(\mathcal L_D(P_1),\ldots,\mathcal L_D(P_{54}))\in\mathbb Z^{54}.$$
定义
$$K_D=
\begin{pmatrix}
v_D\\v_DH\\v_DH^2\\\vdots\\v_DH^{53}
\end{pmatrix}.
\tag{4.1}$$

### 引理 3：Krylov 判据

若 $\det K_D\ne0$，则 $\mathcal L_D$ 在 $\mathcal M\otimes\mathbb C$ 的每条 Hecke 特征线上非零。

**证明。** 若某条特征线由 $u\ne0$ 张成，$Hu=\lambda u$，而 $v_Du=0$，则对每个 $k$ 有
$$v_DH^ku=\lambda^kv_Du=0.$$
于是 $K_Du=0$，与可逆性矛盾。这个论证本身甚至不要求预先核对 $H$ 的无重根性；实际 Hecke 作用半单和满秩还会反过来迫使 $H$ 有 $54$ 个不同特征值。证毕。

### 定理 4：两个共同中心扭曲值均非零

对 $D=-43,-163$，精确模符号计算得到
$$\operatorname{rank}_{\mathbb Q}K_D=54,$$
并有独立的小有限域证书
$$\boxed{\quad
\det(K_{-43}\bmod1009)=161,\qquad
\det(K_{-163}\bmod1009)=415.
\quad}\tag{4.2}$$
因此 (0.1) 对全部 $54$ 个共轭形式成立。

**证明。** 由 (3.1)，$H$ 的分母只含 $2,3$，而 $v_D$ 是整数行。所以 (4.1) 可逐项模 $1009$ 约化。保存的证书含 $H\bmod1009$ 和两条**完整整数行** $v_D$；独立程序只用模素数 Gaussian 消元与行向量乘法，重建两个 $K_D$ 并得到 (4.2)。因此两个有理行列式都非零。引理 3 和 (2.3) 给每一条实际新形式特征线上的扭曲 $L$ 值非零。证毕。

在探索阶段，$T_2$ 和 $T_2+T_3$ 的 Krylov 秩分别为 $45$ 和 $51$；它们的特征值有重复，后一算子的特征多项式含 $X^4$。这两个较小秩没有给出任何扭曲消失。改用实际 $T_2+2T_3$ 后得到 (4.2)，无需改变扭曲泛函。

## 5. 共同普通辅助素数 $47$

### 定理 5

$47$ 在 $\mathbb Q(\sqrt{-43})$ 和 $\mathbb Q(\sqrt{-163})$ 中都分裂。所有 $f\in\mathcal F_{41}$ 的 $a_{47}(f)$ 在系数域的每个 $47$ 进地方都是单位。

**证明。** $-43\equiv4\pmod{47}$、$-163\equiv25\pmod{47}$，均为非零平方。模符号中的实际算子
$$T_{47}=\operatorname{mshecke}(M,47,P)$$
的基分母在 $47$ 可逆，独立有限域证书给
$$\boxed{\det(T_{47}\bmod47)=28\ne0.}\tag{5.1}$$
在全特征分解中，其特征值正是全部 $a_{47}(f)$。这些是代数整数。如果任何一个 $47$ 进嵌入下的特征值具有正赋值，所有其他特征值的赋值仍非负，行列式就会被 $47$ 整除，与 (5.1) 矛盾。因此全部特征值均为单位。权二、level 与 $47$ 互素时，这正是普通性。此论证不假设系数域在 $47$ 分裂或不分歧。证毕。

## 6. 实际 Heegner 点与 BDP 分母的结论

$-43,-163$ 都是基本判别式，两个域的类数均为 $1$：由约化二元二次型的界 $a\le\sqrt{|D|/3}$ 逐项检查，唯一约化型分别为 $[1,1,11]$ 和 $[1,1,41]$。并且
$$\left(\frac{-43}{41}\right)=
\left(\frac{-163}{41}\right)=1.$$
这里 $-43\equiv39\pmod{41}$、$-163\equiv1\pmod{41}$；脚本也精确检查类数与两个 Kronecker 符号。因此两个域分别满足 level $41^2$ 的经典 Heegner 假设。

层 41 的全部 new、Fricke $+$ 因子已有 $L'(f,1)\ne0$，此处沿用 R57 核查的 DLF §5.3 输入，不把它改称本文的数值实验。定理 4 和经典 Gross–Zagier 遂给：对这两个 $D$，每个投影
$$y_f^{(D)}=e_f[P_D-\infty]$$
均非挠；由类数一及 Fricke $+$ 共轭关系，它在张量 $\mathbb Q$ 后为有理 Mordell–Weil 向量。每个因子的有理 Mordell–Weil 模是秩一 $E_f$ 模，故任一 $D$ 都能同时为全部实际因子提供 Heegner 基向量。

由 R47、R68 的对数定理，其每个系数嵌入下的对数在每个辅助素数均非零。特别在共同普通且在 $K_D$ 分裂的 $47$，原始 BDP 公式给
$$\boxed{
L_{47,\rm anti}(f^\sigma/K_D,1)
=\left(\frac{48-\sigma(a_{47}(f))}{47}\right)^2
\left(\log_{\omega_{0,f,\sigma}}y_f^{(D)}\right)^2\ne0.
}\tag{6.1}$$
$48-\sigma(a_{47}(f))\ne0$ 可由权二 Weil 界立即核验。$47$ 也避开 R71 已算出的极化分母支撑，故可用实际项链同源 $q$ 及其在 $47$ 处的整右逆将这些点传入 $A=J_{\rm ns}^+(41)$。

这些结论没有证明圆分 $47$ 进导数或自高度非零。也没有计算规范平移 $\xi$、混合高度或 CM 根导数。尤其 $47$ 并非在每一个系数域中完全分裂；例如 $\mathbb Q(\zeta_{14})^+$ 的情况已排除这一点。故 (6.1) 使用 R68 核查过的一般系数嵌入 BDP 定理，不能仅凭本结果把 Hashimoto 在完全分裂便利假设下书写的圆分公式跨素数延拓。

## 7. 完整的有限证书与复算方法

本结果的全部新文件如下：

- `scripts/p41_twist_nonvanishing.gp`：从零构造有理模符号、new 部分、Fricke $+$ 基，求两条扭曲路径行、真实 $T_2,T_3,T_{47}$，打印带完整矩阵的 JSON 证书。
- `scripts/data/p41_twist_certificate.json`：20,551 字节，包含 $H\bmod1009$、两条整数扭曲行、全部八个特征多项式因子，以及 $T_{47}\bmod47$。
- `scripts/verify_p41_twist_certificate.py`：独立重建 Krylov 矩阵并做有限域消元，只使用 Python 标准库。

证书 SHA-256：

```text
1c0feeac934b5fa55f78b8ee318a829f2212d4f87b95532e4881ac72980e1ceb
```

从根目录运行：

```text
gp -q -f topics/serre-uniformity/scripts/p41_twist_nonvanishing.gp
python topics/serre-uniformity/scripts/verify_p41_twist_certificate.py
```

本次两种程序均运行完成：PARI 从头构造及全部精确核验约 $7$ 秒，Python 独立有限域核验约半秒。耗时只是本环境的执行记录，不是一般层的复杂度断言。PARI 程序需要精确模符号实现；独立 Python 程序核验导出的有限线性代数，不替代对原始模符号空间及算子构造的复算。

所用 PARI 官方源码包为 `pari-2.19.0.tar.gz`，SHA-256：

```text
f317b9722eb5d9094a60303774f066f3a83e3ec1f170be8546c44d7583f30b6d
```

没有把临时二进制模符号缓存、编译产物或第三方大型源码放入仓库。证书中的基由明示的版本及上述构造固定；若另一版本选取不同的有理基，具体非零行列式余数可能变化，应重新导出相应矩阵核验，不能只比较数字 $161,415$。

## 8. 来源及新增内容

- Yu. I. Manin, **Parabolic points and zeta-functions of modular curves**, *Mathematics of the USSR-Izvestiya* **6** (1972), 19–64，DOI [10.1070/IM1972v006n01ABEH001867](https://doi.org/10.1070/IM1972v006n01ABEH001867)，[原刊入口](https://www.mathnet.ru/eng/im2290)、[已打开核对的英文原刊 PDF](https://www.mathnet.ru/links/3d5fd2ca133cef29f025df42b0c53724/im2290_eng.pdf)。§1.2 的有向路径及同调，Theorem 1.9 的可计算生成关系，§3.8（pp.36–37）的本原字符扭曲积分公式。本文 (2.3) 另以选定微分规范完整推导，避免借用不同 $2\pi i$ 约定。
- [PARI/GP 官方 Modular symbols 文档](https://pari.math.u-bordeaux.fr/dochtml/html/Modular_symbols.html)：`msinit`、`msnew`、`msatkinlehner`、`mshecke`、`mseval`、`msstar` 的空间、符号和矩阵含义。本次还核对了官方 2.19.0 源码包内同名函数文档；[官方源码包目录](https://pari.math.u-bordeaux.fr/pub/pari/unix/) 列明该版本发布于 2026-09-28。
- R47、R57、R68：真实解析秩一因子、DLF 层 41 输入、Heegner 投影与一般系数嵌入的 BDP 公式；R71：实际项链同源及极化分母。

经典模符号公式、Gross–Zagier 与 BDP 都不是本文的新发现。本文新完成的是层 41 上**两个共同 Heegner 域的全因子精确非消失证书**、共同普通素数 $47$ 的实际算子证书，以及它们对 R68 高度输入的严格接入。
