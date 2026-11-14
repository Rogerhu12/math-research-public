# R356：原 Gaussian 连接的规范有理原函数与全部测试极的零值

日期：2026-11-13。**状态：以下原 \(\zeta\) 连接在实际窗口内的有理比较、唯一 \(p\) 次共振的准确归一、全部非原点测试极的零值和低阶 jets，以及同一个原除幂目标中的 Gaussian 补偿项均已证明。还给出特征零提升的准确首整商，保留真正第二 Bockstein 所需的下一位。没有将整个 theta frame 称为有理函数，也没有将一个模 \(p\) 比较升级为模 \(p^2\) 的免费原像。**

## 1. 固定原规范与 Cartier 常数

取
\[
p=6s-1,\quad s>13,\quad b=17,\qquad
E_b:y^2=x^3+b,\quad D=D_z,\quad
Dx=2y,\quad Dy=3x^2,\quad D\zeta=-x.
\]
仍在 R338、R342、R351 的原惰性整环 \(\mathcal O\) 上工作，剩余域记为 \(k\)；
可在不改变整性或秩的有限非分歧扩张后包含 \(\mu_6\)。
在原点
\[
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
\zeta=z^{-1}+\cdots,\quad w=z^6,\quad t=-b/x^3.
\]

本篇先明确采用 sigma 规范
\[
\kappa_\sigma=34[z^{p+1}]\log(\sigma/z),\quad
a_\sigma=p\kappa_\sigma,\qquad
\zeta_\sigma=\zeta-\frac{(p+1)\kappa_\sigma}{34}z^p .
\tag{1}
\]
准确有
\[
[z^p]\zeta=\frac{(p+1)\kappa_\sigma}{34},
\]
所以 \([z^p]\zeta_\sigma=0\) 是特征零的等式，不只是模 \(p\) 归一。

置
\[
n_0=(p-1)/2=3s-1,\qquad
c_p=\binom{3s-1}{2s-1}b^s\in k^\times.
\tag{2}
\]
在 \(E_b/k\) 上，Cartier 的直接多项式公式给
\[
\boxed{\mathcal C(dz)=0,\qquad \mathcal C(x\,dz)=c_p\,dz.}
\tag{3}
\]
确实，
\(dz=dx/(2y)= (x^3+b)^{n_0}dx/(2y^p)\)。
第一式没有 \(x^{p-1}\) 项；第二式的唯一相应项是
\(x\cdot x^{3(2s-1)}=x^{p-1}\)，系数恰为 (2)。
所有显示二项式的阶乘小于 \(p\)，故 \(c_p\ne0\)。

若 \(x_s=[z^{p-1}]x\)，形式原点的 (3) 给
\(\bar x_s=c_p\)。由 \(\zeta'=-x\) 又准确有
\[
\frac{a_\sigma}{34}=-\frac{x_s}{p+1},
\qquad
\boxed{\overline{a_\sigma/34}=-c_p.}
\tag{4}
\]
所以
\[
D\zeta_\sigma=-x-\frac{(p+1)a_\sigma}{34}z^{p-1}
\equiv-x+c_pz^{p-1}\pmod p.
\tag{5}
\]
这里没有把普通或另一 CM 型的 Hasse 常数搬入本惰性支。

## 2. 真正有理参数和显式有限原函数

采用 R342 的实际多项式
\[
\mathscr R_p(x)=\frac12\sum_{j=0}^{n_0}
\binom{n_0}{j}b^{n_0-j}\frac{x^{3j+1}}{3j+1},
\qquad
\widetilde Z=\mathscr R_p(x)/y^p .
\tag{6}
\]
这些分母都是 \(p\) 单位。R342 已证明
\[
D\widetilde Z=1-3p\,\frac{x^2\mathscr R_p(x)}{y^{p+1}},
\qquad
Z:=\overline{\widetilde Z},\quad DZ=1,
\quad Z\equiv z\pmod{p,u^{5p}},\quad u=x^{-1/2}.
\tag{7}
\]
最后的比较只在实际已付局部窗口内使用。

因为 \(DZ=1\)，扩张 \(k(E_b)/k(Z)\) 可分。
\(D^p\) 是杀掉 \(k(Z)\) 的 \(k\)-导子，故
\[
\boxed{D^p=0\quad\text{于 }k(E_b).}
\tag{8}
\]
又 (3) 等价于
\[
D^{p-1}(-x)=c_p.
\tag{9}
\]
例如按 \(1,Z,\ldots,Z^{p-1}\) 作 \(k(E_b)^p\)-基，
Cartier 读取 \(Z^{p-1}dZ\) 的系数，而
\(D^{p-1}Z^{p-1}=(p-1)!=-1\)，立即得到 (9)。

定义真正的有限有理函数
\[
\boxed{
G_\sigma
=\sum_{i=0}^{p-2}
 \frac{(-1)^i Z^{i+1}D^i(-x)}{(i+1)!}\ \in k(E_b).
}
\tag{10}
\]
所有阶乘是单位。逐项求导并相消中间项，Wilson 等式给
\[
\boxed{DG_\sigma=-x+c_pZ^{p-1}.}
\tag{11}
\]
这是整个原函数域中的等式，不仅是原点形式解。

更明确地，对任意 \(f\in k(E_b)\)，同一个有限和满足
\[
D\left(\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^if}{(i+1)!}\right)
=f+Z^{p-1}D^{p-1}f.
\]
因此 (10) 没有用一个未指定的“Cartier 为零所以存在原函数”
来掩盖 \(p\) 次幂自由度。

## 3. 原点共振完全支付

**定理1。** 在原实际整性窗口中，
\[
\boxed{\zeta_\sigma\equiv G_\sigma
\pmod{p,z^{5p-2}}.}
\tag{12}
\]
特别它覆盖 R351 所用的全部长度 \(T+1\le3s\) 的原目标。

**证明。** 首先，\(D^i(-x)\) 在 \(O\) 至多有 \(i+2\) 阶极，
而 \(Z\) 在 \(O\) 有一阶零。因此 (10) 每一项在 \(O\) 至多有一阶极。
在模 \(p\) 的原局部参数中，\(Z=z+\cdots\)，且
\[
D^i(-x)=-(-1)^i(i+1)!\,z^{-i-2}+\cdots.
\]
所以每项的主部均为 \(-z^{-1}\)。
模 \(p\) 的总主部为 \(-(p-1)z^{-1}=z^{-1}\)。
所以没有需要另行消掉的负 \(p\) 次幂极。

R342 的椭圆对数比较保证 \(x\) 在所需的
\(z^{5p-3}\) 之前具有整系数。
积分 \(\zeta'=-x\) 时，此范围内唯一可能被 \(p\) 整除的
\(\mu_6\) 型分母是 \(z^p\) 项；(1) 已准确除去它。
故 (12) 的两边在所述 Laurent 窗口都可以约化。

由 (7)，在 (10) 中将 \(Z\) 换成 \(z\)，造成的误差至少为
\(z^{5p-2}\)：第 \(i\) 项的误差阶至少是
\(5p+i-(i+2)\)。
因此其 \(z^p\) 系数准确为
\[
[z^p]G_\sigma
=-\bar x_s
\sum_{i=0}^{p-2}\frac{(-1)^i}{i+1}\binom{p-1}{i}
=-\bar x_s\sum_{j=1}^{p-1}\frac1j=0 .
\tag{13}
\]
最后的和由 \(j\) 与 \(p-j\) 配对为零。
这与原 \(\zeta_\sigma\) 的准确零共振一致。

在同一窗口，(5)、(7)、(11) 使两者差的导数为零。
原 \(\mu_6\) 作用下 \(Z\) 的型为 \(+1\)，
\(G_\sigma\) 和 \(\zeta_\sigma\) 的型均为 \(-1\)。
导数为零的局部差只含 \(z^{mp}\)；
型条件要求 \(mp\equiv-1\pmod6\)，即 \(m\equiv1\pmod6\)。
除已由 (13) 消去的 \(z^p\) 外，下一个可能共振是 \(z^{7p}\)，
超出窗口。主部已相同，故得 (12)。\(\square\)

这里真正支付了原函数的选择。
只从 (11) 的导数相等而不核 (13)，不足以得到 (12)。

## 4. Gaussian 重标仍保全部测试极的零值

若沿 R342 使用
\[
\kappa=\kappa_\sigma+\Delta,\quad \Delta\in\mathcal O,\qquad
a_\kappa=p\kappa,\quad
g_\kappa=e^{-\Delta w^s}g_\sigma,
\]
则整个原有限矩阵不变。
完整 Newton 函数也仍由 R342 的全权证明给出
\[
J_\kappa(u)=(\kappa_\sigma/\kappa)^uJ_{\kappa_\sigma}(u).
\tag{14}
\]
原 \(S(0)=0\)，故中央导数不变；没有只从有限 \(\Gamma\) 推出 (14)。

定义
\[
\delta_\kappa=\frac{(p+1)\Delta}{34},\qquad
\zeta_\kappa=\zeta-\frac{(p+1)\kappa}{34}z^p,
\qquad
\boxed{G_\kappa=G_\sigma-\bar\delta_\kappa Z^p.}
\tag{15}
\]
这个准确的 \(p\) 次幂修正给
\[
\boxed{\zeta_\kappa\equiv G_\kappa\pmod{p,z^{5p-2}}.}
\tag{16}
\]
它不是重新选择一个任意有利的原 theta；\(\Delta\) 与 \(g_\kappa,a_\kappa\)
始终按同一原 Gaussian 重分解一起移动。

令 \(\mathcal P_p\) 为 R346 中全部非原点、非无穷的实际测试点；
等价地，在 \(E_b\) 上取 \(Z=0\) 且 \(x,y\) 为单位的点。
这些零均简单，且 \(Z\) 是其实际局部参数。
由 (10)、(15)，
\[
\boxed{G_\kappa(P)=0\quad(P\in\mathcal P_p).}
\tag{17}
\]
任意 \(\kappa\) 的整重标都保持 (17)，因为新增项仍含 \(Z^p\)。

更强地，在这样的点用局部参数 \(Z\)，有全部已付低阶 jets
\[
\boxed{
G_\kappa
=-\sum_{j=1}^{p-1}\frac{D^{j-1}x(P)}{j!}Z^j
\pmod{Z^p}.
}
\tag{18}
\]
证明是 (11) 的局部积分及 \(G_\kappa(P)=0\)；
\(c_pZ^{p-1}\) 只在下一共振阶参与，不能删去后用到 \(p\) 阶之外。
(18) 覆盖 R346 的全部 \(6K<p\) 极部。

## 5. 固定坏点处的全局极与实际角向因子

\(D^ix\) 是 \(x,y\) 的多项式。
所以 (10) 除 \(O\) 与三个非零二挠点外没有极；
在二挠点的极阶至多 \(p(p-1)\)。
(15) 另加的 \(Z^p\) 也只在这些固定点有极，极阶至多 \(p^2\)。
这些真实的 \(p\) 依赖极没有从原来源预算中免费删除。

令
\[
\boxed{r_{\kappa,p}=(x/y)G_\kappa.}
\tag{19}
\]
它是 \(\mu_6\)-不变的真正有理函数，所以属于 \(k(t)\)。
在 \(O\)，\(x/y=-z+\cdots\)，故
\[
r_{\kappa,p}(0)=-1.
\]
它在 \(x=0\) 无极；仅可能在二挠像 \(t=1\) 有极。
因此可写为
\[
r_{\kappa,p}(t)=\frac{N_{\kappa,p}(t)}{(1-t)^M},
\qquad \deg N_{\kappa,p}\le M,
\tag{20}
\]
例如可统一取 \(M=(p^2+1)/2\)。
sigma 规范可取较小的 \(M=p(p-1)/2\)。
这些界由二挠点到 \(t\) 线的分歧阶二及上述真实极阶得到。

沿 R346，令
\[
B_p(\xi)=\sum_{j=0}^{n_0}
\binom{n_0}{j}\frac{\xi^j}{6j+1}.
\]
该多项式平方自由，且 \(B_p(0)B_p(-1)\ne0\)。
原测试点在 \(t\) 线准确是 \(B_p(-t)=0\)。
由 (17)、\(x/y\) 在这些点为单位，得到真正的角向因子
\[
\boxed{B_p(-t)\mid N_{\kappa,p}(t).}
\tag{21}
\]
分母 \(1-t\) 与 \(B_p(-t)\) 互素。
(21) 属于同一个固定曲线的真实有理函数，不是一个选择的环境曲线。

其次数可能为 \(O(p^2)\)。
因此不能把 (19) 直接宣布为原小次数归一化或导子乘子；
下面只在已付目标和实际局部极部中使用它。

此外，(19) 的极界只描述这一指定连接系数。
乘回原共同 \(G_0\) 及目标单位 \(U_0\) 时，
R351 的完整伴随仍包含 \(D\log U_0\)；
R335 的 \(P_{134}\) 零及原二、六、七挠因子必须一并保留。
不能用 \(r_{\kappa,p}\) 只在 \(t=1\) 有极，删去这些原 frame 的其他坏点。

## 6. 同一个原 \(\Gamma\) 中的 Gaussian 项必须保留

沿 R351 用
\[
W_{\rm phys}=\rho^2a\chi,\quad B=W_{\rm phys}\nu,\quad
\mathcal Z=W_{\rm phys}\frac{x\zeta}{y},\quad
\mathcal D_\zeta=\mathcal Q+A\mathcal E.
\]
R351 的整个原来源恒等式为
\[
M_+\mathcal D_\zeta
=B(\mathsf E-13)M_-+\frac{17}{3}\mathcal Z M_-\mathcal E.
\tag{22}
\]

置
\(r_\kappa^{\rm for}=(x/y)\zeta_\kappa\)。
由 \(\nu=-x/(yz)\)、\(w^s=p\epsilon\)，准确有
\[
\boxed{
\mathcal Z
=W_{\rm phys}r_\kappa^{\rm for}
-\frac{(p+1)a_\kappa}{34}B\epsilon.
}
\tag{23}
\]
这项 Gaussian 补偿不是一个可以先删掉的高阶误差。
(16) 乘 \(x/y\) 给
\[
r_\kappa^{\rm for}(w)
\equiv r_{\kappa,p}(t(w))\pmod{p,w^{5s-1}}.
\]
原目标 \(T+1\le3s\) 完全处于该窗口。因此
\[
\boxed{
\bar{\mathcal Z}
=\bar W_{\rm phys}\,r_{\kappa,p}(\bar t)
-\frac{(p+1)\bar a_\kappa}{34}\bar B\epsilon
}
\tag{24}
\]
是同一个原除幂目标中的等式。
它保留原 charge40、十三行以及多一行的全部成本。

对任意原首核 \(\bar P\in K_1(M_-)\)，
R351 已证明 \(\epsilon\bar M_-(\mathcal E\bar P)=0\)，
无需令 \(\mathcal E\bar P\) 也在核中。
因此 (22)、(24) 给具体的原像成员性
\[
\boxed{
\bar W_{\rm phys}r_{\kappa,p}(\bar t)\,
 \bar M_-(\mathcal E\bar P)
=\frac3{17}\bar M_+(\mathcal D_\zeta\bar P)
\in\operatorname{im}\bar M_+.
}
\tag{25}
\]
这把 (21) 的真实测试极因子接到了原矩阵。
它尚未说明 R346 的每一个 \(q_n(\lambda,P)\) 极部消失；
两边的整左核、接触尾和目标边界仍按 R351 参与。

## 7. 特征零提升及真正下一整商

为了不将 (25) 偷升为模 \(p^2\) 结论，给一个完全指定的整提升。
仍用 (6) 的原 \(\widetilde Z\)，定义
\[
\widetilde G_\sigma=
\sum_{i=0}^{p-2}
 \frac{(-1)^i\widetilde Z^{i+1}D^i(-x)}{(i+1)!},
\quad
\widetilde G_\kappa=\widetilde G_\sigma-\delta_\kappa\widetilde Z^p,
\quad
\widetilde r_\kappa=(x/y)\widetilde G_\kappa.
\tag{26}
\]
这是实际特征零有理函数，所有系数分母为 \(p\) 单位。
这里必须保留原 \(\widetilde Z\) 的真实特征零线性系数：
\[
\lambda_{\rm lin}=[z]\widetilde Z=\frac1{1-3p},\qquad
c_{\rm lin}=\sum_{j=1}^{p-1}\lambda_{\rm lin}^{\,j}.
\]
由每项主部直接得到
\[
\widetilde G_\sigma=-c_{\rm lin}z^{-1}+\cdots,\qquad
\widetilde r_\kappa(0)=c_{\rm lin}.
\]
只有模 \(p\) 时 \(\lambda_{\rm lin}=1\)；
不能在特征零把主部写成 \((1-p)/z\)。
准确有
\[
c_{\rm lin}+1\equiv p\pmod{p^2},\qquad
\eta_{\rm lin}:=(c_{\rm lin}+1)/p\in1+p\mathcal O,
\]
因为
\(\lambda_{\rm lin}^{\,j}\equiv1+3pj\pmod{p^2}\)。

取准确首项归一
\[
\boxed{
\widetilde r_\kappa^\circ
=\widetilde r_\kappa-(c_{\rm lin}+1)
=\widetilde r_\kappa-p\eta_{\rm lin},\qquad
\mathcal A_\kappa=
\frac{r_\kappa^{\rm for}-\widetilde r_\kappa^\circ}{p}
\in w\mathcal O[[w]] .
}
\tag{27}
\]
于整个已付窗口中。
整性由 (16) 保证；两边常数都准确为 \(-1\)，所以商的常数准确为零。
这只是固定有理提升的原常数调整，并未把余下
\(\mathcal A_\kappa\) 置为零。

(23) 现在给精确的下一位分解
\[
\boxed{
\mathcal Z=W_{\rm phys}\widetilde r_\kappa^\circ
-\frac{(p+1)a_\kappa}{34}B\epsilon
+pW_{\rm phys}\mathcal A_\kappa.
}
\tag{28}
\]
对 R351 的真正两侧模 \(p^2\) 核提升
\[
M_-P_2=0\bmod p^2,\qquad \lambda_2M_+=0\bmod p^2,
\]
(22)、(28) 和 R338 的
\(\epsilon M_-(\mathcal EP_2)/p\equiv-\bar m_{13}\mathcal D(P)\)
给
\[
\boxed{
\overline{\frac1p
 \langle\lambda_2,W_{\rm phys}\widetilde r_\kappa^\circ
                    M_-(\mathcal EP_2)\rangle}
+\lambda_0\!\left(\bar W_{\rm phys}\bar{\mathcal A}_\kappa
                    \bar M_-(\mathcal E\bar P)\right)
=-\frac{(p+1)\bar a_\kappa}{34}
 \lambda_0\!\left(\bar B\,\bar m_{13}\mathcal D(P)\right).
}
\tag{29}
\]
第一项的整除性由 (25) 及实际左核保证。
整个组合来自准确整恒等式，不能把其中一个首商或
\(\mathcal A_\kappa\) 单独删去。
将 \(\widetilde r_\kappa\) 改为
\(\widetilde r_\kappa-(c_{\rm lin}+1)\)
不改变配对：其差是该固定整常数乘真正来源 \(W\mathcal EP\)，
\(\lambda_2W_{\rm phys}M_-(\mathcal EP)=\lambda_2M_+(W\mathcal EP)=0\pmod{p^2}\)。

这个首整商也有直接可继续计算的原微分式。
令 \(f=-x\) 及
\[
\widetilde H_f=\sum_{i=0}^{p-2}
 \frac{(-1)^i\widetilde Z^iD^if}{i!},\qquad
E_p=3x^2\mathscr R_p(x)/y^{p+1}.
\]
特征零逐项相消准确给
\[
\boxed{
D\widetilde G_\sigma
=f-\frac{\widetilde Z^{p-1}D^{p-1}f}{(p-1)!}
-pE_p\widetilde H_f .
}
\tag{30}
\]
所以 (27) 的未付下一位有明确的有理 defect 和原形式 \(z\) 的比较，
不是任意可变的提升参数。
本篇保留它；若后续需要第二 Bockstein 的实际极部，
必须将 (29)、(30) 与 R351 的整左核一起使用。

## 8. 结论的准确使用范围

本篇把原 Gaussian 正则化的 \(\zeta\) 连接实际识别为 (10)、(15)，
支付了唯一 \(z^p\) 共振，并得到全部指定测试极的真实零值与 (18)。
它给 R351 原来源伴随的具体局部连接数据，
同时通过 (25) 接入原整评价矩阵。

它没有把原 \(\rho\) 或完整 theta 来源等同于一个有理函数；
也没有将 (18) 超出 \(p\) 阶共振后继续使用。
原中央失败仍只给已付的
\(a_\kappa c_1-pc_2\equiv0\pmod{p^2}\) 聚合；
新来源的中央零没有增加。

证明使用 R342 的原有理参数和全 Gaussian 重标，
R346 的真实测试极，R351/R352 的完整来源算子及整目标。
本篇全为参数证明，没有扫描目标素数。
文件由已授权的 GitHub API 保存；核心同步记录由根代理维护。


### 特征零首项更正

2026-11-13：初版第7节把 \([z]\widetilde Z\) 误作精确的一，
现按 (6) 改为 \(1/(1-3p)\)，并用完整 \(c_{\rm lin}+1\) 归一。
模 \(p\) 的主定理、所有测试极零值及低阶 jets 不变；
(29) 的完整模 \(p^2\) 结构不变，(27) 现给精确常数为零的整提升。
