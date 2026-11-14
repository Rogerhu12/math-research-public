# R209：强幅度全径向相位归一化的严格非零域及径向嵌套

**状态：已证明。** 本文给 R201 完整半周位置定义中的相位归一化一个明确充分域，
并对已经保存的 R201+R205 第五个 932 维实际态给出严格连续消费。
它不要求重新作相位积分，不替代等距、浸入或 reach 的证明，不改变当前 LM 搜索域。
准则失败只表示此充分估计未通过，不表示相位归一化实际为零。

## 1. 完整函数与声明的输入

写物理材料角 $u\in\mathbb R/(2\pi\mathbb Z)$，径向坐标 $s$。
当前完整 R201+R205 公式的未归一化相位是

$$
\psi(s,u)=\psi_{\rm seed}(s,u)+\chi(s)\psi_{\rm tail}(s,u;A)
+\sum_{j=0}^{J-1}B_j(s)
 \sum_{k=1}^K\{p_{jk}\sin(2ku)+q_{jk}\cos(2ku)\}.
$$

其中：

- $\psi_{\rm seed}=\arcsin(r(s)H(u))$，
  $r(s)=\frac12\sin(\pi(1-S_5((s-c)/(S-c))))$ 并按原源作常值端延拓；
- $H(u)$ 是强中央椭圆的准确 R197 安全种子；
- $\chi=S_5((s-c)/(S-c))$，$0\le\chi\le1$；
- $A$ 是完整 R205 弯环的单个全局幅度，声明域为 $0\le A\le6/5$；
- $B_j$ 为 R196 声明的简单非均匀三次 B 样条，端外零延拓且 $C^2$，并有
  $B_j\ge0,\ \sum_jB_j\le1$；
- $p,q$ 是保存的真实正弦/余弦相位系数，均按准确 binary64 有理值解释。

这里的相位是 provider 源中的 `ph`，不是独立的水平角 `th`。
新增水平常数、水平余弦、height、cutHeight 和 radius 列均保留在完整场中，
但不进入这一相位归一化的充分估计。没有遗漏相位的任何一条正弦或余弦列。

所消费的实际公式源为：

1. `scripts/fd2d-R201-R205-variable-amplitude-provider.cjs`，
   SHA256 `eccfb354b52ef49a65e9b4ff74a6d9c3023bbf4fde839184845c2b5dab91ad3b`；
2. `scripts/fd2d-direct-position-tangent-lift-baseline-R187.cjs`，
   SHA256 `ca06fd0651f9479a0f66ea3090d450d695e3f2383d64874bd6ce11eb8698d3bf`；
3. `scripts/fd2d-bent-annulus-reference-R205.cjs`，
   SHA256 `77ec2bdcdb0401319a8ca61a0230fd5041fcf5d5a1285ee0338f1973732628d7`；
4. `scripts/fd2d-cubic-spline-refinement-R196.cjs`，
   SHA256 `ecef2af139d2fe92387c2984ca75edf26e7fd0b6f44e909cf91ac3b2530a5f77`。

第一至第三份已按实际字节核回读。第四份是保存态明示的准确径向函数定义；
其非负与分区性质是标准 Cox–de Boor 递推的代数性质，以下也给出所需理由。

## 2. 对固定强种子已支付的整周界

强原始轴是

$$
A_0=\frac{6134056590672823}{4503599627370496},\qquad
B_0=\frac{1265588444388213}{2251799813685248},
$$

与 R197 强归一化和完整材料 chart 的 bits 完全一致。本文不把尾幅度 $A$ 与轴 $A_0$ 混用。

完整 R197 checkpoint 的 SHA256 是

`a1bf7fecdc3e0739b03329efc8886eecbaff2dca3c9843d909c2ac1f94b4275f`。

其中 64 个实际 Taylor 格已全部完成，原数学源和 R188 算术源分别为
`3ccca82923ac0ed4cebcd66cc912944e41565d8e27567e0bd08f684a029ff79f` 与
`5c04a135eed859a6d6d583877e53681cdc1dddc6102c913152adfc1913a9f97e`。
完整依据、原周长输入及重生入口见
`notes/2026-11-13-fd2d-R197-strong-complete-material-chart.md`。
本次只消费每格已有左右端点，不重新积分任何一格或归一化周长。

令 $Q=\pi/2$，第一象限上的准确材料反解为 $\theta(u)$，并记
$\ell^2=B_0^2+(A_0^2-B_0^2)\sin^2\theta$。准确种子有

$$
\cos\delta(u)=
 \frac{A_0\sin\theta(u)\sin u+B_0\cos\theta(u)\cos u}{\ell(\theta(u))},
\qquad H^2=2(1-\cos\delta).
$$

对每个材料格，准确单调性给出完整 $\theta$ 盒。把其端点和 $u$ 盒向外舍入到
$2^{-40}$ 有理网格，只扩大包围。所有参数仍在 $[0,8/5]$。
对一个有理 $x$ 使用交错 Taylor 和

$$
S_7(x)\le\sin x\le S_8(x),\qquad C_7(x)\le\cos x\le C_8(x),
$$

其中 $S_k=\sum_{i=0}^k(-1)^ix^{2i+1}/(2i+1)!$，
$C_k=\sum_{i=0}^k(-1)^ix^{2i}/(2i)!$。
所保留末项之后的绝对项严格递减；因此交错级数余项有上述符号。
第一象限上的正弦递增、余弦递减把端点不等式变为整格不等式，
必要时与已知 $[0,1]$ 相交。这是有理包围，不是角度采样。
终点的向外舍入须单独说明：实际 126 个非末端上界及全部 128 个左端界均不超过已证 $\pi/2$ 下界；
仅最后的 $\theta$、$u$ 上界是 $1727108826179/1099511627776$，略大于 $\pi/2$。
对这个准确有理数，原 $S_8$ 多项式的值严格大于 1，余量约 $4.3514761\times10^{-14}$，
所以原程序的 $\min(1,S_8)$ 在这里准确返回 1，仍给合法整格上界。
这一端点说明由另一次 0.010 秒的有理读取核实，完整有理余量附在报告中；没有重算 64 格不等式或逆映射。

若 $s_\theta^\pm,c_\theta^\pm,s_u^\pm,c_u^\pm$ 是这些整格界，令

$$
N_-=A_0s_\theta^-s_u^-+B_0c_\theta^-c_u^-,
\qquad
L_+^2=B_0^2+(A_0^2-B_0^2)(s_\theta^+)^2.
$$

实际程序对全部 64 格准确核实了

$$
N_-\ge0,\qquad
N_-^2-\left(\frac{23}{32}\right)^2L_+^2\ge0.
$$

全部通过，最小正余量位于第 14 格，且落在准确区间

$$
\left[
\frac{83765846951}{1099511627776},
\frac{83765846952}{1099511627776}
\right],
$$

约为 $0.076184594$。完整实际有理值和该格见证在报告中。
因两边非负，这些平方不等式严格推出整格
$\cos\delta\ge23/32$。R197 的四象限反射保持 $\cos\delta$ 和 $|H|$，所以

$$
\boxed{\ |H(u)|\le\frac34\quad\text{对全部材料角成立。}\ }
$$

该结论属于此准确强种子；不能不核轴而转借其他中央形状。

## 3. 通用充分系数域与连续相位下界

定义每个径向控制行的完整相位范数

$$
M_j=\sum_{k=1}^K(|p_{jk}|+|q_{jk}|),\qquad M=\max_jM_j.
$$

**定理。** 对第 1 节的完整函数，若第 2 节的种子界已付，而且

$$
0\le A\le\frac65,\qquad \boxed{A+M\le1},
$$

则在整个径向区间和全部材料角上

$$
|\psi(s,u)|<\frac75.
$$

从而准确半周复积分

$$
Z(s)=\int_0^\pi e^{i\psi(s,u)}\,du
$$

满足

$$
\boxed{\ \Re Z(s)>\frac12,\qquad |Z(s)|>\frac12\quad\text{对所有 }s.\ }
$$

**证明。**
首先 $|r|\le1/2$，所以 $|rH|\le3/8$。
由交错三项不等式，

$$
\sin\frac25\ge\frac25-\frac{(2/5)^3}{6}
=\frac{146}{375}>\frac38.
$$

因此主支上的 $|\psi_{\rm seed}|\le\arcsin(3/8)<2/5$。
这个证明同时支付了 seed 的 arcsin 连续定义域；不使用浮点 clamp 作为证明。

R205 的准确尾角满足
$\sin\psi_{\rm tail}=-\cos u\sin\alpha$，
$|\alpha|\le A<\pi/2$，且其水平范数为正。
故其声明的主角有 $|\psi_{\rm tail}|\le A$，并得到
$|\chi\psi_{\rm tail}|\le A$。

三次 B 样条的非负分区性质给出

$$
\left|\sum_jB_j(s)\sum_k
 (p_{jk}\sin2ku+q_{jk}\cos2ku)\right|
 \le\sum_jB_j(s)M_j\le M.
$$

合并得 $|\psi|<2/5+A+M\le7/5$。
这里未使用有限相位 quadrature，也没有只验证径向样本。

最后

$$
\cos\frac75\ge
1-\frac{(7/5)^2}{2}+\frac{(7/5)^4}{24}-\frac{(7/5)^6}{720}
=\frac{1908101}{11250000}>\frac16.
$$

因此所有材料角的 $\cos\psi>1/6$，积分得到
$\Re Z>\pi/6>1/2$，且 $|Z|\ge\Re Z$。证毕。

## 4. 非均匀基底、端点与 C² 相位链

简单非均匀三次 B 样条可以由非负的零阶指示函数通过 Cox–de Boor 递推得到。
在每个有效区间，递推系数非负；同一个低阶基函数在相邻两个高阶项中的系数和为 1。
对内部项求和得到 1，截断两端仅移去非负贡献，所以 $0\le\sum_jB_j\le1$。
三次基函数的支撑跨四个结点区间；简单端结点使端外零延拓在声明端点有零值、零一阶及零二阶导数。
R196 的定义与保存的准确有理 knots 明确指定了这组基，未用 binary64
求值时偶发的 tiny support 尾项替代数学定义。

中央柱及切口的相位两 jet 仍沿原完整 reference，新增相位项在端点零两 jet。
R205 的 smoothstep、固定平领口和完整弯环参考保证所用角函数 $C^2$；
原种子满足已付安全 chart，故 $\psi$ 在闭前缀上 $C^2$。
在有限角区间上可以对积分求两次径向导数，得到

$$
Z_s=\int_0^\pi i\psi_s e^{i\psi}\,du,\qquad
Z_{ss}=\int_0^\pi(i\psi_{ss}-\psi_s^2)e^{i\psi}\,du.
$$

由 $\Re Z>1/2$，全径向只需同一个右半平面 argument 支。
于是 $\beta=\arg Z$ 与其完整两阶链

$$
\beta_s=\Im\frac{Z_s}{Z},\qquad
\beta_{ss}=\Im\left(\frac{Z_{ss}}Z-\left(\frac{Z_s}Z\right)^2\right)
$$

连续有定义。R201 的代数归一化
$e^{i\Phi}=e^{i\psi}\overline Z/|Z|$ 因而也是 $C^2$。
本结论没有把有限积分值的 minMeanR 当作连续下界，也不加全局 $C^3$ 条件。

它只支付归一化因子和这条链的非奇异性。它不推出完整位置图浸入，
不要求或声称归一化后 $\cos\Phi$ 处处为正，也不推出角向/径向度量已经相容。

## 5. 当前第五态的真实准确消费

实际输入：

`notes/2026-11-13-fd2d-R201-R205-amplitude-05-checkpoint.json`，
58528 B，SHA256
`f5708c59bbee004bb859d9205d5eb097c2638e6d682d8a27c92a63d0bf0280c8`。

它有 $J=30,K=7$、932 个保存参数。相位正弦位于原完整 layout，
余弦位于每个追加径向块的最后 7 列；全局幅度位于显式索引 931。
消费者读取并核实这一显式 layout，不沿旧“最后 T”或只正弦的假设。

准确结果为

$$
M=\frac{7385061408773374127}{9223372036854775808},
\qquad
A+M=\frac{9160211858501382831}{9223372036854775808}<1,
$$

$$
1-A-M=
\frac{63160178353392977}{9223372036854775808}
\approx0.0068478402585320595.
$$

最大行是第 21 行。完整 $|\psi|$ 上界
$2/5+A+M\approx1.393152159741468<7/5$。
所有参数按实际 binary64 位解码为精确有理数后求绝对值和，
没有给这些求和套一个未证明的浮点容差。

一次实际纯 V8 执行合计 **4.173 秒**：
完成 64 格种子平方不等式与 30 个真实相位行，所有判断均为 BigInt 有理比较。
无 OS 子进程，无额外相位积分、normal、BVP、参数改变或新 trial。
原 64 格逆映射没有重算。报告中的可选显示数若因巨大有理数溢出而为空，
准确整数对及独立向外 dyadic 显示区间仍完整；所有判断不依赖 display。

## 6. R208 同场细化及 binary64 末舍入

设准确 Boehm 注入的行系数为 $w_{ji}\ge0$，且 $\sum_iw_{ji}\le1$。
对所有相位正弦和余弦通道使用**同一行**，则

$$
p'_{jk}=\sum_iw_{ji}p_{ik},\qquad q'_{jk}=\sum_iw_{ji}q_{ik},
$$

并有

$$
\sum_k(|p'_{jk}|+|q'_{jk}|)
\le\sum_iw_{ji}\sum_k(|p_{ik}|+|q_{ik}|)
\le M.
$$

所以在准确实系数下，R208 的同场径向嵌套不增 $M$；复制不变的尾幅度 $A$
使充分条件自动保持。对新角模补零也保持 $M$，不需要重算相位积分或 R197 chart。

若保存的是末次 binary64 系数 $\widehat p',\widehat q'$，应消费真实逐列舍入包
$|\widehat p'_{jk}-p'_{jk}|\le\epsilon^p_{jk}$、
$|\widehat q'_{jk}-q'_{jk}|\le\epsilon^q_{jk}$，得到

$$
\widehat M\le M+
\max_j\sum_k(\epsilon^p_{jk}+\epsilon^q_{jk}).
$$

还须加上任何实际 $A$ 舍入量。对当前态，只要这些完整误差之和不超过第 5 节准确余量，
R209 就继续成立。也可直接对新的完整保存数组运行同一有理系数消费者，
这通常比消费一个粗舍入包更紧。

**不得把共同点两 jet 差或一个打印的小数差当作系数舍入界。**
新的 J、K、phase layout、amplitudeIndex 和 knots 必须来自实际新 archive。
不把父态的已证域身份无声借给另一个已改变幅度/系数的接受态。

## 7. 可复用实现与准确范围

`scripts/fd2d_R201_strong_phase_sector_certificate.cjs`
导出 `createR201PhaseSectorCertificate()`：

- `certifySeed(checkpoint,{expectedCheckpointSHA256})` 只消费已成严格材料包，
  给整周种子界和整格余量；
- `certifyState(parameters,layout,seed,{stateIdentity,basisDefinition})`
  给当前实际系数充分域、准确余量及完整连续结论；
- `binary64(x)` 明确解码保存的有限位，不先做十进制近似。

首次付种子后，同一个准确中央种子的后续各态只需第二步；
不重复 64 格证书或相位积分。准则检查是独立数学消费，不自动改 LM 接受域。

完整实际报告：
`notes/2026-11-13-fd2d-R209-continuous-phase-domain-05-report.json`。
该报告绑定 R197 完整 checkpoint、当前 state、各实际公式源和此新消费源。

本结论消除了这一个固定输入及上述明确系数域中的连续 phase-zero 风险。
当前场的 metric/曲率/全局法球仍不合格；R209 不代替 R193 误差传播，
不证明强目标已完成，也不把局部充分条件提升为一般不存在性或必要域。
