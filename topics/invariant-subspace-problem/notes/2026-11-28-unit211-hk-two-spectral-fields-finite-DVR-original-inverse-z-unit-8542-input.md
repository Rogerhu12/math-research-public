# 首次输入：两个完整碰撞谱域的有限 DVR 倒 z 原单位返回

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**状态：新源已冻结，尚未执行。** 本文不给任何新排空结果。每个谱域只在预先固定顺序下选择第一个合格的整模型点，然后进行一次原单位目标；目标失败后不换素数或剩余点。

## 1. 本次准确范围与已成前提

范围是当前正确的 $h=k,\Delta=0$、$P_f\ne0$ 原坐标图。这里物理值碰撞的 $D=0$，**从不借用 W 分支的 $D\ne0$ 或反演 $D$**。

两篇已刊完整证明为：

- [约化谱基与唯一 u](../results/R150-appendix-unit211-hk-Delta-zero-reduced-base-and-4788-coordinate-Artin-envelope.md)；
- [原 P 判别式及同 Q 唯一约化](../results/R150-appendix-unit211-hk-independent-P-discriminant-unique-reduced-Q-and-2394-Artin-envelope.md)。

它们在完整不可约域

$$
K_d=\mathbb Q[\lambda]/(F_d),\qquad d=99,300
$$

中，给出 $u=\eta_d\in K_d$；在原物理权局部化保留的每个分量中，又有 $Q=\theta_d\in K_d$。所有其它原权局部化只会删除完整域分量。

这是本次使用的真实特征零前提，并非从一个模点猜测 $u,Q$ 唯一。两个 $F_d$ 的既成不可约性、在原固定十七阶结式中重数一、独立 P 判别式，以及原四阶 Q 结式的一阶赋值，都不重跑。

原准确参数：

| 参数 | 准确定义 SHA256 |
|---|---|
| P，双次数 28/3 | 8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c |
| Mtrue，双次数 110/14 | 65d420e901bd60b711d76ad23699daab655414b0595383a19a93d13180f30663 |
| F99，100 个升序系数定义 | e422b38e5f712eb9237d85ad116dfcdf8ec94f3886a7d97d210b48e3ce6a5a7e |
| F300，301 个升序系数定义 | 5bfbc9ddc3b558dbef77fc19cd495175a1c8ad16461e6166c44cb982a1dca7ea |

本次只再生这些必要输入的定义并核 SHA，不重新运行旧 QQ 整域 $u$ gcd、同 Q gcd、旧八 z 门、旧固定十七阶 Bareiss 或 722 基点证明。

## 2. 一个剩余点为何可以代表整个 QQ 不可约谱域

先固定 $d$。将 $F_d$ 首一化，并选素数 $p$ 使其全部有理系数的分母为 p 单位。要求 $\bar a\in\mathbb F_p$ 是 $\overline F_d$ 的简单根，且另一个谱因子不在该点消失。令

$$
\mathcal O=
\left(\mathbb Z_{(p)}[\lambda]/(F_d)\right)_{(p,\lambda-\bar a)}.
\tag{1}
$$

由于 $F_d$ 在 QQ 不可约，该整环的分式域为 $K_d$；简单根条件使 (1) 成为未分歧 DVR，剩余域为 $\mathbb F_p$。无需假定 $F_d\bmod p$ 整体不可约、平方自由或只有一个根。

本次同时检查 P、Mtrue 及所用原有理权式分子/分母的所有有理常数系数均 p 整。若原 P 的 $u^3$ 系数在 $\bar a$ 非零，则它在 $\mathcal O$ 中为单位。已知 $\eta_d\in K_d$ 满足 P；将 P 首一化，得 $\eta_d$ 在 $\mathcal O$ 上整。DVR 整闭，故

$$
\eta_d\in\mathcal O.
\tag{2}
$$

模 p 的 P/Mtrue **完整**一元 Bézout 若给恰一次 gcd $u-\bar u$，就准确识别 $\eta_d\bmod\mathfrak m=\bar u$。这不是从若干候选 u 中任选一个；每一允许系数降次均保留，特别不要求 Mtrue 的 u 首项非零。

原 $\Delta$ 对 Q 的二次头是

$$
d_2(\lambda)
=-\frac{2(B^2-A^3)(\lambda^2+\lambda-1)}{B^2}.
\tag{3}
$$

若它在 $(\bar a,\bar u)$ 非零，$\theta_d\in K_d$ 满足首一化的 $\Delta$，同样给

$$
\theta_d\in\mathcal O.
\tag{4}
$$

模下对完整原 $\Delta,T_{\rm num}$ 分子取 Q Bézout，要求其 gcd 恰为 $Q-\bar Q$，从而准确识别 $\theta_d$ 的剩余值。不反演 $T_{\rm num}$ 的 Q 首项；原式若降次仍全保。分子的原 Q 无关分母同时检查为非零。

接着在这个准确点检查原 $A,B,\lambda,2\lambda-1,u,u-1,Q,1-Q,P_f,bc,P_{02},S,M$ 的全部实际分子/分母非零。故这些量都是 $\mathcal O$ 中真单位。本次不是把模非零升级为某个未识别代数分支的 QQ 结论；(2)、(4) 已将所有表达式固定在同一个完整域及其 DVR 内。

若某个谱域在原物理局部化中已被删除，它没有待处理的原点。若仍保留，上述整性论证适用。没有选到合格点时，源仅保留整个谱域，不声称它被删除。

## 3. 选点规则必须先于原 z 目标

冻结素数顺序是

$$
1009,1013,1019,1021,1031,1033,1039,1049,
1051,1061,1063,1069,1087,1091,1093,1097.
$$

每个 p 内按整数 $0,1,\ldots,p-1$ 枚举 $\bar a$。选择条件只包括：

1. 全部上述有理常数系数 p 整、目标谱简单根、另一谱非零；
2. P 的三次首项非零，完整模 u gcd 恰一次；
3. 原 Delta 二次头非零，完整模 Q gcd 恰一次；
4. 已列原权单位及下一节的 Loww 常数非零。

**选择函数不构造、不测试任何原 z 理想、秩、gcd 或正目标。** 固定第一个合格点后才构造八个原 z 方程；若其新目标没有返回一，则保留该完整谱域。源绝不按目标结果再试另一个点或素数。F99 与 F300 是两个不同的特征零整域，各自可以有一个这样的固定第一合格点。

## 4. 同一点的八个原 z 方程

所有恢复使用真正双数乘法

$$
(vw)_0=v_0w_0,\qquad
(vw)_1=v_0w_1+v_1w_0,
$$

而不是错误的分量平方。原坐标为

$$
\begin{aligned}
&A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,\\
&\ell=A^3/B^2,\quad T=A^2/B,\quad
w=\lambda-1-T,\quad h=k=1+\xi,\\
&f=-\frac{P_c+bc\Phi z}{P_f},\quad
V=\frac{Jf-G+bcz}{Q},\quad t=z/Q,\quad
W_1=T_0/2+2uf,\\
&x=\frac{(u-\ell Q)V-(u-\ell)W_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\\
&A_1=2f-2V+2bc\,t .
\end{aligned}
\tag{5}
$$

再添 $\rho^2=1-Q$，使用

$$
b=\ell/2+\frac{u-\ell}{2(1-Q)}\rho,\quad c=\bar b,\quad
p=1+\rho,\quad q=1-\rho,\quad X=x+\rho y,\quad Y=\bar X.
$$

令 $a=1-\ell$、$r=X-ap-ct$、$s=Y-aq-bt$。四原行是

$$
(0,0,p,q),\quad(0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0).
\tag{6}
$$

代码逐项用完整原 $\tau$、DK、N4、P2 重建，返回 E0/N0/P1 的准确恢复以及完整 $N_4(V)=0$。八个原同 z 条件固定为

$$
E_1,\ E_{B,e},\ E_{B,o},\ N_1,\ N_{B,e},\ N_{B,o},\ P_{B,e},\ P_{B,o}.
\tag{7}
$$

其 z 次数上界依次为 $2,2,2,2,3,3,3,3$。这是原双数、极化和三次式的结构次数界，反转容量按这个固定列表选取，不因模后最高系数恰好消失而缩减。

因 $1-Q$ 为单位，$\rho$ 为单位；原 B/C 两行及其共轭使 (7) 的偶、奇部分均为真实必要式。未选定某一个 rho 符号，也没有反演一个 rho 范数的新因子。

(5)–(7) 的所有系数在 $\mathcal O$ 中：显式除法只用第2节已检查的原单位及 $2,4$。不需要计算 $\eta_d,\theta_d$ 在 QQ 谱基下的大系数。

## 5. 首一倒 z 三次及完整原来源

引用[完整原 Loww 纤维](../results/R150-appendix-unit211-h-equals-k-Delta-zero-complete-Loww-fibers-8664-cover.md)。令 $m=u-\ell$、$\delta=1-Q$，有

$$
\begin{aligned}
E_{W,2}={}&(2u-u\ell-V)E_{B,e}\\
&+[2(u-\ell Q)-um-mx-\ell\delta y]E_{B,o},\\
N_S={}&\ell N_{B,e}+mN_{B,o},\qquad
P_S=\ell P_{B,e}+mP_{B,o},\\
L_w={}&N_S-P_S+E_{W,2}\\
={}&2P_{02}(2\lambda-1)w
-bc\,t\,[K_w+4(f-u)(t-2)],
\end{aligned}
\tag{8}
$$

$$
K_w=2[t^2+(5u-4x-2)t+2(x^2-\delta y^2)
 +4x+4\delta y-4ux+2u^2-6u+Q].
$$

源在固定剩余点完整返回 (8)，保自由 f 修正。它是已刊的完整原恒等式，故同一 $\mathcal O$ 中也成立，而不只是一次数值偶合。写

$$
L_w(z)=c_0+c_1z+c_2z^2+c_3z^3,\qquad
c_0=-2P_{02}\lambda^2(2\lambda-1)^2/B\in\mathcal O^\times .
\tag{9}
$$

取 $\zeta=1/z$，定义

$$
q_\zeta=\zeta^3+(c_1/c_0)\zeta^2+(c_2/c_0)\zeta+c_3/c_0.
\tag{10}
$$

它始终首一三次，包含 $c_3=0$ 的全部下降支；本次不反演 $c_3$。于是

$$
C=\mathcal O[\zeta]/(q_\zeta)
\tag{11}
$$

在 $\mathcal O$ 上自由秩三，尚未加入八原式。把 (7) 的每个 $F_i(z)$ 以固定容量 $d_i$ 反转成

$$
\widetilde F_i(\zeta)=\zeta^{d_i}F_i(1/\zeta)\in\mathcal O[\zeta],
\qquad
d_i=(2,2,2,2,3,3,3,3).
\tag{12}
$$

所有下降首项和潜在的 $\zeta=0$ 分量完整保留；本次没有先在模下饱和它们。

## 6. 唯一可接受的目标及特征零提升

在固定剩余域中，源用普通多项式欧氏 Bézout，累积九个原来源：

$$
a_0\overline q_\zeta+\sum_{i=1}^8a_i\overline{\widetilde F_i}=g .
\tag{13}
$$

每次除法的商积和每次完整来源返回均核相等。若准确 $g=1$，再将最后九个乘子全乘回一次。只输出小次数、字节数、SHA 和选定点，不保存证书系数。

令 $J=(\widetilde F_1,\ldots,\widetilde F_8)\subset C$。由 (11)，$C/J$ 是有限 $\mathcal O$ 模。实际 (13) 若给一，就有

$$
(C/J)/\mathfrak m(C/J)=0.
$$

Nakayama 引理给 $C/J=0$；张量到其分式域 $K_d$ 后，完整同一点倒 z 原理想仍为单位。因此整个 QQ 不可约谱域、包括它的所有复嵌入都被排除。

这不是“有限域没有点，所以特征零没有点”。有限整模型、已知完整域、u/Q 整性、系数单位及有限模是提升的前提；本次每个前提都有已刊来源或显式实际检查。

因为 (8)、(9) 给 $L_w\in(F_1,\ldots,F_8)$ 且常数 $c_0$ 可逆，原 z 商中 z 已为单位：

$$
z\left[-(c_1+c_2z+c_3z^2)/c_0\right]=1.
$$

故倒 z 单位返回同时排除当前原 z 图；不用从一个正 z 幂或 D 幂的模下返回猜测 QQ 排空。源实际只试目标一。若最终 gcd 正次或未找到整模型，整个相应谱域继续保留。

## 7. 唯一首次源、依赖与预算

新源 blob：eb63f13d8b7e2d9d6752ea19f52b81daae6b2648。

SHA256：c3d60e3048e197a7ebe908f0d4e6c1b6f2bcd435dd0718cec3d3ae41d280523a。

字节数：20013。

建议 basename：

**2026-11-28-unit211-hk-two-spectral-fields-finite-DVR-original-inverse-z-unit-8542.py**

对应输入：

**2026-11-28-unit211-hk-two-spectral-fields-finite-DVR-original-inverse-z-unit-8542-input.md**

总预算180秒、4 GiB，外195秒。所有嵌套 alarm/setitimer 都钳在同一个外层绝对截止；依赖中的4 GiB硬界相同，不暗降资源。

必须同目录固定复制三个已刊源码：

1. 2026-11-28-unit211-h-equals-k-corrected-Delta-zero-F99-original-fibers-8542.py，
   SHA daa2c5331f45b5583c657cbfe407660552763b65a42abda7fa379ae6b92fa005；
2. 2026-11-28-unit211-h-equals-k-corrected-Delta-zero-RWO-Q-projection-8542.py，
   SHA 3fcc2e90677b7bbd0247d72c1922fc6ed0b60da4ced715a7cecbeae656aade33；
3. 2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py，
   SHA 2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2。

第1件仅截到 `unit,fac=rp.factor()` 后、`choices=[...]` 前，准确4728字节，
SHA f3de7830b2ff98c6f4e7df0a891eb7fe2bff61c8ccf6ba6ae83134316ae82f59。
其内第2件只取6055字节定义前缀，第3件只取5121字节正确原 R/W/O 前缀。源码中每层全文件和前缀SHA均核。后续旧 proof/gcd/Gram 驱动不会执行。

原 P 历史只由 Actions 终端从固定 commit
ac40c96b0cfb3758fbf8bd380d18ca288a23601f 的

topics/invariant-subspace-problem/notes/2026-11-27-unit211-equal-singleton-Delta-zero-two-QQ-curves-848-base-cover-receipt-8542.json

临时读取为 **isp-hk-independent-Delta-Tnum-legacy.json**。只选择第1节准确 P SHA 并在 runner 内解码，绝不经工具传载荷或另存 main；同一历史中的错误第二曲线不读取。

参数前缀中的直接 FLINT resultant/QQ factor 只定义已刊 F99/F300，随后严格核已刊两SHA。没有把这一步当新的覆盖结论，也没有进入冻结 ad00 的 QQ 整域 u-gcd。新的数学目标仅是第3–6节两个 finite-DVR 原单位返回。

## 8. 执行后必须保留的范围

若只有一个域返回一，只能排该完整域；另一个整域全部保留。若两者均完整返回一，可合已刊小谱域排除及基分解关闭当前 $h=k,\Delta=0$ 的命名原图，但仍须另保不在该图的条件及 $\Delta\ne0$。

本输入不宣普通 Hilbert ISP 完成，不给新增未知矩阵轨道计数，也不预记源成功。既有 ad00 超时及所有已成/撤回原来源的历史状态不改变。
