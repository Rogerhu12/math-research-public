# 完整ready参数JSON只整理外部空白

会话Astra-larger-e4e2a2bf-20261126（AI-assisted）。2026-11-28 08:09:42 UTC。

## 本次范围

本次完整读取148份10KB–100KB以内的computations/*-ready.json，104份只改字符串外JSON空白、44份原字不动。另42份half/r725/r726/r728/R727/spherical/slerp/R729相关ready明确排除，包含24–29当前半波/Slerp及25续跑的全参数ready。活动queue/request、source-binding、全部runtime、实际moment输入、locations/report/packet/typed均未动。

这104个**完整参数文件仍以同路径、全部原参数词和字段保留**，没有退掉配置、改名作输出、去掉历史、减少预算、选择器、live投影或变量。原所有数字字面（含指数、整数精度和负零）、字符串转义、键序、数组序和原对象结构逐字保，只删字符串外ASCII空格/tab/CR/LF，最后写一个LF。未把解析得到的Number重新序列化。原JSON合法性读取不用于重新构造其数字。

毛节省495096B。精确104个old/current全身份和44个不变项、42个排除项在[完整映射](../computations/complete-ready-json-lexical-format-delivery.json)。每个原体、新体和本次伴随文件都小于100000B，未读取大/二进制raw，未分块或编码数值数据。完整queue的原step对象及运行预算均未随本次格式改变。

## 运行和历史来源的边界

已经实际读到的31/32 driver、launcher、pure主入口不从这些ready读取数值；runtime source角色全是原完整脚本，实际输入由完整CLI/queue指向。当前物理母体的42份参数readies另外排除。此事实只限定本次文件修改边界，不声称所有历史消费者都不存在，也不加新的科学前置审查。

ready中的旧full parent/parameter/source identity仍指原历史版本，不把格式后新文件冒旧SHA。任何旧生成器、参数继承器或whole-hash读者须先按固定提交`6c07ca019af58f0102a40a00c63027948ee0332a`及原全路径，或原Git blob，恢复整个原ready到独立历史目录，连其余原完整输入一起消费。参数原字可恢复；新格式文件自己的字节身份只用current列。

## 三次词法格式历史

| 完整映射 | 原whole固定提交 | 范围 |
|---|---|---|
| [保全账映射](../computations/complete-retention-json-lexical-format-delivery.json) | `f687c963cbc899e211a3d083c12b2f1b7e322d4d` | 87旧retention JSON |
| [历史note映射](../computations/historical-notes-complete-json-lexical-format-delivery.json) | `9eb3fd8d960b61be6ea2440a47580f15923ac0ed` | 96旧note metadata |
| [本次ready映射](../computations/complete-ready-json-lexical-format-delivery.json) | `6c07ca019af58f0102a40a00c63027948ee0332a` | 104完整ready参数 |

三次都只改字符串外空白，不把某一批fixed commit应用到另一批原字节。旧whole hash和新current hash从不混用。全部旧科学结论、失败、来源缺口和原参数责任原字保留；这不是新的数值/数学进展。

## 完整再生

[再生器](../scripts/resume_20261126/reproduce_complete_ready_json_lexical_format.mjs)沿用已刊3694B/360c09a86237840e913c5a45cc3ca1075d87f444的完整词法函数，只更新自身名称和明确schema。它逐项读取全原体，确认原whole身份，产生全新体并确认新whole身份；不运行Python、科学模块、AST、compile、fixture、benchmark，也不进入任何science queue。

```sh
node scripts/resume_20261126/reproduce_complete_ready_json_lexical_format.mjs \
  --manifest computations/complete-ready-json-lexical-format-delivery.json \
  --source-directory <历史仓库根> \
  --output-directory <新的独立仓库路径根>
```

该命令的相对script/manifest路径从课题目录调用，source/output两个根需各自包含完整topics路径。普通新增提交保存此格式变更；没有改写历史或force，也没有把再生说明冒实际研究结果。
