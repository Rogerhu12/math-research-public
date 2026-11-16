# R879：原参考254阶单极函数与无基点铅笔实际完成

日期：2026-11-16 UTC。会话：serre-public-astra-20261115。状态：原参考线丛M0=O_Y(254P0)的源绑定单极函数v0和无基点铅笔(1,v0)已经实际认证。未重构全部特征零系数，原t框架常数尚未展开；五个原Lj的截面、九范数、Picard支持和高度仍未完成。

## 1. 实际运行和冻结来源

公开Actions **run43835253379** / **job133190260738** / source commit
**0f74fb43a6eba2646e34b2950f5de1131470fe29** 成功。原数学core返回0，
**4个完整stage**，core receipt计时 **1.2987670320000007秒**，
最终证书scope计时1.2984929559999898秒；不存在外层timeout或失败伪装。

核心 `R879_original_reference_pole254_function.py`：
31135 bytes / SHA256 **a8573c2a0dfd830cd3cd41dda0858fa108dbcfe0e0fc1ad1d4f78a1b95a2bf33**。
wrapper：
33380 bytes / SHA256 **2703bec3094e8050f1830dca5be02c10df504252ebef1a53f08ab796e3a8fd35**。
实际请求4893 bytes / SHA256 **87535212d2b4822349791bdd9b2c6793a0b0a1ef513bfb58c09ad52ed6f043ad**。
数学configuration SHA256 **5a992444cb39749f5c3f85cbd7ccf1f0cd178ef332bc07dd6c0b10b78f367ff4**。

完整几何论证见[参考函数证明](R879-original-reference-pole254-pencil-from-completed-syzygies.md)，
执行字段和准确系数语义见[方法](../notes/R879-original-reference-pole254-function-method.md)。

唯一原数学producer是R872 run43830071469/sourcea07453ec81e832b0aeef99bded2efaa763adaf13。
本次直接保18件必要原文件；它们的原配置、字节和SHA均已读取核对，
selected-file fingerprint为 **27f3477cac1136888c054803305bb88f8d4692026dd034002070194140c2ed92**。
没有下载原122MB完整carrier，没有重新执行旧点jets、146/418核、乘积或逆。
未再次读取的大依赖仍明确是已经认证的外部准确unit-solve叶，不声称本次全部重新哈希。

## 2. 新系统与实际完成结果

原R872准确配对基满足

$$
uT(c)+bS(c)=0,\qquad S,T:K^{418}\longrightarrow V_3,
$$

且原u、b共同零除子为272P0，u在P0恰消失272阶。
在原normal基上，S和T各抽取272个最高z次项，使两者同属原τV2。
这544个条件的完整核准确同构于H0(272P0)，映射为c到f/u，
其中S(c)=τf、T(c)=τg。

直接复用原V2局部系数矩阵，将f在原局部参数ρ的第0至17阶设为0、第18阶设为1，
形成唯一新的 **563×418** 非齐次系统。原证明给准确秩291、相容性；
实际素数 **1000000753**、原ζ根 **549966761** 下的秩确为 **291**。

本次保存291阶单位子式、两侧逆乘回、规范自由零解以及**全部563行乘回**。
准确特征零解仍定义为原所选单位方阵作用于原右端的唯一解，
不将有限域整数代表冒称已重构的准确系数。两个新V2向量f、g由已成S/T线性组合得到，
原完整全局关系ug+bf=0随准确基线性继承，不重新展开旧乘法。

因此准确原函数

$$
v_0=f/u=-g/b
$$

在P0外无极点，而在P0有

$$
v_0=U_{272}^{-1}\rho^{-254}(1+O(\rho)),
\qquad U_{272}=[\rho^{272}](u/\tau^2)\ne0.
$$

这证明的是**极除子恰为254P0**，不只是上界。
实际证书明确给actual_reference_function_pole_order=254、
actual_reference_pole254_function_certified=true。

## 3. 直接取得原参考铅笔

在M0=O_Y(254P0)中，1在P0外处处非零，v0在P0的纤维非零。
故

$$
(1,v_0)\text{ 全局生成 }M_0.
$$

实际证书actual_reference_basepoint_free_pencil_certified=true。
这已经满足[R876九范数定理](R876-original-nine-norm-generators-and-rigidified-Hecke-ideals.md)
的参考无基点输入；无需再构造参考128基或重复参考672阶铅笔检验。

这个函数是在原K=Q(ζ)上的准确源绑定函数。没有声称它单独在Q上定义；
原参考线丛和其完整生成理想仍按忠实平坦下降识别，原−3下降不改。

原t=a³框架继续保留。如果t=cρ+O(ρ²)，则其在原t^-254框架下的P0值为

$$
c^{254}/U_{272}.
$$

本次没有展开这个常数，也没有把c或U272设为1。相应旗标
original_t_frame_scalar_expanded=false。该表达式需在后续真实刚性化和nonp处理中继续传递。

## 4. 实际输出和必要续载

单日artifact **14210388032**，名称
`serre-global-R879-reference-pole254-43835253379-1`，
**6787421 bytes**，ZIP SHA256
**4b1d3a03d861049f614aaad98d9065b64e82050a11cecf1bc891ab5bbbe10100**，
到期2026-11-17 08:56:14 UTC。完整manifest有15项。

|实际输出|bytes|SHA256|
|---|---:|---|
|完整manifest|2190|dff31b60a5b711b5f9c9337a04d9e637d742ae225ac97b5f66cf9cc20acfb3f3|
|最终证书|7379|bf7172a28ad7efa883b9039ecb6767281e6130885591bd51e52db621b6648bab|
|563×418完整系统|815344|dd374af4e8898a00907d633d86bfceb1967eecc7d5d58bb060b5a710b3055e8c|
|291单位解与完整回代|333109|3ae79b8be03b1d3c6029aebbc55bb4ae1a4eb64897b4474985cca6edbd7fcc81|
|原函数与参考铅笔|14159|bfc553e539371229fc668531030ca6c8327091d2105c00f743427ed09b8a2556|
|原源审计|2564|0a3be3f7e1b4ae505765b825e6d79609c954509f13ac10053cf575bddfdf00cb|
|四stage清单|2612|38a2ad767f58bc5d98e69606f43edb843f4681617955924405746263b41e3502|
|必要18件R872原carrier|5578772|cc4d4c47325c68cadabbbe41fe85339bab9f389dbd2d11578e409d70b734a743|
|core receipt|606|6e2e0ff56e5977d6532c4605d60a1e626d2e61834178e9bcc1b956d819e2d1bb|

同一个公开数学job的标准库步骤已核全部输出字节及真实源身份。
随后纯IO **run43835655251** / **job133191584030** / source
**ee708f967482071b25147190309ec616b82c382c** 读取实际证书和必要小元数据；
根没有声称另行重哈希整个ZIP。
八件原小文件加manifest/reference的小tar为11853 bytes，
SHA256 **8e566d58f9889aae589a75625c2be7b76c7373f39e3d4e2568655073e944418c**。
后继需要f、g或旧S/T实际数组时应消费完整原manifest所指的真实字节，
不以这个小tar代替未读数学叶。

## 5. 立即可用的范围

R876的参考输入现可直接用(1,v0)。
原R873循环7对应目前在另一个合法辅助素数739上保存了实际模坐标；
若在1000000753合并计算，须将其准确已成范数来源合法约化到同一素点，
不能把两处模数组直接拼接。相关新运输只应重做新素点必须的新算术，
原准确Berkowitz范数、旧q尾和已成参考系统不重做。

五个原Mj的128截面、九个域范数、真实Picard作用、活跃η支持、主函数校准、
原t帧常数展开、Poincare period、nonp项和高度均未由本结果宣称完成。
所有新数学和机器数组只在公开Actions与当前必要的单日artifact内；
Git记录证明、源身份和以上精确索引。
