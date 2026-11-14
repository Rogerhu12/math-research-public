# 原 R48 到新 carrier：同一正测度的五基重包与双端高度差

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）。
日期：2026-11-13。
状态：完整应用引理与本地读取接口。下面没有报告新的数值执行；原 PM、PA、正 A、CF、完整 mean/frame 的已有正式结果不重跑。

本说明接 [R48](../results/R48-weighted-compatible-outer-interpolation.md)、[R99](../results/R99-complete-mean-field-to-physical-jet-bridge.md) 与 [R103](../results/R103-reflection-centred-position-and-defect-bridge.md)。对象固定为 cell $0$、segment $7$、part $0$。旧候选是在原 source 坐标 $x\in[0,1/8]$ 上定义的四次归一斜率；新 carrier 在同一真实背景的物理 $r$ 上定义。两者的原非均值端点两 jet 相同，内部函数不同。

## 1. 不把两种局部坐标混为一谈

旧候选使用 $u=8x$，新物理候选使用自己的 $u_r=(r-r_L)/(r_R-r_L)$。这里始终给旧基函数输入 $u=8x$。取旧五个非负基函数

$$
q_{00}=1-3u^2+2u^3,\quad
q_{10}=u-2u^2+u^3,\quad
q_{01}=3u^2-2u^3,\quad
q_{11}^+=u^2-u^3,\quad
b=u^2-2u^3+u^4.
$$

共同的真实正测度为

$$
d\mu=w(r)\,dr=r_x(x)w(x)\,dx.
$$

现有新 $111$ 叶的五真积分已经付了

$$
\omega_i^- \le \int_{I_i}w\,dr\le\omega_i^+,
\qquad
\omega_i=I_{00}^{(r)}+I_{01}^{(r)}.
$$

虽然右边两个新基函数采用 $u_r$，它们的和严格为 $1$，所以这个完整质量恰是同一个 $d\mu$，不需要把 $u_r$ 当成 $u$。

对任一旧非负基函数 $q$，以精确多项式 Bernstein 包围或准确极值给
$q_i^-\le q(8x)\le q_i^+$，其中 $x\in I_i$。则

$$
\boxed{
q_i^-\omega_i^-\le\int_{I_i}q(8x)\,d\mu
\le q_i^+\omega_i^+.
}
\tag{B.1}
$$

这不是新积分，而是已付正测度上的正函数包络。五个总积分、任一完整叶前缀及后缀均可直接相加。每个所得区间还可与同一旧总矩和旧八 bin 的对应区间相交；只有同一个数学积分才可相交。

在一个新叶内部，五个前缀因 integrand 非负而单调，其包络可取“叶左端前缀下界、叶右端前缀上界”，后缀反向处理。若一个旧 bin 被该位置切开，未知部分只能取 $[0,I_{\rm bin}^+]$；不能将整个旧 bin 的质量按长度比例任意分配。

## 2. 同一个旧四次候选的重包

以 $H_L,H_R$ 和两端物理 $H_r,H_{rr}$ 为固定原数据。取 $h_x=1/8$，定义

$$
K_L=\frac{H_{r,L}}{w_L},\qquad
D_L=h_xr_{x,L}
\left(\frac{H_{rr,L}}{w_L}
-\frac{w_{r,L}H_{r,L}}{w_L^2}\right),
$$

右端同理。$D_L,D_R$ 是对旧 $u$ 的导数，不能用新物理 $u_r$ 的导数替代。真实 $r_x$ 只作正的同背景包围。

旧候选的真实系数是

$$
\lambda=
\frac{H_R-H_L-K_LI_{00}-D_LI_{10}-K_RI_{01}+D_RI_{11}}
{I_b}.
\tag{B.2}
$$

对 (B.1) 的改进总矩使用区间算术，再与原已存的 $\lambda$ 区间相交，仍围住同一个由真积分定义的 $\lambda$。不得以新盒中点重新选系数。$I_b$ 的严格正下界必须保留。

旧归一斜率的幂系数是

$$
\begin{aligned}
a_0&=K_L,&a_1&=D_L,\\
a_2&=-3K_L-2D_L+3K_R-D_R+\lambda,\\
a_3&=2K_L+D_L-2K_R+D_R-2\lambda,&a_4&=\lambda.
\end{aligned}
\tag{B.3}
$$

在每个完整新叶上，用精确仿射变换后的 Bernstein 系数包围
$K_{\rm old}(u)=\sum a_ju^j$ 及其导数，最后作真实转换

$$
(K_{\rm old})_r=\frac{8}{r_x}\frac{dK_{\rm old}}{du}.
\tag{B.4}
$$

旧高度同时由左右两端表示：

$$
\begin{aligned}
H_{\rm old}
&=H_L+K_LI_{00}^{\rm pre}+D_LI_{10}^{\rm pre}
 +K_RI_{01}^{\rm pre}-D_RI_{11}^{\rm pre}+\lambda I_b^{\rm pre},\\
H_{\rm old}
&=H_R-K_LI_{00}^{\rm post}-D_LI_{10}^{\rm post}
 -K_RI_{01}^{\rm post}+D_RI_{11}^{\rm post}-\lambda I_b^{\rm post}.
\end{aligned}
\tag{B.5}
$$

两盒相交只收紧同一个旧高度。式 (B.3)–(B.5) 的导数始终来自旧候选自身，不以 Darboux 输出替换。

实际旧 generator 保存的内部 node $1$ 有独立 $r_x$ 盒；外 node $0$ 复用了原共享物理 jet，未保存 $r_x$ 字段。本地消费者必须从同源、包含真实端点的旧/新叶包围取交，或者使用另一个已付的真实端点包围；不能因为字段缺失而补一个浮点值。这样的包围若宽，就在输出中保留宽度。

## 3. 用两端高度差为零保留关联

令 $\Delta H_m=H_{{\rm CF},m}-H_{{\rm old},m}$，
$\Delta K_m=K_{{\rm CF},m}-K_{{\rm old},m}$。CF 的冻结生产源直接使用旧节点表；旧 candidate 与 CF 摘要里的全部节点必须逐项一致，因此

$$
\Delta H_m(r_L)=\Delta H_m(r_R)=0,\qquad
(\Delta H_m)_r=w\Delta K_m.
\tag{B.6}
$$

这里两端相等来自固定数据和构造身份，不是因为两个区间发生重叠。

设每个新叶已包围 $|\Delta K_m|\le k_{im}$。对整叶 $I_i$ 上任意点，(B.6) 给

$$
\boxed{
|\Delta H_m|
\le
\min\left\{
\sum_{j\le i}\omega_j^+k_{jm},
\sum_{j\ge i}\omega_j^+k_{jm},
h_{im}^{\rm direct}
\right\}.
}
\tag{B.7}
$$

$h_{im}^{\rm direct}$ 是 (B.5) 与新 CF 保存高度的直接差盒。两个前后缀故意都包含完整当前叶，以覆盖其全部连续位置；不是只在叶端点成立。三个量围住同一个 $\Delta H_m$，可以取最小值。

这是避免把两个近似相同的大高度区间独立相减后丢失关联的具体接口。它不要求 $\Delta K_m$ 同号，也不以数值样点代替 sup。

## 4. 完整均值及物理五 jet

对每个新叶，旧 $37$ 叶记录中所有相交旧叶都要覆盖其全部位置。取它们的完整 $|c_{\rm old}|$、$|c_{{\rm old},x}|/r_{x,-}$ 最大值和实 $A,D,L$ 的最小值。转换是物理 $c_r$，不能把旧 $c_x$ 原值与 CF 的物理导数相加。

新侧直接用同叶 CF 的实际完整根及物理导数。以 (B.7) 和 $\Delta K$ 形成 R99 的
$(e_K,e_P,e_T)$，可用其完整实线根差界得到 $\delta c_*$，并与
$|c_{\rm old}|+|c_{\rm CF}|$ 取小。实线 $A,D$ 的凹性和 $L$ 的仿射性保留；不要求线段上的每个状态也是均值根。

完整均值高度差只积分一次：

$$
\Delta h_0(r)=\Delta h_0(r_L)+\int_{r_L}^r w\Delta c\,dr.
\tag{B.8}
$$

每叶可用同一个 $\omega_i^+\delta c_{*,i}$，并与已有完整 mean-v4 对旧 R48→CF 的合法前缀界相交。禁止在不同子段重置均值常数。

记 $e_H^{(j)}=\sum_m m^j|\Delta H_m|$，
$e_K^{(j)}=\sum_m m^j|\Delta K_m|$，
$e_{K_r}=\sum_m|\Delta(K_m)_r|$。完整物理差满足

$$
\begin{aligned}
|\Delta h|&\le|\Delta h_0|+e_H^{(0)},&
|\Delta h_\theta|&\le e_H^{(1)},\\
|\Delta h_{\theta\theta}|&\le e_H^{(2)},&
|\Delta h_r|&\le w_+(\delta c_*+e_K^{(0)}),\\
|\Delta h_{r\theta}|&\le w_+e_K^{(1)},&
|\Delta h_{rr}|&\le |w_r|_+(\delta c_*+e_K^{(0)})
 +w_+(\delta c_{r,*}+e_{K_r}).
\end{aligned}
\tag{B.9}
$$

$\delta c_{r,*}$ 至少可取两侧完整真实物理根导数绝对值之和。更紧时调用已冻结的双根径向差公式，保留全部 $G_z$ 项；不能免费把 $\delta c_r$ 设为零。新 CF 里已经保存自己的 $K_r$，旧侧由 (B.4) 得到，所以 (B.9) 不包含任何 PDE 二阶替换。

## 5. 空间参考桥与真解桥的分开使用

(B.9) 支付旧 R48→新 CF 的实际同位置高度导数差。用它们的完整 $p,q,q_\theta$ 和实域，R103 给逐圈居中的位置与单位参考向量差；两侧此时都只是兼容候选参考。

若后续证明某真实同 $g$ 解与新混合参考的完整误差 $\le1/512$，再加 R103 已付的该部分条件界。候选差与真解误差是两项，不能任选较小的一项。

若几何审计用的是径向优先坐标，还须加 R103 的原候选完整 $J$ 中心漂移。本地消费者可在同 $111$ 叶上，用旧 $37$ 叶给出的完整 $J_x$ 包围与新 CF 的物理 $J_r$ 分别付漂移；两种 $r_x$ 比例不得混淆。既有 complete mean-v4 与两端高度相等不自动证明这个平面中心漂移为零。

### 5.1 改造区间之外只保留一次刚体平移

本次只替换 part $0$。在其右侧，两个候选的非均值高度及全部导数重新相同；完整 mean 根 $c$ 也相同。因此两个完整高度只差一个竖直常数。它们的 $a,b,c_{\rm frame},\Gamma,G$ 完全相同，而且反射轴使轴角在径向恒定。于是两种径向优先平面参考在剩余七段只差一个固定平移，单位参考向量相同。

所以，原 R48→CF 的空间差只需在改造区间上算一次；末端平移继续通过其余未改造段，无须给这些段重复累积候选差。这里说的是两个候选之间的差，不是把单个候选自己的非零 $J$ 中心漂移在其余段删掉。

可以选共同左端位置，也可以选共同右端位置，但必须选一个全局规范。右端对齐时，(B.8) 改用从右端的完整 mean 积分，R103 的中心漂移亦用后缀；这样全部右侧未改造参考几何准确重合。左、右两种预算可以分别报告各自的全域最大值，不能逐点取较小值后假装仍是同一个全局规范。

旧 R95 的基准与新 carrier 的内部二阶差可能超过其简单均匀门。因此已另外对新 carrier 自己的实际两 jet 付条件曲率预算；空间桥无需强迫旧 R95 的单一小误差门承担所有任务。仍未支付真实外解、全时族及整闭面远点对。

## 6. 本地输入与执行约束

主要冻结输入：

| 对象 | SHA256 |
|---|---|
| 原八段 candidate | 7da554bdb467fe2b997a01971dd4917003fd5deeb36978e200e1457ea3c8fddf |
| 原 seg7 完整摘要 | 806fdb96b9aa6eafd921c07518a5b52218180d2182f7b8d18abb8e3d695638e4 |
| 原 seg7 正式 resource | 912ad6200027fdb445cd3e8636c1f6cd404a3480d2c013b6c4722e6888016820 |
| 新 CF 完整摘要 | 0ac4b1e14ec34a86035add63e6250660924537c54acc834e497c6ebdd396ae12 |
| 新 CF 全字段 primary | d07456782cfd2cd292cbb77fbbf437617a82ab6039f774fc5637c74a2e486dbe |
| mean-v4 摘要 | a178bc76d676eaa3aa6e0e1f57592dceea27bc996017503097a1fd01f8bde1f2 |
| mean-v4 全 primary | 6b6748eab26c02b1960b367acc22f3a80760d6d40c20aa998ddaa3c4193d0e71 |

原 $37$ 叶 primary 的完整 SHA 必须从已固定原摘要的 part $0$ 条目读取；本文不补猜其哈希。两种完整原 resource 必须真实 exit $0$，所有输入先本地核 SHA。原 candidate、所有 gzip primary 仅由恢复的真实终端读取；不得从 GitHub 工具拿编码数据或分块恢复。

本应用仅重用已付原件与正积分，不重跑 PM/PA/A/CF，不修改任何既有数学源、MJS、候选端点或原 manifest。若原件仍在，先完整归档；若确实缺失，按正式执行参数只重做缺失阶段。环境暂不可读不是文件丢失的证据。
