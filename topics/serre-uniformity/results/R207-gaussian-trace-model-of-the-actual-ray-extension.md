# R207 — 同一实际射线扩张的显式 43 次 Gaussian trace 模型

**已证明并完成精确计算。** 本文固定 R171、R191 的 $p=43$ 和同一个
$776$ 位素数 $q$。我们构造其已标记循环扩张 $L_q/K$ 的一个
$43$ 次整模型；它在 $q$ 处是 Eisenstein 模型，且一致化元保留原来的
tame 生成元。完整系数通过严格根界与 $1325$ 个小素数的 CRT 唯一重建。
这尚未给出 R201 的 Norm 解，$\mathcal L$ 仍未计算。

## 1. 输入与同一个扩张

沿用 [R191](R191-cyclotomic-principalization-and-eta-ray-field.md)：
$K=\mathbf Q(i)$、$\zeta=\zeta_{43}$、
$\mathcal B=K(\zeta)$、$r=i(\zeta-\zeta^{-1})$，
以及
$$
 \sigma(r)=3r-r^3,\qquad \sigma(\zeta)=\zeta^3,\qquad
 h=g(r)(2-r)^{22}.
 \tag{207.1}
$$
$f(r)=0$ 是次数 $42$ 的整多项式；$g$、$q$ 和所有原始权重
$e_j\in[-21,21]\setminus\{0\}$ 均完整嵌入核验程序及证书。
$e_j\equiv3^{-j}\pmod{43}$。R191 已用整数行列式证明
$N_{\mathbf Q(r)/\mathbf Q}g=-q$，并固定唯一的 $q$ 根以及
$\zeta$ 与 R171 Weil 配对的识别；本结果不更换这些输入。

为了得到整 Gaussian trace，把权重换成唯一的正代表
$$
 E_j\in\{1,\ldots,42\},\qquad E_j\equiv e_j\pmod{43}.
$$
定义
$$
 c=\prod_{e_j<0}\sigma^j h,\qquad
 A=\prod_{j=0}^{41}(\sigma^jh)^{E_j}=a_qc^{43},\qquad
 d_j=\frac{E_{j-1}-3E_j}{43}\in\{0,-1,-2\},
 \qquad w=\prod_{j=0}^{41}(\sigma^jh)^{d_j}.
 \tag{207.2}
$$
下标模 $42$。于是
$$
 \sigma A=A^3w^{43}.
 \tag{207.3}
$$
若 $\alpha^{43}=a_q$ 是 R191 的实根，取
$\alpha_+=c\alpha$，则 $\alpha_+^{43}=A$。这是同一个域中的
显式换元；既没有改变扩张，也没有重新选择 Kummer 角色。
原来的提升正好满足
$$
 \widetilde\sigma(\alpha_+)=w\alpha_+^3,\qquad
 \widetilde\sigma^{42}=1,\qquad
 \kappa(\alpha_+)=\zeta\alpha_+.
 \tag{207.4}
$$
阶数 $42$ 还可直接核查：其 $42$ 次方固定 $\mathcal B$，
在实根上只可能相差实的 $43$ 次单位根，故等于恒等。
$\widetilde\sigma$ 与 $\kappa$ 交换；复共轭 $\tau$ 固定
$\alpha_+,r$ 并反演 $\kappa$。
因此
$$
 L_q=\mathcal B(\alpha_+)^{\langle\widetilde\sigma\rangle}
$$
就是 R191 的循环 $43$ 次 $K$ 扩张。

## 2. 整生成元及精确的 tame 方向

置
$$
 \theta=\sum_{j=0}^{41}\widetilde\sigma^j\alpha_+.
 \tag{207.5}
$$
$A$ 为整元，因此每个被加数均为整元。
$\theta$ 被 $\widetilde\sigma$ 和 $\tau$ 固定，故
$\theta\in L_q^+=L_q^{\langle\tau\rangle}$，且整。

在 R191 选定的 $\mathcal B$ 的 $q$ 素点，$h$ 的赋值恰为 $1$，
其余 $41$ 个 $\sigma^jh$ 都是单位。
以基域赋值 $v(q)=1$ 归一，则
$$
 \left\{v\!\left(\widetilde\sigma^j\alpha_+\right):0\le j<42\right\}
   =\left\{\frac1{43},\ldots,\frac{42}{43}\right\}.
 \tag{207.6}
$$
唯一最小项是 $j=0$ 的 $\alpha_+$。所以
$$
 v(\theta)=\frac1{43},\qquad
 \frac{\kappa(\theta)}{\theta}\equiv\zeta\pmod{\mathfrak Q}.
 \tag{207.7}
$$
这不仅识别了域，还保留 R191 的 $\kappa$ 及 R168 的 tame 取向。
$\theta$ 不是有理数，而 $[L_q^+:\mathbf Q]=43$，故
$\mathbf Q(\theta)=L_q^+$。
其首一最小多项式 $P_\theta(T)\in\mathbf Z[T]$ 次数恰为 $43$。

$q$ 在 $L_q^+/\mathbf Q$ 中全分歧；全部 $43$ 个共轭的赋值均为
$1/43$。基本对称式给
$$
 q\mid [T^{43-k}]P_\theta\quad(1\le k\le43),\qquad
 q^2\nmid P_\theta(0).
 \tag{207.8}
$$
下述整数 CRT 输出独立满足全部这些整除式。
Eisenstein 判据因此也是实际输出的不可约证书。
在 $p$ 处，R191 的指定根改为 $c\,b_0$；此处没有重新选定
$p$ 局部 Kummer 规范。

## 3. 严格复数根界

$f$ 满足精确恒等式
$$
 X^{42}f(X+X^{-1})
   =\Phi_{172}(X)=\sum_{j=0}^{42}(-1)^jX^{2j}.
 \tag{207.9}
$$
核验器按整数二项式系数重新验证此式。
所以其 $42$ 个实根是
$2\cos(2\pi k/172)$，其中 $k$ 取 primitive $172$ 次单位根模反号
的代表。沿 (207.1)，角下标递推
$$
 k_0=1,\qquad k_{j+1}=3k_j+86\pmod{172}.
 \tag{207.10}
$$

证书保存每个根的 dyadic 区间
$[n_j/2^{220},(n_j+1)/2^{220}]$。
程序以精确整数运算核查两个端点上的 $f$ 异号、$42$ 个区间互不相交，
并核查区间次序与 $\cos$ 的严格单调次序一致。
结合 (207.9)，这唯一确定了所有区间与角下标的对应；
浮点余弦只用于提出初始区间，不参与证书的正确性依据。

在每个区间上，对 $g(r)(2-r)^{22}$ 做有理区间 Horner 运算，
得到 $|h_j|\le2^{u_j}$。全部 $u_j$ 为
$$
\begin{split}
(&-176,64,-50,53,61,-22,38,30,9,-38,52,61,37,24,-66,59,58,61,\\
 &51,57,54,62,-122,60,18,-87,58,39,48,52,59,24,-29,44,54,61,1,3,-11,31,-4,19).
\end{split}
 \tag{207.11}
$$
置
$$
 a_l=\left\lceil\frac{\sum_j E_j u_{l+j}}{43}\right\rceil,
 \qquad R=\sum_{l=0}^{41}2^{a_l},\qquad B=(R+1)^{43}.
 \tag{207.12}
$$
实际 $160\le a_l\le638$。
每个 $\theta$ 共轭的绝对值不超过 $R$；基本对称式因而把
$P_\theta$ 的每个系数绝对值控制在 $B$ 内。
$R$ 为 $639$ bit 整数，$B$ 为 $27435$ bit 整数。
这些是向上取整的有理界，不是数值拟合或经验系数界。

## 4. 模小素数的完整算法

取 $\ell\equiv1\pmod{172}$，$\ell\ne q$。
在 $\mathbf F_\ell$ 选 primitive $172$ 次根 $\xi$，
取 $r_0=\xi+\xi^{-1}$，沿 (207.1) 得 $r_l$。
逐项计算
$$
 h_l=g(r_l)(2-r_l)^{22},\quad
 A_l=\prod_jh_{l+j}^{E_j},\quad w_l=\prod_jh_{l+j}^{d_j}.
 \tag{207.13}
$$
程序核查 $42$ 个 $r_l$ 互异、$f(r_l)=0$、所有 $h_l\ne0$，
以及 $A_{l+1}=A_l^3w_l^{43}$。

在 $\mathbf F_\ell[X]/(X^{43}-A_0)$ 中，递推
$$
 k_0=1,\quad c_{0,l}=1,\qquad
 k_{j+1}\equiv3k_j\pmod{43},\qquad
 c_{j+1,l}
 =c_{j,l+1}\,w_l^{k_j}A_l^{\lfloor3k_j/43\rfloor}.
 \tag{207.14}
$$
它准确表示
$\widetilde\sigma^j\alpha_+=c_{j,0}\alpha_+^{k_j}$。
$k_j$ 遍历 $1,\ldots,42$，程序还核查第 $42$ 次恰回
$k_{42}=1,c_{42,l}=1$。
于是 $\theta$ 是这个代数中确定的次数至多 $42$ 元素。

该 $43$ 维可分代数的迹满足
$$
 \operatorname{Tr}(\theta^m)
  =43\,[X^0]\bigl(\theta^m\bmod(X^{43}-A_0)\bigr).
 \tag{207.15}
$$
对 $m=1,\ldots,43$ 逐次相乘并用 Newton 恒等式，得到
$P_\theta\bmod\ell$ 的全部 $44$ 个系数。
这并不要求 $X^{43}-A_0$ 在 $\mathbf F_\ell$ 上不可约。
改变 $\alpha_+$ 的根只排列共轭，改变 $\xi$ 只改变计算嵌入，
所以输出仍是同一个有理最小多项式的约减。

## 5. 已完成的 CRT 与独立复算

完整证书保存每个素数及其全部剩余系数，系数统一按降幂排列。

| 项目 | 实际值 |
|---|---:|
| CRT 素数个数 | $1325$ |
| 最小、最大 CRT 素数 | $1000697,\ 2572433$ |
| CRT 模数 $M$ 的 bit 长度 | $27448$ |
| $2B$ 的 bit 长度 | $27436$ |
| 输出最大系数的 bit 长度 | $26948$ |
| 未参与重建的验证素数 | $3000541,\ 3001057,\ 3002089$ |

每个小素数另由试除至平方根验证素性。
程序重新计算所有模素数多项式，逐行核对、完成 CRT，
并以严格不等式 $M>2B$ 唯一恢复每个居中整数系数。
这一步已完整封口，不是“若再收集足够素数”的检查点。

原始 C++ 实现与标准库 JavaScript 实现还独立核对了首两行。
例如 $\ell=1000697$ 的开头为
$$
 (1,0,211881,685851,264133,980135,608435,947772,\ldots),
$$
末四项为 $(521654,986039,637210,407311)$。
最终标准库核验器不依赖 C++、PARI、Sage 或类群计算。

文件：

- [verify_r207_gaussian_trace_degree43.js](../scripts/verify_r207_gaussian_trace_degree43.js)
- [r207_gaussian_trace_degree43_certificate.json](../notes/r207_gaussian_trace_degree43_certificate.json)

~~~sh
node scripts/verify_r207_gaussian_trace_degree43.js --check notes/r207_gaussian_trace_degree43_certificate.json
~~~

证书以紧凑 JSON 保存完整整数及全部 $1325$ 行；没有只保存哈希来
代替可复验数据。输入 $q$ 的素性、$g$ 的范数和原始射线识别仍引用
R171/R191 已完成的证书，本程序没有重新运行大素数 ECPP。

## 6. 对真正 Norm 方程的作用及其边界

令 $F=K(z)$ 为
[44 次普通目标笔记](../notes/2026-11-13-small-robert-norm-target.md)
中的同一个域。
$[F:K]=44$ 与 $[L_q:K]=43$ 互素，故
$$
 FL_q=F(\theta),\qquad [F(\theta):F]=43.
 \tag{207.16}
$$
这里不假设 $F$ 与 $\mathcal B$ 线性不交；
事实上它们有一个二次交域。这不影响 (207.16)。

任意元素唯一写成
$$
 X=\sum_{j=0}^{42}x_j\theta^j,\qquad x_j\in F.
$$
其普通 Norm 方程就是
$$
 \operatorname{Res}_T
 \left(P_\theta(T),\sum_{j=0}^{42}x_jT^j\right)=U
 \tag{207.17}
$$
（目标 $U$ 取 R201 的同一普通单位或其已校准的短形式）。
$q$ 处全分歧，而 $v(\theta)=1/43$；若 $N X=U$ 且 $U$ 是该处单位，
不同项的赋值具有不同的模 $\mathbf Z$ 分数部分。因此
所有 $x_j$ 在该处整，$x_0$ 是单位，且
$$
 \overline X=\overline{x_0}.
 \tag{207.18}
$$
计算规范 Norm primitive 的 $q$ 剩余值无需构造
$\mathbf F_{q^{43}}$，也无需在局部展开 $42$ 个高次项。

然而普通目标与普通 Norm 解不自动带有完整 $C_{44}$ 和 $\tau$ 等变性。
若 $X$ 尚未投影，仍须在 R201 指定的全部共轭素点读取
$\sigma(x_0)$，按原权重合成，并保留模 $p^2$ 根规范及
$S$ 外支撑的 Artin 修正。
单个未投影的常数项对数不能直接命名为 $\mathcal L$。

本结果完成了同一 $q$、同一射线角色、同一 tame 方向的实际
$43$ 次算术模型。尚未找到 (207.17) 的所需全局解；
R200/R201 的最终条件仍是
$$
 \Omega_2^\varepsilon=\varepsilon(10-\mathcal L),
$$
其中 $\mathcal L$ 尚待求值。
