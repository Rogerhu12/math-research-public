# R150 附录：单位 2+1+1 相等非零基点配对的零最高基点值支路为空

作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条范围已证明。** 在原 essential-four 外均值、rank $H=4$、单位 $2+1+1$ 加孤立零点分支中，若两条基点配对相等且非零，而原最高三次式在双点的值为零，则不存在完整原临界点。本稿新增关闭总单点权重 $1/2$ 和 $1$，并接此前总权重零的完整排除；其余相等配对支路继续开放。

## 1. 同一原代数、最高值与孤立零点

沿用[一条零配对附录](R150-appendix-essential-four-unit-two-plus-one-plus-one-one-zero-base-pairing-exclusion.md)的同一原物理除子 $2A+B+C+Z$、Frobenius 代数及完整原 mean/最高/第二梯度。以共同齐次规范令 $p=q=1$，写
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\quad \tau(z)=a z_0+z_1+bz_B+cz_C,
\quad l=b+c,\quad a=1-l,\quad bc\ne0,
$$
$$
K_B=\begin{pmatrix}
0&0&1&1\\0&A_1&r&s\\1&r&0&t\\1&s&t&0
\end{pmatrix},\qquad
U=(u_0,u_1,u_B,u_C),\qquad m=\tau(U).
\tag{1.1}
$$
$A_1$ 是矩阵条目，与物理点 $A$ 不混用。乘法仍为
$zw=(z_0w_0,z_0w_1+z_1w_0,z_Bw_B,z_Cw_C)$，$1=(1,0,1,1)$。若 $k_i$ 是 Gram 的行，则
$$
(D_Kz)_i=\tau(k_i z),\quad d=D_K1,\quad f=\tfrac12\tau(d),
$$
$$
E=e-2D_Kd-2d^2+4fd,
\quad e=(\tau k_0^2,2\tau k_0k_1,\tau k_B^2,\tau k_C^2),
$$
$$
P(z)=\tfrac12\tau((z-\tau(z)1)^3),
$$
$$
N(z)=\tfrac12\tau((d-f1)z^2)-\tau(z)\tau(dz)
+f\tau(z)^2+\tfrac14\tau(zD_Kz).
\tag{1.2}
$$
全部原临界点都满足 $E=0$ 及
$$
(P_0,P_1,P_B,P_C)=(-u_0^3,-3u_0^2u_1,-u_B^3,-u_C^3),
$$
$$
(N_0,N_1,N_B,N_C)=(-mu_0^2,-2mu_0u_1,-mu_B^2,-mu_C^2).
\tag{1.3}
$$
还保留[原孤立零点最高式](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-pairings-zero-base-mean-exclusion.md)所给的无除法必要条件
$$
J=aP_0+P_1+bP_B+cP_C-3(aN_0+N_1+bN_B+cN_C)=2m^3,
$$
$$
2N_i^3+JP_i^2=0,\qquad i=0,B,C.
\tag{1.4}
$$
它来自同一原最高恒等式在 $Z$ 的值 $P(U)=0$，没有另选自由范数参数。

从 (1.2) 直接计算
$$
P_0=\tfrac12l(l-1)(2l-1).
\tag{1.5}
$$
所以本条假设恰为 $l\in\{0,1/2,1\}$，并由 (1.3) 总有 $u_0=0$。$l=0$ 已由[零总权重的完整二阶 germ 与射影排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-equal-base-pairings-zero-total-weight-exclusion.md)关闭；下文只计算两个尚未付的值。

## 2. 统一物理矛盾

设原双点的两允许 jets 为 $v_0,v_1$，孤立零点向量为 $w_Z$。若
$$
A_1=u_0=u_1=0,
\tag{2.1}
$$
则原自配对及 (1.1) 给
$$
K(v_0,v_0)=K(v_0,v_1)=K(v_1,v_1)=0,
$$
$$
K(v_0,w_Z)=K(v_1,w_Z)=K(w_Z,w_Z)=0.
$$
原长度三 $2A+Z$ 的独立 jet 空间因而全等向。但[原长度三全等向 jets 分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)已证明这样的支撑只能是指定的三点约化支撑，不能是 $2+1$；该结论包括无穷远与所有允许局部单位。因此 (2.1) 对原临界点不可能。两支都将直接导出 (2.1)。

## 3. 总单点权重 $l=1/2$

现在 $a=1/2,c=1/2-b$，记 $\beta=bc\ne0$。原 mean 基点式准确为
$$
E_0=A_1-2\beta t.
$$
所以 $A_1=2\beta t$。代入同一原第二梯度，得
$$
N_0=\beta t/2.
$$
已经有 $u_0=0$，故 (1.3) 迫 $N_0=0$。因 $\beta\ne0$，得到 $t=A_1=0$。

此时原两单点 mean 的准确加权和是
$$
2(bE_B+cE_C)=-8\beta(r-s)^2.
$$
故 $r=s$，将共同值记为 $V$。没有除以 $r-s$。原 mean 四式此时全为零，而全部原值与 jets 简化为
$$
P_0=P_1=N_0=N_1=0,
$$
$$
P_B=P_C=P_*:=\tfrac12V^2(2V-3),\qquad
N_B=N_C=P_*/2,\qquad J=-P_*/4.
\tag{3.1}
$$
这些式子对任意允许 $b,c$ 成立，不附加两个权重相等。

若 $P_*=0$，原最高值给 $u_B=u_C=0$，再由 $J=2m^3$ 得 $m=0$。因为 $u_0=0$，此时 $m=u_1$，所以 $u_1=0$。

若 $P_*\ne0$，则 $u_B,u_C\ne0$。由原最高值和第二梯度，
$$
-mu_B^2=P_*/2=-u_B^3/2,
\qquad -mu_C^2=P_*/2=-u_C^3/2,
$$
从而 $m=u_B/2=u_C/2$。因此 $u_B=u_C$，而
$$
m=u_1+b u_B+c u_C=u_1+u_B/2
$$
再次给 $u_1=0$。两种情况均满足 (2.1)，物理矛盾已证。零 $m$、零单点最高值及 $V=0,3/2$ 没有被删除。

## 4. 总单点权重 $l=1$

此时 $a=0,c=1-b$，仍有 $\beta=bc\ne0$。从原最高 jet 与 mean 基点式直接得到
$$
P_1=3A_1/2,
\qquad E_0=2A_1+2(br+cs)-1.
$$
因为 $u_0=0$，(1.3) 要求 $P_1=0$，所以
$$
A_1=0,\qquad br+cs=1/2.
$$
写 $h=r-s$、$\delta=b-c=2b-1$，等价参数化为
$$
r=\tfrac12+c h,\qquad s=\tfrac12-b h.
$$
同一原第二 jet 和 mean 第一 jet 精确给
$$
N_1=-\tfrac12\beta\delta h t,
$$
$$
E_1=2\beta\delta ht-2\beta h^2-\tfrac12.
\tag{4.1}
$$
由 $u_0=0$ 得 $N_1=0$。联合 (4.1)，
$$
4\beta h^2=-1,\qquad h\ne0,\qquad \delta t=0.
\tag{4.2}
$$
若 $\delta=0$，已经有 $b=c=1/2$。若 $t=0$，原两单点 mean 为
$$
E_B=-2c^2h^2-\tfrac12,
\qquad E_C=-2b^2h^2-\tfrac12.
$$
代入 (4.2)，得到 $E_B=(c-b)/(2b)$、$E_C=(b-c)/(2c)$；因此仍须 $b=c=1/2$。这穷尽 $\delta t=0$，未在 $t=0$ 上套一般有理公式。

所以全部剩余抽象 mean 解都具有
$$
b=c=\tfrac12,\quad h^2=-1,\quad
r=(1+h)/2,\quad s=(1-h)/2,\quad A_1=0,
\tag{4.3}
$$
其中 $t$ 暂任意。令 $H=3t-2$。在准确商环 $\mathbb Q[t,h]/(h^2+1)$ 中，原值为
$$
P_0=P_1=N_0=N_1=0,
$$
$$
P_B=-(H+2h)/4,\quad P_C=-(H-2h)/4,
\quad N_B=P_B/2,\quad N_C=P_C/2,\quad J=H/8.
\tag{4.4}
$$
将 (4.4) 代入原 (1.4)，得到
$$
2N_B^3+JP_B^2=\frac{(H+2h)(9t^2-12t+8)}{256},
$$
$$
2N_C^3+JP_C^2=\frac{(H-2h)(9t^2-12t+8)}{256}.
$$
两式之差为 $h(9t^2-12t+8)/64$，而 $h\ne0$，所以
$$
9t^2-12t+8=H^2+4=0.
$$
结合 $h^2=-1$，完整纤维只有 $H=2h$ 或 $H=-2h$，两个代数共轭值都保留。

若 $H=2h$，有 $(P_B,P_C)=(-h,0)$，故 $u_C=0,u_B\ne0$。由 $N_B=P_B/2$ 及原 (1.3)，得 $m=u_B/2$。若 $H=-2h$，有 $(P_B,P_C)=(0,h)$，同样得到 $u_B=0,u_C\ne0$ 和 $m=u_C/2$。两种情形均由
$$
m=u_1+(u_B+u_C)/2
$$
推出 $u_1=0$。再次满足 (2.1)，与同一原 $2A+Z$ 的物理等向分类矛盾。总权重一的整个分支也为空。

## 5. 完整范围与实际精确身份

结合已登记的 $l=0$，本稿排尽 (1.5) 的全部三个零点，因此
$$
\boxed{p=q\ne0\ \Longrightarrow\ P_0\ne0
\quad\text{对任何剩余的原 unit }2+1+1\text{ 临界点}.}
$$
等价地，相等非零配对支路只需继续 $l\notin\{0,1/2,1\}$。这不是整个 unit $2+1+1$、整个 essential-four 或全局 Jacobian 理想的完成结论。

[自足 QQ 源](../notes/2026-11-26-unit-two-plus-one-plus-one-equal-half-or-unit-weight-347c.py)从同一原 Frobenius 乘法重建 $E,P,N,J$，准确核全部上述身份、两个边界和两个最终纤维。它不依赖探索脚本，也不重跑已登记的零总权重结果。源码 SHA-256：`6b4e4fd2bcf9882ed9f43a106854d8fdfa4d9bcce606e12629b3db0a043fda4d`。

实际执行：CPython 3.12.14、SymPy 1.14.0，无 `PYTHONPATH` 覆盖；exit $0$，源内计时 $1.616533$ 秒，峰值 RSS $49960$ KiB。[紧凑执行记录](../notes/2026-11-26-unit-two-plus-one-plus-one-equal-half-or-unit-weight-execution-347c.json)保留命令、源与输出身份及全部标量结论；没有存入可重算数组。

**后续完整闭合（2026-11-26）：** 本条的原边界证明保持有效；余下等配对一般图现由[完整相等配对专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-equal-base-pairings-complete-exclusion.md)关闭，整个 $p=q\ne0$ 不再是待做分支。
