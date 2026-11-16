# R927 实证：原参考铅笔的两端完整理想、九坐标与范数帧

日期：2026-11-16。状态：**原参考 $M_0$ 的两端计算已经实际完成，成功的纯 IO 恢复保留全部19个数学阶段，不重新运行核心。** 本文登记实际辅助素点的完整结果；五个目标的 $\operatorname{Nm}\Phi_j\det U_j$ 标定仍是后继。

## 1. 已完成对象与准确原参考

保持原 $Y$、原循环七对应 $p=\pi_s,q=\pi_t$、原两端 $P_0,P_1$ 和原 $\rho_0,\rho_1=\iota^*\rho_0$。沿[原 R927 证明](R927-original-endpoint-pencil-content-and-complete-norm-frames.md)及[冻结执行方法](../notes/R927-original-reference-endpoint-norm-frames-method.md)，本次只消费：

- R917 已成两端完整秩8正规阶，保几何类型 $2+3+3$、全部剩余域和幂零；
- R923 两端已成全部272个目标正常坐标，实际可靠精度均为267；
- R879 的原参考函数 $v_0=f/u=-g/b$ 与原 $ug+bf=0$、共同零身份；
- R872 原单极／首项及原 R914、R883 的 $\rho_\epsilon,t_\epsilon=t-\epsilon$ 帧；
- 原 canonical dual-seven、scalar $7I$、diamond、$-3$ 下降和 $\nu$ 输运。

直接范数方向仍为 $\operatorname{Nm}_p q^*$，原冻结 Hecke 方向继续由同一个 dual7 同构运输 determinant 的两个因子与两端帧，没有以“自伴随”省掉其原标记。

原参考准确函数满足
$$
 u=U_{272}\rho_0^{272}(1+O(\rho_0)),\qquad
 f=\rho_0^{18}(1+O(\rho_0)),\qquad
 v_0=U_{272}^{-1}\rho_0^{-254}(1+O(\rho_0)).
 \tag{927R.1}
$$
这是 R879/R872 已成准确来源，本次不重新解参考函数、不重新计算272阶点尾。新算术实际只用 R923 的前9项。

所有本篇新数值在原辅助域
$$
 \ell=1000000753,\qquad \zeta=549966761,\qquad s=99932770
$$
得到。原问题的 $p=41$ 不变；这些数值不被改标为41进精度、特征零展开系数或所有地方的单位。

## 2. 两端实际完整块与同一全局帧

在每端完整特殊纤维内，从真正目标 $P_0$ 最大理想的八次幂及 annihilator 分出其整个主分量，保全部幂零。幂等元提升和完整8阶换基均完成；未以约化商或单个几何根代替完整块。

实际结果如下：

|实际量|原源端 $P_0$|原源端 $P_1$|
|---|---:|---:|
|目标 $P_0$ 完整块秩 $r_\epsilon$|2|0|
|完整补块秩|6|8|
|原输入可靠精度|267|267|
|本次实际工作精度|9|9|
|$m_\epsilon=\operatorname{ord}_{\rho_\epsilon}N_{B_*/R}(q^*\rho_0)$|2|0|
|上述参数范数首项 $c_\epsilon^*$|1|1|
|两端同一整数 $\lambda_0$|1|1|

$P_1$ 一侧的目标 $P_0$ 块真实为空。该处分块秩0、空范数1、参数范数阶0与首项1是算法明确采用并核实的合法分支，不作不存在的块逆，也不补造长度三目标标签。

两个端点共同选择 $\lambda_0=1$，所以保留的同一个原全局参考函数是
$$
 1+v_0=\frac{u+f}{u},\qquad
 G_0=N_{E/F}(1+q^*v_0)=\frac{N(q^*(u+f))}{N(q^*u)}.
 \tag{927R.2}
$$
原分式理想为
$$
 B+q^*v_0B=(1+q^*v_0)B.
 \tag{927R.3}
$$
这里的格由原八个正规阶基列正乘同一生成元定义，实际首消费者保存准确表达式、完整模参数两矩阵与全部纤维坐标；未宣称整个 Laurent 格基已展开。

补块上的参考值利用原配对关系和实际整个补块的单位表示求得。目标 $P_0$ 块则使用准确254阶单极及实际低阶参数范数。两种表示属于同一原函数，未给不同分支任意更换参考函数或标量。

## 3. 完整范数首项及原 t 帧

准确计算式仍是
$$
 \mathcal L_{\rho_\epsilon}G_0=
 \left(-254m_\epsilon,\,
 \lambda_0^{r_\epsilon}U_{272}^{-r_\epsilon}
 (c_\epsilon^*)^{-254}C_\epsilon(\lambda_0)\right),
 \tag{927R.4}
$$
其中 $C_\epsilon(T)$ 是完整补块的 $\det(I+T M_{v_0})$ 模参数多项式。没有丢掉原 $U_{272}$，也没有只保留九坐标而删去完整参考 determinant。

实际值为：

|端点|参考范数 $\rho$ 阶|参考范数 $\rho$ 首项|原 $t$ 帧首项|
|---|---:|---:|---:|
|$P_0$|$-508$|155035654|466867763|
|$P_1$|0|728442038|728442038|

原 $t_\epsilon=c_\epsilon\rho_\epsilon+O(\rho_\epsilon^2)$ 使用既成来源，$c_1=-c_0$，没有再次归一化。由原首项换帧式
$$
 G_0^t=c_\epsilon^{-\operatorname{ord}_{\rho_\epsilon}G_0}G_0^\rho,
 \tag{927R.5}
$$
$P_0$ 一侧准确以原 $c_0$ 的正508次幂换帧；另一端阶0。保持同一全局 $G_0$ 和原帧后，实际完成的比值是
$$
 \boxed{\ (G_0^t(P_1)/G_0^t(P_0))\bmod\ell=315436983.\ }
 \tag{927R.6}
$$
它是指定参考 determinant 帧的实际辅助值，不命名为原 theta／Poincaré period。

上述新 $r,m$ 与 content 数据是本合法剩余处的结果。原准确分式理想、单极阶、determinant 表达式和来源 DAG 同时保留；本次明确不从低阶模零推出新特征零实际阶。FINAL 的 characteristic_zero_observed_content_orders_claimed 保持 false。

## 4. 原九参考截面的真实相对坐标

两端的完整8维余矩阵 $C_0,C_1$ 保留所有块并满足
$$
 C_0+\lambda_0 C_1=I_8.
$$
全部64个系数的反向身份已核。对原参数 $i=0,\ldots,8$，每个实际
$\det(C_0+iC_1)$ 与同一范数本原多项式比值相符；这不是在八个几何点取值的替代算法。

|原参数 $i$|$P_0$ 相对坐标|$P_1$ 相对坐标|
|---:|---:|---:|
|0|0|34396996|
|1|1|1|
|2|959335591|387602051|
|3|482704666|100683116|
|4|138076329|417355007|
|5|13242416|162727826|
|6|426570306|381010434|
|7|362075602|127689753|
|8|345975871|476974980|

第一端参数0的零是该原截面在所选参考格帧中的纤维坐标零，不是全局范数函数零、Picard 类零或 inactive 证据。参数1的坐标1来自选择该同一未缩放全局生成元，不是事后把两个端点的首项分别改成1；完整 $G_0$ 数值仍是第3节的非平凡值。

## 5. 实际数学完成与只 IO 恢复的区别

原数学运行是
[run43922183082](https://github.com/Rogerhu12/math-research-public/actions/runs/43922183082)，source e56cbda0e08ce47ff7a3d5bcd7e4837720bd833a，construct job133492204453。其数学步骤成功，core process_exit_code=0、complete=true，生成19个完整数学阶段。FINAL elapsed 为0.4441233889999978秒，core receipt elapsed 为0.4449299609999997秒。

该原 job 后续标准库 verifier 因把真实 common stage 的 five_target_sources 键误读为 future_target_sources 而失败。这个 KeyError 不改变已成核心及数学阶段。原平台 conclusion=failure 被真实记录，没有改写成一次平台成功。

修正后的
[run43923552968](https://github.com/Rogerhu12/math-research-public/actions/runs/43923552968)，construct job133497099855，source4b005ba1dae2a84b6ac3a663befca95c59725e4b，只读取并核验原完整 FINAL、原 complete core、原配置及全部 stage bytes。实际日志明确为
$$
 \texttt{core\_reexecuted=false},\qquad
 \texttt{new\_mathematical\_stage\_count=0}.
$$
19个数学阶段、原 FINAL 和原 core receipt 全部逐字节复用。旧 public input/run/core/manifest 另保为 reused-parent 原文件，新的 public/run receipt 只记录真实 IO-only 操作及原 parent 身份。

成功的 R927_REFERENCE_COMPLETE_IO_REVIEW 还核实：80个原来源文件、19个完整数学阶段、两个实际端点及第2–4节全部标量、九坐标和原帧比值。标准库核验不重做矩阵、范数、幂等元或任何旧源算术。

## 6. 不变的数学来源 pins

|项目|真实 bytes / SHA256|
|---|---|
|数学 core|61605 B；4d0be4a7ced92ca57dad14863fe7433903e2b0c82df1e47e7c1520dfc10aaa28|
|冻结执行方法|10664 B；74347cfb1b6029e3975fbcbc1220c437a01abe0ca61adb61dc309c2878f8feaf|
|数学 configuration|5e299ce6d65bd4a66244bcfada88bdefb9fe4d36e8b9673f381d01dd038ce3bf|
|FINAL|21177 B；09de0ae883cece35b26e645f6f5071c75b4de219f7d28024de286a5192524073|
|原 core receipt|733 B；05a10f654e54c761472ad3cb31be5175d9ee0280472b78ee933e03ddb5564258|
|stage manifest|7509 B；db4c7877d50bfa29440d69c6bcf95554b22f86dff618ba9c0e3148a1adb1a1b4|
|source audit|9387 B；9550199b08af756e0696b3e980ddb1b20ee4df0a9b698d0e933ec5488001a712|
|原80来源 carrier|8288763 B；1f1aececd4bb2614fd991ef34faec4952f09db9258456704b7e0b7c0e4c0c604|
|retained-inputs receipt|4020 B；a6426f6b9425e2ccf178d9d32cc508a690a50746f9950b15abf21d7270400d9c|

FINAL basename 为 p41-original-two-endpoint-reference-norm-frames-certificate.json；stage manifest 为 R927-reference-stage-manifest.json.gz。两者均保原数学 configuration。

实际两个完成证书为：

|端点|文件|bytes|SHA256|
|---|---|---:|---|
|0|R927-reference-P0-complete-reference-ideal-and-norm-frame.json.gz|8689|a76ce6d46544c37119ba270404067027ee693d451e5365605d99c1184dd99084|
|1|R927-reference-P1-complete-reference-ideal-and-norm-frame.json.gz|8694|f2f095db623c9cc306cdc478467e53e2826e7883211d4f8d9a32c61fd3259792|

同一全局参考参数阶段 R927-reference-same-global-reference-integer-frame.json.gz 为6724 B、SHA25691f5d0d3b28b37b37adb442959851448018f3d68315bcd60374b157496c97e47。两端原t帧比较阶段 R927-reference-complete-reference-two-endpoint-t-frame-comparison.json.gz 为6942 B、SHA2567d948e03c8fdfdd357e02ad838cb41b0732bebabcc91730e22aa21e869e0b4c9。

原80来源按真实 producer 分为：R872 9、R879 8、R914 7、R917 11、R923 45。源 R923 的全部267项仍是原完成输入，本次只按原精度取前9项。旧正规阶、全272目标坐标、R879解和原Hensel点尾均没有重算。

## 7. 两次平台载体及后继

原数学已成、IO出口失败的 artifact14253893174 为8652140 B，ZIP SHA256 b88467f38488f0a2c65ed7049a6833572ebd1f1a5270e4341c93c99892bbff90；原 manifest5393 B、30项、SHA256 acdd1a7868850a0dd55d4976e42dc5bdc6747cd0e31b28056d430adaf20b22c5。

成功纯 IO 恢复 artifact14253699467，名 serre-R927-reference-endpoint-norm-frames-43923552968-1，为8702573 B，平台 ZIP SHA256 bf9aada6f88027572125a98de1600c4bec60cb047b7418556f0f81cab1460f73，到期时间2026-11-17T17:56:48Z。其新运输 manifest 为6209 B、35项、SHA256 08edf04168eb598c1a9b7d6c3ee3c5778511b71a86c50613727c149d23bfdd91；reference 为240 B、SHA256 912663d28723fdd8a9c7a1bd6995e585e6ece9553aa07ef0b5618ed8f0d842e7。新 run receipt 为3656 B、SHA256 f6954010451759fd4bd922224fbf5447fec3bba63605e41a8fa901f147a735f1；新 public input 为29679 B、SHA256 9373fcfe51e2ed9d884dd6e2308089ec5af13f8fac6e4600ce87a501310a62fe。新运输身份不覆盖上一节的原数学身份。

独立纯 IO 读回为 [run43925047020](https://github.com/Rogerhu12/math-research-public/actions/runs/43925047020)，read job133502304547，source a683fbacf869ae91eb792c1ba8d4e416fa25c062。其于2026-11-16T18:05:34.407025UTC完成11个选择成员的原 manifest/SHA 核验，实际11次 Range 共366498 B；并非重新下载或重哈希整个平台 ZIP。所存小 tar 为53744 B、SHA256 f57674be98aa484cfd1c7254b30bbd837811c514aa6d0ea95be769697f838ad4。此读回再次核实两个完成证书、共同整数阶段、t 帧比较及原 FINAL，完整数学字节保持。修复 wrapper 的真实 SHA256 为3fa04f1d3ed8b72ec5d763110834ad20bab6c14323f3eed3807d692a6770168d；纯读回摘要未抽该嵌套键而显示 null，不更改原实际请求和计算步骤已绑定的来源。

本次真实已成出口是参考格、九个相对纤维坐标、同一完整参考范数 $G_0$ 与原两端t帧。五目标须从 R907 的实际672无基点铅笔和完整原函数程序接入，另算 $N(q^*\Phi_j)$、目标本原范数多项式与两端共同局部生成元，再正乘 $\operatorname{Nm}\Phi_j\det U_j$ 并除本次原参考 determinant。不能将本次 reference 首项或 $z=0$ 的整Artin范数值代替五目标的端点标定。

实际 FINAL 保留 future_target_sources 未成边界、五目标 NormPhi／理想格／高度皆 false；不把 $I_Z$ 改标为实下降立方，不判原Picard inactive，也没有省掉原dual7、theta二挠、非p项或指定Poincaré高度。该参考来源已可直接复用，无需重跑19个数学阶段。
