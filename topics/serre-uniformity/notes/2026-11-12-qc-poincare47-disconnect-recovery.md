# 断线恢复：层 41 的限制代数、实际 Poincaré 左逆与 47 进对数

日期：2026-11-12；负责：qc_global；基础提交：9069e3b8c724368b9b6473b359d8527ed0c5f839。

**状态：本笔记是从断线前已经读取的完整日志、脚本及数学记录恢复的检查点。没有重造或冒充丢失的 gzip 二进制。** 下列三个 Poincaré 证书在断线前真实生成；前两个阶段已完成独立验证，最后的非零纤维左逆完成主计算及全核/下降检查，但独立完整重算尚未运行。其二进制和部分源码当时尚未推送。应先检查恢复磁盘；若已丢失，按下述算法从已发布的 R102、R110、R112、R117 重算，不用旧 SHA 代替实际运行。

本笔记不宣称算出了非主局部高度，也不宣称完成了二次 Chabauty 或统一性。

## 1. 已发布、可直接重用的基础

工作目录为 topics/serre-uniformity；以下路径均相对此目录。

- scripts/data/p41_makdisi47_certificate.json.gz：SHA256 c6ea2f89f4f64eec78039c5b14b6835295b045ea24ae26f885c4047b21e96222。
- scripts/data/p41_cusp_divisors47_certificate.json.gz：SHA256 ae902f25e6d3674b6d474a70ee12a925c0934c198eff94581cfd5dbba30023fb。
- scripts/data/p41_cm4_divisor47_certificate.json：SHA256 f98b13cbc7afb3ed5d8b2f9249fbe815198b478b23559c319c5ba56b6bd83540。
- scripts/data/p41_group47_checkpoint.json.gz：SHA256 4f982a4801332f9eff196ff9e9f866883b01014579896c20e65d044530b8b655。
- scripts/data/p41_group_operations47_certificate.json.gz：SHA256 6907acf2499d48657e32d07657768d3212329a267ace812377d2172ddfa4f5a6。
- 9069e3b 中完整保存了 820 个评价点的一阶 jets、54 方向 Abel 切向校准、PicChart、实际长乘源码及 95 位固定快照。不要把未推的 155 位快照当作保底。

固定
\[
 q=47^4=4879681,\quad R_2=(\mathbb Z/q)[i]/(i^2+1),\quad
 \mathcal L=K+D,\quad \deg\mathcal L=126,\quad g=54.
\]
V_n=H^0(X,\mathcal L^n)，维数依次为 73、199、325；所有值取在同一 820 点集合 T。W、V2、V3 是 R117 的实际评价基。f 是 R110 固定的实际典范截面，
\[
 D_0=\operatorname{div}_{\mathcal L}(f)=K_f+D.
\]
R112 的
\[
 E_B=K_f+Z_{-4},\qquad B=[E_B-D_0]=[Z_{-4}-D]
\]
是保留挠点的整数除子类。R117 实际负点由截面 s 给出
\[
 \operatorname{div}_{\mathcal L^2}(s)=E_B+E_-,\quad [E_--D_0]=-B.
\]
其第二截面记 t；残余除子与 E_- 不交。s,t 的 73 个系数储存在已发布 group47 checkpoint 的 negative_flip_section_seeds_and_coefficients，先乘 Bcoords 转到 V2 的 199 维坐标。

原主范数测试中的实际有理截面 u,v 属于 V1；其系数也在同一已发布 checkpoint 的 norm_section_seeds_and_coefficients 中。记 D_v=div(v)。u,v 在相关支持上的单位性必须逐范数验证，不能只因在 T 上不为零便推出。

调用已发布接口：

- p41_group_operations47.load_sources(data_dir)；
- make_model(sources) 得到 W,A1,tau,V2,P2,A2,V3,P3,A3,B,WB,AB；
- replay_negative(M,sources[3]) 得到 E_- 的 199×73 理想坐标和下降矩阵；
- p41_r2_matrix 提供精确整矩阵运算。

NumPy int64 的统一整行界为
\[
 2\cdot820(q-1)^2=39050494119936000<2^{63}.
\]
有限代数多项式卷积的相应界仅需 2·126(q−1)^2。每次矩阵乘法后先模 q，再进行下一次乘法；不能将多次乘法未经约化串入一个整数累计。

## 2. 实际限制商与行列式范数

对实际有效平坦除子 E，deg E=126，设
\[
 I_E=H^0(\mathcal L^2(-E))\subset V_2,\quad \dim I_E=73.
\]
先用 V1·I_E 的真实乘积构造
\[
 U_E=H^0(\mathcal L^3(-E)),\quad \dim U_E=199.
\]
选择 199 个真实乘积，检查其 199 阶单位子式及全部评价恒等式；因包含关系和 Riemann–Roch 维数已知，Nakayama 给出整个整格，毋须假定未检查的乘法满射。

取商坐标
\[
 Q_2:V_2\longrightarrow V_2/I_E,\qquad
 Q_3:V_3\longrightarrow V_3/U_E.
\]
两个商均为秩 126 自由模：相应 H^1 消失，因为 deg(L²−E)=126>2g−2，deg(L³−E)=252。对 a∈V1，乘法给实际方阵
\[
 F_a:V_2/I_E\longrightarrow V_3/U_E.
\]
若 F_v 为单位矩阵，则 v 在 E 上不消失，且
\[
 \operatorname{Norm}_E(u/v)=\det(F_u)/\det(F_v).
\]
这正是有限代数 O(E) 上乘以 u/v 的行列式；包含所有几何重数，不需要将 E 分解成点，不要求 E 约化或 étale。

已完成的三个实际范数是：
\[
\begin{array}{c|r}
E&N_E(u/v)\pmod q\\\hline
D_0&3467725\\
E_B&708004\\
E_-&4763767
\end{array}
\]
并且
\[
 708004/3467725=4666447\pmod q,
\]
与 R117 直接在 CM 点和尖点上计算的 N_{Z_{-4}-D}(u/v) 完全一致。

原路径：

- scripts/p41_poincare_norms47.py；
- scripts/data/p41_poincare_norms47_checkpoint.json.gz；
- 原 gzip 1,655,540 bytes；
- 原 SHA256 c9c6698068f2e9225fc043d8ba1275dfd678ba53f13fe9ba5f22d791b5c7c7cf；
- 原运行日志 /tmp/serre-p41-poincare-norms47.log。

norm_data(K,u,v,M,rng) 的证书记录：199 个三次乘积指标、单位逆矩阵、商坐标 Q2/Q3、F_u/F_v 的行列式和范数。determinant 返回 None 只表示当前单位消元不能认证为单位，不能解释成实际行列式等于零。

## 3. 无分解的实际单生成限制代数

在 F_v 为单位时，令
\[
 M_g=F_v^{-1}F_g,\qquad
 {\bf1}=Q_2(v^2).
\]
依次生成 Krylov 矩阵
\[
 \mathcal K=({\bf1},M_g{\bf1},\ldots,M_g^{125}{\bf1}).
\]
实际单位行列式证明这些就是 O(E) 的整基。若
\[
 M_g^{126}{\bf1}=\sum_{j=0}^{125}c_jM_g^j{\bf1},
\]
则
\[
 O(E)\simeq R_2[T]/(T^{126}-\sum c_jT^j),
\]
T 对应 g/v。这不是仅按维数拟合一个代数：M_g 来自真实限制乘法，1 来自真实截面 v²，单位 Krylov 矩阵是实际同构。

三个评价映射为
\[
 \Phi_2=\mathcal K^{-1}Q_2,\quad
 \Phi_3=\mathcal K^{-1}F_v^{-1}Q_3,\quad
 \Phi_1(s)=\Phi_2(vs).
\]
它们分别给 s/v²、s/v³、s/v 在 O(E) 中的多项式坐标。验证全部 199 个实际二次基单项式及全部 325 个三次基与乘法兼容，不能只检验选中的少量点。

D0 和 E_- 可用 g=u；E_B 在原确定性搜索中用第二个候选截面。原证书保留具体 g 系数和 Krylov 逆矩阵，不能将“第二个候选”当作代替系数的数据。

对任何单位代数元素 a，Norm(a)=Res(m_E,a)，也等于 126×126 乘法矩阵的行列式。独立验证器用 Python 整数对求 Euclidean resultant；若中间首项非单位，不能错误判作范数非单位，改用纯 Python 单位主元行列式。后一分支在 E_- 的三次范数上真实触发了两次，最终全部通过。

额外实际值：

- 原负点第二截面 t 满足 N_{E_-}(t/v²)=1412636，单位，因而 E_B 与 E_- 不交。
- 一条实际有理三次截面（原证书包含完整系数）的范数在 D0、E_B、E_- 上依次为 3330941、2815947、4082331，均在基域中且为单位。
- 所有 R2 输出的虚部均按实际下降检验，而非四舍五入丢弃。

原路径和已观察状态：

- scripts/p41_poincare_algebras47.py；
- scripts/verify_p41_poincare_algebras47.py；
- scripts/data/p41_poincare_algebras47_checkpoint.json.gz；
- 原 gzip 386,987 bytes；
- 原 SHA256 6dde252c77baac044b5ddde820c771226b6dee7e7fdc72e3131d3b3b1ed8b365；
- /tmp/serre-p41-poincare-algebras47-verify.log 最后明确显示三个限制代数及独立 resultant 范数全部 PASS，并重得 R117 的 CM 乘积范数。
- 生成器及独立验证器当时均已结束。最后一次读取日志发生在环境断线前。

## 4. 真正非零 Poincaré 纤维中的左逆

采用 Poincaré 规范
\[
 \mathcal P_{[A],[B_y]}=N_A\mathcal O(B_y).
\]
有理截面 1 在不交支持上给标准坐标。取
\[
 A=E_B-D_0,\qquad B_y=E_--D_v.
\]
它们代表 (B,−B)，且真实支持不交：

1. v 在 D0、E_B、E_- 上的单位范数保证 D_v 与这三个有效除子不交；
2. N_{E_-}(t/v²) 为单位，保证 E_B 与 E_- 不交；
3. 新实际计算 N_{E_-}(f/v)=2436042 为单位，保证 D0 与 E_- 不交。

从铅笔 a=t+k s 选截面。原运行 k=0 即成功，所以 a=t。
设
\[
 \operatorname{div}(a)=E_B+E_a,\qquad
 A'=E_a-D_0,\qquad
 \psi=a/f^2.
\]
于是 div ψ=A+A'，且 [A']=−B。由范数单位性验证 E_a 与 E_-、D_v 不交。

E_a 的实际理想通过 s/a 的完整翻转核计算：
\[
 R=(s/a)V_2-V_2\big((s/a)V_2\big)[P_2],
\]
rank R=126，kernel rank73；全部 820 行为零及完整 Frobenius 下降均检查。不能仅按类公式记一个虚构的负点。

在第一变量中相乘后，O(A+A')=O(divψ) 的规范平凡化把有理截面 1 送到 ψ，故两个标准坐标的乘积在零纤维中的坐标是 ψ(B_y)。因此坐标 1 的左逆，在代表 A' 中的坐标严格为
\[
 \lambda=\psi(B_y)^{-1}
 =\frac{N_{D_v}(a/f^2)\,N_{E_-}(f/v)^2}
 {N_{E_-}(a/v^2)}.
\]
这给出范数算法到真实双扩张群律的连接，含符号；不是仅由数值猜测符号。

D_v=div(v) 的限制代数以 f 为分母构造。f 在 D_v 上为单位；取 I_{D_v}=vV1，重复第2–3节，因此不需要更高的 V4/V5。

实际输出为：
\[
\begin{aligned}
N_{E_-}(f/v)&=2436042,\\
N_{E_-}(a/v^2)&=1412636,\\
N_{D_v}(a/f^2)&=1311028,\\
\lambda&=149764,\\
\log_{47}\lambda&=4140042=47\cdot88086\pmod q.
\end{aligned}
\]
用 log47(47)=0、Teichmüller 单位对数为零：
\[
 \log\lambda=\frac1{46}
 \left(w-\frac{w^2}{2}+\frac{w^3}{3}\right),\quad w=\lambda^{46}-1,
\]
模 q 精确成立。程序另核 λψ(B_y)=1。

这些数值是**实际双扩张坐标修正**。尚未选择并计算一个非主高度的 log splitting；不把 4140042 标作 h(B,−B)。

一般换除子代表的坐标规则也应保留。若 A'=A+div g、B'=B+div h，则在固定 Poincaré 纤维中
\[
 \lambda'=\lambda/[g(B)h(A')]
          =\lambda/[h(A)g(B')],
\]
两个表达由 Weil 互反律相等。这里“旧坐标到新坐标”方向不可倒置。

原路径：

- scripts/p41_poincare_inverse47.py（完整源已从工具输出保留，可准确重传）；
- scripts/data/p41_poincare_inverse47_checkpoint.json.gz；
- 原 gzip 847,680 bytes；
- 原 SHA256 885357cd406744ad58e023014463e6892a9669e08e0fcac04933d16a2fe8769f；
- 原日志 /tmp/serre-p41-poincare-inverse47.log；
- 原运行最后三行明确输出 D_v 代数所有乘法恒等式 PASS、LEFT INVERSE 149764、上述 gzip SHA。

该最后阶段的主算法、全核和下降已过；其专门独立重算未运行。应以独立构造 D_v 限制商、纯整数 resultant/行列式和反向群律复验结束，不写成“全部独立通过”。

## 5. 重做顺序与源码丢失边界

若原文件仍在，先保存上述源码和 gzip，再运行：

~~~sh
python -u topics/serre-uniformity/scripts/p41_poincare_norms47.py
python -u topics/serre-uniformity/scripts/p41_poincare_algebras47.py
python -u topics/serre-uniformity/scripts/verify_p41_poincare_algebras47.py
python -u topics/serre-uniformity/scripts/p41_poincare_inverse47.py
~~~

若磁盘丢失，先按第2–3节重建前两个生成器及独立验证器。精确原 inverse 源码的 imports 依赖这些模块；只有它一份文件并不能运行。这是明确的恢复任务，不能把命令列出来就声称可执行。

确定性重建可以改变随机候选和 gzip SHA；必须重算所有实际矩阵并记录新 SHA。前三个 u/v 范数、CM 类比值和第4节的三范数在固定 s,t,u,v,f 不变时应逐项一致；Krylov 生成元、商基或中间矩阵改变不会改变这些实际范数。

norm_data 的随机数只选取真实三次乘积基。make_algebra 的候选 g 需写入证书。原 inverse 主 RNG 为 random.Random(4104712105)，但在前两个依赖源码丢失时不能仅凭该 seed 假定输出矩阵字节一致。

所有新矩阵证书须 gzip 且单文件 <5MB；未验证的重建源标清“待运行”，不得发布为已证明的新结果。必要时可以把完整恢复笔记先推送。

## 6. 并行的真实对数：不要从零重做已验证部分

已发布的实际 jets 和完整54方向校准分别为：

- p41_evaluation_jets47_checkpoint.json.gz：
  a4ff695e00a7dc7d662f3db0d675549852bc7f3490b5c34d3a18dd98a7528b5d；
  GP 常数/下降检查及标准库全部820×73一阶 jets 独立通过。
- p41_abel_tangents47_checkpoint.json.gz：
  34374a7eb86c63e0d9dbf65f1bb1828513db74a7756a1d0e7f6747588b33bf8e；
  独立 Čech 54/54 通过，每方向全部1460个比较坐标相同；54×54切向转换单位。
- p41_formal47_chart_checkpoint.json.gz：
  3835cbbd49a545b1c98e76ec7abd0c5658196c505dbc5cc041c93244352250be。

R123 的 Kodaira–Spencer 因子必须保留：
\[
 \beta(t)=-3/(4+27(32+t)^2),\quad
 \beta(0)=2880480\bmod q,\quad \beta(0)\bmod47=38.
\]
原始 weight2 值不能直接当 dt 系数。

令 D 的行为54条实际 Abel 方向、列为54个选定 chart 坐标，Omega 的行仍为这些方向、列为固定全纯微分。则校准矩阵为 D^{-1}Omega。这与 R123 的列向量写法互为转置。

固定
\[
H=\#J(\mathbb F_{47})=
21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072,
\quad H\bmod47=9.
\]
H 有304位，实际长乘从已发布95位快照继续。断线前子代理最后直接读取150位、226步、SHA256 6b3e541cc4b59ed2bc2f849c8b93ed9e5846a63f00b43a50b797b68e5071c6a2；根代理后来另固定155位、233步快照，但尚未推送。若新快照不存在，保底95位。

运行 p41_formal47_multiply.py 会从 rolling checkpoint 恢复。每5位原子保存，所有 AddFlip 完整核和下降检查；完成304位后必须实际 zero_test_mod47 证明落在形式群，不能只用“理论上 H 杀群”替代点表示检查。

p41_formal47_log.py 已发布且准备就绪，但尚未运行完成。其计算 Y、−Y、−2Y 的实际 chart，并设 F(P)=f_chart(P)−f_chart(0)：
\[
 L(Y)=\frac{2F(Y)-6F(-Y)+F(-2Y)}6\bmod47^4.
\]
整数不变导子/n! 估计使四阶起余项消失。再右乘 D^{-1}Omega，除以有符号的 H，得到 log B 的54坐标。没有减 f_chart(0) 会留下错误的常数 −3f_chart(0)，不能省略。

R121 预留给最终完整实际对数；尚未登记完成。

## 7. 继续的真实 Hecke 计算计划（尚未编码、尚未运行）

避免将匿名 Lie 向量直接当特征形式坐标。下一步在同一个实际评价模型构造 T2、T3：

E0:y²=x³+x+32 在47超奇异且 Frob²=−47，因此2、3循环核全在 F47²。2核横坐标是 x³+x+32 的三个根；3核是 3x⁴+6x²+384x−1 的四个根。所有根 Hensel 提升至 R2。

对核横坐标 r，令 d=x−r。2阶情形
\[
t=3r^2+A,\ u=0,\ w=rt;
\]
3阶情形
\[
t=2(3r^2+A),\ u=4(r^3+Ar+B),\ w=u+rt.
\]
规范 Vélu 同源为
\[
 A'=A-5t,\quad B'=B-7w,\quad
 x'=x+t/d+u/d^2,\quad
 y'=y(1-t/d^2-2u/d^3).
\]
其 pullback dx'/(2y')=dx/(2y)。先逐系数验证曲线恒等式，再应用实际 P,Q。

像基 (φP,φQ) 的 Weil 根为 ζ^ell；取 (φP,[ell^{-1} mod41]φQ) 恢复 ζ。相应项链由 diag(1,ell) 共轭，若项链记录为(a,epsilon)，新记录为(a/ell,epsilon/ell²)。

使用原 R102 的73个实际形式、原固定 ζ、原 basis_inverse，泛化 weight1 计算中的 A（不能仍硬编码1），对7个目标曲线计算完整820行。真实权2 Hecke 值为
\[
 T_\ell W=\ell^{-1}\sum_C W(E/C,\omega_C,\text{transported Cartan}),
 \quad \phi_C^*\omega_C=\omega.
\]
因子1/ell 可由 Tate q 的两种循环核给经典 ell f(q^ell)+ell^{-1}sum f((tau+a)/ell) 校准；还应以 R123 的 KS 函子性复核。

结果必须满足：所有820行回到 V1；保持实际典范核；Frobenius 半线性交换；T2 在54维典范空间的迹为−8；h=T2+2T3 的54次特征多项式与已证 R71/R89 谱分解逐系数相同。只有这些实际作用完成后，才将 log B 送入已证 R89 的 CM 比例和真实 G=54T2+8 平移。

上述只是具体算法入口，不是已完成证书；不要据此标记 Hecke 运算已通过。

## 8. 原始来源与范围

限制行列式范数及 Poincaré 群律与 Mascot 的实际算法相容，原文 arXiv:2608.10815v1，§3.3 Algorithm4、§4.1 Algorithms7–8；本笔记第2–4节独立写清了从真实限制商到真实双扩张的证明连接。

Hashimoto–Lido–Lombardo–Mascot–Parent, Equationless quadratic Chabauty for non-split Cartan modular curves, arXiv:2608.10919v1，§4.3、§6.5–6.7，解释了有限精度双扩张坐标与全局整点闭包之间仍需的输入。特别是：非零局部纤维中的一个运算不等于全局整数提升；存在算法不等于完成全体共同零点分类。
