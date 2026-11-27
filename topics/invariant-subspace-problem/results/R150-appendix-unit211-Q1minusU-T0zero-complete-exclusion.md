# Q=1-u 边界上完整 T0=0 原值排除

日期：2026-11-27（Asia/Taipei，UTC+8）  
会话：Astra-ISP-8542378f-20261127；推导：literature_deddens；AI-assisted GPT-6 Astra Pro

## 1. 结论和覆盖范围

在原 essential unit211 的 LS 系统中，加上 $Q=1-u$，不存在满足原物理单位的 $T_0=0$ 解。本结论是完整复参数排除；没有假设等权 $b=c$，也没有把等权图的任何单位移到此处。

只需已登记的 $Q=1-u,\ y=1$ 整支排除（提交 b85db7e9d6bd9c484005cb6788170f2c145892b6）及原单位 $uQMP_{02}D_{\rm val}\ne0$。下文实际除法不使用 $s$、$2u-1$ 或第二均值首项作为单位。

因此在剩余 Q 边界图中，$\ell=uh$ 的 $h-2$ 可以成为已付单位；该权限仅属于本 Q 边界，不是全部一般 LS 的 $T_0=0$ 排除。

## 2. 原行与合法均值坐标

由
$$
T_0=2u-\ell Q-2u^2=Q(2u-\ell)
$$
和 $Q\ne0$ 得 $\ell=2u$。于是
$$
M=u^2(4u-1),\qquad P_{02}=uQ(4u-1).
$$
故 $4u-1$ 是原物理单位。原 $y=1$ 已排，以下 $y-1\ne0$。

为明确原来源，取 $r^2=u$，
$$
a=1-2u,\quad b=u-r/2,\quad c=u+r/2,\quad
p=1+r,\quad q=1-r,\quad X=x+yr,\quad Y=x-yr,
$$
以及
$$
f=\frac{x+(2u-1)y}{2},\quad
r_G=X-ap-ct,\quad s_G=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bct.
$$
原四行 Gram 为
$$
K=\begin{pmatrix}
0&0&p&q\\
0&A_1&r_G&s_G\\
p&r_G&0&t\\
q&s_G&t&0
\end{pmatrix}.
$$
乘法和迹仍为原代数
$\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C$ 上的乘法及
$\tau(v)=av_0+v_1+bv_B+cv_C$。令 $D_Kv=(\tau(k_i v))_i$，
$d=D_K1$，$\tau(d)=2f$。均值行 $E_i$ 及 $N_4$、$P_2$ 均直接从这些原行构成；证书逐项核回原 $E_0,N_0,P_1$，没有把压缩条件当作充分条件。

由于 $y-1$ 已付，新的 $s$ 由
$$
x=u+\frac{y-s(y-1)}2
\tag{2.1}
$$
唯一确定，不丢失任何 $x$。原 $R_{y0}=4bcR_y$ 对 $t$ 的系数为 $M(y-1)$，故在同一原解上
$$
t=\frac{3u-1+(1-2u)y+s(u-y)}u.
\tag{2.2}
$$
证书把 (2.1)–(2.2) 代回完整 $R_{y0}$ 得恒等零。

将原 $E_1$ 仅除已付标量后，恰得
$$
E=4sy^2+(3-4u-6s-s^2)y+4u-2+s+s^2=0.
\tag{2.3}
$$
其 $u$ 系数为 $4(1-y)$，所以
$$
u=\frac{U}{D},\quad
U=4sy^2+(3-6s-s^2)y+s^2+s-2,\quad D=4(y-1).
\tag{2.4}
$$
同一 $u$ 被代回下述全部原行，不另选参数根。

原 $N_0,P_1$ 的解在此权线上另有准确恒等式
$$
\lambda=y+\frac t4,\qquad T=\frac{3t}4-2u.
\tag{2.5}
$$
这两式在自含源中由原 $L_{\rm num},T_{\rm num},P_{02}$ 完整乘回核验。

## 3. 两个原行的完整公共曲线

取原
$$
R_{t0}=uE_{Bo}+(2u-1)E_{Be}
$$
和原
$$
N_H=P_{02}\{N_4(k_0+k_1)-N_4(k_0)-N_4(k_1)\}
-\frac43L_{\rm num}P_j,
$$
其中 $P_j=3\tau((k_0-\tau(k_0)1)^2(k_1-\tau(k_1)1))$。

依次代入 (2.1)–(2.4)，清除已付分母，并取非零有理标量的 primitive 规范后，实际得到
$$
R=g\bar R,\qquad N_H=g\bar N,\qquad g=s+1-2y,
\tag{3.1}
$$
每一项均由原行重建并完整乘回。具体商为
$$
\begin{aligned}
\bar R={}&(y-1)s^2
+(-3+14y-22y^2+20y^3-8y^4)s\\
&+2-5y+6y^2-4y^3,
\end{aligned}
\tag{3.2}
$$
以及
$$
\begin{aligned}
\bar N={}&(y-1)^2s^4
+(3-14y+17y^2-6y^3)s^3\\
&+(-12y+37y^2-32y^3+8y^4)s^2\\
&+(-2+8y-y^2-14y^3+8y^4)s\\
&+2y-6y^2+4y^3.
\end{aligned}
\tag{3.3}
$$

先支付完整 $g=0$ 曲线，不能因初结式为零而删去它。由 $s=2y-1$ 及 (2.4)，
$$
u=\frac{s^2+1}{4},\qquad x=y=\frac{s+1}{2},\qquad t=0.
$$
原 (2.5) 给 $\lambda=y,T=-2u$，于是
$$
D_{\rm val}
=\ell(2\lambda^2-2\lambda+1)-T^2
=2u\frac{s^2+1}{2}-4u^2=0.
$$
这违反原物理单位，故整条 $g=0$ 已排。余支必有 $\bar R=\bar N=0$。

## 4. 固定六阶 QQ 结式及全部参数覆盖

使用原固定 $s$ 次数 $2,4$ 的六阶 Sylvester 矩阵，实际精确得到
$$
\operatorname{Res}_s(\bar R,\bar N)
=-16(y-1)^6(2y^2-2y+1)^6(4y^2-6y+1).
\tag{4.1}
$$
这是 QQ 上的完整等式。源使用整系数 CRT：先验 $y$ 次数界 24，真实次数 20；七个素数
$101,103,107,109,113,127,131$。系数绝对值界为
$1733140654144$，模乘积为 $228098450046409>2\cdot1733140654144$。
每个素数下按完整次数界插值并全部点回代；CRT 后逐系数界检查，最后对 (4.1) 全系数乘回。无数值根或概率重建。

$y=1$ 已付。令
$$
A(y)=2y^2-2y+1,\qquad B(y)=4y^2-6y+1.
$$
对完整 $A=0$ 商环，不假设不可约性，有原 QQ 恒等式
$$
\bar R=(y-1)g^2+
A(y)\{3-4y+(-1+6y-4y^2)s\}.
\tag{4.2}
$$
因此在 $A=0$ 的任何复点，$\bar R=0$ 与 $y-1\ne0$ 强迫 $g=0$，回到已排的原 $D_{\rm val}=0$ 曲线。没有遗漏重根或选择分支。

剩余全部点只能满足 $B(y)=0$。

## 5. 余二次覆盖的原 NS 返回

使用原加权值行，不换新候选方程：
$$
\begin{aligned}
\mathcal N_S={}&P_{02}^2\{bN_4(k_B)+cN_4(k_C)\}\\
&-2L_{\rm num}
\{(\ell+1)P_{02}^2+2T_{\rm num}P_{02}
  +2L_{\rm num}^2-2L_{\rm num}P_{02}\}.
\end{aligned}
\tag{5.1}
$$
这里
$$
N_4(v)=2\tau(dv^2)-2f\tau(v^2)
-4\tau(v)\tau(dv)+4f\tau(v)^2+\tau(vD_Kv),
$$
$L_{\rm num}=P_{02}\lambda,T_{\rm num}=P_{02}T$ 都是同一原行的解。

在 (2.1)–(2.4) 上清除已付分母后，原 $\mathcal N_S$ 得整系数 $S(s,y)$，其 $s$ 次数 13、$y$ 次数 14。自含源直接从本稿四行 Gram 重建 $S$；没有读取先前缓存或把仅在某个参数点成立的行插入。

用固定原次数 $2,13$ 的十五阶 Sylvester 定义
$$
Z(y)=\operatorname{Res}_s(\bar R,S)\in\mathbb Z[y].
$$
完整先验次数界为 $13\cdot4+2\cdot14=80$。在 $p=1009$ 的 81 个点计算固定十五阶行列式、插值及全部点回代，得到真实整结式的约化 $\bar Z$，次数 65。然后实际扩展 Euclid 并完整乘回给出
$$
a(y)\bar B(y)+b(y)\bar Z(y)=1\quad\text{于 }\mathbb F_{1009}[y],
\tag{5.2}
$$
其中 $\deg a=64,\deg b=1$。全部系数在小回执中；最后 gcd 严格为 1。

该模证书排除的是原 QQ 结式的公共复根，而非直接把“模空”当“复空”：$B\in\mathbb Z[y]$ 的首项 $4$ 在 1009 为单位，故任何非恒定 QQ 公因子的 primitive 整系数代表在 1009 不降为常数；它若同时整除 $B$ 与 $Z$，会与 (5.2) 矛盾。由 Gauss 引理，$\gcd_{\mathbb Q[y]}(B,Z)=1$。因此 $B(y)=0$ 上不存在同一 $s$ 的 $\bar R=S=0$，也就不存在原 LS 解。

本段不要求 $Z$ 的 QQ 最高系数在 1009 为单位；已保度的完整 QQ 覆盖 $B$ 足够。固定 Sylvester 和完整次数界保证 $\bar Z$ 确为原 $Z$ 的约化。

## 6. 实际执行与范围

自含源：

- notes/2026-11-27-unit211-Q1minusU-T0zero-original-return-8542.js
- SHA256：52fe7571bc26117ba6f5e8966c7aac091845f5185f12dec4d929bcbd1cb81cb0

小回执：

- notes/2026-11-27-unit211-Q1minusU-T0zero-original-return-8542.json

整份自含源已在 V8 实际完成，耗时 2277 毫秒；从原 Gram、原 E0/N0/P1 到公共曲线、六阶 QQ 结式、完整 A 商环恒等式和原 NS 的十五阶模结式/Bézout 均在该次执行中核回。全程 BigInt 有理运算及整数模运算；时钟只用于记录耗时。

实际标量剥除记录为：R 剥 $u(u-1)(4u-1)$；N1 剥 $u^2(u-1)^3(4u-1)^2$；NS 剥 $u^3(u-1)^2(4u-1)^2$。其后 $u=U/D$ 清分母阶段没有另剥任何参数因子；primitive 标量分别为 $2,-2,-1$。所以不暗中要求 $s$ 或 $2u-1$ 非零。

这关闭的是 $Q=1-u$ 的完整 $T_0=0$ 支。一般 Q 边界余支和全部 ordinary ISP 仍须继续；本稿不把局部排除写成课题完成。
