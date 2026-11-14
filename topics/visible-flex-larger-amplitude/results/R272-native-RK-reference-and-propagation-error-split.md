# R272 — 节点 G、原 RK 各级误差与零参考传播恒等式

2026-11-14。本文只读冻结源码、既存小报告并作实数代数推导；没有运行 RHS、根、RK、Jacobian、范数、谱或线性求解。它解释后继诊断应区分的对象，不把参考公式当成 actual43 的实际导数，也不增加本题完成标准。

## 1. 已知失败究竟证明了什么

[actual43](https://github.com/Rogerhu12/math-research-public/actions/runs/43626121246) 的 G producer 是 exact_20261114_rawcell0_gauge_equilibrated_correction.py，SHA256 为 16fca40ec0ff21a119ce1563241692248005ec6587af000efb968c5158ad9a00。根会话读取其真实压缩 result 的 SHA 为 cf6e00345697ed8bd4a114c2d79f8625e49626d2263e83f42e7dc60e3020013e；全部 307552 行的原 1372 段精确 binary-real sigma 范数依次为：

- 初始方向：7.09987830368630829e21。
- 第一次修正：3.25806697778557413e21。
- 第二次修正：3.76944193857401563e21，较前次变坏而停止。

这些数来自实际报告，不是本文重新计算。本文没有独立重审该大 artifact 或重算任何 dot。最佳方向最坏行是新段519，对应旧段43、原流步11、Pi 模112。LAPACK info0 只说明该执行未报告零主元，不能把它解释成前向误差、原尺度残差或 native 接受已经满足。

这次结果足以说明：**这一次已保存节点 G 的形成、binary64 LU、误差修正及原坐标恢复组合，没有产生可据其线性质量继续的方向。** 它本身还不能证明原 RK 局部矩阵错误，也不能把失败唯一归因为 RK 不稳定或谱病态。

对给定的有限原数组 A，线性缺陷 A delta+r 测的是这组数组方程的求解误差。即使 A 近似真实导数很差，一个精确线性解仍可使这个缺陷为零；反之，一个准确的导数也可能很难用当前浮点表示求解。必须把“导数质量”和“给定矩阵的求解质量”分开。原非线性试步是否通过仍由原 evaluate/guard/严格范数下降判断，而不是本文件新设一个一般线性容差门。

已完成的 [G 原十试步组件](../notes/2026-11-14-native-gauge-original-trial-replay-interface.md) 因此先保留，不对上述坏方向执行。

## 2. 源码实际计算链

相关冻结源均为公开课题原代码：

- 78718-tail-fourier-product-jacobian.mjs：205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25。
- 78718-tail-fourier-product-flow.mjs：717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f。
- 78718-tail-fourier-root-momentum.mjs：cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88。
- actual41 单步捕获 geometry_20261114_native_rawcell0_step_windows.mjs：07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b。
- actual43 节点 G system：24a51a4e804859bcdbed78b133599a073c6a0a890039e5fe5500281ef7e90b92。

[原生成链说明](../notes/2026-11-14-native-stage-J-generation-and-propagation-scope.md) 已核实际 consumed-source 身份。局部 A 来自同一次隐式根、有限角矩和解析导数组装。状态与 tangent 随后分别进入同一 RK4 四级；tangent 用普通 binary64 乘加。actual41 只在每个原 RK 步前把 tangent 重置为单位阵，原完整226状态、profile、x/h、四次 root/RHS 和最终 port 均保留。

actual43 读取的是已经形成并保存为 binary64 的短 J，然后用 longdouble 表达式形成节点共轭，再存为新的 binary64 块。提高这一后处理的精度不等于提高此前 local A 或 tangent RK 的精度。

实际旧段43的 [completed report](../notes/public-actions-43622149326-1-rawcell0steps/native-rawcell0-step-capture/stage-043-completed-report.json) 为18731字节，SHA256 95dc94bf3bb5ec288899d38333d652de888b3aeeb986fcc2b1116701383f40b7。其原步11的已报最大绝对 J 条目为45618635198.779976，原 sigma 为3.0069370042341896e-16；这些是报告读数，**最大条目不是条件数**。累计 minA 接近1、minD为1，只证明原守卫这次返回了这些值，不给出 tangent 的增益或精度界。

## 3. 对单个原 RK 步的精确误差拆分

本节先以 A1、A2、A3、A4 表示四个完整局部导数的224×224形状块。固定这四个已经返回的数组和原步长 h，将它们的 binary64 字视为精确实数。这里只定义一个有限数组代数对象，不假设它们是精确连续导数。

对完整形状方向 v，定义

$$
\begin{aligned}
z_1&=v,& k_1&=A_1z_1,\\
z_2&=v+\tfrac h2k_1,& k_2&=A_2z_2,\\
z_3&=v+\tfrac h2k_2,& k_3&=A_3z_3,\\
z_4&=v+hk_3,& k_4&=A_4z_4,\\
\mathcal R[A_1,A_2,A_3,A_4]v
&=v+\tfrac h6(k_1+2k_2+2k_3+k_4).
\end{aligned}
$$

末端若是原 stage 出口，才应用原 port 行变换 P。记

$$
J_*v=P\,\mathcal R[A_1,A_2,A_3,A_4]v.
$$

完整226变化可一并保留。设 C_i 是原两行 mean 对224维形状的导数，定义完整226×226矩阵 $\widetilde A_i=\begin{pmatrix}A_i&0\\C_i&0\end{pmatrix}$，初方向 $\widetilde v=(v,0,0)$；将上述同一递推中的 A_i、v 换成这些完整量即可。shape 对 mean 的两列为零，shape 不依赖 mean；原两行 mean 导数仍作用于 shape，不能用“没有反馈”删去它们的读出。若只比较保存的224×224 shape J，则清楚标为这个子块。

保存的短矩阵记为 Jhat。对指定原方向 v，

$$
E_{\rm propagation}(v)=\widehat Jv-J_*v
$$

可由原有限数组的精确乘加定义。它只隔离**这些局部 A 已经给定之后**形成短 J 的浮点传播、最后保存与 port 计算的影响。此差不包括返回根误差、local A 的角矩/Cholesky/解析表达式误差，亦不包括把离散 RK 导数与连续流导数比较的截断误差。

若实际原 nonlinear RHS 和根足够光滑且导数完全一致，精确 RK 的链式导数才可与上述对象对应；实际根停止规则、有限表和舍入另属一个误差层。不能由本差很小就宣布完整 J 是精确 DF。

节点后处理可写成

$$
\operatorname{fl}(G_{\rm out}\widehat JG_{\rm in}^{-1})
 =
G_{\rm out}J_*G_{\rm in}^{-1}
+G_{\rm out}(\widehat J-J_*)G_{\rm in}^{-1}
+E_{\rm form}.
$$

这里 Eform 按等式定义为节点矩阵形成误差。无论 Eform 多小，已经存在的第二项不会因事后共轭而消失。另一方面，实际原1372线性残差仍只针对 Jhat 组成的原有限矩阵；它并没有直接测这个第二项。

## 4. 一个可完全证明、但不能直接套实际四级的 RK 参照

沿 [R269](../results/R269-native-zero-reference-height-slope-gauge.md)，在精确零形状参考的一个固定位置，令

$$
\gamma=r_x/r,\quad a=m^2-4,\quad
b=\frac{\varepsilon\sqrt{12}\mu}{r^7w},\qquad
A=\gamma
\begin{pmatrix}a&b\\-m^2(m^2-1)/b&-a\end{pmatrix}.
$$

其中 m=2,4,…,224，r,w,mu正且 b非零。直接相乘得

$$
A^2=\gamma^2\{(m^2-4)^2-m^2(m^2-1)\}I
   =-\gamma^2(7m^2-16)I.
$$

在“一个步内 A 恰为常矩阵”的额外参考假设下，RK4 放大矩阵是

$$
R(hA)=I+hA+\frac{h^2A^2}{2}
             +\frac{h^3A^3}{6}+\frac{h^4A^4}{24}.
$$

记 xi=h gamma sqrt(7m^2-16)。两特征值的模平方为

$$
|R(i\xi)|^2
 =\left(1-\frac{\xi^2}{2}+\frac{\xi^4}{24}\right)^2
   +\left(\xi-\frac{\xi^3}{6}\right)^2
 =1-\frac{\xi^6}{72}+\frac{\xi^8}{576}.
$$

所以 xi非零时，该模超过1当且仅当 xi平方超过8。这个事实来自有限多项式恒等式，不是数值特征值估计。

这一参考具有四个明确限制：

1. 原实际四级 A 随 profile、x 和非零状态改变，不能只把一个 geometry 点的 xi 代入就称实际 transfer 的谱。
2. 即使该参考谱模不超过1，非正规矩阵的单步算子范数仍可能很大。
3. 固定同一端点坐标的相似变换不改变这个参考放大因子；两端不同 G 可以改局部欧氏大小，但反代回原变量仍是同一有限传播。
4. 当原完整离散映射自身有大增益，稳定算术只能更准确地表示它，不能把它变成另一个较温和的映射。是否需要同 g 的真正 RK 精化，仍需实际四级和精化证据，不凭此参考公式下结论。

另外，原源码分别返回 w=exp(logw)、w2=exp(2logw)，并使用单独的 Math.sqrt 常数和多条幂/乘除路径。它们作为已存 binary64 数组不自动满足精确 w2=w平方 或精确平方根恒等式。本文参考代数不冒作实际数组的逐位关系，后继实测必须用原全部记录和实际 A。

## 5. R271 的逐级坐标可以稳定什么

[R271](../results/R271-discrete-RK-stage-gauge-covariance.md) 已证明：给定任意可逆的输入、级内、输出坐标 Gin、Gi、Gout，用

$$
\eta_i=G_iG_{\rm in}^{-1}\eta_{\rm in}
       +h\sum_{j<i}a_{ij}G_iG_j^{-1}L_j,\qquad
L_i=G_iA_iG_i^{-1}\eta_i
$$

以及完整输出换算，得到与原有限 RK 实数代数完全相同的传播。不能省略 GiGj逆；也不能把连续 G' 连接项积分的另一套 RK 冒作此递推。

作为有明确参照意义的级内坐标，可在 R269 的

$$
G=
\begin{pmatrix}r^4&0\\m^2r^3&br^3\end{pmatrix}
$$

左侧再乘频率尺度

$$
D_m=\operatorname{diag}\left(1,\frac{r}{\sqrt7\,m}\right),
\qquad H_m=D_mG.
$$

对第4节的同一零形状局部 A，直接代入可得

$$
H_mAH_m^{-1}
 =\gamma
 \begin{pmatrix}
 -4&\sqrt7\,m\\-\sqrt7\,m&4
 \end{pmatrix}.
$$

证明只需先算

$$
GAG^{-1}=
\begin{pmatrix}
-4\gamma&r_x\\
-7\gamma m^2/r&4\gamma
\end{pmatrix},
$$

再作上述对角相似变换。这样局部矩阵没有 mu逆 或 m四次 的条目量级。其对称部分是 gamma乘diag(-4,4)，但**它只是局部乘法矩阵，不是完整连续变换方程**。不能省去 HiHj逆或 H' 后据此宣称全流增长界。若写连续变换，H' H逆必须保留。

同一原 profile 内 mu固定，精确参考的级间矩阵还有明确二元式：

$$
H_iH_j^{-1}
 =\left(\frac{r_i}{r_j}\right)^4
  \begin{pmatrix}
  1&0\\
  \frac{m}{\sqrt7}(1-b_i/b_j)&b_i/b_j
  \end{pmatrix}.
$$

它保留了跨级坐标变化；同 x 的第2/3级局部 A 仍可能因其实际状态不同而不同。实际新入口若采用此思路，所有模式耦合必须保留，不能将完整非零 A 替换为112个独立零参考块。节点还须唯一，不能对同一共享节点用两个略异的原 r/w 位值。端口只在原出口作用一次，四级内部用原 engine Pi 坐标。

选择这样的级内 H 是候选算术表示，不是准确性或稳定性的预先证明。形成 HiAiHi逆 本身若从已舍入的严重相消 A 出发，也可能丢精度；因此必须记录局部 A 与变换形成的实际对象，而不是凭公式免除读回。

## 6. 已可接的最小后继诊断

第一步只是原件摘取：[geometry_20261114_native_stage43_field_receipt.py](../computations/geometry_20261114_native_stage43_field_receipt.py)，SHA256 e796449886bdf19b5053d4c1285dcd5041ae6f852fff20eb6e20481c5fa50dcf。它锁 actual41 result、旧43 report/window/压缩和解压 packet，只复制原步11的四个完整 geometry_number_fields、原 x/h、状态 SHA、guard 与 window。它不计算 gamma、xi、范数或理论阈值。

若这些身份支持进一步对照，最小科学探针可只覆盖**这一个已有原步**：

1. 从 actual41 full_states 取其原完整226输入，恢复原 profile、原 x/h 和原 source/port。使用原 state 算式进行恰四次原 rhsWithJacobian，不加入 ODE 步，不改变 H、far、原容差。
2. 流式保全四份原226×224局部 A、返回 derivative/root/geometry 与完整阶段状态。全部状态/几何 SHA与实际41比，完成步的完整状态及 shape/mean/guard也与实际41比。差异如实记录，不伪造同值。
3. 对已知有限方向执行有限数组精确 action：至少取 actual43 最佳完整方向在该步入节点的原224项，并可加最高模式的 Q/Pi 两列。精确比较 Jhat v 与 Jstar v；原出口 port放在同一位置。
4. 分开保存实际原浮点 tangent、精确四级数组 action、R271候选级内表示的 action，以及各自源/位身份。它们不是同一“新 J”文件。
5. 只有目标的意义清楚以后才扩到全868步。原所有非线性试步仍在完整577节点、原 native no-J流上执行。

对指定方向，四个完整矩阵—向量 action 比重建全部224列的任意精度矩阵更小。h和所有 A/v 是明确 dyadic数；最后除以6只引入已知有理因子，可用整数/有理算术精确累加。此处只是可实施的定义与预算方向，没有运行这个探针或宣称其数值。

该探针不能仅用四个 geometry 记录生成“实际 A”：其完整非线性根和全部角耦合仍必须由原函数返回。也不能从一个最高模式见证推广为所有224列或所有868步都已认证。

## 7. 如何据真实分解选下一步

如果某实际方向的传播差很大，R271级间换算、补偿乘加或更高精度 tangent 形成就有直接对象可改善；新矩阵须有新身份，不能冒 actual41 的原 binary64 短 J。保存状态路径不变与改变变分表示是两个独立声明。

如果传播差很小而原全矩阵线性缺陷仍很大，应优先研究给定矩阵的线性解法/形成/恢复精度；不能把“再换一个节点 G”当作已证明的修复。更高精度或不同稳定消去方式若采用，仍须回原完整数组和原 sigma 读实际缺陷。

如果同四级的更准确 action 或实际同 g 精化表明有限 RK12 本身不能可靠表示所需传播，改变实际 RK 网格是另一项明确的同 g 离散精化。新的配置必须重新绑定真实 native 方程、尾锚、完整响应和最终 audit，旧 RK12 的已完成缓存不能冒作新配置。不能用连续变换方程重新 RK 后仍声称原 RK12 有限映射逐字不变。

如果证据指向 local A 本身，则需要针对原有限 root/角矩/隐式导数的独立一致性检查。节点共轭和稳定 tangent 算术不能修复一个错误的 local A；同样，当前并没有这种错误已经发生的证明。

以上分支用于避免重复无信息的全系统坏方向。它们不是新验收规则，也没有据此宣称本题完成、现有尾已成功或新表示必能得到闭面。
