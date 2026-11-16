# 原 rank-four 图的权七／权八指定 RHS：只读完整状态接口

作者：Astra-ISP-789f / literature_audit，与 /root。AI-assisted GPT-6 Astra Pro。  
日期：2026-11-16。

## 1. 要证明的具体正门

本入口固定同一合法剩余映射 $\mathbf F_{127},d\mapsto100$，保留全部十二个 $y,w$ 参数和十个原模坐标。令 $b=\sum_i y_iw_i$，$\delta$ 为 chart 14 的原四阶 mean 子式，原列位置为 $[2,3,4,5]$。

它消费已经完整完成的两个原有界来源空间：

| 已完成空间 | 全输出坐标 | 全原输入列 | 实际秩 | 新指定目标 |
|---|---:|---:|---:|---|
| 权七 $G_7+\langle N_iY_j\rangle$ | 7754 | 312 | 312 | $b\delta e_0$ |
| 权八 $G_8+\langle y_aN_iY_j,N_iC_\ell\rangle$ | 17674 | 1386 | 1312 | 六个 $y_i b\delta e_0$ |

权八原 1386 列包括完整的 1106 列 $G_8$、180 列 $y_aN_iY_j$、100 列 $N_iC_\ell$。本入口保留其字面顺序，没有采用后继换列，也不重新消元这个矩阵。

若权七目标有原梯度来源 $b\delta=\sum_i F_iA_i$，则

$$
\delta=\sum_iF_iA_i-\delta(b-1).
$$

若权八六个目标全部有原梯度来源 $y_i b\delta=\sum_jF_jA_{ij}$，则乘 $w_i$ 求和后

$$
b^2\delta=\sum_jF_j\left(\sum_iw_iA_{ij}\right),
\qquad
\delta=b^2\delta-(b+1)\delta(b-1).
$$

因此任一路真实成功都给出该图上的字面 $\delta$ 来源，倒置 $\delta$ 后即得原规范化理想的单位。它不自动支付另外十四个图，也不把有限域来源提升到 $E$ 或 $\mathbf Q$。

指定空间的非零余式只说明对应目标不在本次声明的有限来源空间中。它不排更高权来源，不排完整稳定闭包，也不排局部原理想为单位。

## 2. 原父身份和完整性门

每个父步骤必须真实为 completed，完整 raw receipt 指向当前 manifest；源码 SHA、语义 binding、原来源门、实际 rank 全部匹配。新程序另独立硬锁每个父的字面 dictionary、全 original input、完整 row state 和完整 result 四个物理 SHA。

权八父的主要固定身份是：

~~~text
parent binding
1fdb39f00f53e51f33cbecef6c25c503c43e85575ad79abbd189ade9fdc7d069
native binding
721ca4b226e01fe685efc7753fbf24aa335e82f7863b82118024b829c18b5d6d

complete-row-state.bin
22008128 bytes
SHA256 e561e3652a0dd2583c8c6b2206c34f5e1c8b0ab4d77275a35b25f16db5ae581e

all-original-row-input.bin
24496256 bytes
SHA256 b9c8085459685cdf728e9ba8cbc005daccfc80a0d8047ddccddb008e4002249a
~~~

权七父为 312 个原单位行的完整状态；其精确 state 为 2212820 字节、SHA-256 `c5553497e614338fc5a811ad5bce78571d1d835e32f269435f756e822e2e35df`。全部其它 bytes/SHA 及来源源码 pin 见 [输入清单](2026-11-16-r150-original-rank-four-bounded-rhs127-inputs-789f.json)。

程序从原单项式规则重建全部输出标签和输入标签，再逐项与已锁字典比较。它不把某个内部未完成状态、最后一次内存对象或相近尺寸文件当作完整父。固定四个数学文件的 SHA 在消费者末端再次核对，证明父文件未被修改。

完整模型仍逐项核原十七梯度的 Jacobian 运输。所选六个 mean 的二十四个二次系数逐项与原四个矩阵匹配；选定子式的两侧 adjugate 产品再次核验，并与先前 chart 14 的规范多项式 SHA 比较。

## 3. 只读 native 及来源符号

新增 native 只包含冻结的原 rank native 和位面头文件，改名其 main 后不调用原 main。它复用已审完整状态读取器和原有限域运算，自测仍保留；没有对任一父输入重新做 Gaussian 消元。

完整状态必须满足 next 等于全部原输入行数，rank 等于已付 312 或 1312；规范单位、原独立来源标签、无未来来源、前导零、padding、全部依赖关系和 EOF 全部保留原读取门。

对目标 $T$，初始原来源系数全零。用已付规范行消去后保存完整余式 $R$ 和全部原输入系数 $q$，符号固定为

$$
T=\sum_{j=1}^{n}q_jV_j+R.
$$

它没有只保存被选枢轴的系数。权七保全部 312 项，权八每列保全部 1386 项。随后从原完整 input 文件重读全部标量，独立核每个输出坐标的上述恒等式：

$$
7754+6\cdot17674=113798
$$

个原标量产品全部通过，才保存结果。

累加只跨最多 2000 个系数项，每项不超过 $126^2$，因此原 unsigned 32 位累加界严格小于 $2^{25}$。位面域运算仍做全部原自测；这个小自测不等于重新消元父矩阵。

独立 RHS 协议将父 binding 与新消费者 binding 分别保存，不伪装成原父输入。所有输出数组仍只写新临时目录。

## 4. 从零余式到完整原来源

每个零余式都要经过以下实际门，不能只依据 native 的零计数：

1. 按字面输入标签把 312 或 1386 个常数系数聚合成原种子的参数多项式乘子。
2. 读取每个用到的原种子或 $N_iY_j/N_iC_\ell$ 阶段，逐文件 stored/logical 双 SHA 和来源身份核验。
3. 重建全部十个模坐标，确认它们严格等于声明的目标向量。
4. 重建完整十八生成元来源，逐整个多项式乘回；本步另硬核第十八个 Bell 来源系数为零，所以得到的确为十七梯度来源。
5. 经同一已付 Jacobian 矩阵转回全部原十七物理梯度，再做完整多项式乘回。

只有相应一个或六个目标全部完成，才执行第 1 节 gluing。其最终十八生成元产品和原十七梯度加 Bell 产品都必须严格等于字面的 $\delta$。完整系数与来源证书分别封存在临时 phase；仓库不保存它们。

## 5. 冻结源码

主 Python：

~~~text
notes/2026-11-16-r150-original-rank-four-bounded-rhs127-789f.py
blob 18d8e4f21b5ce464e2b47b0a40ff040df4aa6009
25458 bytes
SHA256 f613a6d1ed47548117e7b725b6680ea6bd3b3e147b1fa88d2d3a64784177d34f
~~~

新增只读 native：

~~~text
notes/2026-11-16-r150-original-completed-row-rhs127-789f.cpp
blob 97c6316a82e7e1a570496db044074417bcc88034
5825 bytes
SHA256 9707a53c28f7c3082fec631675aea3974b2f637cdd5c5333bfeee46dac5d05a1
~~~

原 rank source 为 9682 字节、SHA-256 `c5c36af57f8d75d2aac7d42b4048be2c8f382fdbe9ed4a0ebefdf85f0c93bd9f`；原位面头文件为 4691 字节、SHA-256 `03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3`。它们逐字复制到新的独立 build 目录，没有修改原文件。

全部九个源码 pin、固定父状态及完整 CLI 见输入清单：blob `59a5cdf4c5c2e74a640f2a38303a77b75481b2de`，6735 字节，SHA-256 `e77c9689d52c35b48257f0968bcf37f673063e6805d7060ed9620fdd5beac338`。

本接口冻结时只完成真实 Python AST 检查和新增 native 的 g++ 编译（exit 0、编译日志为空）。没有新目标数学读数，不预填任何零余式。

## 6. 运行与预算

建议复用当前真实存活且逐 SHA 核过的父目录

~~~text
/tmp/r150-normal-789f-20261116-1040
~~~

在另一个新 out 目录调用输入清单的完整 CLI，Python 为

~~~text
/tmp/r150-normal-789f-20261116-1040/venv/bin/python
~~~

使用 180 秒、2048 MiB，外层 240 秒。无需 Singular。它只读两个已完成原消元，不重做原模型、原 17674 行消元或旧大来源链。

同绑定可续已完整 native 结果和已完整来源 phase；预算 75 不作为完成。未完成的新 native 输出不得采用，数学或身份门失败保持 exit 1。对真正零余式的完整原来源重建若预算不足，后继只能从这些真实已保存的完整阶段继续。

最终完成状态区分 field-positive 与 specified-space-diagnostic。只有相应最终 gluing 门通过才称该 chart 的原正证；其它结论均保留上述精确范围。
