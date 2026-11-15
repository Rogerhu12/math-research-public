# 原自然 u-Schur 的小回执续接包装

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15。

原八阶任务已完成，其主回执 $98033$ B 接近单文件小文本上限。后继增加临时文件清单时，重复的 $4318$ 个单位输出下标会使回执越限。本包装只压缩序列化表示，保原数学文件及检查点绑定不变。

## 精确不变的数学来源

旧 runner 为

~~~
2026-11-15-r150-selected-natural-u-schur-source-jets-runner-789f.py
~~~

字节数 $21664$，SHA256：

~~~
80f6815133250cf559f81afb557f138952f7268ce2d2b43e2c15bfb822775e67
~~~

旧数学语义绑定保持

~~~
1fdb07aa85a565c45d7adfe04721a29cdbe6911cc0cb50ca45044c51f88ccc01
~~~

包装核验上述实际源码后，以该真实路径导入旧 module。它不改变旧 module 的 __file__、sources、native 源、输入身份、来源递推、小 Smith 计算、编译绑定或原完成层。

唯一替换是旧 module 的 jsave：当写主 pipeline 回执时，先取字典浅副本，再取 nativeStatistics 的浅副本，删除副本中的重复字段 unitOriginalOutputIndices。原 nativeStatistics 内存对象完整不动；原 native 独立回执及全部来源数组也不修改。parameters 中原已保的小 nativeSummary 及输入 profile 哈希仍在。

新包装自身 SHA 与这项展示层处理独立记入小回执，不混入旧数学输入绑定。因此此前八阶的来源/Schur/原残量数组按原完整 SHA 继续使用，编译结果也可直接复用。

## 实际命令

在上一完整命令前增加包装和旧 runner 路径，其余原输入保持，最高阶改为十六：

~~~
python -B {scripts}/2026-11-15-r150-selected-natural-u-schur-compact-continuation-789f.py
  --runner {scripts}/2026-11-15-r150-selected-natural-u-schur-source-jets-runner-789f.py
  --
  [上一条命令的全部原输入参数，--out 保持原目录]
  --maximum-degree 16
  --seconds 60
  --memory-mib 512
  --compile-seconds 30
~~~

实际续接目录仍为原 selected-natural-u-schur，不另开空目录。完整旧游标必须至少为八，所有旧完整文件仍由原 runner 逐 SHA 核验。请求阶数及共享预算保持显式有界。

session 应继续读取

~~~
selected-natural-u-schur-pipeline-receipt.json
~~~

其中数学字段的名字和意义不变。额外小包装回执为

~~~
selected-natural-u-schur-serialization-continuation-receipt.json
~~~

记录包装与旧源码身份、实际起止阶、编译复用、被省去的重复序列化字段及真实主回执字节身份。所有数据数组仍只留临时目录。包装本身不执行新的来源数学，实际第九至十六阶由未改动的旧 runner 完成。
