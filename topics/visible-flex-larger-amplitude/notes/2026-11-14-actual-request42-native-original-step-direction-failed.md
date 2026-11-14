# actual42 native：逐原步1372段系统仍产生不可用方向

2026-11-14。**状态：实际数值失败证据。** 本条只读公开Actions已发布的小报告；共享执行环境失联，尚未取回本次大数组作本地完整字节审计。不能把该未做审计写成已完成，也不为等待它阻塞后续有依据的表示研究。

## 1. 原任务及实际身份

公开 run **43623850723**，source **34abbdf26804307a61fa4d18139c969c1cf9c445**，native job **132535274009**。对应 artifact **14124997721**（visible-mainline-rawcell0band-43623850723-1），64948461 B，GitHub报告 ZIP SHA256：

`4b48e8dc236482b5f75bee6bd663a51934ffe23f5eaa7579e6bfc5a4f8567b55`。

固定入口为 `exact_20261114_rawcell0_step_equilibrated_correction.py`，SHA `30a467e8f08d73fcdcd8a69b2d911e0d9f57489c3397c21c775ed1ec4f6cabe6`；adapter 为 `fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81`。原28与41均经固定public artifact PIN读入；两个fetch步骤成功。本次不重ODE/RK/J，原native solve、非线性trial及endpoint/audit调用为0。

对象为actual41的868个实际单步J，加原28其余504个J，共1372段、1373节点、307552未知数。完整cut/far/H、旧节点sigma及明确的新节点sigma都保留。矩阵身份：

`e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521`。

它不是旧576或578矩阵；不同有限表示的残差不能当同一矩阵上的连续迭代。旧长J残差仍仅为诊断，不作为本次失败门。

## 2. 实际形成、均衡及LU

[完整factorization报告](public-actions-43623850723-1-rawcell0band/rawcell0-step-equilibrated-correction/factorization.json)和[equilibration报告](public-actions-43623850723-1-rawcell0band/rawcell0-step-equilibrated-correction/equilibration.json)保存：

| 项目 | 已保存实际值 |
|---|---:|
| 带宽 | kl112、ku335 |
| LAPACK AB | 560×307552 |
| 单份AB/LU字节 | 1377832960 |
| 形成的原矩阵条目位置 | 69149136 |
| 非有限形成项 | 0 |
| 非零舍为零的形成项 | 0 |
| 不可逆binary64幂二尺度操作 | 0 |
| 最终行/列最大条目范围 | [1,1.9999999999847768] |
| 零行、零列 | 0、0 |
| LAPACK factor info | 0 |
| 分解耗时 | 1.1959580149999738秒 |
| LU复用原AB存储/原pointer | 两者true |
| factor后最大RSS | 1486088 KiB |

三轮是所申请的均衡上限；实际第0轮改变尺度，第1轮已达整数指数固定点。初始rhs单舍入的rounded_rows与underflow_to_zero_rows均为0。这些统计说明所声明的幂二表示操作无所报损失，**不说明求解方向准确**。

unfactored AB的Fortran字节SHA为 `b309d60ca32e732574b800eba592c0df636f8ba94a24d2d5ba6ef795f5cca8b6`；LU SHA为 `380c0003107f1e1ba8812dc70c8353a978bfe4d0389316e5d8111888be10129d`。因子阶段报告中的diagnostic_completed/linear_direction_computed仍是当时的false快照，不把它误读成后续所有步骤未发生。

## 3. 完整原尺度exact读回：初解及一次修正均失败

[iteration00](public-actions-43623850723-1-rawcell0band/rawcell0-step-equilibrated-correction/step-iteration-00.json)和[iteration01](public-actions-43623850723-1-rawcell0band/rawcell0-step-equilibrated-correction/step-iteration-01.json)分别报告全部307552行、1372个stage以及68841584个原乘积位置。读取的是保存binary64数组所定义的精确实数缺陷，显示小数不用于比较。

| 实际方向 | 完整原sigma最大缺陷 | 是否比既有最佳新方向严格改善 |
|---|---:|---|
| 初次LU恢复方向 | 1.220667068366455745400027170381442499984279435694246877103584908e22 | 首个候选，作为当前最佳保存 |
| 第一次exact残差修正后 | 1.256277541531653060615717986282373193150355889148965796672509614e22 | false；保留初方向 |

两次最坏位置相同：**新stage518＝旧stage42、原step0、Pi模式112，完整行116367**。该原步是ordinary分支、x=0、h=0.08333333333333333，不应用原出口port。其原sigma bits是 `4e3c472c8ac1a53c`。本次最坏位置来自真实全行报告，不能与此前old43/44或最大J条目位置混为一谈。

初解该行的精确unscaled dyadic是

`[0x1c1e3faf511eb3d663499513307ce6ab5136766f576a0f873cf1960e39a9e065, -232]`。

第一次修正后是

`[0x39e07c6ab9b7e080829bee95cd127b02a9d22d5f73fc622bcc9efb40127b4fe7, -233]`。

同一新布局中保存基态的原sigma范数仍为0.041773078207401988…，最坏为新120＝旧10最后一步、Pi模式95。初方向的“strictly improved”标记只表示首个可保存候选，并不表示它比基态下降，更不表示native接受。两次完整方向均有限、无NaN/Inf；有限也不等于可用。

两次exact读取分别耗时25.767727732000026秒、25.412883290999957秒。修正rhs从精确原残差按既有幂二行尺度单舍入；iteration00记录307330个rounded rows、112个exact-zero rows、0个underflow-to-zero rows。本条没有本地重算这些数量或残差。

## 4. 已保存结果及读取范围

| 保存物 | SHA256 |
|---|---|
| 初次完整1373×224 delta | `ed6a80275b2ce2b75690b0ce555da68d6d0e5f396fc7888d38c02d734be0f94a` |
| 修正后完整delta | `2b25b25da88086542b1a62459e1e89f8272bdd9f9a76207aee2eaf33cae90120` |
| 保存的初方向checkpoint gzip | `8a817f20f0aac9a61beff25ea8c4dd830e217b9ff82e041f0d11de3a06492ede` |
| 577旧节点restriction gzip | `4b8d28db07cde3cffce11558152cf54a8dcac4f7efa192acb5f6a109c1bf8ad1` |
| 初解全部exact行ledger gzip | `326bde63781504e9475055481236d9720aa79b55f2fb85132927f61b60e7af90` |
| 修正后全部exact行ledger gzip | `69aa6e63bbd0f7feecb33401d2af4e99be1d3b9096d319b8688df465f769103a` |
| 原result.json（1068290 B） | `741fb34eab9eb21042f37659637719012bf74213eac9bce69b963ed301c43065` |
| 发布的result.json.gz（101551 B） | `605604c6495aa85496489d636098640c1eefc43cb9cddf52f5f371391ff117ee` |

完整文件位置、尺寸和发布范围来自[publication.json](public-actions-43623850723-1-rawcell0band/publication.json)。root亲读了iteration00/01、factorization、equilibration、memory预算及publication这些小文本。表中大数组及gzip身份是producer/发布manifest提供的身份；没有通过connector读入二进制，也没有声称独立全字节复核。后续恢复终端时可从原artifact读取，不需要重做科学计算。

## 5. 该失败排除了什么，下一实际变化是什么

局部每步J全部有限、行列最大条目均衡到约1、LU info0，仍不足以使完整恢复方向在原sigma下准确。此处失败属于**新的完整1372段保存系统自身**。不能把它归咎于一个未使用的旧长J门，不能据此宣称实际数学尾部无解，也不机械增加同一误差修正次数。

暂不将这条巨大线性缺陷方向送原十试步。下一变化有现成代数依据：[R269](../results/R269-native-zero-reference-height-slope-gauge.md)及[实际节点G合同](2026-11-14-rawcell0-height-slope-node-gauge-contract.md)给唯一节点anchor、原port、完整coupling及原缺陷恢复式。独立实现将在实际已存块上改变节点坐标，明确记录longdouble形成精度和落盘binary64系数，恢复完整delta后仍对本次原1372矩阵作全行exact读回。

该表示是否改善尚无数值证据；不会把零参考方程替换实际非零J，不重ODE/J、不改变g或原验收。真实后继若有可用方向，仍须原577节点nonlinear evaluate、全部原guards和原sigma严格下降；本题完整闭场、幅度、reach及同g精化仍未完成。
