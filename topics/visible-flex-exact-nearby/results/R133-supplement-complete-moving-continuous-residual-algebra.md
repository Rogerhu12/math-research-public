# R133 补篇：moving 全连续残差、完整 primitive 与真实均值

## 1. 声明与输入

本篇把既有 `BudgetPolynomial` 的有向径向/Fourier 误差代数用于真正的
moving 方程。原生输入为完整新中心
SHA `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`，
6145 个径向节点，全部 M=32 的 U 正弦、V 含均值余弦状态，α 的准确 dyadic 值
6890507429876859/9007199254740992，ν=−2572625729470897/72057594037927936。
本次实际中心取原目标 η=0。所有尾、均值、参数对象身份与剩余区域均按原输入保留。

`ReciprocalFullTargetJets` 在每个真实 scalar germ 内提供
γ、β、K、s=1/Cref 的完整前三阶导数，包括原 primitive 无穷尾和
实际 natural graft 的完整 Wiener Taylor majorant。分区包含候选所有径向
节点、原 scalar 节点、.05/.18 控制接缝及 r=3；不跨实际单侧第三阶接缝。
最终覆盖[0,25/8]的并分区共有7296个闭单元。

## 2. 完整三次状态与非局部 primitive

在一个闭径向单元 r=r_mid+h x，|x|≤1，把原完整 dyadic 三次状态准确
换元。逐 Fourier 系数选 dyadic 中心，保留其有向差；所有 M 个模式和 V0
进入误差账。原径向导数直接由完整三次导出，未重新拟合。

每个径向标量 f 使用
\[
 f(r)=f(r_0)+hx f'(r_0)+h^2x^2 f''(r_0)/2
                     +h^3x^3 f'''(\xi)/6.
\]
第三系数使用整个闭单元的导数区间。把各区间系数的 dyadic 中心和差分别
记作有限径向多项式及一个全 \(A^0\) 误差。对乘法继续使用
\[
 \epsilon_{ab}\le M_a\epsilon_b+M_b\epsilon_a+
                         \epsilon_a\epsilon_b,
\]
其中两个 M 都是对应有限参考多项式在整个径向单元的 Fourier \(A^0\) 上界。
这保留径向余项对角向乘积的全部影响。

设原有限输入的角模式指标为 j，即物理频率4j。先形成
\(v=s+\alpha V\)、\(S=\alpha^2U^2+Kv^2\)，完整 S 的支持至2M。
必须先对全部2M取 primitive，再乘原 Uφ/Vφ；不能把中间输出截回M。
有向 FFT 用 N>6M，检查每个数学上不存在的模的区间确实含零后才归零。
对非零频率准确乘 \(1/(4ij)\)，零模置零，因此
\[
 \|If\|_{A^0}\le\tfrac14\|f\|_{A^0},
 \qquad \epsilon_{If}\le\epsilon_f/4.
\]
此处全部输入误差也保留；primitive 的完整径向各阶一起做有向变换。

真实 mean 从变换前的原 V0 系数直接抽出，令
\(m=s+\alpha V_0\)。它不由浮点角平均替代，也不设为 s。
完整 normalized 右端为
\[
\begin{split}
 f_U&=dU_\phi+\gamma mK V_\phi-\beta U(1+\alpha^2U^2+Kv^2),\\
 f_V&=dV_\phi-\gamma mU_\phi+
 \beta\{V-K(3s^2V+3\alpha sV^2+\alpha^2V^3)-\alpha vU^2\},
 \quad d=-\beta IS.
\end{split}
\]
其准确角向支持至3M，含全部 scalar-target 余项时仍成立，因为这些目标量
只有径向变量。故在本实际 N=256、M=32 下，全部至96的角模都被解析。

## 3. 闭单元上的残差范数、未保留模和 C0 恢复

对 R_U=U_r−f_U、R_V=V_r−f_V 的每一个径向多项式系数做完整有向FFT，
把各阶 Fourier \(\ell^1\) 上界相加，再加完整 uniform 误差，得到整个
闭径向单元、整个实角圆的 \(A^0\) 残差上界。还单独保留 j>M 的全部输出。
误差账在未保留模上取同一完整误差是安全上界，不宣称这些费用都来自高模。

\(A^1\) 使用权1+4|j|。完整 scalar/roundoff 误差的支持也至3M，故其
\(A^1\) 费用不超过(1+12M)倍的 \(A^0\) 费用。这个范数控制标准 H1；
没有把只有 \(A^0\) 的任意无穷频误差免费提升为 H1。

真实 v<0 的证明对全部闭角单元使用候选完整第一角 jet 与完整第二角 jet
Taylor 余项，并覆盖整个径向单元。于是 \(m<0\)，
\(\theta_\phi=v/m>0\)，原 lift 对整个实角圆为次数一的微分同胚。
恢复物理残差必须使用
\[
 \varepsilon=\frac1v I\left(\rho_v-\frac v m\langle\rho_v\rangle\right),
 \quad \rho_u=\alpha R_U,\quad\rho_v=\alpha R_V,
\]
\[
 r_u=\rho_u-u_\phi\varepsilon,\quad
 r_v=\rho_v-v_\phi\varepsilon,\quad
 R_B=r_u/v-u r_v/v^2,\quad R_C=-r_v/v^2.
\]
代码先在 \(A^0\) 支付 primitive 与全部 mean，再用已证点态 v-gap 作C0
除法；没有从点态离零免费推出 \(\|1/v\|_{A^0}\) 的上界。

候选第二型仍准确满足 det S=K、tr S=Kv+(1+u²)/v，由此给候选主曲率界。
候选 II 的界不等于某个已存在浸入的曲率或 reach。

## 4. 已实际完成的前八个闭单元和后续覆盖

原过程78221完成前四个完整闭单元后正常保存暂停；25362严格从原第4行
接续至第8行，未重做已有行。首次用时55.80秒包括冷启动；第二次四行增加
13.97秒。native摘要直接提取已经完成的八行，并再次以 Arb 判断声明的有理
门，不重复其单元计算：

| 完整闭区间量 | 严格上/下界 |
|---|---:|
| R_U 全A0 | <2.058e−8 |
| R_V 全A0 | <9.116e−9 |
| 真实 −v 全圆gap | >.090153 |
| 候选最大绝对主曲率 | <11.092579 |
| 完整恢复物理 C 残差 C0 | <2.870e−5 |

范围准确为[0,3843071682022823/2305843009213693952]，只是7296单元的前8个。
其余区间正在从完整已存前缀接续并分片计算。原 PPoly 接缝跳由准确 dyadic
Horner 计算；最终聚合必须覆盖全部接缝，且实际几何连接需消费完整 mean
和换角接口费用。没有将未完成分区、原始小跳或浮点 BVP 成功当成连续解。

源文件为 `fourfold_codazzi_moving_continuous_residual.py`、
`fourfold_codazzi_moving_residual_checkpointed.py` 和
`fourfold_codazzi_moving_residual_prefix.py`。
稳定前八行证书为
`notes/2026-11-13-R133-moving-alpha0765-fullR-first8-continuous-native.json.gz`。
完整 BVP 逆、真非线性帽/long、精确闭面及同族所有几何标准继续处理。
