# R903 实证：五个原 I_Z 的完整 128/400 两权空间、144 补列和 272 维两图格

日期：2026-11-16。状态：**原公开 Actions 消费者已经实际成功，五个方向全部完成。** 本文登记实际结果，不重算旧来源，也不把辅助素点数组改称已展开的特征零系数。

## 1. 已完成的准确出口

原问题仍是 \(p=41\)，本次有限矩阵在原辅助素点
\[
 \ell=1000000753,\qquad \zeta=549966761,\qquad s=99932770
\]
执行。保持原曲线 \(Y\)、\(g=127\)、\(\deg H=272\)、原点 \(P_0\)、原 \(\rho\) 与 \(t\)，以及 R849 的五个
\[
 \mathscr L_j=I_{Z_j},\qquad
 \mathscr M_j=I_{Z_j}(254P_0).
 \tag{903R.1}
\]
消费的原 \(Z_j\)、\(p_j/q_j\)、五个标记主函数和全部常数域共轭均没有更换。

[实际 run 43921416613](https://github.com/Rogerhu12/math-research-public/actions/runs/43921416613) 的 compute job 133489524133 已完成，计算步骤和标准库来源／输出核验步骤均为 success。实际 core 给五个完整方向、136 个保留完整数学阶段；FINAL 的五组完成标志全部为 true：

|原方向 \(j\)|\(H^0(\mathscr M_j)\)|\(H^0(\mathscr M_j(H))\)|权1实际补列|完整两图格秩|原 \(P_0\) 帧|
|---|---:|---:|---:|---:|---|
|1|128|400|144|272|已认证|
|2|128|400|144|272|已认证|
|3|128|400|144|272|已认证|
|4|128|400|144|272|已认证|
|5|128|400|144|272|已认证|

此处的144是完整400空间中补原两组128列所得的指定补列。它不是另一个 \(H^0(I_Z(270P_0))\)。

数学结论使用[原 R903 证明](R903-original-five-Iz-shared-product-two-weight-RR-and-marked-frame.md)的特征零包含、几何维数上界、同一次数两图丛和本次实际单位子式。每个准确核仍由原矩阵、实际选行列及自由恒等列的 unit-solve 表达式定义。实际模数组是这些原准确对象的合法约化；FINAL 明确保留
\[
 \texttt{characteristic\_zero\_RR\_coefficients\_reconstructed=false}.
\]

## 2. 原主因子的方向与正常坐标

真实完成的 R901 给每个 \(j\)
\[
 Z_j=D_j-H+\operatorname{div}(Q^Z_j),\qquad
 W_{D_j}=H^0(3H-D_j),\quad \dim W_{D_j}=418.
 \tag{903R.2}
\]
原 R872 给 \(X=D_\chi\) 和未经重缩放的 \(q_\chi\)：
\[
 \operatorname{div}(q_\chi)=X-2H+272P_0.
 \tag{903R.3}
\]
本次实际采用的同一个全局函数为
\[
 \Phi_j=\frac{Q^Z_j}{q_\chi}.
\]
它正乘给
\[
 \mathcal O(3H-D_j-X-18P_0)
 \xrightarrow{\ \cdot\Phi_j\ }I_{Z_j}(254P_0),
 \tag{903R.4}
\]
以及两边同扭 \(H\) 的同构。原 \(Z_j\) 在 \(P_0\) 外的负支撑继续保留。

原正常坐标顺序仍为
\[
 \mathcal V_m=\{z^k\beta_i:0\le k\le m-\epsilon_i\},\qquad
 \epsilon=(0,1^{144},2^{127}),
\]
先正常行、后幂次。这里已经包含原除以 \(\tau^m\) 的函数表示。本次没有再除一次 \(\tau\)，没有再乘一次82尺度。

最终128数组以 \(690\times128\) 正常矩阵给出，最终400数组以 \(962\times400\) 给出。每个数组同时保留准确 unit-solve 来源、完整正常行及自由恒等行。它们本身尚未乘 \(\Phi_j\)；原目标函数由同一标记嵌入阶段正乘完整 \(\Phi_j\) 才得到。

## 3. 实际执行的完整核和两图证书

每个方向只新增一次父对 \(W_{D_j},W_X\) 的完整962维乘积像，使用原七个完整272维纤维及全部因子、重数。原 \(W,K,K^{-1}\)、旧正常 \(V_3\) 纤维和原 Hensel jets 没有重算。

实际保留原乘积列身份、全部1904评价行、962选行、完整逆及乘回。该同一商同时截出
\[
 U_3=H^0(3H-D_j-X),\quad \dim U_3=146,\qquad
 U_4=H^0(4H-D_j-X),\quad \dim U_4=418.
\]
两个两锚矩阵分别为 \(1884\times690\)、\(1884\times962\)，使用原 \(\tau,\sigma\) 的三次／二次锚。完整544阶单位图和全部原行关系确定准确完整核。

在两个空间上分别施加原阶0至17的18行。它们来自 R880 已成252行矩阵，而非新算点展开。权4仅按原 \(z=z(P_0)+\rho\) 补缺少的最高幂列。两个真18阶核给128、400；阶18保作原首项数据。

权1的固定前256列是同一128基及其原 \(z\) 倍。实际补出的144列保留完整400空间的原列身份；全400单位图、双侧乘回及全部正常行关系均为完成证书的一部分。最后实际272维完整纤维子式认证
\[
 \mathcal O^{128}\oplus\mathcal O(-1)^{144}
 \simeq \pi_*\mathcal O(3H-D_j-X-18P_0).
 \tag{903R.5}
\]
正乘完整 \(\Phi_j\) 后，原 \(\tau\) 图基为 \([\Phi_j a_i,\Phi_j b_\ell]\)，原 \(\sigma\) 图为 \([\Phi_j a_i,\Phi_j b_\ell/z]\)。完整两权 membership、实际子式及两边同次数共同给两图格；未将单个点的数值代替整个272维纤维。

各方向完成后才作闭合工作压缩。被删除的扫描项进入历史 receipt，准确原乘积列、完整选中评价、逆和所有仍被引用的 unit-solve 叶均保留。实际 verifier 确认全部 live 引用及原 \(Q_Z\) 来源存在且 SHA 相符。

## 4. 原 \(P_0\) 首项已经保留的内容

对每个方向，取实际128基中第18阶为单位的第一个原列，保持该列未缩放。设
\[
 Q^Z_j=L_{\rho,j}\rho^{m_j}(1+O(\rho)),\quad
 q_\chi=u_{\chi,272}\rho^{272}(1+O(\rho)),\quad
 a=a_{18}\rho^{18}+O(\rho^{19}),
\]
其中原
\[
 (m_1,m_2,m_3,m_4,m_5)=(-686,-182,-231,-707,-1659).
\]
实际标记阶段保留
\[
 \operatorname{ord}_{P_0}(\Phi_j a)=m_j-254,\qquad
 \operatorname{LC}_{\rho}(\Phi_j a)=\frac{L_{\rho,j}a_{18}}{u_{\chi,272}}.
\]
原 R883 的 \(t=c\rho+O(\rho^2)\) 使用同一准确 \(c\) 来源；相对于原 \(t^{m_j-254}\) 帧，系数是
\[
 \boxed{\ \frac{L_{\rho,j}a_{18}}{u_{\chi,272}}c^{254-m_j}\ }.
 \tag{903R.6}
\]
正幂方向未换，原标量没有重缩成1。实际五个阶段保存其准确表达式和本辅助素点的数值；FINAL 的
\(\texttt{actual\_all\_five\_original\_P0\_frame\_coefficients\_certified}\)
为 true。

本文以完成证书及其原引用登记这些数值，不另行计算或补写未经取回的标量。原 \(P_1\) 同一全局截面的数值、K/Q固定基与两端范数标定仍未由本次计算完成。

## 5. 五个实际方向入口

以下五个文件均为本次真实输出，每个继续引用完整128、400、144、两图格及原标记嵌入：

|方向|实际完整方向证书|bytes|SHA256|
|---|---|---:|---|
|1|R903-j1-complete-two-weight-RR-certificate.json.gz|7322|0e93cf70a5fbbbfefa070284684dba7b1a9f61062dc75960348105f49a613a9d|
|2|R903-j2-complete-two-weight-RR-certificate.json.gz|7316|d802aedf8750dded778b9945445ce1c43df09864cff048bcbba9f2d94a24dfa5|
|3|R903-j3-complete-two-weight-RR-certificate.json.gz|7324|b9b11aaa234f5920180123be646da071aeaf72b751fa03c9234451cbc3abf1cc|
|4|R903-j4-complete-two-weight-RR-certificate.json.gz|7324|47fc31e1c2709337fd8528f7fc3e70dc34be55bd578e3f08eb31ce064538c03c|
|5|R903-j5-complete-two-weight-RR-certificate.json.gz|7321|b1086af0045db4916b90eecf638191f1a4e847a09d07e0a9441c9925570fcb83|

R907 的完整128输入可直接消费以下真实正常空间，避免重做共享乘积与18行核：

|方向|文件|bytes|SHA256|
|---|---|---:|---|
|1|R903-j1-weight3-complete-normal128.json.gz|375993|69a32f9c341531ca7310b102a2b095b658017103de7d13728548d8a6e2740ef3|
|2|R903-j2-weight3-complete-normal128.json.gz|375776|9e3b56d0cdcf55be4ab1a88a60f2c27b76661de0e3ab728f84e98fb9f03c9038|
|3|R903-j3-weight3-complete-normal128.json.gz|376137|c9ae0b84f1537156b7d9d60935bd3af298d7230370586d97495aaf68c93aafdc|
|4|R903-j4-weight3-complete-normal128.json.gz|376158|d78436fd3545137abda824a054efb918a7589e128b6ee921ce1f7aa70138f09b|
|5|R903-j5-weight3-complete-normal128.json.gz|376010|c2b48ccd6025734483b146ed73ca3c93e41251364518a9f79e9e62cf5bab71d5|

标记嵌入 basename 为 R903-j\(j\)-original-Iz-marked-embedding-and-P0-frame.json.gz，精确 spec 从该方向完整证书的 marked_original_P0_frame_and_embedding 读取，不按模板伪造 SHA。

## 6. 实际来源与字节身份

|项目|真实身份|
|---|---|
|run / compute job|43921416613 / 133489524133|
|source commit|280f1840a717c80665133b0ddab8a55a02af7d4e|
|result|R903-original-five-Iz-two-weight-RR-and-marked-frame|
|core SHA256|bc3e9a53af16b4897b410ca2d2564959bbef8a0f2ad330f1c91ac5b9e6c1c88c|
|wrapper SHA256|97b91720dec52a8396456aa8164dc367946def7ebd756e8e00f10a1a76f427e0|
|configuration SHA256|1dbdddfbaadd555c641f60e3d68a54283bd99e30a8844c992f3c2c2fd86f6934|
|FINAL|p41-original-five-Iz-two-weight-RR-certificate.json；21403 B；99d7e2b6c87282d3f1173f3b6f1875caade4d1500c84093a38d316f0f4f32b72|
|core receipt|15839 B；57f30df9872913f9cf0670b35ef6af8524b832644fc428e22d1db2f928eabec8|
|full manifest|21668 B，148项；7f7913ce277c307f70f534fc225f5f03e648e87663fbdf15f03748288ff0454c|
|完整数学 stage manifest|14119 B；3390aaa35ff6c6a38812800be23e21c68d696574e0e7b1a7f918d4f67cc2ac92|
|source audit|6621 B；74dfde85f277e666f66784ed62a6f279a908ff33b85234a88606489945b43288|
|原输入 carrier|R903-retained-original-inputs.tar.gz；92610560 B；347cc2eeb3c55ac9d47b1f809ad5887367613011b556244d62222f83a60ffc13|

stage manifest 的实际 basename 为
R903-stage-manifest-a55effef3aa6f8a07e8df6249e0d547104dd5c554a8a3e77df315da56ff2ed06.json.gz。
FINAL elapsed 为190.911987995秒，core receipt elapsed 为190.912434078秒；两者属于各自真实计时范围，没有混写为同一精确数值。

本次源闭包共72个选择成员：R827 15、R872 9、R880 6、R883 10、R890 13、R901 19。嵌套的 R901 原函数来源 carrier 保原字节并在运行中重哈希；不把嵌套原函数树删成只有局部模矩阵。R827仍是原已结束 exit124 producer，只消费其已成 W/Krylov，不造原算子整体成功身份。

原 R901 输入精确绑定 run43893483097/source dbfb172d6cce083541a34ff507627dc42ddf9859、configuration d2d5e37ccf73b5f0bc608357d61c215035dd7942e9641777696c97a5c657af90、manifest e3e4eefd4a9b234bad8e8f837f115743c3bdbed5aa1cbafe9579f6f84da50538 和 FINAL 69da20e9500254d8b63e6d8b3d2369bcefe8f9d4a43e4efe7db1a226a95c12f1。

完整原 artifact14254777999，名 serre-R903-five-Iz-two-weight-RR-43921416613-1，329127789 B，平台 ZIP SHA256
95534023e7392f2f9cbb03158d2201e3982c3e0c7db51df0aedf3e77bf2b3d00。
一日到期时间为2026-11-17T17:48:18Z。

## 7. 实际 IO 复核与后继边界

原 compute job 的标准库 verifier 报告五方向完成、实际维数128/400/144/272、全部输出 bytes/SHA 与 live 精确引用通过，未执行数学。后续纯 IO run43922955019/read job133494958370，source e68e4a669792c49c3db63d501ac33920e60e2594，按原manifest读取必要小件；R903这组实际16次 Range、255420传输字节，完成后摘要时间2026-11-16T17:53:22.329923+00:00。它核所选成员，不宣称重哈希329 MB整ZIP或重做任何核。

纯 IO 小包 R903-five-Iz-two-weight-complete-intake-selected-original-sources.tar.gz，87570 B，SHA256 8a1f4f49dfef90a8978066f4edc07a09f61f9ae020da27520a6c15a034dd26fd，只保存本次选择小件与来源清单，不能代替所有大数组。后继应从真实原manifest按上列完整证书引用取需要的正常空间、原帧与原函数树。

这次完成了 R876/R907 所需的真实原128来源及相同 \(\Phi_j\) 嵌入。仍须后继实际认证无基点铅笔、完整672子式、九范数、全部原两端帧和相关分母单位。特征零系数展开、K/Q固定列、原 \(P_1\) 值、Hecke活跃性、连接、非p项、Poincaré period与原指定高度均不是本次结果。原三同源的实下降理想也没有被改标为 \(I_{Z_j}\)。

依据为[原 R903 纸证](R903-original-five-Iz-shared-product-two-weight-RR-and-marked-frame.md)、[冻结执行契约](../notes/R903-original-five-Iz-two-weight-RR-execution-method.md)、[实际 run](https://github.com/Rogerhu12/math-research-public/actions/runs/43921416613)及以上真实证书和源字节。主目标仍OPEN；已完成空间可直接作为原后继消费者的来源。
