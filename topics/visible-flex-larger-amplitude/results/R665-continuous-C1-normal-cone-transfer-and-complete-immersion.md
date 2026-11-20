# R665：连续 C1 差、法线锥传递，以及077087的完整浸入

2026-11-20，Astra-larger-resume-24b2ab87-20261120；recover_evidence。

**状态：完整传递定理已证；真实077087场的全部922胞浸入已付。全体正支撑传递尚未付清，未由此宣布闭嵌入。** 本条给出保持完整解析lift的一阶差界，以及利用旧场正支撑、法线及半径界传给新场的准确公式。一次不建角网格的全922胞向外计算得到新场

$$|F_\phi\times F_s|\ge0.02225172>0,\qquad
|F_s|\ge0.86167286>0,\qquad
\rho\ge0.16574514795>0.\tag{1}$$

同时123胞的正支撑传递已通过，其余799胞的界不够正。本条如实保留这个范围：支撑下界为负只表示该界过松，并非发现真实几何支撑为负。

## 1. 同一准确闭合场和旧证书

基场为 R663 已付完整第一jet的0241场，新场为正谱残差Hessian首四步的077087场：

| 角色 | 完整 bundle | SHA256 |
|---|---|---|
| 基场 | curvature-qp-physical-h2-next-six.npz | 0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023 |
| 新场 | curvature-qp-spectral-hessian-four-step.npz | 077087b778921efd85e1b6bbe3b8389bd60f385e2de0e5a767b8f705bc847dc3 |

S/R的准确有理盒、原 $s_i=\alpha_iS+\beta_i$ 节点、宽度、全部binary自由两jet及准确派生端口的定义沿 [R662](R662-complete-closed-C0-difference-and-inherited-size-amplitude.md) 和 [R656](R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md)。J=923、M=160；没有改变节点或参考标量。派生 $T_j(0)=-2j c_j$ 仍按准确实线性式重建。

旧完整证书为 continuous-0241-complete-first-geometry-q2048-r1.json，SHA256
2bfe3a6e4371473e5b54e6b229a28facb2d9fba88e855d518287a5b780637125。
它为每个原胞提供全径向、全角的

$$|N_0|\ge w_0>0,\quad |V_0|^2\ge E_0>0,\quad
A_\beta X_0\cdot n_0\ge a_0>0,\quad |X_0|^2\le R_0^2,\tag{2}$$

其中 $V_0=F_{0,s}$、$T_0=F_{0,\phi}$、$N_0=T_0\times V_0$、$n_0=N_0/|N_0|$，
$A_\beta=\operatorname{diag}(1,1,\beta)$，本次 $\beta=1/4$。报告中的各胞下界独立有效，不假设最坏值在同一角度取得。

## 2. 原闭合式的一阶准确差

沿R656的同一旋转正交架，写

$$X=q+f e_r(\delta)+\chi H e_z,$$

$$V=q_s+f_s e_r(\delta)+\chi_sH e_z,\qquad
T=q_\phi+f\rho e_t(\delta).\tag{3}$$

这里 $e_r(v)=(\cos v,\sin v,0)$、$e_t(v)=(-\sin v,\cos v,0)$，
$\rho=1+\delta_\phi$。q关于 $\phi$ 的导数包括正交架转动；准确系数公式仍用R656的channels(order=1)，未只对标量系数的sine/cosine求导而漏架项。

因为两个场共用 S/R/w，f和$\chi$相同。定义全角核心差预算

$$d_\delta=\sum_{j=1}^M\left|{1-\nu_j^2\over\nu_j}\Delta c_j\right|,
\qquad d_\rho=\sum_{j=1}^M|(1-\nu_j^2)\Delta c_j|,
\quad\nu_j=2j.$$

由单位圆两向量的 Lipschitz 常数1，

$$|\Delta e_r|\le d_\delta,\qquad |\Delta e_t|\le d_\delta.$$

取 $\rho_*\ge\sup|\rho_0|$。恒等式

$$\rho_1e_t(\delta_1)-\rho_0e_t(\delta_0)
=(\rho_1-\rho_0)e_t(\delta_1)
+\rho_0(e_t(\delta_1)-e_t(\delta_0))$$

立即给

$$\begin{aligned}
|\Delta X|&\le Q_X+f_*d_\delta,\\
|A_\beta\Delta X|&\le Q_{\beta X}+f_*d_\delta,\\
|\Delta V|&\le Q_V+f_{s,*}d_\delta,\\
|\Delta T|&\le Q_T+f_*(d_\rho+\rho_*d_\delta).
\end{aligned}\tag{4}$$

这里 $f_*\ge\sup|f|$、$f_{s,*}\ge\sup|f_s|$；$Q_X,Q_{\beta X},Q_V,Q_T$ 是下节给出的准确有限角/径向多项式上界。$0<\beta\le1$ 使 $\|A_\beta\|=1$，解析lift的水平差也不受其缩放影响。

本次两个实际场的全部核心系数相同，所以源码准确取 $d_\delta=d_\rho=0$。完整闭合lift仍参与基场导数、以及 $\chi\Delta H$ 的差分；并不是因为核心不变就忽略高度闭合。

## 3. 先合并高度，再作径向/角系数包围

用R662的准确差两jet和原准确宽度，先构成每胞的 $\Delta q$ 的 quintic Hermite/Bernstein 控制点；对控制点取准确物理 s 导数得到 $\Delta q_s$。若遇lift断点，按准确断点限制到各piece；所有项升到共同degree6。

在相同控制点先合并

$$\Delta q_Z+\chi\Delta H,\qquad
\Delta q_{s,Z}+\chi_s\Delta H,\tag{5}$$

然后才取角系数绝对值。第二式特别避免把较大的 $\chi_s\Delta H$ 与补偿它的有限部分分别估计。

对每个degree6控制点，三个正交分量各取全部有限角系数的l1和，再取三个和的 Euclidean 范数；所有控制点中的最大值，借 Bernstein 基函数非负且和为1，给出整个piece、所有角的范数上界。对 $Q_{\beta X}$，先把Z分量控制点乘准确beta；对 $Q_T$，先按R656含架转动的角导数式重建系数。如此得到(4)中的四个Q。

这个过程没有径向采样间隙。它的松紧来自角系数l1，不影响其连续有效性。

## 4. 保留基场大项抵消的有限 Laurent 算法

法线差还需要基场连续 $V_*\ge|V_0|$、$T_*\ge|T_0|$。直接分别取 $q_s$ 与 $f_s e_r$ 的界会丢失闭合层中的大抵消。源码采取以下严格近似后合并方法，仅用它来求上界，不改变场。

令 $z=e^{2i\phi}$，$\delta=\sum_jd_j\sin(2j\phi)$。则

$$i\delta=\sum_{j=1}^M{d_j\over2}(z^j-z^{-j})$$

是实系数 Laurent 多项式。取固定 K=8，计算

$$P_K(z)=\sum_{n=0}^K{(i\delta)^n\over n!}.\tag{6}$$

实现用逐项向外卷积及除法，保存所有 $-KM,\ldots,KM$ 项，没有在递推中删除高频系数。

若 $D_\delta\ge\sup|\delta|$，沿真实线段的 Taylor 积分余项给

$$|e^{i\delta}-P_K|\le{D_\delta^{K+1}\over(K+1)!}=:\tau_K.\tag{7}$$

证明只需把 $e^{it}$ 作为实参数t的函数，其任意阶导数模恒为1。正负delta都沿长度 $|\delta|$ 的线段积分，因此(7)无需额外指数因子，也没有把复函数任意复方向的估计误用于实相位。

若 $P_K=\sum_{j=-KM}^{KM}b_jz^j$，所有 $b_j$ 实，则

$$\Re P_K=b_0+\sum_{j\ge1}(b_j+b_{-j})\cos(2j\phi),$$

$$\Im P_K=\sum_{j\ge1}(b_j-b_{-j})\sin(2j\phi).\tag{8}$$

把(8)的前M模分别与 $q_s$ 中 R/T 分量和同控制点的 $f_s$ 相乘后合并；Z分量同时合并 $\chi_sH_0$。其余第M+1至KM模不丢弃，分别取cos/sin系数l1和 $C_{\rm tail},S_{\rm tail}$。剩余二维向量范数至多

$$\sqrt{C_{\rm tail}^2+S_{\rm tail}^2}+\tau_K.\tag{9}$$

所以

$$|V_0|\le \Gamma_V+f_{s,*}
\left(\sqrt{C_{\rm tail}^2+S_{\rm tail}^2}+\tau_K\right)=:V_*,\tag{10}$$

其中 $\Gamma_V$ 是合并后有限控制点范数上界。

对T，先把完整有限多项式rho与(6)准确卷积，保留直到 $(K+1)M$ 的全部系数。把 $-\Im(\rho P_K)$、$\Re(\rho P_K)$ 的前M模与 $q_\phi$ 及f合并，对剩余系数作(9)的l1尾。解析余项再付 $\rho_*\tau_K$，即得完整 $T_*$。

所有这些余项均以三角不等式相加。有限Taylor式只是包围工具；最终上界覆盖完整 $\rho e_t(\delta)$ 与 $e_r(\delta)$，没有把它们改成有限带宽场。

## 5. 法线差和浸入传递

记(4)给 $d_V\ge|\Delta V|$、$d_T\ge|\Delta T|$。由准确叉积展开

$$N_1-N_0=T_0\times\Delta V+\Delta T\times V_0+\Delta T\times\Delta V,$$

故

$$|N_1-N_0|\le T_*d_V+V_*d_T+d_Vd_T=:\eta_N.\tag{11}$$

若 $\eta_N<w_0$，则

$$|N_1|\ge w_0-\eta_N>0,\qquad
|V_1|\ge\sqrt{E_0}-d_V.\tag{12}$$

第一式已足够证明带面的浸入；第二式提供可读出的独立速度预算。帽以原Cartesian圆盘图为正则图，原两jet匹配保持C²接合，镜像保持正则性，因此全部胞通过(12)并且核心角图rho正时，得到整个原闭C²球面映射的浸入。

## 6. 利用法线锥的正支撑传递

置 $t=\eta_N/w_0<1$，新旧单位法线夹角为theta。因为

$$N_1\cdot n_0\ge|N_0|-\eta_N>0,$$

有 $0\le\theta<\pi/2$。进一步

$$\eta_N^2\ge|N_1-N_0|^2
=(|N_1|-|N_0|\cos\theta)^2+|N_0|^2\sin^2\theta,$$

所以 $\sin\theta\le t$、$\cos\theta\ge\sqrt{1-t^2}$。

令 $a=A_\beta X_0\cdot n_0\ge a_0>0$，并把 $A_\beta X_0$ 分解成法向与切向部分。由于 $\|A_\beta\|\le1$，

$$|(A_\beta X_0)_\perp|\le\sqrt{R_0^2-a^2}
\le\sqrt{R_0^2-a_0^2}.$$

两个正数量替换的方向分别是 $a\ge a_0$、切向上界随a增加而减小；因此可以在同一式中安全使用 $a_0$。若 $d_{\beta X}\ge|A_\beta\Delta X|$，便有

$$A_\beta X_1\cdot n_1
\ge a_0\sqrt{1-t^2}-\sqrt{R_0^2-a_0^2}\,t-d_{\beta X}.\tag{13}$$

这比先套单位法线的粗全局Lipschitz常数更尖，但仍可能因为(11)独立取全角极值而松。

每个闭胞及piece都获得正的(13)，再加两帽准确支撑 $\beta H_1>0$，就可按R650的正定流投影证明新闭浸入为嵌入。只要仍有一个胞的(13)未正，这条传递本身便未完成闭嵌入证据；不以有限点几何screen替补。

## 7. 本次真实077087应用

所有基本运算采用R656/f512的逐步向外模型。准确同核心检查给 $d_\delta=d_\rho=0$。一次固定8阶 Laurent 预计算返回

| 量 | 向外上界 |
|---|---:|
| 基场phase全角l1 | 1.087463026103627 |
| 基场rho绝对值 | 4.614884783089363 |
| 完整circle Taylor余项 | 0.0000058609425633400215 |
| circle的第160模以外有限Fourier尾范数 | 0.0000000027580795179804637 |
| rho乘circle的相应有限尾范数 | 0.0000008956387569427686 |

先在旧支撑最弱的胞905进行一次必要试读，耗时0.366271821秒，得到

$$d_V\le0.0029093732926686344,\quad
d_T\le0.00008076769906253198,$$

$$t\le0.09316637265944384,\quad
|N_1|\ge0.08753259812669993,\quad
A_{1/4}X_1\cdot n_1\ge0.19567285025279657.$$

随后同源自然完成全922胞，耗时11.148901879秒，exit0，未建角网格、未作径向细分。完整返回有

$$\min|N_1|\ge0.02225172092081137,\qquad
\min|V_1|\ge0.8616728637946797,$$

$$\rho_1\ge0.16574514795307824.$$

Fraction比较给出(1)中的短有理下界。最大位置差为0.0060854566096215585；最大一阶差上界分别为 $d_V\le0.024512305769528297$、$d_T\le0.027175518270117424$。直接使用本次输入的旧第一jet报告中直径界，可另得新场 $D\le4.123843487633937$；这只是该输入证书的C0传递，不宣称是最新或最紧的直径预算。

全体正支撑传递没有通过。已正的原胞数123；未付799胞，区间为60–842及878–893。最坏是胞833：

| 胞833的项 | 返回 |
|---|---:|
| $T_*$ | 5.941479420715221 |
| $V_*$ | 1.5771291179951998 |
| $w_0$ | 0.19956576924992472 |
| $\eta_N$ | 0.17731404832911335 |
| $t$ | 0.8884993102552344 |
| 新法线长度下界 | 0.02225172092081137 |
| 式(13)下界 | −1.2730181798159173 |

它是无lift胞，所以提高Taylor阶不能修复此处的松界。实际差场仅改变0–12角模，基场的全角 $T_*$ 与最小法线长度却在不同角区取得；在(11)中分别取全角极值丢失了同一phi的rho相关性。这说明下一收紧应保留局部角相关性，而不是把本次已失败的全支撑结论写成成功。

报告明确为 complete_scope=true、all_covered_cells_paid=false、embedding_certified=false。完整浸入结论来自(12)及全部922胞正下界；支撑、嵌入、曲率、reach和度量精度没有混作同一结论。

## 8. 完整来源及复算

新完整小源 scripts/resume_20261120/fullclosed_C1_support_transfer.py，共14817字节，SHA256
ec21d8575ad2d121d04beaa2b7ebc1902c0b7604c0dfaf8777610ad27f616200。

| 依赖/输出 | SHA256 |
|---|---|
| R662完整C0/准确场reader | f3b5acf135589c2ad6f10c80bebf7dfdf919350d4b06e9dbb764ba2a2ca0ade0 |
| R656完整几何源 | 2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377 |
| 原严格区间核 | f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d |
| 准确同Hold节点报告 | fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692 |
| 新胞905报告 | 1800e42fa6ce7fc9d9471cda9bef33662c00fd6b17724375bd79cc2a10d5c13b |
| 新全922胞报告 | 48a5b6de8e13a0fc032863f2acdd1a77b82e7e90f8090bb7d30c5a0655bcf568 |

准确S/R有理盒及字段解释沿R662；新报告绑定同一个节点报告SHA及基场完整证书SHA。所有卷积、系数和、sqrt、法线锥公式均使用逐步向外基本算术，不依赖普通FFT误差猜测。Taylor和所有有限Fourier尾已显式支付，未在数值上省略。逐胞大raw只保存在scratch，完整小源、参数和准确输入身份公开。

令topic为本课题目录，work为仓库外重建目录：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python "$topic/scripts/resume_20261120/fullclosed_C1_support_transfer.py" \
 --base "$work/geometry_path/curvature-qp-physical-h2-next-six.npz" \
 --candidate "$work/geometry_path/curvature-qp-spectral-hessian-four-step.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --geometry-source "$topic/scripts/resume_20261120/fullclosed_geometry_interval.py" \
 --interval-source "$topic/scripts/parallel_20261117_arclength_interval_positive.py" \
 --difference-source "$topic/scripts/resume_20261120/fullclosed_C0_difference_interval.py" \
 --base-certificate "$work/root/continuous-0241-complete-first-geometry-q2048-r1.json" \
 --out "$work/recover_evidence/C1-077087-from-0241-full.json" \
 --cells all --taylor-degree 8
~~~

胞905先读的命令仅把cells设905并换报告名。后续若换真实候选，必须绑定新bundle并重新计算对应差；旧场的第一jet证书可合法继续复用。本文没有重跑旧0241全角第一jet覆盖，更没有启动新的全域曲率扫描。

公开源码路径均对应实际执行的同SHA字节；临时数组沿原输入链再生。纯位置输入若替代原诊断清单，计算语义保持，文件路径与输入清单SHA不冒称原raw报告逐字相同。
