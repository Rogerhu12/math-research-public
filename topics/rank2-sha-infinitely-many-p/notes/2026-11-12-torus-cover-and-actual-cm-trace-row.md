# 真实环类迹的环面覆盖与第三次 deck 差分

日期：2026-11-12。状态：本篇的覆盖、完整轨道比较、函数域原始性和
指定 CM 纤维的精确检验均已证明。尚未证明该指定纤维检验对无穷多个
输入素数非零。本篇只处理 $E_{17}$ 的 $a_\ell=0$ 情形。

与本篇配套的[实际 Hecke 行及 Fourier 独立性证明](2026-11-12-actual-hecke-row-and-fourier-independence.md)
证明唯一常系数关系；本篇不重复其 q 展开与 Chebotarev 论证。

## 1. 固定范围和真正的几何 deck 群

固定
$$
 E:y^2=x^3-17x,\quad N=9248,\quad M=3N,\quad
 F=\mathbb Q(\sqrt{-15}).
$$
令 $p\ge13$ 在 $F$ 和 $\mathbb Q(i)$ 均分裂，并排除 R135
明确列出的固定模型、微分坏素数。取合法辅助素数 $\ell$：
$$
 \ell\equiv-1\pmod{1020},\qquad
 \ell+1=pu,\quad p\nmid u.
 \tag{1}
$$
特别地 $u$ 为偶数，$a_\ell(E)=0$。记 $k=\overline{\mathbb F}_p$。

在固定 Weil 配对分量的细模曲线 $X(M)$ 上，真正的 full
$\ell$-level 覆盖 $\widetilde X=X(M\ell)\to X(M)$ 的几何群是
$\mathrm{SL}_2(\mathbb F_\ell)$。因为基底已经带有细 $M$-level，
此处不能未经说明直接写成 $\mathrm{PSL}_2$。

所有以下函数只依赖循环阶 $\ell$ 子群，因而对 full
$\ell$-level 的中心 $\{\pm I\}$ 不变。明确取中心商
$$
 X=\widetilde X/\{\pm I\},\qquad
 G=\operatorname{PSL}_2(\mathbb F_\ell).
 \tag{2}
$$
这里的 $-I$ 只改变 $\ell$-level，保持 $M$-level。
这与把所有 level 同时取负的模问题不同。

令 $h=h_{p,\mathrm{old}}$ 为 R135 的真实权零函数
$$
 h=\frac{\bar H_p+V_3\bar H_p}{\mathrm{Ha}_p},
 \qquad H_p=\theta(\psi_E^{p-2}).
 \tag{3}
$$
对每条 $v\in\mathbb P^1(\mathbb F_\ell)$，将它视作源椭圆曲线的
循环阶 $\ell$ 子群 $C_v$，定义
$$
 h_v=h(E/C_v,\text{运输的 }\Gamma_0(M)\text{ 标记})\in k(X).
 \tag{4}
$$
由于 (3) 是权零函数，(4) 没有任意选择目标微分造成的倍数。
目标 full $M$-level 的 Weil 配对可变为原配对的 $\ell$ 次方；
(3) 已下降至 $X_0(M)$，所以该变化不改变定义。

取函数上的群作用约定，使 $g h_v=h_{gv}$。
相邻 Fourier 稿证明：
$$
 \ker\bigl(k^{\mathbb P^1(\mathbb F_\ell)}\longrightarrow k(X),
                   (c_v)\mapsto\sum c_vh_v\bigr)
                   =k\,(1,\ldots,1),
 \qquad \sum_vh_v=0.
 \tag{5}
$$
最后一式是原 $a_\ell(E)=0$ 的准确几何 Hecke 关系。
为核对权重，尖点处的无权几何迹为
$\ell U_\ell h+V_\ell h$；由于
$a_\ell(H_p)\equiv a_\ell(f)/\ell$、
$\ell^{p-2}=\ell^{-1}$，它正等于 $a_\ell(f)h$，而非任意另选的
Hecke 规范。旧形式的两退化项保持同一关系。

## 2. 两条半环面轨道及原来的完整 $U$ 迹

令
$$
 T\simeq\mathbb F_{\ell^2}^{\times}/\mathbb F_\ell^{\times}
       \subset\operatorname{PGL}_2(\mathbb F_\ell)
$$
为一个 nonsplit 环面。$T$ 的阶为 $\ell+1=pu$，在
$\mathbb P^1(\mathbb F_\ell)$ 上正则作用。其与 $G$ 的交为
$$
 T_0=T\cap G,\qquad |T_0|=(\ell+1)/2.
 \tag{6}
$$
因此 $T_0$ 有且只有两条轨道，每条长度 $(\ell+1)/2$。

取 $U\subset T$ 为唯一阶 $u$ 子群，并令
$$
 U_0=U\cap T_0,\qquad |U_0|=u/2.
$$
若 $t$ 生成 $T$，则 $T_0=\langle t^2\rangle$、
$U=\langle t^p\rangle$、$U_0=\langle t^{2p}\rangle$。
对任意 $v_0$ 有准确的不交并
$$
 Uv_0=U_0v_0\ \sqcup\ U_0t^pv_0.
 \tag{7}
$$
两部分分别落在两条 $T_0$ 轨道中；没有只保留其中一半。

包含映射诱导同构
$$
                T_0/U_0\xrightarrow{\sim}T/U\simeq C_p.
 \tag{8}
$$
故可把 (8) 中的生成元选成原算术 $\Gamma$ 的指定生成元。
若先写 $t^2$，它在 $T/U$ 中通常对应原 $t$ 的平方；不能不加
说明把这两个生成元的矩权逐项视为相同。下文的 $\tau$ 总按 (8)
与实际算术作用匹配。

定义
$$
 B_\ell=\sum_{v\in Uv_0}h_v
        =\sum_{v\in U_0v_0}h_v+
                       \sum_{v\in U_0t^pv_0}h_v.
 \tag{9}
$$
它是 $U_0$ 不变函数，因而下降至
$$
 Y=X/U_0,\qquad Z=X/T_0,\qquad Y\longrightarrow Z.
 \tag{10}
$$
原函数 $h$ 已包含类数二的两项 $\Phi=\pi d_1+\pi d_3$。
所以 (9) 的 $u$ 个 $h_v$ 正对应原 Heegner 点的 **$2u$ 个项**，
不是把类群迹除以 $2$。

## 3. 这是处处 étale 的真实 $C_p$ 覆盖

(10) 的群是 $\Gamma=T_0/U_0$，次数为 $p$。
在开模曲线上，素于 $p$ 的 full $\ell$-level 是 étale；细
$M$-level 消除了椭圆点稳定子。中心商及子群商的相应相对覆盖
仍 étale。

在尖点处，$X\to X(M)$ 的惯性群为阶 $\ell$ 的单幺群。
由于 $\ell\nmid|T_0|$，其与 $T_0$ 的交为平凡，故 (10)
在尖点也没有惯性。这证明 (10) 在紧曲线上处处 étale，尽管
其次数正等于剩余特征 $p$。

由 (5)、(7)，
$$
 N_\Gamma B_\ell:=\sum_{j=0}^{p-1}\tau^jB_\ell
             =\sum_{v\in\mathbb P^1(\mathbb F_\ell)}h_v=0.
 \tag{11}
$$
这里是函数域上的恒等式，不只是所选 CM 纤维中的偶然零值。

## 4. 实际全局行恰处在第一增广层

在特征 $p$ 中置
$$
 \Delta=\tau-1,\quad
 D_1=\sum_{j=0}^{p-1}j\tau^j,\quad
 D_2=\sum_{j=0}^{p-1}\binom j2\tau^j.
$$
直接对 $(T^p-1)/(T-1)=(T-1)^{p-1}$ 微分，得
$$
 N_\Gamma=\Delta^{p-1},\qquad
 D_1=-\tau\Delta^{p-2},\qquad
 D_2=\tau^2\Delta^{p-3}.
 \tag{12}
$$
在每个 $U$-轨道块 $\tau^jUv_0$ 中，$D_1B_\ell$ 的系数为
$j$，$D_2B_\ell$ 的系数为 $\binom j2$。前者的 $j=0,1$、
后者的 $j=0,2$ 给不同系数；由 (5)，两函数均非零。

令 $K=k(Y)$、$K_0=k(Z)$。正常基定理给
$K\simeq K_0[\Gamma]$ 作为 $K_0[\Gamma]$ 模。
因而 (11)--(12) 给完整结论
$$
 \boxed{\quad
 B_\ell\in\Delta K\setminus\Delta^2K,
 \qquad D_2B_\ell\ne0,\quad
 \Delta D_2B_\ell=-D_1B_\ell\ne0,\quad
 \Delta^2D_2B_\ell=0.
 \quad}
 \tag{13}
$$
也就是说，原来的函数本身已经是全局原始的第一增广层；
其第二矩行的 deck Jordan 长度准确为 $2$。
这比仅知某个环境模允许非零更强。

同时，任意 $b\in K$ 都满足
$$
                  D_2b=0\iff b\in\Delta^3K.
 \tag{14}
$$
(14) 是正规模 $K_0[\Delta]/(\Delta^p)$ 的核计算。
因此 (13) 确实排除实际 $B_\ell$ 为全局第三次 deck 差分。
这里的 $\tau-1$ 与绝对 Frobenius 的 $x\mapsto x^p-x$
不是同一个算子。

由相邻稿的极点证明，$D_1B_\ell$、$D_2B_\ell$ 在相应紧曲线
上只有简单超奇异极点，且均有真极点；因而它们也都不是相应
函数域的 untwisted Artin--Schreier 像。这与 $B_\ell\in\Delta K$
不矛盾。

## 5. 原 CM 纤维：标记、类群和、常数扩张都保留

本节先采用同一 prime-to-$p$ level 模问题及其群商的特征零模型，
以及所选 $p$ 处的整模型，仍以 $X,Y,Z$ 记之。下面的 CM 点先在
该特征零模型上构造；在好约化处约化后，回到前述
$k=\overline{\mathbb F}_p$ 上的曲线。因而下文 $Z(F')$ 的 $F'$
是数域，不是将数域点直接写在特征 $p$ 曲线上。

从 R105 的实际最大阶 CM 源点出发，其端环为 $\mathcal O_F$，
并带有原 $\Gamma_0(3N)$ 标记。因为 $\ell$ 在 $F$ 惰性，所有
$\ell+1$ 个阶 $\ell$ 子群给出导子 $\ell$ 的 CM 邻点。
环类群的准确相对商为
$$
 \operatorname{Gal}(F[\ell]/F[1])
 \simeq(\mathcal O_F/\ell)^{\times}/\mathbb F_\ell^{\times}
 \simeq T.
 \tag{15}
$$
这是 R114 的原邻点/CM 互反标记：$T$ 在邻点上正则作用。
由 R105 的实际阶二提升 $\tau_3$，
$$
 X_v=\Phi(z_v)=(1+\tau_3)P[\ell]_v,
 \qquad Q=\sum_{v\in Uv_0}X_v.
 \tag{16}
$$
所以 (9) 在此标记上的值正是 R135 的原完整 $2u$ 迹，逐项相同。

为使用固定 Weil 配对及细 level，可以作素于 $p$ 次数的常数
扩张，但不许删除 (16) 中的项。具体如下：

- $F[1]/F$ 的次数为 $2$；
- 固定 $M=3N$ 的 full level 扩张的群嵌入
  $\mathrm{GL}_2(\mathbb Z/M)$，其阶只含 $2,3,17$；
- 添入 $\mu_\ell$ 的次数整除 $\ell-1$，与 $p$ 互素；
- full $\ell$-torsion 的 CM Cartan 商与 (15) 的差由 scalar
  部分给出，阶整除 $\ell-1$。若还需固定该部分的标记，也只作
  $p$ 素次数扩张。

在 CM Cartan 的阿贝尔 torsion 扩张中再固定全部 $p$ 素部分，
所剩的 $p$ 部分正是 (15) 的唯一 $C_p$ 商。
因此存在一个 $p$ 素次数扩域 $F'/F$，使所选点
$z_{\rm CM}\in Z(F')$ 的 (10) 纤维，作为 $\Gamma$-torsor，
与 $LF'/F'$ 相同；$L/F$ 是原 R113 的度 $p$ 环类子扩张。
可在选定好约化处完成这个比较。全部所用 prime-to-$p$ torsion
和环类扩张在 $p$ 不分歧。

其含义是几何模型保留了原 $C_p$ 纤维，而不是重新选择一个
未知的度 $p$ 扩张。非零与零在这些常数扩张下均忠实保持。
若残数常数扩张次数为 $f$，则相对 Frobenius 变为原 $s^f$；
原算术生成元及 R135 的绝对 Frobenius 公式，应先在原半局部模
写好，再作基变换，不能混用 $s$ 与 $s^f$。

## 6. 第三次差分的实际特化，及仍须支付的箭头

源点是 ordinary CM 点，且 prime-to-$p$ 同源保持 ordinary。
因此 (9)、(13) 的所有函数在原 CM 纤维均正则。
取该纤维的有限 étale 半局部代数 $\mathcal P$；它可能是一域，
也可能完全分裂。两种情况下正常基都给
$\mathcal P\simeq k_0[\Gamma]$，其中 $k_0$ 是基点的有限剩余域。
求值与每个 deck 群环算子相容。

采用 R135 的微分规范 $\omega_0=c_\pi^{-1}\omega_E$，在原
$p$-半局部模中置 $z_0=\log_0(Q)/p$。其整性及全部位的规范
已由 R134--R135 付清。R135 的真实取值公式给
$$
 B_\ell\big|_{\rm CM}=-\bar a_p\,s\bar z_0,
 \tag{17}
$$
其中 $s$ 是 $p$ 上算术 Artin 元。右边的 $-\bar a_p s$ 为
可逆群环算子，与 $D_2$ 交换；必要时在上节的 $p$ 素常数扩张
后解释 (17)。故
$$
 \boxed{\quad
 D_2(B_\ell|_{\rm CM})\ne0
 \iff D_2\bar z_0\ne0
 \Longrightarrow a\le1
 \Longrightarrow\Sha(E/\mathbb Q)[p^\infty]=0.
 \quad}
 \tag{18}
$$
这里最后两步准确引用 R130 的实际半局部格检验和 R125/R127
的整下降；没有从任意非零环境值推出原 $Q$ 的原始性。

若此检验失败，则实际有限纤维上准确有
$$
                   B_\ell|_{\rm CM}\in\Delta^3\mathcal P.
 \tag{19}
$$
全局 (13) 说 $B_\ell\notin\Delta^2K$；它不禁止 (19)。
还可将坏纤维写成两个真实行同时消失：
$D_1B_\ell$ 已下降至 $Z$，而
$\Delta D_2B_\ell=-D_1B_\ell$。若前者在基点不零，第二行不可能
在整个纤维为零；若前者为零，第二行在该纤维为常数，仍须检测
这个常数。

特别地，$Z\to X(M)$ 在固定源椭圆曲线上的全部几何 level 点
约有 $\ell^2$ 个，但原轨道只使用端环 $\mathcal O_F$ 指定的
CM 环面标记。其他任意环面标记不是本题原 Heegner 轨道，
不能把它们全部计为可用 CM 纤维，再以函数的零数界制造非零。

本篇实际留下的任务是：对无穷多个输入 $p$，在原合法辅助
$\ell$ 的 **指定 CM 标记** 上排除 (19)。唯一 Hecke 常关系、
函数域原始性和简单极点已经付清；这项特化原始性尚未付清。

## 依赖与来源

- R103、R105、R114：固定 $F=-15$、真实类数二映射、全部
  inert $\ell$-邻点及环类互反标记。
- R130、R134、R135：实际半局部第二矩、Coleman/Artin 规范、
  Buium--Poonen 的原 CL 取值等式及明确伴随函数。
- [实际 Hecke 行与 Fourier 独立性](2026-11-12-actual-hecke-row-and-fourier-independence.md)：
  (5)、非恒定性及简单极点；其常系数关系不是本篇新增假设。
- 覆盖的 étale 性和 (6)--(14) 在本篇直接证明。
  正常基只用于真实有限 Galois 函数域或有限 étale 纤维代数。
