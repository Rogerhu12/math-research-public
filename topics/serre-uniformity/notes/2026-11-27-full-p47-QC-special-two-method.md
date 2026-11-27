# 原 full47 两个特殊 CM 圆盘的独立 QC 续请求

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

本入口只读标签0、141的两行原 QC 矩阵。
R1122 已关闭的六个圆盘不再计算；原成功请求和 workflow 保留。
本说明不预报两盘的矩阵秩或唯一性。

## 1. 不可变的共同输入

共同消费者仍是
`scripts/full_p47_QC_first_rows.py`，
其 SHA 为 ac9ac63dd31556b6b4952c71a5aa4b9c1e4826c9ccfb044bace50090cf861ea4。
R1122 的原六盘请求以完整 SHA
95e8ccb0bd7906f1c0c47fbebc794c77994b3fd5cba58766d31fbc53ac3dbc0b
作为不可变输入。

新的小请求只另外保存四条完整第三类值、该次自己的完整 Cartier 证书、
真实 run/job/source/request 哈希，以及新入口的源码 pin。
入口在内存中复制旧共同输入，严格替换这几项和请求的圆盘集合；
既不改旧文件，也不以字符串变换改数学源码。
旧高度、Jacobi 坐标、切向、角、$B_q$ 和 $\lambda_0$ 的全部来源及哈希原样消费。

仅新请求可触发独立 workflow。
新入口明确固定
$$
\mathrm{CM\_candidate\_ids}=[0,141],\qquad
(\mathrm{id},Z)\in\{0,141\}\times\{Z_A,Z_B\}.
$$
四条必须是该除子在自身目标的完整 R1118 行；
不能用旧十二条的 `all_eight_log_derivatives` 补缺。

## 2. 新四条实际来源

固定读取 run45998781656 / job140504817189，
source d935282c49c9c19d541729ca5bd59579aac7e82f，
首四短 Cartier v2 请求 SHA
ed9508e1cd4d0f4b9950c68eebde5ada7fddf29d1e63810df7e367bffa6b8bc2。

只有完整 receipt 的四条 clean rows 和该 receipt 的 Cartier 证书可以填入。
每条保自己的实际除子哈希、RR 维数、留数秩、全部尖点和最终除六。
共同原矩阵仍须满足
$$
C_{\rm row}=1-B_q(H),\qquad \det(1-C)=551,
$$
且完整 row/column 哈希与 R1121/R1122 严格一致。
新四条对应的 `all73_frame_values_sha256` 可以不同：
它包含本次新分子的读数，不能错误地要求等于旧十二条的哈希。

入口依次核新请求 SHA、旧共同请求 SHA、全部源码 pin、
四条 clean rows 哈希和实际 Cartier 证书。
父进程与 fresh-exec 的纯 flint 子进程都走这一同一入口。
Sage 与 wheel FLINT 的隔离保持原消费者规定。

## 3. 原公式和完成判据原样保留

调用的完整数学过程仍是原 `read_actual_QC_rows`：
$$
A_{Z,y}=-\operatorname{Tr}(KZb_y^2),\qquad
B_{Z,y}=\operatorname{Tr}(Kb_yd_{Z,y})-\alpha_{Z,y},
$$
其中 trace 保留全部73方向，$K=\kappa/a$、
$L=[\lambda_0,H\lambda_0,\ldots,H^{72}\lambda_0]$，
$\lambda_0=q^{-1}\log(B_qu_4)$。
原 $c_{-4}=B_q^{-1}$、fixed-cycle 的 $1/2,2/3,1/23$
以及两端的原 coarse 参数都不改。

每个新盘只在程序实际求得
$$
\gcd\bigl(t(B_{A,y}+A_{A,y}t),t(B_{B,y}+A_{B,y}t)\bigr)=t
$$
且至少一个 $B_{Z,y}\ne0$ 时，沿 R1103 的完整整尾与非$q$门，
宣称整个原 $j-j_{\rm CM}=4513t$ 圆盘只余原 CM 点。
若判据失败，记录真实失败范围，不能从六个旧盘外推。

本请求的数学预算仍为2400秒，reserve60。
只保源、小输入、输出小矩阵、run/job 和哈希；无 raw artifact。
本固定47结论即使完成，也不是一般素数的 Serre 绝对一致性证明。
