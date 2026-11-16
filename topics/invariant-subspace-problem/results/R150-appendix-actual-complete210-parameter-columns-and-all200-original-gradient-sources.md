# R150：完整 210 个参数列与全部 200 个原梯度来源的实际封存

作者：Astra-ISP-789f / normal_annihilator，与 /root 协作。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

## 1. 本条已经完成的结论

在原数域的合法约化 $\mathbb F_{127}$、系数根 $d=100$ 上，保留全部十二个参数 $y,w$，完整第二轮的 104 个新列及其十八生成元来源现已逐列实际构造、乘回并封存。它们与原 106 列合起来，给出已证明完整性的 **210 列参数模表示**。删去十个原 Bell 列后，留下的 **200 列全部具有原十七梯度来源**。

本条把已经证明的有限生成定理落实为真实数组与可复核来源。它没有执行新的 Gröbner 基或大加权矩阵消元，没有给出单位理想结论，也没有把有限域来源升为特征零来源。

完整性所用的原定理分别是：

- [36 个种子、完整第一轮及原 106 列换源](R150-appendix-original-high-source-exchange-and-thirtysix-seed-stable-closure.md)；
- [至多两轮完成及完整 210 列表示](R150-appendix-original-parameter-stable-closure-stops-at-two-and-complete210-presentation.md)；
- [原特征零未压缩模型的独立两轮定理](R150-appendix-original-characteristic-zero-two-round-closure-and-finite-parameter-presentation.md)。

最后一条的特征零结论依靠原 $E$ 恒等式，并不依靠本条的有限域数组。本文的具体 210／200 列及其交换关系仍限定在 $\mathbb F_{127}$。

## 2. 原模型、字典及此次新增的列

记

$$
B=\mathbb F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad
S=B[u_0,\ldots,u_4].
$$

权为 $\operatorname{wt}(y_i)=1$、$\operatorname{wt}(w_i)=\operatorname{wt}(u_i)=2$。原十个保留单项式按固定顺序为

$$
\mathfrak m=(1,u_0,u_1,u_2,u_3,u_4,
u_1u_4,u_2u_3,u_2u_4,u_3u_4).
$$

令 $A=(A_0,\ldots,A_{17})$ 是已付原模型中的十八生成元：前十七个为经过完整双向 Jacobian 运输的原梯度，末项为 $b-1$，其中 $b=y\cdot w$。该运输保留全部原变量，并非参数点代入。原五个参数矩阵 $N_i\in B^{10\times10}$ 与来源矩阵 $S_i\in S^{18\times10}$ 满足逐坐标原恒等式

$$
\mathfrak m^T N_i=u_i\mathfrak m^T-A^T S_i.
\tag{2.1}
$$

原父 106 列的固定组成是：

| 来源族 | 列数 | 非 Bell 列的权 |
|---|---:|---:|
| 六个均值列 $Y$ | 6 | 5 |
| 二十个保留低交换子列 $C$ | 20 | 6 |
| 十四个原高交换子列 $D$ | 14 | 8 |
| 全部 $N_iY_j$ | 30 | 7 |
| 原权八计算选出的 $N_iC_j$ | 26 | 8 |
| 十个 $(b-1)e_a$ | 10 | 高权 $3+\operatorname{wt}(\mathfrak m_a)$ |

所以父列中有 96 个非 Bell 列。该 106 列与完整第一轮的等价已由原 74 条核关系及十四条换源实际支付，本文不重做那次消元。

只对四个固定、有序的二字路径

$$
\mathcal K=((1,4),(2,3),(2,4),(3,4))
\tag{2.2}
$$

新增下列列：

$$
N_pN_qY_j\quad((p,q)\in\mathcal K,\ 0\le j<6),
\qquad
N_pN_qC_a\quad((p,q)\in\mathcal K,\ 0\le a<20).
\tag{2.3}
$$

两族分别为 24 个权九列和 80 个权十列，合计 104 列。这里的算子次序是先 $N_q$、再 $N_p$；没有把自由十维空间上的矩阵预先视为可交换矩阵。

低交换子所用原种子索引完整固定为

~~~text
1,2,3,4,5, 11,12,13,14,15,
21,22,23,24,25, 31,32,33,34,35.
~~~

它们是原一百个交换子字典中的真实列，不是新任选的系数规范。

## 3. 每条新来源的完整公式与实核门

若已有列 $v$ 及其来源 $\sigma(v)$ 满足

$$
\mathfrak m^T v=A^T\sigma(v),
$$

则由 (2.1) 得到

$$
\sigma(N_iv)=u_i\sigma(v)-S_iv.
\tag{3.1}
$$

因此本次每一条二字来源为

$$
\sigma(N_pN_qv)
=u_pu_q\sigma(v)-u_pS_qv-S_pN_qv.
\tag{3.2}
$$

程序先读取已经支付的真实第一步 $N_qv$ 及其来源，而不是仅用第一步的哈希作算术替代。每种所用第一步均重新计算十坐标与十八来源，并核对完整乘回。随后按 (3.1) 生成第二步，且在注册该列的原子阶段之前，实际要求：

1. 十个向量坐标与十八个来源坐标完整保留；
2. 十坐标不含 $u$，全部十二个参数保留；
3. 每个向量单项式具有声明的权九或权十；
4. 原多项式恒等式 $\mathfrak m^TN_pN_qv=A^T\sigma(N_pN_qv)$ 全部成立；
5. 第十八个 Bell 来源系数严格为零。

来源公式从已付齐次边界恒等式递推，故每个非零的原梯度来源项具有对应总权。均值新列的来源 $u$ 次数至多 2；交换子新列至多 3。程序实际统计的总最大值为 3。

每一整列通过全部门后才写入压缩阶段并原子更新 manifest。恢复时同时核完整压缩 SHA、解压后逻辑 SHA、格式、绑定及原字面列标签。未完成的列不计入进度。

## 4. 真实分阶段执行

执行环境固定为 Python 3.12.14、python-flint 0.9.0。本次三阶段均为同一冻结 v2 源、同一新绑定及同一独立输出目录。

| 阶段 | 预算 | 实际秒数 | 峰值 RSS KiB | 实际完成 |
|---|---|---:|---:|---|
| prepare | 180 秒／768 MiB | 27.174693003995344 | 95168 | 106 个父来源、50 个边界、九个字面路径；56 个第一步实际重放 |
| mean | 120 秒／768 MiB | 31.453019320004387 | 95356 | 全 24 个均值二字来源；12 个所需第一步实际重放 |
| final | 300 秒／1024 MiB | 291.63911485300923 | 130532 | 全 80 个交换子二字来源；40 个所需第一步实际重放；完整 210 列索引 |

三个子进程均真实退出 0。final 严格核复用的 24 个完整均值阶段，没有把它们当作本轮新算的 80 条来源。最后共有 106 个完整阶段：父验证 1 个、新来源 104 个、完整模型索引 1 个。

104 个新列的实际规模为：

| 数据 | 实际项数 |
|---|---:|
| 十坐标向量的参数单项式总数 | 7,034,750 |
| 十八来源坐标的单项式总数 | 2,707,447 |
| 最大来源 $u$ 次数 | 3 |

全部阶段的压缩字节总数为 70,340,461；逻辑字节总数为 401,134,398。这些数学数组只保存在临时工作目录，未写入仓库。

### 4.1 先前失败的准确范围

v1 的 prepare 已真实完成；v1 的 mean 在构造第一条新列后的统计序列化处报 `TypeError: Object of type fmpz is not JSON serializable`。该列尚未注册，因此 v1 新列计数严格为零。

v2 唯一执行行为差异是把 `sourceMaximumUDegree=max(...)` 外包为 `int(max(...))`；另将格式标识改为独立 v2。它没有放宽任何来源门。v2 使用新的源路径、绑定及输出目录，并重新完成 prepare，没有跨绑定挪用 v1 的阶段。

v1 的成功与失败身份均保留；本条的 104 列结论全部来自上述真实 v2 执行。

## 5. 从实际来源到完整 210／200 列表示

记 $L_{36}$ 为六个均值、二十个低交换子和十个 Bell 列的 $B$ 子模。已付定理给出

$$
\operatorname{Cl}_N(L_{36})=L_{36}^{(2)}.
\tag{5.1}
$$

完整第一轮已由本文的父 106 列生成；全部二字作用在原十一条二次关系下化为 (2.2) 的四条字面路径，其误差落在完整第一轮。因此 (2.3) 的 104 列补齐后，确实生成 (5.1)，不是仅生成一个未证明完整的候选子模。

该两轮论证的交换子、二次关系和三次降次部分不使用 Bell 列。删去十个 Bell 列，所得 200 列生成完整齐次非 Bell 子模 $\Gamma_2$，并有

$$
B^{10}/\Gamma_2\simeq S/J_{17},
\qquad
B^{10}/\bigl(\Gamma_2+(b-1)B^{10}\bigr)
\simeq S/(J_{17},b-1),
\tag{5.2}
$$

其中 $J_{17}$ 为同一原十七梯度理想。200 列按权的数量是

$$
(6,20,30,40,24,80)\quad\text{对应权 }(5,6,7,8,9,10).
$$

“完整表示”是 (5.2) 的余核同构，不是说自由参数模秩为十，也不是说 200／210 列独立。本文没有求该参数模的秩、Fitting 理想或单位来源。

## 6. 固定源、参数及执行身份

本次源码：

~~~text
notes/2026-11-16-r150-original-two-round-complete210-sources127-v2-789f.py
blob 9fede0af90889e05eb07cfc87146bec707844794
22552 bytes
SHA256 20cb960bc20fea18001488e84dae35518d74f3338697dfed619eaadae6a6b2aa
~~~

参数与完整 CLI：

- [冻结 inputs](../notes/2026-11-16-r150-original-two-round-complete210-sources127-inputs-v2-789f.json)，blob `6593dbf10947a38dabd9f56120a7bf487f379b67`；
- [执行接口](../notes/2026-11-16-r150-original-two-round-complete210-sources127-interface-v2-789f.md)，blob `7a40c86fe64a4ee93508b4ae479a2f3acbf89f8d`。

三份实际执行身份分别为：

- [prepare](../notes/r150-original-parameter-module-execution-789f/local-20261116-original-complete210-sources127-v2-prepare180.json)，blob `643e5833236908107d8ff6d9e952861ead213b2b`；
- [mean](../notes/r150-original-parameter-module-execution-789f/local-20261116-original-complete210-sources127-v2-mean120.json)，blob `4645f94c4c020113ca1890da57e6d0a8968f2b0a`；
- [final](../notes/r150-original-parameter-module-execution-789f/local-20261116-original-complete210-sources127-v2-final300.json)，blob `5dad06f965cea310623fa6fe9964d8ce1ab3e942`。

共同绑定及 final 的完整身份如下：

~~~text
binding
41638323f597133aadeb65b2a1639899a162e2afbe6e7f7c477e93fae912cd80

final raw receipt: 32576 bytes
77724520a9b2aa89086d7bb39e7dcef48bbc1cef2faaef00e9d98fcc588b24ea

final manifest: 144113 bytes
74eb5557203192b2b3e37b43189ceaa7ec34afeb698884f336331210d1bcf2ff

complete-original210-source-model.json.gz: 35044 bytes
ed0b6811561a0799dff2cab99b2c7685a2ed820978be00c397a69f110972fed5
logical: 148424 bytes
f8b17d755d1515726632280fe110788dcf03128705172944a67d44f12de14bee
~~~

完整模型索引直接引用所有 106 个父列及 104 个新列的真实描述符。原种子描述符来自父 manifest 的 `seeds` 字典；其 `seed-xxx` 标签是语义标签，不能误当作父 `phases` 的键。

## 7. 后续可用范围

此后消费者可以使用这 200／210 列及其完整原来源，进行受控的齐次目标读取或 Bell 局部正来源搜索。所有未注册阶段、未给出的特征零提升和未完成的单位恒等式都仍在本条范围之外。新增权九、权十列不会改变原齐次权七、权八部分；已有相应低权原目标诊断不需要因本次数组封存而重跑。

## 8. 根独立全原复核

/root（OpenAI ChatGPT / GPT-6 Astra Pro）全文审查原源和本稿。[此前24均值独立核](../notes/2026-11-16-r150-original-complete210-mean24-source-checkpoint-789f.md)已实际完成；本次[80交换子独立审计源码](../notes/2026-11-16-r150-original-complete210-commutator80-source-audit-789f.py)不导入producer/helper，直接解码原模型和全部实际阶段。

实际session15362、exit0，158.70670321000216秒、216876KiB；全800个十向量递推坐标、1440个原十八来源递推坐标与80个完整原多项式乘回通过。全部来源项连同原生成元严格同权10，Bell源零、最大$u$次3。24旧均值仅复核与已付独立审计的双SHA相同，不重其算术。

80新列实6,132,866向量项、2,429,334来源项；与24均值实901,884及278,113合并，准确等于正文104总项数。全部106phase的双SHA及总字节已核。根源7440字节/SHA `be2cf5d779a677501d579886ab9466bdeeb03bcbc55b4b33deba1e2613de0a22`；raw834字节/SHA `894339ed3e81755834521c47c7226571839b78a60dc4397450e1dc8ce43a6a53`仅TMP。[运行身份](../notes/r150-original-parameter-module-execution-789f/local-20261116-original-complete210-commutator80-root-audit.json)记录完整输入输出。

完整非Bell商另见[200列证明](R150-appendix-original-nonbell-two-round-twohundred-presentation-and-weight-thresholds.md)，原十八来源权界见[独立过滤等价](R150-appendix-original-eighteen-source-weight-filtration-equivalence.md)。本次实际来源生产未把更高权成员性预填为完成。
