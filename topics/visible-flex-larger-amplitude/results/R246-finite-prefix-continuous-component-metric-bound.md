# R246 — 旧 .984 有限前缀的连续三分量度量界与浸入

## 状态及准确结论

**已证明的对象：**下文逐字节指定的旧 M96、$s\in[0,0.984]$ 有限有理
quintic 前缀。已有完整计算辅助证明覆盖全部 415 个径向区间和全部角度。
它是前任工作区 2026-11-14 09:29 UTC 完成的**本地历史执行**，不是
当前公开仓库 GitHub Actions 的新回执。本条完整整理其证明，并纠正
“度量误差”的范数范围；不修改任何原输入、证书、源码或历史说明字节。

令 $\theta$ 为下文的共同材料角，参考度量为
$g=ds^2+a(s)^2d\theta^2$，$\varepsilon=10^{-6}$。本条的结论是

\[
\max\left\{
\left|F_s\cdot F_s-1\right|,
\frac{|F_s\cdot F_\theta|}{a},
\left|\frac{F_\theta\cdot F_\theta}{a^2}-1\right|
\right\}<\varepsilon
\tag{1}
\]

在整个参数半柱面上成立，并且 $F$ 是 C² 浸入。由 (1) **直接推出的**
归一化度量误差谱算子界是

\[
\|g^{-1/2}(F^*\langle\cdot,\cdot\rangle-g)g^{-1/2}\|_{\rm op}
<2\varepsilon=2\times10^{-6}.
\tag{2}
\]

本条不将 (2) 改写为 $10^{-6}$ 算子界，不预付 R241 的同名算子封套，
也不宣称本题 README 的全部 metric 条件或整面完成标准已满足。

## 一、完全冻结的有限数学对象

输入为
`../notes/2026-11-14-geometry-resume-scaled-sphere-M96-normal-BVP-r1.json.gz`，
SHA256 为
`3ac8c8efa20670342021487a197443f6e1b2ad60f35c7bf2864f355a06424b69`。
它有 416 个径向节点、415 个区间，每个节点有 290 个物理状态量，
即 $3M+2$，$M=96$。节点值 $Y_j$ 与已保存一阶值 $Y'_j$ 逐项保留。
二阶节点数据单独冻结在
`../notes/2026-11-14-geometry-resume-M96-continuous-metric-second-jets.json.gz`，
SHA256 为
`ea653c839655b88cb0fabf50566f8cece44057c2bf81a4cc06fffdb5d380c9f9`。
每个有限 binary64 数在本条均解释为其准确二进制有理值。

在每个 $[s_j,s_{j+1}]$ 上，状态系数取两端匹配
$(Y,Y',Y'')$ 的唯一五次多项式。二阶数据曾如何用有限 ODE/complex-step
近似生成，不参与这一有限对象的定义；这里没有把多项式内部导数替换
为 ODE 右端。

物理场定义为

\[
F(s,\phi)=R(s,\phi)e_r(\phi)
          +T(s,\phi)e_\phi(\phi)+Z(s,\phi)e_z,
\tag{3}
\]

其中 $R,Z$ 含常数与全部 $\cos(2m\phi)$，$T$ 含全部
$\sin(2m\phi)$，$1\le m\le96$；状态排列是
`r[0:M+1], t[1:M+1], z[0:M+1]`。相邻径向多项式共用同一节点的三个
jets。角向为有限光滑三角和，因此位置、两种一阶导和全部二阶混合导
在径向接缝上相容，(3) 是整个闭参数半柱面上的 C² 映射。

标量 $a$ 保留原 `FixedProfile` 的精确定义：415 个保存的标量节点三
jets 取精确有理值，入口三 jet 按 `exact_original_jet` 的有理原入口
公式替换，每段取同样的唯一 quintic。其精确系数清单散列为
`25a69adae6fc0c238cdc1810793df1054e6a8a4526a562bf1aef1490c5e48b09`。
全部 415 个标量节点逐值出现在上述 416 点场 mesh 中，故每个证明区间
完全落在一个标量多项式片内。这里没有重新拟合或重新设计 $a$。

## 二、材料角及需要验证的不等式

完整 96 个已接受 core 系数为 $c_m$。定义

\[
\theta=\Phi(\phi)=\phi+
\sum_{m=1}^{96}\frac{(1-4m^2)c_m}{2m}\sin(2m\phi),
\]

\[
\rho(\phi)=\Phi'(\phi)=1+
\sum_{m=1}^{96}(1-4m^2)c_m\cos(2m\phi).
\tag{4}
\]

下文的全角证明给出 $\rho>0$。又有
$\Phi(\phi+2\pi)=\Phi(\phi)+2\pi$，所以它给出整个圆周的光滑定向
微分同胚。其系数不随 $s$ 改变，因此材料变换保持径向导数，且
$F_\theta=F_\phi/\rho$。

用原 $\phi$ 坐标记

\[
E=F_s\cdot F_s,\qquad B=F_s\cdot F_\phi,
\qquad C=F_\phi\cdot F_\phi.
\]

注意移动极基必须求导，实际角导的极基分量为

\[
F_\phi=(R_\phi-T,\ T_\phi+R,\ Z_\phi).
\tag{5}
\]

对 $a>0,\rho>0$，以下六个函数严格为正就等价于 (1)：

\[
\begin{aligned}
P_{E,+}&=\varepsilon+(E-1),&P_{E,-}&=\varepsilon-(E-1),\\
P_{B,+}&=\varepsilon a\rho+B,&P_{B,-}&=\varepsilon a\rho-B,\\
P_{C,+}&=(1+\varepsilon)a^2\rho^2-C,
&P_{C,-}&=C-(1-\varepsilon)a^2\rho^2.
\end{aligned}
\tag{6}
\]

它们的径向次数分别至多为 8、9、10；真实物理角频率至多为
$4M=384$。这个频率上限来自 Gram 乘积，不能只按 96 个输入模式计数。
在极基中标量积消去整体基底旋转，所以全部 Gram 函数仍以 $\pi$ 为周期。

## 三、径向 Bernstein 证明

在长度为 $h$ 的一段上，匹配两端
$(y_0,d_0,q_0)$ 和 $(y_1,d_1,q_1)$ 的五次 Bernstein 控制点为

\[
\begin{split}
y_0,\quad y_0+hd_0/5,\quad y_0+2hd_0/5+h^2q_0/20,\\
y_1-2hd_1/5+h^2q_1/20,\quad y_1-hd_1/5,\quad y_1.
\end{split}
\tag{7}
\]

端点求导可直接验证三个 jets。径向导数的 Bernstein 控制为相邻控制
差乘 $5/h$。标量多项式按同一公式构造，并以 de Casteljau 限制到该场
区间；这是原多项式的恒等重写，不改变函数。

两个 Bernstein 基函数的精确乘积为

\[
B_i^p(u)B_j^q(u)=
\frac{\binom pi\binom qj}{\binom{p+q}{i+j}}
B_{i+j}^{p+q}(u).
\tag{8}
\]

以 (8) 逐项构造 $E,B,C,a^2$，再做精确权重的次数提升，即得到 (6) 的
径向 Bernstein 控制函数；每个控制函数仍是有明确最高频率的角三角
多项式。因为 $u\in[0,1]$ 时所有 Bernstein 基非负且和为 1，只要每个
控制函数在全角都为正，该径向区间和全部角上的 (6) 就严格为正。
下节支付的是每个控制函数的**全角**正性，不用有限角样点冒充完整圆周。

## 四、区间 Fourier 与全角 Taylor 外包

本次执行使用全圆角数 `1024`，即 $[0,\pi)$ 上 512 个不同点
$\phi_j=\pi j/512$。频率最大为 384，严格小于这一规则的物理
Nyquist 上限 512。因此准确离散 Fourier 变换能恢复每个控制函数
的全部真实系数；没有遗漏高频或借用频率截断假设。

若一个控制函数写作
$P(\phi)=\sum_k\widehat P_ke^{ik\phi}$，对任何 $\phi$ 选最近网格点
$\phi_j$，则 $|\phi-\phi_j|\le\pi/1024$。Taylor 公式及三角不等式给出

\[
P(\phi)\ge P(\phi_j)-d|P'(\phi_j)|
-\frac{d^2}{2}\sum_k k^2
 \big(|\Re\widehat P_k|+|\Im\widehat P_k|\big),
\tag{9}
\]

只要 $d\ge\pi/1024$。求和项是整个圆周上 $|P''|$ 的上界；因此 (9)
覆盖每个角，不依赖“样点足够密”的未证明推断。

实际使用精确有理数

\[
d=\frac{355}{113\cdot1024}.
\]

该覆盖半径的常数也有完整依据。Machin 恒等式
$\pi=16\arctan(1/5)-4\arctan(1/239)$ 可由正分支的正切加减公式验证。
对第一项 arctan 取五项交错级数上界，对第二项取两项交错级数下界，得到

\[
\pi<\frac{5277328977275528}{1679825970703125}<\frac{355}{113}.
\tag{10}
\]

最后一个差的分子为正整数 `45167474711`（公分母为
$113\cdot1679825970703125$），故比较完全是有理算术。历史条件记录
也逐项保存了 (10) 的验证。

### 实际舍入包络

证明源没有调用普通 FFT 后把误差当零。它自行实现基二区间蝶形：

- binary64 输入转为 `longdouble` 时准确表示；所有实数加、减、乘、除
  的结果分别再向 $-\infty,+\infty$ 作一次 `nextafter`，得到外包；
- 加总通过逐层向外舍入的成对求和，Bernstein 权重先作为准确有理数
  再构造包含它的浮点区间；
- FFT 单位根由半角公式构造，每次平方根端点都转回准确有理数，验证
  下端平方不大于输入下端、上端平方不小于输入上端；必要时继续向外移动；
- 单位根的整数幂及全部复数蝶形乘加也由这些实区间运算组成；
- 对结构上确知为零的带宽外 Fourier 系数，可安全与零相交；不是从
  一个小浮点数猜测它为零；
- (9) 中的样点下界、导数绝对值上界、系数和及最后的 Taylor 余项都
  继续向外舍入。报告写成 binary64 时下界向下、上界向上转换。

本次实际平台报告 `longdouble` 有 64 位有效二进制尾数，NumPy
`2.3.5`，Linux x86_64/glibc 2.41。上述基本运算的外包依据是该平台
有限浮点四则运算再向外扩一个相邻可表示数；平方根另外用准确有理平方
验证，不依赖未经检查的近似根。全部报告界已经检查为有限数。

这说明每个实际计算区间都包含所指定有理 quintic/trigonometric 对象
的准确值。表中的正余量因此是对整个参数域的外包结论，而非样点最大值。

## 五、已经完成的历史证明实例

`geometry_20261114_quintic_metric_interval.py` 的执行源码 SHA256 为
`f19995bfd92bfdabd43fbf2f0fa6956788e74d18e68ceda77fb8405b17299a4a`。
历史执行确实遍历全部 `415/415` 区间，每段全部六类不等式的每个
Bernstein 控制及全部角覆盖均已处理。保存条件记录中的十项检查全部
为真，包括输入散列、jet 维度、标量节点对齐、界有限及每项正性。

| 记录项目 | 历史实际结果 |
| --- | --- |
| `passed` / `all_intervals_checked` | `true / true` |
| 场节点 / 场区间 | `416 / 415` |
| 标量节点 | `415`，全部恰为场 mesh 节点 |
| 完整角规则 | 全圆 `1024`，周期内 `512` |
| 最小记录正余量 | `1.8962168920738398e-08` |
| 材料密度记录下界 | `0.16546471387188874` |
| 标量记录下界 | `0.9999999999999999` |
| 最坏区间 | `[0.983,0.984]`，索引 `414` |
| 最坏项目 | `G_minus`，Bernstein 控制 `10`，角索引 `509` |
| 证书内部计时 | `1076.8941724300385 s` |
| 原进程 wall 时间 | `1080.2680027490023 s` |
| 原进程退出码 / 信号 | `0 / null` |
| 峰 RSS | `106300 KiB` |

以上长小数是保存的向外舍入 binary64 数的展示；其数学含义是相应
二进制数的准确值。特别可保守写成统一余量 $>1.89\times10^{-8}$、
$\rho>0.16546471387$ 及 $a>0$，无需把显示十进制的末位当作额外精度。

原监督记录开始于 `2026-11-14T09:11:27.765165+00:00`，结束于
`2026-11-14T09:29:28.005074+00:00`，没有自动重启。本条后继工作仅
读取保存结果、核对这些元数据/散列和展开论证，没有重新执行这 18 分钟
证明计算。

## 六、浸入和算子界的推导

由全域 (6)、$a>0$ 及 $\rho>0$，在 $(s,\theta)$ 的归一化基底中诱导
Gram 矩阵为

\[
\begin{pmatrix}1+e&f\\f&1+d\end{pmatrix},
\qquad |e|,|f|,|d|<\varepsilon.
\]

其首对角项大于 $1-\varepsilon>0$，且行列式严格大于

\[
(1-\varepsilon)^2-\varepsilon^2
=1-2\varepsilon=\frac{499999}{500000}>0.
\]

故 Gram 矩阵处处正定，$F_s,F_\theta$ 处处线性独立，证明整个有限 C²
场为浸入，包括径向节点处的共享 jets。

对任意 $v\in\mathbb R^2$，误差矩阵 $Q=\begin{pmatrix}e&f\\f&d\end{pmatrix}$
满足

\[
|v^TQv|<\varepsilon(v_1^2+2|v_1v_2|+v_2^2)
\le2\varepsilon\,|v|^2
\]

（$v\ne0$ 时取严格界），于是得到 (2)。三分量门不能一般性地推出
$\|Q\|_{\rm op}<\varepsilon$：例如
$Q=0.9\varepsilon\begin{pmatrix}1&1\\1&1\end{pmatrix}$ 的每个分量均
小于 $\varepsilon$，而算子范数为 $1.8\varepsilon$。这只是说明推理
范围，不声称当前实际场的误差就达到该反例数值。

若需严格验证 $\varepsilon$ 的算子门，可以另证
$\varepsilon I\pm Q$ 的主子式条件；完整四个组合不等式已在
`../notes/2026-11-14-public-metric-interval-replay-interface.md` 推导。
它们没有在这份旧证书中被计算，不能补写为已付。

## 七、证据绑定、复现及未付项目

除上述输入、second-jets 和执行源外，证据散列如下。

| 旧证据 | SHA256 |
| --- | --- |
| 完整压缩报告 `...-continuous-metric.json.gz` | `2e582d42fd9e8f464da7a74bd4d86bd75e14d30250b01e9d42a5d76fc509012c` |
| 解压报告 | `93c3b3eba3405bd777b4ca16416f73c0eb57756546b81e3c5e590e176dc48dc2` |
| `...-continuous-metric-conditions.json` | `d648144e29350ee2be25b6aa030bb2051347869936cedbed63b477195c54046b` |
| `...-continuous-metric-resource.json` | `0cd14580a2cc89c006e3f36766518886e36dc01a796484ffe548de4fda56dfe8` |
| `...-continuous-metric-execution.json` | `43d09ab468627427347dba4e4302b26344e862dd5d7e6399b94d26eb7fef5695` |

这些文件的完整共同前缀是
`../notes/2026-11-14-geometry-resume-M96`。原 26 件交接的恢复清单另见
`../notes/2026-11-14-geometry-post43-recovery-manifest.json`。准确命令和
后续输入接口见 `../notes/2026-11-14-public-metric-interval-replay-interface.md`。
未来公开复现应使用原 `--angles 1024`、全部区间和原 frozen second-jets，
并读取报告 `passed` 字段；程序的正常退出本身不等于正性全部通过。

本实例未覆盖 `.99`、`.9975`、新的 complete fullDN、任何 tail/collar
或完整闭曲面；旧二阶节点数据不能移植到新场。旧源直接要求固定五次
标量结构，不能以另拟五次函数替代新 fullDN 冻结的完整 scalar 公式。
它也不证明固定 $g$ 加密极限、精确等距存在、嵌入、reach、整面幅度或
`delta_E > 0`。其连续三分量界和浸入是实质有限场结论，但本课题仍未
完成。
