# R150：一般 LS 零行列式图的 W 参数首项零支完整排除

**状态：已证明。** 在原三值互异、$LS\ne0$、原两线行列式 Delta=0 图中，整个 $u=1/2,Q=2$ 分支排空。它恰覆盖下述小权多项式 W=0 对 ell 的首项零支。因此在 W=0 图上可以合法除以 $u(Q+2)-2$ 来解 ell。一般 W=0、一般 Delta=0 与一般 LS 尚未排空。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 需要支付的首项及完整覆盖

沿用 `results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-Delta-zero-global-monic-value-quadratic.md` 的原坐标、单首项值二次式和三条原一次返回。其小权多项式是

$$\begin{aligned}
W={}&\ell uQ^2+2\ell uQ-2\ell Q+2u^3Q-4u^3\\
&-8u^2Q+8u^2-uQ^2+6uQ-4u.
\end{aligned}$$

W 关于 ell 一次，首项为 $Q V$，其中 $V=u(Q+2)-2$。新源实际核验完整 QQ 结式

$$\operatorname{Res}_u(W,V)=2Q^3(Q-2).\tag{1}$$

在 W=V=0 且原 $Q\ne0$ 上，(1) 给 Q=2，随后 V=0 给 u=1/2。反向代入也使整个 W 为零，ell 完全自由。没有丢失 ell 首项、重数或复嵌入。

原 Delta 零图上 $\Phi\ne0$ 的支付已经由原 P1 双系数零整支排除给出；其论证是原 $N_t=bcQS\zeta\ne0$，故 Delta=0、$P_t=0$ 会强制 $P_f=0$。本稿未假设一般图上的 Phi 非零。

## 2. 同一原 Gram 的四个二次式

在 $u=1/2,Q=2$ 上，原物理因子为

$$\Phi=\tfrac12-2\ell,\qquad P_{02}=-\ell-\tfrac14,\qquad
M=\ell-2\ell^2-\tfrac14,$$

以及 $D=\ell(2\lambda^2-2\lambda+1)-T^2\ne0$。

用同一个原 P1 解 t 后，原 $E1,EB_e,EB_o,N1$ 给四个关于 $(\lambda,T,f)$ 的总次数二次式 $q_0,q_1,q_2,q_3$，其系数在 $\mathbb Q[\ell]$。新源自原 Gram、正确双点乘法、原最高式和第二梯度极化构造它们；没有输入外部缓存系数。四式的 ell 次数依次为 6、7、6、6。

各式乘全部总次数不超过 2 的十个 $(\lambda,T,f)$ 单项式，得到 40 行，作用于总次数不超过 4 的 35 个真实单项式（常数 1 最后一列）。源码逐条重建全部 40 行，实际检查每个行多项式等于原 $q_i$ 乘相应单项式，并检查所有已付内容因子乘回。

这张矩阵的 35 阶满秩行列式恒零；它本身不是排空证据。后续使用其原 34 阶子式和真实单项式的乘法一致性。

## 3. 315 条原 Cramer 系数身份与 37 次一致性覆盖

分式无消元保留完整多项式除法身份，得到一个非零 34 阶子式 $\delta(\ell)$，次数 176。对九个单项式

$$\lambda,\ T,\ f,\ \lambda^2,\ \lambda T,\ T^2,\ \lambda f,\ Tf,\ f^2$$

分别构造一个 40 分量多项式 cofactor 行。令形式右核列的相应分量为 $r_m(\ell)$。源码对每个目标逐列核验

$$c_m\mathcal M=\delta e_m-\delta r_m e_1.\tag{2}$$

这里 $e_1$ 指常数 1 列，共有 **9×35=315 条实际系数乘回**。每个 cofactor 都是 $\mathbb Q[\ell]$ 多项式，且 $\delta r_m$ 为多项式。(2) 直接给出任何原解在 $\delta\ne0$ 时的必要恢复值；不假定形式右核列自动满足单项式乘法。

接着对六个二次单项式计算

$$r_{xy}-r_xr_y.$$

它们的分母都实际整除 $\delta^2$，因此在当前图上是单位。六个分子的 QQ 扩展 Euclid 都逐次乘回，得到共同必要因子 $C_{37}(\ell)$。前两个差的分子次数为 70、69，其 gcd 已为 37 次；其余四个仍返回同一因子。

$$\deg C_{37}=37,\qquad
\mathrm{SHA256}(C_{37})=\texttt{a2d35edd555b3de5c0a577bcc5382ac7501360f0a5f75c1a9148b5d109530ae9}.$$

所以任何原解必须落在 $\delta=0$ 或 $C_{37}=0$。这一覆盖来自原 cofactor 与真实乘法身份，不是数值采样，也不是把自由形式列视为实际点。

## 4. 子式的全部因子和 98 次有限覆盖

完整 QQ 因式分解连同有理内容实际乘回为

$$\delta\doteq(4\ell-1)^{46}(4\ell+1)^{24}
(8\ell^2-4\ell+1)^{22}(2\ell-1)^2
C_6C_{11,a}C_{11,b}C_{32}.\tag{3}$$

只有前三项由原 Phi、P02、bc 支付；它们的全部幂逐一准确除去。没有把 $2\ell-1$ 当作一般单位。余因子和一致性因子给出 98 次平方自由覆盖，包含整个 ell=1/2 纤维。新源实际检查这个 98 次乘积与其导数的 gcd 为 1。

| 因子 | 次数 | SHA256 |
|---|---:|---|
| $C_{37}$ | 37 | `a2d35edd555b3de5c0a577bcc5382ac7501360f0a5f75c1a9148b5d109530ae9` |
| $C_6$ | 6 | `48057bccd022301c075804bcae5e681a7524117e80c377e7bc1c52fd29077bb9` |
| $C_{32}$ | 32 | `e977558e484bcaf1c2de5838464bd93a59ccbf7febc9120f3339dcb4fccbee2d` |
| $C_{11,a}$ | 11 | `c470af408fdaf3ea663f5bd40b7259843c2b8115f0f0f7f41ff6f3467b03747c` |
| $C_{11,b}$ | 11 | `77455933b9a95f9f15d6e765e59bfdb6183bf55866cdb86365a2f7308cbff936` |
| $2\ell-1$ | 1 | 该整有理纤维在第 6 节单独返回 |

(3) 的每个因子和有理内容都由自含源再生并相乘核验；不需要假定这些多项式不可约。

## 5. 97 次非 half 候选的原完整双层一元返回

四个原 f 二次式的常数列三阶子式给 $F_0,F_1$。同一原值矩阵中 $(H_A,H_B,E_\Delta)$ 的常数列子式，除去已付 Phi 后，恰含因子 $2\ell-1$。在本节 $\ell\ne1/2$ 图上再准确除去该因子，记余式 $Z_0$。所有子式来源、常数列身份和剥除乘积都在新源前段重建。

$$\deg_{(\ell,\lambda,T)}F_0=(9,3,3),\quad
\deg F_1=(14,3,3),\quad\deg Z_0=(3,4,4).$$

计算两个**实际 QQ 完整 T 结式**

$$R_0=\operatorname{Res}_T(F_0,Z_0),\qquad
R_1=\operatorname{Res}_T(F_1,Z_0).$$

原 T 次数均为 3、4；结果 $(\ell,\lambda)$ 次数为 (36,12)、(56,12)，项数 460、720。首项零纤维始终保留。两个结式的 SHA256 分别为

- `ed12620c528b1e97edfe979986775c2f021b5135d3001a0224cff8f6deb4fc33`；
- `c9b582996a120ed2aea7dcf55e1f6e782a3f7bf9526fd26f48218faf98c2f5e2`。

令完整 QQ 多项式 $S(\ell)=\operatorname{Res}_\lambda(R_0,R_1)$。源码在模 1009 下计算这个完整 Sylvester 行列式的约化；两个输入的原 lambda 次数 **12、12 均保持**，所有 QQ 系数的分母均为 1009 单位。所得 $\bar S$ 为 1068 次，SHA256 为 `71660e998374a42083899f2b356281d3ed10fdd744dc8b3258928efc0a5bd7ae`。

对上述五个整 QQ 候选，实际分别计算两个乘积与和，验证

$$a\bar C+b\bar S=1.$$

| 整 QQ 候选 | 在 1009 的首项 | Bézout 系数次数 |
|---|---:|---|
| $C_{37}$ | 1 | (1067,36) |
| $C_6$ | 512 | (1067,5) |
| $C_{32}$ | 168 | (1067,31) |
| $C_{11,a}$ | 617 | (1067,10) |
| $C_{11,b}$ | 813 | (1067,10) |

每个候选的单首项 QQ 版本系数都在 $\mathbb Z_{(1009)}$ 中，且其次数保持。因此若 C 与 S 有共同复根，其单首项 QQ 最小多项式由 Gauss 引理可在该局部整环中约化为正次数公共因子，与实际 Bézout 身份矛盾。这排除五个候选的全部复嵌入。

这里使用的是已经从原 cofactor 证明的完整 QQ 一元覆盖，以及两个实际 QQ T 投影产生的完整 lambda 一元结式。没有从任意多变量模单位推断 QQ 空集。

## 6. 整个 ell=1/2 纤维的 QQ 返回

在 ell=1/2，原必要子式在非零 QQ 倍数意义下包含

$$(2T+1)C,\quad F_1,\quad F_2,\quad Z,$$

其中

$$C=9\lambda^2+36\lambda T+9\lambda+54T^2+33T+5,$$

$$F_1=12\lambda^3+36\lambda^2T+4\lambda^2+24\lambda T^2
-16\lambda T-9\lambda-42T^2-32T-6,$$

$$F_2=6\lambda^2T+5\lambda^2+48\lambda T^2+40\lambda T+6\lambda
+108T^3+126T^2+47T+6,$$

$$Z=(2T+1)(3\lambda-6T-4)
(6\lambda^2-8\lambda T-14\lambda+4T^2+12T+9).$$

所有非零 QQ 比例均实际乘回。

若 $T=-1/2$，则原 $F_2=(2\lambda-1)^2/2$，故 lambda=1/2。此时原 D=0，矛盾。

余支 C=0。令

$$C_5=432\lambda^5-288\lambda^4-186\lambda^3+108\lambda^2+40\lambda-19.$$

完整原结式准确为

$$\operatorname{Res}_T(C,F_1)=162\lambda C_5,$$

$$\operatorname{Res}_T(C,F_2)=972(3\lambda-1)C_5.$$

它们的实际 QQ 线性组合给 C5，无需倒置 lambda 或 $3\lambda-1$。另一原完整结式为

$$\operatorname{Res}_T(C,Z)=576(27\lambda-14)
(10368\lambda^3-26496\lambda^2+22065\lambda-5929)
(3\lambda-2)^2(3\lambda-1)^2.$$

此 8 次多项式与 C5 的 QQ 扩展 Euclid 准确返回 1，两个乘积都实际核验；系数次数 (7,4)，合并 SHA256 为 `1b5520fc73574b21344847ee3cc762c2630e728d3c085ca9ad67f12b22b2332a`。故整个五次候选也排空。

(3) 的所有有限候选及 $C_{37}$ 至此无剩余，原 $u=1/2,Q=2$ 整支排除成立。

## 7. 自含证书、实际回执与后续已付范围

自含源：`notes/2026-11-27-unit211-generic-LS-Delta-zero-W-leading-zero-original-return-8542.py`。

- 源 SHA256：`3769e6d602dd3c153e33991f15cd04d97f0b9cbbc6010666611f777ccee2c397`。
- 实际 exit 0；墙钟 **6.831982 秒**；源内完成 6.684575 秒；峰值 RSS **55268 KiB**。
- 配置上限 240 秒、4 GiB。
- stdout 24062 字节，SHA256 `818fd39f32a0d3b2ef91a5d72d74764d4c607b7443f6b71736e1cfbf4fe64186`。
- 回执：`notes/2026-11-27-unit211-generic-LS-Delta-zero-W-leading-zero-execution-8542.json`。

源码只使用其内重建的原式，无仓库外数学输入；不保存可重算的大系数数据。当前可在一般 Delta 零的 W=0 图上使用 $u(Q+2)-2\ne0$，据此解出 ell 并继续原返回。W 本身仍可能为零；一般 Delta 零、一般 LS、R150 及普通 ISP 的完成状态没有改变。
