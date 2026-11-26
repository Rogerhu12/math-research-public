# R227：新 gap 前缀前 15 个实际 Hermite 单元的全域原生 Gram 证书

会话：Astra-visible-flex-6a65；日期：2026-11-26。

## 结论及其范围

本条对 `2026-11-26-6a65-geometry-coupled-gap-prefix.md` 已登记的新 gap $1.05$、$v=.045$ 前缀，证明**实际消费的有限位置场**在前 15 个径向 Hermite 单元的全部连续 $(s,\theta)$ 上近等距且浸入。使用全部保存的 Fourier 系数；没有将角网格最大值当作连续最大值，没有重新跑 Cauchy ODE，也没有删去高频数值尾。

设 $Y$ 为下文准确说明的原生角位置场，$g_*$ 为对应的旋转型目标度量。则在该完整圆环片上

$$
\left\|g_*^{-1/2}\bigl((DY)^TDY-g_*\bigr)g_*^{-1/2}\right\|_{\rm op}
\le
\frac{10894072968664110995085}{79228162514264337593543950336}
<1.38\times10^{-7}.
$$

因此它处处浸入。原生坐标的面积密度满足

$$
|Y_s\times Y_\theta|>.40322802.
$$

最坏证书单元为零起始编号 $9$，其物理位置约为 $s\in[.1353125,.1390625]$。这是该单元上的保守连续上界，不声称真实极值出现在某个观测角或观测点。

本条**不包含**第 16 个用准确形式 coast 端口修复的非多项式单元，也不包含 `WarmMaster.normalized` 的缩放、角重参数链、曲率界、Cauchy ODE 余项、全局单射或全时 reach。故不能据此宣布整个 ramp、全闭曲面或准确等距族完成。

## 1. 冻结的实际位置对象

实际 master 是 `gap105-v045-prefix01-ramp-master.npz`，SHA256 为

```
0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7
```

其 `coefficients` 形状为 $(17,768,3,3)$，最后两轴依次是位置、径向速度、径向加速度与 Cartesian 分量。保存波数为

$$
0,1,\ldots,383,-384,-383,\ldots,-1.
$$

全部 768 个波数都有非零保存系数。文件的 `modes=191` 只标识原有限 Cauchy 流中 $n,m$ 的截断，不是这些位置数据的截断。尤其 Nyquist 波数 $-384$ 不能默默删除。

每个 binary64 实部、虚部均视作其准确 dyadic 有理数。对保存的复系数 $c_k$，定义实函数

$$
\operatorname{Re}\sum_k c_ke^{ik\theta}
=\sum_{k=-384}^{384}d_ke^{ik\theta},\qquad
d_k=\tfrac12(c_k+\overline{c_{-k}}),
$$

缺少的 $c_{384}$ 取零，$d_0=\operatorname{Re}c_0$。配对以有理数完成，没有把不完全共轭的原系数先浮点强制对称。因此上述准确实函数正是消费者的 `real` Fourier 定义。

中央半轴是文件中的准确 dyadic 数，数值分别约为

$$
A=1.4532280772048913,\qquad B=.4032280772048914.
$$

本条先证明这个冻结有限对象，不把它与定义中央种子的非 dyadic 唯一根之间的小差自动消掉。设 $a_\ell=P(A,B)/(2\pi)$ 为该准确椭圆的周长半径。脚本复用已登记的正项周长级数，以有理上下界包含 $a_\ell$，并将有限消费者保存的 `a0` 也纳入目标参数区间。

记 $c=13/128$，$x=s-c$。节点 $x_j$ 是保存的 17 个准确 dyadic 值。单元长度

$$
L_j=x_{j+1}-x_j
$$

也使用准确差；脚本逐单元核验这个差与消费者的 binary64 减法一致。对 $j=0,\ldots,14$，两端 $P,V,A_{ss}$ 由同一保存端迹给出；唯一的左端覆盖是 `WarmMaster.ramp_port(0,u)` 实际采用的准确椭圆柱：

$$
P_0=(A\cos\theta,B\sin\theta,c),\quad V_0=(0,0,1),\quad A_{ss,0}=0.
$$

内部场就是消费者已经采用的物理五次 Hermite 插值。若 $t=(x-x_j)/L_j$，则位置系数由

$$
P_j,\ L_jV_j,\ L_j^2A_{ss,j},\
P_{j+1},\ L_jV_{j+1},\ L_j^2A_{ss,j+1}
$$

及同一六个 Hermite 基函数组成。位置在 $t$ 中次数为 $5$，在 $\theta$ 中准确实 Fourier 次数为 $384$。相邻多项式单元共享完整 $P,V,A_{ss}$ 函数，故它们形成 $C^2$ 周期位置片。

第 16 个单元不在这个多项式类中：它的右端被 `coast_port(0,u)` 替换，而该端口包含新 $\Gamma_{95}$ 的准确弧长角逆。那是另一个必须支付的完整端迹问题。

## 2. 原生角度量不能写错

`WarmMaster` 通过中央椭圆的弧长角 $u$ 消费保存的原生角 $\theta$。两者的关系是

$$
\frac{du}{d\theta}=\frac{\ell(\theta)}{a_\ell},\qquad
\ell(\theta)^2=A^2\sin^2\theta+B^2\cos^2\theta.
$$

因此目标在原生坐标下是

$$
g_*=ds^2+b(s,\theta)^2d\theta^2,\qquad
b(s,\theta)=\frac{f(s)}{a_\ell}\ell(\theta),
$$

而不是 $ds^2+f(s)^2d\theta^2$。其中当前有限消费者的 $r=.06$、$v=.045$ 均按保存的准确 dyadic 参数解释，

$$
\frac{f(s)}{a_\ell}=1+\frac{vr}{a_\ell}J(x/r),
$$

$$
J(z)=21z^6-60z^7+\frac{135}{2}z^8-35z^9+7z^{10}.
$$

级数给出的 $a_\ell$ 区间以及有限 `a0` 都被包含，所以本结论也覆盖以该有限标量写出的同一目标公式。它没有认证数值弧长逆的每次浮点执行误差。

令

$$
E=|Y_s|^2,\qquad F=Y_s\cdot Y_\theta,\qquad G=|Y_\theta|^2.
$$

由于 $v>0$ 且 $J\ge0$，整个证明域内 $b\ge B>0$。因此分别控制 $E-1,F,G-b^2$ 即可控制目标度量下的完整 Gram 误差。

## 3. 精确卷积与 Bernstein 包含

### 3.1 低频部分

实际执行固定低频 cutoff 为 $95$。这只是精确卷积与余项计算之间的分工，未改变场。对 $|k|\le95$ 的位置多项式，所有 $P,L_jV,L_j^2A_{ss}$ 系数都有共同 $2$ 幂分母。物理 $s$ 导数中的 $L_j^{-1}$、$L_j^{-2}$ 留作外置准确有理因子。

脚本计算如下真正的多项式系数卷积：

$$
|Y_t^{\rm low}|^2-L_j^2,\qquad
Y_t^{\rm low}\cdot Y_\theta^{\rm low},\qquad
|Y_\theta^{\rm low}|^2-b^2.
$$

前两项之后分别除以 $L_j^2,L_j$。使用大整数 Kronecker packing，保留 signed real/imaginary 两个通道。每位宽度根据全部 Cartesian 分量、径向乘积及角卷积项的绝对最大可能总和选择，最终每个有符号卷积系数均严格小于半个 radix；故逐位 balanced 解码准确恢复该整数卷积。没有浮点 FFT 卷积误差。另有包含负实部与负虚部的独立短卷积 fixture，与逐项整数双循环比较相等。

对任意径向次数 $d$ 的 Fourier 系数多项式

$$
Q(t,\theta)=\sum_k\sum_{j=0}^d a_{j,k}t^je^{ik\theta},
$$

转换为 Bernstein 形式。其第 $i$ 个控制系数为

$$
\beta_{i,k}=\sum_{j\le i}a_{j,k}
\frac{\binom{i}{j}}{\binom{d}{j}}.
$$

这些都是准确有理数。利用 Bernstein 基非负且总和为 $1$，对整个连续 $t\in[0,1]$ 与整个角圆周都有

$$
|Q(t,\theta)|\le
\max_i\sum_k\bigl(|\operatorname{Re}\beta_{i,k}|
 +|\operatorname{Im}\beta_{i,k}|\bigr).
$$

对目标 $f/a_\ell$ 的局部次数 $10$ 多项式，每个系数先准确有理计算，再包含于声明的 $2^{-200}$ dyadic 近似及准确误差。周长参数区间带来的偏差也单列。平方目标的 $0,1,2$ 阶物理导数误差经 Leibniz 公式支付，不以近似系数替代目标本身。

### 3.2 全部高频余项

记 $T$ 为 $95<|k|\le384$ 的完整保存尾。对位置及其物理导数使用同一 Bernstein 方法，额外乘上实际 $k$、$L_j^{-1}$ 等权重，得到

$$
\delta_s\ge\|T_s\|,\qquad
\delta_\theta\ge\|T_\theta\|.
$$

若低频相应范数上界为 $M_s,M_\theta$，则遗漏于低频卷积的完整贡献被准确包含为

$$
\Delta_E\le2M_s\delta_s+\delta_s^2,
$$

$$
\Delta_F\le M_s\delta_\theta+M_\theta\delta_s+\delta_s\delta_\theta,
$$

$$
\Delta_G\le2M_\theta\delta_\theta+\delta_\theta^2.
$$

$G$ 的一、二阶物理导数也按完整 Leibniz 和式包含。由此得到对所有 768 个保存系数的证明，而不是对截断场的证明。

### 3.3 完整相对 Gram 与浸入

设上述全系数界为 $\varepsilon_E,\varepsilon_F,\varepsilon_G$。相对误差矩阵为

$$
M=\begin{pmatrix}
E-1&F/b\\ F/b&G/b^2-1
\end{pmatrix}.
$$

对称矩阵的算子范数不超过绝对行和最大值，所以

$$
\|M\|_{\rm op}\le
\max\left(\varepsilon_E,\frac{\varepsilon_G}{B^2}\right)
+\frac{\varepsilon_F}{B}.
$$

逐单元计算该式，再取最大，即得开头的有理数。因为该值 $\delta<1$，相对 Gram 的两个特征值都不小于 $1-\delta$，故

$$
|Y_s\times Y_\theta|
=b\sqrt{\det(I+M)}\ge B(1-\delta)>.40322802.
$$

这是整个连续域的浸入结论；它没有排除不同位置点相交。

## 4. 本次实际有理回执

全 15 单元的执行自然 `exit 0`，外部耗时 $35.284689218$ 秒，峰值 RSS $39500$ KiB。脚本、完整报告及进程回执 SHA256 分别为

```
50b61f8b27d9446983c4119f292972615f1ee3d49cf6121feae4cae352922412
be77c270f9dcd4c2d146ba11e961c1535ea7c810f7d916d8554942e9d97c3642
33349e6babaabe3108edb7ec61474eb519b231608df26265850279bf6f912d7a
```

所有内部卷积、Bernstein 系数及误差预算均为整数或有理计算。报告中每个最终非负界向上取到 $2^{-96}$ 网格，并保留准确有理字符串；下表十进制采用稍宽的严格阈值。

| 全前 15 单元的量 | 严格上界 | 最坏证书单元 |
|---|---:|---:|
| $|E-1|$ | $1.366\times10^{-7}$ | $9$ |
| $|F|$ | $1.106\times10^{-9}$ | $11$ |
| $|F|/b$ | $2.743\times10^{-9}$ | $11$ |
| $|G-b^2|/b^2$ | $7.776\times10^{-10}$ | $0$ |
| 谱相对 Gram 误差 | $1.38\times10^{-7}$ | $9$ |
| 高频 $\|T_s\|$ | $6.686\times10^{-12}$ | $7$ |
| 高频 $\|T_\theta\|$ | $2.587\times10^{-12}$ | $14$ |
| 高频 $\|T_{s\theta}\|$ | $1.596\times10^{-9}$ | $9$ |
| 高频 $\|T_{ss\theta}\|$ | $1.702\times10^{-6}$ | $9$ |

另输出了后续归一化分析可消费的连续界：

$$
|G-b^2|<1.265\times10^{-10},\qquad
|\partial_s(G-b^2)|<1.348\times10^{-7},
$$

$$
|\partial_s^2(G-b^2)|<.0002534.
$$

后两项是完整物理导数，已包括高频权重与目标参数余项。它们还没有被代入 `WarmMaster.normalized` 的周长均值、缩放、角重参数和曲率链。

## 5. 复生与尚未支付的接合

复用已发表的新 prefix 实跑生成同一 master 后，在 Git 目录外执行：

```sh
python scripts/6a65-geometry-ramp-native-gram-certificate.py \
  --master "$actual_new_ramp_master" --scripts-dir scripts \
  --cutoff 95 --threshold 1/1000000 \
  --output "$fresh_outside_git_report"
```

脚本默认恰好验证 $j=0,\ldots,14$，输出独立 source SHA 并在结束时复核 master 未变。`--cell` 只用于明确的单元调试，不能生成 `allFirst15PolynomialCellsProved=true`。

下一未支付部分是第 16 单元完整准确 coast 端迹与原保存端迹的连续差，以及由这些差经 Hermite 物理导数放大后的实际场。R225 的周长缩放集合位移界不能直接替代该 $C^2$ 端口差。随后仍须支付已消费 normalized 场的完整 Gram 与曲率。以上缺口均保留，R227 不修改课题完成状态。
