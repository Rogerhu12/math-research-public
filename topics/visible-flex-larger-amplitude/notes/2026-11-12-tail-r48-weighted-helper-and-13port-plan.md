# R48 插值与 R44 完整均值、连续缺陷接口

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

## 已完成的接口

tail_outer_weighted_compatible.py 以 R48 的五个真实正积分定义同一条高度曲线。它保留完整输入角频谱，固定同一个 bubble 系数，由同一积分计算 $H$，直接由四次多项式计算 $\overline K,\overline K_x$。左右累计正积分给同一高度的两个区间包络，可相交收紧。调用 R44 的共享代数核后，完整 mean 根、mean 的实际径向导数、全部残差频率和 Darboux 缺陷仍按原式计算。

tail_outer_compatible_mean_defect.py 的普通物理 $r$ 五次插值入口保留原签名和运算公式；仅把共享的完整 mean 与残差部分提取成内部函数。共享函数本身不证明任意输入场兼容，只有两个明确的构造器支付 $H_x=r_xw\overline K$ 与实际导数身份。

这些接口不把输入积分区间自动当作已证明的积分。实际 source 积分器必须保证总积分、左累计和右累计属于同一个真实背景、同一组五个 integrand。端点 connection momentum 也不由插值自动匹配。

## 实际 13port 候选的坐标

现有 tail-outer-strong-m20-port-norms-recovery.json 有 13 个真实半径端口、全部 20 个 binary $Q$ 和有限角根输出的 binary $L$。它没有各内部端口的二阶 jet。当前尚未用它启动本插值器的真实背景积分。

每个胞元的九段具有不同未 warped source 长度 $\ell_j$。使用一个胞元坐标

$$
u_j(x)=\frac{\sum_{i<j}\ell_i+\ell_jx}{L},
\qquad L=\sum_{i=0}^{8}\ell_i,\qquad
\frac{du}{dx}=\frac{\ell_j}{L}.
$$

因此

$$
r_u=\frac{L}{\ell_j}r_x,\qquad
w_u=\frac{L}{\ell_j}w_x,\qquad
(r_uw)\,du=(r_xw)\,dx.
$$

不能用 $j+x$ 等长拼接替代这个坐标；那样会人为改变物理二阶导数。胞元由内到外是段 $0$ 至段 $8$，左右端口分别是 node $n+1$ 和 node $n$。

## 下一实际输入的定义与待支付项

1. 同一 response、完整 160 个冻结校准参数和 R26 实半径账本保持不变；不重新校准 warp 去强迫最外半径等于 binary $0.3$。
2. 高度使用该 13port 候选自己的 $r^4Q$ 定义，非均值斜率使用其全部 $L$ 与 $P_\theta$。这与准备中的 109 点工具在 cut 使用 exact cutHeight 的约定不同，不能混成同一输入。
3. 内部二阶 jet 必须另行定义并保留来源。拟取同一端点场的有限 Fourier PDE 导数投影作为**候选定义**，保持原全部 20 模；其有限 mean 和乘法逆截断产生的差进入 R44 实际残差，不宣称它等于真实全频轨道的二阶导数。若该定义不足以得到小残差，需增加真正保存的 source 节点；不能以 13 点小性外推整胞元。
4. 每胞元只需五个背景积分，但总积分和用于包围 $H(u)$ 的累计积分都须严格核算。可从 R26 已保存的段内真宽度与 branch/sign 面板开始。对正宽度 $\Delta r$，$\Delta r\inf(wq)\le\int wq\,dr\le\Delta r\sup(wq)$；细分时仍需同一真实 $r_x$ 的严格子宽度，不能插值 binary 半径。
5. 每个面板分别记录 $I_b$ 的严格正下界、bubble 系数、$P$ 的全角范数、完整 mean 根门、真实 $r,r_x,w,(\log w)_x$ 盒、全部 $\mathcal J$ 系数和 Darboux 残差。$I_b$ 很小时端点误差的放大按 R48 §5 明示。
6. 全部径向面板验证、外头 Green/Schur 门和与精确深头 trace 的差仍未支付。109 locator 当前未运行。

### 已落实的端点候选定义

tail_outer_weighted_endpoint.py 已把第 3 项写成可执行的有限代数接口，尚未在实际 13port 上执行。令 $\widehat c$ 为保存的 binary mean，$T=P_\theta$，

$$
W=\frac{\overline K+ET}{1+\widehat c},\qquad
I_J=\frac1{1+\widehat c}\sum_{j=0}^{J}(-W)^j.
$$

在 $\|W\|_{\tau,1}<1$ 时，

$$
\|L^{-1}-I_J\|_{\tau,1}
\le\frac{\|W\|_{\tau,1}^{J+1}}
{(1+\widehat c)(1-\|W\|_{\tau,1})}.
$$

完整 numerator 逐项使用 R44 的真实有限 Fourier 多项式。将它乘 $I_J$，投影回原全部 20 个非均值模式，再加准确线性项，定义候选 $\overline K_x$。被投影掉的非均值多项式尾及上式逆余项均显式记录。

随后定义 $H_r=w\overline K$ 和
$H_{rr}=w(\overline K_x+\ell\overline K)/r_x$。
这些是一个明确候选的端点 jet；R48 用同一正权积分曲线匹配它们，R44 再恢复真实完整 mean 并计算实际连续缺陷。因此没有把投影 PDE 导数当作已经验证的真实径向导数。

单胞元 source 坐标在两端按真实恒等式精确设为 $0,1$；不把同一总长度的两个区间副本相除后得到的虚假端点宽度当成几何误差。面板的实际坐标属于 $[0,1]$ 由 source 定义支付；计算 hull 与该数学区间相交，允许 Arb 半径向外舍入造成的极小越界。

## 小算术验证

只执行了常正权 $\mu=2$ 的有限多项式 fixture。精确目标

$$
K(u)=2^{-20}(u^4+2u^3+3u^2+4u+5)
$$

及其积分提供两个端点，五个积分精确为
$(1,1/6,1,1/6,1/15)$。在 $u=0,1/3,1$ 检查同一 $H,K,K_x$，另检查不等长九段坐标，11 项均通过。该 fixture 没有调用实际 source、Node、BVP、径向流或真实背景积分，不是 13port 径向证书。
