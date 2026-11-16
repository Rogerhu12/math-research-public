# 原 GB 的完整临界广义泛函：常数单位缩减与局部 jet 接口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

本入口消费原完整 F127 GB 与实际 whole299 临界主分量，以原 GB 的全部参数行构造有限局部环上的完整左泛函族。先实做最小的 $h=s^2+s+43$、精度 $t^3$；其完整 primary 维数为 10，循环指数为 $(2,3)$。新代码支持已付五因子，并共享同一个常数缩减缓存，但本次只运行 E8-1。没有预填 detector 数量或常数缩减后的矩阵规模。

## 1. 源码、真实输入和运行方式

| 相对课题路径 | Git blob | 字节 | SHA256 |
|---|---|---:|---|
| notes/2026-11-16-r150-original127-complete-generalized-critical-detectors-789f.py | d10eedffe7c26521e4d7e4a21cb6b2ecc40602d2 | 23978 | e671f2b18e4b5840ddc8a60c9cffe9f127a52d1e0707fefa77fcda148153b271 |
| notes/2026-11-16-r150-original127-complete-generalized-critical-detectors-inputs-789f.json | b7dce0afa1d62e4e042b9cc7b0ce9d6920a69b75 | 3722 | a5a0d52710edca5873344bf8d9448a3c9edb20f8c3722b499f4a1147c88a8287 |

辅助源仍是已实际运行的 notes/2026-11-16-r150-original127-nine-target-cyclic-module-789f.py，blob b4e735dc12e8dee8b483728b895677dcfff23a09，20947 字节，SHA256 d520b190ac84f1990ed8ee84d405cc34c31d09e140ad26b8442c099872d26ed3。只 import reader、矩阵格式与基本检查函数，不运行旧目标任务。

全部实际父文件的 bytes/SHA256 在 inputs JSON 中冻结。父 GB 的真实来源覆盖是原 6188 列，包括新恢复的 660 原来源；新代码不使用旧 5528 子集。原 GB 参数矩阵有 1021 行、1034 列，所有 1021 个 leading-component 标签、节点、规范因子、最高次数及 packed padding 均重新读取并核验。

建议新 step 为 original127-complete-generalized-E8-one-detectors300，300 秒/4096 MiB，外层 360 秒：

~~~text
python {scripts}/2026-11-16-r150-original127-complete-generalized-critical-detectors-789f.py
  --gb-out {work}/original127-complete-graded-module
  --whole-out {work}/original127-whole-torsion
  --profile-out {work}/original127-critical-primary-profiles
  --sources-root {scripts}
  --factor E8-1
  --out {work}/original127-generalized-critical-detectors
  --seconds 300
  --memory-mib 4096
~~~

数学不重做 NF、GB 或 whole torsion；只在其已保存的原矩阵上构造新的泛函。没有声明本地 AST 或数学执行；第一次实际 Python 解析在本任务进行。

## 2. 只剔除原 GB 的实际常数单位行

把原 GB 写成行关系矩阵

$$
G(s)\in k[s]^{1021\times1034},\qquad k=\mathbb F_{127}.
$$

令 $G_0^{\rm const}$ 是其中次数严格为零的全部原行，行数为 $z$。其原 monic、不同 leading-component 身份给常数独立性，程序仍实际 RREF 核秩 $z$，生成完整常数核图

$$
E\in k^{1034\times(1034-z)},\qquad E_{\mathcal F}=I.
$$

必须核 $G_0^{\rm const}E=0$ 的全部原坐标。其余 $m=1021-z$ 行完整保留，定义

$$
Q(s)=G_{\rm positive}(s)E
       \in k[s]^{m\times(m+13)}.
$$

这里没有按参数点删行或除参数多项式。$E^T$ 是常数单位来源消去后的商映射：它满射、核等于常数原关系行空间，因而

$$
\operatorname{coker}G(s)^T\simeq\operatorname{coker}Q(s)^T.
$$

所有正次数原行的每个参数系数都实际乘以 $E$ 后保留。程序记录真实 $z,m$、次数直方图及原行标签；不能从 $\sum\deg G_i=701$ 猜一个未执行的更小矩阵。

## 3. 完整局部环核，不只使用点核

令 $h$ 是指定实际不可约因子，$d=\deg h$，

$$
L=k[\alpha]/(h(\alpha)),\qquad R=L[t]/(t^r),\qquad s=\alpha+t.
$$

$r$ 来自已付完整 primary 的最大循环指数。所有 $L$ 乘法按基 $1,\alpha,\ldots,\alpha^{d-1}$ 展开为 $k$ 上的正则表示；原多项式代入使用精确二项式系数。得到矩阵系数

$$
\widehat Q(t)=\sum_{i=0}^{r-1}Q_i t^i
      \in k[t]/(t^r)^{md\times(m+13)d}.
$$

先实际核 $Q_0$ 的秩为 $md-2d$，其亏秩 2 对应本 primary 的两个已付循环块。选择实际原 scalar 行 $\mathcal I$、列 $\mathcal C$，核原方块 $U_0$ 的完整逆乘积。保留全部其余行与全部自由列。

以自由坐标单位阵构造唯一常单位图

$$
X(t)=\sum_{i=0}^{r-1}X_it^i,\qquad
X_{\mathcal F}(t)=I,\qquad
\widehat Q_{\mathcal I}(t)X(t)=0.
$$

其递推只除 $U_0$。每阶所有 unit 行乘积实际为零，全部未选原行的残量

$$
S(t)=\widehat Q_{\mathcal I^c}(t)X(t)
$$

完整保存。然后对 $S(t)y(t)=0\bmod t^r$ 的全部系数建立 Toeplitz 矩阵，求完整核，而不是逐层挑少数可延向量。

若 $n_h=\dim_kM_h$ 是完整 primary 维数，所得完整局部核的 $k$ 维数必须为

$$
13dr+n_h.
$$

其中 $13dr$ 是原泛型自由部分的全部 jet 歧义。本入口保留它，不将其预先设零。本次 E8-1 的检查值为 $13\cdot2\cdot3+10=88$。只有完整单位图及全部剩余行共同给出这一核。

## 4. 用原 whole 坐标检验完整分离性

设实际 whole 核为 $K\in k^{805\times299}$，实际完整 primary 基为 $U_h\in k^{299\times n_h}$。窗口坐标是原 $(c_i,e_i)$，表示 $s^{e_i}$ 乘第 $c_i$ 个原 NF 输出分量。

对一个局部泛函 $a(t)=E\,x(t)\in R^{1034}$，其对原窗口向量的取值严格为

$$
\ell_a(v_i)=(\alpha+t)^{e_i}a_{c_i}(t).
$$

新代码用原全部 805 个窗口坐标和 $KU_h$ 构造这一限制。把所有候选泛函的 $R$ 值展开成 $k$ 坐标后，必须实际得到满秩 $n_h$。这才证明这些泛函能分离完整 primary；不能仅以局部核的预期维数代替此门。

选择能逐次增加覆盖秩的实际泛函，直到覆盖满 $n_h$。程序不硬编码“两个就够”，所选数量、原局部核列标签与每次覆盖秩全保存。若 $\mathcal R_a$ 是某个所选泛函在原 primary 上的 $k$ 矩阵，另须实际核

$$
\mathcal R_aJ_h=T_{\alpha+t}\mathcal R_a.
$$

这里 $T_{\alpha+t}$ 是 $R$ 上乘 $\alpha+t$ 的完整正则矩阵。此门锁定真实参数作用，排除仅在向量空间中偶然满秩的错误运输。

最后把所选 jets 回填为全部 1034 个原 NF 分量，直接使用重新解码的原 $G(s)$，逐 $t$ 系数乘回**全部 1021 个原 GB 行**。常数行和正次数行均保留，不只核小 Schur。完整 coefficient products 与所有 primary 作用产品是最终成功门。

## 5. 临时数据、续接及后继范围

同一个 out 的公共 binding 包含源码、辅助源、完整 GB/whole/profile 及各实际输入 SHA。共有的原 degree-zero quotient 只生成一次。其余 phase 按五个 factor label 独立命名；后续换 --factor 可复用共同 core，不能混用另一因子的 jets。

每个完整阶段原子保存：原常数商图、小多项式系数、常单位图及全部 Schur、完整有限 jet 核、最后完整原分量泛函。预算/异常诊断写 parameters.error。未完成阶段不计为证书。

本入口最后给出的是**原 NF 输出分量中的完整广义泛函**，不宣称原 4367 个输出的运输已完成。后继必须：

1. 沿同原预基的严格降矩次数三角关系作转置回填，保每阶的全部参数系数；
2. 用原 primitive 17 式在无分歧 lift 环 $(\mathbb Z/127^2)[a]/(\widetilde h(a))[t]/(t^r)$ 核全部 6188 个原标量列确被 $127$ 整除；
3. 扫描全部 1834 个真实全参数 Z 来源；若报告正证，再反向恢复实际整数 lift 并在全部 4367 原行乘回；
4. 若报告该 primary 第一系数连接全零，必须使用本入口已付的完整 primary 分离性及全部 Z 覆盖，不能退回单点负检验。

当前 source 的成功标志明确保留 original4367TransportComplete=false、coefficientBocksteinComputed=false、characteristicZeroConclusionInferred=false。任何下一个数学结论须另有真实消费回执。
