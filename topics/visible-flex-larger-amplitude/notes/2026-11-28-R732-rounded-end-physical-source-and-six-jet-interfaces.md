# R732 圆肩参考的工作实现、冻结身份与实际费用

2026-11-28，Astra-larger-e4e2a2bf-20261126。此为完整源码交付，科学结果尚未返回。R732 定理适用于其准确参考。此处没有把工作积分或离散导数认证为定理中的准确量。

## 1. 实际数据与两条物理路径

同一份完整初始输入给出 R690 的 $S,R,a_{\rm deep}$、原 923 个 $s=aS+b$ 地址、原 Fejér 的 160 个模式字、材料角和初始高度 $H$。完整检查原 bundle、carrier、节点报告、scalar、准备报告和相应源字；验原核 $a=1,a_s=0,a_{ss}=k_0$。外层当前点的 core、$H$、1,333,212 个旋转变量都不决定这个冻结 seed。所有原外层自由度和正常积分仍须使用。

末端使用 $u=(1-a)S-b$。工作值使用原 $S$ 向外盒两端的准确有理中点，然后分别计算正向 $s$ 和反向 $u$，从而避免在靠帽的真地址先把 $s$ 舍入为 $S$ 再相减。求根及圆肩位置的工作值含舍入误差。阈值和材料归属取同一圆肩的工作 $L$。准确 $S$、准确 $L$ 的不确定性要在另一个准确消费者中覆盖。

$b=1/1000,d=7/50,h_T=13/50$。原 out 宽度和 $k_p$ 来自完整原标量的实际有理输入。对 $0<u\le2b$ 计算 R690 (3),(6) 的实际指数和导数，$u=0$ 取平坦极限。工作实现按 $x^{-4}$ 的十进制位数增加精度后作三角降角，以稳定恒等式计算深谷的 $1+\sin(x^{-4})$。它没有用有限个转向来定义输入。真正非零的角可在回到工作数时下溢为零；报告计数记录访问过的这种情况。此计数是查询数，不能代表连续尾的间隔证明。

到 $b$ 为原角；到 $2b$ 由 $(1-\chi)\beta+\int\chi'\beta+d^{-1}\int\chi$ 求角，由 $(1-\chi)\beta'+\chi/d$ 求曲率。其后为定曲率、宽 $b$ 的递减曲率、竖柱三段。实际求出 $A,u_c,u_f,x_f,h_f,L,R_v,Z$，摘要含工作字、全转弯和混合分区以及原函数前缀的身份。积分按各段切点和该段所有原材料结点切分，采用原径向/轮廓阶数的较大者；原外层整胞积分独立保留。不存在把原 R730 旧单位向量用于新末带的路径。

中央六 Bernstein 控制依次是 $\Gamma,\Gamma+\eta e_z,\Gamma+2\eta e_z+(5/4)k_0\eta^2\rho n,Q-2\eta e_z,Q-\eta e_z,Q$，其中 $\eta=1/512$。$Q=R_v e+Ze_z$。实际计算 $(\rho n)_\varphi=\rho' n+\rho t$ 和 $(\rho n)_{\varphi\varphi}=(\rho''-\rho)n+2\rho't$，而非用圆方向 $e(\Theta)$ 代换。整段用同一 $\psi=[1-(2t-1)^{12}]^7$，每个字面角以完整正 Gauss 求中央长度 $S-L$ 的唯一正根、根的两角导数以及逆弧长和两角导数。全部 922 个归一化中央积分胞、两原 Gauss 阶、128 附容差和 Armijo/backtrack 的长度根预算、64 次逆弧长预算都保留。每次实际使用的参数取自同一次完整启动。原报告、当前点、或不同来源的同坐标不提供本次根。

## 2. 两种函数的值

完整原消费者用 `RoundedEndUnitMeridianJet.evaluate(cells,local,phi)` 取 `T0,T0_s,T0_phi,T0_phiphi`。可调用 `evaluate_six_jets` 同时取 `F,F_s,F_phi,F_ss,F_sphi,F_phiphi`。中央和末端依真材料位置分别求值后按原行次序组装。带符号反射、相移、真实帽、outer 归一与约束属于既有各自消费者。这里的六 jets 是单半活动参考的工作求值，不是实际闭曲面的证书。

设 $V=G_t$, $v=|V|$, $T=V/v$, $\ell$ 为中央工作正前缀（含最后部分胞），$\Lambda$ 为当前角的总长，$C=S-L$。求逆所用 $\ell(t,\varphi)=s\Lambda/C$。工作长度求根仅达容差。解析链工作求值为
$$
t_\varphi=((s/C)\Lambda_\varphi-\ell_\varphi)/v,\quad
t_{\varphi\varphi}=((s/C)\Lambda_{\varphi\varphi}-\ell_{\varphi\varphi}
-2v_\varphi t_\varphi-v_t t_\varphi^2)/v .
$$
令 $q=\Lambda/C$；则 $F_s=qT$、$F_{ss}=qT_s$、$F_{s\varphi}=q_\varphi T+qT_\varphi$。$F_\varphi,G_{\varphi\varphi}$ 的复合求导均含 $t_\varphi,t_{\varphi\varphi}$。中央工作 $T_s$ 含 $q/v$。工作反解使用近似部分胞积分，工作解析链不是离散 quadrature 算法的逐条自动微分。准确构造中 $\Lambda=C$，其准确原函数单位速；工作归一、工作根残差与外层对工作单位切向的积分各自承担误差。工作构造在中央/竖柱边界的导数匹配不被冒充为准确等式。

末端 $r=R+x,z=H-h$，$T=-\cos\alpha\,e+\sin\alpha\,e_z$，$T_s=-\alpha'(\sin\alpha\,e+\cos\alpha\,e_z)$，$T_\varphi=-\cos\alpha\,e_\varphi$，$T_{\varphi\varphi}=-\cos\alpha\,e_{\varphi\varphi}$。六位置 jet 直接由同一 $P$ 给出；竖柱取准确的方向载体 $+\!e_z$。$r\ge R$ 并不替换原固定目标的 $a_{\rm deep}$。

## 3. 当前根、来源和未付边界

当前角根包记录实际完整控制、中央长度全角两 jet、正前缀/密度记录、root history、工作 bracket、工作总长及两导数以及相同 frozen-model 身份与圆肩积分身份。正常 science 和 pure 的上层消费者要按自己选中的 immutable normal snapshot 读取同次 seed model/root batch；不得从最新 progress 补缺。中央/末端接口本身不制造 normal packet 或证书。实际 missing outputs、晚失败、未访问角、未返点与原预算分别保留。

R732 已证同一准确参考的全部帽点双方 .126 法球、同圆肩端双方、原末带的三 Gram、闭嵌入及强 $C^2$ 全相位、$D\le4.2$、双 held $>.91$、$\delta_E>0$。参考中央与非原圆肩的目标 Gram、中央/中央与中央/圆肩 reach 未付。新外场仍需在全部原域、所有 32 阶段及全相位验证同一 $g$、真实 $D$、held、reach、$\delta_E$ 和闭合，支付真精化与多时刻网格。准确末带只属于冻结参考；末端开集的原 outer 旋转变量可以改变实际场。源没有增加正宽固定约束。也没有使用只有存在宽度的 R733 内领口，或把本后继当成 run34 的物理源。

本次只编辑完整源文本、说明、清单和核对相应字节哈希。没有在本地执行 Python、积分、AST、fixture、优化、J 或准确费用。本交付时 run/source/model/point、末端工作积分字、中央长度根、normal/几何结果均未实际返回。
