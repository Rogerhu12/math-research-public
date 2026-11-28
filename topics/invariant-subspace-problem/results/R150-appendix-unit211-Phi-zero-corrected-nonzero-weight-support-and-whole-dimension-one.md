# 正确 Phi 全原图的非零纯权关系及完整规范维数至多一

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。
作者：literature_deddens；AI-assisted GPT-6 Astra Pro。

**状态：已证明，唯一首次实际返回成功。** 在当前正确 $\Phi=0$、物理 $D_{\rm phys}\ne0$ 的固定规范原图上，存在由两个真实六次定义的非零整数多项式
$$
F(u,Q)\in\mathbb Z[u,Q]\setminus\{0\},\qquad
\deg_{u,Q}F\le444,
\tag{1}
$$
它属于完整正确六式理想的已付系数局部化。全部原点满足 $F=0$。结合已成精确三生成呈示和两个首项的共同零权点至多 $434$，得到
$$
\boxed{\quad
\dim_{\mathbb C}\{\text{当前完整固定规范原点}\}\le1 .
\quad}
\tag{2}
$$
这里包括所有共同头零权纤维；没有把它们删去，也没有声称原图有限或为空。该结论从纠错后的真实原式重新推出，不恢复已撤回的旧紧凑式链。

## 1. 已成正确来源与系数环

沿[正确整个原 $I_6$ 的十五列三坐标呈示](R150-appendix-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-and-two-sextics.md)，设
$$
s=u-1,\quad\delta=1-Q,\quad K=Q+4s,\quad
L=Q-2s(u-2),\quad \ell=L/Q,
$$
$$
M_n=2uL-L^2-u^2Q,\quad
A=4s^2-Q,\quad B=-Q^2+(12u^2-20u+8)Q-16s^2.
$$
先在纯权环
$$
\mathcal A=\mathbb C[u,Q,(uQ\delta sKLM_nAB)^{-1}]
\tag{3}
$$
工作。这里 $A,B$ 由两个整个正确原零支的排除支付；$u$ 的完整范围来自独立的原零基点 mean 排除，已在[两头共同权支持定理](R150-appendix-unit211-Phi-zero-corrected-two-sextic-heads-434-common-weights.md) 第3节说明。其余因子是既有原权、$P_{02}$、$bc$、$P_f$ 单位。没有在 (3) 中倒置任何新六次首项或物理 $D$ 范数。

完整正确六式的代数
$$
\mathcal B=\mathcal A[\lambda,T,z]/I_6
\tag{4}
$$
在 $\mathcal A[\lambda]$ 上由 $1,T,z$ 生成，并有精确的十五列原关系呈示。它不需要是自由模。已有两条完整原组合
$$
C_{\rm NP},C_{\rm ov}\in I_6,\qquad
\deg_\lambda C_{\rm NP}=\deg_\lambda C_{\rm ov}=6.
\tag{5}
$$

| 原条件 | $(\deg_u,\deg_Q,\deg_\lambda)$ | 总次数 | 项数 |
|---|---:|---:|---:|
| $C_{\rm NP}$ | $(42,22,6)$ | $47$ | $3721$ |
| $C_{\rm ov}$ | $(30,15,6)$ | $33$ | $1824$ |

两个准确原多项式的 SHA256 为

    fcf79be98410a2eea2ebdb588b441b8f4aceb20acb4704a96ee34fc0012d01d5
    2407107501f1790a288ecabd75f14f92c7602859bfc033727b76312675f91014

本次只再生它们的必要参数定义，不执行旧动作、overlap、十五列商同构、末 cofactor 原来源或头 gcd 证明门。

## 2. 固定十二阶矩阵给全图原关系

分别乘以非零有理常数，把 (5) 整数化并除整数公内容，得到
$$
\widehat C_i=c_iC_i\in\mathbb Z[u,Q,\lambda],
\qquad c_i\in\mathbb Q^\times .
\tag{6}
$$
实际返回了全部 $5545$ 个原系数的常数尺度身份。没有剥除任何 $\lambda$ 因子或未付权因子。两个整数模型的参数 SHA256 为

    d172174636dda727467a93a1d6da37da03866ca55855b07a8fbc9802773a5542
    9c05da084849cf0885d038b5d0ce9a878faf84d619964cccb47f19c06ed3f6da

定义固定 $12\times12$ 矩阵 $\mathcal S$：前六行为
$\lambda^r\widehat C_{\rm NP}$，后六行为
$\lambda^r\widehat C_{\rm ov}$，其中 $0\le r<6$；列按
$1,\lambda,\ldots,\lambda^{11}$ 排列。取
$$
F(u,Q)=\det\mathcal S(u,Q).
\tag{7}
$$
(7) 是完整精确参数定义，不以一个模行列式代替 QQ 对象，也不要求展开大的系数载荷。

令 $v_\lambda=(1,\lambda,\ldots,\lambda^{11})^t$。恒等式
$$
e_0^t\operatorname{adj}(\mathcal S)\mathcal S
=F e_0^t
$$
右乘 $v_\lambda$，直接给
$$
F\in(\widehat C_{\rm NP},\widehat C_{\rm ov})
\subset I_6 .
\tag{8}
$$
这是已付系数环上的原多项式身份。它在任何一个、甚至两个 $\lambda^6$ 首项为零时仍成立，保留全部降次纤维；没有通过局部首项倒数推回全图，也没有把三生成模当作自由代数。

## 3. 严格总次数上界

$\widehat C_{\rm NP}$ 的 $\lambda^j$ 系数纯权总次数至多 $47-j$；另一条至多 $33-j$。对矩阵第 $r$ 个平移行，分别赋权 $47+r$ 或 $33+r$；第 $j$ 列赋权 $-j$。实际逐项返回全部 $84$ 个非零条目的次数上界。因此
$$
\begin{aligned}
\deg_{u,Q}F
&\le\sum_{r=0}^5(47+r)+\sum_{r=0}^5(33+r)
-\sum_{j=0}^{11}j\\
&=444.
\end{aligned}
\tag{9}
$$
(9) 只给真实上界，不声称精确 QQ 次数，更不假定最高项没有取消。

## 4. 预定首点的完整返回支付非零性

素数和候选点表事前固定为 $p=1009$ 以及
$$
(2,2),(3,2),(4,2),(5,2),(6,2),(2,3),(3,3),(4,3).
$$
只按输入单位及两个固定顶头选点，未先测试 gcd 或行列式。首点 $(u,Q)=(2,2)$ 即合格：
原 paid 乘积为 $286$，两个整数模型的 $\lambda^6$ 头分别为 $373,417$，均模 $1009$ 非零。

在该唯一选点，实际两多项式按低次到高次的系数为
$$
\begin{aligned}
\bar C_{\rm NP}&=(540,334,205,195,349,462,373),\\
\bar C_{\rm ov}&=(814,629,872,28,726,610,417).
\end{aligned}
$$
完整模 Euclid 返回首一 gcd $1$；两个 Bézout 乘子分别为
$$
(668,885,287,254,865,354),\qquad
(163,390,555,980,166,206).
$$
所有七次除法的乘积及最终多项式身份均返回。同时，同一个固定十二阶矩阵的实际行变换完整返回全部 $144$ 坐标，十二个主元均非零，并给
$$
\det\mathcal S(2,2)=256\pmod {1009}.
\tag{10}
$$
由于 $\mathcal S$ 是整数矩阵多项式，(10) 严格推出 $F\ne0$。这只证明定义 (7) 的原多项式非零；没有从模单点满秩推任何完整复权纤维为空。选点后没有换点、换素数或扩大候选表。

式 (8)–(10) 证明 (1) 及其全图必要性。

## 5. 包括全部 $434$ 特殊权纤维的维数论证

记 $h_{\rm NP},h_{\rm ov}$ 为 (5) 的真实六次头。已成完整 QQ 因式与 gcd 给，在 (3) 的权开集中，它们共同为零的集合为
$$
E=\{H_{31}=H_{14}=0\},\qquad \#E\le434,
\tag{11}
$$
且不存在共同复曲线分量。此处只引用已成原支持定理，不重做头门。

在 $E$ 外，至少一个头非零。在相应头开图上，(5) 给一条首一 $\lambda^6$；结合 (4) 的三生成性，尚未作几何 $D$ 局部化的必要代数由
$$
\lambda^j(1,T,z),\qquad 0\le j<6
\tag{12}
$$
作为纯权模生成。故该代数有限于相应纯权环。又由 (8)，它的权支持包含在非零平面多项式 $F$ 的零集中，后者维数至多一。因此 $E$ 外的必要原代数维数至多一。

对每个 $(u_0,Q_0)\in E$，直接特化整个三生成呈示，所得纤维仍是由 $1,T,z$ 生成的有限 $\mathbb C[\lambda]$ 模。它的 Krull 维数至多一，纵使两个六次同时降阶或恒零。由于 $E$ 只有有限多个不同权点，整个 $E$ 上的原纤维并集维数仍至多一。可能的非约化结构不改变这个维数论证；这里没有把 $434$ 当作整个原系统的方案长度。

因此
$$
\dim\operatorname{Spec}\mathcal B\le1.
\tag{13}
$$
所有 $\lambda$ 整纤维和几何根都仍在 (13) 中。它不是零维性，也不是全原理想为单位。

## 6. 完整规范原坐标的有限恢复

为把 (13) 传给完整原点，不能只省略原 Gram 或孤立列自由度。下面给出同点恢复。

先添首一二次
$$
\rho^2=1-Q=\delta,\qquad
b=\frac{\ell}{2}+\frac{(u-\ell)\rho}{2\delta},
\qquad c=\frac{\ell}{2}-\frac{(u-\ell)\rho}{2\delta}.
\tag{14}
$$
此时 $bc=M_n/(4Q\delta)$ 是原单位，故 $b,c$ 均为单位。记
$$
a=1-\ell,\quad p=1+\rho,\quad q=1-\rho,\quad
m=u-\ell,\quad M=M_n/Q,\quad \theta=u-\ell Q .
$$
所有这些都是权坐标的有限或有理恢复，分母均已付。

在 $\Phi=0$ 上，原 $P_1/N_0/E_0$ 的已成恢复是
$$
\begin{aligned}
P_{02}&=2(u-1)L,&P_f&=4(u-1)^2K,&G&=\lambda P_{02}+(u-1)T_0,\\
P_c&=QP_{02}(\ell+T)-GT_0,&
f&=-P_c/P_f,&t&=z/Q,\\
V&=(Jf-G+bc\,z)/Q,&
W_1&=(T_0+4uf)/2 .
\end{aligned}
\tag{15}
$$
于是
$$
x=\frac{\theta V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad
X=x+\rho y,\quad Y=x-\rho y,
\tag{16}
$$
$$
A_1=2f-2V+2bc\,t,\qquad
r=X-ap-ct,\quad s_{\rm Gram}=Y-aq-bt .
\tag{17}
$$
(14)–(17) 恢复整个真正 dual Gram 四行
$$
(0,0,p,q),\quad(0,A_1,r,s_{\rm Gram}),\quad
(p,r,0,t),\quad(q,s_{\rm Gram},t,0).
$$
没有新增自由 Gram 参数。

归一化孤立列写成 $(1,w,h,k)$。其 $w=\lambda-1-T$；记
$h_1=h-1,k_1=k-1$。原两个矩条件为
$$
bh_1+ck_1=T,\qquad
bh_1^2+ck_1^2=A_\lambda,\qquad
A_\lambda=2\lambda^2-2\lambda+1 .
\tag{18}
$$
消去 $k_1$ 给
$$
b\ell\,h_1^2-2bT h_1+T^2-cA_\lambda=0,\qquad
k_1=(T-bh_1)/c .
\tag{19}
$$
因为 $b\ell$ 已付，(19) 是另一条首一二次扩张。全部额外原矩、个别谱条件及完整孤立列条件继续保留；本稿只用 (18) 的必要性建立有限恢复，不声称 (18) 足以替代整个原系统。

故在反演几何 $D$ 前，完整规范原点被 (4) 先添 $\rho$、再添 $h_1$ 的两个首一二次有限扩张覆盖，维数不增加。最后取
$$
D_{\rm phys}=\ell A_\lambda-T^2
=bc(h_1-k_1)^2\ne0
$$
及其他当前原单位开条件，或加入尚未使用的原方程，只会取开子集或闭子集，不会增加维数。这里不声称 $D$ 局部化后仍有限于原权环，也不倒 $D$ 的权范数。由 (13) 得完整固定规范结论 (2)。

## 7. 唯一实际来源与凭据

新源：[2026-11-28-unit211-Phi-zero-corrected-two-sextics-fixed-lambda-resultant-support-8542.py](../notes/2026-11-28-unit211-Phi-zero-corrected-two-sextics-fixed-lambda-resultant-support-8542.py)。

- Git blob：ed0fc44e741f2482f4593b31ab22fa4f773cc241。
- SHA256：39631a64da054107209d296765b755e2fe25a685f5734cb5607165dd39100b7b。
- 唯一实际 run/job：46135498427 / 140949785183；attempt 1；内部退出码 0。
- 源提交与实际 pull：0c059c08cadb206abdd50843c6c7edc7a61309cf。
- 实际规则读取：2026-11-28 10:30:42.810444 UTC；两 README 无变化。
- 数学最后阶段 $2.426502838$ 秒，驱动 $2.470142187$ 秒，最大子进程 RSS $47144$ KiB。
- stdout $3319$ 字节，SHA256 b3378b1c92e0188808fefb28ba6e8032f824bf2da76083ea34f2c84c5c425783。

准确小回执沿用 [本次唯一执行记录](../notes/2026-11-28-unit211-Phi-zero-corrected-two-sextics-fixed-lambda-resultant-support-8542-execution.json)，不另存重复回执或可重算载荷。两个完整依赖源码均在 AST 执行之前核 SHA；数学源只运行本次新固定矩阵目标，限额 $120$ 秒、$1$ GiB、外层 $135$ 秒。

整个正确 $\Phi=0$ 图已经具有 (1)、(2) 的严格约束，仍允许一维原分量。普通 Hilbert 空间不变子空间问题也未由此完成。
