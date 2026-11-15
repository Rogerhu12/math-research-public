# R815：第三条准确列已成，首四探针对结束于准确条目拒绝

## 1. 真实运行与读取范围

本稿登记公开仓库 Actions 的真实结束产物，不启动新的数学计算。

- 原运行：[43762388370](https://github.com/Rogerhu12/math-research-public/actions/runs/43762388370)，job `132959925649`，source `ca1fe0d562497055f9e5441edc17ac588a25229c`。
- 数学核心 `R815_three_known_columns_reconstruction.py`：SHA256 `515e15557ea3681055178f5da742d5c4fcee9d5d6a313e5c5892124872a72f83`。
- public runner：SHA256 `3b573881361342a9b3849aacc35ff040d067938d82da2ff7b7a4568d332fc69f`；[三列方法](R815-original-three-known-columns-projective-reconstruction-method.md)：SHA256 `6d12fe13d77ba1f8d970cc697faf229027d812f7b7a067590bd6a3946426f6d4`。
- 原 artifact `14181118695`，平台记录 ZIP 长度 `2730829290` B，SHA256 `afe625bfe018dbde69d6b36dffada3278465e50cf54bd4fdc5b375c07a2ae103`，到期 `2026-11-16 21:23:10 UTC`。
- 原 full manifest：`55956` B、`198` 项，SHA256 `0f2be930adc35c414f8f7f69c7dfd2ada3b0b5fe076d66f7c08583d416cd1718`；ZIP 共 `200` 个文件，包括 manifest 及 reference。

本次纯 IO 以平台 artifact/run/source/digest 身份和原 reference→manifest 为入口，经 12 次 HTTP Range 共传输 `13681996` B。选取的 `196` 个小输出共 `13521794` B，逐项核原 bytes/SHA、configuration、target configuration 和来源引用。两个 carrier 没有下载或重哈希，因而本稿不声称重新哈希整份 2.73 GB ZIP，也不声称重新执行原 carrier 的 3037 个输入核验。原运行保有这些输入及其已完成核验回执；本次核的是该真实来源链和所选输出。

实际数学用时 `72.16439556700016` 秒。核心返回 `2`，run 的运行异常字段为 `null`；核心记录的停止原因是预定四对探针已经消费完毕，尚无准确 $M_g$。随后成功证书 verifier 因 `complete=false` 返回失败。这里没有数学核心异常或新来源接口错误。

## 2. 已完成的准确第三列

仍用原 $W=M_w$ 和原 $v_g$。原来源逐系数认证

$$
We_0=e_1,\qquad We_1=e_{271}.
$$

据此，已知三列为

$$
M_ge_0=v_g,\qquad M_ge_1=Wv_g,\qquad
M_ge_{271}=W(M_ge_1).
$$

第二列直接消费前一真实两列产物；这次只新增 $W$ 乘该已成第二列。四个 $W$ 系数对应的乘积块均已完整原子保存。最终 known stage 为 `R815-three-known-columns-exact-original-input.json.gz`，`4423807` B，SHA256 `ffa005aef7bbcdd32b526db012b9413c85d901dd06d780bed4281bdf10fbfb46`。

该 stage 的已成数学断言包括：列号 $[0,1,271]$ 的加权支撑逐项正确，原第三列未截断乘积的六次、七次项准确为零，原 current 中全部 $690+962+1234=2886$ 个对应系数同余成立，以及共同正分母与全部整数分子已联合除去内容。上述断言来自这次真实数学执行；本次 IO 不再做矩阵乘法、gcd 或同余运算。

| 分母 | 十进制位数 | 二进制位数 |
| --- | ---: | ---: |
| 原 $v_g$ 最简共同分母 $d_g$ | 825 | 2738 |
| 原 $W$ 共同分母 | 1921 | 6381 |
| 已成两列最简共同分母 $d_{01}$ | 1953 | 6485 |
| 本次三列最简共同分母 $d_{012}$ | 3082 | 10238 |

$d_{012}$ 的十进制原字符串 SHA256 为 `8e163c8750ba93e19bda8fa9883e1f81dec12caa04cc00464a72b432d371181e`。表中位数仅是已存整数的表示元数据，没有进行新域运算。完整整数和列向量留在一日 artifact。

三列统一到 $d_{012}$ 后，列 $0,1,271$ 分子的最大位数分别为 `10228`、`10230`、`10233` bits；实际非零文本项数分别为 `690`、`962`、`1234`。原标量、原正规基、原 $g$ 与 $W$ 的规范均保持。没有重做原 $Wv_g$ 或原 425 个素数的 CRT。

## 3. 实际探针、候选与拒绝

前一真实两列来源的标量扫描已完成到 `next_coefficient_index=25`，准确失败位置为

$$
10,11,12,13,15,17,20,24.
$$

本次直接复用这段分类，不重做旧标量有理重构。列 $0,1,271$ 被排除出新未知探针；实际四对仍是：

| 探针对 | 原 coefficient indices | 原位置 $(\text{output row},\text{input column},\text{power})$ |
| --- | --- | --- |
| 0 | $(10,11)$ | $(0,2,1),(0,2,2)$ |
| 1 | $(12,13)$ | $(0,2,3),(0,2,4)$ |
| 2 | $(15,17)$ | $(0,3,1),(0,3,3)$ |
| 3 | $(20,24)$ | $(0,4,1),(0,5,0)$ |

四对各七个预定权，合计 `28` 个新三维 LLL 格、`84` 条实际保存行。其中 `8` 行的 $D=0$，其余行没有出现 CRT 非单位分母拒绝。全部行有 `50` 种不同的原分母字符串，包括零；因此本轮共有 `49` 种不同的正分母候选。直接 $D=d_{012}$ 的 baseline 已与 LLL 所给分母重复，不能另加一次计数。

每个正分母候选都构造性使用准确的三条已知列；其余位置仍采用原模数下的中心提升。全部 `49` 个候选均在第一个实际准确交换子条目

$$
[N_D,W](z)_{0,2}\big|_{z=0}
$$

得到非零值，分别写有来源绑定的拒绝回执。这次没有候选通过该条目，没有进入后续七个准确点的完整矩阵交换子认证，也没有得到 $M_g$ 或 $\Gamma$。

原列 $0,1$ 的交换子为构造性恒等式，所以核心没有把它们计为独立筛选。这次真实首失败列是 `2`；不能把前一两列运行的失败位置直接沿用为本次结果。

直接 baseline 的候选定义为 `R815-projective-g-candidate-3c32a7e245be7104f55ff44348e59ab5`。其首失败 residual 是正整数，十进制 `5748` 位、二进制 `19092` 位，原十进制字符串 SHA256 `e540914b42bd0d7556eb2061a925f3530abbad02679d917ba9164daf7e7306f5`；该准确条目文件 `10597` B，SHA256 `373822577379fb6093a709353b0730deba452e255077f2eb4108d22eab2f8bca`。这些只是已保存 residual 的表示元数据，本次没有重算 residual。

核心已经把 $D=d_{012}a$ 内置于搜索。每对剩余模系数 $r_i,r_j$ 的原未加权整数格基就是

$
\begin{pmatrix}
d_{012}&\operatorname{center}(d_{012}r_i)&\operatorname{center}(d_{012}r_j)\\
0&M&0\\
0&0&M
\end{pmatrix},
$

并且原完整幺模变换直接记录 $a=D/d_{012}$。因此“先使未知共同分母成为已知 $d_{012}$ 的倍数”已经实施，不能作为下一条新计算重新提出。当前 LLL 的第一个实坐标仍是 $D$，与其他两坐标施加七个已定权；改用首坐标 $a$ 会改变格的度量，但不会增加任何同余信息，亦没有自动成功界。

## 4. 数学含义与继续消费边界

已经新增的是原准确第三列及其共同分母、真实四格族的全部行与准确拒绝。任何整分子/单一正分母表示的完整 $M_g$，其分母必须被这三列的最简共同分母 $d_{012}$ 整除。这一事实约束后续共同分母搜索，但不为未知列提供分子高度上界。

本轮全部候选失败只排除它们各自构造出的完整中心提升矩阵。它既不证明原 $M_g$ 不存在，也不证明原 `425` 素数、`12707` bits 的 CRT 模数不足，更不排除同一分母配合不同非中心未知列提升。不能把启发式三维 LLL 范围当作有保证的恢复界。

当前扫描仍为 `next_coefficient_index=25`、`unpaired_failure=null`、`completed_pair_count=4`、`scalar_RR_failure_count=8`、`scan_finished=false`。核心的 `candidate_search_exhausted=false`，只因 `probe_pair_limit_reached=true` 停止。若以后实际续同一核心/tag，应恢复该真实扫描和已成三列/四乘积块/LLL/拒绝，避免重新执行首四对；是否继续此策略须由剩余真实问题决定，本稿不自动发起新计算。

## 5. 简明来源登记

- 原 configuration SHA256：`e9bdaaad21dad23d7180383deee207bc279639a8d157029b98ef5fa2236e2c37`。
- 原 false certificate：`17191` B，SHA256 `ee9a66e610ef2b0c55b768da2052cf4ab9fd73d3907558f2f61352d9a6fab5e8`。
- 原 stage manifest `R815-stage-manifest-59a7299aeb1124d4f55f0be7.json.gz`：`14809` B，SHA256 `d1785965ff52debb8c0e678c317af9397cd03f4324e8de016ee0b377f903aaf2`。
- 原 scan current：`3708` B，SHA256 `0bef2e76473291df2ae550dc4568154e329c4248fa8fdb785f53730177ecb80b`。
- 原 imported scan：`3776` B，SHA256 `1f18d6ea4e0dc6ec488bc9ec84b0eeb57755789159b6ad157c70b331e373716f`。
- 原 3037 输入 carrier：`2715514274` B，SHA256 `4c9a6d1e3c2c462efecabeba826697efbbc04a3357db1a74d8bd06027804a1b5`。
- 本次原两列小源 carrier：`1689309` B，SHA256 `a5eac0d510a18fd1c1456600bb9cce7022b9e2837232a4d511af6c9e4531f428`。

四个新乘积块、完整列、LLL 基、拒绝 residual、机器 IO summary 与全部机器回执只在当前一日 active artifact/carrier 或临时纯 IO 传输目录中续传。Git 只登记本纸稿、源码、参数和简明运行/SHA；本稿不把 raw 数据变成可提交附件。
