# R798：原 μ33 的选行坐标公开计算方法

2026-11-15。对应证明：
[R798 原六次幂选行坐标](../results/R798-original-power6-row-coordinate-interface.md)。
本方法只规定新实际任务和可复用接口，不把预期维数写成运行值。

## 1. 初次范围与既有输入

本次生成原 $V_6$ 完整短矩阵的真实1506行可逆子矩阵，
以及原 $\tau^3V_3$ 的690个乘积列。
$\tau$ 是 R786 原 M2 第0行，三次幂第0行的原配方等于 $\tau^3$。
不计算完整有理逆，也不生成全部 $690^2$ 对乘法。

原 R795 已完成1506条普通六次幂，
每条 $q_Y^0,\ldots,q_Y^{81}$ 同时有40个 $\xi$ 坐标和20个
$t=\xi+\xi^{-1}$ 坐标，整数尺度 $82^{12}$。
原 R786 的690条普通三次幂有 $q_Y^0,\ldots,q_Y^{128}$，
整数尺度 $82^6$；本次消费前82项。
额外只读原一次/二次幂第0行，以原 recipe 证实锚点身份，
不重新乘出旧 $\tau^2,\tau^3$。

两个 producer 的 run/source/artifact/full manifest/核心/最终证书/阶段
manifest 均固定在请求中。
逐行文件名由固定幂、维数和原序号唯一导出，
其逐行大小、SHA、configuration 从已绑定的原阶段 manifest 核对。
这样请求无需重复保存超过100KB的1506行哈希列表。

## 2. 核心入口和输出

核心文件为：

- `scripts/R798_original_mu33_row_coordinates.py`；
- `scripts/R798_public_original_mu33_row_coordinates.py` 为公开 runner。

数学核心只允许在 `Rogerhu12/math-research-public` 的 GitHub Actions 执行。
CLI：

~~~
--config JOB.json
--retained RETAINED_DIRECTORY
--output OUTPUT_DIRECTORY
--proof results/R798-original-power6-row-coordinate-interface.md
--method notes/R798-original-mu33-row-coordinate-method.md
--rr-proof results/R793-original-RR-pole-divisors-and-CM-local-algebra.md
--budget-minutes 300
~~~

`result` 固定为 `R798-original-mu33-row-coordinates`；
最终文件为 `p41-original-mu33-row-coordinate-certificate.json`。
输入目录含 `R786/`、`R795/` 两组；每组保留原完整输出 manifest、
run/core receipt、public input、原证书、阶段 manifest 及真正消费的阶段。
R795 另保留原 basis index。

不可变 configuration 包含核心/证明/方法/R793 SHA、
python-flint 0.9.0、两个 producer 的完整绑定、
原字段和参数、尺度、行次序、素数搜索政策。
预算和续接 run 不属于数学身份。
核心各个 `R798-*.json.gz` 阶段原子写入并各自标记 complete；
同一配置的已成阶段只验证并复用。

## 3. 原目标短矩阵与新 minor

直接读取 R795 的 `integer_v_t_coefficients`，
按原1506条基次序排列为1640×1506整数矩阵；
不重新乘出六次幂。
逐行核 `weight=12`、`bound_qY=81`、尺度 $82^{12}$、
原参数和全部已成相位核验标志。

行号固定为 `20*n+r`，其中 `0<=n<=81,0<=r<=19`。
从请求给定起始素数739开始：
在每个实际素数下，对1506×1640转置矩阵作 RREF，
保存真实秩和主元行号。
若秩1506，再准确计算这个实际1506阶模素数 determinant；
非零才接受选行 `I`，其补集 `J` 有134行。
失败素数只记录其真实低秩，不冒称特征零失败。
所有运算在素域进行，不对合数模矩阵求逆。

阶段命名：

- `R798-target-prime-NNNNNNNNNN.json.gz`：每个实际辅助素数；
- `R798-selected-short-rows.json.gz`：成功 `I/J`、prime、
  determinant、矩阵来源、原尺度和坐标约定。

这里只保存新行集与来源，完整原矩阵仍由源文件提供。
没有生成 `A_I^-1`，旧 R775 长系数 minor 不能充当这个新见证。

## 4. 原三次幂运输和双规范乘法

每个原三次幂行只做前82项的相位运输：

1. 第 $n$ 项乘 $\xi^{10n}$，按 $\Phi_{41}$ 准确约化；
2. 对全部 $\xi$ 坐标核反演不变性；
3. 用 $P_r(t)=\xi^r+\xi^{-r}$ 的整数递推换到20维 $t$ 基；
4. 存在 `R798-V3-real-prefix-NNNN.json.gz`，绑定原 R786 文件 SHA。

这不是重跑 E1、M2、旧幂或 Laurent。
`R798-anchor-recipe.json.gz` 只登记原一次/二次/三次幂第0行的
recipe 链与尺度，说明锚点等于 $\tau^3$。

公开的按需函数以两个原 $V_3$ 基索引为输入。
它先取排序后的 `(i,j)`，使同一交换对复用同一阶段。
新积按两条路线形成：

- 原 `qY/xi`：间隔79，准确卷积后按 $\Phi_{41}$ 折叠；
- 原 `v/t`：间隔39，准确卷积后按原20次首一 $g41(t)$ 约化。

第一条运输到 `v/t` 后，与第二条在全部1640个整数坐标准确相等，
才保存 `R798-mu33-product-IIII-JJJJ.json.gz`。
它保存原两个源文件、原两个已成运输阶段、源索引、
尺度 $82^{12}$、`selected_coordinates` 的1506项和
`complement_coordinates` 的134项、成功选行阶段 SHA，
以及完整1640项比较标志。
`I/J` 合起来能无歧义重组完整列。
因此新积的原 $V_6$ 归属来自实际原截面的乘法生成，
没有用只匹配 `I` 代替归属证明。

初次逐一调用 `(0,j)`，`0<=j<690`。
每个完成积即为可续接阶段，不等全部690项结束才保存。
`R798-anchor-embedding-index.json.gz` 列出实际690项，
并把单射的依据准确标为原非零 $\tau^3$ 乘法；
没有在该字段伪填一次未做的模秩计算。

## 5. 后继如何使用这个接口

原 $V_6$ 的坐标定义是 `Ψ_I(s)=C(s)_I`。
如果原基坐标为 `c`，则 `Ψ_I(s)=A_I*c`。
后继全用同一选行 SHA 和原完整输入绑定，
可以直接做空间 span/intersection/kernel/image。

原 $V_3$ 因子仍用 R786 的690维坐标。
任意有理线性组合可先逐项形成原短幂级数，
再调用相同准确卷积与选行函数；
$K$ 或 $L$ 系数按指定有理字段基逐分量双线性组合。
无需先枚举完整690×690表。
基础模块提供精确整数/有理组合产品接口；
它保留输入分母和源组合，完整列先验证后投影。

外来完整1640向量没有生成证明时，不能只丢弃 `J` 宣称属于 $V_6$。
必须按 R798 (798.15) 在原全部1640行代回。
若消费者确实要求原1506基坐标，另启动真正的逐右端 Dixon：
只有模素数逆、整数残差和有理重构，
接受条件是全1640行准确相等。
初次任务不执行这一恢复，最终证书明确其为 false。

## 6. 存储、预算与最终证书

每个三次幂运输行、每个实际素数和每个实际乘积均独立断点。
前序完成阶段不依赖当前预算，不重新计算。
活动输入包携带同源旧文件，续接不要求原 producer 的一天 artifact 仍存在。
源包中不塞未消费的旧幂或新的尾项。

初次最终证书至少给出：

- `complete=true`、原 $p=41$；
- 原输入维数690/1506、完整坐标1640、选行1506、补行134；
- 实际成功 prime、真实 determinant 和成功阶段 SHA；
- 实际690个锚点积，以及全部1640项比较通过；
- 原 $82^6/82^{12}$ 尺度和 $v,t$ 参数；
- 原 `A_I^-1` 未计算、原基系数未恢复、完整690²表未生成；
- 原旧 q 系数、period/Hom/Laurent 未重算；
- 未计算原极除子、$\eta$、$\beta$ 或高度；
- 包含全部新阶段大小/SHA 的 `R798-stage-manifest.json.gz`。

runner 生成完整输出 manifest、run/core/input receipt，
并在上传前核对最终证书及全部新阶段。
只上传一天活跃 checkpoint artifact；
可重算矩阵、完整证书与数据不进入 Git 或 Release。
结果登记只提交脚本、参数、真实 run/source、输出 SHA 和明确结论。

