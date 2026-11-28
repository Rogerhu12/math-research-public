# 固定原源六 jet 的逐字磁盘缓存与真暖场观察 union

日期：2026-11-28。为实际 G12/G14 大点集减少重复原源计算，增加 `2ecf-m12-h2-source-packet-cached.py`。H2 核、C2 adapter、完整 J/Jᵀ、非线性 g、角缓存 v2 均不变。

每个固定 WholePosition 实例使用私有临时目录；记录 data/grid/query-report/query-cache 的 SHA256 和实例实际 source_identity。索引含完整径向 block 的 shape、dtype、bytes 和角节点数 N。首次仍调用原 source，保存原 binary64 的全部六 jet packet 与 target scale；读回逐 bytes 比较。每个命中验证磁盘文件 SHA256 后返回新的 NumPy 数组，防止原 observer 的 in-place `p += W` 污染后续 source。实际场保存后清除这套专用临时目录；不跨几何复用，也不作 source 拟合或新参数选择。

具体实测使用现有 h487 原源的前缀、有限尾、深 collar 三个真实查询点，N384/N768 各一组。与独立原 WholePosition 输出逐字相等；随后把已返回 packet 全填 123、target 全填 -7，再次命中仍逐字等于原 source。实际 2 misses/2 hits，测试目录已删除，耗时 22.943113377s。这只验证缓存与可变数组隔离；没有以测试代替新非线性实场。

- 新入口 SHA256：`f3d2a543f51235633213c046d254327072ab51f45011703dbbc4e53c785a31f6`。
- 实测回执 SHA256：`8d722129c9af64518de34738148f4c2a7580526fccb0840594a71c380090603b`。

另一新消费者 `2ecf-m12-quadrature-observer-union.py` 允许当前 G14 和祖先 G8 同时存在，显式保留各自阶数；它不把 ancestor old_gauss 伪改为新阶。它流式计算每个额外点的真实暖输入 field 与真实更新 field，再分别与当前独立 observer 合并。内存与 block 大小相关，不一次分配数千径向点的大 packet；union 没有积分能量含义。

在已完成 C2 第二场的 16 个真实额外祖先点上，以 block=5 实际跑完四块并 exit 0。新 after 的峰/曲率/支撑与既有原观察器全部完全相等；真 before-union 峰 8.260458152801774e-10，真 after-union 峰 8.057573884765639e-10。前者使用实际暖转移场，未混入零修正 source。

- 真暖 union 消费者 SHA256：`eb8753969c3871705997f15bc153eaa3b0e1c6632b4f675f5492466cfa65487f`。
- 16 点真实回执 SHA256：`e3462fa5cd820805696355e93ffeb79b64eee99bf79ce5a37a4fe2bbdb9300b9`。

G12/G14 新原源查询与下一实际场有独立身份/执行记录，此条不提前宣告该步已完成或已收敛。原 packet 数据只留临时 scratch，不进入 Git。
