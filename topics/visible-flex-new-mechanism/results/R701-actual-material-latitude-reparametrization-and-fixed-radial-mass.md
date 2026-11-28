# R701　实际材料纬圈的可逆重标与冻结径向度量的单标量消元

[R698](R698-two-component-latitude-curl-with-the-actual-signed-binormal-speed.md) 用单位切向 $T$ 与有符号副法向速度消去一条闭性方程。以下从真实 [R680](R680-smaller-tilt-offset-cap-and-positive-hoop-curvature-phase-input.md) 角和实际 [R687](R687-global-darboux-frames-with-quantitative-periodic-immersion-reconstruction.md) 候选出发，在设计阶段将三项虚拟度量全都准确满足。在已冻结的径向度量上，当一个严格质量区间通过时，同样只剩两条真实闭性方程。最终的实际浸入仍须由闭性、真实两阶导数、刚姿和整壳检验取得。

## 1　材料角由严格单调的两个积分确定

以 $\varphi$ 为固定材料角，$\psi$ 为辅助球面曲线参数。设 $T(r,\psi)$ 是单位向量，$v=|T_\psi|>0$，$U=T_\psi/v,B=T\times U$。取有符号光滑坡 $b$，写
$$
 c=(1+b^2)^{-1/2},\qquad s=bc,\qquad W=vc .
$$
所需尺度分解为 $e=m(r)e_0(r,\varphi)>0$，其中基函数 $e_0$ 在该设计阶段给定。令
$$
 P(r,\varphi)=\int_0^\varphi e_0(r,x)^{-1}\,dx,\quad A(r,\psi)=\int_0^\psi W(r,y)\,dy,
 \quad m=P(r,2\pi)/A(r,2\pi).
$$
唯一的 $\varphi=\Phi(r,\psi)$ 由 $P(r,\Phi)=mA(r,\psi)$ 确定，$\Phi(r,0)=0$，$\Phi(r,2\pi)=2\pi$，$J=\Phi_\psi=eW>0$，且 $\Phi(\psi+2\pi)=\Phi(\psi)+2\pi$。定义 $D=e(-cU+sB)$。于同一实际材料点准确地有
$$
 |T|=1,\quad D\cdot T=0,\quad |D|^2=e^2,\quad D\cdot T_\varphi=-1 .        \tag{1}
$$
尤其在 $e_0=1$ 时 $E=m^2$ 已经严格径向。若 $T(r,-\psi)=-S T(r,\psi), S=\operatorname{diag}(1,-1,1)$，$b,e_0$ 是偶函数，则 $\Phi$ 为奇的圆映射，两条反射材料母线保持原标签。$\Phi$ 的角零点是固定材料相位基准，不能任意每圈再加相位而不付径向导数。

R680 真锚 $T=Qe_\psi$、$v=1$、$b=-p(1.01+\cos\psi)$。取 $e_0=\sqrt{1+b^2}$，两个积分逐点相同，故 $m=1,\Phi=\psi$，$D=Qe_r+bQe_z$，准确复现原浸入与一般非旋转度量。可以把 $\log e_0$ 的已给角向部分连续推至零；仅在 $e_0$ 成为径向之后才使用旋转材料相位族。

## 2　完整闭性、两阶径向导数及真实内帽

以下未加标志的 $r$ 偏导在辅助参数 $\psi$ 固定时取。实际材料导数为
$$
 \partial_\varphi=J^{-1}\partial_\psi,\qquad
 L=\left.\partial_r\right|_\varphi=\partial_r-\gamma\partial_\psi,
 \qquad \gamma=\Phi_r/J .
$$
由积分隐式可直接求
$$
 \Phi_r=e_0(m'A+m A_r-P_r),\quad
 \Phi_{rr}=e_0(m''A+2m'A_r+mA_{rr}-P_{rr}-2P_{r\varphi}\Phi_r-P_{\varphi\varphi}\Phi_r^2).
$$
右侧 $P$ 各项及 $e_0$ 只在实际 $\varphi=\Phi$ 取值。特别地
$$
 L^2T=T_{rr}-2\gamma T_{r\psi}+\gamma^2 T_{\psi\psi}+(\gamma\gamma_\psi-\gamma_r)T_\psi .
$$
两条实际方程就是下式在 $U,B$ 方向的投影为零，
$$
 \widetilde G=D_\psi-JT-r(J T_r-\Phi_rT_\psi),\qquad
 G=\widetilde G/J=D_\varphi-T-r LT .                                     \tag{2}
$$
$(D_\psi)\cdot T=J$，故对所有试场 $\widetilde G\cdot T=0$，余下两行等价于整向量。直接取消 $\Phi_rT_\psi$ 会改变原材料方程。

记 $\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}fJ\,d\psi$。从 $0$ 到 $\psi$ 对 $(f-\langle f\rangle)J$ 积分，再减去该原函数的加权均值，所得 $I_\varphi f$ 正是材料角的零均值原函数。取
$$
 C(r)=\int_{r_1}^r\langle D\rangle\,dr,\quad F=C+r I_\varphi T .
$$
有 $F_r-D=-I_\varphi G$，$F_\varphi/r-T=-\langle T\rangle$，从外圈积分得 $r\langle T\rangle=\int_r^{r_1}\langle G\rangle\,ds$。也可把 (2) 按 $\psi$ 全圈积分，$\Phi_r$ 两端为零，分部积分给完全相同的均值方程。其连续闭性范数是 $\overline{|G|^2}=(2\pi)^{-1}\int|\widetilde G|^2/J\,d\psi$。由于 (1)，R698 的全域相对误差界现为 $2L_0+L_0^2$，$L_0$ 取该文以此真实闭性范数和正 $\inf e$ 定义的量。

重心第二导数是 $(2\pi)^{-1}\int (D_rJ+DJ_r)\,d\psi$。实际两阶列仍为
$$
 F_{rr}=C''+2I_\varphi LT+rI_\varphi L^2T,\quad
 F_{r\varphi}=(1-\langle\cdot\rangle)(T+rLT),\quad F_{\varphi\varphi}=rT_\psi/J .   \tag{3}
$$
真实外平圈与内倾平圈需要 $\Phi=\psi$, $\Phi_r=\Phi_{rr}=0$, $T=Qe_\psi,T_r=T_{rr}=0$ 于两端。一个充分输入是各端 $b=b_r=0$、$e_0$ 的角向非恒定部分至二阶径向 jet 为零，且 $T$ 有上述平圈 jets 和相应混合角导数。此时 $A_\psi$ 的两阶径向变化亦为零，$e_0$ 中共同的纯径向尺度被 $m$ 抵消；微分 $P(\Phi)=mA$ 即得要求。$D=Qe_r,D_r=0$，(3) 因而准确给平圈二阶接合。内中心是实际积分 $C(r_0)$。非线性求解期间，直径、两轴投影、真帽支撑、法管和长度预算都须使用这个中心及 (3)。同一径向 $E$ 的不同材料相位要求在 $\varphi-\alpha$ 处求逆 $\Psi(r,\varphi-\alpha)$ 后施原刚姿；直接把 $\psi$ 移 $\alpha$ 一般作用在不同材料上。

## 3　冻结 $E_*$ 后的可行域和单标量真实根

先置 $e_0=1$，给定已冻结的正 $e_*(r)=\sqrt{E_*(r)}$。把当前真实有符号坡写为 $b=\sqrt z\,b_0(r,\psi)$，其中 $z(r)>0$。要求
$$
 M_r(z)=\int_0^{2\pi}\frac{v}{\sqrt{1+z b_0^2}}\,d\psi
       =2\pi/e_*(r)=:P_*(r).                                               \tag{4}
$$
$b_0$ 不恒零时 $M_r$ 严格递减，其导数为 $-\frac12\int v b_0^2(1+zb_0^2)^{-3/2}$。由单调或有界收敛定理，其在 $(0,\infty)$ 的全值域准确为
$$
 \int_{\{b_0=0\}}v\,d\psi<P_*<\int v\,d\psi .                          \tag{5}
$$
两边严格当且仅当存在唯一有限正 $z$。该式允许 $b_0$ 穿零或在弧段恒零。$b_0$ 处处为零时仅可能 $P_*=\int v$，尺度不可辨识，此处须单独做退化处理。未解场不预设 (5)；可用公开计算的有出处单元界验证一对明确的正数根括区 $M(z_-) >P_*>M(z_+)$，这也足以关闭严格内域门。跨 $r$ 的固定 $E$ 求解应保存根、括区和导数余量，不把离散成功当全环已证。在该门成立处，(4) 令 $m=e_*$；于是 (1) 的完整虚拟度量在每个试态都是真正同一冻结目标。物理 $F$ 仍由 (2) 的两行决定。

两端平圈不能裸除消失的质量导数。令 $h$ 为到某一真平圈的材料径向距离，$\beta(r)>0$ 为内部真实坡幅，$\beta=h^2\beta_1(h)$，$\beta_1(0)>0$，置 $b_0=\beta s_0$。稳定的端式为
$$
 \frac{\int v\,d\psi-P_*}{\beta^2}
 = z\int_0^{2\pi}\frac{v s_0^2}{\sqrt{1+z\beta^2s_0^2}\,[1+\sqrt{1+z\beta^2s_0^2}]}\,d\psi .       \tag{6}
$$
若左侧有正的足够光滑单侧延拓，$s_0$ 也有相应单侧正则性且在端点不恒零，右侧于 $h=0$ 是 $z\int v s_0^2/2$，导数正。隐函数定理在准确端点给出唯一有限正根及其光滑延拓。只知点值有界没有这个导数结论。

一类足够的实际端部数据可直接从冻结设计验证。设冻结时 $v_*,s_*$ 真已储存或可从原场恢复，$P_*=\int v_*/\sqrt{1+\beta^2s_*^2}$。当前与原切向均可写成同一端姿的大圆 $T_c=Q(r)e_\psi$ 加角 $C^1$ 范数为 $O(h^3)$ 的场。若 $T=T_c+V$, 则
$$
 \int T_{c,\psi}\cdot V_\psi=\int T_c\cdot V=-\tfrac12\int|V|^2,
 \qquad \int|T_\psi|-2\pi=O(h^6).
$$
这里第一式只用周期性、$T_{c,\psi\psi}=-T_c$ 及 $|T|=|T_c|=1$；对模长在单位向量的一阶展开给第二式。于是 $(\int v-\int v_*)/\beta^2=O(h^2)$，(6) 左侧端极限为准确的 $\int s_*^2/2$。对实际端结内单侧解析的曲线、样条和坡，分子有至少四阶零，商有单侧解析延拓；若输入只具有限光滑性，则须另证所需商导数。R680 的 $\beta=k$ 可用，$s_*= -p(1.01+\cos\psi)/k$ 两端均不恒零。对后续冻结态必须在该态自身检查这个条件，不能仅援引 R680 的端极限。特别是原 R687 的独立径向样条只在端去两列，一般可以出现二次端项；其任意候选或所冻 $E$ 都不因此获得四阶质量差。不得由一次数值近零或只由去列个数开 (6) 的端门。

## 4　原实际未解场的准确转换成本

从自然完成 R687 的真实 $T_*,e_*P_*,C_*'$ 读取，依 R698 取 $D_{\rm pr}=e_*P_*+H$，$H=(G_*\cdot T_*)U/v$，$a_{\rm pr}=D_{\rm pr}\cdot B$。设 $b_{\rm in}=a_{\rm pr}v$，$e_{0,\rm in}=|D_{\rm pr}|$，以原材料角作为辅助 $\psi$。此时 $1/e_{0,\rm in}=v/\sqrt{1+b_{\rm in}^2}$，故第 1 节给 $m=1,\Phi=\psi$，$D=D_{\rm pr}$。准确保留整个原 $T_*$ 及完整有符号坡；初始虚拟目标相对原径向平方长改变 $2(e_*P_*)\cdot H+|H|^2$，实际位置的径向重心差由 R698 (7) 给出。未满足旧方程时这两个成本通常非零。初始 $e_{0,\rm in}$ 并非自动相同的冻结 $E_*$。如原态已冻结，真正的同 $E_*$ 推进应直接检查 (4)–(5)，或在明确的设计阶段结束后对固定原函数另行精化。

原真坡 $p=-Mk$ 在两个内部匀速转接点只具 $C^1$ 正则性。R687 的 $T_*$ 未受其最后绕 $T$ 的转动影响，仍为 $C^2$；一般 $b_{\rm in}$ 却含 $p$。在 $\Phi=\psi$ 的准确起点，$C'$ 只需有连续一阶，故原两阶浸入并无缺口。进入非恒等材料重标后，(3) 另需要足够连续的 $\Phi_{rr}$；分段二阶有界不能自动消除两个转接的材料二阶跳跃。后继必须证明该跳跃在真实浸入抵消，或采用明确的 $C^2$ 辅助坡并支付改变的径向列、重心、目标和二阶物理数据。可在原 $T_*,Q$ 不变时，仅为 $b_{\rm in}=(e_*P_*)\cdot(T_*\times (T_*)_\psi)$ 同时替换 $e_*$ 标量与 $P_*$ 最后转动中的 $p$；二者应使用同一个新 $p$。新的未知坡也应使用同样的 $C^2$ 端幅，实际改量归入 R703 真实输入。

在固定目标下按 (4) 改坡和重标后，立足同一实际材料角 $\varphi$，准确位置改变是
$$
 F_{\rm new}-F_{\rm old}
  =\int_{r_1}^r (\langle D_{\rm new}\rangle-C_{\rm old}')\,ds
    +r I_\varphi[T_*(r,\Psi(r,\varphi))-T_*(r,\varphi)] .              \tag{7}
$$
因此连角参数的改变也会改变当前材料点的物理像。若还改球面切向，就须在第一个 $T_*$ 项换为真实新 $T$。这些改变与原两网/全列费用分列，新物理硬门必须复算。

## 5　准确参数自由和完整新导数

辅助圆本身的保向重标 $\psi\mapsto h(r,\psi)$（固定角零点、保反射）只同时重标球曲线和坡，诱导的材料函数不变。这一自由可在正则 $T_*$ 的邻域用球面曲线的法图消去，$T=\cos f\,T_*+\sin f\,B_*$，$f$ 为奇角函数，坡为一张独立偶角函数。给任意充分接近的球面浸入，可逐原参数解其对 $U_*$ 的位移为零来重标；在原场的导数 $T_{*,\psi}\cdot U_*=v_*>0$ 给唯一近恒等的解。紧性保持其圆微分同胚性。球面曲线允许自交，取的仍是同一参数点附近的分支；反射在两固定标签处对应的球切向准确为 $\pm e_y$，故重标固定零点。这个局部选择消除切向参数形变，未删除任何非零的物理法向形变。实际每个本地指数图均须保持正则，过大变化可在已接受态重新立图。

在固定目标的 (4) 中，$b_0\mapsto c(r)b_0,z\mapsto z/c^2$ 还有一项纯正标量自由。只在这个固定阶段、且所用角矩不为零时固定一个坡角矩。例如 $\int s_*\ne0$ 时保持 $\int s_0=\int s_*$，展开全部其余偶角模式。若该均值过零，可以使用光滑权重 $s_*$，保持 $\int s_0s_*=\int s_*^2>0$，把新场的局部正尺度唯一规定下来。设置独立坐标或精确一个线性约束；不能把原完整矩阵中的小非零奇异方向按阈值截去。设计阶段坡的尺度会真实改变 $E$，应保留。

对任意新参数方向，$\delta v=U\cdot\delta T_\psi$，$\delta U=(\delta T_\psi-U\delta v)/v$，$\delta B=\delta T\times U+T\times\delta U$。设计阶段 $\delta\log m=\delta P(2\pi)/P(2\pi)-\delta A(2\pi)/A(2\pi)$，在固定辅助点有
$$
 \delta\Phi=e_0[\delta m A+m\,\delta A-\delta P|_\varphi] .
$$
固定目标时对 (4) 取隐微分；其自由方向的偏导为
$$
 \int\!\left[\frac{\delta v}{\sqrt{1+zb_0^2}}-
 \frac{zv b_0\delta b_0}{(1+zb_0^2)^{3/2}}\right]d\psi-\delta P_*,
$$
取其相反数除 $M_r'(z)$ 即得 $\delta z$，端点改微分 (6)。$\delta J,\delta D,\delta\Phi_r$ 连同每一项进入 (2)，两投影各自还含 $\delta U\cdot\widetilde G,\delta B\cdot\widetilde G$。新全 Jacobian、所有独立列、真实求根和工作/独立网费用都须重新记录；旧场的参数与已付校准可转入，旧 Jacobian 不是这个算子的 Jacobian。本篇未调用运行中的任何结果、未认证 R687 的实际质量门或任何有限根。
