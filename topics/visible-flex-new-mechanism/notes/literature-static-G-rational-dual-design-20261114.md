# 单 G 原式 7/8 子式 consumer

日期：2026-11-14。**实现设计，尚未执行本次新 Python 源码。** 研究只在公开仓库 Actions。

## 1. 具体目标

[R117](../results/R117-static-weight-one-reduction-and-reciprocal-costs.md) 从已发布完整块和 R114 证明

$$
[\ell_{\mathrm{norm},+1}(S)]
=h(k^3-k)[G].
$$

因此重复对旧 206 项代表做 word 消元没有新信息。新入口只问：完整权一响应真上界为 7 时，原函数 $G$ 是否有一个 $7/8$ 非零有理评价子式？

成功只证明 universal $G\notin\mathcal R_8$，再由 R117 的真实正整圈配平导出对应实际商成本的结论。失败或模控制秩不足保持不确定；有限模拟合不授正面函数身份。

## 2. 冻结来源

新脚本 scripts/literature_static_G_rational_dual.py：

- 16444 bytes；
- SHA256 0872f0fc8b561a547342d530239e35c6ac9a37a5bddc5c472bf16c0df73ac477；
- 未挂 blob 910036e8968f4be8ecd8028b0a0626450ca23ba5。

依赖只复用已有接口：

- 旧 producer 9aa5b136… 保持不变；
- 新输入/报告 helper literature_constrained_static_fourth.py，814e1338…，本 job 的人工检查会一起支付其尚未执行的人工门；
- 真实 publisher helper e66bf0d2…，只验输入，不运行 m8 投影；
- 原有理多项式 evaluator SHA256 6bf16dd5c6cc8157fd53b20b58b504a5c3ea56ade9db9b62a30d385e5e69fd22；
- 完整两个模式响应使用已发表 blocks.full_response 与原 exact.operator_basis，不交换第三算子的外槽和内槽。

本入口没有调用任何 W、局部密度、旧 forcing、constant target 编译器，也不使用不完备 word 代表评价数值。

## 3. 输入与上界证据

默认直接读取 run 43645177423/source 2f1b809c0b0abb7a26303d36940edc203815f872 的已存 full original export。原 main、publisher receipt、packed/raw SHA、全部旧语义源与每个根 hash 均核；fallback 缺 run/source 时只从真实终端 receipt 继承。

额外绑定 local-fourth-quotient-weight-+1.json 的 13499 bytes 与 SHA：

57d8a80b8344f42cd8594e7d117d29098991d1c392d3101264195eeb1a8533c4。

核其全部八列与完整 E8×W36 权枚举一致；已证明的原式依赖是 col6=-col1+col3，故保留 [0,1,2,3,4,5,7] 给真实上界7。没有以模素数小秩代替特征零上界。

$G$ 按几何键 $(1,3,0,0,0,0,0,0)$ 从原式导出取出，再作线性权一投影；两模式 SHA 必须与公开回执完全相同。

## 4. 真右端原函数与证书

固定 $\xi\in[2,3]$、$t=\xi-2$，

$$
f=[t(1-t)]^8,\qquad
g=f(1+2t+3t^2+5t^3),\qquad q=f+ig.
$$

在共同较大物理带上把二者外延零。所有列、两个模式、全部点使用同一个 $f,g$。这是有穷正则有理测试对，没有先施三矩，也未宣称是 $C^\infty$ 圆。

原始 profile DAG 用真实 signed right primitive $I=\int_3^\xi$ 评价；既不补零左尾，也不去掉未满足的右端边界项。完整响应直接在多项式代数中代入原 W 的外槽/内槽公式。

默认 prime=2147483647，24 个内部有理点、两模式及实虚部给96行；检查所有遇到的有理分母可逆。只有七列模秩7且增广8子式非零时才输出 rational_nonmembership_certified。

特征零泛函按原有理矩阵定义为

$$
\mathrm{ev}_{\rm last}
-\mathrm{row}_{\rm last}(A)A_{\rm pivot}^{-1}\mathrm{ev}_{\rm pivot}.
$$

报告的模系数不是该有理泛函的字面系数。非零模行列式仅证明这个真实有理行列式非零。

因为 $G$ 与控制空间有已证 universal 整权分解，成功可升级为 universal $G\notin$ 完整 $\mathcal R_8$；不能据此说当前一个多项式测试对上不存在其他权响应的偶然相消。同一合法三矩圆的忠实评价及真实成本结论按 R114/R117 的独立证明处理。

## 5. 有界运行与输出

默认总120秒、RSS软轮询1024MiB、多项式最大次数256、操作计数上限10000000。主报告<90KB，完整报告先存 gzip，上限2.5MB，总输出4.8MB。主报告保 source/run/completion、原输入和完整证书的核心 checkpoint；完整报告保评价标签、原列身份、模式多项式 hashes、分母清单与 Cramer 证书。

文件：

- static-G-development.json 及其 complete-report.json.gz；
- static-G-rational-dual.json 及其 complete-report.json.gz。

顺序 CLI：

python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_static_G_rational_dual.py

python topics/visible-flex-new-mechanism/scripts/literature_static_G_rational_dual.py --toy-only --output /tmp/static-G-development.json

python topics/visible-flex-new-mechanism/scripts/literature_static_G_rational_dual.py --output /tmp/static-G-rational-dual.json

人工检查包括原多项式右锚与准确子式、R114 的有理矩阵和报告gzip、一个保外槽不对称的人工三线性算子在两种完整相位公式中的一致性。人工通过后才跑真实原式评价。无新几何搜索，无新增默认预算。
