# R133：新互逆主体负前缀的真实全频双向 Cauchy 预算

**已证明（同一实际新度量、完整 Fourier 线性 Cauchy/source 算子）。**
对已保存的两个实际互逆候选，在整个连续 $0\le r\le1/5$ 上，
其**完整无限维线性化**具有以下双向 Cauchy 增益：

| 中心 | 向外的能量范数增益 | 向内的能量范数增益 |
|---|---:|---:|
| alpha=.70，M128 | $<58.424668$ | $<95.679611$ |
| alpha=.75，M256 accepted000 | $<1493.577736$ | $<2408.100850$ |

系数中心虽是有限 Fourier 多项式，变分和源在本定理中并不截断，全部 mean
也保留。完整实际 PPoly 接缝均已支付。第二个中心尚无最终有限 BVP 收敛结论；
这不妨碍在它处定义并严格控制完整线性 Cauchy 系统，但本篇不因此授予主体
PDE 解或混合型边值逆。

## 1. 实际对象及能量空间

令固定中心 $u=\alpha U$、$v=s+\alpha V$，其中 $s=1/C_{\rm ref}$ 来自真实
新目标 $E_\nu=E e^{\nu h}$。其完整线性化见
[准确曲率角系统](R133-supplement-exact-curvature-angle-principal-system.md) 的 (H.7)–(H.9)。
本次使用原全 $|\eta|\le10^{-9}$，每个中心的固定实际参数分别为

$$
\begin{array}{c|c|c}
&\alpha&\nu\\\hline
.70&3152519739159347/4503599627370496&-8203900476603349/288230376151711744\\
.75&3/4&-2443457753738987/72057594037927936.
\end{array}
\tag{E.1}
$$

目标 primitive 的全部无限尾继承自原493盒证书，再通过完整的紧支度量公式
支付新 $\nu$；没有把旧原目标在扰动支撑内直接转授。每个允许的 $\eta$ 都给
相应真实 $s$，固定有限 $U,V$ 则不变。本篇的常数对整个这个 $\eta$ 区间统一。

所有实际盒均验证 $v<0$，故 $C=1/v<0$、$D=\langle C\rangle<0$。
对完整变分 $h=(\xi,\zeta)$ 定义归一化能量范数

$$
\mathfrak N_r(h)^2=
\frac1{2\pi}\int_0^{2\pi}\frac CD
 \bigl(|\xi|^2-K|\zeta|^2\bigr)d\theta.
\tag{E.2}
$$

在真曲率角 $d\phi=(C/D)d\theta$ 中，这就是 (H.10) 除以 $2\pi$ 的平方根。
完整类型证书给 $K<0$；本次直接区间计算也逐盒重新检查这个严格门。

## 2. 不依赖中心已解 PDE 的精确能量对角

为实际消费 (H.11)，令

$$t=\frac{v_r}{v},\qquad
\overline t_C=\frac{\langle Ct\rangle}{D}.$$

因为 $C/D>0$ 且平均为1，$\overline t_C$ 是 $t$ 的真实正权平均。
从 $d=\gamma B/D-\phi_r$ 直接微分，不使用 Codazzi 方程，可得

$$
d_\phi=\gamma\left(u_\theta-\frac{uv_\theta}{v}\right)
 +t-\overline t_C.
\tag{E.3}
$$

例如 $C_r/C=-v_r/v=-t$，且 $D_r/D=-\overline t_C$，所以 (E.3) 直接等于
(H.4) 中保有完整 $R_C$ 的公式。它没有删除近似中心残差。

先在能量对角中作代数相消，而不是分别估计大项，得到

$$
\begin{aligned}
G_1={}&\frac\gamma2
 \left(u_\theta+\frac{uv_\theta}{v}\right)
 -\beta(1+3u^2+Kv^2)+\frac{\overline t_C-t}{2},\\
G_2={}&\frac\gamma2
 \left(-3u_\theta+\frac{uv_\theta}{v}\right)
 +\beta(1-u^2-3Kv^2)+\frac{K'}{2K}
 +\frac{\overline t_C-t}{2}.
\end{aligned}
\tag{E.4}
$$

因此对每个光滑径向片，完整源 $f$ 满足

$$
\frac d{dr}\mathfrak N_r(h)
\le \max\{G_1,G_2\}_{\theta}\,\mathfrak N_r(h)
 +\mathfrak N_r(f).
\tag{E.5}
$$

反向则由 $\max\{-G_1,-G_2\}_{\theta}$ 控制。实际程序分别保留两方向费率，
并只为方便任意子区间的源估计而将其与0取最大。$K'/(2K)$ 的真实符号和
整个区间均保留，没有擅自丢掉不利项。

## 3. 每个完整径向盒的严格支付

令原 target 闭盒、候选 PPoly 节点、紧支接缝 $1/20,9/50$ 取共同精确有理
细分。在每一盒内，每个保存的 IEEE 多项式系数都作为准确 dyadic 值，以
320 bit Arb 区间 Horner 计算整个径向范围及径向导数。

实 sine/cosine 幅度的绝对和准确等于对应复 Fourier 全正负模的 $A_0$ 预算。
因此从全部 $M$ 个候选模得到

$$
|u|\le U_0,\quad |u_\theta|\le U_1,\quad
|v_\theta|\le V_1,\qquad -M_v\le v\le-g_v<0.
\tag{E.6}
$$

每一角点都被这些界覆盖，而非只角网格。若 $t=v_r/v\in[t_-,t_+]$，由真实
正权平均立即有

$$
\left|\frac{\overline t_C-t}{2}\right|
\le\frac{t_+-t_-}{2},\qquad
\left|\frac{uv_\theta}{v}\right|\le U_0V_1/g_v.
\tag{E.7}
$$

程序将这些完整区间直接放入 (E.4)。$u^2$ 使用 $[0,U_0^2]$，$v^2$ 使用
$[g_v^2,M_v^2]$。于是得到每一连续闭盒上的真实区间 $\mathcal G_1,\mathcal G_2$，
定义

$$
g_f=\max(0,\mathcal G_1^+,\mathcal G_2^+),\qquad
g_b=\max(0,-\mathcal G_1^-,-\mathcal G_2^-).
\tag{E.8}
$$

乘以该盒精确长度再相加，就给整个区间的前后向 logarithmic norm 积分。
这没有投影变分 $h$：有限模只用于描述系数中心，(E.5) 对完整角函数成立。

真实目标系数的支付也明确。令

$$N=K_0+\nu\beta h'/(2E),\qquad K_\nu=e^{-\nu h}N,$$

则

$$
N'=K_0'+\frac{\nu(\beta'h'+\beta h'')}{2E}
-\frac{\nu\beta h'E'}{2E^2},\qquad
K_\nu'=e^{-\nu h}(N'-\nu h'N),
$$
$$\beta'=a''/a-\beta^2.
\tag{E.9}$$

所有右侧量来自同一原闭盒；$h,h',h''$ 来自准确紧支多项式。
整个新旋转图也逐盒验证

$$E_\nu-a'^2>0,
\quad s=-a\sqrt{E_\nu/(E_\nu-a'^2)},
\quad s_r=\beta s(1-K_\nu s^2).
\tag{E.10}$$

最后 $v_r=s_r+\alpha V_r$。所以 $t$、$K'/K$ 和能量系数使用同一真实
新目标，未混用有限 primitive 或不同 $\nu$。

## 4. 每个准确 PPoly 接缝

在一个真实候选接口上，$s$ 连续，但保存的 $V$ 两片未必准确相接。
以 Fraction 计算所有原三次端点，得准确
$\Delta v=\alpha\Delta V$，保留其 mean 和全部非零模。若两侧全角负距至少
为 $g>0$，令

$$\epsilon=\|\Delta v\|_{A_0}/g<1.$$

那么 $C_+/C_-=v_-/v_+$ 距1至多 $\epsilon$。对其以 $C_-/D_-$ 作正权
平均可得 $D_+/D_-$ 同样在 $[1-\epsilon,1+\epsilon]$ 中。因此

$$
\frac{(C_+/D_+)}{(C_-/D_-)}
\le\frac{1+\epsilon}{1-\epsilon}.
\tag{E.11}
$$

$K$ 在真实目标接口连续，原物理角下连续的 $h$ 因此满足

$$
\mathfrak N_+(h)\le
\sqrt{\frac{1+\epsilon}{1-\epsilon}}\,\mathfrak N_-(h).
\tag{E.12}
$$

反方向同样成立。每个接口的平方根能量 log 费就是
$\frac12\log[(1+\epsilon)/(1-\epsilon)]$。这正支付 (H.16) 的真实角图接合，
没有把微小 dyadic 接缝删去。若修正另有实际仿射跳 $j$，应在 (E.12) 右侧
再加 $\mathfrak N_+(j)$；本次齐次 Cauchy 增益不免费消去这样的真实输入。

## 5. 完整 Cauchy 与 ordinary source 结论

对区间任意两点，令 $M_f,M_b$ 分别为 (E.8) 盒积分和全部 (E.12) log 费
相加后的指数。完整线性系统在每个光滑片可以按两条真实特征流写成 Volterra
积分方程：因 $K$ 严格负且与0分离，径向对角化矩阵可逆，角输运流的 Jacobian
有界，所有零阶系数有界。对短径向时间，积分式在完整 $C_rL^2_\theta$ 中
是收缩；有限拼接和 (E.12) 给整个区间唯一解。对平滑数据先证明 (E.5)，
再以能量界完备化，得到全部 $L^2$ 初值与 $L^1_rL^2_\theta$ 源的结论。
该构造并不限制初值 Fourier 支撑，零模也没有投影出去。

特别地，向外对全部 $0\le r_0\le r\le1/5$，

$$
\mathfrak N_r(h)\le M_f\left[
\mathfrak N_{r_0}(h_0)+\int_{r_0}^r\mathfrak N_t(f)\,dt
+\sum_{r_0<r_i\le r}\mathfrak N_{r_i+}(j_i)\right].
\tag{E.13}
$$

向内对应式使用 $M_b$ 和反向接口的源范数。参数列、普通 residual 和两个
mean 都可以作为这里的完整输入，不把源限于某个特殊保留通道。

若需要从物理 Fourier $A_0$ 源界消费，(E.6) 给 $C/D\le M_v/g_v$，所以

$$
\mathfrak N_r(f)\le
\sqrt{M_v/g_v}\,
\sqrt{\|f_1\|_{A_0}^2+(-K)^+\|f_2\|_{A_0}^2}.
\tag{E.14}
$$

对固定 $\nu$ 的归一互逆残差，实际源恰为
$-\alpha(R_U,R_V)$；(E.14) 不额外乘原物理 $1/v^2$ 的高度转换因子。
实际非线性余项、参数源或中心跳仍须各自计算，不能据 (E.13) 宣称后验收缩已过。

## 6. 本次实际完整结果

新原生源为 `scripts/fourfold_codazzi_curvature_angle_energy_prefix.py`。它实际
消费原493盒完整 target 与全部保存候选，结果为

| 量 | alpha=.70、M128 | alpha=.75、M256 accepted000 |
|---|---:|---:|
| 全共同连续闭盒数 | 844 | 1192 |
| 全准确内部 PPoly 接缝数 | 359 | 751 |
| 全角、全径向 $|v|$ 下界 | $>.1927902384381$ | $>.1145864894566$ |
| 向外 log 积分 | $<4.067738192$ | $<7.308929686$ |
| 向内 log 积分 | $<4.561005217$ | $<7.786593687$ |
| 全接口 log 费 | $<7.056\cdot10^{-17}$ | $<1.094\cdot10^{-16}$ |

全部严格负号、真实新旋转图、邻接、完整模式和接口门均实际通过；原生运算
分别约6.84秒、20.58秒。全部有向球、共同盒/原 target 索引、候选片索引和
准确跳费保存在

- `notes/2026-11-13-R133-curvature-angle-energy-alpha070-r02-native.json.gz`；
- `notes/2026-11-13-R133-curvature-angle-energy-alpha075-r02-native.json.gz`。

后一候选的输入及可再生的完整 accepted000 检查点，沿用
[原137过程和无损恢复记录](../notes/2026-11-13-R133-reciprocal-m256-exit137-and-complete-resume.md)，
没有重复提交大中间数据，也没有把未收敛状态改成最终成功。

这些常数属于新的实际 $\nu$ 主体中心，不是从旧 type-fixed 对象转授。
本篇到 $r=1/5$ 为止；完整唯一 turning 根在 $(.238,.239)$。剩余负段、真实
转向、正帽两迹及高频返回小除数必须继续连接，不能把全频 Cauchy 界直接称为
完整边值逆或闭面存在。
