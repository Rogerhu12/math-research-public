# WSS 同一修补族在全径向区间的两列有符号普通源

固定原 $\eta_0,\delta_*$，$Q=Q_0+\delta_*Z=(u,v)$、$\nu=\nu_0+\delta_*$、$Z=(a,b)$。研究对象为
$$
 f_N=F(Q,\nu)-Q_r,\qquad f_Z=F_\nu(Q,\nu)+D_QF(Q,\nu)Z-Z_r ,
 \quad 0\le r\le25/8.                                         \tag{WSS.1}
$$
下述实现定义同一真实条件下两列的完整逐格有向包围。原有 [GSR](R149-supplement-selected-signed-Newton-nu-and-whole-cell-Grassmann-response.md) 已给出正区两列的精确公式。此处补上全负区，包括真实 compact 参数微分、根 bracket 的两端以及每个原一侧导数。当前没有首次作业的科学结果。整域已知源大小的 [NHT](R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md) 可独立使用，未重新申请其谱尾或历史 norm targets。

取 $s=s_{\nu_0}$ 的原 rotational 解，$v=s+w$，$u,w$ 各含完整原修补和 $\delta_*Z$。两组 cubic 的原 physical 表达中，base65 只乘一次 $\alpha$，direction193 已为物理坐标。固定 $\nu_0$ 的真实 $G,K_0,\beta$ 及可动 $G_\delta,K_\delta$ 采用 [D.2](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)。写 $\chi=4096x^6(1-x)^6$，$x=(r-1/20)/(9/50-1/20)$，区间外 $\chi=\chi'=0$，$L=\beta\chi'/(2a_{\rm phys}^2 G^2)$。每个原 piece 给 $\chi,\chi'$ 的真实有向值，$a_{\rm phys},G$ 的原全行均须通过正下界。在同一 $\delta=\delta_*$ 写
$$
 \begin{aligned}
 \Delta K&=K_0(e^{-\delta\chi}-1)+\delta e^{-\delta\chi}L,&
 K_\delta&=K_0+\Delta K,& G_\delta&=G e^{\delta\chi/2},\\
 K_\nu&=e^{-\delta\chi}[L-\chi(K_0+\delta L)],&
 J_{\nu,12}&=G e^{-\delta\chi/2}[L-\chi(K_0+\delta L)/2],&
 J_{\nu,21}&=-G_\delta\chi/2 .
 \end{aligned}                                                   \tag{WSS.2}
$$
两行和的剩余两个对角元为零。程序在原完整参数球上包围这些 signed 量。$\Delta K$ 使用 $e^x-1$ 的稳定有向值，在 compact 外它及全部显式参数导准确为零。

记 $S=u^2+K_\delta v^2$、$D=-\beta I S$、$m=\Pi v$。原 $s'=\beta s(1-K_0s^2)$ 必须使用原 $K_0$。故 $f_N$ 的两行恰为
$$
 \begin{pmatrix}
 D u_\phi+G_\delta mK_\delta v_\phi-\beta u(1+S)-u_r\\
 D v_\phi-G_\delta m u_\phi+\beta[w-u^2v-K_\delta w(v^2+vs+s^2)-\Delta K\,s^3]-w_r
 \end{pmatrix}.                                                  \tag{WSS.3}
$$
径向导数先在每一侧的实际 cubic 内求，常值 signed repair 的逐 piece 历史偏移只进原函数值。第2行额外 $-\beta\Delta K s^3$ 保留改变后的算子与该固定 reference 的差。原 complete repair 给 proposal 的值连续；其本身的两侧普通源可不同。

$f_Z$ 先在同一个 $(Q,K_\delta,G_\delta)$ 上使用原 TC 的全 $D_QF$，包括 $I$, moving mean、独立的 $b$-mean rank，另加
$$
 -\beta K_\nu\big[I(v^2)(u_\phi,v_\phi)+v^2(u,v)\big]
 +m(J_{\nu,12}v_\phi,J_{\nu,21}u_\phi)-(a_r,b_r).              \tag{WSS.4}
$$
这是沿原 affine 参数曲线的**总导数**。在真根 bracket 及其右侧，用 GSR 对同一物理公式的参数幂分解，它准确利用 compact 已归零。这两个写法在所有 bump 外重合；没有改动角测度、原频率 $4j$ 或阶数。

全 $\phi$ 支集至 quarter-index288，$1024$ 点有向 FFT 与完整 radial polynomial、Wiener remainder 按原 TC 操作。采用完整正交实基 $\sqrt2\sin(4j\phi),1,\sqrt2\cos(4j\phi)$，每列含 288 odd、一个 independent even mean、288 even nonmean。全部 577×2 的有符号系数区间和各自两端的 one-sided source mean 写入同 job 私有完整文件；每次读回检查全部字节 SHA。程序保原 40 parts、7721 scalar 行、6144 个 cubic、真实根两端和两侧 cuts/compact 两缝，取准确有理共同细分，逐实际交段全覆盖。后继对某个真实 physical box 取所交每个 whole enclosure 的 union，最后才选择 193 个 low 行。跨作业若恢复，须匹配原完整科学结果的 index SHA、所有 piece bytes 和顺序；不公开新系数数组。

第二个新目标是上述两列的有符号径向 polarization
$$
 \int_W\langle f_N(r), f_Z(r)\rangle_{L^2_\phi}\,dr.
$$
分别用 $W=[0,25/8],[0,r_+],[r_-,25/8]$。每段先从敏感于符号的 complete signed carrier 全件读回，正交实基给全部577对积之和，整段长度乘相应真实有向区间再相加。真实参数一致而区间使用可允许依赖损失；该积分是包含而非任取区间端点之积的真值。后两窗口在根 bracket 重叠，未将其当作径向不交进行合并。本计算没有重算历史两个源的独立范数。原 signed source 的两个新目标都不解全 BVP；原 physical root-even、right Robin/mean、height 和高返回仍通过各自同一方程进入。

实现为 [两列公式和整件存取](../scripts/fourfold_codazzi_whole_selected_signed_source_carrier.py)、[独立 owner](../scripts/fourfold_codazzi_whole_selected_signed_source_owner.py) 及 [公共入口](../scripts/fourfold_codazzi_whole_selected_signed_source_public_worker.py)。四个单线程子进程最多八个在途 piece，按原序认证。即使停止，也保存已完成连续前缀、全部完整 chunk 及其后已完成的离散 piece 收据。没有产生源结果之前，不能仅凭此合同给其大小、源的有符号积分或实际 PDE 响应赋值。
