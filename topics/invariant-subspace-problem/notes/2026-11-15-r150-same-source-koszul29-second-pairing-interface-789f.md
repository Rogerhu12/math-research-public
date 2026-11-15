# 同一无穷远原来源的 29×36 二阶 forcing 配对接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。

状态：新 wrapper 的同字节本地 AST 已通过；研究配对尚未执行。随后本地执行环境失联，因而没有把 API 小检查称作本地 python-flint 实测。本文的极小列尺度检查实际由 V8 BigInt 完成。旧 29 个原来源核已经有真 Q 证明；其旧会话临时数组已失，本入口只用原生成器恢复它们，再计算新的小配对。

## 1. 所配对象与量词

固定当前自然无穷远坐标 $u=1/s$，同一原 $17$ 式、所选来源 $J$ 与所选输出 $I$。$B_0$ 是 $4354\times4354$ 常块。当前系数文件的全部 $1309$ 个整数常系数，与旧 point model 的 $17\times77$ 个 primitivePointCoefficients 逐项相等。本入口重新核这一等式；不依赖零点模型，也不把共动系数当自然系数。

原变量次序保持 $m_0,\ldots,m_{10}$；normal 变量为 $m_0,\ldots,m_8$，纯变量为 $d=m_9,c=m_{10}$。source 的 raw 编号为
$17\,\operatorname{index}(\mu)+i+1$，其中乘子按总次数 $0,1,2,3$ 枚举。所有原来源共 $6188$ 个，完整输出共 $4367$ 个。

令 $K\in\mathbb Q^{4354\times29}$ 为旧 29 个真来源核在 $J$ 上的限制。原证书逐列包括全部 $6188$ 个来源系数；$J$ 外 $1834$ 个系数全零，全部 $4367$ 个原输出乘积全零。因此
$$
B_0K=0,\qquad
K^TB_0^TE=0
$$
对任何所选输出嵌入 $E$ 都成立，特别对当前 $E_{\rm new},E_4,E_5$ 同时成立。这是 source 空间的核，不是输出空间的 29 个余类或左头。

旧已付 forcing 为
$$
F=[H_F,T]\in\mathbb Q^{4354\times36},
\qquad
H_F=B_1^T\Lambda F_1,\quad
T=B_1^TE_{\rm old}X+B_2^T\Lambda C.
$$
前三列是完整的三个一阶失败补方向，后 $33$ 列是全部一阶可提升头的二阶 forcing。实际文件保存的就是这 $36$ 列原整数系数。新入口直接使用 originalRightHandSideRows，不按 M0 的逐行 content 除这些行。

本次唯一新矩阵为
$$
P=K^T[H_F,T]\in\mathbb Q^{29\times36}.
$$
先重新完整检查原来源，再形成 $P$，先保存完整 $P$，最后求其 Q 秩及核。

## 2. 真下界与闭合条件

令
$$
\rho=\operatorname{rank}_{\mathbb Q}P,\qquad
h=\operatorname{rank}_{\mathbb Q}(K^TH_F).
$$
完整一阶补空间在 $\operatorname{coker}B_0^T$ 中有维数 $3$。二阶连接的像是 $H_F,T$ 张成空间再商掉这三个一阶补方向。限制到任意真原来源核子空间都给出商空间的一个像，因此
$$
\operatorname{rank}_{\mathbb Q}\beta_2\ge \rho-h\ge\rho-3.
$$

已完成的 $22$ 个二阶头，全部经 $4354$ 原来源乘回，故另有上界
$$
\operatorname{rank}_{\mathbb Q}\beta_2\le33-22=11.
$$
还已有模 $31$ 的下界 $9$。本次实际结果将据此分成：

| 条件 | 完成 outcome | 严格结论 |
|---|---|---|
| $\rho-h=11$ | complete-selected-second-rank-eleven | 完整 Q 第二连接秩恰 $11$；旧 $22$ 个头已完整 |
| $\rho-h=10$ | selected-second-lower-bound-ten | $10\le\operatorname{rank}\beta_2\le11$ |
| $\rho-h\le9$ | paired-subspace-insufficient-to-close-second | 保留 $9\le\operatorname{rank}\beta_2\le11$；此 29 维测试不足 |
| $\rho-h>11$ 或 $\rho>14$ | failed | 与已付全原乘回冲突；判输入或实现失配，不推翻旧结论 |

本入口不要求 $h=3$，从而不遗漏 $\rho<14$ 但 $\rho-h=11$ 的情形。

完整配对核的 $(t,c)$ 坐标为 $\ker P$。其后 $33$ 坐标投影的维数为
$$
\dim\pi_c(\ker P)=33-\rho+h.
$$
代码实际构造该投影、计算其秩，并核整个原矩阵 $PZ=0$。投影维数必须至少 $22$。完整矩阵与基仅留本 job 临时文件，小回执保存尺寸、枢轴、SHA 和实际 Q 秩，不将大有理系数写入 Git。

## 3. 固定源码与输入

新 wrapper：

- 路径：notes/2026-11-15-r150-same-source-koszul29-second-pairing-789f.py
- blob：aadcf9c245884ccac19a55f34853d614749961a9
- 字节：21646
- SHA256：33b8a3e0c501488e5da6e2d654bfa84c915237ea537279fd45d24ba846653f14

下列三个旧源码原样引用：

| 参数 | 文件（均在 notes/ 下） | 字节 | SHA256 |
|---|---|---:|---|
| --helper | 2026-11-15-r150-selected-infinity-fixed-three-coordinate-lll-789f.py | 22765 | 9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428 |
| --preparation | 2026-11-15-r150-koszul-exact-outside-sparse-preparation-789f.py | 7833 | 7fcaee1cf34ea2545f10050fbb899e6d2a682a61485e2351214250072d819170 |
| --support-solver | 2026-11-15-r150-koszul-exact-rational-support-solve-789f.py | 17287 | 0689aec8f35c098a3d1e831297b94102ec38596fe724ac63cdf4bbc9c012e7a2 |

对应 blobs 依次为 e7854ead18387512ab1a9796141f7b03c7c50569、
3495c546ea0a2cae943a1c006bc7491e47540a54、
4ee3fe8769c608968ea4f1e519082bcc88aa4b01。

旧 helper 只导入原来源字典和原整数乘回函数，不调用 LLL。旧 preparation 生成完整标准 $1632$ Koszul 族及其 $1834$ 行外支撑矩阵；旧 solver 选同 $1603$ 单位块、完成 Q 解与全外支撑残差核，再完整运输到原 $6188$ 来源。此前同 solver 的实际耗时为 $33.711323768$ 秒，不把这个旧时间预填成本轮时间。

主要实际输入：

| 输入 | 字节 | SHA256 |
|---|---:|---|
| point model | 87459 | 97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074 |
| native model | 128145 | 291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6 |
| regauged/prepared/second-left-m0-unit-input.json.gz | 9008513 | c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe |
| regauged/full-products 的实际完整回执 | 12690 | b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70 |
| rebuilt-first/same-original-natural-constant-and-first-coefficients.json.gz | 20580 | 7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1 |

旧 selected-infinity-minor-dag-receipt.json 锁 SHA256：
5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68。

旧完整回执的文件名若与预设不同，只允许在同一 full-products 目录按上述完整 bytes/SHA 唯一定位，不按模糊字段接受替代输入。

## 4. 实际 CLI 与预算

~~~text
python -B {scripts}/2026-11-15-r150-same-source-koszul29-second-pairing-789f.py
  --helper {scripts}/2026-11-15-r150-selected-infinity-fixed-three-coordinate-lll-789f.py
  --preparation {scripts}/2026-11-15-r150-koszul-exact-outside-sparse-preparation-789f.py
  --support-solver {scripts}/2026-11-15-r150-koszul-exact-rational-support-solve-789f.py
  --native-model {native_model}
  --point-model {selected_model}
  --selected-receipt {paid_dir}/selected-infinity-minor-dag-receipt.json
  --regauged-out {work}/selected-natural-second-left-regauged
  --rebuild-root {work}/selected-natural-u-rebuilt
  --out {work}/same-source-koszul29-second-pairing
  --seconds 180
  --memory-mib 2048
~~~

所有数学阶段共享一次真实 $180$ 秒时钟，每进程 $2048$ MiB；建议外墙 $210$ 秒。没有 native 编译或软件安装。每个子进程均受剩余真实时间控制；到时给短暂停止宽限后终止，已完成文件不删除。

完成的原 preparation、$1603$ 单位解、完整外支撑核、逐列原来源证书和新配对均可续用。wrapper 的 binding 含完整源码和输入 bytes/SHA，不含绝对路径或预算。旧子程序自己的语义 binding 原样保持。继续同 out 时先验证相同输入与源码；不重已完成的 $1603$ 解和 29 个证书。

本轮不续 normal5 的 $786$ 已成 pivots；它们仍保留在独立目录。本轮不解新的 M0 RHS、不重全 NF、不增加 Dixon 位数。

## 5. 结果、临时文件与发布范围

主回执：
same-source-koszul29-second-pairing-receipt.json。

关键字段：

- pairingRankOverQ；
- firstThreeHFPairingRankOverQ；
- secondConnectionRankLowerBoundFromPairing；
- selectedSecondConnectionRankOverQLowerBound / UpperBound；
- selectedSecondConnectionRankExactly11；
- completeSelectedSecondHeadSpaceProved；
- completePaired33HeadProjectionDimension；
- completeOriginalPairingKernelProductsVerified；
- all1309ConstantCoefficientsExactlyMatched；
- sameSelectedSourceSupportVerified；
- all29FullOriginal4367ProductsZero；
- originalProductCoordinates = 29×4367；
- originalForcingRowsUnscaled；
- sourceKernelDimensionUsed = 29；
- all36SourceKernelDirectionsUsed = false；
- leadingUnitProved = false。

临时目录 reconstructed-source-model、reconstructed-source29、pairing 分开保存实际阶段。pairing 内包括完整原 $29\times36$ 整数矩阵，以及全部核、原坐标 $33$ 投影基和尺度信息。只有小主回执、源码、参数、run ID 和 SHA 可长期保存；不上传大数组。

即使闭合 $\beta_2=11$，也不声称指定行列式的整个 Q Smith 长度已知，更不声称最高系数为 $31$ 单位。

## 6. 有限的实现核验

python-flint 0.9.0 官方 fmpq 文档明确列出 property p 为 numer()、property q 为 denom()：
https://python-flint.readthedocs.io/en/latest/fmpq.html 。

新源码的 qcolumn_primitive 输入由 fmpq 显式初始化或有理矩阵元素组成；没有以 Python int 的缺省零代替待取 p/q 的元素。旧同接口 Q solver 和现有二阶代码已实际使用该 API 完成运行。

独立 V8 BigInt 小检查使用
$$
P=\begin{pmatrix}6&15&21&9\\10&25&5&15\end{pmatrix}.
$$
逐行 gcd 为 $(3,5)$，随后逐列 gcd 为 $(2,5,1,3)$，所得归一矩阵
$$
N=\begin{pmatrix}1&1&7&1\\1&1&1&1\end{pmatrix}
$$
有核列 $(-1,1,0,0)$、$(-1,0,0,1)$。按逆列尺度返回原坐标，primitive 整数列为 $(5,-2,0,0)$ 和 $(3,0,0,-2)$；两个原乘积严格为零。误把除列尺度写成乘列尺度时，原乘积分别为 $(63,105)$、$(15,25)$，所以这个检查能识别方向错误。

实际测试使用 functions.exec 的 V8 BigInt，没有使用研究数据。生成代码 SHA256 为 3c3be02458805bb42c6da0d5a0f098d06089ec5cceec03a0158d1f885b47cafb；实际小回执 SHA256 为 f389edacaaba1ea40b77972839111be81191c2a23785ac4c498d25f739f6bccf。它不冒充本轮 Q 配对或本地 python-flint 运行。
