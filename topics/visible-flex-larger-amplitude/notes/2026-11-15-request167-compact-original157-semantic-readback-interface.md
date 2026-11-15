# Request167 修订：单份原157科学结论，明确大表未逐值阅读

作者：ChatGPT /root/amplitude；2026-11-15。本文替换此前五packet完整选择集传输合同。只在公开Actions读取已存在原日志、原JSON和字节；没有新科学算术、原157重算、数据归档或新的接受门。

## 1. 两次实际读回失败与范围修正

首跑 run43735131654 / source e5dd9ff898b62a85b9f3d98fdc98db4f91201e0d / read job132875931222，在最终metadata index编码处失败：整数outer字典键触发 frozen encoder 的 Non-string JSON metadata key。源随后只将键转为字符串，并保留最终编码异常的具体错误/traceback。

修复版 run43735578724 / source f7e842dbbcf036123919e003b0fb923de792dfac / read job132877329781，已完整解析490个原语义组并完成14095项原字节、顺序、结构和身份核。FD六组各27项、8个outer及其terminal、84次实际trial的必需字段和shape均在原日志中存在；失败发生在输出打包：159个selected sections总807621 B，不能放入五个76000 B packet。本次真实failure index为15213 B / c3b85e519242b1afa67e396c7500062da2953f5749e2bb82d177d2500eb5ab4f。不能据“Actions内已读”声称主控已逐值读过全部J/H/FD或807621 B选择集。

根规则不要求把大数据编码或拆块传过工具，本修订因此改变**传输范围**：保留Actions中的完整原读取、来源及必需字段核，输出一份小于等于90000 B的科学结论。删除tensor引用、字典编码、五packet及大表重建。没有通过提高限额、丢字段后假标完整或重新跑原科学规避边界。

## 2. 固定输入与新增文件身份

唯一日志输入仍为成功163的 read157 job132868510914；run43732715988 / source4e1decc718c712b2eaa26a7da598d89236a21ef0 / attempt1 / report132868952547。官方run/job终态success以及原protocol source bytes/hash必须匹配。

前两个167实际run下载到的同一原日志为8265333 B / caa25be9f57c9d69e3ab8e1764d4ef4431eacbfd40726953df76803dcdafb160，各自只下载一次、使用后已删除。新run不预填未来身份，也不把先前已删临时日志冒成仍在本地。原151/157巨量compute日志及科学artifact均不重新下载。

原163语义索引184436 B / af7100596ea068ec0d194203a2724d8ba1dafb0c6443e03c6b3b31037554936a；原157读回索引62991 B / 16a65e9d484cd0368d135af71ac6b90e0889cba567e5750a7fc05f5dd7cadf25。新读者保留完整490组及两索引的原字节/顺序核。

原科学157仍为 run43729310294 / sourcec71cbeac7fd13c65cf50c7eb39842e9949737b25；其status51842612 B / 931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0，view51846160 B / 82cf345fc42d371eb4adf69e78944a35fce88b3d9503407ec7dff2f25ee8e76a，primary89063 B / 7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2，chain29684 B / 9d8bf161d9b88c0c411d326b1717fd2d32332a49534041ebd495b673a35652bd。只核这些已保存对象的真实身份，不重新生成它们。

题目录前缀为 topics/visible-flex-larger-amplitude/；工作流位于仓库根。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| computations/root_20261115_existing163_157_compact_semantic_readback.py | 57407 | aa37ae1295e24eaa2d98edf396f933a1291444bdfcb1ddb6879f484fd8b3d042 |
| computations/public-existing163-157-compact-semantic-request.json | 15720 | aeefe7afce19205240e2aa22798d059a6782dc6df4263e2b91dacf2bdd6e9305 |
| .github/workflows/visible-larger-public-existing163-157-compact-semantic-readback.yml | 7859 | 7192fd34012ba30350392b54e96b74b78dc341f980910b904db6a6855472f707 |

原metadata helper root_20261115_existing151_157_log_readback.py 保77301 B / ecb77c7e4aae0b7888c58c753ca74d49f0528db3f743443582c3bc4503853250。新源只导入该hash核过的元数据模块；原科学模块不导入。

## 3. 新complete语义与实际打印内容

顶层schema为 existing163157-single-scientific-readback-v2。complete=true只表示：完整原日志和索引核成功、所有要求的原结构存在、下述**声明的小范围科学结论**已成功形成与输出。它不表示所有原科学大表已经经工具传出或由主控逐值阅读。

### 3.1 初末点、终门与FD

初末真实九参数词、三残差/merit、unit defects、Robin两项、原node/mid域余量和原高模/精度限制照原字段选择。原binary64投影点及其已存奇异值/条件数与持久Decimal点分开。完整112向量、原3×9轴J、三残差H只记身份；本次不由这些hash推出数值结论。

六组共162个FD check全部在Actions中解析。输出各原level的标量字段，尤其原maximum_relative_error、valid及完整实际失败/异常check的索引与原异常；error/exception/traceback只有非null原值才构成该分支，不因空字段存在误标失败。若某原level没有保存maximum_relative_error，则保该level九个原scalar check误差；读者不重新求max或做任何FD差分。大正负扰动参数、原差分矩阵、正负响应等只保原完整check/level身份。不得把“原全部check已读且结构核过”写成“全部扰动矩阵已被主控独立逐值核”。

### 3.2 八个方向与内部模型终态

每outer保原merit/残差/半径/接受路径与radius更新，原九gradient、所选九方向、直接作用/轴作用/原差与真实slope、模型有限工作计数/停止及未访后缀。原fallback的实际方向/作用/slope单列，不冒主quadratic路径。

八个terminal均保原九gradient、三模型残差/merit、最后九坐标/局部半径、选择索引与原GN无解/异常分支。Actions内仍核完整3×9 K、9×9 H和GN已解分支的9解、12 RHS/QR残差、9stationarity/列排列/对角；这些核是原结构完整性，不是范数或接受条件。

初始输出尝试额外保**outer7最后terminal**完整3×9 K、9gradient、9×9 H和小GN/QR数组。其余大J/H/K及完整中间表仅原身份。若整份结论因此超过90000 B，这一可选矩阵子集被明确改为identity-only，字段 last_terminal_matrices_not_printed_for_summary_limit 说明实际范围；全部八方向原gradient/action/scalar和全部实际试探仍保留。没有将可选矩阵当新科学门，也没有编码或分块搬运它。

### 3.3 全部84次真实trial

原各outer数量仍必须为 [1,1,1,20,20,20,20,1]。打印统一列名和原行数组：trial index、alpha、accepted、原Armijo bound、actual merit、真实三残差、模型预测reduction、reason/exception、normal stop/target-met/返回误差/选择索引/真实调用与内部试探计数。实际slope从对应outer的原primary或fallback字段读取。原四个接受点的九参数与实际位移另明确保留。

这里不打印每次full112向量、拒绝点的全部参数、normal完整轨迹或全部模型内矩阵。它们保原complete trial/内部覆盖身份。全部实际normal和model异常原字段另列；不把任何内tol=false改写为外Armijo拒绝，亦不重新判断失败原因。

## 4. 单份输出与诚实超限

只有两个job：read和report。read保summary/bytes/SHA三个输出，report只读它们，逐byte/SHA核后原样打印一份 BEGIN_REQUEST167_SCIENTIFIC_SUMMARY / END_REQUEST167_SCIENTIFIC_SUMMARY。

每份ASCII结论最多90000 B；不再输出五个packet、完整array引用表或大对象重建协议。如果明确去掉上述可选terminal矩阵后仍超限，输出complete=false的真实小failure：原summary身份/实际bytes、各scientific字段字节数和清理范围。不会截断84trial、只选择有利trial或声称大表已读。该超限不代表原157科学失败。

原数值token作为opaque lexeme处理；没有Decimal、NumPy、矩阵、范数、rank、FD或优化重算。列名+行数组只是必要原scalar结果的直接呈现，不是原807621 B数据的压缩编码。

## 5. 生命周期、错误与权限

网络只调用官方只读GitHub REST：固定run/job/source身份核与一次日志下载；跳转不转发Authorization，不打印token或签名URL。根/题README实际blob仍21bd547f56590b7f2dd279d0297efb289a9b2783 / bff8aea253a9e6a7a4fac28d810ac454c5499fec。

RUNNER_TEMP中仅建立当前run/attempt专属直接子目录。finally核实际文件身份再删除，工作流always补清此同一目录。原输入日志不上传artifact、Release或Git。read job35分钟、读步骤30分钟，小于原2700秒监控周期；不是改变科学监控或数学预算。

缺字段/shape不合、原GN既无solution又无原失败、来源不匹配、传输问题、超限、清理异常分别如实失败并保原具体traceback。最终JSON编码失败仍有小异常索引。没有通过source或data重标把错误变成科学success。

## 6. 调用与未完成责任

python -u computations/root_20261115_existing163_157_compact_semantic_readback.py --request computations/public-existing163-157-compact-semantic-request.json --request-sha256 aeefe7afce19205240e2aa22798d059a6782dc6df4263e2b91dacf2bdd6e9305 --out "$RUNNER_TEMP/visible-existing163157-$GITHUB_RUN_ID-$GITHUB_RUN_ATTEMPT"

本修订仅以源文本、JSON结构与字节身份完成，未声称在本地通过Python AST、YAML执行或科学fixture。根唯一Git发布与Actions调度；实际新run尚未填。

R350应以实际这份小结论及明确未读大表的范围成文。R351证明与requestless伴随helper独立推进；不以大矩阵搬运、补读或本读者的工程complete作为原科学的新前置门。
