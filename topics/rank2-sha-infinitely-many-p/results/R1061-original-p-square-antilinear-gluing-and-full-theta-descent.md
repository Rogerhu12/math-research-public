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


## 11. 实际 source 进入标准周期矩阵时的两项费用

以下继续使用§6的实际格、原正实 $\Omega_0$、
$\lambda_*=\Omega_0/\delta$ 及 $n=p^2$。
只对每个尚未作完整 circle 积分的实际 theta 字操作。
原 $h$、有限角色、三挠词及 Miller 均按原来源保留。

首先，§6为把物理 $\gamma=\omega c$ 改写成 swap，
对正 factor 作了实际 $[-1]$。在 R1054 的正有限模型中，
它是 $R_+f(B)=f(-B)$。因此进入该周期模型的矩阵准确为
$$
 K^{\rm sw}_{A,B}=K_{A,-B}
   =p^{-2}\zeta^{51(A^2+4AB+B^2)/2},
 \qquad
 K^{\rm sw}=\frac1p
       (1\otimes\rho_+(-t_0))\mathcal C,
 \qquad -t_0=\omega^2.
 \tag{B1}
$$
它同时将 $W_+(a,b)$ 改为 $W_+(-a,-b)$。
原 $v_0$ 固定，但各个已经平移的来源不因此逐字固定；
不能只用未平移 $S$ 为偶函数就省去(B1)。

还须保不同 symplectic 周期基之间的实际 source 矩阵。
记§6的矩阵为 $\tau_g$，另一份基若给
$\tau_r=\tau_g-nJ$，其中
$J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$，
则对完整 level-$N$ theta basis，定义
$$
 \Theta^{N}_{\mu;\alpha,\beta}(z;\tau)
 =\sum_{m\in\mathbf Z^2+\alpha+\mu/N}
   \exp\{\pi iN m^T\tau m+2\pi iN m^T(z+\beta)\},
 \quad \mu\in(\mathbf Z/N)^2 .
$$
这里的 characteristic 是原实际刚性化所规定的有理数，
不任意约化后删去相位。完整基变为
$$
 \boxed{
 \Theta^N_{\mu;\alpha,\beta}(z;\tau_g)
 =
 \exp\!\left[
 \pi i\left(\frac{\mu^T(nJ)\mu}{N}
                -N\alpha^T(nJ)\alpha\right)\right]
 \Theta^N_{\mu;\alpha,\beta+nJ\alpha}(z;\tau_r).
 }
 \tag{B2}
$$
证明只需写 $m=k+\alpha+\mu/N$。
$N k^T(nJ)k$ 是偶整数，且 $k^T(nJ)\mu$ 是整数；
其余两项恰给显示的 characteristic 和常数。
特别 $\alpha=0$ 时，相位为
$\exp(2\pi in\mu_1\mu_2/N)$。
若 $\mathfrak s=\sum_\mu c_\mu^{(g)}\Theta_\mu(\tau_g)$，
则按显示的 $\beta\mapsto\beta+nJ\alpha$ 后，
$c_\mu^{(r)}$ 等于(B2)的显示相位乘 $c_\mu^{(g)}$；
反向运输才取其逆。$N=34$ 的全部 $34^2$ 系数均须如此运输，
不是仅比较两个周期矩阵就可使用同一系数列。

## 12. 两条真正 conductor-p² 椭圆曲线及源变量

写
$$
 \tau_g=\begin{pmatrix}a&b\\b&a\end{pmatrix},\qquad
 \tau_+=a+b=\frac{n(1+\delta)}2,\qquad
 \tau_-=a-b=\frac{n(-1+\delta/3)}2.
 \tag{B3}
$$
两者均在上半平面。它们分别满足 primitive quadratic
equations
$x^2-nx+n^2=0$ 和 $3x^2+3nx+n^2=0$；
两 discriminants 都是 $-3n^2$，所以实际 CM 阶恰为
$\mathcal O_n$，不是原最大阶。

这也给原 cyclic-$p^2$ 点的具体格模型。
$\Lambda_+=\mathbf Z+\tau_+\mathbf Z
=\mathbf Z+n\omega\mathbf Z=\mathcal O_n$。
置 $s=\delta\omega=-(2+\omega)$，则
$s\Lambda_-=n\mathbf Z+s\mathbf Z$。
从源 $\mathbf C/\mathcal O_K$ 出发，两实际解析同源为
$$
 z\longmapsto nz\quad\hbox{到 }E_{\tau_+},
 \qquad
 z\longmapsto(n/s)z\quad\hbox{到 }E_{\tau_-},
 \tag{B4}
$$
其循环核分别是 $\langle1/n\rangle$、$\langle s/n\rangle$。
例如第二个目标拉回格为
$\mathbf Z+(s/n)\mathbf Z
 =\mathcal O_K+(s/n)\mathbf Z$，index 为 $n$。
还严格有 $3\tau_-=\tau_+-2n$。
因此 $\Lambda_+\subset\Lambda_-$、index 为3，恒等映射还给
$E_{\tau_+}\to E_{\tau_-}$ 的原标记 degree3 同源；
其核由 $\tau_-\bmod\Lambda_+$ 生成，拉回解析微分是恒等。
这里的解析微分倍率须与原整微分、AI 标记微分及 period
逐一比较；(B4)不把两份 Néron 微分或两个 $u_{C_1}$ 认成相同。

令
$R=\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)$。
真正的 degree4 同源为
$$
 f:E_{\tau_+}\times E_{\tau_-}\longrightarrow C_p,
 \qquad f(u,v)=R(u,v)^T .
 \tag{B5}
$$
其四个核点由
$(1/2,1/2)$ 与 $(\tau_+/2,\tau_-/2)$ 生成。
$R\mathbf Z^2$ 在 $\mathbf Z^2$ 的 index 为2，
同样的 index 出现在另一半周期格，故 degree 为4；
直接拉回 Riemann form 给
$f^*\Theta_p=\mathcal L_2\boxtimes\mathcal L_2$。
以下完整 theta 公式将保持这四个核点，而不是只取其 reduced
support 或略去一半的 isogeny。

这里还要支付实际 principal 根的二挠特征。
记 $\Theta_g$ 为 $\tau_g$ 的零 characteristic theta 线丛，
$\beta_0=(1/2,1/2)^T$，并令
$\mathcal P_g(T)=\tau_T^*\Theta_g\otimes\Theta_g^{-1}$。
原 $\mathcal O_{E_0}(O)$ 在 $(1,\omega)$ 两条纯基上的
Appell--Humbert half-character 均为 $-1$。
在§6的 $(u,v;f_1,f_2)$ 基中，$q_p^*\Theta_g$ 在
$nu-f_2,nv-f_1,f_1,f_2$ 四条原纯基上的 half-character 均为 $+1$，
而 $q_p^*\mathcal P_g(\beta_0)$ 在它们上面均为 $-1$。
由此，保原刚性化的实际根为
$
 \Theta_p=\Theta_g\otimes\mathcal P_g(\beta_0).
 \tag{B5a}
$
原 symmetric Weyl level 在 $[-1]$ 下稳定，故该下降根为对称线丛。
上述根与它的可能差同时属于 $\ker q_p^*$ 的奇数 $p$ 幂挠群
及二挠群，所以差为零。
$f^\dagger$ 的解析矩阵为 $R$，而
$R\beta_0=(1,0)^T$ 是 product 周期，故
$f^*\mathcal P_g(\beta_0)=\mathcal O$。
因此(B5)后的线丛等式确实保持原 $\Theta_p$，
不仅是 Riemann form 的数值相等。


为锁定原 coherent 变量，先仍在原 $\tau=\omega$ frame
并保全部已付 arch 运输。
原负侧回34层后的物理参数和正侧参数分别为
$q_-=\Omega_0h_\infty T_-$、$q_+=\Omega_0h_\infty T_+$。
原 $[p]$ 覆盖的点变量为 $P_1=q_-/p,P_2=q_+/p$；
不能把 argument $q_j$ 直接当成这个覆盖点。
使用§6的 $A$ 周期矩阵，
$$
 \binom uv
 =\frac1{2\lambda_*}R A^{-1}
       \binom{P_1}{-P_2}
 =
 \binom{\displaystyle
  \frac{p\delta h_\infty}{2(1+\omega)}(T_--T_+)}
 {\displaystyle
  \frac{p\delta h_\infty}{2(1-\omega)}(T_-+T_+)} .
 \tag{B6}
$$
负侧在这里已按原 $\delta$ 拉回返回34层，正侧负号正是(B1)。
再用原两参数 $T_-=-ibZ,\ T_+=-ibW$，
$h_\infty=\sqrt G/(204\pi i)$、
$b=2(\omega-1)/\sqrt G$，得到
$$
 \boxed{
 u=\frac{p}{68\pi}(Z-W),\qquad
 v=\frac{p\delta}{204\pi}(Z+W).
 }
 \tag{B7}
$$
其中 $\delta(1-\omega)=3(1+\omega)$ 固定了第一项的号。
这只是该实际 native arch frame 的明确变量矩阵。
R1060(8)的 $-6\delta$、$Z/\sqrt6,W/\sqrt6$，
以及(10)的实际 graded period，仍须随后按原字运输。
(B7)没有把复数 $\pi$ 或复 period 本身嵌入 $\mathbf C_p$。

## 13. 原全部 level34 系数到两条 level68 来源的精确反写

定义一维的同规范 basis
$$
 \theta^{L}_{j;\alpha,\beta}(u;\tau)
 =\sum_{r\in\mathbf Z+\alpha+j/L}
       \exp\{\pi iL\tau r^2+2\pi iLr(u+\beta)\}.
$$
对任意已固定的 rational characteristics，置
$\alpha_\pm=(\alpha_1\pm\alpha_2)/2$、
$\beta_\pm=(\beta_1\pm\beta_2)/2$。
直接换两个整数求和变量，得到
$$
 \boxed{
 \begin{split}
 &\Theta^N_{\mu;\alpha,\beta}(R(u,v)^T;\tau_g)\\
 &\quad=
 \sum_{\epsilon=0}^1
 \theta^{2N}_{\,\mu_1+\mu_2+N\epsilon;\alpha_+,\beta_+}
        (u;\tau_+)\,
 \theta^{2N}_{\,\mu_1-\mu_2+N\epsilon;\alpha_-,\beta_-}
        (v;\tau_-).
 \end{split}
 }
 \tag{B8}
$$
确切地，若 $m=k+\alpha+\mu/N$，则 $k_1+k_2$ 与
$k_1-k_2$ 同奇偶；分别写成 $2r+\epsilon,2s+\epsilon$。
二次型变成
$N\{\tau_+(m_1+m_2)^2+\tau_-(m_1-m_2)^2\}/2$，
线性项也同时返回(B8)。
因此没有额外的 $1/2$、$1/4$ 或可调 theta-null 常数。
两项是这个完整整数和的奇偶分解，不是少取了(B5)的四核平均。

这是一张显式、可逆返回到其 image 的固定系数矩阵。
在 $N=34$ 时，每个原 $\mu$ 产生两个 level68 index pairs
$$
 (\nu_+,\nu_-)
 =(\mu_1+\mu_2,\mu_1-\mu_2)
       +34\epsilon(1,1)\pmod {68}.
 \tag{B9}
$$
image 的系数在 $\nu_+\not\equiv\nu_-\pmod2$ 时为0，
在同时加 $(34,34)$ 时不变；
其余 pair 的原列由
$\mu_1=(\nu_++\nu_-)/2\bmod34$、
$\mu_2=(\nu_+-\nu_-)/2\bmod34$ 唯一返回。
故全部 $34^2$ 列被原样保存。
characteristic 非零时，四核的 theta-group lift 也按(B8)
运输；不能另用 untwisted lift 删除其相位。

这里的系数不是新增自由参数。
对§3、§9已经构造的实际下降 section，先使用(B1)、
原 Miller 和(B2)进入其确定的 theta frame，再写
$$
 \mathfrak s_{\sigma,h}(z)
    =\sum_{\mu\bmod34}
        c_{\mu,\sigma,h}\,
        \Theta^{34}_{\mu;\alpha_\sigma,\beta_\sigma}(z;\tau_g).
 \tag{B10}
$$
这唯一规定全部 $c_{\mu,\sigma,h}$。
(B5a)的二挠换框也在这份实际系数列中：
若三挠 characteristic 为 $(\alpha_\sigma,\beta_\sigma)$，
从 $\beta_\sigma+\beta_0$ 返回(B10)的 $\beta_\sigma$ 时，
每列的准确对角因子为
$
 \exp\!\left(2\pi i\,34
       (\alpha_\sigma+\mu/34)^T\beta_0\right)
 =(-1)^{\mu_1+\mu_2}\omega^{-17\sigma p}
 =(-1)^{\mu_1+\mu_2}\omega^{-\sigma}.
 \tag{B10a}
$
最后两式使用下节(B12)以及 $p\equiv2\pmod3$。
没有把实际 principal 根免费认成零 characteristic；
这个号与原 Miller/Gaussian 一起进入 $c_{\mu,\sigma,h}$。
若要逐个提取，可令
$t_\mu=\alpha_\sigma+\mu/34$，取原 section 的
$\exp(2\pi i(34\alpha_\sigma+\mu)^Tz)$ Fourier 系数，
再乘
$\exp(-34\pi i t_\mu^T\tau_gt_\mu
          -68\pi i t_\mu^T\beta_\sigma)$。
这是同一实际 theta 来源的系数提取，不是拟合另一份来源。
(B8)--(B9)于是给它的全部 level68 系数及逆返回。

## 14. 两个原三挠词的实际 characteristic

本段固定平移约定：
$\mathcal P_D(T)=\tau_T^*\Theta_D\otimes\Theta_D^{-1}$，
始终用同一个 $\tau_T(P)=P+T$。
原 $S_3=-\Omega_0/3$；
由于 $34S_3=S_3$，$[p]$ 拉回后的负侧正号三挠词在
$X_0$ 上的 flat line 正是
$\mathcal P_{X_0}((pS_3,0))$。
$ q_p^\dagger q_p=[n]$，而 $n\equiv1\bmod3$，
所以在 $C_p$ 上的点准确为
$$
 t_+=q_p(pS_3,0),\qquad t_-=-t_+.
 \tag{B11}
$$
这支付§9的两条 $\kappa^{\pm p}$；
若用 Cartier-dual character 的另一记号，仍以原
$\mathsf T_{+S_3}$、$\mathsf T_{-S_3}$ 锁定这两列，不猜交换号。

在(B1)后的标准格中，
$(S_3/\lambda_*,0)=(-\delta/3,0)$。
用§6的 $u,v;f_1,f_2$ 基，严格有
$$
 (-\delta/3,0)=-(n/3)u-(2/3)f_1+(1/3)f_2.
$$
因此(B11)的两个实际 characteristic 可保持为以下有理 lift：
$$
 \boxed{
 \alpha_\sigma=\sigma p(-2/3,1/3)^T,\qquad
 \beta_\sigma=\sigma p(-n/3,0)^T,\qquad
 t_\sigma=\tau_g\alpha_\sigma+\beta_\sigma,\quad
 \sigma=\pm1 .
 }
 \tag{B12}
$$
不先把这些分数改为模1代表后丢掉其 Weyl phase。
因 $34\equiv1\bmod3$，这个 point 也可直接用于
$\Theta_p^{34}$ 的平移：其 flat twist 正是所需的一条。
所用 characteristic basis 与字面平移之间的完整关系是
$$
 \Theta^N_{\mu;\alpha,\beta}(z;\tau)
 =
 e^{\,\pi iN\alpha^T\tau\alpha+2\pi iN\alpha^T(z+\beta)}
       \Theta^N_{\mu;0,0}(z+\tau\alpha+\beta;\tau).
 \tag{B13}
$$
这给转换 Gaussian 的确切式。
原§7--§9的实际 sigma/Miller lift 仍须通过(B13)转换，
不能因识别了 flat line 就省略其幅度或中心。

代入(B8)，两 elliptic factors 的 characteristic 准确为
$$
 \alpha_{\sigma,+}=-\sigma p/6,\qquad
 \alpha_{\sigma,-}=-\sigma p/2,\qquad
 \beta_{\sigma,+}=\beta_{\sigma,-}=-\sigma pn/6.
 \tag{B14}
$$
它们是原两个三挠词在这个 degree4 同源下的完整返回；
出现的 half-characteristic 是四核 lift 的组成部分，
不是额外选择 dyadic 本征线。
全部 $2\cdot34^2$ 个实际 twisted 系数均保。
ordinary $\delta$-trace 为0仍只是§9的角色结论，
不能把(B10)--(B14)或其完整 $h$/Artin 加权和设为0。

原 bad 输入中的 $-w_0$ 继续按 R1054/R1059 的实际来源保留。
它没有仅凭本节被认成 $C_p$ 上的第三个 untwisted section；
原整球 tensor 本身也不能被擅自当成已经做过
$\widetilde\Gamma_p$ 平均。

## 15. 全 h 投影、冻结权与真正局部 mixed-heat 读者

在任何(B8)的应用中，先保该实际 $h$ 字的全部系数、
characteristics、变量与刚性化，然后才取原积分。
令 $U=Z-W,V=Z+W$。
源圆周的真实作用 $(Z,W)\mapsto(h^{-1}Z,hW)$ 变为
$$
 \binom{U_h}{V_h}
 =
 \begin{pmatrix}
 (h+h^{-1})/2&(h^{-1}-h)/2\\
 (h^{-1}-h)/2&(h+h^{-1})/2
 \end{pmatrix}
 \binom UV .
 \tag{B15}
$$
它保持 $V^2-U^2=4ZW$。
这解释了原 cross Gaussian 可以保在整个积分外，
但一般 $h$ 会混合两条 elliptic theta 变量；
(B15)不是固定 $E_{\tau_+}\times E_{\tau_-}$ 的全局
endomorphism。任意连续 $h$ 也不获得新的 $p$-adic embedding。
只有整个既定积分的系数在原 period 比较后使用
$\overline{\mathbf Q}\hookrightarrow\mathbf C_p$。

冻结标记的 $W\mapsto\chi W$ 则给
$$
 \binom{U'}{V'}
 =
 \frac12\begin{pmatrix}1+\chi&1-\chi\\1-\chi&1+\chi\end{pmatrix}
 \binom UV,\qquad
 V'^2-U'^2=\chi(V^2-U^2).
 \tag{B16}
$$
这与 R1060 的 $\beta_t\chi=\beta_0$ 完全相符。
$\lambda'$、$-\lambda\log\langle\chi\rangle P_2$、
实际 $\Omega,\kappa$ 和全部 lower-Maass 槽都继续保留。
在已经完成的 whole PD 模型中，
$U=Z-W,V=Z+W$ 及其逆的系数在 $\mathbf Z_p$，det 为单位；
故该线性变换是相应 bounded PD 代数的等距自同构。
这不为两个单独 theta factors 另立范数。

还可以给原有限 reader 一张显式矩阵。
若 $P(U,V)=H((V+U)/2,(V-U)/2)$，则
$$
 [Z^nW^{n+2}]H
 =
 \sum_{a=0}^{2n+2} d_{n,a}
      [U^aV^{2n+2-a}]P,\qquad
 d_{n,a}=
 \sum_j(-1)^{a-j}\binom aj
                  \binom{2n+2-a}{n-j}.
 \tag{B17}
$$
越界 binomial 取0。所有 $d_{n,a}$ 是明确整数；
因此可将(B8)的**全部**两点 theta 系数送进
R1060(15)、(19)--(25)的同一有限读者。
(B17)不是只保其中两个特征方向，也没有换入新的正权外权。

最后，把原一变量算子
$L=x\partial_x^2+3\partial_x$ 落实到当前同一个双核。
对 $\iota(F)=W^2F(ZW)$，
$$
 \boxed{
 \partial_Z\partial_W\,\iota(F)=\iota(LF),
 \qquad
 \partial_Z\partial_W=\partial_V^2-\partial_U^2.
 }
 \tag{B18}
$$
所以在原 unit chart 上，临界值测试和斜率测试分别是
$$
 \iota(x^{-2})=Z^{-2}=\frac4{(U+V)^2},\qquad
 \iota(x^{-2}\log x)
 =\frac4{(U+V)^2}\log\!\left(\frac{V^2-U^2}{4}\right).
 \tag{B19}
$$
这里取 $Z,W\ne0$ 且 $x=ZW$ 属于原固定 Teich 分量的
unit chart；对数是原 $\log\langle x\rangle$ 分支。
这只用来运输原测试函数，尚不把 $x$ 宣称为两条椭圆曲线上的
全局函数。直接微分给 $Lx^{-2}=0$，并对 $r\ge1$ 给
$$
 \frac1{r!}L^r(x^{-2}\log x)
   =-(r+1)(r-1)!\,x^{-2-r}.
 \tag{B20}
$$
故同一个 $e^{CL}$ 正确返回 R1056 的完整
$\log-E(C/x)$ 斜率核。
这没有声称 $L$ 在整个 $C(\mathbf Z_p)$ 上有界。

在(B7)的 native frame，令 $a_p=p/(68\pi)$，
则 mixed operator 在两 elliptic 变量中为
$$
 \partial_Z\partial_W
 =-a_p^2\left(\partial_u^2+\frac13\partial_v^2\right).
 \tag{B21}
$$
对(B8)的 level68 theta **basis**，
直接微分其定义得到
$\partial_u^2\theta^{68}=4\pi i\cdot68\,\partial_{\tau_+}
\theta^{68}$，另一条同理。
所以在保持该实际 theta 坐标列与 characteristic 固定时，
(B21)等于
$$
 -\frac{i p^2}{17\pi}
       \left(\partial_{\tau_+}+\frac13\partial_{\tau_-}\right).
 \tag{B22}
$$
这是两条确切 conductor-$p^2$ 曲线上的 heat 方向。
而且它沿 $t\mapsto(\tau_++t,\tau_-+t/3)$，
保持 $3\tau_--\tau_+=-2n$，正切于上述真实 degree3 同源族。
它不自动等于原来源随 moduli 变化的全导数：
若实际 Miller/Gaussian frame 为 $J$，原普通导数作用于
$J\mathfrak s$ 时必须保
$(\partial_Z+\partial_Z\log J)
 (\partial_W+\partial_W\log J)$ 的全部项；
真实 source 系数若随 moduli 运输，其连接项也仍在。
R1060的 proper $-6\delta/\sqrt6$ 与 graded period
同样按其原式运输，不以(B22)删掉。

因此本节确将原 coevaluation 的全部系数送到了两条明确
conductor-$p^2$ theta 来源，并给临界有限转置的具体
mixed-heat 形式。尚未把它识别为一个已规范的全球 Green 函数，
也未由 theta-null、genus2 不分裂或某个单字非零推出
canonical $J'(0)$ 非零。真正后继仍须在(B10)、(B15)--(B22)
的整个原来源、全部权和原坏条件之间建立同一读者的关系。


## 16. 原 division field 内的完整 translated jet

本节接§§7--9，并使用 C 标签以免与前面的 B 标签混淆。
所有式子均为同一原 theta 来源的特征零恒等式；
先给全阶 jet，再付其真实 $p$ 进费用。
没有将某个单独 translated section 预先赋为 canonical 零。

仍写 $r_p=\sigma(pz)/\sigma(z)^{p^2}$、$D=d/dz$。
对非零 $Q\in E_0[p]$ 取§7指定的 lift $q$，令
$$
 Z_Q=\zeta(q)-\eta_Q .
$$
这个差有不含未定 quasi-period 的精确代数表达：
$$
 \boxed{
 Z_Q=-\frac{D^2r_p(Q)}{2p^2Dr_p(Q)}.
 }
 \tag{C1}
$$
证明如下。把 $z=q+\varepsilon$ 代入
$\sigma(pz)=r_p(z)\sigma(z)^{p^2}$。
左边在 $\varepsilon=0$ 为 simple zero；由
$pq\in\Lambda$ 的原准周期，其二阶/一阶导数比是
$2p\eta(pq)$。右边相同比为
$D^2r_p(Q)/Dr_p(Q)+2p^2\zeta(q)$。
用 $\eta_Q=\eta(pq)/p$ 即得(C1)。
这在当前有限扩域内直接确定 $Z_Q$，
没有在 $p$ 挠点代入原点的 sigma 或 zeta 级数。

设当前真正代数 section 为
$s_N(z)=\sigma(z)^N R_N(x(z),y(z))$。
$N=102$ 时 $R_N$ 是原(2)的两条三挠词完整相加后的
$R_{102}$，或已登记参考源的对应多项式；
$N=34$ 时是原 $S,H_3,H_5$ 的对应多项式。
实际 raw 幅度仍乘在这些 section 上。
引入一个**独立形式变量** $Z$，定义
$$
 \mathcal D=
 2y\frac{\partial}{\partial x}
 +3x^2\frac{\partial}{\partial y}
 -x\frac{\partial}{\partial Z},
 \qquad
 A_{N,0}=R_N,\qquad
 A_{N,m+1}=(\mathcal D+NZ)A_{N,m}.
 \tag{C2}
$$
此导子保持 $y^2=x^3+1$。例如
$$
 \begin{aligned}
 A_{N,1}&=DR_N+NZR_N,\\
 A_{N,2}&=D^2R_N+2NZDR_N+(N^2Z^2-Nx)R_N .
 \end{aligned}
 \tag{C3}
$$
必须先在这个多项式/有理函数环中作(C2)，然后代
$(x(Q),y(Q),Z_Q)$。
不能先把 $Z$ 换成(C1)的有理函数再作 $D$；
也不能在 $E[p]$ 的 reduced 坐标代数内擅自定义这个 $D$。
沿当前平移的 local germ，$\eta_Q$ 是固定常数，
所以真正的关系是 $D(\zeta-\eta_Q)=-x$；
这正是(C2)的最后一项。

令 $T\in E[p^2]$ 满足 $pT=Q$，
并使用原(12)/(R1054(59))指定的 theta lift。
记 $b_{N,\widetilde Q}$ 为该实际 lift 在(28)中的常数，
也就是其中心分量乘 $c_Q^N$。
这个记号不重新选择 $N$ 次根；它保留原 finite Weyl 的中心。
对相同原 sigma 刚性化的 symmetric lift，恰有
$b_{N,\widetilde Q}=c_Q^N$。
其它原 lift 相差一个 $\mu_{p^2}$ 分量，已由(59)确定。
因为 $N=34,102$ 均为偶数，(29)进一步给
$$
 b_{N,\widetilde Q}^{\,p^2}
       =\left(\frac p{Dr_p(Q)}\right)^N,
 \qquad
 v_p(b_{N,\widetilde Q})=\frac N{p^2-1}.
 \tag{C4}
$$

从(28)或直接对
$e^{-N\eta_Q(pz'+q/2)}s_N(pz'+q)$ 求导，得到所有 $m\ge0$ 的
完整覆盖 jet：
$$
 \boxed{
 D_{z'}^m\bigl(\mathsf W_T[p]^*s_N\bigr)(0)
   =p^m b_{N,\widetilde Q}
        A_{N,m}(x(Q),y(Q),Z_Q).
 }
 \tag{C5}
$$
这里的 $p^m$ 是实际 $z=pz'$。
原 Gaussian/Weyl multiplier 的所有高阶费用恰在
$NZ$ 和 $DZ=-x$ 中；(C5)不是只保最高导数项的近似。
若改回物理参数 $z$，右侧只去掉这一个 $p^m$。
Taylor 系数还须除 $m!$，不可与导数混同。

## 17. Z_Q 的准确整费用

写
$$
 \Delta_p=p^2-1,\quad d=p+1,\quad
 c_\sigma=[z^d]\log(\sigma(z)/z),\quad
 \kappa_\sigma=pc_\sigma\in\mathcal O^\times .
$$
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)
(5)、(6)、(10)--(13)使用完全相同的 $E_0,\sigma,D$，已付
$$
 \kappa_\sigma\bmod p
  =-(-1)^{(p+1)/6}4^{-(p+1)/6}
       \binom{(p+1)/3}{(p+1)/6}\ne0.
 \tag{C6}
$$
它不是本篇重新取的一份单位。
本节用原 good formal 参数
$w=x^{-1/2}=z+\cdots$，即 R301(6)的参数；
它与§8的 $-x/y$ 整可逆。
准确有
$$
 Dw=\sqrt{1+w^6},\qquad
 L(w)=z
 =\sum_{j\ge0}
 \frac{(-1)^j\binom{2j}{j}}{4^j(6j+1)}w^{6j+1}.
 \tag{C7}
$$

先证明一个全整性事实。
把(30)在 $w$ 参数中写成
$$
 r_p(w)=U(w)\frac{[p](w)}{w^{p^2}},
       \qquad U(w)\in\mathcal O[[w]]^\times,\quad U(0)=1 .
 \tag{C8}
$$
$j=0$ 惰性约化有 $\operatorname{Fr}_p^2=[-p]$：
因为 $p\equiv2\pmod3$，$x\mapsto x^3$ 置换 $\mathbf F_p$，
原曲线的点数角色和为0，故 $a_p=0$，Frobenius 满足这个二次式。
所以
$[p](w)\equiv-w^{p^2}\pmod p$。
$r_p$ 的约化是非零常数：
它不能为零，因为§8的 Weierstrass 论证已经证明
$t^{p^2-1}r_p$ 有单位系数；若其非零约化有一个有限零点，
在该 smooth 点的严格 henselian formal-disc 中必提升出
$r_p$ 的零点，给一个不约化到 $O$ 的特征零 $p$ 挠点，
与 supersingular $E[p]$ 连通矛盾。
而 $r_p$ 仅在 $O$ 有极，故没有其它可能。
在(C8)约化并用 $U(0)=1$，于是准确有
$$
 r_p\bmod p=-1,\qquad U(w)\equiv1\pmod p.
 \tag{C9}
$$

还可锁住 $U-1$ 的第一份非 $p^2$ 系数。
仅作为特征零**形式恒等式**置
$$
 E(w)=\frac{\sigma(L(w))}{w}.
$$
由定义直接得到
$$
 U(w)=\frac{E([p](w))}{E(w)^{p^2}}.
 \tag{C10}
$$
以下只读到 degree $d$，不在挠点评价 $E$。
R301 的原低窗及(C7)表明
$[w^j]\log E(w)$ 在 $0<j<d$ 时整；
其 $d$ 次系数为 $c_\sigma$ 加一个整元素。
说明如下：$L(w)=w+\cdots$ 的所需窗口整可逆；
$\log(L(w)/w)$ 在此窗整，且
$\log(\sigma(L(w))/L(w))$ 的首个非整系数恰是
$c_\sigma w^d$。所有非零次数均为6的倍数，低窗内涉及的
指数/对数分母小于 $p$，没有另一个 $p$ 损失。

$[p](w)$ 在 degree $<p^2$ 的系数都被 $p$ 整除，
而 $\log E$ 的首次数至少6。因此(C10)在 degree $\le d$ 给
$$
 \boxed{
 [w^j](U-1)\in p^2\mathcal O\quad(0<j<d),\qquad
 \frac{[w^d]U}{p}\equiv-\kappa_\sigma\pmod p .
 }
 \tag{C11}
$$
具体地，$\log E([p](w))$ 在这一窗被 $p^2$ 整除；
$-p^2\log E(w)$ 的 $d$ 次项是 $-p^2c_\sigma$ 加 $p^2$ 整项。
从 $\log U$ 返回 $U$ 的非线性项在该窗也被 $p^2$ 整除。
(C9)同时控制全部更高系数，不只控制这个前缀。

在非零 $Q\in E[p]$，(C7)有
$D^2[p](w)(Q)=0$：
$D[p](w)=p\sqrt{1+[p](w)^6}$，再求导并代 $[p](w_Q)=0$。
对(C8)在 $Q$ 取两次导数，与(C1)合并，严格得到
$$
 Z_Q=D\log w(Q)-p^{-2}D\log U(Q).
 \tag{C12}
$$
这里 $U$ 是整单位，故此评价在 $w_Q$ 的 formal disc 内合法。

所有 $w_Q$ 都满足 $v_p(w_Q)=1/\Delta_p$。
(C11)的 $d$ 次项在 $p^{-2}D\log U(Q)$ 中估值为
$-1+p/\Delta_p$，其系数为单位。
更低次数的项估值至少 $-1/\Delta_p$；
由(C9)，更高次数的项估值至少
$-1+(j-1)/\Delta_p$，严格较大。
在 $U^{-1}$ 与 $Dw$ 中乘入非恒项也只提高估值。
所以第一项不会与任何高尾抵消，得到
$$
 \boxed{
 v_p(Z_Q)=-1+\frac p{\Delta_p},\qquad
 \frac{pZ_Q}{w_Q^p}\equiv d\kappa_\sigma
                    \equiv\kappa_\sigma\pmod{\mathfrak m}.
 }
 \tag{C13}
$$
剩余域可以包含全部 actual division-field 数据；$\mathfrak m$
是其 valuation ring 的极大理想。
本证明完全通过整 $U$ 和有限形式系数进行，没有用
$\zeta(q)$ 在临界点的原点级数收敛。

## 18. 所有阶的严格支配与每个原 translated source 的真实半径

假定原固定 $R_N$ 的系数在该位整，且
$s_N(z)=a_0z^a+\cdots$、$a_0\in\mathcal O^\times$。
对本篇三条归一负源 $a=4,N=102$；
原 canonical 正源 $S$ 的 $N=34,a=6$，首系数为1。
参考 $H_3,H_5$ 有原已付的非零中央质量，所以它们须按
$a=0$ 和其真实质量处理，并在需要本节准确估值时保持该质量
在当前位为单位的条件；不能把它们的 $z^6$ 系数冒作首项。
实际 raw 的固定外幅度另按其已付值乘入；若某个其它 transported
线性组合不满足此首项条件，只使用(C5)，不免费套本节等式。

写
$$
 A_{N,m}=\sum_{b=0}^m R_{m,b}(x,y)Z^b.
$$
由(C2)归纳，$R_{m,b}$ 的 Laurent 系数整，且
$$
 \operatorname{pole}_O R_{m,b}\le N-a+m-b,\qquad
 R_{m,m}=N^mR_N .
 \tag{C14}
$$
确切地，$D$ 在 good 参数中加至多一个 pole，
$-x\partial_Z$ 减一个 $Z$ 幂并加至多两个 pole，
$NZ$ 加一个 $Z$ 幂而不改 pole；三项都保持(C14)。
全程仅有整数微分系数，没有除 $m!$，所以任意大的 $m$
也不产生未记分母。

令 $\tau_p=p/\Delta_p$。最高 $Z^m$ 项的估值为
$-(N-a)/\Delta_p+m(-1+\tau_p)$。
由(C13)--(C14)，每个 $b<m$ 项与它的估值差至少
$$
 (m-b)\left(1-\tau_p-\frac1{\Delta_p}\right)
   =(m-b)\left(1-\frac1{p-1}\right)>0 .
 \tag{C15}
$$
因为 $p\nmid N$，最高系数 $N^m a_0$ 仍为单位。
因此所有 $m\ge0$ 都有准确等式
$$
 \boxed{
 \begin{aligned}
 v_p\bigl(A_{N,m}(Q,Z_Q)\bigr)
   &=-\frac{N-a}{\Delta_p}+m(-1+\tau_p),\\
 v_p\!\left(D_{z'}^m
      (\mathsf W_T[p]^*s_N)(0)\right)
   &=\frac a{\Delta_p}+m\tau_p .
 \end{aligned}}
 \tag{C16}
$$
这次确实为每个非零 translated source 单独支付了费用，
不是从 whole theta 有界性倒推。

Taylor 系数是(C16)第二行再减 $v_p(m!)$。
由 Legendre 公式，在闭 Lie 盘 $v_p(z')\ge r$ 上的第 $m$ 项
准确加权估值为
$$
 \frac a{\Delta_p}
 +m\left(r-\frac1{\Delta_p}\right)
 +\frac{s_p(m)}{p-1},
 \tag{C17}
$$
$s_p(m)$ 为 $p$ 进数字和。
故严格 $r>1/\Delta_p$ 时该 series 属于 Tate algebra，
并且常数项严格支配全部非恒项：除其实际常数后的 series
及逆均为 norm1。没有重选原 theta 常数。
在边界 $r=1/\Delta_p$，沿 $m=p^e$ 的加权估值恒为
$a/\Delta_p+1/(p-1)$，所以不为 Tate，也不能在边界直接代入该
Lie series。其精确半径仍须与物理 $z=pz'$、
coherent 变量及 R1060 原 period 全部运输后再使用。
整代数 section 在形式参数中的正则性不消掉这个 Lie 边界。

## 19. 全部 Q、原中心和完整有限临界读者

定义 $\mathcal J_{r,s}$ 为(13)返回**原物理两变量**
$z_-,z_+$ 后的 $(r,s)$ 阶导数。
取每个 $Q\in E[p]$ 的一个原相容 lift $T$；
正侧使用同一个图 lift $\gamma_{102,p}T$。
令
$$
 \mathfrak b_p(Q)=
 b_{102,\widetilde Q}\,
 b_{34,\widetilde{\gamma_{102,p}Q}} .
$$
单个 $b$ 保留原中心；两个乘积在改变相容 lift 时不变，
这是(12)--(13)的同一个 cocycle 消去。
以 $d_{-,r}=D^rs_-(0)$、$d_{+,s}=D^ss_+(0)$ 记原未平移 jet，
则准确有
$$
 \boxed{
 \begin{aligned}
 \mathcal J_{r,s}=\frac1{p^2}\biggl\{
  d_{-,r}d_{+,s}
  +\sum_{\substack{Q\in E[p]\\Q\ne O}}
    \mathfrak b_p(Q)\,
    A_{102,r}(Q,Z_Q)\,
    A_{34,s}(\gamma_{102,p}Q,
                     Z_{\gamma_{102,p}Q})
                 \biggr\}.
 \end{aligned}}
 \tag{C18}
$$
$Q=O$ 不使用(C1)或(C13)，它是式中单独保留的原 seed。
$p^{-2}$ 是阶 $p^4$ 群的真实平均及阶 $p^2$ old 稳定子给出的
那个系数。原 bad 输入还须按 R1054 保留 $-w_0$；
在整个 R1052 所指定的投影之外不能删除它。

(C18)在每个真实 finite/$h$ 字上先按 R1054 Egorov 运输；
原 $R_N$、Miller lift、$\gamma$ 和变量矩阵一起运输。
回到 native coherent $(Z,W)$ 时，要施原
$z_-=\Omega_0h_HT_-/\delta$、$z_+=\Omega_0h_HT_+$，
$T_\pm=-ib(Z,W)$、实际 arch/代数 period 改写及整 $h$ 积分。
这些都是已指定的线性操作。
所以把(C18)代入 R1060 的完整有限转置合法，
但不能将 $\mathcal J_{r,s}/(r!s!)$ 未经这些操作就改名为
该处的 $h_{r,s}$。尤其不得删去那里的冻结外权及其导数。

(C18)是有限 division-field 表达：
$Z_Q$ 用原 $r_p',r_p''$，
$A_{N,m}$ 用(C2)，全部中心常数用(C4)及原 lift。
在有限计算中可先生成(C2)再在各点或其 finite étale 代数中评价。
若以该代数实现，不可在中途约去 torsion 理想后继续求 $D$，
因为 $D(r_p)$ 在这些点不为0；要保整个相应 jet 或先作完(C2)。

还给出具体精度账本。对本篇 canonical $k=1$ 的 $a_-=4,a_+=6$ 规范原源，
每个非零 $Q$ summand 在乘 $p^{-2}$ 后的估值准确为
$$
 -2+\frac{10}{\Delta_p}
       +(r+s)(-1+\tau_p).
 \tag{C19}
$$
它们的和只可能提高估值，不能据单项精度断言全和非零。
$Q=O$ 的真实估值另由 $d_{-,r}d_{+,s}/p^2$ 给出。
若已付 R1060 的某个有限 reader 行是
$\sum a_{r,s}\mathcal J_{r,s}$，要达到绝对 $p^H$，
各未乘 $p^{-2}$ 的完整产品保到
$H+2-v_p(a_{r,s})$ 的绝对精度即够；
原 period、Artin/Cor 和有限 $h$ 权已包含于其实际行系数。
有限求和的项数不另产生一个分母。
这给真正全部连接项的有限精度来源，不是新设另一条 reader。

原 canonical 坏条件只能作用在其已授权的原整 Newton 行。
即使原 $[p]$ seed 已由 R1060 的 exact pullback
运输该坏条件，(C18)中全部非零 $Q$ 的译像和仍必须按同一
有限行处理。本文没有把它们逐项赋零，也没有从(C13)、(C16)
的单项非零推出该完整线性和非零。

本附节是原精确乘法、整形式群和全阶递推的纸面证明；
没有数学执行，也没有另开任何作业。
