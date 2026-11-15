# R832 — 原低权三重张量的 Chow 收缩与纯原 λ 分量

日期：2026-11-15。**状态：下述 Chow 动机分解、三个混合分量的有理等价消失及原对角类的纯 λ 性已证明。唯一端点类的非零性、与 R814 canonical 类的比较，以及原中央的跨素数非零仍开放。**

本篇把 R826 的表示分解提升到真正的 Chow 对应，继而消去三个混合分量。
结果适用于 R830/R831 的不同退化映射，也适用于整个已选定的二处旧空间。
只使用权一动机的全忠实性、椭圆曲线的乘法对应和已发表的权二秩零定理；
不从高余维的 Galois 表示同构推断 Chow 类相同。

## 1. 固定对象、系数与所要证明的范围

沿用原
$$
K=\mathbf Q(\omega),\qquad E_0:y^2=x^3+1,\qquad
\psi_0=\psi_{E_0},\qquad \eta=\eta_{10},
$$
$$
(k_4,k_{10},k_{16})=(13,1,7),\qquad
\eta_j=\eta^{k_j},\qquad
\psi_{17}=\eta^3\psi_0.
\tag{1}
$$
$\eta$ 的阶恰为18，全部有限角色、reciprocity 方向和解析 CM type 都按 R806/R826。
取包含这些角色值和 Hecke 特征值的数域 $\mathbb E$ 为系数域。
**扩张系数域不扩张循环的几何定义域。**

记 $\mathbb L=h^2(E_0)$ 为 Lefschetz 动机；其实现是 R826 的范数因子 $\mathrm N$。
所有动机均取有理等价和 $\mathbb E$ 系数，Chow 群记为
$$
\mathrm{CH}^a(M)=\operatorname{Hom}(\mathbb L^a,M).
\tag{2}
$$
对权二新形式 $x$，$M_x$ 指其模块化阿贝尔簇的实际 $h^1$ Hecke 直和因子。
这些因子通过曲线与 Jacobian 的代数对应实现。
令
$$
\beta_j=\eta_j^{-2}\psi_0,\quad
\gamma_\ell=\eta_\ell^{-7}\psi_0,\quad
\lambda_\ell=\eta_\ell^{-1}\psi_0^3,
$$
$$
f=\theta(\psi_{17}),\qquad g_j=\theta(\beta_j).
\tag{3}
$$
固定 R826 的有序对
$$
\begin{array}{c|c}
\ell&(j,k)\\ \hline
4&(10,16)\\
10&(16,4)\\
16&(4,10).
\end{array}
\tag{4}
$$
本篇处理的八维直和因子是
$$
M=M_f\otimes M_{g_j}\otimes M_{g_k}.
\tag{5}
$$
在共同目标 $X_0(10404)\times X_0(2601)^2$ 中，由实际 Hecke 提取映射得到它。
R831 的次数公式把同一结论传回 $X_1$，不把不同旧空间副本直接相认。

以下先在几何基域 $K$ 证明，再用限制／余限制降回 $\mathbf Q$。
定义 $M_{\lambda_\ell}$ 为 (5) 中全部三个 CM 符号同号的两个直和因子。
这是真实 CM 幂等元的像；其实现为原 $AI(\lambda_\ell)$。
本篇不需要另外选择一个权四 Kuga–Sato 模型并声称二者的高余维 Chow 对应已经比较。

## 2. 原权一因子的 Artin–CM Chow 呈示

在 $K$ 上，$[\omega]$ 给原椭圆曲线的精确 Chow 幂等分解
$$
h^1(E_0)_K=H_+\oplus H_-,
\tag{6}
$$
其中实现分别为 $\psi_0,\bar\psi_0$。
令 $A(\eta^m)$ 为有限角色 $\eta^m$ 对应的 Artin Chow 动机。
若 $H/K$ 是使 $\eta$ 平凡的有限 Galois 扩张，
则它由 $h^0(\operatorname{Spec}H)$ 的群代数幂等元给出。
尤其
$$
A(\eta^m)\otimes h^1(E_0)
$$
是 $h^1(\operatorname{Res}_{H/K}E_{0,H})$ 的直和因子。

这使所有待比较对象都留在阿贝尔簇的 $h^1$ 范畴中。
Faltings 的同态／同源定理，加上 Scholl Corollary 5.10
的阿贝尔簇与其 $h^1$ Chow 动机的全忠实性，给实际同构
$$
\begin{aligned}
(M_f)_K
&\simeq A(\eta^3)H_+\oplus A(\eta^{-3})H_-,\\
(M_{g_j})_K
&\simeq A(\eta^{-2k_j})H_+\oplus A(\eta^{2k_j})H_-,\\
(M_{g_k})_K
&\simeq A(\eta^{-2k_k})H_+\oplus A(\eta^{2k_k})H_-.
\end{aligned}
\tag{7}
$$
这里完整角色的实现同构由 R826 的定义给出。
同态定理在各个幂等直和因子上仍成立；
在必要的有限系数扩张后可取代数对应及其逆。
因此 (7) 不是把一般高权动机的实现同构视作 Chow 同构。

这个步骤也没有声称 $E_0(H)$ 的秩为零。
后面消失的是 (7) 中指定 Artin 因子收缩得到的 $K$ 上实际阿贝尔簇部分。

## 3. 混合 CM 对的精确 Lefschetz 收缩

**引理 1。** 在 $K$ 上的 Chow 动机范畴中，乘法对应给
$$
\boxed{H_+\otimes H_-\simeq\mathbb L.}
\tag{8}
$$

证明。使用 Scholl Theorem 5.2(ii) 的对角拉回／外幂乘法同构
$$
\bigwedge\nolimits^2h^1(E_0)\simeq h^2(E_0)=\mathbb L.
\tag{9}
$$
这里外幂、置换和乘法使用该定理自身的动机约定。
将 (6) 的两个 CM 幂等元代入 (9)，其混合直和因子自然同构于
$H_+\otimes H_-$。
两个同号的外幂因子上 $[\omega]^*$ 的特征分别为
$\omega^2$ 和 $\omega$，而 $\mathbb L$ 上该作用为1。
因此这两个因子在 (9) 的源中已为零，混合因子到 $\mathbb L$ 是同构。
Scholl §5.4 明确说明 (9) 对有理等价成立。
故 (8) 及其逆都是代数对应，不只在 cohomology 上成立。证毕。

(8) 的准确非零标量可以由同一乘法对应固定；本篇仅用其可逆性。
后续消失陈述因而不依赖任何未指定的复周期或 $p$-adic 周期。

把 (7) 展开成八条 CM 线。
全同号两条组成 $M_{\lambda_\ell}$；其余六条分别含一个 $H_+$、一个 $H_-$，
对这对使用 (8)，并保留相应 Artin 角色。
R826 的完整角色等式给：
$$
\begin{array}{c|c|c}
\text{从 }(+,+,+)\text{ 出发的改变}
&\text{收缩前的实现}&\text{收缩后的权一角色}\\ \hline
\text{仅第一符号共轭}&\mathrm N\gamma_\ell&\gamma_\ell\\
\text{仅第二符号共轭}&\mathrm N\psi_{17^3}&\psi_{17^3}\\
\text{仅第三符号共轭}&\mathrm N\psi_{17^5}&\psi_{17^5}.
\end{array}
\tag{10}
$$
例如后两项的 $\eta$ 指数是
$3+2(k_j-k_k)=9$ 和 $3-2(k_j-k_k)=15\bmod18$。
每项与其全共轭项配对，再用第2节的权一同构，得到真正的 Chow 分解
$$
\boxed{
M_K\simeq
(M_{\lambda_\ell})_K
\oplus \mathbb L\otimes(M_{\theta(\gamma_\ell)})_K
\oplus \mathbb L\otimes h^1(E_{17^3})_K
\oplus \mathbb L\otimes h^1(E_{17^5})_K .
}
\tag{11}
$$
所有有限角色与 Tate 因子保留。
这里 $M_{\theta(\gamma_\ell)}$ 是下一节的三维阿贝尔簇的指定二维 Hecke 因子。

## 4. 三个参考对象的真正 Mordell–Weil 秩零

### 4.1 阶十八参考对象是一个三维阿贝尔簇的完整轨道

R757 已证明
$$
\gamma_4=\Psi^{(0)}_8,\quad
\gamma_{10}=\Psi^{(0)}_2,\quad
\gamma_{16}=\Psi^{(0)}_{14},
\tag{12}
$$
其三个 theta series 是实三次域
$$
F^+=\mathbf Q(\zeta_9+\zeta_9^{-1})
$$
的完整共轭轨道，level10404、平凡 nebentypus。
令 $A_\gamma/\mathbf Q$ 为该轨道对应的模块化阿贝尔三维簇。
R757 式(39) 的原完整范数公式分别给
$$
L(\gamma_\ell,1)=C_\ell s_\ell^2>0 .
\tag{13}
$$
因此 $L(A_\gamma,1)\ne0$，且每个原 Hecke 因子的中心值非零。
这里没有把三条非有理新形式称作三条 $\mathbf Q$ 上的椭圆曲线。

为明确支付所用秩零定理的原假设，取其中任一权二新形式。
Kolyvagin–Logachev Theorem 0.3／1.3.2 使用中心值非零，
以及一个辅助虚二次域，使该形式的二次扭曲在1处单零、
判别式素于 $2N$ 并为模 $4N$ 的平方。
Bump–Friedberg–Hoffstein (1990) 引言 Theorem(i)，
对有限集合 $S=\{2,3,17\}$ 给所有 $S$ 中素数分裂的负基本判别式 $D$，
且扭曲在1处恰单零；原形式符号为 $+1$。

这些分裂条件确实满足原定理的额外算术条件：
$2$ 分裂给 $D\equiv1\bmod8$，因而 $D$ 为模16的奇数平方；
$3,17$ 分裂使 $D$ 为这两个奇素数处的单位平方，
由 Hensel 提升为模 $3^2,17^2$ 的平方。
CRT 给模 $4N=16\cdot3^2\cdot17^2$ 的平方条件；
$(D,2N)=1$，且分裂条件排除 $D=-1,-3$。
所以已发表的两项定理适用，得到
$$
\boxed{A_\gamma(\mathbf Q)\otimes\mathbf Q=0.}
\tag{14}
$$
这些定理在此不要求形式非 CM。
本篇只取它们的 Mordell–Weil 结论，不把此秩零参考对象的结论当成原秩二曲线的结论。

### 4.2 两个 sextic 参考对象与基域 K

R307 的完整原参考公式为
$$
\frac{L(E_{17^3},1)}{\Omega_{17^3}}=3,\qquad
\frac{L(E_{17^5},1)}{\Omega_{17^5}}=6.
\tag{15}
$$
同一已发表秩零定理（或原 R307 所用 CM 秩零定理）给这两条曲线在 $\mathbf Q$ 上秩零。

令 $\varepsilon_K$ 是 $K/\mathbf Q$ 的二次角色。
三个对象的每个二维实现均自 $K$ 的 CM 角色诱导，故
$$
\operatorname{Ind}_{G_K}^{G_\mathbf Q}\chi\otimes\varepsilon_K
\simeq \operatorname{Ind}_{G_K}^{G_\mathbf Q}\chi.
\tag{16}
$$
由 Faltings 同源定理，每个对象 $A$ 的二次扭曲 $A^{\varepsilon_K}$
与 $A$ 在 $\mathbf Q$ 上同源。
二次扩张上的正负分解于是给
$$
A(K)\otimes\mathbf Q
\simeq
(A(\mathbf Q)\otimes\mathbf Q)
\oplus(A^{\varepsilon_K}(\mathbf Q)\otimes\mathbf Q)
=0.
\tag{17}
$$
这里分别取
$$
A=A_\gamma,\quad E_{17^3},\quad E_{17^5}.
$$
同样，它们的对偶阿贝尔簇由极化同源，故
$$
\boxed{A^\vee(K)\otimes\mathbf Q=0.}
\tag{18}
$$
(17) 只扩到固定 CM 二次域；不对第2节的任意 Artin 平凡化域断言秩零。

## 5. 三个混合 Chow 群全部消失

**引理 2。** 对上述任一阿贝尔簇 $A/K$，
$$
\mathrm{CH}^2(\mathbb L\otimes h^1(A))_{\mathbb E}
\simeq
\mathrm{CH}^1(h^1(A))_{\mathbb E}
\simeq
\operatorname{Pic}^0(A)(K)\otimes_\mathbf Z\mathbb E.
\tag{19}
$$

第一同构是 (2) 的 Tate 移位。
第二同构由 $h^1$ 的标准 Chow–Künneth 投影给出：
在 $\mathrm{CH}^1(A)$ 中，$[n]^*$ 特征为 $n$ 的部分恰为
$\operatorname{Pic}^0(A)(K)\otimes\mathbf Q$。
可以直接由 Scholl Proposition 3.3、Corollary 3.4 及
§5.11 的 canonical eigenspace 分解读取。
阿贝尔簇有原点，Picard 对偶的这一定义与有理线丛类兼容。

由 (18)、(19) 以及 Hecke 投影，(11) 的三个混合项的 $\mathrm{CH}^2$ 全部为零。
故有：

**定理。** 对原已选定三重张量，
$$
\boxed{
\mathrm{CH}^2(M_K)
=\mathrm{CH}^2((M_{\lambda_\ell})_K).
}
\tag{20}
$$
右侧通过同一个 CM 幂等元的包含识别为左侧直和因子。
这个结论在有理等价层面成立，不只是 Abel–Jacobi 的三个分量为零。

## 6. 回到 Q 上的端点类与全部旧空间

全同号两条线的和及每个混合共轭对的投影都在
$\operatorname{Gal}(K/\mathbf Q)$ 下不变：
几何复共轭同时交换所有 $+$、$-$ 及相应反圆分 Artin 角色，
系数域 $\mathbb E$ 保持为系数，不随几何基变换另作选择。
以余限制除以2将这些对应降回 $\mathbf Q$。
限制在 Chow 群上单射，因为
$$
\operatorname{cor}_{K/\mathbf Q}
\operatorname{res}_{K/\mathbf Q}=2.
\tag{21}
$$
对应的幂等性和全部关系也由同一个限制单射下降。

因此 (20) 对 $\mathbf Q$ 上的原类同样成立。
特别，令 $Z$ 为 R831 共同目标中的唯一端点类，则
$$
\boxed{Z=\operatorname{pr}_{\lambda_\ell}Z.}
\tag{22}
$$
对任意旧空间提取系数 $c=(c_0,c_1,c_2)$、
$d=(d_0,d_1,d_2)$，仍保 R831 的准确式
$$
Z(c,d)=(c_0d_2-c_2d_0)Z
      =(c_0d_2-c_2d_0)\operatorname{pr}_{\lambda_\ell}Z.
\tag{23}
$$
传到 $X_1$ 时仍保原遗忘次数1632、816和退化次数12；
本篇没有改写这些拉回／推出的归一。

由 Abel–Jacobi 的对应相容性，R826 表(20) 的三个混合 ordinary 槽
对以上全部类都为零。
第四槽仍是 R830/R831 的完整原两项公式。
例如端点 $(0,2)$：
$$
\boxed{
AJ_p(Z^1_{02})(\omega_f\omega_g\omega_h)
=
\frac{
 \left\langle\omega_f,\,
 [\{4G_g(Q)h(Q^4)-\bar\pi G_h(Q^4)g(Q^p)\}\,dQ/Q]
 \right\rangle}
 {1+\bar\pi/\pi^2}.
}
\tag{24}
$$
这里 $Z^1_{02}$ 及测试的准确 $X_1$ 规范均按 R831；
不能把共同目标类与高层拉回类的标量省略。

## 7. 新结论留下的实际问题

(22) 证明修复后的端点类在原 $\lambda_\ell$ Chow 分量内；
它没有证明这个类非零，也没有证明该 Chow 群是一维。
R814 的另一固定 generalized-Heegner／canonical 来源
即使落在同一实现，也不能据此与 $Z$ 成比例。
仍须真正的代数对应或全局类比较，并保原有限 test vector、
good pair、period／基比和 Soulé 特殊化。

同理，三个 ordinary 槽全零与 (24) 非零并不矛盾；
它们是不同 CM 因子上的测试。
R818 的复导数非零和 R830 的所有有限局部测试非零仍不能替代 (24) 的指定 $p$-adic 非零。
固定7993的 R817 检测只适用于其已经证明的原类。
本篇没有增加“无穷多个不同 $p$”的结论，主目标保持开放并继续。

## 8. 证明来源

本篇没有新增程序运行或可重算数据。

- A. J. Scholl, *Classical motives*, Proceedings of Symposia in Pure Mathematics
  **55**, Part 1 (1994), 163–187；
  Proposition 3.3、Corollary 3.4、Theorem 5.2(ii)、§5.4、
  Corollary 5.10、§5.11。作者全文：
  <https://www.dpmms.cam.ac.uk/~ajs1005/preprints/classical_motives.pdf>。
- G. Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*,
  Invent. Math. **73** (1983), 349–366，同态／同源定理：
  <https://doi.org/10.1007/BF01388432>。
- V. A. Kolyvagin, D. Yu. Logachev,
  *Finiteness of the Shafarevich–Tate group and the group of rational points
  for some modular abelian varieties*,
  Algebra i Analiz **1**:5 (1989), 171–196；
  English translation, Leningrad Math. J. **1**:5 (1990), 1229–1253。
  Theorem 0.3（俄文印页173）、Theorem 1.3.2（印页176）；
  原文的辅助虚二次域条件由本篇§4.1核对：
  <https://www.mathnet.ru/eng/aa47>；
  <https://www.mathnet.ru/php/getFT.phtml?jrnid=aa&option_lang=eng&paperid=47&what=fullt>。
- D. Bump, S. Friedberg, J. Hoffstein,
  *Nonvanishing theorems for L-functions of modular forms and their derivatives*,
  Invent. Math. **102** (1990), 543–618，引言 Theorem(i)，指定有限集合全部分裂：
  <https://doi.org/10.1007/BF01233440>；
  <https://wstein.org/papers/bib/bump-friedberg-hoffstein-nonvanishing.pdf>。
- [R757](R757-original-type-zero-six-spectrum-and-order-nine-lines.md)：
  三个原 $\gamma$ 的全角色、实三次共轭轨道、式(39)中心值严格非零。
- [R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)：
  两条原 sextic 参考曲线的完整中心值与秩零。
- [R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)、
  [R830](R830-distinct-degeneracy-test-vectors-and-fourth-slot.md)、
  [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)：
  全有限角色张量、真实退化映射、局部测试、共同目标及完整杯积归一。
