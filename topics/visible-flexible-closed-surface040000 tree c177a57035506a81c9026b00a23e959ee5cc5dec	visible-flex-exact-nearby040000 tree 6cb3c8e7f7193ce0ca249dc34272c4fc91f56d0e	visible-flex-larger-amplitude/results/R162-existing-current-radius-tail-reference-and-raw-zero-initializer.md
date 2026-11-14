# R162 — 现有带权平尾 lifting、准确零修正平台及端口一 jet

**状态：已证明。** 当前 provider 的晚段 lifting 本来就是在真实当前半径上评价的平尾曲率。把保存的 raw 修正系数在末平台准确置零，再应用既有 R155 正迹表示，会得到一个无需角投影的新初值：它在整个平台满足 Gauss，形式主曲率严格小于 $33/5$，完整 cut 值和径向、角向一阶迹连续接到准确平尾。本文保留全部 Codazzi 缺陷；该参考不是已经实现的等距浸入、完整核或闭曲面，也不默认替换正在改进的主求解状态。

## 1. 既有函数及准确适用区间

固定物理材料坐标 $(s,u)$ 和目标度量
$$g=ds^2+a(s)^2du^2.$$
令 $S$ 为切口的物理 $s$ 坐标，$c=a_s/a$。数组分量顺序始终为 $(n,m,l)$；相应对称矩阵为
$$\mathrm{II}=\begin{pmatrix}l&m\\m&n\end{pmatrix}.$$
为避免和第二基本形式混淆，下面以 $B(u)$ 表示三个分量组成的向量：
$$B(u)=(\cos^2u,-\sin u\cos u,\sin^2u).$$

在现有 `fd2d_gc_raw_lifted_dae.py::lifting` 中，记固定标量 $s_\eta=.42S$，则尾权重是
$$
\eta(s)=S_5\!\left(\frac{s-s_\eta}{S-s_\eta}\right),\qquad
S_5(t)=10t^3-15t^4+6t^5\quad(0\le t\le1),
\tag{1}
$$
区间外按 $0,1$ 截断。代码中分母使用同一次求值的 `cut-start`；不把不同算式的末位舍入误差冒充逐字节相同。

R132 的非负 Bernstein 尾曲率记为 $\kappa(y)$。现有准确尾 lifting 为
$$
q(s,u)=\kappa(a(s)\sin u),\qquad
k(s,u)=\eta(s)q(s,u),\qquad L(s,u)=k(s,u)B(u).
\tag{2}
$$
这与 R157 固定切口函数 $\kappa(a_c\sin u)$ 的径向延伸不同。这里的 $a(s)$ 是实际目标半径；没有新选一个物理度量。

当前中央 seed 权重在 $s\ge.55$ 恒零，冻结 coast lifting 及 R153 窗的共同支撑最右端约为 $.8675434451024153$。因此本文选取 $s\ge1.3$ 后，既有完整 affine lifting 准确只剩 (2)。这不是近似忽略其它项：其既定紧支窗在这里恒零。

当前 candidate 为
`notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json`，
SHA256 `7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。
其末桥满足 $a_c=4/5$、$L=.026$、$p_d=1.45$ 及准确终相位 $-\pi/2$。七个外设计 bump 在 $[S-.02,S]$ 恒零。

保存的 R155 窗从 $s_-=1.4689731783581288$ 起上升，到
$s_+=1.4759731783581287$ 后准确为 $1$，切口为
$S=1.4889731783581288$。这些是当前实体直接保存的 binary64 坐标；本文使用原保存值，不通过另一个算式重新生成其窗口身份。形式证明只需 $[s_+,S]\subset[S-.02,S]$，不依赖打印小数被当作另一条精确积分定义。

## 2. 准确零修正时既有 R155 自动给出的参考

设某个完整径向区间上 raw 的三个修正函数恒零，且 R155 窗恒为 $1$。由第 1 节，送入正迹变换的原场就是 $L=kB$。于是
$$
d=n_0-l_0=k\cos2u,\qquad m_0=-\frac{k}{2}\sin2u,\qquad n_0+l_0=k.
$$
R155 的平方根和增量准确变成
$$
h=\sqrt{k^2+4K},\qquad
b=\frac{h-k}{2}=\frac{2K}{h+k},\qquad K=-a_{ss}/a.
\tag{3}
$$
最后的商只在 $h+k>0$ 处使用；$K=k=0$ 时直接定义 $b=0$。所以实际完整正迹场是
$$
\widehat n=k\cos^2u+b,\qquad
\widehat m=-k\sin u\cos u,\qquad
\widehat l=k\sin^2u+b.
\tag{4}
$$
这是原 provider 对完整函数的恒等式，不是把 (4) 投影到某个 Fourier 截断后得到的近似。

因 $b^2+kb=K$，该对称矩阵的两个特征值为 $b,k+b$，故
$$\widehat n\widehat l-\widehat m^2=K.$$
内部 $K>0$ 时它正定。切口上 $\eta=1,K=0,a=a_c$，(4) 准确等于 R132 的非负 rank-one 平尾迹，包括其全零开弧及 $n=0$ 轴点。既有 provider 在准确 cut 直接取这个尾迹，不对 $h=0$ 的一般平方根求导。

## 3. 当前保护平台上的严格形式曲率预算

置 $r=S-s$、$D=\pi/2-p_d$。实际末桥的定义是
$$
\epsilon(r)=D(3r^2/L^2-2r^3/L^3),\quad
a=a_c+\int_0^r\cos\epsilon(v)\,dv,\quad
a_s=-\cos\epsilon,\quad K=\frac{\sin\epsilon\,\epsilon_r}{a}.
\tag{5}
$$
在 $0<r<L$ 上，$\epsilon,\epsilon_r>0$，所以 $K>0$。实际输入数满足
$L>1/40$、$p_d>14499/10000$。由 $\pi<22/7$，有 $0<D<1/8$。又 $a\ge4/5$、$\epsilon_r\le3D/(2L)$，故
$$
0<K<\frac{3D^2}{2La}<\frac{75}{64}.
\tag{6}
$$
在整个 R132 控制盒 $0\le p_j\le6/5$ 内，全实轴上
$$0\le\kappa(y)\le\frac{4725}{736}.$$
因为 $0\le\eta\le1$，同一上界也适用于 $k$。令 $C=33/5$，则
$$
C\left(C-\frac{4725}{736}\right)-\frac{75}{64}
=\frac{633}{36800}>0.
\tag{7}
$$
若 $k+b\ge C$，则 $b(k+b)\ge C(C-k)>K$，与 (3) 矛盾。因此
$$
\boxed{0\le b\le k+b<33/5.}
\tag{8}
$$
这是完整角圆、完整保护平台及整个非负尾参数盒上的严格代数结论。它不依赖本次有限点检查。不过，在 Codazzi 和实际 Cartesian 重建尚未成立时，(8) 只是参考 II 的形式特征值界，不能称为已存在曲面的曲率或 reach 证书。

早期淡出区不属于本命题的正 $K$ 平台；那里必须保留实际目标 $K$、真实 Gauss/Codazzi 和完整曲率检查，不能从 (8) 外推。

## 4. 完整径向、角向导数与 Codazzi 缺陷

在 $K>0$ 内部按固定材料角求导。记 $q_y=\kappa_y(a\sin u)$、$v=a_s$，则
$$
k_s=\eta_s q+\eta q_y v\sin u,
\qquad k_u=\eta q_y a\cos u,
\tag{9}
$$
$$
b_s=\frac{K_s-bk_s}{h},\qquad b_u=-\frac{bk_u}{h}.
\tag{10}
$$
于是
$$
\widehat S_s=k_sB+b_s(1,0,1),\qquad
\widehat S_u=k_uB+kB_u+b_u(1,0,1).
\tag{11}
$$
这里 $\widehat S$ 表示 (4) 的分量向量。定义真实材料 Codazzi 缺陷
$$
R_n=n_s-m_u/a-c(l-n),\qquad
R_m=m_s-l_u/a+2cm.
\tag{12}
$$
先将 $kB$ 代入 (12)。因为
$k_s=\eta_s q+\eta q_yv\sin u$、$k_u=\eta q_ya\cos u$，逐项合并得到
$$
R_n^0=\eta_s q\cos^2u+
\eta(1+v)\left(q_y\sin u\cos^2u+\frac{q\cos2u}{a}\right),
\tag{13}
$$
$$
R_m^0=-\eta_s q\sin u\cos u-
\eta(1+v)\left(q_y\sin^2u\cos u+\frac{q\sin2u}{a}\right).
\tag{14}
$$
同加 $b$ 于 $n,l$ 后，$c(l-n)$ 项准确不变，故完整缺陷为
$$
\boxed{R_n=R_n^0+b_s,\qquad R_m=R_m^0-b_u/a.}
\tag{15}
$$
这些项通常不为零。特别是在 $q$ 恒零的尾开弧，内部参考等于 $\sqrt K I$，而
$$R_n=K_s/(2\sqrt K),\qquad R_m=0.$$
小曲率和准确 Gauss 并没有消去这个 Codazzi 误差。

若计算角为 $u=U(s,\xi)$，则
$$\partial_x=\partial_s+U_s\partial_u,\qquad
\partial_\xi=U_\xi\partial_u.$$
因此完整计算式仍含 $U_s/U_\xi$ 的漂移项。原 R155 的实际 $n$ 端点差、角漂移以及参数导数必须一起使用；不能只添加 (15) 的采样值而丢掉实际场变化。当前平台的原角图已经回到 $U=\xi$，但较早淡出区可以仍有 $U_s\ne0$。

积分 Codazzi 消费可以直接用实际端点值处理 $b_s$，不需要为使用本初值增加 $K_s$ 或 II 径向二阶正则性条件。提供 $K_s$ 的小消费者只用于本明确光滑标量 profile 的内部点态诊断。

## 5. 全角一致的真实 cut 一阶迹

由 (5) 的 Taylor 展开，存在 $C_0>0$ 使
$$
a=a_c+r+O(r^5),\quad 1+a_s=O(r^4),\quad
K=C_0r^3+O(r^4),\quad K_s=O(r^2).
\tag{16}
$$
固定权重 (1) 满足
$$1-\eta=O(r^3),\qquad \eta_s=O(r^2).\tag{17}$$

需要控制随角度接近零曲率支撑边界的混合极限。R132 的曲率在内部 $t=(|y|-.34)/.46\in(0,1)$ 为有限和
$$
\kappa(y)=\sum_{j=0}^{d}p_j f_j(t),\qquad
f_j(t)=\frac{630\binom dj}{w}\,t^{j+4}(1-t)^{d-j+4},\quad w=.46.
\tag{18}
$$
各项在区间外延零。所有端点幂至少为 $4$。直接求导并除以 $f_j^{3/4}$，所有剩余幂均非负，所以
$$
|\partial_yf_j|\le C_jf_j^{3/4},\qquad
C_j=\frac{d+8}{w}\left(\frac{630\binom dj}{w}\right)^{1/4}
\tag{19}
$$
是一个足够的常数，且端点导数也为零。由 Hölder 不等式，$0\le p_j\le6/5$ 给
$$
|\kappa_y|
\le\max C_j\sum_j p_j f_j^{3/4}
\le\max C_j\left(\sum_jp_j\right)^{1/4}\kappa^{3/4}
\le C\kappa^{3/4}.
\tag{20}
$$
这对固定尾次数的整个控制盒统一成立，包括某些或全部控制为零。

在 cut 的一个固定邻域中 $\eta\ge1/2$。结合 (9)、(16)–(20)，有统一估计
$$
|k_u|\le Ck^{3/4},\qquad
|k_s|\le Cr^2k+Ck^{3/4}.
\tag{21}
$$
另一方面，$h\ge2\sqrt K$，且对 $k>0$
$$
0\le\frac bh\le\min\left(\frac12,\frac K{k^2}\right).
\tag{22}
$$
在 $k\le\sqrt{2K}$ 与补集分别使用这两个界，可得
$$
\frac bh k^{3/4}\le C K^{3/8}.
\tag{23}
$$
$k=0$ 处由 (20) 直接得 $k_s=k_u=0$，无需使用右侧含 $k^{-2}$ 的写法。于是
$$
|b_u|\le CK^{3/8}=O(r^{9/8}),
\tag{24}
$$
$$
|b_s|\le\frac{|K_s|}{2\sqrt K}+Cr^2+CK^{3/8}
=O(r^{1/2}).
\tag{25}
$$
这证明 $b_s,b_u\to0$ **全角一致**，并非只在非零曲率角固定后取极限。又 $0\le b\le\sqrt K$，所以参考的值及两种一阶迹连续趋于
$$
\widehat S\to\kappa(a_c\sin u)B(u),
\tag{26}
$$
$$
\widehat S_s\to-\kappa_y(a_c\sin u)\sin u\,B(u),
\tag{27}
$$
$$
\widehat S_u\to a_c\kappa_y(a_c\sin u)\cos u\,B(u)
+\kappa(a_c\sin u)B_u(u).
\tag{28}
$$
平尾按同向物理 $s$ 延拓时 $a_s=-1$，其准确 II 是
$\kappa(a(s)\sin u)B(u)$，故 (26)–(28) 正是原平尾的真实值和径向、角向一阶迹。

在固定 $\kappa(a_c\sin u)>0$ 的角度，(10) 进一步给 $b_s=O(r^2)$，(15) 的缺陷为 $O(r^2)$。在零曲率开弧内部，$b_s=O(r^{1/2})$ 一般不恒零。混合支撑边界由 (23)–(25) 支付，不用额外假定尾 $n>0$。

这是当前半径参考的特有端口性质。固定 cut 曲率径向延伸的 R157 参考一般不具有 (27)。本文既未要求 II 径向二阶连续，也未把上述参考的一 jet 结论升级成未知曲面的 $C^3$ 条件；真正的浸入仍须解相容方程。

## 6. 保存系数上的准确零平台初值

设原 mesh 为 $s_0<\cdots<s_N$，原 raw 系数为 $y_i$。选固定物理起点 $s_f=1.3$，终点取实体保存的 $s_+$。令
$$
\mu_i=1-S_5\!\left(\frac{s_i-s_f}{s_+-s_f}\right)
=S_5\!\left(\frac{s_+-s_i}{s_+-s_f}\right),\qquad
\widetilde y_i=\mu_i y_i.
\tag{29}
$$
第二式是 quintic 的准确对称恒等式，代码用它稳定评价靠近平台的微小乘子。$s_i\le s_f$ 时直接复制原数组，不作乘法；$s_i\ge s_+$ 时直接写入准确零。

新 raw 场是 $\mathrm{P1}(\widetilde y_i)$。**它不是**
$(1-\chi(s))\mathrm{P1}(y_i)$：插值与变系数乘法一般不交换。因此需要实际消费新的节点系数及完整字段；不能把淡出窗导数当作该 P1 场的径向导数。

对任一完整 cell $[s_i,s_{i+1}]$，若 $s_i\ge s_+$，则两端新系数均为零，其完整 P1 修正恒零。第 2 节因而适用于整个 cell 和全部角度，不只是节点。共同标量乘子保留原每节点齐次系数关系，包括已满足的 trace gauge $n_{\rm raw}=-l_{\rm raw}$。中央非齐次条件和 coast 消元节点在 $s_f$ 之前，原字节保持；cut 原本的零修正也保持。

物理参数向量 $p$、profile bump、mesh、atlas、原 lifting、R153/R155 窗和所有方程全部不改。变化仅在初始 raw 系数。因此这是**同一物理度量和同一表示内的新初值**，不是原场的同函数加密，也不是新约束或求解门。较早淡出及窗上升区的真实残差必须重新计算；该初值是否更好由相同目标上的实际比较决定。

## 7. 可消费接口和一次真实小域检查

最小 helper：`scripts/fd2d_gc_existing_tail_reference.py`，SHA256
`4b7ce10e568521ec7fe92ed23d0f8b1d947671aa9278fc63f631d007241bd2cf`。

- `zero_tail_plateau_corrections(mesh, corrections, fade_start=1.3, plateau_start=...)` 返回 `corrections / weights / info` 三键；`weights` 是实际节点乘子，上游为 $1$、平台为 $0$。
- `existing_tail_reference` 返回 (4) 的值和角 jet。
- `existing_tail_reference_interior` 返回 (9)–(15)，只在内部 $K>0$ 使用真实 $K_s$。
- `existing_tail_exact_cut_jet` 直接给 (26)–(28)，包括全部零曲率点，不对 $h=0$ 求商。

驱动 `scripts/fd2d-existing-tail-zero-initializer-check.py` 消费真实已闭输入
`notes/2026-11-12-fd2d-raw-bump-interior18-b0003-accepted-0002.npz`，
SHA256 `cef8525a79fe63f1f63b1f2521641612509b32c358a3be9f7b17c153e20dd82c`。
该输入有 $123$ 个节点、raw/central $K=15$、$16$ 个尾参数及 $7$ 个 profile 参数。
节点 $119$ 起准确零，完整 cells $119,120,121$ 满足第 2 节的恒等式。所有原非 `corrections` 数组逐字节相同，所有上游未淡出 raw 字节相同。

真实调用 **33360**，初始 chunk **4e8927**、最终 **16944b**，自然 exit **0**；脚本实测 $0.203$ 秒、最大 RSS $63880$ KiB。报告为
`notes/2026-11-12-fd2d-existing-tail-zero-18b3-01-report.json`，
新初值为 `notes/2026-11-12-fd2d-existing-tail-zero-18b3-01-field.npz`，
SHA256 `282196613cc8e16232164bd5c858fc1c7564d2a4d0bd21527c793f42977abb69`。

独立标量度量/非恒权重的 $561$ 个有限点，径向、角向和 Codazzi 公式差分误差分别不超过
$3.992\times10^{-11}$、$6.296\times10^{-11}$、$6.359\times10^{-11}$。
真实尾参数的局部参考与既有 R155 完整正迹直接求值差不超过
$3.331\times10^{-16}$，角 jet 差不超过 $1.666\times10^{-16}$；
准确平尾径向 jet 的有限算术差不超过 $1.111\times10^{-16}$。

局部有限样本的形式主曲率最大约 $.791571$，点态 Codazzi 最大仍约 $66.55394$。
这些只是实现诊断，严格全角形式曲率预算来自 (6)–(8)。本次未组装或评价完整 BVP 目标/Jacobian，未执行求解、body、全域几何或完成标准检查。

随后数值代理另用已闭 **19 b3** 真态，在同一实际参数 $p$ 和同一完整有限目标上比较原场与 (29)。该次 **13646 / 6f60da** 自然 exit **0**，报告
`notes/2026-11-12-fd2d-tail-fade-whole-choice01-report.json`。
输入 SHA256 为 `ac8bad448e55e8b3f4d565c4717c1d48f09e992591e415cdb6159018fa992714`，
与本节前面的 18 b3 小域输入不同。完整目标范数从 $8.490178$ 增为 $143.502127$，raw 残差最大值从 $2.647027$ 增为 $107.484429$，所以这次初值不替换主线。
这是该明确淡出选择的真实失败；不否定本文局部恒等式，也不据此宣称同一度量不存在相容解。

参考：R132（非负 Bernstein 平尾）、R136（profile 准确定义）、R155（正迹及实际积分 Codazzi）、R156（真实三次末桥）、R157（固定 cut 的不同参考）、R158（独立的同函数角阶嵌套）。
