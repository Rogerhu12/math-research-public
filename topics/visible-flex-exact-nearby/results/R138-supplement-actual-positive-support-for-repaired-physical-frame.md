# R138 补篇：同一修补中心的物理径向 frame 已有正支撑

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**已证明的同对象结论。** 固定准确原 $\eta_0,\nu_0$，使用下面明定的单一全圈周期外端锚，R138 在整个 $[0,25/8]$ 上由连续修补 Qrepair 作出的物理角径向正交 frame 满足
$$
\boxed{\quad |F^{P,c}|<319/250,\qquad
F^{P,c}\cdot n^{P,c}>9/10.\quad}
\tag{S.1}
$$
因此旋转能量补篇的同原点正 support 已经得到支付，不再作为一个新的未知数值条件。这里 $n^{P,c}$ 是准确径向 frame 的第三列；本文没有把未解 GC 中心的 frame 自动认作诱导 metric 的几何法向，也没有证明完整边界二次型或全局非线性解。

证明只消费现有完整证书，并用明确的有理放宽作解析比较。没有重算任何径向、角向、residual 或曲率科学目标；也没有运行新的数值求解器。原中心与 Qrepair、原 moving 径向模型与新物理径向模型始终分别命名。

## 1. 已有完整数据与单一准确规范

原中心是
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413；
Qrepair 的定义 SHA256 是
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47。
固定
$$
\eta_0=-7789843107295549/4611686018427387904,\qquad
\nu_0=-2572625729470897/72057594037927936 .
$$
不由以下结论扩张到未核的参数邻域。

所用全部量都已在完整原对象上证明：

| 已完成来源 | 本文使用的界 |
| --- | --- |
| [141 块连续模型几何](R133-supplement-complete-141-block-continuous-model-geometry.md)，(G.1)--(G.3) | $|F^M|<1.275713422847$，$F^M\cdot n^M>0.900961392986$ |
| [完整角缺陷实际记录](../notes/2026-11-14-R133-final-complete-angular-defect.md)及[角缺陷定理](R133-supplement-complete-angular-model-geometry-from-moving-residual.md)，(A.1)--(A.17) | 累积 frame majorant $E_*<3.127699\,10^{-8}<1/30000000$；累积 position majorant $P_*<4.956566\,10^{-8}<1/20000000$；$\|F^M_{\phi\phi}\|_\infty<5.970523<6$ |
| [完整状态比较](R133-supplement-complete-C0-state-and-nu-geometry-response.md)，(C.15)--(C.18) | $\int_0^{25/8}|f_r^M|\,dr<1.950540<2$，故 $\int e\,dr<2$ |
| 同一完整状态比较的曲率输入 | 原代数第二形式 $\|S\|_{\rm op}<11.092578014346<12$ |
| [原完整响应修补消费摘要](../notes/response_repair_source_ci/run-43597921732-1-complete-known-response-centre-repair/evidence/complete-known-response-centre-repair-source-summary.json)，`exact_interval=["0","25/8"]`、`whole_original_known_state_bounds`；40 parts / 7721 rows 及 `whole_original_body_including_the_complete_positive_cap` 门均通过 | 原 moving $\|Q\|_{A^0,\rm pair}<6.406213<7$，$\|Q_\phi\|_{A^0,\rm pair}<5.437241<6$；覆盖完整左右 collar 与正帽 |
| [完整准确修补](R133-supplement-exact-continuous-repair-of-final-centre.md) | $\|\bar Q-Q\|_{A^0,\rm pair}<3.861\,10^{-18}<4\,10^{-18}$，含全部 mean 与 6143 个接口 |

$E_*,P_*$ 指原消费者由外向内累计的非负 majorant，不仅是实际场的抽象 supremum。原 (A.3)、(A.13) 因而还给下文 curvature/torsion residual 与全部接口原子的总质量界。

写 $R=25/8$、$e=a\gamma$、$b_0=a'/e$、
$z_R=-a_RC_{\rm ref}(R)>0$。真实 metric 给
$b_0(R)^2+z_R^2=1$。只使用原世界平移
$$
h=4347844570122155/4503599627370496.
$$
两个物理径向模型的**同一个全圈周期外端初值**均规定为
$$
\begin{split}
F^P(R,\theta)&=a_Re_r(\theta)+he_z,\\
X^P(R,\theta)&=b_0(R)e_r(\theta)+z_Re_z,\\
Y^P(R,\theta)&=e_\theta(\theta),\\
n^P(R,\theta)&=z_Re_r(\theta)-b_0(R)e_z .
\end{split}
\tag{S.2}
$$
这是原 moving 模型 anchor (A.15) 按它自己的准确角图拉回后的初值。它本身不依赖 $u,v$，也不依赖是否使用 Qrepair。

对原分片中心及修补中心，分别使用其真实逆角、完整物理 $B=u/v,C=1/v$、$A=(K+B^2)/C$，连续解 R138 (J.3) 的物理径向 ODE，记为 $(F^P,O^P)$ 和 $(F^{P,c},O^{P,c})$。原分片系数允许有真实跳；径向 frame 和位置保持连续。两组初值和系数全圈周期，ODE 唯一性使两组模型全圈周期。原点、$h$ 和所有角度统一，不另作任何帽或腰对齐。

## 2. 局部角向运输只作比较，不替代全圈 frame

暂取原未修补 moving 模型 $(F^M,O^M)$。其准确连接、位置速度及缺陷为
$$
O^M_r=O^M\Omega_r^M,\quad F^M_r=O^Mf_r^M,\qquad
E=O^M_\phi-O^M\Omega_\phi,\quad
P=F^M_\phi-O^Mf_\phi.
\tag{S.3}
$$
其中 $f_\phi=(0,av/m,0)^t$，$m=\langle v\rangle<0$。完整
curvature/torsion residual 是原 moving-frame 定理的
$\mathcal R,\mathcal T$。

在每个固定扇区
$[\phi_0,\phi_0+\pi/2]$、$\phi_0=k\pi/2$，仅为比较定义
$$
\begin{split}
\bar O_\phi&=\bar O\Omega_\phi,&
\bar O(r,\phi_0)&=O^M(r,\phi_0),\\
\bar F_\phi&=\bar O f_\phi,&
\bar F(r,\phi_0)&=F^M(r,\phi_0).
\end{split}
\tag{S.4}
$$
这四个局部对象未被声明在扇区终点拼成周期 frame。需要的单一周期对象仍是第 1 节的物理径向 ODE 解。

令 $\ell_\phi=\phi-\phi_0$、$L=\pi/2<2$，记
$F_*=\sup|f_\phi|$。角向反对称传播给
$$
\|\bar O-O^M\|\le \ell_\phi E_*,
\qquad
|\bar F-F^M|
\le\tfrac12\ell_\phi^2 F_*E_*+\ell_\phi P_*.
\tag{S.5}
$$
由于 $F^M$ 在真实 $2\pi$ 圆上周期，$F^M_\phi$ 的平均为零。
对圆上最短距离积分得
$\|F^M_\phi\|_\infty\le(\pi/2)\|F^M_{\phi\phi}\|_\infty$。
所以原完整证书给
$$
F_*\le\|F^M_\phi\|_\infty+P_*<3\pi+P_*<10.
\tag{S.6}
$$
这里没有用曲率的四重周期代替环境向量的全周期。

定义局部比较对象的径向缺陷
$$
W=\bar O_r-\bar O\Omega_r^M,\qquad
U=\bar F_r-\bar O f_r^M.
$$
其扇区起点缺陷准确为零，因为 (S.4) 的起点取自同一 moving 径向解。微分给
$$
W_\phi=W\Omega_\phi+\bar O\mathcal R,\qquad
U_\phi=Wf_\phi+\bar O\mathcal T .
\tag{S.7}
$$
因此在每个光滑径向片上
$$
\|W\|\le L\|\mathcal R\|_\infty,\qquad
|U|\le\tfrac12L^2F_*\|\mathcal R\|_\infty
                         +L\|\mathcal T\|_\infty.
\tag{S.8}
$$
没有任意起点 frame 误差或未知逆。

## 3. 准确物理角、完整 mean 与接口原子

原准确 lift 满足
$$
\theta_\phi=v/m,\qquad
\theta_r=\tau+\epsilon_R,\qquad
\tau=dv/m-\gamma u,\qquad
\epsilon_R=\frac1m I_\phi(R_v-vR_0/m),\quad R_0=\langle R_v\rangle .
\tag{S.9}
$$
这是[原完整 moving frame 恒等式](R133-supplement-moving-frame-with-complete-residual-and-mean.md)的 (4)，不以无 residual 的运输方程替换它。

角连接和理想物理连接准确满足
$$
\Omega_\phi=\theta_\phi\Omega_\theta^P,\qquad
\Omega_r^M=\Omega_r^P+\tau\Omega_\theta^P.
$$
把 (S.4) 的局部对象按自己的真实角图拉回物理 $\theta$，由其角向方程得到
$$
\begin{split}
\partial_r\bar O\big|_\theta-\bar O\Omega_r^P
 &=W-\epsilon_R\bar O\Omega_\theta^P,\\
\partial_r\bar F\big|_\theta-e\bar X
 &=U-a\epsilon_R\bar Y .
\end{split}
\tag{S.10}
$$
关键是 (S.10) 没有 $E\phi_r$ 或 $P\phi_r$；不需估计未付的逆角径向速度。

完整 moving curvature/torsion 原式含分量
$$
\mathcal R_1=\frac{b_0}{m}(R_v-vR_0/m),\qquad
|\mathcal T|=\left|\frac a m(R_v-vR_0/m)\right|.
$$
又 $\|\Omega_\theta^P\|\le|b_0|+a\sqrt{B^2+C^2}$，
$\sqrt{B^2+C^2}\le\|S\|_{\rm op}<12$。
四重 primitive 的准确 $C^0$ 范数为 $\pi/8<2/5$，故
$$
\boxed{\quad
\|\epsilon_R\Omega_\theta^P\|_\infty
 \le\frac25(\|\mathcal R\|_\infty+12\|\mathcal T\|_\infty),
\qquad
a\|\epsilon_R\|_\infty\le\frac25\|\mathcal T\|_\infty.
\quad}
\tag{S.11}
$$
$R_0$ 在这些式子里完整保留。

在原状态的任一真实接口，记
$j_\Omega=\|\Delta\Omega_\phi\|_\infty$、
$j_f=\|\Delta f_\phi\|_\infty$。因 moving 模型本身连续，(S.4) 两侧的角向比较给
$$
\|\Delta\bar O\|_\infty\le Lj_\Omega,\qquad
|\Delta\bar F|_\infty\le\tfrac12L^2F_*j_\Omega+Lj_f
\tag{S.12}
$$
（先在同一 moving 角比较）。角图自身跳
$\Delta\theta=I_\phi\Delta(v/m)$ 也必须支付。固定物理角后，新增费用至多
$$
\frac25(j_\Omega+12j_f)
\quad\hbox{对 frame},\qquad
\frac25j_f\quad\hbox{对 position}.
\tag{S.13}
$$
证明用 $\Delta\Omega_\phi$ 的第一分量
$b_0\Delta(v/m)$ 及 $|\Delta f_\phi|=a|\Delta(v/m)|$，
再沿一侧的真实物理角连接积分。无需除以点态 $v$ 的小间隙。

准确角图为奇的度 1 双射，并固定每个扇区端点 $k\pi/2$。
所以固定物理角的径向射线始终留在对应扇区；上述局部比较没有隐藏的扇区跳或全圈 holonomy 假设。扇区端点可由一侧连续极限覆盖。

## 4. 原物理径向模型的完整误差已经很小

由原完整非负累积 majorant，记其 curvature/torsion 原子测度为
$$
d\mathsf r=\|\mathcal R\|_\infty dr+\sum j_\Omega\delta_{r_j},
\qquad
d\mathsf t=\|\mathcal T\|_\infty dr+\sum j_f\delta_{r_j}.
$$
准确有
$$
\|E(R)\|+\mathsf r([0,R])\le E_*,
\qquad
\|P(R)\|+\mathsf t([0,R])\le P_*.
\tag{S.14}
$$
第二式只丢掉原 $p'$ majorant 中的非负项 $|f_r|E$。全部 6143 个原接口在原证书中已计一次。

以 (S.2) 比较同一物理角径向解与局部比较对象。外端误差由 (S.5) 给出；
径向误差用 (S.8)、(S.10)--(S.14) 和反对称 Duhamel 积分。
再加回 (S.5)，得到全角全径向
$$
\Theta_{PM}:=\|O^P-O^M\circ\phi\|_\infty
\le (2L+2/5)E_*+(24/5)P_*<4\,10^{-7}.
\tag{S.15}
$$
其中物理径向解对局部角参考的 frame 费用可取
$$
\Theta_{\rm loc}=(L+2/5)E_*+(24/5)P_*.
$$
位置费用为
$$
\begin{split}
\Phi_{PM}:=\|F^P-F^M\circ\phi\|_\infty
&\le \left(\int e\,dr\right)\Theta_{\rm loc}
 +L^2F_*E_*+(2L+2/5)P_*\\
&<3\,10^{-6}.
\end{split}
\tag{S.16}
$$
例如同时放宽 $L<2,F_*<10,\int e<2$ 后，
$\Theta_{\rm loc}<3.2\,10^{-7}$，(S.15)--(S.16) 由
$E_*<1/30000000,P_*<1/20000000$ 直接作有理比较即得。
原 moving 模型的完整连续几何误差已经包含在其已证半径/support 中，
这里没有再次加网格费用。

## 5. Qrepair 的同物理角费用，而非直接同 moving 角相减

记 $\varepsilon<4\,10^{-18}$ 为完整修补 $A^0$ 误差。
原 $\|S\|_{\rm op}<12$ 蕴含 $|1/v|<12$，而原真实 $v<0$，
所以
$$
|v|>1/12,\qquad |m|>1/12,\qquad |u|,|v|,|m|<7.
$$
修补后 $|\bar v|,|\bar m|>1/13$。准确商差给
$$
\left|\frac{\bar v}{\bar m}-\frac v m\right|
\le(13+7\cdot12\cdot13)\varepsilon<1200\varepsilon .
$$
于是 $\|\bar\theta-\theta\|_\infty<480\varepsilon$。
原 $\theta_\phi=v/m>1/84$，因此同一物理角的两个逆图满足
$$
|\bar\phi-\phi|<41000\varepsilon .
\tag{S.17}
$$
原全部角导数范数小于 $6$。先在同一 moving 点支付修补，再移动到同一物理点，
得到
$$
\max\{|\,\bar u\circ\bar\phi-u\circ\phi\,|,
       |\,\bar v\circ\bar\phi-v\circ\phi\,|\}
<250000\varepsilon<10^{-12}.
\tag{S.18}
$$
这完整保留 reciprocal mean 与逆角费用，没有把 moving 多项式当成物理 Fourier 多项式。

令右侧状态误差为 $\epsilon<10^{-12}$。原
$|K|=|\det S|<144$，并且 $|u|<7$、$|v|>1/12$、
$|\bar v|>1/13$。逐项商差给
$$
|\bar B-B|<1200\epsilon,\qquad
|\bar A-A|<8000\epsilon .
\tag{S.19}
$$
第二式使用
$A=Kv+u^2/v$；例如其系数不超过
$144+13\cdot15+49\cdot12\cdot13=7983<8000$。

两个物理径向模型的外端初值 (S.2) 完全相同。反对称径向传播及 $\int e<2$
因而给
$$
\boxed{\quad
\|O^{P,c}-O^P\|_\infty<2\,10^{-8},\qquad
\|F^{P,c}-F^P\|_\infty<4\,10^{-8}.
\quad}
\tag{S.20}
$$
原状态和修补状态的接口均按其真实一侧系数使用；物理径向 frame 没有状态跳所造成的额外人为跳。

## 6. 正 support 的实际闭合与能量规范

合并 (S.15)、(S.16)、(S.20)，并在同一真实物理角比较：
$$
\|O^{P,c}-O^M\circ\phi\|_\infty<42\,10^{-8},
\qquad
\|F^{P,c}-F^M\circ\phi\|_\infty<304\,10^{-8}.
\tag{S.21}
$$
两组 frame 都准确正交。由
$$
F^{P,c}\cdot n^{P,c}-F^M\cdot n^M
=(F^{P,c}-F^M)\cdot n^{P,c}
 +F^M\cdot(n^{P,c}-n^M),
$$
旧完整半径/support 界立即给
$$
|F^{P,c}|<1.275713422847+304\,10^{-8}<319/250,
$$
$$
F^{P,c}\cdot n^{P,c}>
0.900961392986-304\,10^{-8}
             -1.276(42\,10^{-8})>9/10.
\tag{S.22}
$$
这证明 (S.1)。

R138 旋转能量补篇的 (E.14)--(E.20) 现在可取本篇这个单一周期
$F^{P,c},O^{P,c}$、$p=0$、$\sigma=1$ 及 $s_{\min}\ge9/10$。
扇区局部比较 frame 从未进入该能量或任何端口域。
方向的真实外端 frame/位置数据、角缺陷初值、193 加 high 边界行和
source 费用仍按原定义给出；本文只固定并支付 base frame 的 support。
如果改取外帽实际世界锚、改变原点或参数族，必须支付相应的已明定变化，
不能把本篇 (S.22) 免费转授给另一个规范。

