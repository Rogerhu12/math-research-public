# R150：一般等权图的整个半权 m=1/2 分支排除

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**已证明。** 在一般等权 $b=c=m/2$ 原图中，整个 $m=1/2$ 分支为空。本结论保全部复 $Q$、原三变量与谱嵌入；不是仅排 $y=1/2$，也不是从单点秩实验推出整线排空。一般等权余支及普通 ISP 继续。

## 1. 覆盖全部原半权点的合法参数

写 $d=1-Q$。原物理单位给 $d\ne0,Q\ne0$。既有完整结论已排除
[y=1](R150-appendix-unit211-equal-weights-singleton-mean-y1-exclusion.md)、
[y=1/2](R150-appendix-unit211-equal-weights-half-singleton-mean-exclusion.md)，并支付
[原均值首项 $A_m$](R150-appendix-unit211-equal-weights-original-mean-leading-zero-exclusion.md)。
故可令
$$
z=\frac{x-m}{y-1},\qquad v=2y-1,
$$
并且 $zv\ne0$。这些都是已有整支证明的结论，不是新取的一般位置。

原均值差及 singleton 奇部给
$$
t=2(1-z)+\frac{2(z-d)y-Q}{m},
$$
$$
(m-1)\{(d+z^2)v-2z\}+z(dv^2-1)=0.
\tag{1}
$$
在 $m=1/2$，第二式恰为
$$
\frac v2(2dzv-d-z^2)=0.
$$
由于 $d,z,v$ 都已付非零，完整恢复
$$
v=\frac{d+z^2}{2dz},\quad
x=\frac{3d-2dz+z^2}{4d},\quad
y=\frac{2dz+d+z^2}{4dz},\quad
t=\frac{(z-d)(d+z^2)}{dz}.
\tag{2}
$$
特别地 $d+z^2=2dzv\ne0$。每个尚可能的原半权点都在 (2) 中；没有除去新的未处理零面。

## 2. 回完整原 Gram 的首一四次均值

从已提交的独立有限原 affine Gram 重新取其完整系数，作 $m=1/2,Q=1-d$ 与 (2) 的完整齐次代入。统一分母
$$
D=4dz,\quad X=z(3d-2dz+z^2),\quad
Y=2dz+d+z^2,\quad T=4(z-d)(d+z^2)
$$
分别给 $x=X/D,y=Y/D,t=T/D$。对总次数 $n$ 的原式，逐项使用 $D^n$ 齐次返回；所有因子均实际乘回。

令 $F_0=2E_1^{\rm raw}$、$F_1=2E_{Be}^{\rm raw}$、$F_2=E_{Bo}^{\rm raw}$，准确得到
$$
D^2F_0=2(d+z^2)E,\qquad
D^2F_1=4(d+z^2)E,\qquad F_2=0,
$$
其中
$$
E=z^4-2d(d+2)z^2+d^2(2d-1).
\tag{3}
$$
因已付 $d+z^2$，每个原点都满足 $E=0$；它关于 $z$ 是全参数首一四次式。

## 3. 同一个 z 的原 N1 和 N_S 余式

保持原归一化
$$
\widehat N_1=2F_N/m^2,\qquad
\widehat N_S=16F_S/m^3.
$$
这里 $F_N,F_S$ 正是独立 affine Gram 源中由原 $N_4$、同一 $N_0/P_1$ 和原加权 singleton 方程给出的必要式，未替换为新的范数条件。

上节的完整代入及对首一 (3) 的整除，实际给
$$
D^2\widehat N_1=2d\,q_N E+4d^2N,
$$
$$
D^3\widehat N_S=8q_S E+32d^3S.
\tag{4}
$$
$q_N,q_S\in\mathbb Q[d,z]$ 是附源实际保留、整乘回的商。只剥非零 $d$ 与有理数，故原解必满足同一 $E=N=S=0$。

两个完整余式为
$$
\begin{aligned}
N={}&-2(d^3+d^2+3)z^3
+(-4d^4+25d^2+16d)z^2\\
&+2d(d^3+d^2+2d-1)z
+d^2(4d^3-10d^2-3d+4),
\end{aligned}
\tag{5}
$$
以及
$$
S=s_3z^3+s_2z^2+s_1z+s_0,
\tag{6}
$$
其中
$$
\begin{aligned}
s_3={}&48d^5+288d^4+601d^3+233d^2-174d-34,\\
s_2={}&8d^7-68d^6-512d^5-1303d^4-1271d^3-20d^2-102d,\\
s_1={}&-48d^6-198d^5-49d^4+147d^3-22d^2-8d,\\
s_0={}&-8d^8+84d^7+362d^6+391d^5-309d^4+52d^3-24d^2.
\end{aligned}
$$
原 $P_S$ 与原不同值分子亦完整返回并乘回，但最终排除已由 (3)–(6) 足够。

## 4. 完整 QQ 投影及实际 Bézout 单位

取原固定次数 $4,3$ 的完整七阶 Sylvester 行列式
$$
R_N(d)=\operatorname{Res}_z(E,N),\qquad
R_S(d)=\operatorname{Res}_z(E,S).
$$
实际在 $\mathbb Q[d]$ 上作完整无分式行列式；每次多项式整除均乘回。准确次数为
$$
\deg R_N=20,\qquad \deg R_S=30.
$$
两式都只剥已付因子 $d^6$，得到
$$
A=R_N/d^6,\quad B=R_S/d^6,\qquad
\deg A=14,\quad\deg B=24.
\tag{7}
$$
剥除乘积逐项核对，没有倒置 $N$ 或 $S$ 的 $z$ 首项。因此任何实际有限 $z$ 原共同根，不论特化后是否降次，仍迫 $A(d)=B(d)=0$。

对这两个真正 QQ 多项式作完整扩展 Euclid，实际得到
$$
a(d)A(d)+b(d)B(d)=1,\qquad
\deg a=23,\quad\deg b=13.
\tag{8}
$$
两个完整乘积及和已直接乘回为常数 1；不是 gcd 标志或模下猜测。全部有理系数可从附源精确再生，原实际输出哈希在回执中。

(7)–(8) 排除所有复 $d$ 的共同根，矛盾。结合第 1 节已经独立关闭的原坐标边界，整个半权分支排除完成。一般等权余图现在可用 $2m-1$ 为单位。

## 5. 源与真实执行

以下源均为纯 JavaScript Function body；以其原输入对象调用：

- [原半权两参数齐次返回](../notes/2026-11-27-unit211-equal-weight-half-weight-original-return-8542.js)：输入独立 affine Gram 源的实际结果，0.241 秒。
- [首一四次原余式](../notes/2026-11-27-unit211-equal-weight-half-weight-monic-remainders-8542.js)：输入上段返回，0.031 秒。
- [固定七阶完整 QQ 结式](../notes/2026-11-27-unit211-equal-weight-half-weight-full-resultants-8542.js)：输入原余式，三条 N1/NS/PS 投影合计 0.061 秒；PS 完整次数亦为30，剥后24。
- [实际 QQ Bézout](../notes/2026-11-27-unit211-equal-weight-half-weight-original-Bezout-8542.js)：输入完整结式，81.740 秒。首两式已返1，第三式的组合系数为0。
- [准确回执与全部源哈希](../notes/2026-11-27-unit211-equal-weight-half-weight-complete-execution-8542.json)。

四段数学均实际完成；没有用额外整源回放作登记门槛。运行在 functions.exec V8 的有理 BigInt 运算中，无 OS 子进程、无可用 RSS，不虚构这些指标。仓库只保存源、参数、哈希和小回执，不存可重算系数缓存。
