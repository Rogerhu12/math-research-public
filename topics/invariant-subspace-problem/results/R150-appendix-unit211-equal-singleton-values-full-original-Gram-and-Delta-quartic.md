# R150：一般 h=k 非 1 碰撞的完整原 Gram 与 Delta 首一四次

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 范围和本次新增内容

[原 U-value atlas](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)已经完整参数化 h=k 非 1 的值碰撞。该旧参数化不算本次新结论。本稿新付：

1. 同一个原 Gram 的 N4(V) 仿射线；
2. 原 Delta 对自由权重 b 的完整首一四次关系，最高系数只含原单位；
3. Delta 非零图中，正确清掉两个原权重后的全部八条原均值/N/P 条件。

这个图满足物理 D=0。凡此前权排除的覆盖用了 D 非零，本稿都不将其直接移到这里。源不倒置 D、Pf、S、T0 或任何代数范数，也不把两个单点的原目标误设为 h=1。原点排空尚未完成。

## 2. 旧矩图与原权

记

$$A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,$$

$$\ell=A^3/B^2,\quad c=\ell-b,\quad a=1-\ell,\quad
h=k=1+\xi,\quad T=A^2/B,\quad w=\lambda-1-T.$$

A,B 在该碰撞图是原单位；lambda 非零。取原

$$p=1+\rho,\quad q=1-\rho,\quad Q=pq,\quad
u=pb+qc=2\rho b+q\ell.$$

原 b,c,rho,p,q 非零，其他原物理条件仍保持。由矩身份有

$$\ell\xi^2=A,\quad \ell\xi^3=B,\quad
\ell A-T^2=0.$$

写

$$V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,\quad \Phi=T_0+4u-4+Q,$$

$$P_{02}=(2-3u)V_2-Qu+2u^3,\quad
P_f=T_0(J-Q),$$

$$G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0.$$

并令

$$S=2\xi+3-2\lambda,\qquad \eta=\xi+3-2\lambda.$$

这里保留整个 S=0 纤维，没有为了计算另加 S 逆。

## 3. 同原 Gram 的两条线

原 E0/N0 恢复在 f,t 上给

$$W_1=T_0/2+2uf,$$
$$W_2=uT_0+\lambda P_{02}+(V_2+2u^2)f-bcQt,$$

$$X=\frac{qW_1-W_2}{bp(q-p)},\qquad
Y=\frac{W_2-pW_1}{cq(q-p)}.$$

然后

$$r=X-ap-ct,\quad s=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bct$$

恢复同一个原 Gram。将实际 V=(1,w,h,h) 代入原 Frobenius 运算，源完整核回

$$\frac Q2N_4(V)=N_Ff+bcQS\xi\,t+N_C, \tag{3.1}$$

其中 N4=4N，且

$$N_F=(3-4\lambda)Q+J\xi\eta,\qquad
N_C=\eta(-G\xi+Qwu).$$

原 P1 条件对应另一个原线

$$P_ff+bcQ\Phi\,t+P_c=0. \tag{3.2}$$

(3.1) 直接从实际四维代数与实际 Gram 逐项核回；不是把 h=1 图的 N 公式未经修改套到 h=k。两个单点值同 h，所有最高/梯度目标继续用 h 的真实幂。

## 4. Delta 的完整首一四次

令

$$\Delta=\Phi N_F-S\xi P_f.$$

把 lambda,rho 视为底参数，ell、xi 在底环，u=2rho b+qell。u 的最高次项给

$$[u^2]\Phi=-2,\quad [u^2]N_F=-2\xi\eta,\quad
[u^4]P_f=4.$$

因此

$$[u^4]\Delta=4\xi(\eta-S)=-4\xi^2,$$

从而

$$\boxed{[b^4]\Delta=-64\xi^2\rho^4.} \tag{4.1}$$

这个系数是原单位，因为 xi=B/A、rho 都非零。源对全部五个 b 系数及归一化后的整多项式乘回；不是只计算最高系数。

于是整个 Delta=0 面为

$$b^4+r_3(\lambda,\rho)b^3+r_2(\lambda,\rho)b^2+
r_1(\lambda,\rho)b+r_0(\lambda,\rho)=0,$$

系数全部只除以 A,B,rho,p,q 的原单位因子。该环境对底参数环有限自由秩 4；这只指首一关系定义的环境，未宣称原解商自由或已排空。完整系数由固定源和小回执准确再生。

## 5. Delta 非零图的正确原尺度

设

$$f_0=c(S\xi P_c-\Phi N_C),\qquad
t_0=(P_fN_C-P_cN_F)/Q,$$

$$D_0=c\Delta,\qquad H=bD_0=bc\Delta.$$

在当前 Delta 非零原图中 H 是原单位，且

$$f=f_0/D_0,\qquad t=t_0/(bD_0).$$

完整原乘回给

$$P_ff_0+cQ\Phi t_0+P_cD_0=0,$$
$$N_Ff_0+cQS\xi t_0+N_CD_0=0.$$

实际 builder 直接构造 H 倍的原 Gram，不在有限代数中取 H 逆。由于这里 c=ell-b 随自由权重变化，必须把 c 也放入 H；只沿用 h=1 图的 H=bDelta 会残留未清的权分母。

同一尺度下，三个均值式乘 H²，五个 N/P 式乘 H³。完整 P1、N4(V) 均返回零，原 E0/N0 恢复也保持。全部八个剩余原式为

$$E_1,E_B,E_C,N_1,N_B,P_B,N_C,P_C,$$

两个单点的梯度目标都为 2lambda P02 h²，最高目标都为 P02 h³，清尺度后再乘相应 H³。原 N1 仍是双点一阶 germ，不是把 nilpotent 行当作简单点。

## 6. 全八原值的实际规模

以下为清原底环分母后的真实分子次数；没有剥任何尚未支付的几何因子。

| 原行 | b 次数 | lambda 次数 | rho 次数 | 项数 |
|---|---:|---:|---:|---:|
| E1 | 14 | 86 | 12 | 8710 |
| EB | 13 | 86 | 12 | 9743 |
| EC | 13 | 80 | 12 | 7948 |
| N1 | 21 | 122 | 17 | 24540 |
| NB | 21 | 127 | 17 | 28087 |
| PB | 21 | 135 | 18 | 32612 |
| NC | 21 | 121 | 17 | 26504 |
| PC | 21 | 117 | 18 | 25480 |

每条分母均实际审计为原 A,B,rho,p,q 的乘积；没有残留 b、c 或 Delta 分母。八条分子与分母的完整大小和 SHA 都在小回执，最大的可再生单条分子约 2.30 MB，不另存系数缓存。

## 7. 实际执行与准确旧失败

源：[正确清 c 的原 Gram 与 Delta 四次](../notes/2026-11-27-unit211-equal-singleton-values-original-c-cleared-Gram-and-Delta-quartic-8542.py)。

- 源 Git blob：1b172cc89b08b123192cb5bcd4517bcc3518bb7a。
- 源 SHA256：fdece673fb4551f0feca0ac304e59327ca83860ccedcc483fa19815e99fec1f2。
- Actions run/job：45998121640 / 140502588909。
- 实际内层 exit0；源 4.184757144 秒，驱动 4.240095449 秒，RSS96500 KiB。
- stdout12470 字节，SHA256：3cdf9ca95e7227961e34fc12b2eed4cca97f7947372d21dad024157da3454547。
- 源 main：06a05b5429725f94d5f878f05cc657e14cb2bf36。
- 12:22:57.758588 UTC 实际 pull 后两 README 无差异。
- 180 秒/4 GiB，Python3.12.14、python-flint0.9.0，单线程。

旧源 27211310 的实际 run45997577456/job140500746670 在 0.079589205 秒、41048 KiB、exit1 停于原 c 分母审计。该次原四次与 N4(V) 线已经完成，八行尚未开始；不冒称资源失败或原点矛盾。失败源与小回执冻结，修正源仅新增必要的原 c 清尺度后首次完整生成八行。

两图 Delta 非零与 Delta 零都保留全部原权面。后续从这些真正原输入继续；本稿没有付整个值碰撞、R150 或 ordinary ISP。
