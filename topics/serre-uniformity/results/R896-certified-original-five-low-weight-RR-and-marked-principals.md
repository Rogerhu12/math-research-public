# R896：原五个和同态的完整低权 RR、有界272代表与标记主函数实际完成

日期：2026-11-16。会话：serre-public-astra-20261115。

**状态：五个方向均在本公开仓库Actions实际完成。** 从原R893完整初始空间，取得完整残余空间、完整146空间和完整418空间，并保存未缩放的原主函数及其ρ/t首项。这里没有完成原五个I_Z的128/144、Hecke支持、连接、period或统一高度。

## 1. 唯一后继来源与实际执行

规范来源是[run43872960726](https://github.com/Rogerhu12/math-research-public/actions/runs/43872960726)，数学job133318710623，source259e2448c7c51131fecc231ee55f7d457397dde8。core退出0，五项complete均为true，实际566个完整数学stage；FINAL内部计时324.5223999秒、core receipt总计时324.523172599秒。wrapper数学结束时间2026-11-16T13:15:04.687155+00:00，artifact随后保存。

冻结数学core为2328123121cb76e50d265222b19510e03ce22588b6bca367c1bd811dd623c1c2，
wrapper为558ad67f7b05662d7692060dcd7ea0742329c3fc85271a4be1e2b4155b2e9129，
方法为8c27bd771868bfa1ad5904c0887ff96226a009bd616674a7177744f05456d0bf。
数学configuration为0f52c636cacceaef9db290f15a492b05db188228680ae84997bb89d2d06d8782。

原辅助处仍是ℓ=1000000753，s=99932770、ζ=549966761、原整场生成元B=3197390。原曲线、level82整数尺度、两图、P0和原ρ均未改变。

首尝试43867022534只在R827 source JSON读取中KeyError，数学core未执行。原R827的result位于configuration内；修正这一严格schema读取后，原五输入和数学算法均未改变。其后的43868495711曾持续queued且0jobs，标准与force取消均返回409；同并发重排后先完成本规范run，而旧队列随后也启动并于13:20完成了一次重复执行。这个重复运行如实保留记录，不计为新增数学结论，不作为第二套后继来源，不再重派R896。下文全部bytes/SHA、选择与数值只来自先完成的43872960726。

## 2. 真正复用的原输入

只读447件原源：C0十件、R827十三件、R872八件、R880六件、R883六件、R890十二件、R893三百九十二件。完整producer、原configuration、manifest和逐成员hash保持原身份。

原R893的全部初始Schur、完整B核、全部B/yB纤维关系与原0至26节点Krylov源均直接复用。原R890七个normal V3整纤维、R880的252×690点矩阵、R872点泛函/qχ和R883原t帧也直接使用。本次只补确实缺少的normal V3节点7至26评价，未重算旧K、K逆、Hensel点jets或初始whole-Q单位。

详细原source绑定见R896-original-source-audit.json.gz，6136 bytes /
be12f4e3652b49a4e31aa82c51d9e7d79c7b5aab4a34292cc40944d950cb544b。
其c0极重数1直接沿R848真实切向及原局部模型；没有由模常数项为零单独推断准确消失。

## 3. 五个完整低权核

保持[R896原证明](R896-original-two-denominator-low-weight-residual-RR-kernels.md)的记号。原B0取原初始完整核的第0列，未经缩放；五个方向的实际B1整数参数都为1，最后146空间的第二锚整数参数也都为1。这些是本次实际接受的选择，后继严格共轭须逐项保留。

|j|n|原极度e|完整纤维N|两B真秩|残余空间维数|padding k|完整padding维数|末端完整维数|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1|12|2970|23|984|396|250|146|418|
|2|8|1674|15|1192|188|42|146|418|
|3|8|1800|15|1066|314|168|146|418|
|4|13|3024|25|1202|178|32|146|418|
|5|14|3339|27|1159|221|75|146|418|

各两B矩阵都为272N×1380，完整规范自由核及第二690行投影已保存。检查原全部6256、4080、4080、6800、7344行；两个原B截面的共同零恰为原E，未去掉剩余因子或重数。原N>n+3给真实乘积空间的全局注入，不使用无根据的V2n注入。

完整残余空间是H0(3H−F0)，其中F0=div_nH(B0)−E，五个F0度为294、502、376、512、469。旧0至k−1阶点约束的实际秩分别为250、42、168、32、75；完整核维数全为146。实际原v在恰第k阶的系数为单位，因此Dstd=div_3H(v)−F0−kP0有效、度272且避P0。

最后每个方向在同一原前七个完整272维Artin纤维中取得真rank962，完整1380列关系核与全部1904行乘回均通过，第二690行投影给完整H0(3H−Dstd)，690×418。没有把146维子空间冒称整个418空间。

全部十五个完整核证书都明确记：
所选单位子式可逆、两侧逆乘积正确、规范自由块为恒等、全部原行乘核为零。准确特征零空间由原源函数、已证几何秩上界与真实单位图定义；保存的有限域数组仍只是其约化，没有冒称已展开准确特征零全系数。

## 4. 原未缩放的标记值

以下表格均为同一辅助ℓ的实际约化，不能称作41单位或全部non-p处单位。

|j|A0(P0)|B0的ρ一阶|v的ρ^k系数|
|---:|---:|---:|---:|
|1|125409778|443088350|743188673|
|2|537146882|75114295|996882774|
|3|598807408|375796262|304284073|
|4|669550365|41358904|313193877|
|5|357859358|519148557|739078028|

五个B0的准确ρ阶均为1；准确零来自同一全局关系与原c0简单极来源，而非仅从模零推得。原v、B0与第二锚均不重缩到点值1。

用原qχ=uχ/τ²，div(qχ)=X−2H+272P0，保存
\[
G_j=\frac{B_{0,j}/\tau^{n_j}}{v_j/\tau^3},
\qquad Q_j=G_jq_\chi^{-(n_j-2)}.
\]
相应准确完整除子恒等式为
\[
\boxed{
 E_j-e_jP_0=(D_j^{\rm std}-H)
 +(n_j-2)(X-H)+\operatorname{div}Q_j .
}
\]
齐次式的τ^(3−n)在正常函数比中已经包含，不能再除一次τ幂。qχ在Q中是负幂。

实际uχ第272阶系数161046291和原t=cρ+O(ρ²)的c=354813668直接沿旧源。故
\[
\operatorname{LC}_\rho Q_j
  =\frac{(B_{0,j})_1}{(v_j)_{k_j}}u_{\chi,272}^{-(n_j-2)},
\qquad
\operatorname{LC}_t Q_j=\operatorname{LC}_\rho Q_j\,c^{e_j-1}.
\]
这里必须正乘原c幂，原t与ρ不是同一个参数。

|j|Q的ρ/t阶|ρ首项|c^(e−1)|t首项|
|---:|---:|---:|---:|---:|
|1|-2969|677819648|204902414|550087191|
|2|-1673|902547522|635297858|710093401|
|3|-1799|82653757|526890704|421229289|
|4|-3023|817240231|235653314|752602615|
|5|-3338|333363277|247069093|468031661|

每个标记文件保存整个全局主函数DAG、B0与v的原准确unit-solve、原E理想来源及qχ/t来源，而非只有上表首项。所有future Galois transport必须沿相同选行、主列、自由列、原整数参数和未缩放截面；本次还未计算六个新共轭。

## 5. 五个完整终点及正常空间身份

下表完整终点文件统一为R896-j{j}-complete-low-weight-RR-certificate.json.gz。

|j|bytes|SHA256|
|---:|---:|---|
|1|6671|86c051f4d7a1af96e90f4dbe5a2ebbbc9dc2be8617822587c728692fbb5ac2f2|
|2|6647|41d62ab6086e2d12fb6af7bce86f9aaad81a925128979c9ddda31ece476b7caf|
|3|6632|e08cca3ab6c30c647ffdc69bb8e916c72b94b97e44001125c55ff6bb2d3ce30f|
|4|6664|96f6b100ede5880bcefdbeec080269fc1e01ff314693d3efeb5c509d08271393|
|5|6665|7abcdd1593f95e0375b6814560f382e8627d839947d7c616889f3199b3f08345|

五个完整正常空间文件统一为R896-j{j}-bounded-pencil-trial-000001-complete-normal418-space.json.gz。

|j|bytes|SHA256|
|---:|---:|---|
|1|590190|b2609005ce42de2b4b66bf804565b10d9123c66f5bc2e085f4c7254f6c9bf2c2|
|2|589663|993f41214df6ed5a649e6e5136941417552f7e2d3958faa339f9d23086a1bb6e|
|3|589767|feebd0bd413075fc74c6cecd362ca120e6d148ebea2f20cd71afa0225b115aa6|
|4|589801|b64019b921d88d07fa35bfd9d195573aa343e2d5cbc98010f1027b4909a7c0d5|
|5|589995|e35804c8d07ca8df771aee35710ba19cbbc87f00b7c069c4f318eb01edc4a46e|

五个完整标记主函数文件统一为R896-j{j}-original-bounded-divisor-and-marked-principal-Q.json.gz。

|j|bytes|SHA256|
|---:|---:|---|
|1|7336|fb69ccce5d2a4eb4b09bf0ff79d7d3cad69cc45ab1ee710df45e77fb0e40b1b2|
|2|7330|36df5c3f5fff2042c67b7f84110e36422a3d4f5148ec1e8626f0870de65189f7|
|3|7318|38631f4072d97f77365bdd7c2ed1dd818fd1ef453ac01a69f6342ddb4e250720|
|4|7341|2485696058fe3b758e55c01a84d5504b1eebcc7b2a90f732b2a732066705145c|
|5|7344|b8d979169aa5c593a170f0ccf36658626541d5e7059ce9b39040db9e9912570b|

## 6. 原产物与后继必要闭包

|对象|bytes|SHA256|
|---|---:|---|
|p41-original-five-sum-Hom-low-weight-residual-RR-certificate.json|15429|66218771f4b0f8d7822282839ca94bcb34049fc3d867248ae4eddf6348fdb24c|
|full-outputs-manifest.json（577原项）|91794|2875d857feb3ae5c786b35946782b6a4cf74d429679c5d54d3dc1c3215755a93|
|R896-original-source-inventory.json|212089|84f6307355a80b35ca5e3c53ed4ea97fbebf41b7720702ae59339c5a3e1d425a|
|R896-retained-original-inputs.tar.gz|172702868|fa44f406550d22a5796c9be6c7322d3332f757221f5c415b1d59b892d4df92fd|

原artifact14228364447名serre-global-R896-five-sum-Hom-low-weight-RR-43872960726-1，525499323 bytes /
09709b33882b32bab65b1ff855e7cd246561cac8ba344251bcab26e3067634bd，到期2026-11-17T13:15:52Z。

为R902和R901实际消费者，run43875866536只读取271个必要原成员：五完整终点、标记pair、B1整数选择、完整低权规范核和投影、padding146、v/w、五418、五Q及已成normal节点7至26。旧大逆保原manifest引用，不重复下载；旧产品扫描不携带。本次IO没有执行新矩阵。

必要tar为45605987 bytes /
7429a99c1997a29a00b3c63909e2bedb8dcf30ff3b3e22419bf1bde2cd3e81c9。
运输artifact14230107731为46773192 bytes /
765ad23b67ca58198c87f38a9487132e74938510884c13b9217315eaecaf47b7，
到期2026-11-17T13:30:12Z。root读完原complete/source字段、真实所有秩及principal首项，并实际哈希该小ZIP及其文件；没有重算任何原算术。

## 7. 原课题的准确出口

这五个完成终点可直接供R902固定六σ单位图和R901原共享树。原R893初始RR已经完成，本篇只登记其后新的低权完整空间，不把两者重新合算一次。

原I_Z的128/144与两图基、Q下降、P1帧值、原Hecke活跃投影与torsion清除、Picard支持、完整non-p、连接、校准period及统一高度仍未完成。R903已给连接到原128空间的正主因子和共用乘积像接口，须等待实际R901终点后执行。固定层41的这些完成输入不构成绝对Serre一致性的证明。

原证明与算法：[R896纸证](R896-original-two-denominator-low-weight-residual-RR-kernels.md)、[R896方法](../notes/R896-original-five-sum-Hom-low-weight-RR-consumer-method.md)、[R893真实初始RR](R893-certified-original-five-sum-Hom-complete-initial-RR.md)、[R872原点和固定χ](R872-certified-original-P0-jets-and-fixed-Picard-spaces.md)、[R883原t帧](R883-certified-original-t-first-order-frame.md)。
