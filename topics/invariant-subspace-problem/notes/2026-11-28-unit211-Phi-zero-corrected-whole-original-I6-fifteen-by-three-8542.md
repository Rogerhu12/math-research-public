# 正确 Phi 全图：新的十五乘三原 I6 呈示与两个三列标量

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

这是尚未执行的唯一首次新输入，不预记 NS/PS 返回、标量次数、原单位或排空。
源为
`2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py`，
15224 字节，SHA256 84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0。
固定总 120 秒/1 GiB，外驱动 135 秒；嵌套 alarm 包括非正请求都钳到最初截止。

## 1. 原图及与既成、冻结门的区别

当前正确 Phi、物理 $D_{\rm val}\ne0$ 图中，整个 A 与整个 B 已独立排除。正确 f62 的实际首三均值头是
$$
h=\frac{M_n^3L^4AB}{8K^3(1-Q)^4},
$$
$$
s=u-1,\quad K=Q+4s,\quad L=Q-2s(u-2),\quad
M_n=2uL-L^2-u^2Q,
$$
$$
A=4s^2-Q,\qquad B=-Q^2+(12u^2-20u+8)Q-16s^2.
$$
由 $M_n=4bcQ(1-Q),\ P_{02}=2sL,\ P_f=4s^2K$ 及完整 A/B 排除，h 在当前整权图已付。原来源见
[整个正确 B 及首三均值推论](../results/R150-appendix-unit211-Phi-zero-true-entire-Bzero-original-exclusion.md)。

本次不执行 f62 的四头因式或共同头零门，也不执行 fd9 的原斜率因式与六乘二门。fd9 已成的三个正确规则和 N1 余式只按相同参数公式再生；不作新的旧证明审核。旧错误 Rbar 的任何来源均不进入。新的十五列包括完整 NS/PS 和两条三次 overlap，覆盖整个原 N1 斜率零面，不倒置该新斜率。

唯一依赖是
`2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py`，
blob f62e66a27d5c999a54d03631ab8d3b31297e7aa2，
SHA256 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。
只执行到 `def param(p):` 前的 4007 字节必要原四式定义，前缀 SHA256：
dd105b713040712dad7cebeefb489c8e1cf53f56cb5fce8ff0de0bf681d6c669。

## 2. 新动作与两条真实三次原关系

在原已付纯权环 $\mathcal S$ 上，置 $v=(1,T,z)^t$。前三均值给
$$
T^2=a\cdot v,\qquad Tz=b\cdot v,\qquad z^2=c\cdot v.
\tag{1}
$$
这只是生成关系，不假设三个元素自由。系数属于 $\mathcal S[\lambda]$。

令 A、B 为列式
$$
A=[e_T,a^t,b^t],\qquad B=[e_z,b^t,c^t].
$$
则原点的行向量满足 $v^tA=Tv^t,\ v^tB=zv^t$。源首次定义并返回这 18 个动作坐标。

置
$$
c_1=(AB-BA)e_T,\qquad c_2=(AB-BA)e_z.
$$
第一列 $(AB-BA)e_0=0$。写 $f_{TT}=T^2-a\cdot v$ 等，$c_1$ 是
$zf_{TT}-Tf_{Tz}$ 再按 (1) 降次所得的原线性行；$c_2$ 对应
$zf_{Tz}-Tf_{zz}$。源返回完整原多项式身份，不把裸 commutator 当没有来源的关系。

准确矩阵恒等式是
$$
A^2-a_0I-a_1A-a_2B=c_1e_z^t,\qquad
B^2-c_0I-c_1^{\rm coeff}A-c_2^{\rm coeff}B=-c_2e_T^t,
$$
$$
AB-b_0I-b_1A-b_2B=c_2e_z^t,\qquad
BA-b_0I-b_1A-b_2B=-c_1e_T^t.
\tag{2}
$$
上式 $c_i^{\rm coeff}$ 表示规则 c 的标量系数，区别于 commutator 列。源逐 36 个坐标返回 (2)。

## 3. 完整原 NS/PS 的新三列来源

原 $f,t,V,X,Y,A_1,r,s$ 都按同一 E0/N0/P1 恢复。使用真实 dual 乘法
$$
(vw)_1=v_0w_1+v_1w_0
$$
以及完整原 N4 和中心三次 P2 定义，首次在三列规则下计算加权 NS、PS。

每个二元乘法保其完整六个未约化系数 $(\ell_0,\ell_T,\ell_z,h_{TT},h_{Tz},h_{zz})$，定义输出
$$
r=\ell+h_{TT}a+h_{Tz}b+h_{zz}c.
\tag{3}
$$
同时用 $p_0q+p_TAq+p_zBq$ 的独立动作路径返回同一三个坐标。由 (1)，该乘法的原差式正是
$\sum h_i f_i$；加上两个父节点的原差式，逐节点归纳得到整个同源 DAG 的来源。

原多次乘法严格采用原 N4/P2 公式的括号顺序，不假三列运算本身已经结合。无需重新展开完整原六式的巨大迹作另一个审核门。程序仅保节点操作和父编号；每个局部乘子由原两个操作数的实际六系数确定，不积累大的系数历史缓存。

所得 $r_N,r_{NS},r_{PS}$ 是同一个原 I6 中的三个系数列。N1 的已成余式作为定义输入，NS/PS 是本次新完整返回。没有用 NS/PS 的某个模像或加权替代部分取代完整原值。

## 4. 十五列恰好给完整原 I6 商

令
$$
G=(r_N,r_{NS},r_{PS},c_1,c_2),\qquad
\mathcal N=\langle G,AG,BG\rangle_{\mathcal S[\lambda]}.
\tag{4}
$$
由 (2)，对任一 g，$A^2g,B^2g,ABg,BAg$ 都是 $g,Ag,Bg,c_1,c_2$ 的线性组合。因此 (4) 对 A、B 都稳定；不是凭一次数值秩推断闭包。

在商 $\mathcal S[\lambda]^3/\mathcal N$ 中，A/B 交换，满足全部三条规则 (1)，并且 $e_0$ 循环：
$Ae_0=e_T,\ Be_0=e_z$。这给从原多项式商到该模的映射；反向用系数列评价为 $1,T,z$，全部十五列都有原 I6 来源。两映射在三个生成元上互逆，所以这是**精确 I6 呈示**，不是仅同解集的必要行空间。

这里 I6 是前三真均值、原 N1、完整 NS、PS 的理想。必要代数在纯权环上构造，不预先反演几何 D；物理 $D\ne0$ 点进入其开集。没有将 D 局部化后的代数无证称为同一有限模，也不声称模自由。

## 5. 两个真正新三阶原标量

分别取三列组
$$
(r_N,r_{NS},r_{PS}),\qquad (r_N,c_1,c_2).
$$
固定三阶 cofactor 给原常数坐标目标。清三实际乘子的纯权分母后，仅将全部三乘子的共同多项式内容精除；重新乘回全部三个模块坐标，目标为 $(C,0,0)$。

因此所得 C 保持真实原 I6 来源，共同内容为零的全部纤维仍包含。只剥当前已经支付的纯权支持，保每个未付权因子与所有 lambda 首项零面。源不把 lambda 头或 N1 斜率加入单位表；任何泛域非零或 gcd 标志都不构成全 Phi 排空。

若实际新标量为零，只记该事实；若实际保留非恒定多项式，只记准确次数、SHA 与必要条件。只有完整原组合返回已付单位才可称当前 Phi 排空。首次之前不预告任何一种结果，不计算大纯权结式，不重跑旧错误模块或任何已冻结门。
