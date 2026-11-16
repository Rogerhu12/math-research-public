# 完整权八原来源前沿：1106＋180＋100 接口

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 实际对象与精确范围

本入口在同一合法固定系数剩余映射 $p=127,d\mapsto100$ 上，保留全部十二个 $y,w$ 参数、十个原模坐标及十八个原生成元来源。它只计算一层完整有界来源前沿，不计算 Bell 单位，不宣称稳定闭包，也不将有限域依赖式提升至特征零。

采用已付五十原列中的六条权五均值 $Y_j$、二十条权六交换子 $C_\ell$、十四条权八交换子 $D_\ell$。令它们生成的齐次子模为 $G$，原 Bell 多项式为 $b=y\cdot w$，并记

$$L_0=G+(b-1)B^{10},
\qquad L_1=L_0+\sum_{i,j}B V_{ij},\qquad V_{ij}=N_iY_j.$$

三十条 $V_{ij}$ 已有完整原十八来源及实际权七秩 312。本步要检查的是全部一百条

$$W_{i\ell}=N_iC_\ell\qquad(0\le i<5,\ 1\le\ell\le20)$$

在完整齐次空间

$$G_8+\sum_{i,j}B_1V_{ij}$$

之外是否有新的常数线性方向。没有把三十列相对较小前缀独立当作全 $L_0$ 的独立性，也不直接把八十列送去新的无界候选计算。

## 2. 新列的原十八来源

原十生成元向量是

$$m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4)^{\mathsf T}.$$

已付全部五个 $N_i$、五个原来源矩阵 $S_i$ 满足

$$m^{\mathsf T}N_i=u_i m^{\mathsf T}-A^{\mathsf T}S_i,$$

其中 $A$ 是五个 $u$ 梯度、六个 $w$ 梯度、六个 $y$ 梯度和 $b-1$。若 $m^{\mathsf T}C_\ell=A^{\mathsf T}\sigma_\ell$，就有

$$m^{\mathsf T}W_{i\ell}
=A^{\mathsf T}\left(u_i\sigma_\ell-S_iC_\ell\right).$$

程序对一百条新来源逐完整多项式乘回验证。它还重新验证全部五十个乘法列身份、全部四十条所用父种子的原十八产品，以及三十个父 $V_{ij}$ 的十坐标和十八来源产品。$y_aV_{ij}$ 使用字面的参数乘子 $y_a$ 及同一来源乘子，不另换规范。

所有原 $u$ 变量都保留在来源系数中；只有十个模坐标要求为纯参数多项式。原十七梯度的完整 Jacobian 运输由同一父模型及其固定来源身份承接。

## 3. 完整 17674 行与 1386 列

仍取 $\operatorname{wt}(y)=1$、$\operatorname{wt}(w)=2$，十个模坐标权为 $(0,2^5,4^4)$。完整权八输出数为

$$|B_8|+5|B_6|+4|B_4|
=8007+5\cdot1715+4\cdot273=17674.$$

原输入依次排列：

| 原来源组 | 完整乘子 | 列数 |
|---|---|---:|
| 六均值 $Y_j$ | 全部 $B_3$ | 552 |
| 二十条 $C_\ell$ | 全部 $B_2$ | 540 |
| 十四条 $D_\ell$ | 常数 1 | 14 |
| 三十条 $V_{ij}$ | 全部六个 $y_a$ | 180 |
| 一百条 $N_iC_\ell$ | 常数 1 | 100 |

前三组合成完整 $G_8$ 的 1106 列，其已付秩 1106 会在本次结果中再次核对。加上 180 列后的完整父前缀为 1286 列；它的秩不预填。再加全部一百条新列后，总数为 1386。

每个原种子标签、乘子指数、全部输出坐标及每个非零系数都保存在同一完整字典中。任何原非零项不在权八输出字典即失败。没有参数点采样、随机行选择或高次数删项。

## 4. native 与完整删列门

逐字复用已审 `original-parameter-seed-compression-rank127` native 和原 F127 位面头文件；真实尺寸仍在该协议的 20000 输出、2000 输入上限内。输入文件 header 的目标起点为 1286，仅最后一百列需要逐列分类；前缀允许有真实线性依赖，不能假其秩 1286。

native 先完成 244990 项域运算自检和 25 项独立普通标量小矩阵产品，再按固定原输入顺序消元。只有完整处理的原行才进入状态；预算退出只保存真实整行前缀。每个被删除目标的关系保持其原目标系数严格为 1，并只使用先前真实独立原列。

Python 消费者对每条新列，不论保留或删除，都重建其表达式并实际核：

1. 全部十个参数多项式坐标相等；
2. 同一系数作用于原十八来源后的完整乘回等于该新列的原目标。

只有这两门全成，才将该列记为已处理。若保留集合是 $K$，最终可宣称的完整 $B$ 子模等式为

$$L_1+\sum_{i,\ell}B W_{i\ell}
=L_1+\sum_{(i,\ell)\in K}B W_{i\ell}.$$

若 $K$ 为空，本步确给全部一百条在 $L_1$ 内的原来源表达；这仍不证明 $N_i$ 对全部 $L_1$ 稳定。若 $K$ 非空，只能说其在声明的完整权八父空间商中独立，不能免费推全未截断 $L_1$ 扩大。后继 $e_0$ 正证仍需真实十坐标、十八生成元、原十七梯度加 Bell 的完整来源；特征零乘回须另付。

## 5. 输入绑定与可重复计算

主源：

~~~text
notes/2026-11-16-r150-original-complete-weight8-frontier127-789f.py
blob 4e8f554b0979ec9c05d0c8c2dfdb024151de3b6b
22828 bytes
SHA256 bf5fa8e6ea1a70ed9441cf28918c9bd46946661afd932c7888f713dc2eadc936
~~~

全部 helper 的 path/blob/bytes/SHA 记于同名 `inputs-789f.json`。原 model、compression、mean-frontier 三个父步骤必须真实 `completed`，来源与 binding 匹配，各当前 manifest 必须与其实际 receipt 的完整描述符匹配。

三十个父新列另以完整 phase 描述符映射钉住：canonical JSON 为 7561 bytes / SHA-256 `84602b544bc3a7275ba3e0d4aa6cbcdfb87eb01c29f5ddca045a344e3144c2df`。每个物理 gzip、逻辑 JSON、原向量与原来源都再完整核验。该映射只含同一三十个数学阶段，不含 native 用时；允许真实重建同一父数学数据，不要求伪造旧运行耗时。当前父 receipt、manifest 物理身份仍进入本次 continuation 状态，实际换父文件不能静默续旧状态。

使用 Python 3.12.14、python-flint 0.9.0、`g++ -std=c++17 -O3`。不需要 Singular。若转 Actions，也必须固定同一 Python 版本，不能绕过已锁 gzip 字节身份。

## 6. CLI、预算与阶段

~~~text
python notes/2026-11-16-r150-original-complete-weight8-frontier127-789f.py
  --model-source {scripts}/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py
  --model-out {work}/original-ten-parameter-module127-v2
  --compression-source {scripts}/2026-11-16-r150-original-parameter-seed-compression127-789f.py
  --compression-out {work}/original-parameter-seed-compression127
  --mean-frontier-source {scripts}/2026-11-16-r150-original-mean-first-frontier127-789f.py
  --mean-frontier-out {work}/original-mean-first-frontier127
  --native-source {scripts}/2026-11-16-r150-original-parameter-seed-compression-rank127-789f.cpp
  --header {scripts}/2026-11-15-r150-original-f127-bitplane-789f.hpp
  --out {work}/original-complete-weight8-frontier127
  --through final --seconds 180 --memory-mib 768
~~~

外层 240 秒。`--through prepare` 只完成一百原来源、全部父来源回读和完整输入，没有秩结论。各新来源及每条完整表达式分别事务封存；相同源码、参数、原父文件和 binding 下可继续这些完整阶段。native 只复用实际已保存的完整原行状态。

Exit 75 表示已记录的真实预算前缀，不算完成；算术、文件、原来源或编译门失败保留 exit 1 与具体诊断。本接口冻结时只有真实 AST 语法检查，没有新数学运行，不预填一百列的保留数、前缀秩或最终秩。

## 7. 数据边界

所有原多项式数组、完整输入、原字典、native 状态、SSI 和 raw 回执只放临时目录。仓库只保存源码、参数、证明及实际运行身份/SHA。此次不启动权十的 $77276\times10152$ 矩阵，也不将八十列或其它未完成前沿直接当成稳定模。
