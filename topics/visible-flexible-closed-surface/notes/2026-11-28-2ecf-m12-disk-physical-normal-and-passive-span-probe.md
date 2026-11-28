# M12：原物理 J 行落盘、完整 normal 逐块消费与实际缓存观察核

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。这里登记已真实执行完的实现等价核；M64 整片运行与新场另有记录。

## 真实内存瓶颈与同方程消费者

M64/G12 的精确静态大小是：142784 个未知数、194 个角通道，一份完整 lower Gram band 为 1,329,604,608 bytes；原 Xs/Xt/bb/weight/residual 五数组合计 789,921,792 bytes，此外原入口还产生全域 Jd 和 Jd+r。此为已知数组大小，不冒充实际 RSS，也不反推此前 SIGKILL 的原因。

新 `2ecf-m12-disk-physical-linearization.py` 保留原训练点、原完整三 Gram 行及实际初始场；按原 block=24 和原表达式生成五数组，用私有 NumPy memmap 存储。每次写后读取原值，逐 bytes 相等才登记；每个径向行保存 SHA256，后续每次切片消费都验证。读回数组是新副本，读写后用 MADV_DONTNEED 释放映射驻留页。每个五数组物理块只需 3,244,032 bytes。原源 packet 的完整六 jet 一块为 5,603,328 bytes；没有删二 jet 或删未知数。

完整 Gram 装配与 H2 band 不改。新的物理 normal 按原径向块计算 Jd，立即计算同块 JT(Jd+r)，再以原块顺序累加梯度，不分配两个全域向量。初始梯度 JT r 同样逐块消费。原非线性能量、原 g、实际角基底/查询/时间范围均不改。只有 slope 与 ||Jd||² 改成逐块 dot 后求和；这两个诊断的浮点归并顺序明确不同，不声称字节相同。

## 已执行的非零 C2 全交叉核

使用同一个实际 121 列、2304 行、两个内三重 knot 的非零有限核，并保留独立 dense Cartesian J 与 H2 对照。真实自然 exit 0；实际值如下：

- `all_five_stored_physical_array_bytes_equal`：`{'Xs': True, 'Xt': True, 'bb': True, 'weight': True, 'residual': True}`。
- `statistics_equal`：`True`。
- `raw_Gram_logical_bytes_equal`：`True`。
- `physical_Jd_bytes_equal`：`True`。
- `initial_gradient_bytes_equal`：`True`。
- `physical_normal_bytes_equal`：`True`。
- `physical_normal_relative_error`：`0.0`。
- `scalar_slope_block_minus_global_dot`：`-1.3877787807814457e-17`。
- `scalar_Jd_norm_squared_block_minus_global_dot`：`0.0`。

因此这组实际核的五数组、statistics、完整 raw Gram、Jd、JT r 和 JT(Jd+r) 均与原消费者字节相同；标量 slope 的块求和实际差 −1.3877787807814457e−17，||Jd||² 差 0。对应原位 H2 / dense direction 与 lambda 重装核仍通过。有限核不能替代 M64 的真实返回或实际 RSS。

## 缓存 N 切换与被动径向诊断

新缓存入口每次角节点数改变时，删除自己持有的上一组 source packet，只保留当前 N 的一组。键、每次文件 SHA 核、写回原值逐字核、返新数组和原源身份完全保留。

实际消费已有 h487 原源的 prefix、有限 tail、深 collar 三个原查询点；顺序 N384 → N768 → N384，每次原 source 输出和新缓存 miss/hit 全部逐字相同。将返出的 packet/target 分别原位填入 123/−7 后，命中仍恢复原值。每阶段只保留一个测试文件，实际 eviction 计数依次 0、1、2。实际测试缓存已清除，exit 0，耗时 16.288848238 秒。

被动径向 probe 只在原 observer 的 gram 返回后记录每个观察半径的峰值，不改任何 residual 或重新求源。三真实点的全部原 statistics 与被动观察完全相同。生产入口将记录所有被采样元素数量、峰值 top 24、prefix top 24、tail top 24，以实际保存场的 coefficient bytes SHA 绑定；它们是有限采样，不能叫连续最大值或 h 收敛。诊断轴明确是 uniform correction-basis theta，原源仍在实际 u(theta) 评价。

## 复现与身份

在题目目录且上述 scripts 均在同目录下，可运行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-disk-normal-c2-fixture.py --scripts scripts --out /tmp/m12-disk-normal-fixture.json
```

实际 source 核的参数显式指向同一个已重生 M48/G6 场，其命令入口为 `2ecf-m12-disk-cache-probe-check.py --scripts scripts --data <M12-prefix-data> --grid <M48-grid> --field <M48-field> --result <M48-result> --query-report <h487-query-report> --query-cache <h487-query-cache> --out <fresh-check.json>`。该核没有新非线性场。

新的参数化运行器 `2ecf-m12-refinement-execute.py` 用显式 parent grid/field/result/R226、new grid、query report/cache、source bounds 驱动真实 transfer → LM → R226 → 旧 geometry/R236 → microspan → 真 parent/child ancestor union；不合成父场，不自动换源。它可重用来公开复现后续 M64 与 h 扩展的准确命令，而不把只有 scratch 的执行回执 SHA 当作配方。

- `2ecf-m12-disk-physical-linearization.py` SHA256 `e7764f421a35b2f9d776940a662f86b02c2a9700215af40a1d6860f41c9916cb`。
- `2ecf-m12-h2-disk-normal-lm.py` SHA256 `17da2cffaff34ec0d7eeb2470079f8a4b3320bd1a83dc876226925485571f39a`。
- `2ecf-m12-h2-c2-disk-normal-lm.py` SHA256 `3fef5e3cfaa5a26ca9bf76647021db15adda61c74bdc28f3e6a9324aac55e42b`。
- `2ecf-m12-h2-disk-normal-cached-lm.py` SHA256 `3b16056cf07641e744eba879fe6bc1190434efeab816b45c1cd18a6753e1af30`。
- `2ecf-m12-disk-normal-c2-fixture.py` SHA256 `7b50129895341a3db3d06489e7213df52a40d30a9ae38cf07a767df4a73ba9ad`。
- `2ecf-m12-disk-cache-probe-check.py` SHA256 `45bce93ad477da3dfb69646af2da3c239ff9c485597c30b7e6d946589203b6f1`。
- `2ecf-m12-refinement-execute.py` SHA256 `3a999859e77cdcbf089196ce893b66d84de54d5e73f0fe22a0fd47cc2773b54f`。
- `disk-normal-c2-fixture-final.json` SHA256 `664fcede0f770b4056246389fe424782ffd13de2a84dd1bce8096c7420c214fb`。
- `disk-cache-probe-check.json` SHA256 `c7f188ef69ad4ff31ddfa2f7b4c32a5a7a0038cf8fc71c5a3c066eafce31a073`。
