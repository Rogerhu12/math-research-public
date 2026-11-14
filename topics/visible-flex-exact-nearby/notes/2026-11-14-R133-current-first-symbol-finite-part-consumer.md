# 当前完整 moving 首符号有限部的公开消费入口

本条执行
`results/R133-supplement-complete-moving-first-symbol-and-root-subtractions.md`
的精确 \(\Xi\) 积分。对象是原 ac1 M32 候选的完整连续值修复定义
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`，
参数为 \(\eta_0\)、原精确 \(\nu_0\)、显式族 \(\delta=0\)。
它不把该积分先称作真实完整返回的 \(\beta\)。

## 完整输入与严格积分

全部 169 个原 high7 scalar germ、全部候选五片、原精确修复定义及
当前物理根复 germ 都按原 SHA 读取。没有重算两条 ray、返回共轭或
原 scalar cache。只在同一实际 root piece 2549 中重新用完整 Arb
Laurent 指数 provider 计算必要的根 jets；原无限原函数余项仍支付。
原 target JSON 及其两个实际 NPZ 输入也须精确检出，不能因为此次
只求根就省略它们。

普通严格区使用同一 candidate/scalar/compact-germ 公共细分。
每个闭格从原 high7 Taylor 恒等式取真实点 jet 和完整格上导数界，
不是对一个无结构的值误差求导。有限三次中心在每片准确求导，
全部连续修复常量保持。所有 Fourier 输出用于
\(\langle u^2\rangle,\langle v^2\rangle,\langle u^4\rangle,
\langle u^2v^2\rangle,\langle v^4\rangle\)；
\(\langle uv_\phi-vu_\phi\rangle=-4\sum_{j=1}^{32}j u_jv_j\)。
均值留在 \(v\) 和 \(\eta=-\gamma m\) 中。

若 \(F=\langle\Xi\rangle\)，格中心 \(c\)、半长 \(h\)，
则原点 jets 与完整六阶导数给

\[
 \int_{c-h}^{c+h}F(r)dr
 \in\sum_{n=0,2,4}\frac{2F^{(n)}(c)h^{n+1}}{n!(n+1)}
 +[-1,1]\,\frac{2h^7}{7}\sup_{[c-h,c+h]}
                                  \left|\frac{F^{(6)}}{6!}\right|.
\]

\(F\) 含 \(q_r\)，所以所需最高原标量阶为 7，恰由保存的真实
完整 high7 身份供应。未使用第 8 阶。未通过分配误差的格只作
精确二分，原失败格和完整已成前缀都保存。

## 真根与解析有限部

唯一根的原全参数包围包含 \(\eta_0\)。对本次固定 \(\eta_0\)
用完整 \(K\) 与整区间 \(K_r>0\) 做有向均值 Newton 收缩，保留
每个实际包围；目标根宽 \(2^{-140}\)。根 cut 初取原根下界减
\(2^{-18}\)，它和实际根同在原 PPoly/scalar 片内。

令 \(\rho=r_*-r\) 及
\(k(\rho)=-K(r_*-\rho)/\rho\)。根等式严格来自已证唯一真根，
不用把一个包含零的浮点 K 球直接设置成零。准确有

\[
 k^{(j)}(\rho)=(-1)^j\int_0^1t^j
                     K^{(j+1)}(r_*-t\rho)dt,
\]

因此 normalized jets 可由同一完整根片的
\((-1)^jK^{(j+1)}/(j+1)!\) 包围，至 \(j=6\) 仍只需 K 的第 7 阶。
根分解使用原证明的四个解析系数
\(\langle\Xi\rangle=A\rho^{-5/2}+B\rho^{-3/2}
+C\rho^{-1/2}-D\rho^{1/2}\)。

消费者分别保留 A 至 5 阶、B 至 4 阶、C 至 3 阶、D 至 2 阶，
逐项准确积分包括两个负次幂的有限部。若真根至 cut 长为 H，
剩余四项的总费为

\[
 \frac{H^{9/2}}{9/2}
 \left(\sup|A^{(6)}/6!|+\sup|B^{(5)}/5!|
             +\sup|C^{(4)}/4!|+\sup|D^{(3)}/3!|\right).
\]

所有 sup 都在完整真根片上取，未用拟合系数推导余项。
根减项准确为 \(g_0=A(0),g_1=A_\rho(0)+B(0)\)。
严格区和根有限部在同一个准确 cut 相加，不遗漏中间小片。

## 执行和科学边界

`scripts/fourfold_codazzi_first_symbol_finite_part_CI.py` 先核全部
manifest 字节和实际 runtime，再启动一个真实数学子进程。
它区分 workflow event commit 与实际 scientific checkout commit。
所有 source、完整输出、原始 prefix、拒绝细分、正常及失败退出均保存。
本地只作源码编写、静态语法检查和 SHA 操作；数值门由公开 Actions
真正运行后才有可引用的结果。

目标整区间宽为 \(10^{-3}\)。达到该宽也只证明这里的同中心
\(\mathfrak X\) 及其准确缩放值；完整 Airy 两行、positive regular
图、Maslov、实际非均值正规形、strong 余项及未知 PDE 背景的相位
费用仍须接线。R31 所选未知 \(\delta_*\) 也未免费代入本次固定
\(\delta=0\) 积分。
