# R131 续篇：完整三阶清分母证书与真实十分之一延拓

2026-11-13，visible-exact-astra-ac0d。

**已证明：同一原目标、同一原腰初值、全部
\(\eta\in[-10^{-9},10^{-9}]\) 的真实 Codazzi Cauchy 解延拓到
\([0,1/10]\)。** 本结论给出完整连续误差和实际一阶导数控制；
它没有把这个更长区间宣称为已经证明嵌入的环带。
先前 R132 的嵌入区间仍为 \([-.07,.07]\)。

与此同时，完整 \([0,1/5]\) 的实际三阶目标、清分母多项式残差
已经运行完成。对这一完整区间使用原 R131 统一误差管的请求
**失败**；失败的全部输入、已通过行和失败门另行保留。
有限候选、连续残差证书、通过的解区间是三个不同的断言。

## 1. 同一个完整目标与完整有限输入

目标仍为
\[
g_0=E(r)\,dr^2+a(r)^2\,d\theta^2,
\qquad
\delta_*=-\frac{7789843107295549}{4611686018427387904}.
\]
\(E\) 是原真实候选的完整 \(|F_r|^2\) 角平均，包括原无限
primitive 余项；没有替换成有限采样平均。原参数宽度仍为
\(10^{-9}\)，全部角圆周仍被覆盖。

本次使用完整 1024 角有限候选的全部 283 个七次径向片段，
含实 mean、全部正频率及其准确共轭负频率、准确共享端点。
原完整 gzip 的 SHA256 为

    da1dcc9e5dbeff97998023db376c9e0c3fcfae48639cc1639dba57c7494c91a3

它由
`notes/2026-11-13-codazzi-dense-r02-n1024-candidate-shards.json`
声明的全部八个 byte shards 无损恢复。消费者逐片核查压缩字节、
解压 payload、区间偏移、完整原字节及所有数组；这种分片只改变
存储方式，不删任何频率、radial coefficient、mean 或接缝。

[三阶方法](R134-supplement-true-cubic-target-and-complete-sharded-residual.md)
先在完整有限多项式层面对两条 Codazzi 残差清分母，保留抵消，
再支付真实 \(K,\gamma,\beta\) 的三阶 Taylor 余项。
真实 \(F_0,\ldots,F_5\) 与 \(E^{(4)}\) 支付
\(K^{(3)},\gamma^{(3)},\beta^{(3)}\)；全部参数和 primitive
尾仍在这些系数中。有限 Fourier 乘法网格为 4096，闭角 cells
为 8192，最大的径向 numerator 次数为24。

完整运行覆盖 \([0,1/5]\) 的全部283闭盒，耗时2426.16秒，
`complete=true`、`failure=null`。原 native 为

`notes/2026-11-13-Codazzi-cubic-cleared-r02-n1024-v1-native.json.gz`，
SHA256：

    92db89ea9640edbeebcbbe871d8383d13c0e3b107478a1fd8641c7aab07555e5

其 producer 和每个 source/input/dependency 身份仍保留；没有把
新 cubic kind 改名成旧 quadratic kind 以绕过旧输入门。

## 2. 原统一误差管在全区间的实际失败

独立新消费者
`scripts/fourfold_codazzi_cubic_C0_continuation.py`
核查上述新 kind、完整覆盖、所有 SHA，以及独立真实腰的加权
导数输入后，才把数学上相同的 bound fields 传给原 R131 kernel。
原初始加权导数来自真实腰曲率公式，不是候选的导数误差。

在固定未加权管 \(T=1/16\) 中，各原闭盒使用
\[
A_0=\gamma_*D_1+|\beta|_*(1+3(\widehat M+T)^2)
                                      +2|\kappa|_*.
\]
R131 的严格仿射上解满足
\[
e_{i+1}>e_i+h_i(A_0e_{i+1}+\rho_0).
\]
所有量均由向外有向算术计算。

从零数起，第151行仍全部通过，覆盖端点为
\[
r_* =\frac{7566047373982433}{72057594037927936},
\qquad e(r_*)<.059473413.
\]
第152行给 \(e<.065570261\)，超过 \(1/16=.0625\)。
该行的正 \(k\)、严格 gap、仿射 margin 及有限真实梯度门均仍
通过，失败门准确是 `C0_inside_tube`。这不证明真实解在此
失去正则性，也不证明不存在更好的上解。

完整失败报告为
`notes/2026-11-13-R131-cubic-cleared-r02-v1-C0-native.json.gz`，
SHA256：

    d65c965235ba9ed2b5cd8bab2ec9b96e003ad5f4d6bccffdcdd7b72d4bfe3e41

该报告及其 producer 保持原样；不存在以新通过报告覆盖旧失败
或把全 \(.2\) 请求标成通过的操作。

## 3. 直接限制同一原闭盒得到严格 \([0,1/10]\) 结论

另一个明确的消费者
`scripts/fourfold_codazzi_cubic_C0_prefix.py`
接受一个位于完整 native 内的有理右端点。它保留所有原 bound
fields 和真实 scalar germ，仅在最后一盒把积分长度缩到所请
端点。原闭盒上的完整上界仍是该闭子盒的上界，故不需要重算
残差或目标几何。

该限制是传给 R131 kernel 的局部参数对象，不改写原 native。
kernel 仍逐盒核查严格相邻、真实 germ 包含关系、最终准确端点、
所有严格 margin、正 \(k\)、实际 gap 与实际加权梯度。
该新消费者的 SHA256 为

    f61691c6c415f720e2ed1f123dfdc9ef61bec16cb5f870a802e653fcc75197ba

全部145个实际闭盒通过。向外舍入后的结论是

| 同一真实解的量 | 已证明的界 |
|---|---:|
| \(\max(\|p-P\|_\infty,\|q-Q\|_\infty)\) | \(<.037014676\) |
| \(q-p\) 的统一下界 | \(>.16819229954\) |
| \(k=\sqrt{-K}\) 的统一下界 | \(>.80669343284\) |
| 终点实际加权梯度 \(\max\{|(p-q)p_\theta|,|(p-q)q_\theta|\}\) | \(<386.628953\) |
| 全区间实际角一阶导数 | \(<2298.731592\) |
| 实际加权梯度输运系数的积分 | \(<.557552021\) |

这里的实际导数控制由
[R131 的准确线性加权输运](R131-linear-degenerate-weighted-gradient-and-C0-continuation.md)
得到。没有读取候选二阶导数、残差角导数或 R134 的 Sobolev
误差门来替代这个结论。

因此原局部经典解可沿同一严格负曲率 chart 连续延拓到
\([0,1/10]\)。准确 Gauss–Codazzi 与 frame 重建仍由
[R126](R126-exact-Codazzi-reconstruction-and-continuation.md)
的同一初值与周期性机制消费；本篇不另选初始曲线或度量。

完整通过报告为
`notes/2026-11-13-R131-cubic-cleared-r01-v1-C0-native.json.gz`，
SHA256：

    a1aafc61cebae71b7829a099ce38d682677c6a9523b472681e874d97a723de7b

newton_source 独立核查了限制后的 kernel 调用、全输入身份、
真初始梯度及原失败保留规则：缩短长度不改变上界的有效范围，
通过范围没有被挪到尚未通过的 \([0,1/5]\)。

## 4. 重现与未付费用

在本题目录使用新的输出路径执行：

~~~bash
python3 scripts/fourfold_codazzi_cubic_C0_prefix.py \
  --native notes/2026-11-13-Codazzi-cubic-cleared-r02-n1024-v1-native.json.gz \
  --right 1/10 --out notes/R131-cubic-prefix-r01-reproduced.json.gz
~~~

以上是同一真实 Cauchy 分支的存在、连续误差和实际一阶导数
结论。更长环带的全角位置、normal 支持、全域嵌入、曲率和
自距离仍需另证；跨根、真实非线性正帽与无限尾的全部 mean/
regular 匹配也未由此完成。最终共同度量闭面族的可见位移、
固定 H、含反射非全等和 reach 必须在同一最终族上另行兑现。
