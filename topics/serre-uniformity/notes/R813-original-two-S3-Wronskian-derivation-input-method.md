# R813 执行契约：两个原 S3 Wronskian 的准确导子输入

日期：2026-11-15。状态：**首次工程契约，尚无新的算术输出。**
证明见 `results/R813-original-Wronskian-normal-derivation-and-cyclic-certificate.md`。
以下首次只做两个690维有理右端的全820行准确认证。

## 1. 固定身份与最小 scope

- RESULT：`R813-original-Wronskian-derivation-inputs`。
- FINAL：`p41-original-Wronskian-derivation-inputs-certificate.json`。
- CLI：`--config --proof --method --retained --output --budget-minutes`。
- 固定 python-flint 0.9.0；新算术仅本公开仓库 Actions。
- 首 scope：`two_original_S3_Wronskian_inputs`。
- 核心预算300分钟、job350分钟；预算耗尽只保存准确续算状态。
- 初次只保存 $G=W(\tau,\sigma)$、$J=W(\tau,w_0)$ 和
  $g=G/\tau^3,h=J/\tau^3$ 的坐标。
  本次不计算 $M_g,M_h,\Gamma$，不预填任何导子或函数 DAG 的成功。

R806 的真实 primitive 候选尚未成功时，request 保持 pending。
不从理论存在性或运行中的候选推定 $w_0$。
本计算不需要 R787/R809 的原 A/B，不重算其任务。

## 2. 三个实际 producer 与源身份

### R805：真实铅笔、S3与所有旧tau乘积

必需小证书、完整 manifest/metadata、stage manifest、accepted pencil、
graded-free basis、S3 basis index及其全部实际690行、旧alias index和实际short minor。
原 $\tau=e_0,\sigma=e_1+n e_{73}$ 的 $n$ 从该producer读取。
原整基次数固定 $0,1^{144},2^{127}$；S3顺序固定 $a$ 外层、$j$ 内层。

逐项核旧alias中的146个 $(0,i)$ 正对应原 V2 第 $i$ 行，
$0\le i<146$，且尺度均为 $82^4$。
这项原recipe的只读检查已确认全部146项存在；
正式core仍把它作为输入断言，不由行号猜测产品身份。
不重新生成任何 $\tau e_i$。

### R806：实际w0、同一690块与原有限域逆

只接受真实complete的 primitive multiplication/cyclic certificate。
读取实际 $w_0$ 的146个原整数坐标、实际候选与cyclic来源、
coordinate chart、所用固定690行、对应有限域inverse及其source。
必须核它与R805的same graded basis、same S3 index、same pencil和所有尺度一致。

如果旧原逆适用且新rhs分母为单位，直接读回；
不重新选 minor、计算旧秩或重新求同一个逆。
若一个新分母在原辅助素数不可逆，按明示参数换素数，
仍保同一原有理690选行及全部820行终验；坏素数不是特征零失败。

本次不需要重求原 $M_w$ 的272列坐标；
它的实际证书只为固定原 $w_0$ 与后继导子源身份。
后继恢复 $M_g,M_h,\Gamma$ 时再按需消费真实原 $M_w$ 分组。

### R786：已成M2及V2

从真实成功活跃包或其已认证后继bundle读取：
原 M2 第0、1、73行及实际 $w_0$ 支持所需各行；
对应的原 V2 第 $i$ 行（即 $\tau e_i$）；
必要metadata、certificate、stage manifest和原recipe。
原129项文件完整核SHA，只取已有 $q_Y^0,\ldots,q_Y^{40}$。
未需要的长尾不生成，旧E1、period、Hom和普通幂不重算。

producer身份绑定 result/run/source/core/manifest/certificate SHA；
artifact只是传输来源。所有继承文件均保持原bytes/SHA。
首次选出的最小闭包进入本次一日bundle，后继不依赖快过期的独立旧包。

## 3. 只新增两个加权formal乘积

保原 $D_0=(q_Y/82)d/dq_Y$。
对 $s=\sigma,w_0$，先由已成原 V2 行合成
$P_s=\tau s$，其原尺度 $82^4$。
直接用旧M2行合成同一个 $s$，不更改原整数坐标。

按恒等式
$$
W(\tau,s)=D_0P_s-2sD_0\tau
$$
形成新的41项：
$$
82[ q_Y^m ]W
=m(P_s)_m-2\sum_{i+j=m}i\,\tau_i s_j,\qquad0\le m\le40.
$$
只有右端的加权formal乘积
$s\cdot\sum_i i\tau_iq_Y^i$ 是新增卷积。
$P_s$ 的普通乘积项全部只读复用。
这个加权formal乘积自身不宣称属于任何普通模形式空间；
完整差的全球 $V_3$ membership 由R813定理813.1给出。

在原 $q_Y/\xi$ 与 $v/t$ 两套准确表示中形成并核对该新目标。
保持原 $v=\xi^{-10}q_Y$ 相位、40维圆分或20维实圆分基。
权重 $m$、$i$ 及 $1/82$ 都是准确有理数；不使用数值导数。

两个目标可逐个落盘；每个完整阶段保存真实 $s$ 坐标、
旧M2/V2源、原乘积别名、准确区间 $[0,41)$、
新加权项来源及未清除的有理比例。
一个已成目标不因第二目标或新scope追加而重新卷积。

## 4. 相对尺度不消失

原 $\tau,\sigma,w_0$ 都带 $82^2$；
旧 $\tau s$ 带 $82^4$；
原 S3 的每条基带 $82^6$。
目标通过上式的准确 $1/82$ 恢复原 $D_0$。

可将每个820维有理目标写为 $\alpha t$，
$t$ 为primitive整数向量、$\alpha\in\mathbb Q$；
只对 $t$ 做整数Dixon，最终坐标乘回整个 $\alpha$。
不能为了使目标“同尺度”额外乘 $82^2$，
不能只登记primitive整数列而丢掉原 $1/82$ 或去content比例。
最终字段须同时保 `original_D0_qY_factor=[1,82]`、
`original_M2_scale=6724`、
`original_V2_scale=45212176`、
`original_S3_scale=82^6` 的真实整数值与准确column scale。

## 5. 同一个690块、完整820行

矩阵是原S3的 $820\times690$ 有理实坐标块，
不是原R786另一个V3坐标基。
原选行与可用模逆读取R805/R806的真实stage。
两个右端共享同一块，仅新增两列坐标。

Dixon每轮在原整数余数上精确更新；
有理重构使用预先固定统一矩形 $2AB<M$。
候选必须在全部820行准确乘回，再恢复原 $\alpha$，
才标记该完整目标成功。
首目标即使已经成功，第二目标仍继续；
若旧FINAL只含部分scope，不能据它直接退出。

每个未成目标只保最新完整lift/余数，
旧位数以name/bytes/SHA/previous链保存。
实际rank、modular determinant、Dixon位数、seconds由真实输出读取，
不从其他任务抄一个相同维数的minor。

## 6. normal向量与消费字段

原S3 row 映射：
$a=0$ 有 $j=0,1,2,3$；
$1\le a\le144$ 有 $j=0,1,2$；
$145\le a<272$ 有 $j=0,1$。
把唯一S3坐标 $x_{a,j}$ 读为
$$
(v_g)_a=\sum_jx^G_{a,j}z^j,\qquad
(v_h)_a=\sum_jx^J_{a,j}z^j.
$$
这是同一原截面除以 $\tau^3$，不再乘原82尺度。

每个目标至少输出：
原target名、$s$ 的146个整数坐标/源、
完整S3输入和目标SHA、
coordinate numerator/positive denominator与原rational scale、
row mapping、normal rank272、degrees $\epsilon$、
regular degree bound3、完整820回代标志、
原 $D_0$ 与标量保留标志。
$g\ne0$ 可从几何证明；代码仍核实际准确向量非零。
不把有限域一次非零或单条Fourier系数当作完整回代。

FINAL明确区分：
`original_two_Wronskian_normal_vectors_computed=true`
只在两目标都准确完成时成立；
`g_h_multiplication_matrices_computed=false`、
`normal_basis_derivation_matrix_computed=false`、
`original_function_DAG_computed=false`、
`eta_or_height_computed=false`。
阶段文件中的真实rank与秒数由成功运行后登记。

## 7. 后继矩阵的已证参数，首次不执行

在原真实 $M_w$ 上恢复 $M_g,M_h$：
weighted bound $3+\epsilon_a-\epsilon_b$，最高5，
每好素数6个好点插值，原第一列逐系数，
严格degree后7个互异有理点完整交换子终验。

再由R813(813.23)–(813.24)恢复 $\Gamma$：
weighted bound $2+\epsilon_a-\epsilon_b$，最高4，
每好素数5个好点插值，$\Gamma e_0=0$逐系数，
非齐次交换子最高5，须6个互异有理点完整终验。
两类数字不能混用。
全部仅有限域数值Krylov逆；已有同源prime/点逆优先读取。
不生成特征零Krylov逆或先求完整隐式方程。

实际 $\Gamma,M_g$ 作用于所有14个原 $L$ 分量；
常数域运输和原 $\rho_j$ 相位保留。
R811原 A/B 乘法矩阵真实返回后，
才按(813.26)形成原 $\delta y_f$ 的完整分子/分母pair。

第二图的同一个导子允许在原H有极。
必须使用
$\Gamma^\sigma=D\Gamma(1/t)D^{-1}-tM_g^\sigma\operatorname{diag}(\epsilon)$，
$M_{\delta t}^\sigma=-t^2M_g^\sigma$，
其中 $M_g^\sigma$ 是相同函数运输；
若读取的是 $G/\sigma^3$ 的regular矩阵，先除 $t^3$。
不把矩阵修正项简化为标量对角阵。

## 8. 保存与授权边界

本地仅源码、AST、schema及传输SHA检查。
新Wronskian、坐标、modular逆、Dixon或导子算术全部在公开Actions。
只有真正完成的原stage可用于下一阶段，pending请求不触发。
大数组、完整证书与临时矩阵只放一日active产物和直接续算bundle；
Git/Release仅保存证明、脚本、参数、run与SHA。
