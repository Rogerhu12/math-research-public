# R676 — 原近自同构 CM 分子的单位逆与三位真实提升

日期：2026-11-15。**状态：已证明。**

本篇保 R673 的同一个原 sigma 和 canonical Gaussian，改用一个明确的
prime-to-p 原 CM 乘法分子。它在原有限窗口中给一个整单位算子，
从而只需该分子模 p³ 即可恢复原 Θ 的模 p² 规范化来源。
全部原 S/T/U 的读取、H 的 Jacobian 及中央除商保持。

这里没有把恢复出的高位当成可选参数，也没有证明指定中央非零。
末节另付首个 p 挠边界上的准确代数数对数身份；它不把内盘逆搬过边界。

## 1. 同一原有限环和实际 CM 同态

保持
\[
p=6s-1>101,\quad d=p+1,\quad b=17,\quad
K=\mathbf Q_p(\omega),\quad\omega^2+\omega+1=0,
\]
\[
u=x^{-1/2}=z+O(z^7),\quad t=bu^6,\quad
C=(1+t)^{-1/2},\quad
H=\sum_{n\ge0}\frac{C_n}{6n+1}t^n,\quad z=uH.
\]
与 R673 一样先在
\[
R=\mathcal O[t]/(t^p),\qquad I=tR
\tag{1}
\]
中工作。H 的整个显示窗口整，有限 exp/log 的分母也都是单位。

取原全局 CM 整数
\[
a=p+\omega,\qquad
\boxed{\alpha=\omega a=\omega^2+p\omega,\qquad
\nu=\alpha\bar\alpha=p^2-p+1.}
\tag{2}
\]
因 p 为奇数，\(\alpha\equiv\omega^2+\omega=-1\equiv1\pmod2\)。
而 \(\nu\) 为正奇数且 \(\nu\equiv1\pmod p\)。
故 R639 已付的原 CM sigma 乘法式可直接用于这个 α，
包括原半特征号；没有另加二次 Gaussian。

单位 ω 不改变六次变量，且
\[
\alpha^{6n}=a^{6n},\qquad \alpha^d=a^d .
\tag{3}
\]
因此以下分子也可看作 p+ω 对应的 Θ 分子，但所有规范用 (2) 固定。

令
\[
\psi_\alpha(x)=
\alpha\prod_{T\in(\ker[\alpha]\setminus0)/\{\pm1\}}(x-x(T)).
\]
原 R639 的身份准确为
\[
\sigma(\alpha z)=\psi_\alpha(x(z))\sigma(z)^\nu.
\tag{4}
\]
定义
\[
\phi_\alpha(x)=x([\alpha]P)\psi_\alpha(x)^2,\qquad
\boxed{B_\alpha(t)=u^{2\nu}\phi_\alpha(u^{-2}).}
\tag{5}
\]
核点的二阶极被 \(\psi_\alpha^2\) 全部取消，且在原点的首项给
\(\phi_\alpha\) 为次数 ν、首项一的 x 多项式。

因核阶为 p 单位，其非零核点都不在原形式群，故其 x 坐标整。
又 \([\alpha](u)/u\) 为常数 α 的整单位，所以
\[
B_\alpha=
\left(\frac{\alpha u}{u([\alpha]P)}\right)^2
\prod_{T/\pm1}(1-x(T)u^2)^2
\]
的形式系数整。它已经是多项式；原六角型使它只依赖 t。
于是
\[
\boxed{B_\alpha\in1+t\mathcal O[t].}
\tag{6}
\]

本篇使用首项 α 的 \(\psi_\alpha\)，因此 (5) 的 \(\phi_\alpha\) 首项为一。
若软件采用 monic 的 CM division polynomial，其对应 numerator 首项为
\(1/\alpha^2\)，必须先乘 α² 才是 (5)。这两个规范不能混用。

## 2. 原对数坐标给一个没有共振的整单位算子

置
\[
\boxed{\xi=tH(t)^6=bz^6.}
\tag{7}
\]
这是 (1) 的整坐标：常数项零、一次项一，故其组合逆也整。
记原 \([\alpha]\) 的实际六次参数为
\[
f_\alpha(t)=b\,u(\alpha z(u))^6 .
\]
原形式对数精确给
\[
\xi(f_\alpha(t))=\alpha^6\xi(t),\qquad
f_\alpha=\xi^{-1}(\alpha^6\xi).
\tag{8}
\]
在原完整形式群中先有 (8)，再在 (1) 截断；没有选一个模型 lift。

定义
\[
\boxed{\mathcal D_\alpha=\frac{\nu-f_\alpha^*}{p}:R\longrightarrow R.}
\tag{9}
\]
它一般不是乘法同态。因为 \(\alpha^6\equiv1\pmod p\)、\(\nu\equiv1\pmod p\)，
(8) 先保证 (9) 整。其在完整整基 \(1,\xi,\ldots,\xi^{p-1}\) 上准确对角：
\[
\boxed{\mathcal D_\alpha(\xi^n)=\delta_{n,p}\xi^n,\qquad
\delta_{n,p}=\frac{\nu-\alpha^{6n}}p,\quad0\le n<p.}
\tag{10}
\]
由 (2)–(3)，
\[
\alpha^{6n}=(p+\omega)^{6n}
=1+6np\omega^2\pmod{p^2},
\]
所以
\[
\boxed{\delta_{n,p}\equiv-1-6n\omega^2\pmod p.}
\tag{11}
\]
由于 p 惰性，\(\bar\omega^2\notin\mathbf F_p\)。
若 \(6n\not\equiv0\pmod p\)，(11) 为零会把 \(\bar\omega^2\) 放入 \(\mathbf F_p\)；
若 \(6n\equiv0\)，(11) 为 −1。因此每个 \(\delta_{n,p}\) 都是单位。

**定理 1。** \(\mathcal D_\alpha\) 是 R 的整自同构，且保持 I。
其完整逆为
\[
\boxed{
\mathcal D_\alpha^{-1}
\left(\sum_{n=0}^{p-1}g_n\xi^n\right)
=\sum_{n=0}^{p-1}\delta_{n,p}^{-1}g_n\xi^n.
}
\tag{12}
\]
这里连常数方向也是单位，\(\delta_{0,p}=p-1\)。

模 p 可写成同一个原坐标的明确一阶算子：
\[
\overline{\mathcal D}_\alpha
=-1-6\bar\omega^2\,\xi\partial_\xi
=-1-6\bar\omega^2\,\frac{tH}{C}\partial_t .
\tag{13}
\]
最后一步使用原 \(H+6tH'=C\)，而不是将 u 与 z 相认。
本篇不用 (13) 代替全部高位；实际逆始终是 (10)–(12)。

特别在原中央指标 n=s，
\[
\boxed{\delta_{s,p}=(\nu-\alpha^d)/p\equiv\omega\pmod p.}
\tag{14}
\]
这个指标在此算子下同样没有共振。

## 3. 全部 canonical 项和整体可除性

仍取原
\[
\Theta=x\sigma^2,\quad
c_b^\dagger=-\frac{b^sC_s}{pd},\quad
\Theta^\dagger=\Theta\exp(-2c_b^\dagger z^d),\quad
L=\log\Theta^\dagger\in I.
\tag{15}
\]
其整性与原 c 的整数差已由 R606/R673 支付。
不会因此改变三条原中央 j。

将 (4) 和 x 坐标乘法式相乘，准确得到
\[
\boxed{\Theta(f_\alpha)=B_\alpha\Theta^\nu.}
\tag{16}
\]
并且 \(z([\alpha]P)^d=\alpha^d z^d\)。
保 (15) 的整个 Gaussian 后，
\[
(\nu-f_\alpha^*)L
=-\log B_\alpha-2c_b^\dagger(\nu-\alpha^d)z^d .
\]
因 \(z^d=b^{-s}\xi^s\)，定义
\[
\boxed{
\mathcal N_\alpha
=\log B_\alpha-\frac{2C_s\delta_{s,p}}d\,\xi^s,\qquad
G_\alpha=-\mathcal N_\alpha/p.
}
\tag{17}
\]
原实际 L 因此满足
\[
\boxed{\mathcal D_\alpha L=G_\alpha.}
\tag{18}
\]

**定理 2。** (17) 的整个差属于 pI，故 \(G_\alpha\in I\)，且
\[
\boxed{L=\mathcal D_\alpha^{-1}G_\alpha,\qquad
\Theta^\dagger=\exp(\mathcal D_\alpha^{-1}G_\alpha).}
\tag{19}
\]
证明先用原实际 \(L\in I\) 和 (9)、(18) 支付整体 p 整除；
然后 (12) 给完整且唯一的整恢复。没有将两个单位项分别除 p 后约化。

若
\[
\log B_\alpha(t(\xi))=\sum_{n=1}^{p-1}b_{n,p}\xi^n,
\]
则 (19) 是完全显示的逐系数式
\[
\boxed{
L(t(\xi))
=-\sum_{n=1}^{p-1}
\frac{b_{n,p}-\mathbf1_{n=s}(2C_s\delta_{s,p}/d)}
     {p\,\delta_{n,p}}\xi^n .
}
\tag{20}
\]
每个分子在除 p 前都已证明可除，剩余分母全是单位。

(17) 还给同一原分子的完整模 p 形状：
\[
\boxed{
\log B_\alpha\equiv2\omega C_s\,\xi^s\pmod p,\qquad
B_\alpha\equiv
\sum_{k=0}^{5}\frac{(2\omega C_s)^k}{k!}\xi^{ks}\pmod{pR}.
}
\tag{21}
\]
因 \(6s=p+1>p-1\)，第六项在显示窗口严格消失。
(21) 是实际分子同余，不是可选的模 p sigma 来源。

## 4. 三位分子恢复两位来源，及准确输入精度

对于任何整数 \(r\ge1\)，(17)–(20) 只需如下有限实际数据：

| 输入 | 所需精度 |
|---|---|
| 原 \(B_\alpha\) 的 \(t^{<p}\) 系数 | 模 \(p^{r+1}\) |
| 原 H 与 \(C_s\) | 模 \(p^{r+1}\) |
| 中央 \(\delta_{s,p}\) | 模 \(p^{r+1}\) |
| 其余单位逆 \(\delta_{n,p}^{-1}\) | 模 \(p^r\) |

\(\delta_{s,p}\) 是显示的 CM 整数商；
需要时直接把 \(\nu-\alpha^d\) 算到模 \(p^{r+2}\) 再除 p。
这不要求另一份高精度同源多项式。
在 ξ 坐标中算完整差后除 p，再用 (12) 返回 t，
得到原 \(\Theta^\dagger\bmod p^r\)。

特别 r=2 时，\(B_\alpha\bmod p^3\) 即足够。
R673 用乘 p 分子时的 \((p^2-f_p^*)\) 含两个 p；
这里 \((\nu-f_\alpha^*)\) 恰是 p 乘一个整单位算子。
这是这一个精度改善的具体原因，不是删除原 Gaussian 或 Jacobian。

此输入阶对单独这个方程有准确的区分力。
若将实际 E 改为
\[
\widetilde E=E(1+pV)\pmod{p^2},\qquad V\in I,
\]
则 \(\log\widetilde E-\log E=pV\bmod p^2\)，故
\[
\boxed{
\mathcal D_\alpha\log\widetilde E-G_\alpha
\equiv p\mathcal D_\alpha V\pmod{p^2}.
}
\tag{22}
\]
非零 \(\bar V\) 的残差必非零。
若把这个变化吸收到分子中，则
\[
\boxed{\log\widetilde B_\alpha-\log B_\alpha
\equiv-p^2\mathcal D_\alpha V\pmod{p^3}.}
\tag{23}
\]
所以只看该分子模 p² 不能区分这些比较提升；
模 p³ 的原数据确实读出它们的不同。
这里不把比较分子称为原 CM 多项式。

## 5. 三原中央行仍由同一个提升读取

将 (19) 恢复的实际 \(E^{[2]}=\Theta^\dagger\bmod p^2\)
代 R673 的原全多项式 \(P_m\)，仍准确有
\[
\boxed{
a_{m,h}^{[2]}
=b^{hs-1}[t^{hs-1}]
(E^{[2]})^{m/2}P_m(t)\,C H^{-h-1}
(1-hp\log H)\pmod{p^2},
}
\tag{24}
\]
其中 \(m=34,72,136\)、\(1\le h\le5\)。
这是同一原 canonical 的 \([z^{h(p+1)}]\) 系数；
全部 \(H^{-hp}\) 修正照旧保留。

在原首行 \(a_{m,1}^{[2]}\equiv0\pmod p\) 时，
同一个实际第二类为
\[
\Xi_{m,p}
=\overline{a_{m,2}^{[2]}}
-\bar\gamma_m^\dagger(a_{m,1}^{[2]}/p\bmod p),
\qquad
\gamma_m^\dagger=-m b^sC_s/d,
\tag{25}
\]
且 \(j_m/p^2=-\bar\gamma_m^{-2}\Xi_{m,p}\bmod p\)。
不能把恢复精度或 (21) 的固定非零系数当成 (25) 的非零证明。

(24) 的十五个数使用同一个 \(B_\alpha\) 和同一个 E；
三个 m 没有独立选 lift，也没有给第三条曲线免费增加中央零。

## 6. 原 logarithmic Θ 在首挠边界的准确代数对数

本节不使用 ξ 的闭边界逆。令
\[
\mathscr L(t)=\log\Theta(t)
\]
先按原正式级数定义。原 R639 的
\[
\zeta_{\rm W}(z(u))=u^{-1}J(t),\qquad
J_n=C_n/(1-6n)
\]
给
\[
\frac{d}{du}\mathscr L(bu^6)=\frac2u(J(t)C(t)-1).
\tag{26}
\]
J 的完整进位界只有对数增长；积分再除 6n 仍只有对数分母增长。
因此 \(\mathscr L\) 在整个 \(|t|<1\) 解析。
这里解析的是 log 级数，不声称原 sigma 指数在该盘收敛。

\(B_\alpha\in1+t\mathcal O[t]\) 的实际 p 进 log 也在该开盘解析，
而原 \([\alpha]\) 是形式群的整自同构。
所以 (16) 的正式 log 身份在整个开盘成立：
\[
\mathscr L(f_\alpha(t))-\nu\mathscr L(t)=\log B_\alpha(t).
\tag{27}
\]

现在取原非零 p 挠点 T，令 \(t_T=b\,u(T)^6\)。
所有这些点在原形式群内，R663 给
\(v_p(u(T))=1/(p^2-1)\)。
由 (2)，
\[
[\alpha]T=[\omega^2]T,\qquad f_\alpha(t_T)=t_T.
\]
因此
\[
\boxed{
\mathscr L(t_T)
=-\frac{\log B_\alpha(t_T)}{p(p-1)}.
}
\tag{28}
\]
右边是一个明确代数数的 p 进对数，所有原点、分子和尺度均固定。
而 \(z(T)=0\)，故把 canonical 项减去后在这些点仍有同一个值。

(28) 不把 log 值称为代数数，也没有对它取未支付收敛的指数。
它也不证明 R663 的完整源余数消失，更不证明 \(j_m=0\) 迫边界解析。
可继续用它研究 R639 完整整单位在这些实际挠点的值；
该步骤须保原范数一投影及全部根的分支，不能只读单个首系数。

## 7. 范围

本篇完成一个实际的 prime-to-p CM 读取接口：整单位逆、整体 p 整除、
三位分子给两位原来源、全部三曲线两位中央读数及首挠边界 log 身份。
没有运行新素数扫描。

\(\alpha,\nu,B_\alpha\) 依赖 p，并非原固定全局来源格的免费新列。
仍须在无穷不同 p 排除原指定首/次中央同时失败，
或从原中央到 R663 全余数、完整同 R forcing 或全九格之间补出真正联系。
原固定曲线无穷初级有限的主目标仍未完成。

## 依赖和规范参考

- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)，
  §2 的原 CM sigma 乘法式及其完整 prime-to-p 整性，§4 的全 zeta 界。
- [R673](R673-original-multiplication-numerator-and-canonical-second-lift.md)，
  原窗口、canonical 整性及三原来源完整读取。
- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)，
  全部首 p 挠点和内盘/闭边界的区分。
- NIST DLMF §23.2，尤其 23.2.15–17 的原 sigma 准周期规范：
  https://dlmf.nist.gov/23.2 。本篇乘法恒等使用 R639 已写出的完整证明。
- Magma Handbook, “Complex Multiplication Division Polynomials”：
  https://magma.maths.usyd.edu.au/magma/handbook/text/1547 。
  其 monic division polynomial 规范对应的 numerator 首项为 \(1/\alpha^2\)；
  本篇在 (5) 明确恢复首项一，不把软件规范误认原分子。
