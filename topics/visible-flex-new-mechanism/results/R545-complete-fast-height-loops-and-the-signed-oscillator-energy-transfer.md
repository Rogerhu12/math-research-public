# R545：完整快高度回路、振子能量的有号转移与真实有限端点接口

日期：2026-11-16。**完整原式与有限维 ODE 的纸面证明；没有执行数值、符号、profile、秩或开发计算。**

本文继续 R543 的同规范离叶问题。首先在 R541 的原稳定起点证明：一个小幅快高度闭回路，从零快振子能量出发时，其水平记忆的二阶项非负；若把振子完整送回，则这一阶恰为零。该结论不决定三阶及更高项，也不排除从起点另选 Gram、使真实起点带有非零相对势能的构造。

证明保留完整第二与第三历史。它们在快方程中都有原尺寸，不能先删掉；只是它们在小幅参数的一阶变分中没有一次项，所以二阶水平记忆可由一阶振子准确读取。本文还支付一个两条真紧高度 bump 的实际端点 IFT，以及进入段的原矩与第三历史成本。最后给非零初能量的同一接口，供另一次从起点固定规范的完整构造使用，不拼接两条不同 $\chi$。

## 1. 固定数据、快时钟和允许参数次序

采用 R521 的同一正交母、原物理窗口、右锚和第二规范 $w=0$。在
$$
S_c=(H,0,\omega_c),\qquad H\min_I(x+\omega_c)>1
$$
处记
$$
c=C_k(S_c)>0,\qquad B_*=-C_h(S_c)>0,\qquad
F_c=\mathcal F(S_c,0,0,0,0).
\tag{1}
$$
R541/R543 的固定 Gram 为
$$
\nu^\delta=
\left(-H^2\lambda/\delta^2+2HF_c,\;
2c/\delta^2,\;\lambda/\delta^2\right).
\tag{2}
$$
在原从起点选择 $\lambda>0$ 时，再要求
$$
0<\lambda<B_*.
\tag{3}
$$
该额外条件与 R541 的合法窗口条件同时可满足。最终每条实际路径只用一条(2)的 $\chi^\delta$，不是沿回路改变 Gram。

定义
$$
\eta=\omega-\omega_c,\quad d=h\eta-k,\quad
j=\frac{\eta}{h}+\frac d{h^2}.
$$
原身份为
$$
\eta_s=\frac{k_s}{2h},\qquad
j_s=-\frac{2dh_s}{h^3},\qquad
k=h^2j-2d.
\tag{4}
$$
固定有限快时间 $T>0$ 和 $f\in C_c^\infty((0,T))$。取幅度 $\varepsilon>0$，先固定任意有限 $\zeta>0$，然后规定
$$
\boxed{
\delta=\zeta\varepsilon,\qquad
s=\delta\tau,\qquad
h(s)=H+\varepsilon f(\tau),\quad 0\le\tau\le T.
}
\tag{5}
$$
高度在两个开放端段准确为 $H$，全部高度 jets 都匹配。物理总时长是 $\delta T$。真实起点为
$$
k=\eta=h_s=k_s=0,\qquad A=T_{\rm third}=0.
\tag{6}
$$
下文用 $\mathsf T$ 表示缩放第三状态，避免与固定快时长 $T$ 混淆。

(5)是一份明确的有限参数联动，不是把“先固定幅度、再令时长任意趋零”的全部成本藏起来。第 7 节另写出一般时长下的原速度平方成本。

## 2. 保留全部历史后的正规快系统

在本节令
$$
\Gamma=h_\tau,\qquad V=k_\tau,\qquad
\mathsf A=\delta A,\qquad
\mathsf T=\delta^2T_{\rm third}.
\tag{7}
$$
R73 的完整矩密度只含几何项和速度二次项，故可准确写成
$$
\Phi_{M_{\rm raw}(S,\gamma,\upsilon)}
=\mathcal M_0(S)+\mathcal M_2(S;\gamma,\upsilon),
\tag{8}
$$
其中 $\mathcal M_2$ 对两个速度齐次二次。没有删掉其中的原五条速度成本。

原第四 ruling 的无加速度部分为
$$
\mathcal F
=R_0+R_2+L_{\rm vel}(A\Delta)
-E(A\Delta,A\Delta)
-4E\{\phi,T_{\rm third}(\phi;\Delta)\}.
\tag{9}
$$
这里按 R521 在一个固定相位读出原标量；$\phi,\Delta$ 是原第一与二次 profile 输入，随后全相位由同一 $\sin^2\theta$ 身份恢复。$R_2$ 对速度二次，$L_{\rm vel}$ 对速度一次。

把完整方程乘以 $\delta^2$，得到
$$
\boxed{
C_h\Gamma_\tau+C_kV_\tau+\mathcal F_\delta
-\Psi(h,d)-\delta^2\frac{HF_c(1+d^2)}h=0,
}
\tag{10}
$$
其中
$$
\Psi(h,d)=-\frac{H^2\lambda(1+d^2)}{2h}
+2cd+\frac{\lambda h}{2},
$$
$$
\begin{aligned}
\mathcal F_\delta={}&
\delta^2R_0(S)+R_2(S;\Gamma,V)
+L_{\rm vel}(S;\Gamma,V)(\mathsf A\Delta)\\
&-E_S(\mathsf A\Delta,\mathsf A\Delta)
-4E_S\{\phi,\mathsf T(\phi;\Delta)\}.
\end{aligned}
\tag{11}
$$
这仍是完整原 ruling，不是无历史势振子。

第二历史的准确快方程为
$$
\boxed{
\mathsf A_\tau
=\delta^2\mathcal M_0(S)+\mathcal M_2(S;\Gamma,V).
}
\tag{12}
$$
按 R77 的原权三身份，第三历史满足
$$
\begin{aligned}
\mathsf T_\tau={}&
-\{\delta^2\mathcal M_0+\mathcal M_2\}\circ\mathsf A
+\delta^2\mathcal C^{[1]}(S;\Gamma,V)\\
&+\partial_\tau P_{\rm acc}(S;\Gamma,V)
+\mathcal A(S)(V\Gamma_\tau-\Gamma V_\tau)\\
&+\sum_{r=0}^3\mathcal B_r(S)\Gamma^{3-r}V^r .
\end{aligned}
\tag{13}
$$
$P_{\rm acc}$ 为原速度二次势。式(13)保留完整有序复合、速度面积、三次速度及端势；没有投到 $W$ 后删除项。

因为 $C_k>0$，(10)给 $V_\tau$ 的光滑显式图。将其代入(13)中原 $P_{\rm acc}$ 的链式导数后，连同
$$
k_\tau=V,\qquad \eta_\tau=V/(2h),\qquad
\Gamma=\varepsilon f',\quad \Gamma_\tau=\varepsilon f''
\tag{14}
$$
组成普通有限维光滑 ODE。不存在未解的第三导数或隐含的独立第三控制。

代入(5)后，这套方程在 $\varepsilon=0$ 正规延拓，零参数解为常 $S_c$、零快速度与零 $\mathsf A,\mathsf T$。固定有限 $T$ 上的普通连续依赖给：充分小的每个有限正 $\varepsilon$ 都有整个快区间上的真实解，保同一合法窗口，且
$$
S-S_c=O(\varepsilon),\quad
\Gamma,V=O(\varepsilon),\quad
\mathsf A=O(\varepsilon^2),\quad
\mathsf T=O(\varepsilon^2).
\tag{15}
$$
最后两个阶数直接由(12)(13)取得：$\delta^2=O(\varepsilon^2)$，面积与速度势从二次幅度开始；三次速度、有序交叉等仍保留在更高阶。

对于最终 $\delta>0$，真实原历史是
$$
A=\mathsf A/\delta,\qquad
T_{\rm third}=\mathsf T/\delta^2,
$$
因此在(5)下
$$
\boxed{A=O(\varepsilon),\qquad T_{\rm third}=O(1).}
\tag{16}
$$
$\mathsf T=O(\varepsilon^2)$ 绝不表示真实第三历史可删。

## 3. 完整一阶振子必须保留固定 $\lambda$

由光滑参数依赖，写
$$
d=\varepsilon D+O(\varepsilon^2).
\tag{17}
$$
原(4)给 $j=O(\varepsilon^2)$，所以
$$
k=-2\varepsilon D+O(\varepsilon^2),\qquad
\eta=-\varepsilon D/H+O(\varepsilon^2).
\tag{18}
$$
在(10)取一阶：$C_h(S_c)=-B_*$、$C_k(S_c)=c$，而
$$
\Psi_h(H,0)=\lambda,\qquad \Psi_d(H,0)=2c.
$$
(11)的速度与历史项没有一次幅度贡献，但它们在实际方程中始终存在。因此
$$
\boxed{
D''+D=-\beta f''-\alpha f,\qquad
D(0)=D'(0)=0,
}
\tag{19}
$$
其中撇号只表示快时间 $\tau$ 导数，且
$$
\beta=\frac{B_*}{2c},\qquad
\alpha=\frac{\lambda}{2c},\qquad
\sigma=\beta-\alpha>0.
\tag{20}
$$
若 $\lambda$ 已先固定，不能把 $-\alpha f$ 擅自降到更高阶。

定义
$$
g=D+\beta f.
$$
因 $f$ 在初始开放区间为零，
$$
\boxed{
g''+g=\sigma f,\qquad g(0)=g'(0)=0.
}
\tag{21}
$$
这是一阶变分方程，不是对完整(10)–(13)的替换。

## 4. 闭高度的二阶记忆由振子能量准确决定

设
$$
\mathcal E(\tau)=\frac12\{g'(\tau)^2+g(\tau)^2\}.
$$
由(21)，
$$
\mathcal E'=\sigma f g'.
$$
因为 $f(0)=f(T)=0$，准确分部积分给
$$
\boxed{
\int_0^T Df'\,d\tau
=\int_0^T gf'\,d\tau
=-\frac{\mathcal E(T)-\mathcal E(0)}{\sigma}.
}
\tag{22}
$$
第一步用 $\int ff'=0$，第二步保留了真实端条件，不假设 $g$ 自己返回。

R543 定义的记忆为 $\rho=j-J(h)$。高度闭合到 $H$，所以本段末 $\rho=j$。用原水平积分而非振子方程来恢复它：
$$
\rho_{\rm out}
=-2\int_0^T\frac{d\,h_\tau}{h^3}\,d\tau
=-\frac{2\varepsilon^2}{H^3}\int_0^T Df'\,d\tau
+O(\varepsilon^3).
$$
于是
$$
\boxed{
\rho_{\rm out}
=\frac{2\varepsilon^2}{\sigma H^3}\mathcal E(T)
+O(\varepsilon^3).
}
\tag{23}
$$

因此：

- 若固定的非零一阶回路留下 $\mathcal E(T)>0$，则充分小的实际正 $\varepsilon$ 给 $\rho_{\rm out}>0$；
- 若一阶振子完整返回 $g(T)=g'(T)=0$，则只得到 $\rho_{\rm out}=O(\varepsilon^3)$，二阶系数恰为零；
- 不能从第二种情形推断真实 $\rho$ 精确为零，亦不能推断三阶项的号。

这是 R541 原零能量入口的局部快回路结论。它不排除 R543 所列的大幅离叶、参数相关长词、更高阶效应或非零真实入能。对 $h>H$ 的另一条负 $p_1$ 叶需要负 $\rho$；简单零能量快回路没有在二阶提供它。

## 5. 两个真紧高度 bump 给完整实际端点 IFT

只讨论线性 endpoint 是否可控时，也必须保持高度自身的全部端 germs。取两个
$$
b_1,b_2\in C_c^\infty((0,T))
$$
并令 $f=f_0+\theta_1b_1+\theta_2b_2$。由(21)，控制到末端 $(g(T),g'(T))$ 的两列为
$$
\sigma
\begin{pmatrix}
\int_0^T\sin(T-\tau)b_i(\tau)\,d\tau\\
\int_0^T\cos(T-\tau)b_i(\tau)\,d\tau
\end{pmatrix},
\qquad i=1,2.
\tag{24}
$$
先选两个内部中心 $\tau_1,\tau_2$，使
$$
\tau_2-\tau_1\notin\pi\mathbb Z.
$$
再在各中心选择足够窄的非负光滑 bump、令其积分为1。(24)的行列式连续趋于非零的两个正弦余弦向量行列式，故在某个有限正宽度即严格非零。只作这一次有限选择，不使用分布或数值秩证据。

因此可以对任意固定 $f_0$ 解唯一两个线性参数，使一阶
$$
D(T)=D'(T)=0.
\tag{25}
$$
若要求回路非平凡，可先把 $f_0$ 选在 $\operatorname{span}\{b_1,b_2\}$ 外。

现在回到完整(10)–(14)。在联动 $\delta=\zeta\varepsilon$ 下，实际末端映射
$$
\left(\frac{d(T)}{\varepsilon},
      \frac{d_\tau(T)}{\varepsilon}\right)
\tag{26}
$$
在 $\varepsilon=0$ 有光滑可去延拓，其值就是(19)的 $(D(T),D'(T))$，参数 Jacobian 为(24)。普通有限参数 IFT 给
$$
\theta=\theta(\varepsilon,\zeta)
$$
于固定 $\zeta>0$ 的一个邻域，并使真实末端准确满足
$$
\boxed{d(T)=0,\qquad d_\tau(T)=0,\qquad d_s(T)=0.}
\tag{27}
$$
全部高度 jets 由共同紧支撑自动闭合。这是真实完整 ruling 的有限端点右逆，保同一个 $\chi^\delta$ 与全部原 history；未执行任何秩计算。

(27)只支付列出的两个末端值。原 $k,\eta$ 可以有 $O(\varepsilon^3)$ 的水平漂移，全部更高 scalar jets 由完整反馈给出，第二与第三历史没有清零。特别，不能把(27)改写成一个开放常 scalar germ 或全端口返回。

对这条真实 IFT 回路，(23)仅给
$$
\rho_{\rm out}=O(\varepsilon^3),
$$
未定其号。

## 6. 第三历史与能量转移不能分开处理

R77 的原速度面积给一个可直接核对的二阶收据。在本次起点，
$$
\Gamma=\varepsilon f'+O(\varepsilon^2),\qquad
V=-2\varepsilon D'+O(\varepsilon^2).
$$
于是
$$
\int_0^T(V\Gamma_\tau-\Gamma V_\tau)\,d\tau
=-4\varepsilon^2\int_0^T D'f''\,d\tau
+O(\varepsilon^3).
\tag{28}
$$
这里用到 $f'$ 在两端为零。

由 $g=D+\beta f$ 及(21)，再一次真实 IBP 得
$$
\int_0^T D'f''\,d\tau
=-\int_0^T g''f'\,d\tau
=\int_0^T gf'\,d\tau
=\int_0^T Df'\,d\tau.
\tag{29}
$$
因此面积项的完整二阶贡献为
$$
\boxed{
\frac{4\varepsilon^2}{\sigma}
\{\mathcal E(T)-\mathcal E(0)\}\,\mathcal A(S_c).
}
\tag{30}
$$
若末快速度 $D'(T)$ 非零，还必须加上原
$$
\varepsilon^2P_{\rm acc}(S_c;0,-2D'(T))
$$
端值；不能因高度平坦而把它删掉。

在(25)(27)的一阶完整振子返回中，(30)与一阶速度端势均为零，所以
$$
\mathsf T_{\rm out}=O(\varepsilon^3),\qquad
T_{{\rm third,out}}=O(\varepsilon)
\quad\text{当 }\delta=\zeta\varepsilon.
\tag{31}
$$
但完整第二历史一般仍为 $A_{\rm out}=O(\varepsilon)$，没有因振子返回而成为零。式(30)也不主张某个具体 $\mathcal A$ 投影必非零；它要求保留原完整算子，若有额外消去只能另按原 profile 身份支付。

## 7. 原两个矩的真实进入成本

原 R73/R543 给
$$
p_1^{\omega_c}=-kd,\qquad
8t_1^{\omega_c}=k^2+2kd-1-(h_s/h)^2.
$$
由(17)(18)，对固定非平凡 $f$，
$$
\int_0^{\delta T}p_1^{\omega_c}\,ds
=2\delta\varepsilon^2\int_0^T D^2\,d\tau
+O(\delta\varepsilon^3).
\tag{32}
$$
若 $D\equiv0$，(19)与紧支撑条件使 $f\equiv0$；故非平凡回路的(32)在充分小参数时严格正。包括实际 IFT 回路在内，其进入段没有免费产生负总 $p_1$。

对 $t_1$，保留原速度项得到准确式
$$
\begin{aligned}
\int_0^{\delta T}t_1^{\omega_c}\,ds
={}&\frac{\delta}{8}\int_0^T(k^2+2kd-1)\,d\tau\\
&-\frac{\varepsilon^2}{8\delta}
\int_0^T\frac{f'(\tau)^2}{(H+\varepsilon f(\tau))^2}\,d\tau.
\end{aligned}
\tag{33}
$$
因此在本稿实际联动 $\delta=\zeta\varepsilon$ 下，
$$
\boxed{
\int_0^{\delta T}t_1^{\omega_c}\,ds
=-\varepsilon\left\{
\frac{\zeta T}{8}
+\frac{1}{8\zeta H^2}\int_0^T f'^2\,d\tau
\right\}+O(\varepsilon^2)<0.
}
\tag{34}
$$
若另采用固定幅度后令 $\delta\to0$ 的次序，(33)显示速度平方成本一般按 $\varepsilon^2/\delta$ 增长。不能以某个未联动的固定正尾长自动压过它。

(32)(34)说明快时钟是一个有真实矩成本的入口工具，不是可任意加在已完成零矩词中的免费边。

## 8. 非零真实初能量的接口：零能量结论不适用

以下是另一个明示条件的有限端点接口。设一份**从起点一次固定**的完整 Gram 族，在与第 2 节相同的正规快系统及零原历史起点下，一阶方程为
$$
D''+D=a_0-\beta f'',\qquad
D(0)=D'(0)=0,\qquad a_0>0.
\tag{35}
$$
这可能来自原起点不在主导稳定支上；它不是在既有路径末端任意指定一个新的振子入能。

定义
$$
g=D+\beta f-a_0,\qquad
g''+g=\beta f,\qquad
g(0)=-a_0,\quad g'(0)=0.
\tag{36}
$$
因此真实初始相对能量为
$$
\mathcal E(0)=a_0^2/2.
$$
对闭高度控制，(22)准确改为
$$
\int_0^T Df'\,d\tau
=-\frac{\mathcal E(T)-\mathcal E(0)}{\beta}.
\tag{37}
$$
第 5 节的两个内部 bump 仍给可逆端点矩阵，只将 $\sigma$ 换成 $\beta$。可以使一阶
$$
g(T)=g'(T)=0,\qquad D(T)=a_0,\quad D'(T)=0.
\tag{38}
$$
于是原水平记忆的二阶项为
$$
\boxed{
j_{\rm out}
=-\frac{\varepsilon^2a_0^2}{\beta H^3}
+O(\varepsilon^3)<0.
}
\tag{39}
$$

若该完整族的目标稳定根 $q_\varepsilon(H)$ 对参数光滑、满足
$$
q_\varepsilon(H)=\varepsilon a_0+O(\varepsilon^2),
$$
则在 $\delta=\zeta\varepsilon$ 下，对真实残差
$$
\left(
\frac{d(T)-q_\varepsilon(H)}{\varepsilon},
\frac{d_\tau(T)}{\varepsilon}
\right)
$$
应用同一个 IFT，即得到准确末端
$$
\boxed{
d(T)=q_\varepsilon(H),\qquad d_s(T)=0,
}
\tag{40}
$$
并保(39)。这只要求完整快族已经按第 2 节正规化，不要求重设 $A,T_{\rm third}$。

此时速度端势的一阶端值为零，但(30)成为
$$
\boxed{
\mathsf T_{\rm out}
=-\frac{2\varepsilon^2a_0^2}{\beta}\mathcal A(S_c)
+O(\varepsilon^3).
}
\tag{41}
$$
在 $\delta=\zeta\varepsilon$ 下，真实 $A=O(\varepsilon)$、真实第三历史为一般非零的 $O(1)$。这些末值必须进入任何后续慢段。负 $j_{\rm out}$ 与这一完整速度面积来自同一真实积分，不能只保前者。

(35)–(41)没有证明任何一条指定新 Gram 族已经满足全部后继稳定跟踪、足够负总矩或正总矩；那些必须由该族本身继续支付。特别不能把本节的非零入能附加到(2)的零能量起点后，仍声称它们是同一已冻结规范。

## 9. 已证明的范围与真正剩余入口

本文已支付：

1. 包含全部原 $A,T_{\rm third}$ 的正规快系统及有限小幅实际存在；
2. R541 零能量起点下的准确一阶振子、二阶记忆正号及完整返回时的二阶零；
3. 保全部高度端 jets 的两 bump 实际端点 IFT；
4. 原 $p_1,t_1$ 与第三历史的真实进入成本；
5. 非零真实初能量一阶模型的同一个可用端点右逆与负记忆收据。

零能量回路在三阶可能产生什么号、如何在原同一规范内加载再真正释放已有能量、以及一次另选 Gram 的非平衡真实起点能否得到全部所需累计，都仍须继续完整构造。本文没有删掉 slow/fast 接缝的原历史，也没有把一个局部能量身份当成全 $M=0$、末 germ、frame、位置或 period 的返回。

## 原式来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：逐点完整矩密度、速度二次结构及原有序第三累计；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)(2)：完整速度势、速度面积与三次速度；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：同一正交母库、完整全相位 ruling 与非退化 $C_k$；
- [R537](R537-prescribed-finite-height-paths-with-one-gauge-and-complete-history-energy-bounds.md)：原水平变量与完整加速度／第三历史关系；
- [R541](R541-finite-curvature-and-positive-total-matrix-entry-on-one-stable-gram-branch.md)：本文第 1–7 节的原固定 Gram；
- [R543](R543-stable-large-gram-leaf-positive-matrix-density-and-exact-transverse-memory.md)：准确 $\rho_s=-2(d-q(h))h_s/h^3$ 与离叶入口门。

