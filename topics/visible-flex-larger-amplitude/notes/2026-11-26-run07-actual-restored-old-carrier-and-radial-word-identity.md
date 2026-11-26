# run07 第3步：整个旧载体恢复成功，径向材料地址已逐字核同

## 实际返回及完整来源

2026-11-26公开 Actions run `45909290354/1` 第3步 `restore-actual-run05-complete-carrier-2397-leaves-20261126-07` 已完成，returncode=0。23:50:32 UTC索引记录该返回；不是从时间、未见错误或同一命令推测成功。root实际读取小卷第三个完整返回对象，未读取runner大数组。

实际source commit为 `40f73dbacdd18bab36cda4cd6b421a1d1b917694`，完整执行源仍为 `ef67425800ae9de626a7f8f48fd89deb125fbf0e4d6af72cf79741d1e254664e`。全部原参数见[完整单步请求](../computations/restore-actual-run05-carrier-run07-ready.json)，准入普通提交为 `f014d5cd94409d6a9af7f9f73e53411744e2d18d`；该队列实际SHA为 `200c9c5cd29d42c389a1cd39cbdc232780aada0ba0b8feebd798b8d0ab61e8d2`。

当次完整紧凑卷 `2026-11-26-public-actions-45909290354-1-part-001.md` 为31775B，SHA256 `8630c9e440a6eaf648e3fcec35eb86e67b03a7d4ddab4db07ca2ba1ef2888749`。卷以后可追加实际返回，本文身份指本次实际读到的版本。源码执行时绑定的此前22619B/94ba版本仍在实际source commit中；旧05小卷53029B/6eca版本也仍按原SHA读取。不能用后来追加后的卷冒充原先字节。

| runner实际输出 | 字节 | 完整SHA256 |
|---|---:|---|
| `run05-actual-observation-carrier-restored/report.json` | 19691 | `926db461a4efce0fa40ab539b9df28143f8664cca25ec96e95ebe1d7aa83dcdf` |
| `run05-actual-observation-carrier-restored/run05-observations-restored.npz` | 227202 | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` |
| `run05-actual-observation-carrier-restored/material-envelope-carrier-binding.json` | 1537 | `aaa65a5ecac807e97cf771a08dd57d2ac26b48adf6acc9592025c0c706581c8e` |

三个对象完整保留在本run runner临时目录，未复制raw到Git/Release/artifact。必要原始文件、完整数学参数与再生方法保[完整输入重建说明](2026-11-26-actual-run05-carrier-deterministic-input-reconstruction.md)，不依赖一个旧SHA猜造数据。

## 真实确定性再生检验

原实际live叶数2397，新实际live叶数2397，总已评价叶4793。全部原准确uncertainty字串真正相等；原accuracy状态仍false。完整原profile identity为 `e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350`，完整scalar数学参数为 `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`，恢复的全部准确923节点定义canonical SHA为 `ba5a3188e048f69b6602b4b784640c70932fbc1f53cfbf13b0857ba25e6b4b02`。

已刊ef674依次硬核原profile、原radius字/绝对误差、全部准确uncertainty和原节点公式，再生成原14个plan成员及全部a/ae/te；最终整个候选NPZ SHA和227202B均与旧05原对象一致。返回 `full_original_carrier_sha_match=true`，不存在放松到局部数组、近似容差或同尺寸的接受分支。因此本次确实取回了原整个observation carrier，不只得到了结构相似的计划。

当前07的真实carrier依然是 `7c8b3cbffd66a360b01341db8e1179f211da3c264de85812020a5e48ad5637c3`。源没有改标它、当前scalar文件或当前node文件。旧reference NPZ、旧H/whole-law缓存、旧seed19结果也没有被重建或冒认。

实际子进程wall为394.008481672秒，内部输入再生为389.465780085秒。真实报告F=0、J=0、root=0；这一步只恢复必要输入，未重跑优化方向、seed19、场或几何。

## 全部径向地址的实际逐字比较

在完整旧dc5文件身份通过后，程序实际重新打开旧候选NPZ和当前7c8 NPZ，比较完整plan成员的dtype、shape与字节；不是由两份摘要形似推断数组相等。

| 数组 | 原05恢复文件与当前07共同完整数组SHA256 | 实际逐字相同 |
|---|---|---|
| `observation_cells` | `3ecef008e7512aa30ef85790e6a0e9bf0414adfed8698249be4fd5df7b19f31b` | true |
| `observation_u` | `ab35773d7256855fcca1355c933ebb2affd8f2e6a1544ea3c6cabf5950152c69` | true |
| `observation_gauss_unit_nodes` | `0d6887a8bbd6ba21f90a86b350730858552df0d2ff00d087a40de05f705e95e6` | true |

实际六个Gauss unit字如下。这六项是后继完整材料地址定义所需的真实有限输入，不是派生误差证书或逐点raw数组：

- `0x1.149ad8bfaff18p-5`
- `0x1.5aebed3546d44p-3`
- `0x1.85d3b4bf2628fp-2`
- `0x1.3d1625a06ceb9p-1`
- `0x1.a94504b2ae4afp-1`
- `0x1.eeb652740500ep-1`

每一项也与当前07对应字相同。完整carrier仍含全部7377个正观测，未因径向重复地址在集合中合并而删除任何原度量行或正权。

## 对完整包络的作用和剩余边界

这次真实返回支付了[完整地点闭包与独立政策](2026-11-26-seed19-permanent-location-source-closure-and-envelope-policy.md)第7节所缺的**旧/新径向地址字节身份**。后继consumer可以从binding指向的两个实际NPZ再次重hash并读取cells/u；不能仅相信producer自报true。旧四分角字还要保原N2048、原精确材料角公式和来源闭包，全部显式旧P0及protected标签仍按完整原payload保留。

即使全E地址责任闭合，新候选的两主曲率、body/半径、双符号witness-distance、帽/H、实际度量与同Phi门仍须逐候选真实消费。未知seed19实际protected升级次序没有被恢复；root选定独立新工作集政策，不能将它说成原e783逐行/优先次序等价。已知完整前缀保留，全E逻辑永久保存，真实typed违反记忆不得丢弃。

本次不是旧几何证书迁移，不证明新场可行，也不证明连续reach/嵌入/全域度量或固定g精化。它消除了一个真实输入身份缺口，使完整新消费者能继续运行；课题未完成，06/07继续。

## 两项可选summary字段的诚实状态

controller列出两条 `summary_errors`，均为读取成功报告中不存在的 `failure.type` / `failure.message`。源在成功分支不写failure对象；本步真实exit0、complete=true、全部输出存在，原整SHA门槛已通过。这里不把可选失败字段缺失解释成科学失败，也不隐去controller的实际记录。若后续失败，源另有完整failure报告路径；本次没有发生该分支。
