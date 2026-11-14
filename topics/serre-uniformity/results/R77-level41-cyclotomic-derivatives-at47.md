# R77. 层 41 全部实际因子的 47 进圆分导数非消失

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明；有界测度、精度界和有限域证书均明确。** 令 $\mathcal F_{41}$ 如 R74，包含 level $1681$、权二、平凡 nebentype、new、Fricke $+$ 的全部 $54$ 个归一化特征形式及系数共轭。R74 已证明它们在辅助素数 $47$ 的每个系数地方都普通。本文进一步证明
$$\boxed{\operatorname{ord}_{s=1}L_{47}(f,s)=1
\qquad(f\in\mathcal F_{41}),}\tag{0.1}$$
其中 $L_{47}(f,s)$ 是普通单位根、平凡 Teichmüller 分支的标准圆分 $47$ 进 $L$ 函数，变量为 $\langle x\rangle^{s-1}$。结论对每个 $47$ 进系数嵌入都成立，不要求系数域完全分裂。

核心证书是一个实际 $54$ 维导数向量：除以 $47$ 后，其 Hecke Krylov 行列式模 $47$ 等于 $21\ne0$。这是严格的首位计算，未用浮点 $L$ 值、$p$ 进 BSD 猜想或尚未实现的高精度算法。

本文先给一变量圆分导数的结论。把它与 Rankin 基变换导数及实际高度作精确比较，应使用相应已核查的 Gross–Zagier 公式与周期规范；这里不额外猜测不同来源之间的极化或周期倍率。

## 1. 实际 star $+$ 空间与全部路径值的整性

现在使用与 R74 的奇扭曲不同的星号分支：
$$\mathcal M^+=
\left(M_{\rm cusp}^{\rm new}(\Gamma_0(1681),2)\right)
^{\iota=+1,\,w_{1681}=+1}.
\tag{1.1}$$
星号仍由 $\operatorname{diag}(-1,1)$ 作用，Fricke 对合仍为 $z\mapsto-1/(1681z)$；两种 $+$ 含义不同。

通过实际有理模符号定义基：

```gp
M = msinit(1681, 2, 1);
Nnew = msnew(M);
W = msatkinlehner(M, 1681, Nnew);
P = Nnew[1] * matker(W - matid(117));
```

$M$ 的维数为 $144$，new cuspidal 部分维数为 $117$，$P$ 的 $54$ 列是 (1.1) 的基。记这些实际有理符号为 $\phi_1,\ldots,\phi_{54}$，并定义行向量
$$v(r)=\bigl(\phi_1([r,\infty]),\ldots,
\phi_{54}([r,\infty])\bigr).
\tag{1.2}$$

### 引理 1：$v(r)$ 对每个有理 $r$ 都是整数行

**证明。** `mspathgens(M)` 给 $\operatorname{Div}^0(\mathbb P^1(\mathbb Q))$ 的 $289$ 个 $\mathbb Z[\Gamma_0(1681)]$ 生成路径，其中 $287$ 个是自由的 $E_1$ 路径，另 $2$ 个带椭圆二阶关系。权二的系数作用平凡，因此后两条路径上任何有理模符号的值均为零。PARI/GP 2.19.0 的权二 `mseval` 在省略路径时返回前 $287$ 个自由路径值；这也由其 `src/basemath/modsym.c` 中 `mseval` 的 `k == 2` 分支确认。脚本用
```gp
generator_values = mseval(M,P);
```
精确计算全部 $54\times287$ 个自由生成元值，并核验其共同分母为 $1$；加上另两条零值，即已处理全部生成路径。

任意有理端点路径可由连分数写成这些生成元的 $\mathbb Z[\Gamma_0]$ 线性组合；这正是模符号的整数生成关系。权二的系数表示 $V_2=\mathbb Q[X,Y]_0=\mathbb Q$ 上，$\Gamma_0$ 作用平凡。因此任意路径值都是已核验整数值的整数线性组合，仍为整数。证毕。

这个证明不能由“$P$ 的矩阵条目为整数”或“$T_{47}$ 的分母不含 $47$”替代；这里确实检查了实际符号在全部路径生成元上的值。

在此基中写
$$T=T_{47},\qquad H=T_2+2T_3.$$
两者的共同分母各为 $2$，且
$$TH=HT,\qquad\det(T\bmod47)=28\ne0.
\tag{1.3}$$
因而它们都作用于 $\mathbb Z_{47}^{54}$，$T$ 还是可逆矩阵。脚本同时核验 $P$ 模 $47$ 的秩为 $54$。

## 2. 在完整 Hecke 模上构造普通测度

下面把辅助素数暂写为 $\ell=47$。由 (1.3)，在矩阵代数中存在唯一与 $T$ 同余的普通根
$$\alpha\in\operatorname{GL}_{54}(\mathbb Z_\ell),\qquad
\alpha^2-T\alpha+\ell I=0,\qquad
\alpha\equiv T\pmod\ell.
\tag{2.1}$$
它可由 $\alpha_0=T$、$\alpha_{n+1}=T-\ell\alpha_n^{-1}$ 收敛构造。该迭代在模 $\ell$ 为可逆的矩阵上是收缩，并始终处于 $T$ 生成的交换闭子代数，所以 $\alpha$ 与 $T,H$ 均交换。逐 Hecke 特征线，它正是 $X^2-a_\ell(f)X+\ell$ 的单位根。

记
$$v_n(a)=v(a/\ell^n),\qquad n\ge0.$$
对 $n\ge1$ 定义行向量值圆柱质量
$$\boxed{\quad
\mu(a+\ell^n\mathbb Z_\ell)
=v_n(a)\alpha^{-n}-v_{n-1}(a)\alpha^{-n-1}.
\quad}\tag{2.2}$$

### 命题 2：真实、整、有界的分布

(2.2) 定义 $\mathbb Z_\ell^{54}$ 值的有界测度；限制到 $\mathbb Z_\ell^\times$ 后可对连续函数积分。

**证明。** 更换 $a$ 的圆柱代表只让 $a/\ell^n$ 和 $a/\ell^{n-1}$ 平移整数；这些平移属于 $\Gamma_0(1681)$，所以质量与代表无关。

实际权二 Hecke 模路径恒等式是
$$\sum_{b=0}^{\ell-1}v_{n+1}(a+b\ell^n)
=v_n(a)T-v_{n-1}(a).
\tag{2.3}$$
它来自 $T_\ell$ 的 $\ell+1$ 个双陪集代表：$z\mapsto(z+b)/\ell$ 以及 $z\mapsto\ell z$。此外，$v_n(a+b\ell^n)=v_n(a)$。于是对 (2.2) 的 $\ell$ 个子圆柱求和得
$$\begin{aligned}
\sum_b\mu(a+b\ell^n+\ell^{n+1}\mathbb Z_\ell)
&=(v_n(a)T-v_{n-1}(a))\alpha^{-n-1}
-\ell v_n(a)\alpha^{-n-2}\\
&=v_n(a)\alpha^{-n}-v_{n-1}(a)\alpha^{-n-1},
\end{aligned}$$
其中使用 $T=\alpha+\ell\alpha^{-1}$。这证明分布关系。

引理 1 给每个 $v_n(a)$ 整，而 $\alpha^{\pm1}$ 是 $\mathbb Z_\ell$ 矩阵，故所有圆柱质量同时属于 $\mathbb Z_\ell^{54}$。这给统一范数上界，因而构成有界测度。证毕。

脚本还在 $n=1$ 的全部 $46$ 个单位剩余类上，对实际整数路径值**精确**核对 (2.3)，确认所用软件 Hecke 作用与上式的归一化相同。

## 3. 与每个标准圆分 $L$ 函数的关系

Balakrishnan–Müller–Stein (2016) §2.2 在任意系数域完成 $(E_f)_\mathfrak l$ 中，以 Shimura 周期归一化的 plus 模符号 $[r]^+_f$ 定义普通测度
$$\mu_{f,\alpha_f}(a+\ell^n\mathbb Z_\ell)
=\alpha_f^{-n}[a/\ell^n]^+_f
-\alpha_f^{-n-1}[a/\ell^{n-1}]^+_f,
\tag{3.1}$$
以及
$$L_\ell(f,s)=\int_{\mathbb Z_\ell^\times}
\langle x\rangle^{s-1}\,d\mu_{f,\alpha_f}(x).
\tag{3.2}$$
这里调用的是该文已定义并证明插值性质的 $L$ 函数，不使用文中的 BSD 猜想。

取一个足够大的有限 $L/\mathbb Q_\ell$，包含所有相关系数嵌入与特征向量。每个代数周期归一化的 $[\ ]^+_{f,\sigma}$ 是 $\mathcal M^+\otimes L$ 的某条非零特征向量，写为 $P u_{f,\sigma}$。由 (2.1)–(2.2)，
$$\mu\,u_{f,\sigma}=\mu_{f^\sigma,\alpha_{f,\sigma}},
\tag{3.3}$$
只要按该归一化选取 $u_{f,\sigma}$；换用另一非零 Shimura 周期，只会将该列向量和对应 $L$ 函数乘一个非零标量。因此非消失不依赖先计算周期倍率，更不需要把复周期本身直接嵌入 $\mathbb Q_\ell$。

令实际导数行向量为
$$\mathscr D:=\int_{\mathbb Z_\ell^\times}
\log_\ell(x)\,d\mu(x)\in\ell\mathbb Z_\ell^{54}.
\tag{3.4}$$
由 (3.2)–(3.3)，
$$\mathscr D u_{f,\sigma}=L_\ell'(f^\sigma,1).
\tag{3.5}$$
这里 $\log_\ell$ 杀掉 Teichmüller 部分，故 (3.4) 就是对 $s$ 的导数。

另外，$w_{1681}=+1$ 将路径 $[0,\infty]$ 变成其反向，故
$$v(0)=0.$$
实际脚本得到完整零行。对 (2.2) 的模 $\ell$ 单位圆柱求和，(2.3) 给
$$\mu(\mathbb Z_\ell^\times)
=v(0)(I-\alpha^{-1})^2=0.
\tag{3.6}$$
所以所有 (3.2) 在 $s=1$ 都为零。证明 (0.1) 只剩证明 (3.5) 的每个值非零。

## 4. 只用 $\ell^2$ 级路径即可严格求导数首位

对 $\ell\nmid a$，定义 Fermat quotient
$$q_\ell(a)=\frac{a^{\ell-1}-1}{\ell}\pmod\ell.$$
因为 $\ell>2$，
$$\frac{\log_\ell(a)}\ell
\equiv\frac{q_\ell(a)}{\ell-1}
\equiv-q_\ell(a)\pmod\ell.
\tag{4.1}$$
记这个剩余值为 $w(a)\in\mathbb F_\ell$。

### 引理 3：首位公式及完整误差界

置 $\overline T=T\bmod\ell$，则
$$\boxed{\quad
\frac{\mathscr D}{\ell}\bmod\ell
=\left(\sum_{\substack{1\le a<\ell^2\\\ell\nmid a}}
w(a)v(a/\ell^2)\bmod\ell\right)\overline T^{-2}.
\quad}\tag{4.2}$$

**证明。** $\log_\ell(x)/\ell$ 在每个模 $\ell^2$ 的单位圆柱上模 $\ell$ 为常数。命题 2 的圆柱质量是 $\mathbb Z_\ell$ 整的，所以把积分中的函数替换为这些常数，误差属于 $\ell\mathbb Z_\ell^{54}$。这是一个实际精度界；若没有质量的整性，不能使用这一界。

将 (2.2) 在 $n=2$ 代入，并用 $\alpha\equiv T\pmod\ell$，所得右侧先为
$$S_2\overline T^{-2}-S_1\overline T^{-3},$$
其中
$$S_i=\sum_{\substack{1\le a<\ell^2\\\ell\nmid a}}
w(a)v(a/\ell^i)\pmod\ell\quad(i=1,2).$$
固定 $a_0\in\{1,\ldots,\ell-1\}$，写 $a=a_0+\ell b$。二项式展开给
$$q_\ell(a_0+\ell b)\equiv q_\ell(a_0)-b/a_0\pmod\ell,$$
故
$$\sum_{b=0}^{\ell-1}w(a_0+\ell b)=0\quad\text{于 }\mathbb F_\ell.$$
同时 $v(a/\ell)=v(a_0/\ell)$，因两端相差整数平移。因此 $S_1=0$，得到 (4.2)。整个推导始终保留普通根的 $\overline T^{-2}$ 因子。证毕。

## 5. 精确首位向量及全因子非消失

令 $\ell=47$。脚本精确求 (4.2) 的 $47\cdot46=2162$ 个有理路径，得到
$$\begin{split}
R:=\mathscr D/47\bmod47=(&1,12,10,4,32,25,34,27,22,40,23,19,23,19,24,15,42,10,\\
&17,11,44,23,29,34,38,19,44,28,26,35,0,1,2,27,46,7,\\
&45,37,44,26,27,3,22,33,3,42,30,38,4,12,11,27,28,44).
\end{split}\tag{5.1}$$
所有第二项的加权和为零，且实际检验 $R\overline T^2=S_2$。

### 定理 4：导数向量对全部实际 Hecke 特征线非零

以 $\overline H=H\bmod47$ 形成
$$\overline K=
\begin{pmatrix}R\\R\overline H\\R\overline H^2\\\vdots\\R\overline H^{53}\end{pmatrix}.$$
则
$$\boxed{\operatorname{rank}_{\mathbb F_{47}}\overline K=54,
\qquad \det\overline K=21.}\tag{5.2}$$
因此对每个 $f\in\mathcal F_{41}$ 和每个 $47$ 进系数嵌入，$L_{47}'(f,1)\ne0$。结合 (3.6)，得到 (0.1)。

**证明。** (5.2) 由随文保存的 $\overline H,R$ 直接有限域消元得到，独立 Python 程序重建并核验此行列式。由引理 3，$\overline K$ 是真实矩阵
$$K(\mathscr D/47,H)=
\begin{pmatrix}\mathscr D/47\\(\mathscr D/47)H\\\vdots\\(\mathscr D/47)H^{53}\end{pmatrix}
\in M_{54}(\mathbb Z_{47})$$
的约化，故后者的行列式是 $47$ 进单位，特别是非零。

若某条实际特征线的非零向量 $u$ 满足 $Hu=\lambda u$ 且 $\mathscr D u=0$，则上述矩阵的每一行作用于 $u$ 都为零，与可逆性矛盾。将 $u=u_{f,\sigma}$ 并用 (3.5)，得全部导数非零。此证明没有把模 $47$ 的 Hecke 特征值是否分离当作额外假设；也不会将一次不满秩的试算误判为某个导数为零。证毕。

在这套明确基中还有
$$v_{47}\det K(\mathscr D,H)=54.$$
这是实际导数行的基依赖信息，不是对每个任意周期规范的标量导数宣称赋值恰为 $1$，更不是 Néron 规范高度调节子的赋值。

### 推论 5：实际 $54$ 维有理 Mordell–Weil 高度在 $47$ 非退化

采用 R75 的一般系数域 Gross–Zagier 规范和非零标准圆分方向，对 $D=-43$ 或 $-163$ 的每个实际 Heegner 向量及每个系数嵌入，都有
$$h_{\mathbb Q,\sigma}\bigl(y_f^{(D)},y_f^{(D)}\bigr)\ne0.$$
经 R71 的真实项链同源传到 $J=J_{\rm ns}^+(41)$ 后，R47 的每个高度系数满足
$$c_f\in(E_f\otimes\mathbb Q_{47})^\times.$$
因此同一普通 splitting 与圆分对数定义的实际高度配对
$$h_{47}:J(\mathbb Q)\otimes\mathbb Q_{47}
\times J(\mathbb Q)\otimes\mathbb Q_{47}\longrightarrow\mathbb Q_{47}$$
非退化。

**证明。** R75 使用 2015 年期刊版 Theorem B 和 (4.4.1)，已严格得到
$$C_{f,\sigma}^{(D)}
=\sigma(\mathcal P_{f,D})L'_{47}(f^\sigma,1)
L_{47}(f^\sigma\otimes\chi_D,1),$$
其中 $\mathcal P_{f,D}\ne0$；R74 和普通插值给最后一个因子非零，定理 4 给中间导数非零。期刊公式的字符因子 $\chi(|D|)^2$ 在求中心导数时乘上 $L_{47}(f,1)=0$ 而消失，不改变此等式。于是 $C_{f,\sigma}^{(D)}\ne0$。

R75 的 $h_K=2h_{\mathbb Q}$ 和普通 Euler 因子给
$$h_{\mathbb Q,\sigma}(y_f^{(D)},y_f^{(D)})
=\frac{C_{f,\sigma}^{(D)}}{2(1-\alpha_{f,\sigma}^{-1})^4}\ne0.$$
R68、R71 的真实点基传输只再乘非零的 $m_f^2\sigma(\kappa_f)$，因此每个 $\sigma(c_f)$ 非零。有限 étale 代数 $E_f\otimes\mathbb Q_{47}$ 的元素在全部特征嵌入非零等价于可逆。

最后，R47 的 Hecke 相容性把不同简单因子正交分开，并在每个秩一模上将高度写成
$$ (x,y)\longmapsto
\operatorname{Tr}_{E_f\otimes\mathbb Q_{47}/\mathbb Q_{47}}(c_fxy).$$
特征零有限 étale 代数的迹配对非退化，而乘 $c_f$ 可逆，所以每个块非退化。各块直和就是所述 $54$ 维实际高度。证毕。

这里使用的是 R75 已核查的一般系数域定理及非零代数周期校准，不调用 Disegni Theorem C 的 period-conjecture 假设。推论只判断非零和非退化，未省去具体高度数值中的周期、极化或微分倍率。

## 6. 保存的证书、执行范围与后续接口

文件为：

- `scripts/p41_cyclotomic_derivative.gp`：从零重建 star $+$、new、Fricke $+$ 空间；核查全部生成元值的整性，逐项求 $2162$ 条路径，核查实际 $T_{47}$ 的分布关系，输出证书。
- `scripts/data/p41_derivative_certificate.json`：保存两张 $54\times54$ 有限域矩阵 $\overline H,\overline T$、$S_2$、零第二项和实际导数首位行 $R$。
- `scripts/verify_p41_derivative_certificate.py`：用 Python 标准库独立核验 $\det\overline T=28$、$R\overline T^2=S_2$ 和 (5.2)，复用 R74 的有限域消元函数。

JSON 证书共 $14,862$ 字节，SHA-256 为

```text
d587111a2abbf3e85c75d0c0e9a489730c65037871bd9116d7151b7c7256de00
```

从仓库根目录运行：

```text
gp -q -f topics/serre-uniformity/scripts/p41_cyclotomic_derivative.gp
python topics/serre-uniformity/scripts/verify_p41_derivative_certificate.py
```

源码版本、官方包及其 SHA-256 与 R74 相同，均为 PARI/GP 2.19.0。这里没有调用 PARI 的 `mspadicmoments`：该接口的现有文档明确限制输入为有理一维特征符号，而本层八个因子的维数均大于 $1$。本文用明示的整向量值测度和首位 Riemann 和完成实际计算，不把一个接口限制误认为数学障碍。

最终完整脚本在本环境约 $24$ 秒运行完毕，包括全部路径生成元整性及 $46$ 个剩余类上的精确 Hecke 分布恒等式；独立 Python 证书核验也已通过。这一运行记录不作为一般层计算复杂度的断言。

R74 已经给 $K=\mathbb Q(\sqrt{-43})$ 或 $\mathbb Q(\sqrt{-163})$ 上全部 Heegner 投影非挠、全部 BDP 分母非零，并给共同普通处 $47$；R71 给这一处的实际同源极化与整投影。本文再提供所有一变量圆分导数的严格非消失。这些是实际高度函数所需的算术输入，但不会单独识别 Chow–Heegner 平移 $\xi$，也不会计算辅助局部高度的 CM 根导数或排除共同根。

## 7. 已核查的原始来源

- J. S. Balakrishnan, J. S. Müller and W. A. Stein, **A $p$-adic analogue of the conjecture of Birch and Swinnerton-Dyer for modular abelian varieties**, *Mathematics of Computation* **85** (2016), 983–1016，DOI [10.1090/mcom/3029](https://doi.org/10.1090/mcom/3029)，[出版抽印本](https://wstein.org/papers/mcom3029.pdf)。§2.2，pp.991–992：一般系数域完成中的 Shimura 归一化 plus/minus 模符号、普通测度和 (2.6) 的圆分 Mellin 定义；§2.5–2.6，pp.994–995：经典模符号求和与 overconvergent 方法的区别。本文只使用这些已定义的对象和性质，不使用其 BSD 猜想。
- [PARI/GP 官方 Modular symbols 文档](https://pari.math.u-bordeaux.fr/dochtml/html/Modular_symbols.html)：`mspathgens`、`mspathlog` 的 $\mathbb Z[\Gamma_0]$ 生成关系，`mseval` 的实际路径取值，及 `msinit`、`msnew`、`msatkinlehner`、`mshecke` 的精确空间和算子。原始源码包及版本哈希见 R74。
- D. Disegni, **$p$-adic heights of Heegner points on Shimura curves**, *Algebra & Number Theory* **9** (2015), 1571–1646，DOI [10.2140/ant.2015.9.1571](https://doi.org/10.2140/ant.2015.9.1571)，[期刊版](https://msp.org/ant/2015/9-7/ant-v9-n7-p03-s.pdf)。推论 5 使用 R75 的精确代入；本分支另独立打开核对了 Theorem A 前的一般系数域、Theorem B、(4.4.1) 的字符与非零代数周期因子、Propositions 5.1.2(5)、6.3.1(3)，与 R75 的高度基变换和基点校准一致。
- R74 证明的空间识别、普通性及经典扭曲非消失；R71 的实际极化；R68、R75 的周期、坐标与 Heegner 高度接口。本文新的实算是全 $54$ 维圆分导数的首位、其误差证明和满秩证书 (5.2)，并由此证明实际 $54$ 维高度非退化。
