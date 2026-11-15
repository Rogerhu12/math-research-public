# R806：原正规基中的 primitive 乘法已准确认证

## 1. 结论及证明范围

沿 [R805 两仿射图与原整基证明](R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)、
[R805 实际自由基](R805-certified-original-affine-pencil-free-basis.md)及
[R806 执行契约](../notes/R806-original-primitive-multiplication-and-cyclic-certificate-method.md)，
本次实际选中的第零候选为
\[
 \tau=e_0,\qquad \sigma=e_1+e_{73},\qquad
 z=\sigma/\tau,\qquad w=w_0/\tau,\quad \boxed{w_0=e_2}.
\]
这里的 \(e_i\) 全是原 \(M_2\) 保存顺序中的截面；\(w_0=e_2\) 是成功产物的实际值，不是预先假定。

在原秩 \(272\)、分次分布 \(1/144/127\) 的正规自由基 \(\beta_a\) 中，
全部乘法列已经准确恢复：
\[
 w\beta_a=\sum_{b=0}^{271}(M_w)_{ba}(z)\beta_b,\qquad
 M_w\in\operatorname{Mat}_{272}(\mathbf Q[z]),
 \qquad \deg(M_w)_{ba}\le1+\epsilon_a-\epsilon_b.
\]
矩阵约定为输出行 \(b\)、输入列 \(a\)。所有越过带权次数界的系数均准确为零。
每一列均在原 \(690\) 维 \(S_3\) 基中求解，并验证全部 \(41\times20=820\) 个原有理坐标；
没有把它改成同维的旧 \(R786\) 系数基。

实际循环见证为
\[
 \ell=1000000007,\qquad z_0=0,\qquad
 \det[\,1,M_w1,\ldots,M_w^{271}1\,](z_0)
       =489861234\pmod\ell\ne0.
\]
故这组幂在特征零函数域中线性无关，\(w\) 是原函数域相对 \(\mathbf Q(z)\) 的 primitive 元。
原正规整基始终保留；没有声称幂环 \(\mathbf Q[z,w]\) 已整闭，也没有计算特征零 \(\mathbf Q(z)\) 上的巨大 Krylov 逆。

这条结果完成原乘法输入。真实 \(A/B\)、五个函数的全部极理想、主函数 \(\eta\)、高度和主 Serre 一致性目标仍须后继完成。

## 2. 实际公开执行与准确验算

| 项目 | 本次实际值 |
|---|---|
| 公共仓库 | Rogerhu12/math-research-public |
| 原计算 run / job | 43707290840 / 132791001049 |
| 原 source commit | 75b1d56c821abe34660477ba8b4c7f7b75a4382b |
| 候选索引 / 公平搜索对角 | 0 / 0 |
| 候选 recipe | original_M2, index 2 |
| 原 \(\sigma\) 参数 \(n\) | 1 |
| 原 \(M_2\) 整数尺度 | \(82^2=6724\) |
| 原 \(S_3\) 基整数尺度 | \(82^6\) |
| 固定原选行维数 / 完整验证行数 | 690 / 820 |
| 准确右端 / 分组 | 272 / 34 组，每组 8 列 |
| 原 core elapsed seconds | 4725.462437718001 |
| 最终原步骤及冻结 wrapper.verify | 全部 success |

组 000 至 017（列 0 至 143）各在 **184 个 \(\ell\)-进 Dixon 位**完成；
组 018 至 033（列 144 至 271）各在 **432 个 \(\ell\)-进 Dixon 位**完成。
这里的“位”是原算法的 prime-adic lifting digits，不是十进制精度。
各组均经过严格矩形界的有理重构、全部 820 行准确等式、带权支撑及对成功模乘法的还原核对。
实际清分母后的列分母十进制长度在第一批最大 792、后一批最大 1921；不把这些大分母省略为整数矩阵。

全行等式的充分性沿已证 \(V_3\) 截面次数 \(816\) 与 \(820\) 个坐标的注入界。
新乘积确由原截面生成，原 \(82\) 的幂、已选 \(\tau,\sigma\) 及原 \(S_3\) 行全部绑定；
因此不是对有限 q 前缀的经验拟合。循环见证在分母为单位的实际素数处非零，
并与准确重构后的同一乘法矩阵一致，故确实证明特征零循环性。

## 3. 冻结源码与参数

所有脚本及参数均位于上述 source commit；重现时使用该提交的原 request，
不替换已完成的 R805 选行、秩或原产品前缀。

| 已提交来源 | SHA-256 |
|---|---|
| scripts/R806_original_primitive_multiplication.py | b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d |
| scripts/R806_public_original_primitive_multiplication.py | b199f04098d2f0b99810f55d93e43af40e58195f393626ea2b1ce03a930b2a8e |
| notes/R806-original-primitive-multiplication-and-cyclic-certificate-method.md | e73f66bd2e4836389dfbf64d5d724ada725944e80233a33e493408971a4242c1 |
| notes/R806-public-original-primitive-multiplication-request.json | 8ab0ac3aff10e81744d7b9e1f51e5d614a82debaada6f6f3e002075c3594de3f |
| .github/workflows/serre-p41-original-primitive-multiplication.yml | 2231a2f74f87f0011fdb94c90835703eb9901b9458f343b1c209bd9352fcf586 |

来源的两组原生产者是 R805 run43705580592/source9f960b8e0b2fa825ab1391e86db4e1383ffdd700
及 R786 run43682100611/sourcedd262672a8b1e2af82277b15e0fa766038609670。
其原证书、manifest、receipt、源代码 SHA 和原 basis/alias schema 均经本次完整 IO 核对。

## 4. 产物身份及完整纯 IO 审读

原产物 artifact **14161637987**，203879878 bytes，ZIP SHA-256
`2f894721e5c657e6f33f304646e55bc3e4ad41fab8bb98495cc7b40db3e26759`；
一日活跃保留至 **2026-11-16 12:25:28 UTC**。
全 ZIP 为 10605 个文件，其中原完整 manifest 列出 10603 个文件；stage manifest 列出 10595 个原 stage。
纯 IO 审读把所有 manifest 的 bytes/SHA 与 ZIP 原字节逐一比对，没有执行任何新增数学计算。

| 原产物项 | bytes | SHA-256 |
|---|---:|---|
| p41-original-primitive-multiplication-certificate.json | 14965 | dd266ee6d46dab53be5cb73553af56a3cb96d6b2cd0459aea79d6e4ebf06ba99 |
| full-outputs-manifest.json | 3988631 | cc569ea17dba9685334fdeeec056ee8a21fe53dfa334be9173afbdcfa0629f69 |
| R806-stage-manifest.json.gz | 512678 | 0b32cfba77138d2fadea50bc922376c9199babb5aa6b7206781d9f030874c652 |
| R806-accepted-primitive-candidate.json.gz | 3904 | 2aac2d669a6f6889d4c84e357cb82aae1e27bcd4fecf43a846ffe5ac7822ce27 |
| R806-candidate-0000000000-definition.json.gz | 3548 | 715faab78be54e3cf91958d0895c8c8d0157d752414feab775cc499859616170 |
| R806-candidate-0000000000-prime-1000000007-z-0-cyclic.json.gz | 374731 | 6d6722d93321e757535fe96f9d3ecc181ac85dc65d67d4bda41a6477ab84f5e8 |
| R806-exact-polynomial-multiplier-in-original-normal-basis.json.gz | 10847 | 63b38d14dbeb4b504619db65f56c151146885173b8cef253dfba3bebc76cd2dd |
| R806-original-input-and-coordinate-chart.json.gz | 45370 | 839b29f9042937529b23699dc6bcad4d669f25108d472887718c77e617120c5b |
| R806-prime-1000000007-fixed-minor-inverse.json.gz | 2410124 | 32dec0fae4a8f6878e5e962d96960fdee7352cff9a5b03617ae2041e59dbd937 |
| R806-retained-producer-inputs.tar.gz | 52120797 | 4c0e1c8448386e412d85de2405de190c32c4879912a906360f6f6031e4fbe9e5 |

原 carrier 含 **2580** 个未改文件：R786 1260、R805 1320。其每个成员均按各自原 manifest 核对，
再用 source commit 的原 wrapper.select_original_inputs 复核选择集合及全部 source/schema。
随后执行未改动的原 wrapper.verify，返回 0；未 import 数学 core 或 flint，未重算 \(M_w\)。

完整纯 IO 审读 run **43714843253**、job **132814017216**，
source **9651443bdb3b230762eb38e95cad28adef93af94**；
审读脚本 scripts/R806_public_success_io_audit.py 的 SHA-256 为
`c4f9f2a6627172dc391b365766555c5d799c32d8f0ed51b48c200b72bea56f15`。
其 52010-byte 摘要 SHA-256 为
`4d12368f1fccdba3d22c93efd16cc6409009f526cf90a80f103d10b9549b5fcf`；
摘要含全部 34 组的原文件名、字节数、SHA、实际位数和分母长度，原大矩阵不打印至日志。

必要未改后继文件在 audit artifact **14162500418**，
109619510 bytes，ZIP SHA-256
`0639c595ee520703de250e106f710ae0984521d5366f52d58c027f9087e08729`，
至 **2026-11-16 12:38:24 UTC**。
其中 selected-original-R806 提供 R811 所需的实际 \(M_w\)、循环见证与源身份；
R813 直接读取原 R806 artifact 内的旧 \(R805/R786\) carrier 和固定模逆，
不要求再次下载更早的独立原产物，也不重新选择基或求逆。
所有 raw、原证书和大坐标仅留必要的一日活跃 artifact，不入 Git 或 Release。

## 5. 已确定的直接消费者

[R813 原 Wronskian 方法](../notes/R813-original-two-S3-Wronskian-derivation-input-method.md)
现在有真实 \(\sigma=e_1+e_{73}\)、\(w_0=e_2\)，可准确生成
\(G=\tau D_0\sigma-\sigma D_0\tau\) 与 \(J=\tau D_0e_2-e_2D_0\tau\)。
只需读取原 M2/V2 的实际支撑 \(0,1,2,73\)，旧 \(\tau e_i\) 不重算；
同一 690 选行和已认证的固定模逆用于两个真实 S3 右端。

[R811](R811-original-normal-polar-ideal-preimages-and-two-chart-certificates.md) 的 \(M_w\) 依赖已满足；
原 \(A/B\) 仍待 R787 成功及 R809 原坐标后才能激活。
后续有限域专化 Krylov 与准确 commutator 验证必须保持这一个原正规整基，
并保留原字段/Norm/三同源/刚性化全部常数。上述完成输入不代替完整极理想或主定理。
