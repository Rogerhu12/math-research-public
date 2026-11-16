# 已付七十四条完整关系的原高权来源交换

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 仅消费实际完成的权八数据

本入口只读已付原 $17674\times1386$ 矩阵、原字典和完整 native 结果。原 1286 列前缀实际独立，最终秩 1312；最后一百列保留 26、删除 74。七十四条关系各自有不同的目标单位坐标，所以正是此固定权八映射的完整常数核基。

不重做大矩阵消元。不用其它参数点、随机投影或未完成的候选。所有结论仍在原 $p=127,d\mapsto100$ 的完整十二参数多项式模型中。

## 2. 原十四高权坐标的完整投影

原十四条权八生成元 $D_\ell$ 在固定字典中的输入位置为 1092 至 1105。程序实际检查这十四个不同原标签的乘子均严格为 1。

从七十四条完整原关系取这十四个坐标，得到 $74\times14$ 矩阵。小消元同步保存七十四条原关系的系数组合，并逐全部 1386 原坐标核乘回。设真实投影秩为 $k$；程序不预填 $k$。

由完整核的投影精确序列，去掉所有十四条 $D_\ell$ 后，固定权八像的余维恰为 $14-k$。实际主元给可交换的 $k$ 个原 $D$。这个判断不要求重新处理 17674 个输出。

## 3. 交换只能在原多项式乘回之后生效

同步小消元使主元 $D$ 系数块为 $I_k$。每个主元行是所选 $k$ 条真实旧依赖式的组合；程序实际核其不使用其它已删除目标。因每条旧依赖式只含其自己和原独立输入，交换来源只需要：

- 未删除的旧均值、交换子、三十条 $V$；
- 已保留的二十六条新像；
- 所选 $k$ 条先前删除的新像。

把原主元 $D$ 移到等式一侧后，逐参数乘子回填完整十坐标，并将同一组合用于原十八来源；两种完整多项式乘回均必须通过。删去 $k$ 个旧 $D$、加回 $k$ 个新像后，命名生成元总数仍为 106，不能称生成元数量下降。

模等价的两方向都保留原来源：新加的像已有父关系，属于旧模；被删的 $D$ 由本次实际交换式属于新模。因此整个参数子模相等。代码另统计真实删去与加回列的单项式数；不由投影秩预称项数减少、候选更快、稳定闭包或单位理想。

## 4. 来源与执行接口

主源：

~~~text
notes/2026-11-16-r150-weight8-old-high-source-exchange127-789f.py
blob b274ce3eeb5698ae3abb84322c72a1941fea48b1
13777 bytes
SHA256 b3e358f5da42777eedbaaea0a7715c754e22f7cc705d3c9f3e5714570355a803
~~~

同名 `inputs-789f.json` 保存完整 helper 和三个原 native 输入的逐字 SHA。原父 manifest 必须与它自己的实际完整 receipt 匹配；其完成状态、原来源终门、完整字典和 native 结果均重新核。

完整 CLI：

~~~text
python notes/2026-11-16-r150-weight8-old-high-source-exchange127-789f.py
  --model-source {scripts}/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py
  --model-out {work}/original-ten-parameter-module127-v2
  --compression-source {scripts}/2026-11-16-r150-original-parameter-seed-compression127-789f.py
  --weight8-source {scripts}/2026-11-16-r150-original-complete-weight8-frontier127-789f.py
  --weight8-out {work}/original-complete-weight8-frontier127
  --mean-frontier-out {work}/original-mean-first-frontier127
  --out {work}/original-weight8-high-exchange127
  --through final --seconds 120 --memory-mib 768
~~~

`--through inspect --seconds 30` 只完成小投影、实际原关系组合和全部 1386 坐标的标量乘回，不能提前称已经完成原多项式换列。`final` 才消费每个原来源并核完整十/十八产品；外层可取 180 秒。同源码、语义 binding 及完整 phase 下继续，旧物理与逻辑 SHA 必须全匹配。

使用 Python 3.12.14、python-flint 0.9.0，无需 native 编译或 Singular。源码冻结时仅 AST 语法检查完成，没有投影秩或换列数学结果。所有原关系数组、来源多项式、完整 raw 均只在临时目录；仓库仅存源码、参数、证明与实际执行身份/SHA。
