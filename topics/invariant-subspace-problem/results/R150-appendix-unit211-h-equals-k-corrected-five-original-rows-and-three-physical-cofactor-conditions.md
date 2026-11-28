# R150 补充：h=k 的正确五原行、三完整 cofactor 与物理因子

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 范围与结论

旧 compact E1 把对偶平方的一阶分量写错；其 R2 后继的原必要性已在[定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md)撤回。本稿从真正的 R2 和独立正确的原均值、N4 极化重新建立 h=k 的同点条件，不恢复旧 Q 六次、235170 界或旧碰撞投影。

固定原 h=k 值图，定义
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,
$$
$$
\ell=A^3/B^2,\quad T=A^2/B,\quad
h=k=1+\xi,\quad w=\lambda-1-T.
$$
本次计算的坐标图仅为
$$
ABQ(1-Q)P_f\ne0. \tag{1}
$$
原物理范围另保 $bcP_{02}\ne0$。所有不在 (1) 内的图按原来源独立处理；本稿不倒置 $\Phi,\Delta,u-\ell,T_0$ 的新独立因子或任一待查头。

本次完整返回五条同一 $z=Qt$ 的原行及三个原 cofactor。三个必要多项式在原物理范围中可准确化为
$$
F_{61,17,9}=F_{76,20,10}=F_{60,16,8}=0. \tag{2}
$$
下标为 $(\lambda,u,Q)$ 次数。它们由 §4 的确定性原行、因式商及完整 SHA 唯一定义。这里只得到三个必要条件，没有排空整个坐标图、没有有限点数或首项单位结论。

## 2. 同一原坐标和真实恢复

置
$$
\delta=1-Q,\quad m=u-\ell,\quad a=1-\ell,\quad
bc=\frac14\left(\ell^2-\frac{m^2}{\delta}\right),
$$
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,\quad \Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad P_f=T_0(J-Q),
$$
$$
G=\lambda P_{02}+(u-1)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0.
$$
原 P1 在 (1) 上给唯一的同点仿射式
$$
f=-\frac{P_c+bc\Phi z}{P_f},\quad
v_n=Jf-G+bc\,z,\quad V=v_n/Q,\quad
W_*=T_0+4uf,\quad N=QW_*-2v_n. \tag{3}
$$
它们来自原 E0、N0、P1；没有把不同投影根的 f、z 拼在一起。

为明确原恢复，可保整个 $\rho^2=\delta$，令 $p=1+\rho,q=1-\rho$，
$b+c=\ell,\rho(b-c)=m$。同一 $X,Y$ 由
$$
bX+cY=V,\qquad bpX+cqY=W_*/2
$$
恢复。再令
$$
r=X-ap-ct,\quad s=Y-aq-bt,\quad A_1=2f-2V+2bc\,t.
$$
原四行 Gram 恰为
$$
g_0=(0,0,p,q),\quad g_1=(0,A_1,r,s),\quad
g_B=(p,r,0,t),\quad g_C=(q,s,t,0).
$$
全程使用
$$
(xy)_1=x_0y_1+x_1y_0,\qquad
\tau(x)=ax_0+x_1+bx_B+cx_C.
$$
令 $d=DK(\mathbf1)$，$DK(v)_j=\tau(g_jv)$，则 $F_2=\tau(d)=2f$。原式为
$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)-4\tau(v)\tau(dv)
       +2F_2\tau(v)^2+\tau(vDK(v)).
$$
原 $P_j$ 是中心化三次型在 $g_0,g_1$ 上的一阶极化。源码完整核回
$$
Q(P_j/3-wP_{02})=P_ff+P_c+bc\Phi z=0. \tag{4}
$$

## 3. 五条真正原行与不除 Delta 的 N(V)

第一行必须取
$$
R_{\rm true}=4Q(f-u)(v_n-Qf)+bc\,z^2
 +z(4bc\,uQ-\ell v_n)+\frac{m}{2\delta}zN. \tag{5}
$$
它是真实原 R2 除 $2\rho$ 的结果。其余三条二次行取独立正确的
$$
W=W_4/(4\delta),\qquad O=\overline O,\qquad
N_1^*=4bc\delta Q^2\left(N_{\rm polar}-\frac{4\lambda}{3}P_j\right).
\tag{6}
$$
$W_4,\overline O$ 的完整原公式见[更正后的四行](R150-appendix-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads.md)及本次自含源；本次将一般 $\ell,T$ 代入 (3)，没有假设 $\Phi=0$。$N_{\rm polar}=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)$。

第五行来自完整原孤立值向量 $\mathcal V=(1,w,h,h)$。定义
$$
\eta=\xi+3-2\lambda,\quad S=2\xi+3-2\lambda,
$$
$$
N_F=(3-4\lambda)Q+J\xi\eta,\quad
N_C=\eta(-G\xi+Qwu),\quad
NV=N_Ff+bcS\xi z+N_C.
$$
原三矩为 $\tau(\mathcal V)=\lambda,\tau(\mathcal V^2)=2\lambda^2,
\tau(\mathcal V^3)=4\lambda^3$，均完整返回。直接同点迹给
$$
\tau(d\mathcal V)=2f+uw+\xi V,
$$
$$
\tau(d\mathcal V^2)=2f+2uw+(2\xi+\xi^2)V,
$$
$$
\tau(\mathcal VDK(\mathcal V))
=2f+2\xi V+2hu w+2bc\xi^2t.
$$
代回完整 N4 定义，F2 项正好相消，得到
$$
QN_4(\mathcal V)=2NV. \tag{7}
$$
所以 NV 确为原必要行。令
$$
\Delta=\Phi N_F-S\xi P_f,\qquad T_{\rm num}=P_fN_C-P_cN_F.
$$
还实际返回
$$
P_fNV=T_{\rm num}-bc\Delta z. \tag{8}
$$
式 (8) 没有除 $\Delta$，故其整个零面仍包含在本次五行模型中。

## 4. 全原 cofactor 与确定性因式

按次序 $(R_{\rm true},W,O,N_1^*,NV)$，把五条原式在 $(1,z,z^2)$ 上取系数。每行先取其完整分母的最小公倍数，再只从所有系数的共同内容中删除 (1) 的实际因子，最后以首个非零系数的首项有理数归一。源码对全部十五个系数逐项重建原有理式，且核验所有分母只受 (1) 支持。

选三组固定原行：
$$
(R_{\rm true},W,O),\quad
(R_{\rm true},W,N_1^*),\quad
(NV,R_{\rm true},W).
$$
若某组三行依次为 $r_i=(r_{i0},r_{i1},r_{i2})$，令
$$
c_0=r_{11}r_{22}-r_{12}r_{21},\quad
c_1=r_{21}r_{02}-r_{22}r_{01},\quad
c_2=r_{01}r_{12}-r_{02}r_{11}.
$$
每组均实际完整返回
$$
\sum_i c_ir_i=(D_j,0,0). \tag{9}
$$
这给同一点原理想中的常数列 $D_j$，不要求任何 z 头非零。按同一 (1) 规则清去 $D_j$ 的已付内容并首项归一，得 $C_j$。完整精确因式乘回为
$$
C_1=\sigma_1(2\lambda-1)^2Z^3F_{61,17,9},
$$
$$
C_2=\sigma_2(2\lambda-1)^2Z^2F_{76,20,10},
$$
$$
C_3=\sigma_3(2\lambda-1)^2Z^2F_{60,16,8}, \tag{10}
$$
其中
$$
\sigma_1=\frac1{56668397794435742564352},\quad
\sigma_2=\frac1{302231454903657293676544},\quad
\sigma_3=\frac1{18446744073709551616}.
$$
三条 $C_j$ 的次数、项数与 SHA 全保[首次实际回执](../notes/2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-execution-8542.json)。

| 剩余因子 | 总次数 | 项数 | 完整规范系数 SHA256 |
|---|---:|---:|---|
| $F_{61,17,9}$ | 79 | 5855 | 69babd37fc45ade649b12b4b849151574080a2bf92c7c2266141d17be1a9d999 |
| $F_{76,20,10}$ | 97 | 8652 | 79b699a63f9715f3c381b9f90ed5083503577553abb97bf89270c18e4afd5cb4 |
| $F_{60,16,8}$ | 77 | 4958 | 6d7e2f49e54cb92cb6bb20f200babf15d8944c5b44c9af9708f5d8652c036473 |

这些因子的定义是 (3)–(10) 的精确多项式商及所列规范。确定性源可以重建；没有把数十万字节系数另存为缓存。

## 5. 两类因子的真正支付

实际共同 39 项因子严格等于
$$
Z=B^4u^2-2A^3B^2u+A^6Q
 =-B^4M=-4B^4bc(1-Q),\qquad M=\ell(2u-\ell Q)-u^2. \tag{11}
$$
其规范 SHA 为 616854de20930ab2387031433e732b543840efaf22697156454c83a455570b08。根会话把第一次已得因子的全部 39 项与 (11) 交叉核回；没有重跑五行门。最后两个等号直接由 $\ell=A^3/B^2$ 和原权恒等式给出。所以 Z 在指定原物理图上非零，这是直接原权身份，不借旧错误头的单位。

另一个因子 $2\lambda-1$ 的完整物理排除早已由前会话
[S0 等值 lambda-half 原证明](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-equal-values-lambda-half-exclusion.md)
支付。这里已重读正文及其正确原 vm 源 0f6fbabe15135c7408a8649fad551eab9b80039a：

- $t\ne0$ 由四条完整原 E/P 恒等式矛盾；
- $t=0$ 确有抽象必要族，必须补回同一第五物理列，五列 Gram 秩二与非退化六维空间中的必需秩至少四矛盾。

该旧结论独立于本会话的 compact 错误，直接复用而不再执行。它是物理原点排除，不能被改写为未构造的裸多项式单位理想。

于是实际物理点上可从 (10) 删除这两个非零因子，得到 (2)。没有由三变量多项式的 gcd 或不可约性推断公共点不存在。

## 6. 首次实际身份与后续范围

自含源：
[2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py](../notes/2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py)。

- 源 blob f33fef3b7448eb3b7d829cb7deb047706f08294d，11368 字节。
- SHA256 2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2。
- run 46106955780 / job 140861753869；3.386197837 秒、94280 KiB、内部 exit 0。
- 全十五原系数、三组完整 cofactor、全部因式返回；212 次精确整除返回。
- source commit db82b18cde7669eeb6086873b33d4319680bd69e。
- 04:19:09.795163 UTC 实际 pull 至 07a9aa283f5d57e11ad6daca9820bf01352a600b，两 README 无变化。
- stdout 14614 字节，SHA256 a273554ecd682269747a1f8630bd89f5f2bd800ff222b14c7cf04ce600642999。

本次完整保原 $\Delta=0$ 及其它未支付权面；所有旧独立已成结论只按核实的原范围复用。余下原单点 N/P 条件、物理第五列和所有坐标边界继续保留。整个 h=k、R150 与普通 Hilbert ISP 均未由本次完成。
