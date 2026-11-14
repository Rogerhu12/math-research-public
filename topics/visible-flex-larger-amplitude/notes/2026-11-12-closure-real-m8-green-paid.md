# R29 的真实 M8 整头部 Green 与相对 1/500 修正球

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**状态：已完成、已在更换后的执行器重新生成的区间计算。** 这是 R29 的一个实际有限频窗应用。它包含完整 mean，但只对明确的辅助8模点态投影边值问题给出存在性，不宣称全频无限尾、原worker的压缩Galerkin问题或完整闭曲面已经完成。

## 1. 同一个实对象和实际参考

背景是 R26 的固定新有理深 g：0..159全部保存参数与 global warp alpha 保留，n≥160源alpha=65/64。范围是physical node225到node12，包括胞元224..12；node12的真实半径来自同函数区间积分。保存的二进制node12 Q2..Q16仅作为八个准确dyadic边界坐标。

对每个m=2,4,…,16，使用R18准确线性深图的斜率区间，传播真实线性方程，并用浅高度归一。整胞元包围逐模、逐分量取sup，再求R23强范数，不由两端点估计中间路径。线性参考只有八个非均值模，但其R23非线性源及holonomy小根包含全部Fourier频率。

原始输入是已推送的
`2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive` ready/response，有限源条件由`closure-wide-strip-head-ledger-paid-source.json`核销。源码和输入的完整hash都写入结果。

## 2. 已支付的真实整胞元预算

M8恢复运行session3196正式exit0，13.609808773秒、峰67660KiB（含输出序列化），2227个panel。213个胞元全部通过R23球。

$$
X_{12}^{\rm ref}\le8.977875266293333\times10^{-38},\qquad
\log_2X_{12}^{\rm ref}\le-123.06689355334580.
$$

$$
\max_n X_n^{\rm ref}/\mathfrak r_n
\le2.930127733329069\times10^{-11},\qquad
\sum_n B_n(X_n^{\rm ref})^2
\le1.284487836167985\times10^{-51}.
$$

这里十进制均向保守方向显示；证明用JSON所存向外dyadic端点。全部cell矩阵、反向majorant、参考sup和准确浅高度图的非零性已经保存，当前不借用旧未归档源码的M1/M8原型。

## 3. 完整源的低频响应

Green恢复运行session5469正式exit0，2.840219275秒、峰57204KiB。准确连续momentum是P=μ_n Xi_n。R29的两端基本列给非零Wronskian；程序按完整cell核而非单向Cauchy最大增益求矩阵Γ。

对R23的完整非线性源在这八模上的投影，令

$$Y_k=\sum_n\Gamma_{kn}B_n(X_n^{\rm ref})^2.$$

结果给

$$Y_{12}\le1.765386639431843\times10^{-40},\qquad
\log_2Y_{12}\le-132.05713961103262,$$

以及准确的统一常数

$$
\eta:=\max_kY_k/X_k^{\rm ref}
\le3159843714651572576465137747092799057133187720535785487121\,2^{-200}
<0.001966375571193024.
$$

Γ使用对角Fourier块范数的sup再乘输入总质量，没有额外乘八，也没有遗漏完整源中投影到这八模的贡献。

## 4. 相对1/500球中的严格辅助解

取Banach范数

$$\|V\|_*=\max_nX_n(V)/X_n^{\rm ref},\qquad r=1/500.$$

在以准确线性参考为中心的半径r球内，R23输入半径仍严格有余量。完整源二次界与R29 Green给映射界

$$\|\mathcal G P_8\mathcal N(Z^{\rm ref}+V)\|_*
\le\eta(1+r)^2
<0.001974248938980082<r.$$

R23的Lipschitz界给

$$\operatorname{Lip}\le4\eta(1+r)
<0.007881233289341640<1.$$

这些比较在`closure-real-green-q003-m8-recovered-radius-ledger.json`用精确Fraction核算。因此Banach定理在整个213胞元上给唯一局部辅助解，其逐胞元强范数修正不超过参考的1/500，mean始终由完整holonomy小根决定并统一积分。

辅助问题的边界条件是：准确**线性**R18深直线、八个固定浅高度；向量场是完整点态非线性源在输出处投影到八模。窗外非均值变量只在这个辅助问题中置零。它不是先压缩乘法算子再求逆的原finite worker，也没有把非线性R18深图换成线性图后仍声称精确全频解。

## 5. 恢复完整性和可收文件

更换执行器后，四件源码归档逐字节恢复到旧hash：

- v2源码归档17866B，SHA256 `84a865de3bcaacb2e268617092ca0f64923ad886a87e7912279d2f804fcad514`。
- 真实M8全部cell group gzip 1314429B，SHA256 `f1dff81b293b5b6085bc8825769875997bb89eb6898a6aca6582769b2692ecd0`，重算后与中断前完全相同。
- Green重新算出的η也与原completed run的准确dyadic值相同。这里仍进行了完整重算，没有因源码或hash一致省略用户要求的恢复计算。

稳定文件为两个`recovered` prefix的主JSON.gz、summary、线性raw-manifest/columns-01-08以及Green radius-ledger；三件新计算入口和R26已推源助手由v2归档精确保全。重做命令见`2026-11-12-closure-executor-change-recovery.md`。

## 6. 当前继续项

46列已按同一v2源码重新启动session98069，在高度门前保存全部cell，不能引用失联session73042的未知终态。低46完整边值响应、R18真实非线性深图、窗外非线性forcing的解析尺度处理，以及node12以外的实际强前缀仍是下一阶段的联合问题。R26的真实Rout已由root另行核算；它与名义binary .3并不相等，不在本计算中混同。
