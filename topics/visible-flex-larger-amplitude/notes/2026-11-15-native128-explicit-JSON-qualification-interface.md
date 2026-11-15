# 原128组件的显式JSON名称限定：152与150共用入口

本文件说明独立入口 geometry_20261115_native128_qualified_json_components.py。原140以及刚发表的R314/R325三源保持原字节；新入口仅在实际Actions编译目录写指定源的副本，将已确定的JSON helper调用限定为全局::quoted。没有改数学、预算、root策略或任何接受门。

## 实际原因和精确修补

原113全局函数为quoted(const std::string&)，并包含iomanip。对于非const std::string实参，未限定调用可由ADL选中std::quoted(string&)；其返回流操纵器与所写三目字符串分支不兼容。实际140的g++返回1已记录，但编译器stderr正文未转发。因此这一名称解析诊断来自固定源码，不冒称原日志直接给出了该文句。

只允许下表五个固定原文件。每件先核完整原SHA，再核OLD token quoted(的精确次数且不存在NEW token，替换成::quoted(，核完整派生SHA，并反向恢复原全文。原Git文件不写入、不改名；派生源保同basename仅存本次compile_dir。原函数的数值表达式、循环、顺序、矩阵、factor、224/226维和两个means全部未改。

| 文件 | 原SHA256 | 次数 | 派生SHA256 |
|---|---|---:|---|
| geometry_20261115_native_operator_trace128.hpp | 950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0 | 12 | 046fafc0421ebf22a68437abab62594a525acbec815a660719f91a2c18cd0a0e |
| geometry_20261115_native_operator_stage128.cpp | 86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926 | 9 | ad61daf7f86f46bac20102764e65d4448f23a725a7db4917235ea789cf7075bd |
| geometry_20261115_native_boundary128.cpp | c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96 | 4 | 994c0b8b52f1f5d7bc18db0fc5430d962bafcb6060bb61b276a50f8bddceb8ed |
| geometry_20261115_native_physical_final128.cpp | a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415 | 49 | 05a4a97c41e0e53347b51fc6eb9936eba62a73e224e267e3c3e14c6e5b74014f |
| geometry_20261115_literal_root_field_tape128.cpp | 2aa2ad6737ca16854350967bddf49846e345ba5195d799d21dcc40a870c925bb | 2 | 425422732388512435fc2dbecadc1098ff3a1c2400ac3f620b91879fb6cd846e |

每次g++实际argv只改其唯一CPP路径，转向本次临时副本；既有flags、两个include目录、输出路径、编译300秒cap、实际global deadline全部保持。operator stage与field exporter另在同compile_dir写上述operator header副本，确保#include采用它。其余shared header、原R283 prefix、原113 CPP、boundary/physical数学依赖仍走原完整身份核验。

## 完整152入口

在原140组件命令的launcher位置改为本文件，并紧接添加--operator-components，其他CLI保持原语义。新顶层schema为native-persistent128-qualified-JSON-contracted-trace-components-launch-v1，source_sha256为本文件实际SHA。

本文件load_baseline()仍返回原R305/R302 input binder和生命周期供同job父入口使用。原R305主程序及validate_prior保持函数正文，显式切换顶层schema和实际entry身份；所有后继prior都需相同新schema、新entry和完整source集合。source集合保原来源并添加原R305 launcher及此实际entry。旧报告不能改标签充当新报告。

stage、boundary、endpoint、audit的数值源码/科学schema和全部完成判据不改。临时编译来源记录列每件原/执行bytes与SHA、全逆向相等、原/执行argv和原prefix。scientific_complete、partial、native/fullDN等原字段仍由实际组件结果决定。152仍承担完整576×224、112边界、338×112和独立audit；本入口不以150单field替代它们。

## 完整150入口

在原R314 launcher位置调用本文件，并添加--strict-field-certificate，保原所有packet/owner/state实SHA、field选择、230列/320bits和预算。新顶层schema为literal-root-field-certificate-qualified-JSON-launch-v1。

本文件在原launcher源的唯一evidence binding位置仅添加两项元数据：实际临时编译来源及此Python source factory的原/执行SHA、逆向全文相等。原数值exporter的变化仍仅下表JSON限定；严格integer interval consumer659ecdc0…不改一字。原full result仍按原schema记录。不会把C当F_e或证明IEEE roundmap导数。

严格consumer若因85KB有限summary溢出返回70，新入口保其returncode与summary_complete=false，不把科学完成和summary传输完成合并。150父入口必须传--retain-temporary-for-same-job，在清理前读取完整launcher/result.json和certificate/result.json，输出全部字段、所有列和未访问后缀。仅summary/哈希不足以恢复230列；此责任由独立150同job编排落实。

## 错误原文与父入口接点

每个实际子进程结束后，本入口读取其stderr；每一完整UTF-8原行通过NATIVE_PERSISTENT128事件输出，保完整原行文本（含原行结束符）、原文件bytes/SHA、行序、该行bytes/SHA。不截行、不base64、不把大数值数组切片传输。编译stdout也作同样输出。单个不可分原行超过60000B时明确列为未转发，complete=false，不能自称错误全文保全。

父同job运行器须在每个组件返回、原清理前，把组件stdout里以NATIVE_PERSISTENT128开头的完整行直接转发至既有fresh watcher。若只抄compact-summary而不转发这些事件，仍会丢compiler原文。process记录同时保存实际执行命令、JSON改写绑定和每个stderr读回的complete/缺失行范围，原caller command若仍是请求argv会明确标为原source请求。

本wrapper并未在本地编译/科学执行。源码文字和全部五件替换逆向/派生hash已核；实际C++编译及科学仍只由公开Actions完成。修复已确定的ADL阻断不保证不存在其他实际错误，更不预付后继方向/响应/物理验收。

## 来源与身份

- 原R305 launcher：a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef。
- 原R314 launcher：cd73cb044e72052b38c6fc9d6517a7e436517f15777a4ace74333bb8a92af596。
- 原共享binder：ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045。
- 新实际entry：15058B，e609fb0aeae3142fcdb779004ddc0966e86c87c437da0984f50ffa814fb40d36；blob6f13e4335daacb19bad446f8542ff4b6ee692b7e。
- 五个源的完整文本diff：21765B，768d50458a0e3e0f21f4538beb74c3e69ce0b8107df807067ff99699420cdfc1；blob8f138d77cd3554fd1811fce731e2b099c23b70d3。diff可从这些精确源重新得到，不是科学数据或额外门。
