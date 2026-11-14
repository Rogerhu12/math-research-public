# R211：实际曲率谱 hinge 的四次放大与完整参数链

**状态：完整有限目标构造及链式证明已完成；原谱分支和实际完整小场核已真实执行。**
本结果针对已观察到的局部曲率尖峰给出一个明确的新数值目标。
它不改变位置场、度量残差、guide 阈值、样本点或原外权；
不证明真实曲率已受限，不是 reach 证书，也不宣称主线新目标已经接受任何步。

## 1. 原实际三维谱残差

沿用 R191 实际位置两 jet 算出的正交形算子

$$
S=\begin{pmatrix}S_{11}&S_{12}\\S_{12}&S_{22}\end{pmatrix}.
$$

它由实际 $X_s,X_u,X_{ss},X_{su},X_{uu}$、实际 Gram 和单位法向计算，
不是参考曲面的第二基本形式或忽略相位链后的近似。
固定原正数 guide $C$，设

$$
f_C(x)=
\begin{cases}x-C&x>C,\\0&|x|\le C,\\x+C&x<-C.\end{cases}
$$

准确谱函数 $Q=f_C(S)=S-\operatorname{clip}(S,[-C,C])$，
原 R191 三行残差是

$$
r=(Q_{11},\sqrt2Q_{12},Q_{22})^\mathsf T,\qquad
q=r^\mathsf Tr=\|Q\|_F^2
=\sum_{i=1}^2\max(0,|\kappa_i|-C)^2.
$$

原函数、源码身份及完整各参数变化链保持：
scripts/fd2d-position-curvature-chain-R191.cjs，
SHA256 d30e2fe21ca065a84776313d8ababba2a8eccc6693e5f60a5c7ba3628652d812。

## 2. 新残差、真实目标与零集合

本定义固定 $\tau=2$，并令

$$
h=\sqrt{1+\frac q{\tau^2}}=\sqrt{1+\frac q4},
\qquad \widetilde r=hr.
$$

因此准确地

$$
\boxed{\|\widetilde r\|^2=q+\frac{q^2}{4}.}
$$

这里的 $q$ 是**每个实际曲率点、尚未乘径向/角向/总权的原三行范数平方**。
对原固定非负采样权 $\omega_\ell$，新曲率目标为

$$
\sum_\ell\omega_\ell\left(q_\ell+\frac{q_\ell^2}{4}\right).
$$

不能先把全部点的残差拼成一个向量再作此变换，
也不能把 $\omega_\ell$ 无声放进 $q_\ell$。
原 degree、节点、G2/物理 knots、角规则、nodeShare 和外 curvature weight 均保留。
完整目标还含原度量与已选几何行时，只替换这部分曲率目标。

由于 $h\ge1$，新旧零集合完全相同：
$\widetilde r=0$ 当且仅当全部实际 $|\kappa_i|\le C$。
标量 $q\mapsto q+q^2/4$ 在 $q\ge0$ 严格递增；
同一固定场的新曲率值大于等于原曲率值，故新 baseline 的增大不能被误称为场退步。
它是原两个谱超量平方之和的平方，含交叉项；
一般不等于分别给每个特征值加四次项的和。

该目标更重视所评点上的大超量，但不能由目标下降推出每一点最大曲率下降，
也不能证明未采样点或连续全域曲率受限。guide 仍是原数值指导，不变成几何完成门。

## 3. 完整一阶链、gradient 和 Gauss–Newton normal

对任一真实参数方向，有

$$
Dq=2r^\mathsf TDr,\qquad Dh=\frac{r^\mathsf TDr}{\tau^2h}.
$$

于是

$$
\boxed{D\widetilde r=h\,Dr+
       r\frac{r^\mathsf TDr}{\tau^2h}.}
$$

等价地，记原 $J=Dr$ 和

$$
B=hI+\frac{rr^\mathsf T}{\tau^2h},
\qquad \widetilde J=BJ.
$$

整个映射 $r\mapsto r\sqrt{1+\|r\|^2/4}$ 在 $\mathbb R^3$ 上光滑，
而且 $h\ge1$；在 $r=0$ 不需要除 $q$、曲率特征值或 $\|r\|$，
不用任何隐蔽 floor 或 damping。

按半平方和梯度的原约定，

$$
\widetilde J^\mathsf T\widetilde r
=\left(1+\frac{2q}{\tau^2}\right)J^\mathsf Tr.
$$

单点 Gauss–Newton 项为

$$
\widetilde J^\mathsf T\widetilde J
=J^\mathsf T\left[
 h^2I+\left(\frac2{\tau^2}
       +\frac q{\tau^4h^2}\right)rr^\mathsf T
 \right]J.
$$

外权 $\omega_\ell$ 在这些式子外相乘，随后与原其它残差 normal 相加。
其列缩放、阻尼和受限方向必须由新 normal 正常产生；
不能把旧目标的 scaled Schur 或方向冒作新目标的准确方向。

$B$ 仅混合同一个空间点的三行，故没有引入新的参数支撑。
原全部 theta 正弦/余弦/常数、psi 正弦/余弦、Z、rho、
全局 cutHeight、全局 A，以及 $\beta_p,\beta_{sp},\beta_{ssp}$ 都通过原 $J$ 保留。
原实际局部 block、两个 global border 及带外非零审计仍适用；
这里没有删除任何微小项或借三带假设丢弃第四带。

## 4. 所有谱分支与阈值约定

R211 不重新实现 $f_C(S)$。它原样调用冻结 R191 的 hinge：

- 两个特征值均处正活动区、均处负活动区，或者均在闭 inactive 区时，
  原源使用准确 affine 分支，包含相同特征值；
- 其余分支特征值不同，原源使用谱 divided difference；
- 在准确 $+C$ 或 $-C$，标量选取的 inactive slope 为 0；
  这是原广义导数约定，不是声称残差在 kink 处光滑。

把原选择的广义导数 $J$ 左乘光滑映射的 $B$，
就是相同分支约定下的新广义导数。
若两特征值都准确位于同一个阈值，原选择 $J=0$，则新选择仍为 0。
若一条特征值在阈值、另一条活动，原 divided-difference 的旋转项仍完整保留，
不能仅把阈值所在坐标行粗暴清零。

平方目标是凸谱盒的距离平方 $q$ 再复合递增光滑标量函数，
所以它在形算子变量中有连续一阶梯度；
这不使残差在谱 kink 处变成经典可微函数，也不使原位置参数问题变成凸优化。

实际分支核覆盖 18 个 case：全部 inactive、同号活动、异号活动、活动与 inactive，
各自重复或不同特征值，以及准确正/负/双侧阈值的组合。
远离阈值的中心有限差分最大 scaled 误差为 $6.038\times10^{-9}$。
阈值处核原 flag、原 inactive 选择和完整组合链；
没有拿错误的双侧光滑导数假设去“验证”一个 kink。

## 5. 独立 wrapper 与注入要求

新源码：

scripts/fd2d-curvature-quartic-hinge-R211.cjs，
SHA256 00609f37b5611d549a85dcdecc61234684c6eb3df2597f61485caa08a15b3f26。

接口 createR211AmplifiedCurvatureAlgebra(original,{tau:2}) 返回：

- curvature 与 variation：分别为原函数的同一引用；
- hinge：只包装原 residual、squared、apply；
- definition：明确 R211 schema、固定 tau、新目标、原 threshold 约定和范围。

该返回对象可以注入原 factory 的 algebra 参数。
构造新目标的调用方必须把此 definition 保存进自己的新目标身份，
并把任何继承的“平方目标仍只是两个谱 hinge 平方和”标志改为新的明确公式。
不能沿旧 objective identity 存新 residual，更不能把新目标范数下降当成原目标下降。

对溢出的真实放大残差或导数，wrapper 明确抛错；
没有裁剪残差、放松 guide、隐蔽平移或添加额外函数列。
原曲率函数的浸入检查也保持原样。

## 6. 完整 30 参数实际场的小核

使用已推 B32 实际 candidate，
R196 非均匀基工厂的 $J=4$ 简单均匀 knots、$K=1$、全周等价 $N=16$，
构造完整 R201+R205 变幅位置场。guide=9.5、weight=0.01、nodeShare=0.5。
全部 30 个参数、两个混合方向和所有 source SHA 均存报告；
theta、psi、height、rho 与新增非反射对称列均明确非零，A=0.25，
cutHeight 系数为 -0.12。

这是一份专为链式核对定义的小场，**不是主线接受态或改善候选**。
它的实际采样曲率峰约 1443.73，明显不合格。其意义是产生非零实际曲率行、
非零相位 S、非零 A/cut 列，并真实检验所有完整链式。

只组装一张 $30\times30$ normal，7749 个真实有限残差行，194 个活动曲率点。
一次包含全部径向通道、A 与 cut 的混合中心差分给：

- 完整加权 residual 的 JVP relative L2：$1.006\times10^{-9}$；
- 最大 scaled JVP 误差：$1.156\times10^{-9}$；
- 半目标方向导数相对误差：$2.058\times10^{-9}$。

同一张 normal 与完整实际 JVP/残差核对：
$d^\mathsf THd=\|Jd\|^2$、A 方向二次型、
两个方向交叉项、$g^\mathsf Td=r^\mathsf TJd$，
最大相对误差不超过 $3.321\times10^{-15}$。
H 对称性和 diagonal 复制差为 0。

在该场实际最坏点，原/新 algebra 下的完整 X 两 jet、
全部活动参数两 jet、相位 C/S/R 和实际谱值逐位相同。
A 与 cut 列都存在且非零，其两 jet 范数分别约 7.533 和 8.010。
相位 S 约 $8.573\times10^{-6}$，故不是把原反射对称的零相位列当非零检查。

小场完整执行耗时 8.354 秒；其中唯一小 normal 为 3.060 秒。
全部为纯 V8，未创建 OS 子进程，未组 932/1025 维 normal，
未作 LM 或更新任何主态。有限 angular/radial quadrature 未在本核中变成连续证书。

## 7. 重生与真实执行记录

scripts/fd2d-R211-complete-small-check.cjs 含实际执行的两个函数原文，
导出 runR211SpectralCheck、runR211SmallFieldCheck、runR211CompleteCheck。
其 Node CLI 可从真实 candidate 重新生成这一个小组；
CLI 本身只做语法编译，未冒已在 OS 执行。

实际报告：
notes/2026-11-13-fd2d-R211-spectral-and-complete-small-field-report.json。

首个准备调用误返回未调用的函数，被 store 序列化拒绝，未执行谱核。
第一次谱 fixture 又错误要求两个不同结合次序的浮点链式逐位一致，
观察最大 scaled 差 $1.919\times10^{-16}$；最终改为明确的
$64\,\mathrm{Number.EPSILON}$ 算术核对预算，wrapper 数学源未变。
这两条准备/fixture 记录完整保留，不伪造成实际场失败或 OS 退出。

本结果允许根代理以新身份重算主线 baseline/normal，并实际比较步长。
它没有预付该新目标的任何真实接受、连续曲率阈值或全局几何结论。
