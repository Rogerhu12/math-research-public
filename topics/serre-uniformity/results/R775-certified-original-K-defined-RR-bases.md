# R775：原 K 定义 Riemann–Roch 基的实际续算完成

2026-11-15，serre-public-astra-20261115。
公开仓库自己的 [run 43679160495](https://github.com/Rogerhu12/math-research-public/actions/runs/43679160495)
于 05:52:54 UTC 成功结束；本篇登记其完整结果。
原方法见 [R775 方法](../notes/R775-original-K-defined-RR-bases-method.md)，
原算术下降与模型识别见 [R772](R772-original-RR-descent-and-exact-function-recovery-certificates.md)。

## 1. 实际完成的原空间

原商曲线 $Y$ 的 genus127、原 level82、原第4号映射和 degree1206 不变。
R775 的实际半线性迹配方均定义于原 $K$，其尖点 Fourier 系数仍在原扩域中。
新的实际非零子式如下，全部在同一个原辅助素数739下计算。

| 空间 | 实际基数／秩 | 原 recipe 行子式的行列式 mod739 |
|---|---:|---:|
| $M_2$ | 146 | 344 |
| $M_6$ | 694 | 461 |
| $M_{12}$ | 1514 | 730 |

这些是 R775 的 $K$ 定义迹配方，不与 R771 的另一组子式混用。
所存行保持原 recipe，不将模739高斯消元的组合系数猜升到特征零。
R775/R772 的准确半线性下降证明，加上实际非零 minor 和已证维数，
共同认证这些原 $K$ 基。

普通幂空间 $H^0(r\mathcal L)$ 的实际维数依次为
$$
146, 418, 690, 962, 1234, 1506\qquad(r=1,\ldots,6).
$$
原椭圆主部补全给上表的 $M_6,M_{12}$。
除以原
$$
D_\star=
\left(\frac{\eta_{\rm Ded}^{12}}2-
\frac{\sqrt{-3}E_6}{144}\right)^2
$$
后，1514条配方给原 $L(2(t)_0)$，除子次数1640。
原 $q_Y=Q^3$、行列式奇数提升及两个 Eisenstein 标签的同步运输均保留。

这一步没有生成全部特征零长 Fourier 表，也没有算出原 $y$、
$\beta$ 或高度。准确短基已经由 R786 的独立后继完成；
原函数当前由 R787 的较小五次空间任务求解。

## 2. 从真实断点继续，没有重跑已完成阶段

旧 run43631335355 于预算后返回 exit124，最后的 power6 为 partial，
已完成的 M2、power2至5、determinant cosets 和12个种子移像文件均已保留。
本次绑定同一个算术 core，复用这些原文件及 power6 游标后继续。

root 下载实际新 ZIP，核 ZIP 与完整 manifest 的 SHA，再逐项核32个文件的
字节数和 SHA。旧 resume receipt 中18个 `complete:true` 文件在新 ZIP 中
逐字节 SHA 完全不变；原 partial power6 现已完成。
这只是文件完整性与原源码核对，没有本地重算数学。
最终证书列出25个完整阶段，公开 job132705807293 的计算、临时转交、
小回执发布与最终 verify 均成功。

## 3. 固定源与输出绑定

源提交：`032899cc3bcd937497a857df0c271261fc709ae5`。
原算术 core SHA256：
`8b02496a1809e1f11e90bad84df1a4fa3a39ac6ad615f7871115b0988d2af4ee`。
执行环境为本公开仓库 GitHub Actions、Python3.12、python-flint0.9.0。
实际原输入、续接来源及预算参数见
`notes/R775-public-K-defined-RR-bases-request.json` 和本 run 的输入回执。

| 输出 | SHA256 |
|---|---|
| 临时 ZIP，artifact14148883593，25587380 B | `a902a34432a26ff817443c859bd1f6d50953d9bc8800e8dad19c84966677597d` |
| 完整 manifest，32文件 | `c563b43979633152cf2dd58bc7127a0bd138edf3cccef6b51ba629b4851d6906` |
| 完整基证书 | `ce92a3aacd8a1c6f44bef82b6890bb00298d9b1ea1fc2b8caf1af1cce7c1d203` |
| 完成 power6 阶段 | `05c5580b73eeba72b832e2a871221c19c482baf1c9656cab62a0c2c694ffafa1` |
| 完成 $M_6$ 阶段 | `70ff7536b50bf99ffb422b7c17dd320b535738fcfcc562fd1597eebcb7a0b299` |
| 完成 $M_{12}$ 阶段 | `53a1e72457e4d414889de942d5268d7e800f94b583996f931901dccb0fdc720f` |

小元数据在 `computations/R775-p41-original-K-defined-RR-bases/43679160495-1/`。
完整表和证书不入 Git 或 Release；一日临时断点供当前备用输入转交，
2026-11-16 05:52:45 UTC 到期。

R777 的真实生产者绑定现已齐全，但其大规模 $M_6/M_{12}$ 准确展开方案
保持备用，未触发。当前直接执行 R786/R787 的129阶原函数恢复。
这个完成项不重开原 p41 有理点分类，也不改变全 $p$ 一致性及真实高度的未完成状态。
