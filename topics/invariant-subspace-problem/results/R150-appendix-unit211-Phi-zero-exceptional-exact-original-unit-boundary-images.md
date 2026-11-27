# Phi=0 二次判别式零支：六条原权重零边界的精确 QQ 像

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 范围及结论

本文仅处理已有结果
[R150-appendix-unit211-Phi-zero-exceptional-mixed-original-168-cover.md](R150-appendix-unit211-Phi-zero-exceptional-mixed-original-168-cover.md)
中的有序图
$$
b=1,\qquad c=\frac12,\qquad \ell=\frac32,\qquad
u=\frac{3+\rho}{2},\qquad Q=1-\rho^2.
$$
三条已完成的、来自同一原点的必要多项式记为
$$
F=F_{26,26}(\rho,\lambda),\quad
G=C_{31,50}(\rho,\lambda),\quad
H=C_{34,48}(\rho,\lambda).
$$
本次没有重算其原行列式或投影。程序从三个已发表精确 JSON 读入全部系数，逐文件及逐多项式核对 SHA256。

六个真原权重单位的零边界给出以下完整 QQ 多项式 gcd：

| 固定 $\rho$ | 三个特化多项式的 $\lambda$ 次数 | 完整 QQ gcd |
|---|---:|---|
| $0$ | $26,50,48$ | $1$ |
| $1$ | $17,42,37$ | $1$ |
| $-1$ | $22,46,44$ | $(\lambda-\tfrac12)^3$ |
| $3$ | $26,50,48$ | $H_6(\lambda)$ |
| $-3$ | $26,50,48$ | $1$ |
| $\tfrac32$ | $26,50,48$ | $1$ |

其中首一多项式
$$
H_6(\lambda)=\lambda^6+\frac35\lambda^5-\frac94\lambda^4
-\frac7{10}\lambda^3+\frac{63}{80}\lambda^2
+\frac{39}{80}\lambda+\frac5{64}
$$
在 $\mathbb Q[\lambda]$ 中不可约。等价整系数表达式是
$$
320H_6=320\lambda^6+192\lambda^5-720\lambda^4
-224\lambda^3+252\lambda^2+156\lambda+25.
$$

这些是完整原边界像计算。它们没有排除整条 $\lambda=\tfrac12$ 纤维或整个 $H_6(\lambda)=0$ 纤维：同一个 $\lambda$ 仍可能配有其他物理允许的 $\rho$。因此当前严格的不同有序 $(\rho,\lambda)$ 点数上界仍为 **168**，本次不降低该界，也不宣称整支排空。

## 2. 为什么这些是真原单位边界

在上述固定权图上，$\rho=0$ 是 $1-Q=0$；$\rho=\pm1$ 是 $Q=0$；$\rho=-3$ 是 $u=0$。另有
$$
-T_0=Q+4(u-1)=-(\rho-3)(\rho+1),
$$
以及
$$
u+Q-1=-\frac12(2\rho-3)(\rho+1).
$$
所以 $\rho=3$ 与 $\rho=\tfrac32$ 分别是已付 $T_0$ 与 $u+Q-1$ 单位的零边界。此处考察的是原多项式的完整代数边界值；这些边界点本身不属于原物理图。

程序对每个固定有理 $\rho_0$ 直接用精确有理数计算 $F(\rho_0,\lambda),G(\rho_0,\lambda),H(\rho_0,\lambda)$。没有利用浮点值，也没有把模因式重建猜测当成 QQ 因式。所报 gcd 由精确 QQ gcd 运算取得；对三个特化多项式都完成了除法与乘回，对 QQ 因式分解完成了全部因子的乘积核对。

## 3. 两个真实 QQ 因子与已付固定投影

设原固定 Sylvester 投影为
$$
R(\lambda)=\operatorname{Res}_{\rho}^{(26,31)}(F,G),
\qquad
S(\lambda)=\operatorname{Res}_{\rho}^{(26,34)}(F,H),
$$
相应矩阵阶分别为 $57$ 与 $60$。使用已有的精确次数与首项结果，将 $R$ 规范为在 $\mathbb Z_{(1009)}[\lambda]$ 中首一的 $2033$ 次多项式。这里仍保留固定原次数；特化时首项降低不改变所使用的行列式。

本次给出了两个真 QQ 因子
$$
\phi_1=\lambda-\frac12,\qquad \phi_6=H_6(\lambda).
$$
在 $\phi_1=0$ 时，三条原曲线有同一个边界根 $\rho=-1$；在 $\phi_6=0$ 时，三条原曲线有同一个边界根 $\rho=3$。因此两个固定 Sylvester 矩阵在相应不可约商域中均有非零右核列
$$
(1,\rho_0,\rho_0^2,\ldots)^{\mathsf T}.
$$
于是
$$
\phi_i\mid R,\qquad \phi_i\mid S\quad(i=1,6)
$$
是实际 QQ 一次整除结论。它并不支付更高 QQ 重数。

已保存的完整模 $1009$ 投影实际给出：

| 真 QQ 因子 | 在 $\bar R$ 中的整多项式重数 | 在 $\bar S$ 中的整多项式重数 | 在已付 $\gcd(\bar R,\bar S)$ 中的重数 |
|---|---:|---:|---:|
| $\bar\phi_1$ | $10$ | $10$ | $10$ |
| $\bar\phi_6$ | $2$ | $2$ | $2$ |

这些重数均由完整模多项式的重复整除与乘回取得。把已知像因子的全部模支持从 $168$ 次共同模因子中移除，得到一个 $146$ 次模余式，完整系数保存在回执中。这里的 $146$ 只是后续新输入的模支持次数：因为整 QQ 纤维排除和上述高 QQ 重数尚未支付，不能把它用作新的原点数上界。

## 4. 精确输入及实际执行

唯一执行源：

- [2026-11-27-unit211-Phi-zero-exceptional-168-exact-unit-boundary-images-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-exceptional-168-exact-unit-boundary-images-input-8542.py)
- Git blob：8af878df4eacb690d6f02b66cb5d4af48016d8af
- SHA256：4f9fe288c4b7eb55034f1d8e4d8edc4d98452e8d14899df124d191b4c115156d

三个同目录 JSON 依赖及完整文件 SHA256：

1. 2026-11-27-unit211-Phi-zero-exceptional-F26-exact-input-8542.json：
   67c73f8f5fef33d509ffebd8165487e5b6abcc59fe391acc4075da1f22287d61。
2. 2026-11-27-unit211-Phi-zero-exceptional-PB-core-and-mod-resultant-exact-input-8542.json：
   74891d2b2f8bd21f74ff063cef7aeed85532a2378e71dac07ad5cfc4d240c8c9。
3. 2026-11-27-unit211-Phi-zero-exceptional-mixed-core-and-mod-return-exact-input-8542.json：
   a9ab01ff03d894ed1fe6033b68268ecbf7b9d36dc2cd4ff3d7bf69b771387073。

实际首次 run **46026317409**，job **140598521067**，源提交
e0128091c8aad4cf8ebd6a6487f9ffe69ffaad63。内部执行：
**0.146117349 秒 / 39728 KiB / exit 0**；全部新数学返回在约 $0.093$ 秒内完成。
stdout 为 $6343$ 字节，SHA256
dcf1c389fb35a7204e7feb9373ada5697a33007604b0f0692a9ba08a0b305062。

此结果仅给出上述真原边界像及实际 QQ 一次整除；普通不变子空间问题没有因此解决。
