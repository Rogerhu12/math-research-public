# 一个固定准确材料 Haar 目标的完整连续 Gram 消费入口

日期：2026-11-26。此文登记完整可执行源码与其新增完整界；没有运行或宣称任何当前候选的连续上界。第一条消费者只接 R671 lambda=1 的完整物理表示，不把 deep 或 SO3 场改名成这个表示。

源：scripts/resume_20261126/frozen_material_haar_interval.py，33593 字节，SHA256 faa8631af1eb81d55521dd23f5697e8fe07203efc0784b79c56bde604e3d3c96。

它与此前 finite physical mean 消费者是独立来源。准确 Haar 目标 evaluator 为 c5a717dbca55311060207672c703293403c16c6e5142b84cc522e660afc67a64，准确角矩源为 1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010。已经登记的 R691 给出准确材料 Haar 的定义与完整角矩。此处新增的是把这些完整区间矩真正接入连续径向 Bernstein/共同分割、支付其完整误差并输出合法全域上下界的消费者。

继承而不重证的部分为 R689 的同域共同分割、公共平方项抵消、当前场角弧完整包围及归一化误差接口；其支持源为 4552c2eafebb98b732d5ab7717b1b72665680a839b18a51c34c08f718f69381f。当前场 R674 六 jet 连续 Gram 源为 fd4cd58045e16a969c8c1be48468ab4c1a7be929ef9b95e2a9a24ca546176b2d，准确 reference-tail profile 源为 f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225。实际物理 factory 为 2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216；整数区间角矩算术绑定 e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2。

## 1. 冻结的对象究竟是什么

给定真实冻结场 F* 及其完整 core，令 theta*=Theta*(phi)、rho*=dTheta*/dphi。目标是完整连续积分

$$
E_*(s)=\frac1{2\pi}\int_0^{2\pi}\rho_*(\phi)|F_{*,s}(s,\phi)|^2\,d\phi,
$$

$$
C_*(s)=\frac1{2\pi}\int_0^{2\pi}
 \frac{|F_{*,\phi}(s,\phi)|^2}{\rho_*(\phi)}\,d\phi,
\qquad
g_*=E_*(s)\,ds^2+C_*(s)\,d\theta^2 .
$$

完整反射奇偶性使准确 Haar 交叉均值为零。角矩 carrier 只是对这些准确积分系数的完整外包；不是把目标改成某个有限网格均值，更不是把区间中点当成准确目标。

新消费者先读取实际 c5a manifest，独立核完整 canonical model 身份与全部 source/input 字节。输入角色必须恰为 bundle、node_report、scalar_input、observation_carrier、reference_carrier；来源角色必须恰为 evaluator、moments、arithmetic、factory、operator、observed、batch、scalar、integer、hold。冻结场、完整 core 和所有固定 radial/scalar/eta 定义与 manifest 逐项相等。

working moment carrier 必须来自同一冻结 bundle 和同一 angular identity，状态完整，完整 rho 正性成立，全部周期积分尾保留。accuracy_reached=false **本身不会使一个完整有效外包失效**。消费者会支付这些实际区间的宽度，不能把未达到的请求精度写成已达到。

当前场允许真的 mesh/M 变化，但不得更换目标。它与冻结场必须保留同一准确 scalar 定义、同一 S/R/width、lambda=1、同一准确 eta 端点和固定前三 core。当前其他 core、q、H 和空间分辨率可以变化；冻结 E*、C*、全部冻结角矩定义和 cap metric 不变。

## 2. 完整角矩怎样进入连续径向多项式

R691 已将准确角积分写成完整矩阵/向量系数。记当前这里的 q、u=q_s 均是**冻结场**的完整径向系数，分成 R/T/Z 三块；f 为其准确共同参考径向函数，z=hH*+k 为其完整轴向项。完整准确公式是

$$
E_*=u^TPu+2f_s\ell^Tu+2z_sb^Tu+f_s^2+z_s^2,
$$

$$
C_*=q^TQq+2f\ell^Tq+f^2 .
$$

P 的三个对角块是 Prr、Ptt、Pzz；Q 的三个对角块是 Qrr、Qtt、Qzz，并有两个互为转置的 R/T 交叉块，所以代码明确包含 $2q_R^TQ_{rt}q_T$。ellR、ellT 和 bZ 的全部条目均读入。没有只保低频或小部分 core，也没有删 exact-tail 的 k。

每个准确 moment 的整数有理上下端点先向外转换成浮点区间，转换过程逐项核确切 Fraction 与实际 binary64 的大小关系，需要时 nextafter 向外补一格。证书从不使用 midpoint_matrices。

在每个 exact joint piece 上，共享 quintic q 及其 s 导数 u 用完整 Hermite 端 jet 和准确符号宽度得到 Bernstein 区间控制点，再精确限制到这个共同物理分片。设

$$
x(t)=\sum_{i=0}^m x_i B_i^m(t),\quad
y(t)=\sum_{j=0}^n y_j B_j^n(t),
$$

则对任一完整矩阵 M，

$$
x(t)^TMy(t)
=\sum_{k=0}^{m+n}
 \left[
 \sum_{i+j=k}
 \frac{\binom mi\binom nj}{\binom{m+n}k}
 x_i^TMy_j
 \right]B_k^{m+n}(t).
$$

这是 Bernstein 乘积恒等式。每个权重是非负准确有理数；每个矩阵乘积、逐项求和、次数提升和标量乘积均由现有 outward interval 算术执行。因此全部真实冻结 E*、C* 的多项式部分被生成的 Bernstein 控制点包围。随后才取控制点 hull；不先把整个径向变化粗化成一个位置区间。

角矩各条目可以相关，但逐项区间扩展仍包含真实联合取值。它可能宽，不能窄到漏掉真实值。矩阵维数与冻结 M、完整 q 各块逐项核对。

## 3. Haar 均值所需的新 scalar remainder 界

R689 的有限 physical mean 入口不能仅换个名字当准确 Haar；本模块独立替换其 target_polynomials。这里必须证明针对完整积分的 scalar fee。

令

$$
d\mu(\phi)=\frac{\rho_*(\phi)}{2\pi}\,d\phi.
$$

准确 rho*>0 且其准确全周期均值为 1，所以 mu 是正概率测度。设某个共同径向分片上的多项式近似给出 $\widehat V$ 和真实 $V=\widehat V+\delta V$，并有统一点态误差 $|\delta V|\le e_V$。则

$$
\begin{aligned}
\left|\int |V|^2d\mu-\int|\widehat V|^2d\mu\right|
&\le 2\int|\widehat V||\delta V|d\mu+\int|\delta V|^2d\mu\\
&\le 2\left(\int|\widehat V|^2d\mu\right)^{1/2}
       \left(\int|\delta V|^2d\mu\right)^{1/2}+e_V^2\\
&\le 2\sqrt{\widehat E_{\rm upper}}\,e_V+e_V^2 .
\end{aligned}
$$

这里用了 Cauchy–Schwarz 和 mu 总质量为 1。因而只需要准确 Haar 多项式均方范数的合法上界，不需要错误地宣称该平均值是点态最大范数。

对于 $V=F_{*,s}$，scalar 误差为径向和轴向两个正交分量，故

$$
e_V=\sqrt{e_{f_s}^2+e_{z_s}^2}.
$$

对于材料角导数 $W=F_{*,\theta}=F_{*,\phi}/\rho_*$，参考误差恰为 $\delta f\,e_\theta$：rho* 完整抵消，故 $|\delta W|\le e_f$。因此

$$
\delta E_*\le2\sqrt{\widehat E_{\rm upper}}e_V+e_V^2,\qquad
\delta C_*\le2\sqrt{\widehat C_{\rm upper}}e_f+e_f^2.
$$

这些式子的每个乘除、根号和相加仍向外舍入。e_z 包含真实 frozen H* 乘 h 的误差和 k 的误差，不能拿当前 H 代替，也不能把所有 hH 项当成公共项删去。

完整 profile 分片和所有准确尾项继续由已有 f122/R674 控制。当前场与冻结场的 scalar remainder 分别支付。若当前分片的包围不足以证目标 E*/C* 的正下界，消费者给该分片失败且没有贡献；不会用某个点的正性取代全分片分母正性。

## 4. 同一公共平方项究竟怎样抵消

在同一物理共同分片上，共同 f 的准确定义、lambda、width、eta 和 scalar 参数一致。由同一个准确中心和同一个 Taylor 次数表示共同 f、f_s。虽然各自区间系数可能因求积包围宽度不同而上下端点不同，它们都包含同一组准确系数；并没有两个不同数学 f。

定义

$$
E_{*,\rm res}=E_*-f_s^2,\qquad
C_{*,\rm res}=C_*-f^2
$$

的多项式部分，上节源码逐项生成它们。当前完整 physical Gram 中的同一 $f_s^2$、$f^2$ 在实际差值分子中作解析恒等抵消。之后仍把当前和冻结 scalar 余项全部付回。这里不是“两个宽区间相减凑出零”，也不是认为数值 carrier 完全相同才可抵消。

含 H 的项不同：$z_s=h_sH+k_s$ 一般随当前 H 变化。冻结的 $z_{*,s}$ 与当前 $z_s$ 各自完整保留，$2z_sb^Tu+z_s^2$ 等项不能无条件消掉。新 target_polynomials 明确保留完整这些项。

当前物理六 jet 的角依赖继续由 R674 的完整 Fourier/非线性角 lift 处理。它在完整闭角弧上给出当前残差分子包围，并支付其四阶余项，不以角节点最大值充全角最大值。冻结目标本身不需要在有限目标角节点再求一次均值；它已经由完整区间角矩表示。

## 5. 相对 Gram、分母和上下界

在材料坐标 (s,theta) 下，真正要比较的是

$$
A=g_*^{-1/2}(F^*\langle\cdot,\cdot\rangle-g_*)g_*^{-1/2}
 =\begin{pmatrix}e&m\\m&c\end{pmatrix}.
$$

当前原 phi 参数要用**当前** rho 换到材料 theta；目标 E*、C* 仍是完全冻结的函数。实际归一化分别支付 E*、C* 与 $\sqrt{E_*C_*}$ 的完整区间分母，且在每个分片上要求其正下界。当前 rho 也须在完整角弧上严格为正。不要将冻结 rho* 和当前 rho 混用。

准确二维实对称矩阵的算子范数为

$$
\|A\|_{\rm op}
=\frac{|e+c|+\sqrt{(e-c)^2+4m^2}}2 .
$$

已有 R674/R689 区间实现向外包围它，返回该共同分片乘完整角域的上界，并可在实际已包围的端点/角节点给准确 supremum 的下界。后者若超过 1e−6，只证明这个真实候选高于目标；不证明其它输入或其它求解路线不能达标。

cap 继续使用同一固定 marker graph 自身的 induced metric；高度平移不改变它。完整相位 family 的 metric 归约沿用已登记 R248 的共轭关系与同一旋转不变目标，不能把这个 flag 当作 embedding/reach/held 的证明。

## 6. 共同分割、自然小批和合法覆盖

当前 q 网格、冻结 q 网格、FullHold、准确尾以及 eta 接点取准确符号公共细分。当前 mesh/M 精化不改变 frozen target；joint pieces 逐个记录当前 cell、冻结 cell 和准确左右端点。每个径向可进一步按正的二幂 subdivision 分片。

默认每次新 admission 至多 64 个**完整分片**，admission budget 为 600 秒。已经开始的一个分片计算自然完成再返回；不凭硬时限杀掉半条区间结果。runner-local journal 保存实际已返回分片，完整签名绑定本源、实际 current/frozen 输入、固定 target、实际完整 moment carrier、角精度、径向细分、scalar degree/panels 和 run 身份。后续必须显式 --resume 且用同一签名。换 working moment carrier 时准确目标可以仍相同，但这是另一份实际证书输入；本 journal 不把不同实际 carrier 无声混起来。

每个分片只有 returned 或 failed 状态。failed 没有数学贡献；跳过 failed 并不消除其覆盖责任。partial return 只报告已覆盖区域的界，不能声称完整域。

一个当前 cell 只有其全部 exact joint pieces/径向 subpieces 成功返齐才算 covered。完整 scope 需要全部当前 cell；公开 compact summary 用 cell 区间字符串和实际 identity 保存这个事实，不提交可重算的大数组或逐分片 raw journal。

只有 complete_scope=true 且完整上界的准确 binary64 Fraction 不大于 1/1000000，metric_certified 与 all_t_metric_certified 才能为 true。无论如何，本源都把 reach_certified、embedding_certified、fixed_metric_convergence_certified 和 topic_completion_certified 保持 false。

## 7. 可运行命令与实际状态

本命令必须绑定已真实返回的 frozen manifest、同场最终 bundle、node 和该候选自身的 reference carrier；路径仅是模板，不是已经存在这些返回的宣称。

~~~bash
python {repo}/topics/visible-flex-larger-amplitude/scripts/resume_20261126/frozen_material_haar_interval.py \
  --repo {repo} \
  --bundle {work}/ACTUAL_SAME_HAAR_CANDIDATE/final.npz \
  --node-report {work}/ACTUAL_SAME_HAAR_CANDIDATE_NODE.json \
  --scalar-input {work}/fullclosed_solver/data/pulse-a5-complete-base.json.gz \
  --reference-carrier {work}/ACTUAL_SAME_HAAR_CANDIDATE/exact-tail-lift-profiles.npz \
  --frozen-target {work}/haar-7ebb-fixed-target/frozen-target.json \
  --target-moments {work}/haar-7ebb-fixed-target/moments.json \
  --angles 8192 --radial-subdivisions 1 --scalar-degree 5 --panels 128 \
  --budget-seconds 600 --maximum-new-pieces 64 \
  --journal {work}/ACTUAL_SAME_HAAR_CANDIDATE-continuous-Gram/journal \
  --out {work}/ACTUAL_SAME_HAAR_CANDIDATE-continuous-Gram/batch-0001.json
~~~

后继换一个新的 --out 文件名并增加 --resume，保同 journal。两个可选 same-byte override JSON 为 --target-input-overrides 与 --target-source-overrides，只解决已核字节的实际路径恢复，不准更换数学输入。--angles 是当前场的连续角弧细化数，不能用它改 frozen angular target；工作 moment report 自己的 Q/阶数同样只是准确积分的外包精度。

新输出 schema 为 R691-frozen-accurate-Haar-continuous-Gram-v1；逐分片 schema 为 R691-frozen-accurate-Haar-continuous-Gram-piece-v1。完整 summary 包含实际 current bundle/node、frozen bundle/target identity、angular identity、working moment carrier SHA/Q/p、完整任务数、成功/失败数、已覆盖 cell 区间、完整和部分域上界、准确分数、真实下界见证以及明确 false 的未付款责任。

源仅做 AST/compile/重复 literal key/keyword 检查。solver 已独立静态核完整 source guard、全部 P/Q/ell/b 乘积、scalar Haar L2 费、共同抵消接口和 R689 certify/validate 接线，未发现阻断。没有本地科学计算或人为 fixture，没有从 stage71 的有效角矩虚构出连续 metric 上界。

执行安排保持原授权：当前约百分之一残差的场不重跑昂贵注定未过的完整 upper。先由准确 Haar 新固定目标的完整 solver 产生实际低误差候选，再对其真实同场 final 和完整 frozen target 启用本消费者；若结果揭示缺口，就继续换输入/方向/精度，不能用本文当任务完成。
