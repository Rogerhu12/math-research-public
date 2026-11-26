# R150 / L0：原 P1/E1 的完整 rho 首项零曲线排除

作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127；2026-11-27（台北）。

**状态：已证明。** 剩余原 L0 图中，原 $P_1$ 返回 $E_1$ 所得 $\rho$ 五次式的整个首项零面为空。因此这个原必要式可合法首一化为 $\rho$ 五次式。所有参数首项降次均保留；一般 L0 仍未排除。

## 1. 原来源和唯一未付首项因子

使用[整个 K 曲线正文](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-K-curve-complete-exclusion.md)的原九式、三个参数 $\rho,\lambda,w$ 及所有原物理单位。整个 $W,G,K$ 曲线已闭，原 $P_1=\alpha t+\beta$ 的 $\alpha$ 也已付为单位。

将同一个原 $P_1$ 返回到 $E_1,N_1,E_{B,e}$ 后的必要式记为 $F_E,F_N,F_B$。它们均从正确双点 Frobenius 乘法及原方程直接重建，分别为此前登记的 `P1_E1`、`P1_N1`、`P1_EBe`。令

$$R=\lambda-1-w,\quad A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,\quad C=RB-A^2.$$

原 $F_E$ 对 $\rho$ 次数为五，其首项的完整非恒定因子为

$$R^2 W C V,$$

只差非零有理常数。这里

$$W=4\lambda w+2\lambda-2w^2-4w-1,$$

而 $V$ 取剥除原单位后的规范，$(\lambda,w)$ 次数为 $(4,6)$，27 项。全部系数由原 $F_E$ 首项唯一确定；其 SHA-256 为

`2cb9819af2ad4da973bc3abbf2f06d07f00cd1432f820fb534734ee0b24ca10e`。

上述首项中出现的另一六项因子

$$4\lambda^3w+2\lambda^3-6\lambda^2w-\lambda^2+3\lambda w-w=-C$$

是原物理单位，不能误当成新的未付曲线。$R,C,W$ 已付，所以本条只须排除整个 $V=0$。

## 2. 完整原投影保留所有 rho 与 w 首项零

先在 $\mathbf Q[\rho,\lambda,w]$ 中重建两个完整 $\rho$ 结式。剥除仅已付的原物理单位及 $W,G,K$ 后得到

$$X=\operatorname{norm}\operatorname{Res}_\rho(F_E,F_N),\qquad Y=\operatorname{norm}\operatorname{Res}_\rho(F_E,F_B).$$

它们正是剩余原图必须满足的两个完整曲线：

| 多项式 | $(\lambda,w)$ 次数 | 项数 | SHA-256 |
|---|---|---:|---|
| $X$ | $(34,52)$ | 1580 | `519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68` |
| $Y$ | $(78,95)$ | 6379 | `c696ee10ac72763cbc2d9e01cd84cdda6bfd5116faa3262ddbf6f96490c54d33` |

此处未倒置待证明的 $V$，也没有用 $F_E$ 的 $\rho$ 首项非零。任何原解即使落在该首项零面，仍使这两个完整 Sylvester 结式为零。

在 $V=0$ 上取完整 $w$ 结式

$$P(\lambda)=\operatorname{norm}\operatorname{Res}_w(V,X).$$

它为 301 次非零有理多项式；平方自由部分为 205 次，完整不可约因子次数为

$$1,2,32,170.$$

平方自由除法及全部因子乘积均实际乘回。两个小因子为

$$2\lambda-1,\qquad8\lambda^2-6\lambda-1.$$

整个过程没有倒置 $V$ 或 $X$ 的 $w$ 首项。因此其任意降次纤维也包含在这份完整覆盖中，不需假定 $V$ 恒为六次。

## 3. 两个大参数域的严格一元排除

设完整有理一元多项式

$$S(\lambda)=\operatorname{Res}_w(V,Y).$$

源在素数 1031 下逐个检查 $V,Y$ 的系数分母为局部单位，并核验原 $w$ 次数 6、95 在约化后保持。所以实际计算的 $\bar S$ 是原完整 Sylvester 结式的精确约化。

对 205 次覆盖中唯一的 32 次和 170 次不可约因子 $\phi$，源分别核验 $\deg\bar\phi=\deg\phi$，并实际乘回

$$a\bar\phi+b\bar S=1.$$

因此 $\phi,S$ 在 $\mathbf Q[\lambda]$ 中互素。确切地，若有正次数有理公因子，因 $\phi$ 的所有系数在 $\mathbf Z_{(1031)}$ 中且首项是单位，Gauss 引理允许把公因子取为该局部环上的首一多项式。约化后它仍有正次数且整除两个约化，违反上述 Bézout 身份。

这是一元有理有限覆盖的排除，不是将多变量模素数单位理想提升。也不需要宣称 $S$ 的 $\lambda$ 次数保持；保证公因子次数保持的是实际 $\phi$ 的单位首项。

## 4. 两个小参数域的同点完整返回

在两个完整域 $\mathbf Q[\lambda]/(\phi)$ 中返回原 $V,X$，保留同一个 $w$，精确 Euclid 得到：

| 完整参数域 | 原公共 $w$ 多项式 | 原矛盾 |
|---|---|---|
| $\lambda=1/2$ | 非零常数倍的 $w^2$ | 原 $w\ne0$ |
| $8\lambda^2-6\lambda-1=0$ | 非零常数倍的 $(w-1)^2$ | 已闭原 $w=1$ 支 |

源分别完成 14 和 17 次域逆乘回，并逐次核验多项式除法与 Bézout 身份。两次剥除后的公共多项式均为非零常数。第二行在整个二次域运算，包含其两个复嵌入，没有分别为 $V,X$ 选根。

四个参数域至此全部排除，所以整个 $V=0$ 不含剩余原解。

由第 1 节的准确首项因子分解，现在 $F_E$ 的整个 $\rho$ 五次首项均为已付单位。后续可在原图上使用对应首一五次关系，所有除法仍须保存原身份；不能直接删除其他原 $N/P$ 方程。

## 5. 自包含源与真实运行

源：[2026-11-27-unit211-L0-V-complete-original-return-8542.py](../notes/2026-11-27-unit211-L0-V-complete-original-return-8542.py)。无参数，从原九式、两个完整 $\rho$ 结式及原首项重新构建全部输入，不读取 scratch 系数。

- Python 3.12.14、python-flint 0.9.0；180 秒源内 alarm、4 GiB 地址空间、210 秒外部硬超时。
- 源 18356 字节，SHA-256 `39efe1cbf347ab72879c0c5fa1e76ab7e082438febaedd5a6fc1a809de627352`。
- 实际退出码 0；外部墙钟 **38.595274 秒**，源内 **38.453523 秒**，最大 RSS **115276 KiB**。
- stdout 11953 字节，SHA-256 `c39f61b9870d483767a28cc24f195189fe85108a987a29ade0892997fba10d9f`。
- [紧凑回执](../notes/2026-11-27-unit211-L0-V-complete-original-execution-8542.json)保全部参数域、实际模 gcd 及末原返回；大系数可由源重算，不入库。

另一次直接构造 $\operatorname{Res}_w(X,Y)$ 的探查只返回上述两个原输入，在新投影 BEGIN 后未返回系数，外部 180 秒硬限退出 124；源内投影 alarm 设 120 秒，但无已交付的 timeout 记录，不将其标成完成或声称获得结式。[准确失败回执](../notes/2026-11-27-unit211-L0-XY-direct-projection-timeout-8542.json)已保留，此大输入冻结。本条改用低次原首项曲线并完整闭合。

当前继续 $W,G,K,V$ 非零下的完整原 L0 系统。$X=Y=0$ 的一般原交点、Bell 真幂来源、算子桥及普通复 Hilbert ISP 仍开放。
