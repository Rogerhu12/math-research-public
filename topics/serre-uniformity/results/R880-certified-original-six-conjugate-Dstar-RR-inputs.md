# R880：原六个非零 Galois 共轭 D* 空间及七项主函数输入的实际认证

日期：2026-11-16。会话：serre-public-astra-20261115。

**状态：本项实际完成。** 六个非零原Galois共轭的完整418维空间均已计算，与先前完成的第零分支合成七个原D*输入。每条截面和单位解沿原第零分支的固定选择共轭，未另选线性等价的替代代表。

实际公开 [run43857317518](https://github.com/Rogerhu12/math-research-public/actions/runs/43857317518)，compute job133264906689，source4478c31d1d601784fb636224adcf90e3fc0978ad；于2026-11-16T11:29:58.050392+00:00结束。core receipt记录351.08276171599994秒、exit0，1093个完成数学阶段，230件原输入。最终证书的六个新空间及七个总输入标志均为true。以下模值全在辅助素点1000000753；不将其单位性质冒认为41处单位。

## 1. 原对象与实际完成范围

沿[六共轭纸证](../notes/R880-original-six-conjugate-bounded-Dstar-spaces.md)、[执行方法](../notes/R880-original-six-conjugate-Dstar-RR-execution-method.md)及[R887原共同尖点输入](R887-certified-original-common-cusp-flip-and-bounded-RR-inputs.md)，设
\[
D_j^*=\sigma^jD^*,\quad W_j=H^0(Y,3H-D_j^*),\quad j=0,\ldots,6.
\]
每个 \(D_j^*\) 有效、次数272、避开原 \(P_0\)，故 \(\dim W_j=418\)。本次实际生成j=1至6的正常V3坐标，同时保留原V3坐标及两者转换来源；原j=0的418基直接复用。

保持原 \(a_j=\sigma^ja\)、\(b_j=\sigma^jb\)、\(v_j=\sigma^jv\)、原选行/主列/自由坐标、v的原核列与成功trial1的w。实际每条分支均验证这些同一索引所需子式仍为单位。准确对象是原有理单位解表达式的Galois像；本次给出其指定剩余嵌入值和全部关系证书，没有宣称展开所有特征零坐标。

第零分支、原S5乘积、正常转换、原Krylov零阶逆、原P0 jets及共同 \(C^*,D_\chi\) 均未重算。七原A/B已在[R880七输入认证](R880-certified-original-seven-Galois-normal-inputs.md)完成，此次只接缺失的六条有界RR链。

## 2. 实际 Galois 顺序与未缩放首项

原根 \(s=99932770\)、\(\zeta=549966761\) 不变。原σ幂0至6对应分支
\[
(0,6,1,2,4,3,5).
\]
文件basename的branch-XX是原分支编号，**并不是σ幂**。下表 \(a_{j,0}\) 为 \(a_j/\tau^3\) 的原值，\(v_{j,123}\) 为 \(v_j/\tau^3\) 的原第123阶，\(\lambda_j\) 为以下主函数的原ρ首项。

|σ幂j|原branch|原B根|a(j,0)|v(j,123)|λj|
|---:|---:|---:|---:|---:|---:|
|1|6|966983841|792820931|65136445|898059288|
|2|1|302421514|141274031|191859949|485743235|
|3|2|527703815|938759787|123285289|780625072|
|4|4|691312857|297709639|271595126|410744390|
|5|3|587546695|172503180|640507606|648540123|
|6|5|920744568|742081719|453154374|364496843|

首项直接来自完成的principal阶段。共同原值
\[
u_{C,252}=207667877,\qquad u_{\chi,272}=161046291
\]
沿原输入保持。第零分支 \(\lambda_0=267133051\) 仍是旧R887值，本次未重新求它。

准确主函数及逐除子恒等式为
\[
\widetilde Q_j
 =\left(\frac{a_j/\tau^3}{v_j/\tau^3}\right)^3
   \frac{u_C/\tau^2}{(u_\chi/\tau^2)^4},
\tag{880.6D.1}
\]
\[
E_{\sigma^jf}-1206P_0
 =-(C^*-H)+3(D_j^*-H)+4(D_\chi-H)
   +\operatorname{div}\widetilde Q_j.
\tag{880.6D.2}
\]
principal因子取正方向。每条实际ρ阶为−1205，且
\[
\widetilde Q_j=\lambda_j\rho^{-1205}(1+O(\rho)),\qquad
\lambda_j=(a_{j,0}/v_{j,123})^3u_{C,252}u_{\chi,272}^{-4}.
\]
本producer未消费R883的t首项，其original_t_frame_value_computed=false必须保留。真实下游接入 \(t=c\rho+O(\rho^2)\) 时，t首项为 \(\lambda_jc^{1205}\)，正乘该幂；不得把上表改名为t首项，或把原标量缩为1。

## 3. 六条完整 RR 链

原G与Γ短多项式各读17个16行块，覆盖全部272行。旧纸证一处“每个16块”的计数笔误已在[R894 §9](R894-original-seven-conjugate-pole-trace-and-bounded-descent.md)更正；实际冻结core/request使用17块，未按笔误执行。

五个旧节点0至4及K、K逆零阶直接复用。只生成必要正阶K/逆jets，使用多重度 \((3,3,2,2,2)\) 的12条件Hasse逆恢复完整短多项式。F0/F1/F2的加权次数界5/7/9及条目次数界7/9/11保留；第一σ层准确为
\[
\sigma_1=zF_1-(5+\epsilon_{\rm col})GF_0.
\]
仅消费原20列 \(\{0,73,\ldots,91\}\)，不换primitive、free1186或规范。

每个新分支实际完成以下既定关系链：

1. 原T11的2866行、2451选列及固定单位子式，给完整415维商；原双铅笔830×1234矩阵再给T5完整415维商。
2. 原830×690的D约束取准确395主元图、全部关系与自由坐标恒等，给完整295维D空间。a取原第一列，b取原295列指定和。
3. 原五纤维1360×1380关系矩阵使用原1111单位图，第二块投影给完整269维残余F空间。完整性使用已证全局维数上界与原关系图；不额外声称五纤维对整个V6单射。
4. 原P0的123条件及同一核图给146维标准化空间，v沿原选列，其第123阶为上表实际非零值。
5. 原v和trial1的w形成实际962单位图，保存全部关系和第二投影，取得完整418；原未缩放w及成功trial保留。

所有原图在六条新剩余嵌入实际满足单位条件，每一级保存完整剩余关系。特征零身份来自全局维数证明和同一准确unit-solve表达式；未把新模筛选定义的新基冒称σ共轭。

## 4. 六个完整418与完整出口

418文件统一名为R880-six-Dstar-branch-XX-Dstar-projected-original-V3-basis.json.gz，每件含original_V3_basis_mod_prime和normal_V3_basis_mod_prime；对应完整关系核及所有来源由同分支完整出口绑定。

|σ幂j|文件XX|字节|SHA-256|
|---:|---:|---:|---|
|1|06|1794281|062ba764c6e8be8270502ce16b14f7a3d9356547507b8882c0760659c7166af0|
|2|01|1794504|cc1e14b720f51d94cfb81e4063ebcb670821819b998dc9ae37787a1deb9a2990|
|3|02|1794539|5ecb6e26b14170131600dde5a36b53738a7b6367e5d71f3f6e77fc918255991f|
|4|04|1794232|c1880eef9fb60c45b7d0e8428b665c0c168220cefb16fd3ffdbf28749b404be8|
|5|03|1794011|10ac32f7e5137052ddc47a87fdb31d0d43767033a66430c2474843238d3b55bd|
|6|05|1794649|2d488ca49c572c5ff84609d5f6184e83d0b07392efdb01c456f444a8d55eb7fa|

完整出口统一名为R880-six-Dstar-branch-XX-complete-Dstar-input.json.gz，XX仍按上表：

|σ幂j|字节|SHA-256|
|---:|---:|---|
|1|7190|92c7d6d6f919c05f2a32be08cbd7ddb3e7d1680e98e95feb2e5bbf50e80e87fb|
|2|7181|d57351940883c15e79bddec64a1911624073953400d466591f142fb6e73d273d|
|3|7186|73953cd744256bf26668bd6c1d297ca42f61b11320808fe3c9f21641f4d8909f|
|4|7176|af7734e0eefd33ecf9ad5d742af74b76d7101ccdfc3bc2049c91da65f53bf1dd|
|5|7207|6e7965ff59da92167741f658fb82c247da5c8dc0087a77c99c3515000c7f4459|
|6|7188|3979016fff1d05bce6b38518c4a846943b9b2903d91b67c972723722a04853e3|

出口还绑定原a/b、v、w、T11/T5完整商、295核、269残余、146空间、962关系核、F0/F1/F2/σ1多项式索引及principal DAG。后继按原manifest读取所需闭包，不把表中hash当成已取得完整原bytes。

## 5. 已成 B 导数直接接 R893

六条B的 \(\delta B,\delta^2B\) 是已经生成F1/F2的原第一列，额外保存为正常坐标多项式向量，两个矩阵均为8×272；没有为后继重算ΓB或Γ²B。

文件统一名为R880-six-Dstar-branch-XX-original-B-derivative-vectors.json.gz：

|σ幂j|文件XX|字节|SHA-256|
|---:|---:|---:|---|
|1|06|28077|d4196840d07a5439b6146461e44a7d817f0424032ce9eaf050a348d31080684a|
|2|01|28081|75fb876a17237d0e48559648b36bc53dea7a6972b7b706f49672d7752bab85c7|
|3|02|28040|91ba89b0f040ace1d04dd13ee5ff9ce6ddf03909e289def567dc8b59867cc3af|
|4|04|28087|1f35720056ce7edf137d228853ce799bb8ed8261d45cfc42fc449991075438ba|
|5|03|28106|5c6ec61a44594ac4ae95e1fa081da25f1ee9cbde59a37b4ee1762b69fd00ec5d|
|6|05|28070|0f82127f14dcd4c4d4c9cdecb196b7d5d4e2c140d78322f61cc415867fa92144|

R893五和需要σ幂1至5时按branch6/1/2/4/3读取；第零B导数沿旧原来源运输。不得按文件自然序误接原Hom标签。

## 6. 源码、最终证书和实际转移

入口为[冻结核心](../scripts/R880_original_six_conjugate_Dstar_RR_inputs.py)、[公开包装器](../scripts/R880_public_original_six_conjugate_Dstar_RR_inputs.py)、[原请求](../notes/R880-six-conjugate-Dstar-public-request.json)。方法及数学配置均在开算前固定。

|项目|字节|SHA-256|
|---|---:|---|
|core|77259|5421c814130021587ac0a97b8fa336b04c5d0d4f784a96cbac4088591b86fb17|
|wrapper|47603|9c2fac9d342b274bf3570af34237c5138738869165a46c66a7627db910208cab|
|方法|9537|09715130e506c4696c1dad736d56062a3a409ede0f1a1b4d040c2effd0257142|
|请求|35313|ff2bdbdfc4ac38ed19cb98cc5e8d8634723da918bb18a64ce0caee27c8420408|
|最终数学证书|17314|3e48e09c24aee9d9912eb1ad79f17421fb797440942c44376dda55574409d1cb|
|来源与固定图审计|11120|7d95dbdc1adcbad2bf47b599d8e8573dea6f8fdfa2c76989460ffd5a8e83e9fb|
|1093阶段manifest|64700|35dbd0af047d41196b74a4a28f522be14ebbde3b8eba30b63cb6b3fb482d3445|
|全输出manifest，1118项|205572|462bd2c6851e7f49e67327c1ab7cf7eae08ca37dcfa65151dafded2ec65f9d2d|
|共享12条件Hasse逆|6838|015a6bc146779012ff575e6d9d59e7c90cb15dccb62b2bb1f5522a3d40180a67|
|core receipt|594|0c12a679bc29c832f6ae191cb87c7d874b0a2c98a833a568a471b6faec60b159|
|run receipt|535|58a0c704672200a9fe89f3ee03e3cbad672bf31c0ccb570ac1570b11bce31bd1|

配置指纹28724072022fdabfe5ad1178e93893ad3b97e5eeed29ee1abb6b5a5433acaa78。
原一日artifact14222091280，名称serre-R880-six-conjugate-Dstar-RR-inputs-43857317518-1，
889731055B / 0763bf87fda063082d2027199eb7b2d08a56e647d764444017e161735645e923，
到期2026-11-17T11:29:59Z。全部新数学仅在本公开仓库Actions执行。

根会话经只读IO [run43859441027](https://github.com/Rogerhu12/math-research-public/actions/runs/43859441027)，job133272180357，source1b6f96f41f1e9fe3500b3b4a85b5d529305457bb，读42个当前必需成员及原全manifest/reference。实际30次Range共11986323B，每个所选成员均按原bytes/SHA绑定；未重下载或声称重哈希整889MB ZIP，未重跑数学。

必要原输入tar为11334333B / 4a25c55affa1674bf1ec101da0333cdbcac371e793830ff3dabaefa7ecbee6e4；
其一日artifact14222183067共11650857B / 669f4e154611c40f0dc59629ac7789ae7cd6d778889819fdefb2cf2b30f98211，
到期2026-11-17T11:38:19Z。R893/R894直接消费这些原件；raw不进Git或Release。

## 7. 接续边界

[R894](R894-original-seven-conjugate-pole-trace-and-bounded-descent.md)所需七个D*418及七项原 \(\widetilde Q_j\) 现已具备，可直接做原七极除子trace的有界聚合与准确下降datum。trace按原常数域Galois计算，不改称Hecke范数。R890已成D2/E节点可在核对完整原来源后复用。

本项没有计算实际七项聚合、K固定下降基、另六个Ef的八flip、五原Lj的128/144空间、Poincaré连接、eη/d/N、非p项、周期或高度。t首项由真实下游R883输入消费。主目标继续OPEN。
