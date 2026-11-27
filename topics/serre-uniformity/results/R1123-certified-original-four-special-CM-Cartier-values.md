# R1123：原 full47 两个特殊 CM 圆盘的四个规范第三类值

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：已证明，公开精确计算成功。**
原标签0与141的四个尚缺 $\alpha_{Z,y}$ 已由独立短 Cartier 请求完整取得。
它们与 [R1121](R1121-certified-original-twelve-short-Cartier-values.md)
的十二个值合起来，付清全部八个原 CM 圆盘的两个对应之局部输入。
本篇不预报这两个圆盘的 QC 行秩；该读取使用新的独立请求。

几何、原完整除子、全部 closed/coarse/cusp 尺度与规范性沿
[R1118](R1118-original-short-Cartier-reading-for-CM-third-kind-values.md)，
最终 QC 接口沿
[R1103](R1103-original-CM-tangents-finite-field-third-kind-and-QC-first-jets.md)。

## 1. 完整执行来源

- source：[d935282c49c9c19d541729ca5bd59579aac7e82f](https://github.com/Rogerhu12/math-research-public/commit/d935282c49c9c19d541729ca5bd59579aac7e82f)。
- [run45998781656](https://github.com/Rogerhu12/math-research-public/actions/runs/45998781656)，
  [job140504817189](https://github.com/Rogerhu12/math-research-public/actions/runs/45998781656/job/140504817189)，attempt1。
  checkout、固定镜像、数学步骤与整个 job 全部 success。
- 数学总耗时 **314.479137561秒**；预算3600秒，reserve120，四个工作进程共用原截止时间。
- 固定 SageMath10.6 官方镜像，python-flint0.9.0；父子进程保持 fresh-exec 隔离。
- 完整 receipt 为 status=complete、completed恰4条、failed_cases为空。
  root/global分别读取完整实际日志，root另核四条 clean rows、
  新 Cartier 证书和后继请求中的记录逐字 canonical SHA 一致。

原首四 Miller 请求仍是独立的旧在途来源；本篇没有把它冒称为成功，
也没有以其它十二条除子的八点读数补入这四条。
本次只构造0/141的四个新除子，共同原 C/E/frame/grid 在新值前核对旧哈希；
R1121已成十二条和R1122已关六盘没有重新计算。

## 2. 四个实际值

全部数值属于 $\mathbf F_{4513}$，对应
$Z_A=13R_0+4R_2$、$Z_B=2R_4-7R_0$，
已经包含清分母后的除六：

$$
\alpha_{Z,y}=
\left.\frac16\frac{\eta^{\rm fix}_{6D_{Z,y}}}{d(j-j_{\rm CM})}\right|_y.
$$

| 原标签 | 原 $j_{\rm CM}$ | 原 CM 判别式 | $\alpha_{Z_A,y}$ | $\alpha_{Z_B,y}$ |
|---:|---:|---:|---:|---:|
| 0 | 0 | $-3$ | 531 | 1857 |
| 141 | 1728 | $-4$ | 1783 | 529 |

特殊点处仍使用原 coarse 参数 $j-j_{\rm CM}$，没有以栈参数代入。
四条都保 method=R1118-short-Cartier、clearing_denominator=6、
order_mod_q=551，并保自己实际除子的 SHA。
每条附带的八点读数只描述**该同一除子**，其中本表取自己的目标位置。

## 3. 各自完整 RR 与留数证书

原清分母除子在特殊纤维发生实际支撑合并，所以本次逐例的 $s$
与一般六盘不同；程序从原 fixed cycles 合并实际权重后读取，
没有沿用一般盘的支撑度。

| case | 约化支撑度 $s$ | $\dim W_S$ | 分子空间维数 | 留数矩阵秩 |
|---|---:|---:|---:|---:|
| 0/$Z_A$ | 111 | 151 | 183 | 110 |
| 0/$Z_B$ | 87 | 175 | 159 | 86 |
| 141/$Z_A$ | 135 | 127 | 207 | 134 |
| 141/$Z_B$ | 127 | 135 | 199 | 126 |

这些仍分别满足 $262-s,\ 72+s,\ s-1$。
四例 all_original_cusps_included=true，均在两条 colon 约束后达到
R1118证明的完整空间维数，随后核全部留数及目标方程。
分母截面避让条件数依次为158、134、202、180，
每个条件都在实际输入上核验。

## 4. 原 Cartier 同帧与新证书

共同原73帧、Gaussian grid、Hodge评价矩阵和 Cartier 算子
在本次新分子读数前全部通过旧哈希门。
仍有 $\det E=3058$、$\det(1-C)=551$，KS常数809，
物理参数为 $B$。完整矩阵的哈希严格不变：

| 对象 | SHA-256 |
|---|---|
| Cartier column matrix | 21fc43c13f58e974adb58804e3480f80d3268104546e31e40ca5370806bbb58f |
| Cartier row matrix | deda5ed6dbe8122f243c46bb60245cf8facc00b6040a8f34958c9ca4241d855d |
| 原 Hodge 评价矩阵 | 8c5073af02da9d9731f7cbff7ab5fa1e061e590fe965355c9a2e79ff463795bb |
| 选定原帧 | ac2b0b2dc168977fe758cbf9b6f9a2eeb5b187d6da566f0940f824c9f375c67f |
| 新四分子对应的全73帧值 | ae73596b74109697086d8421b76734fc42696c86dafb1a93b040a2afa7a8b439 |

最后一项含本次新的实际分子，所以不同于R1121的十二分子哈希；
这不是共同矩阵变化。四条修正准确为
$x=(1-C_{\rm col})^{-1}(C\eta-\eta)$，再取原 coarse 微分值并除六。

## 5. 来源及结果 pin

| 对象 | SHA-256 |
|---|---|
| 首四独立短 Cartier 入口 | d7e5529e9c45183cc902689e93573b3aff0f37ec3e4d0f9956c24aa39affe72a |
| 方法说明 | 0b72ec1b67b6f29cfddd19eefd5084588f486191368a10363250826dbe59be1d |
| 实际请求 | ed9508e1cd4d0f4b9950c68eebde5ada7fddf29d1e63810df7e367bffa6b8bc2 |
| 四条完整 clean rows | 1056547ddb3efa107b5a01dc9fa093c06589dd1f27803897e6913ef3d5438eab |
| 本次完整 Cartier 证书 | 8d2b552051d6b8b62ccffc24c5bef8e276ceb9e9c388fb4da4fc7fb193006856 |

入口：
[方法](../notes/2026-11-27-full-p47-short-Cartier-first-four-method.md)、
[请求](../notes/full-p47-short-Cartier-first-four-request.json)、
[程序](../scripts/full_p47_short_Cartier_first_four.py)。
只保源码、小请求、run/job、哈希与结论；没有提交 raw、artifact 或 Release。

## 6. 直接后继

[两特殊盘 QC 方法](../notes/2026-11-27-full-p47-QC-special-two-method.md)
及其独立请求只读标签0、141。
共同高度、Jacobi 坐标、切向、角、$B_q$ 与 $\lambda_0$
从成功六盘请求按完整 SHA 只读消费；旧六盘请求、源码与workflow不改。
新的四条 clean rows 和本次自己的完整 C 证书已经真实填入，
父进程与 fresh flint 子进程都验证同一新请求和全部旧 pin。

实际首行、共同 gcd 和单位导数仍由公开执行决定。
即使两盘随后关闭，固定47结果仍不是课题README要求的一般素数绝对一致性。
