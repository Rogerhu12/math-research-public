# Request164 r3：同一科学程序的新实际运行与紧凑原值读回

作者：OpenAI ChatGPT（amplitude 协作代理）。日期：2026-11-15。

## 1. 实际来源与本次唯一修订

[R371](../results/R371-actual164-r2-twenty-rejections-and-incomplete-compact-readback.md)已记录 r2：run43742275745，source bab76df48309984c2b78d898bdc84dc4019ca51f，compute132897836261/report132898181128。producer exit0、diagnostic-completed、accepted_point_count=0，原 stop 为 “All original20 real trials rejected; initial independent ten-state retained”。reader 所形成的148101B摘要超过原90000B上限，exit70；实际5243B fallback只证实这一控制流及原身份，不能代替20条逐值试探、具体所选形状或初末FD/域/圆读数。

565694B原status已按原生命周期删除，本修订不声称恢复它。原status SHA为7cbba62b0db919a4d15c0b5dd609932a0ef01a4ae57b36d582f660461a0824e0；未传出的148101B摘要SHA为6733294343997e17bb9f57fce4b5822778b6c52c457d8350afb8844d18114856。

本次只修改标量reader和它的引用，仍由新Actions运行重新执行同一科学程序。新结果须有独立实际run/source/原值，预留R373，不能用R371的已知结果预填。producer1998、family0924、model8cb8、adjoint12a9、真实actual157九参数和原recipe全部保持。没有新增科学比较、rank、响应一致性或内层门。

## 2. 读回范围

目标为约40–60KB的单份结论，硬上限仍90000B。这是根据r2实际段大小缩小输出范围的设计，不是已运行的字节测量。超限、缺字段或真实异常仍明确退出，不能提高上限或拆分/编码raw以伪称完整。

- **全部实际试探**：逐条保trial编号、alpha、accepted、actual_merit、完整三残差、原Armijo bound、原完整slope、节点/中点域极小值、原域flag、reason及exception；新系数xi的seed/actual字面逐档保留。固定旧九参数只记录一次，每条仍核原JSON字面是否等于它。若不同，完整异常十参数保留且报告元数据不一致，不会悄悄删去改变。
- **六候选**：全部保support/power/index、实际伴随三响应、原local-forward三响应、两者逐分量差、原full3导数、响应大小、选择分数、eligible等原flag及完整112响应身份。候选完整7状态轨迹、ratio-action表和重复函数定义仅保整体原身份；唯一实际所选形状仍单独保留。
- **初末两种算术**：保四份原description中完整三残差、当前3×10响应/J、相关原域/条件数/原terminal责任标志与完整112残差身份。四份完整terminal-Robin大表只保身份，不声称逐值读取。
- **全部120个FD列的覆盖**：Actions内仍读取、验证12层每层10列的原顺序；保每层原step/valid/max/覆盖flag与所有实际失败、异常。完整扰动参数/方程表只保身份。全局覆盖只给失败数/身份，详细异常留在相应层，避免重复原错误正文。
- **零扩展**：保原全部标量flags、比较条数、完整比较表身份，以及每一非true或畸形比较的完整原记录。匹配项的重复array描述器和重复参数不逐条传输。它仍是诊断，不能变成新增接受门。
- **完整原status、来源、原域、453圆及终门**：来源、input、实际rule同步、三类stop与未访问后缀、完整原status身份及原已有域/圆标量照保。原literal-binding完整数组描述器和伴随起点/terminal权重矩阵改为整体身份，不能据此声称下游逐值审过全部矩阵。

identity函数只减少逐次重复的scope说明；每项仍用同一完整原JSON的排序ASCII编码形成canonical bytes/SHA。其统一范围在coverage中明示，不对任何科学数值重新计算。这个改动不是把大数据改编码传给工具，而是明确不传所列大表。

## 3. 保持的科学与生命周期

原六候选、独立十坐标、只新增xi方向、fresh ten forward重新定符号、尺度0.01、完整三残差merit、准确提升的原binary64 c_A、20档真实回溯、完整初末FD、Arb160/depth14、453圆、完整112末端和所有原flags不变。当前请求仍从actual157参数重建，不从没有接受点的164r2续接。

原112 science pins与10 support pins的名称集合不变，只改wrapper及reader两项；producer消费45源集合与全部SHA不变。recipe仍7483B / 76a93aa076d0a55781fdb3228a895b25583591b269fa5a866ea8068392946820。whole-child2400s、producer2400s、grace90s、reader300s、science50min/job65min、2700s原规则同步及owned cleanup全部不变。reader之后才清理；原完整错误文本转发路径保持。

request engineering_revision改3，previous_actual_failure改真实r2 tuple及原摘要身份，增加新读回范围说明。workflow只更新reader/wrapper两pin和显示名称，原唯一push触发路径不变。没有预填未来run或任何实际数值。

## 4. 冻结文件与完整差异

路径除workflow外相对topics/visible-flex-larger-amplitude。

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| computations/root_20261115_adjoint_selected_ten_control_scalar_readout.py | 30711 | 0fed29ad22913b7c0cf041de5023d9191bcfc46c3674cafb09e77ed37143c47c | 5614f203c2babd4e20ae976de3acf35c38386fd9 |
| computations/geometry_20261115_adjoint_selected_ten_control_temporary.py | 19031 | 263aaa24b3cf78d194058490a0547ffd66471de09f52a540ac6137c17d6c1df8 | 3f90953a7c6c645319346d395d1323c197d61e02 |
| computations/public-adjoint-selected-ten-control-request.json | 43058 | e14936fe4838edce66175e060be6bd804ca6ddb10c66489a0cd44419e3fa7cba | ecc211c46799b98326ea02fb1f98688f336a8642 |
| .github/workflows/visible-larger-public-adjoint-selected-ten-control.yml | 20767 | 7ea5a78dfa1e670cea3b5e4f84a7dd46e880ea451ee61e6282c86fb27447de64 | 31b16c80e9f99a34b7e2084628fef4e6d6b038b1 |

相对已发表r2的完整四件diff：23191B / ae57af644e1b731281163a4eaf768b7ecf408cd5a1ddbb02449b25648b769c3a，blob c1a4faf945063dd56e7e4538229d240fa1b0fb6e。

当前仅源文本/JSON结构与引用、完整差异及SHA操作；没有本地科学导入、运行或fixture，没有声称本地AST通过。原Actions AST/来源检查保留。以上都是小文本对象，无ref更新、无派发、无可重算raw保存。174全站固定odd组合是另一独立算法，不以本次新运行作为前门。
