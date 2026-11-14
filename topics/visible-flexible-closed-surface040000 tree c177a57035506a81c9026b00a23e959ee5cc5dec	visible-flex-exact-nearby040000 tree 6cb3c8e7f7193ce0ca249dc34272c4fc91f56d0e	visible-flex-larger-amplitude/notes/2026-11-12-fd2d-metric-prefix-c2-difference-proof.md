# 实际 Hermite 前缀的连续差分与旧诱导度量下的 C² 范数

2026-11-12，Astra-visible-flex-fd2d / metric_closure。

**状态：下述差分包围与范数转换的证明完整；已完成的数值应用严格限于 M12 base → M14 base 的完整有限前缀。**
M14 不是新的成功候选：R81、R83、R109 已给它原容差以上的真实度量下界。
本文不把它重新登记成可行图，不把 base 的参考几何换成 R21 的 common 闭图，
也不把前缀结果当成尾、帽或全相位闭曲面的完成证明。

本笔记为 R110 所需的实际差分 consumer 提供计算依据。
它计算的是已经保存的两幅 Cartesian 曲面之差，不使用 BVP 残差代替几何差，
不启动 ODE、不改变保存图、不改变固定目标度量。

## 1. 定义输入与严格的同点比较

每份有限前缀有正的原生径向长度 $S_i$、严格递增的二进制节点
$s_{i,0}=0<\cdots<s_{i,N_i}=S_i$，以及三重对称的柱坐标 Fourier 展开。
每个保存的二进制数在这里都是对应的**精确有理数**。
曲面在相邻节点间为共享值、一阶导、二阶导的五次 Hermite 多项式。
平均高度的节点值按保存的精确二进制增量累加；显示用的累加高度不定义曲面。

比较采用一个明确的参数面：

$$
x\in[0,1],\qquad \psi\in\mathbb R/(2\pi\mathbb Z),
$$
$$
X(x,\psi)=X_{\rm ref}(S_{\rm ref}x,\psi),\qquad
Y(x,\psi)=X_{\rm new}(S_{\rm new}x,\psi),\qquad u=Y-X.
\tag{1}
$$

因此后文的 $u_x$ 是对归一变量 $x$ 求导，不能把它未经尺度转换写成 $u_s$。
如果两个实际图的 Fourier 模数不同，先在同一完整三重基底上补零，再相减。
没有把不同模式截断成同一低阶模型。

程序使用双方所有节点 $s_{i,j}/S_i$ 的精确有理并集。
每个并集小区间 $[l,r]$ 都完全包含在双方各一个原生 span 内。
若某侧 span 是 $[s_j,s_{j+1}]$，记 $h=s_{j+1}-s_j$，则其局部变量为

$$
\tau=a+bt,\quad
a=\frac{Sl-s_j}{h},\quad b=\frac{S(r-l)}h,\quad t\in[0,1].
\tag{2}
$$

$a,b$ 在 Fraction 中精确形成，并逐项包围它们的二进制表示。
原生多项式第 $d$ 次导数额外乘 $(S/h)^d$。
这一步避免在极短区间上把两个独立舍入的端点先相减、再除以 span 长。

原始输入有两种存储：历史 `data_file` gzip NPZ，以及较新的无损分片 `data_storage`。
consumer 分别验证原始 payload SHA 或调用原有的分片 reader；两者最终送入同一实际 Hermite 定义。
若输入是 common-cut 定义，则按元数据的 `common_cut_implementation_sha256`
选择**原来那份** producer 并读入其真实尾端两 jet、桥根和五次修正。
不以本 consumer 的新公式悄悄重新定义 common 图。

## 2. Cartesian 角导数与连续多项式包围

写

$$
X=R e_r(\psi)+T e_\theta(\psi)+Z e_z,
$$
$$
R=r_0+\sum_{j=1}^M r_j\cos(3j\psi),\quad
T=\sum_{j=1}^M t_j\sin(3j\psi),\quad
Z=z_0+\sum_{j=1}^M z_j\cos(3j\psi).
$$

径向微分逐系数进行。因为 $\partial_\psi e_r=e_\theta$、
$\partial_\psi e_\theta=-e_r$，完整 Cartesian 角导数为

$$
X_\psi=(R_\psi-T)e_r+(R+T_\psi)e_\theta+Z_\psi e_z,
\tag{3}
$$
$$
X_{\psi\psi}=(R_{\psi\psi}-2T_\psi-R)e_r
 +(2R_\psi+T_{\psi\psi}-T)e_\theta+Z_{\psi\psi}e_z.
\tag{4}
$$

因此不能只对 $r_j,t_j,z_j$ 乘 Fourier 频率；旋转基底的项是必需的。
程序在**先作两图系数差**之后应用 (3)、(4)，包括 $u_{x\psi}$。
同一个正交柱坐标框架中的三分量 Euclidean 范数等于 Cartesian 范数。

对每个分量的每个三角系数，把径向幂基多项式转换为 Bernstein 基。
若所有 Bernstein 系数已被区间包围，该多项式在 $t\in[0,1]$ 的值属于其系数的凸包；
这是 Bernstein 基非负且总和为一的直接结论。
令 $A_k$ 为第 $k$ 个三角系数在整个径向区间上的绝对上界，则

$$
\sup_{t,\psi}\left|\sum_k a_k(t)\cos(k\psi)
                       +\sum_k b_k(t)\sin(k\psi)\right|
\le\sum_k A_k.
\tag{5}
$$

最后将三个分量上界的平方和开方，得到每个小区间上的

$$
U_0,\ U_x,\ U_\psi,\ U_{xx},\ U_{x\psi},\ U_{\psi\psi}.
\tag{6}
$$

此包围对所有角度和整个径向区间成立，不是有限角网格抽样。
所有多项式运算调用原有 outward 二进制区间类；正项累加使用带舍入补偿的上界，
Bernstein 转换矩阵使用有理系数的外包。
浮点输出中被声明为上界的数仍作为精确二进制数理解，不擅自向下截成较短十进制数。

有一个针对 (3)、(4) 的小型结构核对：取
$R=\cos3\psi,T=\sin3\psi,Z=0$，水平 Cartesian 向量就是 $e^{4i\psi}$。
真实零、一、二阶角导数范数为 $1,4,16$；本程序的分量 $\ell^1$ 包围相应为
$\sqrt2,4\sqrt2,16\sqrt2$（另有向外舍入），正确包含基底旋转贡献。
这只核对一个容易写错的恒等式；实际证书仍由上述连续包围产生。

## 3. 转为实际旧诱导度量的范数

这一节的参考必须是输入的真实 $X$，令 $h=X^*e$。
不把固定目标度量 $g$ 的联络代入。
在一个小区间上，假设已经有参考面积元下界

$$
|X_x\times X_\psi|\ge A>0,
\tag{7}
$$

以及连续参考一阶导数范数上界 $P_x,P_\psi$。
若原证书使用原生变量 $s$，则 (7) 取
$A=S_{\rm ref}A_s$；本程序以精确 Fraction 乘这个尺度。
Gram 矩阵的行列式至少 $A^2$，迹至多 $P_x^2+P_\psi^2$。
对于正定二阶矩阵，最小特征值是行列式除以最大特征值，最大特征值不超过迹。
故

$$
h\ge m I,\qquad m:=\frac{A^2}{P_x^2+P_\psi^2}>0.
\tag{8}
$$

于是 $h(v,v)=1$ 蕴含 $|v|_{\rm coord}\le m^{-1/2}$，且

$$
\varepsilon\le U_0,\qquad
\eta:=\sup_{h(v,v)=1}|du(v)|
\le\frac{\sqrt{U_x^2+U_\psi^2}}{\sqrt m}.
\tag{9}
$$

对于 $V=X$ 或 $V=u$，设其三个二阶导数的向量范数分别有上界
$A_V,B_V,C_V$。为避免与下一式的整体上界混淆，定义

$$
Q_V=\lambda_{\max}
\begin{pmatrix}A_V&B_V\\ B_V&C_V\end{pmatrix}
=\frac{A_V+C_V+\sqrt{(A_V-C_V)^2+4B_V^2}}2.
\tag{10}
$$

对任意坐标向量 $v=(v_1,v_2)$，三角不等式给

$$
|D^2V(v,v)|
\le A_Vv_1^2+2B_V|v_1v_2|+C_Vv_2^2
\le Q_V|v|_{\rm coord}^2.
\tag{11}
$$

其中间的矩阵不必半正定；它对 $(|v_1|,|v_2|)$ 的 Rayleigh 商仍不超过最大特征值。

现在使用真实诱导联络的 Gauss 公式。
记 $\Gamma_h(v,v)$ 为旧诱导度量的 Christoffel 二次项，$P_T$ 为旧切平面的正交投影。
逐坐标展开 Gauss 公式得

$$
dX\bigl(\Gamma_h(v,v)\bigr)=P_T D^2X(v,v).
\tag{12}
$$

因此当 $h(v,v)=1$ 时，

$$
\left|dX\bigl(\Gamma_h(v,v)\bigr)\right|
\le Q_X/m.
$$

由 (9) 的定义，对任意坐标向量 $w$ 都有 $|du(w)|\le\eta|dX(w)|$。
结合 (11)、(12)，

$$
\begin{aligned}
|\nabla_h^2u(v,v)|
&=|D^2u(v,v)-du(\Gamma_h(v,v))|\\
&\le Q_u/m+\eta Q_X/m.
\end{aligned}
$$

于是足够的全小区间上界为

$$
\boxed{\beta\le\frac{Q_u+\eta Q_X}{m}.}
\tag{13}
$$

这只用真实旧图一、二阶导数。$X\in C^2$ 使 $h\in C^1$，其联络连续，
所以没有暗中要求 $X$ 或两图差属于 $C^3$。
也没有把可能不接近真实联络的目标联络用于计算。
式 (13) 虽较逐角直接算 Christoffel 粗，但在当前实跑中有充分预算。

消费者逐一验证：参考面积证书声明完整连续覆盖；证书的 geometry SHA 与比较参考完全一致；
比较行数据的 SHA 未变；所有精确区间首尾相接且覆盖 $[0,1]$；
参考本身的导数在**同一组**小区间上重新作连续包围。

## 4. 已完成的实际 M12 base → M14 base 应用

参考是
`2026-11-09-db6f-root-flat17-coupled-m12f24.json`，SHA
`da43f85ee6715254cca3daddd609c80e23bdf97916acb9ba2034282c3c237c7d`；
比较图是 `2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json`，SHA
`11cd5569b3c2218591a757aea966f9aa25963fa1a3ec69fbb0b6729cb141a42d`。
这两份 actual Cartesian 保存图均为 $24$ 个三重谐波，BVP 源模数分别为 $12$、$14$。
原生节点数分别为 $2570$、$6599$，精确归一节点并集有 $8709$ 个小区间。
两边原生长度恰为同一个二进制有理数

$$
S=4552634583911787/2251799813685248.
$$

完整连续坐标差分输出：

| 导数 | 向量范数上界 |
|---|---:|
| $u$ | $2.5502820898702105\cdot10^{-8}$ |
| $u_x$ | $1.871752972509143\cdot10^{-6}$ |
| $u_\psi$ | $9.442569013385377\cdot10^{-7}$ |
| $u_{xx}$ | $3.8201900833040753\cdot10^{-4}$ |
| $u_{x\psi}$ | $7.381384852388961\cdot10^{-5}$ |
| $u_{\psi\psi}$ | $3.6716233444627045\cdot10^{-5}$ |

参考面积下界取同一个 base 图的完整连续证书
`2026-11-09-db6f-root-flat17-m12-geometry.json`，其原生面积下界为
$0.19996961293783194$，作为精确二进制数
$3602332297248969/18014398509481984$ 使用。
该证书 SHA 为
`20262efff59964dbc6ffb681aa58f934734a1150eaf7e9d42b3654b2e7831d18`。

逐小区间应用 (8)–(13) 后，全前缀得到

$$
\varepsilon\le 2.5502820898702105\cdot10^{-8},\qquad
\eta\le 1.2766692500778978\cdot10^{-5},\qquad
\beta\le 0.019754917072369236.
\tag{14}
$$

全部小区间的 $m$ 至少为 $0.020621242012440606$。
(14) 确实低于 R110 的三个充分阈值，但仅限这里精确定义的 **base 前缀比较**。
R110 的最终旧参考是 R21 的 actual common 闭图，不能仅因为名称相近便直接应用 (14)。
尤其两图 cut 修正的高阶 Fourier 模式不能省略。

实际报告和定义脚本：

- `scripts/fd2d-metric-prefix-c2-difference.py`，本次 SHA
  `fc5d483550bafc8adc4ddf89e07b6d89bc25523a5e1e83fcdf86ae2b76ed77db`；
  `notes/2026-11-12-fd2d-metric-m12-m14-prefix-c2-full.json` 与对应 `-rows.json.gz`。
- `scripts/fd2d-metric-prefix-tensor-difference.py`，本次 SHA
  `ef1b79067ae112de85413a032f87783ef0000abf8660a98ff0060bd688790471`；
  `notes/2026-11-12-fd2d-metric-m12-m14-prefix-induced-full.json` 与对应 `-rows.json.gz`。

真实命令分别用时约 $75.55$ 秒、$63.03$ 秒并正常退出。
工具会话分别为 `71801`、`41989`。
两个大行数据分别约 $2.33$ MB、$1.10$ MB，均 gzip 压缩且小于仓库单文件限制。
报告保留 `UNVERIFIED_GLOBALLY`、`whole_surface_transfer=false` 和 `new_metric_certificate=false`。

### 4.1 M12 actual common → 自身 base 的修正量

随后已真实读取 M12 common 的完整尾 raw 数据、精确增量端值、桥参数和原 common producer，
在全部 $2569$ 个原生 span 上比较其 common 图与自身 base。
这一步确实计入 common 的全部 $64$ 个三重谐波，没有仅保留 base 的 $24$ 模。
参考 common 定义 SHA 为
`253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`。
结果是

| 导数 | 向量范数上界 |
|---|---:|
| $u$ | $1.7243295709225254\cdot10^{-11}$ |
| $u_x$ | $6.936093352414087\cdot10^{-10}$ |
| $u_\psi$ | $1.188531169477414\cdot10^{-9}$ |
| $u_{xx}$ | $1.3586604366914439\cdot10^{-7}$ |
| $u_{x\psi}$ | $5.9235497493432456\cdot10^{-8}$ |
| $u_{\psi\psi}$ | $1.455366101451861\cdot10^{-7}$ |

使用同一 common 自己的完整 geometry 证书
`2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01-geometry.json`
（SHA `fc00c975f1ec9b0413d2d1c77e0dbf3dd27d35016c0b335ff439aba4aeeca462`）
转换到 $h_{\rm common}$ 后，得到

$$
\varepsilon\le1.7243295709225254\cdot10^{-11},\qquad
\eta\le6.432237538694632\cdot10^{-9},\qquad
\beta\le5.820922699604874\cdot10^{-6}.
\tag{14a}
$$

对应报告为 `2026-11-12-fd2d-metric-m12-common-to-base-c2-full.json`、
`2026-11-12-fd2d-metric-m12-common-to-base-induced-full.json` 及各自的 gzip 行数据。
两次命令正常退出，用时约 $99.92$ 秒、$93.90$ 秒；真实工具会话为 `1434`、`23201`。
这确认 consumer 能读取并量化 R21 参考图的真实 common 修正。
它仍不含任何**新的** common 图的修正，不能把 (14a) 和 (14) 未经联络转换便简单相加成全局结论。

## 5. common 前缀与物理尾的全局 C² 对应

本节说明**未来完整比较所需的明确对应**，不声称当前已完成它的全部差分预算。
设两图的 common 定义都使用同一个物理 cut $c$、尾背景斜率 $w(r)$、
同一 exact bridge 根和同一精确前缀物理总长 $L$。
第 $i$ 份原生长度为 $S_i$，common producer 中的缩放满足
$\lambda_i=S_i/L$。

在前缀以物理变量 $\sigma=Lx$ 比较；其实际映射就是
$X_i(S_i x,\psi)$。尾部用共同物理 $r$，并在 cut 附近定义

$$
\sigma=L+\int_r^c\sqrt{1+w(t)^2}\,dt.
\tag{15}
$$

在 $r=c$，令 $E=1+w(c)^2$，则

$$
r_\sigma=-E^{-1/2}=:k,\qquad
r_{\sigma\sigma}=-w(c)w_r(c)/E^2=:k_2.
\tag{16}
$$

原 common producer 的端点目标恰为尾部两 jet

$$
T_0,\qquad (k/\lambda_i)T_1,\qquad
(k^2T_2+k_2T_1)/\lambda_i^2
\tag{17}
$$

（$T_j$ 是物理 $r$ 导数）。把 native 参数改为 $x$ 后，
一、二阶分别乘 $S_i,S_i^2$；由 $S_i/\lambda_i=L$，它们正是
共同变量 $\sigma=Lx$ 的一、二阶尾 jet。
因此两图在同一抽象参数面的 cut 处均为 C²，二者之差也为 C²。

此处角变量直接使用 common producer 拼接的同名 Fourier 角 $\psi=\theta$。
它定义的是用于比较像集几何的真实全局对应。
若还要用该对应比较固定 $g$ 的误差，则必须另核对实际材料角的拉回，
不得把同名适应角自动当成固定物理材料角。

其余接口也必须按各图真实定义处理：

- 中央镜像接口使用各图保存的 exact inlet mirror 两 jet；
  差分在相同的有符号 $x$ 镜像下延拓。
- 两图尾部各自从实际首节点到同一 cuff 使用零两 jet 的 R6 collar。
  即使两首节点半径不同，也在共同物理 $r$ 轴上取节点并集，并保留各自 collar 的准确多项式。
- cuff 处两扰动的值、一阶、二阶均为零，背景旋转轮廓相同。
  使用同一平盘/凸起函数的帽只需分别加本图自己的高度常量；
  因而帽上差分是常向量，$du=\nabla_h^2u=0$。

最后一点并不允许丢掉尾的高度常数差。
反射上尾是 $Z_i=H_{c,i}+\int_r^c w-V_i^z$，故
$u_z=H_{c,\rm new}-H_{c,\rm ref}-(V_{\rm new}^z-V_{\rm ref}^z)$。
公共背景可准确相消，但 $H_c$ 必须从各自实际 mean gauge 定义读取。

只要完整实际新旧 common 前缀、尾、collar、帽比较共同满足 R110 的阈值，
本节就把分块界变为全局界；当前 base-only 报告尚不满足这个前提。
活动部分各相位像集只是初始像集的共同旋转，帽固定，
因而像集的几何转移可由初始比较旋转传递；
这不把适应角的平移冒充实际材料角平移，也不产生新图的度量证书。

## 6. 当前输入限制与可继续复用部分

M12 actual common 的定义与尾 raw shards 当前完整可读。
旧 M14 的 `closed-map.json` 虽已推送，其清单依赖的 $26$ 个尾 raw shards
本地全部缺失；所以本笔记没有重跑或臆造 M14 common 的数值差分。
保留的 producer stdout 只有三个 cut jet 系数最大值，不足以替代完整高频定义。
原 reader 的 common 模式会严格读取这些 raw 定义，缺失就报错。

新实际联解的 base/common 到达后，两脚本可按其原输入直接运行。
对最终几何用途，参考须明确选 R21 的 M12 common，或者分别严格计入旧、新 common 修正后再转换。
对最终 G5 用途，仍要独立证明新图相对原固定 $g$ 的真实全域误差下降到 $2\cdot10^{-9}$。
R109 已说明旧图仅作保圈重标无法代替这一步。
