# R728 — 反转成对半波：不变均值、完整前缀位移与见证距离的定向条件

**已证明：下述明确假设下的均值不变性、完整前缀与六 jet 恒等式、距离条件和平面性；全场可行性仍未证明。**

2026-11-28。本文改变 R726/R727 球面端层种子的**两个完整中央半波次序**：原先第一段为正、第二段为负，改为第一段为负、第二段为正。端层、完整均值方程、幅度方程、固定度量、所有径向切点与原预算均不改变。本文证明准确种子的位置差、全部物理六 jet 差、见证距离和半径的精确差式，并给出 \(\varphi=\pi/2\) 上不依赖旧全局唯一性的平面性结论。

这是一条有明确距离方向的独立新输入。它没有证明新完整 normal 场已可行，也没有从中央 \(|T_s|\) 不变推出 principal curvature、Gram、直径或 reach 不变。现有公开29读数尚没有距离热点的径向位置，因而本文不把条件距离改善写成已观测的全域改善。

## 1. 已有结果、准确对象与本次唯一物理变化

使用以下完整已登记对象，不重做它们的证明：

- [R717](R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 的固定 dyadic Fejér 图、核心 \(\Gamma\) 与准确 \(\Theta_0,\rho_0\)。
- [R711](R711-smooth-triangle-central-profile-and-geometric-comparison.md) 的完整 \(C^3\) profile \(h_\delta\)、全部十二片辅助幅度积分及 \(\lambda\) 反解。
- [R724](R724-paired-halfwave-central-seed-and-complete-source-identity.md) 的两段等长成对半波、端口与物理全相位合同。
- [R725](R725-fixed-width-boundary-cutoff-and-curvature-decomposition.md) 的固定 \(\epsilon=1/8\) 三片端层 cutoff，保留全部八个内部端层切点。
- [R726](R726-spherical-boundary-strong-monotonicity-and-positive-mean-root.md) 的准确最短球面插值与完整三维均值方程。
- [R727](R727-symmetric-spherical-boundary-posterior-root-without-acute-cap.md) 的有条件局部冠存在、唯一、两角导数及跨角接合。本文不把它改成旧 R722 的闭球势或全局唯一性。

令两个中央区间为
\[
 I_1=[a_1,b_1],\qquad I_2=[a_2,b_2],\qquad
 b_1-a_1=b_2-a_2=\ell>0,\quad b_1<a_2.
\]
固定一个准确角 \(\varphi\)。假设原完整 R726 均值方程已有所选准确根
\[
 L_c v+B(d)=K,\qquad L_c=2\ell,\quad
 r=|v|\in(0,1),\quad d=v/r,\quad |d|=1,
 \tag{1}
\]
其中所有端层均为同一个准确最短球面插值
\[
 B(d)=\int_E {\cal S}_{\chi(s)}(u(s,\varphi),d)\,ds,\qquad
 {\cal S}_{\chi}(u,d)=
 \frac{\sin((1-\chi)\theta)}{\sin\theta}u+
 \frac{\sin(\chi\theta)}{\sin\theta}d,\quad
 \theta=\arccos(u\cdot d)<\pi .
 \tag{2}
\]
零角按 R726 的连续延拓。完整尾部、原 scalar 归一化、端层测度与 \(K\) 的真实定义均包括在(1)内。

设原 R711 幅度反解给出
\[
 A_\delta(\lambda)=r,\qquad 0<\lambda<\pi.
 \tag{3}
\]
本文不由 \(0<r<1\) 自动推出全部现行 profile bracket 条件；必须保留实际反解和导数分母的原完整条件。

令 \(e=e_r(\Theta_0(\varphi))\)，并假设
\[
 |e-(e\cdot d)d|>0,\qquad
 w=\frac{e-(e\cdot d)d}{\sqrt{1-(e\cdot d)^2}}.
 \tag{4}
\]
这里是 **\(e_r\) 的投影，不是 \(e_z\) 的投影**。这一点直接由当前1764种子 model 和共享2513均值核的投影架定义决定。R727 的非急角根冠没有自动支付(4)，它仍是独立的准确分母条件。

定义完整正半波
\[
 f(t)=h_\delta(t/2),\qquad 0\le t\le1,\qquad
 \alpha(t)=\lambda f(t).
 \tag{5}
\]
原 profile 给出 \(0\le f\le1\)、两端所需平坦导数及完整六片接合，故
\[
 0\le \sin\alpha(t),\qquad
 J(\lambda)=\int_0^1\sin(\lambda f(t))\,dt>0 .
 \tag{6}
\]
中间严格正性用 \(0<\lambda<\pi\) 及 profile 在一个正测度集合上满足 \(0<f<1\)。

令 \(\eta(s)=1\) 在 \(I_1\)，\(\eta(s)=-1\) 在 \(I_2\)。以全局 polarity \(\sigma\in\{+1,-1\}\) 定义中央切向量
\[
 T^\sigma(s,\varphi)
 =\cos\alpha(t)\,d+\sigma\eta(s)\sin\alpha(t)\,w,
 \qquad t=(s-a_i)/\ell,\ s\in I_i .
 \tag{7}
\]
中央以外，两种方案均取原完整 R726 种子切向量：端层为(2)，其余为原 \(u=T_0\)。原方案是 \(\sigma=+1\)；本次独立新源固定 \(\sigma=-1\)。

准确种子 primitive 是
\[
 F^\sigma(s,\varphi)=\Gamma(\varphi)+\int_0^sT^\sigma(\xi,\varphi)\,d\xi .
 \tag{8}
\]
它不是未经说明就等同于有限积分、当前 SO3 控制、32阶段 normal 根及末端 lift 产生的完整 working 场。第10节明确二者的责任边界。

## 2. 完整均值、根与角 jet 的不变量

两段中央积分之和为
\[
 \begin{aligned}
 \int_{I_1\cup I_2}T^\sigma\,ds
 &=2\ell\left(\int_0^1\cos(\lambda f(t))\,dt\right)d\\
 &\quad+\sigma\ell Jw-\sigma\ell Jw
 =L_cA_\delta(\lambda)d=L_cv .
 \end{aligned}
 \tag{9}
\]
第二个等号使用 R724 已证明的半波余弦均值恒等式，没有删掉任何辅助十二片或把某次浮点正弦和强制设为零。

因此：

1. 完整 \(B,K,L_c\) 以及方程(1)逐函数相同；所有端层、外部积分和 scalar 尾均保留。
2. 在选择同一个已存在准确根分支时，\(v,d,r,\lambda,w\) 与它们的完整一、二角导数均相同。
3. R726/R727 的同一均值方程假设没有因 \(\sigma\) 改变。但已有证据的原 source、model、point、输入与角域归因不能自动搬给新来源。
4. 新种子端点闭合与原种子相同。这个准确恒等式不等于新 working closure 字、Q 矩、校准常量或 normal 控制已经计算，更不允许复用旧 accepted 场。

第2项可以从共同的准确方程和已支付的同分支唯一性/IFT 得出；也可以把同一已存在分支作为两个条件构造的共同输入。不能仅以数值近似根相近代替分支认同。

当前共享2513核的真实接口仍是完整三分量原始 \(v\) 图；保存的是 \(v,d,w,\lambda\) 及它们的两角数组，并没有新增虚构的独立 \(r\) 数组。该核及其全部正权规则原字共享。

## 3. 两个半波的完整位移图

令
\[
 Q(t,\lambda)=\int_0^t\sin(\lambda f(u))\,du .
\]
定义非负横向前缀幅度
\[
 {\cal A}(s,\lambda)=
 \begin{cases}
 0,&s\le a_1,\\
 \ell Q((s-a_1)/\ell,\lambda),&a_1\le s\le b_1,\\
 \ell J(\lambda),&b_1\le s\le a_2,\\
 \ell[J(\lambda)-Q((s-a_2)/\ell,\lambda)],
       &a_2\le s\le b_2,\\
 0,&s\ge b_2 .
 \end{cases}
 \tag{10}
\]
于是
\[
 0\le{\cal A}(s,\lambda)\le\ell J(\lambda).
 \tag{11}
\]
它在第一中央段单调增加，在两段之间保持峰值，在第二中央段单调减小，最后回到零。端层和支撑之间的保留区间也属于中间位置差的真实作用范围。

把不含横向半波的公共 primitive 记为
\[
 {\cal C}(s,\varphi)=
 \Gamma(\varphi)+\int_0^s V(\xi,\varphi)\,d\xi,
 \quad
 V=
 \begin{cases}
 \cos\alpha\,d,&I_1\cup I_2,\\
 T^\sigma,&\text{其余}.
 \end{cases}
 \tag{12}
\]
它是两种种子位置的平均，不声称其自身是一条单位速率种子。由(7)直接积分，
\[
 \boxed{F^\sigma={\cal C}+\sigma{\cal A}w,\qquad
 F^- -F^+=-2{\cal A}w.}
 \tag{13}
\]

| 准确材料区域 | \({\cal A}\) | 从原正首段到反号方案的位置变化 |
|---|---:|---|
| 第一中央段之前 | \(0\) | \(0\) |
| 第一中央段 | 从 \(0\) 增到 \(\ell J\) | \(-2{\cal A}w\) |
| 两中央段之间，包括真实端层/保留间隙 | \(\ell J\) | \(-2\ell Jw\) |
| 第二中央段 | 从 \(\ell J\) 降到 \(0\) | \(-2{\cal A}w\) |
| 第二中央段之后 | \(0\) | \(0\) |

这张图是准确位置账。不能以中间某段切向量没有改变为由，把它的位置变化删去。

正半波均值为 \(rd+Jw\)，是单位向量的均值，故
\[
 r^2+J^2\le1,\qquad
 |F^- -F^+|\le2\ell J\le2\ell\sqrt{1-r^2}.
 \tag{14}
\]
这是有条件的完整位置上界，不是实际直径改善证书。

## 4. 全六 jet 与端口：径向速度范数相同不足以排序曲率

在每个中央段，
\[
 T_s^\sigma
 =\alpha_s[-\sin\alpha\,d+\sigma\eta\cos\alpha\,w],
 \qquad |T_s^\sigma|=|\alpha_s|.
 \tag{15}
\]
两种方案的单位速率与中央 \(|T_s|\) 完全相同。中央以外连 \(T,T_s\) 本身也相同。

令 \(\Delta F=F^--F^+\)。对(13)完整求导得到
\[
 \begin{aligned}
 \Delta F&=-2{\cal A}w,&
 \Delta F_s&=-2{\cal A}_s w,&
 \Delta F_{ss}&=-2{\cal A}_{ss}w,\\
 \Delta F_\varphi&=-2({\cal A}_\varphi w+{\cal A}w_\varphi),&
 \Delta F_{s\varphi}&=-2({\cal A}_{s\varphi}w+
                                  {\cal A}_s w_\varphi),\\
 \Delta F_{\varphi\varphi}
 &=-2({\cal A}_{\varphi\varphi}w+
       2{\cal A}_\varphi w_\varphi+{\cal A}w_{\varphi\varphi}).
 \end{aligned}
 \tag{16}
\]
这里
\[
 {\cal A}_\varphi={\cal A}_\lambda\lambda_\varphi,\qquad
 {\cal A}_{\varphi\varphi}
 ={\cal A}_{\lambda\lambda}\lambda_\varphi^2+
   {\cal A}_\lambda\lambda_{\varphi\varphi},
 \tag{17}
\]
而 \({\cal A}_\lambda,{\cal A}_{\lambda\lambda}\) 从(10)按原完整区间积分
\(f\cos(\lambda f)\) 与 \(-f^2\sin(\lambda f)\)。不能省略投影架导数或幅度两角导数。

所有 profile 内部切点仍是原六片准确切点；反号是一个固定标量乘法，不改变任何片间匹配。在中央端点，原 \(f,f',f''\) 的平坦性给
\[
 T^\sigma=d,\quad T_s^\sigma=0,\quad
 T^\sigma_\varphi=d_\varphi,\quad
 T^\sigma_{\varphi\varphi}=d_{\varphi\varphi},
 \quad T^\sigma_{s\varphi}=0 .
 \tag{18}
\]
它们与原 R725/R726 内端口一致。沿材料径向的 \(C^3\) 切向量和必要的完整 \(C^2\) 曲面接合保留。外端口、core、cap 邻域及其反射/平帽公式均不改。

不过 \(\Delta F_\varphi\) 一般非零；即使中间间隙内 \(\Delta F_s=0\)，也不能认定该处 Gram 或第二基本形式不变。真实 principal curvature 是完整 \(I^{-1}II\) 的谱，不是 \(|T_s|\)。同一固定目标 \(g\) 保留，与诱导度量相等是另一项尚待求解的条件。

## 5. 固定见证点与两种场的精确平方距离差

对任意固定见证点 \(q\in\mathbb R^3\)，由(13)有
\[
 \boxed{
 |F^- -q|^2-|F^+ -q|^2
 =4{\cal A}\,G_q,\qquad
 G_q=w\cdot(q-{\cal C}).
 }
 \tag{19}
\]
因此在 \({\cal A}>0\) 的点：

- \(G_q>0\) 时反号方案严格增加到该见证点的距离；
- \(G_q=0\) 时两种距离相同；
- \(G_q<0\) 时反号方案使该距离变小。

这不是“向内必然更远”的图像直觉，而是包括完整高度分量的精确判据。

真实 geometry 源对当前核心给
\[
 X=1+\sum_{j=1}^{M}c_j,\qquad
 q_\pm=(0,\pm X,0),\qquad
 g_\pm(F)=1-\frac{|F-q_\pm|^2}{L_{\rm wit}^2}.
 \tag{20}
\]
它不是标记材料点的位移，也不是全局 Hausdorff 证书。若比较时 \(X,L_{\rm wit}\) 保持相同，则(19)等价于
\[
 g_\pm(F^-)=g_\pm(F^+)
           -\frac{4{\cal A}G_{q_\pm}}{L_{\rm wit}^2}.
 \tag{21}
\]
对整个准确目标域 \({\cal D}\)，精确的通过条件是
\[
 \inf_{(s,\varphi)\in{\cal D}}
 \left\{|F^+(s,\varphi)-q_\pm|^2
       +4{\cal A}(s,\varphi)G_{q_\pm}(s,\varphi)\right\}
 \ \ge L_{\rm wit}^2
 \tag{22}
\]
并须分别对两个符号、全部上下片/帽/实际物理相位与原 mixed 条件完成所需解释。逐点 \(G_{q_+}>0\) 只给方向；旧距离本身及改善量仍须覆盖整个域。原正 \(g_+\) 若来自 \({\cal A}=0\) 的位置，准确种子反号本身在那里没有收益。

同样，
\[
 \boxed{|F^-|^2-|F^+|^2=-4{\cal A}\,{\cal C}\cdot w.}
 \tag{23}
\]
因此 \(0\le{\cal C}\cdot w\le q_+\cdot w\) 是同时不增该点半径、不减到 \(q_+\) 距离的充分条件。它没有把另一见证点的约束删去。事实上
\[
 G_{q_-}=-Xw_y-{\cal C}\cdot w,\qquad
 G_{q_+}= Xw_y-{\cal C}\cdot w
 \tag{24}
\]
通常不同，改善一个符号可能消耗另一个符号的余量。原两符号读取和全部预算必须保留。

## 6. 第一、第二中央段上的改善符号各自是常量

固定 \(\varphi\)。在任一中央段，\(w\) 不随 \(s\) 改变，
\[
 \frac{d}{ds}({\cal C}\cdot w)
 =\cos\alpha\,d\cdot w=0.
\]
故 \(G_q\) 在该整个中央段上为常量：
\[
 G_q|_{I_1}=w\cdot(q-F(a_1)),\qquad
 G_q|_{I_2}=w\cdot(q-{\cal C}(a_2)).
 \tag{25}
\]
第一入口处 \({\cal A}=0\)，所以 \(F(a_1)\) 是两方案的共同入口。第二入口处 \({\cal A}=\ell J\)，须用公共 \({\cal C}(a_2)\)，不能误用某个方案的 \(F^\sigma(a_2)\)。

于是第一中央段若满足
\[
 w\cdot(q-F(a_1))>0,
 \tag{26}
\]
该段全部 \({\cal A}>0\) 的点均严格改善，不需猜测 profile 峰或距离热点的材料坐标。第二中央段有它自己的同样完整条件。中间间隙仍须按真实公共切向量支付 \(G_q(s)\) 的变化；不能把第一入口条件自动延拓到整个第二段或全部闭面。

## 7. \(\varphi=\pi/2\)：真实投影、平面性与高度竞争

### 7.1 不借旧全局唯一性的平面性

对当前固定 Fejér 图，准确
\[
 \Theta_0(\pi/2)=\pi/2,\qquad
 e=e_y,\qquad \Gamma(\pi/2)=Y e_y,\quad Y=p(\pi/2).
\]
完整 scalar 参考及 \(K\) 均在 \(yz\) 平面：
\[
 u(s,\pi/2)=B_0(s)e_y+C_0(s)e_z,\qquad K_x=0.
 \tag{27}
\]
这是固定公式的准确值，不是把 binary64 \(\cos(\pi/2)\) 工作字强置为零。

令 \(\alpha_0=L_cr>0\)。在(2)中，
\[
 b_\chi(s)=\frac{\sin(\chi\theta)}{\sin\theta}\ge0
\]
于 \(\theta=0\) 取 \(\chi\)。因为 \(u_x=0\)，均值方程的 \(x\) 分量为
\[
 \left(\alpha_0+\int_E b_\chi\,ds\right)d_x=0.
\]
系数严格为正，故
\[
 d_x=0 .
 \tag{28}
\]
这一结论对任意满足(1)的正 \(\alpha_0\) 根成立，不需要急角条件，不需要先借 R722 全局唯一性，也不需要把两条局部根冠凭对称标签认同。

### 7.2 精确投影式和不能省去的高度项

写 \(d=(0,p,z)\)，\(p^2+z^2=1\)。由(4)，投影架合法恰要求 \(z\ne0\)，且
\[
 w=(0,|z|,-p\,\operatorname{sgn}z).
 \tag{29}
\]
因此
\[
 \boxed{
 G_{q_+}
 =|z|(X-{\cal C}_y)
   +p\,\operatorname{sgn}z\,{\cal C}_z .
 }
 \tag{30}
\]
特别地，若 \(z>0\)，则
\[
 G_{q_+}=z(X-{\cal C}_y)+p{\cal C}_z.
 \tag{31}
\]
当 \(p<0\)、\({\cal C}_z>0\) 时，第二项为负。见证点位于水平外侧本身不足以证明 \(G_{q_+}>0\)。只有实际满足
\[
 X-{\cal C}_y>\frac{-p}{z}{\cal C}_z
 \quad(p<0,\ z>0)
 \tag{32}
\]
才能得出相应符号。若 \(p\ge0,z>0,{\cal C}_z\ge0\) 且
\({\cal C}_y<X\)，则(31)直接为正；这些条件也不能未经实际证明就代入。

来源没有给出本文所需的实际 \(p,z,{\cal C}(a_i)\) 精确值。当前 R727 条件本身也不保证 \(z>0\)。因此本文既不预设 \(p<0\)，也不预设 \(p\ge0\)。

### 7.3 全前缀的一维准确公式

令
\[
 a_\chi(s)=\frac{\sin((1-\chi)\theta)}{\sin\theta}\ge0.
\]
在原补集取 \(a_\chi=1\)；在中央段将下面积分的 integrand 置零。因为 \(d\cdot w=0\)，端层满足
\[
 T\cdot w=a_\chi\,u\cdot w
 =a_\chi\bigl(|z|B_0-p\,\operatorname{sgn}z\,C_0\bigr).
\]
所以整个准确前缀有
\[
 \boxed{
 G_{q_+}(s)
 =|z|(X-Y)
 -\int_{[0,s]\setminus(I_1\cup I_2)}
 a_\chi(\xi)
 \bigl(|z|B_0(\xi)-p\,\operatorname{sgn}z\,C_0(\xi)\bigr)
 \,d\xi .
 }
 \tag{33}
\]
它包含所有实际端层、支撑间隙及所有 scalar tail 的真实作用；它不是一个有限角样本的推测。式(33)提供直接可用的定向积分入口：原准确 scalar、实际所选 mean 根及现有切点即可决定符号，无需新的优化方程。

若能够证明 integrand 全非正，则 \(G_{q_+}\ge|z|(X-Y)>0\)。一个充分但非必要的特殊情形是
\(z>0,p\ge0,B_0\le0,C_0\ge0\)。当前 reference 的准确接口使用 \(C_0\ge0\) 分支，prefix 实现取正平方根；prefix 的 \(B_0\) 使用真实 quintic 导数的双向包围。本文没有把这条双向包围偷偷改成全负导数，也没有代替原完整 scalar 费用。

### 7.4 不需要知道 scalar 符号的保守充分界

公共非中央切向量是单位向量，所以其 \(w\) 分量不超过1。第一中央入口因此满足
\[
 G_{q_+}|_{I_1}\ge |z|(X-Y)-a_1.
 \tag{34}
\]
当前固定支持为
\[
 (S/32,15S/32),\qquad(17S/32,31S/32),
\]
物理端层总长为 \(b\)，每端 \(b/4\)，故
\[
 a_1=S/32+b/4.
\]
在拟保留的 \(b/S=1/2\) 输入中，\(a_1=5S/32\)、\(\ell=3S/16\)。
于是
\[
 |z|(X-Y)>5S/32
 \tag{35}
\]
是第一整中央段严格改善的一个完整充分条件。它不是新的运行准入门，尚未获得实际 \(z,S\) 余量，本文没有宣称(35)已满足。

同样，直到第二中央段末端的非中央长度为
\(3S/32+3b/4\)。因此更粗的全前缀条件
\[
 |z|(X-Y)>3S/32+3b/4
 \tag{36}
\]
可保证所有 \({\cal A}>0\) 位置的轴上改善。实际应用优先使用(33)的定向积分，不能因为(36)不通过就判定反号方案无效。

R717 已给固定初始轴差
\[
 X_*-Y_*=\frac{4714}{5005}>\frac{47}{50},
 \qquad |(X-Y)-(X_*-Y_*)|\le14\cdot2^{-53}.
\]
这只支付轴差这一项；它不支付 \(z\)、前缀积分或当前自由核心变化后的新轴差。

## 8. 与真实有限screen记录的关系

当前 geometry 完整源 b46cd96f 的 amplitude 定义确为(20)。同一来源中，有限 reach 量为
\[
 g_{\rm reach}=0.03\,D_{\rm screen}K_{\max}-0.992,\qquad
 D_{\rm screen}=\max(2,2|H|,2\max_{\rm read}|F|),
 \tag{37}
\]
并使用完整六 jet 的真实两支 principal curvature；这里不存在把粗 \(|F_{ss}|\) 三角界换成同一精确 \(2\times2\) 公式就能消除的余量。

已读的 run29 小 index 是固定提交
fec2ee37e0befe693af53f92b3b12bf91b83305f 下
notes/2026-11-28-public-actions-46112781312-1.md，
54,453 B，whole SHA256
e45300467d9831e18a101f391b1febc5772d1a58cdc4509c74522b896f4fc377，
Git blob 40181e1584e7eb7cfcb2780917d271c47bb0aaa7。

该真实可变观察记录当前初点
7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47，
报告有限 reach 为
\(-0.03483574522714061\)，distance_plus 为
\(0.1399812067124947\)，距离角为 \(\pi/2\)。
它没有完整 immutable 科学报告、准确 mean 冠或连续 geometry 证书。距离热点的 \(s\)、cell、\(F\) 和 \(w\) 未在该公开字段中返回。曲率热点的材料位置是另一个观测，不能拿来填距离热点。

因此本次选择反号具有以下具体检验意义：它直接改变(20)依赖的中间位置，同时不改准确边界均值与中央径向转角速度范数；相比继续仅从 \(1/b\) 或 \(1/(1-\epsilon)\) 系数外推，它隔离了一个更直接的位移自由度。但(19)的符号、原两见证的完整余量以及新的 normal 场仍必须由原完整科学计算和准确费用决定。没有把有限 reach 负值当成已通过的连续 reach。

## 9. 固定度量、相位、帽、握持和未标记全等

两种输入都使用同一固定
\(g=ds^2+a(s)^2d\Theta_0^2\)、同一 \(S,H_0,\Gamma,R\)、两等长中央段和全部原变量空间。由(10)，第一中央段以前及第二中央段以后位置和完整角 jet 相同，故原 core/cap 邻域、平帽和其中固定标记不变。

若一个声明为固定握持区的材料集合落在中间 \({\cal A}\ne0\) 区域，不能以“它的切向量没有改”证明其像不变；必须按(13)处理。本文只保留原端口/帽上已固定的握持构造，不把任意中间集合改称固定。

因为 \(\sigma\) 是与 \(s\) 之外的角、mean方向、外层点无关的固定标量，原正交数据协变满足
\[
 d\mapsto Od,\quad w\mapsto Ow,\quad
 T^\sigma\mapsto OT^\sigma .
\]
这保留 R724/R726 的明确半转、反射和
\(\zeta=\Theta_0^{-1}(\Theta_0(\varphi)-\pi t/2)\) 全相位公式的条件范围。当前 normal32 分支、全相位取向、闭面嵌入与 mixed support/reach 仍要各自支付。

此协变把同一 \(\sigma\) 的数据映到同一 \(\sigma\)，不会自动把 \(\sigma=+\) 变成 \(-\)。材料径向反转也交换真实 core/cap 端条件，不能直接当成现有输入的同参数对称。以上只排除了这两种未经证明的显式等同；本文**不声称**两个整像在任意材料重标记或包含反射的 \(E(3)\) 商下不全等。R716 的中心矩、不交、标记相加和 \(\delta_E\) 解释仍须同场实际证据。

## 10. 完整场与工作误差不能由种子恒等式继承

实际外层场还包含全部 current core、三通道 SO3 控制、真实 Q、reference calibration、32个 normal 阶段、raw closure lift 和原完整 working 积分。这些对象对 seed 的位置和角 jet 都敏感。

- 即使准确 \(B,K,r,d,\lambda\) 方程不变，新的 source/model 与物理场函数不同。原 accepted/final、缓存、工作 closure 值、normal 根或 Gram/K 数值不能迁为新结果。
- 若有 independently paid 的完整场误差
  \(|\widetilde F^\sigma-F^\sigma|\le e_\sigma\)，才可用
  \[
  |\widetilde F^--q|
  \ge |F^--q|-e_-
  =\sqrt{|F^+-q|^2+4{\cal A}G_q}-e_-
  \tag{38}
  \]
  或与原场误差结合的保守三角不等式。本文没有填入这样的误差。
- 原 whole-cell 8点 Gauss 和 partial Lagrange积分规则保留；种子计划中的准确切点不会自动改变外层工作求积。真实物理片、两中央符号、全部角和尾的准确后继必须明确接入。
- R727 精确球面均值/两角/投影架/profile 责任保留；新准确 radial 必须同时翻转 \(T,T_s\)、全部两角 jet 与中央 primitive 的横向项，不能只改某个显示标签或只改切向量。
- R723 支持/曲率/D/全相位与独立无标记 tube、R718 同场 \(\sigma\)、R716 全十二矩、全部 mesh/t 精化均需要新完整来源。本文不制造旧八角色或后验 bool 的通过值。

## 11. 已完成的最小完整科学入口

新完整 seed 文件：

[fixed_fejer_R728_reversed_spherical_halfwave_meridian_reference.py](../scripts/resume_20261126/fixed_fejer_R728_reversed_spherical_halfwave_meridian_reference.py)

- 53,384 B。
- SHA256 c6fc04db9223981e1829620613c71de4c0bec93813ec0eeaf5f8ef7770217e86。
- Git blob 11143579520b9509d4d95323052743031f317e6b。
- 固定 PHYSICAL_CENTRAL_POLARITY=-1。
- 完整 physical model 和 paired definition 明列 \([-1,+1]\)。
- 没有新科学 CLI；原 SeedParameters 构造参数、全部数值/域/预算保持。
- 唯一数值算式改变位于 _cutoff_and_profile 的整中央段 sign。其余变化是独立真实 schema、完整物理 model 参数和说明。

完整父 seed 是1764，52,457 B；
共享完整 mean 是2513，48,226 B。后者的每一字节保留，不能只复制一个近似 helper 摘要。

当前旧源码没有可从 CLI 直接指定的全局 polarity 参数。控制 bubble 的符号也不是这个物理自由度；改变两泡参数不能被描述为已经实施(7)。本次以独立完整 source 固定负 polarity，避免冒用旧 source SHA 或在外部偷偷覆写函数。

后继科学家族须以这份 seed 的完整身份递归派生真实 base/Q/calibration、normal/helper/帧/packet、source binder、curvature-cache selector、geometry、driver/pure/launcher。必须保留完整历史来源和实际 registry，具体角色数以最终真实全表为准，不因本论文预先写成“138”。旧137角色及全部变量/参数不应被裁掉；共享2513、固定输入和观察器能逐字共享时就完整共享。

本文交付的是完整可实施的新 seed 和全条件证明。全家族接线、完整原预算的独立运行和后续准确费用继续进行；未来 run/model/point/report/根/证书身份均未填写。
