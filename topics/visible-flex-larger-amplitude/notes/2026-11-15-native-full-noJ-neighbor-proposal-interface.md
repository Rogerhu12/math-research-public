# Request103：原完整 no-J 邻词建议与同一 fresh J 的 R273 回退

分类：求解算法与接线说明；尚无本轮数值结果，不是存在性或收敛证明。

## 直接用途

实际95的首个单词方向在完整仿射模型中下降，但原非线性十档试探全部拒绝。103从同一个真实 failed73 BASE 重新开始；95失败不是已接受尾锚。首个 correction 只增加最多三次原完整 no-J evaluate：原 BASE、node11 的 Q76 输入词向下相邻一词、向上相邻一词。每次都走原576段 flow、原 cut/far 和原 sigma；不由四行局部近似拼出目标范数。

候选必须有有限的原 norm，并严格低于本次 no-J BASE norm 与本次 fresh-withJ norm 两者。该条件只选择建议方向。没有符合者，立即使用已经取得的同一 fresh J 进入原完整 R273 QR。符合者仍须通过原十档 no-J 线搜索；原线搜索不通过时仍按原逻辑失败，不额外插入一个已接受步，不在原失败之后偷偷增加 QR 试探。

## 冻结代码与命令

新增两个拟提交源，旧95四源不改：

| 新源 | 字节数 | SHA-256 |
|---|---:|---|
| geometry_20261115_native_noj_neighbor_proposal.mjs | 8128 | 436cfde61ed98720f0e0802978dc4874c42eb42a0193e426b5c5e9e3e0261037 |
| geometry_20261115_native_noj_neighbor_current576_solve.py | 22724 | c8c072e0d65567ba86e9fb72d3708ef5771c8b4ee475e9fcec611371cd447c79 |

公开Actions中的命令：

~~~sh
python -u "$VISIBLE_COMPUTATIONS/geometry_20261115_native_noj_neighbor_current576_solve.py" \
  --original91-directory "$VISIBLE_PARENT91" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --eta 1 --node-heap 6144 --exact-workers 2 \
  --max-factor-bytes 2147483648 \
  --out "$VISIBLE_OUT/native-work"
~~~

入口使用实际 computations 绝对路径。native-work 必须是尚不存在的 RUNNER_TEMP 子目录，且独立于原输入和源目录。原总预算32、每步10档、eta=1、容差2e-9、原最终 endpoint J 和 audit 均不改。最多三个新增无J调用不计作已接受迭代，并在实际日志中逐一记数。

初始输入仍为完整已存在actual91 artifact：run43672150224，artifact14145200674，10267458 B，ZIP SHA 78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6。该包只在runner临时读取，不再次归档。所用BASE SHA为 f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6。

## 三份临时适配源的责任

入口从四份硬SHA原95源做明确文字变换，生成仅runner使用的 hook、system、chain_qr 三个新basename。它们不能事先提交同名文件，因为生成使用独占创建。system与QR保持原数学代码，只更新真实producer名字、schema及派生依赖SHA。hook替换首建议，传入原evaluate/cellFlow闭包；不存在用旧J代替新J的分支。

主入口记录提交源码SHA、实际执行的派生driver文本SHA以及三个派生源码SHA。派生driver以新提交入口作为真实producer文件；执行文本的独立SHA另报，不伪称两个字节相同。原父件绑定仍按原helper验证；它保留的旧仿射读数只是历史来源，不参与103建议选择。

## 临时文件寿命

每次 correction 保持完整 fresh snapshot、所有原 QR 输入/因子/精确读回，直至同步子进程结束、完整方向读入内存并校验、原状态/target/scales不变检查和返回记录写完。随后删除仅本次新建的 iterationDir。

这个删除位置不截断原科学链：hook finish只消费内存records并写顶层summary；外层driver只读顶层完整原response和summary，不再递归打开历史snapshot/QR descriptor。原 endpoint J/audit使用实际worker状态，不从这些临时文件恢复。父91 binding持续保留到整次原client关闭。全部out只在原close、原result以及compact结果读出后清理。

遵守根README第15条：无upload-artifact、Release或raw Git发布。文件SHA引用描述已消费的临时原字节，不声称以后仍可下载。未来即便native接受，本轮compact日志也不自动成为可供跨进程live客户端读取的已保存锚；不能据此伪造完整原件。

## 输出与实际判读

标准输出保留源码/参数/run身份、每个原no-J建议的实际norm与IEEE词、129248行摘要SHA和真实最坏行；原stage10/11输入、输出、残差分别hash。记录完整原trial的既有标量、每次返回的方向类型、原QR范数/行数/因子摘要，以及最终原response/result SHA。完整向量/矩阵不打印。若原QR子进程失败，先输出其实际错误、有限长度的trace/stderr尾和完整文件SHA，再删除该次临时目录，避免只剩通用退出消息。

原evaluate函数源码SHA固定为9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9。所构造delta必须按原单位步表达式逐词重现被选邻点；全状态、target、scales调用前后保持原字节。诊断argmax仅读原返回数组，不替换ev.norm或原门。遇到实际no-J域错误，保错误及计数；无可用严格改善时返回QR。

这不会保证邻词有益、保证原十档接受或保证R273收敛。本轮实际日志将区分：邻词均不改善而QR执行；某邻词进入原试探；原试探失败；最终原native真正接受。

## 相对95的唯一工作流变更

独立workflow visible-larger-public-native-noj-neighbor.yml，独立push请求 computations/public-native-noj-neighbor-request.json，编号103。原Python3.12.14、Node24.22.1、numpy2.3.5、scipy1.17.0、单线程及350/320分钟限制保持。来源闭包25件：旧24件去掉旧publisher，加两个新源。旧候选源保留作父来源闭包，不由103 selector调用。

不再为32轮累计保存raw预留32GiB；仍保原每次完整factor2GiB上限，逐次消费后释放。最终只清理本请求明确拥有的临时目录。取消旧raw artifact与publisher两步；主控按实际日志发表结论和输出SHA。

旧规则runner源码3b8b6dd5不改，但其旧内嵌README基线已过时。接线先核当前checkout两个明确已读blob：根74c08a36f6c997d0bc1e64a7956b42276f5fa5d7、题bff8aea253a9e6a7a4fac28d810ac454c5499fec，再显式更新运行时BASELINES并打印此责任。原45分钟普通pull/rebase、两README差异判断和实际规则改变时停止行为保持。不是把任意新规则动态视为已读。

## 已做与未做

已完成小文本源锚、哈希和JS语法静态检查；没有本地科学、Git/API写操作或dispatch。环境不可用，未声称本地Python AST已运行。Actions原编译步骤和入口派生compile会实际检查Python文本；这些是实现执行检查，不改变科学验收。尚无103 run、结果或成功锚。
