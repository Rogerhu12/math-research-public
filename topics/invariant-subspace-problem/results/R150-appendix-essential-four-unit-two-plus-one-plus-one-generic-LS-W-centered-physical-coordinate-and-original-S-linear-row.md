# R150：一般 LS 的 W=0 图上的原物理仿射坐标与 N1 的 S 二次项消去

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。

## 1. 精确范围与结论

本附录在此前已登记的一般 LS、Delta=0、W=0 权图工作。旧 L0、S0、k=-1 和 H=0 已闭；本附录不重新证明这些结论，不把它们的 U 值参数与本处的权参数混同。

设

$$
e=u-1,\quad Q=ek,\quad V=(e+1)k+2,\quad
\ell=\frac{(e+1)((k+2)^2-2ek)}{kV},\quad
H=4ek-k^2-4k-8.
$$

除原物理单位外，本图只使用已经支付的 k+1 与 H。尤其不把 ell、k+2、J19、C9 或任何新的系数当作单位。

本附录给出两个原式结论：

1. 从已登记的有限 Gram 坐标 (x,y,t) 到

$$
F=2f-u\lambda,\qquad \lambda,\qquad S=T-2\lambda
$$

的仿射变换在整个当前图上可逆；其逆只使用原物理单位，不需要旧四二次或三次头子式。

2. 原四个二次必要式可由可逆原行组合改写为

$$
E_1,\qquad R_y,\qquad R_t,\qquad R_N=N_1-2eE_1,
$$

且 R_N 对 S 至多一次。该消去是完整原多项式恒等式，在 ell=0 等新首项零面同样成立。

这只是原输入的降次和坐标覆盖，不是一般 W 有限点排空。R_N 的 S 一次系数为零时必须保留整支，不能用本附录直接解 S。

## 2. 原权、Gram 及必要式的再生定义

令 d=1-Q，r^2=d，p=1+r，q=1-r，

$$
b=\frac{\ell}{2}+\frac{u-\ell}{2d}r,\qquad
c=\frac{\ell}{2}-\frac{u-\ell}{2d}r,\qquad a=1-\ell,
$$

并设

$$
V_2=2u-\ell Q,\quad
T_0=V_2-2u^2,\quad
P_{02}=(2-3u)V_2-Qu+2u^3,
$$

$$
J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q),\quad
M=\ell V_2-u^2=4bc(1-Q).
$$

当前图中 u、Q、1-Q、bc、P02、Phi 都是原物理单位。W 权关系为

$$
\Phi(J-2uQ)-P_f=0.
$$

令 X=x+yr，Y=x-yr，并定义

$$
f=\frac{ux+(u-\ell Q)y-T_0/2}{2u},\qquad
W_2=V_2x+(2u-uQ-\ell Q)y,
$$

$$
\lambda=\frac{W_2-uT_0-(V_2+2u^2)f+bcQt}{P_{02}},
$$

$$
T=\frac{[\lambda P_{02}-(1-u)T_0]T_0-P_f f-\Phi bcQt}
        {QP_{02}}-\ell.
$$

原 Gram 的四行是

$$
g_0=(0,0,p,q),\quad
g_1=(0,A_G,R_G,S_G),\quad
g_2=(p,R_G,0,t),\quad
g_3=(q,S_G,t,0),
$$

其中

$$
R_G=X-ap-ct,\quad S_G=Y-aq-bt,\quad
A_G=2f-2bX-2cY+2bct.
$$

使用原代数乘法

$$
v z=(v_0z_0,\ v_0z_1+v_1z_0,\ v_2z_2,\ v_3z_3),
\quad {\bf1}=(1,0,1,1),
$$

$$
\tau(v)=av_0+v_1+bv_2+cv_3,\qquad
K(v)_j=\tau(g_jv),\qquad D=K({\bf1}),\quad F_2=\tau(D)=2f.
$$

原 mean 式为

$$
E_j=\epsilon_j-2K(D)_j-2(D^2)_j+2F_2D_j,
$$

其中 epsilon1=2 tau(g0 g1)，其余 epsilonj=tau(gj^2)。本重建满足 E0=0，E1 属基域，E2=EBe+r EBo，E3=EBe-r EBo。

定义原

$$
\mathcal N(v)=2\tau(Dv^2)-F_2\tau(v^2)
-4\tau(v)\tau(Dv)+2F_2\tau(v)^2+\tau(vK(v)),
$$

$$
\mathcal P(v)=\tau((v-\tau(v){\bf1})^3),
$$

$$
P_j=3\tau((g_0-\tau(g_0){\bf1})^2
             (g_1-\tau(g_1){\bf1})).
$$

则本附录的原 N1 为

$$
N_1=\mathcal N(g_0+g_1)-\mathcal N(g_0)-\mathcal N(g_1)
       -\frac43\lambda P_j.
$$

源码实际逐项返回

$$
\mathcal N(g_0)=2\lambda P_{02},\quad
P_j=3(\lambda-1-T)P_{02},\quad \mathcal P(g_0)=P_{02}.
$$

令 A2=2lambda^2-2lambda+1，B3=4lambda^3-6lambda^2+3lambda-1，原加权必要式为

$$
N_s=b\mathcal N(g_2)+c\mathcal N(g_3)
      -2\lambda P_{02}(\ell+2T+A_2),
$$

$$
P_s=b\mathcal P(g_2)+c\mathcal P(g_3)
      -P_{02}(\ell+3T+3A_2+B_3).
$$

它们也从同一个完整原 Gram 重建。代码保留与 HA、HB 的原加权差值身份；没有把加权必要式冒充全部原值方程的充分条件。

## 3. 整图可逆的原物理坐标

给定独立 F、lambda、S，先令 f=(F+u lambda)/2，T=S+2lambda，并置

$$
t=\frac{T_0[\lambda P_{02}-(1-u)T_0]-P_f f
                  -QP_{02}(T+\ell)}{\Phi bcQ},
$$

$$
g=2uf+T_0/2,\qquad
W_2=\lambda P_{02}+uT_0+(V_2+2u^2)f-bcQt.
$$

记 gy=u-ell Q，Cy=2u-uQ-ell Q。有完整参数恒等式

$$
uC_y-g_yV_2=QM.
$$

于是

$$
x=\frac{C_y g-g_yW_2}{QM},\qquad
y=\frac{uW_2-V_2g}{QM}.
$$

直接乘回分别得到 ux+gy y=g 和 V2 x+Cy y=W2，再由原定义得到同一个 f、lambda、T。因此这是原仿射变换的双侧逆，不是投影后另选的相位解。

Jacobian 为

$$
\det\frac{\partial(F,\lambda,S)}{\partial(x,y,t)}
=-\frac{\Phi bcQM}{uP_{02}^2},
$$

其每一因子均已支付。这里不倒置 x-u-1 或任何头子式。实际 Actions 源对所有这些乘回均有断言，并在其后才形成原 mean/N/P 多项式。

## 4. 原行组合及 S 二次项的全图消去

令 nu=(u-ell Q)/u，定义

$$
R_t=\frac{u}{2bc}\left(EBo+\frac{\nu}{d}EBe\right),
\qquad
R_y=-EBe+\frac{\ell}{2}R_t.
$$

其逆为

$$
EBe=-R_y+\frac{\ell}{2}R_t,\qquad
EBo=\frac{2bc}{u}R_t-\frac{\nu}{d}EBe.
$$

所用分母 2、u、bc、d 均已支付；没有除 ell。因此，连同 N1=RN+2e E1，在当前局部环中有四行原理想等式

$$
(E_1,EBe,EBo,N_1)=(E_1,R_y,R_t,R_N).
$$

证明 RN 的 S 二次项恒零，可以只考察固定 f、lambda 的齐次变化。此时原线性重建给出

$$
bpX_h+cqY_h=0,\quad
Y_h=-\frac{bp}{cq}X_h,\quad
t_h=-\frac{p-q}{cq}X_h.
$$

所有此处的分母都是原物理单位。把这一个方向代入完整原 Gram 的二次头，直接展开得

$$
E_1^h=-\frac{2bp\ell}{cq}X_h^2,\qquad
N_1^h=\frac{4bp\ell(1-u)}{cq}X_h^2
       =2(u-1)E_1^h.
$$

故原多项式 N1-2e E1 的 S^2 系数恒零。这是乘法恒等式；不需要把 E1 的 S^2 系数当作单位。当 ell=0 时两边一同为零，结论仍成立。

完整计算实际得到 [S^2]N1 / [S^2]E1 = 2e，分母为 1，并另行核验 2e [S^2]E1=[S^2]N1 以及 RN+2e E1=N1。四个新原二次行的 S 次数依次为 2、2、2、1。

## 5. 新零面的准确保留

对 RN 作仅含当前已付单位的原行归一化后，FS 系数剥去已付因子，只余

$$
-4L_\ell,\qquad L_\ell=2ek-(k+2)^2,\qquad
\ell=-\frac{uL_\ell}{kV}.
$$

因此该系数是 ell 乘当前局部环的单位。lambda S 系数同样含 Lell，另含日志中完整列出的十二项参数因子。S 的常数系数另有十九项参数因子。源码逐个原系数作因式乘回及已付除法乘回；这些结果都不授权去掉 ell=0 或整个 S 一次系数零面。

完整四个 lambda^2 轴系数也逐个提取并返回。既有最高次定理说明一个原有限解若对应四个头共同非零方向，则落在已闭的共同二次权纤维；它不使任何单个轴系数自动成为单位。因此本附录没有倒置任何单个轴系数。

下一项原消元可以在 RN 的 S 系数非零图解 S，并须同时处理其全零图。一般 W 有限系统、ell=0 权线、u=Q 权线，以及 J19/C9 未付零面均未因本附录而关闭。

## 6. 实际执行、可再生输入与边界

自含源：

- notes/2026-11-27-unit211-generic-LS-W-centered-physical-original-low-structure-8542.py
- Git blob bba2aea4fbd64d3fcb8f3c35c03fb381b785db4f。
- 源 SHA256：60a4c4cf72a7019cbe970ef8e7442ce88c8a93fb54012734cd522d9a136d4fcb。

唯一首次实际 Actions：run 45946296920 / job 140331658496。源耗时 1.135421917 秒，驱动 1.202463626 秒，最大子进程 RSS 47484 KiB，退出码 0。边界是 180 秒、4 GiB；没有运行旧参数 cofactor 展开或 Gröbner 门。

stdout 32931 字节，SHA256：

03d077c15dcd5fef9ccc468bf0f46ccca982e5c95048a10011c3aedef16f345b

实际 pull 时间 2026-11-27 05:31:39.517475 UTC，前后提交同为 93da1df43729ffe1914a8c5e6b146ef5fab6e11c。根 README blob 282e86b03385d3b6245ce7100ae2e2af7b103c2d，课题 README blob 5fbd905291dd044c88d35bd9c07ac0e586ff795a，均未变化。

本次成功标记同时确认原可逆坐标、原 Gram/E0/N0/P1、加权 N/P 迹、四原行可逆组合、S 二次项取消、仅已付单位的归一化，以及所有新系数零面的保留。普通 ISP 的完成状态不变。

实际执行小回执及原系数摘要见[已登记回执](../notes/2026-11-27-unit211-W-centered-physical-actual-execution-8542.json)。
