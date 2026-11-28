# R150 补充：整个当前 W 的 f=u 原分支排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完整结论

在当前已声明的原物理 W 图内，整个
$$
\boxed{f=u}
$$
分支没有原解。已发表的
[整个 t=0 排除](R150-appendix-unit211-W-entire-t-zero-complete-original-exclusion.md)
覆盖其 $t=0$ 部分；本篇用同一个完整原 Gram 排除全部 $f=u,t\ne0$。

因而后续当前 W 可合法使用 $f-u$ 和 $t$ 作为原单位。本结论不外推至其他一般 LS 权图，也没有宣称整个 W 或普通 ISP 已完成。没有回放此前 t=0 的三个结式或两个常数域返回。

## 2. 保全部均值头零的单几何坐标

沿当前 W 权坐标记
$$
u=e+1,\quad Q=ek,\quad V_b=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV_b},
$$
$$
\delta=1-Q,\quad V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
M=\ell V_2-u^2=4bc\delta,\quad g=2\ell-1.
$$
这里 $M$ 是已付原单位。令
$$
V=bX+cY,\quad \omega=2V-(1+2\ell)u,\quad
\widehat U=V_2-u.
$$
本篇使用 $\omega$ 区别原值变量 $w=\lambda-1-T$；源码的自由变量名为 w。

在 $f=u$ 下，原 $E_0$ 精确恢复
$$
x=u+\frac12+\frac{\widehat U\omega}{2M},\qquad
y=\frac12-\frac{u\omega}{2M},\qquad X=x+\rho y,\quad Y=x-\rho y,
\quad \rho^2=\delta.
\tag{1}
$$
真正原 dual 均值给完整因式
$$
E_1-(bE_B+cE_C)
=-2bc\,t\left(t-2-\frac{2\widehat U\omega}{M}\right).
\tag{2}
$$
因此整个 $t\ne0$ 图必须且无遗漏地满足
$$
\boxed{t=2+\frac{2\widehat U\omega}{M}.}
\tag{3}
$$
(2) 亦由已纠正的原 $R_{\rm true}$ 身份直接得到：在 (1) 上
$$
R_{\rm true}=bc\,Q^2t\left(t-2-\frac{2\widehat U\omega}{M}\right),
\qquad E_1-EW=-2R_{\rm true}/Q^2.
$$
这里没有倒置 $V_2,\widehat U$ 或任意新均值头。源码在同一个 (1)、(3) 原 Gram 中完整返回 $E_0,N_0,P_0,P_1$ 及 $E_1=EW$，并保正确的 $-4d_0d_1$ 项。

记
$$
A=2\widehat U^2-\delta V_2,\quad B=g\delta V_2-2M,
$$
$$
R_0=u-1+(1-\ell)Q,\quad
C=(u-\ell)\widehat U+u\ell\delta,\quad D_2=u\delta-C.
$$
两个尚需满足的完整均值精确是
$$
2M\delta EW=A\omega^2+MB,
\qquad
M^2\delta EBo=\widehat U D_2\omega^2+M^2R_0.
\tag{4}
$$
不除任何平方头，原组合即给
$$
F_u=AMR_0-B\widehat U D_2
=AM\delta EBo-2\widehat U D_2\delta EW.
\tag{5}
$$
所以 $A=0$、$\widehat U D_2=0$ 及其交点全部保留。

## 3. 整四次权曲线

W 权代入后，完整乘法身份为
$$
F_u=\frac{e^3u^2(Q-1)\ell H}{V_b^3}K_{fu},
\qquad H=4ek-k^2-4k-8,
$$
其中
$$
\begin{aligned}
K_{fu}={}&-8k^2e^4+(32k+16k^2+6k^3)e^3\\
&-(32+32k+16k^2+4k^3+k^4)e^2\\
&-(16k+18k^2+7k^3+k^4)e
 +16+20k+8k^2+k^3.
\end{aligned}
\tag{6}
$$
外因子在当前 W 均已付，故整个原分支满足 $K_{fu}=0$。
它有 17 项，双次数 $(4,4)$、总次数 6；$e^4$ 头为 $-8k^2$，没有垂直 $k$ 分量。

源码按有理内容规范化所得 $H_4$ 与 (6) 仅差非零有理常数；其完整规范定义 SHA256 为
b7b0b20da6d44a9f3a2594e7f4fc1e9ddad009dd63581612ebd8eee20592698d。
此次完整 QQ 因式乘回只得一个次数 $(4,4)$ 的因子，重数 1。下面的排除并不依赖把它误当一个已付单位。

在同一 $(x,y,t)$ 恢复同一 $\lambda,T$，按完整原定义构造 $N_1,NS,PS$。
所有分母只来自
$$
e,k,u,Q-1,V_b,k+4,P_{02},M,k+1,H,k+2,\ell,L_{\rm half},
$$
其中 $L_{\rm half}=-kV_b(2\ell-1)$；这些是当前已经支付的原单位。清分母和删除已付内容都逐项乘回。没有删除未知公因子或新的值头。

## 4. 六个保次数的原 w 结式

依次取
$$
\operatorname{Res}_{\omega}(EW,N_1),\
\operatorname{Res}_{\omega}(EW,NS),\
\operatorname{Res}_{\omega}(EW,PS)
$$
及将第一行改成 $EBo$ 的三式。使用原全系数的固定 Sylvester 矩阵，阶数分别为 $4,5,5,4,5,5$；每一步 Bareiss 整除均实际乘回。

只剥已付纯权内容后的六式记 $\mathcal R_0,\ldots,\mathcal R_5$：

| 原两行 | 双次数 $(e,k)$ | 总次数 |
|---|---:|---:|
| $EW,N_1$ | $(21,23)$ | 33 |
| $EW,NS$ | $(37,39)$ | 58 |
| $EW,PS$ | $(37,38)$ | 57 |
| $EBo,N_1$ | $(23,27)$ | 39 |
| $EBo,NS$ | $(37,40)$ | 62 |
| $EBo,PS$ | $(37,39)$ | 61 |

任何同一原 $\omega$ 都使六个固定行列式为零。某条均值头退化、整条均值专门化为零、两条同时降次时，这个必要性仍成立。固定 Sylvester 的伴随身份也给原理想来源；临时消元主元从未被当成物理单位。

实际 $\gcd(H_4,\mathcal R_0,\ldots,\mathcal R_5)=1$，在本证明中只用来确认没有共同曲线。它不是排空依据。

## 5. 两个完整一元 QQ 投影及最终 Bézout

取真正原线性组合
$$
C_c=\sum_{j=0}^5c^j\mathcal R_j.
$$
实际 $c=1,2$ 均满足 $\gcd(H_4,C_c)=1$；二者双次数都是 $(37,40)$，总次数 62。

这一步的完整覆盖原则是：$H_4$ 的 $e$ 次数为 4，且没有垂直 $k$ 内容，故至多有四个不同曲线分量；对每个分量，$C_c$ 是关于 $c$ 的非零五次以下多项式。固定 $c=0,\ldots,21$ 至少有两个适用值。本次实际使用的恰为 1、2；未把该原则替代真正投影计算。

计算两个固定 $41\times41$ Sylvester 行列式
$$
S_c(k)=\operatorname{Res}_e(H_4,C_c),\qquad c=1,2,
$$
固定次数为 $(4,37)$。两个完整 QQ 投影均为 244 次，各有 22140 次精确商积返回；全部 $e$ 头零纤维仍被包含。

二者均只剥以下已付因子：
$$
S_c(k)=\gamma_c\,
k^{75}(k+1)^6(k+2)^{42}(k+4)^{30}L_c(k),
\qquad \gamma_c\in\mathbb Q^\times,
\tag{7}
$$
$L_1,L_2$ 为首一 91 次。其精确定义 SHA256 分别为

- $L_1$：36b3928a91271e4679cac23879cc8b7d9e2c4be1fa421212059e5e42e3b98840；
- $L_2$：0066dc38e5c50e334f06cdae31a35db5fdb3451c3242022d565c55b98ba2dde3。

最后在 $\mathbb Q[k]$ 中实际求得并完整乘回
$$
A_1(k)L_1(k)+A_2(k)L_2(k)=1.
\tag{8}
$$
故任何原物理 $k$ 都不能同时满足两条必要投影。这里没有取模、没有数值采样，也没有由多变量 gcd1 直接判空。

(8) 排除整个 $f=u,t\ne0$。合第 1 节已成整个 $t=0$ 结果，完整关闭当前 W 的 $f=u$。所有原首项零、固定结式降次和非约化重数都由同一多项式身份保留，不再有未处理的有限候选。

## 6. 首次实际执行

[自含原源](../notes/2026-11-28-unit211-W-f-equals-u-t-nonzero-whole-original-projections-8542.py)
为 14529 字节，SHA256
5bc14c2eda09fe876d5c1bb659203d29aea8b0cf20b439920bcc8ed857e66770。
未调用任何旧门或旧参数输出。

- run 46109873355，job 140870811382，唯一首次内层 exit 0；
- 驱动 0.840327719 秒，峰值 RSS 46208 KiB；
- 数学末返回 0.789087036 秒，44628 个完整多项式商积；
- stdout 24289 字节，SHA256 b5cbaf90d08d8ffa3efd6d4cb9eb98a8f2bbcae94d9d11beee1fbad54344ed9d；
- source commit 7b9c9becb081552a8c55fd4d52f862eb804d713a；
- 04:57:29.292677 UTC 实际 pull 到 111f36cc51dd4471dea25782e8dc013580b59866，两 README 无变化。

[小执行回执](../notes/2026-11-28-unit211-W-entire-f-equals-u-complete-original-exclusion-receipt-8542.json)
保留原矩阵/投影参数、精确次数和 SHA；不保存可重算系数缓存。后续转当前原补图 $f\ne u$，不重复本支结式。
