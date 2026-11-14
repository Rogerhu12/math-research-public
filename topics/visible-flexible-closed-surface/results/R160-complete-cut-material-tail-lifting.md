# R160 — 固定材料切口尾的完整函数 lifting 及全部变化

**状态：已证明，纯 helper 已在真实参数上通过非零方向检查。** 本文提供一个新的已知函数 lifting。它保留原物理度量和准确 cut II 迹，但改变有限表示的实际字段；不能称为 R158 那样的同函数角阶加密。它不包含新的 BVP 求解或闭曲面结论。

## 1. 用完整切口函数代替参考的角投影

设固定物理度量为 $ds^2+a_\delta(s)^2du^2$，cut 半径 $a_c=4/5$ 固定。atlas $u=U(s,\xi)$ 与参数 $\delta$、尾控制 $p$ 均无关。令 $L(s,\xi;p,\delta)$ 是现有完整 seed/tail/coast lifting，数组分量顺序为 $(n,m,l)$。

R132 的准确平尾在切口给
$$
k_c(u;p)=\kappa(a_c\sin u;p),\qquad
B(u)=(\cos^2u,-\sin u\cos u,\sin^2u).
$$
定义完整切口参考
$$V(s,\xi;p)=k_c(U(s,\xi);p)B(U(s,\xi)).\tag{1}$$
它在固定物理材料角 $u$ 下没有径向变化；计算角固定时仍有 $U_s$ 链式项。它不是 $\kappa(a(s)\sin u)B(u)$，也不是该函数的有限 Fourier 拟合。

取固定物理 $s$ 窗 $\chi(s)\in[0,1]$，在 seed/coast 窗附近恒零，切口附近恒一。新 lifting 是
$$L^*=(1-\chi)L+\chi V.\tag{2}$$
本次可消费窗为 $S_5((s-1.3)/(s_*-1.3))$，两端截断，$s_*=1.4759731783581287$ 为当前末正 trace 平台起点。这里没有把 $\chi$ 随 $\delta$ 或未知参数移动；若将来改变这种定义，必须另付其参数导数。

完整实际场先加 $L^*$，再应用已声明的 R153/R155 点态变换。特别在 $\chi=1$、raw correction 为零、R155 末窗也为一的区域，输入差场和混合项恰为
$$d=k_c\cos2u,\qquad m=-\tfrac12k_c\sin2u.$$
R155 输出因此**准确等于 R157 的 $S_T+bI$**，无须把平方根迹或尾部高角分量压入 $k=15$ 空间。这个结论只在所列参考条件成立时适用；非零 correction 仍是新的自由场，需要真正求解。

此 lifting 本身完全不使用 $K$ 或 $\max(K,0)$。R155 只在其合法保护区内使用真实目标 $K$；其它区域的实际 Gauss 缺陷必须保留。不能通过为参考取正部分而改变真实物理度量。

## 2. 尾参数的准确线性及完整角二 jet

设尾控制数为 $t$、Bernstein 次数 $d=t-1$，宽度 $W=a_c-c_0=23/50$，$c_0=17/50$。令
$$q=(|y|-c_0)/W,$$
并在 $0<q<1$ 定义
$$\beta_j(q)=630\binom dj q^{j+4}(1-q)^{d-j+4}.$$
则曲率及其参数基为
$$
\kappa(y;p)=\sum_jp_j\kappa_j(y),\qquad
\kappa_j=\beta_j/W,
$$
$$
(\kappa_j)_y=\operatorname{sgn}(y)\beta'_j/W^2,
\qquad(\kappa_j)_{yy}=\beta''_j/W^3.
\tag{3}
$$
区间外三者均为零。两端幂至少四阶，故这些所用值和导数在截断端连续；$y=0$ 在固定平直区内，不产生 $|y|$ 的求导奇异。

写 $y=a_c\sin u$，则
$$y_u=a_c\cos u,\quad y_{uu}=-a_c\sin u,$$
$$k_u=\kappa_y y_u,\quad k_{uu}=\kappa_{yy}y_u^2+\kappa_y y_{uu}.$$
分量向量的完整导数是
$$
B_u=(-2\sin u\cos u,\sin^2u-\cos^2u,2\sin u\cos u),
$$
$$B_{uu}=(-2\cos2u,2\sin2u,2\cos2u).$$
因此
$$V_u=k_uB+kB_u,\qquad V_{uu}=k_{uu}B+2k_uB_u+kB_{uu}.\tag{4}$$
把 $\kappa,\kappa_y,\kappa_{yy}$ 换成 (3) 中每一列，便得到全部尾参数列的相同公式，没有有限差分，也不随 raw/central Fourier 阶数改变尾度数。

计算角完整链式法则为
$$
V_s=U_sV_u,\quad V_\xi=U_\xi V_u,\quad
V_{\xi\xi}=U_\xi^2V_{uu}+U_{\xi\xi}V_u,
\tag{5}
$$
$$V_{s\xi}=U_sU_\xi V_{uu}+U_{s\xi}V_u.\tag{6}$$
相同式逐列适用于尾参数。由于 $a_c,U$ 固定，$D_\delta V$ 及其这些 jet 准确为零；不存在把 $a_\delta(s)$ 误放进切口曲率再漏掉链式项的步骤。若 atlas 分片，(5)–(6) 按真实片和所声明的单侧径向 jet 使用，值与角 trace 按 R141 接合。

## 3. 完整新 lifting jet

逐项微分 (2) 得
$$
\begin{aligned}
L^*_s&=(1-\chi)L_s+\chi V_s+\chi_s(V-L),\\
L^*_\xi&=(1-\chi)L_\xi+\chi V_\xi,\\
L^*_{\xi\xi}&=(1-\chi)L_{\xi\xi}+\chi V_{\xi\xi},\\
L^*_{s\xi}&=(1-\chi)L_{s\xi}+\chi V_{s\xi}
                +\chi_s(V_\xi-L_\xi).
\end{aligned}
\tag{7}
$$
这里 $s$ 是实际物理径向坐标，不使用旧 coast clock 的近似节点质量。

设 $P=D_pL$ 为旧尾参数包，$V_p$ 由第 2 节给出。新包满足
$$
P^*=(1-\chi)P+\chi V_p,
$$
$$P^*_s=(1-\chi)P_s+\chi(V_p)_s+\chi_s(V_p-P),$$
$$P^*_\xi=(1-\chi)P_\xi+\chi(V_p)_\xi,$$
二阶角和混合式同 (7)。全域 lifting 对尾参数是仿射的，尾的可变部分严格线性；在本次真正改变的 late 区 seed/coast 项均已消失，故该区域本身就是尾参数的线性函数。

对于物理参数包 $Q=D_\delta L$，完整变化更简单：
$$
Q^*=(1-\chi)Q,\qquad
Q^*_s=(1-\chi)Q_s-\chi_sQ,\qquad
Q^*_\xi=(1-\chi)Q_\xi.
\tag{8}
$$
角二阶为 $(1-\chi)Q_{\xi\xi}$，混合为
$(1-\chi)Q_{s\xi}-\chi_sQ_\xi$。特别是 (8) 的 $-\chi_sQ$ 不能省略。矩阵列数采用实际尾数 $t$ 和 bump 数 $J$，与 R158 的独立尾布局相容。

## 4. 真正 cut 迹与未被保存的径向 II 导数

在准确 cut，旧 lifting 已是准确尾，故
$$L(s_c,\xi)=V(s_c,\xi).$$
由于是完整角函数恒等，其全部已有角 jet 也相等。尾参数列相等；当前 bump 的值及有关 jets 在保护 collar 恒零，故切口物理参数列也相等并为零。于是 (2) 准确保留这些 cut 迹。若原 cut raw correction 恒零，新表示仍可保留这个准确条件。

然而一般 $V_s\ne L_s$。原 lifting 含 $\kappa(a(s)\sin u)$ 的真实半径导数，新切口参考在固定材料 $u$ 下恒定。因此本文**不**宣称径向 II 导数在 cut 处保持，也不宣称由此得到全局 $C^3$。曲面 $C^2$ 接合所用 II 值并未增加这种导数条件；实际位置、标架、第一及第二 jet 的接合仍按 R124/R129 的真实重建支付。改变前缀场后，位置或标架更不会因 II 边界值相同就自动满足尾部刚体匹配。

## 5. 完整右端及参数 Jacobian 必须重算

记
$$I=1/(aU_\xi),\qquad A=U_s/U_\xi,\qquad c=a_s/a.$$
对任意完整 lifting $L=(L_n,L_m,L_l)$，raw correction 方程的真实 forcing 是
$$
\mathcal F_n=I(L_m)_\xi+c(L_l-L_n)+A(L_n)_\xi-(L_n)_s,
$$
$$
\mathcal F_m=I(L_l)_\xi-2cL_m+A(L_m)_\xi-(L_m)_s.
\tag{9}
$$
新 forcing 必须将 (7) 的 $L^*$ 整体代入 (9)。旧 forcing、旧端点差或旧缓存不能被原样沿用。新 known lifting 的 raw 参数列是 (9) 对新 $P^*$ 的同一线性算子，因为 $I,A,c$ 不依赖尾参数。

物理 $\delta$ 的完整列还包含
$$D_\delta I=-I\,D_\delta a/a,\qquad D_\delta c,$$
并有
$$
\begin{aligned}
D\mathcal F_n={}&(DI)(L_m^*)_\xi+I(Q_m^*)_\xi
 +(Dc)(L_l^*-L_n^*)+c(Q_l^*-Q_n^*)\\
&+A(Q_n^*)_\xi-(Q_n^*)_s,\\
D\mathcal F_m={}&(DI)(L_l^*)_\xi+I(Q_l^*)_\xi
 -2(Dc)L_m^*-2cQ_m^*+A(Q_m^*)_\xi-(Q_m^*)_s.
\end{aligned}
\tag{10}
$$
当前 atlas 固定，所以 $DA=0$；这不是在其它可变 atlas 中省略它的许可。

若实际径向离散采用完整 lifting 的准确端点差，端点也必须使用 $L^*$。R152 的既有线性 known-lifting 积分只能在仍相同的区间原样复用，不能把旧 tail 或旧非线性贡献假定为新贡献。后续 R155 的 $E$ 也必须从“raw 加新完整 lifting”重新计算，并保留其实际端点和所有参数变化。

## 6. 和角阶加密的关系

固定 raw 系数时，(2) 一般改变完整场；本次真实小核观测到 lifting 值改变约 $.1896$。所以它是明示的新表示和初猜选择，不能标为同场细化。

一旦两次角空间使用同一个新定义 (2)、同一个 $\chi$、尾控制数和参数值，则 R158 的准确零填充证明仍逐项成立：完整新 lifting 不变，只增加 raw/central 自由度。此时才能谈同函数的角阶嵌套。本文纯 helper 不自行改旧 provider 或生成新的求解状态。

## 7. 可调用实现

`scripts/fd2d_gc_cut_material_tail_lifting.py`，SHA256
`93c13091f2a398188046e35a21983200255e1f852018fe89263a7907962436e2`。

- `cut_material_tail_packet(tail,coords,cut_radius=.8)` 返回完整 $V$ 的值、$s/\xi/\xi\xi$ jet、可用时的混合 jet，以及全部尾参数列；它使用准确 R132 正 Bernstein 家族。
- `blend_cut_material_lifting(old,cut,chi,chi_s,operators=...,project_even=...,project_odd=...)` 实现 (7)–(10) 所需的新值、tail/profile jet，并从新字段重算 full forcing；给出原有限 projectors 时再产生对应的 retained forcing。
- 不给真实 operators 时，helper 删除旧 forcing 项，防止调用者误把旧右端当新右端。

这里返回定义包中的 `nonlinear_trace_reapplied_to_complete_field` 是**后续消费约定**：实际 solver 必须在完整新 lifting 后应用原 R155 规则。纯 helper 自身只返回新 lifting，不执行整个非线性场变换或求解。未来 representation/schema 必须显式登记这个新定义及固定窗口，不能只换旧文件的名字。

## 8. 真实非零方向消费

检查输入为
`notes/2026-11-12-fd2d-positive-trace-tailwarm01-warm.npz`，SHA256
`d671d84b4442547045b4072fde277a961bc42720e6dca07125bfa317cff0ce5b`。
candidate 和度量仍为 R155/R157 的当前实体。只消费其 16 个真实尾控制、7 个真实物理参数、原 atlas 与完整 lifting；没有修改原文件、求 BVP 或改变当前活动源。

在 8 个物理位置、64 个共同角上，包含 $U_s\ne0$ 的实际 atlas 返回区、$\chi=0$ 区和准确 cut，检查了非零尾方向和非零物理方向。全部值、$s/\xi$ jet、完整 forcing 的中心差分与解析 JVP 一致：尾最大绝对误差 $1.287\times10^{-10}$，物理方向最大 $8.626\times10^{-10}$。这些方向的解析量均非零，没有以零方向冒作 JVP 检查。

完整切口角二 jet 另由实际 $U$ 链式求值检查，误差 $2.629\times10^{-7}$。cut 值、角 jet 的有限算术差分别不超过 $1.111\times10^{-16}$、$1.333\times10^{-15}$，尾/物理参数的所用切口迹差为零；这些舍入读数与第 4 节准确函数恒等分开。cut 径向 II lifting 确实改变约 $3.66924$，如实保留，未伪称该导数也接合。$\chi=0$ 区值差为零。

唯一该次执行 session **30501**，初始 chunk **7fdf9f**，完成 chunk **ac6d85**，自然 exit **0**，耗时 **1.546853701 s**，RSS 峰 **82152 KiB**。报告为
`notes/2026-11-12-fd2d-cut-material-tail-lifting-check-01-report.json`，SHA256
`7601503679ff6f0030402df7c5ca1dec7b5637594559d3b85958a4cb014b2174`。
这组有限实现检查只支持公式消费正确；连续相容性、完整几何和本题强标准继续保持未完成状态。
