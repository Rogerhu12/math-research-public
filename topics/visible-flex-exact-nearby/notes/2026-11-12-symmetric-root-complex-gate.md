# 同一实际 root collar 的局部复径向、复角分母门

状态：**已完成有向有限证书。** 只复化原 sym step02 的一个已付
共同多项式 span 内的 root collar；不复化整个分段样条核心，也不
向 D5 参数图转授。

## 1. 明确域与已付分母

实 collar 使用原 simple-root 证书的两个准确 binary64 端点

$$
I_c=[.23788166874999997,\ .23885823125000002].
$$

它位于共同 span $(.23750000000000002,.23969803864366687)$ 内，
包含真实 target 根 $t$。考虑

$$
\boxed{\quad \Re z\in I_c,\quad |\Im z|\le2^{-16},\qquad
\Re\vartheta\in\mathbb R,\quad |\Im\vartheta|\le2^{-11}.\quad}
$$

所有下列点积在复域中均指**双线性解析点积**，不是带复共轭的
Hermitian 平方。置

$$
X=\partial_zF,\quad W=T\times X,\quad
A^2=a^2W\cdot W,\quad H^2=F\cdot F,\quad J=aF\cdot W.
$$

下文用 $F_3$ 表示空间竖直坐标，对应 JSON 中的 `Fz` 字段；
$X$ 始终表示材料径向导数。

在上述整个复积域中，证书给出：

| 量 | 正实部下界 |
|---|---:|
| $-N_{\rm raw}$ | $>.2423214$ |
| $A^2$ | $>.7090238$ |
| $H^2$ | $>.6497501$ |
| $J$ | $>.6802363$ |
| 空间竖直坐标 $F_3$ | $>.2241776$ |
| $a$ | $>1.0969829$ |
| 实 target 的解析延拓 $E$ | $>1.5036384$ |
| 根函数导数 $C'$ | $>161.9603$ |

因此分别取右半平面上的主平方根 $\sqrt{A^2}$、$\sqrt{H^2}$，得到
真正解析、实域取正的归一化。特别

$$
\zeta=\frac J{\sqrt{A^2}\sqrt{H^2}}
$$

全域无零点，且 $|\zeta|>.40712$。这是复数模的界，未把它偷换成
$\Re\zeta>.40712$。

真实 $\kappa(z)=K_0(z)/(z-t)$ 在根处解析延拓，整个复径向矩形上

$$
32.13<|\kappa|<88.49.
$$

同一实际 ground-state 选择的解析延拓
$\ell=F_{3,\theta}/F_3-(F\cdot F_\theta)/(F\cdot F)$ 满足 $|\ell|<7$。
这些是已付的具体 tube；没有把实 collar 半径直接称作复 strip 宽度。

## 2. 真实无限图的复范数，不借用未付 FFT

输入仍是完整 snapshot SHA256
`bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532`。
物理相位先作准确偶奇平均，高度是 slope 的准确积分，未作 Gaussian
平滑。在当前共同 span 中，raw spline 和 base 都是五次多项式，
所以物理 $\beta$、$\gamma$ 的次数至多20、15；实际 $a$ 次数至多5，
实际 $Z$ 次数至多6。

程序通过完整有向 de Boor/Taylor 和二项式乘积生成这些**物理**
多项式的全部导数。对 $z=x+iy$ 用有限准确 Taylor 展开

$$
|\partial_x^r b_k(z)|\le
\sum_{j\ge0}\frac{|y|^j}{j!}
       \sup_{x\in I_c}|\partial_x^{r+j}b_k(x)|
$$

包住复径向系数；它不是把 C4 样条跨 knots 作解析延拓。再以
$(4k)^s\cosh(4k\,2^{-11})$ 权求和，支付真实有限相位的全部所用
混合复导数。cosh 中的 exp 沿用有理 Taylor 与有向平方核。

对 $e^f$ 的混合 Bell majorant 取 $B_{00}=1$，并使用

$$
B_{r,s}=\sum_{i=0}^{r-1}\sum_{j=0}^s
\binom{r-1}{i}\binom{s}{j}\,f_{i+1,j}B_{r-1-i,s-j}
\quad(r>0),
$$

其中 $r=0$ 行用普通一维 Bell 递推。水平分量可由
$2e^{\sigma_\theta+B_{00}^{\rm phase}+G_{00}^{\rm phase}}$
乘 $\beta+\gamma+\theta$ 的 Bell 界控制；竖直分量由
$e^{G_{00}^{\rm phase}}$ 乘 $\gamma$ 的 Bell 界控制。
在 $\theta$ 的一阶 jet 中准确加入常数1；没有漏掉旋转基导数。

关键地，对固定复径向值及固定 $\Im\vartheta$，沿 $\Re\vartheta$
的真实 $T$ 仍为零均值周期向量：水平分量用四重旋转，竖直分量用
准确角奇性及解析周期积分平移。因此零均值原函数的锯齿卷积核仍给

$$
\|P_\theta V\|\le\frac\pi2\|V\|<\frac{11}{7}\|V\|,
$$

对复向量 Banach 范数及所有径向 jet 同样成立。于是

$$
\|\partial_x^rF\|\le |Z^{(r)}|+
\frac{11}{7}\sum_{j=0}^r\binom rj|a^{(j)}|\,
                 \|\partial_x^{r-j}T\|.
$$

这里直接估计的是**完整无限 primitive**，不是有限 DFT 多项式。
所以本复预算没有额外未支付的 Fourier 截断或混叠。

还使用两个合法收紧：实球面单位向量映射的任意混合相位偏导范数
至多1，所以相同 Bell 多项式无指数前因子地给实 jet 界；已有实
连续证书另给 $\|F\|,\|F_x\|$。从实点先沿虚径向、再沿虚角走线段，
用上述**未收紧**复导数界乘路径长度，给出较好的复 $F$ 和 $T$ 界。
所有收紧使用独立已得的粗界，没有循环假设未知范数小。

## 3. 从实正下界到复无零点

记所用复范数界为 $M_F,M_X,M_{X_2},M_T,M_{T_x},M_{T_\theta},\ldots$。
对 $W=T\times X$ 有

$$
\begin{aligned}
|W_x|&\le M_{T_x}M_X+M_TM_{X_2},\\
|W_\theta|&\le M_{T_\theta}M_X+a_+M_TM_{T_x}.
\end{aligned}
$$

第二式准确使用 $X_\theta=a'T+aT_x$ 和 $T\times T=0$。
对 $N_{\rm raw}=-a^2X\cdot(T\times T_\theta)$，

$$
\begin{aligned}
|N_{{\rm raw},x}|\le{}&2a_+|a'|_+M_XM_TM_{T_\theta}\\
&+a_+^2(M_{X_2}M_TM_{T_\theta}
 +M_XM_{T_x}M_{T_\theta}+M_XM_TM_{T_{x\theta}}),\\
|N_{{\rm raw},\theta}|\le{}&
a_+^2M_T(a_+M_{T_x}M_{T_\theta}+M_XM_{T_{\theta\theta}}).
\end{aligned}
$$

对 $A^2,H^2,J,F_3$ 同样直接对双线性式求一阶导数；其中
$X\cdot(T\times X)=0$ 和 $T\cdot(T\times X)=0$ 的准确抵消保留。
每个函数 $g$ 的虚位移损失是
$2^{-16}M_{g_x}+2^{-11}M_{g_\theta}$。
由已证实数下界减去该损失，才得到上表的**正实部**界。

例如实域的基线取 $A^2\ge A_-^2$、$H^2\ge h_-^2$、
$J\ge h_-A_-$、$F_3\ge Q_-\inf I_c$。对应虚位移的最大损失分别为
.012797、.001318、.005296、.000566，已逐项扣除。

## 4. κ 的可去奇性与实际复下界

仍取同一个真均值 $E=\langle F_x\cdot F_x\rangle$ 的解析延拓。
有

$$
E'=2\langle X\cdot X_2\rangle,
\qquad E'''=2\langle X\cdot X_4+3X_2\cdot X_3\rangle,
$$

以及准确恒等式

$$
C''=a'E'''-3a'''E'-2a''''E.
$$

程序给 $|C''|<4538636.133$，所以从实 collar 的
$C'>231.2144894622$ 扣去虚径向损失
$2^{-16}\sup|C''|<69.254092$ 后，仍有 $\Re C'>161.9603$。
令 $t$ 为已严格证明的准确实根，则

$$
\frac{C(z)}{z-t}=\int_0^1C'(t+s(z-t))ds
$$

在根处准确延拓且正实部有同一下界。整个线段留在当前复径向矩形中。
最后

$$
\kappa(z)=\frac{\int_0^1 C'(t+s(z-t))ds}{2a(z)E(z)^2}.
$$

分子正实部、$a,E$ 的正实部和各自模上界支付所列 $|\kappa|$。
虽不据此声称 $\Re\kappa$ 有同一下界，但它已给出无零点以及一个
明确解析对数分支。负根 collar 由准确 $z\mapsto-z$ 反射给相同模界；
负侧 $C'$ 的实部符号相反，不能直接照搬正号。

## 5. 冻结输入与重放

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_root_complex_gate.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --root-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_symmetric_root_interval.json \
  --scalar-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_core_scalar_gate.json \
  --core-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_core_interval.json \
  --radial-width .0000152587890625 --angular-width .00048828125 \
  --out /tmp/visible-root-complex-gate.json
```

永久输出 `data/phase_ring_continuation/type_fixed_step02_root_complex_gate.json`
的 SHA256 为
`f8168f39d19893c5a8615a0cfa66dd79789c83ce85e42abe7b1c2e183eebc5c5`。
源 SHA256 为
`cfdda23bef1543d11cb3c8de21a93cec4e17c68b695eebd7c53d2a00162370f0`。
报告记录所有依赖、完整实证书 hash、混合相位/切向量/位置 majorant
以及每个损失项。新物理多项式 jet 的低四阶与原 root evaluator 的
包络逐项有交；混合 Bell 的线性指数特例也核对通过。

所有数值端点仅用有向基本运算、有理 exp 余项、有限多项式和经过
准确有理平方比较的平方根上界。复归一化的分母有明确正实部。
本门仍不支付参数管、canonical 坐标单叶性、完整 β 区间、传递
算子或闭帽；它只提供这些后续工作可以直接引用的实际局部分母与域宽。
