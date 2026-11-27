# R150 附录：$\Phi=0$ 的原值碰撞、首一 $\ell$ 二次与 8918 个基参数点覆盖

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 旧参数化与本次新增结论

范围为当前一般 unit211 LS 剩余图的 $\Phi=0$ 且 $z_n=TB_3-A_2^2=0$ 部分，仍保全部原物理单位与已付权面排除。这里 $D\ne0$，故 $z=(h-1)(k-1)=z_n/D=0$ 是 $h=1$ 或 $k=1$ 的碰撞。

[旧原 U-value atlas](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md) §2.2 已完整登记该碰撞参数化；它不是一个排除定理。旧 [S0 碰撞排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-h1-k1-value-collision-complete-exclusion.md) 只覆盖 $S=0$。本文不重登记这些旧身份，使用剩余 $S\ne0$ 的实际原输入。

本次新增：$\Phi$ 在碰撞参数化上对 $\ell$ 有已付的非零二次头；在该首一二次商内恢复同一原 $f,t$ 与完整 Gram，形成八条原线性余式，再以真实原单位 $H^3$ 作完整两行返回。得到两条总次数 $98,91$、QQ 二元 gcd 为 $1$ 的必要多项式，所以至多有 $8918$ 个不同的 $(\lambda,\rho)$ 基参数点。本结论不表示这些点均为物理解，也未把它们排空。

## 2. 全碰撞覆盖与首一二次

交换原 B/C 标签后取 $h=1$。令
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1.
$$
原矩及 $D\ne0$ 给 $A_2B_3\ne0$，并精确给出
$$
c=\gamma=\frac{A_2^3}{B_3^2},\quad
b=\ell-\gamma,\quad
k=1+\frac{B_3}{A_2},\quad T=\frac{A_2^2}{B_3},\quad
w=\lambda-1-T.
$$
令原 $\rho=(p-q)/2$，共同规范 $p+q=2$，则
$$
p=1+\rho,\quad q=1-\rho,\quad Q=1-\rho^2,\quad
u=p\ell-2\gamma\rho.
$$
原单位使 $\rho pq\ne0$。又
$$
S=\frac{4\lambda^2-5\lambda+2}{A_2}\ne0,\qquad
\zeta=\frac{B_3p}{2A_2\rho}.
$$
这些除数已由原碰撞矩、配对非退化和已闭整 $S=0$ 支支付。

代回原 $\Phi=-2u^2+6u-4+(1-\ell)Q$，得到
$$
\Phi=-2p^2\ell^2+C_1\ell+C_0,
$$
$$
C_1=8p\gamma\rho+6p-Q,\qquad
C_0=-8\gamma^2\rho^2-12\gamma\rho-4+Q.
$$
故在全部本图上可用
$$
\ell^2+\alpha\ell+\beta=0,\qquad
\alpha=-C_1/(2p^2),\quad \beta=-C_0/(2p^2). \tag{2.1}
$$
头 $-2p^2$ 是原单位；没有新增首项零支。两个 $\ell$ 根与合流根全部保留。

系数环只有 $(\lambda,\rho)$。每个乘法先形成三项原卷积，再按 (2.1) 约化至 $a+b\ell$，并逐系数核查完整原差等于商乘 (2.1)。此操作不是在两个数值根上代点。

## 3. 同一来源的清分母原 Gram

沿用原 $P_f,P_c,N_F,N_C$，其中 $P_f=T_0(J-Q)$ 已付非零。在 $\Phi=0$ 上，原 $P_1$ 与 $N(V)$ 给
$$
f=\frac{f_0}{P_f},\qquad
t=\frac{t_0}{bP_f},
$$
$$
f_0=-P_c,\qquad
t_0=-\frac{N_Ff_0+N_CP_f}{cQS\zeta}. \tag{3.1}
$$
$t_0$ 的除数全在已付的 $(\lambda,\rho)$ 基环。没有倒置二次商中的 $b$、$P_f$ 或它们的范数。

设 $H=bP_f$，为真实原单位，且
$$
W_{1P}=T_0P_f/2+2uf_0,\quad
W_{2P}=(uT_0+\lambda P_{02})P_f+(V_2+2u^2)f_0-cQt_0,
$$
$$
X_0=\frac{qW_{1P}-W_{2P}}{p(q-p)},\qquad
Y_0=\frac{W_{2P}-pW_{1P}}{cq(q-p)}.
$$
令 $a=1-\ell$，
$$
r_0=X_0-apH-ct_0,\quad
s_0=Y_0-aqP_f-t_0,\quad
A_0=2f_0-2X_0-2cY_0+2ct_0.
$$
于是 $H$ 乘原 Gram 矩阵的四行为
$$
(0,0,pH,qH),\quad(0,bA_0,r_0,bs_0),\quad
(pH,r_0,0,t_0),\quad(qH,bs_0,t_0,0). \tag{3.2}
$$
程序直接从 (3.2)、原 Frobenius 乘法和原迹形成
$$
E_1,E_B,E_C,N_1,N_B,P_B,N_C,P_C.
$$
三条均值乘 $H^2$，其余原式乘 $H^3$。它们只按单首一 (2.1) 约化为两列；清基环分母和剥因子只用已付基单位，且每一步除法均回乘。原 $P_1$ 余式与两条真实线恢复也实际核为零。

## 4. 原单位目标与所有临时主元零纤维

记某两条原余式为 $r=(r_0,r_1)$、$s=(s_0,s_1)$，目标为 (3.2) 中同一 $H$ 的三次幂
$$
H^3=t_0+t_1\ell.
$$
暂在 QQ$(\lambda,\rho)$ 中用两行行列式计算 Cramer 系数。这里只作符号场运算，不假设行列式在原点非零。约掉各系数真正公共因子后，取完整最终分母 $\delta$，并实际核回
$$
\delta H^3=A(r_0+r_1\ell)+B(s_0+s_1\ell) \pmod{(2.1)}. \tag{4.1}
$$
(4.1) 的两个系数身份完整成立。所有余分母只属于已付基环；因此它在临时行列式为零处仍有效。原点有两条原式为零、$H\ne0$，所以 $\delta=0$ 是必要条件。

同一来源的 $\ell r$ 也可用，因为它是原式乘同一个 $\ell$，不是另选根。首次实际运行对十一组固定原行对完成 (4.1)，未出现单位分母。全部必要零纤维保留。

首两组来自 $(E_1,E_B)$、$(E_1,E_C)$。只剥已付基单位后分别得到 $F,G$：

| 必要式 | $(\lambda,\rho)$ 次数 | 总次数 | 项数 | SHA256 |
|---|---|---:|---:|---|
| $F$ | $(83,15)$ | 98 | 1344 | 1b9f8c1bb31a9c87d538b40e82134b7834d03aad87774ee07463e7936dec5c48 |
| $G$ | $(77,14)$ | 91 | 1170 | 10868a19c5de665f9c4dc56a2f6e2c7196081de1e2a0fd9f74b3c1dbbc18ac23 |

实际 QQ 二元 gcd 为 $1$，故它们没有公共代数曲线。Bézout 给全部仿射公共点的不同点数至多
$$
98\cdot91=8918.
$$
这是 $(\lambda,\rho)$ 基参数点数，每个基点仍保 (2.1) 的全部 $\ell$ 根。 8918 的计数在交换标签后选定的 $h=1$ 有序图内；另一 $k=1$ 有序图由标签交换覆盖，不将两个有序图的并集不加说明地按同一 8918 计数。交换 B/C 标签保原乘法、迹、值与同一 Gram，覆盖另一 $k=1$ 碰撞。

## 5. 首次实际身份与下一未付接口

- 原源：2026-11-27-unit211-Phi-zero-rank-one-value-monic-ell-original-unit-return-8542.py。
- source SHA256：1ec9ea1cdd07d2a8a04784a6a1d5c272f384d819b61550c1932b49491fe13406。
- run 45988581954，job 140470364006，内部 exit0。
- 驱动时间 4.796086513000002 秒，最大子进程 RSS 57628 KiB。
- stdout 16810 字节，SHA256：80120bc53a8fe0e6ce13497c9c0f7b1686d8de78b8eb3f105c9f3205ed06eda8。
- 原源、真实 pull 提交均为 7a5c98b8e31f4e4596972d48c233ee6106a2dc5c；11:12:55.255663 UTC 两 README blob 无变。
- 八条原行在 1.541598 秒前全部完成；十一条原单位返回最终 4.731649 秒。共有 629 次二维乘法、1887 个完整原差系数身份。

这一有限覆盖仍需原点返回；没有把二元 gcd 为 $1$ 误称为无孤立点，也未从某一范数非零假设删去另一 $\ell$ 根。
