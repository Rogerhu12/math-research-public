# 原 rank4 图的未展开十行、四十六原来源局部正证接口

作者：ChatGPT（AI），Astra-ISP-789f / literature_audit。日期：2026-11-16 UTC。

## 1. 范围与冻结入口

本接口在已付的实际系数位 $\mathbb F_{127},d=100$，保留全部十二个参数 $y_0,\ldots,y_5,w_0,\ldots,w_5$。它消费原十行参数模块的五十个已核来源列，在一个字面的 rank4 mean 子式 $\delta$ 上局部化，搜索常生成元 $e_0$ 的原来源。它没有把这五十列的初始参数子模宣称为对五个矩算子稳定的完整 critical 模块。

冻结计算源为 `2026-11-16-r150-original-rank-four-unexpanded-local-source127-v2-789f.py`，Git blob `11f6bf80f1ced7e5a2a21ae0f763ffb7225102d6`，35070 字节，SHA256 `ee9bdabfdd325150b622e77a91d20eb814c642c8cb66bbf4734106466af630e3`。

格式是 `r150-original-rank-four-unexpanded-local-source127-v2`。本次固定 `--chart 14`，即按六个原 mean 列的四元子集字典选原位置 $(2,3,4,5)$。该选择来自实际十五图统计；新运行仍重新核全部十五个子式的两侧伴随矩阵乘积，不能只接受这一索引。

本文继承 [原五十六个七生成元图](../results/R150-appendix-complete-original-fifty-six-seven-generator-critical-charts.md) 的原来源约定，以及 [mean 二次型与完整 Bell 覆盖](../results/R150-appendix-original-mean-quadrics-dual-normalization-and-complete-bell-cover.md) 的十五个 rank4 子式和四个二次型图。单个 $\delta$ 图上的有限域正证不关闭十九图，不提升到原数域 $E$。

## 2. 四个 Bell 列的精确删除

记 $B=\mathbb F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5]$，$b=y^Tw$，原十个模生成元按

$$
 m=(1,u_0,\ldots,u_4,v_0,\ldots,v_3)
$$

排列。五十个原参数列记为 $V_j\in B^{10}$，每列有已经付清的原十八生成元来源 $\sigma_j$：

$$
 mV_j=\mathcal G\sigma_j,
 \qquad
 \mathcal G=(F'_0,\ldots,F'_{16},b-1).
$$

选定四个 mean 列组成分块矩阵

$$
 V_P=\binom{C}{A},\qquad
 C\in B^{6\times4},\quad A\in B^{4\times4},\quad
 \delta=\det A.
$$

程序用原二次型系数核 $A$，核全部十五图的 $A\operatorname{adj}(A)=\operatorname{adj}(A)A=\delta I_4$。原十个 Bell 列必须逐坐标恰为 $(b-1)e_i$。对每个被消的二次生成元轴 $k=0,\ldots,3$，有字面恒等式

$$
 \delta(b-1)e_{6+k}
 =\sum_{j=0}^3\operatorname{adj}(A)_{jk}(b-1)V_{P_j}
 -\sum_{i=0}^5(C\operatorname{adj}(A))_{ik}(b-1)e_i. \tag{2.1}
$$

因此只删除这四个 Bell 列，保留四个 pivot mean 列、其余原列以及六个低轴 Bell 列，得到 $V_{\mathrm{keep}}\in B^{10\times46}$。设其原 $B$ 列模为 $L_{46}$，五十列模为 $L_{50}$。所有列仍是原裸列，且

$$
 L_{46}\subset L_{50},\qquad
 \delta L_{50}\subset L_{46},\qquad
 (L_{46})_\delta=(L_{50})_\delta. \tag{2.2}
$$

程序核 (2.1) 全四十个原模坐标，并把右侧系数作用到各原十八来源，逐式核四个完整原十八生成元乘积等于左侧原来源乘积。它既不只看点上的秩，也不除未经证明的参数因子。

这与六行 Schur 公式相容，但本入口不展开 $\delta D-C\operatorname{adj}(A)B$。前一真实诊断已经核该矩阵的全部四百六十个原坐标；其 4,768,130 项表明展开体积大；首失败的具体分配位置未定位，故改用稀疏入口降低准备与序列化负担。现在保持十个原行，只作 (2.1) 的小块精确删除。

## 3. 实际局部模块与阳性终门

引入唯一新变量 $\rho$，使用原十行五十六列

$$
 \mathcal V=[V_{\mathrm{keep}},(\rho\delta-1)I_{10}]
 \quad\text{over }B[\rho]. \tag{3.1}
$$

原十七物理变量 $u$ 没有作为参数被代数专门化；它们留在原来源乘回中。矩阵 (3.1) 的参数系数只含十二个原参数和 $\rho$。候选引擎的顺序是固定权顺序 `wp(1,1,1,1,1,1,2,2,2,2,2,2,1),C`，`degBound=0`。

先实际完成独立二行、三列的 `slimgb/lift` 正负控制、单位输出及 FLINT 乘回，再完成本矩阵全部 560 个 SSI 往返坐标核。候选标准基完整返回并持久存在 tmp 后，才能算 $e_0$ 余式。非零余式只记录该初始局部参数子模的诊断，不作原完整理想非成员结论。

若余式为零，另调用目标单列 `lift(Original,Target,Units,"slimgb")`，要求 56 行来源且 $\mathrm{Units}=I_1$；核十个局部多项式乘积，并用独立 FLINT 解析器再次核全部十行。设前 46 个真实来源系数为 $\alpha_j(y,w,\rho)$，后十个为局部器系数。令

$$
 N=\max_{1\le j\le46}\deg_\rho\alpha_j,
 \qquad
 \widetilde\alpha_j=\delta^N\alpha_j(y,w,\delta^{-1})\in B. \tag{3.2}
$$

不需要把后十个局部器系数的 $\rho$ 次数计入 $N$，因为它们在 $\rho=\delta^{-1}$ 时严格消失。程序仍显式核

$$
 V_{\mathrm{keep}}\widetilde\alpha=\delta^N e_0 \tag{3.3}
$$

的全部十个多项式坐标，将它回填到原五十列（四个删除列的系数严格为零），然后构造并核

$$
 \delta^N=\sum_{j\in\mathrm{keep}}\widetilde\alpha_j\,mV_j
 =\mathcal G\left(\sum_{j\in\mathrm{keep}}\widetilde\alpha_j\sigma_j\right). \tag{3.4}
$$

最后使用已付全局三角坐标的十七乘十七 Jacobian 来源变换，逐十七原梯度加 Bell 生成元重新乘回同一个字面 $\delta^N$。只有这一完整终门允许 `completed-positive`。这是实际有限域的原来源，不是特征零来源。

四十六个清分母系数、十八个来源系数和十七个物理来源系数分别保存为完整 phase；末证书只引用这些带双 SHA 的 phase，避免再次把全部多项式组成一个 Python 大对象。所有多项式数据、SSI、原输出和日志仅留 tmp。

## 4. 原父身份与同 job 重建

Python 固定 **3.12.14**，python-flint 固定 **0.9.0**。这保原 gzip 的物理 header 身份；不能用不同 Python 版本的逻辑相同 payload 代过物理 SHA 门。

原模型源：`2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py`，23879 字节，SHA256 `4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4`。原模型 binding 是 `7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4`，manifest 30466 字节，SHA256 `9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2`。

原压缩源：`2026-11-16-r150-original-parameter-seed-compression127-789f.py`，20434 字节，SHA256 `b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9`。压缩 binding 是 `baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca`；其完整 116 列反向展开和保留索引的纯数学 canonical 部分为 620742 字节，SHA256 `a1d73ea1ce5809c87bdc34724c1eb4407d6a5c0ae78fbf16aa3650563aa089dd`。

每次新的独立 job 先按同源码重建原 116 来源，再重建完整五十来源压缩。该入口逐父文件/来源 descriptor 核实际 SHA，不假缓存跨 job 存活，不恢复历史大矩阵。当前完整局部输入 binding 是

`8e701750318d6bed82bd5e202266e025a60da1d23397f2c740badae301ad0bff`。

路径、预算和 `through` 不进入数学 binding；源码、全部固定父数学身份、图索引和列删去规则进入。不同 binding 不能继承完整阶段。

## 5. 已完成的本地准备与后续执行参数

新 v2 的本地准备已经实际完成：9.871052995 秒、峰值 RSS 140588 KiB、exit 0。它完成原五十来源、十七坐标运输、全部十五图伴随矩阵以及 (2.1) 全四条原来源。未展开十行四十六列有 315860 个系数项；含局部器的 ASCII 输入为 5081971 字节，SHA256 `af4b2277ddf5216aee3a2ec38d75119a47f1d90972bb65c4cd0fa55961c2acb8`。本地没有运行 Singular，未得候选或局部单位来源。

同一路径内的首个未展开版本在 5.598 秒因 list/tuple 形状守卫失败，原失败回执保留。v2 仅把四元原索引规范成同一 list 后再严格比较，并使用独立版本、binding 和输出目录。此前展开版 MemoryError 与大小诊断也分别保留。

实际计算 CLI 的固定形式为：

```sh
python 2026-11-16-r150-original-rank-four-unexpanded-local-source127-v2-789f.py \
  --model-source ORIGINAL_MODEL_SOURCE --model-out ORIGINAL_MODEL_OUT \
  --compression-source ORIGINAL_COMPRESSION_SOURCE --compression-out ORIGINAL_COMPRESSION_OUT \
  --out ORIGINAL_RANK4_OUT --chart 14 --singular Singular \
  --through final --seconds 600 --memory-mib 4096
```

本地 `--through prepare --seconds 300 --memory-mib 2048` 已成。独立 Actions 使用原两个重建步骤和第三个上述局部步骤。首次 600 秒；只有真实 exit 75 且多出一个完整候选或验证前缀，才可同 binding 续 1200、1800 秒。单有物化输入、运行中的 GB 或原 MemoryError 不构成续接门。源码中单个展开来源文本上限 64 MiB；完整 phase 有明确物理和逻辑大小限，不移除安全失败机制。

执行清单仅提交源码、参数、run 和输出 hash。真实数学回执在完成 job 日志，数据、来源、SSI 和矩阵不进入 Git、Release 或新 artifact。
