# R133 续篇：moving 全状态校正到完整几何预算

**状态：已证明的条件定理。** 本文消费同一个最终精确 GC 解与一个指定的完整 moving 候选之间的误差。它不证明该精确解已经存在，也不把部分连续 native、浮点样本或未闭合主体升级为闭面证书。新的位置/法向账只使用真正的 mean 离零；真正主曲率仍单独使用点态 v-gap。

前置为[完整 moving 标架及均值残差恒等式](R133-supplement-moving-frame-with-complete-residual-and-mean.md)及[闭面支撑、曲率与 reach 定理](R133-supplement-Czero-curvature-frame-residual-and-global-geometry.md)。本篇补上两者之间的完整非线性差分消费者，允许目标度量参数也有误差，不要求候选满足 GC。

## 1. 同一物理对象、同一世界坐标与全部角模

真实对象的径向度量为
$$
 g=a^2(\gamma^2dr^2+d\theta^2),\qquad \beta=a'/a,
$$
真实 moving 状态为 $u,v$，$m=\langle v\rangle<0$，$v<0$。带帽字母表示已经指定的候选状态及参考径向系数。所有 $\phi$ 范数均取完整四重周期 $\pi/2$，保留 mean 和所有角模。令
$$
 \|f\|_{\mathcal A}=\sum_{n\in\mathbb Z}|\widehat f_n|,
 \qquad f(\phi)=\sum_n\widehat f_n e^{4in\phi}.
$$
于是 $\|fg\|_{\mathcal A}\le\|f\|_{\mathcal A}\|g\|_{\mathcal A}$，
$\|f\|_\infty\le\|f\|_{\mathcal A}$，mean-zero primitive 满足
$\|If\|_{\mathcal A}\le\|f\|_{\mathcal A}/4$。

每个实际闭径向盒上给定全圆有效的非负上界
$$
 \|\widehat u\|_{\mathcal A}\le U,\quad
 \|\widehat v\|_{\mathcal A}\le V,\quad
 \|u-\widehat u\|_{\mathcal A}\le e_u,\quad
 \|v-\widehat v\|_{\mathcal A}\le e_v,\quad
 |m-\widehat m|\le e_m\le e_v.
 \tag{M.1}
$$
必须使用真实 mean 误差 $e_m$，不把它置零。设
$$
 |\widehat m|\ge\mu,\qquad \mu_t=\mu-e_m>0.
$$
另有真实径向系数差
$$
 |a-\widehat a|\le e_a,\quad |\gamma-\widehat\gamma|\le e_\gamma,\quad
 |\beta-\widehat\beta|\le e_\beta,\quad |K-\widehat K|\le e_K.
 \tag{M.2}
$$
以下写
$$
 a_+=\widehat a+e_a,\quad
 G=\widehat\gamma+e_\gamma,\quad
 g=\widehat\gamma-e_\gamma>0,\quad
 B=|\widehat\beta|+e_\beta,\quad k=|\widehat K|+e_K.
$$
若这些符号使用盒上界/下界，所有式子均按有利方向取界。特别，
$E_\nu=E\exp(\nu h)$ 的实际族中 $a,\beta$ 不随 $\nu$ 改变，可准确置
$e_a=e_\beta=0$；$\gamma,K$ 的真实变化仍按(M.2)支付。若同时改变原 affine 参数，不得仍省掉 $e_a,e_\beta$。

在每个精确解的真实 lift 中比较相同的 $(r,\phi)$。这不等于比较相同的物理 $\theta$，但每个 lift 是整个圆的双射，因此这种配对直接控制**全像** Hausdorff 距离。所有外端位置和框架必须已经选在同一个世界坐标系；最终 phase 族不得逐时另作刚体对齐来减小本篇误差。

## 2. 完整 drift 与连接的非线性差分

令
$$
 \widehat S=\widehat u^2+\widehat K\widehat v^2,\quad
 S=u^2+Kv^2,\quad
 \widehat d=-\widehat\beta I\widehat S,\quad d=-\beta IS.
$$
可取
$$
 \widehat S_* = U^2+|\widehat K|V^2,\qquad
 D=|\widehat\beta|\widehat S_*/4,
$$
$$
 \Delta S=(2U+e_u)e_u+k(2V+e_v)e_v+e_KV^2,\qquad
 \Delta d=\frac14\bigl(B\Delta S+e_\beta\widehat S_*\bigr).
 \tag{M.3}
$$
若已经有更紧的真实 $\|\widehat d\|_{\mathcal A}$，可用它代替 $D$。
(M.3)来自准确差分
$S-\widehat S=(u+\widehat u)(u-\widehat u)+
K(v+\widehat v)(v-\widehat v)+(K-\widehat K)\widehat v^2$
和 $d-\widehat d=-\beta I(S-\widehat S)-(\beta-\widehat\beta)I\widehat S$。
因此无限高模、nonmean primitive 和整个 mean 均未删去。

记
$$
 R_v=\frac{e_v}{\mu_t}+\frac{V e_m}{\mu\mu_t},\quad
 R_u=\frac{e_u}{\mu_t}+\frac{U e_m}{\mu\mu_t},\quad
 R_1=\frac{e_m}{\mu\mu_t}.
 \tag{M.4}
$$
此处 $R_v,R_u$ **仅为比值差上界**，不与前置篇的 GC 方程残差混用。准确比值恒等式给
$$
 \|v/m-\widehat v/\widehat m\|_{\mathcal A}\le R_v,\quad
 \|u/m-\widehat u/\widehat m\|_{\mathcal A}\le R_u,\quad
 |1/m-1/\widehat m|\le R_1.
$$

定义 $\tau=dv/m-\gamma u$ 及其带帽对应物。取
$$
 T=DV/\mu+\widehat\gamma U,\qquad
 \Delta\tau=DR_v+\frac{V+e_v}{\mu_t}\Delta d+G e_u+e_\gamma U.
 \tag{M.5}
$$
则 $\|\widehat\tau\|_{\mathcal A}\le T$、$\|\tau-\widehat\tau\|_{\mathcal A}\le\Delta\tau$。
按完整标架篇取
$$
 p=\beta\tau/\gamma,\qquad q=a(\gamma Kv+du/m),\qquad t=ad/m.
$$
无需任何点态 $1/v$ 分母，下列量控制真实连接之差：
$$
 \Delta p=\frac{B}{g}\Delta\tau+
 T\left(\frac{e_\beta}{g}+
 \frac{|\widehat\beta|e_\gamma}{g\widehat\gamma}\right),
$$
$$
 Z=\widehat\gamma|\widehat K|V+DU/\mu,
$$
$$
 \Delta Z=Gk e_v+
 V\bigl(G e_K+|\widehat K|e_\gamma\bigr)+
 DR_u+\frac{U+e_u}{\mu_t}\Delta d,
$$
$$
 \Delta q=a_+\Delta Z+e_a Z,\qquad
 \Delta t=a_+\left(\frac{\Delta d}{\mu_t}+DR_1\right)+e_aD/\mu.
 \tag{M.6}
$$
证明只须依次拆分 $\gamma Kv-\widehat\gamma\widehat K\widehat v$、
$du/m-\widehat d\widehat u/\widehat m$、$ad/m-\widehat a\widehat d/\widehat m$，再用
$|\gamma K-\widehat\gamma\widehat K|\le G e_K+|\widehat K|e_\gamma$。
每个拆分都保留其实际交叉项，(M.6)不是一阶线性化。

对
$$
 \Omega(x,y,z)=
 \begin{pmatrix}0&-x&-y\\x&0&-z\\y&z&0\end{pmatrix}
$$
有准确恒等式 $\|\Omega(x,y,z)\|_{\rm op}=\sqrt{x^2+y^2+z^2}$。
故完整真实径向连接满足
$$
 \sup_\phi\|\Omega_r-\widehat\Omega_r\|_{\rm op}
 \le C_\Omega=\sqrt{(\Delta p)^2+(\Delta q)^2+(\Delta t)^2}.
 \tag{M.7}
$$
而 $f_r=(a\gamma,a\tau,0)^T$ 满足
$$
 \|\widehat f_r\|_\infty\le L=\widehat a\sqrt{\widehat\gamma^2+T^2},
$$
$$
 \|f_r-\widehat f_r\|_\infty\le C_f=
 \sqrt{(a_+e_\gamma+e_a\widehat\gamma)^2+
             (a_+\Delta\tau+e_aT)^2}.
 \tag{M.8}
$$

## 3. 普通径向积分误差和真实接口全部进入预算

令真实 $Q=(X,Y,N)$ 满足 $Q_r=Q\Omega_r$、$Q^TQ=I$。选取指定的可计算参考 $\widetilde Q,\widetilde F$；它们可为保存的有限径向多项式或经严格验证的积分轨迹，不要求参考已经是等距浸入或精确正交。定义其**实际**普通残差
$$
 E_Q=\partial_r\widetilde Q-\widetilde Q\widehat\Omega_r,\qquad
 E_F=\partial_r\widetilde F-\widetilde Q\widehat f_r.
$$
给定 $\|E_Q\|_{\rm op}\le\rho_Q(r)$、$|E_F|\le\rho_F(r)$ 的完整连续界。
在实际外端 $R$，给定同一世界坐标中
$$
 \|Q-\widetilde Q\|_{\rm op}\le b_Q,\qquad
 |F-\widetilde F|\le b_F.
$$
这两个外端费必须来自真正的 cap/long/tail 匹配；不能因为用了旋转圆初值就把它们置零。

若参考框架、位置在有限接口 $s_j$ 有实际跳，分别记其全圆范数上界 $J_{Q,j},J_{F,j}$。逐段相减：
$$
 (Q-\widetilde Q)_r=(Q-\widetilde Q)\widehat\Omega_r
       +Q(\Omega_r-\widehat\Omega_r)-E_Q.
$$
$\widehat\Omega_r$ 反对称，齐次右传播正交。由变常数公式及 $Q$ 的单位算子范数，
$$
 \Theta(r)=b_Q+\int_r^R(C_\Omega+\rho_Q)\,ds+
                      \sum_{r<s_j\le R}J_{Q,j}
 \tag{M.9}
$$
控制 $\sup_\phi\|Q-\widetilde Q\|_{\rm op}$。再用
$$
 (F-\widetilde F)_r
 =(Q-\widetilde Q)\widehat f_r+Q(f_r-\widehat f_r)-E_F
$$
得
$$
 \Phi(r)=b_F+\int_r^R(L\Theta+C_f+\rho_F)\,ds+
                         \sum_{r<s_j\le R}J_{F,j}.
 \tag{M.10}
$$
位置和法向误差分别不超过 $\Phi,\Theta$。这里没有指数 Gronwall 乘子，也没有对状态校正作角微分或除点态小 $v$。

将(M.9)代入(M.10)可用非负 Fubini 保留相关性。若
$\ell(r,s)=\int_r^sL(t)\,dt$，则
$$
 \Phi(r)=b_F+\ell(r,R)b_Q
 +\int_r^R\ell(r,s)(C_\Omega+\rho_Q)(s)\,ds
 +\int_r^R(C_f+\rho_F)(s)\,ds
 +\sum_{r<s_j\le R}\{\ell(r,s_j)J_{Q,j}+J_{F,j}\}.
 \tag{M.11}
$$
逐真实闭盒做这个双积分可避免把外端误差乘整条带的粗最大长度。

PPoly **状态系数**的两侧跳不是自动等于参考框架跳。若按分段连接连续积分参考框架，则 $J_{Q,j}=0$，但状态的真实跳仍必须进入精确 BVP 的接口源；其角连接/位置约束跳按前置篇(13)完整支付。若数值轨迹本身不连续，才使用本节对应的 $J_Q,J_F$。不能把两者混成零，也不能将一个状态跳凭空再当径向 delta 连接重复计入。

还有一个必须保留的区别：在未解候选上
$$
 \widehat\theta_r=\widehat\tau+
 \widehat m^{-1}I(\mathscr R_v-
                      \widehat v\langle\mathscr R_v\rangle/\widehat m).
$$
因此 $\widehat\Omega_r,\widehat f_r$ 是前置篇的**模型 moving 连接**；
不能称它们是未解候选物理坐标的准确拉回。上述差分定理只把它们当指定参考连接，因而完整成立。若使用原物理角积分器，须额外保留这项真实坐标源，不能把两个程序的输出直接混用。

## 4. 全状态 H1 误差可直接消费

取完整归一化范数
$$
 \|f\|_{H^1_4}^2=\sum_{n\in\mathbb Z}(1+16n^2)|\widehat f_n|^2.
$$
Cauchy–Schwarz 及 $\sum_{n\ge1}n^{-2}=\pi^2/6$ 给
$$
 \|f\|_{\mathcal A}
 \le\left(1+2\sum_{n\ge1}(1+16n^2)^{-1}\right)^{1/2}\|f\|_{H^1_4}
 <\frac{11}{10}\|f\|_{H^1_4}.
 \tag{M.12}
$$
因为括号小于 $1+\pi^2/48<1+10/48<121/100$。
常数包含完整 $n=0$ 行；并未使用 mean-zero 假设。
所以真正全局逆/非线性定理若输出同一 moving 状态的完整 $H^1_4$ 校正，可逐分量乘 $11/10$ 输入(M.1)。
若输出的是已变分的 physical 状态、加权 Airy 状态或两个分量之一，则先消费其**完整**坐标、mean 和端口转换，不能把它直接写成(M.1)。
归一化未知量 $U,V$ 的误差也须乘实际 $\alpha$，并包含真实基线 $s_\nu$ 的变化。

## 5. 主曲率另用真实点态 gap

设全圆 $\inf|\widehat v|\ge b>0$ 且 $b_t=b-e_v>0$。形式候选矩阵
$$
 \widehat S_{\rm II}=
 \begin{pmatrix}
 \widehat K\widehat v+\widehat u^2/\widehat v&
                         \widehat u/\widehat v\\
 \widehat u/\widehat v&1/\widehat v
 \end{pmatrix}
$$
不必是参考位置 $\widetilde F$ 的真实形算子。它只是有明确完整谱的代数比较矩阵。
真实精确解的正交形算子由 GC 准确给出同式无帽矩阵。取
$$
 d_A=k e_v+e_KV+\frac{(2U+e_u)e_u}{b_t}
                       +\frac{U^2e_v}{b b_t},\quad
 d_B=\frac{e_u}{b_t}+\frac{Ue_v}{b b_t},\quad
 d_C=\frac{e_v}{b b_t}.
$$
每项来自准确商差，故
$$
 \|S_{\rm II}-\widehat S_{\rm II}\|_{\rm op}
 \le \max(d_A+d_B,d_B+d_C),\qquad
 \kappa_{\rm true}\le\widehat\kappa+
                      \max(d_A+d_B,d_B+d_C).
 \tag{M.13}
$$
$\widehat\kappa$ 须是整个候选代数矩阵的严格最大绝对特征值界。
它可以由真连续 native 支付；有限点采样不够。
这是唯一需要点态 $v$ 分母的曲率账，与(M.3)–(M.11)的仅 mean 分母位置/法向账明确区分。

## 6. 从真正的全域覆盖到最终三项几何门

本节各界要求覆盖完整主体、两帽、无限尾和平端，并对整个最终 phase 参数区间一致。只验证 $0\le r\le25/8$ 不能使用本节的闭面结论。

设在同一个世界原点下已经严格支付参考全域界
$$
 |\widetilde F|\le R_*,\qquad
 \widetilde F\cdot\widetilde N\ge\sigma_*,
$$
以及 $\Phi\le\varepsilon_F,\Theta\le\varepsilon_N$。真实法向单位长度给
$$
 F\cdot N\ge\sigma_*-\varepsilon_F-R_*\varepsilon_N
                         =:\sigma>0.
 \tag{M.14}
$$
证明是准确拆分
$F\cdot N-\widetilde F\cdot\widetilde N
=(F-\widetilde F)\cdot N+\widetilde F\cdot(N-\widetilde N)$；
无须假设 $\widetilde N$ 已单位化。
对由完整 GC/接口产生的连通闭 $C^2$ 浸入，正支撑使径向投影成为
到 $S^2$ 的局部微分同胚。紧致性给覆盖，$S^2$ 单连通和连通性给单层覆盖，
于是实际浸入为嵌入。前置闭面几何篇§5遂给
$$
 \operatorname{reach}(F_t(M))\ge
             \min\{\sigma_t,\,1/\kappa_t\}.
 \tag{M.15}
$$
这里 $\kappa_t$ 使用(M.13)的真实曲率，不能用参考数值积分曲率样本替代。

设 $D_*$ 为参考初始全像直径的已证上界，
$b_*$ 是真实固定握持区像直径的已证下界。
若同一世界坐标下，某个参考末像点到参考初像的**全像**距离已经证为至少 $w_*$，则完整集合的三角不等式给
$$
 D\le D_*+2\varepsilon_{F,0},\qquad
 d_H(F_1(M),F_0(M))
 \ge w_*-\varepsilon_{F,0}-\varepsilon_{F,1}.
 \tag{M.16}
$$
故以下是真正可以直接消费的充分几何门：
$$
 b_*\ge\frac15(D_*+2\varepsilon_{F,0}),\qquad
 w_*-\varepsilon_{F,0}-\varepsilon_{F,1}
       \ge\frac1{20}(D_*+2\varepsilon_{F,0}),
$$
$$
 \inf_t\min\{\sigma_t,1/\kappa_t\}
       \ge\frac3{100}(D_*+2\varepsilon_{F,0}).
 \tag{M.17}
$$
它们不包含任何逐时对齐变换；固定 $H$ 及其内部非空由实际共同帽构造另行给出。
若同一最终族具有前置 R17 的四个不同、非共面固定曲率标记，
任何全等必须逐点固定这四点，因此连反射在内都只能是恒等。
(M.16)的正位移遂排除全等；欧氏群在两紧像上将平移限制到有界集后，
正交群紧致性给 $\delta_{\rm E}>0$。不能把纯相位旋转本身当成这一结论。

完整覆盖的一个实际入口如下。若参考全圆全径向导数分别有
$|\widetilde F_r|\le L_r$、$|\widetilde F_\phi|\le L_\phi$，
一张覆盖所有闭盒的样本网对每点提供同盒网点，坐标距离不超过
$\Delta r/2,\Delta\phi/2$，则它是误差
$$
 h\le L_r\Delta r/2+L_\phi\Delta\phi/2
 \tag{M.18}
$$
的全像网。准确样本见证距离的下界 $d_{\rm grid}$ 因而只给
$w_*\ge d_{\rm grid}-h-e_{\rm witness}$，
其中 $e_{\rm witness}$ 是见证坐标的实际误差。
最近样本距离未经这一扣减只是连续最近距离的上界。
没有网的帽/平端必须另用完整包围盒或集合距离界，不能忽略。

对本篇模型连接参考，可用
$L_r\le\|\widetilde Q\|_\infty L+\rho_F$；
角向使用前置篇的完整 curvature/torsion 传播及真实跳得到
$|\widetilde F_\phi-\widetilde Q(0,\widehat a\widehat v/\widehat m,0)^T|
\le P_*$
后，取
$L_\phi\le\|\widetilde Q\|_\infty\widehat aV/\mu+P_*$。
浮点参考的径向/角向误差也须支付；不能仅凭 FFT 采样声称这个连续角界。

## 7. 对当前主线的准确含义

(M.3)–(M.11)在 $v$ 的腰部尖峰附近仍只有真实 mean 分母，
并允许原 $\nu$ 校正产生的目标系数差；(M.12)把完整状态 $H^1$
直接送入这些账；(M.13)只在最后实际主曲率处付点态 $v$-gap。
这给同一个已选最终中心的全局逆、非线性校正与最终几何之间一个闭合的条件接口。

本篇没有新的执行环境，也未运行丢失的7296盒连续计算、未完成的全域几何，
或任何全局逆/远端 $F$ 求解。其结论属于本题 README 明确列出的条件性中间进展。
下一消费者仍必须实际给出(M.1)–(M.2)、所有径向普通源和接口、
真正共同外端匹配以及(M.14)–(M.18)的全域数值，方能使用最终比例结论。
