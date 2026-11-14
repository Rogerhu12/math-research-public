# 完整参考段与全实时间的复角像

本文与 `scripts/fourfold_complete_reference_segment.py` 同步，处理准确
δ₅ retarget reference 的有限函数定义。它不把 δ₄ 原 trace 称为 δ₅ 真流，
也不自动给出残差、真流误差或 \(q=Y_x\) 下界。

## 1. 对象和完整乘积

接口

```python
ref = RetargetReference(descriptor_path)
segment = CompleteReferenceSegment(ref, leg, number, left=0, right=1)
full = segment.complete_periodic()
gate = segment.real_time_image(Fraction(1, 128), nodes=512, p=8)
```

`CompleteReferenceSegment` 继承已冻结 `NativeRetargetSegment` 的输入验证、
准确时间、分支符号、原始 shard 与 retarget 身份，不增加 `package` 属性。
`complete_periodic()` 直接调用已冻结 `PackageReference` 的完整 Laurent
乘积算法，保留全部八个时间系数和所有乘积频率。它返回真实指定 subspan
上的单项式时间表示，所以原来的 `continuous_bidisk` 可以直接使用。
保存的系数球是同一准确有限函数的包络，不能把其中点选作一个新的参考。

实时间像门另取原整段的八个 Bernstein 控制函数。若原参考及辅助函数为

\[
U(s,x)=\sum_{j=0}^7 B_j^7(s)U_j(x),\qquad
Q(s,x)=\sum_{j=0}^7 B_j^7(s)Q_j(x),\quad0\le s\le1,
\]

令 \(A(x)=a(x)\)（前腿），或 \(A(x)=Q_{f,\rm end}(x)a(x)\)（后腿）。
全部 Laurent 乘积准确物化，得到

\[
C_j(x)=U_j(x)+Q_j(x)A(x),\qquad
Y_j(x)=x/4+C_j(x),\qquad
Y(s,x)=\sum_{j=0}^7 B_j^7(s)Y_j(x).
\tag{1}
\]

初值修正 \(a\) 从保存的整数／二的幂分母读取；原 \(U_j,Q_j\) 的
binary64 系数作为准确 dyadic 输入读取。后腿静态 \(Q_{f,\rm end}\)
也保留全部频率。当前前腿完整乘积次数为644，不能裁回原 U 的516阶。

若指定准确 subspan \([l,r]\subset[0,1]\)，函数仍由同一 (1) 在其
子区间取值。像门允许直接继承原整段的更强界；这和 `complete_periodic`
返回准确受限单项式系数的口径没有矛盾。

## 2. 虚部边界的实 Fourier 多项式

每个 \(C_j\) 在实轴上实，写

\[
C_j(x)=c_{j0}+\sum_{k=1}^K
    \{c_{jk}e^{ikx}+\overline{c_{jk}}e^{-ikx}\},
\quad c_{j0}\in\mathbf R.
\]

对真实 \(x\)，直接相减给出

\[
\Im Y_j(x+iS)
=\frac S4+\sum_{k=1}^K
 \{i c_{jk}\sinh(kS)e^{ikx}
  +\overline{i c_{jk}\sinh(kS)}e^{-ikx}\}.
\tag{2}
\]

因此这本身是**实**的完整有限 Fourier 多项式：正频率系数为
\(i c_{jk}\sinh(kS)\)，常数项准确为 \(S/4\)。没有把 \(C_j\) 的
完整模数或者复时间盘的变化加到虚部预算里。

## 3. 闭角单元上的 Taylor 余项

设 (2) 的系数为 \(d_k\)，取节点 \(x_\ell=2\pi\ell/N\)、
闭单元半宽 \(h_x=\pi/N\)。所有频率在每个节点的值通过有向 native
DFT 求出。高频先按模 N 加入有限频率槽只是**同一点的精确求值**，
不把函数裁成 N/2 阶，也不遗漏 alias。

记

\[
T_{r\ell}=\frac{h_x^r}{r!}
       \sum_{k=-K}^K(ik)^r d_k e^{ikx_\ell},\qquad0\le r\le p.
\]

对每个实 \(|v|\le h_x\)，实角方向的积分 Taylor 余项满足

\[
\left|\sum_k d_ke^{ik(x_\ell+v)}
 -\sum_{r=0}^p T_{r\ell}(v/h_x)^r\right|
\le R_{p+1}:=
\frac{2}{(p+1)!}\sum_{k=1}^K|d_k|(kh_x)^{p+1}.
\tag{3}
\]

因为积分路径是实角方向，\(|e^{ikx}|=1\)，(3) 不需要额外的
\(e^{|k|h_x}\)。代码将全部频率的 (3) 有向加上，得到每个闭单元界

\[
\sup_{|v|\le h_x}|\Im Y_j(x_\ell+v+iS)|
\le \sum_{r=0}^p |T_{r\ell}|+R_{p+1}.
\tag{4}
\]

实值性质使每个 \(T_{r\ell}\) 的精确虚部为零；区间计算先核其虚部
包住零，再取实部包络。全部 N 个闭单元在周期圆上完整覆盖，端点没有
开缝。报告保存每个控制函数的完整余项、全单元上界和最弱单元索引。

## 4. 从边界到全标签带，再到全实时间

\(\Im Y_j\) 对标签复变量调和，且在实方向周期；其线性项 \(x/4\)
的虚部也是周期函数。对紧复圆柱的调和最大／最小值原理，边界
\(\Im x=\pm S\) 的绝对值界控制整带。实系数给出准确共轭对称，
下边界的虚部是上边界的相反数，因此只须支付 (2) 的上边界。

对所有实 \(0\le s\le1\)，Bernstein 权重满足
\(B_j^7(s)\ge0\)、\(\sum_jB_j^7(s)=1\)。由 (1)，

\[
\boxed{\sup_{s\in[0,1],\,|\Im x|\le S}|\Im Y(s,x)|
\le \max_{0\le j\le7}\sup_{x\in\mathbf R}|\Im Y_j(x+iS)|.}
\tag{5}
\]

这是实时间结论；没有要求参考在一个复时间圆上保持相同小虚部。
`continuous_bidisk` 的完整复时间像／q 门仍是独立预算，不由 (5) 代付。

## 5. 实际完成的输入与数值

准确 descriptor SHA
`097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052`
固定 δ₄ 原 reference 与 δ₅ target／H 的 retarget 定义。
使用256 bits、N=512、p=8，对前腿0、419、549三个完整实际参考段运行。
所有段均保留八个控制函数、全部644阶乘积频率。下表是报告有向上界的
向上简写；严格端点和逐控制余项保存在 JSON 中。

| 前腿段 | 标签带 S=1/512 的物理像宽度 | 标签带 S=1/128 的物理像宽度 |
|---|---:|---:|
| 0 | <0.000867880242 | <0.003471863101 |
| 419 | <0.001046550905 | <0.004190427421 |
| 549 | <0.000867875862 | <0.003471910839 |

六个界均小于物理角1/64，但应用时仍必须逐段匹配同一个实际场域，
不能把419的域直接授给其他段。报告
`data/phase_ring_continuation/type_fixed_step02_d5_step5_complete_reference_real_time_images_0_419_549.json.gz`
保存了所有输入 shard 哈希和准确时间口径。

每段另做两条互补完整函数检查：两个非实时间、16个角，逐一比较
原符号乘积与物化后的 \(Y,Y_u,Y_x\)；三个实时间，比较全部 Fourier
系数的原 Bernstein 与受限单项式时间表示。所有区间均重合。
这些检查支持实现的一致性；全实时间和全标签的结论来自 (1)–(5)，
不是从有限测试点外推。

## 6. 后续使用范围

此门可以支付真实场与有限场多项式的差在参考复合后的实时间费用，
前提是同一 physical image 严格含于该实际场的角域。它不包含真实场
本身的截断误差、\(q\) 下界、参考时间导数、密度或有序积分的误差，
也没有认证完整两腿返回或等距曲面的存在。
