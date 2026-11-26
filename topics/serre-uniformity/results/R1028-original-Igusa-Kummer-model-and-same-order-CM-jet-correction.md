# R1028：原 Igusa Kummer 坐标与同阶 CM 首 jet 的真实整修正

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；
global_route / root。

**已证明：在原 \(p\equiv11\bmod12\) 行，底 Hodge 层的整角色提升
允许一条具体的 Igusa 修正，它在原 CM 尾上准确于
\(\varepsilon^4\) 阶出现，并改变同一个首 jet 系数。**
该线是原 Kummer 模型上的 \(b\,db/u^2\)，其节点阶、完整惯性、
三次 deck 角色和节点单位全部保留。

本篇不把“可换一个整 Hodge 提升”当成“可换实际指定商的微分”。
它给出后续实际 Hecke／商比较必须计算的一个系数。
R918 已给整个 Igusa 角色空间的对应，R920 已算权六空间；
这里的新内容是同一个原 \(b\) 上的完整坐标、实际节点阶及
与底层微分在同一 \(\varepsilon^4\) 阶的比较，不重新登记旧维数结论。

## 1. 原模型和本文的角色约定

保持 R1014、R1018、R1023 的模型、原点、六标记与
\(\kappa_4\) 扭曲。置
\[
p=12g-1>37,\qquad m=(p-1)/2=6g-1,\qquad
e_0=m(p+1),\qquad \pi_0^{e_0}=p,\qquad
\varepsilon=\pi_0^m .
\tag{1028.1}
\]
于是 \(\varepsilon^{p+1}=p\)。
底环先作足够的非分歧扩张，所有特殊纤维系数在 \(k\) 中。
惯性生成元和原 deck 作用写为
\[
\sigma(\pi_0)=\xi\pi_0,\quad \xi^{e_0}=1,\qquad
\delta(b)=\zeta^2b .
\tag{1028.2}
\]
\(\xi\) 取原始根，\(\zeta\) 取原三次单位根；二者的作用交换。
本文的 Hodge 权 \(w\) 指
\(\sigma^*\Omega=\xi^w\Omega\)，不是其 Serre 对偶的逆角色。

原中心 \(I\) 是已经保留 tame quotient 的
\(\operatorname{Ig}(p)/\{\pm1\}\) 分量。
\(b\) 是 R1023 的实际 Frobenius 侧坐标，原另一侧仍为 \(a=b^p\)。
取同一个有理椭圆族
\[
E_b:\quad y^2=x^3+3brx+r(1-2b^3),\qquad
r=1-b^3,\qquad \omega=dx/(2y).
\tag{1028.3}
\]
其准确 Hasse 多项式为
\[
h_p(b)=[x^{p-1}](x^3+3brx+r(1-2b^3))^m
      =r^{2g}A_p(b),
\]
\[
A_p(b)=bQ_p(b^3),\qquad
\deg A_p=6g-2,\quad \deg h_p=12g-2=2m.
\tag{1028.4}
\]
\(A_p\) 单首、根全简单，且与 \(r\) 互素，均已在 R1023 §4
由同一个族的 Hasse／Gauss–Manin 方程核准。

本文的 \(u\) 专指平方 Hasse 根，不是 R920 的 tame 基坐标。
实际函数域准确为
\[
\boxed{\quad k(I)=k(b,u),\qquad u^m=h_p(b).\quad}
\tag{1028.5}
\]
说明其来源：在 fine Igusa 模问题上，规范微分
\(\omega_{\rm Ig}=\mathfrak a\,\omega\) 的 Hasse 值为一，
故 \(\mathfrak a^{p-1}=h_p\)。
生成元的正负作用把 \(\mathfrak a\) 变成其负数，取商后
\(u=\mathfrak a^2\)，得到 (1028.5)。与实际 tame 商在 generic
点相同，取正规化即得原光滑中心。
若为取得好族而换一个二次 twist，Hasse 变成 \(d^m h_p\)，
只须把 \(u\) 换为 \(u'=du\)；函数域不变。
同一几何微分须同步运输分子及 \(\omega\) frame，例如原
\(b\,db/u^2\) 写成 \(bd^2\,db/(u')^2\)，不能把字面的
\(b\,db/(du)^2\) 当成原微分。本篇后文始终用 (1028.3) 的原 frame，
没有换成一个任意 Kummer cover。

## 2. 全部节点阶及真正的权六微分

对 (1028.5) 逐类计算正规化上的赋值。

| 基上的点 | 分歧指数 | \(u\) 的阶 | \(db/u^2\) 的阶 |
|---|---:|---:|---:|
| \(A_p(s)=0\) | \(m\) | \(1\) | \(m-3\) |
| \(b^3=1\) | \(m\) | \(2g\) | \(2g-2\) |
| \(b=\infty\) 的每个上方点 | \(1\) | \(-2\) | \(2\) |

第一行使用 \(A_p\) 的简单零。
第二行使用
\(\gcd(m,2g)=\gcd(6g-1,2g)=1\)。
无穷远因为 \(\deg h_p=2m\)，在代数闭剩余域有 \(m\) 个
不分歧点；\(db\) 在每点为二阶极点。
其它点均为单位。

任意 \(u^{-2}\) 角色的 rational differential 都唯一写成
\(F(b)\,db/u^2\)。若 \(F\) 在有限基点有极点，在前两类点的
阶至少分别下降 \(m\)，在其它有限点的阶下降至少一，
都会破坏正则性。因此 \(F\) 必为多项式；
无穷远的阶又准确要求 \(\deg F\le2\)。
故整个 holomorphic 角色空间是
\[
\boxed{\quad
H^0(I,\Omega^1)_{u^{-2}}
 =\langle1,b,b^2\rangle\,\frac{db}{u^2}.
\quad}
\tag{1028.6}
\]

原 \(\delta(b)=\zeta^2b\) 使 \(h_p\) 变为 \(\zeta^2h_p\)。
由于 \(m\equiv2\bmod3\)、\(\gcd(m,3)=1\)，它的唯一 order-three
提升为
\[
\delta(u)=\zeta u .
\tag{1028.7}
\]
因而 (1028.6) 中三条线的 deck 角色依次为 \(1,\zeta^2,\zeta\)。
所需的新部负角色准确为
\[
\boxed{\quad \nu_I=b\,db/u^2,\qquad \delta^*\nu_I=\zeta^2\nu_I.\quad}
\tag{1028.8}
\]
在三个原 CM 节点 \(b=\xi_0\)、\(\xi_0^3=1\)，\(b\) 为单位，
故该微分准确有阶 \(2g-2\)，首系数非零。

其模权也不能换成 R918 的权四。
同一 Gauss–Manin 矩阵给
\(\operatorname{KS}(\omega^2)=db/(2r)\)。
规范 Igusa 微分的平方为 \(u\omega^2\)，所以权 \(k\) 截面
\(F\omega^k\) 的 Igusa 微分为
\[
F\,u^{\,1-k/2}\frac{db}{2r}.
\tag{1028.9}
\]
因此 (1028.6) 对应 \(k=6\)，原三个截面在此 frame 为
\(2r,2rb,2rb^2\)。
这是 R920 §2 所算 \(S_6(H_6)\) 的实际 \(b\)-模型；
不是为本题另造的权四线，也不能直接套用另一权的
\(T_5\) 特征值。

## 3. 完整惯性权，而非只在标量子群上的角色

在任一 \(e_s=1\) 尾的无穷点，R1018 的原参数 \(z\) 满足
\[
\sigma(z)=\xi^{m^2}z .
\]
实际厚度一节点的中心参数 \(w\) 满足 \(zw=\pi_0\) 到保留单位，
故其权为
\[
1-m^2=(p+1)\left(-\frac{m-1}{2}\right).
\tag{1028.10}
\]
在该简单 Hasse 零，\(u\) 是中心的 uniformizer。
中心 deck cover 在 \(\mathbf P^1_b\) 上，惯性固定 \(b\)，
故这一个点读出的 deck 作用已经确定整个 \(I\) 上的作用。
将 (1028.10) 除以 \(p+1\) 并模 \(m\) 看，其值为 \(1/2\)。
所以 \(db/u^2\) 的完整权为
\[
\boxed{\quad w_I=e_0-(p+1).\quad}
\tag{1028.11}
\]
这包含 determinant／normalizer 的原修正；没有只核
\(\mathbf F_p^\times\) 中的平方。

原 compact-type 模型的 Hodge 格是自由的，并满足 base change；
有理链不增加其 Hodge 空间。
对惯性及 \(\delta\) 作单位平均，可取整 eigenlift \(\Omega_I\)，
其特殊纤维只有中心分量 (1028.8)，其它分量为零，并使
\[
\sigma^*\Omega_I=\xi^{w_I}\Omega_I,\qquad
\delta^*\Omega_I=\zeta^2\Omega_I.
\tag{1028.12}
\]
这里 lift 的存在是实际整 Hodge 格的 base change，不是假设
中心在混合特征有一个独立的代数 Jacobian 因子。

## 4. 底 Hodge lift 允许的同角色整修正

令 \(\Omega\) 是原底 Hodge 权 \(m\)、deck 角色 \(\zeta^2\)
的整微分，其特殊纤维在 \(e_s=1\) 尾的底层。
若需要 \(\delta\) 特征向量，取真实尾空间中的对应线性组合；
不把一个被 \(\delta\) 置换的单尾基向量当成特征向量。

对任意非分歧常数 \(c\)，
\[
\boxed{\quad
\Omega\longmapsto\Omega+c\pi_0^{3m+2}\Omega_I
\quad}
\tag{1028.13}
\]
保留整性、同一特殊纤维及两种完整角色，因为
\[
3m+2+w_I=e_0+m.
\tag{1028.14}
\]
这确实是原整 Hodge 格内的修正。

为确定哪些提升差可能进入所需精度，使用 R1018 的全部 Hodge 权：
尾的权至多 \(m^2=e_0/2-m\)；
中心的权是非零的 \((p+1)\) 倍数，且至多 \(w_I\)。
中心无权零，因为其惯性商为 \(\mathbf P^1_b\)。
换一个具有同一特殊纤维的底 eigenlift 时，来自另一尾权的正
\(\pi_0\) 次数至少
\[
e_0+m-m^2=e_0/2+2m>4m.
\]
同权尾提升差的最小次数为 \(e_0\)。
中心权若写为 \(e_0-j(p+1)\)，对应最小正次数为
\(m+j(p+1)\)。
\(j\ge2\) 时它至少 \(5m+4>4m\)；
只有 \(j=1\) 给 (1028.13) 的 \(3m+2\)。
在这个中心权内，指定 \(\delta=\zeta^2\) 的空间由 (1028.8)
准确为一维。因此在精度 \(4m\) 内，保持全部所列数据的可能
提升差只剩 (1028.13) 的这一条中心线。

## 5. 真实厚度三节点把该修正送到 \(\varepsilon^4\)

固定原 \(c_1\) 所在 CM 尾，保持 R1014/R1018 的坐标
\[
D:\quad y^2=x(x^{2g}+A),\quad A\in k^\times,\qquad
Q=(0,0).
\tag{1028.15}
\]
其与 \(I\) 相交的无穷点，以
\[
x=z^{-2},\qquad
y=z^{-(2g+1)}\sqrt{1+Az^{4g}}
\]
为参数描述。实际节点方程是
\[
zw=\rho\,\pi_0^3,\qquad \rho\in R^\times.
\tag{1028.16}
\]
不把原节点单位 \(\rho\) 设成一。
在该中心节点，(1028.8) 写为
\[
\nu_I=(c_Iw^{2g-2}+\cdots)\,dw,\qquad c_I\in k^\times.
\tag{1028.17}
\]
故由同一节点的相对 dualizing differential，传到 \(D\) 的
首 principal part 准确为
\[
-c_I\bar\rho^{\,2g-1}\,
\pi_0^{3(2g-1)}z^{-2g}\,dz,\qquad
3(2g-1)=m-2.
\tag{1028.18}
\]

这里也须排除更早的 normal 层。
在中心的 smooth generic chart，任一正 \(\pi_0^n\) 项的
rational differential 具有权 \(w_I-n\)；
中心惯性阶整除 \(m\)，故其权必为 \((p+1)\) 倍数。
\(0<n<m-2<p+1\) 时不可能出现这种项。
特殊纤维项本身在节点有准确阶 \(2g-2\)，由 (1028.16) 传递的
第一个极部就是 (1028.18)。
如在更低 normal 阶存在无极部项，它须是 \(D\) 上的
holomorphic differential；R1018 的尾角色又排除此项。
同样，\(\Omega_I\) 的两个同特殊纤维 eigenlifts 相差的全局
次数至少 \(p+1\)：它是最大 Hodge 权，距下一个可能中心权
至少 \(p+1\)，距所有尾权更大。
所以这些 lift 差不会改变 (1028.18)。

乘 (1028.13) 的 \(\pi_0^{3m+2}\) 后，准确总阶为
\[
(3m+2)+(m-2)=4m,\qquad \pi_0^{4m}=\varepsilon^4 .
\tag{1028.19}
\]
首层的角色是 \(-3m\)。
原 \(D\) 的全部 holomorphic Hodge 权为
\(3m(2j+1)\)、\(0\le j<g\)，没有一个模 \(e_0\) 等于 \(-3m\)。
故给定 principal part 后，没有同角色 holomorphic ambiguity。
利用
\[
x^{2g-1}\frac{dx}{y}
=-2z^{-2g}(1+Az^{4g})^{-1/2}\,dz,
\]
(1028.18) 唯一确定修正的完整首 normal differential：
\[
\boxed{\quad
\overline{\varepsilon^{-4}
      (c\pi_0^{3m+2}\Omega_I)|_D}
 =\bar c\,\frac{c_I\bar\rho^{\,2g-1}}2
       x^{2g-1}\frac{dx}{y}.
\quad}
\tag{1028.20}
\]
这里除以 \(\varepsilon^4\) 后只沿 \(D\) 取首 normal 层，
并不声称这个除过的微分在整个模型上仍整。

在原 \(Q=(0,0)\) 取 \(t=\sqrt x\)，则
\[
x^{2g-1}\frac{dx}{y}
=\frac2{\sqrt A}\,t^{4g-2}\,dt+\cdots .
\tag{1028.21}
\]
所有显示的外因子均为单位。因此 (1028.13) 确实改变
同一 \(\varepsilon^4t^{4g-2}dt\) 系数，且 \(\bar c\) 任意。
这证明的是一个实际整提升差，不是抽象维数上可能存在某种修正。

## 6. 对原 CM Abel jet 比较的准确含义

只由底 \(e_s=1\) 尾的特殊微分、其完整惯性及 deck 角色，
不能断言原 \(c_1\) 上指定首 jet 系数已经等于某个候选单位：
(1028.13) 保这些数据，(1028.20)–(1028.21) 却改变该系数。
任何只计算中心 rational principal part、随后略去中心
holomorphic contribution 的推导，都会漏掉本篇的实际线。

这不使 R1011 的实际 quotient \(q_C\) 或其 pullback 微分
成为可任意选择的对象。指定商、Hecke 特征系统和原整格
会选定一个具体提升；须对那个提升计算 (1028.13) 的系数。
即使后续证明相关 Hecke spectra 分离，也只能据实际算子
求解非齐次修正，不能因此把系数直接设为零。

R1026 已证明原 log 在饱和 CM Lie 商中为第 \(m\) 层本原。
本篇没有把它转换成某个具体 Néron 商格的单位，也没有证明
它与实际 CM Abel jet 的相对行列式为单位。
R921 对旧指定正 CM quotient 的权四／权十 normal 层保持原结论；
这里研究的是另一条底 Hodge 来源及其权六修正，不能混用。

## 来源与核准

- [R1014](R1014-original-CM-divisor-reduction-and-Igusa-Frobenius-principalization.md)、[R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)：同一 \(b\)、原 compact-type 模型、全部惯性权及实际节点厚度。
- [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)：同一 \(E_b\)、准确 Hasse 多项式及 Gauss–Manin／Kodaira–Spencer frame。
- [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md)，§4：原完整 normalizer 角色、Igusa 的正负商及整个 character space 的对应。
- [R920](R920-original-upper-primitive-Igusa-layer-and-inert-Hecke-row.md)，§2：已经算出的整个权六 tame 空间；本篇只补实际 \(b\)-坐标和节点比较。
- [R921](R921-original-Igusa-node-and-first-Drinfeld-normal-differential.md)：原模型上的整 Hodge 运输和 node principal-part 方法；其旧指定 CM 来源与本文底来源分别保留。
- Ulmer，[On Universal Elliptic Curves Over Igusa Curves，作者原文](https://dlulmer.github.io/research/papers/1990a.pdf)，Lemma 1.1、Proposition 1.2：规范 Igusa 微分、Hasse 根及角色对应。本文的 Kummer 分歧、原 \(\delta\) 和实际 normal 阶按上述方程直接证明。

global_route 与 root 纸面核对原 Kummer 函数域、全部分歧阶、
完整惯性提升、最大 Hodge 权的次数界、实际厚度三节点的单位、
同角色 holomorphic 排除和同一个 \(Q\)-jet。
本篇不使用数学程序或数值窗口。
Serre 主目标仍 OPEN。
