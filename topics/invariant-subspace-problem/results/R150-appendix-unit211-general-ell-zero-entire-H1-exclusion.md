# R150：一般 ell=0 面上整条 H1=0 权曲线的原系统排除

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro）。

## 1. 结论及未扩大范围

原 essential unit211 的一般 LS 权图在

$$
\ell=0,\qquad H_1=2u+Q-2=0
$$

上没有满足原物理单位的解。本结论没有附加 W=0、Delta=0 或 Q=1-u；因而可以在整个一般 ell=0 余面支付 H1。它尚未排除整个 ell=0 面或 ordinary ISP。

这是新一般 ell=0 原 Gram 的四二次头所给的整条边界，不是重新计算旧 Q=1-u、ell=0 权线。

## 2. 原 Gram、原六行及整条曲线

设 r²=1-Q，p=1+r，q=1-r，并在 ell=0 上取

$$
a=1,\quad b=\frac{ur}{2(1-Q)},\quad c=-b,\quad
bc=-\frac{u^2}{4(1-Q)}.
$$

令独立有限变量为 x,y,t，X=x+ry，Y=x-ry。原物理单位含

$$
u(u-1)Q(Q-1)P_{02},\qquad
P_{02}=uA,\quad A=2u^2-6u+4-Q.
$$

从同一原 E0、N0、P1 方程精确重建

$$
f=\frac{x+y+u-1}{2},\quad V_2=2u,\quad T_0=-2u(u-1),
$$

$$
\lambda=\frac{2ux+(2u-uQ)y-uT_0-(2u+2u^2)f+bcQt}{P_{02}},
$$

$$
J=2u(1-u),\quad \Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q),
$$

$$
T=\frac{[\lambda P_{02}-(1-u)T_0]T_0-P_f f-\Phi bcQt}
{QP_{02}}.
$$

四行原 Gram 为

$$
g_0=(0,0,p,q),\quad
g_1=(0,A_G,R_G,S_G),\quad
g_2=(p,R_G,0,t),\quad
g_3=(q,S_G,t,0),
$$

其中 R_G=X-p-ct，S_G=Y-q-bt，A_G=2f-2bX-2cY+2bct。
使用原代数乘法

$$
vz=(v_0z_0,\ v_0z_1+v_1z_0,\ v_2z_2,\ v_3z_3),
\quad {\bf1}=(1,0,1,1),\quad
\tau(v)=v_0+v_1+bv_2+cv_3.
$$

记 K(v)_j=tau(g_j v)、d=K(1)、F2=tau(d)=2f。原 mean 为
E_j=epsilon_j-2K(d)_j-2(d²)_j+2F2 d_j，其中 epsilon1=2tau(g0 g1)，其余 epsilon_j=tau(g_j²)。
原三次型严格按

$$
\mathcal N(v)=2\tau(dv^2)-F_2\tau(v^2)
-4\tau(v)\tau(dv)+2F_2\tau(v)^2+\tau(vK(v)),
$$

$$
\mathcal P(v)=\tau((v-\tau(v){\bf1})^3)
$$

定义。将 E2=EBe+r EBo、E3=EBe-r EBo 分成偶/奇部分，令

$$
P_j=3\tau((g_0-\tau(g_0){\bf1})^2(g_1-\tau(g_1){\bf1})),
$$

$$
N_H=\mathcal N(g_0+g_1)-\mathcal N(g_0)-\mathcal N(g_1)
-\tfrac43\lambda P_j.
$$

再记 A2=2lambda²−2lambda+1、B3=4lambda³−6lambda²+3lambda−1，保留两个真实加权 singleton 必要式

$$
NS=b\mathcal N(g_2)+c\mathcal N(g_3)-2\lambda P_{02}(2T+A_2),
$$

$$
PS=b\mathcal P(g_2)+c\mathcal P(g_3)-P_{02}(3T+3A_2+B_3).
$$

源逐项检查 E0=0、N(g0)=2lambda P02、Pj=3(lambda−1−T)P02、P(g0)=P02，以及 NS/PS 对原 HA/HB 的完整迹身份。因此

$$
F=(E_1,EBe,EBo,N_H,NS,PS)=0
\tag{1}
$$

确实是同一个原解的六条必要式；没有把任意六多项式当作原输入。原 Dphysical=-T² 也被保留，但下述常数 1 反证不需要额外对 D 饱和。

现在令 Q=2−2u。则

$$
Q-1=1-2u,\qquad P_{02}=2u(u-1)^2.
$$

所以整条曲线的原单位仅需 u(u−1)(2u−1)；没有另删有限 u。把此表达式直接代入原 Gram 后才形成 (1)，不是在一个已经除过 H1 的通用规约上强行专化。

六式按已付分母清为多项式，再仅剥上述原单位公因子；每次都检查精确乘回。前四式的有限次数是 2，后两式是 3。

## 3. 完整原 Macaulay 矩阵与两个固定行列式

按照总次数递增、同次数 x 指数递减、再 y 指数递减排列 x,y,t 的全部次数不超过 4 的 35 个单项式，最后将常数列移到第 34 列（编号从 0 开始）。

前四条已清原式各乘全部次数不超过 2 的十个单项式；后两条各乘全部次数不超过 1 的四个单项式。得到固定

$$
M(u)\in M_{48,35}(\mathbb Q[u]).
$$

全部 48 行都以完整原多项式乘积检查来源，故每个原点满足

$$
M(u)\,(x,y,t,x^2,xy,\ldots,1)^{\mathsf T}=0.
\tag{2}
$$

这里省略号严格按上述单项式次序定义，列尾的 1 使该列向量必定非零。

取固定前 34 行的编号列表

$$
I=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
18,20,21,19,30,23,24,31,32,33,29,34,35,36,40,41,42).
$$

定义两个完整 35 阶原行列式

$$
\Delta_{44}=\det M_{I\cup(44),*},\qquad
\Delta_{45}=\det M_{I\cup(45),*}.
\tag{3}
$$

这些编号最初通过 p=1009、u=7 的非恒列消元选择；数值步骤只选行，结论不使用有限域空性。之后 (3) 在 QQ[u] 上独立作完整 Bareiss 行列式，每个行列式的 13685 次精确除法均实际乘回。由于所得是多项式恒等式，中间 Bareiss 主元在某个 u 为零不删除该点。

两行列式次数分别为 72、73。只剥原单位后，有非零有理常数 c44,c45 使

$$
\Delta_j=c_j\,u^{17}(u-1)^{29}(2u-1)^{17}R_j(u),
\quad j=44,45,
$$

$$
\deg R_{44}=9,\qquad \deg R_{45}=10.
\tag{4}
$$

源实际对 (4) 的全部因子乘回，并对两个剩余多项式实行扩展 Euclid，逐项验证

$$
A(u)R_{44}(u)+B(u)R_{45}(u)=1
\quad\text{于 }\mathbb Q[u].
\tag{5}
$$

R44/R45 的唯一规范定义是 (1)–(4) 及源码的单项式次序/清分母约定；其完整系数均由自含源生成，不把可重算大矩阵作为证据文件。

若有任一原点，由 (2) 的非零核列使 (3) 两个行列式同时为零；原单位非零再由 (4) 强迫 R44=R45=0，与完整 QQ 恒等式 (5) 矛盾。故排除的是整条 H1=0 的所有复点，包含全部 finite-coordinate 退化和任何计算主元零点。

## 4. 实际源、哈希与范围

- 自含源：notes/2026-11-27-unit211-general-ell-zero-H1-whole-original-Macaulay-return-8542.py。
- 实际源 SHA256：9fdb2e991def1cf337ad9de961b696563e0f48b9a64dab1eeb23beaa30c66eae。
- 原 48×35 输入 SHA256：95a078fe60e3edcb33ce5508e62bf1a62e1e2b698b4ae0181cca0e0fb612f443。
- 两个完整行列式 SHA256：
  f207c94d10fc2ebfcd41483b423fb4ba67622ef9b5ca8890495d6012768fae5e；
  a41283732ad1375f4b3911393be490266442c2829a6be49fb9b49a03e99b35fa。
- 两个剩余多项式 SHA256：
  2e4d1926da046d91ed4cd212b97fd134b727c5457fcda5ce0be3985764d73696；
  e084e60c2cb1ac74cd6610f3b0df7b1065f31fd542c29345f029dab67a566732。
- Python 3.12.14 / python-flint 0.9.0，单线程，120 秒/1 GiB。实际 2026-11-27 06:35:57 UTC 开始，驱动 0.616868039 秒，源末标记 0.480427929 秒，峰值子进程 RSS 30020 KiB，exit 0。
- 小回执：notes/2026-11-27-unit211-general-ell-zero-H1-original-execution-8542.json。

附存此前实际完成的新一般 ell=0 原四二次头 atlas（源 6e7d8506、驱动 0.265913369 秒、RSS 30464 KiB、exit 0），保全部 15 个头和原 mean 变换。其所选 (x²,xy,xt,t²) 头的未付因子是 H1 与 H2=uQ−2u−2Q+2。本条仅关闭 H1；H2 的独立整支证明另行登记，不以 atlas 的多元 gcd 作空性推断。

