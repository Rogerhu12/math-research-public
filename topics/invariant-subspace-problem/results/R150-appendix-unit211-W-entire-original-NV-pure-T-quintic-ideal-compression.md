# R150：完整原 N4(V) 的纯 T 五次替换与无 D 逆的原理想身份

会话 Astra-ISP-8542378f-20261127，2026-11-27。当前原一般 LS、Delta=0、W=0 的已付局部化域。以下完整纸面推导与新源实际原式乘回均已完成；全部新参数首项零面仍保留，本结果不排空 W。

## 1. 保留的原定义

沿用全 W 首一 T 三次/F 二次环境及已核十一条原行。记

$$
d=1-Q,\quad m=u-\ell,\quad M=\ell^2d-m^2,\quad c_\lambda=3-2\lambda,
$$

$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$

$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell T A_\lambda+2T^3.
$$

令

$$
G=\lambda P_{02}-(1-u)T_0,\quad
w=\lambda-1-T,\quad
P_c=QP_{02}(\ell+T)-G T_0,\quad
g_y=u-\ell Q.
$$

原 P1 在已付仿射重建中准确为

$$
P_f f+\Phi bcQt+P_c=0,\qquad
P_f=T_0(J-Q),\quad P_f=\Phi(J-2uQ).
$$

引入同一个原值中心 s：

$$
v_0=(T+ms)/\ell,\quad
\zeta=v_0+s,\quad S_v=2v_0+c_\lambda,
$$

$$
V=V_0+sV_1,\quad
V_0=(1,w,1+T/\ell,1+T/\ell),\quad
V_1=(0,0,m/\ell-r,m/\ell+r),\quad r^2=d.
$$

第二矩误差为

$$
H_2=Ms^2-D,\qquad \tau(V^2)-2\lambda^2=H_2/\ell.
$$

完整原二次型写为

$$
N_4(V)=Z_0+Z_1s+Z_2s^2,
$$

其中 Z0=N4(V0)、Z2=N4(V1)、Z1=N4(V0+V1)-Z0-Z2。此前十一行的完整 NV 行为

$$
V_{\rm low}=DZ_0+\frac K{2m}Z_1+\frac{D^2}{M}Z_2.
$$

这不是从 N4(V) 中选取一个加权迹。

## 2. 直接从原 Gram 展开的两线身份

为避免把第二矩误差隐去，定义

$$
Z=v_0(v_0+c_\lambda)+ds^2,\quad
U_c=\ell Z-msS_v,\quad V_c=mZ-\ell dsS_v.
$$

原 E0/N0 重建的两条线为

$$
ux+g_yy=2uf+T_0/2,\qquad
V_2x+C_yy=\lambda P_{02}+uT_0+(V_2+2u^2)f-bcQt,
$$

其中 V2=2u-ell Q、Cy=2u-uQ-ell Q。直接乘开有

$$
C_yU_c-V_2V_c=M\{2Z+(2-Q)sS_v\},
$$

$$
g_yU_c-uV_c=M(Z+sS_v).
$$

按同一个原 Frobenius 乘法展开整个 N4(V)，而非先令第二矩为零，得到

$$
\frac Q2N_4(V)=N_f f+bcQ S_v\zeta t+N_c-\frac{Qf}{\ell}H_2,
$$

其中

$$
N_f=(3-4\lambda)Q+2QU_c+T_0(Z+sS_v),
$$

$$
N_c=-G(Z+sS_v)-\frac{QT_0}{2}sS_v
+Qw\{u(v_0+c_\lambda)-g_ys\}.
$$

故在完整 P1 恢复之后，

$$
C:=\Phi N_c-S_v\zeta P_c
=\frac{\Phi Q}{2}N_4(V)-\Phi L_\Delta f
+\frac{\Phi Qf}{\ell}H_2,
$$

这里 W 原身份给

$$
L_\Delta=N_f-S_v\zeta(J-2uQ)
=(3-4\lambda)Q+(4uQ-J)v_0^2
+2uQc_\lambda v_0+Jds^2.
$$

该恒等式保留 H2，不能删去误差项后声称自由变量恒等。

## 3. 原纯值五次的完整定义

置

$$
a=-\Phi G-2P_c,\qquad
b=c_\lambda(-\Phi G-P_c)+\Phi Qwu,\qquad
c_0=\Phi Qwu c_\lambda,
$$

$$
c_s=-\Phi G-\Phi QT_0/2-P_c.
$$

则完整相容式 C 正是

$$
C=a v_0^2+b v_0+c_0-\Phi Gds^2
+c_s s(2v_0+c_\lambda)-\Phi Qwg_ys.
$$

定义纯 T 多项式

$$
a_C=M(aT^2+b\ell T+c_0\ell^2)
+\{am^2-\Phi Gd\ell^2+2c_sm\ell\}D,
$$

$$
b_C=M\{2amT+bm\ell+c_s(2\ell T+c_\lambda\ell^2)
-\Phi Qwg_y\ell^2\},
$$

$$
C_5=2mDa_C+Kb_C.
$$

全部定义只使用此前已付分母。若 KC=am²-Phi Gdell²+2cs mell，则直接代入 v0 给

$$
M\ell^2 C=a_C+b_Cs+K_C H_2.
$$

相同地，旧原 Delta 多项式 aD、bD 满足

$$
M\ell^2L_\Delta=a_D+b_Ds+C_*H_2,
\qquad C_4=2mDa_D+Kb_D.
$$

将第二节恒等式在首一关系 Ms²=D 下精确约化，再乘 2mD、代入同一个 s=K/(2mD)，所有分母消失，得到完整原多项式恒等式

$$
\boxed{C_5+\Phi fC_4=m\Phi QM\ell^2V_{\rm low}.}
$$

最终两侧都在原 F,S,lambda 多项式环中；导出时的形式清分母不把 D 支变成新删去的纤维。该式在 D=0 处也保持多项式意义。新源已经在 qF/q3 约化之前，把原 N4 构造的三 Z 与此等式全部逐项相乘核回。

mPhiQMell² 是当前域已付单位，故有准确理想等式

$$
(C_4,V_{\rm low})=(C_4,C_5).
$$

因此在已发表完整十一条原输入中，把整个 Vlow 换成 C5，保留其它原行，理想不变。此前十一行与十三行之间使用原 D 非零域的范围仍原样保留；新等式不将其外推到另行处理的 h=k 碰撞域。

## 4. 全局首一五次与三列返回

直接收集 C5 的 T 五次系数，使用 m+ell=u、M+m²=ell²d，得

$$
[T^5]C_5=-4uQP_{02}\ell^2d.
$$

各因子均已付，故 C5 确实给全当前 W 的首一 T 五次 q5。它不依赖 A143、B239 或任何新的 lambda 首项被支付。按原首一 q3 约化：

$$
q_5=\overline q_5+Uq_3,\qquad \deg_S\overline q_5\le2.
$$

这是完整 NV 的无 F 原余式。保留 r2 即保留原 C4，故可以直接与先前的 r2、S r2、H01、H02 在同一真实 (1,S,S²) 值列上进行新 cofactor 运算。

## 5. 三个新原常数余子式

本次把 q5 的完整 q3 余式清理为三列行 C5，保留原 r2、S r2、H01、H02。对下面三组，各自实际构造 gamma 并核回全部三个列：

$$
\gamma^{\mathsf T}\mathcal M=(C_{\rm raw},0,0).
$$

每个原点使用同一个 (1,S,S²)，故 C_raw 必为零。只去此前已付因子和非零有理常数，得到下表完整原必要多项式 C：

| 原三行 | C 次数 (e,k,lambda) | 项数 | 总次数 |
|---|---:|---:|---:|
| r2, S r2, C5 | (28,34,14) | 11061 | 64 |
| r2, H01, C5 | (36,46,12) | 16532 | 77 |
| H01, H02, C5 | (43,55,11) | 21565 | 89 |

三条规范系数 SHA256 依次为：

- 8ff2998eff71b6560b3afa13328c8b26f1ec5486bc4193e0c4ebfe43fd61e13c；
- 472a729513c46812d1548bccee0f5d8f4dbe4ea51cb842d9e39c03fb1f30114b；
- 6e0fd9d56ca2db23a5838047778b390d6da7e7d0ba5bfbb6227df53f25d547ce。

它们对 lambda 的首项在只去已付因子后，分别仍有 (e,k) 次数 (23,29)、(27,34)、(30,36)，项数 508、734、858 的未付余式。三条整首项零面都保留，未将任何一条参数多项式全域首一化。

未约化纯 C5 只有六个 T/S 项，完整系数编码 82424 字节，SHA256 8b9974d7919061f9c1972cb265d5bcd78df98f47cf624160e0c67593b0e78c0b。其首一 q3 二次余式编码 368018 字节，SHA256 b929c780ac63dc7fd5637d023bf6be95e25dcdda156b6e47d8b733aeebc04954；三个原常数余子式的完整乘回证书与剥除证书摘要见小回执。全部大系数只在本次内存中构造，不存可重算缓存。

## 6. 唯一实际执行与来源

源码：

[2026-11-27-unit211-W-entire-original-NV-pure-T-quintic-three-column-minors-8542.py](../notes/2026-11-27-unit211-W-entire-original-NV-pure-T-quintic-three-column-minors-8542.py)

SHA256 da64f23af9b938e60c5aa3978b066098d88104093c412878e5b0278f873d79e9，6447 字节，blob 7d3b7e37a8505185e556b2739b70b8fd7194a12b。它只执行 f5c0226e 已有构造前缀及其固定依赖，未重跑旧 cofactor 门；完整原 N4 重新构造是为了本次新的未约化多项式身份。

实际 run 46035666635、job 140630333376，inner exit 0：

- 完整原 N4 未约化新身份、T5 已付首项及三个新 cofactor：6.161249033 秒；
- 驱动墙钟 6.202216625 秒；
- 峰值 RSS 102740 KiB；
- stdout 8297 字节，SHA256 2389d3ddd7b5866ee30353a63ba1fcaf60e83884f80c83e7f9c35cf9e58a85ac；
- 资源上限 180 秒、4 GiB。

真实 pull 在 2026-11-27 16:41:18.328199 UTC 完成，前后 main 均为 d3f79177517cd88f1b7dbdd2245409acdc0e708b，两 README blob 未变。完整数学输出与驱动回执见同 stem 的 receipt JSON。

前置结果：

- [全 W 原首一 T3/F2 环境](R150-appendix-unit211-W-global-monic-T-three-F-two-and-six-column-environment.md)；
- [完整奇 N/P 与完整 NV 的低 D 理想压缩](R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)；
- [完整十一条原行六列返回](R150-appendix-unit211-W-global-D-linear-eleven-original-six-column-return.md)；
- [原四行三列耦合](R150-appendix-unit211-W-coupled-original-Gram-value-four-by-three-complete-minors.md)。

结论只替换完整 NV 并给三条新原必要参数式。原个别 N/P 和所有其它原条件仍保留，不据多变量 gcd 或单个模点宣称排空。
