# R119 续篇：同一对象提高角阶的准确收益与真实 mean / 低模障碍

2026-11-15，visible-exact / tail_connector。

**状态：已证明（解析结论）。** 本篇固定已经发布的同一个
$\mathsf K=2^{128}$、深层 $\zeta_j\asymp\delta_j^{131}$ 对象，
不改变 profile、共同五盒参数点、两条 $\Gamma^*$ 或 fixed stop。
结论区分提高角阶所得的 remaining 高频收益，与完整解中不具有
该收益的真实 mean 和固定低频。以下反例都是准确方程的解；
它们不是把一个预算上界当作实际误差下界。

依赖为：

* [当前全标签与原单位](R119-supplement-controlled-profile-full-label-and-raw-ports.md)，
  C.2、C.3、C.6、C.8--C.12、C.24、C.34、C.40--C.48；
* [强尾完整标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)，
  U.2、U.7--U.13；
* [真实深低 Green / Poisson](R119-supplement-complete-deep-low-Green-Poisson-and-mixed-elimination.md)，
  L.5--L.13；
* [1024阶完整网络](R119-supplement-complete-1024-angular-Sobolev-network-and-physical-cap-Schur.md)，
  U.1--U.3，及
  [强层与物理二 jet](R119-supplement-strong-layer-decay-and-physical-flat-end-C2-reconstruction.md)，
  D.1--D.8；
* [固定径向 ordinary 源逆](R119-supplement-fixed-radial-root-sources-and-complete-ordinary-C2-inverse.md)，
  K.29--K.34。

这里只要在允许的径向成员 $a=0$ 上给出反例，即足以排除覆盖整个
实际背景族的更强统一声明。没有把径向公式转授到非径向背景。

## 1. 全部原单位与真实兼容

记
$$
 \delta_j=(2/25)2^{-j},\qquad
 \zeta_j=\epsilon\delta_{8192}^{-485/4}\delta_j^{131}
 \quad(j\ge8193),\qquad
 \mu_j=\epsilon\delta_{4096}^{3/2}\delta_j^{9/2}.
 \tag{A.1}
$$
固定材料 $t=\log r$ 和物理高度 $h$。实际径向系数是
$$
 \mu_0=\frac{\mu_jp_*}{\rho r^8},\qquad
 (\mu_0h_t)_t+\mu_0Qm^2h=f,\qquad
 N_m=\frac{r^4f_m}{12\mu_j}.
 \tag{A.2}
$$
因此 ordinary 源仍与原 $N=\mu_jp_*^2e/(12r^{10})$ 相同；
未删除任何 $p_*$、$\mu_j$ 或 $\rho$ 因子。mean 时准确为
$$
                  \pi_t=f_0,\qquad \pi=\mu_0h_t.
 \tag{A.3}
$$
本篇所有构造都取唯一平端高度为0，并保持真实端点高度、
总通量、帽和外返回的边界条件。两条 $\Gamma$ 方向以及 $\nu$
均取0。这是完整源系统的一个合法子类，不是删除这些列后的
替代系统。

对任意有限角阶 $s\ge0$ 写
$$
 \mathcal S^{(s)}
   =\sup_{j\ge129}\frac{\delta_j^4}{\zeta_j}
                       \sup_{t\in I_j}\|N(t)\|_{H^s_\theta}.
 \tag{A.4}
$$
下述 mean 源还属于原 $\mathcal S_{2,\beta}$ 的每个角解析窗，
因为只有 $m=0$ 一项。

## 2. 一个精确紧支 mean 源：角上 entire 仍只有 $\delta^{128}$ 二 jet

每个深胞元有真实 $Q=7$、$p_*$ 常数的主平台。C.3 给它的
$y=\sqrt{12}t$ 长度至少 $\delta_j-\eta_j/8>\delta_j/2$，
不论当前两 bump、平移和形状参数的具体允许值。
在该平台中点 $t_j$ 取
$$
 \ell_j=\frac{\delta_j}{8\sqrt{12}},\qquad
 b(x)=
 \begin{cases}(1-x^2)^4,&|x|\le1,\\0,&|x|>1,\end{cases}
 \qquad
 h_j(t,\theta)=\zeta_j\delta_j^{-1}
                   b((t-t_j)/\ell_j).
 \tag{A.5}
$$
支集的两端严格位于同一常平台内。函数 $b$ 为 $C^3$，
$b'(0)=0$、$b''(0)=-8$，且
$|b|\le1$、$|b'|\le8$、$|b''|\le56$。
定义准确源
$$
                   f_j=(\mu_0(h_j)_t)_t .
 \tag{A.6}
$$
在整个支集上 $\mu_{0,t}=-8\mu_0$，所以
$$
 N_j(t)=\frac{p_*}{12\rho r^4}
                      \big((h_j)_{tt}-8(h_j)_t\big).
 \tag{A.7}
$$
这是真实普通源，既不是 weak delta 源，也没有人为增添源端跳。

由 $\ell_j^{-1}<2^5\delta_j^{-1}$、
$\ell_j^{-2}<2^{10}\delta_j^{-2}$ 得
$$
 |(h_j)_t|<2^8\zeta_j\delta_j^{-2},\qquad
 |(h_j)_{tt}|<2^{16}\zeta_j\delta_j^{-3}.
$$
再用 $1\le r\le2$、$p_*\le\mathsf K/\delta_j$，完整范数满足
$$
             \mathcal S^{(s)}(f_j)
                  <2^{17}\mathsf K/\rho
                  \qquad\text{对每个 }s\ge0 .
 \tag{A.8}
$$
右端与 $j$、$s$ 无关，mean 的 $H^s$ 权正好为1。
将 (A.5) 统一乘以 $\rho2^{-145}$ 即可令右端小于1。

在平台中心则有准确值
$$
 (h_j)_t(t_j)=0,\qquad
 |(h_j)_{tt}(t_j)|=6144\zeta_j\delta_j^{-3}.
 \tag{A.9}
$$
物理径向坐标为 $\rho r$；因此该点的物理二阶导数下界为
$$
 \left|\partial_{\rho r}^{\,2}h_j(t_j)\right|
 =\frac{|(h_j)_{tt}(t_j)|}{\rho^2r_j^2}
 \ge 2^{10}\rho^{-2}\epsilon\delta_{8192}^{-485/4}
                                     \delta_j^{128}.
 \tag{A.10}
$$
它是实际解的下界，不是某个估计未能改善。

两端 $h_j=(h_j)_t=0$，故整个胞元
$\int f_j\,dt=[\mu_0(h_j)_t]=0$，所有物理外迹也为0。
在其余全部胞元、有限外段、长段和帽上接0，就得到完整闭系统的
可解源，真实 flux 兼容恰为0，平端 gauge 恰为0。
原增广辅助列不被激发。

还可对全部 $j\ge j_0\ge8193$ 取不交支集的和
$h=\sum_jh_j$、$f=\sum_jf_j$。局部有限和与 (A.9) 的正衰减
给真正平端 $C^2$ 解；$f$ 连续且 (A.8) 仍成立。
每个胞元的总 charge 分别为0，所以无穷和不产生隐藏的端荷。
这个单一源属于所有角 Sobolev 窗和所有角解析窗，但对任意
$\gamma>128$，
$$
       \sup_{j\ge j_0}\delta_j^{-\gamma}
                    \|h\|_{C^2_{\rm phys}(I_j)}=\infty.
 \tag{A.11}
$$
因此增加角阶或缩小一个非零的全局源半径，都不能把泛
$\mathcal S^{(s)}$ 普通源的完整二 jet 声明提升为
统一 $\delta_j^{150}$。

## 3. 连深尾无体源也仍有固定 $m=4$ 的真实衰减上限

mean 不是唯一原因。现在固定 $m=4$，并仅研究第 $j_0\ge8193$
层以后的准确齐次径向尾。C.8--C.9 给
$$
 \nu_4=20,\qquad \alpha=65/64,\qquad C=16\sqrt2,
$$
$$
 B^\infty=
 \begin{pmatrix}
 1-\mathsf K\alpha\nu_4&\alpha\nu_4\\
 (\mathsf K\alpha\nu_4-\mathsf K-1)/C&(1-\alpha\nu_4)/C
 \end{pmatrix}.
 \tag{A.12}
$$
记 $-B^\infty$ 的大根为 $\Lambda_4$、小根为
$\lambda_4=(C\Lambda_4)^{-1}$。强尾 U.7 的准确公式给
$$
 (\mathsf K-1)\alpha\nu_4
       <\Lambda_4<(\mathsf K+1/16)\alpha\nu_4,\qquad
                    2^{132}<\Lambda_4<2^{133}.
 \tag{A.13}
$$
这里没有把谱常数等同于 proof weight $\zeta$。

原 canonical 两态在真正 $p_*=1$ 接缝满足
$W_{j-1}=B_jW_j$。取同一个实特征基
$E=\left(\begin{smallmatrix}1&t\\s&1\end{smallmatrix}\right)$，
其正逆范数均小于2、$|s|<1/16$、$0<t<1/(\mathsf K-1)$。
定义只去掉交替号的真实态
$$
       z_j=(-1)^jE^{-1}W_j,\qquad
       z_{j-1}=(\operatorname{diag}(\Lambda_4,\lambda_4)
                                      +\mathcal E_j)z_j .
 \tag{A.14}
$$
这里没有 $\zeta_j$ 或 $e^{4\tau_j}$ 因子。C.11 的真实全参数
误差及 C.34 的准确锥给
$$
 \|\mathcal E_j\|_\infty<2^{290}\sqrt{\delta_j},\qquad
 \frac{\|\mathcal E_j\|_\infty}{\Lambda_4}
                         <2^{158}\sqrt{\delta_j}.
 \tag{A.15}
$$
L.9--L.12 给同一真正无限允许线
$z_j=u_j(1,s_j)^T$、$|s_j|<1/8$。
原 L 中额外的正 scalar Green 归一化不改变此 projective 斜率。
因此在该线第一行准确有
$$
       u_{j-1}=\Lambda_4(1+e_j)u_j,\qquad
                 |e_j|<2^{160}\sqrt{\delta_j}.
 \tag{A.16}
$$
右端误差在 $j\ge8193$ 绝对可和，其总和小于 $1/16$。
从任意非零 $u_{j_0}$ 出发，所有 $1+e_j$ 均为正，
实际有序乘积的正逆均小于2。于是
$$
 \frac12|u_{j_0}|\Lambda_4^{-(j-j_0)}
       <|u_j|<
          2|u_{j_0}|\Lambda_4^{-(j-j_0)} .
 \tag{A.17}
$$
这既保完整小特征方向，也保全部真实短段、两个 bump、
下降坡平移和形状误差；未把 $B_j$ 直接换成 $B^\infty$。

接缝真实物理高度为
$$
 h_4(t_j)=\rho r_j^4 W_{1,j}/\nu_4
       =(-1)^j\rho r_j^4 u_j(1+t s_j)/20 .
 \tag{A.18}
$$
因 $1/2<|1+t s_j|<2$、$1\le r_j\le2$，
它与 $|u_j|$ 以不依赖 $j$ 的正上下常数等价。
令 $\vartheta=\log_2\Lambda_4\in(132,133)$，
(A.17) 等价于
$$
        c|u_{j_0}|\delta_j^\vartheta
         <|h_4(t_j)|<
             C|u_{j_0}|\delta_j^\vartheta ,
 \tag{A.19}
$$
其中 $c,C>0$ 只依赖固定 $j_0,\rho$ 及真实对象。
特别物理 $C^2$ norm 含高度和角二阶导数，不能对该非零尾
成立任何 $\delta_j^\gamma$、$\gamma>\vartheta$ 的统一上界。

这条允许解确实属于原物理平端域：C.12 的完整胞内流、
C.6 的 $p_*^{-1}$ 和原实际 $Q$ 界将两次径向导数至多放大
固定常数乘 $J\delta_j^{-5/2}$，故 (A.19) 仍使完整二 jet趋0。
反射实解由 $m=\pm4$ 配对得到，所有物理 mean 仍为0。

若需要将此尾作为完整闭系统的一个有源解，可在固定有限胞元
内用一个径向 $C^3$ cutoff 接到外侧零解。准确源取实际
$\operatorname{div}(G\nabla h)$；它仅有 $m=\pm4$、只在这个
有限过渡区非零，在无限深尾为0。帽、长段和所有外迹仍可接0，
物理 mean charge为0。该源属于每个有限角窗及每个角解析窗；
原闭系统的域唯一性认同它就是相应源的解。
因此“深尾无体源”也不足以把完整物理层衰减提升到150。

## 4. 新角阶究竟改善哪一项

对于 remaining 的非mean输出，真实分类仍是
$|m|>A_j=2^{-40}\delta_j^{-1/8}$。原谱权
$v_j=2^{-600000}J^{-4165}\delta_j^{1073/32}$ 和
$w_j=\delta_j^{-64}$ 未改变。
若已经在同一实际解上获得 $H^{2048}$ 界，则纯代数地
$$
 \frac{w_j}{v_j}\langle m\rangle^{-(2048-9)}
 \le 2^{681560}J^{4165}\delta_j^{5035/32}
 \qquad ((j,m)\in P_N,\ j\ge8193).
 \tag{A.20}
$$
相对于原 D.7，幂确实增加128；$5035/32=939/32+128$。
本式只作用真实 remaining 非mean压缩，不作用
$m=0$ 或 $0<|m|\le A_j$。
重新证明2048阶完整算子的费用、high阈值、谱权及物理帽反馈
还须按 U 的有限角公式逐项支付，本篇不把 (A.20) 当作这些门的
证明。

固定低模的真正物理递推为 (A.16)，并不含角阶。
在强标签规范
$X_{m,j}=(-1)^j\zeta_j^{-1}e^{|m|\tau_j}W_{m,j}$ 中，
$\zeta$ 与 $e^{|m|h_j}$ 看似出现在单步主因子；
恢复实际 $W$ 后恰相消，留下 $\Lambda_m^{-1}$。
因此不能把 proof cutoff 导出的128层幂再乘到 (A.19)。

## 5. 对真实迭代域的准确含义

本篇没有否定实际二次余项能够留在原强尾域。
对 $m=4$，(A.13) 反而给
$\vartheta-131>1$，所以固定低模的真实齐次高度相对于
$\zeta_j$ 有正幂余量；这个余量应由真实低核单独消费。

同样，[实际非线性 ordinary 源与两 Γ 提升](R119-supplement-exact-nonlinear-ordinary-sources-and-Gamma-reference-height-lifts.md)
Q.14 的固定 metric 余项保留 $C_j^2$，
Q.21 的提升后 metric 源保留
$n_j|\psi_t|+n_j^2|\psi|$。
它们是泛 $\mathcal S^{(s)}$ 的更小子类。
有望返回原 $\zeta^{131}$ 状态域的论证必须使用这些真实额外
消失阶，以及物理 mean 的完整积分、真实高度常数和
两条 $\Gamma^*$ 耦合，不能用“所有源都衰减150”替代。

具体仍待付的量词是：对一个能迭代的同一实际状态域，
完整 inverse是否将上述相关源送回该域，并且角导数损失、
mean charge、外帽与 $\nu$ 条件都保持一致。
(A.20) 本身既不提供原 $\ell^1_{224}$ 输出，也不提供
有限 Sobolev 邻域上的无损非线性逆。
下一项沿真实余项和低核继续，原几何对象及深 profile保持不变。
