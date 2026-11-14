# R287：实际移动角色的双边极限与任意单位盘逐位右源

2026-11-14，normal-annihilator / 789f。**状态：已证明的中间结论；一般正正常见证仍未排除。**

本稿使用原 Haar 模型 $H=L^2(\mathbb Z_2,\mu)$、$Uf(y)=f(y-1)$、$A=M_wU$ 与实际 $N_j=A^{2^j}/\|A^{2^j}\|$。$\mathcal A$ 为 $A$ 生成的含单位算子范数闭代数。真实递推是

$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
N_j^2=\eta_jN_{j+1},\qquad
0<\eta_j\le e^{-770\cdot16^j}.
\tag{1.1}
$$

所有出现的来源均在原 $\mathcal A$ 或相应真实尾代数内。第一部分补足 [R282 移动源附录](R282-appendix-actual-moving-commutant-sources-and-nonvanishing-normal-error.md)的真实伴随配对；第二部分处理任意非周期、无最高位限制的单位盘逐位参数，其总偏差预算可增长到 $(2^m)^4$ 的固定小倍数。没有排除一般右因子，也没有排除一般正常正湮灭者。

## 1. 同一个移动角色的两种强近似

令

$$
W_j=(I-N_j)(I+N_j)^{-1},\qquad
\chi_j=\mathbf1_{\{j\text{ 位}=0\}}-\mathbf1_{\{j\text{ 位}=1\}}.
$$

按第 $j$ 位写 $t_j=\eta_jN_{j+1}$，则准确有

$$
W_j=(I-t_j)^{-1}
\begin{pmatrix}I+t_j&-2t_j\\-2I&I+t_j\end{pmatrix}.
\tag{1.2}
$$

特别，若输入为第 $j$ 位的 $\Omega_+=(e_0+e_1)/\sqrt2$ 张量任意其余向量，则

$$
W_j(\Omega_+\otimes v)=\Omega_-\otimes v,\qquad
W_j^*(\Omega_+\otimes v)=-\Omega_-\otimes v.
\tag{1.3}
$$

第二式直接对 (1.2) 取伴随再相加两列；不要求 $t_j$ 自伴。故对只依赖低于 $j$ 位的柱函数 $f$，

$$
W_jf=\chi_jf,\qquad W_j^*f=-\chi_jf.
\tag{1.4}
$$

这些都不是全空间的乘法算子等式。所有 $W_j$ 彼此交换，所有 $W_j^*$ 也彼此交换；本稿不混用 $W_j$ 与 $W_k^*$ 的交换性。

沿用 R282 附录的具体来源。对 $0\le j\le n$ 置

$$
\theta_{j,n}=\frac{2\pi2^j}{2^{n+1}},\quad
\alpha_{j,n}=\frac{1+e^{i\theta_{j,n}}}{2},\quad
\beta_{j,n}=\frac{1-e^{i\theta_{j,n}}}{2},
$$

$$
R_n=\prod_{j=0}^n(\alpha_{j,n}I+\beta_{j,n}W_j),\quad
c_n(y)=\exp\left(\frac{2\pi i(y\bmod2^{n+1})}{2^{n+1}}\right).
\tag{1.5}
$$

已有的实际块估计 $\|W_j\|<3$ 给

$$
\sup_n\|R_n\|\le e^{3\pi}.
\tag{1.6}
$$

设 $\sigma_n=\sum_{j=0}^n\theta_{j,n}=2\pi(1-2^{-n-1})$。对每个固定向量，

$$
\boxed{R_n-M_{c_n}\longrightarrow0\quad\mathrm{SOT},}
$$

$$
\boxed{R_n^*-e^{-i\sigma_n}M_{c_n}\longrightarrow0\quad\mathrm{SOT},
\qquad R_n^*-M_{c_n}\longrightarrow0\quad\mathrm{SOT}.}
\tag{1.7}
$$

第一式已在 R282 附录中证明；下面给两式共同的低柱论证，准确付清第二式。固定低 $k$ 位柱函数 $f$，分别将 $R_n$、$R_n^*$ 分成 $j<k$ 的低因子与 $j\ge k$ 的高因子。低角度之和趋零，且

$$
\|\alpha I+\beta W_j-I\|\le4|\beta|\le2|\theta|,
$$

其伴随同界，因此两个低因子积都在算子范数中趋 $I$。高因子必须按 $j=k,k+1,\ldots,n$ 递增作用：每一步的输入仍是该步的低位柱，才可用 (1.4)。原因子的作用是乘 $\alpha+\beta\chi_j$；伴随因子的作用是乘

$$
\overline\alpha-\overline\beta\chi_j
=e^{-i\theta}(\alpha+\beta\chi_j).
\tag{1.8}
$$

高位各乘法因子模长为 $1$，故高因子准确生成对应的高位角色及相位。低位标量角色乘积一致趋 $1$；低位遗漏的总相位也趋零。再用 (1.6)、乘子范数 $1$ 和有限柱稠密性，得 (1.7)。这没有对未经控制的移动输入使用强收敛。

注意，(1.7) 的第二个乘子仍是 $c_n$，不是 $\overline{c_n}$。事实上，$c_n^2\to0$ 弱*，从而对每个固定 $f$，

$$
\boxed{\|R_n^*f-M_{\overline{c_n}}f\|\longrightarrow\sqrt2\,\|f\|.}
\tag{1.9}
$$

这是由 $\|(c_n-\overline{c_n})f\|^2\to2\|f\|^2$ 与 (1.7) 得到的。因此 (1.7) 不提供 $R_n-M_{c_n}\to0$ 的强伴随版本。

## 2. 真来源平方及移动归一化幂的弱极限

写 $N_n=M_{p_n}U^{2^n}$，这里用 $p_n$ 表示原权轮廓，避免与后文 $q=2^m$ 混淆。由原进位递推，

$$
p_n=\mathbf1_{\{n\text{ 位}=1\}}+
\eta_n\mathbf1_{\{n\text{ 位}=0\}}p_{n+1},\qquad
0\le p_n\le1,\qquad p_n\longrightarrow\tfrac12\quad\text{弱*}.
\tag{2.1}
$$

原 $U^{2^n}\to I$ 强，且 $U^{2^n}c_n=-c_n$。由 (1.7)，对每个固定 $f$，

$$
N_nR_nf+p_nc_nf\longrightarrow0\quad\text{于 }H.
\tag{2.2}
$$

在这一步，乘子相位先被精确移出；剩下的平移误差是固定 $f$ 的 $U^{2^n}f-f$。

现在取固定 $f,g$。内积约定线性于第一个变量，由 (1.7)，

$$
\langle R_n^2f,g\rangle
=\langle R_nf,R_n^*g\rangle
\longrightarrow\langle f,g\rangle.
$$

又因为 $R_nN_n=N_nR_n$，由 (2.2)、(1.7)、(2.1)，

$$
\begin{aligned}
\langle N_nR_n^2f,g\rangle
&=\langle N_nR_nf,R_n^*g\rangle\\
&=-\int p_n f\overline g\,d\mu+o(1)
\longrightarrow-\tfrac12\langle f,g\rangle.
\end{aligned}
$$

所以

$$
\boxed{R_n^2\longrightarrow I,\qquad N_nR_n^2\longrightarrow-\tfrac12I
\quad\mathrm{WOT}.}
\tag{2.3}
$$

两个序列一致有界。因此对任意固定迹类 $\rho$，

$$
\boxed{\operatorname{Tr}(\rho R_n^2)\to\operatorname{Tr}\rho,
\qquad \operatorname{Tr}(\rho N_nR_n^2)\to-\tfrac12\operatorname{Tr}\rho.}
\tag{2.4}
$$

推广至迹类只用有限秩迹范数逼近与统一算子界。特别，$F_n=I-R_n^2\in\mathcal A$ 满足 $F_n\to0$ 弱而 $N_nF_n\to I$ 弱；这里的左因子 $N_n$ 随 $n$ 改变，不能换为固定慢符号。

若原见证满足 $\operatorname{Tr}(\rho SG)=0$ 对全部 $G\in\mathcal A$，代入 $G=R_n^2G_0$ 后，(2.3) 对固定 $S,G_0$ 仍只返回原来的 $\operatorname{Tr}(\rho SG_0)=0$。要从 $S=\sum_ja_jX_j$ 中隔离移动第 $n$ 项，必须同时控制所有 $j$ 与 $n$ 相近的项、完整高尾及正常向量近似速度。$a_n\asymp n^{-2}$ 不能被无速率的正常尾 $o(1)$ 自动支付。

## 3. 任意单位盘逐位参数的真实尾来源

下面固定任意尾起点 $m\ge1$，令 $q=2^m$。取任意复数序列 $z=(z_j)_{j\ge m}$，只要求

$$
|z_j|\le1\quad(j\ge m),\qquad
B=\sum_{j\ge m}|1-z_j|<\infty.
\tag{3.1}
$$

没有周期性要求，没有支持长度或最高位限制；允许无穷多个不同参数，也允许有限个 $z_j=0$。实相位 $z_j=e^{i\theta_j}$、$\sum|\theta_j|<\infty$ 是特例，且 $B\le\sum|\theta_j|$。

定义

$$
F_j(z_j)=(I+z_jN_j)(I+N_j)^{-1}
=I+(z_j-1)Y_j,
\quad Y_j=N_j(I+N_j)^{-1},
$$

$$
R_{m,z}=\prod_{j=m}^{\infty}F_j(z_j),
\qquad G_{m,z}=R_{m,z}^{\,2}.
\tag{3.2}
$$

这些无穷积均在算子范数中收敛，且得到真实尾代数中的单位。为完整证明它，利用 $N_j^2=\eta_jN_{j+1}$：对每个 $|z|\le1$，

$$
N_j(I+zN_j)^{-1}
=(N_j-zN_j^2)(I-z^2N_j^2)^{-1},
$$

$$
\|N_j(I+zN_j)^{-1}\|
\le\frac{1+\eta_j}{1-\eta_j}<2.
\tag{3.3}
$$

于是

$$
\|F_j-I\|\le2|1-z_j|,
\qquad
F_j^{-1}=I+(1-z_j)N_j(I+z_jN_j)^{-1},
$$

$$
\|F_j^{-1}-I\|\le2|1-z_j|.
\tag{3.4}
$$

绝对可和的偏差保证正积和逆积都范数收敛；对有限积取恒等式再取极限，证明它们互为逆。每个有限积及逆都在真实尾代数中，因此极限也在该代数中。并有完整预算

$$
\boxed{\|R_{m,z}\|,\ \|R_{m,z}^{-1}\|\le e^{2B},
\qquad
\|G_{m,z}\|,\ \|G_{m,z}^{-1}\|\le e^{4B}.}
\tag{3.5}
$$

这只是实际单位的范数界，不声明它的逆或伴随在任何移动向量上近似某个逐点逆乘子。

## 4. 纯模型的准确矩：每个坐标都保留

纯比较算子为

$$
D_m=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+1)^{-2},
\qquad a_\Sigma=\sum_{j\ge0}a_j<2.
$$

对应的纯因子和来源为

$$
F_j^0=I+(z_j-1)E_j,\qquad
R_{m,z}^0=\prod_{j\ge m}F_j^0,
\qquad G_{m,z}^0=(R_{m,z}^0)^2.
$$

它们同样范数收敛。因 $E_j^2=0$，

$$
(F_j^0)^2=I+2(z_j-1)E_j,
$$

$$
\omega_j((F_j^0)^2)=z_j,\qquad
\omega_j(E_j(F_j^0)^2)=\tfrac12.
\tag{4.1}
$$

令

$$
h_m=\omega_m(D_m^q)=q!\,e_q(a_j/2:j\ge m)>0,
$$

其中 $e_q$ 为基本对称函数。利用 $D_m^q=q!\sum_{|F|=q}a_FE_F$ 的绝对范数收敛展开，(4.1) 给准确公式

$$
\boxed{
\omega_m(D_m^qG_{m,z}^0)
=q!\,2^{-q}\sum_{\substack{F\subset[m,\infty)\\|F|=q}}
a_F\prod_{j\notin F}z_j.}
\tag{4.2}
$$

无穷乘积存在，因为 $\sum|1-z_j|<\infty$；允许其为零。有限来源时逐位相乘即可；无穷来源由范数收敛取极限，而右侧由 $\sum_{|F|=q}a_F<\infty$ 及 $|\prod_{j\notin F}z_j|\le1$ 支付控制收敛。因此

$$
\boxed{|\omega_m(D_m^qG_{m,z}^0)|\le h_m.}
\tag{4.3}
$$

对实相位特例，(4.2) 也可写为

$$
\omega_m(D_m^qG_{m,z}^0)
=e^{i\sum_j\theta_j}\,
q!\,e_q\bigl((a_j/2)e^{-i\theta_j}:j\ge m\bigr).
\tag{4.4}
$$

这里没有把复相消后的来源当成正锥，而是在准确保留所有坐标系数后使用绝对值界。

## 5. 纯全多变量代数的最低次数投影：分母不损失单位逆范数

令 $\mathfrak E_m$ 为所有 $E_j$（$j\ge m$）生成的含单位算子范数闭代数。它有等距自同构

$$
\Gamma_t(E_j)=e^{it}E_j,\qquad t\in\mathbb R.
\tag{5.1}
$$

为避免把无限乘积酉误放入 Haar 表示，证明如下。对任何有限坐标多项式 $P$，选择含其全部坐标的有限集 $J$。在这些位上用 $\operatorname{diag}(1,e^{it})$ 的有限张量积作酉共轭，准确把每个 $E_j$ 变为 $e^{it}E_j$，故保存 $P$ 的算子范数。两个表示取坐标并集可知代入映射良定义。于是它从有限多项式等距延拓到 $\mathfrak E_m$；逆是 $\Gamma_{-t}$。有限多项式逼近还保证 $t\mapsto\Gamma_t(T)$ 对每个 $T\in\mathfrak E_m$ 范数连续。

因此 Bochner 积分

$$
\mathsf P_k(T)=\frac1{2\pi}\int_0^{2\pi}e^{-ikt}\Gamma_t(T)\,dt
\tag{5.2}
$$

是范数不超过 $1$ 的第 $k$ 次齐次投影。每个有限纯积 $G_{m,z}^0$ 的常数项为 $I$，其余项次数均正；范数极限给 $\mathsf P_0(G_{m,z}^0)=I$。又 $\Gamma_t(D_m^q)=e^{iqt}D_m^q$，所以

$$
\boxed{\mathsf P_q(D_m^qG_{m,z}^0)=D_m^q,
\qquad \|D_m^qG_{m,z}^0\|\ge\|D_m^q\|.}
\tag{5.3}
$$

此式对全部 (3.1) 的参数成立，完全不含 $B$ 的指数损失。它在纯比较代数上使用真实有限位酉共轭，没有断言同一 gauge 保持原带进位代数。下一节单独支付返回原模型的全部费用。

## 6. 无限实际来源的全携带误差

原实际估计 $\|Y_j-E_j\|\le4\eta_j$ 给

$$
\|F_j-F_j^0\|\le4\eta_j|1-z_j|.
$$

置 $\gamma_m=e^{-770\cdot16^m}$，则 $j\ge m$ 时 $\eta_j\le\gamma_m$。对有限积作望远镜，再由 (3.4) 和纯积的 $e^B$ 界取极限，得到

$$
\|R_{m,z}-R_{m,z}^0\|\le4\gamma_mB e^{2B},
$$

$$
\boxed{\|G_{m,z}-G_{m,z}^0\|\le8\gamma_mB e^{4B}.}
\tag{6.1}
$$

这些估计对参数所在的最高位和全部跨度统一；没有用截断支持大小替代 $B$，也没有假设实际 $\eta_j$ 本身单调。

取 $S=S_N=\sum a_jN_j$ 或 $S=S_Y=\sum a_jY_j$，令 $Q_m$ 为 R253 相应的实际有限 dyadic 相位消元符号：

$$
\prod_{\zeta^q=1}\gamma_\zeta(S)=I_{<m}\otimes Q_m,
\qquad Q_m\ne0.
$$

沿用已证明且保留全部原进位的估计

$$
\|Q_m-D_m^q\|\le e_m,
\qquad
 e_m=13a_\Sigma q(3a_\Sigma)^{q-1}
\exp\left(-\frac{770}{16}q^4\right).
\tag{6.2}
$$

来源为 [R253 恒等乘子附录 §2](R253-appendix-identity-multiplier-vacuum-ratio-decay.md)；它分别适用于两个原慢符号，并未把实际模型换成纯模型。结合 (3.5)、(6.1) 及 $\|D_m^q\|\le a_\Sigma^q$，有

$$
\boxed{\|Q_mG_{m,z}-D_m^qG_{m,z}^0\|
\le\varepsilon_m(B):=
 e^{4B}\bigl(e_m+8a_\Sigma^q\gamma_mB\bigr).}
\tag{6.3}
$$

(4.3)、(5.3) 因而给

$$
|\omega_m(Q_mG_{m,z})|\le h_m+\varepsilon_m(B),
$$

$$
\boxed{\|Q_mG_{m,z}\|\ge\|D_m^q\|-\varepsilon_m(B).}
\tag{6.4}
$$

与仅用 $\|G^{-1}\|$ 得到的分母不同，(6.4) 保住了最低齐次项的完整范数。无论 (6.4) 右侧是否正，$Q_mG$ 本来就非零，因为 $Q_m\ne0$ 而 $G$ 为实际单位。

## 7. 任意非周期单位盘族在四次总预算下统一失败

调用 [R230《熵偏转与增长周期多模式右滤子》§3](R230-appendix-entropy-tilts-and-growing-period-multivariate-filters.md)的已证纯正锥估计，仅取该文 $W_0=I$，得到

$$
\frac{h_m}{\|D_m^q\|}
\le\exp\left(\frac{m+1}{2}-\frac{\pi q}{16}\right).
\tag{7.1}
$$

这条不等式是对 $D_m^q$ 自身的旧范数下界；没有把本稿无周期 $G$ 套进该文的周期滤子结论。其证明通过每位入选概率 $t_{j,q}=[1+(2(j+1)/q)^2]^{-1}$、有限位 Jensen 偏转、$\mathcal H(t)\ge t^2/2$ 及积分比较，给 $\log(\|D_m^q\|/h_m)\ge\pi q/16-(m+1)/2$。

真空矩另有原单项式下界

$$
h_m\ge(8eq)^{-q}.
\tag{7.2}
$$

例如只保留 $F=\{m,\ldots,m+q-1\}$ 一项，再用 $m\le q$ 与 $q!\ge(q/e)^q$ 即得。

**定理 7.1。** 固定任意

$$
0\le b<\frac{770}{64}.
\tag{7.3}
$$

存在 $m_0(b)$，使对所有 $m\ge m_0(b)$，对全部满足 (3.1) 且 $B\le bq^4$ 的参数序列，以及任一实际慢符号 $S_N$、$S_Y$ 相应的 $Q_m$，均有

$$
\boxed{
\frac{|\omega_m(Q_mG_{m,z})|}{\|Q_mG_{m,z}\|}
\le2\exp\left(\frac{m+1}{2}-\frac{\pi q}{16}\right)
\longrightarrow0.}
\tag{7.4}
$$

**证明。** 由 (6.2)、(6.3)、(7.2)、$\gamma_m=e^{-770q^4}$，一致于 $B\le bq^4$，

$$
\boxed{
\frac{\varepsilon_m(B)}{h_m}
\le\exp\left[-\left(\frac{770}{16}-4b\right)q^4
+O_b(q\log q+\log q)\right]\longrightarrow0.}
\tag{7.5}
$$

当 $b=0$ 时第二误差项为零；一般情形把 $B$ 的额外因子界为 $1+bq^4$ 即得同一式。严格阈值 (7.3) 正好确保所写的四次负指数保留。

令 $A_m=\pi q/16-(m+1)/2$，$t_m(B)=\varepsilon_m(B)/h_m$。由 (6.4)、(7.1)，对充分大的 $m$，

$$
\frac{|\omega_m(Q_mG)|}{\|Q_mG\|}
\le e^{-A_m}\frac{1+t_m(B)}{1-t_m(B)e^{-A_m}}.
$$

括号比值在整个参数族上统一趋 $1$，因而充分大时不超过 $2$。这证明 (7.4)。$\square$

等价地，任何逐层变化的参数族若满足

$$
\limsup_{m\to\infty}\frac{\sum_{j\ge m}|1-z_{m,j}|}{2^{4m}}
<\frac{770}{64},
$$

均满足同一消失结论。特别，任意非周期实相位只要
$\limsup_m\sum_{j\ge m}|\theta_{m,j}|/2^{4m}<770/64$ 即被覆盖；更准确的预算是 $|1-e^{i\theta}|$ 之和。

(1.5) 的角色来源移到任意尾起点后，取任意更远的末端，其总相位小于 $2\pi$，所以平方来源属于定理。末端可以任意快地远离 $m$；(7.4) 不以最高位控制误差。参数也可专门依赖某个未知正常密度，只要它们仍处于 (3.1)、(7.3) 的准确预算内，统一估计不变。

## 8. 已付和仍未付的量词

本稿给出了两个不同的完整结论。第一，具体原交换子来源同时有 (1.7) 的两种固定向量强近似，并给 (2.3)–(2.4) 的真实双边弱/正常迹配对；这不能被写成伴随乘子一致近似。第二，全部满足四次总偏差预算的单位盘逐位来源都已在原模型中支付无限积、单位逆及携带误差，完全允许非周期、无最高位及无穷参数；它们不能使 R253 的真空比产生非消失下界。

R253 的完整量仍为

$$
\kappa_m=\sup_{\substack{G\in\mathcal B_m\\Q_mG\ne0}}
\frac{|\omega_m(Q_mG)|}{\|Q_mG\|}.
$$

本稿没有对 $\kappa_m$ 给上界或非消失下界；没有覆盖任意尾右因子、任意有限头依赖源、越过所证总预算的来源，或不能写成此处单位盘逐位平方乘积的密度专属来源。它也没有将随 $m$ 改变的左因子极限转为固定 $S$ 的强主理想单位。所有正常见证和原不变限制的剩余缺口保持不变。
