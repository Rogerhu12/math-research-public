# R727：对称球面端层的非急角后验正根、完整逆与参数接合

日期：2026-11-28。作者：Astra-larger-e4e2a2bf-20261126 / GPT-6 Astra Pro，AI 辅助。

**状态：下述条件定理及全部估计已证明；当前实际候选是否满足条件尚未支付。** 本条继续 [R726](R726-spherical-boundary-strong-monotonicity-and-positive-mean-root.md) 的同一准确球面插值，不重复其急角定理，也不继承 R709/R722 对欧氏归一化线段的专用势或后验公式。新增内容是：利用 [R725](R725-fixed-width-boundary-cutoff-and-curvature-decomposition.md) 的完整端层反射对称，在任何与反极保持正间隔的统一角域上取得正切向下界，再由一个候选的完整残差证明局部精确正根。

本条允许方向夹角超过 \(\pi/2\)，不要求 \(|K|>b\)。结论只在明确给定的球冠内唯一，不宣称球面其余部分不存在其他根。没有实际数值运行、AST、fixture 或新的执行前门。

## 1. 准确对象与完整假设

令 \(E\) 是有限个闭端层区间之并，积分采用原物理长度测度 \(ds\)，总质量 \(b=\int_Eds>0\)。设有保持该测度的对合 \(\tau:E\to E\)，满足
\[
 \tau^2=\mathrm{id},\qquad
 0\le\chi(s)\le1,\qquad
 \chi(\tau s)=1-\chi(s)
 \quad\text{几乎处处}.
 \tag{1}
\]
R725 的每个完整端层按其中点反射即满足(1)：正向和反向 cutoff 均由
\(C_\epsilon(1-t)=1-C_\epsilon(t)\) 给出。可在每一原区间内定义 \(\tau\)；不跨不同长度的层配对。不要求参考方向 \(u(\tau s)\) 等于、相反于或与 \(u(s)\) 有任何关系。

给定准确单位向量场 \(u:E\to S^2\)。对 \(d\in S^2\) 且
\(\theta(s,d)=\arccos(u(s)\cdot d)<\pi\)，定义 R726 的准确最短弧插值
\[
 S_\chi(u,d)=
 \frac{\sin((1-\chi)\theta)}{\sin\theta}u+
 \frac{\sin(\chi\theta)}{\sin\theta}d.
 \tag{2}
\]
在 \(\theta=0\) 使用同一解析延拓，\(S_\chi(u,u)=u\)。完整均值为
\[
 B(d)=\int_E S_{\chi(s)}(u(s),d)\,ds.
 \tag{3}
\]
所有积分都覆盖完整 \(E\)，不是某个 Gauss 点集或角采样。给定 \(K\in\mathbb R^3\) 与中央总长度 \(L_c>0\)，待求
\[
 \alpha d+B(d)=K,\qquad d\in S^2,\qquad 0<\alpha<L_c.
 \tag{4}
\]
原均值变量是 \(v=(\alpha/L_c)d\)，故(4)等价于
\(L_cv+B(N(v))-K=0\)，其中 \(N(v)=v/|v|\)。

选准确单位候选中心 \(d_0\)、\(0<\alpha_0<L_c\) 和半径
\(0<\eta<\pi/2\)。记闭球冠
\[
 C_\eta=\{d\in S^2:\operatorname{dist}_{S^2}(d,d_0)\le\eta\}.
\]
假定有完整统一界
\[
 \theta(s,d_0)\le\beta,\qquad
 \theta_*:=\beta+\eta<\pi.
 \tag{5}
\]
由球面三角不等式，冠内所有实际角均不超过 \(\theta_*\)。其中
\(0<\theta_*<\pi\)，并无急角要求。定义候选完整残差与两个准确上界
\[
 R_0=\alpha_0d_0+B(d_0)-K,\qquad
 |R_0|\le e,\qquad |P_{d_0}R_0|\le e_T,\qquad
 P_d=I-d\otimes d .
 \tag{6}
\]
允许取 \(e_T=e\)，更小的完整切向上界可直接使用。

定义
\[
 m=\frac b2\cos\frac{\theta_*}{2}>0,\qquad
 L=\frac b2\,\frac{\theta_*}{\sin\theta_*},
 \tag{7}
\]
\[
 a_-=\alpha_0\cos\eta-L\eta-e,\qquad
 a_+=\alpha_0+L\eta+e,\qquad
 \kappa=m+a_-.
 \tag{8}
\]
这里明确用**球面弧长 \(L\eta\)**。仅知沿球面切向的导数界，不能将它偷换为弦长项 \(2L\sin(\eta/2)\)。

**定理。** 若
\[
 a_->0,\qquad a_+<L_c,\qquad e_T<\kappa\eta ,
 \tag{9}
\]
则(4)在 \(C_\eta\) 内存在唯一解，方向严格在冠内，且
\[
 a_-\le\alpha\le a_+,\qquad
 r:=\operatorname{dist}_{S^2}(d,d_0)
 \le\bar r:=\frac{e_T}{\kappa}<\eta.
 \tag{10}
\]
其全三维线性化可逆，逆界、完整参数接合和候选位置误差见第5–7节。下面给出所有估计与存在性证明。

## 2. 单个球面插值的完整方向导数

先取 \(0<\theta<\pi\)，在 \(T_dS^2\) 选单位向量 \(e_u\)，使
\[
 u=\cos\theta\,d+\sin\theta\,e_u,
\]
并取单位 \(h\perp d,e_u\)。沿指向 \(u\) 的单位测地线移动 \(d\) 时，
\(\dot\theta=-1,\ \dot e_u=-d\)。将(2)写为
\[
 S_\chi(u,d)=
 \cos((1-\chi)\theta)d+\sin((1-\chi)\theta)e_u
\]
并逐项求导，得到
\[
 D_dS_\chi[e_u]
 =\chi\{\cos((1-\chi)\theta)e_u
             -\sin((1-\chi)\theta)d\}.
 \tag{11}
\]
沿 \(h\) 方向，一阶 \(u\cdot d\) 不变；直接微分(2)给
\[
 D_dS_\chi[h]=\frac{\sin(\chi\theta)}{\sin\theta}\,h.
 \tag{12}
\]
两像互相正交。因此限制到二维切空间后的完整环境算子范数是
\[
 \|D_dS_\chi\|_{T_dS^2\to\mathbb R^3}
 =\max\!\left\{\chi,\frac{\sin(\chi\theta)}{\sin\theta}\right\}
 =\frac{\sin(\chi\theta)}{\sin\theta}.
 \tag{13}
\]
最后的等号来自 \(\sin\) 在 \([0,\pi]\) 上的凹性：
\(\sin(\chi\theta)\ge\chi\sin\theta\)。

投影到输出切空间后，\(P_dD_dS_\chi\) 在上述正交基中对称，两个特征值为
\[
 a_\chi(\theta)=\chi\cos((1-\chi)\theta),\qquad
 c_\chi(\theta)=\frac{\sin(\chi\theta)}{\sin\theta}.
 \tag{14}
\]
因为 \(c_\chi\ge\chi\ge a_\chi\)，冠内有
\[
 P_dD_dS_\chi
 \succeq \chi\cos((1-\chi)\theta_*)I_{T_dS^2}.
 \tag{15}
\]
这里单个 \(a_\chi\) 可以为负；后续正性由完整配对积分给出，不对每个非急角点误称正定。

由 \(\sin(\chi\theta)\le\chi\theta\) 与
\(x/\sin x\) 在 \((0,\pi)\) 递增，
\[
 \|D_dS_\chi\|
 \le\chi\frac{\theta}{\sin\theta}
 \le\chi\frac{\theta_*}{\sin\theta_*}.
 \tag{16}
\]
其单调性可直接检查：分子导数所需
\(\sin x-x\cos x\) 在0为0，导数为 \(x\sin x>0\)。
在 \(\theta=0\)，(11)–(16)按解析延拓成立，两个切向特征值均为 \(\chi\)，不需选择未定义的 \(e_u\)。

## 3. 对称配对在非急角范围给严格正下界

由(1)及测度不变性，
\[
 \int_E\chi\,ds=b/2.
 \tag{17}
\]
积分(16)即给冠内完整切向导数界
\[
 \|DB(d)\|_{T_dS^2\to\mathbb R^3}\le L.
 \tag{18}
\]

现在证明配对标量不等式。任取 \(0\le x\le1\)、\(0<\Theta<\pi\)，有
\[
 x\cos((1-x)\Theta)+(1-x)\cos(x\Theta)
 \ge\cos(\Theta/2).
 \tag{19}
\]
置 \(A=\Theta/2\in(0,\pi/2)\)、\(t=(x-1/2)\Theta\in[-A,A]\)。左边等于
\[
 \cos A\cos t+(t/A)\sin A\sin t.
\]
它是 \(t\) 的偶函数。在 \(t=0\) 等号成立；对 \(0<t\le A\)，它与 \(\cos A\) 之差为
\[
 \sin t\left\{(t/A)\sin A-\cos A\tan(t/2)\right\}.
 \tag{20}
\]
由凸性且 \(\tan0=0\)，
\[
 \tan(t/2)\le(t/A)\tan(A/2)\le(t/A)\tan A .
\]
因 \(\cos A>0,\sin t>0\)，(20)非负，证明(19)。

将(15)对整个 \(E\) 积分，并用 \(\tau\) 配对及(19)，得到
\[
 \begin{split}
 P_dDB(d)
 &\succeq
 \left(\int_E\chi(s)\cos((1-\chi(s))\theta_*)\,ds\right)I\\
 &=\frac12\int_E
 \{\chi\cos((1-\chi)\theta_*)+
    (1-\chi)\cos(\chi\theta_*)\}\,ds\,I\\
 &\succeq mI.
 \end{split}
 \tag{21}
\]
整个估计对冠内每个 \(d\) 成立。每一项使用同一个合法上界 \(\theta_*\)，所以不需要 \(u(\tau s)=u(s)\)，也不需要真实配对角相等。

若 \(\gamma\) 是冠内从 \(d_0\) 到 \(d\) 的单位速最短测地线，长度 \(r\le\eta\)，由(18)
\[
 |B(d)-B(d_0)|
 \le\int_0^r|DB(\gamma(t))\dot\gamma(t)|\,dt
 \le Lr\le L\eta.
 \tag{22}
\]
(22)是沿弧的积分，不能在没有额外环境空间延拓估计时改成欧氏弦长 Lipschitz 结论。

## 4. 球面势、存在性、唯一性和后验半径

### 4.1 同一准确均值的势

对 \(0\le\chi<1\) 定义
\[
 f_\chi(z)=
 \frac{\cos((1-\chi)\arccos z)-1}{1-\chi},
 \qquad f_1(z)=0.
 \tag{23}
\]
在统一非反极域，\(\chi=1\) 与 \(z=1\) 均按连续光滑延拓解释。
直接求导得
\[
 f_\chi'(z)=
 \frac{\sin((1-\chi)\theta)}{\sin\theta}.
\]
因此球面函数
\[
 V(d)=\int_E f_{\chi(s)}(u(s)\cdot d)\,ds-K\cdot d
 \tag{24}
\]
满足
\[
 \operatorname{grad}_{S^2}V(d)=P_d(B(d)-K).
 \tag{25}
\]
对 \(\chi=1\)，相应 \(S_\chi=d\)，其切向投影为0，正好与 \(f_1=0\) 一致。统一 \(\theta_*<\pi\) 和有限测度保证所用导数可在积分号内取得；零角的解析延拓由(2)的同一函数给出。

定义
\[
 \alpha(d)=d\cdot(K-B(d)).
 \tag{26}
\]
对 \(w\in T_dS^2\)，沿过 \(d\) 的测地线二次求导，使用
\(\ddot\gamma=-|w|^2d\)，得到
\[
 \operatorname{Hess}_{S^2}V(d)[w,w]
 =w\cdot DB(d)w+\alpha(d)|w|^2 .
 \tag{27}
\]
这也是(25)的协变导数。完整环境三维 \(DB\) 不必对称；(21)仅对它的切向投影断言对称及下界。

### 4.2 全冠径向幅度与强凸性

由(6)写
\(K=\alpha_0d_0+B(d_0)-R_0\)。若方向与 \(d_0\) 的夹角为 \(r\le\eta\)，则
\[
 \alpha(d)=\alpha_0\cos r+
           d\cdot(B(d_0)-B(d))-d\cdot R_0 .
 \tag{28}
\]
由(22)、\(\alpha_0>0\) 得
\[
 a_-\le\alpha(d)\le a_+
 \quad(d\in C_\eta).
 \tag{29}
\]
(21)、(27)、(29)遂给
\[
 \operatorname{Hess}_{S^2}V(d)\succeq\kappa I,\qquad\kappa>0.
 \tag{30}
\]

半径小于 \(\pi/2\) 的闭球冠测地凸。为完整说明，任意冠内 \(d_1,d_2\) 的最短弧角 \(\ell<\pi\)，其内部点为
\[
 \gamma(t)=
 \frac{\sin((1-t)\ell)}{\sin\ell}d_1+
 \frac{\sin(t\ell)}{\sin\ell}d_2,\quad0\le t\le1.
\]
两系数非负，且其和至少1；与 \(d_0\) 点积便得
\(d_0\cdot\gamma(t)\ge\cos\eta\)。\(\ell=0\) 用常值弧。故(30)控制冠内两点间的完整最短弧。

### 4.3 排除边界极小点

连续 \(V\) 在紧冠上达到最小值。取任一边界点和从 \(d_0\) 指向它的单位速测地线 \(\gamma:[0,\eta]\to C_\eta\)，令 \(h(t)=V(\gamma(t))\)。由(25)、(6)
\[
 h'(0)=\langle P_{d_0}R_0,\dot\gamma(0)\rangle\ge-e_T .
\]
由(30)
\[
 h'(\eta)\ge-e_T+\kappa\eta>0.
 \tag{31}
\]
因此沿同一弧向内移动会严格降低 \(V\)，任何边界点都不是冠上极小点。最小点在内部，故(25)为零。将 \(B-K\) 分解为法向与切向分量，(26)给出完整方程(4)，而(29)和(9)给 \(0<\alpha<L_c\)。存在性没有假定有根，也没有把近似 Newton 成功当成存在证明。

若冠内有两个不同临界点，连接它们的最短弧上 \(h''\ge\kappa>0\)，但两端 \(h'=0\)，矛盾。故临界点唯一。任何(4)在冠内的根均是(25)临界点，且其 \(\alpha\) 必须等于(26)，所以整个 \((\alpha,d)\) 唯一。

最后令实际根距中心为 \(r>0\)，沿径向弧根处 \(h'(r)=0\)。相同积分给
\[
 0=h'(r)\ge-e_T+\kappa r,
\]
即(10)。若 \(r=0\) 不等式也成立。若 \(e_T=0\)，结论尤其给 \(d=d_0\) 和
\(\alpha=\alpha_0-d_0\cdot R_0\)，不需要人为除以 \(r\)。

## 5. 精确根相对候选的位置与全三维逆界

### 5.1 幅度和原变量误差

将实际根的 \(r\le\bar r\) 代回(28)，有更细的两侧估计
\[
 \alpha_0\cos r-Lr-e\le\alpha
 \le\alpha_0\cos r+Lr+e.
 \tag{32}
\]
因 \(0\le r\le\bar r<\pi/2\)，
\[
 |\alpha-\alpha_0|
 \le e+L\bar r+\alpha_0(1-\cos\bar r).
 \tag{33}
\]
设 \(v=(\alpha/L_c)d,\ v_0=(\alpha_0/L_c)d_0\)，分解
\(\alpha d-\alpha_0d_0=(\alpha-\alpha_0)d+\alpha_0(d-d_0)\)，并用单位球上的准确弦长恒等式，得到
\[
 |v-v_0|\le
 \frac{e+L\bar r+\alpha_0(1-\cos\bar r)
             +2\alpha_0\sin(\bar r/2)}{L_c}.
 \tag{34}
\]
(34)的最后一项来自两个**已知单位向量之差**，故这里使用弦长合法；它与(22)对未知沿弧变化的 \(B\) 使用弧长是两个不同事实。

### 5.2 \((\alpha,d)\) 坐标的完整线性化

在根处取 \(w\in T_dS^2\)，完整线性化为
\[
 J(\delta\alpha,w)=d\,\delta\alpha+\alpha w+DB(d)w.
 \tag{35}
\]
给定任意环境右端 \(f\in\mathbb R^3\)，投影切向得
\[
 (\alpha I+P_dDB(d))w=P_df.
 \tag{36}
\]
(21)、(29)说明左边为二维对称正定算子，最小特征值至少
\(\alpha+m\ge\kappa\)。因此
\[
 |w|\le\frac{|P_df|}{\alpha+m}\le\frac{|f|}{\kappa}.
 \tag{37}
\]
再取(35)沿 \(d\) 的分量，得唯一
\[
 \delta\alpha=d\cdot f-d\cdot DB(d)w,
 \qquad
 |\delta\alpha|\le(1+L/\kappa)|f|.
 \tag{38}
\]
径向输出和两个切向未知共同确定，故这确实给全三维可逆性，不把原三维方程降成标量，也不把完整 \(J\) 误认为对称矩阵。

### 5.3 原 \(v\) 坐标的逆界

记 \(F(v)=L_cv+B(N(v))-K\)。因
\[
 \delta v=(\delta\alpha/L_c)d+(\alpha/L_c)w,
 \qquad d\perp w,
\]
(37)–(38)给欧氏算子逆界
\[
 \|D_vF(v)^{-1}\|
 \le\frac1{L_c}
 \sqrt{(1+L/\kappa)^2+(\alpha/\kappa)^2}
 \le\frac1{L_c}
 \sqrt{(1+L/\kappa)^2+(a_+/\kappa)^2}.
 \tag{39}
\]
这里保留正交分解的平方和，并非随意把切向 \(m\) 当作整个 \(3\times3\) Jacobian 的最小特征值。若实际应用愿意保留 \(\alpha+m\) 或分别支付 \(|P_df|\)、\(|d\cdot f|\)，(37)–(38)还可给更细的逐右端估计。

## 6. 完整角导数、参数依赖与分支接合

本节不将已刊 R726 的完整两角链式展开重做成另一数学定义，而是说明新的存在/逆界怎样给同一展开提供合法解分支。

设数据依赖参数 \(p\)（例如物理角或外部设计参数），在某开参数域内具有 \(C^2\) 依赖。积分区间若随参数变化，必须先用其准确仿射坐标拉回固定有限区间，完整 Jacobian 测度因子一起求导。要求这些被拉回的函数及其至二阶参数导数存在可积统一支配；\(\tau\) 对相应准确测度保(1)。若 \(b,L_c,\chi\) 也变化，其导数同样保留，不从常参特殊式中删掉。具体本课题的固定 seed 参数、固定长度与 cutoff 情形是该合同的子情形。

假定(5)、(9)在邻域中有统一严格余量，候选 \((\alpha_0(p),d_0(p))\) 至少连续，且数据所需光滑性如上。由第4节每个参数有唯一冠内根，且距边界有正间隔。第5节在每个根给完整可逆 Jacobian，普通有限维隐函数定理于是产生局部 \(C^2\) 根。

需说明这些局部分支没有跳到别的冠外根：在固定参数 \(p_*\) 的根处，方向到对应球冠边界有严格间隔；由候选中心/半径的连续性和局部隐式根的连续性，充分靠近 \(p_*\) 时该局部分支仍在当前球冠内。第4节的冠内唯一性使它与该参数的后验构造根相同。相邻局部隐式分支遂逐点相等并接合，给整个参数域上这条受证分支的 \(C^2\) 性。这里没有使用冠外全局唯一性。

当 \(L_c\) 对角 \(\phi\) 固定时，方向与幅度的一阶式可写为
\[
 d\,\alpha_\phi+\alpha d_\phi+
 DB(d)d_\phi=K_\phi-\partial_\phi B,
 \qquad d\cdot d_\phi=0 .
 \tag{40}
\]
右端中的 \(\partial_\phi B\) 是**固定 \(d\)** 后对完整准确端层积分求偏导；它必须包含 \(u\) 的真实角导数以及参数变化时的 cutoff 和测度项。式(37)–(38)给它的完整方向和幅度界。

二阶需保
\[
 d\cdot d_{\phi\phi}=-|d_\phi|^2.
 \tag{41}
\]
写 \(d_{\phi\phi}=w-|d_\phi|^2d,\ w\perp d\)，将它代入完整二阶微分方程。未知 \((\alpha_{\phi\phi},w)\) 仍由(35)同一可逆线性化解出；全部已知项包括
\(2\alpha_\phi d_\phi\)、\(-\alpha|d_\phi|^2d\)、混合
\(2\,\partial_\phi DB[d_\phi]\)、完整二阶方向项及
\(\partial_{\phi\phi}B\)。采用局部球面图时，各坐标二阶项应完整计入；采用 \(v\) 及 \(N(v)\) 图时，它们正是
\(DN(v)v_{\phi\phi}+D^2N(v)[v_\phi,v_\phi]\) 的完整两部分。不能把(41)的法向加速度丢掉，也不能只用一次 root residual 界替这些导数积分费用。

等价地，在原 \(v\) 坐标令 \(F(v,\phi)=L_cv+B(N(v),\phi)-K(\phi)\)，完整且无坐标歧义的公式是
\[
 D_vF\,v_\phi=-F_\phi,
 \tag{42}
\]
\[
 D_vF\,v_{\phi\phi}
 =-F_{\phi\phi}-2D_vF_\phi[v_\phi]
                 -D_v^2F[v_\phi,v_\phi].
 \tag{43}
\]
(39)可分别用于两个完整右端。\(L_c=L_c(\phi)\) 时，(42)–(43)中的偏导须包含它的一阶、二阶；从 \(\alpha=L_c|v|\) 转换也保留这些项。R726 已给的全角展开、零角解析系数及准确场到工作图责任继续适用，新的 \(\kappa,L\) 只替换其合法逆/包围常数，不使旧未支付的积分或尾部误差自动为零。

若完整数据、候选中心、cutoff与所证球冠在物理角上准确周期，周期两端数据同一，冠内唯一性给根同一；局部 \(C^2\) 分支导数亦由同一隐式方程相等，因而周期接合。对任意 \(Q\in O(3)\)，包括反射，
\(S_\chi(Qu,Qd)=Q S_\chi(u,d)\)，残差、角、常数和球冠随 \(Q\) 协变。若完整数据按所需对称变换而候选冠也对应，\(Qd,\alpha\) 是变换后冠内根，唯一性给该分支的准确协变。此处的 \(O(3)\) 协变并不证明最终曲面的未标记非全等性。

## 7. 从实际工作候选到可用的准确后验输入

### 7.1 不能假定保存的浮点方向准确单位长

实际保存的 binary64 三向量 \(v_0^{\mathrm{bin}}\ne0\) 可以逐字视为准确二进有理向量。可定义
\[
 d_0=N(v_0^{\mathrm{bin}}),\qquad
 \alpha_0=L_c|v_0^{\mathrm{bin}}|,
\]
其中平方根和除法按准确实数定义，实际计算需用向外包围。若另选独立有理 \(\alpha_0\)，也须明确记录。不能把保存的近似 \(d\) 直接当成准确单位向量，从而漏掉中心归一化费用。条件 \(0<\alpha_0<L_c\) 和全冠不等式均须按包围后的严格方向证成。

### 7.2 残差和角界必须覆盖同一个完整准确问题

(6)中的 \(B(d_0)\) 是(2)–(3)的准确积分。实际需要对同一原输入、准确端层分割、所有完整叶片及全尾支付求积、cutoff、参考方向、平方根/三角函数、零角解析延拓和浮点费用；只给求解器有限 Gauss residual 不足以推出 \(e\) 或 \(e_T\)。若先得到完整向量盒，可投影得到切向盒，或安全地取 \(e_T=e\)。

(5)需要在每一完整径向/角参数胞上统一成立，而非只在有限角样本。可用准确点积包围及严格非反极间隔推出合法 \(\beta\)，但端点反三角运算和余量也必须付清。一个 sampled acute 布尔值既不是(5)的全域界，也不需要成为本定理的新数值准入条件。原程序允许的非零、非反极工作域继续按其原语义。

### 7.3 分块求证必须给同一分支

若对不同角胞各取候选和球冠，每胞内的本定理先给各自的准确分支。要把它们当成一条全角 \(C^2\) 分支，必须证相邻胞重叠处指向同一个根：例如两后验方向球的已证共同包含关系使一条根落入另一唯一性球冠，或在共同交界给相同候选/同一冠并用完整残差证书。各胞分别“存在某根”不足以自动接成全角同一分支。

实际字面角、周期端点、相邻数据版本、source/model、保存的 mean/root packet、当前点和全部 normal stage 必须与同一连续对象对应。工作 Newton 从哪个初值收敛，不单独替代这一准确分支归因。

### 7.4 工作表达式和原中央幅度分支

已刊 R726 最小 mean/seed 的小角 degree32 多项式、大角三角式及实际两次输入和一次输出归一化是明确工作图。准确 Slerp 的零角解析延拓与该有限图之间仍有截断和舍入费用；在 \(q=1/4\) 的工作切换不能被本定理改称准确 \(C^2\)。本定理的 \(B\) 从头至尾是准确(2)，不是拼接工作多项式。

(9)给 \(0<|v|<1\)，但原中央 profile 的实际幅度方程和逆支另按 R711/R724 的完整合同求证。不能只从这个区间就推出任何指定工作 bracket 或标量逆一定成功；现有工作程序完整保
\(a_\delta(\pi)<|v|<a_\delta(0)\)、原全12片、64次二分、全部角导数及三分量闭合残差。若具体准确 profile 有已证单调支，须把(10)、(33)及其误差区间确实放入该支，再消费原已证逆公式。未返标量结果不补数值。

## 8. 对课题完成标准的精确贡献与限制

本条在明确且可量化的完整候选残差、非反极角域和长度余量下，证明了新球面端层均值的局部准确正根、唯一性、完整逆、位置误差与 \(C^2\) 参数分支。它去掉 R726 先前条件方案中的急角与 \(|K|>b\) 需求，换成可针对真实候选支付的(5)–(9)，没有预设这些条件已对任何当前运行成立。

它不证明本课题当前曲面已经闭嵌入，不把 mean 的完整 \(J_v\) 当作32 stage normal closure 的 \(C_u\)，不付 whole-field relative Gram、全 \(t\) reach、两帽、固定 \(H\) 的直径或整像位移，不给含反射未标记 \(\delta_E>0\)，也不产生同固定 \(g\)/参数的真实空间、频率、时间精化和五时刻完整 mesh。全部这些原义标准仍由真实构造及独立全域证明完成。

源、参数和实际运行应继续推进；这份条件证明不构成新的执行前审核门。新候选失败时保真实失败并换输入或机制继续，不能以“条件未核”或本子定理完成代替课题完成。
