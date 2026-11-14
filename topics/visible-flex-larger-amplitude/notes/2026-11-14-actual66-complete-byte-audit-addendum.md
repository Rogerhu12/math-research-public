# 实际66原件字节附记：完整20-query B、QP数组、observer与14份root输出

分类：既有公开 Actions 原件的完整字节身份读回；非新科学计算。  
作者：ChatGPT（amplitude 与 exact_refinement，AI 辅助）。  
日期：2026-11-14。

## 1. 与主回执的关系

本附记补充[实际66主回执](2026-11-14-actual-request66-twenty-query-nearest-left466.md)
冻结之后完成的字节范围，不修改其原 trial、优化结论或当时“完整大数组尚待
审计”的时间范围。原科学 run `43651436427`、source
`cf3a8ff94fae3f7009f85047c69db3aeb8eb320a`、artifact `14136283207`
均保持；完整 ZIP `562089949` B，SHA256
`96444f8c03257bb817a0367d73a094567eac5cdf895dfb38a7695646f454385b`。

这次合并使用两份已经完成的只读回执，不重新执行 payload 审计或数学。
amplitude 使用冻结20-query reader 的纯字节函数核 domain、condensed和
observer；exact_refinement 为同父阻尼对照保留66基线时另核原 b/g/c、
B及14个 root 输出。两份回执在 B 上有重叠，本附记只计一次，不把重复
读取冒成新增不同原件。

## 2. 已核范围

| 原件类别 | 本次已保存的字节核范围 |
|---|---|
| domain operator | 181个 NPZ、1168个 NPY 数组；压缩文件、成员dtype/shape及原数组字节SHA均匹配 |
| 完整20组 B/Gamma/Pi | 所有分块按原顺序重组后的完整数组 SHA 匹配；完整原 beta、scale、base及端点捕获身份保留 |
| condensed QP arrays | 103个 NPZ、103个 NPY；42个完整引用对应38个不同完整数组，所有分块齐全并重组核SHA |
| collocation observer | 14份原报告，原 finite、residual bytes、collocation bytes 的 unchanged 标志全部为真 |
| midpoint observer | 12个原 NPZ、36个 NPY；全部在原模型中有描述器，文件SHA及原数组身份绑定，保留NaN原bits |
| root / affine / recovery | 14个原 raw文件、共377613808 B，原shape/dtype/size/rawSHA全部匹配producer描述器 |

domain与两份基线报告共同钉住 B 模型
`e6928853c2a125212dc4909a3b2fefada07e7320d23ee0d4817634afec89d511`。
完整行数40960、全列236036、声明连续局部6763、实际 B block并集6425；
node484的338个显式零 B 列仍属完整 H 自由坐标。这里核的是保存数组和
布局身份，没有重新计算 B/B转置、曲率、域、范数或某个优化方向。

14个root文件逐项报告位于合并摘要中，来源为 exact_refinement 的
`verified_condensed_root_arrays`；合并时再次只比较这些既有记录与原
`original_condensation_report.output_arrays` 描述器的名称、shape、dtype、
字节数及SHA，没有重读大payload。原 source/父 pair/新warm/status/FD
身份仍引用主回执已付的15原文件、11项绑定和55源码字节检查。

## 3. 实际保存的回执与压缩身份

完整核查明细较大，以下 gzip 是原 JSON 字节的无损保存，不是截断或分块
搬运大报告。小摘要只摘审计范围、计数和14份raw描述器：

- [合并摘要](2026-11-14-actual66-complete-byte-audit-summary.json)。
- [amplitude完整prefix字节回执](2026-11-14-actual66-prefix-byte-audit.json.gz)：
  gzip 77227 B，SHA `25b4ccf705f74ef69b53c40d0a07e33b2e8543e2fe852ecc09fb287214a759fb`；
  解压后原657748 B，SHA `b553bf721e01b09990e3c75476e46c83d2204f2b167ed17bf6efa427b3d4e48d`。
- [exact_refinement原基线及14raw回执](2026-11-14-actual66-baseline-root-byte-audit.json.gz)：
  原gzip 54606 B，SHA `74cb59651a3908ba2dea664775ff76fde2bcb9f7e268579d4c80c366f5bca6aa`；
  解压后原428556 B，SHA `c7b03aa2b6254c31a49d77cf3ebbd19d30e81b95718790f920adde2f0a3388bb`。

前一回执的只读函数来自冻结 reader
`cf93537dadafa72cbe042a453cbe9a1cec0aca4cf1a25a0d979cca3cdb0b2f2f`。
未调用其下载/main或任何科学模块。NumPy仅用于已有 NPZ解码、dtype/shape、
原bytes转换与SHA；没有执行新的 RHS、Jacobian、ODE、矩阵动作、点积、
范数、优化、有限差分、native或Actions科学运行。

## 4. 不超出原件所能支持的范围

完整链 QR factor 当时只存在于原进程内存，未独立导出完整payload。
本附记不能把其原四组内存hash写成“独立完整factor文件审计”。九个完整
A输入数组也只保原Actions报告hash，本附记没有重新构造这些矩阵或证明
对应数学线性化正确。

当前结果仍是未接受完整 BVP 的优化 warm；字节一致不证明QP严格最优、
连续角域有效、原finite场严格等距或最终闭面成立。它只补足实际66记录的
可追溯性，为后续从其真实 pair 继续，以及同actual64父场的单阻尼对照
提供准确的原件基线，不增加任何科学接受门。
