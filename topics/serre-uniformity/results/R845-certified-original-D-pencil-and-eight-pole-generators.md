# R845：原 D 两生成元与原极除子的八生成元实际完成

日期：2026-11-16。状态：**本项实际准确完成；五个加法映射的极理想和原高度继续。**

公开 run **43780953543**、job **133017821468**，source
**a43b6afad1ffdbcb0357eda63b7683df3c5d2c93**，实际数学用时
**14.88603302秒**，43个完成阶段。在原辅助素数
\(\ell=1000000753\)、原第0分裂分支上，第一个参数即成功：
五旧纤维的 \(1360\times1380\) 原评价矩阵实际秩为 **1111**，
选中1111阶子式的行列式为 **633901576**。

因此 R842 的原完整空间 \(H^0(3H-D)\) 已实际给出两截面，
其共同零除子恰是原 \(D\)；结合 R837 的原两锚，得到
原 \(E_y=(y)_\infty\) 的八个完整 Cartier 理想生成元。
这项结论保持完整重数及函数域内的理想嵌入，不只说明支撑或 Picard 类。

## 1. 两个实际原截面与特征零结论

取 R842 原295个准确单位解基
\(w_0,\ldots,w_{294}\)，本次实际选中
\[
a=w_0,\qquad b_D=\sum_{j=0}^{294}w_j.
\tag{845.1}
\]
产物字段把第二截面记为 b；这里写 \(b_D\)，以区别原椭圆曲线常数 \(b\)。
这些截面的特征零定义是原完整矩阵的规范单位解，
当前有限域向量只是该准确对象在原单位素点的约化。
没有把任意有限域核直接当作特征零截面。

在原 \(Y\) 上，\(g=127\)、\(\deg H=272\)，
\(\deg D=395\)，
\[
V_3=H^0(3H),\quad \dim V_3=690,\quad
W_D=H^0(3H-D),\quad \dim W_D=295.
\]
设 \(a,b_D\) 的共同零除子为 \(D+Z\)。已证铅笔公式给
\[
\operatorname{rank}_L\bigl(V_3^2\xrightarrow{(r,s)\mapsto ar+b_Ds}V_6\bigr)
=1111-\deg Z.
\tag{845.2}
\]
本次实际评价子式给该原乘法的特征零秩下界1111，
而(845.2)给上界1111，故
\[
Z=0,\qquad \operatorname{im}\mu_{a,b_D}=H^0(6H-D).
\tag{845.3}
\]
这只用评价秩下界，不假定五纤维避开 \(D\)、纤维约化，
或评价在整个 \(V_6\) 上单射。

因此原两图的完整理想为
\[
I_{D,\tau}=(a/\tau^3,b_D/\tau^3),\qquad
I_{D,\sigma}=(a/\sigma^3,b_D/\sigma^3).
\tag{845.4}
\]
交叠令 \(t=\tau/\sigma\)，两生成元逐项乘 \(t^3\)。
无需展开原295基的大有理坐标。

## 2. 原极理想的八个实际生成元

R805 已逐点证明同一个原整数 Hom \(f_4\) 的极除子
\[
E_y=\mathcal B+3D,\qquad
\mathcal B=\mathcal D_{\rm cusp}+P_0,\quad
\deg\mathcal B=21,\quad\deg E_y=1206.
\tag{845.5}
\]
原 \(D\) 不是另选的线性等价代表。
R837 的准确 \(u,v\in V_2\) 已由真实1213阶子式证明共同零除子恰为 \(\mathcal B\)。

本次 DAG 保留原 \(u,v\) 的稀疏坐标、清分母、content 与尺度，
以及(845.1)的原单位解来源，实际给出
\[
ua^3,\ ua^2b_D,\ uab_D^2,\ ub_D^3,\qquad
va^3,\ va^2b_D,\ vab_D^2,\ vb_D^3.
\tag{845.6}
\]
八项均是原 \(V_{11}\) 截面。在两图分别除以
\(\tau^{11}\)、\(\sigma^{11}\)，生成
\[
\boxed{I_{E_y}=I_{\mathcal B}I_D^3.}
\tag{845.7}
\]
逐个 DVR 中，生成元最小阶恰为
\(\operatorname{ord}_P\mathcal B+3\operatorname{ord}_P D\)，
所以保留原极点的完整重数。交叠上八项逐项乘 \(t^{11}\)。

八个截面以有完整来源的乘法 DAG 给出。
没有为了首一化引入未知标量，没有另取立方根，
也不需要先构造完整 \(V_{11}\) 乘法表或272阶多项式HNF。
它们的函数常数继续保留；取得理想生成元并不自动选择高度的刚性化。

## 3. 本次新增算术及原计算复用

原 R775 power4/5 前690个 recipe 已准确说明
\(F_j^{(5)}=\tau^2F_j^{(3)}\)。
本次直接读取原 R787 的690条已成 real-power5 行，
不重新做 Fourier 乘积、相位或实子域转换。

使用原 R827 同素数的已成1234阶 S5 选行逆，
按30个右端一组共23组求原 \(V_3\) 的正规坐标。
每组均完成全部1380行代回，以及额外权5坐标为零的支撑检查。
原 \(82^{10}\) 公共尺度相消，准确特征零支撑使用原分次自由基定理，
不从一次模零推断。

原节点 \(z=0,1,2,3,4\) 的 \(W\)、Krylov 矩阵及其逆全部复用。
每个节点只新增原 \(V_3/\tau^3\) 的评价 \(E_c\) 和 \(K_c^{-1}E_c\)，
对截面 \(s\) 计算
\[
[s(c),W_cs(c),\ldots,W_c^{271}s(c)]\,K_c^{-1}E_c.
\tag{845.8}
\]
纤维环的交换性保证这是原乘法，不需纤维半单或新的乘法表。

43个完成数学阶段包括：1个来源/alias审计、23个正规转换块及其索引、
5个纤维评价、1个候选截面、固定 \(a\) 的5个乘法、\(b_D\) 的5个乘法、
1个真实秩证书、1个最终理想DAG。
本次首参数1已成功，未执行剩余参数；固定 \(a\) 的阶段保留供必要后继读取。
原 R842 的2451/415/395秩、原两锚、旧S5逆和旧Krylov逆均未重算。

## 4. 实际来源与产物身份

七组来源为 R842、R827、R787、R786、R775、R809、R837，
共 **1979件、108686012字节**的原文件；
展开来源身份 SHA-256：
**45bbe4b4c3605eb7902389e093380306214039a4c3921f1802400d81a71adb71**。
原父 run 即使预算停，也只消费其来源正确的 complete 阶段，
不把失败父回执改写为成功。

| 项目 | 字节 | SHA-256 |
|---|---:|---|
| 核心 R839_original_pole_pencil.py | 38688 | 601b0b5aeb89d3d37ef6f74151f03a15f92cc5724fbb8574cc6c87f533158b4b |
| 封装 R839_pole_pencil_public.py | 38527 | 8be3fb61034da689bbc4bbe8e30f2c69f062c561f034b10a078dc69553fd9e95 |
| 实际请求 R839-pole-pencil-public-request.json | 9789 | caefb388d2b4fb54ee30636b3c6243dac6749e5540817405f7bfbf3aa394a999 |
| 工作流 serre-R839-original-pole-pencil.yml | 5964 | 228ed65fd0b9de146c3969d1edc40624821c6e7fa02a546abb38bf82882bf611 |
| 最终 certificate | 322708 | 1e71a62ce53d64791ed672591d52d792307e3931dbe0eeea78bed42cee266692 |
| 原 D/Ey 八生成元 DAG | 109669 | 9cf17e78cd112ee527fb6b25890d390d8c59305b9854c89bbbbafbef94730352 |
| 参数1真实五纤维秩 | 112852 | d27322523df2482417c5a2bf6b6dbf71fd05df98cbc1d33b826f4b2a926e71ad |
| 参数1原截面 | 113154 | 6cedff0d3c732c376570b0f513549507053b28a054496c83dd7bab6dbbac617b |
| 原 V3 正规转换索引 | 112114 | 19bc45e50852072815408114d0f4c890fcff971368fb94057a26d58d9cd8639a |
| 原来源及alias审计 | 109316 | c1610d318ebe5c9348fb652c0858c8f4494ddaf8c7ad738275db31cb9eae7cd0 |
| 43阶段 manifest | 111028 | 77262bb109e5857f95b489b1244f971e620b8ea37fdcc9bd40d5571fbc8fa4f7 |
| 全输出 manifest，53件 | 9206 | 8bef49bfa53a00f1bdce31c947e030d92ff5abbae15d0115587f9cf869486099 |
| manifest reference | 235 | 06c1bb8788d1fd35206e3bcacdfefdcd7eb41ea8b56629fad6e7dd826c346f2e |
| 1979件必要输入 carrier | 86850835 | c32273b64fc9fea59749ba55432a640c8ebef24af57d119ea7e64386257a42ff |
| 原来源 inventory | 319372 | 026edd5de113efaced85431453a203345e051c275ae68c27475318c0da20b34a |
| 输入 receipt | 11894 | c4a3054a6952421d2195662b0ed92e54588693e124b3d7e51f70a34c0277d180 |
| public-actions-input | 9805 | 2204716ffc09930039c91673a8f3029a36e6df125c5a666ed617593362a88477 |

最终文件名为 p41-original-D-pencil-and-pole-ideal-certificate.json；
理想程序为 R839-pole-original-D-and-Ey-eight-generator-DAG.json.gz；
秩阶段为 R839-pole-candidate-000001-five-fiber-rank.json.gz。
配置 SHA-256：
**d6d7e284ab025a51d5ac0ef13eb99a7cca0205ffde6fcc3f5b2dc35bc48a2bf2**。

源 R842 的原D基为756940B，
SHA ec71c061e59d34bd9e2eb6b38d071b8b53c169443e538956d34e50c6f0e3af60。
R837 两锚分别为3453B/d57929a0075dde31513dbf586c00eabc01619448753578e2363076b21259b01c、
9574B/c827059c209e1b5a80c57e7126b94a182483a83fd511389738ceb38e03959ecd。
这四个截面来源就是(845.6)实际使用的对象。

原 run 于 **2026-11-16T00:33:43.153988+00:00** 结束，
exit0、error=null、outer_timeout=false。
core547B、SHA df08b097bd726b2841f93ac89962d992b149cf36e52d97d10a56d813974b385e；
run462B、SHA 2065900bca623092c68c80c1b6139437ad26a00393e46a56fefc45d403464451。
含初始化的核心总计时14.889077052999994秒。

一日 artifact **14188093176**，名称
serre-global-R839-original-D-pencil-and-eight-generator-pole-ideal-43780953543-1，
**110888459B**，SHA-256
**34f85e3c564929e04eceb0f326353a77acc7010ecaee1df315704a75e315f8c0**，
到期 **2026-11-17 00:33:43 UTC**。
本地以12次Range共5593568字节读取38个选定成员并核原SHA/配置；
没有本地计算秩、正规转换或矩阵乘法，也没有宣称重新hash完整ZIP或86.85MB载体。

## 5. 后继边界

本项完成原 \(I_D\) 的两生成元、原 \(I_{E_y}\) 的八生成元以及两图运输。
既有准确关系
\[
I_{E_{y_R}}=(y^2-b)I_{E_y}^3
\tag{845.9}
\]
需接入原全局 \(y\) 表达式。这里必须正乘 \(y^2-b\)，
因为 \(\mathcal O(-\operatorname{div}g)=g\mathcal O\)；
先前逆乘号已在原证明EP.17更正。本消费者没有把 R844 的CM点值当作全局函数。

原全局 \(y=A/B\) 的单位chart定义已有登记，
后继可直接消费该完整原源，不必等待大有理坐标展开。
五个加法映射仍须给各自准确全局极理想及原函数运输；
\(c_0\) 刚性化、Picard比较、原 \(\eta\) 与高度没有由本项消去。
本次也未计算Jacobian规范代表或八个 \(V_{11}\) 截面的展开坐标。

Git只保上述数学结论、脚本、参数与简明run/SHA；机器数组、节点、
完整证书及carrier只按一日必要artifact续传。已成43个数学阶段不重跑。

## 来源

- [原D铅笔与八生成元证明](../notes/R839-original-D-pencil-and-eight-generator-pole-ideal.md)，
  更正后SHA ccf70498998b7f3bccbce53954d7bae398054d42b16420118530688cf7080827。
- [原五纤维最小执行契约](../notes/R839-original-five-fiber-pole-pencil-method.md)，
  SHA f8bc9d63d80fcfa14747ff76fb0ce0326326ae3c0a5835edeea03cace406c17d。
- [R842原两图短RR与完整D基](R842-certified-original-two-chart-RR-and-D-unit-kernel.md)。
- [R837原固定21点的两锚](R837-certified-original-P0-evaluation-and-fixed-branch-pencil.md)。
- [原全局函数的准确单位chart与CM消费者](../notes/R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)，命题U.1及U6–U9。
