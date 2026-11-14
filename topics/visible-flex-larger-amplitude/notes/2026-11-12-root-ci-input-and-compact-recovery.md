# 2026-11-12：真实产物导入与首组表示修复

作者：GPT-6 Astra Pro（AI协助）。本记录不构成闭面完成声明。

## 已发生的正式终态

- run43303787139 interval：全46物理Green几何正式0，360.047658655s/46300KiB，10793原叶、10878子片（10870 Taylor+8root）、18完整组；有序Fraction预算正式0，392.053089258s/24636KiB。原local V、rho16完整weak Γ46≤.001239705310、两输出≤.000055648606；uniform V0失败未选。
- run43307481613 interval：root-actual-linear-centre-source正式1，1.002227352s/48636KiB，signal=null，0完整组/0原叶。recovery明确TypeError: list indices must be integers or slices, not str。源码R84生成phi_physical_PK用compact_ball列表，而重建读取处用仅认lower/upper字典的ball，表示不一致已由两个源码定位。
- 本次仅把该列表恢复改为已有pair→exact_q区间合并；所有公式、参数、覆盖和验收门保持。原源SHA0828f8597f2847c2a321d8e2804a9ff21e0084ec1abb1c80421ba303ab659b20，新SHA306b2bc0c49635d731f3bbe91653310f2b2ecba19bcb7437f8ef932f37a5d75b。须fresh全量实际执行，不因实现修复预告数学通过。
- 原q096 run43302113873已数值formal0且summary solver_success=true/audit_pending=false。原72件已通过artifact SHA及原stable63文件逐项字节核对并正常推main。恢复小报告后段仍失败，原异常尚待实际旧gzip日志诊断；稳健报告修补不冒称已知原因，原BVP不重算。

## 新运行器的窄输入导入

触发checkout保持精确源码。独立publisher先实际git pull --rebase origin main并比双README；仅匹配request的topic/notes显式globs，从该main提交经终端git cat-file以原二进制写入，逐件验Git blob SHA1和SHA256，原路径存在则必须完全一致。记录main-imports.json，拒绝改代码、改已存在不同输入或借后续漂移main。

这使已付全46原primary可用于R88，而不通过连接器编码搬大文件。两个旧失败日志也仅经此机制取回，在runner终端解压为小JSON文字诊断，原gzip仍保存。未来非零子进程terminal记录追加有界末尾文字，实际wait4/资源不变。

## 接续

同一interval串行：真实新中心完整源→精确有序cut消费；独立tail源绑定→物理r矩→完整J→正A→carrier完整J→同覆盖比较。依赖失败只跳过相依stage，继续独立子问题。strong独立恢复有界报告→真实固定视图/控制列。R88不因计算exit0便宣告数学门，R90需另有完整证明与实际数值。

原README授权与完成标准始终保留；实际pull后如规则变动立即只读差异并执行新规。
