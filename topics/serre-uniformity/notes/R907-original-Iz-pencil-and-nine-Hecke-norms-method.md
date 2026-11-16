# R907：原五个 I_Z 铅笔与九范数的实际消费契约

日期：2026-11-16。本文固定一个可逐方向执行的消费者。它消费 R903 的原完整 128 空间，实际认证原无基点铅笔，在 R885 已成完整 Artin 对应纤维上求九个新范数，并保存两图的准确九生成元理想与原 dual-seven / 两端 determinant-fibre 刚性化表达。未得到的 R903、R901 或其他生产者身份保持 null；没有将待源表达或 z=0 的取值冒作 P0/P1 的数值标定。

数学依据为 R876（2dfd9e33…）、R873（e6401ca8…）、R885（1c67eca3…）、R879（5f0988a8…）、R901（83a18d8a…）和正式 R903（9fcf3c2c…）。每个完整 SHA、路径以及旧数学模块 SHA 均进入实际数学 tag。所有新数学只在公开 Actions；原 W、Krylov、272 目标坐标、参考函数和其九范数不重算。

## 1. 首 scope 与准确输入

固定原曲线 Y、g=127、H 的次数272、原正规次数 (0,1^144,2^127)，以及辅助素点
ell=1000000753、zeta=549966761、s=99932770。原 p=41 对象、level82、-3 下降、原全部整数尺度保持。

R903 的准确空间与嵌入是
\[
 A_j=H^0(3H-D_j-D_\chi-18P_0),\qquad \dim A_j=128,
\]
\[
 \Phi_j=Q_{Z_j}/q_\chi,\qquad
 \Phi_j A_j=H^0(\mathcal M_j),\quad
 \mathcal M_j=\mathcal O(-Z_j+254P_0),\quad \deg\mathcal M_j=254.
\tag{907.1}
\]
这里 \(q_\chi=u_\chi/\tau^2\)，其除子为
\(D_\chi-2H+272P_0\)；\(Z_j=D_j-H+\operatorname{div}Q_{Z_j}\)。
R903 的 normal128 数组是已经按原 \(\tau^3\) 归一的 \(A_j\) 函数，不再次除 \(\tau\)。
它们是准确 unit-solve 基的合法约化，不能冒充已经展开的特征零系数，也不能称为 K 或 Q 固定基。

参考空间直接沿 R879：
\[
 \mathcal M_0=\mathcal O(254P_0),\qquad (u_0,v_0)=(1,f/u).
\tag{907.2}
\]
其无基点性和恰254阶极点已实际认证，不重求参考128基或参考672子式。R885 在 z=0 已成的参考值和九范数直接读取。

首请求可只做一个指定原方向；同一核心支持方向1至5及同一参考。只完成部分方向时，证书明确列出真实完成者。不存在“模零即 inactive”的出口。

## 2. 816×836 的实际铅笔矩阵

取 R903 的原未缩放 P0 单位列为 \(a\in A_j\)；按确定性正整数次幂组合
\(b(T)=\sum_{i=0}^{127}T^i a_i\) 搜索另一列。实际截面是
\(u=\Phi_j a,\ v=\Phi_j b\)。每个整数 T 保留准确整数含义，不将其模代表改成其他特征零系数。

原 R876 的 Koszul 公式给
\[
 \operatorname{rank}[uV_2,vV_2]=672-\deg Z_{\rm common},
 \qquad \dim V_2=418.
\tag{907.3}
\]
共同非零 \(\Phi_j\) 在函数域中可取消，所以同一秩等于
\(\operatorname{rank}[aV_2,bV_2]\)。这允许铅笔检验直接消费原 normal 数组；不必先在所选源纤维求 \(\Phi_j\)。

每个节点保留完整
\(A_z=\mathbf F_\ell[X]/\chi(z,X)\)，维数272，包括全部不可约因子、重数和幂零元。原 K 逆和 V3 评价均已完成；V2 评价是按原 (normal-row,z-power) 顺序从 V3 中准确抽取的418列，没有再乘82尺度。新算术是 a、b 的评价和各自418个完整乘积。

三个不同旧节点给816×836矩阵。程序实际选672列与672行、保存单位逆和两乘回，才认证无基点。这里**不预先使用“816>798 自动单射”**：若纤维遇到固定除子支撑，作为普通函数的评价仍给原乘法图的一个线性复合；实际672下界与(907.3)的672上界已经足够。它不需要假设所取消的 \(\Phi_j\) 在三个源纤维为单位。

缺秩只推进到有限 schedule 的下一个三节点组合或整数参数；有限前缀耗尽不是原无基点铅笔不存在的证明。固定 a 的已成乘积按节点保存，各 trial 不重做；b 的已成节点乘积也按实际整数参数保存。

## 3. 完整 q*Phi 的真实来源闭包

R903 保存的 R901 原输入 carrier 只使准确主函数树可追溯，并不自动包含 QN 的全部可求值叶。R907 还明确消费原 R899 input inventory/carrier：

- 原七组 \(a_k,v_k\)，共同 \(q_C,q_\chi\)；
- 原 R894 十六个 flip 和原 R890 两个共享 flip 的未缩放 u；
- 原 QN 的完整 principal/DAG 与各原生产者元数据；
- 如 R899 已生成 a0 的完整 V3 多项式，直接读取；否则只由原 R845 五个已成完整纤维值，以前四点作唯一 V3 插值，并在全部第五点及逐行权界乘回。不会重做旧 a0 的 V3 转换或旧纤维乘法。

这些叶给原
\[
 \widetilde Q_k=(a_k/v_k)^3q_Cq_\chi^{-4},\qquad
 Q_N=\Bigl(\prod_{k=0}^{6}\widetilde Q_k\Bigr)F_N.
\tag{907.4}
\]
每个 flip 仍按
\(F_{\rm new}=(qF_{\rm left}F_{\rm right})^{-1}\)，重复父项必须出现两次。
R900 给 \(Q_K=Q_Nw_0/v_K\)，其中 w0、vK 已是原 tau-normal 函数。
R896/R902 的原七共轭给
\[
 Q_{j,k}=(B_{j,k}/v_{j,k})q_\chi^{-(n_j-2)},\qquad
 Q_{Z_j}=F_j\Bigl(\prod_kQ_{j,k}\Bigr)^{q_j}Q_K^{-p_j}.
\tag{907.5}
\]
这里 B 坐标已经除原 \(\tau^{n_j}\)，v 坐标已经除 \(\tau^3\)，不再乘一次 \(\tau^{3-n_j}\)。
R902 的真实次序为 [0,6,1,2,4,3,5]；各叶必须绑定实际 sigma power、原分支和同 s 根。

核心把(907.4)–(907.5)编成保来源的有限乘、逆、整数幂 DAG。旧126 flip、旧16 flip及所有空间不重算。每条叶引用原 producer、完整 source spec、字段和准确 unit-solve 身份；新有限域值单列，绝不替换准确定义。

### 3.1 原载体与 namespace 合同

R899 的真实 inventory 名为 \(\texttt{R899-original-source-inventory.json}\)，receipt 为 \(\texttt{R899-retained-inputs-receipt.json}\)，carrier 为 \(\texttt{R899-retained-original-inputs.tar.gz}\)。全部成员先按其原 inventory 逐 bytes/SHA 核实，再只把本计算需要的原成员装入 R907 新载体；原包的 hash 仅记运输历史，不能留作缺文件的 live dependency。原 source-audit 的 inputs 对象逐字进入 R907 的 QN_inputs，原 identity、配置和每条函数叶均保持。R899 已成插值文件的确切名字是 \(\texttt{R899-zero-branch-a-normal-polynomial-from-old-five-fibres.json.gz}\)。

R903 的 carrier 用于恢复 R901 的原输入 carrier；R901 自身的新126个 u 依其实际 manifest 只取需要的叶。R885 完整 Artin 生产者的 carrier 名为 \(\texttt{R885-Artin-retained-original-inputs.tar.gz}\)，只提供已成原参考、correspondence DAG、必要原元数据等；目标17块仍从同一真实生产者输出读入。它在 R907 的 source_group 明确命名为 ARTIN，避免与 R899 原来名为 R885 的多项式/特征式生产者发生 namespace 混淆；两者 result/core/run 均不更改。全部运输路由只从已绑定实际 producer 的原请求或本次明确请求取得。

预算或方向前缀不进入数学 tag。为此准确全五方向的函数程序一次固定编译；只对请求方向作新矩阵和 Norm 算术，后来扩展方向不覆写同名的较短函数程序。

## 4. 复用原 R885 的整个对应代数

对每个实际已完成的 R885 源节点，直接读取
\[
 A=\mathbf F_\ell[X]/\chi(z,X),\qquad
 E=A[U]/(P(U)/a_8),\qquad \operatorname{rank}_A E=8,
\]
以及原 \(q^*z=U,\ q^*w=K(U)/P'(U)\)、17个目标正常块
\(\gamma_i=q^*\beta_i\)、全部272条完整 E 乘回和参考九范数。

当前已成的是 z=0，**它不是原 P0 或 P1**。没有已成的其他目标节点就不填写其数据，也不为本消费者重放原 adjugate 计算。若该节点上新的 Phi 分母不是整个 E 的单位，保存完整失败见证；可消费以后真正完成的其他 R885 节点，不能删掉失败因子。

任意已成 normal 多项式
\(\sum c_{ik}z^k\beta_i\) 在 E 中按
\(\sum c_{ik}U^k\gamma_i\) 评价。原归一尺度只施一次。
所有除法由原 R885 helper 的完整8阶范数和 A 上多项式 xgcd给出，保存整个2176坐标乘回。零因子或非单位不被当作域中可逆元。

对 Φ 的每个出现分母必须通过该全 E 单位证。Φ 本身无需是单位；它的范数允许是零因子。该条件只说明这个具体有理表达在此有限纤维能直接求值，不否定特征零函数。

## 5. 不假设铅笔首项可逆的一次九范数算法

令 \(a'=q^*a,\ b'=q^*b\)。在完整 A 上构造两个8×8乘法矩阵，
\[
 M(T)=M_{a'}+TM_{b'}.
\]
在交换环 A[T] 中作一次除法自由 Berkowitz：
\[
 \det(XI-M(T))=X^8+c_1(T)X^7+\cdots+c_8(T),
 \quad \deg c_i\le i.
\tag{907.6}
\]
只保 T 的0至8次是严格完整的次数范围；这不是以截断掩盖高次残差。
在 E[T] 中对 \(a'+Tb'\) 作完整 Cayley–Hamilton 乘回，核全部9×8×272标量坐标。
所得
\[
 d(T)=c_8(T)=\operatorname{Nm}_{E/A}(a'+Tb')
\tag{907.7}
\]
准确次数至多8，无须 a'、b' 或某个 a'+tb' 在整个 E 上为单位。

另对 \(\Phi'=q^*\Phi_j\) 求一次8阶乘法特征式并完整乘回，取偶数秩范数
\(c_\Phi=\operatorname{Nm}_{E/A}(\Phi')\)。
九个完整值为
\[
 N_{j,t}=c_\Phi\,d(t),\qquad t=0,\ldots,8.
\tag{907.8}
\]
这是原 \(u_j+tv_j\) 的范数，正乘因子不能省略。
不重做参考九值，不另算九次行列式，不假设 A 半单或分裂。
每个完成 stage 保存其原来源、整个 A/E 维数、全乘回和准确参数。

## 6. 两图完整理想与原 Hecke 方向

实际672证书给真正全局生成的两截面，故原 R876 定理适用于同一准确函数。
以原 generic frame 1，定义
\[
 J_j|_{U_c}=\sum_{t=0}^{8}R_c\,
 N_{K(C_7)/K(Y)}(q^*(\Phi_j(a+tb))),\qquad c=\tau,\sigma.
\tag{907.9}
\]
这里每个 norm 是准确原函数域中基 \(1,U,\ldots,U^7\) 的乘法行列式表达，有限域值是其在已认证纤维的单独约化。
同一九函数同时给两图，不通过删去 a8、P'、r0 的零点来定义理想。
九生成元完整性的根据是真无基点及有限平坦映射，故包含全部分歧和剩余域次数。

公共参考 J0 同样按 R879 的 (1,v0) 和原 R885准确norm program绑定。
输出两图
\[
 \mathcal H_7(I_{Z_j})\simeq J_jJ_0^{-1},\qquad
 J_0^{-1}=\{x\in K(Y):xJ_0\subset R_c\}.
\tag{907.10}
\]
这是完整分式理想表达，**不把9个生成元的倒数之和误作逆理想**。
后继若需材料化Hermite/degree-zero RR，须实际执行相应完整格运算；本消费者不宣称已完成那一步。

直接算术方向为 \(\operatorname{Nm}_{\pi_s}\pi_t^*\)。
冻结原 Hecke 方向 \(\operatorname{Nm}_{\pi_t}\pi_s^*\) 只沿原 R873 canonical dual7运输：
\(\pi_s\jmath=\pi_t,\ \pi_t\jmath=\pi_s\)，两次对偶的 scalar7 在原 level82 G 中，无剩余 diamond。
分子 determinant 与分母 determinant 同时运输，原 -3 下降及两条帧保全，不以自伴随性代替该同构。

M_j 的 Q 定义由原 I_Z、原 P0 与真实下降 datum给出。
选用 L 上的铅笔不会改变由全部九范数生成的完整理想；其下降由同一个原线丛和范数自然性唯一给出。
没有声称所选128基、两截面或单独九函数已是 Q 固定数组。
原 real_descent 立方理想不在本 scope。

## 7. P0/P1 的准确表达与尚未完成的数值

保原
\[
 e_{j,0}=t^{-7(p_j-q_j)},\quad
 m_{j,0}=t^{-7(p_j-q_j)-254},\quad m_{0,0}=t^{-254}.
\]
R903 的原未缩放 P0 单位列及其 c 幂原值用于铅笔第一列，不将其设1。
原 P1 帧继续沿 RF/R849，不从 P0 单位推 P1 单位。

对 \(\alpha=0,1\)，端点对象准确保存为
\[
 \det\bigl((\pi_{s*}\pi_t^*\mathcal M_j)\otimes\kappa(P_\alpha)\bigr)
 \otimes
 \det\bigl((\pi_{s*}\mathcal O_{C_7})\otimes\kappa(P_\alpha)\bigr)^{-1},
\tag{907.11}
\]
再与 j=0 的同一 determinant 对象相除；原 dual7 在这些纤维上也同时运输。
对 P0 施 \(\operatorname{Rig}_{P_0}(L)=L\otimes L(P_0)^{-1}\)。
不能把源 z=0 的 E 代入(907.11)，也不把形式 determinant 表达称为已求出的标定矩阵。

本 scope 明确输出：
P0_endpoint_numeric_calibration_computed=false，
P1_endpoint_numeric_calibration_computed=false，
endpoint_transition_scalars_set_to_one=false。

为后续实际端点消费者保留的最小契约是：每个原端点的完整长度8有限平坦纤维代数；原 q*Mj 与 q*M0 的8维局部模块及真实帧；九截面的整个模块值；对应 determinant 分子/分母的8×8转移矩阵；原dual7在同模块上的运输；原 t 与P1参数/原帧身份。若 primitive P/P' chart在端点坏，须以真实正则化/局部饱和给该完整rank8数据，不能丢掉非单位分量。所有这些未成字段为 null，完整 nilpotent/剩余域次数继续保留。

## 8. 原子输出、来源和恢复

新 RESULT 为 R907-original-Iz-pencils-and-nine-Hecke-norm-generators；
FINAL 为 p41-original-Iz-pencils-and-nine-Hecke-norm-generators-certificate.json。
输出 R907-*.json.gz；current明确complete=false。

同一原节点的固定 a×V2、每trial的 b×V2、816矩阵、672minor、准确铅笔、函数图编译、每个整E叶值/逆、符号Berkowitz层、完整CH、Phi范数、九值、两图ideal/两端表达分别原子保存。
共享 QN/QK/flip 叶按真实来源哈希只评价一次。已成参考、K、target row和所有旧数学只读。

数学tag包括新 core/helper/method/原 helper SHA、全部源BASE/config/选件指纹、准确source输入与固定算法策略；预算、有限trial/方向前缀只作可续控制。
失败current/falseFINAL不冒完整；只验证当前真正存在的完成stage。
恢复同tag，不把旧stage改贴新身份。所有原未缩放标量和准确定义继续存在。

实际成功按方向至少要求：真672、完整Phi合法求值、整个E上的符号CH、九个全A范数，以及同一准确铅笔的两图ideal/dual7/frame表达。
它不要求尚未执行的端点数值、Hermite或Picard支持，也绝不设置其成功旗标。
源码、方法、参数可入Git；机器数组与原始数学来源只在一日artifact/carrier中续存。

