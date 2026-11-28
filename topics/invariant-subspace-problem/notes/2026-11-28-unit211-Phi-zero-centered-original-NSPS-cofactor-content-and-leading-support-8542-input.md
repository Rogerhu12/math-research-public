# Phi 斜率补图：中心后的完整 NS/PS 原两列 cofactor

日期：2026-11-28（Asia/Taipei）。本次是尚未执行的新输入，固定 120 秒 / 1 GiB。

## 1. 原范围与真正新增目标

沿已经完成的
[精确 I10 十八行两列呈示](../results/R150-appendix-unit211-Phi-zero-complete-original-values-exact-eighteen-by-two-presentation.md)
及
[原 N1 斜率补图六行两列定理](../results/R150-appendix-unit211-Phi-zero-original-N1-slope-exact-six-by-two-presentation-and-three-eighth-degree-scalars.md)，保当前原 $\Phi=0,D\ne0$ 图，并仅在明确的斜率 $\Delta_N\ne0$ 上使用两生成元坐标。整个 $\Delta_N=0$ 权面继续保留。

本次不计算旧三个 $\lambda^8$ 标量，也不重新生成十八行的其余原值。只取已成完整 $N_S,P_S$ 的必要原定义，新增一个真实两列 cofactor、它的实际共同乘子取消、完整 $\lambda$ 内容及真实最高系数。无大投影、范数、Gaussian 或旧因式门。

## 2. 不增加单位的中心变化

原 N1 的线性余式为
$$
n=p_0+p_1T+p_2z,\qquad
p_0=e\lambda^2+f\lambda+g,\quad
p_1=a\lambda+b,\quad p_2=c\lambda+d,
$$
其中 $a,b,c,d,e,f,g$ 都是原权量，
$$
\Delta_N=ad-bc,\qquad \mathcal Z=aT+cz.
$$
置
$$
\mathcal X=\mathcal Z+e\lambda+f.
$$
这只是 $A[\lambda]$ 上的平移，不要求 $\lambda\ne0$。模 $n$ 的完整反解是
$$
T=\frac{(c\lambda+d)\mathcal X-de\lambda+cg-df}{\Delta_N},
$$
$$
z=\frac{-(a\lambda+b)\mathcal X+be\lambda+bf-ag}{\Delta_N}.
\tag{1}
$$
实际返回 $\mathcal Z=\mathcal X-e\lambda-f$、$n=0$ 的全部四个系数。特别是 (1) 每个系数对 $\lambda$ 次数至多一。

原首一关系 $\mathcal Z^2=\beta_1\mathcal Z+\beta_0$ 变为
$$
\mathcal X^2=(\beta_1+2h)\mathcal X+
(\beta_0-\beta_1h-h^2),\qquad h=e\lambda+f.
$$
两个新系数对 $\lambda$ 次数均至多二：原三个均值规则的列次数为 $(2,1,1)$，代入 (1) 后即得此上界。源码同时直接检查这两个真正系数。

已成完整 $N_S,P_S$ 的原 $(1,T,z)$ 行次数为 $(3,2,2)$。于是代入 (1)，它们的两个真实系数全部对 $\lambda$ 次数至多三。没有对高次幂反复代入；只在最后一次作坐标变化。

若原三系数行为 $r=(r_0,r_1,r_2)$，新的二系数行为 $(s_0,s_1)$，则
$$
r_0=s_0+s_1h+\kappa p_0,\quad
r_1=as_1+\kappa p_1,\quad
r_2=cs_1+\kappa p_2,\qquad
\kappa=(-cr_1+ar_2)/\Delta_N.
\tag{2}
$$
本次对 $N_S,P_S$ 都返回 (2)，因此仍是同一原理想中的实际来源。

## 3. 真正共乘子取消与完整标量来源

写新二行为 $N=(N_0,N_1)$、$P=(P_0,P_1)$。先以权量公分母 $L$ 清除 $N_1,P_1$ 的分母，构造真正多项式乘子
$$
\mu=LP_1,\qquad \nu=-LN_1.
$$
令 $g_c=\gcd(\mu,\nu)$，对两者逐项精确除法并乘回，得到
$\widehat\mu=\mu/g_c$、$\widehat\nu=\nu/g_c$。
随后直接核
$$
\widehat\mu N+\widehat\nu P=(C,0).
\tag{3}
$$
因此取消的是两个真实乘子的共同因子，且取消后的完整身份 (3) 在其零集上仍成立；没有将一个原方程任意除掉未知因子。

$C$ 的 $\lambda$ 次数至多六。清除它的真实权分母并仅剥已付权因子后，源码还把 (3) 接回 (2)，逐个返回全部三个原系数，得到
$$
\mu_*N_S+\nu_*P_S=C_*+\kappa_*n
 \pmod{(q_R,q_W,q_O)}.
\tag{4}
$$
从而 $C_*$ 是新的原 $I_6$ 标量，而不是只在某个泛型点上的必要值。

接着逐个真实 $\lambda$ 系数作 QQ 权多项式 gcd，精确返回
$$
C_*=\operatorname{cont}_{\lambda}(C_*)\,P_*.
$$
整个未知内容都保留。只有真实已付权因子可以删除。最高系数单独返回、剥已付权因子后保存其完整未付支持；它不自动是单位。若 cofactor 恒等为零，则准确报告此结果，不产生新的排空结论。

## 4. 源与必要前缀

建议源文件：
`2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py`。

源 SHA256：
`baaac1d2cb05437b6c771856aea8991692cad5ff62276e6bce12584d15da8ca6`，
7915 字节。唯一直接依赖是 I10 源：

- `2026-11-28-unit211-Phi-zero-slope-full-original-values-twelve-new-rows-eighteen-two-model-8542.py`，
  SHA256 `527cddc0905e6ab51530b08172fc44c7652926e928de6769603e3a5d037c4c59`。
  可由 `ISP_PHI_I10_SOURCE` 指定。只读到第一次完整 Gram 记录之前的 7782 字节，
  前缀 SHA256 `e65ccba5fe91105a3d2c05d433a19d17b59761f6bc8d1cfffedda7e525f818aa`。
  不进入十二行的保存或其后四个新值条件。

其两件递归依赖保持原规范：

- `2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py`，
  SHA256 `c4af169436165777186a811ccbea1b242b64e0bd84ac14bde43289254c4a2332`，
  由 `ISP_PHI_SLOPE_SOURCE` 指定，只用原 5809 字节坐标前缀；
- `2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，
  SHA256 `100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf`，
  由 `ISP_PHI_FIRST_HEAD_RULE_SOURCE` 指定，只用原 7097 字节规则前缀。

所有嵌套 alarm/setitimer 始终受最初的同一个 120 秒绝对截止约束。输出只含定义、次数、项数、SHA、完整乘回标记及真实执行身份，不存可重算系数、编码载荷或分片。
