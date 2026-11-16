# R150：固定四阶均值图的七个完整有限来源空间余式

作者：Astra-ISP-789f / literature_audit，与 /root。AI-assisted GPT-6 Astra Pro。日期：2026-11-16。

本附录只使用合法剩余点 $\mathbf F_{127}$、系数根 $d=100$ 的原模型。它记录一次实际完成的指定右端计算，并区分该有限来源空间中的否定与完整原梯度理想中的成员性问题。数学数组和完整二进制输出留在临时目录；仓库只保存本证明、可重现源码、输入身份与执行身份。

## 1. 原空间与本次精确问题

令
$$
B=\mathbf F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],
\qquad \operatorname{wt}(y_i)=1,\quad \operatorname{wt}(w_i)=2,
$$
并令 $F=B^{10}$ 的原十个基轴具有权
$$
(0,2,2,2,2,2,4,4,4,4).
$$
原 Bell 多项式为 $b=\sum_i y_iw_i$，权为 $3$；$e_0$ 表示十个原单项式中常数 $1$ 的轴。

采用已付的原均值矩阵构造第 $14$ 个四阶子式 $\delta=\delta_{14}$，其权为 $4$。本次程序重新核验原四个均值矩阵、全部 $24$ 个均值系数、所选 $4\times4$ 方阵的两侧伴随恒等式，以及原 $17$ 个梯度的运输。所用 $\delta$ 的原多项式编码 SHA256 为
eff3070880440dd84f3b8d6bcfac5fc71461537d55b9f3d2c323a4287cdde0f6。
这里的原均值基与规范化 pencil 基相差已付的常数可逆变换；本附录始终保留此次实际输入的原基，不更换子式数值。

以下生成列都带有已付的原 $18$ 列来源，且梯度来源的最后 Bell 系数严格为零：

- 六列 $Y$，权 $5$；
- 二十列 $C$，权 $6$；
- 三十列 $V_i=N_iY_j$，权 $7$；
- 十四列旧 $D$，权 $8$；
- 一百列 $W=N_iC_j$，权 $8$。

记它们生成的齐次 $B$ 子模为 $\mathcal G$。已付十四列换源证明给出
$$
\mathcal G=B\langle Y,C,V,W\rangle.
$$
此等式不把 $\mathcal G$ 声称为完整稳定闭包。换源的准确范围见
[原高来源换基与三十六低种子稳定闭包](../results/R150-appendix-original-high-source-exchange-and-thirtysix-seed-stable-closure.md)。

本次所用的完整两个齐次部分是：

| 权 | 完整原输入矩阵 | 完整秩 | 原输入构成 |
|---|---:|---:|---|
| $7$ | $7754\times312$ | $312$ | $6Y\cdot B_2$、$20C\cdot B_1$、全部 $30V$ |
| $8$ | $17674\times1386$ | $1312$ | 完整旧 $G_8$ 的 $1106$ 列、全部 $180y_iV$、全部 $100W$ |

它们保留全部原输出坐标与全部原输入来源。本次只读取这两个已经完整结束、逐 SHA 绑定的单位行状态；没有重做原消元，也没有使用未完成状态。

## 2. 实际七个余式

对
$$
b\delta e_0\in F_7
\quad\text{及}\quad
y_i b\delta e_0\in F_8\quad(0\le i\le5)
$$
分别执行完整降约，保留全部 $312$ 或 $1386$ 个原来源系数。原输入乘回逐坐标证明
$$
T=Xq+R.
$$
程序核验全部 $113798=7754+6\cdot17674$ 个原标量乘积；每个 $R$ 在全部父单位主元坐标处均为零。父基完整，故 $R=0$ 与该右端属于所列完整有限空间等价。

实际结果为：

| 原右端 | 原余式非零坐标数 |
|---|---:|
| $b\delta e_0$ | $5371$ |
| $y_0b\delta e_0$ | $13123$ |
| $y_1b\delta e_0$ | $13103$ |
| $y_2b\delta e_0$ | $13105$ |
| $y_3b\delta e_0$ | $13109$ |
| $y_4b\delta e_0$ | $13099$ |
| $y_5b\delta e_0$ | $13092$ |

因此严格有
$$
b\delta e_0\notin\mathcal G_7,\qquad
y_i b\delta e_0\notin\mathcal G_8\quad(0\le i\le5).
$$
这些是逐列结论；没有从非零坐标数声称七个余式线性独立。

若首列余式为零，本次正门会由
$\delta=b\delta-\delta(b-1)$ 给出原 $\delta$ 来源；若六个后列全部为零，会由 $\sum_iw_i(y_i b\delta)=b^2\delta$ 及
$\delta=b^2\delta-(b+1)\delta(b-1)$ 给出来源。此次没有任何零余式，故没有产生这类正来源证书。

## 3. 一个严格的有界 Bell 来源推论

这里的“来源权至多 $K$”有以下明确含义：写
$$
\delta e_0=G+(b-1)H,\qquad G\in\mathcal G,\ H\in F,
$$
时，每项梯度生成列及其系数的总权至多 $K$，并且 $\operatorname{wt}(H)+3\le K$。这不允许先引入更高权来源、再以最高项相消降低最终输出。

因为 $\mathcal G$ 的所有生成列权至少为 $5$，它的权 $0,\ldots,4$ 部分为零。若上述表示的来源权至多 $8$，把 $H$ 分成齐次部分；由权 $0,\ldots,3$ 的等式依次得 $H_0=\cdots=H_3=0$，权 $4$ 的等式给
$$
H_4=-\delta e_0.
$$
权 $7$ 的等式随后强制
$$
G_7=-bH_4=b\delta e_0.
$$
因此来源权至多 $8$ 的这种 Bell 表示必然要求
$b\delta e_0\in\mathcal G_7$。反过来，若该成员性成立，则
$\delta e_0=b\delta e_0-\delta(b-1)e_0$ 已给来源权至多 $7$ 的表示。

所以在这个准确的来源空间与权约束下，
$$
\delta e_0\text{ 有权至多 }8\text{ 的 Bell 来源}
\quad\Longleftrightarrow\quad b\delta e_0\in\mathcal G_7.
$$
实际首余式非零，排除了这种权至多 $8$ 的表示。

该推论不直接适用于 $y_i\delta e_0$：它的权为 $5$，而 $\mathcal G_5$ 已可非零，最低权比较必须保留额外的梯度项。也没有由此排除扩大稳定闭包、更高权来源或完整原理想中的 $\delta$ 成员性。

## 4. 原来源与范围

完整父状态、原输入、字典和结果均在运行前核验 SHA；运行后再次核验它们未改变。新的降约读取器保留全部原来源系数，并以原输入的普通系数乘积核验每个右端，未用消元内部等式替代最终原乘回。

上述矩阵属于原 $\mathbf F_{127}$ 模型。其负结果不提升为特征零结论，也不排除完整原梯度理想或 Bell 局部化理想的成员性。本次没有计算新的 Gröbner 基，没有把七列负结果作为整个十九图覆盖的否定。

可重现的源码与完整输入约定是：

- [指定右端消费者](2026-11-16-r150-original-rank-four-bounded-rhs127-789f.py)；
- [完成状态只读原来源读取器](2026-11-16-r150-original-completed-row-rhs127-789f.cpp)；
- [完整输入身份](2026-11-16-r150-original-rank-four-bounded-rhs127-inputs-789f.json)；
- [接口与原正门](2026-11-16-r150-original-rank-four-bounded-rhs127-interface-789f.md)；
- [本次实际执行身份](2026-11-16-r150-original-rank-four-bounded-rhs127-local-execution-789f.json)。

## 5. 实际执行身份与启动边界

实际独立计算于 2026-11-16 14:38:44.035596 UTC 启动，14:38:51.742357 UTC 完成，exit code 为 $0$。源码计时 $7.559555421001278$ 秒，外层墙钟 $7.706783040994196$ 秒；预算 $180$ 秒、$2048$ MiB。父 Python 峰值 RSS 为 $107920$ KiB，子进程峰值为 $195616$ KiB（包括编译）。

数学绑定为
e7a6e012e59891f741e579181bf7f5fcf2f5d872e688959e2255967a06c98baa。

完整原回执为 $6587$ 字节，SHA256：
48fcfcbf7b2f482c11c82927eef843d1c219805c1f564294fecef179637863ed。

完整 manifest 为 $9055$ 字节，SHA256：
1d2fa67473940ea6a64225b6e66cda850e320d0cbb8707ab50315c4a40185ce4。

两份完整新原结果分别为 $8230$、$114544$ 字节，SHA256：
7bcacd54b6398ba22959e8ccaa3eb60024403bc4a323b73482ca9dd8c2ef3999、
89936c7d48b6be0801b9d35546aab9a660a2524465b5635e295c787f377891db。

首次外层尝试调用未安装的 /usr/bin/time，启动器返回 FileNotFoundError，**数学进程尚未启动**。该启动失败身份独立保留；随后用同一未改源码直接运行 Python 得到上述实际结果。它不是一次数学失败或预算暂停，也没有覆盖任何父状态。


## 6. 根的独立全部坐标复核

根先独立回读完整 raw、manifest、两个新阶段的 stored/logical 双 SHA 及全部新 native 文件，再以另一套二进制解析和普通 python-flint 矩阵乘法，从两个完整原输入重新核验全部 $113798$ 个坐标的 $QX+R=T$。全部父主元处的余式为零，七个非零坐标数也与上表一致。此过程不调用 native 降约器或其解析函数，不重做父消元。

实际独立审计 exit 0，耗时 13.503492032003123 秒，峰值 646464 KiB。源码见 [完整原输入产品审计](2026-11-16-r150-original-bounded-rhs-full-product-audit-789f.py)，5528 bytes / SHA-256 `e3d5e1cdc56a4c1fec6859ba0cf69ba8e1d8bc726215f3c58583ffad3252d4cd`；完整临时 raw 为 666 bytes / SHA-256 `2c8be079fc96ed5483461ffd7f8b2af93a8ad2ac76d12e50605f5e4f6b5a0fb1`。执行身份见 [根审计记录](r150-original-parameter-module-execution-789f/local-20261116-original-bounded-rhs-full-product-audit.json)。该复核仍只支付上述两个有限来源空间的结论。
