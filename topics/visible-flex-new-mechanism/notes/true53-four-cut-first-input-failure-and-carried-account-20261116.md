# true53 四cut增广任务的首输入失败与原账延续

日期：2026-11-16。类型：**已发生的运行记录及源码定位**，不构成几何改善、有限问题不可行或课题完成结论。[任务设计](true53-four-cut-exchange-master-design-20261116.md)。

## 1. 原始来源

- 公开run **43825241350**，research **133157415075**，只读report **133157836734**。
- 唯一执行源 **5189a1a78eac6215db75bf5c7d851a8913c6db0f**，workflow `.github/workflows/visible-true53-augmented-master.yml`。
- 原research log **3741178 B**，SHA256 **997e9b9ddaa0ec6ae72f27a94f66895bfe6a1cc51be5850ae204cc4d70566944**。
- research状态failure；stdlib只读report成功读到原7记录，没有研究重算。report成功不改写research失败。
- request **53333 B / a1966ffe1a500f6c9ca448cf1b3fee6da793ac8556fa8bf55da8062c1573d708**；11新源码与240来源绑定均在设计/request。

## 2. 确切失败阶段

原MODEL及正方向来源成功读入；原主矩阵装配保9658行，四条新原行已经追加，首矩阵9662行。此时还没有进入任何有限问题求解。

`AugmentedFirstJets`已完成coarse/fine两份缺失的一阶上下文，但其`_install_known_gradients`在下列metadata断言退出：

```text
ValueError: a source metric gradient would be silently dropped
frame_metric_true53_augmented_first_jets.py, line 553
require(required_from_pools.issubset(self.known_gradients), ...)
```

原5743选定metric梯度、5个MODEL新增梯度和4个已付新cuts的安装已越过各自来源检查。失败断言另外把原ordered pool的metric ID集合要求为已付梯度集合的子集。这个pool/实际选行的语义正在按原生成源码修正；不据此删除一个真实已付行，也不把它写成求解失败。

原记录准确计数：

| 操作 | 已发生 |
|---|---:|
| 一阶输入恢复started / completed | 1 / 0 |
| 两网scalar fields / 变分frame恢复 | 2 / 2 |
| 有限problem / 迭代 / Newton系统 | 0 / 0 / 0 |
| 新方向双网 / 新gradient | 0 / 0 |
| scalar / 实际pair / 普通value | 0 / 0 / 0 |
| U/T重建、源ordinary、旧J或旧方向重算 | 0 |

输入事件17.63444914599995秒嵌套于全任务时间，不能再加一遍。两网已恢复的系数只留下SHA与事件元数据；构造函数抛出后没有交付可持久读取的完整context数组，也没有CACHE记录。这个数据缺口如实保留，不把哈希冒成可复用数组。

## 3. 完整已付账

唯一权威FINAL_CLOCK位于全部COMPLETE输出之后：

- 本次 **36.79963991600005秒**，包括数值imports、两原log读取、配置恢复、矩阵装配、失败上下文、报告和输出。
- 祖先1658.9797906909998秒，加本次后 **1695.779430607秒**。
- 原普通value累计仍 **128**；新普通value **0**。
- 本次未触及600秒上限，也未调用finite/JVP/gradient/scalar/actual。
- 数学stdout在FINAL_CLOCK前3640197 B；峰值RSS562472 KiB。

修复将延续**同一个**600秒科学总额，携带这36.79963991600005秒和失败事件；不能再给一份新的600秒。因为缺失context未导出，修复所需的再次恢复必须明确列为一次修复操作并计费，而不是隐去首失败。所有求解/双网/新行/actual上限保持原任务分配；原J、旧finite及旧方向不重跑。

## 4. 原字面记录身份

以下是原tag后字面JSON加一个LF的身份；不与canonical subtree hash混用。

| tag / 次数 | B | SHA256 |
|---|---:|---|
| PUBLIC_PULL / 1 | 1483 | daaf9ccd096307e712b159a32f6973e69129f4aeeb4656ff0faca8b440cab169 |
| PRIVATE_PULL / 1 | 584 | 123f9655be28577fbca97b1a8ea3f8e4433fb88dcdaf7b5db6c7c8f4da85a2b3 |
| INPUT / 1 | 37000 | 3dc5edee6b96f12a8387d45b0c63aca8902e4710f69196e1978d8fa9358f7ddc |
| INPUT / 2 | 4237 | 733f81767680daaa534f748d46f005dee604f8bc69cfbe3005bf2e613d1781a7 |
| MASTER_INPUT / 1 | 8369 | e729b3492c10acd3dfc3eb0fba19d4325806f7e3b50465764954168ad959796e |
| COMPLETE / 1 | 3590489 | 6cc790b3090a687d5eba44bdabaef662cc1fffd332d9f2bb00b6a91338a9cf4a |
| FINAL_CLOCK / 1 | 6015 | a9648db960caa66e4f2562bbd4af2e32c9cd72cb34cdd69a58625fafafd4ffe9 |

## 5. 每次实际pull后的规则读取

研究前公开实际pull：07:38:49.917193→07:38:50.554071 UTC，before=after5189a1a78eac6215db75bf5c7d851a8913c6db0f，rc0、根/题README空diff。私有07:38:53.574859→07:38:54.570822，before=after96a993b29a0959fae62abd9689212abc1578920d，规则未变且本会话QUEUE唯一进行中。

最新report公开实际pull：**07:39:53.853702→07:39:54.559423 UTC**，源5189a1a7…到已读 **1d56b38c2ae32d4817c976cc75728207541ec2d7**，rc0。根blob21bd547f56590b7f2dd279d0297efb289a9b2783、题blobd0432faff569c8e9af7ed4809847e12880976c11，均空diff。下次实际pull最迟 **08:39:53 UTC**。

私有report **07:39:57.125976→07:39:57.581385 UTC**，before=after **c4039f3d122a2dc5d7739ea2d37d287dc0fff953**；根blob5ba164843b1f5802184178a82d786264404873a3未变、题README不存在，QUEUE本会话唯一进行中。未发表私有正文。

## 6. 当前物理结论

接受点仍53、同g/b0/163族、η细.26601514422985384、κ57.9992694544513，原target.26未达到。失败发生在输入完成前，不提供新的finite、全网或实际下降证据。立即修复确切接线后继续同任务剩余工作，理论子问题照常推进；全部主几何完成门仍未付。
