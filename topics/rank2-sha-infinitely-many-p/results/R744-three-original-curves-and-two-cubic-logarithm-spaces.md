# R744 — 三条原曲线点空间与两个实际三次 logarithm 的分离

日期：2026-11-15。**状态：下述点空间及 logarithm 分离已证明。**

本篇继续 R733/R735/R739 的同两个实际点，不更换原曲线或原负矩。
R739 已处理十七处不分歧的 E1 点；这里把原 E17、E24、E2312
三条曲线的实际六次缩放同时纳入。
E2312 的十七处三次分歧不能删除，但其二处的平方根惯性提供另一项分离。
本篇不给尚未识别的条件积分预先赋予这些点空间。

## 1. 固定域、点和微分

置
\[
K=\mathbf Q(\omega),\quad\omega^2+\omega+1=0,\qquad
E_b:\ y^2=x^3+b,\qquad \varpi_b=\frac{dx}{2y}.
\]
使用 [R733](R733-two-cubic-points-and-algebraic-independence-of-p-adic-logarithms.md)
的实际非扭点，令
\[
t^3=17,\quad \theta^2=t,\quad \theta^3=\sqrt {17},
\quad M=K(\theta),\quad L=K(t).
\tag{1}
\]
相容地选择这些根。两个 E1 点是
\[
Q_2=(-4/t^2,15/17),\qquad
Q_4=(42/t^4,397/289).
\tag{2}
\]
它们分别来自 E289、E83521 的 R733 实际点。
取
\[
\theta_{17}=\theta,\qquad
\theta_{24}^6=24,\qquad
\theta_{2312}=\sqrt2\,t,
\tag{3}
\]
最后一式使用 \(2312=8\cdot17^2\)。所有根都作为固定代数数选择。
原曲线的确切同构为
\[
\phi_b:E_b\longrightarrow E_1,\quad
(x,y)\longmapsto(x/\theta_b^2,y/\theta_b^3),
\qquad \phi_b^*\varpi_1=\theta_b\varpi_b.
\tag{4}
\]
因此对每个有理素数 p 和每个固定代数闭包嵌入，
\[
\log_{E_1,p}(\phi_b R)=\theta_b\log_{E_b,p}(R).
\tag{5}
\]
这里用不变微分定义的完整椭圆 logarithm；可先乘共同整数进入形式群，
再除回该整数。坏约化或小素数不改变本篇的点空间论证。

记 \(\mathscr U_{17}\) 为所有在 K 的十七处不分歧的有限扩张的并；
记 \(\mathscr U_{2,17}\) 为同时在二、十七处不分歧的有限扩张的并。
每个有限点族都落在相应的一个有限合成域中。
这些域可以依赖 p、有限层和所选的原测试；本篇不要求统一次数上界。

定义
\[
\begin{aligned}
\mathcal A={}&
 \phi_{17}E_{17}(\mathscr U_{17})
 +\phi_{24}E_{24}(\mathscr U_{17})
 +\phi_{2312}E_{2312}(\mathscr U_{2,17})\\
&\subset E_1(\overline{\mathbf Q})\otimes_{\mathbf Z}\mathbf Q .
\end{aligned}
\tag{6}
\]
下面的 span 均为真正的 K=End(E1)⊗Q 线性 span，
模去 torsion 后理解；不把 p 进系数当作 End 系数。

## 2. 两个不同坏素数上的精确 Kummer 作用

在十七处，\(X^6-17\) 是 Eisenstein 多项式。
由于 \(\mu_6\subset K\)，M/K 为循环六次扩张，并在十七处完全分歧。
每个非平凡中间扩张仍在该处分歧。
若 F/K 在十七处不分歧，则
\[
F\cap M=K.
\tag{7}
\]
\(\sqrt2\) 和 \(\theta_{24}\) 的定义多项式在十七处均为 étale：
其根为单位，导数中的 2、6 及相应单位在十七处可逆。
所以把这两个根加入 F 仍保十七处不分歧。

取 M/K 的生成元
\[
\sigma(\theta)=-\omega^2\theta,\qquad
\sigma(t)=\omega t.
\tag{8}
\]
在有限合成域 \(F(\sqrt2,\theta_{24})M\) 上令 σ 固定前面的不分歧域。
按照约定 \([\omega](x,y)=(\omega x,y)\)，直接由坐标得到
\[
\begin{array}{c|c}
\text{E1 上的实际点} & \sigma\text{ 的作用}\\ \hline
Q_2 & [\omega]Q_2\\
Q_4 & [\omega^2]Q_4\\
\phi_{17}(R),\ R\in E_{17}(F) & [-\omega^2]\phi_{17}(R)\\
\phi_{24}(S),\ S\in E_{24}(F) & \phi_{24}(S)\\
\phi_{2312}(T),\ T\in E_{2312}(F) & [\omega]\phi_{2312}(T).
\end{array}
\tag{9}
\]
例如 \(\sigma(\theta^{-2})=\omega^2\theta^{-2}\) 且
\(\sigma(\theta^{-3})=-\theta^{-3}\)，给第三行。
最后一行用 \(\sigma(\sqrt2t)=\omega\sqrt2t\)。
因此 E2312 的三次角色确与 Q2 相同；只看十七处不能把两者分开。

另一处的作用也由这些真实域支付。
\(X^3-17\) 的判别式在二处为单位，故 L/K 在二处不分歧。
\(K(\sqrt{17})/K\) 在二处也不分歧：
\(\mathbf Q(\sqrt{17})\) 的判别式为 17。
所以 M/K 在二处不分歧。
而 K 在二处本身不分歧，\(X^2-2\) 在该处 Eisenstein；
对任意二处不分歧 F，有
\[
\sqrt2\notin FL.
\tag{10}
\]
在 \(FL(\sqrt2)\) 上取
\[
\tau(\sqrt2)=-\sqrt2,\qquad \tau|_{FL}=1.
\]
则
\[
\tau Q_2=Q_2,\qquad \tau Q_4=Q_4,\qquad
\tau\phi_{2312}(T)=-\phi_{2312}(T)
\quad(T\in E_{2312}(F)).
\tag{11}
\]
这里没有把 E2312 换成 E289：
二处的实际二次扭角色正是 (11) 所用的数据。

## 3. 原三曲线点 span 的准确分离

**定理 1。**
\[
\boxed{\quad
(KQ_2\oplus KQ_4)\ \cap\ \operatorname{span}_K\mathcal A=0 .
\quad}
\tag{12}
\]
更准确地，若 \(a,b\in K\) 及一个有限的原点组合满足
\[
aQ_2+bQ_4+
 \sum_j c_j\phi_{17}R_j+
 \sum_j d_j\phi_{24}S_j+
 \sum_j e_j\phi_{2312}T_j=0
 \quad\bmod\text{torsion},
\tag{13}
\]
各系数在 K，\(R_j,S_j\) 的定义域在十七处不分歧，
\(T_j\) 的定义域在二、十七处不分歧，则 \(a=b=0\)。

**证明。**
将 (13) 中全部点的定义域合成为一个在十七处不分歧的有限域 F。
加入 \(\sqrt2,\theta_{24}\) 后仍可按 (7)–(8) 取同一个 σ。
在模 torsion 的 K 向量空间上使用真正的有限投影
\[
e_\eta=\frac16\sum_{j=0}^{5}\eta^{-j}\sigma^j,
\qquad \eta\in\{\omega,\omega^2\}.
\tag{14}
\]
这些是 K[Gal] 算子；若要在整 End 模中操作，可先乘 6 并清除 (13) 的分母。
(9) 给
\[
e_{\omega^2}(13):\quad bQ_4=0,\qquad
e_\omega(13):\quad aQ_2+\sum_j e_j\phi_{2312}T_j=0.
\tag{15}
\]
Q4 非扭，所以 \(b=0\)。

第二个关系的所有实际点已落在
\(F_TL(\sqrt2)\)，其中 \(F_T\) 只需合成 Tj 的定义域；
它在二、十七处不分歧。先前 Rj/Sj 的域不再出现在这个关系中，
所以无须假设它们在二处不分歧。
由 (10)–(11)，对第二个关系施加 \(1+\tau\)，得到 \(2aQ_2=0\)。
Q2 非扭，因此 \(a=0\)。证毕。

这也解释了 (6) 的两种定义域条件不能混写：
E17/E24 只需十七处不分歧；
E2312 需要额外的二处条件。
二处条件实际不可删除：原点
\[
T_0=(-8,30\sqrt2)\in E_{2312}(K(\sqrt2))
\]
满足 \(\phi_{2312}T_0=Q_2\)。这是 (4) 的准确逆像，
而 \(K(\sqrt2)/K\) 在十七处不分歧、在二处分歧。
所以若把 E2312 的域门也放宽成仅十七处不分歧，(12) 就明确失败。

## 4. 全 p 的代数系数 logarithm 分离

对固定 p，令
\[
\begin{aligned}
\mathcal W_p=\operatorname{span}_{\overline{\mathbf Q}}\bigl\{&
\theta_{17}\log_{E_{17},p}R,\
\theta_{24}\log_{E_{24},p}S,\
\theta_{2312}\log_{E_{2312},p}T:\ \\
&R,S\text{ 分别定义于 }\mathscr U_{17},\
T\text{ 定义于 }\mathscr U_{2,17}\bigr\}.
\end{aligned}
\tag{16}
\]
仍将所有代数数通过固定嵌入视为 \(\mathbf C_p\) 中的数。
又置
\[
\mathcal T_p=
\overline{\mathbf Q}+
\operatorname{span}_{\overline{\mathbf Q}}
 \{\log_p(\alpha):\alpha\in\overline{\mathbf Q}^{\times}\},
\qquad\log_p(p)=0 .
\tag{17}
\]

**定理 2。**
\[
\boxed{\quad
\operatorname{span}_{\overline{\mathbf Q}}
 \{\log_{E_1,p}Q_2,\log_{E_1,p}Q_4\}
 \ \cap\ (\mathcal W_p+\mathcal T_p)=0 .
\quad}
\tag{18}
\]
两个显示 logarithm 自身也在 \(\overline{\mathbf Q}\) 上独立。

**证明。**
任意候选关系只含有限多个点。
在它们实际张成的 K 向量空间中选一组由这些点组成的基。
定理 1 使 Q2、Q4 可与这组基一并保持 K 线性独立。
清除分母并乘共同整数，使各点进入各自 p 进指数的定义域；
非扭点的 logarithm 不为零。
Fuchs–Pham 的 p 进解析子群定理推论（Theorem 2.2），
以 \(\operatorname{End}(E_1)\otimes\mathbf Q=K\)，
给所有这些 logarithm 的 \(\overline{\mathbf Q}\) 线性独立。

若还含 (17) 的乘法 logarithm 和常数，
用同一定理的代数群形式（Theorem 2.1）作用于
\(\mathbf G_a\times\mathbf G_m^r\times E_1^n\)。
无非零同态连接仿射代数群和椭圆部分，
故一个消失的代数系数线性式在椭圆部分产生同样的 End 线性关系，
与定理 1 矛盾。
这里正是 [R739](R739-seventeen-inertia-and-relative-algebraic-logarithm-separation.md)
§4 中已经完整支付的解析子群论证，只把它的实际点空间换成 (6)。
最后用 (5) 恢复 (16) 的三个微分尺度。证毕。

(18) 不允许把 \(\mathbf C_p\) 中任意未知条件质量作为系数。
它需要所有系数为代数数；
也没有要求代数系数是 p 进单位或不依赖 p。

## 5. 与原两负矩及三来源的接口

R735 对同一个共同周期和同一规范已经证明
\[
\Omega_p I_k=A_{k,p}\log_{E_1,p}Q_k,\qquad
A_{k,p}\in\overline{\mathbf Q}^{\times},\qquad k=2,4.
\tag{19}
\]
因此对任意不全为零的 \(a,b\in\overline{\mathbf Q}\)，有
\[
\boxed{\quad
\Omega_p(aI_2+bI_4)\notin\mathcal W_p+\mathcal T_p .
\quad}
\tag{20}
\]
这适用于 R734 的真实组合，因为其两个系数及 (19) 的常数均已支付。

(20) 给出了三个原曲线若以实际点返回时可用的分离条件。
要用于原中央问题，必须另行证明：

1. 所考察的完整积分，包括所有有限 p 门、伴随正矩和完整返回分母，
   确实等于 (16) 中的有限代数系数点组合及允许的 (17) 项；
2. 实际点的定义域满足分别列出的十七处、二处不分歧条件；
3. 全部共同 period、Euler/Gauss 因子及原混次权已经同步，
   不留任意 p 进伴随系数；
4. R737/R740 的 G4、条件质量及所有外部补偿仍属于同一个所用身份。

特别，R740 的完整 \(Y_\kappa\) 仍有范数34及原十七处 gluing；
不能只因其 W/V 球张量，就将它写进 E24 那一项。
E2312 的二处条件也不由“它是固定曲线”自动获得。
本篇没有补上这些未付接口，不由 (20) 宣称原中央已非零。

## 参考

- [R733](R733-two-cubic-points-and-algebraic-independence-of-p-adic-logarithms.md)：
  两实际非扭点与 End 独立。
- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)：
  原负矩、共同周期与非零代数常数。
- [R739](R739-seventeen-inertia-and-relative-algebraic-logarithm-separation.md)：
  相对点空间的解析子群论证和乘法 logarithm 扩张。
- [R740](R740-original-w-v-spherical-seventeen-tensor-and-mixed-cuts.md)：
  完整返回的十七处张量与不可删除的 Y gluing。
- C. Fuchs, D. H. Pham,
  [The p-adic analytic subgroup theorem revisited](https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf),
  Glasnik Matematički 51(71) (2016), 335–343，Theorems 2.1、2.2。
