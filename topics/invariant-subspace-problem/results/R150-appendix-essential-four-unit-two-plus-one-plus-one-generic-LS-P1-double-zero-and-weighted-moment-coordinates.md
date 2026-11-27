# R150：一般 LS 图的原 P1 双零支完整排除及加权矩四参数坐标

**状态：已证明。** 在三值互异、$LS\ne0$ 的原 unit 2+1+1 非零孤立均值图中，原 $P_1$ 关于 $f,t$ 的两个系数不可能同时为零。证明保留同点配对和全部参数零纤维。本稿还给出保留等权、$\ell=0$ 和 $T=0$ 的加权矩四参数坐标。一般 LS 图本身仍开放。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 原矩的全域有理恢复

写 $x=h-1,y=k-1,s=x+y,z=xy,\ell=b+c,T=bx+cy$，并令

$$A=2\lambda^2-2\lambda+1,\qquad B=4\lambda^3-6\lambda^2+3\lambda-1.$$

原三个 U 矩给 $bx^2+cy^2=A,bx^3+cy^3=B,w=\lambda-1-T$，所以

$$A=sT-\ell z,\qquad B=sA-zT.$$

这两个线性方程的行列式

$$D=\ell A-T^2=bc(x-y)^2$$

已由 $bc\ne0$ 和三值互异支付。故整个图上

$$s=\frac{\ell B-AT}{D},\qquad z=\frac{TB-A^2}{D}.\tag{1}$$

没有除以 $\ell,T,A,B$ 或等权分子。置

$$s_n=\ell B-AT,\quad z_n=TB-A^2,\quad \Delta_n=s_n^2-4z_nD,\quad H_n=2TD-\ell s_n.$$

源码实际核验

$$s_nT-\ell z_n=AD,\quad s_nA-z_nT=BD,\quad \ell^2\Delta_n-H_n^2=4D^3.\tag{2}$$

对 p、q 作同一允许的公共尺度使 $p+q=2$，保留同一个 $d=x-y$、$d^2=\Delta=s^2-4z$。设

$$p=1+\theta d,\quad q=1-\theta d,$$

$$b=\frac\ell2+\frac{2T-\ell s}{2\Delta}d,\qquad c=\frac\ell2-\frac{2T-\ell s}{2\Delta}d.$$

则 $u=bp+cq=\ell+\theta(2T-\ell s)$、$Q=pq=1-\theta^2\Delta$、$bc=D/\Delta$。因此 $(\lambda,\ell,T,\theta)$ 给出完整四参数有理表达，最后的 d 保留整个二次代数而非选一个根。等权 $H_n=0$ 仍包含在内；它只使 $u=\ell$，未被除去。原图因子是

$$L=q(h-1)-p(k-1)=d(1-\theta s),\qquad S=h+k+1-2\lambda=s+3-2\lambda.\tag{3}$$

新源从这些数据重建原 Gram、正确双点乘法和全部三矩。第一阶段有 52 个不同单位多项式检查和 8 次实际逆乘回；分母仅来自 $D,\Delta_n,Q_n=D^2-\theta^2\Delta_n,\theta$，均由原图支付。

## 2. 原两线与 P1 双零的强制关系

令

$$T_0=2u-\ell Q-2u^2,\quad J=2u(1-u)+\ell Q,\quad \Phi=T_0+4u-4+Q.$$

原 $P_1=3wP_0$ 乘已付 Q 后，其线性系数及常数项可取

$$P_f=T_0(J-Q),\qquad P_t=bcQ\Phi,$$

$$P_c=(1-u)T_0^2+P_{02}\{Q(\ell+T)-\lambda T_0\},\qquad P_{02}=2P_0.\tag{4}$$

新源从原最高一阶 germ 核出

$$Q\{2P_1-3wP_{02}\}=3(P_ff+P_tt+P_c).$$

所以 $P_f=P_t=0$ 的原解还须有 $P_c=0$。原 $bcQ\ne0$ 给 $\Phi=0$，而恒等式

$$J-Q=-\Phi-4(u-1)^2$$

和已付 $u-1\ne0$ 给 $T_0=0$。再由

$$T_0+Q+4(u-1)=\Phi,$$

$$T_0=2(u-1)(2\ell-u)-\ell\{Q+4(u-1)\}$$

得到 $Q=-4(u-1),u=2\ell$。原常数项 (4) 与 $P_{02}Q\ne0$ 最后强制

$$T=-\ell.\tag{5}$$

原 $u\ne0$ 因而支付 $\ell\ne0$。$u-1$ 的支付来自此前整个归一化单位基点均值支排除；在共同尺度 $p+q=2$ 中它正是 $u=1$，见 `results/R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-isolated-mean-unit-base-complete-exclusion.md`。

## 3. 未除的四次物理关系

置

$$D_2=A-\ell,\quad W=B+3A-2\ell,\quad Z_n=\ell B+A^2,$$

$$D_n=\ell(A+B)^2+4D_2Z_n,\quad L_n=B+2A-\ell,\quad S_n=A+B+(3-2\lambda)D_2.$$

由 (1)、(5)，

$$s=\frac{A+B}{D_2},\quad z=-\frac{Z_n}{\ell D_2},\quad \Delta=\frac{D_n}{\ell D_2^2}.$$

$D=\ell D_2$ 和 $\ell\ne0$ 支付 $D_2$。原 $u=2\ell$ 配对式强制 $\theta(s+2)=-1$，故

$$\theta=-D_2/W,\qquad Q=-\frac{4D_2^3}{\ell W^2}.$$

这里 $W=D_2(s+2)\ne0$ 由刚才的原等式支付。与 $Q=-4(2\ell-1)$ 合并，得到

$$H(\lambda,\ell)=(A-\ell)^3-\ell(2\ell-1)(B+3A-2\ell)^2=0.\tag{6}$$

H 的 ell 次数为 4，首项恰是常数 $-8$，故整个参数平面上可使用单首项 $H_m=-H/8$，无新增首项零面。本支所有除数来自

$$\ell,\ 2\ell-1,\ D_2,\ D_n,\ W,\ L_n,\ S_n,\ \lambda,\ Z_n.$$

$D_n,Z_n$ 分别来自 $h-k\ne0$ 和 $(h-1)(k-1)\ne0$；$L=2dL_n/W$、$S=S_n/D_2$，故 $L_n,S_n$ 来自原 $LS\ne0$。原 Q 非零也由 ell、$D_2,W$ 的已付性保持。

## 4. 同根原 N(V) 解 t 与全部原方程

新源用整个 $d^2=\Delta$ 二次代数构造 $b,c,p,q,h,k$，并验证三矩、权乘积和配对。原 N(V) 对 f、t 线性，乘 $4\theta Q$ 后的 t 系数为

$$N_t=bcS(\theta s-1)Q=\frac{8\ell D_2^5S_nL_n}{D_nW^3}.\tag{7}$$

(7) 仅含已付单位，故可全局解 $t=-(N_ff+N_c)/N_t$。源先在一般四参数图从原 Gram 核验完整 N(V) 线性身份，再于本支重新构建 Gram 并验证实际 N(V)=0。原 E0/N0、$f=\tau(D_K1)/2$ 也乘回；P1 分子的余项准确是原 H 的倍数。

随后从同一个 d 生成完整原均值、最高式和第二梯度式。共轭配对给八个标量必要式

$$E1,\ EB_e,\ EB_o,\ N1,\ NB_e,\ NB_o,\ PB_e,\ PB_o.$$

它们未被另一范数嵌入替换。分母逐项检查已付，第二阶段有 205 个不同单位多项式检查和 11 次实际逆乘回。每个分子按 $H_m$ 除法后，都实际验证 $p=qH_m+r$ 且 $\deg_\ell r<4$。前四式对 f 二次、后四式对 f 三次。未倒置任何 f 首项。

## 5. 原二次子式与 559 次 QQ 覆盖

前四个原式按真实非零列 $(f^2,f,1)^t$ 写成四行。对行组 $(E1,EB_o,N1)$ 和 $(E1,EB_e,EB_o)$ 的三阶矩阵，逐项验证常数列 cofactor 身份，再按 $H_m$ 精确返回，得到必要式 $R_C,R_S$。其 $(\ell,\lambda)$ 次数为 $(3,163)$、$(3,169)$。六条系数身份全部回乘，不假定函数空间自由，也不除 f 首项。

实际完整 QQ 投影

$$\mathcal R(\lambda)=\operatorname{Res}_{\ell}(H_m,R_C)$$

为 559 次。完整因式分解（含有理内容）实际乘回为

$$\mathcal R\doteq\lambda^{102}(2\lambda-1)^{300}A^{45}C_{4,S}^3C_{4,L}^3C_{43},\tag{8}$$

其中

$$C_{4,S}=72\lambda^4-156\lambda^3+136\lambda^2-54\lambda+9,$$

$$C_{4,L}=8\lambda^4-4\lambda^2+2\lambda+1.$$

完整投影 SHA256 为 `de90e5dad9bd6247dfacdb8e3735fe0abde995ff05116b43d5be5272226889bb`；43 次因子 SHA256 为 `b312b9ffb13dd2f4df3b45c2aec07941c82ccabf6bbc29cf11dec73947cee179`。

这里只因原非零均值移除 lambda=0；其余因子全部在下文返回。所有原 ell 首项零纤维和重数保留。

## 6. 整个 43 次候选的原一元返回

令 $\mathcal S=\operatorname{Res}_{\ell}(H_m,R_S)$ 为完整 QQ Sylvester 结式。模 1009 后，两个输入的原 ell 次数 4、3 保持；$C_{43}$ 的次数保持 43，首项余数为 **609**，其单首项版本所有系数都在 $\mathbb Z_{(1009)}$ 内。

完整 $\overline{\mathcal S}$ 为 578 次。实际计算两个乘积及和，核验

$$a\overline C_{43}+b\overline{\mathcal S}=1,\qquad(\deg a,\deg b)=(577,42).$$

两系数合并 SHA256 为 `f277534d41ff8e989fdc1fb7981b4231db637f512cbcabe54113e1d66f9f7584`。

若原 $C_{43},\mathcal S$ 有共同复根，其单首项 QQ 最小多项式因整除单首项化且 1009 整的 $C_{43}$，由 Gauss 引理属于 $\mathbb Z_{(1009)}[\lambda]$。它约化后仍有正次数，且整除两个模输入，与实际 Bézout 身份矛盾。因此整个 43 次候选排除。这是实际完整一元 QQ 覆盖的返回，不是从多变量模单位判 QQ 空集。

## 7. 余下四个整商代数的原返回

对 $C_{4,S},C_{4,L},A,2\lambda-1$ 分别进入整个 $K=\mathbb Q[\lambda]/(\phi)$，不选复嵌入。在 $K[\ell]$ 内返回原四次 $H_m$，只通过与已付原单位的 gcd 和准确商移除不可能的 ell 根，包括全部重数。

随后使用完整原 $R_E=\operatorname{Res}_f(E1,EB_e)$。它在参数特殊化前按完整 f 次数 2、2 生成，按 $H_m$ 返回的余式身份也先乘回；因此特殊化后 f 首项为零的情形没有遗漏。每个整商代数中，剩余 $H_m$ 与这个原结式的扩展 Euclid 都准确返回 1。

| 完整 lambda 纤维 | 从原 H 移除的已付根 | 剩余 ell 次数 | 实际逆 / 除法 / Bézout 数 | 原返回 |
|---|---|---:|---:|---|
| $C_{4,S}$ 的全部四根 | S 的一次根 | 3 | 33 / 23 / 10 | 1 |
| $C_{4,L}$ 的全部四根 | L 的一次根 | 3 | 33 / 23 / 10 | 1 |
| A 的两个根 | ell=0 | 3 | 33 / 23 / 10 | 1 |
| lambda=1/2 | $u-1=2\ell-1$ 的三个重因子 | 1 | 38 / 26 / 12 | 1 |

每次逆元由 QQ 多项式 xgcd 取得并乘回 1，每次除法及每条扩展组合也乘回。把各商视作完整有限代数时，被逆的每个元素仍有实际逆证书，不依赖未检验的一般位置。(8) 至此无剩余候选，原 P1 双系数零支排空。

## 8. 自含源、真实回执和剩余范围

源：`notes/2026-11-27-unit211-generic-LS-P1-double-zero-original-return-8542.py`。

- 源 SHA256：`7001773497aeb492055b8e2ac6d63d8c044c0f5af937b2997aebadad627dc5f7`；25576 字节。
- 实际 exit 0；墙钟 **11.540406 秒**；源内完成 11.442559 秒；峰值 RSS **47912 KiB**。
- 原上限 360 秒、4 GiB。
- stdout 12876 字节；SHA256 `ca30e7a845dc309897bc6aa9f07c80f3e22353c3167e6400f9fd41795cdbd68b`。
- 小回执：`notes/2026-11-27-unit211-generic-LS-P1-double-zero-execution-8542.json`。

今后一般三值互异 LS 非零图可用 $(P_f,P_t)\ne(0,0)$ 的完整覆盖。原两线的 Cramer 行列式为零支仍需保留；本稿没有把它作已付单位，也没有宣称一般 LS、R150 或普通 ISP 已完成。
