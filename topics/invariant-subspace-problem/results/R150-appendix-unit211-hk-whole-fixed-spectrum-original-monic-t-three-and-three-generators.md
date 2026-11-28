# 正确 h=k：固定谱参数下的全权首一 t 三次与原三生成

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-28（UTC）。

**状态：完整纸面证明，没有新执行。** 在当前正确 $h=k$ 碰撞图已付的原 $P_f$ 权图上，把物理 $\lambda$ 作为权参数固定。完整原 $N_0/P_1$ 使 $f,V$ 对原 $t$ 仿射；三个真均值与完整加权 NS/PS 的四个最高系数在全权环中生成单位理想。因此存在一个原理想内的全权首一三次
$$
q_t(t)=t^3+a_2t^2+a_1t+a_0.
\tag{1}
$$
必要代数在反演任何几何量之前由 $1,t,t^2$ 生成为权环上的模。

此结论不要求新 $\ell=1/2$ 分支先执行；不使用 $2\ell-1$、$\Delta$、$\Phi$、原物理 $D$ 或新的首项逆。它不宣称权参数已经有限或排空，也不把存在的全权组合系数冒充已展开执行的 Bézout。

## 1. 当前原权图和固定谱参数

采用当前正确碰撞值参数
$$
A=2\lambda^2-2\lambda+1,\qquad
B=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
\xi_v=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,\quad
w=\lambda-1-T,\quad h=k=1+\xi_v.
\tag{2}
$$
下文中心变量 $\xi,\eta$ 与此 $\xi_v$ 不混淆。

记
$$
\delta=1-Q,\quad m=u-\ell,\quad a=1-\ell,\quad
M=\ell^2\delta-m^2,\quad bc=M/(4\delta),
$$
$$
T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,\qquad
P_f=T_0(J-Q),
$$
$$
G=\lambda P_{02}-(1-u)T_0,\qquad
P_c=QP_{02}(\ell+T)-GT_0.
\tag{3}
$$

令 $\mathscr A$ 为当前正确碰撞权参数环；它是 $\mathbb Q[\lambda,u,Q]$ 的原已付纯权局部化，包含 (2)–(3) 的系数。本文只实际需要 $A,B,Q,\delta,M,P_{02},P_f$ 为单位，其余已经付款的支持可继续局部化。$M=4bc\delta$，而 $P_f=T_0(J-Q)$ 的单位性在交换环中同时支付 $T_0,J-Q$。不新增任何单位付款。

正确原来源由
[Pf 整碰撞原源静态审计](../notes/2026-11-28-unit211-h-equals-k-Pf-true-original-static-audit-8542.md)
及
[正确原 dual-germ 五式源码](../notes/2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py)
给出。这里使用真 $(d^2)_1=2d_0d_1$；不恢复已撤错误 compact 或其后继投影。

在本证明的分次中，$\lambda,u,Q,\ell,T,w,h$ 都属于系数环，次数为零；只有 $t$ 是几何自变量。**固定物理 $\lambda$ 不等于把其最高一次部分强行付成非零。** 恰恰相反，原 $N_0$ 恢复会给最高一次部分为零的准确线性身份。

## 2. 原 N0/P1 的完整仿射恢复

原两条线写成
$$
QV=Jf-G+bcQt,\qquad
P_ff+bc\,\Phi Qt+P_c=0.
\tag{4}
$$
因 $Q,P_f$ 已付，整个图上
$$
f(t)=-\frac{P_c+bc\,\Phi Qt}{P_f},\qquad
V(t)=\frac{Jf(t)-G+bcQt}{Q}.
\tag{5}
$$
这是完整原线的双向恢复，没有倒 $\Delta,\Phi$ 或任何斜率。特别 $\Phi=0$、$f$ 的 $t$ 系数为零等退化全部包含。

再用原 $E_0$ 和坐标定义
$$
W_1=T_0/2+2uf,\qquad
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},
$$
$$
A_1=2f-2V+2bc\,t.
\tag{6}
$$
所有 $f,V,x,y,A_1$ 都在 $\mathscr A[t]$ 中至多一次。

在首一有限自由且忠实平坦的扩张
$$
\mathscr A'=\mathscr A[\rho]/(\rho^2-\delta)
$$
中置
$$
b=\ell/2+m\rho/(2\delta),\quad
c=\ell/2-m\rho/(2\delta),\quad
p=1+\rho,\quad q=1-\rho,\quad
X=x+\rho y,\quad Y=x-\rho y.
\tag{7}
$$
$b,c,p,q$ 均为单位，因为 $bc$ 和 $pq=Q$ 为单位。始终保整个 $\rho$ 扩张，不选一根。

(6) 精确给
$$
bX+cY=V,\qquad bpX+cqY=W_1,\qquad
E_0=T_0-2W_1+4uf=0.
\tag{8}
$$
若 $f_1,V_1,X_1,Y_1$ 表示各式的 $t$ 系数，便有
$$
bX_1+cY_1=V_1,\qquad bpX_1+cqY_1=2uf_1.
\tag{9}
$$
最关键的是从 (4) 取 $t$ 系数得到
$$
\boxed{\quad Jf_1-QV_1+bcQ=0.\quad}
\tag{10}
$$
右侧 $\lambda P_{02}$、$G$ 都为纯权常数，所以不存在遗漏的最高 $\lambda$ 项。

## 3. 真均值与完整原加权条件

使用真 dual Gram 四行
$$
g_0=(0,0,p,q),\quad
g_1=(0,A_1,r,s),\quad
g_B=(p,r,0,t),\quad
g_C=(q,s,t,0),
$$
其中
$$
r=X-ap-ct,\qquad s=Y-aq-bt.
\tag{11}
$$
$\tau(v)=av_0+v_1+bv_2+cv_3$，头两坐标乘法是
$(vw)_1=v_0w_1+v_1w_0$。所有均值、$N_4$ 与 $P_2$ 采用这个完整原定义。

令 $E_{B,e},E_{B,o}$ 为 $E_B=E_{B,e}+\rho E_{B,o}$ 的偶奇部分，$E_C$ 为共轭。真原均值组合
$$
\mathcal R
=4(f-u)(V-f)+bc\,t^2
+t\!\left(4bc\,u-\ell V+\frac{m(T_0+4uf-2V)}{2\delta}\right)
\tag{12}
$$
满足完整原身份
$$
2\mathcal R+E_1-(\ell E_{B,e}+mE_{B,o})
-\left(\frac m\delta t-a\right)E_0=0.
\tag{13}
$$
这正是正确七自由变量 R 恒等式除去原单位的写法；也可直接由 (11) 和真 dual 乘法展开。(8) 已使 $E_0=0$，故替换 $E_1$ 为 $\mathcal R$ 是可逆的原行变换。没有借错误 Rbar。

完整加权原值为
$$
NS=bN_4(g_B)+cN_4(g_C)-2\lambda\ell h^2P_{02},
$$
$$
PS=bP_2(g_B)+cP_2(g_C)-\ell h^3P_{02}.
\tag{14}
$$
其右端目标在固定 $\lambda,u,Q$ 的分次中是纯权常数。

定义五条必要式
$$
I_5=(\mathcal R,E_{B,e},E_{B,o},NS,PS)\subset\mathscr A[t].
\tag{15}
$$
再加完整 $N_1$ 得原 $I_6$。本证明已经对 $I_5$ 成立；其余个别原值、完整 NV、其它矩条件可继续取商，绝不以这五式替代充分的全物理系统。

前三式 $t$ 次数至多二，NS/PS 至多三。为了保原来源而不引任何首项逆，使用
$$
\mathcal L=NS-PS-V E_{B,e}-(mx+\ell\delta y)E_{B,o}
          =NS-PS-bX E_B-cY E_C.
\tag{16}
$$
第二等式来自
$bX+cY=V$、$\rho(bX-cY)=mx+\ell\delta y$。
故 $\mathcal L\in I_5$，次数至多三。

若沿既有完整 Loww 记号，(16) 也等于
$$
\mathrm{Loww}-(2u-u\ell)E_{B,e}
-\bigl(2(u-\ell Q)-um\bigr)E_{B,o}.
\tag{17}
$$
差仅是纯权倍的二次均值，因此两者三次头相同；本文直接用 (16)，不需要重跑旧 Loww 投影。

## 4. 四个最高系数的整环原来源

令
$$
c_R=[t^2]\mathcal R,\quad
c_e=[t^2]E_{B,e},\quad
c_o=[t^2]E_{B,o},\quad
c_L=[t^3]\mathcal L,
$$
$$
\mathfrak h=(c_R,c_e,c_o,c_L)\subset\mathscr A.
\tag{18}
$$
某条式子降次时对应头准确为零，并不新增头非零假设。

在最高归一 $t=1$ 的写法中，暂将 $f_1,V_1,X_1,Y_1$ 简记为 $f,V,X,Y$。真均值最高二次是
$$
R=4f(V-f)+bc(1-2X-2Y),
$$
$$
E_B^{(2)}=c-2cY-2X^2+4fX,\qquad
E_C^{(2)}=b-2bX-2Y^2+4fY.
\tag{19}
$$
这些量属于 $\mathscr A'$，是已经恢复的四个仿射坐标的实际最高系数，不是新的自由变量。
$R=c_R$，且 $E_B^{(2)},E_C^{(2)}$ 与 $c_e,c_o$ 作可逆偶奇变换。

从原 rowB 直接取最高三次有
$$
N_{B,3}=2c(Y-f)-4cXY+4fX^2,\qquad
P_{B,3}=c-3cX+2X^3.
$$
C 行为共轭。逐项相减给
$$
N_{B,3}-P_{B,3}-X E_B^{(2)}
=c[2(X+Y-f)-2XY-1].
$$
按 $b,c$ 加权，且 (14) 的原目标次数为零，得到
$$
\boxed{\quad c_L=-2bc[1-2(X+Y)+2XY+2f].\quad}
\tag{20}
$$
这是完整原 NS/PS 的最高来源；没有将未付的最高原值变量当成物理单位。

以下通用中心身份亦见
[正确 Phi 全最高原稿 §3–4](R150-appendix-unit211-Phi-zero-corrected-whole-highest-unit-ideal-and-twenty-two-generators.md)，不可变正文 blob 4f11e89b8df2c409dd354944d40112f8260489d9。这里仅使用其通用原展开；该稿的 Phi 权关系从后续 §5 才开始，本证明不借用它、R6 或其任何付款。

## 5. 幂零不丢失的最高单位理想

在
$$
C=\mathscr A'/\mathfrak h\mathscr A'
$$
中计算。若它本来为零，结论已成；否则仍作下面的整交换环运算。由 (20) 和 $bc$ 单位，
$$
1-2(X+Y)+2XY+2f=0.
$$
置
$$
\xi=1-2X,\quad \eta=1-2Y,\quad P=\xi\eta,\quad S=\xi+\eta.
$$
于是
$$
4f=1-\xi-\eta-\xi\eta,
\tag{21}
$$
$$
2E_B^{(2)}=\eta(\xi^2+2c-1),\qquad
2E_C^{(2)}=\xi(\eta^2+2b-1).
\tag{22}
$$
从 (9) 和 (21) 精确得到
$$
cq\,\xi+bp\,\eta+uP=0.
\tag{23}
$$

保留非约化结构的核心恒等式是
$$
\boxed{
P R+P^3
=-2PX^2E_C^{(2)}-2PY^2E_B^{(2)}
 +(S-1)E_B^{(2)}E_C^{(2)}.
}
\tag{24}
$$
其直接展开可先令
$F_b=\eta^2+2b-1,F_c=\xi^2+2c-1$，
由 (21) 得
$$
R+P^2=-2X^2E_C^{(2)}-2Y^2E_B^{(2)}
+\frac{S-1}{4}F_bF_c;
$$
再乘 $P$ 并用 (22) 即得 (24)。

$R,E_B^{(2)},E_C^{(2)}$ 在 $C$ 中全为零，故 $P^3=0$。分别以 $\xi,\eta$ 乘 (23)，得到
$$
cq\,\xi^2=-P(bp+u\xi),\qquad
bp\,\eta^2=-P(cq+u\eta).
$$
因 $bp,cq$ 原已付，
$$
\xi^6=\eta^6=0,\qquad
\mathfrak n=(\xi,\eta)\subset C,\qquad \mathfrak n^{11}=0.
\tag{25}
$$

模掉这个已证幂零理想后，(21) 给
$$
X=Y=\tfrac12,\qquad f=\tfrac14,\qquad V=\ell/2.
\tag{26}
$$
原 $R=0$ 再给
$$
4bc=2\ell-1.
\tag{27}
$$
此处既未假设 $2\ell-1$ 原为单位，也没有将其反演。

但固定谱参数的准确原 $N_0$ 最高线 (10) 在 (26)–(27) 下变成
$$
0=J/4-Q\ell/2+bcQ=(J-Q)/4.
\tag{28}
$$
$J-Q$ 是原 $P_f$ 的单位因子，所以 (28) 是单位矛盾。因此 $C/\mathfrak n=0$。由 $\mathfrak n^{11}=0$，原环 $C$ 本身为零；没有只证明约化点消失然后跳过重数。

$\mathscr A'/\mathscr A$ 有限自由且忠实平坦，单位理想下降，得到
$$
\boxed{\quad \mathfrak h=\mathscr A.\quad}
\tag{29}
$$
这不是对一组数值权点或某个模素数的判断，而是整个原系数环的理想等式。

本证明只有原自由变量 $t$。由于 (5) 已完整仿射消去 $f,V$，不存在额外的 $t_\infty=0$、但 $f,V$ 独立趋于无穷的方向。因此无需引用三变量最高系统的 $t=0$ 图，也无需用 $2\ell-1$ 支付其三均值头。整 $\ell=1/2$ 支仍包含在 (29) 中。

## 6. 真首一 t 三次和原三生成

由 (29)，存在四个真正全权系数
$\alpha_R,\alpha_e,\alpha_o,\alpha_L\in\mathscr A$ 满足
$$
\alpha_Rc_R+\alpha_ec_e+\alpha_oc_o+\alpha_Lc_L=1.
\tag{30}
$$
定义完整原组合
$$
q_t(t)=\alpha_Rt\mathcal R+\alpha_etE_{B,e}
       +\alpha_otE_{B,o}+\alpha_L\mathcal L.
\tag{31}
$$
每项次数至多三，且 (30) 使 $t^3$ 系数恰为 $1$。所以 (31) 就是 (1)，并且
$$
q_t\in I_5\subset I_6.
$$
由 (13)、(16) 可把它直接回到完整原 $E_1,E_B,E_C,NS,PS$ 来源；没有新的分母或虚构的显式系数。

于是
$$
\mathscr A[t]/I_5,\qquad \mathscr A[t]/I_6
$$
都由 $1,t,t^2$ 生成为 $\mathscr A$ 模。这里没有假设这三元自由、独立、交换乘法矩阵已显式构造或各权纤维维数恒定。它们只是首一三次自由环境 $\mathscr A[t]/(q_t)$ 的商。

再加入完整 $N_4(V_{\rm phys})$、个别 N/P 或其它原条件，仍为有限模的商。本文没有把原三次必要商当成全物理充分系统。

## 7. 范围、执行和后续接口

每个固定原权参数 $(\lambda,u,Q)$ 上，反演几何量之前的必要 $t$ 代数长度至多三；$f,V,x,y,A_1$ 按 (5)–(6) 唯一恢复。该结论保重数。权参数支撑可能仍是曲线或更高维；本文没有新纯权覆盖、全权有限点数或排空结论。

随后若再反演 $t$、其它几何量，不能无条件声称所得代数仍为同一 $\mathscr A$ 上的有限模。不过各权纤维原已 Artin，局部化只删其中部分分量，纤维有限性与长度上界仍保持。本篇未把恢复 $\rho$ 或独立尺度 $U_0$ 的额外坐标计入“三”。

(30) 是由完整整环证明得到的存在性，不是已执行的多项式系数清单。本篇没有新脚本、展开矩阵、参数载荷或计算回执；不新增任何复跑门。后续若需要显式 $q_t$，应将它作为新原输入，并仍逐项返回实际原组合，不能以存在性替代已执行的系数。

目前冻结的整个 $\ell=1/2$ 二次常数域源码是独立的第一次原返回，仍按原字节与预算等待实际结果。本纸证不预先判其目标为单位，也不改变它的任何执行边界。
