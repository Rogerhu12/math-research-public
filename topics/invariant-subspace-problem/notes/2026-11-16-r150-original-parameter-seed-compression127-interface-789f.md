# 完整原 116 参数种子的带来源压缩入口

**作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted: GPT-6 Astra Pro。日期：2026-11-16。**

本入口只压缩已实际完成的 $116$ 个 $\mathbf F_{127}[y,w]^{10}$ 原种子的生成列表。每个被删除列必须给出保留原列的参数多项式组合，逐全部十个坐标核验，并再乘回十八个原生成元。它不求稳定闭包，不特化十二个参数，也不把有限域的所选支撑提升为特征零完整性。

## 1. 最终冻结项

| 项目 | blob | bytes | SHA-256 |
|---|---|---:|---|
| driver | 025821b76d7b9a982a52d0ecc205065097ecd66b | 20434 | b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9 |
| native | fb7f7eb7ace4230080eb470594e6aca601ac5f24 | 9682 | c5c36af57f8d75d2aac7d42b4048be2c8f382fdbe9ed4a0ebefdf85f0c93bd9f |
| paid header | 796c0d4c790b3f2294bc203f057e78c0fb16d4ed | 4691 | 03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3 |
| inputs | 6e4b48832dfaa100c9596e2d70a266495d9a06ff | 3090 | 2ae06a8127aedaa09261c3e1bc444ea8a2432d638202bd1c432a677e06317e26 |

路径依次为：

~~~
notes/2026-11-16-r150-original-parameter-seed-compression127-789f.py
notes/2026-11-16-r150-original-parameter-seed-compression-rank127-789f.cpp
notes/2026-11-15-r150-original-f127-bitplane-789f.hpp
notes/2026-11-16-r150-original-parameter-seed-compression127-inputs-789f.json
~~~

父模型主源为 `2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py`，23879 B / SHA **4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4**。

父数学 manifest 必须完整等于 30466 B / **9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2**，binding 必须为 **7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4**。所有读入的种子逐压缩、逻辑 SHA 及原标签再次核验。

已付旧父回执 30925 B / **3615210e27511904dbadc086d8e00438442f33d2538b7f33fa57fa5de9fb18a3** 仅作为历史证据引用。若父模型在新环境诚实重做，允许其用时不同的新 completed 回执，但必须是同一源码、binding 和上述逐字节相同的数学 manifest。新实际父回执 SHA 另行记录，不回填旧时间或假造旧回执。

## 2. 字面分次与完整输出

令 $B=\mathbf F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5]$，权为 $\operatorname{wt}y=1$、$\operatorname{wt}w=2$。十个模块基的权为
$$
(0,2,2,2,2,2,4,4,4,4).
$$
因此模块权 $d$ 的全部输出数为
$$
\dim B_d+5\dim B_{d-2}+4\dim B_{d-4}.
$$
实际字典逐单项式生成并检查唯一性。所用完整参数维数为
$$
\dim B_1=6,\quad \dim B_2=27,\quad \dim B_3=92,\quad
\dim B_4=273,\quad \dim B_6=1715.
$$

第一块完整输出为 $3188$ 行。已有来源是六条 mean 的全部 $6$ 个权一次参数倍数，共 $36$ 列；新增目标是所有交换子的五个 $u$ 轴，共 $50$ 个字面原列。矩阵因此为 $3188\times86$。

第二块完整输出为 $17674$ 行。已有来源是六条 mean 的全部 $92$ 个权三次倍数，以及第一块实际保留的新权六列的全部 $27$ 个权二次倍数。新增目标是所有交换子的四个二次轴，共 $40$ 个字面原列。若第一块保留 $r_6$ 列，第二块恰有
$$
552+27r_6+40
$$
列。其大小不预填秩，也不删任何原目标。

十个 $e_0$ 交换子列须在父数组中实际全零；十个 Bell 列全部保留。没有使用均值点采样或只保部分单项式。

## 3. 常数消元与参数来源

输入按上述字典把每个完整多项式列展开成全部输出坐标，再转置为 native 的输入行。native 在每行右边附原来源单位向量；每次归一、消元同时作用于全部输出和该来源向量。

对一个被删目标 $v_j$，native 必须返回
$$
v_j+\sum_{i<j}q_i v_i=0
$$
且自身系数严格为 $1$，未来来源系数严格为零。只允许引用实际保留的原输入行。

driver 将标量 $q_i$ 与该原输入的参数单项式重新组合为 $c_{ij}(y,w)$。它不以 native 的零残量代替最后验证，而是独立检查
$$
v_j=\sum_i c_{ij}v_i
$$
的全部十个完整多项式坐标。随后用父模型已验证的十八来源 $\sigma(v_i)$ 再核
$$
m v_j=A\left(\sum_i c_{ij}\sigma(v_i)\right).
$$
组合来源可能与父文件中的旧 $\sigma(v_j)$ 相差原 syzygy；不要求二者字面相同，也不以旧来源元数据冒充新乘回。

最后全部 $116$ 原种子均必须在保留列表上有完整展开，共 $1160$ 个模块坐标再次核验。反向包含来自保留列表确为原列表的子集。因此最终结论严格是**同一有限域参数子模**。其最小 $N_i$-稳定闭包也随之相同，但该闭包尚未实际计算。

## 4. 算术与断点门

native 复用已付七位面 $\mathbf F_{127}$ 头文件，并在每次运行先执行：

- 全域、符号、旋转、偏移和 padding 的独立标量算术比对；
- 一个普通标量高斯消元独立小矩阵；
- 该小矩阵的全部真实来源和归一行乘回，共 $25$ 个坐标。

完整输入协议为 R15PCI01，来源状态为 R15PCS01，小结果为 R15PCR01。状态保留全部已经处理的完整输入行、实际原主元标签、归一行及原来源 recipe。只在完整一行结束后检查预算，原子写出状态与结果。

driver 在下一次使用状态前核完整 SHA、同一语义 binding、输入字典和全部输入文件 SHA。未登记的 orphan 状态不能自动采用。native 完成但 Python 关系乘回尚未完成时，可以复用已登记的完整 native 结果，继续最后的原多项式门；不能把这一阶段提前称为压缩成功。

## 5. 实际命令

~~~
python 2026-11-16-r150-original-parameter-seed-compression127-789f.py \
  --model-source {scripts}/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py \
  --model-out {work}/original-ten-parameter-module127-v2 \
  --native-source {scripts}/2026-11-16-r150-original-parameter-seed-compression-rank127-789f.cpp \
  --header {scripts}/2026-11-15-r150-original-f127-bitplane-789f.hpp \
  --out {work}/original-parameter-seed-compression127 \
  --seconds 180 \
  --memory-mib 768 \
  --through final
~~~

源码先通过 Python AST 和 g++ syntax-only；这不计数学执行。单次预算 $180$ 秒 / $768$ MiB，预算中断只接受实际已登记的完整阶段。若仍需续算，同源码、同 binding、同 out，单次最多 $900$ 秒；内存或原身份失败不当作普通预算。

所有数组、矩阵、native 状态和原数学回执仅在临时环境保存。源码、参数、接口、运行身份与完整输出 SHA 可入仓。后续 Singular 候选若不产生 $e_0$ 来源，仍只能报告该实际阶段，不能宣称完整临界理想非单位；特征零正证另需原 $E$ 来源全乘回。

## 6. 实际完成补记

本冻结入口已完成实际独立执行：47.609104284012574秒/exit0，driver峰90836 KiB、child峰162364 KiB。权6全3188×86 rank56，保20删30；权8全17674×1132 rank1106，保14删26。最终50个原列与全部116原列同B子模，所有1160模块坐标和删除列原十八乘积通过。root另用纯Python字典实际16.267秒/51,834,662产品独核全部1160与完整SHA。准确证明、原raw和范围见[50原列同模定理](../results/R150-appendix-original-parameter-seeds-fifty-and-complete-field-module-equivalence.md)；当前未计算Ni稳定闭包或得到单位。
