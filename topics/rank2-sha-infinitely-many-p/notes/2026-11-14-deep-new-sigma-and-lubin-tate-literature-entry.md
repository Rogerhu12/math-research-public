# 2026-11-14 — 新 sigma / Lubin–Tate 文献入口与已读范围

这是检索记录，**不编号为研究结论，也不替代原 J′ 或 forcing 的证明**。

## 1. Kobayashi 的 2026 supersingular 系数讲座

官方 [Number Theory Days in Tokyo 日程与摘要](https://www.ms.u-tokyo.ac.jp/~kelly/NTD2026/program.html)
列明 2026-07-04 Shinichi Kobayashi 的报告
“p-adic aspects of the coefficients of the Weierstrass sigma function at supersingular primes”。
已读官方摘要：报告涉及 supersingular sigma 系数的更精细赋值估计、
同余及 Eisenstein 特殊值的 supercongruence。
官方网页没有给出相应定理的准确公式与全部假设，
因此本课题尚未使用这些口头结果改善 R303/R402/R469 的界。

[官方录像索引](https://journal.ms.u-tokyo.ac.jp/video/conference/2026Number_Theory/index.html)
在此次公开抓取中超时；没有读取录像或据其断言公式。

## 2. Katagiri–Kobayashi 新预印本

Yu Katagiri、Shinichi Kobayashi，
[p-adic properties of division polynomials and algebraic sigma functions](https://arxiv.org/abs/2609.07024)，
arXiv:2609.07024，2026-09-07。

此次已确认作者、标题、日期和 arXiv 摘要。
摘要处理固定局部域上好约化椭圆曲线的 division-polynomial
p 幂子序列极限，包含 ordinary 与 supersingular 情形，
并用 prime-to-p torsion 的 Teichmüller 提升对应的代数 sigma 值描述极限。

**尚未取得全文。**
公开 arXiv abs/html/pdf 抓取返回 DisabledError；
作者主页没有挂这份新稿，另一 HTML 索引明确尚未生成正文。
因此未声称逐定理核过它，更未把 division-polynomial 值的极限
认作本题指定 Taylor prime diagonal、完整中央导数或同一 α/β forcing。
后续若取得正文，需先支付这三种对象之间的实际身份。

## 3. Katagiri 的范数新稿及可读的 Ardakov–Berger 前置

Yu Katagiri，
[Norms of Schneider--Teitelbaum Polynomials in p-adic Fourier Theory](https://arxiv.org/abs/2609.20002)，
arXiv:2609.20002，2026-09-17。
目前只读摘要：它给未分歧二次局部域的相应局部解析 Banach 范数，
并使用 Ardakov–Berger 的系数赋值公式。尚未取得此新稿完整正文。

已经读取的前置是 Konstantin Ardakov、Laurent Berger，
[p-adic Fourier theory for Q_{p²} and the Monna map](https://perso.ens-lyon.fr/laurent.berger/articles/ValPol.pdf)，
现刊于 [Confluentes Mathematici 18 (2026), 71–79](https://cml.centre-mersenne.org/articles/10.5802/cml.105/)。

该文 Theorem A 的坐标准确固定为
$$
\log_{\rm LT}(Z)=\sum_{j\ge0}\frac{Z^{p^{2j}}}{p^j},\qquad
\exp(\Omega\log_{\rm LT}(Z))=\sum_{n\ge0}P_n(\Omega)Z^n.
$$
若 $n=\sum_i n_i p^i$，则其证明给
$$
v_p(P_n(\Omega))
=\frac{p}{p^2-1}\sum_i n_i p^{-i}.
$$
文中明确说明一般系数的赋值依赖所选坐标。
在 $n<p^2$ 的范围，$P_n(\Omega)=\Omega^n/n!$，
可直接用阶乘赋值核对该公式。

这是真正 LT character 的系数公式。
原 $\Theta_{\rm reg}$、完整 sigma 来源、Gaussian 三块和中央 Mellin
不是仅凭名称就能换成这个 character。
目前没有支付使原 α/β 矩阵或 prime diagonal 继承该精确赋值的身份。
全函数范数或一组 norm-one 基也不单独证明指定中央导数非零。

## 4. 与当前工作的关系

R534 的双接触证明独立于上述未读新稿，已经在原有限目标中完成。
当前高 b 镜轴/三层修正仍使用同一 η、原低行高尾和全部 M carry。
本条只保存可继续检索的原始入口，未关闭 O3 或 O8。
