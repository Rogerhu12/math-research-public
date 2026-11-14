# R116：真实射线角图的完整半阶端口、强角档与两层密度界

2026-11-13，visible-exact-astra-f6a2。

**已完成：** 从已付的 R106 全时、全角、整参数射线证书，得到
真实角坐标变换的双向强范数。任意两个时刻之间，完整高度
$H^{1/2}$ / 通量密度 $H^{-1/2}$ 端口的两向常数均小于 $6.202$，
不使用二阶角导数。原始标签到每个物理切口另有较小的单腿常数；
实际 $H^{5/4}$ 双向费用也已支付。全部常数的37个有理门已实际执行。

这给的是同一真实角图的坐标接线，不是完整 PDE 传播。
密度的 $H^{1/2}$ 与其 $H^{-1/2}$ 是两个不同的档；
本篇单列前者的两层估计，不把便宜的端口常数移给它。
实际振幅、源、Airy、帽响应、最终 KAM frame 和全 Schur 仍保留。

## 1. 同一实际输入，以及不可漏掉的角标度

使用 notes/2026-11-12-R106-actual-all-time-ray-tube.json，
完整 UTF8 SHA256 为
6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863。
它已经连续覆盖550段、整个前腿及
$$
p\in[p_0-10^{-9},p_0+10^{-9}],\qquad
p_0=-7789843107295549/4611686018427387904.
$$
同一真实物理射线满足
$$
\Theta(\tau,x+2\pi)=\Theta(\tau,x)+\pi/2,\qquad
\frac{213831}{7812500}<\Theta_x<
\frac{8223669}{7812500},\qquad |\Theta_{xx}|<1100
\tag{116.1}
$$
在所有实时间、实标签及该参数盒上成立。复标签证书更强，但本篇
只消费实图及其真实导数。初值为 $H_5(x)/4$，不是 $x$。

定义归一的次数一圆图
$$
\psi_\tau(x)=4\Theta(\tau,x).
$$
其两边都以 $2\pi$ 为周期，因此应使用
$$
m=\frac{855324}{7812500},\quad
M=\frac{32894676}{7812500},\quad L=4400,\qquad
m<\psi_\tau'<M,\quad |\psi_\tau''|<L.                 \tag{116.2}
$$
不能把 (116.1) 的物理 $\Theta_x$ 当成自圆图导数：
其平均为 $1/4$，而 $\psi'$ 的平均为1。全部后续有理门包含这个因子4。

对物理四周期函数 $f(\theta)$，置 $\widetilde f(y)=f(y/4)$，
则 $f(\Theta(x))=\widetilde f(\psi(x))$。
若 $p_\theta$ 为物理全圆的 conormal density，
四重周期性给准确配对
$$
\int_0^{2\pi}p_\theta(\theta)f(\theta)\,d\theta
=\int_0^{2\pi}4\Theta_x(x)
 p_\theta(\Theta(x))f(\Theta(x))\,dx.                 \tag{116.3}
$$
所以完整归一标签密度是 $4\Theta_x\,p_\theta\circ\Theta$。
若使用未经四重求和的单个物理基本区间及 raw $dx$ 密度，
它是 $\Theta_x\,p_\theta\circ\Theta$；两者差一个明确的4，
不能在端口或普通源中默默互换。

## 2. 不删除均值的完整 Sobolev 空间

所有 Fourier 系数按 $dx/(2\pi)$ 归一。对 $\kappa\ge1$ 定义
$$
\|f\|_{H^s_\kappa}^2
=\sum_{k\in\mathbb Z}(1+\kappa^2k^2)^s|f_k|^2,\qquad
\Lambda_\kappa=(1-\kappa^2\partial_x^2)^{1/2}.          \tag{116.4}
$$
$\kappa=1$ 是归一标签档，$\kappa=4$ 是物理四重角档。
零模始终存在，权恰为1。

设任意次数一、保向实圆图 $\psi$ 满足
$0<m\le\psi'\le M$；因其平均导数为1，必有 $m\le1\le M$。
定义高度与密度两个不同的映射
$$
C_\psi f=f\circ\psi,\qquad
D_\psi f=\psi'(f\circ\psi).                            \tag{116.5}
$$
换元立即给
$$
\|C_\psi\|_{L^2\to L^2}\le m^{-1/2},\qquad
\|D_\psi\|_{L^2\to L^2}\le M^{1/2}.                    \tag{116.6}
$$
又 $(C_\psi f)'=\psi' f'\circ\psi$，故
$$
\|C_\psi\|_{H^1_\kappa\to H^1_\kappa}
\le B:=\max(m^{-1/2},M^{1/2}),                         \tag{116.7}
$$
与 $\kappa$ 无关；零阶与导数项分别用 (116.6) 和
$\int\psi'^2|f'\circ\psi|^2dx\le M\int|f'|^2dy$。

对同一 Fourier Hilbert 标度，端点有界算子的插值给
$$
\boxed{
\begin{aligned}
\|C_\psi:H^s_\kappa\to H^s_\kappa\|
 &\le m^{-(1-s)/2}B^s,\\
\|C_{\psi^{-1}}:H^s_\kappa\to H^s_\kappa\|
 &\le M^{(1-s)/2}B^s,\qquad 0\le s\le1 .
\end{aligned}}                                                     \tag{116.8}
$$
这里可直接证明所用插值：对有限 Fourier 测试向量，将
$\Lambda_\kappa^z C_\psi\Lambda_\kappa^{-z}$ 与它们配对；
在 $\Re z=0,1$ 上，虚幂为酉，因此分别由两个端点 norm 控制。
三线不等式给 (116.8)，再由稠密性延伸。
逆图的端点参数是 $1/M,1/m$，其 $H^1$ 上界仍为同一个 $B$。
整个论证没有投影均值，也没有求 $\psi''$。

按真实 $L^2$ 配对，
$$
C_\psi^*=D_{\psi^{-1}},\qquad D_\psi^*=C_{\psi^{-1}}.
$$
因此完整对偶空间上
$$
\boxed{
\begin{aligned}
\|D_\psi:H^{-s}_\kappa\to H^{-s}_\kappa\|
 &\le M^{(1-s)/2}B^s,\\
\|D_{\psi^{-1}}:H^{-s}_\kappa\to H^{-s}_\kappa\|
 &\le m^{-(1-s)/2}B^s .
\end{aligned}}                                                     \tag{116.9}
$$
密度平均准确保持；其常数输入通常产生非零角模。
高度平均通常改变。上述完整算子包含这两种 mean/high 混合，
没有把常数函数误当成高度和密度的共同不变子空间。

## 3. 实际单腿与任意两切口常数

对 (116.2)，准确有 $mM<1$，所以 $B=m^{-1/2}$。
(116.8)–(116.9) 在 $s=1/2$ 给：

| 实际同一角图 | 正向 | 逆向 |
|---|---:|---:|
| 高度 $H^{1/2}_\kappa$ | $3.023$ | $2.491$ |
| 密度 $H^{-1/2}_\kappa$ | $2.491$ | $3.023$ |

所有数都为严格上界，适用于 $\kappa=1,4$，乃至任何固定 $\kappa\ge1$。
例如逆向半阶界是 $(M/m)^{1/4}<2491/1000$；
正向为 $m^{-1/2}<3023/1000$。

对于任意两个相同参数的时刻，真正的相对圆图为
$$
\phi=\psi_{\tau_1}\circ\psi_{\tau_0}^{-1}.
$$
置 $R=M/m$。则
$$
R^{-1}\le\phi'\le R,\qquad
R=\frac{8223669}{213831}<38.459 .
$$
(116.6)–(116.9) 的两端界现在都为 $\sqrt R$，从而
$$
\boxed{
\|C_{\phi}^{\pm1}:H^s_\kappa\to H^s_\kappa\|,
\quad
\|D_{\phi}^{\pm1}:H^{-s}_\kappa\to H^{-s}_\kappa\|
<\frac{3101}{500}=6.202,\quad 0\le s\le1 .
}                                                                 \tag{116.10}
$$
此处 $C_\phi^{-1}=C_{\phi^{-1}}$，密度同理。
它是完整相对图的费用，不是把550个局部粗上界相乘。
同一特征分支上相对图或其逆对应真实两切口之间的角坐标识别。
不同分支的耦合、真实 PDE 动力学以及跨根传播不由此消失。

### 完整辛端口

对同一 $\kappa$ 令
$$
z^\pm=\frac{\Lambda_\kappa^{1/2}u
          \mp i\Lambda_\kappa^{-1/2}p}{\sqrt2}.
$$
从 $H^{1/2}_\kappa\oplus H^{-1/2}_\kappa$ 到 $L^2\oplus L^2$
的此映射为酉，且端口范数差记录 $2\Im\langle p,u\rangle$。
高度/密度一起变成 $(C_\psi u,D_\psi p)$，由换元保持该配对，
所以它诱导真正的可逆辛端口变换。其普通 Hilbert norm 及逆 norm
均小于3.023；相对切口的两向常数均小于6.202。
没有额外的 $\sqrt2$ 因子，也没有删掉 regular/mean。

不同 $\kappa$ 之间不能免费等同。恒等映射的准确范数为
$$
\|\mathrm{id}:H^s_{\kappa_1}\to H^s_{\kappa_2}\|
=\max\{1,(\kappa_2/\kappa_1)^s\}.                      \tag{116.11}
$$
这由逐 Fourier 模权比的上确界直接得到，负 $s$ 也适用。
因此物理 $4k$ 与最终归一标签 $k$、以及 raw 密度的常数因子，
都可用 (116.3)、(116.11) 显式接线；不能借“共同标签”省去它们。

## 4. 商去常数后的更精确半阶界

本节只用于齐次半范数，不替代 §2 的完整均值接口。
任意这样的 $\psi$ 还有
$$
|f\circ\psi|_{\dot H^{1/2}}
\le(M/m)^{1/4}|f|_{\dot H^{1/2}}.                     \tag{116.12}
$$
反向同一常数。给出一个不含 $\psi''$ 的证明：
将 $\psi$ 径向延拓到单位盘
$\Phi(re^{ix})=r^a e^{i\psi(x)}$，取 $a=\sqrt{mM}$。
它的径向、角向伸长分别为 $ar^{a-1}$、$\psi'r^{a-1}$，
故 Dirichlet energy 的失真至多
$\max(a/m,M/a)=\sqrt{M/m}$。
对 $f$ 的调和延拓 $u$，换元逐项验证
$$
E(u\circ\Phi)
=\int\left[\frac a{\psi'}|u_r|^2r+
          \frac{\psi'}a\frac{|u_x|^2}{r}\right]dr\,dx
\le\sqrt{M/m}\,E(u).
$$
零点处按半径趋零取极限；该映射及逆局部具有所需有限能量，
并可先在环盘上作同一换元。调和延拓最小化同迹 Dirichlet energy，
而 Fourier 级数给 $E(u)=2\pi\sum|k||f_k|^2$，故得 (116.12)。
实际单腿小于2.491；实际相对图仍小于6.202。
其常数方向是零范数方向，不能据此把 full regular 输出省略。

## 5. 已付二阶角导数如何进入真正 $H^{5/4}$

本节使用 (116.2) 的 $L$；半阶便宜门不使用它。
链式法则及实际换元给
$$
(C_\psi f)''=\psi'^2 f''\circ\psi+\psi''f'\circ\psi .
$$
把 $H^2_\kappa$ 写成
$\|f\|_2^2+2\kappa^2\|f'\|_2^2+\kappa^4\|f''\|_2^2$，
先对三项主部一起估计，再保留二阶链式余项，得到
$$
\|C_\psi:H^2_\kappa\to H^2_\kappa\|
\le B_2+\frac{\kappa^2}{1+\kappa^2}\frac L{\sqrt m},
\quad
B_2=\max(m^{-1/2},M^{1/2},M^{3/2}).                    \tag{116.13}
$$
这里使用的是准确离散上界
$\sup_{k\ne0}|k|/(1+\kappa^2k^2)=1/(1+\kappa^2)$，因为 $\kappa\ge1$。
没有丢掉一阶输出或零模。

逆图满足
$$
(\psi^{-1})''=-\frac{\psi''\circ\psi^{-1}}
                   {(\psi'\circ\psi^{-1})^3},
\qquad L_{\rm inv}\le L/m^3.                         \tag{116.14}
$$
对其参数 $(1/M,1/m,L/m^3)$ 使用同一公式。
将 $H^1$、$H^2$ 按 $1/4$ 插值，准确得 $H^{5/4}$；
四次方有理门已支付以下全部严格上界：

| $\kappa$ | 正向 $H^2$ | 逆向 $H^2$ | 正向 $H^{5/4}$ | 逆向 $H^{5/4}$ |
|---:|---:|---:|---:|---:|
| 1 | 6660 | 3441000 | 21 | 99 |
| 4 | 12528 | 6477000 | 25 | 116 |

例如 $\kappa=4$ 的正向四次方预算为
$(3023/1000)^3\,12528<25^4$。
此处取得的是实际原始 $H_5$ 标签与切口之间的高度费用；
R101 的最终 KAM 共轭及 R46 的振幅/frame 仍须接入。

## 6. 密度正半阶：主费用与低层费用分开

对于 R110 的符号
$J_\kappa e_k=\sqrt{\max(1,\kappa|k|)}\,e_k$，使用准确 norm
$$
\|f\|_{\mathsf H^{1/2}_\kappa}^2
=|f_0|^2+\kappa\sum_{k\ne0}|k||f_k|^2.                 \tag{116.15}
$$
它包括 mean，但与 §2 的 Bessel norm 不同。
其非零部分有准确圆周公式
$$
|f|_{\dot H^{1/2}}^2
=\int\!\!\int
 \frac{|f(x)-f(y)|^2}{4\sin^2((x-y)/2)}
 \frac{dx\,dy}{(2\pi)^2}.                             \tag{116.16}
$$
逐模积分给 $\int\sin^2(kh/2)/\sin^2(h/2)\,dh/(2\pi)=|k|$，
先对多项式证明，再由完备化得到全频等式。

写 $J=\psi'$、$f_x=f(\psi(x))$。保留几何平均作准确分解：
$$
J(x)f_x-J(y)f_y
=\sqrt{J(x)J(y)}(f_x-f_y)
+(\sqrt{J(x)}-\sqrt{J(y)})
 (\sqrt{J(x)}f_x+\sqrt{J(y)}f_y).                     \tag{116.17}
$$
第一项换元后两个 Jacobian 精确相消。
保向圆图且 $J\le M$ 给 chord 上界
$$
|e^{i\psi(x)}-e^{i\psi(y)}|
\le M|e^{ix}-e^{iy}|.
$$
证明可取最短角距 $h\le\pi$：若 $Mh\le\pi$，用
$\sin(Mh/2)\le M\sin(h/2)$；若 $Mh\ge\pi$，
$M\sin(h/2)\ge1$。故第一项在 (116.16) 中至多 $M|f|_{\dot H^{1/2}}$。

第二项使用
$|(\sqrt J)'|\le L/(2\sqrt m)$。
最短角距的完整核积分恰为
$$
\int_{-\pi}^{\pi}
 \frac{h^2}{4\sin^2(h/2)}\frac{dh}{2\pi}
=2\log2.
$$
分部积分并用
$\int_0^\pi\log\sin(h/2)\,dh=-\pi\log2$ 即得；
后式也可由 $\log|1-re^{ih}|$ 的 Fourier 展开后令 $r\uparrow1$ 得到。
分别估计 (116.17) 第二项的两个对称部分，
$\|\sqrt J\,f\circ\psi\|_2=\|f\|_2$，所以得到
$$
|D_\psi f|_{\dot H^{1/2}}
\le M|f|_{\dot H^{1/2}}+\frac{\sqrt{2\log2}\,L}{\sqrt m}\|f\|_2.
$$
密度均值准确保持，故完整的两层不等式为
$$
\boxed{
\begin{pmatrix}
 \|D_\psi f\|_2\\
 \|D_\psi f\|_{\mathsf H^{1/2}_\kappa}
\end{pmatrix}
\le
\begin{pmatrix}
 \sqrt M&0\\
 \dfrac{6\sqrt\kappa\,L}{5\sqrt m}&M
\end{pmatrix}
\begin{pmatrix}
 \|f\|_2\\
 \|f\|_{\mathsf H^{1/2}_\kappa}
\end{pmatrix}.
}                                                                 \tag{116.18}
$$
其中 $\sqrt{2\log2}<6/5$ 已由完整有理级数尾支付。
此式保留全频和 mean；没有用有限 Fourier 尾替代真实链式法则。

反向用 $(1/M,1/m,L/m^3)$。
相对图还满足
$$
|\phi''|\le L_{\rm rel}:=\frac{L(M+m)}{m^3},             \tag{116.19}
$$
由 $(\psi_1\circ\psi_0^{-1})''$ 逐项展开得到；逆相对图同一界。
因此两层矩阵始终有效。报告付出了如下粗的低→高费用：

| $\kappa$ | 单腿正向 | 单腿逆向 | 任意相对图，两向 |
|---:|---:|---:|---:|
| 1 | 15962 | 8256400 | 107803000 |
| 4 | 31924 | 16512800 | 215606000 |

实际同档主费用是 $M,1/m,R$，不包含这些大低层数字。
这些是确定的后备两层界；可与 R110 的 signed commutator /
实际 characteristic density 积分费用取较小的已付界。
不能把低→高项当成每一小叶都重新指数化的主增长率。
尤其本节没有把 (116.10) 免费授给密度 $\mathsf H^{1/2}$。

## 7. 对全源接线的作用与仍在推进的项

本篇已经支付同一整参数真实角图的以下部分：

- 完整高度与通量密度的双向 $H^{1/2}\oplus H^{-1/2}$ 接线，
  含所有 mean/regular 交叉项；
- 原始标签到物理切口的真实 $H^{5/4}$ 高度费用；
- 密度正半阶的完整两层费用，以及物理/标签 Fourier 标度转换。

它们可直接接 R107 的准确弱源与 R110 的强传播。
$y_\pm$ 的实际 $B_\pm,d$ 耦合、mean 方程、普通源、
两根/Airy/真实外端和最后的 $K_{\rm wire}$ 必须继续保留。
这里只证明角图这一因子的 norm，不能把它当成完整反馈强余项或右逆。

## 8. 实际执行与重放

源码 scripts/fourfold_true_ray_Sobolev_coordinates_exact.mjs，
报告 notes/2026-11-13-R116-true-ray-Sobolev-coordinates.json。
同一纯 BigInt 核已实际在 V8 通过37门，逐字核对完整 R106 输入 SHA；
没有重新生成 ODE 或 density 叶，也没有声称 native CLI 已运行。

源码 SHA256：
8df0f3d84acb8eec7c8f5814c2df9995497bfb3b2d8934dab801d70b14a2ddf3。

完整报告 SHA256：
3917745a9fbf7bcaa792a63c2164edd11565007ab6445da1437f9fe1eb1c9d94。

原生恢复后可从课题目录用 Node 重放：

~~~sh
node scripts/fourfold_true_ray_Sobolev_coordinates_exact.mjs \
 --out notes/2026-11-13-R116-true-ray-Sobolev-coordinates-replayed.json
~~~

本篇没有新增候选几何的采样值；常数来自原已完成连续证书与上面的
完整算子证明。完整强 PDE 逆、真实邻域及非线性闭面仍继续 open.md。
