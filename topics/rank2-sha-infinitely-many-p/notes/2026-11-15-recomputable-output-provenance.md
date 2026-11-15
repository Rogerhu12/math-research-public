# 规则15：历史可重算输出的复现入口

2026-11-15。遵从根 README 规则15，当前树移除148个已有生成脚本的输出，
合计2,645,461字节。原脚本、固定参数、正文、运行引用及输出SHA256保留；
Git历史没有改写，也没有将数据迁到Release。尚未认定可重建的输入没有据文件名误删。

## 保存的元数据

[完整脚本、参数及哈希清单](../ci/removed-recomputable-output-manifest.json)
固定历史提交
`94c0b45f0e6b91471c9422c79ebdfa9c98c83adb`。
清单包括原输出路径/SHA256/Git blob、对应脚本/SHA256和参数。
audit run `43681121218` 只审计文件与来源，
不是这些历史数学计算的首次run，不冒充首次运行。
以前的真实执行记录仍以原正文和log为准；未查得run_id的条目明确记null。

有些旧文档链接指向本次删除的JSON。它们现在是历史输出路径；
可按清单从该固定提交取回，或按脚本重新计算。它们不是当前树缺失的新数学输入。

## 旧检查器读取已删输出时

[临时复现工具](../scripts/run-with-historical-inputs.py)
只在系统临时目录复制本课题、恢复指定历史输入并验证字节数与SHA256。
它不把输入或新输出写回工作树，也不创建Release。
结束时临时目录整体删除。需要的Node、Python包或Sage仍按原脚本/原workflow准备。

例如R674读取原R594生成报告：
~~~sh
python3 topics/rank2-sha-infinitely-many-p/scripts/run-with-historical-inputs.py \
  --input scripts/check-r594-two-source-six-carry-compensation.json \
  scripts/check-r674-double-s-arithmetic-adaptation.js
~~~
这里只从不可变历史恢复R594输入，R674按保留的当前脚本重新计算并输出到stdout。
不指定 `--input` 时，工具恢复清单中的全部历史输入；
需要检查纯独立程序时可用 `--no-historical-inputs`。

有些旧生成器默认写同名JSON。用下面方式在临时副本中运行并读其新输出：
~~~sh
python3 topics/rank2-sha-infinitely-many-p/scripts/run-with-historical-inputs.py \
  --no-historical-inputs \
  --emit-output scripts/check-r617-original-norm8-annulus-and-negative-five-pole.json \
  scripts/check-r617-original-norm8-annulus-and-negative-five-pole.js
~~~
工具会先删除临时副本中的同名旧文件，要求本次执行确实生成该文件，
再把它送到stdout；不会将恢复的数据冒充本次生成结果。
这两个不同复现路径已在公开 run [43682050475](https://github.com/Rogerhu12/math-research-public/actions/runs/43682050475)
（job 132714580253，源提交 b71230698e5e96d807650bb3ac653607877a9f8b）完成。
R674 的36848字节stdout SHA256为
`c55c6789c38bc37e4536bec1df0e3cf6f2377e4a8ba52d05329ed80a140b2638`；
R617 的10676字节stdout SHA256为
`272e2cdddc71cb6240cacfff5d87e6c3a740423056d6142772c609981acd56ac`。
两者均与清单所记原输出哈希完全相同；原输出未重新入库。

## 尚未清理的类别

旧 `check-jzero-weighted-conductor-integral-part1/2/3.json.gz`
及其主JSON是现有校验器读取的证书输入；尚未找到完整生成器。
同样，原weighted-normalization presentation的主文件是校验输入。
2026-11-15 05:40:06 UTC 的实际CI pull（run 43682050611/job 132714580701）
核两README差异空，库存27,598,858字节、1852文件、无超5MB文件，
仅上述3个旧输入分块；没有新增分块。
其它mixed-I/O及缺明确生成器的历史文件继续按真实依赖审计，
不从“存在同名脚本”推断其可重算。
