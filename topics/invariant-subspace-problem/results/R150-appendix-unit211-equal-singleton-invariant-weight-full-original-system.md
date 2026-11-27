# R150：h=k 值碰撞的权不变量坐标与完整八条原条件

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted GPT-6 Astra Pro。

## 1. 范围和本次结果

继续[原完整 Gram 与 Delta 四次式](R150-appendix-unit211-equal-singleton-values-full-original-Gram-and-Delta-quartic.md)的 h=k≠1 碰撞图。这里只在 Delta≠0 图解两条原线性式；Delta=0 仍由已付首一 b 四次式完整保留。

本次把同一个原点从 (lambda,b,rho) 改写为 (lambda,u,Q)，保留 rho²=1−Q 的两分量表示。全部八条原条件精确返回为八条有理系数标量式；每一个单点行的偶/奇拆分都同时使用原 B、C 两行。因此没有把一个代数扩张中的单方程擅自拆成系数为零。

本次只是原输入的准确改写，不宣称此三参数图有限、为空或已得单位。特别原物理 D=0，旧依赖 D≠0 的等权或其它权排除不能移用到这里。

## 2. 权坐标及两条原线性式

沿用旧 moment 参数：
$$
A=2\lambda^2-2\lambda+1,\qquad B=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
\xi=B/A,\quad \ell=A^3/B^2,\quad
T=A^2/B,\quad w=\lambda-1-T,\quad h=k=1+\xi .
$$
这些是旧原值分层，不计作新结论。原 moment 已保证 A、B 非零。

设
$$
d=1-Q=\rho^2,\quad p=1+\rho,\quad q=1-\rho,\quad
b=\frac{\ell}{2}+\frac{u-\ell}{2d}\rho,\quad
c=\frac{\ell}{2}-\frac{u-\ell}{2d}\rho .
$$
则
$$
b+c=\ell,\quad bp+cq=u,\quad pq=Q,\quad
bc=\frac14\left(\ell^2-\frac{(u-\ell)^2}{d}\right).
$$
原图保持 rho、Q、bc 非零。这里 u=ell 恰 b=c，仍包含于待处理原图。

记
$$
\begin{aligned}
V_2&=2u-\ell Q,&T_0&=V_2-2u^2,\\
J&=2u(1-u)+\ell Q,&\Phi&=T_0+4u-4+Q,\\
P_{02}&=(2-3u)V_2-Qu+2u^3,&P_f&=T_0(J-Q),\\
G_0&=\lambda P_{02}-(1-u)T_0,&
P_c&=QP_{02}(\ell+T)-G_0T_0,\\
S&=2\xi+3-2\lambda,&\eta&=\xi+3-2\lambda,\\
N_f&=(3-4\lambda)Q+J\xi\eta,&
N_c&=\eta(-G_0\xi+Qwu).
\end{aligned}
$$
定义
$$
\Delta=\Phi N_f-S\xi P_f,\quad
F=S\xi P_c-\Phi N_c,\quad
T_{\rm num}=P_fN_c-P_cN_f.
$$
源码完整核对
$$
P_fF+\Phi T_{\rm num}+P_c\Delta=0,\qquad
N_fF+S\xi T_{\rm num}+N_c\Delta=0.
$$
在当前 Delta≠0 图，
$$
f=F/\Delta,\qquad t=T_{\rm num}/(bcQ\Delta).
$$
只用同一个缩放
$$
H=bc\Delta,\quad f_H=bcF,\quad t_H=T_{\rm num}/Q.
$$
没有倒置 T0、Pf、S、D 或一个范数。

## 3. 完整 Gram 的权不变量重建

在形式代数 R[rho]/(rho²−d) 中，令
$$
\begin{aligned}
W_{1P}&=\tfrac12T_0\Delta+2uF,\\
W_{2P}&=(uT_0+\lambda P_{02})\Delta+(V_2+2u^2)F-T_{\rm num},\\
\iota&=-\rho/(2d),\qquad \iota(q-p)=1,\\
X_H&=cq\iota(qW_{1P}-W_{2P})/Q,\\
Y_H&=bp\iota(W_{2P}-pW_{1P})/Q .
\end{aligned}
$$
令 a=1−ell，并置
$$
r_H=X_H-apH-ct_H,\quad
s_H=Y_H-aqH-bt_H,\quad
A_H=2f_H-2bX_H-2cY_H+2bc\,t_H.
$$
同一点原缩放 Gram 为
$$
\widehat K=
\begin{pmatrix}
0&0&pH&qH\\
0&A_H&r_H&s_H\\
pH&r_H&0&t_H\\
qH&s_H&t_H&0
\end{pmatrix}.
$$
源码由原 Frobenius 乘法及同一迹
$$
\tau(v)=av_0+v_1+bv_B+cv_C
$$
重建 mean、N4、P2，而非另拟替代多项式。原 E0、N0、双点最高 jet P1、N4(V) 以及 V=(1,w,h,h) 的三个原 moment 都完整返回。两个单点的梯度目标均是 2lambda P02 h² H³，最高目标均是 P02 h³ H³；没有借用 h=1 图的不同目标。

## 4. 为什么这次允许偶、奇两条标量式

在同一原点，源码准确核对
$$
E_C=\overline{E_B},\quad N_C=\overline{N_B},\quad
P_C=\overline{P_B},
$$
这里横线仅指形式替换 rho→−rho，同时交换 b,c 与 p,q，不是复共轭。若 E_B=e+rho o，则实际原 C 行就是 e−rho o。因为两条实际行都必须为零且 rho≠0，
$$
E_B=E_C=0\quad\Longleftrightarrow\quad e=o=0.
$$
N、P 两对相同。E1 与双点 N1 自身奇部为零。故八原式准确等价于
$$
E_1,E_{Be},E_{Bo},N_1,N_{Be},N_{Bo},P_{Be},P_{Bo}=0.
$$
这个论证保留两条原行；不要求 rho²−d 不可约，也未由一个扩张环等式推出系数全零。

此外保留真实原线性组合
$$
L_{\rm mean}=(u-\ell)E_{Be}+\ell(1-Q)E_{Bo}.
$$
这是原 mean 的标量线性组合，不代替剩余原条件。

## 5. 实际返回的多项式大小

所有标量系数分母逐项核对仅含 A、B、Q、1−Q。清分母后只按真实原单位作 gcd 剥除，并将每次被除因子及全部乘积准确乘回。下面的次数依次为 (lambda,u,Q)，尚未另外剥旧已排除的 lambda=1/2。

| 原标量行 | primitive 次数 | 项数 | 本次剥除 |
|---|---|---:|---|
| E1 | (50,12,6) | 2156 | bc 一次 gcd |
| EBe | (56,13,7) | 2990 | 无 |
| EBo | (56,13,6) | 2585 | 无 |
| N1 | (53,13,6) | 2441 | bc 两次 gcd、Delta 一次 gcd |
| NBe | (76,19,9) | 7255 | bc 一次 gcd |
| NBo | (72,18,8) | 6075 | bc 一次 gcd |
| PBe | (87,21,10) | 9704 | 无 |
| PBo | (81,20,10) | 8127 | 无 |
| Lmean | (50,12,6) | 2459 | bc 一次 gcd |

gcd 循环次数只描述实际除法，不能未经检查改写为某完整多项式的相应幂。每条 raw/primitive 全系数摘要、字节数及 SHA256 保存在附带凭据中，源可再生；未保存较大可重算系数缓存。

## 6. 唯一实际执行与下一原域

[源](../notes/2026-11-27-unit211-equal-singleton-invariant-weight-original-system-8542.py)：
blob d21aec51c80569d8e20c68f8f8c4eb5763a7dc09，8317 字节，SHA256
d718df30a023c60e81f734c5a58305748558af0ea127ce28cecbd9b9b4c44155。

实际 run46001847888/job140515223096，内层 exit0；源 4.953151960 秒，驱动 5.007331983 秒；最大子进程 RSS 67312 KiB。
stdout 7817 字节，SHA256 b3d65e47a324c8d1088e250ad3a6d987524f4d3f34223e71729fcbc52d04c6b8。
实际 main 7bd543fbd1218460bc7cb96113d678bddd165014；12:49:29.142308 UTC 真实 pull 后两 README 无变化。

[完整小凭据](../notes/2026-11-27-unit211-equal-singleton-invariant-weight-original-system-receipt-8542.json)保存所有九个标量输出及 driver 记录。

新的 u=ell 原等权面须独立在 h=k、D=0 图内返回；旧 D≠0 权排除不能替代它。Delta=0 四次图、一般不等权图及物理第五列条件继续保留。普通 ISP 未完成。
