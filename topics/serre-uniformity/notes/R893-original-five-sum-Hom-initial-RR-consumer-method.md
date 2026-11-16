# R893 原五个正和 Hom 的完整初始 RR 消费方法

本方法执行已发表的 R893 证明，固定原曲线、原 -3 下降、原 T、原 rho_j 与原整数尺度。首 scope 是五个 g_j=(1+T^j)f 的完整初始关系核。所有新算术仅在指定公开仓库的 Actions 中执行。数学结果名为 R893-original-five-sum-Hom-complete-initial-RR。

主要证明为 [原完整纤维与 Schur 证书](../results/R893-original-five-sum-Hom-full-fiber-and-initial-RR-Schur-certificates.md)，SHA256 为 91ce6834bda528976265a331fe0c987f4350049e7b228f1cc6c77e0a69142416。独立数学核心为 scripts/R893_original_five_sum_Hom_initial_RR.py；标准库包装器不导入数学核心，也不执行有限域运算。

## 1. 实际来源和尺度

公共辅助素数固定为 1000000753；同一剩余域中的 B 根为 3197390，s 根为 99932770，zeta 根为 549966761。这里 B=lambda*b、s=1+2*zeta，原 b 模型仍由原 R781/R787 field 描述指定。保留其 280 维来源描述；本次正规向量的系数域仍为原 14 维 L。

| 来源组 | 实际消费对象 | 本次不重复的已成算术 |
|---|---|---|
| R849 的真实 R839 producer | 原 523 节点全局函数与五极理想 DAG、五个 rho_j、真实极次数 | 全局原关系、Norm 与三射影 minor 证明 |
| R880 七共轭 normal producer | 已成七支索引及六个新 A/B 对 | 12 个 S5 RHS、原完整 1380 行乘回 |
| R877 与 R827 | 原零支 A 与 B | 零支 S5 解 |
| R809 | S5 基序、六个 C_j 的 12 个准确坐标组 | 六个准确有理重构及全部 1380 行验证 |
| R827 | 原 W、place、g 与 Gamma 的各 17 个 16 行块、完整身份、八个旧 Krylov 点 | 原算子与旧逆 |
| R885 polynomial producer | 已成整 chi(z,T) 和原 0 至 7 节点关系 | 273 节点特征多项式生产 |
| 已成 six-Dstar producer | sigma^1 至 sigma^5 的原 B 一阶导数小阶段 | 相应 Gamma B、F1/F2 与 Hasse 插值 |

七支的真实顺序是原 branch [0,6,1,2,4,3,5]。读取顺序由七支索引的 sigma_power 确定，绝不以 b 根的大小代替 sigma。six-Dstar 的 branch-NN 是原 branch 编号，其 source 原样绑定同一 A/B pair。

R809 的每组准确系数按 numerator / denominator * original_target_rational_scale 恢复并在原 b,s 基评价，各尺度只施一次。S5 的 integer_scale=82^10 是原 e 基固有尺度，不再乘除。同一原 theta*U_j/tau^4 比值已经含原 Hom 的相位，不再插入第二个 rho_j 修正。

本次输出源绑定的特征零 unit-solve 表达式及其模像，不把模数组称为已展开的特征零坐标。本次不求标记第二截面、padding、完整 418 空间、五个 L_j 的 128 空间、Picard 支持或高度。

## 2. 已成导数与仅有的新导数

原 R827 已保存零支 delta B 的 C 基第 0 列。其 C 基为前 271 列 e_i-q_i e_271 与末列 P e_271。因此原完整 normal 向量为
\[
v_i=c_i\quad(i<271),\qquad
v_{271}=P c_{271}-\sum_{i<271}q_i c_i.
\]
本次只进行这一准确基运输，不再算零支 Gamma B。输入的完整 monic 除法和原 normal 乘回证明仍属于原 R827 stage。

非零五支的 B 导数直接读取 six-Dstar 已完成小阶段中的 delta_B_coefficients_mod_prime[8][272]。它们是已成 F1 的第 0 列，原 beta_0=1 且 delta(beta_0)=0。本次保存真实 source ref，不把原阶段改标签。

仍须计算的仅为六个 A 导数，即 sigma^0 至 sigma^5：
\[
\delta a=\Gamma_\tau a+M_g\,\partial_z a.
\]
两个原算子按实际 17 个 16 行块直接读取。每块同时处理全部新 RHS，独立原子保存；输出权界 7-epsilon_i 的高次项必须全零。已完成的块在同一 tag 恢复时只读，不重算。

## 3. 一个整分母与完整 272 维纤维

沿 R893 定义
\[
C=\rho_j^{-3}\sigma^j A,\quad D=\sigma^j B,\quad
F=A^2-bB^2,\quad F_j=C^2-bD^2,
\]
\[
W=B\delta A-A\delta B,\quad W_j=D\delta C-C\delta D,
\quad R=C_jF_jW,\quad S=C_0FW_j,\quad
\Delta=R-S,\quad \Xi=CB-AD.
\]
原正和映射的 y 函数为
\[
Q=BD^3\Delta^3,\qquad
P=-AD^3\Delta^3+\Xi D^2\Delta^2(2S+R)-\Xi^3C_0^3F^2W_j^3,
\qquad y_{g_j}=P/Q.
\]
原 F 只约去一次，两截面同权 98。直接 sigma 公式权 95，真权 98 的运输另乘 t^3；normal 基按 t^epsilon_i 运输。本次 tau 纤维计算不另生成一套 sigma 算术。

节点依次为 a=0,1,2,...。完整纤维使用
\[
A_a=\mathbf F_{1000000753}[T]/\chi(a,T).
\]
旧 0 至 7 节点的 K、逆与已成 k_272 关系全部原样读取。新节点才算 K 和逆；原 chi 只求值，不重新求特征多项式。K 必须在整个 272 维基上可逆，并核两乘回及完整特征关系。

对 Q 使用整 chi 的 xgcd。只有 gcd(Q,chi) 为非零常数时才接受该完整纤维，随后准确核 QQ^-1=1 及全部 272 个 Qy=P 坐标。不能丢弃失败因子、去掉重数或用一个剩余域点代替整个 Artin 代数。不额外要求 C0、F、Wj 为单位。节点不足或一个真实单位条件失败只记该充分测试未成，不推特征零不存在。

## 4. 三个标量插值块消去 A

按原 normal 顺序 (i,k)、0<=k<=n-epsilon_i，令 E_n 为全部已选纤维评价。原关系矩阵是 [E_n,-YE_n]，H=YE_n。对输出 normal 行 i，只取前 m_i=n-epsilon_i+1 个节点恢复其多项式。因 epsilon_i 属于 {0,1,2}，只需长度 n+1、n、n-1 三个标量 Vandermonde 逆。这些逆用 Lagrange 明式形成，并核左右乘回及全部节点插值矩阵。

消去 A 后，
\[
S=H_R-\Lambda H_I.
\]
每 16 个 normal 输出行形成一个完整 Schur 块，保全部原节点标签与原列标签。不求新的大型 A 逆，也不重复原乘法算子。

| j | n | 极次数 e | 完整节点数 | Schur 形状 | 完整 B 核维数 |
|---:|---:|---:|---:|---:|---:|
| 1 | 12 | 2970 | 23 | 3118 x 3138 | 168 |
| 2 | 8 | 1674 | 15 | 2030 x 2050 | 376 |
| 3 | 8 | 1800 | 15 | 2030 x 2050 | 250 |
| 4 | 13 | 3024 | 25 | 3390 x 3410 | 386 |
| 5 | 14 | 3339 | 27 | 3662 x 3682 | 343 |

R893 的独立 RR 维数与完整纤维注入给出特征零秩恰 e。程序先用 S^t 的左至右 RREF 选择真实原行，再在这些行上选原列，保存所选 e 阶 minor 的非零行列式。全部非主元原列为自由恒等坐标：
\[
B_J=-S[I,J]^{-1}S[I,F],\qquad B_F=I.
\]
实际数组须满足全部 Schur 行乘回。非零 minor 加已证特征零秩证明该 unit-solve 是完整原核；有限域数组只是这个确切表达式的约化。

## 5. 所有原关系与后继最小接口

通过同三个标量插值块从 yB 恢复 A，然后在全部已选完整纤维核 A-y_gj B=0。这一步保每个核列，不能只验证一条候选。每方向同时保存全部 B 系数和每个节点的 272 x r B 评价、yB 评价及完整原关系零证书。

成功方向的输出是 H0(nH-E_gj) 的完整源绑定基。后继 R896 应在同一 B 空间内选两条截面，读取已保存的完整纤维评价。它不能改用高次数的 A 与 B 一对，也不能用本次节点数作 V_(2n) 注入。本次程序只保存消费接口，不执行后继产品核、padding 或除子标准化。

## 6. 来源、恢复与失败状态

标准库 wrapper 的各组来源保真实 producer/result/core/configuration。完整原 manifest、public input、run/core receipt 与成功 certificate 均按真实字节核。R827 的历史预算停止按真实完整阶段与退出码 124 读取；其没有成功终证书的事实不改变。

R885 的 15 件旧 R827 载体与新的 g/Gamma 最小 intake 只作传输，原各成员身份不改。所有新增 source files 清单在公开 prepare 中从固定 manifest 展开并进入数学 tag。R809 证书 spec 若仅给原文件名，严格从已 pin 的完整原 manifest 取真实 bytes/SHA；不会猜其字节或绕过原 core receipt。

同 tag 的每个 complete stage 是原子、不可变对象。R893-current.json.gz 是唯一可变进度且 complete=false。stage manifest 以实际成员内容 hash 命名。旧 false FINAL 是历史终点，不约束已推进的 current；true FINAL 的全部引用仍须与当前完整成员准确一致。预算、最大节点数和请求方向是运行控制，不进入数学身份；来源、相位、固定算法、所有 input refs 与核心 SHA 都进入。

预算停止返回 124；有限充分测试未成返回 2；错误返回 1。所有已成原子阶段都保留。外 wrapper 超时为预算加 900 秒，先 SIGTERM，短宽限后 kill，仍写真实退出码、manifest 与一日 artifact。Git 只保存源码、参数、纸面证明和简明运行/SHA 登记；机器向量、矩阵与回执均在一日 active artifact/carrier 续传。

## 7. 唯一成功出口

某方向只有在完整节点数、整 Q 单位、真实 e 阶单位 minor、全部 Schur 核乘回、全部原 N x 272 关系和自由恒等坐标均完成后，才置 complete_initial_RR_space_certified=true。全部五方向通过才置 all_five_complete_initial_RR_spaces_certified=true。核心与 wrapper 均保持展开坐标、标记截面、五 L_j 的 RR128、Hecke 支持、period 与 height 旗标为 false。
