# R1061 — 原 p² 反线性粘合、完整 theta 下降与 Miller 规范

日期：2026-11-28 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

本篇消费 [R1054](R1054-original-p-square-depleted-source-and-exact-conductor-blocks.md)
§10 的同一个完整矩阵及实际 Jacobi 字。固定 $p>211$ 为原好惰性素数；
原 $2,3,17$ Schwartz、full2/full9、全部有限 $h$、Artin/Cor 和
两个三挠译像均不改变。本篇所有几何先对**尚未作无穷环面平均的
实际 theta 字**成立。最后一节再准确返回整个平均及临界读者。

所得的新输入是：原 $p^{-2}$ Weyl 和为阶 $p^4$ 图群的真实下降平均；
其极化类型为 $(34,102)$。固定三同源后得到一个明确的主极化
genus-2 Jacobian，但原来源仍保留在其三重盖的两个非平凡三次角色中。
全部 Miller 函数及其刚性化常数、$p$ 进估值和覆盖变量同时确定。
这没有给新的 canonical 零，也没有证明原临界斜率跨 $p$ 非零。

## 1. 原来源、计数与 Haar

令 $K=\mathbf Q(\omega)$、$\delta=1+2\omega$、$\delta^2=-3$，
$t_0=(1+\delta)/2=-\omega^2$。取原
$E_0:y^2=x^3+1$、微分 $dz=dx/(2y)$，
$\sigma(z)=z+\cdots$。原实周期及格为
$$
 \Omega_0>0,\qquad
 \varpi_0=\frac{\Omega_0}{1-\omega},\qquad
 \Lambda=\varpi_0\mathcal O_K
       =\frac{\Omega_0}{\delta}\mathcal O_K .
 \tag{1}
$$
这是原未平方来源笔记(1)及原 psi4 来源§6的规范。
特别 $q_3=(0,1)$ 可取 lift $-\Omega_0/3$，且
$[\delta]q_3=O$；不得把(1)误改成 $\Omega_0\mathcal O_K$。

正来源是原 $S,H_3,H_5$ 中当前已指定的一条 section
$s_+\in H^0(E_0,\mathcal L_{34})$，
$\mathcal L_N=\mathcal O_{E_0}(NO)$，含原 Fourier 的实际幅度。
负来源是原两条真实三挠字
$$
 s_-=
 [\delta]^*
 \bigl(\mathsf T_{q_3}^{34}s_{\rm old}
          +\mathsf T_{-q_3}^{34}s_{\rm old}\bigr)
 \in H^0(E_0,\mathcal L_{102}).
 \tag{2}
$$
这里两个被拉回的 section 分别属于
$\tau_{\pm q_3}^*\mathcal L_{34}$，不能先把它们都看作
$\mathcal L_{34}$ 的自同构像。
原 psi4 来源(22)--(27)、§§10--11已经固定它们的
Gaussian、$c_{q_3}^{34}$、$\delta$ 和三个实际 raw 幅度。
本文使用(2)的整个字，不重选各项的根或首系数。

令 $R=\mathbf Z/p^2\mathbf Z$，$\zeta=\psi_p(1/p^2)$。
R1054(52)--(60)的实际矩阵为
$$
 M=\begin{pmatrix}1/2&1/102\\-153/2&1/2\end{pmatrix},
 \qquad
 K_{A,B}=p^{-2}
       \zeta^{\,51(A^2-4AB+B^2)/2},
 \qquad v_0(A)=\mathbf1_{p\mid A}.
 \tag{3}
$$
两条有限模的维数是 $p^2$；其 Heisenberg 参数群 $R^2$
的阶是 $p^4$。原完整等式是
$$
 K=\frac1{p^2}\sum_{v\in\mathbf F_p^2}
       W_-(\widetilde v)v_0\otimes W_+(M\widetilde v)v_0.
 \tag{4}
$$
两边的 lift 必须共同运输。R1054(59)给出的无省略参数为
$v=(a,51(2c-a))$、$Mv=(c,51(c-2a))$，$0\le a,c<p$。

有限坐标配对下 $\mathcal C=\sum_A e_A^-\otimes e_A^+$，
有 $K=p^{-1}(1\otimes\rho_+(t_0))\mathcal C$。
实际 Haar $\operatorname{vol}(\mathbf Z_p)=1$ 则是
$$
 \langle e_A^-,e_B^+\rangle_{\rm Haar}=p^{-1}\delta_{A,B},
 \quad
 \mathcal C_{\rm Haar}=p\mathcal C,\quad
 K=p^{-2}(1\otimes\rho_+(t_0))\mathcal C_{\rm Haar}.
 \tag{5}
$$
未扭曲的两组 $W_-(v)v_0$ 与 $W_+(v)v_0$ 在此 Haar 下互为 norm1 的对偶基。
(4)的正侧再经 $\rho_+(t_0)$ 运输，给(5)的扭曲 coevaluation；
不声称运输后的两组仍对普通未扭曲配对互为对偶。
后文不把有限坐标公式的 $p^{-1}$ 当成另一种几何配对的标量。

## 2. inverse Jacobi 确定的真实点方向

这里直接使用 R1054(61)--(63)的 inverse arch Jacobi 返回。
对实际 Gaussian
$$
 \Phi(x;T)=e^{-\pi Gx^2}
       \exp\!\left(\sqrt G\,xT-\frac{T^2}{8\pi}\right),
 \qquad G=51\sqrt3,
$$
逐项完成平方给
$$
 \begin{aligned}
 &\mathsf H_{\epsilon,\infty}(-q,-\xi)\Phi(x;T)\\
 &\quad=
 \exp\!\left[
 \frac{\sqrt Gq-i\epsilon\xi/\sqrt G}{2}T
 -\frac\pi2(Gq^2+\xi^2/G)\right]\,
 \Phi\!\left(x;\,
 T-2\pi\sqrt Gq-\frac{2\pi i\epsilon\xi}{\sqrt G}\right).
 \end{aligned}
 \tag{6}
$$
包括线性及中心 multiplier；不能只取最后的参数位移。
原实际 coherent 变量为
$z_-=\Omega_0h_HT/\delta$、$z_+=\Omega_0h_HT$，
其中 $h_H=\sqrt G/(204\pi i)$。
代入 $q=a/p,\xi=b/p$，并按原 CRT lift 保全部非 $p$ 稳定子，
得到底层 argument 的位移。再用 $z=pz'$，真正的覆盖上
$p^2$ 挠点为
$$
 \begin{aligned}
 \beta_-(a,b)&=
   \frac{\Omega_0}{2\delta p^2}\,(b/51+\delta a),\\
 \beta_+(a,b)&=
   -\frac{\Omega_0}{2p^2}\,(b/51-\delta a).
 \end{aligned}
 \tag{7}
$$
这里分母 $2,3,17$ 表示 $\mathcal O_K/p^2$ 中的实际单位逆；
复代表由(6)的 CRT lift 固定。不能随意换一个代表并删去
其 theta 中心相位。未再除 $p$ 的位移是 $[p]\beta_\pm$，
不是覆盖上的 $p^2$ 点。

在 $(a,b)$ 上 $M$ 把
$u=b/51+\delta a$ 变成 $t_0u$。因此真实点方向是
$$
 \beta_-(Mv)=[t_0]\beta_-(v),\qquad
 \beta_+(Mv)=[\bar t_0]\beta_+(v).
 \tag{8}
$$
这由原 inverse Jacobi 式得出；正负方向不能改成相反标签。
定义
$$
 \gamma_{102,p}=\beta_+M\beta_-^{-1}
       :E_0[p^2]\longrightarrow E_0[p^2].
$$
先将负点沿实际 $\delta$ 送回 degree34 层，得到
$$
 \boxed{
 \gamma_{34,p}=\gamma_{102,p}[\delta]^{-1}
       =-\bar t_0\,c=\omega\,c,\qquad
 \gamma_{102,p}=\delta\bar t_0\,c ,
 }
 \tag{9}
$$
$c$ 是原实模型的复共轭在有限挠点上的作用。
(9)首先是有限群 scheme 在含全部标记的有限扩域上的同构，
不是椭圆曲线上的反全纯代数自同态。
它满足真正的反 CM 关系
$$
 \gamma_{34,p}[\omega]=[\bar\omega]\gamma_{34,p}.
 \tag{10}
$$
对其它实际 finite/$h$ 字，应先按原 Egorov 运输其两条
theta 结构；(9)由该真实运输共轭，不能以新标记自由替代。
全局 rational $t_0$ 的非 $p$ 分量与 $p$ Heisenberg 群交换，
因此本方向核对不要求 tame 向量本身是 $t_0$ 的特征向量。

## 3. 原完整 p⁴ 图群与实际下降

先固定一个尚未作无穷环面平均的字。令
$$
 X=E_0\times E_0,\qquad
 \mathcal L=[p]^*\mathcal L_{102}
                \boxtimes[p]^*\mathcal L_{34}.
$$
用(7)及原 theta-group lifts 定义
$$
 \Gamma_p=
 \{(\beta_-(v),\,\beta_+(Mv)):v\in R^2\}
 =\operatorname{Graph}(\gamma_{102,p}).
 \tag{11}
$$
这是阶 $p^4$ 的有限 étale 群。
正负 Weyl 的中心 cocycle 相反，且 $\det M=1$，所以
$$
 \widetilde\Gamma_p(v)=
 W_-(v)\otimes W_+(Mv)
 \tag{12}
$$
在 $\mathcal L$ 上给真正的群作用：
$\widetilde\Gamma_p(v)\widetilde\Gamma_p(w)
 =\widetilde\Gamma_p(v+w)$。
这已经支付了 lift，强于只证明 commutator 为1。

于是商 $f_p:X\longrightarrow \mathscr B_p=X/\Gamma_p$，
$\deg f_p=p^4$，有唯一带所指定下降数据的 ample 线丛
$\mathcal M_p$，使 $f_p^*\mathcal M_p=\mathcal L$。
可以直接按有限 étale cover 的线丛粘合构造：
在 $f_p$ 分裂的开集上取一张 lift，由(12)识别其它 lift；
严格群律就是三重交上的 cocycle 条件。
此为 theta-group 下降的具体情形，参见 Mumford
《On the equations defining abelian varieties I》§1 Proposition1。

原 seed 是
$$
 s_0=[p]^*s_-\boxtimes[p]^*s_+.
$$
原球 $v_0$ 被 $pR^2$ 的全部 Weyl 固定，故 seed 被
$\widetilde\Gamma_p(pR^2)$ 固定。全 $p^4$ 群平均在它上面准确成为
$$
 \begin{aligned}
 \Pi_{\Gamma_p}s_0
 &=\frac1{p^4}\sum_{v\in R^2}\widetilde\Gamma_p(v)s_0\\
 &=\frac1{p^2}\sum_{v\in\mathbf F_p^2}
             \widetilde\Gamma_p(\widetilde v)s_0
 =K(s_-\otimes s_+).
 \end{aligned}
 \tag{13}
$$
每个 coset 有 $p^2$ 个元素；这正是(4)，没有把商次数误写成
$p^2$。由下降存在唯一 $\mathfrak s_p\in H^0(\mathscr B_p,\mathcal M_p)$，
$$
 \boxed{
 f_p^*\mathfrak s_p=\Pi_{\Gamma_p}s_0,\qquad
 \mathfrak s_p=p^{-4}\operatorname{Tr}_{f_p}(s_0).
 }
 \tag{14}
$$
后式的 trace 使用(12)的实际线丛识别。

若当前两条尚未投影的 seed section 都非零，则(14)非零。
确切地，$p$-primary Heisenberg 在
$H^0(E_0,[p]^*\mathcal L_N)$ 上为标准 $p^2$ 维不可约模
与一个 $N$ 维 multiplicity 空间的张量；
$E[p]$-不变部分是其 old 直线与该 multiplicity 空间。
两条 seed 对应 $v_0\otimes a_-$、$v_0\otimes a_+$，
其中 $a_\pm\ne0$；(13)变成 $K\otimes a_-\otimes a_+$，
而(3)的 $K\ne0$。这一论证也可由完整 Weyl-old 基线性独立直接得到。
它没有把后续 toric/Artin 投影后的 section 或临界标量赋为非零。

## 4. 固定三同源后得到的主极化商

令
$$
 j=([\delta],1):X\longrightarrow X_0=E_0\times E_0,
 \qquad \deg j=3 .
$$
原刚性化给
$\mathcal L=j^*(\mathcal L_{34}^{\,p^2}
                       \boxtimes\mathcal L_{34}^{\,p^2})$。
因为 $p\ne3$，$j$ 在 $\Gamma_p$ 上单射，并送它到
$$
 \widetilde\Gamma_p=\operatorname{Graph}(\gamma_{34,p})
      \subset X_0[p^2].
 \tag{15}
$$
复共轭反转 Weil pairing，而 $\omega$ 的范数为1。
所以(9)是对 product principal polarization 的 anti-isometry。
等价地，在102层
$e_{p^2}(\gamma_{102,p}T,\gamma_{102,p}T')
 =e_{p^2}(T,T')^{-3}$，
正好抵消 $102=3\cdot34$ 的两个 line-bundle commutator。

设 $n=p^2$，$L_0=\mathcal O(O)\boxtimes\mathcal O(O)$。
图(15)在 $L_0^n$ 上有 level lift，商
$$
 q_p:X_0\longrightarrow C_p=X_0/\widetilde\Gamma_p
$$
带 principal polarization $\Theta_p$，满足
$q_p^*\Theta_p=L_0^n$。这里可保实际34次刚性化：
原(12)经 $j$ 返回的 lift 已作用在 $(L_0^n)^{34}$；
由于 $\gcd(34,p)=1$，其在 theta group 中有唯一 compatible
34次根 level lift。具体地，取两个阶 $p^2$ 生成元，先任取其34次根 lift。
每个 lift 的 $p^2$ 次幂在 $\mu_{34}$ 中；因 raising $p^2$
在 $\mu_{34}$ 上可逆，唯一调整使其阶整除 $p^2$。
两 lift 的 commutator 同时在 $\mu_{34}$ 与 $\mu_{p^2}$ 中，故为1。
这给真实 level subgroup；可能差异是
$\operatorname{Hom}(\widetilde\Gamma_p,\mu_{34})=0$。
因此不引入一个自由 Picard twist。

有交换图
$$
 \begin{array}{ccc}
 X&\xrightarrow{j}&X_0\\
 \downarrow f_p&&\downarrow q_p\\
 \mathscr B_p&\xrightarrow{j_p}&C_p ,
 \end{array}
 \qquad \deg j_p=3,\qquad
 \mathcal M_p=j_p^*\Theta_p^{\,34}.
 \tag{16}
$$
$h^0(\Theta_p)=1$，
$j_p^*\Theta_p$ 的 Euler characteristic 是3，极化类型为$(1,3)$；
从而
$$
 \boxed{\operatorname{type}(\mathcal M_p)=(34,102),
 \qquad h^0(\mathscr B_p,\mathcal M_p)=34\cdot102=3468.}
 \tag{17}
$$
直接核次数也得
$\chi(\mathcal L)=102\cdot34\cdot p^4$，
除以真正的 $\deg f_p=p^4$，准确回(17)。

## 5. 对复合 n=p² 的不分裂证明

本节不借只适用于 prime degree 的不可约粘合判据。
在特征零代数闭包上，假定 $(C_p,\Theta_p)$ 为两个椭圆曲线的
product principal polarization。令 $P$ 为其中第一因子的正交投影，
$q=q_p$，$\dagger$ 为 product/principal 极化的伴随。由
$q^*\Theta_p=nL_0$ 得
$$
 q^\dagger q=[n],\qquad qq^\dagger=[n].
$$
于是
$$
 M=q^\dagger Pq\in\operatorname{End}(E_0^2),\qquad
 M^\dagger=M,\quad M^2=nM,
 \quad \operatorname{rank}M=1 .
 \tag{18}
$$
$\operatorname{End}(E_0)=\mathcal O_K$；在 product 坐标写
$$
 M=\begin{pmatrix}k&c\\\bar c&n-k\end{pmatrix},
 \qquad k\in\mathbf Z,\quad c\in\mathcal O_K,\quad
 N(c)=k(n-k).
 \tag{19}
$$
这里 trace $n$ 来自(18)的特征值 $0,n$，而不是另设数值条件。

须证明端点不能出现。若 $k=0$，令
$h=\operatorname{pr}_1q:E_0^2\to E_1$。其第一限制 degree0，
所以 $h(P,Q)=h_2(Q)$；第二限制的 degree 为 $n$。
但 $\ker q$ 包含全部 $(T,\gamma_{34,p}T)$，从而 $h_2$ 杀掉
整个 $E_0[n]$，其阶 $n^2>n$，矛盾。
$k=n$ 同理。因此
$$
                         0<k<n. \tag{20}
$$

由 $M\widetilde\Gamma_p=0$，第一行给
$c\gamma_{34,p}=-[k]$ 于 $E_0[n]$。
$c$ 是 CM 线性，而(10)为反 CM。分别把该式与 $[\omega]$
复合，得到
$$
 [k](\omega-\bar\omega)=0\quad\text{于 }E_0[n].
 \tag{21}
$$
$\omega-\bar\omega=\delta$ 在 $E_0[n]$ 上可逆，因为 $p\ne3$；
故 $n\mid k$，与(20)矛盾。

所以 principal polarization 不分裂。其 theta divisor 是一条
光滑 genus2 曲线，且 $C_p$ 为该曲线的 Jacobian。
这一最后标准事实也可见 Kani《Curves of genus two》§1
Remark1.3/Example1.4；其适用条件是特征零 principal abelian surface，
不是仅有一份纯 Hodge 同型。本节(18)--(21)给本题整个
$n=p^2$ 的自含不分裂证明。

## 6. 明确周期格及固定 source 基变

(9)为真实复坐标中的 $\omega c$。为写最简周期矩阵，
取实际格生成元 $\lambda_*=\Omega_0/\delta$，先用
$T=\lambda_*z$ 归一两条曲线。因为
$\bar\lambda_*=-\lambda_*$，此时(9)在
$\mathcal O_K$ 上是 $-\omega c$。
再对**正 factor**作实际 $[-1]$，就化为
$$
 \gamma^{\rm sw}(a+b\omega)=b+a\omega .
 \tag{22}
$$
这一固定同构也作用在全部 theta section、level 和 Miller 上。
它只是把 quotient 写成一个方便的坐标模型；原公式(13)--(16)
始终使用未改的实际标记。若使用 $\varpi_0$ 作格生成元，
对应矩阵为 $\left(\begin{smallmatrix}1&0\\1&-1\end{smallmatrix}\right)$，
与(22)按上述固定单位变换相容，不能直接略去这个差别。

在(22)模型中，商格为
$\mathcal O_K^2+n^{-1}\{(\lambda,\gamma^{\rm sw}\lambda)\}$。
取
$$
 u=\frac{(1,\omega)}n,\quad
 v=\frac{(\omega,1)}n,\qquad
 f_1=(\omega,0),\quad f_2=(0,\omega).
 \tag{23}
$$
它们生成整个格：$(1,0)=nu-f_2$、$(0,1)=nv-f_1$。
对 $n$ 倍 product Riemann form，
$E(u,f_1)=E(v,f_2)=1$，其余交叉配对为0；
所以 $(u,v;f_1,f_2)$ 是 principal symplectic 基。
由其 $A,B$ 周期矩阵直接得
$$
 \boxed{
 \tau_{C_p}=-\frac n\delta
      \begin{pmatrix}1&-\omega\\-\omega&1\end{pmatrix}.
 }
 \tag{24}
$$
其虚部为
$n/\sqrt3\cdot
\left(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\right)$，
正定。这里保(22)的 source pullback；没有拿同一个 theta
表达直接套到未运输的周期矩阵上。
$C_p$ 随 $p$ 变化，(24)不把它变成主目标所需的一条固定有理曲线。

## 7. 全部 Miller 函数及原 p 幂

下面在实际 $E_0$ 的原刚性化上计算，与§6的方便坐标无关。
对 $T\in E_0[p^2]$，取由实际 theta lift 指定的 lift $t$，
置 $Q=pT$、$q=pt$、$\lambda=pq\in\Lambda$，
$$
 \eta_Q=\eta(\lambda)/p,\qquad
 \eta_T=\eta(\lambda)/p^2=\eta_Q/p .
$$
定义
$$
 \mathcal H_{Q,p}(z)=
 e^{-p\eta_Qz-\eta_Qq/2}
 \frac{\sigma(pz+q)}{\sigma(z)^{p^2}} .
 \tag{25}
$$
这是椭圆函数。确切地，$z\mapsto z+\ell$ 的剩余 multiplier 是
$\exp\{p(\eta(\ell)q-\eta_Q\ell)\}=1$，
由 $pq\in\Lambda$ 及 Legendre 关系得出；
奇数 $p$ 的 sigma half-character 也相消。
其完整除子为
$$
 \operatorname{div}\mathcal H_{Q,p}
       =[p]^{-1}(-Q)-p^2(O).
 \tag{26}
$$
当 $Q=O$ 且原 lift 为0时，
$$
 \mathcal H_{O,p}=r_p
 =\frac{\sigma(pz)}{\sigma(z)^{p^2}},
 \qquad r_p\sim pz^{1-p^2};
 \tag{27}
$$
这是同一原 division function，不将其首 $p$ 除掉。

若 $s_N=\sigma^NR_N$ 是当前真正 section，则 symmetric
theta lift 在 $[p]^*\mathcal L_N$ 上准确给
$$
 \boxed{
 \mathsf W_T([p]^*s_N)(z)
   =\sigma(z)^{Np^2}\,
       \mathcal H_{Q,p}(z)^N\,R_N(pz+q).
 }
 \tag{28}
$$
其左侧的 multiplier 是
$e^{-Np^2\eta_T(z+t/2)}$；代入 $\eta_T=\eta_Q/p$
即证明(28)。对原(6)指定的任何其它 lift，其实际中心分量
在两边同时乘上，不能删除。R1054(59)的共同 lift 给两侧
相反中心相位，整个(13)保持不变。
当 $T\in E[p]$ 时，$pt$ 为周期；$N=34,102$ 均为偶数，
所以准周期和 multiplier 严格相消，这也直接证明§3使用的
整个 old 稳定子。

$z$ 在(25)--(28)是覆盖参数，物理原参数是 $z_{\rm phys}=pz$。
因此返回原 $(r,s)$ coherent 系数时，覆盖系数要乘
$p^{-r-s}$。它和(13)的群平均及(5)的 Haar 系数是三个不同费用，
不相互重复或抵消。R1060 中的整个 PD/完成函数运输可用此
精确变量式，不得把新 degree-$Np^2$ 的标准 completion 免费认成
原 completion 的拉回。

## 8. 常数的代数性与准确 p 进估值

对 $Q\ne O$，(25)的首项为
$c_Qz^{-p^2}$，其中
$$
 c_Q=e^{-\eta_Qq/2}\sigma(q).
$$
记 $\epsilon_\Lambda(\lambda)\in\{\pm1\}$ 为原 sigma
half-character。对 $\sigma(pz)=r_p(z)\sigma(z)^{p^2}$
在 $z=q$ 取首导数，用 $pq=\lambda$ 的准周期，得到
$$
 \boxed{
 c_Q^{\,p^2}
 =\epsilon_\Lambda(pq)\,\frac p{(D r_p)(Q)},
 \qquad D=d/dz.
 }
 \tag{29}
$$
因为 $Q$ 是特征零 simple division point，右侧非零且代数。
所以 $c_Q$ 与 $\mathcal H_{Q,p}$ 的原刚性化均在一个明确有限代数扩域
内；选择的根仍由原 theta lift 决定。
若两个函数同(26)且首项相同，它们的比为常数1，
因此(25)也给完整代数 Miller 函数，而不只是解析式或除子类。

其 $p$ 进估值必须经**整线丛与形式参数**计算。
不把 sigma 的原点级数直接代到边界挠点。
取 good integral 模型的形式参数 $t=-x/y$。
全非零 $E[p]$ 在 supersingular 情形均在形式群中，
$$
 v_p(t_Q)=\frac1{p^2-1}.
$$
整 division function 的实际比较为
$$
 r_p(t)=u(t)\frac{[p](t)}{t^{p^2}},
 \qquad u(t)\in\mathcal O[[t]]^\times,\quad u(0)=1.
 \tag{30}
$$
可由 Weierstrass preparation 完整证明：
$t^{p^2-1}r_p$ 和 $[p](t)/t$ 都是常数项 $p$ 的整级数，
其 formal-disc 零点恰是全部 $p^2-1$ 个非零 $p$ 挠点。
前者不可能所有系数被 $p$ 整除，否则除 $p$ 后常数1的整幂级数
没有这些零点。二者因此有同一个 monic Weierstrass polynomial，
商为(30)的整单位。
高度2的 $[p]$ Newton polygon给上方的 $t_Q$ 估值。

不变导数满足 $D([p](t))(Q)=p$ 乘整单位；
在(30)取导数时含 $[p](t_Q)$ 的其它项全消掉。因此
$$
 v_p((D r_p)(Q))
 =1-\frac{p^2}{p^2-1}
 =-\frac1{p^2-1}.
$$
与(29)合并，准确得到
$$
 \boxed{v_p(c_Q)=\frac1{p^2-1}\qquad(Q\ne O).}
 \tag{31}
$$
这不是一个可略去的单位。$Q=O$ 则保(27)的首 $p$，
不以(31)代替。两类覆盖字及其全和因此均有原规范；
这里尚不由单个 $c_Q$ 的估值推整个临界读者的非零或范数。

## 9. δ 与两条三挠词的完整相容

原精确三同源函数为
$$
 r_\delta(z)=\frac{\sigma(\delta z)}{\sigma(z)^3}
             =\delta x(z),\qquad
 \eta_{\delta Q}\delta=3\eta_Q .
$$
代入(25)逐项得到
$$
 \boxed{
 r_\delta(z)^{p^2}
   \mathcal H_{\delta Q,p}(\delta z)
 =\mathcal H_{Q,p}(z)^3 r_\delta(pz+q).
 }
 \tag{32}
$$
除子、指数和常数都在式中；它不是只在 Picard 群的关系。
对 $Q\ne O$，亦有
$c_{\delta Q}=\delta x(Q)c_Q^3$，
与(31)及 $v_p(x(Q))=-2/(p^2-1)$ 一致。
原两条 $\mathsf T_{\pm q_3}^{34}$ 应分别施用(28)、(32)，
再按(2)相加。这准确实现
$\tau_T^*[\delta]^*=[\delta]^*\tau_{\delta T}^*$；
不能把负侧 $T$ 直接作为34层的同一个点。

再核它们在(16)三盖中的角色。
$\tau_{\pm q_3}^*\mathcal L_{34}\otimes\mathcal L_{34}^{-1}$
是两条非平凡 order3 flat line，因为 $34q_3=q_3\ne O$。
它们被 $[\delta]^*$ 杀掉，并给 $\ker[\delta]$ 的互逆非平凡
characters $\kappa,\kappa^{-1}$。其非平凡性也由
$\delta$-isogeny 的 perfect Cartier pairing 直接得到；
原 lift 中哪个是 $\kappa$，保持由(2)及 R1054(59)的实际 Weyl 词决定。

在 $[p]$ 覆盖上相应 characters 是
$\kappa^p,\kappa^{-p}$，因为 $\tau_U^*[p]^*
 =[p]^*\tau_{pU}^*$。原惰性 $p$ 交换这两条角色。
$\ker\delta$ 与 $\Gamma_p$ 的 orders 互素，theta commutator
同时为三次根和 $p$ 幂根，故为1；所以(13)保持两条角色。
由(16)，原下降 section 因而准确落在
$$
 H^0(C_p,\Theta_p^{34}\otimes\mathcal P_{\kappa^p})
 \ \oplus\
 H^0(C_p,\Theta_p^{34}\otimes\mathcal P_{\kappa^{-p}})
 \subset H^0(\mathscr B_p,\mathcal M_p),
 \tag{33}
$$
其中 $j_{p*}\mathcal O_{\mathscr B_p}
 =\mathcal O_{C_p}\oplus\mathcal P_\kappa\oplus
   \mathcal P_{\kappa^{-1}}$，角色记号按原下降约定固定。
因此它的**普通三盖 trace**到 untwisted $\Theta_p^{34}$ 为0。
这只说明不能把原两词合成 principal 商的一条无扭曲 theta
section；它不是原 Artin/Cor、完整环面积分或临界斜率为零。

## 10. 回到整个原来源与真正尚未支付的量

令 $\mathfrak T_{\rm orig}$ 为 R1054(65)的全部实际 theta 操作。
对每个尚未作 circle 积分的实际字，(13)、(28)、(32)给
$$
 W_p=\mathfrak T_{\rm orig}
       \bigl(f_p^*\mathfrak s_p\bigr),\qquad
 \text{原 bad 输入}=W_p-w_0 .
 \tag{34}
$$
这是一份具体整体同源/线丛来源，不能在(34)中删除原旧项。
只有 R1052 已证明的那一个**完整** unmodified toric flat 投影
才使旧项为零；单个字或另一读者不自动享有该结论。

无穷 $h$ 对两个 coherent 变量的连续旋转，可能将各字写在相应
旋转的周期格上。应先按(6)及原 Egorov 运输全部 arch Gaussian
和 lattice，再取整个积分。代数下降与(29)--(31)在原有限字
所指定的代数刚性化中进行；任意连续 $h_\infty$ 仍是相应解析
参数运输，不能为其临时选择一个新的 $p$ 进嵌入。R1060 已付的 whole 结果
$H(Z,W)=W^2F(ZW)$ 是相应形式/小盘恒等式；
一般并不是一个固定 $C_p$ 或 $\mathscr B_p$ 上的全球 theta section。
连续作用 $(Z,W)\mapsto(tZ,t^{-1}W)$ 也不是该固定 abelian
surface 的椭圆 endomorphism。因此§3的未投影非零和§5的 genus2
结构均不能直接给 whole 临界读者非零。

所有原冻结外权亦逐项保留。例如同一 maximal CM/tame 标记
$t$ 令 $\chi=t/\bar t$ 时，原账本是
$C_t=C_b$、$\Omega_t=\Omega_b/\bar t$、$\rho_t=\rho_b\chi$。
这里 $\Omega_b$ 是 R1060 的实际 $p$ 进基周期，与(1)的
复实周期 $\Omega_0$ 不是同一个记号。准确有
$$
 j_t(-2)\Omega_t^3\rho_t^\ell
       =\Omega_b^3\rho_b^\ell\chi^{\ell+2}.
 \tag{35}
$$
可以在 R1060 的完整有限转置中以
$H_t(Z,\chi W)$ 表达此真实重标；
一阶还保 $-\lambda\log\langle\chi\rangle P_2$ 及全部 Maass 槽。
(35)不把原外权换成另一份逐正权外权。

本篇支付的整体返回可供实际 finite-polynomial/PD
或原 Amice reader 直接消费；仍须以同一原来源证明其值或指定斜率
非零，以及它与 canonical 坏条件的真实关系。
没有增加 compact $p$ 平均，没有将有限 paired 字的非零提升成
所求通常全 Sha 结论，也没有重启数学执行。

### 依赖及原始文献

- [R1054](R1054-original-p-square-depleted-source-and-exact-conductor-blocks.md)
  §§5、8、10，尤其(52)--(65)：全部实际有限字、Haar、inverse Jacobi。
- [原 psi4 双槽来源](../notes/2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)
  §§5--7、10--11：原 $\Omega_0$、两条三挠 Weyl、$\delta$ 与实际幅度。
- [R1060](R1060-original-full-gaussian-transpose-and-critical-slope.md)：
  整个冻结外权、Gaussian、PD/临界转置；本文不重新定义其 reader。
- D. Mumford, *On the equations defining abelian varieties I*,
  Invent. Math. 1 (1966), 287--354，§1 Proposition1、Proposition3；
  [原文](https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf)。
- E. Kani, *The number of curves of genus two with elliptic differentials*，
  J. reine angew. Math. 485 (1997)，§1 Remark1.3/Example1.4；
  [原文页98](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0485/00000104?_format=xml)。
