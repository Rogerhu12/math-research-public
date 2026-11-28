# 原短厚纤维双图与完整多链：独立小软件核验

会话Astra-rank2-Sha-0b097461-20261127；记录日期2026-11-28 UTC。**第二次实际运行的两小checker及独立host均PASS；第一次环境门失败的记录保留。** 完整主课题未完成；v17运行与源不改。

## 1. 本次实际来源与协议

数学依据为[R1071 §§10–11](../results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)：真实G13全窗口、单厚纤维总度21、完整核/低权领先行/两图回代/原field多链/双ideal及post-ideal整条X门。六个新模块是 original_short_graph_field.py、original_short_graph_popov.py、original_short_graph_multichain.py、original_short_graph_outer.py、original_short_graph_kernel.py、original_short_graph_global.py。两个小checker分别核多链外门与完整厚纤维两图。

本次请求[原JSON](../ci/original-short-global-graph-software-request.json)7969B/SHA256 03d325b63d505574486a1bb6034ea503db9094bae18513dd0db7dac3ca2c78f5，包含所有43个实际源pin（8新/35旧），canonical manifest SHA256 d2f9ba0d1fcea025f7ddb592ef0abda68923e41adbca22103ae5f8cd819abe9a。host 13658B/SHA256 48482ba328a25652ddf9f9ffa885ff63e667ff6c2c6423971edf9aa36f7d9fad；独立workflow 3881B/SHA256 5a976ac37ecc1e7530658b46fa41b790abe81e5276ed76a55a33718cb5dcd1c6。旧43源中的producer仅被导入取得原实现，不执行306生产。

根与代理分别按真实字节核43pins、AST/原局部import依赖、JSON manifest、两段bash语法。根读完所有六模块/两个checker/host/workflow，核真实二次域alpha²=alpha+1/4、完整δ0尾、实际双图对象引用缓存、原D单位厚π^m、全部模q进位、全原域kernel、完整常数阶梯、原N/D两图回乘及ideal后双解全X相等。没有在本地运行数学。

两个checker在同一个Sage10.6固定镜像进程内执行；host在启动前读取实际docker inspect，核单一container id、4CPU、16GiB内存与总swap、network none、完整源码RO、三个线程值4、原argv以及无host凭据。420秒timeout/15秒kill，job10分钟；两段真实输出/结果/selector/public envelope均由host重新比对，docker wait必须0才允许HOST。镜像 sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb。

## 2. 待执行的真实案例及拒绝条件

多链checker：3个prime/quadratic manual，包含非二项式真域的原Sage乘法/三角逆/标量逆；真链长度0/3/2及非零δ0尾；8个原整图比较，2个已造ideal后的高次X篡改拒绝，2个相同fraction-field秩但真整子图的拒绝。每个案例用当次旧完整图所得全部H±/X比较，非预报值代原回代。

全图checker：7个真实P¹模型，含非标量公共因子、四阶极和全部29线性中心非单位从而必选二次π²的例；共14张真图比较并读两互补纤维长度、RR维数和完整配对行权。两真删最后一厚位与两错反图必须拒绝。结果明确original_rank306_geometry_executed=false；实际日志尚未取得前均不记通过。

根在启动前读两仓库Actions API：公开in_progress total_count13/queued1，私库in_progress0/queued1；本题仅原v17为heavy，小软件采用独立并发组，低于根规则13的20上限。本次11新路径不匹配v17工作流路径，原所有下游端点/厚交/Norm/九pairs接受协议未改。

## 3. 首次启动前尚未支付的部分

在首次启动之前，没有本次实际source/run/job绑定、43源消费日志、模型比较或软件PASS。即使小软件通过，也只付该小模型的实现，真实306几何、21总度厚纤维及完整下游仍须在原来源上实际返回；不从静态源预写生产结果。

## 4. 第一次实际终态：Sage后环境门失败

实际source552c8deb545839020f254715462828ef8951d963/run46144370977/job140977052249，2026-11-28 12:22:54 UTC创建。根与代理独立读取同一完整日志，25763B/SHA256 e26dbd4a1b211cbb91b465a956b3828495db371bb0c5ac926f1185160699197d。12:23:41.5171874Z的真实CONTRACT为5959B/SHA b832e1e988e5d656ef129fd65012a294a9a11be2ede5b0044c9a5395cc5b293a，含本次43host源绑定、实际4CPU/16GiB含swap、禁网RO、三线程配置4及无host凭据。

12:23:41.9446915Z在execute的环境require报Incorrect isolated execution environment；零SELECTOR、零checker结果、零PUBLIC/HOST PASS。host随后missing PUBLIC是继发失败。job步骤1–3/清理success，步骤4failure，退出1。此失败未执行数学fixture，不是图/全多项式门失败。只保run/source/hash，不存可重算完整log。

根实际读取[Sage固定10.6的sage-env](https://github.com/sagemath/sage/blob/10.6/src/bin/sage-env#L592-L600)，其无条件export OPENBLAS_NUM_THREADS=1，说明Docker配置值不等于Sage后值；第一轮没有打印后者，故不伪称已经观测其具体三值。

## 5. 最小修复与第二次来源

只修改host的execute入口：先打印三线程值、四个凭据键是否存在的布尔、NumPy是否已加载；从不打印凭据值。强制尚未导NumPy且无凭据，随后把三线程值恢复为已经inspect的4，再做原exact门、发真实RUNTIME回执，才进入原两个checker。host独立核此RUNTIME的完整JSON/SHA和PUBLIC相等。数学43源/request/workflow、所有案例与拒绝条件不改；原v17不改。
修复host为15461B/SHA256 f51f71e3f9babf64b480fb1d18eee77aa9d9dbfcc7a7a5adf51f27b1c3660b8b；本次仍待实际source/run/job和完整软件结果。

## 6. 第二次完整软件 PASS：实际原域、厚图及拒绝门

实际source **6b17ab13cc4d1d38b4854403e5abf9ab471e7bd3**，[run46145004405](https://github.com/Rogerhu12/math-research-public/actions/runs/46145004405)/job140978975713/attempt1，2026-11-28 12:30:33 UTC创建；所有步骤最终success。根与代理独立取完整log，各得43121B/SHA256 **6d4403785fa5fefa87e0189acf3b268172216d571550a5ca6c254d4bd2bdb8f5**。以下只保存来源及精确hash，不保存可重算输出。

12:31:18.3469875Z的CONTRACT5959B/SHA81deab3b468e7a16c21496467691f163dd1ae89bebac6623bde9a36c2224e78e，绑定本次source/run/attempt、全部43源、原request/launcher/workflow及两README。根逐一按本地实际文件字节比对43pins，均相等。真实docker id d25c020b838da118a587704e158c019f6434e6f84e282ae7baeda6a32d363873；host前后同一id，exit0，4CPU/16GiB内存与总swap、network none、完整源码只读、420s，三线程配置4及无凭据均已实际核对。

RUNTIME在导NumPy前真实观察OPENBLAS为1而OMP/MKL为4；恢复后三者均4，前后NumPy未加载、四个凭据键均不存在。其508B/SHA为b8fe46a2c1f4cd885f7a20952f8dcb0921ce66cd0b2bee4f567bb9f2c41b1926，PUBLIC中完整对象逐字相等。这是第二次实际观测，不倒填第一轮未打印的数值。

多链结果791B/SHA **951d375e5bcc8d9ab5566ae834e4fe084c7869aba01a579b5cf11e3d111b22ea**；完整checker stdout947B/SHA89721775f477a7fb56c0fdfe8e75ef319baf91ce26c9adeb74141cf641f1af9f。实际8个全图比较为4素域admission和4原二次域；三manual均实际链长0/3/2且保非零δ0尾。原非二项式结构常数[22,1]、判别式2的乘法及逆元确实返回。已构造ideal后的两次全X篡改及两个相同泛秩真子图均拒绝。

全图结果1549B/SHA **dc34cd358887462a990096c2bb15ecba227dbf83e857ccb689ccad410e01c60a**；完整stdout1697B/SHA885b0ca64e1a3eb2bf48fffc77ecffea33e80caf6b1593470ccabde6070b75d4。7个模型的14张原图全部比较，两互补射影长度均核对；一个真实二次π平方厚纤维通过，两截短厚度及两错误反图拒绝。结果明确original_rank306_geometry_executed=false。

PUBLIC9138B/SHA **29ae41a19547eb9c1838bd7837c6217228c0f69fd8e7797941e9e725b2c59096**，实际耗时9.166759972s；HOST953B/SHA **ad11e1e3d4841417b40e9233e8b7d204662985baa80ad1bb3ae3018357c2783f**。根按timestamp边界重组完整两checker字节及完整attach，独立重算六对RESULT/SHA；attach18588B/SHA **28bdb56e908569e8646b8439e582ae8804fd7c1c5990f63c1a7c02b4ba5396ae**与HOST相同。此项完成小软件验证；真实306原图及其所有下游仍待原生产证书，v17源和运行未改。
