# R720　固定前三矩时完整当前核心的轴比与轴差加强

2026-11-27，construction，GPT-6 Astra Pro，AI-assisted。

**状态：完整条件性解析证明；未执行科学、数值积分、CAS、采样或候选计算。** 本文在 [R719](R719-fixed-first-three-fejer-modes-preserve-current-axis-gap.md) 的相同条件下，将完整当前核心的统一轴比提高到 $8/3$，将统一轴差提高到 $21/25$。全部当前高模保留；结论不支付实际场的连续正性、整张闭面的 Hausdorff 距离、共同支持、直径或 reach。

新步骤是将正曲率半径看成概率密度。固定前三 Fourier 系数给出前三个准确矩；两个 Cauchy–Schwarz 不等式给小轴上界，另一个加权 Cauchy–Schwarz 不等式把未知第四矩限制在前三矩之内。所有 RN-even64 舍入费用在下文逐项保留。

## 1. 完整当前对象与主结论

沿用 R719 的完整当前核心
$$
p(\theta)=1+\sum_{j=1}^{M}c_j\cos(2j\theta),\qquad
\rho(\theta)=p(\theta)+p''(\theta)
=1+\sum_{j=1}^{M}(1-4j^2)c_j\cos(2j\theta),
\qquad M\ge3.
\tag{1}
$$
假设准确的连续条件
$$
\rho(\theta)>0\qquad\text{对所有 }\theta\in\mathbb R.
\tag{2}
$$
它必须属于同一个完整当前点。有限角网上的正值、某次 root 成功、工作日志或 reference 的正性均不能替代 (2)。

前三个系数仍为 [R717](R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 固定 recipe 的最近偶数 binary64 值，并按准确二进有理数解释：
$$
c_1=\frac7{16},\qquad
c_2=-\frac3{40}+\delta_2,\qquad
c_3=\frac3{112}+\delta_3,\qquad
|\delta_2|,|\delta_3|\le\epsilon:=2^{-53}.
\tag{3}
$$
$c_1$ 准确可表示，没有它的额外舍入项。其余 $c_4,\ldots,c_M$ 均任意自由，只须与前三项共同满足 (2)。没有令它们为零，没有假设它们保持初始七模的值，也没有将 current M320 回退为 reference M160。

记准确支撑曲线
$$
\Gamma(\theta)=p(\theta)e_r(\theta)+p'(\theta)e_t(\theta),
$$
以及其两半轴
$$
X=p(0)=1+\sum_{j=1}^{M}c_j,\qquad
Y=p(\pi/2)=1+\sum_{j=1}^{M}(-1)^jc_j.
\tag{4}
$$
令
$$
C_{\rm RN}:=\frac{229645}{200704}<2.
\tag{5}
$$

**命题。** 对满足 (1)–(3) 的任意有限 $M\ge3$，
$$
X>0,\qquad Y>0,
\tag{6}
$$
并有
$$
\boxed{\;
X-\frac83Y>
\frac{\pi}{2}
\left(\frac{128707}{86016000}-C_{\rm RN}\epsilon\right)>0,
\qquad
\frac XY>\frac83.
\;}
\tag{7}
$$
同时
$$
\boxed{\;
X-Y>
\frac{21}{25}
+\frac{11233}{2048000}
-\frac{13659}{10240}\epsilon
>\frac{21}{25}.
\;}
\tag{8}
$$
这些严格余量均为准确表达式。证明不使用浮点近似的 $\pi$、开方结果或实际未返回的系数数组。

## 2. 正密度、轴积分与三个固定矩

由 (1) 的 Fourier 正交性，
$$
\int_0^\pi \rho(\theta)\,d\theta=\pi.
$$
因此
$$
d\mu(\theta)=\frac{\rho(\theta)}{\pi}\,d\theta,
\qquad 0\le\theta\le\pi
\tag{9}
$$
是概率测度。定义
$$
z=\cos^2\theta,\qquad
m_k=\mathbb E_\mu[z^k].
\tag{10}
$$
于是 $0\le z\le1$。

R719 的准确轴积分也可由 $\Gamma'=\rho e_t$ 及原反射对称直接得到：
$$
X=\frac12\int_0^\pi\rho(\theta)\sin\theta\,d\theta,\qquad
Y=\frac12\int_0^\pi\rho(\theta)|\cos\theta|\,d\theta.
$$
因而
$$
\boxed{\quad
X=\frac{\pi}{2}\mathbb E_\mu\sqrt{1-z},\qquad
Y=\frac{\pi}{2}\mathbb E_\mu\sqrt z.
\quad}
\tag{11}
$$
(2) 使两个被积函数分别在正测度开区间上严格为正，所以 (6) 成立。无需用某个不相干的数值曲线判断轴的符号。

有限三角恒等式为
$$
\begin{aligned}
\cos^2\theta&=\frac{1+\cos2\theta}{2},\\
\cos^4\theta&=\frac{3+4\cos2\theta+\cos4\theta}{8},\\
\cos^6\theta&=\frac{10+15\cos2\theta+6\cos4\theta+\cos6\theta}{32}.
\end{aligned}
\tag{12}
$$
对任意 $j\ge1$，
$$
\mathbb E_\mu\cos(2j\theta)=\frac{(1-4j^2)c_j}{2}.
$$
代入 (12)，得到
$$
\begin{aligned}
m_1&=\frac12-\frac34c_1=\frac{11}{64},\\
m_2&=\frac38-\frac34c_1-\frac{15}{16}c_2
=\frac{15}{128}-\frac{15}{16}\delta_2,\\
m_3&=\frac5{16}-\frac{45}{64}c_1-\frac{45}{32}c_2-\frac{35}{64}c_3\\
&=\frac{49}{512}-\frac{45}{32}\delta_2-\frac{35}{64}\delta_3.
\end{aligned}
\tag{13}
$$

所有当前 $c_j$，$j\ge4$，在 (13) 中消失的原因是**准确 Fourier 正交性**。它们仍在 $\rho$、概率测度、第四及更高矩、曲线和全部当前变量中。这里没有把原完整场投影成三模场。

## 3. 小轴的两项 Cauchy 上界

对 $0\le z\le1$，恒等地有
$$
\sqrt z=\sqrt z(1-z)+z^{3/2}.
$$
先对函数 $\sqrt z(1-z)$ 与常数 $1$ 用 Cauchy–Schwarz，再对 $\sqrt z$ 与 $z$ 用同一不等式：
$$
\begin{aligned}
\mathbb E_\mu\sqrt z
&=\mathbb E_\mu[\sqrt z(1-z)]+\mathbb E_\mu[z^{3/2}]\\
&\le
\sqrt{\mathbb E_\mu[z(1-z)^2]}
+\sqrt{\mathbb E_\mu z\,\mathbb E_\mu z^2}\\
&=\sqrt A+\sqrt B,
\end{aligned}
\tag{14}
$$
其中
$$
\begin{aligned}
A&=m_1-2m_2+m_3
=\frac{17}{512}+\frac{15}{32}\delta_2-\frac{35}{64}\delta_3,\\
B&=m_1m_2
=\frac{165}{8192}-\frac{165}{1024}\delta_2.
\end{aligned}
\tag{15}
$$
$A$ 与 $B$ 的非负性也直接来自各自的期望表达式。由 (3)，
$$
A\le\frac{17}{512}+\frac{65}{64}\epsilon,\qquad
B\le\frac{165}{8192}+\frac{165}{1024}\epsilon.
\tag{16}
$$

以下两个有理余量是准确的平方差：
$$
\left(\frac{729}{4000}\right)^2-\frac{17}{512}
=\frac{191}{16000000},
\tag{17}
$$
$$
\left(\frac{568}{4000}\right)^2-\frac{165}{8192}
=\frac{2867}{128000000}.
\tag{18}
$$
两者都大于 $1/10^6$。另一方面，
$$
\frac{65}{64}\epsilon<2\epsilon=2^{-52}
<2^{-20}<\frac1{10^6},\qquad
\frac{165}{1024}\epsilon<\epsilon<\frac1{10^6},
\tag{19}
$$
其中 $2^{20}=1048576>10^6$ 给出最后一个严格有理比较。因此
$$
\sqrt A<\frac{729}{4000},\qquad
\sqrt B<\frac{568}{4000}.
$$
由 (14)，
$$
\boxed{\quad
\mathbb E_\mu\sqrt z<\frac{1297}{4000}<\frac{13}{40},
\qquad
Y<\frac{1297\pi}{8000}.
\quad}
\tag{20}
$$
开方界来自严格平方比较；没有执行开方或把显示小数当作准确上界。

## 4. 覆盖整个 $[0,1]$ 的两条多项式下界

准确二项式级数写为
$$
\sqrt{1-z}=1-\sum_{n=1}^{\infty}a_nz^n,\qquad
a_n=\frac{\binom{2n}{n}}{4^n(2n-1)}>0,
\qquad 0\le z<1.
\tag{21}
$$
前三项为 $a_1=1/2$、$a_2=1/8$、$a_3=1/16$。令 $z\uparrow1$，由正项的单调收敛，$\sum_{n\ge1}a_n=1$。因此级数在端点也有相同有限和，且
$$
\sum_{n\ge3}a_n=\frac38,\qquad
\sum_{n\ge4}a_n=\frac5{16}.
$$
在 $[0,1]$ 上，对所有 $n\ge k$ 都有 $z^n\le z^k$，所以
$$
\boxed{\quad
\sqrt{1-z}\ge
1-\frac z2-\frac{z^2}{8}-\frac{3z^3}{8},
\qquad 0\le z\le1,
\quad}
\tag{22}
$$
以及
$$
\boxed{\quad
\sqrt{1-z}\ge
1-\frac z2-\frac{z^2}{8}-\frac{z^3}{16}
-\frac{5z^4}{16},
\qquad 0\le z\le1.
\quad}
\tag{23}
$$
这两条都是包括 $z=1$ 的全区间下界，而非远离端点的局部 Taylor 截断。第四次项的 $5/16$ 是完整正尾的和，不是把单个 Taylor 系数当作全尾。

## 5. 正测度给未知第四矩的上界

记
$$
d=m_1-m_2=\mathbb E_\mu[z(1-z)],\qquad
n=m_2-m_3=\mathbb E_\mu[z^2(1-z)].
\tag{24}
$$
由于 $\rho>0$ 且 $0<z<1$ 在正测度开集成立，$d>0$，$n>0$。

对两个非负平方可积函数
$$
a(z)=\sqrt{z(1-z)},\qquad
b(z)=\sqrt{z^3(1-z)}
$$
应用 Cauchy–Schwarz，
$$
n^2=(\mathbb E_\mu[ab])^2
\le\mathbb E_\mu[a^2]\mathbb E_\mu[b^2]
=d(m_3-m_4).
$$
故
$$
\boxed{\quad
m_4\le m_3-\frac{(m_2-m_3)^2}{m_1-m_2}
=m_3-\frac{n^2}{d}.
\quad}
\tag{25}
$$
$m_4$ 包含自由第四模及当前完整正密度的影响。式 (25) 约束它，没有假定它等于参考值，更没有删除第四模或更高模。

将 (25) 代入 (23) 的期望，注意 $m_4$ 前的系数是负数，得到
$$
\begin{aligned}
\mathbb E_\mu\sqrt{1-z}
&\ge1-\frac{m_1}{2}-\frac{m_2}{8}
-\frac{m_3}{16}-\frac5{16}m_4\\
&\ge L_3+\frac5{16}\frac{n^2}{d},
\end{aligned}
\tag{26}
$$
其中
$$
L_3:=1-\frac{m_1}{2}-\frac{m_2}{8}-\frac38m_3.
\tag{27}
$$
下一个环节保留 (26) 中实际分母与全部舍入误差，而不是只评价理想前三矩。

## 6. 第四矩加强的完整 RN 误差

由 (13)，准确地有
$$
L_3=
\frac{3537}{4096}
+\frac{165}{256}\delta_2+\frac{105}{512}\delta_3
\ge\frac{3537}{4096}-\frac{435}{512}\epsilon.
\tag{28}
$$
同时
$$
\begin{aligned}
d&=d_0+\frac{15}{16}\delta_2,
&d_0&=\frac7{128},\\
n&=n_0+\frac{15}{32}\delta_2+\frac{35}{64}\delta_3,
&n_0&=\frac{11}{512}.
\end{aligned}
\tag{29}
$$
设
$$
a=\frac{65}{64},\qquad b=\frac{15}{16}.
$$
则
$$
n\ge n_0-a\epsilon>0,\qquad
0<d\le d_0+b\epsilon.
\tag{30}
$$
其中正性也可以直接用 $\epsilon<1/128$ 检查：
$$
n_0-\frac a{128}=\frac{111}{8192}>0,\qquad
d_0-\frac b{128}=\frac{97}{2048}>0.
$$
因此
$$
\frac{n^2}{d}\ge
\frac{(n_0-a\epsilon)^2}{d_0+b\epsilon}.
\tag{31}
$$
与理想比值的差准确写为
$$
\frac{n_0^2}{d_0}-
\frac{(n_0-a\epsilon)^2}{d_0+b\epsilon}
=
\frac{(n_0^2b+2d_0n_0a)\epsilon-d_0a^2\epsilon^2}
     {d_0(d_0+b\epsilon)}.
\tag{32}
$$
由正分母，或分别估计减小分子与增大分母的两个非负损失，可得
$$
\frac{n_0^2}{d_0}-
\frac{(n_0-a\epsilon)^2}{d_0+b\epsilon}
\le
\left[\left(\frac{n_0}{d_0}\right)^2b
+2\frac{n_0}{d_0}a\right]\epsilon
=\frac{11825}{12544}\epsilon.
\tag{33}
$$
这里 $n_0/d_0=11/28$，两个有理项分别是
$$
\frac{1815}{12544},\qquad
\frac{715}{896}=\frac{10010}{12544}.
$$
所以所有分母扰动已显式包含。

理想比值及完整理想下界为
$$
\frac{n_0^2}{d_0}=\frac{121}{14336},\qquad
\frac{3537}{4096}+\frac5{16}\frac{121}{14336}
=\frac{198677}{229376}.
\tag{34}
$$
合并 (26)、(28)、(31)–(34)，
$$
\boxed{\quad
\mathbb E_\mu\sqrt{1-z}
\ge\frac{198677}{229376}
-\left(\frac{435}{512}
+\frac5{16}\frac{11825}{12544}\right)\epsilon
=\frac{198677}{229376}
-\frac{229645}{200704}\epsilon.
\quad}
\tag{35}
$$
这就是 (5) 的完整费用。$229645<2\cdot200704$，故 $C_{\rm RN}<2$；本文没有把两个 RN 误差设零。

## 7. 轴比严格超过 $8/3$

由 (20)，
$$
\frac83\,\mathbb E_\mu\sqrt z
<\frac83\frac{1297}{4000}=\frac{1297}{1500}.
$$
相应理想有理余量为
$$
\frac{198677}{229376}-\frac{1297}{1500}
=\frac{128707}{86016000}>\frac1{1000}.
\tag{36}
$$
最后一个比较等价于 $128707>86016$。

由 (19)，$C_{\rm RN}\epsilon<2\epsilon<1/10^6$。所以 (35)–(36) 给出
$$
\mathbb E_\mu\sqrt{1-z}
-\frac83\mathbb E_\mu\sqrt z
>
\frac{128707}{86016000}-C_{\rm RN}\epsilon>0.
\tag{37}
$$
乘以 $\pi/2$ 得到 (7) 的第一式，再除以已证的 $Y>0$，得到 $X/Y>8/3$。这没有假设当前高模已知，也没有把初始七模轴比迁给当前点。

## 8. 用三次下界证明轴差超过 $21/25$

轴差已经可以用较短的 (22)–(28) 支付。由 (20) 的较宽上界 $13/40$，
$$
\begin{aligned}
\mathbb E_\mu\sqrt{1-z}-\mathbb E_\mu\sqrt z
&>
\frac{3537}{4096}-\frac{13}{40}
-\frac{435}{512}\epsilon\\
&=\frac{11029}{20480}-\frac{435}{512}\epsilon>0.
\end{aligned}
\tag{38}
$$
这里 $11029/20480>1/2$ 且 $435/512<1$，所以最后的正性不依赖数值估计。

为给出完全有理的尺度余量，消费 [R712](R712-full-positive-radius-central-second-derivative-comparison.md) 式 (12) 的准确恒等式
$$
\frac{22}{7}-\pi=
I:=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx.
\tag{39}
$$
在 $0<x<1$ 上分母大于1，因此
$$
0<I<\int_0^1x^4(1-x)^4\,dx
=\frac15-\frac46+\frac67-\frac48+\frac19
=\frac1{630}.
$$
故
$$
\pi>\frac{22}{7}-\frac1{630}
=\frac{1979}{630}
>\frac{157}{50},
\tag{40}
$$
其中最后两个有理数的差准确为 $2/1575$。本文只在已有积分恒等式上取明确上界，没有重新计算 $\pi$ 或执行积分。

现在 (11)、(38)、(40) 给
$$
\begin{aligned}
X-Y
&>
\frac{157}{100}
\left(\frac{11029}{20480}-\frac{435}{512}\epsilon\right)\\
&=\frac{1731553}{2048000}
-\frac{13659}{10240}\epsilon\\
&=\frac{21}{25}
+\frac{11233}{2048000}
-\frac{13659}{10240}\epsilon.
\end{aligned}
\tag{41}
$$
而
$$
\frac{11233}{2048000}>\frac1{1000},\qquad
\frac{13659}{10240}\epsilon<2\epsilon<\frac1{10^6},
$$
所以余量严格为正。这证明 (8)，并显式保留全部舍入费用。

## 9. 对当前自由量和实际证据的准确适用范围

1. **任意有限当前 M。** 证明包括 $M=160$、$M=320$ 及任意 $M\ge3$；不需要知道高模的逐词值，不降低自由量，也不新增系数截断。三个矩固定是正交性结论，第四矩的控制来自完整正密度。
2. **准确 RN 参数。** 正式数学系数是 (3) 的准确 dyadic。理想有理值 $-3/40$、$3/112$ 只用于精确比较；(16)、(28)、(29)–(35)、(41) 保留了它们与实际 dyadic 的差。
3. **连续条件尚须同场支付。** 即使旧有限域角网取值全正，也不能从该采样推出 (2)。本定理不声称任何尚未返回的当前点已经满足它。新 N4096 或 J1845 的工作观察层精化同样不自动给出连续正性。
4. **仅核心几何。** $X-Y$ 是两半轴差，不是旋转核心点到整张闭面图像的距离。活动上片、下反射、两平帽和全部固定标记都可能影响完整目标距离。本文没有给出新的 $\sigma$、$D$、reach、握持区比例、metric error 或 $\delta_E$。
5. **已有整像论证可在自身前提下消费。** 如将 $8/3$ 用作 [R718](R718-positive-definite-flow-distance-and-whole-image-held-witness.md) 所需的核心轴比下界，仍须真实同点支付其完整闭面、共同中心/矩阵/支持、端口和相位成员关系。本文没有实例化那套全域证据，也没有产生实际场证书。
6. **不改变科学入口。** 所有原三路 SO3 变量、径向与角向域、32个 normal stages、完整历史和预算保留。没有新 fixture、采样前门或另一个数值验收条件。本文只加强已登记条件性解析结论。

## 10. 来源与新增内容

准确对象、固定前三 RN 值、全当前连续正性和轴积分语义来自 R717/R719。本文直接核读的 R719 全文为9212 B，SHA256
`f043c75457173c9cfa5bbf7b0b9710049edfcb075d31d474231554285768cff7`；
其已刊路径为
`results/R719-fixed-first-three-fejer-modes-preserve-current-axis-gap.md`。
R712 式 (12) 的完整核读源为9441 B，SHA256
`187910c7baec14d8ed36d2f9f8213fe87ffbf762afa30acb365a93287f4b496b`。

R719 的高模逐系数尾和给 $7/3$ 与 $4/5$。本文新增的是：完整概率测度的前三矩、分解后的两项 Cauchy 小轴界、加权 Cauchy 第四矩控制、全 $[0,1]$ 多项式下界，以及显式带 RN 误差的 (7)–(8)。没有重证已有闭面或局部隐函数定理，没有把有限 positive-semidefinite 观测冒成实际连续几何。

以上全部是纸面有理运算、准确不等式和已有证明的明确应用。未运行科学、CAS、数值脚本或任何本地数学样例；文件构造与哈希保护只处理本文文字。
