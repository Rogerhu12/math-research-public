# Phi=0 的 H1 曲线上：新三头的整个零集排除

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完成结论与准确范围

本文继续
[R150-appendix-unit211-Phi-zero-H1-polynomial-v-source-and-fixed-original-norm-interface.md](R150-appendix-unit211-Phi-zero-H1-polynomial-v-source-and-fixed-original-norm-interface.md)
的同一个原值图。范围仍是已付原权单位及物理 $D\ne0$ 的 $\Phi=0$ 图，并进一步限制在原第一头曲线
$$
g(u,Q)=-12H_{6,4}(u,Q)=0.
$$
不将此图移到 $D=0$ 的碰撞分支。

沿用该文的四条清分母、仅剥原已付权单位的多项式
$$
\widetilde R,\quad\widetilde W,\quad\widetilde O,\quad\widetilde N_1
$$
及真实值坐标
$$
v=Jf-G+bc\,z,\qquad z=Qt,\qquad f=-P_c/P_f.
$$
记四条式在 $(T^2,Tv,v^2)$ 上的行系数为 $H_R,H_W,H_O,H_N$，并定义
$$
h=\det
\begin{pmatrix}H_R\\ H_W\\ H_N\end{pmatrix}.
$$

**本次证明：这个原图中不存在满足 $h=0$ 的完整原解。**
因此，当前 H1 剩余原解可合法使用 $(\widetilde R,\widetilde W,\widetilde N_1)$ 的这一头图。

结论不是说 $h$ 在整个权曲线的坐标环中为单位。它的权零点确实存在；本稿用原值方程排除它们。也没有计算新的 P201 投影，已证不同权对上界仍为 804。H1 的全部原解尚未因此排空。

## 2. 固定原权模型与头因子的完整乘回

为明确所有定义，原首一 Q 四次为
$$
g=g_0+g_1Q+g_2Q^2+g_3Q^3+Q^4,
$$
其中
$$
\begin{aligned}
g_0={}&64-272u+512u^2-544u^3+336u^4-112u^5+16u^6,\\
g_1={}&-112+348u-496u^2+440u^3-248u^4+80u^5-12u^6,\\
g_2={}&60-123u+104u^2-52u^3+13u^4,\\
g_3={}&-13+\tfrac{53}{4}u-3u^2.
\end{aligned}
$$
运算始终在完整的
$$
\mathbb Q[u,Q]/(g)
$$
中进行，使用 $1,Q,Q^2,Q^3$ 四个坐标；没有先选择某个 Q 根。

令
$$
\ell_n=Q-2(u-1)(u-2),\qquad
T_0=-Q-4(u-1).
$$
源只从原四式构造前缀取得新 $h$，不执行旧 cofactor、结果式或 Dixon 消元尾段。实际完整四坐标乘回给出
$$
h=(u-1)^5Q^3T_0^2\ell_n\,h_*.
$$
这里每个被移除的因子都是当前图上已经支付的原权单位。余项 $h_*$ 的 Q 次数为 3，四坐标 u 次数至多 11；规范系数身份为 546 字节，SHA256：
19ed54730b0ad5ed9ac67759444e2b9bf1d0795d21d1a41597e337af821f635f。

取乘 $h_*$ 在完整四维 Q 代数中的正则矩阵，得到真正 QQ[u] 多项式
$$
N_h(u)=\operatorname{Norm}_{g}(h_*).
$$
实际次数为 41，系数身份为 1464 字节，SHA256：
a2c1ac2a797e23e42ccf24748daee12fc1c67f869b98b7cbd8c6fde5a91a994d。

完整 QQ 因式分解及乘积返回为
$$
N_h=c\,u^{10}(u-1)^7
(u-\tfrac32)^3(u-\tfrac{12}{5})(u-\tfrac52)
F_9(u)\widehat F_{10}(u),\qquad c\in\mathbb Q^\times.
$$
$F_9$ 和 $\widehat F_{10}$ 均取首一，分别是该完整因式分解中的唯一九次、十次因子。它们的规范身份为：

| 因子 | 系数字节数 | SHA256 |
|---|---:|---|
| $F_9$ | 138 | 30a60a6e2188e060f610ae64e0df7543dec5cce437c7c355d5987bf5a8fb7e39 |
| $\widehat F_{10}$ | 155 | b4cdf1e081ad24397f36f78eafbe55023c2cf77d4aca6e6266560d648157e336 |

这也是 $F_9$ 的精确可再生定义：原四式决定 $h$，上述完整多项式除法决定 $h_*$，固定四维正则行列式决定 $N_h$，QQ 唯一九次首一因子决定 $F_9$。不以模因式猜测定义它。

若 $g(u_0,Q_0)=h_*(u_0,Q_0)=0$，则在该点求值是正则乘法矩阵的非零左零向量，故 $N_h(u_0)=0$。原 g 首一，包含 Q 首项退化或重根的潜在疑虑均不产生遗漏。范数只用来给 u 的完整必要覆盖；没有倒置范数，也没有把某个范数零因子的全部 Q 分量当作实际头零分量。

$u=0,1$ 由原单位排除，另外三条整 u 纤维已经由
[R150-appendix-unit211-Phi-zero-H1-three-linear-poles-complete-exclusion-and-1012-cover.md](R150-appendix-unit211-Phi-zero-H1-three-linear-poles-complete-exclusion-and-1012-cover.md)
完整排除。本次仅按准确因子身份引用，不重复执行它们。

## 3. 九次分量：先取实际头零 Q 纤维

在
$$
K_9=\mathbb Q[u]/(F_9)
$$
中，源对原 $g$ 与实际 $h_*$ 计算完整 $K_9[Q]$ gcd，并将 Bézout 与每步除法乘回。得到首一一次式
$$
q_9(u,Q)=\gcd_{K_9[Q]}(g,h_*),\qquad \deg_Qq_9=1.
$$
随后逐项与全部原已付权单位分子作 QQ gcd。实际没有移除新的 Q 因子；留下的恰是这一条实际头零 Q 纤维。

这里不是把整个 $F_9(u)=0$ 上的四个 Q 根一并排空。结论仅作用于同时满足 $h=0$ 的那个线性 Q 分量。

取 $\mathcal O=\mathbb Z_{(1009)}$。源首先核对首一 $F_9,q_9$ 的系数在此处整，并在完整九维约化代数上验证所有所需原权单位。相应
$$
A_{\mathcal O}=\mathcal O[u,Q]/(F_9,q_9)
$$
是秩 9 的有限自由代数。

原 $(R,O,N_1)$ 三头在整个模代数中为单位：其完整正则矩阵逆均乘回，而非逐残域猜测。因此三头在 $A_{\mathcal O}$ 中也为真单位。原四式的真实规则可在这个固定整模型中建立，完整约化正是源中使用的规则。

选 $(R,O,N_1)$ 给出 $T^2,Tz,z^2$ 的三条首一规则。源对它们与原式的线性组合逐系数乘回，并对六个真实 T、z 乘法列乘回。剩余原 W、其两个乘法列及两个真实交换子列都在同一点消失，不需要假设三生成元商是自由模。

这些列的 $\lambda$ 次数上界分别为
$$
(2,1,1),\qquad (3,2,2).
$$
故相应固定三列 cofactor 的真实 QQ 次数至多为 6。源在共同原点条件之外，先选到一个六次首项在完整九维模代数中为单位的原 cofactor $F$；这支付同一个整模型中的真正首一六次式 $\widehat F$，不是把模次数观测直接当作 QQ 次数。

于是
$$
B_{\mathcal O}=A_{\mathcal O}[\lambda]/(\widehat F)
$$
为秩 54 的有限自由代数。另一个真实原 cofactor H 来自
$$
(\text{剩余 W},\ T\text{乘剩余 W},\ \text{真实交换子 T 列}).
$$
其全部 54 个权及 $\lambda$ 基倍数在模 1009 下形成满秩方阵；完整方阵乘模逆等于单位阵。方阵身份为 11508 字节，SHA256：
518e05f334886d19cd2a89a7474f9f42a1d561b1cc7ea97aad10fe77e0e815d7。

因为这是固定有限自由整模型中的乘 H 矩阵，行列式模 1009 非零说明它在 $\mathcal O$ 中为单位。因此 H 在 $B_{\mathcal O}$ 中可逆，特征零也没有同时满足 $F=H=0$ 的点。整个实际 $F_9$ 头零分量由原方程排除。

整个推理保留所有复嵌入及模模型的全部重数；不要求模 $F_9$ 不可约。素数是在原理想秩测试之前按系数及头的整性选择。1009 首次即合格，实际原理想测试后未更换素数。

## 4. 十次分量准确落在已经排空的共同十权

源在 $K_{10}=\mathbb Q[u]/(\widehat F_{10})$ 中已经完整返回
$$
\deg_Q\gcd(g,h_*)=1,
$$
并逐项核回 Bézout、短除法与原单位检查。

源的通用有限自由六次模型随后没有找到合格三头，在自己的执行回执中准确保留了这个分量。不能把该尝试解释成排空。这里接入已经完成的原定理，不重新运行十权的 60 维原值门。

原分类
[R150-appendix-unit211-Phi-zero-four-original-quadratic-heads-complete-ten-weight-locus.md](R150-appendix-unit211-Phi-zero-four-original-quadratic-heads-complete-ten-weight-locus.md)
明给
$$
\begin{aligned}
F_{10}^{\rm old}(u)={}&23152u^{10}-293804u^9+1660962u^8-5509191u^7\\
&+11867209u^6-17333916u^5+17377608u^4\\
&-11812736u^3+5228032u^2-1373184u+165888
\end{aligned}
$$
及唯一坐标 $Q=-a_9(u)$。将上述已刊整数多项式除以 23152，按新源相同的有理系数字符串数组规范化，得到的 155 字节 SHA256 正是
b4cdf1e081ad24397f36f78eafbe55023c2cf77d4aca6e6266560d648157e336。
所以
$$
\widehat F_{10}=F_{10}^{\rm old}/23152.
$$

还需核对 Q 分量，而不能只凭 u 因子相同就套用旧排除。旧分类在整个十次域中已经证明：$Q=-a_9(u)$ 时，四个原二次头都为零，即四行二次系数矩阵的秩至多为 2。

本稿的变换
$$
(T,z)\longmapsto(T,v),\qquad v=Jf-G+bc\,z
$$
对固定 $(u,Q,\lambda)$ 是可逆仿射变换。因为 $f=-P_c/P_f$ 对 T 是仿射函数，该变换的线性行列式恰为原已付的 $bc\ne0$。它在二次齐次系数上的作用是可逆的对称平方变换。四条清分母及 primitive 处理也只乘除原已付非零权因子。因此四行二次头秩保持；旧 $Q=-a_9(u)$ 必使新的 $h$ 为零。

旧 Q 坐标也满足 $g=0$。另一方面，本次已经精确证明 $g,h_*$ 在同一个十次域中的首一 Q gcd 为一次。因此其唯一根必为旧 $-a_9(u)$。这付清了整个新十次分量与旧十权的同一性，无需再计算四头或再求一次 gcd。

最后
[R150-appendix-unit211-Phi-zero-ten-common-head-weights-complete-original-value-exclusion.md](R150-appendix-unit211-Phi-zero-ten-common-head-weights-complete-original-value-exclusion.md)
已在全部十次域中，分别排除同两线行列式为零及非零的原值分支。故本稿保留的整个十次实际头零分量全部排除。

以上是从已成 QQ 一次 gcd 和已刊完整原定理作出的证明。原执行回执中的 “十次分量保留” 状态不作追改；新结论明确来自这一步数学合成。

## 5. 执行身份及后续可用接口

唯一新执行源：
[2026-11-28-unit211-Phi-zero-H1-original-three-head-paid-factor-and-zero-fibers-8542.py](../notes/2026-11-28-unit211-Phi-zero-H1-original-three-head-paid-factor-and-zero-fibers-8542.py)。

- 源 blob：e3cfca005d09d72437d4606b7547486de49bc10f。
- 源 SHA256：41f0ff6e5148fc51f29421bdf56147bffc66cfa5b4826622ddd72685b26ec1bc。
- 实际 run/job：46072049677 / 140751072347。
- source commit：28da8d75274a75b00e32cb50d86876c458442a19。
- 内层：0.487842716 秒 / 41996 KiB / exit 0。
- stdout：10516 字节，SHA256 8853ff1d8a153ea96bbe0a6c9bc3e88329433e0907800d4b8ef5d0400d4e6277。
- 实际 pull：2026-11-27 21:42:56 UTC，至 d3dff96c273a42c69e95bb036f11bb045517b68e；两份 README blob 均未变化。

数学阶段中，原头因子乘回在约 0.235 秒完成，完整 norm 因式分解在约 0.237 秒完成，九次原纤维排除在约 0.329 秒完成。十次纤维的实际 QQ 一次 gcd 在约 0.354 秒完成，其后五个预定素数未给通用模型，源准确保留它。全文没有依赖外层 workflow 的绿色状态替代数学返回。

头零全部关闭后，可在当前 H1 完整原解上使用 $h^{-1}$ 的三生成元规则，继续同一点的原值约束。原固定结果式的无穷远次数仍须另外支付；未据模 gcd 缩小 P201 或 804 上界。普通不变子空间问题尚未完成。
