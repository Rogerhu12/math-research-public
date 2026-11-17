# 固定pulse全818胞Gram覆盖的实际运行入口

**实际已启动，尚未完成。** 保持26e53e8完整共同五次场、构造q4096、证明角网格16384、标量积分4096段；不重求解、不改变g、不自动加密。按准确节点/标量knot预先生成全部计划：旧quintic481胞、解析段17胞、pulse-first319胞、末胞按准确1−5/2^60分两片，合计819次有界调用。每片调用已冻结R641补充引擎d0661f，保完整预算；界未过和exception分别记录，未访后缀不省。

[批处理源](2026-11-17-parallel-model-pulse-gram-fixed-full-batch.py) SHA256 `7bcbb9b2d0e830da172e57026023af2487c76d31f1dfc6ad586123f2ee3fc4a1`，9370B。只缓存只读输入、已验依赖模块及区间FFT角因子。胞381/514已与此前cold报告比较全部非time字段；每个float按64位字节比较，均完全相同，没有改变算术顺序或证明预算。两cached报告SHA分别`c52c1d1949544d1eec982c24400017b351f1476fd98e032be47f4bb1a72016e8`、`a992c06c7deaff237494755f60aa1ca7cb9a0220335a93862043ecb096c994e7`；cold报告见R641补充。

固定完整计划SHA `9b42d8cc8460318f83335f623ae762ad520678ac65f4a664137571c74c00b11d`；cache-validation SHA `f24cffc2feb4249e21ca9fa2bd4ccd513267dfcac92ed28edb0ee6e7cffc68fd`。这两份与每片JSON均留scratch，不入库。

本次发布时已实际完成48/819，界失败0、异常0；当前最大上界4.678925685532623e−8（cell32），纯计算391.93秒。此为前48片状态，不是全域证书。动态progress每8片更新；最终全部结果及SHA另刊。当前运行目录为仓库外`parallel-pulse-gram-full-fixed-20261117`，model负责终态回读。

T为本题目录，WORK为仓库外工作目录，输出目录必须新建或为空：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python "$T/notes/2026-11-17-parallel-model-pulse-gram-fixed-full-batch.py" --input "$WORK/parallel-pulse-a5-complete-base.json.gz" --engine "$T/notes/2026-11-17-parallel-model-pulse-gram-representative-cells.py" --interval-source "$T/scripts/parallel_20261117_arclength_interval_positive.py" --scalar-oracle "$T/notes/2026-11-17-parallel-inward-integral-enclosure.py" --outdir "$WORK/parallel-pulse-gram-full-fixed-new"
```

未给`--validation-reports`时，入口会按同冻结源生成两份cold参考后核对缓存；原运行用已存两报告目录。若某片失败，不修改source、场、q_N或角数来覆盖其记录。819全部遍历仍不等于闭面、reach或固定度量求解精化。
