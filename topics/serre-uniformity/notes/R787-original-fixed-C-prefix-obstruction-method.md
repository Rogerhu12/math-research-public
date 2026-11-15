# R787：原固定 C 的 branch0 前缀障碍执行契约

日期：2026-11-15。状态：**新消费者的方法与来源契约，未登记任何实际 Ω 或严格 C 拒绝。**

数学证明使用
[共享残差与固定C下一模层障碍](R787-original-fixed-C-next-digit-obstruction-and-shared-source-contract.md)，
SHA256 5c4ab25ce03bdca9dfe49def80e93fa01e481778171426cc1cef5a2fd5f26564。
本次只消费已结束42维与56维有限搜索的98个不同正号整分母，
不再执行这些 LLL 或它们已完成的 A/B 准确检验。

## 1. 唯一首轮 scope

固定
$$
\ell=1000000753,\quad M=\ell^{430},\quad Q=M\ell.
$$
原来源仍是归一自由列1186、其他自由列为零的同一个430位解。
本次 source_mode 为 from_original_430_cleared_residual，
不是尚未发布的更深原 current。

只选原 branch0；仍用实际 selection 的原 $B_{\rm fld},s$ 根，
不另选根或改变 $\lambda$。
保原69个 $A$ 块、70个 $B$ 块：
$$
A_0,\ldots,A_{68},\qquad B_0,\ldots,B_{69}.
$$
原 $J$ 包含于前1380行；输出行恰为其补集146行。
没有计算其余1180条投影方程。

新 RESULT 为 R787-original-fixed-C-prefix-obstructions；
FINAL 为 p41-original-fixed-C-prefix-obstructions-certificate.json。
complete=true 只表示98个本 scope 的必要条件决定全部完成。
它永不表示原准确 $C$、原函数、CM点、极理想或高度已经得到。

## 2. 一个已结束56维产物提供全部实际输入

唯一外层来源为真实56维 run43754407301，
source1827d794565f94455e4f251f20d1979b55fee783，
artifact14178104533，216929678字节。
其平台 ZIP SHA256 为
a6c23bc84d379f96f67233243d5a5fc3838f18cd913502088b4a08de455d4451。
完整 manifest 为38367字节、184项，
SHA256 7418100ba952913eeab8a60604d92ad4ad5ffdd49d3204602897641198ef77f0。
实际小 IO run43757804966 已逐原 manifest 核全部182个非 carrier 文件；
原 frozen verify 已核两个原 carrier 的实际成员。

包装恢复以下原字节目录：

- retained/R787、retained/R781、retained/R786：原1380件闭包；
- candidates/two_probe：原42维的136个非 carrier 源文件与 manifest/reference；
- candidates/three_probe：新56维的非 carrier 源文件与 manifest/reference。

旧42的完整基和42个拒绝在第二个原 carrier，
新56的完整基、56个拒绝在外层小文件。
新56实际旧拒绝复用数为0，故二者给98个不同的正号14维整数 $D$。
消费者仍逐个核候选指纹、原行/符号、旧 outcome/rejection/closed 链和去 content 前的 $D$，
不能只因整数98已知而跳过真实源检查。

读取原 rational-blocks 内的 A_inverse_mod_prime；
它是旧 $1234\times1234$ 有理系数方块的模 $\ell$ 逆，
不是特征零逆，也不是14支 $1186$ 阶 Schur 逆。
读取原 selection 的 kappa_inverse_at_each_L_branch[0]。
这两个真实输入已在1380件内，不新增 producer，不混用 R824 common clear。

## 3. 准确复用的数学模块

原数域实现仍为 R781 core：
d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751。

原 R787 core 为：
93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04。

新核心把它们作为明确、按 SHA 固定的模块。
只复用原 ModularField 的 packed/reduced/multiply；
其系数环仍为原 $B_{\rm fld},s,t$ 的首一商环，允许模 $Q$。
convolution 新增严格70项的覆盖方法，
沿原1521步 $q$ 打包与原39、507的字段间隔。
单次字段积最高位1520，故相邻 $q$ 块不串位；
低70项只依赖输入低70项，不产生任何未需要的尾。

不调用原 Job/lift/correction，不生成下一份原 normalized current，
不重新计算原 Laurent、原 Fourier、原基或任何原分支逆。

## 4. 共享部分只做一次

原430输入记为 $(\bar a,\bar c)$。
先按原 $Z_p,Z_d$ 得到 $Z'\bar c\bmod Q$；
保存一个完成阶段，准确尺度原样保留。
原 $F$ 数据只读已有整数数组的低70块。

随后按每5个 $q$ 块分段计算
$$
\bar A_n=F_n\bar a\bmod Q,\qquad
\bar B_n=F_nZ'\bar c\bmod Q.
$$
只计算所需69个 $A$、70个 $B$；
第69个 $A$ 块不属于本 scope。
每段独立完成后原子保存。
加权 $W_j=\kappa^j\bar B_j\bmod Q$ 也按5块保存。

用70项原打包卷积组成
$$
T_m=\sum_{j=0}^mR_{m-j}W_j
   +246^3\kappa^{m+1}\bar A_{m-1}\pmod Q,
\qquad 1\le m\le69.
$$
另核构造性 $B_0=0$。
所有280个坐标必须能被 $M$ 整除；
记录标准整数商
$$
e_m=T_m/M\bmod\ell.
$$
这些是**正的清分母残差**。
不使用原 correction 内另取负号后的 rhs。

在这一步之后才对14个 $L$ 坐标按原 branch0 评价。
用 selection 中已经保存的 $h=\kappa_0^{-1}$，
依原顺序生成
$$
\gamma_m=246^{-3}h^{m+1},\qquad m=1,\ldots,69.
$$
首幂为2，末幂为70。
乘 $\gamma_m\bmod g_t$ 后展开20个 $t$ 系数，
得1380行正的 $\rho_0$。

令 $U_0$ 为原 A_inverse_mod_prime，
$J$ 为原 A_pivot_rows，
$\mathcal R_{\rm pre}=\{0,\ldots,1379\}\setminus J$。
保存唯一共享结果
$$
\Omega_0=(\rho_0)_{\mathcal R_{\rm pre}}
       -F_A[\mathcal R_{\rm pre}]U_0(\rho_0)_J
       \pmod\ell.
$$
整个共享部分未产生任何新的 $C$ 校正或原 Dixon 位数。

## 5. 每个候选只新增 qC 与一个模右端

对原未除共同 content 的正号 $D$，
非自由列保持旧中心提升规则。
定义
$$
c'=D\bar c-Mq_c.
$$
为了仅得到 $q_c\bmod\ell$，
对每个非自由坐标先算
$$
u=(D\bar c_i)\bmod Q,\qquad
v=u\bmod M,\qquad
q_{c,i}=(u-\operatorname{center}_M(v))/M\bmod\ell.
$$
这里逐原14个整坐标进行。
差可被 $M$ 整除；
无须构造完整旧 $A/B$ 候选，也无须再次检查旧准确 Laurent 残差。

选定自由列的准确 $c'$ 等于未约化 $D$，
所以该列 $q_c=0$，不能套用中心提升公式。
其余自由列同样为零。
保存全部1214×14个小模坐标，使以后若实际需要其他支，
可以直接消费这个已完成商而不再做高精度整阶乘法。

只把它按 branch0 评价为 $q_b$；
先用原 $Z'$ 展开，
再以旧 $F_0,\ldots,F_{69}$ 得一条70项的 $G$。
由原 $R_m$ 和已有 $h$ 得
$$
Y_m=-246^{-3}R_{m,0}h^{m+1}.
$$
一个39步 $t$ 打包的 $YG$ 卷积即可给
$C_yq_c$ 的前1380行。
这只是一个右端，绝不重建1214列的原 $C_y$ 矩阵。

应用同一个旧 $U_0$，得到
$$
\Omega_D=D_0\Omega_0+
 (C_yq_c)_{\mathcal R_{\rm pre}}
 -F_A[\mathcal R_{\rm pre}]U_0(C_yq_c)_J.
$$
这里 $D_0$ 是原 $D$ 在 branch0 的评价，不是14个整坐标中的常数坐标。
保存实际146项、真实输出行号及首个非零位置。
若非零，才能声明这个未除content的固定 $c'$ 不可能是准确分母方向。
若全零，只报告 prefix_only_zero=true；
不能写“$C$ 已正确”“原关系通过”或“430位已足够”。

原42/56的 A/B 失败只作为候选来源记录。
新的严格 $C$ 排除有独立来源、数学身份和实际残差；
不会把旧失败改名成新结果。

## 6. 断点与完成语义

输出只含根目录 R787-fixed-C-*.json.gz 完成阶段，
以及真实新 FINAL、core/run 回执。
临时 .tmp 仅用于原子替换。
没有隐含 work 子目录或新工作 tar。

共享高精度段、权段、除M后的小向量、原 branch 归一化、
共享 $\Omega_0$ 分开保存。
重启时直接读取已完成同 tag 阶段。
原大 convolution 若尚未完成原子写入，则不冒称它已完成；
已完成的源评价与加权段仍可继续消费。

每个候选分为 quotient、prefix-image、result 三个阶段。
完成 result 后才推进 current 的下标；
若写完 result 后中断，恢复只补指针，
不重做该候选算术。
当前记录 complete=false，与完成数学阶段分开。

stage_manifest.files 列全部实际 complete=true 阶段，
排自身及 current；后者另由 resume_state 指定。
两个原数学模块、原来源、原98候选、branch0、
69/70块和146行都属于数学 tag。
预算和一次允许处理的候选数量不改变已成阶段身份。

最终完整统计必须满足
$$
\text{strict_fixed_C_rejected_count}
+\text{prefix_only_zero_count}=98.
$$
正面目标标志 actual_exact_C_recovered、
actual_y_map_recovered、complete_129_function_relation_verified、
beta_or_height_computed 一律为 false。
工作模数是 $\ell^{431}$，
但 new_normalized_Dixon_digits_computed 仍为0。

## 7. 发布与后继边界

所有新数学只在公开仓库 Actions。
源码、参数、证明和简明 run/SHA 登记可进 Git；
机器回执、完整向量、残差和矩阵只在一日 active artifact/carrier 中续传。

若将来扩大到完整1326行或更多 branch，
必须明示新 scope 与真实完成阶段的导入来源；
不能把本次146行的零改写为全局通过。
若原更深 normalized current 实际发布，
应切到已证明的独立 source_mode 并直接消费它；
本次不与仍在运行的原 Dixon 并行重算其下一整步。
