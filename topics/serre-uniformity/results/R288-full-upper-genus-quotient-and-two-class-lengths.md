# R288：实际上层的完整 43 属商与只剩两个类群长度参数

**状态：已证明。** 保留 R171、R191、R264 的同一个
\[
 p=43,\quad K=\mathbf Q(i),\quad
 F=K(A[43])^{\mathbf F_{43}^{\times}},\quad L=FL_q,
 \quad \Delta=C_{44},\quad\Gamma=\langle\gamma\rangle=C_{43}.
\]
\(\Delta\) 与 \(\Gamma\) 在 \(\operatorname{Gal}(L/K)\) 中交换；
\(\gamma\) 仍是 R191/R250 的实际 tame 生成元。写
\[
 A_L=\operatorname{Cl}(L)\otimes\mathbf Z_{43}.
\]
本文从 R264 的完整基域类群消失推出
\[
 \boxed{(A_L)_\Gamma\simeq(A_L)^\Gamma
       \simeq\mathbf F_{43}^{\,5}
       \quad\text{作为 }\mathbf F_{43}[\Delta]\text{ 模，}}
 \tag{288.1}
\]
其非平凡角色准确为 \(\chi^{\pm1},\chi^{\pm8},\chi^{22}\)。
两个同构是存在性同构，并没有把自然映射
\((A_L)^\Gamma\to(A_L)_\Gamma\) 说成同构。

更强地，取 \(\mathcal O=\mathbf Z_{43}[i]\)，
\[
 \mathcal S=\mathcal O[\zeta_{43}],\quad
 \mathcal S_0=\mathbf Z_{43}[\zeta_{43}],\quad
 \varpi=\zeta_{43}-1.
\]
存在唯一两个正整数 \(m_8,m_{22}\) 使
\[
 \boxed{
 A_L\simeq
 (\mathcal O/43)_{\{\pm1\}}\ \oplus\
 (\mathcal S/\varpi^{m_8})_{\{\pm8\}}\ \oplus\
 (\mathcal S_0/\varpi^{m_{22}})_{\{22\}}
 }
 \tag{288.2}
\]
作为 \(\mathbf Z_{43}[\Delta\times\Gamma]\) 模。
在后两项，\(\gamma\) 作用为乘 \(\zeta_{43}\)；
在第一项，\(\Gamma\) 平凡。
下标记录 \(\Delta\) 的不可约 43 进型，不另规定复共轭的半线性标量。

由此整个普通类群的大小被压成
\[
 \boxed{\#A_L=43^{\,2+2m_8+m_{22}}.}
 \tag{288.3}
\]
特别，所有别的 \(\Delta\) 型都消失。忠实型的长度一还可直接由
R171 的 \(\lambda_q=16\ne0\) 和属商重新证明，不需要条件类数。

另有两个完整的下层结论：
\[
 \operatorname{Cl}(L_q)[43^\infty]=0,\qquad
 \operatorname{Cl}_{\{2\}}(L_{11})[43^\infty]=0,
 \tag{288.4}
\]
其中 \(M=F^{\langle\sigma^{11}\rangle}\)、
\(L_{11}=ML_q\)，而 \(\operatorname{Cl}_{\{2\}}\) 表示只反转二上方素点的
普通 \(S\) 类群。第二条比 R257 反转 \(2,43,q\) 的结论更强。

本条没有给出 \(m_8,m_{22}\) 的数值，也没有求出实际普通
Norm 原像或 \(\mathcal L\)。式 (288.2) 描述普通类群；
R250 的忠实上层射线群仍取决于 \(\rho=\mathcal L+3\)。

## 1. 最大 43 属域就是已知的基域 q 射线域

令 \(T/F\) 为模 \(q\mathcal O_F\) 的最大 43 主部射线类域。
R264 已无条件证明
\[
 \operatorname{Gal}(T/F)
  =\operatorname{Cl}_{q\mathcal O_F}(F)[43^\infty]
  \simeq\mathbf F_{43}^{\,6},
 \tag{288.5}
\]
其 \(\Delta\) 角色为
\[
 0,\quad1,\quad43,\quad8,\quad36,\quad22.
 \tag{288.6}
\]
由于 \(L/F\) 的导子整除 \(q\mathcal O_F\)，且次数为 \(43\)，
它包含于 \(T\)。该商的 \(\Delta\) 作用平凡，并且 (288.6) 的平凡
部分恰为一维，所以
\[
 \operatorname{Gal}(T/L)
  \simeq k(\chi)\oplus k(\chi^8)\oplus
        \mathbf F_{43}(\chi^{22})
 \tag{288.7}
\]
作为 \(\mathbf F_{43}[\Delta]\) 模；
这里每个 \(k\) 项合并其两个共轭角色，因而总维数是五。

先证明 \(T/L\) 处处不分歧。
在每个 \(\mathfrak q\mid q\) 处，
\[
 v_{43}(\#\mathbf F_{q^2}^{\times})=1,
\]
故 \(T/F\) 的惯性群的阶至多 \(43\)。
而 \(L/F\) 在该点全分歧且分歧指数为 \(43\)，
所以惯性群映到 \(\operatorname{Gal}(L/F)\) 是同构。
其与 \(\operatorname{Gal}(T/L)\) 的交因此为一。
在其他有限处，\(T/F\) 本来不分歧；\(F,L\) 都无实位置。
于是 \(T/L\) 是一个处处不分歧的阿贝尔 43 扩张。

反向令 \(\mathscr H/L\) 是最大不分歧阿贝尔 43 扩张，
\(\operatorname{Gal}(\mathscr H/L)=A_L\)。
该类域对 \(F\) 是 Galois 的；\(\Gamma\) 对 \(A_L\) 的共轭作用
不依赖提升的选择，因为 \(A_L\) 阿贝尔。
令 \(B\) 是 \(A_L\) 的 \((\gamma-1)\) 像对应的固定域。
于是
\[
 1\longrightarrow(A_L)_\Gamma
 \longrightarrow\operatorname{Gal}(B/F)
 \longrightarrow\Gamma\longrightarrow1.
 \tag{288.8}
\]
核在整个群中中心化。中心阿贝尔核按一个循环商扩张后仍是阿贝尔群：
选一个商生成元的提升，整个群由这个提升及中心核生成，
所以所有生成元两两交换。

因此 \(B/F\) 是阿贝尔 43 扩张。它在 \(q\) 外不分歧；
在 \(q\) 处，因 \(B/L\) 不分歧，分歧指数仍是 \(43\)，
且 \(q\ne43\)，故温和，其阿贝尔局部导子指数至多一。
所以 \(B\subseteq T\)。

前一段的 \(T/L\) 不分歧及 \(T/F\) 阿贝尔又给 \(T\subseteq B\)。
从而
\[
 \boxed{B=T,\qquad (A_L)_\Gamma=\operatorname{Gal}(T/L).}
 \tag{288.9}
\]
这证明了属商的一般性与精确大小，不是只从一个显式不分歧扩张
得到一个大小为 \(43^5\) 的下界。

## 2. 类群 Norm 被零基域杀掉

理想类的 Norm 与扩张满足
\[
 \operatorname{ext}_{F}^{L}\circ N_{L/F}
     =1+\gamma+\cdots+\gamma^{42}
     =N_\Gamma.
\]
R264 给 \(\operatorname{Cl}(F)[43^\infty]=0\)，因此
\[
 \boxed{N_\Gamma A_L=0.}
 \tag{288.10}
\]
故 \(A_L\) 是有限
\[
 \mathbf Z_{43}[\Gamma]/(N_\Gamma)
       \simeq\mathbf Z_{43}[\zeta_{43}]
       =\mathcal S_0
 \tag{288.11}
\]
模，\(\gamma-1\) 对应 \(\varpi\)。
这是实际 \(\Gamma\) 作用的整关系，不只是模 \(43\) 的关系。

\(\mathcal S_0\) 是完全分歧次数 \(42\) 的离散赋值环，
均匀化元为 \(\varpi\)，剩余域为 \(\mathbf F_{43}\)，并有
\(43=u\varpi^{42}\)（\(u\) 为单位）。

由于 \(43\nmid44\)，\(\mathbf Z_{43}[\Delta]\) 半局部分解。
在 \(43\) 模 \(44\) 等于 \(-1\) 的条件下，
除平凡及二次角色外，每个不可约型是一对 \(\{n,-n\}\)，
系数环为未分歧二次环 \(\mathcal O\)。
扩标后其对应环就是 \(\mathcal S=\mathcal O[\zeta_{43}]\)，
剩余域为 \(k\)。

由 (288.7)、(288.9)，每个实际出现的型满足
\[
 \dim_k A_{\{\pm1\}}/\varpi A_{\{\pm1\}}=1,\qquad
 \dim_k A_{\{\pm8\}}/\varpi A_{\{\pm8\}}=1,
\]
二次型的剩余维数为一，其余型的剩余维数为零。
Nakayama 引理及 DVR 上有限模分类立即给
\[
 A_{\{\pm1\}}\simeq\mathcal S/\varpi^{m_1},\quad
 A_{\{\pm8\}}\simeq\mathcal S/\varpi^{m_8},\quad
 A_{\{22\}}\simeq\mathcal S_0/\varpi^{m_{22}},
 \tag{288.12}
\]
其中三个长度都至少一，别的型全部为零。
这里“每型循环”来自一维的准确属商，不是从普通单位的抽象自由性
推断类群长度。

在任一 \(\mathcal S/\varpi^m\) 中，
\[
 \ker(\gamma-1)=\varpi^{m-1}\mathcal S/\varpi^m,\qquad
 A/(\gamma-1)A=\mathcal S/\varpi.
 \tag{288.13}
\]
所以不变量也是每型一个剩余方向，且指数为 \(43\)。
这证明 (288.1) 中的不变量描述。尤其自然映射
\[
 A^\Gamma\longrightarrow A_\Gamma
 \tag{288.14}
\]
在该型上非零当且仅当 \(m=1\)；
当 \(m>1\) 时，它是零映射。

## 3. 实际 q 素理想迫忠实长度 m1=1

每个 \(L\) 中 \(q\) 上方的素理想都被 \(\Gamma\) 固定，
因为 \(L/F\) 在 \(q\) 全分歧。
所以这些素理想的类属于 \(A_L^\Gamma\)。

在属商 (288.9) 中，它们的像就是
\(T/L\) 的实际不分歧 Frobenius。
R171、R201 §2 对同一个 \(q\) 素点和同一个 \(L_q\) 的限制计算给：
原严格 \(W=\chi^{\pm1}\) 类的有限、奇异坐标满足
\[
 a=\lambda_qb,\qquad\lambda_q=16,
\]
限制到 \(L\) 后奇异坐标被杀掉，有限坐标仍为
\[
 2a=32b\ne0.
 \tag{288.15}
\]
非零 \(b\) 是该射线类的生成选择。这是 R201 已检查的实际局部限制；
没有任意更换 Frobenius 提升、用另一个 tame 方向重定义有限坐标。

因此某个 \(\Gamma\) 固定的 \(q\) 理想类在忠实属商中非零。
由 (288.14) 的准确 DVR 描述，只能有
\[
 \boxed{m_1=1.}
 \tag{288.16}
\]
这给出 R210 普通忠实类群结论的一个新的完整证明：
\[
 A_{\{\pm1\}}\simeq\mathcal O/43,
 \qquad\Gamma\text{ 作用平凡}.
\]
它只使用基域完整类群消失、最大属域识别以及同一个实际
\(\lambda_q=16\)；不假定上层单位或上层射线群已经求值。

把 (288.16) 代回 (288.12)，即得 (288.2)–(288.3)。

## 4. 两个下层类群的完整推论

### 4.1 纯 q 射线扩张本身没有 43 类群

\(L/L_q\) 的次数为 \(44\)，与 \(43\) 互素。
理想类扩张映射在 43 主部上单射，像落于
\(A_L^\Delta\)。而 (288.2) 没有平凡 \(\Delta\) 型，所以
\[
 \operatorname{Cl}(L_q)[43^\infty]=0.
 \tag{288.17}
\]
这里直接用 \(\operatorname{Norm}\circ\operatorname{ext}=44\)
核查单射，不假定任意整类群都在扩张中单射。

### 4.2 十一次层的整个类群由二上方素理想生成

令 \(M=F^{\langle\sigma^{11}\rangle}\)，\(L_{11}=ML_q\)。
则 \([L:L_{11}]=4\)。43 主部的扩张与 Norm 给
\[
 \operatorname{Cl}(L_{11})[43^\infty]
       \simeq A_L^{\langle\sigma^{11}\rangle}.
 \tag{288.18}
\]
满射到不变量也可直接核查：
对不变类 \(a\)，\(\operatorname{ext}N(a)=4a\)，
而四在 43 主部上可逆。
(288.2) 中只有 \(\{\pm8\}\) 被 \(\sigma^{11}\) 固定。因此
\[
 \boxed{
 \operatorname{Cl}(L_{11})[43^\infty]
       \simeq\mathcal S/\varpi^{m_8}.
 }
 \tag{288.19}
\]
这是整个 43 类群，其余八个非平凡次数十一角色及平凡型都已消失。

R257 在同一个 \(M\) 与同一个 \(q\) 的射线群中，
用完整的普通素数二生成元
\((g_2)_M=\mathfrak P_2^{\,2}\)
计算了 \(\chi^8\) 主射线坐标，准确得到
\[
 \operatorname{Frob}_{\mathfrak P_2}=-i\,b_0\ne0.
 \tag{288.20}
\]
它不是截断有理系数后的旧试算值。
\(2\) 在 \(L_q/K\) 完全分裂，所以提升到 \(L_{11}\) 后，
(288.20) 仍是其类在 \(\Gamma\) 属商中的非零像。
次数四的基变换只带来可逆因子，不会杀掉此像。

记 \(D_2\) 为 \(\operatorname{Cl}(L_{11})[43^\infty]\)
中由所有二上方素理想类生成的子模。它对 \(\Delta,\Gamma\) 稳定；
(288.20) 表明它满射到唯一非零型的
\(A/\varpi A\simeq k\)。
因此对 \(A/D_2\) 使用 Nakayama，得到
\[
 D_2=A,\qquad
 \boxed{\operatorname{Cl}_{\{2\}}(L_{11})[43^\infty]=0.}
 \tag{288.21}
\]
证明不需要另外反转 \(43\) 或 \(q\)，也不需要知道 \(m_8\)。

一个准确的 Norm 存在性推论是：R257 的普通实目标 \(V_8\)
可以选择一个普通 \(\{2\}\) 单位原像于 \(L_{11}\)，且通过次数二的
取实与普通单位修正，可选于相应实固定域。
做法是循环 Hasse Norm 后，仅在二以外的除子上使用 (288.21)
及 R201 的清支撑论证；模 \(43\) 之外的分量用底域 43 次幂补齐。
若所得普通原像为 \(X\)，则
\(Y=(X\tau X)^{22}/V_8\) 是实的普通 \(\{2\}\) 单位，且
\(N_{L_{11}/M}Y=V_8^{44}/V_8^{43}=V_8\)。
这仍只是存在性，本条没有输出该原像；\(V_8\) 在适当真子域中，
它也不是原忠实 \(\chi^1\) 的 Norm 见证。

## 5. 保留的未知量与射线边界

由 (288.2) 可准确写出普通类群的 43 指数：
\[
 \exp(A_L)=43^{
    \max\{1,\lceil m_8/42\rceil,\lceil m_{22}/42\rceil\}}.
 \tag{288.22}
\]
整个 \(\Gamma\) 作用平凡当且仅当 \(m_8=m_{22}=1\)；
仅知道不变量和属商的阶都为 \(43^5\)，不能推出这两个长度为一。

这些未知长度属于另外两个普通类群型。它们不能代替忠实上层
射线量 \(\rho\)。即使普通忠实类群已确定为 \(\mathcal O/43\)，
R250 的射线群仍可有长度一或二；区分两种情况仍需要实际普通单位
Norm 原像的规范剩余值 \(\mathcal L\)。

因此本条没有把最大属域的显式确定或类群模的分类
冒作 \(N_{L/F}X=U\) 的具体解。非普通见证的外支撑 Artin 修正
也仍按 R200 保留。

## 6. 输入与来源

本条是结构证明，没有新增条件类数或待执行的枚举。

- [R264](R264-full-base-class-vanishing-and-quadratic-robert-unit.md)：
  完整基域 43 类群为零，原 \(q\) 射线群的六个角色和指数 \(43\)。
- [R171](R171-principal-norm-selflocal-tate-slope.md)、
  [R201](R201-s-class-vanishing-and-the-canonical-norm-residue.md) §2：
  \(\lambda_q=16\) 以及在同一 \(L_q\) 上的准确局部限制。
- [R257](R257-degree-eleven-units-and-the-role-of-two.md)：
  完整有理坐标的 \(g_2\)、正 Artin 射线坐标 \(-i\)，
  二在 \(L_q/K\) 分裂及普通目标 \(V_8\)。
- [R250](R250-ray-class-exponent-and-nontrivial-gamma-action.md)：
  忠实上层射线群与 \(\rho\) 的关系；本条没有替代该未知量。
- 全局类域论的理想类 Artin 同构、射线导子判据及
  Norm—扩张相容性，使用与 R201/R250 相同的
  J. S. Milne, *Class Field Theory*，
  [讲义](https://www.jmilne.org/math/CourseNotes/CFT.pdf)。
  所需的最大属域识别和局部惯性论证已在 §1 完整给出。
