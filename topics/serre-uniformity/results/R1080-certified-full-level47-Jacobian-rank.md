# R1080. 原完整层 47 Jacobian 的无条件秩为 73

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

**状态：已证明，含精确及严格区间计算。**
令 $X=X_{\rm ns}^+(47)$、$J=\operatorname{Jac}(X)$。则
$$
\boxed{\quad
\dim J=\operatorname{rank}J(\mathbf Q)=\rho_{\mathbf Q}(J)=73.
\quad}
\tag{1080.1}
$$
R45 的 Heegner 商在这个具体水平恰为整个 $J$（至 $\mathbf Q$-同源）。
对应的完整新 Fricke 正号空间恰有三个有理简单因子，
维数分别为 $16,24,33$。

这里 $\rho_{\mathbf Q}$ 是定义于 $\mathbf Q$ 的 Néron–Severi 秩，
不声称几何 Picard 秩也恰为 73。
本结果不是 Mordell–Weil 饱和证书或有理点分类。
R1074 的八个原 CM 圆盘内部仍须继续排点；全素数 Serre 主目标仍开放。

## 1. 原曲线与正确的平方水平空间

R45 §1 所用 Chen–de Smit–Edixhoven 同源给
$$
J\sim_{\mathbf Q}J_0^+(47^2)^{\rm new}.
\tag{1080.2}
$$
所以必须计算全部
$S_2(\Gamma_0(2209))^{+,{\rm new}}$；
这里的 $+$ 是 Fricke $W_{2209}$ 特征值，不能用 modular symbols
的 star sign=1 代替。

本次首先取有理 modular symbols 的 star-positive 部分。
真实精确维数为：ambient 189、cuspidal 165、new 157，
相应 Sturm bound 为 376。
在这个完整 new space 上独立计算实际 Fricke 矩阵，核 $W^2=I$，
并取得
$$
\operatorname{Tr}W=-11,\qquad
\dim W^+=73,\qquad \dim W^-=84.
\tag{1080.3}
$$
这个维数也与 R1078 §7.1 原 $j$-map 的 Riemann–Hurwitz 计算一致；
后者不依赖秩计算。

对全 new space 作精确 Hecke 分解，逐因子核 Fricke 为 $+I$ 或 $-I$，
并核全部维数及两个符号的维数和。
正号因子恰为下表；每个 coefficient field 的次数等于其 star-positive
因子维数，而且所有嵌入都是实嵌入。

| 本次精确分解中的因子 | 维数/系数域次数 | 已认证的实嵌入数 | 全部严格导数区间的共同粗界 |
|---|---:|---:|---|
| 8 | 16 | 16 | $0.8<L'(f^\sigma,1)<6$ |
| 10 | 24 | 24 | $0.8<L'(f^\sigma,1)<6$ |
| 11 | 33 | 33 | $0.7<L'(f^\sigma,1)<7$ |

因子编号只标识这个钉住的 Sage 分解顺序；
数学对象由其实际新空间、Fricke 号和 q-eigenform 系数哈希共同标识。
没有只抽样一个嵌入后把其余嵌入假定非零。

## 2. 严格 $L'$ 包围公式及尾界

令 $f=\sum_{n\ge1}a_nq^n$ 为其中一个标准化形式，$c=2\pi/47$。
权二 Fricke 正号对应函数方程符号 $-1$。
Dogra–Le Fourn (2021), Lemma 15 的归一化是
$$
L'(f,1)=2\sum_{n\ge1}\frac{a_n}{n}E_1(cn),
\qquad
E_1(x)=\int_x^\infty e^{-t}\frac{dt}{t}.
\tag{1080.4}
$$

为核对所有常数，设
$\Lambda(f,s)=(47/(2\pi))^s\Gamma(s)L(f,s)$。
Fricke 关系给
$$
\Lambda(f,s)=
 \int_1^\infty f(iy/47)(y^{s-1}-y^{1-s})\,dy.
$$
故
$$
\Lambda'(f,1)=
 2\sum_{n\ge1}\frac{a_n}{cn}E_1(cn).
$$
又 $L(f,1)=0$，完成因子的导数不另加项；
乘 $c$ 即得 (1080.4)。

对所有复嵌入，Deligne 界和坏素数的新形式关系给
$|a_n|\le d(n)\sqrt n\le2n$。
这里 $a_{47}=0$，没有漏掉平方水平的坏 Euler 因子。
由 $E_1(x)\le e^{-x}/x$，对 $M\ge1$ 有
$$
\left|2\sum_{n>M}\frac{a_n}{n}E_1(cn)\right|
\le
\frac{4e^{-c(M+1)}}{c(M+1)(1-e^{-c})}.
\tag{1080.5}
$$

实际用 $M=256$、512 bit Arb/acb。
(1080.5) 的球上界小于 $1.116\cdot10^{-15}$。
q 系数全部精确；系数域的实根先在 AA 中严格隔离，
再经有向舍入实区间转换成球，并在原多项式基上评价。
$E_1$ 用认证的 ComplexBall.exp_integral_e(1)，
所有前缀和再以 RealBall.add_error 加入 (1080.5) 的上界。

最终所有 73 个扩大后的球都严格为正，范围如 §1。
普通浮点近似、symbolic E1 或 mpmath 值没有用于这个认证。
完整源脚本逐个验证 $a_0=0,a_1=1,a_{47}=0$、系数域次数及嵌入完备性。
因而全部三个因子的每个共轭形式均满足
$$
L(f^\sigma,1)=0,\qquad L'(f^\sigma,1)\ne0.
\tag{1080.6}
$$

## 3. 从解析非消失到实际代数秩

Dogra–Le Fourn 的已发表正文 Appendix Proposition 8 证明：
对奇水平的标准化权二 Fricke-positive 新形式，若 $L'(f,1)\ne0$，
则其模阿贝尔簇 $A_f$ 满足
$\operatorname{rank}A_f(\mathbf Q)=\dim A_f$。
这是该文明确证明的 Kolyvagin–Logachev 型定理，
不在此假设一般 BSD。

由 (1080.6) 对三个实际因子分别应用该命题，得
$$
\operatorname{rank}A_8(\mathbf Q)=16,\quad
\operatorname{rank}A_{10}(\mathbf Q)=24,\quad
\operatorname{rank}A_{11}(\mathbf Q)=33.
$$
同源保持秩，故 (1080.2) 给
$\operatorname{rank}J(\mathbf Q)=16+24+33=73$。

该文 Corollary 4 对这个完整 Heegner 商给
$\operatorname{rank}J(\mathbf Q)=\dim J=\rho_{\mathbf Q}(J)$。
具体而言，new multiplicity one 排除不同有理简单因子间的同态，
而每个实际系数域是其有理 Rosati 对称 endomorphisms；
各次数相加得到 73。
由此证明 (1080.1)，没有将旧 R45 的一个非零商误作完整 Jacobian。

## 4. 真实执行与可重建标识

- 公开 run [45934421302](https://github.com/Rogerhu12/math-research-public/actions/runs/45934421302)，
  job **140294236296**，attempt 1，结论 success。
- 源提交 **702f543eb3c3eeaac14eacfd7fa377060f4b3328**。
- 数学 consumer 完成时间 **20.665716533 秒**；
  数学总预算 600 秒、预留 30 秒。
- 脚本 [full_p47_rank_certificate.py](../scripts/full_p47_rank_certificate.py)，
  SHA-256 **7a0dc410fd88546567dc56dd086ebd4298e087483830af4bd89a72d87f9ef0ba**。
- 请求 [full-p47-rank-request.json](../notes/full-p47-rank-request.json)，
  SHA-256 **e494da5a248a81156c164409edb8c4304c10059a57aaa1bec9115edc81d07125**。
- 方法 [full-p47-rank-method](../notes/2026-11-27-full-p47-rank-method.md)，
  SHA-256 **53deb26cad2a032822362fd103bc0045d99d3daf77caa11a42a7a4eec994bd49**。
- Sage 10.6，官方 amd64 image digest
  **sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879**。
- 全部精确 q 系数摘要
  **5a1ebea80ab96b00a13c08d81f93237e1919081ed58e15a9301380b077a3de25**；
  全部导数区间摘要
  **57c7bb086b63e413e4f0fad6d77ed2930cd355a2f2ee7f5b3a8786c4666e4389**。

各因子的独立摘要如下：

| 因子维数 | q 系数 SHA-256 | 包围区间 SHA-256 |
|---:|---|---|
| 16 | 314d8c524f8bcf32891c03ebafd9c408c8b53ce584ac7a079bcf2ffe41f0f3b2 | 842c80f6934198cad787d9869a245f5fa90f435e900db9f33231564c2fae49c8 |
| 24 | 28f521ba3d11a801355d2f23b4d9ac724a95261f6b47b35969bc347001ff271c | ca34fb28080e73cb4b3ad7e7d15ef15f1d05b99984824a7d4d3eb6207826e1bb |
| 33 | 19b0cb5e104fb9cd2a8f79013b3ccce10bd8fa0b0c8ab8bbae980661001fb176 | ebd860257d84025955f9bde03f7d01f9e50975e0ae03e76f2af9750bef474cd1 |

全部实际源码、请求、两 README 和 R45 的 SHA 在请求与运行 preflight 中再次核对。
先前两次失败分别只在容器 git preflight 和 QQ kernel 的参数接口停止，
准确来源和完成范围保于
[修复回执](../notes/2026-11-27-full-p47-rank-preflight-repair.md)。
最终成功用全局 proof.all(True) 和精确 decomposition()；
没有为修接口而改用浮点或不完整 Hecke 分解。

不提交可重算的 modular-symbol 矩阵、q 数组或区间数组，
不上传 artifact/Release；上述脚本、参数和哈希给完整重建入口。

## 5. 后继必须继续支付的输入

本结果把原 full47 的 rank=genus 输入付清，
可让 R1078 的全部 trace-zero 对应在完整秩一商上使用。
它不自动支付这些对应的整格、特定辅助素数上的 degree-one 块、
Mordell–Weil 指数、实际高度矩阵、Coleman/迭代积分或深盘首项。
R1074 的完整同点 Kummer 标签仍只把全体有理点限在八个原 CM 盘，
不能与 (1080.1) 拼接成未经证明的盘内唯一性。

## 6. 文献

- N. Dogra, S. Le Fourn, *Quadratic Chabauty for modular curves and modular forms of rank one*,
  Math. Ann. **380** (2021), 393–448，Lemma 15、Definition 4、
  Appendix Proposition 8、Corollary 4；
  [DOI](https://doi.org/10.1007/s00208-020-02112-3)，
  [作者机构保存的期刊版](https://kclpure.kcl.ac.uk/ws/portalfiles/portal/147929133/QuadraticChabautyForModular_DOGRA_Accepted_26_Oct_2020_GOLD_VoR.pdf)。
  根会话已亲读准确命题与导数公式，不把括号内关于最大商的 BSD 条件
  搬到 Proposition 8 的无条件秩结论上。
- B. de Smit, B. Edixhoven, *Sur un résultat d'Imin Chen*,
  Math. Res. Lett. **7** (2000), 147–153，Theorems 1–2；
  [作者全文](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。
- P. Deligne, *La conjecture de Weil. I*,
  Publ. Math. IHES **43** (1974), Théorème 8.2；
  [原刊](https://www.numdam.org/articles/10.1007/BF02684373/)。
- 精确软件接口与球误差约定逐项链接于本次方法文件。
