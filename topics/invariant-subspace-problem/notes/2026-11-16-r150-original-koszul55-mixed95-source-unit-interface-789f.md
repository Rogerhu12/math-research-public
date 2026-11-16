# 原五十五条 Koszul 来源与混合九十五阶单位：冻结计算接口

作者：Astra-ISP-789f / normal_annihilator，与 /root。  
AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

## 1. 本次有限结论

原特征零存在性证明已经单独冻结于
[原五十五条 Koszul 来源与二百一十列呈示](../results/R150-appendix-original-koszul-fiftyfive-quotient-and-characteristic-zero-twohundredten-presentation.md)。
本次从已经完整验证的高次常数源矩阵中，选择四十条原乘积来源，记录同原九十五阶混合子式，并验证全部一百五十五条来源的完整坐标。

本次不构造参数多项式大矩阵，不重算原有理六十阶解，不把有限域坐标视为特征零坐标。原 Bell 单位理想是否成立仍然开放。

状态为静态冻结；共享执行器不可用，尚无本地 AST 或新算术结果。下列 rank 和单位要求是程序硬门，不能预填为实际结果。

## 2. 原字典与既付父证书

使用原固定数域 $E$、合法系数 place $(127,d-100)$ 及普通单项式字典。令 $q_0,\ldots,q_{10}$ 为原十一条二次最高项，并令

$$
D:E^{165}\longrightarrow E^{70},\qquad
T:E^{100}\longrightarrow E^{165}
$$

分别为全部原四次乘法映射和全部 $u_\ell z_s$ 来源。二十条原三次核按既付低 commutator 索引排列。父证书已付

$$
\operatorname{rank}D=70,\qquad DT=0,\qquad
\operatorname{rank}T=95,\qquad \operatorname{im}T=\ker D.
$$

父实际 run 为 43911869940、job 为 133455626806，对应 step：

~~~text
original-low20-original-quartic-syzygy95-unit60
~~~

父 raw 为 8429 B，SHA256：

~~~text
7b23309fe6d5d80c52624f3f9f66b4a9ed311d62a23952cbce3a5e7e5e964f0b
~~~

父 binding：

~~~text
9f0ee10f7e4cece784d8140d063f94c210105e7dded9f811710d6ec6f2825fa1
~~~

完整读取并逐一核物理与逻辑 SHA：

| 相位 | 压缩字节数 | 压缩 SHA256 | 逻辑字节数 | 逻辑 SHA256 |
|---|---:|---|---:|---|
| whole-original-quartic95-input | 16730 | a2d91336495f29ff2a15958ab26cf2cefcb782eb2e7acac2c88d90fb91a2de07 | 95934 | bf86bf186cd64d3ed78e0bf66b794bca62aa72e71abd3de3335e905c7cea0589 |
| complete-original-quartic95-unit | 20816 | 71d679b394ab9c58f542c576690397d8f1cbcba627d74daffd72f9bbb2e3302e | 63121 | b711688351ce47161d8e898f1322a2e4e0c355bf8d7033d7a6bb2884a95343eb |

父 manifest 的预期字节为 901 B，SHA256：

~~~text
11ad47693c39437e3f7d4711a84817e87d96392886802471116da34e1f79dacc
~~~

该 manifest pin 由父实际完整描述符、source、binding 及冻结 canonical writer 重建。本次必须对新重建的物理 manifest 逐字核准；不把这一 provenance 误称为先前另读过旧物理 manifest。

程序重建普通二、三、四次字典，核原十一来源、低二十来源及一百乘积标签；另从同一 $q$ 重建 $D$ 的 11550 坐标，从同一原二十列重建 $T$ 的 16500 坐标。父全部完成门仍须为真。只读父相位不等于重做其 35 阶或 95 阶消元。

## 3. 五十五条原 Koszul 来源

对 $0\le a<b<11$，构造

$$
k_{ab}=q_a e_b-q_b e_a.
$$

原 165 行按 $(g,m)$ 排列，$g=0,\ldots,10$，$m$ 为十五个普通二次单项式。第 $(a,b)$ 列在分量 $b$ 写入 $q_a$，在分量 $a$ 写入 $-q_b$；对角单项式不另乘 $2$。

实际硬门：

$$
\operatorname{rank}(q_0,\ldots,q_{10})=11,\qquad
\operatorname{rank}K=55,\qquad DK=0.
$$

末门覆盖 $70\cdot55=3850$ 个原坐标。特征零独立性则逐来源分量使用原十一条 $q$ 的线性独立性，不凭列数。

## 4. 同一原九十五行上的四十列选择

令 $I_{95}$ 为父实际原单位的九十五行。父原 95 列构成 $\ker D$ 的基，且其 $I_{95}$ 限制可逆，所以行限制在 $\ker D$ 上为同构，因而在 $K$ 的五十五维子空间上单射。

构造

$$
[\,K_{I_{95}},T_{I_{95}}\,]\in\mathbb F_{127}^{95\times155}.
$$

主元严格依原顺序：先全部五十五条 Koszul 列，再一百条原 $T$ 列。硬门要求总秩 95，且前五十五个主元准确为 $0,\ldots,54$；其余主元给四十个原列号 $J_{40}$。

令

$$
M=[\,K,T_{J_{40}}\,],\qquad M_I=M_{I_{95}}.
$$

必须实际核 $\det M_I\ne0$。保存四十个原列号、$(\ell,s)$ 标签、$(\ell,\text{原低来源ID})$ 标签及九十五行原字典。新选择不自动等同于此前有限域 200 呈示中的四十条换源列。

## 5. 全部原坐标核验

实际计算

$$
C=M_I^{-1}[\,K_I,T_I\,].
$$

| 硬门 | 完整坐标数 |
|---|---:|
| 两侧九十五阶单位逆 | 18050 |
| $MC=[K,T]$，全部原 165 行及全部 155 列 | 25575 |
| 全部 95 个选中混合列坐标为单位矩阵 | 9025 |
| 四十个新原乘积列的规范坐标 | 3800 |

最后一门要求顶部五十五行零、底部四十行单位。任何门失败都只记录真实失败，不登记 complete phase。

成功给同一原 $E$ 矩阵的非零子式。原 $E$ 坐标由该原子式伴随矩阵除以行列式定义；有限域坐标只认证原子式，不能逐系数搬成 $E$ 坐标。

## 6. 原来源与二轮呈示的衔接

引用已付 exact-low20 与 canonical-source 定理。任一原 $N_iC_s$ 的来源二次最高项用本次四十个 $u_\ell z_r$ 和五十五个 $k_{ab}$ 表示。先减对应四十条真实 $N_\ell C_r$ 来源，再减真正的

$$
G_a e_b-G_b e_a.
$$

这些完整 $G$-Koszul 来源的原像严格为零；不能只减最高项 $q_a e_b-q_b e_a$ 并忽略较低项。

余来源 $u$ 次数至多一且像仍为原十正常形，由 canonical-source 唯一性落回二十条原低来源。因此普通 $B$ 模中

$$
\langle C_{20},N_iC_{20}:0\le i<5\rangle_B
=
\langle C_{20},(N_iC_s)_{(i,s)\in J_{40}}\rangle_B.
$$

结合六条 mean 与已付至多两轮稳定性，得到至多 200 梯度列，加十条 Bell 列后至多 210 列完整参数呈示。本次把纯存在定理落到实际原四十个索引；不材料化完整参数列，不声称第一轮稳定或 Bell 理想已空。

## 7. 冻结文件

| 文件 | Git blob | 字节数 | SHA256 |
|---|---|---:|---|
| source | 65c4d8a2bcf950c4911044d216faefad0877733b | 16461 | fc1dfea5219a773af1140c3c9e8ba52bcb6acfd36ae67bd325c9317e416d0ab5 |
| inputs | 32c7d3200c10490e28d8ab7debdd1a47ef53fd35 | 9628 | 0a09cfa412b1b419da179ee7086806830a5a985dbfd4aea2939c89b9c2a8ccf5 |

~~~text
notes/2026-11-16-r150-original-koszul55-mixed95-source-unit127-789f.py
notes/2026-11-16-r150-original-koszul55-mixed95-source-unit-inputs-789f.json
~~~

完整父 source、helpers 与重建顺序均在 inputs 逐 SHA 固定。

## 8. CLI、预算与新作业

固定 Python 3.12.14、python-flint 0.9.0；不需要 Singular。

~~~text
python 2026-11-16-r150-original-koszul55-mixed95-source-unit127-789f.py \
  --parent-source {scripts}/2026-11-16-r150-original-quartic-syzygy95-small-field-gate127-789f.py \
  --parent-out {work}/original-quartic-syzygy95-small-gate127 \
  --out {work}/original-koszul55-mixed95-unit127 \
  --seconds 60 \
  --memory-mib 512
~~~

旧作业已关闭。新作业同一 job 顺序真实重建：

1. 原 116 种子 field model：180 秒 / 2048 MiB，outer 240 秒。
2. 原 high95 小门：60 秒 / 512 MiB，outer 120 秒。
3. 本混合95小门：60 秒 / 512 MiB，outer 120 秒。

可沿用原 observer 的十秒心跳。父重建不调用 exact 六逆、旧有理六十阶或 two-four 解。新 consumer 只接新实际全 SHA 相同的父数据。

此 consumer 使用独立新 out，不提供算术续接。预算或错误只保真实完成描述符；没有完整 phase 时不能说成续算或数学否定。

## 9. 相位、回执与边界

成功只登记：

~~~text
complete-original-koszul55-mixed95-unit.json.gz
original-koszul55-mixed95-manifest.json
original-koszul55-mixed95-receipt.json
~~~

完整相位含原标签、场上完整坐标及全部门，压缩/逻辑双 SHA 写 manifest。先原子写相位，再原子登记 manifest，最后计入 completePhases。

异常类型与 message 同时写 parameters.error；最终保真实耗时、峰值 RSS、退出码和完整相位。raw、矩阵、参数数组只留临时目录或完成 job 日志。Git 只保存源码、参数、接口、证明、实际执行身份与输出 SHA。

本接口没有新执行成功声明；actual 后须逐字段读取完整日志并单独冻结正式结论。
