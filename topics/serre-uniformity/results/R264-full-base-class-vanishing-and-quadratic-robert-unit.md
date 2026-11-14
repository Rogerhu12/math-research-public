# R264：完整基域的 43 类群消失与二次 Robert 单位的精确识别

**状态：已证明并完成两部分复算。** 固定 R171 的 \(p=43\)、
\(K=\mathbf Q(i)\) 以及 R219 的
\[
 F=K(A[43])^{\mathbf F_{43}^{\times}}=K(z),\qquad
 A:y^2=x^3-x,\qquad \Delta=\langle\sigma\rangle\simeq C_{44}.
\]
正算术 Artin 标签仍为 \(\sigma=\operatorname{Frob}_{(-1+2i)}\)，
\(\chi(\sigma)=\omega=8+25i\in k=\mathbf F_{43^2}\)。
本文证明
\[
 \boxed{\operatorname{Cl}(F)\otimes\mathbf Z_{43}=0.}
 \tag{264.1}
\]
这里消失的是整个基域 \(F\) 的 43 类群；R163 先前只给出忠实
\(\chi^{\pm1}\) 分量的消失。证明使用实际 Robert 单位、两个小素数上的
有限符号及一个带严格尾界的二次单位恒等式，不使用 PARI 的条件类数。

在同一个大素数 \(q\) 处，结合 R243，完整基域射线群还满足
\[
 \boxed{\operatorname{Cl}_{q\mathcal O_F}(F)[43^\infty]
       \simeq(\mathbf Z/43\mathbf Z)^6.}
 \tag{264.2}
\]
这两条结论都没有求出上层 \(L=FL_q\) 的普通 Norm 原像，也没有求出
R201 的 \(\mathcal L\)。上层射线群的长度问题仍是 R250 的问题，
不能用 (264.2) 代替。

## 1. 两个实际椭圆单位轨道

选择与 R219 相同的实 \(0\ne P\in A[43]\)，令
\(P_j=[-1+2i]^jP\)、\(H_j=\langle P_j\rangle\)，
\(\phi_j:A\to E_j=A/H_j\) 是规范 Vélu 同源。
取 \(P_2=(i,1-i)\)，并用 R198 的准确函数
\[
 \mathcal F_E(Q)=\frac{\Delta_E^{10}}{\psi_{11,E}(Q)}.
\]
定义
\[
 u_j=\prod_{a=1}^{42}\mathcal F_A(P_2+[a]P_j)=\sigma^j u_0,
 \qquad
 R_j=\prod_{a=1}^{42}\mathcal F_A([a]P_j)=\sigma^j R_0.
 \tag{264.3}
\]
二者均在 \(F\) 中，不是形式群环中的未实现符号。R198 的精确同源
Norm 关系给
\[
 R_j=\left(\frac{\Delta_{E_j}}{64}\right)^{10}.
 \tag{264.4}
\]
例如，令 \(Q'\to O\) 于
\(\prod_{\phi_j Q=Q'}\mathcal F_A(Q)=\mathcal F_{E_j}(Q')\)；
因规范同源在原点的参数首项为 \(t'=t\)，消去原点项后，
首项之比正是 (264.4)，没有额外的 \(43^{120}\) 因子。

移位点的导子有 \(2,43\) 两个不同素理想，所以 \(u_j\) 是普通单位。
不移位的 \(R_j\) 只可能在 \(43\) 上有赋值。\(43\) 在 \(F/K\)
全分歧，各共轭 \(R_j\) 在唯一上方素点有相同赋值。因此
\[
 v_j=R_j/R_{j+1},\qquad
 \mathcal R=\prod_{j=0}^{43}R_j^{(-1)^j}
 \tag{264.5}
\]
都是普通单位；后一式的指数和为零。

这里还要核对它们属于可用于类数公式的椭圆单位群，而不只是普通单位。
令 \(P_F\) 为 Oukhaba–Viguié 定义的、由所有 Robert 射线范数及单位根
生成的群，并令 \(E_F^{\rm Rob}=P_F\cap\mathcal O_F^\times\)。
R163/R198 的规范比较说明 \(\mathcal F_A(Q)^{12}\) 是同一
Robert 值的十二次幂。因此
\[
 u_j^{12}\in E_F^{\rm Rob},\quad
 v_j^{12}\in E_F^{\rm Rob},\quad
 \mathcal R^{12}\in E_F^{\rm Rob}.
 \tag{264.6}
\]
对于未移位值，先在导子 \((43)\) 的射线域取范数，再扩到 \(F\)：
若它与 \(F\) 的交域为 \(F'\)，原标量范数是
\(N_{K((43))/F'}\) 的一个整数次幂，因此仍是 \(P_F\) 的生成元的幂。
这不需要把 \(F\) 错认成 \(K((43))\) 的子域。

Oukhaba–Viguié §4、Remark 4.3 给
\[
 C_F\subset E_F^{\rm Rob},\qquad
 (E_F^{\rm Rob})^{44}\subset C_F,
 \tag{264.7}
\]
其中 \(C_F\) 是 Rubin 的椭圆单位群。由于 \(12\) 和 \(44\) 都是
43 进单位，(264.6) 的三个实际单位轨道在 43 进完成后都属于
\(C_F\otimes\mathbf Z_{43}\)。未除以任何零 Euler 因子。

## 2. 42 个非平凡方向的完整有限符号

Dirichlet 单位定理及 \(F/K\) 的复嵌入置换作用给
\[
 (E_F/E_F^{43})\otimes_{\mathbf F_{43}}k
   \simeq\bigoplus_{n=1}^{43} k(\chi^n).
 \tag{264.8}
\]
每条非平凡角色线恰有维数一。这里没有单位根的 43 挠元：
\([F:\mathbf Q]=88\)，不能包含次数 \(42\) 的
\(\mathbf Q(\zeta_{43})\)。

辅助素数和实际点为
\[
\begin{array}{c|c|c}
 \ell&P=(x,y)&\zeta_\ell=e_{43}(P,iP)\\ \hline
 859&(209,591)&510+324i\\
 1031&(808,263)&1002+269i
\end{array}
\tag{264.9}
\]
坐标在 \(\mathbf F_\ell\)，配对在
\(\mathbf F_{\ell^2}=\mathbf F_\ell[i]\)。程序按试除证明两个数为素数，
核查点、阶、Miller 配对、全部 44 个 \([-1+2i]\) 标签，以及
\(P_{44}=[5]P\)。两素数都满足 \(\ell\equiv-1\bmod172\)，
故这些约减确给出 \(F\) 的剩余域为 \(\mathbf F_{\ell^2}\) 的素点。

置
\[
 \ell_{\mathfrak l}(a)=
 \log_{\zeta_\ell}\!\left(\bar a^{(\ell^2-1)/43}\right),\qquad
 S_n(a)=\sum_{j=0}^{43}\omega^{nj}\ell_{\mathfrak l}(\sigma^j a).
 \tag{264.10}
\]
若 \(S_n(a)\ne0\)，则 \(a\) 的 \(\chi^{-n}\) 分量在
\(E_F/E_F^{43}\) 非零；这里明确保留 Fourier 指数的负号。
我们最终覆盖的集合在 \(n\mapsto-n\) 下稳定。

程序从 42 个点的 \(\psi_{11}\) 乘积直接计算 (264.3)，并逐轨道核对
(264.4) 以及 R219 短表达式
\[
 u_j=\left(\frac{2w_j^4}{1-w_j^2}\right)^5,\qquad
 w_j=\frac{z_j-i}{z_j+i}.
 \tag{264.11}
\]
总共核查 \(7392\) 个除法多项式值、\(176\) 条精确标量 Norm 恒等式。
完整值、对数、所有 44 个 Fourier 和都保存于证书，并非只保存秩。

实算结果如下。

| 检测量 | 范围 | 零的角色下标 |
|---|---|---|
| \(S_n(u_0)\)，\(\ell=859\) | 全部奇数 \(n\) | \(11,33\) |
| \(S_n(u_0)\)，\(\ell=1031\) | 全部奇数 \(n\) | 无 |
| \(S_n(R_0)\)，\(\ell=859\) | 非零偶数 \(n\) | \(22\) |

例如第二行的 \(S_{11}(u_0)=25\)。第三行实际使用普通单位
\(v_0=R_0/R_1\)：准确关系为
\[
 S_n(v_0)=(1-\omega^{-n})S_n(R_0).
 \tag{264.12}
\]
非零 \(n\) 时系数可逆。因此所有奇数方向和除 \(22\) 外的所有
非零偶数方向，共 \(42\) 维，都有已经实现的椭圆单位非零类。

辅助素数选择在这里有一个实际限制：这两个素数处的二次实单位约减
落在 \(\mathbf F_\ell^\times\)，其 43 幂剩余符号恒为零。
不能把这条局部零误当成全局单位的 43 可除性。下一节独立解决该方向。

## 3. 二次方向的精确全局恒等式

### 3.1 二次域、正性与整数指数

\(\chi^{22}\) 是 \(F/K\) 的二次角色。
对 \(\alpha=a+bi\bmod43\)，它等于
\[
 \left(\frac{a^2+b^2}{43}\right).
 \tag{264.13}
\]
它杀掉 \(2\) 处的惯性；导子 \((43)\) 的射线群有唯一二次商。
对应域为 \(K(\sqrt{-43})=K(\sqrt{43})\)。
又 \((5/43)=-1\)，所以 (264.13) 在指定 \(-1+2i\) 上确取 \(-1\)。

由 (264.5)，\(\sigma\mathcal R=\mathcal R^{-1}\)，
而复共轭把 \(R_j\) 变成 \(R_{-j}\)，因此
\[
 \mathcal R\in\mathbf Q(\sqrt{43})^\times.
\]
它是普通单位。取实周期 \(\Omega>0\)，使
\(A(\mathbf C)=\mathbf C/\Omega(\mathbf Z+i\mathbf Z)\)，并令
实核为 \(\langle\Omega/43\rangle\)。
其余 43 条核线由 \(\Omega(a+i)/43\)、\(0\le a\le42\) 表示。
复共轭把 \(a\) 与 \(43-a\) 配对；相应判别式比互为共轭，且权重相同。
两条实固定核线的判别式比为正。故
\[
 \mathcal R>0.
 \tag{264.14}
\]

\(\sqrt{43}\) 的连分数为
\[
 [6;\overline{1,1,3,1,5,1,3,1,1,12}].
\]
程序按整数递推核查整个周期及直至首个 Norm 为一的全部收敛分数。
周期长为偶数 \(10\)，故没有 Norm 为 \(-1\) 的单位；正基本单位是
\[
 \epsilon=3482+531\sqrt{43},\qquad 3482^2-43\cdot531^2=1.
\]
标准连分数最小解判据遂说明，存在唯一整数 \(h\) 使
\[
 \mathcal R=\epsilon^h.
 \tag{264.15}
\]
接下来的区间计算只确定这个已知为整数的指数，不是用数值整数关系
猜测一个代数恒等式。

### 3.2 判别式模形式与严格尾界

写
\[
 D(\tau)=e^{2\pi i\tau}
       \prod_{n\ge1}(1-e^{2\pi in\tau})^{24}.
\]
规范同源的格子包含关系给
\[
 \frac{\Delta_{E_{\rm real}}}{\Delta_A}
     =43^{12}\frac{D(43i)}{D(i)},\qquad
 \frac{\Delta_{E_a}}{\Delta_A}
     =\frac{D((a+i)/43)}{D(i)}.
 \tag{264.16}
\]
令 \(s_a=((a^2+1)/43)\)。实核的权重为一，
\(\sum_{a=0}^{42}s_a=-1\)，所以所有分母 \(D(i)\) 抵消：
\[
 \log\mathcal R
 =10\left(
       12\log43+\log|D(43i)|
       +\sum_{a=0}^{42}s_a\log|D((a+i)/43)|
     \right).
 \tag{264.17}
\]
此处的因子 \(10\) 来自 (264.4)，不是 Robert 十二次幂的因子。

在 \(256\) bit 的 Arb 区间运算中，每个级数取 \(N=300\) 项，
并逐次用区间运算核查其有限性。最大展开参数的模满足
\[
 e^{-2\pi/43}<r=87/100.
\]
对任一 \(|q_\tau|\le r\)，
\[
 \left|\sum_{n>N}\log|1-q_\tau^n|\right|
 \le\sum_{n>N}\frac{r^n}{1-r^n}
 \le\frac{r^{N+1}}{(1-r)(1-r^{N+1})}.
\]
因此 (264.17) 的总遗漏项绝对值至多
\[
 T_N=
 44\cdot10\cdot24\,
 \frac{r^{301}}{(1-r)(1-r^{301})}
 < 5.1\cdot10^{-14}.
 \tag{264.18}
\]
程序另以严格区间比较核查此界小于 \(10^{-13}\)。

有限和除以 \(\log\epsilon\) 得到的区间中心为
\[
 -240.000000000000000004647953773251449\ldots,
\]
其区间半径小于 \(7\cdot10^{-47}\)；这是截断有限和的区间，
仍必须加 (264.18)。核验器实际验证
\[
 |\text{有限和}+240\log\epsilon|+T_N
       <\tfrac12\log\epsilon.
\]
结合 (264.15) 的整数性，唯一可能是 \(h=-240\)。因此得到精确等式
\[
 \boxed{\mathcal R=(3482+531\sqrt{43})^{-240}.}
 \tag{264.19}
\]
特别地，\(-240\equiv18\bmod43\) 非零；更准确地
\[
 -2880=1-67\cdot43,\qquad
 [\mathcal R^{12}]=[\epsilon]\quad\text{于 }E_F/E_F^{43}.
 \tag{264.20}
\]
这个类在 \(F\) 中仍非零：若 \(\epsilon=b^{43}\)、\(b\in F\)，
则赋值先迫使 \(b\) 为普通单位；再取
\(N_{F/\mathbf Q(\sqrt{43})}\)，得到
\(\epsilon^{44}=N(b)^{43}\)，与 \(\epsilon\) 为基本单位且
\(43\nmid44\) 矛盾。因此二次方向由一个实际椭圆单位的类准确生成。

这里的正平方根对应上面的复嵌入；换另一实嵌入同时把两边取倒数。
生成性结论不依赖这一选择。

## 4. 从全部单位方向到完整基域类群

令 \(\mathcal C=C_F\otimes\mathbf Z_{43}\)，
\(\mathcal E=E_F\otimes\mathbf Z_{43}\)。它们是
\(\mathbf Z_{43}[\Delta]\) 模；有限生成性及
\(43\nmid44\) 允许逐角色使用 Nakayama。

§2 的实际有限符号证明 \(\mathcal C\to\mathcal E/43\mathcal E\)
在除 \(\chi^{22}\) 外的全部非平凡方向满射。
(264.19)–(264.20) 给最后一个方向。
(264.8) 没有平凡单位方向，于是
\[
 \mathcal C=\mathcal E.
 \tag{264.21}
\]
具体来说，在每条秩一角色线中，一个模 43 非零的实际椭圆单位就是
43 进基。这一步没有将“线性独立”冒称为对整个普通单位群的整基。

有限 Gras 等式（R163 §4 已核条件，或 Oukhaba–Viguié 的完整指数
等式 (1.2)）将 (264.21) 的指数一转成
\[
 \#\operatorname{Cl}(F)[43^\infty]
     =\#\operatorname{Cl}(K)[43^\infty]=1.
\]
基 Hilbert 类域就是 \(K\)，其单位根数为 \(4\)；扩张次数为 \(44\)，
两者都与 \(43\) 互素，故 Rubin 的有限定理可用。
定理没有要求 \(43\) 在 \(K\) 分裂，也没有 ordinary 假设。
这证明 (264.1)，且完全没有使用条件 BNF 类数、条件单位基或 GRH。

## 5. 同一 q 的完整基域射线群

R243 给出了全部普通单位的 43 饱和证明。其全 \(F\) 的 \(q\)
剩余符号映射秩为 \(38\)，单位零方向恰为
\[
 n=1,\ 43,\ 8,\ 36,\ 22.
 \tag{264.22}
\]
该结果不是从本条两个辅助素数推断的，而是 R243 在原大素数 \(q\)
上已实际复算的完整矩阵。

\(q\) 在 \(F/K\) 分成 \(44\) 个素点，
\(v_{43}(q^2-1)=1\)，所以局部乘法群的 43 部分是
\((\mathbf F_{43})^{44}\)，并带有 \(\Delta\) 的正则表示。
用 (264.1) 于通常的单位—射线类群正合列，得到
\[
 \operatorname{Cl}_{q\mathcal O_F}(F)[43^\infty]
   \simeq
 \operatorname{coker}\left(
 E_F/E_F^{43}\longrightarrow
 \bigoplus_{\mathfrak q\mid q}
       \mathbf F_{q^2}^\times/
           (\mathbf F_{q^2}^\times)^{43}
 \right).
 \tag{264.23}
\]
这里没有剩余的普通 43 类群项，也没有可能的 43 平方指数：
左边是一个指数为 \(43\) 的局部群之商。

所以其维数准确为 \(44-38=6\)；扩标到 \(k\) 后，角色为
\[
 \boxed{0,\ 1,\ 43,\ 8,\ 36,\ 22.}
 \tag{264.24}
\]
其中 \(0\) 是单位模本来没有的平凡方向。
这证明 (264.2)。式 (264.24) 只记录 \(\Delta\) 角色；
没有额外声称复共轭在各线上的规范标量。

## 6. 对实际 Norm 工作的准确边界

(264.1) 补足了基域的全部 43 类群信息，(264.23) 则给出原 \(q\)
处整个基域射线群的精确大小与角色。这使任何后续基域
43 主部理想清除都不必再附加未证的类数条件。

但 \(X\in L^\times\)、\(N_{L/F}X=U\) 的实际坐标、普通单位支撑、
以及同一 \(q\) 素点的剩余根仍未产生。
不能由基域类群消失把上层普通单位 Norm 见证写成已求得，
也不能由基域射线群的指数为 \(43\) 推断 R250 的上层射线群指数。
后者仍取决于 \(\rho=\mathcal L+3\)。

若将来采用非普通单位的 Norm 见证，R200 的外支撑正 Artin 修正
仍须保留；本条没有消去该项。R202 继续只留给实际求得的
\(\mathcal L\)。

## 7. 可复算文件、实际执行与来源

文件：

- [verify_r264_full_elliptic_units.py](../scripts/verify_r264_full_elliptic_units.py)
- [verify_r264_quadratic_robert_unit.py](../scripts/verify_r264_quadratic_robert_unit.py)
- [r264_full_elliptic_saturation_certificate.json](../notes/r264_full_elliptic_saturation_certificate.json)

第一部分仅用 Python 标准库及已发表的 R219/R257 核验器。
第二部分用 python-flint 的 Arb 区间算术；它还从整数递推独立核查
Pell 连分数。二者都需执行，第一部分的 PASS 不包含第二部分。

~~~sh
python scripts/verify_r264_full_elliptic_units.py notes/r264_full_elliptic_saturation_certificate.json
python scripts/verify_r264_quadratic_robert_unit.py notes/r264_full_elliptic_saturation_certificate.json
~~~

实际输出分别是：

~~~json
{"status":"PASS","finite_symbol_dimensions_detected":42,"exact_scalar_norm_identities_checked":176,"division_polynomial_evaluations":7392,"quadratic_analytic_section_checked_in_this_run":false,"actual_upper_norm_preimage_computed":false,"actual_L_computed":false}
{"status":"PASS","precision_bits":256,"q_series_terms":300,"certified_quadratic_exponent":-240,"exponent_mod_43":18,"actual_upper_norm_preimage_computed":false,"actual_L_computed":false}
~~~

主要来源和已核输入：

1. [R163](R163-all-prime-primitive-adjoint-robert-generator.md) §4–5：
   有限 Gras 的准确假设及 Robert 范数规范；
   [R198](R198-p-squared-robert-norm-and-a-secondary-contribution.md)：
   精确奇度同源 Norm；
   [R243](R243-complete-unit-norm-kernel-and-43-saturation.md) §6：
   原 \(q\) 的全单位秩 \(38\) 和五个零方向。
2. H. Oukhaba and S. Viguié, *On the Gras Conjecture for Imaginary
   Quadratic Fields*, Canadian Mathematical Bulletin 56 (2013), 148–160，
   [原刊全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf)：
   引言的 Rubin 条件、式 (1.2)、Definition 2.1、§4 的 Robert 范数
   生成元、Remark 4.3。本文已重新读原文相应部分。
3. K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture
   of Birch and Swinnerton-Dyer*, Cetraro notes，
   [全文](https://swc-math.github.io/notes/files/99RubinCM.pdf)，
   Theorem 7.4(iii)：原始挠点 Robert 值的支撑；这也是 R257 已核来源。
4. 判别式格子缩放、连分数 Pell 最小解和射线正合列均在上述证明中
   给出实际使用的形式。浮点近似仅用于显示结果；定理所用比较由
   Arb 区间和显式无穷尾界完成。
