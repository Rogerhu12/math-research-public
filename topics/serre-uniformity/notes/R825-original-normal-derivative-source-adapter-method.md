# R825 小消费者：原 a、b 两图导子向量与C坐标

日期：2026-11-15。状态：**实现契约；原R809 A/B和R815导子全矩阵必须实际完成后才可激活。**
本scope先提供R825所需的$\delta a,\delta b$，不构造大乘法矩阵P/Q或一般多项式核。

## 原对象与范围

RESULT为 R825-original-normal-derivative-inputs，
FINAL为 p41-original-normal-derivative-inputs-certificate.json，
requested_stage为 original_a_b_normal_derivatives_in_two_charts。
核心 R825_original_normal_derivative_inputs.py；
CLI --config --proof --method --retained --output --budget-minutes。
固定python-flint0.9.0和原R811通用Retained/原子IO helper SHA，
不导入其R809/r5乘法求解Job。

只处理原
$$
a=A/\tau^5,\qquad b_0=B/\tau^5
$$
及
$a_\sigma=A/\sigma^5=t^5a_\tau$、
$b_{0,\sigma}=t^5b_{0,\tau}$。
字段basis始终为原
$1,b,\ldots,b^6,s,sb,\ldots,sb^6$；
此处$b_0$区别目标曲线参数$b$。
输入导子矩阵是Q系数，故逐原14分量运算，无需新字段乘法、根或嵌入。

本次输出是导子作用于函数的normal向量和原C基坐标。
不是$M_{\delta a},M_{\delta b}$乘法矩阵，也不是P/Q、一般极理想或D。

## 三条必须真实完成的来源

- R809：原A/B两normal向量、四个7列坐标组、原S5 index与原字段/target配置；
  必须 actual_original_y_normal_vectors_computed=true。
- R815：原g/Gamma的完整两图算子index及全部68个实际row blocks；
  必须是g乘法与Gamma导子两个真实目标，保原七点证书来源。
- R820：两图完整C index及其272+272原列stage；
  实际degree数组都是$0^{271},20$。不重新求C或原20维字段。

各来源必须具有同一个原R805 free-basis SHA、相同EPS、
原$\sigma=e_1+e_{73}$，并保各自真正producer身份。
原source artifact未完成时不得用占位结果激活。

## 原normal列恢复

原R809 S5行给$(a,j)$，对应normal基行a和底变量幂j。
对每个目标、每个原字段分量，准确恢复
$$
v_{a,j}=\frac{\text{coordinate numerator}}
                 {\text{column denominator}}
        \,\text{original target rational scale}.
$$
尺度只乘一次，不再补R787移除的内容或任何82次幂。
每目标恰1234个S5位置，并完整核degree$\le5-\epsilon_a$。
第二图列由$t^{5-\epsilon_a}v_a(1/t)$逐系数运输，
不是仅对字段系数共轭。

## 两图导子运算

第一图准确计算
$$
d_\tau=\Gamma_\tau v_\tau+M_{g,\tau}v_\tau',
\qquad u_\tau=M_{g,\tau}v_\tau .
$$
第二图输入R815的g-sigma块是
$t^3D M_{g,\tau}(1/t)D^{-1}$。
真正$\delta_\sigma t$矩阵要再乘certificate给出的$-1$，
故
$$
d_\sigma=\Gamma_\sigma v_\sigma
        -M_{g,\sigma}^{\rm regular}v_\sigma',
\qquad
u_\sigma=M_{g,\sigma}^{\rm regular}v_\sigma .
$$
$d$逐行degree$\le7-\epsilon_a$，
$u$逐行degree$\le8-\epsilon_a$。
每目标每图$d$有1778个加权有理位置，原14分量都保留。

实现按16个输出行一块，同时处理28列原字段分量。
对每个Mg系数和输入幂的整数矩阵乘积，
同一实际乘积同时累入u和带幂次因子的$v'$部分；
不为两个用途重做相同整数矩阵乘法。
Gamma/g块分母先按真实两数LCM合并，
每个输入分量仍保自己的原分母，不形成28列的无需求大公共分母。
完成块原子保存，断点续算只读已有块。

## 必须保留的第二图额外项

因为$\delta_\sigma=t\delta_\tau$，
$$
\delta_\sigma(t^5a_\tau)
=t^6\delta_\tau a_\tau-5t^7g_\tau a_\tau .
$$
因此对每个normal输出行i准确核
$$
d_{\sigma,i}(t)
=t^{6-\epsilon_i}d_{\tau,i}(1/t)
 -5t^{7-\epsilon_i}u_{\tau,i}(1/t).
$$
两项单独可能有$t^{-1}$，必须实际相消。
不能把$d_\tau$当成普通权7截面直接做$t^7$翻转。

同时完整核
$$
u_{\sigma,i}(t)=t^{8-\epsilon_i}u_{\tau,i}(1/t).
$$
所有原有理系数逐项比较；不以模点或预期次数代替。
a、b0两目标分别认证，字段不混列。

## 原C的准确成员证明与坐标

因为原a、b0在各图正则，而原导子在cusp为零，
两图$d$都应属于实际C。
使用R820既有列
$C_j=e_j-q_j e_{271}$、$C_{271}=P_{20}e_{271}$，
对每个原字段分量准确求
$$
w_{271}=
\bigl(d_{271}+\sum_{j<271}q_jd_j\bigr)/P_{20}.
$$
要求在Q多项式中余数全零，并完整乘回；
其余C坐标$w_j=d_j$。
输出用原d row blocks引用前271行，只新增真实末行商，
避免重复存同一大向量。

C基坐标与原normal坐标分别标清。
这只是自由模换基，不能把它叫$I:C$或P0评价。

## 输出与续接

每个完成row block绑定：
原R809 target与四个坐标组、原输入vector stage、
原Gamma/g row blocks、当前图、28字段列顺序、
源分母与所有确切输出分母、原EPS和正确第二图负号。

最终certificate需逐项保：
两目标normal向量、两图完整运输、原C成员/末坐标商、
所有原尺度和字段分量、全部stage SHA。
明确false：
P/Q_operator_matrices_computed；
general_polar_ideal_or_D_computed；
original_eta_principal_functions_rigidification_or_heights_computed。

完整已成阶段不重算。
公开Actions一日artifact只作紧接消费者的临时传输，
Git/Release不存可重算数据。
