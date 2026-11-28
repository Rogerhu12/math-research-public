# 不删任何行的完整polar分块重算：实际r/J/JT/S字节一致与驻留预算

为进入958径点完整G10空间，先对原205×(128+192)的真实非零warm3场核完整实现的内存生命周期。此处仍是完整12789列、65600点、918400行，既未换目标也未缩基。

新 `2ecf-polar-complete-two-grid-streamed.py` 只让原 `CompleteStreamingLinearized` 使用 `cache_point_blocks=False`：每次完整J/JT/原H装配按原12径点block从固定source memmap和同一z重建PointLinearized。13原行与q2面积行、所有XYZ/Fourier方向、两网格固定权重、原physical H2以及完整跨通道协方差一项不删。area packet仍完整保存，source数据保持memmap。

## 实际完整比较

在同一个原205 prepared、同一个保存的warm3完整z上，同时建立旧cached与新streamed消费者。逐个递归比较所有PointLinearized/AreaPacket内部成员，实际1440个嵌套数组的shape/dtype/全部字节一致，并核标量与字典成员；类方法完全相同。另实际付完整随机物理JVP及完整残差cotangent的JT。

| 实际检查 | 结果 |
|---|---|
| 全部918400行residual字节 | 相同 |
| 完整12789方向JVP字节 | 相同 |
| 完整918400 cotangent的JT字节 | 相同 |
| 全部原physical Sobolev因子字节 | 相同 |
| 全目标/全geometry统计 | 相同 |
| 所有实际point数组与标量 | 相同 |
| 新point_blocks缓存列表 | 空 |

没有显式形成918400×12789的J或dense正规矩阵。完整H仍读取同一PointLinearized方法和逐字相同实例数据，完整angular covariance装配过程不变；生产第一步仍须再付实际G10全J/JT/FD和真实正规残差。

## 驻留与边界

仅统计对象可达、按底层array去重的保留nbytes：原cached97,723,528字节，新streamed35,731,528字节，消除61,992,000字节派生point缓存。按相同点布局扩至958径点，消除量预计289,699,200字节。这是可达array预算，不是G10实测RSS，更不是系统峰值保证。完整band仍每份90,239,184字节；其大小随完整空间确定，此次密化未删任何空间方向。

该比较进程自然exit=0，外部2.344893723秒，peak child RSS225504KiB（同时持有旧/新两个消费者及对照向量），内部2.204837206秒。非线性尝试/接受均0。

G10 solver在首个实际dense基线/状态产生前更新其显式模型：recipe.cachePointBlocks=false，并绑定stream helper SHA。原尚未实际使用的cached入口字节另保 `2ecf-polar-c2-g10-solve-prestream.py`。完整factor建立后，direct物理solve的caller另删除其不使用的 `normal_band` 与augmented RHS，保留factor、scale、原S及全部J/JT行；真实正规残差仍由完整J/JT重算。

新log-radius设计支用独立 `2ecf-polar-log-radius-streamed-design-solve.py`，保持已核联合算子字节不动，在caller层应用同一stream生命周期，并释放不再用于生产dense比较的unscaled joint band。87个新g自由度、全部Cartesian-alpha跨块与全部14行保留；其model单列新g设计epoch，不能和原固定g成本混算。

## 身份

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-complete-two-grid-streamed.py` | `013af2fb811c6d74ab58f69d8ade9c52e767d5dc2bef212b9eff900cb6e1d475` |
| `2ecf-polar-complete-stream-memory-audit-v2.py` | `25207c57a0ca73febaf1df69af8bf9a550de3b130aa0b2ae9c5995da93f1aa05` |
| `polar-complete-stream-memory-audit-v2.json` | `1c56ef526a60e407e868fbfb3cfebd463860c7a994533e16329ffd569c5056ef` |
| `polar-complete-stream-memory-audit-v2-exit.json` | `6e1f939f24f55661cd7018a11a423f1f7487a900453b7c1d89302aea80a8dc5e` |
| `2ecf-polar-c2-g10-solve.py` | `baad827f707e889f1be395d7b010dc91c1f39ce21bebdd5042e992038ffce642` |
| `2ecf-polar-c2-g10-solve-prestream.py` | `5800d0a8ffc96a9c0a50715ed079a83ad5baac8c1bb87f6974a22a1db3cf4e20` |
| `2ecf-polar-log-radius-streamed-design-solve.py` | `2a62893d8b04c2c3b22859c8c9ffd94f8ee7d90996d077642c19f091a3c33303` |

原205规模比较不冒958规模实际RSS或新接受。G10完整source恢复、原目标新baseline与真步继续。
