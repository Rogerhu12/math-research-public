# R133：完整有限 body 与真实 natural graft 的三阶目标 jet

**已证明；实际完成所列7条闭盒与右侧接缝点。** 本篇将已付的
compact-metric 目标系数接口扩到完整有限区间 $[0,25/8]$，给同一个
真实目标的

$$\gamma^{(j)},\ \beta^{(j)},\ K^{(j)},\ s^{(j)},
\qquad 0\le j\le3,\quad s=1/C_r<0.$$

每次调用只在一个真实 scalar germ 和一个 compact-control 多项式片
内工作。原 $[0,1.5]$ 的已用源码完全不变。新增 body 使用原完整 unit
primitive 及全部无限 Fourier 尾；新增 natural graft 使用原实际
构造的完整 Wiener Taylor majorant，不把它替换成完全旋转的模型。

本篇证明的是正确的系数包络算法及已经执行的列明闭盒。尚未执行的
径向盒须在真正 residual producer 中逐盒计算；七处调用不是整个
$[0,25/8]$ 已数值覆盖的证书。也没有据此声称新的 moving BVP 或闭
surface 已存在。

## 1. 准确约去半径的共同公式

设原真实相位图的单位 primitive 修正为 $P$，原圆柱背景为 $(a,z)$。
取

$$L=a'/a,\quad H=z'/a^2,\quad u=LP+P_r,$$
$$e=2L\langle u_x\rangle_\theta+\langle u\cdot u\rangle_\theta.
\tag{J.1}$$

原相位 primitive 的竖直平均为0，其实际径向度量均值于是准确满足

$$E=a^2\overline E,\qquad
\overline E=L^2+a^2H^2+e,\qquad
R=H^2+e/a^2=(E-a'^2)/a^4.\tag{J.2}$$

由 $K=-(a'/\sqrt E)'/(a\sqrt E)$ 直接代入 (J.2)，全部大半径幂先
代数相消，得到

$$
N=H^2(L^2-L')+LHH'+\frac{Le'-2L'e}{2a^2},\qquad
K=N/\overline E^2.
\tag{J.3}
$$

确实，曲率分子先成为
$[-L'\overline E+(L/2)\overline E']/a^2$，展开
$\overline E'$ 即是 (J.3)。因此没有在小 $a$ 处分别估计两个巨大
$a^{-2}$ 项后再相减。

对同一真实控制 $E_\nu=E e^{\nu h}$，记 $G=\overline E e^{\nu h}$。
准确受控旋转间隙为

$$R_\nu=H^2+e/a^2+(\overline E/a^2)\operatorname{expm1}(\nu h),$$
$$K_\nu=e^{-\nu h}\left(K+\frac{\nu Lh'}{2a^2\overline E}\right),
\quad\gamma=\sqrt G,\quad\beta=L,\quad
s=-\sqrt{G/R_\nu}.\tag{J.4}$$

`expm1` 保留了支持外以及支持边缘的准确消去。程序先验证
$a>0,\overline E>0,G>0,R_\nu>0$，再取相应实平方根；它不要求
$K$ 严格同号，故在原 body 的真实 $K=0$ 处也没有除以 $K$。

把 (J.1)–(J.4) 视为以当前真实径向点为中心的 Taylor jet 运算。
$a,z$ 各保留0至5阶实际导数，$L,H,e$ 保留0至4阶 Taylor 系数。
(J.3) 中只有一次径向微分，所以完整 $K$ 三阶 jet 全部有输入。
$\gamma,\beta,s$ 的三阶也同样由这些输入形成。每个输出在最后才乘
$j!$ 变成真实导数；没有把 Taylor 系数误标为导数。

## 2. 新增 body 的完整 primitive 与六阶输入

在 $1.5<r\le3$ 上使用同一原 scalar spline 的准确局部多项式、完整
仿射参数和 unit primitive。实际 Horner jet 保留到5阶；有向 FFT 只
给有限 coefficient 部分，其原解析尾仍按相同 radial Cauchy 半径
支付。若零阶完整余项为 $\varepsilon$、半径为 $\rho$，则

$$\varepsilon_j\ge j!\varepsilon/\rho^j\quad(0\le j\le5)$$

同时控制每个 primitive 分量的相应导数。它是对原完整解析尾先求
导数界，不是对已包住零阶误差的区间形式微分。

对 $0\le n\le4$，先形成

$$u^{(n)}=P^{(n+1)}+\sum_{j=0}^n\binom njL^{(j)}P^{(n-j)}.$$

记其完整分量误差为 $\epsilon_n$，有限部分的每分量 $A_0$ 充分上界
为 $M_n$。真实能量导数由完整乘法公式

$$e^{(n)}=2\sum_{j=0}^n\binom nj L^{(j)}u_x^{(n-j)}(0)
+\sum_{j=0}^n\binom nj\langle u^{(j)}\cdot u^{(n-j)}\rangle$$

给出，其遗漏部分全部由

$$
2\sum_{j=0}^n\binom nj|L^{(j)}|\epsilon_{n-j}
+3\sum_{j=0}^n\binom nj
(M_j\epsilon_{n-j}+M_{n-j}\epsilon_j+\epsilon_j\epsilon_{n-j})
\tag{J.5}
$$

支付。系数3明确包含全部三个空间分量。有限点积采用完整 Fourier
反频率配对，保留真平均；没有把平均删掉或仅从若干角样本估计它。
随后使用 (J.2)–(J.4) 的同一 formal Taylor 运算。

这与已经证明的
[连续互逆残差](R133-supplement-complete-reciprocal-continuous-residual.md)
和[真实稳定正帽 jet](R133-supplement-stable-positive-cap-first-jets.md)
是同一个目标。本次只扩展实际合法 body 区间及完整三阶系数输出。
在 $r\le1.5$ 时，新类直接调用原 `ReciprocalCompactTargetJets`，
保留已经发布的输入和算术。

## 3. 真实 natural graft 的完整高阶 Wiener 费用

在 $3\le r\le25/8$ 令 $x=r-3$、$\ell=1/8$。
使用[原实际 natural graft](R66-actual-family-positive-collar-and-natural-exterior-graft.md)
的准确函数：$\log a$、$H=z'/a^2$、相位 $b_j,g_j$，包括实际
$a^3$ 和 $a^2$ 权、真实入口 Taylor 系数和截止

$$\chi(x)=(1-x/\ell)^5
[1+5x/\ell+15(x/\ell)^2+35(x/\ell)^3+70(x/\ell)^4].$$

这些原函数直接以 `acb_series` 在真实径向闭盒上求0至5阶 jet。
全参数仍在原入口 interval 内；未使用点值拟合。

对一个固定但任意盒内点，把其真实 Taylor 系数的绝对上界作为非负
formal 系数，记

$$B(t)=\sum_{j=0}^5\sum_k|[t^j]b_k|t^j,\qquad
G(t)=\sum_{j=0}^5\sum_k|[t^j]g_k|t^j.$$

原角函数的全部 Fourier $A_0$ 范数满足相应系数逐项界。由于
$\sin$、$\cos$ 的幂级数，所有 Taylor/角卷积由下列非负 series
控制：

$$c_B=\cosh B-1,\quad c_G=\cosh G-1,$$
$$d_x=(1+c_G)\sinh B,\quad
d_y=c_B+c_G+c_Bc_G,\quad d_z=\sinh G,\quad d_h=d_x+d_y.
\tag{J.6}$$

这些是完整非线性三角函数的 majorant，没有截断它们的 Fourier
级数。保留到需要的 Taylor 阶只用于读取对应导数；高于该阶的
未知 Taylor 系数不会进入低阶乘法或合成。

设 $L_a(t)$ 为真实 $L$ 的逐 Taylor 系数绝对值。水平 primitive
算子在允许的四重模上 norm 不超过1，竖直零均值 primitive 的 norm
不超过 $1/4$；其零模的准确结构也保留。因此 $u=LP+P_r$ 的完整
水平和竖直部分由

$$U_h=L_ad_h+d_h',\qquad U_z=(L_ad_z+d_z')/4$$

控制。线性平均项准确只含 primitive 水平第一分量的零模，即
切向差的 $y$ 分量；它由 $d_y$ 控制。因此真实 $e$ 的整个 Taylor
jet 有非负系数 majorant

$$\mathcal E(t)=2L_a(L_ad_y+d_y')+U_h^2+U_z^2.
\tag{J.7}$$

水平两分量的平方和由其 $\ell^1$ 范数的平方 $U_h^2$ 控制，所以
这里不漏另一个水平分量。对 $0\le j\le4$，取
$[t^j]e\in[-[t^j]\mathcal E,[t^j]\mathcal E]$，就支付真实整个
primitive 对平均度量的贡献，包括无限角尾和全部四阶导数。

第五阶相位 jet 恰是 $d_h',d_z'$ 的四阶所需输入。$L$ 只需0至4阶，
由 $\log a$ 的1至5阶提供。无需将只有三阶费用的旧 graft majorant
直接求更高导数。所得 $a,L,H,e$ 再完整代入 (J.2)–(J.4)。
支持外 $h=0$ 准确成立，所以这一真 graft 与主体的 $\nu$ 无关。

程序中的 `complete_primitive_tail_A0` 在该段保存的是整个未展开
primitive 修正的充分 Wiener 界；并非把未算的 Fourier 尾记为0。
各阶 `complete_scaled_energy_error_j` 保存 $j![t^j]\mathcal E$，
与 body 的导数误差字段采用相同单位。

## 4. 真接口及一侧高阶导数

任何非零宽输入不得越过原 scalar germ、$.05,.18$ 控制接缝或 $r=3$。
自然拼接保留原已证 $C^4$ 几何，但不能因此推出目标 $K$ 在拼接处
有全局连续三阶导数。$K'''$ 依赖5阶几何 jet，应按相应真实单片
分别使用。

同样，$r=25/8$ 处接上准确长径向段后，也不能把 graft 的第三曲率
导数免费替成外侧旋转延拓的导数。本次左侧实际 $K'''$ 在该点附近
约为 $-241$；这是保留原截止高阶导数的结果，不是异常或一个可删的
误差。分段 Taylor 残差须在该接口停止，另端使用自己的真 germ。

接口约定：普通 `coefficients(3,3,nu)` 取 body 左侧点 jet。
右侧点须显式调用 `graft_coefficients(3,3,nu)`。两者的低阶共同
几何身份由原实际拼接给出；不对本来允许跳跃的最高阶取人为相等。

## 5. 实际调用、范围和可消费 API

新源码 `scripts/fourfold_codazzi_full_body_graft_target_jets.py` 提供

```python
target = ReciprocalFullTargetJets(object_path, half_width=Fraction(0), nodes=512)
values, germ = target.coefficients(left, right, nu)
```

三个参数均可为准确 `Fraction`。输出的 `gamma,beta,K,s` 以及
后缀 `1,2,3` 是真实径向导数；另给实际 chart 分母、$a,C_r$、完整
primitive 和平均误差。`target.cuts` 包含全部原 body 节点及
`.05,.18,3,25/8`，供真正残差 producer 构造共同分割。

原生文件
`notes/2026-11-13-R133-full-body-graft-third-target-jets-pilot-native.json.gz`
实际正常完成7条非零宽闭盒及 $r=3$ 的独立右侧点 jet，用时约6.14秒。
请求位置为 $1.5,2,2.8,3,3.01,3.0625,3.125$；每条具体端点、原
scalar germ 和 part 都在报告中，不能把位置列表视为径向全覆盖。
每个盒均采用完整 $|\eta|\le10^{-9}$，并与原已完成真参考的
$a,\beta,\gamma,K,C_r$ 包络实际相交，所有门通过。该相交是来源和
单位的检查，正确性证明仍是 (J.1)–(J.7) 的完整算术。

本次记录的主体参数为
$\nu=-80394554034525/2251799813685248$；这些新增盒在控制支持外，
所以它没有被用来偷偷更换支持内部的目标。新 producer 可在新的
真实候选每个闭盒上逐次调用同一 API，支付完整 continuous residual。
本篇不将这些 selected boxes 宣称为新候选的全径向残差证书。
