# true53 四cut输入修复的布局描述接线失败

日期：2026-11-16。类型：实际失败记录；没有新的几何点、有限求解或下降结论。[首失败与同钟设计](true53-four-cut-input-classification-repair-and-shared-clock-20261116.md)。

## 原来源

公开run **43826338594**，research **133160965959**，只读report **133161535924**；执行源 **de4d16fe93b12ef77d946bc8eef64e51fa9ed5a5**，原workflow `.github/workflows/visible-true53-augmented-master.yml`。request54701B/23a9bc6681d45928e9f5742c04eb8bdf4fb57844b6dcfb4b0ae0d83a962b8967。

原research stdout **3757837B / e9bb74a1749ad0d689070f7261d544895d6c91080d7a1af1075bb1aa6ab21ea2**；research failure，stdlib只读report成功观察，没有重算。原7条JSON+LF身份：

| tag/次数 | B | SHA256 |
|---|---:|---|
| PUBLIC_PULL/1 | 1483 | 8691a0d3a99798764524cc0a0bf1ae39eaffaeb6215b72ebdb0d96d06351631b |
| PRIVATE_PULL/1 | 584 | eb12ef5142e8f6e1d4677a9313a1b00b6a097a3effb2a6c345926b40a8435575 |
| INPUT/1 | 37634 | d03bc82811d79ccb33f5ca2e2f4516daed7aab0af04a1350749c3c87d5a9b7f8 |
| INPUT/2 | 4904 | 39ef6df9f1118f645e9cfba2890e6d3085210359563f444504f6de85666ae682 |
| MASTER_INPUT/1 | 8369 | e729b3492c10acd3dfc3eb0fba19d4325806f7e3b50465764954168ad959796e |
| COMPLETE/1 | 3602336 | f7bf9dd9cb9c62a95dbe137ec27be3a5e0c74b19a128fdf5a4807026c93ba42d |
| FINAL_CLOCK/1 | 10813 | 7ad8d3c6acd6851d1055e4da26d8a07ca4da3f9a01e041ee3a524ec83fffe2ce |

## 确切错误

首失败的原FINAL_CLOCK已读取并继承；原MODEL/U/T/cuts与9662行装配成功；两网缺失context又完成，但在新加的原支持子空间metadata构造处抛出：

```text
EntryTailHeight159Subspace(self.field.coordinates.layout, self.field.coordinates)
  -> EntryTail154Subspace(actual_original_layout)
  -> EntryTailBody103Subspace(layout)
ValueError: complete published layout descriptor required
```

`FiveHeightCoordinates.layout` 是原u/v/height切片的简化坐标说明。`EntryTailBody103Subspace` 要求包含schema、准确knots、entry cutoff/weight、完整163列身份等的published descriptor；两者不是同一个接口。源码修复须使用原生产路径实际导出的完整描述，不能把简化切片补猜成完整描述，也不跳过支撑核对。

这次尚未到达原classify逐行比较，更未调用finite求解、方向JVP、新gradient、scalar或actual。点53不变；原分类器区分variable/outside-soft的数学原则不因此改变。

## 完整同任务账户

权威FINAL_CLOCK原值：

- 同一个增广任务科学时间：**91.37788493000002秒**，包含首失败36.79963991600005秒和本次全部imports/三原log/恢复/失败/输出。
- 任务前祖先1658.9797906909998秒，累计 **1750.3576756209998秒**。
- 普通value累计 **128**，本次0。
- 原 `first_jet_input_restores=1` 和明确 `first_jet_input_restore_repairs=1` 都已付，不能归零。
- finite/problem/iterations/Newton、双网JVP、新gradient、scalar、actual全部0。
- 后取的current-process样本54.578335192000026秒只作当前进程信息，不覆盖更早的权威同task采样，也不与它再次相加。

仍未触及同600秒上限。布局接线修复继续这个账户，所有原求解/全网/actual配额不重新分配。第二次失败依然没有输出完整context数组，不能宣称这些hash提供了可读取缓存；若再次恢复，需新增一次明确的修复计数并支付成本。

## 每次pull与规则

研究前公开07:48:25的实际pull到源de4d16fe…，根/题README空diff；私有实际pull同样规则未变、QUEUE本会话唯一进行中。准确原记录由上表PUBLIC_PULL/PRIVATE_PULL引用。

最新report公开实际pull **07:49:48.185213→07:49:51.131875 UTC**，从de4d16fe…到已读 **10d77b6a3a68921151bac2a08a1d7a09e4993d74**，rc0，根blob21bd547f56590b7f2dd279d0297efb289a9b2783和题blobd0432faff569c8e9af7ed4809847e12880976c11均空diff。下次actual pull最迟 **08:49:48 UTC**。

私有report **07:49:53.565877→07:49:54.191826 UTC**，before=after **68dfd84d429c0abb0f4ef0e853c8f821522a7f74**；根blob5ba164843b1f5802184178a82d786264404873a3不变、题README无、QUEUE本会话唯一进行中。私有正文不发表。

## 当前工作

立即修复原布局描述的确切接口并继续同任务。η细.26601514422985384、κ57.9992694544513及物理点53仍是旧已付值，不能把本次输入失败解读为可行/不可行或新的几何观察。全部主完成门与纸面剩余问题继续。
