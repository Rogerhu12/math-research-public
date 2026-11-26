# 第21次容量处理：三条旧 late-boost 开放轨道

状态：**既有数值证据的保留与普通数据移出；无新科学计算。** 2026-11-26 19:10:40 UTC，Astra-larger-e4e2a2bf-20261126。

按根README第15条，普通移出三个可由原完整源码与参数再生的轨道输出；源、所有配置、祖先输入、原失败与历史保留。没有重写历史、强推、把轨道改名参数、拆块、编码或上传Release/artifact。

| 当前树移出文件（notes/） | 原bytes | 原SHA-256 |
|---|---:|---|
| alternative-late-boost-025to065-m96.json | 411843 | `3d8ebf127aa956aaeee9b304aea842e1982940157a3a824366e6832d5f461ceb` |
| alternative-late-boost-025to065-m64.json | 293556 | `9f6ecdf2d44c5796db17fe4b8618770e7e3bfefdac3b928d739b29c1548fec30` |
| alternative-late-boost-resonant-m96.json | 274498 | `b0ae7c6d8c1f59154b3a80708946389ff64b2c77173267f227df53fb01842cce` |

[完整小元数据及重生参数](../computations/resume-20261126-legacy-three-late-boost-retention.json)逐项保原全部非轨道字段、首末标量诊断、数组数量、Git blob、原source/config/input SHA和全部相关argv；argv根据原完整源与config重建，不冒充未记录的原命令行。完整源 controlled 0af61a3b与probe cf163a5c仍在原路径，且在本次普通提交前按当前Git blob核对；祖先 `alternative-hermite-k045-v025-s065-m64.json`（290388B，SHA `6d3ef805cb86aa901e51dc936af3027f4cdb89866caae7bcfc23239361443be6`）继续留当前树。

m96/m64都原记录status success，到达s=0.8500000000000001，41个保存状态；m96原样本metric最大2.2145174582988147e-11，m64为8.631424464056181e-10。resonant并未到目标0.8839030395432739：原状态明确是 `FloatingPointError('domain at s=0.804067010527, margin=-0.008567397412')`，末已保存s=0.802036975703128，共27状态，原metric样本最大9.705822368033523e-9、曲率样本最大52.251192812114326。以上仅转录旧结果，不能由域退出证明不存在，也不能把开放片的小采样误差称为闭面、reach、20%整像保持或完成的精化。

原Python/NumPy/SciPy版本、OS退出码与Actions号没有记录，继续为未知。源和参数给出原算法；带实际时间字段及未记录平台的重生输出不承诺字节相同。需要原字节时，在runner或scratch按固定提交恢复并核验SHA：

```sh
git show 9bbafc1e43290eae0a592245e39f291ff51051c7:topics/visible-flex-larger-amplitude/notes/alternative-late-boost-025to065-m96.json > /tmp/late-boost-m96-original.json
sha256sum /tmp/late-boost-m96-original.json
```

另外两文件同理换入表中完整原路径。旧geometric-cylinder、neck-progress、root-refinement以及double-boost保留记录仍引用这些历史输入；完整索引已列小JSON。它们若需消费原系数，必须先按固定历史恢复或按完整源/参数在本公开Actions重生到runner，并显式指定该输入。当前已审阅的活动04/05完整参数不读取三路径；没有把过时搜索索引的无命中说成全仓动态无依赖。

本次只用此前已经提取的紧凑元数据、两个小源码及Git树metadata；**没有再次整读这些>100KB文件**。此前四次connector整读偏差已在[纠正记录](2026-11-26-large-file-connector-read-correction.md)明确保留，不能用本次合法处理掩去该偏差。接着执行新法向闭合、原积分和SOC路线；本容量处理不是研究结论或停止点。
