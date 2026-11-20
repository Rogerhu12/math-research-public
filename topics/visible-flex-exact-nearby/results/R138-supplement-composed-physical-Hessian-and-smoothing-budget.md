# R138 补篇：先完整复合物理 Hessian，再支付积分平滑的残差预算

2026-11-20，visible-exact-astra-ac637-20261120；global_route 独立逐式核对。

**已证明的新解析结论。** T.8 的 Hessian 与同一完整坐标逆先作准确复合后，
只剩一个小的三角乘子、一个积分平滑项及一个完整 mean 秩项。这个式子
不含原 moving 方向的角导，不含任何待求逆，也不需要 residual 的二次
角导。它可以直接复用 [X 的首次实际结果](R138-supplement-actual-physical-budget-and-false-absorption.md)
给出的全域物理缺陷及 C1 上界，另算此前未执行的完整复合算子预算。

X 的全部成功值及三个 false 充分门保持原样。本篇不重新执行 X 的
物理传播、旧系数 producer 或旧因子链目标，也不提前声称新吸收门成立。

## 1. 准确均值与完整逆角方向

沿用 T、X 的同一真实物理角、同一 Qrepair 和反射类。记
$$
 \mathcal F=(B,C)=(u/v,1/v)\circ\Theta^{-1},\quad
 m=\langle v\rangle_\phi,\quad
 R=(R_u,R_v)=Q_r-F(Q),\quad
 \epsilon=I_\theta(CR_v).
 \tag{Y.1}
$$
右侧 moving residual 均先按实际 $\Theta^{-1}$ 拉回。$I_\theta$ 是
完整圆上均值零 primitive，背景标量为四重函数；所有均值均不删除。

若 $x=(b,c)=D\Psi_Qh$、$\mu=\langle h_2\rangle_\phi$，则
$$
 \boxed{\quad
 \frac{\mu}{m}=-m\langle c\rangle_\theta,\qquad
 \xi=-v q,\qquad
 q=I_\theta\{c-mC\langle c\rangle_\theta\}.
 \quad}
 \tag{Y.2}
$$
第一式也可直接从
$\langle C\rangle_\theta=1/m$ 沿 $h$ 微分得到：
$\langle c\rangle_\theta=-\mu/m^2$。它是两个真实角之间的完整 mean
恒等式，不是把原 mean 当零。

第二式是 X.5 的完整逆方向。为核常数，$\xi$ 在本题为 odd，
$q$ 也为 odd；真实 primitive 规范故恰给该式，没有额外积分常数。
由 $\langle C\rangle_\theta=1/m$，
$q_\theta=c-mC\langle c\rangle_\theta$ 的平均严格为零。

## 2. 先相乘后的完整 Hessian

置
$$
 \mathfrak s=R_u-BR_v,\qquad \mathfrak t=-CR_v,\qquad
 d=\binom{\mathfrak s_\theta}{\mathfrak t_\theta},\qquad
 A_R=\begin{pmatrix}\mathfrak t&\mathfrak s\\0&2\mathfrak t\end{pmatrix}.
 \tag{Y.3}
$$
则 T.8 的完整零阶项准确为
$$
 \boxed{\quad
 f_0=A_Rx+d\,I_\theta\{c-mC\langle c\rangle_\theta\}
          -m\epsilon\mathcal F_\theta\langle c\rangle_\theta .
 \quad}
 \tag{Y.4}
$$

**逐项证明。** 写
$$
 P_c=\begin{pmatrix}C&-BC\\0&-C^2\end{pmatrix},\qquad
 L=P_c^{-1},\qquad t_{\rm vec}=P_cR=C(\mathfrak s,\mathfrak t).
$$
直接矩阵相乘给
$$
 DP_c[t_{\rm vec}]L=A_R.
 \tag{Y.5}
$$
完整逆方向为 $h=L(x+\xi\mathcal F_\theta)$。把它代入 T.8，$\xi$
的系数是
$$
 (A_R-\mathfrak tI)\mathcal F_\theta
                 -(C(\mathfrak s,\mathfrak t))_\theta
       =-C\,d.
 \tag{Y.6}
$$
由 $vC=1$、$\xi=-vq$，该项恰为 $d q$。最后的 mean 项用 (Y.2)
得到 $-m\epsilon\mathcal F_\theta\langle c\rangle$。三组项相加即 (Y.4)。
因此本式与原完整 Hessian 相等，没有独立相减任何正上界。

T.7 的唯一方向一阶项仍是 $-\epsilon x_\theta$，继续放在 T.12--T.14
的共同输运中。这里没有抹去它，也没有将 WVC hybrid 的额外主部差
冒认为真正 $DF(Q_c)$ 的残差。

## 3. 两个残差标量先利用曲率和 torsion 的准确抵消

采用 X 第3、4节的同一个修补后 moving 曲率向量与 torsion：
$$
 \mathcal R=\Omega(r_1,r_2,r_3),\qquad
 \mathcal T=(0,\mathfrak u,0).
$$
原准确关系是
$$
 R_u=\frac ma(r_2-ur_3),\qquad
 R_v=\frac ma(\mathfrak u-vr_3),\qquad
 r_3=-aR_m/m^2.
$$
$r_3$ 仅径向，故 $r_{3,\theta}=0$。在 $\mathfrak s$ 中先抵消 $r_3$；
$\mathfrak t$ 仍保留该均值项，只是它的角导为零。因此准确得到
$$
 \boxed{\quad
 \mathfrak s=\frac ma(r_2-B\mathfrak u),\qquad
 \mathfrak t=\frac ma(r_3-C\mathfrak u).
 \quad}
 \tag{Y.7}
$$

设一个完整闭片上的修补后界为
$|\mathcal R|\le R_0$、$|\mathcal R_\phi|\le R_1$、
$|\mathfrak u|\le T_0$、$|\mathfrak u_\phi|\le T_1$，
并有 $|m|\le m_+$、$a\ge a_->0$、
$\lambda=m/v>0$、$|B|\le B_0$、$|C|\le C_0$、
$|B_\theta|\le B_1$、$|C_\theta|\le C_1$。则
$$
 \begin{split}
 s_0&=\frac{m_+}{a_-}(R_0+B_0T_0),&
 t_0&=\frac{m_+}{a_-}(R_0+C_0T_0),\\
 s_1&=\frac{m_+}{a_-}
                  (\lambda_+R_1+B_1T_0+B_0\lambda_+T_1),&
 t_1&=\frac{m_+}{a_-}(C_1T_0+C_0\lambda_+T_1)
 \end{split}
 \tag{Y.8}
$$
分别控制 $\mathfrak s,\mathfrak t$ 及它们的真实物理角一阶导。
这里的 $R_j,T_j$ 必须已经按 X.11a 付完完整修补费用，不能把原中心
改名为修补中心；原背景 $A^0$ 与 residual $C^0$ 的资格仍分开。
特别，$t_1$ 不需 $R_1$，更不需任何 residual 二次角导。

## 4. ambient 完整算子及真正平滑项

仍令 $W=\omega_\theta-H$，则
$x'=(W\cdot Y,-W\cdot X)=a(b,c)$。因为 $a$ 只径向，(Y.4) 乘 $a$
后仅将 $x$ 换为 $x'$。置 $c'=-W\cdot X$ 和 $J=[-Y,X]$，
T.14 的 Hessian 部分准确成为
$$
 \mathscr H_RW
   =L_RW+Jd\,I_\theta c'
         -mJ\{d\,I_\theta C+\epsilon\mathcal F_\theta\}
                          \langle c'\rangle_\theta ,
 \tag{Y.9}
$$
$$
 L_R=\mathfrak s\,Y\otimes X
             -\mathfrak t(Y\otimes Y+2X\otimes X).
 \tag{Y.10}
$$
其他完整项不变：
$$
 \mathcal T_RW=\mathscr H_RW+Z_*W+E_*W-\epsilon_\theta W,
 \tag{Y.11}
$$
其中 $Z_*,E_*$ 是 X.8 的准确矩阵，所有 mean 和原端条件保持。

记 $o_1\ge\|O_\theta\|_\infty$，$D_0=(s_1^2+t_1^2)^{1/2}$，则
$$
 L_0=(s_0^2+5t_0^2)^{1/2},\qquad
 L_1=2o_1L_0+(s_1^2+5t_1^2)^{1/2}
 \tag{Y.12}
$$
控制 $L_R$ 的 $C^0,C^1$ 范数。证明用正交 frame 中的 $2\times2$
矩阵 Frobenius 范数及两侧 frame 导数；没有分别给各 frame 因子付一串
负阶乘子费用。

对 $0\le\tau\le1/2$ 和四重标量 $f$，
$$
 \|I_\theta f\|_{L^2}
 \le c_\tau\|f\|_{H^{-\tau}},\qquad
 c_\tau=\frac{17^{\tau/2}}4.
 \tag{Y.13}
$$
这是频率 $n\in4\mathbb Z\setminus\{0\}$ 的
$\langle n\rangle^\tau/|n|$ 的准确最大值；该函数在 $n\ge4$ 单调下降。
平均模由 $I$ 准确删除，未在任何别的地方删除。

于是 (Y.9) 的积分项先到 $L^2$，再用
$L^2\hookrightarrow H^{-\tau}$，只需
$$
 \|Jd\,I_\theta(-X\cdot W)\|_{H^{-\tau}}
 \le D_0\,c_\tau\,N_\tau(1,o_1)\|W\|_{H^{-\tau}}.
 \tag{Y.14}
$$
这里 $N_\tau(A_0,A_1)=A_0^{1-\tau}(A_0+A_1)^\tau$ 是 X.3。
输出的 $Jd$ 只付 $C^0$ 范数 $|d|$，不再对它求导；
输入提取 $W\mapsto-X\cdot W$ 保留一次完整 $N_\tau(1,o_1)$。

## 5. 完整 mean 秩项的直接费用

真实逆角 $\Phi=\Theta^{-1}$ 及原 odd primitive 给
$$
 I_\theta C=\frac{\Phi(\theta)-\theta}{m}
      =-\frac{[I_\phi(v-m)]\circ\Phi}{m^2}.
 \tag{Y.15}
$$
导数核对用 $\Phi_\theta=mC$，两边都是 odd，故规范常数相同。
若 $m_-\le|m|$、$\|v-m\|_{A^0_\phi}\le V_\perp$，可取
$$
 C_I=\min\left\{\frac{\pi C_0}{8},
                        \frac{V_\perp}{4m_-^2}\right\}
       \ge\|I_\theta C\|_\infty .
 \tag{Y.16}
$$
第二式用 moving 四重 primitive 的 $A^0$ 范数。原positive闭行的
完整 $V_{\rm nonmean,A0}$ 可直接用；在germ上，
若原完整 $A^\sigma$ 的 $v$ 总范数上界为 $V^\sigma$，
则 $V^\sigma-m_-$ 是合法的 nonmean 上界，因为在每个实际点准确有
$\|v\|_{A^\sigma}=|m|+\|v-m\|_{A^\sigma}$。
这里减的是该非负和中 mean 的**下界**，不是相减两个独立上界。
Qrepair 的完整 nonmean 修补费还须另加。

若 $|\epsilon|\le e_0$、
$\|\mathcal F_\theta\|\le F_1$，(Y.9) 的 mean 秩项满足
$$
 \|\text{mean rank}\|_{H^{-\tau}\to H^{-\tau}}
 \le m_+(D_0C_I+e_0F_1)N_\tau(1,o_1).
 \tag{Y.17}
$$
输出系数只按 $L^2$ 取界。输入平均提取是正交零模投影，与
$-X\cdot W$ 的完整负阶乘子相接。若用非归一化 $2\pi$ 积分，
输出常量的 $\sqrt{2\pi}$ 与平均提取的 $1/\sqrt{2\pi}$ 正好抵消；
没有多添或删掉一个圆周长度因子。

## 6. 可直接执行的完整新上界

结合 (Y.11)--(Y.17)，对 $\tau=0,1/3,1/2$，
$$
 \boxed{\begin{split}
 k_{-\tau}^{\rm comp}
 ={}&N_\tau(L_0,L_1)
      +N_\tau(1,o_1)
          \{c_\tau D_0+m_+(D_0C_I+e_0F_1)\}\\
    &+N_\tau(Z_*)+N_\tau(E_*)+N_\tau(\epsilon_\theta)
 \ \ge\ \|\mathcal T_R\|_{H^{-\tau}\to H^{-\tau}} .
 \end{split}}
 \tag{Y.18}
$$
每个末三项使用 X 已给的完整 $C^0,C^1$ 表达式。没有删掉
$-\epsilon_\theta W$ 或 frame 缺陷。$R$ 二次角导不再出现。
原四重加反射等变类仍先由范数一的群正交投影 $\Pi_{\rm sym}$ 扩展；
$1/4$ 与 (Y.13) 只作用于提取后的四重标量。

本次新消费者可以按以下合法顺序工作：

1. 整个读取 X44737045152 的科学/执行对象，核同一source和对象身份，
   保其全部成功、false门、原始mean/边界/接口范围。
2. 从 X 的实际根四标量取得全正区统一 $Z,Z_\theta,P,P_\theta$ majorant，
   不重新传播它们；$\Gamma,E_\epsilon,A_\Theta,C_E,C_H,C_W$ 也只读。
3. 原4650闭行与真根germ、原7722 angular闭行仅作为原证据读取。
   全4651个真正共同正闭片上，用 (Y.7)--(Y.18) 形成新复合算子上界，
   并形成 T.22 的新 $E_0,E_1$。物理角转换、repair和mean完整保留。
4. 新积分可保守取
   $J_0^{\rm comp}=120C_W^{\rm old}\int(k_0^{\rm comp})^2dr$、
   $(K_-^{\rm comp})^2=\int(k_{-1/3}^{\rm comp})^2dr$。
   非负积分仍扩到原根区间左端，$x/K\le120$ 仅在真正区使用。
5. 读回完整保存球再形成新的 $h_E,w_E,z_E,r_E,r_B$ 和三个 $a$。
   不变的 $h_B,w_B,z_B$、根密度变换因子可直接读取旧球；
   最终门必须消费新旧完整保存球，不能只取显示中点。

这里全部新量仍是指定中心的显式系数预算。没有将未知方向范数或未知
BVP inverse 放入右侧，没有重新求已完成的 X 传播或原几何目标。
根型 $C_*$ 仍须独立证明；即使新 body-only 三门通过，也不自动给根型、
actual whole inverse、WVC hybrid逆、任一RHS或最终固定度量闭族。
