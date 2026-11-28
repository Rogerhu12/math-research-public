# R150 补充：整个 W 的 alpha 零原支只余同一个四重二次权域

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 完整结论

在当前原 W 图定义
$$
\eta=f-u,\quad \delta=1-Q,\quad
\widehat U=u-\ell Q,\quad
\alpha=4\delta\eta-\widehat U t.
$$
由整个
[$t=0$ 排除](R150-appendix-unit211-W-entire-t-zero-complete-original-exclusion.md)
和
[$f=u$ 排除](R150-appendix-unit211-W-entire-f-equals-u-complete-original-exclusion.md)，
$t,\eta$ 都已付。

本次完整原返回证明整个 $\alpha=0$ 支必须满足
$$
\boxed{(k^2+8k+8)^4=0.}
\tag{1}
$$
这是完整原理想的有限覆盖，保留四重结构。它还不是整个 $\alpha=0$ 排除；下一步是完整 $\mathbb Q[k]/(k^2+8k+8)$ 上的原行返回。没有把 UI success、模特化、多变量 gcd1 或两个不同原点的投影当作排空。

## 2. 不留新权头的 f/t 恢复

记
$$
M=\ell(2u-\ell Q)-u^2=4bc\delta,\quad
m=u-\ell,\quad T_0=2u-\ell Q-2u^2,\quad V=bX+cY.
$$
原 $E_0$ 给
$$
W_1=bpX+cqY=\frac{T_0+4uf}{2},\quad
x=\frac{\widehat U V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M}.
\tag{2}
$$
这里 $X=x+\rho y,Y=x-\rho y,\rho^2=\delta$。
将正确 compact $R_{\rm true}$ 除去其原 $Q^2$ 尺度后记为 $\mathcal R$，完整恒等式是
$$
\delta\mathcal R=\alpha V+\frac M4t^2+Mu\,t
+\frac m2t(T_0+4uf)-4\delta f(f-u),
\qquad E_1-EW=-2\mathcal R.
$$
在整个 $\alpha=0$ 上，
$$
f=u+\frac{\widehat U t}{4\delta}.
$$
令
$$
R_w=2u(1-u)-uQ+(2u-1)\ell Q,\quad
A_\alpha=M\delta+\{2u(u-\ell)-\widehat U\}\widehat U.
$$
完整代入返回
$$
4\delta^2\mathcal R
=t\{A_\alpha t-2\ell\delta R_w\}.
\tag{3}
$$
当前 W 权坐标
$$
u=e+1,\quad Q=ek,\quad V_b=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV_b},\quad
H=4ek-k^2-4k-8
$$
使
$$
R_w=-\frac{e^2uH}{V_b},\quad
A_\alpha=\frac{e^2u^2(k+2)H(Q-2)}{kV_b^2}.
$$
所有外因子已经支付；$k+2,Q-2$ 源于整个等权排除。故整个 $\alpha=0$ 具有唯一
$$
\boxed{
t=-\frac{2\delta((k+2)^2-2Q)}{(k+2)(Q-2)},\qquad
f=u+\frac{\widehat U t}{4\delta}.
}
\tag{4}
$$
没有额外 $A_\alpha=0$ 分支。并且 $\alpha=0$ 与 $t(f-u)\ne0$ 还付本支的 $\widehat U\ne0$，不将其外推到全部 W。

## 3. 同一点的均值与完整 weighted N/P

(2)、(4) 只余一个几何变量 $V$。本次从完整真 dual Gram 精确返回
$E_0,N_0,P_0,P_1$、$E_1=EW$ 和全部原 $N_1,NS,PS$。

$EW,EBo$ 对 $V$ 二次，平方头分别是
$$
-\frac{2V_2}{M},\qquad\frac{4u\widehat U}{M^2}.
$$
因此
$$
L_m=2u\widehat U\,EW+MV_2EBo
\tag{5}
$$
是原 $V$ 一次行，仍保其一次头零的整支。尤其 $EBo$ 的平方头在本支已付，可供下一常数域原二次模型使用；本次固定结式没有除这个头。

[完整自由 $f,t$ weighted/jet 身份](R150-appendix-unit211-unrestricted-f-and-t-original-low-weighted-NP-identities.md)在同点恢复中给
$$
L_w=NS-PS+E_{W,2},\quad
L_\lambda=NS-PS+N_1+E_{W,2}+2E_p-2uE_1,
\tag{6}
$$
其中
$$
E_{W,2}=b(2p-u-X)E_B+c(2q-u-Y)E_C,\qquad E_p=bpE_B+cqE_C.
$$
源码逐项回乘 (6)，且 $L_w,L_\lambda$ 对 $V$ 至多二次。保留 $N_1,L_w,NS$ 就保留均值商中的两个完整 weighted 值条件，未丢弃原 $PS$。

清分母与原已付内容后，原行次数为：

| 原行 | $(e,k,V)$ 次数 |
|---|---:|
| $EW$ | $(12,13,2)$ |
| $EBo$ | $(14,14,2)$ |
| $L_m$ | $(10,10,1)$ |
| $N_1$ | $(15,17,2)$ |
| $L_w$ | $(14,15,2)$ |
| $NS$ | $(21,23,3)$ |

每个有理原行都完整乘回，未支付新的原 $V$ 头。

## 4. 四个固定 V 投影

首先计算完整固定 $4\times4$
$\operatorname{Res}_V(EW,EBo)$。
只剥已付权内容后得
$$
H_\alpha(e,k),\qquad\deg_{e,k}H_\alpha=(18,19),\quad
\deg_{\rm total}H_\alpha=28.
$$
它有 263 项，精确定义 SHA256 为
d5a72e7a8505c5b70fd5ee2f9e55627c9ced198751111d7ba2f7867adaaa34a2。

另算
$$
R_0=\operatorname{Res}_V(L_m,N_1),\quad
R_1=\operatorname{Res}_V(L_m,L_w),\quad
R_2=\operatorname{Res}_V(L_m,NS),
$$
固定阶数为 $3,3,4$。删除仅已付权内容后，双次数分别
$(22,23),(22,23),(33,33)$，总次数 $34,34,50$。

整个原解必使四个固定投影为零，包括均值头降次、$L_m$ 的一次头零或整条仿射行零的纤维。所有 Bareiss 商积实际返回，所以临时主元零不会被删除。

实际 $\gcd(H_\alpha,R_0,R_1,R_2)=1$ 仅用于无共同曲线的选择。选择的两个原组合恰为
$$
C_0=R_0,\qquad C_1=R_0+R_1+R_2,
$$
且分别与 $H_\alpha$ 的实际 QQ 多变量 gcd 都是常数。这还没有判空；它只保证下面两个真正的一元投影非零，并说明权必要交集有限。垂直 $k$ 分量没有被丢弃。

## 5. 全 QQ 八次覆盖与四重二次因子

两个固定 e-Sylvester 的次数和完整返回如下：

| 原固定输入 | 矩阵阶数 | 原 k 次数 | 精确商积数 |
|---|---:|---:|---:|
| $(H_\alpha,C_0)$，e 次 $(18,22)$ | 40 | 672 | 20540 |
| $(H_\alpha,C_1)$，e 次 $(18,33)$ | 51 | 969 | 42925 |

第一式只剥 $k^{249}(k+2)^{231}(k+4)^{138}$ 后为 54 次，SHA256
d76dac738a1f6b6e1dfbbe9d79fb58c2924bbe5c9cc27deef2f5a6900ce67bce。
第二式只剥 $k^{355}(k+2)^{209}(k+4)^{128}$ 后为 277 次，SHA256
4ad5793f67c5633b5a8e39a0579913deebcbfc81c73bec7f58dac035e500f716。

实际 QQ 两乘回 Bézout 产生首一共同八次多项式 $F_8$；全部因式和重数也乘回，准确为
$$
F_8=(k^2+8k+8)^4.
$$
$F_8$ 定义 SHA256 为
13ead77db31ba4f52bb3c489331082b8ad66343fc6ff96fc1fb26ac9fff78228。
唯一二次因子的升序小参数是 $[8,8,1]$，其字符串规范数组
$["8","8","1"]$ 的 SHA256 为
9526e32c263849d71edfb1f466d3871c3b56b7484047221b42480bb470bf279b，
与此次实际因式日志一致。识别只用这 13 字节精确参数，没有重算旧投影或从旧 t0 结论猜测。

所有固定结式都有原理想伴随来源，最终 Bézout 保留 (1) 的四重结构。下一步须在整个 QQ 二次域返回同一原 $EBo$、其余均值及 N/P；这里只将 $k$ 支持缩到两个共轭根，没有任选一个嵌入或宣布两点排空。

## 6. 实际执行与后继范围

[原源](../notes/2026-11-28-unit211-W-alpha-zero-whole-original-single-V-projections-8542.py)
15909 字节，SHA256 87abb760a803666ff0ec1e8afeb8c7bdc7737d908b5b8d56625856ad04a2cc61。

- run 46111629722，job 140876235155，内层 exit 0；
- 驱动 21.280518074 秒，峰值 RSS 74344 KiB；
- 数学末返回 21.225337345 秒；63687 次精确多项式商积；
- stdout 25365 字节，SHA256 1b447d2de97aff272df04442b72e3b8e8f349efdffacb285a7d0b5632e95e251；
- source/pull commit 7f057637d0a538556e753c816ec0ab2cb9f329b4；
- 05:20:29.944135 UTC 实际 pull，两 README 不变。

[小回执](../notes/2026-11-28-unit211-W-alpha-zero-F8-whole-original-cover-receipt-8542.json)
保存原行/固定矩阵参数、次数与 SHA，不保存可重算大系数。
整个 $\alpha=0$ 仍留 (1) 的完整二次域；整个 $\alpha\ne0$ 补图由另一新的斜率输入继续。
