# 原 full47 weight-one / 全 cusp Hodge 基的首次有限认证

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

状态：**原来源及算法已纸面核对；这个新请求尚未执行，不预设 rank95。**

本请求消费 [R1090](../results/R1090-original-weight-one-integral-Hodge-source.md)
的原 full $X_{\rm ns}^+(47)$ 来源，只认证 $q=4513$ 的
$\Omega^1(C_\infty)$ 整基与全部23留数的73维全纯核。
不重跑 R1080 的 $L'$、R1081 的平方水平 Hecke 证书、
R1074/R1086 的同点标签或 R1089 的群阶条件。

## 1. 完整的原候选与固定有限前缀

固定 $\zeta_{47}=2\in\mathbf F_{4513}$、$i^2=-1$，
$x=d+ci$ 对应原标签 $(c,d)$。descriptor $(a,c,d)$ 表示
$\rho=d+ci$ 及
$$
F_{a,\rho}=\sum_{x\ne0}
 \left(\zeta^{aN(x)}e_xe_{\rho x}
       +\zeta^{-aN(x)}e_xe_{\bar\rho x}\right).
$$
这是完整 Reynolds 形式；两个相位分别保存。
原 cosine 对称子族不能未经证明替代它。

取 $a=1,\ldots,46$。候选 $\rho$ 是
$0\le c,d\le23$、$(c,d)\ne(0,0)$，
按 $(c+d,c,d)$ 字典序排列的前64项。
一般纯虚 $\rho=ci$ 也保留。
$\rho$ 的 $\pm$/共轭关系与 $a=0$ 的冗余由 R1090 直接证明。

原2208个非零向量按 $\pm$ 取1104个半向量；
完整范数 $N(x)=n$ 有46个组，每组24个半向量。
每组分别计算 $e_xe_{\rho x}$ 与 $e_xe_{\bar\rho x}$，
半向量和乘二，再分别乘 $\zeta^{an}$ 与 $\zeta^{-an}$。
这里不是把范数按 $\pm$ 合并的48点分组。

所有 e 展开使用 R1090 的有限除数公式；
常数项、系数相位、$e_{-x}=-e_x$ 均保原尺度。
真实 finite jet 固定为系数 $c_0,\ldots,c_{167}$。

## 2. 成功、有限未决与中断的准确范围

每个 $\rho$ 完成后，对累计矩阵取行独立子集；
所选每行仍是一条真实 descriptor 对应的原形式。
输出该阶段的精确秩、已完成 $\rho$ 和 descriptor hash。
秩超过95为错误，因为 R1090 已证明原线丛维数95。
第一次达到95后停止搜索，并输出全部95个 descriptor。

若64项结束仍不足95，正常输出有限未决。
它不证明整个 Reynolds 族失败，也不证明模4513的整性不存在。
若预算或程序异常中断，只保留实际已经完整输出的阶段。

当实际秩95成立，R1090 的168-jet单射及 Nakayama
付清原整 $\Omega^1(C_\infty)$ 基；
这一步不借用未付的整版 Khuri–Makdisi 张成定理。

随后在同一95个形式上，逐个 $\zeta\mapsto\zeta^b$，
$b=1,\ldots,23$，读取 **全部** 原 cusp residues $47c_0$。
程序核总和为零、完整 residue rank22，
再取右核的规范 Sage basis matrix，得到73行。
它核原 Hodge jet rank73及标准 cusp 的常数项为零。

实际整 Hodge lift 使用完整 residue map 的单位22 minor精确消极；
有限域 kernel 的任意整数系数 lift 不被冒称全纯。
R1090 已证明模4513后继 CM jet 不依赖这种整 lift 的选择。

## 3. 可供下一实际消费者复用的明确接口

脚本
[full_p47_weight_one_Hodge_certificate.py](../scripts/full_p47_weight_one_Hodge_certificate.py)
可以在另一个已审的本仓库公开 runner 中 import；import 本身不运行数学。

- `build_source(descriptors=None,max_rho_batches=64,callback=...)`
  执行本次固定前缀搜索并返回字典。
- 字典包含 `K`、`engine`、`descriptors`、
  `logarithmic_jets`（95×168）、`residues`（23×95）、
  `kernel`（73×95）、`hodge_jets`（73×168）及 `certificate`。
- 下一请求传入本次已认证的95个 `descriptors` 和
  `expected_certificate`，只重建所需同源原输入并比对全部hash，
  不重跑候选搜索或已成秩断言。
- `engine.jets(descriptors,length,root)` 严格按指定顺序返回
  原形式在指定 Galois 根处的系数；
  $1\le\texttt{length}\le836$。
- `hecke_bridge(source)` 是**本次不调用**的后继接口。
  它用 R1090 的真实 Tate-quotient 公式重建
  $T_2,T_3,T_5$，最高degree835，
  然后返回 $H_2=T_2+2T_3+4T_5$。
  矩阵采用行作用
  $T_n\omega_i=\sum_jM_n[i,j]\omega_j$；
  同一 CM evaluation 列向量受 $M_n$ 作用。
  任何调用必须在另一个已审、有独立预算的公开请求中进行。
  本请求的 `enable_Hecke_bridge` 固定为 false。

全部原矩阵只存在于 runner 内存；公开日志保留95个来源descriptor、
精确秩、维数、完整规范及确定性 SHA-256。
不提交矩阵、artifact或原始级数数据。

## 4. 固定执行与来源锁定

只允许本公开仓库 GitHub Actions 执行。
固定官方 SageMath 10.6 amd64 image
`sagemath/sagemath@sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879`。
数学总窗口600秒，预留30秒：
内部在总经过570秒触发回执，外层600秒硬停止。
setup与拉取容器不进行数学。

请求锁定两份 README、R1090全文、本方法及消费者的 SHA-256；
同时验证本公开仓库、实际 checkout SHA、请求hash、
$p=47,q=4513,\zeta=2$、168系数、64个候选组与固定预算。
Sage `proof.all(True)` 保留；没有调用外部网络来取得数值答案。

首次请求只判断上述原 rank95/kernel73。
R1091 的 Gaussian CM系数、实际 Hecke块上的首对数、
Mordell–Weil 饱和、高度首项及原八盘内部唯一性均不由本请求宣称。
全素数 Serre 主目标仍开放。
