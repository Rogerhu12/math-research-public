# R21：$\mu=4\sqrt2$ 未变形主干的全域整数区间几何证书

2026-11-10，geometry-transfer。

**状态：已证明；主课题的中间结论。** 本文处理
[R20](R20-scaled-fourfold-spectral-family.md) 中 $\mu=4\sqrt2$ 的
未变形旋转主干。有限区间使用只含整数和有向 dyadic 舍入的 ODE 包含，
无穷尾使用解析比较。既不是浮点 ODE，也不是网格点曲率扫描。
没有把 $\mu=\sqrt2$ 的 R14 几何数值转授到这里。

## 1. 对象、结果与复现

令
$$
\mu=4\sqrt2,\qquad A=32+\sqrt2,\qquad
Q(x)=32-A\operatorname{sech}^2x,
$$
$$
h''=Qh,\qquad h(0)=1,\quad h'(0)=0,\qquad
z'=\frac1{h^2},\quad z(0)=0,
$$
$$
X(x,\theta)=h(x)^{-1}e_r(\theta)+z(x)e_z.
\tag{1.1}
$$
两端补点后为闭 $C^2$ 嵌入球面。其全域几何界为
$$
\boxed{
\sup|X|<\frac{23}{20},\qquad
D<\frac{23}{10},\qquad
\max_i|\kappa_i|<4,\qquad
\inf X\cdot n>\frac45,\qquad G<4,
}
\tag{1.2}
$$
其中 $G$ 为 Gauss 曲率。由全局法向管，
$$
\boxed{
\operatorname{reach}(X)>\frac14,\qquad
\frac{\operatorname{reach}(X)}D>\frac5{46}>\frac3{100}.}
\tag{1.3}
$$

复现命令（仓库根）：

~~~bash
python topics/visible-flex-exact-nearby/scripts/mu4_background_interval.py
~~~

[脚本](../scripts/mu4_background_interval.py) 已实际执行成功；
[整数区间证书 JSON](../notes/2026-11-10-mu4-background-interval-certificate.json)
保存全部全区间极值包络及末端有理门。
默认将 $[0,3/2]$ 分成 600 个长度 $1/400$ 的完整小区间。
程序的每个验证判断都是整数交叉相乘，不读显示用小数作决策。
本次运行不足一秒完成；不依赖 SciPy、NumPy 或区间数学外部包。

## 2. 有向算术与初等函数包络

统一固定分母
$$S=2^{160}.$$
区间端点表示为整数除以 $S$。加减使用整数端点；
乘法检查四个端点乘积后，分别向下、向上整除 $S$。
平方在包含零时准确取下界零。正区间求倒数使用
$S^2/b,\ S^2/a$ 的整数向外舍入。
$\sqrt{[a/S,b/S]}$ 的端点由
$\operatorname{isqrt}(aS),\operatorname{isqrt}(bS)$ 给出，
上端若非平方数再加一。因此 $\sqrt2$ 也具有直接整数包络。
这些规则均包含实际实数运算结果。

程序只需 $e^t$ 于 $0\le t\le3$，代码额外允许 $t\le4$。
用正项 Taylor 和
$$
P_{64}(t)=\sum_{k=0}^{64}\frac{t^k}{k!}
$$
及准确余项界
$$
0\le e^t-P_{64}(t)
\le\frac{t^{65}/65!}{1-t/66}.
\tag{2.1}
$$
这是因为尾项从第 65 项起，相邻项比至多为 $t/66<1$。
所有和、积、除法按上面的区间规则计算，余项下端取零。
因此没有调用只保证最近舍入的浮点指数函数。

随后用
$$
\operatorname{sech}^2x=\frac{4e^{2x}}{(e^{2x}+1)^2},\qquad
\tanh x=\frac{e^{2x}-1}{e^{2x}+1},
$$
$$
Q'=2A\operatorname{sech}^2x\tanh x
\tag{2.2}
$$
生成 $Q,Q'$ 包络。$Q$ 在正半轴严格增加，
$\operatorname{sech}^2x$ 递减、$\tanh x$ 递增；
每一小区间的范围取相应端点包络，再按 (2.2) 相乘。
这包含整个小区间，不只包含两个端点。

## 3. 一步 ODE 包含为何覆盖连续解

记 $v=h'$，小区间长度为 $\Delta$。假定左端已有真值包络
$H_i,V_i,Z_i$，并令 $Q_i$ 包含该小区间的势。
取
$$
H_c=\sup_{H_i}|h|,\quad V_c=\sup_{V_i}|v|,\quad
Q_c=\sup_{Q_i}|Q|.
$$
由积分方程，整个小区间上的真实绝对上界满足
$$
\sup|h|\le H_c+\Delta\sup|v|,
\qquad
\sup|v|\le V_c+\Delta Q_c\sup|h|.
$$
因 $\Delta^2Q_c<1$，
$$
M_h=\frac{H_c+\Delta V_c}{1-\Delta^2Q_c},\qquad
M_v=V_c+\Delta Q_cM_h
\tag{3.1}
$$
是有效上界。线性 $h,v$ 系统先验在有限区间存在，故这里的上确界
有限，不需要从未经证明的数值轨迹推出存在性。

初始连续包络可以取
$$
H=H_i+[0,\Delta][-M_v,M_v],\qquad
V=V_i+[0,\Delta][-Q_cM_h,Q_cM_h].
$$
程序再反复四次与积分包络
$$
H_i+[0,\Delta]V,\qquad V_i+[0,\Delta]Q_iH
\tag{3.2}
$$
求交。每次求交仍包含真实解。
每个实际小区间均检查 $H$ 的下端严格为正，所以 $z$ 方程合法，
并有
$$Z=Z_i+[0,\Delta]H^{-2}$$
作为连续高度包络。

记 $Q_{i,0}$ 为左端势包络，$Q_i'$ 为全小区间导数包络。由
$$
h'''=Q'h+Qv,\qquad v''=Q'h+Qv,\qquad z''=-2v/h^3,
$$
下一左端的严格 Taylor 包含为
$$
H_{i+1}\subseteq
H_i+\Delta V_i+\frac{\Delta^2}{2}Q_{i,0}H_i
+\frac{\Delta^3}{6}(Q_i'H+Q_iV),
\tag{3.3}
$$
$$
V_{i+1}\subseteq
V_i+\Delta Q_{i,0}H_i+\frac{\Delta^2}{2}(Q_i'H+Q_iV),
\tag{3.4}
$$
$$
Z_{i+1}\subseteq
Z_i+\Delta H_i^{-2}-\Delta^2V/H^3.
\tag{3.5}
$$
这里右端表示用于下一步的区间，左端表示实际解的真值。
余项是整个小区间的积分余项，不是在某个猜测轨迹上求导。
从准确初值 $(1,0,0)$ 归纳，所有 600 个连续包络都合法。

## 4. 有限区间的实际几何断言

对每个第 3 节所得全小区间包络，令
$$p=\sqrt{1+v^2}.$$
程序用区间运算计算准确几何表达式
$$
|X|^2=h^{-2}+z^2,\qquad
\kappa_\theta=h/p,\qquad
\kappa_s=Q(h/p)^3,
$$
$$
G=Q(h/p)^4,\qquad
X\cdot n=\frac{h^{-1}+zv}{p}.
\tag{4.1}
$$
对整个包络分别验证
$$
|X|^2<\frac{529}{400},\quad
|\kappa_\theta|<4,\quad|\kappa_s|<4,\quad
G<4,\quad X\cdot n>\frac45.
\tag{4.2}
$$
下表仅将证书内的准确 dyadic 分数显示为小数，
不把这些小数当成额外证明输入：

| 全部小区间包络量 | 证书端点的小数显示 |
|---|---:|
| $|X|^2$ 上端最大 | 1.3136868956711547 |
| $\kappa_\theta$ 上端最大 | 1.0000000000000000 |
| $|\kappa_s|$ 上端最大 | 3.841752590658432 |
| 支撑下端最小 | 0.8040625671764027 |
| $G$ 上端最大 | 3.4668298519687926 |
| $h$ 下端最小 | 0.9533848361005285 |

例如第一行的准确分数为
$$
\frac{1919955548963543572930531826462650558304629506693}
 {1461501637330902918203684832716283019655932542976}
<\frac{529}{400}.
$$
其余全部整数端点同样写入 JSON，并由脚本逐小区间直接比较。
所以 (4.2) 是 $[0,3/2]$ 上的连续区间结论。

在 $B=3/2$，程序另行准确验证
$$
h(B)>26,\qquad \frac{v(B)}{h(B)}>\frac{24}{5},\qquad
\frac{81}{100}<z(B)<\frac{33}{40},\qquad Q(B)>25.
\tag{4.3}
$$
下节只使用这些宽的有理门，不依赖末端更多小数位。

## 5. 无穷尾的解析延拓和全部几何界

$Q$ 单调增加且小于 $32$，故 $Q\ge25$ 于 $x\ge B$。
由 (4.3)，$h,v$ 均为正；$h''=Qh>0$ 使它们一直为正。
令 $\omega=v/h$，则
$$\omega'=Q-\omega^2.$$
在 $\omega=24/5$ 处，右端至少为
$$25-(24/5)^2=49/25>0.$$
首次交叉论证给
$$
\omega>\frac{24}{5},\qquad
h(x)>26e^{(24/5)(x-B)}\qquad(x\ge B).
\tag{5.1}
$$
因此
$$
z_\infty-z(B)
<\frac{5}{48\cdot26^2},\qquad
z_\infty<\frac{33}{40}+\frac5{32448}<\frac56.
\tag{5.2}
$$
令 $a=1/h$。由 $a<1/26$，无穷尾上的半径平方满足
$$
|X|^2=a^2+z^2<
\frac1{676}+\frac{25}{36}<\frac{529}{400}.
\tag{5.3}
$$
准确主曲率和 Gauss 公式也可写为
$$
\kappa_\theta=\frac1{\sqrt{a^2+\omega^2}},\qquad
\kappa_s=\frac{Q}{(a^2+\omega^2)^{3/2}},\qquad
G=\frac{Q}{(a^2+\omega^2)^2}.
$$
于是
$$
\kappa_\theta<\frac5{24},\qquad
|\kappa_s|<32(5/24)^3=\frac{125}{432}<4,\qquad
G<32(5/24)^4<4.
\tag{5.4}
$$
支撑满足
$$
X\cdot n=
\frac{a^2+z\omega}{\sqrt{a^2+\omega^2}}
\ge\frac{z}{\sqrt{1+(a/\omega)^2}}
>
\frac{81/100}{\sqrt{1+(5/624)^2}}.
$$
分母严格小于 $101/100$，故
$$X\cdot n>\frac{81}{101}>\frac45. \tag{5.5}$$
偶性给另一端相同的界。因此 (4.2) 与 (5.3)—(5.5) 联合覆盖全实轴。

## 6. 真正两极、嵌入、直径及 reach

由于 $h$ 处处为正，$h$ 为偶函数、$z$ 为奇函数。
在整个正半轴 $\omega<\mu$：若从初值零首次向上碰到 $\mu$，
则 $\omega'=Q-\mu^2<0$，矛盾。结合 $Q\to\mu^2$ 和 (5.1)，
常系数 Riccati 比较给
$$\omega\longrightarrow\mu,\qquad Q\longrightarrow\mu^2.$$
两个极点的高度有限，且经线弧长积分收敛。
在正端以 $a=1/h$ 为径向图坐标，
$$
z_a=-1/v,\qquad
z_a/a=-1/\omega\longrightarrow-1/\mu,\qquad
z_{aa}=-Q/\omega^3\longrightarrow-1/\mu.
$$
因此补点是正则 $C^2$ 旋转图，Cartesian Hessian 连续趋向
$-I/\mu$。负端同理。内部 $z$ 严格增加，每个高度恰有一个圆，
故闭面嵌入。

由全域半径界得 $\sup|X|<23/20$。
更准确地，$X(-x,\theta+\pi)=-X(x,\theta)$，
所以这张完整未标记闭面中心对称；
[R18 §8](R18-waist-normal-hausdorff-witness.md) 的恒等式给
$$D=2\sup|X|<23/10.$$

最后使用 [R14 §7](R14-mode-four-full-tail-geometric-bounds.md)
的通用正支撑法向偏移论证：
正支撑及 $|t|<\min(\sigma,1/K)$ 使所有偏移面的径向投影为
全局微分同胚，且沿每条径向射线随 $t$ 严格嵌套，故全局法向管单射。
这里 $\sigma>4/5$、$K<4$，因此 reach 严格大于 $1/4$，
进而得 (1.3)。这一步付的是全局双点控制，不是从局部曲率
自动推断 reach。

## 7. 使用范围

本证书是新的 $\mu=4\sqrt2$ 未变形背景基线。
它明确给出 $D<2.3$、正 Gauss 曲率低于 $4$ 和充分的 reach 余量，
可供后续点值、法向及曲率误差转移使用。
R16 的有限幅校正、实际尾部与双 bump 在新 $\mu$ 下的重新定量、
公共精确度量和可见幅度尚须由同一个实际构造继续支付。
本文没有把该基线直接当作任意有限幅候选的证书。
