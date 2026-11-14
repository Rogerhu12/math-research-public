# R745：原 p41 的有理 Hodge 基与完整有限 adelic 周期输入

日期：2026-11-14。状态：**下述原六维有理 Hodge 基、精确 Fourier 表、有限平移表、全部相对边端点及独立性证书已经公开 Actions 完成。** 本篇不声称周期值、原商映射、$\beta$ 坐标或高度已经算出。

公开运行 [43616027318](https://github.com/Rogerhu12/math-research-public/actions/runs/43616027318)，attempt 1，源提交 `1768f05c524e2e3d2e01822c0a4f376382c5e608`，在 `2026-11-14T16:31:22.617177+00:00` 成功结束。核心计时 $0.6536467099999754$ 秒。完整计算只在公开仓库 Actions 执行；R738 的原拓扑和 R735 的原目标模型均未重算。

## 1. 固定的原对象与结论

取
$$
p=41,\quad N=246,\quad n=42,\quad
\eta=e^{2\pi i/42},\quad \zeta=\eta^{14},\quad
s=1+2\zeta=\sqrt{-3},\quad \alpha=\sqrt[3]4>0,
\quad F=\mathbf Q(\eta+\eta^{-1}).
\tag{745.1}
$$
写 $\beta=\eta+\eta^{-1}$，并取实际六个系数嵌入
$$
\mathcal H=\{1,13,19,25,31,37\},\qquad
\sigma_h(\eta)=\eta^h.
\tag{745.2}
$$
它们固定 $K=\mathbf Q(\zeta)$，在实域 $F$ 上给出全部六个嵌入。
原 $p$-进标签取自 R717 已完成证书：$\eta$ 的剩余为
$\gamma=7+30\zeta\in\mathbf F_{41^2}$，其阶为 42，且
$\gamma^{14}=\zeta$。所有角色、有限向量和 Fourier 系数都使用这一标签。

源是 R616/R738 的原 $X_1$，满足 $j=6912a^3(1-a^3)$，亏格 400。
R738 的同一左 coset 标记给
$$
c_1=4424,\quad k(c_1)=C,\quad
g_*=\begin{pmatrix}15130&123\\123&1\end{pmatrix},
\qquad c_0:\{2876,2822,2823\}.
\tag{745.3}
$$
$g_*$ 在 $p,3$ 处为恒等、在 2 处为 $C$。原实点 $c_1$ 的解析代表是
$g_*\zeta$；参考 coset 0 上 $a=\zeta$，不能将其误标为 $a=1$。

本篇的六个微分准确为
$$
\boxed{
\omega_j=2\pi i\alpha s\sum_{h\in\mathcal H}
 \sigma_h(\beta)^j\mathcal F_h(\tau)\,d\tau,
\qquad 0\le j\le5,
}
\tag{745.4}
$$
其中 $\mathcal F_h$ 是下面定义的原 Cartan 平均。
它们构成 $q_1^*H^0(A_{\theta,1},\Omega^1)$ 的一个 $\mathbf Q$-基。
计算给出它们在同一宽度 246 尖点的 $Q=e^{2\pi i\tau/246}$ 展开至指数 800，
以及 40 对准确 adelic 平移在全部 819 条原相对边上的端点。

## 2. 原角色、newform 与未改归一的平均向量

对 $y\ne0\in\mathbf F_{41^2}$ 定义
$$
\theta(y)=\eta^{-\log_\gamma(\bar y/y)},\qquad
\theta_h=\sigma_h\theta.
\tag{745.5}
$$
因而 $\theta(\zeta)=\zeta^{-1}$、$\theta(s)=-1$。原 newform 的系数为
$$
a_{m,h}=\sum_{\substack{z\in\mathbf Z[\zeta],\ z\equiv1\ (3)\\
 N z=m,\ (m,3p)=1}}z\theta_h(z),\qquad
f_h(\tau)=\sum_{m\ge1}a_{m,h}e^{2\pi im\tau}.
\tag{745.6}
$$
primary 条件对每个与 3 互素的理想恰选一个生成元，所以没有额外的 $1/6$。
写 $z=a+b\zeta$ 时条件是 $a\equiv1,b\equiv0\pmod3$。
其真实 newform 层为 $9p^2=15129$。共轭理想配对给 $a_{m,h}\in F$。
输出保留 $m=0,\ldots,800$ 的全部精确 $\Phi_{42}$ 坐标；本次前缀包含 325 个 primary 格点项。
源码同时检查 $a_1=1,a_2=0,a_4=-2$，原 $m\equiv1\pmod3$ 支撑、$a_{pm}=0$，以及前缀范围内的 $a_{4m}=-2a_m$。

使用 R588/R592 的有限左模型
$$
V=\mathbf Q(\eta)^{\mathbf F_p}/\mathbf Q(\eta)\mathbf1,
\qquad G(e_r,e_t)=p\delta_{rt}-1.
\tag{745.7}
$$
原 Weyl 公式和原非分裂环面代表为
$$
\rho(w)e_r=-\frac1p\sum_{y\ne0}\theta(y)e_{rNy+\operatorname{Tr}y},
\qquad
t_b=\begin{pmatrix}b&-1\\1&b+1\end{pmatrix}.
\tag{745.8}
$$
直接 Bruhat 分解给
$$
\rho(t_b)e_r=-\frac1p\sum_{y\ne0}\theta(y)
e_{(b^2+b+1)((r+b+1)Ny+\operatorname{Tr}y)+b}.
\tag{745.9}
$$
因此此次精确生成
$$
u=A_{\mathsf T_\zeta}e_0
=\frac1{42}\left(e_0+\sum_{b\in\mathbf F_{41}}\rho(t_b)e_0\right)
=\sum_{r=1}^{40}\frac{c_r(\eta)}{1722}e_r.
\tag{745.10}
$$
输出的 $c_r$ 是次数小于 12 的整数多项式，按 $\Phi_{42}$ 约化；$c_0=0$
只是在 $\sum e_r=0$ 中统一减去零坐标，没有改变平均的标量。
所有坐标的实性、真实环面生成元不变性和原正规化子
$\left(\begin{smallmatrix}-1&-1\\0&1\end{smallmatrix}\right)$ 不变性均由精确等式核验。

同一批有限和同时输出原完整范数
$$
N_1=42G(u,u),\qquad N_1\bmod41=40=-1.
\tag{745.11}
$$
该 $N_1$ 的全部 12 个整数坐标保存在系数 artifact 中，供其他原通道直接复用。
这里的模 41 陈述使用 (745.1) 的指定嵌入；没有声称所有共轭 $N_h$ 都是单位。

## 3. $\alpha s$ 与 $c_1$ 的一次相位运输

先在参考解析标记取
$$
H_0^\circ=f_h(\tau/246),\qquad H_2^\circ=f_h(4\tau/246),
\qquad v=(1,-\zeta^2)^{\mathsf t}.
\tag{745.12}
$$
在 $(H_0^\circ,4H_2^\circ)$ 的系数列上，原纯 2 层右 slash 为
$$
S_2=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
T_2=\begin{pmatrix}-1&0\\-1&1\end{pmatrix}.
\tag{745.13}
$$
原纯 3 层平移乘 $\zeta$，而 $Q_8$ 核中的 $S_3$ 作用平凡。
右 slash 的矩阵次序给 $(T_2S_2)v=\zeta^2v$，故几何 graph 的 $(C,T_3)$ 固定该线。
完整算术 graph 的行列式 $-1$ 元素还要施加 $\zeta\mapsto\zeta^2$，准确有
$$
T_2\bar v=-v,\qquad \bar s=-s.
\tag{745.14}
$$
因此规范算术线是 $s(H_0^\circ-4\zeta^2H_2^\circ)$。
R575 的原正三次扭曲再要求乘 $\alpha$，得到 (745.4) 的准确 $\alpha s$。

$p$ 处采用 R742 §3 的完整算术作用：经典右 slash 对应有限左作用的逆，
包括 $\zeta_p\mapsto\zeta_p^d$ 所对应的 $e_r\mapsto e_{dr}$。
于是 (745.10) 的真实正规化子不变性给出算术下降，而非只给复解析的不变性。
对 $F/\mathbf Q$ 取 (745.4) 的迹，即得六个有理微分。
原 tame graph 和非分裂正规化子的局部不变空间均为一维；原 newform 的 multiplicity one
识别其张成空间为 R616 的实际原本原因子 Hodge 空间。

由 (745.3)、(745.13) 有
$$
(H_0^\circ-4\zeta^2H_2^\circ)|_2g_*
=\zeta^2(H_0^\circ-4\zeta^2H_2^\circ).
\tag{745.15}
$$
因此全局 Fourier 和周期表使用参考函数，计算 $c_1$ 值时在 $g_*\zeta$ 求值，
或先作这一次 slash 再在 $\zeta$ 求值。不得再重复乘 $\zeta^2$。
$c_0$ 的原纯 2 层反射把 $v$ 送至 $(-\zeta^2,1)^{\mathsf t}$，与 R586 一致。
这些标量固定的是实际微分空间，并不预先给 Néron 整格或商映射的单位比例。

## 4. 已返回的 Fourier 表与独立性证书

取唯一 CRT 代表
$$
0\le k_r<246,\qquad k_r\equiv0\pmod6,\qquad k_r\equiv r\pmod{41}.
\tag{745.16}
$$
原有限模型的第 $r$ 项是 $H_{i,r}^\circ(\tau)=H_i^\circ(\tau-k_r)$。
若 $\xi=e^{2\pi i/41}$，其绝对 Fourier 相位为 $\xi^{-mr/6}$，指数中的 $6^{-1}$ 在 $\mathbf F_{41}$ 中取值。
定义整数迹
$$
U_{j,m,r}=\operatorname{Tr}_{F/\mathbf Q}(\beta^j a_{m,1}c_r),
\qquad P_{j,m}(\xi)=\sum_{r=1}^{40}U_{j,m,r}\xi^{-mr/6}.
\tag{745.17}
$$
本次生成的完整表准确实现
$$
\boxed{
\omega_j=\frac{246\alpha}{1722}
\left(\sum_{m\ \mathrm{odd}}sP_{j,m}(\xi)Q^m
 +\sum_{4\mid m}3P_{j,m}(\xi)Q^m\right)\frac{dQ}{Q}.
}
\tag{745.18}
$$
无 $m\equiv2\pmod4$ 项。因 $1+2\zeta^2=-s$，原 $a_{4m}=-2a_m$ 正好给第二类系数的 $-s^2=3$。
微分中的 $246$ 来自 $2\pi i\,d\tau=246\,dQ/Q$，不可与 raw 函数归一混淆。

实际独立性证书选
$$
\ell=739,\qquad \xi\mapsto538,\qquad s\mapsto98,
\qquad (m_1,\ldots,m_6)=(1,4,7,13,16,19).
\tag{745.19}
$$
其中 $538$ 阶恰为 41，$98^2=-3\pmod{739}$。去掉每行 (745.18) 中非零公共因子后的精确矩阵为
$$
\begin{pmatrix}
49&255&145&540&725&465\\
632&53&643&255&4&463\\
27&81&710&395&98&404\\
179&663&247&334&518&291\\
194&300&647&273&405&212\\
285&717&256&195&551&357
\end{pmatrix},\qquad \det\equiv407\ne0\pmod{739}.
\tag{745.20}
$$
所以 (745.4) 在特征零线性独立。它们已位于六维原 Hodge 空间，故确为其基。
此证书是公开输出，不是本地另算的行列式。

指数 800 的前缀也有原曲线上的确定性意义：非零全纯微分在亏格 400 曲线的零点总次数是 798。
若其 Fourier 函数的指数 $1,\ldots,800$ 全零，微分在此尖点至少有 800 阶零，矛盾。
这里没有换用其他层曲线的 Sturm 界。

同一输出还固定原源坐标的展开。若 $u=a/\alpha$，则
$$
u^3=\frac18-\frac{sE_6}{576\eta_{\mathrm{Ded}}^{12}},\qquad
\frac a\alpha=\frac{s}{12}Q^{-41}
\left(\frac{E_6(Q^{246})}{\prod_{m\ge1}(1-Q^{246m})^{12}}+24sQ^{123}\right)^{1/3},
\tag{745.21}
$$
括号根取常数项一。沿 $\tau=-1/2+iy$ 从尖点到 $\zeta$ 的相位固定这一支，参考点的值是 $a=\zeta$；
经原 $g_*$ 后为 $a=1$。源码逐项检查有限展开的立方恒等式，未改原粗参数 $a$。

## 5. 完整的 80 平移、819 边和端点输入

定义准确正行列式矩阵
$$
A_r=\begin{pmatrix}1&-k_r\\0&246\end{pmatrix},\qquad
B_r=\begin{pmatrix}4&-4k_r\\0&246\end{pmatrix}.
\tag{745.22}
$$
原 weight-two determinant slash 给
$H_{0,r}^\circ=246(f_h|_2A_r)$、$H_{2,r}^\circ=246(f_h|_2B_r)/4$，所以
$$
\boxed{
\omega_j=\frac{\alpha s}{7}
\sum_{h\in\mathcal H}\sum_{r=1}^{40}
\sigma_h(\beta^j c_r)
\left(A_r^*(2\pi i f_h\,d\tau)-\zeta^2B_r^*(2\pi i f_h\,d\tau)\right).
}
\tag{745.23}
$$
$246/1722=1/7$ 仅来自所显示的原平均分母和微分拉回因子。

对 R738 保存的每个原正向 Manin 矩阵
$g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，输出四端点
$$
A_rg0=\frac{b-k_rd}{246d},\quad
A_rg\infty=\frac{a-k_rc}{246c},\quad
B_rg0=\frac{4(b-k_rd)}{246d},\quad
B_rg\infty=\frac{4(a-k_rc)}{246c}.
\tag{745.24}
$$
它们精确约分，零分母记录为无穷；全部 40 对与 819 条原相对边已覆盖，去重后为 **87961 个有理端点**。
闭周期仍按 R738 的原 800 条整数闭链求有符号和，没有重新生成同调或改变交配。

若 $\lambda_h(t)=\Omega_0^{-1}\int_\infty^t2\pi i f_h\,d\tau$，对应括号是
$$
\lambda_h(A_rg\infty)-\lambda_h(A_rg0)
-\zeta^2\bigl(\lambda_h(B_rg\infty)-\lambda_h(B_rg0)\bigr).
\tag{745.25}
$$
R732 的完整 CM 核适用于这些原端点。此处已完成的是精确系数、矩阵、端点和符号；
尚未把 (745.25) 的代数值计算出来。随后可以利用同一有限表示的恒等关系压缩端点，而不能任意换一组周期。

## 6. 公开证书、全部文件绑定与可重建性

小文件目录：
`computations/R745-p41-original-Hodge-input/43616027318-1/`。
完整 artifact：`serre-global-R745-p41-original-Hodge-input-43616027318-1`。

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `p41-original-Hodge-input-certificate.json` | 1907 | `7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be` |
| `core-receipt.json` | 282 | `4038fdd9d50a3b33566cd739ac8d7b3f0bf379b58ece9822ceb30af4f21b083b` |
| `run-receipt.json` | 517 | `d57c4893024681d495a5da2e2d98a87df7fd4f0bb6c6f45338c9aff5b6d1da63` |
| `public-actions-input.json` | 3066 | `47b6a0d75bddcea8543f9d8e3a1bb7bb69899bf1db56c6beef71ad6a002e80a8` |
| `retained-topology-receipt.json` | 809 | `95c5fb1f6b0dfbd8eb41bbf912fd9eb440bccc308bbca625cdf86426d11e8b56` |
| `original-p41-Hodge-q-expansions.json.gz` | 78852 | `a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd` |
| `original-p41-Hodge-period-kernel-input.json.gz` | 658317 | `e86d39538c5b0b858fa92349a4f5b92fdbfc3e6fa3f5262b140f556a374b95e1` |

完整 manifest 的 SHA-256 是 `1c9aa2d9e05ad3722ef42151c5cbfabb3183d80f2c4ac1f9a0fc132bacfbaa51`。
两份可重建的大表仅保存在 artifact，其 SHA 和小证书入 Git。
系数表包括全部 $a_m,c_r,N_1$、六个 Fourier 表、原坐标分支和实际秩证书；
周期输入表包括原 80 个矩阵、六个嵌入上的精确系数、全部端点和原闭链引用。

执行源的精确 SHA-256：

| 源 | SHA-256 |
|---|---|
| `R745_p41_original_Hodge_input.py` | `48e8bb1189e39c0f0500be6b20da8a21e2788b5b73bdb9fea32d17540b144b4d` |
| `R745_public_Hodge_input.py` | `31851634280af3065fb41c445e921a14178de910ce3cd34de48c79997628446b` |
| `R745-p41-original-Hodge-input-method.md` | `911593aeaa0dd3f5d3ef577efbc2a448ba4c498224de81a3af5335b8f1c71329` |
| `R745-public-p41-Hodge-input-request.json` | `f5aa94f469849bf4e94a81d721e066bff13fd4796c7d5afd25cc24e6027619ed` |

原拓扑输入固定为 R738 run `43612108090`：两张完整表分别为
`6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161` 和
`d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf`，
小证书为 `a853f36bf5d6f7d238e805a5c2134b2f7b3db17528195d56d980e66c9c769009`。
原角色标签取 R717 run `43597163388` 的 2472 字节证书，SHA
`fb4d9ffadacda241575ab92a49f66819d8ac077ececa8f5151adf4aea3751fa6`。
输入凭据还逐一绑定 R575、R586、R592、R616、R732、R738、R742，以及执行时根和课题 README 的内容哈希。

## 7. 对后续原商计算的精确交付

本篇已把 R732 输入中的原有理 Hodge 基和全部 adelic 平移变成实际有限数据，
并与 R738 的整数闭同调、原 $c_0/c_1$、同一粗坐标和 R735 的目标模型相接。
实际周期值、由周期核求得的同态格、原 $q$ 的有理函数和 $q(c_1)-q(c_0)$ 坐标仍须继续计算。
原 Néron/Manin 比例、Poincaré 提升、Hodge splitting 和非 $p$ 局部修正仍按 R724 保留；
本次 Hodge 输入不替代那些真实高度数据，也不宣称 Serre 一致性完成。

## 依据

- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)、[R586](R586-actual-c0-marking-and-six-torsion-kernel.md)、[R592](R592-actual-integral-CM-jet-lattice-and-complete-tail.md)：原 tame 向量、有限模型、三次扭曲与两处标记。
- [R616](R616-original-CM-point-difference-and-explicit-height-basis.md)：实际原正因子与完整算术 graph。
- [R732](R732-original-CM-period-kernel-and-bounded-rational-function-recovery.md)、[R738](R738-certified-original-p41-period-input.md)：精确 CM 周期核及同一整数拓扑。
- [R742](R742-unramified-original-first-jets-and-depth-seven-Abel-isometry.md)：完整行列式作用和有限左作用/经典右作用的方向。
- [预运行方法](../notes/R745-p41-original-Hodge-input-method.md) 与本篇列出的公开原输出：全部新生成坐标及其验证。
- P. Mercuri–R. Schoof, *Modular forms invariant under non-split Cartan subgroups*, §§4–6，[作者稿](https://reneschoof.github.io/mcom3503.pdf)：原有限 cuspidal 模型与 Cartan trace。
- J. Brau–N. Jones, *Elliptic curves with 2-torsion contained in the 3-torsion field*, Theorem 1.4，[作者稿](https://homepages.math.uic.edu/~ncjones/2tin3t.pdf)：原 level-six graph 与 $j$ 模型。
