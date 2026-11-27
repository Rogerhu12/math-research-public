# R150 附录：等单点值碰撞中整个 T0 零面的原排除

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 完整结论

在原 unit211 非零孤立 mean 的 $h=k$ 碰撞图中，
$$
\boxed{T_0\ne0.}
$$
此前 [整个 $T_0=\Delta=0$ 原面](R150-appendix-unit211-equal-singleton-T0-Delta-zero-complete-original-exclusion.md)已用唯一有理基参数和原 mean 常数身份排除。本稿处理互补 $\Delta\ne0$ 面：在两个真实参数 $(\lambda,u)$ 上重建未缩放的完整原 Gram；两个固定四阶原结式的真实 QQ 余式分别为 28 次、12 次，实际扩展 gcd 返回常数 1。

本结论是物理 $D=0$ 碰撞自己的证明，未移用旧 $D\ne0$ 值图的 $T_0$ 定理。现在可在整个原 $h=k$ 图支付 $T_0$，但其他权边界、原第五列和普通 ISP 均未自动关闭。

## 2. 同一点两参数与未缩放原 Gram

仍置
$$
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
\quad \xi=B/A,
$$
$$
\ell=A^3/B^2,\quad T=A^2/B,\quad
w=\lambda-1-T,\quad h=k=1+\xi,
$$
$$
S=2\xi+3-2\lambda,\quad\eta=\xi+3-2\lambda.
$$
在 $T_0=0$ 面，$Q=2u(1-u)/\ell,\ d=1-Q$。直接原式给
$$
bc=\frac{u^2(2\ell-1)}{4d},\quad
P_{02}=uQ(2\ell-1),\quad
\Phi=\frac{2(u-1)(2\ell-u)}{\ell}.
\tag{2.1}
$$
设
$$
Z_\lambda=\frac{(3\lambda-1)(2\lambda-1)}{B},\quad
E=\ell+T,\quad
W_\lambda=w-\lambda\xi(2\ell-1).
$$
原两仿射行在本面有
$$
P_f=0,\qquad N_f=QZ_\lambda,\qquad
\Delta=\Phi QZ_\lambda.
\tag{2.2}
$$
此前已由原第一行证明 $\Phi\ne0$。本稿只在原 $\Delta\ne0$ 补图上，故 $Z_\lambda\ne0$；$u-2\ell$ 由 (2.1) 同时是合法单位。

原解的两个 Gram 参数可准确写成
$$
f=
\frac{u\{uS\xi(2\ell-1)E-(u-2\ell)\eta W_\lambda\}}
{(u-2\ell)Z_\lambda},\qquad
t=-\frac{4dE}{u-2\ell}.
\tag{2.3}
$$
源将 (2.3) 代回原两条仿射行，并验证 $f\Delta=F$。所有分母都属于本原补图的已付单位；没有新加一般权条件。

以原 $p=1+\rho,q=1-\rho,\rho^2=d$、
$$
b=\ell/2+(u-\ell)/(2\rho),\quad
c=\ell/2-(u-\ell)/(2\rho),\quad a=1-\ell
$$
重建原双点 Gram。具体仍从
$$
W_1=T_0/2+2uf,\quad
W_2=uT_0+\lambda P_{02}+(V_2+2u^2)f-bcQt,
$$
$$
X=\frac{cq(qW_1-W_2)}{bcQ(q-p)},\quad
Y=\frac{bp(W_2-pW_1)}{bcQ(q-p)}
$$
得到 $r=X-ap-ct,s=Y-aq-bt,A_1=2f-2bX-2cY+2bct$，四行是
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0).
$$
这是未缩放的 $H=1$ 原 Gram。完整 moment、$E_0,N_0,P_1,N_4(V)$ 均实际逐式返回。两个 singleton 的 N 目标仍为 $2\lambda P_{02}(1+\xi)^2$，P 目标仍为 $P_{02}(1+\xi)^3$。

因为两条实际 B/C 原式同时存在、互为共轭且 $\rho\ne0$，其偶、奇两系数为必要式。这不把单独一条扩张方程任意拆成两条零式。

## 3. 全八原式与严格单位剥除

各系数分母逐项只用 $A,B,Q,d,bc,\Phi,N_f$ 的分子因子审计，完整清分母后每次除法均回乘。primitive 化额外只允许原 $\lambda,P_{02},S,u-\ell$ 等已经支付的原单位；后者由整个等权碰撞原排除支付。本次没有剥任何尚未排除的几何首项。

完整八原必要多项式的双次数与项数为：

| 原行 | $(\deg_\lambda,\deg_u)$ | 项数 |
|---|---:|---:|
| $E_1$ | $(20,2)$ | 60 |
| $E_{B,e}$ | $(17,3)$ | 71 |
| $E_{B,o}$ | $(17,2)$ | 53 |
| $N_1$ | $(16,2)$ | 48 |
| $N_{B,e}$ | $(34,4)$ | 164 |
| $N_{B,o}$ | $(27,3)$ | 109 |
| $P_{B,e}$ | $(34,5)$ | 199 |
| $P_{B,o}$ | $(28,4)$ | 138 |

每个原分子的完整 QQ 因式分解均实际乘回。所有原值条件保留；下面只需其中三行就足以得到矛盾。

## 4. 两个固定四阶原 QQ 投影即返回单位

对 $(E_1,E_{B,o})$ 和 $(E_1,N_1)$ 的 primitive 二次 $u$ 多项式，各自构造固定 $4\times4$ Sylvester 矩阵。每条矩阵行由原多项式及其单项式倍乘重建，并逐行乘回。

因此任何原共同有限 $u$ 都使两个行列式为零，即使其二次首项在某个 $\lambda$ 上退化。该必要性不要求参数首项可逆。

| 原对 | 固定阶数 | 原 $\lambda$ 行列式次数 | 只剥已付原单位后 |
|---|---:|---:|---:|
| $(E_1,E_{B,o})$ | 4 | 71 | 28 |
| $(E_1,N_1)$ | 4 | 67 | 12 |

记最后两个首一 QQ 多项式为 $R_{28},R_{12}$。其完整升幂系数保在回执，规范 SHA-256 分别为

- 1f095dbc25f38faaa5e9f9c838299f81540286d5ed22e2d47c1a26030669658d；
- 6ca957d7057444ea04ad32d7f42b205722a3969d3e8e035f691fcf356d435364。

原 71 次行列式只剥 $A$ 因子 12 轮、原 $bc$ 因子 5 轮、本补图 $N_f$ 因子 2 轮、$\lambda$ 因子 3 轮；原 67 次分别为 16、5、4、4 轮。这里“轮”是对指定已付多项式做真实 gcd 后的完整回乘，不将这些数字混称为每个不可约因子的重数。

实际 QQ 扩展 gcd 和累计标签乘回给
$$
\boxed{a(\lambda)R_{28}(\lambda)+b(\lambda)R_{12}(\lambda)=1.}
\tag{4.1}
$$
故不存在两个投影的公共复根，更不存在原点。这个排除直接在 QQ 中成立，不需要好素数提升或进一步有限纤维筛选。

连同已排的 $\Delta=0$ 面，整个 $T_0=0$ 碰撞面排除。除了这两个互补原面，没有丢掉任何 $T_0=0$ 参数。

## 5. 实际执行身份

[两参数原返回源](../notes/2026-11-27-unit211-equal-singleton-T0-nonzero-Delta-original-two-parameter-return-8542.py)：

- git blob：55898c9cc67257b5e22fbd5fe0af851bfbaee0c3。
- SHA-256：031d1737a60b359ffd82231b374efec96232fdc64ceda551aa55d91fe39d1bba。
- [Actions run 46011596196](https://github.com/Rogerhu12/math-research-public/actions/runs/46011596196)，job 140548221367，inner exit 0。
- 源 0.162297511 秒，驱动 0.222151756 秒，子进程峰值 41044 KiB。
- stdout 33432 字节，SHA-256 6a8dc83dc5d350d02a15ce88a605598342e8c92e9ca3b8b7b91d4accbb6755bc。
- Python 3.12.14、python-flint 0.9.0、单线程；180 秒/4 GiB上限。
- 2026-11-27 13:57:50 UTC 实际 pull 到 6110da26281f1154fbaa8b0751189be88c5b1adc，根及本题 README 无差异。
- [完整小执行回执](../notes/2026-11-27-unit211-equal-singleton-entire-T0-zero-exclusion-receipt-8542.json)保全八 primitive 因式、两个固定投影、QQ gcd 和原执行状态。

所有已成原行、单位剥除及两个投影只运行本次需要的返回。源在第二个投影返回单位后即结束，没有再运行其他候选投影。下一原权面 $J=Q$ 及整个一般碰撞仍开放。
