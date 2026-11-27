# R150 补充：Phi=0 的整个 rho 判别式零权面及原必要曲线

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 判别式零的完整原覆盖

沿用新原坐标 $d=b-c$、$\ell=b+c$、$u=\ell+d\rho$、
$Q=1-\rho^2$。原 $\Phi=0$ 恰为
$$
A\rho^2+B\rho+C=0,
$$
$$
A=\ell-1-2d^2,\qquad B=2d(3-2\ell),\qquad
C=-(\ell-1)(2\ell-3).
\tag{1.1}
$$
本节讨论此 $\rho$ 二次的判别式 $\mathfrak D_\rho$；它不是原 $P_1/N(V)$ 两线的行列式。

完整整数恒等式为
$$
\mathfrak D_\rho=B^2-4AC
=4(2\ell-3)(2b-1)(2c-1).
\tag{1.2}
$$
全等权原排除已付 $d\ne0$，原物理单位支付
$\rho(1+\rho)(1-\rho)\ne0$。

在 $c=1/2$ 上 $\ell=1+d$，(1.1) 精确成为
$$
\Phi=d(1-2d)(\rho+1)^2.
$$
所以原点只能有 $d=1/2$，从而 $b=1$。同理，$b=1/2$ 时
$$
\Phi=-d(1+2d)(\rho-1)^2,
$$
迫使 $c=1$。在 $\ell=3/2$ 上，
$$
\Phi=(1/2-2d^2)\rho^2,
$$
所以也只能有 $d=\pm1/2$。反过来，这两组权重使
$A=B=C=0$，对任意 $\rho$ 都有 $\Phi=0$。

因此在原单位域上，整个 $\Phi=0,\mathfrak D_\rho=0$ 权面恰由
$$
(b,c)=(1,1/2),\qquad (b,c)=(1/2,1)
\tag{1.3}
$$
且 $\rho$ 自由这两条有序权支构成。原 $B/C$ 交换覆盖两支。

这与 $\rho$ 二次头零的主支不同：$A=0$ 的完整分解还包括
$\rho=-d,\ell=1+2d^2$。本篇原源只处理 (1.3)，保留自由 $\rho$，不把它限于头零主支中的两个交点。

## 2. 新两参数原矩与值恢复

选择 $(b,c)=(1,1/2)$，有
$$
\ell=3/2,\qquad u=(3+\rho)/2,\qquad Q=1-\rho^2,
$$
$$
m=u-\ell=\rho/2,\qquad M=2\rho^2,
$$
$$
T_0=(\rho-3)(\rho+1),\qquad J-Q=-(\rho+1)^2.
\tag{2.1}
$$
原 $b,c$ 次序的另一种选择由 $B/C$ 交换处理，因此两参数
$(\rho,\lambda)$ 保持整个 (1.3)。

记
$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell T A_2+2T^3.
$$
原六次矩关系在本支恰为
$$
M K^2-4m^2D^3=\rho^2(2K^2-D^3)=0.
\tag{2.2}
$$
除去原单位 $\rho^2$ 后，$2K^2-D^3$ 的 $T^6$ 首项为常数 $9$。故其首一六次只依赖 $\lambda$，而非 $\rho$。本源的每一次乘法均即时按此原关系约化至 $T$ 次数至多 $5$，保全部原 $T$ 分支。

原 $f,t$ 仍由同一个原 $P_1/N(V)$ 两线恢复。所用权分母是已付 $P_f=T_0(J-Q)$ 等原单位，几何分母只为
$$
D,\qquad S_nZ,\qquad
S_n=D S,\quad Z=2mD\zeta.
\tag{2.3}
$$
完整八个原必要行均已实际返回。两条 $B/C$ 原式同时保留，因实际 $\rho\ne0$，它们的偶、奇谱系数给下表的必要行。没有把单条式拆成两条独立条件。

| 原行 | $(\rho,\lambda,T)$ 次数 | 项数 |
|---|---|---:|
| $E_1$ | $(5,14,5)$ | 450 |
| $E_{B,e}$ | $(5,14,5)$ | 450 |
| $E_{B,o}$ | $(5,14,5)$ | 450 |
| $N_1$ | $(4,14,5)$ | 375 |
| $N_{B,e}$ | $(9,25,5)$ | 1410 |
| $N_{B,o}$ | $(9,25,5)$ | 1410 |
| $P_{B,e}$ | $(9,27,5)$ | 1530 |
| $P_{B,o}$ | $(9,27,5)$ | 1530 |

这些八行在本次实际 $1.934$ 秒内完成；没有新范数逆。

## 3. 实际原单位必要曲线

沿用前一篇已证明的六列同点原 Cramer 构造，本次实际选中
$$
E_1,E_{B,e},E_{B,o},N_1,N_{B,e},N_{B,o}
$$
六条原行，不含 $T$ 倍数。取原单位
$$
U=D S_nZ=2mD^3S\zeta.
\tag{3.1}
$$
设六个原行的坐标矩阵为 $L$，$\Delta=\det L$；
$\Delta_i$ 是把其第 $i$ 行换成 $U$ 坐标后的完整行列式。

本次 $385$ 次 Bareiss 精确除法全部回乘。随后实际验证全部六个坐标的恒等式
$$
\Delta U=\sum_{i=1}^{6}\Delta_i r_i.
\tag{3.2}
$$
令 $g=\gcd(\Delta,\Delta_1,\ldots,\Delta_6)$，把 (3.2) 同时除以
$g$ 后再次完整回乘；这是多项式恒等式，所以保留 $g=0$ 及所有临时主元零纤维。

从 $\Delta/g$ 中只逐次除去与已付原权单位的 gcd。执行记录的来源标签及次数为
$$
u-1:2,\qquad Q:1,\qquad T_0:1.
$$
这里标签标示每次合法 gcd 的原单位来源，不表示每轮都除去整个原单位多项式。规范化非零 QQ 常数后得到唯一确定的必要核心
$$
C_{\rm ex}(\rho,\lambda),
\qquad
\deg_{(\rho,\lambda)} C_{\rm ex}=(31,52),
\qquad \#\operatorname{supp} C_{\rm ex}=1696.
\tag{3.3}
$$
其 SHA256 为
9da42cee8eb94465c733f9606eab7813f5d2db8829525fdcac422fdf9d88b8c1。

相关原多项式的完整数据摘要：

| 对象 | 双次数 | 项数 | SHA256 |
|---|---|---:|---|
| $\Delta$ | $(37,88)$ | 3382 | 846ac47bba8ab59d8f51574e6eb68cadd27ade029638288809e6a28ad2c7e0a4 |
| 公共 $g$ | $(2,36)$ | 74 | 9a902b470d72a8ace3179e9efd62fac6d4eb69be8524e9823cc989126d77de48 |
| $C_{\rm ex}$ | $(31,52)$ | 1696 | 9da42cee8eb94465c733f9606eab7813f5d2db8829525fdcac422fdf9d88b8c1 |

每个原点使全部 $r_i$ 为零，而 (3.1) 非零；(3.2) 的完整公共取消和原单位剥除因此给
$$
C_{\rm ex}(\rho,\lambda)=0
\tag{3.4}
$$
作为整个 (1.3) 的必要条件。

(3.4) 是一条原必要曲线。本次没有排空曲线，没有给出有限点数，也没有把其因子假定成原单位。整个 $\rho$ 判别式零支仍待实际原方程返回。

## 4. 唯一执行与范围

源：

[2026-11-27-unit211-Phi-zero-rho-head-zero-exceptional-weights-original-return-8542.py](../notes/2026-11-27-unit211-Phi-zero-rho-head-zero-exceptional-weights-original-return-8542.py)

- Git blob：bfd6151de6090587eefd3dcfcacb2583975ac5d4。
- SHA256：738d7b965ad82fc67a34251b43f9267adaae738ca7e14bc4574d3cfadb80949d。
- 实际 run：46011857381；job：140549133060。
- 源提交：3579f4aa646ea02dabdcd8f52ad14ec8b03bf3d1。
- 原退出码 $0$；耗时 $6.255342967$ 秒；峰值子进程 RSS $50448$ KiB。
- stdout：$21873$ 字节；SHA256 为 d2baa25ee5f95180cf6a252d187dae45a24a169a2cde704eb7d6d9bce718a360。
- 两 README 的实际 pull／差异记录时间为 2026-11-27 21:59:44（Asia/Taipei），均无变化。
- 固定 $120$ 秒／$1$ GiB；完整八原行、全部七个真实行列式及公共取消后六坐标均已支付。

本源输出明确为 wholeExceptionalConstantWeightBranchesExcluded=false。它提供了整个新原权支的必要曲线；其余 $\Phi=0$ 图及普通 ISP 均没有因此完成。
