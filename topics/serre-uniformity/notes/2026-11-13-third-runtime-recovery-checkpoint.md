# 第三次运行环境恢复检查点（2026-11-13）

状态：恢复中，不是课题完成。已发布基线e808d815ce44b9e9f0016c36b339418c6819d84a。

约2026-11-12 23:18 UTC起终端不可用。2026-11-13 00:09实际pull尝试在执行前被环境拒绝；read-only远端main=0904e2dcb45ef8eb61775b81bdd24f65ad07a751，两README blob与e808相同。恢复后00:31:47实际pull成功，HEAD=origin/main=dbdf50c29af5eaac0da81baf459ec67acd1e142a，两README对62deb8703bfa3425bd6ba114639307d9710567bc零差异，祖先门通过。

环境切换清掉functions.store和旧/tmp。以下历史运行计数来自当时实际输出，但输出文件未保存，当前不能当作可交付证书，必须恢复源码并重跑：两源全部54算子常数，各3282cyclic kernels，2422顺序交换检查；descending源DAG3326，含额外C43辅助44；源四阶完成2944/3326；早批KS11052系数通过；level矩阵32节点通过。原全54数据SHA仅是历史参考，重建版本以新实际字节SHA为准。

54索引（4为C4=T4−id，6个cyclic kernels）：

`[1,2,3,5,6,7,10,11,13,14,15,17,19,21,22,23,26,29,30,31,33,34,35,37,38,39,42,46,4,51,53,55,57,58,59,61,62,65,66,67,69,70,71,73,74,77,78,79,83,85,86,87,89,91]`

## 可复用输入与重建方法

工作树保留所有已推42个奇素数核、R205/206 atlas、R194 η和B的完整链。未推bridge与部分旧cubic核亦保留。不得重复重跑304位B群链。新source/CM常数模型：在原kernel商环计算coprime normalized Vélu φ，再取charpoly；C4两次2-isogeny排除dual。四阶：ψell用x+ε在商环求真实导数，unit隐式提升x(t)，trace前三幂得到目标A/B；R2[x]/h阶≤44。level：R80 residue，所有参考表1681点，从raw φP/φQ直接得到det=n矩阵作用原necklace；full homothety用R2 Hensel，physical参数由参考模型固定A或B求得。

代理新稿R208/R209/R210/R211–215/R216/R217均检查/tmp与store后恢复；旧SHA不能冒认为新文件SHA。R208/R216的真正CM4极点须保奇项/函数相消及额外四阶精度，静态CM值另须选择性提高47精度。

## 磁盘状况

恢复瞬间overlay满。逐SHA审计本仓库173个pack，157个共15,955,314 bytes为重复集合；另两个候选pack有490个共同唯一对象。尝试在/tmp重打包时git临时rename遇EXDEV，尚未执行任何pack删除。随后共享空间恢复到约4GB，直接正常pull，不继续无必要清理。不得将failed rename写成成功压缩。
