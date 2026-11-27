# R150：一般 LS 零行列式图的全域单首项值二次式与完整值投影

**状态：已证明的降维定理；一般 Delta 零图尚未排空。** 本稿把原值部分变成一个单首项二次式和三个一次式，逐项给出原理想来源，并保留所有一次首项零纤维。再以同一个原 Gram 得到四个必要参数子式。这里的完整投影指四条值等式的共同根存在性；原物理非零条件及其余 N/P 条件仍须返回。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 图、原单位与新值变量

沿用 `results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-P1-double-zero-and-weighted-moment-coordinates.md` 的三值互异、原 $LS\ne0$ 图和 $p+q=2$ 公共尺度。设

$$p=1+r,\quad q=1-r,\quad r^2=1-Q,\qquad \ell=b+c,\quad u=bp+cq.$$

整个二次代数中的权为

$$b=\frac\ell2+\frac{u-\ell}{2(1-Q)}r,\qquad c=\frac\ell2-\frac{u-\ell}{2(1-Q)}r.$$

用同一个 r 写原值

$$h-1=v_0+v_1r,\qquad k-1=v_0-v_1r.$$

置 $T=b(h-1)+c(k-1)$ 和 $\zeta=v_0-v_1$。原非零均值单位 $u\ne0$ 直接给

$$v_1=\frac{T-\ell\zeta}{u},\qquad v_0=\frac{T+(u-\ell)\zeta}{u}.\tag{1}$$

(1) 不要求 ell、T 或等权分子 $u-\ell$ 非零。还实际核验

$$q(h-1)-p(k-1)=-2r\zeta.$$

故原 L 非零给 $\zeta\ne0$，三值互异给 $v_1\ne0$。以下记

$$A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,$$

$$V_2=2u-\ell Q,\quad M=\ell V_2-u^2=4bc(1-Q),\quad D=\ell A-T^2.$$

原 $bc(1-Q)\ne0$ 支付 M。原第二矩成立时，$D=bc(h-k)^2\ne0$。另外，$Q,u,u-1,P_{02}=2P_0,\lambda$ 均沿用已付原单位；$u-1$ 的整支排除见 `results/R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-isolated-mean-unit-base-complete-exclusion.md`。

## 2. 两个小原矩与可双向返回的单首项二次式

记 $z=(h-1)(k-1)$。由 (1)，

$$u^2z=QT^2+2T(u-\ell Q)\zeta-M\zeta^2.$$

令

$$H_A=\ell M\zeta^2-2TM\zeta+V_2T^2-u^2A,$$

$$H_B=-TM\zeta^2+\{2T^2(u-\ell Q)-2uA(u-\ell)\}\zeta+QT^3-2uAT+u^2B.$$

从原向量 $V=(1,w,h,k)$、$w=\lambda-1-T$ 和正确双点乘法直接得到

$$\tau(V)=\lambda,$$

$$\tau(V^2)-2\lambda^2=H_A/u^2,$$

$$\tau(V^3)-4\lambda^3=\{(3+2v_0)H_A-H_B\}/u^2.\tag{2}$$

新源同时核验 $D+\ell H_A/u^2=bc(h-k)^2$。设

$$s_n=\ell B-AT,\qquad z_n=TB-A^2,$$

$$H_L=-2(u-\ell)D\zeta+u s_n-2TD.$$

实际恒等式为

$$T H_A+\ell H_B=uH_L.\tag{3}$$

另一条组合产生全域单首项式

$$H_M=\frac{A H_A+T H_B}{MD}
=\zeta^2-\frac{2T(u-\ell Q)}M\zeta-\frac{QT^2}M+\frac{u^2z_n}{MD}.\tag{4}$$

反向也逐项乘回：

$$H_A=\ell M H_M-\frac{uT}{D}H_L,\qquad
H_B=-TM H_M+\frac{uA}{D}H_L.\tag{5}$$

所以原两矩理想在已付 M、D、u 的局部化中，恰由 $H_M,H_L$ 生成。由于 (4) 的首项是常数 1，所有 ell=0、T=0、$u=\ell$ 纤维都被保留。原两个小矩分别只有 11、19 项。

## 3. 原两线、Phi 的支付与准确 N(V) 余项

定义

$$T_0=2u-\ell Q-2u^2,\quad J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,$$

$$P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,$$

$$G=\lambda P_{02}-(1-u)T_0,\quad w=\lambda-1-T,$$

$$P_f=T_0(J-Q),\quad P_t=bcQ\Phi,\quad
P_c=QP_{02}(\ell+T)-GT_0.$$

原 P1 等式给 $P_ff+P_tt+P_c=0$，源码从原最高一阶 germ 核验其完整尺度身份。再设 $S=2v_0+3-2\lambda$，并令

$$N_f=(3-4\lambda)Q-zJ+S\{2uQv_1+\zeta J\},\qquad N_t=bcQS\zeta,$$

$$R_1=u(3-2\lambda+v_0+v_1)-\ell Qv_1,$$

$$N_c=G(z-S\zeta)+\frac12SQT_0v_1+QwR_1.$$

对原 $N_4=4N$，**准确**的原式身份是

$$\frac Q2 N_4(V)=N_ff+N_tt+N_c-\frac{Qf}{u^2}H_A.\tag{6}$$

(6) 由完整原 Gram 实际展开乘回；没有把原第二矩的倍数遗漏。原两线的行列式在 $H_A=0$ 上等价于

$$E_\Delta=\Phi N_f-S\zeta P_f=0,$$

而相容条件为

$$E_C=\Phi N_c-S\zeta P_c=0.\tag{7}$$

$N_t=bcQS\zeta$ 是原 LS 图单位。若原行列式为零又 $P_t=0$，便有 $P_f=0$，与已经完整排空的原 P1 双系数零支矛盾。因此本稿整个 Delta 零图上 $\Phi\ne0$，可合法使用 $t=-(P_ff+P_c)/(bcQ\Phi)$。未把一般图上的 Phi 直接当作单位。

## 4. 三条一次返回与原组合身份

置

$$\bar s=s_n/D,\quad\bar z=z_n/D,\quad\bar v=\bar s/2,\quad
\bar S=\bar s+3-2\lambda.$$

(3)—(5) 给准确余项

$$v_0-\bar v=-H_L/(2uD),\qquad z-\bar z=-MH_M/u^2.\tag{8}$$

定义小权多项式

$$\begin{aligned}
W={}&\ell uQ^2+2\ell uQ-2\ell Q+2u^3Q-4u^3\\
&-8u^2Q+8u^2-uQ^2+6uQ-4u.
\end{aligned}$$

W 有 **10 项**，对 $(\ell,u,Q)$ 的次数为 $(1,3,2)$。源码核验

$$2W=\Phi(J-2uQ)-P_f.$$

原 $E_\Delta$ 返回为一次式

$$L_\Delta=\Phi\{(3-4\lambda)Q-J\bar z+uQ\bar S\bar s\}
+2\bar S W\zeta.\tag{9}$$

相容条件返回为

$$\begin{aligned}
L_C={}&\Phi\{G\bar z+\bar SQT_0\bar s/4
+Qw[u(3-2\lambda)+(u-\ell Q/2)\bar s]\}\\
&+\zeta\{\Phi[-G\bar S-\bar SQT_0/2+Qw(\ell Q-u)]-\bar S P_c\}.
\end{aligned}\tag{10}$$

为使理想来源可审，令 $v_*=v_0-\bar v=-H_L/(2uD)$、$z_*=z-\bar z=-MH_M/u^2$。源码实际核验以下两条完整身份：

$$E_\Delta-L_\Delta=\frac{\Phi JM}{u^2}H_M
+v_*\{2uQ\Phi[2(v_0+\bar v)+3-2\lambda]+4W\zeta\},$$

$$\begin{aligned}
E_C-L_C={}&\Phi Gz_*\\
&+v_*\{\Phi[-2G\zeta+QT_0(2(v_0+\bar v)+3-2\lambda-2\zeta)/2
+Qw(2u-\ell Q)]-2\zeta P_c\}.
\end{aligned}$$

因此四条原值等式 $H_A,H_B,E_\Delta,E_C$ 与 $H_M,H_L,L_\Delta,L_C$ 的理想在上述已付局部化中相同。全部返回只增加已付分母 u、M、D；没有倒置 W、$u-\ell$ 或任一一次首项。

## 5. 六条参数条件的完整值等式投影

把三个一次式写为 $L_i=a_i\zeta+b_i$，把 (4) 写为 $H_M=\zeta^2+B_M\zeta+C_M$。必要参数式为三对

$$a_i b_j-a_j b_i=0\quad(i<j),\tag{11}$$

以及三个

$$b_i^2-a_iB_Mb_i+a_i^2C_M=0.\tag{12}$$

源码不是仅调用“结式”，而是逐项核验

$$a_iL_j-a_jL_i=a_i b_j-a_jb_i,$$

$$a_i^2H_M-(a_i\zeta+a_iB_M-b_i)L_i
=b_i^2-a_iB_Mb_i+a_i^2C_M.$$

在复数参数点，六式也充分保证这四条**等式**有共同根：若某个 $a_i\ne0$，(11) 使全部一次式有同一个根，而 (12) 使该根满足 $H_M$；若三个 $a_i$ 都为零，(12) 强制三个 $b_i$ 都为零，单首项二次式在复数域有根。这一论证完整覆盖各一次首项为零的情况。

原非零条件 $\zeta\ne0$、$v_1\ne0$、$LS\ne0$ 及原全 N/P 返回仍是原模型的一部分。六式描述上述四条等式的投影，不能单独保证恢复出的根具有全部物理非零条件。

## 6. 同一 Gram 的四个必要参数子式

从原 E0、N0 解出的同一 Gram，使用上文已付 $P_t$ 代入 t。四个原式 $E1,EB_e,EB_o,N1$ 都变成 f 二次式。其中 N1 使用原 P1 消去 w；其原双线性极化身份在源码中直接构造。

把四式作用于真实非零列 $(f^2,f,1)^t$，各三行给一个三阶子式。源码核验全部 12 条常数列 cofactor 身份。剥除的公共因子仅来自 Q、bc、Phi；没有倒置任何 f 二次首项。

| 三行 | $(\ell,u,Q,\lambda,T)$ 次数 | 项数 |
|---|---|---:|
| E1、EBe、EBo | (10,17,9,3,3) | 3320 |
| E1、EBe、N1 | (14,21,11,3,3) | 6871 |
| E1、EBo、N1 | (14,21,11,3,3) | 6220 |
| EBe、EBo、N1 | (13,20,11,3,3) | 5338 |

这四式只作完整原系统的必要条件。它们与 (11)—(12) 共同给五参数的新输入；本稿没有声称四个子式足以恢复同一个 f，也未声称它们与完整九式理想相等。

## 7. 自含源、实际回执和本轮冻结探针

自含源：`notes/2026-11-27-unit211-generic-LS-Delta-zero-global-monic-value-quadratic-original-return-8542.py`。

- 源 SHA256：`ea0ffae265bd5f89cbbb98edf58c7dbc6375a36698a5a5e0508483de669a17ba`。
- 实际 exit 0；墙钟 **1.288568 秒**；峰值 RSS **48700 KiB**。
- 源限 240 秒、4 GiB；检查 22 个不同的有理分母。
- stdout 9157 字节，SHA256 `cb608d2996a8109f1db7295cd9898b2eeb08ddbad53e1129c4b3e7e479f9c712`。
- 回执：`notes/2026-11-27-unit211-generic-LS-Delta-zero-global-monic-value-quadratic-execution-8542.json`。

此前两个更大的原矩阵探针未被作为任何数学结论使用，准确源与小回执已冻结：

1. 一般四二次 M10：配置 180 秒、4 GiB；最后日志为 Bareiss index 6、41.440944 秒，未返回完整 determinant/cofactor。终态输出被截断，补收 session29289 返回 `Unknown process id`，故最终退出码、总墙钟、RSS 明记 unknown。源及回执前缀 `2026-11-27-unit211-generic-LS-four-quadratic-M10-incomplete-...-8542`。
2. 三均值 Dixon M6：实际 signal 9，**29.381049 秒**、RSS **520816 KiB**；配置 150 秒、4 GiB；没有完整 determinant/cofactor。信号的外部原因未知。其精确源、原行再生源及回执前缀 `2026-11-27-unit211-generic-LS-mean-Dixon-M6-incomplete-...-8542`、`2026-11-27-unit211-generic-LS-Dixon-quadratic-rows-probe-8542.py`。

后续从本稿的小原值结构继续，不重跑这两个未完成输入。一般 Delta 零、一般 LS、R150 及普通 ISP 仍开放。
