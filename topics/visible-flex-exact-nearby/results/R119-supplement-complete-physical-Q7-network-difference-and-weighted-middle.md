# R119 续篇：完整物理 Q=7 网络差、根图 Möbius 接线与新谱权中频压缩

2026-11-14，visible-exact / tail_connector。

**状态：解析证明，供独立审查。** 本篇固定同一个真实背景
$X=X_{\Gamma^*(\mathbf a,\Omega),\Omega}(\mathbf a)$，比较其完整
fixed-parameter Jacobi 网络与五参数选择所得的径向网络。
两者都使用下降坡两侧原来的 $Q=7$ 物理端口。
实际参数值 $\Gamma^*-\bar\Gamma$、两个根图、两段外负缓冲、
完整正区双端响应、两条 mean 行和全部 Fourier 交叉均保留。

对较深层 $j\ge8193$，$J=j+5$、$\delta=\delta_j$，本篇得到每条
真实内部行及其 adjoint 列的全频一阶损失界
$$
 \boxed{\quad
 \|\Delta\mathcal U_i:H^1(\text{全部邻端口})\to L^2\|,
 \quad
 \|(\Delta\mathcal U)^*_i:H^1(\text{全部邻端口})\to L^2\|
 <2^{22000}J^{24}\delta^{-38}
                   \mathcal N_{i|j}\mathcal X .
 \quad}                                                     \tag{D.1}
$$
这里是完整原物理角上的算子差，不是逐 Fourier 对角差，也没有
把角 pullback 的小位移当成同阶 operator 小量。

用[五盒完整径向谱选择](R119-supplement-five-local-parameter-cube-and-complete-radial-network-selection.md)
(Q.27) 的实际逐窗权 $\mathcal W$，原物理角的裸中频投影
$P_{\rm mid}$ 满足
$$
 \boxed{\quad
 \|\mathcal W^{-1}P_{\rm mid}
        (\mathcal U_a-\mathcal U_0)
       P_{\rm mid}\mathcal W^{-1}\|_{\ell^2L^2\to\ell^2L^2}
 <2^{-6000000}.
 \quad}                                                     \tag{D.2}
$$
外 high prefix、无限 low 余尾和 mean 尚未在 (D.2) 中消去。
特别，$P_{\rm mid}(I-\mathcal U_0)P_{\rm mid}$ **不是** 五盒篇的
有限有效 $I-U_M$。最后一节写出准确 Schur 差及其尚需的输入，
不据 (D.2) 宣布实际全网络 inverse。

## 1. 同一对象、端口和原参数值变化

采用五盒篇的同一实际共同参数点以及
[当前紧/高混频型](R119-supplement-current-compact-and-high-scaled-mixed-pocket-forms.md)
(A.1)--(A.3)。特别
$$
 \mathcal X\le2^{-8388608},\qquad
 n_i=4\mathcal N_{i|j}\mathcal X,\qquad
 \mathcal N_{i|j}
 <2^{-20010}2^{-(31867/256)(j-8193)}.                       \tag{D.3}
$$
$\mathcal N_{i|j}$ 是原完整六项邻胞和，保留两次规范接缝；
它不是重新设定的单层小量。所有正区和 root germ 不依赖下降
bump；下降形状、两个补偿 bump 和真实 $\Gamma^*$ 都在原全
$C^4$ 盒内。整体相似尺度 $\rho(\Gamma^*)$ 在双方使用同一个值；
它从齐次 canonical 单位中相消，仍留在 raw 源和物理重建中。

[固定窗口原定义](R119-supplement-phase-preserving-actual-finite-Schur-controls.md)
§1 的窗口只包含下降坡及两侧各长 $a_j/4$ 的 $Q=7$ 缓冲。
两个真正的转向根在窗口外。下文绝不把该窗口端口改名为
root-Airy amplitude。

在每个 $Q=7$ 切口置
$$
 k_m=\sqrt{7m^2-16}\quad(m\ne0),\qquad k_0=1,\qquad
 \mu_0=w_{\rm ref}/a_{\rm phys}.
$$
对齐次源，固定 canonical 两行是
$$
 Z_1=k^{1/2}\sqrt{\mu_0}\,h,\qquad
 Z_2=k^{-1/2}\mu_0^{-1/2}(p-4\mu_0h),\qquad
 p=\mu(h_t-dh_\theta).                                   \tag{D.4}
$$
有 weak 源时把 $p$ 换成 $p+F^t$。非mean的 (D.4) 正是原
wave 单位，因为端点 $\mu_{0,t}/\mu_0=-8$。$k_0=1$ 只是给
原两个真实 mean 状态一个固定正的 canonical 单位，没有用
$m^{-1}$ 定义它们，也没有清除常高度方向。

(D.4) 保持 raw 高度/total-flux Green pairing。固定
$(Z_1\mp iZ_2)/\sqrt2$ 为两 wave 行，并按各段 outward 法向作
明确交换。所有以下同阶范数都在这同一 $L^2$ 或 $H^1$ 单位中。

当前参数值的完整逐行差由第51束 (H.4) 及第55束 (N.2),
(N.9)--(N.16) 的同对象重付给出。放宽为
$$
 \gamma_i:=|\Gamma_i^*-\bar\Gamma_i|
 <2^{200}J^4\delta^{-6}\mathcal N_{i|j}\mathcal X.          \tag{D.5}
$$
这两个分量都保留；$\Gamma^*$ 的**导数列**将在第7节另写。
参数值的差与未知 Jacobi 方向中的 $D\Gamma^*$ 不是同一项。

## 2. 固定物理角的完整 strict Cauchy 差

使用
[完整严格密度证明](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
(S.6)--(S.18)，令
$$
 \Lambda=\mu qv,\quad q=\sqrt Q,\quad w=\sqrt\Lambda h,
 \quad
 \zeta=\frac{p+\frac12\mu(\ell_t-d\ell_\theta)h}{\sqrt\Lambda},
 \quad \ell=\log\Lambda,\quad y_\sigma=(w_\theta+\sigma\zeta)/2 .
$$
齐次方程在**原物理角**准确为
$$
 (y_\sigma)_t+\partial_\theta(g_\sigma y_\sigma)
       =-\sigma\kappa w/2,\qquad
 w_t=d(y_++y_-)+qv(y_+-y_-),\qquad g_\sigma=-d-\sigma qv .
 \tag{D.6}
$$
完整空间是
$$
 \mathcal E_s=
 \{(a,y_+,y_-):\langle y_++y_-\rangle=0\},\qquad
 w=a+\partial_\theta^{-1}(y_++y_-).
 \tag{D.7}
$$
$a=\langle w\rangle$ 的方程由 (D.6) 第二式取平均得到。
另一个独立 mean 是 $\langle y_+-y_-\rangle$。两者都留在
$\mathcal E_s$，它与原完整特征标签 $\mathcal F_s$ 双向等价。

原 (S.16),(S.19)--(S.20) 使该真实坐标转换及逆的 norm 小于
$2^{24}$。因为原完整光学长度小于1，lift 差的 mean 项也在此
常数内。第55束对原宽盒重付后的 strict 条件数取
$2^{1100}J^5\delta^{-10}$；加入上述两端转换和 actual 的因子2，
任意两个 strict 截面的物理演化满足
$$
 \|U_a(t,s)\|_{\mathcal E_r},\ \|U_0(t,s)\|_{\mathcal E_r}
       <K_{\rm ph}:=2^{1150}J^5\delta^{-10},
 \qquad r=-1/2,\ 1/2.                                   \tag{D.8}
$$
这并非由同宽小 pullback 差推出；它只是两个完整 bounded 坐标
转换与原已付实际演化的有序复合。

同一 $\Gamma$ 下，(S.10)--(S.13) 给
$\int\|\kappa-\kappa_0\|_{\mathcal A_1}
 <2^{128}J^2\delta^{-5}n$，以及
$\int(\|d\|_{\mathcal A_1}+q\|v-1\|_{\mathcal A_1})<2^{10}Jn$。
将 (D.6) 作为
$\mathcal E_{r+1}\to\mathcal E_r$ 的 generator，完整乘积和 mean
行因而给
$$
 \int\|\mathsf A_a-\mathsf A_{0,\Gamma}\|
          _{\mathcal E_{r+1}\to\mathcal E_r}
       <2^{256}J^3\delta^{-5}n,\qquad r=-1/2 .             \tag{D.9}
$$
传输主项仍保留一次 $\partial_\theta$；这正是显示的一阶损失。
mean 行用归一平均和实际解析乘子估计，不作一点取值。

为比较实际 $\Gamma^*$ 与 $\bar\Gamma$，只对**系数**作 Cauchy。
[双 bump 重建](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
(U.1),(U.5)--(U.6) 给实际复盒：
第一 bump 的 $|\psi_1'|\le96$、第二 bump 的
$|\psi_2'|\le384$，其支集上分别 $S'>1$ 和 $S'>1/2$，
而 $\Delta>80$。以当前实参数为中心的半径 $2^{-64}$ 复盘
严格包含于原盒，并使 $Q$ 在 bump 支集上相对改变小于
$2^{-32}$；其它位置不变。于是 $\sqrt Q$ 取同一个解析支。

原[参考几何](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)
(F.3) 及第53束 (C.15) 在此更小复盘可放宽成
$$
 |Q|<2^{20}J\delta^{-3/2},\quad
 |Q_t|<2^{30}J\delta^{-3},\quad
 |Q_{tt}|<2^{40}J\delta^{-9/2},\quad
 |\sqrt Q|>1/32,\quad |I|<4\delta .
$$
第三 jet 的两个 bump 比例已经在双参数篇 §2 支付。
把这些数直接代入 (S.8)，而非对传播算子作复参数延拓，得到
$$
 \int_I\left(1+|\sqrt Q|+|\kappa_0|\right)dt
                         <2^{128}J^2\delta^{-5}.
$$
例如最大的粗项 $Q_t^2/|\sqrt Q|^5$ 积分小于
$2^{87}J^2\delta^{-5}$；其它项的 $\delta$ 幂更小。
系数 Cauchy、两个参数计数和 (D.9) 因而给
$$
 \int\|\mathsf A_a-\mathsf A_{0,\bar\Gamma}\|
            _{\mathcal E_{1/2}\to\mathcal E_{-1/2}}
 <2^{512}J^3\delta^{-5}(n+\gamma_i).                      \tag{D.10}
$$
这里没有声称复杂角或复参数的无限高频 propagator 在实
$L^2$ 上有界。

在光滑输入上直接用准确 Duhamel：
$$
 U_a(t,s)-U_0(t,s)
  =\int_s^t U_a(t,\tau)
       (\mathsf A_a-\mathsf A_0)(\tau)U_0(\tau,s)\,d\tau .
 \tag{D.11}
$$
左边演化只消费 $\mathcal E_{-1/2}$，右边只消费
$\mathcal E_{1/2}$，二者都由 (D.8) 支付。连续延拓即给
$$
 \|U_a-U_0:\mathcal E_{1/2}\to\mathcal E_{-1/2}\|
 <2^{2813}J^{13}\delta^{-25}(n+\gamma_i).                 \tag{D.12}
$$
同一 $\Gamma$ 时可将 $2813$ 改为 $2557$，但以下保留前者。
逆向传播用同一个公式，界不变。这里总共只乘两个完整 Cauchy
因子；没有先形成相对 interaction，再额外乘第三个因子。

在 $Q=7,Q_t=0$ 的端点，(D.4) 与 (D.7) 的双向转换满足
$$
 \|J_Q^{\pm1}\|<2^{128},\qquad
 \|J_{Q,a}^{\pm1}-J_{Q,0}^{\pm1}\|<2^{160}n
 \tag{D.13}
$$
于 $H^r\oplus H^r\leftrightarrow\mathcal E_{r-1/2}$，
$r=0,1$。可直接代
$w=\sqrt{q/D}\,u$ 和
$\zeta=\sqrt{D/q}\{v+(\mu/\mu_0)
(\ell_t-d\ell_\theta)u/2\}$ 核实：
径向 $\ell_t=-8$ 正好消去 (D.4) 的 $4\mu_0h$ shear，
$k_m\asymp1+|m|$，mean 用 $k_0=1$ 单独代入。
剩余实际乘子及其角导由 (S.10) 支付；$\mu_0$ 的绝对大小相消。

因此完整短负窗口的 Cauchy 差进入 $H^1\to L^2$。
将完整 transfer 改为 scattering 时也不另收条件数：
固定 incoming，径向左状态的 norm 至多 $\sqrt2$ 倍 incoming，
传递差成为实际 scattering 的 particular；完整源消元的 norm
小于2。故
$$
 \|S_{i,a}-S_{i,0}:H^1\to L^2\|
 <2^{3500}J^{18}\delta^{-32}
                     \mathcal N_{i|j}\mathcal X.          \tag{D.14}
$$
(D.5) 已在此代入。实际和径向 $S_i$ 都在完整两端 $L^2$ 上
酉，径向算子在全部 $H^r$ 上亦 norm1。
恒等式
$\Delta S^*=-S_a^*\Delta S\,S_0^*$
给相同的 adjoint 一阶损失界；mean 仍在实际算子中。

## 3. 根到 fixed strict 切口：直接使用 balanced-root 两行

本节只用
[联合解析根](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
(J.27)--(J.31) 和
[准确根图](R119-supplement-actual-root-graph-to-fixed-radial-two-port.md)
(G.4),(G.14)--(G.26)。
中间根端口取
$$
 (W u,W^{-1}u_\xi),\qquad
 W_m=(1+(|m|/b)^{4/3})^{1/4}.
 \tag{D.15}
$$
它与正区 (C.21) 的 true 根端口完全相同。
无需再转成自由 Airy 振幅；旧 (H.17) 的已勘误低模 frame 估计
不参与本篇任何一步。

根平衡演化 $U_R$ 的正逆 norm小于 $2^{2185}$，
且 actual-minus-radial 正反差小于 $2^{6606}n$。
根外固定 canonical 截面上的 $A_*$ 就是 (G.22)，
双向 norm小于 $2^{20}\sqrt b$。
真实 graph 的 $\mathcal T_g$ 双向 norm小于 $2^{21}$，
并由 (G.21) 给
$\|\mathcal T_g-\mathcal P_g\|<2^{112}bn$。
再由 (G.4),(G.16) 的准确特征位移，
$$
 \|\mathcal P_g-I:\mathcal E_{r+1}\to\mathcal E_r\|
                                  <2^{100}n/b .
 \tag{D.16}
$$
高度 mean 是 (G.17) 的完整行，没有另丢一个 primitive 常数。

还须将 graph 的角换回真正原物理切口。二维密度行列式不变量
(G.24) 给 $k=\alpha c=\Lambda\circ\Psi^{-1}$。因此由 (G.25)
和 density 共轭的完整 shear 准确得到
$$
 w_{\rm phys}=W_g\circ H,\qquad
 (y_\sigma)_{\rm phys}=H'\,Y_{\varsigma\sigma}\circ H .
 \tag{D.17}
$$
这里 $W_g$ 是 graph 密度高度，不是 (D.15) 的 Fourier 权。
证明第二式时，(G.25) 中
$-\varsigma H's_gW_g$ 恰被物理
$(\ell_t-d\ell_\theta)w_{\rm phys}/(2qv)$ 抵消；
这是完整 conormal 链式法则，不是删除 normal shear。
第一式的平均仍是 $\langle W_g\circ H\rangle$。
$\varsigma=-1$ 时的支交换准确保留。

记 (D.17) 的完整 map 为 $J_H$，把固定支交换纳入其径向版本。
(G.4) 和同一圆周 FTC 给双向 norm小于 $2^{24}$，以及
$\|J_H-J_{H,0}:\mathcal E_{r+1}\to\mathcal E_r\|
 <2^{100}n/b$。于是完整根到固定物理 strict 口为
$$
 L_e=J_H\,\mathcal T_g\,A_*\,U_R .                         \tag{D.18}
$$
准确有
$$
 \|L_e^{\pm1}\|<2^{2300}\sqrt b,\qquad
 \|L_{e,a}-L_{e,0}:H^{r+1}\to\mathcal E_{r-1/2}\|
                                      <2^{6700}b^{3/2}n ,
 \quad r=0 .
 \tag{D.19}
$$
第一项的 bits 为 $24+21+20+2185<2300$。
第二项按四因素有序差展开：root 势差至多
$2^{6671}\sqrt b\,n$；graph 差乘 $A_*U_R$ 至多
$2^{2350}b^{3/2}n$；两个 angular FTC 项只更小。
所有前后因素分别在已付 $r=0,1$ 窗内。
逆恒等式
$L_a^{-1}-L_0^{-1}=-L_a^{-1}(L_a-L_0)L_0^{-1}$
进一步给
$$
 \|L_{e,a}^{-1}-L_{e,0}^{-1}:
                    \mathcal E_{1/2}\to H^0\oplus H^0\|
                                 <2^{11400}b^{5/2}n .
 \tag{D.20}
$$
这就是需要的完整 mean、图和双行费用；未从逐模 Airy 高度界外推。

## 4. 两段真实负缓冲，全部费用带回 Q=7

从每个 root 到相邻下降窗口的 $Q=7$ 口，仍有一个真实
strict 缓冲。它不含两个 $\Gamma$ bump 或新 compact 支集，
所以 radial profile 在该处准确相同。
结合 (D.8),(D.12)--(D.13),(D.18)，定义其完整 transfer
$B_e=J_Q U_{\rm st}L_e$，按 outward 法向作固定 wave 交换后，
$B_e$ 是 onto 的 $J$-unitary 算子。

实际斜率的原宽界是
$$
                b<2^{32}\sqrt J\,\delta^{-9/4}.
$$
(D.19) 与 strict 条件数给
$$
 \|B_e\|,\ \|B_e^{-1}\|
 <K_B:=2^{3800}J^6\delta^{-89/8}.                         \tag{D.21}
$$
$89/8=10+9/8$，来自 $\delta^{-10}\sqrt b$。
有序 forward 差与 inverse 差都满足
$$
 \|B_{e,a}-B_{e,0}:H^1\to L^2\|,\quad
 \|B_{e,a}^{-1}-B_{e,0}^{-1}:H^1\to L^2\|
 <E_B:=2^{13200}J^{15}\delta^{-209/8}n .                  \tag{D.22}
$$
最坏径向幂是 strict 差的 $\delta^{-25}$ 乘 $\sqrt b$，
即 $209/8$。其它两类分别是
$\delta^{-10}b^{3/2}$ 和
$\delta^{-10}b^{5/2}$，对应 $107/8$ 与 $125/8$，
都严格小于 $209/8$。最大的 inverse bits 小于
$128+1150+11400+80=12758$。
(D.21)--(D.22) 同时覆盖两侧缓冲；没有穿过一个根后再把它
与 $Q=7$ 口等同，也没有丢掉 root 低输入到高输出。

## 5. 完整正图及一个无需高阶实际逆的 Möbius 比较

先在两个根的**原物理角**工作。把
[正区完整 DN](R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md)
(C.5) 的端角设成 $K_-=K_+=\mathrm{id}$：
先解真实 drift，再以原光学变量插回两端 identity。
这是同一物理方程的一次明确坐标选择，并非改变已选 KAM 角图。
该构造的 $H_\pm-\mathrm{id}$ 小于原 (C.6) 上界，故
(C.7)--(C.20) 的完整 form/resolvent 证明逐项适用。
接着用 (C.21) 的实际密度和全部 normal shear，得到 (D.15)
单位中的真正双根 graph $R_a$。其径向参考是 $R_0$，且
$$
 R_a,\ R_0\text{ 在两根完整 }L^2\text{ 上酉},\qquad
 \|R_a-R_0\|_{L^2\to L^2}<E_R:=2^{170}J^2\delta^{-2}n .
 \tag{D.23}
$$
两端 cross、共同常高度、mean 高度差及 mean flux 均保留。
(C.20) 还给所需原 Sobolev 窗，但下面只用它的 $L^2$ 门。

为避免多乘一个虚假的 graph 条件数，记录完整算子恒等式。
设 $T=(A,B;C,D)$ 是一个 onto $J$-unitary，$\|T^{\pm1}\|\le K$，
根 graph 为 $v=Ru$，$R$ 酉。则
$$
 F=A+BR,\qquad S=(C+DR)F^{-1}.                            \tag{D.24}
$$
$A^*A\ge I$ 与 $AA^*\ge I$ 同时保证 $A$ 可逆，且
$\|A^{-1}B\|^2\le1-\|A\|^{-2}<1$，故 $F$ 满射可逆。
$T(u,Ru)$ 是 null 向量，所以其两行 norm相等；再用
$\|T^{-1}\|\le K$，准确得到 $\|F^{-1}\|\le K$。
同一 Green pairing 及反向构造说明 $S$ 满射酉。

对 actual 和 radial 两个系统，令 $\Delta$ 表示 actual-minus-radial。
直接由 $S_aF_a=C_a+D_aR_a$ 相减：
$$
 \begin{split}
 (S_a-S_0)F_0={}&
  \Delta C+\Delta D R_0
        -S_a(\Delta A+\Delta B R_0)\\
 &+(D_a-S_aB_a)(R_a-R_0).
 \end{split}                                             \tag{D.25}
$$
径向 $F_0^{-1}$ 在 $H^1$ 上与 $L^2$ 有同一个界，$R_0$ 在
$H^1$ 上 norm1；实际 $S_a$ 只在 $L^2$ 上收费1。
若 $\|\Delta T:H^1\to L^2\|\le E_T$，则
$$
       \|\Delta S:H^1\to L^2\|
                     \le4K E_T+2K^2 E_R .                \tag{D.26}
$$
没有要求未知实际 $F_a^{-1}$ 具有一个未支付的 $H^1$ norm。
实际 adjoint 的同一一阶门再由
$\Delta S^*=-S_a^*\Delta S\,S_0^*$ 得到。

现在取 $T$ 为左右两个 (D.21) 缓冲的 direct sum，并按固定
法向作必要的交换。它把真正完整 positive root graph 送到
两个下降窗口的 $Q=7$ 口。所得完整正连接 $P_a$ 因而满足
$$
 \begin{split}
 \|P_a-P_0:H^1\to L^2\|
 &<4K_BE_B+2K_B^2E_R\\
 &<2^{18000}J^{24}\delta^{-38}n .
 \end{split}                                             \tag{D.27}
$$
第一项的准确 $\delta$ 幂是
$89/8+209/8=149/4<38$；第二项为
$89/4+2=97/4<38$。
这一步完整消费两个根、两个外负缓冲和中间正区。
它不使用正区 transmission 的正下界，不倒除指数小的 cross。

## 6. 完整原网络差及已选择权的实际消费

在所有真实内部 $Q=7$ 口保留原 wiring：
$$
 y=S_a x+t_a,\qquad x=P_a y+p_a,\qquad
 \mathcal U_a=P_a S_a .
 \tag{D.28}
$$
$P_a$ 是各完整 (D.27) 的连接直和和固定置换。
最外尚未消去的端口照常作为实际外输入；不得给它补造反射。
(D.1) 只涉及深部内部行，任何有限穷尽都保留两端真实资料。
每行/列的相邻端口数按原宽界不超过8。

准确有
$$
 \Delta\mathcal U=P_a(S_a-S_0)+(P_a-P_0)S_0 .
$$
第一项左因子在 $L^2$ 上酉，第二项右因子径向且在 $H^1$
上酉。(D.14),(D.27) 及 $n=4\mathcal N\mathcal X$ 因此给
(D.1)。adjoint 用相反有序式，仍只在实际一侧消费 $L^2$
酉性。完整输出无限 Fourier 尾、mean 及跨角锥均在此界中。

现在只作固定原物理角上的裸压缩：
$$
 P_{{\rm mid},i}=\mathbf1_{\{A_j\le |m|\le T_j\}},\qquad
 A_j=2^{-40}\delta_j^{-1/8},\quad
 T_j=2^{65664}J^2\delta_j^{-9}.
 \tag{D.29}
$$
$\mathcal W$ 必须使用五盒篇 (Q.27)；其统一上包络是
$$
 \mathcal W_{i,m}^{-2}
       <V_j:=2^{864000}J^{8330}\delta_j^{-1073/16}.
 \tag{D.30}
$$
没有恢复先前较有利但不再适用的旧 $\delta$ 权。

对每个真实相邻块，以 (D.1) 消费一次输入 $H^1$，
再乘两侧 (D.30)。相邻 $J,\delta$ 的固定比、每列/行至多8项，
以及 $\langle m\rangle<2T_j$ 共可收在额外 $2^{2000}$ 内。
故加权块的 Schur 行、列上界都小于
$$
 2^{970000}J^{8400}\delta^{-1825/16}
                            \mathcal N_{i|j}\mathcal X .
 \tag{D.31}
$$
显示的径向幂准确来自
$$
                 38+9+\frac{1073}{16}=\frac{1825}{16}.
$$
(D.31) 没有使用输出 cutoff 偷换输入 cutoff，也不要求输入
属于某个 $\kappa$ 包；三个缩放区之间的所有混频块一起参加。

在首层 $J<2^{14}$、$\delta^{-1}<2^{8197}$，其二进制指数小于
$$
 970000+8400\cdot14+\frac{1825\cdot8197}{16}
                      -20010-8388608<-6000000 .
$$
每深一层的真实指数余量为
$$
 \frac{31867}{256}-\frac{1825}{16}
                       =\frac{2667}{256}>10 .
$$
而 $(1+1/J)^{8400}<4$ 于 $J\ge8198$；
因而完整行列界随后至少按 $2^{-8}$ 下降。
Hilbert 块 Schur 估计即得 (D.2)，且与径向穷尽长度无关。
以上是显示有理不等式的解析费用，没有新数值试验或未运行门。

## 7. 原 ordinary/weak、joint 两列及准确外 Schur 范围

所有 preceding homogeneous maps 都以 total flux 定义。
对真正 affine 根图
$v=Ru+q_R$ 和 transfer
$(u_{\rm cut},v_{\rm cut})=T(u,v)+(f_u,f_v)$，
(D.24) 的完整 source 准确成为
$$
 q_{\rm cut}=(D-SB)q_R+f_v-Sf_u,\qquad
 \|q_{\rm cut}\|\le2K\|q_R\|+2\|(f_u,f_v)\| .             \tag{D.32}
$$
正区 $q_R$ 必须来自原 (C.25)--(C.33) 的完整 Piola、
ordinary 修正、dual energy 电荷和两个 mean。
root 的源对仍为 (J.34)--(J.37)，graph 的 body 与法向负荷
仍为 (G.30)--(G.37)，strict 仍为 (S.32)--(S.35)。
本篇没有从任意粗径向 $L^2$ 体源自动取得这些混合图 trace norm；
原 producer 没提供 bare $F^t$ 端迹时，只授 total-flux 端口。

$\Gamma^*$ 值的变化已经由 (D.5),(D.10),(D.14) 进入齐次比较。
对实际选参解作 Jacobi 微分时，两个 metric 列还必须完整保留：
$$
 (I-\mathcal U_a)x
     =g_{\rm ord,weak}+\mathcal B_a\dot\Gamma+g_{\rm ext},
 \qquad
 \mathcal C_a x+\mathcal A_a\dot\Gamma=g_{\rm phase}.
 \tag{D.33}
$$
$\mathcal B_a$ 是原两个 strict 支集的真实 metric/source 列，
并含参数化端口微分；$\mathcal C_a,\mathcal A_a$ 是两个完整
joint 相位方程的微分。第55束给该 joint 选择的真实逆，
但将其改成 (D.33) 的原端口/source-to-label norm仍须实际收费。
不能把 $D\Gamma^*(0)=0$ 写成当前非零背景的
$\dot\Gamma=0$，也不能把这些 affine 列从问题中删除。

最后明确裸压缩与正确有效网络的差别。
若把一完整酉网络按保留 $P$ 与外部 $Q$ 分成
$$
 U=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad
 R=(I-D)^{-1},
$$
则真正有效算子和完整源是
$$
 S_{\rm eff}=A+BRC,\qquad
 g_{\rm eff}=g_P+BRg_Q,\qquad x_Q=R(Cx_P+g_Q).
 \tag{D.34}
$$
五盒篇的径向 $U_M$ 使用的正是这种真实外消元，含完整 high
prefix、无限 low 允许线及 affine 源。它不等于 $A$。

当实际和径向外逆都在所用空间中存在时，有准确有序恒等式
$$
 S_{{\rm eff},a}-S_{{\rm eff},0}
  =\begin{pmatrix}I&B_aR_a\end{pmatrix}
       (U_a-U_0)
       \binom I{R_0C_0}.
 \tag{D.35}
$$
若暂在一个有界 $L^2$ 外逆合同中讨论，酉性还能准确节省条件数：
$$
 RC C^*R^*=R+R^*-I,\qquad
 R^*B^*BR=R+R^*-I,
$$
$$
 \|RC\|,\|BR\|\le(2\|R\|+1)^{1/2}.                       \tag{D.36}
$$
这些式子来自 $CC^*+DD^*=I$ 与 $B^*B+D^*D=I$，全部顺序保留。
不过真正 high inverse 含角阶损失，不能把其
$H^{s+1}\to H^s$ 结论代成一个免费有界 $L^2$ 的 $\|R\|$。
同样，原 strong low-tail 的标签权不能在 (D.35) 中抹掉。
实际高角表示与本篇原物理角 cutoff 之间的 commutator、
两侧外 Poisson 范数、原层权和 (D.33) 的 joint 列仍须一起付清。

本篇完成的是完整物理网络差及其新真实谱权下的中频压缩。
继续任务是消费 (D.35) 的两个真实外响应，并接回同一共同参数的
完整 ordinary/weak/joint source-to-label 方程，而非重复局部 PSD。
