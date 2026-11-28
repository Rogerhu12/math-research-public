# R150 附录：整 b0 的实际同 h 恢复、原 D 关系与三个权参数条件

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（UTC）。

本附录记录同 h 四乘五原输入的首次实际完整返回。四条恢复关系确有同一个非零纯权首项 h，但它仍含总次数 34 的未付支撑；原 D 的恢复分子也非零。三个新的纯权必要核全部非零，且逐一完整返回到五个原源。因此本次得到明确的恢复图与新原条件，没有排除整 b0，没有删除 h=0 的任何纤维，也没有新增纯 u 覆盖或点数界。

## 1. 原范围与必要输入

沿用[整 b0 五原二次](R150-appendix-unit211-W-b0-inverse-slope-five-original-quadrics-six-weight-conditions.md)的原物理图：当前 W、两个 singleton 值互异、$D\ne0$，只使用已经支付的原单位。权坐标为

$$
\nu=\frac{(2u-1)(k+2)}{uk+2},\qquad
d=u\nu-(2u-1),\qquad r=2u-1-\nu,
$$

$$
k=\frac{2r}{d},\qquad
Q=\frac{2(u-1)r}{d},\qquad
\ell=\frac{u\{\nu^2-(u+1)\nu+2u-1\}}r.
\tag{1}
$$

仅在本 b0 整支，既有原值论证支付 $A_*=uQ(\nu+2)$，所以

$$
\kappa=\frac{\ell}{\nu+2},\qquad T=-\kappa(3-2\lambda)
\tag{2}
$$

合法。$\nu+2$ 没有被外推为整个 W 的单位。

原子理想保持为

$$
J_5=(E_1,E_{B,e},E_{B,o},N_1,q_2)
    =(q_f,r_1,r_2,r_3,q_2),
\tag{3}
$$

其中

$$
q_f=f^2+(a\lambda+b)f+c\lambda^2+d_1\lambda+e_0,\qquad
r_i=A_i(\lambda)+B_i(\lambda)f.
$$

这里 $q_2=2a_d/\ell$，原身份为 $C_4=mD\ell q_2$。三个 $r_i$ 与 $q_2$ 对 $(\lambda,f)$ 总次数至多二，且没有 $f^2$ 项。$E_1$ 来自真 dual 乘法的独立原均值，未替换成加权 singleton 均值。整个原 $I_{11}$ 仍保留；$J_5$ 是它在当前物理图上的必要子系统，不宣称单独充分。

本次只再生 (1)–(3) 的必要定义和旧 G36 的准确坐标拉回。没有重新执行旧六个 Sylvester 投影、旧 primitive PRS、C74/C78 的 gcd，或全图 NS/PS 六核。

## 2. 实际四乘五与统一取消

以

$$
v=(1,\lambda,f,\lambda^2,\lambda f)^{\mathsf t}
$$

为单项式列。四行 $r_1,r_2,r_3,q_2$ 仅乘各自实际已付权分母 LCM，得到

$$
F=L v,\qquad L=[c_0\mid B],\quad B\in A_W^{4\times4}.
\tag{4}
$$

每条 F 同时保留相对于 (3) 左边五个原源的纯权组合。

程序计算固定 B 的十六个三阶余子式，并完整返回

$$
B\operatorname{adj}B=(\operatorname{adj}B)B=(\det B)I
\tag{5}
$$

的全部 32 个坐标。原头 $h_{\rm raw}=\det B$ 非零，双次数为 $(45,52)$、总次数 74。

将四条伴随关系复合至五原源，得到二十个实际乘子。源码只清这些乘子的共同已付分母，再对全部二十分子作一次统一共同因子取消。共同因子双次数 $(14,18)$、总次数 27、197 项，SHA256 为 d9de1529f64c81fdb19bd4da3410628a77540d0cf2d6d40630cd25fdea6c9930。

取消后四条关系重新逐原式和逐 f 系数返回；不是将原方程除以未知因子。它们为

$$
H_\lambda=h\lambda-K_\lambda,\quad
H_f=hf-K_f,\quad
H_{\lambda^2}=h\lambda^2-K_{\lambda^2},\quad
H_{\lambda f}=h\lambda f-K_{\lambda f}\ \in J_5.
\tag{6}
$$

所有 h、K 的最终分母实际都是非零有理常数。同一个 h 用于四条关系，并实际核得

$$
BH=hF,\qquad
L(h,K_\lambda,K_f,K_{\lambda^2},K_{\lambda f})^{\mathsf t}=0.
\tag{7}
$$

规范 h 分子的双次数为 $(31,34)$、总次数 47、839 项，定义 25588 字节，SHA256：

aa0a9635c0fdb5efe9650034385e78f6052becd1a97a095a546849efff2ffd3b。

按旧原单位剥支持后，余头双次数 $(22,27)$、总次数 34、521 项，定义 14810 字节，SHA256：

98ebe5e0c615c4aba59cfe7343bf7c141fd86595090cfebfc256ff5b677c1612。

实际剥除仅记录 gcd 层：u 为 3 层，u−1、d、r、ν−1、ell、P02 各 1 层；这些层数不解释为某个未展开因式的指数。源码明确返回 headIsAlreadyPaid=false，没有把这个新总次数 34 的支撑付成单位，也没有对它作新的因式分解。

四个 K 分子的实际规模如下；分母均为上述非零有理常数。

| 参数 | u 次数 | ν 次数 | 总次数 | 项数 | 定义字节 |
|---|---:|---:|---:|---:|---:|
| $K_\lambda$ | 31 | 35 | 48 | 863 | 26371 |
| $K_f$ | 33 | 35 | 49 | 914 | 28033 |
| $K_{\lambda^2}$ | 31 | 35 | 48 | 863 | 26402 |
| $K_{\lambda f}$ | 33 | 36 | 50 | 947 | 29062 |

全部参数 SHA 与定义位置保存在小执行回执；不存系数缓存。

## 3. 原 D 的实际恢复关系

(2) 使物理 D 成为同一 lambda 的二次式：

$$
D=d_2\lambda^2+d_1'\lambda+d_0.
$$

本次先完整返回五原源身份

$$
hD-C_D=d_2H_{\lambda^2}+d_1'H_\lambda,\qquad
C_D=d_2K_{\lambda^2}+d_1'K_\lambda+d_0h.
\tag{8}
$$

$C_D$ 实际非零，双次数 $(32,36)$、总次数 50、891 项，定义 27228 字节，分母是非零有理常数。分子 SHA256：

c366ffdd7d1fb73a757e6c4010231d8afc7f7c35edd871141d482f4623e27caf。

因此本次没有获得 $hD=0$，更没有获得原单位矛盾。在明确的 h 开图，$D=C_D/h$；物理 $D\ne0$ 在该图要求 $C_D\ne0$。在 h 零面，(8) 只给 $C_D=0$，仍须保留全部原五式和 $I_{11}$，不能据此删去该面。

## 4. 三个纯权必要核及完整来源

按[同 h 纸面定理](R150-appendix-unit211-W-b0-simultaneous-four-by-five-same-head-original-recovery.md)，定义

$$
\begin{aligned}
S_1&=hK_{\lambda^2}-K_\lambda^2,\\
S_2&=hK_{\lambda f}-K_\lambda K_f,\\
S_q&=K_f^2+(aK_\lambda+bh)K_f
       +cK_\lambda^2+d_1hK_\lambda+e_0h^2.
\end{aligned}
\tag{9}
$$

实际五原源分别来自

$$
\begin{aligned}
S_1&=(h\lambda+K_\lambda)H_\lambda-hH_{\lambda^2},\\
S_2&=h\lambda H_f+K_fH_\lambda-hH_{\lambda f},\\
S_q&=h^2q_f-(hf+K_f+ah\lambda+bh)H_f\\
&\quad-\{aK_f+c(h\lambda+K_\lambda)+d_1h\}H_\lambda.
\end{aligned}
\tag{10}
$$

对每条 (10)，源码只清五个实际乘子的已付分母，精除这五个乘子的共同因子，再把新组合完整乘回五个原源。最后仅剥已经支付的权支撑。记最终三核为 $C_1,C_2,C_q$；本次实际得到三个非零原条件 $C_i\in J_5$。

| 原核 | u 次数 | ν 次数 | 总次数 | 项数 | 定义字节 | 完成秒数 |
|---|---:|---:|---:|---:|---:|---:|
| $C_1$ | 50 | 62 | 78 | 2594 | 113567 | 3.432765025 |
| $C_2$ | 51 | 63 | 80 | 2714 | 118647 | 5.957190723 |
| $C_q$ | 55 | 69 | 87 | 3201 | 147489 | 10.562334598 |

三个精确定义 SHA256 依次为：

- b0359dbfa9f34ac55da98a73ebebaf750233b352c89ec88a5a6d4704ab12cd42；
- 87eb843bae8bd7a7627633ef5dd7b2604ec1ae0d005d80e18b6f439934095254；
- 31e81bc98adf893428bf9598993fe1d3e384d206ce0b90b29dc1b4bb874f9bcd。

对应实际五乘子共同因子的总次数分别是 13、11、10；这些因子不被当单位。新 C 的原组合直接成立，故共同因子零面也被覆盖。最终 paid gcd 层分别为：

- $C_1$：u 三层、u−1 一层、ν+2 一层；
- $C_2$：u 三层、u−1 一层、r 一层、ν+2 一层；
- $C_q$：u 三层、u−1 两层、r 一层、ν+2 一层。

本次不计算三个核的 gcd 或结式，也不把它们非零解释为原图为空。

## 5. 完整恢复开图与未付零面

(6)–(10) 连同 (7) 给出明确 h 局部化后的原理想身份

$$
J_5 A_W[h^{-1}][\lambda,f]
=(H_\lambda,H_f,S_1,S_2,S_q).
\tag{11}
$$

所以

$$
A_W[h^{-1}][\lambda,f]/J_5
\cong A_W[h^{-1}]/(S_1,S_2,S_q),\qquad
\lambda=K_\lambda/h,\quad f=K_f/h.
\tag{12}
$$

这是原商的双向同构，不要求原生成元自由，也不丢重数。实际 primitive 核亦可替代右端的三个 S：每个 $C_i$ 有完整原组合，且相应 $S_i$ 是 $C_i$ 乘一个权环元素；故 (11) 的同一理想也由 $H_\lambda,H_f,C_1,C_2,C_q$ 生成。这里未使用被取消共同因子的逆。

在 h=0 的整支，(6) 要求四个 K 同时为零，但这四个权条件不被宣称等价于原五式。仍保留全部 $J_5$ 和所有个别原值条件。新纯权核则因完整五源身份同样适用于这一整支。

本次首项未全支付，故 (12) 仅是明确的恢复开图。既有整 b0 有限界保持原范围；本篇不增加新的全支点数界，也不把 $J_5$ 的恢复当成 $I_{11}$ 的充分解。

## 6. 首次实际记录与再生定义

源：

[2026-11-28-unit211-W-b0-simultaneous-four-by-five-same-head-original-D-8542.py](../notes/2026-11-28-unit211-W-b0-simultaneous-four-by-five-same-head-original-D-8542.py)。

源 Git blob：1898abba431faf62aca343cc2122e48b45d0599d；21087 字节；SHA256：

313957129f4b54195253caf973ca1fdb93faaa59adb0027c1c9924c2d2faf3bd。

[首次输入说明](../notes/2026-11-28-unit211-W-b0-simultaneous-four-by-five-same-head-original-D-8542-input.md)保留未执行时的原状态；本篇记录其实际结果。自含零依赖，原预算 180 秒、4 GiB，外层 195 秒，没有改预算或重跑。

- Actions run：[46140669502](https://github.com/Rogerhu12/math-research-public/actions/runs/46140669502)。
- Job：[140965655310](https://github.com/Rogerhu12/math-research-public/actions/runs/46140669502/job/140965655310)。
- 冻结源提交：d4f22f04af0ba57d4735cca0f3e68ecc59e018d6。
- 实际 driver：10.652680686 秒、81764 KiB、源 exit 0。
- 数学最终 checkpoint：10.567500124 秒。
- stdout：8299 字节，SHA256 764f85b1acc22644914360c05abb7d5dc7ab51e1d5f4c265a6b1e4af63e69ebf。
- 32 个伴随坐标、384 次精确多项式除法乘回、29 个新五源原关系的 f 系数坐标核对、三个新纯权完整返回均完成。

实际 pull 在 2026-11-28 11:36:33.612241 UTC 从源提交到 2f352316248e46ee0c854edf310bfff20a791905；两份 README 无变。已读 root blob 为 99c5ad8d06e939e6cfbbab1afdeffa5463f15f18，课题 blob 为 5fbd905291dd044c88d35bd9c07ac0e586ff795a。

[小执行回执](../notes/2026-11-28-unit211-W-b0-simultaneous-four-by-five-same-head-original-D-8542-execution.json)保存实际 driver、七条数学 checkpoint、参数次数/字节/SHA。所有可重算系数不入库。本次没有重放旧六投影或 PRS，没有形成新的纯 u 覆盖、因式分解或排空结论。
