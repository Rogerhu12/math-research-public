# R623 同一归一化角场的有限线性 primitive 与完整余项

2026-11-27。**已证明的新全角 primitive / 曲率充分接口；尚未执行新科学。**
本条针对同一实际 97q 材料，完整保留原归一化、四个 Fourier 模式及所有
径向控制，只改善 [R621](R621-normal-projected-covariant-blocks-and-reach-input.md)
中的 primitive 上界。不把它解释成新曲面，也不把 a237 原 K 上界当成真实峰。

## 1. 先追溯实际源码：垂直切向量不是 v

原 `r582_local_tail_columns_model_20261126.py` 的 `geometry` 明确定义

\[
T=c\{-\sin(\theta+u),\ \cos(\theta+u),\ v\},
\qquad c=(1+v^2)^{-1/2}.
\tag{1}
\]

因此真实垂直分量为 **C=vc**。`r604_rotating_frame_continuous_norms_20261127.py`
的 `rotating_difference` 同样准确返回 `C=v*c`，原 R621 已按这一定义执行。
有限 Fourier 的是原变量 v，不能把 C 偷换成 v。

令原四频率为 $m=2,4,6,8$。按原 `angular`、`seed_v`、尾部矩阵的
onset-major / mode-minor 索引，实际有

\[
v(s,\theta)=\sum_{j=0}^3 b_{2(j+1)}(s)\sin(2(j+1)\theta),
\tag{2}
\]

\[
b_{2(j+1)}(s)=B_j^v(s)+\epsilon V(s)
\left[\mathbf1_{j=0}+\mathbf1_{j<2}\sum_{\ell=0}^3
q_{88+2\ell+j}\chi_\ell(s)\right].
\tag{3}
\]

这里 $B_j^v$ 为原 enveloped degree-five B-spline，八个控制数依次是
`q[32+j:64:4]`；$V=-2C_{\rm seed}/a_{\rm frozen}$ 是同一原
common-endpoint Hermite seed 和同一冻结半径商所定义的场；
$\epsilon=p-.18$ 按原 stored real 参数解释。四个原 gate 为
`(.78,.82)`, `(.82,.84)`, `(.84,.86)`, `(.86,.88)`。
(3) 的 value / s / ss 包含原全部乘积导数。首个 mode2 seed、
八个 v 尾部控制、mode6/8 的 B-spline 均保留。

现有 `SameFieldRadialDesign.coefficients` 已实现这个准确组合，并先把
同一 seed 的所有 gate multiplier 合并再做 interval hull；新接口一次
读取该结果，既生成原 u/v 全角 jets，又生成下述 primitive 界。
不重新拟合、舍弃小系数、换 seed，亦不在 seed zero suffix 丢掉仍存在的
B-spline 角场。全部 float 数据均沿用原准确 binary64 参数的实数定义。

## 2. 有限线性 primitive 的准确全角界

记 P 为周期 $2\pi$ 的唯一零均值 primitive。由于所有频率非零，

\[
\partial_s^j Pv(s,\theta)
=-\sum_{m\in\{2,4,6,8\}}\frac{b_m^{(j)}(s)}m\cos(m\theta),
\quad j=0,1,2.
\tag{4}
\]

因此简单的逐系数上界是

\[
L_j\le\sum_m\frac{\sup|b_m^{(j)}|}{m}.
\tag{5}
\]

还可在同一份系数盒上无采样地保留四频率的角相关性。令
$x=\cos(2\theta)\in[-1,1]$、$t=(x+1)/2\in[0,1]$，则(4)是

\[
Q_j(t)=-\sum_{k=1}^4\frac{b_{2k}^{(j)}}{2k}T_k(2t-1).
\tag{6}
\]

它是一个次数至多四的多项式，未截断任何频率。四个 $T_k(2t-1)$ 的
共同 degree-four Bernstein 系数是以下**准确有理数**：

| k | B0 | B1 | B2 | B3 | B4 |
|---:|---:|---:|---:|---:|---:|
| 1 | −1 | −1/2 | 0 | 1/2 | 1 |
| 2 | 1 | −1 | −5/3 | −1 | 1 |
| 3 | −1 | 7/2 | 0 | −7/2 | 1 |
| 4 | 1 | −7 | 35/3 | −7 | 1 |

例如 $T_3(2t-1)=32t^3-48t^2+18t-1$，
$T_4(2t-1)=128t^4-256t^3+160t^2-32t+1$；上表直接由
$t^r=\sum_{i=r}^4\binom{i}{r}/\binom4r\,B_i^4(t)$ 得到。

把每个真实径向系数的 interval 代入上表，使用向外加、乘、整数除法。
再用准确分点 $1/2$ 的 outward de Casteljau 两层，把整个 `[0,1]`
覆盖为四个闭子区间。Bernstein 基函数非负且和为 1，所以每个完整
子区间上 Q 的值都在该子区间系数的 hull 内；所有子区间上最大绝对
端点是全角上界。取它与(5)右端较小者，仍是合法 $L_j$。
这里没有选若干 theta 点代替连续角域，也没有用浮点根查找冒充极值证书。
径向 s 与角变量的系数依赖只使盒更宽，不影响包含关系。

## 3. 完整归一化余项与无限角尾

准确写

\[
C=v+R(v),\qquad R(v)=v(c-1).
\tag{7}
\]

用稳定恒等式，避免两个近 1 数相减：

\[
c-1=-\frac{v^2c^2}{1+c},\qquad
R'(v)=c^3-1=(c-1)(c^2+c+1),\qquad
R''(v)=-3vc^5.
\tag{8}
\]

所以在同一 complete u/v jet box 上，

\[
R_s=(c^3-1)v_s,\qquad
R_{ss}=(c^3-1)v_{ss}-3vc^5v_s^2.
\tag{9}
\]

(7)--(9) 都是原归一化场的准确实数恒等式，不是有限 Taylor 截断。
余项所含无限 Fourier 频率全部保留在这些连续 interval 界里。

原 v 是奇函数且为 $\pi$ 周期；c 是 v 的偶函数，因此 C、R 和它们的
s、ss 导数也为奇函数、$\pi$ 周期，在完整一周期内均值为零。
把已付 R504 的周期 $2\pi$ primitive 界按角变量缩放，周期 $\pi$
的常数是 $\pi/4<11/14$。故

\[
\|\partial_s^j PC\|_\infty
\le L_j+\frac{11}{14}\|\partial_s^jR\|_\infty=:Z_j,
\qquad j=0,1,2.
\tag{10}
\]

也可用同一周期性直接得到
$\|\partial_s^j PC\|_\infty\le(11/14)\|\partial_s^j C\|_\infty$。
两者较小值仍有效。新实现同时保留这个备选界，不预设线性分解在所有
cell 都更紧。原 `rotating_difference` 对 C 的完整归一化导数一直保留。

## 4. 原水平 primitive 与 R621 分块继续完整成立

沿用原旋转 frame：

\[
\Delta T=T-e_\theta=Ae_\theta+Be_r+Ce_z.
\]

u、v 与 c 的 $\pi$ 周期性使水平向量 $Ae_\theta+Be_r$ 在角平移
$\pi$ 时取反，因此其完整角均值为零；s、ss 导数同样成立。
新接口仍使用原完整常数 $11/7>\pi/2$，定义

\[
H_j=\frac{11}{7}\sup\sqrt{(\partial_s^jA)^2+(\partial_s^jB)^2}.
\tag{11}
\]

环境水平 / 垂直正交，故完整 vector primitive 由
$P_j=\sqrt{H_j^2+Z_j^2}$ 包住；它还可与原
$(11/7)\sup\sqrt{A_j^2+B_j^2+C_j^2}$ 取较小值。
这些每一个都是全角上界，取 min 不需要它们在同一个 theta 取得最大。

对原参考单位法向
$n_0=n_r e_r+n_z e_z$，其 reference-normal primitive 界改为

\[
N_j=|n_r|H_j+|n_z|Z_j.
\tag{12}
\]

参考法向依赖 theta 不妨碍此式：对每个 theta 先用点态水平投影不超过
水平向量范数，再取全角 sup。没有把变系数法向穿过 primitive 算子。

现有 R621 的 H11、H12、H22 公式原样保留：只将其完整 primitive 大小
替为 Pj，将其 reference-normal primitive 大小替为 Nj。H12、H22 的
直接角导数部分仍使用原完整 A、B、C 和 theta jets，未以线性 v 替换 C。
current / reference a、z 的全部一二 jets、Christoffel 系数、直接
current-reference 差场保持同一材料与同一 reference。

## 5. 从这同一 cell 到实际主曲率

完整微分差由同一盒仍可包为局部 alpha。若此前已对**同一个 q / mesh /
参考面 / 完整闭材料**证明全域 alpha≤A<1，则可用两个合法上界的较小值；
这只是消费已有结论，不重新发出全域 C1 或 C0 证书。
令使用的 cell 上界为 a<1，原 R621 给 oriented-normal 差

\[
\gamma=a\sqrt{\frac2{1+\sqrt{1-a^2}}}.
\tag{13}
\]

令 bij 是原 reference-normal H 块的上界，hij 是相同实际环境 H 块的
上界。实际法向块由 $b_{ij}+\gamma h_{ij}$ 包住。再加同-cell 参考面
真实子午 / 周向曲率绝对上界 km、ko，得到非负对称矩阵

\[
M=\begin{pmatrix}
k_m+b_{11}+\gamma h_{11}&b_{12}+\gamma h_{12}\\
b_{12}+\gamma h_{12}&k_o+b_{22}+\gamma h_{22}
\end{pmatrix}.
\tag{14}
\]

其最大特征值的准确公式除以 $(1-a)^2$，即实际两主曲率绝对值的上界。
证明与 R621 完全相同：实际参考二阶项投到新法向只缩小参考曲率绝对值；
换材料联络只差实际切向，投法向后消失；实际单位切向的参考长度至多
$(1-a)^{-1}$，二次代入给最后的平方因子。

新 helper 返回新 K 以及原完整环境块、reference/current-normal 块、
每频率的完整径向系数盒、线性/余项 primitive 和实际所用 alpha 诊断。
它本身不提供未遍历区域的结论，也不借旧局部叶表宣称新 K 全域成立。

## 6. 本次 a237 的准确应用范围

待公开新科学将只消费原 run `45895935112` / job `140169696746` 已完整付清的
同一 a237 全域 reference rho/D、delta/alpha 和材料/闭合/帽/core 身份。
新的任务是用以上新盒遍历完整材料半径、原全角公式、全核心柱、上下反射
和两 Cartesian flat cap，取得新全域 K。参考认证和原 global C0/C1 门
不重跑，也不把它们转借给后继优化的不同 q。

同一未保存的材料端点数组 / interval 高度 prefix 如必须再生，费用全部
计入新 scope；mesh hash 必须仍包含 knots 和全部 endpoint jets，不只
核对网格坐标。旧 fine/Jac/方向/7点诊断不重放。若有区间未覆盖，不能授予
新全域 K；有效宽界在精化终止处照实保留，不剪成目标预算。

完整新 K 可以与上述旧的**同 q 完整输入**接到 R604，必要时接 R622；
每张充分证书都使用自己准确的近门与近项，不混拼两个近远结果。
这个接口没有证明固定 g 的 metric refinement、宏观振幅或主课题完成。

实现：[r623_finite_vertical_primitive_curvature_20261127.py](../scripts/r623_finite_vertical_primitive_curvature_20261127.py)。
本地只有纸证、源码 / AST / hash；没有执行任何新 primitive 或曲率值。
