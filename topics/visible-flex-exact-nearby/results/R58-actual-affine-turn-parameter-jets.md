# R58 — 真实 affine 参数族的转折根二阶导数与端点正规化

2026-11-12。**已证明。** 本文数学证明与程序在执行器更换后重建，
全部区间已实际重新计算；下列数字来自新的有向输出，不从旧摘要拼造。

## 1. 对象与结论的范围

沿用 R57 的准确 affine 参数族。原始样条控制值为
$S_p=S_0+pV$，三个均值参数为 $\alpha_p=\alpha_0+pw$，
固定的半径修正与背景权重不随 p 改变。先乘实际背景权重，再明确
作 $a,\beta$ 的偶对称和 $\gamma$ 的奇对称；高度导数取实际
偶斜率，高度由零点积分定义。角向位置使用 R33 的无限单位切向量
原函数。此对象并不等于把控制值逐个舍入后的另一张图。

写
$$
 g_0(p)=E(x,p)\,dx^2+a(x,p)^2\,d\theta^2,
 \qquad E=\langle |F_x|^2\rangle_\theta.
$$
这里目标度量与 p 同步改变。令
$$
 C=a_xE_x-2a_{xx}E,
 \qquad K=\frac{C}{2aE^2}. \tag{58.1}
$$
R57 已给共同闭 collar 上的 $a,E>0$、$C_x>0$ 及唯一根
$t(p)$。本文计算的是这个真实族的 $t'(p),t''(p)$，不是
径向背景作用量的导数，也不是 rounded predictor 的差商。

令 $s\in[\operatorname{binary64}(.999),1]$，定义
$$
 Q(s,p)=\frac{-K(t(p)s,p)}{1-s^2}. \tag{58.2}
$$
在 s=1 处取连续延拓。本文同时给固定 s 时的 $Q_p,Q_{pp}$
严格区间计算方法。若使用 $-K/(t^2-x^2)$ 的另一规范，则该量为
$Q/t^2$，不能遗漏此因子。

## 2. 有限混合 Taylor 代数

在
$$
 \mathcal A=\mathbb R[u,v]/(u^6,v^3)
$$
中表示归一化混合 jet
$$
 [f]_{ij}=\frac{\partial_x^i\partial_p^j f}{i!j!},
 \qquad 0\le i\le5,\quad0\le j\le2. \tag{58.3}
$$
乘法就是截断卷积，因而准确实现 Leibniz 公式。非恒定理想中的
元素 $\nu$ 满足 $\nu^8=0$：存活单项式总次数至多 7。
所以对任意解析标量函数 f，其复合准确为
$$
 f(c+\nu)=\sum_{k=0}^{7}\frac{f^{(k)}(c)}{k!}\nu^k
 \quad\text{在 }\mathcal A\text{ 中}. \tag{58.4}
$$
特别地，sin、cos、exp 只需有限多项式；若常数项 c 的区间不含
零，则逆为 $c^{-1}\sum_{k=0}^7(-\nu/c)^k$。这里没有截断
Taylor 余项，因为舍去的单项式在所需 jet 商代数中准确为零。

区间常数项和区间四则运算把所有真实系数包含其中。三角常数项
仍须用有向的标量三角函数预算，不能将普通 sin/cos 的浮点值直接
视为准确端点。对全部系数使用向外运算，有限卷积和式 (58.4) 即
给混合 jet 的包含关系。

原始 affine 样条在参数方向只有 0、1 阶：
$$
 [S]_{i0}=(S_0^{(i)}+pV^{(i)})/i!,\quad
 [S]_{i1}=V^{(i)}/i!,\quad [S]_{i2}=0. \tag{58.5}
$$
不能先把所有控制值分别扩成一个独立盒，再对那个盒任意求导来
代替式 (58.5)；该做法会丢失实际参数方向与各径向导数的关系。

每个径向闭单元使用所选样条多项式的实际导数。对称化第 i 阶
导数按
$$
 \tfrac12\{S^{(i)}(x)+\epsilon(-1)^iS^{(i)}(-x)\},
 \qquad \epsilon=+1\text{ 或 }-1,
$$
计算。闭单元中心允许是端点；高阶多项式系数取该单元所选 span
的值，不能跨相邻多项式取不对应的端点导数。

## 3. 实际单位切向量及无限原函数的混合 jet

旋转基中的单位切向量为
$$
 T=(-\cos\gamma\sin\beta,\ \cos\gamma\cos\beta,\ \sin\gamma).
 \tag{58.6}
$$
将实际 $\beta,\gamma$ 的混合 jet 代入式 (58.4)，可得到全部
18 个切向量系数。primitive 是线性算子，所以混合求导与它可
交换；有限 Fourier primitive 的每个系数由相同线性矩阵计算。

为支付无限角尾，设 B、G 是各混合相位系数在角复带
$|\operatorname{Im}\theta|\le\sigma$ 上的非负系数模上界多项式。
水平旋转基另外贡献 $e^\sigma$。逐系数非负 majorant 可取
$$
 M(u,v)=2\exp(\sigma+B(u,v)+G(u,v))+\exp(G(u,v)).
 \tag{58.7}
$$
因此 $[M]_{ij}$ 控制对应 Cartesian 切向量 jet 的三分量绝对
值之和。将 R33 的线性 primitive DFT/截断尾因子
$\Phi_0(N,m,\sigma)$ 逐个乘以 $[M]_{ij}$，得到每个
primitive jet 的误差。复合里的常数指数也须向外计算；不能只
给有限 FFT 的加密差。

对本接口，quarter 角节点数 256 对应全圈 N=1024；去掉 quarter
Nyquist 后的 Cartesian 最高频率为 m=509。有限 primitive 的
平方最高频率 1018 小于 1024，所以全圈离散均值对有限 primitive
的二次内积准确。旋转基表达产生相同的物理标量均值。

$F_x=a_x\mathcal PT+a\mathcal PT_x+Z_x e_z$。对半径 jet 与
primitive 误差作同一截断卷积，得到实际 $F_x$ 所需混合 jet
的误差。若两项有限向量的范数上界为 $L_1,L_2$，误差范数
上界为 $\varepsilon_1,\varepsilon_2$，则
$$
 |\langle X_1+e_1,X_2+e_2\rangle-
   \langle X_1,X_2\rangle|
 \le L_1\varepsilon_2+L_2\varepsilon_1+
       \varepsilon_1\varepsilon_2. \tag{58.8}
$$
对归一化 jet 中每一对卷积项使用式 (58.8)，即付清
$E=\langle F_x,F_x\rangle$ 的无限 primitive 费用。有限 DFT
本身的区间算术、三角函数与累加误差仍通过同一向外 evaluator
计算，不由式 (58.8) 免费覆盖。

式 (58.1) 再经卷积与区间倒数得到 C、K 的混合 jet。只请求已
由输入支持的阶数：C 至 x 三阶、p 二阶；K 至 x 三阶、p 二阶。
由五阶 F jet 得到四阶 E jet 足够，不能把截断后人为置零的更高
系数当作真实高阶导数。

## 4. 根的参数导数

共同 collar 上 $C_x>0$，根位于同一光滑样条多项式区，因此
隐函数定理给 C² 参数根。对 $C(t(p),p)=0$ 求导得
$$
 t'=-\frac{C_p}{C_x}, \qquad
 t''=-\frac{C_{pp}+2C_{xp}t'+C_{xx}(t')^2}{C_x}. \tag{58.9}
$$
所有 C 导数必须在共同根区间乘参数管上求包含区间，而非仅在
一个浮点根中心取值。先包 $t'$，再将其包含区间代入第二式；
丢失的变量相关性只放宽区间，不影响包含关系。

## 5. 端点商的无奇性公式与两个参数导数

令 $\xi=1-u(1-s)$，u∈[0,1]。由 K(t,p)=0 与基本微积分定理，
$$
 Q(s,p)=\frac{t}{1+s}I_0,
 \qquad I_0=\int_0^1 K_x(t\xi,p)\,du. \tag{58.10}
$$
该式在 s=1 仍成立，自动包含连续延拓 Q(1,p)=tK_x(t,p)/2。
固定 s（所以固定 $\xi$）求导，写
$$
 I_1=\int_0^1\{K_{xx}\xi t'+K_{xp}\}\,du,
$$
$$
 I_2=\int_0^1\{K_{xxx}\xi^2(t')^2+
             2K_{xxp}\xi t'+K_{xx}\xi t''+K_{xpp}\}\,du.
 \tag{58.11}
$$
于是准确地有
$$
 Q_p=\frac{t'I_0+tI_1}{1+s},\qquad
 Q_{pp}=\frac{t''I_0+2t'I_1+tI_2}{1+s}. \tag{58.12}
$$
必须保留 $K_{xx}\xi t''$ 和两个外层乘积项；只对 K 的显式
参数依赖求导是不完整的。

先确认全部 $t\xi$ 落在共同 collar，再对各 integrand 作统一
区间包络。积分区间长度为 1，故 integrand 的包含区间本身就是
积分的包含区间；这一步不使用未认证的数值求积。如此得到的
Q、Qp、Qpp 同时包含 s=1。

## 6. 本次实际重新生成的有限证书

准确参数管为 $|p|\le\operatorname{binary64}(.01)$。共同根区间
为 $[\operatorname{binary64}(.238394),\operatorname{binary64}(.238400)]$。
共同 collar 以准确有理数 $238397/10^6$ 为中心、$1/4096$ 为半径；
执行时使用向外 binary 包
$[.238152859375,.23864114062500003]$。对全部
$s\in[\operatorname{binary64}(.999),1]$，程序先以有向乘法确认
$t s$ 落在该 collar 内。

本次输出的根导数包含区间为

| 量 | 向外 binary64 下端点 | 向外 binary64 上端点 |
|---|---:|---:|
| $t'$ | $6.09017437625649\cdot10^{-5}$ | $6.131183542564892\cdot10^{-5}$ |
| $t''$ | $-9.611822624178768\cdot10^{-7}$ | $-9.192323068841328\cdot10^{-7}$ |
| $Q$ | $6.326887717921247$ | $8.008205957629116$ |
| $Q_p$ | $-.0331470360721899$ | $.034189594869203636$ |
| $Q_{pp}$ | $-.003856195442885595$ | $-.0015585858385117426$ |

这些长端点按 JSON 中 binary64 的准确值解释。可直接使用较松的
有理安全界
$$
6.09\cdot10^{-5}<t'<6.132\cdot10^{-5},\qquad
-9.612\cdot10^{-7}<t''<-9.192\cdot10^{-7},
$$
$$
6.326<Q<8.009,\quad -.033148<Q_p<.034190,\quad
-.003857<Q_{pp}<-.001558. \tag{58.13}
$$

共同根盒上本次有向计算给
$299.7439775069<C_x<300.7596878140$，且 $C_p<0$；
共同 collar 上 $a>1.09697$、$E>1.50720$、$K_x>53.07925$。
完整 C/K 混合导数、每个归一化 primitive 尾误差及 mean 修正均在
下面的报告中。角带选择为 $\sigma=.08$，quarter 节点 256；
没有用角节点加倍差替代无限尾。

报告：`data/phase_ring_continuation/type_fixed_step02_d5_parameter_root_jets.json`，
SHA256 `a69184f1236ccef8fa595d42fa505bf6178cbc9c6acfd9ebbb1127ad0e37e3b9`。

计算源 `scripts/fourfold_phase_parameter_root_jets.py`，SHA256
`1c31538344f81ab201a28148bdcb3eb78b9cf04391b453a11ac79abcc27d6f7a`。
有限代数源 `scripts/fourfold_mixed_jet_algebra.py`，SHA256
`d895f1fdd917776a45a80872aab50ed9ce1820d6d03f40a468602dbbc67f81c8`。
程序在每次执行前，用准确 Fraction 对全部 18 个混合系数核验
$\sin(2u+3v)$、$\cos(2u+3v)$、$e^{2u+3v}$ 和
$(1+2u+3v)^{-1}$ 的独立闭式表达；这只是实现回归，完整依据仍是
§2 的有限代数证明。

来源为 R55 的准确 full-inputs SHA
`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`，
R57 方向 SHA `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`，
共同根报告 SHA `b5900c391667b2a1be90912f2abaf58eaea66dfc51c082a8db39ea582b4b94a8`。
依赖源 SHA 全部保存在新报告中。

在课题目录重放：

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python scripts/fourfold_phase_parameter_root_jets.py \
      --inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
      --frozen-direction data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
      --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_parameter_root_interval.json \
      --out /tmp/visible-R58-root-jets.json

本结果支付真实移动端点的两个参数导数和根附近商的二阶源。
它不支付整个 ODE 的残差、复角流域、返回映射的二阶参数范数，
也不将有限 ray 的 Jacobian 或差商升格成精确返回算子。

