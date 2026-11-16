# R901：五个原 I_Z 有界代表与共同翻转树实际认证

日期：2026-11-16。状态：原固定计划的126个新增完整翻转和五个原方向已经实际完成；原两个R890翻转直接复用。五个有界代表、原标记主函数、全部准确Galois下降表达式及原 $t$ 首项均已保存。本次不声称五个128/144空间、下降矩阵或高度已经完成。

## 1. 原运行与完成范围

数学依据沿 [R901 原共享树与主函数证明](R901-original-five-Z-shared-bounded-flip-DAG-and-marked-principals.md)，SHA256 83a18d8a4236567bbd3b0f76920f37de1ded1085b33bf4275507c039922125f2。固定计划 SHA256 为7d5300ec14bf83119768d6f41d44e940e5e073348d765538f154f51ddf69431a；计划中的零计数现在由本篇实际结果取代，原计划本身不改。

实际 [公开 run 43893483097](https://github.com/Rogerhu12/math-research-public/actions/runs/43893483097)，数学 job133390762003，源提交dbfb172d6cce083541a34ff507627dc42ddf9859，结果success/exit0。

|身份或实际计数|值|
|---|---|
|core SHA256|2cacb66f8b111746cdb8e51879f1c861e0aa59f0fb15d891c18c3c7c749fc920|
|wrapper SHA256|c2aad47b0af2a85e87f8fc8f955c879043d0c0de2c4046b530f5ee56444356d2|
|configuration SHA256|d2d5e37ccf73b5f0bc608357d61c215035dd7942e9641777696c97a5c657af90|
|新增完整翻转|126|
|直接复用原R890翻转|2|
|合计完整翻转|128|
|实际完整方向|1、2、3、4、5|
|实际保留的完成数学stage|3976|
|当前current数量|1|
|core receipt用时|6916.692942205001秒|
|FINAL内部用时|6916.692119684秒|

完整消费出口另核3156个不同的当前有效见证文件。126条已闭工作保留收据保存了旧中间工作压缩的准确清单：历史淘汰4284个中间stage，不改变当前有效见证、原函数来源树或完成计数。历史清单只约束其自身历史，不被误作当前必须仍存在的文件集合。

规则job133390643815在2026-11-16T15:10:22.721057+00:00真正pull main至c2359e514c58df71f6fa74012a62f3d6aad9471d。两README的SHA为6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9、35f82f3d96f1e07d1b7c3f0320398fdc0cd68d0c0e55ac17881c9f976299646d，无变化。规则读取提交与冻结数学源提交分别记录，不混为同一值。

## 2. 全部原输入和共享部分不重算

原辅助地方仍为 $\ell=1000000753$，原 $\sigma$ 分支次序为 $0,6,1,2,4,3,5$。输入按真实来源分组：

|原组|所选原文件数|
|---|---:|
|R827|15|
|R872|12|
|R883|10|
|R890|39|
|R896|32|
|R900|12|
|R902|157|

原五个恒等分支和三十个严格共轭的全部35个完整418空间及其标记主函数都绑定。R900的 $K$ 上定义代表和原 $Q_K$ 保持；不是将终末新除子或基误当作 $K$ 上固定。

原R890的两个完成对象为：

- R890-flip-04-D2-complete-flip-certificate.json.gz：4883字节，SHA256 c8008a9f419a518e6a1e7b91b89cde0a6f150ff16f373ce061751683b9595d23。
- R890-flip-05-E-complete-flip-certificate.json.gz：4953字节，SHA256 cdce3ef46d9c8c556fdf26a44997f51eb445976a363a4284870f1b9f18798313。

其完整累积函数 $F$ 一并原样复用。原 $W$、Krylov、正常纤维、局部jets、旧空间、三十严格共轭及上述两个翻转没有重新计算。

## 3. 原126树的真正数学出口

计算按原固定的12个 $\chi$ 节点、24个共享trace节点和每个方向18个节点推进。每一个新节点都已经给出完整正常418空间和其准确来源绑定的标记翻转，最后五个方向全部完成。只取最初两个右端不能满足本出口；实际消费者保全原完整基、原选行列、原锚和全部乘回。

原五个参数始终为

$$
(p_j)=(165,93,100,168,371),\qquad
(q_j)=(67,67,67,67,134).
\tag{901R.1}
$$

完整原标记函数保持

$$
Q_{Z_j}=F_j\bigl(NQ_j\bigr)^{q_j}Q_K^{-p_j}.
\tag{901R.2}
$$

这是原函数的正乘方向：$NQ_j$ 正幂、$Q_K$ 负幂，累积翻转 $F_j$ 的来源树不删。负 $\chi$ 次幂已经属于原 $Q_j$，不能再重复插入。原七重datum、下降和最后一次只取所需 $L$ 方向的规则均沿原证明。

实际证书的
actual_all_126_new_complete_normal418_spaces_certified、
actual_original_all_five_I_Z_bounded_representatives_certified、
actual_all_five_exact_Galois_descent_data_recorded、
actual_original_all_five_t_leading_coefficients_computed
均为true。准确下降datum是来源表达式；descent_matrices_or_K_fixed_bases_computed及terminal_divisors_or_bases_claimed_K_fixed仍为false。

每个方向仍是原 $I_{Z_j}$。没有将它改称真正实下降的立方理想 $\mathcal R_{\rm cal}I_{Z_j}^3$，也没有因有限域数组位于同一剩余域就改变原域定义。

## 4. 五个原端点阶与未缩放 t 帧

原 $P_0$ 参数为 $\rho_0$，$t=c\rho_0+\cdots$ 的同一个 $c$ 继续由R883提供。五个实际原 $Q_Z$ 阶为

|方向|$\operatorname{ord}_{\rho_0}Q_{Z_j}$|
|---|---:|
|1|−686|
|2|−182|
|3|−231|
|4|−707|
|5|−1659|

源标量没有归一为1。若某方向原 $\rho$ 首项为 $a\rho^m$，则其原 $t$ 首项为 $ac^{-m}t^m$；上表各负阶对应原 $c$ 的正幂。五个实际首项及完整来源DAG存于下列方向stage，后继必须直接消费，不能换成另一参数或只留阶而丢单位。

|原方向stage|字节|SHA256|
|---|---:|---|
|R901-j1-original-Z-marked-principal-and-descent.json.gz|16708|40ea717fb45d23a9da1db2c34dd56ce607911c9a7cfe7e51f7dd699aea65162d|
|R901-j2-original-Z-marked-principal-and-descent.json.gz|16552|c9458d173464f70b3911b12eca1076fa407db95bd1b8e0bf462f260c6462248e|
|R901-j3-original-Z-marked-principal-and-descent.json.gz|16483|fc79a00b9bd78021b15c28d15ea9df531649e1b8cda06ba58090258eb611f9fe|
|R901-j4-original-Z-marked-principal-and-descent.json.gz|16417|ddcf5aa2b3b655f2d07db68d90e7e49d087eccbef21cfcbd10cd4e6dd0da9940|
|R901-j5-original-Z-marked-principal-and-descent.json.gz|16421|4ab0d5d05f8259ce8f679890b435cbddd9d5853043750c8e1af6bea6613c5128|

各stage通过 source_complete_DZ_normal418 引用原完整终末空间。消费此引用及其manifest即可取真实418列，不能据文件名预填新基或下降矩阵。

## 5. 实际证书、manifest 与载体

|成员|字节|SHA256|
|---|---:|---|
|p41-original-five-Z-shared-bounded-flip-certificate.json|81141|69da20e9500254d8b63e6d8b3d2369bcefe8f9d4a43e4efe7db1a226a95c12f1|
|full-outputs-manifest.json|602364|e3e4eefd4a9b234bad8e8f837f115743c3bdbed5aa1cbafe9579f6f84da50538|
|full-outputs-manifest-reference.json|185|2477492d76acc70db8ca6c07e14cf73288d0be5a6687b55f66bef8ea920b559e|
|R901-retained-original-inputs.tar.gz|61682628|edf8e204cc996af08a87a99fa6e20b529911b7b3519cf7455f9f4d7c896f1de2|
|R901-original-source-inventory.json|111364|3e3c111386411e4e7cc8fc66ea8456671a84b91b7dd44d4bcc1f62a5afe948c0|

完整manifest实际有3987个entry。完成stage清单为
R901-stage-manifest-f5b9ee0bb6427da730d4693ab6f87ba2c1f09aa6121086cffccb448c1f889bb1.json.gz，
225749字节，SHA256 9a1f006173fbb06376b24cda896499c94b0e6d2bbebb1cbb1e50366836ef689c。

原一日artifact14251161202，名称serre-R901-five-Z-shared-flips-43893483097-1，
大小5906554358字节，平台archive digest
64304b92b1c478767627acea94e3e332e9414c19b5bc812416ef8289bccce5b4，
到期2026-11-17T17:20:01Z。

v26纯IO实际run43919701128/read job133483549799/source
bb74b6fd8ca8c06549466f047d0081e97776f96c只取8个所需原metadata，选件tar623644字节，
SHA256 fc5d599b525d1a22cbefc239648d3f40cd42000b8e4aebbeb2d4eee84a1bc529。
它给出上述真实manifest/reference和FINAL字段，不代全部原数学阶段；也未在外部重新下载并哈希5.9GB整个ZIP。新数学仅在原公开Actions中执行。

## 6. 立即接续的原缺口

R903现在可把真实五个418空间作为输入，按已证共享962像构造未加18阶条件的146/418空间，再得原128/400及原256前缀加144补。其原正乘为 $\Phi_j=Q_{Z_j}/q_\chi$，不另插 $\tau$；所需已成19行jets直接复用。R903的这些新空间、两图子式和标定仍须它自己的实际完成证书。

R907的五个无基点铅笔、九Hecke范数、$\operatorname{Nm}\Phi$、两端格与原帧继续接真实R903。七原连接的单独求值也不能代五个 $\sigma,c_Y$ 和主函数组合。活跃谱支持、原非 $p$ 项、Poincaré period、splitting和height仍未完成。绝对Serre一致性主目标保持OPEN。
